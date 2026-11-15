# Source for library/listening/listening-20.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l20.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l20-ann-gipedo", "title": "Ανακοίνωση στο γήπεδο", "title_en": "An announcement at the stadium", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα ενός γηπέδου πριν από έναν ποδοσφαιρικό αγώνα.",
 "script": [
  L("Εκφωνητής", "m", "Καλησπέρα σας και καλώς ήρθατε στο γήπεδο. Ο αγώνας θα ξεκινήσει με καθυστέρηση είκοσι λεπτών, λόγω του αυξημένου ελέγχου στις εισόδους. Παρακαλούμε όσους βρίσκονται ακόμη έξω να έχουν έτοιμα το εισιτήριο και την ταυτότητά τους.", "Good evening and welcome to the stadium. The match will start twenty minutes late, due to increased checks at the entrances. We ask those who are still outside to have their ticket and their ID ready."),
  L("Εκφωνητής", "m", "Υπενθυμίζουμε ότι απαγορεύεται αυστηρά η χρήση καπνογόνων και η είσοδος με γυάλινα μπουκάλια. Θεατές που θα παραβιάσουν τους κανόνες θα απομακρύνονται από το γήπεδο χωρίς επιστροφή του αντιτίμου.", "We remind you that the use of flares and entry with glass bottles is strictly forbidden. Spectators who break the rules will be removed from the stadium without a refund."),
  L("Εκφωνητής", "m", "Μετά το τέλος του αγώνα, οι θεατές της ανατολικής κερκίδας παρακαλούνται να παραμείνουν στις θέσεις τους δέκα λεπτά, ώσπου να αποχωρήσουν οι φιλοξενούμενοι οπαδοί. Ο σταθμός του μετρό θα λειτουργεί ως τη μία μετά τα μεσάνυχτα.", "After the end of the match, spectators in the east stand are asked to stay in their seats for ten minutes, until the visiting fans have left. The metro station will operate until one after midnight."),
 ],
 "questions": [
  Q("Γιατί θα καθυστερήσει ο αγώνας;", ["Λόγω βροχής", "Λόγω του αυξημένου ελέγχου στις εισόδους", "Λόγω τραυματισμού ενός παίκτη", "Λόγω βλάβης στους προβολείς"], 1, "λόγω του αυξημένου ελέγχου στις εισόδους"),
  Q("Τι θα συμβεί σε όσους παραβιάσουν τους κανόνες;", ["Θα πληρώσουν πρόστιμο", "Θα απομακρυνθούν χωρίς επιστροφή χρημάτων", "Θα μεταφερθούν σε άλλη κερκίδα", "Θα πάρουν προειδοποίηση"], 1, "θα απομακρύνονται από το γήπεδο χωρίς επιστροφή του αντιτίμου"),
  Q("Τι ζητείται από τους θεατές της ανατολικής κερκίδας;", ["Να φύγουν πριν από το τέλος", "Να παραμείνουν στις θέσεις τους δέκα λεπτά μετά τον αγώνα", "Να χρησιμοποιήσουν άλλη έξοδο", "Να πάνε στο μετρό αμέσως"], 1, "παρακαλούνται να παραμείνουν στις θέσεις τους δέκα λεπτά"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "γηπέδου": "γήπεδο — stadium, pitch", "καθυστέρηση": "καθυστέρηση — delay", "εισόδους": "είσοδος — entrance", "απαγορεύεται": "απαγορεύεται — it is forbidden", "καπνογόνων": "καπνογόνο — flare (smoke bomb)", "θα παραβιάσουν": "παραβιάζω — to break, violate", "αντιτίμου": "αντίτιμο — price paid, cost", "κερκίδας": "κερκίδα — stand (in a stadium)", "φιλοξενούμενοι": "φιλοξενούμενος — visiting (team or fans)", "οπαδοί": "οπαδός — fan, supporter"},
})

ITEMS.append({
 "id": "l20-vm-vivliothiki", "title": "Ένα βιβλίο που άργησε", "title_en": "An overdue book", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τη δημοτική βιβλιοθήκη.",
 "script": [
  L("Βιβλιοθηκονόμος", "f", "Καλημέρα, σας τηλεφωνώ από τη Δημοτική Βιβλιοθήκη. Σύμφωνα με το σύστημά μας, έχετε δανειστεί δύο βιβλία, τα οποία έπρεπε να επιστραφούν πριν από τρεις εβδομάδες. Το ένα από αυτά το έχουν ζητήσει άλλοι δύο αναγνώστες.", "Good morning, I'm calling from the Municipal Library. According to our system, you have borrowed two books which should have been returned three weeks ago. One of them has been requested by two other readers."),
  L("Βιβλιοθηκονόμος", "f", "Δεν επιβάλλουμε πρόστιμα, αλλά μέχρι να επιστρέψετε τα βιβλία η κάρτα μέλους σας θα παραμείνει ανενεργή και δεν θα μπορείτε να δανειστείτε άλλα. Αν θέλετε να κρατήσετε το δεύτερο βιβλίο, μπορείτε να ανανεώσετε τον δανεισμό ηλεκτρονικά, μέσα από τον λογαριασμό σας.", "We don't impose fines, but until you return the books your membership card will remain inactive and you won't be able to borrow others. If you want to keep the second book, you can renew the loan online, through your account."),
  L("Βιβλιοθηκονόμος", "f", "Αν είστε εκτός Αθήνας, μπορείτε να μας τα στείλετε και με το ταχυδρομείο. Υπάρχει επίσης κουτί επιστροφών δίπλα στην κεντρική είσοδο, που είναι ανοιχτό όλο το εικοσιτετράωρο.", "If you are out of Athens, you can also send them to us by post. There is also a returns box next to the main entrance, which is open twenty-four hours a day."),
 ],
 "questions": [
  Q("Γιατί είναι επείγον να επιστραφεί το ένα βιβλίο;", ["Γιατί είναι πολύ ακριβό", "Γιατί το έχουν ζητήσει άλλοι δύο αναγνώστες", "Γιατί η βιβλιοθήκη θα κλείσει", "Γιατί είναι το μοναδικό αντίτυπο στην Ελλάδα"], 1, "Το ένα από αυτά το έχουν ζητήσει άλλοι δύο αναγνώστες"),
  Q("Ποια είναι η συνέπεια της καθυστέρησης;", ["Ένα πρόστιμο", "Η κάρτα μέλους μένει ανενεργή", "Η διαγραφή από τη βιβλιοθήκη", "Μια επιστολή στον δήμο"], 1, "η κάρτα μέλους σας θα παραμείνει ανενεργή"),
  Q("Πότε μπορεί κανείς να χρησιμοποιήσει το κουτί επιστροφών;", ["Μόνο τις ώρες λειτουργίας", "Μόνο τα Σαββατοκύριακα", "Όλο το εικοσιτετράωρο", "Μόνο το πρωί"], 2, "που είναι ανοιχτό όλο το εικοσιτετράωρο"),
 ],
 "gloss": {"τηλεφωνητή": "τηλεφωνητής — answering machine", "δανειστεί": "δανείζομαι — to borrow", "να επιστραφούν": "επιστρέφομαι — to be returned", "αναγνώστες": "αναγνώστης — reader", "επιβάλλουμε": "επιβάλλω — to impose", "πρόστιμα": "πρόστιμο — fine", "ανενεργή": "ανενεργός — inactive", "να ανανεώσετε": "ανανεώνω — to renew", "δανεισμό": "δανεισμός — loan, lending", "εικοσιτετράωρο": "εικοσιτετράωρο — twenty-four hours"},
})

ITEMS.append({
 "id": "l20-dia-podilato", "title": "Ένα ποδήλατο για την πόλη", "title_en": "A bike for the city", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα κατάστημα ποδηλάτων.",
 "script": [
  L("Πωλητής", "m", "Καλημέρα. Τι είδους ποδήλατο ψάχνετε; Για βόλτες, για βουνό ή για καθημερινές μετακινήσεις;", "Good morning. What kind of bike are you looking for? For rides, for the mountains or for daily commuting?"),
  L("Πελάτισσα", "f", "Για να πηγαίνω στη δουλειά, περίπου έξι χιλιόμετρα. Το πρόβλημα είναι ότι η διαδρομή έχει δύο μεγάλες ανηφόρες και δεν θέλω να φτάνω στο γραφείο ιδρωμένη.", "To get to work, about six kilometres. The problem is that the route has two big hills and I don't want to arrive at the office sweaty."),
  L("Πωλητής", "m", "Τότε σας προτείνω ένα ηλεκτρικό. Η μπαταρία κρατάει γύρω στα πενήντα χιλιόμετρα, άρα θα τη φορτίζετε μία με δύο φορές την εβδομάδα. Είναι ακριβότερο, αλλά ο δήμος δίνει επιδότηση για την αγορά, που καλύπτει ένα μέρος της τιμής.", "Then I'd suggest an electric one. The battery lasts about fifty kilometres, so you'd charge it once or twice a week. It's more expensive, but the council gives a subsidy for the purchase which covers part of the price."),
  L("Πελάτισσα", "f", "Ωραία. Και πού θα το αφήνω; Στο γραφείο δεν έχουμε χώρο, και φοβάμαι μήπως μου το κλέψουν.", "Great. And where will I leave it? There's no room at the office, and I'm afraid it might be stolen."),
  L("Πωλητής", "m", "Μαζί με το ποδήλατο θα σας δώσουμε μια γερή κλειδαριά. Και η μπαταρία βγαίνει, οπότε μπορείτε να την παίρνετε μαζί σας· χωρίς αυτήν, το ποδήλατο δεν ενδιαφέρει κανέναν κλέφτη.", "With the bike we'll give you a strong lock. And the battery comes out, so you can take it with you; without it, the bike is of no interest to any thief."),
 ],
 "questions": [
  Q("Τι ανησυχεί την πελάτισσα για τη διαδρομή;", ["Η κίνηση στους δρόμους", "Οι ανηφόρες, γιατί δεν θέλει να φτάνει ιδρωμένη", "Η απόσταση των είκοσι χιλιομέτρων", "Η έλλειψη ποδηλατόδρομων"], 1, "η διαδρομή έχει δύο μεγάλες ανηφόρες και δεν θέλω να φτάνω στο γραφείο ιδρωμένη"),
  Q("Τι λέει ο πωλητής για την τιμή;", ["Ότι το ηλεκτρικό είναι φθηνότερο", "Ότι ο δήμος δίνει επιδότηση για ένα μέρος της", "Ότι μπορεί να πληρώσει σε δόσεις", "Ότι έχει έκπτωση μόνο αυτή την εβδομάδα"], 1, "ο δήμος δίνει επιδότηση για την αγορά, που καλύπτει ένα μέρος της τιμής"),
  Q("Γιατί, σύμφωνα με τον πωλητή, δεν θα κλέψουν εύκολα το ποδήλατο;", ["Γιατί έχει συναγερμό", "Γιατί η μπαταρία βγαίνει και χωρίς αυτήν δεν ενδιαφέρει κανέναν", "Γιατί είναι ασφαλισμένο", "Γιατί θα το αφήνει στο γραφείο"], 1, "η μπαταρία βγαίνει, οπότε μπορείτε να την παίρνετε μαζί σας"),
 ],
 "gloss": {"μετακινήσεις": "μετακίνηση — getting around, commuting", "ανηφόρες": "ανηφόρα — uphill stretch", "ιδρωμένη": "ιδρωμένος — sweaty", "μπαταρία": "μπαταρία — battery", "θα τη φορτίζετε": "φορτίζω — to charge", "επιδότηση": "επιδότηση — subsidy", "καλύπτει": "καλύπτω — to cover", "κλειδαριά": "κλειδαριά — lock", "κλέφτη": "κλέφτης — thief"},
})

ITEMS.append({
 "id": "l20-dia-diavatirio", "title": "Ανανέωση διαβατηρίου", "title_en": "Renewing a passport", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση στο γραφείο διαβατηρίων ενός αστυνομικού τμήματος.",
 "script": [
  L("Πολίτης", "m", "Καλημέρα. Το διαβατήριό μου λήγει τον άλλο μήνα και φεύγω για τον Καναδά σε έξι εβδομάδες. Προλαβαίνω να βγάλω καινούργιο;", "Good morning. My passport expires next month and I'm leaving for Canada in six weeks. Is there time to get a new one?"),
  L("Υπάλληλος", "f", "Κανονικά, το διαβατήριο εκδίδεται σε λίγες εργάσιμες μέρες από τη στιγμή που θα καταθέσετε την αίτηση. Πρώτα όμως πρέπει να κλείσετε ραντεβού ηλεκτρονικά και να πληρώσετε το παράβολο. Έχετε φέρει φωτογραφίες;", "Normally the passport is issued within a few working days of submitting the application. But first you have to book an appointment online and pay the fee. Have you brought photographs?"),
  L("Πολίτης", "m", "Έχω αυτές εδώ, τις έβγαλα σε ένα μηχάνημα στο μετρό.", "I have these here, I took them in a machine at the metro."),
  L("Υπάλληλος", "f", "Δυστυχώς δεν γίνονται δεκτές: το φόντο δεν είναι ομοιόμορφο και φοράτε γυαλιά. Χρειάζεστε φωτογραφίες από φωτογράφο, σύμφωνα με τις προδιαγραφές. Και μην ξεχάσετε να φέρετε και το παλιό διαβατήριο, γιατί θα ακυρωθεί.", "Unfortunately they won't be accepted: the background isn't uniform and you're wearing glasses. You need photos from a photographer, according to the specifications. And don't forget to bring the old passport too, because it will be cancelled."),
 ],
 "questions": [
  Q("Γιατί βιάζεται ο πολίτης;", ["Γιατί έχασε το διαβατήριό του", "Γιατί φεύγει για τον Καναδά σε έξι εβδομάδες", "Γιατί αλλάζει δουλειά", "Γιατί το διαβατήριο έχει λήξει εδώ και χρόνια"], 1, "φεύγω για τον Καναδά σε έξι εβδομάδες"),
  Q("Τι πρέπει να κάνει πρώτα;", ["Να φέρει δύο μάρτυρες", "Να κλείσει ραντεβού ηλεκτρονικά και να πληρώσει το παράβολο", "Να πάει στο προξενείο", "Να στείλει την αίτηση με το ταχυδρομείο"], 1, "πρέπει να κλείσετε ραντεβού ηλεκτρονικά και να πληρώσετε το παράβολο"),
  Q("Γιατί δεν γίνονται δεκτές οι φωτογραφίες του;", ["Γιατί είναι ασπρόμαυρες", "Γιατί είναι παλιές", "Γιατί το φόντο δεν είναι ομοιόμορφο και φοράει γυαλιά", "Γιατί είναι πολύ μικρές"], 2, "το φόντο δεν είναι ομοιόμορφο και φοράτε γυαλιά"),
 ],
 "gloss": {"διαβατηρίων": "διαβατήριο — passport", "αστυνομικού τμήματος": "αστυνομικό τμήμα — police station", "λήγει": "λήγω — to expire", "Προλαβαίνω": "προλαβαίνω — to have time, make it in time", "εκδίδεται": "εκδίδομαι — to be issued", "εργάσιμες": "εργάσιμος — working (day)", "καταθέσετε": "καταθέτω — to submit, file", "παράβολο": "παράβολο — (state) fee", "φόντο": "φόντο — background", "ομοιόμορφο": "ομοιόμορφος — uniform, even", "προδιαγραφές": "προδιαγραφή — specification", "θα ακυρωθεί": "ακυρώνομαι — to be cancelled"},
})

ITEMS.append({
 "id": "l20-mon-misthos", "title": "Ο πρώτος μου μισθός", "title_en": "My first pay packet", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να θυμάται σε ένα podcast τον πρώτο της μισθό.",
 "script": [
  L("Σοφία", "f", "Ήμουν δεκαεπτά χρονών και το καλοκαίρι δούλεψα σε ένα ζαχαροπλαστείο στο λιμάνι. Οκτώ ώρες την ημέρα, όρθια, να σερβίρω παγωτά σε τουρίστες που άλλαζαν γνώμη τρεις φορές πριν διαλέξουν γεύση.", "I was seventeen and in the summer I worked in a patisserie at the harbour. Eight hours a day, on my feet, serving ice cream to tourists who changed their minds three times before choosing a flavour."),
  L("Σοφία", "f", "Στο τέλος του πρώτου μήνα, ο ιδιοκτήτης μού έδωσε έναν φάκελο με μετρητά. Θυμάμαι ότι τον άνοιξα στο λεωφορείο και μέτρησα τα χαρτονομίσματα τρεις φορές. Δεν ήταν πολλά, αλλά ήταν τα πρώτα χρήματα που είχα κερδίσει μόνη μου.", "At the end of the first month, the owner gave me an envelope of cash. I remember opening it on the bus and counting the notes three times. It wasn't much, but it was the first money I had earned myself."),
  L("Σοφία", "f", "Είχα σχεδιάσει να αγοράσω ένα κινητό. Τελικά όμως αγόρασα στη μητέρα μου ένα πλυντήριο πιάτων, γιατί την έβλεπα κάθε βράδυ να πλένει με το χέρι μετά από δέκα ώρες δουλειά. Εκείνη έκλαψε. Από τότε έχω πάρει πολλούς μισθούς, αλλά κανένας δεν μου έδωσε τέτοια χαρά.", "I had planned to buy a mobile phone. But in the end I bought my mother a dishwasher, because I saw her every evening washing up by hand after ten hours' work. She cried. Since then I've had many pay packets, but none gave me such joy."),
 ],
 "questions": [
  Q("Πού δούλεψε η Σοφία εκείνο το καλοκαίρι;", ["Σε ένα ξενοδοχείο", "Σε ένα ζαχαροπλαστείο στο λιμάνι", "Σε ένα σούπερ μάρκετ", "Σε μια ταβέρνα"], 1, "δούλεψα σε ένα ζαχαροπλαστείο στο λιμάνι"),
  Q("Τι έκανε όταν πήρε τον πρώτο της μισθό;", ["Τον κατέθεσε στην τράπεζα", "Μέτρησε τα χρήματα τρεις φορές στο λεωφορείο", "Τον έδωσε όλο στον πατέρα της", "Πήγε αμέσως για ψώνια"], 1, "τον άνοιξα στο λεωφορείο και μέτρησα τα χαρτονομίσματα τρεις φορές"),
  Q("Τι αγόρασε τελικά με τα χρήματα;", ["Ένα κινητό", "Ένα πλυντήριο πιάτων για τη μητέρα της", "Ένα εισιτήριο για ταξίδι", "Βιβλία για το σχολείο"], 1, "αγόρασα στη μητέρα μου ένα πλυντήριο πιάτων"),
 ],
 "gloss": {"μισθό": "μισθός — salary, pay", "ζαχαροπλαστείο": "ζαχαροπλαστείο — patisserie, cake shop", "όρθια": "όρθιος — standing", "γεύση": "γεύση — flavour", "φάκελο": "φάκελος — envelope", "μετρητά": "μετρητά — cash", "χαρτονομίσματα": "χαρτονόμισμα — banknote", "είχα κερδίσει": "κερδίζω — to earn, win", "πλυντήριο πιάτων": "πλυντήριο πιάτων — dishwasher"},
})

ITEMS.append({
 "id": "l20-rep-nafplio", "title": "Ναύπλιο, η πρώτη πρωτεύουσα", "title_en": "Nafplio, the first capital", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από το Ναύπλιο.",
 "script": [
  L("Ρεπόρτερ", "f", "Περπατώντας στα στενά του Ναυπλίου, με τα νεοκλασικά σπίτια και τα μπαλκόνια γεμάτα βουκαμβίλιες, είναι εύκολο να ξεχάσει κανείς ότι εδώ γράφτηκαν μερικές από τις πιο δραματικές σελίδες της νεότερης ελληνικής ιστορίας.", "Walking through the narrow streets of Nafplio, with its neoclassical houses and balconies full of bougainvillea, it's easy to forget that some of the most dramatic pages of modern Greek history were written here."),
  L("Ρεπόρτερ", "f", "Το 1828 αποβιβάστηκε εδώ ο Ιωάννης Καποδίστριας, ο πρώτος κυβερνήτης της Ελλάδας, και λίγο αργότερα, μετά από ένα σύντομο διάστημα στην Αίγινα, το Ναύπλιο έγινε η έδρα της κυβέρνησης του νέου κράτους. Το 1831, ο Καποδίστριας δολοφονήθηκε μπροστά στην εκκλησία του Αγίου Σπυρίδωνα, όπου ακόμη και σήμερα δείχνουν στους επισκέπτες το σημάδι μιας σφαίρας στον τοίχο.", "In 1828 Ioannis Kapodistrias, the first governor of Greece, landed here, and shortly afterwards, after a brief period on Aegina, Nafplio became the seat of government of the new state. In 1831, Kapodistrias was assassinated in front of the church of Agios Spyridon, where even today visitors are shown the mark of a bullet in the wall."),
  L("Ρεπόρτερ", "f", "Το 1834 η πρωτεύουσα μεταφέρθηκε στην Αθήνα. Πάνω από την πόλη υψώνεται το κάστρο του Παλαμηδίου, που χτίστηκε από τους Βενετούς. Η παράδοση λέει ότι τα σκαλοπάτια του είναι εννιακόσια ενενήντα εννιά· στην πραγματικότητα είναι λιγότερα, αλλά όσοι τα ανεβαίνουν το καλοκαίρι δύσκολα θα διαφωνήσουν.", "In 1834 the capital was moved to Athens. Above the town rises the Palamidi fortress, built by the Venetians. Tradition says its steps number nine hundred and ninety-nine; in fact there are fewer, but anyone who climbs them in summer will hardly disagree."),
 ],
 "questions": [
  Q("Τι έγινε το 1828;", ["Χτίστηκε το Παλαμήδι", "Αποβιβάστηκε στο Ναύπλιο ο Καποδίστριας", "Η πρωτεύουσα μεταφέρθηκε στην Αθήνα", "Δολοφονήθηκε ο Καποδίστριας"], 1, "Το 1828 αποβιβάστηκε εδώ ο Ιωάννης Καποδίστριας"),
  Q("Τι δείχνουν στους επισκέπτες στον Άγιο Σπυρίδωνα;", ["Τον τάφο του Καποδίστρια", "Το σημάδι μιας σφαίρας στον τοίχο", "Μια παλιά εικόνα", "Το γραφείο του κυβερνήτη"], 1, "δείχνουν στους επισκέπτες το σημάδι μιας σφαίρας στον τοίχο"),
  Q("Τι λέει η ρεπόρτερ για τα σκαλοπάτια του Παλαμηδίου;", ["Ότι είναι ακριβώς 999", "Ότι είναι λιγότερα από όσα λέει η παράδοση", "Ότι κλείνουν το καλοκαίρι", "Ότι χτίστηκαν πρόσφατα"], 1, "στην πραγματικότητα είναι λιγότερα"),
 ],
 "gloss": {"στενά": "στενό — narrow street, alley", "νεοκλασικά": "νεοκλασικός — neoclassical", "βουκαμβίλιες": "βουκαμβίλια — bougainvillea", "κυβερνήτης": "κυβερνήτης — governor", "έδρα της κυβέρνησης": "έδρα της κυβέρνησης — seat of government", "αποβιβάστηκε": "αποβιβάζομαι — to land, disembark", "δολοφονήθηκε": "δολοφονούμαι — to be assassinated", "σφαίρας": "σφαίρα — bullet", "μεταφέρθηκε": "μεταφέρομαι — to be moved", "υψώνεται": "υψώνομαι — to rise", "σκαλοπάτια": "σκαλοπάτι — step"},
})

ITEMS.append({
 "id": "l20-rep-epidavros", "title": "Το θέατρο της Επιδαύρου", "title_en": "The theatre of Epidaurus", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από το αρχαίο θέατρο της Επιδαύρου, λίγο πριν από μια παράσταση.",
 "script": [
  L("Ρεπόρτερ", "m", "Ο ήλιος δύει πίσω από τους λόφους και οι κερκίδες γεμίζουν σιγά σιγά. Το θέατρο της Επιδαύρου χτίστηκε τον 4ο αιώνα π.Χ., κοντά στο ιερό του Ασκληπιού, του θεού της ιατρικής, όπου έρχονταν άρρωστοι από όλο τον ελληνικό κόσμο.", "The sun is setting behind the hills and the stands are slowly filling. The theatre of Epidaurus was built in the 4th century BC, near the sanctuary of Asclepius, the god of medicine, where sick people came from all over the Greek world."),
  L("Ρεπόρτερ", "m", "Αυτό που εντυπωσιάζει περισσότερο είναι η ακουστική του. Ένας ξεναγός στέκεται στο κέντρο της ορχήστρας και σκίζει ένα κομμάτι χαρτί· ο ήχος ακούγεται καθαρά ως την τελευταία σειρά, όπου κάθονται πάνω από δώδεκα χιλιάδες θεατές. Οι επιστήμονες εξακολουθούν να μελετούν πώς το πέτυχαν οι αρχαίοι αρχιτέκτονες.", "What is most impressive is its acoustics. A guide stands in the centre of the orchestra and tears a piece of paper; the sound can be heard clearly up to the last row, where more than twelve thousand spectators sit. Scientists are still studying how the ancient architects achieved it."),
  L("Ρεπόρτερ", "m", "Από τα μέσα του εικοστού αιώνα, το θέατρο ζωντανεύει ξανά κάθε καλοκαίρι με παραστάσεις αρχαίου δράματος. Για πολλούς Έλληνες, μια βραδιά εδώ, κάτω από τα αστέρια, είναι ένα είδος προσκυνήματος.", "Since the middle of the twentieth century, the theatre has come alive again every summer with performances of ancient drama. For many Greeks, an evening here, under the stars, is a kind of pilgrimage."),
 ],
 "questions": [
  Q("Κοντά σε ποιο ιερό χτίστηκε το θέατρο;", ["Του Δία", "Του Απόλλωνα", "Του Ασκληπιού", "Της Αθηνάς"], 2, "κοντά στο ιερό του Ασκληπιού, του θεού της ιατρικής"),
  Q("Τι δείχνει το πείραμα με το χαρτί;", ["Ότι το θέατρο είναι πολύ μεγάλο", "Ότι ο ήχος ακούγεται καθαρά ως την τελευταία σειρά", "Ότι ο αέρας είναι δυνατός", "Ότι οι ξεναγοί είναι καλοί ηθοποιοί"], 1, "ο ήχος ακούγεται καθαρά ως την τελευταία σειρά"),
  Q("Τι λέει ο ρεπόρτερ για τις σημερινές παραστάσεις;", ["Ότι γίνονται μόνο τον χειμώνα", "Ότι ξεκίνησαν πριν από λίγα χρόνια", "Ότι γίνονται κάθε καλοκαίρι από τα μέσα του εικοστού αιώνα", "Ότι έχουν σταματήσει"], 2, "Από τα μέσα του εικοστού αιώνα, το θέατρο ζωντανεύει ξανά κάθε καλοκαίρι"),
 ],
 "gloss": {"παράσταση": "παράσταση — performance", "δύει": "δύω — to set (of the sun)", "κερκίδες": "κερκίδα — tier of seats, stand", "ιερό": "ιερό — sanctuary", "ακουστική": "ακουστική — acoustics", "ξεναγός": "ξεναγός — tour guide", "ορχήστρας": "ορχήστρα — orchestra (the circular floor of an ancient theatre)", "σκίζει": "σκίζω — to tear", "εξακολουθούν": "εξακολουθώ — to continue", "αρχαίου δράματος": "αρχαίο δράμα — ancient drama", "προσκυνήματος": "προσκύνημα — pilgrimage"},
})

ITEMS.append({
 "id": "l20-int-diasosi", "title": "Εθελοντής στη διάσωση", "title_en": "A volunteer rescuer", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν εθελοντή μιας ομάδας ορεινής διάσωσης.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς αποφασίσατε να γίνετε εθελοντής διασώστης;", "How did you decide to become a volunteer rescuer?"),
  L("Εθελοντής", "m", "Πριν από οκτώ χρόνια χάθηκα ο ίδιος στον Όλυμπο, μέσα στην ομίχλη. Με βρήκαν δύο εθελοντές στις τρεις τα ξημερώματα. Όταν γύρισα στη Θεσσαλονίκη, το πρώτο που έκανα ήταν να γραφτώ στην ομάδα τους. Ένιωθα ότι χρωστούσα κάτι.", "Eight years ago I got lost myself on Olympus, in the fog. Two volunteers found me at three in the morning. When I got back to Thessaloniki, the first thing I did was join their team. I felt I owed something."),
  L("Δημοσιογράφος", "f", "Ποια είναι τα πιο συνηθισμένα λάθη των πεζοπόρων;", "What are walkers' most common mistakes?"),
  L("Εθελοντής", "m", "Ξεκινούν αργά το μεσημέρι, χωρίς να έχουν δει την πρόγνωση του καιρού, με αθλητικά παπούτσια και μισό μπουκάλι νερό. Και πολλοί βασίζονται μόνο στο κινητό τους για τον προσανατολισμό, ενώ στο βουνό το σήμα χάνεται και η μπαταρία αδειάζει γρήγορα στο κρύο. Πάντα να λέτε σε κάποιον πού πηγαίνετε και πότε σκοπεύετε να γυρίσετε.", "They start late at midday, without having looked at the weather forecast, in trainers and with half a bottle of water. And many rely only on their mobile for navigation, while on the mountain the signal disappears and the battery runs down fast in the cold. Always tell someone where you are going and when you plan to come back."),
 ],
 "questions": [
  Q("Γιατί έγινε εθελοντής;", ["Γιατί είναι γιατρός", "Γιατί τον είχαν σώσει κάποτε εθελοντές και ένιωθε ότι χρωστούσε", "Γιατί του το ζήτησε ένας φίλος", "Γιατί ήθελε να γνωρίσει κόσμο"], 1, "Ένιωθα ότι χρωστούσα κάτι"),
  Q("Ποιο από τα παρακάτω ΔΕΝ αναφέρει ως συνηθισμένο λάθος;", ["Ότι ξεκινούν αργά", "Ότι φορούν αθλητικά παπούτσια", "Ότι περπατούν σε μεγάλες ομάδες", "Ότι παίρνουν λίγο νερό"], 2, "Ξεκινούν αργά το μεσημέρι ... με αθλητικά παπούτσια και μισό μπουκάλι νερό"),
  Q("Ποια συμβουλή δίνει στο τέλος;", ["Να έχουν πάντα δεύτερο κινητό", "Να λένε σε κάποιον πού πάνε και πότε θα γυρίσουν", "Να περπατούν μόνο το πρωί", "Να μην πηγαίνουν ποτέ μόνοι"], 1, "Πάντα να λέτε σε κάποιον πού πηγαίνετε και πότε σκοπεύετε να γυρίσετε"),
 ],
 "gloss": {"ορεινής διάσωσης": "ορεινή διάσωση — mountain rescue", "διασώστης": "διασώστης — rescuer", "ομίχλη": "ομίχλη — fog", "να γραφτώ": "γράφομαι — to sign up, join", "χρωστούσα": "χρωστάω — to owe", "πεζοπόρων": "πεζοπόρος — hiker, walker", "πρόγνωση του καιρού": "πρόγνωση του καιρού — weather forecast", "βασίζονται": "βασίζομαι — to rely on", "προσανατολισμό": "προσανατολισμός — orientation, navigation", "σήμα": "σήμα — signal"},
})

ITEMS.append({
 "id": "l20-mon-alfavito", "title": "Από πού ήρθε το ελληνικό αλφάβητο", "title_en": "Where the Greek alphabet came from", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για την ιστορία της γραφής.",
 "script": [
  L("Αφηγήτρια", "f", "Οι Έλληνες δεν επινόησαν τη γραφή από το μηδέν. Γύρω στον 8ο αιώνα π.Χ., μετά από αιώνες κατά τους οποίους η γραφή είχε ξεχαστεί, υιοθέτησαν το αλφάβητο των Φοινίκων, ενός λαού εμπόρων και ναυτικών από τις ακτές της σημερινής Συρίας και του Λιβάνου. Ακόμη και τα ονόματα των γραμμάτων το μαρτυρούν: το «άλφα» και το «βήτα» δεν σημαίνουν τίποτα στα ελληνικά, ενώ στις σημιτικές γλώσσες σημαίνουν «βόδι» και «σπίτι».", "The Greeks did not invent writing from scratch. Around the 8th century BC, after centuries during which writing had been forgotten, they adopted the alphabet of the Phoenicians, a people of merchants and sailors from the coasts of today's Syria and Lebanon. Even the names of the letters bear witness to it: 'alpha' and 'beta' mean nothing in Greek, while in the Semitic languages they mean 'ox' and 'house'."),
  L("Αφηγήτρια", "f", "Η μεγάλη καινοτομία των Ελλήνων ήταν τα φωνήεντα. Το φοινικικό αλφάβητο σημείωνε μόνο σύμφωνα· ο αναγνώστης έπρεπε να μαντέψει τα φωνήεντα από τα συμφραζόμενα. Οι Έλληνες χρησιμοποίησαν ορισμένα σύμβολα που δεν τους χρειάζονταν για να αποδώσουν φωνήεντα, και δημιούργησαν έτσι ένα από τα πρώτα πλήρη αλφάβητα της ιστορίας.", "The Greeks' great innovation was vowels. The Phoenician alphabet marked only consonants; the reader had to guess the vowels from the context. The Greeks used certain symbols they didn't need to represent vowels, and so created one of the first complete alphabets in history."),
  L("Αφηγήτρια", "f", "Στην αρχή δεν υπήρχε ένα ενιαίο ελληνικό αλφάβητο, αλλά πολλές τοπικές παραλλαγές. Μία από αυτές, που χρησιμοποιούσαν άποικοι από την Εύβοια στη νότια Ιταλία, πέρασε στους Ετρούσκους και από εκεί στους Ρωμαίους. Έτσι, κάθε φορά που γράφουμε με λατινικούς χαρακτήρες, χρησιμοποιούμε στην ουσία μακρινούς απογόνους των ελληνικών γραμμάτων.", "At first there was no single Greek alphabet, but many local variants. One of them, used by colonists from Euboea in southern Italy, passed to the Etruscans and from there to the Romans. So every time we write in Latin characters, we are essentially using distant descendants of the Greek letters."),
 ],
 "questions": [
  Q("Από ποιον λαό υιοθέτησαν οι Έλληνες το αλφάβητο;", ["Από τους Αιγυπτίους", "Από τους Φοίνικες", "Από τους Ρωμαίους", "Από τους Ετρούσκους"], 1, "υιοθέτησαν το αλφάβητο των Φοινίκων"),
  Q("Τι δείχνουν, κατά την αφηγήτρια, τα ονόματα «άλφα» και «βήτα»;", ["Ότι είναι αρχαίες ελληνικές λέξεις", "Ότι προέρχονται από σημιτικές γλώσσες", "Ότι τα επινόησε ένας φιλόσοφος", "Ότι σημαίνουν «αρχή» και «τέλος»"], 1, "στις σημιτικές γλώσσες σημαίνουν «βόδι» και «σπίτι»"),
  Q("Ποια ήταν η μεγάλη καινοτομία των Ελλήνων;", ["Η γραφή από δεξιά προς τα αριστερά", "Η προσθήκη φωνηέντων", "Τα κεφαλαία γράμματα", "Η χρήση της πέτρας ως υλικού"], 1, "Η μεγάλη καινοτομία των Ελλήνων ήταν τα φωνήεντα"),
  Q("Πώς έφτασε το ελληνικό αλφάβητο στους Ρωμαίους;", ["Μέσω των Φοινίκων", "Μέσω των Ετρούσκων, από Ευβοείς αποίκους στη νότια Ιταλία", "Μέσω του Βυζαντίου", "Μέσω της Αιγύπτου"], 1, "πέρασε στους Ετρούσκους και από εκεί στους Ρωμαίους"),
 ],
 "gloss": {"γραφής": "γραφή — writing", "επινόησαν": "επινοώ — to invent", "υιοθέτησαν": "υιοθετώ — to adopt", "μαρτυρούν": "μαρτυρώ — to bear witness to", "σημιτικές": "σημιτικός — Semitic", "βόδι": "βόδι — ox", "καινοτομία": "καινοτομία — innovation", "φωνήεντα": "φωνήεν — vowel", "σύμφωνα": "σύμφωνο — consonant", "να μαντέψει": "μαντεύω — to guess", "συμφραζόμενα": "συμφραζόμενα — context", "παραλλαγές": "παραλλαγή — variant", "άποικοι": "άποικος — colonist, settler", "απογόνους": "απόγονος — descendant"},
})

ITEMS.append({
 "id": "l20-int-metafrasi", "title": "Η μετάφραση στην εποχή της τεχνητής νοημοσύνης", "title_en": "Translation in the age of AI", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια μεταφράστρια λογοτεχνίας για την αυτόματη μετάφραση.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί λένε ότι σε λίγα χρόνια οι μεταφραστές δεν θα χρειάζονται. Φοβάστε για το επάγγελμά σας;", "Many people say that in a few years translators won't be needed. Do you fear for your profession?"),
  L("Μεταφράστρια", "f", "Θα ήμουν ανειλικρινής αν έλεγα ότι δεν έχει αλλάξει τίποτα. Στα τεχνικά κείμενα, στα εγχειρίδια, στα συμβόλαια, τα εργαλεία αυτά κάνουν ήδη πολύ καλή δουλειά, και πολλοί συνάδελφοι πλέον διορθώνουν αντί να μεταφράζουν. Οι αμοιβές τους έχουν πέσει αισθητά.", "I'd be dishonest if I said nothing had changed. In technical texts, manuals, contracts, these tools already do very good work, and many colleagues now edit instead of translating. Their fees have fallen noticeably."),
  L("Δημοσιογράφος", "m", "Και στη λογοτεχνία;", "And in literature?"),
  L("Μεταφράστρια", "f", "Εκεί το πρόβλημα δεν είναι οι λέξεις, αλλά οι επιλογές. Ένα μυθιστόρημα έχει ρυθμό, ειρωνεία, σιωπές, λογοπαίγνια. Η μηχανή σού δίνει την πιο πιθανή απόδοση μιας φράσης, ενώ η καλή μετάφραση είναι συχνά η λιγότερο πιθανή, αυτή που τολμά. Μεταφράζοντας, παίρνω εκατοντάδες αποφάσεις σε κάθε σελίδα, και για καθεμιά από αυτές είμαι υπεύθυνη απέναντι στον συγγραφέα και στον αναγνώστη.", "There the problem isn't the words but the choices. A novel has rhythm, irony, silences, wordplay. The machine gives you the most probable rendering of a phrase, while a good translation is often the least probable one, the one that dares. When translating, I make hundreds of decisions on every page, and for each of them I am accountable to the author and to the reader."),
  L("Μεταφράστρια", "f", "Αυτό που με ανησυχεί περισσότερο δεν είναι η αντικατάσταση, αλλά η συνήθεια. Αν οι αναγνώστες συνηθίσουν σε κείμενα επίπεδα και «σωστά», ίσως πάψουν να ζητούν κάτι περισσότερο.", "What worries me most isn't replacement but habit. If readers get used to flat, 'correct' texts, they may stop asking for anything more."),
 ],
 "questions": [
  Q("Τι έχει αλλάξει, κατά τη μεταφράστρια, στα τεχνικά κείμενα;", ["Τίποτα", "Πολλοί μεταφραστές διορθώνουν πλέον αντί να μεταφράζουν και οι αμοιβές έπεσαν", "Οι αμοιβές αυξήθηκαν", "Δεν χρησιμοποιούνται πια εργαλεία"], 1, "πολλοί συνάδελφοι πλέον διορθώνουν αντί να μεταφράζουν"),
  Q("Ποια είναι, κατά τη γνώμη της, η διαφορά μηχανής και καλού μεταφραστή στη λογοτεχνία;", ["Η μηχανή κάνει περισσότερα γραμματικά λάθη", "Η μηχανή δίνει την πιο πιθανή απόδοση, ενώ η καλή μετάφραση συχνά τολμά", "Ο μεταφραστής είναι πιο γρήγορος", "Η μηχανή δεν ξέρει αρκετές λέξεις"], 1, "Η μηχανή σού δίνει την πιο πιθανή απόδοση μιας φράσης, ενώ η καλή μετάφραση είναι συχνά η λιγότερο πιθανή"),
  Q("Απέναντι σε ποιους νιώθει υπεύθυνη;", ["Απέναντι στον εκδότη μόνο", "Απέναντι στον συγγραφέα και στον αναγνώστη", "Απέναντι στους συναδέλφους της", "Απέναντι στους κριτικούς"], 1, "είμαι υπεύθυνη απέναντι στον συγγραφέα και στον αναγνώστη"),
  Q("Τι την ανησυχεί περισσότερο;", ["Ότι θα χάσει τη δουλειά της αύριο", "Ότι οι αναγνώστες θα συνηθίσουν σε επίπεδα κείμενα και θα πάψουν να ζητούν κάτι περισσότερο", "Ότι τα βιβλία θα ακριβύνουν", "Ότι οι συγγραφείς θα γράφουν στα αγγλικά"], 1, "Αν οι αναγνώστες συνηθίσουν σε κείμενα επίπεδα και «σωστά», ίσως πάψουν να ζητούν κάτι περισσότερο"),
 ],
 "gloss": {"μεταφράστρια": "μεταφράστρια — translator (female)", "αυτόματη": "αυτόματος — automatic", "επάγγελμά": "επάγγελμα — profession", "ανειλικρινής": "ανειλικρινής — insincere, dishonest", "εγχειρίδια": "εγχειρίδιο — manual", "συμβόλαια": "συμβόλαιο — contract", "συνάδελφοι": "συνάδελφος — colleague", "αμοιβές": "αμοιβή — fee", "αισθητά": "αισθητά — noticeably", "ειρωνεία": "ειρωνεία — irony", "λογοπαίγνια": "λογοπαίγνιο — pun, wordplay", "απόδοση": "απόδοση — rendering", "υπεύθυνη": "υπεύθυνος — responsible, accountable", "αντικατάσταση": "αντικατάσταση — replacement", "επίπεδα": "επίπεδος — flat"},
})

rnd = random.Random(20)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-20.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
