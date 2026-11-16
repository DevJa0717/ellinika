# Source for library/listening/listening-84.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l84.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l84-ann-pyrasfaleia", "title": "Άσκηση πυρασφάλειας στο ξενοδοχείο", "title_en": "Fire drill at the hotel", "type": "announcement", "level": "B2",
 "context_el": "Μένετε σε ένα ξενοδοχείο. Από τα μεγάφωνα του διαδρόμου ακούτε μια ανακοίνωση.",
 "script": [
  L("Υπεύθυνη", "f", "Αγαπητοί επισκέπτες, καλημέρα σας. Σας ενημερώνουμε ότι σήμερα, στις έντεκα το πρωί, θα γίνει άσκηση πυρασφάλειας. Θα ακούσετε τον συναγερμό για περίπου δύο λεπτά. Δεν υπάρχει κανένας πραγματικός κίνδυνος.", "Dear guests, good morning. We inform you that today, at eleven in the morning, there will be a fire drill. You will hear the alarm for about two minutes. There is no real danger."),
  L("Υπεύθυνη", "f", "Όταν ακούσετε τον συναγερμό, παρακαλούμε να αφήσετε τα πράγματά σας στο δωμάτιο και να βγείτε από το κτίριο από τις σκάλες κινδύνου, που σημειώνονται με πράσινα φωτεινά σήματα. Μη χρησιμοποιείτε τους ανελκυστήρες σε καμία περίπτωση.", "When you hear the alarm, please leave your belongings in your room and leave the building by the emergency stairs, which are marked with green illuminated signs. Do not use the lifts under any circumstances."),
  L("Υπεύθυνη", "f", "Το σημείο συγκέντρωσης βρίσκεται στο πάρκινγκ, απέναντι από την κεντρική είσοδο. Εκεί το προσωπικό θα ελέγξει ότι όλοι οι επισκέπτες βγήκαν με ασφάλεια. Η άσκηση θα διαρκέσει περίπου είκοσι λεπτά, και στη συνέχεια το εστιατόριο θα σας προσφέρει δωρεάν καφέ. Ευχαριστούμε για τη συνεργασία.", "The assembly point is in the car park, opposite the main entrance. There the staff will check that all guests have left safely. The drill will last about twenty minutes, and afterwards the restaurant will offer you free coffee. Thank you for your cooperation."),
 ],
 "questions": [
  Q("Τι πρέπει να κάνουν οι επισκέπτες όταν ακούσουν τον συναγερμό;", ["Να πάρουν μαζί τις βαλίτσες τους", "Να μείνουν στο δωμάτιο", "Να βγουν από τις σκάλες κινδύνου", "Να κατέβουν με τον ανελκυστήρα"], 2, "να βγείτε από το κτίριο από τις σκάλες κινδύνου"),
  Q("Πού βρίσκεται το σημείο συγκέντρωσης;", ["Στη ρεσεψιόν", "Στο πάρκινγκ, απέναντι από την κεντρική είσοδο", "Στην πισίνα", "Στον κήπο πίσω από το ξενοδοχείο"], 1, "Το σημείο συγκέντρωσης βρίσκεται στο πάρκινγκ, απέναντι από την κεντρική είσοδο"),
  Q("Τι θα προσφέρει το εστιατόριο μετά την άσκηση;", ["Δωρεάν πρωινό", "Δωρεάν καφέ", "Έκπτωση στο δείπνο", "Ένα ποτό στο μπαρ"], 1, "το εστιατόριο θα σας προσφέρει δωρεάν καφέ"),
 ],
 "gloss": {"άσκηση πυρασφάλειας": "άσκηση πυρασφάλειας — fire drill", "συναγερμό": "συναγερμός — alarm", "σκάλες κινδύνου": "σκάλα κινδύνου — emergency stairs", "φωτεινά σήματα": "φωτεινό σήμα — illuminated sign", "ανελκυστήρες": "ανελκυστήρας — lift", "σημείο συγκέντρωσης": "σημείο συγκέντρωσης — assembly point", "προσωπικό": "προσωπικό — staff"},
})
ITEMS.append({
 "id": "l84-vm-kalorifer", "title": "Μήνυμα από τον ιδιοκτήτη για το καλοριφέρ", "title_en": "Voicemail from the landlord about the heating", "type": "voicemail", "level": "B2",
 "context_el": "Νοικιάζετε ένα διαμέρισμα. Ακούτε ένα μήνυμα από τον ιδιοκτήτη στον τηλεφωνητή σας.",
 "script": [
  L("Κύριος Παπαδάκης", "m", "Καλησπέρα σας, ο Παπαδάκης είμαι, ο ιδιοκτήτης. Έλαβα το μήνυμά σας ότι το καλοριφέρ στο υπνοδωμάτιο δεν ζεσταίνεται. Μίλησα με τον υδραυλικό, και μου είπε ότι μάλλον έχει αέρα μέσα και χρειάζεται εξαέρωση. Είναι απλό, αλλά πρέπει να το κάνει τεχνικός.", "Good evening, it's Papadakis, the landlord. I got your message that the radiator in the bedroom isn't heating up. I spoke to the plumber, and he told me it probably has air in it and needs bleeding. It's simple, but a technician has to do it."),
  L("Κύριος Παπαδάκης", "m", "Μπορεί να περάσει την Πέμπτη το πρωί, γύρω στις δέκα. Αν δεν είστε στο σπίτι, μπορείτε να αφήσετε το κλειδί στην κυρία Ελένη, στο ισόγειο· τη γνωρίζει. Θα του πάρει περίπου μισή ώρα.", "He can come on Thursday morning, around ten. If you're not at home, you can leave the key with Mrs Eleni on the ground floor; she knows him. It'll take him about half an hour."),
  L("Κύριος Παπαδάκης", "m", "Μέχρι τότε, σας παρακαλώ, μην ανοίξετε μόνος σας τη βαλβίδα, γιατί τρέχουν νερά και μπορεί να λερωθεί το πάτωμα. Την επίσκεψη την πληρώνω εγώ, φυσικά. Πείτε μου αν σας βολεύει η Πέμπτη. Καλό βράδυ.", "Until then, please don't open the valve yourself, because water comes out and the floor may get dirty. I'll pay for the visit, of course. Let me know if Thursday suits you. Good night."),
 ],
 "questions": [
  Q("Τι πιστεύει ο υδραυλικός ότι έχει το καλοριφέρ;", ["Είναι χαλασμένο και πρέπει να αλλάξει", "Έχει αέρα μέσα", "Δεν έχει νερό", "Έχει διαρροή"], 1, "μάλλον έχει αέρα μέσα"),
  Q("Πού μπορεί ο ενοικιαστής να αφήσει το κλειδί;", ["Στον θυρωρό", "Κάτω από το χαλάκι", "Στην κυρία Ελένη, στο ισόγειο", "Στο γραφείο του ιδιοκτήτη"], 2, "μπορείτε να αφήσετε το κλειδί στην κυρία Ελένη, στο ισόγειο"),
  Q("Γιατί δεν πρέπει να ανοίξει ο ενοικιαστής τη βαλβίδα;", ["Γιατί είναι επικίνδυνο", "Γιατί τρέχουν νερά και μπορεί να λερωθεί το πάτωμα", "Γιατί θα σπάσει", "Γιατί θα πληρώσει πρόστιμο"], 1, "γιατί τρέχουν νερά και μπορεί να λερωθεί το πάτωμα"),
 ],
 "gloss": {"καλοριφέρ": "καλοριφέρ — radiator, central heating", "ιδιοκτήτης": "ιδιοκτήτης — owner, landlord", "υδραυλικό": "υδραυλικός — plumber", "εξαέρωση": "εξαέρωση — bleeding (of a radiator)", "ισόγειο": "ισόγειο — ground floor", "βαλβίδα": "βαλβίδα — valve", "λερωθεί": "λερώνομαι — to get dirty"},
})
ITEMS.append({
 "id": "l84-dia-strifoma", "title": "Στον ράφτη για ένα στρίφωμα", "title_en": "At the tailor's for a hem", "type": "dialogue", "level": "B2",
 "context_el": "Μια πελάτισσα πηγαίνει σε ένα ραφείο της γειτονιάς με ένα καινούργιο παντελόνι.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Αγόρασα αυτό το παντελόνι για τον γάμο της αδερφής μου, αλλά μου είναι μακρύ. Μπορείτε να μου κάνετε στρίφωμα;", "Good morning. I bought these trousers for my sister's wedding, but they're too long for me. Can you take up the hem?"),
  L("Ράφτης", "m", "Βεβαίως. Θα το φορέσετε με τακούνια ή με φλατ παπούτσια; Αυτό έχει μεγάλη σημασία για το μήκος. Αν τα έχετε μαζί σας, καλύτερα να τα φορέσετε τώρα, για να το μετρήσω σωστά.", "Of course. Will you wear them with heels or flat shoes? That matters a lot for the length. If you have them with you, it's best to put them on now, so I can measure properly."),
  L("Πελάτισσα", "f", "Με τακούνια, και τα έφερα. Πόσο θα κοστίσει και πότε θα είναι έτοιμο; Ο γάμος είναι το Σάββατο.", "With heels, and I brought them. How much will it cost and when will it be ready? The wedding is on Saturday."),
  L("Ράφτης", "m", "Δώδεκα ευρώ. Κανονικά χρειάζομαι μία εβδομάδα, γιατί έχω πολλή δουλειά, αλλά για γάμο θα το έχετε την Πέμπτη το απόγευμα. Βλέπω όμως ότι το ύφασμα είναι λεπτό. Θα σας πρότεινα να το ράψω στο χέρι, για να μη φαίνεται η ραφή απ’ έξω.", "Twelve euros. Normally I need a week, because I have a lot of work, but for a wedding you'll have it on Thursday afternoon. I can see, though, that the fabric is thin. I'd suggest sewing it by hand, so the stitching doesn't show on the outside."),
  L("Πελάτισσα", "f", "Αυτό κοστίζει περισσότερο;", "Does that cost more?"),
  L("Ράφτης", "m", "Πέντε ευρώ παραπάνω. Αλλά σε γάμο θα σας κοιτάνε όλοι, και δεν θέλουμε να φαίνεται η κλωστή στις φωτογραφίες.", "Five euros more. But at a wedding everyone will be looking at you, and we don't want the thread to show in the photos."),
 ],
 "questions": [
  Q("Γιατί ο ράφτης ρωτάει για τα παπούτσια;", ["Γιατί πουλάει και παπούτσια", "Γιατί έχουν σημασία για το μήκος", "Γιατί θέλει να ταιριάζει το χρώμα", "Γιατί θέλει να τα επισκευάσει"], 1, "Αυτό έχει μεγάλη σημασία για το μήκος"),
  Q("Πότε θα είναι έτοιμο το παντελόνι;", ["Σε μία εβδομάδα", "Την Παρασκευή το πρωί", "Την Πέμπτη το απόγευμα", "Το Σάββατο"], 2, "για γάμο θα το έχετε την Πέμπτη το απόγευμα"),
  Q("Γιατί προτείνει να το ράψει στο χέρι;", ["Γιατί η ραπτομηχανή του είναι χαλασμένη", "Για να μη φαίνεται η ραφή απ’ έξω", "Γιατί είναι πιο γρήγορο", "Γιατί είναι φθηνότερο"], 1, "για να μη φαίνεται η ραφή απ’ έξω"),
 ],
 "gloss": {"ραφείο": "ραφείο — tailor's shop", "στρίφωμα": "στρίφωμα — hem", "τακούνια": "τακούνι — heel", "μήκος": "μήκος — length", "ύφασμα": "ύφασμα — fabric", "ράψω": "ράβω — to sew", "ραφή": "ραφή — seam, stitching", "κλωστή": "κλωστή — thread"},
})
ITEMS.append({
 "id": "l84-int-fylakas-mouseiou", "title": "Η φύλακας του μουσείου", "title_en": "The museum guard", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, ένας δημοσιογράφος μιλά με μια φύλακα αρχαιοτήτων σε ένα μεγάλο μουσείο της Αθήνας.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Μαυρίδου, πόσα χρόνια φυλάτε αρχαία;", "Ms Mavridou, how many years have you been guarding antiquities?"),
  L("Ελπίδα", "f", "Δεκαοχτώ. Σπούδασα αρχαιολογία, αλλά δεν βρήκα δουλειά σε ανασκαφές, και έκανα αίτηση για φύλακας. Νόμιζα ότι θα ήταν προσωρινό. Τελικά ερωτεύτηκα τη δουλειά. Περνάω οχτώ ώρες τη μέρα με αγάλματα δυόμισι χιλιάδων χρόνων. Ποιος άλλος μπορεί να το πει αυτό;", "Eighteen. I studied archaeology, but I couldn't find work on excavations, so I applied to be a guard. I thought it would be temporary. In the end I fell in love with the job. I spend eight hours a day with statues two and a half thousand years old. Who else can say that?"),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο συνηθισμένο πρόβλημα με τους επισκέπτες;", "What's the most common problem with visitors?"),
  L("Ελπίδα", "f", "Ότι θέλουν να αγγίξουν τα εκθέματα. Δεν το κάνουν από κακία· απλώς ένα μάρμαρο σε προσκαλεί να το χαϊδέψεις. Όμως το λίπος από τα χέρια μας αφήνει σημάδια, και με εκατομμύρια επισκέπτες η ζημιά θα ήταν τεράστια. Το δεύτερο πρόβλημα είναι οι σέλφι: οι άνθρωποι κάνουν βήματα προς τα πίσω χωρίς να κοιτάζουν.", "That they want to touch the exhibits. They don't do it out of malice; a marble simply invites you to stroke it. But the oil from our hands leaves marks, and with millions of visitors the damage would be enormous. The second problem is selfies: people step backwards without looking."),
  L("Δημοσιογράφος", "m", "Έχετε αγαπημένο έκθεμα;", "Do you have a favourite exhibit?"),
  L("Ελπίδα", "f", "Ένα μικρό επιτύμβιο ανάγλυφο, με ένα κορίτσι που κρατάει ένα περιστέρι. Δεν είναι από τα διάσημα, και οι περισσότεροι περνάνε από μπροστά του χωρίς να σταματήσουν. Εγώ το καλημερίζω κάθε πρωί. Μερικές φορές νομίζω ότι είμαι η μόνη που το βλέπει πραγματικά.", "A small funerary relief, with a girl holding a dove. It's not one of the famous ones, and most people walk past it without stopping. I say good morning to it every day. Sometimes I think I'm the only one who really sees it."),
 ],
 "questions": [
  Q("Πώς έγινε η Ελπίδα φύλακας;", ["Ήταν το όνειρό της από παιδί", "Δεν βρήκε δουλειά σε ανασκαφές και έκανε αίτηση", "Τη σύστησε ένας καθηγητής της", "Δούλευε πριν στο πωλητήριο του μουσείου"], 1, "δεν βρήκα δουλειά σε ανασκαφές, και έκανα αίτηση για φύλακας"),
  Q("Γιατί δεν πρέπει οι επισκέπτες να αγγίζουν τα εκθέματα;", ["Γιατί είναι εύθραυστα και σπάνε αμέσως", "Γιατί το λίπος από τα χέρια αφήνει σημάδια", "Γιατί έχουν σκόνη", "Γιατί υπάρχει συναγερμός"], 1, "το λίπος από τα χέρια μας αφήνει σημάδια"),
  Q("Ποιο είναι το αγαπημένο της έκθεμα;", ["Ένα διάσημο άγαλμα θεού", "Ένα χρυσό κόσμημα", "Ένα μικρό επιτύμβιο ανάγλυφο με ένα κορίτσι και ένα περιστέρι", "Ένα αγγείο με ζωγραφιές"], 2, "Ένα μικρό επιτύμβιο ανάγλυφο, με ένα κορίτσι που κρατάει ένα περιστέρι"),
 ],
 "gloss": {"φύλακα αρχαιοτήτων": "φύλακας αρχαιοτήτων — antiquities guard", "ανασκαφές": "ανασκαφή — excavation", "προσωρινό": "προσωρινός — temporary", "εκθέματα": "έκθεμα — exhibit", "κακία": "κακία — malice", "χαϊδέψεις": "χαϊδεύω — to stroke", "λίπος": "λίπος — oil, grease", "επιτύμβιο ανάγλυφο": "επιτύμβιο ανάγλυφο — funerary relief", "περιστέρι": "περιστέρι — dove, pigeon", "καλημερίζω": "καλημερίζω — to say good morning to"},
})
ITEMS.append({
 "id": "l84-rep-dadia", "title": "Οι γύπες της Δαδιάς", "title_en": "The vultures of Dadia", "type": "report", "level": "B2",
 "context_el": "Σε μια εκπομπή για τη φύση, ένας δημοσιογράφος μιλά από το δάσος της Δαδιάς, στον Έβρο.",
 "script": [
  L("Δημοσιογράφος", "m", "Βρισκόμαστε στο Εθνικό Πάρκο Δάσους Δαδιάς, στον νομό Έβρου, ένα από τα σημαντικότερα καταφύγια αρπακτικών πουλιών στην Ευρώπη. Εδώ έχουν καταγραφεί τριάντα έξι από τα τριάντα οχτώ είδη αρπακτικών που ζουν στην ήπειρό μας.", "We are in the Dadia Forest National Park, in the prefecture of Evros, one of the most important refuges for birds of prey in Europe. Thirty-six of the thirty-eight species of raptors that live on our continent have been recorded here."),
  L("Δημοσιογράφος", "m", "Το μεγάλο αστέρι της περιοχής είναι ο μαύρος γύπας, ένα τεράστιο πουλί με άνοιγμα φτερών σχεδόν τρία μέτρα. Η Δαδιά φιλοξενεί τη μοναδική αποικία μαύρων γυπών σε όλα τα Βαλκάνια. Πριν από μερικές δεκαετίες είχαν απομείνει ελάχιστα ζευγάρια, όμως χάρη στην προστασία ο πληθυσμός τους αυξάνεται.", "The great star of the area is the black vulture, a huge bird with a wingspan of almost three metres. Dadia is home to the only colony of black vultures in the whole of the Balkans. A few decades ago only a handful of pairs were left, but thanks to protection their population is growing."),
  L("Δημοσιογράφος", "m", "Οι γύπες τρέφονται με νεκρά ζώα, γι’ αυτό λειτουργεί εδώ ένας ειδικός χώρος τροφοδοσίας. Οι επισκέπτες μπορούν να τους παρατηρήσουν από ένα παρατηρητήριο, χωρίς να τους ενοχλούν. Ο μεγαλύτερος κίνδυνος για τα πουλιά σήμερα είναι τα δηλητηριασμένα δολώματα που αφήνουν κάποιοι για τους λύκους και τις αλεπούδες.", "Vultures feed on dead animals, so a special feeding site operates here. Visitors can watch them from an observation hide, without disturbing them. The greatest danger to the birds today is the poisoned baits that some people leave out for wolves and foxes."),
 ],
 "questions": [
  Q("Πόσα είδη αρπακτικών έχουν καταγραφεί στη Δαδιά;", ["Δεκαοχτώ", "Τριάντα έξι", "Τριάντα οχτώ", "Εκατό"], 1, "Εδώ έχουν καταγραφεί τριάντα έξι από τα τριάντα οχτώ είδη αρπακτικών"),
  Q("Τι είναι μοναδικό στη Δαδιά;", ["Η μόνη αποικία μαύρων γυπών στα Βαλκάνια", "Το μεγαλύτερο δάσος της Ευρώπης", "Η μόνη λίμνη του Έβρου", "Το παλαιότερο παρατηρητήριο του κόσμου"], 0, "Η Δαδιά φιλοξενεί τη μοναδική αποικία μαύρων γυπών σε όλα τα Βαλκάνια"),
  Q("Ποιος είναι ο μεγαλύτερος κίνδυνος για τα πουλιά σήμερα;", ["Οι επισκέπτες", "Οι πυρκαγιές", "Τα δηλητηριασμένα δολώματα", "Το κυνήγι"], 2, "τα δηλητηριασμένα δολώματα"),
 ],
 "gloss": {"γύπες": "γύπας — vulture", "αρπακτικών": "αρπακτικό — bird of prey", "καταγραφεί": "καταγράφομαι — to be recorded", "άνοιγμα φτερών": "άνοιγμα φτερών — wingspan", "αποικία": "αποικία — colony", "τρέφονται": "τρέφομαι — to feed on", "τροφοδοσίας": "τροφοδοσία — feeding, supply", "παρατηρητήριο": "παρατηρητήριο — observation hide", "δηλητηριασμένα": "δηλητηριασμένος — poisoned", "δολώματα": "δόλωμα — bait"},
})
ITEMS.append({
 "id": "l84-rep-palamidi", "title": "Το Παλαμήδι", "title_en": "The Palamidi fortress", "type": "report", "level": "B2",
 "context_el": "Σε μια ταξιδιωτική εκπομπή, μια δημοσιογράφος παρουσιάζει το κάστρο του Παλαμηδίου, στο Ναύπλιο.",
 "script": [
  L("Δημοσιογράφος", "f", "Πάνω από το Ναύπλιο, σε έναν βράχο ύψους διακοσίων περίπου μέτρων, υψώνεται το Παλαμήδι, ένα από τα πιο εντυπωσιακά κάστρα της Ελλάδας. Το έχτισαν οι Ενετοί στις αρχές του 18ου αιώνα, μέσα σε μόλις τρία χρόνια, για να προστατέψουν την πόλη από τους Οθωμανούς.", "Above Nafplio, on a rock about two hundred metres high, rises Palamidi, one of the most impressive castles in Greece. The Venetians built it at the beginning of the 18th century, in just three years, to protect the town from the Ottomans."),
  L("Δημοσιογράφος", "f", "Για να ανέβει κανείς με τα πόδια, πρέπει να ανέβει μια ατελείωτη πέτρινη σκάλα. Οι ντόπιοι λένε ότι έχει εννιακόσια ενενήντα εννιά σκαλιά. Στην πραγματικότητα είναι λιγότερα, αλλά όποιος τα ανεβαίνει τον Αύγουστο μάλλον δεν θα συμφωνήσει.", "To go up on foot, you have to climb an endless stone staircase. The locals say it has nine hundred and ninety-nine steps. In reality there are fewer, but anyone who climbs them in August probably won't agree."),
  L("Δημοσιογράφος", "f", "Το κάστρο έχει οχτώ προμαχώνες, που φέρουν ονόματα αρχαίων ηρώων και αγίων. Σε ένα από τα κελιά του φυλακίστηκε για ένα διάστημα ο Θεόδωρος Κολοκοτρώνης, μετά την Επανάσταση, όταν κατηγορήθηκε για συνωμοσία. Σήμερα οι επισκέπτες μπορούν να δουν το στενό κελί του και να απολαύσουν από τα τείχη μια μαγευτική θέα στον Αργολικό κόλπο.", "The castle has eight bastions, which bear the names of ancient heroes and saints. In one of its cells Theodoros Kolokotronis was imprisoned for a time, after the Revolution, when he was accused of conspiracy. Today visitors can see his narrow cell and enjoy an enchanting view of the Argolic Gulf from the walls."),
 ],
 "questions": [
  Q("Ποιοι έχτισαν το Παλαμήδι;", ["Οι Οθωμανοί", "Οι Ενετοί", "Οι Βυζαντινοί", "Οι Φράγκοι"], 1, "Το έχτισαν οι Ενετοί στις αρχές του 18ου αιώνα"),
  Q("Τι λένε οι ντόπιοι για τη σκάλα;", ["Ότι είναι επικίνδυνη", "Ότι έχει εννιακόσια ενενήντα εννιά σκαλιά", "Ότι χτίστηκε από τον Κολοκοτρώνη", "Ότι είναι κλειστή τον Αύγουστο"], 1, "Οι ντόπιοι λένε ότι έχει εννιακόσια ενενήντα εννιά σκαλιά"),
  Q("Γιατί φυλακίστηκε ο Κολοκοτρώνης στο Παλαμήδι;", ["Γιατί κατηγορήθηκε για συνωμοσία", "Γιατί πιάστηκε από τους Οθωμανούς", "Γιατί δεν πλήρωσε φόρους", "Γιατί έκλεψε από το κάστρο"], 0, "όταν κατηγορήθηκε για συνωμοσία"),
 ],
 "gloss": {"υψώνεται": "υψώνομαι — to rise, tower", "Ενετοί": "Ενετός — Venetian", "Οθωμανούς": "Οθωμανός — Ottoman", "ατελείωτη": "ατελείωτος — endless", "σκαλιά": "σκαλί — step", "προμαχώνες": "προμαχώνας — bastion", "κελιά": "κελί — cell", "φυλακίστηκε": "φυλακίζομαι — to be imprisoned", "συνωμοσία": "συνωμοσία — conspiracy", "μαγευτική": "μαγευτικός — enchanting"},
})
ITEMS.append({
 "id": "l84-mono-choris-kinito", "title": "Ένας μήνας χωρίς κινητό", "title_en": "A month without a mobile phone", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast, ένας φοιτητής μιλά για ένα πείραμα που έκανε με τον εαυτό του.",
 "script": [
  L("Άγγελος", "m", "Τον περασμένο Φεβρουάριο κλείδωσα το κινητό μου σε ένα συρτάρι για έναν ολόκληρο μήνα. Δεν το έκανα για κάποια πρόκληση στο ίντερνετ. Είχα προσέξει ότι το έπιανα πάνω από εκατό φορές τη μέρα και ότι δεν μπορούσα να διαβάσω ούτε δέκα σελίδες ενός βιβλίου χωρίς να το κοιτάξω.", "Last February I locked my mobile in a drawer for a whole month. I didn't do it for some internet challenge. I had noticed that I picked it up more than a hundred times a day and that I couldn't read even ten pages of a book without looking at it."),
  L("Άγγελος", "m", "Αγόρασα ένα παλιό κινητό με κουμπιά, μόνο για τηλεφωνήματα, και ένα ξυπνητήρι. Οι πρώτες μέρες ήταν δύσκολες. Χανόμουν στην πόλη χωρίς χάρτη, και έπρεπε να ρωτάω τους περαστικούς για τον δρόμο. Οι φίλοι μου θύμωναν, γιατί δεν απαντούσα στα μηνύματα της ομάδας.", "I bought an old phone with buttons, just for calls, and an alarm clock. The first days were difficult. I got lost in the city without a map, and I had to ask passers-by for directions. My friends got annoyed because I didn't answer the group messages."),
  L("Άγγελος", "m", "Μετά τη δεύτερη εβδομάδα, όμως, κάτι άλλαξε. Διάβασα τέσσερα βιβλία, κοιμόμουν καλύτερα και άρχισα να θυμάμαι τηλέφωνα απ’ έξω. Όταν τελείωσε ο μήνας, ξαναπήρα το κινητό μου, αλλά έσβησα τις περισσότερες εφαρμογές. Και το βράδυ το αφήνω πια στην κουζίνα.", "After the second week, though, something changed. I read four books, I slept better and I started remembering phone numbers by heart. When the month was over I took my phone back, but I deleted most of the apps. And at night I now leave it in the kitchen."),
 ],
 "questions": [
  Q("Γιατί αποφάσισε ο Άγγελος να κλειδώσει το κινητό του;", ["Για μια πρόκληση στο ίντερνετ", "Γιατί είχε χαλάσει", "Γιατί το έπιανε πάνω από εκατό φορές τη μέρα", "Γιατί του το ζήτησαν οι γονείς του"], 2, "το έπιανα πάνω από εκατό φορές τη μέρα"),
  Q("Τι πρόβλημα είχε τις πρώτες μέρες;", ["Δεν μπορούσε να κοιμηθεί", "Χανόταν στην πόλη χωρίς χάρτη", "Δεν ξυπνούσε για τα μαθήματα", "Ξόδευε πολλά χρήματα"], 1, "Χανόμουν στην πόλη χωρίς χάρτη"),
  Q("Τι έκανε όταν τελείωσε ο μήνας;", ["Αγόρασε καινούργιο κινητό", "Κράτησε το παλιό κινητό με κουμπιά", "Ξαναπήρε το κινητό του, αλλά έσβησε τις περισσότερες εφαρμογές", "Συνέχισε για άλλον έναν μήνα"], 2, "ξαναπήρα το κινητό μου, αλλά έσβησα τις περισσότερες εφαρμογές"),
 ],
 "gloss": {"κλείδωσα": "κλειδώνω — to lock", "συρτάρι": "συρτάρι — drawer", "πρόκληση": "πρόκληση — challenge", "κουμπιά": "κουμπί — button", "περαστικούς": "περαστικός — passer-by", "θύμωναν": "θυμώνω — to get angry", "απ’ έξω": "απ’ έξω — by heart", "εφαρμογές": "εφαρμογή — app"},
})
ITEMS.append({
 "id": "l84-mono-panigyri", "title": "Ο πρώτος μου χορός στο πανηγύρι", "title_en": "My first dance at the village festival", "type": "monologue", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, μια ακροάτρια που μεγάλωσε στη Γερμανία θυμάται το πρώτο της πανηγύρι στην Ελλάδα.",
 "script": [
  L("Κατερίνα", "f", "Μεγάλωσα στη Στουτγκάρδη, από γονείς Ηπειρώτες. Στα δεκαπέντε μου ήρθα για πρώτη φορά το καλοκαίρι στο χωριό του πατέρα μου, κοντά στα Γιάννενα, και έπεσα πάνω στο πανηγύρι του Δεκαπενταύγουστου. Ήμουν πεπεισμένη ότι θα βαριόμουν τρομερά.", "I grew up in Stuttgart, with parents from Epirus. At fifteen I came for the first time in summer to my father's village, near Ioannina, and I happened upon the festival of the fifteenth of August. I was convinced I'd be terribly bored."),
  L("Κατερίνα", "f", "Η πλατεία ήταν γεμάτη τραπέζια, και κάτω από τον πλάτανο έπαιζε μια κομπανία με κλαρίνο, βιολί και λαούτο. Γύρω στα μεσάνυχτα άρχισε ένας αργός χορός, και μια ηλικιωμένη θεία με τράβηξε από το χέρι μέσα στον κύκλο. Δεν ήξερα τα βήματα και πατούσα όλους στα πόδια.", "The square was full of tables, and under the plane tree a band was playing clarinet, violin and lute. Around midnight a slow dance began, and an elderly aunt pulled me by the hand into the circle. I didn't know the steps and I trod on everyone's feet."),
  L("Κατερίνα", "f", "Κανείς όμως δεν γέλασε. Η θεία μού ψιθύριζε τα βήματα στο αυτί: «δεξί, δεξί, πίσω». Χορέψαμε ως τις πέντε το πρωί. Εκείνο το βράδυ κατάλαβα ότι ο χορός εδώ δεν είναι επίδειξη, αλλά ένας τρόπος να ανήκεις κάπου. Από τότε δεν έχω χάσει ούτε ένα πανηγύρι.", "But nobody laughed. My aunt whispered the steps in my ear: 'right, right, back.' We danced until five in the morning. That night I understood that dancing here isn't a show, but a way of belonging somewhere. Since then I haven't missed a single festival."),
 ],
 "questions": [
  Q("Τι περίμενε η Κατερίνα από το πανηγύρι;", ["Ότι θα διασκέδαζε πολύ", "Ότι θα βαριόταν τρομερά", "Ότι θα γνώριζε νέους φίλους", "Ότι θα χόρευε όλη τη νύχτα"], 1, "Ήμουν πεπεισμένη ότι θα βαριόμουν τρομερά"),
  Q("Ποιος την έβαλε στον χορό;", ["Ο πατέρας της", "Ένας νεαρός του χωριού", "Μια ηλικιωμένη θεία", "Ο κλαρινετίστας"], 2, "μια ηλικιωμένη θεία με τράβηξε από το χέρι μέσα στον κύκλο"),
  Q("Τι κατάλαβε εκείνο το βράδυ;", ["Ότι ο χορός είναι ένας τρόπος να ανήκεις κάπου", "Ότι πρέπει να μάθει χορό σε σχολή", "Ότι προτιμά τη Γερμανία", "Ότι ο χορός είναι επίδειξη"], 0, "ένας τρόπος να ανήκεις κάπου"),
 ],
 "gloss": {"πανηγύρι": "πανηγύρι — village festival (for a saint's day)", "Ηπειρώτες": "Ηπειρώτης — person from Epirus", "Δεκαπενταύγουστου": "Δεκαπενταύγουστος — the fifteenth of August (Dormition)", "πεπεισμένη": "πεπεισμένος — convinced", "κομπανία": "κομπανία — (folk) band", "λαούτο": "λαούτο — lute", "κύκλο": "κύκλος — circle", "ψιθύριζε": "ψιθυρίζω — to whisper", "επίδειξη": "επίδειξη — show, display"},
})
ITEMS.append({
 "id": "l84-c1-spasmena-parathyra", "title": "Η θεωρία των σπασμένων παραθύρων", "title_en": "The broken windows theory", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την πόλη και την κοινωνία, μια δημοσιογράφος συζητά με έναν εγκληματολόγο.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Ραφαηλίδη, τι υποστηρίζει η περίφημη «θεωρία των σπασμένων παραθύρων»;", "Mr Rafailidis, what does the famous 'broken windows theory' claim?"),
  L("Εγκληματολόγος", "m", "Τη διατύπωσαν δύο αμερικανοί ερευνητές σε ένα άρθρο του 1982. Η βασική ιδέα είναι ότι τα μικρά σημάδια εγκατάλειψης, ένα σπασμένο τζάμι, γκράφιτι, σκουπίδια στον δρόμο, στέλνουν ένα μήνυμα: εδώ κανείς δεν ενδιαφέρεται. Και αυτό το μήνυμα, κατά τη θεωρία, ενθαρρύνει σταδιακά πιο σοβαρές παραβάσεις.", "Two American researchers formulated it in an article in 1982. The basic idea is that small signs of neglect, a broken pane, graffiti, rubbish in the street, send a message: nobody cares here. And this message, according to the theory, gradually encourages more serious offences."),
  L("Δημοσιογράφος", "f", "Υπάρχουν πειραματικά δεδομένα που τη στηρίζουν;", "Is there experimental evidence to support it?"),
  L("Εγκληματολόγος", "m", "Ορισμένα, ναι. Σε μια ολλανδική έρευνα, οι ερευνητές κρέμασαν διαφημιστικά φυλλάδια στα τιμόνια ποδηλάτων σε ένα πάρκινγκ. Όταν ο τοίχος δίπλα ήταν καθαρός, το ένα τρίτο περίπου των ποδηλατών πέταξε το φυλλάδιο κάτω. Όταν ο τοίχος ήταν γεμάτος γκράφιτι, το ποσοστό σχεδόν διπλασιάστηκε. Η αταξία, φαίνεται, είναι μεταδοτική.", "Some, yes. In a Dutch study, the researchers hung advertising flyers on the handlebars of bicycles in a car park. When the wall next to them was clean, about a third of the cyclists threw the flyer on the ground. When the wall was covered in graffiti, the rate almost doubled. Disorder, it seems, is contagious."),
  L("Δημοσιογράφος", "f", "Η Νέα Υόρκη όμως δεν εφάρμοσε τη θεωρία τη δεκαετία του 1990, με μεγάλη επιτυχία;", "But didn't New York apply the theory in the 1990s, with great success?"),
  L("Εγκληματολόγος", "m", "Εκεί αρχίζουν οι διαφωνίες. Η αστυνομία της πόλης κυνήγησε αυστηρά τις μικροπαραβάσεις, και η εγκληματικότητα μειώθηκε θεαματικά. Όμως μειώθηκε σχεδόν το ίδιο και σε πόλεις που δεν εφάρμοσαν τέτοιες πολιτικές. Επιπλέον, η αυστηρή αστυνόμευση έπληξε δυσανάλογα τις φτωχές γειτονιές. Το πιο χρήσιμο δίδαγμα, κατά τη γνώμη μου, δεν αφορά την αστυνομία, αλλά τους δήμους: ένα καθαρό, φροντισμένο πάρκο είναι ήδη μια μορφή πρόληψης.", "That's where the disagreements begin. The city police cracked down hard on minor offences, and crime fell spectacularly. But it fell almost as much in cities that did not apply such policies. Moreover, strict policing hit poor neighbourhoods disproportionately. The most useful lesson, in my view, is not about the police but about municipalities: a clean, well-kept park is already a form of prevention."),
 ],
 "questions": [
  Q("Ποια είναι η βασική ιδέα της θεωρίας;", ["Ότι οι φτωχές γειτονιές έχουν περισσότερη εγκληματικότητα", "Ότι τα μικρά σημάδια εγκατάλειψης ενθαρρύνουν πιο σοβαρές παραβάσεις", "Ότι τα γκράφιτι είναι τέχνη", "Ότι η αστυνομία πρέπει να είναι αυστηρή με όλους"], 1, "τα μικρά σημάδια εγκατάλειψης"),
  Q("Τι έδειξε η ολλανδική έρευνα;", ["Ότι οι ποδηλάτες δεν πετούν ποτέ σκουπίδια", "Ότι με γκράφιτι στον τοίχο σχεδόν διπλασιάστηκε το ποσοστό όσων πέταξαν το φυλλάδιο", "Ότι τα φυλλάδια ενοχλούν τους ποδηλάτες", "Ότι οι καθαροί τοίχοι προσελκύουν γκράφιτι"], 1, "το ποσοστό σχεδόν διπλασιάστηκε"),
  Q("Γιατί αμφισβητείται η επιτυχία της Νέας Υόρκης;", ["Γιατί η εγκληματικότητα αυξήθηκε", "Γιατί μειώθηκε σχεδόν το ίδιο και σε πόλεις που δεν εφάρμοσαν τέτοιες πολιτικές", "Γιατί η αστυνομία δεν εφάρμοσε ποτέ τη θεωρία", "Γιατί τα στοιχεία χάθηκαν"], 1, "μειώθηκε σχεδόν το ίδιο και σε πόλεις που δεν εφάρμοσαν τέτοιες πολιτικές"),
 ],
 "gloss": {"εγκληματολόγο": "εγκληματολόγος — criminologist", "διατύπωσαν": "διατυπώνω — to formulate", "εγκατάλειψης": "εγκατάλειψη — neglect, abandonment", "τζάμι": "τζάμι — windowpane", "παραβάσεις": "παράβαση — offence", "φυλλάδια": "φυλλάδιο — flyer, leaflet", "τιμόνια": "τιμόνι — handlebars", "αταξία": "αταξία — disorder", "μεταδοτική": "μεταδοτικός — contagious", "δυσανάλογα": "δυσανάλογα — disproportionately", "πρόληψης": "πρόληψη — prevention"},
})
ITEMS.append({
 "id": "l84-c1-psychologia-doron", "title": "Η ψυχολογία των δώρων", "title_en": "The psychology of gifts", "type": "monologue", "level": "C1",
 "context_el": "Σε ένα podcast λίγο πριν από τις γιορτές, μια κοινωνική ψυχολόγος μιλά για το τι κάνει ένα δώρο πετυχημένο.",
 "script": [
  L("Ψυχολόγος", "f", "Κάθε Δεκέμβριο ξοδεύουμε χρόνο, χρήματα και άγχος για να βρούμε το «τέλειο» δώρο. Κι όμως, οι έρευνες δείχνουν ότι αυτοί που κάνουν τα δώρα και αυτοί που τα δέχονται δεν σκέφτονται με τον ίδιο τρόπο. Ένας αμερικανός οικονομολόγος υπολόγισε κάποτε ότι οι παραλήπτες αποτιμούν τα δώρα τους έως και ένα τρίτο λιγότερο από όσο κόστισαν.", "Every December we spend time, money and stress trying to find the 'perfect' gift. And yet research shows that those who give gifts and those who receive them don't think in the same way. An American economist once calculated that recipients value their gifts up to a third less than they cost."),
  L("Ψυχολόγος", "f", "Αυτοί που κάνουν τα δώρα θέλουν συνήθως να εκπλήξουν. Αποφεύγουν ό,τι τους έχει ζητηθεί, γιατί τους φαίνεται ανέμπνευστο. Οι παραλήπτες, αντίθετα, εκτιμούν περισσότερο ακριβώς αυτό που ζήτησαν, γιατί δείχνει ότι κάποιος τους άκουσε. Επίσης, όσοι κάνουν δώρα υπερεκτιμούν τη σημασία της τιμής· για τον παραλήπτη, η τιμή μετράει πολύ λιγότερο απ’ ό,τι νομίζουμε.", "Givers usually want to surprise. They avoid what they've been asked for, because it seems uninspired to them. Recipients, on the other hand, appreciate most precisely what they asked for, because it shows that someone listened to them. Givers also overestimate the importance of price; for the recipient, price matters much less than we think."),
  L("Ψυχολόγος", "f", "Υπάρχει μία κατηγορία δώρων που φαίνεται να κερδίζει σχεδόν πάντα: οι εμπειρίες. Ένα εισιτήριο για μια συναυλία, ένα μάθημα μαγειρικής, μια εκδρομή, ιδίως όταν τα μοιραζόμαστε με τον παραλήπτη, φέρνουν τους ανθρώπους πιο κοντά απ’ ό,τι ένα αντικείμενο. Τα πράγματα παλιώνουν· οι αναμνήσεις, αντίθετα, συχνά γίνονται πιο γλυκές με τον χρόνο.", "There is one category of gift that seems to win almost every time: experiences. A ticket to a concert, a cookery class, an outing, especially when we share them with the recipient, bring people closer than an object does. Things get old; memories, by contrast, often grow sweeter with time."),
 ],
 "questions": [
  Q("Τι υπολόγισε ο αμερικανός οικονομολόγος;", ["Ότι ξοδεύουμε περισσότερα κάθε χρόνο", "Ότι οι παραλήπτες αποτιμούν τα δώρα έως και ένα τρίτο λιγότερο από όσο κόστισαν", "Ότι τα ακριβά δώρα είναι πιο πετυχημένα", "Ότι οι άνθρωποι προτιμούν χρήματα"], 1, "οι παραλήπτες αποτιμούν τα δώρα τους έως και ένα τρίτο λιγότερο από όσο κόστισαν"),
  Q("Τι εκτιμούν περισσότερο οι παραλήπτες;", ["Τα ακριβά δώρα", "Τις εκπλήξεις", "Αυτό που ζήτησαν", "Τα χειροποίητα δώρα"], 2, "εκτιμούν περισσότερο ακριβώς αυτό που ζήτησαν"),
  Q("Γιατί οι εμπειρίες είναι συχνά καλύτερα δώρα;", ["Γιατί είναι φθηνότερες", "Γιατί φέρνουν τους ανθρώπους πιο κοντά και οι αναμνήσεις γλυκαίνουν με τον χρόνο", "Γιατί δεν χρειάζονται περιτύλιγμα", "Γιατί μπορούν να ανταλλαχθούν"], 1, "φέρνουν τους ανθρώπους πιο κοντά απ’ ό,τι ένα αντικείμενο"),
 ],
 "gloss": {"παραλήπτες": "παραλήπτης — recipient", "αποτιμούν": "αποτιμώ — to value, appraise", "εκπλήξουν": "εκπλήσσω — to surprise", "ανέμπνευστο": "ανέμπνευστος — uninspired", "υπερεκτιμούν": "υπερεκτιμώ — to overestimate", "κατηγορία": "κατηγορία — category", "παλιώνουν": "παλιώνω — to get old"},
})

rnd = random.Random(84)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-84.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
