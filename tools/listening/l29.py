# Source for library/listening/listening-29.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l29.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l29-ann-anaklisi", "title": "Ανάκληση προϊόντος", "title_en": "A product recall", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα ενός σούπερ μάρκετ.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί πελάτες, σας ενημερώνουμε ότι, ύστερα από οδηγία του Ενιαίου Φορέα Ελέγχου Τροφίμων, ανακαλείται από την αγορά το τυρί κρέμα σε συσκευασία των διακοσίων γραμμαρίων, με ημερομηνία λήξης δώδεκα Δεκεμβρίου. Σε ορισμένες συσκευασίες εντοπίστηκε βακτήριο που μπορεί να προκαλέσει τροφική δηλητηρίαση.", "Dear customers, we inform you that, following an instruction from the Hellenic Food Authority, the cream cheese in 200-gram packs with a use-by date of 12 December is being recalled from the market. A bacterium that can cause food poisoning was found in some packs."),
  L("Εκφωνητής", "m", "Αν έχετε αγοράσει το συγκεκριμένο προϊόν, παρακαλούμε να μην το καταναλώσετε. Μπορείτε να το επιστρέψετε στο ταμείο εξυπηρέτησης πελατών και θα σας επιστραφούν τα χρήματα, ακόμη κι αν δεν έχετε την απόδειξη. Η επιστροφή μπορεί να γίνει σε οποιοδήποτε κατάστημα της αλυσίδας μας.", "If you have bought this product, please do not eat it. You can return it to the customer service desk and you will get your money back, even if you don't have the receipt. The return can be made at any store in our chain."),
  L("Εκφωνητής", "m", "Οι υπόλοιπες συσκευασίες της ίδιας εταιρείας, καθώς και το ίδιο τυρί με άλλη ημερομηνία λήξης, είναι απολύτως ασφαλή. Ζητούμε συγγνώμη για την ταλαιπωρία.", "The company's other packs, as well as the same cheese with a different use-by date, are completely safe. We apologise for the inconvenience."),
 ],
 "questions": [
  Q("Γιατί ανακαλείται το τυρί;", ["Γιατί είχε λάθος τιμή", "Γιατί σε ορισμένες συσκευασίες βρέθηκε επικίνδυνο βακτήριο", "Γιατί είχε λήξει", "Γιατί η συσκευασία ήταν σπασμένη"], 1, "Σε ορισμένες συσκευασίες εντοπίστηκε βακτήριο που μπορεί να προκαλέσει τροφική δηλητηρίαση"),
  Q("Τι ισχύει για την επιστροφή;", ["Χρειάζεται απαραίτητα απόδειξη", "Γίνεται χωρίς απόδειξη, σε οποιοδήποτε κατάστημα της αλυσίδας", "Γίνεται μόνο στο κατάστημα της αγοράς", "Δεν επιστρέφονται χρήματα"], 1, "ακόμη κι αν δεν έχετε την απόδειξη … σε οποιοδήποτε κατάστημα της αλυσίδας μας"),
  Q("Ποια προϊόντα είναι ασφαλή;", ["Κανένα προϊόν της εταιρείας", "Το ίδιο τυρί με άλλη ημερομηνία λήξης", "Μόνο τα τυριά των διακοσίων γραμμαρίων", "Μόνο τα γαλακτοκομικά"], 1, "το ίδιο τυρί με άλλη ημερομηνία λήξης, είναι απολύτως ασφαλή"),
 ],
 "gloss": {"ανακαλείται": "ανακαλώ — to recall", "Φορέα": "φορέας — body, authority", "συσκευασία": "συσκευασία — pack, packaging", "ημερομηνία λήξης": "ημερομηνία λήξης — use-by date", "εντοπίστηκε": "εντοπίζω — to detect, locate", "βακτήριο": "βακτήριο — bacterium", "δηλητηρίαση": "δηλητηρίαση — poisoning", "να μην το καταναλώσετε": "καταναλώνω — to consume", "εξυπηρέτησης πελατών": "εξυπηρέτηση πελατών — customer service", "αλυσίδας": "αλυσίδα — chain", "ταλαιπωρία": "ταλαιπωρία — inconvenience"},
})

ITEMS.append({
 "id": "l29-vm-ilektrologos", "title": "Μήνυμα από τον ηλεκτρολόγο", "title_en": "A message from the electrician", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τον ηλεκτρολόγο που ήρθε να δει το σπίτι σας.",
 "script": [
  L("Ηλεκτρολόγος", "m", "Καλησπέρα, κυρία Ραφαηλίδου, ο Θανάσης είμαι, ο ηλεκτρολόγος. Σας τηλεφωνώ για την προσφορά που μου ζητήσατε για την ανακαίνιση της κουζίνας. Το κόστος για τις καινούργιες πρίζες και τον φωτισμό θα είναι γύρω στα τετρακόσια ευρώ, μαζί με τα υλικά.", "Good evening, Mrs Rafailidou, it's Thanasis, the electrician. I'm calling about the quote you asked me for the kitchen renovation. The cost of the new sockets and the lighting will be about four hundred euros, including materials."),
  L("Ηλεκτρολόγος", "m", "Πρέπει όμως να σας πω κάτι πιο σοβαρό. Όταν άνοιξα τον πίνακα, είδα ότι δεν έχετε διακόπτη διαρροής, το λεγόμενο «ρελέ». Είναι ο διακόπτης που κόβει αμέσως το ρεύμα αν κάποιος πάθει ηλεκτροπληξία. Σε ένα σπίτι με μικρά παιδιά, αυτό δεν πρέπει να περιμένει.", "But I have to tell you something more serious. When I opened the fuse box, I saw that you don't have a residual-current device, the so-called 'relay'. It's the switch that cuts the power immediately if someone gets an electric shock. In a house with small children, that shouldn't wait."),
  L("Ηλεκτρολόγος", "m", "Η τοποθέτηση κοστίζει περίπου ογδόντα ευρώ και κρατάει μία ώρα. Θα μπορούσα να έρθω ακόμη και αύριο το πρωί. Πάρτε με όταν μπορέσετε, ακόμη και αργά το βράδυ.", "Fitting it costs about eighty euros and takes an hour. I could come as early as tomorrow morning. Call me when you can, even late in the evening."),
 ],
 "questions": [
  Q("Για ποια δουλειά ζήτησε προσφορά η κυρία Ραφαηλίδου;", ["Για το μπάνιο", "Για την ανακαίνιση της κουζίνας", "Για τον κλιματισμό", "Για την πρόσοψη του σπιτιού"], 1, "την προσφορά που μου ζητήσατε για την ανακαίνιση της κουζίνας"),
  Q("Τι σοβαρό πρόβλημα βρήκε ο ηλεκτρολόγος;", ["Τα καλώδια είχαν καεί", "Δεν υπάρχει διακόπτης διαρροής", "Ο πίνακας ήταν βρεγμένος", "Το ρεύμα κόβεται συχνά"], 1, "δεν έχετε διακόπτη διαρροής"),
  Q("Γιατί, κατά τον ηλεκτρολόγο, η δουλειά δεν πρέπει να περιμένει;", ["Γιατί θα αυξηθούν οι τιμές", "Γιατί στο σπίτι μένουν μικρά παιδιά", "Γιατί φεύγει για διακοπές", "Γιατί το απαιτεί ο νόμος από αύριο"], 1, "Σε ένα σπίτι με μικρά παιδιά, αυτό δεν πρέπει να περιμένει"),
 ],
 "gloss": {"ηλεκτρολόγο": "ηλεκτρολόγος — electrician", "προσφορά": "προσφορά — quote, offer", "ανακαίνιση": "ανακαίνιση — renovation", "πρίζες": "πρίζα — socket", "φωτισμό": "φωτισμός — lighting", "υλικά": "υλικό — material", "πίνακα": "(ηλεκτρικός) πίνακας — fuse box", "διακόπτη διαρροής": "διακόπτης διαρροής — residual-current device (RCD)", "ηλεκτροπληξία": "ηλεκτροπληξία — electric shock", "τοποθέτηση": "τοποθέτηση — fitting, installation"},
})

ITEMS.append({
 "id": "l29-dia-afm", "title": "Στην εφορία", "title_en": "At the tax office", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε μια εφορία, όπου ένας ξένος ζητά αριθμό φορολογικού μητρώου.",
 "script": [
  L("Πολίτης", "m", "Καλημέρα. Είμαι Ιταλός, μετακόμισα στην Ελλάδα για δουλειά και μου είπαν ότι χρειάζομαι ΑΦΜ. Τι ακριβώς είναι και πώς τον βγάζω;", "Good morning. I'm Italian, I moved to Greece for work and I was told I need a tax number. What exactly is it and how do I get it?"),
  L("Υπάλληλος", "f", "Ο ΑΦΜ είναι ο αριθμός φορολογικού μητρώου. Θα τον χρειαστείτε σχεδόν για τα πάντα: για να σας πληρώσει ο εργοδότης σας, για να νοικιάσετε σπίτι, για να ανοίξετε λογαριασμό στην τράπεζα ή για να συνδέσετε ρεύμα. Φέρατε το διαβατήριο ή την ταυτότητά σας;", "The tax number is your tax registration number. You'll need it for almost everything: for your employer to pay you, to rent a flat, to open a bank account or to get the electricity connected. Did you bring your passport or identity card?"),
  L("Πολίτης", "m", "Ναι, την ιταλική μου ταυτότητα. Έχω και το συμφωνητικό του διαμερίσματος.", "Yes, my Italian identity card. I also have the lease for the flat."),
  L("Υπάλληλος", "f", "Τέλεια, το συμφωνητικό αποδεικνύει τη διεύθυνσή σας. Ως πολίτης της Ευρωπαϊκής Ένωσης δεν χρειάζεστε άδεια διαμονής για τον ΑΦΜ. Θα συμπληρώσουμε μαζί μια αίτηση και θα τον έχετε σε δέκα λεπτά. Μετά, σας συμβουλεύω να ζητήσετε και κωδικούς για την ηλεκτρονική πλατφόρμα, ώστε να μη χρειάζεται να έρχεστε εδώ για κάθε βεβαίωση.", "Great, the lease proves your address. As an EU citizen you don't need a residence permit for the tax number. We'll fill in an application together and you'll have it in ten minutes. Afterwards, I'd advise you to also ask for passwords for the online platform, so you don't have to come here for every certificate."),
  L("Πολίτης", "m", "Δέκα λεπτά; Στην Ιταλία μού είχαν πει να κάνω υπομονή με τη γραφειοκρατία!", "Ten minutes? In Italy they'd told me to be patient with the bureaucracy!"),
 ],
 "questions": [
  Q("Για ποιο από τα παρακάτω, σύμφωνα με την υπάλληλο, χρειάζεται ο ΑΦΜ;", ["Για να βγάλει δίπλωμα οδήγησης", "Για να νοικιάσει σπίτι", "Για να ταξιδέψει στο εξωτερικό", "Για να γραφτεί σε γυμναστήριο"], 1, "για να νοικιάσετε σπίτι"),
  Q("Τι αποδεικνύει το συμφωνητικό του διαμερίσματος;", ["Την ιθαγένειά του", "Τη διεύθυνσή του", "Τον μισθό του", "Την ηλικία του"], 1, "το συμφωνητικό αποδεικνύει τη διεύθυνσή σας"),
  Q("Γιατί η υπάλληλος τον συμβουλεύει να ζητήσει κωδικούς;", ["Για να πληρώνει λιγότερους φόρους", "Για να μη χρειάζεται να έρχεται στην εφορία για κάθε βεβαίωση", "Για να βρει δουλειά", "Γιατί είναι υποχρεωτικό"], 1, "ώστε να μη χρειάζεται να έρχεστε εδώ για κάθε βεβαίωση"),
 ],
 "gloss": {"εφορία": "εφορία — tax office", "φορολογικού μητρώου": "φορολογικό μητρώο — tax register", "ΑΦΜ": "ΑΦΜ (αριθμός φορολογικού μητρώου) — tax number", "εργοδότης": "εργοδότης — employer", "να συνδέσετε": "συνδέω — to connect", "συμφωνητικό": "συμφωνητικό — agreement, lease", "αποδεικνύει": "αποδεικνύω — to prove", "άδεια διαμονής": "άδεια διαμονής — residence permit", "πλατφόρμα": "πλατφόρμα — platform", "βεβαίωση": "βεβαίωση — certificate", "γραφειοκρατία": "γραφειοκρατία — bureaucracy"},
})

ITEMS.append({
 "id": "l29-dia-koinochrista", "title": "Τα κοινόχρηστα", "title_en": "The building's shared costs", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο ανάμεσα σε δύο γείτονες σε μια πολυκατοικία.",
 "script": [
  L("Γειτόνισσα", "f", "Καλημέρα, κύριε Σωτήρη. Είδατε το χαρτί με τα κοινόχρηστα στην είσοδο; Φέτος τον Ιανουάριο πληρώνουμε σχεδόν διπλάσια από πέρσι!", "Good morning, Mr Sotiris. Did you see the notice with the shared costs in the entrance? This January we're paying almost double last year!"),
  L("Γείτονας", "m", "Το είδα, κυρία Λένα. Ο διαχειριστής λέει ότι φταίει κυρίως το πετρέλαιο θέρμανσης, που ακρίβυνε πολύ. Και φέτος ο καυστήρας δούλευε πιο πολλές ώρες, γιατί κάποιοι ζήτησαν να ανάβει και το απόγευμα.", "I saw it, Mrs Lena. The building manager says it's mainly the heating oil, which has become much more expensive. And this year the boiler ran for more hours, because some people asked for it to come on in the afternoon too."),
  L("Γειτόνισσα", "f", "Εγώ όμως λείπω όλη μέρα στη δουλειά! Δεν είναι δίκαιο να πληρώνω για ζέστη που δεν χρησιμοποιώ.", "But I'm out at work all day! It's not fair for me to pay for heat I don't use."),
  L("Γείτονας", "m", "Έχετε δίκιο. Γι' αυτό στη γενική συνέλευση τον Μάρτιο θα προτείνω να βάλουμε θερμιδομετρητές σε κάθε διαμέρισμα. Έτσι ο καθένας θα πληρώνει ανάλογα με την κατανάλωσή του. Το κόστος της εγκατάστασης θα αποσβεστεί σε δύο με τρία χρόνια.", "You're right. That's why at the general meeting in March I'll propose that we put heat meters in every flat. That way everyone will pay according to their consumption. The cost of installation will pay for itself in two to three years."),
  L("Γειτόνισσα", "f", "Θα σας υποστηρίξω. Και ας ελέγξουμε και τα παράθυρα της σκάλας· το χειμώνα μένουν συνέχεια ανοιχτά!", "I'll support you. And let's check the stairwell windows too; in winter they're always left open!"),
 ],
 "questions": [
  Q("Γιατί, σύμφωνα με τον διαχειριστή, αυξήθηκαν τα κοινόχρηστα;", ["Λόγω επισκευής του ανελκυστήρα", "Κυρίως λόγω του ακριβότερου πετρελαίου θέρμανσης", "Γιατί προσλήφθηκε καθαρίστρια", "Λόγω νέων φόρων"], 1, "φταίει κυρίως το πετρέλαιο θέρμανσης, που ακρίβυνε πολύ"),
  Q("Γιατί διαμαρτύρεται η κυρία Λένα;", ["Γιατί δεν ζεσταίνεται το σπίτι της", "Γιατί πληρώνει για θέρμανση που δεν χρησιμοποιεί", "Γιατί δεν την ενημέρωσαν", "Γιατί ο καυστήρας κάνει θόρυβο"], 1, "Δεν είναι δίκαιο να πληρώνω για ζέστη που δεν χρησιμοποιώ"),
  Q("Τι θα προτείνει ο κύριος Σωτήρης στη συνέλευση;", ["Να κλείσει ο καυστήρας", "Να μπουν θερμιδομετρητές σε κάθε διαμέρισμα", "Να αλλάξει διαχειριστής", "Να μπει φυσικό αέριο"], 1, "θα προτείνω να βάλουμε θερμιδομετρητές σε κάθε διαμέρισμα"),
 ],
 "gloss": {"κοινόχρηστα": "κοινόχρηστα — shared building costs", "διπλάσια": "διπλάσιος — double", "διαχειριστής": "διαχειριστής — building manager", "πετρέλαιο θέρμανσης": "πετρέλαιο θέρμανσης — heating oil", "ακρίβυνε": "ακριβαίνω — to become more expensive", "καυστήρας": "καυστήρας — boiler", "δίκαιο": "δίκαιος — fair", "συνέλευση": "συνέλευση — meeting, assembly", "θερμιδομετρητές": "θερμιδομετρητής — heat meter", "κατανάλωσή": "κατανάλωση — consumption", "θα αποσβεστεί": "αποσβένομαι — to pay for itself, be written off"},
})

ITEMS.append({
 "id": "l29-mon-kolymbi", "title": "Κολύμπι στα πενήντα", "title_en": "Swimming at fifty", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλάει σε μια ραδιοφωνική εκπομπή για το πώς έμαθε κολύμπι.",
 "script": [
  L("Αλεξάνδρα", "f", "Μεγάλωσα στη Λάρισα, μακριά από τη θάλασσα, και οι γονείς μου δεν ήξεραν κολύμπι. Έτσι, ούτε εγώ έμαθα ποτέ. Στις διακοπές καθόμουν στην ακτή και έλεγα σε όλους ότι προτιμώ τον ήλιο. Η αλήθεια ήταν ότι ντρεπόμουν και φοβόμουν το νερό.", "I grew up in Larissa, far from the sea, and my parents couldn't swim. So I never learned either. On holiday I sat on the shore and told everyone I preferred the sun. The truth was that I was embarrassed and afraid of the water."),
  L("Αλεξάνδρα", "f", "Πριν από δύο χρόνια, όταν έκλεισα τα πενήντα, η εγγονή μου με ρώτησε γιατί δεν μπαίνω ποτέ στη θάλασσα μαζί της. Εκείνο το βράδυ γράφτηκα σε ένα κολυμβητήριο, σε ένα τμήμα για ενήλικες αρχάριους. Ήμασταν οκτώ, όλοι πάνω από σαράντα, και όλοι με την ίδια ντροπή.", "Two years ago, when I turned fifty, my granddaughter asked me why I never go into the sea with her. That evening I signed up at a swimming pool, in a class for adult beginners. There were eight of us, all over forty, and all with the same embarrassment."),
  L("Αλεξάνδρα", "f", "Τους πρώτους δύο μήνες απλώς μαθαίναμε να βάζουμε το πρόσωπο στο νερό και να αναπνέουμε. Ο προπονητής μας έλεγε ότι οι ενήλικες δεν μαθαίνουν πιο αργά από τα παιδιά, απλώς φοβούνται περισσότερο. Πέρσι το καλοκαίρι κολύμπησα για πρώτη φορά στα βαθιά, με την εγγονή μου δίπλα μου. Ήταν από τις πιο ευτυχισμένες στιγμές της ζωής μου.", "For the first two months we just learned to put our faces in the water and breathe. Our coach told us that adults don't learn more slowly than children, they're just more afraid. Last summer I swam out of my depth for the first time, with my granddaughter beside me. It was one of the happiest moments of my life."),
 ],
 "questions": [
  Q("Γιατί η Αλεξάνδρα δεν έμαθε κολύμπι ως παιδί;", ["Γιατί ήταν άρρωστη", "Γιατί μεγάλωσε μακριά από τη θάλασσα και οι γονείς της δεν ήξεραν κολύμπι", "Γιατί δεν της άρεσε ο ήλιος", "Γιατί δεν υπήρχε κολυμβητήριο στη Λάρισα"], 1, "Μεγάλωσα στη Λάρισα, μακριά από τη θάλασσα, και οι γονείς μου δεν ήξεραν κολύμπι"),
  Q("Τι την έκανε να γραφτεί σε κολυμβητήριο;", ["Μια συμβουλή του γιατρού", "Η ερώτηση της εγγονής της", "Ένα ατύχημα στη θάλασσα", "Μια προσφορά του κολυμβητηρίου"], 1, "η εγγονή μου με ρώτησε γιατί δεν μπαίνω ποτέ στη θάλασσα μαζί της"),
  Q("Τι έλεγε ο προπονητής για τους ενήλικες;", ["Ότι μαθαίνουν πιο αργά από τα παιδιά", "Ότι δεν μαθαίνουν πιο αργά, απλώς φοβούνται περισσότερο", "Ότι πρέπει να κάνουν ιδιαίτερα μαθήματα", "Ότι δεν πρέπει να κολυμπούν στα βαθιά"], 1, "οι ενήλικες δεν μαθαίνουν πιο αργά από τα παιδιά, απλώς φοβούνται περισσότερο"),
 ],
 "gloss": {"ακτή": "ακτή — shore", "ντρεπόμουν": "ντρέπομαι — to be embarrassed, ashamed", "έκλεισα τα πενήντα": "κλείνω τα πενήντα — to turn fifty", "εγγονή": "εγγονή — granddaughter", "κολυμβητήριο": "κολυμβητήριο — swimming pool", "ενήλικες": "ενήλικας — adult", "αρχάριους": "αρχάριος — beginner", "ντροπή": "ντροπή — shame, embarrassment", "να αναπνέουμε": "αναπνέω — to breathe", "προπονητής": "προπονητής — coach", "στα βαθιά": "στα βαθιά — out of one's depth, in deep water"},
})

ITEMS.append({
 "id": "l29-rep-dimitsana", "title": "Η δύναμη του νερού στη Δημητσάνα", "title_en": "Water power in Dimitsana", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από τη Δημητσάνα, ένα ορεινό χωριό της Αρκαδίας.",
 "script": [
  L("Ρεπόρτερ", "f", "Η Δημητσάνα είναι χτισμένη σαν αμφιθέατρο πάνω από το φαράγγι του Λούσιου. Το ποτάμι, με τα άφθονα νερά του, ήταν για αιώνες η μεγαλύτερη περιουσία του τόπου. Εδώ λειτουργούσαν νερόμυλοι, νεροτριβές για τα υφάσματα και εργαστήρια που κατεργάζονταν δέρματα.", "Dimitsana is built like an amphitheatre above the Lousios gorge. The river, with its abundant water, was for centuries the area's greatest asset. Watermills operated here, fulling mills for cloth and workshops that processed hides."),
  L("Ρεπόρτερ", "f", "Η πιο γνωστή, όμως, δραστηριότητα ήταν τα μπαρουτόμυλα. Στα χρόνια της Επανάστασης του 1821, η μπαρούτη που παραγόταν εδώ τροφοδοτούσε τους αγωνιστές, γι' αυτό η Δημητσάνα έμεινε στην ιστορία ως ένα από τα σημαντικότερα κέντρα του Αγώνα.", "The best-known activity, however, was the gunpowder mills. In the years of the 1821 Revolution, the gunpowder produced here supplied the fighters, which is why Dimitsana went down in history as one of the most important centres of the struggle."),
  L("Ρεπόρτερ", "f", "Σήμερα, στο Υπαίθριο Μουσείο Υδροκίνησης, οι επισκέπτες μπορούν να δουν πώς δούλευαν αυτές οι εγκαταστάσεις, που έχουν αποκατασταθεί και λειτουργούν ξανά. Από εδώ ξεκινά και ένα από τα πιο όμορφα μονοπάτια της Πελοποννήσου, που ακολουθεί το ποτάμι και περνά από μοναστήρια χτισμένα στους βράχους.", "Today, at the Open-Air Water Power Museum, visitors can see how these installations worked; they have been restored and operate again. One of the most beautiful paths in the Peloponnese also starts here, following the river and passing monasteries built into the rocks."),
 ],
 "questions": [
  Q("Τι ήταν για αιώνες η μεγαλύτερη περιουσία της Δημητσάνας;", ["Τα δάση", "Το ποτάμι με τα άφθονα νερά του", "Τα πρόβατα", "Τα μοναστήρια"], 1, "Το ποτάμι, με τα άφθονα νερά του, ήταν για αιώνες η μεγαλύτερη περιουσία του τόπου"),
  Q("Γιατί η Δημητσάνα είναι σημαντική για την Επανάσταση του 1821;", ["Γιατί εκεί υπογράφηκε η ανεξαρτησία", "Γιατί η μπαρούτη της τροφοδοτούσε τους αγωνιστές", "Γιατί γεννήθηκε εκεί ο Κολοκοτρώνης", "Γιατί εκεί έγινε η πρώτη μάχη"], 1, "η μπαρούτη που παραγόταν εδώ τροφοδοτούσε τους αγωνιστές"),
  Q("Τι μπορούν να δουν σήμερα οι επισκέπτες στο μουσείο;", ["Όπλα της Επανάστασης", "Πώς δούλευαν οι εγκαταστάσεις, που λειτουργούν ξανά", "Μια συλλογή από υφάσματα", "Ένα αρχαίο θέατρο"], 1, "μπορούν να δουν πώς δούλευαν αυτές οι εγκαταστάσεις, που έχουν αποκατασταθεί και λειτουργούν ξανά"),
 ],
 "gloss": {"αμφιθέατρο": "αμφιθέατρο — amphitheatre", "φαράγγι": "φαράγγι — gorge", "άφθονα": "άφθονος — abundant", "περιουσία": "περιουσία — wealth, asset", "νερόμυλοι": "νερόμυλος — watermill", "νεροτριβές": "νεροτριβή — fulling mill (water-driven cloth washer)", "κατεργάζονταν": "κατεργάζομαι — to process, work", "μπαρουτόμυλα": "μπαρουτόμυλος — gunpowder mill", "τροφοδοτούσε": "τροφοδοτώ — to supply", "αγωνιστές": "αγωνιστής — fighter (in the 1821 war)", "Υδροκίνησης": "υδροκίνηση — water power", "έχουν αποκατασταθεί": "αποκαθίσταμαι — to be restored"},
})

ITEMS.append({
 "id": "l29-rep-dirou", "title": "Τα σπήλαια του Διρού", "title_en": "The Diros caves", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από τα σπήλαια του Διρού, στη Μάνη.",
 "script": [
  L("Ρεπόρτερ", "m", "Η βάρκα προχωρά αθόρυβα σε ένα υπόγειο ποτάμι. Ο βαρκάρης σπρώχνει με ένα κοντάρι, και γύρω μας οι σταλακτίτες κρέμονται από την οροφή σαν κρύσταλλα. Βρισκόμαστε στη Βλυχάδα, ένα από τα σπήλαια του Διρού, στη δυτική ακτή της Μάνης.", "The boat moves silently along an underground river. The boatman pushes with a pole, and around us the stalactites hang from the ceiling like crystals. We are in Vlychada, one of the Diros caves, on the west coast of the Mani."),
  L("Ρεπόρτερ", "m", "Η διαδρομή με τη βάρκα έχει μήκος περίπου ενάμισι χιλιομέτρου, και τελειώνει με ένα σύντομο κομμάτι με τα πόδια. Το νερό, μισό αλμυρό και μισό γλυκό, έχει σε ορισμένα σημεία βάθος πάνω από είκοσι μέτρα. Οι εξερευνητές έχουν χαρτογραφήσει μέχρι σήμερα πολλά χιλιόμετρα διαδρόμων, και πιστεύεται ότι το σπήλαιο συνεχίζεται ακόμη πιο βαθιά.", "The boat route is about one and a half kilometres long, and ends with a short stretch on foot. The water, half salt and half fresh, is more than twenty metres deep in places. Explorers have so far mapped many kilometres of passages, and the cave is believed to go even deeper."),
  L("Ρεπόρτερ", "m", "Λίγα μέτρα πιο πέρα βρίσκεται η Αλεπότρυπα, ένα σπήλαιο που κατοικήθηκε στη Νεολιθική εποχή. Εκεί οι αρχαιολόγοι βρήκαν εργαλεία, αγγεία και ταφές, που μας δείχνουν ότι άνθρωποι ζούσαν σε αυτή την περιοχή πριν από χιλιάδες χρόνια. Συμβουλή για τους επισκέπτες: πάρτε μια ζακέτα, γιατί μέσα η θερμοκρασία μένει σταθερή, γύρω στους δεκαοκτώ βαθμούς, ακόμη και τον Αύγουστο.", "A few metres further on is Alepotrypa, a cave that was inhabited in the Neolithic period. There archaeologists found tools, pots and burials, which show us that people lived in this area thousands of years ago. A tip for visitors: take a cardigan, because inside the temperature stays constant, around eighteen degrees, even in August."),
 ],
 "questions": [
  Q("Πώς κινείται η βάρκα μέσα στο σπήλαιο;", ["Με μηχανή", "Ο βαρκάρης τη σπρώχνει με ένα κοντάρι", "Με κουπιά που κάνουν οι επισκέπτες", "Τη σέρνει ένα σχοινί"], 1, "Ο βαρκάρης σπρώχνει με ένα κοντάρι"),
  Q("Τι βρήκαν οι αρχαιολόγοι στην Αλεπότρυπα;", ["Νομίσματα και κοσμήματα", "Εργαλεία, αγγεία και ταφές", "Ένα αρχαίο ναό", "Οστά δεινοσαύρων"], 1, "βρήκαν εργαλεία, αγγεία και ταφές"),
  Q("Γιατί ο ρεπόρτερ συμβουλεύει τους επισκέπτες να πάρουν ζακέτα;", ["Γιατί φυσάει πολύ", "Γιατί μέσα η θερμοκρασία μένει γύρω στους δεκαοκτώ βαθμούς", "Γιατί βρέχονται στη βάρκα", "Γιατί το σπήλαιο είναι ανοιχτό μόνο τον χειμώνα"], 1, "μέσα η θερμοκρασία μένει σταθερή, γύρω στους δεκαοκτώ βαθμούς"),
 ],
 "gloss": {"σπήλαια": "σπήλαιο — cave", "αθόρυβα": "αθόρυβα — silently", "υπόγειο": "υπόγειος — underground", "βαρκάρης": "βαρκάρης — boatman", "κοντάρι": "κοντάρι — pole", "σταλακτίτες": "σταλακτίτης — stalactite", "οροφή": "οροφή — ceiling, roof", "κρύσταλλα": "κρύσταλλο — crystal", "εξερευνητές": "εξερευνητής — explorer", "χαρτογραφήσει": "χαρτογραφώ — to map", "διαδρόμων": "διάδρομος — passage, corridor", "κατοικήθηκε": "κατοικούμαι — to be inhabited", "αγγεία": "αγγείο — pot, vessel", "ταφές": "ταφή — burial", "ζακέτα": "ζακέτα — cardigan"},
})

ITEMS.append({
 "id": "l29-int-kolymvitis", "title": "Ένας παραολυμπιονίκης", "title_en": "A Paralympic champion", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν κολυμβητή που έχει κερδίσει μετάλλια στους Παραολυμπιακούς Αγώνες.",
 "script": [
  L("Δημοσιογράφος", "f", "Χάσατε το πόδι σας σε τροχαίο στα δεκαεννιά σας. Πώς φτάσατε από εκεί στα Παραολυμπιακά μετάλλια;", "You lost your leg in a road accident at nineteen. How did you get from there to Paralympic medals?"),
  L("Κολυμβητής", "m", "Ο πρώτος χρόνος ήταν πολύ σκοτεινός. Δεν ήθελα να βγαίνω από το σπίτι. Ο φυσικοθεραπευτής μου μού πρότεινε να κολυμπάω για την αποκατάσταση, γιατί στο νερό το σώμα δεν έχει βάρος. Εκεί ένιωσα για πρώτη φορά ξανά ελεύθερος. Ένας προπονητής με είδε να κολυμπάω και με ρώτησε αν θα ήθελα να αγωνιστώ.", "The first year was very dark. I didn't want to leave the house. My physiotherapist suggested I swim for rehabilitation, because in water the body has no weight. There I felt free again for the first time. A coach saw me swimming and asked if I'd like to compete."),
  L("Δημοσιογράφος", "f", "Πώς είναι μια μέρα της προπόνησής σας;", "What's a day of your training like?"),
  L("Κολυμβητής", "m", "Ξυπνάω στις πέντε και μισή, και στις έξι είμαι στην πισίνα. Κολυμπάω περίπου έξι χιλιόμετρα το πρωί και άλλα τόσα το απόγευμα, και ενδιάμεσα κάνω γυμναστήριο. Το πιο δύσκολο, όμως, δεν είναι η κούραση. Είναι ότι για χρόνια οι πισίνες δεν είχαν ράμπες ή ανελκυστήρες, και έπρεπε να ζητάω βοήθεια για τα πιο απλά πράγματα.", "I wake up at half past five, and at six I'm in the pool. I swim about six kilometres in the morning and the same again in the afternoon, and in between I do the gym. The hardest thing, though, isn't the tiredness. It's that for years the pools had no ramps or lifts, and I had to ask for help with the simplest things."),
  L("Κολυμβητής", "m", "Τα πράγματα έχουν βελτιωθεί, αλλά η προσβασιμότητα δεν είναι χάρη· είναι δικαίωμα. Αν τα μετάλλιά μου βοηθήσουν ένα παιδί με αναπηρία να μπει σε μια πισίνα χωρίς να ντρέπεται, αυτό θα είναι η μεγαλύτερη νίκη μου.", "Things have improved, but accessibility isn't a favour; it's a right. If my medals help a child with a disability to get into a pool without feeling embarrassed, that will be my greatest victory."),
 ],
 "questions": [
  Q("Γιατί άρχισε να κολυμπάει;", ["Γιατί ήταν κολυμβητής από παιδί", "Για την αποκατάστασή του, με πρόταση του φυσικοθεραπευτή", "Για να χάσει βάρος", "Γιατί του το ζήτησαν οι φίλοι του"], 1, "Ο φυσικοθεραπευτής μου μού πρότεινε να κολυμπάω για την αποκατάσταση"),
  Q("Τι θεωρεί το πιο δύσκολο ο κολυμβητής;", ["Την κούραση", "Την έλλειψη πρόσβασης στις πισίνες για χρόνια", "Το πρωινό ξύπνημα", "Τα ταξίδια"], 1, "για χρόνια οι πισίνες δεν είχαν ράμπες ή ανελκυστήρες"),
  Q("Ποια θα ήταν, κατά τον ίδιο, η μεγαλύτερη νίκη του;", ["Ένα χρυσό μετάλλιο", "Να βοηθήσει ένα παιδί με αναπηρία να μπει σε πισίνα χωρίς ντροπή", "Ένα παγκόσμιο ρεκόρ", "Να γίνει προπονητής"], 1, "Αν τα μετάλλιά μου βοηθήσουν ένα παιδί με αναπηρία να μπει σε μια πισίνα χωρίς να ντρέπεται"),
 ],
 "gloss": {"κολυμβητή": "κολυμβητής — swimmer", "μετάλλια": "μετάλλιο — medal", "Παραολυμπιακούς Αγώνες": "Παραολυμπιακοί Αγώνες — Paralympic Games", "τροχαίο": "τροχαίο — road accident", "σκοτεινός": "σκοτεινός — dark", "φυσικοθεραπευτής": "φυσικοθεραπευτής — physiotherapist", "αποκατάσταση": "αποκατάσταση — rehabilitation", "να αγωνιστώ": "αγωνίζομαι — to compete", "ράμπες": "ράμπα — ramp", "ανελκυστήρες": "ανελκυστήρας — lift, elevator", "προσβασιμότητα": "προσβασιμότητα — accessibility", "χάρη": "χάρη — favour", "αναπηρία": "αναπηρία — disability"},
})

ITEMS.append({
 "id": "l29-mon-alosi", "title": "Η Άλωση της Πόλης", "title_en": "The Fall of Constantinople", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για την Άλωση της Κωνσταντινούπολης το 1453.",
 "script": [
  L("Ιστορικός", "f", "Την άνοιξη του 1453, η Κωνσταντινούπολη ήταν η σκιά του παλιού της εαυτού. Η άλλοτε κραταιά αυτοκρατορία είχε περιοριστεί σχεδόν στην ίδια την Πόλη και σε λίγα εδάφη στην Πελοπόννησο, ενώ ο πληθυσμός της πρωτεύουσας, που κάποτε ξεπερνούσε τις τετρακόσιες χιλιάδες, είχε πέσει κατά πολλούς υπολογισμούς κάτω από τις πενήντα χιλιάδες.", "In the spring of 1453, Constantinople was a shadow of its former self. The once mighty empire had been reduced almost to the City itself and a few territories in the Peloponnese, while the population of the capital, which had once exceeded four hundred thousand, had fallen by many estimates below fifty thousand."),
  L("Ιστορικός", "f", "Απέναντι σε αυτούς, ο νεαρός σουλτάνος Μωάμεθ ο Β΄ είχε συγκεντρώσει έναν στρατό πολλαπλάσιο και, κυρίως, ένα νέο όπλο: τεράστια κανόνια, ικανά να γκρεμίσουν τα θεοδοσιανά τείχη, που επί χίλια χρόνια θεωρούνταν απόρθητα. Η πολιορκία κράτησε περίπου επτά εβδομάδες, και οι υπερασπιστές, με επικεφαλής τον αυτοκράτορα Κωνσταντίνο ΙΑ΄ Παλαιολόγο, αντιστάθηκαν με μια επιμονή που εντυπωσίασε ακόμη και τους εχθρούς τους.", "Facing them, the young sultan Mehmed II had assembled an army many times larger and, above all, a new weapon: huge cannons, capable of bringing down the Theodosian walls, which for a thousand years had been considered impregnable. The siege lasted about seven weeks, and the defenders, led by the emperor Constantine XI Palaiologos, resisted with a tenacity that impressed even their enemies."),
  L("Ιστορικός", "f", "Στις είκοσι εννιά Μαΐου η Πόλη έπεσε. Ο αυτοκράτορας σκοτώθηκε μαχόμενος, και το σώμα του δεν αναγνωρίστηκε ποτέ με βεβαιότητα. Από αυτή την αβεβαιότητα γεννήθηκε ο θρύλος του «Μαρμαρωμένου Βασιλιά», που κοιμάται σε μια σπηλιά και θα ξυπνήσει κάποτε για να πάρει πίσω την Πόλη.", "On the twenty-ninth of May the City fell. The emperor was killed fighting, and his body was never identified with certainty. From this uncertainty was born the legend of the 'Marble Emperor', who sleeps in a cave and will one day wake to take back the City."),
  L("Ιστορικός", "f", "Οι συνέπειες ξεπέρασαν κατά πολύ τα όρια της Ανατολής. Πολλοί λόγιοι είχαν ήδη καταφύγει, ή κατέφυγαν τότε, στην Ιταλία, φέρνοντας μαζί τους χειρόγραφα αρχαίων συγγραφέων. Αν και η σημασία τους συχνά υπερβάλλεται, συνέβαλαν αναμφίβολα στην αναβίωση των ελληνικών σπουδών στη Δύση, την εποχή της Αναγέννησης.", "The consequences went far beyond the borders of the East. Many scholars had already fled, or fled then, to Italy, bringing with them manuscripts of ancient authors. Although their importance is often exaggerated, they undoubtedly contributed to the revival of Greek studies in the West, in the age of the Renaissance."),
 ],
 "questions": [
  Q("Σε τι κατάσταση βρισκόταν η Κωνσταντινούπολη την άνοιξη του 1453;", ["Ήταν στο απόγειο της δύναμής της", "Ήταν η σκιά του παλιού της εαυτού, με πολύ μικρότερο πληθυσμό", "Είχε μόλις κερδίσει έναν πόλεμο", "Ήταν ήδη υπό οθωμανική κατοχή"], 1, "η Κωνσταντινούπολη ήταν η σκιά του παλιού της εαυτού"),
  Q("Ποιο ήταν το νέο όπλο του Μωάμεθ;", ["Πολεμικά πλοία", "Τεράστια κανόνια, ικανά να γκρεμίσουν τα τείχη", "Το υγρό πυρ", "Ιππικό από την Ασία"], 1, "τεράστια κανόνια, ικανά να γκρεμίσουν τα θεοδοσιανά τείχη"),
  Q("Από τι γεννήθηκε ο θρύλος του «Μαρμαρωμένου Βασιλιά»;", ["Από ένα άγαλμα του αυτοκράτορα", "Από το ότι το σώμα του αυτοκράτορα δεν αναγνωρίστηκε ποτέ με βεβαιότητα", "Από ένα όνειρο του σουλτάνου", "Από μια επιγραφή στα τείχη"], 1, "το σώμα του δεν αναγνωρίστηκε ποτέ με βεβαιότητα. Από αυτή την αβεβαιότητα γεννήθηκε ο θρύλος"),
  Q("Πώς κρίνει η ομιλήτρια τον ρόλο των λογίων που κατέφυγαν στην Ιταλία;", ["Τον θεωρεί ασήμαντο", "Θεωρεί ότι συχνά υπερβάλλεται, αλλά ότι συνέβαλαν αναμφίβολα στην αναβίωση των ελληνικών σπουδών", "Θεωρεί ότι αυτοί προκάλεσαν μόνοι τους την Αναγέννηση", "Δεν αναφέρεται σε αυτόν"], 1, "Αν και η σημασία τους συχνά υπερβάλλεται, συνέβαλαν αναμφίβολα στην αναβίωση των ελληνικών σπουδών"),
 ],
 "gloss": {"Άλωση": "άλωση — fall, capture (of a city)", "κραταιά": "κραταιός — mighty", "είχε περιοριστεί": "περιορίζομαι — to be reduced, confined", "υπολογισμούς": "υπολογισμός — estimate, calculation", "πολλαπλάσιο": "πολλαπλάσιος — many times larger", "κανόνια": "κανόνι — cannon", "απόρθητα": "απόρθητος — impregnable", "πολιορκία": "πολιορκία — siege", "υπερασπιστές": "υπερασπιστής — defender", "επιμονή": "επιμονή — persistence, tenacity", "Μαρμαρωμένου": "μαρμαρωμένος — turned to marble", "λόγιοι": "λόγιος — scholar", "χειρόγραφα": "χειρόγραφο — manuscript", "υπερβάλλεται": "υπερβάλλω — to exaggerate", "αναβίωση": "αναβίωση — revival", "Αναγέννησης": "Αναγέννηση — Renaissance"},
})

ITEMS.append({
 "id": "l29-int-nostalgia", "title": "Τι είναι η νοσταλγία;", "title_en": "What is nostalgia?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν ψυχολόγο για τη νοσταλγία.",
 "script": [
  L("Δημοσιογράφος", "f", "Η λέξη «νοσταλγία» ακούγεται πολύ ελληνική, κι όμως δεν τη χρησιμοποιούσαν οι αρχαίοι. Από πού προέρχεται;", "The word 'nostalgia' sounds very Greek, and yet the ancients didn't use it. Where does it come from?"),
  L("Ψυχολόγος", "m", "Πράγματι, τη δημιούργησε το 1688 ένας Ελβετός φοιτητής ιατρικής, ο Γιοχάνες Χόφερ, από τις ελληνικές λέξεις «νόστος», δηλαδή επιστροφή στην πατρίδα, και «άλγος», πόνος. Με αυτήν περιέγραφε μια ασθένεια που παρατηρούσε σε Ελβετούς μισθοφόρους μακριά από το σπίτι τους: μελαγχολία, αϋπνία, ακόμη και πυρετό. Για δύο αιώνες, η νοσταλγία θεωρούνταν πάθηση που μπορούσε να αποβεί και θανατηφόρα.", "Indeed, it was coined in 1688 by a Swiss medical student, Johannes Hofer, from the Greek words 'nostos', that is, return home, and 'algos', pain. With it he described an illness he observed in Swiss mercenaries far from home: melancholy, insomnia, even fever. For two centuries, nostalgia was considered a condition that could even prove fatal."),
  L("Δημοσιογράφος", "f", "Και σήμερα; Είναι κάτι κακό να νοσταλγούμε;", "And today? Is it a bad thing to feel nostalgic?"),
  L("Ψυχολόγος", "m", "Οι σύγχρονες έρευνες δείχνουν μάλλον το αντίθετο. Η νοσταλγία είναι ένα γλυκόπικρο συναίσθημα, αλλά στις περισσότερες περιπτώσεις έχει θετικά αποτελέσματα: ενισχύει την αίσθηση ότι η ζωή μας έχει νόημα και συνέχεια, μας κάνει να νιώθουμε πιο συνδεδεμένοι με τους άλλους και μας βοηθά να αντιμετωπίσουμε τη μοναξιά. Είναι χαρακτηριστικό ότι οι άνθρωποι νοσταλγούν περισσότερο σε περιόδους αβεβαιότητας ή όταν κάνει κρύο.", "Modern research suggests rather the opposite. Nostalgia is a bittersweet emotion, but in most cases it has positive effects: it strengthens the sense that our life has meaning and continuity, makes us feel more connected to others and helps us cope with loneliness. Tellingly, people feel more nostalgic in times of uncertainty or when it's cold."),
  L("Ψυχολόγος", "m", "Υπάρχει βέβαια και μια παγίδα: όταν η νοσταλγία γίνεται εξιδανίκευση. Όταν πιστεύουμε ότι «παλιά όλα ήταν καλύτερα», ξεχνάμε τις δυσκολίες του παρελθόντος και απαξιώνουμε το παρόν. Η υγιής νοσταλγία κοιτάζει πίσω για να πάρει δύναμη, όχι για να μείνει εκεί.", "There is of course also a trap: when nostalgia becomes idealisation. When we believe that 'everything was better in the old days', we forget the difficulties of the past and devalue the present. Healthy nostalgia looks back to draw strength, not to stay there."),
 ],
 "questions": [
  Q("Ποιος δημιούργησε τη λέξη «νοσταλγία»;", ["Ο Όμηρος", "Ένας Ελβετός φοιτητής ιατρικής το 1688", "Ένας Έλληνας ποιητής του 19ου αιώνα", "Ένας Γάλλος φιλόσοφος"], 1, "τη δημιούργησε το 1688 ένας Ελβετός φοιτητής ιατρικής"),
  Q("Πώς θεωρούνταν αρχικά η νοσταλγία;", ["Ως ένα ευχάριστο συναίσθημα", "Ως πάθηση που μπορούσε να αποβεί και θανατηφόρα", "Ως ποιητική έμπνευση", "Ως αρετή των στρατιωτών"], 1, "η νοσταλγία θεωρούνταν πάθηση που μπορούσε να αποβεί και θανατηφόρα"),
  Q("Ποιο από τα παρακάτω είναι, κατά τον ψυχολόγο, θετικό αποτέλεσμα της νοσταλγίας;", ["Μας κάνει να ξεχνάμε το παρελθόν", "Μας βοηθά να αντιμετωπίσουμε τη μοναξιά", "Μας προστατεύει από το κρύο", "Μας κάνει πιο ανταγωνιστικούς"], 1, "μας βοηθά να αντιμετωπίσουμε τη μοναξιά"),
  Q("Ποια είναι η «παγίδα» της νοσταλγίας;", ["Ότι κρατάει πολύ λίγο", "Η εξιδανίκευση του παρελθόντος και η απαξίωση του παρόντος", "Ότι προκαλεί πυρετό", "Ότι μας απομονώνει από την οικογένεια"], 1, "όταν η νοσταλγία γίνεται εξιδανίκευση … ξεχνάμε τις δυσκολίες του παρελθόντος και απαξιώνουμε το παρόν"),
 ],
 "gloss": {"ψυχολόγο": "ψυχολόγος — psychologist", "νόστος": "νόστος — homecoming (Homeric)", "άλγος": "άλγος — pain (learned)", "μισθοφόρους": "μισθοφόρος — mercenary", "μελαγχολία": "μελαγχολία — melancholy", "αϋπνία": "αϋπνία — insomnia", "πάθηση": "πάθηση — condition, disorder", "να αποβεί": "αποβαίνω — to prove, turn out", "θανατηφόρα": "θανατηφόρος — fatal", "γλυκόπικρο": "γλυκόπικρος — bittersweet", "ενισχύει": "ενισχύω — to strengthen", "αβεβαιότητας": "αβεβαιότητα — uncertainty", "παγίδα": "παγίδα — trap", "εξιδανίκευση": "εξιδανίκευση — idealisation", "απαξιώνουμε": "απαξιώνω — to devalue, disparage"},
})
rnd = random.Random(29)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-29.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
