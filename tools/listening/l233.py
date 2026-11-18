# Source for library/listening/listening-233.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l233.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l233-news-leoforeio-choris-odigo", "title": "Ένα λεωφορείο χωρίς οδηγό στην παραλιακή", "title_en": "A driverless bus on the seafront", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Από τη Δευτέρα, ένα μικρό ηλεκτρικό λεωφορείο χωρίς οδηγό θα κάνει δοκιμαστικά δρομολόγια στην παραλιακή λεωφόρο της πόλης μας. Το λεωφορείο θα κινείται σε μια διαδρομή δύο χιλιομέτρων, από το λιμάνι ως το δημοτικό κολυμβητήριο.", "From Monday, a small driverless electric bus will run trial services on our city's seafront avenue. The bus will travel a two-kilometre route, from the harbour to the municipal swimming pool."),
  L("Εκφωνητής", "m", "Χωράει δώδεκα επιβάτες και δεν θα ξεπερνά τα είκοσι χιλιόμετρα την ώρα. Με αισθητήρες και κάμερες «βλέπει» τους πεζούς, τα ποδήλατα και τα αυτοκίνητα γύρω του και σταματά μόνο του, αν κάτι βρεθεί μπροστά του.", "It holds twelve passengers and won't go faster than twenty kilometres an hour. With sensors and cameras it 'sees' the pedestrians, bicycles and cars around it and stops by itself if something gets in front of it."),
  L("Εκφωνητής", "m", "Για λόγους ασφαλείας, τους πρώτους τρεις μήνες θα υπάρχει πάντα μέσα ένας υπάλληλος του δήμου, που θα μπορεί να το σταματήσει με ένα κουμπί. Η διαδρομή θα είναι δωρεάν, και οι επιβάτες θα καλούνται να συμπληρώνουν ένα σύντομο ερωτηματολόγιο για την εμπειρία τους.", "For safety reasons, for the first three months there will always be a municipal employee on board who can stop it with a button. The ride will be free, and passengers will be asked to fill in a short questionnaire about their experience."),
  L("Εκφωνητής", "m", "Οι επαγγελματίες ταξί της πόλης εξέφρασαν ανησυχίες για το μέλλον της δουλειάς τους. Ο δήμαρχος απάντησε ότι πρόκειται για ένα πείραμα και ότι κάθε απόφαση θα παρθεί μετά τη δοκιμαστική περίοδο, λαμβάνοντας υπόψη τη γνώμη των κατοίκων.", "The city's taxi drivers expressed concerns about the future of their work. The mayor replied that it is an experiment and that any decision will be taken after the trial period, taking residents' views into account."),
 ],
 "questions": [
  Q("Πού θα κινείται το λεωφορείο;", ["Στο κέντρο της πόλης", "Από το λιμάνι ως το δημοτικό κολυμβητήριο", "Από το αεροδρόμιο ως το λιμάνι", "Σε όλες τις γειτονιές"], 1, "σε μια διαδρομή δύο χιλιομέτρων, από το λιμάνι ως το δημοτικό κολυμβητήριο"),
  Q("Τι κάνει το λεωφορείο αν κάτι βρεθεί μπροστά του;", ["Κορνάρει", "Αλλάζει διαδρομή", "Σταματά μόνο του", "Καλεί τον οδηγό"], 2, "σταματά μόνο του, αν κάτι βρεθεί μπροστά του"),
  Q("Ποιος θα βρίσκεται μέσα τους πρώτους τρεις μήνες;", ["Ένας αστυνομικός", "Ένας υπάλληλος του δήμου", "Ένας μηχανικός της εταιρείας", "Κανείς"], 1, "θα υπάρχει πάντα μέσα ένας υπάλληλος του δήμου"),
  Q("Τι απάντησε ο δήμαρχος στους οδηγούς ταξί;", ["Ότι τα ταξί θα καταργηθούν", "Ότι πρόκειται για πείραμα και η απόφαση θα παρθεί αργότερα", "Ότι θα τους δώσει αποζημίωση", "Ότι το λεωφορείο θα σταματήσει αμέσως"], 1, "πρόκειται για ένα πείραμα και ότι κάθε απόφαση θα παρθεί μετά τη δοκιμαστική περίοδο"),
 ],
 "gloss": {"δοκιμαστικά": "δοκιμαστικός — trial, test", "δρομολόγια": "δρομολόγιο — (scheduled) service, route", "παραλιακή": "παραλιακός — seafront", "αισθητήρες": "αισθητήρας — sensor", "πεζούς": "πεζός — pedestrian", "ερωτηματολόγιο": "ερωτηματολόγιο — questionnaire", "εξέφρασαν": "εκφράζω — to express", "ανησυχίες": "ανησυχία — concern", "λαμβάνοντας υπόψη": "λαμβάνω υπόψη — to take into account"},
})
ITEMS.append({
 "id": "l233-vm-vintekasetes", "title": "Μήνυμα για τις παλιές βιντεοκασέτες", "title_en": "A message about the old videotapes", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δώσει σε ένα κατάστημα τις παλιές οικογενειακές βιντεοκασέτες σας για να τις μεταφέρουν σε ψηφιακή μορφή. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Τεχνικός", "m", "Γεια σας, είμαι ο Άρης από το φωτογραφείο στην Αγίου Νικολάου, για τις δεκατέσσερις βιντεοκασέτες που μας φέρατε την περασμένη εβδομάδα. Τις έχω ελέγξει όλες και θέλω να σας πω πώς πάμε.", "Hello, it's Aris from the photo shop on Agiou Nikolaou Street, about the fourteen videotapes you brought us last week. I've checked them all and I want to tell you how things stand."),
  L("Τεχνικός", "m", "Οι δώδεκα είναι σε καλή κατάσταση και έχουν ήδη περαστεί. Δύο όμως έχουν πρόβλημα. Η μία, αυτή που γράφει «Βάφτιση 1994», έχει μούχλα στην ταινία, γιατί μάλλον φυλαγόταν σε υγρό μέρος. Μπορώ να την καθαρίσω, αλλά υπάρχει ένας μικρός κίνδυνος να χαθούν μερικά λεπτά από την αρχή.", "Twelve are in good condition and have already been transferred. Two, however, have a problem. One, the one that says 'Christening 1994', has mould on the tape, probably because it was kept somewhere damp. I can clean it, but there's a small risk that a few minutes at the start will be lost."),
  L("Τεχνικός", "m", "Η άλλη έχει κοπεί στη μέση. Αυτή μπορώ να την κολλήσω χωρίς να χαθεί σχεδόν τίποτα. Το καθάρισμα και η επισκευή κοστίζουν δέκα ευρώ η καθεμία, εκτός από την τιμή που συμφωνήσαμε.", "The other has snapped in the middle. That one I can splice without losing almost anything. The cleaning and the repair cost ten euros each, on top of the price we agreed."),
  L("Τεχνικός", "m", "Πείτε μου αν θέλετε να προχωρήσω. Τα αρχεία θα σας τα δώσω σε ένα στικάκι, αλλά αν θέλετε, μπορώ να τα ανεβάσω και σε έναν σύνδεσμο για να τα στείλετε στους συγγενείς σας. Τα λέμε!", "Let me know if you want me to go ahead. I'll give you the files on a USB stick, but if you like, I can also upload them to a link so you can send them to your relatives. Speak soon!"),
 ],
 "questions": [
  Q("Πόσες κασέτες έχουν ήδη μεταφερθεί;", ["Δεκατέσσερις", "Δώδεκα", "Δύο", "Καμία"], 1, "Οι δώδεκα είναι σε καλή κατάσταση και έχουν ήδη περαστεί"),
  Q("Ποιο είναι το πρόβλημα της κασέτας «Βάφτιση 1994»;", ["Έχει κοπεί στη μέση", "Έχει μούχλα στην ταινία", "Λείπει η ετικέτα", "Είναι άδεια"], 1, "έχει μούχλα στην ταινία"),
  Q("Τι κίνδυνος υπάρχει αν την καθαρίσει;", ["Να χαλάσει το μηχάνημα", "Να χαθούν μερικά λεπτά από την αρχή", "Να χαθεί όλη η κασέτα", "Να χαθεί ο ήχος"], 1, "υπάρχει ένας μικρός κίνδυνος να χαθούν μερικά λεπτά από την αρχή"),
  Q("Τι προτείνει για τα αρχεία, εκτός από το στικάκι;", ["Να τα γράψει σε DVD", "Να τα ανεβάσει σε έναν σύνδεσμο", "Να τα τυπώσει", "Να τα στείλει με το ταχυδρομείο"], 1, "μπορώ να τα ανεβάσω και σε έναν σύνδεσμο"),
 ],
 "gloss": {"βιντεοκασέτες": "βιντεοκασέτα — videotape", "ψηφιακή μορφή": "ψηφιακή μορφή — digital format", "περαστεί": "περνιέμαι — to be transferred (colloquial)", "Βάφτιση": "βάφτιση — christening", "μούχλα": "μούχλα — mould", "υγρό": "υγρός — damp", "κοπεί": "κόβομαι — to be cut, snap", "κολλήσω": "κολλάω — to stick, splice", "στικάκι": "στικάκι — USB stick", "σύνδεσμο": "σύνδεσμος — link", "συγγενείς": "συγγενής — relative"},
})
ITEMS.append({
 "id": "l233-c1-mono-fermouar", "title": "Η μακριά ιστορία του φερμουάρ", "title_en": "The long history of the zip", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια εκπομπή για την ιστορία των καθημερινών αντικειμένων.",
 "script": [
  L("Ομιλητής", "m", "Το ανοίγουμε και το κλείνουμε δεκάδες φορές την ημέρα, χωρίς να το σκεφτόμαστε. Κι όμως, το φερμουάρ χρειάστηκε σχεδόν τριάντα χρόνια για να γίνει αξιόπιστο, και άλλα τόσα για να το εμπιστευτούν οι ράφτες.", "We open and close it dozens of times a day without thinking about it. And yet the zip needed almost thirty years to become reliable, and as many again for tailors to trust it."),
  L("Ομιλητής", "m", "Η πρώτη εκδοχή που είχε κάποια εμπορική τύχη παρουσιάστηκε στις Ηνωμένες Πολιτείες στις αρχές της δεκαετίας του 1890, από έναν εφευρέτη που ήθελε να γλιτώσει τον κόσμο από τα ατελείωτα κορδόνια των μποτών. Ο μηχανισμός του όμως άνοιγε μόνος του την πιο ακατάλληλη στιγμή, και οι πελάτες δεν πείστηκαν.", "The first version that had some commercial success was presented in the United States in the early 1890s, by an inventor who wanted to spare people the endless laces of boots. His mechanism, however, came open by itself at the worst possible moment, and customers weren't convinced."),
  L("Ομιλητής", "m", "Τη λύση έδωσε το 1913 ένας Σουηδός μηχανικός που ζούσε στην Αμερική. Αντί για γάντζους, χρησιμοποίησε μικρά δοντάκια που κουμπώνουν το ένα μέσα στο άλλο, σχεδόν όπως τα σημερινά. Το όνομα «zipper» ήρθε λίγο αργότερα από μια εταιρεία που το έβαλε σε λαστιχένιες μπότες, μιμούμενη τον ήχο που κάνει όταν κλείνει. Στα ελληνικά, αντίθετα, κρατήσαμε τη γαλλική λέξη.", "The solution came in 1913 from a Swedish engineer living in America. Instead of hooks, he used small teeth that lock into one another, almost like today's. The name 'zipper' came a little later from a company that put it on rubber boots, imitating the sound it makes when it closes. In Greek, by contrast, we kept the French word."),
  L("Ομιλητής", "m", "Για χρόνια οι σοβαροί ράφτες το θεωρούσαν φθηνό τέχνασμα, κατάλληλο για τσάντες και μπότες αλλά όχι για ένα καλό παντελόνι. Χρειάστηκε η μόδα του μεσοπολέμου για να αλλάξει η εικόνα του. Η ιστορία του φερμουάρ θυμίζει ότι μια εφεύρεση δεν αρκεί να λειτουργεί· πρέπει και να γίνει αποδεκτή.", "For years serious tailors considered it a cheap gimmick, suitable for bags and boots but not for a good pair of trousers. It took interwar fashion to change its image. The history of the zip is a reminder that it's not enough for an invention to work; it also has to be accepted."),
 ],
 "questions": [
  Q("Τι ήθελε να πετύχει ο πρώτος εφευρέτης;", ["Να κάνει πιο φθηνά τα ρούχα", "Να γλιτώσει τον κόσμο από τα κορδόνια των μποτών", "Να κλείνουν καλύτερα οι τσάντες", "Να αντικαταστήσει τα κουμπιά στα πουκάμισα"], 1, "ήθελε να γλιτώσει τον κόσμο από τα ατελείωτα κορδόνια των μποτών"),
  Q("Ποιο ήταν το πρόβλημα της πρώτης εκδοχής;", ["Ήταν πολύ ακριβή", "Άνοιγε μόνη της την πιο ακατάλληλη στιγμή", "Ήταν πολύ βαριά", "Σκούριαζε γρήγορα"], 1, "άνοιγε μόνος του την πιο ακατάλληλη στιγμή"),
  Q("Από πού προέρχεται το αγγλικό όνομα «zipper»;", ["Από το όνομα του εφευρέτη", "Από μια γαλλική λέξη", "Από τον ήχο που κάνει όταν κλείνει", "Από μια πόλη της Σουηδίας"], 2, "μιμούμενη τον ήχο που κάνει όταν κλείνει"),
  Q("Ποιο συμπέρασμα βγάζει ο ομιλητής;", ["Ότι οι ράφτες είχαν δίκιο", "Ότι μια εφεύρεση πρέπει όχι μόνο να λειτουργεί αλλά και να γίνει αποδεκτή", "Ότι οι Σουηδοί είναι οι καλύτεροι μηχανικοί", "Ότι το φερμουάρ θα αντικατασταθεί σύντομα"], 1, "μια εφεύρεση δεν αρκεί να λειτουργεί· πρέπει και να γίνει αποδεκτή"),
 ],
 "gloss": {"φερμουάρ": "φερμουάρ — zip, zipper", "αξιόπιστο": "αξιόπιστος — reliable", "εκδοχή": "εκδοχή — version", "εφευρέτη": "εφευρέτης — inventor", "γλιτώσει": "γλιτώνω — to spare, save", "ακατάλληλη": "ακατάλληλος — unsuitable", "γάντζους": "γάντζος — hook", "κουμπώνουν": "κουμπώνω — to fasten, lock together", "μιμούμενη": "μιμούμενος — imitating", "τέχνασμα": "τέχνασμα — gimmick, trick", "μεσοπολέμου": "μεσοπόλεμος — the interwar period", "αποδεκτή": "αποδεκτός — accepted"},
})
ITEMS.append({
 "id": "l233-c1-int-thorybos-thalassa", "title": "Μια βιολόγος για τον θόρυβο κάτω από τη θάλασσα", "title_en": "A biologist on noise under the sea", "type": "interview", "level": "C1",
 "context_el": "Μια βιολόγος που μελετά τα κητώδη μιλά σε μια ραδιοφωνική εκπομπή για την ηχορρύπανση στις ελληνικές θάλασσες.",
 "script": [
  L("Δημοσιογράφος", "m", "Όταν ακούμε για ρύπανση της θάλασσας, σκεφτόμαστε πλαστικά και πετρέλαιο. Εσείς μιλάτε για θόρυβο. Τι εννοείτε;", "When we hear about sea pollution, we think of plastics and oil. You talk about noise. What do you mean?"),
  L("Βιολόγος", "f", "Ο ήχος ταξιδεύει στο νερό πολύ πιο γρήγορα και πολύ πιο μακριά από ό,τι στον αέρα. Για τις φάλαινες και τα δελφίνια, η ακοή είναι ό,τι είναι για εμάς η όραση: μ' αυτήν βρίσκουν τροφή, προσανατολίζονται και επικοινωνούν. Οι έλικες των πλοίων, οι σεισμικές έρευνες για υδρογονάνθρακες και τα στρατιωτικά σόναρ γεμίζουν αυτόν τον κόσμο με ένα συνεχές βουητό.", "Sound travels much faster and much further in water than in air. For whales and dolphins, hearing is what sight is for us: with it they find food, find their way and communicate. Ships' propellers, seismic surveys for hydrocarbons and military sonar fill that world with a constant hum."),
  L("Δημοσιογράφος", "m", "Υπάρχουν αποδείξεις ότι αυτό τους κάνει κακό;", "Is there evidence that this harms them?"),
  L("Βιολόγος", "f", "Η πιο γνωστή περίπτωση έγινε στον Κυπαρισσιακό κόλπο το 1996, όταν δώδεκα ζιφιοί, ένα είδος φάλαινας που καταδύεται πολύ βαθιά, βγήκαν νεκροί ή ετοιμοθάνατοι στις ακτές. Η χρονική σύμπτωση με μια άσκηση στρατιωτικού σόναρ στην περιοχή καταγράφηκε σε επιστημονική δημοσίευση, και από τότε παρόμοια περιστατικά έχουν συνδεθεί με σόναρ σε διάφορα μέρη του κόσμου. Ο συνεχής θόρυβος της ναυσιπλοΐας είναι λιγότερο θεαματικός, αλλά μπορεί να αναγκάζει τα ζώα να εγκαταλείπουν περιοχές όπου τρέφονται.", "The best-known case happened in the Gulf of Kyparissia in 1996, when twelve Cuvier's beaked whales, a species of whale that dives very deep, came ashore dead or dying. The coincidence in time with a military sonar exercise in the area was recorded in a scientific publication, and since then similar incidents have been linked to sonar in various parts of the world. The constant noise of shipping is less spectacular, but it can force animals to abandon areas where they feed."),
  L("Δημοσιογράφος", "m", "Μπορούμε να κάνουμε κάτι;", "Can we do anything?"),
  L("Βιολόγος", "f", "Ευτυχώς, ο θόρυβος έχει ένα πλεονέκτημα σε σχέση με άλλους ρύπους: μόλις σταματήσει η πηγή, εξαφανίζεται. Όταν τα πλοία μειώνουν λίγο την ταχύτητά τους, ο θόρυβος μειώνεται αισθητά, και καταναλώνουν και λιγότερα καύσιμα. Αν προσθέσουμε και μικρές αλλαγές στις θαλάσσιες διαδρομές, μακριά από τις περιοχές όπου ζουν οι φυσητήρες, θα έχουμε κάνει ήδη πολλά με μικρό κόστος.", "Fortunately, noise has an advantage over other pollutants: as soon as the source stops, it disappears. When ships reduce their speed a little, the noise drops noticeably, and they also use less fuel. If we add small changes to shipping routes, away from the areas where sperm whales live, we'll already have done a lot at little cost."),
 ],
 "questions": [
  Q("Γιατί ο θόρυβος είναι τόσο σημαντικός για τα κητώδη;", ["Γιατί τα τρομάζει μόνο τη νύχτα", "Γιατί η ακοή είναι γι' αυτά ό,τι η όραση για εμάς", "Γιατί δεν βλέπουν καθόλου", "Γιατί ζουν μόνο κοντά στις ακτές"], 1, "η ακοή είναι ό,τι είναι για εμάς η όραση"),
  Q("Τι συνέβη στον Κυπαρισσιακό κόλπο το 1996;", ["Βυθίστηκε ένα πλοίο", "Δώδεκα ζιφιοί βγήκαν νεκροί ή ετοιμοθάνατοι στις ακτές", "Έγινε ένας μεγάλος σεισμός", "Ανακαλύφθηκε ένα νέο είδος δελφινιού"], 1, "δώδεκα ζιφιοί … βγήκαν νεκροί ή ετοιμοθάνατοι στις ακτές"),
  Q("Τι λέει η βιολόγος για τον θόρυβο της ναυσιπλοΐας;", ["Ότι δεν επηρεάζει τα ζώα", "Ότι μπορεί να αναγκάζει τα ζώα να εγκαταλείπουν περιοχές όπου τρέφονται", "Ότι είναι πιο επικίνδυνος από το σόναρ", "Ότι ακούγεται μόνο κοντά στα λιμάνια"], 1, "μπορεί να αναγκάζει τα ζώα να εγκαταλείπουν περιοχές όπου τρέφονται"),
  Q("Ποιο πλεονέκτημα έχει ο θόρυβος σε σχέση με άλλους ρύπους;", ["Είναι φθηνότερο να μετρηθεί", "Εξαφανίζεται μόλις σταματήσει η πηγή", "Δεν φτάνει σε μεγάλο βάθος", "Το νερό τον απορροφά αμέσως"], 1, "μόλις σταματήσει η πηγή, εξαφανίζεται"),
 ],
 "gloss": {"κητώδη": "κητώδη — cetaceans", "ηχορρύπανση": "ηχορρύπανση — noise pollution", "προσανατολίζονται": "προσανατολίζομαι — to find one's way, orient oneself", "έλικες": "έλικας — propeller", "υδρογονάνθρακες": "υδρογονάνθρακας — hydrocarbon", "σόναρ": "σόναρ — sonar", "βουητό": "βουητό — hum, drone", "ζιφιοί": "ζιφιός — Cuvier's beaked whale", "ετοιμοθάνατοι": "ετοιμοθάνατος — dying", "σύμπτωση": "σύμπτωση — coincidence", "ναυσιπλοΐας": "ναυσιπλοΐα — shipping, navigation", "ρύπους": "ρύπος — pollutant", "φυσητήρες": "φυσητήρας — sperm whale"},
})
rnd = random.Random(233)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-233.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
