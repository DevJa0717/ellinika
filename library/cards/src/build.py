#!/usr/bin/env python3
"""Build library/cards/index.json and library/cards/<group>.json (pocket grammar cards) from the plain-text sources here.

One file per group, NN-group.txt (NN gives the order):
  group: <id> | <Greek name> | <English name>
  "# card-id | LEVEL | Greek title | English title"   starts a card (one topic, one printed page)
  blocks separated by blank lines, as in library/pos/src and library/syntax/src:
    | a | b | c          table (first row = header; "|-" lines ignored)
    > Greek || English   examples
    ! text               watch-out callout
    - item               rule list
    @ lesson-id, pos.<doc>~<n>, syntax.<doc>~<n>, cards.<id>   "Go deeper" links (checked here)
    anything else        paragraph (**bold**, *italic*)
Run after library/syntax/src/build.py (cards link to syntax sections and vice versa; run both twice on first build).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
APP = os.path.dirname(os.path.dirname(OUT))
sys.path.insert(0, os.path.join(APP, "library/syntax/src"))
import build as syn  # noqa: E402  (shares the block parser and the link table)


def parse(path):
    text = open(path, encoding="utf-8").read().replace("\r\n", "\n")
    head, _, rest = text.partition("\n# ")
    m = re.match(r"group:\s*(.+)", head.strip())
    if not m:
        sys.exit(f"{path}: needs a 'group:' line")
    gid, gel, gen = [p.strip() for p in m.group(1).split("|")]
    group = {"id": gid, "el": gel, "title": gen, "cards": []}
    for chunk in ("# " + rest).split("\n# "):
        chunk = chunk[2:] if chunk.startswith("# ") else chunk
        first, _, body = chunk.partition("\n")
        parts = [p.strip() for p in first.split("|")]
        if len(parts) != 4:
            sys.exit(f"{path}: bad card header: {first}")
        card = {"id": parts[0], "level": parts[1], "el": parts[2], "title": parts[3], "group": gid, "body": []}
        for blk in re.split(r"\n\s*\n", body.strip()):
            if blk.strip():
                card["body"] += syn.blocks_of(blk, path)
        if any("check" in b for b in card["body"]):
            sys.exit(f"{path}: cards have no exercises ({card['id']})")
        group["cards"].append(card)
    return group


def main():
    links = syn.link_table()
    sdir = os.path.join(APP, "library/syntax")
    if os.path.exists(os.path.join(sdir, "index.json")):
        for it in json.load(open(os.path.join(sdir, "index.json"), encoding="utf-8"))["items"]:
            d = json.load(open(os.path.join(sdir, it["file"]), encoding="utf-8"))
            links["syntax." + d["id"]] = {"href": "#syntax." + d["id"], "kind": "Syntax", "el": d["el"], "title": d["title"]}
            for i, s in enumerate(d["sections"]):
                links[f"syntax.{d['id']}~{i}"] = {"href": f"#syntax.{d['id']}~{i}", "kind": "Syntax", "el": s["el"], "title": s["title"]}
    groups = [parse(os.path.join(HERE, f)) for f in sorted(os.listdir(HERE)) if f.endswith(".txt")]
    ids = [c["id"] for g in groups for c in g["cards"]]
    if len(ids) != len(set(ids)):
        sys.exit("duplicate card ids")
    for g in groups:
        for c in g["cards"]:
            links["cards." + c["id"]] = {"href": "#cards." + c["id"], "kind": "Card", "el": c["el"], "title": c["title"]}
    bad = 0
    for g in groups:
        for c in g["cards"]:
            for b in c["body"]:
                if "links" in b:
                    res = []
                    for x in b["links"]:
                        if x in links: res.append(links[x])
                        else: print(f"  unknown link {x} in card {c['id']}"); bad += 1
                    b["links"] = res
        with open(os.path.join(OUT, g["id"] + ".json"), "w", encoding="utf-8") as fh:
            json.dump(g, fh, ensure_ascii=False, indent=1)
        print(f"{g['id']:12} {len(g['cards']):3} cards")
    idx = {"groups": [{"id": g["id"], "el": g["el"], "title": g["title"], "file": g["id"] + ".json"} for g in groups],
           "cards": [{"id": c["id"], "el": c["el"], "title": c["title"], "level": c["level"], "group": g["id"]} for g in groups for c in g["cards"]]}
    with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as fh:
        json.dump(idx, fh, ensure_ascii=False, indent=1)
    print(f"total: {len(idx['cards'])} cards in {len(groups)} groups")
    if bad:
        sys.exit(f"{bad} unknown links")


if __name__ == "__main__":
    main()
