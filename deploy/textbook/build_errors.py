#!/usr/bin/env python3
"""Error hunt workbook: printable companion volume built from library/errors/*.json.

Usage: python3 build_errors.py --app <app root> --out <dir>   writes "<dir>/Errors.html"
Then:  node render_pdf.js <dir> <dir> Errors; node render_cover.js <dir>/Cover.html <dir>/cover.pdf;
       python3 swap_cover.py <dir>/Ellinika-Errors-textbook.pdf <dir>/cover.pdf; compress.py into downloads/textbook/Ellinika-Errors.pdf
Each topic: what goes wrong, then the sentences to correct with a writing line; then the short texts;
the answer key at the back gives every corrected form with the reason.
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from covers_el import el_date

APP = sys.argv[sys.argv.index("--app") + 1] if "--app" in sys.argv else "/mnt/project-files/app"
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "/tmp/errors-build"
SRC = f"{APP}/library/errors"
CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "textbook.css"), encoding="utf-8").read()
EXTRA_CSS = """
.ef-about { background: #f3f6fb; border-left: 3px solid #3e5c8a; padding: 6px 10px; margin: 6px 0 10px; }
.ef-list { margin: 0; padding-left: 0; list-style: none; }
.ef-list li { margin: 0 0 7px; break-inside: avoid; display: grid; grid-template-columns: 2.2em 1fr; }
.ef-list .n { font: 600 9pt sans-serif; color: #3e5c8a; }
.ef-s { font-size: 11.5pt; }
.ef-line { border-bottom: 1px dotted #9aa3b2; height: 6mm; grid-column: 2; }
.ef-txt { font-size: 11.5pt; line-height: 2.1; margin: 4px 0 8px; }
.ef-txt-box { break-inside: avoid; margin-bottom: 8mm; }
.lvl { display: inline-block; font: 600 8pt sans-serif; color: #fff; background: #3e5c8a; border-radius: 3px; padding: 1px 5px; margin-right: 6px; vertical-align: middle; }
.lvl-h { font: 600 10pt sans-serif; color: #3e5c8a; margin: 10px 0 4px; border-bottom: 1px solid #d5dbe5; }
.k p { margin: 0 0 5px; break-inside: avoid; font-size: 9.5pt; }
.k .bad { text-decoration: line-through; color: #a33; }
.k .ok { color: #1d6b3a; font-weight: 600; }
.k .cat { font: 600 7.5pt sans-serif; color: #6b7487; text-transform: uppercase; letter-spacing: .03em; }
"""
LV = ["A2", "B1", "B2", "C1"]

def esc(s): return html.escape("" if s is None else str(s), quote=True)
def md(s):
    s = esc(s); s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s); return re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
def wrong(it): return "".join(p if isinstance(p, str) else it["errs"][p]["w"] for p in it["parts"])
def fixed(it): return "".join(p if isinstance(p, str) else it["errs"][p]["r"][0] for p in it["parts"])

def key_entry(n, it, cats):
    if it.get("ok"):
        return f'<p><strong>{n}.</strong> ✓ <span lang="el">{esc(wrong(it))}</span> · {md(it["why"])}</p>'
    parts = []
    for e in it["errs"]:
        alt = f' (also: <span lang="el">{esc(", ".join(e["r"][1:]))}</span>)' if len(e["r"]) > 1 else ""
        parts.append(f'<span class="cat">{esc(cats[e["c"]])}</span> <span class="bad" lang="el">{esc(e["w"])}</span> → <span class="ok" lang="el">{esc(e["r"][0])}</span>{alt}: {md(e["why"])}')
    lead = f'<strong>{n}.</strong> <span lang="el">{esc(fixed(it))}</span><br>' if len(it["errs"]) == 1 else f"<strong>{n}.</strong> "
    return "<p>" + lead + "<br>".join(parts) + "</p>"

def main():
    idx = json.load(open(f"{SRC}/index.json", encoding="utf-8"))
    cats = {c["id"]: c["el"] for c in idx["categories"]}
    toc, body, keys, n = [], [], [], 0
    for ci, c in enumerate(idx["categories"], 1):
        d = json.load(open(f"{SRC}/{c['file']}", encoding="utf-8"))
        pid = f"cat-{d['id']}"
        toc.append(f'<li><a href="#{pid}">{ci}. {esc(d["title"])}</a> <span lang="el">· {esc(d["el"])}</span></li>')
        out = [f'<section class="lesson" id="{pid}"><h2 class="unit"><span lang="el">{ci}. {esc(d["el"])}</span> <span class="lt-en">{esc(d["title"])}</span></h2>',
               f'<div class="ef-about">{md(d["about"])}</div>']
        keys.append(f'<h3 class="lvl-h">{ci}. <span lang="el">{esc(d["el"])}</span></h3>')
        for L in LV:
            items = [x for x in d["items"] if x["level"] == L]
            if not items: continue
            out.append(f'<div class="lvl-h">{L}</div><ol class="ef-list">')
            for it in items:
                n += 1
                out.append(f'<li><span class="n">{n}.</span><span class="ef-s" lang="el">{esc(wrong(it))}</span><span class="ef-line"></span></li>')
                keys.append(key_entry(n, it, cats))
            out.append("</ol>")
        out.append("</section>")
        body.append("".join(out))
    paras = json.load(open(f"{SRC}/paragraphs.json", encoding="utf-8"))["items"]
    toc.append('<li class="toc-p"><a href="#texts">Find every mistake in a text</a> <span lang="el">· Κείμενα</span></li>')
    keys.append('<h3 class="lvl-h">Κείμενα · Texts</h3>')
    out = ['<section class="part" id="texts"><div class="part-h"><div class="pn">Part 2</div><h1>Find every mistake in a text</h1><div class="pel" lang="el">Βρες όλα τα λάθη</div></div>',
           "<p>Each text is a learner's email, letter or essay. The number of mistakes is given; underline them and write the corrections above the line.</p>"]
    for it in paras:
        n += 1
        out.append(f'<div class="ef-txt-box"><h3 class="lt"><span lang="el"><span class="lvl">{esc(it["level"])}</span>{n}. {esc(it["el"])}</span>'
                   f'<span class="lt-en">{esc(it["title"])} · {len(it["errs"])} mistakes</span></h3><p class="ef-txt" lang="el">{esc(wrong(it))}</p></div>')
        keys.append(f'<p><strong>{n}. <span lang="el">{esc(it["el"])}</span></strong></p><p lang="el">{esc(fixed(it))}</p><p><em>{esc(it["en"])}</em></p>' +
                    "".join(f'<p><span class="cat">{esc(cats[e["c"]])}</span> <span class="bad" lang="el">{esc(e["w"])}</span> → <span class="ok" lang="el">{esc(e["r"][0])}</span>: {md(e["why"])}</p>' for e in it["errs"]))
    out.append("</section>")
    body.append("".join(out))
    n_sent = sum(c["count"] for c in idx["categories"])
    n_err = sum(c["errors"] for c in idx["categories"]) + sum(p["errors"] for p in idx["paragraphs"])
    intro = ('<section class="part" id="how"><div class="part-h"><div class="pn">Part 1</div><h1>Sentences by topic</h1><div class="pel" lang="el">Προτάσεις ανά θέμα</div></div>'
             "<p>Each sentence has one mistake, or none: a few are correct on purpose, to keep you from correcting what is right. "
             "Find the mistake and write the corrected sentence on the line. The sentences run from A2 to C1 inside each topic. "
             "The answer key at the back gives the correct form and the reason. The same exercises are interactive in the app under Resources → Βρες το λάθος.</p></section>")
    toc_html = (f'<section class="toc"><h1>Contents</h1><ol class="toc-l"><li class="toc-p"><a href="#how">Sentences by topic</a><ol>{"".join(toc[:-1])}</ol></li>'
                f'{toc[-1]}<li class="toc-p"><a href="#answers">Answer key</a></li></ol></section>')
    cover = ('<section class="cover" lang="el"><div class="c-top">Ελληνικά · Τετράδιο ασκήσεων</div><div class="c-lvl">Βρες το λάθος</div>'
             '<div class="c-name">Τα συνηθισμένα λάθη των μαθητών της ελληνικής</div>'
             f'<p class="c-blurb">{n_sent} προτάσεις σε {len(idx["categories"])} θεματικές ενότητες και {len(paras)} κείμενα, με {n_err} λάθη για να τα βρεις και να τα διορθώσεις: '
             'πτώσεις, συμφωνία, γένος, άρθρο, ποιόν ενεργείας, υποτακτική, αδύναμοι τύποι, τελικό -ν, τονισμός, ορθογραφία, ρηματικοί τύποι, προθέσεις, σύνταξη, ύφος, λεξιλόγιο. '
             'Με λύσεις και εξηγήσεις για κάθε λάθος.</p>'
             f'<div class="c-foot">Α2–Γ1 · Έκδοση {el_date()}</div></section>')
    answers = f'<section class="part k" id="answers"><div class="part-h"><div class="pn">Answers</div><h1>Answer key</h1><div class="pel" lang="el">Λύσεις</div></div>{"".join(keys)}</section>'
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ελληνικά · Error hunt</title><style>{CSS}{EXTRA_CSS}</style></head>'
           f'<body>{cover}{toc_html}{intro}{"".join(body)}{answers}</body></html>')
    os.makedirs(OUT, exist_ok=True)
    open(f"{OUT}/Errors.html", "w", encoding="utf-8").write(doc)
    # the cover alone, printed without the page footer and swapped in as page 1 by swap_cover.py (covers carry no English)
    open(f"{OUT}/Cover.html", "w", encoding="utf-8").write(f'<!doctype html><html lang="el"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{cover}</body></html>')
    print(f"Errors: {n_sent} sentences, {len(paras)} texts, {n_err} mistakes, {len(doc) // 1024} KB html")

if __name__ == "__main__":
    main()
