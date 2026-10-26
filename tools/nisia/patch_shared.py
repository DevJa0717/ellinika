#!/usr/bin/env python3
"""Idempotent shared-file edits for the nisia (islands) and diaspora readers.
Usage: python3 patch_shared.py <app_root> [<downloads_textbook_dir>]   (repo root, or /mnt/project-files/app)
Adds the SHELVES entries and the "see also" line in bilingual.js, the library/index.json rows and the offline-files.json
entries, and lists the two PDFs on the textbook index. Bump bilingual.js ?v in index.html and the sw.js CACHE by hand."""
import json, os, re, sys, glob
root = sys.argv[1]
ADD = {"nisia": "The Greek islands", "diaspora": "The Greek diaspora"}
ROWS = [{"id": "nisia", "route": "nisia", "el": "Τα ελληνικά νησιά", "title": "The Greek islands one by one: bilingual reader, 38 chapters by archipelago, B1–C1", "ready": True},
        {"id": "diaspora", "route": "diaspora", "el": "Η ελληνική διασπορά", "title": "The Greek diaspora: bilingual reader from the ancient colonies to today's emigrants, 17 chapters, B1+–C1", "ready": True}]
SEE = '''      ${ch.see?.length ? `<p class="bl-see sub"><span lang="el">Δείτε επίσης</span> · See also: ${ch.see.map((x) => `<a href="${E.esc(x.href)}"><span lang="el">${E.esc(x.el)}</span></a>`).join(" · ")}</p>` : ""}'''
BRIEF = '''      ${ch.summary_en ? `<section class="card bl-brief"><h3>In brief</h3><p>${E.md(ch.summary_en)}</p></section>` : ""}'''

p = os.path.join(root, "bilingual.js"); s = open(p, encoding="utf-8").read(); t = s
m = re.search(r"const SHELVES = \{([^}]*)\};", t); body = m.group(1).rstrip()
for k, v in ADD.items():
    if f"{k}:" not in body: body += f', {k}: "{v}"'
t = t[:m.start(1)] + body + " " + t[m.end(1):]
if "bl-see" not in t:
    t = t.replace(BRIEF, BRIEF + "\n" + SEE, 1)
    t = re.sub(r"^\.bl-toc \{", ".bl-see { margin: 0 0 14px; line-height: 1.7; }\n.bl-toc {", t, count=1, flags=re.M)
if t != s: open(p, "w", encoding="utf-8").write(t); print("patched", p)

p = os.path.join(root, "library/index.json"); d = json.load(open(p)); ids = [x["id"] for x in d["shelves"]]
if not all(r["id"] in ids for r in ROWS):
    at = max(i for i, x in enumerate(ids) if x in ("simera", "politeia", "kouzina", "athlitismos", "mathiatriki", "epistimi")) + 1
    for r in reversed(ROWS):
        if r["id"] not in ids: d["shelves"].insert(at, r)
    open(p, "w", encoding="utf-8").write(json.dumps(d, ensure_ascii=False, indent=1) + "\n"); print("patched", p)

p = os.path.join(root, "offline-files.json"); raw = open(p).read(); o = json.loads(raw); n = 0
for sh in ADD:
    for f in sorted(glob.glob(f"{root}/library/{sh}/*.json")) + sorted(glob.glob(f"{root}/img/{sh}/*.jpg")):
        rel = os.path.relpath(f, root)
        if rel not in o["files"]: o["files"].append(rel); n += 1
if n: open(p, "w").write(json.dumps(o, ensure_ascii=False, indent=1 if raw.startswith('{\n "') else None) + ("\n" if raw.endswith("\n") else "")); print("offline +", n)

if len(sys.argv) > 2:
    p = os.path.join(sys.argv[2], "index.html"); s = open(p, encoding="utf-8").read()
    new = ('<li><a href="Ellinika-Islands.pdf"><span class="lv">B1–C1</span><span class="t">The Greek islands · Τα ελληνικά νησιά: bilingual reader, the inhabited islands one by one, archipelago by archipelago<small>172 pages · 7.7 MB · 38 chapters, 37 pictures, 152 questions</small></span></a></li>\n'
           '<li><a href="Ellinika-Diaspora.pdf"><span class="lv">B1+–C1</span><span class="t">The Greek diaspora · Η ελληνική διασπορά: bilingual reader from the ancient colonies to today\'s emigrants<small>69 pages · 3 MB · 17 chapters, 14 pictures, 68 questions</small></span></a></li>\n')
    if "Ellinika-Islands.pdf" not in s:
        i = s.index('<li><a href="Ellinika-Writing-workbook.pdf"'); open(p, "w", encoding="utf-8").write(s[:i] + new + s[i:]); print("patched", p)
