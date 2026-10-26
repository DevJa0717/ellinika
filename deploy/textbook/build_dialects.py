#!/usr/bin/env python3
"""Dialects of Modern Greek: a standalone companion volume built from app/library/dialects/*.json.

Usage: python3 build_dialects.py --out <dir>   writes "<dir>/Dialects.html" (copies fonts next to it)
Then:  node render_pdf.js <dir> <dir> Dialects, then compress.py into downloads/textbook/Ellinika-Dialects.pdf
The maps are drawn from map.json with the same projection as dialects.js. Recordings are embedded in the app,
so the book lists them with their YouTube links, citations and (for subtitled clips) the full transcript.
"""
import datetime, html, json, os, re, shutil, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from covers_el import el_date, el_level

ROOT = "/mnt/project-files"
DL = f"{ROOT}/app/library/dialects"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else f"{ROOT}/downloads/textbook/build"
CSS = open(os.path.join(HERE, "textbook.css"), encoding="utf-8").read()
EXTRA_CSS = """
.lead { font-size: 11pt; }
dl.facts { display: grid; grid-template-columns: 30mm 1fr; gap: 1.2mm 4mm; margin: 3mm 0 4mm; padding: 3mm 4mm; background: var(--soft); border-radius: 2mm; break-inside: avoid; }
dl.facts dt { font: 700 8.5pt "TBSans", sans-serif; color: var(--accent2); text-transform: uppercase; letter-spacing: .04em; }
dl.facts dd { margin: 0; }
figure.map { margin: 3mm 0 4mm; break-inside: avoid; }
figure.map svg { width: 100%; height: auto; display: block; border: 1px solid var(--line); border-radius: 2mm; background: #eaf2fa; }
figure.map .land { fill: #f4efe4; stroke: #b9b2a0; stroke-width: .6; }
figure.map .greek { fill: #e3dccb; stroke: #a99f88; stroke-width: .6; }
figure.map text { font: 600 12px "TBSans", sans-serif; fill: #1b2233; paint-order: stroke; stroke: #fff; stroke-width: 3px; }
figure.map .dim circle { opacity: .35; }
figcaption { font-size: 8.5pt; color: var(--muted); margin-top: 1mm; }
ul.legend { list-style: none; padding: 0; display: flex; flex-wrap: wrap; gap: 1mm 5mm; font: 8.5pt "TBSans", sans-serif; }
ul.legend i { display: inline-block; width: 3mm; height: 3mm; border-radius: 50%; margin-right: 1.5mm; vertical-align: -0.3mm; }
ol.tl { list-style: none; padding: 0; border-left: 2px solid var(--line); margin-left: 1mm; }
ol.tl li { padding: 0 0 2mm 4mm; break-inside: avoid; }
ol.tl b { display: block; font: 700 9pt "TBSans", sans-serif; color: var(--accent2); }
.ex-l { list-style: none; padding: 0; }
.ex-l li { border-left: 3px solid var(--accent2); padding: 0.5mm 0 0.5mm 3mm; margin: 0 0 2mm; break-inside: avoid; }
.ex-l .d { font-size: 10.5pt; }
.ex-l .s, .ex-l .e { display: block; font-size: 9pt; color: var(--muted); }
.ex-l .s::before { content: "Standard: "; font: 700 7.5pt "TBSans", sans-serif; text-transform: uppercase; }
.yes { color: #2e7d4f; font-weight: 700; } .part-y { color: #b5781a; font-weight: 700; } .no { color: #9aa2b1; }
.sample { background: var(--warm); padding: 3mm 4mm; border-radius: 2mm; margin: 4mm 0; }
.sample .ln { margin: 0; }
.sample .tr-en { margin-top: 2mm; color: var(--muted); font-style: italic; }
.culture { border-left: 3px solid #b8892b; background: #fbf6ea; padding: 2mm 4mm; margin: 4mm 0; }
.clip { border: 1px solid var(--line); border-radius: 2mm; padding: 3mm 4mm; margin: 3mm 0; }
.clip h4 { margin-top: 0; }
.clip .cite { font-size: 8.3pt; color: var(--muted); }
table.cues td { font-size: 8.8pt; } table.cues td.t { white-space: nowrap; color: var(--muted); font-family: "TBSans", sans-serif; width: 9mm; }
table.cues .tr { display: block; color: var(--muted); font-size: 8.3pt; }
.qs ol { margin: 0; } .qs li { margin: 1.5mm 0; break-inside: avoid; } .qs .q-opts { color: #3c4658; }
ol.src { font-size: 8.8pt; } ol.src a { word-break: break-all; }
.glos { columns: 2; column-gap: 8mm; font-size: 8.8pt; }
div.keep { break-inside: avoid; display: block; }\n.newpage { break-before: page; }
.glos p { margin: 0 0 1mm; break-inside: avoid; }
"""

def esc(s): return html.escape("" if s is None else str(s), quote=True)

def md(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s

def noTap(t): return re.sub(r"\s*[^.]*\bTap\b[^.]*\.", "", str(t))  # screen-only instructions

def paras(t): return "".join(f"<p>{md(p)}</p>" for p in str(t).split("\n\n") if p.strip())

def map_svg(m, idx, focus=None):
    col = {g["id"]: g["color"] for g in idx["groups"]}
    W, N, K, SC = float(m["W"]), float(m["N"]), float(m["K"]), float(m["SC"])
    out = []
    for k in idx["markers"]:
        x, y = (k["lon"] - W) * K * SC, (N - k["lat"]) * SC
        on = not focus or k["id"] in focus
        big = bool(focus) and on
        dx = k.get("dx", 9); anchor = "end" if dx < 0 else "start"
        body = f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{7.5 if big else 5.5}" fill="{col.get(k["group"], "#888")}"/>'
        if k.get("label") and on:
            body += f'<text x="{x + dx:.1f}" y="{y + k.get("dy", 4):.1f}" text-anchor="{anchor}">{esc(k["label"])}</text>'
        out.append(f'<g class="{"" if on else "dim"}">{body}</g>')
    return (f'<svg viewBox="0 0 {m["w"]} {m["h"]}"><path class="land" d="{m["land"]}"/><path class="greek" d="{m["greek"]}"/>{"".join(out)}</svg>')

def cell(c):
    s = str(c if c is not None else "")
    return {"✓": '<span class="yes">✓</span>', "~": '<span class="part-y">~</span>', "–": '<span class="no">–</span>'}.get(s.strip(), md(s))

def section(s):
    h = ""
    if s.get("h"): h += f'<h4>{esc(s["h"])}{f" <span class=sub lang=el>· {esc(s[chr(101)+chr(108)])}</span>" if s.get("el") else ""}</h4>'
    if s.get("text"): h += paras(s["text"])
    if s.get("timeline"): h += '<ol class="tl">' + "".join(f'<li><b>{esc(t["when"])}</b>{md(t["text"])}</li>' for t in s["timeline"]) + "</ol>"
    if s.get("table"):
        t = s["table"]
        keep = len(t["rows"]) <= 18
        h += ('<div class="keep"><table>' if keep else "<table>") + ("<thead><tr>" + "".join(f"<th>{esc(c)}</th>" for c in t["head"]) + "</tr></thead><tbody>"
              + "".join("<tr>" + "".join(f"<td>{cell(c)}</td>" for c in r) + "</tr>" for r in t["rows"]) + "</tbody></table>") + ("</div>" if keep else "")
    if s.get("examples"):
        h += '<ul class="ex-l">' + "".join(f'<li><span class="d" lang="el">{esc(x["el"])}</span>'
             + (f'<span class="s" lang="el">{esc(x["std"])}</span>' if x.get("std") else "")
             + (f'<span class="e">{esc(x["en"])}</span>' if x.get("en") else "") + "</li>" for x in s["examples"]) + "</ul>"
    if s.get("notes"): h += "<ul>" + "".join(f"<li>{md(n)}</li>" for n in s["notes"]) + "</ul>"
    if s.get("after"): h += f"<p>{md(s['after'])}</p>"
    grid = s.get("table") and len(s["table"]["rows"]) > 10 and any(str(c).strip() in ("✓", "~", "–") for r in s["table"]["rows"] for c in r)
    return f'<section class="lesson{" newpage" if grid else ""}">{h}</section>'

def mmss(t): return f"{int(t // 60)}:{int(t % 60):02d}"

def listen(L):
    h = f'<h3>{esc(L.get("h", "Listen"))}</h3>' + (f"<p>{md(noTap(L['intro']))}</p>" if L.get("intro") else "")
    h += "<p class='sub'>In the app these recordings play inside the page, with subtitles you can tap. Here each one is listed with its link.</p>"
    for c in L["clips"]:
        url = f"https://www.youtube.com/watch?v={c['yt']}"
        h += (f'<div class="clip"><h4>{f"<span lang=el>{esc(c[chr(101)+chr(108)])}</span> · " if c.get("el") else ""}{esc(c["title"])}</h4>'
              + (f"<p>{md(c['who'])}</p>" if c.get("who") else "")
              + f'<p>Watch: <a href="{url}">{url}</a></p>'
              + (f"<p><strong>Listen for:</strong> {md(c['listenFor'])}</p>" if c.get("listenFor") else ""))
        if c.get("cues"):
            h += ('<table class="cues"><tbody>' + "".join(
                f'<tr><td class="t">{mmss(q["t"])}</td><td lang="el">{esc(q["el"])}<span class="tr">{esc(q.get("tr", ""))}</span></td><td class="en">{esc(q.get("en", ""))}</td></tr>'
                for q in c["cues"]) + "</tbody></table>")
        elif c.get("note"):
            h += f"<p class='sub'>{md(c['note'])}</p>"
        h += f'<p class="cite">{esc(c["cite"])}</p></div>'
    if L.get("render") and any(c.get("cues") for c in L["clips"]):
        h += f"<p class='sub'>{md(L['render'])} Each transcript row gives the Greek-script line, VLACH's transcription under it, and the English.</p>"
    return h

def main():
    idx = json.load(open(f"{DL}/index.json", encoding="utf-8"))
    m = json.load(open(f"{DL}/map.json", encoding="utf-8"))
    groups = {g["id"]: g for g in idx["groups"]}
    toc, body, keys = [], [], []
    legend = '<ul class="legend">' + "".join(f'<li><i style="background:{g["color"]}"></i>{esc(g["en"])}</li>' for g in idx["groups"]) + "</ul>"
    body.append('<section class="part" id="map"><div class="part-h"><div class="pn">Overview</div><h1>The dialect map</h1>'
                '<div class="pel" lang="el">Ο χάρτης των διαλέκτων</div></div>'
                + (paras(noTap(idx["intro"])) if idx.get("intro") else "")
                + f'<figure class="map">{map_svg(m, idx)}<figcaption>{md(noTap(idx.get("mapCaption", "")))}</figcaption></figure>{legend}</section>')
    toc.append('<li class="toc-p"><a href="#map">The dialect map</a></li>')
    for n, it in enumerate(idx["items"], 1):
        d = json.load(open(f"{DL}/{it['file']}", encoding="utf-8"))
        pid = f"d-{d['id']}"; g = groups.get(it["group"], {})
        toc.append(f'<li class="toc-p"><a href="#{pid}">{n}. {esc(d["title"])}</a> <span lang="el">· {esc(d["el"])}</span></li>')
        h = (f'<section class="part" id="{pid}"><div class="part-h"><div class="pn">Chapter {n} · {esc(g.get("en", ""))}{" · " + esc(d["status"]) if d.get("status") else ""}</div>'
             f'<h1 lang="el">{esc(d["el"])}</h1><div class="pel">{esc(d["title"])}</div></div>')
        if d.get("lead"): h += f'<p class="lead">{md(d["lead"])}</p>'
        if d.get("facts"): h += '<dl class="facts">' + "".join(f"<dt>{esc(k)}</dt><dd>{md(v)}</dd>" for k, v in d["facts"]) + "</dl>"
        if d.get("markers"): h += f'<figure class="map">{map_svg(m, idx, d["markers"])}</figure>'
        h += "".join(section(s) for s in d.get("sections", []))
        if d.get("sample"):
            s = d["sample"]
            h += (f'<div class="sample"><h4>{esc(s.get("h", "Sample text"))}</h4>' + (f"<p class='sub'>{md(noTap(s['intro']))}</p>" if s.get("intro") else "")
                  + '<div lang="el">' + "".join(f'<p class="ln">{esc(l)}</p>' for l in s["lines"]) + "</div>"
                  + ('<div class="tr-en">' + "".join(f'<p class="ln">{esc(l)}</p>' for l in s["en"]) + "</div>" if s.get("en") else "")
                  + ("<ul>" + "".join(f"<li>{md(x)}</li>" for x in s["notes"]) + "</ul>" if s.get("notes") else "")
                  + (f"<p class='sub'>{md(s['source'])}</p>" if s.get("source") else "") + "</div>")
        if d.get("listen"): h += listen(d["listen"])
        if d.get("culture"): h += f'<div class="culture"><h4>{esc(d["culture"].get("h", "Culture"))}</h4>{paras(d["culture"]["text"])}</div>'
        if d.get("questions"):
            h += '<div class="qs sc"><div class="gl-h">Check your understanding</div><ol>'
            for q in d["questions"]:
                k = len(keys) + 1; L = "abcdef"
                opts = " &nbsp; ".join(f"({L[i]}) {md(o)}" for i, o in enumerate(q["options"]))
                h += f'<li value="{k}">{md(q["q"])}<div class="q-opts">{opts}</div></li>'
                right = L[q["options"].index(q["answer"])]
                keys.append((d["el"], f'<strong>{k}.</strong> ({right}) {md(q["answer"])}' + (f' · {md(q["why"])}' if q.get("why") else "")))
            h += "</ol></div>"
        if d.get("gloss"):
            gl = {k: v for k, v in d["gloss"].items()}
            for c in (d.get("listen") or {}).get("clips", []): gl.update(c.get("gloss") or {})
            h += '<h4>Glossary</h4><div class="glos">' + "".join(f'<p><span lang="el"><strong>{esc(k)}</strong></span> {esc(v)}</p>' for k, v in sorted(gl.items(), key=lambda x: x[0].lower())) + "</div>"
        if d.get("sources"):
            h += '<h4>Sources</h4><ol class="src">' + "".join(f'<li>{esc(s["label"])}' + (f' · <a href="{esc(s["url"])}">{esc(s["url"])}</a>' if s.get("url") else "") + (f' · {esc(s["note"])}' if s.get("note") else "") + "</li>" for s in d["sources"]) + "</ol>"
        body.append(h + "</section>")
    key_html, last = "", None
    for el, k in keys:
        if el != last: key_html += f'<h4 lang="el">{esc(el)}</h4>'; last = el
        key_html += f"<p>{k}</p>"
    toc.append('<li class="toc-p"><a href="#answers">Answer key</a></li>')
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Answers</div><h1>Answer key</h1><div class="pel" lang="el">Λύσεις</div></div><div class="key">{key_html}</div></section>')
    credits = ("<section class='part' id='credits'><h2 class='unit'>Sources and credits</h2>"
               "<p>Written for the Ελληνικά app, for personal, non-commercial study. Each chapter lists its own sources. The main ones are the dialect chapters of the Portal for the Greek Language (Centre for the Greek Language), Trudgill (2003), Horrocks (2010), Browning, Kontosopoulos, Dawkins (1916), Rohlfs and Sitaridou.</p>"
               "<p>The maps are drawn from Natural Earth outlines (public domain). Sample texts are traditional or long out of copyright.</p>"
               "<p>Recordings: Vanishing Languages and Cultural Heritage (VLACH), Austrian Academy of Sciences (www.oeaw.ac.at/vlach). The transcriptions and English translations are VLACH's and are cited under each clip. The Greek-script lines are the app's rendering of those transcriptions.</p></section>")
    cover = ('<section class="cover" lang="el"><div class="c-top">Ελληνικά · Συνοδευτικός τόμος</div><div class="c-lvl" style="font-size:64pt">Διάλεκτοι</div>'
             '<div class="c-name">Οι διάλεκτοι της νέας ελληνικής</div>'
             f'<p class="c-blurb">Από πού προήλθαν οι διάλεκτοι και πώς τις αναγνωρίζουμε: ιστορία, ταξινόμηση και {len(idx["items"]) - 2} διαλεκτικές περιοχές, '
             f'με χάρτες, πίνακες χαρακτηριστικών, δείγματα κειμένων, ηχογραφήσεις αρχείου με απομαγνητοφωνήσεις και {len(keys)} ερωτήσεις με τις απαντήσεις τους.</p>'
             f'<div class="c-foot">Έκδοση {el_date()}</div></section>')
    toc_html = f'<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(toc)}<li class="toc-p"><a href="#credits">Sources and credits</a></li></ol></section>'
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ελληνικά · Dialects of Modern Greek</title><style>{CSS}{EXTRA_CSS}</style></head>'
           f'<body>{cover}{toc_html}{"".join(body)}{credits}</body></html>')
    os.makedirs(OUT, exist_ok=True)
    if not os.path.exists(f"{OUT}/fonts"): shutil.copytree(os.path.join(HERE, "fonts"), f"{OUT}/fonts")
    with open(f"{OUT}/Dialects.html", "w", encoding="utf-8") as f: f.write(doc)
    print(f"Dialects: {len(idx['items'])} chapters, {len(keys)} questions, {len(doc) // 1024} KB html")

if __name__ == "__main__":
    main()
