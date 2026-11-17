# Source for library/listening/listening-107.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l107.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l107-ann-psekasmoi-kounoupia", "title": "Ψεκασμοί για τα κουνούπια αυτή την εβδομάδα", "title_en": "Mosquito spraying this week", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Ο δήμος ενημερώνει τους κατοίκους ότι από τη Δευτέρα ως την Τετάρτη θα γίνουν ψεκασμοί για την καταπολέμηση των κουνουπιών στις περιοχές κοντά στο ποτάμι και στο κανάλι.", "The municipality informs residents that from Monday to Wednesday spraying will take place to control mosquitoes in the areas near the river and the canal."),
  L("Εκφωνητής", "m", "Οι ψεκασμοί θα γίνονται νωρίς το πρωί, από τις πέντε ως τις οχτώ, όταν δεν φυσάει δυνατός αέρας. Συνιστάται στους κατοίκους να κρατούν κλειστά τα παράθυρα τις ώρες αυτές και να μαζέψουν από τα μπαλκόνια τα ρούχα και τα παιχνίδια των παιδιών.", "The spraying will take place early in the morning, from five to eight, when there is no strong wind. Residents are advised to keep their windows closed during these hours and to bring in clothes and children's toys from their balconies."),
  L("Εκφωνητής", "m", "Παράλληλα, ο δήμος ζητά από όλους να αδειάζουν τακτικά τα πιατάκια από τις γλάστρες και κάθε δοχείο με στάσιμο νερό, γιατί εκεί γεννούν τα κουνούπια. Οι μελισσοκόμοι της περιοχής παρακαλούνται να κλείσουν τις κυψέλες τους πριν από τον ψεκασμό.", "At the same time, the municipality asks everyone to regularly empty the saucers under flowerpots and any container with standing water, because that is where mosquitoes lay their eggs. Beekeepers in the area are asked to close their hives before the spraying."),
 ],
 "questions": [
  Q("Πότε θα γίνονται οι ψεκασμοί;", ["Το μεσημέρι", "Νωρίς το πρωί, από τις πέντε ως τις οχτώ", "Αργά το βράδυ", "Όποτε φυσάει αέρας"], 1, "νωρίς το πρωί, από τις πέντε ως τις οχτώ"),
  Q("Τι συνιστάται στους κατοίκους;", ["Να φύγουν από τα σπίτια τους", "Να ποτίσουν τις γλάστρες", "Να κρατούν κλειστά τα παράθυρα και να μαζέψουν ρούχα και παιχνίδια από τα μπαλκόνια", "Να αγοράσουν εντομοαπωθητικό"], 2, "να κρατούν κλειστά τα παράθυρα τις ώρες αυτές και να μαζέψουν από τα μπαλκόνια τα ρούχα και τα παιχνίδια των παιδιών"),
  Q("Γιατί πρέπει να αδειάζουν τα δοχεία με νερό;", ["Γιατί εκεί γεννούν τα κουνούπια", "Γιατί το νερό θα μολυνθεί από τον ψεκασμό", "Γιατί υπάρχει λειψυδρία", "Γιατί το ζητούν οι μελισσοκόμοι"], 0, "γιατί εκεί γεννούν τα κουνούπια"),
 ],
 "gloss": {"ψεκασμοί": "ψεκασμός — spraying", "καταπολέμηση": "καταπολέμηση — control, fight against", "Συνιστάται": "συνιστάται — it is advised", "πιατάκια": "πιατάκι — saucer", "στάσιμο": "στάσιμος — standing, stagnant", "γεννούν": "γεννώ — to lay eggs, give birth", "κυψέλες": "κυψέλη — beehive"}
})

ITEMS.append({
 "id": "l107-vm-klimatistiko", "title": "Μήνυμα για την τοποθέτηση του κλιματιστικού", "title_en": "A message about installing the air conditioner", "type": "voicemail", "level": "B2",
 "context_el": "Αγοράσατε ένα κλιματιστικό. Ακούτε ένα μήνυμα από το κατάστημα στον τηλεφωνητή.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, κύριε Αντωνίου, από το κατάστημα ηλεκτρικών ειδών σας καλώ, για το κλιματιστικό που αγοράσατε το Σάββατο. Ο τεχνικός μας μπορεί να έρθει για την τοποθέτηση την Παρασκευή το πρωί, ανάμεσα στις εννιά και στις έντεκα.", "Good morning, Mr Antoniou, I'm calling from the electrical goods shop about the air conditioner you bought on Saturday. Our technician can come for the installation on Friday morning, between nine and eleven."),
  L("Υπάλληλος", "f", "Επειδή μένετε στον πέμπτο όροφο, η εξωτερική μονάδα θα μπει στο μπαλκόνι. Θα σας παρακαλούσα να ενημερώσετε τον διαχειριστή της πολυκατοικίας, γιατί ο τεχνικός θα χρειαστεί να ανοίξει μια τρύπα στον εξωτερικό τοίχο.", "Because you live on the fifth floor, the outdoor unit will go on the balcony. I would ask you to inform the building manager, because the technician will need to drill a hole in the outside wall."),
  L("Υπάλληλος", "f", "Η τοποθέτηση είναι δωρεάν, όπως σας είπαμε, αλλά αν χρειαστούν σωλήνες πάνω από τρία μέτρα, κάθε επιπλέον μέτρο χρεώνεται δεκαπέντε ευρώ. Αν η Παρασκευή δεν σας βολεύει, πάρτε μας μέχρι αύριο το μεσημέρι, για να σας κλείσουμε άλλη μέρα.", "The installation is free, as we told you, but if more than three metres of piping is needed, each extra metre is charged at fifteen euros. If Friday doesn't suit you, call us by tomorrow noon so that we can book you another day."),
 ],
 "questions": [
  Q("Πότε μπορεί να έρθει ο τεχνικός;", ["Το Σάββατο το πρωί", "Την Παρασκευή το απόγευμα", "Αύριο το μεσημέρι", "Την Παρασκευή το πρωί, ανάμεσα στις εννιά και στις έντεκα"], 3, "την Παρασκευή το πρωί, ανάμεσα στις εννιά και στις έντεκα"),
  Q("Γιατί πρέπει να ενημερώσει τον διαχειριστή;", ["Γιατί θα κοπεί το ρεύμα", "Γιατί ο τεχνικός θα χρειαστεί να ανοίξει μια τρύπα στον εξωτερικό τοίχο", "Γιατί ο τεχνικός θα χρησιμοποιήσει την ταράτσα", "Γιατί θα κλείσει το ασανσέρ"], 1, "ο τεχνικός θα χρειαστεί να ανοίξει μια τρύπα στον εξωτερικό τοίχο"),
  Q("Πότε θα πληρώσει κάτι επιπλέον;", ["Αν χρειαστούν σωλήνες πάνω από τρία μέτρα", "Αν ο τεχνικός έρθει το Σάββατο", "Αν η μονάδα μπει στην ταράτσα", "Σε κάθε περίπτωση"], 0, "αν χρειαστούν σωλήνες πάνω από τρία μέτρα"),
 ],
 "gloss": {"κλιματιστικό": "κλιματιστικό — air conditioner", "τοποθέτηση": "τοποθέτηση — installation", "μονάδα": "μονάδα — unit", "διαχειριστή": "διαχειριστής — (building) manager", "σωλήνες": "σωλήνας — pipe", "χρεώνεται": "χρεώνομαι — to be charged", "βολεύει": "βολεύω — to suit, be convenient"}
})

ITEMS.append({
 "id": "l107-dia-adeia-avgoustou", "title": "Ποιος θα πάρει άδεια τον Αύγουστο;", "title_en": "Who gets leave in August?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο συνάδελφοι σε ένα μικρό γραφείο συζητούν για τις καλοκαιρινές τους άδειες.",
 "script": [
  L("Νίκος", "m", "Ελπίδα, ο διευθυντής θέλει μέχρι την Παρασκευή τις ημερομηνίες για τις άδειες. Το πρόβλημα είναι ότι πρέπει να μένει πάντα ένας από τους δυο μας στο γραφείο.", "Elpida, the manager wants the dates for our leave by Friday. The problem is that one of us two must always stay in the office."),
  L("Ελπίδα", "f", "Το ξέρω. Εγώ θα ήθελα τις δύο πρώτες εβδομάδες του Αυγούστου. Η αδελφή μου παντρεύεται στην Κρήτη στις οχτώ και έχω ήδη κλείσει εισιτήρια.", "I know. I'd like the first two weeks of August. My sister is getting married in Crete on the eighth and I've already booked tickets."),
  L("Νίκος", "m", "Άσχημα. Κι εγώ ήθελα αρχές Αυγούστου, γιατί τότε έχουν άδεια και τα παιδιά από τις κατασκηνώσεις.", "Too bad. I wanted early August too, because that's when the kids are back from summer camp."),
  L("Ελπίδα", "f", "Τα παιδιά μέχρι πότε είναι στην κατασκήνωση;", "Until when are the kids at camp?"),
  L("Νίκος", "m", "Μέχρι τις τριάντα Ιουλίου. Μετά είναι ελεύθερα όλο τον Αύγουστο, μέχρι να ανοίξουν τα σχολεία.", "Until the thirtieth of July. After that they're free all of August, until schools open."),
  L("Ελπίδα", "f", "Τότε δεν μπορείς να πάρεις το δεύτερο δεκαπενθήμερο; Η θάλασσα είναι ακόμα ζεστή και οι παραλίες έχουν λιγότερο κόσμο μετά τον Δεκαπενταύγουστο.", "Then can't you take the second fortnight? The sea is still warm and the beaches are less crowded after the fifteenth of August."),
  L("Νίκος", "m", "Έχεις δίκιο, και τα ενοίκια πέφτουν. Εντάξει, αλλά τα Χριστούγεννα διαλέγω εγώ πρώτος.", "You're right, and rents drop. OK, but at Christmas I choose first."),
 ],
 "questions": [
  Q("Γιατί θέλει η Ελπίδα τις δύο πρώτες εβδομάδες;", ["Γιατί τότε είναι φθηνότερα τα εισιτήρια", "Γιατί η αδελφή της παντρεύεται στην Κρήτη στις οχτώ", "Γιατί έχει κατασκήνωση", "Γιατί το ζήτησε ο διευθυντής"], 1, "Η αδελφή μου παντρεύεται στην Κρήτη στις οχτώ"),
  Q("Ποιο επιχείρημα δεν χρησιμοποιείται για το δεύτερο δεκαπενθήμερο;", ["Η θάλασσα είναι ακόμα ζεστή", "Οι παραλίες έχουν λιγότερο κόσμο", "Τα ενοίκια πέφτουν", "Ο καιρός είναι πιο δροσερός"], 3, "Η θάλασσα είναι ακόμα ζεστή και οι παραλίες έχουν λιγότερο κόσμο μετά τον Δεκαπενταύγουστο"),
  Q("Τι ζητά ο Νίκος ως αντάλλαγμα;", ["Να διαλέξει πρώτος τα Χριστούγεννα", "Να πάρει τρεις εβδομάδες", "Να δουλεύει η Ελπίδα τα Σάββατα", "Να του πληρώσει τα εισιτήρια"], 0, "τα Χριστούγεννα διαλέγω εγώ πρώτος"),
 ],
 "gloss": {"άδειες": "άδεια — leave (from work)", "κατασκηνώσεις": "κατασκήνωση — summer camp", "δεκαπενθήμερο": "δεκαπενθήμερο — fortnight", "Δεκαπενταύγουστο": "Δεκαπενταύγουστος — 15 August (Dormition holiday)", "ενοίκια": "ενοίκιο — rent"}
})

ITEMS.append({
 "id": "l107-int-odigos-nyxterinou", "title": "Οδηγός στο νυχτερινό λεωφορείο", "title_en": "Driving the night bus", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια οδηγό λεωφορείου σε μια ραδιοφωνική εκπομπή για τη ζωή στην πόλη.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Σταυροπούλου, εδώ και έξι χρόνια οδηγείτε μόνο τη νυχτερινή γραμμή. Το επιλέξατε;", "Mrs Stavropoulou, for six years now you have driven only the night line. Did you choose it?"),
  L("Οδηγός", "f", "Ναι, και πολλοί συνάδελφοι απορούν. Η νύχτα έχει λιγότερη κίνηση και λιγότερο άγχος. Τη μέρα παλεύεις με τα φανάρια και τα παρκαρισμένα αυτοκίνητα· τη νύχτα οδηγείς πραγματικά.", "Yes, and many colleagues are puzzled. The night has less traffic and less stress. During the day you fight with traffic lights and parked cars; at night you really drive."),
  L("Δημοσιογράφος", "m", "Ποιοι είναι οι επιβάτες σας;", "Who are your passengers?"),
  L("Οδηγός", "f", "Νοσηλευτές που σχολάνε από τη βάρδια, φουρνάρηδες που ανοίγουν στις τρεις, φοιτητές που γυρίζουν από τη διασκέδαση. Πολλούς τους ξέρω πια με το όνομά τους. Ένας ηλικιωμένος κύριος, που καθαρίζει γραφεία, μου φέρνει κάθε Παρασκευή ένα κουλούρι.", "Nurses finishing their shift, bakers who open at three, students coming back from a night out. I know many of them by name now. An elderly gentleman who cleans offices brings me a koulouri every Friday."),
  L("Δημοσιογράφος", "m", "Δεν φοβάστε ποτέ;", "Are you never afraid?"),
  L("Οδηγός", "f", "Σπάνια. Υπάρχουν κάμερες και ένα κουμπί που ειδοποιεί αμέσως το κέντρο. Το δύσκολο είναι άλλο: ο ύπνος τη μέρα. Έχω βάλει σκούρες κουρτίνες και κλείνω το κινητό, αλλιώς δεν ξεκουράζομαι.", "Rarely. There are cameras and a button that instantly alerts the control centre. The hard part is something else: sleeping during the day. I've put up dark curtains and I switch off my phone, otherwise I don't rest."),
 ],
 "questions": [
  Q("Γιατί προτιμά τη νυχτερινή γραμμή;", ["Γιατί πληρώνεται περισσότερο", "Γιατί η νύχτα έχει λιγότερη κίνηση και λιγότερο άγχος", "Γιατί δεν της αρέσουν οι επιβάτες της μέρας", "Γιατί δεν της έδωσαν άλλη επιλογή"], 1, "Η νύχτα έχει λιγότερη κίνηση και λιγότερο άγχος"),
  Q("Τι κάνει κάθε Παρασκευή ένας ηλικιωμένος επιβάτης;", ["Της φέρνει ένα κουλούρι", "Της λέει τα νέα της γειτονιάς", "Πηγαίνει στον φούρνο μαζί της", "Παραπονιέται για την καθυστέρηση"], 0, "μου φέρνει κάθε Παρασκευή ένα κουλούρι"),
  Q("Ποιο είναι, κατά τη γνώμη της, το πιο δύσκολο;", ["Οι μεθυσμένοι επιβάτες", "Η μοναξιά", "Ο ύπνος τη μέρα", "Το κρύο τον χειμώνα"], 2, "Το δύσκολο είναι άλλο: ο ύπνος τη μέρα"),
 ],
 "gloss": {"απορούν": "απορώ — to wonder, be puzzled", "παλεύεις": "παλεύω — to struggle, fight", "σχολάνε": "σχολάω — to finish work", "βάρδια": "βάρδια — shift", "ειδοποιεί": "ειδοποιώ — to alert, notify", "κουρτίνες": "κουρτίνα — curtain"}
})

ITEMS.append({
 "id": "l107-rep-yiothesia-elias", "title": "Υιοθετήστε ένα ελαιόδεντρο", "title_en": "Adopt an olive tree", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για την ύπαιθρο.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε ένα χωριό της Μεσσηνίας, μια ομάδα νέων αγροτών βρήκε έναν πρωτότυπο τρόπο να σώσει τους παλιούς ελαιώνες που είχαν εγκαταλειφθεί. Ο καθένας, από οπουδήποτε στον κόσμο, μπορεί να «υιοθετήσει» ένα ελαιόδεντρο πληρώνοντας ένα ποσό τον χρόνο.", "In a village in Messinia, a group of young farmers found an original way to save the old olive groves that had been abandoned. Anyone, from anywhere in the world, can 'adopt' an olive tree by paying an annual amount."),
  L("Αγρότης", "m", "Με τα χρήματα καθαρίζουμε τα χωράφια, κλαδεύουμε και μαζεύουμε τις ελιές. Κάθε θετός γονιός παίρνει το Δεκέμβριο πέντε λίτρα λάδι από το δικό του δέντρο και μια φωτογραφία του. Μερικοί έρχονται κιόλας να βοηθήσουν στο μάζεμα.", "With the money we clear the fields, prune and harvest the olives. Each adoptive parent receives five litres of oil from their own tree in December, along with a photo of it. Some even come to help with the harvest."),
  L("Ρεπόρτερ", "f", "Σήμερα το πρόγραμμα έχει πάνω από χίλια διακόσια «υιοθετημένα» δέντρα, κυρίως από τη Γερμανία, την Ολλανδία και την Αθήνα. Το πιο σημαντικό, λένε οι αγρότες, είναι ότι τρεις οικογένειες γύρισαν στο χωριό και ζουν πια από αυτή τη δουλειά.", "Today the scheme has over one thousand two hundred 'adopted' trees, mainly from Germany, the Netherlands and Athens. Most importantly, the farmers say, three families returned to the village and now make a living from this work."),
 ],
 "questions": [
  Q("Ποιος ήταν ο σκοπός του προγράμματος;", ["Να πουλήσουν τους ελαιώνες σε ξένους", "Να φτιάξουν ένα ξενοδοχείο", "Να σώσουν τους παλιούς ελαιώνες που είχαν εγκαταλειφθεί", "Να φυτέψουν καινούργια δέντρα"], 2, "να σώσει τους παλιούς ελαιώνες που είχαν εγκαταλειφθεί"),
  Q("Τι παίρνει κάθε «θετός γονιός»;", ["Πέντε λίτρα λάδι από το δέντρο του και μια φωτογραφία", "Ένα κομμάτι γης", "Δωρεάν διαμονή στο χωριό", "Ένα δενδρύλλιο"], 0, "πέντε λίτρα λάδι από το δικό του δέντρο και μια φωτογραφία του"),
  Q("Ποιο θεωρούν οι αγρότες το πιο σημαντικό αποτέλεσμα;", ["Τα κέρδη από τις εξαγωγές", "Ότι τρεις οικογένειες γύρισαν στο χωριό και ζουν από αυτή τη δουλειά", "Ότι το χωριό έγινε τουριστικό", "Ότι πήραν βραβείο"], 1, "τρεις οικογένειες γύρισαν στο χωριό και ζουν πια από αυτή τη δουλειά"),
 ],
 "gloss": {"ελαιώνες": "ελαιώνας — olive grove", "εγκαταλειφθεί": "εγκαταλείπω — to abandon", "υιοθετήσει": "υιοθετώ — to adopt", "κλαδεύουμε": "κλαδεύω — to prune", "θετός": "θετός — adoptive", "μάζεμα": "μάζεμα — harvest, picking"}
})

ITEMS.append({
 "id": "l107-rep-protes-voitheies-goneis", "title": "Πρώτες βοήθειες για γονείς μωρών", "title_en": "First aid for parents of babies", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στο δελτίο ειδήσεων ενός τοπικού σταθμού.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο πολιτιστικό κέντρο της γειτονιάς, δώδεκα γονείς κάθονται στο πάτωμα με μια κούκλα μωρού στην αγκαλιά. Παρακολουθούν ένα δωρεάν σεμινάριο πρώτων βοηθειών, που οργανώνει ο δήμος μαζί με εθελοντές διασώστες.", "At the neighbourhood cultural centre, twelve parents sit on the floor with a baby doll in their arms. They are attending a free first-aid seminar organised by the municipality together with volunteer paramedics."),
  L("Διασώστρια", "f", "Μαθαίνουν τι να κάνουν αν το μωρό πνιγεί με ένα κομμάτι φαγητό ή με ένα μικρό παιχνίδι, και πώς γίνεται η καρδιοπνευμονική αναζωογόνηση σε βρέφος, που είναι πολύ διαφορετική από ό,τι σε έναν ενήλικα. Το πιο σημαντικό, όμως, είναι να μην πανικοβληθούν και να καλέσουν αμέσως το εκατόν εξήντα έξι.", "They learn what to do if the baby chokes on a piece of food or a small toy, and how CPR is performed on an infant, which is very different from an adult. The most important thing, though, is not to panic and to call 166 immediately."),
  L("Ρεπόρτερ", "m", "Τα σεμινάρια γίνονται κάθε δεύτερο Σάββατο και οι θέσεις γεμίζουν μέσα σε λίγες ώρες. Ο δήμος σκοπεύει να προσθέσει και απογευματινά τμήματα για τους παππούδες και τις γιαγιάδες που κρατούν τα εγγόνια τους.", "The seminars take place every other Saturday and the places fill up within a few hours. The municipality plans to add afternoon classes for grandparents who look after their grandchildren."),
 ],
 "questions": [
  Q("Ποιος οργανώνει το σεμινάριο;", ["Ένα ιδιωτικό νοσοκομείο", "Ο δήμος μαζί με εθελοντές διασώστες", "Ένας σύλλογος γονέων", "Το υπουργείο Παιδείας"], 1, "οργανώνει ο δήμος μαζί με εθελοντές διασώστες"),
  Q("Τι θεωρεί η διασώστρια το πιο σημαντικό;", ["Να έχουν πάντα φαρμακείο στο σπίτι", "Να μην πανικοβληθούν και να καλέσουν αμέσως το εκατόν εξήντα έξι", "Να μην δίνουν ποτέ παιχνίδια στα μωρά", "Να πάρουν δίπλωμα διασώστη"], 1, "να μην πανικοβληθούν και να καλέσουν αμέσως το εκατόν εξήντα έξι"),
  Q("Τι σκοπεύει να προσθέσει ο δήμος;", ["Σεμινάρια για δασκάλους", "Μαθήματα κολύμβησης για μωρά", "Απογευματινά τμήματα για παππούδες και γιαγιάδες", "Ένα ιατρείο στο πολιτιστικό κέντρο"], 2, "απογευματινά τμήματα για τους παππούδες και τις γιαγιάδες"),
 ],
 "gloss": {"διασώστες": "διασώστης — paramedic, rescuer", "πνιγεί": "πνίγομαι — to choke", "καρδιοπνευμονική": "καρδιοπνευμονική αναζωογόνηση — CPR", "βρέφος": "βρέφος — infant", "πανικοβληθούν": "πανικοβάλλομαι — to panic", "εγγόνια": "εγγόνι — grandchild"}
})

ITEMS.append({
 "id": "l107-mono-emfialomeno-nero", "title": "Γιατί σταμάτησα να αγοράζω εμφιαλωμένο νερό", "title_en": "Why I stopped buying bottled water", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν ακροατή να μιλά σε μια ραδιοφωνική εκπομπή για τις καθημερινές συνήθειες.",
 "script": [
  L("Ορέστης", "m", "Μέχρι πριν από δύο χρόνια κουβαλούσα κάθε εβδομάδα από το σούπερ μάρκετ δύο εξάδες με μπουκάλια νερό. Ένα βράδυ μέτρησα τις άδειες πλαστικές φιάλες που είχαμε μαζέψει μέσα σε έναν μήνα στην ανακύκλωση: ήταν πάνω από εκατό, μόνο για τρία άτομα.", "Until two years ago I carried two six-packs of bottled water home from the supermarket every week. One evening I counted the empty plastic bottles we had collected for recycling in one month: there were over a hundred, just for three people."),
  L("Ορέστης", "m", "Πήρα τηλέφωνο την εταιρεία ύδρευσης του δήμου και ρώτησα αν το νερό της βρύσης είναι ασφαλές. Μου εξήγησαν ότι ελέγχεται τακτικά και ότι τα αποτελέσματα δημοσιεύονται στην ιστοσελίδα τους. Το μόνο πρόβλημα στη δική μας περιοχή ήταν η γεύση από το χλώριο.", "I phoned the municipal water company and asked whether tap water is safe. They explained that it is tested regularly and that the results are published on their website. The only problem in our area was the taste of chlorine."),
  L("Ορέστης", "m", "Αγοράσαμε λοιπόν μια κανάτα με φίλτρο και τρία μεταλλικά παγούρια. Το νερό το βάζουμε στο ψυγείο και η γεύση είναι μια χαρά. Υπολόγισα ότι γλιτώνουμε περίπου διακόσια ευρώ τον χρόνο, και, το πιο ωραίο, δεν σέρνω πια βαριές σακούλες στη σκάλα της πολυκατοικίας.", "So we bought a filter jug and three metal water bottles. We keep the water in the fridge and it tastes fine. I worked out that we save about two hundred euros a year and, best of all, I no longer drag heavy bags up the stairs of the apartment block."),
 ],
 "questions": [
  Q("Τι τον έκανε να αλλάξει συνήθεια;", ["Μια διαφήμιση στην τηλεόραση", "Μέτρησε πάνω από εκατό άδειες πλαστικές φιάλες σε έναν μήνα", "Τον συμβούλεψε ο γιατρός του", "Ακρίβυνε το νερό στο σούπερ μάρκετ"], 1, "ήταν πάνω από εκατό, μόνο για τρία άτομα"),
  Q("Τι έμαθε από την εταιρεία ύδρευσης;", ["Ότι το νερό ελέγχεται τακτικά και τα αποτελέσματα δημοσιεύονται", "Ότι το νερό πρέπει να βράζεται", "Ότι θα αλλάξουν οι σωλήνες της περιοχής", "Ότι το νερό δεν είναι πόσιμο"], 0, "ελέγχεται τακτικά και ότι τα αποτελέσματα δημοσιεύονται στην ιστοσελίδα τους"),
  Q("Ποιο ήταν το μόνο πρόβλημα στην περιοχή του;", ["Οι συχνές διακοπές νερού", "Το νερό ήταν θολό", "Η γεύση από το χλώριο", "Η χαμηλή πίεση"], 2, "Το μόνο πρόβλημα στη δική μας περιοχή ήταν η γεύση από το χλώριο"),
 ],
 "gloss": {"εξάδες": "εξάδα — six-pack", "φιάλες": "φιάλη — bottle", "ύδρευσης": "ύδρευση — water supply", "χλώριο": "χλώριο — chlorine", "κανάτα": "κανάτα — jug", "παγούρια": "παγούρι — water bottle, flask", "σέρνω": "σέρνω — to drag"}
})

ITEMS.append({
 "id": "l107-mono-ethelontria-pyrosvestria", "title": "Η πρώτη μου χρονιά ως εθελόντρια πυροσβέστρια", "title_en": "My first year as a volunteer firefighter", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νέα γυναίκα να μιλά σε μια εκδήλωση του δήμου για τον εθελοντισμό.",
 "script": [
  L("Δανάη", "f", "Πριν από έναν χρόνο, μετά τη μεγάλη φωτιά στο βουνό πάνω από το χωριό μας, αποφάσισα να γίνω εθελόντρια πυροσβέστρια. Είμαι λογίστρια και δεν είχα κρατήσει ποτέ μάνικα στα χέρια μου.", "A year ago, after the big fire on the mountain above our village, I decided to become a volunteer firefighter. I'm an accountant and I had never held a fire hose in my hands."),
  L("Δανάη", "f", "Η εκπαίδευση κράτησε τρεις μήνες, κάθε Σαββατοκύριακο. Μάθαμε να διαβάζουμε τον αέρα, να ανοίγουμε αντιπυρικές ζώνες και, κυρίως, πότε να υποχωρούμε. Ο εκπαιδευτής μας έλεγε συνέχεια: «Κανένα δέντρο δεν αξίζει περισσότερο από έναν άνθρωπο».", "The training lasted three months, every weekend. We learned to read the wind, to open firebreaks and, above all, when to retreat. Our instructor kept saying: 'No tree is worth more than a person.'"),
  L("Δανάη", "f", "Το καλοκαίρι βγήκαμε σε έντεκα περιστατικά, τα περισσότερα μικρές φωτιές σε ξερά χόρτα. Το πιο κουραστικό δεν ήταν η φωτιά, αλλά οι περιπολίες τις ζεστές νύχτες. Τα παιδιά της ομάδας, όμως, έγιναν η δεύτερη οικογένειά μου, και του χρόνου θα ξαναπάω.", "In the summer we went out on eleven incidents, most of them small fires in dry grass. The most tiring thing wasn't the fire but the patrols on hot nights. But the people in the team became my second family, and next year I'll do it again."),
 ],
 "questions": [
  Q("Τι την έκανε να γίνει εθελόντρια;", ["Η μεγάλη φωτιά στο βουνό πάνω από το χωριό της", "Ένα σεμινάριο στη δουλειά της", "Η πρόταση μιας φίλης", "Μια διαφήμιση του δήμου"], 0, "μετά τη μεγάλη φωτιά στο βουνό πάνω από το χωριό μας"),
  Q("Τι τονίζει ο εκπαιδευτής;", ["Ότι η ταχύτητα είναι το πιο σημαντικό", "Ότι κανένα δέντρο δεν αξίζει περισσότερο από έναν άνθρωπο", "Ότι πρέπει να μένουν πάντα μέχρι το τέλος", "Ότι ο αέρας δεν μπορεί να προβλεφθεί"], 1, "Κανένα δέντρο δεν αξίζει περισσότερο από έναν άνθρωπο"),
  Q("Τι ήταν το πιο κουραστικό για εκείνη;", ["Η εκπαίδευση", "Οι μεγάλες φωτιές", "Οι περιπολίες τις ζεστές νύχτες", "Η δουλειά της ως λογίστρια"], 2, "οι περιπολίες τις ζεστές νύχτες"),
 ],
 "gloss": {"εθελόντρια": "εθελόντρια — volunteer (f.)", "μάνικα": "μάνικα — fire hose", "αντιπυρικές": "αντιπυρική ζώνη — firebreak", "υποχωρούμε": "υποχωρώ — to retreat", "περιστατικά": "περιστατικό — incident", "περιπολίες": "περιπολία — patrol"}
})

ITEMS.append({
 "id": "l107-c1-diplani-oura", "title": "Γιατί η διπλανή ουρά μοιάζει πάντα πιο γρήγορη;", "title_en": "Why does the other queue always seem faster?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή εκλαϊκευμένης επιστήμης.",
 "script": [
  L("Παρουσιάστρια", "f", "Όλοι το έχουμε ζήσει: διαλέγουμε ταμείο στο σούπερ μάρκετ και, μόλις σταθούμε, η διπλανή ουρά αρχίζει να κυλάει σαν νερό. Είναι κατάρα ή απλώς ιδέα μας; Η απάντηση είναι, εν μέρει, απλά μαθηματικά. Αν υπάρχουν τρία ταμεία, η πιθανότητα να είναι το δικό μας το γρηγορότερο είναι μόλις μία στις τρεις. Με άλλα λόγια, τις περισσότερες φορές κάποια άλλη ουρά θα προχωρήσει πράγματι πιο γρήγορα.", "We've all experienced it: we choose a checkout at the supermarket and, as soon as we stand there, the next queue starts flowing like water. Is it a curse or just our imagination? The answer is, partly, simple mathematics. If there are three checkouts, the probability that ours is the fastest is just one in three. In other words, most of the time some other queue really will move faster."),
  L("Παρουσιάστρια", "f", "Υπάρχει όμως και ένας ψυχολογικός παράγοντας. Τις φορές που μας προσπερνούν, τις θυμόμαστε με εκνευρισμό· τις φορές που προσπερνάμε εμείς, μάλλον δεν τις προσέχουμε καν. Επιπλέον, ο χρόνος της αναμονής φαίνεται συχνά μεγαλύτερος από ό,τι είναι, ιδίως όταν δεν έχουμε τίποτα να κάνουμε, και ακόμη περισσότερο όταν δεν ξέρουμε πόσο θα περιμένουμε.", "But there is also a psychological factor. The times we are overtaken we remember with irritation; the times we overtake, we probably don't even notice. Moreover, waiting time often seems longer than it is, especially when we have nothing to do, and even more so when we don't know how long we'll wait."),
  L("Παρουσιάστρια", "f", "Γι' αυτό πολλές τράπεζες και ταχυδρομεία έχουν υιοθετήσει τη μία κοινή ουρά που τροφοδοτεί όλα τα ταμεία, ή τα χαρτάκια με αριθμούς. Ο μέσος χρόνος αναμονής δεν μειώνεται απαραίτητα, η αίσθηση της αδικίας όμως εξαφανίζεται: κανείς δεν μπορεί να «διαλέξει λάθος». Και, όπως φαίνεται, αυτό που μας εκνευρίζει περισσότερο δεν είναι τόσο η αναμονή όσο η υποψία ότι οι άλλοι περιμένουν λιγότερο.", "That's why many banks and post offices have adopted a single shared queue that feeds all the counters, or numbered tickets. The average waiting time doesn't necessarily decrease, but the sense of unfairness disappears: no one can 'choose wrong'. And, it seems, what annoys us most is not so much the waiting as the suspicion that others are waiting less."),
 ],
 "questions": [
  Q("Τι δείχνουν, σύμφωνα με την παρουσιάστρια, τα μαθηματικά;", ["Ότι η δική μας ουρά είναι πάντα η πιο αργή", "Ότι με τρία ταμεία η πιθανότητα να είναι το δικό μας το γρηγορότερο είναι μία στις τρεις", "Ότι όλες οι ουρές κινούνται με την ίδια ταχύτητα", "Ότι οι μικρές ουρές είναι πάντα πιο γρήγορες"], 1, "η πιθανότητα να είναι το δικό μας το γρηγορότερο είναι μόλις μία στις τρεις"),
  Q("Ποιος ψυχολογικός παράγοντας αναφέρεται;", ["Θυμόμαστε όταν μας προσπερνούν, αλλά μάλλον δεν προσέχουμε όταν προσπερνάμε εμείς", "Βαριόμαστε τους ταμίες", "Προτιμάμε πάντα την ουρά με τους λιγότερους ανθρώπους", "Ξεχνάμε γρήγορα την αναμονή"], 0, "Τις φορές που μας προσπερνούν, τις θυμόμαστε με εκνευρισμό"),
  Q("Πότε φαίνεται η αναμονή ακόμη μεγαλύτερη;", ["Όταν είμαστε με παρέα", "Όταν ακούμε μουσική", "Όταν η ουρά είναι κοντά στην είσοδο", "Όταν δεν ξέρουμε πόσο θα περιμένουμε"], 3, "ακόμη περισσότερο όταν δεν ξέρουμε πόσο θα περιμένουμε"),
  Q("Τι πετυχαίνει η μία κοινή ουρά;", ["Μειώνει πάντα στο μισό τον χρόνο αναμονής", "Χρειάζεται λιγότερους υπαλλήλους", "Εξαφανίζει την αίσθηση της αδικίας", "Επιτρέπει στους πελάτες να διαλέξουν ταμία"], 2, "η αίσθηση της αδικίας όμως εξαφανίζεται"),
 ],
 "gloss": {"κυλάει": "κυλάω — to flow, roll", "προσπερνούν": "προσπερνώ — to overtake", "εκνευρισμό": "εκνευρισμός — irritation", "αναμονής": "αναμονή — waiting", "τροφοδοτεί": "τροφοδοτώ — to feed, supply", "υποψία": "υποψία — suspicion"}
})

ITEMS.append({
 "id": "l107-c1-tainies-tromou", "title": "Γιατί μας αρέσει να φοβόμαστε στις ταινίες τρόμου;", "title_en": "Why do we enjoy being scared by horror films?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια ψυχολόγο σε μια εκπομπή για τον κινηματογράφο.",
 "script": [
  L("Δημοσιογράφος", "m", "Ο φόβος είναι ένα δυσάρεστο συναίσθημα. Γιατί, λοιπόν, πληρώνουμε εισιτήριο για να φοβηθούμε;", "Fear is an unpleasant emotion. So why do we pay for a ticket to be frightened?"),
  L("Ψυχολόγος", "f", "Γιατί είναι φόβος υπό έλεγχο. Ο οργανισμός αντιδρά σαν να υπάρχει πραγματικός κίνδυνος: η καρδιά χτυπά πιο γρήγορα, η αναπνοή επιταχύνεται. Ταυτόχρονα, όμως, ξέρουμε ότι καθόμαστε σε μια ασφαλή πολυθρόνα. Αυτός ο συνδυασμός διέγερσης και ασφάλειας μπορεί να είναι ευχάριστος, και η ανακούφιση στο τέλος συχνά βιώνεται σαν ανταμοιβή.", "Because it is fear under control. The body reacts as if there were real danger: the heart beats faster, breathing speeds up. At the same time, though, we know we're sitting in a safe armchair. This combination of arousal and safety can be pleasant, and the relief at the end is often experienced as a reward."),
  L("Δημοσιογράφος", "m", "Υπάρχει και κάποια χρησιμότητα σε αυτό;", "Is there any usefulness in it as well?"),
  L("Ψυχολόγος", "f", "Ορισμένοι ερευνητές πιστεύουν ότι οι ιστορίες τρόμου λειτουργούν σαν πρόβα: μας επιτρέπουν να «δοκιμάσουμε» επικίνδυνες καταστάσεις χωρίς πραγματικό κόστος. Μια μελέτη στη διάρκεια της πανδημίας βρήκε ότι οι φανατικοί θεατές τέτοιων ταινιών δήλωναν λιγότερη ψυχολογική πίεση από τους άλλους. Αυτό, βέβαια, δεν αποδεικνύει ότι οι ταινίες τούς έκαναν πιο ανθεκτικούς· μπορεί απλώς οι πιο ψύχραιμοι άνθρωποι να τις προτιμούν.", "Some researchers believe that horror stories work like a rehearsal: they let us 'try out' dangerous situations at no real cost. A study during the pandemic found that keen fans of such films reported less psychological distress than others. Of course, this doesn't prove that the films made them more resilient; it may simply be that calmer people prefer them."),
  L("Δημοσιογράφος", "m", "Και όσοι δεν αντέχουν ούτε το τρέιλερ;", "And those who can't stand even the trailer?"),
  L("Ψυχολόγος", "f", "Είναι απολύτως φυσιολογικό. Οι άνθρωποι διαφέρουν πολύ στο πόση έντονη διέγερση αναζητούν. Για κάποιους η ίδια σκηνή είναι διασκεδαστική, για άλλους απλώς τρομακτική με την κακή έννοια. Κανείς δεν πρέπει να νιώθει ότι «αποτυγχάνει» επειδή κλείνει τα μάτια.", "It's completely normal. People differ greatly in how much intense arousal they seek. For some the same scene is entertaining, for others simply frightening in the bad sense. No one should feel they are 'failing' because they close their eyes."),
 ],
 "questions": [
  Q("Γιατί, σύμφωνα με την ψυχολόγο, μπορεί να είναι ευχάριστος ο φόβος σε μια ταινία;", ["Γιατί ο οργανισμός δεν αντιδρά καθόλου", "Γιατί συνδυάζει διέγερση και ασφάλεια", "Γιατί οι ταινίες είναι πάντα αστείες", "Γιατί βλέπουμε τις ταινίες με παρέα"], 1, "Αυτός ο συνδυασμός διέγερσης και ασφάλειας μπορεί να είναι ευχάριστος"),
  Q("Με τι παρομοιάζουν ορισμένοι ερευνητές τις ιστορίες τρόμου;", ["Με πρόβα για επικίνδυνες καταστάσεις", "Με φάρμακο για την αϋπνία", "Με αθλητική προπόνηση", "Με όνειρο"], 0, "οι ιστορίες τρόμου λειτουργούν σαν πρόβα"),
  Q("Τι λέει η ψυχολόγος για τη μελέτη της πανδημίας;", ["Ότι απέδειξε πως οι ταινίες τρόμου μάς κάνουν πιο ανθεκτικούς", "Ότι δεν βρήκε καμία διαφορά", "Ότι το αποτέλεσμα δεν αποδεικνύει σχέση αιτίας, γιατί ίσως οι πιο ψύχραιμοι προτιμούν τέτοιες ταινίες", "Ότι αφορούσε μόνο παιδιά"], 2, "μπορεί απλώς οι πιο ψύχραιμοι άνθρωποι να τις προτιμούν"),
  Q("Τι λέει για όσους δεν αντέχουν τις ταινίες τρόμου;", ["Ότι πρέπει να εξασκηθούν σιγά σιγά", "Ότι έχουν κάποιο πρόβλημα άγχους", "Ότι χάνουν μια χρήσιμη εμπειρία", "Ότι είναι απολύτως φυσιολογικό, γιατί οι άνθρωποι διαφέρουν στο πόση διέγερση αναζητούν"], 3, "Είναι απολύτως φυσιολογικό"),
 ],
 "gloss": {"επιταχύνεται": "επιταχύνομαι — to speed up", "διέγερσης": "διέγερση — arousal, excitement", "ανακούφιση": "ανακούφιση — relief", "ανταμοιβή": "ανταμοιβή — reward", "πρόβα": "πρόβα — rehearsal", "ανθεκτικούς": "ανθεκτικός — resilient", "ψύχραιμοι": "ψύχραιμος — calm, cool-headed"}
})

rnd = random.Random(107)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-107.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
