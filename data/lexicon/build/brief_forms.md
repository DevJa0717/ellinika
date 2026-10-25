# Brief: inflected forms + consistency check for Modern Greek lexicon entries

Do NOT call any mcp__hearthbot__ tools. Do not write anything under /mnt/project-files. Do not install packages. Write only the output file you are given. Do the linguistic work yourself (you are a fluent Greek lexicographer); a script may only write/validate JSON you composed.

Input: a JSON array of lexicon entries. For EACH entry output one object, same order:
{"lemma": "<exactly as input>", "forms": [...], "fix": {...}}   ("fix" only when something must change)

## 1. forms
Every distinct inflected written form of the word in Standard Modern Greek (monotonic accents, lowercase unless the lemma is capitalised), INCLUDING the lemma itself. These feed a tap-to-look-up index, so completeness of common forms matters more than rare ones.
- Nouns: nom/gen/acc/voc singular and plural (plural only if used). Include common variant genitives (e.g. both -ου forms if both are used).
- Adjectives / participles / ordinals / pronouns / articles that decline: all masculine, feminine, neuter forms in all cases, sg and pl; plus the -α adverb if one exists (ωραία). Do not add comparatives.
- Verbs: present (6 persons), imperfect (6), simple past/aorist (6), perfective subjunctive stem forms (θα/να + 6 persons, e.g. γράψω γράψεις γράψει γράψουμε γράψετε γράψουν), imperatives (imperfective and perfective, 2sg and 2pl), gerund in -οντας/-ώντας; and for verbs with a passive: passive present (6), passive past/aorist (6), passive perfective subjunctive (6), passive imperative where used, and the -μένος participle in m/f/n sg (μένος, μένη, μένο) and pl (μένοι, μένες, μένα). Include common colloquial variants (e.g. -ούνε, -ανε endings; -άει and -ά for -άω verbs). Deponents: their own present, imperfect, aorist, subjunctive, imperative.
- Indeclinables (adverbs, prepositions, conjunctions, particles, phrases): just ["lemma"] (for multiword phrases, the phrase itself).

## 2. fix (consistency check)
Check these fields and give corrected values only where wrong or missing, as dotted paths: {"noun.model": "f-α-a", "noun.gen_sg": "...", "verb.aorist_1sg": "...", "adjective.model": "...", "needs_review": false, "lemma_fix": "..."}.
- Noun models must match Holton's paradigms (ids below). Pay special attention to feminine -α nouns: f-α-a = gen. pl. stressed on the PENULT (ελπίδα→ελπίδων, εβδομάδων, εικόνων, μητέρων, ομάδων, σελίδων: most -άδα/-ίδα, -όνα, many 3-syllable -α with penult stress); f-α-b = gen. pl. stressed on the FINAL (θάλασσα→θαλασσών, γυναικών, ωρών, καρδιών; all -ία, -εια, -ιά, -τρια, -ισσα). Also: masc -ας: m-ας-a (γείτονας, pl -ες, gen.pl like γειτόνων; αγώνας→αγώνων) vs m-ας-b (τουρίστας, άντρας, μήνας: gen.pl on final -ών). -ος masc: m-ος-fixed (stress stays: γάμος, οδηγός), m-ος-antepenult-a (άνθρωπος→ανθρώπου), m-ος-antepenult-b (καλόγερος→καλόγερου). Neuter -ο: n-ο-a (θέατρο→θεάτρου) vs n-ο-b (σύννεφο→σύννεφου) — and penult-stressed -ο neuters (βουνό, βιβλίο) are n-ο-a.
- Valid noun models: m-ας-a, m-ας-b, m-ης, m-ος-fixed, m-ος-antepenult-a, m-ος-antepenult-b, m-έας, m-imparisyllabic-final, m-imparisyllabic-penult, m-imparisyllabic-antepenult, f-α-a, f-α-b, f-η-ες, f-ος, f-η-εις, f-imparisyllabic-ά, f-imparisyllabic-ού, f-ω-b, common-ής-είς, n-ο-a, n-ο-b, n-ί, n-ι, n-ος-2syl, n-ος-3syl, n-μα, n-ιμο, n-ας, n-ως, n-ον, indecl. If truly none fits (πυρ, οξύ, μέλι-type), use "irregular" and put the forms in "forms".
- Valid adjective models: adj-ος-η-ο, adj-ος-α-ο, adj-ος-ια-ο, adj-ύς-ιά-ύ, adj-ής-ιά-ί, adj-πολύς, adj-ής-ές-fixed, adj-ης-ες-shift, adj-ης-α-ικο, adj-άς-ού-άδικο, adj-ων-ουσα-ον, indecl, or "irregular" (e.g. two-ending έγκυος, ευγνώμων, μέγας; then give the forms).
- Verbs: aorist_1sg should be the everyday modern form. For learned verbs prefer the form people actually use (e.g. passive aorist συνελήφθην is fine; for εκρήγνυμαι use εξερράγην only if nothing commoner exists). conj_group must be A, B1, B2, deponent or irregular.
- needs_review: set false when you settle the doubt; leave true only if a form is still genuinely uncertain.
- lemma_fix: only if the lemma is not a real dictionary headword (e.g. an inflected form).
Do not touch glosses, examples, themes or cefr.

Output: JSON array (UTF-8, ensure_ascii False) at the output path; validate it parses and has one object per input entry. Report in at most three lines: entries, fixes made, still needs_review.
