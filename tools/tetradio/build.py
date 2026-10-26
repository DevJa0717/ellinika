#!/usr/bin/env python3
"""Writing workbook (Τετράδιο γραπτού λόγου): builds library/tetradio/*.json from src/*.py.
Usage: python3 tools/tetradio/build.py   (run from anywhere; writes into the repo's library/tetradio/)"""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "src"))
OUT = os.path.join(HERE, "..", "..", "library", "tetradio")
import p1, p2, p3, p4, tools  # noqa: E402

PARTS = [
    dict(id="exam", el="Η εξέταση", en="The exam"),
    dict(id="found", el="Θεμέλια", en="Foundations", level="B1"),
    dict(id="personal", el="Προσωπικά κείμενα · Α΄ μέρος", en="Personal texts · Part A", level="B1–B2"),
    dict(id="formal", el="Επίσημα κείμενα · Β΄ μέρος", en="Formal texts · Part B", level="B2"),
    dict(id="argue", el="Γνώμη και επιχειρηματολογία", en="Opinion and argument", level="B2+–C1"),
    dict(id="tools", el="Εργαλεία", en="Tools"),
]
GREEK = re.compile(r"[Ͱ-Ͽἀ-῿]+")

def words(paras):
    return sum(len(GREEK.findall(p)) for p in paras)

def main():
    items = p1.ITEMS + p2.ITEMS + p3.ITEMS + p4.ITEMS + tools.ITEMS
    os.makedirs(OUT, exist_ok=True)
    ids = set()
    idx = []
    gloss = tools.GLOSS
    for it in items:
        assert it["id"] not in ids, it["id"]; ids.add(it["id"])
        assert it["part"] in {p["id"] for p in PARTS}, it["id"]
        for m in it.get("models", []):
            assert len(m["text"]) == len(m["text_en"]), (it["id"], m["el"], len(m["text"]), len(m["text_en"]))
            m["words"] = words(m["text"])
        for t in it.get("tasks", []):
            if t.get("model"):
                assert len(t["model"]) == len(t["model_en"]), (t["id"], len(t["model"]), len(t["model_en"]))
                t["model_words"] = words(t["model"])
        it["gloss"] = {**gloss, **it.get("gloss", {})}
        with open(os.path.join(OUT, it["id"] + ".json"), "w", encoding="utf-8") as f:
            json.dump(it, f, ensure_ascii=False, indent=1)
        idx.append(dict(id=it["id"], file=it["id"] + ".json", kind=it["kind"], part=it["part"], level=it["level"], el=it["el"], title=it["title"],
                        tasks=[t["id"] for t in it.get("tasks", [])], models=len(it.get("models", [])) + sum(1 for t in it.get("tasks", []) if t.get("model")),
                        drills=len(it.get("drills", []))))
    index = dict(kind="workbook", el="Τετράδιο γραπτού λόγου", title="Writing workbook: graded letters, emails, opinion pieces and essays for the B2 writing paper",
                 parts=PARTS, items=idx)
    with open(os.path.join(OUT, "index.json"), "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=1)
    nm = sum(i["models"] for i in idx); nt = sum(len(i["tasks"]) for i in idx); nd = sum(i["drills"] for i in idx)
    print(f"tetradio: {len(idx)} items, {nm} model texts, {nt} tasks, {nd} drill questions")

if __name__ == "__main__":
    main()
