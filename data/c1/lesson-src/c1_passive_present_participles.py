import json, sys
P = [  # verb, participle, typical phrase, meaning
 ("εργάζομαι","εργαζόμενος","οι εργαζόμενοι","employees, workers"),
 ("ενδιαφέρομαι","ενδιαφερόμενος","οι ενδιαφερόμενοι","those interested; interested party"),
 ("προΐσταμαι","προϊστάμενος","ο προϊστάμενός μου","my boss, superior"),
 ("έρχομαι","ερχόμενος","τον ερχόμενο μήνα","next, coming"),
 ("λέγομαι","λεγόμενος","ο λεγόμενος 'εθνικός διάλογος'; τα λεγόμενά του","so-called; what he said"),
 ("αναμένομαι","αναμενόμενος","όπως ήταν αναμενόμενο","expected"),
 ("κατηγορούμαι","κατηγορούμενος","ο κατηγορούμενος","defendant, the accused"),
 ("περιέχομαι","περιεχόμενος","το περιεχόμενο","content(s)"),
 ("ενδέχεται","ενδεχόμενος","το ενδεχόμενο πρόωρων εκλογών","possible; possibility"),
 ("εμπλέκομαι","εμπλεκόμενος","οι εμπλεκόμενοι φορείς","involved"),
 ("προτείνομαι","προτεινόμενος","η προτεινόμενη λύση","proposed"),
 ("προβλέπομαι","προβλεπόμενος","οι προβλεπόμενες ποινές","provided for (by law)"),
 ("οφείλομαι","οφειλόμενος","τα οφειλόμενα; οφειλόμενη σε…","owed, due; due to"),
 ("ζητούμαι","ζητούμενος","το ζητούμενο","the point, what is at stake"),
 ("θεωρούμαι","θεωρούμενος","ο θεωρούμενος ως φαβορί","considered"),
 ("αποκαλούμαι","αποκαλούμενος","η αποκαλούμενη 'γενιά των 700 ευρώ'","so-called"),
 ("εξαρτώμαι","εξαρτώμενος","τα εξαρτώμενα μέλη","dependent"),
 ("ερωτώμαι","ερωτώμενος","οι ερωτώμενοι της δημοσκόπησης","respondents"),
 ("πλήττομαι","πληττόμενος","οι πληττόμενες περιοχές","affected, hit"),
 ("διαγωνίζομαι","διαγωνιζόμενος","οι διαγωνιζόμενοι","contestants, candidates"),
 ("επιβάλλομαι","επιβαλλόμενος","τα επιβαλλόμενα μέτρα","imposed; required"),
 ("απασχολούμαι","απασχολούμενος","οι απασχολούμενοι στον τουρισμό","those employed"),
 ("συνεργάζομαι","συνεργαζόμενος","οι συνεργαζόμενες εταιρείες","partner, cooperating"),
 ("τεκταίνομαι","τεκταινόμενος","τα τεκταινόμενα","goings-on (behind the scenes)"),
]
L = {
 "el": "Μετοχές σε -όμενος, -ούμενος",
 "title": "Present passive participles: οι εργαζόμενοι, το ζητούμενο",
 "section": "C1 · learned morphology",
 "goal": "Read and use the -όμενος participles that make formal Greek compact, and keep them apart from -μένος.",
 "blocks": [
  {"type":"text","text":"Besides the perfect participle in **-μένος** (B2), formal Greek has a **present passive participle** in **-όμενος** (also -ούμενος, -ώμενος). It declines like any -ος, -η, -ο adjective, so it is easy on the endings, but it is a register signal: one participle replaces a whole relative clause. *Οι άνθρωποι που εργάζονται* → **οι εργαζόμενοι**; *η λύση που προτείνεται* → **η προτεινόμενη λύση**."},
  {"type":"table","title":"Formation from the present passive","head":["Present passive","Participle","Stress"],"rows":[
    ["-ομαι: εργάζ**ομαι**, προτείν**ομαι**","εργαζ**όμενος**, προτειν**όμενος**","always on -**ό**-"],
    ["-ούμαι: θεωρ**ούμαι**, απασχολ**ούμαι**","θεωρ**ούμενος**, απασχολ**ούμενος**","always on -**ού**-"],
    ["-ώμαι: εξαρτ**ώμαι**, ερωτ**ώμαι**","εξαρτ**ώμενος**, ερωτ**ώμενος**","always on -**ώ**-"],
    ["-ιέμαι (αγαπιέμαι), -άμαι (θυμάμαι)","none: use a relative clause","—"]]},
  {"type":"table","title":"-όμενος vs -μένος","head":["-όμενος: in progress, expected, general","-μένος: completed, resulting state"],"rows":[
    ["ο **ερχόμενος** μήνας 'the coming month'","ο **περασμένος** μήνας 'last month'"],
    ["τα **γραφόμενα** 'what is being written (in the press)'","τα **γραμμένα** 'what is written (down)'"],
    ["ο **εξεταζόμενος** 'the person being examined'","ο **εξετασμένος** 'one who has been examined'"],
    ["ο **ασφαλιζόμενος** 'the insured (person paying in)'","**ασφαλισμένος** 'insured (state)'"],
    ["οι **πληττόμενες** περιοχές 'the areas being hit'","οι **πληγείσες** περιοχές 'the areas that were hit' (learned aorist participle, news only)"]]},
  {"type":"table","title":"Two dozen to own","head":["Verb","Participle","Typical phrase","Meaning"],"rows":[[a,f"**{b}**",c,d] for a,b,c,d in P]},
  {"type":"callout","text":"**Nominalised:** most of these are used as nouns with the article: **οι εργαζόμενοι, οι ενδιαφερόμενοι, ο κατηγορούμενος, το περιεχόμενο, το ενδεχόμενο, το ζητούμενο, τα τεκταινόμενα**. *Το ζητούμενο είναι…* 'the point is…' is a C1 favourite for framing an argument.\n\n**Learned aorist participles in -είς, -είσα, -έν** appear in the news and the law: *ο εκλεγείς πρόεδρος* 'the elected president', *οι συλληφθέντες* 'those arrested', *οι πληγέντες* 'the victims, those hit', *το προκύψαν πρόβλημα* 'the problem that arose'. Recognise them; you never need to produce them."},
  {"type":"reading","title":"Νέα ρύθμιση για την τηλεργασία","text":"Το υπουργείο Εργασίας έθεσε σε δημόσια διαβούλευση την **προτεινόμενη** ρύθμιση για την τηλεργασία. Σύμφωνα με το **περιεχόμενο** του σχεδίου, οι **εργαζόμενοι** θα μπορούν να δουλεύουν από το σπίτι έως δύο ημέρες την εβδομάδα, εφόσον συμφωνεί ο **προϊστάμενός** τους.\n\nΟι **ενδιαφερόμενοι** φορείς έχουν προθεσμία έως τον **ερχόμενο** μήνα για να καταθέσουν τις παρατηρήσεις τους. Όπως ήταν **αναμενόμενο**, οι εργοδοτικές οργανώσεις χαιρέτισαν τη ρύθμιση, ενώ τα συνδικάτα ζητούν να καλυφθούν τα **οφειλόμενα** έξοδα ρεύματος και ίντερνετ.\n\nΣε πρόσφατη δημοσκόπηση, επτά στους δέκα **ερωτώμενους** δήλωσαν ότι θα προτιμούσαν ένα μεικτό μοντέλο. Το **ζητούμενο**, σύμφωνα με αναλυτές, δεν είναι αν θα υπάρξει τηλεργασία, αλλά ποιος θα σηκώσει το κόστος της. Δεν αποκλείεται, πάντως, το **ενδεχόμενο** να αλλάξει το κείμενο πριν φτάσει στη Βουλή.","en":"The Ministry of Labour has put the proposed regulation on remote work out to public consultation. According to the content of the draft, employees will be able to work from home up to two days a week, provided their superior agrees.\n\nThe bodies concerned have until next month to submit their comments. As expected, employers' organisations welcomed the regulation, while the unions are asking for the electricity and internet costs owed to be covered.\n\nIn a recent poll, seven out of ten respondents said they would prefer a hybrid model. The real question, analysts say, is not whether there will be remote work but who will bear its cost. The possibility that the text will change before it reaches Parliament is not ruled out, in any case.",
   "gloss":{"τηλεργασία":"remote work","έθεσε σε διαβούλευση":"put out to consultation","φορείς":"bodies, organisations","προθεσμία":"deadline","χαιρέτισαν":"welcomed","συνδικάτα":"trade unions","μεικτό":"mixed, hybrid","σηκώσει το κόστος":"bear the cost"},
   "questions":[
    {"prompt":"Υπό ποια προϋπόθεση θα δουλεύει κανείς από το σπίτι;","answer":"Αν συμφωνεί ο προϊστάμενός του.","options":["Αν συμφωνεί ο προϊστάμενός του.","Αν πληρώνει ο ίδιος το ρεύμα.","Μόνο αν μένει μακριά.","Μόνο τον ερχόμενο μήνα."],"why":"εφόσον συμφωνεί ο προϊστάμενός τους."},
    {"prompt":"Τι ζητούν τα συνδικάτα;","answer":"Να πληρωθούν τα έξοδα που έχουν οι εργαζόμενοι στο σπίτι.","options":["Να πληρωθούν τα έξοδα που έχουν οι εργαζόμενοι στο σπίτι.","Να καταργηθεί η τηλεργασία.","Περισσότερες ημέρες τηλεργασίας.","Νέα δημοσκόπηση."],"why":"να καλυφθούν τα οφειλόμενα έξοδα ρεύματος και ίντερνετ."},
    {"prompt":"Ποιο είναι, κατά τους αναλυτές, το πραγματικό ερώτημα;","answer":"Ποιος θα πληρώσει το κόστος.","options":["Ποιος θα πληρώσει το κόστος.","Αν θα υπάρξει τηλεργασία.","Πότε θα ψηφιστεί ο νόμος.","Πόσοι προτιμούν το γραφείο."],"why":"Το ζητούμενο … ποιος θα σηκώσει το κόστος της."}]}
 ],
 "practice": [
  {"gen":"type","n":10,"items":[{"prompt":f"Participle in -μενος of **{a}** (→ {d})","answer":b,"why":f"{a} → {b}: {c}"} for a,b,c,d in P]},
  {"gen":"mc","items":[
    {"prompt":"Οι ___ πρέπει να υποβάλουν αίτηση έως την Παρασκευή. (those interested)","answer":"ενδιαφερόμενοι","options":["ενδιαφερόμενοι","ενδιαφέροντες","ενδιαφερμένοι","ενδιαφέρονται"],"why":"οι ενδιαφερόμενοι; ενδιαφέροντες means 'interesting'."},
    {"prompt":"Ο ___ αρνήθηκε όλες τις κατηγορίες. (the accused)","answer":"κατηγορούμενος","options":["κατηγορούμενος","κατηγορημένος","κατήγορος","κατηγορών"],"why":"ο κατηγορούμενος 'defendant'; ο κατήγορος is the prosecutor."},
    {"prompt":"Το ___ δεν είναι να κερδίσουμε, αλλά να πείσουμε. (the point)","answer":"ζητούμενο","options":["ζητούμενο","ζητημένο","ζήτημα","ζητούμενος"],"why":"Το ζητούμενο είναι… 'the point is…'."},
    {"prompt":"Δεν αποκλείουμε το ___ πρόωρων εκλογών. (possibility)","answer":"ενδεχόμενο","options":["ενδεχόμενο","ενδεχομένως","ενδεχόμενος","ενδέχεται"],"why":"το ενδεχόμενο (noun). ενδεχομένως is the adverb 'possibly'."},
    {"prompt":"Τα μέτρα αφορούν τις ___ από τις πλημμύρες περιοχές. (being hit)","answer":"πληττόμενες","options":["πληττόμενες","πληγωμένες","πληκτικές","πλήττουσες"],"why":"πλήττομαι → πληττόμενος. πληκτικός = boring!"},
    {"prompt":"Όπως ήταν ___, η συνάντηση δεν κατέληξε πουθενά. (expected)","answer":"αναμενόμενο","options":["αναμενόμενο","αναμενόμενος","περιμένοντας","αναμένοντας"],"why":"όπως ήταν αναμενόμενο (neuter, impersonal)."},
    {"prompt":"Οι ___ στον τουρισμό αυξήθηκαν κατά 8%. (those employed)","answer":"απασχολούμενοι","options":["απασχολούμενοι","απασχολημένοι","απασχόληση","απασχολώντες"],"why":"οι απασχολούμενοι = people in employment; απασχολημένος = busy."},
    {"prompt":"Τα ___ του υπουργού προκάλεσαν αντιδράσεις. (what he said)","answer":"λεγόμενα","options":["λεγόμενα","λέγοντας","λέξεις","ειπωμένα"],"why":"τα λεγόμενά του 'his words, what he said'."}]}
 ]
}
json.dump(L, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
