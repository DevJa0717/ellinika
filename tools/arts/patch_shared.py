#!/usr/bin/env python3
"""Idempotent small edits to shared files for the mousiki/skini/eortes shelves (arts readers thread).
Usage: python3 patch_shared.py <root>   where <root> holds bilingual.js (app root: repo root or /mnt/project-files/app)
and optionally deploy/textbook/build_bilingual.py (repo root or /mnt/project-files)."""
import os, re, sys
root = sys.argv[1]
ADD = {"mousiki": "Greek music", "skini": "Theatre and cinema", "eortes": "The Orthodox year"}

def patch(path, fn):
    if not os.path.exists(path): print("skip", path); return
    s = open(path, encoding="utf-8").read(); t = fn(s)
    if t != s: open(path, "w", encoding="utf-8").write(t); print("patched", path)
    else: print("unchanged", path)

def viewer(s):
    m = re.search(r"const SHELVES = \{([^}]*)\};", s)
    body = m.group(1).rstrip()
    for k, v in ADD.items():
        if f"{k}:" not in body: body += f', {k}: "{v}"'
    body += " "
    s = s[:m.start(1)] + body + s[m.end(1):]
    if "bl-listen" not in s:
        s = s.replace(".bl-src ol {", ".bl-listen ul { margin: 0; padding-left: 20px; } .bl-listen li { margin: 0 0 8px; overflow-wrap: anywhere; } .bl-listen .ex-en { display: block; }\n.bl-src ol {", 1)
        anchor = "      ${ch.sources?.length ? `<section class=\"bl-sec bl-src\""
        assert anchor in s, "viewer anchor not found"
        s = s.replace(anchor, "      ${ch.listen?.length ? `<section class=\"card bl-sec bl-listen no-look\" id=\"bl-listen\"><h3><span class=\"el\" lang=\"el\">Ακούστε και δείτε</span>Listen and watch</h3><ul>${ch.listen.map((l) => `<li><a href=\"${E.esc(l.url)}\" target=\"_blank\" rel=\"noopener\">${E.esc(l.title)}</a>${l.note ? `<span class=\"ex-en\">${E.esc(l.note)}</span>` : \"\"}</li>`).join(\"\")}</ul></section>` : \"\"}\n" + anchor, 1)
    return s

def pdf(s):
    if 'c.get("listen")' in s: return s
    anchor = '            if c.get("sources"):\n                h.append(\'<div class="srcs">'
    assert anchor in s, "pdf anchor not found"
    add = ('            if c.get("listen"):\n'
           '                h.append(\'<div class="srcs"><div class="box-h">Ακούστε και δείτε · Listen and watch</div><ul>\' + "".join(\n'
           '                    f\'<li><span lang="el">{esc(l["title"])}</span> {esc(l["url"])}{" · " + esc(l["note"]) if l.get("note") else ""}</li>\' for l in c["listen"]) + "</ul></div>")\n')
    return s.replace(anchor, add + anchor, 1)

patch(os.path.join(root, "bilingual.js"), viewer)
patch(os.path.join(root, "deploy/textbook/build_bilingual.py"), pdf)
