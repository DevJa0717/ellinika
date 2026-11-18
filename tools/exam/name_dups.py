# Find Γ1 texts that share a proper name near their start (catches same-topic repeats whose titles differ,
# e.g. "Ο αστρονόμος που έβαλε τον Ήλιο στο κέντρο" vs "Ο Αρίσταρχος ..."). Prints groups of 2-3 texts of the
# same task type; read them and replace real repeats. Usage: python3 tools/exam/name_dups.py [min_set]
import json, glob, re, sys, collections, os
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
min_set = int(sys.argv[1]) if len(sys.argv) > 1 else 0
d = collections.defaultdict(list)
for f in sorted(glob.glob(os.path.join(root, 'library/exam/c1-tasks*.json'))):
    for t in json.load(open(f, encoding='utf-8'))['tasks']:
        if re.search(r'reading-[13]$|use-[13]$', t['id']):
            first = re.findall(r'\b[Α-ΩΆΈΉΊΌΎΏ][α-ωάέήίόύώϊϋΐΰς]{4,}', t.get('text_el', '')[:250])[:3]
            for n in set(first): d[n[:6]].append((t['id'], t['title'][:50]))
for k, v in sorted(d.items()):
    kinds = {x[0].rsplit('-', 2)[-2] + x[0].rsplit('-', 1)[-1] for x in v}
    nums = [int(re.search(r'c1-p(\d+)', x[0]).group(1)) for x in v if re.search(r'c1-p(\d+)', x[0])]
    if 1 < len(v) < 4 and len(kinds) == 1 and nums and max(nums) >= min_set: print(k, v)
