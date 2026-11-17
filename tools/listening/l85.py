# Source for library/listening/listening-85.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l85.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l85-ann-exetaseis", "title": "Πριν από τις εξετάσεις ελληνομάθειας", "title_en": "Before the Greek language exam", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα εξεταστικό κέντρο για την Πιστοποίηση Ελληνομάθειας. Ο επιτηρητής κάνει μια ανακοίνωση πριν αρχίσει η εξέταση.",
 "script": [
  L("Επιτηρητής", "m", "Καλημέρα σας και καλή επιτυχία. Πριν ξεκινήσουμε, παρακαλώ ελέγξτε ότι έχετε πάνω στο θρανίο την ταυτότητα ή το διαβατήριό σας και μόνο μπλε ή μαύρο στυλό. Τα κινητά τηλέφωνα πρέπει να είναι κλειστά, όχι απλώς στο αθόρυβο, και να βρίσκονται μέσα στις τσάντες σας, στο μπροστινό μέρος της αίθουσας.", "Good morning and good luck. Before we begin, please check that you have your identity card or passport on your desk and only a blue or black pen. Mobile phones must be switched off, not just on silent, and must be in your bags at the front of the room."),
  L("Επιτηρητής", "m", "Η εξέταση ξεκινά με την κατανόηση προφορικού λόγου. Κάθε κείμενο θα το ακούσετε δύο φορές. Πριν από κάθε άκουσμα θα έχετε λίγο χρόνο να διαβάσετε τις ερωτήσεις. Στη διάρκεια της ηχογράφησης δεν επιτρέπεται να βγείτε από την αίθουσα.", "The exam begins with listening comprehension. You will hear each text twice. Before each listening you will have a little time to read the questions. During the recording you may not leave the room."),
  L("Επιτηρητής", "m", "Τις απαντήσεις σας θα τις γράψετε στο απαντητικό φύλλο, όχι στο τετράδιο των ερωτήσεων· ό,τι γράψετε στο τετράδιο δεν βαθμολογείται. Αν έχετε κάποια απορία, σηκώστε το χέρι σας και θα έρθω κοντά σας. Μην μιλάτε με τους διπλανούς σας. Ξεκινάμε σε δύο λεπτά.", "You will write your answers on the answer sheet, not in the question booklet; anything you write in the booklet is not marked. If you have a question, raise your hand and I'll come to you. Don't talk to the people next to you. We start in two minutes."),
 ],
 "questions": [
  Q("Τι πρέπει να κάνουν οι υποψήφιοι με τα κινητά τους;", ["Να τα βάλουν στο αθόρυβο πάνω στο θρανίο", "Να τα κλείσουν και να τα αφήσουν στις τσάντες τους, μπροστά", "Να τα δώσουν στον επιτηρητή", "Να τα αφήσουν στο αυτοκίνητο"], 1, "Τα κινητά τηλέφωνα πρέπει να είναι κλειστά"),
  Q("Πόσες φορές θα ακούσουν κάθε κείμενο;", ["Μία", "Δύο", "Τρεις", "Όσες θέλουν"], 1, "Κάθε κείμενο θα το ακούσετε δύο φορές"),
  Q("Πού πρέπει να γράψουν τις απαντήσεις τους;", ["Στο τετράδιο των ερωτήσεων", "Σε ένα πρόχειρο χαρτί", "Στο απαντητικό φύλλο", "Στον υπολογιστή"], 2, "Τις απαντήσεις σας θα τις γράψετε στο απαντητικό φύλλο"),
 ],
 "gloss": {"εξεταστικό κέντρο": "εξεταστικό κέντρο — exam centre", "επιτηρητής": "επιτηρητής — invigilator", "θρανίο": "θρανίο — (school) desk", "αθόρυβο": "αθόρυβο — silent mode", "κατανόηση προφορικού λόγου": "κατανόηση προφορικού λόγου — listening comprehension", "άκουσμα": "άκουσμα — hearing, listening", "ηχογράφησης": "ηχογράφηση — recording", "απαντητικό φύλλο": "απαντητικό φύλλο — answer sheet", "βαθμολογείται": "βαθμολογούμαι — to be marked", "απορία": "απορία — question, query"},
})
ITEMS.append({
 "id": "l85-vm-afixi-xenona", "title": "Μήνυμα για την άφιξη στον ξενώνα", "title_en": "Voicemail about arriving at the guesthouse", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει δωμάτιο σε έναν ξενώνα στο Πήλιο. Ακούτε ένα μήνυμα από την ιδιοκτήτρια.",
 "script": [
  L("Δέσποινα", "f", "Γεια σας, είμαι η Δέσποινα από τον ξενώνα «Η Καστανιά». Είδα στο μήνυμά σας ότι θα φτάσετε αργά την Παρασκευή, μετά τις δέκα. Δεν υπάρχει πρόβλημα, αλλά εγώ δεν θα είμαι εκεί, γιατί έχω ένα βάφτισι στον Βόλο.", "Hello, this is Despina from 'The Chestnut Tree' guesthouse. I saw in your message that you'll arrive late on Friday, after ten. That's no problem, but I won't be there, because I have a christening in Volos."),
  L("Δέσποινα", "f", "Το κλειδί θα είναι σε ένα μικρό μεταλλικό κουτί δίπλα στην πόρτα της κουζίνας, στα αριστερά της εισόδου. Ο κωδικός είναι το έτος που χτίστηκε το σπίτι, που είναι γραμμένο πάνω από την πόρτα: ένα, οχτώ, εννιά, δύο. Το δωμάτιό σας είναι το τρία, στον πρώτο όροφο.", "The key will be in a small metal box next to the kitchen door, to the left of the entrance. The code is the year the house was built, which is written above the door: one, eight, nine, two. Your room is number three, on the first floor."),
  L("Δέσποινα", "f", "Ο δρόμος μετά την εκκλησία στενεύει πολύ και δεν έχει φώτα, οπότε σας συμβουλεύω να αφήσετε το αυτοκίνητο στο πάρκινγκ της πλατείας και να περπατήσετε τα τελευταία διακόσια μέτρα. Το πρωινό σερβίρεται από τις οχτώ και μισή στην αυλή. Καλό ταξίδι!", "The road after the church gets very narrow and has no lights, so I advise you to leave the car in the car park on the square and walk the last two hundred metres. Breakfast is served from half past eight in the courtyard. Have a good trip!"),
 ],
 "questions": [
  Q("Γιατί η Δέσποινα δεν θα είναι στον ξενώνα;", ["Γιατί είναι άρρωστη", "Γιατί έχει ένα βάφτισι στον Βόλο", "Γιατί ο ξενώνας είναι κλειστός", "Γιατί δουλεύει τα βράδια"], 1, "έχω ένα βάφτισι στον Βόλο"),
  Q("Ποιος είναι ο κωδικός του κουτιού;", ["Ο αριθμός του δωματίου", "Το έτος που χτίστηκε το σπίτι", "Τα τελευταία ψηφία του τηλεφώνου της", "Η ημερομηνία της κράτησης"], 1, "Ο κωδικός είναι το έτος που χτίστηκε το σπίτι"),
  Q("Τι συμβουλεύει για το αυτοκίνητο;", ["Να το αφήσουν στην πλατεία και να περπατήσουν", "Να παρκάρουν μπροστά στην πόρτα", "Να έρθουν με ταξί", "Να περάσουν από την εκκλησία με προσοχή"], 0, "σας συμβουλεύω να αφήσετε το αυτοκίνητο στο πάρκινγκ της πλατείας"),
 ],
 "gloss": {"ξενώνα": "ξενώνας — guesthouse", "ιδιοκτήτρια": "ιδιοκτήτρια — (female) owner", "βάφτισι": "βάφτιση / βάφτισι — christening", "μεταλλικό": "μεταλλικός — metal", "κωδικός": "κωδικός — code", "έτος": "έτος — year", "στενεύει": "στενεύω — to narrow", "σερβίρεται": "σερβίρομαι — to be served"},
})
ITEMS.append({
 "id": "l85-dia-venzinadiko", "title": "Στο βενζινάδικο", "title_en": "At the petrol station", "type": "dialogue", "level": "B2",
 "context_el": "Ένας οδηγός σταματά σε ένα βενζινάδικο στην εθνική οδό, πριν από ένα μεγάλο ταξίδι.",
 "script": [
  L("Υπάλληλος", "m", "Καλησπέρα. Τι να βάλουμε;", "Good evening. What shall we put in?"),
  L("Οδηγός", "f", "Γεμίστε το, αμόλυβδη. Και, αν μπορείτε, ρίξτε μια ματιά στα λάστιχα. Το ταμπλό μού δείχνει μια ένδειξη για την πίεση και δεν ξέρω τι σημαίνει.", "Fill it up, unleaded. And if you can, have a look at the tyres. The dashboard is showing me a warning about the pressure and I don't know what it means."),
  L("Υπάλληλος", "m", "Σημαίνει ότι κάποιο λάστιχο έχει χαμηλή πίεση. Για να δούμε... Ναι, το πίσω δεξί είναι πολύ πιο χαμηλό από τα άλλα. Βλέπω κι ένα καρφί εδώ, στο πλάι. Μάλλον το πατήσατε κάπου.", "It means one of the tyres has low pressure. Let's see... Yes, the rear right is much lower than the others. I can see a nail here too, on the side. You probably drove over it somewhere."),
  L("Οδηγός", "f", "Ωχ. Πάω μέχρι τη Θεσσαλονίκη απόψε. Μπορώ να συνεχίσω έτσι;", "Oh no. I'm going all the way to Thessaloniki tonight. Can I carry on like this?"),
  L("Υπάλληλος", "m", "Δεν θα σας το συνιστούσα. Επειδή το καρφί είναι στο πλάι, το λάστιχο δεν επισκευάζεται, πρέπει να αλλάξει. Μπορώ να σας βάλω τη ρεζέρβα τώρα, σε δέκα λεπτά. Με τη ρεζέρβα, όμως, μην πηγαίνετε πάνω από ογδόντα χιλιόμετρα την ώρα, και αύριο αλλάξτε το λάστιχο σε ένα βουλκανιζατέρ.", "I wouldn't recommend it. Because the nail is in the side, the tyre can't be repaired; it has to be replaced. I can fit the spare for you now, in ten minutes. With the spare, though, don't go over eighty kilometres an hour, and tomorrow change the tyre at a tyre shop."),
  L("Οδηγός", "f", "Εντάξει, βάλτε τη ρεζέρβα. Καλύτερα να αργήσω μία ώρα παρά να μείνω στη μέση της εθνικής.", "All right, fit the spare. Better to be an hour late than to be stuck in the middle of the motorway."),
 ],
 "questions": [
  Q("Τι πρόβλημα έχει το αυτοκίνητο;", ["Δεν ανάβουν τα φώτα", "Ένα λάστιχο έχει χαμηλή πίεση", "Το ρεζερβουάρ τρέχει", "Η μπαταρία είναι άδεια"], 1, "κάποιο λάστιχο έχει χαμηλή πίεση"),
  Q("Γιατί το λάστιχο δεν επισκευάζεται;", ["Γιατί είναι πολύ παλιό", "Γιατί το καρφί είναι στο πλάι", "Γιατί το βενζινάδικο δεν έχει εργαλεία", "Γιατί είναι Κυριακή"], 1, "Επειδή το καρφί είναι στο πλάι, το λάστιχο δεν επισκευάζεται"),
  Q("Τι πρέπει να προσέξει η οδηγός με τη ρεζέρβα;", ["Να μην οδηγεί τη νύχτα", "Να μην πηγαίνει πάνω από ογδόντα χιλιόμετρα την ώρα", "Να ελέγχει την πίεση κάθε ώρα", "Να μην παίρνει την εθνική"], 1, "μην πηγαίνετε πάνω από ογδόντα χιλιόμετρα την ώρα"),
 ],
 "gloss": {"βενζινάδικο": "βενζινάδικο — petrol station", "εθνική οδό": "εθνική οδός — national road, motorway", "αμόλυβδη": "αμόλυβδη — unleaded (petrol)", "λάστιχα": "λάστιχο — tyre", "ταμπλό": "ταμπλό — dashboard", "ένδειξη": "ένδειξη — warning light, indication", "πίεση": "πίεση — pressure", "καρφί": "καρφί — nail", "ρεζέρβα": "ρεζέρβα — spare tyre", "βουλκανιζατέρ": "βουλκανιζατέρ — tyre repair shop"},
})
ITEMS.append({
 "id": "l85-int-giatroi-klooun", "title": "Κλόουν στο νοσοκομείο", "title_en": "Clowns at the hospital", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, μια δημοσιογράφος μιλά με μια ηθοποιό που επισκέπτεται παιδιατρικές κλινικές ως κλόουν.",
 "script": [
  L("Δημοσιογράφος", "f", "Κυρία Λαμπράκη, πώς ξεκίνησε όλο αυτό;", "Ms Lambraki, how did all this start?"),
  L("Ναταλία", "f", "Είμαι ηθοποιός, και πριν από δέκα χρόνια ο ανιψιός μου νοσηλεύτηκε για δύο μήνες. Έβλεπα πόσο βαρετές και τρομακτικές ήταν οι μέρες του. Μια μέρα φόρεσα μια κόκκινη μύτη και πήγα να τον δω. Γέλασε για πρώτη φορά μετά από εβδομάδες. Τότε αποφάσισα να εκπαιδευτώ σωστά.", "I'm an actress, and ten years ago my nephew was in hospital for two months. I saw how boring and frightening his days were. One day I put on a red nose and went to see him. He laughed for the first time in weeks. That's when I decided to train properly."),
  L("Δημοσιογράφος", "f", "Χρειάζεται εκπαίδευση για να γίνει κανείς κλόουν σε νοσοκομείο;", "Do you need training to be a hospital clown?"),
  L("Ναταλία", "f", "Οπωσδήποτε. Δεν αρκεί να είσαι αστείος. Πρέπει να ξέρεις τους κανόνες υγιεινής, να συνεργάζεσαι με τους γιατρούς και τις νοσηλεύτριες, και κυρίως να «διαβάζεις» το παιδί. Αν ένα παιδί δεν θέλει να μας δει, φεύγουμε. Είναι ίσως η μόνη φορά στο νοσοκομείο που ένα παιδί μπορεί να πει «όχι» και να το σεβαστούν όλοι.", "Absolutely. It's not enough to be funny. You need to know the hygiene rules, work with the doctors and nurses, and above all 'read' the child. If a child doesn't want to see us, we leave. It's perhaps the only time in hospital that a child can say 'no' and everyone respects it."),
  L("Δημοσιογράφος", "f", "Υπάρχουν δύσκολες στιγμές;", "Are there difficult moments?"),
  L("Ναταλία", "f", "Πολλές. Όμως έχουμε δει παιδιά να φοβούνται λιγότερο πριν από μια ένεση ή μια εξέταση, και γονείς να χαμογελούν ξανά. Μερικές φορές οι γιατροί μάς ζητούν να είμαστε παρόντες σε μια δύσκολη διαδικασία, για να αποσπάσουμε την προσοχή του παιδιού. Η κόκκινη μύτη, τελικά, είναι κι αυτή ένα είδος φαρμάκου.", "Many. But we've seen children be less afraid before an injection or a test, and parents smile again. Sometimes the doctors ask us to be present at a difficult procedure, to distract the child. The red nose is, in the end, a kind of medicine too."),
 ],
 "questions": [
  Q("Τι έκανε τη Ναταλία να ξεκινήσει;", ["Μια διαφήμιση στο νοσοκομείο", "Η νοσηλεία του ανιψιού της", "Ένα σεμινάριο θεάτρου", "Μια πρόταση από έναν γιατρό"], 1, "ο ανιψιός μου νοσηλεύτηκε για δύο μήνες"),
  Q("Τι κάνουν οι κλόουν αν ένα παιδί δεν θέλει να τους δει;", ["Επιμένουν μέχρι να γελάσει", "Φεύγουν", "Ζητούν από τους γονείς να το πείσουν", "Περιμένουν έξω από την πόρτα"], 1, "Αν ένα παιδί δεν θέλει να μας δει, φεύγουμε"),
  Q("Γιατί τους ζητούν μερικές φορές οι γιατροί να είναι παρόντες;", ["Για να βοηθήσουν τις νοσηλεύτριες", "Για να αποσπάσουν την προσοχή του παιδιού", "Για να εξηγήσουν τη θεραπεία", "Για να βγάλουν φωτογραφίες"], 1, "για να αποσπάσουμε την προσοχή του παιδιού"),
 ],
 "gloss": {"παιδιατρικές κλινικές": "παιδιατρική κλινική — children's ward", "κλόουν": "κλόουν — clown", "ανιψιός": "ανιψιός — nephew", "νοσηλεύτηκε": "νοσηλεύομαι — to be in hospital", "υγιεινής": "υγιεινή — hygiene", "σεβαστούν": "σέβομαι — to respect", "ένεση": "ένεση — injection", "διαδικασία": "διαδικασία — procedure", "αποσπάσουμε": "αποσπώ (την προσοχή) — to distract"},
})
ITEMS.append({
 "id": "l85-rep-astypalaia", "title": "Η Αστυπάλαια", "title_en": "Astypalaia", "type": "report", "level": "B2",
 "context_el": "Σε μια ταξιδιωτική εκπομπή, ένας δημοσιογράφος παρουσιάζει την Αστυπάλαια, στα Δωδεκάνησα.",
 "script": [
  L("Δημοσιογράφος", "m", "Η Αστυπάλαια, το δυτικότερο νησί των Δωδεκανήσων, έχει ένα παράξενο σχήμα: από ψηλά μοιάζει με πεταλούδα, γιατί δύο μεγάλα κομμάτια στεριάς ενώνονται με μια στενή λωρίδα γης. Στην ενδοχώρα δεν θα βρείτε πολλά δέντρα, θα βρείτε όμως αμέτρητους κόλπους με ήσυχες παραλίες.", "Astypalaia, the westernmost island of the Dodecanese, has a strange shape: from above it looks like a butterfly, because two large pieces of land are joined by a narrow strip. Inland you won't find many trees, but you will find countless bays with quiet beaches."),
  L("Δημοσιογράφος", "m", "Η Χώρα, χτισμένη πάνω σε έναν λόφο, είναι από τις ομορφότερες του Αιγαίου. Στην κορυφή υψώνεται το βενετσιάνικο κάστρο, που έχτισε τον 15ο αιώνα η οικογένεια Κουιρίνι. Μέσα στα τείχη του έμεναν κάποτε οι κάτοικοι, για να προστατεύονται από τους πειρατές. Λίγο πιο κάτω, μια σειρά από λευκούς ανεμόμυλους στέκεται σαν φρουρά.", "Chora, built on a hill, is one of the most beautiful in the Aegean. At the top rises the Venetian castle, built in the 15th century by the Querini family. Inside its walls the inhabitants once lived, to protect themselves from pirates. A little lower down, a row of white windmills stands like a guard."),
  L("Δημοσιογράφος", "m", "Τα τελευταία χρόνια η Αστυπάλαια έγινε γνωστή και για κάτι άλλο: είναι το πρώτο ελληνικό νησί που προσπαθεί να αντικαταστήσει τα συμβατικά αυτοκίνητα με ηλεκτρικά. Οι κάτοικοι πήραν επιδότηση για ηλεκτρικά οχήματα, τοποθετήθηκαν σταθμοί φόρτισης, και η συγκοινωνία γίνεται πλέον με μικρά ηλεκτρικά λεωφορεία που τα καλεί κανείς από το κινητό του.", "In recent years Astypalaia has also become known for something else: it is the first Greek island trying to replace conventional cars with electric ones. Residents received a subsidy for electric vehicles, charging stations were installed, and public transport now runs on small electric buses that you call from your mobile."),
 ],
 "questions": [
  Q("Με τι μοιάζει η Αστυπάλαια από ψηλά;", ["Με αστέρι", "Με πεταλούδα", "Με καράβι", "Με καρδιά"], 1, "από ψηλά μοιάζει με πεταλούδα"),
  Q("Γιατί οι κάτοικοι έμεναν παλιά μέσα στο κάστρο;", ["Για να προστατεύονται από τους πειρατές", "Γιατί εκεί είχε νερό", "Γιατί ήταν πιο δροσερά", "Γιατί το διέταξε ο βασιλιάς"], 0, "για να προστατεύονται από τους πειρατές"),
  Q("Για ποιο λόγο έγινε πρόσφατα γνωστό το νησί;", ["Για ένα μουσικό φεστιβάλ", "Για την προσπάθεια να αντικατασταθούν τα συμβατικά αυτοκίνητα με ηλεκτρικά", "Για ένα νέο αεροδρόμιο", "Για τα αρχαία του"], 1, "προσπαθεί να αντικαταστήσει τα συμβατικά αυτοκίνητα με ηλεκτρικά"),
 ],
 "gloss": {"δυτικότερο": "δυτικότερος — westernmost", "λωρίδα": "λωρίδα — strip", "ενδοχώρα": "ενδοχώρα — inland, interior", "κόλπους": "κόλπος — bay", "βενετσιάνικο": "βενετσιάνικος — Venetian", "πειρατές": "πειρατής — pirate", "ανεμόμυλους": "ανεμόμυλος — windmill", "φρουρά": "φρουρά — guard", "συμβατικά": "συμβατικός — conventional", "επιδότηση": "επιδότηση — subsidy", "σταθμοί φόρτισης": "σταθμός φόρτισης — charging station"},
})
ITEMS.append({
 "id": "l85-rep-veroia", "title": "Η κρυμμένη Βέροια", "title_en": "Hidden Veria", "type": "report", "level": "B2",
 "context_el": "Σε μια εκπομπή για τις ελληνικές πόλεις, μια δημοσιογράφος περπατά στα στενά της Βέροιας.",
 "script": [
  L("Δημοσιογράφος", "f", "Η Βέροια, στις πλαγιές του Βερμίου, είναι μια πόλη που κρύβει τους θησαυρούς της. Εδώ σώζονται δεκάδες βυζαντινές και μεταβυζαντινές εκκλησίες, πολλές από τις οποίες δεν φαίνονται καν από τον δρόμο. Την εποχή της οθωμανικής κυριαρχίας οι χριστιανοί τις έχτιζαν χαμηλές, μέσα σε αυλές, ώστε να μοιάζουν με σπίτια ή αποθήκες.", "Veria, on the slopes of Mount Vermio, is a town that hides its treasures. Dozens of Byzantine and post-Byzantine churches survive here, many of which can't even be seen from the street. In the period of Ottoman rule Christians built them low, inside courtyards, so that they looked like houses or storerooms."),
  L("Δημοσιογράφος", "f", "Δίπλα στον ποταμό Τριπόταμο βρίσκεται η Μπαρμπούτα, η παλιά εβραϊκή συνοικία, με ξύλινα σπίτια και στενά καλντερίμια. Η εβραϊκή κοινότητα της πόλης χάθηκε σχεδόν ολόκληρη στο Ολοκαύτωμα. Σήμερα η συναγωγή έχει αναστηλωθεί, και η συνοικία είναι από τις πιο ατμοσφαιρικές γωνιές της Μακεδονίας.", "Next to the river Tripotamos lies Barbouta, the old Jewish quarter, with wooden houses and narrow cobbled lanes. The town's Jewish community perished almost entirely in the Holocaust. Today the synagogue has been restored, and the quarter is one of the most atmospheric corners of Macedonia."),
  L("Δημοσιογράφος", "f", "Στο κέντρο της πόλης, ένα μνημείο με ψηφιδωτά σημειώνει το σημείο όπου, σύμφωνα με την παράδοση, κήρυξε ο Απόστολος Παύλος. Και μόνο δώδεκα χιλιόμετρα μακριά βρίσκεται η Βεργίνα, με τους βασιλικούς τάφους των Μακεδόνων. Η Βέροια, λοιπόν, είναι ιδανική βάση για να εξερευνήσει κανείς την περιοχή.", "In the town centre, a monument with mosaics marks the spot where, according to tradition, the Apostle Paul preached. And only twelve kilometres away is Vergina, with the royal tombs of the Macedonians. So Veria is an ideal base for exploring the area."),
 ],
 "questions": [
  Q("Γιατί πολλές εκκλησίες της Βέροιας δεν φαίνονται από τον δρόμο;", ["Γιατί είναι κάτω από τη γη", "Γιατί χτίζονταν χαμηλές, μέσα σε αυλές, για να μοιάζουν με σπίτια", "Γιατί τις έχουν καλύψει δέντρα", "Γιατί είναι κλειστές για το κοινό"], 1, "οι χριστιανοί τις έχτιζαν χαμηλές, μέσα σε αυλές"),
  Q("Τι είναι η Μπαρμπούτα;", ["Ένα βουνό κοντά στην πόλη", "Η παλιά εβραϊκή συνοικία", "Ένας βυζαντινός ναός", "Ένα μουσείο"], 1, "η Μπαρμπούτα, η παλιά εβραϊκή συνοικία"),
  Q("Πόσο απέχει η Βεργίνα από τη Βέροια;", ["Δύο χιλιόμετρα", "Δώδεκα χιλιόμετρα", "Πενήντα χιλιόμετρα", "Εκατό χιλιόμετρα"], 1, "μόνο δώδεκα χιλιόμετρα μακριά βρίσκεται η Βεργίνα"),
 ],
 "gloss": {"πλαγιές": "πλαγιά — slope", "θησαυρούς": "θησαυρός — treasure", "μεταβυζαντινές": "μεταβυζαντινός — post-Byzantine", "κυριαρχίας": "κυριαρχία — rule, domination", "αποθήκες": "αποθήκη — storeroom", "συνοικία": "συνοικία — quarter, neighbourhood", "καλντερίμια": "καλντερίμι — cobbled lane", "Ολοκαύτωμα": "Ολοκαύτωμα — the Holocaust", "συναγωγή": "συναγωγή — synagogue", "κήρυξε": "κηρύσσω — to preach"},
})
ITEMS.append({
 "id": "l85-mono-servitora", "title": "Η πρώτη μου δουλειά ως σερβιτόρα", "title_en": "My first job as a waitress", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για τις πρώτες δουλειές, μια μηχανικός θυμάται το καλοκαίρι που δούλεψε σε μια ταβέρνα.",
 "script": [
  L("Αλεξάνδρα", "f", "Το καλοκαίρι που τελείωσα το λύκειο, βρήκα δουλειά ως σερβιτόρα σε μια ταβέρνα στη Νάξο. Νόμιζα ότι θα ήταν εύκολο: κουβαλάς πιάτα, παίρνεις παραγγελίες, χαμογελάς. Την πρώτη κιόλας μέρα έσπασα τέσσερα ποτήρια και έφερα μουσακά σε έναν πελάτη που είχε παραγγείλει ψάρι.", "The summer I finished school, I found a job as a waitress in a taverna on Naxos. I thought it would be easy: you carry plates, take orders, smile. On the very first day I broke four glasses and brought moussaka to a customer who had ordered fish."),
  L("Αλεξάνδρα", "f", "Ο ιδιοκτήτης, ο κυρ Μανώλης, δεν θύμωσε. Μου έδωσε ένα μικρό σημειωματάριο και μου είπε: «Μην εμπιστεύεσαι ποτέ τη μνήμη σου όταν το μαγαζί είναι γεμάτο». Μου έμαθε επίσης να κουβαλάω τρία πιάτα στο ένα χέρι, κάτι που ακόμα κάνω για να εντυπωσιάζω τους φίλους μου.", "The owner, Mr Manolis, didn't get angry. He gave me a little notebook and told me: 'Never trust your memory when the place is full.' He also taught me to carry three plates in one hand, something I still do to impress my friends."),
  L("Αλεξάνδρα", "f", "Δούλευα δώδεκα ώρες τη μέρα, χωρίς ρεπό, και τα πόδια μου πονούσαν κάθε βράδυ. Όμως εκείνο το καλοκαίρι έμαθα περισσότερα από οποιοδήποτε μάθημα: να μένω ήρεμη όταν όλοι βιάζονται, να μιλάω με αγνώστους και να λέω «συγγνώμη, φταίω εγώ». Σήμερα, ως μηχανικός, διαχειρίζομαι μεγάλα έργα. Ακόμα κουβαλάω πάντα ένα σημειωματάριο.", "I worked twelve hours a day, with no day off, and my feet hurt every evening. But that summer I learnt more than in any class: to stay calm when everyone is in a hurry, to talk to strangers and to say 'sorry, it's my fault'. Today, as an engineer, I manage big projects. I still always carry a notebook."),
 ],
 "questions": [
  Q("Τι συνέβη την πρώτη μέρα;", ["Ήρθε αργά στη δουλειά", "Έσπασε ποτήρια και έφερε λάθος πιάτο", "Μάλωσε με έναν πελάτη", "Έχασε το λεωφορείο"], 1, "έσπασα τέσσερα ποτήρια και έφερα μουσακά σε έναν πελάτη που είχε παραγγείλει ψάρι"),
  Q("Τι της έδωσε ο κυρ Μανώλης;", ["Ένα μικρό σημειωματάριο", "Μια αύξηση", "Ένα καινούργιο ζευγάρι παπούτσια", "Μια μέρα ρεπό"], 0, "Μου έδωσε ένα μικρό σημειωματάριο"),
  Q("Τι έμαθε εκείνο το καλοκαίρι, σύμφωνα με την ίδια;", ["Να μαγειρεύει", "Να μένει ήρεμη όταν όλοι βιάζονται", "Να μιλάει αγγλικά", "Να κάνει λογαριασμούς"], 1, "να μένω ήρεμη όταν όλοι βιάζονται"),
 ],
 "gloss": {"σερβιτόρα": "σερβιτόρα — waitress", "παραγγελίες": "παραγγελία — order", "παραγγείλει": "παραγγέλνω — to order", "σημειωματάριο": "σημειωματάριο — notebook", "εμπιστεύεσαι": "εμπιστεύομαι — to trust", "εντυπωσιάζω": "εντυπωσιάζω — to impress", "ρεπό": "ρεπό — day off", "διαχειρίζομαι": "διαχειρίζομαι — to manage"},
})
ITEMS.append({
 "id": "l85-mono-treximo-sta-peninta", "title": "Άρχισα να τρέχω στα πενήντα", "title_en": "I started running at fifty", "type": "monologue", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για την υγεία, ένας ακροατής μιλά για το πώς ξεκίνησε το τρέξιμο.",
 "script": [
  L("Παναγιώτης", "m", "Στα πενήντα μου ήμουν είκοσι κιλά πάνω από το κανονικό βάρος μου και λαχάνιαζα ανεβαίνοντας τις σκάλες της πολυκατοικίας. Ο γιατρός μου είπε ότι η πίεσή μου ήταν ανησυχητική. Εκείνο το βράδυ η κόρη μου μού έκανε δώρο ένα ζευγάρι αθλητικά παπούτσια.", "At fifty I was twenty kilos over my normal weight and I got out of breath climbing the stairs of our block of flats. My doctor told me my blood pressure was worrying. That evening my daughter gave me a pair of running shoes as a present."),
  L("Παναγιώτης", "m", "Την πρώτη φορά δεν μπόρεσα να τρέξω ούτε δύο λεπτά συνεχόμενα. Ακολούθησα ένα πρόγραμμα για αρχάριους: ένα λεπτό τρέξιμο, δύο λεπτά περπάτημα, τρεις φορές την εβδομάδα. Κάθε εβδομάδα πρόσθετα λίγο ακόμα. Το πιο δύσκολο δεν ήταν το σώμα, αλλά η ντροπή. Νόμιζα ότι όλοι στο πάρκο με κοίταζαν και γελούσαν.", "The first time I couldn't run even two minutes without stopping. I followed a beginners' programme: one minute running, two minutes walking, three times a week. Every week I added a little more. The hardest thing wasn't my body but the embarrassment. I thought everyone in the park was looking at me and laughing."),
  L("Παναγιώτης", "m", "Δύο χρόνια μετά, έτρεξα τα δέκα χιλιόμετρα του Κλασικού Μαραθωνίου. Τερμάτισα από τους τελευταίους, αλλά η κόρη μου με περίμενε στο Παναθηναϊκό Στάδιο. Η πίεσή μου είναι πια φυσιολογική. Και ανακάλυψα ότι κανείς στο πάρκο δεν γελούσε· οι περισσότεροι ήταν απασχολημένοι με τη δική τους ανάσα.", "Two years later I ran the ten kilometres of the Classic Marathon. I finished among the last, but my daughter was waiting for me at the Panathenaic Stadium. My blood pressure is now normal. And I discovered that nobody in the park was laughing; most of them were busy with their own breathing."),
 ],
 "questions": [
  Q("Τι του έκανε δώρο η κόρη του;", ["Μια συνδρομή σε γυμναστήριο", "Ένα ζευγάρι αθλητικά παπούτσια", "Ένα ρολόι για τρέξιμο", "Ένα ποδήλατο"], 1, "η κόρη μου μού έκανε δώρο ένα ζευγάρι αθλητικά παπούτσια"),
  Q("Ποιο ήταν το πιο δύσκολο στην αρχή;", ["Ο πόνος στα γόνατα", "Η έλλειψη χρόνου", "Η ντροπή", "Ο καιρός"], 2, "Το πιο δύσκολο δεν ήταν το σώμα, αλλά η ντροπή"),
  Q("Τι ανακάλυψε για τους άλλους στο πάρκο;", ["Ότι γελούσαν μαζί του", "Ότι κανείς δεν γελούσε, γιατί ήταν απασχολημένοι με τη δική τους ανάσα", "Ότι ήταν όλοι επαγγελματίες", "Ότι τον αναγνώριζαν από την τηλεόραση"], 1, "κανείς στο πάρκο δεν γελούσε"),
 ],
 "gloss": {"λαχάνιαζα": "λαχανιάζω — to get out of breath", "πίεσή": "πίεση — blood pressure", "ανησυχητική": "ανησυχητικός — worrying", "συνεχόμενα": "συνεχόμενα — continuously", "αρχάριους": "αρχάριος — beginner", "ντροπή": "ντροπή — embarrassment, shame", "Τερμάτισα": "τερματίζω — to finish (a race)", "φυσιολογική": "φυσιολογικός — normal", "ανάσα": "ανάσα — breath"},
})
ITEMS.append({
 "id": "l85-c1-ntaningk-krougker", "title": "Γιατί όσοι ξέρουν λίγα νομίζουν ότι ξέρουν πολλά;", "title_en": "Why do those who know little think they know a lot?", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την ψυχολογία της καθημερινότητας, ένας δημοσιογράφος συζητά με μια γνωστική ψυχολόγο για το λεγόμενο φαινόμενο Ντάνινγκ-Κρούγκερ.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Βαλαβάνη, τι περιγράφει το φαινόμενο Ντάνινγκ-Κρούγκερ;", "Ms Valavani, what does the Dunning–Kruger effect describe?"),
  L("Ψυχολόγος", "f", "Το περιέγραψαν δύο αμερικανοί ψυχολόγοι στα τέλη της δεκαετίας του 1990. Ζήτησαν από φοιτητές να λύσουν ασκήσεις λογικής, γραμματικής και χιούμορ, και μετά να εκτιμήσουν πόσο καλά τα πήγαν. Όσοι είχαν τις χαμηλότερες επιδόσεις υπερεκτίμησαν θεαματικά τον εαυτό τους: ενώ βρίσκονταν στο κατώτερο τέταρτο, πίστευαν ότι ήταν πάνω από τον μέσο όρο.", "Two American psychologists described it at the end of the 1990s. They asked students to solve tasks in logic, grammar and humour, and then to estimate how well they had done. Those with the lowest scores overestimated themselves dramatically: although they were in the bottom quarter, they believed they were above average."),
  L("Δημοσιογράφος", "m", "Και πώς εξηγείται αυτό;", "And how is that explained?"),
  L("Ψυχολόγος", "f", "Η εξήγηση των ερευνητών είναι ότι οι δεξιότητες που χρειάζεσαι για να κάνεις κάτι καλά είναι οι ίδιες που χρειάζεσαι για να καταλάβεις ότι το κάνεις άσχημα. Αν δεν ξέρεις τους κανόνες της γραμματικής, δεν μπορείς να δεις ούτε τα δικά σου λάθη. Υπάρχει και η άλλη όψη: οι πιο ικανοί τείνουν να υποτιμούν ελαφρώς τον εαυτό τους, γιατί υποθέτουν ότι ό,τι είναι εύκολο για αυτούς είναι εύκολο για όλους.", "The researchers' explanation is that the skills you need to do something well are the same ones you need to realise you are doing it badly. If you don't know the rules of grammar, you can't see your own mistakes either. There is also the other side: the most competent tend to slightly underestimate themselves, because they assume that what is easy for them is easy for everyone."),
  L("Δημοσιογράφος", "m", "Έχει δεχτεί κριτική η θεωρία;", "Has the theory been criticised?"),
  L("Ψυχολόγος", "f", "Ναι, και σοβαρή. Κάποιοι στατιστικολόγοι υποστηρίζουν ότι ένα μέρος του φαινομένου οφείλεται σε στατιστικά τεχνάσματα και όχι στην ψυχολογία. Το βέβαιο είναι ότι κανείς μας δεν είναι απρόσβλητος. Ο καλύτερος τρόπος να προστατευτούμε είναι να ζητάμε ειλικρινή ανατροφοδότηση και να μαθαίνουμε περισσότερα· όσο περισσότερα μαθαίνουμε, τόσο καλύτερα βλέπουμε πόσα δεν ξέρουμε.", "Yes, and serious criticism. Some statisticians argue that part of the effect is due to statistical artefacts rather than psychology. What is certain is that none of us is immune. The best way to protect ourselves is to ask for honest feedback and to keep learning; the more we learn, the better we see how much we don't know."),
 ],
 "questions": [
  Q("Τι έδειξε η αρχική έρευνα;", ["Ότι οι καλύτεροι φοιτητές υπερεκτιμούσαν τον εαυτό τους", "Ότι όσοι είχαν τις χαμηλότερες επιδόσεις υπερεκτίμησαν θεαματικά τον εαυτό τους", "Ότι όλοι εκτιμούσαν σωστά τις επιδόσεις τους", "Ότι το χιούμορ δεν μπορεί να μετρηθεί"], 1, "Όσοι είχαν τις χαμηλότερες επιδόσεις υπερεκτίμησαν θεαματικά τον εαυτό τους"),
  Q("Γιατί, σύμφωνα με τους ερευνητές, οι λιγότερο ικανοί δεν βλέπουν τα λάθη τους;", ["Γιατί δεν τους ενδιαφέρει", "Γιατί χρειάζονται τις ίδιες δεξιότητες για να καταλάβουν ότι κάνουν κάτι άσχημα", "Γιατί κανείς δεν τους διορθώνει", "Γιατί είναι υπερβολικά αισιόδοξοι από τη φύση τους"], 1, "οι δεξιότητες που χρειάζεσαι για να κάνεις κάτι καλά είναι οι ίδιες"),
  Q("Τι προτείνει η ψυχολόγος για να προστατευτούμε;", ["Να μην κρίνουμε ποτέ τον εαυτό μας", "Να εμπιστευόμαστε την πρώτη μας εντύπωση", "Να ζητάμε ειλικρινή ανατροφοδότηση και να μαθαίνουμε περισσότερα", "Να αποφεύγουμε τα τεστ"], 2, "να ζητάμε ειλικρινή ανατροφοδότηση"),
 ],
 "gloss": {"γνωστική ψυχολόγο": "γνωστική ψυχολογία — cognitive psychology", "επιδόσεις": "επίδοση — performance, score", "υπερεκτίμησαν": "υπερεκτιμώ — to overestimate", "κατώτερο τέταρτο": "κατώτερο τέταρτο — bottom quarter", "δεξιότητες": "δεξιότητα — skill", "υποτιμούν": "υποτιμώ — to underestimate", "στατιστικολόγοι": "στατιστικολόγος — statistician", "τεχνάσματα": "τέχνασμα — artefact, trick", "απρόσβλητος": "απρόσβλητος — immune", "ανατροφοδότηση": "ανατροφοδότηση — feedback"},
})
ITEMS.append({
 "id": "l85-c1-ypnos-efivon", "title": "Πρέπει τα σχολεία να αρχίζουν αργότερα;", "title_en": "Should schools start later?", "type": "monologue", "level": "C1",
 "context_el": "Σε μια διάλεξη για γονείς και εκπαιδευτικούς, ένας παιδίατρος μιλά για τον ύπνο των εφήβων.",
 "script": [
  L("Παιδίατρος", "m", "Οι γονείς των εφήβων συχνά παραπονιούνται ότι τα παιδιά τους δεν κοιμούνται πριν από τα μεσάνυχτα και ότι το πρωί δεν ξυπνούν με τίποτα. Συνήθως το αποδίδουμε στην τεμπελιά ή στα κινητά. Η βιολογία, όμως, έχει τον δικό της ρόλο: στην εφηβεία το εσωτερικό ρολόι του οργανισμού μετατοπίζεται, και η μελατονίνη, η ορμόνη του ύπνου, εκκρίνεται έως και δύο ώρες αργότερα απ’ ό,τι στα παιδιά ή στους ενήλικες.", "Parents of teenagers often complain that their children don't fall asleep before midnight and that in the morning they simply won't wake up. We usually put it down to laziness or to phones. Biology, however, plays its own part: in adolescence the body's internal clock shifts, and melatonin, the sleep hormone, is released up to two hours later than in children or adults."),
  L("Παιδίατρος", "m", "Το αποτέλεσμα είναι ότι ένας έφηβος που πρέπει να είναι στην τάξη στις οχτώ παρά τέταρτο ζει μόνιμα με στέρηση ύπνου. Και η στέρηση ύπνου δεν σημαίνει απλώς νύστα: συνδέεται με χαμηλότερες επιδόσεις, περισσότερα τροχαία ατυχήματα και αυξημένο κίνδυνο κατάθλιψης. Γι’ αυτό η Αμερικανική Ακαδημία Παιδιατρικής συνιστά τα γυμνάσια και τα λύκεια να μην ξεκινούν πριν από τις οχτώ και μισή.", "The result is that a teenager who must be in class at a quarter to eight lives permanently with sleep deprivation. And sleep deprivation doesn't just mean drowsiness: it is linked to lower performance, more road accidents and an increased risk of depression. That is why the American Academy of Pediatrics recommends that secondary schools should not start before half past eight."),
  L("Παιδίατρος", "m", "Όταν το Σιάτλ μετέθεσε την έναρξη των μαθημάτων σχεδόν μία ώρα αργότερα, οι μαθητές κοιμούνταν κατά μέσο όρο μισή ώρα περισσότερο, και οι βαθμοί τους βελτιώθηκαν. Δεν είναι, βέβαια, μια απλή αλλαγή: επηρεάζει τα δρομολόγια των λεωφορείων, τα απογευματινά φροντιστήρια και το ωράριο των γονιών. Αλλά αξίζει τουλάχιστον να το συζητήσουμε, αντί να κατηγορούμε τους εφήβους για κάτι που, σε μεγάλο βαθμό, δεν ελέγχουν.", "When Seattle moved the start of classes almost an hour later, students slept on average half an hour longer, and their grades improved. It is not, of course, a simple change: it affects bus routes, afternoon tutoring schools and parents' working hours. But it is at least worth discussing, instead of blaming teenagers for something that, to a large extent, they don't control."),
 ],
 "questions": [
  Q("Τι συμβαίνει στον οργανισμό των εφήβων, σύμφωνα με τον ομιλητή;", ["Χρειάζονται λιγότερο ύπνο", "Η μελατονίνη εκκρίνεται έως και δύο ώρες αργότερα", "Κοιμούνται καλύτερα με το κινητό", "Ξυπνούν πιο εύκολα από τους ενήλικες"], 1, "η μελατονίνη, η ορμόνη του ύπνου, εκκρίνεται έως και δύο ώρες αργότερα"),
  Q("Τι συνιστά η Αμερικανική Ακαδημία Παιδιατρικής;", ["Να απαγορευτούν τα κινητά στα σχολεία", "Τα γυμνάσια και τα λύκεια να μην ξεκινούν πριν από τις οχτώ και μισή", "Οι έφηβοι να κοιμούνται το μεσημέρι", "Να μειωθούν οι ώρες των μαθημάτων"], 1, "τα γυμνάσια και τα λύκεια να μην ξεκινούν πριν από τις οχτώ και μισή"),
  Q("Τι έγινε όταν το Σιάτλ άλλαξε το ωράριο;", ["Οι μαθητές άργησαν περισσότερο", "Οι μαθητές κοιμούνταν μισή ώρα περισσότερο και οι βαθμοί τους βελτιώθηκαν", "Οι γονείς αντέδρασαν και το ωράριο άλλαξε ξανά", "Δεν παρατηρήθηκε καμία διαφορά"], 1, "οι μαθητές κοιμούνταν κατά μέσο όρο μισή ώρα περισσότερο"),
 ],
 "gloss": {"εφήβων": "έφηβος — teenager", "τεμπελιά": "τεμπελιά — laziness", "εφηβεία": "εφηβεία — adolescence", "μετατοπίζεται": "μετατοπίζομαι — to shift", "εκκρίνεται": "εκκρίνομαι — to be secreted, released", "στέρηση ύπνου": "στέρηση ύπνου — sleep deprivation", "νύστα": "νύστα — drowsiness", "κατάθλιψης": "κατάθλιψη — depression", "μετέθεσε": "μεταθέτω — to move, postpone", "φροντιστήρια": "φροντιστήριο — tutoring school (cram school)"},
})

rnd = random.Random(85)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-85.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
