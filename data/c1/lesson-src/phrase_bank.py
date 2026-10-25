# Builds C1 phrase-bank lessons (c1-bank-*.json) from data/c1/phrases/*.json. Run from /mnt/project-files.
import json, glob, random, unicodedata
def strip(s): return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if unicodedata.category(c) != "Mn").strip()
# phrases already taught in the hand-written C1 lessons
taught = set()
for f in glob.glob("app/lessons/c1-*.json"):
    if "c1-bank-" in f: continue
    t = json.dumps(json.load(open(f)), ensure_ascii=False)
    taught.add(t)
taught = " ".join(taught)
taught_n = strip(taught)
def fresh(items): return [x for x in items if " " not in x["el"].strip() or strip(x["el"]) not in taught_n]
def chunks(xs, n): return [xs[i:i+n] for i in range(0, len(xs), n)]
SETS = [
 ("idioms", "Ιδιωματισμοί", "Idiom bank", "idiom", lambda x: x.get("literal_en", ""), 50),
 ("collocations", "Συνάψεις", "Collocation bank", "collocation", lambda x: x.get("colloquial_equiv", ""), 60),
 ("learned-phrases", "Λόγιες φράσεις", "Learned-phrase bank", "learned phrase", lambda x: x.get("origin_note", ""), 60),
 ("connectors", "Συνδετικά", "Connector bank", "connector", lambda x: x.get("function", ""), 60),
]
out = []
for key, el, title, kind, extra, size in SETS:
    items = fresh(json.load(open(f"data/c1/phrases/{key}.json")))
    head = {"idioms": "Literally", "collocations": "Everyday equivalent", "learned-phrases": "Origin", "connectors": "Function"}[key]
    for i, ch in enumerate(chunks(items, size), 1):
        if len(ch) < 15: continue
        random.seed(f"{key}{i}")
        meanings = [x["meaning_en"] for x in ch]
        mc = [{"prompt": f"**{x['el']}** means…", "answer": x["meaning_en"], "options": [x["meaning_en"]] + random.sample([m for m in meanings if m != x["meaning_en"]], 3), "why": f"*{x['example_el']}* {x['example_en']}"} for x in ch]
        ty = [{"prompt": f"Say in Greek ({kind}): **{x['meaning_en']}**" + (f" (lit. *{x['literal_en']}*)" if key == "idioms" else ""), "answer": x["el"], "why": f"*{x['example_el']}*"} for x in ch]
        lid = f"c1-bank-{key}-{i}"
        L = {"el": f"{el} ({i})", "title": f"{title} {i}: {', '.join(x['el'] for x in ch[:3])}", "section": "C1 · phrase bank",
             "goal": f"Add {len(ch)} more {kind}s to your active repertoire.",
             "blocks": [
               {"type": "text", "text": f"A bank set of {len(ch)} {kind}s from the project's C1 phrase lists (meanings and examples curated against el.wiktionary and the Triantafyllidis dictionary). Read through the table once, then let Practice do the work: it asks for meaning first, then production. Missed items come back at the end of the set."},
               {"type": "table", "title": f"{len(ch)} {kind}s", "head": ["Greek", "Meaning", head, "Example"],
                "rows": [[f"**{x['el']}**", x["meaning_en"], extra(x), f"*{x['example_el']}* {x['example_en']}"] for x in ch]}],
             "practice": [{"gen": "mc", "n": 12, "items": mc}, {"gen": "type", "n": 10, "items": ty}]}
        json.dump(L, open(f"app/lessons/{lid}.json", "w"), ensure_ascii=False, indent=1)
        out.append(lid)
json.dump(out, open("data/c1/lesson-src/bank-ids.json", "w"))
print(len(out), out)
