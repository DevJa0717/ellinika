# Source for library/listening/listening-17.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l17.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l17-ann-sinema", "title": "Βροχή στο θερινό σινεμά", "title_en": "Rain at the open-air cinema", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση σε έναν θερινό κινηματογράφο, λίγο πριν από την προβολή.",
 "script": [
  L("Υπάλληλος", "m", "Καλησπέρα σας. Λόγω της βροχής που αναμένεται μετά τις δέκα, η δεύτερη προβολή της ταινίας, στις δέκα και μισή, ακυρώνεται. Η πρώτη προβολή, στις εννιά, θα γίνει κανονικά, εκτός αν η βροχή αρχίσει νωρίτερα.", "Good evening. Because of the rain expected after ten, the second screening of the film, at half past ten, is cancelled. The first screening, at nine, will go ahead as normal, unless the rain starts earlier."),
  L("Υπάλληλος", "m", "Όσοι έχετε εισιτήριο για τη δεύτερη προβολή μπορείτε να το χρησιμοποιήσετε οποιαδήποτε βραδιά της εβδομάδας, για την ίδια ταινία, ή να πάρετε πίσω τα χρήματά σας από το ταμείο.", "Those of you with a ticket for the second screening can use it on any evening this week, for the same film, or get your money back at the box office."),
  L("Υπάλληλος", "m", "Αν η βροχή διακόψει την πρώτη προβολή πριν από τη μέση της ταινίας, θα σας δώσουμε ένα δωρεάν εισιτήριο. Το κυλικείο θα παραμείνει ανοιχτό κάτω από το στέγαστρο. Σας ευχαριστούμε για την κατανόηση.", "If the rain interrupts the first screening before the middle of the film, we will give you a free ticket. The snack bar will stay open under the canopy. Thank you for your understanding."),
 ],
 "questions": [
  Q("Τι ακυρώνεται απόψε;", ["Και οι δύο προβολές", "Η δεύτερη προβολή", "Η πρώτη προβολή", "Μόνο το κυλικείο"], 1, "η δεύτερη προβολή της ταινίας, στις δέκα και μισή, ακυρώνεται"),
  Q("Τι μπορούν να κάνουν όσοι έχουν εισιτήριο για τη δεύτερη προβολή;", ["Να μπουν στην πρώτη προβολή", "Να το χρησιμοποιήσουν άλλη βραδιά ή να πάρουν πίσω τα χρήματα", "Να δουν άλλη ταινία", "Τίποτα"], 1, "μπορείτε να το χρησιμοποιήσετε οποιαδήποτε βραδιά της εβδομάδας"),
  Q("Πότε θα πάρουν οι θεατές δωρεάν εισιτήριο;", ["Αν η βροχή διακόψει την ταινία πριν από τη μέση της", "Αν φύγουν νωρίς", "Αν αγοράσουν κάτι από το κυλικείο", "Σε κάθε περίπτωση"], 0, "Αν η βροχή διακόψει την πρώτη προβολή πριν από τη μέση της ταινίας"),
 ],
 "gloss": {"θερινό κινηματογράφο": "θερινός κινηματογράφος — open-air (summer) cinema", "προβολή": "προβολή — screening", "αναμένεται": "αναμένεται — is expected", "ακυρώνεται": "ακυρώνομαι — to be cancelled", "ταμείο": "ταμείο — box office, till", "διακόψει": "διακόπτω — to interrupt", "κυλικείο": "κυλικείο — snack bar", "στέγαστρο": "στέγαστρο — canopy, shelter", "κατανόηση": "κατανόηση — understanding"},
})

ITEMS.append({
 "id": "l17-vm-asfaleia", "title": "Μήνυμα από την ασφαλιστική", "title_en": "A message from the insurance company", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από μια ασφαλιστική εταιρεία προς μια οδηγό που είχε ένα μικρό ατύχημα.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα, κυρία Ζαχαρίου, σας καλώ από την ασφαλιστική σας εταιρεία σχετικά με το τρακάρισμα της περασμένης Τρίτης. Λάβαμε τη δήλωση ατυχήματος που συμπληρώσατε με τον άλλο οδηγό, και από ό,τι φαίνεται η ευθύνη είναι εξ ολοκλήρου δική του.", "Good morning, Mrs Zachariou, I'm calling from your insurance company about last Tuesday's collision. We've received the accident report you filled in with the other driver, and it appears the fault is entirely his."),
  L("Υπάλληλος", "m", "Αυτό σημαίνει ότι η ζημιά στο αυτοκίνητό σας θα καλυφθεί από τη δική του ασφάλεια και δεν θα επηρεαστεί η δική σας κατηγορία. Ένας πραγματογνώμονας θα έρθει να δει το αυτοκίνητο την Πέμπτη, μεταξύ δέκα και δώδεκα· παρακαλώ να μην το επισκευάσετε πριν από την επίσκεψή του.", "This means the damage to your car will be covered by his insurance and your own rating will not be affected. An assessor will come to see the car on Thursday, between ten and twelve; please don't have it repaired before his visit."),
  L("Υπάλληλος", "m", "Αν χρειάζεστε αυτοκίνητο στο μεταξύ, το συμβόλαιό σας περιλαμβάνει όχημα αντικατάστασης για πέντε μέρες. Πάρτε μας στο κέντρο εξυπηρέτησης για να το κανονίσουμε.", "If you need a car in the meantime, your policy includes a replacement vehicle for five days. Call our service centre so we can arrange it."),
 ],
 "questions": [
  Q("Ποιος ευθύνεται για το ατύχημα, σύμφωνα με την ασφαλιστική;", ["Η κυρία Ζαχαρίου", "Ο άλλος οδηγός", "Και οι δύο", "Δεν έχει αποφασιστεί ακόμη"], 1, "η ευθύνη είναι εξ ολοκλήρου δική του"),
  Q("Τι δεν πρέπει να κάνει η κυρία Ζαχαρίου πριν από την Πέμπτη;", ["Να οδηγήσει το αυτοκίνητο", "Να επισκευάσει το αυτοκίνητο", "Να μιλήσει με τον άλλο οδηγό", "Να πάει στην αστυνομία"], 1, "παρακαλώ να μην το επισκευάσετε πριν από την επίσκεψή του"),
  Q("Τι περιλαμβάνει το συμβόλαιό της;", ["Δωρεάν επισκευή", "Όχημα αντικατάστασης για πέντε μέρες", "Ταξί για μία εβδομάδα", "Έκπτωση στο επόμενο συμβόλαιο"], 1, "το συμβόλαιό σας περιλαμβάνει όχημα αντικατάστασης για πέντε μέρες"),
 ],
 "gloss": {"ασφαλιστική εταιρεία": "ασφαλιστική εταιρεία — insurance company", "ατύχημα": "ατύχημα — accident", "τρακάρισμα": "τρακάρισμα — (car) crash, collision", "δήλωση ατυχήματος": "δήλωση ατυχήματος — accident report", "ευθύνη": "ευθύνη — fault, liability", "εξ ολοκλήρου": "εξ ολοκλήρου — entirely", "ζημιά": "ζημιά — damage", "θα καλυφθεί": "καλύπτομαι — to be covered", "πραγματογνώμονας": "πραγματογνώμονας — (insurance) assessor", "να μην το επισκευάσετε": "επισκευάζω — to repair", "συμβόλαιό": "συμβόλαιο — (insurance) policy, contract", "όχημα αντικατάστασης": "όχημα αντικατάστασης — replacement vehicle"},
})

ITEMS.append({
 "id": "l17-dia-sideradiko", "title": "Στο σιδεράδικο", "title_en": "At the hardware shop", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα κατάστημα με είδη κιγκαλερίας ανάμεσα σε έναν πελάτη και τον πωλητή.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Η βρύση της κουζίνας στάζει εδώ και μία εβδομάδα, και ο υδραυλικός μου είπε ότι δεν μπορεί να έρθει πριν από τον άλλο μήνα. Σκέφτομαι να τη φτιάξω μόνος μου.", "Good morning. The kitchen tap has been dripping for a week, and the plumber told me he can't come before next month. I'm thinking of fixing it myself."),
  L("Πωλητής", "m", "Τις περισσότερες φορές φταίει η φλάντζα ή ο μηχανισμός μέσα στη βρύση. Ξέρετε τι μάρκα είναι; Αν μου φέρετε το παλιό ανταλλακτικό, θα σας δώσω ακριβώς το ίδιο.", "Most of the time it's the washer or the cartridge inside the tap. Do you know what brand it is? If you bring me the old part, I'll give you exactly the same one."),
  L("Πελάτης", "m", "Δεν ξέρω καν πώς να το βγάλω. Χρειάζομαι κάποιο ειδικό εργαλείο;", "I don't even know how to take it out. Do I need a special tool?"),
  L("Πωλητής", "m", "Ένα γαλλικό κλειδί και ένα κατσαβίδι αρκούν. Το σημαντικότερο: πριν ξεκινήσετε, κλείστε τον γενικό διακόπτη του νερού, αλλιώς θα πλημμυρίσετε την κουζίνα. Και βάλτε μια πετσέτα στον νεροχύτη, για να μη σας πέσουν τα μικρά κομμάτια στην αποχέτευση.", "An adjustable spanner and a screwdriver are enough. Most important: before you start, turn off the main water valve, otherwise you'll flood the kitchen. And put a towel in the sink, so the small pieces don't fall down the drain."),
 ],
 "questions": [
  Q("Γιατί θέλει ο πελάτης να φτιάξει μόνος του τη βρύση;", ["Γιατί ο υδραυλικός είναι πολύ ακριβός", "Γιατί ο υδραυλικός δεν μπορεί να έρθει πριν από τον άλλο μήνα", "Γιατί είναι υδραυλικός", "Γιατί η βρύση είναι καινούργια"], 1, "ο υδραυλικός μου είπε ότι δεν μπορεί να έρθει πριν από τον άλλο μήνα"),
  Q("Τι προτείνει ο πωλητής για το ανταλλακτικό;", ["Να αγοράσει καινούργια βρύση", "Να του φέρει το παλιό ανταλλακτικό", "Να το παραγγείλει από το διαδίκτυο", "Να ρωτήσει τον υδραυλικό"], 1, "Αν μου φέρετε το παλιό ανταλλακτικό, θα σας δώσω ακριβώς το ίδιο"),
  Q("Ποιο είναι το σημαντικότερο πριν από την επισκευή;", ["Να αγοράσει ειδικό εργαλείο", "Να κλείσει τον γενικό διακόπτη του νερού", "Να αδειάσει τον νεροχύτη", "Να διαβάσει τις οδηγίες"], 1, "κλείστε τον γενικό διακόπτη του νερού"),
 ],
 "gloss": {"είδη κιγκαλερίας": "είδη κιγκαλερίας — hardware (goods)", "βρύση": "βρύση — tap", "στάζει": "στάζω — to drip", "υδραυλικός": "υδραυλικός — plumber", "φλάντζα": "φλάντζα — washer, seal", "ανταλλακτικό": "ανταλλακτικό — spare part", "γαλλικό κλειδί": "γαλλικό κλειδί — adjustable spanner", "κατσαβίδι": "κατσαβίδι — screwdriver", "γενικό διακόπτη του νερού": "γενικός διακόπτης του νερού — main water valve", "θα πλημμυρίσετε": "πλημμυρίζω — to flood", "νεροχύτη": "νεροχύτης — sink", "αποχέτευση": "αποχέτευση — drain"},
})

ITEMS.append({
 "id": "l17-dia-oreivasia", "title": "Πεζοπορία το Σάββατο", "title_en": "A hike on Saturday", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε δύο φίλους να σχεδιάζουν μια πεζοπορία στο βουνό.",
 "script": [
  L("Λευτέρης", "m", "Λοιπόν, για το Σάββατο σκέφτηκα τη διαδρομή από το χωριό ως το φαράγγι. Είναι περίπου πέντε ώρες με επιστροφή, χωρίς πολλές ανηφόρες.", "So, for Saturday I thought of the route from the village to the gorge. It's about five hours there and back, without many climbs."),
  L("Χαρά", "f", "Ωραία, αλλά είδες την πρόγνωση; Λέει για καταιγίδες το απόγευμα. Δεν θα ήθελα να μας πιάσει η βροχή μέσα στο φαράγγι, εκεί το νερό ανεβαίνει πολύ γρήγορα.", "Nice, but did you see the forecast? It says storms in the afternoon. I wouldn't want the rain to catch us inside the gorge; the water rises very fast there."),
  L("Λευτέρης", "m", "Δίκιο έχεις. Τότε να ξεκινήσουμε στις έξι το πρωί, για να έχουμε γυρίσει ως τις δώδεκα. Θα πάρουμε και αδιάβροχα για καλό και για κακό.", "You're right. Then let's start at six in the morning, so we're back by twelve. We'll take raincoats too, just in case."),
  L("Χαρά", "f", "Συμφωνώ. Και να πούμε σε κάποιον πού πάμε και τι ώρα υπολογίζουμε να γυρίσουμε. Στο φαράγγι δεν έχει σήμα το κινητό.", "Agreed. And let's tell someone where we're going and what time we expect to be back. There's no phone signal in the gorge."),
 ],
 "questions": [
  Q("Τι ανησυχεί τη Χαρά;", ["Ότι η διαδρομή είναι πολύ μεγάλη", "Ότι προβλέπονται καταιγίδες το απόγευμα", "Ότι δεν έχει παπούτσια πεζοπορίας", "Ότι το φαράγγι είναι κλειστό"], 1, "Λέει για καταιγίδες το απόγευμα"),
  Q("Τι αποφασίζουν να κάνουν;", ["Να αναβάλουν την πεζοπορία", "Να ξεκινήσουν νωρίς για να γυρίσουν ως το μεσημέρι", "Να πάνε με αυτοκίνητο", "Να αλλάξουν διαδρομή"], 1, "να ξεκινήσουμε στις έξι το πρωί, για να έχουμε γυρίσει ως τις δώδεκα"),
  Q("Γιατί θέλει η Χαρά να ενημερώσουν κάποιον;", ["Γιατί θέλει να έρθει κι άλλος", "Γιατί στο φαράγγι δεν έχει σήμα το κινητό", "Γιατί το απαιτεί ο νόμος", "Γιατί δεν ξέρουν τον δρόμο"], 1, "Στο φαράγγι δεν έχει σήμα το κινητό"),
 ],
 "gloss": {"πεζοπορία": "πεζοπορία — hike, hiking", "διαδρομή": "διαδρομή — route", "φαράγγι": "φαράγγι — gorge", "ανηφόρες": "ανηφόρα — uphill climb", "πρόγνωση": "πρόγνωση — (weather) forecast", "καταιγίδες": "καταιγίδα — storm", "να μας πιάσει η βροχή": "μας πιάνει η βροχή — to get caught in the rain", "αδιάβροχα": "αδιάβροχο — raincoat", "για καλό και για κακό": "για καλό και για κακό — just in case", "υπολογίζουμε": "υπολογίζω — to reckon, expect", "σήμα": "σήμα — (phone) signal"},
})

ITEMS.append({
 "id": "l17-mon-avstralia", "title": "Ο παππούς μου στη Μελβούρνη", "title_en": "My grandfather in Melbourne", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια νέα γυναίκα να μιλάει για τον παππού της, που μετανάστευσε στην Αυστραλία.",
 "script": [
  L("Σοφία", "f", "Ο παππούς μου έφυγε από ένα χωριό της Αρκαδίας το 1956, στα δεκαεννιά του, με ένα πλοίο που έκανε σχεδόν έναν μήνα για να φτάσει στη Μελβούρνη. Δεν ήξερε λέξη αγγλικά και είχε στην τσέπη του μόνο τη διεύθυνση ενός ξαδέρφου.", "My grandfather left a village in Arcadia in 1956, at nineteen, on a ship that took almost a month to reach Melbourne. He didn't know a word of English and had in his pocket only the address of a cousin."),
  L("Σοφία", "f", "Τα πρώτα χρόνια δούλευε σε ένα εργοστάσιο αυτοκινήτων, σε βάρδιες δώδεκα ωρών, και τα βράδια έστελνε γράμματα στη μάνα του. Αργότερα άνοιξε με τη γιαγιά μου ένα μικρό μπακάλικο, που έγινε σημείο συνάντησης για τους Έλληνες της γειτονιάς.", "In the early years he worked at a car factory, in twelve-hour shifts, and in the evenings he sent letters to his mother. Later he opened a small grocery shop with my grandmother, which became a meeting place for the Greeks of the neighbourhood."),
  L("Σοφία", "f", "Εγώ γεννήθηκα στη Μελβούρνη, αλλά στο σπίτι μιλούσαμε μόνο ελληνικά και τα Σάββατα πήγαινα στο ελληνικό σχολείο. Όταν πέρσι ήρθα για πρώτη φορά στο χωριό του, οι γέροι στο καφενείο τον θυμούνταν ακόμη. Ένιωσα ότι έκλεισε ένας κύκλος.", "I was born in Melbourne, but at home we spoke only Greek and on Saturdays I went to Greek school. When I came to his village for the first time last year, the old men in the café still remembered him. I felt a circle had closed."),
 ],
 "questions": [
  Q("Τι είχε μαζί του ο παππούς όταν έφτασε στη Μελβούρνη;", ["Πολλά χρήματα", "Ένα συμβόλαιο εργασίας", "Μόνο τη διεύθυνση ενός ξαδέρφου", "Ένα λεξικό αγγλικών"], 2, "είχε στην τσέπη του μόνο τη διεύθυνση ενός ξαδέρφου"),
  Q("Τι έγινε το μπακάλικο του παππού;", ["Μια μεγάλη αλυσίδα", "Σημείο συνάντησης για τους Έλληνες της γειτονιάς", "Ένα εστιατόριο", "Ένα εργοστάσιο"], 1, "έγινε σημείο συνάντησης για τους Έλληνες της γειτονιάς"),
  Q("Τι ένιωσε η Σοφία όταν επισκέφτηκε το χωριό;", ["Απογοήτευση", "Ότι έκλεισε ένας κύκλος", "Ότι δεν την καταλάβαιναν", "Ότι ήθελε να γυρίσει αμέσως"], 1, "Ένιωσα ότι έκλεισε ένας κύκλος"),
 ],
 "gloss": {"μετανάστευσε": "μεταναστεύω — to emigrate", "ξαδέρφου": "ξάδερφος — cousin", "εργοστάσιο": "εργοστάσιο — factory", "βάρδιες": "βάρδια — shift", "μπακάλικο": "μπακάλικο — grocery shop", "σημείο συνάντησης": "σημείο συνάντησης — meeting place", "γέροι": "γέρος — old man", "θυμούνταν": "θυμάμαι — to remember", "έκλεισε ένας κύκλος": "κλείνει ένας κύκλος — a circle closes"},
})

ITEMS.append({
 "id": "l17-rep-tinos", "title": "Οι μαρμαράδες της Τήνου", "title_en": "The marble carvers of Tinos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από τον Πύργο, ένα χωριό της Τήνου.",
 "script": [
  L("Δημοσιογράφος", "f", "Στον Πύργο της Τήνου, ο ήχος του σφυριού πάνω στο μάρμαρο ακούγεται από τα πρώτα σπίτια του χωριού. Εδώ η μαρμαροτεχνία είναι ζωντανή εδώ και αιώνες, και το 2015 η UNESCO την ενέγραψε στον κατάλογο της άυλης πολιτιστικής κληρονομιάς.", "In Pyrgos on Tinos, the sound of the hammer on marble can be heard from the first houses of the village. Here marble craftsmanship has been alive for centuries, and in 2015 UNESCO inscribed it on the list of intangible cultural heritage."),
  L("Δημοσιογράφος", "f", "Στα σοκάκια θα δείτε παντού δείγματα της τέχνης: ανάγλυφα υπέρθυρα πάνω από τις πόρτες, βρύσες, καμπαναριά και τους περίφημους περιστεριώνες. Από τον Πύργο κατάγονταν και σπουδαίοι γλύπτες, όπως ο Γιαννούλης Χαλεπάς, του οποίου το σπίτι λειτουργεί σήμερα ως μουσείο.", "In the alleys you will see examples of the craft everywhere: carved lintels above doors, fountains, bell towers and the famous dovecotes. Great sculptors came from Pyrgos too, such as Yannoulis Chalepas, whose house operates today as a museum."),
  L("Δημοσιογράφος", "f", "Στη Σχολή Καλών Τεχνών του χωριού, νέοι από όλη την Ελλάδα μαθαίνουν να δουλεύουν το μάρμαρο με τα παραδοσιακά εργαλεία. Οι δάσκαλοι λένε ότι χρειάζονται τουλάχιστον τρία χρόνια για να μάθει κανείς τα βασικά, και μια ολόκληρη ζωή για να γίνει μάστορας.", "At the village's School of Fine Arts, young people from all over Greece learn to work marble with traditional tools. The teachers say it takes at least three years to learn the basics, and a whole lifetime to become a master."),
 ],
 "questions": [
  Q("Τι έγινε το 2015;", ["Άνοιξε η Σχολή Καλών Τεχνών", "Η UNESCO ενέγραψε τη μαρμαροτεχνία της Τήνου στην άυλη κληρονομιά", "Έκλεισαν τα λατομεία", "Ιδρύθηκε το μουσείο Χαλεπά"], 1, "το 2015 η UNESCO την ενέγραψε στον κατάλογο της άυλης πολιτιστικής κληρονομιάς"),
  Q("Ποιο από τα παρακάτω ΔΕΝ αναφέρεται ως δείγμα της τέχνης στα σοκάκια;", ["Τα ανάγλυφα υπέρθυρα", "Οι βρύσες", "Τα αγάλματα θεών", "Οι περιστεριώνες"], 2, "ανάγλυφα υπέρθυρα πάνω από τις πόρτες, βρύσες, καμπαναριά και τους περίφημους περιστεριώνες"),
  Q("Πόσο χρόνο χρειάζεται κανείς για να μάθει τα βασικά;", ["Μερικούς μήνες", "Τουλάχιστον τρία χρόνια", "Μια ολόκληρη ζωή", "Ένα καλοκαίρι"], 1, "χρειάζονται τουλάχιστον τρία χρόνια για να μάθει κανείς τα βασικά"),
 ],
 "gloss": {"σφυριού": "σφυρί — hammer", "μάρμαρο": "μάρμαρο — marble", "μαρμαροτεχνία": "μαρμαροτεχνία — marble craftsmanship", "ενέγραψε": "εγγράφω — to inscribe, enrol", "ανάγλυφα": "ανάγλυφος — carved in relief", "υπέρθυρα": "υπέρθυρο — lintel, fanlight", "καμπαναριά": "καμπαναριό — bell tower", "περιστεριώνες": "περιστεριώνας — dovecote", "γλύπτες": "γλύπτης — sculptor", "Σχολή Καλών Τεχνών": "Σχολή Καλών Τεχνών — School of Fine Arts", "μάστορας": "μάστορας — master craftsman"},
})

ITEMS.append({
 "id": "l17-rep-apolithomeno", "title": "Το απολιθωμένο δάσος της Λέσβου", "title_en": "The petrified forest of Lesvos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από το απολιθωμένο δάσος, στη δυτική Λέσβο.",
 "script": [
  L("Δημοσιογράφος", "m", "Κοντά στο Σίγρι, στη δυτική Λέσβο, κορμοί δέντρων στέκονται όρθιοι μέσα σε ένα ξερό τοπίο. Δεν είναι όμως από ξύλο, αλλά από πέτρα. Πριν από περίπου είκοσι εκατομμύρια χρόνια, ηφαιστειακές εκρήξεις έθαψαν ένα ολόκληρο δάσος κάτω από στάχτη.", "Near Sigri, in western Lesvos, tree trunks stand upright in a dry landscape. They are not made of wood, however, but of stone. About twenty million years ago, volcanic eruptions buried an entire forest under ash."),
  L("Γεωλόγος", "f", "Η στάχτη προστάτεψε τα δέντρα από την αποσύνθεση. Με τον καιρό, το νερό που κυκλοφορούσε στο έδαφος αντικατέστησε σιγά σιγά το ξύλο με διοξείδιο του πυριτίου, διατηρώντας όμως τη δομή του. Σε κάποιους κορμούς μπορούμε ακόμη να μετρήσουμε τους δακτυλίους.", "The ash protected the trees from decomposition. Over time, water circulating in the ground gradually replaced the wood with silica, while preserving its structure. On some trunks we can still count the rings."),
  L("Δημοσιογράφος", "m", "Η περιοχή έχει χαρακτηριστεί Παγκόσμιο Γεωπάρκο της UNESCO, και στο Μουσείο Φυσικής Ιστορίας του Σιγρίου ο επισκέπτης μπορεί να δει κορμούς, φύλλα και καρπούς που βρέθηκαν στις ανασκαφές. Οι επιστήμονες λένε ότι τα απολιθώματα δείχνουν πως το κλίμα της Λέσβου ήταν κάποτε υποτροπικό.", "The area has been designated a UNESCO Global Geopark, and at the Natural History Museum in Sigri visitors can see trunks, leaves and fruits found in the excavations. Scientists say the fossils show that the climate of Lesvos was once subtropical."),
 ],
 "questions": [
  Q("Τι προκάλεσε την απολίθωση του δάσους;", ["Ένας σεισμός", "Ηφαιστειακές εκρήξεις που έθαψαν το δάσος κάτω από στάχτη", "Μια πλημμύρα", "Μια πυρκαγιά"], 1, "ηφαιστειακές εκρήξεις έθαψαν ένα ολόκληρο δάσος κάτω από στάχτη"),
  Q("Τι μπορούμε να δούμε ακόμη σε κάποιους κορμούς;", ["Τα φύλλα τους", "Τους δακτυλίους τους", "Τα χρώματα του ξύλου", "Φωλιές πουλιών"], 1, "Σε κάποιους κορμούς μπορούμε ακόμη να μετρήσουμε τους δακτυλίους"),
  Q("Τι δείχνουν τα απολιθώματα για το κλίμα της Λέσβου;", ["Ότι ήταν πάντα ξηρό", "Ότι ήταν κάποτε υποτροπικό", "Ότι ήταν πολικό", "Ότι δεν έχει αλλάξει"], 1, "το κλίμα της Λέσβου ήταν κάποτε υποτροπικό"),
 ],
 "gloss": {"απολιθωμένο": "απολιθωμένος — petrified", "κορμοί": "κορμός — trunk", "όρθιοι": "όρθιος — upright, standing", "ηφαιστειακές εκρήξεις": "ηφαιστειακή έκρηξη — volcanic eruption", "έθαψαν": "θάβω — to bury", "στάχτη": "στάχτη — ash", "αποσύνθεση": "αποσύνθεση — decomposition", "διοξείδιο του πυριτίου": "διοξείδιο του πυριτίου — silica", "δομή": "δομή — structure", "δακτυλίους": "δακτύλιος — (tree) ring", "Γεωπάρκο": "γεωπάρκο — geopark", "απολιθώματα": "απολίθωμα — fossil", "υποτροπικό": "υποτροπικός — subtropical"},
})

ITEMS.append({
 "id": "l17-int-krokos", "title": "Ο κρόκος της Κοζάνης", "title_en": "Saffron from Kozani", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν νέο παραγωγό κρόκου στη Δυτική Μακεδονία.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Τσιούρη, ο κρόκος Κοζάνης θεωρείται από τους καλύτερους στον κόσμο. Πώς είναι η συγκομιδή;", "Mr Tsiouris, Kozani saffron is considered among the best in the world. What is the harvest like?"),
  L("Παραγωγός", "m", "Είναι μια δουλειά που δεν μπορεί να γίνει με μηχανές. Τον Οκτώβριο και τον Νοέμβριο, τα λουλούδια ανοίγουν σχεδόν όλα μαζί, και πρέπει να τα μαζέψουμε με το χέρι πολύ νωρίς το πρωί, πριν ανοίξουν εντελώς από τον ήλιο. Μετά, το βράδυ, όλη η οικογένεια κάθεται γύρω από το τραπέζι και ξεχωρίζει τα στίγματα, τις τρεις κόκκινες ίνες κάθε λουλουδιού.", "It's a job that can't be done with machines. In October and November, the flowers open almost all at once, and we must pick them by hand very early in the morning, before they open fully in the sun. Then, in the evening, the whole family sits around the table and separates the stigmas, the three red threads of each flower."),
  L("Δημοσιογράφος", "f", "Γι' αυτό είναι τόσο ακριβός;", "Is that why it's so expensive?"),
  L("Παραγωγός", "m", "Ακριβώς. Για ένα κιλό αποξηραμένου κρόκου χρειάζονται περίπου εκατόν πενήντα χιλιάδες λουλούδια. Όλη η παραγωγή περνά από τον συνεταιρισμό, που ελέγχει την ποιότητα και την πουλά σε όλο τον κόσμο. Τα τελευταία χρόνια, πολλοί νέοι επιστρέφουν στην καλλιέργεια, γιατί ο κρόκος δεν χρειάζεται πολύ νερό και αντέχει στην ξηρασία.", "Exactly. For one kilo of dried saffron, about one hundred and fifty thousand flowers are needed. All production goes through the cooperative, which checks the quality and sells it all over the world. In recent years, many young people are returning to the crop, because saffron doesn't need much water and withstands drought."),
 ],
 "questions": [
  Q("Πότε μαζεύουν τα λουλούδια του κρόκου;", ["Το καλοκαίρι, το μεσημέρι", "Τον Οκτώβριο και τον Νοέμβριο, νωρίς το πρωί", "Την άνοιξη, το βράδυ", "Όλο τον χρόνο"], 1, "Τον Οκτώβριο και τον Νοέμβριο"),
  Q("Γιατί είναι ακριβός ο κρόκος;", ["Γιατί εισάγεται", "Γιατί για ένα κιλό χρειάζονται περίπου 150.000 λουλούδια", "Γιατί καλλιεργείται σε θερμοκήπια", "Γιατί η παραγωγή είναι μηχανική"], 1, "Για ένα κιλό αποξηραμένου κρόκου χρειάζονται περίπου εκατόν πενήντα χιλιάδες λουλούδια"),
  Q("Γιατί επιστρέφουν πολλοί νέοι στην καλλιέργεια;", ["Γιατί πήραν επιδότηση", "Γιατί ο κρόκος δεν χρειάζεται πολύ νερό και αντέχει στην ξηρασία", "Γιατί η δουλειά είναι εύκολη", "Γιατί έκλεισαν τα εργοστάσια"], 1, "ο κρόκος δεν χρειάζεται πολύ νερό και αντέχει στην ξηρασία"),
 ],
 "gloss": {"κρόκου": "κρόκος — saffron (crocus)", "συγκομιδή": "συγκομιδή — harvest", "μηχανές": "μηχανή — machine", "ξεχωρίζει": "ξεχωρίζω — to separate", "στίγματα": "στίγμα — stigma (of a flower)", "ίνες": "ίνα — fibre, thread", "αποξηραμένου": "αποξηραμένος — dried", "συνεταιρισμό": "συνεταιρισμός — cooperative", "καλλιέργεια": "καλλιέργεια — cultivation, crop", "ξηρασία": "ξηρασία — drought"},
})

ITEMS.append({
 "id": "l17-mon-omiros", "title": "Πώς γεννήθηκαν τα ομηρικά έπη", "title_en": "How the Homeric epics were born", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για την προφορική παράδοση των ομηρικών επών.",
 "script": [
  L("Φιλόλογος", "f", "Γιατί στην «Ιλιάδα» η Αυγή είναι πάντα «ροδοδάχτυλη» και ο Αχιλλέας «γοργοπόδαρος», ακόμη κι όταν κάθεται; Για αιώνες οι μελετητές θεωρούσαν αυτά τα επίθετα απλά στολίδια. Τη δεκαετία του 1920, ένας νεαρός Αμερικανός φιλόλογος, ο Μίλμαν Πάρι, πρότεινε μια διαφορετική εξήγηση.", "Why in the 'Iliad' is Dawn always 'rosy-fingered' and Achilles 'swift-footed', even when he is sitting down? For centuries scholars considered these epithets mere ornaments. In the 1920s, a young American philologist, Milman Parry, proposed a different explanation."),
  L("Φιλόλογος", "f", "Ο Πάρι έδειξε ότι οι φράσεις αυτές, οι λεγόμενοι «τύποι», ταιριάζουν ακριβώς σε συγκεκριμένα σημεία του δακτυλικού εξάμετρου. Ήταν, δηλαδή, εργαλεία ενός ποιητή που συνέθετε την ώρα που τραγουδούσε, χωρίς γραφή. Για να ελέγξει την υπόθεσή του, ταξίδεψε στη Γιουγκοσλαβία και ηχογράφησε αγράμματους λαϊκούς τραγουδιστές που αυτοσχεδίαζαν επικά τραγούδια χιλιάδων στίχων, χρησιμοποιώντας ακριβώς τέτοιους τύπους.", "Parry showed that these phrases, the so-called 'formulas', fit exactly into specific positions of the dactylic hexameter. They were, in other words, the tools of a poet composing as he sang, without writing. To test his hypothesis, he travelled to Yugoslavia and recorded illiterate folk singers who improvised epic songs thousands of lines long, using exactly such formulas."),
  L("Φιλόλογος", "f", "Η θεωρία του άλλαξε ριζικά τον τρόπο που διαβάζουμε τον Όμηρο. Τα έπη δεν είναι πια έργο ενός μοναχικού συγγραφέα, αλλά καρπός μιας μακραίωνης προφορικής παράδοσης. Το ερώτημα πότε και πώς καταγράφηκαν, και ποιος ήταν τελικά ο «Όμηρος», παραμένει, πάντως, ανοιχτό.", "His theory radically changed the way we read Homer. The epics are no longer the work of a solitary author, but the fruit of a centuries-long oral tradition. The question of when and how they were written down, and who 'Homer' ultimately was, nevertheless remains open."),
 ],
 "questions": [
  Q("Πώς θεωρούσαν παλιότερα οι μελετητές τα σταθερά επίθετα του Ομήρου;", ["Ως λάθη των αντιγραφέων", "Ως απλά στολίδια", "Ως ονόματα θεών", "Ως μεταγενέστερες προσθήκες"], 1, "Για αιώνες οι μελετητές θεωρούσαν αυτά τα επίθετα απλά στολίδια"),
  Q("Τι έδειξε ο Πάρι για τους «τύπους»;", ["Ότι γράφτηκαν από διαφορετικούς ποιητές", "Ότι ήταν εργαλεία για να συνθέτει ο ποιητής ενώ τραγουδούσε", "Ότι προέρχονταν από τη Γιουγκοσλαβία", "Ότι δεν ταιριάζουν στο μέτρο"], 1, "Ήταν, δηλαδή, εργαλεία ενός ποιητή που συνέθετε την ώρα που τραγουδούσε"),
  Q("Ποιο ερώτημα παραμένει ανοιχτό, σύμφωνα με την ομιλήτρια;", ["Αν ο Πάρι είχε δίκιο", "Πότε και πώς καταγράφηκαν τα έπη και ποιος ήταν ο Όμηρος", "Αν τα έπη ήταν προφορικά", "Πόσους στίχους έχει η «Ιλιάδα»"], 1, "Το ερώτημα πότε και πώς καταγράφηκαν, και ποιος ήταν τελικά ο «Όμηρος», παραμένει, πάντως, ανοιχτό"),
 ],
 "gloss": {"ομηρικών επών": "ομηρικά έπη — the Homeric epics", "προφορική παράδοση": "προφορική παράδοση — oral tradition", "ροδοδάχτυλη": "ροδοδάχτυλος — rosy-fingered", "γοργοπόδαρος": "γοργοπόδαρος — swift-footed", "μελετητές": "μελετητής — scholar", "επίθετα": "επίθετο — epithet; adjective", "στολίδια": "στολίδι — ornament", "φιλόλογος": "φιλόλογος — philologist", "τύποι": "τύπος — formula; type", "δακτυλικού εξάμετρου": "δακτυλικό εξάμετρο — dactylic hexameter", "συνέθετε": "συνθέτω — to compose", "αγράμματους": "αγράμματος — illiterate", "αυτοσχεδίαζαν": "αυτοσχεδιάζω — to improvise", "στίχων": "στίχος — line (of verse)", "μακραίωνης": "μακραίωνος — centuries-long", "καταγράφηκαν": "καταγράφομαι — to be written down, recorded"},
})

ITEMS.append({
 "id": "l17-int-akropoli", "title": "Πόσους επισκέπτες αντέχει η Ακρόπολη;", "title_en": "How many visitors can the Acropolis take?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια αρχαιολόγο για τον υπερτουρισμό στους αρχαιολογικούς χώρους.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Δρόσου, από το 2023 η είσοδος στην Ακρόπολη γίνεται με ωριαίες ζώνες και υπάρχει ημερήσιο όριο επισκεπτών. Ήταν απαραίτητο;", "Ms Drosou, since 2023 entry to the Acropolis has been by hourly time slots and there is a daily visitor limit. Was it necessary?"),
  L("Αρχαιολόγος", "f", "Απολύτως. Τους καλοκαιρινούς μήνες, χιλιάδες άνθρωποι στριμώχνονταν ταυτόχρονα στα Προπύλαια, κάτω από τον καυτό ήλιο. Δεν ήταν μόνο θέμα ασφάλειας για τους επισκέπτες· η συνεχής τριβή φθείρει τα μάρμαρα, και τα σκαλοπάτια έχουν γυαλίσει τόσο που γλιστράνε. Ένα μνημείο δεν είναι λούνα παρκ.", "Absolutely. In the summer months, thousands of people were crowding into the Propylaea at the same time, under the scorching sun. It wasn't only a safety issue for visitors; the constant friction wears down the marble, and the steps have become so polished that they're slippery. A monument is not a fun fair."),
  L("Δημοσιογράφος", "m", "Δεν υπάρχει κίνδυνος να γίνουν τα μνημεία προνόμιο όσων προλαβαίνουν να κλείσουν θέση;", "Isn't there a risk that monuments become the privilege of those who manage to book a slot in time?"),
  L("Αρχαιολόγος", "f", "Είναι ένας εύλογος προβληματισμός. Γι' αυτό πιστεύω ότι το όριο πρέπει να συνδυάζεται με μέτρα που διασπείρουν τους επισκέπτες: λιγότερο γνωστοί χώροι, όπως η αρχαία Αγορά ή ο Κεραμεικός, βρίσκονται σε απόσταση λίγων λεπτών και είναι σχεδόν άδειοι. Ο στόχος δεν είναι να αποκλείσουμε τον κόσμο, αλλά να του δώσουμε την ευκαιρία να ζήσει την εμπειρία με αξιοπρέπεια.", "That's a reasonable concern. That's why I believe the limit must be combined with measures that spread visitors out: lesser-known sites, such as the ancient Agora or the Kerameikos, are a few minutes away and almost empty. The aim isn't to exclude people, but to give them the chance to have the experience with dignity."),
 ],
 "questions": [
  Q("Τι άλλαξε στην είσοδο της Ακρόπολης από το 2023;", ["Έγινε δωρεάν", "Γίνεται με ωριαίες ζώνες και ημερήσιο όριο", "Κλείνει τα καλοκαίρια", "Επιτρέπεται μόνο με ξεναγό"], 1, "η είσοδος στην Ακρόπολη γίνεται με ωριαίες ζώνες και υπάρχει ημερήσιο όριο επισκεπτών"),
  Q("Ποιο πρόβλημα για τα ίδια τα μνημεία αναφέρει η αρχαιολόγος;", ["Τα γκράφιτι", "Τη φθορά των μαρμάρων από τη συνεχή τριβή", "Την ατμοσφαιρική ρύπανση", "Τους σεισμούς"], 1, "η συνεχής τριβή φθείρει τα μάρμαρα"),
  Q("Τι προτείνει για να μη γίνουν τα μνημεία προνόμιο λίγων;", ["Να καταργηθεί το όριο", "Να αυξηθούν οι τιμές", "Να διασπαρούν οι επισκέπτες σε λιγότερο γνωστούς χώρους", "Να ανοίγει η Ακρόπολη και τη νύχτα"], 2, "το όριο πρέπει να συνδυάζεται με μέτρα που διασπείρουν τους επισκέπτες"),
 ],
 "gloss": {"υπερτουρισμό": "υπερτουρισμός — overtourism", "αρχαιολογικούς χώρους": "αρχαιολογικός χώρος — archaeological site", "ωριαίες ζώνες": "ωριαία ζώνη — hourly time slot", "ημερήσιο όριο": "ημερήσιο όριο — daily limit", "στριμώχνονταν": "στριμώχνομαι — to crowd, squeeze", "Προπύλαια": "Προπύλαια — the Propylaea (gateway of the Acropolis)", "καυτό": "καυτός — scorching", "τριβή": "τριβή — friction, wear", "φθείρει": "φθείρω — to wear down", "γλιστράνε": "γλιστράω — to be slippery, slip", "προνόμιο": "προνόμιο — privilege", "εύλογος προβληματισμός": "εύλογος προβληματισμός — reasonable concern", "διασπείρουν": "διασπείρω — to spread out, disperse", "Κεραμεικός": "Κεραμεικός — the Kerameikos (ancient cemetery of Athens)", "αξιοπρέπεια": "αξιοπρέπεια — dignity"},
})

rnd = random.Random(17)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-17.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
