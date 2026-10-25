# Writes data/c1/course-c1-units.json from the C1 lesson files present (run from /mnt/project-files).
import json, os
U = [("C1 · Unit 12","Learned morphology",["c1-internal-augment","c1-active-participles","c1-present-participles","c1-learned-nouns","c1-learned-verbs","c1-learned-phrases"]),
     ("C1 · Unit 13","Argument and register",["c1-nominal-style","c1-register","c1-connectors","c1-collocations","c1-hedging","c1-emphasis"]),
     ("C1 · Unit 14","Idiom and the living tradition",["c1-idioms-1","c1-idioms-2","c1-ancient-sayings","c1-language-question","c1-read-register-speeches"]),
     ("C1 · Unit 15","Reading at C1",["c1-read-philosophy","c1-read-history","c1-read-society","c1-read-science-tech","c1-read-law","c1-read-press","c1-read-cavafy","c1-read-prose"]),
     ("C1 · Unit 16","Γ1 exam practice",["c1-exam-reading","c1-exam-language"]),
     ("C1 · Unit 17","Phrase bank",json.load(open("data/c1/lesson-src/bank-ids.json")) if os.path.exists("data/c1/lesson-src/bank-ids.json") else [])]
out = []
for label, title, ids in U:
    ls = []
    for i in ids:
        f = f"app/lessons/{i}.json"
        if not os.path.exists(f): continue
        d = json.load(open(f)); e = {"id": i, "el": d["el"], "title": d["title"], "file": i + ".json"}
        if i == "c1-internal-augment": e["holton"] = "6.23"
        ls.append(e)
    if ls: out.append({"label": label, "title": title, "lessons": ls})
json.dump({"note": "Append these units to course.json after B2 Unit 11 (C1 lessons; files already in app/lessons/).", "units": out}, open("data/c1/course-c1-units.json", "w"), ensure_ascii=False, indent=1)
print(sum(len(u["lessons"]) for u in out), "lessons in", len(out), "units")
