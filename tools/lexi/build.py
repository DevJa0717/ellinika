#!/usr/bin/env python3
"""Data for the frequency-ranked vocabulary course (#lexi, lexi.js).

Reads data/lexicon/core-1000.json + core-3000.json + collocations.json and writes library/lexi/:
  index.json            band list (500 words each, by freq_rank) with CEFR spread and part-of-speech counts
  lemmas.json           the lemmas of every band (for progress counts without loading the bands)
  band-01.json …        one file per band: compact word records for study, review and the word list
Record: {r: rank, l: lemma, a: article or "", p: pos, g: gloss, h: grammar header (form_key), x: [example el, en],
         c: [[collocation el, en], …] (up to 3), alt: other accepted answers (same-gloss lemmas, slash variants)}
Usage: python3 tools/lexi/build.py
"""
import json, os, re, collections
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
LEX = os.path.join(ROOT, "data", "lexicon")
OUT = os.path.join(ROOT, "library", "lexi")
BAND = 500
ART = {"m": "ο", "f": "η", "n": "το"}

entries = [e for f in ("core-1000.json", "core-3000.json") for e in json.load(open(os.path.join(LEX, f), encoding="utf-8"))]
entries.sort(key=lambda e: e["freq_rank"])
col = json.load(open(os.path.join(LEX, "collocations.json"), encoding="utf-8"))["entries"]
by_gloss = collections.defaultdict(list)
for e in entries:
    by_gloss[e["gloss"].strip().lower()].append(e["lemma"])

def rec(e):
    n = e.get("noun") or {}
    art = ""
    if e["pos"] == "noun" and n.get("gender") in ART and not n.get("pl_only"):
        art = ART[n["gender"]]
    elif e["pos"] == "noun" and n.get("pl_only") and n.get("gender") in ART:
        art = {"m": "οι", "f": "οι", "n": "τα"}[n["gender"]]
    ex = e.get("example") or {}
    cs = [[c["el"], c["en"]] for c in (col.get(e["lemma"], {}).get("collocations") or [])[:3]]
    alt = [l for l in by_gloss[e["gloss"].strip().lower()] if l != e["lemma"]][:4]
    alt += [v.strip() for v in re.split(r"\s*/\s*", e["lemma"]) if v.strip() and v.strip() != e["lemma"]]
    r = {"r": e["freq_rank"], "l": e["lemma"], "a": art, "p": e["pos"], "g": e["gloss"], "h": e.get("form_key") or ""}
    if ex.get("el"): r["x"] = [ex["el"], ex.get("en", "")]
    if cs: r["c"] = cs
    if alt: r["alt"] = alt
    return r

os.makedirs(OUT, exist_ok=True)
bands = []
for i in range(0, len(entries), BAND):
    chunk = entries[i:i + BAND]
    no = i // BAND + 1
    recs = [rec(e) for e in chunk]
    json.dump(recs, open(os.path.join(OUT, f"band-{no:02d}.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    cefr = collections.Counter(e.get("cefr_est") or "?" for e in chunk)
    pos = collections.Counter(e["pos"] for e in chunk)
    bands.append({"n": no, "from": chunk[0]["freq_rank"], "to": chunk[-1]["freq_rank"], "count": len(chunk),
                  "cefr": dict(cefr.most_common()), "pos": dict(pos.most_common(4)),
                  "sample": [e["lemma"] for e in chunk[:8]]})
json.dump([[e["lemma"] for e in entries[i:i + BAND]] for i in range(0, len(entries), BAND)],
          open(os.path.join(OUT, "lemmas.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
json.dump({"about": "Frequency-ranked vocabulary course: every word of the app's lexicon in bands of 500 by corpus frequency "
           "(wordfreq / subtitles / news counts; ranks after ~11,600 are topic and exam words with no corpus count, in the order they were added).",
           "band": BAND, "total": len(entries), "bands": bands},
          open(os.path.join(OUT, "index.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(bands), "bands,", len(entries), "words ->", OUT)
