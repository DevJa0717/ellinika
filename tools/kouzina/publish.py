#!/usr/bin/env python3
"""Publish the cookbook shelf to a clean clone/worktree of the GitHub Pages repo (only this shelf's paths plus the shared
one-line edits it needs). Usage: python3 publish.py <repo worktree> [--pdf]
Copies app/library/kouzina, app/img/kouzina, tools/kouzina, app/bilingual.js; adds the kouzina row to library/index.json
(project and repo); bumps bilingual.js?v= in index.html and the sw.js CACHE version once per run; adds the shelf's files to
offline-files.json; with --pdf also copies downloads/textbook/Ellinika-Cookbook.pdf."""
import json, os, re, shutil, sys, glob
P, R = "/mnt/project-files", sys.argv[1]
ROW = {"id": "kouzina", "route": "kouzina", "el": "Η ελληνική κουζίνα", "title": "Greek cookbook: bilingual recipes from every region, with the history, goods and heritage of Greek food", "ready": True}
def sync(src, dst):
    if os.path.isdir(src):
        if os.path.exists(dst): shutil.rmtree(dst)
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__"))
    elif os.path.exists(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(src, dst)
sync(f"{P}/app/library/kouzina", f"{R}/library/kouzina")
sync(f"{P}/app/img/kouzina", f"{R}/img/kouzina")
sync(f"{P}/tools/kouzina", f"{R}/tools/kouzina")
sync(f"{P}/app/bilingual.js", f"{R}/bilingual.js")
if "--pdf" in sys.argv: sync(f"{P}/downloads/textbook/Ellinika-Cookbook.pdf", f"{R}/downloads/textbook/Ellinika-Cookbook.pdf")
for base in (f"{P}/app", R):
    p = f"{base}/library/index.json"; d = json.load(open(p, encoding="utf-8"))
    sh = d["shelves"]
    if not any(x["id"] == "kouzina" for x in sh):
        i = next(i for i, x in enumerate(sh) if x["id"] == "politeia") + 1
        sh.insert(i, ROW); json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    h = f"{base}/index.html"; s = open(h, encoding="utf-8").read()
    m = re.search(r'bilingual\.js\?v=(\d+)', s)
    s = s.replace(m.group(0), f"bilingual.js?v={int(m.group(1)) + 1}") if base == R else s
    if base == R: open(h, "w", encoding="utf-8").write(s); NEWV = int(m.group(1)) + 1
    w = f"{base}/sw.js"; t = open(w, encoding="utf-8").read()
    m = re.search(r'ellinika-v(\d+)', t)
    if base == R: t = t.replace(m.group(0), f"ellinika-v{int(m.group(1)) + 1}", 1); open(w, "w", encoding="utf-8").write(t); NEWC = int(m.group(1)) + 1
# keep the project copies of index.html and sw.js identical to the repo's
shutil.copy2(f"{R}/index.html", f"{P}/app/index.html"); shutil.copy2(f"{R}/sw.js", f"{P}/app/sw.js")
o = f"{R}/offline-files.json"; d = json.load(open(o, encoding="utf-8"))
mine = sorted(os.path.relpath(f, R) for f in glob.glob(f"{R}/library/kouzina/*.json") + glob.glob(f"{R}/img/kouzina/*"))
d["files"] = sorted(set(x for x in d["files"] if not x.startswith(("library/kouzina/", "img/kouzina/"))) | set(mine))
json.dump(d, open(o, "w", encoding="utf-8"), ensure_ascii=False)
print(f"published {len(mine)} shelf files; bilingual.js?v={NEWV}, sw ellinika-v{NEWC}")
