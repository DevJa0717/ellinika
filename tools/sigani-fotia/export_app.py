#!/usr/bin/env python3
"""Export Σιγανή φωτιά for the app reader (sigani.js): library/sigani/book.json + img/sigani/.
Usage: python3 tools/sigani-fotia/export_app.py  (from the repo root). Prints words the lookup may not know."""
import json, os, re, sys, unicodedata, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import content as C, extras as X

def strip(s):
    s = unicodedata.normalize('NFD', s.lower()); s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('ς', 'σ')
TAGS = re.compile(r'<[^>]+>')
def clean(h): return TAGS.sub('', h).replace('&amp;', '&')

lex = json.load(open(os.path.join(ROOT, 'data/lexicon/core-1000.json'))) + json.load(open(os.path.join(ROOT, 'data/lexicon/core-3000.json')))
lemmas = {}
for e in lex:
    for alt in re.split(r'\s*[/,]\s*', e.get('lemma') or ''):
        if alt: lemmas.setdefault(strip(alt), alt)
forms = json.load(open(os.path.join(ROOT, 'data/lexicon/forms-index.json')))['forms']
known = set(lemmas) | {strip(f) for f in forms}

GLOSS = {
 "Μάρκο": "Μάρκο — Marco (Italian name, not declined)", "Νταβίντε": "Νταβίντε — Davide (Italian name, not declined)",
 "Στέφανο": "Στέφανο — Stefano (Italian name, not declined)", "Μπολόνια": "Μπολόνια — Bologna", "Μπολόνιας": "Μπολόνια — of Bologna",
 "Τοσκάνη": "Τοσκάνη — Tuscany", "Τοσκάνης": "Τοσκάνη — of Tuscany", "Φλωρεντία": "Φλωρεντία — Florence", "Φλωρεντίας": "Φλωρεντία — of Florence",
 "Άρνου": "Άρνος — the Arno (river in Florence)", "Πόντε": "Πόντε Βέκιο — the Ponte Vecchio (old bridge in Florence)",
 "Βέκιο": "Πόντε Βέκιο — the Ponte Vecchio (old bridge in Florence)", "Αιμιλία": "Αιμιλία — Emilia (region of Bologna)",
 "αρκούδο": "αρκούδος — he-bear; a big hairy man", "αρκούδος": "αρκούδος — he-bear; a big hairy man",
 "καταρρακτωδώς": "καταρρακτωδώς — in torrents", "σιγόβραζε": "σιγοβράζω — to simmer", "σιγοβράζω": "σιγοβράζω — to simmer",
 "ανεβοκατέβαινε": "ανεβοκατεβαίνω — to rise and fall", "σφιχταγκαλιασμένοι": "σφιχταγκαλιασμένος — holding each other tight",
 "ασυγχρόνιστες": "ασυγχρόνιστος — out of sync", "φρεσκοπλυμένο": "φρεσκοπλυμένος — freshly washed",
 "χτίζανε": "χτίζω — to build (popular imperfect form)", "πιτσιλίστηκαν": "πιτσιλίζομαι — to splash each other",
 "κληματόβεργες": "κληματόβεργα — vine shoot", "κληματόβεργα": "κληματόβεργα — vine shoot", "βαρελάς": "βαρελάς — cooper, barrel maker",
 "παγοκύστη": "παγοκύστη — ice pack", "τελάρα": "τελάρο — crate", "τσαμπιά": "τσαμπί — bunch of grapes",
 "ζηλιάρικο": "ζηλιάρικος — jealous", "σουβλιά": "σουβλιά — sharp pang", "ολόχρυσο": "ολόχρυσος — all golden",
 "αναστηλωμένο": "αναστηλωμένος — restored", "αναστηλωθεί": "αναστηλώνομαι — to be restored", "αναστήλωση": "αναστήλωση — restoration",
 "αγροτόσπιτου": "αγροτόσπιτο — farmhouse", "αγροτόσπιτο": "αγροτόσπιτο — farmhouse", "ατελιέ": "ατελιέ — studio",
 "ξανακοιμήθηκε": "ξανακοιμάμαι — to fall asleep again", "ξαναέστηνε": "ξαναστήνω — to put back up", "ξαναστήσει": "ξαναστήνω — to put back up",
 "ξανάφτιαχνε": "ξαναφτιάχνω — to redo, rebuild", "ξαναπάρει": "ξαναπαίρνω — to take again",
 "κουλουριάστηκε": "κουλουριάζομαι — to curl up", "αγαπιούνταν": "αγαπιέμαι — to love each other (imperfect)",
 "ακατάληπτο": "ακατάληπτος — unintelligible", "ασυγκράτητα": "ασυγκράτητα — uncontrollably", "βαβούρα": "βαβούρα — hubbub, din",
 "βρεγμένους": "βρεγμένος — wet", "ενδόμυχη": "ενδόμυχος — inmost, intimate", "λοξά": "λοξά — at a slant, diagonally",
 "μυρωδάτα": "μυρωδάτος — fragrant", "νανούριζε": "νανουρίζω — to lull, rock", "ξέχειλο": "ξέχειλος — brimming",
 "ξεφορτώνοντας": "ξεφορτώνω — to unload", "σάλεψε": "σαλεύω — to stir", "σκέπαστρο": "σκέπαστρο — shelter, cover",
 "σχεδιαστήριο": "σχεδιαστήριο — drawing board", "φλογερό": "φλογερός — burning, fiery", "φλογερός": "φλογερός — burning, fiery",
}

def items():
    out = []
    def mk(key, s, part):
        en = X.EN[key]; assert len(en) == len(s['prose']), (key, len(en), len(s['prose']))
        vocab = []
        for g, _ in s['lex']:
            for piece in re.split(r',\s*', g):
                w = re.sub(r'^(ο|η|το|οι|τα|τις|τους)\s+', '', piece.strip())
                if ' ' not in w and strip(w) in lemmas and lemmas[strip(w)] not in vocab: vocab.append(lemmas[strip(w)])
        return dict(id=key, part=part, eyebrow=s['eyebrow'], el=clean(s['title']), level=C.LEVELS[s['level']], pre=s.get('pre'),
                    images=[dict(file='img/sigani/' + f, alt=a) for f, a in s['imgs']],
                    paras=[dict(el=p, en=e) for p, e in zip(s['prose'], en)],
                    lex=[dict(el=g, en=e) for g, e in s['lex']], grammar=s['gram'], vocab=vocab,
                    questions=[dict(q=q, options=o, answer=a, why=w) for q, o, a, w in X.Q[key]])
    out.append(mk('lead', C.LEAD, 'one'))
    for i, s in enumerate(C.STORIES, 1): out.append(mk(f's{i:02d}', s, 'one'))
    for i, s in enumerate(C.STORIES2, 13): out.append(mk(f's{i:02d}', s, 'two'))
    return out

book = dict(
    el=C.TITLE, title="Slow fire: illustrated love stories of Marco and Davide, and later Stefano (B2–C1)",
    tagline=C.TAGLINE, cover='img/sigani/00.jpg', front=C.FRONT,
    parts=[dict(id='one', el='Πρώτο μέρος · Μάρκο και Νταβίντε', en='Part one · Marco and Davide', closing=dict(file='img/sigani/' + C.CLOSING[0], alt=C.CLOSING[1], caption=C.CLOSING[2])),
           dict(id='two', el='Δεύτερο μέρος · Τρεις', en='Part two · Three', intro=[dict(el=p, en=e) for p, e in zip(C.PART2, X.EN['part2'])],
                closing=dict(file='img/sigani/' + C.CLOSING2[0], alt=C.CLOSING2[1], caption=C.CLOSING2[2]))],
    items=items(), reflect=[C.REFLECT, C.REFLECT2],
    appendix=dict(el=C.APPENDIX_TITLE, sub=C.APPENDIX_SUB, groups=[dict(el=h, rows=[dict(el=g, en=e) for g, e in rows]) for h, rows in C.APPENDIX]),
    gloss=GLOSS, pdf='downloads/textbook/Ellinika-Sigani-fotia.pdf')

os.makedirs(os.path.join(ROOT, 'library/sigani'), exist_ok=True)
json.dump(book, open(os.path.join(ROOT, 'library/sigani/book.json'), 'w'), ensure_ascii=False, indent=1)
os.makedirs(os.path.join(ROOT, 'img/sigani'), exist_ok=True)
for f in os.listdir(os.path.join(HERE, 'img')): shutil.copy(os.path.join(HERE, 'img', f), os.path.join(ROOT, 'img/sigani', f))
# coverage report
miss = {}
texts = [p['el'] for it in book['items'] for p in it['paras']] + [p['el'] for p in book['parts'][1]['intro']]
for t in texts:
    for w in re.findall(r'[Ͱ-Ͽἀ-῿]+', clean(t)):
        k = strip(w)
        if k not in known and k not in {strip(g) for g in GLOSS}: miss[w] = miss.get(w, 0) + 1
print(len(book['items']), 'items;', sum(len(i['vocab']) for i in book['items']), 'vocab lemmas;', len(miss), 'forms not in the forms index:')
print(' '.join(sorted(miss)))
