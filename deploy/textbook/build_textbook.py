#!/usr/bin/env python3
"""Companion textbook: one HTML book per CEFR level, built from the app's lessons and data.

Usage: python3 build_textbook.py [A1 A2 B1 B2 C1]
Writes <out>/<level>.html; render_pdf.js turns them into PDFs.
Sources: app/lessons (course.json order), app/library, data/grammar, data/lexicon, data/colloquial, data/c1.
"""
import html, json, os, random, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from covers_el import el_date, el_level
from collections import OrderedDict

ROOT = "/mnt/project-files"
APP, DATA = f"{ROOT}/app", f"{ROOT}/data"
LESS, LIB = f"{APP}/lessons", f"{APP}/library"
OUT = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else f"{ROOT}/downloads/textbook/build"
LEVELS = ["A1", "A2", "B1", "B2", "C1"]

_cache = {}
def J(path):
    if path not in _cache:
        with open(path, encoding="utf-8") as f:
            _cache[path] = json.load(f)
    return _cache[path]

def resolve(ref):
    file, _, path = ref.partition("#")
    obj = J(f"{DATA}/{file}")
    if not path:
        return obj
    for part in re.findall(r"[^.\[\]]+(?:\[[^\]]+\])?", path):
        m = re.match(r"^([^\[]+)(?:\[([^=\]]+)=([^\]]+)\])?$", part)
        obj = obj.get(m.group(1)) if isinstance(obj, dict) else None
        if m.group(2):
            obj = next((x for x in (obj or []) if str(x.get(m.group(2))) == m.group(3)), None)
    return obj

# ---------- text helpers (same markdown subset as app.js) ----------
def esc(s):
    return html.escape("" if s is None else str(s), quote=True)

def md(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    return s

def paras(s, cls=""):
    c = f' class="{cls}"' if cls else ""
    return "".join(f"<p{c}>{md(p).replace(chr(10), '<br>')}</p>" for p in re.split(r"\n\n+", str(s or "")) if p.strip())

def gr(s):
    return f'<span lang="el">{esc(s)}</span>'

_ids = {}
def anchor(text):
    base = re.sub(r"[^a-z0-9]+", "-", str(text).lower()).strip("-") or "s"
    n = _ids.get(base, 0); _ids[base] = n + 1
    return base if not n else f"{base}-{n}"

# ---------- lexicon ----------
LEX = OrderedDict()
for f in ["lexicon/core-1000.json", "lexicon/core-3000.json", "colloquial/colloquial-lexicon.json"]:
    d = J(f"{DATA}/{f}")
    for e in d if isinstance(d, list) else d.get("entries", []):
        LEX.setdefault(e["lemma"], e)
COLLOC = J(f"{DATA}/lexicon/collocations.json")["entries"]
ART = {"m": "ο", "f": "η", "n": "το"}
def with_art(e):
    g = (e.get("noun") or {}).get("gender")
    return f"{ART[g]} {e['lemma']}" if e.get("pos") == "noun" and g in ART else e["lemma"]

POS = {"noun": "n.", "verb": "v.", "adjective": "adj.", "adverb": "adv.", "preposition": "prep.", "conjunction": "conj.",
       "pronoun": "pron.", "particle": "part.", "article": "art.", "numeral": "num.", "interjection": "interj.", "phrase": "phr."}

# ---------- block renderers (mirror app.js BLOCKS) ----------
PERSONS = [("1sg", "εγώ"), ("2sg", "εσύ"), ("3sg", "αυτός/ή/ό"), ("1pl", "εμείς"), ("2pl", "εσείς"), ("3pl", "αυτοί/ές/ά")]

def rule_item(r):
    if r is None:
        return ""
    if not isinstance(r, dict):
        return md(r)
    text = r.get("rule") or r.get("text") or r.get("note") or r.get("description") or r.get("en") or ""
    exs = r.get("examples") or r.get("example") or []
    if not isinstance(exs, list):
        exs = [exs]
    out = []
    for x in exs:
        if isinstance(x, dict):
            s = gr(x.get("el") or x.get("form") or "")
            if x.get("ipa"): s += f" [{esc(x['ipa'])}]"
            if x.get("en") or x.get("gloss"): s += f' <span class="en">{esc(x.get("en") or x.get("gloss"))}</span>'
            out.append(s)
        else:
            out.append(gr(x))
    head = md(text) if text else (gr(r.get("el")) + (f' <span class="en">{esc(r["en"])}</span>' if r.get("en") else "") if r.get("el") else "")
    return head + ("<br>" + " · ".join(out) if out else "")

def h3(t, el=False):
    return f'<h4{" lang=\"el\"" if el else ""}>{esc(t)}</h4>' if t else ""

def tbl(head, rows, cls="", big_first=False, raw=False):
    th = "".join(f"<th>{esc(h)}</th>" for h in head) if head else ""
    body = "".join("<tr>" + "".join(f'<td{" class=\"big\"" if i == 0 and big_first else ""}>{c if raw else md(c)}</td>' for i, c in enumerate(r)) + "</tr>" for r in rows)
    return f'<table class="{cls}">{"<thead><tr>" + th + "</tr></thead>" if th else ""}<tbody>{body}</tbody></table>'

def gloss_box(g):
    if not g:
        return ""
    items = []
    for k, v in g.items():
        v = str(v)
        items.append(f"<li>{gr(k)} <span class=\"en\">{esc(v)}</span></li>" if " — " not in v else
                     f"<li>{gr(k)} · {gr(v.split(' — ', 1)[0])} <span class=\"en\">{esc(v.split(' — ', 1)[1])}</span></li>")
    return f'<div class="gloss"><div class="gl-h">Glossary</div><ul>{"".join(items)}</ul></div>'

def b_text(b): return h3(b.get("title")) + paras(b.get("text"))
def b_callout(b): return f'<div class="callout">{paras(b.get("text"))}</div>'
def b_culture(b): return f'<div class="culture"><div class="eyebrow">Πολιτισμός · culture</div>{h3(b.get("title"))}{paras(b.get("text"))}</div>'

def b_reading(b):
    en = f'<div class="trans"><div class="gl-h">Translation</div>{paras(b["en"])}</div>' if b.get("en") else ""
    return (f'<div class="reading"><div class="eyebrow">Ανάγνωση · reading</div><h4 lang="el">{esc(b.get("title"))}</h4>'
            f'<div class="rd" lang="el">{paras(b.get("text"))}</div>{en}{gloss_box(b.get("gloss"))}</div>')

def dialogue_html(title, setting, lines, gloss=None, eyebrow="Διάλογος · dialogue transcript"):
    rows = "".join(f'<tr><td class="who" lang="el">{esc(l.get("who") or l.get("speaker") or "")}</td><td class="el" lang="el">{esc(l.get("el"))}</td><td class="en">{esc(l.get("en") or "")}</td></tr>' for l in lines)
    return (f'<div class="dialogue"><div class="eyebrow">{eyebrow}</div><h4 lang="el">{esc(title)}</h4>'
            f'{f"<p class=sub>{esc(setting)}</p>" if setting else ""}<table class="dl">{rows}</table>{gloss_box(gloss)}</div>')

def b_dialogue(b): return dialogue_html(b.get("title"), b.get("setting"), b.get("lines", []), b.get("gloss"))

def b_rules(b):
    lst = b.get("items") or resolve(b["src"])
    if isinstance(lst, str): lst = [lst]
    lst = lst or []
    if b.get("pick"): lst = [lst[i] for i in b["pick"] if i < len(lst)]
    return h3(b.get("title")) + "<ul>" + "".join(f"<li>{rule_item(r)}</li>" for r in lst) + "</ul>"

def b_examples(b):
    lst = b.get("items") or resolve(b["src"]) or []
    if b.get("limit"): lst = lst[: b["limit"]]
    rows = []
    for x in lst:
        el = esc(x.get("el")) + (f' <span class="ipa">[{esc(x["ipa"])}]</span>' if x.get("ipa") else "")
        rows.append(f'<tr><td class="el" lang="el">{el}</td><td class="en">{esc(x.get("en") or x.get("use") or x.get("function") or "")}</td></tr>')
    return h3(b.get("title")) + f'<table class="ex">{"".join(rows)}</table>'

def b_table(b):
    return h3(b.get("title")) + tbl(b.get("head"), b.get("rows", []), big_first=b.get("bigFirst"))

def b_alphabet(b):
    abc = resolve("grammar/alphabet-phonology.json#alphabet")
    return tbl(["Letter", "Name", "Sound"], [[f'<span class="big" lang="el">{esc(l["upper"])} {esc(l["lower"])}</span>', f'{gr(l["name"])} <span class="ipa">[{esc(l["name_ipa"])}]</span>', esc(l["sound"])] for l in abc], raw=True)

def b_digraphs(b):
    d = resolve("grammar/alphabet-phonology.json#digraphs")
    rows = [[x["spelling"], x["sound"], ""] for x in d["vowel"]]
    rows += [[x["spelling"], x["sound"], f"inside a word: {x['word_internal']}" if x.get("word_internal") else ", ".join(e["el"] for e in x.get("examples", []))] for x in d["consonant"]]
    rows += [[x["spelling"], f"{x['before_vowel_or_voiced']} / {x['before_voiceless_or_final']}", ", ".join(f"{e['el']} [{e['ipa']}]" for e in x.get("examples", [])) or x.get("note", "")] for x in d["vowel_plus_upsilon"]]
    return tbl(["Spelling", "Sound", "Notes"], [[f'<span class="big" lang="el">{esc(a)}</span>', f"[{esc(s)}]", esc(n)] for a, s, n in rows], raw=True) + f'<p class="sub">{esc(d.get("double_consonants"))}</p>'

def b_article(b):
    a = resolve(b.get("src") or "grammar/nouns-full.json#articles.definite")
    cases = b.get("cases") or ["nom", "acc", "gen"]
    rows = [[f"<b>{c} {num}</b>"] + [gr(a[num][g][c]) for g in "mfn"] for num in ("sg", "pl") for c in cases]
    return h3(b.get("title")) + tbl(["", "masc.", "fem.", "neut."], rows, cls="pdg", raw=True)

def noun_paradigm(ps, cases, title=None):
    def cell(p, num, c):
        f = (p.get(num) or {}).get(c) or (p.get(f"voc_{num}") if c == "voc" else "")
        # vocative = nominative in the plural, and in the singular of feminines and neuters
        if not f and c == "voc" and (num == "pl" or p.get("gender") in ("f", "n")): f = (p.get(num) or {}).get("nom", "")
        return f or ""
    rows = [[f"<b>{c} {num}</b>"] + [gr(cell(p, num, c)) for p in ps] for num in ("sg", "pl") for c in cases]
    head = "<tr><th></th>" + "".join(f'<th><span lang="el">{esc(p.get("model"))}</span><br><span class="ipa">{esc(p.get("gloss"))}</span></th>' for p in ps) + "</tr>"
    body = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    notes = "".join(f'<p class="sub"><strong lang="el">{esc(p["model"])}</strong>: {md(p["stress"])}</p>' for p in ps if p.get("stress"))
    return h3(title) + f'<table class="pdg"><thead>{head}</thead><tbody>{body}</tbody></table>{notes}'

def b_noun_paradigm(b):
    ps = [p for p in (resolve(s) for s in b["src"]) if p]
    return noun_paradigm(ps, b.get("cases") or ["nom", "acc", "gen", "voc"], b.get("title"))

def b_verb_paradigm(b):
    cols = [resolve(c["src"]) or {} for c in b["columns"]]
    rows = [[f'<b lang="el">{pro}</b>'] + [gr(c.get(k, "")) for c in cols] for k, pro in PERSONS]
    return h3(b.get("title")) + tbl([""] + [c["label"] for c in b["columns"]], rows, cls="pdg", raw=True)

def b_uses(b):
    lst = (resolve(b["src"]) or [])[: b.get("limit") or 10]
    out = []
    for u in lst:
        exs = u.get("examples") or ([u] if u.get("el") else [])
        out.append(f'<li><strong>{esc(u.get("use") or u.get("meaning") or "")}</strong>' + "".join(f'<br>{gr(x.get("el"))} <span class="en">{esc(x.get("en"))}</span>' for x in exs[: b.get("per") or 2]) + "</li>")
    return h3(b.get("title")) + f'<ul class="uses">{"".join(out)}</ul>'

def b_prep(b):
    preps = resolve("grammar/prepositions.json#sections[section=8.2].prepositions")
    out = ""
    for p in [p for p in preps if p["preposition"].split(" ")[0] in b["only"]]:
        uses = "".join(f'<li><strong>{esc(u.get("meaning"))}</strong>' + "".join(f'<br>{gr(x.get("el"))} <span class="en">{esc(x.get("en"))}</span>' for x in (u.get("examples") or [])[:2]) + "</li>" for u in p["uses"][: b.get("limit") or 8])
        out += f'<h4 lang="el">{esc(p["preposition"])} <span class="ipa">+ {esc(p["case"])}</span></h4><p class="sub">{esc(p.get("gloss"))}{" · " + esc(p["colloquial_form"]) if p.get("colloquial_form") else ""}</p><ul class="uses">{uses}</ul>'
    return out

def b_vocab(b):
    if b.get("words"):
        lst = [LEX[w] for w in b["words"] if w in LEX]
    else:
        rx = re.compile(b["match"])
        lst = [e for e in LEX.values() if rx.search(e["lemma"]) and (not b.get("pos") or e.get("pos") == b["pos"]) and (not b.get("gender") or (e.get("noun") or {}).get("gender") == b["gender"])][: b.get("limit") or 24]
    items = "".join(f'<li>{gr(with_art(e) if b.get("article") else e["lemma"])} <span class="en">{esc(e.get("gloss"))}</span></li>' for e in lst)
    return h3(b.get("title")) + f'<ul class="wordgrid">{items}</ul>'

def b_video(b): return video_html(b)

BLOCKS = {"text": b_text, "callout": b_callout, "culture": b_culture, "reading": b_reading, "dialogue": b_dialogue, "rules": b_rules,
          "examples": b_examples, "table": b_table, "alphabet": b_alphabet, "digraphs": b_digraphs, "article": b_article,
          "noun-paradigm": b_noun_paradigm, "verb-paradigm": b_verb_paradigm, "uses": b_uses, "prep": b_prep, "vocab": b_vocab, "video": b_video}

# ---------- videos (subtitle cues = transcripts) ----------
VIDEOS = J(f"{LESS}/videos.json")["videos"] + J(f"{LESS}/videos-c1.json")["videos"]
def fmt_t(t):
    t = int(float(t or 0)); return f"{t // 60}:{t % 60:02d}"
def video_html(v):
    rows = "".join(f'<tr><td class="who">{fmt_t(c.get("t"))}</td><td class="el" lang="el">{esc(c.get("el"))}</td><td class="en">{esc(c.get("en") or "")}</td></tr>' for c in v.get("cues", []))
    src = v.get("source") or (v.get("embed") or {}).get("src") or ""
    if (v.get("embed") or {}).get("kind") == "youtube" and not v.get("source"):
        src = f"https://www.youtube.com/watch?v={v['embed']['src']}"
    cred = " · ".join(x for x in [v.get("credit"), v.get("license")] if x)
    link = f' · <a href="{esc(src)}">watch</a>' if src.startswith("http") else ""
    return (f'<div class="dialogue video"><div class="eyebrow">Βίντεο · video transcript</div><h4 lang="el">{esc(v.get("title"))}</h4>'
            f'<p class="sub">{esc(v.get("title_en") or "")}{" · " + esc(cred) if cred else ""}{link}</p><table class="dl">{rows}</table>{gloss_box(v.get("gloss"))}</div>')

# ---------- exercises (static items only; generated drills are represented by their tables) ----------
class Exercises:
    def __init__(self):
        self.keys = []   # (lesson title, anchor, [answers])
    def render(self, lesson_title, lid, practice, rng):
        items = []
        for p in practice:
            g = p.get("gen")
            if g in ("mc", "type"):
                for q in p.get("items", []):
                    items.append((g, q.get("prompt"), q.get("big"), q.get("options") if g == "mc" else None, q.get("answer"), q.get("why")))
            elif g == "reading-q":
                for q in p.get("questions", []):
                    items.append(("mc", q.get("prompt"), None, q.get("options"), q.get("answer"), q.get("why")))
        if not items:
            return ""
        lis, ans = [], []
        for i, (g, prompt, big, opts, answer, why) in enumerate(items, 1):
            body = md(prompt or "")
            if big: body += f' <span class="big" lang="el">{md(big)}</span>'
            if opts:
                o = list(opts); rng.shuffle(o)
                letters = "abcdefgh"
                body += '<ol class="opts" type="a">' + "".join(f"<li>{md(x)}</li>" for x in o) + "</ol>"
                k = o.index(answer) if answer in o else -1
                ans.append(f"<b>{i}</b> {letters[k] + ') ' if k >= 0 else ''}{md(answer)}" + (f' <span class="en">{md(why)}</span>' if why else ""))
            else:
                body += '<div class="blank"></div>'
                ans.append(f"<b>{i}</b> {gr(answer) if answer else ''}" + (f' <span class="en">{md(why)}</span>' if why else ""))
            lis.append(f"<li>{body}</li>")
        self.keys.append((lesson_title, lid, ans))
        return f'<div class="exercises"><h4>Exercises</h4><ol class="ex-items">{"".join(lis)}</ol><p class="sub">Answers: <a href="#key-{lid}">answer key</a>.</p></div>'
    def key_html(self):
        out = ""
        for title, lid, ans in self.keys:
            out += f'<div class="keyblock" id="key-{lid}"><h4><a href="#{lid}">{esc(title)}</a></h4><p>{" · ".join(ans)}</p></div>'
        return out

# ---------- course classification ----------
COURSE = J(f"{LESS}/course.json")
LEVEL_RX = re.compile(r"(?:^|-)(a1|a2|b1|b2|c1)(?:-|$)")
def lesson_level(fname, unit_label):
    m = LEVEL_RX.search(fname.replace(".json", ""))
    if m: return m.group(1).upper()
    m = re.match(r"(A1|A2|B1|B2|C1)", unit_label)
    if m: return m.group(1)
    if unit_label.startswith("Colloquial"): return "B2"
    return None

def unit_part(label, fname):
    if fname.startswith("listen-"): return "listen"
    if fname.startswith(("dlg-", "read-", "c1-read-")): return "input"
    if fname.startswith(("exam-", "c1-exam-")): return "exam"
    if fname.startswith(("sit-", "vt-", "theme-", "slang-", "c1-bank-", "c1-idioms", "c1-ancient", "c1-collocations")) or "Phrase bank" in label: return "vocab"
    if fname.startswith("c1-language-question"): return "input"
    return "grammar"

PARTS = OrderedDict([
    ("grammar", ("Grammar and syntax", "Γραμματική και σύνταξη")),
    ("vocab", ("Vocabulary, situations and usage", "Λεξιλόγιο και χρήση")),
    ("input", ("Comprehensible input: dialogues and readings", "Διάλογοι και κείμενα")),
    ("listen", ("Listening transcripts", "Απομαγνητοφωνήσεις")),
    ("exam", ("Exam skills, writing and speaking", "Εξετάσεις, γραπτός και προφορικός λόγος")),
])

LEVEL_INFO = {
    "A1": ("Breakthrough", "Script and sound, nouns and the article, first verbs, first situations and dialogues."),
    "A2": ("Waystage", "Adjectives, pronouns, the genitive, past and future, the subjunctive with να, everyday situations, graded readings and the declension workshop."),
    "B1": ("Threshold", "The verb system in depth (aspect, passive, perfect), complex sentences, vocabulary themes, dialogues, readings and news."),
    "B2": ("Vantage", "The full passive system, formal declensions, word building, complex sentences, exam themes and skills, real listening, colloquial and regional Greek."),
    "C1": ("Effective operational proficiency", "Learned morphology, argument and register, idiom and the living tradition, authentic texts, the Γ1 exam and the phrase bank."),
}

# Greek-only cover text (official names of the Greek certificate levels)
LEVEL_INFO_EL = {
    "A1": ("Στοιχειώδης γνώση", "Γραφή και προφορά, ουσιαστικά και άρθρο, τα πρώτα ρήματα, οι πρώτες καθημερινές περιστάσεις και οι πρώτοι διάλογοι."),
    "A2": ("Βασική γνώση", "Επίθετα, αντωνυμίες, η γενική, παρελθόν και μέλλον, η υποτακτική με το «να», καθημερινές περιστάσεις, διαβαθμισμένα κείμενα και το εργαστήρι της κλίσης."),
    "B1": ("Μέτρια γνώση", "Το ρηματικό σύστημα σε βάθος (ποιόν ενεργείας, παθητική φωνή, συντελεσμένοι χρόνοι), σύνθετες προτάσεις, θεματικό λεξιλόγιο, διάλογοι, κείμενα και ειδήσεις."),
    "B2": ("Καλή γνώση", "Η παθητική φωνή στο σύνολό της, λόγιες κλίσεις, παραγωγή και σύνθεση λέξεων, σύνθετες προτάσεις, θέματα και δεξιότητες των εξετάσεων, αυθεντικά ακούσματα, η καθομιλουμένη και οι τοπικές ποικιλίες."),
    "C1": ("Πολύ καλή γνώση", "Λόγια μορφολογία, επιχειρηματολογία και ύφος, ιδιωματισμοί και η ζωντανή παράδοση, αυθεντικά κείμενα, οι εξετάσεις του Γ1 και η τράπεζα φράσεων."),
}

# ---------- library ----------
def lib_items(shelf):
    ix = J(f"{LIB}/{shelf}/index.json")["items"]
    return [(it, J(f"{LIB}/{shelf}/{it['file']}")) for it in ix]

def story_html(d, kind):
    paras_el = "".join(f'<p lang="el">{md(p.get("el"))}</p>' for p in d.get("paras", []))
    paras_en = "".join(f"<p>{md(p.get('en'))}</p>" for p in d.get("paras", []) if p.get("en"))
    meta = " · ".join(x for x in [d.get("author"), d.get("title")] if x)
    notes = "".join(f"<li>{md(n)}</li>" for n in d.get("notes", []))
    q = d.get("questions", [])
    return (f'<div class="reading"><div class="eyebrow">{kind}</div><h4 lang="el">{esc(d.get("el"))}</h4><p class="sub">{esc(meta)}</p>'
            f'<div class="rd">{paras_el}</div>'
            + (f'<div class="notes"><div class="gl-h">Notes</div><ul>{notes}</ul></div>' if notes else "")
            + (f'<div class="trans"><div class="gl-h">Translation</div>{paras_en}</div>' if paras_en else "")
            + gloss_box(d.get("gloss")) + "</div>"), q

def vocab_list(words):
    lst = [LEX[w] for w in words if w in LEX]
    miss = [w for w in words if w not in LEX]
    items = "".join(f'<li>{gr(with_art(e))} <span class="en">{esc(e.get("gloss"))}</span></li>' for e in lst) + "".join(f"<li>{gr(w)}</li>" for w in miss)
    return f'<div class="words"><h4>Words to learn</h4><ul class="wordgrid">{items}</ul></div>' if items else ""

# ---------- reference appendices ----------
def leaves_grid(d):
    """Render nested {sg:{nom..}} or {m:{nom..}} dicts as a table."""
    if not isinstance(d, dict): return md(d)
    cols = [k for k in d if isinstance(d[k], dict)]
    if not cols: return tbl(None, [[f"<b>{esc(k)}</b>", gr(v) if not isinstance(v, (list, dict)) else esc(json.dumps(v, ensure_ascii=False))] for k, v in d.items()], cls="pdg", raw=True)
    rows_k = []
    for c in cols:
        for k in d[c]:
            if k not in rows_k: rows_k.append(k)
    return tbl([""] + cols, [[f"<b>{esc(k)}</b>"] + [gr(d[c].get(k, "")) if not isinstance(d[c].get(k), (dict, list)) else esc(str(d[c].get(k))) for c in cols] for k in rows_k], cls="pdg", raw=True)

def generic(o, depth=0):
    """A readable rendering of arbitrary grammar JSON (as library.js block())."""
    SKIP = {"pdf_pages", "pdf_page", "source", "section", "id", "related_files", "variety", "src", "cite"}
    if o is None: return ""
    if isinstance(o, str): return f"<p>{md(o)}</p>"
    if isinstance(o, (int, float)): return f"<p>{o}</p>"
    if isinstance(o, list):
        if all(isinstance(x, str) for x in o): return "<ul>" + "".join(f"<li>{md(x)}</li>" for x in o) + "</ul>"
        if all(isinstance(x, dict) and "el" in x for x in o):
            return f'<table class="ex">{"".join(f"<tr><td class=el lang=el>{esc(x.get("el"))}</td><td class=en>{esc(x.get("en") or x.get("note") or "")}</td></tr>" for x in o)}</table>'
        if o and all(isinstance(x, dict) for x in o) and all(not isinstance(v, (dict, list)) for x in o for v in x.values()):
            keys = [k for k in OrderedDict((k, 1) for x in o for k in x) if k not in SKIP]
            return tbl([k.replace("_", " ") for k in keys], [[esc(x.get(k, "")) for k in keys] for x in o], cls="ref", raw=True)
        return "".join(f'<div class="sub-blk">{generic(x, depth + 1)}</div>' for x in o)
    if isinstance(o, dict):
        if o and all(isinstance(v, dict) and all(not isinstance(w, (dict, list)) for w in v.values()) for v in o.values()) and len(o) <= 6:
            return leaves_grid(o)
        if o and all(not isinstance(v, (dict, list)) for v in o.values()) and len(o) <= 8 and all(len(str(v)) < 40 for v in o.values()):
            return leaves_grid(o)
        out = ""
        for k, v in o.items():
            if k in SKIP or v in (None, "", [], {}): continue
            if k in ("rule", "rules", "note", "notes", "examples", "text"):
                out += generic(v, depth + 1)
            else:
                lvl = min(6, 5 + depth)
                out += f'<h{lvl} class="rk">{esc(str(k).replace("_", " "))}</h{lvl}>' + generic(v, depth + 1)
        return out
    return ""

def ref_nouns():
    n = J(f"{DATA}/grammar/nouns-full.json")
    GEN = {"m": "Masculine nouns", "f": "Feminine nouns", "n": "Neuter nouns"}
    out = ""
    for g in "mfn":
        ps = [p for p in n["paradigms"] if p.get("gender") == g]
        out += f"<h3>{GEN[g]}</h3>"
        for i in range(0, len(ps), 3):
            grp = ps[i:i + 3]
            out += noun_paradigm(grp, ["nom", "acc", "gen", "voc"])
            for p in grp:
                if p.get("examples"): out += f'<p class="cloud"><b lang="el">{esc(p["model"])}</b> like: <span lang="el">{esc(" · ".join(p["examples"]))}</span></p>'
    for k, t in [("irregular_neuters", "Irregular neuters"), ("gender_change_in_plural", "Nouns that change gender in the plural"), ("common_gender", "Common gender"), ("indeclinable", "Indeclinable nouns"), ("vocative_notes", "Vocative")]:
        if n.get(k): out += f"<h3>{t}</h3>" + generic(n[k])
    return out

def ref_articles():
    a = J(f"{DATA}/grammar/nouns-full.json")["articles"]
    return ("<h3>Definite article</h3>" + leaves_grid({"m": {**{f"sg {k}": v for k, v in a["definite"]["sg"]["m"].items()}, **{f"pl {k}": v for k, v in a["definite"]["pl"]["m"].items()}},
                                                       "f": {**{f"sg {k}": v for k, v in a["definite"]["sg"]["f"].items()}, **{f"pl {k}": v for k, v in a["definite"]["pl"]["f"].items()}},
                                                       "n": {**{f"sg {k}": v for k, v in a["definite"]["sg"]["n"].items()}, **{f"pl {k}": v for k, v in a["definite"]["pl"]["n"].items()}}})
            + f'<p>{md(a.get("final_n_rule", ""))}</p><h3>Indefinite article</h3>' + leaves_grid({g: a["indefinite"][g] for g in "mfn"}) + generic(a["indefinite"].get("notes"))
            + "<h3>σε + article</h3>" + generic(a.get("se_contraction")))

def ref_adjectives():
    a = J(f"{DATA}/grammar/adjectives.json")
    out = ""
    for p in a["paradigms"]:
        out += f'<h4><span lang="el">{esc(p["model"])}</span> <span class="ipa">{esc(p.get("gloss", ""))}{" · " + esc(p["applies"]) if p.get("applies") else ""}</span></h4>'
        rows = [[f"<b>{c} {num}</b>"] + [gr(p[num][g][c] if isinstance(p[num].get(g), dict) else p[num].get(c, {}).get(g, "")) for g in "mfn"] for num in ("sg", "pl") for c in ("nom", "acc", "gen", "voc") if c in (p[num].get("m") or p[num])]
        try:
            out += tbl(["", "masc.", "fem.", "neut."], rows, cls="pdg", raw=True)
        except Exception:
            out += generic({"sg": p["sg"], "pl": p["pl"]})
        if p.get("examples"): out += f'<p class="cloud">Like this: <span lang="el">{esc(" · ".join(p["examples"]))}</span></p>'
    return out + "<h3>Comparison</h3>" + generic(a.get("comparison")) + "<h3>Indeclinable adjectives</h3>" + generic(a.get("indeclinable"))

def ref_pronouns():
    out = ""
    for f in ["pronouns.json", "pronouns-holton.json"]:
        d = J(f"{DATA}/grammar/{f}")
        for k, v in d.items():
            if isinstance(v, (dict, list)) and k not in ("related_files", "cases_covered"):
                out += f"<h3>{esc(k.replace('_', ' ').capitalize())}</h3>" + generic(v)
    return out

def ref_verbs():
    v = J(f"{DATA}/grammar/verbs-holton.json")
    out = ""
    for s in v["sections"]:
        if not any(k.startswith("paradigm") for k in s): continue
        p = s.get("paradigm") or s.get("paradigm_έχω")
        model = s.get("model_verb") or ("έχω" if s.get("paradigm_έχω") else "είμαι" if s.get("section") == "6.7" else "")
        out += f'<h3><span lang="el">{esc(model)}</span> <span class="ipa">{esc(s.get("title", ""))}</span></h3>' + generic(p)
        extra = {k: s[k] for k in s if k.startswith("verbs") and isinstance(s[k], list)}
        if extra: out += generic(extra)
        if s.get("non_finite_forms"): out += "<h5>Non-finite forms</h5>" + generic(s["non_finite_forms"])
    return out

def ref_irregular():
    vs = J(f"{DATA}/grammar/verbs-holton.json")["irregular_verbs_6.25"]["verbs"]
    cols = [("present", "Present"), ("meaning", "Meaning"), ("active_simple_past", "Simple past"), ("dependent", "Dependent"), ("perfective_imperative", "Imperative"), ("imperfect", "Imperfect"), ("passive_simple_past", "Passive past"), ("passive_dependent", "Passive dep."), ("passive_perfect_participle", "Participle")]
    rows = [[(gr(f"{x['present']} ({x['conjugation_type']})" if k == "present" and x.get("conjugation_type") else x.get(k) or "") if k != "meaning" else esc(x.get(k) or "")) for k, _ in cols] for x in vs]
    pp = J(f"{DATA}/grammar/verbs-past-future.json")["principal_parts"]
    return ("<h3>Irregular verbs (166 most common)</h3>" + tbl([l for _, l in cols], rows, cls="irr", raw=True)
            + "<h3>Principal parts of common verbs</h3>" + tbl(["Present", "Meaning", "Simple past", "Future"], [[gr(x["present"]), esc(x.get("gloss")), gr(x.get("aorist_1sg") or "—"), gr(x.get("future_1sg") or "—")] for x in pp], cls="irr", raw=True))

def ref_file(name, title=None):
    d = J(f"{DATA}/grammar/{name}")
    out = ""
    if isinstance(d, dict) and isinstance(d.get("sections"), list):
        for s in d["sections"]:
            out += f'<h3>{esc(s.get("title", ""))}</h3>' + generic({k: v for k, v in s.items() if k != "title"})
        rest = {k: v for k, v in d.items() if k not in ("sections", "source", "variety", "related_files", "note")}
        out += generic(rest)
    else:
        out = generic({k: v for k, v in d.items() if k not in ("source", "variety", "related_files")} if isinstance(d, dict) else d)
    return out

def ref_glossary():
    d = J(f"{DATA}/grammar/glossary.json")
    return generic(d.get("terms") if isinstance(d, dict) and d.get("terms") else d)

REFS = {
    "A1": [("Articles", ref_articles), ("Personal and other pronouns", ref_pronouns)],
    "A2": [("Noun declension tables", ref_nouns), ("Adjective tables", ref_adjectives), ("Numerals", lambda: ref_file("numerals.json")), ("Prepositions", lambda: ref_file("prepositions.json"))],
    "B1": [("Verb conjugation models", ref_verbs), ("Irregular verbs and principal parts", ref_irregular), ("Conjunctions", lambda: ref_file("conjunctions.json"))],
    "B2": [("Word formation", lambda: ref_file("word-formation.json")), ("Address and politeness", lambda: ref_file("address-politeness.json")), ("Grammar terms", ref_glossary)],
    "C1": [("Appendices: learned and archaic forms", lambda: ref_file("appendices.json"))],
}

# ---------- CSS ----------
CSS = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "textbook.css"), encoding="utf-8").read()

# ---------- book assembly ----------
def build(level):
    _ids.clear()
    rng = random.Random(f"ellinika-{level}")
    ex = Exercises()
    parts = OrderedDict((k, []) for k in PARTS)   # part -> [(unit title, [(lesson html, title, id)])]
    used_videos = set()
    lesson_ids = set()
    lesson_texts = set()
    for u in COURSE["units"]:
        if u.get("daily"): continue
        for l in u["lessons"]:
            if lesson_level(l["file"], u["label"]) != level: continue
            p = f"{LESS}/{l['file']}"
            if not os.path.exists(p): continue
            d = J(p)
            lid = anchor(l["id"]); lesson_ids.add(l["id"])
            body = ""
            for b in d.get("blocks", []):
                fn = BLOCKS.get(b.get("type"))
                if not fn: continue
                try:
                    body += fn(b)
                except Exception as e:
                    print(f"  ! {l['file']} block {b.get('type')}: {e}", file=sys.stderr)
                if b.get("type") == "reading": lesson_texts.add(re.sub(r"\s+", " ", b.get("text", ""))[:60])
            for v in VIDEOS:
                if l["id"] in v.get("lessons", []) and v["id"] not in used_videos and (l["file"].startswith("listen-") or v.get("level") == level):
                    body += video_html(v); used_videos.add(v["id"])
            # paradigm drills from generator specs: show the tables they drill, when not already on the page
            for pr in d.get("practice", []):
                if pr.get("gen") == "decline" and pr.get("ids"):
                    n = J(f"{DATA}/grammar/nouns-full.json")["paradigms"]
                    ps = [x for x in n if x.get("id") in pr["ids"]]
                    if ps and not any(x["model"] in body for x in ps):
                        body += '<div class="drill"><h4>Drill tables</h4>' + "".join(noun_paradigm(ps[i:i + 4], ["nom", "acc", "gen", "voc"]) for i in range(0, len(ps), 4)) + "</div>"
            body += vocab_list(d.get("vocab") or [])
            body += ex.render(d.get("title") or l["title"], lid, d.get("practice", []), rng)
            title_el, title_en = d.get("el") or l.get("el"), d.get("title") or l["title"]
            html_l = f'<section class="lesson" id="{lid}"><h3 class="lt"><span lang="el">{esc(title_el)}</span><span class="lt-en">{esc(title_en)}</span></h3>{body}</section>'
            part = unit_part(u["label"], l["file"])
            unit_title = re.sub(r"^(A1|A2|B1|B2|C1) · ", "", u["label"]) + ": " + u["title"]
            units = parts[part]
            if not units or units[-1][0] != unit_title: units.append((unit_title, []))
            units[-1][1].append((html_l, f"{title_el} · {title_en}", lid))

    # library and corpus additions
    extra = OrderedDict((k, []) for k in PARTS)
    def add(part, unit, html_s, title, lid):
        units = extra[part]
        if not units or units[-1][0] != unit: units.append((unit, []))
        units[-1][1].append((html_s, title, lid))
    for shelf, kind, unit in [("stories", "Διήγημα · graded story", "Graded short stories"), ("news", "Ειδήσεις · news", "News reader"),
                              ("opinion", "Άρθρο γνώμης · opinion", "Opinion articles"), ("classics", "Κλασικό διήγημα · classic story", "Classic Greek stories")]:
        for it, d in lib_items(shelf):
            if it.get("level") != level: continue
            lid = anchor(f"{shelf}-{it['id']}")
            s, qs = story_html(d, kind)
            prac = [{"gen": "reading-q", "questions": [{"prompt": q.get("q") or q.get("prompt"), "options": q.get("options"), "answer": q.get("answer"), "why": q.get("why")} for q in qs]}] if qs else []
            s += vocab_list(d.get("vocab") or [])
            if d.get("writing"): s += f'<div class="callout"><b>Writing task.</b> <span lang="el">{md(d["writing"])}</span></div>'
            s += ex.render(d.get("el"), lid, prac, rng)
            add("input", unit, f'<section class="lesson" id="{lid}">{s}</section>', f"{d.get('el')} · {d.get('title')}", lid)
    if level == "C1":
        for t in J(f"{DATA}/c1/texts/index.json")["texts"]:
            d = J(f"{DATA}/c1/texts/{t['file']}") if os.path.exists(f"{DATA}/c1/texts/{t['file']}") else None
            if not d or not d.get("text"): continue
            txt = d.get("text_monotonic") or d["text"]
            if re.sub(r"\s+", " ", txt)[:60] in lesson_texts: continue
            lid = anchor("text-" + d["id"])
            meta = " · ".join(str(x) for x in [d.get("author"), d.get("date"), d.get("license")] if x)
            s = (f'<div class="reading"><div class="eyebrow">Αυθεντικό κείμενο · authentic text ({esc(d.get("kind"))}, {esc(d.get("register", ""))})</div><h4 lang="el">{esc(d.get("title"))}</h4>'
                 f'<p class="sub">{esc(meta)}{f" · <a href=\"{esc(d.get("url"))}\">source</a>" if d.get("url") else ""}</p><div class="rd" lang="el">{paras(txt)}</div>'
                 + (f'<div class="notes"><div class="gl-h">Notes</div>{generic(d["notes"])}</div>' if d.get("notes") else "") + "</div>")
            add("input", "Authentic C1 texts", f'<section class="lesson" id="{lid}">{s}</section>', d.get("title"), lid)
    # listening library
    import glob
    for f in sorted(glob.glob(f"{LIB}/listening/*.json")):
        for it in J(f)["items"]:
            if it.get("level") != level: continue
            lid = anchor("listening-" + it["id"])
            s = (f'<p class="sub" lang="el">{esc(it.get("context_el") or "")}</p>' + dialogue_html(it.get("title"), f"{it.get('title_en', '')} · {it.get('type', '')}", it.get("script", []), it.get("gloss"), "Ακρόαση · listening transcript"))
            s += vocab_list(it.get("vocab") or [])
            prac = [{"gen": "reading-q", "questions": [{"prompt": q.get("q") or q.get("prompt"), "options": q.get("options"), "answer": q.get("answer"), "why": q.get("why")} for q in it.get("questions", [])]}]
            s += ex.render(it.get("title"), lid, prac, rng)
            add("listen", "Listening practice", f'<section class="lesson" id="{lid}">{s}</section>', f"{it.get('title')} · {it.get('title_en', '')}", lid)
    for v in VIDEOS:
        if v.get("level") == level and v["id"] not in used_videos:
            lid = anchor("video-" + v["id"]); used_videos.add(v["id"])
            add("listen", "Video transcripts", f'<section class="lesson" id="{lid}">{video_html(v)}</section>', v.get("title"), lid)
    # exam, writing, speaking, register, phrases
    if level in ("B2", "C1"):
        files = ["b2-tasks.json", "b2-tasks-2.json", "b2-tasks-3.json", "b2-tasks-4.json"] if level == "B2" else ["c1-tasks.json"]
        for fn in files:
            for t in J(f"{LIB}/exam/{fn}")["tasks"]:
                lid = anchor("exam-" + t["id"])
                txt = t.get("text_el", "")
                s = (f'<div class="reading exam"><div class="eyebrow">Εξέταση · {esc(t.get("paper", ""))}</div><h4 lang="el">{esc(t.get("title"))}</h4>'
                     f'<p class="sub">{esc(t.get("task_type", ""))}</p><p class="instr" lang="el">{esc(t.get("instructions_el", ""))}</p><div class="rd" lang="el">{paras(txt.replace(chr(10), chr(10) + chr(10)) if txt.count(chr(10)) > 3 and chr(10) + chr(10) not in txt else txt)}</div>')
                qs = t.get("questions", [])
                opts_shared = qs and qs[0].get("options") and all(q.get("options") == qs[0]["options"] for q in qs) and len(qs) > 2
                if opts_shared:
                    s += f'<div class="bank"><b>Choose from:</b> <span lang="el">{" · ".join(esc(o) for o in qs[0]["options"])}</span></div>'
                lis = "".join(f'<li><span lang="el">{esc(q.get("prompt"))}</span>' + ("" if opts_shared or not q.get("options") else '<ul class="opts2">' + "".join(f'<li lang="el">{esc(o)}</li>' for o in q["options"]) + "</ul>") + "</li>" for q in qs)
                s += f'<ol class="ex-items">{lis}</ol></div>'
                ex.keys.append((t.get("title"), lid, [f"<b>{i}</b> {gr(q.get('answer'))}" + (f' <span class="en">{esc(q.get("answer_note"))}</span>' if q.get("answer_note") else "") for i, q in enumerate(qs, 1)] + ([f'<span class="en">{esc(t["answer_note"])}</span>'] if t.get("answer_note") else [])))
                s += f'<p class="sub">Answers: <a href="#key-{lid}">answer key</a>.</p>'
                add("exam", "Exam practice tasks" if level == "B2" else "Γ1 practice tasks", f'<section class="lesson" id="{lid}">{s}</section>', t.get("title"), lid)
        ws = J(f"{LIB}/writing/workshop.json")
        want = "B2" if level == "B2" else "Γ1"
        for w in ws["writing"]:
            if w.get("level") != want: continue
            lid = anchor("writing-" + w["id"])
            s = (f'<div class="reading"><div class="eyebrow">Γραπτός λόγος · writing task{" (official sample)" if w.get("official") else ""}</div><h4>{esc(w.get("genre", ""))}</h4>'
                 f'<p class="sub">{esc(w.get("register", ""))}{f" · {w["words"]} words" if w.get("words") else ""}</p><div lang="el">{paras(w.get("prompt_el"))}</div><div class="en">{paras(w.get("prompt_en"))}</div>'
                 + (f'<h5>Plan</h5>{generic(w["plan"])}' if w.get("plan") else "") + (f'<h5>Useful phrases</h5>{generic(w["phrases"])}' if w.get("phrases") else "")
                 + (f'<h5>Model answer</h5><div class="rd" lang="el">{paras(w["model_el"])}</div>' if w.get("model_el") else "")
                 + (f'<div class="trans"><div class="gl-h">Translation</div>{paras(w["model_en"])}</div>' if w.get("model_en") else "")
                 + (f'<h5>Notes</h5>{generic(w["notes"])}' if w.get("notes") else "") + "</div>")
            add("exam", "Writing workshop", f'<section class="lesson" id="{lid}">{s}</section>', w.get("genre"), lid)
        for w in ws["speaking"]:
            if w.get("level") != want: continue
            lid = anchor("speaking-" + w["id"])
            s = (f'<div class="reading"><div class="eyebrow">Προφορικός λόγος · speaking part {w.get("part")}</div><div lang="el">{paras(w.get("prompt_el"))}</div><div class="en">{paras(w.get("prompt_en"))}</div>'
                 + (f'<h5>Roles</h5>{generic(w["roles"])}' if w.get("roles") else "") + (f'<h5>Useful phrases</h5>{generic(w["phrases"])}' if w.get("phrases") else "")
                 + (f'<h5>Model answer</h5><div class="rd" lang="el">{paras(w["model_el"])}</div>' if w.get("model_el") else "")
                 + (f'<div class="trans"><div class="gl-h">Translation</div>{paras(w["model_en"])}</div>' if w.get("model_en") else "") + "</div>")
            add("exam", "Speaking workshop", f'<section class="lesson" id="{lid}">{s}</section>', (w.get("prompt_en") or "").split("\n")[0][:80], lid)
        if level == "B2": rub = ws.get("rubric", [])
        else: rub = []
        if rub:
            add("exam", "Writing workshop", '<section class="lesson"><h4>Self-check rubric</h4><table class="ex">' + "".join(f'<tr><td class="el" lang="el">{esc(r["el"])}</td><td class="en">{esc(r["en"])}</td></tr>' for r in rub) + "</table></section>", "Self-check rubric", anchor("rubric"))
    for r in J(f"{LIB}/register/register.json")["items"]:
        if r.get("level") != level: continue
        lid = anchor("register-" + r["id"])
        s = (f'<div class="reading"><div class="eyebrow">Ύφος · register rewrite ({esc(r.get("from"))} → {"formal" if r.get("from") == "informal" else "informal"})</div><p class="sub">{esc(r.get("situation"))}</p>'
             f'<table class="ex"><tr><td class="el" lang="el">{esc(r.get("el_from"))}</td><td class="el" lang="el">{esc(r.get("el_to"))}</td></tr></table><p class="en">{esc(r.get("en"))}</p>'
             + (f'<h5>What changes</h5>{generic(r["changes"])}' if r.get("changes") else "") + "</div>")
        add("exam", "Register: formal and informal rewrites", f'<section class="lesson" id="{lid}">{s}</section>', r.get("situation", "")[:80], lid)
    if level == "B1":
        ph = J(f"{LIB}/phrases/phrases.json")
        for g in ph["groups"]:
            lid = anchor("phrases-" + g["id"])
            s = f'<h4><span lang="el">{esc(g["el"])}</span> · {esc(g["en"])}</h4><table class="ex">' + "".join(f'<tr><td class="el" lang="el"><b>{esc(i["el"])}</b>{"<br>" + esc(i["ex"]) if i.get("ex") else ""}</td><td class="en">{esc(i["en"])}{" · " + esc(i["reg"]) if i.get("reg") else ""}</td></tr>' for i in g["items"]) + "</table>"
            add("vocab", "Conversation phrasebook", f'<section class="lesson" id="{lid}">{s}</section>', f"{g['el']} · {g['en']}", lid)

    # vocabulary list for the level
    words = [e for e in LEX.values() if e.get("cefr_est") == level]
    words.sort(key=lambda e: (e.get("rank") or e.get("freq_rank") or 10 ** 6))
    rows = []
    for e in words:
        col = (COLLOC.get(e["lemma"]) or {}).get("collocations") or []
        ex_el = (e.get("example") or {}).get("el")
        ex_en = (e.get("example") or {}).get("en")
        extra_bits = []
        if e.get("form_key") and e.get("pos") in ("verb", "noun", "adjective") and "|" in str(e.get("form_key")): extra_bits.append(esc(e["form_key"]))
        if e.get("register") and e.get("register") != "neutral": extra_bits.append(esc(e["register"]))
        rows.append(f'<tr><td class="lemma" lang="el">{esc(with_art(e))}</td><td class="pos">{POS.get(e.get("pos"), esc(e.get("pos") or ""))}</td>'
                    f'<td>{esc(e.get("gloss"))}{"<div class=fk>" + " · ".join(extra_bits) + "</div>" if extra_bits else ""}'
                    + (f'<div class="vx"><span lang="el">{esc(ex_el)}</span> <span class="en">{esc(ex_en)}</span></div>' if ex_el else "")
                    + (f'<div class="vc" lang="el">{" · ".join(esc(c.get("el")) for c in col[:3])}</div>' if col else "") + "</td></tr>")
    vocab_html = (f'<p>The {len(words):,} words that the app’s word lists rate {level}, in frequency order (most common first). Nouns carry their article; '
                  f'each entry has an example sentence and, where the lexicon has them, common collocations.</p><table class="vocab"><tbody>{"".join(rows)}</tbody></table>')

    # ---------- assemble ----------
    name, blurb = LEVEL_INFO[level]
    toc, body = [], []
    chap = 0
    for key, (pt, pel) in PARTS.items():
        units = parts[key] + extra[key]
        if not units: continue
        chap += 1
        pid = anchor(f"part-{key}")
        toc.append(f'<li class="toc-p"><a href="#{pid}">{chap}. {esc(pt)}</a><ol>')
        body.append(f'<section class="part" id="{pid}"><div class="part-h"><div class="pn">Part {chap}</div><h1>{esc(pt)}</h1><div class="pel" lang="el">{esc(pel)}</div></div>')
        for ut, lessons in units:
            uid = anchor("unit-" + ut)
            toc.append(f'<li><a href="#{uid}">{esc(ut)}</a></li>')
            body.append(f'<h2 class="unit" id="{uid}">{esc(ut)}</h2>' + "".join(h for h, _, _ in lessons))
        toc.append("</ol></li>")
        body.append("</section>")
        if key == "vocab":
            chap += 1
            toc.append(f'<li class="toc-p"><a href="#wordlist">{chap}. Word list for {level}</a></li>')
            body.append(f'<section class="part" id="wordlist"><div class="part-h"><div class="pn">Part {chap}</div><h1>Word list for {level}</h1><div class="pel" lang="el">Λεξιλόγιο {level}</div></div>{vocab_html}</section>')
    if REFS.get(level):
        chap += 1
        toc.append(f'<li class="toc-p"><a href="#reference">{chap}. Reference tables</a><ol>')
        body.append(f'<section class="part" id="reference"><div class="part-h"><div class="pn">Part {chap}</div><h1>Reference tables</h1><div class="pel" lang="el">Πίνακες γραμματικής</div></div>')
        for t, fn in REFS[level]:
            rid = anchor("ref-" + t)
            toc.append(f'<li><a href="#{rid}">{esc(t)}</a></li>')
            try:
                body.append(f'<h2 class="unit" id="{rid}">{esc(t)}</h2><div class="refx">{fn()}</div>')
            except Exception as e:
                print(f"  ! ref {t}: {e}", file=sys.stderr)
        toc.append("</ol></li>"); body.append("</section>")
    chap += 1
    toc.append(f'<li class="toc-p"><a href="#answers">{chap}. Answer key</a></li>')
    body.append(f'<section class="part" id="answers"><div class="part-h"><div class="pn">Part {chap}</div><h1>Answer key</h1><div class="pel" lang="el">Λύσεις</div></div><div class="key">{ex.key_html()}</div></section>')
    credits = ("<section class='part' id='credits'><h2 class='unit'>Sources and credits</h2>"
               "<p>Built from the lessons, readings and data of the Ελληνικά app, for personal, non-commercial study.</p><ul>"
               "<li>Grammar data: D. Holton, P. Mackridge, I. Philippaki-Warburton, V. Spyropoulos, <em>Greek: An Essential Grammar</em> (Routledge), used for personal study only.</li>"
               "<li>Grammar notes: Ε. Πουλοπούλου (Poulopoulou), <em>Modern Greek: Grammar Notes for Absolute Beginners</em>, CC BY-NC-SA. Material derived from it is shared under the same licence, non-commercially.</li>"
               "<li>Exam sample tasks: © Κέντρο Ελληνικής Γλώσσας (Centre for the Greek Language), greek-language.gr, reproduced for private exam preparation.</li>"
               "<li>Authentic texts: Greek Wikipedia contributors (CC BY-SA 4.0), Greek Wikisource (public domain), EUR-Lex, and the press excerpts credited beside each text.</li>"
               "<li>Video transcripts: the creators and licences named beside each video.</li>"
               "<li>Word frequency: OpenSubtitles 2018 frequency list and the app’s annotated lexicon.</li></ul></section>")
    name_el, blurb_el = LEVEL_INFO_EL[level]
    cover = (f'<section class="cover" lang="el"><div class="c-top">Ελληνικά · Συνοδευτικό εγχειρίδιο</div><div class="c-lvl">{el_level(level)}</div><div class="c-name">{name_el}</div>'
             f'<p class="c-blurb">{esc(blurb_el)}</p><div class="c-foot">Τόμος {LEVELS.index(level) + 1} από 5 · Έκδοση {el_date()}</div></section>')
    toc_html = f'<section class="toc"><h1>Contents</h1><ol class="toc-l">{"".join(toc)}<li class="toc-p"><a href="#credits">Sources and credits</a></li></ol></section>'
    doc = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Ελληνικά {level} · Companion textbook</title><style>{CSS}</style></head>'
           f'<body>{cover}{toc_html}{"".join(body)}{credits}</body></html>')
    os.makedirs(OUT, exist_ok=True)
    with open(f"{OUT}/{level}.html", "w", encoding="utf-8") as f:
        f.write(doc)
    n_less = sum(len(ls) for k in parts for _, ls in parts[k] + extra[k])
    print(f"{level}: {n_less} sections, {len(words)} words, {sum(len(a) for _, _, a in ex.keys)} answers, {len(doc) // 1024} KB html")

if __name__ == "__main__":
    lv = [a for a in sys.argv[1:] if a in LEVELS] or LEVELS
    for L in lv:
        build(L)
