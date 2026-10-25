# Brief: collocations and related words for production practice

Do NOT call any mcp__hearthbot__ tools. Do not install packages. Write only the output file you are given. Do the linguistic work yourself (you are a fluent Greek lexicographer and teacher); a script may only write/validate JSON you composed.

Purpose: the learner (grammar ~B1, aiming at B2 exam and intellectual conversation) needs to PRODUCE words in natural combinations. For each input entry, write:
- "collocations": 2–4 high-frequency, natural Modern Greek word combinations containing the lemma (any inflected form), each {"el": "...", "en": "..."}. Prefer verb+noun, adjective+noun, noun+genitive, fixed prepositional uses (e.g. for απόφαση: παίρνω απόφαση / take a decision; οριστική απόφαση / final decision; κατά την απόφαση του δικαστηρίου...). For function words, give typical frames instead (για να + subj., παρά το ότι...).
- "synonyms": 0–3 Modern Greek near-synonyms (lemmas), most useful first; mark register in brackets when it differs, e.g. "ζω (everyday)".
- "antonyms": 0–2 lemmas, only clear opposites.
- "family": 0–4 derived/related lemmas a learner can guess from this one (απόφαση → αποφασίζω, αποφασιστικός).
Keep it accurate and standard; no invented combinations; register-mark slang/learned items.

Input: JSON array of {lemma, pos, gloss}. Output: JSON array, same order, one object per input: {"lemma": exact input lemma, "collocations": [...], "synonyms": [...], "antonyms": [...], "family": [...]}. Validate it parses and matches the input lemmas. Report in at most two lines.
