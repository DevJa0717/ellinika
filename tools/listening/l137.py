# Source for library/listening/listening-137.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l137.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l137-ann-laiki", "title": "Η λαϊκή αγορά αλλάζει δρόμο", "title_en": "The street market moves", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε στο τοπικό ραδιόφωνο μια ανακοίνωση του δήμου.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος ενημερώνει ότι, λόγω έργων αντικατάστασης του αγωγού νερού στην οδό Αγίου Νικολάου, η λαϊκή αγορά της Πέμπτης θα μεταφερθεί προσωρινά, για τέσσερις εβδομάδες, στην οδό Ελευθερίας, δίπλα στο δημοτικό πάρκο.", "The municipality announces that, because of works to replace the water main on Agiou Nikolaou Street, the Thursday street market will move temporarily, for four weeks, to Eleftherias Street, next to the municipal park."),
  L("Εκφωνήτρια", "f", "Η στάθμευση στην οδό Ελευθερίας θα απαγορεύεται κάθε Τετάρτη από τις δέκα το βράδυ έως την Πέμπτη στις τέσσερις το απόγευμα. Τα αυτοκίνητα που δεν θα έχουν μετακινηθεί θα απομακρύνονται με γερανό.", "Parking on Eleftherias Street will be banned every Wednesday from ten at night until Thursday at four in the afternoon. Cars that have not been moved will be towed away."),
  L("Εκφωνήτρια", "f", "Για τους ηλικιωμένους που δυσκολεύονται να περπατήσουν ως το νέο σημείο, ένα δημοτικό μικρό λεωφορείο θα εκτελεί δωρεάν δρομολόγια από την κεντρική πλατεία κάθε μισή ώρα.", "For elderly people who find it hard to walk to the new spot, a small municipal bus will run free trips from the central square every half hour."),
 ],
 "questions": [
  Q("Γιατί μεταφέρεται η λαϊκή αγορά;", ["Γιατί διαμαρτυρήθηκαν οι κάτοικοι", "Λόγω έργων στον αγωγό νερού", "Γιατί ανοίγει ένα καινούργιο πάρκο", "Λόγω μιας γιορτής"], 1, "λόγω έργων αντικατάστασης του αγωγού νερού"),
  Q("Τι θα γίνει με τα αυτοκίνητα που δεν θα έχουν μετακινηθεί;", ["Θα πάρουν μόνο πρόστιμο", "Θα απομακρύνονται με γερανό", "Θα μείνουν εκεί", "Θα τα μετακινήσουν οι πωλητές"], 1, "θα απομακρύνονται με γερανό"),
  Q("Τι θα κάνει το δημοτικό μικρό λεωφορείο;", ["Θα μεταφέρει τους πωλητές", "Θα πηγαίνει μόνο στο πάρκο τα Σαββατοκύριακα", "Θα εκτελεί δωρεάν δρομολόγια από την κεντρική πλατεία κάθε μισή ώρα", "Θα κοστίζει ένα ευρώ"], 2, "ένα δημοτικό μικρό λεωφορείο θα εκτελεί δωρεάν δρομολόγια από την κεντρική πλατεία κάθε μισή ώρα"),
 ],
 "gloss": {"αντικατάστασης": "αντικατάσταση — replacement", "αγωγού": "αγωγός — pipe, main", "μεταφερθεί": "μεταφέρομαι — to be moved", "προσωρινά": "προσωρινά — temporarily", "στάθμευση": "στάθμευση — parking", "απαγορεύεται": "απαγορεύομαι — to be forbidden", "μετακινηθεί": "μετακινούμαι — to be moved", "απομακρύνονται": "απομακρύνομαι — to be removed", "γερανό": "γερανός — tow truck, crane", "εκτελεί δωρεάν δρομολόγια": "εκτελώ δρομολόγια — to run trips (of a bus)"}
})

ITEMS.append({
 "id": "l137-vm-apentomosi", "title": "Απεντόμωση στην πολυκατοικία", "title_en": "Pest control in the building", "type": "voicemail", "level": "B2",
 "context_el": "Μένετε σε μια πολυκατοικία. Ακούτε ένα μήνυμα από τη διαχειρίστρια στον τηλεφωνητή σας.",
 "script": [
  L("Διαχειρίστρια", "f", "Καλησπέρα, η Ρούλα είμαι, η διαχειρίστρια. Σας ενημερώνω ότι την ερχόμενη Τρίτη, στις εννιά το πρωί, θα γίνει απεντόμωση σε όλη την πολυκατοικία, γιατί κάποιοι ένοικοι βρήκαν κατσαρίδες στο υπόγειο και στις σκάλες.", "Good evening, it's Roula, the building manager. I'm letting you know that next Tuesday, at nine in the morning, there will be pest control in the whole building, because some residents found cockroaches in the basement and on the stairs."),
  L("Διαχειρίστρια", "f", "Ο τεχνικός θα ψεκάσει και μέσα στα διαμερίσματα, οπότε θα χρειαστεί να του ανοίξετε. Αν δεν θα είστε σπίτι, αφήστε μου το κλειδί από τη Δευτέρα. Πριν φύγετε, καλύψτε τα τρόφιμα και τα πιάτα, και πάρτε μαζί σας τα κατοικίδια.", "The technician will also spray inside the flats, so you'll need to let him in. If you won't be home, leave me the key from Monday. Before you go, cover food and dishes, and take your pets with you."),
  L("Διαχειρίστρια", "f", "Μετά τον ψεκασμό, καλό είναι να μην μπείτε στο σπίτι για τέσσερις ώρες και να αερίσετε καλά. Το κόστος θα μοιραστεί στα κοινόχρηστα του μήνα. Ευχαριστώ!", "After the spraying, it's best not to go into the flat for four hours and to air it well. The cost will be shared in this month's building charges. Thank you!"),
 ],
 "questions": [
  Q("Γιατί θα γίνει απεντόμωση;", ["Γιατί το ζητά ο νόμος κάθε χρόνο", "Γιατί κάποιοι ένοικοι βρήκαν κατσαρίδες", "Γιατί ήρθαν ποντίκια από το πάρκο", "Γιατί ανακαινίζεται το υπόγειο"], 1, "γιατί κάποιοι ένοικοι βρήκαν κατσαρίδες στο υπόγειο και στις σκάλες"),
  Q("Τι πρέπει να κάνετε, αν δεν θα είστε σπίτι;", ["Να αφήσετε το κλειδί στη διαχειρίστρια", "Να αφήσετε την πόρτα ανοιχτή", "Να αλλάξετε μέρα", "Τίποτα"], 0, "αφήστε μου το κλειδί από τη Δευτέρα"),
  Q("Πόση ώρα δεν πρέπει να μπείτε στο σπίτι μετά τον ψεκασμό;", ["Μία ώρα", "Όλη τη μέρα", "Τέσσερις ώρες", "Δύο μέρες"], 2, "να μην μπείτε στο σπίτι για τέσσερις ώρες"),
 ],
 "gloss": {"απεντόμωση": "απεντόμωση — pest control (insects)", "διαχειρίστρια": "διαχειρίστρια — building manager (woman)", "ένοικοι": "ένοικος — resident, tenant", "κατσαρίδες": "κατσαρίδα — cockroach", "ψεκάσει": "ψεκάζω — to spray", "τρόφιμα": "τρόφιμα — food", "κατοικίδια": "κατοικίδιο — pet", "ψεκασμό": "ψεκασμός — spraying", "αερίσετε": "αερίζω — to air", "κοινόχρηστα": "κοινόχρηστα — shared building charges"}
})

ITEMS.append({
 "id": "l137-dia-koino-aftokinito", "title": "Ένα αυτοκίνητο για τρεις οικογένειες", "title_en": "One car for three families", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο γείτονες να συζητούν στη σκάλα της πολυκατοικίας.",
 "script": [
  L("Ηλίας", "m", "Σκεφτόμαστε να πουλήσουμε το αυτοκίνητο. Το χρησιμοποιούμε μόνο τα Σαββατοκύριακα, και πληρώνουμε ασφάλεια, τέλη κυκλοφορίας και πάρκινγκ όλο τον χρόνο.", "We're thinking of selling the car. We only use it at weekends, and we pay insurance, road tax and parking all year round."),
  L("Κατερίνα", "f", "Κι εμείς το ίδιο. Τι λες να αγοράσουμε ένα μαζί, μαζί και με τον Παύλο από τον τρίτο; Θα μοιραζόμαστε όλα τα έξοδα στα τρία.", "Same with us. What do you say we buy one together, along with Pavlos from the third floor? We'd split all the costs three ways."),
  L("Ηλίας", "m", "Ακούγεται καλό, αλλά τι θα γίνει αν το θέλουμε όλοι την ίδια μέρα; Ή αν κάποιος κάνει μια γρατζουνιά;", "Sounds good, but what happens if we all want it on the same day? Or if someone makes a scratch?"),
  L("Κατερίνα", "f", "Μια φίλη μου το κάνει ήδη. Έχουν ένα κοινό ημερολόγιο στο κινητό, όπου κλείνει ο καθένας τις μέρες του, και έχουν γράψει σε ένα χαρτί κανόνες για τις ζημιές και τη βενζίνη. Λέει ότι σε δύο χρόνια δεν έχουν μαλώσει ούτε μία φορά.", "A friend of mine already does it. They have a shared calendar on their phones where each person books their days, and they've written rules on paper for damage and petrol. She says that in two years they haven't argued once."),
 ],
 "questions": [
  Q("Γιατί σκέφτεται ο Ηλίας να πουλήσει το αυτοκίνητο;", ["Γιατί είναι πολύ παλιό", "Γιατί το χρησιμοποιούν μόνο τα Σαββατοκύριακα αλλά πληρώνουν έξοδα όλο τον χρόνο", "Γιατί μετακομίζουν", "Γιατί δεν βρίσκουν πάρκινγκ"], 1, "Το χρησιμοποιούμε μόνο τα Σαββατοκύριακα, και πληρώνουμε ασφάλεια, τέλη κυκλοφορίας και πάρκινγκ όλο τον χρόνο"),
  Q("Τι προτείνει η Κατερίνα;", ["Να νοικιάζουν αυτοκίνητο", "Να αγοράσουν ποδήλατα", "Να αγοράσουν ένα αυτοκίνητο μαζί με τον Παύλο και να μοιράζονται τα έξοδα", "Να παίρνουν ταξί"], 2, "Τι λες να αγοράσουμε ένα μαζί, μαζί και με τον Παύλο από τον τρίτο"),
  Q("Πώς οργανώνεται η φίλη της Κατερίνας;", ["Με ένα κοινό ημερολόγιο στο κινητό και γραπτούς κανόνες", "Ο καθένας παίρνει το αυτοκίνητο μία εβδομάδα τον μήνα", "Αποφασίζουν με κλήρωση", "Δεν έχουν κανόνες"], 0, "Έχουν ένα κοινό ημερολόγιο στο κινητό"),
 ],
 "gloss": {"ασφάλεια": "ασφάλεια — insurance", "τέλη κυκλοφορίας": "τέλη κυκλοφορίας — road tax", "μοιραζόμαστε": "μοιράζομαι — to share", "έξοδα": "έξοδα — expenses", "γρατζουνιά": "γρατζουνιά — scratch", "ημερολόγιο": "ημερολόγιο — calendar", "ζημιές": "ζημιά — damage", "μαλώσει": "μαλώνω — to argue, quarrel"}
})

ITEMS.append({
 "id": "l137-int-skylos-diasosis", "title": "Με τον σκύλο της στα χαλάσματα", "title_en": "With her dog in the rubble", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από συνέντευξη με μια εθελόντρια διασώστρια.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνει ένας σκύλος διάσωσης;", "What exactly does a rescue dog do?"),
  L("Διασώστρια", "f", "Ψάχνει ανθρώπους με τη μύτη του: χαμένους πεζοπόρους στο βουνό ή ανθρώπους παγιδευμένους κάτω από χαλάσματα μετά από σεισμό. Ένας σκύλος μπορεί να ψάξει σε μισή ώρα μια περιοχή για την οποία δέκα άνθρωποι θα χρειάζονταν μια ολόκληρη μέρα. Όταν βρει κάποιον, γαβγίζει και δεν φεύγει από το σημείο.", "It searches for people with its nose: lost hikers in the mountains or people trapped under rubble after an earthquake. A dog can search in half an hour an area for which ten people would need a whole day. When it finds someone, it barks and doesn't leave the spot."),
  L("Δημοσιογράφος", "m", "Πόσο κρατά η εκπαίδευση;", "How long does the training take?"),
  L("Διασώστρια", "f", "Περίπου δύο χρόνια, και γίνεται σαν παιχνίδι. Στην αρχή κρύβεται κάποιος με το αγαπημένο παιχνίδι του σκύλου, και ο σκύλος μαθαίνει ότι, αν τον βρει, θα παίξουν. Η Λούνα μου έχει πάρει μέρος σε δεκαπέντε επιχειρήσεις. Η πιο συγκινητική ήταν όταν βρήκε έναν ηλικιωμένο που είχε χαθεί σε ένα φαράγγι, ζωντανό, μετά από δύο νύχτες.", "About two years, and it's done like a game. At first someone hides with the dog's favourite toy, and the dog learns that if it finds them, they'll play. My Luna has taken part in fifteen operations. The most moving was when she found an elderly man who had got lost in a gorge, alive, after two nights."),
 ],
 "questions": [
  Q("Τι κάνει ο σκύλος, όταν βρει κάποιον;", ["Επιστρέφει στη διασώστρια", "Γαβγίζει και δεν φεύγει από το σημείο", "Σκάβει μόνος του", "Φέρνει ένα αντικείμενο"], 1, "γαβγίζει και δεν φεύγει από το σημείο"),
  Q("Πώς γίνεται η εκπαίδευση;", ["Με αυστηρές τιμωρίες", "Σαν παιχνίδι, με το αγαπημένο παιχνίδι του σκύλου", "Μόνο με λιχουδιές", "Σε στρατιωτική σχολή"], 1, "γίνεται σαν παιχνίδι"),
  Q("Ποια ήταν η πιο συγκινητική επιχείρηση της Λούνας;", ["Όταν βρήκε έναν ηλικιωμένο ζωντανό σε ένα φαράγγι μετά από δύο νύχτες", "Όταν βρήκε ένα παιδί σε ένα δάσος", "Μετά από έναν σεισμό στο εξωτερικό", "Όταν βρήκε έναν ψαρά στη θάλασσα"], 0, "βρήκε έναν ηλικιωμένο που είχε χαθεί σε ένα φαράγγι, ζωντανό, μετά από δύο νύχτες"),
 ],
 "gloss": {"χαλάσματα": "χαλάσματα — rubble, ruins", "διασώστρια": "διασώστρια — rescuer (woman)", "διάσωσης": "διάσωση — rescue", "πεζοπόρους": "πεζοπόρος — hiker", "παγιδευμένους": "παγιδευμένος — trapped", "γαβγίζει": "γαβγίζω — to bark", "εκπαίδευση": "εκπαίδευση — training", "επιχειρήσεις": "επιχείρηση — operation (rescue)", "συγκινητική": "συγκινητικός — moving", "φαράγγι": "φαράγγι — gorge"}
})

ITEMS.append({
 "id": "l137-int-kiniti-vivliothiki", "title": "Μια βιβλιοθήκη σε τέσσερις ρόδες", "title_en": "A library on four wheels", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από ρεπορτάζ για τα ορεινά χωριά.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς λειτουργεί η κινητή βιβλιοθήκη;", "How does the mobile library work?"),
  L("Βιβλιοθηκάριος", "m", "Είναι ένα φορτηγάκι με ράφια, που χωράει περίπου δύο χιλιάδες βιβλία. Κάθε εβδομάδα επισκεπτόμαστε δεκαοχτώ χωριά. Σταματάμε στην πλατεία, συνήθως έξω από το καφενείο, και οι κάτοικοι έρχονται να επιστρέψουν τα βιβλία που δανείστηκαν και να πάρουν καινούργια.", "It's a small van with shelves that holds about two thousand books. Every week we visit eighteen villages. We stop in the square, usually outside the café, and residents come to return the books they borrowed and take new ones."),
  L("Δημοσιογράφος", "f", "Ποιοι είναι οι πιο τακτικοί αναγνώστες;", "Who are the most regular readers?"),
  L("Βιβλιοθηκάριος", "m", "Οι ηλικιωμένες κυρίες, χωρίς αμφιβολία. Τους αρέσουν τα ιστορικά μυθιστορήματα και τα βιβλία με μεγάλα γράμματα. Αλλά και τα παιδιά του χωριού, που δεν έχουν βιβλιοπωλείο σε απόσταση σαράντα χιλιομέτρων. Τον χειμώνα, όταν χιονίζει, δεν μπορούμε να ανέβουμε σε μερικά χωριά, οπότε στέλνουμε τα βιβλία με τον ταχυδρόμο.", "Elderly ladies, without a doubt. They like historical novels and large-print books. But also the village children, who don't have a bookshop within forty kilometres. In winter, when it snows, we can't get up to some villages, so we send the books with the postman."),
 ],
 "questions": [
  Q("Πού σταματά συνήθως η κινητή βιβλιοθήκη;", ["Έξω από το σχολείο", "Στην πλατεία, έξω από το καφενείο", "Στην εκκλησία", "Στο δημαρχείο"], 1, "Σταματάμε στην πλατεία, συνήθως έξω από το καφενείο"),
  Q("Τι αρέσει στις ηλικιωμένες κυρίες;", ["Τα περιοδικά μόδας", "Τα βιβλία μαγειρικής", "Τα ιστορικά μυθιστορήματα και τα βιβλία με μεγάλα γράμματα", "Τα αστυνομικά"], 2, "Τους αρέσουν τα ιστορικά μυθιστορήματα και τα βιβλία με μεγάλα γράμματα"),
  Q("Τι κάνουν τον χειμώνα, όταν χιονίζει;", ["Στέλνουν τα βιβλία με τον ταχυδρόμο", "Σταματούν τη λειτουργία", "Πηγαίνουν με τα πόδια", "Ανοίγουν ηλεκτρονική βιβλιοθήκη"], 0, "στέλνουμε τα βιβλία με τον ταχυδρόμο"),
 ],
 "gloss": {"κινητή": "κινητός — mobile", "φορτηγάκι": "φορτηγάκι — small van", "ράφια": "ράφι — shelf", "χωράει": "χωράω — to hold, fit", "δανείστηκαν": "δανείζομαι — to borrow", "τακτικοί": "τακτικός — regular", "μυθιστορήματα": "μυθιστόρημα — novel", "απόσταση": "απόσταση — distance", "ταχυδρόμο": "ταχυδρόμος — postman"}
})

ITEMS.append({
 "id": "l137-vm-mikroviologiko", "title": "Το ραντεβού για τις εξετάσεις αίματος", "title_en": "The blood-test appointment", "type": "voicemail", "level": "B2",
 "context_el": "Κλείσατε ραντεβού για εξετάσεις αίματος. Ακούτε ένα μήνυμα από το μικροβιολογικό εργαστήριο στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, από το μικροβιολογικό εργαστήριο «Υγεία». Σας υπενθυμίζουμε το ραντεβού σας για αιμοληψία αύριο, Πέμπτη, στις οχτώ και μισή το πρωί.", "Good morning, from the 'Health' microbiology lab. We're reminding you of your appointment for a blood test tomorrow, Thursday, at half past eight in the morning."),
  L("Υπάλληλος", "f", "Επειδή ο γιατρός σας ζήτησε σάκχαρο και χοληστερίνη, πρέπει να έρθετε νηστικός. Μην φάτε τίποτα μετά τις οχτώ το βράδυ. Νερό μπορείτε να πιείτε, αλλά όχι καφέ. Φέρτε μαζί το παραπεμπτικό και την ταυτότητά σας.", "Because your doctor asked for blood sugar and cholesterol, you need to come fasting. Don't eat anything after eight in the evening. You may drink water, but not coffee. Bring the referral and your ID with you."),
  L("Υπάλληλος", "f", "Τα αποτελέσματα θα σας σταλούν με ηλεκτρονικό ταχυδρομείο μέσα σε δύο εργάσιμες μέρες. Αν δεν μπορείτε να έρθετε, παρακαλούμε ενημερώστε μας από σήμερα, για να δώσουμε τη θέση σε άλλον. Ευχαριστούμε.", "The results will be sent to you by email within two working days. If you can't come, please let us know today, so we can give the slot to someone else. Thank you."),
 ],
 "questions": [
  Q("Γιατί πρέπει να έρθετε νηστικός;", ["Γιατί θα κάνετε και αξονική", "Γιατί ο γιατρός ζήτησε σάκχαρο και χοληστερίνη", "Γιατί το εργαστήριο το ζητά πάντα", "Γιατί η εξέταση θα κρατήσει πολύ"], 1, "Επειδή ο γιατρός σας ζήτησε σάκχαρο και χοληστερίνη, πρέπει να έρθετε νηστικός"),
  Q("Τι μπορείτε να πιείτε πριν από την εξέταση;", ["Καφέ χωρίς ζάχαρη", "Χυμό", "Νερό", "Τίποτα απολύτως"], 2, "Νερό μπορείτε να πιείτε, αλλά όχι καφέ"),
  Q("Πώς θα πάρετε τα αποτελέσματα;", ["Με ηλεκτρονικό ταχυδρομείο μέσα σε δύο εργάσιμες μέρες", "Θα τα πάρετε την ίδια μέρα στο εργαστήριο", "Θα τα στείλουν στον γιατρό σας με φαξ", "Με το ταχυδρομείο σε μία εβδομάδα"], 0, "Τα αποτελέσματα θα σας σταλούν με ηλεκτρονικό ταχυδρομείο μέσα σε δύο εργάσιμες μέρες"),
 ],
 "gloss": {"μικροβιολογικό εργαστήριο": "μικροβιολογικό εργαστήριο — medical (diagnostic) laboratory", "υπενθυμίζουμε": "υπενθυμίζω — to remind", "αιμοληψία": "αιμοληψία — blood sampling", "σάκχαρο": "σάκχαρο — blood sugar", "χοληστερίνη": "χοληστερίνη — cholesterol", "νηστικός": "νηστικός — fasting, on an empty stomach", "παραπεμπτικό": "παραπεμπτικό — (doctor's) referral", "αποτελέσματα": "αποτέλεσμα — result", "εργάσιμες": "εργάσιμος — working (day)"}
})

ITEMS.append({
 "id": "l137-dia-anoixto-grafeio", "title": "Θόρυβος στο ανοιχτό γραφείο", "title_en": "Noise in the open-plan office", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο συναδέλφους να συζητούν στο διάλειμμα.",
 "script": [
  L("Σοφία", "f", "Από τότε που γκρέμισαν τους τοίχους και μας έβαλαν όλους σε έναν χώρο, δεν μπορώ να συγκεντρωθώ. Ο ένας μιλάει στο τηλέφωνο, ο άλλος τρώει πατατάκια, ο τρίτος έχει συνέχεια τηλεδιάσκεψη.", "Since they knocked down the walls and put us all in one space, I can't concentrate. One person talks on the phone, another eats crisps, a third is always on a video call."),
  L("Γιάννης", "m", "Εμένα μου αρέσει, η αλήθεια είναι. Μιλάμε περισσότερο, λύνουμε γρηγορότερα τα προβλήματα. Πριν, για να ρωτήσω κάτι τον Στέφανο, έπρεπε να του στείλω μέιλ.", "Honestly, I like it. We talk more, we solve problems faster. Before, to ask Stefanos something, I had to send him an email."),
  L("Σοφία", "f", "Ναι, αλλά εγώ γράφω αναφορές. Χρειάζομαι ησυχία. Χθες φόρεσα ακουστικά όλη μέρα και στο τέλος με πονούσε το κεφάλι.", "Yes, but I write reports. I need quiet. Yesterday I wore headphones all day and by the end my head hurt."),
  L("Γιάννης", "m", "Γιατί δεν ζητάς να χρησιμοποιείς την αίθουσα συσκέψεων τα πρωινά; Συνήθως είναι άδεια μέχρι τις δώδεκα. Ή να προτείνουμε στον διευθυντή μια «ζώνη ησυχίας» στη γωνία, όπου δεν θα επιτρέπονται τα τηλέφωνα.", "Why don't you ask to use the meeting room in the mornings? It's usually empty until twelve. Or we could suggest to the manager a 'quiet zone' in the corner, where phones won't be allowed."),
 ],
 "questions": [
  Q("Τι ενοχλεί τη Σοφία;", ["Ο κλιματισμός", "Ο θόρυβος στον κοινό χώρο", "Το πολύ φως", "Ο νέος διευθυντής"], 1, "δεν μπορώ να συγκεντρωθώ"),
  Q("Τι θετικό βλέπει ο Γιάννης;", ["Ότι έχουν περισσότερο χώρο", "Ότι μπορεί να φοράει ακουστικά", "Ότι μιλάνε περισσότερο και λύνουν γρηγορότερα τα προβλήματα", "Ότι δεν χρειάζεται να πηγαίνει σε συσκέψεις"], 2, "Μιλάμε περισσότερο, λύνουμε γρηγορότερα τα προβλήματα"),
  Q("Τι της προτείνει ο Γιάννης;", ["Να χρησιμοποιεί την αίθουσα συσκέψεων τα πρωινά ή να ζητήσουν μια «ζώνη ησυχίας»", "Να δουλεύει από το σπίτι", "Να αλλάξει θέση με τον Στέφανο", "Να μιλήσει στους συναδέλφους με θυμό"], 0, "Γιατί δεν ζητάς να χρησιμοποιείς την αίθουσα συσκέψεων τα πρωινά"),
 ],
 "gloss": {"γκρέμισαν": "γκρεμίζω — to knock down", "συγκεντρωθώ": "συγκεντρώνομαι — to concentrate", "τηλεδιάσκεψη": "τηλεδιάσκεψη — video call", "αναφορές": "αναφορά — report", "ακουστικά": "ακουστικά — headphones", "αίθουσα συσκέψεων": "αίθουσα συσκέψεων — meeting room", "ζώνη ησυχίας": "ζώνη ησυχίας — quiet zone", "επιτρέπονται": "επιτρέπομαι — to be allowed"}
})

ITEMS.append({
 "id": "l137-news-tiganelaio", "title": "Κάδοι για το τηγανέλαιο", "title_en": "Bins for used cooking oil", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις τοπικές ειδήσεις.",
 "script": [
  L("Ρεπόρτερ", "m", "Από τη Δευτέρα, σε είκοσι σημεία της πόλης, έξω από σούπερ μάρκετ και σχολεία, τοποθετούνται ειδικοί κάδοι για το χρησιμοποιημένο μαγειρικό λάδι.", "From Monday, at twenty points around the town, outside supermarkets and schools, special bins for used cooking oil are being installed."),
  L("Ρεπόρτερ", "m", "Οι κάτοικοι καλούνται να μαζεύουν το λάδι από το τηγάνι σε ένα πλαστικό μπουκάλι, να το κλείνουν καλά και να το ρίχνουν στον κάδο. Το λάδι που καταλήγει στον νεροχύτη φράζει τους σωλήνες και ρυπαίνει τη θάλασσα· σύμφωνα με τον δήμο, ένα λίτρο λάδι μπορεί να μολύνει τεράστιες ποσότητες νερού.", "Residents are asked to collect the oil from the frying pan in a plastic bottle, close it well and drop it in the bin. Oil that ends up in the sink blocks the pipes and pollutes the sea; according to the municipality, one litre of oil can contaminate huge quantities of water."),
  L("Ρεπόρτερ", "m", "Το λάδι που θα συλλέγεται θα πηγαίνει σε εργοστάσιο, όπου θα γίνεται βιοντίζελ. Τα σχολεία που θα μαζέψουν τις περισσότερες ποσότητες ως το καλοκαίρι θα κερδίσουν εξοπλισμό για τα εργαστήριά τους.", "The oil collected will go to a factory, where it will be turned into biodiesel. The schools that collect the largest quantities by summer will win equipment for their labs."),
 ],
 "questions": [
  Q("Τι πρέπει να κάνουν οι κάτοικοι με το λάδι;", ["Να το ρίχνουν στον νεροχύτη με ζεστό νερό", "Να το μαζεύουν σε πλαστικό μπουκάλι και να το ρίχνουν στον κάδο", "Να το πηγαίνουν στο δημαρχείο", "Να το ξαναχρησιμοποιούν"], 1, "να μαζεύουν το λάδι από το τηγάνι σε ένα πλαστικό μπουκάλι, να το κλείνουν καλά και να το ρίχνουν στον κάδο"),
  Q("Τι θα γίνεται το λάδι που θα συλλέγεται;", ["Σαπούνι", "Λίπασμα", "Βιοντίζελ", "Ζωοτροφή"], 2, "όπου θα γίνεται βιοντίζελ"),
  Q("Τι θα κερδίσουν τα σχολεία που θα μαζέψουν τις περισσότερες ποσότητες;", ["Εξοπλισμό για τα εργαστήριά τους", "Μια εκδρομή", "Χρήματα για τους μαθητές", "Βιβλία για τη βιβλιοθήκη"], 0, "θα κερδίσουν εξοπλισμό για τα εργαστήριά τους"),
 ],
 "gloss": {"κάδοι": "κάδος — bin", "τοποθετούνται": "τοποθετούμαι — to be placed, installed", "τηγάνι": "τηγάνι — frying pan", "νεροχύτη": "νεροχύτης — (kitchen) sink", "φράζει": "φράζω — to block", "σωλήνες": "σωλήνας — pipe", "ρυπαίνει": "ρυπαίνω — to pollute", "μολύνει": "μολύνω — to contaminate", "συλλέγεται": "συλλέγομαι — to be collected", "βιοντίζελ": "βιοντίζελ — biodiesel", "εξοπλισμό": "εξοπλισμός — equipment"}
})

ITEMS.append({
 "id": "l137-c1-overview", "title": "Η Γη από ψηλά: το «φαινόμενο της επισκόπησης»", "title_en": "Earth from above: the overview effect", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ένα ντοκιμαντέρ για την εξερεύνηση του διαστήματος.",
 "script": [
  L("Αφηγήτρια", "f", "Την παραμονή των Χριστουγέννων του 1968, το διαστημόπλοιο «Απόλλων 8» έκανε τον γύρο της Σελήνης. Ξαφνικά, πάνω από τον γκρίζο ορίζοντά της, εμφανίστηκε η Γη, μια μικρή γαλάζια σφαίρα μέσα στο μαύρο κενό. Ο αστροναύτης Γουίλιαμ Άντερς τη φωτογράφισε, και η εικόνα, γνωστή ως «Ανατολή της Γης», έγινε μία από τις πιο διάσημες φωτογραφίες του εικοστού αιώνα.", "On Christmas Eve 1968, the Apollo 8 spacecraft was orbiting the Moon. Suddenly, above its grey horizon, the Earth appeared, a small blue sphere in the black void. The astronaut William Anders photographed it, and the image, known as 'Earthrise', became one of the most famous photographs of the twentieth century."),
  L("Αφηγήτρια", "f", "Πολλοί αστροναύτες περιγράφουν μια παρόμοια εμπειρία: βλέποντας τον πλανήτη από ψηλά, χωρίς σύνορα, με μια ατμόσφαιρα τόσο λεπτή που μοιάζει με στρώμα βερνικιού, νιώθουν ξαφνικά πόσο εύθραυστος είναι και πόσο ενωμένη είναι η ανθρωπότητα. Το 1987 ο συγγραφέας Φρανκ Γουάιτ ονόμασε αυτή τη γνωστική μεταστροφή «φαινόμενο της επισκόπησης».", "Many astronauts describe a similar experience: seeing the planet from above, without borders, with an atmosphere so thin it looks like a layer of varnish, they suddenly feel how fragile it is and how united humanity is. In 1987 the writer Frank White named this cognitive shift the 'overview effect'."),
  L("Αφηγήτρια", "f", "Για ορισμένους, η εμπειρία δεν είναι μόνο δέος, αλλά και θλίψη ή ανησυχία για την τύχη του πλανήτη. Ψυχολόγοι μελετούν σήμερα αν κάτι ανάλογο μπορεί να προκληθεί και στη Γη, με εικονική πραγματικότητα, ώστε να ευαισθητοποιηθούν περισσότεροι άνθρωποι για το περιβάλλον.", "For some, the experience is not only awe but also sadness or worry about the planet's fate. Psychologists are now studying whether something similar can be induced on Earth, with virtual reality, so that more people become aware of the environment."),
  L("Αφηγήτρια", "f", "Τα αποτελέσματα, προς το παρόν, είναι αντιφατικά. Ίσως, όπως λένε κάποιοι αστροναύτες, τίποτα δεν αντικαθιστά τη στιγμή που βλέπεις με τα μάτια σου ότι όλα όσα γνωρίζεις χωρούν σε μια κουκκίδα.", "The results, for now, are mixed. Perhaps, as some astronauts say, nothing replaces the moment when you see with your own eyes that everything you know fits into a dot."),
 ],
 "questions": [
  Q("Τι έδειχνε η φωτογραφία «Ανατολή της Γης»;", ["Την επιφάνεια της Σελήνης από κοντά", "Τη Γη να εμφανίζεται πάνω από τον ορίζοντα της Σελήνης", "Τον Ήλιο πίσω από τη Γη", "Τους αστροναύτες μέσα στο διαστημόπλοιο"], 1, "πάνω από τον γκρίζο ορίζοντά της, εμφανίστηκε η Γη"),
  Q("Τι νιώθουν πολλοί αστροναύτες βλέποντας τη Γη από ψηλά;", ["Φόβο για το ταξίδι της επιστροφής", "Υπερηφάνεια για τη χώρα τους", "Πόσο εύθραυστος είναι ο πλανήτης και πόσο ενωμένη είναι η ανθρωπότητα", "Ανυπομονησία να γυρίσουν"], 2, "νιώθουν ξαφνικά πόσο εύθραυστος είναι και πόσο ενωμένη είναι η ανθρωπότητα"),
  Q("Τι μελετούν σήμερα ορισμένοι ψυχολόγοι;", ["Αν μπορεί να προκληθεί κάτι ανάλογο στη Γη με εικονική πραγματικότητα", "Πώς επηρεάζει η έλλειψη βαρύτητας τον ύπνο", "Γιατί οι αστροναύτες παθαίνουν κατάθλιψη", "Πώς θα ζήσουν άνθρωποι στη Σελήνη"], 0, "αν κάτι ανάλογο μπορεί να προκληθεί και στη Γη, με εικονική πραγματικότητα"),
  Q("Πώς χαρακτηρίζει η αφηγήτρια τα μέχρι τώρα αποτελέσματα αυτών των μελετών;", ["Εντυπωσιακά", "Οριστικά", "Αρνητικά", "Αντιφατικά"], 3, "Τα αποτελέσματα, προς το παρόν, είναι αντιφατικά"),
 ],
 "gloss": {"επισκόπησης": "επισκόπηση — overview", "παραμονή": "παραμονή — eve", "διαστημόπλοιο": "διαστημόπλοιο — spacecraft", "ορίζοντά": "ορίζοντας — horizon", "σφαίρα": "σφαίρα — sphere", "κενό": "κενό — void", "σύνορα": "σύνορο — border", "στρώμα": "στρώμα — layer", "βερνικιού": "βερνίκι — varnish", "εύθραυστος": "εύθραυστος — fragile", "μεταστροφή": "μεταστροφή — shift, change of outlook", "δέος": "δέος — awe", "εικονική πραγματικότητα": "εικονική πραγματικότητα — virtual reality", "ευαισθητοποιηθούν": "ευαισθητοποιούμαι — to become aware", "αντιφατικά": "αντιφατικός — contradictory, mixed", "κουκκίδα": "κουκκίδα — dot"}
})

ITEMS.append({
 "id": "l137-c1-aiginitis", "title": "Δημήτριος Αιγινήτης, ο αστρονόμος του Θησείου", "title_en": "Dimitrios Eginitis, the astronomer of Thiseio", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με έναν ιστορικό της επιστήμης για τον Δημήτριο Αιγινήτη.",
 "script": [
  L("Δημοσιογράφος", "f", "Ποιος ήταν ο Δημήτριος Αιγινήτης;", "Who was Dimitrios Eginitis?"),
  L("Ιστορικός", "m", "Ήταν αστρονόμος, γεννημένος στην Αθήνα το 1862. Σπούδασε μαθηματικά στην Αθήνα και αστρονομία στο Παρίσι. Το 1890, πολύ νέος ακόμα, ανέλαβε τη διεύθυνση του Αστεροσκοπείου Αθηνών, στον λόφο των Νυμφών, απέναντι από το Θησείο. Το βρήκε σχεδόν εγκαταλελειμμένο, με παλιά όργανα, και το μετέτρεψε σε σύγχρονο ερευνητικό ίδρυμα.", "He was an astronomer, born in Athens in 1862. He studied mathematics in Athens and astronomy in Paris. In 1890, still very young, he became director of the Athens Observatory, on the Hill of the Nymphs, opposite Thiseio. He found it almost abandoned, with old instruments, and turned it into a modern research institution."),
  L("Δημοσιογράφος", "f", "Δεν ασχολήθηκε όμως μόνο με τα άστρα.", "But he didn't only deal with the stars."),
  L("Ιστορικός", "m", "Καθόλου. Οργάνωσε ένα δίκτυο μετεωρολογικών σταθμών σε όλη τη χώρα, και το Αστεροσκοπείο άρχισε να καταγράφει συστηματικά και τους σεισμούς. Ήταν επίσης από τους βασικούς υποστηρικτές της υιοθέτησης του Γρηγοριανού ημερολογίου, που η Ελλάδα εφάρμοσε τελικά το 1923, όταν μετά τις 15 Φεβρουαρίου ακολούθησε κατευθείαν η 1η Μαρτίου.", "Not at all. He organised a network of meteorological stations across the country, and the Observatory also began systematically recording earthquakes. He was also one of the main supporters of adopting the Gregorian calendar, which Greece finally introduced in 1923, when 15 February was followed directly by 1 March."),
  L("Δημοσιογράφος", "f", "Πώς τον θυμόμαστε σήμερα;", "How do we remember him today?"),
  L("Ιστορικός", "m", "Ως έναν από τους θεμελιωτές της σύγχρονης επιστημονικής έρευνας στην Ελλάδα. Το 1926 ήταν από τα πρώτα μέλη της Ακαδημίας Αθηνών. Και κάθε φορά που κάποιος ανεβαίνει στον λόφο του Αστεροσκοπείου για να δει τα αστέρια πάνω από την Ακρόπολη, περπατά, χωρίς να το ξέρει, στα βήματά του.", "As one of the founders of modern scientific research in Greece. In 1926 he was among the first members of the Academy of Athens. And every time someone climbs the Observatory hill to look at the stars above the Acropolis, they walk, without knowing it, in his footsteps."),
 ],
 "questions": [
  Q("Σε τι κατάσταση βρήκε το Αστεροσκοπείο το 1890;", ["Σε άριστη κατάσταση", "Σχεδόν εγκαταλελειμμένο, με παλιά όργανα", "Κατεστραμμένο από σεισμό", "Υπό κατασκευή"], 1, "Το βρήκε σχεδόν εγκαταλελειμμένο, με παλιά όργανα"),
  Q("Τι οργάνωσε, εκτός από την αστρονομική έρευνα;", ["Ένα πανεπιστήμιο", "Ένα πλανητάριο", "Ένα δίκτυο μετεωρολογικών σταθμών σε όλη τη χώρα", "Μια σχολή πιλότων"], 2, "Οργάνωσε ένα δίκτυο μετεωρολογικών σταθμών σε όλη τη χώρα"),
  Q("Τι έγινε στην Ελλάδα το 1923;", ["Υιοθετήθηκε το Γρηγοριανό ημερολόγιο, και μετά τις 15 Φεβρουαρίου ακολούθησε η 1η Μαρτίου", "Ιδρύθηκε το Αστεροσκοπείο", "Ιδρύθηκε η Ακαδημία Αθηνών", "Έγινε ένας μεγάλος σεισμός"], 0, "όταν μετά τις 15 Φεβρουαρίου ακολούθησε κατευθείαν η 1η Μαρτίου"),
  Q("Τι ήταν το 1926;", ["Διευθυντής ενός μουσείου", "Υπουργός", "Πρύτανης του πανεπιστημίου", "Ένα από τα πρώτα μέλη της Ακαδημίας Αθηνών"], 3, "Το 1926 ήταν από τα πρώτα μέλη της Ακαδημίας Αθηνών"),
 ],
 "gloss": {"αστρονόμος": "αστρονόμος — astronomer", "Αστεροσκοπείου": "αστεροσκοπείο — observatory", "εγκαταλελειμμένο": "εγκαταλελειμμένος — abandoned", "όργανα": "όργανο — instrument", "ερευνητικό ίδρυμα": "ερευνητικό ίδρυμα — research institution", "δίκτυο": "δίκτυο — network", "μετεωρολογικών": "μετεωρολογικός — meteorological", "καταγράφει": "καταγράφω — to record", "υποστηρικτές": "υποστηρικτής — supporter", "υιοθέτησης": "υιοθέτηση — adoption", "ημερολογίου": "ημερολόγιο — calendar", "θεμελιωτές": "θεμελιωτής — founder"}
})

rnd = random.Random(137)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-137.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
