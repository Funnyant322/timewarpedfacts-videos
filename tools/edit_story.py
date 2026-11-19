#!/usr/bin/env python3
"""Edit an animated story Short (Zack D.-style) from AI video clips + narration.

Usage: python3 tools/edit_story.py spec.json

spec.json:
{
  "out": "videos/s001_microwave.mp4",
  "vo": "work/x/vo.mp3",
  "words": "work/x/words.json",          # ElevenLabs Scribe word timings
  "music": "music/03_clockwork_discovery.mp3",
  "music_db": -24,
  "tail": 0.6,                            # seconds of picture after the last word
  "clips": [                              # in order; each starts at its cue on the narration timeline
    {"video": "work/x/v1.mp4", "cue": "In 1945"},
    {"video": "work/x/v2.mp4", "cue": "when he felt"}
  ]
}
Each clip fills the time until the next clip's cue. Clips that are too short are slowed down
(never below 0.6x); longer ones are trimmed from the start. Captions: one big word at a time,
white with a thick black outline, in the lower-middle of the frame, timed from the word list.
"""
import json, os, subprocess, sys, tempfile

W, H, FPS = 1080, 1920, 30
HERE = os.path.dirname(os.path.abspath(__file__))
FONTDIR = os.path.join(HERE, "..", "fonts")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stderr[-3000:])
        raise SystemExit("command failed: " + " ".join(cmd[:8]))
    return r.stdout


def dur(p):
    return float(run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p]).strip())


def norm(t):
    return "".join(c for c in t.lower() if c.isalnum())


def load_words(path):
    d = json.load(open(path))
    ws = d["words"] if isinstance(d, dict) else d
    return [w for w in ws if w.get("type", "word") == "word" and not w["text"].startswith("[")]


def find_cues(clips, words):
    toks = [norm(w["text"]) for w in words]
    pos = 0
    for c in clips:
        cue = [norm(x) for x in c["cue"].split() if norm(x)]
        for j in range(pos, len(toks) - len(cue) + 1):
            if toks[j:j + len(cue)] == cue:
                c["start"] = 0.0 if not clips.index(c) else max(0.0, words[j]["start"] - 0.05)
                pos = j + len(cue)
                break
        else:
            raise SystemExit(f"cue not found: {c['cue']!r}")


def ass_time(t):
    h = int(t // 3600); m = int(t % 3600 // 60); s = t % 60
    return f"{h}:{m:02d}:{s:05.2f}"


def write_ass(words, path, total):
    head = (
        "[Script Info]\nScriptType: v4.00+\nPlayResX: 1080\nPlayResY: 1920\nWrapStyle: 2\n\n"
        "[V4+ Styles]\nFormat: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, "
        "Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, "
        "MarginL, MarginR, MarginV, Encoding\n"
        "Style: Cap,Inter ExtraBold,112,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,7,3,2,60,60,560,1\n\n"
        "[Events]\nFormat: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n")
    lines = []
    for i, w in enumerate(words):
        s = w["start"]
        e = words[i + 1]["start"] if i + 1 < len(words) else min(w["end"] + 0.4, total)
        e = max(e, s + 0.12)
        txt = w["text"].strip().strip('"')
        # little pop-in: start at 85% size, settle to 100% in 80 ms
        lines.append(f"Dialogue: 0,{ass_time(s)},{ass_time(e)},Cap,,0,0,0,,{{\\fscx85\\fscy85\\t(0,80,\\fscx100\\fscy100)}}{txt}")
    open(path, "w").write(head + "\n".join(lines) + "\n")


def main():
    spec_path = sys.argv[1]
    spec = json.load(open(spec_path))
    base = os.path.dirname(os.path.abspath(spec_path))
    p = lambda x: x if os.path.isabs(x) else os.path.normpath(os.path.join(base, x))
    words = load_words(p(spec["words"]))
    vo = p(spec["vo"]); out = p(spec["out"])
    total = dur(vo) + float(spec.get("tail", 0.6))
    clips = spec["clips"]
    find_cues(clips, words)
    tmp = tempfile.mkdtemp(prefix="story_")
    parts = []
    for i, c in enumerate(clips):
        end = clips[i + 1]["start"] if i + 1 < len(clips) else total
        need = end - c["start"]
        src = p(c["video"])
        have = dur(src)
        factor = max(1.0, need / have)
        if need / have > 1 / 0.6:
            print(f"WARNING: clip {i} slowed to {have/need:.2f}x")
        part = os.path.join(tmp, f"p{i:02d}.mp4")
        vf = (f"setpts={factor:.4f}*PTS,scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
              f"fps={FPS},format=yuv420p")
        run(["ffmpeg", "-y", "-v", "error", "-i", src, "-an", "-vf", vf, "-t", f"{need:.3f}",
             "-c:v", "libx264", "-preset", "medium", "-crf", "18", part])
        parts.append(part)
    lst = os.path.join(tmp, "l.txt")
    open(lst, "w").writelines(f"file '{x}'\n" for x in parts)
    joined = os.path.join(tmp, "joined.mp4")
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", joined])
    ass = os.path.join(tmp, "caps.ass")
    write_ass(words, ass, total)
    mdb = float(spec.get("music_db", -24))
    fc = (f"[0:v]subtitles={ass}:fontsdir={FONTDIR}[v];"
          f"[1:a]apad=whole_dur={total:.3f}[vo];"
          f"[2:a]aloop=loop=-1:size=2e9,atrim=0:{total:.3f},volume={mdb}dB,afade=t=out:st={total-0.8:.3f}:d=0.8[m];"
          f"[vo][m]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11,aresample=44100[a]")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    run(["ffmpeg", "-y", "-v", "error", "-i", joined, "-i", vo, "-i", p(spec["music"]), "-filter_complex", fc,
         "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p",
         "-c:a", "aac", "-b:a", "192k", "-t", f"{total:.3f}", "-movflags", "+faststart", out])
    print(json.dumps({"out": out, "duration": round(dur(out), 2), "bytes": os.path.getsize(out)}))


if __name__ == "__main__":
    main()
