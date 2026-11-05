#!/usr/bin/env python3
"""check_sources.py <shelf> : every source URL resolves (Wikipedia titles batched via the API, others via curl; 403 = bot block)."""
import importlib.util, urllib.request, urllib.parse, time, json, subprocess, sys, os
spec = importlib.util.spec_from_file_location("s", os.path.join(os.path.dirname(os.path.abspath(__file__)), sys.argv[1], "sources.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
bad = 0; wiki = {}
for k, (t, u) in m.SRC.items():
    if not u: continue
    if "wikipedia.org/wiki/" in u:
        lang = u.split("//")[1][:2]; title = urllib.parse.unquote(u.split("/wiki/")[1]).split("#")[0].replace("_", " ")
        wiki.setdefault(lang, []).append((k, title))
    else:
        code = subprocess.run(["curl", "-s", "-o", "/dev/null", "-m", "15", "-L", "-A", "Mozilla/5.0", "-w", "%{http_code}", u], capture_output=True, text=True).stdout
        if code not in ("200", "403"): print(code, k, u, flush=True); bad += 1
for lang, items in wiki.items():
    for i in range(0, len(items), 40):
        chunk = items[i:i+40]
        q = f"https://{lang}.wikipedia.org/w/api.php?action=query&format=json&redirects=1&titles=" + urllib.parse.quote("|".join(t for _, t in chunk))
        d = None
        for n in range(8):
            try: d = json.load(urllib.request.urlopen(urllib.request.Request(q, headers={"User-Agent": "EllinikaReader/1.0"}), timeout=20)); break
            except Exception as e: print("retry", e, flush=True); time.sleep(10 * (n + 1))
        missing = {p["title"] for p in d["query"]["pages"].values() if "missing" in p}
        norm = {x["from"]: x["to"] for x in d["query"].get("normalized", [])}
        for k, t in chunk:
            if norm.get(t, t) in missing: print("MISSING", k, t, flush=True); bad += 1
print("bad:", bad)
