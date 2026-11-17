# Source for library/listening/listening-146.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l146.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l146-vm-kapnodocho", "title": "Καθάρισμα καμινάδας πριν από τον χειμώνα", "title_en": "Chimney cleaning before winter", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από έναν τεχνικό που καθαρίζει καμινάδες.",
 "script": [
  L("Τεχνικός", "m", "Καλησπέρα σας, ο Μιχάλης είμαι, για το καθάρισμα της καμινάδας. Μπορώ να έρθω την Πέμπτη το πρωί, γύρω στις εννιά. Η δουλειά κρατάει περίπου δύο ώρες.", "Good evening, it's Michalis, about cleaning the chimney. I can come on Thursday morning, around nine. The job takes about two hours."),
  L("Τεχνικός", "m", "Θα σας παρακαλούσα να μην ανάψετε το τζάκι από την Τετάρτη το βράδυ, γιατί πρέπει να είναι εντελώς κρύο. Και αν μπορείτε, μετακινήστε τα έπιπλα και τα χαλιά γύρω από το τζάκι. Εγώ θα φέρω πανιά για να μη λερωθεί τίποτα.", "Please don't light the fireplace from Wednesday evening, because it has to be completely cold. And if you can, move the furniture and rugs around the fireplace. I'll bring cloths so nothing gets dirty."),
  L("Τεχνικός", "m", "Αφού έχετε να την καθαρίσετε τρία χρόνια, μπορεί να έχει μαζευτεί πολλή καπνιά, που είναι επικίνδυνη γιατί μπορεί να πάρει φωτιά. Η τιμή είναι εξήντα ευρώ, και στο τέλος θα σας δώσω και βεβαίωση. Αν δεν σας βολεύει η Πέμπτη, στείλτε μου ένα μήνυμα.", "Since it hasn't been cleaned for three years, a lot of soot may have built up, which is dangerous because it can catch fire. The price is sixty euros, and at the end I'll also give you a certificate. If Thursday doesn't suit you, send me a message."),
 ],
 "questions": [
  Q("Τι σας ζητάει να μην κάνετε από την Τετάρτη το βράδυ;", ["Να ανάψετε το τζάκι", "Να καθαρίσετε το σπίτι", "Να ανοίξετε τα παράθυρα", "Να βγείτε από το σπίτι"], 0, "να μην ανάψετε το τζάκι από την Τετάρτη το βράδυ"),
  Q("Γιατί είναι επικίνδυνη η καπνιά;", ["Γιατί μυρίζει άσχημα", "Γιατί μπορεί να πάρει φωτιά", "Γιατί λερώνει τα έπιπλα", "Γιατί κλείνει τα παράθυρα"], 1, "μπορεί να πάρει φωτιά"),
  Q("Τι θα σας δώσει στο τέλος;", ["Ένα δώρο", "Έκπτωση για την επόμενη φορά", "Βεβαίωση", "Καινούργια πανιά"], 2, "στο τέλος θα σας δώσω και βεβαίωση"),
 ],
 "gloss": {"καμινάδας": "καμινάδα — chimney", "τζάκι": "τζάκι — fireplace", "μετακινήστε": "μετακινώ — to move", "χαλιά": "χαλί — rug, carpet", "πανιά": "πανί — cloth", "λερωθεί": "λερώνομαι — to get dirty", "καπνιά": "καπνιά — soot", "βεβαίωση": "βεβαίωση — certificate", "βολεύει": "βολεύω — to suit"}
})

ITEMS.append({
 "id": "l146-ann-iatreia", "title": "Νέο σύστημα στα εξωτερικά ιατρεία", "title_en": "A new system at the outpatient clinics", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στην αίθουσα αναμονής ενός νοσοκομείου και ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Παρακαλούνται οι ασθενείς των εξωτερικών ιατρείων να προσέξουν: το μηχάνημα με τα χαρτάκια προτεραιότητας στην είσοδο δεν λειτουργεί σήμερα. Όσοι έχετε κλείσει ραντεβού ηλεκτρονικά, δεν χρειάζεται να πάρετε χαρτάκι.", "Outpatient clinic patients are asked to note: the queue-ticket machine at the entrance is not working today. Those of you who booked an appointment online do not need to take a ticket."),
  L("Εκφωνήτρια", "f", "Θα σας καλέσουμε με το ονοματεπώνυμό σας, με τη σειρά του ραντεβού. Όσοι ήρθατε χωρίς ραντεβού, παρακαλούμε να περάσετε από τη γραμματεία, δίπλα στο κυλικείο, για να γραφτείτε σε λίστα.", "We will call you by your full name, in the order of your appointment. Those of you who came without an appointment, please go to the reception desk, next to the cafeteria, to put your name on a list."),
  L("Εκφωνήτρια", "f", "Το καρδιολογικό ιατρείο λειτουργεί σήμερα στον δεύτερο όροφο, και όχι στο ισόγειο. Ευχαριστούμε για την κατανόηση.", "The cardiology clinic is operating on the second floor today, and not on the ground floor. Thank you for your understanding."),
 ],
 "questions": [
  Q("Τι πρόβλημα υπάρχει σήμερα;", ["Λείπουν γιατροί", "Δεν λειτουργεί το μηχάνημα με τα χαρτάκια προτεραιότητας", "Το νοσοκομείο κλείνει νωρίς", "Δεν λειτουργεί το ασανσέρ"], 1, "δεν λειτουργεί σήμερα"),
  Q("Τι πρέπει να κάνουν όσοι ήρθαν χωρίς ραντεβού;", ["Να περάσουν από τη γραμματεία για να γραφτούν σε λίστα", "Να φύγουν και να έρθουν αύριο", "Να τηλεφωνήσουν", "Να πάρουν χαρτάκι"], 0, "να περάσετε από τη γραμματεία"),
  Q("Πού λειτουργεί σήμερα το καρδιολογικό ιατρείο;", ["Στο ισόγειο", "Στο κυλικείο", "Στον δεύτερο όροφο", "Σε άλλο κτίριο"], 2, "Το καρδιολογικό ιατρείο λειτουργεί σήμερα στον δεύτερο όροφο"),
 ],
 "gloss": {"αίθουσα αναμονής": "αίθουσα αναμονής — waiting room", "εξωτερικών ιατρείων": "εξωτερικά ιατρεία — outpatient clinics", "μηχάνημα": "μηχάνημα — machine", "προτεραιότητας": "προτεραιότητα — priority, queue order", "ηλεκτρονικά": "ηλεκτρονικά — online", "ονοματεπώνυμό": "ονοματεπώνυμο — full name", "γραμματεία": "γραμματεία — reception, office", "κυλικείο": "κυλικείο — cafeteria, canteen", "καρδιολογικό": "καρδιολογικός — cardiology", "κατανόηση": "κατανόηση — understanding"}
})

ITEMS.append({
 "id": "l146-dia-egkavma", "title": "Κάηκα στον ήλιο", "title_en": "I got sunburnt", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο σε ένα φαρμακείο κοντά σε μια παραλία.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Χθες αποκοιμήθηκα στην παραλία και κάηκα στην πλάτη. Σήμερα με τσούζει πολύ και δεν μπορώ να φορέσω ούτε μπλουζάκι.", "Good morning. Yesterday I fell asleep on the beach and got burnt on my back. Today it stings a lot and I can't even wear a T-shirt."),
  L("Φαρμακοποιός", "f", "Για να δω... Είναι κόκκινο, αλλά δεν βλέπω φουσκάλες, οπότε είναι ήπιο έγκαυμα. Θα σας δώσω μια δροσιστική κρέμα με αλόη. Βάλτε την τρεις φορές τη μέρα, και κάντε χλιαρά ντους, όχι ζεστά.", "Let me see... It's red, but I don't see blisters, so it's a mild burn. I'll give you a cooling cream with aloe. Put it on three times a day, and take lukewarm showers, not hot ones."),
  L("Πελάτης", "m", "Μπορώ να πάω στη θάλασσα αύριο;", "Can I go to the sea tomorrow?"),
  L("Φαρμακοποιός", "f", "Καλύτερα να μείνετε στη σκιά για δύο τρεις μέρες. Και πίνετε πολύ νερό. Αν εμφανιστούν φουσκάλες ή πυρετός, πρέπει να δείτε γιατρό. Και την επόμενη φορά, αντηλιακό κάθε δύο ώρες, ακόμα κι αν ο ουρανός έχει σύννεφα.", "Better stay in the shade for two or three days. And drink plenty of water. If blisters or a fever appear, you need to see a doctor. And next time, sunscreen every two hours, even if the sky is cloudy."),
 ],
 "questions": [
  Q("Πώς κάηκε ο πελάτης;", ["Μαγειρεύοντας", "Αποκοιμήθηκε στην παραλία", "Έπαιζε βόλεϊ όλη μέρα", "Έκανε σκι"], 1, "Χθες αποκοιμήθηκα στην παραλία"),
  Q("Γιατί η φαρμακοποιός λέει ότι το έγκαυμα είναι ήπιο;", ["Γιατί δεν πονάει", "Γιατί είναι μικρό", "Γιατί δεν βλέπει φουσκάλες", "Γιατί έγινε πριν από μία εβδομάδα"], 2, "δεν βλέπω φουσκάλες, οπότε είναι ήπιο έγκαυμα"),
  Q("Πότε πρέπει να δει γιατρό;", ["Αν εμφανιστούν φουσκάλες ή πυρετός", "Αν η κρέμα τελειώσει", "Αμέσως", "Αν θέλει να πάει στη θάλασσα"], 0, "Αν εμφανιστούν φουσκάλες ή πυρετός, πρέπει να δείτε γιατρό"),
 ],
 "gloss": {"αποκοιμήθηκα": "αποκοιμιέμαι — to fall asleep", "κάηκα": "καίγομαι — to get burnt", "τσούζει": "τσούζω — to sting", "φουσκάλες": "φουσκάλα — blister", "ήπιο": "ήπιος — mild", "έγκαυμα": "έγκαυμα — burn", "δροσιστική": "δροσιστικός — cooling", "χλιαρά": "χλιαρός — lukewarm", "αντηλιακό": "αντηλιακό — sunscreen"}
})

ITEMS.append({
 "id": "l146-int-dichtya", "title": "Η γυναίκα που μπαλώνει δίχτυα", "title_en": "The woman who mends nets", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε τοπικό ραδιόφωνο με μια γυναίκα που επιδιορθώνει δίχτυα σε ένα λιμάνι.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Ευτυχία, πώς ξεκινήσατε αυτή τη δουλειά;", "Mrs Eftychia, how did you start this job?"),
  L("Ευτυχία", "f", "Ο πατέρας μου ήταν ψαράς, και από δέκα χρονών καθόμουν μαζί του στο μουράγιο και του κρατούσα τη σαΐτα. Όταν παντρεύτηκα έναν ψαρά, συνέχισα να μπαλώνω τα δίχτυα του, και σιγά σιγά άρχισαν να μου φέρνουν και άλλοι.", "My father was a fisherman, and from the age of ten I sat with him on the quay and held the netting needle for him. When I married a fisherman, I went on mending his nets, and little by little others started bringing me theirs."),
  L("Δημοσιογράφος", "m", "Πόσο χρόνο παίρνει ένα δίχτυ;", "How long does a net take?"),
  L("Ευτυχία", "f", "Εξαρτάται από τη ζημιά. Ένα δελφίνι μπορεί να ανοίξει μια τρύπα ενός μέτρου μέσα σε ένα λεπτό, κι εγώ θέλω μια ολόκληρη μέρα για να την κλείσω. Τα μάτια του διχτυού πρέπει να είναι όλα ίδια, αλλιώς το ψάρι φεύγει.", "It depends on the damage. A dolphin can open a hole a metre wide in a minute, and I need a whole day to close it. The meshes of the net must all be the same, otherwise the fish escape."),
  L("Δημοσιογράφος", "m", "Υπάρχουν νέοι που θέλουν να μάθουν;", "Are there young people who want to learn?"),
  L("Ευτυχία", "f", "Λίγοι. Τα καινούργια δίχτυα είναι φθηνά και πολλοί προτιμούν να τα πετάνε. Πέρσι όμως ήρθαν δύο κοπέλες από το σχολείο και τους έμαθα τα βασικά. Αν συνεχίσουν, θα είμαι ευχαριστημένη.", "Few. New nets are cheap and many prefer to throw them away. But last year two girls came from the school and I taught them the basics. If they keep going, I'll be happy."),
 ],
 "questions": [
  Q("Πώς έμαθε η κυρία Ευτυχία τη δουλειά;", ["Δίπλα στον πατέρα της, από μικρή", "Σε μια σχολή", "Από τον άντρα της, μετά τον γάμο", "Από βιβλία"], 0, "από δέκα χρονών καθόμουν μαζί του στο μουράγιο"),
  Q("Γιατί πρέπει τα μάτια του διχτυού να είναι όλα ίδια;", ["Για να είναι πιο όμορφο", "Για να μη φεύγει το ψάρι", "Για να είναι πιο ελαφρύ", "Για να στεγνώνει γρήγορα"], 1, "αλλιώς το ψάρι φεύγει"),
  Q("Γιατί λίγοι νέοι θέλουν να μάθουν;", ["Γιατί η δουλειά είναι επικίνδυνη", "Γιατί δεν υπάρχουν πια ψαράδες", "Γιατί τα καινούργια δίχτυα είναι φθηνά και πολλοί τα πετάνε", "Γιατί πληρώνεται πολύ λίγο"], 2, "Τα καινούργια δίχτυα είναι φθηνά και πολλοί προτιμούν να τα πετάνε"),
 ],
 "gloss": {"επιδιορθώνει": "επιδιορθώνω — to repair", "δίχτυα": "δίχτυ — fishing net", "μουράγιο": "μουράγιο — quay, harbour wall", "σαΐτα": "σαΐτα — netting needle (shuttle)", "μπαλώνω": "μπαλώνω — to mend, patch", "ζημιά": "ζημιά — damage", "τρύπα": "τρύπα — hole", "μάτια": "μάτι — mesh (of a net); eye", "βασικά": "τα βασικά — the basics"}
})

ITEMS.append({
 "id": "l146-news-vryses", "title": "Βρύσες αντί για πλαστικά μπουκάλια", "title_en": "Fountains instead of plastic bottles", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός τοπικού ραδιοφώνου.",
 "script": [
  L("Εκφωνήτρια", "f", "Είκοσι νέες βρύσες με πόσιμο νερό τοποθετήθηκαν αυτή την εβδομάδα σε πλατείες, πάρκα και στάσεις λεωφορείων της πόλης. Στόχος του δήμου είναι να μειωθεί η χρήση πλαστικών μπουκαλιών, ιδιαίτερα τους καλοκαιρινούς μήνες.", "Twenty new drinking-water fountains were installed this week in squares, parks and bus stops around the city. The municipality's aim is to reduce the use of plastic bottles, especially in the summer months."),
  L("Εκφωνήτρια", "f", "Οι βρύσες έχουν δύο στόμια: ένα για να πίνει κανείς απευθείας, και ένα πιο ψηλό για να γεμίζει μπουκάλια και παγούρια. Μία στις τρεις έχει και μια μικρή λεκάνη στο έδαφος για τα σκυλιά.", "The fountains have two spouts: one for drinking directly, and a higher one for filling bottles and flasks. One in three also has a small bowl on the ground for dogs."),
  L("Εκφωνήτρια", "f", "Σύμφωνα με τον δήμο, το νερό ελέγχεται κάθε μήνα, και τα αποτελέσματα θα αναρτώνται στην ιστοσελίδα. Τα σχολεία της πόλης θα μοιράσουν στους μαθητές δωρεάν παγούρια.", "According to the municipality, the water is tested every month, and the results will be posted on the website. The city's schools will hand out free flasks to pupils."),
 ],
 "questions": [
  Q("Ποιος είναι ο στόχος του δήμου;", ["Να μειωθεί η χρήση πλαστικών μπουκαλιών", "Να ποτίζονται τα πάρκα", "Να μειωθεί ο λογαριασμός του νερού", "Να γίνει η πόλη πιο δροσερή"], 0, "Στόχος του δήμου είναι να μειωθεί η χρήση πλαστικών μπουκαλιών"),
  Q("Τι έχει μία στις τρεις βρύσες;", ["Οθόνη με πληροφορίες", "Ζεστό νερό", "Μια μικρή λεκάνη για τα σκυλιά", "Ψυγείο"], 2, "Μία στις τρεις έχει και μια μικρή λεκάνη στο έδαφος για τα σκυλιά"),
  Q("Τι θα μοιράσουν τα σχολεία;", ["Δωρεάν μπουκάλια νερό", "Δωρεάν παγούρια", "Φυλλάδια", "Εισιτήρια λεωφορείου"], 1, "Τα σχολεία της πόλης θα μοιράσουν στους μαθητές δωρεάν παγούρια"),
 ],
 "gloss": {"βρύσες": "βρύση — tap, fountain", "πόσιμο": "πόσιμος — drinkable", "τοποθετήθηκαν": "τοποθετούμαι — to be installed", "στόμια": "στόμιο — spout, opening", "απευθείας": "απευθείας — directly", "παγούρια": "παγούρι — water bottle, flask", "λεκάνη": "λεκάνη — bowl, basin", "ελέγχεται": "ελέγχομαι — to be tested", "αναρτώνται": "αναρτώμαι — to be posted"}
})

ITEMS.append({
 "id": "l146-mon-katapsyktis", "title": "Πώς ξεπαγώνουμε τον καταψύκτη", "title_en": "How to defrost the freezer", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε ένα απόσπασμα από μια εκπομπή με πρακτικές συμβουλές για το σπίτι.",
 "script": [
  L("Παρουσιαστής", "m", "Όταν ο πάγος στον καταψύκτη ξεπεράσει το μισό εκατοστό, ο καταψύκτης καταναλώνει περισσότερο ρεύμα. Γι' αυτό καλό είναι να τον ξεπαγώνουμε τουλάχιστον μία φορά τον χρόνο, ιδανικά τον χειμώνα, όταν η κουζίνα είναι δροσερή.", "When the ice in the freezer is thicker than half a centimetre, the freezer uses more electricity. That's why it's a good idea to defrost it at least once a year, ideally in winter, when the kitchen is cool."),
  L("Παρουσιαστής", "m", "Πρώτα αδειάζουμε τα τρόφιμα και τα βάζουμε σε μια τσάντα-ψυγείο, ή απλώς στο μπαλκόνι, αν κάνει κρύο. Μετά βγάζουμε τον καταψύκτη από την πρίζα και αφήνουμε την πόρτα ανοιχτή, με πετσέτες από κάτω.", "First we empty the food and put it in a cool bag, or simply on the balcony if it's cold. Then we unplug the freezer and leave the door open, with towels underneath."),
  L("Παρουσιαστής", "m", "Για να πάει πιο γρήγορα, βάλτε μέσα ένα κατσαρόλι με ζεστό νερό. Μη χρησιμοποιήσετε ποτέ μαχαίρι για να σπάσετε τον πάγο, γιατί μπορεί να τρυπήσετε τα τοιχώματα. Στο τέλος σκουπίστε καλά, και περιμένετε μισή ώρα πριν βάλετε ξανά τα τρόφιμα.", "To make it go faster, put a pan of hot water inside. Never use a knife to break the ice, because you might puncture the walls. At the end wipe it well, and wait half an hour before putting the food back."),
 ],
 "questions": [
  Q("Γιατί πρέπει να ξεπαγώνουμε τον καταψύκτη;", ["Γιατί με πολύ πάγο καταναλώνει περισσότερο ρεύμα", "Γιατί χαλάνε τα τρόφιμα", "Γιατί κάνει θόρυβο", "Γιατί μυρίζει"], 0, "ο καταψύκτης καταναλώνει περισσότερο ρεύμα"),
  Q("Τι βοηθάει να πάει πιο γρήγορα το ξεπάγωμα;", ["Ένα σεσουάρ", "Ένα μαχαίρι", "Ένα κατσαρόλι με ζεστό νερό", "Αλάτι"], 2, "βάλτε μέσα ένα κατσαρόλι με ζεστό νερό"),
  Q("Γιατί δεν πρέπει να χρησιμοποιούμε μαχαίρι;", ["Γιατί είναι επικίνδυνο για τα χέρια", "Γιατί μπορεί να τρυπήσουμε τα τοιχώματα", "Γιατί χαλάει το μαχαίρι", "Γιατί αργεί περισσότερο"], 1, "μπορεί να τρυπήσετε τα τοιχώματα"),
 ],
 "gloss": {"καταψύκτη": "καταψύκτης — freezer", "ξεπεράσει": "ξεπερνώ — to exceed", "καταναλώνει": "καταναλώνω — to consume", "ξεπαγώνουμε": "ξεπαγώνω — to defrost", "τσάντα-ψυγείο": "τσάντα-ψυγείο — cool bag", "πρίζα": "πρίζα — socket", "κατσαρόλι": "κατσαρόλι — saucepan", "τρυπήσετε": "τρυπάω — to puncture", "τοιχώματα": "τοίχωμα — (inner) wall", "σκουπίστε": "σκουπίζω — to wipe"}
})

ITEMS.append({
 "id": "l146-rep-epitrapezia", "title": "Η επιστροφή των επιτραπέζιων", "title_en": "The return of board games", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για τον ελεύθερο χρόνο.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε μια εποχή που περνάμε τόσες ώρες μπροστά σε οθόνες, τα επιτραπέζια παιχνίδια ζουν μια απρόσμενη αναγέννηση. Στην Αθήνα και στη Θεσσαλονίκη έχουν ανοίξει τα τελευταία χρόνια αρκετά καφέ όπου οι πελάτες πληρώνουν για να παίξουν, όχι μόνο για να πιουν.", "At a time when we spend so many hours in front of screens, board games are enjoying an unexpected revival. In Athens and Thessaloniki several cafés have opened in recent years where customers pay to play, not just to drink."),
  L("Ρεπόρτερ", "m", "Σε ένα τέτοιο καφέ στα Πετράλωνα, τα ράφια έχουν πάνω από οχτακόσια παιχνίδια. Ο ιδιοκτήτης, ο Άρης, εξηγεί τους κανόνες σε όσους δεν τους ξέρουν. «Οι περισσότεροι έρχονται για ένα παιχνίδι και μένουν τρεις ώρες», λέει.", "In one such café in Petralona, the shelves hold more than eight hundred games. The owner, Aris, explains the rules to those who don't know them. \"Most people come for one game and stay three hours,\" he says."),
  L("Ρεπόρτερ", "m", "Οι ψυχολόγοι λένε ότι τα επιτραπέζια βοηθούν τους ανθρώπους να μιλήσουν πρόσωπο με πρόσωπο, και τα παιδιά να μάθουν να χάνουν. Ο Άρης έχει τη δική του εξήγηση: «Στο κινητό παίζεις μόνος σου. Εδώ γελάς με τους άλλους.»", "Psychologists say board games help people talk face to face, and help children learn to lose. Aris has his own explanation: \"On your phone you play alone. Here you laugh with others.\""),
 ],
 "questions": [
  Q("Τι συμβαίνει με τα επιτραπέζια παιχνίδια σύμφωνα με το ρεπορτάζ;", ["Ζουν μια απρόσμενη αναγέννηση", "Δεν τα παίζει πια κανείς", "Απαγορεύονται στα καφέ", "Παίζονται μόνο από παιδιά"], 0, "τα επιτραπέζια παιχνίδια ζουν μια απρόσμενη αναγέννηση"),
  Q("Τι κάνει ο Άρης για τους νέους πελάτες;", ["Τους κάνει έκπτωση", "Τους εξηγεί τους κανόνες", "Τους δανείζει παιχνίδια για το σπίτι", "Τους διαλέγει αντίπαλο"], 1, "εξηγεί τους κανόνες σε όσους δεν τους ξέρουν"),
  Q("Σε τι βοηθούν τα επιτραπέζια τα παιδιά, κατά τους ψυχολόγους;", ["Στα μαθηματικά", "Στον ύπνο", "Να μάθουν να χάνουν", "Να διαβάζουν γρηγορότερα"], 2, "τα παιδιά να μάθουν να χάνουν"),
 ],
 "gloss": {"επιτραπέζια": "επιτραπέζιο (παιχνίδι) — board game", "απρόσμενη": "απρόσμενος — unexpected", "αναγέννηση": "αναγέννηση — revival, renaissance", "ράφια": "ράφι — shelf", "ιδιοκτήτης": "ιδιοκτήτης — owner", "κανόνες": "κανόνας — rule", "πρόσωπο με πρόσωπο": "πρόσωπο με πρόσωπο — face to face", "εξήγηση": "εξήγηση — explanation"}
})

ITEMS.append({
 "id": "l146-dia-vardia", "title": "Αλλάζουμε βάρδια;", "title_en": "Shall we swap shifts?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο ανάμεσα σε δύο συναδέλφους σε ένα σούπερ μάρκετ.",
 "script": [
  L("Κατερίνα", "f", "Στέλιο, έχεις ένα λεπτό; Το Σάββατο έχω πρωινή βάρδια, αλλά παντρεύεται η ξαδέρφη μου στο χωριό. Μήπως μπορούμε να αλλάξουμε; Εγώ να κάνω τη δική σου βάρδια την Κυριακή.", "Stelios, have you got a minute? On Saturday I'm on the morning shift, but my cousin is getting married in the village. Could we swap? I'd do your shift on Sunday."),
  L("Στέλιος", "m", "Την Κυριακή έχω απογευματινή, ως τις δέκα το βράδυ. Σε πειράζει να κλείσεις εσύ το μαγαζί;", "On Sunday I'm on the afternoon shift, until ten at night. Do you mind closing the shop?"),
  L("Κατερίνα", "f", "Καθόλου. Πρέπει όμως να το εγκρίνει ο υπεύθυνος βάρδιας. Τη φορά που άλλαξα με τη Δήμητρα χωρίς να τον ρωτήσω, έγινε φασαρία.", "Not at all. But the shift supervisor has to approve it. The time I swapped with Dimitra without asking him, there was a fuss."),
  L("Στέλιος", "m", "Τότε στείλ' του ένα μήνυμα τώρα, και γράψε ότι συμφωνώ κι εγώ. Α, και φέρε μου κουφέτα από τον γάμο.", "Then send him a message now, and write that I agree too. Oh, and bring me some sugared almonds from the wedding."),
 ],
 "questions": [
  Q("Γιατί θέλει η Κατερίνα να αλλάξει βάρδια;", ["Είναι άρρωστη", "Παντρεύεται η ξαδέρφη της", "Έχει εξετάσεις", "Πάει διακοπές"], 1, "παντρεύεται η ξαδέρφη μου στο χωριό"),
  Q("Τι θα πρέπει να κάνει η Κατερίνα την Κυριακή;", ["Να ανοίξει το μαγαζί το πρωί", "Να κλείσει το μαγαζί στις δέκα το βράδυ", "Να κάνει απογραφή", "Τίποτα"], 1, "Σε πειράζει να κλείσεις εσύ το μαγαζί;"),
  Q("Γιατί θέλει να ρωτήσει τον υπεύθυνο βάρδιας;", ["Γιατί την τελευταία φορά που δεν ρώτησε έγινε φασαρία", "Γιατί θέλει άδεια μίας εβδομάδας", "Γιατί θέλει να πληρωθεί υπερωρίες", "Γιατί ο Στέλιος δεν συμφωνεί"], 0, "Τη φορά που άλλαξα με τη Δήμητρα χωρίς να τον ρωτήσω, έγινε φασαρία"),
 ],
 "gloss": {"βάρδια": "βάρδια — shift", "πρωινή": "πρωινός — morning", "ξαδέρφη": "ξαδέρφη — cousin (female)", "απογευματινή": "απογευματινός — afternoon", "εγκρίνει": "εγκρίνω — to approve", "υπεύθυνος": "υπεύθυνος — supervisor, person in charge", "φασαρία": "φασαρία — fuss, trouble", "κουφέτα": "κουφέτο — sugared almond"}
})

ITEMS.append({
 "id": "l146-c1-moore", "title": "Ο νόμος του Μουρ", "title_en": "Moore's law", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ομιλία για την ιστορία της τεχνολογίας.",
 "script": [
  L("Ομιλήτρια", "f", "Το 1965 ο Γκόρντον Μουρ, που αργότερα θα συνίδρυε την Intel, δημοσίευσε ένα σύντομο άρθρο με μια τολμηρή πρόβλεψη: ο αριθμός των εξαρτημάτων που χωρούν σε ένα ολοκληρωμένο κύκλωμα θα διπλασιαζόταν περίπου κάθε χρόνο. Δέκα χρόνια αργότερα αναθεώρησε την εκτίμησή του σε έναν διπλασιασμό κάθε δύο χρόνια.", "In 1965 Gordon Moore, who would later co-found Intel, published a short article with a bold prediction: the number of components that fit on an integrated circuit would double roughly every year. Ten years later he revised his estimate to a doubling every two years."),
  L("Ομιλήτρια", "f", "Ο «νόμος» του Μουρ δεν είναι νόμος της φύσης, όπως η βαρύτητα. Είναι μια εμπειρική παρατήρηση, η οποία σε μεγάλο βαθμό αυτοεπιβεβαιώθηκε: η βιομηχανία την υιοθέτησε ως στόχο, και οι εταιρείες σχεδίαζαν την έρευνά τους ώστε να μη μείνουν πίσω από την καμπύλη.", "Moore's \"law\" is not a law of nature, like gravity. It is an empirical observation which to a large extent fulfilled itself: the industry adopted it as a target, and companies planned their research so as not to fall behind the curve."),
  L("Ομιλήτρια", "f", "Για δεκαετίες, η πρόβλεψη επαληθευόταν με εντυπωσιακή ακρίβεια, και σε αυτήν οφείλουμε εν μέρει το ότι ένα κινητό σήμερα είναι ισχυρότερο από τους υπολογιστές που έστειλαν ανθρώπους στη Σελήνη.", "For decades the prediction held with impressive accuracy, and we owe to it in part the fact that a mobile phone today is more powerful than the computers that sent people to the Moon."),
  L("Ομιλήτρια", "f", "Τα τελευταία χρόνια όμως ο ρυθμός έχει επιβραδυνθεί, καθώς τα τρανζίστορ πλησιάζουν το μέγεθος λίγων ατόμων και το κόστος της κατασκευής εκτοξεύεται. Πολλοί μιλούν για το τέλος του νόμου· άλλοι πιστεύουν ότι η πρόοδος απλώς θα πάρει άλλες μορφές.", "In recent years, though, the pace has slowed, as transistors approach the size of a few atoms and the cost of manufacturing soars. Many speak of the end of the law; others believe progress will simply take other forms."),
 ],
 "questions": [
  Q("Τι προέβλεπε αρχικά ο Μουρ το 1965;", ["Ότι οι υπολογιστές θα γίνονταν φθηνότεροι κάθε χρόνο", "Ότι ο αριθμός των εξαρτημάτων σε ένα κύκλωμα θα διπλασιαζόταν περίπου κάθε χρόνο", "Ότι κάθε σπίτι θα είχε υπολογιστή", "Ότι η Intel θα γινόταν η μεγαλύτερη εταιρεία"], 1, "θα διπλασιαζόταν περίπου κάθε χρόνο"),
  Q("Γιατί λέγεται ότι ο νόμος «αυτοεπιβεβαιώθηκε»;", ["Γιατί η βιομηχανία τον υιοθέτησε ως στόχο", "Γιατί αποδείχτηκε μαθηματικά", "Γιατί τον επιβεβαίωσε η NASA", "Γιατί ο Μουρ τον άλλαξε"], 0, "η βιομηχανία την υιοθέτησε ως στόχο"),
  Q("Τι οφείλουμε εν μέρει στην πρόβλεψη, σύμφωνα με την ομιλήτρια;", ["Τα ταξίδια στη Σελήνη", "Τη μείωση του κόστους της ενέργειας", "Το ότι ένα κινητό είναι ισχυρότερο από τους υπολογιστές των αποστολών στη Σελήνη", "Την εφεύρεση του τρανζίστορ"], 2, "ένα κινητό σήμερα είναι ισχυρότερο από τους υπολογιστές που έστειλαν ανθρώπους στη Σελήνη"),
  Q("Γιατί έχει επιβραδυνθεί ο ρυθμός;", ["Γιατί δεν υπάρχει πια ζήτηση", "Γιατί απαγορεύτηκε από τις κυβερνήσεις", "Γιατί οι εταιρείες έχασαν το ενδιαφέρον τους", "Γιατί τα τρανζίστορ πλησιάζουν το μέγεθος λίγων ατόμων και το κόστος εκτοξεύεται"], 3, "τα τρανζίστορ πλησιάζουν το μέγεθος λίγων ατόμων"),
 ],
 "gloss": {"συνίδρυε": "συνιδρύω — to co-found", "τολμηρή": "τολμηρός — bold", "εξαρτημάτων": "εξάρτημα — component", "ολοκληρωμένο κύκλωμα": "ολοκληρωμένο κύκλωμα — integrated circuit", "αναθεώρησε": "αναθεωρώ — to revise", "εμπειρική": "εμπειρικός — empirical", "αυτοεπιβεβαιώθηκε": "αυτοεπιβεβαιώνομαι — to fulfil itself", "υιοθέτησε": "υιοθετώ — to adopt", "καμπύλη": "καμπύλη — curve", "επαληθευόταν": "επαληθεύομαι — to be borne out", "επιβραδυνθεί": "επιβραδύνομαι — to slow down", "εκτοξεύεται": "εκτοξεύομαι — to soar"}
})

ITEMS.append({
 "id": "l146-c1-ikea", "title": "Το φαινόμενο ΙΚΕΑ", "title_en": "The IKEA effect", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή για την ψυχολογία της κατανάλωσης, με καλεσμένο έναν ερευνητή.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι είναι το λεγόμενο «φαινόμενο ΙΚΕΑ»;", "What is the so-called \"IKEA effect\"?"),
  L("Ερευνητής", "m", "Είναι η τάση μας να δίνουμε μεγαλύτερη αξία σε πράγματα που έχουμε φτιάξει ή συναρμολογήσει μόνοι μας. Το όνομα το έδωσαν τρεις ερευνητές, ανάμεσά τους ο Νταν Αριέλι, σε μια μελέτη που δημοσιεύτηκε το 2011. Οι συμμετέχοντες που συναρμολόγησαν ένα απλό κουτί αποθήκευσης ήταν διατεθειμένοι να πληρώσουν γι' αυτό σημαντικά περισσότερα από όσους το πήραν έτοιμο.", "It's our tendency to place greater value on things we have made or assembled ourselves. The name was given by three researchers, among them Dan Ariely, in a study published in 2011. Participants who assembled a simple storage box were willing to pay significantly more for it than those who got it ready-made."),
  L("Δημοσιογράφος", "f", "Ισχύει πάντα;", "Does it always hold?"),
  L("Ερευνητής", "m", "Όχι. Το φαινόμενο χάνεται όταν η κατασκευή μένει ημιτελής ή όταν οι συμμετέχοντες την αποτυγχάνουν. Με άλλα λόγια, δεν αγαπάμε τον κόπο καθαυτόν, αλλά τον κόπο που καταλήγει σε επιτυχία. Η ικανοποίηση πηγάζει από την αίσθηση ότι είμαστε ικανοί.", "No. The effect disappears when the construction is left unfinished or when the participants fail at it. In other words, we don't love effort as such, but effort that ends in success. The satisfaction comes from the feeling of being competent."),
  L("Δημοσιογράφος", "f", "Συχνά ακούμε την ιστορία με τα έτοιμα μείγματα για κέικ, στα οποία προστέθηκε η οδηγία να βάζει κανείς ένα αυγό.", "We often hear the story about cake mixes, to which the instruction to add an egg was added."),
  L("Ερευνητής", "m", "Είναι μια ωραία ιστορία, αλλά τα ιστορικά στοιχεία γι' αυτήν είναι αμφιλεγόμενα. Καλό είναι να την αντιμετωπίζουμε περισσότερο ως μύθο της διαφήμισης παρά ως απόδειξη.", "It's a nice story, but the historical evidence for it is disputed. It's best to treat it more as an advertising myth than as proof."),
 ],
 "questions": [
  Q("Τι είναι το φαινόμενο ΙΚΕΑ;", ["Η τάση να δίνουμε μεγαλύτερη αξία σε πράγματα που φτιάξαμε μόνοι μας", "Η προτίμηση για φθηνά έπιπλα", "Η τάση να αγοράζουμε περισσότερα από όσα χρειαζόμαστε", "Ο φόβος να συναρμολογούμε έπιπλα"], 0, "η τάση μας να δίνουμε μεγαλύτερη αξία σε πράγματα που έχουμε φτιάξει ή συναρμολογήσει μόνοι μας"),
  Q("Τι έδειξε η μελέτη του 2011;", ["Ότι οι συμμετέχοντες προτιμούσαν τα έτοιμα κουτιά", "Ότι όσοι συναρμολόγησαν το κουτί ήταν διατεθειμένοι να πληρώσουν περισσότερα", "Ότι κανείς δεν μπορούσε να συναρμολογήσει το κουτί", "Ότι η τιμή δεν είχε σημασία"], 1, "ήταν διατεθειμένοι να πληρώσουν γι' αυτό σημαντικά περισσότερα"),
  Q("Πότε χάνεται το φαινόμενο;", ["Όταν το αντικείμενο είναι ακριβό", "Όταν η κατασκευή διαρκεί πολύ", "Όταν η κατασκευή μένει ημιτελής ή αποτυγχάνει", "Όταν βοηθούν και άλλοι"], 2, "όταν η κατασκευή μένει ημιτελής ή όταν οι συμμετέχοντες την αποτυγχάνουν"),
  Q("Τι λέει ο ερευνητής για την ιστορία με τα μείγματα για κέικ;", ["Ότι είναι αποδεδειγμένη", "Ότι την επινόησε ο ίδιος", "Ότι αφορά μόνο την Αμερική", "Ότι τα ιστορικά στοιχεία γι' αυτήν είναι αμφιλεγόμενα"], 3, "τα ιστορικά στοιχεία γι' αυτήν είναι αμφιλεγόμενα"),
 ],
 "gloss": {"συναρμολογήσει": "συναρμολογώ — to assemble", "διατεθειμένοι": "διατεθειμένος — willing", "ημιτελής": "ημιτελής — unfinished", "καθαυτόν": "καθαυτός — as such, in itself", "πηγάζει": "πηγάζω — to stem from", "ικανοί": "ικανός — capable, competent", "μείγματα": "μείγμα — mix", "αμφιλεγόμενα": "αμφιλεγόμενος — disputed, controversial", "απόδειξη": "απόδειξη — proof"}
})

rnd = random.Random(146)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-146.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
