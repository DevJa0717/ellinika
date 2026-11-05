PART = dict(id="dioikisi", el="Η γλώσσα της διοίκησης", en="The language of officialdom",
            intro_el="Ανακοινώσεις δήμων, πανεπιστημίων και της Πολιτικής Προστασίας: πώς διαβάζουμε τα ελληνικά των υπηρεσιών.",
            intro_en="Announcements from town halls, universities and Civil Protection: how to read the Greek of public services.")

CHAPTERS = [
dict(
 id="anakoinoseis", el="Πώς διαβάζουμε μια ανακοίνωση", title="How to read an official announcement", level="C1",
 summary_en="Officialese (υπηρεσιακή γλώσσα) survives in every announcement: the town hall's notice on a road opening and an office relocation (and a note on how the 2011 Kallikratis reform abolished the old prefectures), a university faculty's call for placement exams, and a Civil Protection weather warning. Each text is decoded sentence by sentence into everyday Greek.",
 sections=[
  dict(id="dimos", el="Ανακοίνωση του δήμου", en="A town-hall notice", paras=[
   ("«Ο Δήμος ανακοινώνει ότι, λόγω των εργασιών διάνοιξης της οδού Αγίου Δημητρίου, η κυκλοφορία θα διακοπεί για χρονικό διάστημα ενός διμήνου. Σημειωτέον ότι οι υπηρεσίες του Δήμου θα μετεγκατασταθούν προσωρινά στο οίκημα του πρώην νομαρχιακού διοικητηρίου. Οι πολίτες παρακαλούνται για την κατανόησή τους». Σε απλά ελληνικά: ο δρόμος θα κλείσει για δύο μήνες, επειδή τον ανοίγουν, και τα γραφεία του δήμου πηγαίνουν για λίγο στο παλιό κτίριο της νομαρχίας.",
    "'The Municipality announces that, owing to works to open up Agiou Dimitriou Street, traffic will be suspended for a period of two months. It should be noted that municipal services will be temporarily relocated to the premises of the former prefectural administration building. Citizens are asked for their understanding.' In plain Greek: the road will be closed for two months because they are opening it up, and the council offices are moving for a while to the old prefecture building.", ["w_officialese", "w_press_release"]),
   ("Οι νομαρχίες καταργήθηκαν με τη μεταρρύθμιση «Καλλικράτης», που εφαρμόστηκε το 2010–2011· τη θέση τους πήραν οι περιφέρειες και οι μεγαλύτεροι δήμοι. Πολλά κτίρια όμως λέγονται ακόμα «νομαρχία», όπως πολλοί λένε ακόμα «δραχμές» για τα λεφτά. Η υπηρεσιακή γλώσσα αγαπά τις παθητικές μετοχές («οι πολίτες παρακαλούνται»), τις λόγιες λέξεις («οίκημα» αντί για «κτίριο») και τα επιρρήματα σε -ως.",
    "The prefectures were abolished by the 'Kallikratis' reform, implemented in 2010–2011; regions and larger municipalities took their place. But many buildings are still called 'the prefecture', just as many people still say 'drachmas' for money. Officialese loves passives ('citizens are requested'), learned words (οίκημα for κτίριο) and adverbs in -ως.", ["w_kallikratis", "w_officialese"]),
  ]),
  dict(id="panepistimio", el="Ανακοίνωση της σχολής", en="A faculty notice", paras=[
   ("«Ο Κοσμήτορας της Σχολής ανακοινώνει ότι οι κατατακτήριες εξετάσεις για πτυχιούχους θα διεξαχθούν εντός του δεκαημέρου 10–20 Δεκεμβρίου. Οι αιτήσεις υποβάλλονται έως την εκπνοή της τακτής προθεσμίας. Ο αριθμός των εισακτέων ορίζεται ισάριθμος με τις κενές θέσεις, με διαβάθμιση βάσει της βαθμολογίας. Το Συντονιστικό Όργανο της Σχολής εισηγείται τη συμμετοχή ενός συντονιστή ανά μάθημα». Δηλαδή: όσοι έχουν ήδη πτυχίο μπορούν να δώσουν εξετάσεις για να μπουν σε άλλη σχολή, τον Δεκέμβριο· θα μπουν τόσοι όσες οι θέσεις, με σειρά βαθμολογίας.",
    "'The Dean of the School announces that placement exams for graduates will be held within the ten days 10–20 December. Applications are to be submitted by the expiry of the set deadline. The number of entrants is set equal to the vacant places, ranked by mark. The School's Coordinating Body recommends one coordinator per subject.' That is: people who already have a degree can sit exams to enter another school in December; as many will get in as there are places, in order of marks.", ["w_education_greece"]),
  ]),
  dict(id="politiki-prostasia", el="Μήνυμα της Πολιτικής Προστασίας", en="A Civil Protection message", paras=[
   ("«Έκτακτο δελτίο επιδείνωσης καιρού. Από το απόγευμα της Πέμπτης αναμένονται σποραδικές καταιγίδες, κατά τόπους ισχυρές, και διάσπαρτες χαλαζοπτώσεις. Συνιστάται επαγρύπνηση στους πολίτες και αποφυγή μετακινήσεων κοντά σε ρέματα, όπου ενδέχεται να σημειωθεί αυξημένη εκροή υδάτων». Σε απλά λόγια: θα βρέξει δυνατά σε μερικά σημεία, ίσως πέσει και χαλάζι· προσέξτε και μην πηγαίνετε κοντά σε ρέματα, γιατί μπορεί να πλημμυρίσουν.",
    "'Emergency bulletin on deteriorating weather. From Thursday afternoon sporadic thunderstorms are expected, locally severe, with scattered hail. Citizens are advised to be vigilant and to avoid travel near streams, where increased outflow of water may occur.' In plain words: it will rain hard in some places, maybe hail too; be careful and don't go near streams, because they may flood.", ["w_civil_protection", "w_weather_warning"]),
   ("Η γλώσσα αυτή έχει τη λογική της: πρέπει να είναι ακριβής και ουδέτερη. Συχνά όμως γίνεται δυσνόητη, και μια σωρεία λόγιων λέξεων κρύβει το απλό μήνυμα. Οι ειδικοί της επικοινωνίας μνημονεύουν πάντα τον κανόνα: πρώτα τι πρέπει να κάνει ο πολίτης, και μετά οι εξηγήσεις. Η μετεξέλιξη της υπηρεσιακής γλώσσας προς πιο απλά ελληνικά βρίσκεται, όπως λένε, «στο μεταίχμιο»: η διάθεση υπάρχει, οι συνήθειες αντιστέκονται.",
    "This language has its logic: it must be precise and neutral. But it often becomes hard to understand, and a pile (σωρεία) of learned words hides the simple message. Communication experts always cite the rule: first what the citizen must do, then the explanations. The evolution of officialese towards plainer Greek is, as they say, 'at a turning point' (στο μεταίχμιο): the will is there, but habits resist.", ["w_officialese"]),
  ]),
 ],
 grammar=[
  dict(level="C1", title="Οι πολίτες παρακαλούνται: the impersonal official passive",
       el="Η παθητική φωνή των ανακοινώσεων.",
       en="Official notices address the public in the passive: **οι πολίτες παρακαλούνται να…** (citizens are requested to), **οι ενδιαφερόμενοι καλούνται να…** (those interested are invited to), **απαγορεύεται η στάθμευση**, **συνιστάται επαγρύπνηση**, **θα διεξαχθούν** (will be held). Spoken Greek uses the active: *παρακαλούμε τους πολίτες*, *μην παρκάρετε*.",
       examples=[("Οι ενδιαφερόμενοι καλούνται να υποβάλουν αίτηση.", "Those interested are invited to apply."), ("Απαγορεύεται η είσοδος σε μη εξουσιοδοτημένα άτομα.", "No entry for unauthorised persons."), ("Οι εξετάσεις θα διεξαχθούν τον Δεκέμβριο.", "The exams will be held in December.")]),
  dict(level="C1", title="Σημειωτέον, εισακτέος: verbal adjectives in -τέος",
       el="Ρηματικά επίθετα σε -τέος (κάτι που πρέπει να γίνει).",
       en="Ancient verbal adjectives in **-τέος** mean 'that must be done': **σημειωτέον** (it must be noted), **εισακτέοι** (those to be admitted), **ληπτέος** (to be taken: *ληπτέα μέτρα*), **αποδεκτός** differs (acceptable). They survive in formal and administrative texts.",
       examples=[("Σημειωτέον ότι η προθεσμία δεν παρατείνεται.", "It should be noted that the deadline will not be extended."), ("Ο αριθμός των εισακτέων αυξήθηκε.", "The number of entrants increased."), ("Συζητήθηκαν τα ληπτέα μέτρα.", "The measures to be taken were discussed.")]),
  dict(level="C1", title="Δίμηνο, δεκαήμερο, εξάμηνο: compound time nouns",
       el="Σύνθετα ουσιαστικά για χρονικά διαστήματα.",
       en="Number + period gives neuter nouns: **το δίμηνο**, **το τρίμηνο**, **το εξάμηνο** (semester), **το δεκαήμερο**, **το δεκαπενθήμερο** (fortnight), **το τριήμερο** (long weekend), **η πενταετία**, **η δεκαετία**. Adjectives: **διμηνιαίος**, **εξαμηνιαίος**.",
       examples=[("Ο δρόμος θα κλείσει για ένα δίμηνο.", "The road will close for two months."), ("Φεύγουμε για τριήμερο στο χωριό.", "We're off to the village for a long weekend."), ("Το χειμερινό εξάμηνο αρχίζει τον Οκτώβριο.", "The winter semester starts in October.")]),
 ],
 terms=[
  ("η διάνοιξη", "opening up (of a road)", "Κατασκευή νέου δρόμου ή διεύρυνση παλιού.", "Building a new road or widening an old one."),
  ("η μετεγκατάσταση", "relocation", "Μεταφορά μιας υπηρεσίας σε άλλο χώρο.", "Moving a service to another place."),
  ("το οίκημα", "premises, building", "Λόγια λέξη για το κτίριο.", "A formal word for a building."),
  ("νομαρχιακός", "prefectural", "Της παλιάς νομαρχίας.", "Of the former prefecture."),
  ("ο κοσμήτορας", "dean", "Ο επικεφαλής μιας πανεπιστημιακής σχολής.", "The head of a university school."),
  ("κατατακτήριος", "placement (exam)", "Για εισαγωγή πτυχιούχων σε άλλη σχολή.", "For graduates entering another school."),
  ("τακτός", "fixed, set", "Ορισμένος από πριν.", "Set in advance."),
  ("ισάριθμος", "equal in number", "Με τον ίδιο αριθμό.", "Of the same number."),
  ("σποραδικός", "sporadic, scattered", "Που εμφανίζεται εδώ κι εκεί, όχι παντού.", "Appearing here and there, not everywhere."),
  ("η επαγρύπνηση", "vigilance", "Αυξημένη προσοχή απέναντι σε κίνδυνο.", "Heightened attention to danger."),
 ],
 questions=[
  ("Γιατί θα κλείσει ο δρόμος;", ["Για εργασίες διάνοιξης", "Για παρέλαση", "Λόγω χιονιού", "Για πάντα"], "Για εργασίες διάνοιξης", "Για ένα δίμηνο."),
  ("Πότε καταργήθηκαν οι νομαρχίες;", ["Με τον «Καλλικράτη», το 2010–2011", "Το 1821", "Το 1974", "Δεν καταργήθηκαν"], "Με τον «Καλλικράτη», το 2010–2011", "Τη θέση τους πήραν οι περιφέρειες."),
  ("Ποιος μπορεί να δώσει κατατακτήριες εξετάσεις;", ["Όσοι έχουν ήδη πτυχίο", "Οι μαθητές του λυκείου", "Οι καθηγητές", "Όλοι"], "Όσοι έχουν ήδη πτυχίο", "Για να μπουν σε άλλη σχολή."),
  ("Τι σημαίνει «σποραδικές καταιγίδες»;", ["Καταιγίδες σε μερικά σημεία", "Καταιγίδες παντού", "Χωρίς βροχή", "Χιόνι"], "Καταιγίδες σε μερικά σημεία", "Σποραδικός = εδώ κι εκεί."),
  ("Ποιος είναι ο κανόνας της καλής ανακοίνωσης;", ["Πρώτα τι πρέπει να κάνει ο πολίτης", "Πρώτα οι εξηγήσεις", "Όσο πιο λόγια τόσο καλύτερα", "Μόνο αριθμοί"], "Πρώτα τι πρέπει να κάνει ο πολίτης", "Μετά οι εξηγήσεις."),
 ],
 vocab=["η διάνοιξη", "το δίμηνο", "σημειωτέον", "η μετεγκατάσταση", "το οίκημα", "νομαρχιακός", "το διοικητήριο", "ο κοσμήτορας", "κατατακτήριος", "το δεκαήμερο", "η εκπνοή", "τακτός", "ισάριθμος", "η διαβάθμιση", "εισηγούμαι", "ο συντονιστής"],
),
]
