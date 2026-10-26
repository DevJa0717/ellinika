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
    g = set(x for x in gen if x)
    if None in gen or not g: return False
    extra = idx_forms - g
    return g <= idx_forms and all(x.endswith("ν") and x[:-1] in g for x in extra)

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
        if not w and not cands and not pl_only:
            g = gen_noun(lemma, model)
            if g and (not n.get("gen_sg") or g[1] == n["gen_sg"]) and forms_agree(g, INV.get(lemma, set())):
                if model.startswith("m-ος") and g[3] not in INV.get(lemma, set()): g[3] = ""
                out.append({"l": lemma, "g": gender, "m": model, "lv": e.get("cefr_est") or "B2", "en": short_gloss(e["gloss"]),
                            "r": e.get("freq_rank") or 99999, "f": g, "src": "rule"})
                report["nouns"] += 1; report["nouns_rule"] += 1
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
        if not w and not cands:
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
    for k in ("noun_mismatch_examples", "adj_mismatch_examples", "verb_mismatch_examples", "pron_missing"): report[k] = []
    lex, wk = load_lex(), load_wikt()
    fi = json.load(open(os.path.join(ROOT, "data", "lexicon", "forms-index.json")))["forms"]
    FI.update(fi)
    for form, lemmas in fi.items():
        for l in lemmas: INV.setdefault(l, set()).add(form)
    nouns = build_nouns(lex, wk, report)
    adjs = build_adjs(lex, wk, report)
    verbs = build_verbs(lex, wk, report)
    load_hunspell(); hun_pass(nouns, adjs, verbs, report)
    prons = build_pronouns(wk, report)
    phrases = build_phrases(lex, nouns, adjs, report)
    cloze = build_cloze(lex, nouns, adjs, verbs, report)
    os.makedirs(OUT, exist_ok=True)
    def dump(name, obj):
        with open(os.path.join(OUT, name), "w") as fh: json.dump(obj, fh, ensure_ascii=False, separators=(",", ":"))
    src = "Paradigms: Wiktionary inflection tables (via kaikki.org, CC BY-SA 4.0), kept only where they agree with the app's word list."
    dump("nouns.json", {"source": src, "notes": NOUN_NOTES, "words": nouns})
    dump("adjectives.json", {"source": src, "notes": ADJ_NOTES, "words": adjs})
    dump("verbs.json", {"source": src, "words": verbs})
    dump("pronouns.json", {"source": src + " Article and pronoun tables after data/grammar/declensions.json.", "tables": prons, "phrases": phrases})
    dump("context.json", {"source": "Sentences: the word list's example sentences (data/lexicon).", "items": cloze})
    for k, v in sorted(report.items()):
        if isinstance(v, list): print(k, len(v), v[:25])
        else: print(k, v)

if __name__ == "__main__":
    main()
