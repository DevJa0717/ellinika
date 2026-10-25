# Ελληνικά: Project Ledger

The shared record of this project. Every agent and thread reads this before starting work and appends to it when work lands. People are welcome to edit it too.

Last updated: 2026-10-17

---

## How to use this ledger (conventions for agents)

1. **Read first.** Before starting a task, read the Goal, Roadmap, Decisions and Open questions sections so you build on what exists instead of re-deciding it.
2. **Append, don't rewrite.** Add new Progress log entries at the bottom of that section, newest last. Never delete or rewrite another thread's entry; if it is wrong, add a new entry that corrects it.
3. **Keep the edit small and safe.** Other threads may edit at the same time. Re-read the file just before writing, make one small edit, then read it back about ten seconds later to confirm your change survived. Re-apply it if it was overwritten.
4. **Log format.** One entry per milestone, not per step:
   ```
   ### YYYY-MM-DD · <thread title>
   - What changed: <one or two lines>
   - Where: <paths under /mnt/project-files, PR or artifact links>
   - Next: <what the next agent should pick up, or "none">
   ```
5. **Decisions.** When the user makes a decision (or you pick a default they accept), add a row to the Decisions table with the date and reason. Change a decision only by adding a new row that supersedes the old one.
6. **Roadmap status.** Update the status marker on a roadmap item when its state changes: `[ ]` not started, `[~]` in progress, `[x]` done. Add the thread that owns it in brackets.
7. **Open questions.** Add questions that need the user's call. When answered, move the answer into Decisions and strike the question through.
8. **Artifacts live beside it.** Put project outputs under `/mnt/project-files/<area>/` (for example `grammar/`, `app/`, `content/`) and link them from your log entry. Keep this file under about 30 KB; when the log grows long, move older entries to `ledger/archive/LOG-YYYY-MM.md` and leave a link.

---

## Project goal

Build an app for mastering Greek grammar. Later phases expand it to vocabulary, spaced repetition, and comprehensible input.

Guiding principles (proposed, confirm or edit):
- Grammar first: learners should be able to drill and understand forms (declension, conjugation, agreement) before the app broadens.
- Build content and engine separately, so grammar tables, vocab lists and texts are data the app reads, and later phases reuse them.
- Every phase should leave something usable on its own.

---

## Roadmap

### Phase 0: Foundations
- [x] Decide the Greek variety and scope (see Decisions) [Project ledger]
- [x] Choose the platform and tech stack (web, mobile, desktop) [Greek lessons web app: static mobile web app]
- [ ] Set up the repository and project structure
- [ ] Define the content data format (how grammar tables, words and exercises are stored)

### Phase 1: Grammar
- [~] Alphabet, pronunciation and stress (τόνος) [Greek essential grammar]
- [~] Articles and noun declension (genders, cases, number) [Greek lexicon and grammar data]
- [~] Adjectives and agreement [Greek grammar book; Holton paradigms in adjectives.json]
- [~] Pronouns (personal, possessive, demonstrative, relative) [Greek grammar book; Holton in pronouns-holton.json]
- [~] Verbs: present tense, conjugation groups (A, B1, B2) [Greek lexicon and grammar data]
- [~] Verbs: past tenses (imperfect, aorist) [Greek grammar book]
- [~] Verbs: future, subjunctive, imperative [Greek grammar book]
- [~] Verbs: passive / mediopassive voice [Holton in verbs-holton.json]
- [~] Exercise types: fill in the form, transform, multiple choice, explanation on error [Greek lessons web app]

### Phase 2: Vocabulary
- [~] Core frequency word list with gender, declension and conjugation class linked to Phase 1 data [Greek lexicon and grammar data]
- [~] Themed sets and example sentences [Lexicon to 3,000 words: core-3000.json, B2 thematic layer planned]

### Phase 3: Spaced repetition
- [ ] Scheduling algorithm (for example SM-2 or FSRS)
- [ ] Review queue covering both grammar forms and vocabulary
- [ ] Progress tracking and stats

### Phase 4: Comprehensible input
- [ ] Graded readers or short texts by level
- [ ] Tap-to-look-up words and forms, linked to grammar and vocab data
- [ ] Audio, where available

---

## Decisions

| Date | Decision | Reason | Thread |
|------|----------|--------|--------|
| 2026-10-17 | The project ledger lives at `/mnt/project-files/ledger/LEDGER.md` and all agents read and append to it | One shared, plain-text record every thread can reach | Project ledger |
| 2026-10-17 | Default to Standard Modern Greek for all content data | Coordinator default for the reference files Devon supplied, all of which are Modern Greek | Greek lexicon and grammar data |
| 2026-10-17 | Words 1001-3000 come from the OpenSubtitles 2018 frequency list (CC BY-SA 4.0) in a separate core-3000.json; a further 1,000 B2-exam thematic words go in b2-thematic-1000.json | Verifiable open frequency source; Devon asked for B2 exam topics | Lexicon to 3,000 words |
| 2026-10-17 | Mastery Tracker: B2 readiness = vocab 40% + grammar 40% + comprehension 20%; a word is "known" only when produced EN→EL and used in a sentence with FSRS stability ≥ 90 days (recognition tracked separately as "understood"); grammar lessons need 90%+ re-passed after a 30-day gap; C1 shown greyed on the ladder | Devon's answers: production and spontaneous intellectual conversation are the goal, retention bar "much stricter" | Lexicon to 3,000 words |
| 2026-10-17 | Content data lives as JSON under `/mnt/project-files/data/` (`lexicon/`, `grammar/`) | Keeps content separate from the app engine, per the guiding principles | Greek lexicon and grammar data |
| 2026-10-17 | The app is a static web site (plain HTML/CSS/JS, no build step) in `/mnt/project-files/app/`, reading lessons from `app/lessons/*.json` and content from `data/` | No repo attached; Devon uses it on a phone via an Artifact preview; personal use only | Greek lessons web app |
| 2026-10-17 | Course runs A1 to B2 now, C1 later; progress is a "Road to B2" mastery tracker | Devon's request | Greek lessons web app |
| 2026-10-17 | Modern Greek only, in a modern, everyday register at a high level; history appears only as etymology notes | Devon's answer to "Which Greek?" | Project ledger |
| 2026-10-17 | Web app, mobile friendly | Devon's answer to "Platform?"; matches the static web app already built | Project ledger |
| 2026-10-17 | Learner level: grammar at B1, vocabulary lower. Devon picks up patterns fast and builds vocabulary more slowly, so vocabulary work should be boosted until it matches grammar level | Devon's answer to "Learner level?" | Project ledger |
| 2026-10-17 | Interface language switchable (English / Greek explanations) | Devon's answer to "Interface language?" | Project ledger |
| 2026-10-17 | Always one single user: no accounts, no multi-user sync | Devon's answer to "Accounts and sync?" | Project ledger |

---

## Open questions

- ~~**Which Greek?**~~ Answered: Modern, everyday register (see Decisions).
- ~~**Platform?**~~ Answered: mobile-friendly web app.
- ~~**Learner level?**~~ Answered: grammar B1, vocabulary lower, boost vocab.
- ~~**Interface language?**~~ Answered: switchable.
- ~~**Accounts and sync?**~~ Answered: always one single user.

---

## Progress log

### 2026-10-17 · Project ledger
- What changed: Created this ledger with goal, roadmap, decisions, open questions and conventions.
- Where: `/mnt/project-files/ledger/LEDGER.md`
- Next: Answer the open questions in Phase 0, then pick the stack and set up the repository.

### 2026-10-17 · Greek lexicon and grammar data
- What changed: Extracted Devon's reference files into JSON. Lexicon: 997 of the 1000 frequency words (rank, lemma, translit, POS, gloss, example el/en; nouns with gen sg, gender, declension; verbs with present/aorist 1sg and group A/B/deponent; adjectives with 3 genders). 80 entries carry `needs_review` where the source form key was irregular. Grammar: article, 9 noun models with all cases, personal pronouns; verb stems, endings, present paradigms A/B1/B2, aspect examples.
- Where: `/mnt/project-files/data/lexicon/core-1000.json`, `/mnt/project-files/data/grammar/declensions.json`, `/mnt/project-files/data/grammar/verbs.json`; per-file notes in `/mnt/project-files/.notes/inputs.md`
- Next: (1) Extract verb guide sections 4 onward (subjunctive, imperative, passive, irregulars) into verbs.json. (2) Split lexicon group B into B1/B2 and resolve the 80 `needs_review` entries. (3) Add the missing feminine -η model (αδελφή) and adjective paradigms. (4) Mine the Section 4 PDF (d0ce0c63) and Vocabulary Guide for thematic sets, prepositions-by-case and A1-B2 sentence patterns.

### 2026-10-17 · Greek.zip contents
- What changed: Inspected Devon's Greek.zip. It is a design asset for a printed cover page ("Ελληνικά, Τόμος Α΄", Εγχειρίδιο 01): two HTML cover sheet versions, two preview screenshots, seven Greek stock photos. No vocabulary or grammar data; nothing added to app data. Possibly reusable later for app branding (palette: paper #f3ece0, aegean #1c3d5a, terracotta #b5532a; fonts Cormorant Garamond / EB Garamond).
- Where: original upload only (not copied into project files)
- Next: none

### 2026-10-17 · Greek grammar book
- What changed: Devon's two PDFs are one book split in two: Poulopoulou, "Modern Greek: Grammar Notes for Absolute Beginners" (A1-A2, Kallipos 2015, CC BY-NC-SA, so non-commercial use with attribution only). Extracted into four new files (existing files untouched): present tense groups A1/A2/B1/B2, passive groups -ομαι/-άμαι and είμαι with basic verb lists; indefinite article, numerals 1/3/4, telling time, πολύς/λίγος, adjective models ακριβός/νέος, comparison; personal (weak vs strong), demonstrative, interrogative, indefinite and relative pronouns; aorist endings and stress rule, future models, and present/aorist/future for 99 basic verbs. Nominative and accusative only; the book's genitive chapter is not yet extracted.
- Where: `/mnt/project-files/data/grammar/verbs-present-groups.json`, `noun-dependents.json`, `pronouns.json`, `verbs-past-future.json`; uploads 8e8e722c (book pp. 1-91) and d3fd3815 (pp. 92-176), notes in `.notes/inputs.md`
- Next: (1) Extract Ch 10 (genitive of nouns/adjectives/articles, possessives μου/σου/του) and Ch 7 (prepositions by case). (2) Extract Ch 1 (alphabet, stress, digraphs) for the roadmap's alphabet item. (3) Owner of verbs.json may want to fold A1/A2 split and the 99 principal parts into the lexicon's verb entries (aorist_1sg).

### 2026-10-17 · Greek essential grammar (Holton et al.)
- What changed: Devon's 50-page PDF is the first half of Holton, Mackridge & Philippaki-Warburton, "Greek: An Essential Grammar" 2nd ed. (Routledge 2016), photographed pages with no text layer. Copyrighted, no open license: data restates rules in our own words with short examples only, for personal/non-commercial use. Extracted Ch 1-2 (alphabet with names and sounds, vowels and their spellings, digraphs incl. αυ/ευ rule, 25 consonants with palatal/glide rules, initial clusters, colloquial vs formal doublets, sandhi across word boundaries, stress and enclisis, intonation, monotonic accent rules, diaeresis, capitals, punctuation) and §3.1-3.2 (noun-phrase patterns, case by function). No new lexicon items worth adding.
- Where: `/mnt/project-files/data/grammar/alphabet-phonology.json`, `/mnt/project-files/data/grammar/noun-phrase.json`; upload 7635aa83 (PDF pp. 1-25 front matter, 26-40 Ch 1, 41-46 Ch 2, 47-50 §3.1-3.2)
- Stopped at: end of the upload (PDF p. 50, mid §3.2). One page of the three-consonant cluster list seems missing between PDF pp. 34 and 35.
- Next: When Devon uploads the second half, start at §3.3 (gender, number, case, articles, declensions); compare with declensions.json rather than duplicating. Pages are images, so render with pdftoppm at 100 dpi and read them.

### 2026-10-17 · Greek essential grammar part 2 (Holton §3.3-3.51)
- What changed: Extracted the second Holton upload (60 scanned pages, same book and copyright terms as part 1, so no new license). New `nouns-full.json`: gender rules, articles (with τη(ν)/μια(ν) rule and σε-contractions), 31 noun paradigms covering every declension class in §3.9-3.29 with stress rules and word lists, irregular neuters, common gender, vocative of names, gender change in plural, indeclinables. New `adjectives.json`: 11 adjective paradigms (ψηλός, τέλειος, γλυκός, βαρύς, καφετής, πολύς, ακριβής, συνήθης, τεμπέλης, φαγάς, επείγων), indeclinables, comparative/superlative rules and irregulars. Added agreement (§3.48) and case uses (§3.49-3.51) to `noun-phrase.json`. `declensions.json` left untouched; nouns-full.json is the superset.
- Where: `/mnt/project-files/data/grammar/nouns-full.json`, `adjectives.json`, `noun-phrase.json`; upload 86b689c6 (PDF pp. 1-40 nouns, 41-55 adjectives, 56-60 §3.48-3.51)
- Stopped at: PDF p. 60, mid §3.51 (accusative of time).
- Next: Uploads 418329ba (60 pp.) and cf552d33 (51 pp.) are book pp. 111-220; continue from §3.51.

### 2026-10-17 · Greek essential grammar part 2 (Holton, rest of book)
- What changed: Extracted the remaining five Holton uploads, so the whole book is now in data. Same book and copyright terms, so no license change. Files: `noun-phrase.json` gains genitive/vocative uses, article use and omission, adjective use (§3.51-3.57); `pronouns-holton.json` (Ch 4, full weak/strong paradigms and clitic rules); `numerals.json` (Ch 5); `verb-phrase.json` (§6.1); `verbs-holton.json` (Ch 6: stems, aspect, moods, voice, full paradigms for χάνω/αγαπώ/θεωρώ/κοιμάμαι/είμαι/λέω, perfective-stem classes, participles, 166 irregular verbs with principal parts); `adverbs.json` (Ch 7); `prepositions.json` (Ch 8); `conjunctions.json` (Ch 9); `clauses.json` + `clauses-2.json` (Ch 10, split at §10.9.1/10.9.2); `word-formation.json` (Ch 11); `address-politeness.json` (Ch 12); `appendices.json` (correspondence table, 65 abbreviations); `glossary.json` (grammatical terms). Earlier Poulopoulou files (pronouns.json, verbs-*.json) left untouched; Holton files are parallel, not merged.
- Where: `/mnt/project-files/data/grammar/`; uploads 418329ba, cf552d33, 3b712c2e, afb4adc8, a92060f7 (see `.notes/inputs.md`)
- Caveats: A few spots need a human eye: the appendix correspondence table was low-res, the αποδεικνύω participle was cut off at the page edge, and two Ch 10 examples were printed oddly (both kept as printed, with notes). The index and publisher pages were skipped.
- Next: (1) Merge or cross-check the parallel sources (Holton vs Poulopoulou vs declensions.json) into one canonical grammar set before building exercises. (2) Fold verbs-holton irregular principal parts into lexicon verb entries.

### 2026-10-17 · Essential Greek PDFs
- What changed: Devon's five "Essential Greek part 1-5" PDFs are the same Holton, Mackridge & Philippaki-Warburton book already fully extracted, as a text-layer copy (Ch 1 to §12.1.6). Same copyright terms as before, so no license change. No new data added. Used the text to check two flagged gaps: the three-consonant cluster list was already complete (note corrected in `alphabet-phonology.json`), and the αποδεικνύω participle `απο(δε)δειγμένος` in `verbs-holton.json` matches the book.
- Where: uploads dbdd5171, 1a851669, 146f1f43, 34dec5a2, d8b3b998 (see `.notes/inputs.md`)
- Next: These PDFs are searchable, so use them to proof the scanned-page extractions. Greek in the text layer is in a legacy font encoding and needs remapping.

### 2026-10-17 · Data coverage count
- What changed: Counted the data. Lexicon: 997 entries (974 unique lemmas; 507 nouns, 211 verbs, 112 adj, 80 adv), all with an example sentence, 204 verbs with aorist, 80 `needs_review`. Grammar: 23 files, ~180 Holton section numbers tagged, ~355 rule fields, ~1,590 el/en example pairs, ~70 paradigms (40 noun incl. 9 starter models, 13 adjective, 16 verb), 166 Holton irregulars + 99 Poulopoulou principal parts, 101 glossary terms. Overlap: Holton vs Poulopoulou verb lists share 34 verbs; only 80 of 211 lexicon verbs appear in either list. Poulopoulou/declensions.json cover the same ground as Holton with different model words (only παιδί shared).
- Where: no files changed; counts from scripts over `/mnt/project-files/data/`
- Next: Canonical merge (see previous entry); fill principal parts for the 131 lexicon verbs in neither list.

### 2026-10-17 · Greek lessons web app
- What changed: Built the first version of the learning app. Course map of 47 lessons A1 to B2 (each planned lesson names its Holton sections); 9 lessons built: alphabet, digraphs/αυ-ευ, stress, gender and article, cases and full article, masculine -ος, είμαι, present tense 1st conjugation, and B1 aspect. Each has a Learn page (rules/tables pulled live from data/ via refs like `grammar/nouns-full.json#paradigms[id=m-ος-fixed]`) and a Practice set (generators in app.js: multiple choice, typed answers with accent-only "almost", full table fill, decline-like and conjugate drills from the lexicon; missed items repeat). On-screen Greek keypad. Home shows a first "Road to B2" tracker (share of lessons per level at 85%+). Progress saves in the browser (localStorage).
- Where: `/mnt/project-files/app/` (index.html, app.css, app.js, lessons/course.json + lesson files, tools/bundle_preview.py); preview https://claude.ai/artifact/SXiVDwZ4P84iJcP87Abd24 (republish: run `python3 tools/bundle_preview.py <scratch>/pub` from app/ and publish its index.html with the JSON files)
- Format: a lesson file is `{el, title, section, goal, blocks:[...], practice:[{gen,...}]}`. Block types and generators are listed in app.js (BLOCKS, GENERATORS). To build a planned lesson, add `"file"` to its entry in course.json.
- Vocabulary loads `data/lexicon/core-3000.json` if present, else core-1000.json.
- Next: (1) Mastery Tracker v2: add vocabulary known per level (needs word review / SRS with CEFR tags from the 3000-word list) and per-topic detail. (2) Build the remaining A1 lessons (feminine/neuter nouns, verbs in -ώ, negation and questions), then A2. (3) Move progress from localStorage to an artifact store if Devon wants it on more than one device.

### 2026-10-17 · Greek lessons web app (B2 syllabus)
- What changed: Re-plotted the B1-B2 course map from Devon's B2 exam syllabus (51 lessons total). Lessons carry `"b2": "grammar"|"syntax"` tags; course.json has a `b2_syllabus` block with the 7 exam themes (work, society, environment, technology, health, education, culture). The Road to B2 tracker now shows per-level bars plus B2 exam rows: grammar 0/14, syntax 0/11, vocabulary themes 0/7. A theme counts as mastered via progress key `theme-<id>` once themed word sets exist.
- Where: `/mnt/project-files/app/lessons/course.json`, `app/app.js` (tracker()); preview https://claude.ai/artifact/SXiVDwZ4P84iJcP87Abd24
- Next: Vocabulary thread: tag the B2 1,000 words with these theme ids so the app can build a themed word review per topic.

### 2026-10-17 · Lexicon to 3,000 words (batch 1)
- What changed: Started `core-3000.json` (additions only, ranks 1001+, no lemma from core-1000). Batch 1 = 358 entries (ranks 1001-1358) from the first 680 frequency candidates. Same entry format as core-1000 plus `cefr_est` (model estimate A1-C1) and `freq_count`; verb groups use A/B1/B2/deponent (core-1000 still uses B). Ranks follow corpus frequency, so some very common words missing from core-1000 (να, δεν, θα, ναι) sit at the top. Also drafted the Mastery Tracker plan (B2 readiness = vocab 40% + grammar 40% + comprehension 20%, everyday-coverage metric, plus a 1,000-word B2 thematic layer in `b2-thematic-1000.json` tagged by topic).
- Source: OpenSubtitles 2018 frequency list, [hermitdave/FrequencyWords](https://github.com/hermitdave/FrequencyWords) `content/2018/el/el_50k.txt`, content licensed CC BY-SA 4.0 (credit it in the app; share-alike applies to the list itself). Forms lemmatized with spaCy `el_core_news_md`, then corrected by hand. Glosses and example sentences are written by Claude, not copied.
- Where: `/mnt/project-files/data/lexicon/core-3000.json`; build kit (candidates, writer brief, merge script; next index in `NEXT`) in `/mnt/project-files/data/lexicon/build/` (scripts expect scratchpad paths, edit S/OUT at the top); plan doc https://claude.ai/code/artifact/30b4c588-d7bb-4fa8-908a-a6b9a5ddf8e7
- Status for the app thread: core-3000.json is usable now (valid JSON, same shape as core-1000) but partial; it grows in place, ranks are reassigned on each batch, so key on `lemma`, not `rank`.
- Next: Batches 2-5 from candidate index 680 onward until ranks reach 3000 (about 1,650 more entries, roughly 2,000 more candidates per 1,000 entries). Then backfill `cefr_est`/`freq_count` on core-1000, then the B2 thematic 1,000. Kept as-is for Devon to judge: a few vulgar words labelled (vulgar), and spelling variants of core words (ημέρα, βδομάδα, επάνω).

### 2026-10-17 · B2 exam study plan
- What changed: 30-week plan from 19 Oct 2026 to the May 2027 B2 Certificate of Attainment, starting from the alphabet: phases A1 (wk 1-5), A2 (6-11, go/no-go checkpoint), B1 (12-18), B2 (19-25, one exam theme per week), exam practice (26-30). Assigns all 51 course.json lessons to weeks (about 2 a week), 3,000 frequency words by week 18 and the 1,000 B2 thematic words in weeks 19-25, plus a daily 90-minute routine and four-skill targets.
- Where: `/mnt/project-files/plan/b2-study-plan.md`; machine-readable `/mnt/project-files/plan/b2-schedule.json` (per week: `start`, `phase`, `lessons` ids, cumulative `lessons_total`, `core_words`, `b2_words`, `theme`; `mastery_threshold` 0.85)
- Next: **Greek lessons web app thread:** the Mastery Tracker can show "on schedule" by finding the current week in b2-schedule.json by `start` date and comparing lessons at 85%+ with `lessons_total` (and known words with `core_words + b2_words` once word review exists). Build lessons in schedule order; week 3 needs a1-fem-neut, week 5 a1-present-2 and a1-negation-questions.

### 2026-10-17 · Greek lessons web app (tracker rules, learner profile)
- What changed: Tracker headline is now the weighted overall score (vocab 40 / grammar 40 / comprehension 20, only grammar live so far), C1 shows greyed on the ladder, and the note uses the vocabulary thread's bar (production EN→EL, 90+ days). Learner profile from Devon: experienced polyglot, so lessons stay brisk and skip hand-holding; declensions are the weak spot.
- Where: `app/app.js` tracker(); preview v3 https://claude.ai/artifact/SXiVDwZ4P84iJcP87Abd24
- Next: Build a "declension gym": mixed drills across all nouns-full/adjectives paradigms (generated from lexicon nouns by class), with spaced review of missed forms, linked from every noun/adjective lesson. Then grammar lesson re-pass after 30 days (90%+) per the tracker decision.


### 2026-10-17 · B2 exam study plan (revised)
- What changed: Devon is an experienced polyglot and finds declensions hard, so the plan is faster: A1 wk 1-3, A2 wk 4-7 plus a declension consolidation week 8 (go/no-go moves to week 8), B1 wk 9-14 (3,000 core words by week 14), B2 wk 15-21 plus declension week 22, exam practice wk 23-30. Adds a daily 10-minute declension drill. Supersedes the week assignments in the entry above.
- Where: `/mnt/project-files/plan/b2-study-plan.md`, `/mnt/project-files/plan/b2-schedule.json` (same fields; consolidation weeks have empty `lessons` and `"focus": "declension consolidation"`)
- Next: **Greek lessons web app thread:** same tracker hook as above. A declension drill generator (decline a lexicon noun with article and adjective in all cases) would serve the daily drill; lessons a1-fem-neut and a2-adjectives are needed by weeks 2 and 4.

### 2026-10-17 · Greek lessons web app (app backlog from Devon's answers)
- What changed: nothing built yet; backlog from Devon's answers to the open questions (single user forever, so localStorage stays; Modern Greek with etymology as side notes; grammar ~B1, vocabulary lower).
- Next (priority order): (1) Test-out: Devon can already skip a lesson by going straight to Practice (85%+ marks it mastered); add a "Test out of this unit" button that runs all of a unit's practice sets at once. (2) Vocabulary review (production EN→EL, spaced) weighted ahead of new grammar, so vocab catches up to B1. (3) Declension gym. (4) English/Greek interface switch: put UI strings in one table in app.js and add `en`/`el` fields to lesson text blocks. (5) Optional `etym` field on vocab/lesson blocks for etymology side notes.

### 2026-10-17 · Project ledger (Devon's answers)
- What changed: Devon answered all five open questions; recorded as Decisions. Modern everyday Greek (etymology only as side notes), mobile-friendly web app, grammar at B1 with vocabulary lower and to be boosted, switchable English/Greek interface, always a single user.
- Where: Decisions and Open questions sections of this file
- Next: (1) **B2 exam study plan thread:** the plan starts from the alphabet at A1, but Devon's grammar is already around B1; consider re-pacing grammar and shifting weight to vocabulary. (2) **Greek lessons web app thread:** add an interface-language switch (EN/EL explanations); no accounts needed, localStorage is fine for one user on one device.

### 2026-10-17 · B2 exam study plan (revised for starting level)
- What changed: Devon's grammar is already about B1 and vocabulary is lower and slower, so: weeks 1-2 test out of all A1-A2 lessons (`"mode": "test-out"`), week 3 declension week + B1 placement mock, B1 lessons wk 4-9, B2 lessons wk 10-16, declension week 17, theme-only weeks 18-21, exam practice wk 22-30. Vocabulary gets the most daily time: 3,000 core words by week 14, B2 themes wk 15-21. Go/no-go is now end of week 9 and is vocabulary-led. Supersedes both earlier plan entries.
- Where: `/mnt/project-files/plan/b2-study-plan.md`, `/mnt/project-files/plan/b2-schedule.json`
- Next: **Greek lessons web app thread:** tracker hook unchanged. Vocabulary is the main measure now, so word review/SRS matters more than new lessons; the A1-A2 lessons not yet built only need Practice sets for test-out. B1 lessons are due from week 4 (9 Nov).

### 2026-10-17 · Greek lessons web app (Greek blue redesign, declension gym)
- What changed: Single dark look (deep Aegean blue, white text, gold Greek-key border); units on the home page and Learn pages swipe sideways (scroll-snap pager with dots and Back/Next). Photo slots read `app/img/manifest.json` (`{"photos":[{file, caption, credit, license}]}`), currently empty: commons.wikimedia.org / upload.wikimedia.org are blocked by the network policy and Devon was asked to allow them. New generators: `decline` (any noun from Holton's 31 classes by analogy with the model, stress position copied from the end; verified on all model paradigms), `adj-agree`, `conjugate-2` (αγαπώ/θεωρώ types), `review` (spaced review of misses at 1/3/7/21/60/120 days, stored in localStorage `progress.review`). New "Daily" unit with the Declension gym (`daily: true` units are left out of the tracker). New lessons: a1-fem-neut, a1-present-2, a1-negation-questions, a2-adjectives, a2-weak-pronouns (15 live).
- Where: `/mnt/project-files/app/`; preview v6 https://claude.ai/artifact/SXiVDwZ4P84iJcP87Abd24
- Next: once Wikimedia is allowed, fetch ~10 photos of Greece into app/img/ (resize to ~1000px), fill manifest.json with credit/license, and log licenses here. Continue A2 lessons in course order.

### 2026-10-17 · Greek lessons web app (all A1, A2 nearly complete)
- What changed: 24 lessons live: all of A1, A2 except a2-possessives, plus b1-aspect and the Declension gym. New generators: `number-words` (1-9,999 with gender agreement), `prep-blank` (Holton §8.2 sentences with the preposition blanked), `principal-parts` (Poulopoulou's 99 verbs or Holton's 166 irregulars), `aorist-person` (stress/augment rule; irregular_1 group keeps fixed stress), `imperfect` (1st conj. from lexicon, 2nd conj. -ούσα), `future-person` (θα/να + perfective, three ending patterns). New Learn block `prep`. Data path note: keys containing dots (`irregular_verbs_6.25`) can't go through `resolve()` paths; read the file and index directly.
- Where: `/mnt/project-files/app/lessons/`; preview v7 https://claude.ai/artifact/SXiVDwZ4P84iJcP87Abd24
- Next: a2-possessives, then B1 units 6-7 (subjunctive, imperatives with clitics, passive present/past, perfect, relatives, complement, temporal, causal, conditionals).


### 2026-10-17 · App thread · B1 complete (preview v9)
- B1 Units 6–7 built: b1-aspect, b1-subjunctive, b1-imperative, b1-passive-present, b1-passive-past, b1-perfect, b1-relatives, b1-complement, b1-temporal, b1-causal, b1-conditionals, b1-comparison, b1-politeness.
- New generators: word-blank (src[] example sentences + words[] + distractors), passive-present, passive-aorist (common:true = lexicon verbs only), perfect (tenses). New block: uses (src list of {use|meaning, examples}).
- Note: Holton §10.13+ (10.15 temporal, 10.22 comparison…) lives in grammar/clauses-2.json, not clauses.json. Rules blocks need strings, not objects.
- Photos still blocked (Wikimedia unreachable from the container); img/manifest.json empty, plumbing ready.
- Next: B2 Unit 8 (b2-passive-irregular, b2-deponents, b2-participles), then Units 9–11 in course.json order.

### 2026-10-17 · App thread · B2 Units 8–9 (preview v10)
- Built: b2-passive-irregular, b2-deponents, b2-participles, b2-nouns-formal, b2-adjectives-formal, b2-learned.
- New generators: irregular-part (any column of Holton 6.25; `only` list or `common`), participle-agree (-μένος), gerund (-οντας/-ώντας + irregulars). adj-agree now handles -ής "mf" cells and stress-shifting cells (σύνηθες, επειγόντων) and takes `exclude`. decline handles m/f nouns (συγγενής) and picks τη/την by the next sound.
- Fixes: lexicon() now merges core-1000 + core-3000 (core-3000 holds only ranks 1001+, so before this the app saw just 358 words). derive() keeps a stressed ί/ύ before a vowel as its own syllable (περίοδοι, not πέριοδοι).
- window.__ellinika.GENERATORS is exposed for testing (scratch test: run a generator spec in the page).
- Next: Unit 10 (b2-suffixes, b2-prefixes from grammar/word-formation.json), then Unit 11 syntax lessons.

### 2026-10-17 · Greece photos
- What changed: Added 15 openly licensed Wikimedia Commons photos (CC BY-SA / CC0), cropped 16:9, 1200 px wide, ~150-280 KB each, and filled img/manifest.json in the existing format ({file, caption, credit, license, source}); captions are in Greek. The current photoFor() code picks them up with no code change. Files: acropolis, oia, delphi, plaka, meteora, thessaloniki, chania, navagio, mykonos, corfu, zagori, lindos, hydra, rhodes, karystos (.jpg).
- Where: /mnt/project-files/app/img/ (manifest.json, CREDITS.md with author, license and source link per file)
- Next: App thread may want a link to img/CREDITS.md somewhere in the UI; set a lesson's "photo" index to pin a specific image.

### 2026-10-17 · App thread · Course A1–B2 complete, photos live (preview v13)
- All 52 lessons in course.json are built. Added: Unit 10 (b2-suffixes, b2-prefixes) and Unit 11 (b2-concession, b2-result-purpose, b2-counterfactual, b2-indirect, b2-word-order, b2-discourse, b2-particles).
- Photos: 15 Wikimedia Commons photos (from the photos thread) are published; captions/credits come from img/manifest.json, and a "Photo credits" link on the home page opens #credits (renderCredits in app.js). Licenses also in app/img/CREDITS.md.
- Next (backlog, in priority order): (1) vocabulary review, production EN→EL with spacing, feeding the tracker's 40% vocab weight; (2) themed word-set slots for b2-thematic-1000.json once it exists; (3) "test out of unit" button; (4) EN/EL interface switch; (5) grammar 30-day re-pass rule in the tracker; (6) C1 units.

## Handoff 2026-10-18 (end of day, coordinator)

### Devon's directives today (2026-10-18), verbatim intent
- Remove only descriptive metadata under lesson sections (source citations, section labels, goal lines). Never shorten lesson content; Devon never asked for "leaner".
- Integrate cultural insights in lessons; expand lessons with more grammar practice and spaced recall of vocabulary; comprehensible-input reading texts from A2 onward; tap/hover lookup on any word, including words not yet introduced.
- Expand vocabulary to the 4000 most common words, comprehensively annotated.
- Sporadically embed videos (YouTube/public media) in containers, not stored; overlay Greek subtitles that can be paused and hovered word by word for lookup.
- Usage tier is now 5x monthly: lessons intensive, several lessons per major topic, UI more visually appealing.
- Web scraping allowed for advanced content; start building C1.
- Add units on popular and regional slang, curse words, insults, colloquialisms.
- Stop at clean end points tonight; tomorrow's tasks as simple paste-able commands.

### Active threads and file ownership
- "Intensive lessons with practice and readings": owns app/app.js, app/app.css, app/index.html, app/lessons/course.json and A1–B2 lesson files. First checkpoint live: word lookup, spaced recall, metadata removed, photo hero, culture notes on A1. In progress: A2–B2 culture notes/practice/readings, 23 new in-depth lessons (8 declension, 8 verb system, 7 B2 themes), subtitled videos.
- "Vocabulary to 4000 words": owns data/lexicon/ (core-1000.json, core-3000.json, build/).
- "C1 content from the web": owns data/c1/; writes c1-*.json lessons as new files, hands course.json entries to the lessons thread.
- "Slang, swearing and colloquial Greek": owns data/colloquial/; writes slang-*.json lessons plus a colloquial lexicon file in core-3000 entry format.

### Reference materials (all under /mnt/project-files)
- data/grammar/*.json: Holton "Greek: An Essential Grammar" fully extracted (nouns-full, verbs-holton 166 irregulars, pronouns-holton, clauses, clauses-2, word-formation, etc.); Poulopoulou "Modern Greek: Grammar Notes for Absolute Beginners" (CC BY-NC-SA, credit on Credits page). Personal use only.
- data/lexicon/core-1000.json, core-3000.json, build/candidates.json (frequency candidates), build/known_core.json, build/agent_brief.md, build/NEXT.
- plan/b2-study-plan.md and plan/b2-schedule.json: road to the B2 exam, May 2027; B2 syllabus themes (work, social issues, environment, technology, health, education, culture/media) and grammar list are in the plan.
- app/img/ with CREDITS.md and manifest.json (Wikimedia Commons photos).
- .notes/inputs.md: inputs log.
- Preview artifact: https://claude.ai/artifact/SXiVDwZ4P84iJcP87Abd24 (republish as new version, never a new artifact).
- Learner: experienced polyglot, grammar ~B1, vocabulary weaker, declensions weak spot, goal spontaneous intellectual conversation. Tracker: vocab 40 / grammar 40 / comprehension 20; known = produced English→Greek with 90+ day stability.

### Tomorrow: paste one of these into the project chat
1. "Continue Intensive lessons: finish culture notes, practice and readings for every A2–B2 lesson and republish."
2. "Continue Intensive lessons: build the 23 in-depth lessons (declension, verb system, B2 themes) and republish."
3. "Continue Intensive lessons: add embedded videos with synced tappable Greek subtitles."
4. "Continue Vocabulary to 4000 words from build/NEXT."
5. "Continue C1 content: write the C1 lessons from data/c1/ and wire them into course.json."
6. "Continue Slang units: finish slang-*.json and the colloquial lexicon, wire into course.json."
7. "Polish the app UI (visual pass) and republish."

### Thread stopping points (each thread appends its own below)


### 2026-10-18 · Intensive lessons with practice and readings (preview v16)
- What changed: Word lookup on any Greek word (tap, or hover with a mouse): `app/lookup.js` builds accent-insensitive inflected forms from the lexicon plus Holton's irregular table, `lessons/lookup-extra.json` (function words, irregular forms) and `lessons/lookup-gloss.json` (758 glosses for words in lesson pages), plus each reading's own `gloss`. Popup has "+ Add to my words". Coverage checker: `node tools/check_lookup.js [--all] lessons/x.json`.
- English→Greek spaced vocab recall (`progress.vocab`, interval ×2.5 per correct recall, known at 90 days) is appended to every lesson's practice (lesson field `vocab` = priority lemmas), plus a Daily "Word recall" lesson (gym-words.json). Vocab and reading questions are scored separately from grammar mastery.
- New blocks: `culture`, `reading` (text, en, gloss, questions → comprehension items), `video` (from lessons/videos.json, synced subtitle line with tappable words; not populated yet). Tracker: words known/4000, words in recall, reading passed (course.json `reading: true`, set by `python3 tools/sync_course.py`).
- Removed UI metadata only: source citations, section eyebrows, goal lines, intro blurbs, unit notes (cite/section stay in the JSON). Credits moved to #credits. New look: photo hero, card depth, reading pages on paper.
- All 52 existing lessons enriched: culture note each, extra production practice (≈30-35 items), `vocab` lists, readings in all A2-B2 lessons (40). New units: "A2 · Declension workshop" (decl-masculine/feminine/neuter/stress), "B1 · Verb workshop" (verbs-aorist-stems, -aorist-irregular, -aspect-future-subj, -passive-stems, -passive-continuous, -clitics, -na-clauses), "B2 · Themes" (theme-work/society/environment/technology/health). 68 lessons live, 56 with readings.
- Videos: YouTube captions/audio are bot-blocked from the container, so subtitles must come from Wikimedia Commons TimedText (el.srt, needs a User-Agent) or archive.org; no videos.json written yet.
- Where: /mnt/project-files/app/ (app.js, lookup.js, app.css, lessons/); preview https://claude.ai/artifact/SXiVDwZ4P84iJcP87Abd24 (v16). Briefs: tomorrow's commands below are self-contained.

#### Tomorrow (paste one line per message in the "Intensive lessons with practice and readings" thread)
1. `Write the 4 lessons decl-adjectives-2, decl-pronouns, decl-noun-phrase, decl-vocative into the A2 Declension workshop unit (same format as decl-masculine.json), then republish.`
2. `Write verbs-aspect-imperative (continuous vs perfective imperatives, μη(ν) + να, clitics, irregular imperatives) into the B1 Verb workshop unit, then republish.`
3. `Write theme-education and theme-culture into the B2 Themes unit (same format as theme-work.json), then republish.`
4. `Find 8-14 Greek-audio videos with accurate timed Greek subtitles (Commons TimedText or archive.org), write lessons/videos.json, test that embeds play in the preview, then republish.`
5. `Re-run the lookup coverage crawl on all lessons, gloss the remaining misses (incl. Ηράκλειο, χανόντουσαν) into lookup-gloss.json, then republish.`
6. `Check the new lessons in the preview against Holton (spot-check 10 forms per lesson) and fix any errors.`
7. `Add the C1 lesson files already in app/lessons/ (c1-*.json, from the C1 thread) and any slang lessons to course.json as new units, then republish.`

### 2026-10-18 · Library add-ons roadmap (thread "Add-ons for serious study")
Add-ons live in a Library section of the app (`#library`), built as a separate module `app/library.js` with content under `app/library/` (manifest `app/library/index.json`: new readings, sheets or tables are added by dropping a JSON file in and listing it, no app.js change). app.js gets only a small hook (`window.Ellinika` helpers + `window.EllinikaAddons` routes). Paste one line per message in the "Add-ons for serious study" thread, in this order:
1. `Library 1 · Grammar tables: articles, all noun paradigms, adjectives, pronouns, model verb conjugations, the searchable irregular-verb table, numerals, from data/grammar, then republish.`
2. `Library 2 · Table links: add a "Table" button in the word-lookup popup that opens the paradigm for that word's pattern, then republish.`
3. `Library 3 · Graded stories: write 12 original short stories (4 each A2, B1, B2) with glosses, comprehension questions and vocab lists into app/library/stories/, then republish.`
4. `Library 4 · Classic short stories: take 6 public-domain Greek stories (Παπαδιαμάντης, Βιζυηνός, Καρκαβίτσας, Wikisource) in excerpts, add B2/C1 glosses, notes on katharevousa forms and questions, then republish.`
5. `Library 5 · News reader: collect 15 openly licensed Greek news texts (el.wikinews, CC BY) on B2 themes, add glosses, exam-style questions and key vocab, then republish.`
6. `Library 6 · Exercise sheets: printable worksheets generated from the grammar data (declension grids, conjugation grids, case transformations, aspect choice) with answer keys and print CSS, then republish.`
7. `Library 7 · Paradigm drill: fill-the-whole-table drills for any noun, adjective or verb pattern, scored into the tracker, then republish.`
8. `Library 8 · B2 exam practice: turn the B2 sample papers in data/c1/syllabus/sample-papers into timed reading and language-use sections with scoring, then republish.`
9. `Library 9 · Writing and speaking workshop: B2 prompts from writing-speaking-prompts.json with model answers, phrase banks and self-check rubrics, then republish.`
10. `Library 10 · Conversation phrasebook: discourse and argument phrases for intellectual conversation (opinion, hedging, conceding, contrasting), tappable and added to recall, then republish.`
11. `Library 11 · Backup: export and import progress as a JSON file, so progress survives a browser reset, then republish.`

### 2026-10-18 · Add-ons for serious study · Library 1 landed (preview v17)
- What changed: Library hub (`#library`, linked from the home hero and footer) and Grammar tables (`#ref.articles|nouns|adjectives|pronouns|verbs|irregular|numerals`) rendered straight from data/grammar: all 31 noun paradigms with "find a noun's pattern" search, 11 adjective paradigms with search, comparison, pronouns, model conjugations (είμαι, χάνω, αγαπώ, θεωρώ, κοιμάμαι, έχω), the 166-verb irregular table with filter, numerals. Greek in tables is tappable for lookup; book § references are hidden; print CSS included.
- Hook: app.js exposes `window.Ellinika` (helpers) and routes any hash found in `window.EllinikaAddons` to it; index.html loads `library.js` before app.js; tools/bundle_preview.py inlines library.js and copies app/library/. Shelves are listed in app/library/index.json (`ready: true` makes one live).
- Publish note: bundle with `python3 tools/bundle_preview.py OUT`, then delete OUT/data/c1 and OUT/data/lexicon/build before publishing (c1 holds 65 MB of PDFs/MP3).
- Next: roadmap item 2 (Table links in the lookup popup).

### 2026-10-18 · Add-ons for serious study · Library 2 landed (preview v18)
- What changed: the word-lookup popup shows "Table ↗" for nouns, adjectives and verbs; it opens `#ref.<tab>~<word>`, which fills the pattern search (nouns/adjectives) or filters the irregular-verb table, falling back to the model conjugations for regular verbs.
- Where: app.js (REF_TAB + one line in showLookup), library.js (routes.ref). Next: roadmap item 3 (graded stories).

### 2026-10-18 · Add-ons for serious study · Library 3 (partial) and 11 landed (preview v21)
- What changed: reading-shelf reader in library.js (`#stories`, `#classics`, `#news` share one renderer: text on paper, tappable lookup with per-text glosses via `Ellinika.setGloss`, English translation toggle, notes, questions scored into `progress.library["<shelf>/<id>"]`, "Add all to my words"). 4 graded stories in app/library/stories/ (A2 a2-klidi, a2-laiki; B1 b1-karavi; B2 b2-giagia), lookup misses glossed to zero. Backup page `#backup` saves/restores progress as JSON; the preview declares the `downloads` capability for the save.
- Story file format: {el, title, level, author?, paras:[{el,en}], gloss:{form:"lemma — meaning"}, notes:[], questions:[{q,options,answer,why?}], vocab:[lemma]}; list it in the shelf's index.json. Check lookup misses with the playwright snippet pattern (click every `.story .w`, count "Not in the word list").
- Next (paste in the "Add-ons for serious study" thread): `Library 3 · Write 8 more graded stories (2 A2, 3 B1, 3 B2) into app/library/stories/, gloss lookup misses to zero, then republish.` then roadmap items 4-10 in order (item 11 done).
- 2026-10-18 (preview v22): +2 stories (b1-kafeneio, b2-metanastis), 6 total, all lookup misses glossed. Remaining for Library 3: 2 A2, 2 B1, 2 B2.

### 2026-10-18 · Add-ons for serious study · stopping point (preview v22)
- Live: Library 1 (grammar tables), 2 (table links), 3 partial (6 graded stories), 11 (backup). All files valid.
- Started, not published: Library 4. app/library/classics/vizyinos-amartima.json (Βιζυηνός opening, 3 paras, monotonic, translation, ~120 καθαρεύουσα glosses, notes, questions) is written; raw Wikisource texts are in app/library/classics/src/ (oneiro.txt = Παπαδιαμάντης «Όνειρο στο κύμα», amartima.txt). Polytonic→monotonic converter: copy the mono.py logic (strip breathings/iota subscript, circumflex/grave→acute, unaccent monosyllables, ποῦ/πῶς keep accent). Wikisource needs a User-Agent and rate-limits fast bursts.
- Resume with these, one per message in the "Add-ons for serious study" thread:
  1. `Library 4 · Wire the classics shelf: write app/library/classics/index.json with vizyinos-amartima, add a Παπαδιαμάντης «Όνειρο στο κύμα» excerpt (paras 1, 2, 5 of src/oneiro.txt) and 4 more public-domain excerpts, gloss lookup misses to zero, set the shelf ready, then republish.`
  2. `Library 3 · Write 6 more graded stories (2 A2, 2 B1, 2 B2) into app/library/stories/, gloss lookup misses to zero, then republish.`
  3. Then roadmap items 5, 6, 7, 8, 9, 10 using the paste lines in the roadmap entry above.

### 2026-10-18 · C1 content and lessons (stopped for the daily limit)
- What changed: 10 C1 lessons written as new files, same JSON shape as b2-*.json, each with rules/tables, a culture note, an original reading with gloss and questions, and practice; all render without errors in a test copy of the app. Unit 12 learned morphology: c1-internal-augment, c1-active-participles, c1-present-participles, c1-learned-nouns, c1-learned-verbs, c1-learned-phrases. Unit 13 argument and register: c1-nominal-style, c1-register, c1-hedging, c1-emphasis. Raw material: 49 C1 reading texts (Wikipedia, public-domain literature incl. Cavafy/Papadiamantis/Psycharis, Constitution and EU Charter, opinion excerpts, speeches) with sources; CGL Γ1 sample papers and specs (partly processed). Phrase and video gathering stopped before writing output.
- Where: app/lessons/c1-*.json; course.json entries ready to paste in data/c1/course-c1-units.json; data/c1/texts/ (index.json, sources.json), data/c1/syllabus/; lesson builder scripts and test harness in data/c1/lesson-src/
- Next: see Tomorrow below.

#### Tomorrow (C1), paste one line per task into the project chat
1. `Lessons thread: append the two units in data/c1/course-c1-units.json to course.json after B2 Unit 11 and un-grey C1 on the ladder.`
2. `C1 thread: finish data/c1/syllabus (README, sources.json, check c1-spec.json and writing-speaking-prompts.json are complete).`
3. `C1 thread: build data/c1/phrases (idioms 250+, learned phrases 150+, collocations 200+, connectors 80+), each item with Greek, meaning, register, example and source URL (el.wiktionary first).`
4. `C1 thread: find 8-15 Greek C1 videos with timed Greek captions and write data/c1/videos/videos-c1.json in the lessons/videos.json schema, then hand it to the lessons thread.`
5. `C1 thread: write Unit 13 remainder (c1-connectors, c1-collocations) from data/c1/phrases, and Unit 14 idiom (c1-idioms-1, c1-idioms-2, c1-ancient-sayings, c1-language-question).`
6. `C1 thread: write Unit 15 authentic readings (society, science, literature, law) from data/c1/texts with gloss and questions, and attach the Γ1 sample reading tasks.`

### 2026-10-18 · Colloquial Greek units (stopped for the daily limit)
- What changed: nothing built yet. Read the lesson format and lookup code; wrote the unit plan (13 slang lessons) and format notes.
- Where: `/mnt/project-files/data/colloquial/PLAN.md`
- Tomorrow (paste in the "Colloquial Greek units" thread):
  - `Build slang lessons 1-4 from data/colloquial/PLAN.md, plus colloquial-lexicon.json entries and SOURCES.md for them`
  - `Build slang lessons 5-8 (youth, swearing, insults, nightlife) from data/colloquial/PLAN.md`
  - `Build slang lessons 9-13 (regional and dialogues) from data/colloquial/PLAN.md, then send the file list and course.json entries to the coordinator`
- For the app thread, once lessons land: add `colloquial/colloquial-lexicon.json` to lexicon() in app.js and a "Colloquial Greek" unit to course.json.

### 2026-10-18 (day 2) · Add-ons for serious study · Library 4 landed (preview v23)
- Classic stories shelf live (`#classics`): Βιζυηνός «Το αμάρτημα της μητρός μου» (opening, 3 paras) and Παπαδιαμάντης «Όνειρο στο κύμα» (7-paragraph excerpt: goats, Moschoula at the window), both monotonic, translated, fully glossed (0 lookup misses), notes on καθαρεύουσα forms, questions. Sources: Greek Wikisource raw text in app/library/classics/src/ (not published).
- Publishing note: other threads publish lessons/ to the same artifact; publish only library/ files plus index.html, never lessons/.
- Library 6 landed (preview v24): `#sheets` with 4 self-checking, printable, regenerable sheets built from the data: noun declension grids (lexicon nouns × Holton paradigm via app.js `derive`, unsafe words skipped), article+adjective+noun phrases in all 6 case/number cells, present-tense conjugation (groups A, B1 αγαπώ-type, B2 θεωρώ-type), irregular verb principal parts (Holton table, verbs in the 3000 list). Scores in `progress.library["sheets/<id>"]`. Known gap: derive follows the model, so rare exceptions (e.g. φίλη gen. pl. φίλων) can come out as the model's φιλών.
- Library 7 landed (preview v25): `#drill` lists every Holton noun, adjective and verb-tense paradigm (31 + 11 + verb tenses); `#drill.<id>` is a blank whole-table to fill, with Check, answers, and "Another word, same pattern" (only words the analogy builds safely). Scores in `progress.library["drill/<id>"]`, chips turn green at 90%+. Not yet counted in the home tracker (that is app.js, lessons thread).
- Library 8 landed (preview v26): `#exam` runs the 17 official sample tasks in data/c1/syllabus/reading-tasks.json (Γ1 level; gap-fill, headings, multiple choice, summary gaps, error spotting, word formation, synonyms) with a timer, dropdown/radio/typed answers, marking against the key (letters or full options, "a / b" alternatives, accent-tolerant), suggested corrections, scores in `progress.library["exam/<id>"]`. Only B2 oral/writing samples exist locally, so the B2 versions of these tasks still need sourcing.
- Publish recipe now: `python3 tools/bundle_preview.py OUT`, delete OUT/data/lexicon/build, OUT/data/colloquial, OUT/library/classics/src, and every file under OUT/data/c1 except syllabus/reading-tasks.json and syllabus/writing-speaking-prompts.json. Publish only index.html + library/ + those two data files (lessons/ belongs to the lessons thread).
- Library 3 complete and Library 10 landed (preview v27): 12 short stories now (A2 ×4, B1 ×4, B2 ×4: added a2-farmakeio, a2-paralia, b1-pascha, b1-enoikio, b2-ergasia, b2-perivallon), all 0 lookup misses. `#phrases` conversation phrasebook: 14 situations, 95 phrases with register and example, tappable lookup, and `#phrases.practice` English→Greek recall with spaced intervals in `progress.library.phr`.

### 2026-10-18 (day 2) · Intensive lessons · preview v28
- New lessons wired into course.json: decl-adjectives-2, decl-pronouns, decl-noun-phrase, decl-vocative (A2 · Declension workshop, now 8 lessons); verbs-aspect-imperative (B1 · Verb workshop, now 8); theme-education, theme-culture (B2 · Themes, now 7). C1 Units 12–13 appended, C1 un-greyed on the tracker (excluded from the B2 grammar score).
- Accuracy review of 30 lessons (decl-*, verbs-*, theme-*, c1-*): about 70 fixes (over-general rules, second-correct mc distractors, wrong accept variants, factual softening). No wrong paradigms found.
- Lookup: crawl of all 86 lessons found 1,461 unresolved words; all glossed into lessons/lookup-gloss.json (now 2,379 entries), 159 wrong stem guesses corrected. lookup.js `build()` now also takes data/lexicon/forms-index.json (vocab thread) and names.json; core-4000.json is gone from lexicon(). tools/check_lookup.js uses the same sources.
- UI: tables with 3+ columns stack into labelled cards on phones; hidden popup no longer leaves a stray dot; Greek eyebrows unaccented capitals; course title "Modern Greek, from A1 to C1".
- Pending: videos.json (videos agent still working; 6 videos so far), slang-*.json are in lessons/ but not wired (waiting for the slang thread's course entries).

### 2026-10-18 · C1 content and lessons (day 2, stopped at the usage limit)
- What changed: 16 more C1 lessons (26 total, all render-tested): Unit 13 adds c1-connectors, c1-collocations; Unit 14 idiom: c1-idioms-1, c1-idioms-2, c1-ancient-sayings, c1-language-question, c1-read-register-speeches; Unit 15 reading: c1-read-philosophy, -history, -society, -science-tech, -cavafy, -prose. 22 C1 TEDx videos with human Greek subtitles (Amara) + English lines, 831 cues, each tagged with a C1 lesson id. Γ1 syllabus complete (exam spec, 43 can-dos, 17 official reading/use-of-language tasks with keys, writing/speaking prompts). Phrase data partial (learned-phrases.json only).
- Where: app/lessons/c1-*.json; course entries for all C1 units in data/c1/course-c1-units.json (rebuild: `python3 data/c1/lesson-src/build_course_units.py`); videos in data/c1/videos/videos-c1.json (lessons/videos.json schema); data/c1/syllabus/, data/c1/texts/, data/c1/lesson-src/
- Next (lessons thread): replace the C1 units in course.json with those in data/c1/course-c1-units.json; merge data/c1/videos/videos-c1.json into lessons/videos.json; add `.rd-text p { white-space: pre-line }` to app.css so poem line breaks show in c1-read-cavafy.

#### Tomorrow (C1), one line per task
1. `Lessons thread: sync course.json C1 units from data/c1/course-c1-units.json, merge data/c1/videos/videos-c1.json into lessons/videos.json, add .rd-text p { white-space: pre-line } to app.css.`
2. `C1 thread: resume the "C1 law, press, exam practice" agent to write c1-read-law, c1-read-press, c1-exam-reading, c1-exam-language (brief: scratchpad lesson_brief.md, copy in data/c1/lesson-src/lesson_brief.md).`
3. `C1 thread: resume the phrases agent to finish data/c1/phrases (idioms, collocations, connectors, sources, README).`
4. `C1 thread: build a C1 word list (1,000 words beyond core-4000) from data/c1/texts and the video cues, hand it to the vocabulary thread.`

### 2026-10-18 14:10 · Colloquial Greek units (checkpoint)
- What changed: 12 of 13 slang lessons written in app/lessons/ (discourse, everyday, idioms, youth, swearing, insults, nightlife, athens-thessaloniki, crete, cyprus, regions, dialogues), each 50-87 KB with tables, strength ratings 0-5, dialogues, culture, reading, ~45-50 practice items. slang-morphology still being written. Merged lexicon: data/colloquial/colloquial-lexicon.json (784 entries so far, core-3000 shape + register/strength/region/lesson). Tools: data/colloquial/tools/merge_check.py (merge parts + validate), check_lookup_colloquial.js (lookup coverage incl. colloquial lexicon).
- Not yet wired: course.json unit and lexicon() loading are for the lessons thread (see final entry).

### 2026-10-18 · C1 content and lessons (checkpoint 14:10 UTC)
- What changed: the four remaining lessons are in and render-tested: c1-read-law, c1-read-press (Unit 15), c1-exam-reading (official ΚΕΓ Γ1 reading tasks with keys, 61 questions), c1-exam-language (use-of-language tasks plus the Γ1 writing/speaking prompts and criteria). C1 now has 28 lesson files in 5 units (12-16); a script check confirms every mc answer is among its options. Tomorrow-list items 2 is done; item 3 (phrases) and item 4 (C1 word list, ~1,200 lemmas beyond the lexicon, in the lexicon schema, at data/c1/words/c1-words.json) are running.
- Where: data/c1/course-c1-units.json now lists Units 12-16 (27 entries; rebuild with `python3 data/c1/lesson-src/build_course_units.py`)
- Next: **lessons thread**: replace the C1 units in course.json with all five units from data/c1/course-c1-units.json; merge data/c1/videos/videos-c1.json (22 videos) into lessons/videos.json; add `.rd-text p { white-space: pre-line }` to app.css for the Cavafy poems. **Vocabulary thread**: data/c1/words/c1-words.json can be merged as a C1 layer once it lands.

### 2026-10-18 14:25 · Vocabulary: quality and lookup coverage (checkpoint)
- Lexicon: 5,692 entries (core-1000.json 968 + core-3000.json 4,724), all with gloss, example, translit, CEFR; round 2 added 1,240 words found in the new slang, Ancient-quote, C1, decl/verbs/theme lessons. Duplicate spellings (γαμάω/γαμώ, ξενυχτάω/ξενυχτώ) folded.
- data/lexicon/forms-index.json: 71,666 inflected forms → lemma. data/lexicon/names.json: 294 names/places, same "Name|gloss" format as app/lookup-gloss.json.
- **For the lessons thread (lookup misses):** app lookup still finds no entry for 3,230 distinct words (5,712 tokens of 148,062). The lexicon now covers most of them through forms-index.json and names.json, which lookup.js does not read yet. Please wire both into lookup.js build(): try the exact lowercase form in forms-index, then the accent-stripped form, then names.json. Words classified "fragment"/"other" in data/lexicon/build/misses/*.out.json (endings, abbreviations, deliberately wrong quiz options) should stay unmatched.
- Round 3 running: 2,229 still-unknown words (mostly c1-* readings, slang-*), batches build/misses/s00–s11.
- Merge command after any new outputs: `python3 /mnt/project-files/data/lexicon/build/finalize.py --write` (idempotent).

### 2026-10-18 · C1 content and lessons (phrase bank)
- What changed: phrase datasets complete in data/c1/phrases/ (idioms 406, learned phrases 335, collocations 359, connectors 175; sources + README). Generated 20 phrase-bank lessons (c1-bank-idioms-1..8, -collocations-1..6, -learned-phrases-1..4, -connectors-1..2), each a table of 22-60 items plus meaning (mc) and production (type) practice, skipping phrases already taught in the hand-written C1 lessons. Render-tested.
- Where: app/lessons/c1-bank-*.json; generator data/c1/lesson-src/phrase_bank.py; data/c1/course-c1-units.json now has Units 12-17 (47 lessons).
- Next: **lessons thread**: sync all C1 units (12-17) into course.json from data/c1/course-c1-units.json.

### 2026-10-18 · Colloquial Greek units (all 13 lessons done)
- What changed: 13 colloquial lessons in app/lessons/: slang-discourse, slang-everyday, slang-idioms, slang-morphology, slang-youth, slang-swearing, slang-insults, slang-nightlife, slang-athens-thessaloniki, slang-crete, slang-cyprus, slang-regions, slang-dialogues. Each 51-87 KB, same JSON shape as theme-*.json (blocks text/table/examples/callout/culture/rules/reading; practice type+mc, 44-51 items each), with 0-5 strength ratings, register notes, comebacks, dialogues, pronunciation, culture and a glossed reading. All pass data/colloquial/tools/merge_check.py (valid JSON, answers in options/accept, gloss keys in text, vocab lemmas resolvable) and reading lookup coverage is 0 misses with the colloquial files loaded.
- Data: data/colloquial/colloquial-lexicon.json (927 entries, core-3000 shape + register/strength/region/lesson; pos "phrase" for multi-word items), data/colloquial/colloquial-lookup.json (85 surface forms, lookup-extra format "form": "lemma|gloss"), data/colloquial/SOURCES.md (all sources; unverified items flagged there), course entries in data/colloquial/course-colloquial-units.json (4 units, flag "colloquial": true).
- **For the lessons thread** (owner of app.js/course.json), three changes wire it in:
  1. app.js lexicon(): add "colloquial/colloquial-lexicon.json" to the file list (needed for vocab-recall on the slang lessons and for tap lookup). Entries have no rank, so they sort after core words in fresh-word picks; filter on `register` if colloquial words should stay out of the core vocab counts.
  2. app.js lookupIndex() and tools/check_lookup.js: merge data/colloquial/colloquial-lookup.json into the extra map, like lookup-extra.json.
  3. course.json: append the 4 units from data/colloquial/course-colloquial-units.json after the B2/C1 units (or as a separate track); keep them out of the B2 tracker (like daily units) unless Devon wants them counted.
- Not done: no in-browser render test of these files (structure checked by script only; same block types as live lessons).

### 2026-10-18 (day 2) · Intensive lessons · preview v29: slang and C1 wired in
- course.json: C1 units replaced by Units 12-17 from data/c1/course-c1-units.json (47 lessons); 4 Colloquial units appended from data/colloquial/course-colloquial-units.json (13 slang lessons). 25 units, 136 lessons. Tracker: C1 and Slang each get a bar but stay out of the B2 overall score and the Reading bar.
- app.js: lexicon() also loads colloquial/colloquial-lexicon.json; lookupIndex() merges colloquial/colloquial-lookup.json (plus names.json and forms-index.json from v28). Videos load from lessons/videos.json AND lessons/videos-c1.json (a copy of data/c1/videos/videos-c1.json, 22 TEDx talks); re-copy if the C1 thread updates it. tools/check_lookup.js uses the same sources.
- app.css: `.rd-text p { white-space: pre-line }` for the Cavafy poems.
- Smoke-tested all 13 slang lessons and 3 new C1 lessons (load + 30-83 practice items each).
- Running: videos agent (lessons/videos.json), new lessons for B2 themes 2 (travel, family, economy, city), an A2 "Everyday situations" unit (sit-*), a B2 "Exam skills" unit (exam-*). Not yet in course.json.
- Tomorrow (intensive-lessons thread): `Wire theme-travel/family/economy/city, sit-*, exam-* into course.json, review them for accuracy, re-run the lookup crawl, republish`.

### 2026-10-18 (day 2) · Add-ons for serious study · continued
- Library 9 landed (preview v30): `#writing` workshop is live. 14 writing tasks (2 official B2 tasks + 6 original B2 tasks with ~200-word model answers and translations, 4 official Γ1 prompts + 2 original Γ1 prompts without models), each with plan, phrase bank, register notes, live word count against the target, timer and an 8-point self-check rubric; drafts are saved in `progress.library.drafts` (so Backup carries them), finished tasks in `progress.library["writing/<id>"]`. 18 speaking tasks: part 1 warm-up, 10 part-2 questions (8 official + 2 picture tasks) and 7 part-3 role-card debates (4 official + 3 new), all with phrase banks and model answers. Every word looks up (gloss map in workshop.json, 0 misses).
- Library 5 landed (preview v31): `#news` is live with 7 B2 news texts (3 Greek Wikinews CC BY 2.5: Wikipedia strike, Ierapetra hospital protest, Nielsen consumer survey; 4 original texts: heatwave and the Acropolis, Attica water shortage, four-day week, tourism staff shortages), each translated, glossed (0 lookup misses), with register notes, 5 exam-style questions and vocab. A second worker is writing 5 more (technology, health, education, culture/media, phone ban); news/index.json is rebuilt from the files in news/ by the lead.
- Also in v31: two new exercise sheets, `#sheets.aorist` (simple past, all six persons) and `#sheets.passive-past` (-ηκα passive past), built from the lexicon's aorist forms. Plural stress moves to the antepenult and a stressed syllabic augment drops (έγραψα → γράψαμε); verbs with an internal augment (διέκρινα, εισήγαγα) are skipped because their plural cannot be derived safely.

- Preview v32: classics shelf now has 4 texts, adding Καρκαβίτσας «Η θάλασσα» (Λόγια της πλώρης, opening, 8 paras) and Θεοτόκης «Η τιμή και το χρήμα» (chapter 1 opening, 8 paras, Corfiot spelling kept and explained), both translated, glossed (0 misses), with notes and questions. Raw Wikisource text in classics/src/. Note: curly-apostrophe elisions (τ’ κ’) need the apostrophe kept in gloss keys.
- Preview v34: news reader complete with 12 B2 texts (added AI in schools, ΕΡΤ/ΣΕΕΜΟ, Facebook monkey photo, cancer study, US phone-while-driving ban; 0 lookup misses) and a new `#sheets.future` sheet: θα/να perfective forms for σ/ξ/ψ aorist verbs (έγραψα → γράψω) plus -θηκα/-τηκα passives (αγαπηθώ); irregular perfectives (είπα → πω, ήρθα → έρθω) are left to the irregular-verbs sheet.
- Preview v36: news reader at 18 texts (added Thessaloniki metro, Epidaurus festival, James Webb telescope, European elections, Athens rents, Athens 2004 legacy; originals, 0 misses) and classics at 6 (added Βικέλας «Λουκής Λάρας» opening, real καθαρεύουσα with notes, and Εφταλιώτης «Η βασιλόπιτα του Βαγγέλη»; 0 misses). The exam page now also loads library/exam/b2-tasks.json (B2 official sample + practice sets, listed before the Γ1 tasks); that file is being written.
- Preview v38: `#exam` now leads with B2. library/exam/b2-tasks.json holds 27 tasks / 220 questions: the official B2 sample series 1 (3 reading + 3 use-of-language tasks, transcribed from the PDFs with the official keys) and 3 original practice sets in the same layout, each with an extra case/agreement, verb-form or preposition+article drill. Every task scores 100% when filled with its key (scratchpad t15.js). Feedback now shows `answer_note` explanations, and summary tasks can reopen their source text.
- Preview v39: `#listening` shelf: 14 B2 listening items (3 announcements, 2 voicemails, 4 dialogues, 3 radio interviews, 2 reports; 65 questions) in library/listening/listening.json, read aloud line by line by the device's Greek speech voice (two voices if available, else pitch tells speakers apart; speed control), exam-style questions with proof quotes, transcript with translation and per-line replay, a word-by-word dictation mode (`#listening.<id>~dict`), add-to-recall. Scores: `progress.library["listening/<id>"]`, dictation `["dict/<id>"]`. 0 lookup misses. Not heard on a real device yet: headless Chromium has no Greek voice, so only the no-voice fallback was tested.
- Preview v40: listening at 28 items (library/listening/listening-2.json adds ferry, library, bank, landlord, job interview, pharmacy, ΚΕΠ, neighbours, exam stress, regional cuisine, urban heat, half marathon, book fair, a monologue on adult language learning; 0 misses). New `#sheets.context` sheet: gaps a vocab word inside a real sentence from the stories and news, with the dictionary form and meaning as the hint, so the learner has to produce the inflected form.
- Preview v41: search box on the Library page and `#search.<query>`: one accent- and case-insensitive search over every lesson in course.json (blocks, practice, vocab), stories, news, classics, workshop tasks, listening scripts and the phrasebook, with highlighted snippets; the index is built on the first search. #exam also loads library/exam/b2-tasks-2.json (practice sets 4-6, being written).
- Preview v45: B2 practice sets 4-6 live (library/exam/b2-tasks-2.json, 21 tasks, 159 items; extra drills on genitives incl. -μα and feminine -ος, comparatives/superlatives, ο οποίος and clitics); all score 100% with the key (t20.js). Dropdown options are now shown alphabetically so their order no longer gives away the answer, and each task's overall answer_note appears after Submit. #exam now has 7 B2 sets (48 tasks) plus the Γ1 samples.
- Preview v46: `#mistakes` notebook (Library shelf «Τα λάθη μου»): every wrong answer from sheets, drills, exams, listening and phrase practice is logged in `progress.library.mistakes` (max 400, repeat misses counted), listed with what was written vs. the answer and a link back, and `#mistakes.review` drills the 20 most-missed (typed, or two-way choice for multiple choice); a right answer clears the entry. Backup carries it.
- Preview v47: `#mock` mock exam (Library shelf «Δοκιμαστική εξέταση»): pick a B2 set (official or practice 1-6), Start clears earlier scores for its parts and starts the clock; the paper page lists its reading and use-of-language tasks, two random listening items (one long, one short) and one B2 writing task, each opened on its own page with scores collected back; writing is scored by ticking the 8-point rubric. Finish shows each skill against the real pass mark (60% in every skill, per the ΚΕΓ 2022 guide in data/c1/syllabus/spec-docs/odigos_ell_2022.txt) and keeps attempt history in `progress.library.mock`.
- Preview v48: the artifact now declares capabilities `{downloads: true, sample: {}}` (other threads: omit `capabilities` when publishing so this carries forward). Workshop writing tasks get a "Feedback from Claude" button (examiner-style: scores per criterion group, corrected text, numbered error list with case/agreement first, better phrases, next step; streams in) and speaking tasks get "Practise this with Claude" (typed conversation in Greek where Claude plays role Β or the examiner and flags case errors with ✎). Both use the viewer's own Claude usage, ask permission on first use, and stay hidden where `sample` is unavailable. Not exercised in the real viewer yet (headless test confirms they hide cleanly). A microphone recorder is not possible: no microphone capability exists for artifacts.
- Preview v50: graded stories at 18 (added B1 name day in Thessaloniki, night KTEL bus, student flat; B2 Ikaria panigyri, ministry bureaucracy, olive-grove inheritance; 0 misses). Note: this bundle also carried the lexicon thread's collocation popup code from app.js (collocations.json loads lazily and fails quietly if not yet published).
- 20:51 · **v51 Expression trainer** (#expr): 1,275 C1 phrases in four decks (connectors 175, collocations 359, idioms 406, learned phrases 335) from data/c1/phrases/. Browse with a filter, or practise English to Greek with a cloze from the example sentence; spaced schedule in progress.library.expr, misses go to Mistakes. Shelf added to library/index.json.

- 21:05 · **v52 Opinion articles** (#opinion): 6 original long-form άρθρα γνώμης (3 B2, 3 C1, 770–880 words each: brain drain, overtourism, English in Greek, remote work on the islands, the Parthenon sculptures, social media). Each paragraph is labelled with its argument role (Θέση, Αντίλογος, Αντίκρουση…) and its connectors are highlighted (toggle); "How the argument is built" outline; 6 questions; a 250–300 word reply box saved in drafts with Claude examiner feedback. Opinion texts also feed search and the context sheet. 0 lookup misses.

- 21:10 · **v53 Rebuild the argument** (#argue): the paragraphs of an opinion article are shuffled; tap them into order, Check marks each position and shows its role. Best score per article in progress.library["argue/<id>"].

- 21:27 · **v54 Opinion shelf at 12 articles**: added housing and young people (B2), φροντιστήρια and Πανελλήνιες (C1), wildfire prevention (B2), bureaucracy and gov.gr (C1), the diaspora and Greek schools abroad (B2), AI and work (C1). All in #argue too; 0 lookup misses.

- 21:30 · **v55 Summary writing**: every opinion article now has a 60–80 word Greek summary task (B2 exam type) above the reply box, draft saved in drafts["opinion/<id>~sum"], with Claude feedback that receives the full article and checks content kept or missed.

- 21:47 · **v56 Register converter** (#register): 36 messages (10 B1, 18 B2, 8 C1), half to formalise and half to make informal; rewrite, compare with a model and 6–7 annotated changes, self-check saved as progress.library["register/<id>"], draft saved, Claude feedback on register and errors. 0 lookup misses.

- 21:49 · **v57 Today's session** (#today, first shelf in the Library): a daily plan of about 100 minutes, fixed per day and rotating to undone material: expressions due, a B2 reading task, a language-use task, a listening item, an opinion article with summary, a writing task (or a register rewrite every third day), a speaking prompt, and mistakes review. Ticks in progress.library.today. Lessons thread may want to link #today from the home screen.

- 22:20 · **v59 Listening 50, exam sets 7–9**: listening-3.json and listening-4.json add 22 items (announcements, dialogues, interviews, voicemails, monologues, reports), 0 lookup misses; b2-tasks-3.json adds practice sets 7–9 (21 tasks, every key scores 100%). File lists are now EXAM_FILES and LISTEN_FILES in library.js (exam, listening, mock, search, Today). Exam route now loads library/exam/gloss.json for rarer words (being written: 303 forms).

- 22:24 · **v60 Exam text lookups**: library/exam/gloss.json (303 forms) loaded by the exam route; all 69 B2 tasks now have 0 lookup misses (checked with t29.js).

- 2026-10-19 00:11 · **v61 B2 practice sets 10–12**: b2-tasks-4.json (21 tasks; use-4 drills on accusative plural, passive aorist, future aspect), every key scores 100%, exam gloss now 396 forms so all 90 B2 tasks have 0 lookup misses; exam list and mock now include sets 7–12 (series prefixes match "b2-p1-" exactly, so p10+ group correctly).

- 2026-10-19 00:12 · **v62 Where to focus** (#focus, second Library shelf): average saved score per skill (B2 reading, language use, listening, sheets, drill, reading for meaning, C1) as bars against the 60% pass line, expression count, mistakes by kind over 30 days, and a "Do next" list of the lowest scores under 60% plus skills not yet tried.

- 2026-10-19 00:36 · **v63–v65 · ENDPOINT (Devon asked for a structured stop)**: the section formerly called "Add-ons for a serious learner" / "Library" is now **"Advanced level"** in the app (heading, tab title, crumbs, home-screen links in app.js) and in this thread's label; the route stays #library. v63 fixed the crawl's one page error (#drill.n-f-ω-b, a paradigm with no plural). v64 adds listening-5.json: 8 C1 items (debates, lectures, interviews, report, essay), 0 lookup misses, kept out of the B2 mock and Today. v65 adds exam/c1-tasks.json: C1 practice sets 1–3 (24 tasks, every key scores 100%), credited as original practice; exam gloss now 602 forms, 0 misses across all 114 practice tasks. State on disk = v65; the Netlify zip can be rebuilt from it.

#### Tomorrow (Advanced level thread), paste in the "Advanced level" thread (formerly the add-ons thread); kept current
1. `Lessons thread: count library scores (drill/, sheets/, exam/, stories/, writing/ in progress.library) in the home tracker.`
2. `Advanced level: check #listening, #mock and #today on a phone; try the Claude feedback buttons (workshop, opinion summary/reply, register). Next roadmap item if wanted: Γ1 writing and speaking tasks in the workshop with C1 rubric.`
3. `Lessons thread: count listening/ and dict/ scores in the tracker's comprehension bar.`

### 2026-10-18 14:55 · Vocabulary: quality and lookup coverage (checkpoint 2)
- Correction to checkpoint 1: lookup.js and check_lookup.js already read forms-index.json and names.json (thanks, lessons thread). With the app's real sources, lookup now finds 98.0% of the 217,464 Greek word tokens in all 165 lesson/library files (4,257 misses, 646 stem guesses).
- Lexicon: 7,075 entries (core-1000 968 + core-3000 6,107). Round 3 added 395 entries plus 1,299 form links (Papadiamantis/Vizyinos katharevousa, Cretan/Cypriot/Pontic words, slang). Merged data/c1/words/c1-words.json (253 C1 words) into core-3000. forms-index 86,514 forms; names.json 528.
- Running: round 4 on 1,446 still-unknown words (videos-c1, slang-morphology, c1-bank-*) as build/misses/t00–t07; forms for the C1 words as build/forms/f22–f23.
- When those land: `python3 /mnt/project-files/data/lexicon/build/apply_forms.py --write && python3 /mnt/project-files/data/lexicon/build/finalize.py --write`. Coverage (same sources as the app): `cd /tmp && node /mnt/project-files/data/lexicon/build/misses/cov.js`.

### 2026-10-18 15:30 · Vocabulary: quality and lookup coverage (checkpoint 3)
- Lexicon 7,963 entries (core-1000 968 + core-3000 6,995); forms-index 99,801 forms; names.json 649. 0 entries missing gloss/example/translit/CEFR; 16 flagged needs_review (rare dialect words).
- Lookup coverage with the app's own sources: 99.65% of Greek word tokens in all lesson/library files resolve (802 misses of ~230k, mostly abbreviations such as ΚΕΓ, ΤΝ, κτλ and ending fragments).
- Same-word dedupe now keeps accent pairs apart (θόλος/θολός, πότε/ποτέ) and folds -άω/-ώ and unaccented spellings.
- Running: corpus-gap pass build/misses/c00–c07: 1,556 frequent subtitle words absent from the index (άνδρες, λάθη, ήλπιζα, σκύλα…) plus core gaps (μέτρο, χρονιά, όποιος, απλώς, έως, the hundreds 500–900). Merge after: `python3 /mnt/project-files/data/lexicon/build/finalize.py --write`.

### 2026-10-18 (day 2) · Intensive lessons · preview v33
- New units in course.json: "A2 · Everyday situations" (sit-shopping, sit-eating-out, sit-getting-around, sit-health, sit-home-services), "B2 · Exam skills" (exam-writing-informal, exam-writing-formal, exam-writing-essay, exam-speaking, built on the official B2 sample papers in data/c1/syllabus), and B2 · Themes now 11 (+travel, family, economy, city). All 13 reviewed: 34 fixes (mostly τη/δε before vowels or stops in accept lists, missing enclitic accents, two second-correct mc options, two over-general rules).
- Lookup: crawl of all 149 lessons (with forms-index, names, colloquial sources) found 1,538 misses + 133 wrong guesses; all glossed into lessons/lookup-gloss.json (now 4,050 entries). Re-check: 2 misses left. Crawl scripts: scratchpad crawl.js + misses.js (session-local; recreate from tools/check_lookup.js if the scratchpad is gone).
- videos.json: 9 videos (videos agent still running); videos-c1.json re-copied from data/c1/videos.
- Tomorrow (intensive-lessons thread): `Finish videos.json and republish`; `Write more intensive lessons where the course is thin (B1 Unit 7 clauses in depth, B2 word formation drills)`; `Re-run the lookup crawl after any new lessons`.

### 2026-10-18 15:55 · Vocabulary: quality and lookup coverage (checkpoint 4)
- Lexicon 8,214 entries (core-1000 968 + core-3000 7,246); forms-index 101,246 forms; names.json 1,781 (now includes the foreign first names and places common in film subtitles, so tapping «Τζακ» or «Νέα Υόρκη» in a video works).
- Lesson lookup with the app's sources: 99.88% of 233,121 Greek word tokens resolve (274 misses, mostly abbreviations and drill fragments).
- Corpus-gap pass done: added μέτρο, χρονιά, όποιος, απλώς, έως, δεσποινίς, the hundreds 500–900 and ~250 frequent subtitle words; αδελφός folded into αδερφός.
- Running: second quality spot-check on 300 random lesson-vocabulary entries (build/spotcheck2a/2b); finalize.py applies every spotcheck*.out.json.
- 16:05 spot-check 2: 300 random lesson-vocabulary entries reviewed, 10 needed a change (~3%, all forms/models, no wrong glosses or bad examples). Fixes applied, plus a sweep restoring missing accents on 58 adjective feminine/neuter forms (παραγωγική, ορθό…).

### 2026-10-18 · C1 content and lessons (day 2 complete)
- What changed: C1 word list done: 1,232 lemmas beyond the lexicon (ranks 5001-6232) in the lexicon schema plus `topic` and `seen_in`; the vocabulary thread is already merging it. All C1 items from the earlier Tomorrow lists are now done: 47 C1 lesson files in Units 12-17, 22 subtitled videos, 49 texts, Γ1 syllabus, 1,275 phrases, 1,232 words.
- Where: data/c1/words/c1-words.json (README, sources); course entries data/c1/course-c1-units.json; videos data/c1/videos/videos-c1.json
- Next: see Tomorrow.

#### Tomorrow (C1), one line per task
1. `Lessons thread: sync C1 Units 12-17 from data/c1/course-c1-units.json into course.json, merge data/c1/videos/videos-c1.json into lessons/videos.json, add .rd-text p { white-space: pre-line } to app.css, then publish.`
2. `C1 thread: add c1-writing lessons: the four Γ1 writing prompts in data/c1/syllabus with model answers, annotated for connectors, register and nominal style.`
3. `C1 thread: build 15 more subtitled videos from data/c1/videos/amara-greek-tedx-index.json for lessons that have fewer than 2 videos.`
4. `C1 thread: fact-check the culture blocks in c1-read-history, c1-read-society and c1-read-register-speeches against sources.`

### 2026-10-18 19:30 · Vocabulary: collocations for production practice (stopping point)
- New file data/lexicon/collocations.json (838 KB): `{"about", "entries": {lemma: {collocations:[{el,en}], synonyms:[], antonyms:[], family:[]}}}` for the 2,000 most frequent content words (7,580 collocations). Example: απόφαση → παίρνω απόφαση / make a decision, οριστική απόφαση, απόφαση του δικαστηρίου; family αποφασίζω, αποφασιστικός, αναποφάσιστος.
- **For the lessons thread:** worth showing in the word lookup card and in vocabulary review (e.g. a "use it" step: give the English collocation, the learner produces the Greek). Load lazily; it is keyed by the same lemma as core-*.json.
- Lexicon state: 8,214 entries, 101,246 forms, 1,781 names; lesson lookup 99.9%; spot-check error rate ~3% (forms only).
- Tomorrow (paste into the project chat):
  1. "Vocabulary: extend collocations to the next 2,000 words (data/lexicon/build/brief_colloc.md, batches like build/colloc/)."
  2. "Vocabulary: after new lessons land, run `cd /tmp && node /mnt/project-files/data/lexicon/build/misses/cov.js` and resolve misses with build/brief_misses.md, then `python3 /mnt/project-files/data/lexicon/build/finalize.py --write`."
  3. "Vocabulary: review the 17 needs_review entries in core-3000.json."

### 2026-10-18 (day 2, evening) · Intensive lessons · preview v35
- New units: "B1 · Sentence workshop" (clauses-relative, -conditional, -time-cause, -reported; reviewed, 19 fixes) after B1 Unit 7; "B2 · Word-building workshop" (words-nouns, -adjectives, -verbs, -families; review running) after B2 Unit 10. b2-indirect softened to "no obligatory backshift".
- lessons/videos.json final: 11 Commons videos (2 A2, 2 B1, 7 B2), Whisper timings + hand-corrected Greek; doubtful phrases listed in the videos agent's notes (scratchpad/video/).
- Publish note: library/* files belong to the add-ons thread; this thread now publishes only lessons/*, data/lexicon/* and index.html (bundle from the app folder so index.html carries everyone's latest app.js/library.js).
- Word-building review: 23 fixes applied, republished as v37.
- Tomorrow (intensive-lessons thread): `Re-run the lookup crawl over all 157 lessons and gloss new misses`; `More intensive lessons where thin: A1 situations, B1 vocabulary themes (food, home, body, weather), B2 listening tasks with the videos`.

### 2026-10-18 (day 2, night) · Intensive lessons · preview v42
- New unit "B1 · Vocabulary themes" (vt-food, vt-home, vt-body, vt-nature, vt-people; 48-49 items each, 12 vocab lemmas each not drilled elsewhere) after the B1 Sentence workshop; reviewed, 35 fixes. Course now 162 lessons.
- Lookup crawl over all 162 lessons: 3 misses left; lookup-gloss.json now 4,661 entries.
- Tomorrow (intensive-lessons thread): `Write B2 listening lessons built on lessons/videos.json (comprehension questions per video, dictation-style gap fills from the cues)`; `Write A1 everyday situations (greetings, numbers and time, café, family) for completeness`; `Re-run the lookup crawl after any new lessons (scratchpad crawl.js + misses.js, or tools/check_lookup.js --all per file)`.
- v43: new unit "B2 · Listening" (listen-a2, listen-b1, listen-b2-public, listen-b2-history) built on lessons/videos.json: key words, grammar heard, full transcript as reading, dictation gap-fills; each video's `lessons` array now lists its listening lesson. Reviewed against the cues: 20 small fixes, republished. Course: 166 lessons.
- v49: new unit "A1 · First situations" (sit-a1-meeting, -numbers-time, -cafe, -family) after A1 Unit 3; reviewed, 22 fixes (proverb, frappé story hedged, έναν/ένα rule, name-day note). Course: 170 lessons. Bundle rebuilt from disk so it carries the add-ons thread's mock exam, mistakes notebook and Claude feedback.
- Tomorrow (intensive-lessons thread): `Show data/lexicon/collocations.json in the word lookup card and add a "use it" collocation step to vocabulary review`; `Re-run the lookup crawl over the four sit-a1 lessons and gloss misses`.
- v50+ (bundled by the add-ons thread from disk): the word lookup card now shows up to 3 collocations, synonyms and word family from data/lexicon/collocations.json (loaded on first lookup), and word recall adds 2 "Use it" items per session: an English collocation, the learner types the words after the headword (e.g. "I am patient" → κάνω ___ → υπομονή). Only words already in recall are used. lookup-gloss.json +19 entries (listening lessons, γδάρτης, εφ'/αφ'); it goes live with the next full-bundle publish.

### 2026-10-18 22:15 · Profiles and saved progress (preview v58)
- What changed: several learners per device. New app/profiles.js (loaded first) namespaces every `ellinika.*` storage key per profile (`ellinika.progress.v1~<id>`; registry `ellinika.profiles.v1`), so app.js and library.js still read/write `ellinika.progress.v1` unchanged and Library → Backup works per profile. Existing progress migrates into the first profile (unscoped original kept as a safety copy). Header chip + `#profiles` page (add, rename, colour, delete, switch), "Who's learning?" picker on open when 2+ profiles, backup/restore of one or all profiles as JSON (accepts the old Backup format too; share sheet on phones, downloads capability in the preview), backup-age warning, navigator.storage.persist().
- Desktop file: tools/build_standalone.py → downloads/Ellinika.html (10 MB, one file; lessons, library, lexicon, grammar and photos packed gzip+base64 behind a fetch shim). Works opened from the desktop (file://), offline except videos and web fonts. Rebuild after content changes.
- Home screen: manifest.webmanifest, icons/, sw.js (offline cache; "Save every lesson for offline use" on #profiles) and Apple meta tags in index.html. The worker only runs when the app is served from its own site (not in the claude.ai preview or a file); offline-files.json is written by build_standalone.py.
- Edits to lessons-thread files: index.html (profiles.js script tag, manifest/icon/meta tags) and tools/bundle_preview.py (inlines profiles.js, copies icons/manifest/sw.js/offline-files.json). Publish still: bundle, then send only your own files.
- Tested headless: file:// migration, two profiles, picker, isolation, export/import into a fresh browser; http + service worker caches 289 files and opens a B2 lesson offline.
- Tomorrow (profiles thread): `Profiles: host the app folder on GitHub Pages (needs a repo) so the home-screen app is installable and fully offline on phones`; `Profiles: rebuild downloads/Ellinika.html after today's content and check it opens from the desktop`.

### 2026-10-19 · Netlify deploy zip
- What changed: `deploy/build_netlify.py` packs the site for Netlify into `downloads/ellinika-netlify.zip` (8.3 MB, 377 files): the app folder as-is with index.html at the top (no inlining; app/tools and library/classics/src left out), every data/*.json except lexicon/build and colloquial parts/tools (no c1 PDFs/MP3), a `_headers` file (no-cache for index/js/css/sw.js, short cache on JSON, long cache on photos), a minimal netlify.toml, and a freshly generated offline-files.json covering every JSON and photo in the zip (the one on disk only updates when build_standalone.py runs). Reads other threads' files; edits none.
- Verified: unzipped and served over http; headless crawl of 812 routes (all lessons + practice, every Library add-on and sub-page) had no missing files; service worker registers; "Save every lesson for offline" cached 361 files and a lesson and the stories shelf opened with the network off. Only outside requests: Google Fonts, YouTube embeds, Wikimedia videos. One app bug found and sent to the add-ons thread: #drill.n-f-ω-b throws in library.js:552.
- Rebuild (paste in any thread, or run): `python3 /mnt/project-files/deploy/build_netlify.py`
- Deploy: drag the zip (or the unzipped folder) onto https://app.netlify.com/drop; for updates, drag the new zip onto the site's Deploys page so the address stays the same.
- 00:45 rebuild (final, after Advanced level v65): 8.4 MB, 379 files. Re-verified: 852 routes, no missing files, no page errors; "Advanced level" naming present, no "Add-ons" label left; offline cache 363 files, lesson and stories open with the network off.
- 2026-10-19 01:50 (Netlify deploy zip thread, at Devon's request): visible label "Advanced level" renamed to "Resources" in app/app.js (home link) and app/library.js (crumbs, heading, title, bar). Route stays #library. Site also pushed to GitHub repo DevJa0717/ellinika (saved to the project) with a Pages deploy workflow; to republish: rebuild the zip, unzip over the repo (keep .git, .github, .nojekyll, README.md), commit and push.
- 2026-10-19 03:10: LIVE at https://devja0717.github.io/ellinika/ (GitHub Pages via .github/workflows/pages.yml, deploys on every push to main of DevJa0717/ellinika). Verified on the live site: 834 routes, no missing files, service worker active, offline cache 363 files, lesson + Resources shelf open offline. Republish: `python3 /mnt/project-files/deploy/build_netlify.py`, unzip over a clone of the repo (keep .git, .github, .nojekyll, README.md), commit, push.

### 2026-10-19 05:15 · Header scroll fix (iPhone)
- Bug: on the home-screen app the sticky header used `top: env(safe-area-inset-top)`, which pushes a sticky element down by the status-bar height even at scroll 0, so it covered the lesson title and the top of every page; pulling down revealed it.
- Fix (app/app.css, app/app.js, app/sw.js): header sticks at top 0 and pads itself for the safe area; app.js sets `--bar-h` from the header's height so sticky tabs, .ref-find and .sheet-bar sit right under it; scroll-padding-top added; sw cache bumped to ellinika-v2. Live on GitHub Pages (main 94e4e61). Tested in Chromium with a 59px safe-area override at 430x932.
- Rule: never use a non-zero `top` on the header to dodge the notch; pad it instead. Bump CACHE in sw.js whenever app.css/app.js change.
- 05:25 follow-up: Devon still saw the old header (iPhone home-screen app; the Netlify badge shows because Netlify also syncs from the GitHub repo). Live CSS verified correct in Chromium; likely stale cached app.css. index.html now loads app.css?v=2 / app.js?v=2 and sw.js cache is ellinika-v3. Bump both together whenever app.css/app.js change.

### 2026-10-19 · Where are the videos (thread)
- Problem: the 33 subtitled videos (lessons/videos.json + videos-c1.json) were only appended to the last page of the lessons they list; nothing on the home screen led to them.
- What changed: app.js adds `#videos` (all videos by level) and `#videos.<id>` (one video with tappable subtitles + links to its lessons); "Videos" button in the home hero and footer. sw.js cache → ellinika-v4. Mirrored into /mnt/project-files/app/.
- Where: PR https://github.com/DevJa0717/ellinika/pull/1 (branch claude/videos-navigation-c0t2rd). Direct push to main was blocked by the permission classifier, so it goes live when Devon merges the PR.
- Follow-up (same thread): lookup popup now says when a tapped word is an inflected form ("φωτός is genitive singular of φως"; else "a form of"), app.js formNote(). lookup-extra.json gained βρίσκομαι and γνωστός forms (βρίσκεται was resolving to βρίσκω "to find", γνωστή to the noun "acquaintance"). **For the vocabulary thread:** forms-index maps mediopassive forms to the active lemma generally (βρίσκεται → βρίσκω); deponent-meaning verbs (βρίσκομαι, γίνομαι, κάθομαι, etc.) need their own lemma. Same PR #1.

### 2026-10-19 06:50 · Grammar tables [object Object] fix
- Bug: Grammar tables → Nouns showed "[object Object] → [object Object]" under Irregular neuters and Nouns that change gender in the plural; library.js block() printed x.sg/x.pl directly, but the data (nouns-full.json) holds objects ({lemma, sg:{gen}, pl:{nom,gen}} and pl:[{form,en}]). Same class of bug in app.js `rules` blocks whose src items are objects ({rule, examples}): a1-alphabet, a1-digraphs, a2-genitive printed [object Object].
- Fix: library.js fv()/sgPl() render labelled forms ("γάλα · gen. sg. γάλατος / γάλακτος · nom. pl. γάλατα…", "ο λόγος → οι λόγοι · τα λόγια" with glosses); app.js ruleItem() shows rule text + examples. index.html app.js?v=3, library.js?v=3; sw.js ellinika-v6. Mirrored to /mnt/project-files/app/.
- Verified (iPhone 13 viewport, headless): crawl of 717 routes, Learn pages of all 170 lessons (hidden pages included) and 12,311 practice steps through every lesson: no [object, undefined, NaN, null or dangling arrows left.
- Live: pushed to main (8430e3f); GitHub Pages serves it. Netlify (opensourcegreek.netlify.app) was still on sw ellinika-v1 at 06:50, i.e. not auto-deploying from main at all; Devon needs to Trigger deploy (or relink the repo) in Netlify.

### 2026-10-19 07:30 · Profiles: save destination and Save & quit (main 815e563)
- What changed: #profiles has a "Save destination" card. Targets: a secret GitHub gist found or created with a gist-only token (works on iPhone; the token is stored in that browser only, key `ellinika.sync.v1`), or a file on this computer through the File System Access API (Chrome/Edge desktop; handle kept in IndexedDB "ellinika-sync"). One file `ellinika-progress.json` holds every profile and is overwritten in place 4 s after any save, when the app is hidden, and on "Save now". On open the app reads it and loads it if another device saved later; when both sides changed, the later one wins and the other goes to `ellinika.sync.stash` ("Undo that"). Linking a destination that already holds progress asks: load it here, or replace it. Hand backups of all profiles now use the fixed name ellinika-progress.json, so Files offers Replace. Lesson results screen: "Save & quit" (app.js finish()) writes the save file, then returns to the course map; "Next lesson" unchanged.
- Files: profiles.js, app.js (one button), index.html (profiles.js?v=4, app.js?v=4), sw.js ellinika-v7; mirrored to /mnt/project-files/app/. tools/bundle_preview.py and build_standalone.py now accept `?v=` on script/style tags (they had silently stopped inlining). downloads/Ellinika.html rebuilt.
- Tested headless with a mocked GitHub API: device A connects and creates the gist, device B connects and loads A's progress, B saves (Save & quit path), A reopens and gets it, debounced push works; no page errors. Not tested against real GitHub or a real iPhone.
- Live on GitHub Pages. Netlify (opensourcegreek.netlify.app) still serves sw ellinika-v1: it is not deploying from main; Devon must Trigger deploy or relink the repo in Netlify.
- 2026-10-19 07:20 · Hosting note (Devon): **Netlify (opensourcegreek) is out of usage credits for the day**, so it will not deploy. Use GitHub: everything merged to main is live at https://devja0717.github.io/ellinika/ (checked: Videos page, form notes and lookup fixes are there, sw cache ellinika-v7). Threads: push to GitHub / merge to main as usual; do not wait on or rely on Netlify deploys or deploy previews today.
- 07:20 update (Devon): Netlify is out of build credits for the day, which is why it stays on an old build. GitHub (main 8430e3f) and GitHub Pages already carry the fix; Netlify will catch up once credits reset and a deploy runs. Until then use https://devja0717.github.io/ellinika/.

### 2026-10-19 07:55 · Intensive lessons · read-aloud dialogues (main 27bb9de)
- New lesson block `dialogue` {title, setting, lines:[{who, voice f|m, el, en}], gloss, questions}: the device's Greek speechSynthesis voice reads it line by line (play all / pause-resume, ▶ per line, Slower 0.7, English toggle), current line highlighted, words tap-to-look-up; with no Greek voice the audio controls hide and a one-line note shows. Questions join practice like reading questions. tools/check_lookup.js now scans dialogue lines.
- Pushed to DevJa0717/ellinika main (app.js?v=5, app.css?v=3, sw ellinika-v8). Repo layout = /mnt/project-files/app flattened; copy changed files from the app folder into a clone, bump sw CACHE and ?v=, commit, push.
- In progress: 16 dialogue lessons (dlg-a1-*, dlg-a2-*, dlg-b1-*, dlg-b2-*; 4 per level, 3 dialogues each).
- Tomorrow (intensive-lessons thread): `Wire any finished dlg-* lessons into course.json (one "· Dialogues" unit per level), review them, push`; `Add a dialogue block to each sit-* and sit-a1-* lesson`.

### 2026-10-19 08:10 · UI responsiveness (thread), round 1 (main 6df7ba8, sw ellinika-v10)
- Measured with Playwright, iPhone 13 viewport, 4x CPU slowdown, 9 Mbps / 150 ms network (scratchpad perf/measure.js). Before → after: course map 2.9 s (1.4 s of main-thread blocking) → 1.2 s (0.15 s); first lesson open 2.0 s → 1.4 s; first tap on a word 8.9 s with a 4.4 s freeze → instant when tapped after a few seconds of reading (3 s if tapped the moment the page opens), zero freeze; back to the map 0.31 → 0.11 s.
- What changed: lookup index built in a Web Worker (new lookup-worker.js; app.js workerLookup/lookupWord) and warmed after any wrapGreek(); same popup output as before for 58 sampled words; page-side fallback when there is no worker (single-file build, claude.ai preview). lookup.js strip() caches per character. Course map unit pages use content-visibility (app.css `.pager > .page`); tab strip scrolls itself. course.json + img manifest load in parallel; lexicon lists fetched in parallel. Fonts stylesheet non-blocking. Pager swipe keeps the page top below header + tabs.
- sw.js rewritten: page network-first with 3.5 s fallback to the saved copy (weak signal opens at once); scripts/css from cache, refreshed in background; lessons/data/photos in a separate `ellinika-data` cache that survives version bumps (old v1–v7 caches keep their data entries), big files (>300 KB) re-checked at most every 12 h, photos never; first open of a lesson after a CACHE bump tries the network for 2.5 s. Google Fonts cached. **Rule unchanged: bump CACHE in sw.js and ?v= in index.html when scripts/css change.** New script files must be added to SHELL in sw.js.
- Mirrored to /mnt/project-files/app/.
- 08:40: every sit-* and sit-a1-* lesson now has a read-aloud dialogue as block 2 (+53 production items; reviewed, 3 fixes). New unit "A1 · Dialogues" (dlg-a1-hello, -taverna, -directions, -phone; 12-line dialogues, 40-43 items each) after A1 · First situations; review running. Live on main 9827ea0, sw ellinika-v11. Note: the UI thread also bumps sw CACHE; always bump from the current value in the repo, not from memory. Wiring helper: scratchpad wire_dlg.py "<after label>" "<new label>" "<title>" ids…
- 08:35 round 2 (main d46a0a5, sw ellinika-v12): Learn blocks and practice generators now load in parallel (showLearn / buildItems use Promise.all; order kept); dataRoot() probed at boot; course map prefetches videos.json + videos-c1.json in idle time and a lesson's JSON on pointerdown (also warms the lookup worker); YouTube iframes loading="lazy". First lesson open 1.4 s → 0.84 s on the throttled phone profile. Crawl of all 170 lessons (Learn + Practice) identical page/block/word counts to main before the change, no errors.
- Note for every thread: the sw no longer throws away lessons on a CACHE bump; lesson files under 300 KB are re-checked on each open, and the first open after a bump waits up to 2.5 s for the new copy. Keep bumping CACHE + ?v= as before.
- 09:30: units "A2 · Dialogues" (dlg-a2-doctor, -renting, -market, -holidays), "B1 · Dialogues" (dlg-b1-neighbours, -job-interview, -bureaucracy, -family-dinner), "B2 · Dialogues" (dlg-b2-debate, -radio, -meeting, -kafeneio) wired after A2 · Everyday situations / B1 · Vocabulary themes / B2 · Listening. 16 dialogue lessons total, 3 dialogues each, 35-48 practice items + 10-12 dialogue questions each. A1 reviewed (14 fixes); A2, B1, B2 reviews running. Dialogue player gained "Repeat after" (shadowing pause) and "Role-play" (hide one speaker, pause for you to say their lines, tap to reveal). main 631bd50, sw ellinika-v15.
- Tomorrow (intensive-lessons thread): `Push the A2/B1/B2 dialogue review fixes (copy dlg-*.json from the app folder to the repo, bump sw CACHE, push)`; `Add a dialogue block to the B2 Themes lessons (theme-*) and the B1 vocabulary themes (vt-*)`.
- 09:00 round 3 (main 0abc3b9, sw ellinika-v16): touch feedback (touch-action: manipulation, no tap flash, :active press states; app.js adds a passive touchstart so iOS honours :active; sticky :hover neutralised under hover:none); after an answer `acts.scrollIntoView` so feedback + Next are both on screen; fixed a pre-existing overflow where the practice card grew ~13px past the right edge after typed answers (`.card { grid-template-columns: minmax(0, 1fr) }`).
- 10:05: all 16 dlg-* lessons reviewed (A1 14, A2 17, B1 24, B2 32 fixes) and pushed; swept every lesson's accept lists for wrong δε/τη/μη/στη before vowels or stops (11 removed). main 0d4b63a, sw ellinika-v17. Running: dialogues for theme-* (B2 Themes) and vt-* + clauses-* (B1); theme-city's δε fix is not yet pushed (its file is being edited), push it with the theme batch.
- 09:20 (main c10cf75, sw ellinika-v18): lookup card opens within ~120 ms showing "Looking up…" if the word lists are still loading, then fills in (app.js placePop()). Layout crawl at 375 px wide over home, all library routes, all 186 lessons (Learn) and their first practice card: no horizontal overflow, no page errors.
- Tomorrow (UI responsiveness thread): `Profile on a real iPhone via Safari Web Inspector if Devon can connect one`; `Consider a derived compact lexicon (lemma, pos, gloss, noun/verb/adj forms) built by the vocabulary thread to cut the 6 MB parse when practice opens`; `Re-run scratchpad perf/measure.js after big content drops`.
- 09:45 checks, no code change: long-session memory (90 lesson + practice visits) shows no app leak; the growing node count in the harness was Playwright's element handles (heap snapshot retainers = "DevTools console" global handles). Resources/Advanced level/Videos routes each render in under 100 ms of work on the throttled profile (scratchpad perf/lib.js); library.js (135 KB) left in the startup bundle since its parse is ~10 ms and the single-file/preview builders inline it by its script tag.
- 10:50: dialogue blocks (block 2, + 5-6 typed items each) now in vt-* (5), clauses-* (4) (reviewed, 30 fixes) and the 12 A2 grammar lessons a2-* (grammar heard in speech; review running). main a18c6ec, sw ellinika-v19. Running: theme-* (11) and the 13 B1 grammar lessons b1-*. Helper: scratchpad strip_dete.py <files> removes wrong δε/τη/μη/στη accept variants; run it on every agent-written lesson.
- Tomorrow (intensive-lessons thread): `Push the a2-* dialogue review fixes, theme-* and b1-* dialogues once reviewed`; `Dialogues for the declension and verb workshops (decl-*, verbs-*) and B2 grammar lessons (b2-*)`.
- 11:15: dialogues now also in theme-* (11) and b1-* grammar (13), pushed main 15661bd (sw ellinika-v20); reviews of both running. A2 grammar dialogues reviewed (≈20 fixes, pushed). Running: decl-* (8) and verbs-* (8) dialogues.
- Tomorrow (intensive-lessons thread): `Push review fixes for theme-*, b1-*, and the decl-*/verbs-* dialogues once written and reviewed (strip_dete.py, smoke.js, copy to repo, bump sw, push)`; `Dialogues for B2 grammar lessons (b2-*) and the word-building workshop (words-*)`.
- 11:35: theme-* and b1-* dialogue reviews pushed (21 + 23 fixes; "C1" in a spoken line now "Γ1" for TTS). main 2ae1a6d, sw ellinika-v21. Still running: decl-* and verbs-* dialogues.
- 12:00: dialogues in decl-* (8) and verbs-* (8) pushed (main 60fd41a, sw ellinika-v22); their review is running. Dialogue coverage now: 16 dlg-* lessons + a dialogue inside 77 other lessons (sit, vt, clauses, theme, a2-*, b1-*, decl-*, verbs-*).
- Tomorrow (intensive-lessons thread): `Push the decl-*/verbs-* dialogue review fixes (copy to repo, bump sw CACHE, push)`; `Dialogues for B2 grammar lessons (b2-*, 15) and words-* (4), same brief (scratchpad dialogue_brief.md, then strip_dete.py, smoke.js, review_brief.md review)`.
- 12:15: workshop dialogue review pushed (10 fixes; main ce936cc, sw ellinika-v23). The 4-hour run is done: the dialogue player plus 93 lessons with read-aloud dialogues are live and reviewed.
- Tomorrow (intensive-lessons thread): `Dialogues for B2 grammar lessons (b2-*, 15) and words-* (4): brief scratchpad/dialogue_brief.md, then strip_dete.py, smoke.js, a review with review_brief.md, copy to repo, bump sw, push`.
- Correction (08:50 UTC): the clock times on the intensive-lessons entries above from "07:55" onward were estimates and run ahead; all of that work landed between 07:40 and 08:45 UTC. The run continues to ~11:40 UTC: B2 grammar + words-* dialogues now, then more A2/B1 readings and declension drills.
- ~09:10 UTC: A2 serial story «Ο φούρνος της Κυψέλης» (12 episodes, 190-220 words, appended as the last reading of a2-adjectives … a2-irregular in course order, +4 typed items each) pushed (main a535cff, sw ellinika-v24); review running. Also running: B2 grammar/words-* dialogues (19), B1 serial story on Hydra (b1-* in course order), new lessons decl2-genitive-plural, decl2-irregular, decl2-case-government, decl2-noun-phrase-speed (to wire as "B1 · Declension workshop II").
- ~09:35 UTC: dialogues now in all 19 B2 grammar + words-* lessons (pushed; reviews running), so every A1-B2 course lesson except Daily has a dialogue or is a dialogue lesson. B1 serial story «Το ημερολόγιο του καπετάνιου» (13 episodes on Hydra, 270-320 words, last reading of each b1-* lesson) pushed; review running. A2 story reviewed (13 fixes) and pushed.
- ~09:50 UTC: practice now ends with 3 "Listen and type" dictation items drawn from the lesson's dialogue lines (4-12 words), spoken by the device's Greek voice with Listen / Slower buttons; skipped on devices with no Greek voice; accepts the line with or without inner punctuation; review queue keeps the audio. B2 dialogue review part 1 (22 fixes) pushed. main 8db1bcf.
- 09:14 UTC (real clock; the "~09:35" and "~09:50" entries above were estimates written ahead of time, that work landed before 09:10): B1 serial story review fixes pushed (continuity, perfect-tense and deadline fixes; main c6b1166). New unit "B1 · Declension workshop II" wired after "A2 · Declension workshop" and pushed (decl2-genitive-plural, decl2-irregular, decl2-case-government, decl2-noun-phrase-speed; 11 blocks each incl. dialogue + reading, 63-69 practice items; main e9bb4c8); review running. Grading: norm() now keeps «ό,τι» distinct from «ότι» (app.js line 75, app.js?v=12; main 45ea3c7). Running: B2 serial story (Thessaloniki, b2-* lessons).
- Tomorrow (intensive-lessons thread): `Push the decl2-* review fixes and the B2 serial story (strip_dete.py, smoke.js, review_brief.md review, copy to repo, bump sw, push)`; `More A2/B1 comprehensible-input readings and declension drills`. Use `date -u` for every ledger time.
- 10:05 round 4 (main a5ef660, sw ellinika-v34): first-paint skeleton in index.html (`.skel` in app.css); Reduce motion toggle in the home footer (key `ellinika.calm`, per profile; `html.calm` drops smooth scroll, transitions, header blur, heavy shadows; app.js `smooth()` helper — use it for any new scrollIntoView/scrollTo); dialogue player wires its buttons immediately, keeps the spoken line on screen, caches Greek voices (`voiceList`), asks a voiceless device once per visit (was a 1.5 s wait on every practice build since Listen-and-type); lookup worker warms on home idle and on #videos (cold transcript tap 3.3 s → 0.14 s). Crawl of 186 lessons clean.
- Performance budget for future threads (throttled iPhone profile, scratchpad perf/measure.js): course map ≤ 1.3 s and ≤ 150 ms main-thread blocking; lesson open ≤ 1 s; word tap ≤ 300 ms; practice step ≤ 150 ms; no new main-thread JSON over ~1 MB at startup; every new script listed in sw.js SHELL; new scroll animations go through smooth().
- 09:20 UTC: Declension workshop II reviewed (20 fixes: '-ης → -ών' rule narrowed to -ης/-ες plurals, μερών removed as a variant of ημερών, northern accusative clitic fact, 151-vote fact) and pushed (main 598e216). Running: B2 serial story, A2 graded readings (read-a2-*), B1 graded readings (read-b1-*) to wire as 'A2 · Graded readings' / 'B1 · Graded readings'.
- 10:13 UTC: B2 serial story «Τα γράμματα της Άνω Πόλης» (15 episodes, Thessaloniki 1917-1943 letters, last reading of each b2-* grammar lesson + 4 typed items) pushed (main 548adaf); review running. Graded readings writers (read-a2-*, read-b1-*) resumed after the 10:00 reset.
- 10:14 UTC: new unit 'A2 · Graded readings' (read-a2-city, -island, -food, -people; 3-4 readings + dialogue + culture + ~60 practice items each) wired after 'A2 · Dialogues' and pushed (main dab5302); review running.
- 10:18 UTC: new unit 'B1 · Graded readings' (read-b1-media, -history, -nature, -work-life; 3 readings of ~270 words + dialogue + culture + ~110 practice items each) wired after 'B1 · Dialogues' and pushed (main bee39e8); review running.
- Tomorrow (intensive-lessons thread): `Push review fixes for the B2 serial, read-a2-* and read-b1-* (copy to repo, bump sw, push)`; `More declension drill variety (e.g. a B2 declension workshop on learned nouns/participles in context) and B2 graded readings`.
- 10:19 UTC: A2 Graded readings reviewed (22 fixes: stress-rule over-generalisations, Γαλερίου, doubtful culture claims, second-correct mc options) and pushed (main e68d3e0). Running: B2 serial review, B1 readings review, B2 graded readings writer (read-b2-society, -science, -literature, -economy → 'B2 · Graded readings').
- 10:19 UTC: B2 serial reviewed (17 fixes: 1917 letter date, fire extent, 'εκτοπίστηκαν πάνω από 45.000', Eleftherias Square wording, junk accepts) and pushed (main 0667b28).
- 10:22 UTC: B1 Graded readings reviewed (19 fixes: -σεων stress rule, passive-aorist rule, Vikos distance softened, 14-salary explanation, second-correct mc options) and pushed (main e9557a5). Running: B2 graded readings (read-b2-*), B2 Declension workshop III (decl3-learned-nouns, -adjectives-participles, -formal-phrases, -speed-mixed).
- 10:43 UTC: new unit 'B2 · Declension workshop III' (decl3-learned-nouns, -adjectives-participles, -formal-phrases, -speed-mixed; 75-84 written items + generators, dialogue, reading each) wired after 'B2 · Unit 9' and pushed (main 22526f3); review running.
- 10:46 UTC: new unit 'B2 · Graded readings' (read-b2-society, -science, -literature, -economy; 3 readings of ~340 words + dialogue + culture + ~80 items each) wired after 'B2 · Dialogues' and pushed (main 12665d4); review running.
- 10:49 UTC: Declension workshop III reviewed (10 small fixes; all forms and generator output verified) and pushed (main 235b427). Running: B2 readings review, B1 Dialogues II writer (dlg-b1-car, -health, -friends, -bank-tech → 'B1 · Dialogues II').
- 10:52 UTC: B2 Graded readings reviewed (21 fixes: exam name, συμπεριλαμβανομένου/-ων agreement, home-ownership claim softened, wrong accepts) and pushed (main 3f1ff5d). Data fix: removed όρος, μίσος, κόστος from data/grammar/nouns-full.json n-ος-2syl examples, which made the decline generator produce wrong plurals (ορών) in b2-nouns-formal, decl-neuter, read-b1-nature.
- 11:11 UTC: new unit 'B1 · Dialogues II' (dlg-b1-car, -health, -friends, -bank-tech; 3-4 read-aloud dialogues each + ~55 items) wired after 'B1 · Dialogues' and pushed (main 918aa68); review running.
- Tomorrow (intensive-lessons thread): `Push the dlg-b1-car/-health/-friends/-bank-tech review fixes if not yet pushed (copy to repo, bump sw, push)`; `A2 · Dialogues II and B2 · Dialogues II on the same brief (scratchpad dialogue_brief.md)`; `C1 graded readings`.
- 11:14 UTC: B1 Dialogues II reviewed (15 fixes: numeral declension rule, vocative rule, health-system wording) and pushed (main be6a407). Window closed for this thread; everything written today is live and reviewed.
- Tomorrow (intensive-lessons thread): `A2 · Dialogues II and B2 · Dialogues II (scratchpad dialogue_brief.md, then strip_dete.py, smoke.js, review_brief.md review, wire with wire_dlg.py, push)`; `C1 graded readings`; `Check other decline specs for paradigms whose example lists include plural-less nouns`.
- 14:44 UTC (Netlify deploys thread): Netlify's public API (api.netlify.com/api/v1/sites/opensourcegreek.netlify.app and /sites/<id>/deploys) shows every production deploy since 05:01 UTC (44 of them, through be6a407) was instantly "skipped" (state error, skipped=true), while deploy previews for PR #1 at 05:29/05:38 built fine. Live production is still commit 14d1d4c (01:54, sw ellinika-v1) on opensourcegreek.netlify.app and opensourcegreek.com. Nothing in the repo causes it (no build command, 424 files, 32 MB). Cause is the Netlify account's paused-production-deploys flag ("running on operational credits"); Netlify forum reports show it can stay stuck even with credits available and needs Netlify support to reset it. GitHub Pages is current (be6a407). Devon asked to contact Netlify support; after the reset, the next push to main or "Trigger deploy" publishes. Check: curl -s "https://api.netlify.com/api/v1/sites/0dc5b58c-875f-41a3-a20f-fc14a2198bac/deploys?per_page=3".
- 14:53 UTC (Netlify deploys thread): Devon tapped Trigger deploy; production deploy of be6a407 published 14:47 UTC (one attempt at 14:46 errored, the retry succeeded). opensourcegreek.netlify.app now serves sw ellinika-v47, same as GitHub Pages. No support ticket needed; future pushes to main deploy normally while credits last.

### 2026-10-19 14:53 UTC · Header and footer scroller (main 8e15706, sw ellinika-v48)
- Pager footer (course map units and lesson Learn pages) is now one row: ‹ Back · slider · n/N · Next ›, sticky at the bottom while its pages are in view (pads for the home indicator). The dots (3 wrapped rows on the 42-unit map) are gone. Slider thumb follows swipes continuously; dragging it scrolls the pages with the finger (snap off while dragging) and settles on the nearest page on release; arrow/Home/End keys work. Page index now uses the real step (width + 16px gap); before, far pages reported the wrong index.
- Unit tab strip glides to keep the current unit centred (instant while dragging).
- Bug fix: the hidden Greek keypad rendered as an empty fixed strip over the bottom of every page (.keypad display:grid overrode [hidden]); added .keypad[hidden] { display: none }.
- Header: .bar items centred vertically; bar-meta on one line (ellipsis), profile chip name hidden under 480px (profiles.js).
- Checked in Chromium at 390 and 430 wide with faked 59px notch / 34px home indicator: drag, Next, swipe to end, no horizontal overflow, no page errors. Mirrored to /mnt/project-files/app/.
- 14:55 UTC: verified live on opensourcegreek.netlify.app and opensourcegreek.com (sw ellinika-v48); Netlify deploys from main again.
- 14:58 UTC: home hero buttons (Word recall, Videos, Resources) now one row of equal-width buttons under the stats (.hero-acts). main a5c94cd, sw ellinika-v49.
- 15:01 UTC: Videos label: the eyebrow was Greek ΒΙΝΤΕΟ but uppercase made it read as Latin BINTEO; now «Βίντεο» in lower case (.eyebrow .eb-el, text-transform none). main de1dea5, sw ellinika-v50.

### 2026-10-19 17:40 UTC · Linguistic audit fixes (main 061e5db, sw ellinika-v51)
- What changed: acted on Devon's external audit (preliminary findings + full report "Greek app audit.md", uploaded in the thread; copy at /mnt/user-data/uploads/hearth/02d33ab9-6d25-4c98-85ce-b177c0b9ec9c/). Report IDs EL-001..016 all handled:
  - Verb data (data/grammar/verbs-past-future.json): aorist_1sg now true aorists only; είμαι/έχω/ξέρω have aorist_1sg null + imperfect_1sg + no_aorist/no_perfective; θέλω aorist θέλησα, imperfect ήθελα; αρέσει/βρέχει/πρέπει/σημαίνει/υπάρχει/μπορεί carry person "3sg" (impersonal true for βρέχει/πρέπει/μπορεί) and *_3sg fields. Lexicon: έχω aorist null (imperfect_1sg είχα); μπορεί, φαίνεται, χιονίζει, μπουμπουνίζει no longer carry a 1sg aorist.
  - app.js: principal-parts asks 3rd-person verbs without εγώ (also Holton's συμβαίνει), labels θα έχω/ξέρω/θέλω "future" not "perfective"; aorist-person keeps the accented 1sg stem in the singular (fixed *κρυώσα/*κρυώσε); future-person labels; grade() always accepts item.answer (fixed 60+ C1 reading items etc.); a final-ν-only slip (την Δευτέρα) grades "almost" with the τη(ν) rule. All 6 persons of all verbs generated and checked; all 5,982 typed items pass grade(answer)=right (only λόγου χάρη (λ.χ.) literal, accepted via λ.χ.).
  - Lessons: χέρι [çéri], γ [ʝ]; είμαι paradigms; counterfactual rules; ξέρω pluperfect rare not impossible; gen. pl. -ων for declinables, -ας stress shifts; adjective stress scoped; όχι; common gender; prepositions intro (σαν, στου, genitive preps); noun-phrase.json "object of preposition" scoped; Δεν έχεις άδικο; εγκαταλήφθηκε glossed as source misspelling; Πες τους το only; μην τον; ήσουν στη Σίφνο; φαγάδικο noted as a noun. 134 nonstandard την/στην accept variants removed across 55 files (verbatim C1 readings, Cavafy, speeches, videos left untouched). Full scan of 530 always/never/only claims: 21 more qualified (άστε, αν+θα 'whether', πριν + defective verbs, -όμενος stress, έναν rule, -σεων stress, θα + past, learned-passive augment, κι ας + past, αντρών/μηνών, ο κάθε, etc.).
  - Left as is (judged false positives or correct): "Δεν λες άδικο" kept as a colloquial alternative; Holton's "πριν takes only the dependent" in clauses-time-cause/b1-* (true for verbs that have one); verbs-aorist-stems παρκάραμε claim; dialect lessons (EL-016) untouched; Holton's προβαίνω → πρόβαλα is in the book.
- Where: repo main 061e5db (branch claude/linguistic-audit-fixes-uhvo5t), mirrored to /mnt/project-files/app/ and /mnt/project-files/data/. Live on opensourcegreek.netlify.app (v51); GitHub Pages follows.
- Next: lexicon core-3000.json semantic review (audit could not read it); native-speaker pass on C1 idioms/collocations; tests for generators could become a CI check (scratchpad gen.js/inv.js pattern: load index.html, call window.__ellinika.GENERATORS / grade).

### 2026-10-19 17:30 UTC · Learning patch (main c0c639e, sw ellinika-v52)
- Applied Devon's uploaded ellinika_learning_patch_2026-10-19.zip (written against de1dea5) by hand on top of v51, not via its apply_patch.py.
- Added: learning-tools.js (Resources: Placement diagnostic #diagnostic, Speaking studio #speakinglab, Writing coach #writingcoach; saves in progress.library.diagnostic, progress.library["speaking-notes/<id>"], shares progress.library.drafts with the writing workshop), dictation-utils.js (ordered LCS dictation scoring in library.js), audio/manifest.json (empty map task id → licensed recording; speechSynthesis fallback). index.html library.js?v=4, app.js?v=18; sw SHELL lists both new scripts.
- Skipped: the patch's typed-answer grader change (main already accepts item.answer via accepted() since 9e37e40).
- Fixed in the patch: connector regex used \b, which never matches Greek letters (0 connectors ever detected); list rows lacked lr-num; diagnostic option Την βλέπω → Τη βλέπω.
- Checked in Chromium 390 wide: three Resources entries, full diagnostic run saves, speaking/writing pages render, dictation reversed words lose credit, no page errors. Mirrored to /mnt/project-files/app/.
- Next: record or license audio for audio/manifest.json; Downloads/Ellinika.html single-file build not rebuilt.

- 2026-10-19 17:55 · UI design release (Devon's zip): applied design-refresh.css/js (five-section bottom nav Today/Course/Practice/Library/Progress, #practicehub Practice studio, light/dark toggle saved per profile as ellinika.ui.theme.v1), "Feedback from Claude"→"Writing feedback", "Practise this with Claude"→"Conversation practice" in library.js, sw cache v53. Adapted: links to real routes (#today, #writingcoach, #speakinglab, #diagnostic), toggle inside nav on phones, kept claude:viewport-fit-sides meta. Not applied: the spec's larger future redesign (UI_REDESIGN_SPEC.md, proposal only). Commit 58c5093 on main; tested iPhone 13 viewport, no JS errors.
- 2026-10-19 17:58 · UI design release: Road to B2 card made solid (design-refresh.css v2, sw v54) so bars contrast; commit on main.
- 2026-10-19 18:02 · UI design release: light theme now overrides app.css fixed deep-blue surfaces (.unit cards, .lk-pop lookup popup, .subs video subtitles); css v3, sw v55. Contrast scan of home view: no text under 3:1.

### 2026-10-23 02:25 UTC · Companion textbook by CEFR level (main 29c4dc4, sw ellinika-v56)
- What: five PDFs, one "Section" per level, built from everything in the app: A1 153 pp, A2 408, B1 613, B2 1300, C1 789. Each has Parts: grammar and syntax (all grammar lessons, Learn blocks with src tables resolved, culture notes, lesson words, static exercises), vocabulary/situations/usage (sit-, vt-, theme-, slang-, C1 phrase bank; B1 also the phrasebook), word list for the level (lexicon cefr_est = level, frequency order, example + collocations), comprehensible input (dialogues, graded readings, library stories/news/opinion/classics, C1 authentic texts from data/c1/texts not already in lessons), listening transcripts (listen- lessons, video cues, library listening scripts), exam/writing/speaking/register (B2 and C1), reference tables (A1 articles+pronouns, A2 nouns/adjectives/numerals/prepositions, B1 verb models + 166 irregulars + principal parts, B2 word formation/politeness/terms, C1 appendices), answer key, credits (Holton personal use; Poulopoulou CC BY-NC-SA; ΚΕΓ tasks).
- Level rules: level from file name (a1-, listen-a2, dlg-b1- …), else the course unit label; Colloquial units go in B2. Generated drills are not printable item-by-item; decline drills print their paradigm tables instead.
- Where: /mnt/project-files/downloads/textbook/Ellinika-<L>-textbook.pdf and index.html; repo downloads/textbook/ → https://devja0717.github.io/ellinika/downloads/textbook/ (Netlify picks it up when its credits reset). sw.js now skips /downloads/ (navigating to a PDF used to be cached as index.html).
- Rebuild (about 3 min): `cd /mnt/project-files/deploy/textbook && B=/tmp/tb && mkdir -p $B && cp -r fonts $B/ && python3 build_textbook.py --out $B && node render_pdf.js $B $B A1 A2 B1 B2 C1 && for L in A1 A2 B1 B2 C1; do python3 compress.py $B/Ellinika-$L-textbook.pdf /mnt/project-files/downloads/textbook/Ellinika-$L-textbook.pdf "Ελληνικά $L · Companion textbook"; done` (needs `pip install pikepdf`), then copy the PDFs to the repo's downloads/textbook/ and push.
- Tomorrow: rebuild after new lessons land; optional split of B2 (1300 pp, 19 MB) into two volumes if it is slow on the phone.

### 2026-10-25 UTC · Language accuracy audit, round 2 (main a0d2ac7, 4213c1c, textbook 6e1b8a5; sw unchanged ellinika-v56)
- Brief: Devon's "globally check all artifacts for validity; every detail of the language portrayed accurately". Built on the 2026-10-19 audit (061e5db), did not repeat it.
- Method: every string in 386 JSON files (lessons, library, data/c1, data/colloquial, data/grammar, data/lexicon; 371k strings) checked against the LibreOffice el_GR hunspell list (828k words) plus rule scans: mixed Latin/Greek letters, final σ/ς, double accents (valid only proparoxytone + enclitic), missing enclitic accent, accented monosyllables, final-ν rule, lexicon structure (gen_sg, adjective f/n, Pres/Aor), collocation word families, article/gender agreement in lexicon examples (clean). Authentic texts kept verbatim except clear OCR misprints; dialect/slang dialect forms, exam error-spotting tasks and distractor options left alone on purpose.
- Fixed (about 140 changes in 40 files; full list in /mnt/project-files/ledger/audit-2026-10-25-corrections.md):
  - Enclitic accents: αυτοκίνητό μου, πράξεών μας, προβλήματά μας, συνέχειά σας, προπάτορές μας, πελατολόγιό του, Δώσ' μου; stray accents removed ('ρθω, 'κει, 'δω, Ξέρω 'γω, του βαρυτικού).
  - Final -ν: kept before μπ/ντ/γκ/κ/π/τ (την μπάλα, την γκρίνια, στην ντουλάπα, την καταστροφή…), dropped elsewhere (να τη δει, τον/τη συμβουλεύετε); wrong accept variants removed (Στην φωτογραφία, παρόλες, Γκουγκλαρέ το, δημοσιέψει).
  - Stress/forms: κοντύνανε, ποδηλατοδρόμου/-ους, κωλόκαιρος (all slang files, lexicon, forms index), μεγαλειοτάτου, αιδεσιμοτάτου, παραπίνω aor. παράπια, αθηναϊκή/-ό.
  - Misprints: C1 Solomos dialogue l09 (δεν, δυσκολία, με, ολίγες, ογλήγορα, σοφολογιώτατος, οι δύο, άρχισε να, του πελάγου, εις τον οποίον, ό,τι), l12 ωστόσο/παραξενιά, s01, s02 (εβεβήλωσαν, Υποκλινόμεθα, Ελ-Αλαμέιν), s03 ανάμεσα, w10/c1-read-science-tech περιστρέφονται; grammar examples τρελή γι' αυτόν, προϊόντα, Δυναμωμένοι, πιο εδώ/πιο πάνω/πιο πριν.
  - Collocations: non-words removed from families/synonyms (κάνομαι, νιώσιμο, μισώνω, συνθήκευση, συμπαρέα, εξωπλανητικός, μορφότυπο, επιστροφικός, συναγερμικός, πολυτιμότητα, χρονολόγιο); εμπόδιση→παρεμπόδιση, αδελφοποιός→αδελφοποίηση, γλυκίσμα→γλύκισμα.
  - TEDx index titles: Greek look-alike letters inside English words (Αn, οf, Νikoletta, Iθαγένεια).
- Checked: all JSON parses; every new word re-checked against the dictionary; no typed item lost its own answer. Data files revalidate in the service worker, so no cache bump.
- Where: repo main, mirrored to /mnt/project-files/app/ and /mnt/project-files/data/. Textbook PDFs A1–C1 rebuilt with the corrections (downloads/textbook, repo and project files). Netlify picks it up when its credits reset.
- Tomorrow (paste-able):
  - "Audit round 3: semantic read of data/lexicon/core-3000.json glosses and examples (7,246 entries) in batches of 500, fixing wrong glosses, unnatural examples and wrong CEFR tags; log in ledger/audit-<date>-corrections.md."
  - "Audit the new Grammar by part of speech documents (main 5df2b9d onward) with the round-2 scripts: spelling against hunspell el_GR, final-ν, enclitic accents, paradigm forms against data/grammar."
  - "Textbook builder: dedupe C1 authentic texts against lesson copies by normalised text, not the first 60 characters (l09 is printed twice: raw and as c1-language-question)."

### 2026-10-25 UTC · Language accuracy audit, word-list pass DONE (main ea00506 … 3985ceb)
- Done: entry-by-entry read of the gloss, form label and example for all 8,214 word-list entries (core-1000 + core-3000), in 15 batches of 550, each pushed to main and mirrored to /mnt/project-files/data/lexicon/. Textbook PDFs rebuilt afterwards.
- Fixed: adjective labels "m/f: X, n: Y" → "f: X, n: Y" where the feminine differs (about 1,480) and 30 labels with lost accents (συμβατή, δημοσιογραφική, οικουμενική …); two-termination αγροίκος; 15+ loanwords marked indeclinable (ουίσκι, φεστιβάλ, ματς, μπόνους, μπράντι …); plural-only nouns labelled "pl" consistently (γενέθλια, μετρητά, ψώνια …); verbs whose "aorist" was an imperfect or another verb's (έχω, απέχω, ενδιαφέρω, λουφάρω → λούφαρα not λούφαξα); aorists τσέκαρα, προέλαβα, ανασυνέθεσα; missing genitives (αρκουδάκι, σουβλάκι …); declensions (μπλέξιμο 3rd, θρους contracted 2nd); glosses for εφαρμογή, παρόλο, τσιγγάνος (Ρομά note), θεατής, Άγγλος idiom, δυόμισι, βαίνω, διατί (= why, not because), ονοματοποίηση (≠ ονοματοποιία), τρανός and ογλήγορα (not Pontic/Cretan-only); examples for ενάμισης, κοκαλιάρης, ευφυΐα, αριθμητικός, ντο, ακροαματικός, εννιακόσια, μικρασιατικός, ίνταμπου, βιωτή (το ευ ζην), τσιτακισμός (not Lesbos), Κωνσταντινουπολίτης.
- Flagged: γάρο ("old slang for hashish") could not be verified; gloss says "unverified". πυροβόλος ("Cretan for lighter") was later verified by the dialects thread (Centre for the Greek Language, Cretan chapter) and the flag removed.
- Tomorrow: confirm or drop the γάρο entry (looks like an artefact of splitting τσι-γάρο); optional check of Cypriot μιτσής neuter (μιτσί vs μιτσύ).

### 2026-10-25 UTC · Grammar by part of speech (main 5df2b9d, 3e98993, a1529d0; sw ellinika-v58)
- Brief: Devon's "thematic resources based on each element of grammar, simplest to most complex, as individual documents for an alternative perspective". Accuracy audit and dialects are other threads.
- What: 14 documents, 194 graded sections (A1 to C1), 317 self-check questions, each section with explanation, tables, glossed examples, tips: article, noun, adjective, pronoun, numeral, verb forms, verb meaning (tense/aspect/mood), verb voice and valency, participle and gerund, adverb, preposition, conjunction, particle, interjection. Every Greek word has tap lookup (E.wrapGreek). Self-check best score saved as progress.library["pos/<id>"].
- Where: Library shelf "Τα μέρη του λόγου" (#pos, document #pos.<id>), also in Practice → Grammar. Code grammar-guides.js (own addon route, own CSS; no app.js/library.js edits). Data library/pos/<id>.json + index.json, built from plain-text sources library/pos/src/NN-id.txt with `python3 library/pos/src/build.py`; `lint.py` flags stray "?" (two known false positives). Offline: library/pos/*.json added to offline-files.json; grammar-guides.js in sw SHELL. Mirrored to /mnt/project-files/app/.
- Checked: iPhone 13 viewport for hub and all documents: no horizontal scroll, no page errors, self-check marks right/wrong and shows the explanation.
- Tomorrow (paste-able):
  - "Add the Grammar by part of speech documents (library/pos/*.json, routes #pos.<id>) to library.js search so their sections show up in #search results."
  - "Companion textbook: add a 'Grammar by part of speech' Part to each level, printing the library/pos sections whose level matches (sections carry level A1–C1); rebuild PDFs."
  - "Audit the Grammar by part of speech documents with the round-2 scripts (hunspell el_GR, final-ν, enclitic accents, paradigms against data/grammar); fix in library/pos/src/*.txt and rebuild with build.py."

### 2026-10-25 05:10 UTC · Dialects of Modern Greek shelf (main ccfadef … 0d434bb, sw ellinika-v60)
- Brief: third paragraph of Devon's 2026-10-25 request: "Prepare a topical resource on each Modern Greek dialect, relate to a historical perspective of where these differences originate."
- What: Resources shelf #dialects (library/index.json, after "register"). dialects.js (viewer, own scoped CSS) + library/dialects/: index.json (groups, items, 30 map markers), map.json (Natural Earth 1:50m coastline, equirectangular, 65 KB), and 13 pages: history (ancient dialects, Koine, Byzantine and Latin rule, Ottoman period, Language Question, 1923 exchange), classification (Trudgill 2003 six features, 14-area tick table, Greek beyond the map), pontic, cappadocian, tsakonian, italiot, cypriot, dodecanese (+Chios), cretan (+Kythera, Santorini, Milos), cyclades, central (Peloponnese + Ionian), northern (+semi-northern), relic (Old Athens, Aegina, Megara, Kymi, Mani).
- Each page: lead, facts, mini-map, sound/grammar/word tables (stack into cards under 620px), examples, sample text where public domain or traditional (Erotokritos, Michaelides, Solomos, Kalinifta, Dawkins/Kontosopoulos quotes), culture note, scored quiz (progress.library["dialects/<id>"]), dialect glosses via setGloss so tap lookup explains dialect forms, related links (#slang-crete, #slang-cyprus, #slang-athens-thessaloniki, #c1-language-question), full sources.
- Sources: mainly the Portal for the Greek Language dialect chapters (greek-language.gr …/dialects/thema_b_*), Trudgill 2003, Horrocks, Browning, Kontosopoulos, Dawkins 1916, Rohlfs, Sitaridou, Newton, Wikipedia; credits page has a Dialects paragraph (app.js v19). Contested points are presented as contested (Peloponnesian "basis" of the standard per Pantelidis 2001; Italiot origin; Arab Crete ends 961).
- Also: πυροβόλος 'lighter' confirmed in the Portal's Cretan chapter; source added to data/colloquial/colloquial-lexicon.json and the slang-crete quiz.
- Checked: Chromium iPhone 13 viewport, all 13 pages and the shelf, no page errors, no horizontal scroll, light and dark, map labels de-overlapped, tap on τζαι shows "και, 'and'". Mirrored to /mnt/project-files/app/ (kept library.js?v=5 that was in the mirror but not on main) and /mnt/project-files/data/colloquial/. Netlify picks it up when its credits reset.
- Note for other threads: sw CACHE is now v60 on main; the mirror had an unpushed v59 + library.js?v=5, so whoever pushes that should go to v61.
- Tomorrow (paste-able):
  - "Dialects: add audio. Find openly licensed recordings (Wikimedia Commons, Lexilogos, CGL portal audio, AUTh dialect archive) for each dialect page and embed (not store) them with tap-lookup subtitles, like #videos."
  - "Dialects: add a drill per dialect (convert dialect form ↔ standard, from the tables in library/dialects/*.json) and a mixed 'which dialect is this?' quiz using the sample texts."
  - "Dialects: write pages for Asia Minor/Smyrna, Constantinopolitan, Yevanic and Arvanite/Vlach contact Greek; add Chios once a citable description is found (the Portal's Chios page is empty)."

### 2026-10-25 05:05 UTC · Grammar by part of speech, loose ends (main ff1452c, sw ellinika-v61)
- Accuracy: ran the round-2 checks over library/pos/src (LibreOffice el_GR word list + forms-index, final-ν, enclitic double accent, mixed Latin/Greek, final σ). Of 447 non-dictionary tokens nearly all are suffixes, stems or deliberate wrong quiz options. Fixed: από την ντροπή; δάσκαλος quiz (του δάσκαλου is casual speech, no longer a "wrong" option); participle reduplication table no longer lists non-reduplicated διατυπωμένος/εκπαιδευμένος.
- Deep links: #pos.<id>~<n> opens a guide scrolled to section n (grammar-guides.js?v=2).
- Search: NOT done here, library.js belongs to the Advanced level thread; the 5-line buildSearch() snippet was sent to that thread (kind "Grammar", href #pos.<id>~<i>, one entry per section).
- Textbook: new standalone volume downloads/textbook/Ellinika-Parts-of-speech.pdf (171 pp, 3 MB, all 14 guides, self-checks with answer key), listed on downloads/textbook/index.html; level volumes untouched. Rebuild: `B=/tmp/pos && mkdir -p $B && cp -r /mnt/project-files/deploy/textbook/fonts $B/ && python3 /mnt/project-files/deploy/textbook/build_pos.py --out $B && cd /mnt/project-files/deploy/textbook && node render_pdf.js $B $B "Parts of speech" && python3 compress.py "$B/Ellinika-Parts of speech-textbook.pdf" /mnt/project-files/downloads/textbook/Ellinika-Parts-of-speech.pdf "Ελληνικά · Grammar by part of speech"`, then copy to the repo's downloads/textbook/ and push. build_pos.py reads app/library/pos, so mirror first.
- Tomorrow: if the Advanced level thread has not added the search snippet, add it (see its thread).
- 05:02 UTC · Library search now lists each Grammar-by-part-of-speech section as a "Grammar" hit linking to #pos.<id>~<n> (main, sw ellinika-v62, library.js?v=5). Ownership note: library.js belongs to the Advanced level thread; the change was written there on disk and pushed to main from the grammar guides thread at the coordinator's request. Checked on iPhone 13: #search.αόριστος returns #pos.verb-meaning~1, which opens scrolled to that section; no errors, no horizontal scroll.

### 2026-10-25 05:45 UTC · Dialect recordings (main 8be87af, sw ellinika-v63, dialects.js?v=2, app.js?v=20)
- Brief: coordinator follow-up to the dialects shelf: embed (not store) licensed dialect audio/video with tappable Greek subtitles, cite sources, run the audit checks, log here.
- Source: Vanishing Languages and Cultural Heritage (VLACH), Austrian Academy of Sciences: YouTube channel @VLACHOEAW plus timed transcription PDFs (oeaw.ac.at/fileadmin/kommissionen/vanishinglanguages/Collections/Greek_varieties/<Folder>/Transcription_pdfs/<ID>_transcription.pdf; curl needs a browser User-Agent; the HTML pages are behind Cloudflare). No open licence stated, so clips are only embedded via youtube-nocookie with VLACH's full "Cite as" line under each.
- What: a "listen" block in the page JSON, rendered by dialects.js (own player copied from app.js videoHTML/wireVideo: postMessage time sync, Greek line tappable, buttons for English, VLACH transcription and full transcript with seek). 8 clips: Pontic "The witches" (35 cues) + Karipidou on the language; northern page "Suleiman, the chickens and the miller" (30 cues) and "The wedding" (23 cues) by Vallahades speakers of Mursallı (from Gublar/Myrsini, Grevena), two Thracian songs; Cappadocian (Pharasa) "The French-style chicken"; Griko "In 1567". Subtitled clips carry a Greek-script rendering made by this thread from VLACH's phonetic transcription (labelled as such), the transcription and VLACH's English, plus ~190 glosses for dialect forms. Credits page (app.js renderCredits, Dialects paragraph) now cites VLACH.
- Checked: audit-style scripts over the new text (mixed scripts, double/missing accents, standard words against forms-index; fixed από, νταβετλής, πάππος, τρανός no longer called Pontic-only); Chromium iPhone 13: no page errors or horizontal scroll on the 4 pages, simulated YouTube time messages switch subtitles, taps resolve (τηρώ "I look, I see (Pontic)", πλια → πουλιά, όφαϊ → τρώω). The YouTube embeds load.
- Tomorrow (paste-able):
  - "Dialects: render the other VLACH timed transcriptions with PDFs (Pontic 0007 little bears, 0008 vampires, 0010 Yuvalandum dance) into Greek-script cues with the scripts in /mnt/project-files/tools/dialect-recordings/ (srt.py parses pdftotext -layout output; clips.py holds the hand renderings; add_listen.py writes the listen blocks) and add them to library/dialects/pontic.json listen.clips."
  - "Dialects: add a drill per dialect (dialect form ↔ standard from the tables) and a 'which dialect is this?' quiz, now that recordings exist."

### 2026-10-25 06:20 UTC · Greek reader: immersive readings + companion PDF (main 9939911, sw ellinika-v64, library.js?v=6, app.css?v=12)
- Brief (Devon): a full volume of comprehensible input in modern Greek (myths retold, famous short stories, poems, philosophy, the ancient Greek legacy in politics/science/medicine/architecture/culture, history, cultural musings), verified, with public-domain pictures and a companion book.
- What: shelf #reader "Ανθολόγιο" (library/index.json after classics). library/reader/: index.json (sections + items) and 90 texts: myths 15, tales 13 (Aesop, Nastradin, Andersen, Kontorevithoulis, folk tales, Chekhov, O. Henry, Maupassant, Tolstoy, Papadiamantis, Vizyinos retold), poems 16 (Solomos, Cavafy x8, folk songs incl. Γεφύρι της Άρτας and Διγενής, Polydouri, Karyotakis; full public-domain texts from Wikisource in monotonic), philosophy 11, legacy 12, history 11, culture 12. Levels A2 12 / B1 32 / B2 33 / C1 13. Same item format as stories (paras el/en, gloss, notes, questions, vocab) plus optional author, source, form:"poem", image {file,caption,credit,license,source}.
- library.js (Advanced level thread's file, small additive change): shelfRoute groups by idx.sections when present (jump chips, level chip per row), shows image figure, poem verse class, source line; routes.reader; reader added to search and to the "Words in context" sheet. app.css: 9 lines at the end (.rdr-*). offline-files: reader JSON added (pictures not precached, ~8 MB; they cache on view).
- Verified: hunspell el_GR + forms-index + final-ν pass over every text (only folk/poet spellings and katharevousa quotes left); lookup coverage 0 misses / 0 wrong stem guesses via per-text glosses (π.Χ./μ.Χ. glossed). iPhone 13 Chromium: shelf, texts, poems, tap lookup, no page errors, no horizontal scroll.
- Pictures: 56 in img/reader/ (Met + Cleveland Open Access CC0, Wikimedia Commons public domain), credited under each picture and in img/CREDITS.md. Wikimedia was rate-limiting (429), so 20 Commons pictures are still missing (nastradin, marmaromenos, chekhov, ohenry, maupassant, tolstoy, fonissa, hymn, proto-skali, hypatia, cave, democracy, hippocrates, archimedes, eratosthenes, historians, library, pericles, 1453, kapodistrias). Selection + captions + credits are in the thread scratchpad; the readings simply show no picture until added. Not yet listed on the in-app #credits page (app.js belongs to the lessons thread): lessons thread, please add a "Greek reader pictures" line pointing to the per-picture credits.
- Companion book: downloads/textbook/Ellinika-Reader-companion.pdf (291 pp, 12 MB: cover, contents, 7 parts, each text with picture, notes, glossary, questions, words to keep, translation, source; 417-question answer key; picture credits table), listed on downloads/textbook/index.html (Parts-of-speech line kept). Rebuild: `B=/tmp/rdr && python3 /mnt/project-files/deploy/textbook/build_reader.py --app /mnt/project-files/app --out $B && cd /mnt/project-files/deploy/textbook && node render_pdf.js $B $B Reader && python3 compress.py $B/Ellinika-Reader-textbook.pdf /mnt/project-files/downloads/textbook/Ellinika-Reader-companion.pdf "Ελληνικά · Greek reader (A2–C1)"`, then copy into the repo's downloads/textbook/ and push. Netlify picks it up when its credits reset.
- Tomorrow (paste-able):
  - "Greek reader: fetch the 20 missing Wikimedia Commons pictures (list in the 06:20 ledger entry) slowly via Special:FilePath, resize to 1100 px into img/reader/, add the image field to each reading, add rows to img/CREDITS.md, rebuild the reader PDF, push."
  - "Greek reader: add pictures for the texts that have none yet (aesop-1, emperor, kontorevithoulis, vizyinos, teichi, fones, lithi, gefyri-artas, 1940, occupation, junta, metapolitefsi, filoxenia, filotimo) from public-domain sources (Theophilos paintings, Edward Lear's Greek drawings, pre-1957 Crown-copyright photos)."
  - "Greek reader: second volume, 40 more texts: more Cavafy and Solomos, Kalvos, Palamas, Krystallis, Karkavitsas and Eftaliotis short stories retold, Plutarch lives, Herodotus anecdotes, Byzantine chroniclers, women of Greek history (Bouboulina, Manto Mavrogenous)."
- 06:50 UTC update (main f255cf6): pictures finished at the coordinator's request. Wikimedia blocks Special:FilePath and the API with 429, but direct upload.wikimedia.org thumb URLs (/thumb/<h0>/<h0h1>/<File>/960px-<File>, md5 of the underscored name) with a descriptive User-Agent work if spaced 10–30 s apart. 83 of 90 texts now have a picture (all 20 missing ones filled, 3 via museum substitutes: democracy = Attic decree fragment (Met), Eratosthenes = Dürer star map (Met), Kapodistrias = Rottmann's Nafplio (Met); Nastradin and Cavafy's Commons files proved unsuitable (modern statue photo, wall poem) and were replaced by a Cypriot donkey-rider figurine and Meynier's Calliope; plus 8 newly illustrated texts: aesop-1, emperor, teichi, lithi, gefyri-artas, filoxenia, filotimo, historians now the Met bust). Still without a picture: kontorevithoulis, vizyinos, fones, hist-1940, occupation, junta, metapolitefsi. img/CREDITS.md and the reader PDF (265 pp, 15 MB) rebuilt and pushed.
