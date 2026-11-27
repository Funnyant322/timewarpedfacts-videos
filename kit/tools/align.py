"""Free word timings: split script into phrases at punctuation, match them to speech segments
found by silence detection, spread words inside each phrase by letter count.
usage: python3 align.py voice.mp3 "script text" out_words.json"""
import sys, re, json, subprocess
mp3, text, out = sys.argv[1:4]
def segs(noise, dur):
    r = subprocess.run(["ffmpeg","-i",mp3,"-af",f"silencedetect=noise={noise}dB:d={dur}","-f","null","-"],capture_output=True,text=True).stderr
    total = float(re.search(r"Duration: (\d+):(\d+):([\d.]+)", r).groups()[2]) + 60*int(re.search(r"Duration: (\d+):(\d+)", r).group(2))
    ss = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r)]; se = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r)]
    out=[]; cur=0.0
    for a,b in zip(ss,se+[total]):
        if a-cur>0.08: out.append((cur,a))
        cur=b
    if total-cur>0.08: out.append((cur,total))
    return out
words = text.split()
phrases=[]; cur=[]
for w in words:
    cur.append(w)
    if re.search(r'[.?!,…]["”]?$|\.\.\.$', w): phrases.append(cur); cur=[]
if cur: phrases.append(cur)
best=None
for noise in (-35,-32,-38,-30,-40):
    for d in (0.18,0.14,0.22,0.12,0.28):
        s=segs(noise,d)
        if best is None or abs(len(s)-len(phrases))<abs(len(best)-len(phrases)): best=s
        if len(s)==len(phrases): break
    if len(best)==len(phrases): break
s=best
if len(s)!=len(phrases):
    # merge/split: fall back to one block spread over all speech by phrase letter share
    st,en=s[0][0],s[-1][1]; tot=sum(len("".join(p)) for p in phrases); t=st; s=[]
    for p in phrases:
        L=(en-st)*len("".join(p))/tot; s.append((t,t+L*0.92)); t+=L
res=[]
for (a,b),p in zip(s,phrases):
    tot=sum(len(w)+1 for w in p); t=a
    for w in p:
        L=(b-a)*(len(w)+1)/tot; res.append({"text":w,"type":"word","start":round(t,3),"end":round(t+L,3)}); t+=L
json.dump({"words":res},open(out,"w"),indent=1)
print("phrases",len(phrases),"segments",len(best),"end",res[-1]["end"])
