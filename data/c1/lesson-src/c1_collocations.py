import json, sys, random
random.seed(5)
V = [ # verb, noun, meaning, everyday
 ("λαμβάνω","μέτρα","take measures","παίρνω μέτρα"),
 ("λαμβάνω","υπόψη","take into account","σκέφτομαι"),
 ("ασκώ","κριτική","criticise","κατακρίνω"),
 ("ασκώ","πίεση","exert pressure","πιέζω"),
 ("θέτω","ζήτημα / ερώτημα","raise an issue / question","ρωτάω"),
 ("θέτω","σε κίνδυνο","put at risk","βάζω σε κίνδυνο"),
 ("θέτω","σε εφαρμογή","put into effect","εφαρμόζω"),
 ("διεξάγω","έρευνα","conduct research","κάνω έρευνα"),
 ("καταβάλλω","προσπάθεια","make an effort","προσπαθώ"),
 ("καταβάλλω","ποσό","pay a sum","πληρώνω"),
 ("παίζω","καθοριστικό ρόλο","play a decisive role","μετράω πολύ"),
 ("δίνω","έμφαση σε","place emphasis on","τονίζω"),
 ("έρχομαι","σε επαφή με","come into contact with","μιλάω με"),
 ("έρχομαι","σε σύγκρουση με","come into conflict with","τσακώνομαι"),
 ("φέρω","ευθύνη","bear responsibility","φταίω"),
 ("αναλαμβάνω","την ευθύνη","take responsibility","—"),
 ("προβαίνω","σε δηλώσεις","make statements","δηλώνω"),
 ("εκφράζω","επιφυλάξεις","express reservations","έχω αμφιβολίες"),
 ("διατυπώνω","άποψη / πρόταση","formulate a view / proposal","λέω τη γνώμη μου"),
 ("αντλώ","συμπεράσματα","draw conclusions","βγάζω συμπεράσματα"),
 ("επιφέρει","αλλαγές","brings about changes","φέρνει αλλαγές"),
 ("εγείρει","ερωτήματα","raises questions","βγάζει ερωτήματα"),
 ("προκαλώ","αντιδράσεις","provoke reactions","—"),
 ("τυγχάνω","αποδοχής (+gen.)","meet with acceptance","γίνομαι αποδεκτός"),
 ("χαίρω","εκτίμησης (+gen.)","enjoy esteem","με εκτιμούν"),
 ("καλύπτω","ανάγκες","meet needs","—"),
 ("αποτελώ","αντικείμενο συζήτησης","be the subject of discussion","συζητιέται"),
 ("κάνω","λόγο για","speak of, mention","μιλάω για"),
 ("δίνω","το πράσινο φως","give the green light","εγκρίνω"),
 ("βάζω","τέλος σε","put an end to","σταματάω"),
]
A = [("ευρεία απήχηση","wide appeal"),("οξεία κριτική","sharp criticism"),("έντονη ανησυχία","serious concern"),("ραγδαία ανάπτυξη","rapid growth"),
 ("καίριο ζήτημα","crucial issue"),("ουσιαστική αλλαγή","substantive change"),("θεμελιώδες δικαίωμα","fundamental right"),("εύλογη απορία","reasonable question"),
 ("ευρύτερο πλαίσιο","wider context"),("κρίσιμη καμπή","critical turning point"),("βαθιά τομή","deep reform (lit. cut)"),("πρόσφορο έδαφος","fertile ground"),
 ("αδιέξοδη κατάσταση","deadlock"),("ευαίσθητο θέμα","sensitive issue"),("σημαντική πρόοδος","significant progress"),("ισχυρό επιχείρημα","strong argument")]
nouns=[n for _,n,_,_ in V]
mc=[]
for v,n,m,e in V:
    BAN={'σε κίνδυνο':['βάζω'],'ζήτημα / ερώτημα':['εγείρει','διατυπώνω'],'ερωτήματα':['θέτω','προκαλώ'],'αλλαγές':['προκαλώ','φέρω','βάζω'],'αντιδράσεις':['επιφέρει','εγείρει'],'τέλος σε':['θέτω'],'σε εφαρμογή':['βάζω'],'έμφαση σε':['θέτω'],'ευθύνη':['αναλαμβάνω'],'την ευθύνη':['φέρω'],'σε δηλώσεις':['προχωρώ'],'το πράσινο φως':[],'άποψη / πρόταση':['εκφράζω','θέτω'],'επιφυλάξεις':['διατυπώνω','θέτω'],'μέτρα':['παίρνω']}
    others=sorted(x for x in set(v2 for v2,_,_,_ in V) if x!=v and x not in BAN.get(n,[]))
    mc.append({"prompt":f"___ {n} ({m})","answer":v,"options":[v]+random.sample(others,3),"why":f"{v} {n}"+(f"; everyday: {e}" if e!="—" else "")})
L = {
 "el":"Λόγιες συνάψεις",
 "title":"Formal collocations: λαμβάνω μέτρα, ασκώ κριτική, καταβάλλω προσπάθεια",
 "section":"C1 · argument and register",
 "goal":"Use the fixed verb + noun and adjective + noun pairs that make formal Greek sound native rather than translated.",
 "blocks":[
  {"type":"text","text":"Much of what separates C1 from B2 writing is **collocation**: knowing that Greeks *ασκούν* κριτική (not *κάνουν*), *καταβάλλουν* προσπάθεια, *διεξάγουν* έρευνα, and that criticism is *οξεία* and growth *ραγδαία*. The verb is often a learned one whose basic meaning has faded (*ασκώ* 'exercise', *φέρω* 'carry', *τυγχάνω* 'happen to get'); the pair is what carries the meaning. Learn them as units."},
  {"type":"table","title":"Verb + noun","head":["Collocation","Meaning","Everyday equivalent"],"rows":[[f"**{v} {n}**",m,e] for v,n,m,e in V]},
  {"type":"table","title":"Adjective + noun","head":["Collocation","Meaning"],"rows":[[f"**{a}**",b] for a,b in A]},
  {"type":"callout","text":"**Genitive objects:** a few learned verbs take a genitive, a real C1 signal: **τυγχάνω** αποδοχής / προσοχής / θετικής υποδοχής 'meet with acceptance/attention/a warm welcome'; **χαίρω** εκτίμησης / σεβασμού 'enjoy esteem/respect'; **χρήζω** διερεύνησης 'require investigation'. Their everyday equivalents take the accusative or are passive.\n\n**καταβάλλω vs καταβάλλομαι:** *καταβάλλω προσπάθεια* 'make an effort', but *είμαι καταβεβλημένος* 'I'm exhausted'."},
  {"type":"culture","title":"Η γλώσσα των δελτίων τύπου","text":"Press releases are built almost entirely from these pairs: *Η κυβέρνηση έλαβε μέτρα… Ο υπουργός εξέφρασε επιφυλάξεις… Η πρόταση έτυχε ευρείας αποδοχής…* Reading two or three ministry announcements a week (they're short and public) is the fastest way to absorb them."},
  {"type":"reading","title":"Δελτίο τύπου","text":"Η Περιφέρεια ανακοινώνει ότι, κατόπιν της έντονης ανησυχίας που **εξέφρασαν** οι κάτοικοι, **έλαβε** σειρά **μέτρων** για την προστασία του υδροφόρου ορίζοντα. Το ζήτημα **ετέθη** για πρώτη φορά πριν από δύο χρόνια, όταν πανεπιστημιακή ομάδα **διεξήγαγε έρευνα** και **άντλησε συμπεράσματα** που **εγείρουν σοβαρά ερωτήματα**.\n\nΗ Περιφέρεια **καταβάλλει** κάθε δυνατή **προσπάθεια** να **καλύψει τις ανάγκες** των αγροτών, **λαμβάνοντας υπόψη** τις δυσκολίες της περιόδου. Ωστόσο, η κατάσταση **θέτει σε κίνδυνο** τη βιωσιμότητα της περιοχής και απαιτεί **ουσιαστικές αλλαγές**.\n\nΤο σχέδιο, που **έτυχε ευρείας αποδοχής** στη διαβούλευση, **δίνει έμφαση** στην εξοικονόμηση νερού και **βάζει τέλος** στις παράνομες γεωτρήσεις. Η Περιφέρεια **φέρει** ακέραια **την ευθύνη** για την εφαρμογή του.","en":"The Region announces that, following the serious concern expressed by residents, it has taken a series of measures to protect the groundwater table. The issue was first raised two years ago, when a university team conducted research and drew conclusions that raise serious questions.\n\nThe Region is making every possible effort to meet farmers' needs, taking into account the difficulties of the period. However, the situation puts the sustainability of the area at risk and requires substantive changes.\n\nThe plan, which met with wide acceptance in the consultation, places emphasis on saving water and puts an end to illegal boreholes. The Region bears full responsibility for its implementation.",
   "gloss":{"Περιφέρεια":"Region (administrative)","κατόπιν":"following, after","υδροφόρου ορίζοντα":"water table (gen.)","βιωσιμότητα":"sustainability","εξοικονόμηση":"saving","γεωτρήσεις":"boreholes","ακέραια":"fully, wholly"},
   "questions":[{"prompt":"Πώς ξεκίνησε η συζήτηση για το πρόβλημα;","answer":"Με μια πανεπιστημιακή έρευνα πριν από δύο χρόνια.","options":["Με μια πανεπιστημιακή έρευνα πριν από δύο χρόνια.","Με διαμαρτυρία των αγροτών φέτος.","Με παράνομες γεωτρήσεις της Περιφέρειας.","Με ένα νέο νόμο."],"why":"ετέθη … όταν πανεπιστημιακή ομάδα διεξήγαγε έρευνα."},
    {"prompt":"Τι προβλέπει το σχέδιο;","answer":"Εξοικονόμηση νερού και τέλος στις παράνομες γεωτρήσεις.","options":["Εξοικονόμηση νερού και τέλος στις παράνομες γεωτρήσεις.","Νέες γεωτρήσεις για τους αγρότες.","Αποζημιώσεις για τους κατοίκους.","Κλείσιμο του πανεπιστημίου."],"why":"δίνει έμφαση στην εξοικονόμηση νερού και βάζει τέλος στις παράνομες γεωτρήσεις."}]}
 ],
 "practice":[
  {"gen":"mc","n":12,"items":mc},
  {"gen":"type","n":8,"items":[{"prompt":f"Say in Greek: **{b}** (adj + noun)","answer":a,"why":a} for a,b in A]}
 ]
}
json.dump(L, open("/mnt/project-files/app/lessons/c1-collocations.json","w"), ensure_ascii=False, indent=1)
print("ok")
