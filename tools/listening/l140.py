# Source for library/listening/listening-140.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l140.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l140-vm-pseires", "title": "Ψείρες στην τάξη", "title_en": "Head lice in the class", "type": "voicemail", "level": "B2",
 "context_el": "Το παιδί σας πηγαίνει στο δημοτικό. Ακούτε ένα μήνυμα από τη δασκάλα του στον τηλεφωνητή σας.",
 "script": [
  L("Δασκάλα", "f", "Καλησπέρα σας, η κυρία Δήμητρα είμαι, η δασκάλα της Τρίτης τάξης. Σας ενημερώνω ότι σε τρία παιδιά της τάξης βρέθηκαν ψείρες. Μην ανησυχείτε, είναι πολύ συνηθισμένο στα σχολεία και δεν έχει καμία σχέση με την καθαριότητα.", "Good evening, it's Mrs Dimitra, the Year Three teacher. I'm letting you know that head lice have been found on three children in the class. Don't worry, it's very common in schools and has nothing to do with cleanliness."),
  L("Δασκάλα", "f", "Σας παρακαλούμε απόψε να ελέγξετε προσεκτικά τα μαλλιά του παιδιού σας, ιδίως πίσω από τα αυτιά και στον σβέρκο, με μια λεπτή χτένα. Αν βρείτε κάτι, ο φαρμακοποιός θα σας προτείνει την κατάλληλη λοσιόν.", "Please check your child's hair carefully tonight, especially behind the ears and on the nape of the neck, with a fine comb. If you find anything, the pharmacist will recommend the right lotion."),
  L("Δασκάλα", "f", "Το παιδί μπορεί να έρθει κανονικά στο σχολείο μετά την πρώτη θεραπεία. Και κάτι ακόμα: πείτε στα παιδιά να μην ανταλλάσσουν σκουφιά και χτένες για λίγο καιρό. Ευχαριστώ πολύ.", "The child can come to school as normal after the first treatment. And one more thing: tell the children not to swap hats and combs for a while. Thank you very much."),
 ],
 "questions": [
  Q("Τι λέει η δασκάλα για τις ψείρες;", ["Ότι οφείλονται σε κακή καθαριότητα", "Ότι είναι πολύ συνηθισμένες στα σχολεία", "Ότι είναι επικίνδυνες", "Ότι βρέθηκαν σε όλη την τάξη"], 1, "είναι πολύ συνηθισμένο στα σχολεία"),
  Q("Πού πρέπει να ελέγξετε ιδιαίτερα;", ["Στο μέτωπο", "Πίσω από τα αυτιά και στον σβέρκο", "Στα φρύδια", "Στα ρούχα"], 1, "ιδίως πίσω από τα αυτιά και στον σβέρκο"),
  Q("Πότε μπορεί το παιδί να γυρίσει στο σχολείο;", ["Μετά από μία εβδομάδα", "Μόνο με χαρτί από γιατρό", "Μετά την πρώτη θεραπεία", "Τον επόμενο μήνα"], 2, "Το παιδί μπορεί να έρθει κανονικά στο σχολείο μετά την πρώτη θεραπεία"),
 ],
 "gloss": {"ψείρες": "ψείρα — louse", "καθαριότητα": "καθαριότητα — cleanliness", "ελέγξετε": "ελέγχω — to check", "σβέρκο": "σβέρκος — nape of the neck", "χτένα": "χτένα — comb", "κατάλληλη": "κατάλληλος — suitable", "λοσιόν": "λοσιόν — lotion", "θεραπεία": "θεραπεία — treatment", "ανταλλάσσουν": "ανταλλάσσω — to swap, exchange", "σκουφιά": "σκούφος — woolly hat"}
})

ITEMS.append({
 "id": "l140-dia-logariasmos", "title": "Ο λογαριασμός στα τέσσερα", "title_en": "Splitting the bill four ways", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους να συζητούν μετά από ένα δείπνο σε ταβέρνα.",
 "script": [
  L("Στέλιος", "m", "Ήρθε ο λογαριασμός: εκατόν είκοσι ευρώ. Λέω να τον μοιράσουμε στα τέσσερα, τριάντα ο καθένας, να τελειώνουμε.", "The bill's here: a hundred and twenty euros. I say we split it four ways, thirty each, and be done with it."),
  L("Δανάη", "f", "Μισό λεπτό. Εγώ έφαγα μόνο μια σαλάτα και ήπια νερό. Εσείς παραγγείλατε μπριζόλες και δύο μπουκάλια κρασί. Δεν μου φαίνεται δίκαιο να πληρώσω το ίδιο.", "Hang on. I only had a salad and drank water. You lot ordered steaks and two bottles of wine. It doesn't seem fair to me to pay the same."),
  L("Στέλιος", "m", "Έχεις δίκιο, συγγνώμη, δεν το σκέφτηκα. Αλλά αν αρχίσουμε να μετράμε ποιος έφαγε τι, θα κάτσουμε εδώ μέχρι το πρωί.", "You're right, sorry, I didn't think. But if we start counting who ate what, we'll be sitting here till morning."),
  L("Δανάη", "f", "Τότε ας κάνουμε κάτι απλό: εγώ δίνω δεκαπέντε για τη σαλάτα και το φιλοδώρημα, και οι τρεις σας μοιράζεστε τα υπόλοιπα. Και την επόμενη φορά, ας το συζητήσουμε πριν παραγγείλουμε.", "Then let's do something simple: I'll put in fifteen for the salad and the tip, and the three of you split the rest. And next time, let's talk about it before we order."),
 ],
 "questions": [
  Q("Τι προτείνει αρχικά ο Στέλιος;", ["Να πληρώσει εκείνος όλο τον λογαριασμό", "Να μοιράσουν τον λογαριασμό στα τέσσερα", "Να πληρώσει ο καθένας ό,τι έφαγε", "Να ζητήσουν έκπτωση"], 1, "Λέω να τον μοιράσουμε στα τέσσερα"),
  Q("Γιατί διαφωνεί η Δανάη;", ["Γιατί δεν έχει μετρητά", "Γιατί το φαγητό ήταν κακό", "Γιατί έφαγε μόνο μια σαλάτα και ήπια νερό", "Γιατί ο λογαριασμός είναι λάθος"], 2, "Εγώ έφαγα μόνο μια σαλάτα και ήπια νερό"),
  Q("Τι προτείνει τελικά η Δανάη;", ["Να δώσει δεκαπέντε ευρώ και οι άλλοι να μοιραστούν τα υπόλοιπα", "Να πληρώσει τριάντα ευρώ", "Να μην αφήσουν φιλοδώρημα", "Να πληρώσει ο Στέλιος για όλους"], 0, "εγώ δίνω δεκαπέντε για τη σαλάτα και το φιλοδώρημα, και οι τρεις σας μοιράζεστε τα υπόλοιπα"),
 ],
 "gloss": {"λογαριασμός": "λογαριασμός — bill", "μοιράσουμε": "μοιράζω — to split, share", "παραγγείλατε": "παραγγέλνω — to order", "μπριζόλες": "μπριζόλα — steak, chop", "δίκαιο": "δίκαιος — fair", "Έχεις δίκιο": "έχω δίκιο — to be right", "φιλοδώρημα": "φιλοδώρημα — tip", "υπόλοιπα": "υπόλοιπο — rest, remainder"}
})

ITEMS.append({
 "id": "l140-int-farmakopoios", "title": "Η μόνη φαρμακοποιός του νησιού", "title_en": "The island's only pharmacist", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική εκπομπή για τη ζωή στα μικρά νησιά.",
 "script": [
  L("Δημοσιογράφος", "m", "Είστε η μόνη φαρμακοποιός σε ένα νησί με τριακόσιους κατοίκους τον χειμώνα. Πώς είναι μια μέρα σας;", "You're the only pharmacist on an island with three hundred residents in winter. What is one of your days like?"),
  L("Φαρμακοποιός", "f", "Το φαρμακείο ανοίγει στις εννιά, αλλά το κινητό μου χτυπά από τις επτά. Επειδή ο γιατρός του κέντρου υγείας είναι συνήθως μόνος, οι κάτοικοι με ρωτούν για τα πάντα: για πυρετούς, για τσιμπήματα από μέλισσες, ακόμα και για τα φάρμακα των ζώων τους.", "The pharmacy opens at nine, but my mobile rings from seven. Because the doctor at the health centre is usually on his own, residents ask me about everything: fevers, bee stings, even their animals' medicines."),
  L("Δημοσιογράφος", "m", "Και τι γίνεται όταν λείπει κάποιο φάρμακο;", "And what happens when a medicine is missing?"),
  L("Φαρμακοποιός", "f", "Αυτό είναι το μεγαλύτερο άγχος μου. Τα φάρμακα έρχονται με το πλοίο δύο φορές την εβδομάδα, και τον χειμώνα, με τα μποφόρ, μπορεί να μην έρθει πλοίο για πέντε μέρες. Γι' αυτό κρατώ πάντα ένα μεγάλο απόθεμα, ιδίως για όσους έχουν χρόνιες ασθένειες. Έχω ένα τετράδιο με το όνομα κάθε ηλικιωμένου και τα φάρμακα που παίρνει.", "That's my biggest worry. Medicines come by boat twice a week, and in winter, with strong winds, there may be no boat for five days. That's why I always keep a large stock, especially for people with chronic illnesses. I have a notebook with the name of every elderly person and the medicines they take."),
 ],
 "questions": [
  Q("Γιατί οι κάτοικοι τη ρωτούν για τα πάντα;", ["Γιατί είναι και γιατρός", "Γιατί ο γιατρός του κέντρου υγείας είναι συνήθως μόνος", "Γιατί δεν υπάρχει κέντρο υγείας", "Γιατί είναι συγγενείς της"], 1, "Επειδή ο γιατρός του κέντρου υγείας είναι συνήθως μόνος"),
  Q("Ποιο είναι το μεγαλύτερο άγχος της;", ["Να λείψει κάποιο φάρμακο", "Οι τουρίστες του καλοκαιριού", "Τα χαμηλά κέρδη", "Η μοναξιά"], 0, "Αυτό είναι το μεγαλύτερο άγχος μου"),
  Q("Τι έχει σε ένα τετράδιο;", ["Τα χρέη των πελατών", "Τα δρομολόγια των πλοίων", "Το όνομα κάθε ηλικιωμένου και τα φάρμακα που παίρνει", "Συνταγές μαγειρικής"], 2, "Έχω ένα τετράδιο με το όνομα κάθε ηλικιωμένου και τα φάρμακα που παίρνει"),
 ],
 "gloss": {"φαρμακοποιός": "φαρμακοποιός — pharmacist", "κέντρου υγείας": "κέντρο υγείας — health centre", "πυρετούς": "πυρετός — fever", "τσιμπήματα": "τσίμπημα — sting, bite", "άγχος": "άγχος — anxiety, worry", "μποφόρ": "μποφόρ — Beaufort (wind force)", "απόθεμα": "απόθεμα — stock, supply", "χρόνιες": "χρόνιος — chronic", "ασθένειες": "ασθένεια — illness", "τετράδιο": "τετράδιο — notebook"}
})

ITEMS.append({
 "id": "l140-ann-metro", "title": "Λεωφορεία αντί για μετρό", "title_en": "Buses instead of the metro", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε σταθμό του μετρό και ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνητής", "m", "Ενημερώνουμε το επιβατικό κοινό ότι, λόγω εργασιών αναβάθμισης των γραμμών, τα δύο επόμενα Σαββατοκύριακα οι σταθμοί από το Μοναστηράκι έως το Φάληρο θα παραμείνουν κλειστοί, από το Σάββατο στις πέντε το πρωί έως την Κυριακή στο τέλος της βάρδιας.", "We inform passengers that, because of works to upgrade the tracks, on the next two weekends the stations from Monastiraki to Faliro will remain closed, from Saturday at five in the morning until the end of service on Sunday."),
  L("Εκφωνητής", "m", "Για την εξυπηρέτησή σας, θα κυκλοφορούν λεωφορεία αντικατάστασης κάθε δέκα λεπτά, με στάσεις έξω από κάθε σταθμό. Τα λεωφορεία θα έχουν στο μπροστινό τζάμι μια κίτρινη πινακίδα με την ένδειξη «Μετρό».", "For your convenience, replacement buses will run every ten minutes, with stops outside each station. The buses will have a yellow sign with the word 'Metro' on the windscreen."),
  L("Εκφωνητής", "m", "Τα εισιτήρια του μετρό ισχύουν κανονικά και στα λεωφορεία. Επειδή η διαδρομή θα διαρκεί περίπου είκοσι λεπτά περισσότερο, παρακαλούνται όσοι πηγαίνουν στο λιμάνι για πλοίο να ξεκινήσουν νωρίτερα.", "Metro tickets are valid on the buses as normal. Because the journey will take about twenty minutes longer, passengers going to the port for a ferry are asked to set off earlier."),
 ],
 "questions": [
  Q("Γιατί θα κλείσουν οι σταθμοί;", ["Λόγω απεργίας", "Λόγω εργασιών αναβάθμισης των γραμμών", "Λόγω μιας συναυλίας", "Λόγω καθαρισμού"], 1, "λόγω εργασιών αναβάθμισης των γραμμών"),
  Q("Πώς θα αναγνωρίζετε τα λεωφορεία αντικατάστασης;", ["Είναι κόκκινα", "Έχουν μια κίτρινη πινακίδα με την ένδειξη «Μετρό»", "Έχουν αριθμό 100", "Δεν έχουν κάποιο σήμα"], 1, "μια κίτρινη πινακίδα με την ένδειξη «Μετρό»"),
  Q("Τι ζητείται από όσους πηγαίνουν στο λιμάνι;", ["Να πάρουν ταξί", "Να αγοράσουν άλλο εισιτήριο", "Να ξεκινήσουν νωρίτερα", "Να πάνε με τα πόδια"], 2, "παρακαλούνται όσοι πηγαίνουν στο λιμάνι για πλοίο να ξεκινήσουν νωρίτερα"),
 ],
 "gloss": {"επιβατικό κοινό": "επιβατικό κοινό — passengers (formal)", "αναβάθμισης": "αναβάθμιση — upgrade", "παραμείνουν": "παραμένω — to remain", "βάρδιας": "βάρδια — shift; here: service", "εξυπηρέτησή": "εξυπηρέτηση — service, convenience", "αντικατάστασης": "αντικατάσταση — replacement", "τζάμι": "τζάμι — windscreen, glass", "πινακίδα": "πινακίδα — sign", "ένδειξη": "ένδειξη — label, indication", "ισχύουν": "ισχύω — to be valid"}
})

ITEMS.append({
 "id": "l140-news-vythos", "title": "Δύτες καθαρίζουν το λιμάνι", "title_en": "Divers clean the harbour", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα σύντομο ρεπορτάζ στις τοπικές ειδήσεις.",
 "script": [
  L("Ρεπόρτερ", "f", "Περισσότεροι από σαράντα εθελοντές δύτες βούτηξαν χθες στο λιμάνι της πόλης για να καθαρίσουν τον βυθό. Μέσα σε τέσσερις ώρες ανέσυραν πάνω από δύο τόνους σκουπίδια: λάστιχα αυτοκινήτων, καρέκλες, ποδήλατα, ακόμα και ένα παλιό ψυγείο.", "More than forty volunteer divers dived into the town's harbour yesterday to clean the seabed. Within four hours they brought up over two tonnes of rubbish: car tyres, chairs, bicycles, even an old fridge."),
  L("Ρεπόρτερ", "f", "Στην προβλήτα, δεκάδες κάτοικοι, ανάμεσά τους πολλά παιδιά, βοηθούσαν να ξεχωριστούν τα αντικείμενα για ανακύκλωση. Θαλάσσιοι βιολόγοι έλεγχαν κάθε αντικείμενο πριν πεταχτεί, γιατί πάνω σε αρκετά είχαν εγκατασταθεί μικρά καβούρια και χταπόδια, που επιστράφηκαν στη θάλασσα.", "On the jetty, dozens of residents, many children among them, helped sort the items for recycling. Marine biologists checked each item before it was thrown away, because small crabs and octopuses had settled on several of them, and these were returned to the sea."),
  L("Ρεπόρτερ", "f", "Οι διοργανωτές λένε ότι το πιο συνηθισμένο εύρημα ήταν τα πλαστικά μπουκάλια, και ζητούν από τον δήμο να τοποθετήσει περισσότερους κάδους στην παραλία. Ο επόμενος καθαρισμός έχει προγραμματιστεί για την άνοιξη.", "The organisers say the most common find was plastic bottles, and they're asking the municipality to put more bins on the seafront. The next clean-up is scheduled for the spring."),
 ],
 "questions": [
  Q("Πόσα σκουπίδια ανέσυραν οι δύτες;", ["Δύο κιλά", "Πάνω από δύο τόνους", "Σαράντα τόνους", "Τέσσερις τόνους"], 1, "ανέσυραν πάνω από δύο τόνους σκουπίδια"),
  Q("Γιατί οι βιολόγοι έλεγχαν κάθε αντικείμενο;", ["Για να βρουν αρχαία", "Γιατί πάνω σε αρκετά είχαν εγκατασταθεί μικρά καβούρια και χταπόδια", "Για να υπολογίσουν το βάρος", "Για να τα πουλήσουν"], 1, "γιατί πάνω σε αρκετά είχαν εγκατασταθεί μικρά καβούρια και χταπόδια"),
  Q("Τι ζητούν οι διοργανωτές από τον δήμο;", ["Να απαγορεύσει τα σκάφη", "Χρήματα για τον επόμενο καθαρισμό", "Να τοποθετήσει περισσότερους κάδους στην παραλία", "Να κλείσει το λιμάνι"], 2, "ζητούν από τον δήμο να τοποθετήσει περισσότερους κάδους στην παραλία"),
 ],
 "gloss": {"δύτες": "δύτης — diver", "βούτηξαν": "βουτάω — to dive", "βυθό": "βυθός — seabed", "ανέσυραν": "ανασύρω — to bring up, pull out", "λάστιχα": "λάστιχο — tyre", "προβλήτα": "προβλήτα — jetty, pier", "ξεχωριστούν": "ξεχωρίζω — to sort, separate", "καβούρια": "καβούρι — crab", "εύρημα": "εύρημα — find", "κάδους": "κάδος — bin"}
})

ITEMS.append({
 "id": "l140-vm-ilektrologos", "title": "Ο ηλεκτρολογικός πίνακας", "title_en": "The fuse box", "type": "voicemail", "level": "B2",
 "context_el": "Χθες έπεσε το ρεύμα στο σπίτι σας. Ακούτε ένα μήνυμα από τον ηλεκτρολόγο στον τηλεφωνητή σας.",
 "script": [
  L("Ηλεκτρολόγος", "m", "Γεια σας, ο Μιχάλης είμαι, ο ηλεκτρολόγος. Κοίταξα τις φωτογραφίες που μου στείλατε. Ο ηλεκτρολογικός σας πίνακας είναι πάνω από τριάντα χρονών και οι ασφάλειες είναι από τις παλιές, τις βιδωτές. Γι' αυτό πέφτουν κάθε φορά που ανάβετε μαζί τον φούρνο και το πλυντήριο.", "Hello, it's Michalis, the electrician. I looked at the photos you sent me. Your fuse box is over thirty years old and the fuses are the old screw-in kind. That's why they trip every time you turn on the oven and the washing machine together."),
  L("Ηλεκτρολόγος", "m", "Η λύση είναι να αλλάξουμε όλο τον πίνακα και να βάλουμε και διακόπτη διαρροής, που σας προστατεύει από ηλεκτροπληξία. Είναι δουλειά μιας μέρας, και θα μείνετε χωρίς ρεύμα περίπου πέντε ώρες.", "The solution is to replace the whole box and also fit a residual-current device, which protects you from electric shock. It's a day's work, and you'll be without power for about five hours."),
  L("Ηλεκτρολόγος", "m", "Μπορώ να έρθω την άλλη Τρίτη. Μέχρι τότε, προσπαθήστε να μη λειτουργείτε ταυτόχρονα πολλές μεγάλες συσκευές. Θα σας στείλω την προσφορά με μήνυμα.", "I can come next Tuesday. Until then, try not to run several big appliances at the same time. I'll send you the quote by message."),
 ],
 "questions": [
  Q("Γιατί πέφτουν οι ασφάλειες;", ["Γιατί ο φούρνος είναι χαλασμένος", "Γιατί ο πίνακας είναι παλιός και ανάβουν μαζί ο φούρνος και το πλυντήριο", "Γιατί μπήκε νερό στον πίνακα", "Γιατί ο λογαριασμός δεν πληρώθηκε"], 1, "Γι' αυτό πέφτουν κάθε φορά που ανάβετε μαζί τον φούρνο και το πλυντήριο"),
  Q("Τι προτείνει ο ηλεκτρολόγος;", ["Να αλλάξουν όλο τον πίνακα και να μπει διακόπτης διαρροής", "Να αλλάξουν μόνο τις ασφάλειες", "Να αγοράσουν καινούργιο φούρνο", "Να καλέσουν την εταιρεία ρεύματος"], 0, "Η λύση είναι να αλλάξουμε όλο τον πίνακα και να βάλουμε και διακόπτη διαρροής"),
  Q("Τι πρέπει να κάνετε μέχρι την Τρίτη;", ["Να κλείσετε τον γενικό διακόπτη", "Να μη χρησιμοποιείτε καθόλου ρεύμα", "Να μη λειτουργείτε ταυτόχρονα πολλές μεγάλες συσκευές", "Να του στείλετε κι άλλες φωτογραφίες"], 2, "προσπαθήστε να μη λειτουργείτε ταυτόχρονα πολλές μεγάλες συσκευές"),
 ],
 "gloss": {"ηλεκτρολόγος": "ηλεκτρολόγος — electrician", "ηλεκτρολογικός σας πίνακας": "ηλεκτρολογικός πίνακας — fuse box, consumer unit", "ασφάλειες": "ασφάλεια — fuse", "βιδωτές": "βιδωτός — screw-in", "διακόπτη διαρροής": "διακόπτης διαρροής — residual-current device", "ηλεκτροπληξία": "ηλεκτροπληξία — electric shock", "ταυτόχρονα": "ταυτόχρονα — at the same time", "συσκευές": "συσκευή — appliance", "προσφορά": "προσφορά — quote, offer"}
})

ITEMS.append({
 "id": "l140-dia-douleia-efivos", "title": "Μια δουλειά για το καλοκαίρι", "title_en": "A summer job", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε μια μητέρα και τον δεκαεξάχρονο γιο της να συζητούν.",
 "script": [
  L("Άρης", "m", "Μαμά, ο θείος του Φώτη έχει καφετέρια στην παραλία και ψάχνει παιδιά για το καλοκαίρι. Θέλω να δουλέψω εκεί, τέσσερις ώρες τη μέρα.", "Mum, Fotis's uncle has a café on the beach and he's looking for young people for the summer. I want to work there, four hours a day."),
  L("Μητέρα", "f", "Είσαι δεκαέξι. Μήπως είναι νωρίς; Και του χρόνου έχεις Πανελλήνιες, θα πρέπει να διαβάζεις.", "You're sixteen. Isn't it a bit early? And next year you have the national exams, you'll need to study."),
  L("Άρης", "m", "Γι' αυτό το θέλω τώρα, όχι του χρόνου. Θα μάθω να μιλάω με κόσμο, θα βγάζω τα δικά μου λεφτά και δεν θα σου ζητάω για κάθε έξοδο. Ο Φώτης δούλεψε πέρσι και λέει ότι έμαθε περισσότερα εκεί παρά σε όλο το σχολείο.", "That's why I want it now, not next year. I'll learn to talk to people, I'll earn my own money and I won't ask you for every outing. Fotis worked last year and says he learned more there than in the whole of school."),
  L("Μητέρα", "f", "Εντάξει, αλλά με δύο όρους. Πρώτα, θέλω να μιλήσω με τον θείο του για το ωράριο και να έχεις κανονική ασφάλιση. Και δεύτερον, από τα λεφτά που θα βγάλεις, το μισό θα μπει σε έναν λογαριασμό για τις σπουδές σου.", "All right, but on two conditions. First, I want to talk to his uncle about the hours, and you must have proper insurance. And second, half of the money you earn goes into an account for your studies."),
 ],
 "questions": [
  Q("Τι ανησυχεί αρχικά τη μητέρα;", ["Ότι η καφετέρια είναι μακριά", "Ότι ο Άρης είναι μικρός και του χρόνου έχει Πανελλήνιες", "Ότι ο μισθός είναι χαμηλός", "Ότι δεν ξέρει τον Φώτη"], 1, "Είσαι δεκαέξι. Μήπως είναι νωρίς;"),
  Q("Τι λέει ο Φώτης για τη δουλειά του πέρσι;", ["Ότι ήταν πολύ κουραστική", "Ότι δεν πληρώθηκε", "Ότι έμαθε περισσότερα εκεί παρά σε όλο το σχολείο", "Ότι δεν θα ξαναδουλέψει"], 2, "λέει ότι έμαθε περισσότερα εκεί παρά σε όλο το σχολείο"),
  Q("Ποιος είναι ένας από τους όρους της μητέρας;", ["Το μισό από τα λεφτά να μπει σε λογαριασμό για τις σπουδές του", "Να δουλεύει μόνο τα Σαββατοκύριακα", "Να δουλεύει μαζί του και ο Φώτης", "Να γυρίζει σπίτι πριν από τις οχτώ"], 0, "το μισό θα μπει σε έναν λογαριασμό για τις σπουδές σου"),
 ],
 "gloss": {"καφετέρια": "καφετέρια — café", "Πανελλήνιες": "Πανελλήνιες — national university entrance exams", "έξοδο": "έξοδος — outing, night out", "όρους": "όρος — condition, term", "ωράριο": "ωράριο — working hours", "ασφάλιση": "ασφάλιση — (social) insurance", "λογαριασμό": "λογαριασμός — (bank) account", "σπουδές": "σπουδές — studies"}
})

ITEMS.append({
 "id": "l140-int-klarinitzis", "title": "Ένα κλαρίνο στα πανηγύρια", "title_en": "A clarinet at the village festivals", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή για την παραδοσιακή μουσική.",
 "script": [
  L("Δημοσιογράφος", "f", "Παίζετε κλαρίνο στα πανηγύρια της Ηπείρου εδώ και τριάντα χρόνια. Πώς ξεκινήσατε;", "You've been playing the clarinet at festivals in Epirus for thirty years. How did you start?"),
  L("Μουσικός", "m", "Ο παππούς μου ήταν κλαριντζής, και ο πατέρας μου έπαιζε λαούτο στην ίδια κομπανία. Στα έντεκά μου μού έδωσαν το παλιό κλαρίνο του παππού. Δεν έμαθα ποτέ νότες· έμαθα ακούγοντας και μιμούμενος, όπως μάθαιναν όλοι τότε.", "My grandfather was a clarinet player, and my father played the lute in the same band. At eleven they gave me my grandfather's old clarinet. I never learned to read music; I learned by listening and imitating, the way everyone learned back then."),
  L("Δημοσιογράφος", "f", "Πόσο κρατάει ένα πανηγύρι;", "How long does a festival last?"),
  L("Μουσικός", "m", "Συχνά από τις δέκα το βράδυ μέχρι το πρωί. Κάποιες φορές παίζουμε δώδεκα ώρες σχεδόν χωρίς διάλειμμα. Το πιο συγκινητικό είναι όταν ένας ηλικιωμένος σηκώνεται και ζητά ένα τραγούδι από το χωριό του, που κανείς άλλος δεν θυμάται πια. Τότε νιώθεις ότι δεν παίζεις απλώς μουσική, αλλά κρατάς ζωντανή τη μνήμη ενός τόπου.", "Often from ten at night until the morning. Sometimes we play for twelve hours with almost no break. The most moving thing is when an old man stands up and asks for a song from his village that nobody else remembers any more. Then you feel you're not just playing music, but keeping the memory of a place alive."),
 ],
 "questions": [
  Q("Πώς έμαθε να παίζει κλαρίνο;", ["Σε ωδείο, με νότες", "Ακούγοντας και μιμούμενος", "Με μαθήματα στο ίντερνετ", "Στο σχολείο"], 1, "έμαθα ακούγοντας και μιμούμενος"),
  Q("Πόσο κρατάει συχνά ένα πανηγύρι;", ["Δύο ώρες", "Ένα απόγευμα", "Από τις δέκα το βράδυ μέχρι το πρωί", "Τρεις μέρες"], 2, "Συχνά από τις δέκα το βράδυ μέχρι το πρωί"),
  Q("Ποια στιγμή είναι για εκείνον η πιο συγκινητική;", ["Όταν ένας ηλικιωμένος ζητά ένα ξεχασμένο τραγούδι από το χωριό του", "Όταν τελειώνει το πανηγύρι", "Όταν πληρώνεται", "Όταν χορεύουν οι νέοι"], 0, "όταν ένας ηλικιωμένος σηκώνεται και ζητά ένα τραγούδι από το χωριό του"),
 ],
 "gloss": {"κλαρίνο": "κλαρίνο — clarinet", "πανηγύρια": "πανηγύρι — village festival", "κλαριντζής": "κλαριντζής — clarinet player (folk)", "λαούτο": "λαούτο — lute", "κομπανία": "κομπανία — folk band", "νότες": "νότα — (musical) note", "μιμούμενος": "μιμούμενος — imitating", "διάλειμμα": "διάλειμμα — break", "συγκινητικό": "συγκινητικός — moving"}
})

ITEMS.append({
 "id": "l140-c1-thiseas", "title": "Το πλοίο του Θησέα", "title_en": "The ship of Theseus", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη φιλοσοφίας για το ευρύ κοινό.",
 "script": [
  L("Ομιλήτρια", "f", "Ο Πλούταρχος, στον βίο του Θησέα, αναφέρει ότι οι Αθηναίοι διατηρούσαν για αιώνες το πλοίο με το οποίο ο μυθικός ήρωας είχε γυρίσει από την Κρήτη. Όποτε μια σανίδα σάπιζε, την αντικαθιστούσαν με καινούργια. Κάποια στιγμή, λέει, οι φιλόσοφοι άρχισαν να διαφωνούν: ήταν ακόμα το ίδιο πλοίο ή ένα διαφορετικό;", "Plutarch, in his Life of Theseus, reports that the Athenians preserved for centuries the ship in which the mythical hero had returned from Crete. Whenever a plank rotted, they replaced it with a new one. At some point, he says, philosophers began to disagree: was it still the same ship or a different one?"),
  L("Ομιλήτρια", "f", "Το ερώτημα έγινε ακόμη πιο περίπλοκο τον δέκατο έβδομο αιώνα, όταν ο Άγγλος φιλόσοφος Τόμας Χομπς πρόσθεσε μια ανησυχητική λεπτομέρεια. Ας υποθέσουμε ότι κάποιος μάζευε όλες τις παλιές σανίδες που πετάχτηκαν και ξανάχτιζε μ' αυτές το πλοίο. Ποιο από τα δύο θα ήταν τότε το «αληθινό» πλοίο του Θησέα;", "The question became even more complicated in the seventeenth century, when the English philosopher Thomas Hobbes added a troubling detail. Suppose someone gathered all the old planks that had been thrown away and rebuilt the ship with them. Which of the two would then be the 'real' ship of Theseus?"),
  L("Ομιλήτρια", "f", "Το παράδοξο δεν είναι ένα απλό πνευματικό παιχνίδι. Το σώμα μας ανανεώνει συνεχώς πολλά από τα κύτταρά του· οι πόλεις αλλάζουν κτίρια και κατοίκους· τα κράτη αλλάζουν νόμους και σύνορα. Κι όμως, μιλάμε για τον ίδιο άνθρωπο, την ίδια πόλη, το ίδιο κράτος. Ίσως, όπως έχουν προτείνει ορισμένοι φιλόσοφοι, η ταυτότητα ενός πράγματος να μη βρίσκεται στο υλικό του, αλλά στη συνέχεια, στη μορφή και στην ιστορία που μοιράζονται τα μέρη του.", "The paradox is not just an intellectual game. Our body constantly renews many of its cells; cities change buildings and inhabitants; states change laws and borders. And yet we speak of the same person, the same city, the same state. Perhaps, as some philosophers have suggested, the identity of a thing lies not in its material, but in the continuity, the form and the history that its parts share."),
 ],
 "questions": [
  Q("Τι έκαναν οι Αθηναίοι με το πλοίο του Θησέα, σύμφωνα με τον Πλούταρχο;", ["Το έκαψαν προς τιμήν του", "Αντικαθιστούσαν κάθε σάπια σανίδα με καινούργια", "Το πούλησαν στους Κρητικούς", "Το έθαψαν σε έναν τάφο"], 1, "Όποτε μια σανίδα σάπιζε, την αντικαθιστούσαν με καινούργια"),
  Q("Τι πρόσθεσε ο Τόμας Χομπς;", ["Ότι το πλοίο δεν υπήρξε ποτέ", "Ότι ο Θησέας ήταν ιστορικό πρόσωπο", "Την περίπτωση ενός δεύτερου πλοίου, χτισμένου από τις παλιές σανίδες", "Ότι το πλοίο βρίσκεται στην Αγγλία"], 2, "Ας υποθέσουμε ότι κάποιος μάζευε όλες τις παλιές σανίδες που πετάχτηκαν και ξανάχτιζε μ' αυτές το πλοίο"),
  Q("Γιατί, κατά την ομιλήτρια, το παράδοξο δεν είναι απλό παιχνίδι;", ["Γιατί αφορά και το σώμα μας, τις πόλεις και τα κράτη", "Γιατί το λύνουν μόνο οι μαθηματικοί", "Γιατί έχει λυθεί οριστικά", "Γιατί αφορά μόνο τα πλοία"], 0, "Το σώμα μας ανανεώνει συνεχώς πολλά από τα κύτταρά του"),
  Q("Πού βρίσκεται ίσως η ταυτότητα ενός πράγματος, σύμφωνα με ορισμένους φιλοσόφους;", ["Μόνο στο υλικό του", "Στο όνομά του", "Στην τιμή του", "Στη συνέχεια, στη μορφή και στην ιστορία που μοιράζονται τα μέρη του"], 3, "στη συνέχεια, στη μορφή και στην ιστορία που μοιράζονται τα μέρη του"),
 ],
 "gloss": {"διάλεξη": "διάλεξη — lecture", "βίο": "βίος — life (biography)", "διατηρούσαν": "διατηρώ — to preserve", "μυθικός": "μυθικός — mythical", "σανίδα": "σανίδα — plank", "σάπιζε": "σαπίζω — to rot", "αντικαθιστούσαν": "αντικαθιστώ — to replace", "περίπλοκο": "περίπλοκος — complicated", "ανησυχητική": "ανησυχητικός — troubling", "παράδοξο": "παράδοξο — paradox", "ανανεώνει": "ανανεώνω — to renew", "κύτταρά": "κύτταρο — cell", "ταυτότητα": "ταυτότητα — identity", "συνέχεια": "συνέχεια — continuity"}
})

ITEMS.append({
 "id": "l140-c1-plank", "title": "Η επιστήμη προοδεύει «μία κηδεία τη φορά»;", "title_en": "Does science advance 'one funeral at a time'?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια κοινωνιολόγο της επιστήμης.",
 "script": [
  L("Δημοσιογράφος", "m", "Υπάρχει μια φράση που αποδίδεται στον φυσικό Μαξ Πλανκ: ότι η επιστήμη προοδεύει «μία κηδεία τη φορά». Την είπε πραγματικά;", "There's a phrase attributed to the physicist Max Planck: that science advances 'one funeral at a time'. Did he really say it?"),
  L("Κοινωνιολόγος", "f", "Όχι με αυτά τα λόγια. Η σύντομη εκδοχή είναι μεταγενέστερη απλοποίηση. Στην αυτοβιογραφία του όμως ο Πλανκ έγραψε κάτι παρόμοιο: ότι μια νέα επιστημονική αλήθεια δεν θριαμβεύει επειδή πείθει τους αντιπάλους της, αλλά επειδή οι αντίπαλοι κάποτε πεθαίνουν και μεγαλώνει μια νέα γενιά, εξοικειωμένη μαζί της από την αρχή.", "Not in those words. The short version is a later simplification. In his autobiography, however, Planck wrote something similar: that a new scientific truth does not triumph because it convinces its opponents, but because its opponents eventually die and a new generation grows up that is familiar with it from the start."),
  L("Δημοσιογράφος", "m", "Είναι αλήθεια ή απλώς μια πικρή παρατήρηση;", "Is it true or just a bitter observation?"),
  L("Κοινωνιολόγος", "f", "Το 2019 μια ομάδα οικονομολόγων προσπάθησε να το ελέγξει. Μελέτησαν τι συνέβη σε ερευνητικά πεδία της βιολογίας και της ιατρικής μετά τον αιφνίδιο θάνατο εξεχόντων επιστημόνων. Βρήκαν ότι τα επόμενα χρόνια αυξήθηκαν οι δημοσιεύσεις από ερευνητές που δεν είχαν συνεργαστεί ποτέ μαζί τους, και ότι οι εργασίες αυτές συχνά έφερναν νέες ιδέες και γίνονταν ευρέως γνωστές.", "In 2019 a team of economists tried to test it. They studied what happened in research fields in biology and medicine after the sudden death of eminent scientists. They found that in the following years publications increased from researchers who had never collaborated with them, and that this work often brought new ideas and became widely known."),
  L("Δημοσιογράφος", "m", "Άρα οι μεγάλοι επιστήμονες εμποδίζουν την πρόοδο;", "So great scientists hold back progress?"),
  L("Κοινωνιολόγος", "f", "Θα ήταν άδικο να το πούμε έτσι. Δεν πρόκειται για κακή πρόθεση, αλλά για δομές: όποιος έχει κύρος επηρεάζει τις χρηματοδοτήσεις, τις κρίσεις των άρθρων και τις προσλήψεις, και οι νεότεροι διστάζουν να αμφισβητήσουν ένα πεδίο που φαίνεται «κλειστό». Το συμπέρασμα δεν είναι να περιμένουμε κηδείες, αλλά να σχεδιάζουμε θεσμούς που αφήνουν χώρο στις αιρετικές ιδέες.", "It would be unfair to put it that way. It's not about bad intentions, but about structures: whoever has prestige influences funding, peer review and hiring, and younger researchers hesitate to challenge a field that seems 'closed'. The conclusion isn't to wait for funerals, but to design institutions that leave room for heretical ideas."),
 ],
 "questions": [
  Q("Είπε ο Πλανκ τη φράση «μία κηδεία τη φορά»;", ["Ναι, ακριβώς με αυτά τα λόγια", "Όχι με αυτά τα λόγια, αλλά έγραψε κάτι παρόμοιο στην αυτοβιογραφία του", "Όχι, την είπε ο Αϊνστάιν", "Δεν είναι γνωστό"], 1, "Όχι με αυτά τα λόγια"),
  Q("Τι βρήκε η έρευνα του 2019;", ["Ότι η πρόοδος σταματά μετά τον θάνατο ενός μεγάλου επιστήμονα", "Ότι οι μαθητές του συνεχίζουν το ίδιο έργο", "Ότι αυξάνονται οι δημοσιεύσεις από ερευνητές εκτός του κύκλου του, συχνά με νέες ιδέες", "Ότι κανείς δεν ασχολείται πια με το πεδίο"], 2, "αυξήθηκαν οι δημοσιεύσεις από ερευνητές που δεν είχαν συνεργαστεί ποτέ μαζί τους"),
  Q("Πώς εξηγεί η κοινωνιολόγος το φαινόμενο;", ["Με τις δομές και την επιρροή όσων έχουν κύρος", "Με την κακή πρόθεση των μεγάλων επιστημόνων", "Με την έλλειψη χρημάτων", "Με την τύχη"], 0, "Δεν πρόκειται για κακή πρόθεση, αλλά για δομές"),
  Q("Ποιο είναι, κατά την κοινωνιολόγο, το σωστό συμπέρασμα;", ["Να περιμένουμε να αλλάξουν οι γενιές", "Να μην εμπιστευόμαστε τους μεγάλους επιστήμονες", "Να σταματήσουν οι κρίσεις των άρθρων", "Να σχεδιάζουμε θεσμούς που αφήνουν χώρο στις αιρετικές ιδέες"], 3, "να σχεδιάζουμε θεσμούς που αφήνουν χώρο στις αιρετικές ιδέες"),
 ],
 "gloss": {"κοινωνιολόγο": "κοινωνιολόγος — sociologist", "αποδίδεται": "αποδίδομαι — to be attributed", "προοδεύει": "προοδεύω — to progress", "κηδεία": "κηδεία — funeral", "απλοποίηση": "απλοποίηση — simplification", "θριαμβεύει": "θριαμβεύω — to triumph", "εξοικειωμένη": "εξοικειωμένος — familiar", "αιφνίδιο": "αιφνίδιος — sudden", "εξεχόντων": "εξέχων — eminent", "δημοσιεύσεις": "δημοσίευση — publication", "κύρος": "κύρος — prestige", "χρηματοδοτήσεις": "χρηματοδότηση — funding", "αμφισβητήσουν": "αμφισβητώ — to challenge", "αιρετικές": "αιρετικός — heretical"}
})

rnd = random.Random(140)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-140.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
