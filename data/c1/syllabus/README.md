# C1 (Γ1) Modern Greek: syllabus and exam material

Retrieved 2026-10-18 from the Centre for the Greek Language (ΚΕΓ), https://www.greek-language.gr/certification/. This is for personal, non-commercial study only. The ΚΕΓ papers are © ΚΕΓ, and the exam texts are adapted from third-party publications (credited in each item).

## Files
- **c1-spec.json** has six parts:
  - `exam`: the five papers, task types, timings, word counts, points, the 60%-per-skill pass rule, the holistic writing scale for Γ1, and the indicative study hours.
  - `can_do`: 43 descriptors, each in Greek and English. They come from the ΚΕΓ Γ1 level page, the ΚΕΓ self-assessment grid and the CEFR 2001 C1 descriptors. The Greek versions of the CEFR descriptors are my own translations and are flagged as such.
  - `grammar_inventory`: 29 topics with Greek examples. Each topic is tied to evidence in the sample papers where there is any.
  - `text_types`: 17 entries.
  - `themes`: 12 entries.
  - `functions`: 20 entries.
- **reading-tasks.json** holds 17 tasks and 97 questions:
  - 8 reading tasks (Κατανόηση γραπτού λόγου) from the two official Γ1 sample series.
  - 8 use-of-language tasks (Χρήση γλώσσας): error spotting, phrase gap-fill, word formation, and synonyms/definitions.
  - 1 extra Γ1 reading task from the 2022 candidate guide. That one has no published key, so its answers are `null`.
  - All other answers come from the papers' own keys (ΛΥΣΕΙΣ). For the error-spotting items, the key gives only the wrong word; the `suggested_correction` is my own addition.
  - Gaps in the texts are marked `[n]`, and matching tasks number their paragraphs `[n]`.
- **writing-speaking-prompts.json** contains:
  - 4 Γ1 writing prompts, each with an English gloss.
  - Both Γ1 speaking sets: warm-up questions, 16 monologue questions, 4 picture sets (the images themselves are not included) and 11 discussions with A/B role cards.
  - 2 B2 writing prompts and one B2 set of monologue questions, for comparison.
- **sample-papers/** has 14 official PDFs, each with a `.txt` extraction (made with `pdftotext -layout`):
  - Γ1, two series: reading, use of language, listening, writing and oral.
  - B2, series 1, for comparison: reading, use of language, writing and oral.
  - The Γ1 listening audio (`g1_kpl_v_akoystiko.mp3`, 35 MB). The listening PDFs include the answer keys and full transcripts (ΚΕΙΜΕΝΑ CD), which can be used as listening or reading texts.
- **spec-docs/** contains:
  - The Γ1 and B2 structure tables and the general structure document.
  - The Γ1 writing criteria and the Γ1 level-description page (HTML and TXT).
  - The self-assessment grid, the 2022 exam guide, and the CEFR in English.
- **sources.json** records the title, author, URL, licence note, retrieval date and file for every item.

## Caveats and what I couldn't get
- The ΚΕΓ publishes no explicit Γ1 grammar list; the only list it gives is the idioms list on the level page. I compiled the grammar inventory myself from standard Modern Greek grammar and checked it against the sample papers.
- The sample papers are older: they date from about 2011–2013 and use the post-2010 format. I found no newer Γ1 papers online. The book "Εξεταστικά θέματα 2015-2018, Γ1 & Γ2" and the Γ1 sample-papers book can only be bought in print.
- I did not find a public, detailed rubric for the Γ1 speaking test.
- The Greek text of `dome_ton_exetastikon_thematon_genika.txt` came out garbled because of the PDF's font encoding; read the PDF instead.
- I did not download the full audio zip for C1–C2 (`audio_exetastika_C1-C2.zip`, 366 MB), which goes with the older 2001-era practice books.
- I found no public level syllabus from the Ε.Κ.Π.Α. Διδασκαλείο. Its leaflet has no level content.
- I did not find an official Greek translation of the CEFR online.
- I extracted the listening tasks only as raw text (the `.txt` files), not into structured JSON.
