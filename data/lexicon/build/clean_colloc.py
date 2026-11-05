#!/usr/bin/env python3
"""Remove invented items from collocations.json. Candidates come from words neither the el_GR hunspell list nor the
forms index knows (most are real diminutives, slang and loans); the ones judged invented are listed in DROP.
Usage: python3 clean_colloc.py [--write]"""
import json, os, re, sys
B = os.path.dirname(os.path.abspath(__file__)); L = os.path.dirname(B)
DROP = set('μετακινήσιμος επιπεδότητα ανέγγραφος απορρητοποίηση ανθρωπογένεια οργανισμικός αρχιδεσμοφύλακας κορμικός '
           'ανελκυστικός καταλογογράφηση βρύχιος πειρασμικός οικοδεσποτικός ροϊκός ψιλόλιγνος εμφυλιοπολεμικός εφικτότητα '
           'σεμιναριακός λωρίδιο ρηγματώνω ρηγμάτωση απορρησία υπολήψιμος αμφοτερόπλευρη καταμαχώ τρακάρισα ξυνός υποκοσμικός ρηματοποιώ σύμπλεξη '
           'αποδοκιμή ανορθολογιστής ασπροπροσωπία κακοτεχνίτης κουτσομιλάω κοσμοπλημμυρισμένος παλιοκαιρός παραήπια πιτουρένιος πληθυσμιολογία πρόβαση ρηχαίνω σκέπαστος σουλουπωτή συνδυαστός ψυχοδραστικότητα μισόκαρδος '
           'σκευωρός τριχικός χειραγωγήσιμος φαρμακοδιέγερση υπερεντείνω ναυάγηση διοπτρία θανάτωμα σαββατοκύριακη τρίψη πλεούμενος'.split())
C = json.load(open(f'{L}/collocations.json')); n = 0
def bad(s): return any(w in DROP for w in re.findall(r'[Ͱ-Ͽ]+', s))
for l, e in C['entries'].items():
    for k in ('synonyms', 'antonyms', 'family'):
        keep = [x for x in e.get(k, []) if not bad(x)]; n += len(e.get(k, [])) - len(keep); e[k] = keep
    keep = [c for c in e['collocations'] if not bad(c['el'])]; n += len(e['collocations']) - len(keep)
    e['collocations'] = keep or e['collocations']
print('removed', n)
if '--write' in sys.argv: json.dump(C, open(f'{L}/collocations.json', 'w'), ensure_ascii=False, separators=(',', ':'))
