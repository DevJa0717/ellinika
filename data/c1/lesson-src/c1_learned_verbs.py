import json, sys
MI = [ # present 3sg, past 3sg, meaning, example
 ("τίθεται","ετέθη","is set, is raised (θέτω)","Τίθεται το ερώτημα αν… / Το θέμα ετέθη στη σύσκεψη."),
 ("δίδεται","εδόθη","is given (δίνω)","Δίδεται η δυνατότητα σε όλους. / Εδόθη παράταση."),
 ("καθίσταται","κατέστη","becomes, is rendered","Κατέστη σαφές ότι… 'It became clear that…'"),
 ("υφίσταται","υπέστη","exists; suffers, undergoes","Δεν υφίσταται λόγος ανησυχίας. / Υπέστη σοβαρές ζημιές."),
 ("συνίσταται","συνέστη","consists in; is recommended","Το πρόβλημα συνίσταται στην έλλειψη χρόνου. / Συνίσταται προσοχή."),
 ("διατίθεται","διετέθη","is available, allocated","Το βιβλίο διατίθεται σε όλα τα βιβλιοπωλεία."),
 ("προτίθεται","—","intends (+ να)","Η κυβέρνηση προτίθεται να μειώσει τους φόρους."),
 ("επιτίθεται","επιτέθηκε","attacks","Ο σκύλος επιτέθηκε στον ταχυδρόμο."),
 ("ανατίθεται","ανατέθηκε","is assigned","Η μελέτη ανατέθηκε σε ιδιωτική εταιρεία."),
]
IMP = [
 ("πρόκειται να","be going to; be due to","Πρόκειται να ανακοινωθούν μέτρα."),
 ("πρόκειται για","it is a matter of, it's about","Πρόκειται για σοβαρό λάθος."),
 ("δεν πρόκειται να","there's no way that…","Δεν πρόκειται να υποχωρήσω!"),
 ("επιβάλλεται (να)","it is imperative","Επιβάλλεται να ληφθούν μέτρα."),
 ("απαιτείται","is required","Απαιτείται άριστη γνώση αγγλικών."),
 ("ενδείκνυται","is advisable, appropriate","Δεν ενδείκνυται για παιδιά."),
 ("εκκρεμεί","is pending","Εκκρεμεί η απόφαση του δικαστηρίου."),
 ("εναπόκειται σε","it is up to","Εναπόκειται στον καθένα να αποφασίσει."),
 ("διέπει","governs (rules, law)","Οι κανόνες που διέπουν τη λειτουργία της Βουλής."),
 ("εμπίπτει σε","falls within","Δεν εμπίπτει στις αρμοδιότητές μου."),
 ("ελλοχεύει","lurks","Ελλοχεύει ο κίνδυνος της αδιαφορίας."),
 ("διαφαίνεται","emerges, becomes apparent","Διαφαίνεται μια λύση."),
 ("επέρχεται","ensues, comes about","Επήλθε συμφωνία."),
 ("προκύπτει","arises, follows","Από τα στοιχεία προκύπτει ότι… / Προέκυψε πρόβλημα."),
 ("αρμόζει","befits","Όπως αρμόζει σε έναν πρόεδρο."),
 ("δέον (να)","it is proper/necessary (very formal)","Δέον να σημειωθεί ότι…"),
]
L = {
 "el": "Λόγια ρήματα",
 "title": "Learned verbs: τίθεται, κατέστη, υπέστη, πρόκειται, εναπόκειται",
 "section": "C1 · learned morphology",
 "goal": "Recognise the learned verb forms of formal Greek and use the dozen impersonals that structure an argument.",
 "blocks": [
  {"type":"text","text":"Formal Greek keeps a handful of ancient **-μι** verbs (τίθημι 'place', δίδωμι 'give', ίστημι 'stand') inside compounds you meet every day: **τίθεται** 'is placed, raised', **καθίσταται** 'becomes', **υφίσταται** 'exists, suffers'. They have their own present (-ται with -ι- or -ί- reduplication: τ**ί**θεται, δ**ί**δεται, **ί**σταται) and learned pasts (ετέθη, εδόθη, κατέστη, υπέστη). Around them sits a set of **impersonal verbs** (πρόκειται, επιβάλλεται, εναπόκειται, προκύπτει) that do the work English gives to 'it is…that' constructions."},
  {"type":"table","title":"Survivors of -μι verbs","head":["Present 3sg","Past 3sg","Meaning","Example"],"rows":[[f"**{a}**",f"**{b}**",c,d] for a,b,c,d in MI]},
  {"type":"callout","text":"**Persons other than the 3rd** are rare but exist: *υφίσταμαι πίεση* 'I am under pressure', *δεν προτίθεμαι να…* 'I have no intention of…', *καθίσταμαι υπεύθυνος* 'I am rendered responsible'. In speech the 3sg/3pl carry 95% of the load: **τίθεται, τίθενται, κατέστη, κατέστησαν, υπέστησαν**.\n\n**καθιστώ** is the active partner of καθίσταμαι: *Η απόφαση καθιστά αδύνατη τη συνεργασία* 'The decision makes cooperation impossible'. Its past: **κατέστησε** (*κατέστησε σαφές ότι…* 'made it clear that…')."},
  {"type":"table","title":"Impersonals that structure an argument","head":["Verb","Meaning","Example"],"rows":[[f"**{a}**",b,c] for a,b,c in IMP]},
  {"type":"callout","text":"**πρόκειται** has three readings: future intention *Πρόκειται να φύγει* 'He's due to leave'; strong refusal *Δεν πρόκειται!* 'No way!'; identification *Πρόκειται για…* 'It's about / It's a case of…'. The last one is your universal answer to *Τι είναι αυτό;* in formal speech: *Πρόκειται για ένα σχέδιο που…*\n\n**προέκυψε / επήλθε / κατέστη** are the learned pasts of προκύπτει, επέρχεται, καθίσταται; the everyday equivalents are *βγήκε, ήρθε, έγινε*."},
  {"type":"culture","title":"Η γλώσσα της ανακοίνωσης","text":"Every Greek announcement, from a ministry to a block of flats (*πολυκατοικία*), reaches for these verbs. A typical notice on the lift: *Γνωστοποιείται στους κ.κ. ενοίκους ότι λόγω εργασιών η παροχή νερού θα διακοπεί… Παρακαλούνται οι ένοικοι…* 'Messrs. tenants are hereby informed…'. Greeks parody this register (*ξύλινη γλώσσα* 'wooden language', officialese) but switch into it instantly when they write a complaint."},
  {"type":"reading","title":"Ανακοίνωση του Συλλόγου Γονέων","text":"Το Διοικητικό Συμβούλιο του Συλλόγου Γονέων και Κηδεμόνων γνωστοποιεί ότι, κατά τη χθεσινή συνεδρίαση, **ετέθη** εκ νέου το ζήτημα της θέρμανσης του σχολείου. Όπως **κατέστη** σαφές από την ενημέρωση της διευθύντριας, το κτίριο **υπέστη** σοβαρές φθορές κατά τη διάρκεια της κακοκαιρίας του Ιανουαρίου και **εκκρεμεί** ακόμη η επισκευή του λεβητοστασίου.\n\n**Πρόκειται για** ζήτημα που **δεν εμπίπτει** στις αρμοδιότητες του Συλλόγου, αλλά του Δήμου. Ωστόσο, **επιβάλλεται** να ενεργήσουμε άμεσα, καθώς **ελλοχεύει** ο κίνδυνος να κλείσει το σχολείο τον χειμώνα.\n\nΤο Δ.Σ. **προτίθεται** να ζητήσει συνάντηση με τον Δήμαρχο. Από τα στοιχεία που έχουμε στη διάθεσή μας **προκύπτει** ότι το απαιτούμενο ποσό **διατίθεται** ήδη στον προϋπολογισμό. **Εναπόκειται**, επομένως, στη δημοτική αρχή να το αξιοποιήσει. **Συνίσταται** στους γονείς να ντύνουν τα παιδιά ζεστά μέχρι νεωτέρας.","en":"The Board of the Parents' and Guardians' Association announces that at yesterday's meeting the issue of the school's heating was raised again. As became clear from the head teacher's briefing, the building suffered serious damage during the January storm and the repair of the boiler room is still pending.\n\nThis is a matter that does not fall within the Association's remit but the Municipality's. Nevertheless we must act immediately, as there is a risk that the school will close in winter.\n\nThe Board intends to request a meeting with the Mayor. The figures at our disposal show that the required sum is already available in the budget. It is therefore up to the municipal authority to use it. Parents are advised to dress their children warmly until further notice.",
   "gloss":{"κηδεμόνων":"guardians (gen. pl.)","γνωστοποιεί":"announces, makes known","εκ νέου":"anew, again","φθορές":"damage, wear","λεβητοστασίου":"boiler room (gen.)","αρμοδιότητες":"remit, competences","προϋπολογισμό":"budget","μέχρι νεωτέρας":"until further notice"},
   "questions":[
    {"prompt":"Ποιος είναι αρμόδιος για την επισκευή;","answer":"Ο Δήμος.","options":["Ο Δήμος.","Ο Σύλλογος Γονέων.","Η διευθύντρια.","Το υπουργείο."],"why":"δεν εμπίπτει στις αρμοδιότητες του Συλλόγου, αλλά του Δήμου."},
    {"prompt":"Τι λείπει, σύμφωνα με τον Σύλλογο;","answer":"Η απόφαση του Δήμου να χρησιμοποιήσει τα χρήματα που ήδη έχει.","options":["Η απόφαση του Δήμου να χρησιμοποιήσει τα χρήματα που ήδη έχει.","Τα χρήματα για την επισκευή.","Η άδεια από το υπουργείο.","Ένα νέο λεβητοστάσιο στον προϋπολογισμό."],"why":"το ποσό διατίθεται ήδη … Εναπόκειται … στη δημοτική αρχή να το αξιοποιήσει."}]}
 ],
 "practice": [
  {"gen":"mc","items":[
    {"prompt":"Στη σύσκεψη ___ το θέμα της χρηματοδότησης. (was raised)","answer":"ετέθη","options":["ετέθη","τίθεται","έθεσε","τέθηκαν"],"why":"Past passive 3sg of θέτω, learned: ετέθη (also τέθηκε)."},
    {"prompt":"Μετά τη συζήτηση ___ σαφές ότι δεν υπάρχει συμφωνία. (became)","answer":"κατέστη","options":["κατέστη","καθίσταται","κατέστησε","καθίστηκε"],"why":"κατέστη σαφές 'it became clear'; κατέστησε is transitive 'made'."},
    {"prompt":"Το πλοίο ___ ζημιές από την κακοκαιρία. (suffered)","answer":"υπέστη","options":["υπέστη","υφίσταται","υπήρξε","υπέφερε"],"why":"υπέστη ζημιές; υπέφερε means suffered pain."},
    {"prompt":"___ για μια πρόταση που αξίζει προσοχή. (It's a matter of)","answer":"Πρόκειται","options":["Πρόκειται","Προκύπτει","Επιβάλλεται","Ενδείκνυται"],"why":"Πρόκειται για + accusative."},
    {"prompt":"___ στους πολίτες να αποφασίσουν. (It is up to)","answer":"Εναπόκειται","options":["Εναπόκειται","Εμπίπτει","Επέρχεται","Διέπει"],"why":"εναπόκειται σε κάποιον."},
    {"prompt":"Το θέμα δεν ___ στις αρμοδιότητές μας. (fall within)","answer":"εμπίπτει","options":["εμπίπτει","εναπόκειται","συνίσταται","επέρχεται"],"why":"εμπίπτω σε 'fall within'."},
    {"prompt":"Από την έρευνα ___ ότι οι νέοι διαβάζουν λιγότερο. (it follows)","answer":"προκύπτει","options":["προκύπτει","πρόκειται","ελλοχεύει","αρμόζει"],"why":"προκύπτει ότι 'it emerges/follows that'."},
    {"prompt":"Η κυβέρνηση ___ να αυξήσει τον κατώτατο μισθό. (intends)","answer":"προτίθεται","options":["προτίθεται","πρόκειται","προτείνει","προκύπτει"],"why":"προτίθεμαι να 'intend to'. (πρόκειται να = is due to, no subject intent.)"},
    {"prompt":"Ποιο σημαίνει «Δεν θα το κάνω με τίποτα»;","answer":"Δεν πρόκειται να το κάνω.","options":["Δεν πρόκειται να το κάνω.","Δεν ενδείκνυται να το κάνω.","Δεν εκκρεμεί να το κάνω.","Δεν προκύπτει να το κάνω."],"why":"δεν πρόκειται να = no way."},
    {"prompt":"Το φάρμακο δεν ___ για παιδιά κάτω των 12. (is advisable)","answer":"ενδείκνυται","options":["ενδείκνυται","επιβάλλεται","διατίθεται","εμπίπτει"],"why":"ενδείκνυται 'is indicated, advisable'."},
    {"prompt":"Ο νόμος που ___ τις εκλογές άλλαξε το 2016. (governs)","answer":"διέπει","options":["διέπει","διατίθεται","διαφαίνεται","διακόπτει"],"why":"διέπω 'govern' (rules, laws)."},
    {"prompt":"Τελικά ___ συμφωνία μετά από δεκαέξι ώρες. (came about)","answer":"επήλθε","options":["επήλθε","επέρχεται","επιτέθηκε","επέβαλε"],"why":"επέρχεται → past επήλθε."}]},
  {"gen":"type","n":6,"items":[
    {"prompt":"Say it formally: *Βγήκε ένα πρόβλημα.* → ___ πρόβλημα.","answer":"Προέκυψε","accept":["Προέκυψε","προέκυψε"],"why":"βγήκε → προέκυψε."},
    {"prompt":"Say it formally: *Έγινε φανερό ότι…* → ___ σαφές ότι…","answer":"Κατέστη","accept":["Κατέστη","κατέστη"]},
    {"prompt":"Say it formally: *Πρέπει οπωσδήποτε να…* → ___ να…","answer":"Επιβάλλεται","accept":["Επιβάλλεται","επιβάλλεται"]},
    {"prompt":"Say it formally: *Χρειάζεται πτυχίο.* → ___ πτυχίο.","answer":"Απαιτείται","accept":["Απαιτείται","απαιτείται"]},
    {"prompt":"Say it formally: *Δεν υπάρχει λόγος.* → Δεν ___ λόγος.","answer":"υφίσταται","accept":["υφίσταται"]},
    {"prompt":"Say it formally: *Μπαίνει το ερώτημα…* → ___ το ερώτημα…","answer":"Τίθεται","accept":["Τίθεται","τίθεται"]},
    {"prompt":"Say it formally: *Το βιβλίο πουλιέται παντού.* → Το βιβλίο ___ παντού.","answer":"διατίθεται","accept":["διατίθεται"]},
    {"prompt":"Say it formally: *Εξαρτάται από σένα.* → ___ σε σένα.","answer":"Εναπόκειται","accept":["Εναπόκειται","εναπόκειται"]}]}
 ]
}
json.dump(L, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
