# Source for library/listening/listening-8.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l8.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l8-ann-nero", "title": "Διακοπή υδροδότησης", "title_en": "The water will be cut off", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση της δημοτικής επιχείρησης ύδρευσης σε τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Η Δημοτική Επιχείρηση Ύδρευσης και Αποχέτευσης ενημερώνει ότι την Τρίτη, από τις εννιά το πρωί έως τις τέσσερις το απόγευμα, θα γίνει διακοπή υδροδότησης στις συνοικίες Αγία Τριάδα και Παλιό Λιμάνι, λόγω αντικατάστασης του κεντρικού αγωγού.", "The Municipal Water Supply and Sewerage Company announces that on Tuesday, from nine in the morning until four in the afternoon, the water supply will be cut off in the Agia Triada and Old Harbour districts, owing to the replacement of the main pipe."),
  L("Εκφωνήτρια", "f", "Σε περίπτωση που οι εργασίες καθυστερήσουν, η υδροδότηση ενδέχεται να αποκατασταθεί αργότερα από την προβλεπόμενη ώρα. Όταν το νερό επανέλθει, μπορεί για λίγα λεπτά να είναι θολό. Συνιστάται να το αφήσετε να τρέξει, πριν το χρησιμοποιήσετε για πόσιμο ή για μαγείρεμα.", "If the work is delayed, the supply may be restored later than the scheduled time. When the water comes back, it may be cloudy for a few minutes. You are advised to let it run before using it for drinking or cooking."),
  L("Εκφωνήτρια", "f", "Για τις ανάγκες των κατοίκων, βυτιοφόρο με πόσιμο νερό θα βρίσκεται στην πλατεία της Αγίας Τριάδας. Η επιχείρηση ζητά την κατανόηση των πολιτών για την ταλαιπωρία.", "For residents' needs, a tanker with drinking water will be stationed in Agia Triada square. The company apologises to the public for the inconvenience."),
 ],
 "questions": [
  Q("Γιατί θα κοπεί το νερό;", ["Λόγω λειψυδρίας", "Για να αντικατασταθεί ο κεντρικός αγωγός", "Λόγω βλάβης από τη βροχή", "Επειδή δεν πληρώθηκαν οι λογαριασμοί"], 1, "λόγω αντικατάστασης του κεντρικού αγωγού"),
  Q("Τι συμβουλεύει η ανακοίνωση όταν επιστρέψει το νερό;", ["Να το βράσετε για δέκα λεπτά", "Να μην το πιείτε για μια μέρα", "Να το αφήσετε να τρέξει λίγο πριν το πιείτε", "Να ειδοποιήσετε την επιχείρηση"], 2, "Συνιστάται να το αφήσετε να τρέξει, πριν το χρησιμοποιήσετε για πόσιμο"),
  Q("Πού μπορούν οι κάτοικοι να βρουν νερό την Τρίτη;", ["Σε ένα βυτιοφόρο στην πλατεία", "Στα γραφεία της επιχείρησης", "Στα σούπερ μάρκετ, δωρεάν", "Στο Παλιό Λιμάνι"], 0, "βυτιοφόρο με πόσιμο νερό θα βρίσκεται στην πλατεία της Αγίας Τριάδας"),
 ],
 "gloss": {"υδροδότησης": "υδροδότηση — water supply", "Αποχέτευσης": "αποχέτευση — sewerage", "συνοικίες": "συνοικία — district, neighbourhood", "αγωγού": "αγωγός — pipe, main", "ενδέχεται": "ενδέχεται — it is possible that, may", "αποκατασταθεί": "αποκαθίσταμαι — to be restored", "επανέλθει": "επανέρχομαι — to return", "θολό": "θολός — cloudy, murky", "πόσιμο": "πόσιμος — drinkable", "βυτιοφόρο": "βυτιοφόρο — tanker truck", "ταλαιπωρία": "ταλαιπωρία — inconvenience, hassle"},
})

ITEMS.append({
 "id": "l8-vm-synergeio", "title": "Νέα από το συνεργείο", "title_en": "News from the garage", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα που άφησε ο μηχανικός ενός συνεργείου στην κυρία Αλεξίου.",
 "script": [
  L("Μηχανικός", "m", "Καλημέρα σας, κυρία Αλεξίου, ο Στέλιος είμαι από το συνεργείο. Σας παίρνω για το αυτοκίνητο. Κοιτάξαμε τον θόρυβο που μας είπατε: είναι τα τακάκια στα μπροστινά φρένα, έχουν φαγωθεί τελείως και πρέπει να αλλαχτούν. Αυτό δεν σηκώνει αναβολή, δεν είναι ασφαλές να κυκλοφορείτε έτσι.", "Good morning, Mrs Alexiou, it's Stelios from the garage. I'm calling about the car. We looked at the noise you told us about: it's the pads on the front brakes, they're completely worn and need changing. That can't wait, it isn't safe to drive like that."),
  L("Μηχανικός", "m", "Είδαμε επίσης ότι πλησιάζει και το σέρβις των εξήντα χιλιάδων, με αλλαγή λαδιών και φίλτρων. Αν θέλετε, το κάνουμε τώρα μαζί, για να μην ξαναφέρετε το αυτοκίνητο σε δύο μήνες. Τα φρένα μόνα τους βγαίνουν γύρω στα ενενήντα ευρώ, μαζί με το σέρβις γύρω στα διακόσια σαράντα.", "We also saw that the sixty-thousand service is coming up, with an oil and filter change. If you like, we'll do it now as well, so you don't have to bring the car back in two months. The brakes alone come to around ninety euros, with the service around two hundred and forty."),
  L("Μηχανικός", "m", "Πείτε μου μέχρι το μεσημέρι τι θέλετε να κάνουμε, γιατί πρέπει να παραγγείλω τα ανταλλακτικά. Αν μου απαντήσετε έγκαιρα, το αυτοκίνητο θα είναι έτοιμο αύριο το απόγευμα.", "Let me know by midday what you'd like us to do, because I need to order the parts. If you get back to me in time, the car will be ready tomorrow afternoon."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα του αυτοκινήτου;", ["Χρειάζεται καινούργια λάστιχα", "Τα τακάκια των μπροστινών φρένων έχουν φθαρεί", "Η μπαταρία έχει αδειάσει", "Χαλάει λάδια"], 1, "είναι τα τακάκια στα μπροστινά φρένα, έχουν φαγωθεί τελείως"),
  Q("Τι προτείνει ο μηχανικός;", ["Να γίνει μαζί με τα φρένα και το σέρβις", "Να αλλάξει αυτοκίνητο", "Να περιμένει δύο μήνες για τα φρένα", "Να πάει σε άλλο συνεργείο"], 0, "Αν θέλετε, το κάνουμε τώρα μαζί, για να μην ξαναφέρετε το αυτοκίνητο σε δύο μήνες."),
  Q("Γιατί θέλει απάντηση μέχρι το μεσημέρι;", ["Γιατί το συνεργείο κλείνει νωρίς", "Γιατί φεύγει για διακοπές", "Για να παραγγείλει τα ανταλλακτικά", "Γιατί θα ανέβουν οι τιμές"], 2, "πρέπει να παραγγείλω τα ανταλλακτικά"),
 ],
 "gloss": {"συνεργείο": "συνεργείο — (car) garage, repair shop", "τακάκια": "τακάκι — brake pad", "φρένα": "φρένο — brake", "έχουν φαγωθεί": "τρώγομαι — to wear out", "δεν σηκώνει αναβολή": "δεν σηκώνει αναβολή — it can't be put off", "σέρβις": "σέρβις — service (of a car)", "λαδιών": "λάδι — oil", "φίλτρων": "φίλτρο — filter", "ανταλλακτικά": "ανταλλακτικό — spare part", "έγκαιρα": "έγκαιρα — in time"},
})

ITEMS.append({
 "id": "l8-dia-logariasmos", "title": "Ο λογαριασμός του ρεύματος", "title_en": "The electricity bill", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση ανάμεσα σε δύο συγκάτοικους, τη Μυρτώ και τον Ορέστη.",
 "script": [
  L("Μυρτώ", "f", "Ορέστη, ήρθε ο λογαριασμός του ρεύματος. Κάτσε πριν τον δεις: εκατόν ογδόντα ευρώ για δύο μήνες.", "Orestis, the electricity bill has come. Sit down before you see it: a hundred and eighty euros for two months."),
  L("Ορέστης", "m", "Πόσα; Τον χειμώνα πληρώναμε τα μισά! Μήπως έκαναν λάθος στην ένδειξη του μετρητή;", "How much? In winter we paid half that! Maybe they got the meter reading wrong?"),
  L("Μυρτώ", "f", "Το σκέφτηκα κι εγώ, αλλά κατέβηκα και κοίταξα τον μετρητή. Η ένδειξη είναι σωστή. Νομίζω ότι φταίει το κλιματιστικό. Το αφήνεις αναμμένο όλη νύχτα στο δωμάτιό σου, στους δεκαοκτώ βαθμούς.", "I thought so too, but I went down and checked the meter. The reading is correct. I think the air conditioner is to blame. You leave it on all night in your room, at eighteen degrees."),
  L("Ορέστης", "m", "Εντάξει, φταίω λίγο, το παραδέχομαι. Αλλά και εσύ βάζεις το πλυντήριο για δύο μπλούζες.", "OK, it's partly my fault, I admit it. But you also run the washing machine for two T-shirts."),
  L("Μυρτώ", "f", "Δίκιο έχεις, θα περιμένω να γεμίζει. Ας κάνουμε κάτι: μοιράζουμε αυτόν τον λογαριασμό ως εξής, εσύ τα εκατό κι εγώ τα ογδόντα, και από δω και πέρα το κλιματιστικό στους είκοσι έξι και με χρονοδιακόπτη.", "You're right, I'll wait until it's full. Let's do this: we split this bill like this, you a hundred and me eighty, and from now on the air conditioner at twenty-six and on a timer."),
  L("Ορέστης", "m", "Συμφωνώ. Και να δούμε μήπως μας συμφέρει άλλος πάροχος. Η αδερφή μου άλλαξε και πληρώνει πολύ λιγότερα.", "Agreed. And let's see whether another provider would be better value. My sister switched and pays much less."),
 ],
 "questions": [
  Q("Τι έλεγξε η Μυρτώ πριν μιλήσει στον Ορέστη;", ["Αν ο λογαριασμός ήταν πληρωμένος", "Την ένδειξη του μετρητή", "Τις τιμές άλλων παρόχων", "Αν το κλιματιστικό είχε βλάβη"], 1, "κατέβηκα και κοίταξα τον μετρητή. Η ένδειξη είναι σωστή."),
  Q("Πώς θα μοιράσουν τον λογαριασμό;", ["Μισά-μισά", "Θα τον πληρώσει όλο ο Ορέστης", "Ο Ορέστης θα πληρώσει περισσότερα", "Η Μυρτώ θα πληρώσει περισσότερα"], 2, "εσύ τα εκατό κι εγώ τα ογδόντα"),
  Q("Τι αναλαμβάνει να αλλάξει η Μυρτώ;", ["Θα βάζει το πλυντήριο μόνο όταν είναι γεμάτο", "Θα σβήνει το κλιματιστικό", "Θα αλλάξει πάροχο", "Θα πληρώνει τους λογαριασμούς"], 0, "θα περιμένω να γεμίζει"),
  Q("Τι προτείνει ο Ορέστης στο τέλος;", ["Να αγοράσουν καινούργιο κλιματιστικό", "Να εξετάσουν αν τους συμφέρει άλλος πάροχος", "Να μετακομίσουν", "Να μιλήσουν στην αδερφή του"], 1, "να δούμε μήπως μας συμφέρει άλλος πάροχος"),
 ],
 "gloss": {"συγκάτοικους": "συγκάτοικος — flatmate", "ένδειξη": "ένδειξη — reading (of a meter)", "μετρητή": "μετρητής — meter", "κλιματιστικό": "κλιματιστικό — air conditioner", "αναμμένο": "αναμμένος — switched on, lit", "το παραδέχομαι": "παραδέχομαι — to admit", "πλυντήριο": "πλυντήριο — washing machine", "από δω και πέρα": "από δω και πέρα — from now on", "χρονοδιακόπτη": "χρονοδιακόπτης — timer", "μας συμφέρει": "με συμφέρει — it pays, is good value for me", "πάροχος": "πάροχος — (service) provider"},
})

ITEMS.append({
 "id": "l8-dia-teloneio", "title": "Το δέμα που κόλλησε στο τελωνείο", "title_en": "The parcel stuck at customs", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα κατάστημα των ταχυδρομείων ανάμεσα σε μια πελάτισσα και έναν υπάλληλο.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Περιμένω ένα δέμα από τον Καναδά εδώ και τρεις εβδομάδες. Στην ιστοσελίδα γράφει «σε εκκρεμότητα στο τελωνείο». Τι σημαίνει αυτό;", "Good morning. I've been waiting for a parcel from Canada for three weeks. The website says 'pending at customs'. What does that mean?"),
  L("Υπάλληλος", "m", "Δώστε μου τον αριθμό αποστολής να δω… Ναι, το δέμα σας έρχεται από χώρα εκτός Ευρωπαϊκής Ένωσης, οπότε περνάει από τελωνειακό έλεγχο. Η αξία που δήλωσε ο αποστολέας είναι εκατόν πενήντα ευρώ, άρα αναλογεί ΦΠΑ.", "Give me the tracking number so I can look… Yes, your parcel is coming from a country outside the European Union, so it goes through customs. The value declared by the sender is a hundred and fifty euros, so VAT is due."),
  L("Πελάτισσα", "f", "Μα είναι δώρο! Η θεία μου μού έστειλε ένα πλεκτό κι ένα βιβλίο.", "But it's a present! My aunt sent me a knitted jumper and a book."),
  L("Υπάλληλος", "m", "Καταλαβαίνω. Τα δώρα από ιδιώτη σε ιδιώτη απαλλάσσονται μόνο αν η αξία τους είναι κάτω από σαράντα πέντε ευρώ. Επειδή η δηλωμένη αξία είναι μεγαλύτερη, θα πρέπει να πληρώσετε τον φόρο, συν ένα μικρό τέλος εκτελωνισμού.", "I understand. Gifts from one private individual to another are exempt only if their value is under forty-five euros. Because the declared value is higher, you'll have to pay the tax, plus a small customs clearance fee."),
  L("Πελάτισσα", "f", "Και πώς γίνεται αυτό; Πρέπει να πάω στο τελωνείο;", "And how is that done? Do I have to go to the customs office?"),
  L("Υπάλληλος", "m", "Όχι, θα σας έρθει ηλεκτρονικό μήνυμα με σύνδεσμο. Ανεβάζετε μια φωτογραφία της ταυτότητάς σας, πληρώνετε με κάρτα, και σε δύο με τρεις εργάσιμες το δέμα έρχεται εδώ. Αν δεν πληρώσετε μέσα σε είκοσι μέρες, επιστρέφεται στον αποστολέα.", "No, you'll get an email with a link. You upload a photo of your ID card, pay by card, and in two to three working days the parcel arrives here. If you don't pay within twenty days, it goes back to the sender."),
 ],
 "questions": [
  Q("Γιατί το δέμα περνάει από τελωνείο;", ["Γιατί περιέχει απαγορευμένο αντικείμενο", "Γιατί έρχεται από χώρα εκτός ΕΕ", "Γιατί είναι πολύ βαρύ", "Γιατί η διεύθυνση ήταν λάθος"], 1, "το δέμα σας έρχεται από χώρα εκτός Ευρωπαϊκής Ένωσης"),
  Q("Γιατί η πελάτισσα πρέπει να πληρώσει, αν και είναι δώρο;", ["Γιατί η δηλωμένη αξία είναι πάνω από το όριο απαλλαγής", "Γιατί τα βιβλία φορολογούνται πάντα", "Γιατί ο αποστολέας είναι εταιρεία", "Γιατί άργησε να το παραλάβει"], 0, "απαλλάσσονται μόνο αν η αξία τους είναι κάτω από σαράντα πέντε ευρώ"),
  Q("Τι πρέπει να κάνει για να πάρει το δέμα;", ["Να πάει αυτοπροσώπως στο τελωνείο", "Να ζητήσει από τη θεία της να το ξαναστείλει", "Να πληρώσει ηλεκτρονικά μέσω του συνδέσμου που θα λάβει", "Να πληρώσει μετρητά στο ταχυδρομείο"], 2, "θα σας έρθει ηλεκτρονικό μήνυμα με σύνδεσμο ... πληρώνετε με κάρτα"),
 ],
 "gloss": {"δέμα": "δέμα — parcel", "σε εκκρεμότητα": "σε εκκρεμότητα — pending", "τελωνείο": "τελωνείο — customs (office)", "αριθμό αποστολής": "αριθμός αποστολής — tracking number", "αποστολέας": "αποστολέας — sender", "αναλογεί": "αναλογεί — is due, corresponds", "πλεκτό": "πλεκτό — knitted garment", "απαλλάσσονται": "απαλλάσσομαι — to be exempt", "τέλος εκτελωνισμού": "τέλος εκτελωνισμού — customs clearance fee", "σύνδεσμο": "σύνδεσμος — link", "εργάσιμες": "εργάσιμη (μέρα) — working day"},
})

ITEMS.append({
 "id": "l8-mon-giagia", "title": "Η γιαγιά μου και το κινητό", "title_en": "My grandmother and the smartphone", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε τη Ζωή να μιλάει σε ένα podcast για το πώς έμαθε στη γιαγιά της να χρησιμοποιεί κινητό.",
 "script": [
  L("Ζωή", "f", "Η γιαγιά μου είναι ογδόντα δύο χρονών και μέχρι πέρσι είχε ένα κινητό με κουμπιά, που το χρησιμοποιούσε μόνο για να απαντάει. Όταν έφυγα για σπουδές στη Γερμανία, μου είπε: «Θέλω να σε βλέπω, όχι μόνο να σε ακούω». Έτσι, το καλοκαίρι, της πήρα ένα έξυπνο κινητό και αποφάσισα να γίνω η δασκάλα της.", "My grandmother is eighty-two and until last year she had a phone with buttons that she used only for answering. When I left to study in Germany, she said to me: 'I want to see you, not just hear you.' So in the summer I got her a smartphone and decided to be her teacher."),
  L("Ζωή", "f", "Το πρώτο που κατάλαβα είναι ότι εμείς οι νέοι εξηγούμε πολύ γρήγορα. Λέμε «πάτα εκεί, σύρε προς τα πάνω» και τα έχουμε κάνει πριν καν εκείνη δει τι έγινε. Άρχισα λοιπόν να της γράφω σε ένα τετράδιο κάθε βήμα, με μεγάλα γράμματα, και να την αφήνω να το κάνει μόνη της, ακόμα κι αν αργούσε.", "The first thing I realised is that we young people explain far too fast. We say 'tap there, swipe up' and we've done it before she has even seen what happened. So I started writing every step in a notebook for her, in big letters, and letting her do it herself, even when she was slow."),
  L("Ζωή", "f", "Το δεύτερο ήταν ο φόβος. Φοβόταν ότι αν πατήσει κάτι λάθος, θα «χαλάσει» το κινητό ή θα της πάρουν τα λεφτά. Της είπα ότι δεν χαλάει τίποτα με ένα λάθος πάτημα, αλλά και ότι ποτέ δεν δίνουμε κωδικούς σε όποιον μας τους ζητήσει με μήνυμα.", "The second was fear. She was afraid that if she pressed something wrong, she'd 'break' the phone or someone would take her money. I told her nothing breaks from one wrong tap, but also that we never give passwords to anyone who asks for them by message."),
  L("Ζωή", "f", "Σήμερα με παίρνει βιντεοκλήση κάθε Κυριακή, και τις προάλλες μού έστειλε φωτογραφία από τις ντομάτες του κήπου. Δεν ξέρω ποια από τις δυο μας έμαθε περισσότερα: εγώ πάντως έμαθα να έχω υπομονή.", "Today she video-calls me every Sunday, and the other day she sent me a photo of the tomatoes in her garden. I don't know which of us learned more: anyway, I learned to be patient."),
 ],
 "questions": [
  Q("Γιατί η γιαγιά ήθελε έξυπνο κινητό;", ["Για να διαβάζει ειδήσεις", "Για να βλέπει την εγγονή της που σπουδάζει στο εξωτερικό", "Γιατί χάλασε το παλιό της", "Για να πληρώνει λογαριασμούς"], 1, "«Θέλω να σε βλέπω, όχι μόνο να σε ακούω»"),
  Q("Ποιο λάθος των νέων διαπίστωσε η Ζωή;", ["Ότι εξηγούν πολύ γρήγορα", "Ότι δεν έχουν χρόνο για τους παππούδες", "Ότι χρησιμοποιούν πολλά αγγλικά", "Ότι γράφουν με μικρά γράμματα"], 0, "εμείς οι νέοι εξηγούμε πολύ γρήγορα"),
  Q("Τι φοβόταν η γιαγιά;", ["Ότι το κινητό θα της κάνει κακό στα μάτια", "Ότι θα ξεχάσει τα βήματα", "Ότι με ένα λάθος θα χαλάσει το κινητό ή θα χάσει χρήματα", "Ότι θα την κοροϊδέψουν"], 2, "Φοβόταν ότι αν πατήσει κάτι λάθος, θα «χαλάσει» το κινητό ή θα της πάρουν τα λεφτά."),
  Q("Τι λέει η Ζωή ότι έμαθε η ίδια;", ["Να μαγειρεύει", "Να κάνει βιντεοκλήσεις", "Να καλλιεργεί ντομάτες", "Να έχει υπομονή"], 3, "εγώ πάντως έμαθα να έχω υπομονή"),
 ],
 "gloss": {"κουμπιά": "κουμπί — button", "έξυπνο κινητό": "έξυπνο κινητό — smartphone", "σύρε": "σέρνω — to drag, swipe", "τετράδιο": "τετράδιο — notebook, exercise book", "πάτημα": "πάτημα — press, tap", "κωδικούς": "κωδικός — password, code", "βιντεοκλήση": "βιντεοκλήση — video call", "τις προάλλες": "τις προάλλες — the other day", "υπομονή": "υπομονή — patience"},
})

ITEMS.append({
 "id": "l8-mon-xorodia", "title": "Χορωδία για αρχάριους", "title_en": "A choir for beginners", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε τον Χρήστο, έναν λογιστή πενήντα χρονών, να μιλάει για τη χορωδία στην οποία μπήκε πριν από δύο χρόνια.",
 "script": [
  L("Χρήστος", "m", "Όλη μου τη ζωή πίστευα ότι δεν έχω φωνή. Στο σχολείο, η δασκάλα της μουσικής μού είχε πει να «κάνω ότι τραγουδάω» στη γιορτή, και αυτό μου έμεινε. Πριν από δύο χρόνια, ο δήμος έβγαλε μια ανακοίνωση: χορωδία ενηλίκων, δεν χρειάζεται να ξέρετε νότες, δεν γίνεται οντισιόν. Πήγα σχεδόν για πλάκα.", "All my life I believed I had no voice. At school the music teacher told me to 'pretend to sing' at the school celebration, and that stuck with me. Two years ago the council put out a notice: adult choir, no need to read music, no audition. I went almost as a joke."),
  L("Χρήστος", "m", "Η μαέστρος μάς εξήγησε από την πρώτη μέρα ότι σχεδόν όλοι μπορούν να τραγουδήσουν σωστά, αρκεί να μάθουν να ακούνε. Κάναμε ασκήσεις αναπνοής, που στην αρχή μου φαίνονταν αστείες, και μαθαίναμε τα τραγούδια ακούγοντας, φωνή φωνή. Οι βασικές φωνές είναι τέσσερις· εμένα με έβαλαν στους βαρύτονους.", "The conductor explained from day one that almost everyone can sing in tune, as long as they learn to listen. We did breathing exercises, which seemed silly to me at first, and we learned the songs by ear, part by part. There are four basic voice parts; they put me with the baritones."),
  L("Χρήστος", "m", "Δεν θα σας πω ότι έγινα σολίστ. Αλλά κάθε Τετάρτη βράδυ, για δύο ώρες, δεν σκέφτομαι ούτε φορολογικές δηλώσεις ούτε προθεσμίες. Και όταν τα Χριστούγεννα τραγουδήσαμε στην πλατεία και η κόρη μου με κοίταζε από το πλήθος, ένιωσα ότι νίκησα επιτέλους εκείνη τη δασκάλα.", "I won't tell you I became a soloist. But every Wednesday evening, for two hours, I don't think about tax returns or deadlines. And when we sang in the square at Christmas and my daughter was watching me from the crowd, I felt I had finally beaten that teacher."),
 ],
 "questions": [
  Q("Γιατί ο Χρήστος πίστευε ότι δεν μπορεί να τραγουδήσει;", ["Γιατί δεν ήξερε νότες", "Εξαιτίας ενός σχολίου της δασκάλας του στο σχολείο", "Γιατί είχε πρόβλημα στις φωνητικές χορδές", "Γιατί τον κορόιδευε η οικογένειά του"], 1, "η δασκάλα της μουσικής μού είχε πει να «κάνω ότι τραγουδάω» ... και αυτό μου έμεινε"),
  Q("Τι πίστευε η μαέστρος;", ["Ότι μόνο λίγοι έχουν ταλέντο", "Ότι πρέπει πρώτα να μάθουν νότες", "Ότι σχεδόν όλοι μπορούν να τραγουδήσουν σωστά αν μάθουν να ακούνε", "Ότι οι ενήλικες δεν μαθαίνουν εύκολα"], 2, "σχεδόν όλοι μπορούν να τραγουδήσουν σωστά, αρκεί να μάθουν να ακούνε"),
  Q("Τι του προσφέρει κυρίως η χορωδία;", ["Ένα διάλειμμα από το άγχος της δουλειάς", "Επιπλέον εισόδημα", "Επαγγελματική καριέρα στο τραγούδι", "Νέους πελάτες"], 0, "δεν σκέφτομαι ούτε φορολογικές δηλώσεις ούτε προθεσμίες"),
 ],
 "gloss": {"χορωδία": "χορωδία — choir", "για πλάκα": "για πλάκα — for fun, as a joke", "νότες": "νότα — (musical) note", "οντισιόν": "οντισιόν — audition", "μαέστρος": "μαέστρος — conductor", "αναπνοής": "αναπνοή — breathing", "φωνή φωνή": "φωνή φωνή — part by part", "βαρύτονους": "βαρύτονος — baritone", "σολίστ": "σολίστ — soloist", "φορολογικές δηλώσεις": "φορολογική δήλωση — tax return", "προθεσμίες": "προθεσμία — deadline", "πλήθος": "πλήθος — crowd"},
})

ITEMS.append({
 "id": "l8-rep-adespota", "title": "Τα αδέσποτα της πόλης", "title_en": "The town's stray animals", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για ένα πρόγραμμα ενός δήμου για τα αδέσποτα ζώα.",
 "script": [
  L("Ρεπόρτερ", "m", "Πριν από τρία χρόνια, στους δρόμους του δήμου ζούσαν, σύμφωνα με υπολογισμούς, πάνω από τετρακόσιοι αδέσποτοι σκύλοι. Κάποιοι κάτοικοι τούς τάιζαν, άλλοι παραπονιούνταν για γαβγίσματα και για επιθέσεις σε ποδηλάτες. Σήμερα ο αριθμός έχει μειωθεί σχεδόν στο μισό.", "Three years ago, according to estimates, over four hundred stray dogs were living on the municipality's streets. Some residents fed them, others complained about barking and attacks on cyclists. Today the number has fallen by almost half."),
  L("Ρεπόρτερ", "m", "Το μυστικό, λέει ο υπεύθυνος του προγράμματος, δεν είναι κάποια θαυματουργή λύση, αλλά η συστηματική στείρωση. Κάθε ζώο που περισυλλέγεται εμβολιάζεται, στειρώνεται, παίρνει ηλεκτρονική σήμανση και, αν δεν βρεθεί οικογένεια να το υιοθετήσει, επιστρέφει στη γειτονιά του, όπου το φροντίζουν εθελοντές.", "The secret, says the programme's coordinator, is not some miracle solution but systematic sterilisation. Every animal that is picked up is vaccinated, neutered, microchipped and, if no family is found to adopt it, returned to its neighbourhood, where volunteers look after it."),
  L("Ρεπόρτερ", "m", "Σημαντικό ρόλο έπαιξαν και οι υιοθεσίες: μέσα από ημέρες γνωριμίας στο πάρκο, πάνω από εκατόν πενήντα σκυλιά βρήκαν σπίτι. Το μεγαλύτερο πρόβλημα παραμένει η εγκατάλειψη. Κάθε καλοκαίρι, λένε οι εθελοντές, εμφανίζονται κουτάβια δεμένα σε κολόνες ή αφημένα σε χωράφια. Ο νόμος προβλέπει πλέον βαριά πρόστιμα, αλλά οι παραβάτες σπάνια εντοπίζονται.", "Adoptions also played an important part: through meet-and-greet days in the park, over a hundred and fifty dogs found homes. The biggest problem remains abandonment. Every summer, the volunteers say, puppies turn up tied to posts or left in fields. The law now provides for heavy fines, but offenders are rarely tracked down."),
 ],
 "questions": [
  Q("Τι άλλαξε τα τελευταία τρία χρόνια;", ["Τα αδέσποτα σχεδόν μειώθηκαν στο μισό", "Τα αδέσποτα διπλασιάστηκαν", "Απαγορεύτηκε το τάισμα", "Οι εθελοντές σταμάτησαν να βοηθούν"], 0, "Σήμερα ο αριθμός έχει μειωθεί σχεδόν στο μισό."),
  Q("Ποια είναι, κατά τον υπεύθυνο, η βάση της επιτυχίας;", ["Τα πρόστιμα", "Η συστηματική στείρωση των ζώων", "Η μεταφορά των ζώων σε άλλη πόλη", "Τα νέα καταφύγια"], 1, "δεν είναι κάποια θαυματουργή λύση, αλλά η συστηματική στείρωση"),
  Q("Τι γίνεται με ένα ζώο που δεν υιοθετείται;", ["Μένει μόνιμα σε καταφύγιο", "Στέλνεται στο εξωτερικό", "Επιστρέφει στη γειτονιά του και το φροντίζουν εθελοντές", "Το παίρνει ο δήμος σε φάρμα"], 2, "επιστρέφει στη γειτονιά του, όπου το φροντίζουν εθελοντές"),
  Q("Ποιο πρόβλημα παραμένει;", ["Η έλλειψη κτηνιάτρων", "Οι επιθέσεις σε ποδηλάτες", "Η έλλειψη χρημάτων", "Η εγκατάλειψη ζώων, κυρίως το καλοκαίρι"], 3, "Το μεγαλύτερο πρόβλημα παραμένει η εγκατάλειψη. Κάθε καλοκαίρι ... εμφανίζονται κουτάβια"),
 ],
 "gloss": {"αδέσποτα": "αδέσποτος — stray", "υπολογισμούς": "υπολογισμός — estimate, calculation", "τάιζαν": "ταΐζω — to feed", "γαβγίσματα": "γάβγισμα — barking", "θαυματουργή": "θαυματουργός — miraculous", "στείρωση": "στείρωση — sterilisation, neutering", "περισυλλέγεται": "περισυλλέγω — to pick up, collect", "εμβολιάζεται": "εμβολιάζω — to vaccinate", "ηλεκτρονική σήμανση": "ηλεκτρονική σήμανση — microchipping", "να το υιοθετήσει": "υιοθετώ — to adopt", "εγκατάλειψη": "εγκατάλειψη — abandonment", "κουτάβια": "κουτάβι — puppy", "παραβάτες": "παραβάτης — offender"},
})

ITEMS.append({
 "id": "l8-rep-elia", "title": "Η ελιά σε έναν θερμότερο κόσμο", "title_en": "The olive in a warmer world", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τη σοδειά της ελιάς και την τιμή του ελαιολάδου.",
 "script": [
  L("Ρεπόρτερ", "f", "Στα ελαιοτριβεία της Μεσσηνίας η εικόνα φέτος είναι μικτή. Μετά από δύο δύσκολες χρονιές, με καύσωνες την άνοιξη, την ώρα που ανθίζουν τα δέντρα, η παραγωγή ανέκαμψε, αλλά παραμένει μακριά από τα επίπεδα του παρελθόντος.", "At the olive mills of Messinia the picture this year is mixed. After two difficult years, with heatwaves in spring just when the trees flower, production has recovered, but it remains far from past levels."),
  L("Ρεπόρτερ", "f", "Ο κύριος Γιαννακόπουλος καλλιεργεί τριακόσια δέντρα που φύτεψε ο προπάππους του. «Η ελιά είναι ανθεκτική», μας λέει, «αντέχει την ξηρασία καλύτερα από τα περισσότερα δέντρα. Αυτό που δεν αντέχει είναι ο ζεστός αέρας πάνω στο άνθος. Τότε το άνθος καίγεται και δεν δένει καρπός».", "Mr Giannakopoulos grows three hundred trees planted by his great-grandfather. 'The olive is hardy,' he tells us, 'it withstands drought better than most trees. What it can't stand is hot wind on the blossom. Then the blossom burns and no fruit sets.'"),
  L("Ρεπόρτερ", "f", "Η μειωμένη παραγωγή σε όλη τη Μεσόγειο εκτόξευσε την τιμή του ελαιολάδου, που σχεδόν τριπλασιάστηκε μέσα σε δύο χρόνια. Οι παραγωγοί είδαν καλύτερες τιμές, αλλά πολλά νοικοκυριά άρχισαν να αγοράζουν λιγότερο ή να στρέφονται σε φθηνότερα σπορέλαια. Οι γεωπόνοι συστήνουν ποικιλίες που ανθίζουν πιο νωρίς και άρδευση σε κρίσιμες εβδομάδες, κάτι όμως που απαιτεί νερό, το οποίο επίσης λιγοστεύει.", "Lower production across the Mediterranean sent olive oil prices soaring; they nearly tripled within two years. Producers saw better prices, but many households began buying less or turning to cheaper seed oils. Agronomists recommend varieties that flower earlier and irrigation during critical weeks, which, however, requires water, which is also becoming scarce."),
 ],
 "questions": [
  Q("Τι προκάλεσε τις κακές σοδειές των προηγούμενων χρόνων;", ["Οι παγετοί του χειμώνα", "Οι καύσωνες την άνοιξη, όταν ανθίζουν τα δέντρα", "Μια ασθένεια των δέντρων", "Η έλλειψη εργατών"], 1, "με καύσωνες την άνοιξη, την ώρα που ανθίζουν τα δέντρα"),
  Q("Τι λέει ο κύριος Γιαννακόπουλος για την ελιά;", ["Ότι δεν αντέχει την ξηρασία", "Ότι χρειάζεται πολύ νερό", "Ότι αντέχει την ξηρασία αλλά όχι τον ζεστό αέρα στο άνθος", "Ότι θέλει να την ξεριζώσει"], 2, "αντέχει την ξηρασία καλύτερα από τα περισσότερα δέντρα. Αυτό που δεν αντέχει είναι ο ζεστός αέρας πάνω στο άνθος"),
  Q("Πώς αντέδρασαν πολλά νοικοκυριά στην αύξηση της τιμής;", ["Αγόρασαν περισσότερο για να κάνουν απόθεμα", "Αγόρασαν λιγότερο ή στράφηκαν σε φθηνότερα λάδια", "Άρχισαν να φυτεύουν ελιές", "Δεν άλλαξαν τίποτα"], 1, "πολλά νοικοκυριά άρχισαν να αγοράζουν λιγότερο ή να στρέφονται σε φθηνότερα σπορέλαια"),
  Q("Ποια δυσκολία έχει η λύση της άρδευσης;", ["Είναι παράνομη", "Κάνει το λάδι πικρό", "Απαιτεί νερό, που επίσης λιγοστεύει", "Είναι πολύ αργή"], 2, "κάτι όμως που απαιτεί νερό, το οποίο επίσης λιγοστεύει"),
 ],
 "gloss": {"σοδειά": "σοδειά — harvest, crop", "ελαιοτριβεία": "ελαιοτριβείο — olive mill", "ανθίζουν": "ανθίζω — to flower", "ανέκαμψε": "ανακάμπτω — to recover", "προπάππους": "προπάππους — great-grandfather", "ανθεκτική": "ανθεκτικός — hardy, resistant", "ξηρασία": "ξηρασία — drought", "άνθος": "άνθος — blossom, flower", "δεν δένει καρπός": "δένει ο καρπός — the fruit sets", "εκτόξευσε": "εκτοξεύω — to send soaring, launch", "σπορέλαια": "σπορέλαιο — seed oil", "γεωπόνοι": "γεωπόνος — agronomist", "ποικιλίες": "ποικιλία — variety", "άρδευση": "άρδευση — irrigation", "λιγοστεύει": "λιγοστεύω — to dwindle, become scarce"},
})

ITEMS.append({
 "id": "l8-int-toponymia", "title": "Τα ονόματα των χωριών", "title_en": "The names of the villages", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν ιστορικό που μελετά τις μετονομασίες οικισμών στην Ελλάδα του εικοστού αιώνα.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Παπαδημητρίου, πολλοί αναγνώστες μάς γράφουν ότι στα χαρτιά των παππούδων τους το χωριό τους έχει άλλο όνομα από το σημερινό. Πώς εξηγείται αυτό;", "Mr Papadimitriou, many readers write to us that in their grandparents' papers their village has a different name from today's. How is that explained?"),
  L("Ιστορικός", "m", "Ανάμεσα στο 1913 και τη δεκαετία του εβδομήντα μετονομάστηκαν περίπου τέσσερις χιλιάδες οικισμοί, κυρίως στη Μακεδονία, την Ήπειρο και τη Θράκη. Τα παλιά ονόματα ήταν συχνά σλαβικής, τουρκικής, αρβανίτικης ή βλάχικης προέλευσης, και το κράτος τα θεωρούσε υπόλειμμα μιας εποχής που ήθελε να αφήσει πίσω του.", "Between 1913 and the 1970s about four thousand settlements were renamed, mainly in Macedonia, Epirus and Thrace. The old names were often of Slavic, Turkish, Arvanitic or Vlach origin, and the state regarded them as a remnant of an era it wanted to leave behind."),
  L("Δημοσιογράφος", "f", "Με ποιο κριτήριο επιλέγονταν τα νέα ονόματα;", "By what criterion were the new names chosen?"),
  L("Ιστορικός", "m", "Η επιτροπή που ήταν αρμόδια προτιμούσε ονόματα από την αρχαία γραμματεία, ακόμα κι όταν η σύνδεση με τον τόπο ήταν αμφίβολη. Κάποτε απλώς μετέφραζαν το παλιό όνομα: ένα χωριό που λεγόταν στα τουρκικά «άσπρη πηγή» έγινε Ασπρόβρυση. Άλλοτε πάλι πήραν το όνομα ενός αγίου ή ενός ήρωα της επανάστασης.", "The responsible committee preferred names from ancient literature, even when the link with the place was doubtful. Sometimes they simply translated the old name: a village called 'white spring' in Turkish became Asprovrysi. At other times they took the name of a saint or a hero of the revolution."),
  L("Δημοσιογράφος", "f", "Και οι κάτοικοι; Υιοθέτησαν τα νέα ονόματα;", "And the residents? Did they adopt the new names?"),
  L("Ιστορικός", "m", "Όχι πάντα, και όχι αμέσως. Σε πολλά μέρη οι ηλικιωμένοι εξακολουθούν να χρησιμοποιούν το παλιό όνομα στην καθημερινή κουβέντα, ενώ το επίσημο υπάρχει μόνο στις πινακίδες και στα έγγραφα. Για μένα, αυτά τα δύο ονόματα δεν είναι αντίπαλοι. Είναι δύο στρώματα της ίδιας ιστορίας, και αξίζει να καταγράψουμε τα παλιά πριν χαθούν μαζί με όσους τα θυμούνται.", "Not always, and not immediately. In many places older people still use the old name in everyday conversation, while the official one exists only on signs and in documents. For me these two names are not rivals. They are two layers of the same history, and it is worth recording the old ones before they are lost along with those who remember them."),
 ],
 "questions": [
  Q("Γιατί άλλαξαν τα ονόματα πολλών οικισμών;", ["Γιατί ήταν δύσκολα στην προφορά", "Γιατί το κράτος ήθελε να σβήσει ίχνη προηγούμενων εποχών και γλωσσών", "Γιατί το ζήτησαν οι κάτοικοι", "Λόγω συγχώνευσης χωριών"], 1, "το κράτος τα θεωρούσε υπόλειμμα μιας εποχής που ήθελε να αφήσει πίσω του"),
  Q("Πώς δημιουργήθηκε το όνομα Ασπρόβρυση, σύμφωνα με το παράδειγμα;", ["Από αρχαίο κείμενο", "Από το όνομα ενός αγίου", "Με μετάφραση του παλιού τουρκικού ονόματος", "Από έναν ήρωα της επανάστασης"], 2, "Κάποτε απλώς μετέφραζαν το παλιό όνομα: ένα χωριό που λεγόταν στα τουρκικά «άσπρη πηγή» έγινε Ασπρόβρυση."),
  Q("Τι παρατηρεί για τη χρήση των ονομάτων σήμερα;", ["Τα παλιά ονόματα έχουν ξεχαστεί εντελώς", "Οι νέοι προτιμούν τα παλιά ονόματα", "Τα παλιά ονόματα είναι πλέον τα επίσημα", "Συχνά οι ηλικιωμένοι λένε ακόμη το παλιό όνομα, ενώ το νέο είναι το επίσημο"], 3, "οι ηλικιωμένοι εξακολουθούν να χρησιμοποιούν το παλιό όνομα στην καθημερινή κουβέντα"),
  Q("Ποια είναι η στάση του ιστορικού;", ["Θεωρεί ότι πρέπει να επανέλθουν όλα τα παλιά ονόματα", "Βλέπει τα δύο ονόματα ως στρώματα της ίδιας ιστορίας και θέλει να καταγραφούν τα παλιά", "Πιστεύει ότι οι μετονομασίες ήταν απολύτως σωστές", "Δεν παίρνει θέση"], 1, "Είναι δύο στρώματα της ίδιας ιστορίας, και αξίζει να καταγράψουμε τα παλιά πριν χαθούν"),
 ],
 "gloss": {"μετονομασίες": "μετονομασία — renaming", "οικισμών": "οικισμός — settlement", "μετονομάστηκαν": "μετονομάζω — to rename", "προέλευσης": "προέλευση — origin", "υπόλειμμα": "υπόλειμμα — remnant", "κριτήριο": "κριτήριο — criterion", "αρμόδια": "αρμόδιος — responsible, competent", "γραμματεία": "γραμματεία — literature (of a period)", "αμφίβολη": "αμφίβολος — doubtful", "εξακολουθούν": "εξακολουθώ — to continue, still (do)", "αντίπαλοι": "αντίπαλος — rival, opponent", "στρώματα": "στρώμα — layer", "να καταγράψουμε": "καταγράφω — to record, document"},
})

ITEMS.append({
 "id": "l8-mon-varemara", "title": "Υπεράσπιση της βαρεμάρας", "title_en": "In defence of boredom", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε απόσπασμα από μια ραδιοφωνική εκπομπή, όπου μια δοκιμιογράφος μιλάει για την πλήξη.",
 "script": [
  L("Δοκιμιογράφος", "f", "Θυμάστε πότε βαρεθήκατε τελευταία φορά; Εννοώ πραγματικά βαρεθήκατε, χωρίς να βγάλετε αμέσως το κινητό από την τσέπη; Οι περισσότεροι δυσκολευόμαστε να απαντήσουμε. Γεμίζουμε κάθε κενό, στη στάση του λεωφορείου, στην ουρά του φούρνου, ακόμα και στα φανάρια, σαν να φοβόμαστε τη σιωπή του ίδιου μας του μυαλού.", "Do you remember when you were last bored? I mean really bored, without immediately taking your phone out of your pocket? Most of us find it hard to answer. We fill every gap, at the bus stop, in the queue at the bakery, even at traffic lights, as if we were afraid of the silence of our own minds."),
  L("Δοκιμιογράφος", "f", "Κι όμως, η πλήξη δεν είναι εχθρός. Είναι, θα έλεγα, ο προθάλαμος της φαντασίας. Τα παιδιά που βαριούνται ένα απόγευμα του Αυγούστου είναι συνήθως εκείνα που στο τέλος εφευρίσκουν ένα παιχνίδι, φτιάχνουν μια καλύβα ή γράφουν μια ιστορία. Η βαρεμάρα είναι μια μορφή δυσφορίας που μας σπρώχνει να αναζητήσουμε νόημα μόνοι μας, αντί να μας το σερβίρει κάποιος έτοιμο.", "And yet boredom is not an enemy. It is, I would say, the antechamber of imagination. Children who are bored on an August afternoon are usually the ones who end up inventing a game, building a hut or writing a story. Boredom is a form of discomfort that pushes us to look for meaning ourselves, instead of having it served to us ready-made."),
  L("Δοκιμιογράφος", "f", "Δεν υποστηρίζω, βέβαια, ότι πρέπει να πετάξουμε τις οθόνες μας. Υποστηρίζω κάτι πιο μετριοπαθές: να αφήνουμε, μέσα στη μέρα, μικρές νησίδες απραξίας. Δέκα λεπτά χωρίς ερέθισμα δεν είναι χαμένος χρόνος. Είναι ίσως ο μόνος χρόνος που ανήκει πραγματικά σε εμάς.", "I am not claiming, of course, that we should throw away our screens. I am claiming something more modest: that we leave small islands of idleness within the day. Ten minutes without stimulus is not lost time. It is perhaps the only time that truly belongs to us."),
 ],
 "questions": [
  Q("Τι παρατηρεί η ομιλήτρια για τη σύγχρονη συμπεριφορά;", ["Ότι βαριόμαστε περισσότερο από ποτέ", "Ότι γεμίζουμε κάθε κενό χρόνο για να μη μείνουμε με τις σκέψεις μας", "Ότι διαβάζουμε περισσότερα βιβλία", "Ότι τα παιδιά δεν παίζουν πια έξω"], 1, "Γεμίζουμε κάθε κενό ... σαν να φοβόμαστε τη σιωπή του ίδιου μας του μυαλού."),
  Q("Τι εννοεί λέγοντας ότι η πλήξη είναι «ο προθάλαμος της φαντασίας»;", ["Ότι η βαρεμάρα συχνά οδηγεί σε δημιουργικότητα", "Ότι η φαντασία είναι επικίνδυνη", "Ότι μόνο τα παιδιά έχουν φαντασία", "Ότι η πλήξη είναι αρρώστια"], 0, "Τα παιδιά που βαριούνται ... εφευρίσκουν ένα παιχνίδι, φτιάχνουν μια καλύβα ή γράφουν μια ιστορία."),
  Q("Ποια είναι η πρότασή της;", ["Να καταργηθούν τα κινητά", "Να μένουμε με τις ώρες χωρίς να κάνουμε τίποτα", "Να αφήνουμε μικρά διαστήματα της μέρας χωρίς ερεθίσματα", "Να δουλεύουμε λιγότερες ώρες"], 2, "να αφήνουμε, μέσα στη μέρα, μικρές νησίδες απραξίας"),
 ],
 "gloss": {"δοκιμιογράφος": "δοκιμιογράφος — essayist", "πλήξη": "πλήξη — boredom", "κενό": "κενό — gap, void", "φανάρια": "φανάρι — traffic light", "προθάλαμος": "προθάλαμος — antechamber, anteroom", "εφευρίσκουν": "εφευρίσκω — to invent", "καλύβα": "καλύβα — hut", "δυσφορίας": "δυσφορία — discomfort, unease", "μετριοπαθές": "μετριοπαθής — moderate", "νησίδες": "νησίδα — islet, (traffic) island", "απραξίας": "απραξία — inactivity, idleness", "ερέθισμα": "ερέθισμα — stimulus"},
})
rnd = random.Random(8)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-8.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
