"""Merge glosses into a chapter: addgloss.py <id> <<'EOF' then lines 'form = lemma — gloss'"""
import json, sys
p = f"/mnt/project-files/app/library/philosophers/{sys.argv[1]}.json"
d = json.load(open(p, encoding="utf-8"))
n = 0
for line in sys.stdin:
    if "=" not in line: continue
    f, g = line.split("=", 1); f, g = f.strip(), g.strip()
    if f and g: d.setdefault("gloss", {})[f] = g; n += 1
json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(n, "glosses added to", sys.argv[1])
