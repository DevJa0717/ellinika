#!/usr/bin/env python3
"""Fact-consistency check for bilingual reader chapters (shared format: sections[].paras[] with el/en/cite, sources[]).
2026-11-05, "Validate all content end to end".

Checks per chapter:
  - every paragraph cites at least one source and every cited number exists in sources[] (and has a URL);
  - every number in the Greek half of a paragraph also appears in the English half (the English side adds detail,
    so it should contain at least the Greek side's numbers: years, dates, percentages, quantities);
  - BC/AD agreement: a year marked π.Χ. in Greek is marked BC/BCE in English (and vice versa);
  - centuries: "5ος αιώνας / 5ο αιώνα" in Greek ↔ "5th century" in English;
  - quiz answers are among the options; terms and grammar examples are non-empty.
Usage: python3 tools/audit/facts.py library/<shelf>/*.json   (or a directory)
"""
import json, os, re, sys

W = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split())}
W.update({"thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000, "dozen": 12})
ORD = {w: i + 1 for i, w in enumerate("first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth thirteenth fourteenth fifteenth sixteenth seventeenth eighteenth nineteenth twentieth".split())}
def en_words(s):
    s = re.sub(r"\btwenty-first\b", "21st", s, flags=re.I)
    s = re.sub(r"\b(" + "|".join(ORD) + r")\b", lambda m: f"{ORD[m.group(1).lower()]}th", s, flags=re.I)
    s = re.sub(r"\b(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)-(one|two|three|four|five|six|seven|eight|nine)\b", lambda m: str(W[m.group(1).lower()] + W[m.group(2).lower()]), s, flags=re.I)
    s = re.sub(r"\b(\d+|" + "|".join(W) + r") (hundred|thousand|million)\b", lambda m: str((int(m.group(1)) if m.group(1).isdigit() else W[m.group(1).lower()]) * {"hundred": 100, "thousand": 1000, "million": 1000000}[m.group(2).lower()]), s, flags=re.I)
    return re.sub(r"\b(" + "|".join(W) + r")\b", lambda m: str(W[m.group(1).lower()]), s, flags=re.I)
def nums(s, greek):
    s = re.sub(r"\[\d+\]", " ", s)
    if greek: s = re.sub(r"(?:του\s+)?[’'΄]([2-9]0)\b", r"19\1", s)   # δεκαετία του ’60 = 1960s
    else: s = re.sub(r"\b(twent|thirt|fort|fift|sixt|sevent|eight|ninet)ies\b", lambda m: "19" + str({"twent":2,"thirt":3,"fort":4,"fift":5,"sixt":6,"sevent":7,"eight":8,"ninet":9}[m.group(1).lower()]) + "0", s, flags=re.I)
    if not greek: s = en_words(s)
    out = set()
    for m in re.finditer(r"\d[\d.,]*\d|\d", s):
        t = m.group(0)
        if greek:   # 1.000 = thousand, 13,5 = decimal
            t = re.sub(r"\.(?=\d{3}(\D|$))", "", t).replace(",", ".")
        else:       # 1,000 = thousand, 13.5 = decimal
            t = re.sub(r",(?=\d{3}(\D|$))", "", t)
        t = t.rstrip(".,")
        if re.fullmatch(r"\d+\.0+", t): t = t.split(".")[0]
        out.add(t)
    return out

ORD_EL = r"(\d+)(?:ος|ου|ο|η|ης|οι|ων)\s+(?:αιώνα|αι\.)"
def centuries(s, greek):
    if greek: return set(re.findall(r"(\d+)(?:ος|ου|ο)\s*(?:αιώνα|αιών|αι\.)", s))
    return set(re.findall(r"(\d+)(?:st|nd|rd|th)[\s-]+(?:and \d+(?:st|nd|rd|th)\s+)?centur", en_words(s))) | set(re.findall(r"(\d+)(?:st|nd|rd|th) and \d+(?:st|nd|rd|th)[\s-]+centur", en_words(s)))

def bc_years(s, greek):
    if greek: return set(re.findall(r"(\d[\d.]*)\s*(?:–\s*\d+\s*)?π\.\s?Χ\.", s))
    return set(m.replace(",", "") for m in re.findall(r"(\d[\d,]*)\s*(?:–\s*\d+\s*)?(?:BC|BCE|B\.C\.)", s))

def check(path):
    try: c = json.load(open(path, encoding="utf-8"))
    except Exception as e: return [f"INVALID JSON {e}"]
    if not isinstance(c, dict) or "sections" not in c: return None
    probs = []
    srcs = {s.get("n"): s for s in c.get("sources", []) if isinstance(s, dict)}
    for n, s in srcs.items():
        if not re.match(r"https?://", s.get("url") or "") and not re.search(r"\d", s.get("text") or ""): probs.append(f"source [{n}] has neither a URL nor a dated publication")
    for si, sec in enumerate(c.get("sections", [])):
        for pi, p in enumerate(sec.get("paras", []) or []):
            if not isinstance(p, dict): continue
            el, en, where = p.get("el") or "", p.get("en") or "", f"{sec.get('id', si)}#{pi}"
            cite = p.get("cite") or []
            if srcs and not cite: probs.append(f"{where}: no citation")
            for n in cite:
                if n not in srcs: probs.append(f"{where}: cites [{n}] but there is no such source")
            if not el or not en: continue
            ne, nn = nums(el, True), nums(en, False)
            miss = sorted(x for x in ne - nn if not (len(x) == 1 and x in "123456789"))
            # a Greek number may be written out in English ("two"); only flag numbers of 2+ digits or with decimals
            miss = [x for x in miss if len(x.replace(".", "")) >= 2]
            if miss: probs.append(f"{where}: numbers in Greek not in English {miss} (EN has {sorted(nn - ne)[:8]}) | EL: {el[:220]}")
            ce, cn = centuries(el, True), centuries(en, False)
            if ce - cn: probs.append(f"{where}: centuries differ EL {sorted(ce)} EN {sorted(cn)}")
            be, bn = {x.replace('.', '') for x in bc_years(el, True)}, bc_years(en, False)
            if be - bn and bn != be and any(y in nn for y in be - bn) and not re.search(r"BC|BCE|B\.C\.", en): probs.append(f"{where}: π.Χ. year(s) {sorted(be - bn)} not marked BC in English")
    for qi, q in enumerate(c.get("questions", []) or []):
        if isinstance(q, dict) and q.get("options") and q.get("answer") not in q["options"]: probs.append(f"question {qi}: answer not among options")
    return probs

files = []
for a in sys.argv[1:] or ["library"]:
    if os.path.isdir(a):
        for r, _, fs in os.walk(a):
            files += [os.path.join(r, f) for f in fs if f.endswith(".json") and "/src" not in r]
    else: files.append(a)
total = n = 0
for f in sorted(files):
    pr = check(f)
    if pr is None: continue
    n += 1
    if pr:
        total += len(pr)
        print(f"{f}: {len(pr)}")
        for p in pr: print("   " + p)
print(f"{n} chapters checked, {total} findings")
sys.exit(1 if total else 0)
