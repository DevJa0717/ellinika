# Source for library/listening/listening-19.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l19.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l19-ann-tram", "title": "Αλλαγές στα δρομολόγια του τραμ", "title_en": "Changes to the tram timetable", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση μέσα σε έναν συρμό του τραμ.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί επιβάτες, σας ενημερώνουμε ότι από το Σάββατο και για τρεις εβδομάδες η γραμμή του τραμ προς την παραλία θα τερματίζει στη στάση «Πλατεία», λόγω εργασιών αντικατάστασης των σιδηροτροχιών.", "Dear passengers, we inform you that from Saturday and for three weeks the tram line towards the seafront will terminate at the 'Square' stop, due to work replacing the rails."),
  L("Εκφωνητής", "m", "Από την «Πλατεία» ως το τέρμα θα εκτελούνται δρομολόγια με λεωφορεία, κάθε δέκα λεπτά. Τα εισιτήρια και οι κάρτες που ισχύουν για το τραμ ισχύουν και για τα λεωφορεία αυτά, χωρίς νέα επικύρωση, εφόσον δεν έχουν περάσει ενενήντα λεπτά.", "From the 'Square' to the terminus, buses will run every ten minutes. Tickets and cards valid for the tram are also valid on these buses, without validating again, as long as ninety minutes have not passed."),
  L("Εκφωνητής", "m", "Τα βράδια της Παρασκευής και του Σαββάτου τα δρομολόγια θα παρατείνονται ως τις δύο τα ξημερώματα. Ζητούμε την κατανόησή σας για την ταλαιπωρία.", "On Friday and Saturday nights the services will be extended until two in the morning. We ask for your understanding for the inconvenience."),
 ],
 "questions": [
  Q("Γιατί δεν θα φτάνει το τραμ ως την παραλία;", ["Λόγω απεργίας", "Λόγω αντικατάστασης των σιδηροτροχιών", "Λόγω ενός ατυχήματος", "Λόγω μιας συναυλίας"], 1, "λόγω εργασιών αντικατάστασης των σιδηροτροχιών"),
  Q("Τι ισχύει για τα εισιτήρια;", ["Χρειάζεται νέο εισιτήριο για το λεωφορείο", "Ισχύουν και στο λεωφορείο χωρίς νέα επικύρωση, μέσα σε ενενήντα λεπτά", "Τα λεωφορεία είναι δωρεάν όλη μέρα", "Ισχύουν μόνο οι μηνιαίες κάρτες"], 1, "ισχύουν και για τα λεωφορεία αυτά, χωρίς νέα επικύρωση, εφόσον δεν έχουν περάσει ενενήντα λεπτά"),
  Q("Τι αλλάζει τα βράδια της Παρασκευής και του Σαββάτου;", ["Δεν θα υπάρχουν δρομολόγια", "Τα δρομολόγια θα παρατείνονται ως τις δύο", "Τα λεωφορεία θα περνούν κάθε μισή ώρα", "Το τραμ θα φτάνει κανονικά ως την παραλία"], 1, "τα δρομολόγια θα παρατείνονται ως τις δύο τα ξημερώματα"),
 ],
 "gloss": {"συρμό": "συρμός — train (set of carriages)", "τερματίζει": "τερματίζω — to terminate (a route)", "αντικατάστασης": "αντικατάσταση — replacement", "σιδηροτροχιών": "σιδηροτροχιά — rail, track", "τέρμα": "τέρμα — terminus", "επικύρωση": "επικύρωση — validation (of a ticket)", "εφόσον": "εφόσον — as long as, provided that", "θα παρατείνονται": "παρατείνομαι — to be extended", "ξημερώματα": "ξημερώματα — early hours of the morning", "ταλαιπωρία": "ταλαιπωρία — inconvenience, hassle"},
})

ITEMS.append({
 "id": "l19-vm-katharistirio", "title": "Μήνυμα από το καθαριστήριο", "title_en": "A message from the dry cleaner's", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από ένα καθαριστήριο.",
 "script": [
  L("Υπάλληλος", "f", "Καλησπέρα σας, σας καλώ από το καθαριστήριο «Λευκό» για το παλτό που μας φέρατε την Τρίτη. Δυστυχώς, ο λεκές στο μανίκι δεν έφυγε εντελώς με τον πρώτο καθαρισμό.", "Good evening, I'm calling from the 'Lefko' dry cleaner's about the coat you brought us on Tuesday. Unfortunately, the stain on the sleeve didn't come out completely with the first cleaning."),
  L("Υπάλληλος", "f", "Μπορούμε να δοκιμάσουμε ένα ειδικό προϊόν για λεκέδες από κρασί, αλλά επειδή το ύφασμα είναι μάλλινο και ευαίσθητο, υπάρχει ένας μικρός κίνδυνος να αλλάξει λίγο το χρώμα. Γι' αυτό χρειαζόμαστε πρώτα τη δική σας έγκριση.", "We can try a special product for wine stains, but because the fabric is woollen and delicate, there is a small risk that the colour may change slightly. That's why we first need your approval."),
  L("Υπάλληλος", "f", "Αν συμφωνείτε, το παλτό θα είναι έτοιμο την Πέμπτη, χωρίς επιπλέον χρέωση. Αν προτιμάτε να το παραλάβετε όπως είναι, μπορείτε να περάσετε από αύριο. Ανοίγουμε στις οχτώ.", "If you agree, the coat will be ready on Thursday, at no extra charge. If you prefer to collect it as it is, you can come by from tomorrow. We open at eight."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με το παλτό;", ["Χάθηκε", "Ο λεκές στο μανίκι δεν έφυγε εντελώς", "Σκίστηκε στον καθαρισμό", "Μίκρυνε"], 1, "ο λεκές στο μανίκι δεν έφυγε εντελώς"),
  Q("Γιατί χρειάζεται το καθαριστήριο την έγκριση του πελάτη;", ["Γιατί το ειδικό προϊόν κοστίζει ακριβά", "Γιατί υπάρχει μικρός κίνδυνος να αλλάξει λίγο το χρώμα", "Γιατί θα αργήσει μια εβδομάδα", "Γιατί πρέπει να στείλουν το παλτό αλλού"], 1, "υπάρχει ένας μικρός κίνδυνος να αλλάξει λίγο το χρώμα"),
  Q("Πόσο θα κοστίσει ο δεύτερος καθαρισμός;", ["Δέκα ευρώ", "Το μισό της πρώτης τιμής", "Τίποτα επιπλέον", "Θα το πουν την Πέμπτη"], 2, "χωρίς επιπλέον χρέωση"),
 ],
 "gloss": {"καθαριστήριο": "καθαριστήριο — dry cleaner's", "τηλεφωνητή": "τηλεφωνητής — answering machine", "παλτό": "παλτό — coat", "λεκές": "λεκές — stain", "μανίκι": "μανίκι — sleeve", "ύφασμα": "ύφασμα — fabric", "μάλλινο": "μάλλινος — woollen", "ευαίσθητο": "ευαίσθητος — delicate, sensitive", "έγκριση": "έγκριση — approval", "χρέωση": "χρέωση — charge", "να το παραλάβετε": "παραλαμβάνω — to collect, receive"},
})

ITEMS.append({
 "id": "l19-dia-sygkatoikos", "title": "Ψάχνοντας συγκάτοικο", "title_en": "Looking for a flatmate", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια φοιτήτρια που δείχνει το διαμέρισμά της σε έναν πιθανό συγκάτοικο.",
 "script": [
  L("Ιφιγένεια", "f", "Έλα, πέρασε. Αυτό είναι το δωμάτιο που μένει ελεύθερο. Είναι το μικρότερο, αλλά έχει μπαλκόνι και βλέπει στην αυλή, οπότε έχει ησυχία. Το νοίκι είναι διακόσια πενήντα ευρώ το άτομο, συν τα κοινόχρηστα.", "Come in. This is the room that's free. It's the smallest, but it has a balcony and looks onto the courtyard, so it's quiet. The rent is two hundred and fifty euros each, plus the building charges."),
  L("Στέλιος", "m", "Ωραίο είναι. Τι γίνεται με τους λογαριασμούς και τις δουλειές του σπιτιού; Στο προηγούμενο σπίτι είχαμε συνέχεια καβγάδες για τα πιάτα.", "It's nice. What about the bills and the housework? In my previous flat we were always arguing about the dishes."),
  L("Ιφιγένεια", "f", "Χα, το ξέρω αυτό. Εδώ έχουμε έναν πίνακα στην κουζίνα με τις δουλειές της εβδομάδας, και οι λογαριασμοί μοιράζονται στα δύο μέσω μιας εφαρμογής. Ένα μόνο σου ζητάω: να μην καπνίζεις μέσα στο σπίτι, γιατί έχω άσθμα.", "Ha, I know that. Here we have a board in the kitchen with the week's chores, and the bills are split in two via an app. I only ask one thing: that you don't smoke inside, because I have asthma."),
  L("Στέλιος", "m", "Δεν καπνίζω καθόλου, οπότε κανένα πρόβλημα. Θα μπορούσα να μετακομίσω στις αρχές του μήνα;", "I don't smoke at all, so no problem. Could I move in at the beginning of the month?"),
 ],
 "questions": [
  Q("Γιατί έχει ησυχία το δωμάτιο;", ["Γιατί είναι στον τελευταίο όροφο", "Γιατί βλέπει στην αυλή", "Γιατί έχει διπλά τζάμια", "Γιατί είναι το μεγαλύτερο"], 1, "βλέπει στην αυλή, οπότε έχει ησυχία"),
  Q("Πώς μοιράζονται οι λογαριασμοί;", ["Τους πληρώνει η Ιφιγένεια", "Στα δύο, μέσω μιας εφαρμογής", "Ανάλογα με το μέγεθος του δωματίου", "Τους πληρώνει ο ιδιοκτήτης"], 1, "οι λογαριασμοί μοιράζονται στα δύο μέσω μιας εφαρμογής"),
  Q("Τι ζητάει η Ιφιγένεια από τον Στέλιο;", ["Να πλένει πάντα τα πιάτα", "Να μην καπνίζει μέσα στο σπίτι", "Να πληρώσει δύο νοίκια μπροστά", "Να μη φέρνει φίλους"], 1, "να μην καπνίζεις μέσα στο σπίτι, γιατί έχω άσθμα"),
 ],
 "gloss": {"συγκάτοικο": "συγκάτοικος — flatmate", "αυλή": "αυλή — courtyard, yard", "νοίκι": "νοίκι — rent", "κοινόχρηστα": "κοινόχρηστα — shared building charges", "καβγάδες": "καβγάς — quarrel, row", "δουλειές του σπιτιού": "δουλειές του σπιτιού — housework", "μοιράζονται": "μοιράζομαι — to be shared, split", "εφαρμογής": "εφαρμογή — app", "άσθμα": "άσθμα — asthma", "να μετακομίσω": "μετακομίζω — to move (house)"},
})

ITEMS.append({
 "id": "l19-dia-taverna", "title": "Ένα τραπέζι για δώδεκα", "title_en": "A table for twelve", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε ένα τηλεφώνημα σε μια ταβέρνα για μια κράτηση.",
 "script": [
  L("Πελάτης", "m", "Καλησπέρα, θα ήθελα να κλείσω ένα τραπέζι για το Σάββατο το βράδυ, για δώδεκα άτομα. Είναι τα γενέθλια της γυναίκας μου και θέλω να της κάνω έκπληξη.", "Good evening, I'd like to book a table for Saturday evening, for twelve people. It's my wife's birthday and I want to surprise her."),
  L("Ταβερνιάρισσα", "f", "Χρόνια της πολλά! Για δώδεκα άτομα μπορώ να σας βάλω στην πίσω αυλή, κάτω από την κληματαριά, στις εννιά. Νωρίτερα δεν γίνεται, γιατί έχουμε μια βάφτιση.", "Many happy returns to her! For twelve people I can put you in the back yard, under the vine arbour, at nine. Earlier isn't possible, because we have a christening."),
  L("Πελάτης", "m", "Στις εννιά είναι μια χαρά. Μπορούμε να φέρουμε δική μας τούρτα; Και ένας φίλος είναι χορτοφάγος, υπάρχουν αρκετά πιάτα γι' αυτόν;", "Nine is fine. Can we bring our own cake? And a friend is vegetarian, are there enough dishes for him?"),
  L("Ταβερνιάρισσα", "f", "Την τούρτα φέρτε τη χωρίς πρόβλημα, θα τη βάλουμε στο ψυγείο. Για τον φίλο σας έχουμε γεμιστά, φασολάκια, μελιτζάνες στον φούρνο και φρέσκες σαλάτες. Θα χρειαστώ μόνο ένα κινητό για επιβεβαίωση την Παρασκευή.", "Bring the cake, no problem, we'll put it in the fridge. For your friend we have stuffed vegetables, green beans, baked aubergines and fresh salads. I'll just need a mobile number for confirmation on Friday."),
 ],
 "questions": [
  Q("Γιατί δεν μπορούν να έρθουν νωρίτερα από τις εννιά;", ["Γιατί η ταβέρνα ανοίγει στις εννιά", "Γιατί η ταβέρνα έχει μια βάφτιση", "Γιατί η γυναίκα του δουλεύει ως αργά", "Γιατί η αυλή είναι κλειστή"], 1, "Νωρίτερα δεν γίνεται, γιατί έχουμε μια βάφτιση"),
  Q("Τι θα γίνει με την τούρτα;", ["Θα την ετοιμάσει η ταβέρνα", "Δεν επιτρέπεται", "Θα τη βάλουν στο ψυγείο της ταβέρνας", "Θα την παραγγείλουν από ζαχαροπλαστείο"], 2, "θα τη βάλουμε στο ψυγείο"),
  Q("Τι θα χρειαστεί η ταβερνιάρισσα;", ["Μια προκαταβολή", "Ένα κινητό για επιβεβαίωση την Παρασκευή", "Τον ακριβή αριθμό των χορτοφάγων", "Το μενού από πριν"], 1, "Θα χρειαστώ μόνο ένα κινητό για επιβεβαίωση την Παρασκευή"),
 ],
 "gloss": {"κράτηση": "κράτηση — reservation", "να κλείσω": "κλείνω (τραπέζι) — to book (a table)", "έκπληξη": "έκπληξη — surprise", "Χρόνια της πολλά": "χρόνια πολλά — many happy returns", "κληματαριά": "κληματαριά — vine arbour, pergola", "βάφτιση": "βάφτιση — christening", "τούρτα": "τούρτα — (layer) cake", "χορτοφάγος": "χορτοφάγος — vegetarian", "γεμιστά": "γεμιστά — stuffed vegetables", "επιβεβαίωση": "επιβεβαίωση — confirmation"},
})

ITEMS.append({
 "id": "l19-mon-skylos", "title": "Υιοθέτησα έναν σκύλο", "title_en": "I adopted a dog", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλά σε ένα ραδιοφωνικό πρόγραμμα για το πώς υιοθέτησε έναν σκύλο.",
 "script": [
  L("Ορέστης", "m", "Δεν ήμουν ποτέ άνθρωπος των ζώων. Πέρσι όμως, μετά τη σύνταξη, το σπίτι μού φαινόταν άδειο. Η κόρη μου με πήγε σχεδόν με το ζόρι σε ένα καταφύγιο αδέσποτων στα περίχωρα της πόλης.", "I was never an animal person. But last year, after retiring, the house felt empty to me. My daughter took me, almost by force, to a shelter for strays on the outskirts of the city."),
  L("Ορέστης", "m", "Εκεί ήταν ο Μπόμπος, ένα μεγάλο, γέρικο σκυλί με ένα αυτί κομμένο. Όλοι οι επισκέπτες προτιμούσαν τα κουτάβια, κι εκείνος καθόταν σε μια γωνία και κοίταζε. Οι εθελοντές μού είπαν ότι ήταν στο καταφύγιο τρία χρόνια.", "There was Bobos, a big, old dog with a torn ear. All the visitors preferred the puppies, and he sat in a corner watching. The volunteers told me he had been at the shelter for three years."),
  L("Ορέστης", "m", "Τον πήρα για μια δοκιμαστική εβδομάδα και δεν τον έδωσα ποτέ πίσω. Τώρα περπατάμε δύο φορές την ημέρα, γνώρισα όλους τους γείτονες και ο γιατρός λέει ότι η πίεσή μου έπεσε. Νόμιζα ότι εγώ θα έσωζα εκείνον· στην πραγματικότητα, με έσωσε αυτός.", "I took him for a trial week and never gave him back. Now we walk twice a day, I've met all the neighbours and the doctor says my blood pressure has dropped. I thought I would save him; in fact, he saved me."),
 ],
 "questions": [
  Q("Γιατί πήγε ο Ορέστης στο καταφύγιο;", ["Γιατί ήθελε πάντα σκύλο", "Γιατί τον πήγε η κόρη του, όταν το σπίτι τού φαινόταν άδειο", "Γιατί έγινε εθελοντής", "Γιατί βρήκε ένα αδέσποτο στον δρόμο"], 1, "Η κόρη μου με πήγε σχεδόν με το ζόρι σε ένα καταφύγιο"),
  Q("Γιατί δεν είχε υιοθετηθεί ο Μπόμπος;", ["Γιατί ήταν επιθετικός", "Γιατί ήταν άρρωστος", "Γιατί οι επισκέπτες προτιμούσαν τα κουτάβια", "Γιατί είχε έρθει πρόσφατα"], 2, "Όλοι οι επισκέπτες προτιμούσαν τα κουτάβια"),
  Q("Τι εννοεί ο Ορέστης με τη φράση «με έσωσε αυτός»;", ["Ότι ο σκύλος τον προστάτεψε από κλέφτη", "Ότι ο σκύλος βελτίωσε την υγεία και την κοινωνική του ζωή", "Ότι ο σκύλος τον βρήκε όταν χάθηκε", "Ότι ο σκύλος έφυγε από το σπίτι"], 1, "γνώρισα όλους τους γείτονες και ο γιατρός λέει ότι η πίεσή μου έπεσε"),
 ],
 "gloss": {"υιοθέτησε": "υιοθετώ — to adopt", "σύνταξη": "σύνταξη — retirement, pension", "με το ζόρι": "με το ζόρι — by force, reluctantly", "καταφύγιο": "καταφύγιο — shelter", "αδέσποτων": "αδέσποτος — stray", "περίχωρα": "περίχωρα — outskirts", "γέρικο": "γέρικος — old (of animals)", "κουτάβια": "κουτάβι — puppy", "εθελοντές": "εθελοντής — volunteer", "δοκιμαστική": "δοκιμαστικός — trial", "πίεσή": "πίεση — blood pressure"},
})

ITEMS.append({
 "id": "l19-rep-kerkini", "title": "Η λίμνη Κερκίνη", "title_en": "Lake Kerkini", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από τη λίμνη Κερκίνη, στον νομό Σερρών.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρισκόμαστε στις όχθες της λίμνης Κερκίνης, κοντά στα σύνορα με τη Βουλγαρία και τη Βόρεια Μακεδονία. Λίγοι ξέρουν ότι η λίμνη είναι τεχνητή: δημιουργήθηκε τη δεκαετία του 1930, με ένα φράγμα στον ποταμό Στρυμόνα, για να ελεγχθούν οι πλημμύρες και να ποτίζονται τα χωράφια του κάμπου.", "We're on the shores of Lake Kerkini, near the borders with Bulgaria and North Macedonia. Few people know the lake is artificial: it was created in the 1930s, with a dam on the river Strymonas, to control floods and irrigate the fields of the plain."),
  L("Ρεπόρτερ", "f", "Σήμερα είναι ένας από τους σημαντικότερους υγροτόπους της Ευρώπης. Εδώ ζουν ή περνούν εκατοντάδες είδη πουλιών, ανάμεσά τους αργυροπελεκάνοι, κορμοράνοι και ερωδιοί, που φωλιάζουν στα δέντρα του νερού. Φωτογράφοι από όλο τον κόσμο έρχονται κάθε χειμώνα για να τους απαθανατίσουν.", "Today it is one of the most important wetlands in Europe. Hundreds of bird species live here or pass through, among them Dalmatian pelicans, cormorants and herons, which nest in the trees in the water. Photographers from all over the world come every winter to capture them."),
  L("Ρεπόρτερ", "f", "Χαρακτηριστικό της περιοχής είναι και τα βουβάλια, που βόσκουν ελεύθερα στα ρηχά νερά. Οι ντόπιοι κτηνοτρόφοι παράγουν από το γάλα τους γιαούρτι και τυριά, ενώ μικρά βαρκάκια πηγαίνουν τους επισκέπτες κοντά στις αποικίες των πουλιών, χωρίς να τα ενοχλούν.", "Another feature of the area is the water buffaloes, which graze freely in the shallow water. Local livestock farmers make yoghurt and cheeses from their milk, while small boats take visitors close to the bird colonies without disturbing them."),
 ],
 "questions": [
  Q("Γιατί δημιουργήθηκε η λίμνη;", ["Για να γίνει τουριστικός προορισμός", "Για τον έλεγχο των πλημμυρών και το πότισμα των χωραφιών", "Για την παραγωγή ηλεκτρικού ρεύματος", "Για την προστασία των πουλιών"], 1, "για να ελεγχθούν οι πλημμύρες και να ποτίζονται τα χωράφια του κάμπου"),
  Q("Γιατί έρχονται φωτογράφοι κάθε χειμώνα;", ["Για τα χιονισμένα βουνά", "Για τα πουλιά της λίμνης", "Για τα παραδοσιακά χωριά", "Για έναν διαγωνισμό"], 1, "Φωτογράφοι από όλο τον κόσμο έρχονται κάθε χειμώνα για να τους απαθανατίσουν"),
  Q("Τι κάνουν οι ντόπιοι κτηνοτρόφοι;", ["Ψαρεύουν στη λίμνη", "Παράγουν γιαούρτι και τυριά από το γάλα των βουβαλιών", "Φτιάχνουν βάρκες", "Καλλιεργούν ρύζι"], 1, "Οι ντόπιοι κτηνοτρόφοι παράγουν από το γάλα τους γιαούρτι και τυριά"),
 ],
 "gloss": {"όχθες": "όχθη — shore, bank", "τεχνητή": "τεχνητός — artificial", "φράγμα": "φράγμα — dam", "πλημμύρες": "πλημμύρα — flood", "κάμπου": "κάμπος — plain", "υγροτόπους": "υγρότοπος — wetland", "αργυροπελεκάνοι": "αργυροπελεκάνος — Dalmatian pelican", "κορμοράνοι": "κορμοράνος — cormorant", "ερωδιοί": "ερωδιός — heron", "φωλιάζουν": "φωλιάζω — to nest", "να τους απαθανατίσουν": "απαθανατίζω — to capture (on film), immortalise", "βουβάλια": "βουβάλι — water buffalo", "ρηχά": "ρηχός — shallow", "κτηνοτρόφοι": "κτηνοτρόφος — livestock farmer", "αποικίες": "αποικία — colony"},
})

ITEMS.append({
 "id": "l19-rep-feta", "title": "Η φέτα και η προστασία της", "title_en": "Feta and its protection", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από ένα τυροκομείο στην Ήπειρο.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο μικρό τυροκομείο της οικογένειας Ζήση, το γάλα φτάνει κάθε πρωί από τα γύρω βουνά. Για να ονομαστεί ένα τυρί «φέτα», πρέπει να φτιαχτεί από πρόβειο γάλα ή από μείγμα πρόβειου και κατσικίσιου, με το κατσικίσιο να μην ξεπερνά το τριάντα τοις εκατό.", "At the Zisis family's small cheese dairy, the milk arrives every morning from the surrounding mountains. For a cheese to be called 'feta', it must be made from sheep's milk or a mix of sheep's and goat's milk, with the goat's milk not exceeding thirty per cent."),
  L("Ρεπόρτερ", "m", "Από το 2002 η φέτα είναι προϊόν προστατευόμενης ονομασίας προέλευσης στην Ευρωπαϊκή Ένωση. Αυτό σημαίνει ότι μόνο τυριά που παράγονται σε συγκεκριμένες περιοχές της Ελλάδας, με την παραδοσιακή μέθοδο, μπορούν να φέρουν αυτό το όνομα. Η απόφαση ήρθε μετά από πολύχρονες δικαστικές διαμάχες με άλλες χώρες.", "Since 2002 feta has been a product with a protected designation of origin in the European Union. This means that only cheeses produced in specific regions of Greece, using the traditional method, may bear the name. The decision came after years of legal disputes with other countries."),
  L("Τυροκόμος", "f", "Το μυστικό είναι η άλμη και ο χρόνος. Η φέτα ωριμάζει τουλάχιστον δύο μήνες. Και το γάλα από ζώα που βόσκουν ελεύθερα σε βουνά με αγριολούλουδα δίνει μια γεύση που δεν αντιγράφεται.", "The secret is the brine and time. Feta matures for at least two months. And milk from animals grazing freely on mountains full of wild flowers gives a flavour that can't be copied."),
 ],
 "questions": [
  Q("Από τι γάλα πρέπει να φτιάχνεται η φέτα;", ["Μόνο από κατσικίσιο", "Από αγελαδινό και πρόβειο", "Από πρόβειο ή μείγμα με έως τριάντα τοις εκατό κατσικίσιο", "Από οποιοδήποτε γάλα"], 2, "πρέπει να φτιαχτεί από πρόβειο γάλα ή από μείγμα πρόβειου και κατσικίσιου"),
  Q("Τι σημαίνει η προστατευόμενη ονομασία προέλευσης;", ["Ότι η φέτα δεν εξάγεται", "Ότι μόνο τυριά από συγκεκριμένες περιοχές της Ελλάδας με την παραδοσιακή μέθοδο λέγονται φέτα", "Ότι η τιμή της είναι σταθερή", "Ότι κάθε ευρωπαϊκή χώρα μπορεί να τη φτιάχνει"], 1, "μόνο τυριά που παράγονται σε συγκεκριμένες περιοχές της Ελλάδας, με την παραδοσιακή μέθοδο, μπορούν να φέρουν αυτό το όνομα"),
  Q("Πόσο ωριμάζει τουλάχιστον η φέτα;", ["Δύο εβδομάδες", "Δύο μήνες", "Έξι μήνες", "Έναν χρόνο"], 1, "Η φέτα ωριμάζει τουλάχιστον δύο μήνες"),
 ],
 "gloss": {"τυροκομείο": "τυροκομείο — cheese dairy", "πρόβειο": "πρόβειος — sheep's", "μείγμα": "μείγμα — mixture", "κατσικίσιο": "κατσικίσιος — goat's", "προστατευόμενης ονομασίας προέλευσης": "προστατευόμενη ονομασία προέλευσης — protected designation of origin (PDO)", "να φέρουν": "φέρω — to bear (a name, a label)", "δικαστικές": "δικαστικός — legal, judicial", "διαμάχες": "διαμάχη — dispute", "άλμη": "άλμη — brine", "ωριμάζει": "ωριμάζω — to mature, ripen", "αγριολούλουδα": "αγριολούλουδο — wild flower"},
})

ITEMS.append({
 "id": "l19-int-astronomos", "title": "Η αστρονόμος του Χελμού", "title_en": "The astronomer of Mount Helmos", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια αστρονόμο που δουλεύει στο αστεροσκοπείο του Χελμού, κοντά στα Καλάβρυτα.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς είναι μια μέρα, ή μάλλον μια νύχτα, στο αστεροσκοπείο;", "What is a day, or rather a night, like at the observatory?"),
  L("Αστρονόμος", "f", "Ανεβαίνουμε το απόγευμα, σε υψόμετρο πάνω από δύο χιλιάδες τριακόσια μέτρα, και ελέγχουμε τον καιρό. Αν ο ουρανός είναι καθαρός, δουλεύουμε όλη τη νύχτα με το τηλεσκόπιο «Αρίσταρχος», που είναι από τα μεγαλύτερα στην Ευρώπη. Τον χειμώνα, με το χιόνι, μένουμε εκεί πάνω για αρκετές μέρες.", "We go up in the afternoon, to an altitude of over two thousand three hundred metres, and check the weather. If the sky is clear, we work all night with the 'Aristarchos' telescope, which is one of the largest in Europe. In winter, with the snow, we stay up there for several days."),
  L("Δημοσιογράφος", "m", "Τι σας ανησυχεί περισσότερο σήμερα;", "What worries you most today?"),
  L("Αστρονόμος", "f", "Η φωτορρύπανση. Τα φώτα των πόλεων και των δρόμων φτάνουν όλο και πιο μακριά, και ο σκοτεινός ουρανός γίνεται σπάνιος. Τα περισσότερα παιδιά στις πόλεις δεν έχουν δει ποτέ τον Γαλαξία. Και δεν χρειάζονται δαπανηρές λύσεις: φωτιστικά που φωτίζουν προς τα κάτω και όχι προς τον ουρανό κάνουν τεράστια διαφορά.", "Light pollution. The lights of towns and roads reach further and further, and a dark sky is becoming rare. Most children in cities have never seen the Milky Way. And costly solutions aren't needed: lamps that shine downwards and not towards the sky make a huge difference."),
 ],
 "questions": [
  Q("Τι κάνουν οι αστρονόμοι όταν ο ουρανός είναι καθαρός;", ["Γυρίζουν στο σπίτι τους", "Δουλεύουν όλη τη νύχτα με το τηλεσκόπιο", "Κάνουν ξεναγήσεις", "Επισκευάζουν το τηλεσκόπιο"], 1, "Αν ο ουρανός είναι καθαρός, δουλεύουμε όλη τη νύχτα με το τηλεσκόπιο"),
  Q("Τι ανησυχεί περισσότερο την αστρονόμο;", ["Το κρύο", "Η φωτορρύπανση", "Η έλλειψη χρημάτων", "Ο αριθμός των επισκεπτών"], 1, "Η φωτορρύπανση"),
  Q("Ποια λύση προτείνει;", ["Να σβήνουν όλα τα φώτα τη νύχτα", "Φωτιστικά που φωτίζουν προς τα κάτω", "Να χτιστούν περισσότερα αστεροσκοπεία", "Να μένουν τα παιδιά μακριά από τις πόλεις"], 1, "φωτιστικά που φωτίζουν προς τα κάτω και όχι προς τον ουρανό κάνουν τεράστια διαφορά"),
 ],
 "gloss": {"αστρονόμο": "αστρονόμος — astronomer", "αστεροσκοπείο": "αστεροσκοπείο — observatory", "υψόμετρο": "υψόμετρο — altitude", "τηλεσκόπιο": "τηλεσκόπιο — telescope", "φωτορρύπανση": "φωτορρύπανση — light pollution", "σκοτεινός": "σκοτεινός — dark", "σπάνιος": "σπάνιος — rare", "Γαλαξία": "Γαλαξίας — the Milky Way", "δαπανηρές": "δαπανηρός — costly", "φωτιστικά": "φωτιστικό — light fitting, lamp"},
})

ITEMS.append({
 "id": "l19-mon-chatzidakis", "title": "Ο Χατζιδάκις και το ρεμπέτικο", "title_en": "Hadjidakis and rebetiko", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια μουσικολόγο να μιλά σε μια εκδήλωση για τη διάλεξη του Μάνου Χατζιδάκι για το ρεμπέτικο.",
 "script": [
  L("Μουσικολόγος", "f", "Τον Ιανουάριο του 1949 ένας νεαρός συνθέτης, ο Μάνος Χατζιδάκις, έδωσε μια διάλεξη στο Θέατρο Τέχνης του Κάρολου Κουν που προκάλεσε αναστάτωση. Υποστήριξε ότι το ρεμπέτικο, που οι μορφωμένοι αστοί θεωρούσαν μουσική των τεκέδων και του υποκόσμου, ήταν στην πραγματικότητα γνήσια λαϊκή τέχνη.", "In January 1949 a young composer, Manos Hadjidakis, gave a lecture at Karolos Koun's Art Theatre that caused a stir. He argued that rebetiko, which the educated middle class considered the music of hashish dens and the underworld, was in fact genuine popular art."),
  L("Μουσικολόγος", "f", "Για τον Χατζιδάκι, τα τραγούδια του Βασίλη Τσιτσάνη και άλλων συνέχιζαν, με νέα μορφή, τη μακριά παράδοση του δημοτικού τραγουδιού και της βυζαντινής μουσικής. Μιλούσε για τη λιτότητα, για τη σεμνότητα της έκφρασης, για ένα πάθος που δεν γίνεται ποτέ μελόδραμα.", "For Hadjidakis, the songs of Vassilis Tsitsanis and others continued, in a new form, the long tradition of folk song and Byzantine music. He spoke of their austerity, the restraint of their expression, a passion that never turns into melodrama."),
  L("Μουσικολόγος", "f", "Η διάλεξη δεν άλλαξε από τη μια μέρα στην άλλη τη στάση του κοινού. Άνοιξε όμως έναν δρόμο. Λίγα χρόνια αργότερα, ο ίδιος ο Χατζιδάκις, και στη συνέχεια ο Θεοδωράκης, χρησιμοποίησαν το μπουζούκι και τους ρυθμούς του ρεμπέτικου σε έργα που απευθύνονταν σε όλη την κοινωνία.", "The lecture didn't change the public's attitude overnight. But it opened a path. A few years later, Hadjidakis himself, and then Theodorakis, used the bouzouki and the rhythms of rebetiko in works addressed to the whole of society."),
  L("Μουσικολόγος", "f", "Αυτό που με εντυπωσιάζει είναι το θάρρος της χειρονομίας. Ένας νέος από την καλή κοινωνία στάθηκε μπροστά σε ένα αστικό ακροατήριο και του είπε, ουσιαστικά, ότι η τέχνη που περιφρονούσε ήταν δική του.", "What impresses me is the courage of the gesture. A young man from good society stood before a middle-class audience and told it, in essence, that the art it despised was its own."),
 ],
 "questions": [
  Q("Πώς έβλεπαν οι μορφωμένοι αστοί το ρεμπέτικο πριν από τη διάλεξη;", ["Ως γνήσια λαϊκή τέχνη", "Ως μουσική των τεκέδων και του υποκόσμου", "Ως εξέλιξη της βυζαντινής μουσικής", "Ως ξένη μουσική"], 1, "οι μορφωμένοι αστοί θεωρούσαν μουσική των τεκέδων και του υποκόσμου"),
  Q("Με ποια παράδοση συνέδεε ο Χατζιδάκις το ρεμπέτικο;", ["Με την ευρωπαϊκή όπερα", "Με το δημοτικό τραγούδι και τη βυζαντινή μουσική", "Με την αμερικανική τζαζ", "Με την αρχαία τραγωδία"], 1, "συνέχιζαν, με νέα μορφή, τη μακριά παράδοση του δημοτικού τραγουδιού και της βυζαντινής μουσικής"),
  Q("Ποια ήταν, κατά τη μουσικολόγο, η συνέπεια της διάλεξης;", ["Άλλαξε αμέσως τη στάση του κοινού", "Δεν είχε καμία συνέπεια", "Άνοιξε έναν δρόμο που ακολούθησαν αργότερα συνθέτες", "Απαγορεύτηκε το ρεμπέτικο"], 2, "Η διάλεξη δεν άλλαξε από τη μια μέρα στην άλλη τη στάση του κοινού. Άνοιξε όμως έναν δρόμο"),
  Q("Τι θαυμάζει περισσότερο η μουσικολόγος;", ["Το θάρρος της χειρονομίας του Χατζιδάκι", "Τη φωνή του Τσιτσάνη", "Την ακρίβεια της ανάλυσης", "Την επιτυχία των ταινιών"], 0, "Αυτό που με εντυπωσιάζει είναι το θάρρος της χειρονομίας"),
 ],
 "gloss": {"μουσικολόγο": "μουσικολόγος — musicologist", "διάλεξη": "διάλεξη — lecture", "συνθέτης": "συνθέτης — composer", "αναστάτωση": "αναστάτωση — stir, commotion", "μορφωμένοι": "μορφωμένος — educated", "αστοί": "αστός — member of the middle class, bourgeois", "τεκέδων": "τεκές — hashish den", "υποκόσμου": "υπόκοσμος — underworld", "γνήσια": "γνήσιος — genuine", "λιτότητα": "λιτότητα — austerity, simplicity", "σεμνότητα": "σεμνότητα — modesty, restraint", "μελόδραμα": "μελόδραμα — melodrama", "χειρονομίας": "χειρονομία — gesture", "ακροατήριο": "ακροατήριο — audience", "περιφρονούσε": "περιφρονώ — to despise, look down on"},
})

ITEMS.append({
 "id": "l19-int-archaia", "title": "Αρχαία ελληνικά στο σχολείο;", "title_en": "Ancient Greek at school?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συζήτηση με μια φιλόλογο για τη διδασκαλία των αρχαίων ελληνικών στο σχολείο.",
 "script": [
  L("Δημοσιογράφος", "m", "Κάθε τόσο ανοίγει η ίδια συζήτηση: χρειάζονται τα αρχαία ελληνικά στο σημερινό σχολείο ή είναι ένα βάρος για τους μαθητές;", "Every so often the same debate opens: is Ancient Greek needed in today's school, or is it a burden on pupils?"),
  L("Φιλόλογος", "f", "Το ερώτημα, κατά τη γνώμη μου, είναι λάθος διατυπωμένο. Το πρόβλημα δεν είναι αν διδάσκονται τα αρχαία, αλλά πώς. Όταν το μάθημα περιορίζεται στην αποστήθιση κανόνων γραμματικής και σε μεταφράσεις χωρίς νόημα, είναι φυσικό οι μαθητές να το μισούν.", "The question, in my view, is wrongly put. The problem isn't whether Ancient Greek is taught, but how. When the lesson is limited to memorising grammar rules and meaningless translations, it's natural for pupils to hate it."),
  L("Δημοσιογράφος", "m", "Και τι προτείνετε;", "And what do you propose?"),
  L("Φιλόλογος", "f", "Να διαβάζουμε τα κείμενα για αυτό που λένε. Ο Θουκυδίδης για τον πόλεμο και την εξουσία, ο Σοφοκλής για τη σύγκρουση νόμου και συνείδησης, είναι πιο επίκαιροι από πολλά σημερινά άρθρα. Η γλώσσα έρχεται μετά, σχεδόν φυσικά, όταν υπάρχει ενδιαφέρον.", "Read the texts for what they say. Thucydides on war and power, Sophocles on the clash between law and conscience, are more topical than many of today's articles. The language comes afterwards, almost naturally, when there is interest."),
  L("Φιλόλογος", "f", "Υπάρχει και κάτι ακόμα: η γνώση των αρχαίων βοηθά να καταλαβαίνουμε πώς φτιάχνονται οι λέξεις της νέας ελληνικής. Δεν είναι όμως απαραίτητη για να τη μιλάς σωστά. Το να πούμε στα παιδιά ότι χωρίς αρχαία δεν θα μάθουν ποτέ καλά ελληνικά είναι υπερβολή που κάνει περισσότερο κακό παρά καλό.", "There's something else too: knowing Ancient Greek helps us understand how the words of Modern Greek are formed. But it isn't necessary in order to speak it correctly. Telling children that without Ancient Greek they will never learn good Greek is an exaggeration that does more harm than good."),
 ],
 "questions": [
  Q("Ποια είναι η βασική θέση της φιλολόγου;", ["Ότι τα αρχαία πρέπει να καταργηθούν", "Ότι το πρόβλημα είναι ο τρόπος διδασκαλίας και όχι το ίδιο το μάθημα", "Ότι οι μαθητές πρέπει να μαθαίνουν περισσότερη γραμματική", "Ότι τα αρχαία πρέπει να διδάσκονται μόνο στο πανεπιστήμιο"], 1, "Το πρόβλημα δεν είναι αν διδάσκονται τα αρχαία, αλλά πώς"),
  Q("Τι προτείνει για τη διδασκαλία;", ["Περισσότερες ώρες αποστήθισης", "Να διαβάζονται τα κείμενα για το περιεχόμενό τους", "Να διδάσκονται μόνο σε μετάφραση", "Να διαβάζονται μόνο σημερινά άρθρα"], 1, "Να διαβάζουμε τα κείμενα για αυτό που λένε"),
  Q("Γιατί αναφέρει τον Θουκυδίδη και τον Σοφοκλή;", ["Γιατί η γλώσσα τους είναι εύκολη", "Γιατί είναι επίκαιροι για ζητήματα όπως ο πόλεμος και η συνείδηση", "Γιατί είναι οι αγαπημένοι των μαθητών", "Γιατί εξετάζονται στις Πανελλήνιες"], 1, "είναι πιο επίκαιροι από πολλά σημερινά άρθρα"),
  Q("Ποια άποψη χαρακτηρίζει «υπερβολή»;", ["Ότι τα αρχαία βοηθούν στην κατανόηση των λέξεων", "Ότι χωρίς αρχαία δεν μαθαίνει κανείς καλά ελληνικά", "Ότι ο Σοφοκλής είναι επίκαιρος", "Ότι οι μαθητές μισούν τη γραμματική"], 1, "Το να πούμε στα παιδιά ότι χωρίς αρχαία δεν θα μάθουν ποτέ καλά ελληνικά είναι υπερβολή"),
 ],
 "gloss": {"φιλόλογο": "φιλόλογος — philologist, teacher of Greek language and literature", "Κάθε τόσο": "κάθε τόσο — every so often", "βάρος": "βάρος — burden", "διατυπωμένο": "διατυπώνω — to formulate, put (a question)", "αποστήθιση": "αποστήθιση — memorising, learning by heart", "εξουσία": "εξουσία — power", "σύγκρουση": "σύγκρουση — clash, conflict", "συνείδησης": "συνείδηση — conscience", "επίκαιροι": "επίκαιρος — topical", "απαραίτητη": "απαραίτητος — necessary", "υπερβολή": "υπερβολή — exaggeration"},
})

rnd = random.Random(19)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-19.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
