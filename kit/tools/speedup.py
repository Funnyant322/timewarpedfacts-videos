"""Tighten pacing: shrink gaps between words to MAXGAP, then speed everything up by SPEED.
Usage: python3 speedup.py in.json out.json [speed] [maxgap]"""
import json, sys, subprocess
R = json.load(open(sys.argv[1])); out = sys.argv[2]
SPEED = float(sys.argv[3]) if len(sys.argv) > 3 else 1.12
MAXGAP = float(sys.argv[4]) if len(sys.argv) > 4 else 0.22
W = json.load(open(R["words"]))["words"]
words = [w for w in W if w["type"] == "word" and not (w["text"].startswith("[") or w["text"].endswith("]"))]
# keep-segments of the original audio
segs = []; prev_end = 0.0
for w in words:
    gap = w["start"] - prev_end
    if gap > MAXGAP:
        # drop the middle of the gap, keep MAXGAP/2 on each side
        segs.append((prev_end + MAXGAP / 2, w["start"] - MAXGAP / 2, "cut"))
    prev_end = max(prev_end, w["end"])
END0 = R.get("end", words[-1]["end"] + 1)
cuts = [(a, b) for a, b, _ in segs if b > a]
def m(t):
    """map original time -> new time"""
    removed = 0.0
    for a, b in cuts:
        if t >= b: removed += b - a
        elif t > a: removed += t - a
    return (t - removed) / SPEED
# build ffmpeg filter: keep intervals
keep = []; cur = 0.0
for a, b in cuts:
    keep.append((cur, a)); cur = b
keep.append((cur, END0))
parts = "".join(f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[k{i}];" for i, (a, b) in enumerate(keep))
cat = "".join(f"[k{i}]" for i in range(len(keep))) + f"concat=n={len(keep)}:v=0:a=1,atempo={SPEED}[o]"
vo = R["voice"].replace(".mp3", "_fast.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", R["voice"], "-filter_complex", parts + cat, "-map", "[o]", vo], check=True)
nw = []
for w in W:
    w = dict(w); w["start"] = m(w["start"]); w["end"] = m(w["end"]); nw.append(w)
wf = R["words"].replace(".json", "_fast.json"); json.dump({"words": nw}, open(wf, "w"))
R["voice"], R["words"], R["end"] = vo, wf, round(m(END0), 2)
for s in R["scenes"]: s["t"] = round(m(s["t"]), 2)
for o in R.get("overlays", []):
    o["start"], o["end"] = round(m(o["start"]), 2), round(m(o["end"]), 2)
    for k in ("msgs", "mails"):
        for x in o.get(k, []): x["t"] = round(m(x["t"]), 2)
    if "times" in o: o["times"] = [round(m(t), 2) for t in o["times"]]
    if "flood" in o: o["flood"] = [round(m(t), 2) for t in o["flood"]]
    if "seen" in o: o["seen"] = round(m(o["seen"]), 2)
for e in R.get("sfx_events", []): e["t"] = round(m(e["t"]), 2)
R["extra_dings"] = [round(m(t), 2) for t in R.get("extra_dings", [])]
json.dump(R, open(out, "w"), indent=1)
print("end", END0, "->", R["end"])
