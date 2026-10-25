#!/usr/bin/env python3
"""Greek reader: the companion volume to the app's Reader shelf (library/reader/*.json), with its public-domain pictures.

Usage: python3 build_reader.py [--app <app dir>] [--out <dir>]   writes "<dir>/Reader.html"
Then:  node render_pdf.js <dir> <dir> Reader, then compress.py into downloads/textbook/Ellinika-Reader-companion.pdf
Kept separate from build_textbook.py (the level volumes) so the two can change independently.
"""
import datetime, html, json, os, re, sys

ROOT = "/mnt/project-files"
APP = sys.argv[sys.argv.index("--app") + 1] if "--app" in sys.argv else f"{ROOT}/app"
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else f"{ROOT}/downloads/textbook/build"
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, "textbook.css"), encoding="utf-8").read().replace('url("fonts/', f'url("file://{HERE}/fonts/')
EXTRA_CSS = """
.cover.rdr { background: linear-gradient(160deg, #3a1f12 0%, #7a3b1d 55%, #b5532a 100%); }
.cover.rdr .c-lvl { font-size: 64pt; margin-top: 18mm; }
.c-img { margin-top: 12mm; max-width: 150mm; max-height: 95mm; border: 3px solid rgba(255,255,255,0.85); align-self: flex-start; }
.c-cap { font-size: 8pt; opacity: 0.7; margin-top: 2mm; }
.sec-intro { font-size: 10.5pt; }
.text { page-break-before: always; }
.text-h { display: flex; gap: 4mm; align-items: baseline; border-bottom: 2px solid var(--accent2); padding-bottom: 1.5mm; margin-bottom: 3mm; }
.text-h h2 { font-size: 17pt; margin: 0; color: var(--accent); }
.text-h .en { font-size: 10pt; }
.lvl { display: inline-block; font: 700 8.5pt "TBSans", sans-serif; color: #fff; background: var(--accent2); border-radius: 3px; padding: 1px 6px; }
.by { font-family: "TBSans", sans-serif; font-size: 9pt; color: var(--muted); margin: -1mm 0 3mm; }
figure.pic { margin: 0 0 4mm; text-align: center; break-inside: avoid; }
figure.pic img { max-width: 100%; max-height: 92mm; }
figure.pic figcaption { font-size: 8pt; color: var(--muted); margin-top: 1.2mm; }
.rd.poem p { white-space: pre-line; text-align: left; font-style: italic; margin-bottom: 1em; }
.trans.poem p { white-space: pre-line; }
.src { font-size: 8pt; color: var(--muted); margin-top: 2mm; }
.qs ol { margin: 1mm 0; } .qs li { margin: 1.4mm 0; break-inside: avoid; }
.qs .q-opts { font-size: 9pt; color: #3c4658; }
.vw { font-size: 8.8pt; color: var(--muted); }
table.cred { font-size: 7.8pt; }
table.cred td { padding: 0.8mm 1.4mm; }
"""

def esc(s):
    return html.escape("" if s is None else str(s), quote=True)

def md(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s

def gloss_box(g):
    if not g: return ""
    items = []
    for form, v in g.items():
        lemma, _, mean = v.partition(" — ")
        head = esc(form) if lemma.strip() == form else f"{esc(form)} <span class='sub'>({esc(lemma)})</span>"
        items.append(f"<li><strong lang='el'>{head}</strong> {esc(mean or lemma)}</li>")
    return f'<div class="gloss"><div class="gl-h">Glossary</div><ul>{"".join(items)}</ul></div>'

def figure(img):
    if not img: return ""
    path = os.path.join(APP, img["file"])
    if not os.path.exists(path): return ""
    cred = ", ".join(x for x in (img.get("credit"), img.get("license")) if x)
    return f'<figure class="pic"><img src="file://{esc(path)}"><figcaption><span lang="el">{esc(img.get("caption"))}</span>{" · " + esc(cred) if cred else ""}</figcaption></figure>'

def main():
    idx = json.load(open(f"{APP}/library/reader/index.json", encoding="utf-8"))
    toc, body, keys, creds = [], [], [], []
    n_text = 0
    for si, sec in enumerate(idx["sections"], 1):
        items = [x for x in idx["items"] if x["section"] == sec["id"]]
        sid = f"sec-{sec['id']}"
        toc.append(f'<li class="toc-p"><a href="#{sid}">{si}. {esc(sec["title"])}</a> <span lang="el">· {esc(sec["el"])}</span><ol>')
        body.append(f'<section class="part" id="{sid}"><div class="part-h"><div class="pn">Part {si} · {len(items)} texts</div>'
                    f'<h1 lang="el">{esc(sec["el"])}</h1><div class="pel">{esc(sec["title"])}</div></div>'
                    f'<ol class="sec-intro">{"".join(f"<li><span class=lvl>{esc(x["level"])}</span> <span lang=el>{esc(x["el"])}</span> <span class=en>{esc(x["title"])}</span></li>" for x in items)}</ol></section>')
        for it in items:
            d = json.load(open(f"{APP}/library/reader/{it['file']}", encoding="utf-8"))
            n_text += 1
            tid = f"t-{it['id']}"
            poem = " poem" if d.get("form") == "poem" else ""
            toc.append(f'<li><a href="#{tid}">{esc(d["level"])} · <span lang="el">{esc(d["el"])}</span></a></li>')
            qs = ""
            if d.get("questions"):
                qs = '<div class="qs"><div class="gl-h">Questions</div><ol>'
                for q in d["questions"]:
                    k = len(keys) + 1
                    opts = " &nbsp; ".join(f"({'abcd'[i]}) {esc(o)}" for i, o in enumerate(q["options"]))
                    qs += f'<li value="{k}" lang="el">{esc(q["q"])}<div class="q-opts">{opts}</div></li>'
                    keys.append(f'<strong>{k}.</strong> ({"abcd"[q["options"].index(q["answer"])]}) <span lang="el">{esc(q["answer"])}</span>')
                qs += "</ol></div>"
            if d.get("image"):
                creds.append(d)
            body.append(
                f'<section class="text" id="{tid}"><div class="text-h"><span class="lvl">{esc(d["level"])}</span><h2 lang="el">{esc(d["el"])}</h2><span class="en">{esc(d["title"])}</span></div>'
                + (f'<div class="by" lang="el">{esc(d["author"])}</div>' if d.get("author") else "")
                + figure(d.get("image"))
                + f'<div class="rd{poem}" lang="el">{"".join(f"<p>{esc(p["el"])}</p>" for p in d["paras"])}</div>'
                + (f'<div class="notes culture"><div class="gl-h">Notes</div><ul>{"".join(f"<li>{md(x)}</li>" for x in d["notes"])}</ul></div>' if d.get("notes") else "")
                + gloss_box(d.get("gloss"))
                + qs
                + (f'<p class="vw"><strong>Words to keep:</strong> <span lang="el">{esc(" · ".join(d["vocab"]))}</span></p>' if d.get("vocab") else "")
                + (f'<div class="trans{poem}"><div class="gl-h">Translation</div>{"".join(f"<p>{esc(p.get("en"))}</p>" for p in d["paras"])}</div>' if any(p.get("en") for p in d["paras"]) else "")
                + (f'<p class="src" lang="el">{esc(d["source"])}</p>' if d.get("source") else "")
                + "</section>")
        toc.append("</ol></li>")
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Answers</div><h1>Answer key</h1><div class="pel" lang="el">Λύσεις</div></div><div class="key">{"".join(f"<p>{k}</p>" for k in keys)}</div></section>')
    rows = "".join(f'<tr><td lang="el">{esc(d["el"])}</td><td lang="el">{esc(d["image"].get("caption"))}</td><td>{esc(d["image"].get("credit"))}</td><td>{esc(d["image"].get("license"))}</td><td>{esc(d["image"].get("source"))}</td></tr>' for d in creds)
    body.append(f'<section class="part" id="credits"><h2 class="unit">Pictures and sources</h2>'
                f'<p>Every picture is in the public domain or released under CC0 by its museum: The Metropolitan Museum of Art (Open Access), the Cleveland Museum of Art (Open Access) and Wikimedia Commons (works whose authors died long ago, or faithful photographs of them).</p>'
                f'<table class="cred"><thead><tr><th>Text</th><th>Picture</th><th>From</th><th>Licence</th><th>Source</th></tr></thead><tbody>{rows}</tbody></table>'
                f'<p>The texts were written in modern Greek for the Ελληνικά app, for personal, non-commercial study. Poems and folk songs are given in full from public-domain editions on Βικιθήκη (Greek Wikisource), in monotonic spelling; their sources are named under each text.</p></section>')
    cover_img = next((d["image"] for d in creds if d["image"]["file"].endswith("legacy-parthenon.jpg")), creds[0]["image"] if creds else None)
    cover = ('<section class="cover rdr"><div class="c-top">Ελληνικά · Companion reader</div><div class="c-lvl" lang="el">Ανθολόγιο</div>'
             '<div class="c-name">Greek reader: myths, stories, poems and ideas</div>'
             f'<p class="c-blurb">{n_text} graded texts in modern Greek, A2 to C1: Greek myths retold, famous short stories and fables, poems and folk songs, '
             'the philosophers, what the ancient Greeks gave politics, science, medicine, architecture and culture, Greek history and cultural musings. '
             f'Each with notes, a glossary, questions ({len(keys)} in all, answers at the back) and a translation.</p>'
             + (f'<img class="c-img" src="file://{esc(os.path.join(APP, cover_img["file"]))}"><div class="c-cap" lang="el">{esc(cover_img.get("caption"))}</div>' if cover_img else "")
             + f'<div class="c-foot">A2–C1 · built {datetime.date.today().isoformat()}</div></section>')
    toc_html = f'<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(toc)}<li class="toc-p"><a href="#answers">Answer key</a></li><li class="toc-p"><a href="#credits">Pictures and sources</a></li></ol></section>'
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ελληνικά · Greek reader</title><style>{CSS}{EXTRA_CSS}</style></head>'
           f'<body>{cover}{toc_html}{"".join(body)}</body></html>')
    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/Reader.html", "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"Reader: {n_text} texts, {len(creds)} pictures, {len(keys)} questions, {len(doc) // 1024} KB html")

if __name__ == "__main__":
    main()
