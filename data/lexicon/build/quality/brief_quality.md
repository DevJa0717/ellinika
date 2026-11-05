# Brief: quality pass on new lexicon entries (sense order and collocations)

Do NOT call any mcp__hearthbot__ tools. Do not install packages. Do not run git. Write only the output file you are given. Do the linguistic work yourself (you are a fluent Greek lexicographer); a script may only write/validate JSON you composed.

Input: JSON array of {lemma, pos, gloss, example, collocations [{el,en}], synonyms, antonyms, family}. These entries were written and reviewed once already; this pass checks two things only:
1. Sense order in "gloss": the sense a learner meets most often in today's Greek (speech, news) must come first; rarer, technical or older senses after. Missing main senses must be added. Keep glosses short (semicolon between senses).
2. Collocations and related words: every collocation must be a natural, frequent Modern Greek combination with correct agreement, accents and an accurate English; drop or replace odd, invented or rare ones (keep 2-4). Synonyms must be true near-synonyms in the main sense, antonyms true opposites, family real words of the same root. Remove anything doubtful rather than guess.
Also fix an example that contradicts a corrected first sense.

Output: JSON array with ONLY the entries that need a change (empty array if none), each:
{"lemma": "<exact>", "gloss": "<new gloss, only if changed>", "example": {"el","en"} (only if changed), "collocations": [...full new list, only if changed], "synonyms": [...], "antonyms": [...], "family": [...] (each only if changed), "why": "<short reason>"}
Only change what is actually wrong or badly ordered; do not rewrite good material for taste. Validate the output parses and every lemma exists in the input. Report in at most three lines: entries checked, gloss reorders, collocation fixes.
