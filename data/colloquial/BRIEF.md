# Writer brief: colloquial Greek lessons (read fully before writing)

Learner: Devon, adult experienced polyglot, Greek grammar ~B1, aiming at natural spontaneous conversation and later C1. Personal-use app, single user. Treat slang, swearing, insults and sex/drug vocabulary frankly, as a linguist would: no bowdlerising, no moralising, but always give register, strength and when it is (not) acceptable. Lessons must be intensive and comprehensive (Devon explicitly does NOT want lean or shortened content). Aim for 30-45 KB per lesson file.

## Output per lesson (you write these yourself)
1. `/mnt/project-files/app/lessons/<id>.json` — the lesson. Valid JSON, UTF-8, Greek in monotonic orthography.
2. `/mnt/project-files/data/colloquial/parts/lex-<id>.json` — JSON array of lexicon entries for every slang/colloquial word or expression the lesson teaches (aim 40-90 per lesson; skip words already in the core lexicon unless the slang sense is new, in which case add an entry whose gloss gives the slang sense).
3. `/mnt/project-files/data/colloquial/parts/sources-<id>.md` — markdown list of sources you actually consulted (URL + what you took from it). Sources go ONLY here, never inside lesson text.

## Lesson JSON shape (copy exactly; see app/lessons/theme-work.json as a model)
{"el": "<Greek title>", "title": "<English title>", "vocab": ["<8-14 lemmas, single words or short phrases using only Greek letters/spaces, each must exist as a lemma in your lex file or the core lexicon>"],
 "blocks": [ ... ], "practice": [ ... ]}
Do NOT add goal/intro/section/source fields.

Block types (only these):
- {"type":"text","title":"...","text":"paragraphs separated by \n\n, **bold**, *italic*"}
- {"type":"table","title":"...","head":["..",".."],"rows":[["..",".."],...]}  (cells support **bold**/*italic*)
- {"type":"examples","title":"...","items":[{"el":"...","en":"..."}]}  (use for dialogues: one line per item, "— " or "Α:"/"Β:" speaker prefixes in el)
- {"type":"callout","text":"**Heading**\n\n..."}
- {"type":"culture","title":"...","text":"..."}
- {"type":"rules","title":"...","items":["...","..."]}
- {"type":"reading","title":"<Greek>","text":"<Greek, 250-450 words, colloquial/naturalistic: a chat, a scene, a monologue, a forum post>","en":"<full English translation>","gloss":{"<surface form exactly as in text>":"<lemma> — <English>"},"questions":[{"prompt":"<Greek>","answer":"...","options":["... (answer included)","...","..."]}]}
  Gloss every slang/rare word in the reading (25-50 entries). 4-6 questions.

Every lesson should contain: core tables with columns like Greek | Literal | Meaning | Register/strength (use a 0-5 strength scale: 0 neutral, 1 casual, 2 slangy/cheeky, 3 rude, 4 vulgar/offensive, 5 taboo, never with strangers) and a "when to use / who says it" note; typical responses or comebacks where relevant; at least two example dialogues (examples blocks, 8-16 lines each); pronunciation notes in words (no audio: stress, elisions like τα 'φαγα, assimilations, intonation, where emphasis falls); a culture block; a "common mistakes / false friends" callout; one reading.

Practice (only these generators):
- {"gen":"type","items":[{"prompt":"English meaning or cloze, ask for the Greek","answer":"...","accept":["...variants..."],"why":"short explanation"}]}  — 20-35 production items (English → Greek, cloze, register switching e.g. "Say this politely: ...", "Make this ruder: ...").
- {"gen":"mc","items":[{"prompt":"...","answer":"...","options":["... answer included ..."],"why":"..."}]}  — 12-20 items: meaning, register choice ("Which is acceptable with your boss?"), best response in a situation, strength ranking.

## Lexicon entry shape (same as data/lexicon/core-3000.json, plus colloquial fields)
{"lemma":"μαλάκας","translit":"malakas","pos":"noun|verb|adjective|adverb|other|phrase","gloss":"...","example":{"el":"...","en":"..."},
 "noun":{"gen_sg":"μαλάκα","gender":"m","declension":1,"model":"m-ας"}  (nouns only; use your best model label)
 "verb":{"present_1sg":"...","aorist_1sg":"...","conj_group":"A|B1|B2|deponent"}  (verbs only)
 "adjective":{"m":"..","f":"..","n":".."}  (adjectives only)
 "register":"colloquial|slang|vulgar|offensive|dialect", "strength":0-5, "region":"common|Athens|Thessaloniki|North|Crete|Cyprus|Pontic|Ionian|Peloponnese|...", "lesson":"<id>", "cefr_est":"B1|B2|C1", "source":"colloquial lexicon; entry written by Claude"}
Use pos "phrase" for multi-word expressions (they are shown in lessons but not used by tap lookup). Glosses should flag strength, e.g. "(vulgar, 4/5) fuck it". 

## Research
Web research is encouraged (WebSearch/WebFetch: slang.gr, el.wiktionary.org, Wikipedia (el/en) articles on Greek dialects, Cretan/Cypriot dialect glossaries, forums, lyrics, sitcom/stand-up material). Check what you are unsure about rather than inventing; do not invent slang. Write all example sentences and dialogues yourself (do not copy lyrics or long passages).

## Shared-folder rules
/mnt/project-files is a shared network folder used by other sessions. Only write the files named above (new files). Do NOT edit app.js, app.css, course.json, data/lexicon/, data/c1/ or the ledger. Do not run whole-folder content searches (grep -r) over /mnt/project-files. Do not install packages. Validate each JSON file with `python3 -c "import json;json.load(open(PATH))"` and re-read your files ~10 s after writing to confirm they persisted. Do not call any mcp__hearthbot__ tools.

When done, reply with: files written, sizes, entry counts, and anything you were unsure about.
