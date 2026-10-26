#!/usr/bin/env python3
"""Printable drill books built from the app's drill data (library/drills/*.json, made by tools/drills/build.py):
  Κλίση ονομάτων  (articles, pronouns, nouns, adjectives, noun phrases, forms in context)
  Συζυγία ρημάτων (verbs: principal parts, conjugation grids, single forms, forms in context)
Every exercise is numbered; the answer key is at the back of each book. Selection is seeded, so a rebuild is stable.

Usage: python3 deploy/textbook/build_drills.py --out <dir>      writes "<dir>/Declension drills.html" and "<dir>/Conjugation drills.html"
Then:  node deploy/textbook/render_drills.js <dir> downloads/textbook
       python3 deploy/textbook/compress.py <pdf> <pdf> "<title>"   (render_drills.js runs it for you)
"""
import html, json, os, random, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from covers_el import el_date

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(ROOT, "library", "drills")
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(ROOT, "deploy", "textbook", "build")
CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "textbook.css"), encoding="utf-8").read()
EXTRA = """
.dr-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 4mm 5mm; margin: 3mm 0 5mm; }
.dr-grid.two { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.dr-grid table { table-layout: fixed; } .dr-grid td { overflow-wrap: anywhere; } .dr-grid th:first-child { width: 11mm; }
.dr-grid table, .dr-model table { width: 100%; border-collapse: collapse; font-size: 8.6pt; break-inside: avoid; }
.dr-grid caption { text-align: left; font-weight: 700; font-size: 9pt; padding: 0 0 1mm; }
.dr-grid caption small { font-weight: 400; color: #5b6478; }
.dr-grid td, .dr-grid th, .dr-model td, .dr-model th { border: 0.6pt solid #c9d1de; padding: 1.2mm 1.4mm; height: 5mm; }
.dr-grid th, .dr-model th { background: #eef3fa; font-size: 7.4pt; font-weight: 700; text-align: left; }
.dr-grid td.given { color: #1d4e89; font-weight: 700; }
.dr-model { margin: 2mm 0 4mm; break-inside: avoid; }
.dr-model table { max-width: 120mm; }
.dr-note { border-left: 3px solid #b8892b; background: #fbf6ea; padding: 2mm 3mm; margin: 2mm 0 4mm; font-size: 9pt; break-inside: avoid; }
.dr-items { columns: 2; column-gap: 8mm; margin: 2mm 0 5mm; padding-left: 7mm; font-size: 9.3pt; }
.dr-items li { break-inside: avoid; margin: 0 0 1.6mm; }
.dr-items .cue { color: #5b6478; font-size: 8.2pt; }
.dr-items .blank { width: 30mm; } .dr-items .blank, .dr-cloze .blank { display: inline-block; width: 24mm; height: auto; vertical-align: baseline; border-bottom: 0.7pt solid #8a94a6; }
.dr-cloze { padding-left: 7mm; font-size: 9.5pt; }
.dr-cloze li { break-inside: avoid; margin: 0 0 2.2mm; }
.dr-cloze .cue { color: #5b6478; font-size: 8.2pt; }
.dr-pp { width: 100%; border-collapse: collapse; font-size: 9pt; margin: 2mm 0 5mm; }
.dr-pp td, .dr-pp th { border: 0.6pt solid #c9d1de; padding: 1.3mm 1.6mm; height: 5.2mm; }
.dr-pp th { background: #eef3fa; font-size: 7.6pt; text-align: left; }
.dr-pp td.given { color: #1d4e89; font-weight: 700; }
h3.ex { font-size: 10.5pt; margin: 5mm 0 1mm; color: #1d4e89; break-after: avoid; }
h3.ex + p.inst { margin-top: 0; font-size: 9pt; color: #5b6478; break-after: avoid; }
.key { columns: 2; column-gap: 8mm; font-size: 8.4pt; }
.key h4 { font-size: 9pt; margin: 3mm 0 1mm; break-after: avoid; color: #1d4e89; }
.key p { margin: 0 0 1mm; }
.key table { width: 100%; border-collapse: collapse; font-size: 7.8pt; margin: 0 0 2mm; break-inside: avoid; }
.key td { border: 0.4pt solid #d6dce6; padding: 0.6mm 1mm; }
"""

def esc(s): return html.escape("" if s is None else str(s), quote=True)
def first(c): return (c or "").split("|")[0]
def alts(c): return " / ".join(x for x in (c or "").split("|") if x)
def J(n): return json.load(open(os.path.join(D, n + ".json"), encoding="utf-8"))

CASES = [("nom", "Nom."), ("gen", "Gen."), ("acc", "Acc."), ("voc", "Voc.")]
CASE_EN = ["nominative", "genitive", "accusative", "vocative"]
CASE_SHORT = ["nom.", "gen.", "acc.", "voc."]
ART = {"m": [["ο", "του", "τον"], ["οι", "των", "τους"]], "f": [["η", "της", "τη|την"], ["οι", "των", "τις"]], "n": [["το", "του", "το"], ["τα", "των", "τα"]]}
LV = ["A1", "A2", "B1", "B2", "C1", "C2"]

def tin(nxt): return "την" if re.match(r"[αεηιουωάέήίόύώκπτξψ]", nxt or "") else "τη"
def art(g, num, ci, nxt=""):
    if ci == 3: return ""
    a = ART["m" if g == "c" else g][num][ci]
    return tin(nxt) if a == "τη|την" else a

class Book:
    def __init__(self):
        self.body, self.toc, self.key, self.n = [], [], [], 0
    def part(self, pid, title, el, intro=""):
        self.toc.append(f'<li class="toc-p"><a href="#{pid}">{esc(title)}</a> <span lang="el">· {esc(el)}</span><ol>')
        self.body.append(f'<section class="part" id="{pid}"><div class="part-h"><div class="pn">{esc(title)}</div><h1 lang="el">{esc(el)}</h1></div>{intro}')
        self.key.append(f'<h4>{esc(title)}</h4>')
    def end_part(self):
        self.toc.append("</ol></li>"); self.body.append("</section>")
    def sec(self, sid, title, el):
        self.toc.append(f'<li><a href="#{sid}">{esc(title)}</a></li>')
        self.body.append(f'<section class="lesson" id="{sid}"><h2 class="unit"><span lang="el">{esc(el)}</span> <span class="lt-en">· {esc(title)}</span></h2>')
    def end_sec(self): self.body.append("</section>")
    def ex(self, title, inst):
        self.n += 1
        self.body.append(f'<h3 class="ex">Exercise {self.n} · {esc(title)}</h3><p class="inst">{esc(inst)}</p>')
        return self.n

def items_list(book, n, rows):
    """rows: [(prompt_html, answer_text)] -> numbered two-column list; answers to the key."""
    book.body.append('<ol class="dr-items">' + "".join(f'<li>{p} <span class="blank">&nbsp;</span></li>' for p, _ in rows) + "</ol>")
    book.key.append(f'<p><b>{n}.</b> ' + "; ".join(f"{i}) <span lang=\"el\">{esc(a)}</span>" for i, (_, a) in enumerate(rows, 1)) + "</p>")

def cloze_list(book, n, rows):
    book.body.append('<ol class="dr-cloze">' + "".join(f'<li lang="el">{p}</li>' for p, _ in rows) + "</ol>")
    book.key.append(f'<p><b>{n}.</b> ' + "; ".join(f"{i}) <span lang=\"el\">{esc(a)}</span>" for i, (_, a) in enumerate(rows, 1)) + "</p>")

# ------------------------------------------------------------------ declension book
NOUN_TYPES = [
    ("m-ος", "Masculine nouns in -ος", "Αρσενικά σε -ος", lambda m: m.startswith("m-ος")),
    ("m-ας", "Masculine nouns in -ας", "Αρσενικά σε -ας", lambda m: m.startswith("m-ας")),
    ("m-ης", "Masculine nouns in -ης / -ής", "Αρσενικά σε -ης", lambda m: m == "m-ης"),
    ("m-εας", "Masculine nouns in -έας", "Αρσενικά σε -έας", lambda m: m == "m-έας"),
    ("m-imp", "Masculine nouns with plural -δες", "Ανισοσύλλαβα αρσενικά", lambda m: m.startswith("m-imparisyllabic")),
    ("f-α", "Feminine nouns in -α", "Θηλυκά σε -α", lambda m: m.startswith("f-α")),
    ("f-η-ες", "Feminine nouns in -η, plural -ες", "Θηλυκά σε -η (-ες)", lambda m: m == "f-η-ες"),
    ("f-η-εις", "Feminine nouns in -η, plural -εις", "Θηλυκά σε -η (-εις)", lambda m: m == "f-η-εις"),
    ("f-ος", "Feminine nouns in -ος and -ού/-ά", "Θηλυκά σε -ος, -ού, -ά", lambda m: m in ("f-ος", "f-imparisyllabic-ά", "f-imparisyllabic-ού")),
    ("n-ο", "Neuter nouns in -ο", "Ουδέτερα σε -ο", lambda m: m.startswith("n-ο-")),
    ("n-ι", "Neuter nouns in -ι", "Ουδέτερα σε -ι", lambda m: m in ("n-ι", "n-ί")),
    ("n-μα", "Neuter nouns in -μα and -ιμο", "Ουδέτερα σε -μα", lambda m: m in ("n-μα", "n-ιμο")),
    ("n-ος", "Neuter nouns in -ος, -ον, -ας, -ως", "Ουδέτερα σε -ος και άλλα", lambda m: m.startswith("n-ος") or m in ("n-ον", "n-ας", "n-ως")),
]

def noun_table(w, blank, given=(0,)):
    rows = []
    for ci, (_, lab) in enumerate(CASES):
        cells = []
        for num in (0, 1):
            i = num * 4 + ci
            f = w["f"][i]
            if not f: cells.append("<td>—</td>"); continue
            text = (art(w["g"], num, ci, first(f)) + " " if ci < 3 else "") + first(f)
            if blank and i not in given: text = (art(w["g"], num, ci, first(f)) if ci < 3 else "")
            cells.append(f'<td lang="el"{" class=given" if blank and i in given else ""}>{esc(text)}</td>')
        rows.append(f"<tr><th>{lab}</th>{''.join(cells)}</tr>")
    return f'<table><caption lang="el">{esc(w["l"])} <small>{esc(w["en"])}</small></caption><tr><th></th><th>sg.</th><th>pl.</th></tr>{"".join(rows)}</table>'

def decl_book():
    rnd = random.Random(2610)
    N, A, P, C = J("nouns"), J("adjectives"), J("pronouns"), J("context")
    b = Book()
    # Part 1: articles and pronouns
    b.part("p-pron", "Part 1 · Articles and pronouns", "Άρθρα και αντωνυμίες",
           "<p>The article carries most of the case information in Greek, so it comes first. Fill each table, then the single forms.</p>")
    b.sec("p-pron-t", "Tables", "Πίνακες")
    n = b.ex("Complete the tables", "The nominative is given; write the other forms. Where two forms exist, either is right (τη/την: see the final -ν rule in the key).")
    grids, keyrows = [], []
    for t in P["tables"]:
        if t["kind"] == "pers":
            rows = "".join("<tr>" + f'<td class="given" lang="el">{esc(r[0])}</td>' + "<td></td>" * 4 + "</tr>" for r in t["rows"])
            grids.append(f'<table><caption lang="el">{esc(t["l"])} <small>{esc(t["en"])}</small></caption><tr><th>nom.</th><th>gen.</th><th>gen. weak</th><th>acc.</th><th>acc. weak</th></tr>{rows}</table>')
            keyrows.append(f'<table><tr><td colspan=5 lang="el"><b>{esc(t["l"])}</b></td></tr>' + "".join("<tr>" + "".join(f'<td lang="el">{esc(alts(c))}</td>' for c in r) + "</tr>" for r in t["rows"]) + "</table>")
            continue
        nums = 1 if t["kind"] == "g3sg" else 2
        rows = []
        for num in range(nums):
            for ci in range(3):
                cells = []
                for g in range(3):
                    i = num * 9 + ci * 3 + g
                    cells.append(f'<td class="given" lang="el">{esc(first(t["f"][i]))}</td>' if (num == 0 and ci == 0) else "<td></td>")
                rows.append(f"<tr><th>{['sg.', 'pl.'][num]} {CASE_SHORT[ci]}</th>{''.join(cells)}</tr>")
        grids.append(f'<table><caption lang="el">{esc(t["l"])} <small>{esc(t["en"])}</small></caption><tr><th></th><th>m.</th><th>f.</th><th>n.</th></tr>{"".join(rows)}</table>')
        keyrows.append(f'<table><tr><td colspan=4 lang="el"><b>{esc(t["l"])}</b></td></tr>' + "".join(
            f"<tr><td>{['sg.', 'pl.'][num]} {CASE_SHORT[ci]}</td>" + "".join(f'<td lang="el">{esc(alts(t["f"][num * 9 + ci * 3 + g]))}</td>' for g in range(3)) + "</tr>"
            for num in range(nums) for ci in range(3)) + "</table>")
    b.body.append('<div class="dr-grid two">' + "".join(grids) + "</div>")
    b.key.append(f"<p><b>{n}.</b></p>" + "".join(keyrows))
    b.end_sec()
    b.sec("p-pron-i", "Single forms", "Μεμονωμένοι τύποι")
    n = b.ex("Give the form", "Write the form asked for.")
    rows = []
    GN = ["masc.", "fem.", "neut."]
    for t in P["tables"]:
        if t["kind"] == "pers":
            for ri, r in enumerate(t["rows"]):
                for ci, lab in [(2, "gen. weak"), (4, "acc. weak"), (3, "acc. strong")]:
                    rows.append((f'<span lang="el">{esc(r[0])}</span> <span class="cue">→ {lab}</span>', alts(r[ci])))
            continue
        cells = [i for i, c in enumerate(t["f"]) if c and i]
        for i in rnd.sample(cells, min(6, len(cells))):
            num, ci, g = i // 9, (i // 3) % 3, i % 3
            rows.append((f'<span lang="el">{esc(t["l"])}</span> <span class="cue">→ {GN[g]} {CASE_SHORT[ci]} {["sg.", "pl."][num]}</span>', alts(t["f"][i])))
    items_list(b, n, rows)
    b.end_sec(); b.end_part()

    # Part 2: nouns by type
    b.part("p-nouns", "Part 2 · Nouns by declension type", "Ουσιαστικά",
           "<p>Each section opens with a model table and the rule, then a set of tables to complete (nominative singular given, article printed) and single forms to write with their article. Words run from the most frequent A1 words to B2 and C1.</p>")
    for tid, en, el, test in NOUN_TYPES:
        ws = [w for w in N["words"] if test(w["m"]) and w["f"][0]]
        if not ws: continue
        b.sec("n-" + tid, en, el)
        model = ws[0]
        b.body.append(f'<div class="dr-model">{noun_table(model, False)}</div>')
        notes = {N["notes"].get(w["m"]) for w in ws if N["notes"].get(w["m"])}
        for note in sorted(notes, key=lambda x: len(x))[:3]: b.body.append(f'<div class="dr-note" lang="el">{esc(note)}</div>')
        pool = ws[1:]
        grid_ws = pool[:min(len(pool), 24)] if len(pool) <= 36 else pool[:12] + rnd.sample(pool[12:], 12)
        n = b.ex("Complete the tables", "Write each form after its article. The vocative has no article.")
        b.body.append('<div class="dr-grid">' + "".join(noun_table(w, True) for w in grid_ws) + "</div>")
        b.key.append(f"<p><b>{n}.</b> " + "; ".join(
            f'<span lang="el"><b>{esc(w["l"])}</b>: ' + ", ".join(esc(first(w["f"][i])) for i in range(1, 8) if w["f"][i]) + "</span>" for w in grid_ws) + "</p>")
        rest = [w for w in pool if w not in grid_ws] or pool
        rows = []
        for w in rnd.sample(rest, min(len(rest), 60)):
            cells = [i for i in range(1, 8) if w["f"][i] and not (i & 3 == 3 and (i > 4 or w["g"] not in ("m", "c")))]
            if not cells: continue
            i = rnd.choice(cells); num, ci = i >> 2, i & 3
            a0 = "ο/η" if w["g"] == "c" else ART[w["g"]][0][0]
            ans = (art(w["g"], num, ci, first(w["f"][i])) + " " if ci < 3 else "") + first(w["f"][i])
            rows.append((f'<span lang="el">{a0} {esc(w["l"])}</span> <span class="cue">→ {CASE_SHORT[ci]} {["sg.", "pl."][num]}</span>', ans))
        if rows:
            n = b.ex("With the article", "Write the form with its article.")
            items_list(b, n, rows)
        b.end_sec()
    b.end_part()

    # Part 3: adjectives
    b.part("p-adj", "Part 3 · Adjectives", "Επίθετα", "<p>Adjectives agree with their noun in gender, number and case. The genitive plural is the same in all three genders.</p>")
    AMODELS = [("adj-ος-η-ο", "-ος, -η, -ο", "καλός, καλή, καλό"), ("adj-ος-α-ο", "-ος, -α, -ο", "ωραίος, ωραία, ωραίο"), ("adj-ύς-ιά-ύ", "-ύς, -ιά, -ύ", "βαθύς, βαθιά, βαθύ"),
               ("adj-ής-ές-fixed", "-ής, -ής, -ές", "ακριβής, ακριβές"), ("adj-ης-ες-shift", "-ης, -ης, -ες", "πλήρης, πλήρες"), ("adj-ων-ουσα-ον", "-ων, -ουσα, -ον", "ενδιαφέρων"),
               ("adj-ης-α-ικο", "-ης, -α, -ικο", "τεμπέλης"), ("adj-ής-ιά-ί", "-ής, -ιά, -ί", "πορτοκαλής"), ("adj-άς-ού-άδικο", "-άς, -ού, -άδικο", "φαγάς")]
    for mid, ending, eg in AMODELS:
        ws = [w for w in A["words"] if w["m"] == mid]
        if not ws: continue
        b.sec("a-" + mid, f"Adjectives in {ending}", f"Επίθετα σε {ending}")
        def adj_table(w, blank):
            rows = []
            for num in (0, 1):
                for ci in range(3):
                    cells = []
                    for g in range(3):
                        i = num * 12 + ci * 3 + g
                        if blank and not (num == 0 and ci == 0): cells.append("<td></td>")
                        else: cells.append(f'<td lang="el"{" class=given" if blank else ""}>{esc(first(w["f"][i]))}</td>')
                    rows.append(f"<tr><th>{['sg.', 'pl.'][num]} {CASE_SHORT[ci]}</th>{''.join(cells)}</tr>")
            return f'<table><caption lang="el">{esc(w["l"])} <small>{esc(w["en"])}</small></caption><tr><th></th><th>m.</th><th>f.</th><th>n.</th></tr>{"".join(rows)}</table>'
        b.body.append(f'<div class="dr-model">{adj_table(ws[0], False)}</div>')
        if A["notes"].get(mid): b.body.append(f'<div class="dr-note" lang="el">{esc(A["notes"][mid])}</div>')
        pool = ws[1:]
        gw = pool[:min(len(pool), 9)] if len(pool) <= 20 else pool[:6] + rnd.sample(pool[6:], 12 if mid == "adj-ος-η-ο" else 6)
        if gw:
            n = b.ex("Complete the tables", "The nominative singular is given in all three genders.")
            b.body.append('<div class="dr-grid two">' + "".join(adj_table(w, True) for w in gw) + "</div>")
            b.key.append(f"<p><b>{n}.</b> " + "; ".join(
                f'<span lang="el"><b>{esc(w["l"])}</b>: ' + ", ".join(esc(first(w["f"][num * 12 + ci * 3 + g])) for num in (0, 1) for ci in range(3) for g in range(3) if not (num == 0 and ci == 0)) + "</span>" for w in gw) + "</p>")
        rest = [w for w in pool if w not in gw]
        if rest:
            rows = []
            for w in rnd.sample(rest, min(len(rest), 80 if mid == "adj-ος-η-ο" else 30)):
                cells = [i for i in range(24) if w["f"][i] and (i // 3) % 4 != 3 and i not in (0,)]
                i = rnd.choice(cells); num, ci, g = i // 12, (i // 3) % 4, i % 3
                a = art("mfn"[g], num, ci, first(w["f"][i]))
                rows.append((f'<span lang="el">{a} <span class="blank">&nbsp;</span></span> <span class="cue">({esc(w["l"])}, {["m.", "f.", "n."][g]} {CASE_SHORT[ci]} {["sg.", "pl."][num]})</span>', first(w["f"][i])))
            n = b.ex("After the article", "Write the adjective in the form the article needs.")
            b.body.append('<ol class="dr-items">' + "".join(f"<li>{p}</li>" for p, _ in rows) + "</ol>")
            b.key.append(f'<p><b>{n}.</b> ' + "; ".join(f"{i}) <span lang=\"el\">{esc(a)}</span>" for i, (_, a) in enumerate(rows, 1)) + "</p>")
        b.end_sec()
    b.end_part()

    # Part 4: noun phrases
    NW = {w["l"]: w for w in N["words"]}; AW = {w["l"]: w for w in A["words"]}
    b.part("p-phr", "Part 4 · Whole noun phrases", "Άρθρο, επίθετο, ουσιαστικό", "<p>Article, adjective and noun must all change together. The phrases are common collocations from the word list.</p>")
    b.sec("p-phr-1", "Decline the phrase", "Κλίνε τη φράση")
    phr = sorted(P["phrases"], key=lambda p: (LV.index(p["lv"]) if p["lv"] in LV else 9))
    rows = []
    for p in phr:
        no, ad = NW.get(p["n"]), AW.get(p["a"])
        if not no or not ad or no["g"] == "c": continue
        gi = "mfn".index(no["g"])
        cells = [i for i in range(1, 8) if i & 3 != 3 and no["f"][i] and ad["f"][(i >> 2) * 12 + (i & 3) * 3 + gi]]
        if not cells: continue
        i = rnd.choice(cells); num, ci = i >> 2, i & 3
        af = first(ad["f"][num * 12 + ci * 3 + gi])
        rows.append((f'<span lang="el">{ART[no["g"]][0][0]} {esc(p["a"])} {esc(p["n"])}</span> <span class="cue">({esc(p["en"])}) → {CASE_SHORT[ci]} {["sg.", "pl."][num]}</span>',
                     f'{art(no["g"], num, ci, af)} {af} {first(no["f"][i])}'))
    n = b.ex("Put the phrase in the case and number asked", "Write article, adjective and noun.")
    items_list(b, n, rows)
    b.end_sec(); b.end_part()

    # Part 5: in context (nouns and adjectives)
    b.part("p-ctx", "Part 5 · Forms in context", "Μέσα στη φράση", "<p>Real example sentences from the word list. Write the word in brackets in the form the sentence needs.</p>")
    for k, en, el in [("n", "Nouns", "Ουσιαστικά"), ("a", "Adjectives", "Επίθετα")]:
        its = [x for x in C["items"] if x["k"] == k]
        its = sorted(rnd.sample(its, min(len(its), 450)), key=lambda x: (LV.index(x["lv"]) if x["lv"] in LV else 9))
        b.sec("ctx-" + k, en, el)
        for lv in LV[:5]:
            sub = [x for x in its if x["lv"] == lv or (lv == "C1" and x["lv"] == "C2")]
            if not sub: continue
            n = b.ex(f"{en}, level {lv}", "Fill each gap with the right form of the word in brackets.")
            cloze_list(b, n, [(esc(x["s"]).replace("___", '<span class="blank">&nbsp;</span>') + f' <span class="cue">({esc(x["l"])})</span>', x["a"]) for x in sub])
        b.end_sec()
    b.end_part()
    total = count_blanks(b)
    tot_el = f"{total:,}".replace(",", ".")
    cover = ('<section class="cover" lang="el"><div class="c-top">Ελληνικά · Τετράδιο ασκήσεων</div><div class="c-lvl" style="font-size:72pt">Κλίση ονομάτων</div>'
             '<div class="c-name">Άρθρα, αντωνυμίες, ουσιαστικά, επίθετα</div>'
             f'<p class="c-blurb">{b.n} ασκήσεις με περίπου {tot_el} κενά προς συμπλήρωση, σε πραγματικές λέξεις του λεξιλογίου της εφαρμογής: ' +
             'πίνακες κλίσης ανά τύπο, μεμονωμένοι τύποι, ολόκληρες ονοματικές φράσεις και προτάσεις με κενά. Οι λύσεις βρίσκονται στο τέλος.</p>'
             f'<div class="c-foot">Α1–Γ1 · Έκδοση {el_date()}</div></section>')
    return finish(b, cover, "Ελληνικά · Κλίση ονομάτων", "Declension drills.html"), b.n, total

# ------------------------------------------------------------------ conjugation book
PERS = ["εγώ", "εσύ", "αυτός", "εμείς", "εσείς", "αυτοί"]
ECHO = ["έχω", "έχεις", "έχει", "έχουμε", "έχετε", "έχουν"]
EICHA = ["είχα", "είχες", "είχε", "είχαμε", "είχατε", "είχαν"]
TN = {"pres": ("Present", "ενεστώτας"), "impf": ("Imperfect", "παρατατικός"), "aor": ("Aorist", "αόριστος"), "fut": ("Simple future", "στιγμιαίος μέλλοντας"),
      "perf": ("Present perfect", "παρακείμενος"), "plup": ("Pluperfect", "υπερσυντέλικος")}

def vform(src, t, p):
    if t == "fut": return ("θα " + first(src["dep"][p])) if src["dep"][p] else ""
    if t == "perf": return f'{ECHO[p]} {src["inf"]}' if src.get("inf") else ""
    if t == "plup": return f'{EICHA[p]} {src["inf"]}' if src.get("inf") else ""
    return first(src[t][p])

def model_verb(w, src, label):
    ts = [t for t in ("pres", "impf", "aor", "fut", "perf") if not (t == "aor" and src.get("one_past"))]
    head = "".join(f"<th>{TN[t][0]}<br><span lang=el>{TN[t][1]}</span></th>" for t in ts)
    rows = "".join(f"<tr><th lang=el>{PERS[p]}</th>" + "".join(f'<td lang="el">{esc(vform(src, t, p))}</td>' for t in ts) + "</tr>" for p in range(6))
    imp = ""
    if src["impP"][0] or src["impP"][1]:
        imp = f'<p class="sub" lang="el">Προστακτική: {esc(alts(src["impP"][0]) or "—")}, {esc(alts(src["impP"][1]) or "—")}' + (
            f' · εξακολουθητική: {esc(alts(src["impI"][0]) or "—")}, {esc(alts(src["impI"][1]) or "—")}' if any(src["impI"]) else "") + "</p>"
    return f'<div class="dr-model"><table style="max-width:none"><caption lang="el" style="text-align:left;font-weight:700">{esc(label)}</caption><tr><th></th>{head}</tr>{rows}</table>{imp}</div>'

def conj_book():
    rnd = random.Random(2611)
    V, C = J("verbs"), J("context")
    b = Book()
    b.part("v-intro", "Part 1 · Principal parts", "Βασικοί τύποι",
           "<p>Every Greek verb is built from two stems: the imperfective (present, imperfect, continuous future) and the perfective (aorist, simple future, να-forms, perfect). "
           "Knowing the present, the aorist and the dependent form of a verb gives you almost everything. Start here.</p>")
    GROUPS = [("A", "Group A verbs (-ω, stressed on the stem)", "Ρήματα α΄ συζυγίας", lambda w: w["grp"] == "A" and not w["dep"]),
              ("B1", "Group B1 verbs (-άω / -ώ, -άς)", "Ρήματα β΄ συζυγίας, -άω", lambda w: w["grp"] == "B1"),
              ("B2", "Group B2 verbs (-ώ, -είς)", "Ρήματα β΄ συζυγίας, -ώ, -είς", lambda w: w["grp"] == "B2"),
              ("irr", "Irregular verbs", "Ανώμαλα ρήματα", lambda w: w["grp"] == "irregular" and not w["dep"]),
              ("dep", "Deponent verbs (-ομαι, -άμαι, -ούμαι)", "Αποθετικά ρήματα", lambda w: w["dep"])]
    for gid, en, el, test in GROUPS:
        ws = [w for w in V["words"] if test(w)]
        if not ws: continue
        b.sec("pp-" + gid, en, el)
        sel = ws[:20] + (rnd.sample(ws[20:], min(len(ws) - 20, 20)) if len(ws) > 20 else [])
        n = b.ex("Principal parts", "Write the imperfect, the aorist and the dependent (θα/να) form, all in the 1st person singular." + (" Deponents: the forms are passive in shape." if gid == "dep" else ""))
        rows = "".join(f'<tr><td class="given" lang="el">{esc(w["l"])} <span class="sub">{esc(w["en"])}</span></td><td></td><td></td><td></td></tr>' for w in sel)
        b.body.append(f'<table class="dr-pp"><tr><th>present</th><th>imperfect</th><th>aorist</th><th>θα / να</th></tr>{rows}</table>')
        b.key.append(f"<p><b>{n}.</b> " + "; ".join(
            f'<span lang="el"><b>{esc(w["l"])}</b>: {esc(first(w["A"]["impf"][0]))}, {esc(first(w["A"]["aor"][0]) if not w["A"].get("one_past") else "(no separate aorist)")}, {esc(first(w["A"]["dep"][0]))}</span>' for w in sel) + "</p>")
        b.end_sec()
    pw = [w for w in V["words"] if w.get("P")]
    b.sec("pp-pass", "Passive principal parts", "Παθητική φωνή: βασικοί τύποι")
    sel = pw[:20] + rnd.sample(pw[20:], min(len(pw) - 20, 25))
    n = b.ex("From active to passive", "Write the passive present, the passive aorist and the passive participle.")
    rows = "".join(f'<tr><td class="given" lang="el">{esc(w["l"])} <span class="sub">{esc(w["en"])}</span></td><td></td><td></td><td></td></tr>' for w in sel)
    b.body.append(f'<table class="dr-pp"><tr><th>active</th><th>passive present</th><th>passive aorist</th><th>participle</th></tr>{rows}</table>')
    b.key.append(f"<p><b>{n}.</b> " + "; ".join(f'<span lang="el"><b>{esc(w["l"])}</b>: {esc(first(w["P"]["pres"][0]))}, {esc(first(w["P"]["aor"][0]))}, {esc(w["P"].get("ptc") or "—")}</span>' for w in sel) + "</p>")
    b.end_sec(); b.end_part()

    b.part("v-conj", "Part 2 · Conjugation by tense", "Συζυγία ανά χρόνο",
           "<p>Each section shows one model verb in full, then grids to fill (one verb, one tense, all six persons) and single forms.</p>")
    MODELS = {"A": "γράφω", "B1": "αγαπώ", "B2": "μπορώ", "irr": "λέω", "dep": "έρχομαι"}
    for gid, en, el, test in GROUPS:
        ws = [w for w in V["words"] if test(w)]
        if not ws: continue
        b.sec("cj-" + gid, en, el)
        m = next((w for w in ws if w["l"] == MODELS[gid]), ws[0])
        b.body.append(model_verb(m, m["A"], f'{m["l"]} · {m["en"]}'))
        pool = [w for w in ws if w is not m]
        tenses = ["pres", "impf", "aor", "fut", "perf"]
        grids, key = [], []
        for w in (pool[:15] + rnd.sample(pool[15:], min(len(pool) - 15, 15)) if len(pool) > 15 else pool):
            t = rnd.choice([t for t in tenses if not (t == "aor" and w["A"].get("one_past")) and all(vform(w["A"], t, p) for p in range(6))] or ["pres"])
            rows = "".join(f'<tr><th lang="el">{PERS[p]}</th><td lang="el">{"θα " if t == "fut" else ""}</td></tr>' for p in range(6))
            grids.append(f'<table><caption lang="el">{esc(w["l"])} <small>{TN[t][0].lower()} · {TN[t][1]}</small></caption>{rows}</table>')
            key.append(f'<span lang="el"><b>{esc(w["l"])}</b> ({TN[t][1]}): ' + ", ".join(esc(vform(w["A"], t, p)) for p in range(6)) + "</span>")
        n = b.ex("Conjugate", "Write all six persons of the tense shown.")
        b.body.append('<div class="dr-grid">' + "".join(grids) + "</div>")
        b.key.append(f"<p><b>{n}.</b> " + "; ".join(key) + "</p>")
        rows = []
        for w in rnd.sample(pool, min(len(pool), 70)):
            t = rnd.choice(["pres", "impf", "aor", "fut", "perf", "plup"]); p = rnd.randrange(6)
            if t == "aor" and w["A"].get("one_past"): t = "impf"
            f = vform(w["A"], t, p)
            if not f or (t == "pres" and p == 0): continue
            rows.append((f'<span lang="el">({PERS[p]}) {esc(w["l"])}</span> <span class="cue">→ {TN[t][0].lower()}</span>', f))
        n = b.ex("Single forms", "Write the form for the person in brackets.")
        items_list(b, n, rows)
        imp = [w for w in pool if w["A"]["impP"][0] and w["A"]["impP"][1]]
        if imp:
            rows = []
            for w in rnd.sample(imp, min(len(imp), 16)):
                rows.append((f'<span lang="el">{esc(w["l"])}</span> <span class="cue">→ imperative, εσύ and εσείς</span>', f'{first(w["A"]["impP"][0])}, {first(w["A"]["impP"][1])}'))
            n = b.ex("Imperative", "Give the one-off (perfective) imperative for εσύ and for εσείς.")
            items_list(b, n, rows)
        b.end_sec()
    # passive
    b.sec("cj-pass", "The passive voice", "Παθητική φωνή")
    m = next((w for w in pw if w["l"] == "γράφω"), pw[0])
    b.body.append(model_verb(m, m["P"], f'{first(m["P"]["pres"][0])} · passive of {m["l"]}'))
    grids, key = [], []
    for w in pw[:12] + rnd.sample(pw[12:], 12):
        if w is m: continue
        t = rnd.choice([t for t in ("pres", "impf", "aor", "fut") if all(vform(w["P"], t, p) for p in range(6))] or ["aor"])
        rows = "".join(f'<tr><th lang="el">{PERS[p]}</th><td lang="el">{"θα " if t == "fut" else ""}</td></tr>' for p in range(6))
        grids.append(f'<table><caption lang="el">{esc(first(w["P"]["pres"][0]))} <small>{TN[t][0].lower()} · {TN[t][1]}</small></caption>{rows}</table>')
        key.append(f'<span lang="el"><b>{esc(first(w["P"]["pres"][0]))}</b> ({TN[t][1]}): ' + ", ".join(esc(vform(w["P"], t, p)) for p in range(6)) + "</span>")
    n = b.ex("Conjugate in the passive", "Write all six persons of the tense shown.")
    b.body.append('<div class="dr-grid">' + "".join(grids) + "</div>")
    b.key.append(f"<p><b>{n}.</b> " + "; ".join(key) + "</p>")
    rows = []
    for w in rnd.sample(pw, 80):
        t = rnd.choice(["pres", "impf", "aor", "fut", "perf"]); p = rnd.randrange(6)
        f = vform(w["P"], t, p)
        if not f: continue
        rows.append((f'<span lang="el">({PERS[p]}) {esc(first(w["P"]["pres"][0]))}</span> <span class="cue">→ {TN[t][0].lower()}</span>', f))
    n = b.ex("Single passive forms", "Write the form for the person in brackets.")
    items_list(b, n, rows)
    b.end_sec(); b.end_part()

    b.part("v-ctx", "Part 3 · Verbs in context", "Τα ρήματα μέσα στη φράση", "<p>Real example sentences from the word list. Write the verb in brackets in the form the sentence needs; the tense and person are given as a hint.</p>")
    its = [x for x in C["items"] if x["k"] == "v"]
    its = sorted(rnd.sample(its, min(len(its), 800)), key=lambda x: LV.index(x["lv"]) if x["lv"] in LV else 9)
    def lab(c):
        vk, t, p = c.split(".")
        return {"pres": "present", "impf": "imperfect", "aor": "aorist", "dep": "θα/να form"}[t] + (" passive" if vk == "P" else "") + ", " + ["1sg", "2sg", "3sg", "1pl", "2pl", "3pl"][int(p)]
    for lv in LV[:5]:
        sub = [x for x in its if x["lv"] == lv or (lv == "C1" and x["lv"] == "C2")]
        if not sub: continue
        b.sec("vc-" + lv, f"Level {lv}", f"Επίπεδο {lv}")
        n = b.ex(f"Verbs in context, {lv}", "Fill each gap with the right form of the verb in brackets.")
        cloze_list(b, n, [(esc(x["s"]).replace("___", '<span class="blank">&nbsp;</span>') + f' <span class="cue">({esc(x["l"])}: {esc(" or ".join(dict.fromkeys(lab(c) for c in x["c"][:2])))})</span>', x["a"]) for x in sub])
        b.end_sec()
    b.end_part()
    total = count_blanks(b)
    tot_el = f"{total:,}".replace(",", ".")
    cover = ('<section class="cover" lang="el"><div class="c-top">Ελληνικά · Τετράδιο ασκήσεων</div><div class="c-lvl" style="font-size:72pt">Συζυγία ρημάτων</div>'
             '<div class="c-name">Χρόνοι, όψεις, φωνές</div>'
             f'<p class="c-blurb">{b.n} ασκήσεις με περίπου {tot_el} κενά προς συμπλήρωση, σε πραγματικά ρήματα του λεξιλογίου της εφαρμογής: ' +
             'βασικοί τύποι, κλίση σε όλους τους χρόνους της ενεργητικής και της παθητικής φωνής, προστακτική, αποθετικά και προτάσεις με κενά. Οι λύσεις βρίσκονται στο τέλος.</p>'
             f'<div class="c-foot">Α1–Γ1 · Έκδοση {el_date()}</div></section>')
    return finish(b, cover, "Ελληνικά · Συζυγία ρημάτων", "Conjugation drills.html"), b.n, total

def count_blanks(b):
    """Cells left for the learner (empty, or holding only an article or θα) plus the gaps in the lists."""
    body = "".join(b.body)
    return len(re.findall(r'<td(?: lang="el")?>(?:[α-ω]{1,4} ?)?</td>|class="blank"', body))

def finish(b, cover, title, fname):
    toc = f'<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(b.toc)}<li class="toc-p"><a href="#answers">Answer key</a></li><li class="toc-p"><a href="#credits">Sources</a></li></ol></section>'
    key = f'<section class="part" id="answers"><div class="part-h"><div class="pn">Answers</div><h1>Answer key</h1><div class="pel" lang="el">Λύσεις</div></div><div class="key">{"".join(b.key)}</div></section>'
    credits = ("<section class='part' id='credits'><h2 class='unit'>Sources</h2><p>Made for the Ελληνικά app, for personal, non-commercial study. "
               "Words, glosses and example sentences: the app's word list (data/lexicon). Paradigms: Wiktionary's inflection tables (via kaikki.org, CC BY-SA 4.0), "
               "kept only where they agree with the word list; regular words without a Wiktionary table were generated by rule and kept only where every form matches the word list's forms index. "
               "The same items are in the app under Resources → Τετράδια κλίσης, with instant feedback and spaced review.</p></section>")
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{esc(title)}</title><style>{CSS}{EXTRA}</style></head>'
           f'<body>{cover}{toc}{"".join(b.body)}{key}{credits}</body></html>')
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(doc)
    return len(doc)

if __name__ == "__main__":
    for f in (decl_book, conj_book):
        size, n, total = f()
        print(f.__name__, n, "exercises,", total, "blanks,", size // 1024, "KB html")
