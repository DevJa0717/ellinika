#!/usr/bin/env python3
"""glossfill.py <shelf> : build the shelf to /tmp, run check.js, and fill lookup MISS/GUESS forms from the glosses of
all other library shelves (pool) into <shelf>/gloss.txt. Prints the forms still missing (write them into gloss.txt by hand)."""
import json, os, re, subprocess, sys, glob
HERE = os.path.dirname(os.path.abspath(__file__)); S = sys.argv[1]
OUT = f"/tmp/claude-0/out/{S}"
subprocess.run(["python3", os.path.join(HERE, "build.py"), S, OUT], check=True)
pool = {}
for f in glob.glob("/mnt/project-files/app/library/*/*.json"):
    try: d = json.load(open(f, encoding="utf-8"))
    except Exception: continue
    for it in ([d] if isinstance(d, dict) else []):
        g = it.get("gloss") if isinstance(it.get("gloss"), dict) else None
        if g:
            for k, v in g.items():
                if isinstance(v, str) and "—" in v: pool.setdefault(k, v)
for gf in glob.glob(os.path.join(HERE, "*/gloss.txt")) + [os.path.join(HERE, "gloss.txt"), "/mnt/project-files/tools/philosophers/common-gloss.txt", "/mnt/project-files/tools/politeia/gloss.txt"]:
    if os.path.exists(gf):
        for line in open(gf, encoding="utf-8"):
            if "=" in line and not line.startswith("#"):
                a, b = line.split("=", 1); pool.setdefault(a.strip(), b.strip())
r = subprocess.run("node /mnt/project-files/tools/philosophers/check.js " + " ".join(f for f in glob.glob(OUT + "/*.json") if not f.endswith("index.json")), shell=True, capture_output=True, text=True, env={**os.environ, "LANG": "C.UTF-8"})
miss = []
for line in r.stdout.splitlines():
    m = re.match(r"\s+(MISS|GUESS): (.*)", line)
    if m:
        for w in m.group(2).split():
            miss.append(w.split("→")[0])
miss = list(dict.fromkeys(miss))
gl = os.path.join(HERE, S, "gloss.txt")
have = set()
if os.path.exists(gl):
    have = {l.split("=", 1)[0].strip() for l in open(gl, encoding="utf-8") if "=" in l}
add, left = [], []
for w in miss:
    if w in have: left.append(w + "  (in gloss.txt but still missing?)"); continue
    if w in pool: add.append(f"{w} = {pool[w]}")
    elif w.lower() in pool: add.append(f"{w} = {pool[w.lower()]}")
    else: left.append(w)
if add:
    with open(gl, "a", encoding="utf-8") as fh: fh.write("\n".join(add) + "\n")
print(f"filled {len(add)} from pool; {len(left)} still missing:")
print(" ".join(left))
print("\n".join(l for l in r.stdout.splitlines() if re.match(r"\s+(ACCENT|SPELL\?|PROBLEM|WARN)", l) and "index.json" not in l))
