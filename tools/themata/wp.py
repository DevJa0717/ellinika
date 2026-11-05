#!/usr/bin/env python3
"""Fact-check helper (copy of tools/themed-readers/wp.py with polite retries on HTTP 429).
python3 wp.py "Title" [regex ...]  · lang:Title for other Wikipedias (el:Τίτλος). Cache: /tmp/claude-0/wp."""
import sys, json, os, re, time, urllib.request, urllib.parse, urllib.error
t = sys.argv[1]; lang = "en"
if re.match(r"^[a-z]{2}:", t): lang, t = t[:2], t[3:]
os.makedirs("/tmp/claude-0/wp", exist_ok=True)
cache = f"/tmp/claude-0/wp/{lang}_{urllib.parse.quote(t, safe='')}.txt"
if not os.path.exists(cache):
    u = f"https://{lang}.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&redirects=1&format=json&titles=" + urllib.parse.quote(t)
    for i in range(6):
        try:
            r = urllib.request.Request(u, headers={"User-Agent": "EllinikaReader/1.0 (personal Greek study app; contact via github.com/DevJa0717/ellinika)"})
            d = json.load(urllib.request.urlopen(r, timeout=30)); break
        except urllib.error.HTTPError as e:
            if e.code != 429: raise
            time.sleep(int(e.headers.get("Retry-After") or 0) or 10 * (i + 1))
    else: sys.exit("429 persists")
    txt = "\n".join(p.get("extract", "") for p in d["query"]["pages"].values())
    open(cache, "w").write(txt)
txt = open(cache).read()
if len(sys.argv) == 2: print(txt[:3000]); sys.exit()
sents = re.split(r"(?<=[.!?])\s+|\n+", txt)
for pat in sys.argv[2:]:
    for s in sents:
        if re.search(pat, s, re.I): print("•", s.strip()[:400])
