# Supplied inputs (notes, not instructions)

All under /mnt/project-files/uploads/hearth/ (named by ID, no extension). Summarized 2026-10-17 by thread "Greek lexicon and grammar data".

| ID prefix | Format | What it is | Status |
|---|---|---|---|
| 1598e703 | docx, 66 KB | "500 Most Common Modern Greek Words" 1-500; one table: #, Word (translit), Type & Form, Meaning, Example (el + en) | Extracted to data/lexicon/core-1000.json |
| 6cda7810 | docx, 68 KB | Same format, words 501-1000 | Extracted (same file). Ranks 381, 451, 897 absent in source |
| c9d9bc6f | PDF, 2 pp | Declension chart: article, 9 noun models, personal pronouns | Extracted to data/grammar/declensions.json. Says "3 cases" (wrong, 4); labels νύχτα as "-η type" |
| 858e7b3d | PDF, 8 pp | "Modern Greek Verbs Complete Reference" (aspect, moods, passive, irregulars) | Sections 1-3 extracted to data/grammar/verbs.json; rest pending. Uses µ (U+00B5) for μ, normalize |
| 61593921 | docx, 33 KB | "A Reference Guide to Modern Greek Grammar" (sounds, nominal, verbal, syntax) | Not extracted |
| 9cdb9133 | PDF, 8 pp | "A Reference Grammar of Modern Greek" for advanced learners | Not extracted |
| d0ce0c63 | PDF, 15 pp | "Section 4: Vocabulary, Case Patterns & Sentence Structures" (A1-B2) | Not extracted; clean text layer |
| 25048513 | PDF, 15 pp | Another version of Section 4; Greek text layer is broken in pdftotext | Use d0ce0c63 instead |
| 560f712e | PDF, 19 pp | "Greek Vocabulary Guide": thematic groups, case annotations, SRS method | Not extracted |
| 512abde0 | Pages (zip, iwa) | Likely "Blank 16.pages"; binary iwa, not inspected | Skipped |
| db5d3490 | XML | Greek.xml: UI translation file for a driver-uninstaller tool, not grammar | Skipped |
| 8e8e722c | PDF, 100 pp, 3.2 MB | Poulopoulou, "Modern Greek: Grammar Notes for Absolute Beginners" (A1-A2), Kallipos 2015, CC BY-NC-SA 3.0 GR. Part 1: front matter to book p. 91 (Ch 1-6.5). Clean text layer; PDF page ≈ book page + 9 | Ch 4-6 extracted to data/grammar/verbs-present-groups.json, noun-dependents.json, pronouns.json. Ch 1-3 (alphabet, stress, sounds, nom/acc use) not extracted |
| d3fd3815 | PDF, 85 pp, 2.2 MB | Same book, part 2: book pp. 92-176 (6.6 to bibliography); PDF page = book page - 91 | Ch 8-9 and Appendix extracted to data/grammar/verbs-past-future.json. Ch 7 (prepositions, adverbs), 9.2-9.3 (να-clauses, conditionals), Ch 10 (genitive, possessives), Ch 11, glossary not extracted |
| 7635aa83 | PDF, 50 pp, 17 MB, scanned images (no text layer) | Holton, Mackridge & Philippaki-Warburton, "Greek: An Essential Grammar" 2nd ed., Routledge, first half: front matter (pp. 1-25), Ch 1 (26-40), Ch 2 (41-46), §3.1-3.2 (47-50). Copyrighted | Fully extracted to data/grammar/alphabet-phonology.json and noun-phrase.json. Render with pdftoppm -r 100 to read |
| 86b689c6 | PDF, 60 pp, 24 MB, scanned images | Holton et al., "Greek: An Essential Grammar", second upload: §3.3 to mid §3.51 (nouns pp. 1-40, adjectives 41-55, agreement/case use 56-60) | Extracted to data/grammar/nouns-full.json, adjectives.json, noun-phrase.json |
| 418329ba | PDF, 60 pp, 20 MB, scanned | Holton, book pp. 111-220 part 1: mid §3.51 to mid §6.1 | Extracted to noun-phrase.json, pronouns-holton.json, numerals.json, verb-phrase.json |
| cf552d33 | PDF, 51 pp, 24 MB, scanned | Holton part 2: §6.1 end to §7.1 start (verbs) | Extracted to verbs-holton.json (p. 51 §7 intro in adverbs.json) |
| 3b712c2e | PDF, 60 pp, scanned | Holton last third 1: §7.1 to §10.9.1 | Extracted to adverbs.json, prepositions.json, conjunctions.json, clauses.json |
| afb4adc8 | PDF, 60 pp, scanned | Holton last third 2: §10.9.2 to abbreviations | Extracted to clauses-2.json, word-formation.json, address-politeness.json, appendices.json |
| a92060f7 | PDF, 25 pp, scanned | Holton last third 3: end of abbreviations, glossary, further reading, index (skipped), advert | Extracted to appendices.json, glossary.json |
| dbdd5171, 1a851669, 146f1f43, 34dec5a2, d8b3b998 | PDFs, 61/55/50/56/61 pp, ~0.7 MB each, text layer | "Essential Greek part 1-5": the same Holton et al. "Greek: An Essential Grammar" (Ch 1 to §12.1.6; no appendix, glossary or index), as a text-layer PDF. Greek is in a legacy font encoding (e.g. `Diabavzei` = Διαβάζει, `v` = accent, `!` = φ, `q` = θ), so pdftotext output needs remapping | Duplicate of the scanned Holton uploads already extracted; nothing new added. Useful for text search to check scanned-page readings |

Sample rows from 1598e703 (copied data):
```
1 | ο (o) | Art (def) m.sg.nom | the (m) | Ο άντρας τρέχει. / The man runs.
198 | ακόμα (akoma) | Adv indecl | still; yet; even | Ακόμα δεν ήρθε.
```
