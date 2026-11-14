# Source for library/listening/listening-15.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l15.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l15-ann-tachydromeio", "title": "Αλλαγές στο ταχυδρομείο", "title_en": "Changes at the post office", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση στο κατάστημα ταχυδρομείου της γειτονιάς σας.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί πελάτες, σας ενημερώνουμε ότι από την πρώτη Δεκεμβρίου το κατάστημά μας θα λειτουργεί μόνο πρωινές ώρες, από τις επτάμισι έως τις δύο και μισή, από Δευτέρα έως Παρασκευή.", "Dear customers, we inform you that from the first of December our branch will open only in the morning, from half past seven to half past two, Monday to Friday."),
  L("Εκφωνητής", "m", "Οι συστημένες επιστολές και τα δέματα που δεν παραδόθηκαν θα φυλάσσονται εδώ για δέκα εργάσιμες ημέρες. Μετά από αυτό το διάστημα, επιστρέφονται στον αποστολέα.", "Registered letters and parcels that could not be delivered will be kept here for ten working days. After that period, they are returned to the sender."),
  L("Εκφωνητής", "m", "Για να αποφύγετε την αναμονή, μπορείτε να παραλαμβάνετε τα δέματά σας από τις αυτόματες θυρίδες που τοποθετήθηκαν δίπλα στην είσοδο και λειτουργούν όλο το εικοσιτετράωρο. Θα χρειαστείτε μόνο τον κωδικό που θα λάβετε με γραπτό μήνυμα.", "To avoid queuing, you can collect your parcels from the automatic lockers installed next to the entrance, which operate around the clock. You will only need the code you will receive by text message."),
 ],
 "questions": [
  Q("Τι θα αλλάξει από την πρώτη Δεκεμβρίου;", ["Το κατάστημα θα κλείσει οριστικά", "Το κατάστημα θα ανοίγει μόνο το πρωί", "Το κατάστημα θα ανοίγει και τα Σάββατα", "Οι τιμές των αποστολών θα αυξηθούν"], 1, "θα λειτουργεί μόνο πρωινές ώρες"),
  Q("Τι γίνεται με ένα δέμα που δεν παραλαμβάνεται σε δέκα εργάσιμες;", ["Καταστρέφεται", "Πηγαίνει στις θυρίδες", "Επιστρέφει στον αποστολέα", "Παραδίδεται στον γείτονα"], 2, "επιστρέφονται στον αποστολέα"),
  Q("Τι χρειάζεται κανείς για να χρησιμοποιήσει τις αυτόματες θυρίδες;", ["Την ταυτότητά του", "Έναν κωδικό από γραπτό μήνυμα", "Μια ειδική κάρτα", "Ραντεβού με τον υπάλληλο"], 1, "Θα χρειαστείτε μόνο τον κωδικό που θα λάβετε με γραπτό μήνυμα"),
 ],
 "gloss": {"κατάστημα ταχυδρομείου": "κατάστημα ταχυδρομείου — post office (branch)", "συστημένες επιστολές": "συστημένη επιστολή — registered letter", "δέματα": "δέμα — parcel", "θα φυλάσσονται": "φυλάσσομαι — to be kept, stored", "εργάσιμες ημέρες": "εργάσιμη ημέρα — working day", "αποστολέα": "αποστολέας — sender", "αναμονή": "αναμονή — waiting, queue", "αυτόματες θυρίδες": "αυτόματη θυρίδα — parcel locker", "όλο το εικοσιτετράωρο": "όλο το εικοσιτετράωρο — around the clock", "γραπτό μήνυμα": "γραπτό μήνυμα — text message, SMS"},
})

ITEMS.append({
 "id": "l15-vm-fysikotherapeftis", "title": "Μήνυμα από τον φυσικοθεραπευτή", "title_en": "A message from the physiotherapist", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από ένα κέντρο φυσικοθεραπείας προς μια ασθενή.",
 "script": [
  L("Φυσικοθεραπευτής", "m", "Καλημέρα σας, κυρία Παπαδάκη, ο Στέλιος είμαι από το κέντρο φυσικοθεραπείας. Δυστυχώς θα λείπω σε ένα συνέδριο την ερχόμενη εβδομάδα, οπότε οι δύο συνεδρίες σας, της Τρίτης και της Πέμπτης, πρέπει να μετακινηθούν.", "Good morning, Mrs Papadaki, it's Stelios from the physiotherapy centre. Unfortunately I'll be away at a conference next week, so your two sessions, on Tuesday and Thursday, need to be moved."),
  L("Φυσικοθεραπευτής", "m", "Σας προτείνω δύο λύσεις: είτε να κάνετε τις συνεδρίες με τη συνάδελφό μου, την κυρία Ρένα, στις ίδιες ώρες, είτε να τις προσθέσουμε στο τέλος του προγράμματος, ώστε να μη χάσετε καμία από τις δέκα που σας έγραψε ο ορθοπεδικός.", "I can suggest two solutions: either you do the sessions with my colleague, Ms Rena, at the same times, or we add them at the end of the programme, so you don't lose any of the ten the orthopaedist prescribed."),
  L("Φυσικοθεραπευτής", "m", "Στο μεταξύ, μη σταματήσετε τις ασκήσεις για τον ώμο που σας έδειξα· κάντε τις δύο φορές τη μέρα, χωρίς να πιέζετε αν νιώσετε πόνο. Πάρτε με όταν μπορέσετε για να μου πείτε τι προτιμάτε.", "In the meantime, don't stop the shoulder exercises I showed you; do them twice a day, without forcing it if you feel pain. Call me when you can to tell me what you prefer."),
 ],
 "questions": [
  Q("Γιατί πρέπει να αλλάξουν οι συνεδρίες;", ["Επειδή η ασθενής θα ταξιδέψει", "Επειδή ο φυσικοθεραπευτής θα λείπει σε συνέδριο", "Επειδή το κέντρο θα κλείσει για ανακαίνιση", "Επειδή ο ορθοπεδικός άλλαξε τη θεραπεία"], 1, "θα λείπω σε ένα συνέδριο την ερχόμενη εβδομάδα"),
  Q("Ποια είναι μία από τις λύσεις που προτείνει;", ["Να ακυρωθούν οι δύο συνεδρίες", "Να γίνουν οι συνεδρίες στο σπίτι της", "Να κάνει τις συνεδρίες με μια συνάδελφό του", "Να πάει ξανά στον ορθοπεδικό"], 2, "να κάνετε τις συνεδρίες με τη συνάδελφό μου"),
  Q("Τι πρέπει να κάνει η ασθενής στο μεταξύ;", ["Να ξεκουράσει εντελώς τον ώμο", "Να συνεχίσει τις ασκήσεις δύο φορές τη μέρα", "Να παίρνει παυσίπονα", "Να βάζει πάγο κάθε βράδυ"], 1, "κάντε τις δύο φορές τη μέρα"),
 ],
 "gloss": {"κέντρο φυσικοθεραπείας": "κέντρο φυσικοθεραπείας — physiotherapy centre", "συνέδριο": "συνέδριο — conference", "συνεδρίες": "συνεδρία — (therapy) session", "να μετακινηθούν": "μετακινούμαι — to be moved, rescheduled", "συνάδελφό": "συνάδελφος — colleague", "ορθοπεδικός": "ορθοπεδικός — orthopaedist", "ώμο": "ώμος — shoulder", "να πιέζετε": "πιέζω — to push, force", "Πάρτε με": "παίρνω (τηλέφωνο) — to call"},
})

ITEMS.append({
 "id": "l15-dia-vaftisi", "title": "Το τραπέζι της βάφτισης", "title_en": "The christening lunch", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια τηλεφωνική συζήτηση ανάμεσα σε μια μητέρα και τον ιδιοκτήτη μιας ταβέρνας.",
 "script": [
  L("Μαρίνα", "f", "Καλησπέρα σας. Βαφτίζουμε τον γιο μας στις είκοσι Απριλίου, στο εκκλησάκι του Αγίου Νικολάου, και θα θέλαμε να κάνουμε το τραπέζι σε εσάς. Θα είμαστε γύρω στα εβδομήντα άτομα.", "Good evening. We're christening our son on the twentieth of April, at the little church of Saint Nicholas, and we'd like to have the lunch at your place. We'll be about seventy people."),
  L("Ιδιοκτήτης", "m", "Χαρά μας! Για τόσα άτομα σας προτείνω την αυλή κάτω από τα πλατάνια. Έχουμε δύο μενού: το ένα με ορεκτικά, σαλάτες και κρέας στη σούβλα, το άλλο με ψάρι. Τα παιδιά κάτω των έξι δεν χρεώνονται.", "Our pleasure! For that many people I'd suggest the courtyard under the plane trees. We have two menus: one with starters, salads and spit-roasted meat, the other with fish. Children under six are free."),
  L("Μαρίνα", "f", "Τέλεια, το κρέας μάλλον. Μπορούμε να φέρουμε εμείς τα κουφέτα και την τούρτα; Και θα ήθελα να ρωτήσω αν μπορεί να έρθει ένα μικρό συγκρότημα με κλαρίνο και λαούτο.", "Perfect, the meat probably. Can we bring the sugared almonds and the cake ourselves? And I wanted to ask if a small band with clarinet and lute can come."),
  L("Ιδιοκτήτης", "m", "Και βέβαια, η μουσική επιτρέπεται ως τις έξι το απόγευμα, λόγω των γειτόνων. Για να κλείσουμε την ημερομηνία, χρειάζομαι μια προκαταβολή διακοσίων ευρώ ως το τέλος του μήνα.", "Of course, music is allowed until six in the evening, because of the neighbours. To book the date, I need a deposit of two hundred euros by the end of the month."),
 ],
 "questions": [
  Q("Πού προτείνει ο ιδιοκτήτης να γίνει το τραπέζι;", ["Στη μεγάλη αίθουσα", "Στην αυλή κάτω από τα πλατάνια", "Στην παραλία", "Στο προαύλιο της εκκλησίας"], 1, "την αυλή κάτω από τα πλατάνια"),
  Q("Τι θέλει να φέρει η ίδια η Μαρίνα;", ["Το κρασί", "Τα κουφέτα και την τούρτα", "Τα λουλούδια και τα τραπεζομάντιλα", "Το ψάρι"], 1, "Μπορούμε να φέρουμε εμείς τα κουφέτα και την τούρτα;"),
  Q("Ποιος περιορισμός υπάρχει για τη μουσική;", ["Δεν επιτρέπεται καθόλου", "Επιτρέπεται μόνο από ηχεία", "Επιτρέπεται ως τις έξι το απόγευμα", "Πρέπει να τη διαλέξει η ταβέρνα"], 2, "η μουσική επιτρέπεται ως τις έξι το απόγευμα"),
 ],
 "gloss": {"Βαφτίζουμε": "βαφτίζω — to christen, baptise", "εκκλησάκι": "εκκλησάκι — little church, chapel", "πλατάνια": "πλάτανος — plane tree", "ορεκτικά": "ορεκτικό — starter", "κρέας στη σούβλα": "κρέας στη σούβλα — spit-roasted meat", "δεν χρεώνονται": "χρεώνομαι — to be charged", "κουφέτα": "κουφέτο — sugared almond (given at weddings and christenings)", "συγκρότημα": "συγκρότημα — band", "κλαρίνο": "κλαρίνο — clarinet", "λαούτο": "λαούτο — lute (Greek folk lute)", "να κλείσουμε την ημερομηνία": "κλείνω την ημερομηνία — to book the date", "προκαταβολή": "προκαταβολή — deposit"},
})

ITEMS.append({
 "id": "l15-dia-afm", "title": "Αριθμός φορολογικού μητρώου", "title_en": "Getting a tax number", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε μια εφορία ανάμεσα σε έναν ξένο και μια υπάλληλο.",
 "script": [
  L("Τομ", "m", "Καλημέρα. Ήρθα πρόσφατα στην Ελλάδα για δουλειά και ο εργοδότης μου μού ζήτησε ΑΦΜ για να με προσλάβει. Τι πρέπει να κάνω;", "Good morning. I came to Greece recently for work and my employer asked me for a tax number in order to hire me. What do I need to do?"),
  L("Υπάλληλος", "f", "Θα χρειαστώ το διαβατήριό σας ή την ταυτότητά σας, αν είστε πολίτης της Ευρωπαϊκής Ένωσης, και ένα αποδεικτικό διεύθυνσης εδώ, για παράδειγμα το μισθωτήριο του σπιτιού ή έναν λογαριασμό ρεύματος στο όνομά σας.", "I'll need your passport, or your identity card if you are an EU citizen, and proof of an address here, for example the lease for your home or an electricity bill in your name."),
  L("Τομ", "m", "Το συμβόλαιο ενοικίασης το έχω, αλλά είναι μόνο στα ελληνικά. Πρέπει να το μεταφράσω;", "I have the rental contract, but it's only in Greek. Do I have to translate it?"),
  L("Υπάλληλος", "f", "Όχι, αφού είναι ελληνικό έγγραφο, δεν χρειάζεται. Μετάφραση θέλουν μόνο τα ξενόγλωσσα έγγραφα. Συμπληρώστε αυτή την αίτηση και ο αριθμός θα εκδοθεί σήμερα κιόλας. Μετά, με τον ΑΦΜ, θα πάρετε και ΑΜΚΑ για την ασφάλισή σας.", "No, since it's a Greek document, there's no need. Only documents in foreign languages need translating. Fill in this form and the number will be issued today. Then, with the tax number, you'll also get a social security number for your insurance."),
 ],
 "questions": [
  Q("Γιατί χρειάζεται ο Τομ ΑΦΜ;", ["Για να νοικιάσει σπίτι", "Για να τον προσλάβει ο εργοδότης του", "Για να ανοίξει λογαριασμό στην τράπεζα", "Για να αγοράσει αυτοκίνητο"], 1, "ο εργοδότης μου μού ζήτησε ΑΦΜ για να με προσλάβει"),
  Q("Χρειάζεται μετάφραση το μισθωτήριο του Τομ;", ["Ναι, επίσημη μετάφραση", "Ναι, αλλά απλή", "Όχι, γιατί είναι ελληνικό έγγραφο", "Όχι, γιατί δεν χρειάζεται αποδεικτικό διεύθυνσης"], 2, "αφού είναι ελληνικό έγγραφο, δεν χρειάζεται"),
  Q("Πότε θα εκδοθεί ο αριθμός;", ["Την ίδια μέρα", "Σε μία εβδομάδα", "Αφού πάρει ΑΜΚΑ", "Μετά τη μετάφραση"], 0, "ο αριθμός θα εκδοθεί σήμερα κιόλας"),
 ],
 "gloss": {"εφορία": "εφορία — tax office", "εργοδότης": "εργοδότης — employer", "ΑΦΜ": "ΑΦΜ (Αριθμός Φορολογικού Μητρώου) — tax identification number", "να με προσλάβει": "προσλαμβάνω — to hire", "αποδεικτικό διεύθυνσης": "αποδεικτικό διεύθυνσης — proof of address", "μισθωτήριο": "μισθωτήριο — lease", "συμβόλαιο ενοικίασης": "συμβόλαιο ενοικίασης — rental contract", "ξενόγλωσσα έγγραφα": "ξενόγλωσσο έγγραφο — document in a foreign language", "θα εκδοθεί": "εκδίδομαι — to be issued", "ΑΜΚΑ": "ΑΜΚΑ — social security number", "ασφάλισή": "ασφάλιση — (social) insurance"},
})

ITEMS.append({
 "id": "l15-mon-choros", "title": "Μαθαίνοντας παραδοσιακούς χορούς", "title_en": "Learning traditional dances", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλάει για το τμήμα παραδοσιακών χορών όπου γράφτηκε.",
 "script": [
  L("Δανάη", "f", "Πριν από δύο χρόνια γράφτηκα σε ένα τμήμα παραδοσιακών χορών σε έναν πολιτιστικό σύλλογο της γειτονιάς μου. Ντρεπόμουν, γιατί σε κάθε γάμο έμενα στην άκρη, ενώ όλοι οι άλλοι έπιαναν τον κύκλο.", "Two years ago I signed up for a traditional dance class at a cultural association in my neighbourhood. I was embarrassed, because at every wedding I stayed on the sidelines while everyone else joined the circle."),
  L("Δανάη", "f", "Ξεκινήσαμε με τον συρτό και τον καλαματιανό, που χορεύονται σχεδόν παντού. Ο δάσκαλος μας εξηγούσε από πού κατάγεται κάθε χορός και τι λένε τα τραγούδια. Ο καλαματιανός, για παράδειγμα, έχει ρυθμό επτά χρόνων, γι' αυτό στην αρχή μπερδευόμουν συνέχεια.", "We started with the syrtos and the kalamatianos, which are danced almost everywhere. The teacher explained where each dance comes from and what the songs say. The kalamatianos, for example, is in seven beats, which is why I kept getting confused at first."),
  L("Δανάη", "f", "Αυτό που δεν περίμενα ήταν η παρέα. Μετά το μάθημα πηγαίνουμε για τσίπουρο, και το καλοκαίρι ο σύλλογος οργανώνει εκδρομές σε πανηγύρια στα χωριά. Πέρσι χόρεψα για πρώτη φορά μπροστά, στην πρώτη θέση του κύκλου, και ένιωσα ότι πια ανήκω κάπου.", "What I didn't expect was the company. After class we go for tsipouro, and in summer the association organises trips to village festivals. Last year, for the first time, I danced at the front, leading the circle, and I felt that I finally belong somewhere."),
 ],
 "questions": [
  Q("Γιατί γράφτηκε η Δανάη στο τμήμα χορού;", ["Για να γνωρίσει τον μελλοντικό της σύζυγο", "Γιατί ντρεπόταν που δεν χόρευε στους γάμους", "Γιατί της το πρότεινε ο γιατρός της", "Για να γίνει δασκάλα χορού"], 1, "Ντρεπόμουν, γιατί σε κάθε γάμο έμενα στην άκρη"),
  Q("Γιατί δυσκολευόταν στην αρχή με τον καλαματιανό;", ["Γιατί είναι πολύ γρήγορος", "Γιατί χορεύεται μόνο στην Καλαμάτα", "Γιατί έχει ρυθμό επτά χρόνων", "Γιατί δεν καταλάβαινε τα τραγούδια"], 2, "έχει ρυθμό επτά χρόνων, γι' αυτό στην αρχή μπερδευόμουν συνέχεια"),
  Q("Τι ήταν αυτό που δεν περίμενε η Δανάη;", ["Τη δυσκολία των χορών", "Το κόστος των μαθημάτων", "Την παρέα που απέκτησε", "Τα ταξίδια στο εξωτερικό"], 2, "Αυτό που δεν περίμενα ήταν η παρέα"),
 ],
 "gloss": {"τμήμα παραδοσιακών χορών": "τμήμα παραδοσιακών χορών — traditional dance class", "πολιτιστικό σύλλογο": "πολιτιστικός σύλλογος — cultural association", "Ντρεπόμουν": "ντρέπομαι — to be embarrassed, shy", "έπιαναν τον κύκλο": "πιάνω τον κύκλο — to join the (dance) circle", "συρτό": "συρτός — syrtos (Greek circle dance)", "καλαματιανό": "καλαματιανός — kalamatianos (dance in 7/8)", "κατάγεται": "κατάγομαι — to come from, originate", "ρυθμό επτά χρόνων": "ρυθμός επτά χρόνων — seven-beat rhythm (7/8)", "μπερδευόμουν": "μπερδεύομαι — to get confused", "τσίπουρο": "τσίπουρο — tsipouro (grape spirit)", "πανηγύρια": "πανηγύρι — village (saint's day) festival", "ανήκω": "ανήκω — to belong"},
})

ITEMS.append({
 "id": "l15-rep-prespes", "title": "Οι πελεκάνοι των Πρεσπών", "title_en": "The pelicans of Prespa", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από τις λίμνες Πρέσπες, στη Μακεδονία.",
 "script": [
  L("Δημοσιογράφος", "f", "Βρισκόμαστε στις Πρέσπες, στα σύνορα της Ελλάδας με την Αλβανία και τη Βόρεια Μακεδονία. Η Μεγάλη Πρέσπα μοιράζεται ανάμεσα στις τρεις χώρες, ενώ η Μικρή Πρέσπα ανήκει σχεδόν ολόκληρη στην Ελλάδα. Εδώ ζει η μεγαλύτερη αποικία αργυροπελεκάνων στον κόσμο.", "We are at Prespa, on Greece's border with Albania and North Macedonia. Great Prespa is shared among the three countries, while Small Prespa belongs almost entirely to Greece. The world's largest colony of Dalmatian pelicans lives here."),
  L("Δημοσιογράφος", "f", "Την άνοιξη, οι πελεκάνοι φωλιάζουν στους καλαμιώνες της λίμνης. Οι ορνιθολόγοι ζητούν από τους επισκέπτες να τους παρατηρούν από μακριά, από τα ειδικά παρατηρητήρια, γιατί η ανθρώπινη παρουσία μπορεί να τους αναγκάσει να εγκαταλείψουν τις φωλιές τους.", "In spring, the pelicans nest in the lake's reed beds. Ornithologists ask visitors to watch them from a distance, from the special observation hides, because human presence can force them to abandon their nests."),
  L("Δημοσιογράφος", "f", "Οι κάτοικοι της περιοχής ζουν κυρίως από την καλλιέργεια των φασολιών, των γνωστών γιγάντων Πρεσπών, και, όλο και περισσότερο, από τον οικοτουρισμό. Στη μικρή λίμνη, ένα πλωτό γεφύρι οδηγεί στο νησάκι του Αγίου Αχιλλείου, με τα ερείπια μιας βυζαντινής βασιλικής.", "Local residents live mainly from growing beans, the well-known Prespa giant beans, and, more and more, from ecotourism. On the small lake, a floating footbridge leads to the islet of Agios Achilleios, with the ruins of a Byzantine basilica."),
 ],
 "questions": [
  Q("Τι ξεχωρίζει τις Πρέσπες, σύμφωνα με το ρεπορτάζ;", ["Είναι η βαθύτερη λίμνη της Ευρώπης", "Φιλοξενούν τη μεγαλύτερη αποικία αργυροπελεκάνων στον κόσμο", "Ανήκουν ολόκληρες στην Ελλάδα", "Έχουν θερμές πηγές"], 1, "Εδώ ζει η μεγαλύτερη αποικία αργυροπελεκάνων στον κόσμο"),
  Q("Γιατί πρέπει οι επισκέπτες να παρατηρούν τα πουλιά από μακριά;", ["Γιατί οι πελεκάνοι είναι επιθετικοί", "Γιατί η παρουσία τους μπορεί να τα κάνει να εγκαταλείψουν τις φωλιές", "Γιατί απαγορεύεται η φωτογράφιση", "Γιατί οι καλαμιώνες είναι επικίνδυνοι"], 1, "η ανθρώπινη παρουσία μπορεί να τους αναγκάσει να εγκαταλείψουν τις φωλιές τους"),
  Q("Από τι ζουν κυρίως οι κάτοικοι;", ["Από το ψάρεμα", "Από την κτηνοτροφία", "Από την καλλιέργεια φασολιών και τον οικοτουρισμό", "Από τη βιομηχανία"], 2, "ζουν κυρίως από την καλλιέργεια των φασολιών"),
 ],
 "gloss": {"σύνορα": "σύνορα — border", "μοιράζεται": "μοιράζομαι — to be shared", "αποικία": "αποικία — colony", "αργυροπελεκάνων": "αργυροπελεκάνος — Dalmatian pelican", "φωλιάζουν": "φωλιάζω — to nest", "καλαμιώνες": "καλαμιώνας — reed bed", "ορνιθολόγοι": "ορνιθολόγος — ornithologist", "παρατηρητήρια": "παρατηρητήριο — observation hide", "να εγκαταλείψουν": "εγκαταλείπω — to abandon", "γιγάντων": "γίγαντες — giant beans", "οικοτουρισμό": "οικοτουρισμός — ecotourism", "πλωτό γεφύρι": "πλωτό γεφύρι — floating footbridge", "ερείπια": "ερείπια — ruins", "βασιλικής": "βασιλική — basilica"},
})

ITEMS.append({
 "id": "l15-rep-masticha", "title": "Τα δάκρυα της Χίου", "title_en": "The tears of Chios", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα τηλεοπτικό ρεπορτάζ για τη μαστίχα της Χίου.",
 "script": [
  L("Δημοσιογράφος", "m", "Στα μαστιχοχώρια της νότιας Χίου, όπως το Πυργί και τα Μεστά, η καλλιέργεια του μαστιχόδεντρου συνεχίζεται εδώ και αιώνες. Το δέντρο, ο σχίνος, φυτρώνει και σε άλλα μέρη της Μεσογείου, αλλά μόνο εδώ δίνει μαστίχα σε εμπορική ποσότητα.", "In the mastic villages of southern Chios, such as Pyrgi and Mesta, the cultivation of the mastic tree has continued for centuries. The tree, the lentisk, grows in other parts of the Mediterranean too, but only here does it yield mastic in commercial quantities."),
  L("Δημοσιογράφος", "m", "Τον χειμώνα οι παραγωγοί καθαρίζουν το έδαφος γύρω από κάθε δέντρο και το στρώνουν με άσπρο χώμα. Το καλοκαίρι κεντούν τον κορμό με ένα αιχμηρό εργαλείο, και η ρητίνη τρέχει σαν δάκρυα και πέφτει στο χώμα, όπου στεγνώνει.", "In winter the growers clear the ground around each tree and spread it with white earth. In summer they score the trunk with a sharp tool, and the resin runs like tears and falls onto the ground, where it dries."),
  L("Δημοσιογράφος", "m", "Η γνώση της καλλιέργειας της μαστίχας έχει ενταχθεί από την UNESCO στην άυλη πολιτιστική κληρονομιά της ανθρωπότητας. Σήμερα η μαστίχα χρησιμοποιείται στη ζαχαροπλαστική, στα ποτά και στα καλλυντικά, αλλά οι παραγωγοί ανησυχούν για τη γήρανση του πληθυσμού και για τις πυρκαγιές, όπως αυτή του 2012, που έκαψε χιλιάδες δέντρα.", "The know-how of mastic cultivation has been inscribed by UNESCO on the intangible cultural heritage of humanity. Today mastic is used in confectionery, drinks and cosmetics, but growers worry about the ageing population and about wildfires, such as the one in 2012 that burned thousands of trees."),
 ],
 "questions": [
  Q("Τι ισχύει για τον σχίνο;", ["Φυτρώνει μόνο στη Χίο", "Δίνει μαστίχα σε εμπορική ποσότητα μόνο στη Χίο", "Καλλιεργείται μόνο τα τελευταία χρόνια", "Δεν χρειάζεται καμία φροντίδα"], 1, "μόνο εδώ δίνει μαστίχα σε εμπορική ποσότητα"),
  Q("Πώς συλλέγεται η μαστίχα;", ["Κόβουν τα κλαδιά του δέντρου", "Κεντούν τον κορμό και η ρητίνη πέφτει στο χώμα", "Βράζουν τα φύλλα", "Τινάζουν το δέντρο με ραβδιά"], 1, "κεντούν τον κορμό με ένα αιχμηρό εργαλείο"),
  Q("Τι ανησυχεί τους παραγωγούς;", ["Οι χαμηλές τιμές στο εξωτερικό", "Η γήρανση του πληθυσμού και οι πυρκαγιές", "Οι νέοι κανόνες της UNESCO", "Η έλλειψη άσπρου χώματος"], 1, "οι παραγωγοί ανησυχούν για τη γήρανση του πληθυσμού και για τις πυρκαγιές"),
 ],
 "gloss": {"μαστίχα": "μαστίχα — mastic (resin)", "μαστιχοχώρια": "μαστιχοχώρια — the mastic villages of Chios", "μαστιχόδεντρου": "μαστιχόδεντρο — mastic tree", "σχίνος": "σχίνος — lentisk, mastic bush", "φυτρώνει": "φυτρώνω — to grow, sprout", "εμπορική ποσότητα": "εμπορική ποσότητα — commercial quantity", "το στρώνουν": "στρώνω — to spread, cover", "κεντούν": "κεντώ — to prick, score (the bark)", "κορμό": "κορμός — trunk", "αιχμηρό": "αιχμηρός — sharp, pointed", "ρητίνη": "ρητίνη — resin", "άυλη πολιτιστική κληρονομιά": "άυλη πολιτιστική κληρονομιά — intangible cultural heritage", "ζαχαροπλαστική": "ζαχαροπλαστική — confectionery", "γήρανση": "γήρανση — ageing"},
})

ITEMS.append({
 "id": "l15-int-syntiritria", "title": "Η συντηρήτρια εικόνων", "title_en": "The icon conservator", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια συντηρήτρια που δουλεύει σε βυζαντινές εικόνες.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αλεξίου, τι ακριβώς κάνει ένας συντηρητής έργων τέχνης;", "Ms Alexiou, what exactly does an art conservator do?"),
  L("Συντηρήτρια", "f", "Η δουλειά μας είναι να σταματήσουμε τη φθορά ενός έργου και να το διατηρήσουμε όσο γίνεται πιο κοντά στη μορφή που είχε. Δεν «ξαναζωγραφίζουμε» τις εικόνες. Αν λείπει ένα κομμάτι, το συμπληρώνουμε με τρόπο που να φαίνεται από κοντά, ώστε να μην εξαπατάμε τον θεατή.", "Our job is to stop the deterioration of a work and preserve it as close as possible to the form it had. We don't 'repaint' icons. If a piece is missing, we fill it in a way that is visible close up, so as not to deceive the viewer."),
  L("Δημοσιογράφος", "m", "Ποιος είναι ο μεγαλύτερος εχθρός μιας παλιάς εικόνας;", "What is the greatest enemy of an old icon?"),
  L("Συντηρήτρια", "f", "Η υγρασία και οι απότομες αλλαγές θερμοκρασίας. Το ξύλο φουσκώνει και συρρικνώνεται, και η ζωγραφική επιφάνεια ξεκολλάει. Και φυσικά ο καπνός από τα κεριά, που μαυρίζει τα χρώματα. Πολλές φορές, όταν καθαρίζουμε μια εικόνα, ανακαλύπτουμε από κάτω μια παλαιότερη ζωγραφική, που κανείς δεν ήξερε ότι υπήρχε. Είναι η πιο συγκινητική στιγμή της δουλειάς μου.", "Humidity and sudden changes of temperature. The wood swells and shrinks, and the painted surface comes away. And of course the smoke from candles, which blackens the colours. Often, when we clean an icon, we discover an older painting underneath that nobody knew existed. It's the most moving moment of my work."),
 ],
 "questions": [
  Q("Πώς συμπληρώνει η συντηρήτρια ένα κομμάτι που λείπει;", ["Το ξαναζωγραφίζει όπως ήταν", "Με τρόπο που να φαίνεται από κοντά", "Δεν το συμπληρώνει ποτέ", "Με ένα κομμάτι από άλλη εικόνα"], 1, "το συμπληρώνουμε με τρόπο που να φαίνεται από κοντά"),
  Q("Ποιος είναι ο μεγαλύτερος εχθρός των εικόνων;", ["Το φως του ήλιου", "Τα έντομα", "Η υγρασία και οι απότομες αλλαγές θερμοκρασίας", "Οι κλέφτες"], 2, "Η υγρασία και οι απότομες αλλαγές θερμοκρασίας"),
  Q("Ποια είναι η πιο συγκινητική στιγμή της δουλειάς της;", ["Όταν επιστρέφει μια εικόνα στην εκκλησία", "Όταν ανακαλύπτει μια παλαιότερη ζωγραφική από κάτω", "Όταν τελειώνει μια δύσκολη συντήρηση", "Όταν οι πιστοί προσκυνούν την εικόνα"], 1, "ανακαλύπτουμε από κάτω μια παλαιότερη ζωγραφική"),
 ],
 "gloss": {"συντηρήτρια": "συντηρήτρια — (female) conservator", "συντηρητής": "συντηρητής — conservator", "φθορά": "φθορά — deterioration, wear", "να το διατηρήσουμε": "διατηρώ — to preserve", "το συμπληρώνουμε": "συμπληρώνω — to fill in, complete", "να μην εξαπατάμε": "εξαπατώ — to deceive", "εχθρός": "εχθρός — enemy", "υγρασία": "υγρασία — humidity, damp", "φουσκώνει": "φουσκώνω — to swell", "συρρικνώνεται": "συρρικνώνομαι — to shrink", "ξεκολλάει": "ξεκολλάω — to come unstuck, peel off", "μαυρίζει": "μαυρίζω — to blacken", "συγκινητική": "συγκινητικός — moving, touching"},
})

ITEMS.append({
 "id": "l15-mon-filellinismos", "title": "Ο φιλελληνισμός", "title_en": "Philhellenism", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη ιστορικού για το φιλελληνικό κίνημα της δεκαετίας του 1820.",
 "script": [
  L("Ιστορικός", "m", "Όταν ξέσπασε η Ελληνική Επανάσταση το 1821, οι κυβερνήσεις της Ευρώπης την αντιμετώπισαν με καχυποψία. Μετά την ήττα του Ναπολέοντα, η Ιερή Συμμαχία ήθελε να διατηρήσει την τάξη, και κάθε εξέγερση θεωρούνταν απειλή. Η κοινή γνώμη, όμως, κινήθηκε προς την αντίθετη κατεύθυνση.", "When the Greek Revolution broke out in 1821, Europe's governments viewed it with suspicion. After Napoleon's defeat, the Holy Alliance wanted to preserve order, and every uprising was seen as a threat. Public opinion, however, moved in the opposite direction."),
  L("Ιστορικός", "m", "Σε πόλεις όπως το Λονδίνο, το Παρίσι και η Γενεύη ιδρύθηκαν φιλελληνικές επιτροπές, που συγκέντρωναν χρήματα και όπλα. Εκατοντάδες εθελοντές ήρθαν να πολεμήσουν, και πολλοί σκοτώθηκαν ή πέθαναν από αρρώστιες. Ο πιο διάσημος, ο λόρδος Βύρων, πέθανε στο Μεσολόγγι το 1824, και ο θάνατός του συγκλόνισε την Ευρώπη.", "In cities such as London, Paris and Geneva, philhellenic committees were founded, raising money and weapons. Hundreds of volunteers came to fight, and many were killed or died of disease. The most famous, Lord Byron, died at Missolonghi in 1824, and his death shook Europe."),
  L("Ιστορικός", "m", "Η τέχνη έπαιξε κι αυτή τον ρόλο της. Ο Ντελακρουά, με τη «Σφαγή της Χίου», έφερε μπροστά στα μάτια του παρισινού κοινού τη βία του πολέμου. Αυτή η πίεση της κοινής γνώμης συνέβαλε, μαζί βέβαια με τους γεωπολιτικούς υπολογισμούς, στην απόφαση της Βρετανίας, της Γαλλίας και της Ρωσίας να παρέμβουν· η ναυμαχία του Ναβαρίνου, το 1827, ήταν η καμπή.", "Art played its part too. Delacroix, with 'The Massacre at Chios', brought the violence of the war before the eyes of the Parisian public. This pressure of public opinion contributed, together of course with geopolitical calculations, to the decision of Britain, France and Russia to intervene; the naval battle of Navarino, in 1827, was the turning point."),
  L("Ιστορικός", "m", "Θα ήταν αφελές, πάντως, να δούμε τον φιλελληνισμό μόνο ως ανιδιοτελή αγάπη. Πολλοί φιλέλληνες αγαπούσαν μια εξιδανικευμένη αρχαία Ελλάδα και απογοητεύτηκαν όταν συνάντησαν τους πραγματικούς Έλληνες της εποχής τους.", "It would be naive, however, to see philhellenism only as selfless love. Many philhellenes loved an idealised ancient Greece and were disappointed when they met the real Greeks of their own time."),
 ],
 "questions": [
  Q("Πώς αντιμετώπισαν αρχικά οι ευρωπαϊκές κυβερνήσεις την Επανάσταση;", ["Με ενθουσιασμό", "Με καχυποψία, γιατί κάθε εξέγερση θεωρούνταν απειλή", "Με αδιαφορία", "Με στρατιωτική βοήθεια"], 1, "οι κυβερνήσεις της Ευρώπης την αντιμετώπισαν με καχυποψία"),
  Q("Τι συνέβαλε στην απόφαση των τριών δυνάμεων να παρέμβουν, σύμφωνα με τον ομιλητή;", ["Μόνο η πίεση της κοινής γνώμης", "Μόνο οικονομικά συμφέροντα", "Η πίεση της κοινής γνώμης μαζί με γεωπολιτικούς υπολογισμούς", "Ο θάνατος του Ναπολέοντα"], 2, "μαζί βέβαια με τους γεωπολιτικούς υπολογισμούς"),
  Q("Γιατί απογοητεύτηκαν πολλοί φιλέλληνες;", ["Γιατί η Επανάσταση απέτυχε", "Γιατί οι πραγματικοί Έλληνες δεν έμοιαζαν με την εξιδανικευμένη εικόνα τους", "Γιατί δεν πληρώθηκαν", "Γιατί οι κυβερνήσεις τους τιμώρησαν"], 1, "απογοητεύτηκαν όταν συνάντησαν τους πραγματικούς Έλληνες της εποχής τους"),
 ],
 "gloss": {"φιλελληνικό κίνημα": "φιλελληνικό κίνημα — philhellenic movement", "ξέσπασε": "ξεσπώ — to break out", "καχυποψία": "καχυποψία — suspicion", "ήττα": "ήττα — defeat", "Ιερή Συμμαχία": "Ιερή Συμμαχία — Holy Alliance", "εξέγερση": "εξέγερση — uprising", "κοινή γνώμη": "κοινή γνώμη — public opinion", "επιτροπές": "επιτροπή — committee", "συγκλόνισε": "συγκλονίζω — to shake, shock", "Σφαγή της Χίου": "Σφαγή της Χίου — The Massacre at Chios (painting, 1824)", "συνέβαλε": "συμβάλλω — to contribute", "γεωπολιτικούς υπολογισμούς": "γεωπολιτικοί υπολογισμοί — geopolitical calculations", "να παρέμβουν": "παρεμβαίνω — to intervene", "ναυμαχία": "ναυμαχία — naval battle", "καμπή": "καμπή — turning point", "αφελές": "αφελής — naive", "ανιδιοτελή": "ανιδιοτελής — selfless", "εξιδανικευμένη": "εξιδανικευμένος — idealised"},
})

ITEMS.append({
 "id": "l15-int-dimografiko", "title": "Το δημογραφικό", "title_en": "Greece's demographic problem", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια δημογράφο για τη μείωση του πληθυσμού στην Ελλάδα.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Σταθοπούλου, πόσο σοβαρό είναι το δημογραφικό πρόβλημα της χώρας;", "Ms Stathopoulou, how serious is the country's demographic problem?"),
  L("Δημογράφος", "f", "Πολύ σοβαρό. Από το 2011 οι θάνατοι ξεπερνούν κάθε χρόνο τις γεννήσεις, και ο δείκτης γονιμότητας κυμαίνεται γύρω στο ένα κόμμα τρία, πολύ κάτω από το δύο κόμμα ένα που χρειάζεται για να ανανεωθεί ο πληθυσμός. Ανάμεσα στις απογραφές του 2011 και του 2021, ο πληθυσμός μειώθηκε κατά περίπου τετρακόσιες χιλιάδες ανθρώπους.", "Very serious. Since 2011 deaths have exceeded births every year, and the fertility rate hovers around one point three, well below the two point one needed for the population to replace itself. Between the 2011 and 2021 censuses, the population fell by about four hundred thousand people."),
  L("Δημοσιογράφος", "m", "Ποιες είναι οι αιτίες; Συχνά ακούμε ότι φταίει μόνο η οικονομική κρίση.", "What are the causes? We often hear that the economic crisis alone is to blame."),
  L("Δημογράφος", "f", "Η κρίση επιτάχυνε μια τάση που υπήρχε ήδη. Οι νέοι μένουν περισσότερο στο πατρικό τους, παντρεύονται αργότερα και κάνουν το πρώτο παιδί μετά τα τριάντα. Προστέθηκε και η μετανάστευση εκατοντάδων χιλιάδων νέων στο εξωτερικό. Τα επιδόματα γέννησης βοηθούν, αλλά από μόνα τους δεν αρκούν· χρειάζονται σταθερές δουλειές, προσιτή στέγη και παιδικοί σταθμοί, ώστε να μη χρειάζεται να διαλέξει κανείς ανάμεσα στην καριέρα και την οικογένεια.", "The crisis accelerated a trend that already existed. Young people stay longer in their parents' home, marry later and have their first child after thirty. On top of that came the emigration of hundreds of thousands of young people abroad. Birth allowances help, but on their own they are not enough; what is needed is stable jobs, affordable housing and nurseries, so that nobody has to choose between career and family."),
 ],
 "questions": [
  Q("Τι ισχύει από το 2011, σύμφωνα με τη δημογράφο;", ["Οι γεννήσεις ξεπερνούν τους θανάτους", "Οι θάνατοι ξεπερνούν κάθε χρόνο τις γεννήσεις", "Ο πληθυσμός αυξάνεται λόγω μετανάστευσης", "Ο δείκτης γονιμότητας έφτασε το δύο κόμμα ένα"], 1, "Από το 2011 οι θάνατοι ξεπερνούν κάθε χρόνο τις γεννήσεις"),
  Q("Ποιος ήταν ο ρόλος της οικονομικής κρίσης;", ["Ήταν η μόνη αιτία του προβλήματος", "Δεν έπαιξε κανέναν ρόλο", "Επιτάχυνε μια τάση που υπήρχε ήδη", "Αύξησε τις γεννήσεις"], 2, "Η κρίση επιτάχυνε μια τάση που υπήρχε ήδη"),
  Q("Τι πιστεύει η δημογράφος για τα επιδόματα γέννησης;", ["Ότι είναι η καλύτερη λύση", "Ότι βοηθούν, αλλά δεν αρκούν από μόνα τους", "Ότι πρέπει να καταργηθούν", "Ότι δεν βοηθούν καθόλου"], 1, "Τα επιδόματα γέννησης βοηθούν, αλλά από μόνα τους δεν αρκούν"),
 ],
 "gloss": {"δημογράφο": "δημογράφος — demographer", "δημογραφικό πρόβλημα": "δημογραφικό πρόβλημα — demographic problem", "ξεπερνούν": "ξεπερνώ — to exceed", "δείκτης γονιμότητας": "δείκτης γονιμότητας — fertility rate", "κυμαίνεται": "κυμαίνομαι — to range, hover", "να ανανεωθεί": "ανανεώνομαι — to be renewed, replace itself", "απογραφές": "απογραφή — census", "επιτάχυνε": "επιταχύνω — to accelerate", "τάση": "τάση — trend", "πατρικό": "πατρικό — parents' home", "μετανάστευση": "μετανάστευση — emigration", "επιδόματα γέννησης": "επίδομα γέννησης — birth allowance", "από μόνα τους": "από μόνος του — on its own", "προσιτή στέγη": "προσιτή στέγη — affordable housing", "παιδικοί σταθμοί": "παιδικός σταθμός — nursery, day care"},
})

rnd = random.Random(15)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-15.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
