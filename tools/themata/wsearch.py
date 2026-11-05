#!/usr/bin/env python3
"""wsearch.py [lang:]query : Wikipedia title search (first 6 hits)."""
import sys, json, urllib.request, urllib.parse
q = sys.argv[1]; lang = "en"
if q[2:3] == ":" : lang, q = q[:2], q[3:]
u = f"https://{lang}.wikipedia.org/w/api.php?action=query&list=search&format=json&srlimit=6&srsearch=" + urllib.parse.quote(q)
d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "EllinikaReader/1.0"}), timeout=30))
print(q, "→", " | ".join(h["title"] for h in d["query"]["search"]))
