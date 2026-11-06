#!/usr/bin/env python3
"""Companion word books for the frequency-ranked vocabulary course (#lexi): one PDF per 1,000 words (two app bands).

Usage: python3 build_lexi.py [--vol 1,2,...] [--app <app root>] [--out <dir>]
Writes downloads/textbook/Ellinika-Vocabulary-01.pdf … -19.pdf. Each volume: Greek-only cover, then per band of 500
words a word list (rank, word with article, grammar header, meaning, example, two common combinations) and a
self-test page (40 meanings to put into Greek), with the answer key at the end of the volume.
Data: library/lexi/band-NN.json (tools/lexi/build.py). Rendering and the cover/body join reuse build_wordfamilies.py.
"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_wordfamilies as wf
from covers_el import el_date, el_level

APP = wf.APP
OUT = wf.OUT
D = os.path.join(APP, "library", "lexi")
esc = wf.esc
POS_EL = {"noun": "ουσ.", "verb": "ρ.", "adjective": "επίθ.", "adverb": "επίρρ.", "pronoun": "αντων.", "conjunction": "σύνδ.",
          "preposition": "πρόθ.", "particle": "μόρ.", "numeral": "αριθμ.", "article": "άρθρο", "other": "έκφρ."}
STYLE = """<style>
.lx-tbl { width: 100%; border-collapse: collapse; font-size: 8.9pt; table-layout: fixed; }
.lx-tbl col.r { width: 9mm; } .lx-tbl col.w { width: 44mm; } .lx-tbl col.m { width: auto; }
.lx-tbl td { border: none; border-bottom: 0.6pt solid #d9dee8; padding: 1.4mm 1.2mm 1.6mm; vertical-align: top; }
.lx-tbl tr { break-inside: avoid; }
.lx-tbl td.r { color: #7a8396; font-family: "TBSans", sans-serif; font-size: 7.4pt; padding-top: 2mm; }
.lx-tbl .w { font-size: 11.5pt; font-weight: 700; color: #0f2a4d; display: block; }
.lx-tbl .h { display: block; color: #7a8396; font-size: 7.6pt; margin-top: 0.6mm; }
.lx-tbl .g { font-family: "TBSans", sans-serif; font-size: 8.8pt; color: #222; display: block; }
.lx-tbl .x { display: block; margin-top: 0.8mm; }
.lx-tbl .xe { display: block; color: #5b6475; font-style: italic; font-size: 8.2pt; }
.lx-tbl .c { display: block; margin-top: 0.8mm; font-size: 8.2pt; color: #333; }
.lx-tbl .c i { color: #7a8396; font-style: normal; font-family: "TBSans", sans-serif; font-size: 7.6pt; }
.lx-test { columns: 2; column-gap: 9mm; font-size: 9.2pt; padding-left: 6mm; margin: 0; }
.lx-test li { break-inside: avoid; margin: 0 0 3.1mm; }
.lx-test .ln { display: block; border-bottom: 0.8pt solid #aab3c2; height: 5mm; margin-top: 0.5mm; }
.lx-key { columns: 3; column-gap: 6mm; font-size: 8.6pt; padding-left: 6mm; }
.lx-key li { break-inside: avoid; }
.lx-intro p { font-size: 10pt; }
</style>"""

def fmt(n):
    return f"{n:,}".replace(",", ".")

def volume(v, idx):
    bands = [b for b in idx["bands"] if (b["n"] + 1) // 2 == v]
    rnd = random.Random(v)
    body, keys, toc = [], [], []
    for b in bands:
        words = json.load(open(os.path.join(D, f"band-{b['n']:02d}.json"), encoding="utf-8"))
        rows = []
        for w in words:
            word = (w["a"] + " " if w.get("a") else "") + w["l"]
            x = f'<span class="x" lang="el">{esc(w["x"][0])}</span><span class="xe">{esc(w["x"][1])}</span>' if w.get("x") else ""
            c = " · ".join(f'<span lang="el">{esc(a)}</span> <i>{esc(e)}</i>' for a, e in (w.get("c") or [])[:2])
            rows.append(f'<tr><td class="r">{w["r"]}</td><td><span class="w" lang="el">{esc(word)}</span><span class="h" lang="el">{esc(POS_EL.get(w["p"], ""))} {esc(w.get("h", ""))}</span></td>'
                        f'<td><span class="g">{esc(w["g"])}</span>{x}{f"<span class=c>{c}</span>" if c else ""}</td></tr>')
        bid = f"b{b['n']}"
        toc.append(f'<li class="toc-p"><a href="#{bid}"><span lang="el">Λέξεις {fmt(b["from"])}–{fmt(b["to"])}</span></a> · word list and self-test</li>')
        body.append(f'<section class="part" id="{bid}"><div class="part-h"><div class="pn">Band {b["n"]} · Ζώνη {b["n"]}</div>'
                    f'<h1 lang="el">Λέξεις {fmt(b["from"])}–{fmt(b["to"])}</h1><div class="pel">{esc(", ".join(b["sample"]))} …</div></div>'
                    f'<table class="lx-tbl"><colgroup><col class="r"><col class="w"><col class="m"></colgroup><tbody>{"".join(rows)}</tbody></table></section>')
        test = rnd.sample(words, min(40, len(words)))
        body.append(f'<section class="part"><div class="part-h"><div class="pn">Self-test · Αυτοαξιολόγηση</div><h1 lang="el">Λέξεις {fmt(b["from"])}–{fmt(b["to"])}</h1>'
                    f'<div class="pel">Write the Greek word (with its article for nouns). Answers at the end of the book.</div></div>'
                    f'<ol class="lx-test">{"".join(f"<li>{esc(w["g"])}<span class=ln></span></li>" for w in test)}</ol></section>')
        keys.append(f'<h3 lang="el">Λέξεις {fmt(b["from"])}–{fmt(b["to"])}</h3><ol class="lx-key">'
                    + "".join(f'<li lang="el">{esc((w["a"] + " " if w.get("a") else "") + w["l"])}</li>' for w in test) + "</ol>")
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Λύσεις</div><h1>Answer key</h1></div>{"".join(keys)}</section>')
    toc.append('<li class="toc-p"><a href="#answers">Answer key · Λύσεις</a></li>')
    first, last = bands[0]["from"], bands[-1]["to"]
    cefr = {}
    for b in bands:
        for k, n in b["cefr"].items(): cefr[k] = cefr.get(k, 0) + n
    lv = [k for k in ("A1", "A2", "B1", "B2", "C1") if cefr.get(k, 0) >= 0.08 * sum(cefr.values())]
    lv_txt = el_level(f"{lv[0]}–{lv[-1]}" if len(lv) > 1 else lv[0]) if lv else ""
    intro = (f'<section class="toc lx-intro"><h1>Contents · Περιεχόμενα</h1><ol class="toc-l">{"".join(toc)}</ol>'
             f'<p>This book lists words {fmt(first)}–{fmt(last)} of the app\'s dictionary in order of frequency, exactly as in the app\'s vocabulary course '
             f'(Resources → Λεξιλόγιο κατά συχνότητα). For each word: its rank, the word with its article, the grammar you need to use it '
             f'(genitive, past tense, feminine and neuter forms), the meaning, an example sentence and two common combinations. '
             f'Each band ends with a self-test of 40 meanings to put into Greek.</p></section>')
    cov = wf.cover("Ελληνικά · Συνοδευτικό εγχειρίδιο", "Λεξιλόγιο", f"Τόμος {v} · Λέξεις {fmt(first)}–{fmt(last)}",
                   f"Οι λέξεις {fmt(first)} έως {fmt(last)} της ελληνικής κατά συχνότητα, με το άρθρο, τους βασικούς τύπους, τη σημασία, "
                   f"ένα παράδειγμα και συχνές φράσεις για κάθε λέξη, και ασκήσεις αυτοαξιολόγησης με λύσεις.",
                   f"{lv_txt + ' · ' if lv_txt else ''}Έκδοση {el_date()}")
    return cov, wf.page(f"Ελληνικά · Λεξιλόγιο {v}", STYLE + intro + "".join(body)), first, last

if __name__ == "__main__":
    idx = json.load(open(os.path.join(D, "index.json"), encoding="utf-8"))
    nvol = (len(idx["bands"]) + 1) // 2
    vols = [int(x) for x in sys.argv[sys.argv.index("--vol") + 1].split(",")] if "--vol" in sys.argv else range(1, nvol + 1)
    for v in vols:
        cov, body, first, last = volume(v, idx)
        title = f"Ελληνικά · Λεξιλόγιο, τόμος {v}"
        wf.render(cov, body, f"Ελληνικά · Λεξιλόγιο {fmt(first)}–{fmt(last)}", os.path.join(OUT, f"Ellinika-Vocabulary-{v:02d}.pdf"), title)
