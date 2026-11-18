# TimeWarpedFacts videos

Public hosting for the TimeWarpedFacts YouTube Shorts ("facts that distort your perception of time").
Metricool pulls each video from its raw GitHub URL when it publishes.

- `videos/` – finished Shorts (1080x1920, 30 fps)
- `specs/` – the render spec of each Short (images, on-screen text, timing cues)
- `music/` – original ElevenLabs music beds (rotated)
- `tools/render.py` – the renderer (ffmpeg + Pillow)
- `log.json` – every Short: date, format, title, facts, music
- `PIPELINE.md` – the step-by-step daily run the scheduled task follows

Rules, rotation and the fact bank live in the History Facts Channel Playbook doc.
