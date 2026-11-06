# Brief: example sentence and grammar-header check (lexicon entries)

Do NOT call any mcp__hearthbot__ tools. Do not install packages. Do not run git. Write only the output file you are given. Do the linguistic work yourself (you are a fluent Greek lexicographer and teacher); a script may only write/validate JSON you composed.

The learner (grammar ~B1, aiming at the B2 exam; declensions are a weak spot) sees each entry's example sentence and grammar header in the app's tap-lookup and in drills. Input: JSON array of {lemma, pos, gloss, form_key, noun|verb|adjective (grammar block), example {el, en}}.

Check two things only:
1. Example: the Greek must be natural, idiomatic, grammatical Modern Greek (agreement, case, accents, final -ν rule, word order) that uses the headword (any inflected form) in its FIRST gloss sense, and the English must translate it accurately. Replace an example that is wrong, unnatural, a calque, uses a different word instead of the headword, or illustrates only a minor sense. Keep replacements short (6–14 words), everyday or news register, and useful for a B1–B2 learner.
2. Grammar header: noun gender and genitive singular (gen_sg), noun model; verb aorist_1sg / aorist_passive_1sg / participle (current standard forms; null only if no form is in use); adjective feminine/neuter forms. Fix only clear errors. When you change gen_sg or an aorist, also give the matching new form_key in the same style as the input (e.g. "Gen: πόλης | f (3rd decl)" or "Pres: γράφω | Aor: έγραψα").

Output: JSON array with ONLY the entries that need a change (empty array if none), each:
{"lemma": "<exact>", "set": {"example": {"el": "...", "en": "..."}, "noun.gen_sg": "...", "noun.gender": "...", "noun.model": "...", "verb.aorist_1sg": "...", "verb.aorist_passive_1sg": "...", "verb.participle": "...", "adjective.f": "...", "adjective.n": "...", "form_key": "..."}, "why": "<short reason>"}
Include in "set" only the keys you change. Do not rewrite good material for taste. Validate the output parses and every lemma exists in the input. Report in at most three lines: entries checked, examples replaced, grammar fixes.
