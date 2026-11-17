# Source for library/listening/listening-141.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l141.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l141-int-cheimerini-kolymvisi", "title": "Κολύμπι τον Ιανουάριο", "title_en": "Swimming in January", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική εκπομπή για τον αθλητισμό.",
 "script": [
  L("Δημοσιογράφος", "m", "Κολυμπάτε στη θάλασσα όλο τον χειμώνα, ακόμα και όταν το νερό έχει δώδεκα βαθμούς. Γιατί;", "You swim in the sea all winter, even when the water is twelve degrees. Why?"),
  L("Κολυμβήτρια", "f", "Ξεκίνησα πριν από οχτώ χρόνια, μετά από μια δύσκολη περίοδο στη ζωή μου. Μια φίλη με πήρε μαζί της ένα πρωί του Νοεμβρίου. Τα πρώτα δευτερόλεπτα νόμιζα ότι θα σταματήσει η καρδιά μου. Όταν βγήκα όμως, ένιωθα τόσο ζωντανή όσο δεν είχα νιώσει εδώ και μήνες.", "I started eight years ago, after a difficult period in my life. A friend took me with her one November morning. In the first few seconds I thought my heart would stop. But when I got out, I felt more alive than I had felt for months."),
  L("Δημοσιογράφος", "m", "Δεν είναι επικίνδυνο;", "Isn't it dangerous?"),
  L("Κολυμβήτρια", "f", "Μπορεί να είναι, αν δεν προσέχεις. Δεν κολυμπάμε ποτέ μόνοι, μένουμε στο νερό λίγα λεπτά και μπαίνουμε σιγά σιγά, όχι με βουτιά. Όποιος έχει πρόβλημα με την καρδιά ή την πίεση πρέπει πρώτα να ρωτήσει τον γιατρό του. Και μετά το μπάνιο, ζεστό τσάι και στεγνά ρούχα αμέσως. Η ομάδα μας έχει πια σαράντα μέλη, και ο μεγαλύτερος είναι ογδόντα δύο χρονών.", "It can be, if you're not careful. We never swim alone, we stay in the water a few minutes and go in slowly, not by diving. Anyone with a heart or blood-pressure problem should ask their doctor first. And after the swim, hot tea and dry clothes straight away. Our group now has forty members, and the oldest is eighty-two."),
 ],
 "questions": [
  Q("Πώς ένιωσε όταν βγήκε από το νερό την πρώτη φορά;", ["Πολύ άρρωστη", "Τόσο ζωντανή όσο δεν είχε νιώσει εδώ και μήνες", "Φοβισμένη", "Απογοητευμένη"], 1, "ένιωθα τόσο ζωντανή όσο δεν είχα νιώσει εδώ και μήνες"),
  Q("Ποιος από τους παρακάτω κανόνες αναφέρεται;", ["Μπαίνουν με βουτιά", "Μένουν στο νερό μία ώρα", "Δεν κολυμπούν ποτέ μόνοι", "Κολυμπούν μόνο το απόγευμα"], 2, "Δεν κολυμπάμε ποτέ μόνοι"),
  Q("Τι πρέπει να κάνει όποιος έχει πρόβλημα με την καρδιά;", ["Να ρωτήσει πρώτα τον γιατρό του", "Να κολυμπά μόνο το καλοκαίρι", "Να φορά στολή", "Να μην πίνει τσάι"], 0, "πρέπει πρώτα να ρωτήσει τον γιατρό του"),
 ],
 "gloss": {"βαθμούς": "βαθμός — degree", "περίοδο": "περίοδος — period", "δευτερόλεπτα": "δευτερόλεπτο — second", "ζωντανή": "ζωντανός — alive", "επικίνδυνο": "επικίνδυνος — dangerous", "βουτιά": "βουτιά — dive", "πίεση": "πίεση — blood pressure", "στεγνά": "στεγνός — dry", "μέλη": "μέλος — member"}
})

ITEMS.append({
 "id": "l141-vm-check-in", "title": "Νωρίς στο ξενοδοχείο", "title_en": "Early at the hotel", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει δωμάτιο σε ένα ξενοδοχείο. Ακούτε ένα μήνυμα από τη ρεσεψιόν στον τηλεφωνητή σας.",
 "script": [
  L("Ρεσεψιονίστ", "f", "Καλημέρα σας, από το ξενοδοχείο «Ακρόπολις» σας τηλεφωνώ. Λάβαμε το email σας ότι η πτήση σας φτάνει στις επτά το πρωί και ότι θα θέλατε να μπείτε στο δωμάτιο νωρίτερα. Δυστυχώς, εκείνη την ημέρα είμαστε γεμάτοι, και τα δωμάτια ελευθερώνονται μετά τις έντεκα.", "Good morning, I'm calling from the 'Akropolis' hotel. We received your email saying that your flight arrives at seven in the morning and that you'd like to get into the room earlier. Unfortunately, we're full that day, and rooms become free after eleven."),
  L("Ρεσεψιονίστ", "f", "Μπορείτε όμως να αφήσετε τις βαλίτσες σας δωρεάν στη ρεσεψιόν και να χρησιμοποιήσετε το μπάνιο του γυμναστηρίου μας για ένα ντους. Επίσης, το πρωινό σερβίρεται μέχρι τις δέκα και μισή, και με μικρή χρέωση μπορείτε να το πάρετε κι εκείνη τη μέρα.", "But you can leave your suitcases free of charge at reception and use our gym's bathroom for a shower. Also, breakfast is served until half past ten, and for a small charge you can have it that day too."),
  L("Ρεσεψιονίστ", "f", "Θα σας στείλουμε μήνυμα στο κινητό μόλις το δωμάτιό σας είναι έτοιμο. Καλό ταξίδι!", "We'll send you a message on your mobile as soon as your room is ready. Have a good trip!"),
 ],
 "questions": [
  Q("Γιατί δεν μπορείτε να μπείτε νωρίς στο δωμάτιο;", ["Γιατί το ξενοδοχείο είναι γεμάτο", "Γιατί δεν πληρώσατε", "Γιατί γίνονται εργασίες", "Γιατί η πτήση άλλαξε"], 0, "εκείνη την ημέρα είμαστε γεμάτοι"),
  Q("Τι μπορείτε να κάνετε στο μεταξύ;", ["Να κοιμηθείτε στο λόμπι", "Να αφήσετε τις βαλίτσες και να κάνετε ντους στο γυμναστήριο", "Να πάρετε ένα άλλο δωμάτιο δωρεάν", "Να ακυρώσετε χωρίς χρέωση"], 1, "Μπορείτε όμως να αφήσετε τις βαλίτσες σας δωρεάν στη ρεσεψιόν"),
  Q("Πώς θα μάθετε ότι το δωμάτιο είναι έτοιμο;", ["Θα ρωτάτε κάθε ώρα", "Θα σας πάρουν τηλέφωνο", "Θα σας στείλουν μήνυμα στο κινητό", "Θα σας στείλουν email"], 2, "Θα σας στείλουμε μήνυμα στο κινητό"),
 ],
 "gloss": {"ρεσεψιόν": "ρεσεψιόν — reception", "Λάβαμε": "λαμβάνω — to receive", "ελευθερώνονται": "ελευθερώνομαι — to become free", "βαλίτσες": "βαλίτσα — suitcase", "ντους": "ντους — shower", "σερβίρεται": "σερβίρομαι — to be served", "χρέωση": "χρέωση — charge"}
})

ITEMS.append({
 "id": "l141-ann-therino", "title": "Βροχή στο θερινό σινεμά", "title_en": "Rain at the open-air cinema", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα θερινό σινεμά και ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Υπάλληλος", "m", "Καλησπέρα σας. Λόγω της βροχής που προβλέπεται να αρχίσει σε λίγα λεπτά, η αποψινή προβολή της ταινίας «Η νύχτα των αστεριών» δεν θα πραγματοποιηθεί στον κήπο.", "Good evening. Because of the rain forecast to start in a few minutes, tonight's screening of the film 'The Night of the Stars' will not take place in the garden."),
  L("Υπάλληλος", "m", "Όσοι έχουν εισιτήριο μπορούν να παρακολουθήσουν την ταινία στη χειμερινή αίθουσα, στον πρώτο όροφο του διπλανού κτιρίου, στις δέκα και τέταρτο, δηλαδή με ένα τέταρτο καθυστέρηση. Η αίθουσα έχει διακόσιες θέσεις, οπότε οι θέσεις δεν θα είναι αριθμημένες.", "Ticket holders can watch the film in the winter hall, on the first floor of the building next door, at a quarter past ten, that is, fifteen minutes late. The hall has two hundred seats, so seats will not be numbered."),
  L("Υπάλληλος", "m", "Όσοι προτιμούν να έρθουν άλλη βραδιά μπορούν να ανταλλάξουν το εισιτήριό τους στο ταμείο μέχρι το τέλος της εβδομάδας. Ευχαριστούμε για την κατανόηση.", "Those who'd rather come another evening can exchange their ticket at the box office until the end of the week. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί δεν θα γίνει η προβολή στον κήπο;", ["Γιατί χάλασε η μηχανή προβολής", "Λόγω της βροχής", "Γιατί δεν ήρθε η ταινία", "Λόγω θορύβου"], 1, "Λόγω της βροχής"),
  Q("Πότε θα αρχίσει η ταινία στη χειμερινή αίθουσα;", ["Στις δέκα", "Στις εννιά και μισή", "Στις δέκα και τέταρτο", "Στις έντεκα"], 2, "στις δέκα και τέταρτο"),
  Q("Τι μπορούν να κάνουν όσοι θέλουν να έρθουν άλλη βραδιά;", ["Να ανταλλάξουν το εισιτήριο στο ταμείο μέχρι το τέλος της εβδομάδας", "Να πάρουν πίσω τα χρήματά τους", "Να έρθουν μόνο το Σάββατο", "Τίποτα"], 0, "μπορούν να ανταλλάξουν το εισιτήριό τους στο ταμείο μέχρι το τέλος της εβδομάδας"),
 ],
 "gloss": {"θερινό σινεμά": "θερινό σινεμά — open-air cinema", "προβλέπεται": "προβλέπεται — it is forecast", "προβολή": "προβολή — screening", "πραγματοποιηθεί": "πραγματοποιούμαι — to take place", "χειμερινή αίθουσα": "χειμερινή αίθουσα — indoor (winter) cinema hall", "αριθμημένες": "αριθμημένος — numbered", "ανταλλάξουν": "ανταλλάσσω — to exchange", "ταμείο": "ταμείο — box office", "κατανόηση": "κατανόηση — understanding"}
})

ITEMS.append({
 "id": "l141-dia-kleidia", "title": "Τα κλειδιά μέσα στο αυτοκίνητο", "title_en": "Keys locked in the car", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα τηλεφώνημα ανάμεσα σε μια οδηγό και μια υπάλληλο της οδικής βοήθειας.",
 "script": [
  L("Οδηγός", "f", "Καλησπέρα. Έκλεισα την πόρτα του αυτοκινήτου και τα κλειδιά έμειναν μέσα, πάνω στο κάθισμα. Το χειρότερο είναι ότι η μηχανή δουλεύει ακόμα.", "Good evening. I closed the car door and the keys stayed inside, on the seat. The worst thing is that the engine is still running."),
  L("Υπάλληλος", "f", "Μην ανησυχείτε, συμβαίνει πιο συχνά απ' ό,τι νομίζετε. Πού βρίσκεστε ακριβώς; Και μου λέτε τον αριθμό κυκλοφορίας;", "Don't worry, it happens more often than you think. Where exactly are you? And could you tell me the registration number?"),
  L("Οδηγός", "f", "Είμαι στο πάρκινγκ του σούπερ μάρκετ, στην έξοδο της εθνικής οδού για τη Λαμία. ΙΚΡ 4582.", "I'm in the supermarket car park, at the exit of the national road for Lamia. IKR 4582."),
  L("Υπάλληλος", "f", "Εντάξει. Ο τεχνικός μας θα είναι εκεί σε περίπου σαράντα λεπτά. Θα ανοίξει την πόρτα χωρίς να προκαλέσει ζημιά. Θα σας ζητήσει όμως την ταυτότητά σας και την άδεια κυκλοφορίας, για να βεβαιωθεί ότι το αυτοκίνητο είναι δικό σας. Αν η άδεια είναι μέσα στο αυτοκίνητο, θα τη δείξετε μόλις ανοίξει.", "All right. Our technician will be there in about forty minutes. He'll open the door without causing damage. But he'll ask for your ID and the vehicle registration document, to make sure the car is yours. If the document is inside the car, you'll show it as soon as he opens it."),
 ],
 "questions": [
  Q("Τι πρόβλημα έχει η οδηγός;", ["Έμεινε από βενζίνη", "Τα κλειδιά έμειναν μέσα στο αυτοκίνητο", "Έσκασε ένα λάστιχο", "Έχασε το κινητό της"], 1, "τα κλειδιά έμειναν μέσα, πάνω στο κάθισμα"),
  Q("Σε πόση ώρα θα φτάσει ο τεχνικός;", ["Σε δέκα λεπτά", "Σε δύο ώρες", "Σε περίπου σαράντα λεπτά", "Αύριο το πρωί"], 2, "θα είναι εκεί σε περίπου σαράντα λεπτά"),
  Q("Γιατί θα ζητήσει ο τεχνικός την ταυτότητα και την άδεια κυκλοφορίας;", ["Για να βεβαιωθεί ότι το αυτοκίνητο είναι δικό της", "Για να γράψει πρόστιμο", "Για να υπολογίσει το κόστος", "Για την ασφάλεια του αυτοκινήτου"], 0, "για να βεβαιωθεί ότι το αυτοκίνητο είναι δικό σας"),
 ],
 "gloss": {"οδικής βοήθειας": "οδική βοήθεια — roadside assistance", "κάθισμα": "κάθισμα — seat", "μηχανή": "μηχανή — engine", "αριθμό κυκλοφορίας": "αριθμός κυκλοφορίας — registration number", "εθνικής οδού": "εθνική οδός — national road, motorway", "προκαλέσει": "προκαλώ — to cause", "ζημιά": "ζημιά — damage", "άδεια κυκλοφορίας": "άδεια κυκλοφορίας — vehicle registration document", "βεβαιωθεί": "βεβαιώνομαι — to make sure"}
})

ITEMS.append({
 "id": "l141-dia-antallagi-spition", "title": "Ανταλλαγή σπιτιών για διακοπές", "title_en": "A home swap for the holidays", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά για τις καλοκαιρινές διακοπές.",
 "script": [
  L("Ηλέκτρα", "f", "Βρήκα μια οικογένεια από τη Λυών που θέλει να ανταλλάξουμε σπίτια τον Αύγουστο. Αυτοί έρχονται στο δικό μας, εμείς πάμε στο δικό τους, και κανείς δεν πληρώνει ξενοδοχείο.", "I found a family from Lyon who want to swap homes with us in August. They come to ours, we go to theirs, and nobody pays for a hotel."),
  L("Γιάννης", "m", "Και θα αφήσουμε αγνώστους να κοιμούνται στο κρεβάτι μας και να χρησιμοποιούν την κουζίνα μας; Δεν ξέρω...", "And we'll let strangers sleep in our bed and use our kitchen? I don't know..."),
  L("Ηλέκτρα", "f", "Δεν είναι τελείως άγνωστοι. Η πλατφόρμα έχει κριτικές από άλλες οικογένειες, και αυτοί έχουν κάνει ήδη πέντε ανταλλαγές, όλες με άριστες κριτικές. Μιλήσαμε και σε βιντεοκλήση· έχουν δύο παιδιά στην ηλικία των δικών μας.", "They're not complete strangers. The platform has reviews from other families, and they've already done five swaps, all with excellent reviews. We also talked on a video call; they have two children the same age as ours."),
  L("Γιάννης", "m", "Εντάξει, αλλά θα κλειδώσουμε τη μικρή αποθήκη με τα προσωπικά μας πράγματα. Και θα τους ζητήσουμε να ποτίζουν τις γλάστρες, αφού θα μείνουν τρεις εβδομάδες.", "All right, but we'll lock the little storeroom with our personal things. And we'll ask them to water the plants, since they'll be staying three weeks."),
 ],
 "questions": [
  Q("Ποιο είναι το βασικό πλεονέκτημα της ανταλλαγής, σύμφωνα με την Ηλέκτρα;", ["Ότι κανείς δεν πληρώνει ξενοδοχείο", "Ότι μαθαίνουν γαλλικά", "Ότι το σπίτι τους θα βαφτεί", "Ότι θα πάρουν χρήματα"], 0, "κανείς δεν πληρώνει ξενοδοχείο"),
  Q("Γιατί λέει η Ηλέκτρα ότι δεν είναι τελείως άγνωστοι;", ["Γιατί είναι συγγενείς", "Γιατί έχουν άριστες κριτικές από πέντε ανταλλαγές και μίλησαν σε βιντεοκλήση", "Γιατί τους γνώρισαν πέρσι", "Γιατί είναι συνάδελφοι"], 1, "αυτοί έχουν κάνει ήδη πέντε ανταλλαγές, όλες με άριστες κριτικές"),
  Q("Τι θα κάνει ο Γιάννης πριν φύγουν;", ["Θα πουλήσει το αυτοκίνητο", "Θα αλλάξει κλειδαριές", "Θα κλειδώσει τη μικρή αποθήκη με τα προσωπικά τους πράγματα", "Θα πάρει μαζί τις γλάστρες"], 2, "θα κλειδώσουμε τη μικρή αποθήκη με τα προσωπικά μας πράγματα"),
 ],
 "gloss": {"ανταλλάξουμε": "ανταλλάσσω — to swap, exchange", "αγνώστους": "άγνωστος — stranger", "πλατφόρμα": "πλατφόρμα — platform (website)", "κριτικές": "κριτική — review", "άριστες": "άριστος — excellent", "βιντεοκλήση": "βιντεοκλήση — video call", "κλειδώσουμε": "κλειδώνω — to lock", "αποθήκη": "αποθήκη — storeroom", "ποτίζουν": "ποτίζω — to water", "γλάστρες": "γλάστρα — flowerpot, plant"}
})

ITEMS.append({
 "id": "l141-news-orchistra", "title": "Μια ορχήστρα χωρίς σύνορα", "title_en": "An orchestra without borders", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια πολιτιστική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Σαράντα παιδιά από δεκαπέντε χώρες, ανάμεσά τους από τη Συρία, το Αφγανιστάν και την Ελλάδα, έδωσαν χθες την πρώτη τους συναυλία στο δημοτικό θέατρο της πόλης. Η νεανική ορχήστρα δημιουργήθηκε πριν από δύο χρόνια από μια ομάδα μουσικών που διδάσκουν εθελοντικά.", "Forty children from fifteen countries, among them from Syria, Afghanistan and Greece, gave their first concert yesterday at the town's municipal theatre. The youth orchestra was set up two years ago by a group of musicians who teach as volunteers."),
  L("Ρεπόρτερ", "f", "Τα περισσότερα παιδιά δεν είχαν πιάσει ποτέ μουσικό όργανο. Τα βιολιά, τα τσέλα και τα φλάουτα τα δώρισαν ωδεία και ιδιώτες από όλη τη χώρα. Οι πρόβες γίνονται δύο φορές την εβδομάδα, και, όπως λένε οι δάσκαλοι, εκεί τα παιδιά μαθαίνουν και ελληνικά, γιατί οι οδηγίες δίνονται στη γλώσσα που έχουν όλα κοινή.", "Most of the children had never held a musical instrument. The violins, cellos and flutes were donated by conservatories and private individuals from all over the country. Rehearsals take place twice a week, and, as the teachers say, that's where the children also learn Greek, because instructions are given in the language they all share."),
  L("Ρεπόρτερ", "f", "Το πρόγραμμα της συναυλίας περιλάμβανε κλασικά έργα, αλλά και τραγούδια από τις πατρίδες των παιδιών. Το κοινό, όρθιο, χειροκροτούσε για πέντε λεπτά. Τον Μάιο η ορχήστρα θα παίξει στη Θεσσαλονίκη.", "The concert programme included classical works, but also songs from the children's home countries. The audience, on its feet, applauded for five minutes. In May the orchestra will play in Thessaloniki."),
 ],
 "questions": [
  Q("Ποιος δημιούργησε την ορχήστρα;", ["Ο δήμος", "Μια ομάδα μουσικών που διδάσκουν εθελοντικά", "Οι γονείς των παιδιών", "Ένα ωδείο"], 1, "από μια ομάδα μουσικών που διδάσκουν εθελοντικά"),
  Q("Από πού προέρχονται τα μουσικά όργανα;", ["Τα αγόρασε το κράτος", "Τα έφεραν τα παιδιά από τις πατρίδες τους", "Τα δώρισαν ωδεία και ιδιώτες", "Τα νοικιάζουν"], 2, "τα δώρισαν ωδεία και ιδιώτες από όλη τη χώρα"),
  Q("Γιατί τα παιδιά μαθαίνουν και ελληνικά στις πρόβες;", ["Γιατί οι οδηγίες δίνονται στη γλώσσα που έχουν όλα κοινή", "Γιατί τραγουδούν μόνο ελληνικά τραγούδια", "Γιατί γράφουν εξετάσεις", "Γιατί το ζητούν οι γονείς"], 0, "γιατί οι οδηγίες δίνονται στη γλώσσα που έχουν όλα κοινή"),
 ],
 "gloss": {"συναυλία": "συναυλία — concert", "νεανική": "νεανικός — youth (adj.)", "ορχήστρα": "ορχήστρα — orchestra", "εθελοντικά": "εθελοντικά — as volunteers", "μουσικό όργανο": "μουσικό όργανο — musical instrument", "τσέλα": "τσέλο — cello", "φλάουτα": "φλάουτο — flute", "ωδεία": "ωδείο — conservatory, music school", "πρόβες": "πρόβα — rehearsal", "χειροκροτούσε": "χειροκροτώ — to applaud"}
})

ITEMS.append({
 "id": "l141-vm-skafos", "title": "Οι εξετάσεις για το δίπλωμα σκάφους", "title_en": "The boat licence exams", "type": "voicemail", "level": "B2",
 "context_el": "Παρακολουθείτε μαθήματα για δίπλωμα ταχύπλοου σκάφους. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Εκπαιδευτής", "m", "Καλησπέρα, ο Στράτος είμαι, από τη σχολή ναυτικής εκπαίδευσης. Το Λιμεναρχείο όρισε την ημερομηνία των εξετάσεων: θα γίνουν την Τετάρτη είκοσι δύο του μήνα. Η θεωρία το πρωί στις εννιά, και η πρακτική εξέταση στο λιμάνι το μεσημέρι.", "Good evening, it's Stratos from the boating school. The Port Authority has set the exam date: they'll be on Wednesday the twenty-second of the month. The theory in the morning at nine, and the practical exam at the harbour at midday."),
  L("Εκπαιδευτής", "m", "Επειδή χάσατε δύο μαθήματα πρακτικής, σας προτείνω να κάνουμε μία επιπλέον ώρα στο σκάφος το Σάββατο το πρωί, για να εξασκηθείτε στο δέσιμο κόμπων και στον ελλιμενισμό. Εκεί κόβονται οι περισσότεροι υποψήφιοι.", "Because you missed two practical lessons, I suggest we do one extra hour on the boat on Saturday morning, so you can practise tying knots and berthing. That's where most candidates fail."),
  L("Εκπαιδευτής", "m", "Μην ξεχάσετε να φέρετε την ταυτότητα και το πιστοποιητικό υγείας από τον γιατρό. Χωρίς αυτό δεν θα σας αφήσουν να εξεταστείτε. Πάρτε με τηλέφωνο να μου πείτε για το Σάββατο.", "Don't forget to bring your ID card and the health certificate from the doctor. Without it they won't let you take the exam. Give me a call to tell me about Saturday."),
 ],
 "questions": [
  Q("Πότε θα γίνει η πρακτική εξέταση;", ["Την Τετάρτη στις εννιά το πρωί", "Την Τετάρτη το μεσημέρι", "Το Σάββατο το πρωί", "Την επόμενη εβδομάδα"], 1, "η πρακτική εξέταση στο λιμάνι το μεσημέρι"),
  Q("Γιατί σας προτείνει μια επιπλέον ώρα;", ["Γιατί κόψατε στη θεωρία", "Γιατί άλλαξε το σκάφος", "Γιατί χάσατε δύο μαθήματα πρακτικής", "Γιατί το ζήτησε το Λιμεναρχείο"], 2, "Επειδή χάσατε δύο μαθήματα πρακτικής"),
  Q("Τι πρέπει να φέρετε απαραίτητα;", ["Την ταυτότητα και το πιστοποιητικό υγείας", "Ένα σωσίβιο", "Το βιβλίο της θεωρίας", "Δύο φωτογραφίες"], 0, "να φέρετε την ταυτότητα και το πιστοποιητικό υγείας από τον γιατρό"),
 ],
 "gloss": {"δίπλωμα": "δίπλωμα — licence", "ταχύπλοου σκάφους": "ταχύπλοο σκάφος — speedboat", "Λιμεναρχείο": "λιμεναρχείο — port authority", "όρισε": "ορίζω — to set, fix", "θεωρία": "θεωρία — theory", "εξασκηθείτε": "εξασκούμαι — to practise", "κόμπων": "κόμπος — knot", "ελλιμενισμό": "ελλιμενισμός — berthing, mooring", "υποψήφιοι": "υποψήφιος — candidate", "πιστοποιητικό υγείας": "πιστοποιητικό υγείας — health certificate"}
})

ITEMS.append({
 "id": "l141-int-paidiki-chorodia", "title": "Είκοσι παιδιά, μία φωνή", "title_en": "Twenty children, one voice", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή για τη μουσική εκπαίδευση.",
 "script": [
  L("Δημοσιογράφος", "m", "Διευθύνετε μια παιδική χορωδία εδώ και δεκαπέντε χρόνια. Τι μαθαίνουν τα παιδιά, εκτός από το τραγούδι;", "You've been conducting a children's choir for fifteen years. What do the children learn, apart from singing?"),
  L("Μαέστρος", "f", "Κυρίως να ακούνε. Σε μια χορωδία, αν κάποιος τραγουδά πιο δυνατά από τους άλλους, χαλάει το αποτέλεσμα. Τα παιδιά μαθαίνουν να προσαρμόζουν τη φωνή τους στη φωνή του διπλανού τους. Αυτό, πιστεύω, είναι μάθημα και για τη ζωή.", "Mainly to listen. In a choir, if someone sings louder than the others, it spoils the result. The children learn to adjust their voice to the voice of the child next to them. That, I believe, is a lesson for life as well."),
  L("Δημοσιογράφος", "m", "Δέχεστε όλα τα παιδιά;", "Do you accept all children?"),
  L("Μαέστρος", "f", "Όλα, χωρίς ακρόαση. Μερικά έρχονται φάλτσα και ντροπαλά, και σε έναν χρόνο είναι αυτά που τραγουδούν τα σόλο. Το μόνο που ζητάμε είναι να έρχονται σε κάθε πρόβα. Αν λείπουν συχνά, δυσκολεύεται όλη η ομάδα, γιατί η κάθε φωνή έχει τη θέση της.", "All of them, without an audition. Some come out of tune and shy, and within a year they're the ones singing the solos. The only thing we ask is that they come to every rehearsal. If they're often absent, the whole group struggles, because every voice has its place."),
 ],
 "questions": [
  Q("Τι μαθαίνουν κυρίως τα παιδιά, κατά τη μαέστρο;", ["Να διαβάζουν νότες", "Να ακούνε και να προσαρμόζουν τη φωνή τους στους άλλους", "Να τραγουδούν πιο δυνατά", "Να παίζουν πιάνο"], 1, "Κυρίως να ακούνε"),
  Q("Πώς γίνεται η επιλογή των παιδιών;", ["Με ακρόαση", "Με σύσταση από το σχολείο", "Δεν γίνεται επιλογή· δέχονται όλα τα παιδιά", "Με κλήρωση"], 2, "Όλα, χωρίς ακρόαση"),
  Q("Τι ζητούν από τα παιδιά;", ["Να έρχονται σε κάθε πρόβα", "Να έχουν μουσικό όργανο", "Να πληρώνουν συνδρομή", "Να τραγουδούν σόλο"], 0, "Το μόνο που ζητάμε είναι να έρχονται σε κάθε πρόβα"),
 ],
 "gloss": {"Διευθύνετε": "διευθύνω — to conduct, direct", "χορωδία": "χορωδία — choir", "αποτέλεσμα": "αποτέλεσμα — result", "προσαρμόζουν": "προσαρμόζω — to adjust", "ακρόαση": "ακρόαση — audition", "φάλτσα": "φάλτσος — out of tune", "ντροπαλά": "ντροπαλός — shy", "σόλο": "σόλο — solo", "πρόβα": "πρόβα — rehearsal"}
})

ITEMS.append({
 "id": "l141-c1-moravec", "title": "Το παράδοξο του Μοράβετς", "title_en": "Moravec's paradox", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ομιλία για την τεχνητή νοημοσύνη.",
 "script": [
  L("Ομιλητής", "m", "Τη δεκαετία του 1980, ο ρομποτικός Χανς Μοράβετς και άλλοι ερευνητές διατύπωσαν μια παρατήρηση που ακούγεται αντιφατική: για έναν υπολογιστή είναι σχετικά εύκολο να λύσει προβλήματα που εμείς θεωρούμε δύσκολα, όπως ένα τεστ λογικής ή μια παρτίδα σκάκι, και εξαιρετικά δύσκολο να κάνει όσα ένα παιδί ενός έτους κάνει χωρίς προσπάθεια: να αναγνωρίσει ένα πρόσωπο, να πιάσει ένα παιχνίδι, να περπατήσει σε ανώμαλο έδαφος.", "In the 1980s, the roboticist Hans Moravec and other researchers formulated an observation that sounds contradictory: for a computer it is relatively easy to solve problems that we consider difficult, such as a logic test or a game of chess, and extremely difficult to do what a one-year-old child does effortlessly: recognise a face, grab a toy, walk on uneven ground."),
  L("Ομιλητής", "m", "Η εξήγηση που πρότεινε ο ίδιος ο Μοράβετς είναι εξελικτική. Οι αισθητηριακές και κινητικές μας ικανότητες είναι προϊόν εκατομμυρίων ετών εξέλιξης· έχουν τελειοποιηθεί τόσο, ώστε λειτουργούν ασυνείδητα και μας φαίνονται απλές. Αντίθετα, η αφηρημένη σκέψη, τα μαθηματικά και η λογική είναι πολύ πρόσφατα επιτεύγματα του είδους μας, και γι' αυτό τα βιώνουμε ως δύσκολα.", "The explanation Moravec himself proposed is evolutionary. Our sensory and motor abilities are the product of millions of years of evolution; they have been perfected so much that they work unconsciously and seem simple to us. By contrast, abstract thought, mathematics and logic are very recent achievements of our species, and that is why we experience them as difficult."),
  L("Ομιλητής", "m", "Τα τελευταία χρόνια η τεχνητή νοημοσύνη έχει κάνει εντυπωσιακά βήματα και στην όραση και στη γλώσσα, οπότε κάποιοι υποστηρίζουν ότι το παράδοξο έχει αρχίσει να ξεθωριάζει. Όμως ένα ρομπότ που διπλώνει ρούχα ή καθαρίζει ένα ακατάστατο δωμάτιο με την ευελιξία ενός ανθρώπου παραμένει, προς το παρόν, μεγαλύτερη πρόκληση από ένα πρόγραμμα που γράφει ποιήματα. Ίσως το μάθημα είναι ότι αυτό που λέμε «εύκολο» μάς λέει περισσότερα για τη δική μας ιστορία παρά για τη φύση του προβλήματος.", "In recent years artificial intelligence has made impressive strides in vision and language too, so some argue that the paradox has begun to fade. But a robot that folds clothes or tidies a messy room with a human's dexterity remains, for now, a bigger challenge than a program that writes poems. Perhaps the lesson is that what we call 'easy' tells us more about our own history than about the nature of the problem."),
 ],
 "questions": [
  Q("Τι λέει το παράδοξο του Μοράβετς;", ["Ότι οι υπολογιστές δεν θα παίξουν ποτέ σκάκι", "Ότι για τους υπολογιστές είναι εύκολα όσα εμείς θεωρούμε δύσκολα και δύσκολα όσα ένα μωρό κάνει χωρίς προσπάθεια", "Ότι τα παιδιά μαθαίνουν πιο γρήγορα από τους ενήλικες", "Ότι η λογική είναι η πιο αρχαία ικανότητα"], 1, "για έναν υπολογιστή είναι σχετικά εύκολο να λύσει προβλήματα που εμείς θεωρούμε δύσκολα"),
  Q("Πώς εξηγεί ο Μοράβετς το παράδοξο;", ["Με την έλλειψη χρημάτων για έρευνα", "Με την κακή εκπαίδευση των υπολογιστών", "Με την εξέλιξη: οι κινητικές ικανότητες τελειοποιήθηκαν σε εκατομμύρια χρόνια", "Με τη δυσκολία του σκακιού"], 2, "Η εξήγηση που πρότεινε ο ίδιος ο Μοράβετς είναι εξελικτική"),
  Q("Γιατί βιώνουμε τα μαθηματικά ως δύσκολα;", ["Γιατί είναι πολύ πρόσφατα επιτεύγματα του είδους μας", "Γιατί δεν τα διδάσκουμε καλά", "Γιατί τα χρησιμοποιούμε σπάνια", "Γιατί απαιτούν υπολογιστή"], 0, "είναι πολύ πρόσφατα επιτεύγματα του είδους μας"),
  Q("Τι παραμένει, κατά τον ομιλητή, μεγάλη πρόκληση;", ["Ένα πρόγραμμα που γράφει ποιήματα", "Η αναγνώριση της γλώσσας", "Μια παρτίδα σκάκι", "Ένα ρομπότ που διπλώνει ρούχα ή καθαρίζει ένα ακατάστατο δωμάτιο"], 3, "ένα ρομπότ που διπλώνει ρούχα ή καθαρίζει ένα ακατάστατο δωμάτιο"),
 ],
 "gloss": {"τεχνητή νοημοσύνη": "τεχνητή νοημοσύνη — artificial intelligence", "ρομποτικός": "ρομποτικός — roboticist", "αντιφατική": "αντιφατικός — contradictory", "παρτίδα": "παρτίδα — game (of chess)", "ανώμαλο": "ανώμαλος — uneven", "εξελικτική": "εξελικτικός — evolutionary", "αισθητηριακές": "αισθητηριακός — sensory", "κινητικές": "κινητικός — motor", "ασυνείδητα": "ασυνείδητα — unconsciously", "αφηρημένη": "αφηρημένος — abstract", "επιτεύγματα": "επίτευγμα — achievement", "ξεθωριάζει": "ξεθωριάζω — to fade", "ευελιξία": "ευελιξία — dexterity, flexibility", "πρόκληση": "πρόκληση — challenge"}
})

ITEMS.append({
 "id": "l141-c1-katara-niki", "title": "Η «κατάρα του νικητή»", "title_en": "The 'winner's curse'", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια οικονομική εκπομπή στο ραδιόφωνο.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι εννοούν οι οικονομολόγοι όταν μιλούν για την «κατάρα του νικητή»;", "What do economists mean when they talk about the 'winner's curse'?"),
  L("Οικονομολόγος", "m", "Τον όρο τον χρησιμοποίησαν το 1971 τρεις μηχανικοί μιας αμερικανικής πετρελαϊκής εταιρείας. Είχαν παρατηρήσει ότι οι εταιρείες που κέρδιζαν τους πλειστηριασμούς για τα δικαιώματα γεώτρησης στον Κόλπο του Μεξικού είχαν συχνά απογοητευτικά κέρδη. Η εξήγηση ήταν απλή αλλά ενοχλητική: κανείς δεν ήξερε με βεβαιότητα πόσο πετρέλαιο υπήρχε, και κέρδιζε συνήθως εκείνος που είχε κάνει την πιο αισιόδοξη, δηλαδή την πιο υπερβολική, εκτίμηση.", "The term was used in 1971 by three engineers at an American oil company. They had observed that the companies that won auctions for drilling rights in the Gulf of Mexico often had disappointing profits. The explanation was simple but uncomfortable: nobody knew for certain how much oil there was, and the winner was usually the one who had made the most optimistic, that is, the most exaggerated, estimate."),
  L("Δημοσιογράφος", "f", "Δηλαδή το να κερδίσεις είναι από μόνο του κακό σημάδι.", "So winning is in itself a bad sign."),
  L("Οικονομολόγος", "m", "Όταν η αξία του αντικειμένου είναι ίδια για όλους αλλά αβέβαιη, ναι. Υπάρχει ένα κλασικό πείραμα σε πανεπιστημιακές αίθουσες: ο καθηγητής δείχνει ένα βάζο με κέρματα και ζητά από τους φοιτητές να κάνουν προσφορές. Ο μέσος όρος των προσφορών είναι συνήθως χαμηλότερος από την πραγματική αξία, αλλά η νικητήρια προσφορά σχεδόν πάντα την ξεπερνά. Ο νικητής, με άλλα λόγια, πληρώνει ακριβώς επειδή έκανε το μεγαλύτερο λάθος.", "When the value of the item is the same for everyone but uncertain, yes. There's a classic experiment in university lecture halls: the professor shows a jar of coins and asks the students to bid. The average bid is usually lower than the real value, but the winning bid almost always exceeds it. The winner, in other words, pays precisely because they made the biggest mistake."),
  L("Δημοσιογράφος", "f", "Και πώς προστατεύεται κανείς;", "And how does one protect oneself?"),
  L("Οικονομολόγος", "m", "Με μια σκέψη που μοιάζει παράλογη: πριν κάνεις προσφορά, να υποθέσεις ότι θα κερδίσεις, και να αναρωτηθείς τι σημαίνει αυτό για την εκτίμησή σου. Αν ισχύει για πετρελαϊκές εταιρείες, ισχύει και για όποιον «κερδίζει» ένα διαμέρισμα σε έναν άγριο διαγωνισμό προσφορών.", "With a thought that seems absurd: before you bid, assume that you will win, and ask yourself what that means for your estimate. If it applies to oil companies, it also applies to anyone who 'wins' a flat in a fierce bidding war."),
 ],
 "questions": [
  Q("Τι είχαν παρατηρήσει οι τρεις μηχανικοί το 1971;", ["Ότι το πετρέλαιο στον Κόλπο του Μεξικού είχε τελειώσει", "Ότι οι νικητές των πλειστηριασμών είχαν συχνά απογοητευτικά κέρδη", "Ότι οι πλειστηριασμοί ήταν παράνομοι", "Ότι οι μικρές εταιρείες κέρδιζαν πάντα"], 1, "είχαν συχνά απογοητευτικά κέρδη"),
  Q("Ποιος κέρδιζε συνήθως τους πλειστηριασμούς;", ["Η μεγαλύτερη εταιρεία", "Η εταιρεία με τους καλύτερους μηχανικούς", "Εκείνος που είχε κάνει την πιο αισιόδοξη εκτίμηση", "Εκείνος που έφτανε πρώτος"], 2, "κέρδιζε συνήθως εκείνος που είχε κάνει την πιο αισιόδοξη, δηλαδή την πιο υπερβολική, εκτίμηση"),
  Q("Τι δείχνει το πείραμα με το βάζο;", ["Ότι η νικητήρια προσφορά σχεδόν πάντα ξεπερνά την πραγματική αξία", "Ότι οι φοιτητές μαντεύουν σωστά", "Ότι ο μέσος όρος είναι πάντα υπερβολικός", "Ότι κανείς δεν θέλει να κάνει προσφορά"], 0, "η νικητήρια προσφορά σχεδόν πάντα την ξεπερνά"),
  Q("Τι συμβουλεύει ο οικονομολόγος;", ["Να μην κάνουμε ποτέ προσφορές", "Να προσφέρουμε πάντα λιγότερο από τον μέσο όρο", "Να συμβουλευόμαστε έναν μηχανικό", "Να υποθέτουμε ότι θα κερδίσουμε και να αναρωτιόμαστε τι σημαίνει αυτό για την εκτίμησή μας"], 3, "να υποθέσεις ότι θα κερδίσεις, και να αναρωτηθείς τι σημαίνει αυτό για την εκτίμησή σου"),
 ],
 "gloss": {"κατάρα": "κατάρα — curse", "πετρελαϊκής": "πετρελαϊκός — oil (adj.)", "πλειστηριασμούς": "πλειστηριασμός — auction", "γεώτρησης": "γεώτρηση — drilling", "απογοητευτικά": "απογοητευτικός — disappointing", "βεβαιότητα": "βεβαιότητα — certainty", "αισιόδοξη": "αισιόδοξος — optimistic", "εκτίμηση": "εκτίμηση — estimate", "αβέβαιη": "αβέβαιος — uncertain", "κέρματα": "κέρμα — coin", "προσφορές": "προσφορά — bid, offer", "νικητήρια": "νικητήριος — winning", "παράλογη": "παράλογος — absurd"}
})

rnd = random.Random(141)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-141.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
