#!/usr/bin/env python3
"""Supplement volumes: the Β2/Γ1 practice sets and listening items added after a given textbook build.

Usage: python3 build_supplement.py --since <git commit> [--out DIR] [B2 C1]
The level textbooks (build_textbook.py) hold everything up to <commit>; this writes <out>/<L>-supplement.html
with only the exam-task and listening files added to the repo after it. render_pdf.js prints them
(name them "<L>-supplement" so the PDF becomes Ellinika-<L>-supplement-textbook.pdf, then rename).
"""
import os, random, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_textbook as bt
from covers_el import el_date, el_level

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SINCE = sys.argv[sys.argv.index("--since") + 1]
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else os.path.join(REPO, "downloads/textbook/build")
esc, anchor = bt.esc, bt.anchor

def added(path):
    out = subprocess.check_output(["git", "-C", REPO, "diff", "--name-only", "--diff-filter=A", SINCE, "HEAD", "--", path]).decode().split()
    return sorted(out, key=num)

def num(f):
    m = re.findall(r"\d+", os.path.basename(f))
    return int(m[-1]) if m else 1

def build(level):
    bt._ids.clear()
    rng = random.Random(f"ellinika-supplement-{level}")
    ex = bt.Exercises()
    pre = "b2-tasks" if level == "B2" else "c1-tasks"
    offset = 8 if level == "B2" else 2          # file b2-tasks-N.json is practice set N+8; c1-tasks-N.json is set N+2
    exam_files = [f for f in added("library/exam") if os.path.basename(f).startswith(pre)]
    listen_files = added("library/listening")
    sets = [num(f) + offset for f in exam_files]
    units = []   # (unit title, [section html])
    toc = []

    # exam practice: one unit per practice set
    n_tasks = 0
    for f in exam_files:
        sn = num(f) + offset
        secs = []
        for t in bt.J(os.path.join(REPO, f))["tasks"]:
            lid = anchor("exam-" + t["id"])
            txt = t.get("text_el", "")
            s = (f'<div class="reading exam"><div class="eyebrow">Εξέταση · {esc(t.get("paper", ""))}</div><h4 lang="el">{esc(t.get("title"))}</h4>'
                 f'<p class="sub">{esc(t.get("task_type", ""))}</p><p class="instr" lang="el">{esc(t.get("instructions_el", ""))}</p><div class="rd" lang="el">{bt.paras(txt.replace(chr(10), chr(10) + chr(10)) if txt.count(chr(10)) > 3 and chr(10) + chr(10) not in txt else txt)}</div>')
            qs = t.get("questions", [])
            shared = qs and qs[0].get("options") and all(q.get("options") == qs[0]["options"] for q in qs) and len(qs) > 2
            if shared:
                s += f'<div class="bank"><b>Choose from:</b> <span lang="el">{" · ".join(esc(o) for o in qs[0]["options"])}</span></div>'
            s += '<ol class="ex-items">' + "".join(f'<li><span lang="el">{esc(q.get("prompt"))}</span>' + ("" if shared or not q.get("options") else '<ul class="opts2">' + "".join(f'<li lang="el">{esc(o)}</li>' for o in q["options"]) + "</ul>") + "</li>" for q in qs) + "</ol></div>"
            ex.keys.append((t.get("title"), lid, [f"<b>{i}</b> {bt.gr(q.get('answer'))}" + (f' <span class="en">{esc(q.get("answer_note"))}</span>' if q.get("answer_note") else "") for i, q in enumerate(qs, 1)] + ([f'<span class="en">{esc(t["answer_note"])}</span>'] if t.get("answer_note") else [])))
            s += f'<p class="sub">Answers: <a href="#key-{lid}">answer key</a>.</p>'
            secs.append(f'<section class="lesson" id="{lid}">{s}</section>')
            n_tasks += 1
        units.append(("exam", f"{'Β2' if level == 'B2' else 'Γ1'} practice set {sn}", secs))

    # listening items of this level, in batch order
    n_listen = 0
    for f in listen_files:
        secs = []
        for it in bt.J(os.path.join(REPO, f))["items"]:
            if it.get("level") != level: continue
            lid = anchor("listening-" + it["id"])
            s = (f'<p class="sub" lang="el">{esc(it.get("context_el") or "")}</p>' + bt.dialogue_html(it.get("title"), f"{it.get('title_en', '')} · {it.get('type', '')}", it.get("script", []), it.get("gloss"), "Ακρόαση · listening transcript"))
            s += bt.vocab_list(it.get("vocab") or [])
            prac = [{"gen": "reading-q", "questions": [{"prompt": q.get("q") or q.get("prompt"), "options": q.get("options"), "answer": q.get("answer"), "why": q.get("why")} for q in it.get("questions", [])]}]
            s += ex.render(it.get("title"), lid, prac, rng)
            secs.append(f'<section class="lesson" id="{lid}">{s}</section>')
            n_listen += 1
        if secs: units.append(("listen", f"Listening batch {num(f)}", secs))

    body, chap = [], 0
    for key, title, el in [("exam", "Exam practice sets", "Εξεταστική προετοιμασία"), ("listen", "Listening transcripts", "Απομαγνητοφωνήσεις")]:
        us = [(t, s) for k, t, s in units if k == key]
        if not us: continue
        chap += 1
        pid = anchor(f"part-{key}")
        toc.append(f'<li class="toc-p"><a href="#{pid}">{chap}. {esc(title)}</a><ol>')
        body.append(f'<section class="part" id="{pid}"><div class="part-h"><div class="pn">Part {chap}</div><h1>{esc(title)}</h1><div class="pel" lang="el">{esc(el)}</div></div>')
        for ut, secs in us:
            uid = anchor("unit-" + ut)
            toc.append(f'<li><a href="#{uid}">{esc(ut)}</a></li>')
            body.append(f'<h2 class="unit" id="{uid}">{esc(ut)}</h2>' + "".join(secs))
        toc.append("</ol></li>"); body.append("</section>")
    chap += 1
    toc.append(f'<li class="toc-p"><a href="#answers">{chap}. Answer key</a></li>')
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Part {chap}</div><h1>Answer key</h1><div class="pel" lang="el">Λύσεις</div></div><div class="key">{ex.key_html()}</div></section>')

    lv = el_level(level)
    cover = (f'<section class="cover" lang="el"><div class="c-top">Ελληνικά · Συμπλήρωμα του εγχειριδίου</div><div class="c-lvl">{lv}</div>'
             f'<div class="c-name">{bt.LEVEL_INFO_EL[level][0]}</div>'
             f'<p class="c-blurb">Όσα προστέθηκαν μετά την τελευταία έκδοση του τόμου {lv}: τα σύνολα εξεταστικής προετοιμασίας {sets[0]}–{sets[-1]} '
             f'({n_tasks} θέματα με λύσεις) και {n_listen} νέα ακούσματα με απομαγνητοφώνηση, λεξιλόγιο και ερωτήσεις κατανόησης.</p>'
             f'<div class="c-foot">Συμπλήρωμα του τόμου {bt.LEVELS.index(level) + 1} · Έκδοση {el_date()}</div></section>')
    toc_html = f'<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(toc)}</ol></section>'
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ελληνικά {level} · Supplement</title><style>{bt.CSS}</style></head>'
           f'<body>{cover}{toc_html}{"".join(body)}</body></html>')
    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/{level}-supplement.html", "w", encoding="utf-8") as fh:
        fh.write(doc)
    print(f"{level} supplement: sets {sets[0]}–{sets[-1]}, {n_tasks} tasks, {n_listen} listening items, {sum(len(a) for _, _, a in ex.keys)} answers, {len(doc) // 1024} KB")

if __name__ == "__main__":
    for L in [a for a in sys.argv[1:] if a in ("B2", "C1")] or ["B2", "C1"]:
        build(L)
