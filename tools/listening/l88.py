# Source for library/listening/listening-88.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l88.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l88-ann-seirines", "title": "Δοκιμή σειρήνων στην πόλη", "title_en": "A siren test in the city", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε στο τοπικό ραδιόφωνο μια ανακοίνωση του δήμου.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο Δήμος ενημερώνει τους πολίτες ότι την Πέμπτη, στις δώδεκα το μεσημέρι ακριβώς, θα γίνει δοκιμή του νέου συστήματος σειρήνων προειδοποίησης. Θα ακουστούν σε όλη την πόλη, για περίπου ενενήντα δευτερόλεπτα. Πρόκειται μόνο για δοκιμή: δεν υπάρχει κανένας κίνδυνος.", "The Municipality informs citizens that on Thursday, at exactly twelve noon, the new warning-siren system will be tested. The sirens will be heard across the whole city for about ninety seconds. This is only a test: there is no danger whatsoever."),
  L("Εκφωνήτρια", "f", "Κατά τη διάρκεια της δοκιμής δεν χρειάζεται να κάνετε τίποτα. Μην καλείτε το 112 και την αστυνομία για να ρωτήσετε τι συμβαίνει, ώστε οι γραμμές να μείνουν ελεύθερες για πραγματικά επείγοντα περιστατικά. Παρακαλούμε ενημερώστε τους ηλικιωμένους γείτονες και όσους δεν μιλούν καλά ελληνικά, για να μην ανησυχήσουν.", "During the test you don't need to do anything. Please don't call 112 or the police to ask what is happening, so that the lines stay free for real emergencies. Please let elderly neighbours and anyone who doesn't speak Greek well know, so they won't worry."),
  L("Εκφωνήτρια", "f", "Σε περίπτωση πραγματικού κινδύνου, οι σειρήνες θα ακούγονται με διακοπές, και ταυτόχρονα θα σταλεί μήνυμα στα κινητά τηλέφωνα. Τότε θα πρέπει να ακολουθήσετε τις οδηγίες του μηνύματος. Περισσότερες πληροφορίες θα βρείτε στην ιστοσελίδα του δήμου.", "In case of real danger, the sirens will sound intermittently, and at the same time a message will be sent to mobile phones. Then you should follow the instructions in the message. You'll find more information on the municipality's website."),
 ],
 "questions": [
  Q("Πόσο θα διαρκέσει η δοκιμή;", ["Περίπου δέκα λεπτά", "Περίπου ενενήντα δευτερόλεπτα", "Μία ώρα", "Όλη τη μέρα"], 1, "για περίπου ενενήντα δευτερόλεπτα"),
  Q("Γιατί ζητείται να μην τηλεφωνούν οι πολίτες στο 112;", ["Γιατί το 112 δεν λειτουργεί την Πέμπτη", "Για να μείνουν οι γραμμές ελεύθερες για πραγματικά επείγοντα", "Γιατί η κλήση κοστίζει ακριβά", "Γιατί η αστυνομία δεν ξέρει τίποτα"], 1, "ώστε οι γραμμές να μείνουν ελεύθερες για πραγματικά επείγοντα περιστατικά"),
  Q("Πώς θα καταλάβει κανείς ότι ο κίνδυνος είναι πραγματικός;", ["Οι σειρήνες θα ακούγονται με διακοπές και θα έρθει μήνυμα στο κινητό", "Θα χτυπήσουν οι καμπάνες", "Θα ανακοινωθεί μόνο στο ραδιόφωνο", "Οι σειρήνες θα ακούγονται χωρίς σταματημό"], 0, "οι σειρήνες θα ακούγονται με διακοπές, και ταυτόχρονα θα σταλεί μήνυμα στα κινητά τηλέφωνα"),
 ],
 "gloss": {"δήμου": "δήμος — municipality", "δοκιμή": "δοκιμή — test", "σειρήνων": "σειρήνα — siren", "προειδοποίησης": "προειδοποίηση — warning", "κίνδυνος": "κίνδυνος — danger", "επείγοντα περιστατικά": "επείγον περιστατικό — emergency", "ηλικιωμένους": "ηλικιωμένος — elderly", "ανησυχήσουν": "ανησυχώ — to worry", "με διακοπές": "με διακοπές — intermittently", "ταυτόχρονα": "ταυτόχρονα — at the same time"},
})
ITEMS.append({
 "id": "l88-vm-aerodromio", "title": "Πάρε με από το αεροδρόμιο!", "title_en": "Pick me up from the airport!", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στο κινητό σας από μια φίλη που επιστρέφει από ταξίδι.",
 "script": [
  L("Φίλη", "f", "Γεια σου, η Κατερίνα είμαι. Έχω ένα μικρό πρόβλημα και, αν μπορείς, θέλω τη βοήθειά σου. Το αεροπλάνο μας δεν μπόρεσε να προσγειωθεί στη Θεσσαλονίκη λόγω της πυκνής ομίχλης, και μας έστειλαν στην Καβάλα. Μόλις βγήκαμε από το αεροπλάνο.", "Hi, it's Katerina. I've got a small problem and, if you can, I'd like your help. Our plane couldn't land in Thessaloniki because of the thick fog, and they sent us to Kavala. We've just got off the plane."),
  L("Φίλη", "f", "Η εταιρεία λέει ότι θα μας πάει με λεωφορείο στη Θεσσαλονίκη, αλλά δεν ξέρουν ακόμη πότε, ίσως σε δύο ή τρεις ώρες. Υπολογίζω να φτάσουμε στο αεροδρόμιο της Θεσσαλονίκης γύρω στις δύο τα ξημερώματα. Τέτοια ώρα δεν υπάρχει λεωφορείο για την πόλη, και το ταξί κοστίζει μια περιουσία.", "The airline says they'll take us to Thessaloniki by coach, but they don't know when yet, maybe in two or three hours. I reckon we'll get to Thessaloniki airport around two in the morning. At that hour there's no bus into town, and a taxi costs a fortune."),
  L("Φίλη", "f", "Θα μπορούσες να έρθεις να με πάρεις; Ξέρω ότι είναι αργά και ότι αύριο δουλεύεις, οπότε, αν δεν μπορείς, μην ανησυχείς καθόλου, θα βρω μια λύση. Θα σου στείλω γραπτό μήνυμα μόλις μάθω την ακριβή ώρα. Σ' ευχαριστώ πολύ!", "Could you come and pick me up? I know it's late and that you're working tomorrow, so if you can't, don't worry at all, I'll find a solution. I'll text you as soon as I know the exact time. Thanks so much!"),
 ],
 "questions": [
  Q("Γιατί το αεροπλάνο πήγε στην Καβάλα;", ["Λόγω απεργίας", "Λόγω τεχνικού προβλήματος", "Λόγω πυκνής ομίχλης στη Θεσσαλονίκη", "Λόγω δυνατού ανέμου"], 2, "δεν μπόρεσε να προσγειωθεί στη Θεσσαλονίκη λόγω της πυκνής ομίχλης"),
  Q("Πώς θα πάνε οι επιβάτες στη Θεσσαλονίκη;", ["Με τρένο", "Με λεωφορείο της εταιρείας", "Με άλλο αεροπλάνο", "Με ταξί"], 1, "θα μας πάει με λεωφορείο στη Θεσσαλονίκη"),
  Q("Τι θα κάνει η Κατερίνα όταν μάθει την ακριβή ώρα;", ["Θα πάρει ταξί", "Θα στείλει γραπτό μήνυμα", "Θα κλείσει δωμάτιο σε ξενοδοχείο", "Θα τηλεφωνήσει στους γονείς της"], 1, "Θα σου στείλω γραπτό μήνυμα μόλις μάθω την ακριβή ώρα"),
 ],
 "gloss": {"προσγειωθεί": "προσγειώνομαι — to land", "πυκνής": "πυκνός — thick, dense", "ομίχλης": "ομίχλη — fog", "Υπολογίζω": "υπολογίζω — to reckon, estimate", "ξημερώματα": "τα ξημερώματα — the small hours", "περιουσία": "περιουσία — fortune, property", "να με πάρεις": "παίρνω κάποιον — to pick someone up", "λύση": "λύση — solution", "γραπτό μήνυμα": "γραπτό μήνυμα — text message", "ακριβή": "ακριβής — exact"},
})
ITEMS.append({
 "id": "l88-dia-psygeio", "title": "Ένα μεταχειρισμένο ψυγείο", "title_en": "A second-hand fridge", "type": "dialogue", "level": "B2",
 "context_el": "Ένας νεαρός πηγαίνει να δει ένα μεταχειρισμένο ψυγείο που πουλάει μια κυρία μέσω μιας αγγελίας στο διαδίκτυο.",
 "script": [
  L("Αγοραστής", "m", "Καλησπέρα, εγώ σας πήρα τηλέφωνο για το ψυγείο της αγγελίας.", "Good evening, I'm the one who called you about the fridge in the ad."),
  L("Πωλήτρια", "f", "Α, καλώς ήρθατε. Ορίστε, είναι αυτό εδώ. Είναι τεσσάρων χρόνων και λειτουργεί άψογα. Το πουλάμε μόνο επειδή αλλάξαμε κουζίνα και δεν χωράει στη νέα θέση.", "Ah, welcome. Here it is, this one. It's four years old and works perfectly. We're only selling it because we redid the kitchen and it doesn't fit in the new space."),
  L("Αγοραστής", "m", "Φαίνεται σε πολύ καλή κατάσταση. Ενεργειακή κλάση ποια είναι; Θέλω κάτι που να μην καίει πολύ ρεύμα.", "It looks in very good condition. What's its energy class? I want something that doesn't use much electricity."),
  L("Πωλήτρια", "f", "Είναι Α, το γράφει και το αυτοκόλλητο εδώ στο πλάι. Έχω ακόμη και το βιβλιαράκι οδηγιών. Η μόνη ατέλεια είναι μια μικρή γρατζουνιά στην πόρτα, εδώ κάτω, βλέπετε;", "It's A; the sticker here on the side says so too. I've even still got the instruction booklet. The only flaw is a small scratch on the door, down here, see?"),
  L("Αγοραστής", "m", "Ναι, δεν με πειράζει. Στην αγγελία γράφατε διακόσια ευρώ. Θα το δίνατε στα εκατόν εβδομήντα; Θα πρέπει να πληρώσω και κάποιον να το μεταφέρει, γιατί μένω στον τέταρτο χωρίς ασανσέρ.", "Yes, I don't mind. In the ad you said two hundred euros. Would you let it go for a hundred and seventy? I'll also have to pay someone to move it, because I live on the fourth floor with no lift."),
  L("Πωλήτρια", "f", "Ας πούμε εκατόν ογδόντα, και σας δίνω δώρο και τα ράφια του καταψύκτη που είχα αγοράσει επιπλέον. Α, και μια συμβουλή: όταν το βάλετε στη θέση του, περιμένετε τρεις με τέσσερις ώρες πριν το ανάψετε.", "Let's say a hundred and eighty, and I'll throw in the extra freezer shelves I'd bought. Oh, and a tip: once you've put it in place, wait three to four hours before you switch it on."),
 ],
 "questions": [
  Q("Γιατί πουλάει η κυρία το ψυγείο;", ["Γιατί χάλασε", "Γιατί δεν χωράει στη νέα κουζίνα", "Γιατί μετακομίζει στο εξωτερικό", "Γιατί καίει πολύ ρεύμα"], 1, "αλλάξαμε κουζίνα και δεν χωράει στη νέα θέση"),
  Q("Ποια ατέλεια έχει το ψυγείο;", ["Δεν κλείνει καλά η πόρτα", "Κάνει θόρυβο", "Μια μικρή γρατζουνιά στην πόρτα", "Λείπει ένα ράφι"], 2, "μια μικρή γρατζουνιά στην πόρτα"),
  Q("Σε ποια τιμή καταλήγει η πωλήτρια;", ["Διακόσια ευρώ", "Εκατόν εβδομήντα ευρώ", "Εκατόν ογδόντα ευρώ", "Εκατόν πενήντα ευρώ"], 2, "Ας πούμε εκατόν ογδόντα"),
 ],
 "gloss": {"μεταχειρισμένο": "μεταχειρισμένος — second-hand", "αγγελίας": "αγγελία — ad, classified", "άψογα": "άψογα — perfectly, flawlessly", "κατάσταση": "κατάσταση — condition", "Ενεργειακή κλάση": "ενεργειακή κλάση — energy class", "αυτοκόλλητο": "αυτοκόλλητο — sticker", "ατέλεια": "ατέλεια — flaw", "γρατζουνιά": "γρατζουνιά — scratch", "μεταφέρει": "μεταφέρω — to move, transport", "καταψύκτη": "καταψύκτης — freezer"},
})
ITEMS.append({
 "id": "l88-int-oreivatissa", "title": "Η ορειβάτισσα", "title_en": "The mountaineer", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, μια δημοσιογράφος μιλά με μια ορειβάτισσα που μόλις επέστρεψε από τα Ιμαλάια.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς ξεκίνησαν όλα; Δεν μεγαλώσατε, νομίζω, κοντά στα βουνά.", "How did it all start? I don't think you grew up near the mountains."),
  L("Ορειβάτισσα", "f", "Όχι, είμαι από τον Πειραιά, παιδί της θάλασσας. Στα είκοσι, μια φίλη με έπεισε να ανέβουμε στον Όλυμπο. Θυμάμαι ότι στο καταφύγιο ήμουν εξαντλημένη, αλλά όταν είδα την ανατολή από την κορυφή, ήξερα ότι θα ξαναγύριζα. Από τότε περνάω σχεδόν κάθε Σαββατοκύριακο στα βουνά.", "No, I'm from Piraeus, a child of the sea. At twenty, a friend persuaded me to climb Olympus. I remember being exhausted at the refuge, but when I saw the sunrise from the summit, I knew I'd go back. Since then I've spent almost every weekend in the mountains."),
  L("Δημοσιογράφος", "f", "Και τώρα επιστρέψατε από μια κορυφή πάνω από οκτώ χιλιάδες μέτρα. Ποιο ήταν το πιο δύσκολο;", "And now you're back from a peak over eight thousand metres. What was the hardest part?"),
  L("Ορειβάτισσα", "f", "Όχι η κούραση, όπως νομίζουν πολλοί, αλλά το υψόμετρο. Εκεί πάνω ο αέρας έχει πολύ λιγότερο οξυγόνο. Πονάει το κεφάλι, δεν έχεις όρεξη, δεν κοιμάσαι. Γι' αυτό ανεβαίνεις σιγά σιγά: ανεβαίνεις σε ένα στρατόπεδο, κατεβαίνεις πάλι, και ξανά, ώσπου το σώμα να συνηθίσει. Αυτό κράτησε σχεδόν έξι εβδομάδες.", "Not the fatigue, as many people think, but the altitude. Up there the air has much less oxygen. Your head aches, you've no appetite, you don't sleep. That's why you go up slowly: you climb to a camp, come back down, and again, until your body gets used to it. That took almost six weeks."),
  L("Δημοσιογράφος", "f", "Φτάσατε τελικά στην κορυφή;", "Did you reach the summit in the end?"),
  L("Ορειβάτισσα", "f", "Όχι. Διακόσια μέτρα πριν από την κορυφή, ο καιρός χάλασε και ο Νεπαλέζος οδηγός μας είπε να γυρίσουμε. Ήταν η σωστή απόφαση. Στο βουνό η κορυφή είναι προαιρετική· η επιστροφή είναι υποχρεωτική.", "No. Two hundred metres before the summit, the weather turned and our Nepali guide told us to turn back. It was the right decision. On the mountain the summit is optional; the return is compulsory."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η ορειβάτισσα να ανεβαίνει σε βουνά;", ["Μεγάλωσε σε ένα ορεινό χωριό", "Μια φίλη την έπεισε να ανέβουν στον Όλυμπο", "Το έκανε ο πατέρας της", "Γράφτηκε σε σύλλογο στο σχολείο"], 1, "μια φίλη με έπεισε να ανέβουμε στον Όλυμπο"),
  Q("Τι ήταν, κατά τη γνώμη της, το πιο δύσκολο;", ["Η κούραση", "Το κρύο", "Το υψόμετρο και η έλλειψη οξυγόνου", "Η μοναξιά"], 2, "Όχι η κούραση, όπως νομίζουν πολλοί, αλλά το υψόμετρο"),
  Q("Γιατί δεν έφτασε στην κορυφή;", ["Τραυματίστηκε", "Ο καιρός χάλασε και ο οδηγός είπε να γυρίσουν", "Της τελείωσε το οξυγόνο", "Έχασε τον δρόμο"], 1, "ο καιρός χάλασε και ο Νεπαλέζος οδηγός μας είπε να γυρίσουμε"),
 ],
 "gloss": {"ορειβάτισσα": "ορειβάτισσα — (female) mountaineer", "με έπεισε": "πείθω — to persuade", "καταφύγιο": "καταφύγιο — (mountain) refuge", "εξαντλημένη": "εξαντλημένος — exhausted", "ανατολή": "ανατολή — sunrise", "κορυφή": "κορυφή — summit, peak", "υψόμετρο": "υψόμετρο — altitude", "οξυγόνο": "οξυγόνο — oxygen", "στρατόπεδο": "στρατόπεδο — camp", "προαιρετική": "προαιρετικός — optional", "υποχρεωτική": "υποχρεωτικός — compulsory"},
})
ITEMS.append({
 "id": "l88-rep-florina", "title": "Η Φλώρινα", "title_en": "Florina", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ταξιδιωτικό ρεπορτάζ στο ραδιόφωνο.",
 "script": [
  L("Ρεπόρτερ", "m", "Βρισκόμαστε στη Φλώρινα, στη βορειοδυτική Μακεδονία, λίγα χιλιόμετρα από τα σύνορα με τη Βόρεια Μακεδονία. Μέσα από την πόλη κυλάει το ποτάμι Σακουλέβας, και στις όχθες του στέκονται παλιά νεοκλασικά σπίτια, πολλά από αυτά ανακαινισμένα. Τον χειμώνα, με την ομίχλη πάνω στο νερό, η πόλη έχει κάτι από σκηνικό ταινίας.", "We're in Florina, in north-western Macedonia, a few kilometres from the border with North Macedonia. The Sakoulevas river runs through the town, and along its banks stand old neoclassical houses, many of them restored. In winter, with the fog over the water, the town has something of a film set about it."),
  L("Ρεπόρτερ", "m", "Και δεν είναι τυχαίο: εδώ γύρισε ο Θόδωρος Αγγελόπουλος μέρος της ταινίας «Το μετέωρο βήμα του πελαργού». Η Φλώρινα έχει επίσης ζωντανή καλλιτεχνική ζωή· η πόλη έχει Μουσείο Σύγχρονης Τέχνης, και στη Σχολή Καλών Τεχνών της σπουδάζουν φοιτητές από όλη την Ελλάδα.", "And it's no accident: this is where Theo Angelopoulos shot part of the film 'The Suspended Step of the Stork'. Florina also has a lively art scene; the town has a Museum of Contemporary Art, and students from all over Greece study at its School of Fine Arts."),
  L("Ρεπόρτερ", "m", "Πριν φύγετε, μην παραλείψετε να δοκιμάσετε τις περίφημες κόκκινες πιπεριές Φλωρίνης, ψητές με λίγο λάδι και σκόρδο. Και αν έχετε μια μέρα παραπάνω, οι λίμνες των Πρεσπών, με τους πελεκάνους και τα βυζαντινά ερημητήρια, απέχουν λιγότερο από μία ώρα με το αυτοκίνητο.", "Before you leave, don't miss the famous red Florina peppers, roasted with a little oil and garlic. And if you've got an extra day, the Prespa lakes, with their pelicans and Byzantine hermitages, are less than an hour away by car."),
 ],
 "questions": [
  Q("Τι βρίσκεται στις όχθες του ποταμού Σακουλέβα;", ["Εργοστάσια", "Παλιά νεοκλασικά σπίτια", "Ένα μεγάλο πάρκο", "Ξενοδοχεία"], 1, "στις όχθες του στέκονται παλιά νεοκλασικά σπίτια"),
  Q("Ποιος γύρισε ταινία στη Φλώρινα;", ["Ο Μιχάλης Κακογιάννης", "Ο Θόδωρος Αγγελόπουλος", "Ο Νίκος Κούνδουρος", "Ο Γιώργος Λάνθιμος"], 1, "εδώ γύρισε ο Θόδωρος Αγγελόπουλος μέρος της ταινίας"),
  Q("Ποιο τοπικό προϊόν προτείνει ο ρεπόρτερ;", ["Το τυρί φέτα", "Τις κόκκινες πιπεριές", "Το κρασί", "Τα κάστανα"], 1, "τις περίφημες κόκκινες πιπεριές Φλωρίνης"),
 ],
 "gloss": {"σύνορα": "σύνορα — border", "κυλάει": "κυλάω — to flow, roll", "όχθες": "όχθη — (river) bank", "νεοκλασικά": "νεοκλασικός — neoclassical", "ανακαινισμένα": "ανακαινισμένος — renovated, restored", "σκηνικό": "σκηνικό — set, scenery", "μετέωρο": "μετέωρος — suspended, in mid-air", "πελαργού": "πελαργός — stork", "μην παραλείψετε": "παραλείπω — to leave out, miss", "πελεκάνους": "πελεκάνος — pelican", "ερημητήρια": "ερημητήριο — hermitage"},
})
ITEMS.append({
 "id": "l88-rep-folegandros", "title": "Η Φολέγανδρος", "title_en": "Folegandros", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα μικρό νησί των Κυκλάδων.",
 "script": [
  L("Ρεπόρτερ", "f", "Η Φολέγανδρος είναι ένα μικρό, βραχώδες νησί των Κυκλάδων, ανάμεσα στη Μήλο και τη Σίκινο. Το πιο εντυπωσιακό της σημείο είναι η Χώρα, χτισμένη στην άκρη ενός γκρεμού, περίπου διακόσια μέτρα πάνω από τη θάλασσα. Τα σοκάκια της είναι τόσο στενά, που τα αυτοκίνητα δεν μπαίνουν καθόλου.", "Folegandros is a small, rocky island in the Cyclades, between Milos and Sikinos. Its most striking spot is the Chora, built on the edge of a cliff about two hundred metres above the sea. Its alleys are so narrow that cars can't get in at all."),
  L("Ρεπόρτερ", "f", "Η απομόνωση του νησιού έχει και σκοτεινή πλευρά. Τον εικοστό αιώνα, η Φολέγανδρος ήταν τόπος εξορίας: εδώ έστελναν πολιτικούς κρατούμενους, που ζούσαν μαζί με τους ντόπιους, συχνά σε μεγάλη φτώχεια. Οι παλαιότεροι κάτοικοι θυμούνται ακόμη ονόματα και ιστορίες.", "The island's isolation also has a dark side. In the twentieth century, Folegandros was a place of exile: political prisoners were sent here, living alongside the locals, often in great poverty. Older residents still remember names and stories."),
  L("Ρεπόρτερ", "f", "Σήμερα το νησί προσελκύει όσους αναζητούν ησυχία και περπάτημα. Ένα παλιό μονοπάτι ανεβαίνει από τη Χώρα στην εκκλησία της Παναγίας, απ' όπου η θέα στο ηλιοβασίλεμα κόβει την ανάσα. Και στις ταβέρνες, ζητήστε τα «μάτσατα», χειροποίητα ζυμαρικά που σερβίρονται συνήθως με κόκορα ή κουνέλι.", "Today the island attracts people looking for peace and walking. An old path climbs from the Chora to the church of the Virgin, from where the view at sunset takes your breath away. And in the tavernas, ask for 'matsata', hand-made pasta usually served with rooster or rabbit."),
 ],
 "questions": [
  Q("Πού είναι χτισμένη η Χώρα της Φολεγάνδρου;", ["Δίπλα στο λιμάνι", "Στην άκρη ενός γκρεμού", "Σε μια κοιλάδα", "Σε ένα νησάκι απέναντι"], 1, "χτισμένη στην άκρη ενός γκρεμού"),
  Q("Τι ήταν η Φολέγανδρος τον εικοστό αιώνα;", ["Βάση του ναυτικού", "Τόπος εξορίας", "Κέντρο εμπορίου", "Τόπος διακοπών βασιλιάδων"], 1, "η Φολέγανδρος ήταν τόπος εξορίας"),
  Q("Τι είναι τα «μάτσατα»;", ["Ένα τοπικό γλυκό", "Χειροποίητα ζυμαρικά", "Ένα είδος τυριού", "Ένας παραδοσιακός χορός"], 1, "χειροποίητα ζυμαρικά που σερβίρονται συνήθως με κόκορα ή κουνέλι"),
 ],
 "gloss": {"βραχώδες": "βραχώδης — rocky", "εντυπωσιακό": "εντυπωσιακός — impressive, striking", "γκρεμού": "γκρεμός — cliff", "σοκάκια": "σοκάκι — alley, lane", "απομόνωση": "απομόνωση — isolation", "εξορίας": "εξορία — exile", "κρατούμενους": "κρατούμενος — prisoner, detainee", "ντόπιους": "ντόπιος — local", "μονοπάτι": "μονοπάτι — path", "κόβει την ανάσα": "κόβει την ανάσα — takes your breath away", "ζυμαρικά": "ζυμαρικά — pasta"},
})
ITEMS.append({
 "id": "l88-mono-choris-diktya", "title": "Τρεις μήνες χωρίς κοινωνικά δίκτυα", "title_en": "Three months without social media", "type": "monologue", "level": "B2",
 "context_el": "Ένας φοιτητής μιλά σε ένα podcast για ένα πείραμα που έκανε με τον εαυτό του.",
 "script": [
  L("Φοιτητής", "m", "Πέρσι τον Ιανουάριο κοίταξα τα στατιστικά του κινητού μου και πάγωσα: πέντε ώρες τη μέρα, κυρίως σε κοινωνικά δίκτυα. Πέντε ώρες! Αποφάσισα να σβήσω όλες τις εφαρμογές για τρεις μήνες. Κράτησα μόνο τα μηνύματα και τις κλήσεις.", "Last January I looked at my phone's statistics and froze: five hours a day, mostly on social media. Five hours! I decided to delete all the apps for three months. I kept only messages and calls."),
  L("Φοιτητής", "m", "Οι πρώτες δέκα μέρες ήταν πραγματικά δύσκολες. Έπιανα το κινητό χωρίς να το καταλαβαίνω, άνοιγα την οθόνη και δεν είχα τι να κάνω. Ένιωθα ότι έχανα όλα όσα συνέβαιναν. Κάποιοι φίλοι μάλιστα παρεξηγήθηκαν, γιατί δεν έβλεπα τις αναρτήσεις τους και δεν τις σχολίαζα.", "The first ten days were really hard. I'd pick up my phone without realising, unlock the screen and have nothing to do. I felt I was missing everything that was going on. Some friends even took offence, because I wasn't seeing their posts or commenting on them."),
  L("Φοιτητής", "m", "Μετά όμως κάτι άλλαξε. Διάβασα έξι βιβλία, κοιμόμουν καλύτερα και άρχισα να τηλεφωνώ στους φίλους μου αντί να τους στέλνω καρδούλες. Όταν τελείωσαν οι τρεις μήνες, ξανάβαλα μόνο μία εφαρμογή, και μόνο στον υπολογιστή. Δεν λέω ότι τα κοινωνικά δίκτυα είναι κακά. Απλώς τώρα αποφασίζω εγώ πότε θα τα χρησιμοποιήσω.", "But then something changed. I read six books, I slept better and I started phoning my friends instead of sending them little hearts. When the three months were up, I reinstalled just one app, and only on the computer. I'm not saying social media is bad. It's just that now I decide when I'll use it."),
 ],
 "questions": [
  Q("Τι τον έκανε να αποφασίσει το πείραμα;", ["Μια συμβουλή του γιατρού του", "Τα στατιστικά του κινητού του", "Ένα άρθρο σε εφημερίδα", "Ένα στοίχημα με φίλους"], 1, "κοίταξα τα στατιστικά του κινητού μου και πάγωσα"),
  Q("Γιατί παρεξηγήθηκαν κάποιοι φίλοι του;", ["Γιατί δεν απαντούσε στο τηλέφωνο", "Γιατί δεν έβλεπε ούτε σχολίαζε τις αναρτήσεις τους", "Γιατί δεν πήγε στα γενέθλιά τους", "Γιατί τους κατηγόρησε"], 1, "δεν έβλεπα τις αναρτήσεις τους και δεν τις σχολίαζα"),
  Q("Τι έκανε όταν τελείωσαν οι τρεις μήνες;", ["Ξανάβαλε όλες τις εφαρμογές", "Δεν ξανάβαλε καμία εφαρμογή", "Ξανάβαλε μία εφαρμογή, μόνο στον υπολογιστή", "Πούλησε το κινητό του"], 2, "ξανάβαλα μόνο μία εφαρμογή, και μόνο στον υπολογιστή"),
 ],
 "gloss": {"πείραμα": "πείραμα — experiment", "στατιστικά": "στατιστικά — statistics", "πάγωσα": "παγώνω — to freeze", "σβήσω": "σβήνω — to delete", "εφαρμογές": "εφαρμογή — app", "παρεξηγήθηκαν": "παρεξηγούμαι — to take offence", "αναρτήσεις": "ανάρτηση — post", "σχολίαζα": "σχολιάζω — to comment on", "καρδούλες": "καρδούλα — little heart (emoji)", "ξανάβαλα": "ξαναβάζω — to put back, reinstall"},
})
ITEMS.append({
 "id": "l88-mono-michanaki", "title": "Μηχανάκι στα πενήντα", "title_en": "A motorbike at fifty", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα διηγείται σε μια παρέα πώς έμαθε να οδηγεί μηχανάκι.",
 "script": [
  L("Γυναίκα", "f", "Όλη μου τη ζωή φοβόμουν τα μηχανάκια. Ο πατέρας μου είχε πάθει ένα σοβαρό ατύχημα όταν ήμουν μικρή, και στο σπίτι μας η λέξη «μηχανή» ήταν σχεδόν απαγορευμένη. Όταν όμως η κόρη μου έφυγε για σπουδές και μετακόμισα σε ένα προάστιο χωρίς καλή συγκοινωνία, κατάλαβα ότι χρειαζόμουν μια λύση.", "All my life I was afraid of motorbikes. My father had had a serious accident when I was little, and in our house the word 'motorbike' was almost forbidden. But when my daughter went off to university and I moved to a suburb with poor public transport, I realised I needed a solution."),
  L("Γυναίκα", "f", "Στη σχολή οδηγών ήμουν η μεγαλύτερη μαθήτρια, με διαφορά τριάντα χρόνων από τους υπόλοιπους. Την πρώτη μέρα έπεσα στο προαύλιο, πριν καν βάλω δεύτερη ταχύτητα. Ο εκπαιδευτής, ένας υπομονετικός κύριος, με βοήθησε να σηκωθώ και μου είπε: «Όλοι πέφτουν μία φορά. Το θέμα είναι να ξανανέβεις αμέσως».", "At the driving school I was the oldest student, thirty years older than the rest. On the first day I fell over in the yard, before I'd even put it in second gear. The instructor, a patient man, helped me up and said: 'Everyone falls once. The point is to get back on straight away.'"),
  L("Γυναίκα", "f", "Πήρα το δίπλωμα με την πρώτη. Τώρα πηγαίνω κάθε μέρα στη δουλειά σε είκοσι λεπτά αντί για μία ώρα, πάντα με κράνος και προσεκτικά. Και ξέρετε ποιο είναι το καλύτερο; Ο πατέρας μου, στα ογδόντα του, μου ζήτησε την περασμένη Κυριακή να τον πάω βόλτα μέχρι τη θάλασσα.", "I passed my test first time. Now I get to work every day in twenty minutes instead of an hour, always with a helmet and carefully. And do you know the best part? Last Sunday my father, at eighty, asked me to take him for a ride down to the sea."),
 ],
 "questions": [
  Q("Γιατί φοβόταν τα μηχανάκια;", ["Είχε πέσει η ίδια από μηχανή", "Ο πατέρας της είχε πάθει σοβαρό ατύχημα", "Η κόρη της είχε τραυματιστεί", "Της το είχε απαγορεύσει ο άντρας της"], 1, "Ο πατέρας μου είχε πάθει ένα σοβαρό ατύχημα όταν ήμουν μικρή"),
  Q("Τι της είπε ο εκπαιδευτής όταν έπεσε;", ["Ότι ίσως δεν είναι για εκείνη", "Ότι όλοι πέφτουν μία φορά και πρέπει να ξανανέβει αμέσως", "Να σταματήσει για εκείνη τη μέρα", "Να αγοράσει πιο μικρό μηχανάκι"], 1, "Όλοι πέφτουν μία φορά. Το θέμα είναι να ξανανέβεις αμέσως"),
  Q("Τι της ζήτησε ο πατέρας της την περασμένη Κυριακή;", ["Να πουλήσει το μηχανάκι", "Να τον πάει βόλτα μέχρι τη θάλασσα", "Να του μάθει να οδηγεί", "Να φοράει πάντα κράνος"], 1, "μου ζήτησε την περασμένη Κυριακή να τον πάω βόλτα μέχρι τη θάλασσα"),
 ],
 "gloss": {"μηχανάκι": "μηχανάκι — motorbike, scooter", "ατύχημα": "ατύχημα — accident", "απαγορευμένη": "απαγορευμένος — forbidden", "προάστιο": "προάστιο — suburb", "συγκοινωνία": "συγκοινωνία — public transport", "προαύλιο": "προαύλιο — yard", "ταχύτητα": "ταχύτητα — gear; speed", "εκπαιδευτής": "εκπαιδευτής — instructor", "υπομονετικός": "υπομονετικός — patient", "δίπλωμα": "δίπλωμα — (driving) licence", "με την πρώτη": "με την πρώτη — at the first attempt", "κράνος": "κράνος — helmet"},
})
ITEMS.append({
 "id": "l88-c1-chameno-kostos", "title": "Γιατί δεν αφήνουμε ένα κακό βιβλίο;", "title_en": "Why don't we put down a bad book?", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την οικονομία της καθημερινής ζωής, ο παρουσιαστής συζητά με μια οικονομολόγο που μελετά τις αποφάσεις των ανθρώπων.",
 "script": [
  L("Παρουσιαστής", "m", "Όλοι το έχουμε κάνει: πληρώσαμε ένα ακριβό εισιτήριο, η παράσταση είναι απαίσια, κι όμως μένουμε ως το τέλος. Γιατί;", "We've all done it: we paid for an expensive ticket, the show is awful, and yet we stay to the end. Why?"),
  L("Οικονομολόγος", "f", "Οι οικονομολόγοι το ονομάζουν «πλάνη του χαμένου κόστους». Τα χρήματα του εισιτηρίου έχουν ήδη ξοδευτεί· δεν θα τα πάρετε πίσω ό,τι κι αν κάνετε. Λογικά, λοιπόν, η μόνη ερώτηση που έχει σημασία είναι: «Από εδώ και πέρα, τι θα μου προσφέρει περισσότερα, να μείνω ή να φύγω;». Εμείς όμως νιώθουμε ότι, αν φύγουμε, θα έχουμε «πετάξει» τα λεφτά μας, και έτσι προσθέτουμε στη χαμένη επένδυση και χαμένο χρόνο.", "Economists call it the 'sunk cost fallacy'. The ticket money has already been spent; you won't get it back whatever you do. Logically, then, the only question that matters is: 'From here on, what will give me more, staying or leaving?' But we feel that if we leave, we'll have 'thrown away' our money, and so we add lost time to the lost investment."),
  L("Παρουσιαστής", "m", "Υπάρχουν πειράματα που το δείχνουν;", "Are there experiments that show this?"),
  L("Οικονομολόγος", "f", "Ένα κλασικό, από τη δεκαετία του ογδόντα: οι ερευνητές ζήτησαν από φοιτητές να φανταστούν ότι έχουν κλείσει δύο εκδρομές για σκι το ίδιο Σαββατοκύριακο, μια ακριβή και μια φθηνότερη, που όμως τους αρέσει περισσότερο. Δεν μπορούν να ακυρώσουν καμία. Περίπου οι μισοί διάλεξαν την ακριβή, δηλαδή αυτή που θα απολάμβαναν λιγότερο, μόνο και μόνο επειδή είχαν πληρώσει περισσότερα.", "A classic one, from the eighties: researchers asked students to imagine they'd booked two ski trips for the same weekend, an expensive one and a cheaper one that they like more. They can't cancel either. About half chose the expensive one, that is, the one they'd enjoy less, purely because they'd paid more for it."),
  L("Παρουσιαστής", "m", "Και πέρα από τα εισιτήρια;", "And beyond tickets?"),
  L("Οικονομολόγος", "f", "Το ίδιο φαινόμενο εμφανίζεται σε πολύ μεγαλύτερη κλίμακα: κυβερνήσεις που συνεχίζουν έργα τα οποία προφανώς δεν θα αποδώσουν, «γιατί έχουμε ήδη ξοδέψει τόσα», ή άνθρωποι που μένουν χρόνια σε μια σχέση ή μια δουλειά που τους κάνει δυστυχισμένους. Το αντίδοτο είναι απλό στη θεωρία, δύσκολο στην πράξη: να κοιτάμε μπροστά, όχι πίσω. Και να θυμόμαστε ότι το να αφήσεις ένα κακό βιβλίο στη μέση δεν είναι αποτυχία· είναι η πρώτη καλή απόφαση.", "The same phenomenon appears on a much larger scale: governments that carry on with projects which plainly won't pay off, 'because we've already spent so much', or people who stay for years in a relationship or a job that makes them unhappy. The antidote is simple in theory, hard in practice: look forward, not back. And remember that putting a bad book down halfway isn't a failure; it's the first good decision."),
 ],
 "questions": [
  Q("Ποια είναι, κατά την οικονομολόγο, η μόνη λογική ερώτηση μετά από μια δαπάνη που δεν επιστρέφεται;", ["Πόσα πλήρωσα;", "Από εδώ και πέρα, τι θα μου προσφέρει περισσότερα;", "Ποιος φταίει για την κακή επιλογή;", "Πώς θα πάρω πίσω τα χρήματά μου;"], 1, "«Από εδώ και πέρα, τι θα μου προσφέρει περισσότερα, να μείνω ή να φύγω;»"),
  Q("Τι έδειξε το πείραμα με τις εκδρομές για σκι;", ["Οι φοιτητές ακύρωσαν και τις δύο εκδρομές", "Οι περισσότεροι διάλεξαν τη φθηνότερη", "Περίπου οι μισοί διάλεξαν την ακριβή, που θα απολάμβαναν λιγότερο", "Κανείς δεν μπορούσε να αποφασίσει"], 2, "Περίπου οι μισοί διάλεξαν την ακριβή, δηλαδή αυτή που θα απολάμβαναν λιγότερο"),
  Q("Ποιο είναι το αντίδοτο που προτείνει;", ["Να μην αγοράζουμε ποτέ ακριβά εισιτήρια", "Να κοιτάμε μπροστά, όχι πίσω", "Να ζητάμε πάντα τη γνώμη των άλλων", "Να ολοκληρώνουμε πάντα ό,τι ξεκινάμε"], 1, "να κοιτάμε μπροστά, όχι πίσω"),
  Q("Πώς βλέπει η οικονομολόγος το να αφήσει κανείς ένα κακό βιβλίο στη μέση;", ["Ως αποτυχία", "Ως έλλειψη υπομονής", "Ως την πρώτη καλή απόφαση", "Ως σπατάλη χρημάτων"], 2, "δεν είναι αποτυχία· είναι η πρώτη καλή απόφαση"),
 ],
 "gloss": {"οικονομολόγο": "οικονομολόγος — economist", "απαίσια": "απαίσιος — awful", "πλάνη": "πλάνη — fallacy, delusion", "χαμένου κόστους": "χαμένο κόστος — sunk cost", "επένδυση": "επένδυση — investment", "ακυρώσουν": "ακυρώνω — to cancel", "απολάμβαναν": "απολαμβάνω — to enjoy", "κλίμακα": "κλίμακα — scale", "αποδώσουν": "αποδίδω — to pay off, yield", "αντίδοτο": "αντίδοτο — antidote", "αποτυχία": "αποτυχία — failure"},
})
ITEMS.append({
 "id": "l88-c1-anoloklirwto", "title": "Η δύναμη του ανολοκλήρωτου", "title_en": "The power of the unfinished", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ομιλία μιας ψυχολόγου σε μια εκδήλωση για τη μνήμη και την παραγωγικότητα.",
 "script": [
  L("Ψυχολόγος", "f", "Τη δεκαετία του 1920, στο Βερολίνο, μια νεαρή φοιτήτρια ψυχολογίας, η Μπλούμα Ζεϊγκάρνικ, καθόταν σε ένα καφενείο με τον καθηγητή της, τον Κουρτ Λέβιν. Παρατήρησαν κάτι παράξενο: ο σερβιτόρος θυμόταν με ακρίβεια όλες τις παραγγελίες που δεν είχαν ακόμη πληρωθεί, αλλά, μόλις ένας πελάτης πλήρωνε, η παραγγελία του φαινόταν να σβήνεται από τη μνήμη του.", "In the 1920s, in Berlin, a young psychology student, Bluma Zeigarnik, was sitting in a café with her professor, Kurt Lewin. They noticed something strange: the waiter remembered precisely all the orders that hadn't yet been paid, but as soon as a customer paid, their order seemed to be wiped from his memory."),
  L("Ψυχολόγος", "f", "Η Ζεϊγκάρνικ μετέφερε την παρατήρηση στο εργαστήριο. Έδινε στους συμμετέχοντες απλές εργασίες, όπως παζλ ή αριθμητικά προβλήματα, και διέκοπτε μερικές από αυτές πριν ολοκληρωθούν. Αργότερα, οι συμμετέχοντες θυμούνταν τις διακομμένες εργασίες πολύ καλύτερα από εκείνες που είχαν τελειώσει. Το φαινόμενο πήρε το όνομά της. Οφείλω πάντως να πω ότι οι μεταγενέστερες επαναλήψεις των πειραμάτων έδωσαν ανάμεικτα αποτελέσματα· το φαινόμενο υπάρχει, αλλά δεν είναι τόσο ισχυρό ή τόσο καθολικό όσο πιστευόταν.", "Zeigarnik took the observation into the laboratory. She gave participants simple tasks, such as puzzles or arithmetic problems, and interrupted some of them before they were finished. Later, the participants remembered the interrupted tasks much better than the ones they had completed. The effect was named after her. I should say, though, that later replications of the experiments gave mixed results; the effect exists, but it isn't as strong or as universal as was believed."),
  L("Ψυχολόγος", "f", "Γιατί μας ενδιαφέρει σήμερα; Πρώτον, γιατί εξηγεί κάτι γνώριμο: τις ανολοκλήρωτες υποχρεώσεις που μας τριβελίζουν το μυαλό τη νύχτα. Δεύτερον, γιατί μια νεότερη έρευνα έδειξε ότι αρκεί κάτι πολύ απλό για να ησυχάσει αυτή η ενόχληση: να γράψουμε ένα συγκεκριμένο σχέδιο για το πότε και πώς θα ολοκληρώσουμε την εργασία. Δεν χρειάζεται να την τελειώσουμε· αρκεί να ξέρει το μυαλό ότι έχει φροντιστεί. Και τρίτον, γιατί το φαινόμενο μπορεί να γίνει σύμμαχος: αν αναβάλλετε συνεχώς κάτι, ξεκινήστε το έστω και για πέντε λεπτά. Το ανολοκλήρωτο θα σας τραβήξει πίσω.", "Why does it interest us today? First, because it explains something familiar: the unfinished obligations that nag at our minds at night. Second, because more recent research showed that something very simple is enough to quiet this nagging: writing down a specific plan for when and how we'll complete the task. We don't need to finish it; it's enough for the mind to know it's been taken care of. And third, because the effect can become an ally: if you keep putting something off, start it, even for five minutes. The unfinished will pull you back."),
 ],
 "questions": [
  Q("Τι παρατήρησαν η Ζεϊγκάρνικ και ο Λέβιν στο καφενείο;", ["Ότι ο σερβιτόρος ξεχνούσε όλες τις παραγγελίες", "Ότι ο σερβιτόρος θυμόταν τις απλήρωτες παραγγελίες αλλά ξεχνούσε όσες είχαν πληρωθεί", "Ότι οι πελάτες θυμούνταν τι είχαν παραγγείλει", "Ότι ο σερβιτόρος έγραφε τα πάντα σε χαρτί"], 1, "ο σερβιτόρος θυμόταν με ακρίβεια όλες τις παραγγελίες που δεν είχαν ακόμη πληρωθεί"),
  Q("Τι λέει η ψυχολόγος για τις μεταγενέστερες επαναλήψεις των πειραμάτων;", ["Ότι επιβεβαίωσαν πλήρως τα αρχικά ευρήματα", "Ότι απέδειξαν πως το φαινόμενο δεν υπάρχει", "Ότι έδωσαν ανάμεικτα αποτελέσματα", "Ότι δεν έγιναν ποτέ"], 2, "οι μεταγενέστερες επαναλήψεις των πειραμάτων έδωσαν ανάμεικτα αποτελέσματα"),
  Q("Τι αρκεί, σύμφωνα με τη νεότερη έρευνα, για να ησυχάσει το μυαλό;", ["Να ολοκληρώσουμε αμέσως την εργασία", "Να γράψουμε ένα συγκεκριμένο σχέδιο για το πότε και πώς θα την ολοκληρώσουμε", "Να την αναθέσουμε σε άλλον", "Να την ξεχάσουμε εντελώς"], 1, "να γράψουμε ένα συγκεκριμένο σχέδιο για το πότε και πώς θα ολοκληρώσουμε την εργασία"),
  Q("Τι συμβουλεύει όσους αναβάλλουν συνεχώς κάτι;", ["Να περιμένουν την κατάλληλη στιγμή", "Να το ξεκινήσουν έστω και για πέντε λεπτά", "Να το χωρίσουν σε δέκα μέρη", "Να ζητήσουν βοήθεια"], 1, "ξεκινήστε το έστω και για πέντε λεπτά"),
 ],
 "gloss": {"παραγωγικότητα": "παραγωγικότητα — productivity", "παραγγελίες": "παραγγελία — order", "εργαστήριο": "εργαστήριο — laboratory", "συμμετέχοντες": "συμμετέχων — participant", "διέκοπτε": "διακόπτω — to interrupt", "διακομμένες": "διακομμένος — interrupted", "μεταγενέστερες": "μεταγενέστερος — later, subsequent", "ανάμεικτα": "ανάμεικτος — mixed", "καθολικό": "καθολικός — universal", "τριβελίζουν": "τριβελίζω — to nag at, gnaw at", "σύμμαχος": "σύμμαχος — ally", "αναβάλλετε": "αναβάλλω — to put off, postpone"},
})

rnd = random.Random(88)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-88.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
