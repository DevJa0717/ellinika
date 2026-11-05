#!/usr/bin/env python3
"""Grammar outline (Schaum's-style) companion volume, built from library/theoria/*.json.

Each chapter: theory by section, then "Solved problems" (with solutions), then "Supplementary problems"
(every drill of the chapter). The answer key, grouped by chapter, and the references close the book.

Usage: python3 build_theoria.py --out <dir>        writes "<dir>/Grammar outline.html"
Then:  node render_theoria.js <dir> downloads/textbook
       python3 compress.py downloads/textbook/Ellinika-Grammar-outline.pdf downloads/textbook/Ellinika-Grammar-outline.pdf "Ελληνικά · Γραμματική"
"""
import html, json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from covers_el import el_date, el_level

APP = os.environ.get("APP", os.path.abspath(os.path.join(HERE, "../..")))
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(APP, "downloads/textbook/build")
SITE = "https://devja0717.github.io/ellinika/"
SRC = os.path.join(APP, "library/theoria")
CSS = open(os.path.join(HERE, "textbook.css"), encoding="utf-8").read()
EXTRA_CSS = """
.pos-tip { border-left: 3px solid #b8892b; background: #fbf6ea; padding: 6px 10px; margin: 8px 0; break-inside: avoid; }
.lvl { display: inline-block; font: 600 8pt sans-serif; color: #fff; background: #3e5c8a; border-radius: 3px; padding: 1px 5px; margin-right: 6px; vertical-align: middle; }
.rel { font-size: 8.5pt; color: var(--muted); margin: 2mm 0 3mm; }
.rel a { color: var(--accent); }
.prob-h { font-family: "TBSans", sans-serif; font-size: 12pt; color: var(--accent); border-bottom: 2px solid var(--accent); padding-bottom: 1mm; margin: 7mm 0 3mm; break-after: avoid; }
.solved { margin: 0; padding: 0; list-style: none; }
.solved li { margin: 0 0 3mm; break-inside: avoid; }
.solved .n { font-family: "TBSans", sans-serif; font-weight: 700; color: var(--accent); margin-right: 4px; }
.solved .sol { margin: 1mm 0 0 7mm; }
.solved .sol b { font-family: "TBSans", sans-serif; font-size: 8.5pt; color: var(--accent2); text-transform: uppercase; letter-spacing: 0.05em; margin-right: 4px; }
.solved .why { margin: 0.5mm 0 0 7mm; color: var(--muted); font-size: 9pt; }
.supp { margin: 0; padding-left: 9mm; }
.supp li { margin: 0 0 2.4mm; break-inside: avoid; }
.supp .q-opts, .supp .tiles { color: #3c4658; }
.supp .line { border-bottom: 1px solid #aab3c2; height: 5.5mm; width: 85%; }
.key h3 { font-family: "TBSans", sans-serif; font-size: 10.5pt; color: var(--accent); margin: 4mm 0 1mm; break-after: avoid; }
.key p { margin: 0.6mm 0; font-size: 8.6pt; line-height: 1.35; }
.part-page { page-break-before: always; height: 230mm; display: flex; flex-direction: column; justify-content: center; }
.part-page .pp-n { font-family: "TBSans", sans-serif; color: var(--accent2); letter-spacing: 0.1em; text-transform: uppercase; }
.part-page h1 { font-size: 30pt; color: var(--accent); margin: 3mm 0; }
.part-page .pp-en { font-family: "TBSans", sans-serif; color: var(--muted); font-size: 14pt; }
.part-page ol { margin-top: 8mm; font-size: 11pt; }
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
    if not q.get("keepCase"):
        ws[0] = ws[0][:1].lower() + ws[0][1:]
    r = random.Random(n * 31 + len(ws))
    order = ws[:]
    while len(order) > 1 and order == ws:
        r.shuffle(order)
    return " / ".join(order)


def alts(a):
    return [x.strip() for x in str(a).split(" | ") if x.strip()]


def theory(b):
    if "p" in b: return f"<p>{md(b['p'])}</p>"
    if "tip" in b: return f'<div class="pos-tip">{md(b["tip"])}</div>'
    if "list" in b: return "<ul>" + "".join(f"<li>{md(x)}</li>" for x in b["list"]) + "</ul>"
    if "olist" in b: return "<ol>" + "".join(f"<li>{md(x)}</li>" for x in b["olist"]) + "</ol>"
    if "ex" in b:
        rows = "".join(f'<tr><td class="el" lang="el">{md(x.get("el"))}</td><td class="en">{md(x.get("en"))}</td></tr>' for x in b["ex"])
        return f'<table class="ex">{rows}</table>'
    if "table" in b:
        t = b["table"]
        th = "".join(f"<th>{md(h)}</th>" for h in t.get("head") or [])
        rows = "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in t.get("rows", []))
        return f'<table>{"<thead><tr>" + th + "</tr></thead>" if any(str(h).strip() for h in t.get("head") or []) else ""}<tbody>{rows}</tbody></table>'
    if "links" in b and b["links"]:
        return '<div class="rel">In the app: ' + " · ".join(
            f'<a href="{SITE}{esc(l["href"])}">{esc(l.get("el") or l.get("title"))}</a>' for l in b["links"]) + "</div>"
    return ""


def chapter(d, keys):
    num = d["num"]
    solved, supp = [], []
    out = [f'<section class="part" id="ch-{d["id"]}"><div class="part-h"><div class="pn">Chapter {num} · {esc(d.get("span", ""))}</div>'
           f'<h1>{esc(d["title"])}</h1><div class="pel" lang="el">{esc(d["el"])}</div></div>']
    out.append("".join(theory(b) for b in d.get("intro", [])))
    for i, s in enumerate(d["sections"]):
        inner = []
        for b in s["body"]:
            if "solved" in b: solved += b["solved"]
            elif "check" in b: supp += b["check"]
            else: inner.append(theory(b))
        out.append(f'<section class="lesson" id="ch-{d["id"]}-{i}"><h3 class="lt"><span lang="el"><span class="lvl">{esc(s["level"])}</span>{esc(s["el"])}</span>'
                   f'<span class="lt-en">{esc(s["title"])}</span></h3>{"".join(inner)}</section>')
    if solved:
        out.append('<h2 class="prob-h">Solved problems · Λυμένες ασκήσεις</h2><ol class="solved">')
        for k, p in enumerate(solved, 1):
            a = alts(p["a"])
            also = "".join(f"<br>also: {md(x)}" for x in a[1:3])
            out.append(f'<li><span class="n">{num}.{k}</span>{md(p["q"])}<div class="sol" lang="el"><b>Solution</b>{md(a[0] if a else "")}{also}</div>'
                       + (f'<div class="why">{md(p["why"])}</div>' if p.get("why") else "") + "</li>")
        out.append("</ol>")
    if supp:
        out.append('<h2 class="prob-h">Supplementary problems · Ασκήσεις</h2><ol class="supp">')
        ck = []
        for k, q in enumerate(supp, 1):
            n = f"{num}.{k}"
            if q["type"] == "choice":
                letters = "abcdefgh"
                opts = " &nbsp; ".join(f"({letters[i]}) {md(o)}" for i, o in enumerate(q["options"]))
                out.append(f'<li value="{k}">{md(q["q"])}<div class="q-opts" lang="el">{opts}</div></li>')
                ans = f'({letters[q["options"].index(q["answer"])]}) {md(q["answer"])}'
            elif q["type"] == "order":
                out.append(f'<li value="{k}">Put in order: {md(q["q"])}<div class="tiles" lang="el">{esc(tiles(q, k))}</div><div class="line"></div></li>')
                ans = md(q["answer"]) + "".join(f" (also: {md(a)})" for a in q.get("accept", [])[:2])
            else:
                out.append(f'<li value="{k}">{md(q["q"])}<div class="line"></div></li>')
                ans = md(q["answer"]) + "".join(f" (also: {md(a)})" for a in q.get("accept", [])[:2])
            ck.append(f'<p><strong>{n}</strong> {ans}' + (f' · {md(q["why"])}' if q.get("why") else "") + "</p>")
        out.append("</ol>")
        keys.append((num, d["title"], d["el"], ck))
    out.append("</section>")
    return "".join(out), len(solved), len(supp)


def references():
    p = os.path.join(SRC, "references.json")
    if not os.path.exists(p): return ""
    r = json.load(open(p, encoding="utf-8"))
    out = [f'<section class="part" id="refs"><div class="part-h"><div class="pn">References</div><h1>{esc(r["title"])}</h1><div class="pel" lang="el">{esc(r["el"])}</div></div>']
    out.append("".join(theory(b) for b in r.get("intro", []) if "links" not in b))
    for s in r["sections"]:
        out.append(f'<h3 class="lt"><span lang="el">{esc(s["el"])}</span><span class="lt-en">{esc(s["title"])}</span></h3>')
        out.append("".join(theory(b) for b in s["body"]))
    out.append("</section>")
    return "".join(out)


def main():
    os.makedirs(OUT, exist_ok=True)
    idx = json.load(open(os.path.join(SRC, "index.json"), encoding="utf-8"))
    toc, body, keys = [], [], []
    tot_s = tot_q = 0
    parts = []
    for it in idx["items"]:
        if it.get("part"): parts.append((it["part"], []))
        parts[-1][1].append(it)
    for (pn, pel, pen), items in parts:
        pid = "part-" + str(items[0]["num"])
        body.append(f'<section class="part-page" id="{pid}"><div class="pp-n" lang="el">{esc(pn)}</div><h1 lang="el">{esc(pel)}</h1><div class="pp-en">{esc(pen)}</div><ol>'
                    + "".join(f'<li value="{it["num"]}"><span lang="el">{esc(it["el"])}</span> · {esc(it["title"])}</li>' for it in items) + "</ol></section>")
        toc.append(f'<li class="toc-p"><a href="#{pid}"><span lang="el">{esc(pn)} · {esc(pel)}</span></a> · {esc(pen)}<ol>')
        for it in items:
            d = json.load(open(os.path.join(SRC, it["file"]), encoding="utf-8"))
            html_, ns, nq = chapter(d, keys)
            body.append(html_); tot_s += ns; tot_q += nq
            toc.append(f'<li value="{it["num"]}"><a href="#ch-{d["id"]}">{esc(d["title"])}</a> <span lang="el">· {esc(d["el"])}</span></li>')
        toc.append("</ol></li>")
    key_html = "".join(f'<h3>{num}. {esc(t)} <span lang="el">· {esc(el)}</span></h3>' + "".join(ck) for num, t, el, ck in keys)
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Answers</div><h1>Answers to supplementary problems</h1><div class="pel" lang="el">Λύσεις</div></div><div class="key">{key_html}</div></section>')
    body.append(references())
    toc.append('<li class="toc-p"><a href="#answers">Answers to supplementary problems</a></li><li class="toc-p"><a href="#refs">References and validation</a></li>')
    n = len(idx["items"]); secs = sum(i["sections"] for i in idx["items"])
    cover = ('<section class="cover" lang="el"><div class="c-top">Ελληνικά · Συνοδευτικό εγχειρίδιο</div><div class="c-lvl" style="font-size:72pt">Γραμματική</div>'
             '<div class="c-name">Γραμματική σε θεωρία και ασκήσεις</div>'
             f'<p class="c-blurb">{n} κεφάλαια σε {len(parts)} μέρη και {secs} ενότητες: σύντομη θεωρία με παραδείγματα από την καθημερινή γλώσσα, '
             f'{tot_s} λυμένες ασκήσεις, {tot_q} ασκήσεις με λύσεις, βιβλιογραφία και έλεγχος.</p>'
             f'<div class="c-foot">{el_level("A1–C1")} · Έκδοση {el_date()}</div></section>')
    toc_html = f'<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(toc)}</ol></section>'
    page = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ελληνικά · Γραμματική σε θεωρία και ασκήσεις</title>'
            f'<style>{CSS}{EXTRA_CSS}</style></head><body>{cover}{toc_html}{"".join(body)}</body></html>')
    with open(os.path.join(OUT, "Grammar outline.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Grammar outline: {n} chapters, {len(parts)} parts, {secs} sections, {tot_s} solved, {tot_q} supplementary problems")


if __name__ == "__main__":
    main()
