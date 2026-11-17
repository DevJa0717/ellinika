# Source for library/listening/listening-138.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l138.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l138-vm-thyrotilefono", "title": "Το δέμα που δεν παραδόθηκε", "title_en": "The parcel that wasn't delivered", "type": "voicemail", "level": "B2",
 "context_el": "Περιμένετε ένα δέμα. Ακούτε ένα μήνυμα από τον κούριερ στον τηλεφωνητή σας.",
 "script": [
  L("Κούριερ", "m", "Καλημέρα σας, από την εταιρεία ταχυμεταφορών σας παίρνω. Ήρθα σήμερα στις έντεκα για να σας παραδώσω ένα δέμα, αλλά το θυροτηλέφωνο της πολυκατοικίας δεν λειτουργεί. Χτύπησα το κουδούνι σας τρεις φορές και δεν άκουσα τίποτα, ούτε μπορούσα να μπω στην είσοδο.", "Good morning, I'm calling from the courier company. I came today at eleven to deliver a parcel to you, but the building's intercom isn't working. I rang your bell three times and heard nothing, and I couldn't get into the entrance either."),
  L("Κούριερ", "m", "Αύριο θα ξαναπεράσω ανάμεσα στις δέκα και στις δώδεκα. Αν θέλετε, στείλτε μου ένα μήνυμα σε αυτό τον αριθμό όταν θα είστε σπίτι, και θα σας τηλεφωνήσω μόλις φτάσω έξω από την πόρτα, για να κατεβείτε.", "Tomorrow I'll come by again between ten and twelve. If you like, send me a message at this number when you're at home, and I'll call you as soon as I'm outside the door, so that you can come down."),
  L("Κούριερ", "m", "Αν πάλι δεν σας βρω, το δέμα θα μείνει πέντε εργάσιμες μέρες στο κατάστημά μας στην οδό Πατησίων, και μπορείτε να το παραλάβετε με την ταυτότητά σας. Καλή συνέχεια.", "If I don't find you again, the parcel will stay for five working days at our shop on Patision Street, and you can collect it with your ID card. Have a good day."),
 ],
 "questions": [
  Q("Γιατί δεν παραδόθηκε το δέμα;", ["Γιατί η διεύθυνση ήταν λάθος", "Γιατί το θυροτηλέφωνο της πολυκατοικίας δεν λειτουργεί", "Γιατί το δέμα ήταν πολύ βαρύ", "Γιατί ο κούριερ άργησε πολύ"], 1, "το θυροτηλέφωνο της πολυκατοικίας δεν λειτουργεί"),
  Q("Τι σας ζητά να κάνετε ο κούριερ για αύριο;", ["Να του στείλετε μήνυμα όταν θα είστε σπίτι", "Να αφήσετε την είσοδο ανοιχτή", "Να πάτε εσείς στο κατάστημα", "Να αλλάξετε τη διεύθυνση"], 0, "στείλτε μου ένα μήνυμα σε αυτό τον αριθμό όταν θα είστε σπίτι"),
  Q("Τι θα χρειαστείτε για να παραλάβετε το δέμα από το κατάστημα;", ["Την απόδειξη αγοράς", "Έναν κωδικό στο κινητό", "Την ταυτότητά σας", "Μια εξουσιοδότηση"], 2, "μπορείτε να το παραλάβετε με την ταυτότητά σας"),
 ],
 "gloss": {"κούριερ": "κούριερ — courier", "ταχυμεταφορών": "ταχυμεταφορές — courier services", "παραδώσω": "παραδίδω — to deliver", "θυροτηλέφωνο": "θυροτηλέφωνο — intercom", "λειτουργεί": "λειτουργώ — to work, function", "κουδούνι": "κουδούνι — doorbell", "είσοδο": "είσοδος — entrance", "εργάσιμες": "εργάσιμος — working (day)", "παραλάβετε": "παραλαμβάνω — to collect, receive"}
})

ITEMS.append({
 "id": "l138-dia-afygrantiras", "title": "Μούχλα στην κρεβατοκάμαρα", "title_en": "Mould in the bedroom", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο συγκάτοικους να συζητούν στο σαλόνι τους.",
 "script": [
  L("Νίκος", "m", "Είδες τη γωνία πάνω από την ντουλάπα μου; Έχει γεμίσει μαύρες κουκκίδες. Και τα παπούτσια μου στο κάτω ράφι μυρίζουν υγρασία.", "Have you seen the corner above my wardrobe? It's full of black spots. And my shoes on the bottom shelf smell damp."),
  L("Σοφία", "f", "Μούχλα είναι. Το σπίτι είναι ισόγειο, και τον χειμώνα δεν ανοίγουμε σχεδόν ποτέ τα παράθυρα. Λέω να πάρουμε έναν αφυγραντήρα. Η αδερφή μου έχει έναν και μαζεύει δύο λίτρα νερό τη μέρα.", "It's mould. The flat is on the ground floor, and in winter we hardly ever open the windows. I say we get a dehumidifier. My sister has one and it collects two litres of water a day."),
  L("Νίκος", "m", "Δεν θα ανεβάσει πολύ το ρεύμα; Και δεν κάνει θόρυβο;", "Won't it push up the electricity bill a lot? And doesn't it make noise?"),
  L("Σοφία", "f", "Καταναλώνει λιγότερο από ένα ηλεκτρικό καλοριφέρ. Τον βάζουμε στη δική σου κρεβατοκάμαρα όσο είσαι στη δουλειά, για να μη σε ενοχλεί. Αλλά πρέπει κι εμείς να αερίζουμε δέκα λεπτά κάθε πρωί, αλλιώς θα πληρώνουμε για να διορθώνουμε τις κακές μας συνήθειες.", "It uses less than an electric radiator. We'll put it in your bedroom while you're at work, so it doesn't bother you. But we also have to air the place for ten minutes every morning, otherwise we'll be paying to fix our bad habits."),
 ],
 "questions": [
  Q("Τι πρόβλημα έχει ο Νίκος στο δωμάτιό του;", ["Το παράθυρο δεν κλείνει", "Μαύρες κουκκίδες στη γωνία και παπούτσια που μυρίζουν υγρασία", "Η ντουλάπα έσπασε", "Κάνει πολύ ζέστη"], 1, "Έχει γεμίσει μαύρες κουκκίδες. Και τα παπούτσια μου στο κάτω ράφι μυρίζουν υγρασία"),
  Q("Τι ανησυχεί τον Νίκο για τον αφυγραντήρα;", ["Το ρεύμα και ο θόρυβος", "Η τιμή αγοράς", "Το μέγεθος", "Η εγγύηση"], 0, "Δεν θα ανεβάσει πολύ το ρεύμα; Και δεν κάνει θόρυβο;"),
  Q("Τι λέει η Σοφία ότι πρέπει να κάνουν κι εκείνοι;", ["Να βάψουν τον τοίχο", "Να μετακομίσουν", "Να αερίζουν δέκα λεπτά κάθε πρωί", "Να βάζουν καλοριφέρ όλη τη νύχτα"], 2, "πρέπει κι εμείς να αερίζουμε δέκα λεπτά κάθε πρωί"),
 ],
 "gloss": {"συγκάτοικους": "συγκάτοικος — flatmate", "κουκκίδες": "κουκκίδα — dot, spot", "ράφι": "ράφι — shelf", "υγρασία": "υγρασία — damp, humidity", "Μούχλα": "μούχλα — mould", "ισόγειο": "ισόγειο — ground floor", "αφυγραντήρα": "αφυγραντήρας — dehumidifier", "Καταναλώνει": "καταναλώνω — to consume", "ενοχλεί": "ενοχλώ — to bother", "αερίζουμε": "αερίζω — to air"}
})

ITEMS.append({
 "id": "l138-news-vrysoules", "title": "Δωρεάν νερό στις πλατείες", "title_en": "Free water in the squares", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα σύντομο ρεπορτάζ στις τοπικές ειδήσεις.",
 "script": [
  L("Ρεπόρτερ", "f", "Είκοσι νέες βρυσούλες πόσιμου νερού τοποθετήθηκαν αυτή την εβδομάδα σε πλατείες, πάρκα και στάσεις λεωφορείων του δήμου. Ο στόχος, όπως εξηγεί η αντιδήμαρχος περιβάλλοντος, είναι να αγοράζουμε λιγότερα πλαστικά μπουκάλια και να έχουν όλοι πρόσβαση σε δροσερό νερό τις ζεστές μέρες.", "Twenty new drinking-water fountains were installed this week in squares, parks and bus stops in the municipality. The aim, as the deputy mayor for the environment explains, is for us to buy fewer plastic bottles and for everyone to have access to cool water on hot days."),
  L("Ρεπόρτερ", "f", "Κάθε βρυσούλα έχει δύο βρύσες: μία ψηλή για τους ενήλικες, που γεμίζει και παγούρια, και μία χαμηλή για τα παιδιά και για τους ανθρώπους σε αναπηρικό αμαξίδιο. Στη βάση υπάρχει και ένα μικρό μπολ για τους σκύλους.", "Each fountain has two taps: a tall one for adults, which also fills water bottles, and a low one for children and for people in wheelchairs. At the base there is also a small bowl for dogs."),
  L("Ρεπόρτερ", "f", "Το νερό ελέγχεται από εργαστήριο κάθε μήνα, και τα αποτελέσματα θα δημοσιεύονται στην ιστοσελίδα του δήμου. Αν η δοκιμή πετύχει, μέχρι το καλοκαίρι θα έχουν μπει άλλες τριάντα.", "The water is tested by a laboratory every month, and the results will be published on the municipality's website. If the trial succeeds, another thirty will have been put in by the summer."),
 ],
 "questions": [
  Q("Ποιος είναι ο στόχος των νέων βρυσών;", ["Να πληρώνουμε λιγότερο νερό στο σπίτι", "Να αγοράζουμε λιγότερα πλαστικά μπουκάλια και να έχουν όλοι πρόσβαση σε νερό", "Να ποτίζονται τα πάρκα", "Να διακοσμηθούν οι πλατείες"], 1, "να αγοράζουμε λιγότερα πλαστικά μπουκάλια και να έχουν όλοι πρόσβαση σε δροσερό νερό"),
  Q("Για ποιους είναι η χαμηλή βρύση;", ["Για τους ποδηλάτες", "Για τους σκύλους", "Για τα παιδιά και τους ανθρώπους σε αναπηρικό αμαξίδιο", "Για τους υπαλλήλους του δήμου"], 2, "μία χαμηλή για τα παιδιά και για τους ανθρώπους σε αναπηρικό αμαξίδιο"),
  Q("Πού θα δημοσιεύονται τα αποτελέσματα των ελέγχων;", ["Στην ιστοσελίδα του δήμου", "Πάνω σε κάθε βρυσούλα", "Στην τοπική εφημερίδα", "Πουθενά"], 0, "τα αποτελέσματα θα δημοσιεύονται στην ιστοσελίδα του δήμου"),
 ],
 "gloss": {"βρυσούλες": "βρυσούλα — small fountain, tap", "πόσιμου": "πόσιμος — drinkable", "τοποθετήθηκαν": "τοποθετούμαι — to be installed", "αντιδήμαρχος": "αντιδήμαρχος — deputy mayor", "πρόσβαση": "πρόσβαση — access", "παγούρια": "παγούρι — water bottle, flask", "αναπηρικό αμαξίδιο": "αναπηρικό αμαξίδιο — wheelchair", "ελέγχεται": "ελέγχομαι — to be tested", "δημοσιεύονται": "δημοσιεύομαι — to be published", "δοκιμή": "δοκιμή — trial"}
})

ITEMS.append({
 "id": "l138-int-nychtofylakas", "title": "Μόνος με τα αγάλματα", "title_en": "Alone with the statues", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική εκπομπή για τις νυχτερινές δουλειές.",
 "script": [
  L("Δημοσιογράφος", "f", "Δουλεύετε δεκαπέντε χρόνια ως νυχτοφύλακας σε αρχαιολογικό μουσείο. Πώς είναι μια νύχτα σας;", "You've worked for fifteen years as a night guard in an archaeological museum. What is one of your nights like?"),
  L("Νυχτοφύλακας", "m", "Πιάνω δουλειά στις δέκα. Πρώτα ελέγχω με τη συνάδελφο της απογευματινής βάρδιας ότι όλες οι πόρτες και τα παράθυρα είναι κλειστά. Μετά κάθομαι στο δωμάτιο με τις οθόνες των καμερών, και κάθε δύο ώρες κάνω έναν γύρο σε όλες τις αίθουσες με τον φακό.", "I start work at ten. First, with my colleague from the afternoon shift, I check that all the doors and windows are closed. Then I sit in the room with the camera screens, and every two hours I do a round of all the halls with a torch."),
  L("Δημοσιογράφος", "f", "Δεν φοβάστε;", "Aren't you afraid?"),
  L("Νυχτοφύλακας", "m", "Τα πρώτα βράδια, λίγο. Τα αγάλματα στο σκοτάδι φαίνονται σαν να σε κοιτάνε. Τώρα πια τους λέω καληνύχτα. Το πιο συνηθισμένο πρόβλημα δεν είναι οι κλέφτες, αλλά οι συναγερμοί που χτυπούν χωρίς λόγο, συνήθως από μια αράχνη μπροστά σε κάποιον αισθητήρα.", "The first nights, a little. In the dark the statues look as if they are watching you. Now I say goodnight to them. The most common problem isn't thieves, but alarms that go off for no reason, usually because of a spider in front of a sensor."),
 ],
 "questions": [
  Q("Τι κάνει ο νυχτοφύλακας κάθε δύο ώρες;", ["Γράφει μια αναφορά", "Κάνει έναν γύρο σε όλες τις αίθουσες με τον φακό", "Τηλεφωνεί στον διευθυντή", "Αλλάζει τις κάμερες"], 1, "κάθε δύο ώρες κάνω έναν γύρο σε όλες τις αίθουσες με τον φακό"),
  Q("Πώς ένιωθε τα πρώτα βράδια;", ["Βαριόταν πολύ", "Φοβόταν λίγο, γιατί τα αγάλματα έμοιαζαν να τον κοιτάνε", "Ήταν πολύ κουρασμένος", "Δεν ένιωθε τίποτα"], 1, "Τα αγάλματα στο σκοτάδι φαίνονται σαν να σε κοιτάνε"),
  Q("Ποιο είναι το πιο συνηθισμένο πρόβλημα;", ["Οι κλέφτες", "Οι διακοπές ρεύματος", "Οι συναγερμοί που χτυπούν χωρίς λόγο", "Τα ζώα που μπαίνουν στις αίθουσες"], 2, "οι συναγερμοί που χτυπούν χωρίς λόγο"),
 ],
 "gloss": {"νυχτοφύλακας": "νυχτοφύλακας — night guard", "συνάδελφο": "συνάδελφος — colleague", "βάρδιας": "βάρδια — shift", "οθόνες": "οθόνη — screen", "αίθουσες": "αίθουσα — hall, gallery", "φακό": "φακός — torch, flashlight", "αγάλματα": "άγαλμα — statue", "συναγερμοί": "συναγερμός — alarm", "αράχνη": "αράχνη — spider", "αισθητήρα": "αισθητήρας — sensor"}
})

ITEMS.append({
 "id": "l138-ann-kladema", "title": "Κλάδεμα δέντρων στη γειτονιά", "title_en": "Tree pruning in the neighbourhood", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ηχογραφημένη ανακοίνωση από αυτοκίνητο του δήμου που περνά από τη γειτονιά σας.",
 "script": [
  L("Εκφωνητής", "m", "Ο δήμος ενημερώνει τους κατοίκους ότι από τη Δευτέρα έως την Τετάρτη θα γίνει κλάδεμα των δέντρων στις οδούς Ερμού, Αθηνάς και Σαπφούς, από τις επτά το πρωί έως τις τρεις το μεσημέρι.", "The municipality informs residents that from Monday to Wednesday tree pruning will take place on Ermou, Athinas and Sapfous Streets, from seven in the morning until three in the afternoon."),
  L("Εκφωνητής", "m", "Παρακαλούνται οι οδηγοί να μην αφήνουν τα αυτοκίνητά τους κάτω από τα δέντρα τις μέρες αυτές, γιατί υπάρχει κίνδυνος να πέσουν κλαδιά. Ο δήμος δεν θα είναι υπεύθυνος για ζημιές σε οχήματα που δεν έχουν μετακινηθεί.", "Drivers are asked not to leave their cars under the trees on these days, because there is a danger of falling branches. The municipality will not be responsible for damage to vehicles that have not been moved."),
  L("Εκφωνητής", "m", "Τα κομμένα κλαδιά θα μεταφερθούν στο κέντρο κομποστοποίησης. Οι κάτοικοι που θέλουν δωρεάν κομπόστ για τις γλάστρες και τους κήπους τους μπορούν να το παραλάβουν από εκεί τον επόμενο μήνα.", "The cut branches will be taken to the composting centre. Residents who want free compost for their pots and gardens can collect it from there next month."),
 ],
 "questions": [
  Q("Τι ζητά ο δήμος από τους οδηγούς;", ["Να μην αφήνουν τα αυτοκίνητά τους κάτω από τα δέντρα", "Να οδηγούν αργά", "Να βοηθήσουν στο κλάδεμα", "Να πληρώσουν ένα τέλος"], 0, "Παρακαλούνται οι οδηγοί να μην αφήνουν τα αυτοκίνητά τους κάτω από τα δέντρα"),
  Q("Γιατί;", ["Γιατί θα κλείσουν οι δρόμοι για πάντα", "Γιατί υπάρχει κίνδυνος να πέσουν κλαδιά", "Γιατί θα πλυθούν οι δρόμοι", "Γιατί θα φυτευτούν νέα δέντρα"], 1, "γιατί υπάρχει κίνδυνος να πέσουν κλαδιά"),
  Q("Τι θα γίνει με τα κομμένα κλαδιά;", ["Θα καούν", "Θα πουληθούν για καυσόξυλα", "Θα μεταφερθούν στο κέντρο κομποστοποίησης", "Θα μείνουν στο πεζοδρόμιο"], 2, "Τα κομμένα κλαδιά θα μεταφερθούν στο κέντρο κομποστοποίησης"),
 ],
 "gloss": {"κλάδεμα": "κλάδεμα — pruning", "κατοίκους": "κάτοικος — resident", "κλαδιά": "κλαδί — branch", "υπεύθυνος": "υπεύθυνος — responsible", "ζημιές": "ζημιά — damage", "οχήματα": "όχημα — vehicle", "μετακινηθεί": "μετακινούμαι — to be moved", "κομποστοποίησης": "κομποστοποίηση — composting", "γλάστρες": "γλάστρα — flowerpot"}
})

ITEMS.append({
 "id": "l138-dia-gatokafe", "title": "Ένα καφέ με γάτες", "title_en": "A café with cats", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλες να συζητούν ένα σχέδιο της μίας.",
 "script": [
  L("Ειρήνη", "f", "Θέλω να ανοίξω ένα καφέ με γάτες, σαν αυτά που είδα στην Ιαπωνία. Οι πελάτες πίνουν τον καφέ τους και οι γάτες κυκλοφορούν ελεύθερες ανάμεσα στα τραπέζια.", "I want to open a café with cats, like the ones I saw in Japan. Customers drink their coffee and the cats roam freely between the tables."),
  L("Μαρίνα", "f", "Ωραίο ακούγεται, αλλά σκέψου την υγιεινή. Η κουζίνα δεν μπορεί να είναι στον ίδιο χώρο με τα ζώα. Και τι θα γίνει με όσους έχουν αλλεργία;", "Sounds nice, but think about hygiene. The kitchen can't be in the same space as the animals. And what about people with allergies?"),
  L("Ειρήνη", "f", "Το έχω σκεφτεί. Ο χώρος έχει δύο αίθουσες με γυάλινη πόρτα ανάμεσα. Στη μία θα είναι η κουζίνα και ο πάγκος, και στην άλλη οι γάτες. Και όλες θα είναι αδέσποτες από το καταφύγιο, που θα μπορεί κανείς να τις υιοθετήσει.", "I've thought about it. The place has two rooms with a glass door between them. The kitchen and the counter will be in one, and the cats in the other. And they will all be strays from the shelter, which people will be able to adopt."),
  L("Μαρίνα", "f", "Αυτό μου αρέσει πολύ. Δηλαδή κάθε φορά που κάποιος παίρνει μια γάτα σπίτι, έρχεται μια καινούργια από το καταφύγιο. Μόνο φρόντισε να μη θέλεις να τις κρατήσεις όλες εσύ!", "I really like that. So every time someone takes a cat home, a new one comes from the shelter. Just make sure you don't want to keep them all yourself!"),
 ],
 "questions": [
  Q("Τι ανησυχεί τη Μαρίνα;", ["Το ενοίκιο", "Η υγιεινή και οι πελάτες με αλλεργία", "Ο θόρυβος", "Οι τιμές του καφέ"], 1, "σκέψου την υγιεινή"),
  Q("Πώς θα χωρίζεται ο χώρος;", ["Σε δύο αίθουσες με γυάλινη πόρτα ανάμεσα", "Σε τρεις ορόφους", "Με μια κουρτίνα", "Δεν θα χωρίζεται"], 0, "Ο χώρος έχει δύο αίθουσες με γυάλινη πόρτα ανάμεσα"),
  Q("Από πού θα είναι οι γάτες;", ["Από ένα κατάστημα κατοικίδιων", "Από την Ιαπωνία", "Αδέσποτες από το καταφύγιο, για υιοθεσία", "Δικές της"], 2, "όλες θα είναι αδέσποτες από το καταφύγιο, που θα μπορεί κανείς να τις υιοθετήσει"),
 ],
 "gloss": {"κυκλοφορούν": "κυκλοφορώ — to move around", "υγιεινή": "υγιεινή — hygiene", "αλλεργία": "αλλεργία — allergy", "γυάλινη": "γυάλινος — glass (adj.)", "πάγκος": "πάγκος — counter", "αδέσποτες": "αδέσποτος — stray", "καταφύγιο": "καταφύγιο — shelter", "υιοθετήσει": "υιοθετώ — to adopt"}
})

ITEMS.append({
 "id": "l138-vm-spa", "title": "Η δωροεπιταγή λήγει", "title_en": "The gift voucher is expiring", "type": "voicemail", "level": "B2",
 "context_el": "Πέρυσι σας έκαναν δώρο μια δωροεπιταγή. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλησπέρα σας, από το κέντρο ευεξίας «Θέρμη» σας τηλεφωνώ. Στο σύστημά μας βλέπω ότι έχετε μια δωροεπιταγή για ένα μασάζ και μία είσοδο στη σάουνα, που λήγει στις τριάντα του μήνα.", "Good evening, I'm calling from the 'Thermi' wellness centre. In our system I see that you have a gift voucher for a massage and one entry to the sauna, which expires on the thirtieth of the month."),
  L("Υπάλληλος", "f", "Τα Σαββατοκύριακα είμαστε σχεδόν γεμάτοι μέχρι τότε, αλλά τις καθημερινές μετά τις πέντε έχουμε αρκετά ελεύθερα ραντεβού. Αν δεν προλαβαίνετε, μπορούμε να παρατείνουμε τη δωροεπιταγή για δύο μήνες, με μια μικρή χρέωση δέκα ευρώ.", "At weekends we're almost full until then, but on weekdays after five we have quite a few free appointments. If you can't make it, we can extend the voucher for two months, for a small charge of ten euros."),
  L("Υπάλληλος", "f", "Για ραντεβού, καλέστε μας ή κλείστε απευθείας από την ιστοσελίδα, γράφοντας τον κωδικό που υπάρχει στην πίσω πλευρά της κάρτας. Σας ευχαριστώ.", "For an appointment, call us or book directly on the website, entering the code on the back of the card. Thank you."),
 ],
 "questions": [
  Q("Τι περιλαμβάνει η δωροεπιταγή;", ["Ένα μασάζ και μία είσοδο στη σάουνα", "Ένα κούρεμα", "Ένα μήνα γυμναστήριο", "Ένα δείπνο"], 0, "μια δωροεπιταγή για ένα μασάζ και μία είσοδο στη σάουνα"),
  Q("Πότε έχει το κέντρο ελεύθερα ραντεβού;", ["Τα Σαββατοκύριακα το πρωί", "Τις καθημερινές μετά τις πέντε", "Μόνο τη Δευτέρα", "Καθόλου μέχρι το τέλος του μήνα"], 1, "τις καθημερινές μετά τις πέντε έχουμε αρκετά ελεύθερα ραντεβού"),
  Q("Τι μπορεί να γίνει αν δεν προλαβαίνετε;", ["Θα σας επιστρέψουν τα χρήματα", "Η δωροεπιταγή θα χαθεί χωρίς άλλη επιλογή", "Μπορεί να παραταθεί για δύο μήνες με χρέωση δέκα ευρώ", "Μπορείτε να τη δώσετε σε άλλον δωρεάν"], 2, "μπορούμε να παρατείνουμε τη δωροεπιταγή για δύο μήνες, με μια μικρή χρέωση δέκα ευρώ"),
 ],
 "gloss": {"δωροεπιταγή": "δωροεπιταγή — gift voucher", "ευεξίας": "ευεξία — wellness", "μασάζ": "μασάζ — massage", "σάουνα": "σάουνα — sauna", "λήγει": "λήγω — to expire", "προλαβαίνετε": "προλαβαίνω — to manage in time", "παρατείνουμε": "παρατείνω — to extend", "χρέωση": "χρέωση — charge", "απευθείας": "απευθείας — directly"}
})

ITEMS.append({
 "id": "l138-int-daneistiki", "title": "Δανείζουμε τρυπάνια, όχι βιβλία", "title_en": "We lend drills, not books", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια εκπομπή για τη ζωή στη γειτονιά.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς είναι η «δανειστική αποθήκη» που ανοίξατε;", "What exactly is the 'lending store' that you opened?"),
  L("Υπεύθυνη", "f", "Μοιάζει με βιβλιοθήκη, μόνο που αντί για βιβλία δανείζουμε πράγματα που οι περισσότεροι χρησιμοποιούν δυο φορές τον χρόνο: τρυπάνια, σκάλες, σκηνές για κάμπινγκ, μια ραπτομηχανή, ακόμα και μια μηχανή για παγωτό.", "It's like a library, except that instead of books we lend things most people use twice a year: drills, ladders, camping tents, a sewing machine, even an ice-cream maker."),
  L("Δημοσιογράφος", "m", "Και πώς λειτουργεί;", "And how does it work?"),
  L("Υπεύθυνη", "f", "Τα μέλη πληρώνουν είκοσι ευρώ τον χρόνο και κρατούν κάθε αντικείμενο έως μία εβδομάδα. Τα περισσότερα πράγματα μάς τα χάρισαν οι ίδιοι οι γείτονες. Το πιο δημοφιλές είναι, παραδόξως, η σκάλα: όλοι κάποια στιγμή πρέπει να αλλάξουν μια λάμπα στο ταβάνι.", "Members pay twenty euros a year and keep each item for up to a week. Most of the things were donated by the neighbours themselves. The most popular, surprisingly, is the ladder: everyone at some point has to change a bulb in the ceiling."),
 ],
 "questions": [
  Q("Τι δανείζει η «δανειστική αποθήκη»;", ["Βιβλία και περιοδικά", "Πράγματα που οι περισσότεροι χρησιμοποιούν σπάνια", "Χρήματα", "Ρούχα για γάμους"], 1, "δανείζουμε πράγματα που οι περισσότεροι χρησιμοποιούν δυο φορές τον χρόνο"),
  Q("Από πού προέρχονται τα περισσότερα αντικείμενα;", ["Τα χάρισαν οι γείτονες", "Τα αγόρασε ο δήμος", "Τα έδωσε ένα κατάστημα", "Τα έφτιαξαν οι ίδιοι"], 0, "Τα περισσότερα πράγματα μάς τα χάρισαν οι ίδιοι οι γείτονες"),
  Q("Ποιο είναι το πιο δημοφιλές αντικείμενο;", ["Το τρυπάνι", "Η ραπτομηχανή", "Η σκάλα", "Η μηχανή για παγωτό"], 2, "Το πιο δημοφιλές είναι, παραδόξως, η σκάλα"),
 ],
 "gloss": {"δανειστική": "δανειστικός — lending", "αποθήκη": "αποθήκη — storeroom", "δανείζουμε": "δανείζω — to lend", "τρυπάνια": "τρυπάνι — drill", "σκηνές": "σκηνή — tent", "ραπτομηχανή": "ραπτομηχανή — sewing machine", "χάρισαν": "χαρίζω — to give away", "δημοφιλές": "δημοφιλής — popular", "παραδόξως": "παραδόξως — surprisingly", "ταβάνι": "ταβάνι — ceiling"}
})

ITEMS.append({
 "id": "l138-c1-mpemba", "title": "Παγώνει πιο γρήγορα το ζεστό νερό;", "title_en": "Does hot water freeze faster?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκλαϊκευτική ομιλία για τη φυσική.",
 "script": [
  L("Ομιλήτρια", "f", "Το 1963 ένας μαθητής στην Τανζανία, ο Εράστο Μπέμπα, έφτιαχνε παγωτό στο σχολείο. Βιαζόταν και έβαλε το μείγμα του στην κατάψυξη ζεστό, χωρίς να περιμένει να κρυώσει. Προς έκπληξή του, το δικό του πάγωσε πριν από τα μείγματα των συμμαθητών του, που είχαν μπει κρύα.", "In 1963 a schoolboy in Tanzania, Erasto Mpemba, was making ice cream at school. He was in a hurry and put his mixture in the freezer hot, without waiting for it to cool. To his surprise, his froze before his classmates' mixtures, which had gone in cold."),
  L("Ομιλήτρια", "f", "Ο καθηγητής του τον κορόιδεψε, αλλά ο Μπέμπα δεν το έβαλε κάτω. Λίγα χρόνια αργότερα ρώτησε έναν επισκέπτη φυσικό, τον Ντένις Όσμπορν, ο οποίος έκανε δικά του πειράματα, και το 1969 δημοσίευσαν μαζί ένα άρθρο. Από τότε το φαινόμενο φέρει το όνομα του μαθητή, αν και είχαν περιγράψει κάτι ανάλογο αιώνες νωρίτερα ο Αριστοτέλης, ο Φράνσις Μπέικον και ο Ντεκάρτ.", "His teacher made fun of him, but Mpemba didn't give up. A few years later he asked a visiting physicist, Denis Osborne, who carried out his own experiments, and in 1969 they published an article together. Since then the phenomenon has borne the student's name, although Aristotle, Francis Bacon and Descartes had described something similar centuries earlier."),
  L("Ομιλήτρια", "f", "Το ενδιαφέρον είναι ότι, μισό αιώνα μετά, οι φυσικοί δεν συμφωνούν ακόμα αν το φαινόμενο υπάρχει πραγματικά. Έχουν προταθεί εξηγήσεις, όπως η εξάτμιση, που μειώνει την ποσότητα του ζεστού νερού, ή τα διαλυμένα αέρια. Όμως σε προσεκτικά ελεγχόμενα πειράματα το αποτέλεσμα συχνά δεν επαναλαμβάνεται, και εξαρτάται πολύ από το δοχείο, την κατάψυξη και από το τι ακριβώς ορίζουμε ως «πάγωσε».", "What is interesting is that, half a century later, physicists still do not agree whether the phenomenon really exists. Explanations have been proposed, such as evaporation, which reduces the amount of hot water, or dissolved gases. But in carefully controlled experiments the result often isn't repeated, and it depends a great deal on the container, the freezer and on exactly what we define as 'frozen'."),
  L("Ομιλήτρια", "f", "Γι' αυτό η ιστορία του Μπέμπα διδάσκεται σήμερα όχι ως απόδειξη ενός νόμου της φύσης, αλλά ως μάθημα επιστημονικής στάσης: να παίρνεις στα σοβαρά μια απρόσμενη παρατήρηση, ακόμα κι αν προέρχεται από έναν μαθητή, και ύστερα να την ελέγχεις αυστηρά.", "That is why Mpemba's story is taught today not as proof of a law of nature, but as a lesson in scientific attitude: to take an unexpected observation seriously, even if it comes from a schoolboy, and then to test it rigorously."),
 ],
 "questions": [
  Q("Τι παρατήρησε ο Μπέμπα το 1963;", ["Ότι το κρύο μείγμα πάγωσε πρώτο", "Ότι το δικό του ζεστό μείγμα πάγωσε πριν από τα κρύα", "Ότι η κατάψυξη του σχολείου ήταν χαλασμένη", "Ότι το παγωτό δεν παγώνει με ζάχαρη"], 1, "το δικό του πάγωσε πριν από τα μείγματα των συμμαθητών του, που είχαν μπει κρύα"),
  Q("Πώς αντέδρασε αρχικά ο καθηγητής του;", ["Τον κορόιδεψε", "Τον βράβευσε", "Έγραψε ένα άρθρο", "Ειδοποίησε έναν φυσικό"], 0, "Ο καθηγητής του τον κορόιδεψε"),
  Q("Τι ισχύει σήμερα για το φαινόμενο, σύμφωνα με την ομιλήτρια;", ["Έχει αποδειχθεί οριστικά", "Έχει απορριφθεί οριστικά", "Οι φυσικοί δεν συμφωνούν ακόμα αν υπάρχει πραγματικά", "Το εξήγησε πλήρως ο Αριστοτέλης"], 2, "οι φυσικοί δεν συμφωνούν ακόμα αν το φαινόμενο υπάρχει πραγματικά"),
  Q("Ως τι διδάσκεται σήμερα η ιστορία του Μπέμπα;", ["Ως συνταγή για παγωτό", "Ως απόδειξη ενός νόμου της φύσης", "Ως παράδειγμα κακής επιστήμης", "Ως μάθημα επιστημονικής στάσης"], 3, "ως μάθημα επιστημονικής στάσης"),
 ],
 "gloss": {"εκλαϊκευτική": "εκλαϊκευτικός — popular-science", "μείγμα": "μείγμα — mixture", "κατάψυξη": "κατάψυξη — freezer", "κορόιδεψε": "κοροϊδεύω — to make fun of", "δεν το έβαλε κάτω": "δεν το βάζω κάτω — not to give up", "πειράματα": "πείραμα — experiment", "φέρει": "φέρω — to bear (a name)", "εξάτμιση": "εξάτμιση — evaporation", "διαλυμένα": "διαλυμένος — dissolved", "δοχείο": "δοχείο — container", "απρόσμενη": "απρόσμενος — unexpected", "αυστηρά": "αυστηρά — rigorously"}
})

ITEMS.append({
 "id": "l138-c1-metatopisi", "title": "Τι θεωρούμε «φυσιολογικό» στη θάλασσα", "title_en": "What we consider 'normal' in the sea", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια θαλάσσια βιολόγο.",
 "script": [
  L("Δημοσιογράφος", "m", "Μιλάτε συχνά για το «σύνδρομο της μετατοπιζόμενης γραμμής αναφοράς». Τι σημαίνει αυτός ο δύσκολος όρος;", "You often talk about 'shifting baseline syndrome'. What does this difficult term mean?"),
  L("Βιολόγος", "f", "Τον πρότεινε το 1995 ο ιχθυολόγος Ντάνιελ Πόλι, σε ένα σύντομο άρθρο για την αλιεία. Παρατήρησε ότι κάθε γενιά επιστημόνων θεωρεί ως φυσιολογική κατάσταση εκείνη που βρήκε όταν ξεκίνησε την καριέρα της. Έτσι, οι μειώσεις των ψαριών μετριούνται κάθε φορά από ένα σημείο ήδη φτωχότερο, και η συνολική απώλεια μένει αόρατη.", "It was proposed in 1995 by the fisheries scientist Daniel Pauly, in a short article on fisheries. He observed that each generation of scientists regards as normal the state it found when it began its career. So the declines in fish are measured each time from a point that is already poorer, and the overall loss stays invisible."),
  L("Δημοσιογράφος", "m", "Δηλαδή ξεχνάμε πώς ήταν η θάλασσα παλιά.", "So we forget what the sea used to be like."),
  L("Βιολόγος", "f", "Ακριβώς, και δεν αφορά μόνο τους επιστήμονες. Ένας ψαράς εβδομήντα χρονών σάς διηγείται ότι στα νιάτα του έπιανε ροφούς τόσο μεγάλους που τους κουβαλούσαν δύο άνθρωποι. Ο εγγονός του, που δεν έχει δει ποτέ τέτοιο ψάρι, θεωρεί έναν ροφό δύο κιλών μεγάλη επιτυχία. Κανείς από τους δύο δεν λέει ψέματα· απλώς ο καθένας μετρά από διαφορετική αφετηρία.", "Exactly, and it doesn't only concern scientists. A seventy-year-old fisherman tells you that in his youth he caught groupers so big that two people carried them. His grandson, who has never seen such a fish, considers a two-kilo grouper a great success. Neither of them is lying; each simply measures from a different starting point."),
  L("Δημοσιογράφος", "m", "Και πώς αντιμετωπίζεται αυτό;", "And how is this dealt with?"),
  L("Βιολόγος", "f", "Ψάχνοντας παλαιότερες πηγές: αρχεία από ιχθυαγορές, ημερολόγια ψαράδων, παλιές φωτογραφίες από αγώνες ψαρέματος, ακόμα και πίνακες ζωγραφικής. Μόνο αν ξέρουμε από πού ξεκινήσαμε μπορούμε να θέσουμε φιλόδοξους στόχους αποκατάστασης, αντί να ικανοποιούμαστε με μια θάλασσα που απλώς δεν χειροτέρεψε άλλο.", "By looking for older sources: records from fish markets, fishermen's diaries, old photographs from fishing competitions, even paintings. Only if we know where we started from can we set ambitious restoration targets, instead of being satisfied with a sea that simply hasn't got any worse."),
 ],
 "questions": [
  Q("Τι παρατήρησε ο Ντάνιελ Πόλι;", ["Ότι τα ψάρια αυξάνονται κάθε χρόνο", "Ότι κάθε γενιά επιστημόνων θεωρεί φυσιολογική την κατάσταση που βρήκε στην αρχή της καριέρας της", "Ότι οι ψαράδες λένε ψέματα για τα ψάρια τους", "Ότι η αλιεία δεν επηρεάζει τη θάλασσα"], 1, "κάθε γενιά επιστημόνων θεωρεί ως φυσιολογική κατάσταση εκείνη που βρήκε όταν ξεκίνησε την καριέρα της"),
  Q("Ποια είναι η συνέπεια αυτού του φαινομένου;", ["Η συνολική απώλεια μένει αόρατη", "Οι επιστήμονες σταματούν να μετρούν", "Τα ψάρια μεγαλώνουν", "Οι ψαράδες αλλάζουν επάγγελμα"], 0, "η συνολική απώλεια μένει αόρατη"),
  Q("Τι δείχνει το παράδειγμα του ψαρά και του εγγονού του;", ["Ότι ο παππούς υπερβάλλει", "Ότι ο εγγονός είναι καλύτερος ψαράς", "Ότι οι ροφοί έχουν εξαφανιστεί εντελώς", "Ότι ο καθένας μετρά από διαφορετική αφετηρία"], 3, "απλώς ο καθένας μετρά από διαφορετική αφετηρία"),
  Q("Γιατί χρειάζονται οι παλαιότερες πηγές, κατά τη βιολόγο;", ["Για να γραφτεί ένα βιβλίο ιστορίας", "Για να τεθούν φιλόδοξοι στόχοι αποκατάστασης", "Για να πουληθούν οι φωτογραφίες", "Για να απαγορευτεί κάθε ψάρεμα"], 1, "μπορούμε να θέσουμε φιλόδοξους στόχους αποκατάστασης"),
 ],
 "gloss": {"θαλάσσια": "θαλάσσιος — marine", "σύνδρομο": "σύνδρομο — syndrome", "μετατοπιζόμενης": "μετατοπίζομαι — to shift", "γραμμής αναφοράς": "γραμμή αναφοράς — baseline", "ιχθυολόγος": "ιχθυολόγος — ichthyologist, fisheries scientist", "αλιεία": "αλιεία — fishing, fisheries", "απώλεια": "απώλεια — loss", "αόρατη": "αόρατος — invisible", "ροφούς": "ροφός — dusky grouper", "αφετηρία": "αφετηρία — starting point", "ιχθυαγορές": "ιχθυαγορά — fish market", "φιλόδοξους": "φιλόδοξος — ambitious", "αποκατάστασης": "αποκατάσταση — restoration"}
})

rnd = random.Random(138)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-138.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
