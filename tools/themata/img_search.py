#!/usr/bin/env python3
"""img_search.py "query" [n] : Openverse CC0/PDM image candidates (id, size, title, creator, source)."""
import sys, json, urllib.request, urllib.parse
q = sys.argv[1]; n = int(sys.argv[2]) if len(sys.argv) > 2 else 5
u = "https://api.openverse.org/v1/images/?license=cc0,pdm&page_size=20&q=" + urllib.parse.quote(q)
d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "EllinikaReader/1.0"}), timeout=30))
k = 0
for r in d.get("results", []):
    if (r.get("width") or 0) < 800: continue
    print(f'{r["id"]} {r.get("width")}x{r.get("height")} [{r["license"]}] {r.get("title","")[:70]} | {r.get("creator","")[:30]} | {r.get("foreign_landing_url","")}')
    k += 1
    if k >= n: break
