#!/usr/bin/env python3
"""Build the declension and conjugation drill data (library/drills/*.json).

Every paradigm is a real word from the app's word list (data/lexicon/core-1000.json and
core-3000.json) with its full paradigm taken from Wiktionary's inflection tables
(tools/drills/wiktionary-el-extract.jsonl.gz, a filtered copy of kaikki.org's Greek extract,
CC BY-SA 4.0). A paradigm is kept only when it agrees with what the word list already says
about the word (genitive singular and gender for nouns, feminine and neuter for adjectives,
present, aorist and passive aorist for verbs), so two independent sources back every item.
Context items come from the word list's own example sentences.

Usage: python3 tools/drills/build.py            (writes library/drills/ and prints a report)
"""
import gzip, json, os, re, sys, unicodedata, collections

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "library", "drills")
WIKT = os.path.join(ROOT, "tools", "drills", "wiktionary-el-extract.jsonl.gz")

GREEK = re.compile(r"^[α-ωάέήίόύώϊϋΐΰς]+$")
SKIP_TAGS = {"rare", "archaic", "dated", "obsolete", "dialectal", "poetic", "Katharevousa", "literary", "idiomatic", "uncommon"}
SOFT_TAGS = {"informal", "colloquial"}  # accepted, never shown as the main answer

def nfc(s): return unicodedata.normalize("NFC", s).strip()

def ok_word(f):
    return bool(f) and GREEK.match(f) is not None

def accents(w): return sum(1 for c in w if c in "άέήίόύώΐΰ")

def stress_ok(w):
    # Monosyllables may be unaccented; everything else carries exactly one accent.
    vowels = len(re.findall(r"(αι|ει|οι|ου|αυ|ευ|[αεηιουωάέήίόύώϊϋΐΰ])", w))
    a = accents(w)
    return a == 1 or (a == 0 and vowels <= 1)

def load_lex():
    lex = []
    for f in ("core-1000.json", "core-3000.json"):
        lex += json.load(open(os.path.join(ROOT, "data", "lexicon", f)))
    return lex

def load_wikt():
    by = collections.defaultdict(list)
    with gzip.open(WIKT, "rt") as fh:
        for line in fh:
            d = json.loads(line)
            by[(d["word"], d["pos"])].append(d)
    return by

def cell_forms(entry, need, ban=()):
    """Forms whose tags include every tag in `need` and none in `ban`; returns (main, accepted)."""
    main, acc = [], []
    for f in entry.get("forms", []):
        tags = set(f.get("tags") or [])
        if not need <= tags or tags & set(ban): continue
        if tags & SKIP_TAGS: continue
        # Wiktionary sometimes annotates a cell ("κάνω (κάμνω →)") or lists two forms in one ("πάνε, άμε").
        raw = re.sub(r"\s*\(.*$", "", nfc(f.get("form", "")))
        for part in re.split(r"\s*[,–]\s*|\s+-\s+", raw):
            bracket = "[" in part or "]" in part  # Wiktionary brackets mark learned or rare forms
            form = part.strip("[] ")
            if not ok_word(form.replace("θα ", "", 1)): continue
            if form not in acc: acc.append(form)
            if not tags & SOFT_TAGS and not bracket and form not in main: main.append(form)
    if not main: main = acc[:1]
    if not acc: return None
    # main answer first, then the other accepted spellings
    return [main[0]] + [x for x in acc if x != main[0]]

CASES = ["nominative", "genitive", "accusative", "vocative"]
NUMS = ["singular", "plural"]
GEN = {"m": "masculine", "f": "feminine", "n": "neuter"}


# ---------------- rule-generated paradigms (only where Wiktionary has no table) ----------------
# Kept only when the generated forms and the lexicon's forms index (written independently, per word)
# give exactly the same set of forms, so these too are backed by two sources.
NUC = re.compile(r"(αι|ει|οι|ου|υι|αυ|ευ|[αεηιουω])")
PLAIN = str.maketrans("άέήίόύώ", "αεηιουω")
ACC1 = {"α": "ά", "ε": "έ", "η": "ή", "ι": "ί", "ο": "ό", "υ": "ύ", "ω": "ώ"}

def strip(w): return w.translate(PLAIN)

def nuclei(w):
    # Plain vowel count; words with synizesis (μπάνιο, δουλειά) may come out wrong here,
    # and the forms-index comparison below then rejects them.
    return [m.span() for m in NUC.finditer(strip(w))]

def accent_pos(w):
    """Syllable (1 = last) carrying the accent, or 0."""
    nu = nuclei(w)
    for i, (a, b) in enumerate(nu):
        if any(c in "άέήίόύώ" for c in w[a:b]): return len(nu) - i
    return 0

def put_accent(w, k):
    """Accent the k-th syllable from the end (digraphs take it on the second letter)."""
    s = strip(w)
    nu = nuclei(s)
    if k > len(nu) or k < 1: return None
    a, b = nu[len(nu) - k]
    i = b - 1
    return s[:i] + ACC1[s[i]] + s[i + 1:]

def limit(w, mx):
    k = accent_pos(w)
    return put_accent(w, mx) if k > mx else w

def gen_noun(lemma, model):
    L = lemma
    ult = accent_pos(L) == 1
    def stem(n): return L[:-n]
    def keep(st, ends): return [st + e for e in ends]
    if model == "m-ος-fixed":
        st = stem(2)
        if ult: return [st + e for e in ["ός", "ού", "ό", "έ", "οί", "ών", "ούς", "οί"]]
        if accent_pos(L) != 2: return None
        return keep(st, ["ος", "ου", "ο", "ε", "οι", "ων", "ους", "οι"])
    if model in ("m-ος-antepenult-a", "m-ος-antepenult-b"):  # άνθρωπος, ανθρώπου · πονοκέφαλος, πονοκέφαλου
        st = stem(2)
        if accent_pos(L) != 3: return None
        f = keep(st, ["ος", "ου", "ο", "ε", "οι", "ων", "ους", "οι"])
        if model.endswith("-a"):
            for i in (1, 5, 6): f[i] = put_accent(f[i], 2)
        return f
    if model == "n-ο-b":  # κόκκαλο, κόκκαλου: the stress stays put
        st = stem(1)
        if ult: return None
        return keep(st, ["ο", "ου", "ο", "ο", "α", "ων", "α", "α"])
    if model == "n-ιμο":  # δέσιμο, δεσίματος, δεσίματα, δεσιμάτων
        if not L.endswith("ιμο") or accent_pos(L) != 3: return None
        st = strip(L[:-1])
        return [L, put_accent(st + "ατος", 3), L, L, put_accent(st + "ατα", 3), put_accent(st + "ατων", 2), put_accent(st + "ατα", 3), put_accent(st + "ατα", 3)]
    if model == "m-ης":
        st = stem(2)
        if ult: return [st + e for e in ["ής", "ή", "ή", "ή", "ές", "ών", "ές", "ές"]]
        f = keep(st, ["ης", "η", "η", "η", "ες", "ων", "ες", "ες"]); f[5] = put_accent(st + "ων", 1); return f
    if model == "f-α-b":
        st = stem(1)
        if ult: return [st + e for e in ["ά", "άς", "ά", "ά", "ές", "ών", "ές", "ές"]]
        f = keep(st, ["α", "ας", "α", "α", "ες", "ων", "ες", "ες"]); f[5] = put_accent(st + "ων", 1); return f
    if model == "f-α-a":
        st = stem(1)
        if ult: return None
        f = keep(st, ["α", "ας", "α", "α", "ες", "ων", "ες", "ες"]); f[5] = limit(f[5], 2); return f
    if model == "f-η-ες":
        st = stem(1)
        if ult: return [st + e for e in ["ή", "ής", "ή", "ή", "ές", "ών", "ές", "ές"]]
        f = keep(st, ["η", "ης", "η", "η", "ες", "ων", "ες", "ες"]); f[5] = put_accent(st + "ων", 1); return f
    if model == "f-η-εις":
        st = stem(1)
        if ult: return None
        f = keep(st, ["η", "ης", "η", "η", "εις", "εων", "εις", "εις"])
        for i in (4, 6, 7): f[i] = limit(f[i], 2)
        f[5] = put_accent(st + "εων", 3); return f
    if model in ("n-ο-a", "n-ο-b"):
        st = stem(1)
        if ult: return [st + e for e in ["ό", "ού", "ό", "ό", "ά", "ών", "ά", "ά"]]
        f = keep(st, ["ο", "ου", "ο", "ο", "α", "ων", "α", "α"])
        if model == "n-ο-a": f[1], f[5] = limit(f[1], 2), limit(f[5], 2)
        return f
    if model == "n-ι":
        st = stem(1)
        return [L, strip(st) + "ιού", L, L, st + "ια", strip(st) + "ιών", st + "ια", st + "ια"]
    if model == "n-ί":
        st = stem(1)
        return [L, st + "ιού", L, L, st + "ιά", st + "ιών", st + "ιά", st + "ιά"]
    if model == "n-μα":
        st = stem(2)
        f = [L, st + "ματος", L, L, st + "ματα", st + "ματων", st + "ματα", st + "ματα"]
        f = [limit(x, 3) for x in f]; f[5] = put_accent(f[5], 2); return f
    if model == "m-ας-a":
        st = stem(2)
        if ult: return None
        f = keep(st, ["ας", "α", "α", "α", "ες", "ων", "ες", "ες"]); f[5] = limit(f[5], 2); return f
    if model == "m-ας-b":
        st = stem(2)
        if ult: return None
        f = keep(st, ["ας", "α", "α", "α", "ες", "ων", "ες", "ες"]); f[5] = put_accent(st + "ων", 1); return f
    return None

def gen_adj(lemma, model):
    if model not in ("adj-ος-η-ο", "adj-ος-α-ο") or not lemma.endswith(("ος", "ός")): return None
    st = lemma[:-2]
    ult = accent_pos(lemma) == 1
    fe = "α" if model == "adj-ος-α-ο" else "η"
    if ult:
        fa = ACC1[fe]
        M = ["ός", "ού", "ό", "έ", "οί", "ών", "ούς", "οί"]; F = [fa, fa + "ς", fa, fa, "ές", "ών", "ές", "ές"]; N = ["ό", "ού", "ό", "ό", "ά", "ών", "ά", "ά"]
    else:
        M = ["ος", "ου", "ο", "ε", "οι", "ων", "ους", "οι"]; F = [fe, fe + "ς", fe, fe, "ες", "ων", "ες", "ες"]; N = ["ο", "ου", "ο", "ο", "α", "ων", "α", "α"]
    cells = []
    for k in range(8):  # sg nom gen acc voc, pl nom gen acc voc; genders m f n within
        for E in (M, F, N): cells.append(st + E[k])
    return cells

def forms_agree(gen, idx_forms):
    """Every generated form must be in the word list's forms index (lower-cased, so Δευτέρα matches δευτέρας).
    Extra index forms are variants (κόκαλο beside κόκκαλο, learned διώξεως) and no longer block the table."""
    if None in gen: return False
    g = set(x.lower() for x in gen if x)
    return bool(g) and g <= {x.lower() for x in idx_forms}

# ---------------- nouns ----------------
NOUN_NOTES = {
    "m-ος-fixed": "Masculine -ος, stress stays put: ο δρόμος, του δρόμου, τον δρόμο, δρόμε! · οι δρόμοι, των δρόμων, τους δρόμους. The vocative of most two-syllable nouns ends in -ε.",
    "m-ος-antepenult-a": "Masculine -ος stressed on the third syllable from the end: the accent moves one syllable right in the genitive singular and in the genitive and accusative plural (ο άνθρωπος, του ανθρώπου, των ανθρώπων, τους ανθρώπους).",
    "m-ος-antepenult-b": "Masculine -ος stressed on the third from the end that keeps its stress in every form, as many colloquial and diminutive words do (του φιλαράκου, τους φιλαράκους).",
    "m-ας-a": "Masculine -ας with a plural in -ες: ο πατέρας, του πατέρα, τον πατέρα · οι πατέρες, των πατέρων, τους πατέρες. The genitive plural often shifts the stress (γειτόνων, αγώνων).",
    "m-ας-b": "Masculine -ας whose genitive plural is stressed on the last syllable: οι άντρες, των αντρών · οι μήνες, των μηνών. Words in -ίας and -ιστας belong here.",
    "m-ης": "Masculine -ης with a plural in -ες: ο μαθητής, του μαθητή, τον μαθητή · οι μαθητές, των μαθητών, τους μαθητές. The genitive plural is always stressed on -ών.",
    "m-έας": "Masculine -έας: ο γονέας, του γονέα · οι γονείς, των γονέων, τους γονείς (plural in -είς, learned genitive plural in -έων).",
    "m-imparisyllabic-final": "Masculine 'imparisyllabic' nouns stressed on the ending: ο καφές, του καφέ · οι καφέδες, των καφέδων. The plural adds a syllable (-δες).",
    "m-imparisyllabic-penult": "Masculine imparisyllabic nouns stressed on the stem: ο χασάπης, του χασάπη · οι χασάπηδες, των χασάπηδων. The plural adds -δες and keeps the stress.",
    "m-imparisyllabic-antepenult": "Masculine imparisyllabic noun stressed on the third from the end: ο φούρναρης, του φούρναρη · οι φουρνάρηδες, των φουρνάρηδων.",
    "f-α-a": "Feminine -α whose genitive plural keeps the stress on the stem's own syllable or shifts to the penult only when needed: η μητέρα, της μητέρας · οι μητέρες, των μητέρων · η εβδομάδα, των εβδομάδων.",
    "f-α-b": "Feminine -α with the genitive plural stressed on the last syllable: η ώρα, της ώρας · οι ώρες, των ωρών · η θάλασσα, των θαλασσών. This is the most common feminine type.",
    "f-η-ες": "Feminine -η with plural -ες: η φωνή, της φωνής · οι φωνές, των φωνών. The genitive plural is stressed on -ών.",
    "f-η-εις": "Feminine -η with plural -εις (the 'πόλη' type, ancient -ις/-εως): η πόλη, της πόλης · οι πόλεις, των πόλεων, τις πόλεις. The genitive plural -εων moves the stress to the penult (αποφάσεων).",
    "f-ος": "Feminine nouns in -ος: they decline like masculine -ος nouns but take feminine articles (η μέθοδος, της μεθόδου, τη μέθοδο · οι μέθοδοι, των μεθόδων, τις μεθόδους).",
    "f-imparisyllabic-ά": "Feminine imparisyllabic in stressed -ά: η γιαγιά, της γιαγιάς · οι γιαγιάδες, των γιαγιάδων.",
    "f-imparisyllabic-ού": "Feminine imparisyllabic in -ού: η αλεπού, της αλεπούς · οι αλεπούδες, των αλεπούδων.",
    "f-ω-b": "Feminine learned noun in -ώ: η ηχώ, της ηχούς (no plural in use).",
    "n-ο-a": "Neuter -ο: το βιβλίο, του βιβλίου · τα βιβλία, των βιβλίων. Words stressed on the third from the end move the stress in the genitive (αυτοκίνητο, του αυτοκινήτου).",
    "n-ο-b": "Neuter -ο that keeps its stress in the genitive, typical of everyday words (του σύννεφου, των σύννεφων · του κοτόπουλου).",
    "n-ι": "Neuter -ι: το σπίτι, του σπιτιού · τα σπίτια, των σπιτιών. The genitive adds -ιού/-ιών and moves the stress to the end.",
    "n-ί": "Neuter stressed -ί: το παιδί, του παιδιού · τα παιδιά, των παιδιών.",
    "n-μα": "Neuter -μα: το θέμα, του θέματος · τα θέματα, των θεμάτων. The genitive adds -τος/-των; the stress moves forward when the word would otherwise be stressed four syllables from the end.",
    "n-ιμο": "Neuter verbal nouns in -ιμο: το τρέξιμο, του τρεξίματος · τα τρεξίματα, των τρεξιμάτων.",
    "n-ος-2syl": "Neuter -ος (ancient -ος, -ους): το κράτος, του κράτους · τα κράτη, των κρατών.",
    "n-ος-3syl": "Neuter -ος of three or more syllables: το μέγεθος, του μεγέθους · τα μεγέθη, των μεγεθών (stress shifts in the genitive).",
    "n-ον": "Neuter learned nouns in -ον (participles): το περιβάλλον, του περιβάλλοντος · τα περιβάλλοντα, των περιβαλλόντων.",
    "n-ας": "Neuter -ας: το κρέας, του κρέατος · τα κρέατα, των κρεάτων.",
    "n-ως": "Neuter -ως: το φως, του φωτός · τα φώτα, των φώτων; το γεγονός, του γεγονότος.",
    "irregular": "Irregular or learned noun; learn its forms as a set.",
    "common-ής-είς": "Common-gender learned noun in -ής: ο/η συγγενής, του/της συγγενή · οι συγγενείς, των συγγενών.",
}

def pick_entry(entries, test):
    for e in entries:
        if test(e): return e
    return None

RULE_NOUN_SKIP = {"τρίο"}  # forms index ties it to the numeral τρία; the plural is disputed (τα τρίο / τα τρία)

def build_nouns(lex, wk, report):
    out = []
    for e in lex:
        if e["pos"] != "noun": continue
        n = e.get("noun") or {}
        model = n.get("model")
        if model in (None, "indecl") or n.get("declension") in (None, "indecl", 0): report["noun_skip_indecl"] += 1; continue
        lemma, gender = e["lemma"], n.get("gender")
        if gender == "common": gender = "c"  # ο/η γιατρός: masculine forms, either article
        if gender not in GEN and gender != "c": report["noun_skip_gender"] += 1; continue
        cands = wk.get((lemma, "noun"), [])
        pl_only = bool(n.get("pl_only"))
        def fits(w):
            ns = cell_forms(w, {"nominative", "plural" if pl_only else "singular"})
            if not ns or lemma not in ns: return False
            if n.get("gen_sg") and not pl_only:
                gs = cell_forms(w, {"genitive", "singular"})
                if not gs or n["gen_sg"] not in gs: return False
            return True
        w = pick_entry(cands, fits)
        if not w and not pl_only and lemma not in RULE_NOUN_SKIP:  # no Wiktionary table, or none that agrees with the word list: try the class rule (gated on the forms index)
            g = gen_noun(lemma, model)
            if g and (not n.get("gen_sg") or g[1] == n["gen_sg"]) and forms_agree(g, INV.get(lemma, set())):
                if model.startswith("m-ος") and g[3] not in INV.get(lemma, set()): g[3] = ""
                out.append({"l": lemma, "g": gender, "m": model, "lv": e.get("cefr_est") or "B2", "en": short_gloss(e["gloss"]),
                            "r": e.get("freq_rank") or 99999, "f": g, "src": "rule"})
                report["nouns"] += 1; report["nouns_rule"] += 1
                continue
            # Singular-heavy words (months, Παναγία, σωτηρία): the plural is rare, so the index lacks it. Keep the table when
            # nominative, genitive and accusative singular are all attested, and leave unattested cells empty.
            idx = {x.lower() for x in INV.get(lemma, set())}
            if g and None not in g and (not n.get("gen_sg") or g[1] == n["gen_sg"]) and all(g[i].lower() in idx for i in (0, 1, 2)):
                part = [x if x and x.lower() in idx else "" for x in g]
                out.append({"l": lemma, "g": gender, "m": model, "lv": e.get("cefr_est") or "B2", "en": short_gloss(e["gloss"]),
                            "r": e.get("freq_rank") or 99999, "f": part, "src": "rule"})
                report["nouns"] += 1; report["nouns_rule_partial"] += 1
                continue
        if not w:
            report["noun_skip_nomatch" if cands else "noun_skip_nowikt"] += 1
            if cands: report["noun_mismatch_examples"].append(lemma)
            continue
        cells = []
        for num in NUMS:
            for case in CASES:
                f = cell_forms(w, {case, num})
                cells.append("|".join(f) if f and all(stress_ok(x) for x in f[:1]) else "")
        if not any(cells[4:]) and not pl_only and not cells[1]: report["noun_skip_thin"] += 1; continue
        out.append({"l": lemma, "g": gender, "m": model, "lv": e.get("cefr_est") or "B2", "en": short_gloss(e["gloss"]),
                    "r": e.get("freq_rank") or 99999, "f": cells})
        report["nouns"] += 1
    out.sort(key=lambda x: (LV.index(x["lv"]) if x["lv"] in LV else 9, x["r"]))
    return out

INV = {}
FI = {}
LV = ["A1", "A2", "B1", "B2", "C1", "C2"]

def short_gloss(g):
    g = re.sub(r"\s*\([^)]*\)", "", g or "").split(";")[0].strip()
    return g[:48]

# ---------------- adjectives ----------------
ADJ_NOTES = {
    "adj-ος-η-ο": "-ος, -η, -ο: masculine like δρόμος, feminine like φωνή, neuter like βιβλίο (καλός, καλή, καλό). The genitive plural is the same for all three genders.",
    "adj-ος-α-ο": "-ος, -α, -ο after a vowel (and some after -ρ): ωραίος, ωραία, ωραίο · νέος, νέα, νέο. The feminine keeps -α in every case (της ωραίας).",
    "adj-ος-ια-ο": "-ος, -ια, -ο: γλυκός, γλυκιά, γλυκό; feminine like δουλειά.",
    "adj-ύς-ιά-ύ": "-ύς, -ιά, -ύ: βαθύς, βαθιά, βαθύ; masculine and neuter plural add -ι- (οι βαθιοί, τα βαθιά).",
    "adj-ής-ές-fixed": "Learned -ής, -ής, -ές: ακριβής, ακριβές; genitive -ούς, plural -είς and -ή (οι ακριβείς, τα ακριβή, των ακριβών).",
    "adj-ης-ες-shift": "Learned -ης, -ης, -ες stressed on the stem: πλήρης, πλήρες; the stress moves in the neuter and genitive plural (σύνηθες, των συνήθων).",
    "adj-ων-ουσα-ον": "Participle-like -ων, -ουσα, -ον: ενδιαφέρων, ενδιαφέρουσα, ενδιαφέρον; masculine and neuter genitive -οντος.",
    "adj-ης-α-ικο": "Colloquial -ης, -α, -ικο: τεμπέλης, τεμπέλα, τεμπέλικο; plural τεμπέληδες.",
    "adj-ής-ιά-ί": "Colour adjectives -ής, -ιά, -ί: πορτοκαλής, πορτοκαλιά, πορτοκαλί; plural πορτοκαλιοί, πορτοκαλιές, πορτοκαλιά.",
    "adj-άς-ού-άδικο": "Colloquial -άς, -ού, -άδικο: φαγάς, φαγού, φαγάδικο; plural φαγάδες, φαγούδες, φαγάδικα.",
    "adj-πολύς": "πολύς, πολλή, πολύ is irregular: πολλοί, πολλές, πολλά; του πολύ / της πολλής are rare.",
    "irregular": "Irregular adjective; learn its forms as a set.",
}

def build_adjs(lex, wk, report):
    out = []
    for e in lex:
        if e["pos"] != "adjective": continue
        a = e.get("adjective") or {}
        model = a.get("model")
        if model in (None, "indecl"): report["adj_skip_indecl"] += 1; continue
        lemma = e["lemma"]
        cands = wk.get((lemma, "adj"), [])
        def fits(w):
            NB = ("comparative", "superlative")
            ms = cell_forms(w, {"nominative", "singular", "masculine"}, NB)
            fs = cell_forms(w, {"nominative", "singular", "feminine"}, NB)
            ns = cell_forms(w, {"nominative", "singular", "neuter"}, NB)
            return bool(ms and lemma in ms and fs and a.get("f") in fs and ns and a.get("n") in ns)
        w = pick_entry(cands, fits)
        if not w:  # also when Wiktionary disagrees with the word list
            g = gen_adj(lemma, model)
            if g and g[1] == a.get("f") and g[2] == a.get("n") and forms_agree(g, INV.get(lemma, set())):
                out.append({"l": lemma, "m": model, "lv": e.get("cefr_est") or "B2", "en": short_gloss(e["gloss"]),
                            "r": e.get("freq_rank") or 99999, "f": g, "src": "rule"})
                report["adjs"] += 1; report["adjs_rule"] += 1
                continue
        if not w:
            report["adj_skip_nomatch" if cands else "adj_skip_nowikt"] += 1
            if cands: report["adj_mismatch_examples"].append(lemma)
            continue
        cells = []
        for num in NUMS:
            for case in CASES:
                for g in "mfn":
                    f = cell_forms(w, {case, num, GEN[g]}, ("comparative", "superlative"))
                    cells.append("|".join(f) if f and stress_ok(f[0]) else "")
        if sum(1 for c in cells if c) < 18: report["adj_skip_thin"] += 1; continue
        # Masculine vocative only where the forms index knows it (καλέ μου φίλε yes, *όλε no).
        if cells[9] and cells[9].split("|")[0] not in INV.get(lemma, set()): cells[9] = ""
        out.append({"l": lemma, "m": model, "lv": e.get("cefr_est") or "B2", "en": short_gloss(e["gloss"]),
                    "r": e.get("freq_rank") or 99999, "f": cells})
        report["adjs"] += 1
    out.sort(key=lambda x: (LV.index(x["lv"]) if x["lv"] in LV else 9, x["r"]))
    return out

# ---------------- verbs ----------------
PERS = [("first-person", "singular"), ("second-person", "singular"), ("third-person", "singular"),
        ("first-person", "plural"), ("second-person", "plural"), ("third-person", "plural")]

def six(w, need, ban=()):
    row = []
    for p, n in PERS:
        f = cell_forms(w, need | {p, n}, ban)
        row.append("|".join(f) if f and stress_ok(f[0].split()[-1]) else "")
    return row

def verb_voice(w, voice):
    v = {voice}
    ban_dep = ("dependent", "future", "imperative", "participle")
    pres = six(w, v | {"imperfective", "indicative", "present"}, ban_dep + ("imperfect",))
    impf = six(w, v | {"imperfect", "indicative"}, ("future",))
    aor = six(w, v | {"past", "perfective", "indicative"}, ("dependent", "future", "imperfect"))
    dep = six(w, v | {"dependent", "perfective"}, ("future",))
    def imp(aspect):
        r = []
        for n in ("singular", "plural"):
            f = cell_forms(w, v | {"imperative", aspect, "second-person", n})
            r.append("|".join(f) if f and stress_ok(f[0]) else "")
        return r
    inf = cell_forms(w, v | {"infinitive-aorist"}) if voice == "passive" else None
    if voice == "active":
        inf = None
        for f in w.get("forms", []):
            t = set(f.get("tags") or [])
            if "infinitive-aorist" in t and "passive" not in t:
                x = nfc(f["form"])
                if ok_word(x): inf = [x]; break
    ptc = None
    if voice == "passive":
        p = cell_forms(w, {"participle", "passive", "past"})
        if p and p[0].endswith("ος"): ptc = p[0]
    return {"pres": pres, "impf": impf, "aor": aor, "dep": dep, "impP": imp("perfective"),
            "impI": imp("imperfective"), "inf": inf[0] if inf else "", "ptc": ptc or ""}

def build_verbs(lex, wk, report):
    out = []
    for e in lex:
        if e["pos"] != "verb": continue
        v = e.get("verb") or {}
        lemma = e["lemma"]
        deponent = v.get("conj_group") == "deponent" or lemma.endswith(("μαι",))
        cands = wk.get((lemma, "verb"), []) + (wk.get((lemma[:-1] + "άω", "verb"), []) if lemma.endswith("ώ") else []) \
            + (wk.get((lemma[:-4] + "ω", "verb"), []) if lemma.endswith("ομαι") else [])
        main_voice = "passive" if deponent else "active"
        if deponent and any(cell_forms(w, {"active", "present", "first-person", "singular"}, ("dependent",)) for w in cands if w["word"] == lemma):
            deponent, main_voice = False, "active"  # είμαι is tagged active
        def fits(w):
            pr = cell_forms(w, {main_voice, "imperfective", "indicative", "present", "first-person", "singular"}, ("dependent", "future", "imperative"))
            if not pr or lemma not in pr: return False
            if v.get("aorist_1sg"):
                ao = cell_forms(w, {main_voice, "past", "perfective", "indicative", "first-person", "singular"}, ("dependent", "future"))
                if ao: return v["aorist_1sg"] in ao
                # Verbs with one past tense (περιμένω → περίμενα, είμαι → ήμουν): the word list's "aorist" is the imperfect.
                im = cell_forms(w, {main_voice, "imperfect", "indicative", "first-person", "singular"}, ("future",))
                return bool(im and v["aorist_1sg"] in im)
            return True
        w = pick_entry(cands, fits)
        if not w:
            report["verb_skip_nomatch" if cands else "verb_skip_nowikt"] += 1
            if cands: report["verb_mismatch_examples"].append(lemma)
            continue
        A = verb_voice(w, main_voice)
        if not any(A["aor"]) and any(A["impf"]):
            A["aor"], A["one_past"] = list(A["impf"]), True
            if not any(A["dep"]): A["dep"] = list(A["pres"])
        if sum(1 for k in ("pres", "impf", "aor", "dep") for c in A[k] if c) < 18: report["verb_skip_thin"] += 1; continue
        item = {"l": lemma, "lv": e.get("cefr_est") or "B2", "en": short_gloss(e["gloss"]), "r": e.get("freq_rank") or 99999,
                "grp": v.get("conj_group") or "", "dep": deponent, "A": A}
        # A passive paradigm only for verbs whose word-list entry gives a passive aorist, and only if Wiktionary agrees.
        pa = v.get("aorist_passive_1sg")
        if not deponent and pa:
            P = verb_voice(w, "passive")
            ao = P["aor"][0].split("|") if P["aor"][0] else []
            if pa in ao and sum(1 for k in ("pres", "aor", "dep") for c in P[k] if c) >= 15:
                item["P"] = P; report["verbs_passive"] += 1
            else:
                report["verb_passive_dropped"] += 1
        out.append(item)
        report["verbs"] += 1
    out.sort(key=lambda x: (LV.index(x["lv"]) if x["lv"] in LV else 9, x["r"]))
    return out

# ---------------- rule-built verb paradigms (verbs Wiktionary has no usable table for) ----------------
# Each cell is built from the conjugation classes in data/grammar (verbs-present-groups.json, verbs-past-future.json):
# the stem plus the class endings, written without accents. A cell keeps only the forms that the word list's
# forms index (data/lexicon/forms-index.json, written independently per word) also has, and it takes the accent
# from there. So every form shown is backed by two sources, and hunspell checks it a third time afterwards.
AUG = [("αμφι", "αμφε"), ("υπερ", "υπερε"), ("περι", "περιε"), ("κατα", "κατε"), ("δια", "διε"), ("απο", "απε"), ("παρα", "παρε"),
       ("μετα", "μετε"), ("ανα", "ανε"), ("επι", "επε"), ("υπο", "υπε"), ("αντι", "αντε"), ("προ", "προε"),
       ("εισ", "εισε"), ("συν", "συνε"), ("συγ", "συνε"), ("συμ", "συνε"), ("συλ", "συνε"), ("συρ", "συνε"),
       ("συ", "συνε"), ("εκ", "εξε"), ("εξ", "εξε"), ("εν", "ενε"), ("εμ", "ενε"), ("εγ", "ενε"), ("ελ", "ενε"),
       ("κατ", "κατε"), ("δι", "διε"), ("απ", "απε"), ("παρ", "παρε"), ("μετ", "μετε"), ("αν", "ανε"),
       ("επ", "επε"), ("υπ", "υπε"), ("αντ", "αντε"), ("αφ", "αφε"), ("εφ", "εφε"), ("καθ", "καθε")]

def aug_variants(s):
    """The stem itself, with the syllabic augment, and with the internal augments of learned compounds."""
    out = [s, "ε" + s]
    for pre, rep in AUG:
        if s.startswith(pre) and len(s) > len(pre) + 1: out.append(rep + s[len(pre):])
    for i, c in enumerate(s):
        if c == "ε" and s[i:i + 2] not in ("ει", "ευ"): out.append(s[:i] + "ει" + s[i + 1:])
        if c == "α" and i == 0: out.append("η" + s[1:])
    seen = []
    for x in out:
        if x not in seen: seen.append(x)
    return seen

PLAININV = {}

def hits(lemma, plains, end=None):
    """Accented forms in the forms index for each unaccented candidate, main answer first.
    end: the endings of a class stressed on the ending (αγαπ-άς, μιμ-ούμαι, μιμηθ-ώ): the accent must fall inside it,
    so that the imperative κούνα is not taken for the present κουνά."""
    idx = PLAININV.get(lemma, {})
    out = []
    for p in plains:
        n = 0
        if end:
            e = next((x for x in sorted(end, key=len, reverse=True) if p.endswith(x)), "")
            n = len(nuclei(e)) or 1
        for f in sorted(idx.get(p, []), key=lambda w: -accent_pos(w)):  # earlier accent first: μιμήθηκαν before μιμηθήκαν
            if end and accent_pos(f) > n: continue
            if stress_ok(f) and f not in out: out.append(f)
    return "|".join(out)

def row(lemma, stems, ends, end=False):
    """ends: per person a list of endings. Stems are tried in order; the stem that gives the 1st person is preferred."""
    cells = []
    order = list(stems)
    for k, alts in enumerate(ends):
        cells.append(hits(lemma, [s + e for s in order for e in alts], alts if end else None))
        if k == 0 and cells[0]:
            first = strip(cells[0].split("|")[0])
            pref = [s for s in order if any(first == s + e for e in alts)]
            order = pref + [s for s in order if s not in pref]
    return cells

A_PRES = [["ω"], ["εις"], ["ει"], ["ουμε"], ["ετε"], ["ουν", "ουνε"]]
A_PAST = [["α"], ["ες"], ["ε"], ["αμε"], ["ατε"], ["αν", "ανε"]]
B1_PRES = [["αω", "ω"], ["ας"], ["αει", "α"], ["αμε", "ουμε"], ["ατε"], ["ανε", "αν", "ουν", "ουνε"]]
B2_PRES = [["ω", "αω"], ["εις", "ας"], ["ει", "αει"], ["ουμε", "αμε"], ["ειτε", "ατε"], ["ουν", "ουνε", "ανε", "αν"]]
B_IMPF = [["ουσα"], ["ουσες"], ["ουσε"], ["ουσαμε"], ["ουσατε"], ["ουσαν", "ουσανε"]]
P_ENDS = {  # passive and deponent presents, after Holton's classes
    "ομαι": [["ομαι"], ["εσαι"], ["εται"], ["ομαστε"], ["εστε", "οσαστε"], ["ονται"]],
    "αμαι": [["αμαι", "ουμαι"], ["ασαι"], ["αται"], ["ομαστε", "ουμαστε"], ["αστε", "οσαστε"], ["ουνται", "ονται", "ανται"]],
    "ιεμαι": [["ιεμαι"], ["ιεσαι"], ["ιεται"], ["ιομαστε"], ["ιεστε", "ιοσαστε"], ["ιουνται", "ιονται"]],
    "ουμαι": [["ουμαι"], ["εισαι", "ιεσαι"], ["ειται", "ιεται"], ["ουμαστε"], ["ειστε"], ["ουνται"]],
}
P_IMPF = {
    "ομαι": [["ομουν", "ομουνα"], ["οσουν", "οσουνα"], ["οταν", "οτανε"], ["ομασταν", "ομαστε"], ["οσασταν", "οσαστε"], ["ονταν", "οντουσαν"]],
    "αμαι": [["ομουν", "ομουνα"], ["οσουν", "οσουνα"], ["οταν", "οτανε"], ["ομασταν"], ["οσασταν"], ["ονταν", "οντουσαν", "ουνταν"]],
    "ιεμαι": [["ιομουν", "ιομουνα"], ["ιοσουν", "ιοσουνα"], ["ιοταν", "ιοτανε"], ["ιομασταν"], ["ιοσασταν"], ["ιονταν", "ιουνταν", "ιοντουσαν"]],
    "ουμαι": [["ουμουν"], ["ουσουν"], ["ουνταν", "ουταν"], ["ουμασταν"], ["ουσασταν"], ["ουνταν", "ουντουσαν"]],
}
PA_AOR = [["ηκα"], ["ηκες"], ["ηκε"], ["ηκαμε"], ["ηκατε"], ["ηκαν", "ηκανε"]]
PA_DEP = [["ω"], ["εις"], ["ει"], ["ουμε"], ["ειτε"], ["ουν", "ουνε"]]

def dep_stem(lemma, P, a1):
    """The perfective stem (γράψ-ω, διαθέσ-ω): a -ω form in the forms index whose stem ends like the aorist's."""
    best, score = None, 0
    A = strip(a1)[:-1]
    for p in PLAININV.get(lemma, {}):
        if not p.endswith("ω") or p.endswith(("ουμαι", "θω")): continue
        s = p[:-1]
        if not s or s[:2] != P[:2]: continue
        if not (p + "" in PLAININV[lemma] and (s + "εις") in PLAININV[lemma]): continue
        k = 0
        while k < min(len(s), len(A)) and s[-1 - k] == A[-1 - k]: k += 1
        if k < 2: continue
        sc = k * 2 + (0 if p == P else 1)
        if sc > score: best, score = s, sc
    return best

def passive_rule(lemma, pstem, ptype, apas):
    """Passive or deponent voice from a present stem + class, and the passive aorist."""
    e = ptype in ("ιεμαι", "ουμαι")
    V = {"pres": row(lemma, [pstem], P_ENDS[ptype], e), "impf": row(lemma, [pstem], P_IMPF[ptype], e),
         "aor": ["", "", "", "", "", ""], "dep": ["", "", "", "", "", ""], "impP": ["", ""], "impI": ["", ""], "inf": "", "ptc": ""}
    V["impI"][1] = V["pres"][4].split("|")[0] if V["pres"][4] else ""
    if apas and strip(apas).endswith("ηκα"):
        T = strip(apas)[:-3]
        V["aor"] = row(lemma, [T], PA_AOR)
        V["dep"] = row(lemma, [T], PA_DEP, True)
        if T.endswith("θ"): sg = [T[:-1] + "σου"]
        elif T.endswith("στ"): sg = [T[:-1] + "ου"]
        else: sg = []
        V["impP"] = [hits(lemma, sg), hits(lemma, [T + "ειτε"])]
        V["inf"] = hits(lemma, [T + "ει"]).split("|")[0]
        ptc = [f for p, fs in PLAININV.get(lemma, {}).items() for f in fs
               if p.endswith("μενος") and not p.endswith(("ομενος", "ουμενος", "ωμενος", "ιομενος", "αμενος"))]
        V["ptc"] = ptc[0] if len(ptc) == 1 else ""
    return V

def build_rule_verbs(lex, have, report):
    for form, lemmas in FI.items():
        for l in lemmas: PLAININV.setdefault(l, {}).setdefault(strip(form), []).append(form)
    out = []
    for e in lex:
        if e["pos"] != "verb" or e["lemma"] in have or " " in e["lemma"]: continue
        lemma, v = e["lemma"], e.get("verb") or {}
        grp, a1, apas = v.get("conj_group") or "", v.get("aorist_1sg"), v.get("aorist_passive_1sg")
        P = strip(lemma)
        if lemma not in INV: report["rverb_skip_noforms"] += 1; continue
        item = {"l": lemma, "lv": e.get("cefr_est") or "B2", "en": short_gloss(e["gloss"]), "r": e.get("freq_rank") or 99999,
                "grp": grp, "dep": False, "src": "rule"}
        kind_a, s = False, ""
        ptype = next((t for t in ("ιεμαι", "ουμαι", "αμαι", "ομαι") if P.endswith(t)), None)
        if ptype:  # deponent: present class from the ending, aorist from the word list
            if ptype == "ιεμαι": ptype = "ομαι" if P.endswith("ιομαι") else "ιεμαι"
            A = passive_rule(lemma, P[:-len(ptype)], ptype, a1)
            item["dep"] = True
        elif P.endswith("ω"):
            s = P[:-2] if P.endswith("αω") and grp in ("B1", "") else P[:-1]  # κουνάω: stem κουν-, like αγαπώ
            if grp == "B1" or P.endswith("αω") or (grp != "B2" and lemma.endswith("ώ") and (s + "ας") in PLAININV[lemma]):
                pres, impf, kind = row(lemma, [s], B1_PRES, True), row(lemma, [s], B_IMPF, True), "B1"
            elif lemma.endswith("ώ"):
                pres, impf, kind = row(lemma, [s], B2_PRES, True), row(lemma, [s], B_IMPF, True), "B2"
            else:
                pres, impf, kind = row(lemma, [s], A_PRES), row(lemma, aug_variants(s), A_PAST), "A"
                kind_a = True
            A = {"pres": pres, "impf": impf, "aor": [""] * 6, "dep": [""] * 6, "impP": ["", ""], "impI": ["", ""], "inf": "", "ptc": ""}
            ds = dep_stem(lemma, P, a1) if a1 else None
            if a1 and ds:
                Aa = strip(a1)[:-1]
                stems = [Aa] + [x for x in aug_variants(ds) if x != Aa]
                # Singular and 3rd plural keep the augment; the bare stem would give the imperative (διάθεσε), not έ-/διέθεσε.
                sg = [Aa] + [x for x in aug_variants(ds) if x not in (Aa, ds)]
                if Aa == ds: sg = [ds]
                A["aor"] = row(lemma, sg, A_PAST[:5] + [["αν"]])
                A["aor"][5] = "|".join(x for x in (A["aor"][5].split("|") + hits(lemma, [ds + "αν", ds + "ανε"]).split("|")) if x)
                A["aor"][5] = "|".join(dict.fromkeys(A["aor"][5].split("|"))) if A["aor"][5] else ""
                # 1st/2nd plural drop the syllabic augment: γράψαμε, not *έγραψαμε
                A["aor"][3] = hits(lemma, [ds + "αμε"] + [x + "αμε" for x in stems if x != "ε" + ds])
                A["aor"][4] = hits(lemma, [ds + "ατε"] + [x + "ατε" for x in stems if x != "ε" + ds])
                A["dep"] = row(lemma, [ds], A_PRES)
                colloq = kind == "B1" and "άω" in pres[0]  # αγάπα, but no *αντικαθιστά
                A["impP"] = [hits(lemma, [ds + "ε"] + ([s + "α"] if colloq else [])),
                             hits(lemma, [ds + "τε", ds + "ετε"])]
                A["inf"] = A["dep"][2].split("|")[0] if A["dep"][2] else ""
            elif a1 and a1 == hits(lemma, [s + "α"]).split("|")[0] or (not a1 and any(impf)):
                A["aor"], A["one_past"] = list(impf), True
                A["dep"] = list(pres)
            if kind == "A": A["impI"] = [hits(lemma, [s + "ε"]), pres[4].split("|")[0] if pres[4] else ""]
            elif kind == "B1": A["impI"] = [hits(lemma, [s + "α"]) if "άω" in pres[0] else "", hits(lemma, [s + "ατε"])]
            else: A["impI"] = ["", pres[4].split("|")[0] if pres[4] else ""]
            if apas and not item["dep"]:
                pt = {"A": "ομαι", "B1": "ιεμαι", "B2": "ουμαι"}[kind]
                Pv = passive_rule(lemma, s, pt, apas)
                if kind == "B1" and not Pv["pres"][0]:  # learned -ώ verbs: αντικαθίσταμαι, εξαρτώμαι
                    Pv2 = passive_rule(lemma, s, "αμαι", apas)
                    if sum(1 for c in Pv2["pres"] if c) > sum(1 for c in Pv["pres"] if c): Pv = Pv2
                if sum(1 for k in ("pres", "aor", "dep") for c in Pv[k] if c) >= 15 and apas in Pv["aor"][0].split("|"):
                    item["P"] = Pv; report["rverbs_passive"] += 1
        else:
            report["rverb_skip_shape"] += 1; continue
        # Principal parts must agree with the word list: the 1st singular present is the lemma, the aorist is the word list's.
        p0 = A["pres"][0].split("|") if A["pres"][0] else []
        if lemma not in p0: report["rverb_skip_present"] += 1; report["rverb_present_examples"].append(lemma); continue
        A["pres"][0] = "|".join([lemma] + [x for x in p0 if x != lemma])  # the word list's headword first (υποτιμώ, not υποτιμάω)
        if a1 and not A.get("one_past"):
            ao = A["aor"][0].split("|") if A["aor"][0] else []
            if a1 not in ao: report["rverb_skip_aorist"] += 1; report["rverb_aorist_examples"].append(lemma); continue
            A["aor"][0] = "|".join([a1] + [x for x in ao if x != a1])
        if kind_a and not A.get("one_past"):  # the ε→ει augment candidate (διαμειν-) can pick up aorist forms (διαμείναμε): keep those out of the imperfect
            aorset = {x for k in ("aor", "impP") for c in A[k] for x in c.split("|") if x}
            eiv = [x for x in aug_variants(s) if "ει" in x and "ει" not in s]
            A["impf"] = ["|".join(x for x in c.split("|") if x and not (x in aorset and any(strip(x).startswith(v) for v in eiv))) for c in A["impf"]]
        if sum(1 for k in ("pres", "impf", "aor", "dep") for c in A[k] if c) < 18:
            report["rverb_skip_thin"] += 1; report["rverb_thin_examples"].append(lemma); continue
        item["A"] = A
        out.append(item)
        report["rverbs"] += 1
    return out

# ---------------- verbs written out by hand (tools/drills/manual-verbs.txt) ----------------
MANUAL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "manual-verbs.txt")

def build_manual_verbs(lex, have, report):
    """Hand-written tables for the verbs left over (suppletive compounds, learned verbs, impersonals).
    A form stays only if the forms index or the el_GR word list also has it; the rest are reported."""
    if not os.path.exists(MANUAL): return []
    if not HUN: load_hunspell()
    by = {e["lemma"]: e for e in lex if e["pos"] == "verb"}
    blocks, cur = [], None
    for line in open(MANUAL, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#"): continue
        if line.startswith("@"):
            w = line[1:].split(); cur = {"l": w[0], "flags": set(w[1:]), "t": {}}; blocks.append(cur); continue
        k, _, v = line.partition(":")
        cur["t"][k.strip()] = [c.strip() for c in v.split(",")]
    out = []
    for b in blocks:
        lemma = b["l"]
        if lemma in have or lemma not in by: report["mverb_skip"] += 1; continue
        e, known = by[lemma], INV.get(lemma, set())
        def ok(f): return f in known or all(t in HUN for t in f.split())
        def cell(c):
            if c in ("", "-"): return ""
            fs = [nfc(x) for x in c.split("/")]
            keep = [f for f in fs if ok(f)]
            for f in fs:
                if f not in keep: report["mverb_dropped"].append(lemma + ":" + f)
            return "|".join(keep)
        A = {t: [cell(c) for c in (b["t"].get(t) or ["-"] * n)] for t, n in (("pres", 6), ("impf", 6), ("aor", 6), ("dep", 6), ("impP", 2), ("impI", 2))}
        A["inf"] = cell(b["t"].get("inf", ["-"])[0]).split("|")[0]
        A["ptc"] = ""
        if "one_past" in b["flags"]:
            A["aor"], A["one_past"] = list(A["impf"]), True
            if not any(A["dep"]): A["dep"] = list(A["pres"])
        out.append({"l": lemma, "lv": e.get("cefr_est") or "B2", "en": short_gloss(e["gloss"]), "r": e.get("freq_rank") or 99999,
                    "grp": (e.get("verb") or {}).get("conj_group") or "", "dep": "dep" in b["flags"], "src": "manual", "A": A})
        report["mverbs"] += 1
    return out

# ---------------- pronouns and articles ----------------
HAND = {  # singular-only pronouns that decline like ένας (Wiktionary has no table for them)
    "κανένας": ["κανένας|κανείς", "καμία|καμιά", "κανένα", "κανενός", "καμίας|καμιάς", "κανενός", "κανέναν|κανένα", "καμία|καμιά", "κανένα"],
    "καθένας": ["καθένας", "καθεμία|καθεμιά", "καθένα", "καθενός", "καθεμίας|καθεμιάς", "καθενός", "καθέναν|καθένα", "καθεμία|καθεμιά", "καθένα"],
}

def build_pronouns(wk, report):
    """Article and pronoun tables written out by hand, then checked against Wiktionary where it has them."""
    def adj_like(word):
        for w in wk.get((word, "pron"), []) + wk.get((word, "adj"), []) + wk.get((word, "det"), []):
            cells = []
            for num in NUMS:
                for case in ["nominative", "genitive", "accusative"]:
                    for g in "mfn":
                        f = cell_forms(w, {case, num, GEN[g]}, ("weak",))
                        cells.append("|".join(f) if f else "")
            if sum(1 for c in cells if c) >= 15: return cells
        return None
    tables = []
    # Definite article (data/grammar/declensions.json), final -ν rule noted in feedback.
    art = ["ο", "η", "το", "του", "της", "του", "τον", "τη|την", "το",
           "οι", "οι", "τα", "των", "των", "των", "τους", "τις", "τα"]
    tables.append({"id": "art-def", "l": "ο, η, το", "en": "the (definite article)", "lv": "A1", "kind": "g3", "f": art,
                   "note": "την keeps its -ν before a vowel and before κ, π, τ, μπ, ντ, γκ, τσ, τζ, ξ, ψ; elsewhere τη is usual (τη Δευτέρα, την Τρίτη)."})
    indef = ["ένας", "μια|μία", "ένα", "ενός", "μιας|μίας", "ενός", "έναν|ένα", "μια|μία", "ένα"]
    tables.append({"id": "art-indef", "l": "ένας, μια, ένα", "en": "a, an; one", "lv": "A1", "kind": "g3sg", "f": indef,
                   "note": "The indefinite article has no plural; 'some' is μερικοί/κάποιοι or nothing at all."})
    # Personal pronouns: strong and weak (declensions.json personal_pronouns).
    pers = {"id": "pers", "l": "εγώ, εσύ, αυτός …", "en": "personal pronouns", "lv": "A1", "kind": "pers",
            "rows": [["εγώ", "εμένα", "μου", "εμένα", "με"], ["εσύ", "εσένα", "σου", "εσένα", "σε"],
                     ["αυτός", "αυτού", "του", "αυτόν", "τον"], ["αυτή", "αυτής", "της", "αυτή|αυτήν", "τη|την"], ["αυτό", "αυτού", "του", "αυτό", "το"],
                     ["εμείς", "εμάς", "μας", "εμάς", "μας"], ["εσείς", "εσάς", "σας", "εσάς", "σας"],
                     ["αυτοί", "αυτών", "τους", "αυτούς", "τους"], ["αυτές", "αυτών", "τους", "αυτές", "τις|τες"], ["αυτά", "αυτών", "τους", "αυτά", "τα"]],
            "note": "Weak forms (μου, σε, τον …) sit right before the verb, or after an imperative or gerund; strong forms (εμένα, εσένα …) are for emphasis and after prepositions (για μένα)."}
    tables.append(pers)
    for word, en, lv, note in [
        ("αυτός", "this; he, she, it", "A1", "αυτός declines like καλός (-ος, -η, -ο); the accusative αυτόν keeps its -ν."),
        ("εκείνος", "that; that one", "A1", "εκείνος declines like αυτός; masculine accusative εκείνον (εκείνο before a consonant is common too)."),
        ("ποιος", "who; which", "A1", "ποιος, ποια, ποιο; the genitive has long forms (ποιανού, ποιανής, ποιανών) alongside learned ποιου, ποιας, ποιων."),
        ("κάποιος", "someone; some", "A2", "κάποιος declines like ποιος: κάποιου/κάποιανού, κάποιας, κάποιων."),
        ("όλος", "all, whole", "A1", "όλος, όλη, όλο takes the article after it: όλοι οι φίλοι, όλη τη μέρα."),
        ("τέτοιος", "such", "A2", "τέτοιος, τέτοια, τέτοιο declines like ωραίος (feminine in -α)."),
        ("τόσος", "so much, so many", "A2", "τόσος, τόση, τόσο declines like καλός."),
        ("πόσος", "how much, how many", "A1", "πόσος, πόση, πόσο declines like καλός: πόσοι, πόσες, πόσα."),
        ("ίδιος", "same; -self", "A2", "ίδιος, ίδια, ίδιο: ο ίδιος = the same one, or 'himself' (ο ίδιος το είπε)."),
        ("άλλος", "other", "A1", "άλλος, άλλη, άλλο declines like καλός."),
        ("οποίος", "who, which (relative, with article)", "B1", "ο οποίος, η οποία, το οποίο always takes the article and agrees with the noun it refers to (της οποίας, των οποίων)."),
        ("κανένας", "no, none; anyone", "A2", "κανένας/κανείς, καμία/καμιά, κανένα: singular only, declines like ένας."),
        ("καθένας", "each one, everyone", "B1", "καθένας, καθεμία/καθεμιά, καθένα: singular only, declines like ένας."),
        ("δικός", "own (δικός μου = mine)", "A2", "δικός, δική, δικό + weak possessive: δικός μου, δική σου, των δικών μας."),
    ]:
        cells = adj_like(word) or HAND.get(word)
        if not cells:
            report["pron_missing"].append(word); continue
        sg_only = word in ("κανένας", "καθένας")
        parts = cells[6].split("|")  # masculine accusative: the -ν form is the standard written one (κάποιον)
        if len(parts) > 1 and not parts[0].endswith("ν") and any(x.endswith("ν") for x in parts):
            cells[6] = "|".join(sorted(parts, key=lambda x: not x.endswith("ν")))
        if sg_only: cells = cells[:9]
        tables.append({"id": "pr-" + word, "l": word, "en": en, "lv": lv, "kind": "g3sg" if sg_only else "g3", "f": cells, "note": note})
    report["pronoun_tables"] = len(tables)
    return tables

# ---------------- noun phrases from the collocation list ----------------
def build_phrases(lex, nouns, adjs, report):
    col = json.load(open(os.path.join(ROOT, "data", "lexicon", "collocations.json")))["entries"]
    N = {x["l"]: x for x in nouns}; A = {x["l"]: x for x in adjs}
    out, seen = [], set()
    for lemma, ent in col.items():
        for c in ent.get("collocations", []):
            toks = nfc(c["el"]).split()
            if len(toks) != 2: continue
            a, n = toks
            if a in A and n in N and (a, n) not in seen:
                noun = N[n]; adj = A[a]
                if noun["g"] == "c": continue
                gi = "mfn".index(noun["g"])
                if adj["f"][gi].split("|")[0] != a: continue  # adjective must agree with the noun's gender as given
                seen.add((a, n))
                out.append({"a": a, "n": n, "en": c["en"], "lv": max(adj["lv"], noun["lv"], key=lambda x: LV.index(x) if x in LV else 9)})
    report["phrases"] = len(out)
    return out

# ---------------- context sentences from the word list's examples ----------------
def build_cloze(lex, nouns, adjs, verbs, report):
    form2 = collections.defaultdict(list)  # form -> [(kind, lemma, cellcode)]
    for x in nouns:
        for i, c in enumerate(x["f"]):
            for j, f in enumerate(c.split("|") if c else []):
                form2[f].append(("n", x["l"], i, j == 0))
    for x in adjs:
        for i, c in enumerate(x["f"]):
            for j, f in enumerate(c.split("|") if c else []):
                form2[f].append(("a", x["l"], i, j == 0))
    for x in verbs:
        for voice in ("A", "P"):
            if voice not in x: continue
            for t in ("pres", "impf", "aor", "dep"):
                for i, c in enumerate(x[voice][t]):
                    for j, f in enumerate(c.split("|") if c else []):
                        form2[f].append(("v", x["l"], voice + "." + t + "." + str(i), j == 0))
    out, seen = [], set()
    TOK = re.compile(r"[\wάέήίόύώϊϋΐΰΆΈΉΊΌΎΏ]+")
    for e in lex:
        ex = e.get("example") or {}
        s, en = nfc(ex.get("el") or ""), (ex.get("en") or "").strip()
        if not s or not en or s in seen: continue
        best = None
        for m in TOK.finditer(s):
            tok = m.group(0)
            low = tok.lower()
            if tok != low and m.start() == 0: pass
            elif tok != low: continue  # skip names
            hits = form2.get(low, [])
            if not hits: continue
            lemmas = {(h[0], h[1]) for h in hits}
            if len(lemmas) != 1: continue  # ambiguous between two words
            k, l = hits[0][0], hits[0][1]
            if low == l: continue
            if set(FI.get(low, [l])) != {l}: continue  # the forms index knows another word with this form (άσε: αφήνω, not άσος)  # the dictionary form itself teaches nothing here
            mains = [h for h in hits if h[3]]
            cells = sorted({h[2] for h in (mains or hits)}, key=str)
            if k == "v" and any(not str(c).split(".")[1] in ("pres", "impf", "aor", "dep") for c in cells): continue
            score = (2 if l == e["lemma"] else 1, len(low))
            if not best or score > best[0]: best = (score, m.start(), m.end(), tok, k, l, cells)
        if not best: continue
        _, a, b, tok, k, l, cells = best
        seen.add(s)
        out.append({"s": s[:a] + "___" + s[b:], "en": en, "k": k, "l": l, "c": cells, "a": tok, "lv": e.get("cefr_est") or "B2"})
    report["cloze"] = len(out)
    return out

HUN = set()

def load_hunspell():
    """LibreOffice el_GR word list (https://github.com/LibreOffice/dictionaries/tree/master/el_GR), path in EL_DIC.
    Used as a third check per cell: a main form it does not know gives way to an alternative it knows,
    and vocatives and imperatives it does not know are dropped (ώμε, οδήγα)."""
    path = os.environ.get("EL_DIC")
    if not path or not os.path.exists(path): print("EL_DIC not set: skipping the hunspell pass"); return
    with open(path, encoding="iso-8859-7") as fh:
        next(fh)
        for line in fh: HUN.add(line.strip().split("/")[0].lower())

def hun_cell(cell, drop_unknown, report, key):
    if not HUN or not cell: return cell
    forms = cell.split("|")
    known = [f for f in forms if all(t in HUN for t in f.split() if t != "θα")]
    if known and forms[0] not in known:
        report["hun_promoted"] += 1
        return "|".join([known[0]] + [f for f in forms if f != known[0]])
    if not known and drop_unknown:
        report["hun_dropped_" + key] += 1
        return ""
    if not known: report["hun_unknown_kept"] += 1
    return cell

def hun_pass(nouns, adjs, verbs, report):
    for w in nouns:
        w["f"] = [hun_cell(c, (i & 3) == 3, report, "voc") for i, c in enumerate(w["f"])]
    for w in adjs:
        w["f"] = [hun_cell(c, (i // 3) % 4 == 3, report, "voc") for i, c in enumerate(w["f"])]
    for w in verbs:
        for v in ("A", "P"):
            if v not in w: continue
            for t in ("pres", "impf", "aor", "dep", "impP", "impI"):
                w[v][t] = [hun_cell(c, t.startswith("imp"), report, "imp") for c in w[v][t]]

def main():
    report = collections.Counter(); report.update({})
    for k in ("noun_mismatch_examples", "adj_mismatch_examples", "verb_mismatch_examples", "pron_missing", "rverb_aorist_examples", "rverb_thin_examples", "rverb_present_examples", "mverb_dropped"): report[k] = []
    lex, wk = load_lex(), load_wikt()
    fi = json.load(open(os.path.join(ROOT, "data", "lexicon", "forms-index.json")))["forms"]
    FI.update(fi)
    for form, lemmas in fi.items():
        for l in lemmas: INV.setdefault(l, set()).add(form)
    nouns = build_nouns(lex, wk, report)
    adjs = build_adjs(lex, wk, report)
    verbs = build_verbs(lex, wk, report)
    verbs += build_manual_verbs(lex, {w["l"] for w in verbs}, report)  # hand-written tables win over rule-built ones
    verbs += build_rule_verbs(lex, {w["l"] for w in verbs}, report)
    # Wiktionary entries come and go between kaikki.org dumps; a paradigm that passed the gate in an earlier build is kept
    # while its word is still in the word list with the same part of speech and principal parts.
    lexpos = {(e["lemma"], e["pos"]): e for e in lex}
    for name, lst, pos in (("nouns.json", nouns, "noun"), ("adjectives.json", adjs, "adjective"), ("verbs.json", verbs, "verb")):
        prev_path = os.path.join(OUT, name)
        if not os.path.exists(prev_path): continue
        have = {w["l"] for w in lst}
        for w in json.load(open(prev_path))["words"]:
            e = lexpos.get((w["l"], pos))
            if w["l"] in have or not e: continue
            if pos == "verb":
                a1 = (e.get("verb") or {}).get("aorist_1sg")
                if a1 and not w["A"].get("one_past") and a1 not in (w["A"]["aor"][0] or "").split("|"): continue
            w["r"] = e.get("freq_rank") or w.get("r"); lst.append(w); report["kept_from_previous_" + pos] += 1
    verbs.sort(key=lambda x: (LV.index(x["lv"]) if x["lv"] in LV else 9, x["r"]))
    if not HUN: load_hunspell()
    hun_pass(nouns, adjs, verbs, report)
    prons = build_pronouns(wk, report)
    phrases = build_phrases(lex, nouns, adjs, report)
    cloze = build_cloze(lex, nouns, adjs, verbs, report)
    os.makedirs(OUT, exist_ok=True)
    def dump(name, obj):
        with open(os.path.join(OUT, name), "w") as fh: json.dump(obj, fh, ensure_ascii=False, separators=(",", ":"))
    src = "Paradigms: Wiktionary inflection tables (via kaikki.org, CC BY-SA 4.0), kept only where they agree with the app's word list."
    dump("nouns.json", {"source": src, "notes": NOUN_NOTES, "words": nouns})
    dump("adjectives.json", {"source": src, "notes": ADJ_NOTES, "words": adjs})
    dump("verbs.json", {"source": src + " Verbs marked src=manual are written out by hand after Holton and Triantafyllidis, each form confirmed by the forms index or the el_GR word list. Verbs marked src=rule (no usable Wiktionary table) are built from the conjugation classes in data/grammar and kept only where every form is also in the word list's forms index.", "words": verbs})
    dump("pronouns.json", {"source": src + " Article and pronoun tables after data/grammar/declensions.json.", "tables": prons, "phrases": phrases})
    dump("context.json", {"source": "Sentences: the word list's example sentences (data/lexicon).", "items": cloze})
    for k, v in sorted(report.items()):
        if isinstance(v, list): print(k, len(v), v[:25])
        else: print(k, v)

if __name__ == "__main__":
    main()
