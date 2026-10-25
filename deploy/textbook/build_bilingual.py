#!/usr/bin/env python3
"""Companion PDF for any bilingual reader shelf (shared format, app/bilingual.js): philosophers, istoria, simera, politeia …

Usage: python3 build_bilingual.py --shelf <id> [--app <app dir>] [--out <build dir>] [--pdf <final pdf path>]
  writes <out>/<shelf>.html; with --pdf it also renders it (render_pdf.js) and packs it (compress.py) into that path.
Example: python3 build_bilingual.py --shelf philosophers --pdf /mnt/project-files/downloads/textbook/Ellinika-Philosophers.pdf
Layout: cover (index title, intro, a picture), contents by part, part pages with dates and intro, then each chapter:
header, picture, "In brief", new terms, the sections with each Greek paragraph followed by its English (source numbers
in brackets), grammar notes, glossary (the chapter's tap-lookup glosses), questions, words to keep, sources.
At the back: answer key and picture credits. Needs pikepdf for --pdf (pip install pikepdf).
"""
import datetime, html, json, os, re, subprocess, sys

ROOT = "/mnt/project-files"
arg = lambda k, d=None: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
SHELF = arg("--shelf")
if not SHELF: sys.exit(__doc__)
APP = arg("--app", f"{ROOT}/app")
OUT = arg("--out", f"/tmp/bilingual-{SHELF}")
PDF = arg("--pdf")
HERE = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(HERE, "textbook.css"), encoding="utf-8").read().replace('url("fonts/', f'url("file://{HERE}/fonts/')
EXTRA_CSS = """
.cover.bl { background: linear-gradient(160deg, #0a2747 0%, #18436e 55%, #2f6b8f 100%); }
.cover.bl .c-lvl { font-size: 46pt; line-height: 1.1; margin-top: 16mm; }
.c-img { margin-top: 10mm; max-width: 150mm; max-height: 95mm; border: 3px solid rgba(255,255,255,0.85); align-self: flex-start; }
.c-cap { font-size: 8pt; opacity: 0.75; margin-top: 2mm; }
.p-dates { font: 600 10pt "TBSans", sans-serif; color: var(--accent2); margin: 2mm 0 4mm; }
.p-intro { font-size: 10.5pt; margin: 0 0 3mm; }
.p-intro.en { color: var(--muted); font-size: 9.5pt; }
.chap { page-break-before: always; }
.chap-h { border-bottom: 2px solid var(--accent2); padding-bottom: 1.5mm; margin-bottom: 3mm; }
.chap-h h2 { font-size: 20pt; margin: 1mm 0 0; color: var(--accent); }
.chap-h .en { font-size: 11pt; }
.chap-h .meta { font: 600 8.5pt "TBSans", sans-serif; color: var(--muted); }
.lvl { display: inline-block; font: 700 8.5pt "TBSans", sans-serif; color: #fff; background: var(--accent2); border-radius: 3px; padding: 1px 6px; margin-right: 2mm; }
.theme { display: inline-block; font: 600 8.5pt "TBSans", sans-serif; color: var(--accent); border: 1px solid var(--accent2); border-radius: 3px; padding: 0 5px; margin-right: 2mm; }
figure.pic { margin: 0 0 4mm; text-align: center; break-inside: avoid; }
figure.pic img { max-width: 100%; max-height: 95mm; }
figure.pic figcaption { font-size: 8pt; color: var(--muted); margin-top: 1.2mm; }
.brief { background: #f2f5f9; border-left: 3px solid var(--accent2); padding: 2.5mm 3.5mm; font-size: 9.8pt; margin: 0 0 4mm; break-inside: avoid; }
.box-h { font: 700 9pt "TBSans", sans-serif; text-transform: uppercase; letter-spacing: .05em; color: var(--accent2); margin: 0 0 1.5mm; }
.terms { border: 1px solid #cfd6e0; border-radius: 2mm; padding: 2.5mm 3.5mm; margin: 0 0 4mm; font-size: 9.5pt; }
.terms dl { margin: 0; columns: 2; column-gap: 6mm; }
.terms dt { font-weight: 700; break-after: avoid; }
.terms dt .en { font-weight: 400; }
.terms dd { margin: 0 0 2mm; break-inside: avoid; }
.terms dd .en { display: block; color: var(--muted); font-size: 8.8pt; }
h3.sec { font-size: 13pt; margin: 5mm 0 2mm; color: var(--accent); break-after: avoid; }
h3.sec .en { font-size: 10pt; font-weight: 400; margin-left: 2mm; }
.bp { margin: 0 0 3mm; }
.bp .gr { margin: 0; font-size: 10.8pt; line-height: 1.5; }
.bp .tr { margin: 1mm 0 0; padding-left: 3mm; border-left: 2px solid #d5dbe4; color: #3c4658; font-size: 9.2pt; line-height: 1.45; }
.cite { font: 600 7pt "TBSans", sans-serif; color: var(--accent2); vertical-align: super; }
.gram { margin: 4mm 0; break-inside: auto; }
.gram .g { border-top: 1px solid #d5dbe4; padding-top: 2mm; margin-top: 2mm; break-inside: avoid; font-size: 9.6pt; }
.gram h4 { margin: 0 0 1mm; font-size: 10.5pt; }
.gram ul { margin: 1mm 0 0; }
.gram li .en { display: block; font-size: 9pt; }
.gloss { columns: 2; column-gap: 6mm; font-size: 8.4pt; }
.gloss ul { margin: 0; padding-left: 0; list-style: none; }
.gloss li { margin: 0 0 0.6mm; break-inside: avoid; }
.qs ol { margin: 1mm 0; } .qs li { margin: 1.4mm 0; break-inside: avoid; }
.qs .q-opts { font-size: 9pt; color: #3c4658; }
.vw { font-size: 8.8pt; color: var(--muted); }
.srcs ol { font-size: 8.2pt; padding-left: 6mm; } .srcs li { margin: 0 0 1mm; overflow-wrap: anywhere; }
table.cred { font-size: 7.8pt; } table.cred td { padding: 0.8mm 1.4mm; overflow-wrap: anywhere; }
"""

def esc(s):
    return html.escape("" if s is None else str(s), quote=True)

def md(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)

def figure(img):
    if not img: return ""
    path = os.path.join(APP, img["file"])
    if not os.path.exists(path): return ""
    cred = " · ".join(x for x in (img.get("credit"), img.get("license")) if x)
    cap = esc(img.get("caption")) + (f" · {esc(img['caption_en'])}" if img.get("caption_en") else "")
    return f'<figure class="pic"><img src="file://{esc(path)}"><figcaption><span lang="el">{cap}</span><br>{esc(cred)}</figcaption></figure>'

def main():
    base = f"{APP}/library/{SHELF}"
    idx = json.load(open(f"{base}/index.json", encoding="utf-8"))
    themes = {t["id"]: t for t in idx.get("themes", [])}
    parts = idx.get("parts") or [{"id": None, "el": idx.get("el", ""), "en": idx.get("title", "")}]
    toc, body, keys, creds = [], [], [], []
    n = 0
    for pi, p in enumerate(parts, 1):
        items = [x for x in idx["items"] if p["id"] is None or x.get("part") == p["id"]]
        if not items: continue
        pid = f"part-{p['id'] or pi}"
        toc.append(f'<li class="toc-p"><a href="#{pid}">{pi}. <span lang="el">{esc(p.get("el"))}</span></a> <span class="en">· {esc(p.get("en"))}</span><ol>')
        body.append(f'<section class="part" id="{pid}"><div class="part-h"><div class="pn">Part {pi} · {len(items)} chapters</div>'
                    f'<h1 lang="el">{esc(p.get("el"))}</h1><div class="pel">{esc(p.get("en"))}</div></div>'
                    + (f'<div class="p-dates">{esc(p["dates"])}</div>' if p.get("dates") else "")
                    + (f'<p class="p-intro" lang="el">{esc(p["intro_el"])}</p>' if p.get("intro_el") else "")
                    + (f'<p class="p-intro en">{esc(p["intro_en"])}</p>' if p.get("intro_en") else "")
                    + f'<ol class="sec-intro">{"".join(f"<li><span class=lvl>{esc(x.get("level"))}</span> <span lang=el>{esc(x["el"])}</span> <span class=en>· {esc(x["title"])}</span></li>" for x in items)}</ol></section>')
        for it in items:
            c = json.load(open(f"{base}/{it['file']}", encoding="utf-8"))
            n += 1
            cid = f"c-{it['id']}"
            th = themes.get(c.get("theme") or it.get("theme"))
            toc.append(f'<li><a href="#{cid}">{esc(c.get("level") or it.get("level"))} · <span lang="el">{esc(c["el"])}</span></a> <span class="en">{esc(c["title"])}</span></li>')
            src_ok = {s["n"] for s in c.get("sources", [])}
            cite = lambda para: "".join(f'<span class="cite">[{k}]</span>' for k in para.get("cite", []) if k in src_ok)
            h = [f'<section class="chap" id="{cid}"><div class="chap-h"><div class="meta"><span class="lvl">{esc(c.get("level") or it.get("level"))}</span>'
                 + (f'<span class="theme" lang="el">{esc(th["el"])}</span>' if th else "")
                 + f'{esc(c.get("dates") or it.get("dates") or "")}</div><h2 lang="el">{esc(c["el"])}</h2><div class="en">{esc(c["title"])}</div></div>',
                 figure(c.get("image"))]
            if c.get("image") and os.path.exists(os.path.join(APP, c["image"]["file"])): creds.append(c)
            if c.get("summary_en"): h.append(f'<div class="brief"><div class="box-h">In brief</div>{md(c["summary_en"])}</div>')
            if c.get("terms"):
                h.append('<div class="terms"><div class="box-h">Νέοι όροι · New terms</div><dl>' + "".join(
                    f'<dt lang="el">{esc(t["el"])} <span class="en">· {esc(t.get("en"))}</span></dt><dd><span lang="el">{esc(t.get("def_el"))}</span><span class="en">{esc(t.get("def_en"))}</span></dd>'
                    for t in c["terms"]) + "</dl></div>")
            for s in c.get("sections", []):
                h.append(f'<h3 class="sec"><span lang="el">{esc(s["el"])}</span><span class="en">{esc(s.get("en"))}</span></h3>')
                for para in s.get("paras", []):
                    h.append(f'<div class="bp"><p class="gr" lang="el">{esc(para["el"])}{cite(para)}</p>'
                             + (f'<p class="tr">{esc(para["en"])}</p>' if para.get("en") else "") + "</div>")
            if c.get("grammar"):
                h.append('<div class="gram"><div class="box-h">Γραμματική · Grammar notes</div>' + "".join(
                    f'<div class="g"><h4>{f"<span class=lvl>{esc(g.get("level"))}</span>" if g.get("level") else ""}{esc(g["title"])}</h4>'
                    + (f'<p lang="el">{esc(g["el"])}</p>' if g.get("el") else "") + (f"<p>{md(g['en'])}</p>" if g.get("en") else "")
                    + (f'<ul>{"".join(f"<li><span lang=el>{esc(x["el"])}</span><span class=en>{esc(x.get("en"))}</span></li>" for x in g["examples"])}</ul>' if g.get("examples") else "")
                    + "</div>" for g in c["grammar"]) + "</div>")
            if c.get("gloss"):
                items_g = []
                for form, v in sorted(c["gloss"].items(), key=lambda kv: kv[0].lower()):
                    lemma, _, mean = v.partition(" — ")
                    head = esc(form) if lemma.strip() == form else f"{esc(form)} <span class='sub'>({esc(lemma)})</span>"
                    items_g.append(f"<li><strong lang='el'>{head}</strong> {esc(mean or lemma)}</li>")
                h.append(f'<div class="box-h">Glossary</div><div class="gloss"><ul>{"".join(items_g)}</ul></div>')
            if c.get("questions"):
                q = '<div class="qs"><div class="box-h">Ερωτήσεις · Questions</div><ol>'
                for x in c["questions"]:
                    k = len(keys) + 1
                    opts = " &nbsp; ".join(f"({'abcd'[i]}) {esc(o)}" for i, o in enumerate(x["options"]))
                    q += f'<li value="{k}" lang="el">{esc(x["q"])}<div class="q-opts">{opts}</div></li>'
                    keys.append(f'<strong>{k}.</strong> ({"abcd"[x["options"].index(x["answer"])]}) <span lang="el">{esc(x["answer"])}</span>' + (f' <span class="en">{esc(x["why"])}</span>' if x.get("why") else ""))
                h.append(q + "</ol></div>")
            if c.get("vocab"): h.append(f'<p class="vw"><strong>Words to keep:</strong> <span lang="el">{esc(" · ".join(c["vocab"]))}</span></p>')
            if c.get("sources"):
                h.append('<div class="srcs"><div class="box-h">Πηγές · Sources</div><ol>' + "".join(
                    f'<li value="{s["n"]}">{esc(s["text"])}{" " + esc(s["url"]) if s.get("url") else ""}</li>' for s in c["sources"]) + "</ol></div>")
            body.append("".join(h) + "</section>")
        toc.append("</ol></li>")
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Answers</div><h1>Answer key</h1><div class="pel" lang="el">Λύσεις</div></div><div class="key">{"".join(f"<p>{k}</p>" for k in keys)}</div></section>')
    rows = "".join(f'<tr><td lang="el">{esc(c["el"])}</td><td lang="el">{esc(c["image"].get("caption"))}</td><td>{esc(c["image"].get("credit"))}</td><td>{esc(c["image"].get("license"))}</td><td>{esc(c["image"].get("source"))}</td></tr>' for c in creds)
    body.append(f'<section class="part" id="credits"><h2 class="unit">Pictures</h2>'
                f'<p>Every picture is in the public domain, released under CC0 by its museum, or used under the free licence named beside it.</p>'
                f'<table class="cred"><thead><tr><th>Chapter</th><th>Picture</th><th>From</th><th>Licence</th><th>Source</th></tr></thead><tbody>{rows}</tbody></table>'
                f'<p>The texts were written in modern Greek and English for the Ελληνικά app, for personal, non-commercial study. Each chapter lists the sources its statements were checked against.</p></section>')
    cov = next((c["image"] for c in creds), None)
    cover = (f'<section class="cover bl"><div class="c-top">Ελληνικά · Bilingual reader</div><div class="c-lvl" lang="el">{esc(idx.get("el"))}</div>'
             f'<div class="c-name">{esc(idx.get("title"))}</div>'
             f'<p class="c-blurb">{esc(idx.get("intro_en"))} {n} chapters, {len(keys)} questions (answers at the back).</p>'
             + (f'<img class="c-img" src="file://{esc(os.path.join(APP, cov["file"]))}"><div class="c-cap" lang="el">{esc(cov.get("caption"))}</div>' if cov else "")
             + f'<div class="c-foot">Built {datetime.date.today().isoformat()} · devja0717.github.io/ellinika/#{esc(SHELF)}</div></section>')
    toc_html = f'<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(toc)}<li class="toc-p"><a href="#answers">Answer key</a></li><li class="toc-p"><a href="#credits">Pictures</a></li></ol></section>'
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ελληνικά · {esc(idx.get("el"))}</title><style>{CSS}{EXTRA_CSS}</style></head>'
           f'<body>{cover}{toc_html}{"".join(body)}</body></html>')
    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/{SHELF}.html", "w", encoding="utf-8") as f: f.write(doc)
    print(f"{SHELF}: {n} chapters, {len(creds)} pictures, {len(keys)} questions, {len(doc) // 1024} KB html -> {OUT}/{SHELF}.html")
    if PDF:
        subprocess.run(["node", os.path.join(HERE, "render_pdf.js"), OUT, OUT, SHELF], check=True, cwd=HERE)
        subprocess.run([sys.executable, os.path.join(HERE, "compress.py"), f"{OUT}/Ellinika-{SHELF}-textbook.pdf", PDF, f"Ελληνικά · {idx.get('el')}"], check=True)
        print("PDF:", PDF, f"{os.path.getsize(PDF) / 1048576:.1f} MB")

if __name__ == "__main__":
    main()
