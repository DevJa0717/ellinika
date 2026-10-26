#!/usr/bin/env python3
"""Fact-check helper: python3 wp.py "Title" [regex ...] prints the matching sentences of the English Wikipedia article
(plain-text extract, cached in /tmp/claude-0/wp). Use lang:Title (e.g. el:Τίτλος) for other Wikipedias."""
import sys, json, os, re, urllib.request, urllib.parse
t = sys.argv[1]; lang = "en"
if re.match(r"^[a-z]{2}:", t): lang, t = t[:2], t[3:]
cache = f"/tmp/claude-0/wp/{lang}_{urllib.parse.quote(t, safe='')}.txt"
if not os.path.exists(cache):
    u = f"https://{lang}.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&redirects=1&format=json&titles=" + urllib.parse.quote(t)
    r = urllib.request.Request(u, headers={"User-Agent": "EllinikaReader/1.0 (personal Greek study app)"})
    d = json.load(urllib.request.urlopen(r, timeout=30))
    txt = "\n".join(p.get("extract", "") for p in d["query"]["pages"].values())
    open(cache, "w").write(txt)
txt = open(cache).read()
if len(sys.argv) == 2: print(txt[:3000]); sys.exit()
sents = re.split(r"(?<=[.!?])\s+|\n+", txt)
for pat in sys.argv[2:]:
    for s in sents:
        if re.search(pat, s, re.I): print("•", s.strip()[:400])
