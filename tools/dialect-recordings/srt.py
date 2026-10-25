import re,sys,json
def parse(path):
  t=open(path).read()
  # split into cue blocks: number line, time line, then text lines in two columns
  lines=t.split('\n'); cues=[]; cur=None
  for ln in lines:
    if 'VLACH Transcriptions' in ln or re.match(r'^\s*\d+\s*$',ln.strip()) and False: continue
    m=re.match(r'\s*(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)',ln)
    if m:
      cur={'t':m.group(1),'d':m.group(2),'L':[],'R':[]}; cues.append(cur); continue
    if cur is None: continue
    if re.match(r'^\s*\d+(\s+\d+)?\s*$',ln): continue
    if not ln.strip(): continue
    # split column at the position where the right column starts (2+ spaces gap)
    parts=re.split(r'\s{3,}',ln.strip(),maxsplit=1)
    lead=len(ln)-len(ln.lstrip())
    if lead>30: cur['R'].append(ln.strip())
    elif len(parts)==2: cur['L'].append(parts[0]); cur['R'].append(parts[1])
    else: cur['L'].append(parts[0])
  def s(x):
    h,m,r=x.split(':'); sec,ms=r.split(','); return round(int(h)*3600+int(m)*60+int(sec)+int(ms)/1000,2)
  return [{'t':s(c['t']),'d':s(c['d']),'tr':' '.join(c['L']),'en':' '.join(c['R'])} for c in cues]
if __name__=='__main__':
  for c in parse(sys.argv[1]): print(f"{c['t']}\t{c['d']}\t{c['tr']}\t|| {c['en']}")
