#!/usr/bin/env python3
"""Render a TimeWarpedFacts Short (1080x1920, 30 fps) from a JSON spec.

Usage: python3 tools/render.py spec.json

spec.json:
{
  "out": "videos/004_slug.mp4",
  "vo": "work/vo.mp3",                 # narration (Jason Steele)
  "music": "work/music.mp3",           # ElevenLabs music bed
  "music_db": -20,                     # music gain in dB (low under the voice)
  "loop_tail": 0.7,                    # seconds of the opening image at the end so the Short loops
  "segments": [                        # in order; times in seconds on the narration timeline
    {"image": "work/01.png", "text": "Things that existed at the same time", "sub": "Your brain won't accept the last one...", "start": 0.0, "end": 3.1},
    {"image": "work/02.png", "text": "Harvard University is older than calculus...", "start": 3.1, "end": 7.4}
  ]
}
The look follows the channel rules: centred image over a blurred copy of itself,
white text with a black outline, slow zoom on every image.
"""
import json, os, subprocess, sys, tempfile, textwrap
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(HERE, "..", "fonts", "Inter-ExtraBold.otf")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-3000:])
        raise SystemExit(f"command failed: {' '.join(cmd[:6])} ...")
    return r.stdout


def duration(path):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path]).strip())


def fg_box(img_path):
    """Size of the centred foreground image: full width, height capped at 1080."""
    w, h = Image.open(img_path).size
    fw = W
    fh = round(W * h / w)
    if fh > 1080:
        fh = 1080
        fw = round(1080 * w / h)
    return fw - fw % 2, fh - fh % 2


def text_overlay(path, text, sub, fg_top):
    """Transparent 1080x1920 PNG with outlined white text near the top of the image."""
    im = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    y = max(fg_top + 36, 300)
    for content, size, stroke, width in ((text, 62, 7, 26), (sub, 40, 5, 38)):
        if not content:
            continue
        font = ImageFont.truetype(FONT, size)
        for line in textwrap.wrap(content, width=width):
            tw = d.textlength(line, font=font)
            d.text(((W - tw) / 2, y), line, font=font, fill="white", stroke_width=stroke, stroke_fill="black")
            y += int(size * 1.18)
        y += 14
    im.save(path)


def _norm(t):
    return "".join(c for c in t.lower() if c.isalnum())


def apply_cues(segs, words):
    """Set each segment's start from its "cue" (the first words of that beat in the narration).

    words: ElevenLabs Scribe word list [{text,start,end,type}] (a dict with "words" also works).
    Cues are matched in order, so a repeated phrase later in the script is found correctly."""
    if isinstance(words, dict):
        words = words.get("words", [])
    ws = [w for w in words if w.get("type", "word") == "word" and not w["text"].startswith("[")]
    toks = [_norm(w["text"]) for w in ws]
    pos = 0
    for i, s in enumerate(segs):
        cue = [_norm(x) for x in s.get("cue", "").split() if _norm(x)]
        if not cue:
            if "start" not in s:
                raise SystemExit(f"segment {i} has neither cue nor start")
            continue
        for j in range(pos, len(toks) - len(cue) + 1):
            if toks[j:j + len(cue)] == cue:
                s["start"] = max(0.0, ws[j]["start"] - 0.08)
                pos = j + len(cue)
                break
        else:
            raise SystemExit(f"cue not found in narration: {s['cue']!r}")
    for i, s in enumerate(segs):
        s.setdefault("end", segs[i + 1]["start"] if i + 1 < len(segs) else 0)


def render_segment(seg, dur, out, tmp, idx):
    img = seg["image"]
    fw, fh = fg_box(img)
    fg_top = (H - fh) // 2
    ov = os.path.join(tmp, f"text_{idx}.png")
    text_overlay(ov, seg.get("text", ""), seg.get("sub", ""), fg_top)
    frames = max(1, round(dur * FPS))
    zoom = 0.07  # slow push-in over the segment
    fc = (
        f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=28:2,eq=brightness=-0.12,setsar=1[bg];"
        f"[0:v]scale={fw*3}:{fh*3},zoompan=z='1+{zoom}*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={fw}x{fh}:fps={FPS}[fg];"
        f"[bg][fg]overlay=(W-w)/2:(H-h)/2[v1];[v1][1:v]overlay=0:0,format=yuv420p[v]"
    )
    run(["ffmpeg", "-y", "-v", "error", "-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.3f}", "-i", img,
         "-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.3f}", "-i", ov,
         "-filter_complex", fc, "-map", "[v]", "-frames:v", str(frames), "-r", str(FPS),
         "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", out])


def main():
    spec_path = sys.argv[1]
    spec = json.load(open(spec_path))
    base = os.path.dirname(os.path.abspath(spec_path))
    p = lambda x: x if os.path.isabs(x) else os.path.join(base, x)
    segs = spec["segments"]
    for s in segs:
        s["image"] = p(s["image"])
    if spec.get("words"):
        apply_cues(segs, json.load(open(p(spec["words"]))))
    vo, music, out = p(spec["vo"]), p(spec["music"]), p(spec["out"])
    vo_len = duration(vo)
    tail = float(spec.get("loop_tail", 0.7))
    # last segment runs to the end of the narration (+ a beat), then the opening image returns for the loop
    segs[-1]["end"] = max(segs[-1]["end"], vo_len + 0.3)
    segs[0]["start"] = 0.0
    total = segs[-1]["end"] + tail
    if not 25 <= total <= 60:
        print(f"WARNING: total length {total:.1f}s is outside 25-60s")

    tmp = tempfile.mkdtemp(prefix="twf_")
    parts = []
    for i, s in enumerate(segs):
        end = segs[i + 1]["start"] if i + 1 < len(segs) else s["end"]
        dur = end - s["start"]
        if dur <= 0.2:
            raise SystemExit(f"segment {i} too short ({dur:.2f}s)")
        part = os.path.join(tmp, f"seg_{i:02d}.mp4")
        render_segment(s, dur, part, tmp, i)
        parts.append(part)
    # loop tail: the opening image with the opening text, so the end flows back into the start
    part = os.path.join(tmp, "seg_tail.mp4")
    render_segment(segs[0], tail, part, tmp, 99)
    parts.append(part)

    lst = os.path.join(tmp, "list.txt")
    with open(lst, "w") as f:
        f.writelines(f"file '{x}'\n" for x in parts)
    silent = os.path.join(tmp, "video.mp4")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", silent])

    mdb = float(spec.get("music_db", -20))
    fc = (
        f"[1:a]apad=whole_dur={total:.3f}[vo];"
        f"[2:a]aloop=loop=-1:size=2e9,atrim=0:{total:.3f},volume={mdb}dB,afade=t=in:d=0.4,afade=t=out:st={total-0.6:.3f}:d=0.6[m];"
        f"[vo][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[a]"
    )
    os.makedirs(os.path.dirname(out), exist_ok=True)
    run(["ffmpeg", "-y", "-v", "error", "-i", silent, "-i", vo, "-i", music, "-filter_complex", fc,
         "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}",
         "-movflags", "+faststart", out])
    print(json.dumps({"out": out, "duration": round(duration(out), 2), "bytes": os.path.getsize(out)}))


if __name__ == "__main__":
    main()
