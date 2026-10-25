# Brief: write Modern Greek lexicon entries from a frequency candidate list

Do NOT call any mcp__hearthbot__ tools. Do not write anything under /mnt/project-files. Do not install packages.

Input: a JSON array of candidates, each {i, cand, upos, forms, count}. They come from the OpenSubtitles 2018 Greek frequency list (word forms), lemmatized automatically by spaCy, so many are WRONG lemmas (inflected forms like ξέρεις, πάρω, έκανα, πέθανε; typos like οχι, vα; abbreviations).
Also read known_core.json in the same folder: accent-stripped lowercase lemmas and principal parts already in our 1,000-word lexicon.

For each candidate, in order:
1. Normalize to the dictionary lemma: verbs = present 1sg (ξέρεις→ξέρω, πάρω→παίρνω, πέθανε→πεθαίνω, κοιμηθεί→κοιμάμαι); nouns = nom sg (or nom pl if plural-only); adjectives = masc nom sg; fix accents/typos.
2. SKIP it if: the normalized lemma (accent-stripped, lowercase) is in known_core.json; or it's a proper name, a foreign word, an abbreviation, a typo with no real lemma, a bare interjection with no learner value, or a slur. Mild colloquial words that a learner really hears (e.g. διάολος, φίλε as φίλος if not known) are fine.
3. SKIP duplicates within your own output: if two candidates normalize to the same lemma, write one entry and list both i values.
4. Otherwise write one entry. Use correct Standard Modern Greek (monotonic accents). Be accurate: principal parts and genitives must be real forms. If unsure of a form, set it to null and add "needs_review": true.

Entry format (match exactly; omit sub-objects that don't apply):
{
 "lemma": "αντιμετωπίζω",
 "translit": "antimetopizo",      // simple Latin, same scheme as existing data: η/ι/υ/ει/οι→i, ω/ο→o, αι→e, ου→ou, β→v, γ→g, δ→d, θ→th, ξ→ks, φ→f, χ→ch, ψ→ps, αυ/ευ→av/ev or af/ef by voicing, μπ→b initially else mb, ντ→d initially else nd, γκ→g initially else ng
 "pos": "verb",                   // one of: noun, verb, adjective, adverb, pronoun, preposition, conjunction, particle, numeral, article, other (use other for phrases/ordinals/interjections)
 "pos_raw": "Verb",               // Noun, Verb, Adj, Adv, Pron, Prep, Conj, Part, Num, Phr, Interj
 "form_key": "Pres: αντιμετωπίζω | Aor: αντιμετώπισα",
 "gloss": "to face; to deal with",  // short, semicolon-separated senses
 "example": {"el": "Πρέπει να αντιμετωπίσουμε το πρόβλημα.", "en": "We must deal with the problem."},  // ONE natural, everyday sentence, 4-10 words, A2-B1 grammar where possible, written by you
 "verb": {"present_1sg": "αντιμετωπίζω", "aorist_1sg": "αντιμετώπισα", "conj_group": "A"},   // conj_group: "A" (-ω stressed before ending), "B1" (-άω/-ώ like αγαπώ), "B2" (-ώ like θεωρώ/μπορώ), "deponent" (-ομαι/-άμαι/-ούμαι). Non-active verbs: aorist_1sg is the passive aorist (κοιμήθηκα). Verbs with no aorist: null.
 "cefr_est": "B1",                // your estimate of the CEFR level at which a learner normally meets this word: A1, A2, B1, B2, C1
 "cand_i": [1160]
}
Nouns: "form_key": "Gen: συνάντησης | f (1st decl)", "noun": {"gen_sg": "συνάντησης", "gender": "f", "declension": 1}  // declension 1 = fem -α/-η and masc -ας/-ης; 2 = -ος/-ο; 3 = neuter -μα, -ος(neut), fem -η/-ση with -εις/-ης; gender m/f/n/common.
Adjectives: "form_key": "m/f: σκοτεινή, n: σκοτεινό", "adjective": {"m": "σκοτεινός", "f": "σκοτεινή", "n": "σκοτεινό"}
Indeclinables: "form_key": "indecl".

Output: write a JSON array (UTF-8, ensure_ascii False) to the output path you are given, then validate it parses with python3 and report: entries written, candidates skipped, and any entries flagged needs_review. Keep the report to a few lines.
