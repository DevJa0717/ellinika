# Source for library/listening/listening-52.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l52.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l52-ann-tsouchtres", "title": "Τσούχτρες στην παραλία", "title_en": "Jellyfish on the beach", "type": "announcement", "level": "B2",
 "context_el": "Κάνετε μπάνιο σε μια οργανωμένη παραλία. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα της ναυαγοσωστικής σκοπιάς.",
 "script": [
  L("Ναυαγοσώστρια", "f", "Προσοχή, παρακαλώ. Σας ενημερώνουμε ότι τα τελευταία λεπτά έχουν εμφανιστεί πολλές τσούχτρες στο δεξί τμήμα της παραλίας, κοντά στα βράχια. Παρακαλούμε τους λουόμενους να βγουν από το νερό σε αυτό το σημείο και να κολυμπούν μόνο ανάμεσα στις κίτρινες σημαδούρες.", "Attention, please. We inform you that in the last few minutes many jellyfish have appeared in the right-hand part of the beach, near the rocks. We ask bathers to come out of the water at this spot and to swim only between the yellow buoys."),
  L("Ναυαγοσώστρια", "f", "Αν σας τσιμπήσει τσούχτρα, μην τρίβετε το σημείο και μην το ξεπλένετε με γλυκό νερό, γιατί ο πόνος χειροτερεύει. Ξεπλύνετε με θαλασσινό νερό και ελάτε στη σκοπιά, όπου υπάρχει ειδική αλοιφή. Ιδιαίτερη προσοχή στα μικρά παιδιά.", "If a jellyfish stings you, do not rub the spot and do not rinse it with fresh water, because the pain gets worse. Rinse with sea water and come to the lifeguard tower, where there is a special ointment. Particular care with small children."),
  L("Ναυαγοσώστρια", "f", "Η κόκκινη σημαία θα παραμείνει στο δεξί τμήμα μέχρι νεωτέρας. Ευχαριστούμε για τη συνεργασία σας.", "The red flag will remain on the right-hand part until further notice. Thank you for your cooperation."),
 ],
 "questions": [
  Q("Πού έχουν εμφανιστεί οι τσούχτρες;", ["Σε όλη την παραλία", "Στο δεξί τμήμα, κοντά στα βράχια", "Ανάμεσα στις κίτρινες σημαδούρες", "Στο λιμανάκι"], 1, "στο δεξί τμήμα της παραλίας, κοντά στα βράχια"),
  Q("Τι δεν πρέπει να κάνει κάποιος αν τον τσιμπήσει τσούχτρα;", ["Να έρθει στη σκοπιά", "Να ξεπλύνει το σημείο με γλυκό νερό", "Να ξεπλύνει με θαλασσινό νερό", "Να βγει από το νερό"], 1, "μην το ξεπλένετε με γλυκό νερό, γιατί ο πόνος χειροτερεύει"),
  Q("Μέχρι πότε θα μείνει η κόκκινη σημαία;", ["Μέχρι το απόγευμα", "Μέχρι νεωτέρας", "Για μία ώρα", "Μέχρι αύριο το πρωί"], 1, "θα παραμείνει στο δεξί τμήμα μέχρι νεωτέρας"),
 ],
 "gloss": {"τσούχτρες": "τσούχτρα — jellyfish (stinging)", "ναυαγοσωστικής σκοπιάς": "ναυαγοσωστική σκοπιά — lifeguard tower", "λουόμενους": "λουόμενος — bather", "σημαδούρες": "σημαδούρα — buoy", "τσιμπήσει": "τσιμπάω — to sting, bite, pinch", "τρίβετε": "τρίβω — to rub", "γλυκό νερό": "γλυκό νερό — fresh water", "αλοιφή": "αλοιφή — ointment", "μέχρι νεωτέρας": "μέχρι νεωτέρας — until further notice"},
})

ITEMS.append({
 "id": "l52-vm-synergeio", "title": "Το αυτοκίνητο είναι έτοιμο;", "title_en": "Is the car ready?", "type": "voicemail", "level": "B2",
 "context_el": "Αφήσατε το αυτοκίνητό σας σε ένα συνεργείο για σέρβις. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Μηχανικός", "m", "Καλησπέρα, κύριε Αθανασίου, ο Μανώλης από το συνεργείο είμαι. Κάναμε το σέρβις στο αυτοκίνητό σας: αλλάξαμε λάδια, φίλτρα και τα μπροστινά τακάκια, όπως είχαμε πει. Όταν όμως το σηκώσαμε, είδαμε ότι η εξάτμιση έχει σαπίσει και χάνει από δύο σημεία.", "Good evening, Mr Athanasiou, it's Manolis from the garage. We've done the service on your car: we changed the oil, the filters and the front brake pads, as we'd said. But when we lifted it up, we saw that the exhaust has rusted through and is leaking in two places."),
  L("Μηχανικός", "m", "Δεν είναι επικίνδυνο άμεσα, αλλά με τέτοια εξάτμιση δεν θα περάσετε το ΚΤΕΟ τον άλλο μήνα. Η καινούργια κοστίζει γύρω στα διακόσια ευρώ με την εργασία. Αν θέλετε να την αλλάξουμε, πρέπει να παραγγείλουμε το ανταλλακτικό σήμερα, για να έρθει αύριο το πρωί.", "It isn't immediately dangerous, but with an exhaust like that you won't pass the MOT next month. A new one costs around two hundred euros including labour. If you want us to change it, we need to order the part today so that it arrives tomorrow morning."),
  L("Μηχανικός", "m", "Πάρτε με μέχρι τις επτά να μου πείτε τι αποφασίσατε. Σε κάθε περίπτωση, το αυτοκίνητο μπορείτε να το παραλάβετε από αύριο στις δώδεκα.", "Call me by seven to tell me what you've decided. Either way, you can collect the car from tomorrow at twelve."),
 ],
 "questions": [
  Q("Τι πρόβλημα βρήκε ο μηχανικός;", ["Τα τακάκια είχαν φθαρεί", "Η εξάτμιση έχει σαπίσει και χάνει", "Το λάδι ήταν λίγο", "Η μπαταρία είχε αδειάσει"], 1, "η εξάτμιση έχει σαπίσει και χάνει από δύο σημεία"),
  Q("Γιατί πρέπει να αποφασίσει γρήγορα ο κ. Αθανασίου;", ["Γιατί το συνεργείο κλείνει για διακοπές", "Γιατί το ανταλλακτικό πρέπει να παραγγελθεί σήμερα", "Γιατί η τιμή θα ανέβει", "Γιατί το αυτοκίνητο είναι επικίνδυνο"], 1, "πρέπει να παραγγείλουμε το ανταλλακτικό σήμερα, για να έρθει αύριο το πρωί"),
  Q("Πότε μπορεί να παραλάβει το αυτοκίνητο;", ["Σήμερα στις επτά", "Από αύριο στις δώδεκα", "Τον άλλο μήνα", "Αύριο το πρωί στις οκτώ"], 1, "μπορείτε να το παραλάβετε από αύριο στις δώδεκα"),
 ],
 "gloss": {"συνεργείο": "συνεργείο — garage, repair shop", "τακάκια": "τακάκι — brake pad", "εξάτμιση": "εξάτμιση — exhaust (pipe)", "έχει σαπίσει": "σαπίζω — to rot, rust through", "χάνει": "χάνω — to lose; to leak", "ΚΤΕΟ": "ΚΤΕΟ — vehicle roadworthiness test (like the MOT)", "ανταλλακτικό": "ανταλλακτικό — spare part", "παραλάβετε": "παραλαμβάνω — to collect, take delivery of"},
})

ITEMS.append({
 "id": "l52-dia-enoikio", "title": "Βλέποντας ένα διαμέρισμα", "title_en": "Viewing a flat", "type": "dialogue", "level": "B2",
 "context_el": "Η Δέσποινα ψάχνει διαμέρισμα για ενοικίαση στη Θεσσαλονίκη και το επισκέπτεται με τον ιδιοκτήτη.",
 "script": [
  L("Ιδιοκτήτης", "m", "Ορίστε, περάστε. Όπως βλέπετε, είναι πολύ φωτεινό, γιατί βλέπει νότια. Το σαλόνι και η κουζίνα είναι ενιαίος χώρος, και υπάρχουν δύο υπνοδωμάτια.", "Here, come in. As you can see, it's very bright, because it faces south. The living room and kitchen are open-plan, and there are two bedrooms."),
  L("Δέσποινα", "f", "Πολύ ωραίο. Η θέρμανση πώς είναι; Στην αγγελία έγραφε αυτόνομη.", "Very nice. What's the heating like? The ad said independent."),
  L("Ιδιοκτήτης", "m", "Ναι, έχει δική του αντλία θερμότητας, οπότε πληρώνετε μόνο ό,τι καταναλώνετε. Τα κοινόχρηστα είναι γύρω στα τριάντα ευρώ τον μήνα, γιατί δεν υπάρχει κεντρική θέρμανση.", "Yes, it has its own heat pump, so you pay only for what you use. The service charges are around thirty euros a month, because there's no central heating."),
  L("Δέσποινα", "f", "Και κατοικίδια επιτρέπονται; Έχω μια γάτα.", "And are pets allowed? I have a cat."),
  L("Ιδιοκτήτης", "m", "Μια γάτα δεν είναι πρόβλημα. Ζητάω μόνο δύο ενοίκια εγγύηση και συμβόλαιο για τρία χρόνια. Αν σας ενδιαφέρει, το σπίτι είναι διαθέσιμο από την πρώτη του μήνα.", "A cat is no problem. I only ask for two months' rent as a deposit and a three-year contract. If you're interested, the flat is available from the first of the month."),
  L("Δέσποινα", "f", "Μου αρέσει πολύ. Θα ήθελα μόνο να το δω και μια φορά το βράδυ, να καταλάβω αν έχει θόρυβο από τον δρόμο.", "I like it a lot. I'd just like to see it once in the evening too, to find out if there's noise from the street."),
 ],
 "questions": [
  Q("Γιατί είναι φωτεινό το διαμέρισμα;", ["Γιατί είναι στον τελευταίο όροφο", "Γιατί βλέπει νότια", "Γιατί έχει μεγάλα παράθυρα στην κουζίνα", "Γιατί δεν έχει απέναντι πολυκατοικία"], 1, "είναι πολύ φωτεινό, γιατί βλέπει νότια"),
  Q("Γιατί τα κοινόχρηστα είναι χαμηλά;", ["Γιατί η πολυκατοικία είναι καινούργια", "Γιατί δεν υπάρχει κεντρική θέρμανση", "Γιατί δεν υπάρχει ασανσέρ", "Γιατί τα πληρώνει ο ιδιοκτήτης"], 1, "Τα κοινόχρηστα είναι γύρω στα τριάντα ευρώ τον μήνα, γιατί δεν υπάρχει κεντρική θέρμανση"),
  Q("Τι θέλει να κάνει η Δέσποινα πριν αποφασίσει;", ["Να μιλήσει με τους γείτονες", "Να δει το σπίτι και το βράδυ", "Να φέρει τη γάτα της", "Να διαπραγματευτεί την τιμή"], 1, "Θα ήθελα μόνο να το δω και μια φορά το βράδυ"),
 ],
 "gloss": {"ενοικίαση": "ενοικίαση — renting, letting", "βλέπει νότια": "βλέπω νότια — to face south", "ενιαίος χώρος": "ενιαίος χώρος — open-plan space", "αγγελία": "αγγελία — advertisement (classified)", "αυτόνομη": "αυτόνομος — independent (of heating: not shared)", "αντλία θερμότητας": "αντλία θερμότητας — heat pump", "κοινόχρηστα": "κοινόχρηστα — building service charges", "κατοικίδια": "κατοικίδιο — pet", "εγγύηση": "εγγύηση — deposit; guarantee", "συμβόλαιο": "συμβόλαιο — contract, lease"},
})

ITEMS.append({
 "id": "l52-dia-tango", "title": "Μαθήματα τάνγκο", "title_en": "Tango lessons", "type": "dialogue", "level": "B2",
 "context_el": "Ο Παύλος τηλεφωνεί σε μια σχολή χορού για να ρωτήσει για μαθήματα τάνγκο για τον ίδιο και τη γυναίκα του.",
 "script": [
  L("Παύλος", "m", "Καλησπέρα. Θα ήθελα πληροφορίες για τα μαθήματα τάνγκο. Είμαστε εντελώς αρχάριοι, εγώ και η γυναίκα μου.", "Good evening. I'd like some information about the tango lessons. We're complete beginners, my wife and I."),
  L("Υπάλληλος", "f", "Μάλιστα. Έχουμε τμήμα αρχαρίων κάθε Τρίτη και Πέμπτη στις οχτώμισι. Ένας νέος κύκλος ξεκινάει την επόμενη Τρίτη, οπότε έρχεστε στην κατάλληλη στιγμή.", "Certainly. We have a beginners' class every Tuesday and Thursday at half past eight. A new course starts next Tuesday, so you're calling at just the right moment."),
  L("Παύλος", "m", "Τέλεια. Και το κόστος; Υπάρχει κάποια έκπτωση για ζευγάρια;", "Perfect. And the cost? Is there a discount for couples?"),
  L("Υπάλληλος", "f", "Ο μήνας κοστίζει πενήντα ευρώ το άτομο, αλλά τα ζευγάρια πληρώνουν ογδόντα συνολικά. Το πρώτο μάθημα είναι δωρεάν, για να δείτε αν σας αρέσει.", "A month costs fifty euros per person, but couples pay eighty in total. The first lesson is free, so you can see if you like it."),
  L("Παύλος", "m", "Χρειαζόμαστε ειδικά παπούτσια;", "Do we need special shoes?"),
  L("Υπάλληλος", "f", "Στην αρχή όχι. Φέρτε απλώς παπούτσια με λεία σόλα, που γλιστράνε λίγο. Τα αθλητικά δεν είναι καλά, γιατί κολλάνε στο πάτωμα. Αν συνεχίσετε, θα σας προτείνω αργότερα ένα κατάστημα.", "Not at first. Just bring shoes with smooth soles that slide a little. Trainers aren't good, because they stick to the floor. If you continue, I'll recommend a shop later."),
 ],
 "questions": [
  Q("Πότε ξεκινάει ο νέος κύκλος μαθημάτων;", ["Την επόμενη Πέμπτη", "Την επόμενη Τρίτη", "Τον άλλο μήνα", "Απόψε"], 1, "Ένας νέος κύκλος ξεκινάει την επόμενη Τρίτη"),
  Q("Πόσο πληρώνει ένα ζευγάρι τον μήνα;", ["Εκατό ευρώ", "Ογδόντα ευρώ συνολικά", "Πενήντα ευρώ", "Τίποτα τον πρώτο μήνα"], 1, "τα ζευγάρια πληρώνουν ογδόντα συνολικά"),
  Q("Γιατί δεν είναι κατάλληλα τα αθλητικά παπούτσια;", ["Γιατί είναι βαριά", "Γιατί κολλάνε στο πάτωμα", "Γιατί χαλάνε το πάτωμα", "Γιατί δεν επιτρέπονται στη σχολή"], 1, "Τα αθλητικά δεν είναι καλά, γιατί κολλάνε στο πάτωμα"),
 ],
 "gloss": {"αρχάριοι": "αρχάριος — beginner", "τμήμα αρχαρίων": "τμήμα αρχαρίων — beginners' class", "κύκλος": "κύκλος — course, cycle (of lessons)", "συνολικά": "συνολικά — in total", "λεία σόλα": "λεία σόλα — smooth sole", "γλιστράνε": "γλιστράω — to slide, slip", "κολλάνε": "κολλάω — to stick"},
})

ITEMS.append({
 "id": "l52-int-anapalaiosi", "title": "Η αρχιτέκτονας των παλιών σπιτιών", "title_en": "The architect of old houses", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με την Ευανθία, μια αρχιτέκτονα που αναπαλαιώνει παραδοσιακά σπίτια στο Πήλιο.",
 "script": [
  L("Δημοσιογράφος", "m", "Ευανθία, πώς αποφασίσατε να ασχοληθείτε με τα παλιά σπίτια;", "Evanthia, how did you decide to work on old houses?"),
  L("Ευανθία", "f", "Όταν τελείωσα τη σχολή, δούλεψα πέντε χρόνια σε ένα μεγάλο γραφείο στην Αθήνα και σχεδίαζα πολυκατοικίες. Κάποια στιγμή η γιαγιά μου μου άφησε ένα ερειπωμένο σπίτι στη Μακρινίτσα. Ξεκίνησα να το φτιάχνω για μένα, και μέσα σε δύο χρόνια οι μισοί γείτονες μου ζητούσαν να φτιάξω και τα δικά τους.", "When I finished my degree, I worked for five years in a big practice in Athens designing apartment blocks. At some point my grandmother left me a ruined house in Makrinitsa. I started repairing it for myself, and within two years half the neighbours were asking me to do theirs too."),
  L("Δημοσιογράφος", "m", "Ποια είναι η μεγαλύτερη δυσκολία;", "What's the biggest difficulty?"),
  L("Ευανθία", "f", "Οι τεχνίτες. Λίγοι άνθρωποι ξέρουν ακόμα να χτίζουν ξερολιθιά ή να στρώνουν στέγη με πλάκες. Γι' αυτό συνεργάζομαι με δύο μάστορες εβδομήντα χρονών και τους ζητάω να μαθαίνουν την τέχνη τους σε νέα παιδιά από τα χωριά.", "The craftsmen. Few people still know how to build a dry-stone wall or lay a roof with slabs. That's why I work with two master builders in their seventies and ask them to teach their craft to young people from the villages."),
  L("Δημοσιογράφος", "m", "Δεν είναι πιο ακριβό από ένα καινούργιο σπίτι;", "Isn't it more expensive than a new house?"),
  L("Ευανθία", "f", "Συχνά ναι, κατά είκοσι με τριάντα τοις εκατό. Όμως ένα πέτρινο σπίτι με χοντρούς τοίχους κρατάει δροσιά το καλοκαίρι και ζέστη τον χειμώνα. Σε βάθος χρόνου, η διαφορά βγαίνει από την ενέργεια που εξοικονομείς.", "Often yes, by twenty to thirty percent. But a stone house with thick walls stays cool in summer and warm in winter. In the long run, the difference is recovered from the energy you save."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η Ευανθία να ασχολείται με τα παλιά σπίτια;", ["Τη ζήτησε ο δήμος της Μακρινίτσας", "Επισκεύασε ένα σπίτι που της άφησε η γιαγιά της", "Το σπούδασε σε μεταπτυχιακό", "Αγόρασε ένα παλιό σπίτι για επένδυση"], 1, "η γιαγιά μου μου άφησε ένα ερειπωμένο σπίτι στη Μακρινίτσα. Ξεκίνησα να το φτιάχνω για μένα"),
  Q("Τι κάνει για το πρόβλημα με τους τεχνίτες;", ["Φέρνει τεχνίτες από το εξωτερικό", "Ζητάει από δύο ηλικιωμένους μάστορες να μαθαίνουν την τέχνη σε νέους", "Χρησιμοποιεί σύγχρονα υλικά", "Κάνει η ίδια όλες τις δουλειές"], 1, "τους ζητάω να μαθαίνουν την τέχνη τους σε νέα παιδιά από τα χωριά"),
  Q("Γιατί, κατά την Ευανθία, αξίζει τελικά το επιπλέον κόστος;", ["Γιατί τα σπίτια πουλιούνται πιο ακριβά", "Γιατί εξοικονομείς ενέργεια με τους χοντρούς τοίχους", "Γιατί το κράτος δίνει επιδότηση", "Γιατί δεν χρειάζονται ποτέ επισκευή"], 1, "Σε βάθος χρόνου, η διαφορά βγαίνει από την ενέργεια που εξοικονομείς"),
 ],
 "gloss": {"αναπαλαιώνει": "αναπαλαιώνω — to restore (an old building)", "ερειπωμένο": "ερειπωμένος — ruined, derelict", "τεχνίτες": "τεχνίτης — craftsman", "ξερολιθιά": "ξερολιθιά — dry-stone wall", "πλάκες": "πλάκα — (stone) slab", "μάστορες": "μάστορας — master builder, craftsman", "βάθος χρόνου": "σε βάθος χρόνου — in the long run", "εξοικονομείς": "εξοικονομώ — to save (energy, money)"},
})

ITEMS.append({
 "id": "l52-rep-dioryga", "title": "Η Διώρυγα της Κορίνθου", "title_en": "The Corinth Canal", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ για τη Διώρυγα της Κορίνθου.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρίσκομαι πάνω από τη Διώρυγα της Κορίνθου, σε ύψος σχεδόν ογδόντα μέτρων από το νερό. Από εδώ το κανάλι μοιάζει με μια ίσια, βαθιά πληγή στη γη, μήκους περίπου έξι χιλιομέτρων, που ενώνει τον Κορινθιακό με τον Σαρωνικό κόλπο.", "I'm standing above the Corinth Canal, almost eighty metres above the water. From here the canal looks like a straight, deep wound in the earth, about six kilometres long, joining the Gulf of Corinth with the Saronic Gulf."),
  L("Ρεπόρτερ", "f", "Η ιδέα είναι πανάρχαια: ήδη ο τύραννος Περίανδρος, τον έβδομο αιώνα π.Χ., σκέφτηκε να κόψει τον Ισθμό, και ο Νέρων ξεκίνησε τις εργασίες το 67 μ.Χ. Τελικά η διώρυγα ολοκληρώθηκε μόλις το 1893. Ως τότε, τα πλοία είτε έκαναν τον γύρο της Πελοποννήσου είτε σέρνονταν πάνω σε έναν λιθόστρωτο δρόμο, τον Δίολκο.", "The idea is ancient: already the tyrant Periander, in the seventh century BC, thought of cutting through the Isthmus, and Nero began the work in 67 AD. In the end the canal was completed only in 1893. Until then, ships either sailed round the Peloponnese or were dragged over a paved road, the Diolkos."),
  L("Ρεπόρτερ", "f", "Σήμερα, επειδή είναι στενή, μόλις είκοσι ενός μέτρων, η διώρυγα δεν εξυπηρετεί τα μεγάλα εμπορικά πλοία. Τη χρησιμοποιούν κυρίως σκάφη αναψυχής και κρουαζιερόπλοια μικρού μεγέθους, ενώ οι κατολισθήσεις στα πρανή της την κρατούν συχνά κλειστή για μήνες.", "Today, because it is narrow, just twenty-one metres, the canal cannot serve large cargo ships. It is used mainly by pleasure craft and small cruise ships, while landslides on its slopes often keep it closed for months."),
 ],
 "questions": [
  Q("Ποιους κόλπους ενώνει η διώρυγα;", ["Τον Θερμαϊκό και τον Σαρωνικό", "Τον Κορινθιακό και τον Σαρωνικό", "Τον Αργολικό και τον Κορινθιακό", "Τον Σαρωνικό και τον Αργολικό"], 1, "ενώνει τον Κορινθιακό με τον Σαρωνικό κόλπο"),
  Q("Πώς περνούσαν τα πλοία τον Ισθμό πριν από το 1893;", ["Με ένα αρχαίο κανάλι του Νέρωνα", "Σέρνονταν πάνω σε έναν λιθόστρωτο δρόμο", "Με σιδηρόδρομο", "Δεν μπορούσαν να περάσουν με κανέναν τρόπο"], 1, "σέρνονταν πάνω σε έναν λιθόστρωτο δρόμο, τον Δίολκο"),
  Q("Γιατί δεν τη χρησιμοποιούν τα μεγάλα εμπορικά πλοία;", ["Γιατί τα διόδια είναι ακριβά", "Γιατί είναι πολύ στενή", "Γιατί είναι ρηχή", "Γιατί είναι πάντα κλειστή"], 1, "επειδή είναι στενή, μόλις είκοσι ενός μέτρων, η διώρυγα δεν εξυπηρετεί τα μεγάλα εμπορικά πλοία"),
 ],
 "gloss": {"Διώρυγα": "διώρυγα — canal (ship canal)", "πληγή": "πληγή — wound", "πανάρχαια": "πανάρχαιος — very ancient", "Ισθμό": "ισθμός — isthmus", "σέρνονταν": "σέρνομαι — to be dragged", "λιθόστρωτο": "λιθόστρωτος — paved with stone", "σκάφη αναψυχής": "σκάφος αναψυχής — pleasure craft, yacht", "κατολισθήσεις": "κατολίσθηση — landslide", "πρανή": "πρανές — slope, bank (of a cutting)"},
})

ITEMS.append({
 "id": "l52-dia-parnitha", "title": "Πεζοπορία στην Πάρνηθα", "title_en": "A hike on Parnitha", "type": "dialogue", "level": "B2",
 "context_el": "Η Ζωή και ο Άλκης κανονίζουν μια πεζοπορία στην Πάρνηθα για την Κυριακή.",
 "script": [
  L("Ζωή", "f", "Λοιπόν, για την Κυριακή σκέφτηκα να ανέβουμε στο καταφύγιο Μπάφι. Είναι περίπου τρεις ώρες από το Τελεφερίκ, με ανηφόρα στην αρχή αλλά όχι δύσκολη.", "So, for Sunday I thought we could go up to the Bafi refuge. It's about three hours from the Teleferik, uphill at the start but not difficult."),
  L("Άλκης", "m", "Ωραία. Μόνο που η πρόγνωση λέει βροχή μετά τις τρεις το μεσημέρι. Λες να ξεκινήσουμε νωρίτερα;", "Great. Only the forecast says rain after three in the afternoon. Shall we start earlier?"),
  L("Ζωή", "f", "Ναι, να φύγουμε από την Αθήνα στις επτά. Έτσι θα είμαστε στο καταφύγιο για φαγητό και θα κατεβούμε πριν χαλάσει ο καιρός.", "Yes, let's leave Athens at seven. That way we'll be at the refuge for lunch and come down before the weather turns."),
  L("Άλκης", "m", "Να πάρουμε φαγητό μαζί ή τρώμε στο καταφύγιο;", "Should we take food with us or do we eat at the refuge?"),
  L("Ζωή", "f", "Το καταφύγιο σερβίρει φαγητό τα Σαββατοκύριακα, φασολάδα και τέτοια. Πάρε όμως οπωσδήποτε δύο μπουκάλια νερό και ένα αντιανεμικό, γιατί εκεί πάνω κάνει πολύ πιο κρύο από ό,τι στην πόλη.", "The refuge serves food at weekends, bean soup and that sort of thing. But definitely bring two bottles of water and a windbreaker, because up there it's much colder than in the city."),
  L("Άλκης", "m", "Και τα ελάφια; Λένε ότι τα βλέπεις συχνά.", "And the deer? They say you often see them."),
  L("Ζωή", "f", "Αν είμαστε ήσυχοι, ίσως. Αλλά μην τους δώσεις τίποτα να φάνε, απαγορεύεται.", "If we're quiet, maybe. But don't give them anything to eat; it's forbidden."),
 ],
 "questions": [
  Q("Γιατί αποφασίζουν να ξεκινήσουν νωρίς;", ["Γιατί το καταφύγιο κλείνει νωρίς", "Γιατί η πρόγνωση λέει βροχή μετά τις τρεις", "Για να δουν τα ελάφια", "Γιατί η διαδρομή είναι πολύ μεγάλη"], 1, "η πρόγνωση λέει βροχή μετά τις τρεις το μεσημέρι"),
  Q("Τι πρέπει οπωσδήποτε να πάρει μαζί του ο Άλκης;", ["Φαγητό για όλη τη μέρα", "Νερό και αντιανεμικό", "Ομπρέλα", "Φακό"], 1, "Πάρε όμως οπωσδήποτε δύο μπουκάλια νερό και ένα αντιανεμικό"),
  Q("Τι λέει η Ζωή για τα ελάφια;", ["Ότι είναι επικίνδυνα", "Ότι απαγορεύεται να τα ταΐζουν", "Ότι εμφανίζονται μόνο τη νύχτα", "Ότι υπάρχουν μόνο κοντά στο Τελεφερίκ"], 1, "μην τους δώσεις τίποτα να φάνε, απαγορεύεται"),
 ],
 "gloss": {"πεζοπορία": "πεζοπορία — hike, hiking", "καταφύγιο": "καταφύγιο — mountain refuge, hut", "ανηφόρα": "ανηφόρα — uphill slope", "πρόγνωση": "πρόγνωση — (weather) forecast", "πριν χαλάσει ο καιρός": "χαλάει ο καιρός — the weather turns bad", "φασολάδα": "φασολάδα — bean soup", "αντιανεμικό": "αντιανεμικό — windbreaker", "ελάφια": "ελάφι — deer"},
})

ITEMS.append({
 "id": "l52-mono-mageiriki", "title": "Πριν από το μάθημα μαγειρικής", "title_en": "Before the cooking class", "type": "monologue", "level": "B2",
 "context_el": "Έχετε γραφτεί σε ένα μάθημα κρητικής μαγειρικής. Θα ακούσετε τη σεφ να μιλάει στους συμμετέχοντες πριν ξεκινήσουν.",
 "script": [
  L("Σεφ", "f", "Καλώς ήρθατε! Σήμερα θα φτιάξουμε τρία πιάτα: ντάκο, καλιτσούνια και κρητικό σαλιγκάρι μπουμπουριστό. Μην ανησυχείτε, όσοι δεν τρώνε σαλιγκάρια μπορούν να φτιάξουν στη θέση τους χόρτα με αυγά.", "Welcome! Today we'll make three dishes: dakos, kalitsounia and Cretan fried snails. Don't worry, those who don't eat snails can make wild greens with eggs instead."),
  L("Σεφ", "f", "Πριν αρχίσουμε, πλύνετε καλά τα χέρια σας και φορέστε τις ποδιές που βρίσκονται πάνω στους πάγκους. Κάθε πάγκος έχει δύο άτομα. Τα μαχαίρια είναι πολύ κοφτερά, οπότε κόβετε πάντα με τα δάχτυλα μαζεμένα, όπως θα σας δείξω.", "Before we start, wash your hands well and put on the aprons that are on the counters. Each counter has two people. The knives are very sharp, so always cut with your fingers tucked in, as I'll show you."),
  L("Σεφ", "f", "Για τα καλιτσούνια, η ζύμη πρέπει να ξεκουραστεί μισή ώρα, γι' αυτό θα ξεκινήσουμε από αυτήν. Στο τέλος θα καθίσουμε όλοι μαζί να φάμε ό,τι φτιάξαμε, με κρασί από τη Σητεία. Και θα πάρετε μαζί σας τις συνταγές, τυπωμένες.", "For the kalitsounia, the dough needs to rest for half an hour, so we'll start with that. At the end we'll all sit down together to eat what we've made, with wine from Sitia. And you'll take the recipes home with you, printed."),
 ],
 "questions": [
  Q("Τι μπορούν να φτιάξουν όσοι δεν τρώνε σαλιγκάρια;", ["Ντάκο", "Χόρτα με αυγά", "Περισσότερα καλιτσούνια", "Σαλάτα"], 1, "μπορούν να φτιάξουν στη θέση τους χόρτα με αυγά"),
  Q("Γιατί θα ξεκινήσουν από τα καλιτσούνια;", ["Γιατί είναι το πιο εύκολο πιάτο", "Γιατί η ζύμη πρέπει να ξεκουραστεί μισή ώρα", "Γιατί ψήνονται πολύ ώρα", "Γιατί είναι το αγαπημένο της σεφ"], 1, "η ζύμη πρέπει να ξεκουραστεί μισή ώρα, γι' αυτό θα ξεκινήσουμε από αυτήν"),
  Q("Τι θα πάρουν μαζί τους οι συμμετέχοντες;", ["Ένα μπουκάλι κρασί", "Τις συνταγές, τυπωμένες", "Τις ποδιές", "Ένα κουτί καλιτσούνια"], 1, "θα πάρετε μαζί σας τις συνταγές, τυπωμένες"),
 ],
 "gloss": {"ντάκο": "ντάκος — Cretan rusk salad with tomato and cheese", "καλιτσούνια": "καλιτσούνι — small Cretan cheese pie", "μπουμπουριστό": "μπουμπουριστός — (snails) fried face-down in oil (Cretan)", "χόρτα": "χόρτα — wild greens", "ποδιές": "ποδιά — apron", "πάγκους": "πάγκος — (kitchen) counter, bench", "κοφτερά": "κοφτερός — sharp", "ζύμη": "ζύμη — dough", "ξεκουραστεί": "ξεκουράζομαι — to rest"},
})

ITEMS.append({
 "id": "l52-c1-xoria", "title": "Ζωή ξανά στα ορεινά χωριά;", "title_en": "Life again in the mountain villages?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν κοινωνιολόγο για την ερήμωση και τις προσπάθειες αναζωογόνησης των ορεινών χωριών.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Σταθόπουλε, τα ορεινά χωριά αδειάζουν εδώ και δεκαετίες. Είναι μια διαδικασία αναστρέψιμη;", "Mr Stathopoulos, mountain villages have been emptying for decades. Is it a reversible process?"),
  L("Κοινωνιολόγος", "m", "Η ερήμωση ξεκίνησε μαζικά τη δεκαετία του '50 και του '60, με την εσωτερική μετανάστευση προς την Αθήνα και τη Θεσσαλονίκη και την εξωτερική προς τη Γερμανία και την Αυστραλία. Σήμερα υπάρχουν χωριά με λιγότερους από δέκα μόνιμους κατοίκους, όλοι συνταξιούχοι. Το να αντιστραφεί πλήρως αυτή η πορεία δεν είναι ρεαλιστικό· μπορούμε όμως να μιλάμε για θύλακες αναζωογόνησης.", "Depopulation began on a mass scale in the fifties and sixties, with internal migration to Athens and Thessaloniki and emigration to Germany and Australia. Today there are villages with fewer than ten permanent residents, all pensioners. Fully reversing that trend is not realistic; but we can talk about pockets of revival."),
  L("Δημοσιογράφος", "f", "Ποιοι είναι αυτοί που επιστρέφουν;", "Who are the people returning?"),
  L("Κοινωνιολόγος", "m", "Δύο ομάδες κυρίως. Η πρώτη είναι νέοι που, μετά την οικονομική κρίση, είδαν ότι στην πόλη δεν είχαν προοπτική και γύρισαν στα πατρικά τους κτήματα, συχνά με σύγχρονες ιδέες: βιολογικές καλλιέργειες, μεταποίηση, πωλήσεις μέσω διαδικτύου. Η δεύτερη, πιο πρόσφατη, είναι όσοι εργάζονται εξ αποστάσεως και μπορούν να ζουν οπουδήποτε υπάρχει καλή σύνδεση.", "Two groups mainly. The first are young people who, after the economic crisis, saw they had no prospects in the city and returned to their family land, often with modern ideas: organic farming, processing, online sales. The second, more recent, are those who work remotely and can live wherever there is a good connection."),
  L("Δημοσιογράφος", "f", "Τι τους κρατάει, ή τι τους διώχνει;", "What keeps them, or what drives them away?"),
  L("Κοινωνιολόγος", "m", "Το κρίσιμο ζήτημα είναι οι υποδομές. Μια οικογένεια με παιδιά δεν θα μείνει σε ένα χωριό όπου το σχολείο έκλεισε και το πλησιέστερο κέντρο υγείας απέχει μία ώρα δρόμο. Κάθε φορά που κλείνει ένα σχολείο για εξοικονόμηση πόρων, ουσιαστικά υπογράφεται η καταδίκη ενός χωριού. Αν η πολιτεία θέλει πράγματι να στηρίξει την ύπαιθρο, πρέπει να αντιμετωπίσει αυτές τις υπηρεσίες ως επένδυση και όχι ως κόστος.", "The crucial issue is infrastructure. A family with children will not stay in a village where the school has closed and the nearest health centre is an hour's drive away. Every time a school is closed to save resources, a village's death warrant is effectively signed. If the state really wants to support the countryside, it must treat these services as an investment, not a cost."),
 ],
 "questions": [
  Q("Πώς βλέπει ο κοινωνιολόγος το ενδεχόμενο να αντιστραφεί η ερήμωση;", ["Πιστεύει ότι θα αντιστραφεί πλήρως σε λίγα χρόνια", "Θεωρεί μη ρεαλιστική την πλήρη αντιστροφή, αλλά βλέπει θύλακες αναζωογόνησης", "Θεωρεί ότι δεν υπάρχει καμία ελπίδα", "Πιστεύει ότι εξαρτάται μόνο από τον τουρισμό"], 1, "Το να αντιστραφεί πλήρως αυτή η πορεία δεν είναι ρεαλιστικό· μπορούμε όμως να μιλάμε για θύλακες αναζωογόνησης"),
  Q("Τι χαρακτηρίζει την πρώτη ομάδα όσων επιστρέφουν;", ["Είναι συνταξιούχοι που γυρίζουν από τη Γερμανία", "Είναι νέοι που γύρισαν μετά την κρίση, συχνά με σύγχρονες ιδέες για την παραγωγή", "Είναι ξένοι που αγόρασαν εξοχικά", "Είναι δημόσιοι υπάλληλοι που μετατέθηκαν"], 1, "νέοι που, μετά την οικονομική κρίση, ... γύρισαν στα πατρικά τους κτήματα, συχνά με σύγχρονες ιδέες"),
  Q("Τι κάνει δυνατή την επιστροφή της δεύτερης ομάδας;", ["Οι επιδοτήσεις για αγρότες", "Η εξ αποστάσεως εργασία και η καλή σύνδεση στο διαδίκτυο", "Τα χαμηλά ενοίκια", "Οι νέοι δρόμοι"], 1, "όσοι εργάζονται εξ αποστάσεως και μπορούν να ζουν οπουδήποτε υπάρχει καλή σύνδεση"),
  Q("Τι εννοεί λέγοντας ότι με το κλείσιμο ενός σχολείου «υπογράφεται η καταδίκη ενός χωριού»;", ["Ότι οι δάσκαλοι φεύγουν πρώτοι", "Ότι χωρίς σχολείο οι οικογένειες δεν μένουν και το χωριό σβήνει", "Ότι το κράτος πουλάει τα κτίρια", "Ότι οι κάτοικοι διαμαρτύρονται στα δικαστήρια"], 1, "Μια οικογένεια με παιδιά δεν θα μείνει σε ένα χωριό όπου το σχολείο έκλεισε"),
 ],
 "gloss": {"ερήμωση": "ερήμωση — depopulation, desertion", "αναζωογόνησης": "αναζωογόνηση — revival, revitalisation", "αναστρέψιμη": "αναστρέψιμος — reversible", "αντιστραφεί": "αντιστρέφομαι — to be reversed", "θύλακες": "θύλακας — pocket, enclave", "πατρικά τους κτήματα": "πατρικά κτήματα — family land, ancestral fields", "μεταποίηση": "μεταποίηση — (food) processing", "εξ αποστάσεως": "εξ αποστάσεως — remotely, at a distance", "υποδομές": "υποδομές — infrastructure", "εξοικονόμηση πόρων": "εξοικονόμηση πόρων — saving resources", "καταδίκη": "καταδίκη — conviction; death sentence, doom", "ύπαιθρο": "ύπαιθρος — countryside"},
})

ITEMS.append({
 "id": "l52-c1-kapodistrias", "title": "Ιωάννης Καποδίστριας", "title_en": "Ioannis Kapodistrias", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια ομιλία ενός ιστορικού για τον Ιωάννη Καποδίστρια, τον πρώτο κυβερνήτη της Ελλάδας.",
 "script": [
  L("Ιστορικός", "m", "Ο Ιωάννης Καποδίστριας γεννήθηκε στην Κέρκυρα το 1776, σε μια αριστοκρατική οικογένεια. Σπούδασε ιατρική στην Πάντοβα, αλλά πολύ γρήγορα στράφηκε στην πολιτική: υπηρέτησε την Επτάνησο Πολιτεία και, όταν τα νησιά πέρασαν στους Γάλλους, μπήκε στη διπλωματική υπηρεσία της Ρωσίας.", "Ioannis Kapodistrias was born in Corfu in 1776, into an aristocratic family. He studied medicine in Padua, but very soon turned to politics: he served the Septinsular Republic and, when the islands passed to the French, he joined the diplomatic service of Russia."),
  L("Ιστορικός", "m", "Εκεί η άνοδός του υπήρξε εντυπωσιακή. Στο Συνέδριο της Βιέννης συνέβαλε αποφασιστικά στη διαμόρφωση της ελβετικής ουδετερότητας, και από το 1816 μοιραζόταν τη θέση του υπουργού Εξωτερικών του τσάρου. Όταν ξέσπασε η Επανάσταση του 1821, βρέθηκε σε δύσκολη θέση: ως Έλληνας τη συμπαθούσε, ως υπουργός μιας δύναμης που υπερασπιζόταν την παλαιά τάξη δεν μπορούσε να τη στηρίξει ανοιχτά. Το 1822 αποχώρησε από την υπηρεσία.", "There his rise was spectacular. At the Congress of Vienna he contributed decisively to shaping Swiss neutrality, and from 1816 he shared the post of the tsar's foreign minister. When the Revolution of 1821 broke out, he found himself in a difficult position: as a Greek he sympathised with it, as minister of a power defending the old order he could not openly support it. In 1822 he withdrew from the service."),
  L("Ιστορικός", "m", "Το 1827 η Εθνοσυνέλευση της Τροιζήνας τον εξέλεξε κυβερνήτη, και τον Ιανουάριο του 1828 έφτασε σε μια χώρα κατεστραμμένη, χωρίς κράτος, χωρίς οικονομία. Μέσα σε τρία χρόνια ίδρυσε σχολεία και το Ορφανοτροφείο της Αίγινας, οργάνωσε τακτικό στρατό, κυκλοφόρησε το πρώτο εθνικό νόμισμα, τον φοίνικα. Η συγκεντρωτική του διακυβέρνηση, όμως, τον έφερε σε σύγκρουση με τους προκρίτους, τους Υδραίους πλοιοκτήτες και τους Μανιάτες.", "In 1827 the National Assembly of Troezen elected him governor, and in January 1828 he arrived in a devastated country, without a state, without an economy. Within three years he founded schools and the Aegina Orphanage, organised a regular army and issued the first national currency, the phoenix. His centralised government, however, brought him into conflict with the local notables, the shipowners of Hydra and the Maniots."),
  L("Ιστορικός", "m", "Στις 9 Οκτωβρίου 1831, έξω από τον ναό του Αγίου Σπυρίδωνα στο Ναύπλιο, δολοφονήθηκε από τον Κωνσταντίνο και τον Γεώργιο Μαυρομιχάλη. Μέχρι σήμερα, η αποτίμησή του διχάζει: για άλλους ήταν ο οραματιστής θεμελιωτής του κράτους, για άλλους ένας αυταρχικός ηγέτης που αγνόησε τις τοπικές ισορροπίες.", "On 9 October 1831, outside the church of Saint Spyridon in Nafplio, he was assassinated by Konstantinos and Georgios Mavromichalis. To this day, the assessment of him divides opinion: for some he was the visionary founder of the state, for others an authoritarian leader who ignored local balances of power."),
 ],
 "questions": [
  Q("Τι σπούδασε ο Καποδίστριας;", ["Νομικά στη Βιέννη", "Ιατρική στην Πάντοβα", "Φιλοσοφία στην Αγία Πετρούπολη", "Στρατιωτικά στο Παρίσι"], 1, "Σπούδασε ιατρική στην Πάντοβα"),
  Q("Γιατί βρέθηκε σε δύσκολη θέση το 1821;", ["Γιατί οι Έλληνες τον θεωρούσαν προδότη", "Γιατί ως Έλληνας συμπαθούσε την Επανάσταση, αλλά ως Ρώσος υπουργός δεν μπορούσε να τη στηρίξει ανοιχτά", "Γιατί ήταν άρρωστος", "Γιατί είχε συλληφθεί από τους Γάλλους"], 1, "ως Έλληνας τη συμπαθούσε, ως υπουργός μιας δύναμης που υπερασπιζόταν την παλαιά τάξη δεν μπορούσε να τη στηρίξει ανοιχτά"),
  Q("Ποιο από τα παρακάτω ΔΕΝ αναφέρεται ως έργο του ως κυβερνήτη;", ["Η ίδρυση του Ορφανοτροφείου της Αίγινας", "Η σύνταξη του πρώτου συντάγματος της Ελβετίας", "Η κυκλοφορία του φοίνικα", "Η οργάνωση τακτικού στρατού"], 1, "Η Ελβετία αναφέρεται για το Συνέδριο της Βιέννης, πριν γίνει κυβερνήτης· τα άλλα τρία αναφέρονται ως έργα του στην Ελλάδα"),
  Q("Τι λέει ο ιστορικός για τη σημερινή αποτίμηση του Καποδίστρια;", ["Ότι όλοι τον θεωρούν εθνικό ήρωα", "Ότι οι απόψεις διχάζονται ανάμεσα στον οραματιστή θεμελιωτή και τον αυταρχικό ηγέτη", "Ότι έχει ξεχαστεί", "Ότι τον θυμούνται κυρίως ως γιατρό"], 1, "η αποτίμησή του διχάζει: για άλλους ήταν ο οραματιστής θεμελιωτής του κράτους, για άλλους ένας αυταρχικός ηγέτης"),
 ],
 "gloss": {"κυβερνήτη": "κυβερνήτης — governor (head of state, 1828–1831)", "Επτάνησο Πολιτεία": "Επτάνησος Πολιτεία — the Septinsular Republic (Ionian Islands, 1800–1807)", "ουδετερότητας": "ουδετερότητα — neutrality", "παλαιά τάξη": "παλαιά τάξη — the old order", "Εθνοσυνέλευση": "εθνοσυνέλευση — national assembly", "Ορφανοτροφείο": "ορφανοτροφείο — orphanage", "φοίνικα": "φοίνικας — phoenix (first Greek currency, 1828)", "συγκεντρωτική": "συγκεντρωτικός — centralised", "προκρίτους": "πρόκριτος — local notable", "δολοφονήθηκε": "δολοφονούμαι — to be assassinated", "αποτίμησή": "αποτίμηση — assessment, appraisal", "διχάζει": "διχάζω — to divide (opinion)", "θεμελιωτής": "θεμελιωτής — founder"},
})

rnd = random.Random(52)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-52.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
