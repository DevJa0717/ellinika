# Source for library/listening/listening-129.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l129.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l129-ann-apagoreftiko", "title": "Απαγορευτικό απόπλου στο λιμάνι", "title_en": "Ferries held in port by gale warning", "type": "announcement", "level": "B2",
 "context_el": "Περιμένετε στο λιμάνι του Πειραιά για να πάτε στις Κυκλάδες. Ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Παρακαλούνται οι επιβάτες για Σύρο, Τήνο και Μύκονο να προσέξουν: λόγω των ισχυρών βοριάδων, που φτάνουν τα εννιά μποφόρ στο Αιγαίο, το Λιμεναρχείο έχει εκδώσει απαγορευτικό απόπλου. Το πλοίο των επτά και μισή δεν θα αναχωρήσει στην ώρα του.", "Passengers for Syros, Tinos and Mykonos are asked to note: because of strong northerly winds reaching force nine in the Aegean, the Port Authority has issued a ban on sailing. The seven-thirty ship will not leave on time."),
  L("Εκφωνήτρια", "f", "Σύμφωνα με την πρόγνωση, οι άνεμοι θα εξασθενήσουν το απόγευμα. Η εταιρεία θα ενημερώσει με γραπτό μήνυμα όσους έχουν δηλώσει αριθμό κινητού για τη νέα ώρα αναχώρησης. Παρακαλούμε να παραμείνετε κοντά στο λιμάνι.", "According to the forecast, the winds will weaken in the afternoon. The company will inform by text message those who have registered a mobile number about the new departure time. Please remain near the port."),
  L("Εκφωνήτρια", "f", "Όσοι επιθυμούν να ακυρώσουν το ταξίδι τους μπορούν να πάρουν πίσω ολόκληρο το ποσό του εισιτηρίου από τα εκδοτήρια της εταιρείας, στην πύλη Ε7. Για τους επιβάτες με μικρά παιδιά, η αίθουσα αναμονής στον πρώτο όροφο παραμένει ανοιχτή.", "Those who wish to cancel their journey can get the full price of the ticket back from the company's ticket offices at gate E7. For passengers with small children, the waiting room on the first floor remains open."),
 ],
 "questions": [
  Q("Γιατί δεν θα αναχωρήσει το πλοίο στην ώρα του;", ["Λόγω βλάβης στη μηχανή", "Λόγω των ισχυρών ανέμων και του απαγορευτικού απόπλου", "Λόγω απεργίας", "Γιατί άργησε να φτάσει από τα νησιά"], 1, "το Λιμεναρχείο έχει εκδώσει απαγορευτικό απόπλου"),
  Q("Πώς θα μάθουν οι επιβάτες τη νέα ώρα αναχώρησης;", ["Από την ιστοσελίδα του λιμανιού", "Από την τηλεόραση", "Με γραπτό μήνυμα στο κινητό τους", "Από τα εκδοτήρια μόνο"], 2, "θα ενημερώσει με γραπτό μήνυμα όσους έχουν δηλώσει αριθμό κινητού"),
  Q("Τι μπορούν να κάνουν όσοι θέλουν να ακυρώσουν το ταξίδι;", ["Να πάρουν πίσω ολόκληρο το ποσό από τα εκδοτήρια στην πύλη Ε7", "Να αλλάξουν το εισιτήριο για αεροπλάνο", "Να πάρουν πίσω το μισό ποσό", "Να ζητήσουν δωρεάν ξενοδοχείο"], 0, "μπορούν να πάρουν πίσω ολόκληρο το ποσό του εισιτηρίου από τα εκδοτήρια της εταιρείας, στην πύλη Ε7"),
 ],
 "gloss": {"βοριάδων": "βοριάς — north wind", "μποφόρ": "μποφόρ — Beaufort (wind force)", "Λιμεναρχείο": "Λιμεναρχείο — Port Authority", "απαγορευτικό απόπλου": "απαγορευτικό απόπλου — ban on ships leaving port", "αναχωρήσει": "αναχωρώ — to depart", "πρόγνωση": "πρόγνωση — (weather) forecast", "εξασθενήσουν": "εξασθενώ — to weaken", "παραμείνετε": "παραμένω — to remain", "ακυρώσουν": "ακυρώνω — to cancel", "εκδοτήρια": "εκδοτήριο — ticket office", "αίθουσα αναμονής": "αίθουσα αναμονής — waiting room"}
})

ITEMS.append({
 "id": "l129-vm-metafrasi-ptyxion", "title": "Μήνυμα για τη μετάφραση των πτυχίων", "title_en": "A message about translating your degrees", "type": "voicemail", "level": "B2",
 "context_el": "Θέλετε να δουλέψετε στο εξωτερικό και δώσατε τα πτυχία σας για μετάφραση. Ακούτε ένα μήνυμα από τη μεταφράστρια.",
 "script": [
  L("Μεταφράστρια", "f", "Καλησπέρα, η Ευδοκία Ραφαηλίδου είμαι, από το μεταφραστικό γραφείο. Τελείωσα τη μετάφραση του πτυχίου και της αναλυτικής βαθμολογίας σας στα γερμανικά. Υπάρχει όμως ένα μικρό πρόβλημα με το πιστοποιητικό γέννησης.", "Good evening, it's Evdokia Rafailidou from the translation office. I've finished translating your degree and your transcript of marks into German. But there's a small problem with the birth certificate."),
  L("Μεταφράστρια", "f", "Το αντίγραφο που μου φέρατε είναι παλιό, και οι γερμανικές αρχές ζητούν πιστοποιητικό που να έχει εκδοθεί τους τελευταίους έξι μήνες. Μπορείτε να βγάλετε καινούργιο από το διαδίκτυο, μέσα σε λίγα λεπτά, και να μου το στείλετε με ηλεκτρονικό ταχυδρομείο.", "The copy you brought me is old, and the German authorities ask for a certificate issued within the last six months. You can get a new one online in a few minutes and send it to me by email."),
  L("Μεταφράστρια", "f", "Τα υπόλοιπα έγγραφα είναι έτοιμα και σφραγισμένα. Μπορείτε να περάσετε να τα πάρετε από την Τρίτη, μετά τις δέκα. Το γραφείο είναι κλειστό τη Δευτέρα, λόγω αργίας. Ευχαριστώ!", "The other documents are ready and stamped. You can come and pick them up from Tuesday, after ten. The office is closed on Monday because of a public holiday. Thank you!"),
 ],
 "questions": [
  Q("Ποιο έγγραφο έχει πρόβλημα;", ["Το πτυχίο", "Το πιστοποιητικό γέννησης", "Η αναλυτική βαθμολογία", "Το διαβατήριο"], 1, "Υπάρχει όμως ένα μικρό πρόβλημα με το πιστοποιητικό γέννησης"),
  Q("Τι πρέπει να κάνει ο πελάτης;", ["Να πάει στη γερμανική πρεσβεία", "Να πληρώσει επιπλέον", "Να βγάλει καινούργιο πιστοποιητικό από το διαδίκτυο και να το στείλει", "Να φέρει το πρωτότυπο πτυχίο"], 2, "Μπορείτε να βγάλετε καινούργιο από το διαδίκτυο"),
  Q("Πότε μπορεί να πάρει τα έτοιμα έγγραφα;", ["Από την Τρίτη, μετά τις δέκα", "Τη Δευτέρα το πρωί", "Σήμερα το βράδυ", "Σε δύο εβδομάδες"], 0, "Μπορείτε να περάσετε να τα πάρετε από την Τρίτη, μετά τις δέκα"),
 ],
 "gloss": {"πτυχία": "πτυχίο — degree (certificate)", "μεταφραστικό γραφείο": "μεταφραστικό γραφείο — translation office", "αναλυτικής βαθμολογίας": "αναλυτική βαθμολογία — transcript of marks", "πιστοποιητικό γέννησης": "πιστοποιητικό γέννησης — birth certificate", "αντίγραφο": "αντίγραφο — copy", "αρχές": "αρχές — the authorities", "εκδοθεί": "εκδίδομαι — to be issued", "έγγραφα": "έγγραφο — document", "σφραγισμένα": "σφραγισμένος — stamped, sealed", "αργίας": "αργία — public holiday"}
})

ITEMS.append({
 "id": "l129-dial-tilergasia-xorio", "title": "Δουλειά από το χωριό;", "title_en": "Working from the village?", "type": "dialogue", "level": "B2",
 "context_el": "Ο Στράτος και η Ζωή ζουν στην Αθήνα. Η Ζωή προτείνει να μετακομίσουν στο χωριό της στην Αρκαδία.",
 "script": [
  L("Ζωή", "f", "Στράτο, το σκέφτομαι σοβαρά: αφού και οι δύο δουλεύουμε πια από το σπίτι, γιατί να μη μείνουμε στο σπίτι της γιαγιάς μου στο χωριό; Θα γλιτώναμε το νοίκι και θα ζούσαμε πιο ήρεμα.", "Stratos, I'm seriously thinking about it: since we both work from home now, why don't we live in my grandmother's house in the village? We'd save the rent and live more calmly."),
  L("Στράτος", "m", "Ακούγεται ωραίο, αλλά έχει καλό ίντερνετ εκεί; Εγώ έχω βιντεοκλήσεις με πελάτες σχεδόν κάθε μέρα. Αν κόβεται η σύνδεση, θα έχω πρόβλημα. Και το σπίτι θέλει επισκευές, η στέγη έσταζε τον περασμένο χειμώνα.", "Sounds nice, but is there good internet there? I have video calls with clients almost every day. If the connection keeps dropping, I'll be in trouble. And the house needs repairs; the roof was leaking last winter."),
  L("Ζωή", "f", "Ρώτησα τον ξάδερφό μου: πέρσι έφεραν οπτική ίνα στο χωριό, και η σύνδεση είναι καλύτερη απ' ό,τι εδώ. Για τη στέγη, τα χρήματα που θα γλιτώσουμε από το νοίκι φτάνουν για την επισκευή μέσα σε λίγους μήνες.", "I asked my cousin: last year they brought fibre optic to the village, and the connection is better than here. As for the roof, the money we'll save on rent will cover the repair within a few months."),
  L("Στράτος", "m", "Εντάξει, ας το δοκιμάσουμε, αλλά όχι για πάντα από την αρχή. Ας μείνουμε εκεί τρεις μήνες, από την άνοιξη, και μετά αποφασίζουμε. Το διαμέρισμα εδώ μπορούμε να το νοικιάσουμε για λίγο σε φοιτητές.", "OK, let's try it, but not for good from the start. Let's stay there three months, from the spring, and then decide. We can rent out the flat here to students for a while."),
 ],
 "questions": [
  Q("Γιατί θέλει η Ζωή να μετακομίσουν στο χωριό;", ["Γιατί βρήκε δουλειά εκεί", "Γιατί θα γλίτωναν το νοίκι και θα ζούσαν πιο ήρεμα", "Γιατί είναι άρρωστη η γιαγιά της", "Γιατί ο Στράτος το ζήτησε"], 1, "Θα γλιτώναμε το νοίκι και θα ζούσαμε πιο ήρεμα"),
  Q("Τι ανησυχεί τον Στράτο;", ["Η απόσταση από τους φίλους", "Το κρύο του χειμώνα", "Το ίντερνετ για τις βιντεοκλήσεις και η στέγη που έσταζε", "Η έλλειψη σχολείων"], 2, "έχει καλό ίντερνετ εκεί"),
  Q("Τι αποφασίζουν τελικά;", ["Να μείνουν στο χωριό τρεις μήνες από την άνοιξη και μετά να αποφασίσουν", "Να πουλήσουν το διαμέρισμα", "Να μείνουν στην Αθήνα", "Να μετακομίσουν αμέσως για πάντα"], 0, "Ας μείνουμε εκεί τρεις μήνες, από την άνοιξη, και μετά αποφασίζουμε"),
 ],
 "gloss": {"γλιτώναμε": "γλιτώνω — to save (money), avoid", "νοίκι": "νοίκι — rent", "βιντεοκλήσεις": "βιντεοκλήση — video call", "σύνδεση": "σύνδεση — connection", "επισκευές": "επισκευή — repair", "στέγη": "στέγη — roof", "έσταζε": "στάζω — to drip, leak", "ξάδερφό": "ξάδερφος — cousin", "οπτική ίνα": "οπτική ίνα — fibre optic", "διαμέρισμα": "διαμέρισμα — flat, apartment", "νοικιάσουμε": "νοικιάζω — to rent (out)"}
})

ITEMS.append({
 "id": "l129-int-odigos-troley", "title": "Είκοσι χρόνια στο τιμόνι του τρόλεϊ", "title_en": "Twenty years at the wheel of a trolleybus", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια ραδιοφωνική συνέντευξη με μια γυναίκα που οδηγεί τρόλεϊ στην Αθήνα.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Ορφανού, πώς ξεκινά μια μέρα στη δουλειά σας;", "Ms Orfanou, how does a day at work begin for you?"),
  L("Οδηγός", "f", "Όταν έχω πρωινή βάρδια, ξυπνάω στις τέσσερις και μισή. Στις πέντε και μισή είμαι στο αμαξοστάσιο, ελέγχω το όχημα, τα φρένα, τις πόρτες, και στις έξι ξεκινάω το πρώτο δρομολόγιο. Τα πρώτα δρομολόγια έχουν μια ιδιαίτερη ησυχία· οι επιβάτες είναι κυρίως εργαζόμενοι που πάνε στις δουλειές τους.", "When I'm on the early shift, I wake up at half past four. At half past five I'm at the depot, I check the vehicle, the brakes, the doors, and at six I start the first route. The first trips have a special quietness; the passengers are mostly workers going to their jobs."),
  L("Δημοσιογράφος", "m", "Τι είναι το πιο δύσκολο σε αυτή τη δουλειά;", "What's the hardest thing in this job?"),
  L("Οδηγός", "f", "Η κίνηση, χωρίς αμφιβολία, και τα παρκαρισμένα αυτοκίνητα σε διπλή σειρά. Το τρόλεϊ δεν μπορεί να απομακρυνθεί πολύ από τα καλώδια. Αν στρίψω απότομα για να περάσω ένα αυτοκίνητο, μπορεί να βγουν οι κεραίες από τα σύρματα, και τότε πρέπει να κατέβω να τις ξαναβάλω, ενώ από πίσω κορνάρουν.", "Traffic, without doubt, and cars double-parked. A trolleybus can't move far from the overhead wires. If I turn sharply to get past a car, the poles can come off the wires, and then I have to get out and put them back, while people honk behind me."),
  L("Δημοσιογράφος", "m", "Και τι σας αρέσει περισσότερο;", "And what do you like most?"),
  L("Οδηγός", "f", "Οι άνθρωποι. Έχω τακτικούς επιβάτες που τους ξέρω είκοσι χρόνια. Μια κυρία μού φέρνει κάθε Χριστούγεννα μελομακάρονα, κι ένας μαθητής που πήγαινα στο σχολείο είναι σήμερα γιατρός και μου στέλνει ακόμα ευχές για τη γιορτή μου.", "The people. I have regular passengers I've known for twenty years. A lady brings me melomakarona every Christmas, and a schoolboy I used to drive to school is now a doctor and still sends me wishes on my name day."),
 ],
 "questions": [
  Q("Τι κάνει η οδηγός στο αμαξοστάσιο πριν από το πρώτο δρομολόγιο;", ["Πίνει καφέ με τους συναδέλφους", "Ελέγχει το όχημα, τα φρένα και τις πόρτες", "Καθαρίζει το τρόλεϊ", "Πουλάει εισιτήρια"], 1, "ελέγχω το όχημα, τα φρένα, τις πόρτες"),
  Q("Τι συμβαίνει αν στρίψει απότομα;", ["Χαλάνε τα φρένα", "Σβήνουν τα φώτα", "Μπορεί να βγουν οι κεραίες από τα σύρματα", "Ανοίγουν οι πόρτες"], 2, "μπορεί να βγουν οι κεραίες από τα σύρματα"),
  Q("Τι της αρέσει περισσότερο στη δουλειά της;", ["Οι άνθρωποι και οι τακτικοί επιβάτες", "Το καλό ωράριο", "Ο μισθός", "Η ησυχία της νύχτας"], 0, "Οι άνθρωποι. Έχω τακτικούς επιβάτες"),
 ],
 "gloss": {"τρόλεϊ": "τρόλεϊ — trolleybus", "βάρδια": "βάρδια — shift", "αμαξοστάσιο": "αμαξοστάσιο — (bus) depot", "όχημα": "όχημα — vehicle", "φρένα": "φρένο — brake", "δρομολόγιο": "δρομολόγιο — route, trip", "παρκαρισμένα": "παρκαρισμένος — parked", "απομακρυνθεί": "απομακρύνομαι — to move away", "καλώδια": "καλώδιο — cable, wire", "κεραίες": "κεραία — (trolley) pole; antenna", "σύρματα": "σύρμα — wire", "κορνάρουν": "κορνάρω — to honk", "τακτικούς": "τακτικός — regular", "μελομακάρονα": "μελομακάρονο — honey cookie (Christmas)"}
})

ITEMS.append({
 "id": "l129-rep-trikykla", "title": "Βόλτα με τρίκυκλο για τους παππούδες", "title_en": "Trishaw rides for older people", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από μια εκπομπή για την καθημερινή ζωή στις ελληνικές πόλεις.",
 "script": [
  L("Ρεπόρτερ", "m", "Κάθε Τετάρτη και Σάββατο, δύο ηλεκτρικά τρίκυκλα με ένα άνετο κάθισμα μπροστά ξεκινούν από ένα γηροκομείο της Καλαμάτας. Οδηγοί είναι εθελοντές, φοιτητές οι περισσότεροι, και επιβάτες οι ηλικιωμένοι που δεν μπορούν πια να περπατήσουν μεγάλες αποστάσεις.", "Every Wednesday and Saturday, two electric trishaws with a comfortable seat at the front set off from a care home in Kalamata. The drivers are volunteers, mostly students, and the passengers are older people who can no longer walk long distances."),
  L("Εθελόντρια", "f", "Τους πάμε όπου θέλουν: στην παραλία, στο παλιό τους σπίτι, στην αγορά. Πολλοί δεν είχαν βγει από το γηροκομείο εδώ και χρόνια. Και μιλάνε συνέχεια, μας λένε ιστορίες για το πώς ήταν η πόλη όταν ήταν νέοι. Εμένα μου έχουν μάθει περισσότερη ιστορία από το σχολείο!", "We take them wherever they want: to the beach, to their old house, to the market. Many hadn't been out of the care home for years. And they talk all the time, telling us stories about what the town was like when they were young. They've taught me more history than school!"),
  L("Ρεπόρτερ", "m", "Η ιδέα ήρθε από τη Δανία, όπου παρόμοια προγράμματα λειτουργούν εδώ και χρόνια. Τα τρίκυκλα αγοράστηκαν με δωρεές τοπικών επιχειρήσεων. Τώρα ο σύλλογος ψάχνει περισσότερους εθελοντές, ώστε οι βόλτες να γίνονται κάθε μέρα.", "The idea came from Denmark, where similar schemes have been running for years. The trishaws were bought with donations from local businesses. Now the association is looking for more volunteers, so that rides can take place every day."),
 ],
 "questions": [
  Q("Ποιοι είναι οι οδηγοί των τρίκυκλων;", ["Υπάλληλοι του δήμου", "Εθελοντές, κυρίως φοιτητές", "Νοσηλευτές του γηροκομείου", "Συγγενείς των ηλικιωμένων"], 1, "Οδηγοί είναι εθελοντές, φοιτητές οι περισσότεροι"),
  Q("Τι λέει η εθελόντρια ότι έχει κερδίσει;", ["Χρήματα για τις σπουδές της", "Ένα πιστοποιητικό", "Έχει μάθει πολλή ιστορία από τις ιστορίες των ηλικιωμένων", "Έναν καινούργιο φίλο στη Δανία"], 2, "Εμένα μου έχουν μάθει περισσότερη ιστορία από το σχολείο"),
  Q("Γιατί ψάχνει ο σύλλογος περισσότερους εθελοντές;", ["Για να γίνονται οι βόλτες κάθε μέρα", "Γιατί οι φοιτητές έφυγαν", "Για να αγοράσει καινούργια τρίκυκλα", "Για να ανοίξει ένα δεύτερο γηροκομείο"], 0, "ώστε οι βόλτες να γίνονται κάθε μέρα"),
 ],
 "gloss": {"τρίκυκλα": "τρίκυκλο — tricycle, trishaw", "κάθισμα": "κάθισμα — seat", "γηροκομείο": "γηροκομείο — care home, old people's home", "εθελοντές": "εθελοντής — volunteer", "ηλικιωμένοι": "ηλικιωμένος — elderly person", "αποστάσεις": "απόσταση — distance", "παρόμοια": "παρόμοιος — similar", "δωρεές": "δωρεά — donation", "επιχειρήσεων": "επιχείρηση — business", "σύλλογος": "σύλλογος — association"}
})

ITEMS.append({
 "id": "l129-rep-foitites-se-ilikiomenous", "title": "Ένα δωμάτιο με αντάλλαγμα την παρέα", "title_en": "A room in exchange for company", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα πρόγραμμα στη Θεσσαλονίκη που φέρνει κοντά φοιτητές και ηλικιωμένους.",
 "script": [
  L("Ρεπόρτερ", "f", "Η κυρία Αλίκη είναι ογδόντα δύο χρονών και ζει μόνη σε ένα μεγάλο διαμέρισμα στη Θεσσαλονίκη. Από τον Οκτώβριο μοιράζεται το σπίτι της με τη Σοφία, μια φοιτήτρια ιατρικής από την Κρήτη. Η Σοφία δεν πληρώνει ενοίκιο· σε αντάλλαγμα, περνά με την κυρία Αλίκη τουλάχιστον δύο βράδια την εβδομάδα και τη βοηθά με τα ψώνια.", "Mrs Aliki is eighty-two and lives alone in a large flat in Thessaloniki. Since October she has shared her home with Sofia, a medical student from Crete. Sofia pays no rent; in exchange, she spends at least two evenings a week with Mrs Aliki and helps her with the shopping."),
  L("Κυρία Αλίκη", "f", "Μετά τον θάνατο του άντρα μου, το σπίτι ήταν πολύ ήσυχο. Τώρα έχω κάποιον να του πω καλημέρα. Η Σοφία μού έμαθε να κάνω βιντεοκλήσεις με τα εγγόνια μου στην Αυστραλία, κι εγώ της μαθαίνω να φτιάχνει πίτες.", "After my husband died, the house was very quiet. Now I have someone to say good morning to. Sofia taught me to make video calls with my grandchildren in Australia, and I'm teaching her to make pies."),
  L("Ρεπόρτερ", "f", "Το πρόγραμμα το οργανώνει μια μη κυβερνητική οργάνωση, που γνωρίζει πρώτα τους ενδιαφερόμενους και ελέγχει αν ταιριάζουν. Οι δύο πλευρές υπογράφουν μια συμφωνία με σαφείς κανόνες, για παράδειγμα για τις επισκέψεις φίλων και τις ώρες ησυχίας.", "The scheme is run by a non-governmental organisation, which first meets those interested and checks whether they're a good match. Both sides sign an agreement with clear rules, for example about friends visiting and quiet hours."),
 ],
 "questions": [
  Q("Τι δίνει η Σοφία σε αντάλλαγμα για το δωμάτιο;", ["Πληρώνει μειωμένο ενοίκιο", "Περνά δύο βράδια την εβδομάδα με την κυρία Αλίκη και τη βοηθά με τα ψώνια", "Καθαρίζει όλο το σπίτι", "Μαγειρεύει κάθε μέρα"], 1, "περνά με την κυρία Αλίκη τουλάχιστον δύο βράδια την εβδομάδα και τη βοηθά με τα ψώνια"),
  Q("Τι έμαθε η κυρία Αλίκη από τη Σοφία;", ["Να μαγειρεύει πίτες", "Να οδηγεί", "Να κάνει βιντεοκλήσεις με τα εγγόνια της", "Να μιλάει αγγλικά"], 2, "Η Σοφία μού έμαθε να κάνω βιντεοκλήσεις με τα εγγόνια μου"),
  Q("Τι κάνει η οργάνωση πριν ξεκινήσει μια συγκατοίκηση;", ["Γνωρίζει τους ενδιαφερόμενους και ελέγχει αν ταιριάζουν", "Ζητά προκαταβολή", "Επισκευάζει το διαμέρισμα", "Βρίσκει δουλειά στον φοιτητή"], 0, "γνωρίζει πρώτα τους ενδιαφερόμενους και ελέγχει αν ταιριάζουν"),
 ],
 "gloss": {"μοιράζεται": "μοιράζομαι — to share", "ενοίκιο": "ενοίκιο — rent", "αντάλλαγμα": "σε αντάλλαγμα — in exchange", "ψώνια": "ψώνια — shopping", "βιντεοκλήσεις": "βιντεοκλήση — video call", "εγγόνια": "εγγόνι — grandchild", "μη κυβερνητική οργάνωση": "μη κυβερνητική οργάνωση — NGO", "ενδιαφερόμενους": "ενδιαφερόμενος — person interested", "συμφωνία": "συμφωνία — agreement", "σαφείς": "σαφής — clear", "ησυχίας": "ησυχία — quiet"}
})

ITEMS.append({
 "id": "l129-mono-kleidomeni-exo", "title": "Κλειδωμένη έξω με τις παντόφλες", "title_en": "Locked out in my slippers", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να διηγείται σε μια ραδιοφωνική εκπομπή ένα αστείο περιστατικό.",
 "script": [
  L("Κατερίνα", "f", "Ήταν μια Κυριακή πρωί του Ιανουαρίου. Βγήκα στο κεφαλόσκαλο με τις πιτζάμες και τις παντόφλες για να πάρω την εφημερίδα, και ο αέρας από το ανοιχτό παράθυρο έκλεισε την πόρτα πίσω μου. Τα κλειδιά, φυσικά, ήταν μέσα, και το κινητό μου επίσης.", "It was a Sunday morning in January. I went out onto the landing in my pyjamas and slippers to get the newspaper, and the draught from the open window shut the door behind me. The keys, of course, were inside, and so was my phone."),
  L("Κατερίνα", "f", "Χτύπησα στη γειτόνισσα απέναντι, την κυρία Βούλα, που δεν της είχα μιλήσει ποτέ πέρα από μια καλημέρα. Με έβαλε μέσα, μου έφτιαξε καφέ και μου δάνεισε ένα ζευγάρι κάλτσες. Από το τηλέφωνό της πήρα έναν κλειδαρά, που είπε ότι θα ερχόταν σε δύο ώρες.", "I knocked on the neighbour opposite, Mrs Voula, whom I'd never spoken to beyond a good morning. She let me in, made me coffee and lent me a pair of socks. From her phone I called a locksmith, who said he'd come in two hours."),
  L("Κατερίνα", "f", "Εκείνες οι δύο ώρες ήταν από τις πιο ευχάριστες της χρονιάς. Μου έδειξε φωτογραφίες από τα νιάτα της, μου είπε όλα τα κουτσομπολιά της πολυκατοικίας. Από τότε πίνουμε καφέ κάθε Κυριακή, και της έχω δώσει ένα κλειδί του σπιτιού μου, για σιγουριά.", "Those two hours were among the most pleasant of the year. She showed me photos from her youth and told me all the gossip in the building. Since then we have coffee every Sunday, and I've given her a key to my flat, just in case."),
 ],
 "questions": [
  Q("Πώς έμεινε η Κατερίνα έξω από το σπίτι;", ["Έχασε τα κλειδιά της στον δρόμο", "Ο αέρας από το ανοιχτό παράθυρο έκλεισε την πόρτα", "Κάποιος άλλαξε την κλειδαριά", "Ξέχασε τον κωδικό της πόρτας"], 1, "ο αέρας από το ανοιχτό παράθυρο έκλεισε την πόρτα πίσω μου"),
  Q("Τι έκανε η κυρία Βούλα;", ["Άνοιξε την πόρτα με ένα σύρμα", "Κάλεσε την αστυνομία", "Την έβαλε μέσα, της έφτιαξε καφέ και της δάνεισε κάλτσες", "Της έδωσε ένα κινητό"], 2, "Με έβαλε μέσα, μου έφτιαξε καφέ και μου δάνεισε ένα ζευγάρι κάλτσες"),
  Q("Τι άλλαξε μετά από εκείνη τη μέρα;", ["Πίνουν καφέ κάθε Κυριακή και η γειτόνισσα έχει ένα κλειδί της", "Η Κατερίνα μετακόμισε", "Η Κατερίνα αγόρασε καινούργια πόρτα", "Δεν μιλάνε πια"], 0, "Από τότε πίνουμε καφέ κάθε Κυριακή, και της έχω δώσει ένα κλειδί"),
 ],
 "gloss": {"περιστατικό": "περιστατικό — incident", "κεφαλόσκαλο": "κεφαλόσκαλο — landing (top of the stairs)", "πιτζάμες": "πιτζάμα — pyjamas", "παντόφλες": "παντόφλα — slipper", "γειτόνισσα": "γειτόνισσα — (female) neighbour", "δάνεισε": "δανείζω — to lend", "κάλτσες": "κάλτσα — sock", "κλειδαρά": "κλειδαράς — locksmith", "νιάτα": "νιάτα — youth", "κουτσομπολιά": "κουτσομπολιό — gossip", "σιγουριά": "για σιγουριά — just in case"}
})

ITEMS.append({
 "id": "l129-mono-tavli-geitonas", "title": "Το τάβλι με τον κυρ Παντελή", "title_en": "Backgammon with Mr Pantelis", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν νεαρό να μιλά σε ένα πόντκαστ για μια απρόσμενη φιλία.",
 "script": [
  L("Άρης", "m", "Όταν μετακόμισα στην Πάτρα για σπουδές, δεν ήξερα κανέναν. Κάθε απόγευμα έβλεπα στο μπαλκόνι του ισογείου έναν ηλικιωμένο κύριο να παίζει τάβλι μόνος του, κουνώντας το κεφάλι σαν να μάλωνε με έναν αόρατο αντίπαλο.", "When I moved to Patras to study, I didn't know anyone. Every afternoon I'd see an elderly man on the ground-floor balcony playing backgammon on his own, shaking his head as if arguing with an invisible opponent."),
  L("Άρης", "m", "Μια μέρα μού φώναξε: «Ξέρεις να παίζεις, νεαρέ;» Του είπα την αλήθεια, ότι ήξερα μόνο τους κανόνες. Γέλασε και μου είπε ότι αυτό είναι το χειρότερο, γιατί θα νομίζω ότι ξέρω. Από εκείνη τη μέρα παίζαμε σχεδόν κάθε απόγευμα, και τους πρώτους μήνες έχανα συνέχεια.", "One day he called out to me: 'Do you know how to play, young man?' I told him the truth, that I only knew the rules. He laughed and said that was the worst, because I'd think I knew. From that day we played almost every afternoon, and for the first few months I lost all the time."),
  L("Άρης", "m", "Ο κυρ Παντελής ήταν συνταξιούχος ναυτικός και ανάμεσα στις ζαριές μού διηγιόταν ιστορίες από λιμάνια όλου του κόσμου. Όταν πήρα το πτυχίο μου, ήρθε στην τελετή με κουστούμι. Σήμερα ζω στην Αθήνα, αλλά κάθε φορά που πάω στην Πάτρα, η πρώτη μου στάση είναι εκείνο το μπαλκόνι.", "Mr Pantelis was a retired sailor, and between throws of the dice he'd tell me stories from ports all over the world. When I got my degree, he came to the ceremony in a suit. Today I live in Athens, but every time I go to Patras, my first stop is that balcony."),
 ],
 "questions": [
  Q("Τι έβλεπε ο Άρης κάθε απόγευμα;", ["Έναν κύριο να ποτίζει λουλούδια", "Έναν ηλικιωμένο να παίζει τάβλι μόνος του", "Παιδιά να παίζουν μπάλα", "Έναν ναυτικό να επισκευάζει ένα δίχτυ"], 1, "έναν ηλικιωμένο κύριο να παίζει τάβλι μόνος του"),
  Q("Τι απάντησε ο Άρης όταν ο κυρ Παντελής τον ρώτησε αν ξέρει να παίζει;", ["Ότι είναι πολύ καλός παίκτης", "Ότι δεν έχει χρόνο", "Ότι ήξερε μόνο τους κανόνες", "Ότι προτιμά το σκάκι"], 2, "ότι ήξερα μόνο τους κανόνες"),
  Q("Τι έκανε ο κυρ Παντελής όταν ο Άρης πήρε το πτυχίο του;", ["Ήρθε στην τελετή με κουστούμι", "Του χάρισε ένα τάβλι", "Του έγραψε ένα γράμμα", "Οργάνωσε ένα πάρτι"], 0, "ήρθε στην τελετή με κουστούμι"),
 ],
 "gloss": {"απρόσμενη": "απρόσμενος — unexpected", "ισογείου": "ισόγειο — ground floor", "τάβλι": "τάβλι — backgammon", "μάλωνε": "μαλώνω — to argue, quarrel", "αόρατο": "αόρατος — invisible", "αντίπαλο": "αντίπαλος — opponent", "κανόνες": "κανόνας — rule", "συνταξιούχος": "συνταξιούχος — pensioner, retired", "ζαριές": "ζαριά — throw of the dice", "διηγιόταν": "διηγούμαι — to tell, narrate", "τελετή": "τελετή — ceremony", "κουστούμι": "κουστούμι — suit"}
})

ITEMS.append({
 "id": "l129-c1-tragodia-koinon", "title": "Η τραγωδία των κοινών αγαθών", "title_en": "The tragedy of the commons", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ένα ραδιοφωνικό δοκίμιο για την οικονομία και το περιβάλλον.",
 "script": [
  L("Ομιλητής", "m", "Το 1968 ο Αμερικανός οικολόγος Γκάρετ Χάρντιν δημοσίευσε ένα άρθρο με τίτλο «Η τραγωδία των κοινών». Χρησιμοποίησε ένα απλό παράδειγμα: ένα βοσκοτόπι που ανήκει σε όλους. Κάθε βοσκός έχει συμφέρον να βάλει ένα ακόμη ζώο να βοσκήσει, γιατί το κέρδος είναι δικό του, ενώ η ζημιά από την υπερβόσκηση μοιράζεται σε όλους.", "In 1968 the American ecologist Garrett Hardin published an article entitled 'The Tragedy of the Commons'. He used a simple example: a pasture that belongs to everyone. Each herdsman has an interest in putting one more animal out to graze, because the profit is his, while the damage from overgrazing is shared among everyone."),
  L("Ομιλητής", "m", "Αν όλοι σκεφτούν με τον ίδιο τρόπο, το βοσκοτόπι καταστρέφεται, και τελικά χάνουν όλοι. Το ίδιο σχήμα μπορεί να εφαρμοστεί στην υπεραλίευση, στα υπόγεια νερά που αντλούνται χωρίς έλεγχο, ακόμη και στην ατμόσφαιρα, που λειτουργεί σαν ένας τεράστιος κοινός χώρος απόρριψης ρύπων.", "If everyone thinks the same way, the pasture is destroyed and in the end everyone loses. The same pattern can be applied to overfishing, to groundwater pumped without control, even to the atmosphere, which works like a huge shared dumping ground for pollutants."),
  L("Ομιλητής", "m", "Ο Χάρντιν θεωρούσε ότι οι μόνες λύσεις ήταν είτε η ιδιωτικοποίηση είτε ο αυστηρός κρατικός έλεγχος. Η πολιτική επιστήμονας Ελίνορ Όστρομ, όμως, που τιμήθηκε το 2009 με το Νόμπελ Οικονομικών, έδειξε ότι υπάρχει και τρίτος δρόμος. Μελετώντας κοινότητες σε όλο τον κόσμο, διαπίστωσε ότι πολλές διαχειρίζονται με επιτυχία κοινούς πόρους για αιώνες.", "Hardin believed the only solutions were either privatisation or strict state control. The political scientist Elinor Ostrom, however, who was awarded the Nobel Prize in Economics in 2009, showed that there is a third way. Studying communities around the world, she found that many manage shared resources successfully for centuries."),
  L("Ομιλητής", "m", "Το μυστικό, σύμφωνα με την Όστρομ, βρίσκεται σε κανόνες που διαμορφώνουν οι ίδιοι οι χρήστες, σε τρόπους να παρακολουθείται η τήρησή τους και σε κυρώσεις που αυξάνονται σταδιακά. Με άλλα λόγια, η «τραγωδία» δεν είναι αναπόφευκτη· είναι αποτέλεσμα της έλλειψης θεσμών εμπιστοσύνης και συνεργασίας.", "The secret, according to Ostrom, lies in rules drawn up by the users themselves, in ways of monitoring that they're kept, and in sanctions that increase gradually. In other words, the 'tragedy' is not inevitable; it's the result of a lack of institutions of trust and cooperation."),
 ],
 "questions": [
  Q("Γιατί, σύμφωνα με τον Χάρντιν, κάθε βοσκός βάζει ένα ακόμη ζώο;", ["Γιατί δεν ξέρει τους κανόνες", "Γιατί το κέρδος είναι δικό του ενώ η ζημιά μοιράζεται σε όλους", "Γιατί το βοσκοτόπι είναι πολύ μεγάλο", "Γιατί το ζητά το κράτος"], 1, "το κέρδος είναι δικό του, ενώ η ζημιά από την υπερβόσκηση μοιράζεται σε όλους"),
  Q("Σε ποια άλλα παραδείγματα εφαρμόζεται το ίδιο σχήμα;", ["Στο εμπόριο και στις τράπεζες", "Στην εκπαίδευση", "Στην υπεραλίευση, στα υπόγεια νερά και στην ατμόσφαιρα", "Στον τουρισμό και στις μεταφορές"], 2, "στην υπεραλίευση, στα υπόγεια νερά που αντλούνται χωρίς έλεγχο"),
  Q("Τι έδειξε η Ελίνορ Όστρομ;", ["Ότι πολλές κοινότητες διαχειρίζονται με επιτυχία κοινούς πόρους", "Ότι η ιδιωτικοποίηση είναι η μόνη λύση", "Ότι ο Χάρντιν είχε απόλυτο δίκιο", "Ότι οι κοινοί πόροι δεν εξαντλούνται ποτέ"], 0, "πολλές διαχειρίζονται με επιτυχία κοινούς πόρους για αιώνες"),
  Q("Σε τι βρίσκεται το μυστικό, κατά την Όστρομ;", ["Στην αυστηρή αστυνόμευση από το κράτος", "Σε κανόνες που διαμορφώνουν οι ίδιοι οι χρήστες, παρακολούθηση και σταδιακές κυρώσεις", "Στη μείωση του πληθυσμού", "Στη νέα τεχνολογία"], 1, "σε κανόνες που διαμορφώνουν οι ίδιοι οι χρήστες"),
 ],
 "gloss": {"οικολόγος": "οικολόγος — ecologist", "βοσκοτόπι": "βοσκοτόπι — pasture", "συμφέρον": "συμφέρον — interest, advantage", "υπερβόσκηση": "υπερβόσκηση — overgrazing", "υπεραλίευση": "υπεραλίευση — overfishing", "υπόγεια νερά": "υπόγεια νερά — groundwater", "αντλούνται": "αντλούμαι — to be pumped", "ρύπων": "ρύπος — pollutant", "ιδιωτικοποίηση": "ιδιωτικοποίηση — privatisation", "διαχειρίζονται": "διαχειρίζομαι — to manage", "πόρους": "πόρος — resource", "τήρησή": "τήρηση — observance, keeping (of rules)", "κυρώσεις": "κύρωση — sanction", "αναπόφευκτη": "αναπόφευκτος — inevitable", "θεσμών": "θεσμός — institution"}
})

ITEMS.append({
 "id": "l129-c1-botsaris", "title": "Μάρκος Μπότσαρης, η νυχτερινή επίθεση στο Κεφαλόβρυσο", "title_en": "Markos Botsaris and the night attack at Kefalovryso", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια ιστορικό για τον Σουλιώτη οπλαρχηγό Μάρκο Μπότσαρη.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Λαμπράκη, πώς σημάδεψε το Σούλι τη ζωή του Μάρκου Μπότσαρη;", "Ms Lambraki, how did Souli shape the life of Markos Botsaris?"),
  L("Ιστορικός", "f", "Καθοριστικά. Γεννήθηκε στο Σούλι γύρω στο 1788, σε μια οικογένεια με μεγάλη πολεμική παράδοση. Όταν οι Σουλιώτες αναγκάστηκαν να εγκαταλείψουν τα χωριά τους το 1803, μετά από χρόνια πολέμου με τον Αλή Πασά, η οικογένειά του κατέφυγε στα Επτάνησα. Εκεί ο νεαρός Μάρκος υπηρέτησε σε στρατιωτικά σώματα που οργάνωναν οι ξένες δυνάμεις που κατείχαν τα νησιά.", "Decisively. He was born in Souli around 1788, into a family with a great military tradition. When the Souliots were forced to abandon their villages in 1803, after years of war with Ali Pasha, his family took refuge in the Ionian Islands. There the young Markos served in military units organised by the foreign powers that held the islands."),
  L("Δημοσιογράφος", "m", "Και στην Επανάσταση;", "And in the Revolution?"),
  L("Ιστορικός", "f", "Πήρε μέρος στις επιχειρήσεις στη Δυτική Ελλάδα και στην πρώτη πολιορκία του Μεσολογγίου, το 1822. Τον Αύγουστο του 1823, όταν ένας μεγάλος οθωμανικός στρατός κατέβαινε προς τη Δυτική Στερεά, σχεδίασε μια τολμηρή νυχτερινή επίθεση στο στρατόπεδο του εχθρού, στο Κεφαλόβρυσο, κοντά στο Καρπενήσι. Η επίθεση προκάλεσε μεγάλη σύγχυση στους αντιπάλους, αλλά ο ίδιος ο Μπότσαρης σκοτώθηκε κατά τη διάρκειά της.", "He took part in the operations in Western Greece and in the first siege of Missolonghi in 1822. In August 1823, when a large Ottoman army was coming down towards Western Central Greece, he planned a daring night attack on the enemy camp at Kefalovryso, near Karpenisi. The attack caused great confusion among the enemy, but Botsaris himself was killed during it."),
  L("Δημοσιογράφος", "m", "Γιατί έγινε τόσο γρήγορα θρύλος;", "Why did he become a legend so quickly?"),
  L("Ιστορικός", "f", "Ο θάνατός του συνέπεσε με την εποχή που ο φιλελληνισμός βρισκόταν στην ακμή του. Η είδηση έφτασε γρήγορα στην Ευρώπη και στην Αμερική, όπου γράφτηκαν ποιήματα προς τιμήν του. Θάφτηκε στο Μεσολόγγι, και σήμερα ο τάφος του βρίσκεται στον Κήπο των Ηρώων της πόλης. Η μορφή του έγινε σύμβολο αυτοθυσίας, κάτι που ίσως κάλυψε την πιο σύνθετη πραγματικότητα της εποχής.", "His death coincided with the time when philhellenism was at its peak. The news quickly reached Europe and America, where poems were written in his honour. He was buried in Missolonghi, and today his grave is in the town's Garden of Heroes. His figure became a symbol of self-sacrifice, which perhaps covered the more complex reality of the period."),
 ],
 "questions": [
  Q("Πού κατέφυγε η οικογένεια του Μπότσαρη μετά το 1803;", ["Στη Μάνη", "Στα Επτάνησα", "Στην Κωνσταντινούπολη", "Στην Ιταλία"], 1, "η οικογένειά του κατέφυγε στα Επτάνησα"),
  Q("Τι σχεδίασε ο Μπότσαρης τον Αύγουστο του 1823;", ["Την άμυνα του Μεσολογγίου", "Μια ειρηνική συμφωνία", "Μια τολμηρή νυχτερινή επίθεση στο στρατόπεδο του εχθρού", "Μια ναυμαχία"], 2, "σχεδίασε μια τολμηρή νυχτερινή επίθεση στο στρατόπεδο του εχθρού"),
  Q("Πού βρίσκεται σήμερα ο τάφος του;", ["Στον Κήπο των Ηρώων του Μεσολογγίου", "Στο Καρπενήσι", "Στο Σούλι", "Στην Κέρκυρα"], 0, "ο τάφος του βρίσκεται στον Κήπο των Ηρώων της πόλης"),
  Q("Τι λέει η ιστορικός για τον θρύλο του Μπότσαρη;", ["Ότι δημιουργήθηκε πολλά χρόνια αργότερα", "Ότι η μορφή του έγινε σύμβολο αυτοθυσίας, που ίσως κάλυψε μια πιο σύνθετη πραγματικότητα", "Ότι δεν έγινε γνωστός έξω από την Ελλάδα", "Ότι οι Ευρωπαίοι τον αγνόησαν"], 1, "Η μορφή του έγινε σύμβολο αυτοθυσίας"),
 ],
 "gloss": {"οπλαρχηγό": "οπλαρχηγός — chieftain, leader of an armed band", "σημάδεψε": "σημαδεύω — to mark, shape", "Καθοριστικά": "καθοριστικά — decisively", "εγκαταλείψουν": "εγκαταλείπω — to abandon", "κατέφυγε": "καταφεύγω — to take refuge", "υπηρέτησε": "υπηρετώ — to serve", "κατείχαν": "κατέχω — to hold, occupy", "πολιορκία": "πολιορκία — siege", "τολμηρή": "τολμηρός — daring", "στρατόπεδο": "στρατόπεδο — camp", "σύγχυση": "σύγχυση — confusion", "θρύλος": "θρύλος — legend", "συνέπεσε": "συμπίπτω — to coincide", "φιλελληνισμός": "φιλελληνισμός — philhellenism", "ακμή": "ακμή — peak", "αυτοθυσίας": "αυτοθυσία — self-sacrifice"}
})

rnd = random.Random(129)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-129.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
