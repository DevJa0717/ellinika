#!/usr/bin/env python3
"""Grammar by part of speech: a standalone companion volume built from app/library/pos/*.json.

Usage: python3 build_pos.py --out <dir>   writes "<dir>/Parts of speech.html"
Then:  node render_pdf.js <dir> <dir> "Parts of speech", then compress.py into downloads/textbook/Ellinika-Parts-of-speech.pdf
Kept separate from build_textbook.py (the level volumes) so the two can change independently.
"""
import datetime, html, json, os, re, sys

ROOT = "/mnt/project-files"
POS = f"{ROOT}/app/library/pos"
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else f"{ROOT}/downloads/textbook/build"
CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "textbook.css"), encoding="utf-8").read()
EXTRA_CSS = """
.pos-tip { border-left: 3px solid #b8892b; background: #fbf6ea; padding: 6px 10px; margin: 8px 0; break-inside: avoid; }
.sc { margin: 8px 0; padding: 6px 10px; border: 1px dashed #b9c0cc; break-inside: avoid; }
.sc ol { margin: 4px 0 0; } .sc li { margin: 3px 0; }
.sc .q-opts { color: #3c4658; }
.lvl { display: inline-block; font: 600 8pt sans-serif; color: #fff; background: #3e5c8a; border-radius: 3px; padding: 1px 5px; margin-right: 6px; vertical-align: middle; }
"""

def esc(s):
    return html.escape("" if s is None else str(s), quote=True)

def md(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s

def para(s):
    return f"<p>{md(s)}</p>"

def block(b, keys, ref):
    if "p" in b: return para(b["p"])
    if "tip" in b: return f'<div class="pos-tip">{md(b["tip"])}</div>'
    if "list" in b: return "<ul>" + "".join(f"<li>{md(x)}</li>" for x in b["list"]) + "</ul>"
    if "ex" in b:
        rows = "".join(f'<tr><td class="el" lang="el">{md(x.get("el"))}</td><td class="en">{md(x.get("en"))}</td></tr>' for x in b["ex"])
        return f'<table class="ex">{rows}</table>'
    if "table" in b:
        t = b["table"]
        th = "".join(f"<th>{md(h)}</th>" for h in t.get("head") or [])
        rows = "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in t.get("rows", []))
        return f'<table>{"<thead><tr>" + th + "</tr></thead>" if th else ""}<tbody>{rows}</tbody></table>'
    if "check" in b:
        out = '<div class="sc"><div class="gl-h">Self-check</div><ol>'
        for q in b["check"]:
            n = len(keys) + 1
            letters = "abcd"
            opts = " &nbsp; ".join(f"({letters[i]}) {md(o)}" for i, o in enumerate(q["options"]))
            out += f'<li value="{n}">{md(q["q"])}<div class="q-opts" lang="el">{opts}</div></li>'
            right = letters[q["options"].index(q["answer"])]
            keys.append((n, ref, f'<strong>{n}.</strong> ({right}) {md(q["answer"])}' + (f' · {md(q["why"])}' if q.get("why") else "")))
        return out + "</ol></div>"
    return ""

def main():
    idx = json.load(open(f"{POS}/index.json", encoding="utf-8"))
    toc, body, keys = [], [], []
    for n, it in enumerate(idx["items"], 1):
        d = json.load(open(f"{POS}/{it['file']}", encoding="utf-8"))
        pid = f"pos-{d['id']}"
        toc.append(f'<li class="toc-p"><a href="#{pid}">{n}. {esc(d["title"])}</a> <span lang="el">· {esc(d["el"])}</span><ol>')
        body.append(f'<section class="part" id="{pid}"><div class="part-h"><div class="pn">Part {n} · {esc(d.get("span", ""))}</div>'
                    f'<h1>{esc(d["title"])}</h1><div class="pel" lang="el">{esc(d["el"])}</div></div>')
        body.append("".join(para(p) for p in d.get("intro", [])) if isinstance(d.get("intro"), list) else (para(d["intro"]) if d.get("intro") else ""))
        for i, s in enumerate(d["sections"]):
            sid = f"{pid}-{i}"
            toc.append(f'<li><a href="#{sid}">{esc(s["level"])} · {esc(s["title"])}</a></li>')
            inner = "".join(block(b, keys, f"{d['title']} · {s['title']}") for b in s["body"])
            body.append(f'<section class="lesson" id="{sid}"><h3 class="lt"><span lang="el"><span class="lvl">{esc(s["level"])}</span>{esc(s["el"])}</span>'
                        f'<span class="lt-en">{esc(s["title"])}</span></h3>{inner}</section>')
        toc.append("</ol></li>"); body.append("</section>")
    key_html = "".join(f"<p>{k}</p>" for _, _, k in keys)
    toc.append('<li class="toc-p"><a href="#answers">Answer key</a></li>')
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Answers</div><h1>Answer key</h1><div class="pel" lang="el">Λύσεις</div></div><div class="key">{key_html}</div></section>')
    credits = ("<section class='part' id='credits'><h2 class='unit'>Sources and credits</h2>"
               "<p>Written for the Ελληνικά app, for personal, non-commercial study, drawing on:</p><ul>"
               "<li>D. Holton, P. Mackridge, I. Philippaki-Warburton, V. Spyropoulos, <em>Greek: An Essential Grammar</em> (Routledge), used for personal study only.</li>"
               "<li>Ε. Πουλοπούλου (Poulopoulou), <em>Modern Greek: Grammar Notes for Absolute Beginners</em>, CC BY-NC-SA. Material derived from it is shared under the same licence, non-commercially.</li></ul></section>")
    cover = ('<section class="cover"><div class="c-top">Ελληνικά · Companion textbook</div><div class="c-lvl" lang="el">Τα μέρη του λόγου</div>'
             '<div class="c-name">Grammar by part of speech</div>'
             f'<p class="c-blurb">{len(idx["items"])} parts of speech, each taken from its simplest uses at A1 to the learned forms of C1, '
             f'with tables, glossed examples and {len(keys)} self-check questions.</p>'
             f'<div class="c-foot">A1–C1 · built {datetime.date.today().isoformat()}</div></section>')
    toc_html = f'<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(toc)}<li class="toc-p"><a href="#credits">Sources and credits</a></li></ol></section>'
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ελληνικά · Grammar by part of speech</title><style>{CSS}{EXTRA_CSS}</style></head>'
           f'<body>{cover}{toc_html}{"".join(body)}{credits}</body></html>')
    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/Parts of speech.html", "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"POS: {len(idx['items'])} documents, {len(keys)} questions, {len(doc) // 1024} KB html")

if __name__ == "__main__":
    main()
