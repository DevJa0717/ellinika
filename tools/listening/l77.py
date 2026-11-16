# Source for library/listening/listening-77.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l77.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l77-ann-spilaio-limnon", "title": "Ανακοίνωση στο Σπήλαιο των Λιμνών", "title_en": "Announcement at the Cave of the Lakes", "type": "announcement", "level": "B2",
 "context_el": "Επισκέπτεστε το Σπήλαιο των Λιμνών στα Καστριά της Αχαΐας. Θα ακούσετε μια ανακοίνωση στην αίθουσα αναμονής πριν από την ξενάγηση.",
 "script": [
  L("Ξεναγός", "f", "Καλώς ήρθατε στο Σπήλαιο των Λιμνών. Η επόμενη ξενάγηση ξεκινά σε δέκα λεπτά και διαρκεί περίπου σαράντα λεπτά. Μέσα στο σπήλαιο η θερμοκρασία μένει σχεδόν σταθερή όλο τον χρόνο, γύρω στους δεκατέσσερις βαθμούς, οπότε όσοι φοράτε κοντομάνικα καλό είναι να πάρετε μια ζακέτα.", "Welcome to the Cave of the Lakes. The next guided tour starts in ten minutes and lasts about forty minutes. Inside the cave the temperature stays almost constant all year round, at about fourteen degrees, so those of you in short sleeves would do well to take a cardigan."),
  L("Ξεναγός", "f", "Η διαδρομή γίνεται πάνω σε τεχνητούς διαδρόμους, δίπλα στις κλιμακωτές λίμνες. Το δάπεδο είναι υγρό και σε κάποια σημεία γλιστράει, γι’ αυτό κρατιέστε από την κουπαστή και μην τρέχετε. Απαγορεύεται αυστηρά να αγγίζετε τους σταλακτίτες: το λίπος από τα χέρια μας σταματά την ανάπτυξή τους, που είναι μόλις λίγα χιλιοστά κάθε αιώνα.", "The route is along man-made walkways, next to the terraced lakes. The floor is wet and slippery in places, so hold on to the handrail and don't run. Touching the stalactites is strictly forbidden: the grease from our hands stops their growth, which is only a few millimetres per century."),
  L("Ξεναγός", "f", "Η φωτογράφηση επιτρέπεται, αλλά χωρίς φλας. Τα καροτσάκια μωρών πρέπει να μείνουν εδώ, στον χώρο φύλαξης. Ευχαριστούμε και καλή περιήγηση.", "Photography is allowed, but without flash. Baby buggies must stay here, in the storage area. Thank you and enjoy the tour."),
 ],
 "questions": [
  Q("Γιατί προτείνει η ξεναγός να πάρουν ζακέτα;", ["Γιατί έχει αέρα", "Γιατί μέσα η θερμοκρασία είναι γύρω στους δεκατέσσερις βαθμούς", "Γιατί θα βρέξει", "Γιατί η ξενάγηση κρατά πολλές ώρες"], 1, "η θερμοκρασία μένει σχεδόν σταθερή όλο τον χρόνο, γύρω στους δεκατέσσερις βαθμούς"),
  Q("Γιατί δεν πρέπει να αγγίζουν τους σταλακτίτες;", ["Γιατί είναι κοφτεροί", "Γιατί το λίπος από τα χέρια σταματά την ανάπτυξή τους", "Γιατί είναι βρόμικοι", "Γιατί μπορεί να σπάσουν και να πέσουν"], 1, "το λίπος από τα χέρια μας σταματά την ανάπτυξή τους"),
  Q("Τι ισχύει για τη φωτογράφηση;", ["Απαγορεύεται εντελώς", "Επιτρέπεται, αλλά χωρίς φλας", "Επιτρέπεται μόνο με άδεια", "Επιτρέπεται μόνο στην έξοδο"], 1, "Η φωτογράφηση επιτρέπεται, αλλά χωρίς φλας"),
 ],
 "gloss": {"ξενάγηση": "ξενάγηση — guided tour", "σταθερή": "σταθερός — constant, stable", "κοντομάνικα": "κοντομάνικο — short-sleeved top", "ζακέτα": "ζακέτα — cardigan", "κλιμακωτές": "κλιμακωτός — terraced, stepped", "γλιστράει": "γλιστράω — to be slippery, to slip", "κουπαστή": "κουπαστή — handrail", "σταλακτίτες": "σταλακτίτης — stalactite", "χιλιοστά": "χιλιοστό — millimetre", "καροτσάκια": "καροτσάκι — (baby) buggy"},
})

ITEMS.append({
 "id": "l77-vm-topografos", "title": "Μήνυμα από τον τοπογράφο", "title_en": "Message from the land surveyor", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κληρονομήσει ένα οικόπεδο σε ένα χωριό και θέλετε να το πουλήσετε. Θα ακούσετε ένα μήνυμα από τον τοπογράφο που προσλάβατε.",
 "script": [
  L("Τοπογράφος", "m", "Καλημέρα, ο Σταύρος Λιάκος είμαι, ο τοπογράφος. Πήγα χθες στο οικόπεδο και έκανα τις μετρήσεις. Τα καλά νέα είναι ότι η έκταση είναι μεγαλύτερη απ’ ό,τι γράφει το παλιό συμβόλαιο: όχι τρία, αλλά σχεδόν τρία και μισό στρέμματα.", "Good morning, it's Stavros Liakos, the surveyor. I went to the plot yesterday and took the measurements. The good news is that the area is bigger than the old deed says: not three, but almost three and a half stremmata."),
  L("Τοπογράφος", "m", "Τα λιγότερο καλά νέα: ο γείτονας από τη βόρεια πλευρά έχει χτίσει μια μάντρα που μπαίνει περίπου δύο μέτρα μέσα στο δικό σας κομμάτι. Αυτό πρέπει να ξεκαθαρίσει πριν από την πώληση, γιατί κανένας συμβολαιογράφος δεν θα προχωρήσει με τέτοια διαφορά.", "The less good news: the neighbour on the north side has built a wall that comes about two metres into your piece. This has to be cleared up before the sale, because no notary will proceed with a discrepancy like that."),
  L("Τοπογράφος", "m", "Προτείνω να μιλήσετε πρώτα φιλικά μαζί του· συνήθως τέτοια θέματα λύνονται χωρίς δικηγόρους. Το τοπογραφικό διάγραμμα θα είναι έτοιμο την Παρασκευή. Πάρτε με όποτε μπορείτε.", "I suggest you first talk to him in a friendly way; these things are usually settled without lawyers. The survey plan will be ready on Friday. Call me whenever you can."),
 ],
 "questions": [
  Q("Τι διαπίστωσε ο τοπογράφος για την έκταση;", ["Ότι είναι μικρότερη από το συμβόλαιο", "Ότι είναι σχεδόν τρία και μισό στρέμματα, μεγαλύτερη από το συμβόλαιο", "Ότι είναι ακριβώς όσο γράφει το συμβόλαιο", "Ότι δεν μπορεί να μετρηθεί"], 1, "όχι τρία, αλλά σχεδόν τρία και μισό στρέμματα"),
  Q("Ποιο πρόβλημα υπάρχει με τον γείτονα;", ["Θέλει να αγοράσει το οικόπεδο", "Η μάντρα του μπαίνει δύο μέτρα μέσα στο οικόπεδο", "Έκοψε τα δέντρα", "Έχει ανοίξει δρόμο μέσα από το οικόπεδο"], 1, "έχει χτίσει μια μάντρα που μπαίνει περίπου δύο μέτρα μέσα στο δικό σας κομμάτι"),
  Q("Τι προτείνει ο τοπογράφος;", ["Να πάνε αμέσως στο δικαστήριο", "Να μιλήσουν πρώτα φιλικά με τον γείτονα", "Να ακυρώσουν την πώληση", "Να γκρεμίσουν τη μάντρα"], 1, "Προτείνω να μιλήσετε πρώτα φιλικά μαζί του"),
 ],
 "gloss": {"κληρονομήσει": "κληρονομώ — to inherit", "οικόπεδο": "οικόπεδο — plot of land", "τοπογράφο": "τοπογράφος — land surveyor", "μετρήσεις": "μέτρηση — measurement", "έκταση": "έκταση — area, extent", "συμβόλαιο": "συμβόλαιο — deed, contract", "στρέμματα": "στρέμμα — stremma (1,000 m²)", "μάντρα": "μάντρα — boundary wall", "συμβολαιογράφος": "συμβολαιογράφος — notary", "τοπογραφικό διάγραμμα": "τοπογραφικό διάγραμμα — survey plan"},
})

ITEMS.append({
 "id": "l77-dia-afthaireto", "title": "Το αυθαίρετο του θείου", "title_en": "Uncle's unauthorised extension", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέρφια συζητούν για ένα δωμάτιο που είχε χτίσει ο θείος τους χωρίς άδεια, πάνω στην ταράτσα του πατρικού τους σπιτιού.",
 "script": [
  L("Μαρίνα", "f", "Ο μηχανικός μου είπε σήμερα ότι το δωμάτιο στην ταράτσα είναι αυθαίρετο. Ο θείος το έχτισε το ογδόντα πέντε χωρίς καμία άδεια. Αν δεν το τακτοποιήσουμε, δεν μπορούμε ούτε να πουλήσουμε ούτε να νοικιάσουμε νόμιμα το σπίτι.", "The engineer told me today that the room on the roof is unauthorised. Uncle built it in eighty-five without any permit. If we don't regularise it, we can neither sell nor legally rent out the house."),
  L("Στέλιος", "m", "Δηλαδή τι, θα το γκρεμίσουμε; Εκεί μέσα έχουμε περάσει όλα τα καλοκαίρια της παιδικής μας ηλικίας.", "Meaning what, we'll knock it down? We spent every summer of our childhood in there."),
  L("Μαρίνα", "f", "Όχι απαραίτητα. Υπάρχει διαδικασία νομιμοποίησης: πληρώνεις ένα πρόστιμο, ανάλογα με τα τετραγωνικά και την παλαιότητα, και ο μηχανικός καταθέτει τα χαρτιά ηλεκτρονικά. Για τόσο παλιά κατασκευή το πρόστιμο είναι μικρότερο.", "Not necessarily. There's a legalisation procedure: you pay a fine, depending on the square metres and the age, and the engineer submits the papers online. For such an old structure the fine is smaller."),
  L("Στέλιος", "m", "Και πόσο είναι περίπου; Γιατί αν μιλάμε για χιλιάδες, ίσως είναι καλύτερα να το αφήσουμε για αργότερα.", "And how much is it roughly? Because if we're talking thousands, maybe it's better to leave it for later."),
  L("Μαρίνα", "f", "Κάτι λιγότερο από δύο χιλιάδες, μαζί με την αμοιβή του μηχανικού. Και να ξέρεις ότι όσο το αφήνουμε, τόσο ρισκάρουμε να αλλάξει ο νόμος και να γίνει πιο ακριβό. Εγώ λέω να το κάνουμε τώρα και να το μοιράσουμε.", "A bit under two thousand, including the engineer's fee. And bear in mind that the longer we leave it, the more we risk the law changing and it getting more expensive. I say we do it now and split it."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με το δωμάτιο στην ταράτσα;", ["Έχει υγρασία", "Χτίστηκε χωρίς άδεια", "Είναι επικίνδυνο να πέσει", "Ανήκει στον γείτονα"], 1, "Ο θείος το έχτισε το ογδόντα πέντε χωρίς καμία άδεια"),
  Q("Από τι εξαρτάται το πρόστιμο;", ["Από το εισόδημα των ιδιοκτητών", "Από τα τετραγωνικά και την παλαιότητα", "Από την περιοχή μόνο", "Από τον αριθμό των ιδιοκτητών"], 1, "ανάλογα με τα τετραγωνικά και την παλαιότητα"),
  Q("Γιατί θέλει η Μαρίνα να το κάνουν τώρα;", ["Γιατί έχει αγοραστή", "Γιατί μπορεί να αλλάξει ο νόμος και να γίνει πιο ακριβό", "Γιατί το ζήτησε ο θείος", "Γιατί λήγει η άδεια"], 1, "ρισκάρουμε να αλλάξει ο νόμος και να γίνει πιο ακριβό"),
 ],
 "gloss": {"αυθαίρετο": "αυθαίρετο — unauthorised building", "ταράτσα": "ταράτσα — flat roof", "πατρικού": "πατρικό — family home", "τακτοποιήσουμε": "τακτοποιώ — to regularise, sort out", "γκρεμίσουμε": "γκρεμίζω — to demolish", "νομιμοποίησης": "νομιμοποίηση — legalisation", "πρόστιμο": "πρόστιμο — fine", "τετραγωνικά": "τετραγωνικά — square metres", "παλαιότητα": "παλαιότητα — age (of a building)", "αμοιβή": "αμοιβή — fee"},
})

ITEMS.append({
 "id": "l77-dia-glyko-koutaliou", "title": "Γλυκό του κουταλιού με τη γιαγιά", "title_en": "Making spoon sweets with grandma", "type": "dialogue", "level": "B2",
 "context_el": "Μια εγγονή φτιάχνει για πρώτη φορά γλυκό του κουταλιού σύκο με τη γιαγιά της.",
 "script": [
  L("Δανάη", "f", "Γιαγιά, η συνταγή στο ίντερνετ λέει να τα βράσουμε όλα μαζί, σύκα, ζάχαρη και νερό, για μία ώρα. Γιατί εσύ τα έχεις στο νερό από χθες;", "Grandma, the recipe online says to boil everything together, figs, sugar and water, for an hour. Why have you had them in water since yesterday?"),
  L("Γιαγιά", "f", "Γιατί αυτά είναι μικρά, άγουρα σύκα, παιδί μου, και έχουν ένα γάλα πικρό. Τα τρυπάμε με πιρούνι, τα ζεματάμε και τα αφήνουμε στο κρύο νερό, που το αλλάζουμε τρεις τέσσερις φορές. Αλλιώς το γλυκό πικρίζει.", "Because these are small, unripe figs, my dear, and they have a bitter milk. We prick them with a fork, blanch them and leave them in cold water, which we change three or four times. Otherwise the sweet turns bitter."),
  L("Δανάη", "f", "Και πώς καταλαβαίνεις ότι το σιρόπι έδεσε; Εδώ γράφει να χρησιμοποιήσουμε θερμόμετρο.", "And how do you tell the syrup has set? It says here to use a thermometer."),
  L("Γιαγιά", "f", "Θερμόμετρο! Ρίχνεις μια σταγόνα σε ένα πιατάκι. Αν κυλήσει, θέλει κι άλλο βράσιμο. Αν μείνει στρογγυλή σαν μαργαριτάρι, είναι έτοιμο. Και στο τέλος στύβεις λίγο λεμόνι, για να μη ζαχαρώσει στο βάζο.", "Thermometer! You drop a drop on a little plate. If it runs, it needs more boiling. If it stays round like a pearl, it's ready. And at the end you squeeze in a little lemon, so it doesn't crystallise in the jar."),
  L("Δανάη", "f", "Θα το γράψω, γιατί αυτό δεν το λέει καμία συνταγή.", "I'll write that down, because no recipe says that."),
 ],
 "questions": [
  Q("Γιατί η γιαγιά έχει τα σύκα στο νερό από χθες;", ["Για να μαλακώσουν", "Για να φύγει το πικρό γάλα τους", "Για να πλυθούν από το χώμα", "Για να μεγαλώσουν"], 1, "έχουν ένα γάλα πικρό"),
  Q("Πώς καταλαβαίνει η γιαγιά ότι το σιρόπι είναι έτοιμο;", ["Με θερμόμετρο", "Η σταγόνα μένει στρογγυλή σαν μαργαριτάρι", "Μετά από ακριβώς μία ώρα", "Από το χρώμα του"], 1, "Αν μείνει στρογγυλή σαν μαργαριτάρι, είναι έτοιμο"),
  Q("Γιατί βάζει λεμόνι στο τέλος;", ["Για να έχει πιο ξινή γεύση", "Για να μη ζαχαρώσει στο βάζο", "Για να αλλάξει χρώμα", "Για να κρυώσει πιο γρήγορα"], 1, "για να μη ζαχαρώσει στο βάζο"),
 ],
 "gloss": {"γλυκό του κουταλιού": "γλυκό του κουταλιού — spoon sweet (fruit in syrup)", "άγουρα": "άγουρος — unripe", "τρυπάμε": "τρυπάω — to prick, pierce", "ζεματάμε": "ζεματάω — to blanch, scald", "πικρίζει": "πικρίζω — to turn bitter", "σιρόπι": "σιρόπι — syrup", "έδεσε": "δένω — (of syrup) to thicken, set", "μαργαριτάρι": "μαργαριτάρι — pearl", "στύβεις": "στύβω — to squeeze", "ζαχαρώσει": "ζαχαρώνω — to crystallise (sugar)"},
})

ITEMS.append({
 "id": "l77-int-glossologos", "title": "Η γλωσσολόγος που βοηθά την αστυνομία", "title_en": "The linguist who helps the police", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή μιλά μια γλωσσολόγος που αναλύει κείμενα για λογαριασμό της δικαιοσύνης.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνει ένας δικαστικός γλωσσολόγος;", "What exactly does a forensic linguist do?"),
  L("Γλωσσολόγος", "f", "Αναλύουμε γλωσσικό υλικό που σχετίζεται με μια υπόθεση: απειλητικά μηνύματα, ανώνυμες επιστολές, ακόμα και ηχογραφημένες κλήσεις. Το πιο συνηθισμένο ερώτημα είναι αν δύο κείμενα έχουν γραφτεί από το ίδιο πρόσωπο.", "We analyse language material connected to a case: threatening messages, anonymous letters, even recorded calls. The most common question is whether two texts were written by the same person."),
  L("Δημοσιογράφος", "m", "Και πώς το καταλαβαίνετε αυτό;", "And how do you work that out?"),
  L("Γλωσσολόγος", "f", "Ο καθένας μας έχει ένα γλωσσικό αποτύπωμα: λέξεις που επαναλαμβάνει, ορθογραφικά λάθη που κάνει πάντα, τον τρόπο που χρησιμοποιεί τα σημεία στίξης. Είχαμε μια υπόθεση όπου ο δράστης έγραφε πάντα τη λέξη «σήμερα» χωρίς τόνο και έβαζε τρία θαυμαστικά. Δεν είναι απόδειξη από μόνο του, αλλά μαζί με άλλα στοιχεία βοηθά.", "Each of us has a linguistic fingerprint: words we repeat, spelling mistakes we always make, the way we use punctuation. We had a case where the culprit always wrote the word «σήμερα» without an accent and put three exclamation marks. It isn't proof on its own, but together with other evidence it helps."),
  L("Δημοσιογράφος", "m", "Υπάρχουν όρια σε αυτό που μπορείτε να πείτε;", "Are there limits to what you can say?"),
  L("Γλωσσολόγος", "f", "Πολλά. Δεν λέμε ποτέ «αυτός το έγραψε». Λέμε ότι τα στοιχεία στηρίζουν περισσότερο ή λιγότερο μια υπόθεση. Η τελική κρίση ανήκει στο δικαστήριο.", "Many. We never say 'he wrote it'. We say the evidence supports a hypothesis more or less strongly. The final judgement belongs to the court."),
 ],
 "questions": [
  Q("Ποιο είναι το πιο συνηθισμένο ερώτημα που της θέτουν;", ["Αν ένα κείμενο είναι μεταφρασμένο", "Αν δύο κείμενα γράφτηκαν από το ίδιο πρόσωπο", "Πόσο χρονών είναι ο συγγραφέας", "Από ποια χώρα είναι ο δράστης"], 1, "αν δύο κείμενα έχουν γραφτεί από το ίδιο πρόσωπο"),
  Q("Τι είναι το «γλωσσικό αποτύπωμα»;", ["Η φωνή κάποιου", "Οι προσωπικές συνήθειες στη γραφή, όπως λέξεις, λάθη και στίξη", "Ο γραφικός χαρακτήρας", "Η μητρική γλώσσα κάποιου"], 1, "λέξεις που επαναλαμβάνει, ορθογραφικά λάθη που κάνει πάντα, τον τρόπο που χρησιμοποιεί τα σημεία στίξης"),
  Q("Τι δεν λέει ποτέ η γλωσσολόγος στο δικαστήριο;", ["Ότι τα στοιχεία στηρίζουν μια υπόθεση", "«Αυτός το έγραψε»", "Ότι χρειάζεται περισσότερο υλικό", "Ότι το κείμενο είναι ανώνυμο"], 1, "Δεν λέμε ποτέ «αυτός το έγραψε»"),
 ],
 "gloss": {"γλωσσολόγος": "γλωσσολόγος — linguist", "δικαιοσύνης": "δικαιοσύνη — justice (system)", "δικαστικός": "δικαστικός — forensic, judicial", "απειλητικά": "απειλητικός — threatening", "ανώνυμες επιστολές": "ανώνυμη επιστολή — anonymous letter", "αποτύπωμα": "αποτύπωμα — fingerprint, imprint", "σημεία στίξης": "σημεία στίξης — punctuation marks", "δράστης": "δράστης — culprit, perpetrator", "θαυμαστικά": "θαυμαστικό — exclamation mark", "κρίση": "κρίση — judgement"},
})

ITEMS.append({
 "id": "l77-rep-retsina", "title": "Η επιστροφή της ρετσίνας", "title_en": "The return of retsina", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από μια ραδιοφωνική εκπομπή για το κρασί.",
 "script": [
  L("Ρεπόρτερ", "f", "Για πολλά χρόνια η ρετσίνα είχε κακό όνομα. Τις δεκαετίες του εβδομήντα και του ογδόντα, μαζί με τον μαζικό τουρισμό, γέμισαν οι ταβέρνες με φτηνή ρετσίνα χύμα, συχνά κακής ποιότητας, και πολλοί ξένοι γύρισαν σπίτι τους με την ιδέα ότι το ελληνικό κρασί μυρίζει τερεβινθέλαιο.", "For many years retsina had a bad name. In the seventies and eighties, along with mass tourism, the tavernas filled with cheap bulk retsina, often of poor quality, and many foreigners went home with the idea that Greek wine smells of turpentine."),
  L("Ρεπόρτερ", "f", "Η ρετσίνα όμως έχει βαθιές ρίζες. Στην αρχαιότητα οι αμφορείς σφραγίζονταν με ρετσίνι πεύκου, για να μη χαλάει το κρασί, και η γεύση αυτή έγινε σιγά σιγά επιθυμητή. Σήμερα το ρετσίνι προστίθεται στον μούστο κατά τη ζύμωση, κυρίως σε κρασί από την αττική ποικιλία σαββατιανό.", "But retsina has deep roots. In antiquity amphorae were sealed with pine resin so the wine wouldn't spoil, and this taste gradually became desirable. Today the resin is added to the must during fermentation, mainly to wine from the Attic Savvatiano variety."),
  L("Ρεπόρτερ", "f", "Τα τελευταία χρόνια μια νέα γενιά οινοποιών βάζει πολύ λιγότερο ρετσίνι και πολύ περισσότερη φροντίδα. Οι ρετσίνες τους κερδίζουν βραβεία και μπαίνουν σε κάρτες εστιατορίων στη Νέα Υόρκη και το Λονδίνο. Όπως μας είπε ένας από αυτούς, «η ρετσίνα δεν ήταν ποτέ το πρόβλημα· το πρόβλημα ήταν η βιασύνη».", "In recent years a new generation of winemakers has been putting in much less resin and much more care. Their retsinas win awards and appear on restaurant wine lists in New York and London. As one of them told us, 'retsina was never the problem; the problem was the hurry.'"),
 ],
 "questions": [
  Q("Γιατί είχε η ρετσίνα κακό όνομα;", ["Γιατί ήταν πολύ ακριβή", "Γιατί στα χρόνια του μαζικού τουρισμού σερβιριζόταν φτηνή και κακής ποιότητας", "Γιατί απαγορεύτηκε", "Γιατί ήταν πολύ γλυκιά"], 1, "γέμισαν οι ταβέρνες με φτηνή ρετσίνα χύμα, συχνά κακής ποιότητας"),
  Q("Γιατί έβαζαν ρετσίνι στους αρχαίους αμφορείς;", ["Για να έχει χρώμα το κρασί", "Για να μη χαλάει το κρασί", "Για θρησκευτικούς λόγους", "Για να είναι πιο δυνατό το κρασί"], 1, "σφραγίζονταν με ρετσίνι πεύκου, για να μη χαλάει το κρασί"),
  Q("Τι κάνουν διαφορετικά οι νέοι οινοποιοί;", ["Βάζουν περισσότερο ρετσίνι", "Βάζουν λιγότερο ρετσίνι και περισσότερη φροντίδα", "Χρησιμοποιούν μόνο ξένες ποικιλίες", "Πουλάνε μόνο χύμα"], 1, "βάζει πολύ λιγότερο ρετσίνι και πολύ περισσότερη φροντίδα"),
 ],
 "gloss": {"ρετσίνα": "ρετσίνα — retsina (resinated wine)", "χύμα": "χύμα — in bulk, loose", "τερεβινθέλαιο": "τερεβινθέλαιο — turpentine", "αμφορείς": "αμφορέας — amphora", "σφραγίζονταν": "σφραγίζω — to seal", "ρετσίνι": "ρετσίνι — resin", "μούστο": "μούστος — must (grape juice)", "ζύμωση": "ζύμωση — fermentation", "ποικιλία": "ποικιλία — (grape) variety", "οινοποιών": "οινοποιός — winemaker"},
})

ITEMS.append({
 "id": "l77-mono-kalligrafia", "title": "Καλλιγραφία με πένα και μελάνι", "title_en": "Calligraphy with pen and ink", "type": "monologue", "level": "B2",
 "context_el": "Μια λογίστρια μιλά σε ένα podcast για το χόμπι που ανακάλυψε στα πενήντα της.",
 "script": [
  L("Ευτυχία", "f", "Όλη μέρα πληκτρολογώ αριθμούς. Κάποια στιγμή συνειδητοποίησα ότι δεν είχα γράψει κάτι με το χέρι, πέρα από τη λίστα του σούπερ μάρκετ, εδώ και χρόνια. Έτσι γράφτηκα σε ένα εργαστήρι καλλιγραφίας, κυρίως από περιέργεια.", "I type numbers all day. At some point I realised I hadn't written anything by hand, apart from the supermarket list, for years. So I signed up for a calligraphy workshop, mainly out of curiosity."),
  L("Ευτυχία", "f", "Τις πρώτες εβδομάδες δεν γράφαμε καν γράμματα. Κάναμε μόνο γραμμές, κάθετες και πλάγιες, σελίδες ολόκληρες, για να μάθει το χέρι να κρατά την πένα στη σωστή γωνία. Μου φαινόταν βαρετό, αλλά ο δάσκαλος επέμενε ότι η καλλιγραφία είναι πρώτα απ’ όλα υπομονή.", "For the first weeks we didn't even write letters. We only drew lines, vertical and slanted, whole pages, so the hand would learn to hold the pen at the right angle. It seemed boring to me, but the teacher insisted that calligraphy is first and foremost patience."),
  L("Ευτυχία", "f", "Σήμερα γράφω ευχετήριες κάρτες για όλη την οικογένεια, και φέτος μου ζήτησαν να γράψω τα ονόματα στις προσκλήσεις ενός γάμου. Αλλά το πιο σημαντικό είναι άλλο: όταν γράφω, το μυαλό μου ησυχάζει. Δεν μπορείς να σκέφτεσαι τα φορολογικά και να φτιάχνεις ένα τέλειο άλφα ταυτόχρονα.", "Today I write greeting cards for the whole family, and this year I was asked to write the names on the invitations for a wedding. But the most important thing is something else: when I write, my mind goes quiet. You can't think about tax returns and make a perfect alpha at the same time."),
 ],
 "questions": [
  Q("Γιατί ξεκίνησε η Ευτυχία την καλλιγραφία;", ["Το πρότεινε ο γιατρός της", "Συνειδητοποίησε ότι δεν έγραφε πια με το χέρι", "Ήθελε να γίνει επαγγελματίας", "Της το έκαναν δώρο"], 1, "δεν είχα γράψει κάτι με το χέρι, πέρα από τη λίστα του σούπερ μάρκετ, εδώ και χρόνια"),
  Q("Τι έκαναν τις πρώτες εβδομάδες;", ["Έγραφαν ολόκληρα ποιήματα", "Έκαναν μόνο γραμμές για να μάθει το χέρι τη σωστή γωνία", "Διάβαζαν για την ιστορία της γραφής", "Έφτιαχναν μελάνι"], 1, "Κάναμε μόνο γραμμές, κάθετες και πλάγιες"),
  Q("Ποιο είναι για εκείνη το πιο σημαντικό όφελος;", ["Τα χρήματα από τις προσκλήσεις", "Ότι το μυαλό της ησυχάζει", "Ότι γνώρισε νέους φίλους", "Ότι βελτιώθηκε στη δουλειά"], 1, "όταν γράφω, το μυαλό μου ησυχάζει"),
 ],
 "gloss": {"πληκτρολογώ": "πληκτρολογώ — to type", "συνειδητοποίησα": "συνειδητοποιώ — to realise", "εργαστήρι": "εργαστήρι — workshop", "καλλιγραφίας": "καλλιγραφία — calligraphy", "κάθετες": "κάθετος — vertical", "πλάγιες": "πλάγιος — slanted", "πένα": "πένα — nib pen", "ευχετήριες κάρτες": "ευχετήρια κάρτα — greeting card", "προσκλήσεις": "πρόσκληση — invitation", "φορολογικά": "φορολογικά — tax matters"},
})

ITEMS.append({
 "id": "l77-mono-lachnos", "title": "Ο λαχνός που κέρδισε", "title_en": "The winning lottery ticket", "type": "monologue", "level": "B2",
 "context_el": "Ένας συνταξιούχος διηγείται σε μια εκπομπή τι έγινε όταν κέρδισε ένα μικρό ποσό στο λαχείο.",
 "script": [
  L("Κυρ Αντώνης", "m", "Σαράντα χρόνια αγόραζα κάθε εβδομάδα ένα λαχείο από τον ίδιο λαχειοπώλη, τον κυρ Μήτσο, στη γωνία της πλατείας. Δεν κέρδιζα ποτέ τίποτα, εκτός από κανένα δεκάρικο. Το έκανα πιο πολύ για την κουβέντα μαζί του.", "For forty years I bought a lottery ticket every week from the same lottery seller, Mr Mitsos, on the corner of the square. I never won anything, apart from the odd tenner. I did it more for the chat with him."),
  L("Κυρ Αντώνης", "m", "Πέρσι τον Δεκέμβριο ο λαχνός μου κέρδισε πέντε χιλιάδες ευρώ. Όχι εκατομμύρια, αλλά για έναν συνταξιούχο είναι πολλά. Και ξέρετε τι έπαθα; Από την επόμενη μέρα άρχισαν να με παίρνουν τηλέφωνο συγγενείς που είχα να τους ακούσω δέκα χρόνια.", "Last December my ticket won five thousand euros. Not millions, but for a pensioner it's a lot. And do you know what happened to me? From the next day relatives I hadn't heard from in ten years started calling me."),
  L("Κυρ Αντώνης", "m", "Στο τέλος έκανα τρία πράγματα: άλλαξα τα παράθυρα του σπιτιού, που έμπαζαν αέρα, πήγα τη γυναίκα μου ένα ταξίδι στη Βιέννη και έδωσα ένα μέρος στον κυρ Μήτσο. Εκείνος μου πούλησε τον λαχνό, δικαίωμά του κι αυτουνού. Συνεχίζω να αγοράζω κάθε εβδομάδα, αλλά πια δεν περιμένω τίποτα.", "In the end I did three things: I changed the windows of the house, which let in draughts, I took my wife on a trip to Vienna and I gave a share to Mr Mitsos. He sold me the ticket, it's his right too. I keep buying every week, but now I expect nothing."),
 ],
 "questions": [
  Q("Γιατί αγόραζε ο κυρ Αντώνης λαχείο κάθε εβδομάδα;", ["Γιατί πίστευε ότι θα γίνει πλούσιος", "Κυρίως για την κουβέντα με τον λαχειοπώλη", "Γιατί το ζητούσε η γυναίκα του", "Για να βοηθήσει φιλανθρωπικούς σκοπούς"], 1, "Το έκανα πιο πολύ για την κουβέντα μαζί του"),
  Q("Τι συνέβη μετά τη νίκη του;", ["Τον κάλεσε η τηλεόραση", "Άρχισαν να του τηλεφωνούν ξεχασμένοι συγγενείς", "Σταμάτησε να βγαίνει από το σπίτι", "Μετακόμισε σε άλλη πόλη"], 1, "άρχισαν να με παίρνουν τηλέφωνο συγγενείς που είχα να τους ακούσω δέκα χρόνια"),
  Q("Ποιο από τα παρακάτω ΔΕΝ έκανε με τα χρήματα;", ["Άλλαξε τα παράθυρα", "Αγόρασε καινούργιο αυτοκίνητο", "Πήγε ταξίδι στη Βιέννη", "Έδωσε ένα μέρος στον λαχειοπώλη"], 1, "άλλαξα τα παράθυρα του σπιτιού, που έμπαζαν αέρα, πήγα τη γυναίκα μου ένα ταξίδι στη Βιέννη και έδωσα ένα μέρος στον κυρ Μήτσο"),
 ],
 "gloss": {"λαχνός": "λαχνός — lottery ticket, winning number", "λαχείο": "λαχείο — lottery (ticket)", "συνταξιούχος": "συνταξιούχος — pensioner", "λαχειοπώλη": "λαχειοπώλης — lottery-ticket seller", "δεκάρικο": "δεκάρικο — ten-euro note, tenner", "κουβέντα": "κουβέντα — chat", "συγγενείς": "συγγενής — relative", "έμπαζαν": "μπάζω — to let in (draughts, water)", "δικαίωμά": "δικαίωμα — right"},
})

ITEMS.append({
 "id": "l77-c1-taricheftis", "title": "Ταρίχευση και μουσεία φυσικής ιστορίας", "title_en": "Taxidermy and natural history museums", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε απόσπασμα από μια ομιλία της επιμελήτριας ενός μουσείου φυσικής ιστορίας για τις συλλογές βαλσαμωμένων ζώων.",
 "script": [
  L("Επιμελήτρια", "f", "Πολλοί επισκέπτες, ιδίως νέοι, μας ρωτούν αν είναι ηθικό να εκθέτουμε βαλσαμωμένα ζώα. Η ερώτηση είναι εύλογη, και δεν θα την αποφύγω. Θα ξεκινήσω, όμως, από μια διευκρίνιση: κανένα από τα εκθέματα που προστέθηκαν στη συλλογή τις τελευταίες δεκαετίες δεν θανατώθηκε για να εκτεθεί. Προέρχονται από ζωολογικούς κήπους, από κέντρα περίθαλψης άγριων ζώων ή από τροχαία ατυχήματα.", "Many visitors, especially young ones, ask us whether it is ethical to exhibit stuffed animals. The question is reasonable, and I won't avoid it. I will begin, however, with a clarification: none of the exhibits added to the collection in recent decades was killed in order to be displayed. They come from zoos, from wildlife rehabilitation centres or from road accidents."),
  L("Επιμελήτρια", "f", "Τα παλαιότερα δείγματα, αντίθετα, συλλέχθηκαν τον δέκατο ένατο αιώνα με μεθόδους που σήμερα θα θεωρούσαμε απαράδεκτες. Θα μπορούσαμε να τα αποσύρουμε, για να ξεχάσουμε αυτό το παρελθόν. Προτιμούμε να τα κρατήσουμε και να το αφηγηθούμε, γιατί η απόκρυψη δεν είναι μορφή μεταμέλειας.", "The older specimens, by contrast, were collected in the nineteenth century by methods we would consider unacceptable today. We could withdraw them, so as to forget that past. We prefer to keep them and to tell that story, because concealment is not a form of remorse."),
  L("Επιμελήτρια", "f", "Υπάρχει, εξάλλου, και ένας επιστημονικός λόγος. Από αυτά τα δείγματα οι ερευνητές απομονώνουν σήμερα γενετικό υλικό, συγκρίνουν πληθυσμούς που έχουν εκλείψει με τους σημερινούς και μελετούν πώς επηρέασε η ρύπανση τα φτερά των πουλιών μέσα σε έναν αιώνα. Ένα βαλσαμωμένο ζώο, με άλλα λόγια, δεν είναι απλώς διακοσμητικό· είναι ένα αρχείο.", "There is, moreover, a scientific reason. From these specimens researchers today extract genetic material, compare populations that have died out with today's and study how pollution affected birds' feathers over a century. A stuffed animal, in other words, is not merely decorative; it is an archive."),
 ],
 "questions": [
  Q("Από πού προέρχονται τα πρόσφατα εκθέματα;", ["Από κυνηγούς", "Από ζωολογικούς κήπους, κέντρα περίθαλψης ή τροχαία ατυχήματα", "Από αγορές στο εξωτερικό", "Από ιδιωτικές συλλογές του 19ου αιώνα"], 1, "Προέρχονται από ζωολογικούς κήπους, από κέντρα περίθαλψης άγριων ζώων ή από τροχαία ατυχήματα"),
  Q("Γιατί το μουσείο δεν αποσύρει τα παλαιά δείγματα;", ["Γιατί είναι πολύ ακριβά", "Γιατί η απόκρυψη του παρελθόντος δεν είναι μεταμέλεια", "Γιατί το απαγορεύει ο νόμος", "Γιατί είναι τα πιο δημοφιλή"], 1, "η απόκρυψη δεν είναι μορφή μεταμέλειας"),
  Q("Τι εννοεί η επιμελήτρια λέγοντας ότι ένα βαλσαμωμένο ζώο «είναι ένα αρχείο»;", ["Ότι έχει καταγραφεί σε κατάλογο", "Ότι προσφέρει επιστημονικά δεδομένα για το παρελθόν", "Ότι φυλάγεται σε αποθήκη", "Ότι έχει μεγάλη χρηματική αξία"], 1, "οι ερευνητές απομονώνουν σήμερα γενετικό υλικό, συγκρίνουν πληθυσμούς που έχουν εκλείψει με τους σημερινούς"),
 ],
 "gloss": {"βαλσαμωμένων": "βαλσαμωμένος — stuffed (animal)", "εύλογη": "εύλογος — reasonable", "διευκρίνιση": "διευκρίνιση — clarification", "θανατώθηκε": "θανατώνω — to put to death, kill", "περίθαλψης": "περίθαλψη — care, rehabilitation", "απαράδεκτες": "απαράδεκτος — unacceptable", "αποσύρουμε": "αποσύρω — to withdraw", "απόκρυψη": "απόκρυψη — concealment", "μεταμέλειας": "μεταμέλεια — remorse", "έχουν εκλείψει": "εκλείπω — to die out, disappear"},
})

ITEMS.append({
 "id": "l77-c1-geitonies-afthaireta", "title": "Τι μας λένε τα αυθαίρετα για την ελληνική πόλη", "title_en": "What unauthorised buildings tell us about the Greek city", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την πόλη και την αρχιτεκτονική, ένας πολεοδόμος μιλά για την αυθαίρετη δόμηση στην Ελλάδα.",
 "script": [
  L("Δημοσιογράφος", "f", "Η αυθαίρετη δόμηση συνήθως παρουσιάζεται ως ελληνική ιδιαιτερότητα, σχεδόν ως εθνικό ελάττωμα. Συμφωνείτε;", "Unauthorised building is usually presented as a Greek peculiarity, almost a national defect. Do you agree?"),
  L("Πολεοδόμος", "m", "Εν μέρει. Είναι εύκολο να την αποδώσουμε στην ασυνειδησία του πολίτη, αλλά αυτή η ερμηνεία βολεύει κυρίως το κράτος. Για δεκαετίες, η πολιτεία δεν προσέφερε ούτε φτηνή κατοικία ούτε σχέδια πόλης που να προλαβαίνουν την εσωτερική μετανάστευση. Ο κόσμος έχτισε μόνος του, και το κράτος έκανε τα στραβά μάτια, γιατί έτσι λυνόταν ένα πρόβλημα που το ίδιο δεν μπορούσε να λύσει.", "Partly. It's easy to attribute it to the citizen's lack of conscience, but that interpretation mainly suits the state. For decades, the state offered neither cheap housing nor town plans that kept pace with internal migration. People built on their own, and the state turned a blind eye, because that solved a problem it could not solve itself."),
  L("Δημοσιογράφος", "f", "Και οι διαδοχικές νομιμοποιήσεις;", "And the successive legalisations?"),
  L("Πολεοδόμος", "m", "Αυτές είναι η άλλη όψη του ίδιου νομίσματος. Κάθε ρύθμιση φέρνει έσοδα στα δημόσια ταμεία, αλλά ταυτόχρονα στέλνει το μήνυμα ότι η παρανομία στο τέλος συγχωρείται. Το αποτέλεσμα είναι ένας φαύλος κύκλος. Δεν λέω ότι πρέπει να γκρεμιστούν όλα· κάτι τέτοιο θα ήταν κοινωνικά ανεδαφικό. Λέω ότι η τακτοποίηση πρέπει να συνδέεται με πραγματικές βελτιώσεις: στατική επάρκεια, ενεργειακή αναβάθμιση, δημόσιο χώρο.", "These are the other side of the same coin. Each settlement brings revenue to the public coffers, but at the same time sends the message that illegality is forgiven in the end. The result is a vicious circle. I'm not saying everything should be demolished; that would be socially unrealistic. I'm saying regularisation must be tied to real improvements: structural adequacy, energy upgrades, public space."),
 ],
 "questions": [
  Q("Ποια ερμηνεία της αυθαίρετης δόμησης θεωρεί ο πολεοδόμος βολική για το κράτος;", ["Ότι φταίει η οικονομική κρίση", "Ότι φταίει η ασυνειδησία του πολίτη", "Ότι φταίνε οι μηχανικοί", "Ότι φταίει ο τουρισμός"], 1, "Είναι εύκολο να την αποδώσουμε στην ασυνειδησία του πολίτη, αλλά αυτή η ερμηνεία βολεύει κυρίως το κράτος"),
  Q("Γιατί, κατά τον ομιλητή, το κράτος έκανε τα στραβά μάτια;", ["Γιατί δεν γνώριζε το πρόβλημα", "Γιατί έτσι λυνόταν ένα στεγαστικό πρόβλημα που το ίδιο δεν μπορούσε να λύσει", "Γιατί το ζητούσε η Ευρωπαϊκή Ένωση", "Γιατί δεν είχε αρκετούς υπαλλήλους"], 1, "έτσι λυνόταν ένα πρόβλημα που το ίδιο δεν μπορούσε να λύσει"),
  Q("Τι προτείνει για τις νομιμοποιήσεις;", ["Να καταργηθούν εντελώς", "Να συνδέονται με πραγματικές βελτιώσεις των κτιρίων και της πόλης", "Να γκρεμιστούν όλα τα αυθαίρετα", "Να γίνουν πιο φτηνές"], 1, "η τακτοποίηση πρέπει να συνδέεται με πραγματικές βελτιώσεις"),
 ],
 "gloss": {"πολεοδόμος": "πολεοδόμος — town planner", "δόμηση": "δόμηση — building, construction", "ιδιαιτερότητα": "ιδιαιτερότητα — peculiarity", "ελάττωμα": "ελάττωμα — defect, flaw", "ασυνειδησία": "ασυνειδησία — lack of conscience, irresponsibility", "έκανε τα στραβά μάτια": "κάνω τα στραβά μάτια — to turn a blind eye", "νομιμοποιήσεις": "νομιμοποίηση — legalisation", "φαύλος κύκλος": "φαύλος κύκλος — vicious circle", "ανεδαφικό": "ανεδαφικός — unrealistic", "στατική επάρκεια": "στατική επάρκεια — structural adequacy"},
})

rnd = random.Random(77)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-77.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
