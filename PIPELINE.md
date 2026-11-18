# TimeWarpedFacts — daily Short pipeline

The daily scheduled task follows this file exactly. One run = one new Short, scheduled for **tomorrow 10:00 Asia/Singapore** (9 PM US Eastern). David does not review before it goes live, so every check below matters.

Fixed IDs
- Metricool brand **TimeWarpedFacts, blogId 8203057**, network youtube. Never touch any other brand (7623082 One Catch, 7625407 Aura Deficit, 8203302 ASMR).
- YouTube channel ID UCKI3Iz0eiEgJ4i0uPRs7vhg.
- Playbook doc (rules, rotation, requests, fact bank): Claude Docs artifact `7bcc1c14-7d91-475b-94df-ff031854615d` (https://claude.ai/artifact/GHeXpCS2eo8pDnuBmetk9z). It is the source of truth for the rules; this file is the how-to.
- Narrator: ElevenLabs voice **X1jCiTiZo6yr6tNO9AG8** (Jason Steele), model **eleven_v4**, always `generations_count: 1`.
- Images: ElevenLabs `creative_generate_image`, model **gemini-2.5-flash-image** (16:9 by default), always `generations_count: 1`.
- Repo: public `Funnyant322/timewarpedfacts-videos`, branch main. Video URL for Metricool: `https://raw.githubusercontent.com/Funnyant322/timewarpedfacts-videos/main/videos/<file>.mp4`.

## 0. Setup
1. `add_repo` Funnyant322/timewarpedfacts-videos with access "push", clone it to /home/claude/timewarpedfacts-videos (use `--filter=blob:limit=200k` so old videos aren't downloaded), `git config user.name Funnyant322`.
2. Read `log.json` (every Short so far: number, date, format, title, facts, music track).

## 1. Is there anything to do?
- POST_DATE = tomorrow (Asia/Singapore). If POST_DATE is a **Sunday**, stop quietly (Sunday is the long-form day, no Short).
- Metricool `getScheduledPosts` brandId 8203057, timezone Asia/Singapore, POST_DATE 00:00 to 23:59. If a non-draft YouTube post already exists that day, stop quietly.
- ElevenLabs `account_get_usage`: if fewer than ~6,000 credits are left, don't start; notify David (step 12) that credits ran out.

## 2. Decide the video
1. Read the playbook doc with the Claude Docs tools (read the project, then the tab's node). Load `guide(["topic.index","topic.editing"])` before editing it.
2. **Video requests first**: if the "Video requests" checklist has an unticked item, make the OLDEST one (its format can be whatever fits the idea).
3. Otherwise FORMAT = the weekly rotation row for POST_DATE's weekday (Mon A, Tue B, Wed A, Thu C, Fri A, Sat D). If that equals the format of the last entry in log.json, use the next format in the order A→B→C→D→A that differs from it.
4. Never repeat a fact already in log.json or marked "Used" in the fact bank. Pick facts that fit the format (A: 5 time-bending pairs, best last; B: one person/animal + 3–4 things that happened in their lifetime; C: one fact + the story + twist; D: 3–4 then-vs-now pairs).

## 3. Fact-check (playbook "Fact-check rule" — no shortcuts)
For every fact: find the exact dates/numbers, confirm them in **two independent reputable sources** (WebSearch/WebFetch: encyclopedias, museums, universities, reputable news; not social media or fact-list sites), do the arithmetic ("closer to X than Y" must win by a clear margin), use "around"/"over"/"scientists think" where sources vary, and drop anything shaky. Add each new fact as a row at the bottom of the fact bank table (Fact | Key dates | Status "Verified – Short NNN" | Source links, both sources) BEFORE generating anything. If a requested fact is false, leave it out and say so in the summary.

## 4. Script, title, metadata
- 30–45 s spoken (about 80–105 words). Hook in the first 2 s promising a feeling + payoff; strongest fact last; end with "Follow for more history that breaks your brain." (or a close variant). Use eleven_v4 tags sparingly: `[intrigued]` at the start, `[slowly]` before the last fact. Blank line between beats.
- On-screen text per beat: short, true, under ~12 words (sub-line only on the opening beat). Hook text on beat 1 must be readable in under 2 s.
- Title (under 70 chars, curiosity + no clickbait lies), description (2–3 sentences + "New history facts every day." + 3 hashtags incl. #shorts #history), 6–10 tags, first-comment question.
- Disclosure: `isAiGeneratedContent: true` if any image could pass as a real photo of a real event or person (photo-style, albumen, 1930s B&W etc.); otherwise false. When unsure, true.

## 5. Generate (ElevenLabs)
1. `creative_create_flow` name "TWF Short NNN – <slug>"; pass its flow_id to every call.
2. Speech: `creative_generate_speech` (voice/model above, generations_count 1). Poll `creative_get_flow_run_status` until done.
3. Images: one per beat (5–8), `creative_generate_image` generations_count 1. Style: "Realistic oil painting / 19th-century academic painting / realistic paleoart of …, warm cinematic light, no text". No photographs of real people; real people only as paintings, or show their places/objects instead. Never repeat an image from an earlier Short. Fire them all, then poll.
4. LOOK at every image (`creative_get_generations` shows previews). Regenerate (once) any image with garbled text, extra limbs, wrong era, or that misrepresents the fact.
5. Transcribe the narration: `creative_transcribe_audio` model eleven_scribe_v1, connect_from = speech node_id; poll; you need `words_download_url`.
6. Download narration, images and words.json with curl from the `full_res_url` / `content_url` / `words_download_url` (elevenlabsusercontent.com is reachable) into `work/` (git-ignored).

## 6. Music
Use a track from `music/` that is different from the last 2 Shorts in log.json. While `music/` has fewer than 4 tracks, generate one new one first: `creative_generate_in_flow` node_type "music", model eleven_music_v2_5, generations_count 1, prompt like "40-second instrumental bed for a history documentary short: <new mood/instruments>, no vocals, steady level, loopable" — save it as `music/NN_<slug>.mp3` and commit it.

## 7. Render
Write `specs/NNN.json` (see `tools/render.py` docstring): `vo`, `music`, `words`, `music_db: -20`, `loop_tail: 0.7`, and `segments` with `image`, `text`, optional `sub`, and `cue` = the first 2–4 spoken words of that beat (exactly as in the script). The last segment is the CTA beat and reuses image 1 so the ending loops back to the opening. Then:

`python3 tools/render.py specs/NNN.json` → `videos/NNN_<slug>.mp4`

## 8. Check before publishing (all must pass)
- `ffprobe`: 1080x1920, 30 fps, has audio, duration 28–50 s; file under 50 MB.
- Loudness about −14 LUFS (`ffmpeg -i X -af ebur128 -f null -`).
- Contact sheet (`ffmpeg -i X -vf "fps=1/2.5,scale=216:384,tile=6x3" -frames:v 1 sheet.png`) — LOOK at it: text fully on screen and readable, each text matches its image, no blank or duplicated beats, ending returns to the opening image. Also look at the frame at 0.5 s full size (the hook frame).
- Listen-check by transcript: the narration words match the script (no skipped/garbled facts).
Fix and re-render until clean. If something can't be fixed, don't schedule (step 12).

## 9. Publish the file
`git add videos/NNN_*.mp4 specs/NNN.json log.json music/` → commit "Short NNN: <title>" → push to main. Then `curl -sI <raw URL>` must return 200 with the same content-length as the local file (wait ~30 s and retry once if not).

## 10. Schedule in Metricool
`createScheduledPost` blogId "8203057", date `<POST_DATE>T10:00:00+08:00`, info:
```json
{"autoPublish": true, "draft": false, "descendants": [], "firstCommentText": "<question>", "hasNotReadNotes": false,
 "media": ["<raw URL>"], "mediaAltText": [], "providers": [{"network": "youtube"}],
 "publicationDate": {"dateTime": "<POST_DATE>T10:00:00", "timezone": "Asia/Singapore"},
 "shortener": false, "smartLinkData": {"ids": []}, "text": "<description>",
 "youtubeData": {"title": "<title>", "type": "short", "privacy": "public", "tags": [...], "category": "EDUCATION", "madeForKids": false, "isAiGeneratedContent": <bool>}}
```
Then `getScheduledPosts` for POST_DATE: exactly one non-draft YouTube post at 10:00. Never create a second post if one already exists; never edit or delete other posts.

## 11. Record
- log.json: append {number, post_date, format, title, facts (short list), music, file, flow_id, metricool_planner_url}; commit + push.
- Playbook doc: set the new fact-bank rows' Status to "Used in Short NNN (POST_DATE)". If this was a request, tick it and add the posting date.

## 12. Notify David (PushNotification)
Success — first sentence: "Tomorrow's TimeWarpedFacts Short is scheduled: <title>." Then the facts in one line, the post time, the Metricool plannerUrl.
Failure — if any step fails (credits, generation, fact-check finding too few solid facts, render, GitHub push, Metricool), schedule nothing half-finished and say exactly which step failed and why, so tomorrow isn't silently empty.
