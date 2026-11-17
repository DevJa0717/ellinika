# Source for library/listening/listening-128.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l128.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l128-ann-roloi-dimarxeiou", "title": "Σιωπή στο ρολόι του δημαρχείου", "title_en": "Silence from the town hall clock", "type": "announcement", "level": "B2",
 "context_el": "Μένετε στο κέντρο μιας επαρχιακής πόλης. Ακούτε μια ανακοίνωση του δήμου από το τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Ο Δήμος ενημερώνει τους κατοίκους ότι από τη Δευτέρα το ιστορικό ρολόι του δημαρχείου θα σταματήσει να λειτουργεί για περίπου έξι εβδομάδες. Ο μηχανισμός του, που κατασκευάστηκε στις αρχές του περασμένου αιώνα, θα αποσυναρμολογηθεί και θα μεταφερθεί σε ειδικό εργαστήριο για συντήρηση.", "The Municipality informs residents that from Monday the historic town hall clock will stop working for about six weeks. Its mechanism, built at the beginning of the last century, will be dismantled and taken to a specialist workshop for maintenance."),
  L("Εκφωνητής", "m", "Κατά τη διάρκεια των εργασιών η καμπάνα δεν θα χτυπά τις ώρες. Επίσης, το πεζοδρόμιο μπροστά στην κεντρική είσοδο θα είναι κλειστό, και οι πολίτες που έχουν δουλειά στο δημαρχείο θα εξυπηρετούνται από την πλαϊνή είσοδο, στην οδό Ερμού.", "While the work is going on, the bell will not strike the hours. The pavement in front of the main entrance will also be closed, and citizens with business at the town hall will be served at the side entrance, on Ermou Street."),
  L("Εκφωνητής", "m", "Όσοι έχουν παλιές φωτογραφίες του ρολογιού καλούνται να τις φέρουν στο γραφείο πολιτισμού. Θα χρησιμοποιηθούν σε μια μικρή έκθεση για την ιστορία του, που θα εγκαινιαστεί μαζί με την επαναλειτουργία του.", "Anyone who has old photographs of the clock is invited to bring them to the culture office. They will be used in a small exhibition about its history, which will open when the clock starts working again."),
 ],
 "questions": [
  Q("Γιατί θα σταματήσει το ρολόι;", ["Γιατί θα αντικατασταθεί με ψηφιακό", "Γιατί ο μηχανισμός του θα συντηρηθεί σε ειδικό εργαστήριο", "Γιατί ενοχλούσε τους κατοίκους", "Γιατί θα βαφτεί το δημαρχείο"], 1, "θα μεταφερθεί σε ειδικό εργαστήριο για συντήρηση"),
  Q("Από πού θα εξυπηρετούνται οι πολίτες;", ["Από το γραφείο πολιτισμού", "Από ένα κοντινό σχολείο", "Από την πλαϊνή είσοδο, στην οδό Ερμού", "Μόνο ηλεκτρονικά"], 2, "θα εξυπηρετούνται από την πλαϊνή είσοδο, στην οδό Ερμού"),
  Q("Τι ζητά ο δήμος από τους κατοίκους;", ["Να φέρουν παλιές φωτογραφίες του ρολογιού", "Να δώσουν χρήματα για την επισκευή", "Να μην παρκάρουν στο κέντρο", "Να ψηφίσουν για το χρώμα του ρολογιού"], 0, "Όσοι έχουν παλιές φωτογραφίες του ρολογιού καλούνται να τις φέρουν στο γραφείο πολιτισμού"),
 ],
 "gloss": {"μηχανισμός": "μηχανισμός — mechanism", "αποσυναρμολογηθεί": "αποσυναρμολογώ — to dismantle", "συντήρηση": "συντήρηση — maintenance", "καμπάνα": "καμπάνα — bell", "πεζοδρόμιο": "πεζοδρόμιο — pavement", "εξυπηρετούνται": "εξυπηρετούμαι — to be served", "πλαϊνή": "πλαϊνός — side (adj.)", "έκθεση": "έκθεση — exhibition", "εγκαινιαστεί": "εγκαινιάζω — to open, inaugurate", "επαναλειτουργία": "επαναλειτουργία — reopening, resumed operation"}
})

ITEMS.append({
 "id": "l128-vm-geoponos-lemonia", "title": "Μήνυμα από τον γεωπόνο για τη λεμονιά", "title_en": "A message from the agronomist about the lemon tree", "type": "voicemail", "level": "B2",
 "context_el": "Η λεμονιά στην αυλή σας έχει πρόβλημα και ζητήσατε τη γνώμη ενός γεωπόνου. Ακούτε το μήνυμά του στον τηλεφωνητή.",
 "script": [
  L("Γεωπόνος", "m", "Καλημέρα, ο Νίκος Βλάχος είμαι, ο γεωπόνος. Είδα τις φωτογραφίες που μου στείλατε. Τα κολλώδη φύλλα και η μαύρη σκόνη πάνω τους δείχνουν ότι η λεμονιά σας έχει κοκκοειδή, ένα μικρό έντομο που ρουφάει τους χυμούς του φυτού. Δεν είναι κάτι σοβαρό, αν το αντιμετωπίσουμε έγκαιρα.", "Good morning, it's Nikos Vlachos, the agronomist. I saw the photos you sent me. The sticky leaves and the black dust on them show that your lemon tree has scale insects, a small insect that sucks the plant's sap. It's nothing serious if we deal with it in time."),
  L("Γεωπόνος", "m", "Δεν χρειάζονται ισχυρά φάρμακα. Ψεκάστε το δέντρο με θερινό λάδι, νωρίς το πρωί ή αργά το απόγευμα, ποτέ με δυνατό ήλιο, γιατί καίγονται τα φύλλα. Κόψτε επίσης τα κλαδιά που είναι πολύ πυκνά, για να αερίζεται το εσωτερικό του δέντρου.", "No strong chemicals are needed. Spray the tree with summer oil, early in the morning or late in the afternoon, never in strong sun, because the leaves get burnt. Also cut the branches that are too dense, so that the inside of the tree gets air."),
  L("Γεωπόνος", "m", "Θα περάσω από εκεί την επόμενη Πέμπτη, γύρω στις δέκα, να δω πώς πάει. Αν δεν είστε σπίτι, αφήστε μου ανοιχτή την πόρτα της αυλής. Γεια σας.", "I'll drop by next Thursday, around ten, to see how it's going. If you're not at home, leave the yard door open for me. Goodbye."),
 ],
 "questions": [
  Q("Τι πρόβλημα έχει η λεμονιά;", ["Της λείπει νερό", "Έχει κοκκοειδή, ένα έντομο που ρουφάει τους χυμούς της", "Έχει πάθει ζημιά από τον παγετό", "Είναι πολύ γέρικη"], 1, "η λεμονιά σας έχει κοκκοειδή"),
  Q("Πότε πρέπει να γίνει ο ψεκασμός;", ["Το μεσημέρι", "Μόνο όταν βρέχει", "Νωρίς το πρωί ή αργά το απόγευμα", "Τη νύχτα"], 2, "νωρίς το πρωί ή αργά το απόγευμα"),
  Q("Τι ζητά ο γεωπόνος, αν δεν είναι κανείς σπίτι;", ["Να του αφήσουν ανοιχτή την πόρτα της αυλής", "Να του τηλεφωνήσουν", "Να αφήσουν το κλειδί στον γείτονα", "Να αλλάξουν τη μέρα"], 0, "αφήστε μου ανοιχτή την πόρτα της αυλής"),
 ],
 "gloss": {"λεμονιά": "λεμονιά — lemon tree", "γεωπόνου": "γεωπόνος — agronomist", "κολλώδη": "κολλώδης — sticky", "κοκκοειδή": "κοκκοειδή — scale insects", "ρουφάει": "ρουφάω — to suck", "χυμούς": "χυμός — juice; (of plants) sap", "έγκαιρα": "έγκαιρα — in time", "Ψεκάστε": "ψεκάζω — to spray", "θερινό λάδι": "θερινό λάδι — summer (horticultural) oil", "κλαδιά": "κλαδί — branch", "αερίζεται": "αερίζομαι — to get air, be ventilated"}
})

ITEMS.append({
 "id": "l128-dial-party-trampolino", "title": "Πάρτι στα τραμπολίνο ή στην αυλή;", "title_en": "A party at the trampoline park or in the yard?", "type": "dialogue", "level": "B2",
 "context_el": "Η Ρένα και ο Θοδωρής οργανώνουν τα γενέθλια της κόρης τους, της Ιφιγένειας, που κλείνει τα οκτώ.",
 "script": [
  L("Ρένα", "f", "Θοδωρή, πρέπει να αποφασίσουμε για το πάρτι της Ιφιγένειας. Εκείνη θέλει οπωσδήποτε να το κάνει στο καινούργιο πάρκο με τα τραμπολίνο, όπως έκαναν και δύο συμμαθητές της.", "Thodoris, we need to decide about Ifigeneia's party. She absolutely wants to have it at the new trampoline park, as two of her classmates did."),
  L("Θοδωρής", "m", "Το είδα στο διαδίκτυο. Είναι σχεδόν είκοσι ευρώ το παιδί, και θέλει να καλέσει όλη την τάξη, είκοσι τέσσερα παιδιά. Δεν είναι λίγα. Και φοβάμαι λίγο και για τραυματισμούς.", "I saw it online. It's almost twenty euros per child, and she wants to invite the whole class, twenty-four children. That's not cheap. And I'm a bit worried about injuries too."),
  L("Ρένα", "f", "Για την ασφάλεια ρώτησα: έχουν εκπαιδευμένους επόπτες και δεν αφήνουν πάνω από έξι παιδιά σε κάθε τραμπολίνο. Για το κόστος όμως έχεις δίκιο. Τι λες να το κάνουμε στο σπίτι, με παιχνίδια στην αυλή;", "I asked about safety: they have trained supervisors and don't allow more than six children on each trampoline. But you're right about the cost. What do you say we do it at home, with games in the yard?"),
  L("Θοδωρής", "m", "Στην αυλή δεν χωράνε είκοσι τέσσερα παιδιά. Προτείνω κάτι ενδιάμεσο: το πάρκο, αλλά μόνο με τους πιο στενούς της φίλους, οκτώ παιδιά, και για την τάξη να στείλουμε μια τούρτα στο σχολείο.", "Twenty-four children won't fit in the yard. I suggest something in between: the park, but only with her closest friends, eight children, and for the class we send a cake to school."),
 ],
 "questions": [
  Q("Γιατί θέλει η Ιφιγένεια το πάρκο με τα τραμπολίνο;", ["Γιατί είναι κοντά στο σπίτι", "Γιατί έκαναν εκεί πάρτι και δύο συμμαθητές της", "Γιατί είναι δωρεάν", "Γιατί το πρότεινε η δασκάλα"], 1, "όπως έκαναν και δύο συμμαθητές της"),
  Q("Τι ανησυχεί τον Θοδωρή;", ["Ο καιρός", "Η απόσταση", "Το κόστος και οι τραυματισμοί", "Ο θόρυβος"], 2, "φοβάμαι λίγο και για τραυματισμούς"),
  Q("Τι προτείνει τελικά ο Θοδωρής;", ["Πάρκο με οκτώ στενούς φίλους και τούρτα για την τάξη στο σχολείο", "Πάρτι στην αυλή για όλη την τάξη", "Να αναβληθεί το πάρτι", "Να πληρώσουν οι γονείς των φίλων"], 0, "το πάρκο, αλλά μόνο με τους πιο στενούς της φίλους"),
 ],
 "gloss": {"τραμπολίνο": "τραμπολίνο — trampoline", "συμμαθητές": "συμμαθητής — classmate", "διαδίκτυο": "διαδίκτυο — internet", "τραυματισμούς": "τραυματισμός — injury", "εκπαιδευμένους": "εκπαιδευμένος — trained", "επόπτες": "επόπτης — supervisor", "κόστος": "κόστος — cost", "ενδιάμεσο": "ενδιάμεσος — in between, intermediate", "στενούς": "στενός φίλος — close friend", "τούρτα": "τούρτα — (birthday) cake"}
})

ITEMS.append({
 "id": "l128-int-archeio-dimou", "title": "Η φύλακας της μνήμης της πόλης", "title_en": "The keeper of the town's memory", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη στο τοπικό ραδιόφωνο με την υπεύθυνη του ιστορικού αρχείου του δήμου.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Σαββίδου, τι ακριβώς φυλάσσεται σε ένα δημοτικό αρχείο;", "Ms Savvidou, what exactly is kept in a municipal archive?"),
  L("Αρχειονόμος", "f", "Σχεδόν τα πάντα για την καθημερινή ζωή της πόλης εδώ και διακόσια χρόνια: πρακτικά του δημοτικού συμβουλίου, άδειες για καταστήματα, σχέδια κτιρίων, ακόμη και επιστολές πολιτών με παράπονα για τον φωτισμό των δρόμων. Για τους ιστορικούς είναι θησαυρός.", "Almost everything about the daily life of the town over the last two hundred years: minutes of the town council, licences for shops, building plans, even letters from citizens complaining about the street lighting. For historians it's a treasure."),
  L("Δημοσιογράφος", "m", "Ποιος έρχεται να τα συμβουλευτεί;", "Who comes to consult them?"),
  L("Αρχειονόμος", "f", "Περισσότεροι απ' όσους φαντάζεστε, και όχι μόνο ερευνητές. Πολλοί έρχονται για να βρουν τις ρίζες της οικογένειάς τους ή επειδή χρειάζονται το παλιό σχέδιο του σπιτιού τους για μια πολεοδομική υπόθεση.", "More people than you'd imagine, and not only researchers. Many come to find their family roots, or because they need the old plan of their house for a planning case."),
  L("Δημοσιογράφος", "m", "Και ποια είναι η μεγαλύτερη πρόκληση;", "And what is the biggest challenge?"),
  L("Αρχειονόμος", "f", "Η υγρασία, χωρίς αμφιβολία. Πολλά έγγραφα έμειναν για χρόνια σε υπόγεια. Τώρα τα ψηφιοποιούμε σιγά σιγά, ώστε το κοινό να μπορεί να τα βλέπει στην οθόνη χωρίς να πιάνει στα χέρια του τα πρωτότυπα.", "Damp, without a doubt. Many documents stayed in basements for years. Now we're digitising them little by little, so that the public can see them on screen without handling the originals."),
 ],
 "questions": [
  Q("Τι είδους έγγραφα υπάρχουν στο αρχείο;", ["Μόνο βιβλία λογοτεχνίας", "Πρακτικά του δημοτικού συμβουλίου, άδειες, σχέδια κτιρίων και επιστολές πολιτών", "Μόνο φωτογραφίες", "Μόνο δικαστικές αποφάσεις"], 1, "πρακτικά του δημοτικού συμβουλίου, άδειες για καταστήματα, σχέδια κτιρίων"),
  Q("Γιατί έρχονται στο αρχείο πολλοί απλοί πολίτες;", ["Για να δανειστούν βιβλία", "Για να δουλέψουν εθελοντικά", "Για να βρουν τις ρίζες της οικογένειάς τους ή το σχέδιο του σπιτιού τους", "Για να πληρώσουν λογαριασμούς"], 2, "Πολλοί έρχονται για να βρουν τις ρίζες της οικογένειάς τους"),
  Q("Γιατί ψηφιοποιούνται τα έγγραφα;", ["Για να βλέπει το κοινό τα έγγραφα στην οθόνη χωρίς να αγγίζει τα πρωτότυπα", "Για να πουληθούν τα πρωτότυπα", "Για να μη χρειάζεται πια αρχειονόμος", "Γιατί το κτίριο θα κλείσει"], 0, "ώστε το κοινό να μπορεί να τα βλέπει στην οθόνη"),
 ],
 "gloss": {"αρχείου": "αρχείο — archive", "φυλάσσεται": "φυλάσσομαι — to be kept", "πρακτικά": "πρακτικά — minutes (of a meeting)", "δημοτικού συμβουλίου": "δημοτικό συμβούλιο — town council", "άδειες": "άδεια — licence, permit", "παράπονα": "παράπονο — complaint", "φωτισμό": "φωτισμός — lighting", "θησαυρός": "θησαυρός — treasure", "συμβουλευτεί": "συμβουλεύομαι — to consult", "ρίζες": "ρίζα — root", "πολεοδομική": "πολεοδομικός — town-planning (adj.)", "υγρασία": "υγρασία — damp, humidity", "υπόγεια": "υπόγειο — basement", "ψηφιοποιούμε": "ψηφιοποιώ — to digitise", "πρωτότυπα": "πρωτότυπο — original"}
})

ITEMS.append({
 "id": "l128-rep-gala-automato", "title": "Φρέσκο γάλα από τον αυτόματο πωλητή", "title_en": "Fresh milk from a vending machine", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από μια περιφερειακή ειδησεογραφική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Στην πλατεία ενός χωριού της Θεσσαλίας, δίπλα στο καφενείο, υπάρχει από την άνοιξη ένα ασυνήθιστο μηχάνημα: ένας αυτόματος πωλητής φρέσκου γάλακτος. Τον τοποθέτησαν δύο αδέλφια κτηνοτρόφοι, που έχουν μια μικρή φάρμα με σαράντα αγελάδες λίγα χιλιόμετρα έξω από το χωριό.", "In the square of a village in Thessaly, next to the café, there has been an unusual machine since the spring: a fresh-milk vending machine. It was put there by two brothers who are livestock farmers and have a small farm with forty cows a few kilometres outside the village."),
  L("Κτηνοτρόφος", "m", "Οι γαλακτοβιομηχανίες μάς πλήρωναν πολύ χαμηλή τιμή, ενώ στο σούπερ μάρκετ το γάλα πουλιόταν ακριβά. Σκεφτήκαμε να το πουλάμε κατευθείαν στον κόσμο. Το γεμίζουμε κάθε πρωί, και ό,τι δεν πουληθεί μέσα σε είκοσι τέσσερις ώρες το αποσύρουμε.", "The dairy companies paid us a very low price, while in the supermarket milk was sold at a high price. We thought of selling it directly to people. We fill it every morning, and whatever isn't sold within twenty-four hours we take out."),
  L("Ρεπόρτερ", "f", "Οι πελάτες φέρνουν το δικό τους γυάλινο μπουκάλι ή αγοράζουν ένα από το διπλανό μηχάνημα. Οι κτηνοτρόφοι τους συμβουλεύουν να βράζουν το γάλα πριν το πιουν, γιατί δεν είναι παστεριωμένο. Η επιτυχία ήταν τέτοια, ώστε σκέφτονται να βάλουν ακόμη έναν πωλητή στην κοντινή πόλη.", "Customers bring their own glass bottle or buy one from the machine next to it. The farmers advise them to boil the milk before drinking it, because it isn't pasteurised. The success has been such that they're thinking of putting another machine in the nearby town."),
 ],
 "questions": [
  Q("Γιατί αποφάσισαν τα αδέλφια να πουλάνε το γάλα απευθείας;", ["Γιατί έκλεισε το σούπερ μάρκετ", "Γιατί οι γαλακτοβιομηχανίες πλήρωναν πολύ χαμηλή τιμή", "Γιατί τους το ζήτησε ο δήμος", "Γιατί τους περίσσευε γάλα το καλοκαίρι"], 1, "Οι γαλακτοβιομηχανίες μάς πλήρωναν πολύ χαμηλή τιμή"),
  Q("Τι γίνεται με το γάλα που δεν πουλιέται μέσα σε μία μέρα;", ["Το δίνουν στο καφενείο", "Γίνεται τυρί", "Το αποσύρουν", "Πουλιέται σε χαμηλότερη τιμή"], 2, "ό,τι δεν πουληθεί μέσα σε είκοσι τέσσερις ώρες το αποσύρουμε"),
  Q("Τι συμβουλεύουν οι κτηνοτρόφοι τους πελάτες;", ["Να βράζουν το γάλα πριν το πιουν", "Να το πίνουν αμέσως", "Να το βάζουν στην κατάψυξη", "Να το αραιώνουν με νερό"], 0, "να βράζουν το γάλα πριν το πιουν"),
 ],
 "gloss": {"ασυνήθιστο": "ασυνήθιστος — unusual", "μηχάνημα": "μηχάνημα — machine", "αυτόματος πωλητής": "αυτόματος πωλητής — vending machine", "κτηνοτρόφοι": "κτηνοτρόφος — livestock farmer", "φάρμα": "φάρμα — farm", "αγελάδες": "αγελάδα — cow", "γαλακτοβιομηχανίες": "γαλακτοβιομηχανία — dairy company", "κατευθείαν": "κατευθείαν — directly", "αποσύρουμε": "αποσύρω — to withdraw, take off sale", "γυάλινο": "γυάλινος — glass (adj.)", "βράζουν": "βράζω — to boil", "παστεριωμένο": "παστεριωμένος — pasteurised"}
})

ITEMS.append({
 "id": "l128-rep-scholeio-treis-mathites", "title": "Ένα σχολείο με τρεις μαθητές", "title_en": "A school with three pupils", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα μικρό σχολείο σε ορεινό χωριό της Ηπείρου.",
 "script": [
  L("Ρεπόρτερ", "m", "Το δημοτικό σχολείο του χωριού έχει φέτος μόλις τρεις μαθητές: δύο αδέλφια, της πρώτης και της τέταρτης τάξης, και ένα κορίτσι της έκτης. Τους διδάσκει μία δασκάλα, που ταξιδεύει κάθε μέρα σαράντα λεπτά από την πόλη μέσα από στενούς ορεινούς δρόμους.", "This year the village primary school has only three pupils: two siblings, in the first and fourth year, and a girl in the sixth. They're taught by one teacher, who travels forty minutes every day from the town along narrow mountain roads."),
  L("Δασκάλα", "f", "Στην αρχή αναρωτιόμουν πώς θα κάνω μάθημα σε τρεις διαφορετικές τάξεις ταυτόχρονα. Τελικά τα μεγαλύτερα παιδιά βοηθούν το μικρό, και αυτό τους κάνει καλό: μαθαίνουν να εξηγούν και να έχουν υπομονή. Κάθε Παρασκευή, επίσης, κάνουμε μάθημα μέσω βιντεοκλήσης με ένα σχολείο της Αθήνας.", "At first I wondered how I would teach three different years at the same time. In the end the older children help the little one, and that does them good: they learn to explain and to be patient. Also, every Friday we have a lesson by video call with a school in Athens."),
  L("Ρεπόρτερ", "m", "Για τους κατοίκους το σχολείο είναι κάτι παραπάνω από ένα κτίριο. Όπως λένε, αν κλείσει, οι οικογένειες θα φύγουν και το χωριό θα αδειάσει. Γι' αυτό ο σύλλογος του χωριού προσφέρει δωρεάν σπίτι σε όποια νέα οικογένεια με παιδιά εγκατασταθεί εκεί.", "For the residents the school is more than a building. As they say, if it closes, families will leave and the village will empty. That's why the village association offers a free house to any new family with children that settles there."),
 ],
 "questions": [
  Q("Τι ανησυχούσε τη δασκάλα στην αρχή;", ["Η έλλειψη βιβλίων", "Το μάθημα σε τρεις διαφορετικές τάξεις ταυτόχρονα", "Το κρύο στο σχολείο", "Οι γονείς των μαθητών"], 1, "πώς θα κάνω μάθημα σε τρεις διαφορετικές τάξεις ταυτόχρονα"),
  Q("Τι κάνουν τα παιδιά κάθε Παρασκευή;", ["Πάνε εκδρομή στην πόλη", "Παίζουν θέατρο", "Κάνουν μάθημα μέσω βιντεοκλήσης με ένα σχολείο της Αθήνας", "Δεν έχουν σχολείο"], 2, "κάνουμε μάθημα μέσω βιντεοκλήσης με ένα σχολείο της Αθήνας"),
  Q("Τι προσφέρει ο σύλλογος του χωριού;", ["Δωρεάν σπίτι σε νέες οικογένειες με παιδιά", "Υποτροφίες στους μαθητές", "Ένα σχολικό λεωφορείο", "Δωρεάν γεύματα"], 0, "προσφέρει δωρεάν σπίτι σε όποια νέα οικογένεια με παιδιά"),
 ],
 "gloss": {"ορεινό": "ορεινός — mountain (adj.)", "δημοτικό σχολείο": "δημοτικό σχολείο — primary school", "διδάσκει": "διδάσκω — to teach", "αναρωτιόμουν": "αναρωτιέμαι — to wonder", "ταυτόχρονα": "ταυτόχρονα — at the same time", "υπομονή": "υπομονή — patience", "βιντεοκλήσης": "βιντεοκλήση — video call", "κατοίκους": "κάτοικος — resident", "αδειάσει": "αδειάζω — to empty", "σύλλογος": "σύλλογος — association, club", "εγκατασταθεί": "εγκαθίσταμαι — to settle"}
})

ITEMS.append({
 "id": "l128-mono-iaponika", "title": "Ιαπωνικά στα σαράντα", "title_en": "Japanese at forty", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλά σε ένα πόντκαστ για το πώς άρχισε να μαθαίνει ιαπωνικά.",
 "script": [
  L("Ευαγγελία", "f", "Όταν έκλεισα τα σαράντα, αποφάσισα να κάνω κάτι εντελώς καινούργιο για μένα. Από παιδί αγαπούσα τα ιαπωνικά κινούμενα σχέδια, και έτσι γράφτηκα σε ένα τμήμα ιαπωνικών, δύο βράδια την εβδομάδα. Οι φίλοι μου γελούσαν: «Τι θα τα κάνεις;» μου έλεγαν.", "When I turned forty, I decided to do something completely new for me. I'd loved Japanese cartoons since I was a child, so I signed up for a Japanese class, two evenings a week. My friends laughed: 'What will you do with it?' they'd say."),
  L("Ευαγγελία", "f", "Τον πρώτο χρόνο σκέφτηκα πολλές φορές να τα παρατήσω. Το πιο δύσκολο δεν ήταν η προφορά, που σε αρκετά σημεία θυμίζει τα ελληνικά, αλλά η γραφή: υπάρχουν τρία διαφορετικά συστήματα, και χιλιάδες ιδεογράμματα. Έγραφα καρτέλες και τις κολλούσα παντού, ακόμα και στον καθρέφτη του μπάνιου.", "In the first year I thought many times about giving up. The hardest thing wasn't the pronunciation, which in quite a few ways is like Greek, but the writing: there are three different systems, and thousands of characters. I wrote flashcards and stuck them everywhere, even on the bathroom mirror."),
  L("Ευαγγελία", "f", "Πέρσι έκανα το πρώτο μου ταξίδι στην Ιαπωνία. Σε ένα μικρό εστιατόριο στο Κιότο παρήγγειλα στα ιαπωνικά, και ο ιδιοκτήτης μού χαμογέλασε και μου έφερε δωρεάν ένα γλυκό. Εκείνη τη στιγμή κατάλαβα ότι όλος ο κόπος άξιζε.", "Last year I made my first trip to Japan. In a small restaurant in Kyoto I ordered in Japanese, and the owner smiled at me and brought me a dessert for free. At that moment I knew all the effort had been worth it."),
 ],
 "questions": [
  Q("Γιατί άρχισε να μαθαίνει ιαπωνικά;", ["Για τη δουλειά της", "Γιατί από παιδί αγαπούσε τα ιαπωνικά κινούμενα σχέδια", "Γιατί παντρεύτηκε έναν Ιάπωνα", "Γιατί της το πρότειναν οι φίλοι της"], 1, "Από παιδί αγαπούσα τα ιαπωνικά κινούμενα σχέδια"),
  Q("Τι ήταν το πιο δύσκολο;", ["Η προφορά", "Η γραμματική", "Η γραφή, με τρία συστήματα και χιλιάδες ιδεογράμματα", "Η έλλειψη χρόνου"], 2, "υπάρχουν τρία διαφορετικά συστήματα, και χιλιάδες ιδεογράμματα"),
  Q("Τι έγινε στο εστιατόριο στο Κιότο;", ["Ο ιδιοκτήτης τής χαμογέλασε και της έφερε δωρεάν ένα γλυκό", "Δεν την κατάλαβαν", "Πλήρωσε πολύ ακριβά", "Γνώρισε μια Ελληνίδα"], 0, "ο ιδιοκτήτης μού χαμογέλασε και μου έφερε δωρεάν ένα γλυκό"),
 ],
 "gloss": {"κινούμενα σχέδια": "κινούμενα σχέδια — cartoons, animation", "τμήμα": "τμήμα — class (group of learners)", "παρατήσω": "παρατάω — to give up", "προφορά": "προφορά — pronunciation", "γραφή": "γραφή — writing (system)", "ιδεογράμματα": "ιδεόγραμμα — ideogram, character", "καρτέλες": "καρτέλα — card, flashcard", "καθρέφτη": "καθρέφτης — mirror", "παρήγγειλα": "παραγγέλνω — to order", "κόπος": "κόπος — effort, trouble", "άξιζε": "αξίζει — it is worth it"}
})

ITEMS.append({
 "id": "l128-mono-skylos-proi", "title": "Ο σκύλος που με έκανε πρωινό τύπο", "title_en": "The dog that made me a morning person", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλά σε μια ραδιοφωνική εκπομπή για το πώς άλλαξε η καθημερινότητά του.",
 "script": [
  L("Μανώλης", "m", "Για χρόνια ήμουν άνθρωπος της νύχτας. Δούλευα ως γραφίστας από το σπίτι, κοιμόμουν στις τρεις και ξυπνούσα στις έντεκα. Όλα άλλαξαν όταν υιοθέτησα τον Μπέμπη, ένα κουτάβι από ένα καταφύγιο.", "For years I was a night owl. I worked as a graphic designer from home, went to sleep at three and woke up at eleven. Everything changed when I adopted Bebis, a puppy from a shelter."),
  L("Μανώλης", "m", "Ο Μπέμπης είχε το δικό του πρόγραμμα: στις επτά το πρωί καθόταν δίπλα στο κρεβάτι και γάβγιζε μέχρι να σηκωθώ. Τις πρώτες εβδομάδες ήμουν σαν ζόμπι. Σιγά σιγά όμως άρχισα να πέφτω για ύπνο νωρίτερα, γιατί απλώς δεν άντεχα.", "Bebis had his own schedule: at seven in the morning he'd sit next to the bed and bark until I got up. For the first few weeks I was like a zombie. But little by little I started going to bed earlier, simply because I couldn't keep going."),
  L("Μανώλης", "m", "Σήμερα, δύο χρόνια μετά, ξυπνάω χωρίς ξυπνητήρι. Η πρωινή βόλτα στο πάρκο είναι η αγαπημένη μου ώρα: γνώρισα άλλους ιδιοκτήτες σκύλων και έχουμε κάνει παρέα. Και το πιο περίεργο: δουλεύω καλύτερα το πρωί από ό,τι δούλευα ποτέ τη νύχτα.", "Today, two years later, I wake up without an alarm clock. The morning walk in the park is my favourite time: I've met other dog owners and we've become friends. And the strangest thing: I work better in the morning than I ever did at night."),
 ],
 "questions": [
  Q("Πώς ζούσε ο Μανώλης πριν από τον σκύλο;", ["Δούλευε σε γραφείο από τις εννιά", "Κοιμόταν στις τρεις και ξυπνούσε στις έντεκα", "Ξυπνούσε πολύ νωρίς", "Ταξίδευε συνέχεια"], 1, "κοιμόμουν στις τρεις και ξυπνούσα στις έντεκα"),
  Q("Τι έκανε ο Μπέμπης στις επτά το πρωί;", ["Κοιμόταν", "Έτρωγε", "Καθόταν δίπλα στο κρεβάτι και γάβγιζε", "Έβγαινε μόνος του στην αυλή"], 2, "καθόταν δίπλα στο κρεβάτι και γάβγιζε"),
  Q("Τι λέει ο Μανώλης για τη δουλειά του σήμερα;", ["Δουλεύει καλύτερα το πρωί απ' ό,τι δούλευε τη νύχτα", "Την άφησε", "Δουλεύει λιγότερες ώρες", "Δουλεύει πια σε γραφείο"], 0, "δουλεύω καλύτερα το πρωί από ό,τι δούλευα ποτέ τη νύχτα"),
 ],
 "gloss": {"καθημερινότητά": "καθημερινότητα — daily life, routine", "γραφίστας": "γραφίστας — graphic designer", "υιοθέτησα": "υιοθετώ — to adopt", "κουτάβι": "κουτάβι — puppy", "καταφύγιο": "καταφύγιο — (animal) shelter", "γάβγιζε": "γαβγίζω — to bark", "ζόμπι": "ζόμπι — zombie", "άντεχα": "αντέχω — to bear, keep going", "ξυπνητήρι": "ξυπνητήρι — alarm clock", "ιδιοκτήτες": "ιδιοκτήτης — owner", "παρέα": "κάνω παρέα — to hang out, become friends"}
})

ITEMS.append({
 "id": "l128-c1-peltzman", "title": "Όταν η ασφάλεια μάς κάνει απρόσεκτους", "title_en": "When safety makes us careless", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη για την ψυχολογία του κινδύνου.",
 "script": [
  L("Ομιλήτρια", "f", "Το 1975 ο Αμερικανός οικονομολόγος Σαμ Πέλτσμαν δημοσίευσε μια μελέτη που προκάλεσε μεγάλη αντιπαράθεση. Εξέτασε τους νόμους που είχαν κάνει υποχρεωτικές τις ζώνες ασφαλείας και άλλα μέτρα στα αυτοκίνητα, και υποστήριξε ότι δεν είχαν μειώσει τόσο όσο αναμενόταν τους θανάτους στους δρόμους.", "In 1975 the American economist Sam Peltzman published a study that caused a great controversy. He examined the laws that had made seat belts and other measures in cars compulsory, and argued that they had not reduced road deaths as much as expected."),
  L("Ομιλήτρια", "f", "Η εξήγησή του ήταν ότι οι οδηγοί, νιώθοντας πιο ασφαλείς, οδηγούσαν πιο επιθετικά, με αποτέλεσμα να κινδυνεύουν περισσότερο οι πεζοί και οι ποδηλάτες. Το φαινόμενο αυτό έγινε γνωστό ως «φαινόμενο Πέλτσμαν» ή, γενικότερα, ως αντιστάθμιση του κινδύνου: όταν κάτι μας προστατεύει, τείνουμε να παίρνουμε μεγαλύτερα ρίσκα.", "His explanation was that drivers, feeling safer, drove more aggressively, so that pedestrians and cyclists were put at greater risk. The phenomenon became known as the 'Peltzman effect' or, more generally, as risk compensation: when something protects us, we tend to take bigger risks."),
  L("Ομιλήτρια", "f", "Θα ήταν όμως λάθος να συμπεράνουμε ότι οι ζώνες ασφαλείας είναι άχρηστες. Οι περισσότερες μεταγενέστερες έρευνες έδειξαν ότι η αντιστάθμιση υπάρχει, αλλά συνήθως είναι μικρή, και το συνολικό όφελος από τα μέτρα ασφαλείας παραμένει σαφές. Το ζήτημα δεν είναι αν θα τα εφαρμόσουμε, αλλά πώς.", "It would be wrong, however, to conclude that seat belts are useless. Most later research showed that compensation exists but is usually small, and the overall benefit of safety measures remains clear. The question is not whether to apply them, but how."),
  L("Ομιλήτρια", "f", "Τι σημαίνει αυτό στην πράξη; Ότι η τεχνολογία δεν αρκεί. Ένα αυτοκίνητο με τα πιο σύγχρονα συστήματα υποβοήθησης δεν προστατεύει κανέναν, αν ο οδηγός τα αντιμετωπίζει ως άδεια για απροσεξία. Η ενημέρωση και η καλλιέργεια της υπευθυνότητας είναι εξίσου σημαντικές με τις μηχανές.", "What does this mean in practice? That technology is not enough. A car with the most modern driver-assistance systems protects no one if the driver treats them as a licence to be careless. Information and fostering a sense of responsibility are just as important as the machines."),
 ],
 "questions": [
  Q("Τι υποστήριξε ο Πέλτσμαν στη μελέτη του;", ["Ότι οι ζώνες ασφαλείας ήταν επικίνδυνες", "Ότι τα μέτρα ασφαλείας δεν είχαν μειώσει τους θανάτους τόσο όσο αναμενόταν", "Ότι έπρεπε να απαγορευτούν τα γρήγορα αυτοκίνητα", "Ότι οι πεζοί ήταν υπεύθυνοι για τα ατυχήματα"], 1, "δεν είχαν μειώσει τόσο όσο αναμενόταν τους θανάτους στους δρόμους"),
  Q("Πώς εξήγησε το φαινόμενο;", ["Τα αυτοκίνητα ήταν χαμηλής ποιότητας", "Οι δρόμοι ήταν σε κακή κατάσταση", "Οι οδηγοί, νιώθοντας πιο ασφαλείς, οδηγούσαν πιο επιθετικά", "Οι νόμοι δεν εφαρμόζονταν"], 2, "οι οδηγοί, νιώθοντας πιο ασφαλείς, οδηγούσαν πιο επιθετικά"),
  Q("Τι έδειξαν οι μεταγενέστερες έρευνες;", ["Ότι η αντιστάθμιση είναι συνήθως μικρή και το όφελος των μέτρων σαφές", "Ότι ο Πέλτσμαν είχε απόλυτο δίκιο", "Ότι το φαινόμενο δεν υπάρχει καθόλου", "Ότι οι ζώνες αυξάνουν τους θανάτους"], 0, "η αντιστάθμιση υπάρχει, αλλά συνήθως είναι μικρή"),
  Q("Ποιο είναι το συμπέρασμα της ομιλήτριας;", ["Να καταργηθούν τα συστήματα υποβοήθησης", "Η τεχνολογία δεν αρκεί· χρειάζονται επίσης ενημέρωση και υπευθυνότητα", "Οι οδηγοί πρέπει να πληρώνουν μεγαλύτερα πρόστιμα", "Τα αυτοκίνητα πρέπει να γίνουν πιο αργά"], 1, "Η ενημέρωση και η καλλιέργεια της υπευθυνότητας είναι εξίσου σημαντικές"),
 ],
 "gloss": {"αντιπαράθεση": "αντιπαράθεση — controversy, dispute", "υποχρεωτικές": "υποχρεωτικός — compulsory", "ζώνες ασφαλείας": "ζώνη ασφαλείας — seat belt", "επιθετικά": "επιθετικά — aggressively", "αντιστάθμιση του κινδύνου": "αντιστάθμιση του κινδύνου — risk compensation", "ρίσκα": "ρίσκο — risk", "μεταγενέστερες": "μεταγενέστερος — later, subsequent", "όφελος": "όφελος — benefit", "συστήματα υποβοήθησης": "σύστημα υποβοήθησης — driver-assistance system", "απροσεξία": "απροσεξία — carelessness", "καλλιέργεια": "καλλιέργεια — cultivation, fostering", "υπευθυνότητας": "υπευθυνότητα — sense of responsibility"}
})

ITEMS.append({
 "id": "l128-c1-miaoulis", "title": "Ο Μιαούλης και τα πυρπολικά της Ύδρας", "title_en": "Miaoulis and the fireships of Hydra", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με έναν ιστορικό για τον Ανδρέα Μιαούλη.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Καλαμαράκη, ποιος ήταν ο Ανδρέας Μιαούλης πριν από την Επανάσταση;", "Mr Kalamarakis, who was Andreas Miaoulis before the Revolution?"),
  L("Ιστορικός", "m", "Ήταν ένας από τους πλούσιους πλοιοκτήτες της Ύδρας. Γεννήθηκε γύρω στο 1769 και από νέος ταξίδευε στη Μεσόγειο, μεταφέροντας κυρίως σιτηρά. Στα χρόνια των ναπολεόντειων πολέμων πολλοί Υδραίοι καπεταναίοι πλούτισαν σπάζοντας τους αποκλεισμούς, και ο Μιαούλης ήταν ανάμεσά τους.", "He was one of the wealthy shipowners of Hydra. He was born around 1769 and from a young age sailed the Mediterranean, carrying mainly grain. During the Napoleonic Wars many Hydriot captains grew rich by running the blockades, and Miaoulis was among them."),
  L("Δημοσιογράφος", "f", "Και στη διάρκεια του Αγώνα;", "And during the War of Independence?"),
  L("Ιστορικός", "m", "Έγινε ο αρχηγός του ελληνικού στόλου. Τα ελληνικά πλοία ήταν μικρότερα από τα οθωμανικά, γι' αυτό οι Έλληνες στηρίχτηκαν σε μεγάλο βαθμό στα πυρπολικά, παλιά καράβια γεμάτα εύφλεκτα υλικά, που τα οδηγούσαν πάνω στα εχθρικά πλοία. Το 1825, για παράδειγμα, μια επίθεση με πυρπολικά στο λιμάνι της Μεθώνης κατέστρεψε αρκετά αιγυπτιακά πλοία.", "He became the commander of the Greek fleet. The Greek ships were smaller than the Ottoman ones, so the Greeks relied heavily on fireships, old vessels full of flammable material, which they steered onto the enemy ships. In 1825, for example, a fireship attack in the harbour of Methoni destroyed several Egyptian ships."),
  L("Δημοσιογράφος", "f", "Ποια ήταν η πιο αμφιλεγόμενη στιγμή της ζωής του;", "What was the most controversial moment of his life?"),
  L("Ιστορικός", "m", "Χωρίς αμφιβολία το 1831. Στη σύγκρουση ανάμεσα στον Καποδίστρια και στους Υδραίους, ο Μιαούλης κατέλαβε τον εθνικό στόλο στον Πόρο. Όταν κατέφθασαν ρωσικά πλοία που υποστήριζαν την κυβέρνηση, προτίμησε να ανατινάξει τη ναυαρχίδα «Ελλάς» και άλλα πλοία παρά να τα παραδώσει. Άλλοι το είδαν ως πράξη ανυπακοής, άλλοι ως συνέπεια ενός βαθύ εμφύλιου διχασμού.", "Without doubt 1831. In the conflict between Kapodistrias and the Hydriots, Miaoulis seized the national fleet at Poros. When Russian ships supporting the government arrived, he chose to blow up the flagship Hellas and other ships rather than hand them over. Some saw it as an act of insubordination, others as the result of a deep civil split."),
  L("Δημοσιογράφος", "f", "Πώς τον θυμούνται σήμερα στην Ύδρα;", "How is he remembered on Hydra today?"),
  L("Ιστορικός", "m", "Κάθε χρόνο, στα τέλη Ιουνίου, γιορτάζονται τα «Μιαούλεια», με αναπαράσταση ναυμαχίας και πυρπόληση ενός ομοιώματος πλοίου στο λιμάνι. Είναι μια γιορτή που θυμίζει πόσο στενά συνδέθηκε το νησί με τη θάλασσα και με τον Αγώνα.", "Every year, at the end of June, the 'Miaoulia' are celebrated, with a re-enactment of a sea battle and the burning of a replica ship in the harbour. It's a festival that recalls how closely the island was bound up with the sea and with the struggle for independence."),
 ],
 "questions": [
  Q("Πώς πλούτισαν πολλοί Υδραίοι καπεταναίοι πριν από την Επανάσταση;", ["Από το ψάρεμα", "Σπάζοντας τους αποκλεισμούς στα χρόνια των ναπολεόντειων πολέμων", "Από την πειρατεία στον Ατλαντικό", "Από το εμπόριο κρασιού με την Ιταλία"], 1, "πολλοί Υδραίοι καπεταναίοι πλούτισαν σπάζοντας τους αποκλεισμούς"),
  Q("Γιατί στηρίχτηκαν οι Έλληνες στα πυρπολικά;", ["Γιατί ήταν φθηνά στην κατασκευή", "Γιατί τα έστελνε η Ρωσία", "Γιατί τα ελληνικά πλοία ήταν μικρότερα από τα οθωμανικά", "Γιατί δεν είχαν κανόνια"], 2, "Τα ελληνικά πλοία ήταν μικρότερα από τα οθωμανικά"),
  Q("Τι έκανε ο Μιαούλης στον Πόρο το 1831;", ["Ανατίναξε τη ναυαρχίδα «Ελλάς» και άλλα πλοία, για να μην τα παραδώσει", "Παρέδωσε τον στόλο στους Ρώσους", "Συμφώνησε με τον Καποδίστρια", "Έφυγε για την Ιταλία"], 0, "προτίμησε να ανατινάξει τη ναυαρχίδα «Ελλάς» και άλλα πλοία παρά να τα παραδώσει"),
  Q("Τι περιλαμβάνουν τα «Μιαούλεια»;", ["Αγώνες κολύμβησης", "Αναπαράσταση ναυμαχίας και πυρπόληση ομοιώματος πλοίου", "Έκθεση ζωγραφικής", "Λιτανεία με εικόνες"], 1, "αναπαράσταση ναυμαχίας και πυρπόληση ενός ομοιώματος πλοίου"),
 ],
 "gloss": {"πλοιοκτήτες": "πλοιοκτήτης — shipowner", "σιτηρά": "σιτηρά — grain", "ναπολεόντειων πολέμων": "ναπολεόντειοι πόλεμοι — Napoleonic Wars", "πλούτισαν": "πλουτίζω — to grow rich", "αποκλεισμούς": "αποκλεισμός — blockade", "στόλου": "στόλος — fleet", "πυρπολικά": "πυρπολικό — fireship", "εύφλεκτα": "εύφλεκτος — flammable", "αμφιλεγόμενη": "αμφιλεγόμενος — controversial", "κατέλαβε": "καταλαμβάνω — to seize", "ανατινάξει": "ανατινάζω — to blow up", "ναυαρχίδα": "ναυαρχίδα — flagship", "ανυπακοής": "ανυπακοή — insubordination", "διχασμού": "διχασμός — split, schism", "Μιαούλεια": "Μιαούλεια — festival in honour of Miaoulis on Hydra", "αναπαράσταση": "αναπαράσταση — re-enactment", "ναυμαχίας": "ναυμαχία — sea battle", "πυρπόληση": "πυρπόληση — burning, setting on fire", "ομοιώματος": "ομοίωμα — replica, model"}
})

rnd = random.Random(128)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-128.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
