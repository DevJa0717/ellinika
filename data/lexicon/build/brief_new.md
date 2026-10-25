# Brief: write Modern Greek lexicon entries from a frequency candidate list

Do NOT call any mcp__hearthbot__ tools. Do not write anything under /mnt/project-files. Do not install packages. Write only the output file you are given.

Input: a JSON array of candidates, each {i, cand, upos, forms, count}. They come from the OpenSubtitles 2018 Greek frequency list (word forms), lemmatized automatically by spaCy, so many lemmas are WRONG (inflected forms like ξέρεις, πάρω, έκανα, πέθανε; typos like οχι; abbreviations). The `forms` list shows the real corpus forms behind each candidate; use it to work out the true lemma.
Also read known.json (path given): accent-stripped lowercase lemmas and principal parts already in the lexicon.

For each candidate, in order:
1. Normalize to the dictionary lemma: verbs = present 1sg (ξέρεις→ξέρω, πάρω→παίρνω, πέθανε→πεθαίνω, κοιμηθεί→κοιμάμαι); nouns = nom sg (nom pl if plural-only); adjectives = masc nom sg; fix accents/typos. Diminutives that are fully lexical (κοριτσάκι, σπιτάκι) are fine as their own lemma.
2. SKIP it if: the normalized lemma (accent-stripped, lowercase) is in known.json; or it is a proper name, a foreign word, an abbreviation, a typo with no real lemma, a bare interjection with no learner value, or a slur/obscenity. Mild colloquial words a learner really hears are fine.
3. If two candidates normalize to the same lemma, write ONE entry and list both i values in cand_i.
4. Otherwise write one entry in correct Standard Modern Greek (monotonic accents). Be accurate: principal parts, genitives and models must be real. If unsure of a form, set it to null and add "needs_review": true.

Entry format (match exactly; omit sub-objects that do not apply):
{
 "lemma": "αντιμετωπίζω",
 "translit": "antimetopizo",
 "pos": "verb",
 "pos_raw": "Verb",
 "form_key": "Pres: αντιμετωπίζω | Aor: αντιμετώπισα",
 "gloss": "to face; to deal with",
 "example": {"el": "Πρέπει να αντιμετωπίσουμε το πρόβλημα.", "en": "We must deal with the problem."},
 "verb": {"present_1sg": "αντιμετωπίζω", "aorist_1sg": "αντιμετώπισα", "aorist_passive_1sg": "αντιμετωπίστηκα", "participle": "αντιμετωπισμένος", "conj_group": "A"},
 "cefr_est": "B1",
 "themes": ["society"],
 "cand_i": [1160]
}

Field rules:
- translit: simple Latin: η/ι/υ/ει/οι→i, ω/ο→o, αι→e, ου→ou, β→v, γ→g, δ→d, θ→th, ξ→ks, φ→f, χ→ch, ψ→ps, αυ/ευ→av/ev before voiced sounds and vowels, af/ef before voiceless, μπ→b initially else mb, ντ→d initially else nd, γκ→g initially else ng. No accents.
- pos: one of noun, verb, adjective, adverb, pronoun, preposition, conjunction, particle, numeral, article, other (other = phrases/ordinals/interjections). pos_raw: Noun, Verb, Adj, Adv, Pron, Prep, Conj, Part, Num, Phr, Interj.
- gloss: short English, semicolon-separated senses, most common first. Verbs start with "to ".
- example: ONE natural everyday sentence, 4-10 words, written by you, using the word (any inflected form), A2-B1 grammar where possible. Make it carry meaning (not "This is a X."); vary sentence shapes.
- verb: present_1sg; aorist_1sg (active simple past; for non-active verbs like κοιμάμαι, the passive aorist κοιμήθηκα; null if none); aorist_passive_1sg (only for active verbs that have a commonly used passive aorist, else omit); participle (-μένος passive participle if in common use, else omit); conj_group: "A" (stress before -ω: γράφω), "B1" (-άω/-ώ like αγαπώ), "B2" (-ώ like θεωρώ, μπορώ), "deponent" (-ομαι/-άμαι/-ούμαι), "irregular" for είμαι-type.
- Nouns: "form_key": "Gen: συνάντησης | f (1st decl)", "noun": {"gen_sg": "συνάντησης", "gender": "f", "declension": 1, "model": "f-η-ες"}. declension 1 = fem -α/-η(-ες) and masc -ας/-ης; 2 = -ος/-ο and neuter -ι/-ί; 3 = neuter -μα, -ος(neut), fem -η/-ση with -εις, -ως/-ον neuters. gender m/f/n/common. Add "pl_only": true for plural-only nouns.
  model = the Holton paradigm id it declines like. Choose from:
  m-ας-a (γείτονας, gen.pl stress may move: αγώνας, αιώνας), m-ας-b (τουρίστας, άντρας: pl -ες, gen.pl -ών), m-ης (εργάτης), m-ος-fixed (οδηγός, γάμος: stress fixed), m-ος-antepenult-a (άνθρωπος: stress moves to penult in gen), m-ος-antepenult-b (καλόγερος: stress stays), m-έας (κουρέας), m-imparisyllabic-final (γαλατάς -άδες), m-imparisyllabic-penult (μανάβης -ηδες), m-imparisyllabic-antepenult (φούρναρης),
  f-α-a (ελπίδα, εβδομάδα, εικόνα, μητέρα, ομάδα, σελίδα, most -άδα/-ίδα: gen.pl stressed on PENULT, ελπίδων), f-α-b (θάλασσα, αξία, γυναίκα, ώρα, καρδιά, all -ία/-εια/-ιά/-τρια/-ισσα: gen.pl stressed on FINAL, θαλασσών), f-η-ες (τέχνη, αγάπη), f-ος (μέθοδος), f-η-εις (κυβέρνηση, πόλη), f-imparisyllabic-ά (γιαγιά -άδες), f-imparisyllabic-ού (αλεπού), f-ω-b (ηχώ),
  common-ής-είς (συγγενής), n-ο-a (θέατρο: stress may move), n-ο-b (αντρόγυνο: stress stays), n-ί (παιδί), n-ι (αγόρι), n-ος-2syl (κράτος), n-ος-3syl (έδαφος), n-μα (αποτέλεσμα), n-ιμο (πλύσιμο), n-ας (κρέας), n-ως (φως, γεγονός), n-ον (ενδιαφέρον).
  Use null (and needs_review) only if none fits (e.g. indeclinable loanwords: then "model": "indecl", gen_sg same as nom).
- Adjectives: "form_key": "m/f: σκοτεινή, n: σκοτεινό", "adjective": {"m": "σκοτεινός", "f": "σκοτεινή", "n": "σκοτεινό", "model": "adj-ος-η-ο"}. models: adj-ος-η-ο (ψηλός), adj-ος-α-ο (τέλειος, ωραίος), adj-ος-ια-ο (γλυκός, φρέσκος), adj-ύς-ιά-ύ (βαρύς), adj-ής-ιά-ί (καφετής), adj-ής-ές-fixed (ακριβής), adj-ης-ες-shift (συνήθης), adj-ης-α-ικο (τεμπέλης), adj-άς-ού-άδικο (φαγάς), adj-ων-ουσα-ον (επείγων), "indecl" (μπλε, ροζ).
- Indeclinables (adverbs, particles etc.): "form_key": "indecl".
- cefr_est: the CEFR level at which a learner normally meets the word: A1, A2, B1, B2, C1.
- themes: ONLY if the word clearly belongs to one or more B2 exam topics; otherwise omit the field. Ids: work (jobs, workplace, economy), society (social issues, politics, law, current events, crime), environment (nature, climate, energy, animals, weather), technology (computers, internet, devices, science), health (body, illness, medicine, fitness, food as nutrition), education (school, university, learning, youth), culture (arts, media, film, music, books, sport, leisure, travel, tourism). Most function words and everyday basics get no theme.
- cand_i: the candidate i values this entry covers.

Output: write a JSON array (UTF-8, ensure_ascii False) to the output path, validate it parses with python3, and report in at most four lines: entries written, candidates skipped, entries flagged needs_review.
