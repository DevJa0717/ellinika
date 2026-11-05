# Brief: second-pass review of new Modern Greek lexicon entries

Do NOT call any mcp__hearthbot__ tools. Do not install packages. Do not run git. Write only the output file you are given. Do the linguistic work yourself (you are a fluent Greek lexicographer and a careful editor); a script may only write/validate JSON you composed.

Input: a JSON array of lexicon entries written by another writer (lemma, pos, form_key, gloss, register?, example {el,en}, noun/verb/adjective object, cefr_est, themes?). Read EVERY entry and check:
1. gloss: is it the right meaning, with the most common sense first? Wrong or misleading senses, false friends, missing main sense.
2. example.el: natural, idiomatic Modern Greek a native would say or read today; correct agreement (article/adjective/noun gender, case, number), verb forms, accents, final -ν rule (την/στην/τον keep ν before vowels and κ π τ ξ ψ μπ ντ γκ τσ τζ; τη/στη otherwise); uses the headword. example.en: an accurate, idiomatic translation of exactly that sentence.
3. grammar data: noun gender, gen_sg (real form, correct stress), model (Holton paradigm ids as in /home/user/ellinika/data/lexicon/build/10k/brief_10k.md); verb aorist_1sg / aorist_passive_1sg / participle (real, everyday forms), conj_group; adjective f/n forms and model.
4. pos and cefr_est plausible (A1-C1); register marked where a learner needs it (vulgar/colloquial/formal).
5. Is it a real headword (not an inflected form, a misspelling, or a proper name)? If not, mark it for dropping.

Output: a JSON array containing ONLY the entries that need a change (an empty array if all are fine), each:
{"lemma": "<exactly as input>", "set": {"<dotted path>": <new value>, ...}, "why": "<short reason>"}
Paths: "gloss", "example" (give the whole {"el","en"} object), "form_key", "cefr_est", "register", "pos", "noun.gen_sg", "noun.gender", "noun.model", "verb.aorist_1sg", "verb.aorist_passive_1sg", "verb.participle", "verb.conj_group", "adjective.f", "adjective.n", "adjective.model". To drop an entry: {"lemma": ..., "set": {"DROP": true}, "why": ...}.
When you change a principal part, also update form_key to match ("Gen: X | f (1st decl)", "Pres: X | Aor: Y", "f: X, n: Y").
Only change what is actually wrong; do not rewrite good sentences for taste. Validate the output parses. Report in at most three lines: entries reviewed, changes by kind, drops.
