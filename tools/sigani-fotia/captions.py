import json, numpy as np
from PIL import Image, ImageDraw, ImageFont
F='fonts/FiraSansCondensed-600i.ttf'
boxes={int(k):v for k,v in json.load(open('boxes.json')).items()}
boxes[2]=[[24,24,293,61]]; boxes[6]=[[24,25,244,60]]+boxes[6]
boxes[7]=boxes[7]+[[153,449,470,481]]; boxes[9]=[[24,17,260,53]]+boxes[9]; boxes[13]=[[24,25,276,61]]+boxes[13]
Q1='«Η βεβαιότητα, απλή κι απέραντη, πως είναι εκεί που πρέπει.»'
T={i:[] for i in range(16,22)}
T.update({0:['Μαζί.'],
 1:['Η αργοπορημένη μας συνάντηση.',Q1],
 2:['Συνάντηση στην Τοσκάνη.'],
 3:['Η σφραγίδα του κελαριού.','«Το πρώτο φιλί, ανάμεσα στη μυρωδιά του μούστου και στη δροσερή σκιά του κελαριού.»'],
 4:['Πρώτα βήματα στη Μπολόνια.','«Η πρώτη φορά που ο Μάρκο φέρνει τον Νταβίντε κάτω από τις στοές της Μπολόνιας, ανάμεσα σε γέλια κι αμηχανία.»'],
 5:['Βροχή στην ταράτσα.','«Ένα κλεμμένο φιλί στη βροχή, πάνω από τις στέγες της Μπολόνιας.»'],
 6:['Η επίσκεψη στη Μπολόνια.','Επίσκεψη-έκπληξη στη Μπολόνια.'],
 7:['Κουζίνα κι εξομολογήσεις.','Οι ιστορίες ανακατεύονται με το κρασί.'],
 8:['Μπάνιο στο φεγγαρόφωτο.'],
 9:['Η αμοιβαία φροντίδα.','«Όταν η αμοιβαία φροντίδα γίνεται πιο ερωτική από τον φλογερό πόθο.»'],
 10:['Στη βροχή της Φλωρεντίας.','Ούτε βιασύνη, ούτε μετάνιωμα.'],
 11:['Το δώρο του χρόνου.','«Ένα ήσυχο απόγευμα στο αμπέλι του Νταβίντε, για να μάθουν το λεξιλόγιο της τρυφερότητας.»'],
 12:['Το ήσυχο πρωινό.','«Δεν ήταν πια ο φλογερός πόθος, μα η βεβαιότητα πως ήταν εκεί.»'],
 13:['Πρωινή αγκαλιά.','«Ένα γλυκό φιλί ξυπνήματος, πριν ανέβει για τα καλά το φως.»'],
 14:['Ο αμπελώνας την αυγή.','Το μέλλον, σε σιγανή φωτιά.'],
 15:['Η αργοπορημένη μας συνάντηση.',Q1]})
# badge D positions (x0,y0,x1,y1) of the letter, and M reference height
BADGE={0:[((445,416,467,440),'Δ')],14:[((445,416,467,440),'Δ')],1:[((385,515,405,534),'Δ')],15:[((452,427,471,446),'Δ')],
       21:[((375,690,391,708),'Δ'),((401,690,417,708),'Σ')]}
def wrap(d,text,font,maxw):
    words=text.split(); lines=[]; cur=''
    for w in words:
        t=(cur+' '+w).strip()
        if d.textlength(t,font=font)<=maxw or not cur: cur=t
        else: lines.append(cur); cur=w
    lines.append(cur); return lines
for i in range(22):
    im=Image.open(f'img/{i:02d}.jpeg').convert('RGB'); a=np.asarray(im)
    d=ImageDraw.Draw(im); W,H=im.size
    for (x0,y0,x1,y1),text in zip(sorted(boxes.get(i,[]),key=lambda b:b[1]),T[i]):
        fill=tuple(int(v) for v in np.median(a[y0+3:y1-3,x0+3:x1-3].reshape(-1,3),axis=0))
        top = y0 < H/2; h=y1-y0; w=x1-x0
        if top:
            size=min(23,int(h*0.62))
            while True:
                f=ImageFont.truetype(F,size); tw=d.textlength(text,font=f)
                need=tw+18
                if need<=W-15-x0 or size<=15: break
                size-=1
            nx1=max(x1,int(x0+need)); nx1=min(nx1,W-12)
            ny1=y1
            d.rectangle([x0-3,y0-3,max(x1,nx1)+3,ny1+3],fill=(0,0,0))
            d.rectangle([x0,y0,nx1,ny1],fill=fill)
            # erase leftover original if new box narrower
            if nx1<x1: pass
            asc,desc=f.getmetrics()
            d.text((x0+9,(y0+y1)/2),text,font=f,fill=(20,16,14),anchor='lm')
        else:
            best=None
            for size in range(20,11,-1):
                f=ImageFont.truetype(F,size)
                lines=wrap(d,text,f,w-20); lh=int(size*1.12)
                if len(lines)*lh+8<=h or (size<=12):
                    best=(f,lines,lh); break
            if best is None: best=(f,lines,lh)
            f,lines,lh=best
            th=len(lines)*lh
            ny0=min(y0, y1-th-10)
            d.rectangle([x0-3,ny0-3,x1+3,y1+3],fill=(0,0,0))
            d.rectangle([x0,ny0,x1,y1],fill=fill)
            cy=(ny0+y1)/2-th/2+lh/2
            for k,l in enumerate(lines):
                d.text(((x0+x1)/2,cy+k*lh),l,font=f,fill=(20,16,14),anchor='mm')
    for (x0,y0,x1,y1),letter in BADGE.get(i,[]):
        ring=np.concatenate([a[y0-2:y1+2,x0-4:x0-1].reshape(-1,3),a[y0-2:y1+2,x1+1:x1+4].reshape(-1,3)])
        col=tuple(int(v) for v in np.median(ring,axis=0))
        ink=tuple(int(v) for v in np.percentile(a[y0:y1,x0:x1].reshape(-1,3),3,axis=0))
        d.rectangle([x0,y0,x1,y1],fill=col)
        f=ImageFont.truetype('fonts/Literata-600.ttf',int((y1-y0)*1.05))
        d.text(((x0+x1)/2,(y0+y1)/2+1),letter,font=f,fill=ink,anchor='mm')
    im.save(f'imgel/{i:02d}.jpg',quality=88)
