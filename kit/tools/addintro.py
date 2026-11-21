"""Prepend a short spoken title clip to a (sped-up) recipe.
Usage: python3 addintro.py in_f.json intro.mp3 out.json "Every type of friend, part three!"
Trims silence from the clip, puts it first, shifts every time in the recipe by its length,
and adds the title words as subtitles. The first scene is held for the intro."""
import json, sys, subprocess
R = json.load(open(sys.argv[1])); clip = sys.argv[2]; out = sys.argv[3]; text = sys.argv[4]
trim = clip.replace(".mp3", "_trim.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", clip, "-af",
                "silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,atempo=1.08",
                trim], check=True)
D = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", trim],
                         capture_output=True, text=True).stdout) + 0.12
voice = R["voice"].replace(".wav", "_intro.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", trim, "-i", R["voice"], "-filter_complex",
                f"[0:a]apad=pad_dur=0.12[a];[a][1:a]concat=n=2:v=0:a=1[o]", "-map", "[o]", voice], check=True)
W = json.load(open(R["words"]))["words"]
for w in W: w["start"] += D; w["end"] += D
toks = text.split(); step = (D - 0.12) / len(toks)
intro = [{"text": t, "type": "word", "start": i * step, "end": (i + 1) * step} for i, t in enumerate(toks)]
wf = R["words"].replace(".json", "_intro.json"); json.dump({"words": intro + W}, open(wf, "w"))
sh = lambda t: round(t + D, 2)
for s in R["scenes"][1:]: s["t"] = sh(s["t"])
for o in R.get("overlays", []):
    o["start"], o["end"] = sh(o["start"]), sh(o["end"])
    for k in ("msgs", "mails"):
        for x in o.get(k, []): x["t"] = sh(x["t"])
    if "times" in o: o["times"] = [sh(t) for t in o["times"]]
    if "flood" in o: o["flood"] = [sh(t) for t in o["flood"]]
    if "seen" in o: o["seen"] = sh(o["seen"])
for e in R.get("sfx_events", []): e["t"] = sh(e["t"])
R["extra_dings"] = [sh(t) for t in R.get("extra_dings", [])]
R["voice"], R["words"], R["end"] = voice, wf, sh(R["end"])
json.dump(R, open(out, "w"), indent=1)
print("intro", round(D, 2), "end", R["end"])
