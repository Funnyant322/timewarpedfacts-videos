# Channel pipeline — "What happens if…?" (3D animated Shorts)

Replaces the old history-facts pipeline (retired 2026-11-19). Reference video:
`videos/w001_what_if_you_swallow_gum.mp4` (spec `specs_story/w001.json`,
ElevenLabs flow `4RLRHsdBaBCOyDTDYKFU`).

## Format rules
- Title/hook is always a question: "What happens if you …?"
- Everyday, relatable, slightly gross/scary/surprising topics (body, survival,
  everyday objects, physics). No history topics. No real named people.
- 28–38 s, 7 shots, every shot animated (no stills).
- Story arc: hook (Max does the thing) → myth/fear → what really happens inside
  (2–3 "inside the body / zoomed-in" shots) → the extreme case (real documented
  case) → Max's punchline ending with a simple rule ("One piece? Fine. A whole
  pack? Spit it out.").
- Recurring host character **Max**: ~10-year-old boy, messy dark-brown hair,
  freckles, red hoodie with white drawstrings, jeans. Character sheet =
  generation `PwNxOcCwephxJFmbwanw` on flow `4RLRHsdBaBCOyDTDYKFU` (wire it as the
  `images` reference on every keyframe where Max appears).
- Kid-friendly visuals: no blood, no gore, cartoon "inside the body" style.

## Fact-checking (mandatory)
Every claim checked against at least one reliable source (medical journals,
PubMed, university/hospital sites, major science outlets) before narration.
Numbers in the script must match a source; if unsure, make the line vaguer.
Keep the sources list in the commit message.

## Production steps
1. Pick topic + write script (~110 words) with eleven_v4 tags
   ([curious], [whispering], [deadpan], [laughs], [serious], [cheerful]).
2. `creative_create_flow` (name "WhatIf NNN - topic").
3. TTS: eleven_v4, voice Liam `VWoZS7XxvCTNUPpiPuUJ`, generations_count 1.
4. Transcribe the TTS node with eleven_scribe_v1 (free) → strip `[tag]` words
   → `work/wNNN/words.json`.
5. 7 keyframes: gemini-3-pro-image, model_parameters
   `{"aspect_ratio":"9:16","resolution":"1K"}`, generations_count 1.
   Prompts start with "Single full-frame 3D CGI render (feature-animation
   quality, NOT 2D, NOT panels)", say "upright portrait", end "No text."
   Check every keyframe; regenerate any that are 2D/comic, multi-panel,
   sideways, or off-model.
6. 7 clips: kling-2.5-turbo, start_frame = keyframe node,
   `{"duration_secs":5,"aspect_ratio":"9:16","negative_prompt":"text, watermark, blurry, distorted, extra fingers"}`.
7. Download clips (content_url) to `work/wNNN/v1..v7.mp4`, contact-sheet check.
8. Spec `specs_story/wNNN.json` (paths relative to specs_story/, cue = first
   2–3 words of each shot's line), music `music/03_clockwork_discovery.mp3` at
   −24 dB → `python3 tools/edit_story.py specs_story/wNNN.json`.
9. Check frames + loudness (~−14 LUFS), commit + push, then schedule in
   Metricool (brand 8203057) using the raw.githubusercontent.com URL.

## Cost (ElevenLabs credits, approx.)
TTS ~650 · 7 keyframes ~9–11k · 7 Kling clips ~14.8k · total ~25–32k per video
(more if shots need redoing). Creator plan = ~158k/month shared with One Catch.
