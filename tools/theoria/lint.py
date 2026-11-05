#!/usr/bin/env python3
"""Lint the grammar-outline sources (library/theoria/src/*.txt) for drafting slips: unfinished asides, options that
contain English commentary, choice items whose answer also appears as a distractor, empty explanations.
Usage: python3 tools/theoria/lint.py [files]"""
import glob, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "../../library/theoria/src")
META = re.compile(r"\?\*\*|\*\*[^*]*\?\*\*|\? no\b|\bno:|is not one|is not in this group|is possible, but|which is wrong|Keep to the|\(this one|the everyday question is|one way;|could be a|is right|is formal;|is possible;|not offered|pick it|choose the form|\bTODO\b")
LAT3 = re.compile(r"[A-Za-z]+\s+[A-Za-z]+\s+[A-Za-z]+")
bad = 0
files = sys.argv[1:] or sorted(glob.glob(os.path.join(SRC, "[0-9][0-9]-*.txt")))
for f in files:
    for n, l in enumerate(open(f, encoding="utf-8"), 1):
        l = l.rstrip("\n")
        msg = []
        if META.search(l):
            msg.append("drafting aside")
        if l.startswith("? "):
            body, _, why = l[2:].partition("||")
            parts = [p.strip() for p in body.split(" | ")]
            for o in parts[1:]:
                pure = sum(1 for x in parts[1:] if not re.search(r"[A-Za-z]", x))
                if LAT3.search(o.lstrip("*")) and pure >= 2:
                    msg.append("English inside an option: " + o)
            if not why.strip():
                msg.append("no explanation")
        if l.startswith(("= ", "S ")) and "=>" not in l:
            msg.append("missing =>")
        if l.startswith(("= ", "~ ")) and "||" not in l:
            msg.append("no explanation")
        if re.match(r"^\s*\|\s*$", l):
            msg.append("stray pipe")
        for m in msg:
            print(f"{os.path.basename(f)}:{n}: {m}: {l[:110]}"); bad += 1
print(f"{bad} lint problems")
sys.exit(1 if bad else 0)
