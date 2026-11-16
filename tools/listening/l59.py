# Source for library/listening/listening-59.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l59.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l59-ann-planitario", "title": "Ανακοίνωση στο πλανητάριο", "title_en": "An announcement at the planetarium", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στην αίθουσα αναμονής ενός πλανηταρίου. Θα ακούσετε μια ανακοίνωση πριν από την έναρξη της προβολής.",
 "script": [
  L("Ανακοίνωση", "f", "Αγαπητοί επισκέπτες, καλώς ήρθατε στο πλανητάριο. Η προβολή «Ταξίδι στο ηλιακό σύστημα» θα ξεκινήσει σε δέκα λεπτά στον θόλο. Παρακαλούμε να έχετε μαζί σας το εισιτήριό σας, όπου αναγράφεται ο αριθμός της θέσης σας.", "Dear visitors, welcome to the planetarium. The show 'Journey through the solar system' will begin in ten minutes in the dome. Please have your ticket with you; it shows your seat number."),
  L("Ανακοίνωση", "f", "Σας υπενθυμίζουμε ότι μετά την έναρξη της προβολής η είσοδος δεν επιτρέπεται, γιατί το φως από την πόρτα χαλάει την εικόνα στον θόλο. Τα καθίσματα γέρνουν προς τα πίσω· για τη δική σας άνεση, μην ακουμπάτε τσάντες στα πόδια σας.", "We remind you that once the show has started no entry is allowed, because light from the door spoils the image on the dome. The seats tilt backwards; for your comfort, don't rest bags at your feet."),
  L("Ανακοίνωση", "f", "Η προβολή διαρκεί σαράντα πέντε λεπτά και δεν συνιστάται για παιδιά κάτω των πέντε ετών. Στο τέλος, ένας αστρονόμος θα απαντήσει σε ερωτήσεις του κοινού. Η χρήση κινητών τηλεφώνων και η φωτογράφιση απαγορεύονται.", "The show lasts forty-five minutes and is not recommended for children under five. At the end, an astronomer will answer questions from the audience. Using mobile phones and taking photographs are forbidden."),
 ],
 "questions": [
  Q("Γιατί δεν επιτρέπεται η είσοδος μετά την έναρξη;", ["Γιατί δεν υπάρχουν άλλες θέσεις", "Γιατί το φως από την πόρτα χαλάει την εικόνα στον θόλο", "Γιατί ενοχλεί τον αστρονόμο", "Για λόγους ασφαλείας"], 1, "γιατί το φως από την πόρτα χαλάει την εικόνα στον θόλο"),
  Q("Για ποιους δεν συνιστάται η προβολή;", ["Για ηλικιωμένους", "Για παιδιά κάτω των πέντε ετών", "Για άτομα με προβλήματα όρασης", "Για ομάδες σχολείων"], 1, "δεν συνιστάται για παιδιά κάτω των πέντε ετών"),
  Q("Τι θα γίνει στο τέλος της προβολής;", ["Θα δοθούν δώρα", "Ένας αστρονόμος θα απαντήσει σε ερωτήσεις", "Θα ακολουθήσει δεύτερη προβολή", "Θα γίνει παρατήρηση με τηλεσκόπιο"], 1, "ένας αστρονόμος θα απαντήσει σε ερωτήσεις του κοινού"),
 ],
 "gloss": {"πλανητάριο": "πλανητάριο — planetarium", "προβολή": "προβολή — show, screening", "θόλο": "θόλος — dome", "αναγράφεται": "αναγράφομαι — to be written, shown", "γέρνουν": "γέρνω — to tilt, lean", "άνεση": "άνεση — comfort", "συνιστάται": "συνιστάται — it is recommended", "φωτογράφιση": "φωτογράφιση — taking photographs"},
})

ITEMS.append({
 "id": "l59-vm-orologopoios", "title": "Μήνυμα από τον ωρολογοποιό", "title_en": "A message from the watchmaker", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε αφήσει ένα παλιό ρολόι για επισκευή. Θα ακούσετε ένα μήνυμα από τον ωρολογοποιό στον τηλεφωνητή σας.",
 "script": [
  L("Ωρολογοποιός", "m", "Καλημέρα σας, ο Μιλτιάδης είμαι, από το ωρολογοποιείο της οδού Ερμού. Σας τηλεφωνώ για το ρολόι τσέπης του παππού σας. Το άνοιξα και είδα ότι το πρόβλημα δεν είναι μόνο το ελατήριο, όπως νομίζαμε. Έχει σπάσει κι ένα γρανάζι, και πρέπει να παραγγείλω ανταλλακτικό από την Ελβετία.", "Good morning, it's Miltiadis, from the watchmaker's on Ermou Street. I'm calling about your grandfather's pocket watch. I opened it and saw that the problem isn't only the spring, as we thought. A gear wheel has also broken, and I have to order a spare part from Switzerland."),
  L("Ωρολογοποιός", "m", "Αυτό σημαίνει ότι το κόστος θα είναι περίπου εκατόν είκοσι ευρώ αντί για εξήντα, και ότι θα χρειαστούν τρεις με τέσσερις εβδομάδες. Δεν θέλω να προχωρήσω χωρίς τη σύμφωνη γνώμη σας.", "That means the cost will be about one hundred and twenty euros instead of sixty, and that it will take three to four weeks. I don't want to go ahead without your agreement."),
  L("Ωρολογοποιός", "m", "Είναι πολύ ωραίο κομμάτι, αξίζει τον κόπο, κατά τη γνώμη μου. Πείτε μου τι αποφασίζετε. Είμαι στο μαγαζί ως τις δύο.", "It's a very fine piece; in my opinion it's worth the trouble. Let me know what you decide. I'm in the shop until two."),
 ],
 "questions": [
  Q("Τι ανακάλυψε ο ωρολογοποιός;", ["Ότι το ρολόι είναι ψεύτικο", "Ότι έχει σπάσει κι ένα γρανάζι", "Ότι λείπει το καπάκι", "Ότι το ρολόι δουλεύει κανονικά"], 1, "Έχει σπάσει κι ένα γρανάζι"),
  Q("Πόσο θα κοστίσει περίπου η επισκευή;", ["Εξήντα ευρώ", "Εκατόν είκοσι ευρώ", "Διακόσια ευρώ", "Είκοσι ευρώ"], 1, "το κόστος θα είναι περίπου εκατόν είκοσι ευρώ αντί για εξήντα"),
  Q("Τι ζητάει από τον πελάτη;", ["Να πληρώσει προκαταβολή", "Να του πει αν θέλει να προχωρήσει", "Να φέρει το ρολόι ξανά", "Να βρει το ανταλλακτικό μόνος του"], 1, "Δεν θέλω να προχωρήσω χωρίς τη σύμφωνη γνώμη σας"),
 ],
 "gloss": {"ωρολογοποιείο": "ωρολογοποιείο — watchmaker's shop", "ρολόι τσέπης": "ρολόι τσέπης — pocket watch", "ελατήριο": "ελατήριο — spring", "γρανάζι": "γρανάζι — gear wheel", "ανταλλακτικό": "ανταλλακτικό — spare part", "σύμφωνη γνώμη": "σύμφωνη γνώμη — agreement, consent", "αξίζει τον κόπο": "αξίζει τον κόπο — it is worth the trouble"},
})

ITEMS.append({
 "id": "l59-dia-magio", "title": "Ένα μαγιό για το καλοκαίρι", "title_en": "A swimsuit for the summer", "type": "dialogue", "level": "B2",
 "context_el": "Ένας άντρας ψάχνει μαγιό σε ένα κατάστημα αθλητικών ειδών. Θα ακούσετε τη συζήτησή του με την πωλήτρια.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Ψάχνω ένα μαγιό για κολύμβηση σε πισίνα. Έγραψα τον γιο μου σε ένα τμήμα κολύμβησης και αποφάσισα να ξεκινήσω κι εγώ.", "Good morning. I'm looking for swimming trunks for the pool. I've enrolled my son in a swimming class and decided to start myself too."),
  L("Πωλήτρια", "f", "Μπράβο σας! Για την πισίνα σάς προτείνω ένα εφαρμοστό μαγιό, όχι βερμούδα, γιατί η βερμούδα γεμίζει νερό και σας κουράζει. Επίσης, τα μαγιό από ειδικό ύφασμα αντέχουν περισσότερο στο χλώριο.", "Well done! For the pool I'd suggest close-fitting trunks, not board shorts, because board shorts fill with water and tire you. Also, swimwear made of special fabric lasts longer in chlorine."),
  L("Πελάτης", "m", "Δεν ήξερα ότι το χλώριο καταστρέφει τα ρούχα. Και τι νούμερο θα χρειαστώ; Συνήθως φοράω μέτριο.", "I didn't know chlorine ruins clothes. And what size will I need? I usually wear medium."),
  L("Πωλήτρια", "f", "Στα εφαρμοστά καλύτερα να το δοκιμάσετε, γιατί κάθε μάρκα έχει διαφορετικά νούμερα. Τα δοκιμαστήρια είναι εκεί αριστερά. Σας θυμίζω μόνο ότι τα μαγιό τα δοκιμάζουμε πάνω από το εσώρουχο, για λόγους υγιεινής.", "With close-fitting ones it's better to try them on, because every brand has different sizes. The fitting rooms are over there on the left. I'd just remind you that swimwear is tried on over underwear, for reasons of hygiene."),
  L("Πελάτης", "m", "Βεβαίως. Χρειάζομαι και σκουφάκι και γυαλάκια. Υπάρχει κάποια προσφορά;", "Of course. I also need a cap and goggles. Is there an offer?"),
  L("Πωλήτρια", "f", "Ναι, αν πάρετε και τα τρία, έχετε είκοσι τοις εκατό έκπτωση στο σύνολο.", "Yes, if you take all three, you get twenty per cent off the total."),
 ],
 "questions": [
  Q("Γιατί δεν του προτείνει βερμούδα η πωλήτρια;", ["Γιατί είναι ακριβή", "Γιατί γεμίζει νερό και τον κουράζει", "Γιατί δεν επιτρέπεται στην πισίνα", "Γιατί δεν έχει το νούμερό του"], 1, "η βερμούδα γεμίζει νερό και σας κουράζει"),
  Q("Γιατί πρέπει να δοκιμάσει το μαγιό;", ["Γιατί δεν γίνονται επιστροφές", "Γιατί κάθε μάρκα έχει διαφορετικά νούμερα", "Γιατί είναι από ειδικό ύφασμα", "Γιατί άλλαξε το νούμερό του"], 1, "κάθε μάρκα έχει διαφορετικά νούμερα"),
  Q("Ποια είναι η προσφορά;", ["Ένα δωρεάν σκουφάκι", "Είκοσι τοις εκατό έκπτωση αν πάρει και τα τρία", "Δύο μαγιό στην τιμή του ενός", "Δωρεάν γυαλάκια"], 1, "αν πάρετε και τα τρία, έχετε είκοσι τοις εκατό έκπτωση στο σύνολο"),
 ],
 "gloss": {"μαγιό": "μαγιό — swimsuit, trunks", "εφαρμοστό": "εφαρμοστός — close-fitting", "βερμούδα": "βερμούδα — board shorts", "χλώριο": "χλώριο — chlorine", "νούμερο": "νούμερο — size", "δοκιμαστήρια": "δοκιμαστήριο — fitting room", "εσώρουχο": "εσώρουχο — underwear", "υγιεινής": "υγιεινή — hygiene"},
})

ITEMS.append({
 "id": "l59-dia-skafos", "title": "Ενοικίαση σκάφους χωρίς δίπλωμα", "title_en": "Renting a boat without a licence", "type": "dialogue", "level": "B2",
 "context_el": "Μια παρέα θέλει να νοικιάσει ένα μικρό σκάφος σε ένα νησί. Θα ακούσετε τη συζήτηση ενός από τους φίλους με τον υπάλληλο.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Θα θέλαμε να νοικιάσουμε ένα σκάφος για αύριο, για να πάμε στις παραλίες της νότιας πλευράς. Κανείς μας δεν έχει δίπλωμα, όμως. Γίνεται;", "Good morning. We'd like to rent a boat for tomorrow, to go to the beaches on the south side. None of us has a licence, though. Is that possible?"),
  L("Υπάλληλος", "m", "Γίνεται. Έχουμε φουσκωτά με μηχανή μέχρι τριάντα ίππους, που δεν απαιτούν δίπλωμα. Χωράνε μέχρι πέντε άτομα. Πριν φύγετε, θα σας κάνω μια σύντομη εκπαίδευση, μισή ώρα περίπου, και θα σας δείξω στον χάρτη πού επιτρέπεται να πάτε.", "It is. We have inflatables with an engine of up to thirty horsepower, which don't require a licence. They hold up to five people. Before you leave, I'll give you a short training session, about half an hour, and show you on the map where you're allowed to go."),
  L("Πελάτισσα", "f", "Τέλεια. Πόσο κοστίζει η μέρα; Και τα καύσιμα;", "Perfect. How much is it per day? And the fuel?"),
  L("Υπάλληλος", "m", "Ογδόντα ευρώ τη μέρα, από τις εννιά ως τις έξι. Τα καύσιμα πληρώνονται χωριστά, ανάλογα με την κατανάλωση. Θα σας ζητήσω και την ταυτότητα ενός από εσάς ως εγγύηση.", "Eighty euros a day, from nine to six. Fuel is paid separately, according to consumption. I'll also ask for one of your ID cards as a deposit."),
  L("Πελάτισσα", "f", "Και αν χαλάσει ο καιρός;", "And if the weather turns bad?"),
  L("Υπάλληλος", "m", "Αν τα μποφόρ ξεπεράσουν τα πέντε, δεν βγαίνει κανένα σκάφος, και σας επιστρέφουμε τα χρήματα ή αλλάζουμε μέρα. Και στη θάλασσα, αν δείτε ότι σηκώνεται αέρας, γυρίζετε αμέσως. Με τη θάλασσα δεν παίζουμε.", "If the wind goes above force five, no boat goes out, and we refund your money or change the day. And at sea, if you see the wind getting up, you come back at once. You don't play games with the sea."),
 ],
 "questions": [
  Q("Τι είδους σκάφος μπορούν να νοικιάσουν χωρίς δίπλωμα;", ["Ένα ιστιοπλοϊκό", "Ένα φουσκωτό με μηχανή μέχρι τριάντα ίππους", "Ένα ταχύπλοο", "Ένα καΐκι με καπετάνιο"], 1, "Έχουμε φουσκωτά με μηχανή μέχρι τριάντα ίππους, που δεν απαιτούν δίπλωμα"),
  Q("Τι θα γίνει πριν φύγουν;", ["Θα πληρώσουν τα καύσιμα", "Θα κάνουν μια σύντομη εκπαίδευση", "Θα υπογράψουν ασφάλεια", "Θα περιμένουν τον καπετάνιο"], 1, "θα σας κάνω μια σύντομη εκπαίδευση, μισή ώρα περίπου"),
  Q("Τι γίνεται αν τα μποφόρ ξεπεράσουν τα πέντε;", ["Πληρώνουν διπλά", "Δεν βγαίνει κανένα σκάφος και παίρνουν πίσω τα χρήματα ή αλλάζουν μέρα", "Πρέπει να μείνουν κοντά στο λιμάνι", "Τους δίνουν μεγαλύτερο σκάφος"], 1, "δεν βγαίνει κανένα σκάφος, και σας επιστρέφουμε τα χρήματα ή αλλάζουμε μέρα"),
 ],
 "gloss": {"σκάφος": "σκάφος — boat", "δίπλωμα": "δίπλωμα — licence", "φουσκωτά": "φουσκωτό — inflatable boat", "ίππους": "ίππος — horsepower", "καύσιμα": "καύσιμα — fuel", "κατανάλωση": "κατανάλωση — consumption", "εγγύηση": "εγγύηση — deposit, guarantee", "μποφόρ": "μποφόρ — Beaufort (wind force)"},
})

ITEMS.append({
 "id": "l59-int-mageiras-ploiou", "title": "Ο μάγειρας του φορτηγού πλοίου", "title_en": "The cook on a cargo ship", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για τη ζωή των ναυτικών, η δημοσιογράφος μιλά με έναν μάγειρα που δούλεψε τριάντα χρόνια σε φορτηγά πλοία.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Μανώλη, πώς είναι να μαγειρεύεις για ένα πλήρωμα στη μέση του ωκεανού;", "Mr Manolis, what's it like to cook for a crew in the middle of the ocean?"),
  L("Μάγειρας", "m", "Είναι η πιο υπεύθυνη δουλειά στο πλοίο, κατά τη γνώμη μου, μετά τον καπετάνιο. Τα ταξίδια κρατούν μήνες, και το φαγητό είναι η μόνη χαρά της μέρας. Αν το φαγητό είναι κακό, πέφτει το ηθικό όλου του πληρώματος. Πρέπει να προγραμματίζεις τα τρόφιμα για εβδομάδες, γιατί στη μέση του Ατλαντικού δεν υπάρχει σούπερ μάρκετ.", "It's the most responsible job on the ship, in my view, after the captain's. Voyages last months, and food is the only joy of the day. If the food is bad, the whole crew's morale drops. You have to plan the provisions for weeks, because in the middle of the Atlantic there's no supermarket."),
  L("Δημοσιογράφος", "f", "Τα πληρώματα είναι συνήθως πολυεθνικά. Πώς τα καταφέρνατε με τις διαφορετικές κουζίνες;", "Crews are usually multinational. How did you manage with the different cuisines?"),
  L("Μάγειρας", "m", "Αυτό ήταν το πιο ενδιαφέρον. Είχα Φιλιππινέζους, Ινδούς, Ουκρανούς. Έμαθα από αυτούς να φτιάχνω το αδόμπο και το κάρι, κι εγώ τους μάθαινα μουσακά και φασολάδα. Την Κυριακή κάναμε πάντα κάτι γιορτινό, ό,τι κι αν γινόταν.", "That was the most interesting part. I had Filipinos, Indians, Ukrainians. I learned from them to make adobo and curry, and I taught them moussaka and bean soup. On Sundays we always made something festive, whatever happened."),
  L("Δημοσιογράφος", "f", "Και με τη φουρτούνα;", "And in rough seas?"),
  L("Μάγειρας", "m", "Τότε ξεχνάς τις συνταγές. Δένεις τις κατσαρόλες στη φωτιά με ειδικές μπάρες και φτιάχνεις κάτι απλό, σούπα ή σάντουιτς. Μια φορά, σε μια καταιγίδα στον Βισκαϊκό, μια ολόκληρη κατσαρόλα με φακές προσγειώθηκε στο ταβάνι!", "Then you forget the recipes. You fix the pots to the stove with special bars and make something simple, soup or sandwiches. Once, in a storm in the Bay of Biscay, a whole pot of lentils landed on the ceiling!"),
 ],
 "questions": [
  Q("Γιατί θεωρεί τη δουλειά του τόσο υπεύθυνη;", ["Γιατί κοστίζει πολλά χρήματα", "Γιατί το φαγητό είναι η μόνη χαρά της μέρας και επηρεάζει το ηθικό του πληρώματος", "Γιατί είναι επικίνδυνη", "Γιατί δουλεύει μόνος του"], 1, "Αν το φαγητό είναι κακό, πέφτει το ηθικό όλου του πληρώματος"),
  Q("Τι έκανε με τις διαφορετικές κουζίνες;", ["Μαγείρευε μόνο ελληνικά φαγητά", "Αντάλλασσε συνταγές με τα μέλη του πληρώματος", "Άφηνε τον καθένα να μαγειρεύει μόνος του", "Αγόραζε έτοιμα φαγητά"], 1, "Έμαθα από αυτούς να φτιάχνω το αδόμπο και το κάρι, κι εγώ τους μάθαινα μουσακά και φασολάδα"),
  Q("Τι κάνει όταν έχει φουρτούνα;", ["Δεν μαγειρεύει καθόλου", "Δένει τις κατσαρόλες και φτιάχνει κάτι απλό", "Μαγειρεύει στο κατάστρωμα", "Σερβίρει μόνο φρούτα"], 1, "Δένεις τις κατσαρόλες στη φωτιά με ειδικές μπάρες και φτιάχνεις κάτι απλό"),
 ],
 "gloss": {"πλήρωμα": "πλήρωμα — crew", "ηθικό": "ηθικό — morale", "τρόφιμα": "τρόφιμα — provisions, food supplies", "πολυεθνικά": "πολυεθνικός — multinational", "γιορτινό": "γιορτινός — festive", "φουρτούνα": "φουρτούνα — rough sea, storm", "καταιγίδα": "καταιγίδα — storm", "προσγειώθηκε": "προσγειώνομαι — to land"},
})

ITEMS.append({
 "id": "l59-rep-geraki", "title": "Το Γεράκι της Λακωνίας", "title_en": "Geraki in Laconia", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από ένα λιγότερο γνωστό βυζαντινό μνημείο της Πελοποννήσου.",
 "script": [
  L("Ρεπόρτερ", "f", "Λίγοι από τους επισκέπτες του Μυστρά ξέρουν ότι μόλις σαράντα χιλιόμετρα ανατολικά βρίσκεται ένας άλλος, σχεδόν άγνωστος θησαυρός: το Γεράκι. Πάνω σε έναν λόφο, πάνω από το σημερινό χωριό, υψώνεται το κάστρο που έχτισαν οι Φράγκοι τον δέκατο τρίτο αιώνα, όταν κατέλαβαν την Πελοπόννησο.", "Few visitors to Mystras know that just forty kilometres to the east lies another, almost unknown treasure: Geraki. On a hill above the present-day village rises the castle the Franks built in the thirteenth century, when they conquered the Peloponnese."),
  L("Ρεπόρτερ", "f", "Η μεγάλη έκπληξη, όμως, είναι οι εκκλησίες. Μέσα στο κάστρο, στους πρόποδες του λόφου και γύρω από το χωριό, σώζονται δεκάδες μικρές βυζαντινές εκκλησίες, πολλές με τοιχογραφίες σε εντυπωσιακά καλή κατάσταση. Κάποιες είναι κλειδωμένες, αλλά ο φύλακας του αρχαιολογικού χώρου ανοίγει κατόπιν συνεννόησης.", "The big surprise, though, is the churches. Inside the castle, at the foot of the hill and around the village, dozens of small Byzantine churches survive, many with frescoes in remarkably good condition. Some are locked, but the site guard opens them by arrangement."),
  L("Ρεπόρτερ", "f", "Ο χώρος είναι ανοιχτός μόνο το πρωί, και η ανάβαση γίνεται από ένα απότομο μονοπάτι, οπότε χρειάζονται κλειστά παπούτσια και νερό. Από ψηλά, η θέα απλώνεται ως τον Ταΰγετο και τον Πάρνωνα. Εδώ δεν θα βρείτε πλήθη τουριστών, μόνο σιωπή και ιστορία.", "The site is open only in the morning, and the climb is up a steep path, so you need closed shoes and water. From the top, the view stretches to Taygetus and Parnon. Here you won't find crowds of tourists, only silence and history."),
 ],
 "questions": [
  Q("Ποιοι έχτισαν το κάστρο του Γερακίου;", ["Οι Βυζαντινοί", "Οι Φράγκοι", "Οι Βενετοί", "Οι Οθωμανοί"], 1, "το κάστρο που έχτισαν οι Φράγκοι τον δέκατο τρίτο αιώνα"),
  Q("Ποια είναι η μεγάλη έκπληξη του Γερακίου;", ["Το μουσείο", "Οι δεκάδες βυζαντινές εκκλησίες με τοιχογραφίες", "Ένα αρχαίο θέατρο", "Μια σπηλιά"], 1, "σώζονται δεκάδες μικρές βυζαντινές εκκλησίες, πολλές με τοιχογραφίες"),
  Q("Τι συμβουλεύει η ρεπόρτερ τους επισκέπτες;", ["Να πάνε το απόγευμα", "Να φορούν κλειστά παπούτσια και να έχουν νερό", "Να κλείσουν ξενάγηση", "Να πάνε με αυτοκίνητο ως την κορυφή"], 1, "χρειάζονται κλειστά παπούτσια και νερό"),
 ],
 "gloss": {"θησαυρός": "θησαυρός — treasure", "υψώνεται": "υψώνομαι — to rise", "κατέλαβαν": "καταλαμβάνω — to conquer, occupy", "πρόποδες": "πρόποδες — foot (of a hill)", "τοιχογραφίες": "τοιχογραφία — fresco", "κατόπιν συνεννόησης": "κατόπιν συνεννόησης — by arrangement", "απότομο": "απότομος — steep", "πλήθη": "πλήθος — crowd"},
})

ITEMS.append({
 "id": "l59-dia-plexi", "title": "Μαθήματα πλεξίματος", "title_en": "Knitting lessons", "type": "dialogue", "level": "B2",
 "context_el": "Ένας νεαρός άντρας ρωτά για ένα εργαστήρι πλεξίματος σε ένα κατάστημα με μαλλιά. Θα ακούσετε τη συζήτησή του με την ιδιοκτήτρια.",
 "script": [
  L("Πάνος", "m", "Καλησπέρα. Είδα στη βιτρίνα ότι κάνετε μαθήματα πλεξίματος. Δέχεστε και άντρες;", "Good evening. I saw in the window that you do knitting lessons. Do you accept men too?"),
  L("Ιδιοκτήτρια", "f", "Φυσικά! Στο τμήμα της Τετάρτης έχουμε ήδη δύο άντρες. Παλιά στα νησιά οι ψαράδες έπλεκαν οι ίδιοι τα δίχτυα και τα πουλόβερ τους. Το πλέξιμο δεν είναι μόνο γυναικεία υπόθεση.", "Of course! In the Wednesday class we already have two men. In the old days on the islands fishermen knitted their own nets and sweaters. Knitting isn't just a women's thing."),
  L("Πάνος", "m", "Χαίρομαι που το ακούω. Ο ψυχολόγος μου μού πρότεινε να βρω μια δραστηριότητα με τα χέρια, για να χαλαρώνω μετά τη δουλειά. Δουλεύω όλη μέρα μπροστά σε οθόνη.", "I'm glad to hear it. My psychologist suggested I find an activity with my hands, to relax after work. I work in front of a screen all day."),
  L("Ιδιοκτήτρια", "f", "Έχει δίκιο. Πολλοί μαθητές μου λένε ότι το πλέξιμο είναι σαν διαλογισμός: μετράς τους πόντους, και το μυαλό ησυχάζει. Τα μαθήματα είναι οκτώ, μία φορά την εβδομάδα, και στο τέλος θα έχετε φτιάξει ένα κασκόλ.", "She's right. Many of my students tell me that knitting is like meditation: you count the stitches and your mind calms down. There are eight lessons, once a week, and at the end you'll have made a scarf."),
  L("Πάνος", "m", "Τι χρειάζεται να φέρω;", "What do I need to bring?"),
  L("Ιδιοκτήτρια", "f", "Τίποτα. Τις βελόνες και το πρώτο κουβάρι τα δίνουμε εμείς, μαζί με το δίδακτρο. Σας συμβουλεύω μόνο να διαλέξετε ένα ανοιχτό χρώμα, γιατί στα σκούρα μαλλιά δεν φαίνονται καλά οι πόντοι στην αρχή.", "Nothing. We provide the needles and the first ball of wool, with the fee. I'd only advise you to choose a light colour, because on dark wool the stitches don't show well at first."),
 ],
 "questions": [
  Q("Γιατί θέλει ο Πάνος να μάθει πλέξιμο;", ["Για να κάνει δώρα", "Για να χαλαρώνει μετά τη δουλειά, όπως του πρότεινε ο ψυχολόγος του", "Για να ανοίξει μαγαζί", "Γιατί του το ζήτησε η γιαγιά του"], 1, "Ο ψυχολόγος μου μού πρότεινε να βρω μια δραστηριότητα με τα χέρια, για να χαλαρώνω"),
  Q("Τι θα έχει φτιάξει στο τέλος των μαθημάτων;", ["Ένα πουλόβερ", "Ένα κασκόλ", "Ένα σκουφάκι", "Ένα δίχτυ"], 1, "στο τέλος θα έχετε φτιάξει ένα κασκόλ"),
  Q("Γιατί του συμβουλεύει να διαλέξει ανοιχτό χρώμα;", ["Γιατί είναι φθηνότερο", "Γιατί στα σκούρα μαλλιά δεν φαίνονται καλά οι πόντοι στην αρχή", "Γιατί είναι της μόδας", "Γιατί τα σκούρα έχουν τελειώσει"], 1, "στα σκούρα μαλλιά δεν φαίνονται καλά οι πόντοι στην αρχή"),
 ],
 "gloss": {"πλεξίματος": "πλέξιμο — knitting", "έπλεκαν": "πλέκω — to knit", "δίχτυα": "δίχτυ — net", "διαλογισμός": "διαλογισμός — meditation", "πόντους": "πόντος — stitch", "κασκόλ": "κασκόλ — scarf", "βελόνες": "βελόνα — (knitting) needle", "κουβάρι": "κουβάρι — ball of wool", "δίδακτρο": "δίδακτρα — fee (for lessons)"},
})

ITEMS.append({
 "id": "l59-mono-zachari", "title": "Ένας μήνας χωρίς ζάχαρη", "title_en": "A month without sugar", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλά σε ένα πόντκαστ για μια πρόκληση που έθεσε στον εαυτό της.",
 "script": [
  L("Ομιλήτρια", "f", "Τον περασμένο Ιανουάριο, μετά τις γιορτές, αποφάσισα να περάσω έναν ολόκληρο μήνα χωρίς πρόσθετη ζάχαρη. Όχι γλυκά, όχι αναψυκτικά, ούτε καν ζάχαρη στον καφέ. Νόμιζα ότι θα ήταν εύκολο, αφού δεν θεωρούσα τον εαυτό μου λιχούδη.", "Last January, after the holidays, I decided to spend a whole month without added sugar. No sweets, no soft drinks, not even sugar in my coffee. I thought it would be easy, since I didn't consider myself to have a sweet tooth."),
  L("Ομιλήτρια", "f", "Η πρώτη έκπληξη ήταν πόσα προϊόντα περιέχουν ζάχαρη: το ψωμί του τοστ, οι σάλτσες, ακόμη και τα «υγιεινά» δημητριακά. Άρχισα να διαβάζω τις ετικέτες στο σούπερ μάρκετ και έμενα με το στόμα ανοιχτό. Την πρώτη εβδομάδα είχα πονοκεφάλους και ήμουν νευρική, ιδίως το απόγευμα.", "The first surprise was how many products contain sugar: sandwich bread, sauces, even 'healthy' cereals. I started reading the labels in the supermarket and was left open-mouthed. In the first week I had headaches and was irritable, especially in the afternoon."),
  L("Ομιλήτρια", "f", "Μετά τη δεύτερη εβδομάδα, όμως, κάτι άλλαξε. Κοιμόμουν καλύτερα, είχα περισσότερη ενέργεια, και τα φρούτα μου φαίνονταν πιο γλυκά από ποτέ. Σήμερα τρώω πάλι γλυκό, αλλά σπάνια και συνειδητά. Το μεγαλύτερο κέρδος δεν ήταν τα κιλά που έχασα, αλλά ότι ξανάμαθα να γεύομαι.", "After the second week, though, something changed. I slept better, had more energy, and fruit seemed sweeter than ever. Today I eat sweets again, but rarely and consciously. The biggest gain wasn't the kilos I lost, but that I learned to taste again."),
 ],
 "questions": [
  Q("Τι ήταν η πρώτη έκπληξη για την ομιλήτρια;", ["Ότι δεν της έλειπαν τα γλυκά", "Πόσα προϊόντα περιέχουν ζάχαρη", "Ότι έχασε πολλά κιλά", "Ότι ο καφές χωρίς ζάχαρη είναι νόστιμος"], 1, "Η πρώτη έκπληξη ήταν πόσα προϊόντα περιέχουν ζάχαρη"),
  Q("Πώς ένιωθε την πρώτη εβδομάδα;", ["Είχε περισσότερη ενέργεια", "Είχε πονοκεφάλους και ήταν νευρική", "Κοιμόταν καλύτερα", "Δεν ένιωθε καμία διαφορά"], 1, "Την πρώτη εβδομάδα είχα πονοκεφάλους και ήμουν νευρική"),
  Q("Ποιο ήταν, κατά την ίδια, το μεγαλύτερο κέρδος;", ["Τα κιλά που έχασε", "Ότι ξανάμαθε να γεύεται", "Ότι εξοικονόμησε χρήματα", "Ότι σταμάτησε τον καφέ"], 1, "Το μεγαλύτερο κέρδος δεν ήταν τα κιλά που έχασα, αλλά ότι ξανάμαθα να γεύομαι"),
 ],
 "gloss": {"πρόσθετη": "πρόσθετος — added", "αναψυκτικά": "αναψυκτικό — soft drink", "λιχούδη": "λιχούδης — person with a sweet tooth", "δημητριακά": "δημητριακά — cereals", "ετικέτες": "ετικέτα — label", "νευρική": "νευρικός — irritable, nervous", "συνειδητά": "συνειδητά — consciously", "γεύομαι": "γεύομαι — to taste"},
})

ITEMS.append({
 "id": "l59-c1-proforiki-istoria", "title": "Η προφορική ιστορία", "title_en": "Oral history", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την ιστορία, ο δημοσιογράφος συζητά με μια ιστορικό που συγκεντρώνει μαρτυρίες ηλικιωμένων.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αθανασίου, τι ακριβώς είναι η προφορική ιστορία;", "Ms Athanasiou, what exactly is oral history?"),
  L("Ιστορικός", "f", "Είναι η καταγραφή του παρελθόντος μέσα από τις αφηγήσεις των ανθρώπων που το έζησαν. Ηχογραφούμε συνεντεύξεις, συνήθως με ηλικιωμένους, για γεγονότα όπως η Κατοχή, ο Εμφύλιος ή η εσωτερική μετανάστευση. Τα γραπτά αρχεία μάς λένε τι αποφάσισαν οι κυβερνήσεις· οι προφορικές μαρτυρίες μάς λένε πώς το βίωσαν οι απλοί άνθρωποι, μια μάνα στο χωριό ή ένας εργάτης στο λιμάνι.", "It's recording the past through the accounts of the people who lived it. We record interviews, usually with older people, about events such as the Occupation, the Civil War or internal migration. Written archives tell us what governments decided; oral testimonies tell us how ordinary people experienced it, a mother in a village or a worker at the port."),
  L("Δημοσιογράφος", "m", "Η μνήμη, όμως, δεν είναι αναξιόπιστη; Οι άνθρωποι ξεχνούν, ωραιοποιούν…", "But isn't memory unreliable? People forget, embellish…"),
  L("Ιστορικός", "f", "Ασφαλώς, και αυτό δεν το κρύβουμε. Η μνήμη είναι επιλεκτική και επηρεάζεται από όσα ακολούθησαν, ακόμη και από όσα είδε κανείς αργότερα στην τηλεόραση. Γι’ αυτό διασταυρώνουμε τις μαρτυρίες μεταξύ τους και με τα γραπτά τεκμήρια. Όμως και τα λάθη έχουν αξία: όταν ένας ηλικιωμένος θυμάται ένα γεγονός διαφορετικά από ό,τι έγινε, μας αποκαλύπτει πώς η κοινότητά του το ερμήνευσε και το ενέταξε στη συλλογική της μνήμη.", "Of course, and we don't hide it. Memory is selective and influenced by what came later, even by what one saw later on television. That's why we cross-check testimonies against each other and against written evidence. But mistakes have value too: when an older person remembers an event differently from what happened, they reveal how their community interpreted it and fitted it into its collective memory."),
  L("Δημοσιογράφος", "m", "Υπάρχει κάποια επείγουσα διάσταση σε αυτή τη δουλειά;", "Is there an urgent dimension to this work?"),
  L("Ιστορικός", "f", "Απολύτως. Η γενιά που έζησε την Κατοχή σβήνει. Κάθε φορά που πεθαίνει ένας από αυτούς τους ανθρώπους, χάνεται μια ολόκληρη βιβλιοθήκη. Γι’ αυτό ενθαρρύνουμε και τους νέους να ηχογραφούν τους παππούδες τους. Δεν χρειάζεται εξειδικευμένος εξοπλισμός· ένα κινητό και, κυρίως, υπομονή και διάθεση για ακρόαση αρκούν.", "Absolutely. The generation that lived through the Occupation is disappearing. Every time one of these people dies, a whole library is lost. That's why we also encourage young people to record their grandparents. No specialist equipment is needed; a mobile phone and, above all, patience and a willingness to listen are enough."),
 ],
 "questions": [
  Q("Τι προσφέρουν οι προφορικές μαρτυρίες σε σχέση με τα γραπτά αρχεία;", ["Ακριβέστερες ημερομηνίες", "Το πώς βίωσαν τα γεγονότα οι απλοί άνθρωποι", "Τις αποφάσεις των κυβερνήσεων", "Στατιστικά στοιχεία"], 1, "οι προφορικές μαρτυρίες μάς λένε πώς το βίωσαν οι απλοί άνθρωποι"),
  Q("Πώς αντιμετωπίζουν οι ιστορικοί το πρόβλημα της αναξιόπιστης μνήμης;", ["Αγνοούν τις μαρτυρίες με λάθη", "Διασταυρώνουν τις μαρτυρίες μεταξύ τους και με γραπτά τεκμήρια", "Ηχογραφούν μόνο νέους ανθρώπους", "Ζητούν από τους μάρτυρες να γράψουν τις αναμνήσεις τους"], 1, "διασταυρώνουμε τις μαρτυρίες μεταξύ τους και με τα γραπτά τεκμήρια"),
  Q("Γιατί, κατά την ιστορικό, έχουν αξία και τα λάθη της μνήμης;", ["Γιατί διασκεδάζουν το κοινό", "Γιατί αποκαλύπτουν πώς η κοινότητα ερμήνευσε ένα γεγονός", "Γιατί διορθώνουν τα γραπτά αρχεία", "Γιατί δείχνουν ποιος λέει ψέματα"], 1, "μας αποκαλύπτει πώς η κοινότητά του το ερμήνευσε και το ενέταξε στη συλλογική της μνήμη"),
  Q("Τι ενθαρρύνει τους νέους να κάνουν;", ["Να σπουδάσουν ιστορία", "Να ηχογραφούν τους παππούδες τους", "Να γράφουν βιβλία", "Να επισκέπτονται αρχεία"], 1, "ενθαρρύνουμε και τους νέους να ηχογραφούν τους παππούδες τους"),
 ],
 "gloss": {"καταγραφή": "καταγραφή — recording, documentation", "αφηγήσεις": "αφήγηση — account, narrative", "μαρτυρίες": "μαρτυρία — testimony", "βίωσαν": "βιώνω — to experience", "ωραιοποιούν": "ωραιοποιώ — to embellish", "επιλεκτική": "επιλεκτικός — selective", "διασταυρώνουμε": "διασταυρώνω — to cross-check", "τεκμήρια": "τεκμήριο — piece of evidence", "συλλογική": "συλλογικός — collective", "ακρόαση": "ακρόαση — listening"},
})

ITEMS.append({
 "id": "l59-c1-navarino", "title": "Η ναυμαχία του Ναυαρίνου", "title_en": "The Battle of Navarino", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για μια ναυμαχία που έκρινε την έκβαση της Ελληνικής Επανάστασης.",
 "script": [
  L("Ιστορικός", "f", "Το 1827 η Ελληνική Επανάσταση βρισκόταν σε κρίσιμο σημείο. Ο Ιμπραήμ, με τα αιγυπτιακά στρατεύματα, είχε καταστρέψει μεγάλο μέρος της Πελοποννήσου, και το Μεσολόγγι είχε πέσει. Πολλοί πίστευαν ότι η εξέγερση πλησίαζε στο τέλος της.", "In 1827 the Greek Revolution was at a critical point. Ibrahim, with the Egyptian troops, had devastated much of the Peloponnese, and Missolonghi had fallen. Many believed the uprising was nearing its end."),
  L("Ιστορικός", "f", "Τον Ιούλιο του ίδιου χρόνου, η Βρετανία, η Γαλλία και η Ρωσία υπέγραψαν τη Συνθήκη του Λονδίνου, με την οποία ζητούσαν ανακωχή και αυτονομία για την Ελλάδα. Έστειλαν τους στόλους τους στην περιοχή, με εντολή να επιβάλουν την ανακωχή, κατά προτίμηση χωρίς μάχη. Στις 20 Οκτωβρίου 1827, ο συμμαχικός στόλος, υπό τον Βρετανό ναύαρχο Κόδριγκτον, μπήκε στον κόλπο του Ναυαρίνου, όπου ήταν αγκυροβολημένος ο τουρκοαιγυπτιακός στόλος.", "In July of that year, Britain, France and Russia signed the Treaty of London, demanding an armistice and autonomy for Greece. They sent their fleets to the area with orders to impose the armistice, preferably without a battle. On 20 October 1827 the allied fleet, under the British admiral Codrington, entered the bay of Navarino, where the Turkish-Egyptian fleet lay at anchor."),
  L("Ιστορικός", "f", "Η ναυμαχία, που κατά πάσα πιθανότητα ξέσπασε από ένα επεισόδιο και όχι από προσχεδιασμένη επίθεση, κράτησε λίγες ώρες. Ο τουρκοαιγυπτιακός στόλος καταστράφηκε σχεδόν ολοσχερώς. Είναι μια από τις ειρωνείες της ιστορίας ότι μια μάχη που καμία από τις Δυνάμεις δεν επιθυμούσε άνοιξε τον δρόμο για την ανεξαρτησία. Από εκείνη τη στιγμή, η ίδρυση ελληνικού κράτους έπαψε να είναι ζήτημα του αν και έγινε ζήτημα του πώς.", "The battle, which in all probability broke out from an incident rather than a premeditated attack, lasted a few hours. The Turkish-Egyptian fleet was almost completely destroyed. It is one of history's ironies that a battle none of the Powers wanted opened the way to independence. From that moment on, the founding of a Greek state ceased to be a question of whether and became a question of how."),
 ],
 "questions": [
  Q("Σε τι κατάσταση βρισκόταν η Επανάσταση το 1827;", ["Οι Έλληνες είχαν απελευθερώσει την Πελοπόννησο", "Βρισκόταν σε κρίσιμο σημείο μετά τις επιτυχίες του Ιμπραήμ", "Είχε μόλις ξεκινήσει", "Είχε ήδη τελειώσει"], 1, "η Ελληνική Επανάσταση βρισκόταν σε κρίσιμο σημείο"),
  Q("Ποια ήταν η εντολή των συμμαχικών στόλων;", ["Να καταστρέψουν τον τουρκοαιγυπτιακό στόλο", "Να επιβάλουν την ανακωχή, κατά προτίμηση χωρίς μάχη", "Να μεταφέρουν στρατό στην Πελοπόννησο", "Να καταλάβουν το Ναυαρίνο"], 1, "με εντολή να επιβάλουν την ανακωχή, κατά προτίμηση χωρίς μάχη"),
  Q("Πώς ξέσπασε, κατά πάσα πιθανότητα, η ναυμαχία;", ["Από προσχεδιασμένη επίθεση", "Από ένα επεισόδιο", "Μετά από τελεσίγραφο", "Από επίθεση των Ελλήνων"], 1, "κατά πάσα πιθανότητα ξέσπασε από ένα επεισόδιο και όχι από προσχεδιασμένη επίθεση"),
  Q("Ποια «ειρωνεία της ιστορίας» επισημαίνει η ομιλήτρια;", ["Ότι οι Έλληνες δεν πήραν μέρος στη ναυμαχία", "Ότι μια μάχη που καμία Δύναμη δεν επιθυμούσε άνοιξε τον δρόμο για την ανεξαρτησία", "Ότι ο Κόδριγκτον τιμωρήθηκε", "Ότι η μάχη έγινε μετά το τέλος του πολέμου"], 1, "μια μάχη που καμία από τις Δυνάμεις δεν επιθυμούσε άνοιξε τον δρόμο για την ανεξαρτησία"),
 ],
 "gloss": {"ναυμαχία": "ναυμαχία — naval battle", "έκβαση": "έκβαση — outcome", "ανακωχή": "ανακωχή — armistice", "αυτονομία": "αυτονομία — autonomy", "ναύαρχο": "ναύαρχος — admiral", "αγκυροβολημένος": "αγκυροβολημένος — at anchor", "προσχεδιασμένη": "προσχεδιασμένος — premeditated", "ολοσχερώς": "ολοσχερώς — completely", "ειρωνείες": "ειρωνεία — irony", "έπαψε": "παύω — to cease"},
})

rnd = random.Random(59)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-59.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
