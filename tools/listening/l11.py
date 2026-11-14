# Source for library/listening/listening-11.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l11.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l11-ann-panepistimio", "title": "Δηλώσεις μαθημάτων", "title_en": "Signing up for courses", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ηχογραφημένη ανακοίνωση της γραμματείας ενός πανεπιστημιακού τμήματος.",
 "script": [
  L("Γραμματέας", "f", "Η γραμματεία του Τμήματος Ιστορίας ενημερώνει τους φοιτητές ότι οι δηλώσεις μαθημάτων για το εαρινό εξάμηνο θα γίνονται ηλεκτρονικά, από τη Δευτέρα πέντε έως την Παρασκευή εννιά Φεβρουαρίου. Μετά τη λήξη της προθεσμίας δεν θα γίνονται δεκτές αλλαγές.", "The secretariat of the History Department informs students that course registrations for the spring semester will be made online, from Monday the fifth to Friday the ninth of February. After the deadline no changes will be accepted."),
  L("Γραμματέας", "f", "Υπενθυμίζεται ότι οι φοιτητές μπορούν να δηλώσουν έως οκτώ μαθήματα, από τα οποία τουλάχιστον δύο πρέπει να είναι μαθήματα επιλογής. Όσοι χρωστούν μαθήματα από προηγούμενα έτη πρέπει να τα δηλώσουν ξανά, αλλιώς δεν θα έχουν δικαίωμα συμμετοχής στις εξετάσεις.", "Students are reminded that they may register for up to eight courses, at least two of which must be electives. Those who owe courses from previous years must register for them again, otherwise they will not be entitled to sit the exams."),
  L("Γραμματέας", "f", "Λόγω του μεγάλου αριθμού αιτημάτων, η γραμματεία δεν θα εξυπηρετεί τηλεφωνικά κατά την περίοδο των δηλώσεων. Για οποιοδήποτε πρόβλημα, οι φοιτητές μπορούν να στέλνουν email, αναφέροντας τον αριθμό μητρώου τους.", "Because of the large number of requests, the secretariat will not answer the phone during the registration period. For any problem, students can send an email, giving their student registration number."),
 ],
 "questions": [
  Q("Τι ισχύει μετά την Παρασκευή εννιά Φεβρουαρίου;", ["Οι δηλώσεις γίνονται μόνο στη γραμματεία", "Δεν επιτρέπονται πια αλλαγές", "Αρχίζουν οι εξετάσεις", "Ανοίγουν οι δηλώσεις για τα μαθήματα επιλογής"], 1, "Μετά τη λήξη της προθεσμίας δεν θα γίνονται δεκτές αλλαγές."),
  Q("Τι πρέπει να κάνουν όσοι χρωστούν μαθήματα;", ["Να πληρώσουν παράβολο", "Να τα δηλώσουν ξανά για να μπορούν να εξεταστούν", "Να στείλουν email στον καθηγητή", "Τίποτα, δηλώνονται αυτόματα"], 1, "πρέπει να τα δηλώσουν ξανά, αλλιώς δεν θα έχουν δικαίωμα συμμετοχής στις εξετάσεις"),
  Q("Πώς μπορούν οι φοιτητές να επικοινωνήσουν με τη γραμματεία αυτές τις μέρες;", ["Μόνο τηλεφωνικά", "Μόνο με email, γράφοντας τον αριθμό μητρώου", "Μόνο αυτοπροσώπως", "Μέσω των καθηγητών τους"], 1, "οι φοιτητές μπορούν να στέλνουν email, αναφέροντας τον αριθμό μητρώου τους"),
 ],
 "gloss": {"γραμματεία": "γραμματεία — secretariat, (department) office", "δηλώσεις μαθημάτων": "δήλωση μαθημάτων — course registration", "εαρινό εξάμηνο": "εαρινό εξάμηνο — spring semester", "προθεσμίας": "προθεσμία — deadline", "γίνονται δεκτές": "γίνομαι δεκτός — to be accepted", "μαθήματα επιλογής": "μάθημα επιλογής — elective course", "χρωστούν": "χρωστάω — to owe; χρωστάω μάθημα — to have an exam still to pass", "δικαίωμα": "δικαίωμα — right, entitlement", "αριθμό μητρώου": "αριθμός μητρώου — (student) registration number"},
})

ITEMS.append({
 "id": "l11-vm-ktiniatreio", "title": "Υπενθύμιση από το κτηνιατρείο", "title_en": "A reminder from the vet", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από ένα κτηνιατρείο προς την κυρία Σταυρίδου.",
 "script": [
  L("Βοηθός", "m", "Καλησπέρα, κυρία Σταυρίδου, από το κτηνιατρείο σας παίρνουμε. Σας υπενθυμίζουμε ότι πλησιάζει η ετήσια επανάληψη του εμβολίου της γάτας σας, της Μέλισσας. Έχει ήδη περάσει ένας χρόνος από την τελευταία φορά, τον Νοέμβριο.", "Good evening, Mrs Stavridou, we're calling from the vet's. We'd like to remind you that your cat Melissa's annual booster vaccination is coming up. A year has already passed since last time, in November."),
  L("Βοηθός", "m", "Η γιατρός θα ήθελε, με την ευκαιρία, να της κάνει και μια γενική εξέταση, αφού την τελευταία φορά είχε πάρει λίγο βάρος. Φέρτε τη νηστική, χωρίς φαγητό από το προηγούμενο βράδυ, γιατί μπορεί να χρειαστεί και εξέταση αίματος.", "The doctor would also like, while she's here, to give her a general check-up, since last time she had put on a little weight. Please bring her without food from the night before, because a blood test may also be needed."),
  L("Βοηθός", "m", "Έχουμε διαθέσιμα ραντεβού την Τετάρτη το πρωί και την Πέμπτη το απόγευμα. Πάρτε μας όποτε σας βολεύει για να κανονίσουμε. Και μην ξεχάσετε το βιβλιάριο υγείας της!", "We have appointments available on Wednesday morning and Thursday afternoon. Call us whenever suits you to arrange it. And don't forget her health booklet!"),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί ο βοηθός;", ["Για να ανακοινώσει αποτελέσματα εξετάσεων", "Για να υπενθυμίσει το ετήσιο εμβόλιο της γάτας", "Γιατί η γάτα χάθηκε", "Για να ακυρώσει ένα ραντεβού"], 1, "πλησιάζει η ετήσια επανάληψη του εμβολίου της γάτας σας"),
  Q("Γιατί πρέπει η γάτα να έρθει νηστική;", ["Γιατί θα κάνει εγχείρηση", "Γιατί είναι πολύ παχιά", "Γιατί ίσως χρειαστεί εξέταση αίματος", "Γιατί το εμβόλιο το απαιτεί"], 2, "μπορεί να χρειαστεί και εξέταση αίματος"),
  Q("Τι ζητάει να φέρει η κυρία Σταυρίδου;", ["Το βιβλιάριο υγείας της γάτας", "Ένα δείγμα τροφής", "Τα αποτελέσματα των παλιών εξετάσεων", "Χρήματα σε μετρητά"], 0, "μην ξεχάσετε το βιβλιάριο υγείας της"),
 ],
 "gloss": {"κτηνιατρείο": "κτηνιατρείο — vet's practice", "επανάληψη": "επανάληψη — repeat; (here) booster", "εμβολίου": "εμβόλιο — vaccine", "με την ευκαιρία": "με την ευκαιρία — while we're at it", "γενική εξέταση": "γενική εξέταση — general check-up", "είχε πάρει λίγο βάρος": "παίρνω βάρος — to put on weight", "νηστική": "νηστικός — without having eaten, fasting", "εξέταση αίματος": "εξέταση αίματος — blood test", "όποτε σας βολεύει": "όποτε σας βολεύει — whenever suits you", "βιβλιάριο υγείας": "βιβλιάριο υγείας — health booklet"},
})

ITEMS.append({
 "id": "l11-dia-xenodoxeio", "title": "Αλλαγή κράτησης", "title_en": "Changing a hotel booking", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε ένα τηλεφώνημα ανάμεσα σε έναν πελάτη και τη ρεσεψιόν ενός ξενοδοχείου στη Ζαγορά Πηλίου.",
 "script": [
  L("Υπάλληλος", "f", "Ξενοδοχείο «Ο Πλάτανος», καλημέρα σας.", "Hotel 'The Plane Tree', good morning."),
  L("Πελάτης", "m", "Καλημέρα. Έχω κάνει κράτηση για τρεις νύχτες, από την Παρασκευή, στο όνομα Αλεξανδρόπουλος. Δυστυχώς, δεν μπορούμε να έρθουμε πριν από το Σάββατο, γιατί η γυναίκα μου έχει μια υποχρέωση στη δουλειά. Γίνεται να μετακινήσουμε την κράτηση κατά μία μέρα;", "Good morning. I've booked three nights from Friday, under the name Alexandropoulos. Unfortunately we can't come before Saturday, because my wife has a work commitment. Is it possible to move the booking by one day?"),
  L("Υπάλληλος", "f", "Να δω… Για το Σάββατο και την Κυριακή έχουμε το δωμάτιό σας, αλλά τη Δευτέρα είμαστε πλήρεις, γιατί έχουμε μια ομάδα από έναν σύλλογο. Μπορώ να σας δώσω για τη Δευτέρα ένα άλλο δωμάτιο, λίγο μικρότερο, χωρίς θέα στη θάλασσα.", "Let me see… For Saturday and Sunday we have your room, but on Monday we're full, because we have a group from an association. I can give you another room for Monday, a bit smaller, without a sea view."),
  L("Πελάτης", "m", "Δεν πειράζει, για μία νύχτα. Θα υπάρξει κάποια χρέωση για την αλλαγή; Είχα πληρώσει προκαταβολή.", "That's fine, for one night. Will there be a charge for the change? I paid a deposit."),
  L("Υπάλληλος", "f", "Όχι, αφού μας ειδοποιήσατε έγκαιρα, πάνω από σαράντα οκτώ ώρες πριν, δεν υπάρχει χρέωση. Η προκαταβολή μεταφέρεται στη νέα κράτηση. Και επειδή το δεύτερο δωμάτιο είναι φθηνότερο, θα σας κάνουμε έκπτωση είκοσι ευρώ για εκείνη τη νύχτα.", "No, since you let us know in good time, more than forty-eight hours before, there's no charge. The deposit is transferred to the new booking. And because the second room is cheaper, we'll give you a twenty-euro discount for that night."),
  L("Πελάτης", "m", "Τέλεια. Θα σας στείλετε επιβεβαίωση με email;", "Perfect. Will you send me a confirmation by email?"),
  L("Υπάλληλος", "f", "Βεβαίως, μέσα στην επόμενη ώρα. Καλό ταξίδι, και αν περάσετε από το χωριό, δοκιμάστε την τυρόπιτα στο καφενείο της πλατείας!", "Of course, within the next hour. Have a good trip, and if you go through the village, try the cheese pie at the café in the square!"),
 ],
 "questions": [
  Q("Γιατί θέλει ο πελάτης να αλλάξει την κράτηση;", ["Γιατί αρρώστησε", "Γιατί η γυναίκα του έχει υποχρέωση στη δουλειά την Παρασκευή", "Γιατί βρήκε φθηνότερο ξενοδοχείο", "Γιατί χάλασε το αυτοκίνητό του"], 1, "δεν μπορούμε να έρθουμε πριν από το Σάββατο, γιατί η γυναίκα μου έχει μια υποχρέωση στη δουλειά"),
  Q("Τι πρόβλημα υπάρχει με τη Δευτέρα;", ["Το ξενοδοχείο κλείνει", "Το δωμάτιό τους είναι κλεισμένο από μια ομάδα, οπότε θα πάρουν άλλο δωμάτιο", "Δεν υπάρχει λεωφορείο", "Η τιμή είναι διπλή"], 1, "τη Δευτέρα είμαστε πλήρεις ... Μπορώ να σας δώσω για τη Δευτέρα ένα άλλο δωμάτιο"),
  Q("Γιατί δεν θα πληρώσει χρέωση για την αλλαγή;", ["Γιατί είναι τακτικός πελάτης", "Γιατί ειδοποίησε πάνω από σαράντα οκτώ ώρες πριν", "Γιατί δεν είχε πληρώσει προκαταβολή", "Γιατί το ξενοδοχείο έκανε λάθος"], 1, "αφού μας ειδοποιήσατε έγκαιρα, πάνω από σαράντα οκτώ ώρες πριν, δεν υπάρχει χρέωση"),
 ],
 "gloss": {"κράτηση": "κράτηση — booking", "υποχρέωση": "υποχρέωση — commitment, obligation", "Γίνεται να": "γίνεται να — is it possible to", "μετακινήσουμε": "μετακινώ — to move, shift", "πλήρεις": "πλήρης — full", "σύλλογο": "σύλλογος — association, club", "θέα": "θέα — view", "χρέωση": "χρέωση — charge", "προκαταβολή": "προκαταβολή — deposit, advance payment", "ειδοποιήσατε": "ειδοποιώ — to notify", "επιβεβαίωση": "επιβεβαίωση — confirmation"},
})

ITEMS.append({
 "id": "l11-dia-mitera", "title": "Ποιος θα φροντίσει τη μαμά;", "title_en": "Who will look after Mum?", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση ανάμεσα σε δύο αδέρφια, την Κατερίνα και τον Νίκο, για τη μητέρα τους, που έσπασε το πόδι της.",
 "script": [
  L("Κατερίνα", "f", "Νίκο, μίλησα με τον γιατρό. Η μαμά θα βγει από το νοσοκομείο την Πέμπτη, αλλά για έξι εβδομάδες δεν θα μπορεί να περπατάει χωρίς βοήθεια. Δεν γίνεται να μείνει μόνη της στο σπίτι.", "Nikos, I spoke to the doctor. Mum will come out of hospital on Thursday, but for six weeks she won't be able to walk without help. She can't stay alone at home."),
  L("Νίκος", "m", "Το ξέρω. Εγώ σκεφτόμουν να έρθει να μείνει σε μας, αλλά το διαμέρισμά μας είναι στον τέταρτο χωρίς ασανσέρ. Πώς θα ανεβαίνει;", "I know. I was thinking she could come and stay with us, but our flat is on the fourth floor with no lift. How will she get up?"),
  L("Κατερίνα", "f", "Κι εμένα το σπίτι είναι μικρό, και δουλεύω βάρδιες στο νοσοκομείο. Τι λες να μείνει στο δικό της σπίτι, που είναι ισόγειο, και να βρούμε μια κυρία να είναι μαζί της τη μέρα;", "My place is small too, and I work shifts at the hospital. What do you think about her staying in her own house, which is on the ground floor, and us finding a woman to be with her during the day?"),
  L("Νίκος", "m", "Καλή ιδέα, αλλά το κόστος; Μια φροντίστρια για όλη τη μέρα θέλει γύρω στα χίλια ευρώ τον μήνα.", "Good idea, but the cost? A carer for the whole day costs around a thousand euros a month."),
  L("Κατερίνα", "f", "Αν το μοιραστούμε, είναι πεντακόσια ο καθένας, για ενάμιση μήνα. Και τα βράδια μπορούμε να πηγαίνουμε εναλλάξ: εγώ Δευτέρα, Τετάρτη, Παρασκευή, εσύ τις υπόλοιπες. Τα Σαββατοκύριακα θα έρχονται και τα παιδιά.", "If we split it, it's five hundred each, for a month and a half. And in the evenings we can take turns: me on Monday, Wednesday and Friday, you the rest. At weekends the kids will come too."),
  L("Νίκος", "m", "Εντάξει. Μόνο που πρέπει να το πούμε με τρόπο στη μαμά. Ξέρεις πόσο περήφανη είναι· θα πει ότι δεν χρειάζεται κανέναν.", "OK. Only we'll have to tell Mum tactfully. You know how proud she is; she'll say she doesn't need anyone."),
 ],
 "questions": [
  Q("Γιατί η μητέρα δεν μπορεί να μείνει στο σπίτι του Νίκου;", ["Γιατί ο Νίκος μένει σε άλλη πόλη", "Γιατί το διαμέρισμα είναι σε τέταρτο όροφο χωρίς ασανσέρ", "Γιατί δεν τα πάει καλά με τη νύφη της", "Γιατί το σπίτι είναι πολύ ακριβό"], 1, "το διαμέρισμά μας είναι στον τέταρτο χωρίς ασανσέρ"),
  Q("Τι προτείνει η Κατερίνα;", ["Να μπει η μητέρα σε γηροκομείο", "Να μείνει η μητέρα στο δικό της σπίτι με μια φροντίστρια τη μέρα", "Να σταματήσει εκείνη τη δουλειά", "Να μείνει η μητέρα στο νοσοκομείο"], 1, "να μείνει στο δικό της σπίτι ... και να βρούμε μια κυρία να είναι μαζί της τη μέρα"),
  Q("Πώς θα οργανώσουν τα βράδια;", ["Θα μένει πάντα η Κατερίνα", "Θα πηγαίνουν με τη σειρά", "Θα πληρώσουν και βραδινή φροντίστρια", "Θα μένουν τα εγγόνια"], 1, "τα βράδια μπορούμε να πηγαίνουμε εναλλάξ"),
  Q("Τι ανησυχεί τον Νίκο στο τέλος;", ["Το κόστος", "Ότι η μητέρα τους από περηφάνια δεν θα θέλει βοήθεια", "Ότι η φροντίστρια δεν θα είναι καλή", "Ότι η Κατερίνα δουλεύει πολύ"], 1, "Ξέρεις πόσο περήφανη είναι· θα πει ότι δεν χρειάζεται κανέναν."),
 ],
 "gloss": {"έσπασε": "σπάω — to break", "ασανσέρ": "ασανσέρ — lift, elevator", "βάρδιες": "βάρδια — shift", "ισόγειο": "ισόγειο — ground floor", "φροντίστρια": "φροντιστής/φροντίστρια — carer", "Αν το μοιραστούμε": "μοιράζομαι — to share, split", "εναλλάξ": "εναλλάξ — in turns, alternately", "με τρόπο": "με τρόπο — tactfully", "περήφανη": "περήφανος — proud"},
})

ITEMS.append({
 "id": "l11-mon-thiteia", "title": "Η θητεία μου", "title_en": "My military service", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε τον Άγγελο, είκοσι τεσσάρων χρονών, να μιλάει για τη στρατιωτική του θητεία.",
 "script": [
  L("Άγγελος", "m", "Στην Ελλάδα η στρατιωτική θητεία είναι υποχρεωτική για τους άντρες. Εγώ την ανέβαλλα όσο σπούδαζα, και πέρυσι, μόλις πήρα το πτυχίο μου, παρουσιάστηκα στο κέντρο εκπαίδευσης. Ομολογώ ότι πήγα με πολύ κακή διάθεση. Σκεφτόμουν ότι χάνω έναν χρόνο από τη ζωή μου, τη στιγμή που οι φίλοι μου έβρισκαν τις πρώτες τους δουλειές.", "In Greece military service is compulsory for men. I kept putting it off while I was studying, and last year, as soon as I got my degree, I reported to the training centre. I admit I went in a very bad mood. I thought I was losing a year of my life, just when my friends were finding their first jobs."),
  L("Άγγελος", "m", "Οι πρώτες εβδομάδες ήταν δύσκολες. Ξύπνημα στις έξι, σκοπιές τη νύχτα, πειθαρχία σε όλα. Όμως εκεί γνώρισα παιδιά που αλλιώς δεν θα συναντούσα ποτέ: έναν βοσκό από την Κρήτη, έναν προγραμματιστή από τη Θεσσαλονίκη, έναν ψαρά από τη Σάμο. Κοιμόμασταν στον ίδιο θάλαμο, τρώγαμε στο ίδιο τραπέζι, και κάπως έτσι γίναμε φίλοι.", "The first weeks were hard. Getting up at six, guard duty at night, discipline in everything. But there I met people I would never have met otherwise: a shepherd from Crete, a programmer from Thessaloniki, a fisherman from Samos. We slept in the same dormitory, ate at the same table, and somehow that's how we became friends."),
  L("Άγγελος", "m", "Δεν θα πω ότι ο στρατός με άλλαξε ριζικά ή ότι ήταν η καλύτερη χρονιά της ζωής μου. Αλλά έμαθα να συνεννοούμαι με ανθρώπους πολύ διαφορετικούς από εμένα και να αντέχω την κούραση χωρίς να γκρινιάζω συνέχεια. Και κάθε καλοκαίρι, οι τέσσερις μας κανονίζουμε να βρισκόμαστε σε ένα από τα νησιά μας.", "I won't say the army changed me radically or that it was the best year of my life. But I learned to get on with people very different from me and to put up with tiredness without complaining all the time. And every summer the four of us arrange to meet on one of our islands."),
 ],
 "questions": [
  Q("Πώς ένιωθε ο Άγγελος πριν πάει στον στρατό;", ["Ανυπομονούσε", "Ήταν δυσαρεστημένος, γιατί πίστευε ότι θα χάσει χρόνο", "Ήταν περήφανος", "Ήταν αδιάφορος"], 1, "πήγα με πολύ κακή διάθεση. Σκεφτόμουν ότι χάνω έναν χρόνο από τη ζωή μου"),
  Q("Τι εκτίμησε περισσότερο από τη θητεία του;", ["Την εκπαίδευση στα όπλα", "Τη γνωριμία με ανθρώπους πολύ διαφορετικούς από αυτόν", "Τον μισθό", "Τα ταξίδια"], 1, "γνώρισα παιδιά που αλλιώς δεν θα συναντούσα ποτέ"),
  Q("Τι λέει για το πώς τον επηρέασε ο στρατός;", ["Ότι τον άλλαξε εντελώς", "Ότι ήταν η καλύτερη χρονιά της ζωής του", "Ότι έμαθε να συνεννοείται με άλλους και να αντέχει χωρίς γκρίνια", "Ότι δεν έμαθε τίποτα"], 2, "έμαθα να συνεννοούμαι με ανθρώπους πολύ διαφορετικούς από εμένα και να αντέχω την κούραση"),
 ],
 "gloss": {"θητεία": "θητεία — (military) service; term of office", "την ανέβαλλα": "αναβάλλω — to postpone, defer", "πτυχίο": "πτυχίο — (university) degree", "παρουσιάστηκα": "παρουσιάζομαι — to report (for duty)", "Ομολογώ": "ομολογώ — to admit", "σκοπιές": "σκοπιά — guard duty, sentry post", "πειθαρχία": "πειθαρχία — discipline", "βοσκό": "βοσκός — shepherd", "θάλαμο": "θάλαμος — dormitory, ward", "ριζικά": "ριζικά — radically", "να συνεννοούμαι": "συνεννοούμαι — to communicate, get on", "γκρινιάζω": "γκρινιάζω — to complain, grumble"},
})

ITEMS.append({
 "id": "l11-rep-pelargoi", "title": "Οι πελαργοί της Θεσσαλίας", "title_en": "The storks of Thessaly", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από ένα χωριό του θεσσαλικού κάμπου.",
 "script": [
  L("Δημοσιογράφος", "f", "Κάθε άνοιξη, γύρω στα τέλη Φεβρουαρίου, οι κάτοικοι των χωριών του θεσσαλικού κάμπου σηκώνουν το βλέμμα στις στέγες και στις κολόνες της ΔΕΗ. Περιμένουν τους πελαργούς, που επιστρέφουν από την Αφρική για να φωλιάσουν στις ίδιες φωλιές με την προηγούμενη χρονιά.", "Every spring, around the end of February, the people of the villages of the Thessalian plain lift their eyes to the roofs and the electricity poles. They are waiting for the storks, which return from Africa to nest in the same nests as the previous year."),
  L("Δημοσιογράφος", "f", "Οι φωλιές είναι τεράστιες, μπορεί να ζυγίζουν και εκατοντάδες κιλά, και συχνά βρίσκονται πάνω σε καμπαναριά. Οι ντόπιοι τις θεωρούν σημάδι καλοτυχίας και κανείς δεν τολμά να τις πειράξει.", "The nests are huge, they can weigh hundreds of kilos, and they are often found on bell towers. The locals consider them a sign of good luck and nobody dares to touch them."),
  L("Δημοσιογράφος", "f", "Οι ορνιθολόγοι, ωστόσο, ανησυχούν. Οι πλημμύρες των τελευταίων χρόνων κατέστρεψαν μεγάλο μέρος των υγροτόπων όπου τα πουλιά βρίσκουν τροφή, ενώ τα φυτοφάρμακα μειώνουν τα έντομα και τα βατράχια. Γι' αυτό ζητούν από τους αγρότες να αφήνουν μικρές λωρίδες γης ακαλλιέργητες.", "Ornithologists, however, are worried. The floods of recent years destroyed a large part of the wetlands where the birds find food, while pesticides are reducing insects and frogs. That is why they are asking farmers to leave small strips of land uncultivated."),
 ],
 "questions": [
  Q("Τι κάνουν οι πελαργοί όταν επιστρέφουν;", ["Χτίζουν πάντα καινούργιες φωλιές", "Χρησιμοποιούν τις φωλιές της προηγούμενης χρονιάς", "Μένουν μόνο λίγες μέρες", "Πηγαίνουν στις πόλεις"], 1, "για να φωλιάσουν στις ίδιες φωλιές με την προηγούμενη χρονιά"),
  Q("Πώς βλέπουν οι κάτοικοι τις φωλιές;", ["Ως πρόβλημα για τα σπίτια τους", "Ως σημάδι καλοτυχίας", "Ως αξιοθέατο για τουρίστες", "Ως κίνδυνο για το ηλεκτρικό δίκτυο"], 1, "Οι ντόπιοι τις θεωρούν σημάδι καλοτυχίας"),
  Q("Τι ζητούν οι ορνιθολόγοι από τους αγρότες;", ["Να αφήνουν λωρίδες γης χωρίς καλλιέργεια", "Να χτίζουν τεχνητές φωλιές", "Να ταΐζουν τα πουλιά", "Να σταματήσουν να ποτίζουν"], 0, "ζητούν από τους αγρότες να αφήνουν μικρές λωρίδες γης ακαλλιέργητες"),
 ],
 "gloss": {"πελαργούς": "πελαργός — stork", "θεσσαλικού κάμπου": "θεσσαλικός κάμπος — Thessalian plain", "σηκώνουν το βλέμμα": "σηκώνω το βλέμμα — to look up", "φωλιάσουν": "φωλιάζω — to nest", "καμπαναριά": "καμπαναριό — bell tower", "καλοτυχίας": "καλοτυχία — good luck", "πειράξει": "πειράζω — to touch, disturb", "ορνιθολόγοι": "ορνιθολόγος — ornithologist", "υγροτόπων": "υγρότοπος — wetland", "φυτοφάρμακα": "φυτοφάρμακο — pesticide", "λωρίδες": "λωρίδα — strip", "ακαλλιέργητες": "ακαλλιέργητος — uncultivated"},
})

ITEMS.append({
 "id": "l11-rep-kafeneia", "title": "Το τελευταίο καφενείο του χωριού", "title_en": "The last café in the village", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τα καφενεία που κλείνουν στα ορεινά χωριά.",
 "script": [
  L("Δημοσιογράφος", "m", "Στην πλατεία του χωριού, κάτω από τον πλάτανο, ο κυρ Θανάσης ανοίγει το καφενείο του κάθε πρωί στις έξι, όπως έκανε και ο πατέρας του. Σήμερα όμως οι θαμώνες είναι μόλις τέσσερις, όλοι πάνω από εβδομήντα.", "In the village square, under the plane tree, Mr Thanasis opens his café every morning at six, as his father did. Today, however, there are only four regulars, all over seventy."),
  L("Θανάσης", "m", "Παλιά δεν έβρισκες καρέκλα. Εδώ έπιναν τον καφέ τους, εδώ έπαιζαν τάβλι, εδώ μάθαιναν τα νέα. Εδώ ήταν και το τηλέφωνο του χωριού, το μοναδικό. Τώρα οι νέοι έφυγαν στην πόλη και κανείς δεν θέλει να το συνεχίσει.", "In the old days you couldn't find a chair. Here they drank their coffee, here they played backgammon, here they heard the news. The village telephone was here too, the only one. Now the young people have left for the city and nobody wants to carry it on."),
  L("Δημοσιογράφος", "m", "Σε κάποιους δήμους έχουν βρει λύσεις: το καφενείο γίνεται ταυτόχρονα και μικρό παντοπωλείο, σημείο παραλαβής δεμάτων ή και χώρος όπου ο γιατρός του κέντρου υγείας εξετάζει μία φορά την εβδομάδα. Έτσι, το καφενείο συνεχίζει να είναι η καρδιά του χωριού.", "Some municipalities have found solutions: the café also becomes a small grocery, a parcel pick-up point, or even a place where the health-centre doctor sees patients once a week. In this way, the café continues to be the heart of the village."),
 ],
 "questions": [
  Q("Ποιοι είναι οι πελάτες του καφενείου σήμερα;", ["Τουρίστες", "Λίγοι ηλικιωμένοι", "Νέοι από την πόλη", "Εργάτες από τα χωράφια"], 1, "οι θαμώνες είναι μόλις τέσσερις, όλοι πάνω από εβδομήντα"),
  Q("Γιατί κινδυνεύει να κλείσει το καφενείο;", ["Επειδή ο δήμος το απαγορεύει", "Επειδή οι νέοι έφυγαν και κανείς δεν θα το συνεχίσει", "Επειδή ο καφές ακρίβυνε", "Επειδή άνοιξε άλλο καφενείο"], 1, "οι νέοι έφυγαν στην πόλη και κανείς δεν θέλει να το συνεχίσει"),
  Q("Ποια λύση αναφέρεται;", ["Να γίνει μουσείο", "Να πουληθεί σε εταιρεία", "Να προσφέρει και άλλες υπηρεσίες, όπως παραλαβή δεμάτων", "Να ανοίγει μόνο το καλοκαίρι"], 2, "το καφενείο γίνεται ταυτόχρονα και μικρό παντοπωλείο, σημείο παραλαβής δεμάτων"),
 ],
 "gloss": {"πλάτανο": "πλάτανος — plane tree", "κυρ Θανάσης": "κυρ — Mr (colloquial, before a first name)", "θαμώνες": "θαμώνας — regular customer", "δεν έβρισκες καρέκλα": "δεν βρίσκεις καρέκλα — there isn't a free chair", "τάβλι": "τάβλι — backgammon", "να το συνεχίσει": "συνεχίζω — to carry on", "δήμους": "δήμος — municipality", "παντοπωλείο": "παντοπωλείο — grocery shop", "σημείο παραλαβής δεμάτων": "σημείο παραλαβής δεμάτων — parcel pick-up point", "κέντρου υγείας": "κέντρο υγείας — health centre"},
})

ITEMS.append({
 "id": "l11-int-paixnidia", "title": "Φτιάχνοντας βιντεοπαιχνίδια στην Ελλάδα", "title_en": "Making video games in Greece", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια νέα δημιουργό βιντεοπαιχνιδιών.",
 "script": [
  L("Δημοσιογράφος", "m", "Το παιχνίδι σας κατέβηκε πάνω από διακόσιες χιλιάδες φορές τον πρώτο μήνα. Το περιμένατε;", "Your game was downloaded more than two hundred thousand times in the first month. Did you expect it?"),
  L("Ιωάννα", "f", "Καθόλου! Είμαστε μια ομάδα πέντε ατόμων και δουλεύαμε τρία χρόνια σε ένα μικρό γραφείο στη Θεσσαλονίκη, τα πρώτα δύο χωρίς μισθό. Ζούσαμε με τις οικονομίες μας και με μικροδουλειές.", "Not at all! We're a team of five and we worked for three years in a small office in Thessaloniki, the first two without pay. We lived on our savings and on odd jobs."),
  L("Δημοσιογράφος", "m", "Το παιχνίδι βασίζεται στην ελληνική μυθολογία. Δεν φοβηθήκατε ότι είναι ένα θέμα που έχει χρησιμοποιηθεί πολλές φορές;", "The game is based on Greek mythology. Weren't you afraid it is a theme that has been used many times?"),
  L("Ιωάννα", "f", "Ναι, γι' αυτό αποφασίσαμε να μην έχουμε ως ήρωα κάποιον θεό ή τον Ηρακλή, αλλά ένα κορίτσι από ένα νησί που πρέπει να σώσει το χωριό της. Οι μύθοι είναι στο φόντο. Και η μουσική είναι από παραδοσιακά νησιώτικα όργανα, κάτι που οι παίκτες στο εξωτερικό λάτρεψαν.", "Yes, that's why we decided not to have a god or Heracles as the hero, but a girl from an island who has to save her village. The myths are in the background. And the music comes from traditional island instruments, something players abroad loved."),
  L("Δημοσιογράφος", "m", "Τι θα λέγατε σε έναν νέο που θέλει να ασχοληθεί με αυτόν τον χώρο;", "What would you say to a young person who wants to get into this field?"),
  L("Ιωάννα", "f", "Να ξεκινήσει με κάτι μικρό και να το τελειώσει. Οι περισσότεροι αρχίζουν με τεράστια σχέδια και τα παρατάνε στη μέση.", "To start with something small and finish it. Most people start with huge plans and give up halfway."),
 ],
 "questions": [
  Q("Πώς ζούσε η ομάδα τα πρώτα χρόνια;", ["Με χρηματοδότηση από εταιρεία", "Με τις οικονομίες τους και μικροδουλειές", "Με κρατική επιχορήγηση", "Με τα έσοδα από προηγούμενο παιχνίδι"], 1, "Ζούσαμε με τις οικονομίες μας και με μικροδουλειές."),
  Q("Πώς διαφέρει το παιχνίδι από άλλα με θέμα τη μυθολογία;", ["Ο ήρωας είναι ο Ηρακλής", "Η πρωταγωνίστρια είναι ένα απλό κορίτσι από νησί", "Δεν έχει καθόλου μύθους", "Παίζεται μόνο στα ελληνικά"], 1, "ένα κορίτσι από ένα νησί που πρέπει να σώσει το χωριό της"),
  Q("Ποια συμβουλή δίνει η Ιωάννα;", ["Να ξεκινάς με μεγάλα σχέδια", "Να φύγεις στο εξωτερικό", "Να ξεκινάς με κάτι μικρό και να το ολοκληρώνεις", "Να σπουδάσεις πρώτα μουσική"], 2, "Να ξεκινήσει με κάτι μικρό και να το τελειώσει."),
 ],
 "gloss": {"κατέβηκε": "κατεβαίνω — (of an app, game) to be downloaded", "χωρίς μισθό": "μισθός — salary, pay", "οικονομίες": "οικονομίες — savings", "μικροδουλειές": "μικροδουλειά — odd job", "βασίζεται": "βασίζομαι — to be based (on)", "στο φόντο": "φόντο — background", "νησιώτικα όργανα": "νησιώτικος — island (adj.); όργανο — instrument", "λάτρεψαν": "λατρεύω — to adore", "να ασχοληθεί": "ασχολούμαι με — to get involved in, work in", "τα παρατάνε": "τα παρατάω — to give up, abandon"},
})

ITEMS.append({
 "id": "l11-mon-polykatoikia", "title": "Η πολυκατοικία και η αντιπαροχή", "title_en": "The apartment block and the antiparochi system", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια αρχιτέκτονα να μιλά σε ένα σεμινάριο για την ιστορία της αθηναϊκής πολυκατοικίας.",
 "script": [
  L("Αρχιτέκτονας", "f", "Όποιος πετάξει πάνω από την Αθήνα βλέπει μια λευκή θάλασσα από πολυκατοικίες. Αυτή η εικόνα δεν είναι προϊόν κεντρικού σχεδιασμού· είναι κυρίως αποτέλεσμα ενός θεσμού που εφαρμόστηκε μαζικά από τη δεκαετία του '50 και μετά: της αντιπαροχής.", "Anyone who flies over Athens sees a white sea of apartment blocks. This image is not the product of central planning; it is mainly the result of an arrangement applied massively from the 1950s onwards: the antiparochi."),
  L("Αρχιτέκτονας", "f", "Ο μηχανισμός ήταν απλός. Ο ιδιοκτήτης ενός οικοπέδου με μια μονοκατοικία, που συνήθως δεν είχε χρήματα να χτίσει, το παραχωρούσε σε έναν εργολάβο. Εκείνος έχτιζε πολυκατοικία με δικά του έξοδα και, σε αντάλλαγμα, ο ιδιοκτήτης έπαιρνε μερικά διαμερίσματα, ενώ τα υπόλοιπα τα πουλούσε ο εργολάβος.", "The mechanism was simple. The owner of a plot with a single-family house, who usually had no money to build, would hand it over to a contractor. The contractor built an apartment block at his own expense and, in exchange, the owner received a few flats, while the contractor sold the rest."),
  L("Αρχιτέκτονας", "f", "Το σύστημα αυτό στέγασε εκατομμύρια ανθρώπους που έφταναν από την επαρχία, χωρίς κρατικό δανεισμό, και δημιούργησε μια ευρεία μεσαία τάξη ιδιοκτητών. Το τίμημα όμως ήταν βαρύ: χάθηκαν νεοκλασικά κτίρια, οι ελεύθεροι χώροι και το πράσινο περιορίστηκαν δραματικά, και η πόλη πύκνωσε χωρίς σχέδιο.", "This system housed millions of people arriving from the provinces, without state borrowing, and created a broad middle class of owners. But the price was heavy: neoclassical buildings were lost, open spaces and greenery were dramatically reduced, and the city grew denser without a plan."),
  L("Αρχιτέκτονας", "f", "Σήμερα συζητάμε αν η πολυκατοικία είναι πρόβλημα ή κληρονομιά. Η άποψή μου είναι ότι αποτελεί και τα δύο. Με τις πιλοτές, τους ακάλυπτους και τις ταράτσες της, προσφέρει χώρους που, αν τους ξαναδούμε με φαντασία, μπορούν να δώσουν στην πόλη την ανάσα που της λείπει.", "Today we debate whether the apartment block is a problem or a heritage. My view is that it is both. With its pilotis, its inner courtyards and its roof terraces, it offers spaces which, if we look at them again with imagination, can give the city the breathing room it lacks."),
 ],
 "questions": [
  Q("Σύμφωνα με την ομιλήτρια, πώς διαμορφώθηκε η σημερινή εικόνα της Αθήνας;", ["Με ένα κεντρικό πολεοδομικό σχέδιο", "Κυρίως μέσω της αντιπαροχής", "Με κρατικές κατοικίες", "Με ξένες επενδύσεις"], 1, "είναι κυρίως αποτέλεσμα ενός θεσμού ... της αντιπαροχής"),
  Q("Τι έπαιρνε ο ιδιοκτήτης του οικοπέδου;", ["Ολόκληρη την πολυκατοικία", "Ένα ποσό σε μετρητά", "Μερικά διαμερίσματα", "Ένα κρατικό δάνειο"], 2, "σε αντάλλαγμα, ο ιδιοκτήτης έπαιρνε μερικά διαμερίσματα"),
  Q("Ποιο θετικό αποτέλεσμα αναγνωρίζει;", ["Τη διάσωση των νεοκλασικών", "Τη στέγαση εκατομμυρίων χωρίς κρατικό δανεισμό", "Την αύξηση του πρασίνου", "Τον σωστό πολεοδομικό σχεδιασμό"], 1, "στέγασε εκατομμύρια ανθρώπους ... χωρίς κρατικό δανεισμό"),
  Q("Ποια είναι η τελική της θέση;", ["Οι πολυκατοικίες πρέπει να γκρεμιστούν", "Η πολυκατοικία είναι και πρόβλημα και κληρονομιά, με δυνατότητες", "Η αντιπαροχή πρέπει να επανέλθει", "Η Αθήνα δεν έχει ανάγκη από ελεύθερους χώρους"], 1, "Η άποψή μου είναι ότι αποτελεί και τα δύο."),
 ],
 "gloss": {"κεντρικού σχεδιασμού": "κεντρικός σχεδιασμός — central planning", "θεσμού": "θεσμός — institution, arrangement", "αντιπαροχής": "αντιπαροχή — system where a landowner gives a plot to a builder in exchange for flats", "οικοπέδου": "οικόπεδο — building plot", "παραχωρούσε": "παραχωρώ — to hand over, grant", "εργολάβο": "εργολάβος — building contractor", "σε αντάλλαγμα": "σε αντάλλαγμα — in exchange", "στέγασε": "στεγάζω — to house", "επαρχία": "επαρχία — the provinces", "δανεισμό": "δανεισμός — borrowing", "τίμημα": "τίμημα — price, cost", "πύκνωσε": "πυκνώνω — to become denser", "κληρονομιά": "κληρονομιά — heritage, inheritance", "πιλοτές": "πιλοτή — pilotis, open ground floor on columns", "ακάλυπτους": "ακάλυπτος — inner courtyard of a block", "ταράτσες": "ταράτσα — flat roof terrace", "την ανάσα": "ανάσα — breath; (here) breathing room"},
})

ITEMS.append({
 "id": "l11-int-stegasi", "title": "Γιατί δεν βρίσκουμε σπίτι;", "title_en": "Why can't we find a home?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν οικονομολόγο για το στεγαστικό πρόβλημα.",
 "script": [
  L("Δημοσιογράφος", "f", "Τα ενοίκια στην Αθήνα έχουν αυξηθεί πάνω από πενήντα τοις εκατό σε λίγα χρόνια. Πού οφείλεται αυτή η εκτίναξη;", "Rents in Athens have risen by more than fifty per cent in a few years. What is behind this surge?"),
  L("Οικονομολόγος", "m", "Δεν υπάρχει μία αιτία. Κατά τη διάρκεια της κρίσης σχεδόν σταμάτησε η ανέγερση νέων κατοικιών, άρα η προσφορά έμεινε στάσιμη. Ταυτόχρονα, ένα σημαντικό μέρος των διαμερισμάτων στο κέντρο πέρασε στη βραχυχρόνια μίσθωση για τουρίστες, ενώ πολλά άλλα μένουν κλειστά, επειδή οι ιδιοκτήτες φοβούνται κακοπληρωτές ή δεν έχουν χρήματα να τα ανακαινίσουν.", "There isn't one cause. During the crisis the construction of new housing almost stopped, so supply stayed stagnant. At the same time, a significant share of the flats in the centre moved to short-term rental for tourists, while many others remain closed, because owners fear tenants who won't pay or don't have the money to renovate them."),
  L("Δημοσιογράφος", "f", "Η κυβέρνηση έχει ανακοινώσει επιδοτήσεις για νέους. Βοηθούν;", "The government has announced subsidies for young people. Do they help?"),
  L("Οικονομολόγος", "m", "Βραχυπρόθεσμα ανακουφίζουν κάποια νοικοκυριά, αλλά υπάρχει ο κίνδυνος, όταν αυξάνεις τη ζήτηση χωρίς να αυξάνεις την προσφορά, απλώς να ανεβαίνουν κι άλλο οι τιμές. Το ουσιαστικό ζητούμενο είναι να επιστρέψουν στην αγορά τα κλειστά σπίτια και να χτιστούν νέα, ίσως και κοινωνικές κατοικίες, που στην Ελλάδα σχεδόν δεν υπάρχουν.", "In the short term they relieve some households, but there is the risk, when you increase demand without increasing supply, that prices simply rise further. The real issue is for closed homes to return to the market and for new ones to be built, perhaps social housing too, which barely exists in Greece."),
  L("Δημοσιογράφος", "f", "Και οι νέοι, μέχρι τότε;", "And young people, in the meantime?"),
  L("Οικονομολόγος", "m", "Μένουν με τους γονείς τους μέχρι τα τριάντα και κάτι, όπως δείχνουν όλα τα στοιχεία. Αυτό δεν είναι πολιτισμική επιλογή, όπως λέγεται συχνά· είναι κυρίως οικονομική αναγκαιότητα, με συνέπειες και για τη γεννητικότητα.", "They live with their parents until their thirties, as all the data show. This is not a cultural choice, as is often said; it is mainly an economic necessity, with consequences for the birth rate too."),
 ],
 "questions": [
  Q("Ποια αιτία της αύξησης των ενοικίων ΔΕΝ αναφέρει ο οικονομολόγος;", ["Η στασιμότητα στην ανέγερση κατοικιών", "Η βραχυχρόνια μίσθωση σε τουρίστες", "Τα κλειστά διαμερίσματα", "Η αύξηση του πληθυσμού της Αθήνας"], 3, "Αναφέρει την ανέγερση, τη βραχυχρόνια μίσθωση και τα κλειστά σπίτια· όχι τον πληθυσμό."),
  Q("Ποιος είναι ο κίνδυνος των επιδοτήσεων;", ["Να μην τις ζητήσει κανείς", "Να αυξηθούν ακόμα περισσότερο οι τιμές", "Να κοστίσουν πολύ στο κράτος", "Να ωφελήσουν μόνο τους ιδιοκτήτες τουριστικών καταλυμάτων"], 1, "όταν αυξάνεις τη ζήτηση χωρίς να αυξάνεις την προσφορά, απλώς να ανεβαίνουν κι άλλο οι τιμές"),
  Q("Πώς ερμηνεύει το ότι οι νέοι μένουν με τους γονείς τους;", ["Ως πολιτισμική παράδοση", "Ως προσωπική επιλογή", "Κυρίως ως οικονομική αναγκαιότητα", "Ως αποτέλεσμα των σπουδών"], 2, "δεν είναι πολιτισμική επιλογή ... είναι κυρίως οικονομική αναγκαιότητα"),
 ],
 "gloss": {"εκτίναξη": "εκτίναξη — surge, sharp rise", "ανέγερση": "ανέγερση — construction, erection (of buildings)", "προσφορά": "προσφορά — supply; offer", "στάσιμη": "στάσιμος — stagnant", "βραχυχρόνια μίσθωση": "βραχυχρόνια μίσθωση — short-term rental", "κακοπληρωτές": "κακοπληρωτής — bad payer", "επιδοτήσεις": "επιδότηση — subsidy", "Βραχυπρόθεσμα": "βραχυπρόθεσμα — in the short term", "ανακουφίζουν": "ανακουφίζω — to relieve", "νοικοκυριά": "νοικοκυριό — household", "ζήτηση": "ζήτηση — demand", "ζητούμενο": "ζητούμενο — the real issue, what is needed", "κοινωνικές κατοικίες": "κοινωνική κατοικία — social housing", "αναγκαιότητα": "αναγκαιότητα — necessity", "γεννητικότητα": "γεννητικότητα — birth rate"},
})
rnd = random.Random(11)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-11.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
