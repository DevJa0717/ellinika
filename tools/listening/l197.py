# Source for library/listening/listening-197.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l197.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l197-ann-apografi-vivliothikis", "title": "Η δημοτική βιβλιοθήκη κλείνει για απογραφή", "title_en": "The municipal library closes for stocktaking", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα της δημοτικής βιβλιοθήκης.",
 "script": [
  L("Βιβλιοθηκονόμος", "f", "Αγαπητοί αναγνώστες, σας ενημερώνουμε ότι η βιβλιοθήκη θα παραμείνει κλειστή από τη Δευτέρα 24 έως και την Παρασκευή 28 Νοεμβρίου λόγω της ετήσιας απογραφής. Εκείνη την εβδομάδα το προσωπικό θα ελέγξει όλα τα ράφια και θα καταγράψει ποια βιβλία λείπουν ή χρειάζονται επιδιόρθωση.", "Dear readers, we inform you that the library will remain closed from Monday the 24th to Friday the 28th of November inclusive for the annual stocktaking. That week the staff will check all the shelves and record which books are missing or need repair."),
  L("Βιβλιοθηκονόμος", "f", "Όσα βιβλία λήγουν μέσα σε αυτές τις μέρες παίρνουν αυτόματα παράταση μέχρι τις 5 Δεκεμβρίου, χωρίς πρόστιμο. Αν θέλετε να επιστρέψετε κάποιο βιβλίο, μπορείτε να το αφήσετε στο κουτί επιστροφών δίπλα στην κεντρική είσοδο, που θα λειτουργεί κανονικά.", "Books that are due during these days automatically get an extension until 5 December, with no fine. If you want to return a book, you can leave it in the returns box next to the main entrance, which will work as normal."),
  L("Βιβλιοθηκονόμος", "f", "Η αναγνωστική αίθουσα του πρώτου ορόφου θα ανοίξει ξανά μία μέρα αργότερα, το Σάββατο, επειδή θα βαφτεί. Σας ευχαριστούμε για την κατανόηση.", "The first-floor reading room will reopen one day later, on Saturday, because it will be painted. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί κλείνει η βιβλιοθήκη;", ["Για ανακαίνιση", "Για την ετήσια απογραφή", "Λόγω απεργίας", "Λόγω διακοπών"], 1, "λόγω της ετήσιας απογραφής"),
  Q("Τι γίνεται με τα βιβλία που λήγουν εκείνη την εβδομάδα;", ["Πρέπει να επιστραφούν την Παρασκευή", "Πληρώνουν πρόστιμο", "Παίρνουν αυτόματα παράταση", "Ανανεώνονται μόνο ηλεκτρονικά"], 2, "παίρνουν αυτόματα παράταση"),
  Q("Γιατί η αναγνωστική αίθουσα θα ανοίξει αργότερα;", ["Γιατί θα βαφτεί", "Γιατί θα αλλάξουν τα ράφια", "Γιατί θα γίνει μια εκδήλωση", "Γιατί λείπει προσωπικό"], 0, "επειδή θα βαφτεί"),
 ],
 "gloss": {"απογραφής": "απογραφή — stocktaking, inventory", "επιδιόρθωση": "επιδιόρθωση — repair", "παράταση": "παράταση — extension", "πρόστιμο": "πρόστιμο — fine", "αναγνωστική": "αναγνωστική αίθουσα — reading room"},
})

ITEMS.append({
 "id": "l197-int-iliaka-rologia", "title": "Ο κατασκευαστής ηλιακών ρολογιών", "title_en": "The sundial maker", "type": "interview", "level": "B2",
 "context_el": "Συνέντευξη με έναν μαρμαρά από την Τήνο που φτιάχνει ηλιακά ρολόγια.",
 "script": [
  L("Δημοσιογράφος", "f", "Ποιος παραγγέλνει σήμερα ένα ηλιακό ρολόι;", "Who orders a sundial today?"),
  L("Μαρμαράς", "m", "Περισσότεροι απ' όσους φαντάζεστε. Κυρίως άνθρωποι που φτιάχνουν ένα σπίτι στο νησί και θέλουν κάτι στον τοίχο της αυλής που να μη χρειάζεται μπαταρία. Έχω φτιάξει και για σχολεία, γιατί είναι ένας πολύ καλός τρόπος να μάθουν τα παιδιά πώς κινείται η Γη.", "More people than you'd imagine. Mainly people building a house on the island who want something on the courtyard wall that doesn't need a battery. I've also made them for schools, because it's a very good way for children to learn how the Earth moves."),
  L("Δημοσιογράφος", "f", "Είναι δύσκολο να υπολογίσετε σωστά τις γραμμές;", "Is it difficult to calculate the lines correctly?"),
  L("Μαρμαράς", "m", "Αυτό είναι το πιο δύσκολο κομμάτι. Κάθε ρολόι είναι μοναδικό, γιατί εξαρτάται από το γεωγραφικό πλάτος του τόπου και από το πού ακριβώς κοιτάζει ο τοίχος. Παλιά έκανα τους υπολογισμούς με χαρτί και μολύβι και μου έπαιρναν μια εβδομάδα. Τώρα χρησιμοποιώ ένα πρόγραμμα στον υπολογιστή, αλλά πάντα πηγαίνω στο σπίτι να δω τον τοίχο με τα μάτια μου.", "That's the hardest part. Every sundial is unique, because it depends on the latitude of the place and on exactly which way the wall faces. I used to do the calculations with paper and pencil and they took me a week. Now I use a computer program, but I always go to the house to see the wall with my own eyes."),
  L("Δημοσιογράφος", "f", "Δείχνει πάντα τη σωστή ώρα;", "Does it always show the right time?"),
  L("Μαρμαράς", "m", "Δείχνει την ηλιακή ώρα, όχι την ώρα του κινητού σας. Το καλοκαίρι, με τη θερινή ώρα, η διαφορά είναι πάνω από μία ώρα. Οι πελάτες στην αρχή παραπονιούνται. Μετά τους αρέσει που έχουν στον τοίχο τους μια ώρα που δεν βιάζεται.", "It shows solar time, not the time on your phone. In summer, with daylight saving time, the difference is over an hour. Customers complain at first. Then they like having on their wall a time that isn't in a hurry."),
 ],
 "questions": [
  Q("Γιατί φτιάχνει ηλιακά ρολόγια και για σχολεία;", ["Γιατί είναι φθηνά", "Γιατί βοηθούν τα παιδιά να μάθουν πώς κινείται η Γη", "Γιατί του το ζήτησε το υπουργείο", "Γιατί τα σχολεία δεν έχουν ρολόγια"], 1, "να μάθουν τα παιδιά πώς κινείται η Γη"),
  Q("Από τι εξαρτάται κάθε ρολόι;", ["Από το μέγεθος του μαρμάρου", "Από το γεωγραφικό πλάτος και από το πού κοιτάζει ο τοίχος", "Από την εποχή του χρόνου", "Από το χρώμα του τοίχου"], 1, "εξαρτάται από το γεωγραφικό πλάτος του τόπου"),
  Q("Γιατί παραπονιούνται στην αρχή οι πελάτες;", ["Γιατί το ρολόι χαλάει", "Γιατί η ηλιακή ώρα διαφέρει από την ώρα του κινητού", "Γιατί η κατασκευή αργεί", "Γιατί κοστίζει ακριβά"], 1, "Δείχνει την ηλιακή ώρα, όχι την ώρα του κινητού σας"),
 ],
 "gloss": {"μαρμαρά": "μαρμαράς — marble carver", "πλάτος": "γεωγραφικό πλάτος — latitude", "υπολογισμούς": "υπολογισμός — calculation", "θερινή": "θερινή ώρα — daylight saving time", "παραπονιούνται": "παραπονιέμαι — to complain"},
})

ITEMS.append({
 "id": "l197-vm-syntagi", "title": "Μήνυμα από το ιατρείο για τη συνταγή", "title_en": "A message from the doctor's surgery about a prescription", "type": "voicemail", "level": "B2",
 "context_el": "Είχατε ζητήσει από τον γιατρό σας να σας γράψει ξανά ένα φάρμακο. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα σας, από το ιατρείο του κυρίου Ζαφειρίου σας παίρνω, η Βούλα. Η ηλεκτρονική συνταγή για την πίεση είναι έτοιμη. Θα σας έρθει μήνυμα στο κινητό με τον κωδικό, και με αυτόν μπορείτε να πάρετε τα φάρμακα από οποιοδήποτε φαρμακείο.", "Good morning, I'm calling from Mr Zafeiriou's surgery, it's Voula. The electronic prescription for your blood pressure is ready. You'll get a text on your mobile with the code, and with it you can collect the medicine from any pharmacy."),
  L("Γραμματέας", "f", "Ο γιατρός σάς έγραψε για τρεις μήνες αυτή τη φορά, οπότε δεν χρειάζεται να μας πάρετε τον άλλο μήνα. Θέλει όμως να σας δει πριν τελειώσουν, για να κάνετε και τις εξετάσεις αίματος που είχατε αφήσει.", "The doctor has prescribed for three months this time, so you don't need to call us next month. But he wants to see you before they run out, so you can also do the blood tests you had put off."),
  L("Γραμματέας", "f", "Αν δεν σας έρθει το μήνυμα μέσα στη μέρα, μάλλον έχουμε παλιό αριθμό. Πάρτε μας τότε να τον διορθώσουμε. Είμαστε εδώ ως τις δύο. Γεια σας.", "If you don't get the message within the day, we probably have an old number. Call us then so we can correct it. We're here until two. Goodbye."),
 ],
 "questions": [
  Q("Πώς θα πάρει ο ακροατής τον κωδικό της συνταγής;", ["Θα τον πάρει από το ιατρείο", "Με μήνυμα στο κινητό", "Με email", "Από το φαρμακείο"], 1, "Θα σας έρθει μήνυμα στο κινητό με τον κωδικό"),
  Q("Για πόσο καιρό είναι η συνταγή;", ["Για έναν μήνα", "Για δύο μήνες", "Για τρεις μήνες", "Για έναν χρόνο"], 2, "σάς έγραψε για τρεις μήνες"),
  Q("Τι πρέπει να κάνει αν δεν πάρει μήνυμα μέσα στη μέρα;", ["Να πάει σε άλλο φαρμακείο", "Να τηλεφωνήσει στο ιατρείο", "Να περιμένει μέχρι αύριο", "Να ξαναστείλει email"], 1, "Πάρτε μας τότε να τον διορθώσουμε"),
 ],
 "gloss": {"ιατρείο": "ιατρείο — doctor's surgery", "συνταγή": "συνταγή — prescription", "πίεση": "πίεση — blood pressure", "εξετάσεις": "εξετάσεις αίματος — blood tests", "κωδικό": "κωδικός — code"},
})

ITEMS.append({
 "id": "l197-mono-milao-monos-mou", "title": "Μιλάω φωναχτά με τον εαυτό μου", "title_en": "I talk to myself out loud", "type": "monologue", "level": "B2",
 "context_el": "Ένας ακροατής μιλάει σε μια ραδιοφωνική εκπομπή για μια συνήθειά του.",
 "script": [
  L("Θοδωρής", "m", "Από παιδί μιλάω μόνος μου. Όχι συνέχεια, αλλά όταν μαγειρεύω, όταν ψάχνω τα κλειδιά μου ή όταν προσπαθώ να λύσω ένα πρόβλημα στη δουλειά. Λέω πράγματα όπως «Λοιπόν, Θοδωρή, πρώτα το κρεμμύδι» ή «Πού τα άφησες πάλι;».", "I've talked to myself since I was a child. Not all the time, but when I'm cooking, when I'm looking for my keys or when I'm trying to solve a problem at work. I say things like 'Right, Thodoris, the onion first' or 'Where did you leave them this time?'"),
  L("Θοδωρής", "m", "Για χρόνια ντρεπόμουν. Μια φορά, στο σούπερ μάρκετ, μια κυρία με ρώτησε αν είμαι καλά, γιατί έλεγα δυνατά τη λίστα με τα ψώνια. Από τότε φορούσα ακουστικά, για να νομίζουν οι άλλοι ότι μιλάω στο τηλέφωνο.", "For years I was embarrassed. Once, at the supermarket, a lady asked me if I was all right, because I was saying my shopping list out loud. After that I wore earphones, so others would think I was on the phone."),
  L("Θοδωρής", "m", "Πριν από λίγο καιρό διάβασα ότι πολλοί άνθρωποι το κάνουν και ότι μπορεί να βοηθάει τη συγκέντρωση, ειδικά όταν μιλάμε στον εαυτό μας σε δεύτερο πρόσωπο, σαν να είμαστε προπονητές. Δεν ξέρω αν ισχύει για όλους. Για μένα, πάντως, ισχύει. Έβγαλα τα ακουστικά.", "A little while ago I read that many people do it and that it may help concentration, especially when we talk to ourselves in the second person, as if we were coaches. I don't know if it's true for everyone. For me, anyway, it is. I took the earphones off."),
 ],
 "questions": [
  Q("Πότε μιλάει συνήθως μόνος του ο Θοδωρής;", ["Μόνο όταν είναι στενοχωρημένος", "Όταν μαγειρεύει, ψάχνει κάτι ή λύνει ένα πρόβλημα", "Μόνο στο αυτοκίνητο", "Όταν δεν μπορεί να κοιμηθεί"], 1, "όταν μαγειρεύω, όταν ψάχνω τα κλειδιά μου"),
  Q("Γιατί φορούσε ακουστικά;", ["Για να ακούει μουσική", "Για να νομίζουν οι άλλοι ότι μιλάει στο τηλέφωνο", "Για να μην ακούει τον θόρυβο", "Γιατί του το πρότεινε ένας γιατρός"], 1, "για να νομίζουν οι άλλοι ότι μιλάω στο τηλέφωνο"),
  Q("Τι διάβασε πριν από λίγο καιρό;", ["Ότι είναι σημάδι άγχους", "Ότι πρέπει να το σταματήσει", "Ότι μπορεί να βοηθάει τη συγκέντρωση", "Ότι το κάνουν μόνο τα παιδιά"], 2, "μπορεί να βοηθάει τη συγκέντρωση"),
 ],
 "gloss": {"ντρεπόμουν": "ντρέπομαι — to be embarrassed, ashamed", "ακουστικά": "ακουστικά — earphones", "συγκέντρωση": "συγκέντρωση — concentration", "προπονητές": "προπονητής — coach"},
})

ITEMS.append({
 "id": "l197-dia-synantisi-apofoiton", "title": "Θα πάμε στη συνάντηση των αποφοίτων;", "title_en": "Shall we go to the school reunion?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο παλιοί συμμαθητές μιλούν στο τηλέφωνο για μια πρόσκληση.",
 "script": [
  L("Κατερίνα", "f", "Είδες την πρόσκληση; Κλείνουμε είκοσι χρόνια από την αποφοίτηση και κάνουν συνάντηση στην ταβέρνα του Λευτέρη, στις 13 Δεκεμβρίου.", "Did you see the invitation? It's twenty years since we graduated and they're holding a reunion at Lefteris's taverna on 13 December."),
  L("Άρης", "m", "Την είδα. Δεν ξέρω αν θέλω να πάω. Οι μισοί θα μιλάνε για τις δουλειές τους και για τα παιδιά τους, κι εγώ θα πω ότι ακόμα δεν έχω αποφασίσει τι θέλω να γίνω όταν μεγαλώσω.", "I saw it. I don't know if I want to go. Half of them will talk about their jobs and their kids, and I'll say I still haven't decided what I want to be when I grow up."),
  L("Κατερίνα", "f", "Έλα τώρα. Κανείς δεν θα σε ρωτήσει για βιογραφικό. Θα έρθει και ο κύριος Σταθόπουλος, ο φιλόλογος. Θυμάσαι που σε έβαλε να διαβάσεις το ποίημά σου στη γιορτή της 25ης Μαρτίου;", "Come on. Nobody's going to ask you for a CV. Mr Stathopoulos, the Greek teacher, is coming too. Remember when he made you read your poem at the 25th of March celebration?"),
  L("Άρης", "m", "Πώς να μην το θυμάμαι; Έτρεμαν τα γόνατά μου. Εντάξει, αν έρχεται εκείνος, θα έρθω. Αλλά με ένα όρο: να φύγουμε μαζί αν αρχίσουν να δείχνουν φωτογραφίες από τις διακοπές τους.", "How could I forget? My knees were shaking. OK, if he's coming, I'll come. But on one condition: we leave together if they start showing photos from their holidays."),
  L("Κατερίνα", "f", "Σύμφωνοι. Θα σε περάσω να σε πάρω στις οχτώ.", "Deal. I'll come and pick you up at eight."),
 ],
 "questions": [
  Q("Γιατί διστάζει ο Άρης να πάει;", ["Γιατί δεν του αρέσει η ταβέρνα", "Γιατί φοβάται ότι όλοι θα μιλάνε για δουλειές και παιδιά", "Γιατί θα λείπει ταξίδι", "Γιατί είναι θυμωμένος με την Κατερίνα"], 1, "Οι μισοί θα μιλάνε για τις δουλειές τους και για τα παιδιά τους"),
  Q("Τι πείθει τελικά τον Άρη να πάει;", ["Ότι θα είναι δωρεάν", "Ότι θα έρθει ο παλιός του φιλόλογος", "Ότι θα γίνει σε άλλη πόλη", "Ότι θα παίξει μουσική"], 1, "αν έρχεται εκείνος, θα έρθω"),
  Q("Ποιον όρο βάζει ο Άρης;", ["Να μη μείνουν πολύ αργά", "Να φύγουν μαζί αν αρχίσουν να δείχνουν φωτογραφίες από διακοπές", "Να μην πει κανείς για τη δουλειά του", "Να οδηγήσει εκείνος"], 1, "να φύγουμε μαζί αν αρχίσουν να δείχνουν φωτογραφίες"),
 ],
 "gloss": {"αποφοίτηση": "αποφοίτηση — graduation (from school)", "βιογραφικό": "βιογραφικό — CV, résumé", "φιλόλογος": "φιλόλογος — teacher of Greek language and literature", "γόνατά": "γόνατο — knee", "όρο": "όρος — condition, term"},
})

ITEMS.append({
 "id": "l197-rep-lemonada", "title": "Παιδιά πουλάνε λεμονάδα για τη σχολική βιβλιοθήκη", "title_en": "Children sell lemonade for the school library", "type": "report", "level": "B2",
 "context_el": "Ρεπορτάζ από μια τοπική ραδιοφωνική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Κάθε Σάββατο πρωί, έξω από τη λαϊκή αγορά της γειτονιάς, ένα τραπεζάκι με μια χειρόγραφη πινακίδα τραβάει την προσοχή: «Λεμονάδα για βιβλία». Πίσω του στέκονται μαθητές της πέμπτης τάξης του δημοτικού σχολείου που βρίσκεται στην απέναντι γωνία.", "Every Saturday morning, outside the neighbourhood street market, a small table with a handwritten sign catches the eye: 'Lemonade for books'. Behind it stand fifth-year pupils from the primary school on the opposite corner."),
  L("Ρεπόρτερ", "f", "Η ιδέα ήταν της δασκάλας τους. Η σχολική βιβλιοθήκη είχε μόνο λίγα παλιά βιβλία, και τα παιδιά αποφάσισαν να μαζέψουν χρήματα μόνα τους. Τα λεμόνια τα δίνει ένας παραγωγός της λαϊκής και τη ζάχαρη ένα μπακάλικο. Τα παιδιά κάνουν όλα τα υπόλοιπα: στύβουν, μετράνε τα ρέστα και κρατούν ένα τετράδιο με τα έσοδα.", "The idea was their teacher's. The school library had only a few old books, and the children decided to raise money themselves. The lemons are donated by a stallholder at the market and the sugar by a grocer's. The children do everything else: they squeeze, count the change and keep a notebook of the takings."),
  L("Ρεπόρτερ", "f", "Μέσα σε τρεις μήνες μάζεψαν πάνω από οχτακόσια ευρώ και αγόρασαν εκατόν είκοσι βιβλία, που τα διάλεξαν τα ίδια, με ψηφοφορία. Η δασκάλα λέει ότι έμαθαν περισσότερα μαθηματικά πίσω από το τραπεζάκι παρά στην τάξη. Οι μαθητές πάντως έχουν ήδη νέο στόχο: τον χειμώνα, ζεστή σοκολάτα.", "Within three months they raised over eight hundred euros and bought a hundred and twenty books, which they chose themselves, by vote. The teacher says they learned more maths behind the little table than in the classroom. The pupils, anyway, already have a new goal: in winter, hot chocolate."),
 ],
 "questions": [
  Q("Ποιος δίνει τα λεμόνια;", ["Οι γονείς", "Ένας παραγωγός της λαϊκής", "Ένα μπακάλικο", "Ο δήμος"], 1, "Τα λεμόνια τα δίνει ένας παραγωγός της λαϊκής"),
  Q("Πώς διάλεξαν τα βιβλία;", ["Τα διάλεξε η δασκάλα", "Με ψηφοφορία των παιδιών", "Τα πρότεινε ο βιβλιοπώλης", "Από έναν κατάλογο του υπουργείου"], 1, "που τα διάλεξαν τα ίδια, με ψηφοφορία"),
  Q("Ποιος είναι ο νέος στόχος των μαθητών;", ["Να πουλήσουν βιβλία", "Να πουλήσουν ζεστή σοκολάτα τον χειμώνα", "Να ανοίξουν καφετέρια", "Να πάνε εκδρομή"], 1, "τον χειμώνα, ζεστή σοκολάτα"),
 ],
 "gloss": {"λαϊκή": "λαϊκή (αγορά) — street market", "χειρόγραφη": "χειρόγραφος — handwritten", "μπακάλικο": "μπακάλικο — grocer's shop", "στύβουν": "στύβω — to squeeze", "ρέστα": "ρέστα — change (money)", "έσοδα": "έσοδα — takings, income"},
})

ITEMS.append({
 "id": "l197-int-kafe-syndromo-down", "title": "Ένα καφέ με σερβιτόρους με σύνδρομο Down", "title_en": "A café whose waiters have Down syndrome", "type": "interview", "level": "B2",
 "context_el": "Συνέντευξη με την υπεύθυνη ενός καφέ όπου εργάζονται νέοι με σύνδρομο Down.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς ξεκίνησε το καφέ;", "How did the café start?"),
  L("Υπεύθυνη", "f", "Ξεκίνησε από μια ομάδα γονέων. Τα παιδιά μας τελείωναν το σχολείο και δεν υπήρχε τίποτα για αυτά μετά. Θέλαμε μια πραγματική δουλειά, με μισθό και ασφάλιση, όχι ένα εργαστήρι όπου απλώς περνούν την ώρα τους.", "It started with a group of parents. Our children were finishing school and there was nothing for them afterwards. We wanted a real job, with a salary and insurance, not a workshop where they just pass the time."),
  L("Δημοσιογράφος", "m", "Πώς αντιδρούν οι πελάτες;", "How do customers react?"),
  L("Υπεύθυνη", "f", "Οι περισσότεροι έρχονται μία φορά από περιέργεια και μετά γίνονται θαμώνες. Ο Νίκος, ο πιο παλιός μας σερβιτόρος, θυμάται τι πίνει ο καθένας. Μπαίνεις και σου λέει «Φρέντο χωρίς ζάχαρη, σωστά;» πριν προλάβεις να καθίσεις. Βέβαια, μερικές φορές οι παραγγελίες αργούν λίγο. Στον τοίχο έχουμε γράψει: «Εδώ ο καφές δεν βιάζεται».", "Most come once out of curiosity and then become regulars. Nikos, our longest-serving waiter, remembers what everyone drinks. You walk in and he says 'Freddo without sugar, right?' before you've had time to sit down. Of course, sometimes orders take a little longer. On the wall we've written: 'Here coffee isn't in a hurry'."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το επόμενο βήμα;", "What's the next step?"),
  L("Υπεύθυνη", "f", "Να μη χρειάζονται πια καφέ σαν το δικό μας. Θα ήθελα τα παιδιά μας να δουλεύουν σε οποιοδήποτε μαγαζί της γειτονιάς, και να μην το βρίσκει κανείς παράξενο.", "That cafés like ours are no longer needed. I'd like our children to work in any shop in the neighbourhood, and for nobody to find it strange."),
 ],
 "questions": [
  Q("Τι ήθελαν οι γονείς για τα παιδιά τους;", ["Ένα εργαστήρι για να περνούν την ώρα τους", "Μια πραγματική δουλειά με μισθό και ασφάλιση", "Ένα σχολείο για ενήλικες", "Μια κατασκήνωση"], 1, "Θέλαμε μια πραγματική δουλειά, με μισθό και ασφάλιση"),
  Q("Τι κάνει ο Νίκος;", ["Φτιάχνει τα γλυκά", "Θυμάται τι πίνει ο κάθε πελάτης", "Κρατάει το ταμείο", "Γράφει στον τοίχο"], 1, "θυμάται τι πίνει ο καθένας"),
  Q("Ποιο είναι το επόμενο βήμα για την υπεύθυνη;", ["Να ανοίξουν δεύτερο καφέ", "Να μη χρειάζονται πια τέτοια καφέ", "Να μεγαλώσει το μαγαζί", "Να βγουν στην τηλεόραση"], 1, "Να μη χρειάζονται πια καφέ σαν το δικό μας"),
 ],
 "gloss": {"σύνδρομο": "σύνδρομο Down — Down syndrome", "ασφάλιση": "ασφάλιση — (social) insurance", "περιέργεια": "περιέργεια — curiosity", "θαμώνες": "θαμώνας — regular customer", "παράξενο": "παράξενος — strange"},
})

ITEMS.append({
 "id": "l197-news-romaiko-navagio", "title": "Υποβρύχια έρευνα εντόπισε ρωμαϊκό ναυάγιο", "title_en": "Underwater survey locates a Roman shipwreck", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων του ραδιοφώνου.",
 "script": [
  L("Εκφωνητής", "m", "Ένα ναυάγιο της ρωμαϊκής εποχής εντόπισαν δύτες της Εφορείας Εναλίων Αρχαιοτήτων σε βάθος περίπου σαράντα μέτρων, ανοιχτά ενός μικρού νησιού των Δωδεκανήσων. Το πλοίο μετέφερε αμφορείς, πιθανότατα με κρασί ή λάδι, και πολλοί από αυτούς σώζονται ακόμα στη θέση τους.", "A shipwreck from the Roman era was located by divers of the Ephorate of Underwater Antiquities at a depth of about forty metres, off a small island in the Dodecanese. The ship was carrying amphorae, most likely with wine or oil, and many of them are still preserved in place."),
  L("Εκφωνητής", "m", "Το ναυάγιο το είχε δει πρώτος πέρσι ένας ψαράς της περιοχής, όταν τα δίχτυα του πιάστηκαν σε κάτι σκληρό στον βυθό. Οι αρχαιολόγοι λένε ότι το εύρημα θα βοηθήσει να καταλάβουμε καλύτερα τους εμπορικούς δρόμους του Αιγαίου εκείνης της εποχής.", "The wreck was first seen last year by a local fisherman, when his nets got caught on something hard on the seabed. The archaeologists say the find will help us better understand the trade routes of the Aegean at that time."),
  L("Εκφωνητής", "m", "Η ακριβής θέση δεν ανακοινώθηκε, για να προστατευτεί το ναυάγιο από αρχαιοκάπηλους. Η έρευνα θα συνεχιστεί την άνοιξη.", "The exact location was not announced, to protect the wreck from looters. The survey will continue in the spring."),
 ],
 "questions": [
  Q("Τι μετέφερε το πλοίο;", ["Μάρμαρα", "Αμφορείς, πιθανότατα με κρασί ή λάδι", "Νομίσματα", "Όπλα"], 1, "Το πλοίο μετέφερε αμφορείς"),
  Q("Ποιος είδε πρώτος το ναυάγιο;", ["Ένας τουρίστας", "Ένας ψαράς της περιοχής", "Ένας φοιτητής αρχαιολογίας", "Ένα υποβρύχιο ρομπότ"], 1, "Το ναυάγιο το είχε δει πρώτος πέρσι ένας ψαράς της περιοχής"),
  Q("Γιατί δεν ανακοινώθηκε η ακριβής θέση;", ["Γιατί δεν είναι ακόμα γνωστή", "Για να προστατευτεί από αρχαιοκάπηλους", "Γιατί υπάρχει κίνδυνος για τους δύτες", "Γιατί το ζήτησε ο ψαράς"], 1, "για να προστατευτεί το ναυάγιο από αρχαιοκάπηλους"),
 ],
 "gloss": {"ναυάγιο": "ναυάγιο — shipwreck", "Εναλίων": "ενάλιος — underwater, marine", "αμφορείς": "αμφορέας — amphora", "εύρημα": "εύρημα — find", "αρχαιοκάπηλους": "αρχαιοκάπηλος — looter of antiquities"},
})

ITEMS.append({
 "id": "l197-c1-mono-moudiasma", "title": "Γιατί μουδιάζει το πόδι μας;", "title_en": "Why does our leg go numb?", "type": "monologue", "level": "C1",
 "context_el": "Απόσπασμα από podcast εκλαΐκευσης της επιστήμης.",
 "script": [
  L("Παρουσιάστρια", "f", "Καθόμαστε σταυροπόδι σε μια συναυλία ή στο γραφείο, και όταν σηκωνόμαστε, το πόδι μας δεν μας ακούει. Στην αρχή δεν νιώθουμε σχεδόν τίποτα και μετά έρχεται εκείνο το ενοχλητικό τσίμπημα, σαν να περπατούν χιλιάδες μυρμήγκια κάτω από το δέρμα. Οι γιατροί το λένε παραισθησία· εμείς λέμε απλώς ότι «μούδιασε το πόδι μας».", "We sit cross-legged at a concert or at the office, and when we stand up, our leg won't obey us. At first we feel almost nothing and then comes that annoying prickling, as if thousands of ants were walking under the skin. Doctors call it paraesthesia; we simply say our leg has gone numb."),
  L("Παρουσιάστρια", "f", "Παρά την κοινή πεποίθηση, η αιτία δεν είναι κυρίως ότι «κόπηκε η κυκλοφορία». Το βασικό είναι η πίεση που ασκείται σε ένα νεύρο. Όταν ένα νεύρο πιέζεται για αρκετή ώρα, και τα αιμοφόρα αγγεία γύρω του δεν το τροφοδοτούν όπως πρέπει, παύει προσωρινά να μεταφέρει κανονικά τα μηνύματα προς τον εγκέφαλο. Γι' αυτό, για λίγο, το άκρο μοιάζει ξένο.", "Contrary to popular belief, the cause isn't mainly that 'the circulation was cut off'. The key factor is the pressure on a nerve. When a nerve is compressed for long enough, and the blood vessels around it don't supply it properly, it temporarily stops carrying messages to the brain normally. That's why, for a while, the limb feels foreign."),
  L("Παρουσιάστρια", "f", "Το τσίμπημα έρχεται όταν η πίεση φεύγει: το νεύρο ξαναρχίζει να λειτουργεί, αλλά για λίγα λεπτά στέλνει σήματα ακανόνιστα, και ο εγκέφαλος τα ερμηνεύει ως μυρμήγκιασμα. Η καλύτερη λύση είναι η πιο απλή: αλλάζουμε στάση και κινούμε απαλά το πόδι. Αν όμως το μούδιασμα εμφανίζεται συχνά χωρίς προφανή λόγο ή δεν περνάει, αξίζει να το συζητήσουμε με έναν γιατρό, γιατί μπορεί να σχετίζεται με άλλα προβλήματα υγείας.", "The prickling comes when the pressure goes away: the nerve starts working again, but for a few minutes it sends signals irregularly, and the brain interprets them as tingling. The best solution is the simplest one: we change position and gently move the leg. But if the numbness appears often for no obvious reason or doesn't go away, it's worth discussing with a doctor, because it may be related to other health problems."),
 ],
 "questions": [
  Q("Ποια είναι, σύμφωνα με την παρουσιάστρια, η βασική αιτία του μουδιάσματος;", ["Το κρύο", "Η πίεση που ασκείται σε ένα νεύρο", "Η έλλειψη νερού", "Η κούραση των μυών"], 1, "Το βασικό είναι η πίεση που ασκείται σε ένα νεύρο"),
  Q("Γιατί νιώθουμε τσίμπημα όταν φεύγει η πίεση;", ["Γιατί το αίμα κρυώνει", "Γιατί το νεύρο στέλνει για λίγο σήματα ακανόνιστα", "Γιατί οι μύες σφίγγονται", "Γιατί το δέρμα ερεθίζεται"], 1, "στέλνει σήματα ακανόνιστα"),
  Q("Πότε αξίζει να μιλήσουμε σε γιατρό;", ["Κάθε φορά που μουδιάζει το πόδι", "Όταν το μούδιασμα εμφανίζεται συχνά χωρίς προφανή λόγο ή δεν περνάει", "Μόνο αν πονάει", "Ποτέ, είναι αθώο"], 1, "Αν όμως το μούδιασμα εμφανίζεται συχνά χωρίς προφανή λόγο ή δεν περνάει"),
 ],
 "gloss": {"σταυροπόδι": "σταυροπόδι — cross-legged", "παραισθησία": "παραισθησία — paraesthesia, pins and needles", "πεποίθηση": "πεποίθηση — belief", "αιμοφόρα": "αιμοφόρα αγγεία — blood vessels", "ακανόνιστα": "ακανόνιστος — irregular", "μυρμήγκιασμα": "μυρμήγκιασμα — tingling"},
})

ITEMS.append({
 "id": "l197-c1-int-korifi-anamniseon", "title": "Γιατί θυμόμαστε περισσότερο τα νιάτα μας;", "title_en": "Why do we remember our youth best?", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με μια γνωστική ψυχολόγο σε μια εκπομπή για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "m", "Αν ζητήσουμε από έναν εξηντάρη να μας πει τις πιο ζωντανές του αναμνήσεις, από ποια περίοδο θα είναι οι περισσότερες;", "If we ask a sixty-year-old to tell us their most vivid memories, which period will most of them come from?"),
  L("Ψυχολόγος", "f", "Με μεγάλη πιθανότητα από την εφηβεία και τα πρώτα χρόνια της ενήλικης ζωής, περίπου από τα δέκα ως τα τριάντα. Το φαινόμενο είναι τόσο σταθερό που έχει και όνομα: στη βιβλιογραφία το λέμε «εξόγκωμα αναπόλησης». Οι αναμνήσεις δεν κατανέμονται ομοιόμορφα στη διάρκεια της ζωής· σε εκείνη τη δεκαετία ή δύο, η καμπύλη ανεβαίνει απότομα.", "Very probably from adolescence and the first years of adult life, roughly from ten to thirty. The phenomenon is so consistent that it has a name: in the literature we call it the 'reminiscence bump'. Memories aren't distributed evenly across a lifetime; in that decade or two, the curve rises sharply."),
  L("Δημοσιογράφος", "m", "Και γιατί συμβαίνει αυτό;", "And why does that happen?"),
  L("Ψυχολόγος", "f", "Υπάρχουν διάφορες εξηγήσεις, που μάλλον συνυπάρχουν. Η πρώτη είναι η καινοτομία: τότε ζούμε τις περισσότερες «πρώτες φορές», το πρώτο ταξίδι μόνοι, την πρώτη δουλειά, τον πρώτο έρωτα, και ό,τι είναι καινούργιο καταγράφεται πιο έντονα. Η δεύτερη αφορά την ταυτότητα: σε αυτή την ηλικία διαμορφώνουμε το ποιοι είμαστε, και οι αναμνήσεις εκείνων των χρόνων γίνονται τα θεμέλια της ιστορίας που λέμε για τον εαυτό μας. Υπάρχει και μια τρίτη, πολιτισμική: κάθε κοινωνία έχει ένα άγραφο σενάριο για το πότε «πρέπει» να συμβαίνουν τα σημαντικά γεγονότα, και αυτό το σενάριο κατευθύνει και τη μνήμη μας.", "There are several explanations, which probably coexist. The first is novelty: that's when we live most of our 'first times', the first trip alone, the first job, first love, and whatever is new is recorded more intensely. The second concerns identity: at that age we shape who we are, and the memories of those years become the foundations of the story we tell about ourselves. There's also a third, cultural one: every society has an unwritten script for when important events 'should' happen, and that script also steers our memory."),
  L("Δημοσιογράφος", "m", "Εξηγεί αυτό και γιατί η μουσική της εφηβείας μας συγκινεί τόσο;", "Does this also explain why the music of our teenage years moves us so much?"),
  L("Ψυχολόγος", "f", "Σε μεγάλο βαθμό, ναι. Τα τραγούδια εκείνων των χρόνων είναι δεμένα με τις πρώτες φορές και με την ταυτότητά μας. Γι' αυτό ένα τραγούδι στο ραδιόφωνο μπορεί να μας ταξιδέψει σαράντα χρόνια πίσω μέσα σε τρία δευτερόλεπτα.", "To a large extent, yes. The songs of those years are tied to the first times and to our identity. That's why a song on the radio can take us forty years back in three seconds."),
 ],
 "questions": [
  Q("Από ποια περίοδο προέρχονται οι περισσότερες ζωντανές αναμνήσεις ενός εξηντάρη;", ["Από την πρώιμη παιδική ηλικία", "Περίπου από τα δέκα ως τα τριάντα", "Από τα τελευταία δέκα χρόνια", "Ομοιόμορφα από όλη τη ζωή"], 1, "περίπου από τα δέκα ως τα τριάντα"),
  Q("Τι σημαίνει η εξήγηση της «καινοτομίας»;", ["Ότι οι νέοι έχουν καλύτερη μνήμη", "Ότι ό,τι ζούμε για πρώτη φορά καταγράφεται πιο έντονα", "Ότι η τεχνολογία βοηθά τη μνήμη", "Ότι θυμόμαστε μόνο τα ευχάριστα"], 1, "ό,τι είναι καινούργιο καταγράφεται πιο έντονα"),
  Q("Τι είναι το «άγραφο σενάριο» που αναφέρει;", ["Ένα βιβλίο ψυχολογίας", "Η αντίληψη μιας κοινωνίας για το πότε πρέπει να συμβαίνουν τα σημαντικά γεγονότα", "Ένα ημερολόγιο της εφηβείας", "Μια θεραπεία για τη μνήμη"], 1, "κάθε κοινωνία έχει ένα άγραφο σενάριο για το πότε «πρέπει» να συμβαίνουν τα σημαντικά γεγονότα"),
  Q("Γιατί η μουσική της εφηβείας μάς συγκινεί τόσο;", ["Γιατί ήταν καλύτερη από τη σημερινή", "Γιατί είναι δεμένη με τις πρώτες φορές και με την ταυτότητά μας", "Γιατί την ακούμε συχνά στο ραδιόφωνο", "Γιατί τότε ακούγαμε πιο δυνατά"], 1, "Τα τραγούδια εκείνων των χρόνων είναι δεμένα με τις πρώτες φορές και με την ταυτότητά μας"),
 ],
 "gloss": {"εξηντάρη": "εξηντάρης — sixty-year-old", "εφηβεία": "εφηβεία — adolescence", "εξόγκωμα": "εξόγκωμα — bump, swelling", "αναπόλησης": "αναπόληση — reminiscence", "κατανέμονται": "κατανέμομαι — to be distributed", "θεμέλια": "θεμέλιο — foundation", "άγραφο": "άγραφος — unwritten"},
})

rnd = random.Random(197)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-197.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
