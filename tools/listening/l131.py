# Source for library/listening/listening-131.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l131.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l131-ann-ekthesi-vivliou", "title": "Ανακοίνωση στην έκθεση βιβλίου", "title_en": "Announcement at the book fair", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε μια μεγάλη έκθεση βιβλίου. Ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί επισκέπτες, καλώς ήρθατε στην έκθεση βιβλίου. Σας ενημερώνουμε ότι η παρουσίαση του νέου μυθιστορήματος της Ελένης Μαργαρίτη, που ήταν προγραμματισμένη για τις έξι στην αίθουσα Α, μεταφέρεται στις επτά, στην αίθουσα Γ, στον πρώτο όροφο.", "Dear visitors, welcome to the book fair. Please note that the presentation of Eleni Margariti's new novel, scheduled for six o'clock in hall A, is moved to seven o'clock, in hall C, on the first floor."),
  L("Εκφωνητής", "m", "Μετά την παρουσίαση η συγγραφέας θα υπογράφει αντίτυπα στο περίπτερο του εκδοτικού της οίκου. Οι αναγνώστες που θέλουν υπογραφή παρακαλούνται να πάρουν αριθμό προτεραιότητας από το περίπτερο μέχρι τις έξι και μισή.", "After the presentation the author will sign copies at her publisher's stand. Readers who would like a signature are asked to take a queue number from the stand by half past six."),
  L("Εκφωνητής", "m", "Υπενθυμίζουμε επίσης ότι στον χώρο για παιδιά, δίπλα στην κεντρική είσοδο, η θεατρική ανάγνωση παραμυθιών συνεχίζεται κάθε μία ώρα. Η είσοδος σε όλες τις εκδηλώσεις είναι ελεύθερη. Σας ευχαριστούμε.", "We also remind you that in the children's area, next to the main entrance, the dramatised fairy-tale readings continue every hour. Entry to all events is free. Thank you."),
 ],
 "questions": [
  Q("Τι αλλάζει στην παρουσίαση του μυθιστορήματος;", ["Ακυρώνεται", "Μεταφέρεται σε άλλη ώρα και αίθουσα", "Γίνεται την επόμενη μέρα", "Θα γίνει χωρίς τη συγγραφέα"], 1, "μεταφέρεται στις επτά, στην αίθουσα Γ"),
  Q("Τι πρέπει να κάνουν όσοι θέλουν υπογραφή;", ["Να αγοράσουν εισιτήριο", "Να κάνουν κράτηση στο διαδίκτυο", "Να πάρουν αριθμό προτεραιότητας από το περίπτερο", "Να περιμένουν στην αίθουσα Α"], 2, "παρακαλούνται να πάρουν αριθμό προτεραιότητας από το περίπτερο"),
  Q("Πού γίνονται οι αναγνώσεις παραμυθιών;", ["Στον χώρο για παιδιά, δίπλα στην κεντρική είσοδο", "Στην αίθουσα Γ", "Στο περίπτερο του εκδοτικού οίκου", "Στον δεύτερο όροφο"], 0, "στον χώρο για παιδιά, δίπλα στην κεντρική είσοδο"),
 ],
 "gloss": {"έκθεση βιβλίου": "έκθεση βιβλίου — book fair", "παρουσίαση": "παρουσίαση — (book) launch, presentation", "μυθιστορήματος": "μυθιστόρημα — novel", "προγραμματισμένη": "προγραμματισμένος — scheduled", "μεταφέρεται": "μεταφέρομαι — to be moved", "αντίτυπα": "αντίτυπο — copy (of a book)", "περίπτερο": "περίπτερο — stand, booth", "εκδοτικού": "εκδοτικός οίκος — publishing house", "αριθμό προτεραιότητας": "αριθμός προτεραιότητας — queue number", "θεατρική ανάγνωση": "θεατρική ανάγνωση — dramatised reading", "εκδηλώσεις": "εκδήλωση — event"}
})

ITEMS.append({
 "id": "l131-vm-fotografos-gamou", "title": "Μήνυμα από τη φωτογράφο του γάμου", "title_en": "A message from the wedding photographer", "type": "voicemail", "level": "B2",
 "context_el": "Παντρευτήκατε πριν από δύο μήνες. Ακούτε ένα μήνυμα από τη φωτογράφο του γάμου σας στον τηλεφωνητή.",
 "script": [
  L("Φωτογράφος", "f", "Γεια σας, η Ζωή είμαι, η φωτογράφος. Σας έχω καλά νέα: οι φωτογραφίες του γάμου σας είναι έτοιμες. Τις επεξεργάστηκα όλες και σας έστειλα σήμερα το πρωί στο ηλεκτρονικό ταχυδρομείο έναν σύνδεσμο, για να τις δείτε.", "Hello, it's Zoi, the photographer. I have good news: your wedding photos are ready. I've edited them all, and this morning I emailed you a link so you can see them."),
  L("Φωτογράφος", "f", "Για το άλμπουμ θα χρειαστώ να διαλέξετε μέχρι ογδόντα φωτογραφίες. Μπορείτε να τις σημειώσετε με ένα αστεράκι μέσα στον σύνδεσμο. Αν θέλετε περισσότερες σελίδες, υπάρχει μια μικρή επιπλέον χρέωση.", "For the album I'll need you to choose up to eighty photos. You can mark them with a little star inside the link. If you want more pages, there's a small extra charge."),
  L("Φωτογράφος", "f", "Ο σύνδεσμος θα είναι ενεργός για έναν μήνα, οπότε σας συμβουλεύω να κατεβάσετε τις φωτογραφίες σας στον υπολογιστή όσο το δυνατόν πιο σύντομα. Για οποιαδήποτε απορία, πάρτε με τηλέφωνο. Γεια σας!", "The link will be active for one month, so I advise you to download your photos to your computer as soon as possible. For any question, give me a call. Bye!"),
 ],
 "questions": [
  Q("Πώς μπορούν να δουν οι νεόνυμφοι τις φωτογραφίες;", ["Στο στούντιο της φωτογράφου", "Μέσω ενός συνδέσμου στο ηλεκτρονικό τους ταχυδρομείο", "Σε ένα στικάκι που θα τους ταχυδρομήσει", "Σε ένα δοκιμαστικό άλμπουμ"], 1, "σας έστειλα σήμερα το πρωί στο ηλεκτρονικό ταχυδρομείο έναν σύνδεσμο"),
  Q("Πόσες φωτογραφίες μπορούν να διαλέξουν για το άλμπουμ χωρίς επιπλέον χρέωση;", ["Σαράντα", "Εκατό", "Μέχρι ογδόντα", "Όσες θέλουν"], 2, "θα χρειαστώ να διαλέξετε μέχρι ογδόντα φωτογραφίες"),
  Q("Τι τους συμβουλεύει η φωτογράφος;", ["Να κατεβάσουν τις φωτογραφίες όσο πιο σύντομα γίνεται", "Να τυπώσουν όλες τις φωτογραφίες", "Να της τηλεφωνήσουν πριν διαλέξουν", "Να στείλουν τον σύνδεσμο στους καλεσμένους"], 0, "σας συμβουλεύω να κατεβάσετε τις φωτογραφίες σας στον υπολογιστή όσο το δυνατόν πιο σύντομα"),
 ],
 "gloss": {"Παντρευτήκατε": "παντρεύομαι — to get married", "επεξεργάστηκα": "επεξεργάζομαι — to edit, process", "ηλεκτρονικό ταχυδρομείο": "ηλεκτρονικό ταχυδρομείο — email", "σύνδεσμο": "σύνδεσμος — link", "άλμπουμ": "άλμπουμ — album", "αστεράκι": "αστεράκι — little star", "επιπλέον χρέωση": "επιπλέον χρέωση — extra charge", "ενεργός": "ενεργός — active", "κατεβάσετε": "κατεβάζω — to download", "απορία": "απορία — question, query"}
})

ITEMS.append({
 "id": "l131-dial-parti-genethlion", "title": "Πού θα κάνουμε το πάρτι του μικρού;", "title_en": "Where shall we have our son's party?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο γονείς συζητούν πού θα γιορτάσουν τα έβδομα γενέθλια του γιου τους.",
 "script": [
  L("Μαρίνα", "f", "Ο Άρης θέλει να καλέσει όλη την τάξη, είκοσι τέσσερα παιδιά. Στο σπίτι δεν χωράμε με τίποτα. Σκέφτομαι να κλείσουμε έναν παιδότοπο.", "Aris wants to invite the whole class, twenty-four children. There's no way we fit in the flat. I'm thinking of booking a children's play centre."),
  L("Στέλιος", "m", "Ο παιδότοπος κοστίζει μια περιουσία, σχεδόν δεκαπέντε ευρώ το παιδί. Γιατί να μην κάνουμε το πάρτι στο πάρκο, κάτω από τα πεύκα; Φέρνουμε σάντουιτς, τούρτα και μια μπάλα.", "The play centre costs a fortune, almost fifteen euros per child. Why don't we have the party in the park, under the pine trees? We bring sandwiches, a cake and a ball."),
  L("Μαρίνα", "f", "Και αν βρέξει; Είμαστε αρχές Νοεμβρίου. Δεν θέλω να τρέχουμε με είκοσι τέσσερα βρεγμένα παιδιά.", "And what if it rains? It's early November. I don't want to be running around with twenty-four wet children."),
  L("Στέλιος", "m", "Έχεις δίκιο. Τότε ας ρωτήσουμε στην ενορία· η αίθουσα της εκκλησίας νοικιάζεται φτηνά, και έχει και αυλή. Αν βγει ήλιος, τα παιδιά παίζουν έξω.", "You're right. Then let's ask at the parish; the church hall can be rented cheaply, and it has a yard too. If the sun comes out, the kids play outside."),
 ],
 "questions": [
  Q("Γιατί δεν μπορούν να κάνουν το πάρτι στο σπίτι;", ["Γιατί κάνουν ανακαίνιση", "Γιατί δεν χωράνε είκοσι τέσσερα παιδιά", "Γιατί διαμαρτύρονται οι γείτονες", "Γιατί ο Άρης δεν θέλει"], 1, "Στο σπίτι δεν χωράμε με τίποτα"),
  Q("Ποιο είναι το πρόβλημα με το πάρκο, κατά τη Μαρίνα;", ["Είναι πολύ μακριά", "Δεν επιτρέπονται πάρτι", "Μπορεί να βρέξει", "Δεν έχει σκιά"], 2, "Και αν βρέξει;"),
  Q("Τι προτείνει τελικά ο Στέλιος;", ["Την αίθουσα της εκκλησίας, που έχει και αυλή", "Έναν ακριβό παιδότοπο", "Να αναβάλουν το πάρτι για την άνοιξη", "Να καλέσουν λιγότερα παιδιά"], 0, "η αίθουσα της εκκλησίας νοικιάζεται φτηνά, και έχει και αυλή"),
 ],
 "gloss": {"γενέθλια": "γενέθλια — birthday", "παιδότοπο": "παιδότοπος — children's play centre", "περιουσία": "περιουσία — fortune", "πεύκα": "πεύκο — pine tree", "τούρτα": "τούρτα — (birthday) cake", "βρεγμένα": "βρεγμένος — wet", "ενορία": "ενορία — parish", "νοικιάζεται": "νοικιάζομαι — to be rented", "αυλή": "αυλή — yard, courtyard"}
})

ITEMS.append({
 "id": "l131-int-psaltis", "title": "Ένας νέος ψάλτης", "title_en": "A young church cantor", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια ραδιοφωνική συνέντευξη με έναν νέο άντρα που ψέλνει σε μια εκκλησία της Αθήνας.",
 "script": [
  L("Δημοσιογράφος", "f", "Γιάννη, είσαι είκοσι τεσσάρων χρονών και ψάλτης. Πώς ξεκίνησες;", "Giannis, you're twenty-four and a cantor. How did you start?"),
  L("Ψάλτης", "m", "Ο παππούς μου έψελνε σε μια εκκλησία στο χωριό, και από μικρός στεκόμουν δίπλα του στο αναλόγιο. Στα δώδεκα γράφτηκα σε μια σχολή βυζαντινής μουσικής. Εκεί έμαθα να διαβάζω τη βυζαντινή σημειογραφία, που είναι εντελώς διαφορετική από τις νότες του πενταγράμμου.", "My grandfather used to chant in a church in the village, and from a young age I stood next to him at the lectern. At twelve I enrolled in a school of Byzantine music. There I learned to read Byzantine notation, which is completely different from the notes of the staff."),
  L("Δημοσιογράφος", "f", "Τι είναι το πιο δύσκολο σε αυτή τη μουσική;", "What's the hardest thing about this music?"),
  L("Ψάλτης", "m", "Τα διαστήματα. Η βυζαντινή μουσική έχει φθόγγους ανάμεσα στις νότες του πιάνου, και το αυτί χρειάζεται χρόνια για να τους συνηθίσει. Επίσης, ψέλνουμε χωρίς όργανα, μόνο με τη φωνή, οπότε δεν μπορείς να κρυφτείς πίσω από τίποτα.", "The intervals. Byzantine music has notes between the notes of the piano, and the ear needs years to get used to them. Also, we chant without instruments, only with the voice, so you can't hide behind anything."),
  L("Δημοσιογράφος", "f", "Και οι φίλοι σου τι λένε;", "And what do your friends say?"),
  L("Ψάλτης", "m", "Στην αρχή με πείραζαν. Από τότε όμως που η βυζαντινή μουσική μπήκε στον κατάλογο της άυλης πολιτιστικής κληρονομιάς της UNESCO, μερικοί έρχονται να με ακούσουν. Ένας μάλιστα άρχισε μαθήματα!", "At first they teased me. But since Byzantine music was added to UNESCO's list of intangible cultural heritage, some of them come to hear me. One even started lessons!"),
 ],
 "questions": [
  Q("Πώς ξεκίνησε ο Γιάννης να ψέλνει;", ["Τον έστειλαν οι γονείς του σε ωδείο", "Από μικρός στεκόταν δίπλα στον παππού του στο αναλόγιο", "Το ανακάλυψε στον στρατό", "Τον έμαθε ο ιερέας της ενορίας του"], 1, "από μικρός στεκόμουν δίπλα του στο αναλόγιο"),
  Q("Τι είναι το πιο δύσκολο στη βυζαντινή μουσική, κατά τον Γιάννη;", ["Οι μακριοί ύμνοι", "Τα αρχαία κείμενα", "Τα διαστήματα, με φθόγγους ανάμεσα στις νότες του πιάνου", "Το όργανο που τη συνοδεύει"], 2, "Τα διαστήματα. Η βυζαντινή μουσική έχει φθόγγους ανάμεσα στις νότες του πιάνου"),
  Q("Τι άλλαξε στη στάση των φίλων του;", ["Μερικοί έρχονται να τον ακούσουν, κι ένας άρχισε μαθήματα", "Σταμάτησαν να τον πειράζουν, αλλά δεν ενδιαφέρονται", "Τον κάλεσαν να ψάλει σε μια συναυλία", "Του ζήτησαν να ηχογραφήσει έναν δίσκο"], 0, "μερικοί έρχονται να με ακούσουν. Ένας μάλιστα άρχισε μαθήματα"),
 ],
 "gloss": {"ψέλνει": "ψέλνω — to chant (in church)", "ψάλτης": "ψάλτης — (church) cantor", "αναλόγιο": "αναλόγιο — lectern", "βυζαντινής μουσικής": "βυζαντινή μουσική — Byzantine (church) music", "σημειογραφία": "σημειογραφία — (musical) notation", "πενταγράμμου": "πεντάγραμμο — (musical) staff", "διαστήματα": "διάστημα — interval", "φθόγγους": "φθόγγος — (musical) note, tone", "πείραζαν": "πειράζω — to tease", "άυλης πολιτιστικής κληρονομιάς": "άυλη πολιτιστική κληρονομιά — intangible cultural heritage"}
})

ITEMS.append({
 "id": "l131-rep-vivlia-braille", "title": "Βιβλία σε γραφή Μπράιγ στη δημοτική βιβλιοθήκη", "title_en": "Braille books at the municipal library", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε έναν τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Ρεπόρτερ", "f", "Η δημοτική βιβλιοθήκη της πόλης μας εγκαινίασε χθες ένα καινούργιο τμήμα για ανθρώπους με προβλήματα όρασης. Στα ράφια του υπάρχουν πλέον περισσότερα από τριακόσια βιβλία σε γραφή Μπράιγ, αλλά και εκατοντάδες ηχητικά βιβλία.", "Our town's municipal library yesterday opened a new section for people with visual impairments. Its shelves now hold more than three hundred books in Braille, as well as hundreds of audiobooks."),
  L("Ρεπόρτερ", "f", "Τα βιβλία σε γραφή Μπράιγ είναι ογκώδη: ένα μυθιστόρημα μπορεί να χρειαστεί πέντε ή έξι τόμους. Γι' αυτό η βιβλιοθήκη προσφέρει και δωρεάν αποστολή στο σπίτι, για όσους δυσκολεύονται να μετακινηθούν.", "Braille books are bulky: one novel may need five or six volumes. That's why the library also offers free home delivery for those who find it hard to get around."),
  L("Ρεπόρτερ", "f", "Η ιδέα ξεκίνησε από μια συνταξιούχο δασκάλα, η οποία έχασε την όρασή της πριν από λίγα χρόνια. Κάθε Πέμπτη απόγευμα, η ίδια θα διδάσκει γραφή Μπράιγ σε όποιον ενδιαφέρεται, ακόμα και σε όσους βλέπουν.", "The idea came from a retired teacher who lost her sight a few years ago. Every Thursday afternoon she herself will teach Braille to anyone interested, even to sighted people."),
 ],
 "questions": [
  Q("Τι περιλαμβάνει το νέο τμήμα της βιβλιοθήκης;", ["Μόνο ηχητικά βιβλία", "Βιβλία σε γραφή Μπράιγ και ηχητικά βιβλία", "Υπολογιστές για τυφλούς", "Μεγάλες οθόνες ανάγνωσης"], 1, "περισσότερα από τριακόσια βιβλία σε γραφή Μπράιγ, αλλά και εκατοντάδες ηχητικά βιβλία"),
  Q("Γιατί η βιβλιοθήκη στέλνει βιβλία στο σπίτι;", ["Γιατί δεν έχει αρκετό χώρο", "Γιατί το ζήτησε ο δήμος", "Για όσους δυσκολεύονται να μετακινηθούν", "Γιατί τα βιβλία είναι πολύ ακριβά"], 2, "για όσους δυσκολεύονται να μετακινηθούν"),
  Q("Τι θα κάνει κάθε Πέμπτη η συνταξιούχος δασκάλα;", ["Θα διδάσκει γραφή Μπράιγ σε όποιον ενδιαφέρεται", "Θα διαβάζει βιβλία στο ραδιόφωνο", "Θα μεταφράζει βιβλία", "Θα επισκέπτεται σχολεία"], 0, "η ίδια θα διδάσκει γραφή Μπράιγ σε όποιον ενδιαφέρεται"),
 ],
 "gloss": {"εγκαινίασε": "εγκαινιάζω — to open, inaugurate", "τμήμα": "τμήμα — section", "όρασης": "όραση — sight, vision", "γραφή Μπράιγ": "γραφή Μπράιγ — Braille", "ηχητικά βιβλία": "ηχητικό βιβλίο — audiobook", "ογκώδη": "ογκώδης — bulky", "τόμους": "τόμος — volume", "αποστολή": "αποστολή — delivery, dispatch", "μετακινηθούν": "μετακινούμαι — to get around, move"}
})

ITEMS.append({
 "id": "l131-rep-skoteinos-ouranos", "title": "Ένα χωριό χαμηλώνει τα φώτα για τα αστέρια", "title_en": "A village dims its lights for the stars", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα ορεινό χωριό που άλλαξε τον δημόσιο φωτισμό του.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε ένα ορεινό χωριό της Πελοποννήσου, η κοινότητα αποφάσισε να αλλάξει όλες τις λάμπες των δρόμων. Τα καινούργια φωτιστικά ρίχνουν το φως μόνο προς τα κάτω και έχουν πιο ζεστό, κιτρινωπό χρώμα.", "In a mountain village in the Peloponnese, the community decided to change all the street lamps. The new fittings throw light only downwards and have a warmer, yellowish colour."),
  L("Ρεπόρτερ", "m", "Ο στόχος είναι να μειωθεί η φωτορύπανση, δηλαδή το τεχνητό φως που κρύβει τον νυχτερινό ουρανό. Τώρα, τις καθαρές νύχτες, ο Γαλαξίας φαίνεται με γυμνό μάτι από την πλατεία του χωριού. Παράλληλα, ο λογαριασμός του ρεύματος για τον δημόσιο φωτισμό μειώθηκε σχεδόν στο μισό.", "The aim is to reduce light pollution, that is, the artificial light that hides the night sky. Now, on clear nights, the Milky Way can be seen with the naked eye from the village square. At the same time, the electricity bill for street lighting fell by almost half."),
  L("Ρεπόρτερ", "m", "Ήδη έρχονται ερασιτέχνες αστρονόμοι από την Αθήνα με τα τηλεσκόπιά τους, και οι δύο ξενώνες του χωριού είναι γεμάτοι τα Σαββατοκύριακα, ακόμα και τον χειμώνα.", "Amateur astronomers are already coming from Athens with their telescopes, and the village's two guesthouses are full at weekends, even in winter."),
 ],
 "questions": [
  Q("Πώς είναι τα καινούργια φωτιστικά;", ["Πιο δυνατά και λευκά", "Ρίχνουν το φως μόνο προς τα κάτω και έχουν ζεστό χρώμα", "Ανάβουν μόνο όταν περνάει κάποιος", "Λειτουργούν με ηλιακή ενέργεια"], 1, "Τα καινούργια φωτιστικά ρίχνουν το φως μόνο προς τα κάτω και έχουν πιο ζεστό, κιτρινωπό χρώμα"),
  Q("Τι άλλο κέρδισε η κοινότητα, εκτός από τον καθαρό ουρανό;", ["Μια επιχορήγηση από την Ευρώπη", "Ένα καινούργιο αστεροσκοπείο", "Μικρότερο λογαριασμό ρεύματος", "Περισσότερους μόνιμους κατοίκους"], 2, "ο λογαριασμός του ρεύματος για τον δημόσιο φωτισμό μειώθηκε σχεδόν στο μισό"),
  Q("Ποιοι επισκέπτονται τώρα το χωριό;", ["Ερασιτέχνες αστρονόμοι με τα τηλεσκόπιά τους", "Μαθητές σε σχολικές εκδρομές", "Ορειβάτες", "Επιστήμονες από το εξωτερικό"], 0, "έρχονται ερασιτέχνες αστρονόμοι από την Αθήνα με τα τηλεσκόπιά τους"),
 ],
 "gloss": {"ορεινό": "ορεινός — mountain (adj.)", "φωτιστικά": "φωτιστικό — light fitting", "κιτρινωπό": "κιτρινωπός — yellowish", "φωτορύπανση": "φωτορύπανση — light pollution", "τεχνητό": "τεχνητός — artificial", "Γαλαξίας": "Γαλαξίας — the Milky Way", "γυμνό μάτι": "με γυμνό μάτι — with the naked eye", "δημόσιο φωτισμό": "δημόσιος φωτισμός — street lighting", "ερασιτέχνες": "ερασιτέχνης — amateur", "τηλεσκόπιά": "τηλεσκόπιο — telescope", "ξενώνες": "ξενώνας — guesthouse"}
})

ITEMS.append({
 "id": "l131-mono-enorkos", "title": "Όταν κληρώθηκα ένορκος", "title_en": "When I was drawn as a juror", "type": "monologue", "level": "B2",
 "context_el": "Ένας άντρας μιλά σε ένα podcast για την εμπειρία του ως ενόρκου σε ένα δικαστήριο.",
 "script": [
  L("Αντώνης", "m", "Πέρσι μού ήρθε ένα χαρτί από το δικαστήριο: είχα κληρωθεί ένορκος. Στην αρχή τρόμαξα. Είμαι υδραυλικός, δεν ξέρω τίποτα από νόμους. Σκέφτηκα μάλιστα να ζητήσω να με εξαιρέσουν, γιατί θα έχανα μέρες από τη δουλειά.", "Last year I got a paper from the court: I had been drawn as a juror. At first I was scared. I'm a plumber; I know nothing about law. I even thought about asking to be excused, because I'd lose days of work."),
  L("Αντώνης", "m", "Τελικά πήγα. Η υπόθεση ήταν σοβαρή, και κράτησε τρεις εβδομάδες. Αυτό που με εντυπωσίασε ήταν ότι οι δικαστές άκουγαν με προσοχή τη γνώμη μας, σαν να ήμασταν ίσοι. Κανείς δεν μας κοίταξε αφ' υψηλού.", "In the end I went. The case was serious, and it lasted three weeks. What impressed me was that the judges listened carefully to our opinion, as if we were equals. Nobody looked down on us."),
  L("Αντώνης", "m", "Το πιο δύσκολο ήταν η απόφαση. Κοιμόμουν άσχημα, γιατί ήξερα ότι από εμάς εξαρτιόταν η ζωή ενός ανθρώπου. Σήμερα, όμως, χαίρομαι που το έζησα. Κατάλαβα ότι η δικαιοσύνη δεν είναι κάτι μακρινό· είναι και δική μας ευθύνη.", "The hardest part was the verdict. I slept badly, because I knew a person's life depended on us. Today, though, I'm glad I lived through it. I understood that justice isn't something distant; it's our responsibility too."),
 ],
 "questions": [
  Q("Πώς αντέδρασε ο Αντώνης όταν έμαθε ότι κληρώθηκε;", ["Χάρηκε πολύ", "Τρόμαξε, γιατί δεν ξέρει τίποτα από νόμους", "Δεν έδωσε σημασία", "Ζήτησε αμέσως να εξαιρεθεί"], 1, "Στην αρχή τρόμαξα. Είμαι υδραυλικός, δεν ξέρω τίποτα από νόμους"),
  Q("Τι τον εντυπωσίασε στο δικαστήριο;", ["Η διάρκεια της υπόθεσης", "Το μέγεθος της αίθουσας", "Ότι οι δικαστές άκουγαν με προσοχή τη γνώμη των ενόρκων", "Ότι οι δικηγόροι μιλούσαν απλά"], 2, "οι δικαστές άκουγαν με προσοχή τη γνώμη μας, σαν να ήμασταν ίσοι"),
  Q("Τι κατάλαβε τελικά;", ["Ότι η δικαιοσύνη είναι και δική μας ευθύνη", "Ότι οι νόμοι είναι πολύ περίπλοκοι", "Ότι δεν θέλει να ξαναγίνει ένορκος", "Ότι οι δικαστές κάνουν συχνά λάθη"], 0, "η δικαιοσύνη δεν είναι κάτι μακρινό· είναι και δική μας ευθύνη"),
 ],
 "gloss": {"ενόρκου": "ένορκος — juror", "δικαστήριο": "δικαστήριο — court", "κληρωθεί": "κληρώνομαι — to be drawn (by lot)", "τρόμαξα": "τρομάζω — to get scared", "εξαιρέσουν": "εξαιρώ — to exempt, excuse", "υπόθεση": "υπόθεση — (court) case", "δικαστές": "δικαστής — judge", "αφ' υψηλού": "αφ' υψηλού — condescendingly, from on high", "εξαρτιόταν": "εξαρτώμαι — to depend", "δικαιοσύνη": "δικαιοσύνη — justice", "ευθύνη": "ευθύνη — responsibility"}
})

ITEMS.append({
 "id": "l131-mono-chronokapsoula", "title": "Η χρονοκάψουλα της τάξης μας", "title_en": "Our class time capsule", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα διηγείται τι βρήκαν όταν άνοιξαν μια χρονοκάψουλα που είχαν θάψει στο σχολείο τους.",
 "script": [
  L("Ναταλία", "f", "Το 2001, στην έκτη δημοτικού, η δασκάλα μας είχε μια ιδέα: να γράψει ο καθένας ένα γράμμα στον εαυτό του, όπως θα ήταν σε είκοσι πέντε χρόνια. Τα βάλαμε σε ένα μεταλλικό κουτί μαζί με φωτογραφίες και ένα κασετάκι και το θάψαμε στην αυλή, κάτω από τη μουριά.", "In 2001, in the sixth year of primary school, our teacher had an idea: each of us would write a letter to ourselves as we'd be in twenty-five years. We put them in a metal box together with photos and a little cassette and buried it in the playground, under the mulberry tree."),
  L("Ναταλία", "f", "Τον περασμένο μήνα μαζευτήκαμε ξανά, δεκαεννιά από τους είκοσι δύο. Ο διευθυντής μάς έδωσε την άδεια να σκάψουμε. Το κουτί είχε σκουριάσει, αλλά τα γράμματα ήταν σχεδόν άθικτα.", "Last month we got together again, nineteen of the twenty-two. The head teacher gave us permission to dig. The box had rusted, but the letters were almost intact."),
  L("Ναταλία", "f", "Στο δικό μου είχα γράψει ότι θα γινόμουν κτηνίατρος και θα ζούσα σε ένα νησί. Τελικά έγινα λογίστρια και μένω στο Περιστέρι. Γέλασα πολύ, αλλά στο τέλος του γράμματος είχα γράψει: «Ελπίζω να είσαι ακόμα φίλη με την Κατερίνα». Και είμαι. Αυτό μετράει περισσότερο.", "In mine I had written that I'd become a vet and live on an island. In the end I became an accountant and live in Peristeri. I laughed a lot, but at the end of the letter I had written: 'I hope you're still friends with Katerina.' And I am. That matters more."),
 ],
 "questions": [
  Q("Τι έγραψαν τα παιδιά το 2001;", ["Μια έκθεση για το σχολείο τους", "Ένα γράμμα στον εαυτό τους σε είκοσι πέντε χρόνια", "Ευχές για τη δασκάλα τους", "Ένα ημερολόγιο της χρονιάς"], 1, "να γράψει ο καθένας ένα γράμμα στον εαυτό του, όπως θα ήταν σε είκοσι πέντε χρόνια"),
  Q("Σε τι κατάσταση βρήκαν τα γράμματα;", ["Είχαν καταστραφεί από το νερό", "Έλειπαν μερικά", "Ήταν σχεδόν άθικτα", "Ήταν σκισμένα"], 2, "τα γράμματα ήταν σχεδόν άθικτα"),
  Q("Τι μετράει περισσότερο για τη Ναταλία;", ["Ότι είναι ακόμα φίλη με την Κατερίνα", "Ότι έγινε λογίστρια", "Ότι ζει στο Περιστέρι", "Ότι θυμόταν τη δασκάλα της"], 0, "«Ελπίζω να είσαι ακόμα φίλη με την Κατερίνα». Και είμαι. Αυτό μετράει περισσότερο"),
 ],
 "gloss": {"χρονοκάψουλα": "χρονοκάψουλα — time capsule", "θάψει": "θάβω — to bury", "μεταλλικό": "μεταλλικός — metal (adj.)", "κασετάκι": "κασετάκι — small (audio) cassette", "μουριά": "μουριά — mulberry tree", "σκάψουμε": "σκάβω — to dig", "σκουριάσει": "σκουριάζω — to rust", "άθικτα": "άθικτος — intact", "λογίστρια": "λογίστρια — accountant (f.)", "μετράει": "μετράω — to matter, count"}
})

ITEMS.append({
 "id": "l131-c1-benford", "title": "Γιατί το 1 είναι παντού", "title_en": "Why the digit 1 is everywhere", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική εκπομπή εκλαϊκευμένης επιστήμης για τον λεγόμενο νόμο του Μπένφορντ.",
 "script": [
  L("Παρουσιάστρια", "f", "Πάρτε έναν οποιονδήποτε μεγάλο κατάλογο αριθμών από την πραγματική ζωή: τους πληθυσμούς των πόλεων του κόσμου, τα μήκη των ποταμών, τις τιμές των μετοχών. Κοιτάξτε μόνο το πρώτο ψηφίο κάθε αριθμού. Θα περίμενε κανείς ότι κάθε ψηφίο, από το 1 ως το 9, θα εμφανίζεται περίπου εξίσου συχνά. Κι όμως, δεν συμβαίνει αυτό.", "Take any large list of numbers from real life: the populations of the world's cities, the lengths of rivers, share prices. Look only at the first digit of each number. You'd expect each digit, from 1 to 9, to appear roughly equally often. And yet that's not what happens."),
  L("Παρουσιάστρια", "f", "Το 1 εμφανίζεται ως πρώτο ψηφίο σε περίπου τριάντα τοις εκατό των περιπτώσεων, ενώ το 9 σε λιγότερο από πέντε τοις εκατό. Το φαινόμενο το είχε παρατηρήσει ήδη το 1881 ο αστρονόμος Σάιμον Νιούκομ, όταν πρόσεξε ότι οι πρώτες σελίδες των πινάκων λογαρίθμων ήταν πολύ πιο φθαρμένες από τις τελευταίες. Πήρε όμως το όνομά του από τον φυσικό Φρανκ Μπένφορντ, ο οποίος το 1938 το επιβεβαίωσε σε χιλιάδες δεδομένα.", "1 appears as the first digit in about thirty per cent of cases, while 9 appears in less than five per cent. The phenomenon had already been noticed in 1881 by the astronomer Simon Newcomb, when he saw that the first pages of logarithm tables were much more worn than the last ones. It was named, however, after the physicist Frank Benford, who in 1938 confirmed it on thousands of data."),
  L("Παρουσιάστρια", "f", "Η εξήγηση, με απλά λόγια, είναι ότι πολλά μεγέθη αυξάνονται με ποσοστά: για να περάσει μια πόλη από τις εκατό στις διακόσιες χιλιάδες κατοίκους πρέπει να διπλασιαστεί, ενώ από τις οχτακόσιες στις εννιακόσιες χιλιάδες αρκεί μια αύξηση γύρω στο δώδεκα τοις εκατό. Έτσι, οι αριθμοί «μένουν» περισσότερο χρόνο στο 1.", "The explanation, in simple terms, is that many quantities grow by percentages: for a city to go from a hundred to two hundred thousand inhabitants it has to double, whereas from eight hundred to nine hundred thousand an increase of around twelve per cent is enough. So numbers 'stay' longer on 1."),
  L("Παρουσιάστρια", "f", "Το πιο εντυπωσιακό είναι η πρακτική χρήση του νόμου. Ελεγκτές και φορολογικές αρχές τον χρησιμοποιούν για να εντοπίζουν ύποπτους λογαριασμούς: όποιος επινοεί αριθμούς τείνει να μοιράζει τα ψηφία πολύ «δίκαια», και αυτή ακριβώς η ομοιομορφία τον προδίδει. Δεν αποτελεί βέβαια απόδειξη απάτης, αλλά ένα σημάδι που αξίζει περαιτέρω έρευνα.", "The most striking thing is the law's practical use. Auditors and tax authorities use it to spot suspicious accounts: anyone who makes up numbers tends to spread the digits too 'fairly', and it's exactly this uniformity that gives them away. Of course it isn't proof of fraud, but a sign worth further investigation."),
 ],
 "questions": [
  Q("Τι θα περίμενε κανείς για τα πρώτα ψηφία των αριθμών;", ["Ότι το 9 θα είναι το πιο συχνό", "Ότι όλα θα εμφανίζονται περίπου εξίσου συχνά", "Ότι το 1 θα είναι σπάνιο", "Ότι θα εξαρτώνται από τη χώρα"], 1, "Θα περίμενε κανείς ότι κάθε ψηφίο, από το 1 ως το 9, θα εμφανίζεται περίπου εξίσου συχνά"),
  Q("Τι πρόσεξε ο Σάιμον Νιούκομ;", ["Ότι οι πληθυσμοί των πόλεων αυξάνονται γρήγορα", "Ότι οι τιμές των μετοχών αρχίζουν συνήθως από 9", "Ότι οι πρώτες σελίδες των πινάκων λογαρίθμων ήταν πιο φθαρμένες", "Ότι οι φορολογικές δηλώσεις είχαν λάθη"], 2, "οι πρώτες σελίδες των πινάκων λογαρίθμων ήταν πολύ πιο φθαρμένες από τις τελευταίες"),
  Q("Πώς εξηγείται, με απλά λόγια, το φαινόμενο;", ["Πολλά μεγέθη αυξάνονται με ποσοστά, οπότε οι αριθμοί μένουν περισσότερο στο 1", "Οι άνθρωποι προτιμούν το 1 όταν γράφουν αριθμούς", "Οι υπολογιστές στρογγυλεύουν τους αριθμούς", "Οι μικροί αριθμοί είναι πιο εύκολοι στη μέτρηση"], 0, "πολλά μεγέθη αυξάνονται με ποσοστά"),
  Q("Τι ισχύει για τη χρήση του νόμου από τους ελεγκτές;", ["Αποδεικνύει με βεβαιότητα την απάτη", "Χρησιμοποιείται μόνο σε επιστημονικά δεδομένα", "Δείχνει ότι οι επινοημένοι αριθμοί είναι πάντα μικροί", "Δίνει ένα σημάδι που αξίζει περαιτέρω έρευνα, όχι απόδειξη"], 3, "Δεν αποτελεί βέβαια απόδειξη απάτης, αλλά ένα σημάδι που αξίζει περαιτέρω έρευνα"),
 ],
 "gloss": {"εκλαϊκευμένης": "εκλαϊκευμένος — popular(ised)", "κατάλογο": "κατάλογος — list", "μετοχών": "μετοχή — share (stock)", "ψηφίο": "ψηφίο — digit", "πινάκων λογαρίθμων": "πίνακας λογαρίθμων — logarithm table", "φθαρμένες": "φθαρμένος — worn", "επιβεβαίωσε": "επιβεβαιώνω — to confirm", "δεδομένα": "δεδομένα — data", "διπλασιαστεί": "διπλασιάζομαι — to double", "Ελεγκτές": "ελεγκτής — auditor", "επινοεί": "επινοώ — to make up, invent", "ομοιομορφία": "ομοιομορφία — uniformity", "προδίδει": "προδίδω — to give away, betray", "απάτης": "απάτη — fraud", "περαιτέρω": "περαιτέρω — further"}
})

ITEMS.append({
 "id": "l131-c1-kosmas-aitolos", "title": "Κοσμάς ο Αιτωλός, ο κήρυκας των σχολείων", "title_en": "Kosmas of Aetolia, the preacher of schools", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια ιστορικό για τον Κοσμά τον Αιτωλό, έναν μοναχό του 18ου αιώνα.",
 "script": [
  L("Δημοσιογράφος", "m", "Ποιος ήταν ο Κοσμάς ο Αιτωλός;", "Who was Kosmas of Aetolia?"),
  L("Ιστορικός", "f", "Γεννήθηκε στις αρχές του 18ου αιώνα σε ένα χωριό της Αιτωλίας, σε μια φτωχή οικογένεια. Σπούδασε αργά, και στη συνέχεια έγινε μοναχός στο Άγιον Όρος. Γύρω στα σαράντα πέντε του, όμως, αποφάσισε να εγκαταλείψει τη μοναστική ησυχία και να περιοδεύσει στα χωριά της υπόδουλης Ελλάδας ως κήρυκας.", "He was born at the beginning of the eighteenth century in a village in Aetolia, into a poor family. He studied late, and then became a monk on Mount Athos. Around the age of forty-five, however, he decided to leave the monastic quiet and travel round the villages of enslaved Greece as a preacher."),
  L("Δημοσιογράφος", "m", "Τι δίδασκε στα κηρύγματά του;", "What did he teach in his sermons?"),
  L("Ιστορικός", "f", "Εκτός από τη θρησκευτική διδασκαλία, επέμενε σε κάτι πολύ πρακτικό: την παιδεία. Παρότρυνε τους χωρικούς να ιδρύουν σχολεία και να μορφώνουν τα παιδιά τους, και κορίτσια και αγόρια. Η παράδοση του αποδίδει την ίδρυση εκατοντάδων σχολείων, αν και ο αριθμός είναι μάλλον υπερβολικός. Μιλούσε, επίσης, στη γλώσσα του λαού, και όχι στα λόγια ελληνικά της εποχής, γι' αυτό τον καταλάβαιναν όλοι.", "Apart from religious teaching, he insisted on something very practical: education. He urged villagers to found schools and educate their children, girls as well as boys. Tradition credits him with founding hundreds of schools, although the number is probably exaggerated. He also spoke in the language of the people, not in the learned Greek of the time, which is why everyone understood him."),
  L("Δημοσιογράφος", "m", "Πώς τελείωσε η ζωή του;", "How did his life end?"),
  L("Ιστορικός", "f", "Η δράση του ενόχλησε πολλούς, και κάποιοι τον κατήγγειλαν στις οθωμανικές αρχές. Το 1779 απαγχονίστηκε κοντά στο Βεράτι, στη σημερινή Αλβανία. Το 1961 η Εκκλησία τον ανακήρυξε άγιο, και πολλοί τον θεωρούν σήμερα έναν από τους πρωτεργάτες της νεοελληνικής παιδείας.", "His activity troubled many, and some denounced him to the Ottoman authorities. In 1779 he was hanged near Berat, in present-day Albania. In 1961 the Church declared him a saint, and many today regard him as one of the pioneers of modern Greek education."),
 ],
 "questions": [
  Q("Τι αποφάσισε ο Κοσμάς γύρω στα σαράντα πέντε του;", ["Να γυρίσει στο χωριό του ως δάσκαλος", "Να εγκαταλείψει τη μοναστική ησυχία και να περιοδεύσει ως κήρυκας", "Να σπουδάσει στο εξωτερικό", "Να γίνει ηγούμενος ενός μοναστηριού"], 1, "αποφάσισε να εγκαταλείψει τη μοναστική ησυχία και να περιοδεύσει στα χωριά της υπόδουλης Ελλάδας ως κήρυκας"),
  Q("Τι παρότρυνε τους χωρικούς να κάνουν;", ["Να εγκαταλείψουν τα χωριά τους", "Να χτίσουν εκκλησίες", "Να ιδρύουν σχολεία και να μορφώνουν τα παιδιά τους", "Να ξεσηκωθούν αμέσως"], 2, "Παρότρυνε τους χωρικούς να ιδρύουν σχολεία και να μορφώνουν τα παιδιά τους"),
  Q("Τι λέει η ιστορικός για τον αριθμό των σχολείων που του αποδίδονται;", ["Είναι μάλλον υπερβολικός", "Είναι ακριβής", "Είναι πολύ μικρότερος από τον πραγματικό", "Δεν τον αναφέρει καμία πηγή"], 0, "ο αριθμός είναι μάλλον υπερβολικός"),
  Q("Γιατί τον καταλάβαιναν όλοι;", ["Γιατί κήρυττε μόνο σε μικρά χωριά", "Γιατί έγραφε βιβλία για παιδιά", "Γιατί χρησιμοποιούσε εικόνες", "Γιατί μιλούσε στη γλώσσα του λαού"], 3, "Μιλούσε, επίσης, στη γλώσσα του λαού, και όχι στα λόγια ελληνικά της εποχής"),
 ],
 "gloss": {"μοναχό": "μοναχός — monk", "μοναστική": "μοναστικός — monastic", "περιοδεύσει": "περιοδεύω — to tour, travel round", "υπόδουλης": "υπόδουλος — enslaved, under foreign rule", "κήρυκας": "κήρυκας — preacher", "κηρύγματά": "κήρυγμα — sermon", "παιδεία": "παιδεία — education", "Παρότρυνε": "παροτρύνω — to urge", "χωρικούς": "χωρικός — villager", "μορφώνουν": "μορφώνω — to educate", "υπερβολικός": "υπερβολικός — exaggerated", "λόγια": "λόγιος — learned, scholarly", "κατήγγειλαν": "καταγγέλλω — to denounce", "απαγχονίστηκε": "απαγχονίζομαι — to be hanged", "ανακήρυξε": "ανακηρύσσω — to proclaim, declare", "πρωτεργάτες": "πρωτεργάτης — pioneer, prime mover"}
})

rnd = random.Random(131)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-131.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
