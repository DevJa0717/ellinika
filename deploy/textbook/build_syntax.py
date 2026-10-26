#!/usr/bin/env python3
"""Syntax and discourse guide + pocket grammar cards: two companion volumes built from app/library/syntax and app/library/cards.

Usage: python3 build_syntax.py --out <dir>   writes "<dir>/Syntax.html" and "<dir>/Grammar cards.html"
Then:  node render_syntax.js <dir> downloads/textbook   (fits every card on one page, prints both PDFs)
       python3 compress.py <pdf> <pdf> "<title>" for each.
"""
import html, json, os, random, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from covers_el import el_date, el_level

ROOT = "/mnt/project-files"
APP = os.environ.get("APP", f"{ROOT}/app")
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else f"{ROOT}/downloads/textbook/build"
SITE = "https://devja0717.github.io/ellinika/"
CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "textbook.css"), encoding="utf-8").read()
EXTRA_CSS = """
.pos-tip { border-left: 3px solid #b8892b; background: #fbf6ea; padding: 6px 10px; margin: 8px 0; break-inside: avoid; }
.sc { margin: 8px 0; padding: 6px 10px; border: 1px dashed #b9c0cc; }
.sc ol { margin: 4px 0 0; } .sc li { margin: 4px 0; break-inside: avoid; }
.sc .q-opts { color: #3c4658; }
.sc .tiles { color: #3c4658; letter-spacing: 0.01em; }
.sc .line { border-bottom: 1px solid #aab3c2; height: 6mm; width: 85%; }
.lvl { display: inline-block; font: 600 8pt sans-serif; color: #fff; background: #3e5c8a; border-radius: 3px; padding: 1px 5px; margin-right: 6px; vertical-align: middle; }
.rel { font-size: 8.5pt; color: var(--muted); margin: 2mm 0 3mm; }
.rel a { color: var(--accent); }
/* one card per page */
.card { page-break-before: always; width: 178mm; box-sizing: border-box; }
.card-h { display: flex; justify-content: space-between; align-items: baseline; border-bottom: 3px solid var(--accent); padding-bottom: 2mm; margin-bottom: 3mm; }
.card-h h1 { margin: 0; font-size: 18pt; color: var(--accent); }
.card-h .ce { font-family: "TBSans", sans-serif; color: var(--muted); font-size: 10pt; }
.card-h .cg { font-family: "TBSans", sans-serif; color: var(--accent2); font-size: 8pt; text-transform: uppercase; letter-spacing: 0.08em; text-align: right; }
.card table { margin: 1mm 0 2.5mm; }
.card ul { margin: 1mm 0 2mm; }
"""


def esc(s):
    return html.escape("" if s is None else str(s), quote=True)


def md(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s


def words(s):
    return re.sub(r"[.;;!?·]+$", "", s).split()


def tiles(q, n):
    ws = words(q["answer"])
    ws[0] = ws[0][:1].lower() + ws[0][1:]
    r = random.Random(n * 31 + len(ws))
    order = ws[:]
    while len(order) > 1 and order == ws:
        r.shuffle(order)
    return " / ".join(order)


def block(b, keys, ref):
    if "p" in b: return f"<p>{md(b['p'])}</p>"
    if "tip" in b: return f'<div class="pos-tip">{md(b["tip"])}</div>'
    if "list" in b: return "<ul>" + "".join(f"<li>{md(x)}</li>" for x in b["list"]) + "</ul>"
    if "ex" in b:
        rows = "".join(f'<tr><td class="el" lang="el">{md(x.get("el"))}</td><td class="en">{md(x.get("en"))}</td></tr>' for x in b["ex"])
        return f'<table class="ex">{rows}</table>'
    if "table" in b:
        t = b["table"]
        th = "".join(f"<th>{md(h)}</th>" for h in t.get("head") or [])
        rows = "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in t.get("rows", []))
        return f'<table>{"<thead><tr>" + th + "</tr></thead>" if any(h.strip() for h in t.get("head") or []) else ""}<tbody>{rows}</tbody></table>'
    if "links" in b:
        return '<div class="rel">In the app: ' + " · ".join(
            f'<a href="{SITE}{esc(l["href"])}">{esc(l["el"] or l["title"])}</a>' for l in b["links"]) + "</div>"
    if "check" in b:
        out = '<div class="sc"><div class="gl-h">Exercises</div><ol>'
        for q in b["check"]:
            n = len(keys) + 1
            if q["type"] == "choice":
                letters = "abcdef"
                opts = " &nbsp; ".join(f"({letters[i]}) {md(o)}" for i, o in enumerate(q["options"]))
                out += f'<li value="{n}">{md(q["q"])}<div class="q-opts" lang="el">{opts}</div></li>'
                ans = f'({letters[q["options"].index(q["answer"])]}) {md(q["answer"])}'
            elif q["type"] == "order":
                out += f'<li value="{n}">Put in order: {md(q["q"])}<div class="tiles" lang="el">{esc(tiles(q, n))}</div><div class="line"></div></li>'
                ans = md(q["answer"]) + "".join(f" (also: {md(a)})" for a in q.get("accept", []))
            else:
                out += f'<li value="{n}">{md(q["q"])}<div class="line"></div></li>'
                ans = md(q["answer"]) + "".join(f" (also: {md(a)})" for a in q.get("accept", []))
            keys.append((n, ref, f'<strong>{n}.</strong> {ans}' + (f' · {md(q["why"])}' if q.get("why") else "")))
        return out + "</ol></div>"
    return ""


def page(title, cover, toc, body):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{esc(title)}</title><style>{CSS}{EXTRA_CSS}</style></head>'
            f'<body>{cover}{toc}{body}</body></html>')


CREDITS = ("<section class='part' id='credits'><h2 class='unit'>Sources and credits</h2>"
           "<p>Written for the Ελληνικά app, for personal, non-commercial study, drawing on:</p><ul>"
           "<li>D. Holton, P. Mackridge, I. Philippaki-Warburton, V. Spyropoulos, <em>Greek: An Essential Grammar</em> (Routledge), used for personal study only.</li>"
           "<li>Ε. Πουλοπούλου (Poulopoulou), <em>Modern Greek: Grammar Notes for Absolute Beginners</em>, CC BY-NC-SA. Material derived from it is shared under the same licence, non-commercially.</li></ul></section>")


def syntax():
    idx = json.load(open(f"{APP}/library/syntax/index.json", encoding="utf-8"))
    toc, body, keys = [], [], []
    for n, it in enumerate(idx["items"], 1):
        d = json.load(open(f"{APP}/library/syntax/{it['file']}", encoding="utf-8"))
        pid = f"syn-{d['id']}"
        toc.append(f'<li class="toc-p"><a href="#{pid}">{n}. {esc(d["title"])}</a> <span lang="el">· {esc(d["el"])}</span><ol>')
        body.append(f'<section class="part" id="{pid}"><div class="part-h"><div class="pn">Part {n} · {esc(d.get("span", ""))}</div>'
                    f'<h1>{esc(d["title"])}</h1><div class="pel" lang="el">{esc(d["el"])}</div></div>')
        body.append("".join(block(b, keys, d["title"]) for b in d.get("intro", [])))
        for i, s in enumerate(d["sections"]):
            sid = f"{pid}-{i}"
            toc.append(f'<li><a href="#{sid}">{esc(s["level"])} · {esc(s["title"])}</a></li>')
            inner = "".join(block(b, keys, f"{d['title']} · {s['title']}") for b in s["body"])
            body.append(f'<section class="lesson" id="{sid}"><h3 class="lt"><span lang="el"><span class="lvl">{esc(s["level"])}</span>{esc(s["el"])}</span>'
                        f'<span class="lt-en">{esc(s["title"])}</span></h3>{inner}</section>')
        toc.append("</ol></li>"); body.append("</section>")
    key_html = "".join(f"<p>{k}</p>" for _, _, k in keys)
    toc.append('<li class="toc-p"><a href="#answers">Answer key</a></li><li class="toc-p"><a href="#credits">Sources and credits</a></li>')
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Answers</div><h1>Answer key</h1><div class="pel" lang="el">Λύσεις</div></div><div class="key">{key_html}</div></section>')
    body.append(CREDITS)
    secs = sum(i["sections"] for i in idx["items"])
    cover = ('<section class="cover" lang="el"><div class="c-top">Ελληνικά · Συνοδευτικό εγχειρίδιο</div><div class="c-lvl" style="font-size:80pt">Σύνταξη</div>'
             '<div class="c-name">Σύνταξη και λόγος</div>'
             f'<p class="c-blurb">{len(idx["items"])} κεφάλαια και {secs} ενότητες: σειρά των λέξεων, αδύναμοι τύποι, άρνηση, ερωτήσεις, συμφωνία, '
             f'αλυσίδες με το «να», δευτερεύουσες προτάσεις, υποθετικοί λόγοι, πλάγιος λόγος και οργάνωση του κειμένου, με {len(keys)} ασκήσεις και λύσεις.</p>'
             f'<div class="c-foot">{el_level("A1–C1")} · Έκδοση {el_date()}</div></section>')
    toc_html = f'<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(toc)}</ol></section>'
    with open(f"{OUT}/Syntax.html", "w", encoding="utf-8") as f:
        f.write(page("Ελληνικά · Syntax and discourse", cover, toc_html, "".join(body)))
    print(f"Syntax: {len(idx['items'])} parts, {secs} sections, {len(keys)} exercises")


def cards():
    idx = json.load(open(f"{APP}/library/cards/index.json", encoding="utf-8"))
    toc, body, n = [], [], 0
    for g in idx["groups"]:
        d = json.load(open(f"{APP}/library/cards/{g['file']}", encoding="utf-8"))
        toc.append(f'<li class="toc-p">{esc(g["title"])} <span lang="el">· {esc(g["el"])}</span><ol>')
        for c in d["cards"]:
            n += 1
            toc.append(f'<li><a href="#card-{c["id"]}">{n}. {esc(c["title"])}</a></li>')
            inner = "".join(block(b, [], c["title"]) for b in c["body"])
            body.append(f'<section class="card" id="card-{c["id"]}"><div class="card-h"><div><h1 lang="el">{esc(c["el"])}</h1>'
                        f'<div class="ce">{esc(c["title"])}</div></div><div class="cg"><span class="lvl">{esc(c["level"])}</span><br>{n} · {esc(g["title"])}</div></div>'
                        f'<div class="cb">{inner}</div></section>')
        toc.append("</ol></li>")
    cover = ('<section class="cover" lang="el"><div class="c-top">Ελληνικά · Συνοδευτικό εγχειρίδιο</div><div class="c-lvl" style="font-size:80pt">Κάρτες</div>'
             '<div class="c-name">Κάρτες γραμματικής για επανάληψη</div>'
             f'<p class="c-blurb">{n} κάρτες σε {len(idx["groups"])} ομάδες, μία σελίδα η καθεμία: προφορά, ονόματα, επίθετα, αντωνυμίες, αριθμοί, ρήματα, '
             'μικρές λέξεις, σύνταξη και λόγια γλώσσα.</p>'
             f'<div class="c-foot">{el_level("A1–C1")} · Έκδοση {el_date()}</div></section>')
    toc_html = f'<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(toc)}</ol></section>'
    with open(f"{OUT}/Grammar cards.html", "w", encoding="utf-8") as f:
        f.write(page("Ελληνικά · Pocket grammar cards", cover, toc_html, "".join(body) + CREDITS))
    print(f"Cards: {len(idx['groups'])} groups, {n} cards")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    syntax()
    cards()
