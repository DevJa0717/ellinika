# C1 word list

`c1-words.json` holds **1232 C1 lemmas**, ranked 5001–6232. None of them is in the app lexicon (`data/lexicon/core-1000.json`, `core-3000.json`, `build/known.json`) at build time. The lexicon thread's own upcoming misses are excluded too.

## Schema
Each entry uses the lexicon schema exactly: rank, lemma, translit, pos, pos_raw, form_key, gloss, example{el,en}, cefr_est, freq_count, freq_rank, source, noun/verb/adjective. Two fields are added: **topic** and **seen_in**.

- `cefr_est` is "C1". `freq_count` and `freq_rank` are null.
- `source` is "C1 corpus (data/c1); entry written by Claude".
- **Nouns** have `form_key` = `Gen: X | Pl: Y | g (decl)`, with ", pl only" appended for plural-only nouns. They also add `noun.nom_pl`. The app only reads `noun.gen_sg`, so the extra field is harmless.
- **Verbs** have `form_key` = `Pres: X | Aor: Y` and `verb.conj_group` (A/B1/B2/deponent/irregular).
- **Adjectives** have `form_key` = `m/f: F, n: N` or `indecl`, plus the m/f/n forms and a model.
- All text is NFC, monotonic Greek.

## Counts
1232 entries; 732 have a non-empty `seen_in`.

| pos | n |
|---|---|
| noun | 678 |
| adjective | 349 |
| verb | 133 |
| adverb | 46 |
| other | 23 |
| conjunction | 2 |
| pronoun | 1 |

| topic | n |
|---|---|
| general | 328 |
| politics | 144 |
| psychology | 143 |
| science | 122 |
| economics | 107 |
| law | 88 |
| language | 88 |
| society | 82 |
| arts | 68 |
| culture | 62 |

## Method
1. Lemmas came from the following sources, in priority order: C1 lessons (`app/lessons/c1-*.json`), video cues (`data/c1/videos/videos-c1.json`), reading texts (`data/c1/texts/`), and then own knowledge of C1 registers (politics, law, economics, science, psychology, arts, language, society, culture, general). The topics are listed in the topic table above.
2. Entries were written in batches of about 200 in a compact line format. A builder script produced the JSON and transliterated with a copy of the lexicon's `translit.py`.
3. Dedupe ran against the current lexicon, matching accent-insensitively, and against `build/misses/*.out.json`. Entries the lexicon had already imported from this file under the source string above were not counted as "known", so they stay here. In all, about 300 written lines were dropped as already present in the lexicon.
4. `seen_in` lists the C1 lessons, video ids and text ids in which a form of the lemma appears. It is computed by stem-prefix matching for single words and substring matching for phrases.
5. Each entry was checked for: all keys present, NFC, one accent per polysyllabic form, and an example that uses the word.

## Caveats
- `seen_in` is heuristic. Expect occasional false positives (shared stems) and misses (suppletive forms).
- The lexicon thread merges this file into `core-3000.json`. Re-running the dedupe later will therefore show those entries as known, which is expected.
- Glosses and examples are Claude-written and not corpus-attested. Rare forms such as plurals of abstract nouns are marked "—" where they are not in normal use.
