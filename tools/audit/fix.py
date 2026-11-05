#!/usr/bin/env python3
"""Apply one text correction everywhere it occurs (built JSON *and* the generator sources, so a rebuild keeps it)
and log it. 2026-11-05, "Validate all content end to end".

Usage: python3 tools/audit/fix.py "old text" "new text" "why" [--in library/simera] [--log ledger/audit-2026-11-05-corrections.md]
Searches library/, lessons/, data/, tools/ (.json .txt .py .js .md, skipping tools/audit and ledger), refuses to
touch a JSON file it would leave invalid, prints every file changed, appends one line to the log.
"""
import json, os, sys

args = sys.argv[1:]
def opt(k, d):
    if k in args:
        i = args.index(k); v = args[i + 1]; del args[i:i + 2]; return v
    return d
LOG = opt("--log", "ledger/audit-2026-11-05-corrections.md")
SCOPE = opt("--in", None)
old, new, why = args[0], args[1], (args[2] if len(args) > 2 else "")
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
roots = [SCOPE] if SCOPE else ["library", "lessons", "data", "tools", "deploy"]
changed = []
for r in roots:
    for d, _, fs in os.walk(os.path.join(ROOT, r)):
        if "/tools/audit" in d or "/node_modules" in d or "__pycache__" in d: continue
        for f in fs:
            if not f.endswith((".json", ".txt", ".py", ".js", ".md", ".lst")): continue
            p = os.path.join(d, f)
            try: s = open(p, encoding="utf-8").read()
            except Exception: continue
            # JSON-escaped variant for generator sources that hold JSON-ish strings
            if old not in s: continue
            t = s.replace(old, new)
            if f.endswith(".json"):
                try: json.loads(t)
                except Exception as e: print(f"SKIP (would break JSON) {p}: {e}"); continue
            open(p, "w", encoding="utf-8").write(t)
            changed.append(os.path.relpath(p, ROOT))
if not changed: sys.exit(f"not found: {old!r}")
for c in changed: print("fixed", c)
with open(os.path.join(ROOT, LOG), "a", encoding="utf-8") as L:
    L.write(f"- {', '.join('`' + c + '`' for c in changed)}: {old} → {new}" + (f" ({why})" if why else "") + "\n")
