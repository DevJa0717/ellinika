#!/usr/bin/env python3
"""Idempotent small edits to shared files for the athlitismos / mathiatriki / epistimi shelves (themed readers thread).
Usage: python3 patch_shared.py <app_root>   (repo root, or /mnt/project-files/app)
Adds the SHELVES entries in bilingual.js, the library/index.json rows, and the offline-files.json entries;
when the viewer changes it also bumps the bilingual.js ?v in index.html and the sw.js cache name."""
import json, os, re, sys
root = sys.argv[1]
ADD = {"athlitismos": "Greek sport", "mathiatriki": "Maths and medicine", "epistimi": "Science and technology"}
ROWS = [
    {"id": "athlitismos", "route": "athlitismos", "el": "Ο αθλητισμός των Ελλήνων", "title": "Bilingual sport reader: from Olympia and the 1896 revival to Euro 2004, basketball and the language of the stands", "ready": True},
    {"id": "mathiatriki", "route": "mathiatriki", "el": "Μαθηματικά και ιατρική των Ελλήνων", "title": "Bilingual reader on Greek mathematics and medicine: Thales to Carathéodory, Hippocrates to the Pap test", "ready": True},
    {"id": "epistimi", "route": "epistimi", "el": "Επιστήμη και τεχνολογία", "title": "Bilingual science and technology reader: the Antikythera mechanism, earthquakes, climate, CERN, space and AI", "ready": True},
]
READERS = ["philosophers", "istoria", "simera", "politeia", "kouzina", "mousiki", "skini", "eortes"]

def rw(path, fn):
    s = open(path, encoding="utf-8").read(); t = fn(s)
    if t != s:
        open(path, "w", encoding="utf-8").write(t); print("patched", path); return True
    print("unchanged", path); return False

def viewer(s):
    m = re.search(r"const SHELVES = \{([^}]*)\};", s)
    body = m.group(1).rstrip()
    for k, v in ADD.items():
        if f"{k}:" not in body: body += f', {k}: "{v}"'
    body += " "
    return s[:m.start(1)] + body + s[m.end(1):]

changed = rw(os.path.join(root, "bilingual.js"), viewer)
if changed:
    rw(os.path.join(root, "index.html"), lambda s: re.sub(r"bilingual\.js\?v=(\d+)", lambda m: f"bilingual.js?v={int(m.group(1)) + 1}", s, count=1))

def lib(s):
    d = json.loads(s); sh = d["shelves"]; ids = [x["id"] for x in sh]
    at = max([ids.index(r) for r in READERS if r in ids] or [len(sh) - 1]) + 1
    for row in ROWS:
        if row["id"] in ids: continue
        sh.insert(at, row); at += 1; ids = [x["id"] for x in sh]
    return json.dumps(d, ensure_ascii=False, indent=1) + "\n" if s.endswith("\n") else json.dumps(d, ensure_ascii=False, indent=1)
libpath = os.path.join(root, "library/index.json")
orig = open(libpath, encoding="utf-8").read()
# keep the file's own formatting when nothing changes
if any(f'"id": "{r["id"]}"' not in orig for r in ROWS):
    changed = rw(libpath, lib) or changed
else:
    print("unchanged", libpath)

def offline(s):
    d = json.loads(s); have = set(d["files"])
    for sh in ADD:
        for sub, ext in ((f"library/{sh}", ".json"), (f"img/{sh}", ".jpg")):
            p = os.path.join(root, sub)
            if os.path.isdir(p):
                for f in os.listdir(p):
                    if f.endswith(ext): have.add(f"{sub}/{f}")
    d["files"] = sorted(have)
    return json.dumps(d, ensure_ascii=False)
offpath = os.path.join(root, "offline-files.json")
if os.path.exists(offpath): changed = rw(offpath, offline) or changed

if changed:
    rw(os.path.join(root, "sw.js"), lambda s: re.sub(r'const CACHE = "ellinika-v(\d+)"', lambda m: f'const CACHE = "ellinika-v{int(m.group(1)) + 1}"', s, count=1))
