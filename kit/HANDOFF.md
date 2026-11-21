# What If Things — handoff for the next Claude session (written 20 Nov 2026, 22:15 SGT)

Read this first, then kit/PLAN.md. User: David (Singapore, doesn't code, wants short plain-language answers, never invent numbers, check every fact).

## Hard rules
- Metricool brand for this channel: blogId **8203057** (YouTube only). NEVER touch brands 7623082, 7625407, 8203302.
- Never use or clone David's own voice.
- If a video needs another ElevenLabs generation, just do it (no need to ask). Quality over cost: new scenes beat reused ones when they make the video better.
- Zoom in when it makes the video more engaging, but never cut off important parts.
- Keep the "topics done" list in memory (/areas/history-facts-channel.md) updated every time.

## Channel
- YouTube "What If Things", ID UCKI3Iz0eiEgJ4i0uPRs7vhg, @whatifthingsofficial. Google account sginterviewprep.help@gmail.com (in the built-in browser use `?authuser=sginterviewprep.help@gmail.com` for Studio).
- Format: "Every Type of ___ Explained", flat 2D cartoon (Everything Professor / things__explained style). Characters: Sam (teal t-shirt), Leo (orange hoodie), Mum (purple dress).
- Voice: ElevenLabs James – Husky & Engaging, voice_id EkK5I93UQWFDigLMpZcX, model eleven_v4, generations_count 1, natural pauses. Word timings via creative_transcribe_audio (scribe, free).

## Posting
- 4 Shorts a day at 09:00, 13:00, 17:00, 21:00 SGT, one part from each of 4 running series.
- Current batch: Friend, Group Chat, Cinema, Sibling.
  - Part 1s: LIVE 20 Nov (Friend zMRzj3cNpYQ, Group Chat 7rD7jpXd3lo, Cinema sclDGqU_GVY, Sibling FVilOvYYJIU).
  - Part 2s: SCHEDULED Sat 21 Nov 09:00/13:00/17:00/21:00 (Metricool post ids 435620214, 435620255, 435620308, 435620337).
  - **NEXT TASK: make Part 3s for Sun 22 Nov** (then Part 4s for Mon 23 Nov), send to David to check, then schedule.
- After these 4 series: Public Transport, Supermarket, Student, Teacher. Then the backlog in PLAN.md (Parent, Gamer, Party, Gym…, paradoxes, riddles, trending-news explainers with confirmed facts only).
- Metricool post: media = raw.githubusercontent URL of the mp4; youtubeData {title "… pt N #shorts", type "short", privacy "public", category "COMEDY", madeForKids false, isAiGeneratedContent false}; text = short caption + #shorts #funny #relatable. Verify after with getScheduledPosts.

## NEW style rules (20 Nov evening)
- **Bigger picture:** scene area is now 1080x1350 (4:5) inside the 1080x1920 frame, title boxes over the top of the picture, subtitles lower-middle, "Follow for Part N" near the bottom. Already in kit/tools/engine.py.
- **Generate every new scene at aspect_ratio 4:5** (gemini-3.1-flash-image, resolution 1K, ~609 credits each). With a reference image wired in: add the node with creative_add_flow_node (model_parameters {"aspect_ratio":"4:5","resolution":"1K"}), then creative_run_flow_nodes with generations_count 1. Prompt tip: say "flat 2D cartoon in the same style as the reference picture" — a prompt with "recreate this exact scene" got blocked once.
- Use finished scenes as references, not character sheets (sheets leak duplicate characters).
- **Make videos longer from Part 3 on:** aim ~50–60 s (Part 1–2 were 27–35 s). More types/beats per part, more scenes.

## Tools / files
- Engine: kit/tools/engine.py → `python3 engine.py recipe.json [t1 t2 …]` (times = check frames). Recipe keys: out, voice, words, end, title[], footer[], scenes[{img,t,focus,zoom,pan,tilt}], overlays (phone, inbox, bubble, plates, banner, card), sfx_events (crinkle, crunch, boom, ding, pop, smash, sad, cheer). Images read from img/<name>.png.
- Recipes: kit/recipes/ (fr2, gc2, cn2, sb2 are the newest, already in 4:5 layout).
- Scenes: kit/scenes_tall/ = 4:5 versions (use these). kit/scenes/ = old 16:9.
- ElevenLabs flow: lm3GGXl6JOYuYbsAGZFD. Character sheet nodes: Sam D9uEvV8zHtPxf6F6dQFq, Leo m9bkxGlq8NPJBNbqMqHu, Mum HPAuThM5kAjL5ERW1Y4A. Good scene refs: cafe_arrival oC3nQyUOJDi0heySyZg8, TV hug (Leo+Mum) FSxtsj8acijInOmsro8j, plate scene (Sam+Mum) 1IMfb4AK7jjcXLyV1Cmo. To use a kit image as a ref: creative_attach_reference_file with its raw GitHub URL + flow_id.
- Repo: github.com/Funnyant322/timewarpedfacts-videos (videos in videos/every_type/). Git user Funnyant322 / Funnyant322@users.noreply.github.com; push with `git -c push.negotiate=true push origin HEAD:main`.
- PC kit folder: C:\Users\1234d\Videos\What If Things Kit (save videos/scenes there with device_commit_files).
- Credits: ElevenLabs Creator plan, 59,585 of 152,432 used as of 20 Nov 22:00 (~92,800 left), resets 20 Dec. Check with account_get_usage.

## ElevenLabs accounts (21 Nov 2026)
- David has TWO ElevenLabs accounts. Keep using the ORIGINAL one (yearly Creator, resets 20 Dec) until its credits run out.
- Check with account_get_usage before generating. When the original runs out (or is too low for the next video), STOP and tell David to switch the ElevenLabs connector (Claude Settings → Connectors → disconnect, reconnect, sign in with the second account). He has to do the switch himself.
- Second account: monthly Creator bought 21 Nov ($11 first month, $22 after) — remind him to decide before ~21 Dec.
- Heads-up: the original account dropped from 59,585 to 129,923 used (of 152,432) overnight 20→21 Nov, likely other channels' automations sharing it.

## Comment question on every post (21 Nov 2026)
- Add a first comment to every Metricool post (firstCommentText), e.g. "Which type should I do next? 👇" or "Which type of ___ are you? 👇". Metricool posts it as a comment; David can pin it in YouTube Studio.

## More content + more pictures (21 Nov 2026, David's feedback on Group Chat pt 2)
- Group Chat pt 2 felt like the same picture too long and too little content. Bigger channels pack in more.
- From Part 3 on: 3-4 types (or 3-4 beats) per video, a NEW picture every ~3-4 seconds (about 10-14 different pictures per 50-60 s video), no picture on screen longer than ~5 s. Zooms/pans only as extra motion, not as a substitute for new pictures.
- Cost estimate ~609 credits per picture + voice, so roughly 7,000-9,000 credits per video.

## Fast start (21 Nov 2026, David: intro too slow, viewers swipe)
- NO spoken intro ("Every type of X explained… part two:" took ~5 s). The title is on screen already. The first spoken words must be the first type/joke, within the first second.
- Cinema pt2 and Sibling pt2 were re-cut (videos/every_type/*_pt2_fast.mp4) to start at the first type.

## Pacing (21 Nov 2026, David: whole video too slow)
- After rendering the voice + words, ALWAYS run `python3 kit/tools/speedup.py recipe.json recipe_f.json 1.04 0.32` (cuts gaps between words to 0.32 s, plays 4% faster — David found 1.12/0.22 too fast, re-times scenes/overlays/sfx), then render the _f recipe.
- Write recipes in ORIGINAL voice timing; speedup.py maps everything.
- Use few [pause] tags in scripts. A shot needs ≥1 s after speedup.
- Friend pt3 (recipe fr3.json → fr3f.json) is the template for the new style: 3 types, 6 new pictures + 2 reused, ~17 shots, section cards ("THE SPOILER", "11:00 PM"), phone overlay scale 1.2, bubbles, ends on "WHICH ONE IS YOURS?". 36 s after speedup. Cost ~5,300 credits (images with 2 refs cost 812 each, 1 ref 609).
- For more length, add a 4th type rather than slowing down.

## Free pictures via Gemini app (21 Nov 2026) — preferred over ElevenLabs images
- Built-in browser, gemini.google.com, account 1234davidteyu@gmail.com (Gemini Plus). Upload menu (+) → Create image; aspect ratio picker → 3:4.
- Reference: Drive folder "What If Things - Gemini refs" (owned by 12345davidteyu, shared to 1234davidteyu). Attach via + → Drive → search "ref_characters" → select → scroll → Insert. (Page CSP blocks fetch/paste of outside images.)
- Prompt: "Use the attached pictures as the style and character reference… flat 2D cartoon… [scene]… Vertical portrait, character large. No text."
- ~20 s per picture. Download: find button "Download full-sized image" → lands in C:\Users\1234d\Downloads\Gemini_Generated_Image_*.jpg (1792x2400, no visible watermark) → device_stage_files.
- Downloads folder is connected to the session. Use ~3 Gemini tabs in parallel (limit is per account).
- ElevenLabs now only for voice (~640 credits/video).
- Gemini downloads gotchas: the other Claude session also saves Gemini pictures to Downloads — only use files you clicked (check timestamps + content). Some downloads stay as *.tmp (full JPEG inside, usable). If a download never arrives, reuse another picture. Pictures are 1792x2400 (3:4): crop top/bottom to 4:5 and resize to 1080x1350 into img/.
- In-page helper: window.gemGen(prompt) (set via javascript_tool) types prompt with execCommand insertText, clicks Send, waits for the new image, clicks "Download full-sized image". Max 2 per JS call (45 s tool timeout).
- Group Chat pt3 (gc3.json) made this way: 7 Gemini pictures, voice 546 credits (+165 for transcription this time).
- Quick spoken title (David 21 Nov): after speedup, add a fast intro clip: generate "[energetic, quick] Every type of X, part N!" (~50-60 credits), then `python3 kit/tools/addintro.py rec_f.json intro.mp3 rec_i.json "Every type of X, part N!"` and render rec_i.json. ~2 s, then straight into the first type.
- Gemini "Deeper analysis (4 Neon)" model is LOCKED on 1234davidteyu@gmail.com (lock icon) — only Auto / Everyday help (4 Hydrogen) available there.
