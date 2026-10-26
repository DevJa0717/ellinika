#!/usr/bin/env python3
"""Companion PDFs for the Word families (#families) and False friends (#confusables) shelves.

Usage: python3 build_wordfamilies.py [--app <app root>] [--out <dir for PDFs>]
Writes Ellinika-Word-families.pdf and Ellinika-False-friends.pdf. The cover (Greek only, no footer) and the
body (with a page footer) are printed separately with Chromium and joined with pikepdf, then compressed.
Data: library/families/*.json, library/confusables/*.json (built by tools/wordfamilies/build.py).
"""
import html, json, os, random, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from covers_el import el_date

APP = sys.argv[sys.argv.index("--app") + 1] if "--app" in sys.argv else os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(APP, "downloads", "textbook")
CSS = open(os.path.join(HERE, "textbook.css"), encoding="utf-8").read().replace('url("fonts/', f'url("file://{HERE}/fonts/')
EXTRA = """
.tip { border-left: 3px solid #b8892b; background: #fbf6ea; padding: 2mm 4mm; margin: 3mm 0; break-inside: avoid; }
.fam { margin: 5mm 0 6mm; break-inside: auto; }
.fam-h { display: flex; gap: 4mm; align-items: baseline; border-bottom: 1px solid var(--line); padding-bottom: 1mm; break-after: avoid; }
.fam-k { font-family: "TBSerif", serif; font-size: 15pt; color: #b5532a; font-weight: 700; }
.fam-m { font-family: "TBSans", sans-serif; font-size: 9.5pt; color: var(--ink); }
.fam-b { font-family: "TBSans", sans-serif; font-size: 8.5pt; color: var(--muted); }
table.mem { border: none; font-size: 9.4pt; margin: 1.5mm 0 2mm; }
table.mem td { border: none; border-bottom: 1px dotted var(--line); padding: 0.7mm 1.5mm; width: 25%; }
table.mem td.g { font-weight: 700; }
table.mem td.e { color: var(--muted); font-size: 8.6pt; }
.note { background: var(--soft); border-left: 3px solid var(--accent); padding: 1.5mm 3.5mm; margin: 2mm 0; font-size: 9.4pt; break-inside: avoid; }
.trap { font-family: "TBSans", sans-serif; color: #a33a2a; font-weight: 700; font-size: 9pt; text-transform: none; }
.set { margin: 4mm 0 5mm; break-inside: avoid; border-top: 1px solid var(--line); padding-top: 2mm; }
.set-w { display: flex; flex-wrap: wrap; gap: 2mm 7mm; margin: 1mm 0 1.5mm; }
.set-w span.g { font-size: 13pt; font-weight: 700; color: var(--accent); }
.set-w span.e { color: var(--muted); font-size: 9pt; }
.drill-l { columns: 2; column-gap: 8mm; font-size: 9.3pt; padding-left: 5mm; }
.drill-l li { break-inside: avoid; margin: 0 0 2mm; }
.drill-l .h { color: var(--muted); font-size: 8.2pt; }
.ln { display: inline-block; border-bottom: 1px solid #aab3c2; width: 40mm; height: 4mm; }
.gaps li { margin: 0 0 2.2mm; break-inside: avoid; }
.gaps .o { color: var(--muted); font-size: 9pt; }
"""

def esc(s):
    return html.escape("" if s is None else str(s), quote=True)

def md(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s

def block(b):
    if "p" in b: return f"<p>{md(b['p'])}</p>"
    if "tip" in b: return f'<div class="tip">{md(b["tip"])}</div>'
    if "list" in b: return "<ul>" + "".join(f"<li>{md(x)}</li>" for x in b["list"]) + "</ul>"
    if "ex" in b: return ex_table(b["ex"])
    if "table" in b:
        t = b["table"]
        th = "".join(f"<th>{md(h)}</th>" for h in t["head"])
        rows = "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in t["rows"])
        return f"<table><thead><tr>{th}</tr></thead><tbody>{rows}</tbody></table>"
    return ""

def ex_table(ex):
    if not ex: return ""
    rows = "".join(f'<tr><td class="el" lang="el">{md(x["el"])}</td><td class="en">{md(x["en"])}</td></tr>' for x in ex)
    return f'<table class="ex">{rows}</table>'

def cover(top, name, sub, blurb, foot):
    return (f'<section class="cover" lang="el"><div class="c-top">{esc(top)}</div><div class="c-lvl" style="font-size:54pt;margin-top:45mm">{esc(name)}</div>'
            f'<div class="c-name">{esc(sub)}</div><p class="c-blurb">{blurb}</p><div class="c-foot">{esc(foot)}</div></section>')

def page(title, body):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{esc(title)}</title><style>{CSS}{EXTRA}</style></head>'
            f'<body>{body}</body></html>')

def families():
    D = os.path.join(APP, "library", "families")
    idx = json.load(open(os.path.join(D, "index.json"), encoding="utf-8"))
    rnd = random.Random(7)
    toc, body, keys = [], [], []
    n_ex = 0
    for part in idx["parts"]:
        toc.append(f'<li class="toc-p">{esc(part["id"])}. <span lang="el">{esc(part["el"])}</span> · {esc(part["title"])}<ol>')
        for it in [x for x in idx["items"] if x["part"] == part["id"]]:
            d = json.load(open(os.path.join(D, it["file"]), encoding="utf-8"))
            cid = "f-" + d["id"]
            toc.append(f'<li><a href="#{cid}"><span lang="el">{esc(d["el"])}</span></a></li>')
            body.append(f'<section class="part" id="{cid}"><div class="part-h"><div class="pn">{esc(part["el"])} · {esc(d["level"])}</div>'
                        f'<h1 lang="el">{esc(d["el"])}</h1><div class="pel">{esc(d["title"])}</div></div>')
            body.append("".join(block(b) for b in d.get("intro", [])))
            for s in d.get("sections", []):
                body.append(f'<section class="lesson"><h3 class="lt"><span lang="el">{esc(s["el"])}</span><span class="lt-en">{esc(s["level"])} · {esc(s["title"])}</span></h3>'
                            + "".join(block(b) for b in s["body"]) + "</section>")
            for g in d["groups"]:
                cells = [f'<td class="g" lang="el">{esc(m["el"])}</td><td class="e">{esc(m["en"])}</td>' for m in g["members"]]
                rows = "".join("<tr>" + "".join(cells[i:i + 2]) + ("<td></td><td></td>" if len(cells[i:i + 2]) < 2 else "") + "</tr>" for i in range(0, len(cells), 2))
                body.append(f'<div class="fam"><div class="fam-h"><span class="fam-k" lang="el">{esc(g["key"])}</span><span class="fam-m">{esc(g["meaning"])}</span>'
                            + (f'<span class="fam-b">από <span lang="el">{esc(g["el"])}</span></span>' if g.get("el") else "") + "</div>"
                            f'<table class="mem">{rows}</table>' + (f'<div class="note">{md(g["note"])}</div>' if g.get("note") else "") + ex_table(g.get("ex")) + "</div>")
            pick = rnd.sample(d["drill"], min(16, len(d["drill"])))
            start = n_ex + 1
            body.append('<div class="exercises"><h4>Άσκηση · Say it in Greek</h4><p class="instr">Write the Greek word. The root or affix is given as a hint.</p>'
                        f'<ol class="drill-l" start="{start}">' + "".join(f'<li>{esc(x["en"])} <span class="h">(<span lang="el">{esc(x["hint"])}</span>)</span><br><span class="ln"></span></li>' for x in pick) + "</ol></div>")
            keys.append(f'<div class="keyblock"><h4 lang="el">{esc(d["el"])}</h4><p>' + "; ".join(f'<strong>{start + i}.</strong> <span lang="el">{esc(x["answer"])}</span>' for i, x in enumerate(pick)) + "</p></div>")
            n_ex += len(pick)
            body.append("</section>")
        toc.append("</ol></li>")
    toc.append('<li class="toc-p"><a href="#answers">Answer key · Λύσεις</a></li>')
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Λύσεις</div><h1>Answer key</h1></div><div class="key">{"".join(keys)}</div></section>')
    n_groups = sum(x["groups"] for x in idx["items"])
    cov = cover("Ελληνικά · Συνοδευτικό εγχειρίδιο", "Οικογένειες λέξεων", "Ρίζες, προθήματα και επιθήματα",
                f'{len(idx["items"])} κεφάλαια, {n_groups} οικογένειες και {idx["words"]} λέξεις: πώς χτίζεται μια ελληνική λέξη, τα προθήματα, τα επιθήματα και οι μεγάλες ρίζες, '
                f'με σημειώσεις, παραδείγματα και {n_ex} ασκήσεις παραγωγής.', f"Α2–Γ1 · Έκδοση {el_date()}")
    toc_html = f'<section class="toc"><h1>Contents · Περιεχόμενα</h1><ol class="toc-l">{"".join(toc)}</ol></section>'
    return cov, page("Ελληνικά · Οικογένειες λέξεων", toc_html + "".join(body)), n_ex

def confusables():
    D = os.path.join(APP, "library", "confusables")
    idx = json.load(open(os.path.join(D, "index.json"), encoding="utf-8"))
    rnd = random.Random(11)
    toc, body, keys = [], [], []
    n = 0; n_sets = 0
    for it in idx["items"]:
        d = json.load(open(os.path.join(D, it["file"]), encoding="utf-8"))
        cid = "c-" + d["id"]
        toc.append(f'<li class="toc-p"><a href="#{cid}"><span lang="el">{esc(d["el"])}</span></a> · {esc(d["title"])}</li>')
        body.append(f'<section class="part" id="{cid}"><div class="part-h"><div class="pn">{esc(d["level"])}</div><h1 lang="el">{esc(d["el"])}</h1><div class="pel">{esc(d["title"])}</div></div>')
        body.append("".join(f"<p>{md(p)}</p>" for p in d["intro"]))
        for p in d["pairs"]:
            n_sets += 1
            body.append('<div class="set">' + (f'<div class="trap">{esc(p["trap"])}</div>' if p.get("trap") else "")
                        + '<div class="set-w">' + "".join(f'<span><span class="g" lang="el">{esc(w["el"])}</span> <span class="e">{esc(w["en"])}</span></span>' for w in p["words"]) + "</div>"
                        f'<p>{md(p["note"])}</p>{ex_table(p["ex"])}</div>')
        gaps = [g for p in d["pairs"] for g in p["gaps"]]
        start = n + 1
        items = []
        for g in gaps:
            opts = [g["a"]] + g["o"]; rnd.shuffle(opts)
            items.append((g, opts))
        body.append('<div class="exercises"><h4>Άσκηση 1 · Choose the right word</h4>'
                    f'<ol class="gaps" start="{start}">' + "".join(
                        f'<li><span lang="el">{esc(g["s"]).replace("___", "<span class=ln style=width:22mm></span>")}</span><br><span class="o" lang="el">'
                        + " · ".join(f"({'abcd'[i]}) {esc(o)}" for i, o in enumerate(opts)) + "</span></li>" for g, opts in items) + "</ol>")
        keys_c = [f'<strong>{start + i}.</strong> ({"abcd"[opts.index(g["a"])]}) <span lang="el">{esc(g["a"])}</span>' for i, (g, opts) in enumerate(items)]
        n += len(items)
        prod = rnd.sample(d["produce"], min(10, len(d["produce"])))
        start2 = n + 1
        body.append(f'<h4>Άσκηση 2 · Say it in Greek</h4><ol class="drill-l" start="{start2}">' + "".join(f'<li>{esc(x["en"])}<br><span class="ln"></span></li>' for x in prod) + "</ol></div>")
        keys_c += [f'<strong>{start2 + i}.</strong> <span lang="el">{esc(x["answer"])}</span>' for i, x in enumerate(prod)]
        n += len(prod)
        keys.append(f'<div class="keyblock"><h4 lang="el">{esc(d["el"])}</h4><p>{"; ".join(keys_c)}</p></div>')
        body.append("</section>")
    toc.append('<li class="toc-p"><a href="#answers">Answer key · Λύσεις</a></li>')
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Λύσεις</div><h1>Answer key</h1></div><div class="key">{"".join(keys)}</div></section>')
    cov = cover("Ελληνικά · Συνοδευτικό εγχειρίδιο", "Ψευδόφιλοι και παρώνυμα", "Λέξεις που μπερδεύονται",
                f'{len(idx["items"])} κεφάλαια και {n_sets} ομάδες λέξεων: ψευδόφιλοι με τα αγγλικά, λέξεις με πολλές σημασίες, λέξεις που αλλάζουν με τον τόνο ή την ορθογραφία, '
                f'ρήματα και συνώνυμα που μπερδεύονται, με αντιθετικά παραδείγματα και {n} ασκήσεις.', f"Α1–Γ1 · Έκδοση {el_date()}")
    toc_html = f'<section class="toc"><h1>Contents · Περιεχόμενα</h1><ol class="toc-l">{"".join(toc)}</ol></section>'
    return cov, page("Ελληνικά · Ψευδόφιλοι και παρώνυμα", toc_html + "".join(body)), n

RENDER = r"""
const { chromium } = require("/opt/node22/lib/node_modules/playwright");
(async () => {
  const [src, out, footer] = process.argv.slice(2);
  const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" });
  const p = await b.newPage();
  await p.goto("file://" + src, { waitUntil: "load", timeout: 0 });
  await p.evaluate(() => document.fonts.ready);
  const opt = { path: out, format: "A4", printBackground: true, outline: true, tagged: true, preferCSSPageSize: true, timeout: 0 };
  if (footer) Object.assign(opt, { displayHeaderFooter: true, headerTemplate: "<span></span>",
    footerTemplate: `<div style="font-family:sans-serif;font-size:7.5pt;color:#7a8396;width:100%;padding:0 16mm;display:flex;justify-content:space-between"><span>${footer}</span><span class="pageNumber"></span></div>` });
  await p.pdf(opt); await b.close();
})();
"""

def render(cov_html, body_html, footer, pdf, title):
    import pikepdf
    tmp = tempfile.mkdtemp()
    js = os.path.join(tmp, "r.js"); open(js, "w").write(RENDER)
    c, bd = os.path.join(tmp, "cover.html"), os.path.join(tmp, "body.html")
    open(c, "w", encoding="utf-8").write(page(title, cov_html))
    # The body's first page must not use the cover's zero-margin @page :first rule.
    open(bd, "w", encoding="utf-8").write(body_html.replace("@page :first { margin: 0; }", ""))
    subprocess.run(["node", js, c, os.path.join(tmp, "c.pdf"), ""], check=True)
    subprocess.run(["node", js, bd, os.path.join(tmp, "b.pdf"), footer], check=True)
    with pikepdf.open(os.path.join(tmp, "b.pdf")) as b, pikepdf.open(os.path.join(tmp, "c.pdf")) as cv:
        b.pages.insert(0, cv.pages[0])
        b.docinfo["/Title"] = title
        os.makedirs(OUT, exist_ok=True)
        b.save(pdf, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate, recompress_flate=True)
    with pikepdf.open(pdf) as p:
        print(os.path.basename(pdf), len(p.pages), "pages", round(os.path.getsize(pdf) / 1048576, 1), "MB")

if __name__ == "__main__":
    cov, body, n = families()
    render(cov, body, "Ελληνικά · Οικογένειες λέξεων", os.path.join(OUT, "Ellinika-Word-families.pdf"), "Ελληνικά · Οικογένειες λέξεων")
    cov, body, n = confusables()
    render(cov, body, "Ελληνικά · Ψευδόφιλοι και παρώνυμα", os.path.join(OUT, "Ellinika-False-friends.pdf"), "Ελληνικά · Ψευδόφιλοι και παρώνυμα")
