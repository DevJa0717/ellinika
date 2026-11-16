# Source for library/listening/listening-25.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l25.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l25-ann-paralia", "title": "Καθαρίζουμε την παραλία", "title_en": "Let's clean the beach", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση του δήμου στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος, σε συνεργασία με περιβαλλοντικούς συλλόγους, οργανώνει την Κυριακή εθελοντικό καθαρισμό της παραλίας του Αγίου Νικολάου. Η συνάντηση θα γίνει στις εννιά το πρωί στο αναψυκτήριο, και η δράση θα διαρκέσει περίπου τρεις ώρες.", "The council, together with environmental associations, is organising a volunteer beach clean-up at Agios Nikolaos beach on Sunday. The meeting point is the snack bar at nine in the morning, and the activity will last about three hours."),
  L("Εκφωνήτρια", "f", "Γάντια, σακούλες και νερό θα δοθούν στους συμμετέχοντες. Παρακαλούνται να φορούν καπέλο και αντηλιακό και να φέρουν, αν θέλουν, το δικό τους μπουκάλι, ώστε να μειωθούν τα πλαστικά. Τα παιδιά μπορούν να συμμετέχουν μόνο με τη συνοδεία ενήλικα.", "Gloves, bags and water will be given to participants. They are asked to wear a hat and sunscreen and to bring, if they wish, their own bottle, so as to reduce plastic. Children may take part only accompanied by an adult."),
  L("Εκφωνήτρια", "f", "Τα απορρίμματα θα διαχωριστούν επί τόπου για ανακύκλωση, και οι επιστήμονες του συλλόγου θα καταγράψουν τα είδη τους για μια ευρωπαϊκή έρευνα για τη ρύπανση των θαλασσών. Στο τέλος θα ακολουθήσει κέρασμα για όλους.", "The rubbish will be sorted on the spot for recycling, and the association's scientists will record the types for a European study on marine pollution. At the end there will be refreshments for everyone."),
 ],
 "questions": [
  Q("Πού θα συναντηθούν οι εθελοντές;", ["Στο δημαρχείο", "Στο αναψυκτήριο της παραλίας", "Στο λιμάνι", "Στην πλατεία"], 1, "Η συνάντηση θα γίνει στις εννιά το πρωί στο αναψυκτήριο"),
  Q("Γιατί προτείνεται να φέρουν δικό τους μπουκάλι;", ["Γιατί δεν θα δοθεί νερό", "Για να μειωθούν τα πλαστικά", "Γιατί θα κάνει ζέστη", "Για να το γεμίσουν με άμμο"], 1, "ώστε να μειωθούν τα πλαστικά"),
  Q("Τι θα γίνει με τα απορρίμματα;", ["Θα πεταχτούν σε χωματερή", "Θα διαχωριστούν για ανακύκλωση και θα καταγραφούν για μια έρευνα", "Θα καούν", "Θα σταλούν στο εξωτερικό"], 1, "θα διαχωριστούν επί τόπου για ανακύκλωση, και οι επιστήμονες του συλλόγου θα καταγράψουν τα είδη τους"),
 ],
 "gloss": {"περιβαλλοντικούς": "περιβαλλοντικός — environmental", "εθελοντικό": "εθελοντικός — volunteer", "αναψυκτήριο": "αναψυκτήριο — snack bar, kiosk", "δράση": "δράση — activity, action", "αντηλιακό": "αντηλιακό — sunscreen", "συνοδεία": "συνοδεία — company, escort", "απορρίμματα": "απόρριμμα — waste, rubbish", "θα διαχωριστούν": "διαχωρίζομαι — to be separated, sorted", "επί τόπου": "επί τόπου — on the spot", "ρύπανση": "ρύπανση — pollution", "κέρασμα": "κέρασμα — treat, refreshments"},
})

ITEMS.append({
 "id": "l25-vm-courier", "title": "Ένα δέμα που δεν παραδόθηκε", "title_en": "A parcel that wasn't delivered", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από μια εταιρεία ταχυμεταφορών.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, από την εταιρεία ταχυμεταφορών σάς καλούμε σχετικά με ένα δέμα στο όνομά σας. Ο διανομέας μας πέρασε σήμερα το πρωί από τη διεύθυνσή σας, αλλά δεν απάντησε κανείς στο κουδούνι, και το δέμα χρειάζεται υπογραφή παραλήπτη.", "Good morning, we're calling from the courier company about a parcel in your name. Our courier came by your address this morning, but nobody answered the bell, and the parcel needs the recipient's signature."),
  L("Υπάλληλος", "m", "Έχετε δύο επιλογές. Μπορείτε να το παραλάβετε από το κατάστημά μας στην οδό Πατησίων, από Δευτέρα έως Παρασκευή, οχτώ με οχτώ, με την αστυνομική σας ταυτότητα. Ή μπορείτε να κλείσετε νέα ημερομηνία παράδοσης από την ιστοσελίδα μας, με τον αριθμό αποστολής που σας στείλαμε με μήνυμα.", "You have two options. You can collect it from our shop on Patision Street, Monday to Friday, eight to eight, with your ID card. Or you can book a new delivery date on our website, with the tracking number we sent you by text."),
  L("Υπάλληλος", "m", "Σας ενημερώνουμε ότι το δέμα θα παραμείνει στο κατάστημα για δέκα ημέρες. Μετά από αυτό το διάστημα θα επιστραφεί στον αποστολέα.", "Please note that the parcel will remain at the shop for ten days. After that period it will be returned to the sender."),
 ],
 "questions": [
  Q("Γιατί δεν παραδόθηκε το δέμα;", ["Γιατί η διεύθυνση ήταν λάθος", "Γιατί δεν απάντησε κανείς και χρειάζεται υπογραφή", "Γιατί είχε χαλάσει", "Γιατί δεν είχε πληρωθεί"], 1, "δεν απάντησε κανείς στο κουδούνι, και το δέμα χρειάζεται υπογραφή παραλήπτη"),
  Q("Τι πρέπει να έχει μαζί του για να το παραλάβει από το κατάστημα;", ["Την απόδειξη αγοράς", "Την αστυνομική του ταυτότητα", "Το διαβατήριο", "Ένα εξουσιοδοτημένο πρόσωπο"], 1, "με την αστυνομική σας ταυτότητα"),
  Q("Τι θα συμβεί αν δεν το παραλάβει μέσα σε δέκα ημέρες;", ["Θα πληρώσει πρόστιμο", "Θα επιστραφεί στον αποστολέα", "Θα καταστραφεί", "Θα του σταλεί ξανά"], 1, "θα επιστραφεί στον αποστολέα"),
 ],
 "gloss": {"ταχυμεταφορών": "ταχυμεταφορές — courier services", "διανομέας": "διανομέας — courier, delivery person", "κουδούνι": "κουδούνι — doorbell", "υπογραφή": "υπογραφή — signature", "παραλήπτη": "παραλήπτης — recipient", "να το παραλάβετε": "παραλαμβάνω — to collect, receive", "αριθμό αποστολής": "αριθμός αποστολής — tracking number", "θα παραμείνει": "παραμένω — to remain", "διάστημα": "διάστημα — period", "αποστολέα": "αποστολέας — sender"},
})

ITEMS.append({
 "id": "l25-dia-apolesthenta", "title": "Στο γραφείο απολεσθέντων", "title_en": "At the lost property office", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση στο γραφείο απολεσθέντων αντικειμένων ενός σιδηροδρομικού σταθμού.",
 "script": [
  L("Επιβάτισσα", "f", "Καλησπέρα. Ξέχασα το σακίδιό μου στο τρένο από τη Θεσσαλονίκη, που έφτασε στις τρεις. Το κατάλαβα μόνο όταν είχα βγει από τον σταθμό.", "Good afternoon. I left my backpack on the train from Thessaloniki that arrived at three. I only realised once I'd left the station."),
  L("Υπάλληλος", "m", "Θα το ελέγξω. Οι συνοδοί συνήθως φέρνουν εδώ ό,τι βρίσκουν μετά τον καθαρισμό των βαγονιών. Μπορείτε να μου το περιγράψετε; Και σε ποιο βαγόνι καθόσασταν;", "I'll check. The conductors usually bring here whatever they find after the carriages are cleaned. Can you describe it? And which carriage were you sitting in?"),
  L("Επιβάτισσα", "f", "Στο βαγόνι πέντε, θέση σαράντα δύο. Είναι ένα μαύρο σακίδιο με ένα κόκκινο μπρελόκ σε σχήμα αστεριού. Μέσα έχει τον φορητό μου υπολογιστή και ένα βιβλίο.", "Carriage five, seat forty-two. It's a black backpack with a red star-shaped keyring. Inside there's my laptop and a book."),
  L("Υπάλληλος", "m", "Έχετε τύχη· ήρθε πριν από μισή ώρα. Για να σας το δώσω, όμως, πρέπει να μου πείτε τι βιβλίο είναι, για να βεβαιωθώ ότι είναι δικό σας, και να υπογράψετε εδώ. Χρειάζομαι και την ταυτότητά σας.", "You're in luck; it came in half an hour ago. But to give it to you, you need to tell me what book it is, so I can be sure it's yours, and sign here. I also need your ID."),
 ],
 "questions": [
  Q("Πότε κατάλαβε η επιβάτισσα ότι είχε ξεχάσει το σακίδιο;", ["Μέσα στο τρένο", "Όταν είχε βγει από τον σταθμό", "Το επόμενο πρωί", "Στη Θεσσαλονίκη"], 1, "Το κατάλαβα μόνο όταν είχα βγει από τον σταθμό"),
  Q("Πώς φτάνουν τα ξεχασμένα αντικείμενα στο γραφείο;", ["Τα φέρνουν οι επιβάτες", "Τα φέρνουν οι συνοδοί μετά τον καθαρισμό των βαγονιών", "Τα φέρνει η αστυνομία", "Τα στέλνει ο σταθμός της Θεσσαλονίκης"], 1, "Οι συνοδοί συνήθως φέρνουν εδώ ό,τι βρίσκουν μετά τον καθαρισμό των βαγονιών"),
  Q("Τι της ζητά ο υπάλληλος για να βεβαιωθεί ότι το σακίδιο είναι δικό της;", ["Τον κωδικό του υπολογιστή", "Να του πει τι βιβλίο έχει μέσα", "Το εισιτήριο", "Μια φωτογραφία του σακιδίου"], 1, "πρέπει να μου πείτε τι βιβλίο είναι, για να βεβαιωθώ ότι είναι δικό σας"),
 ],
 "gloss": {"απολεσθέντων": "απολεσθέντα (αντικείμενα) — lost property", "σιδηροδρομικού": "σιδηροδρομικός — railway (adj.)", "σακίδιό": "σακίδιο — backpack", "συνοδοί": "συνοδός — (train) conductor, attendant", "βαγονιών": "βαγόνι — carriage", "περιγράψετε": "περιγράφω — to describe", "μπρελόκ": "μπρελόκ — keyring", "σχήμα": "σχήμα — shape", "φορητό μου υπολογιστή": "φορητός υπολογιστής — laptop", "να βεβαιωθώ": "βεβαιώνομαι — to make sure"},
})

ITEMS.append({
 "id": "l25-dia-odeio", "title": "Μαθήματα κιθάρας", "title_en": "Guitar lessons", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση στη γραμματεία ενός ωδείου.",
 "script": [
  L("Πελάτης", "m", "Γεια σας. Θα ήθελα να γραφτώ σε μαθήματα κιθάρας. Είμαι σαράντα πέντε χρονών και δεν έχω πιάσει ποτέ όργανο στα χέρια μου. Μήπως είναι αργά;", "Hello. I'd like to sign up for guitar lessons. I'm forty-five and I've never held an instrument in my hands. Is it too late?"),
  L("Γραμματέας", "f", "Καθόλου! Έχουμε πολλούς ενήλικες μαθητές, ο μεγαλύτερος είναι εβδομήντα δύο. Για αρχάριους προτείνουμε ατομικά μαθήματα μισής ώρας, μία φορά την εβδομάδα, τουλάχιστον τους πρώτους μήνες. Υπάρχει και ομαδικό τμήμα για ενήλικες, την Τετάρτη το βράδυ, που κοστίζει λιγότερο.", "Not at all! We have many adult students; the oldest is seventy-two. For beginners we suggest individual half-hour lessons once a week, at least for the first few months. There's also a group class for adults on Wednesday evening, which costs less."),
  L("Πελάτης", "m", "Το ομαδικό μου ακούγεται καλύτερο· νομίζω ότι θα ντρεπόμουν λιγότερο. Χρειάζεται να έχω δική μου κιθάρα από την αρχή;", "The group class sounds better to me; I think I'd be less embarrassed. Do I need to have my own guitar from the start?"),
  L("Γραμματέας", "f", "Για τον πρώτο μήνα μπορούμε να σας δανείσουμε μία από το ωδείο. Σας συμβουλεύω να μην αγοράσετε ακριβή κιθάρα πριν δείτε αν σας αρέσει. Η πρώτη ομαδική συνάντηση είναι δωρεάν, ώστε να δείτε πώς είναι πριν πληρώσετε.", "For the first month we can lend you one from the conservatory. I advise you not to buy an expensive guitar before you see whether you like it. The first group session is free, so you can see what it's like before you pay."),
 ],
 "questions": [
  Q("Τι ανησυχεί τον πελάτη;", ["Το κόστος", "Μήπως είναι πολύ μεγάλος για να ξεκινήσει", "Το ωράριο", "Η απόσταση από το σπίτι του"], 1, "Μήπως είναι αργά;"),
  Q("Γιατί προτιμά το ομαδικό τμήμα;", ["Γιατί είναι πιο κοντά", "Γιατί νομίζει ότι θα ντρέπεται λιγότερο", "Γιατί έχει φίλους εκεί", "Γιατί είναι το πρωί"], 1, "νομίζω ότι θα ντρεπόμουν λιγότερο"),
  Q("Τι του προτείνει η γραμματέας για την κιθάρα;", ["Να αγοράσει αμέσως μια καλή κιθάρα", "Να δανειστεί μία από το ωδείο τον πρώτο μήνα", "Να νοικιάσει μία από ένα κατάστημα", "Να χρησιμοποιεί την κιθάρα του δασκάλου"], 1, "Για τον πρώτο μήνα μπορούμε να σας δανείσουμε μία από το ωδείο"),
 ],
 "gloss": {"ωδείου": "ωδείο — conservatory, music school", "να γραφτώ": "γράφομαι — to sign up", "όργανο": "όργανο — (musical) instrument", "αρχάριους": "αρχάριος — beginner", "ατομικά": "ατομικός — individual", "ομαδικό τμήμα": "ομαδικό τμήμα — group class", "θα ντρεπόμουν": "ντρέπομαι — to be shy, embarrassed", "να σας δανείσουμε": "δανείζω — to lend", "συνάντηση": "συνάντηση — session, meeting"},
})

ITEMS.append({
 "id": "l25-mon-xylourgos", "title": "Από την τράπεζα στο ξυλουργείο", "title_en": "From the bank to the carpenter's workshop", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλάει για την αλλαγή της καριέρας του.",
 "script": [
  L("Άντρας", "m", "Για δεκαπέντε χρόνια δούλευα σε μια τράπεζα, στο τμήμα δανείων. Είχα καλό μισθό και σταθερό ωράριο, αλλά κάθε Κυριακή βράδυ ένιωθα ένα βάρος στο στομάχι. Το μόνο που με χαλάρωνε ήταν να φτιάχνω μικρά έπιπλα στην αποθήκη της πολυκατοικίας μας.", "For fifteen years I worked at a bank, in the loans department. I had a good salary and regular hours, but every Sunday evening I felt a weight in my stomach. The only thing that relaxed me was making small pieces of furniture in our building's storeroom."),
  L("Άντρας", "m", "Στα σαράντα, όταν η τράπεζα πρότεινε εθελουσία έξοδο, το αποφάσισα. Η γυναίκα μου με στήριξε, αν και φοβόταν. Δούλεψα δύο χρόνια ως βοηθός σε έναν παλιό ξυλουργό, ο οποίος μου έμαθε όσα δεν διδάσκονται σε κανένα σεμινάριο: πώς να διαβάζω τα νερά του ξύλου, πώς να ακούω το πριόνι.", "At forty, when the bank offered voluntary redundancy, I made up my mind. My wife supported me, although she was afraid. I worked for two years as assistant to an old carpenter, who taught me what isn't taught in any seminar: how to read the grain of the wood, how to listen to the saw."),
  L("Άντρας", "m", "Σήμερα έχω δικό μου μικρό εργαστήριο. Βγάζω λιγότερα χρήματα, και οι πρώτοι δύο χρόνοι ήταν πραγματικά δύσκολοι. Όμως όταν παραδίδω ένα τραπέζι σε μια οικογένεια και ξέρω ότι θα τρώνε σε αυτό για τριάντα χρόνια, νιώθω κάτι που δεν ένιωσα ποτέ εγκρίνοντας ένα δάνειο.", "Today I have my own small workshop. I earn less money, and the first two years were really hard. But when I deliver a table to a family and know they'll eat at it for thirty years, I feel something I never felt approving a loan."),
 ],
 "questions": [
  Q("Τι τον χαλάρωνε όταν δούλευε στην τράπεζα;", ["Το τρέξιμο", "Να φτιάχνει μικρά έπιπλα", "Η μουσική", "Τα ταξίδια"], 1, "Το μόνο που με χαλάρωνε ήταν να φτιάχνω μικρά έπιπλα"),
  Q("Πώς έμαθε την τέχνη;", ["Σε μια σχολή ξυλουργικής", "Δουλεύοντας δύο χρόνια ως βοηθός ενός παλιού ξυλουργού", "Από βίντεο στο διαδίκτυο", "Από τον πατέρα του"], 1, "Δούλεψα δύο χρόνια ως βοηθός σε έναν παλιό ξυλουργό"),
  Q("Τι νιώθει σήμερα για τη δουλειά του;", ["Ότι βγάζει περισσότερα χρήματα", "Μια ικανοποίηση που δεν ένιωθε στην τράπεζα", "Ότι μετάνιωσε", "Ότι κουράζεται πολύ"], 1, "νιώθω κάτι που δεν ένιωσα ποτέ εγκρίνοντας ένα δάνειο"),
 ],
 "gloss": {"δανείων": "δάνειο — loan", "βάρος": "βάρος — weight", "με χαλάρωνε": "χαλαρώνω — to relax", "έπιπλα": "έπιπλο — piece of furniture", "εθελουσία έξοδο": "εθελουσία έξοδος — voluntary redundancy", "με στήριξε": "στηρίζω — to support", "ξυλουργό": "ξυλουργός — carpenter", "νερά του ξύλου": "τα νερά του ξύλου — the grain of the wood", "πριόνι": "πριόνι — saw", "εγκρίνοντας": "εγκρίνω — to approve"},
})

ITEMS.append({
 "id": "l25-rep-aigina", "title": "Η Αίγινα", "title_en": "Aegina", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για την Αίγινα σε μια ταξιδιωτική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Μόλις μία ώρα με το πλοίο από τον Πειραιά, η Αίγινα είναι ο αγαπημένος προορισμός πολλών Αθηναίων για ένα Σαββατοκύριακο. Το πρώτο που βλέπει κανείς στο λιμάνι είναι οι πάγκοι με τα φιστίκια, που έκαναν το νησί γνωστό σε όλη την Ελλάδα και έχουν πάρει την πιστοποίηση προϊόντος προστατευόμενης ονομασίας προέλευσης.", "Just an hour by boat from Piraeus, Aegina is the favourite weekend destination of many Athenians. The first thing you see in the harbour are the stalls with pistachios, which made the island known all over Greece and have been certified as a product with protected designation of origin."),
  L("Ρεπόρτερ", "f", "Λίγοι γνωρίζουν ότι η Αίγινα υπήρξε για λίγο έδρα της πρώτης ελληνικής κυβέρνησης, μετά την άφιξη του Καποδίστρια το 1828. Εδώ κόπηκε και το πρώτο νόμισμα του νέου κράτους, ο φοίνικας.", "Few know that Aegina was briefly the seat of the first Greek government, after Kapodistrias arrived in 1828. The first coin of the new state, the phoenix, was also minted here."),
  L("Ρεπόρτερ", "f", "Στην κορυφή ενός λόφου, μέσα στα πεύκα, στέκεται ο ναός της Αφαίας, ένας από τους καλύτερα σωσμένους αρχαίους ναούς της χώρας. Σύμφωνα με μια δημοφιλή άποψη, ο ναός της Αφαίας, ο Παρθενώνας και ο ναός του Ποσειδώνα στο Σούνιο σχηματίζουν ένα ισόπλευρο τρίγωνο, αν και οι αρχαιολόγοι το θεωρούν μάλλον σύμπτωση.", "On top of a hill, among the pines, stands the temple of Aphaia, one of the best-preserved ancient temples in the country. According to a popular view, the temple of Aphaia, the Parthenon and the temple of Poseidon at Sounion form an equilateral triangle, although archaeologists consider this more likely a coincidence."),
 ],
 "questions": [
  Q("Για ποιο προϊόν είναι γνωστή η Αίγινα;", ["Για το μέλι", "Για τα φιστίκια", "Για το κρασί", "Για το λάδι"], 1, "οι πάγκοι με τα φιστίκια, που έκαναν το νησί γνωστό σε όλη την Ελλάδα"),
  Q("Τι έγινε στην Αίγινα μετά το 1828;", ["Χτίστηκε ο ναός της Αφαίας", "Έγινε για λίγο έδρα της κυβέρνησης και κόπηκε το πρώτο νόμισμα", "Ιδρύθηκε το πρώτο πανεπιστήμιο", "Έγινε η πρώτη πρωτεύουσα για δεκαετίες"], 1, "υπήρξε για λίγο έδρα της πρώτης ελληνικής κυβέρνησης ... Εδώ κόπηκε και το πρώτο νόμισμα"),
  Q("Τι πιστεύουν οι αρχαιολόγοι για το «ιερό τρίγωνο»;", ["Ότι σχεδιάστηκε σκόπιμα", "Ότι είναι μάλλον σύμπτωση", "Ότι είναι ένας μύθος του 19ου αιώνα", "Ότι αποδεικνύει μια αρχαία θρησκεία"], 1, "οι αρχαιολόγοι το θεωρούν μάλλον σύμπτωση"),
 ],
 "gloss": {"προορισμός": "προορισμός — destination", "πάγκοι": "πάγκος — stall", "φιστίκια": "φιστίκι — pistachio", "πιστοποίηση": "πιστοποίηση — certification", "προστατευόμενης ονομασίας προέλευσης": "ΠΟΠ — protected designation of origin", "έδρα": "έδρα — seat", "άφιξη": "άφιξη — arrival", "κόπηκε": "κόβομαι — to be minted (of coins); to be cut", "νόμισμα": "νόμισμα — coin, currency", "πεύκα": "πεύκο — pine", "σωσμένους": "σωσμένος — preserved", "ισόπλευρο": "ισόπλευρος — equilateral", "σύμπτωση": "σύμπτωση — coincidence"},
})

ITEMS.append({
 "id": "l25-rep-olympos", "title": "Ο Όλυμπος", "title_en": "Mount Olympus", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από τον Όλυμπο.",
 "script": [
  L("Ρεπόρτερ", "m", "Βρισκόμαστε στο Λιτόχωρο, στους πρόποδες του Ολύμπου, του ψηλότερου βουνού της Ελλάδας. Η ψηλότερη κορυφή του, ο Μύτικας, φτάνει τα δύο χιλιάδες εννιακόσια δεκαεπτά μέτρα. Για τους αρχαίους, εδώ ζούσαν οι δώδεκα θεοί, κρυμμένοι πίσω από τα σύννεφα.", "We are in Litochoro, at the foot of Olympus, Greece's highest mountain. Its highest peak, Mytikas, reaches two thousand nine hundred and seventeen metres. For the ancients, this is where the twelve gods lived, hidden behind the clouds."),
  L("Ρεπόρτερ", "m", "Παρά τη φήμη του, ο Μύτικας κατακτήθηκε πολύ αργά: το 1913, από δύο Ελβετούς και έναν ντόπιο κυνηγό, τον Χρήστο Κάκαλο, ο οποίος τους οδήγησε ως την κορυφή. Το 1938 ο Όλυμπος έγινε ο πρώτος εθνικός δρυμός της Ελλάδας.", "Despite its fame, Mytikas was conquered very late: in 1913, by two Swiss and a local hunter, Christos Kakkalos, who guided them to the summit. In 1938 Olympus became Greece's first national park."),
  L("Ρεπόρτερ", "m", "Σήμερα χιλιάδες ορειβάτες ανεβαίνουν κάθε καλοκαίρι, συνήθως διανυκτερεύοντας σε ένα από τα καταφύγια. Οι διασώστες, όμως, προειδοποιούν: ο καιρός στο βουνό αλλάζει απότομα, και η τελευταία ανάβαση προς την κορυφή απαιτεί εμπειρία και κατάλληλο εξοπλισμό.", "Today thousands of climbers go up every summer, usually staying overnight in one of the refuges. Rescuers, however, warn: the weather on the mountain changes suddenly, and the final climb to the summit requires experience and proper equipment."),
 ],
 "questions": [
  Q("Ποια ήταν η σημασία του Ολύμπου για τους αρχαίους;", ["Ήταν τόπος αγώνων", "Εκεί πίστευαν ότι ζούσαν οι δώδεκα θεοί", "Ήταν σύνορο με τη Θράκη", "Εκεί έκαναν θυσίες στον Ποσειδώνα"], 1, "Για τους αρχαίους, εδώ ζούσαν οι δώδεκα θεοί"),
  Q("Ποιος οδήγησε τους πρώτους ορειβάτες στην κορυφή το 1913;", ["Ένας Ελβετός οδηγός", "Ένας ντόπιος κυνηγός, ο Χρήστος Κάκαλος", "Ένας Γερμανός αρχαιολόγος", "Ένας μοναχός"], 1, "έναν ντόπιο κυνηγό, τον Χρήστο Κάκαλο, ο οποίος τους οδήγησε ως την κορυφή"),
  Q("Τι συμβουλεύουν οι διασώστες;", ["Να μην ανεβαίνει κανείς το καλοκαίρι", "Ότι η τελευταία ανάβαση απαιτεί εμπειρία και εξοπλισμό", "Να μη διανυκτερεύει κανείς στα καταφύγια", "Να ανεβαίνουν μόνο με οργανωμένες ομάδες"], 1, "η τελευταία ανάβαση προς την κορυφή απαιτεί εμπειρία και κατάλληλο εξοπλισμό"),
 ],
 "gloss": {"πρόποδες": "πρόποδες — foot (of a mountain)", "κορυφή": "κορυφή — peak, summit", "σύννεφα": "σύννεφο — cloud", "κατακτήθηκε": "κατακτιέμαι — to be conquered", "κυνηγό": "κυνηγός — hunter", "εθνικός δρυμός": "εθνικός δρυμός — national park", "ορειβάτες": "ορειβάτης — mountaineer", "διανυκτερεύοντας": "διανυκτερεύω — to stay overnight", "καταφύγια": "καταφύγιο — (mountain) refuge", "διασώστες": "διασώστης — rescuer", "ανάβαση": "ανάβαση — climb, ascent", "εξοπλισμό": "εξοπλισμός — equipment"},
})

ITEMS.append({
 "id": "l25-int-diermineas", "title": "Διερμηνέας στα δικαστήρια", "title_en": "A court interpreter", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια διερμηνέα που εργάζεται στα δικαστήρια.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνει ένας δικαστικός διερμηνέας;", "What exactly does a court interpreter do?"),
  L("Διερμηνέας", "f", "Μεταφράζουμε προφορικά, την ώρα της δίκης, για κατηγορουμένους, μάρτυρες ή θύματα που δεν μιλούν ελληνικά. Εγώ δουλεύω με αραβικά και γαλλικά. Χωρίς διερμηνέα, ένας άνθρωπος μπορεί να καταδικαστεί χωρίς να καταλάβει καν τι του καταλογίζουν.", "We interpret orally, during the trial, for defendants, witnesses or victims who don't speak Greek. I work with Arabic and French. Without an interpreter, a person can be convicted without even understanding what they're accused of."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο δύσκολο κομμάτι;", "What's the hardest part?"),
  L("Διερμηνέας", "f", "Η ουδετερότητα. Πρέπει να μεταφέρω κάθε λέξη με ακρίβεια, ακόμη κι αν κάποιος λέει κάτι που με θυμώνει ή με συγκινεί. Δεν επιτρέπεται να βελτιώσω τη διατύπωση ή να εξηγήσω. Και φυσικά, οι νομικοί όροι: μια λάθος λέξη μπορεί να αλλάξει την έκβαση μιας υπόθεσης. Γι' αυτό διαβάζω τον φάκελο πριν από κάθε δίκη και ετοιμάζω το δικό μου γλωσσάρι.", "Neutrality. I have to convey every word accurately, even if someone says something that makes me angry or moves me. I'm not allowed to improve the wording or explain. And of course, the legal terms: one wrong word can change the outcome of a case. That's why I read the file before every trial and prepare my own glossary."),
 ],
 "questions": [
  Q("Γιατί είναι απαραίτητος ο διερμηνέας στη δίκη;", ["Για να καθυστερεί η διαδικασία", "Για να καταλαβαίνει ο κατηγορούμενος τι του καταλογίζουν", "Για να υπερασπίζεται τον κατηγορούμενο", "Για να γράφει τα πρακτικά"], 1, "ένας άνθρωπος μπορεί να καταδικαστεί χωρίς να καταλάβει καν τι του καταλογίζουν"),
  Q("Τι δεν επιτρέπεται να κάνει η διερμηνέας;", ["Να μεταφράζει προφορικά", "Να βελτιώσει τη διατύπωση ή να εξηγήσει", "Να διαβάσει τον φάκελο", "Να δουλεύει με δύο γλώσσες"], 1, "Δεν επιτρέπεται να βελτιώσω τη διατύπωση ή να εξηγήσω"),
  Q("Πώς προετοιμάζεται για κάθε δίκη;", ["Μιλά με τον δικαστή", "Διαβάζει τον φάκελο και ετοιμάζει γλωσσάρι", "Συναντά τον κατηγορούμενο", "Δεν προετοιμάζεται"], 1, "διαβάζω τον φάκελο πριν από κάθε δίκη και ετοιμάζω το δικό μου γλωσσάρι"),
 ],
 "gloss": {"διερμηνέα": "διερμηνέας — interpreter", "δικαστήρια": "δικαστήριο — court", "δίκης": "δίκη — trial", "κατηγορουμένους": "κατηγορούμενος — defendant", "μάρτυρες": "μάρτυρας — witness", "θύματα": "θύμα — victim", "να καταδικαστεί": "καταδικάζομαι — to be convicted", "καταλογίζουν": "καταλογίζω — to accuse of, attribute", "ουδετερότητα": "ουδετερότητα — neutrality", "διατύπωση": "διατύπωση — wording", "νομικοί όροι": "νομικός όρος — legal term", "έκβαση": "έκβαση — outcome", "υπόθεσης": "υπόθεση — case", "γλωσσάρι": "γλωσσάρι — glossary"},
})

ITEMS.append({
 "id": "l25-mon-ostrakismos", "title": "Ο οστρακισμός", "title_en": "Ostracism", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για τον θεσμό του οστρακισμού στην αρχαία Αθήνα.",
 "script": [
  L("Ιστορικός", "m", "Ο οστρακισμός ήταν ένας από τους πιο παράξενους θεσμούς της αθηναϊκής δημοκρατίας. Μία φορά τον χρόνο, η Εκκλησία του Δήμου αποφάσιζε αν θα γινόταν οστρακοφορία. Αν η απάντηση ήταν θετική, οι πολίτες χάραζαν σε ένα κομμάτι σπασμένου αγγείου, το όστρακο, το όνομα του πολιτικού που θεωρούσαν επικίνδυνο για την πόλη.", "Ostracism was one of the strangest institutions of Athenian democracy. Once a year, the Assembly decided whether an ostracism would take place. If the answer was yes, citizens scratched on a piece of broken pottery, the ostrakon, the name of the politician they considered dangerous for the city."),
  L("Ιστορικός", "m", "Αν συγκεντρώνονταν τουλάχιστον έξι χιλιάδες όστρακα, ο πολιτικός με τις περισσότερες ψήφους έπρεπε να εγκαταλείψει την Αθήνα για δέκα χρόνια. Δεν έχανε όμως ούτε την περιουσία του ούτε τα πολιτικά του δικαιώματα· όταν επέστρεφε, μπορούσε να ξαναμπεί στην πολιτική. Ήταν, με άλλα λόγια, ένα μέτρο πρόληψης και όχι τιμωρίας.", "If at least six thousand ostraka were collected, the politician with the most votes had to leave Athens for ten years. But he lost neither his property nor his political rights; when he returned, he could re-enter politics. It was, in other words, a preventive measure and not a punishment."),
  L("Ιστορικός", "m", "Ο θεσμός σκόπευε να προστατεύσει τη δημοκρατία από όσους αποκτούσαν υπερβολική δύναμη και θα μπορούσαν να γίνουν τύραννοι. Στην πράξη, όμως, χρησιμοποιήθηκε και ως όπλο στις πολιτικές αντιπαραθέσεις. Οι αρχαιολόγοι έχουν βρει ομάδες οστράκων με το όνομα του Θεμιστοκλή γραμμένο από λίγα μόνο χέρια, κάτι που υποδηλώνει ότι κάποιοι τα ετοίμαζαν από πριν για να τα μοιράσουν σε ψηφοφόρους.", "The institution was meant to protect democracy from those who acquired excessive power and could become tyrants. In practice, however, it was also used as a weapon in political conflicts. Archaeologists have found groups of ostraka with Themistocles' name written by only a few hands, which suggests that some people prepared them in advance to hand out to voters."),
  L("Ιστορικός", "m", "Ο οστρακισμός εγκαταλείφθηκε στα τέλη του πέμπτου αιώνα, όταν δύο αντίπαλοι πολιτικοί συνεννοήθηκαν και έστρεψαν τις ψήφους των οπαδών τους εναντίον ενός τρίτου, ασήμαντου σχετικά, πολιτικού. Ο θεσμός είχε χάσει το νόημά του. Το δίδαγμα παραμένει επίκαιρο: κάθε μηχανισμός προστασίας της δημοκρατίας μπορεί να στραφεί εναντίον της, αν πέσει σε λάθος χέρια.", "Ostracism was abandoned at the end of the fifth century, when two rival politicians came to an agreement and turned their supporters' votes against a third, relatively insignificant politician. The institution had lost its meaning. The lesson remains topical: any mechanism for protecting democracy can be turned against it if it falls into the wrong hands."),
 ],
 "questions": [
  Q("Τι έγραφαν οι πολίτες στο όστρακο;", ["Τη γνώμη τους για έναν νόμο", "Το όνομα του πολιτικού που θεωρούσαν επικίνδυνο", "Το δικό τους όνομα", "Το όνομα του υποψήφιου άρχοντα"], 1, "το όνομα του πολιτικού που θεωρούσαν επικίνδυνο για την πόλη"),
  Q("Γιατί ο ιστορικός χαρακτηρίζει τον οστρακισμό «μέτρο πρόληψης και όχι τιμωρίας»;", ["Γιατί κρατούσε μόνο έναν χρόνο", "Γιατί ο εξόριστος δεν έχανε την περιουσία ούτε τα πολιτικά του δικαιώματα", "Γιατί δεν εφαρμόστηκε ποτέ", "Γιατί αφορούσε μόνο ξένους"], 1, "Δεν έχανε όμως ούτε την περιουσία του ούτε τα πολιτικά του δικαιώματα"),
  Q("Τι δείχνουν τα όστρακα με το όνομα του Θεμιστοκλή;", ["Ότι ήταν πολύ αγαπητός", "Ότι κάποιοι τα ετοίμαζαν από πριν για να τα μοιράσουν", "Ότι ήξερε να γράφει", "Ότι ψήφισε ο ίδιος"], 1, "κάποιοι τα ετοίμαζαν από πριν για να τα μοιράσουν σε ψηφοφόρους"),
  Q("Ποιο δίδαγμα αντλεί ο ιστορικός;", ["Ότι η δημοκρατία δεν χρειάζεται προστασία", "Ότι κάθε μηχανισμός προστασίας της δημοκρατίας μπορεί να στραφεί εναντίον της", "Ότι ο οστρακισμός πρέπει να επανέλθει", "Ότι οι πολιτικοί ήταν πάντα διεφθαρμένοι"], 1, "κάθε μηχανισμός προστασίας της δημοκρατίας μπορεί να στραφεί εναντίον της"),
 ],
 "gloss": {"οστρακισμού": "οστρακισμός — ostracism", "θεσμός": "θεσμός — institution", "Εκκλησία του Δήμου": "Εκκλησία του Δήμου — the (Athenian) Assembly", "οστρακοφορία": "οστρακοφορία — ostracism vote", "χάραζαν": "χαράζω — to scratch, engrave", "αγγείου": "αγγείο — pot, vessel", "περιουσία": "περιουσία — property", "πρόληψης": "πρόληψη — prevention", "τιμωρίας": "τιμωρία — punishment", "τύραννοι": "τύραννος — tyrant", "υποδηλώνει": "υποδηλώνω — to suggest, imply", "ψηφοφόρους": "ψηφοφόρος — voter", "εγκαταλείφθηκε": "εγκαταλείπομαι — to be abandoned", "συνεννοήθηκαν": "συνεννοούμαι — to come to an agreement", "ασήμαντου": "ασήμαντος — insignificant", "δίδαγμα": "δίδαγμα — lesson", "επίκαιρο": "επίκαιρος — topical"},
})

ITEMS.append({
 "id": "l25-int-mikroplastika", "title": "Τα μικροπλαστικά", "title_en": "Microplastics", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια ωκεανογράφο για τα μικροπλαστικά.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς είναι τα μικροπλαστικά;", "What exactly are microplastics?"),
  L("Ωκεανογράφος", "f", "Είναι κομματάκια πλαστικού μικρότερα από πέντε χιλιοστά. Κάποια κατασκευάζονται εξαρχής τόσο μικρά, όπως οι μικροσφαίρες που υπήρχαν παλιότερα σε καλλυντικά. Τα περισσότερα, όμως, προέρχονται από τη διάσπαση μεγαλύτερων αντικειμένων: μιας σακούλας, ενός μπουκαλιού, ακόμη και των συνθετικών ρούχων μας, που απελευθερώνουν ίνες σε κάθε πλύση.", "They're pieces of plastic smaller than five millimetres. Some are made that small from the start, like the microbeads that used to be in cosmetics. Most, however, come from larger objects breaking down: a bag, a bottle, even our synthetic clothes, which release fibres with every wash."),
  L("Δημοσιογράφος", "m", "Και πόσο σοβαρό είναι το πρόβλημα στη Μεσόγειο;", "And how serious is the problem in the Mediterranean?"),
  L("Ωκεανογράφος", "f", "Η Μεσόγειος είναι μια σχεδόν κλειστή θάλασσα, με πυκνοκατοικημένες ακτές και έντονη ναυσιπλοΐα, οπότε τα πλαστικά παραμένουν εδώ για πολύ καιρό. Οι μετρήσεις δείχνουν συγκεντρώσεις από τις υψηλότερες στον κόσμο. Τα μικροπλαστικά τα τρώνε τα ψάρια και τα μύδια, και έτσι μπαίνουν στην τροφική αλυσίδα. Για τις επιπτώσεις στην ανθρώπινη υγεία, πάντως, η έρευνα βρίσκεται ακόμη σε αρχικό στάδιο· δεν θέλω να τρομάξω κανέναν χωρίς στοιχεία.", "The Mediterranean is an almost enclosed sea, with densely populated coasts and heavy shipping, so plastics stay here for a long time. Measurements show concentrations among the highest in the world. Microplastics are eaten by fish and mussels, and so they enter the food chain. As for the effects on human health, however, research is still at an early stage; I don't want to frighten anyone without evidence."),
  L("Ωκεανογράφος", "f", "Το σημαντικότερο είναι να σταματήσουμε το πρόβλημα στην πηγή του. Ο καθαρισμός της θάλασσας από κομμάτια που δεν φαίνονται καν είναι σχεδόν αδύνατος. Λιγότερα πλαστικά μιας χρήσης, καλύτερη διαχείριση των απορριμμάτων και φίλτρα στα πλυντήρια: αυτές είναι οι λύσεις που λειτουργούν.", "The most important thing is to stop the problem at its source. Cleaning the sea of pieces you can't even see is almost impossible. Fewer single-use plastics, better waste management and filters on washing machines: those are the solutions that work."),
 ],
 "questions": [
  Q("Από πού προέρχονται τα περισσότερα μικροπλαστικά;", ["Από καλλυντικά", "Από τη διάσπαση μεγαλύτερων αντικειμένων και τις ίνες των ρούχων", "Από τα ηφαίστεια", "Από τα ψάρια"], 1, "Τα περισσότερα, όμως, προέρχονται από τη διάσπαση μεγαλύτερων αντικειμένων"),
  Q("Γιατί το πρόβλημα είναι σοβαρό στη Μεσόγειο;", ["Γιατί είναι πολύ βαθιά", "Γιατί είναι σχεδόν κλειστή, με πυκνοκατοικημένες ακτές και έντονη ναυσιπλοΐα", "Γιατί δεν υπάρχουν ψάρια", "Γιατί είναι πολύ ζεστή"], 1, "Η Μεσόγειος είναι μια σχεδόν κλειστή θάλασσα, με πυκνοκατοικημένες ακτές και έντονη ναυσιπλοΐα"),
  Q("Τι λέει για τις επιπτώσεις στην ανθρώπινη υγεία;", ["Ότι είναι αποδεδειγμένα καταστροφικές", "Ότι η έρευνα βρίσκεται ακόμη σε αρχικό στάδιο", "Ότι δεν υπάρχουν καθόλου", "Ότι αφορούν μόνο τα παιδιά"], 1, "η έρευνα βρίσκεται ακόμη σε αρχικό στάδιο"),
  Q("Ποια λύση θεωρεί σημαντικότερη;", ["Τον καθαρισμό της θάλασσας", "Να σταματήσει το πρόβλημα στην πηγή του", "Την απαγόρευση της αλιείας", "Νέα σκάφη καθαρισμού"], 1, "Το σημαντικότερο είναι να σταματήσουμε το πρόβλημα στην πηγή του"),
 ],
 "gloss": {"ωκεανογράφο": "ωκεανογράφος — oceanographer", "μικροπλαστικά": "μικροπλαστικό — microplastic", "χιλιοστά": "χιλιοστό — millimetre", "εξαρχής": "εξαρχής — from the outset", "μικροσφαίρες": "μικροσφαίρα — microbead", "καλλυντικά": "καλλυντικό — cosmetic", "διάσπαση": "διάσπαση — breakdown", "ίνες": "ίνα — fibre", "πυκνοκατοικημένες": "πυκνοκατοικημένος — densely populated", "ναυσιπλοΐα": "ναυσιπλοΐα — shipping, navigation", "συγκεντρώσεις": "συγκέντρωση — concentration", "μύδια": "μύδι — mussel", "τροφική αλυσίδα": "τροφική αλυσίδα — food chain", "επιπτώσεις": "επίπτωση — effect, impact", "στάδιο": "στάδιο — stage", "πηγή": "πηγή — source", "μιας χρήσης": "μιας χρήσης — single-use"},
})
rnd = random.Random(25)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-25.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
