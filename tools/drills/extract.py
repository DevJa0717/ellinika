#!/usr/bin/env python3
"""Filter kaikki.org's Greek Wiktionary extract (https://kaikki.org/dictionary/Greek/kaikki.org-dictionary-Greek.jsonl)
down to the words the drill builder needs, into tools/drills/wiktionary-el-extract.jsonl.gz.
Usage: python3 -I tools/drills/extract.py /path/to/kaikki.org-dictionary-Greek.jsonl"""
import gzip, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
lex = []
for f in ("core-1000.json", "core-3000.json"):
    lex += json.load(open(os.path.join(ROOT, "data", "lexicon", f)))
want = {e["lemma"] for e in lex}
for e in lex:
    l = e["lemma"]
    if e["pos"] == "verb" and l.endswith("ώ"): want.add(l[:-1] + "άω")
    if e["pos"] == "verb" and l.endswith("ομαι"): want.add(l[:-4] + "ω")
    if e["pos"] == "noun": want.add(l.lower())
want |= set("ο ένας αυτός εκείνος τούτος ποιος οποίος κάποιος κανένας κανείς όλος τέτοιος τόσος πόσος δικός ίδιος καθένας κάθε άλλος".split())
POS = {"noun", "adj", "verb", "pron", "det", "article", "num", "name"}
n = 0
with gzip.open(os.path.join(ROOT, "tools", "drills", "wiktionary-el-extract.jsonl.gz"), "wt") as out:
    for line in open(sys.argv[1]):
        d = json.loads(line)
        if d.get("word") in want and d.get("pos") in POS and d.get("forms"):
            keep = {k: d[k] for k in ("word", "pos", "forms", "head_templates", "tags") if k in d}
            keep["senses"] = [{"glosses": s.get("glosses"), "tags": s.get("tags")} for s in d.get("senses", [])[:3]]
            out.write(json.dumps(keep, ensure_ascii=False) + "\n"); n += 1
print(n, "entries")
