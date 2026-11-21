"""Every Type Of ... video engine. Usage: python3 engine.py recipe.json [t1 t2 ...]  (times = test frames)"""
import json, subprocess, math, sys, wave, struct, random, glob, os
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
G = "/usr/share/fonts/truetype/google-fonts/ofl/"
def mont(size, style="Bold"):
    f = ImageFont.truetype(G + "montserrat/Montserrat[wght].ttf", size); f.set_variation_by_name(style); return f
SUB_F = ImageFont.truetype((glob.glob(G + "comicrelief/*Bold*.ttf") or glob.glob(G + "comicrelief/*.ttf"))[0], 52)
BUB_F = ImageFont.truetype((glob.glob(G + "comicrelief/*Bold*.ttf") or glob.glob(G + "comicrelief/*.ttf"))[0], 34)
TITLE_F, FOOT_F = mont(58, "Bold"), mont(44, "Bold")
PH_F, PH_SMALL, PH_NAME, PH_TINY = mont(25, "SemiBold"), mont(20, "Medium"), mont(25, "Bold"), mont(19, "SemiBold")
PH_F2 = mont(21, "SemiBold"); IN_NAME, IN_SUBJ = mont(28, "Bold"), mont(22, "Medium")
SX, SY, SW, SH = 0, 285, 1080, 1350
TALL = True
AV = {"Sam": (60, 170, 150), "Leo": (232, 140, 50), "Maya": (200, 90, 160), "Jay": (90, 120, 220), "Boss": (90, 90, 90), "You": (10, 132, 255)}

def trim(im):
    """Remove a plain light border/frame, then fit to the scene area shape."""
    import numpy as np
    a = np.array(im).astype(int); c = a[2, 2]
    corners = [a[2, 2], a[2, -3], a[-3, 2], a[-3, -3]]
    if c.sum() > 600 and all(abs(x - c).sum() < 30 for x in corners):
        diff = np.abs(a - c).sum(2) > 40
        rows = np.where(diff.mean(1) > 0.5)[0]; cols = np.where(diff.mean(0) > 0.5)[0]
        if len(rows) and len(cols):
            x0, x1, y0, y1 = cols.min() + 4, cols.max() - 4, rows.min() + 4, rows.max() - 4
            if (x1 - x0) > im.width * 0.6 and (y1 - y0) > im.height * 0.6:
                im = im.crop((x0, y0, x1, y1))
    w, h = im.size; target = SW / SH
    if w / h > target + 0.01:
        # too wide: keep everything, extend the top/bottom edge colours instead of cutting the sides
        nh = int(w / target); pad = nh - h; top = pad // 2
        out = Image.new("RGB", (w, nh))
        out.paste(im.crop((0, 0, w, 1)).resize((w, top)), (0, 0))
        out.paste(im, (0, top))
        out.paste(im.crop((0, h - 1, w, h)).resize((w, nh - top - h)), (0, top + h))
        im = out
    elif w / h < target - 0.01:
        nh = int(w / target); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    return im

def ease(p): return 0.5 - 0.5 * math.cos(math.pi * max(0, min(1, p)))

class Video:
    def __init__(self, R):
        self.R = R
        raw = [w for w in json.load(open(R["words"]))["words"] if w["type"] == "word"]
        self.words = [w for w in raw if not (w["text"].startswith("[") or w["text"].endswith("]"))]
        self.END = R.get("end", self.words[-1]["end"] + 1.0)
        self.imgs = {s["img"]: trim(Image.open(f"img/{s['img']}.png").convert("RGB")) for s in R["scenes"]}
        chunks, cur = [], []
        for w in self.words:
            cur.append(w)
            if len(cur) >= 5 or (len(cur) >= 2 and w["text"][-1] in ".,?:!…\""):
                chunks.append(cur); cur = []
        if cur: chunks.append(cur)
        self.chunks = chunks

    # ---------- overlays ----------
    def phone(self, ov, t):
        pw, ph = 380, 560
        im = Image.new("RGBA", (pw, ph), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, pw - 1, ph - 1), 46, fill=(25, 25, 28), outline=(0, 0, 0), width=4)
        d.rounded_rectangle((14, 14, pw - 15, ph - 15), 36, fill=(250, 250, 250))
        shown = [m for m in ov["msgs"] if m["t"] <= t]
        d.text((44, 30), (shown[-1].get("clock") if shown and shown[-1].get("clock") else ov.get("clock", "9:41")), font=PH_SMALL, fill=(30, 30, 30))
        d.rounded_rectangle((pw // 2 - 50, 26, pw // 2 + 50, 50), 12, fill=(25, 25, 28))
        d.line((14, 108, pw - 15, 108), fill=(220, 220, 220), width=2)
        title = ov.get("title", "Chat")
        d.ellipse((30, 62, 70, 102), fill=AV.get(ov.get("title_av", title), (150, 150, 150)))
        d.text((50, 82), title[0], font=PH_NAME, fill="white", anchor="mm")
        d.text((84, 82), title, font=PH_NAME, fill=(20, 20, 20), anchor="lm")
        group = ov.get("group", False)
        rows = shown[-6:]; y = 122
        for m in rows:
            pop = min(1.0, (t - m["t"]) / 0.18)
            if m.get("note"):
                d.text((pw / 2, y + 14), m["note"], font=PH_TINY, fill=(140, 140, 140), anchor="mm"); y += 34; continue
            who, txt = m["from"], m.get("text", "")
            if m.get("voice"):
                me = who == ov.get("me")
                if group and not me:
                    d.text((70, y + 2), who, font=PH_TINY, fill=AV.get(who, (120, 120, 120)), anchor="lt"); y += 22
                    d.ellipse((28, y + 8, 62, y + 42), fill=AV.get(who, (150, 150, 150)))
                bw2, bh2 = 270, 54; x0 = (70 if group else 30) if not me else pw - 30 - bw2
                col = (229, 229, 234) if not me else (10, 132, 255)
                s_ = 0.6 + 0.4 * pop; cx = x0 + bw2 / 2
                d.rounded_rectangle((cx - bw2 * s_ / 2, y, cx + bw2 * s_ / 2, y + bh2 * s_), 25, fill=col)
                if pop >= 1:
                    d.polygon([(x0 + 18, y + 15), (x0 + 18, y + 39), (x0 + 38, y + 27)], fill=(40, 40, 40))
                    random.seed(11)
                    for i in range(26):
                        hh = random.randint(4, 18); xx = x0 + 48 + i * 6
                        d.line((xx, y + 27 - hh, xx, y + 27 + hh), fill=(90, 90, 90), width=3)
                    d.text((x0 + bw2 - 14, y + 27), m["voice"], font=PH_TINY, fill=(60, 60, 60), anchor="rm")
                y += bh2 + 12; continue
            me = who == ov.get("me")
            fnt = PH_F if d.textlength(txt, font=PH_F) + 36 <= pw - 100 else PH_F2
            tw = d.textlength(txt, font=fnt); bw, bh = tw + 36, 50
            if group and not me:
                d.text((70, y + 2), who, font=PH_TINY, fill=AV.get(who, (120, 120, 120)), anchor="lt"); y += 22
            if me: x0, col, tc = pw - 30 - bw, (10, 132, 255), (255, 255, 255)
            else:
                x0, col, tc = (70 if group else 30), (229, 229, 234), (20, 20, 20)
                if group: d.ellipse((28, y + 8, 62, y + 42), fill=AV.get(who, (150, 150, 150)))
            s = 0.6 + 0.4 * pop; cx = x0 + bw / 2
            d.rounded_rectangle((cx - bw * s / 2, y, cx + bw * s / 2, y + bh * s), 23, fill=col)
            if pop >= 1: d.text((x0 + 18, y + bh / 2), txt, font=fnt, fill=tc, anchor="lm")
            y += bh + 12
        if ov.get("seen") and t >= ov["seen"]:
            d.text((pw - 34, y), "Seen by everyone", font=PH_TINY, fill=(120, 120, 120), anchor="rt")
        return im

    def inbox(self, ov, t):
        bw, bh = 560, 520
        im = Image.new("RGBA", (bw, bh), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
        d.rounded_rectangle((0, 0, bw - 1, bh - 1), 18, fill=(255, 255, 255), outline=(30, 30, 30), width=4)
        d.rounded_rectangle((4, 4, bw - 5, 64), 14, fill=(66, 103, 178))
        shown = [m for m in ov["mails"] if m["t"] <= t]
        d.text((24, 34), "Inbox", font=PH_NAME, fill="white", anchor="lm")
        n = len(shown) + sum(m.get("burst", 0) for m in shown if False)
        extra = 0
        if ov.get("flood") and t >= ov["flood"][0]:
            extra = int((min(t, ov["flood"][1]) - ov["flood"][0]) * 14)
        cnt = len(shown) + extra
        if cnt:
            d.rounded_rectangle((bw - 110, 18, bw - 20, 52), 17, fill=(230, 60, 60))
            d.text((bw - 65, 35), str(cnt), font=PH_NAME, fill="white", anchor="mm")
        rows = list(reversed(shown))
        if extra:
            rows = [{"from": "Everyone", "subj": "RE: RE: RE: Office closed Friday"}] * min(extra, 6) + rows
        y = 76
        for m in rows[:7]:
            d.ellipse((18, y + 8, 58, y + 48), fill=AV.get(m["from"], (150, 150, 150)))
            d.text((38, y + 28), m["from"][0], font=PH_NAME, fill="white", anchor="mm")
            d.text((72, y + 2), m["from"], font=IN_NAME, fill=(20, 20, 20))
            d.text((72, y + 34), m["subj"][:34], font=IN_SUBJ, fill=(70, 70, 70))
            d.line((16, y + 60, bw - 16, y + 60), fill=(225, 225, 225), width=2)
            y += 64
        return im

    def bubble(self, ov, t, crop):
        d = ImageDraw.Draw(crop)
        x, y = ov["x"] * SW, ov["y"] * SH
        tw = d.textlength(ov["text"], font=BUB_F); pop = min(1, (t - ov["start"]) / 0.15)
        w2, h2 = (tw / 2 + 26) * (0.7 + 0.3 * pop), 36 * (0.7 + 0.3 * pop)
        tx, ty = ov.get("tail", (x - 40, y + 70))
        d.polygon([(x - 34, y + 24), (x + 34, y + 24), (tx * SW if tx <= 1 else tx, ty * SH if ty <= 1 else ty)], fill="white", outline="black")
        d.rounded_rectangle((x - w2, y - h2, x + w2, y + h2), 30, fill="white", outline="black", width=4)
        if pop >= 1: d.text((x, y), ov["text"], font=BUB_F, fill="black", anchor="mm")

    def plates(self, ov, t, crop):
        d = ImageDraw.Draw(crop)
        k = sum(1 for tt in ov["times"] if t >= tt)
        n = 1 if k == 1 else (2 if k == 2 else (0 if k == 0 else min(14, 3 + int((t - ov["times"][2]) * 20))))
        bx, by = ov["x"] * SW, ov["y"] * SH
        for i in range(n):
            yy = by - i * 22
            d.ellipse((bx - 90, yy - 16, bx + 90, yy + 16), fill="white", outline="black", width=4)
            d.ellipse((bx - 50, yy - 8, bx + 50, yy + 8), outline=(180, 180, 180), width=3)

    def banner(self, ov, t, crop):
        app = ease(min((t - ov["start"]) / 0.3, (ov["end"] - t) / 0.3, 1))
        bw, bh = 640, 96; x = (SW - bw) // 2; y = int(-bh + app * (bh + 20))
        d = ImageDraw.Draw(crop)
        d.rounded_rectangle((x, y, x + bw, y + bh), 22, fill=(245, 245, 245), outline=(40, 40, 40), width=3)
        d.ellipse((x + 18, y + 22, x + 70, y + 74), fill=AV.get(ov.get("who", "Leo")))
        d.text((x + 44, y + 48), ov.get("who", "Leo")[0], font=PH_NAME, fill="white", anchor="mm")
        d.text((x + 88, y + 30), ov.get("app", "Instagram"), font=PH_TINY, fill=(110, 110, 110), anchor="lm")
        d.text((x + 88, y + 62), ov["text"], font=PH_F, fill=(20, 20, 20), anchor="lm")

    # ---------- frame ----------
    def frame(self, t):
        R = self.R; c = Image.new("RGB", (W, H), (0, 0, 0))
        sc = R["scenes"]; k = max(i for i, s in enumerate(sc) if t >= s["t"])
        s = sc[k]; s1 = sc[k + 1]["t"] if k + 1 < len(sc) else self.END
        p = (t - s["t"]) / max(0.01, s1 - s["t"])
        z0, z1 = s.get("zoom", [1.0, 1.08]); z = z0 + (z1 - z0) * ease(p)
        if t - s["t"] < 0.15 and k > 0: z *= 1.05 - 0.05 * (t - s["t"]) / 0.15
        fx, fy = s.get("focus", [0.5, 0.5])
        if "pan" in s: fx = s["pan"][0] + (s["pan"][1] - s["pan"][0]) * ease(p)
        if "tilt" in s: fy = s["tilt"][0] + (s["tilt"][1] - s["tilt"][0]) * ease(p)
        im = self.imgs[s["img"]]; cw, ch = im.width / z, im.height / z
        cx = min(max(fx * im.width, cw / 2), im.width - cw / 2); cy = min(max(fy * im.height, ch / 2), im.height - ch / 2)
        crop = im.crop((int(cx - cw / 2), int(cy - ch / 2), int(cx + cw / 2), int(cy + ch / 2))).resize((SW, SH), Image.LANCZOS)
        for ov in R.get("overlays", []):
            if not (ov["start"] <= t < ov["end"]): continue
            if ov["type"] in ("phone", "inbox"):
                app = min((t - ov["start"]) / 0.35, (ov["end"] - t) / 0.25, 1)
                o = self.phone(ov, t) if ov["type"] == "phone" else self.inbox(ov, t)
                sc_ = ov.get("scale", 0.92); o = o.resize((int(o.width * sc_), int(o.height * sc_)), Image.LANCZOS)
                off = int((1 - ease(app)) * 700)
                x = int(ov.get("x", SW - o.width - 70)) if ov.get("side", "right") == "right" else 70
                crop.paste(o, (x, 300 + off), o)
            elif ov["type"] == "bubble": self.bubble(ov, t, crop)
            elif ov["type"] == "plates": self.plates(ov, t, crop)
            elif ov["type"] == "banner": self.banner(ov, t, crop)
            elif ov["type"] == "card":
                dd = ImageDraw.Draw(crop); pop = min(1, (t - ov["start"]) / 0.15)
                cf = TITLE_F
                for sz in (58, 52, 46, 40, 36):
                    cf = mont(sz, "Bold")
                    if dd.textlength(ov["text"], font=cf) <= SW - 120: break
                tw = dd.textlength(ov["text"], font=cf) * (0.8 + 0.2 * pop)
                cx, cy = SW / 2, ov.get("y", 0.5) * SH
                dd.rounded_rectangle((cx - tw / 2 - 30, cy - 50, cx + tw / 2 + 30, cy + 50), 14, fill="white", outline="black", width=5)
                if pop >= 1: dd.text((cx, cy), ov["text"], font=cf, fill="black", anchor="mm")
        c.paste(crop, (SX, SY)); d = ImageDraw.Draw(c)
        lines = R["title"]; top = SY + 90
        for i, line in enumerate(lines):
            tw = d.textlength(line, font=TITLE_F); y = top + i * 80
            d.rounded_rectangle(((W - tw) / 2 - 22, y - 37, (W + tw) / 2 + 22, y + 39), 10, fill="white")
            d.text((W / 2, y), line, font=TITLE_F, fill="black", anchor="mm")
        for i, line in enumerate(R.get("footer", ["Follow for", "Part 2"])):
            tw = d.textlength(line, font=FOOT_F); y = SY + SH - 230 + i * 66
            d.rounded_rectangle(((W - tw) / 2 - 18, y - 30, (W + tw) / 2 + 18, y + 32), 10, fill="white")
            d.text((W / 2, y), line, font=FOOT_F, fill="black", anchor="mm")
        for chn in self.chunks:
            if chn[0]["start"] - 0.05 <= t <= chn[-1]["end"] + 0.25:
                txt = " ".join(w["text"] for w in chn).replace("…", "...").lower()
                d.text((W / 2, SY + SH * 0.73), txt, font=SUB_F, fill="white", anchor="mm", stroke_width=5, stroke_fill="black")
                break
        return c

    # ---------- sound ----------
    def sfx(self, path):
        sr = 44100; n = int(self.END * sr); buf = [0.0] * n
        def add(t0, smp, g=1.0):
            i0 = int(t0 * sr)
            for i, v in enumerate(smp):
                if 0 <= i0 + i < n: buf[i0 + i] += v * g
        def tone(freqs, dur=0.35, decay=9, amp=0.22):
            out = [0.0] * int((dur + 0.1 * len(freqs)) * sr)
            for j, f in enumerate(freqs):
                st = int(j * 0.09 * sr)
                for i in range(int(dur * sr)):
                    tt = i / sr; out[st + i] += amp * math.sin(2 * math.pi * f * tt) * math.exp(-tt * decay)
            return out
        def whoosh(L=0.28, seed=1):
            random.seed(seed); out = []; prev = 0; N = int(L * sr)
            for i in range(N):
                prev = prev * 0.92 + (random.random() * 2 - 1) * 0.08; out.append(prev * math.sin(math.pi * i / N) * 0.5)
            return out
        def pop(): return tone([660], 0.12, 30, 0.25)
        ding, wh = tone([1318.5, 1760]), whoosh()
        for s in self.R["scenes"][1:]:
            if s["img"] != "SAME": add(s["t"] - 0.12, wh)
        for ov in self.R.get("overlays", []):
            if ov["type"] in ("phone", "inbox"): add(ov["start"], wh)
            for m in ov.get("msgs", []) + ov.get("mails", []):
                if not m.get("note"): add(m["t"], ding)
            if ov["type"] in ("bubble", "card"): add(ov["start"], pop())
            if ov["type"] == "banner": add(ov["start"], ding)
            if ov["type"] == "plates":
                for tt in ov["times"]: add(tt, tone([520, 780], 0.2, 14, 0.2))
            if ov.get("flood"):
                tt = ov["flood"][0]
                while tt < ov["flood"][1]: add(tt, ding, 0.6); tt += 0.18
        for tt in self.R.get("extra_dings", []): add(tt, ding)
        def crinkle(dur):
            random.seed(7); out = [0.0] * int(dur * sr); i = 0
            while i < len(out):
                L = random.randint(60, 400); a = random.uniform(0.1, 0.45)
                for j in range(L):
                    if i + j < len(out): out[i + j] += (random.random() * 2 - 1) * a * math.exp(-j / (L / 3))
                i += L + random.randint(100, 2500)
            return out
        def crunch():
            random.seed(3); out = []; prev = 0
            for i in range(int(0.22 * sr)):
                prev = prev * 0.6 + (random.random() * 2 - 1) * 0.4
                out.append(prev * 0.9 * math.exp(-i / (0.05 * sr)) * (1 if random.random() > 0.3 else 0.3))
            return out
        def boom():
            out = []
            random.seed(5); prev = 0
            for i in range(int(1.2 * sr)):
                prev = prev * 0.985 + (random.random() * 2 - 1) * 0.06
                out.append((prev * 3 + 0.5 * math.sin(2 * math.pi * 55 * i / sr)) * math.exp(-i / (0.35 * sr)))
            return out
        for e in self.R.get("sfx_events", []):
            k = e["kind"]
            if k == "crinkle": add(e["t"], crinkle(e.get("dur", 1.0)), e.get("gain", 0.6))
            elif k == "crunch": add(e["t"], crunch(), e.get("gain", 0.8))
            elif k == "boom": add(e["t"], boom(), e.get("gain", 0.6))
            elif k == "ding": add(e["t"], ding, e.get("gain", 1.0))
            elif k == "pop": add(e["t"], pop(), e.get("gain", 1.0))
            elif k == "smash": add(e["t"], crunch(), 1.0); add(e["t"] + 0.05, tone([2600, 3100, 2200], 0.4, 6, 0.12))
            elif k == "sad": add(e["t"], tone([392, 370, 349, 330], 0.45, 4, 0.18))
            elif k == "cheer": add(e["t"], tone([523, 659, 784, 1047], 0.3, 6, 0.18))
        with wave.open(path, "w") as wf:
            wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr)
            wf.writeframes(b"".join(struct.pack("<h", int(max(-1, min(1, v)) * 32767)) for v in buf))

    def render(self, out):
        self.sfx(out + ".sfx.wav")
        ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                               "-i", self.R["voice"], "-i", out + ".sfx.wav",
                               "-filter_complex", "[1:a]apad[v];[v][2:a]amix=inputs=2:duration=longest:normalize=0,loudnorm=I=-14:TP=-1.5[a]",
                               "-map", "0:v", "-map", "[a]", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p",
                               "-c:a", "aac", "-b:a", "192k", "-t", str(self.END), "-movflags", "+faststart", out], stdin=subprocess.PIPE)
        for i in range(int(self.END * FPS)): ff.stdin.write(self.frame(i / FPS).tobytes())
        ff.stdin.close(); ff.wait(); os.remove(out + ".sfx.wav")

if __name__ == "__main__":
    R = json.load(open(sys.argv[1])); v = Video(R)
    if len(sys.argv) > 2:
        for t in map(float, sys.argv[2:]): v.frame(t).save(f"check_{R['out']}_{t:05.1f}.jpg", quality=85)
    else:
        v.render(R["out"] + ".mp4"); print("done", R["out"])
