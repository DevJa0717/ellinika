# Source for library/listening/listening-135.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l135.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l135-ann-antallagi", "title": "Γιορτή ανταλλαγής ρούχων στη δημοτική βιβλιοθήκη", "title_en": "A clothes-swap party at the municipal library", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε στο τοπικό ραδιόφωνο μια ανακοίνωση για μια εκδήλωση της γειτονιάς.",
 "script": [
  L("Εκφωνητής", "m", "Η δημοτική βιβλιοθήκη και η ομάδα εθελοντών «Δεύτερη Ζωή» διοργανώνουν την Κυριακή, από τις έντεκα το πρωί έως τις τέσσερις το απόγευμα, μια γιορτή ανταλλαγής ρούχων στην αυλή της βιβλιοθήκης.", "The municipal library and the volunteer group 'Second Life' are organising a clothes-swap party in the library courtyard on Sunday, from eleven in the morning to four in the afternoon."),
  L("Εκφωνητής", "m", "Ο κάθε επισκέπτης μπορεί να φέρει έως δέκα ρούχα ή αξεσουάρ, καθαρά και σε καλή κατάσταση, και να πάρει τον ίδιο αριθμό κομματιών. Δεν γίνονται δεκτά εσώρουχα ούτε παπούτσια.", "Each visitor can bring up to ten items of clothing or accessories, clean and in good condition, and take the same number of pieces. Underwear and shoes are not accepted."),
  L("Εκφωνητής", "m", "Ό,τι περισσέψει στο τέλος της ημέρας θα δοθεί στο κοινωνικό παντοπωλείο του δήμου. Κατά τη διάρκεια της εκδήλωσης, μια μοδίστρα θα δείχνει δωρεάν πώς να κάνει κανείς μικρές μεταποιήσεις και επιδιορθώσεις.", "Whatever is left over at the end of the day will be given to the municipality's social grocery. During the event, a dressmaker will show, free of charge, how to do small alterations and repairs."),
 ],
 "questions": [
  Q("Πόσα ρούχα μπορεί να φέρει ο κάθε επισκέπτης;", ["Όσα θέλει", "Έως πέντε", "Έως δέκα", "Μόνο ένα"], 2, "Ο κάθε επισκέπτης μπορεί να φέρει έως δέκα ρούχα ή αξεσουάρ"),
  Q("Τι δεν γίνεται δεκτό;", ["Εσώρουχα και παπούτσια", "Παιδικά ρούχα", "Τσάντες και καπέλα", "Χειμωνιάτικα παλτά"], 0, "Δεν γίνονται δεκτά εσώρουχα ούτε παπούτσια"),
  Q("Τι θα γίνει με τα ρούχα που θα περισσέψουν;", ["Θα πουληθούν σε παζάρι", "Θα ανακυκλωθούν", "Θα επιστραφούν στους κατόχους τους", "Θα δοθούν στο κοινωνικό παντοπωλείο του δήμου"], 3, "Ό,τι περισσέψει στο τέλος της ημέρας θα δοθεί στο κοινωνικό παντοπωλείο του δήμου"),
 ],
 "gloss": {"ανταλλαγής": "ανταλλαγή — exchange, swap", "εθελοντών": "εθελοντής — volunteer", "διοργανώνουν": "διοργανώνω — to organise", "αυλή": "αυλή — courtyard", "αξεσουάρ": "αξεσουάρ — accessory", "κομματιών": "κομμάτι — piece", "γίνονται δεκτά": "γίνομαι δεκτός — to be accepted", "εσώρουχα": "εσώρουχο — underwear", "περισσέψει": "περισσεύω — to be left over", "κοινωνικό παντοπωλείο": "κοινωνικό παντοπωλείο — social grocery (food bank)", "μοδίστρα": "μοδίστρα — dressmaker", "μεταποιήσεις": "μεταποίηση — alteration", "επιδιορθώσεις": "επιδιόρθωση — repair, mending"}
})

ITEMS.append({
 "id": "l135-vm-kounavi", "title": "Ένα κουνάβι στη σοφίτα", "title_en": "A stone marten in the attic", "type": "voicemail", "level": "B2",
 "context_el": "Ακούγατε θορύβους στη σοφίτα του σπιτιού σας τη νύχτα και καλέσατε μια εταιρεία. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Τεχνικός", "m", "Καλησπέρα, είμαι ο Στάθης από την εταιρεία που ήρθε χθες στο σπίτι σας. Κοίταξα τις φωτογραφίες από τη σοφίτα και, όπως υποψιαζόμουν, δεν πρόκειται για ποντίκια. Τα ίχνη και οι μασημένες μονώσεις δείχνουν ότι έχει κάνει φωλιά ένα κουνάβι.", "Good evening, this is Stathis from the company that came to your house yesterday. I looked at the photos from the attic and, as I suspected, it isn't mice. The tracks and the chewed insulation show that a stone marten has made a nest."),
  L("Τεχνικός", "m", "Να ξέρετε ότι τα κουνάβια δεν τα σκοτώνουμε ούτε τα δηλητηριάζουμε. Αυτό που κάνουμε είναι να βρούμε από πού μπαίνει, συνήθως από ένα κενό κάτω από τα κεραμίδια, και να το κλείσουμε τη νύχτα, όταν έχει βγει για κυνήγι.", "You should know that we don't kill or poison martens. What we do is find where it gets in, usually through a gap under the roof tiles, and close it at night, when it has gone out hunting."),
  L("Τεχνικός", "m", "Μέχρι τότε, σας συμβουλεύω να μην αφήνετε το αυτοκίνητο κάτω από το δέντρο της αυλής, γιατί τα κουνάβια πολλές φορές μασάνε τα καλώδια της μηχανής. Πάρτε με, να κλείσουμε μέρα. Ευχαριστώ.", "Until then, I advise you not to leave the car under the tree in the yard, because martens often chew engine cables. Call me so we can fix a day. Thank you."),
 ],
 "questions": [
  Q("Τι προκαλεί τους θορύβους, σύμφωνα με τον τεχνικό;", ["Ποντίκια", "Ένα κουνάβι", "Μια κουκουβάγια", "Μια γάτα του γείτονα"], 1, "έχει κάνει φωλιά ένα κουνάβι"),
  Q("Πώς σκοπεύει να λύσει το πρόβλημα;", ["Με δηλητήριο", "Με μια παγίδα με δόλωμα", "Κλείνοντας το σημείο από όπου μπαίνει το ζώο, όταν έχει βγει", "Με μια συσκευή που κάνει θόρυβο"], 2, "να βρούμε από πού μπαίνει, συνήθως από ένα κενό κάτω από τα κεραμίδια, και να το κλείσουμε τη νύχτα, όταν έχει βγει για κυνήγι"),
  Q("Τι συμβουλεύει μέχρι τότε;", ["Να μην αφήνετε το αυτοκίνητο κάτω από το δέντρο της αυλής", "Να μην ανεβαίνετε στη σοφίτα", "Να κρατάτε το φως αναμμένο", "Να κλείνετε τα παράθυρα"], 0, "να μην αφήνετε το αυτοκίνητο κάτω από το δέντρο της αυλής"),
 ],
 "gloss": {"σοφίτα": "σοφίτα — attic", "υποψιαζόμουν": "υποψιάζομαι — to suspect", "ίχνη": "ίχνος — track, trace", "μασημένες": "μασημένος — chewed", "μονώσεις": "μόνωση — insulation", "φωλιά": "φωλιά — nest, den", "κουνάβι": "κουνάβι — stone marten", "δηλητηριάζουμε": "δηλητηριάζω — to poison", "κενό": "κενό — gap", "κεραμίδια": "κεραμίδι — roof tile", "κυνήγι": "κυνήγι — hunting", "καλώδια": "καλώδιο — cable", "κλείσουμε μέρα": "κλείνω μέρα — to fix a date"}
})

ITEMS.append({
 "id": "l135-dia-ypnovasia", "title": "Ο μικρός υπνοβατεί", "title_en": "The little one sleepwalks", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλες να συζητούν στο τηλέφωνο.",
 "script": [
  L("Δανάη", "f", "Δεν θα το πιστέψεις. Χθες στις δύο τα ξημερώματα βρήκα τον Άρη στην κουζίνα να ανοίγει το ψυγείο, με τα μάτια ανοιχτά. Του μίλησα και δεν μου απάντησε. Το πρωί δεν θυμόταν τίποτα.", "You won't believe it. Yesterday at two in the morning I found Aris in the kitchen opening the fridge, with his eyes open. I spoke to him and he didn't answer. In the morning he didn't remember anything."),
  L("Ρένα", "f", "Υπνοβασία. Το έπαθε κι η αδερφή μου μικρή. Η παιδίατρος μάς είχε πει ότι είναι αρκετά συνηθισμένο σε αυτή την ηλικία και συνήθως περνάει μόνο του όσο μεγαλώνει το παιδί. Μην τον ξυπνήσεις απότομα, απλώς οδήγησέ τον ήρεμα πίσω στο κρεβάτι.", "Sleepwalking. My sister had it when she was little. The paediatrician told us it's quite common at that age and usually passes by itself as the child grows. Don't wake him abruptly, just lead him calmly back to bed."),
  L("Δανάη", "f", "Κι αν ανοίξει την πόρτα και βγει στη σκάλα;", "And what if he opens the door and goes out onto the stairs?"),
  L("Ρένα", "f", "Εμείς βάζαμε ένα κουδουνάκι στην πόρτα του δωματίου, για να ακούμε όταν σηκώνεται. Και πρόσεξε να κοιμάται αρκετά, γιατί η κούραση το χειροτερεύει. Αν πάντως συμβαίνει συχνά, να το πεις στον γιατρό.", "We used to put a little bell on the bedroom door, so we'd hear when she got up. And make sure he sleeps enough, because tiredness makes it worse. Anyway, if it happens often, tell the doctor."),
 ],
 "questions": [
  Q("Τι έκανε ο Άρης στις δύο τα ξημερώματα;", ["Έκλαιγε στο κρεβάτι του", "Έβλεπε τηλεόραση", "Άνοιγε το ψυγείο με τα μάτια ανοιχτά", "Έπαιζε στο μπαλκόνι"], 2, "βρήκα τον Άρη στην κουζίνα να ανοίγει το ψυγείο, με τα μάτια ανοιχτά"),
  Q("Τι συμβουλεύει η Ρένα να κάνει η Δανάη, όταν τον βρει;", ["Να τον οδηγήσει ήρεμα πίσω στο κρεβάτι", "Να τον ξυπνήσει αμέσως", "Να του δώσει νερό", "Να τον αφήσει να κάνει ό,τι θέλει"], 0, "απλώς οδήγησέ τον ήρεμα πίσω στο κρεβάτι"),
  Q("Γιατί έβαζαν κουδουνάκι στην πόρτα;", ["Για να ξυπνάει το παιδί", "Για να ακούν όταν σηκώνεται", "Για να μη φοβάται το σκοτάδι", "Γιατί του το είπε η παιδίατρος"], 1, "για να ακούμε όταν σηκώνεται"),
 ],
 "gloss": {"ξημερώματα": "ξημερώματα — small hours", "Υπνοβασία": "υπνοβασία — sleepwalking", "παιδίατρος": "παιδίατρος — paediatrician", "συνηθισμένο": "συνηθισμένος — common", "απότομα": "απότομα — abruptly", "οδήγησέ": "οδηγώ — to lead", "κουδουνάκι": "κουδουνάκι — little bell", "κούραση": "κούραση — tiredness", "χειροτερεύει": "χειροτερεύω — to make worse"}
})

ITEMS.append({
 "id": "l135-int-rymoulko", "title": "Καπετάνισσα σε ρυμουλκό", "title_en": "A woman captain on a tugboat", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική εκπομπή για επαγγέλματα της θάλασσας.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνει ένα ρυμουλκό στο λιμάνι;", "What exactly does a tugboat do in the port?"),
  L("Καπετάνισσα", "f", "Τα μεγάλα πλοία, τα δεξαμενόπλοια, τα κρουαζιερόπλοια, δεν μπορούν να κάνουν μόνα τους ελιγμούς σε στενό χώρο. Εμείς τα σπρώχνουμε ή τα τραβάμε με σκοινιά, για να δέσουν με ασφάλεια. Είναι σαν να παρκάρεις μια πολυκατοικία με ένα μικρό αυτοκίνητο.", "Big ships, tankers, cruise ships, can't manoeuvre on their own in a tight space. We push them or pull them with ropes so they can berth safely. It's like parking a block of flats with a small car."),
  L("Δημοσιογράφος", "m", "Και πώς είναι να είσαι γυναίκα σε αυτή τη δουλειά;", "And what's it like being a woman in this job?"),
  L("Καπετάνισσα", "f", "Στην αρχή κάποιοι πλοίαρχοι ζητούσαν να μιλήσουν «με τον καπετάνιο». Τώρα με ξέρουν. Το δύσκολο δεν είναι αυτό, είναι οι βάρδιες: δουλεύουμε εικοσιτετράωρα, και όταν έχει νοτιά, κανείς δεν κοιμάται. Η μεγαλύτερη ικανοποίηση είναι όταν δένει ένα πλοίο χωρίς ούτε μια γρατζουνιά.", "At first some masters asked to speak 'to the captain'. Now they know me. That's not the hard part; it's the shifts: we work twenty-four-hour shifts, and when there's a southerly wind, nobody sleeps. The greatest satisfaction is when a ship berths without a single scratch."),
 ],
 "questions": [
  Q("Τι κάνει ένα ρυμουλκό;", ["Μεταφέρει επιβάτες στα νησιά", "Καθαρίζει το νερό του λιμανιού", "Ψαρεύει στα ανοιχτά", "Σπρώχνει ή τραβά τα μεγάλα πλοία, για να δέσουν με ασφάλεια"], 3, "Εμείς τα σπρώχνουμε ή τα τραβάμε με σκοινιά, για να δέσουν με ασφάλεια"),
  Q("Τι συνέβαινε στην αρχή της καριέρας της;", ["Κάποιοι πλοίαρχοι ζητούσαν να μιλήσουν «με τον καπετάνιο»", "Δεν έβρισκε δουλειά", "Φοβόταν τη θάλασσα", "Δούλευε μόνο τη μέρα"], 0, "Στην αρχή κάποιοι πλοίαρχοι ζητούσαν να μιλήσουν «με τον καπετάνιο»"),
  Q("Τι θεωρεί πιο δύσκολο στη δουλειά της;", ["Τον χαμηλό μισθό", "Τις βάρδιες", "Τη σχέση με τους συναδέλφους", "Τα καινούργια μηχανήματα"], 1, "Το δύσκολο δεν είναι αυτό, είναι οι βάρδιες"),
 ],
 "gloss": {"ρυμουλκό": "ρυμουλκό — tugboat", "δεξαμενόπλοια": "δεξαμενόπλοιο — tanker", "κρουαζιερόπλοια": "κρουαζιερόπλοιο — cruise ship", "ελιγμούς": "ελιγμός — manoeuvre", "σκοινιά": "σκοινί — rope", "δέσουν": "δένω — to berth, moor", "πλοίαρχοι": "πλοίαρχος — ship's master", "βάρδιες": "βάρδια — shift", "νοτιά": "νοτιάς — southerly wind", "ικανοποίηση": "ικανοποίηση — satisfaction", "γρατζουνιά": "γρατζουνιά — scratch"}
})

ITEMS.append({
 "id": "l135-int-kamariera", "title": "Μια μέρα με μια καμαριέρα", "title_en": "A day with a hotel chambermaid", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από ρεπορτάζ για τους εργαζόμενους στον τουρισμό.",
 "script": [
  L("Δημοσιογράφος", "f", "Πόσα δωμάτια καθαρίζετε την ημέρα;", "How many rooms do you clean a day?"),
  L("Καμαριέρα", "f", "Τον Αύγουστο, γύρω στα δεκαπέντε με είκοσι. Σε κάθε αναχώρηση αλλάζουμε σεντόνια και πετσέτες, καθαρίζουμε το μπάνιο, ελέγχουμε το μίνι μπαρ. Έχουμε περίπου είκοσι λεπτά για κάθε δωμάτιο, οπότε δεν σταματάς καθόλου.", "In August, around fifteen to twenty. At every check-out we change sheets and towels, clean the bathroom, check the minibar. We have about twenty minutes per room, so you never stop."),
  L("Δημοσιογράφος", "f", "Τι είναι το πιο κουραστικό;", "What's the most tiring thing?"),
  L("Καμαριέρα", "f", "Η μέση. Σκύβεις συνέχεια, για να στρώσεις κρεβάτια. Γι' αυτό φέτος το ξενοδοχείο έφερε φυσιοθεραπεύτρια, που μας έδειξε πώς να κινούμαστε σωστά. Οι πελάτες δεν μας βλέπουν σχεδόν ποτέ, αλλά μερικοί αφήνουν ένα σημείωμα στο τέλος: «Ευχαριστούμε». Αυτό μου φτιάχνει τη μέρα.", "My back. You bend all the time to make beds. That's why this year the hotel brought in a physiotherapist who showed us how to move properly. Guests almost never see us, but some leave a note at the end: 'Thank you'. That makes my day."),
 ],
 "questions": [
  Q("Πόσο χρόνο έχει περίπου για κάθε δωμάτιο;", ["Πέντε λεπτά", "Μία ώρα", "Είκοσι λεπτά", "Όσο χρειάζεται"], 2, "Έχουμε περίπου είκοσι λεπτά για κάθε δωμάτιο"),
  Q("Τι έκανε φέτος το ξενοδοχείο;", ["Έφερε φυσιοθεραπεύτρια να τους δείξει πώς να κινούνται σωστά", "Προσέλαβε περισσότερο προσωπικό", "Αύξησε τους μισθούς", "Αγόρασε καινούργια κρεβάτια"], 0, "το ξενοδοχείο έφερε φυσιοθεραπεύτρια, που μας έδειξε πώς να κινούμαστε σωστά"),
  Q("Τι της «φτιάχνει τη μέρα»;", ["Τα φιλοδωρήματα", "Ένα σημείωμα που λέει «Ευχαριστούμε»", "Τα μεγάλα διαλείμματα", "Οι κουβέντες με τους πελάτες"], 1, "μερικοί αφήνουν ένα σημείωμα στο τέλος: «Ευχαριστούμε». Αυτό μου φτιάχνει τη μέρα"),
 ],
 "gloss": {"αναχώρηση": "αναχώρηση — departure, check-out", "σεντόνια": "σεντόνι — sheet", "πετσέτες": "πετσέτα — towel", "κουραστικό": "κουραστικός — tiring", "μέση": "μέση — lower back, waist", "Σκύβεις": "σκύβω — to bend down", "στρώσεις": "στρώνω — to make (a bed)", "φυσιοθεραπεύτρια": "φυσιοθεραπεύτρια — physiotherapist", "σημείωμα": "σημείωμα — note", "φτιάχνει τη μέρα": "μου φτιάχνει τη μέρα — makes my day"}
})

ITEMS.append({
 "id": "l135-news-paschalitses", "title": "Πασχαλίτσες αντί για φάρμακα", "title_en": "Ladybirds instead of pesticides", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις τοπικές ειδήσεις.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε ένα θερμοκήπιο με πιπεριές έξω από την πόλη, ένας νεαρός αγρότης δοκιμάζει φέτος κάτι διαφορετικό: αντί να ψεκάζει με φυτοφάρμακα για τις αφίδες, αφήνει ελεύθερες χιλιάδες πασχαλίτσες.", "In a pepper greenhouse outside the town, a young farmer is trying something different this year: instead of spraying pesticides against aphids, he releases thousands of ladybirds."),
  L("Ρεπόρτερ", "m", "Μια πασχαλίτσα μπορεί να φάει δεκάδες αφίδες την ημέρα, και οι προνύμφες της είναι ακόμη πιο αδηφάγες. Ο αγρότης αγοράζει τα έντομα από ειδική εταιρεία, και λέει ότι το κόστος είναι περίπου ίδιο με των φαρμάκων.", "A ladybird can eat dozens of aphids a day, and its larvae are even more voracious. The farmer buys the insects from a specialist company and says the cost is about the same as for the chemicals."),
  L("Ρεπόρτερ", "m", "Το μεγάλο κέρδος, όπως λέει, είναι ότι μπορεί να πουλάει τις πιπεριές σε αγορές που ζητούν προϊόντα χωρίς υπολείμματα φυτοφαρμάκων. Η μόνη δυσκολία; Τα πρώτα βράδια, πολλές πασχαλίτσες προσπαθούσαν να φύγουν από τις χαραμάδες.", "The big gain, he says, is that he can sell the peppers in markets that want products without pesticide residues. The only difficulty? On the first evenings, many ladybirds tried to escape through the cracks."),
 ],
 "questions": [
  Q("Τι δοκιμάζει ο αγρότης;", ["Να καλλιεργεί χωρίς νερό", "Να αφήνει ελεύθερες πασχαλίτσες αντί να ψεκάζει", "Να φυτεύει ντομάτες αντί για πιπεριές", "Να χρησιμοποιεί drones"], 1, "αντί να ψεκάζει με φυτοφάρμακα για τις αφίδες, αφήνει ελεύθερες χιλιάδες πασχαλίτσες"),
  Q("Πώς είναι το κόστος σε σύγκριση με τα φάρμακα;", ["Πολύ μεγαλύτερο", "Μηδενικό", "Περίπου ίδιο", "Το μισό"], 2, "το κόστος είναι περίπου ίδιο με των φαρμάκων"),
  Q("Ποιο είναι το μεγάλο κέρδος, σύμφωνα με τον αγρότη;", ["Μπορεί να πουλάει σε αγορές που ζητούν προϊόντα χωρίς υπολείμματα φυτοφαρμάκων", "Οι πιπεριές μεγαλώνουν πιο γρήγορα", "Παίρνει επιδότηση από το κράτος", "Δεν χρειάζεται εργάτες"], 0, "μπορεί να πουλάει τις πιπεριές σε αγορές που ζητούν προϊόντα χωρίς υπολείμματα φυτοφαρμάκων"),
 ],
 "gloss": {"πασχαλίτσες": "πασχαλίτσα — ladybird", "θερμοκήπιο": "θερμοκήπιο — greenhouse", "ψεκάζει": "ψεκάζω — to spray", "φυτοφάρμακα": "φυτοφάρμακο — pesticide", "αφίδες": "αφίδα — aphid", "προνύμφες": "προνύμφη — larva", "αδηφάγες": "αδηφάγος — voracious", "έντομα": "έντομο — insect", "υπολείμματα": "υπόλειμμα — residue", "χαραμάδες": "χαραμάδα — crack, chink"}
})

ITEMS.append({
 "id": "l135-int-radiofono", "title": "Το ραδιόφωνο της γειτονιάς", "title_en": "The neighbourhood radio station", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με τον ιδρυτή ενός κοινοτικού ραδιοφώνου.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς ξεκίνησε ο σταθμός σας;", "How did your station start?"),
  L("Ιδρυτής", "m", "Από ένα υπόγειο και έναν παλιό υπολογιστή. Εκπέμπουμε μόνο μέσω διαδικτύου, γιατί μια συχνότητα στα FM κοστίζει πολύ. Όλοι οι παραγωγοί είναι εθελοντές από τη γειτονιά: ένας συνταξιούχος ναυτικός παίζει ρεμπέτικα, δύο μαθήτριες κάνουν εκπομπή για βιβλία, ένας μάγειρας δίνει συνταγές ζωντανά.", "From a basement and an old computer. We broadcast only online, because an FM frequency costs a lot. All the presenters are volunteers from the neighbourhood: a retired sailor plays rebetiko, two schoolgirls do a show about books, a cook gives recipes live."),
  L("Δημοσιογράφος", "f", "Τι προσφέρει ένα τόσο μικρό ραδιόφωνο;", "What does such a small radio station offer?"),
  L("Ιδρυτής", "m", "Μιλάμε για πράγματα που δεν θα ακούσεις αλλού: πότε κλείνει ο δρόμος για έργα, ποιος φούρνος ανοίγει, ποια ηλικιωμένη χρειάζεται βοήθεια με τα ψώνια. Τώρα ψάχνουμε κάποιον να κάνει εκπομπή στα αραβικά, γιατί στη γειτονιά μένουν πολλές οικογένειες από τη Συρία.", "We talk about things you won't hear elsewhere: when the street closes for works, which bakery is opening, which elderly woman needs help with her shopping. Now we're looking for someone to do a programme in Arabic, because many families from Syria live in the neighbourhood."),
 ],
 "questions": [
  Q("Γιατί ο σταθμός εκπέμπει μόνο μέσω διαδικτύου;", ["Γιατί έτσι τον ακούνε περισσότεροι", "Γιατί το ζήτησαν οι ακροατές", "Γιατί μια συχνότητα στα FM κοστίζει πολύ", "Γιατί δεν επιτρέπεται από τον νόμο"], 2, "γιατί μια συχνότητα στα FM κοστίζει πολύ"),
  Q("Ποιοι κάνουν τις εκπομπές;", ["Επαγγελματίες δημοσιογράφοι", "Εθελοντές από τη γειτονιά", "Φοιτητές δημοσιογραφίας", "Υπάλληλοι του δήμου"], 1, "Όλοι οι παραγωγοί είναι εθελοντές από τη γειτονιά"),
  Q("Τι ψάχνει τώρα ο σταθμός;", ["Κάποιον να κάνει εκπομπή στα αραβικά", "Καινούργιο υπόγειο", "Χορηγούς", "Έναν τεχνικό ήχου"], 0, "Τώρα ψάχνουμε κάποιον να κάνει εκπομπή στα αραβικά"),
 ],
 "gloss": {"ιδρυτή": "ιδρυτής — founder", "κοινοτικού": "κοινοτικός — community (adj.)", "σταθμός": "σταθμός — station", "υπόγειο": "υπόγειο — basement", "Εκπέμπουμε": "εκπέμπω — to broadcast", "συχνότητα": "συχνότητα — frequency", "παραγωγοί": "παραγωγός — (radio) presenter, producer", "συνταξιούχος": "συνταξιούχος — pensioner, retired", "ναυτικός": "ναυτικός — sailor", "ζωντανά": "ζωντανά — live", "ηλικιωμένη": "ηλικιωμένη — elderly woman"}
})

ITEMS.append({
 "id": "l135-vm-exetaseis", "title": "Αλλαγή αίθουσας για την προφορική εξέταση", "title_en": "A room change for the speaking exam", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δηλώσει συμμετοχή στις εξετάσεις πιστοποίησης ελληνομάθειας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, σας καλώ από το εξεταστικό κέντρο, σχετικά με την προφορική σας εξέταση το Σάββατο. Λόγω εργασιών στο κτίριο, η εξέταση δεν θα γίνει στην αίθουσα που αναφέρει η πρόσκλησή σας, αλλά στη βιβλιοθήκη, στον δεύτερο όροφο.", "Good morning, I'm calling from the exam centre about your speaking exam on Saturday. Because of works in the building, the exam won't take place in the room stated on your invitation, but in the library, on the second floor."),
  L("Υπάλληλος", "f", "Η ώρα παραμένει η ίδια, όμως σας παρακαλούμε να είστε εκεί μισή ώρα νωρίτερα, γιατί ο έλεγχος των στοιχείων θα γίνεται στην είσοδο του κτιρίου. Μην ξεχάσετε το διαβατήριο ή την ταυτότητά σας· χωρίς αυτά δεν μπορείτε να εξεταστείτε.", "The time stays the same, but please be there half an hour earlier, because ID checks will take place at the building entrance. Don't forget your passport or identity card; without them you cannot sit the exam."),
  L("Υπάλληλος", "f", "Στην αίθουσα αναμονής δεν επιτρέπονται τα κινητά, οπότε θα τα αφήσετε σε ένα ντουλάπι. Αν έχετε απορίες, καλέστε μας στο ίδιο νούμερο. Καλή επιτυχία!", "Mobile phones are not allowed in the waiting room, so you'll leave them in a locker. If you have any questions, call us on the same number. Good luck!"),
 ],
 "questions": [
  Q("Πού θα γίνει τελικά η εξέταση;", ["Στην αίθουσα της πρόσκλησης", "Στη βιβλιοθήκη, στον δεύτερο όροφο", "Σε άλλο κτίριο", "Στο ισόγειο"], 1, "αλλά στη βιβλιοθήκη, στον δεύτερο όροφο"),
  Q("Γιατί πρέπει να είστε εκεί μισή ώρα νωρίτερα;", ["Γιατί άλλαξε η ώρα της εξέτασης", "Για να γράψετε ένα τεστ", "Γιατί ο έλεγχος των στοιχείων θα γίνεται στην είσοδο του κτιρίου", "Για να πληρώσετε τα εξέταστρα"], 2, "γιατί ο έλεγχος των στοιχείων θα γίνεται στην είσοδο του κτιρίου"),
  Q("Τι θα κάνετε με το κινητό σας;", ["Θα το αφήσετε σε ένα ντουλάπι", "Θα το κλείσετε μέσα στην αίθουσα", "Θα το δώσετε στον εξεταστή", "Μπορείτε να το κρατήσετε"], 0, "θα τα αφήσετε σε ένα ντουλάπι"),
 ],
 "gloss": {"πιστοποίησης ελληνομάθειας": "πιστοποίηση ελληνομάθειας — Greek language certification", "εξεταστικό κέντρο": "εξεταστικό κέντρο — exam centre", "προφορική": "προφορικός — oral, speaking", "εργασιών": "εργασία — work (construction)", "πρόσκλησή": "πρόσκληση — invitation, notice", "όροφο": "όροφος — floor", "στοιχείων": "στοιχεία — personal details, ID", "εξεταστείτε": "εξετάζομαι — to be examined, sit an exam", "αναμονής": "αναμονή — waiting", "ντουλάπι": "ντουλάπι — locker, cupboard"}
})

ITEMS.append({
 "id": "l135-c1-franklin", "title": "Το φαινόμενο Φράνκλιν", "title_en": "The Benjamin Franklin effect", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ένα podcast για την κοινωνική ψυχολογία.",
 "script": [
  L("Ομιλητής", "m", "Στην αυτοβιογραφία του, ο Βενιαμίν Φράνκλιν διηγείται πώς κέρδισε έναν πολιτικό αντίπαλο στη Νομοθετική Συνέλευση της Πενσιλβάνια. Δεν τον κολάκευσε ούτε του έκανε κάποια χάρη. Αντίθετα, του έγραψε ένα σημείωμα και του ζήτησε να του δανείσει ένα σπάνιο βιβλίο από τη βιβλιοθήκη του.", "In his autobiography, Benjamin Franklin tells how he won over a political rival in the Pennsylvania Assembly. He didn't flatter him or do him a favour. On the contrary, he wrote him a note and asked to borrow a rare book from his library."),
  L("Ομιλητής", "m", "Ο αντίπαλος τού το έστειλε αμέσως. Ο Φράνκλιν το επέστρεψε σε μια εβδομάδα, με ένα θερμό ευχαριστήριο σημείωμα, και την επόμενη φορά που συναντήθηκαν, ο άνθρωπος τού μίλησε για πρώτη φορά με ευγένεια. Έγιναν, γράφει, φίλοι ως τον θάνατό του. Ο Φράνκλιν το συνόψισε σε ένα παλιό ρητό: όποιος σου έχει κάνει μια φορά καλό είναι πιο πρόθυμος να σου κάνει κι άλλο από εκείνον που έχεις υποχρεώσει εσύ.", "The rival sent it at once. Franklin returned it within a week with a warm note of thanks, and the next time they met, the man spoke to him civilly for the first time. They became, he writes, friends until the man's death. Franklin summed it up in an old maxim: he who has once done you a kindness will be more ready to do you another than he whom you yourself have obliged."),
  L("Ομιλητής", "m", "Το 1969 δύο ψυχολόγοι, ο Τζέκερ και ο Λάντι, το δοκίμασαν πειραματικά. Οι συμμετέχοντες κέρδισαν χρήματα σε ένα τεστ. Σε μερικούς ο ερευνητής ζήτησε στο τέλος, ως προσωπική χάρη, να του επιστρέψουν τα χρήματα. Αυτοί, όταν ρωτήθηκαν, δήλωσαν ότι τον συμπαθούσαν περισσότερο από τους άλλους.", "In 1969 two psychologists, Jecker and Landy, tested it experimentally. Participants won money in a test. Some were asked by the researcher at the end, as a personal favour, to give the money back. When asked, these people said they liked him more than the others did."),
  L("Ομιλητής", "m", "Η πιο συνηθισμένη εξήγηση είναι η γνωστική ασυμφωνία. Όταν βοηθάμε κάποιον, το μυαλό μας χρειάζεται έναν λόγο, και ο πιο βολικός είναι ότι μας αρέσει. Δηλαδή δεν βοηθάμε μόνο όσους συμπαθούμε· συχνά καταλήγουμε να συμπαθούμε όσους βοηθήσαμε.", "The most common explanation is cognitive dissonance. When we help someone, our mind needs a reason, and the most convenient one is that we like them. In other words, we don't only help those we like; we often end up liking those we have helped."),
 ],
 "questions": [
  Q("Τι έκανε ο Φράνκλιν για να κερδίσει τον αντίπαλό του;", ["Τον κολάκευσε δημόσια", "Του ζήτησε να του δανείσει ένα σπάνιο βιβλίο", "Του έκανε ένα ακριβό δώρο", "Τον ψήφισε σε μια εκλογή"], 1, "του ζήτησε να του δανείσει ένα σπάνιο βιβλίο από τη βιβλιοθήκη του"),
  Q("Τι λέει το ρητό που ανέφερε ο Φράνκλιν;", ["Ένας καλός φίλος αξίζει περισσότερο από ένα βιβλίο", "Δεν πρέπει να χρωστάμε χάρες", "Όποιος σου έχει κάνει μια φορά καλό είναι πιο πρόθυμος να σου κάνει κι άλλο", "Οι αντίπαλοι δεν γίνονται ποτέ φίλοι"], 2, "όποιος σου έχει κάνει μια φορά καλό είναι πιο πρόθυμος να σου κάνει κι άλλο"),
  Q("Τι έδειξε το πείραμα του 1969;", ["Όσοι επέστρεψαν τα χρήματα ως προσωπική χάρη συμπαθούσαν περισσότερο τον ερευνητή", "Όσοι κράτησαν τα χρήματα ήταν πιο ευχαριστημένοι", "Οι συμμετέχοντες δεν ήθελαν να επιστρέψουν τα χρήματα", "Τα χρήματα δεν επηρεάζουν τη συμπάθεια"], 0, "δήλωσαν ότι τον συμπαθούσαν περισσότερο από τους άλλους"),
  Q("Πώς εξηγείται συνήθως το φαινόμενο;", ["Με την ανάγκη για ανταπόδοση", "Με τον φόβο της απόρριψης", "Με την επιρροή της ομάδας", "Με τη γνωστική ασυμφωνία: δικαιολογούμε τη βοήθεια λέγοντας ότι μας αρέσει ο άλλος"], 3, "Η πιο συνηθισμένη εξήγηση είναι η γνωστική ασυμφωνία"),
 ],
 "gloss": {"αυτοβιογραφία": "αυτοβιογραφία — autobiography", "διηγείται": "διηγούμαι — to tell, narrate", "αντίπαλο": "αντίπαλος — rival, opponent", "Νομοθετική Συνέλευση": "Νομοθετική Συνέλευση — legislative assembly", "κολάκευσε": "κολακεύω — to flatter", "ευχαριστήριο": "ευχαριστήριος — of thanks", "συνόψισε": "συνοψίζω — to sum up", "ρητό": "ρητό — maxim, saying", "πρόθυμος": "πρόθυμος — willing", "υποχρεώσει": "υποχρεώνω — to oblige, do a favour", "πειραματικά": "πειραματικά — experimentally", "συμπαθούσαν": "συμπαθώ — to like", "γνωστική ασυμφωνία": "γνωστική ασυμφωνία — cognitive dissonance", "βολικός": "βολικός — convenient"}
})

ITEMS.append({
 "id": "l135-c1-gazis", "title": "Άνθιμος Γαζής, ο λόγιος από τις Μηλιές", "title_en": "Anthimos Gazis, the scholar from Milies", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια ιστορικό για τον Άνθιμο Γαζή.",
 "script": [
  L("Δημοσιογράφος", "m", "Ποιος ήταν ο Άνθιμος Γαζής;", "Who was Anthimos Gazis?"),
  L("Ιστορικός", "f", "Ήταν κληρικός και λόγιος από τις Μηλιές του Πηλίου, ένας από τους πιο δραστήριους ανθρώπους του Νεοελληνικού Διαφωτισμού. Έζησε πολλά χρόνια στη Βιέννη, όπου υπηρέτησε ως ιερέας στην ελληνική κοινότητα και ασχολήθηκε με εκδόσεις: μεταφράσεις επιστημονικών βιβλίων, ένα μεγάλο λεξικό της αρχαίας ελληνικής, ακόμη κι έναν χάρτη της Ελλάδας.", "He was a cleric and scholar from Milies on Pelion, one of the most active figures of the Modern Greek Enlightenment. He lived for many years in Vienna, where he served as a priest in the Greek community and worked on publications: translations of scientific books, a large dictionary of Ancient Greek, even a map of Greece."),
  L("Δημοσιογράφος", "m", "Και το περιοδικό;", "And the journal?"),
  L("Ιστορικός", "f", "Ναι, το 1811 ίδρυσε στη Βιέννη τον «Ερμή τον Λόγιο», ένα από τα πρώτα ελληνικά περιοδικά, όπου δημοσιεύονταν άρθρα για τη γλώσσα, τις επιστήμες και την παιδεία. Παράλληλα έστελνε βιβλία στον τόπο του, και στις Μηλιές δημιουργήθηκε μια βιβλιοθήκη, που σώζεται ως σήμερα.", "Yes, in 1811 he founded 'Hermes the Scholar' in Vienna, one of the first Greek journals, which published articles on language, the sciences and education. At the same time he sent books to his home town, and a library was created in Milies that survives to this day."),
  L("Δημοσιογράφος", "m", "Δεν έμεινε όμως μόνο στα γράμματα.", "But he didn't stick only to letters."),
  L("Ιστορικός", "f", "Όχι. Μυήθηκε στη Φιλική Εταιρεία, και την άνοιξη του 1821 κήρυξε την Επανάσταση στο Πήλιο. Το κίνημα εκεί καταπνίγηκε γρήγορα, αλλά ο ίδιος συνέχισε να συμμετέχει στα πολιτικά του Αγώνα. Πέθανε στη Σύρο το 1828. Τον θυμόμαστε σαν παράδειγμα λόγιου που πίστευε ότι η παιδεία και η ελευθερία πάνε μαζί.", "No. He was initiated into the Filiki Etaireia, and in the spring of 1821 he declared the Revolution on Pelion. The movement there was quickly crushed, but he himself went on taking part in the politics of the struggle. He died on Syros in 1828. We remember him as an example of a scholar who believed that education and freedom go together."),
 ],
 "questions": [
  Q("Με τι ασχολήθηκε στη Βιέννη, εκτός από την ιερατική του υπηρεσία;", ["Με το εμπόριο", "Με εκδόσεις: μεταφράσεις, ένα λεξικό, έναν χάρτη", "Με τη διδασκαλία στο πανεπιστήμιο", "Με τη ζωγραφική"], 1, "ασχολήθηκε με εκδόσεις: μεταφράσεις επιστημονικών βιβλίων, ένα μεγάλο λεξικό της αρχαίας ελληνικής, ακόμη κι έναν χάρτη της Ελλάδας"),
  Q("Τι ήταν ο «Ερμής ο Λόγιος»;", ["Ένα σχολείο στις Μηλιές", "Μια εφημερίδα της Αθήνας", "Ένα από τα πρώτα ελληνικά περιοδικά", "Ένα πλοίο της Επανάστασης"], 2, "ένα από τα πρώτα ελληνικά περιοδικά"),
  Q("Τι δημιουργήθηκε στις Μηλιές με τα βιβλία που έστελνε;", ["Μια βιβλιοθήκη που σώζεται ως σήμερα", "Ένα τυπογραφείο", "Ένα μουσείο", "Ένα πανεπιστήμιο"], 0, "στις Μηλιές δημιουργήθηκε μια βιβλιοθήκη, που σώζεται ως σήμερα"),
  Q("Τι έκανε την άνοιξη του 1821;", ["Έφυγε για το Παρίσι", "Έγινε καθηγητής", "Έγραψε ένα λεξικό", "Κήρυξε την Επανάσταση στο Πήλιο"], 3, "την άνοιξη του 1821 κήρυξε την Επανάσταση στο Πήλιο"),
 ],
 "gloss": {"λόγιο": "λόγιος — scholar", "κληρικός": "κληρικός — cleric", "δραστήριους": "δραστήριος — active", "Διαφωτισμού": "Διαφωτισμός — the Enlightenment", "υπηρέτησε": "υπηρετώ — to serve", "κοινότητα": "κοινότητα — community", "εκδόσεις": "έκδοση — publication", "λεξικό": "λεξικό — dictionary", "περιοδικό": "περιοδικό — journal, magazine", "παιδεία": "παιδεία — education", "σώζεται": "σώζομαι — to survive", "Μυήθηκε": "μυούμαι — to be initiated", "κήρυξε": "κηρύσσω — to declare", "καταπνίγηκε": "καταπνίγομαι — to be crushed, suppressed"}
})

rnd = random.Random(135)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-135.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
