#!/usr/bin/env python3
"""Writing workbook (Τετράδιο γραπτού λόγου): companion PDF built from library/tetradio/*.json.

Usage: python3 build_tetradio.py [--app <repo or app dir>] [--pdf <out.pdf>]
Default --app is the repository root this script lives in; default --pdf is downloads/textbook/Ellinika-Writing-workbook.pdf there.
Writes "<tmp>/Writing.html", prints it with render_pdf.js (Chromium) and packs it with compress.py (needs pikepdf).
Model answers go to an appendix so the printed tasks can be done before they are seen.
"""
import html, json, os, re, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from covers_el import el_date

arg = lambda k, d: sys.argv[sys.argv.index(k) + 1] if k in sys.argv else d
APP = arg("--app", os.path.normpath(os.path.join(HERE, "..", "..")))
PDF = arg("--pdf", os.path.join(APP, "downloads", "textbook", "Ellinika-Writing-workbook.pdf"))
SRC = os.path.join(APP, "library", "tetradio")
CSS = open(os.path.join(HERE, "textbook.css"), encoding="utf-8").read()
EXTRA = """
.tip { border-left: 3px solid #b8892b; background: #fbf6ea; padding: 6px 10px; margin: 8px 0; break-inside: avoid; }
.lvl { display: inline-block; font: 600 8pt sans-serif; color: #fff; background: #3e5c8a; border-radius: 3px; padding: 1px 5px; margin-right: 6px; vertical-align: middle; }
.reg { display: inline-block; font: 600 7pt sans-serif; border: 1px solid #9aa6b8; border-radius: 3px; padding: 0 3px; margin-left: 4px; color: #3c4658; }
.model { border: 1px solid #c9d2df; border-radius: 2mm; padding: 3mm 4mm; margin: 3mm 0; }
.model p { white-space: pre-line; margin: 0 0 2mm; }
.model .el p { font-size: 11pt; line-height: 1.5; }
.task { border-left: 3px solid #3e5c8a; padding: 1mm 0 1mm 4mm; margin: 4mm 0 2mm; break-inside: avoid; }
.lines { height: 62mm; background: repeating-linear-gradient(#fff 0 7.6mm, #c9d2df 7.6mm 7.8mm); margin: 2mm 0 5mm; break-inside: avoid; }
table.st th { text-align: left; width: 32%; font-weight: 600; }
.ck { list-style: none; padding-left: 0; } .ck li { margin: 2mm 0; padding-left: 7mm; position: relative; break-inside: avoid; }
.ck li::before { content: ""; position: absolute; left: 0; top: 1mm; width: 3.4mm; height: 3.4mm; border: 1px solid #3e5c8a; border-radius: 0.6mm; }
.wr { font-size: 9pt; color: #3c4658; } .wr s { color: #b0413e; }
.con td { font-size: 9.5pt; vertical-align: top; } .con td.el { width: 30%; }
.sc { margin: 8px 0; padding: 6px 10px; border: 1px dashed #b9c0cc; break-inside: avoid; }
.sc ol { margin: 4px 0 0; } .sc li { margin: 3px 0; } .sc .q-opts { color: #3c4658; }
"""

def esc(s): return html.escape("" if s is None else str(s), quote=True)
def md(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)

def block(b):
    if "p" in b: return f"<p>{md(b['p'])}</p>"
    if "tip" in b: return f'<div class="tip">{md(b["tip"])}</div>'
    if "list" in b: return "<ul>" + "".join(f"<li>{md(x)}</li>" for x in b["list"]) + "</ul>"
    if "table" in b:
        t = b["table"]
        return ("<table><thead><tr>" + "".join(f"<th>{md(h)}</th>" for h in t["head"]) + "</tr></thead><tbody>"
                + "".join("<tr>" + "".join(f"<td>{md(c)}</td>" for c in r) + "</tr>" for r in t["rows"]) + "</tbody></table>")
    return ""

def drills(lst, keys, ref):
    if not lst: return ""
    out = '<div class="sc"><div class="gl-h">Ασκήσεις · Quick check</div><ol>'
    for q in lst:
        n = len(keys) + 1
        opts = " &nbsp; ".join(f"({'abcd'[i]}) {esc(o)}" for i, o in enumerate(q["options"]))
        out += f'<li value="{n}" lang="el">{md(q["q"])}<div class="q-opts">{opts}</div></li>'
        keys.append(f'<strong>{n}.</strong> ({"abcd"[q["options"].index(q["answer"])]}) <span lang="el">{esc(q["answer"])}</span>' + (f' · {md(q["why"])}' if q.get("why") else "") + f' <span class="sub">({esc(ref)})</span>')
    return out + "</ol></div>"

def paras(ps, cls=""): return f'<div class="{cls}">' + "".join(f"<p>{md(p)}</p>" for p in ps) + "</div>"

def unit(d, keys, answers, tno):
    o = [''.join(block(b) for b in d.get("intro", []))]
    if d.get("structure"):
        o.append('<h4>Η δομή · Structure</h4><table class="st"><tbody>' + "".join(
            f'<tr><th><span lang="el">{esc(r[0])}</span><br><span class="sub">{esc(r[1])}</span></th><td>{md(r[2])}</td></tr>' for r in d["structure"]) + "</tbody></table>")
    for s in d.get("sections", []):
        o.append(f'<h4><span lang="el">{esc(s["el"])}</span> · {esc(s["en"])}</h4>' + "".join(block(b) for b in s["body"]))
    for m in d.get("models", []):
        o.append(f'<h4><span class="lvl">{esc(m["level"])}</span><span lang="el">{esc(m["el"])}</span> · Model text, {m["words"]} words</h4>'
                 f'<p class="sub" lang="el">{md(m["task_el"])}</p>'
                 + (f'<p class="sub"><em>Before:</em> <span lang="el">{md(m["before"])}</span></p>' if m.get("before") else "")
                 + f'<div class="model">{paras(m["text"], "el")}</div><div class="trans"><div class="gl-h">Translation</div>{paras(m["text_en"])}</div>'
                 + '<div class="notes"><div class="gl-h">Why it works</div><ul>' + "".join(f"<li>{md(n)}</li>" for n in m["notes"]) + "</ul></div>")
    for g in d.get("phrases", []):
        o.append(f'<h4><span lang="el">{esc(g["el"])}</span> · {esc(g["en"])}</h4><table class="ex">' + "".join(
            f'<tr><td class="el" lang="el">{esc(x["el"])}{f"<span class=reg>{x["reg"]}</span>" if x.get("reg") else ""}</td><td class="en">{esc(x["en"])}</td></tr>' for x in g["items"]) + "</table>")
    for g in d.get("grammar", []):
        o.append(f'<h4>Γραμματική · {esc(g["title"])}</h4><p>{md(g["en"])}</p><table class="ex">' + "".join(
            f'<tr><td class="el" lang="el">{esc(x["el"])}</td><td class="en">{esc(x["en"])}</td></tr>' for x in g["examples"]) + "</table>")
    o.append(drills(d.get("drills"), keys, d["el"]))
    for t in d.get("tasks", []):
        tno[0] += 1
        has = bool(t.get("model"))
        o.append(f'<div class="task"><h4><span class="lvl">{esc(t["level"])}</span>Task {tno[0]} · {t["words"]} words{" · model answer in the appendix" if has else ""}</h4>'
                 f'<p lang="el">{md(t["el"])}</p><p class="sub">{md(t["en"])}</p>'
                 + ('<ul>' + "".join(f"<li>{md(x)}</li>" for x in t.get("plan", [])) + "</ul>" if t.get("plan") else "") + '</div><div class="lines"></div>')
        if has:
            answers.append(f'<section class="lesson"><h3 class="lt"><span lang="el"><span class="lvl">{esc(t["level"])}</span>Task {tno[0]} · {esc(d["el"])}</span>'
                           f'<span class="lt-en">{t["model_words"]} words</span></h3><p class="sub" lang="el">{md(t["el"])}</p>'
                           f'<div class="model">{paras(t["model"], "el")}</div><div class="trans"><div class="gl-h">Translation</div>{paras(t["model_en"])}</div></section>')
    return "".join(o)

def bank(d, keys):
    o = ["".join(block(b) for b in d["intro"])]
    for g in d["groups"]:
        o.append(f'<h4><span lang="el">{esc(g["el"])}</span> · {esc(g["en"])}</h4><table class="con">' + "".join(
            f'<tr><td class="el" lang="el"><strong>{esc(c["el"])}</strong><span class="reg">{c["reg"]}</span><br><span class="sub">{esc(c["en"])}</span></td>'
            f'<td><span lang="el">{esc(c["ex"]["el"])}</span><br><span class="sub">{esc(c["ex"]["en"])}{" · " + md(c["note"]) if c.get("note") else ""}</span></td></tr>' for c in g["items"]) + "</table>")
    for s in d.get("sections", []):
        o.append(f'<h4><span lang="el">{esc(s["el"])}</span> · {esc(s["en"])}</h4>' + "".join(block(b) for b in s["body"]))
    o.append(drills(d.get("drills"), keys, d["el"]))
    return "".join(o)

def checklist(d):
    o = ["".join(block(b) for b in d["intro"])]
    for s in d["checks"]:
        o.append(f'<h4><span lang="el">{esc(s["el"])}</span> · {esc(s["en"])}</h4><ul class="ck">' + "".join(
            f'<li><span lang="el">{esc(k["el"])}</span><br><span class="sub">{md(k["en"])}</span>'
            + (f'<br><span class="wr" lang="el"><s>{esc(k["wrong"])}</s> → {esc(k["right"])}</span>' if k.get("wrong") else "") + "</li>" for k in s["items"]) + "</ul>")
    return "".join(o)

def main():
    idx = json.load(open(os.path.join(SRC, "index.json"), encoding="utf-8"))
    toc, body, keys, answers, tno = [], [], [], [], [0]
    nmodels = sum(i["models"] for i in idx["items"]); ntasks = sum(len(i["tasks"]) for i in idx["items"])
    for p in idx["parts"]:
        its = [i for i in idx["items"] if i["part"] == p["id"]]
        pid = "p-" + p["id"]
        toc.append(f'<li class="toc-p"><a href="#{pid}">{esc(p["en"])}</a> <span lang="el">· {esc(p["el"])}</span><ol>')
        body.append(f'<section class="part" id="{pid}"><div class="part-h"><div class="pn">{esc(p.get("level", ""))}</div><h1>{esc(p["en"])}</h1><div class="pel" lang="el">{esc(p["el"])}</div></div>')
        for it in its:
            d = json.load(open(os.path.join(SRC, it["file"]), encoding="utf-8"))
            sid = "u-" + d["id"]
            toc.append(f'<li><a href="#{sid}">{esc(d["level"])} · <span lang="el">{esc(d["el"])}</span></a> <span class="sub">· {esc(d["title"])}</span></li>')
            inner = bank(d, keys) if d["kind"] == "bank" else checklist(d) if d["kind"] == "checklist" else unit(d, keys, answers, tno)
            body.append(f'<section class="lesson" id="{sid}"><h3 class="lt"><span lang="el"><span class="lvl">{esc(d["level"])}</span>{esc(d["el"])}</span>'
                        f'<span class="lt-en">{esc(d["title"])}</span></h3>{inner}</section>')
        toc.append("</ol></li>"); body.append("</section>")
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Appendix</div><h1>Model answers</h1><div class="pel" lang="el">Υποδειγματικές απαντήσεις</div></div>{"".join(answers)}</section>')
    body.append(f'<section class="part" id="key"><div class="part-h"><div class="pn">Appendix</div><h1>Answer key</h1><div class="pel" lang="el">Λύσεις</div></div><div class="key">{"".join(f"<p>{k}</p>" for k in keys)}</div></section>')
    body.append("<section class='part' id='credits'><h2 class='unit'>Sources</h2><p>Written for the Ελληνικά app, for personal, non-commercial study. Exam format from the Centre for the Greek Language "
                "(Κέντρο Ελληνικής Γλώσσας), <em>Πιστοποίηση Ελληνομάθειας</em>: level specifications for Β2 and Γ1, the Γ1 writing criteria and the candidates' guide, "
                "greek-language.gr/certification. All model texts, prompts and exercises are original; names, places and businesses in them are invented.</p></section>")
    toc.append('<li class="toc-p"><a href="#answers">Model answers</a></li><li class="toc-p"><a href="#key">Answer key</a></li>')
    cover = ('<section class="cover" lang="el"><div class="c-top">Ελληνικά · Συνοδευτικό εγχειρίδιο</div><div class="c-lvl">Τετράδιο γραπτού λόγου</div>'
             '<div class="c-name">Επιστολές, μηνύματα, άρθρα γνώμης και δοκίμια</div>'
             f'<p class="c-blurb">{len([i for i in idx["items"] if i["kind"] == "unit"])} διαβαθμισμένες ενότητες για το Β΄ επίπεδο της Πιστοποίησης Ελληνομάθειας και πέρα από αυτό, '
             f'με {nmodels} υποδειγματικά κείμενα, {ntasks} θέματα για γράψιμο, τράπεζα συνδέσμων και λίστα διόρθωσης.</p>'
             f'<div class="c-foot">Β1–Γ1 · Έκδοση {el_date()}</div></section>')
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ελληνικά · Writing workbook</title><style>{CSS}{EXTRA}</style></head>'
           f'<body>{cover}<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(toc)}</ol></section>{"".join(body)}</body></html>')
    tmp = tempfile.mkdtemp(prefix="tetradio-")
    open(os.path.join(tmp, "Writing.html"), "w", encoding="utf-8").write(doc)
    subprocess.run(["node", os.path.join(HERE, "render_pdf.js"), tmp, tmp, "Writing"], check=True, cwd=HERE)
    # Greek-only cover: print page 1 again without the English footer and swap it in (same method as the other volumes).
    open(os.path.join(tmp, "Cover.html"), "w", encoding="utf-8").write(f'<!doctype html><html lang="el"><head><meta charset="utf-8"><style>{CSS}{EXTRA}</style></head><body>{cover}</body></html>')
    js = ('const { chromium } = require("/opt/node22/lib/node_modules/playwright");(async()=>{const b=await chromium.launch({executablePath:"/opt/pw-browsers/chromium"});'
          'const p=await b.newPage();await p.goto("file://"+process.argv[1]);await p.evaluate(()=>document.fonts.ready);'
          'await p.pdf({path:process.argv[2],format:"A4",printBackground:true,preferCSSPageSize:true,pageRanges:"1"});await b.close();})();')
    subprocess.run(["node", "-e", js, os.path.join(tmp, "Cover.html"), os.path.join(tmp, "cover.pdf")], check=True)
    import pikepdf
    with pikepdf.open(os.path.join(tmp, "Ellinika-Writing-textbook.pdf"), allow_overwriting_input=True) as pdf, pikepdf.open(os.path.join(tmp, "cover.pdf")) as cv:
        for k in ("/Contents", "/Resources"):
            o = cv.pages[0].obj[k]
            pdf.pages[0].obj[k] = pdf.copy_foreign(o if o.is_indirect else cv.make_indirect(o))
        pdf.save()
    subprocess.run([sys.executable, os.path.join(HERE, "compress.py"), os.path.join(tmp, "Ellinika-Writing-textbook.pdf"), PDF, "Ελληνικά · Τετράδιο γραπτού λόγου"], check=True)
    print(f"tetradio PDF: {len(keys)} questions, {len(answers)} model answers → {PDF} ({os.path.getsize(PDF) // 1024} KB)")

if __name__ == "__main__":
    main()
