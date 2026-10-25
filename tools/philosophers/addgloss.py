"""Merge glosses into a chapter: addgloss.py <id> [< lines 'form = lemma — gloss'].
Also adds entries from common-gloss.txt (same format) whose form occurs in the chapter's Greek text."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
p = f"/mnt/project-files/app/library/philosophers/{sys.argv[1]}.json"
d = json.load(open(p, encoding="utf-8"))
text = json.dumps(d, ensure_ascii=False)
tokens = set(re.findall(r"[Ͱ-Ͽἀ-῿.]+", text))
tokens |= {t.strip(".") for t in tokens}
def parse(lines):
    for line in lines:
        if "=" in line:
            f, g = line.split("=", 1); f, g = f.strip(), g.strip()
            if f and g: yield f, g
n = 0
common = os.path.join(HERE, "common-gloss.txt")
if os.path.exists(common):
    for f, g in parse(open(common, encoding="utf-8")):
        if f in tokens and f not in d.get("gloss", {}): d.setdefault("gloss", {})[f] = g; n += 1
if not sys.stdin.isatty():
    for f, g in parse(sys.stdin): d.setdefault("gloss", {})[f] = g; n += 1
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(n, "glosses added to", sys.argv[1])
