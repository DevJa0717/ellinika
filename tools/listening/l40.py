# Source for library/listening/listening-40.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l40.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l40-ann-anaklisi", "title": "Ανάκληση προϊόντος", "title_en": "A product recall", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα μιας αλυσίδας σούπερ μάρκετ.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί πελάτες, σας ενημερώνουμε ότι, σε συνεννόηση με τον Ενιαίο Φορέα Ελέγχου Τροφίμων, αποσύρεται από τα ράφια το γιαούρτι στραγγιστό του ενός κιλού της εταιρείας «Λευκό Βουνό», με ημερομηνία λήξης δεκαπέντε Δεκεμβρίου. Σε έλεγχο διαπιστώθηκε ότι ορισμένες συσκευασίες ενδέχεται να περιέχουν μικρά κομμάτια πλαστικού.", "Dear customers, we inform you that, in consultation with the Hellenic Food Authority, the one-kilo strained yoghurt from the company \"Lefko Vouno\" with an expiry date of 15 December is being withdrawn from the shelves. An inspection found that some packs may contain small pieces of plastic."),
  L("Εκφωνήτρια", "f", "Οι υπόλοιπες συσκευασίες και οι άλλες ημερομηνίες λήξης δεν επηρεάζονται και μπορούν να καταναλωθούν κανονικά. Αν έχετε ήδη αγοράσει το συγκεκριμένο προϊόν, σας παρακαλούμε να μην το καταναλώσετε.", "The other packs and the other expiry dates are not affected and can be consumed as normal. If you have already bought this particular product, please do not eat it."),
  L("Εκφωνήτρια", "f", "Μπορείτε να το επιστρέψετε σε οποιοδήποτε κατάστημα της αλυσίδας, ακόμη και ανοιγμένο και χωρίς απόδειξη, και θα σας επιστραφεί ολόκληρο το ποσό. Για περισσότερες πληροφορίες, απευθυνθείτε στο γραφείο εξυπηρέτησης πελατών, δίπλα στα ταμεία. Ζητούμε συγγνώμη για την αναστάτωση.", "You can return it to any store in the chain, even opened and without a receipt, and the full amount will be refunded to you. For more information, please go to the customer service desk next to the tills. We apologise for the inconvenience."),
 ],
 "questions": [
  Q("Ποιο προϊόν αποσύρεται;", ["Όλα τα γιαούρτια της εταιρείας", "Ένα γιαούρτι ενός κιλού με συγκεκριμένη ημερομηνία λήξης", "Ένα γάλα με πλαστική συσκευασία", "Ένα τυρί που έληξε"], 1, "το γιαούρτι στραγγιστό του ενός κιλού… με ημερομηνία λήξης δεκαπέντε Δεκεμβρίου"),
  Q("Γιατί αποσύρεται;", ["Επειδή έληξε", "Επειδή μπορεί να περιέχει κομμάτια πλαστικού", "Επειδή έχει λάθος τιμή", "Επειδή δεν διατηρήθηκε στο ψυγείο"], 1, "ορισμένες συσκευασίες ενδέχεται να περιέχουν μικρά κομμάτια πλαστικού"),
  Q("Πώς μπορεί κανείς να πάρει πίσω τα χρήματά του;", ["Μόνο με απόδειξη και κλειστή συσκευασία", "Επιστρέφοντας το προϊόν σε οποιοδήποτε κατάστημα, ακόμη και χωρίς απόδειξη", "Στέλνοντας email στην εταιρεία", "Μόνο στο κατάστημα όπου το αγόρασε"], 1, "Μπορείτε να το επιστρέψετε σε οποιοδήποτε κατάστημα της αλυσίδας, ακόμη και ανοιγμένο και χωρίς απόδειξη"),
 ],
 "gloss": {"σε συνεννόηση": "σε συνεννόηση με — in consultation with", "αποσύρεται": "αποσύρομαι — to be withdrawn", "ράφια": "ράφι — shelf", "στραγγιστό": "στραγγιστός — strained", "ημερομηνία λήξης": "ημερομηνία λήξης — expiry date", "συσκευασίες": "συσκευασία — pack, packaging", "ενδέχεται": "ενδέχεται — may, it is possible that", "να καταναλωθούν": "καταναλώνομαι — to be consumed", "απόδειξη": "απόδειξη — receipt", "εξυπηρέτησης πελατών": "εξυπηρέτηση πελατών — customer service", "αναστάτωση": "αναστάτωση — inconvenience, disruption"},
})

ITEMS.append({
 "id": "l40-vm-katataxi", "title": "Τεστ κατάταξης", "title_en": "A placement test", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από ένα κέντρο ξένων γλωσσών στον τηλεφωνητή σας.",
 "script": [
  L("Γραμματεία", "f", "Καλημέρα σας, κύριε Ραφαηλίδη, από το κέντρο ξένων γλωσσών «Λόγος» σας παίρνω. Λάβαμε την αίτησή σας για τα τμήματα ενηλίκων στα ιταλικά. Πριν σας εντάξουμε σε κάποιο τμήμα, θα πρέπει να δώσετε ένα σύντομο τεστ κατάταξης, για να δούμε σε ποιο επίπεδο βρίσκεστε.", "Good morning, Mr Rafailidis, I'm calling from the \"Logos\" foreign language centre. We received your application for the adult classes in Italian. Before we put you in a class, you'll need to take a short placement test, so that we can see what level you are at."),
  L("Γραμματεία", "f", "Το τεστ έχει ένα γραπτό μέρος, περίπου σαράντα λεπτά, και μια μικρή συζήτηση με τη διδάσκουσα. Μπορείτε να έρθετε είτε την Τρίτη στις έξι το απόγευμα είτε το Σάββατο στις έντεκα το πρωί. Δεν χρειάζεται να διαβάσετε τίποτα· θέλουμε απλώς να δούμε τι ξέρετε.", "The test has a written part, about forty minutes, and a short conversation with the teacher. You can come either on Tuesday at six in the evening or on Saturday at eleven in the morning. You don't need to study anything; we just want to see what you know."),
  L("Γραμματεία", "f", "Τα μαθήματα αρχίζουν στις δεκαπέντε του μήνα. Αν γραφτείτε μέχρι το τέλος της εβδομάδας, έχετε έκπτωση δέκα τοις εκατό στα δίδακτρα του πρώτου τριμήνου. Παρακαλώ πείτε μου ποια μέρα σας βολεύει, στο τηλέφωνο της γραμματείας ή με ένα email. Ευχαριστώ.", "Lessons begin on the fifteenth of the month. If you enrol by the end of the week, you get a ten per cent discount on the first term's fees. Please let me know which day suits you, on the office phone or by email. Thank you."),
 ],
 "questions": [
  Q("Γιατί πρέπει ο κύριος Ραφαηλίδης να δώσει τεστ;", ["Για να πάρει πιστοποιητικό", "Για να δουν σε ποιο επίπεδο βρίσκεται", "Επειδή δεν πλήρωσε τα δίδακτρα", "Για να γίνει καθηγητής"], 1, "για να δούμε σε ποιο επίπεδο βρίσκεστε"),
  Q("Από τι αποτελείται το τεστ;", ["Μόνο από μια συνέντευξη", "Από ένα γραπτό μέρος και μια μικρή συζήτηση", "Από μια εργασία για το σπίτι", "Από ένα τεστ ακουστικής κατανόησης"], 1, "Το τεστ έχει ένα γραπτό μέρος… και μια μικρή συζήτηση με τη διδάσκουσα"),
  Q("Πώς μπορεί να πάρει έκπτωση;", ["Αν φέρει έναν φίλο", "Αν γραφτεί μέχρι το τέλος της εβδομάδας", "Αν πληρώσει όλη τη χρονιά", "Αν περάσει το τεστ με άριστα"], 1, "Αν γραφτείτε μέχρι το τέλος της εβδομάδας, έχετε έκπτωση δέκα τοις εκατό"),
 ],
 "gloss": {"κέντρο ξένων γλωσσών": "κέντρο ξένων γλωσσών — language school", "τμήματα": "τμήμα — class, group", "ενηλίκων": "ενήλικος — adult", "σας εντάξουμε": "εντάσσω — to place, include", "τεστ κατάταξης": "τεστ κατάταξης — placement test", "διδάσκουσα": "διδάσκουσα — (female) teacher", "γραφτείτε": "γράφομαι — to enrol", "δίδακτρα": "δίδακτρα — tuition fees", "τριμήνου": "τρίμηνο — term, quarter", "σας βολεύει": "βολεύει — it suits"},
})

ITEMS.append({
 "id": "l40-dia-enoikiasi", "title": "Ενοικίαση αυτοκινήτου", "title_en": "Renting a car", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα γραφείο ενοικίασης αυτοκινήτων στο λιμάνι της Νάξου.",
 "script": [
  L("Τουρίστρια", "f", "Καλησπέρα. Θα ήθελα ένα μικρό αυτοκίνητο για τέσσερις μέρες, από αύριο το πρωί. Θέλουμε να γυρίσουμε τα ορεινά χωριά.", "Good afternoon. I'd like a small car for four days, from tomorrow morning. We want to go round the mountain villages."),
  L("Υπάλληλος", "m", "Μάλιστα. Για τα ορεινά σάς προτείνω ένα αυτοκίνητο λίγο πιο δυνατό, γιατί οι ανηφόρες είναι απότομες. Η τιμή είναι σαράντα πέντε ευρώ τη μέρα, με πλήρη ασφάλεια. Χρειάζομαι το δίπλωμά σας, την ταυτότητα ή το διαβατήριο και μια πιστωτική κάρτα για την εγγύηση.", "Certainly. For the mountains I'd suggest a slightly more powerful car, because the climbs are steep. The price is forty-five euros a day, with full insurance. I need your driving licence, your ID card or passport and a credit card for the deposit."),
  L("Τουρίστρια", "f", "Η πλήρης ασφάλεια καλύπτει και τα λάστιχα; Μας είπαν ότι κάποιοι χωματόδρομοι είναι σε κακή κατάσταση.", "Does the full insurance also cover the tyres? We were told some of the dirt roads are in bad condition."),
  L("Υπάλληλος", "m", "Τα λάστιχα και τα τζάμια καλύπτονται, αλλά ζημιές στο κάτω μέρος του αυτοκινήτου από χωματόδρομο δεν καλύπτονται. Γι' αυτό σας συμβουλεύω να μείνετε στους ασφαλτοστρωμένους δρόμους. Το αυτοκίνητο το παραλαμβάνετε με γεμάτο ρεζερβουάρ και πρέπει να το επιστρέψετε επίσης γεμάτο.", "Tyres and windows are covered, but damage to the underside of the car from dirt roads is not. That's why I advise you to stay on the asphalt roads. You collect the car with a full tank and you must return it full as well."),
 ],
 "questions": [
  Q("Γιατί ο υπάλληλος προτείνει ένα πιο δυνατό αυτοκίνητο;", ["Επειδή είναι πιο φθηνό", "Επειδή οι ανηφόρες στα ορεινά είναι απότομες", "Επειδή είναι τέσσερα άτομα", "Επειδή τα μικρά αυτοκίνητα έχουν τελειώσει"], 1, "οι ανηφόρες είναι απότομες"),
  Q("Τι ΔΕΝ καλύπτει η πλήρης ασφάλεια;", ["Τα λάστιχα", "Ζημιές στο κάτω μέρος από χωματόδρομο", "Τα τζάμια", "Τίποτα, καλύπτει τα πάντα"], 1, "ζημιές στο κάτω μέρος του αυτοκινήτου από χωματόδρομο δεν καλύπτονται"),
  Q("Πώς πρέπει να επιστραφεί το αυτοκίνητο;", ["Πλυμένο", "Με γεμάτο ρεζερβουάρ", "Πριν από τις δέκα το πρωί", "Στο αεροδρόμιο"], 1, "πρέπει να το επιστρέψετε επίσης γεμάτο"),
 ],
 "gloss": {"ενοικίασης": "ενοικίαση — rental", "ορεινά": "ορεινός — mountain (adj.)", "ανηφόρες": "ανηφόρα — uphill climb", "πλήρη ασφάλεια": "πλήρης ασφάλεια — full insurance", "δίπλωμά": "δίπλωμα (οδήγησης) — driving licence", "εγγύηση": "εγγύηση — deposit, guarantee", "λάστιχα": "λάστιχο — tyre", "χωματόδρομοι": "χωματόδρομος — dirt road", "τζάμια": "τζάμι — window (glass)", "ασφαλτοστρωμένους": "ασφαλτοστρωμένος — paved, asphalted", "ρεζερβουάρ": "ρεζερβουάρ — fuel tank"},
})

ITEMS.append({
 "id": "l40-dia-podilato", "title": "Στο συνεργείο ποδηλάτων", "title_en": "At the bike repair shop", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο ανάμεσα σε μια πελάτισσα και έναν τεχνικό σε ένα συνεργείο ποδηλάτων.",
 "script": [
  L("Πελάτισσα", "f", "Γεια σας. Το ποδήλατό μου κάνει έναν περίεργο θόρυβο όταν αλλάζω ταχύτητες, και τα φρένα δεν πιάνουν καλά, ειδικά όταν βρέχει.", "Hello. My bike makes a strange noise when I change gear, and the brakes don't grip well, especially when it rains."),
  L("Τεχνικός", "m", "Για να δούμε. Η αλυσίδα είναι πολύ φθαρμένη και δεν έχει λαδωθεί εδώ και καιρό, γι' αυτό πηδάει στα γρανάζια. Και τα τακάκια των φρένων έχουν σχεδόν λιώσει. Πόσα χιλιόμετρα κάνετε περίπου;", "Let's see. The chain is very worn and hasn't been oiled for a long time, that's why it jumps on the gears. And the brake pads are almost worn through. Roughly how many kilometres do you do?"),
  L("Πελάτισσα", "f", "Πηγαίνω κάθε μέρα στη δουλειά, δέκα χιλιόμετρα πήγαινε έλα. Δεν το έχω πάει ποτέ για σέρβις εδώ και δύο χρόνια.", "I ride to work every day, ten kilometres there and back. I haven't taken it for a service in two years."),
  L("Τεχνικός", "m", "Τότε είναι φυσικό. Θα σας αλλάξω αλυσίδα και τακάκια και θα ρυθμίσω τις ταχύτητες. Θα κοστίσει γύρω στα πενήντα ευρώ και θα είναι έτοιμο αύριο το μεσημέρι. Και κάτι ακόμα: να λαδώνετε την αλυσίδα μία φορά τον μήνα, και πάντα μετά από βροχή. Έτσι θα κρατήσει πολύ περισσότερο.", "Then it's natural. I'll replace the chain and the pads and adjust the gears. It'll cost about fifty euros and it'll be ready tomorrow at midday. And one more thing: oil the chain once a month, and always after rain. That way it will last much longer."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με την αλυσίδα;", ["Έχει σπάσει", "Είναι φθαρμένη και δεν έχει λαδωθεί", "Είναι πολύ μεγάλη", "Έχει σκουριάσει από τη θάλασσα"], 1, "Η αλυσίδα είναι πολύ φθαρμένη και δεν έχει λαδωθεί εδώ και καιρό"),
  Q("Πόσο συχνά χρησιμοποιεί η πελάτισσα το ποδήλατο;", ["Μόνο τα Σαββατοκύριακα", "Κάθε μέρα για τη δουλειά", "Σπάνια", "Μόνο το καλοκαίρι"], 1, "Πηγαίνω κάθε μέρα στη δουλειά"),
  Q("Τι συμβουλεύει ο τεχνικός;", ["Να αγοράσει καινούργιο ποδήλατο", "Να λαδώνει την αλυσίδα μία φορά τον μήνα και μετά από βροχή", "Να μην οδηγεί όταν βρέχει", "Να φέρνει το ποδήλατο κάθε εβδομάδα"], 1, "να λαδώνετε την αλυσίδα μία φορά τον μήνα, και πάντα μετά από βροχή"),
 ],
 "gloss": {"ταχύτητες": "ταχύτητα — gear", "φρένα": "φρένο — brake", "δεν πιάνουν": "πιάνω — to grip, catch", "αλυσίδα": "αλυσίδα — chain", "φθαρμένη": "φθαρμένος — worn", "δεν έχει λαδωθεί": "λαδώνομαι — to be oiled", "γρανάζια": "γρανάζι — gear wheel, cog", "τακάκια": "τακάκι — brake pad", "πήγαινε έλα": "πήγαινε έλα — there and back", "θα ρυθμίσω": "ρυθμίζω — to adjust"},
})

ITEMS.append({
 "id": "l40-mono-ryzi", "title": "Το ρύζι της Χαλάστρας", "title_en": "The rice of Chalastra", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν αγρότη από τη Χαλάστρα, κοντά στη Θεσσαλονίκη, να μιλάει για την καλλιέργεια του ρυζιού.",
 "script": [
  L("Αγρότης", "m", "Πολλοί ξαφνιάζονται όταν τους λέω ότι η Ελλάδα παράγει ρύζι. Κι όμως, εδώ, στο δέλτα του Αξιού, οι οικογένειές μας το καλλιεργούν εδώ και δεκαετίες. Ο παππούς μου ήρθε ως πρόσφυγας από την Ανατολική Θράκη και ήταν από τους πρώτους που φύτεψαν ρύζι σε αυτά τα χωράφια.", "Many people are surprised when I tell them that Greece produces rice. And yet here, in the Axios delta, our families have been growing it for decades. My grandfather came as a refugee from Eastern Thrace and was one of the first to plant rice in these fields."),
  L("Αγρότης", "m", "Το ρύζι θέλει πολύ νερό. Την άνοιξη πλημμυρίζουμε τα χωράφια με νερό από το ποτάμι, και τα φυτά μεγαλώνουν μέσα σε αυτό ως τον Σεπτέμβριο. Από ψηλά, τον Ιούνιο, ο κάμπος μοιάζει με καθρέφτη. Πάνω από τους ορυζώνες πετούν ερωδιοί και φλαμίνγκο, γιατί η περιοχή είναι από τους σημαντικότερους υγροτόπους της χώρας.", "Rice needs a lot of water. In spring we flood the fields with water from the river, and the plants grow in it until September. From above, in June, the plain looks like a mirror. Herons and flamingos fly over the paddies, because the area is one of the most important wetlands in the country."),
  L("Αγρότης", "m", "Τα τελευταία χρόνια έχουμε δύο μεγάλα προβλήματα. Το πρώτο είναι η λειψυδρία: τα καλοκαίρια με λίγη βροχή το ποτάμι κατεβάζει λιγότερο νερό, και η θάλασσα μπαίνει στα χωράφια και τα αλατίζει. Το δεύτερο είναι οι τιμές· το ρύζι από την Ασία είναι πολύ φθηνότερο. Γι' αυτό προσπαθούμε να πουλάμε απευθείας στους καταναλωτές, με το όνομα του τόπου μας πάνω στη συσκευασία.", "In recent years we've had two big problems. The first is water shortage: in summers with little rain the river brings down less water, and the sea gets into the fields and makes them salty. The second is prices; rice from Asia is much cheaper. That's why we try to sell directly to consumers, with the name of our place on the packet."),
 ],
 "questions": [
  Q("Ποιος ήταν από τους πρώτους που φύτεψαν ρύζι στην περιοχή;", ["Ο πατέρας του", "Ο παππούς του, που ήρθε ως πρόσφυγας", "Ένας γεωπόνος από την Ασία", "Ο ίδιος"], 1, "Ο παππούς μου ήρθε ως πρόσφυγας από την Ανατολική Θράκη και ήταν από τους πρώτους"),
  Q("Γιατί ο κάμπος μοιάζει με καθρέφτη τον Ιούνιο;", ["Επειδή έχει χιονίσει", "Επειδή τα χωράφια είναι πλημμυρισμένα με νερό", "Επειδή υπάρχουν θερμοκήπια", "Επειδή έχει ξεραθεί"], 1, "Την άνοιξη πλημμυρίζουμε τα χωράφια με νερό από το ποτάμι"),
  Q("Τι συμβαίνει όταν το ποτάμι έχει λίγο νερό;", ["Τα πουλιά φεύγουν", "Η θάλασσα μπαίνει στα χωράφια και τα αλατίζει", "Το ρύζι ωριμάζει γρηγορότερα", "Οι τιμές πέφτουν"], 1, "η θάλασσα μπαίνει στα χωράφια και τα αλατίζει"),
 ],
 "gloss": {"καλλιέργεια": "καλλιέργεια — cultivation", "δέλτα": "δέλτα — (river) delta", "πρόσφυγας": "πρόσφυγας — refugee", "πλημμυρίζουμε": "πλημμυρίζω — to flood", "κάμπος": "κάμπος — plain", "ορυζώνες": "ορυζώνας — rice paddy", "ερωδιοί": "ερωδιός — heron", "υγροτόπους": "υγρότοπος — wetland", "λειψυδρία": "λειψυδρία — water shortage", "τα αλατίζει": "αλατίζω — to salt, make salty", "καταναλωτές": "καταναλωτής — consumer"},
})

ITEMS.append({
 "id": "l40-rep-sxolika-geymata", "title": "Ένα ζεστό φαγητό στο σχολείο", "title_en": "A hot meal at school", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ για ένα πρόγραμμα σχολικών γευμάτων.",
 "script": [
  L("Ρεπόρτερ", "f", "Είναι μεσημέρι στο δημοτικό σχολείο ενός χωριού της Αιτωλοακαρνανίας, και στην τραπεζαρία μυρίζει φακές. Εδώ και τρία χρόνια, κάθε μαθητής παίρνει δωρεάν ένα ζεστό γεύμα κάθε μέρα, στο πλαίσιο ενός κρατικού προγράμματος που εφαρμόζεται σε χιλιάδες σχολεία της χώρας.", "It's midday at the primary school of a village in Aitoloakarnania, and the dining room smells of lentils. For three years now, every pupil has received a free hot meal every day, as part of a state programme being applied in thousands of schools around the country."),
  L("Διευθυντής", "m", "Πριν από το πρόγραμμα, κάποια παιδιά έρχονταν χωρίς πρωινό και χωρίς κολατσιό. Οι δάσκαλοι το έβλεπαν στη συγκέντρωσή τους: μετά τις έντεκα δεν μπορούσαν να προσέξουν. Τώρα όλα τα παιδιά τρώνε το ίδιο φαγητό, στο ίδιο τραπέζι, και κανείς δεν ξεχωρίζει.", "Before the programme, some children came without breakfast and without a snack. The teachers saw it in their concentration: after eleven they couldn't pay attention. Now all the children eat the same food, at the same table, and nobody stands out."),
  L("Ρεπόρτερ", "f", "Τα γεύματα ετοιμάζονται από εταιρείες με βάση ένα μενού που έχουν καταρτίσει διαιτολόγοι, με όσπρια, λαχανικά και φρούτα. Δεν λείπουν και τα παράπονα: οι γονείς ζητούν περισσότερα τοπικά προϊόντα, ενώ σε ορισμένες περιοχές το φαγητό φτάνει κρύο. Το υπουργείο υπόσχεται βελτιώσεις στους επόμενους διαγωνισμούς.", "The meals are prepared by companies based on a menu drawn up by dietitians, with pulses, vegetables and fruit. There are complaints too: parents are asking for more local produce, while in some areas the food arrives cold. The ministry promises improvements in the next tenders."),
 ],
 "questions": [
  Q("Τι λαμβάνουν οι μαθητές μέσω του προγράμματος;", ["Δωρεάν βιβλία", "Ένα δωρεάν ζεστό γεύμα κάθε μέρα", "Ένα δωρεάν πρωινό μία φορά την εβδομάδα", "Έκπτωση στο κυλικείο"], 1, "κάθε μαθητής παίρνει δωρεάν ένα ζεστό γεύμα κάθε μέρα"),
  Q("Ποια αλλαγή επισημαίνει ο διευθυντής;", ["Τα παιδιά παίρνουν καλύτερους βαθμούς στα μαθηματικά", "Όλα τα παιδιά τρώνε μαζί το ίδιο φαγητό και κανείς δεν ξεχωρίζει", "Οι γονείς έρχονται πιο συχνά στο σχολείο", "Τα παιδιά φεύγουν νωρίτερα"], 1, "Τώρα όλα τα παιδιά τρώνε το ίδιο φαγητό, στο ίδιο τραπέζι, και κανείς δεν ξεχωρίζει"),
  Q("Ποιο παράπονο αναφέρεται;", ["Ότι οι μερίδες είναι μικρές", "Ότι σε ορισμένες περιοχές το φαγητό φτάνει κρύο", "Ότι το πρόγραμμα κοστίζει πολύ στους γονείς", "Ότι τα παιδιά δεν τρώνε όσπρια"], 1, "σε ορισμένες περιοχές το φαγητό φτάνει κρύο"),
 ],
 "gloss": {"τραπεζαρία": "τραπεζαρία — dining room", "γεύμα": "γεύμα — meal", "στο πλαίσιο": "στο πλαίσιο — as part of", "κολατσιό": "κολατσιό — snack", "συγκέντρωσή": "συγκέντρωση — concentration", "δεν ξεχωρίζει": "ξεχωρίζω — to stand out", "έχουν καταρτίσει": "καταρτίζω — to draw up", "διαιτολόγοι": "διαιτολόγος — dietitian", "όσπρια": "όσπρια — pulses, legumes", "παράπονα": "παράπονο — complaint", "διαγωνισμούς": "διαγωνισμός — (public) tender"},
})

ITEMS.append({
 "id": "l40-rep-omonoia", "title": "Η νέα Ομόνοια", "title_en": "The new Omonia", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα τηλεοπτικό ρεπορτάζ για την ανάπλαση μιας κεντρικής πλατείας της Αθήνας.",
 "script": [
  L("Ρεπόρτερ", "m", "Για δεκαετίες, η πλατεία Ομονοίας ήταν για πολλούς Αθηναίους ένας χώρος που απλώς διέσχιζαν βιαστικά. Τσιμέντο, κυκλοφοριακό χάος και λίγα παγκάκια. Μετά την τελευταία ανάπλαση, η εικόνα έχει αλλάξει: στο κέντρο της πλατείας λειτουργεί ξανά ένα μεγάλο σιντριβάνι, και γύρω του έχουν φυτευτεί δέντρα.", "For decades, Omonia Square was for many Athenians a place they simply crossed in a hurry. Concrete, traffic chaos and few benches. After the latest redevelopment, the picture has changed: a large fountain works again in the centre of the square, and trees have been planted around it."),
  L("Καταστηματάρχισσα", "f", "Έχω το κατάστημά μου εδώ και είκοσι χρόνια. Τα βράδια ο κόσμος κάθεται πια γύρω από το σιντριβάνι, τα παιδιά παίζουν με το νερό τα καλοκαίρια. Πριν, μετά τις οχτώ, η πλατεία άδειαζε. Η κίνηση στο μαγαζί έχει αυξηθεί αισθητά.", "I've had my shop here for twenty years. In the evenings people now sit around the fountain, children play with the water in summer. Before, after eight o'clock, the square emptied. Business in the shop has increased noticeably."),
  L("Ρεπόρτερ", "m", "Δεν συμφωνούν όλοι. Αρχιτέκτονες επικρίνουν το ότι η πλατεία παραμένει κυρίως σκληρή επιφάνεια, που ζεσταίνεται πολύ τους θερινούς μήνες, και ζητούν περισσότερο πράσινο. Άλλοι επισημαίνουν ότι τα κοινωνικά προβλήματα της περιοχής, όπως η φτώχεια και οι άστεγοι, δεν λύνονται με μια ανάπλαση. Ο δήμος απαντά ότι η πλατεία είναι η αρχή και όχι το τέλος της αναβάθμισης του κέντρου.", "Not everyone agrees. Architects criticise the fact that the square remains mainly a hard surface, which heats up a lot in the summer months, and ask for more greenery. Others point out that the area's social problems, such as poverty and homelessness, are not solved with a redevelopment. The municipality replies that the square is the beginning and not the end of the upgrading of the centre."),
 ],
 "questions": [
  Q("Τι υπάρχει σήμερα στο κέντρο της πλατείας;", ["Ένα πάρκινγκ", "Ένα μεγάλο σιντριβάνι", "Ένα άγαλμα", "Μια παιδική χαρά"], 1, "στο κέντρο της πλατείας λειτουργεί ξανά ένα μεγάλο σιντριβάνι"),
  Q("Τι έχει αλλάξει για την καταστηματάρχισσα;", ["Πλήρωσε περισσότερο ενοίκιο", "Η κίνηση στο μαγαζί της έχει αυξηθεί", "Έκλεισε το μαγαζί της", "Αλλάζει ωράριο"], 1, "Η κίνηση στο μαγαζί έχει αυξηθεί αισθητά"),
  Q("Τι επικρίνουν οι αρχιτέκτονες;", ["Ότι το σιντριβάνι είναι πολύ μικρό", "Ότι η πλατεία παραμένει κυρίως σκληρή επιφάνεια με λίγο πράσινο", "Ότι κόστισε πολύ", "Ότι έγιναν πολλά παγκάκια"], 1, "η πλατεία παραμένει κυρίως σκληρή επιφάνεια… και ζητούν περισσότερο πράσινο"),
 ],
 "gloss": {"ανάπλαση": "ανάπλαση — (urban) redevelopment", "διέσχιζαν": "διασχίζω — to cross", "κυκλοφοριακό": "κυκλοφοριακός — traffic (adj.)", "παγκάκια": "παγκάκι — bench", "σιντριβάνι": "σιντριβάνι — fountain", "έχουν φυτευτεί": "φυτεύομαι — to be planted", "επικρίνουν": "επικρίνω — to criticise", "άστεγοι": "άστεγος — homeless person", "αναβάθμισης": "αναβάθμιση — upgrading"},
})

ITEMS.append({
 "id": "l40-int-taxitzou", "title": "Οδηγός ταξί τη νύχτα", "title_en": "A night-shift taxi driver", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια γυναίκα που οδηγεί ταξί τη νύχτα στην Αθήνα.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσο καιρό οδηγείτε ταξί, και γιατί διαλέξατε τη νυχτερινή βάρδια;", "How long have you been driving a taxi, and why did you choose the night shift?"),
  L("Οδηγός", "f", "Οδηγώ εδώ και έντεκα χρόνια. Πριν δούλευα σε λογιστικό γραφείο, αλλά έκλεισε στην κρίση. Το ταξί ήταν του άντρα μου· εκείνος δουλεύει τη μέρα κι εγώ τη νύχτα. Τη νύχτα η κίνηση είναι λιγότερη και οι διαδρομές πιο ενδιαφέρουσες.", "I've been driving for eleven years. Before that I worked in an accounting office, but it closed during the crisis. The taxi was my husband's; he works days and I work nights. At night there's less traffic and the trips are more interesting."),
  L("Δημοσιογράφος", "m", "Δεν φοβάστε;", "Aren't you afraid?"),
  L("Οδηγός", "f", "Στην αρχή φοβόμουν. Τώρα ξέρω να διαβάζω τους ανθρώπους από το πώς σηκώνουν το χέρι στον δρόμο. Έχω πάντα ανοιχτή την εφαρμογή με τον εντοπισμό, και οι συνάδελφοι ξέρουν πού βρίσκομαι. Σε έντεκα χρόνια μόνο δύο φορές ένιωσα πραγματικά άβολα.", "At first I was afraid. Now I know how to read people from the way they raise their hand in the street. I always have the tracking app on, and my colleagues know where I am. In eleven years I've only felt really uncomfortable twice."),
  L("Δημοσιογράφος", "m", "Ποια διαδρομή δεν θα ξεχάσετε ποτέ;", "Which trip will you never forget?"),
  L("Οδηγός", "f", "Ένα βράδυ του Αυγούστου πήρα μια γυναίκα που ήταν έτοιμη να γεννήσει. Ο άντρας της ήταν στο πλοίο και δεν απαντούσε στο τηλέφωνο. Φτάσαμε στο μαιευτήριο σε δώδεκα λεπτά, που για την Αθήνα είναι ρεκόρ. Έναν μήνα αργότερα με βρήκαν και οι δύο στην πιάτσα για να μου γνωρίσουν το μωρό.", "One August night I picked up a woman who was about to give birth. Her husband was on a ship and wasn't answering his phone. We got to the maternity hospital in twelve minutes, which for Athens is a record. A month later the two of them found me at the taxi rank to introduce me to the baby."),
 ],
 "questions": [
  Q("Τι έκανε η οδηγός πριν οδηγήσει ταξί;", ["Ήταν νοσηλεύτρια", "Δούλευε σε λογιστικό γραφείο", "Ήταν φοιτήτρια", "Δούλευε σε πλοίο"], 1, "Πριν δούλευα σε λογιστικό γραφείο, αλλά έκλεισε στην κρίση"),
  Q("Πώς αισθάνεται ασφαλής τη νύχτα;", ["Δουλεύει μόνο σε κεντρικούς δρόμους", "Έχει ανοιχτή την εφαρμογή εντοπισμού και οι συνάδελφοι ξέρουν πού βρίσκεται", "Δεν παίρνει ποτέ άντρες πελάτες", "Δουλεύει μαζί με τον άντρα της"], 1, "Έχω πάντα ανοιχτή την εφαρμογή με τον εντοπισμό, και οι συνάδελφοι ξέρουν πού βρίσκομαι"),
  Q("Γιατί δεν θα ξεχάσει τη διαδρομή του Αυγούστου;", ["Επειδή έχασε τον δρόμο", "Επειδή μετέφερε μια γυναίκα που ήταν έτοιμη να γεννήσει", "Επειδή ο πελάτης δεν πλήρωσε", "Επειδή είχε ατύχημα"], 1, "πήρα μια γυναίκα που ήταν έτοιμη να γεννήσει"),
 ],
 "gloss": {"νυχτερινή βάρδια": "νυχτερινή βάρδια — night shift", "λογιστικό γραφείο": "λογιστικό γραφείο — accounting office", "διαδρομές": "διαδρομή — trip, route", "εντοπισμό": "εντοπισμός — tracking, location", "συνάδελφοι": "συνάδελφος — colleague", "άβολα": "άβολα — uncomfortable", "να γεννήσει": "γεννώ — to give birth", "μαιευτήριο": "μαιευτήριο — maternity hospital", "πιάτσα": "πιάτσα — taxi rank"},
})

ITEMS.append({
 "id": "l40-mono-anavoli", "title": "Γιατί αναβάλλουμε;", "title_en": "Why do we procrastinate?", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε απόσπασμα από μια ομιλία ενός ψυχολόγου για την αναβλητικότητα.",
 "script": [
  L("Ψυχολόγος", "m", "Όλοι το έχουμε ζήσει: έχουμε μια σημαντική εργασία να παραδώσουμε, και ξαφνικά μας πιάνει μια ακατανίκητη επιθυμία να τακτοποιήσουμε τα συρτάρια μας. Η αναβλητικότητα θεωρείται συνήθως ζήτημα κακής διαχείρισης του χρόνου ή, χειρότερα, τεμπελιάς. Οι έρευνες των τελευταίων δεκαετιών, ωστόσο, δείχνουν κάτι διαφορετικό.", "We have all experienced it: we have an important piece of work to hand in, and suddenly we are seized by an irresistible urge to tidy our drawers. Procrastination is usually seen as a matter of poor time management or, worse, laziness. Research over the last few decades, however, points to something different."),
  L("Ψυχολόγος", "m", "Στον πυρήνα της, η αναβλητικότητα είναι ένας τρόπος διαχείρισης δυσάρεστων συναισθημάτων. Αναβάλλουμε όχι επειδή δεν ξέρουμε τι πρέπει να κάνουμε, αλλά επειδή η εργασία μάς προκαλεί άγχος, πλήξη ή φόβο αποτυχίας. Η αναβολή μάς προσφέρει μια άμεση ανακούφιση, την οποία όμως πληρώνουμε αργότερα με τόκο, όταν η προθεσμία πλησιάζει και το άγχος πολλαπλασιάζεται.", "At its core, procrastination is a way of managing unpleasant emotions. We put things off not because we don't know what we have to do, but because the task causes us anxiety, boredom or fear of failure. Putting it off gives us immediate relief, which, however, we pay for later with interest, when the deadline approaches and the anxiety multiplies."),
  L("Ψυχολόγος", "m", "Ιδιαίτερα ευάλωτοι είναι οι τελειομανείς. Όταν πιστεύουμε ότι το αποτέλεσμα πρέπει να είναι άψογο, η απλή έναρξη μοιάζει απειλητική, γιατί κάθε πρώτη απόπειρα είναι εξ ορισμού ατελής. Παράδοξο αλλά αληθινό: όσο περισσότερο νοιαζόμαστε για κάτι, τόσο πιο πιθανό είναι να το αναβάλουμε.", "Perfectionists are particularly vulnerable. When we believe that the result must be flawless, simply starting seems threatening, because every first attempt is by definition imperfect. Paradoxical but true: the more we care about something, the more likely we are to put it off."),
  L("Ψυχολόγος", "m", "Τι μπορούμε λοιπόν να κάνουμε; Η αυστηρότητα απέναντι στον εαυτό μας, όσο κι αν φαίνεται λογική, συνήθως επιδεινώνει το πρόβλημα. Μελέτες με φοιτητές έδειξαν ότι όσοι συγχώρεσαν τον εαυτό τους για την αναβλητικότητα πριν από μια εξεταστική ανέβαλαν λιγότερο στην επόμενη. Βοηθά επίσης να μειώσουμε το κατώφλι: να δεσμευτούμε όχι να γράψουμε όλη την εργασία, αλλά απλώς να δουλέψουμε δέκα λεπτά. Τις περισσότερες φορές, το δύσκολο είναι η αρχή.", "So what can we do? Being harsh with ourselves, however logical it may seem, usually makes the problem worse. Studies with students showed that those who forgave themselves for procrastinating before one exam period procrastinated less in the next. It also helps to lower the threshold: to commit not to writing the whole paper, but simply to working for ten minutes. Most of the time, the hard part is starting."),
 ],
 "questions": [
  Q("Πώς θεωρείται συνήθως η αναβλητικότητα, σύμφωνα με τον ψυχολόγο;", ["Ως ασθένεια", "Ως κακή διαχείριση του χρόνου ή τεμπελιά", "Ως ένδειξη ευφυΐας", "Ως πρόβλημα μόνο των φοιτητών"], 1, "Η αναβλητικότητα θεωρείται συνήθως ζήτημα κακής διαχείρισης του χρόνου ή, χειρότερα, τεμπελιάς"),
  Q("Τι είναι στην ουσία της η αναβλητικότητα, σύμφωνα με τις έρευνες;", ["Έλλειψη γνώσεων", "Ένας τρόπος διαχείρισης δυσάρεστων συναισθημάτων", "Αποτέλεσμα κούρασης", "Συνήθεια που κληρονομείται"], 1, "η αναβλητικότητα είναι ένας τρόπος διαχείρισης δυσάρεστων συναισθημάτων"),
  Q("Γιατί οι τελειομανείς αναβάλλουν συχνά;", ["Επειδή βαριούνται εύκολα", "Επειδή κάθε πρώτη απόπειρα είναι ατελής και η έναρξη μοιάζει απειλητική", "Επειδή έχουν πολλές υποχρεώσεις", "Επειδή δεν νοιάζονται για το αποτέλεσμα"], 1, "η απλή έναρξη μοιάζει απειλητική, γιατί κάθε πρώτη απόπειρα είναι εξ ορισμού ατελής"),
  Q("Τι έδειξαν οι μελέτες με φοιτητές;", ["Ότι η αυστηρότητα μειώνει την αναβολή", "Ότι όσοι συγχώρεσαν τον εαυτό τους ανέβαλαν λιγότερο στη συνέχεια", "Ότι οι φοιτητές αναβάλλουν περισσότερο από τους εργαζόμενους", "Ότι η αναβολή βελτιώνει τους βαθμούς"], 1, "όσοι συγχώρεσαν τον εαυτό τους… ανέβαλαν λιγότερο στην επόμενη"),
 ],
 "gloss": {"αναβλητικότητα": "αναβλητικότητα — procrastination", "ακατανίκητη": "ακατανίκητος — irresistible", "να τακτοποιήσουμε": "τακτοποιώ — to tidy", "τεμπελιάς": "τεμπελιά — laziness", "πυρήνα": "πυρήνας — core", "πλήξη": "πλήξη — boredom", "ανακούφιση": "ανακούφιση — relief", "με τόκο": "με τόκο — with interest", "προθεσμία": "προθεσμία — deadline", "ευάλωτοι": "ευάλωτος — vulnerable", "τελειομανείς": "τελειομανής — perfectionist", "άψογο": "άψογος — flawless", "απόπειρα": "απόπειρα — attempt", "επιδεινώνει": "επιδεινώνω — to worsen", "κατώφλι": "κατώφλι — threshold"},
})

ITEMS.append({
 "id": "l40-int-ispaniki-gripi", "title": "Η πανδημία του 1918", "title_en": "The 1918 pandemic", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια ιστορικό της ιατρικής για την πανδημία γρίπης του 1918.",
 "script": [
  L("Δημοσιογράφος", "m", "Γιατί μια πανδημία που ξεκίνησε, κατά πάσα πιθανότητα, μακριά από την Ιβηρική έμεινε στην ιστορία ως «ισπανική γρίπη»;", "Why did a pandemic that, in all likelihood, began far from the Iberian peninsula go down in history as the \"Spanish flu\"?"),
  L("Ιστορικός", "f", "Λόγω της λογοκρισίας. Το 1918 ο Πρώτος Παγκόσμιος Πόλεμος βρισκόταν στο τέλος του, και οι εμπόλεμες χώρες απέφευγαν να δημοσιεύουν ειδήσεις που θα μπορούσαν να πλήξουν το ηθικό του πληθυσμού. Η Ισπανία, ουδέτερη χώρα, είχε ελεύθερο Τύπο, που έγραφε ανοιχτά για την επιδημία. Έτσι δημιουργήθηκε η εντύπωση ότι η Ισπανία είχε πληγεί περισσότερο από όλες.", "Because of censorship. In 1918 the First World War was coming to an end, and the countries at war avoided publishing news that could damage the population's morale. Spain, a neutral country, had a free press, which wrote openly about the epidemic. That's how the impression arose that Spain had been hit harder than anyone else."),
  L("Δημοσιογράφος", "m", "Τι την έκανε τόσο θανατηφόρα;", "What made it so deadly?"),
  L("Ιστορικός", "f", "Ένα από τα πιο ανησυχητικά χαρακτηριστικά της ήταν ότι δεν έπληττε μόνο τους ηλικιωμένους και τα βρέφη, όπως συνήθως η εποχική γρίπη, αλλά και νέους, υγιείς ενήλικες. Το δεύτερο κύμα, το φθινόπωρο του 1918, ήταν το πιο φονικό. Οι συνθήκες του πολέμου, με τα συνωστισμένα στρατόπεδα και τις μαζικές μετακινήσεις στρατευμάτων, ευνόησαν την εξάπλωση. Και φυσικά δεν υπήρχαν ούτε εμβόλια ούτε αντιβιοτικά για τις δευτερογενείς πνευμονίες.", "One of its most worrying features was that it struck not only the elderly and infants, as seasonal flu usually does, but also young, healthy adults. The second wave, in autumn 1918, was the deadliest. Wartime conditions, with crowded camps and mass troop movements, favoured its spread. And of course there were neither vaccines nor antibiotics for the secondary pneumonias."),
  L("Δημοσιογράφος", "m", "Τι έμαθαν, κατά τη γνώμη σας, οι κοινωνίες από εκείνη την εμπειρία;", "What, in your opinion, did societies learn from that experience?"),
  L("Ιστορικός", "f", "Λιγότερα απ' όσα θα περίμενε κανείς. Η πανδημία, παρότι στοίχισε τη ζωή σε δεκάδες εκατομμύρια ανθρώπους, ξεχάστηκε γρήγορα, σκιασμένη από τη μνήμη του πολέμου. Ωστόσο, ορισμένα μέτρα που δοκιμάστηκαν τότε, όπως το κλείσιμο σχολείων και θεάτρων ή η χρήση μάσκας, επανήλθαν έναν αιώνα αργότερα. Οι μελέτες για τις αμερικανικές πόλεις του 1918 δείχνουν ότι όσες εφάρμοσαν τέτοια μέτρα νωρίς και για μεγαλύτερο διάστημα είχαν χαμηλότερη θνησιμότητα. Το δίδαγμα είναι διαχρονικό: στις επιδημίες, ο χρόνος της αντίδρασης μετράει όσο και η ίδια η αντίδραση.", "Less than one might expect. The pandemic, although it cost the lives of tens of millions of people, was quickly forgotten, overshadowed by the memory of the war. However, some measures tried at the time, such as closing schools and theatres or wearing masks, came back a century later. Studies of American cities in 1918 show that those which applied such measures early and for longer had lower mortality. The lesson is timeless: in epidemics, the timing of the response matters as much as the response itself."),
 ],
 "questions": [
  Q("Γιατί η πανδημία ονομάστηκε «ισπανική»;", ["Επειδή ξεκίνησε στην Ισπανία", "Επειδή ο ελεύθερος ισπανικός Τύπος έγραφε ανοιχτά γι' αυτήν", "Επειδή την ανακάλυψε ένας Ισπανός γιατρός", "Επειδή η Ισπανία είχε τους περισσότερους νεκρούς"], 1, "Η Ισπανία, ουδέτερη χώρα, είχε ελεύθερο Τύπο, που έγραφε ανοιχτά για την επιδημία"),
  Q("Ποιο χαρακτηριστικό της ήταν ιδιαίτερα ανησυχητικό;", ["Ότι προσέβαλλε μόνο παιδιά", "Ότι έπληττε και νέους, υγιείς ενήλικες", "Ότι μεταδιδόταν μόνο μέσω νερού", "Ότι κράτησε μόνο λίγες εβδομάδες"], 1, "δεν έπληττε μόνο τους ηλικιωμένους και τα βρέφη… αλλά και νέους, υγιείς ενήλικες"),
  Q("Ποιοι παράγοντες ευνόησαν την εξάπλωση;", ["Η ζέστη του καλοκαιριού", "Τα συνωστισμένα στρατόπεδα και οι μαζικές μετακινήσεις στρατευμάτων", "Τα ταξίδια με αεροπλάνο", "Η έλλειψη νοσοκομείων στις πόλεις"], 1, "με τα συνωστισμένα στρατόπεδα και τις μαζικές μετακινήσεις στρατευμάτων"),
  Q("Ποιο είναι το δίδαγμα, σύμφωνα με την ιστορικό;", ["Ότι οι μάσκες δεν βοηθούν", "Ότι ο χρόνος της αντίδρασης μετράει όσο και η ίδια η αντίδραση", "Ότι οι πανδημίες δεν επαναλαμβάνονται", "Ότι μόνο τα εμβόλια σώζουν ζωές"], 1, "ο χρόνος της αντίδρασης μετράει όσο και η ίδια η αντίδραση"),
 ],
 "gloss": {"κατά πάσα πιθανότητα": "κατά πάσα πιθανότητα — in all likelihood", "λογοκρισίας": "λογοκρισία — censorship", "εμπόλεμες": "εμπόλεμος — at war, belligerent", "να πλήξουν": "πλήττω — to hit, damage", "ηθικό": "ηθικό — morale", "ουδέτερη": "ουδέτερος — neutral", "θανατηφόρα": "θανατηφόρος — deadly", "βρέφη": "βρέφος — infant", "εποχική": "εποχικός — seasonal", "συνωστισμένα": "συνωστισμένος — crowded", "εξάπλωση": "εξάπλωση — spread", "δευτερογενείς": "δευτερογενής — secondary", "σκιασμένη": "σκιασμένος — overshadowed", "δίδαγμα": "δίδαγμα — lesson", "διαχρονικό": "διαχρονικός — timeless"},
})

rnd = random.Random(40)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-40.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
