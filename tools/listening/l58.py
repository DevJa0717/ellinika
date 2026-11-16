# Source for library/listening/listening-58.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l58.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l58-ann-kyliomenes", "title": "Εκτός λειτουργίας οι κυλιόμενες σκάλες", "title_en": "Escalators out of service", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε έναν σταθμό του μετρό της Αθήνας. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Ανακοίνωση", "f", "Αγαπητοί επιβάτες, σας ενημερώνουμε ότι λόγω εργασιών συντήρησης οι κυλιόμενες σκάλες της εξόδου προς την οδό Πανεπιστημίου θα είναι εκτός λειτουργίας από σήμερα έως και την Παρασκευή.", "Dear passengers, we inform you that because of maintenance work the escalators at the exit towards Panepistimiou Street will be out of service from today up to and including Friday."),
  L("Ανακοίνωση", "f", "Οι επιβάτες που κατευθύνονται προς την έξοδο αυτή παρακαλούνται να χρησιμοποιούν τις σταθερές σκάλες ή την έξοδο προς την πλατεία Συντάγματος. Τα άτομα με κινητικά προβλήματα, οι ηλικιωμένοι και όσοι έχουν καρότσι μπορούν να χρησιμοποιούν τον ανελκυστήρα, που λειτουργεί κανονικά.", "Passengers heading for this exit are asked to use the fixed stairs or the exit towards Syntagma Square. People with mobility problems, the elderly and anyone with a pushchair can use the lift, which is working normally."),
  L("Ανακοίνωση", "f", "Για οποιαδήποτε βοήθεια, απευθυνθείτε στο προσωπικό του σταθμού. Ζητούμε συγγνώμη για την ταλαιπωρία.", "For any help, please ask the station staff. We apologise for the inconvenience."),
 ],
 "questions": [
  Q("Μέχρι πότε θα είναι εκτός λειτουργίας οι κυλιόμενες σκάλες;", ["Μέχρι αύριο", "Έως και την Παρασκευή", "Για έναν μήνα", "Μόνο τις πρωινές ώρες"], 1, "θα είναι εκτός λειτουργίας από σήμερα έως και την Παρασκευή"),
  Q("Τι μπορούν να κάνουν οι επιβάτες που πηγαίνουν προς την οδό Πανεπιστημίου;", ["Να περιμένουν το επόμενο τρένο", "Να χρησιμοποιούν τις σταθερές σκάλες ή άλλη έξοδο", "Να πάρουν λεωφορείο", "Να κατέβουν στον επόμενο σταθμό"], 1, "παρακαλούνται να χρησιμοποιούν τις σταθερές σκάλες ή την έξοδο προς την πλατεία Συντάγματος"),
  Q("Ποιοι μπορούν να χρησιμοποιήσουν τον ανελκυστήρα;", ["Μόνο το προσωπικό", "Άτομα με κινητικά προβλήματα, ηλικιωμένοι και όσοι έχουν καρότσι", "Όλοι οι επιβάτες με εισιτήριο", "Κανείς, γιατί είναι χαλασμένος"], 1, "Τα άτομα με κινητικά προβλήματα, οι ηλικιωμένοι και όσοι έχουν καρότσι μπορούν να χρησιμοποιούν τον ανελκυστήρα"),
 ],
 "gloss": {"κυλιόμενες σκάλες": "κυλιόμενη σκάλα — escalator", "συντήρησης": "συντήρηση — maintenance", "εκτός λειτουργίας": "εκτός λειτουργίας — out of service", "σταθερές": "σταθερός — fixed", "κινητικά προβλήματα": "κινητικά προβλήματα — mobility problems", "καρότσι": "καρότσι — pushchair", "ανελκυστήρα": "ανελκυστήρας — lift", "ταλαιπωρία": "ταλαιπωρία — inconvenience"},
})

ITEMS.append({
 "id": "l58-vm-archeio", "title": "Μήνυμα από τα Γενικά Αρχεία του Κράτους", "title_en": "A message from the State Archives", "type": "voicemail", "level": "B2",
 "context_el": "Ψάχνετε πληροφορίες για τον προπάππου σας και έχετε υποβάλει αίτηση στα Γενικά Αρχεία του Κράτους. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, κυρία Ζαφειρίου, σας τηλεφωνώ από τα Γενικά Αρχεία του Κράτους, σχετικά με την αίτησή σας για τον προπάππου σας, τον Αναστάσιο Ζαφειρίου. Έχω καλά νέα: βρήκαμε το όνομά του στα μητρώα αρρένων του Δήμου Ναυπλίου, καθώς και ένα έγγραφο από τη στρατιωτική του θητεία το 1912.", "Good morning, Mrs Zafeiriou, I'm calling from the State Archives about your request concerning your great-grandfather, Anastasios Zafeiriou. I have good news: we found his name in the male registers of the Municipality of Nafplio, as well as a document from his military service in 1912."),
  L("Υπάλληλος", "m", "Τα πρωτότυπα δεν μπορούν να βγουν από το αρχείο, αλλά μπορείτε να τα δείτε στο αναγνωστήριό μας, από Δευτέρα έως Παρασκευή, εννιά με τρεις. Αν θέλετε ψηφιακά αντίγραφα, θα σας τα στείλουμε με ηλεκτρονικό ταχυδρομείο, με μια μικρή χρέωση.", "The originals cannot leave the archive, but you can see them in our reading room, Monday to Friday, nine to three. If you want digital copies, we'll send them by email, for a small charge."),
  L("Υπάλληλος", "m", "Όταν έρθετε, φέρτε μαζί σας την αστυνομική σας ταυτότητα. Καλή συνέχεια.", "When you come, bring your identity card with you. Have a good day."),
 ],
 "questions": [
  Q("Τι βρήκαν τα Αρχεία;", ["Μια φωτογραφία του προπάππου", "Το όνομά του στα μητρώα αρρένων και ένα έγγραφο από τη θητεία του", "Το σπίτι όπου γεννήθηκε", "Τη διαθήκη του"], 1, "βρήκαμε το όνομά του στα μητρώα αρρένων του Δήμου Ναυπλίου, καθώς και ένα έγγραφο από τη στρατιωτική του θητεία"),
  Q("Πού μπορεί η κυρία Ζαφειρίου να δει τα πρωτότυπα;", ["Στο σπίτι της", "Στο αναγνωστήριο των Αρχείων", "Στο Δημαρχείο Ναυπλίου", "Σε ένα μουσείο"], 1, "μπορείτε να τα δείτε στο αναγνωστήριό μας"),
  Q("Τι πρέπει να φέρει μαζί της;", ["Την αίτηση", "Την αστυνομική της ταυτότητα", "Ένα φλασάκι", "Χρήματα σε μετρητά"], 1, "φέρτε μαζί σας την αστυνομική σας ταυτότητα"),
 ],
 "gloss": {"προπάππου": "προπάππους — great-grandfather", "μητρώα αρρένων": "μητρώο αρρένων — register of male citizens", "έγγραφο": "έγγραφο — document", "θητεία": "θητεία — (military) service", "πρωτότυπα": "πρωτότυπο — original", "αναγνωστήριό": "αναγνωστήριο — reading room", "αντίγραφα": "αντίγραφο — copy", "χρέωση": "χρέωση — charge"},
})

ITEMS.append({
 "id": "l58-dia-tenis", "title": "Κράτηση γηπέδου τένις", "title_en": "Booking a tennis court", "type": "dialogue", "level": "B2",
 "context_el": "Ένας άντρας τηλεφωνεί σε έναν όμιλο αντισφαίρισης για να κλείσει γήπεδο. Θα ακούσετε τη συζήτησή του με τη γραμματέα.",
 "script": [
  L("Πελάτης", "m", "Καλησπέρα σας. Θα ήθελα να κλείσω ένα γήπεδο για την Κυριακή το πρωί, για δύο άτομα. Δεν είμαστε μέλη του ομίλου.", "Good evening. I'd like to book a court for Sunday morning, for two people. We're not members of the club."),
  L("Γραμματέας", "f", "Τις Κυριακές τα πρωινά τα γήπεδα είναι κλεισμένα από τα μέλη μέχρι τις δώδεκα. Μπορώ να σας δώσω ένα γήπεδο από τις δώδεκα μέχρι τη μία, αλλά τότε ο ήλιος θα είναι αρκετά δυνατός.", "On Sunday mornings the courts are booked by members until twelve. I can give you a court from twelve to one, but the sun will be quite strong then."),
  L("Πελάτης", "m", "Μήπως έχετε κάτι νωρίς το Σάββατο;", "Do you perhaps have something early on Saturday?"),
  L("Γραμματέας", "f", "Ναι, το Σάββατο στις οχτώ έχω ελεύθερο το γήπεδο τρία, με χωμάτινη επιφάνεια. Η τιμή για μη μέλη είναι δεκαπέντε ευρώ την ώρα. Αν χρειάζεστε ρακέτες, τις νοικιάζουμε με τρία ευρώ η μία.", "Yes, on Saturday at eight court three is free, a clay court. The price for non-members is fifteen euros an hour. If you need rackets, we rent them for three euros each."),
  L("Πελάτης", "m", "Τέλεια, θα το πάρουμε. Ρακέτες έχουμε, αλλά όχι μπαλάκια.", "Perfect, we'll take it. We have rackets, but no balls."),
  L("Γραμματέας", "f", "Μπαλάκια πουλάμε στη γραμματεία. Προσοχή μόνο: στο χωμάτινο γήπεδο είναι υποχρεωτικά τα ειδικά παπούτσια τένις, χωρίς μαύρη σόλα. Και αν ακυρώσετε, ενημερώστε μας τουλάχιστον μια μέρα νωρίτερα.", "We sell balls at the office. Just note: on the clay court special tennis shoes, without black soles, are compulsory. And if you cancel, let us know at least a day in advance."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί ο πελάτης να παίξει την Κυριακή το πρωί;", ["Γιατί το γήπεδο επισκευάζεται", "Γιατί τα γήπεδα είναι κλεισμένα από τα μέλη μέχρι τις δώδεκα", "Γιατί ο όμιλος είναι κλειστός", "Γιατί έχει αγώνες"], 1, "Τις Κυριακές τα πρωινά τα γήπεδα είναι κλεισμένα από τα μέλη μέχρι τις δώδεκα"),
  Q("Τι πρέπει να αγοράσουν οι παίκτες;", ["Ρακέτες", "Μπαλάκια", "Κάρτα μέλους", "Πετσέτες"], 1, "Ρακέτες έχουμε, αλλά όχι μπαλάκια"),
  Q("Ποιος κανόνας ισχύει για το χωμάτινο γήπεδο;", ["Απαγορεύεται να παίζουν πάνω από δύο άτομα", "Είναι υποχρεωτικά τα ειδικά παπούτσια τένις χωρίς μαύρη σόλα", "Πρέπει να το ποτίσουν μετά το παιχνίδι", "Δεν επιτρέπεται το παιχνίδι με βροχή"], 1, "στο χωμάτινο γήπεδο είναι υποχρεωτικά τα ειδικά παπούτσια τένις, χωρίς μαύρη σόλα"),
 ],
 "gloss": {"ομίλου": "όμιλος — club", "αντισφαίρισης": "αντισφαίριση — tennis (formal)", "χωμάτινη": "χωμάτινος — clay, earth", "επιφάνεια": "επιφάνεια — surface", "ρακέτες": "ρακέτα — racket", "μπαλάκια": "μπαλάκι — (tennis) ball", "σόλα": "σόλα — sole", "υποχρεωτικά": "υποχρεωτικός — compulsory"},
})

ITEMS.append({
 "id": "l58-dia-skala", "title": "Η σκάλα του γείτονα", "title_en": "The neighbour's ladder", "type": "dialogue", "level": "B2",
 "context_el": "Μια γυναίκα χτυπά την πόρτα του γείτονά της για να του ζητήσει κάτι. Θα ακούσετε τη συζήτησή τους.",
 "script": [
  L("Ρένα", "f", "Καλημέρα, κύριε Θανάση. Συγγνώμη που σας ενοχλώ τόσο πρωί. Μήπως έχετε μια ψηλή σκάλα να μου δανείσετε; Κάηκε η λάμπα στο ταβάνι του σαλονιού και δεν φτάνω.", "Good morning, Mr Thanasis. Sorry to bother you so early. Do you perhaps have a tall ladder you could lend me? The bulb in the living-room ceiling has gone and I can't reach."),
  L("Θανάσης", "m", "Βεβαίως, έχω μια αλουμινένια στην αποθήκη. Αλλά προσέξτε, είναι λίγο βαριά. Θέλετε να έρθω να σας βοηθήσω; Δεν είναι καλό να ανεβαίνετε μόνη σας χωρίς κάποιον να κρατάει τη σκάλα.", "Of course, I have an aluminium one in the storeroom. But be careful, it's a bit heavy. Do you want me to come and help? It's not good to climb up on your own without someone holding the ladder."),
  L("Ρένα", "f", "Θα ήταν υπέροχο, αν δεν σας χαλάω το πρόγραμμα. Η αλήθεια είναι ότι φοβάμαι λίγο τα ύψη.", "That would be wonderful, if I'm not spoiling your plans. The truth is I'm a little afraid of heights."),
  L("Θανάσης", "m", "Κανένα πρόβλημα, έχω χρόνο ως τις έντεκα. Πριν την αλλάξουμε, όμως, να κατεβάσετε τον γενικό διακόπτη, για ασφάλεια. Έχετε καινούργια λάμπα;", "No problem, I have time until eleven. Before we change it, though, you should switch off the mains, for safety. Do you have a new bulb?"),
  L("Ρένα", "f", "Ναι, αγόρασα χθες μια λάμπα εξοικονόμησης ενέργειας. Ελάτε μετά να σας κεράσω έναν καφέ, σας παρακαλώ.", "Yes, I bought an energy-saving bulb yesterday. Please come afterwards and let me treat you to a coffee."),
 ],
 "questions": [
  Q("Τι χρειάζεται η Ρένα;", ["Ένα κατσαβίδι", "Μια ψηλή σκάλα", "Μια καινούργια λάμπα", "Έναν ηλεκτρολόγο"], 1, "Μήπως έχετε μια ψηλή σκάλα να μου δανείσετε;"),
  Q("Γιατί προτείνει ο Θανάσης να τη βοηθήσει;", ["Γιατί η σκάλα είναι χαλασμένη", "Γιατί δεν είναι καλό να ανεβαίνει μόνη της χωρίς κάποιον να κρατάει τη σκάλα", "Γιατί εκείνη δεν ξέρει να αλλάζει λάμπες", "Γιατί θέλει να δει το σπίτι της"], 1, "Δεν είναι καλό να ανεβαίνετε μόνη σας χωρίς κάποιον να κρατάει τη σκάλα"),
  Q("Τι πρέπει να κάνει η Ρένα πριν από την αλλαγή της λάμπας;", ["Να ανοίξει τα παράθυρα", "Να κατεβάσει τον γενικό διακόπτη", "Να καθαρίσει το ταβάνι", "Να αγοράσει άλλη λάμπα"], 1, "να κατεβάσετε τον γενικό διακόπτη, για ασφάλεια"),
 ],
 "gloss": {"σκάλα": "σκάλα — ladder; stairs", "δανείσετε": "δανείζω — to lend", "ταβάνι": "ταβάνι — ceiling", "αλουμινένια": "αλουμινένιος — aluminium", "αποθήκη": "αποθήκη — storeroom", "γενικό διακόπτη": "γενικός διακόπτης — mains switch", "εξοικονόμησης ενέργειας": "εξοικονόμηση ενέργειας — energy saving", "κεράσω": "κερνώ — to treat (someone to something)"},
})

ITEMS.append({
 "id": "l58-int-varelas", "title": "Ο τελευταίος βαρελάς", "title_en": "The last cooper", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για τα παραδοσιακά επαγγέλματα, ο δημοσιογράφος μιλά με έναν βαρελά από τη Νεμέα.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Λάμπρο, είστε από τους λίγους βαρελάδες που έχουν μείνει στην Ελλάδα. Πώς ξεκινήσατε;", "Mr Lambros, you're one of the few coopers left in Greece. How did you start?"),
  L("Βαρελάς", "m", "Το εργαστήρι το άνοιξε ο παππούς μου το 1938. Εγώ μπήκα μέσα δώδεκα χρονών, τα καλοκαίρια, και έμαθα κοιτάζοντας. Τότε κάθε χωριό με αμπέλια είχε τον βαρελά του. Μετά ήρθαν οι ανοξείδωτες δεξαμενές και η δουλειά σχεδόν χάθηκε.", "The workshop was opened by my grandfather in 1938. I started there at twelve, in the summers, and learned by watching. Back then every village with vineyards had its cooper. Then stainless-steel tanks came and the trade almost disappeared."),
  L("Δημοσιογράφος", "f", "Και σήμερα; Ποιος αγοράζει βαρέλια;", "And today? Who buys barrels?"),
  L("Βαρελάς", "m", "Τα τελευταία χρόνια τα μικρά οινοποιεία ξαναζήτησαν το βαρέλι, γιατί το ξύλο δίνει στο κρασί άρωμα και χαρακτήρα. Χρησιμοποιώ κυρίως δρυ από τα δάση της Ευρυτανίας. Το ξύλο πρέπει να στεγνώσει στον ανοιχτό αέρα δύο με τρία χρόνια πριν το δουλέψω.", "In recent years small wineries have started asking for barrels again, because the wood gives the wine aroma and character. I mainly use oak from the forests of Evrytania. The wood has to dry in the open air for two to three years before I work it."),
  L("Δημοσιογράφος", "f", "Ποιο είναι το πιο δύσκολο στάδιο;", "What's the hardest stage?"),
  L("Βαρελάς", "m", "Το λύγισμα των σανίδων. Τις ζεσταίνουμε πάνω από φωτιά και τις βρέχουμε, ώσπου να λυγίσουν χωρίς να σπάσουν. Αν βιαστείς, χάνεις ολόκληρο το βαρέλι. Αυτή η δουλειά θέλει υπομονή, όπως και το κρασί.", "Bending the staves. We heat them over a fire and wet them until they bend without breaking. If you rush, you lose the whole barrel. This work needs patience, like wine."),
 ],
 "questions": [
  Q("Γιατί η δουλειά του βαρελά σχεδόν χάθηκε;", ["Γιατί έκλεισαν τα αμπέλια", "Γιατί ήρθαν οι ανοξείδωτες δεξαμενές", "Γιατί ακρίβυνε το ξύλο", "Γιατί απαγορεύτηκε από τον νόμο"], 1, "Μετά ήρθαν οι ανοξείδωτες δεξαμενές και η δουλειά σχεδόν χάθηκε"),
  Q("Γιατί τα μικρά οινοποιεία ξαναζητούν βαρέλια;", ["Γιατί είναι φθηνότερα", "Γιατί το ξύλο δίνει στο κρασί άρωμα και χαρακτήρα", "Γιατί είναι πιο ελαφριά", "Γιατί το ζητάει η Ευρωπαϊκή Ένωση"], 1, "γιατί το ξύλο δίνει στο κρασί άρωμα και χαρακτήρα"),
  Q("Ποιο είναι το πιο δύσκολο στάδιο της κατασκευής;", ["Το κόψιμο του δέντρου", "Το λύγισμα των σανίδων", "Το βάψιμο", "Η μεταφορά"], 1, "Το λύγισμα των σανίδων"),
 ],
 "gloss": {"τον βαρελά": "βαρελάς — cooper", "βαρελάδες": "βαρελάς — cooper", "ανοξείδωτες": "ανοξείδωτος — stainless", "δεξαμενές": "δεξαμενή — tank", "οινοποιεία": "οινοποιείο — winery", "δρυ": "δρυς — oak", "λύγισμα": "λύγισμα — bending", "σανίδων": "σανίδα — plank, stave"},
})

ITEMS.append({
 "id": "l58-rep-zalongo", "title": "Το Ζάλογγο και η μνήμη του Σουλίου", "title_en": "Zalongo and the memory of Souli", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από την Ήπειρο, για ένα μνημείο με μεγάλη ιστορική σημασία.",
 "script": [
  L("Ρεπόρτερ", "m", "Βρισκόμαστε στο Ζάλογγο, λίγα χιλιόμετρα βόρεια της Πρέβεζας. Πάνω στον βράχο δεσπόζει ένα τεράστιο γλυπτό με γυναικείες μορφές, ορατό από χιλιόμετρα μακριά. Είναι το μνημείο για τις Σουλιώτισσες, που, σύμφωνα με την παράδοση, έπεσαν στον γκρεμό το 1803 για να μην πιαστούν αιχμάλωτες από τα στρατεύματα του Αλή Πασά.", "We're at Zalongo, a few kilometres north of Preveza. On the rock stands a huge sculpture of female figures, visible from miles away. It's the monument to the women of Souli who, according to tradition, threw themselves off the cliff in 1803 so as not to be taken prisoner by the troops of Ali Pasha."),
  L("Ρεπόρτερ", "m", "Το Σούλι, μια ομάδα ορεινών χωριών στη Θεσπρωτία, είχε αντισταθεί για χρόνια στον Αλή Πασά. Η ιστορία του χορού των γυναικών στην άκρη του γκρεμού έγινε θρύλος και τραγούδι. Οι ιστορικοί σημειώνουν ότι κάποιες λεπτομέρειες προστέθηκαν αργότερα, όμως η θυσία ανθρώπων στο Ζάλογγο είναι γεγονός.", "Souli, a group of mountain villages in Thesprotia, had resisted Ali Pasha for years. The story of the women's dance at the edge of the cliff became legend and song. Historians note that some details were added later, but the sacrifice of people at Zalongo is a fact."),
  L("Ρεπόρτερ", "m", "Για να φτάσει κανείς στο μνημείο πρέπει να ανέβει περίπου τετρακόσια πενήντα σκαλοπάτια. Από την κορυφή η θέα απλώνεται ως τον Αμβρακικό κόλπο και το Ιόνιο. Δίπλα βρίσκονται τα ερείπια της αρχαίας Κασσώπης, που αξίζει επίσης μια επίσκεψη.", "To reach the monument you have to climb about four hundred and fifty steps. From the top the view stretches to the Ambracian Gulf and the Ionian. Nearby are the ruins of ancient Kassope, which is also worth a visit."),
 ],
 "questions": [
  Q("Τι αναπαριστά το γλυπτό του Ζαλόγγου;", ["Στρατιώτες του Αλή Πασά", "Γυναικείες μορφές, τις Σουλιώτισσες", "Έναν αρχαίο θεό", "Ψαράδες της Πρέβεζας"], 1, "ένα τεράστιο γλυπτό με γυναικείες μορφές ... το μνημείο για τις Σουλιώτισσες"),
  Q("Τι λένε οι ιστορικοί για την ιστορία του χορού;", ["Ότι είναι εντελώς φανταστική", "Ότι κάποιες λεπτομέρειες προστέθηκαν αργότερα, αλλά η θυσία είναι γεγονός", "Ότι έγινε το 1903", "Ότι δεν έγινε στο Ζάλογγο"], 1, "κάποιες λεπτομέρειες προστέθηκαν αργότερα, όμως η θυσία ανθρώπων στο Ζάλογγο είναι γεγονός"),
  Q("Τι υπάρχει κοντά στο μνημείο;", ["Ένα κάστρο του Αλή Πασά", "Τα ερείπια της αρχαίας Κασσώπης", "Ένα μοναστήρι", "Μια παραλία"], 1, "Δίπλα βρίσκονται τα ερείπια της αρχαίας Κασσώπης"),
 ],
 "gloss": {"δεσπόζει": "δεσπόζω — to dominate, tower over", "γλυπτό": "γλυπτό — sculpture", "γκρεμό": "γκρεμός — cliff", "αιχμάλωτες": "αιχμάλωτος — prisoner", "στρατεύματα": "στράτευμα — troops", "θρύλος": "θρύλος — legend", "θυσία": "θυσία — sacrifice", "ερείπια": "ερείπιο — ruin"},
})

ITEMS.append({
 "id": "l58-dia-mathima-kolymvisis", "title": "Μαθήματα κολύμβησης για ενήλικες", "title_en": "Swimming lessons for adults", "type": "dialogue", "level": "B2",
 "context_el": "Μια γυναίκα πενήντα χρονών ζητά πληροφορίες σε ένα κολυμβητικό κέντρο. Θα ακούσετε τη συζήτησή της με τον προπονητή.",
 "script": [
  L("Μαρίνα", "f", "Καλησπέρα. Θα σας φανεί αστείο, αλλά είμαι πενήντα χρονών και δεν ξέρω κολύμπι. Έχετε τμήματα για ενήλικες αρχάριους;", "Good evening. It'll sound funny to you, but I'm fifty and I can't swim. Do you have classes for adult beginners?"),
  L("Προπονητής", "m", "Καθόλου αστείο, είναι πολύ πιο συνηθισμένο απ’ όσο νομίζετε. Έχουμε τμήμα ενηλίκων Τρίτη και Πέμπτη στις οχτώ το βράδυ. Τα τμήματα είναι μικρά, έξι άτομα το πολύ, και ξεκινάμε στη ρηχή πισίνα, όπου πατάτε.", "Not funny at all; it's much more common than you think. We have an adult class on Tuesday and Thursday at eight in the evening. The groups are small, six people at most, and we start in the shallow pool, where you can stand."),
  L("Μαρίνα", "f", "Αυτό με καθησυχάζει. Η αλήθεια είναι ότι φοβάμαι το νερό από παιδί, όταν κόντεψα να πνιγώ σε μια παραλία.", "That reassures me. The truth is I've been afraid of water since I was a child, when I nearly drowned on a beach."),
  L("Προπονητής", "m", "Τότε το πρώτο μας βήμα δεν θα είναι το κολύμπι, αλλά η εξοικείωση με το νερό: να βάζετε το πρόσωπο μέσα, να επιπλέετε, να αναπνέετε σωστά. Δεν θα σας πιέσουμε. Χρειάζεστε μόνο σκουφάκι, γυαλάκια, σαγιονάρες και ιατρική βεβαίωση από παθολόγο.", "Then our first step won't be swimming but getting used to the water: putting your face in, floating, breathing properly. We won't push you. You only need a cap, goggles, flip-flops and a medical certificate from a GP."),
 ],
 "questions": [
  Q("Πόσα άτομα έχει το πολύ ένα τμήμα ενηλίκων;", ["Τέσσερα", "Έξι", "Δέκα", "Δώδεκα"], 1, "Τα τμήματα είναι μικρά, έξι άτομα το πολύ"),
  Q("Γιατί φοβάται η Μαρίνα το νερό;", ["Γιατί δεν έχει πάει ποτέ σε θάλασσα", "Γιατί κόντεψε να πνιγεί όταν ήταν παιδί", "Γιατί έχει πρόβλημα υγείας", "Γιατί δεν της αρέσει το κρύο"], 1, "φοβάμαι το νερό από παιδί, όταν κόντεψα να πνιγώ σε μια παραλία"),
  Q("Ποιο θα είναι το πρώτο βήμα στα μαθήματα;", ["Οι καταδύσεις", "Η εξοικείωση με το νερό", "Το κολύμπι σε βαθιά νερά", "Η γυμναστική έξω από την πισίνα"], 1, "το πρώτο μας βήμα δεν θα είναι το κολύμπι, αλλά η εξοικείωση με το νερό"),
 ],
 "gloss": {"αρχάριους": "αρχάριος — beginner", "ρηχή": "ρηχός — shallow", "πατάτε": "πατώ — to touch the bottom, stand", "καθησυχάζει": "καθησυχάζω — to reassure", "πνιγώ": "πνίγομαι — to drown", "εξοικείωση": "εξοικείωση — familiarisation", "επιπλέετε": "επιπλέω — to float", "βεβαίωση": "βεβαίωση — certificate"},
})

ITEMS.append({
 "id": "l58-mono-chovoli", "title": "Ο καφές στη χόβολη", "title_en": "Coffee in the embers", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν καφετζή σε ένα παλιό καφενείο της Ξάνθης να μιλά για τον τρόπο που φτιάχνει τον ελληνικό καφέ.",
 "script": [
  L("Καφετζής", "m", "Εδώ στο καφενείο ψήνουμε τον καφέ όπως τον έψηναν οι παλιοί, στη χόβολη. Έχω ένα μεγάλο χάλκινο ταψί γεμάτο ψιλή άμμο, που τη ζεσταίνω από κάτω με κάρβουνα. Χώνω το μπρίκι μέσα στην καυτή άμμο και ο καφές ψήνεται σιγά σιγά, απ’ όλες τις μεριές.", "Here in the café we make coffee the way the old people did, in the embers. I have a big copper tray full of fine sand, which I heat from below with charcoal. I push the briki into the hot sand and the coffee brews slowly, from all sides."),
  L("Καφετζής", "m", "Το μυστικό είναι να μη βιαστείς. Στο γκάζι ο καφές βράζει γρήγορα και χάνει το καϊμάκι του. Στην άμμο ανεβαίνει αργά, και ο αφρός μένει πυκνός και βελούδινος. Μόλις φουσκώσει, τον τραβάω αμέσως, πριν ξεχειλίσει.", "The secret is not to rush. On gas the coffee boils quickly and loses its kaimaki. In the sand it rises slowly, and the foam stays thick and velvety. As soon as it swells, I pull it out at once, before it boils over."),
  L("Καφετζής", "m", "Τον σερβίρουμε πάντα με ένα ποτήρι κρύο νερό και ένα λουκούμι. Οι πελάτες μου κάθονται ώρες, παίζουν τάβλι και συζητούν. Ο καφές στη χόβολη δεν είναι απλώς ρόφημα, είναι λόγος να καθίσεις και να μιλήσεις με τον άλλον.", "We always serve it with a glass of cold water and a loukoumi. My customers sit for hours, play backgammon and talk. Coffee in the embers isn't just a drink; it's a reason to sit and talk with someone."),
 ],
 "questions": [
  Q("Πώς ζεσταίνεται η άμμος στο ταψί;", ["Με ηλεκτρικό ρεύμα", "Με κάρβουνα από κάτω", "Με γκάζι", "Στον ήλιο"], 1, "τη ζεσταίνω από κάτω με κάρβουνα"),
  Q("Γιατί ο καφές στην άμμο είναι καλύτερος, κατά τον καφετζή;", ["Γιατί είναι πιο γλυκός", "Γιατί ανεβαίνει αργά και ο αφρός μένει πυκνός", "Γιατί είναι πιο ζεστός", "Γιατί χρειάζεται λιγότερο καφέ"], 1, "Στην άμμο ανεβαίνει αργά, και ο αφρός μένει πυκνός και βελούδινος"),
  Q("Τι σημαίνει, για τον καφετζή, ο καφές στη χόβολη;", ["Μια ακριβή πολυτέλεια", "Έναν λόγο να καθίσεις και να μιλήσεις με τον άλλον", "Μια τουριστική ατραξιόν", "Ένα φάρμακο για το στομάχι"], 1, "είναι λόγος να καθίσεις και να μιλήσεις με τον άλλον"),
 ],
 "gloss": {"χόβολη": "χόβολη — embers, hot ash", "χάλκινο": "χάλκινος — copper", "ταψί": "ταψί — tray", "κάρβουνα": "κάρβουνο — charcoal", "μπρίκι": "μπρίκι — briki, small coffee pot", "καϊμάκι": "καϊμάκι — the foam on Greek coffee", "ξεχειλίσει": "ξεχειλίζω — to boil over, overflow", "ρόφημα": "ρόφημα — (hot) drink"},
})

ITEMS.append({
 "id": "l58-c1-erimosi", "title": "Η ερήμωση των ορεινών χωριών", "title_en": "The depopulation of mountain villages", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την ελληνική ύπαιθρο, η δημοσιογράφος συζητά με μια δημογράφο για το μέλλον των ορεινών χωριών.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Κουτσούκη, πόσο σοβαρό είναι το φαινόμενο της ερήμωσης στα ορεινά της χώρας;", "Ms Koutsouki, how serious is the depopulation of the country's mountain areas?"),
  L("Δημογράφος", "f", "Πολύ σοβαρό. Σύμφωνα με τις απογραφές, εκατοντάδες χωριά έχουν σήμερα λιγότερους από δέκα μόνιμους κατοίκους, και κάποια έχουν εγκαταλειφθεί εντελώς. Η διαδικασία ξεκίνησε μεταπολεμικά, με την αστυφιλία και τη μετανάστευση, και επιταχύνθηκε από τη γήρανση του πληθυσμού. Όταν κλείνει το σχολείο, το χωριό έχει ουσιαστικά υπογράψει τη θανατική του καταδίκη.", "Very serious. According to the censuses, hundreds of villages today have fewer than ten permanent residents, and some have been abandoned completely. The process began after the war, with the drift to the cities and emigration, and was accelerated by population ageing. When the school closes, the village has essentially signed its own death sentence."),
  L("Δημοσιογράφος", "m", "Βλέπουμε, όμως, και κάποιες αντίθετες τάσεις. Νέοι που επιστρέφουν, ψηφιακοί νομάδες…", "But we also see some opposite trends. Young people returning, digital nomads…"),
  L("Δημογράφος", "f", "Υπάρχουν, και είναι ενθαρρυντικές, αλλά δεν πρέπει να τις υπερεκτιμούμε. Η τηλεργασία επέτρεψε σε ορισμένους να εγκατασταθούν στην ύπαιθρο, κυρίως όμως σε χωριά κοντά σε πόλεις και με καλή σύνδεση στο διαδίκτυο. Για να κρατηθεί κάποιος σε ένα απομακρυσμένο χωριό, χρειάζεται κάτι παραπάνω από ένα ρομαντικό όνειρο: γιατρό, σχολείο, συγκοινωνία, δουλειά για τον σύντροφο.", "They exist, and they're encouraging, but we shouldn't overestimate them. Remote work has allowed some people to settle in the countryside, but mainly in villages near towns with a good internet connection. To keep someone in a remote village you need more than a romantic dream: a doctor, a school, transport, work for their partner."),
  L("Δημοσιογράφος", "m", "Τι πολιτικές θα προτείνατε;", "What policies would you propose?"),
  L("Δημογράφος", "f", "Πρώτα απ’ όλα, να σταματήσουμε να σχεδιάζουμε τις υπηρεσίες με αποκλειστικό κριτήριο τον αριθμό των χρηστών. Ένα σχολείο με οχτώ μαθητές μπορεί να φαίνεται ασύμφορο στα χαρτιά, αλλά το κόστος του κλεισίματός του, για την κοινότητα, είναι ανυπολόγιστο. Χρειαζόμαστε επίσης κίνητρα για την αξιοποίηση των εγκαταλειμμένων σπιτιών και, κυρίως, μακροπρόθεσμο σχεδιασμό, όχι αποσπασματικά προγράμματα που λήγουν με την επόμενη κυβέρνηση.", "First of all, we must stop designing services solely on the basis of the number of users. A school with eight pupils may look uneconomic on paper, but the cost of closing it, for the community, is incalculable. We also need incentives to make use of abandoned houses and, above all, long-term planning, not piecemeal programmes that end with the next government."),
 ],
 "questions": [
  Q("Ποια ήταν, κατά τη δημογράφο, η αρχική αιτία της ερήμωσης;", ["Οι φυσικές καταστροφές", "Η αστυφιλία και η μετανάστευση μεταπολεμικά", "Η έλλειψη νερού", "Οι υψηλοί φόροι"], 1, "Η διαδικασία ξεκίνησε μεταπολεμικά, με την αστυφιλία και τη μετανάστευση"),
  Q("Πώς κρίνει η δημογράφος την επιστροφή νέων και ψηφιακών νομάδων;", ["Τη θεωρεί λύση του προβλήματος", "Ενθαρρυντική, αλλά περιορισμένη κυρίως σε χωριά κοντά σε πόλεις", "Επικίνδυνη για τις τοπικές κοινωνίες", "Ανύπαρκτη"], 1, "είναι ενθαρρυντικές, αλλά δεν πρέπει να τις υπερεκτιμούμε ... κυρίως όμως σε χωριά κοντά σε πόλεις"),
  Q("Τι υποστηρίζει για ένα σχολείο με οχτώ μαθητές;", ["Ότι πρέπει να κλείσει για οικονομία", "Ότι το κόστος του κλεισίματός του για την κοινότητα είναι ανυπολόγιστο", "Ότι πρέπει να ενωθεί με άλλο σχολείο", "Ότι πρέπει να γίνει ιδιωτικό"], 1, "το κόστος του κλεισίματός του, για την κοινότητα, είναι ανυπολόγιστο"),
  Q("Ποιο είναι, κατά τη δημογράφο, το κυριότερο που χρειάζεται;", ["Περισσότερος τουρισμός", "Μακροπρόθεσμος σχεδιασμός", "Νέοι δρόμοι", "Μεγαλύτερες συντάξεις"], 1, "κυρίως, μακροπρόθεσμο σχεδιασμό, όχι αποσπασματικά προγράμματα"),
 ],
 "gloss": {"ερήμωσης": "ερήμωση — depopulation, desertion", "απογραφές": "απογραφή — census", "αστυφιλία": "αστυφιλία — drift to the cities", "γήρανση": "γήρανση — ageing", "θανατική": "θανατική καταδίκη — death sentence", "υπερεκτιμούμε": "υπερεκτιμώ — to overestimate", "ασύμφορο": "ασύμφορος — uneconomic", "ανυπολόγιστο": "ανυπολόγιστος — incalculable", "κίνητρα": "κίνητρο — incentive", "αποσπασματικά": "αποσπασματικός — piecemeal"},
})

ITEMS.append({
 "id": "l58-c1-orlofika", "title": "Τα Ορλωφικά", "title_en": "The Orlov revolt", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για μια εξέγερση των Ελλήνων τον 18ο αιώνα.",
 "script": [
  L("Ιστορικός", "m", "Πενήντα χρόνια πριν από την Επανάσταση του 1821, η Πελοπόννησος γνώρισε μια εξέγερση που έμεινε στην ιστορία με το όνομα «Ορλωφικά». Το 1770, στο πλαίσιο του Ρωσοτουρκικού πολέμου, η αυτοκράτειρα της Ρωσίας Αικατερίνη η Μεγάλη έστειλε στο Αιγαίο έναν στόλο υπό τους αδελφούς Ορλόφ. Στόχος της ήταν να ανοίξει ένα δεύτερο μέτωπο εναντίον των Οθωμανών, ξεσηκώνοντας τους ορθόδοξους υπηκόους τους.", "Fifty years before the Revolution of 1821, the Peloponnese saw an uprising that went down in history as the Orlov revolt. In 1770, during the Russo-Turkish War, Catherine the Great of Russia sent a fleet to the Aegean under the Orlov brothers. Her aim was to open a second front against the Ottomans by stirring up their Orthodox subjects."),
  L("Ιστορικός", "m", "Οι Έλληνες, και ιδιαίτερα οι Μανιάτες, πίστεψαν ότι είχε έρθει η ώρα της απελευθέρωσης. Όμως η ρωσική δύναμη που αποβιβάστηκε ήταν ελάχιστη, ασύγκριτα μικρότερη από όσο περίμεναν. Μετά από κάποιες αρχικές επιτυχίες, οι εξεγερμένοι ηττήθηκαν, και οι Ρώσοι αποχώρησαν. Στην αποτυχία συνέβαλε και η έλλειψη συντονισμού ανάμεσα στους ίδιους τους Έλληνες.", "The Greeks, and especially the Maniots, believed that the hour of liberation had come. But the Russian force that landed was tiny, incomparably smaller than they had expected. After some initial successes, the insurgents were defeated and the Russians withdrew. The lack of coordination among the Greeks themselves also contributed to the failure."),
  L("Ιστορικός", "m", "Τα αντίποινα ήταν τρομερά. Για σχεδόν μια δεκαετία η Πελοπόννησος λεηλατήθηκε από αλβανικά άτακτα σώματα, που η Πύλη είχε καλέσει για να καταστείλει την εξέγερση και που στη συνέχεια δεν μπορούσε να ελέγξει. Το μάθημα που πήραν πολλοί Έλληνες ήταν σκληρό, αλλά πολύτιμο: η ελευθερία δεν θα ερχόταν ως δώρο από μια ξένη δύναμη, που ενεργούσε πρωτίστως για τα δικά της συμφέροντα. Η ιδέα αυτή θα ωριμάσει στις επόμενες δεκαετίες και θα αποτελέσει ένα από τα θεμέλια της Φιλικής Εταιρείας.", "The reprisals were terrible. For almost a decade the Peloponnese was plundered by Albanian irregular troops, whom the Porte had called in to suppress the revolt and then could not control. The lesson many Greeks drew was harsh but valuable: freedom would not come as a gift from a foreign power acting primarily in its own interests. This idea would mature over the following decades and become one of the foundations of the Filiki Etaireia."),
 ],
 "questions": [
  Q("Ποιος ήταν ο στόχος της Αικατερίνης της Μεγάλης;", ["Να κατακτήσει την Πελοπόννησο", "Να ανοίξει δεύτερο μέτωπο εναντίον των Οθωμανών", "Να ιδρύσει ελληνικό κράτος", "Να προστατέψει το εμπόριο στο Αιγαίο"], 1, "Στόχος της ήταν να ανοίξει ένα δεύτερο μέτωπο εναντίον των Οθωμανών"),
  Q("Γιατί απέτυχε η εξέγερση, σύμφωνα με τον ομιλητή;", ["Γιατί οι Έλληνες δεν ήθελαν να πολεμήσουν", "Γιατί η ρωσική δύναμη ήταν ελάχιστη και έλειπε ο συντονισμός", "Γιατί οι Μανιάτες συμμάχησαν με τους Οθωμανούς", "Γιατί ο στόλος βυθίστηκε"], 1, "η ρωσική δύναμη που αποβιβάστηκε ήταν ελάχιστη ... Στην αποτυχία συνέβαλε και η έλλειψη συντονισμού"),
  Q("Τι συνέβη μετά την αποτυχία;", ["Υπογράφηκε ειρήνη που ωφέλησε τους Έλληνες", "Η Πελοπόννησος λεηλατήθηκε για σχεδόν μια δεκαετία", "Οι Ρώσοι έμειναν στην Πελοπόννησο", "Ιδρύθηκε η Φιλική Εταιρεία"], 1, "Για σχεδόν μια δεκαετία η Πελοπόννησος λεηλατήθηκε από αλβανικά άτακτα σώματα"),
  Q("Ποιο μάθημα πήραν οι Έλληνες;", ["Ότι η Ρωσία ήταν ο μόνος σύμμαχός τους", "Ότι η ελευθερία δεν θα ερχόταν ως δώρο από μια ξένη δύναμη", "Ότι έπρεπε να αποφεύγουν τον πόλεμο", "Ότι η Μάνη έπρεπε να γίνει ανεξάρτητη"], 1, "η ελευθερία δεν θα ερχόταν ως δώρο από μια ξένη δύναμη"),
 ],
 "gloss": {"εξέγερση": "εξέγερση — uprising, revolt", "αυτοκράτειρα": "αυτοκράτειρα — empress", "μέτωπο": "μέτωπο — front", "υπηκόους": "υπήκοος — subject", "αποβιβάστηκε": "αποβιβάζομαι — to land, disembark", "συντονισμού": "συντονισμός — coordination", "αντίποινα": "αντίποινα — reprisals", "λεηλατήθηκε": "λεηλατώ — to plunder", "άτακτα σώματα": "άτακτα σώματα — irregular troops", "καταστείλει": "καταστέλλω — to suppress"},
})

rnd = random.Random(58)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-58.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
