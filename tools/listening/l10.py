# Source for library/listening/listening-10.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l10.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l10-ann-anaklisi", "title": "Ανάκληση προϊόντος", "title_en": "A product recall", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα ενός σούπερ μάρκετ.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί πελάτες, σας ενημερώνουμε ότι, σε συνεννόηση με τον Ενιαίο Φορέα Ελέγχου Τροφίμων, ανακαλείται το τυρί κρέμα σε συσκευασία διακοσίων γραμμαρίων με ημερομηνία λήξης δεκαπέντε Μαρτίου. Σε ορισμένες συσκευασίες εντοπίστηκε βακτήριο που μπορεί να προκαλέσει τροφική δηλητηρίαση.", "Dear customers, we inform you that, in consultation with the Hellenic Food Authority, the cream cheese in 200-gram packs with a best-before date of 15 March is being recalled. A bacterium that can cause food poisoning was found in some packs."),
  L("Εκφωνήτρια", "f", "Αν έχετε αγοράσει το συγκεκριμένο προϊόν, παρακαλούμε να μην το καταναλώσετε. Μπορείτε να το επιστρέψετε σε οποιοδήποτε κατάστημά μας, ακόμη και ανοιγμένο και χωρίς απόδειξη, και θα σας επιστραφεί ολόκληρο το ποσό.", "If you have bought this product, please do not eat it. You can return it to any of our shops, even opened and without a receipt, and you will be refunded the full amount."),
  L("Εκφωνήτρια", "f", "Οι υπόλοιπες συσκευασίες του ίδιου τυριού, με άλλη ημερομηνία λήξης, είναι απολύτως ασφαλείς. Για περισσότερες πληροφορίες απευθυνθείτε στο γκισέ εξυπηρέτησης πελατών, δίπλα στην έξοδο. Ζητούμε συγγνώμη για την αναστάτωση.", "Other packs of the same cheese, with a different date, are completely safe. For more information please go to the customer service desk next to the exit. We apologise for the disruption."),
 ],
 "questions": [
  Q("Γιατί ανακαλείται το προϊόν;", ["Γιατί έληξε", "Γιατί η συσκευασία ήταν ελαττωματική", "Γιατί βρέθηκε βακτήριο σε κάποιες συσκευασίες", "Γιατί η τιμή ήταν λάθος"], 2, "Σε ορισμένες συσκευασίες εντοπίστηκε βακτήριο"),
  Q("Τι ισχύει για την επιστροφή;", ["Χρειάζεται απόδειξη", "Το προϊόν πρέπει να είναι κλειστό", "Επιστρέφεται όλο το ποσό ακόμη και χωρίς απόδειξη", "Δίνεται μόνο πιστωτικό σημείωμα"], 2, "ακόμη και ανοιγμένο και χωρίς απόδειξη, και θα σας επιστραφεί ολόκληρο το ποσό"),
  Q("Ποιες συσκευασίες είναι ασφαλείς;", ["Καμία", "Όσες έχουν άλλη ημερομηνία λήξης", "Μόνο οι μεγάλες συσκευασίες", "Όσες αγοράστηκαν σήμερα"], 1, "Οι υπόλοιπες συσκευασίες του ίδιου τυριού, με άλλη ημερομηνία λήξης, είναι απολύτως ασφαλείς."),
 ],
 "gloss": {"σε συνεννόηση": "σε συνεννόηση με — in consultation with", "ανακαλείται": "ανακαλώ — to recall, withdraw", "συσκευασία": "συσκευασία — pack, packaging", "ημερομηνία λήξης": "ημερομηνία λήξης — expiry / best-before date", "εντοπίστηκε": "εντοπίζω — to detect, locate", "βακτήριο": "βακτήριο — bacterium", "τροφική δηλητηρίαση": "τροφική δηλητηρίαση — food poisoning", "καταναλώσετε": "καταναλώνω — to consume", "γκισέ": "γκισέ — counter, desk", "αναστάτωση": "αναστάτωση — disruption, upset"},
})

ITEMS.append({
 "id": "l10-vm-gymnastirio", "title": "Πάγωμα συνδρομής", "title_en": "Freezing a gym membership", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από τη γραμματεία ενός γυμναστηρίου προς έναν πελάτη, τον κύριο Δρόσο.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα, κύριε Δρόσο, σας τηλεφωνώ από το γυμναστήριο, σχετικά με το email που μας στείλατε. Λυπούμαστε πολύ για τον τραυματισμό σας. Μπορούμε, βεβαίως, να παγώσουμε τη συνδρομή σας, ώστε να μη χάσετε τους μήνες που έχετε πληρώσει.", "Good morning, Mr Drosos, I'm calling from the gym about the email you sent us. We are very sorry about your injury. We can of course freeze your membership so you don't lose the months you've paid for."),
  L("Γραμματέας", "f", "Σύμφωνα με τους όρους της ετήσιας συνδρομής, το πάγωμα μπορεί να διαρκέσει έως τρεις μήνες. Για να το ενεργοποιήσουμε, χρειαζόμαστε μια βεβαίωση από τον γιατρό σας, όπου να αναφέρεται πόσο καιρό δεν θα μπορείτε να γυμναστείτε. Μπορείτε να μας τη στείλετε σκαναρισμένη.", "Under the terms of the annual membership, the freeze can last up to three months. To activate it we need a certificate from your doctor stating how long you won't be able to exercise. You can send it to us scanned."),
  L("Γραμματέας", "f", "Α, και κάτι ακόμη: ο φυσικοθεραπευτής μας κάνει πρόγραμμα αποκατάστασης για μέλη, με έκπτωση τριάντα τοις εκατό. Αν σας ενδιαφέρει, όταν σας το επιτρέψει ο γιατρός σας, πείτε μας να σας κλείσουμε ένα πρώτο ραντεβού. Περαστικά!", "Oh, and one more thing: our physiotherapist runs a rehabilitation programme for members, with a thirty per cent discount. If you're interested, once your doctor allows it, let us know and we'll book you a first appointment. Get well soon!"),
 ],
 "questions": [
  Q("Γιατί ο κύριος Δρόσος θέλει να παγώσει τη συνδρομή του;", ["Γιατί φεύγει ταξίδι", "Γιατί τραυματίστηκε", "Γιατί δεν έχει χρήματα", "Γιατί μετακομίζει"], 1, "Λυπούμαστε πολύ για τον τραυματισμό σας."),
  Q("Τι χρειάζεται για να παγώσει η συνδρομή;", ["Να πάει αυτοπροσώπως στο γυμναστήριο", "Να πληρώσει ένα μικρό ποσό", "Μια βεβαίωση από τον γιατρό του", "Να ανανεώσει τη συνδρομή του"], 2, "χρειαζόμαστε μια βεβαίωση από τον γιατρό σας"),
  Q("Τι του προτείνει επιπλέον η γραμματέας;", ["Ένα πρόγραμμα αποκατάστασης με έκπτωση", "Να αλλάξει γυμναστήριο", "Ένα δωρεάν μασάζ", "Μαθήματα κολύμβησης"], 0, "ο φυσικοθεραπευτής μας κάνει πρόγραμμα αποκατάστασης για μέλη, με έκπτωση τριάντα τοις εκατό"),
 ],
 "gloss": {"πάγωμα": "πάγωμα — freeze, freezing", "συνδρομής": "συνδρομή — membership, subscription", "τραυματισμό": "τραυματισμός — injury", "όρους": "όρος — term, condition", "ενεργοποιήσουμε": "ενεργοποιώ — to activate", "βεβαίωση": "βεβαίωση — certificate, written confirmation", "σκαναρισμένη": "σκαναρισμένος — scanned", "φυσικοθεραπευτής": "φυσικοθεραπευτής — physiotherapist", "αποκατάστασης": "αποκατάσταση — rehabilitation, restoration", "Περαστικά": "περαστικά — get well soon"},
})

ITEMS.append({
 "id": "l10-dia-syntaxi", "title": "Η αποχαιρετιστήρια γιορτή", "title_en": "The farewell party", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε δύο συναδέλφους, τη Λένα και τον Μάκη, να οργανώνουν μια αποχαιρετιστήρια γιορτή για έναν συνάδελφο που βγαίνει στη σύνταξη.",
 "script": [
  L("Λένα", "f", "Μάκη, ο κύριος Τάσος φεύγει στο τέλος του μήνα, μετά από τριάντα πέντε χρόνια στην εταιρεία. Πρέπει να του κάνουμε κάτι ωραίο.", "Makis, Mr Tasos leaves at the end of the month, after thirty-five years with the company. We should do something nice for him."),
  L("Μάκης", "m", "Οπωσδήποτε. Σκεφτόμουν ένα τραπέζι σε μια ταβέρνα, την Παρασκευή το βράδυ. Αλλά δεν ξέρω αν θα έρθουν όλοι, μερικοί έχουν μικρά παιδιά.", "Definitely. I was thinking of a dinner at a taverna on Friday evening. But I don't know if everyone will come; some have small children."),
  L("Λένα", "f", "Τότε ας το κάνουμε εδώ, στο γραφείο, την τελευταία του μέρα, γύρω στις δύο. Φέρνουμε φαγητά, κάνουμε μια μικρή ομιλία, και όποιος θέλει μένει παραπάνω. Έτσι δεν θα λείψει κανείς.", "Then let's do it here at the office, on his last day, around two. We bring food, give a short speech, and anyone who wants can stay longer. That way nobody will miss it."),
  L("Μάκης", "m", "Καλή ιδέα. Και για δώρο; Να μαζέψουμε χρήματα για ένα ρολόι;", "Good idea. And a present? Shall we collect money for a watch?"),
  L("Λένα", "f", "Ρολόι, όταν βγαίνει στη σύνταξη; Λίγο ειρωνικό, δεν νομίζεις; Ξέρω ότι θέλει να ασχοληθεί με την κηπουρική στο χωριό του. Να του πάρουμε ένα καλό σετ εργαλεία κήπου και ένα άλμπουμ με φωτογραφίες και ευχές από όλους μας.", "A watch, when he's retiring? A bit ironic, don't you think? I know he wants to take up gardening in his village. Let's get him a good set of garden tools and an album with photos and wishes from all of us."),
  L("Μάκης", "m", "Τέλειο. Αναλαμβάνω εγώ να μαζέψω τις φωτογραφίες, έχω κάποιες παλιές από τις εκδρομές της εταιρείας. Εσύ στείλε ένα μήνυμα σε όλους για τα χρήματα.", "Perfect. I'll take care of collecting the photos; I have some old ones from company trips. You send everyone a message about the money."),
 ],
 "questions": [
  Q("Γιατί η Λένα προτείνει να γίνει η γιορτή στο γραφείο;", ["Γιατί είναι φθηνότερο", "Για να μπορέσουν να έρθουν όλοι", "Γιατί το ζήτησε ο κύριος Τάσος", "Γιατί οι ταβέρνες είναι κλειστές"], 1, "Έτσι δεν θα λείψει κανείς."),
  Q("Γιατί η Λένα δεν θέλει να του πάρουν ρολόι;", ["Γιατί είναι ακριβό", "Γιατί έχει ήδη πολλά", "Γιατί της φαίνεται ειρωνικό δώρο για κάποιον που συνταξιοδοτείται", "Γιατί δεν φοράει ρολόι"], 2, "Ρολόι, όταν βγαίνει στη σύνταξη; Λίγο ειρωνικό"),
  Q("Τι θα αναλάβει ο Μάκης;", ["Να αγοράσει τα εργαλεία", "Να μαζέψει φωτογραφίες", "Να κάνει την ομιλία", "Να στείλει μήνυμα για τα χρήματα"], 1, "Αναλαμβάνω εγώ να μαζέψω τις φωτογραφίες"),
 ],
 "gloss": {"αποχαιρετιστήρια": "αποχαιρετιστήριος — farewell (adj.)", "συναδέλφους": "συνάδελφος — colleague", "σύνταξη": "σύνταξη — pension; βγαίνω στη σύνταξη — to retire", "Οπωσδήποτε": "οπωσδήποτε — definitely", "ομιλία": "ομιλία — speech", "ειρωνικό": "ειρωνικός — ironic", "κηπουρική": "κηπουρική — gardening", "ευχές": "ευχή — wish", "Αναλαμβάνω": "αναλαμβάνω — to take on, take charge of"},
})

ITEMS.append({
 "id": "l10-dia-enoikiasi", "title": "Ενοικίαση αυτοκινήτου", "title_en": "Hiring a car", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα γραφείο ενοικίασης αυτοκινήτων στο αεροδρόμιο της Κρήτης.",
 "script": [
  L("Υπάλληλος", "m", "Καλώς ήρθατε. Έχετε κράτηση;", "Welcome. Do you have a booking?"),
  L("Πελάτισσα", "f", "Ναι, στο όνομα Κωνσταντίνου, για ένα μικρό αυτοκίνητο, πέντε μέρες.", "Yes, under the name Konstantinou, for a small car, five days."),
  L("Υπάλληλος", "m", "Μάλιστα, εδώ είναι. Η τιμή περιλαμβάνει τη βασική ασφάλεια, αλλά με απαλλαγή εξακοσίων ευρώ. Αυτό σημαίνει ότι, αν πάθει ζημιά το αυτοκίνητο, πληρώνετε εσείς μέχρι εξακόσια ευρώ. Με δέκα ευρώ την ημέρα παραπάνω, έχετε πλήρη κάλυψη και δεν πληρώνετε τίποτα.", "Right, here it is. The price includes basic insurance, but with a six-hundred-euro excess. That means that if the car is damaged, you pay up to six hundred euros. For ten euros a day more, you have full cover and pay nothing."),
  L("Πελάτισσα", "f", "Η πλήρης κάλυψη ισχύει και για τα λάστιχα και τα τζάμια; Θέλω να πάω σε κάτι παραλίες με χωματόδρομο.", "Does full cover also apply to the tyres and the windows? I want to go to some beaches with a dirt road."),
  L("Υπάλληλος", "m", "Τζάμια και λάστιχα, ναι. Προσέξτε όμως: σε χωματόδρομους δεν καλύπτεται η ζημιά κάτω από το αυτοκίνητο. Το γράφει το συμβόλαιο. Σας συμβουλεύω να αφήνετε το αυτοκίνητο εκεί που τελειώνει η άσφαλτος και να περπατάτε τα τελευταία μέτρα.", "Windows and tyres, yes. But be careful: on dirt roads damage to the underside of the car is not covered. It's in the contract. I advise you to leave the car where the asphalt ends and walk the last few metres."),
  L("Πελάτισσα", "f", "Εντάξει, θα πάρω την πλήρη κάλυψη. Και η βενζίνη;", "OK, I'll take full cover. And the petrol?"),
  L("Υπάλληλος", "m", "Το παραλαμβάνετε με γεμάτο ρεζερβουάρ και το επιστρέφετε γεμάτο. Αν όχι, χρεώνουμε τη διαφορά, και λίγο πιο ακριβά από το βενζινάδικο.", "You get it with a full tank and return it full. If not, we charge the difference, and a little more than the petrol station."),
 ],
 "questions": [
  Q("Τι σημαίνει η «απαλλαγή εξακοσίων ευρώ»;", ["Ότι κερδίζει έκπτωση εξακόσια ευρώ", "Ότι σε περίπτωση ζημιάς πληρώνει η ίδια μέχρι εξακόσια ευρώ", "Ότι πρέπει να αφήσει εγγύηση εξακόσια ευρώ σε μετρητά", "Ότι η ασφάλεια κοστίζει εξακόσια ευρώ"], 1, "αν πάθει ζημιά το αυτοκίνητο, πληρώνετε εσείς μέχρι εξακόσια ευρώ"),
  Q("Τι ΔΕΝ καλύπτει η πλήρης ασφάλεια;", ["Τα τζάμια", "Τα λάστιχα", "Ζημιές κάτω από το αυτοκίνητο σε χωματόδρομο", "Κλοπή"], 2, "σε χωματόδρομους δεν καλύπτεται η ζημιά κάτω από το αυτοκίνητο"),
  Q("Τι ισχύει για τη βενζίνη;", ["Είναι δωρεάν", "Πρέπει να επιστρέψει το αυτοκίνητο με γεμάτο ρεζερβουάρ", "Πληρώνει μόνο ό,τι καταναλώσει, σε τιμή βενζινάδικου", "Πρέπει να το επιστρέψει με άδειο ρεζερβουάρ"], 1, "Το παραλαμβάνετε με γεμάτο ρεζερβουάρ και το επιστρέφετε γεμάτο."),
 ],
 "gloss": {"ενοικίασης": "ενοικίαση — hire, rental", "κράτηση": "κράτηση — booking", "ασφάλεια": "ασφάλεια — insurance", "απαλλαγή": "απαλλαγή — excess (insurance), exemption", "ζημιά": "ζημιά — damage", "κάλυψη": "κάλυψη — cover", "λάστιχα": "λάστιχο — tyre", "τζάμια": "τζάμι — window (pane), glass", "χωματόδρομο": "χωματόδρομος — dirt road", "συμβόλαιο": "συμβόλαιο — contract", "άσφαλτος": "άσφαλτος — asphalt, tarmac", "ρεζερβουάρ": "ρεζερβουάρ — (fuel) tank", "βενζινάδικο": "βενζινάδικο — petrol station"},
})

ITEMS.append({
 "id": "l10-dia-goneis", "title": "Συνάντηση με τη δασκάλα", "title_en": "Meeting the teacher", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση ανάμεσα σε μια δασκάλα δημοτικού και τον πατέρα ενός μαθητή, του Άρη.",
 "script": [
  L("Δασκάλα", "f", "Σας ευχαριστώ που ήρθατε, κύριε Βλάχο. Ήθελα να μιλήσουμε για τον Άρη. Είναι έξυπνο παιδί και στα μαθηματικά είναι από τους καλύτερους της τάξης.", "Thank you for coming, Mr Vlachos. I wanted us to talk about Aris. He's a bright child and in maths he's one of the best in the class."),
  L("Πατέρας", "m", "Χαίρομαι που το ακούω. Υπάρχει όμως κάποιο πρόβλημα, έτσι δεν είναι;", "I'm glad to hear it. But there is some problem, isn't there?"),
  L("Δασκάλα", "f", "Όχι πρόβλημα ακριβώς. Τις τελευταίες εβδομάδες τον βλέπω αφηρημένο, κουρασμένο. Δυο τρεις φορές αποκοιμήθηκε στο θρανίο, και δεν φέρνει τις εργασίες του. Αναρωτιόμουν αν άλλαξε κάτι στο σπίτι.", "Not a problem exactly. In recent weeks I've seen him absent-minded, tired. Two or three times he fell asleep at his desk, and he isn't handing in his homework. I was wondering whether something had changed at home."),
  L("Πατέρας", "m", "Ίσως φταίει ότι γεννήθηκε η αδερφούλα του πριν από ενάμιση μήνα. Το μωρό ξυπνάει τη νύχτα και, για να πω την αλήθεια, ο Άρης έχει παραπονεθεί ότι τώρα όλοι ασχολούνται μόνο με εκείνη.", "Maybe it's because his little sister was born a month and a half ago. The baby wakes up at night and, to tell the truth, Aris has complained that now everyone pays attention only to her."),
  L("Δασκάλα", "f", "Αυτό εξηγεί πολλά, και είναι απολύτως φυσιολογικό. Θα πρότεινα να περνάτε λίγο χρόνο μόνο με εκείνον κάθε μέρα, έστω και μισή ώρα, χωρίς το μωρό. Κι εγώ θα του δώσω έναν ρόλο στην τάξη, να βοηθάει στα μαθηματικά τους συμμαθητές του, για να νιώσει ότι τον υπολογίζουν.", "That explains a lot, and it's completely normal. I'd suggest you spend a little time alone with him every day, even half an hour, without the baby. And I'll give him a role in class, helping his classmates with maths, so he feels he matters."),
 ],
 "questions": [
  Q("Τι ανησυχεί τη δασκάλα;", ["Οι κακοί βαθμοί του Άρη στα μαθηματικά", "Ότι ο Άρης φαίνεται κουρασμένος και αφηρημένος", "Ότι ο Άρης τσακώνεται με τους συμμαθητές του", "Ότι ο Άρης λείπει συχνά"], 1, "τον βλέπω αφηρημένο, κουρασμένο"),
  Q("Ποια εξήγηση δίνει ο πατέρας;", ["Ότι ο Άρης βλέπει τηλεόραση ως αργά", "Ότι μετακόμισαν", "Ότι γεννήθηκε η αδερφή του και το μωρό ξυπνάει τη νύχτα", "Ότι ο Άρης είναι άρρωστος"], 2, "γεννήθηκε η αδερφούλα του ... Το μωρό ξυπνάει τη νύχτα"),
  Q("Τι θα κάνει η δασκάλα;", ["Θα του βάλει περισσότερες εργασίες", "Θα του δώσει ρόλο βοηθού στα μαθηματικά", "Θα τον στείλει στον ψυχολόγο του σχολείου", "Θα τον αλλάξει θέση"], 1, "θα του δώσω έναν ρόλο στην τάξη, να βοηθάει στα μαθηματικά τους συμμαθητές του"),
 ],
 "gloss": {"αφηρημένο": "αφηρημένος — absent-minded", "αποκοιμήθηκε": "αποκοιμιέμαι — to fall asleep, doze off", "θρανίο": "θρανίο — school desk", "εργασίες": "εργασία — (home)work, assignment", "Αναρωτιόμουν": "αναρωτιέμαι — to wonder", "αδερφούλα": "αδερφούλα — little sister", "έχει παραπονεθεί": "παραπονιέμαι — to complain", "φυσιολογικό": "φυσιολογικός — normal", "έστω": "έστω — even (if only)", "συμμαθητές": "συμμαθητής — classmate", "τον υπολογίζουν": "υπολογίζω κάποιον — to take someone into account, value"},
})

ITEMS.append({
 "id": "l10-mon-kapnisma", "title": "Πώς έκοψα το τσιγάρο", "title_en": "How I quit smoking", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε τον Παναγιώτη, πενήντα πέντε χρονών, να μιλάει για το πώς έκοψε το κάπνισμα.",
 "script": [
  L("Παναγιώτης", "m", "Κάπνιζα τριάντα χρόνια, ένα πακέτο τη μέρα, μερικές φορές και παραπάνω. Είχα προσπαθήσει να το κόψω τουλάχιστον πέντε φορές. Την πιο μεγάλη φορά άντεξα τρεις μήνες, και μετά, σε έναν γάμο, ένας φίλος μού είπε «ένα δεν σε πειράζει». Την επόμενη μέρα αγόραζα πάλι πακέτο.", "I smoked for thirty years, a pack a day, sometimes more. I had tried to quit at least five times. The longest time I lasted three months, and then, at a wedding, a friend told me 'one won't hurt you'. The next day I was buying a pack again."),
  L("Παναγιώτης", "m", "Αυτή τη φορά άλλαξα δύο πράγματα. Πρώτον, πήγα στο ιατρείο διακοπής καπνίσματος του νοσοκομείου, που είναι δωρεάν. Η γιατρός μού εξήγησε ότι η νικοτίνη είναι εξάρτηση και όχι θέμα θέλησης, και μου έδωσε μια θεραπεία για τις πρώτες δύσκολες εβδομάδες. Δεύτερον, σκέφτηκα πότε ακριβώς άναβα τσιγάρο: με τον πρωινό καφέ, στο αυτοκίνητο, μετά το φαγητό. Και άλλαξα αυτές τις συνήθειες. Τον καφέ τον έπινα πια όρθιος, στο μπαλκόνι, και στο αυτοκίνητο είχα πάντα τσίχλες.", "This time I changed two things. First, I went to the hospital's stop-smoking clinic, which is free. The doctor explained that nicotine is an addiction and not a matter of willpower, and she gave me a treatment for the first difficult weeks. Second, I thought about exactly when I lit a cigarette: with my morning coffee, in the car, after meals. And I changed those habits. I drank my coffee standing up, on the balcony, and in the car I always had chewing gum."),
  L("Παναγιώτης", "m", "Έχουν περάσει δύο χρόνια. Ανεβαίνω τα σκαλιά χωρίς να λαχανιάζω, νιώθω ξανά τις γεύσεις, και με τα λεφτά που γλίτωσα πήγαμε με τη γυναίκα μου ταξίδι στη Βιέννη. Ακόμα και σήμερα, όμως, όταν μου προσφέρουν τσιγάρο, λέω «όχι, ευχαριστώ, δεν καπνίζω», και όχι «το έκοψα». Είναι μικρή διαφορά, αλλά για μένα σημαντική.", "Two years have passed. I climb the stairs without getting out of breath, I can taste flavours again, and with the money I saved my wife and I went on a trip to Vienna. Even today, though, when people offer me a cigarette, I say 'no thanks, I don't smoke', not 'I've quit'. It's a small difference, but an important one for me."),
 ],
 "questions": [
  Q("Τι συνέβη στην πιο μεγάλη από τις προηγούμενες προσπάθειές του;", ["Άντεξε έναν χρόνο", "Ξανάρχισε μετά από τρεις μήνες, επειδή δέχτηκε ένα τσιγάρο σε γάμο", "Αρρώστησε", "Τον βοήθησε ένας φίλος"], 1, "άντεξα τρεις μήνες, και μετά, σε έναν γάμο, ένας φίλος μού είπε «ένα δεν σε πειράζει»"),
  Q("Τι του εξήγησε η γιατρός;", ["Ότι το κάπνισμα είναι θέμα θέλησης", "Ότι η νικοτίνη προκαλεί εξάρτηση", "Ότι πρέπει να το κόψει σιγά σιγά", "Ότι δεν χρειάζεται θεραπεία"], 1, "η νικοτίνη είναι εξάρτηση και όχι θέμα θέλησης"),
  Q("Ποια στρατηγική χρησιμοποίησε;", ["Άλλαξε τις συνήθειες που συνδέονταν με το τσιγάρο", "Σταμάτησε να πίνει καφέ", "Πούλησε το αυτοκίνητό του", "Απέφευγε τους φίλους του"], 0, "σκέφτηκα πότε ακριβώς άναβα τσιγάρο ... Και άλλαξα αυτές τις συνήθειες."),
  Q("Γιατί προτιμά να λέει «δεν καπνίζω» αντί «το έκοψα»;", ["Γιατί είναι πιο ευγενικό", "Γιατί έτσι νιώθει ότι δεν είναι πια καπνιστής, όχι απλώς κάποιος που σταμάτησε", "Γιατί ντρέπεται που κάπνιζε", "Γιατί δεν τον πιστεύουν"], 1, "Είναι μικρή διαφορά, αλλά για μένα σημαντική."),
 ],
 "gloss": {"πακέτο": "πακέτο — pack(et)", "να το κόψω": "κόβω (το τσιγάρο) — to give up (smoking)", "άντεξα": "αντέχω — to last, hold out", "ιατρείο διακοπής καπνίσματος": "ιατρείο διακοπής καπνίσματος — stop-smoking clinic", "εξάρτηση": "εξάρτηση — addiction, dependence", "θέλησης": "θέληση — willpower", "άναβα": "ανάβω — to light", "τσίχλες": "τσίχλα — chewing gum", "λαχανιάζω": "λαχανιάζω — to get out of breath", "γλίτωσα": "γλιτώνω — to save, spare"},
})

ITEMS.append({
 "id": "l10-rep-laxanokipos", "title": "Ένας λαχανόκηπος ανάμεσα στις πολυκατοικίες", "title_en": "A vegetable garden among the apartment blocks", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για έναν δημοτικό λαχανόκηπο σε μια πυκνοκατοικημένη συνοικία.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε ένα οικόπεδο που για χρόνια ήταν γεμάτο μπάζα και αγριόχορτα, ανάμεσα σε εξαώροφες πολυκατοικίες, φυτρώνουν σήμερα ντομάτες, κολοκυθάκια και βασιλικός. Ο δήμος χώρισε τον χώρο σε εξήντα μικρά κομμάτια των είκοσι τετραγωνικών μέτρων και τα παραχώρησε δωρεάν σε κατοίκους της περιοχής.", "On a plot that for years was full of rubble and weeds, between six-storey apartment blocks, tomatoes, courgettes and basil grow today. The municipality divided the space into sixty small plots of twenty square metres and gave them free of charge to local residents."),
  L("Ρεπόρτερ", "m", "Οι αιτήσεις ήταν τριπλάσιες από τα διαθέσιμα κομμάτια, γι' αυτό έγινε κλήρωση, με προτεραιότητα σε συνταξιούχους, ανέργους και οικογένειες με παιδιά. Οι καλλιεργητές πρέπει να τηρούν κάποιους κανόνες: απαγορεύονται τα χημικά φυτοφάρμακα, και όποιος αφήσει το κομμάτι του απεριποίητο για δύο μήνες το χάνει.", "Applications were three times the available plots, so there was a draw, with priority for pensioners, the unemployed and families with children. The growers must follow some rules: chemical pesticides are banned, and anyone who leaves their plot untended for two months loses it."),
  L("Ρεπόρτερ", "m", "Πέρα από τα λαχανικά, ο κήπος έφερε κάτι που δεν είχε προβλεφθεί: γειτονιά. Άνθρωποι που ζούσαν χρόνια στον ίδιο δρόμο χωρίς να λένε καλημέρα ανταλλάσσουν τώρα σπόρους και συμβουλές, και το καλοκαίρι οργανώνουν μια γιορτή συγκομιδής. Το σχολείο της περιοχής έχει δικό του κομμάτι, όπου οι μαθητές μαθαίνουν από πού έρχεται το φαγητό τους.", "Beyond the vegetables, the garden has brought something nobody had foreseen: a sense of neighbourhood. People who had lived for years on the same street without saying good morning now exchange seeds and advice, and in summer they organise a harvest festival. The local school has its own plot, where pupils learn where their food comes from."),
 ],
 "questions": [
  Q("Τι ήταν παλιά ο χώρος του κήπου;", ["Πάρκινγκ", "Ένα εγκαταλειμμένο οικόπεδο με μπάζα", "Παιδική χαρά", "Λαϊκή αγορά"], 1, "Σε ένα οικόπεδο που για χρόνια ήταν γεμάτο μπάζα και αγριόχορτα"),
  Q("Πώς μοιράστηκαν τα κομμάτια;", ["Με σειρά προτεραιότητας στις αιτήσεις", "Με κλήρωση, με προτεραιότητα σε ορισμένες ομάδες", "Τα αγόρασαν οι κάτοικοι", "Τα πήραν μόνο οι συνταξιούχοι"], 1, "έγινε κλήρωση, με προτεραιότητα σε συνταξιούχους, ανέργους και οικογένειες με παιδιά"),
  Q("Πότε χάνει κάποιος το κομμάτι του;", ["Αν χρησιμοποιήσει βιολογικά λιπάσματα", "Αν το αφήσει απεριποίητο για δύο μήνες", "Αν πουλήσει τα λαχανικά του", "Αν δεν πάει στη γιορτή"], 1, "όποιος αφήσει το κομμάτι του απεριποίητο για δύο μήνες το χάνει"),
  Q("Ποιο απρόσμενο αποτέλεσμα είχε ο κήπος;", ["Ανέβηκαν οι τιμές των σπιτιών", "Δημιουργήθηκαν δεσμοί ανάμεσα στους γείτονες", "Μειώθηκαν τα σκουπίδια", "Έκλεισε η λαϊκή"], 1, "ο κήπος έφερε κάτι που δεν είχε προβλεφθεί: γειτονιά"),
 ],
 "gloss": {"λαχανόκηπο": "λαχανόκηπος — vegetable garden", "πυκνοκατοικημένη": "πυκνοκατοικημένος — densely populated", "οικόπεδο": "οικόπεδο — plot (of land)", "μπάζα": "μπάζα — rubble", "αγριόχορτα": "αγριόχορτο — weed", "φυτρώνουν": "φυτρώνω — to grow, sprout", "κολοκυθάκια": "κολοκυθάκι — courgette", "βασιλικός": "βασιλικός — basil", "παραχώρησε": "παραχωρώ — to grant, hand over", "κλήρωση": "κλήρωση — draw, lottery", "καλλιεργητές": "καλλιεργητής — grower", "φυτοφάρμακα": "φυτοφάρμακο — pesticide", "απεριποίητο": "απεριποίητος — untended, neglected", "σπόρους": "σπόρος — seed", "συγκομιδής": "συγκομιδή — harvest"},
})

ITEMS.append({
 "id": "l10-rep-ilektrika", "title": "Τα ηλεκτρικά λεωφορεία", "title_en": "The electric buses", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τα νέα ηλεκτρικά λεωφορεία μιας μεγάλης πόλης.",
 "script": [
  L("Ρεπόρτερ", "f", "Από αυτή την εβδομάδα κυκλοφορούν στους δρόμους της πόλης τα πρώτα σαράντα ηλεκτρικά λεωφορεία. Το πρώτο που προσέχουν οι επιβάτες είναι η ησυχία: δεν ακούγεται ο θόρυβος της μηχανής ούτε μυρίζει πετρέλαιο στις στάσεις.", "From this week the first forty electric buses are running on the city's streets. The first thing passengers notice is the quiet: you can't hear the engine noise and there's no smell of diesel at the stops."),
  L("Ρεπόρτερ", "f", "Κάθε λεωφορείο φορτίζει τη νύχτα στο αμαξοστάσιο και έχει αυτονομία περίπου διακόσια πενήντα χιλιόμετρα, αρκετά για μια ολόκληρη μέρα δρομολογίων. Οι οδηγοί εκπαιδεύτηκαν σε έναν διαφορετικό τρόπο οδήγησης: όταν φρενάρουν ομαλά, η μπαταρία ξαναφορτίζει, οπότε η ήρεμη οδήγηση εξοικονομεί ενέργεια.", "Each bus charges overnight at the depot and has a range of about two hundred and fifty kilometres, enough for a whole day of routes. Drivers were trained in a different way of driving: when they brake smoothly the battery recharges, so calm driving saves energy."),
  L("Ρεπόρτερ", "f", "Δεν λείπουν όμως και οι επιφυλάξεις. Οι εργαζόμενοι επισημαίνουν ότι τα λεωφορεία είναι λίγα σε σχέση με τις ανάγκες, και ότι το πραγματικό πρόβλημα των επιβατών δεν είναι το καύσιμο, αλλά η αναμονή στις στάσεις. Η εταιρεία απαντά ότι μέχρι το τέλος της επόμενης χρονιάς θα παραληφθούν άλλα εκατόν είκοσι οχήματα και ότι θα δημιουργηθούν νέες λεωφορειολωρίδες.", "But there are reservations too. Workers point out that there are few buses compared with what is needed, and that passengers' real problem isn't the fuel but the waiting at stops. The company replies that by the end of next year another hundred and twenty vehicles will be delivered and new bus lanes will be created."),
 ],
 "questions": [
  Q("Τι προσέχουν πρώτα οι επιβάτες στα νέα λεωφορεία;", ["Ότι είναι πιο γρήγορα", "Ότι είναι αθόρυβα και δεν μυρίζουν καυσαέρια", "Ότι είναι πιο φθηνά", "Ότι έχουν δωρεάν ίντερνετ"], 1, "δεν ακούγεται ο θόρυβος της μηχανής ούτε μυρίζει πετρέλαιο"),
  Q("Γιατί εκπαιδεύτηκαν οι οδηγοί;", ["Για να οδηγούν πιο γρήγορα", "Γιατί η ήπια οδήγηση και το ομαλό φρενάρισμα εξοικονομούν ενέργεια", "Για να επισκευάζουν τις μπαταρίες", "Για να εξυπηρετούν τουρίστες"], 1, "όταν φρενάρουν ομαλά, η μπαταρία ξαναφορτίζει, οπότε η ήρεμη οδήγηση εξοικονομεί ενέργεια"),
  Q("Ποια επιφύλαξη εκφράζουν οι εργαζόμενοι;", ["Ότι οι μπαταρίες είναι επικίνδυνες", "Ότι τα λεωφορεία είναι πολύ μεγάλα", "Ότι τα λεωφορεία είναι λίγα και η αναμονή στις στάσεις παραμένει πρόβλημα", "Ότι οι μισθοί τους μειώθηκαν"], 2, "τα λεωφορεία είναι λίγα σε σχέση με τις ανάγκες ... το πραγματικό πρόβλημα ... η αναμονή στις στάσεις"),
 ],
 "gloss": {"κυκλοφορούν": "κυκλοφορώ — to run, circulate", "φορτίζει": "φορτίζω — to charge", "αμαξοστάσιο": "αμαξοστάσιο — (bus) depot", "αυτονομία": "αυτονομία — range (of a vehicle), autonomy", "φρενάρουν": "φρενάρω — to brake", "ομαλά": "ομαλά — smoothly", "εξοικονομεί": "εξοικονομώ — to save", "επιφυλάξεις": "επιφύλαξη — reservation", "επισημαίνουν": "επισημαίνω — to point out", "καύσιμο": "καύσιμο — fuel", "αναμονή": "αναμονή — waiting", "οχήματα": "όχημα — vehicle", "λεωφορειολωρίδες": "λεωφορειολωρίδα — bus lane"},
})

ITEMS.append({
 "id": "l10-int-melissokomos", "title": "Μια νέα μελισσοκόμος", "title_en": "A young beekeeper", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με την Ιφιγένεια, μια μελισσοκόμο από την Εύβοια.",
 "script": [
  L("Δημοσιογράφος", "m", "Ιφιγένεια, σπούδασες οικονομικά και δούλευες σε τράπεζα. Πώς έγινες μελισσοκόμος;", "Ifigeneia, you studied economics and worked in a bank. How did you become a beekeeper?"),
  L("Ιφιγένεια", "f", "Ο θείος μου είχε κυψέλες στη βόρεια Εύβοια. Όταν τις κατέστρεψαν οι μεγάλες πυρκαγιές του 2021, ήταν έτοιμος να τα παρατήσει. Πήγα να τον βοηθήσω να ξαναρχίσει, για ένα καλοκαίρι, και δεν γύρισα ποτέ στην τράπεζα.", "My uncle had hives in northern Evia. When the big fires of 2021 destroyed them, he was ready to give up. I went to help him start again, for one summer, and I never went back to the bank."),
  L("Δημοσιογράφος", "m", "Πώς είναι η δουλειά μετά τις φωτιές;", "What is the work like after the fires?"),
  L("Ιφιγένεια", "f", "Πολύ δύσκολη. Το πευκόμελο, που ήταν το βασικό μας προϊόν, χρειάζεται πεύκα, και τα πεύκα θέλουν δεκαετίες για να μεγαλώσουν. Έτσι μεταφέρουμε τις κυψέλες σε άλλες περιοχές, ανάλογα με την εποχή: την άνοιξη σε ανθισμένα χωράφια, το καλοκαίρι στο θυμάρι, στα βουνά. Οι μέλισσες είναι στην ουσία νομάδες.", "Very difficult. Pine honey, our main product, needs pine trees, and pines take decades to grow. So we move the hives to other areas depending on the season: in spring to fields in bloom, in summer to the thyme in the mountains. The bees are essentially nomads."),
  L("Δημοσιογράφος", "m", "Ακούμε συχνά ότι οι μέλισσες κινδυνεύουν. Το βλέπετε κι εσείς;", "We often hear that bees are in danger. Do you see that too?"),
  L("Ιφιγένεια", "f", "Ναι. Η ζέστη, τα φυτοφάρμακα και ένα παράσιτο, η βαρρόα, εξασθενούν τα μελίσσια. Κάθε χειμώνα χάνουμε περισσότερα από ό,τι πριν από δέκα χρόνια. Όποιος θέλει να βοηθήσει μπορεί να φυτέψει λουλούδια στο μπαλκόνι του και να αγοράζει μέλι απευθείας από μελισσοκόμους. Χωρίς μέλισσες, δεν χάνουμε μόνο το μέλι, χάνουμε τα μισά φρούτα και λαχανικά μας.", "Yes. The heat, pesticides and a parasite, varroa, weaken the colonies. Every winter we lose more than ten years ago. Anyone who wants to help can plant flowers on their balcony and buy honey directly from beekeepers. Without bees we don't just lose honey, we lose half our fruit and vegetables."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η Ιφιγένεια τη μελισσοκομία;", ["Σπούδασε γεωπονία", "Πήγε να βοηθήσει τον θείο της μετά τις πυρκαγιές και έμεινε", "Κληρονόμησε κυψέλες", "Ήταν το χόμπι της από παιδί"], 1, "Πήγα να τον βοηθήσω να ξαναρχίσει, για ένα καλοκαίρι, και δεν γύρισα ποτέ στην τράπεζα."),
  Q("Γιατί μετακινούν τις κυψέλες;", ["Για να τις προστατέψουν από κλέφτες", "Γιατί τα καμένα πεύκα δεν έχουν ακόμη ξαναμεγαλώσει και ακολουθούν τα λουλούδια κάθε εποχής", "Γιατί το απαιτεί ο νόμος", "Για να πουλήσουν σε άλλες αγορές"], 1, "τα πεύκα θέλουν δεκαετίες για να μεγαλώσουν. Έτσι μεταφέρουμε τις κυψέλες σε άλλες περιοχές, ανάλογα με την εποχή"),
  Q("Τι συμβουλεύει όσους θέλουν να βοηθήσουν τις μέλισσες;", ["Να κάνουν δωρεές", "Να φυτεύουν λουλούδια και να αγοράζουν μέλι από μελισσοκόμους", "Να γίνουν εθελοντές στην Εύβοια", "Να τρώνε λιγότερο μέλι"], 1, "μπορεί να φυτέψει λουλούδια στο μπαλκόνι του και να αγοράζει μέλι απευθείας από μελισσοκόμους"),
 ],
 "gloss": {"μελισσοκόμος": "μελισσοκόμος — beekeeper", "κυψέλες": "κυψέλη — beehive", "πυρκαγιές": "πυρκαγιά — (large) fire", "να τα παρατήσει": "τα παρατάω — to give up", "πευκόμελο": "πευκόμελο — pine honey", "ανθισμένα": "ανθισμένος — in bloom", "θυμάρι": "θυμάρι — thyme", "νομάδες": "νομάδας — nomad", "παράσιτο": "παράσιτο — parasite", "εξασθενούν": "εξασθενώ — to weaken", "μελίσσια": "μελίσσι — (bee) colony, swarm", "απευθείας": "απευθείας — directly"},
})

ITEMS.append({
 "id": "l10-int-noimatiki", "title": "Διερμηνέας της νοηματικής", "title_en": "A sign language interpreter", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με τον Σπύρο, διερμηνέα της ελληνικής νοηματικής γλώσσας.",
 "script": [
  L("Δημοσιογράφος", "f", "Σπύρο, πολλοί σε έχουν δει στην τηλεόραση, στο κάτω μέρος της οθόνης, την ώρα των ειδήσεων. Πώς έμαθες τη νοηματική;", "Spyros, many people have seen you on television, at the bottom of the screen, during the news. How did you learn sign language?"),
  L("Σπύρος", "m", "Είμαι αυτό που λέμε «παιδί κωφών γονιών». Η νοηματική ήταν η πρώτη μου γλώσσα· τα ελληνικά τα έμαθα από τη γιαγιά μου και στο νηπιαγωγείο. Για χρόνια ήμουν ο άτυπος διερμηνέας της οικογένειας, στον γιατρό, στην τράπεζα, ακόμα και στις συναντήσεις γονέων στο σχολείο μου. Ήταν βάρος για ένα παιδί, αλλά και μια πρώτη εκπαίδευση.", "I'm what we call a 'child of deaf adults'. Sign language was my first language; I learned Greek from my grandmother and at nursery school. For years I was the family's informal interpreter, at the doctor's, at the bank, even at parents' meetings at my own school. It was a burden for a child, but also a first training."),
  L("Δημοσιογράφος", "f", "Πολλοί πιστεύουν ότι η νοηματική είναι απλώς τα ελληνικά με χειρονομίες. Ισχύει;", "Many people think sign language is just Greek with gestures. Is that true?"),
  L("Σπύρος", "m", "Καθόλου, και αυτή είναι η πιο συνηθισμένη παρεξήγηση. Η ελληνική νοηματική είναι αυτόνομη γλώσσα, με δικό της λεξιλόγιο και δική της γραμματική, που αξιοποιεί τον χώρο, την κίνηση και την έκφραση του προσώπου. Για παράδειγμα, μια ερώτηση δεν φαίνεται μόνο από τα χέρια, αλλά από τα φρύδια. Αναγνωρίστηκε επίσημα από το κράτος το 2017, κάτι που η κοινότητα των κωφών διεκδικούσε για δεκαετίες.", "Not at all, and that's the most common misconception. Greek Sign Language is an independent language, with its own vocabulary and its own grammar, which makes use of space, movement and facial expression. For example, a question isn't shown only by the hands but by the eyebrows. It was officially recognised by the state in 2017, something the deaf community had been demanding for decades."),
  L("Δημοσιογράφος", "f", "Ποια είναι η μεγαλύτερη δυσκολία στη δουλειά σου;", "What is the biggest difficulty in your job?"),
  L("Σπύρος", "m", "Η ταχύτητα και η ευθύνη. Στις ειδήσεις, ο παρουσιαστής δεν περιμένει να τελειώσω. Πρέπει να αποφασίζω μέσα σε δευτερόλεπτα πώς θα αποδώσω μια λέξη για την οποία δεν υπάρχει καθιερωμένο νόημα, όπως έναν νέο οικονομικό όρο. Και ξέρω ότι, για πολλούς ανθρώπους, εκείνη τη στιγμή εγώ είμαι η μόνη πρόσβαση στην ενημέρωση.", "Speed and responsibility. On the news, the presenter doesn't wait for me to finish. I have to decide within seconds how to render a word for which there is no established sign, like a new economic term. And I know that, for many people, at that moment I am their only access to the news."),
 ],
 "questions": [
  Q("Πώς έμαθε ο Σπύρος τη νοηματική;", ["Σε σχολή διερμηνέων", "Ως πρώτη του γλώσσα, από τους κωφούς γονείς του", "Από τη γιαγιά του", "Στο νηπιαγωγείο"], 1, "Είμαι αυτό που λέμε «παιδί κωφών γονιών». Η νοηματική ήταν η πρώτη μου γλώσσα"),
  Q("Ποια παρεξήγηση διορθώνει;", ["Ότι η νοηματική είναι ίδια σε όλο τον κόσμο", "Ότι η νοηματική είναι τα ελληνικά με χειρονομίες, ενώ είναι αυτόνομη γλώσσα", "Ότι οι κωφοί δεν μπορούν να διαβάσουν", "Ότι η νοηματική δεν έχει γραμματική"], 1, "Η ελληνική νοηματική είναι αυτόνομη γλώσσα, με δικό της λεξιλόγιο και δική της γραμματική"),
  Q("Τι παράδειγμα δίνει για τη γραμματική της νοηματικής;", ["Ότι τα ρήματα δεν έχουν χρόνους", "Ότι μια ερώτηση δηλώνεται και με τα φρύδια", "Ότι δεν υπάρχουν ουσιαστικά", "Ότι χρησιμοποιεί μόνο το ένα χέρι"], 1, "μια ερώτηση δεν φαίνεται μόνο από τα χέρια, αλλά από τα φρύδια"),
  Q("Γιατί νιώθει μεγάλη ευθύνη στις ειδήσεις;", ["Γιατί τον βλέπουν οι συνάδελφοί του", "Γιατί για πολλούς κωφούς είναι η μόνη πρόσβαση στην ενημέρωση εκείνη τη στιγμή", "Γιατί οι ειδήσεις είναι ζωντανές και δεν επιτρέπονται λάθη από τον παρουσιαστή", "Γιατί πληρώνεται ανάλογα με τα λάθη του"], 1, "για πολλούς ανθρώπους, εκείνη τη στιγμή εγώ είμαι η μόνη πρόσβαση στην ενημέρωση"),
 ],
 "gloss": {"διερμηνέας": "διερμηνέας — interpreter", "νοηματική": "νοηματική (γλώσσα) — sign language", "κωφών": "κωφός — deaf", "νηπιαγωγείο": "νηπιαγωγείο — nursery school, kindergarten", "άτυπος": "άτυπος — informal", "χειρονομίες": "χειρονομία — gesture", "παρεξήγηση": "παρεξήγηση — misunderstanding", "αυτόνομη": "αυτόνομος — independent, autonomous", "αξιοποιεί": "αξιοποιώ — to make use of", "φρύδια": "φρύδι — eyebrow", "διεκδικούσε": "διεκδικώ — to claim, demand", "αποδώσω": "αποδίδω — to render, convey", "καθιερωμένο": "καθιερωμένος — established", "πρόσβαση": "πρόσβαση — access"},
})
rnd = random.Random(10)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-10.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
