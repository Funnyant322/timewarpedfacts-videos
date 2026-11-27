# Rules for every session

- **Pictures:** make all AI scene pictures in **Google Flow** (https://labs.google/flow, Nano Banana model) in the built-in browser, account 1234davidteyu@gmail.com. Do NOT use the Gemini chat (it caps at ~10 pictures then waits) and do NOT use ElevenLabs images. Use Blender only for things Flow can't do. (David's rule, 22 Nov 2026. Check the real daily Flow limit the first time and note it in kit/HANDOFF.md.)
- Read kit/HANDOFF.md before making anything.
- In Flow use **Nano Banana 2.1** for these cartoon pictures (Nano Banana Pro uses the allowance much faster; only for realistic shots).
- Speed: open **several Flow tabs** in the built-in browser and start pictures in all of them at once, then download them together. Aim for ~10-15 new pictures per video.
- **Review rule (from 22 Nov 2026):** David is now hands-on with What If Things (and 3AM Rules). From pt6 onwards: send him scripts/ideas first, then the finished video, and only schedule in Metricool after he says ok. Already-scheduled pt4/pt5 (23-24 Nov) stay as they are. From then on post 2 videos a day (not 4). Performance reviews on Mondays and Thursdays. (Satisfy Lab and Ember Hours stay fully automated.)

## Music library (23 Nov 2026)
- All music tracks live in kit/music/ (repo) and on David's PC at Music\Video Music Library (README.txt lists the mood of each one).
- Reuse these first; they cost nothing. Only make a new track when no mood fits. Then save the new track to both places and add a line to README.txt.

## Flow full-res download - SOLVED (26 Nov 2026)
- Front the Flow tab (tabs_select), then read `[...document.querySelectorAll('img')]` srcs containing `/asb/`. Strip the `=s512-rw` ending and add `=s0` for the full image (896x1200 for 3:4).
- Bundle all of a project's images into ONE download (fetch each `=s0`, write `IMG<i> <len>\n` + bytes into one Blob, click an <a download>). It lands in Downloads (sometimes as a .tmp name until saved). Stage it, then split with d1/unb.py logic.
- Ask the Flow agent for many images in one message ("generate 7 separate images, 1 each... use the image you just made as the reference"). Don't navigate a tab while it's generating (that cancels it). Open a 2nd tab with tabs_create, NOT preview_start (that one reuses the current tab).
- New video format from 26 Nov: no spoken title, joke in the first second, ~30 s, footer [] (no "Follow for part"), no CTA.
- 26 Nov upgrade (approved style to try): recipe keys "full": true (picture fills the whole 9:16 screen), "caps": "big" (3-word bold captions, current word yellow), "title_y": 230, footer []. Make Flow pictures at 9:16. Cards at y≈0.40 so they don't hit the captions (0.64). Example: kit/recipes/mk8_pt_sm.py

## Posting plan (27 Nov 2026)
- Public Transport + Supermarket series: 2 videos a day until both series end.
- After that: What If Things goes to 1 video a day, and each video gets more time and polish. Still send script first, then the video, and only schedule after David's OK.
