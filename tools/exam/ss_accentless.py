# Accent-insensitive search over library/exam and library/listening: python3 tools/exam/ss_accentless.py word1 word2 ... (run from the repo root)
import sys,glob,json,unicodedata
def n(s): return ''.join(c for c in unicodedata.normalize('NFD',s.lower()) if unicodedata.category(c)!='Mn')
keys=[n(k) for k in sys.argv[1:]]
cnt={k:0 for k in keys}; ex={k:'' for k in keys}
for f in glob.glob('library/exam/*.json')+glob.glob('library/listening/*.json'):
    s=n(open(f).read())
    for k in keys:
        c=s.count(k)
        if c:
            cnt[k]+=c
            if not ex[k]:
                i=s.find(k); ex[k]=f.split('/')[-1]+': '+s[max(0,i-40):i+40].replace('\n',' ')
for k in keys: print(k,cnt[k],ex[k])
