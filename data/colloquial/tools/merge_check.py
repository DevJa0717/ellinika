"""Merge parts/lex-*.json into colloquial-lexicon.json, parts/sources-*.md into SOURCES.md, and check slang lessons.
Run: python3 -I /mnt/project-files/data/colloquial/tools/merge_check.py"""
import json, glob, os, re
R = "/mnt/project-files"
C = R + "/data/colloquial"
IDS = ["slang-discourse","slang-everyday","slang-idioms","slang-morphology","slang-youth","slang-swearing","slang-insults",
       "slang-nightlife","slang-athens-thessaloniki","slang-crete","slang-cyprus","slang-regions","slang-dialogues"]
core = set()
for f in ["core-1000.json","core-3000.json","core-4000.json"]:
    p = R+"/data/lexicon/"+f
    if os.path.exists(p):
        d = json.load(open(p)); core |= {e["lemma"] for e in (d if isinstance(d,list) else d["entries"])}
out, seen = [], {}
for lid in IDS:
    p = f"{C}/parts/lex-{lid}.json"
    if not os.path.exists(p): continue
    for e in json.load(open(p)):
        e.setdefault("lesson", lid); e.setdefault("source", "colloquial lexicon; entry written by Claude")
        k = e["lemma"]
        if k in seen: seen[k].setdefault("also_in", []).append(lid); continue
        seen[k] = e; out.append(e)
json.dump(out, open(C+"/colloquial-lexicon.json","w"), ensure_ascii=False, indent=1)
src = ["# Sources for the colloquial Greek lessons\n"]
for lid in IDS:
    p = f"{C}/parts/sources-{lid}.md"
    if os.path.exists(p): src.append(f"\n## {lid}\n\n" + open(p).read().strip() + "\n")
open(C+"/SOURCES.md","w").write("".join(src))
lex = core | set(seen)
BL = {"text","table","examples","callout","culture","rules","reading"}; GEN = {"type","mc"}
print(f"lexicon: {len(out)} entries")
for lid in IDS:
    p = f"{R}/app/lessons/{lid}.json"
    if not os.path.exists(p): print(f"{lid}: MISSING"); continue
    try: d = json.load(open(p))
    except Exception as ex: print(f"{lid}: INVALID JSON {ex}"); continue
    probs = []
    for k in ["el","title","blocks","practice","vocab"]:
        if k not in d: probs.append("no "+k)
    for b in d.get("blocks",[]):
        if b.get("type") not in BL: probs.append("block type "+str(b.get("type")))
        if b.get("type")=="table" and any(len(r)!=len(b["head"]) for r in b["rows"]): probs.append("ragged table "+b.get("title",""))
        if b.get("type")=="reading":
            miss = [g for g in b.get("gloss",{}) if g not in b["text"]]
            if miss: probs.append(f"gloss not in text: {miss[:5]}")
            for q in b.get("questions",[]):
                if q["answer"] not in q["options"]: probs.append("reading q answer not in options")
    n = 0
    for s in d.get("practice",[]):
        if s.get("gen") not in GEN: probs.append("gen "+str(s.get("gen")))
        for it in s.get("items",[]):
            n += 1
            if s["gen"]=="mc" and it["answer"] not in it["options"]: probs.append("mc answer not in options: "+it["prompt"][:40])
            if s["gen"]=="type" and it["answer"] not in it.get("accept",[it["answer"]]): probs.append("type answer not in accept: "+it["prompt"][:40])
    vm = [v for v in d.get("vocab",[]) if v not in lex]
    if vm: probs.append(f"vocab not in lexicon: {vm}")
    print(f"{lid}: {os.path.getsize(p)//1024} KB, {len(d.get('blocks',[]))} blocks, {n} practice items" + ("; " + " | ".join(probs) if probs else "; ok"))
