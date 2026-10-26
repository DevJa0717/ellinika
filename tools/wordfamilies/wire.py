#!/usr/bin/env python3
"""Wire the #families and #confusables shelves into the shared app files. Idempotent: safe to re-run after a rebase.
index.html (script tag), sw.js (SHELL + cache bump), library/index.json (two shelf rows after "klisi" or "pos"),
offline-files.json (the shelf JSON)."""
import glob, json, os, re
R = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(R)
JS = "word-families.js"
h = open("index.html", encoding="utf-8").read()
if JS not in h:
    h = re.sub(r'(<script src="app\.js\?v=\d+"></script>)', f'<script src="{JS}?v=1"></script>\n\\1', h)
    open("index.html", "w", encoding="utf-8").write(h)
s = open("sw.js", encoding="utf-8").read()
if f'"{JS}"' not in s:
    s = s.replace('"app.js", "manifest.webmanifest"', f'"{JS}", "app.js", "manifest.webmanifest"')
    n = int(re.search(r'ellinika-v(\d+)', s).group(1))
    s = re.sub(r'ellinika-v\d+', f'ellinika-v{n + 1}', s, count=1)
    open("sw.js", "w", encoding="utf-8").write(s)
L = json.load(open("library/index.json", encoding="utf-8"))
ids = [x["id"] for x in L["shelves"]]
rows = [
    {"id": "families", "route": "families", "el": "Οικογένειες λέξεων",
     "title": "Word families: roots, prefixes and suffixes with the words they generate, and production drills", "ready": True},
    {"id": "confusables", "route": "confusables", "el": "Ψευδόφιλοι και παρώνυμα",
     "title": "False friends and confusables: pairs learners mix up, with contrastive examples and drills", "ready": True},
]
if "families" not in ids:
    at = ids.index("klisi") + 1 if "klisi" in ids else ids.index("pos") + 1
    L["shelves"][at:at] = rows
    json.dump(L, open("library/index.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
o = json.load(open("offline-files.json", encoding="utf-8"))
mine = sorted(glob.glob("library/families/*.json") + glob.glob("library/confusables/*.json"))
add = [f for f in mine if f not in o["files"]]
if add:
    o["files"] += add
    json.dump(o, open("offline-files.json", "w", encoding="utf-8"), separators=(",", ":"))
print("wired:", JS in open("index.html").read(), re.search(r'ellinika-v\d+', open("sw.js").read()).group(0), len(add), "offline files added")
