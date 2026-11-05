#!/usr/bin/env python3
"""Idempotent shared-file edits for the everyday-theme readers (thread "Add readers and units for uncovered themes").
Usage: python3 patch_shared.py <app_root>   Adds, for every shelf below whose library/<id>/index.json exists:
the SHELVES entry in bilingual.js, the library/index.json row (after the other bilingual readers), the offline-files.json
entries; when anything changed it bumps bilingual.js ?v in index.html and the sw.js cache name."""
import json, os, re, sys
root = sys.argv[1]
ALL = [
 ("kathimerini", "Everyday life", "Η καθημερινή ζωή στην Ελλάδα", "Everyday life in Greece: bilingual reader on renting, the apartment block, bills, paperwork, taxes, banks and IRIS, shopping, returns, parcels, metro, car, coaches, ferries and taxis (B1+–C1)"),
 ("ygeia", "Health and the body", "Υγεία, σώμα και ψυχή", "Health, body and mind: bilingual reader on the body, the doctor, the pharmacy, hospitals and emergencies, the dentist, pregnancy, mental health and healthy living (B1+–C1)"),
 ("douleia", "Work and money", "Δουλειά και χρήμα", "Work and money: bilingual reader on job hunting, interviews, contracts and rights, salaries and insurance, office life, freelancing, unemployment, strikes, loans and pensions (B1+–C1)"),
 ("scheseis", "Relationships and feelings", "Σχέσεις και συναισθήματα", "Relationships and feelings: bilingual reader on emotions, character, friendship, dating, couples, weddings and baptisms, family, arguments and making up (B1+–C1)"),
 ("nomos", "Law, police and justice", "Νόμος, αστυνομία και δικαιοσύνη", "Law, police and justice: bilingual reader on calling the police, theft and fraud, accidents, courts and trials, lawyers, prisons, crime news and crime fiction (B2–C1)"),
 ("eleftheros", "Free time", "Ελεύθερος χρόνος", "Free time: bilingual reader on going out, TV and series, phones and social media, clothes and looks, pets and animals, holidays and camping, hobbies and games (B1+–C1)"),
]
SH = [s for s in ALL if os.path.exists(os.path.join(root, "library", s[0], "index.json"))]
AFTER = ["philosophers", "istoria", "simera", "politeia", "kouzina", "athlitismos", "mathiatriki", "epistimi", "nisia", "diaspora", "mousiki", "skini", "eortes"]
def rw(path, fn):
    s = open(path, encoding="utf-8").read(); t = fn(s)
    if t != s: open(path, "w", encoding="utf-8").write(t); print("patched", path); return True
    print("unchanged", path); return False
def viewer(s):
    m = re.search(r"const SHELVES = \{([^}]*)\};", s); body = m.group(1).rstrip()
    for k, v, *_ in SH:
        if f" {k}:" not in body and f"{{{k}:" not in body: body += f', {k}: "{v}"'
    return s[:m.start(1)] + body + " " + s[m.end(1):]
changed = rw(os.path.join(root, "bilingual.js"), viewer)
libpath = os.path.join(root, "library/index.json"); orig = open(libpath, encoding="utf-8").read()
if any(f'"id": "{k}"' not in orig for k, *_ in SH):
    def lib(s):
        d = json.loads(s); sh = d["shelves"]; ids = [x["id"] for x in sh]
        at = max([ids.index(r) for r in AFTER + [x[0] for x in ALL] if r in ids] or [len(sh) - 1]) + 1
        for k, _, el, title in SH:
            if k in ids: continue
            sh.insert(at, {"id": k, "route": k, "el": el, "title": title, "ready": True}); at += 1; ids = [x["id"] for x in sh]
        return json.dumps(d, ensure_ascii=False, indent=1) + ("\n" if s.endswith("\n") else "")
    changed = rw(libpath, lib) or changed
def offline(s):
    d = json.loads(s); have = set(d["files"])
    for k, *_ in SH:
        for sub, ext in ((f"library/{k}", ".json"), (f"img/{k}", ".jpg")):
            p = os.path.join(root, sub)
            if os.path.isdir(p): have |= {f"{sub}/{f}" for f in os.listdir(p) if f.endswith(ext)}
    d["files"] = sorted(have); return json.dumps(d, ensure_ascii=False)
offpath = os.path.join(root, "offline-files.json")
if os.path.exists(offpath): changed = rw(offpath, offline) or changed
if changed:
    rw(os.path.join(root, "index.html"), lambda s: re.sub(r"bilingual\.js\?v=(\d+)", lambda m: f"bilingual.js?v={int(m.group(1)) + 1}", s, count=1))
    rw(os.path.join(root, "sw.js"), lambda s: re.sub(r'const CACHE = "ellinika-v(\d+)"', lambda m: f'const CACHE = "ellinika-v{int(m.group(1)) + 1}"', s, count=1))
