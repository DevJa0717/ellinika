import re,sys,glob,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for f in sorted(glob.glob('*.txt')):
    for i,l in enumerate(open(f).read().split('\n'),1):
        if l.startswith('? '): continue
        if re.search(r'[^\s(«"]\?(?![»"])\s', l+' ') and not re.search(r';', l) and re.search(r'\w\?( |$|\)|,)', l):
            print(f,i,l[:140])
