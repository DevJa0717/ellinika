# Source for library/listening/listening-118.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l118.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l118-ann-parousiasi-vivliou", "title": "Παρουσίαση βιβλίου στο βιβλιοπωλείο", "title_en": "A book launch at the bookshop", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα βιβλιοπωλείο για την παρουσίαση ενός νέου μυθιστορήματος. Ακούτε μια ανακοίνωση.",
 "script": [
  L("Υπάλληλος", "f", "Καλησπέρα σας και ευχαριστούμε που ήρθατε τόσοι πολλοί. Η συγγραφέας μάς ενημέρωσε ότι έχει κολλήσει στην κίνηση και θα φτάσει με περίπου είκοσι λεπτά καθυστέρηση. Ζητούμε συγγνώμη για την αναμονή.", "Good evening and thank you for coming in such numbers. The author has let us know that she is stuck in traffic and will arrive about twenty minutes late. We apologise for the wait."),
  L("Υπάλληλος", "f", "Στο μεταξύ, σας προσφέρουμε ένα ποτήρι κρασί στον πρώτο όροφο. Η παρουσίαση θα διαρκέσει περίπου μία ώρα και στο τέλος θα υπάρχει χρόνος για ερωτήσεις από το κοινό.", "In the meantime, we offer you a glass of wine on the first floor. The presentation will last about an hour and at the end there will be time for questions from the audience."),
  L("Υπάλληλος", "f", "Η συγγραφέας θα υπογράφει αντίτυπα μόνο του καινούργιου της βιβλίου, όχι των παλαιότερων, γιατί δεν θα υπάρχει αρκετός χρόνος. Όσοι αγοράσουν το βιβλίο απόψε έχουν έκπτωση δεκαπέντε τοις εκατό.", "The author will sign copies of her new book only, not of her older ones, because there won't be enough time. Those who buy the book tonight get a fifteen per cent discount."),
 ],
 "questions": [
  Q("Γιατί θα αργήσει η συγγραφέας;", ["Γιατί είναι άρρωστη", "Γιατί έχει κολλήσει στην κίνηση", "Γιατί άλλαξε η ώρα της εκδήλωσης", "Γιατί έχασε το τρένο"], 1, "έχει κολλήσει στην κίνηση"),
  Q("Τι προσφέρει το βιβλιοπωλείο στο μεταξύ;", ["Ένα ποτήρι κρασί στον πρώτο όροφο", "Δωρεάν βιβλία", "Καφέ και γλυκά", "Μια ξενάγηση στο βιβλιοπωλείο"], 0, "σας προσφέρουμε ένα ποτήρι κρασί στον πρώτο όροφο"),
  Q("Ποια βιβλία θα υπογράφει η συγγραφέας;", ["Όλα τα βιβλία της", "Μόνο τα παλαιότερα", "Όσα φέρει το κοινό από το σπίτι", "Μόνο το καινούργιο της βιβλίο"], 3, "θα υπογράφει αντίτυπα μόνο του καινούργιου της βιβλίου"),
 ],
 "gloss": {"παρουσίαση": "παρουσίαση — (book) launch, presentation", "μυθιστορήματος": "μυθιστόρημα — novel", "συγγραφέας": "συγγραφέας — author", "κολλήσει": "κολλάω στην κίνηση — to get stuck in traffic", "αναμονή": "αναμονή — wait", "Στο μεταξύ": "στο μεταξύ — in the meantime", "διαρκέσει": "διαρκώ — to last", "υπογράφει": "υπογράφω — to sign", "αντίτυπα": "αντίτυπο — copy (of a book)", "έκπτωση": "έκπτωση — discount"}
})

ITEMS.append({
 "id": "l118-vm-oreivatikos-syllogos", "title": "Μήνυμα από τον ορειβατικό σύλλογο", "title_en": "A message from the mountaineering club", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δηλώσει συμμετοχή σε μια ορειβατική εξόρμηση. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Αρχηγός", "m", "Γεια σας, ο Νίκος είμαι από τον ορειβατικό σύλλογο, ο αρχηγός της κυριακάτικης εξόρμησης. Σας ενημερώνω ότι αλλάζουμε διαδρομή. Η πρόγνωση δείχνει δυνατούς ανέμους στην κορυφή, οπότε δεν θα ανέβουμε ως εκεί. Θα κάνουμε μια χαμηλότερη διαδρομή μέσα στο φαράγγι.", "Hello, this is Nikos from the mountaineering club, the leader of Sunday's outing. I'm letting you know that we're changing route. The forecast shows strong winds on the summit, so we won't go up that far. We'll do a lower route through the gorge."),
  L("Αρχηγός", "m", "Επειδή η νέα διαδρομή είναι μεγαλύτερη, το λεωφορείο θα φύγει μισή ώρα νωρίτερα, στις έξι και μισή, από το ίδιο σημείο. Μην ξεχάσετε φακό κεφαλής, γιατί ίσως επιστρέψουμε όταν θα έχει σκοτεινιάσει.", "Because the new route is longer, the coach will leave half an hour earlier, at half past six, from the same place. Don't forget a head torch, because we may return after it has got dark."),
  L("Αρχηγός", "m", "Στο φαράγγι θα διασχίσουμε δύο φορές το ρέμα, οπότε καλό είναι να έχετε μαζί ένα δεύτερο ζευγάρι κάλτσες. Αν δεν σας βολεύει η αλλαγή, πείτε μου ως την Παρασκευή για να σας επιστρέψουμε τα χρήματα.", "In the gorge we'll cross the stream twice, so it's a good idea to bring a second pair of socks. If the change doesn't suit you, tell me by Friday so that we can refund your money."),
 ],
 "questions": [
  Q("Γιατί αλλάζει η διαδρομή;", ["Γιατί έκλεισε το μονοπάτι", "Γιατί η πρόγνωση δείχνει δυνατούς ανέμους στην κορυφή", "Γιατί δήλωσαν λίγοι συμμετοχή", "Γιατί χάλασε το λεωφορείο"], 1, "Η πρόγνωση δείχνει δυνατούς ανέμους στην κορυφή"),
  Q("Γιατί πρέπει να έχουν μαζί φακό κεφαλής;", ["Γιατί θα περάσουν από σπηλιά", "Γιατί θα ξεκινήσουν πριν ξημερώσει", "Γιατί ίσως επιστρέψουν όταν θα έχει σκοτεινιάσει", "Γιατί το ζητά ο κανονισμός του συλλόγου"], 2, "ίσως επιστρέψουμε όταν θα έχει σκοτεινιάσει"),
  Q("Τι πρέπει να κάνουν όσοι δεν θέλουν τη νέα διαδρομή;", ["Να το πουν ως την Παρασκευή για να πάρουν πίσω τα χρήματα", "Να έρθουν στο γραφείο του συλλόγου", "Να πάνε μόνοι τους στην κορυφή", "Να στείλουν ένα μήνυμα την Κυριακή"], 0, "πείτε μου ως την Παρασκευή για να σας επιστρέψουμε τα χρήματα"),
 ],
 "gloss": {"ορειβατικό": "ορειβατικός — mountaineering (adj.)", "εξόρμηση": "εξόρμηση — outing, excursion", "αρχηγός": "αρχηγός — leader", "κορυφή": "κορυφή — summit, peak", "φαράγγι": "φαράγγι — gorge", "φακό κεφαλής": "φακός κεφαλής — head torch", "σκοτεινιάσει": "σκοτεινιάζει — it gets dark", "διασχίσουμε": "διασχίζω — to cross", "ρέμα": "ρέμα — stream", "βολεύει": "με βολεύει — it suits me"}
})

ITEMS.append({
 "id": "l118-dial-protos-choros", "title": "Ο πρώτος χορός στον γάμο μας", "title_en": "The first dance at our wedding", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι που θα παντρευτεί σε δύο μήνες, ο Άρης και η Φωτεινή, συζητά για τον πρώτο χορό στον γάμο.",
 "script": [
  L("Φωτεινή", "f", "Άρη, η αδερφή μου λέει ότι πρέπει να κάνουμε μαθήματα χορού για τον γάμο. Στον δικό της γάμο έκαναν ταγκό και όλοι ακόμα το θυμούνται.", "Aris, my sister says we should take dance lessons for the wedding. At her wedding they did a tango and everyone still remembers it."),
  L("Άρης", "m", "Ακριβώς γι’ αυτό δεν θέλω. Δεν θέλω να μας συγκρίνουν. Και ξέρεις ότι εγώ χορεύω σαν ντουλάπα. Γιατί να μη χορέψουμε απλώς ένα βαλς, κάτι απλό;", "That's exactly why I don't want to. I don't want them to compare us. And you know I dance like a wardrobe. Why don't we just dance a waltz, something simple?"),
  L("Φωτεινή", "f", "Ακόμα και για το βαλς χρειαζόμαστε λίγη εξάσκηση. Δεν λέω να γίνουμε επαγγελματίες. Πέντε μαθήματα, όσο για να μην πατάς τα πόδια μου μπροστά σε διακόσιους καλεσμένους.", "Even for the waltz we need a bit of practice. I'm not saying we should become professionals. Five lessons, just enough so you don't step on my feet in front of two hundred guests."),
  L("Άρης", "m", "Εντάξει, αυτό είναι λογικό. Αλλά να ξέρεις, μετά το βαλς θέλω να ακολουθήσει αμέσως ένα συρτό, να σηκωθεί όλος ο κόσμος και να σταματήσουν να κοιτάνε εμάς.", "OK, that's reasonable. But you should know, after the waltz I want a syrtos to follow straight away, so that everyone gets up and stops looking at us."),
  L("Φωτεινή", "f", "Συμφωνώ. Θα πω στην ορχήστρα να είναι έτοιμη. Και θα βρω μια σχολή κοντά στη δουλειά σου, για να μην έχεις δικαιολογίες.", "Agreed. I'll tell the band to be ready. And I'll find a school near your work, so you have no excuses."),
 ],
 "questions": [
  Q("Γιατί ο Άρης δεν θέλει να χορέψουν ταγκό;", ["Γιατί δεν του αρέσει η μουσική", "Γιατί δεν θέλει να τους συγκρίνουν με την αδερφή της Φωτεινής", "Γιατί είναι πολύ ακριβά τα μαθήματα", "Γιατί έχει πρόβλημα στο πόδι"], 1, "Δεν θέλω να μας συγκρίνουν"),
  Q("Πόσα μαθήματα προτείνει η Φωτεινή;", ["Πέντε", "Δέκα", "Ένα", "Είκοσι"], 0, "Πέντε μαθήματα"),
  Q("Τι θέλει ο Άρης να γίνει αμέσως μετά το βαλς;", ["Να κόψουν την τούρτα", "Να βγάλουν φωτογραφίες", "Να ακολουθήσει ένα συρτό για να σηκωθεί όλος ο κόσμος", "Να κάνουν μια ομιλία"], 2, "μετά το βαλς θέλω να ακολουθήσει αμέσως ένα συρτό"),
 ],
 "gloss": {"παντρευτεί": "παντρεύομαι — to get married", "ταγκό": "ταγκό — tango", "συγκρίνουν": "συγκρίνω — to compare", "βαλς": "βαλς — waltz", "εξάσκηση": "εξάσκηση — practice", "επαγγελματίες": "επαγγελματίας — professional", "καλεσμένους": "καλεσμένος — guest", "συρτό": "συρτός — syrtos (Greek circle dance)", "ορχήστρα": "ορχήστρα — band, orchestra", "δικαιολογίες": "δικαιολογία — excuse"}
})

ITEMS.append({
 "id": "l118-int-ypotitlistria", "title": "Μια μεταφράστρια υποτίτλων", "title_en": "A subtitle translator", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια μεταφράστρια υποτίτλων σε ραδιοφωνική εκπομπή για τα επαγγέλματα.",
 "script": [
  L("Δημοσιογράφος", "m", "Όλοι διαβάζουμε υπότιτλους, αλλά λίγοι σκεφτόμαστε ποιος τους γράφει. Πόσο δύσκολο είναι;", "We all read subtitles, but few of us think about who writes them. How difficult is it?"),
  L("Μεταφράστρια", "f", "Πιο δύσκολο απ’ ό,τι φαίνεται. Δεν μεταφράζω απλώς τον διάλογο. Έχω περιορισμένο χώρο, συνήθως δύο γραμμές, και λίγα δευτερόλεπτα, γιατί ο θεατής πρέπει να προλάβει να διαβάσει και να δει την εικόνα. Έτσι, πολλές φορές πρέπει να συντομεύσω μια φράση χωρίς να χαθεί το νόημα.", "Harder than it looks. I don't simply translate the dialogue. I have limited space, usually two lines, and a few seconds, because the viewer has to manage to read and watch the picture. So I often have to shorten a sentence without losing the meaning."),
  L("Δημοσιογράφος", "m", "Τι σας δυσκολεύει περισσότερο;", "What do you find hardest?"),
  L("Μεταφράστρια", "f", "Τα αστεία και τα λογοπαίγνια. Ένα αστείο που βασίζεται σε μια λέξη της αγγλικής συχνά δεν λειτουργεί καθόλου στα ελληνικά. Τότε πρέπει να εφεύρω ένα καινούργιο αστείο, που να ταιριάζει με την εικόνα. Αν ο ηθοποιός δείχνει ένα μήλο, δεν μπορώ να κάνω αστείο με πορτοκάλια.", "Jokes and puns. A joke that's based on an English word often doesn't work at all in Greek. Then I have to invent a new joke that fits the picture. If the actor is pointing at an apple, I can't make a joke about oranges."),
  L("Δημοσιογράφος", "m", "Και η πίεση του χρόνου;", "And time pressure?"),
  L("Μεταφράστρια", "f", "Είναι μεγάλη. Για μια σειρά που βγαίνει ταυτόχρονα σε όλο τον κόσμο, μπορεί να έχω μόνο λίγες μέρες για μια ολόκληρη σεζόν. Η καλύτερη αναγνώριση, πάντως, είναι όταν κανείς δεν προσέχει τους υπότιτλους. Σημαίνει ότι έκανα καλά τη δουλειά μου.", "It's huge. For a series that comes out at the same time all over the world, I may have only a few days for a whole season. The best recognition, though, is when nobody notices the subtitles. It means I did my job well."),
 ],
 "questions": [
  Q("Γιατί πρέπει συχνά να συντομεύει τις φράσεις;", ["Γιατί το ζητούν οι ηθοποιοί", "Γιατί έχει περιορισμένο χώρο και λίγα δευτερόλεπτα", "Γιατί τα ελληνικά είναι πιο σύντομα", "Γιατί πληρώνεται ανά λέξη"], 1, "Έχω περιορισμένο χώρο, συνήθως δύο γραμμές, και λίγα δευτερόλεπτα"),
  Q("Τι κάνει όταν ένα αστείο δεν λειτουργεί στα ελληνικά;", ["Το αφήνει στα αγγλικά", "Το παραλείπει", "Εφευρίσκει ένα καινούργιο αστείο που να ταιριάζει με την εικόνα", "Βάζει μια σημείωση στο κάτω μέρος της οθόνης"], 2, "πρέπει να εφεύρω ένα καινούργιο αστείο, που να ταιριάζει με την εικόνα"),
  Q("Ποια θεωρεί την καλύτερη αναγνώριση της δουλειάς της;", ["Όταν κανείς δεν προσέχει τους υπότιτλους", "Όταν παίρνει βραβείο", "Όταν οι θεατές τη συγχαίρουν", "Όταν τελειώνει γρήγορα"], 0, "όταν κανείς δεν προσέχει τους υπότιτλους"),
 ],
 "gloss": {"υπότιτλους": "υπότιτλος — subtitle", "μεταφράστρια": "μεταφράστρια — translator (female)", "περιορισμένο": "περιορισμένος — limited", "προλάβει": "προλαβαίνω — to manage (in time)", "συντομεύσω": "συντομεύω — to shorten", "λογοπαίγνια": "λογοπαίγνιο — pun, wordplay", "εφεύρω": "εφευρίσκω — to invent", "ταυτόχρονα": "ταυτόχρονα — at the same time", "σεζόν": "σεζόν — season (of a series)", "αναγνώριση": "αναγνώριση — recognition"}
})

ITEMS.append({
 "id": "l118-rep-scholeio-choris-tsantes", "title": "Ένα σχολείο χωρίς βαριές τσάντες", "title_en": "A school without heavy schoolbags", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις τοπικές ειδήσεις.",
 "script": [
  L("Ρεπόρτερ", "f", "Στο δημοτικό σχολείο της γειτονιάς μας, οι μαθητές δεν κουβαλούν πια κάθε μέρα όλα τους τα βιβλία. Με χρήματα που μάζεψε ο σύλλογος γονέων από ένα χριστουγεννιάτικο παζάρι, τοποθετήθηκαν σε κάθε τάξη μικρά ντουλαπάκια με κλειδαριά.", "At our neighbourhood primary school, the pupils no longer carry all their books every day. With money the parents' association raised at a Christmas bazaar, small lockable cupboards have been installed in every classroom."),
  L("Ρεπόρτερ", "f", "Η ιδέα ξεκίνησε όταν μια μητέρα, φυσικοθεραπεύτρια στο επάγγελμα, ζύγισε τις τσάντες των παιδιών μιας τάξης. Κάποιες ζύγιζαν πάνω από επτά κιλά. Οι γιατροί συχνά συστήνουν η τσάντα να μην ξεπερνά περίπου το δέκα τοις εκατό του βάρους του παιδιού.", "The idea started when a mother, a physiotherapist by profession, weighed the bags of the children in one class. Some weighed over seven kilos. Doctors often recommend that a schoolbag shouldn't exceed about ten per cent of the child's weight."),
  L("Ρεπόρτερ", "f", "Τώρα τα παιδιά παίρνουν στο σπίτι μόνο τα βιβλία που χρειάζονται για τα μαθήματα της επόμενης μέρας. Οι δάσκαλοι λένε ότι στην αρχή κάποιοι μαθητές ξεχνούσαν τα βιβλία τους, αλλά μέσα σε έναν μήνα όλοι συνήθισαν το νέο σύστημα.", "Now the children take home only the books they need for the next day's lessons. The teachers say that at first some pupils forgot their books, but within a month everyone got used to the new system."),
 ],
 "questions": [
  Q("Πώς βρέθηκαν τα χρήματα για τα ντουλαπάκια;", ["Από τον δήμο", "Από ένα χριστουγεννιάτικο παζάρι του συλλόγου γονέων", "Από μια εταιρεία", "Από το υπουργείο"], 1, "Με χρήματα που μάζεψε ο σύλλογος γονέων από ένα χριστουγεννιάτικο παζάρι"),
  Q("Τι έκανε η μητέρα που ξεκίνησε την ιδέα;", ["Ζύγισε τις τσάντες των παιδιών μιας τάξης", "Έγραψε στον δήμαρχο", "Έφτιαξε τα ντουλαπάκια", "Έκανε μια ομιλία στο σχολείο"], 0, "ζύγισε τις τσάντες των παιδιών μιας τάξης"),
  Q("Τι συνέβη στην αρχή, σύμφωνα με τους δασκάλους;", ["Χάθηκαν κάποια κλειδιά", "Οι γονείς διαμαρτυρήθηκαν", "Κάποια ντουλαπάκια χάλασαν", "Κάποιοι μαθητές ξεχνούσαν τα βιβλία τους"], 3, "στην αρχή κάποιοι μαθητές ξεχνούσαν τα βιβλία τους"),
 ],
 "gloss": {"κουβαλούν": "κουβαλάω — to carry", "σύλλογος γονέων": "σύλλογος γονέων — parents' association", "παζάρι": "παζάρι — bazaar, fair", "τοποθετήθηκαν": "τοποθετούμαι — to be installed, placed", "ντουλαπάκια": "ντουλαπάκι — small cupboard, locker", "κλειδαριά": "κλειδαριά — lock", "φυσικοθεραπεύτρια": "φυσικοθεραπεύτρια — physiotherapist (female)", "ζύγισε": "ζυγίζω — to weigh", "συστήνουν": "συστήνω — to recommend", "συνήθισαν": "συνηθίζω — to get used to"}
})

ITEMS.append({
 "id": "l118-rep-plateia-geitonias", "title": "Μια γειτονιά ξαναφτιάχνει την πλατεία της", "title_en": "A neighbourhood remakes its square", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε ραδιοφωνική εκπομπή για την πόλη.",
 "script": [
  L("Ρεπόρτερ", "m", "Για χρόνια, η μικρή πλατεία στο τέλος της οδού Φιλελλήνων ήταν ένας χώρος στάθμευσης χωρίς άδεια, με σπασμένα παγκάκια και ούτε ένα δέντρο. Πέρσι, μια ομάδα κατοίκων αποφάσισε ότι αυτό πρέπει να αλλάξει.", "For years, the little square at the end of Filellinon Street was an unauthorised car park, with broken benches and not a single tree. Last year, a group of residents decided this had to change."),
  L("Ρεπόρτερ", "m", "Αντί να περιμένουν τον δήμο, οργάνωσαν μια ψηφοφορία στη γειτονιά για το τι θα ήθελαν να γίνει. Οι περισσότεροι ψήφισαν για σκιά, μια βρύση και μια μικρή παιδική χαρά. Ο δήμος δέχτηκε να πληρώσει τα υλικά, αν οι κάτοικοι έκαναν μόνοι τους τη δουλειά.", "Instead of waiting for the council, they organised a vote in the neighbourhood on what they would like to see. Most voted for shade, a drinking fountain and a small playground. The council agreed to pay for the materials, if the residents did the work themselves."),
  L("Ρεπόρτερ", "m", "Επί τρία Σαββατοκύριακα, γείτονες κάθε ηλικίας φύτεψαν δέντρα, έβαψαν παγκάκια και έστρωσαν βότσαλα. Σήμερα η πλατεία γεμίζει τα απογεύματα. Το πιο σημαντικό, λέει μια κάτοικος, δεν είναι η πλατεία, αλλά ότι μάθαμε επιτέλους τα ονόματα των γειτόνων μας.", "For three weekends, neighbours of all ages planted trees, painted benches and laid pebbles. Today the square fills up in the afternoons. The most important thing, says one resident, isn't the square, but that we finally learned our neighbours' names."),
 ],
 "questions": [
  Q("Τι ήταν παλιά η πλατεία;", ["Μια λαϊκή αγορά", "Ένας χώρος στάθμευσης χωρίς άδεια", "Ένα γήπεδο", "Ένα οικόπεδο προς πώληση"], 1, "ήταν ένας χώρος στάθμευσης χωρίς άδεια"),
  Q("Με ποια προϋπόθεση δέχτηκε ο δήμος να πληρώσει τα υλικά;", ["Αν οι κάτοικοι πλήρωναν τα μισά", "Αν η πλατεία πάρει το όνομα του δημάρχου", "Αν οι κάτοικοι έκαναν μόνοι τους τη δουλειά", "Αν τελείωνε μέσα σε έναν μήνα"], 2, "αν οι κάτοικοι έκαναν μόνοι τους τη δουλειά"),
  Q("Ποιο είναι, κατά μια κάτοικο, το πιο σημαντικό αποτέλεσμα;", ["Ότι οι γείτονες έμαθαν επιτέλους ο ένας το όνομα του άλλου", "Ότι ανέβηκαν οι τιμές των σπιτιών", "Ότι η πλατεία είναι πιο όμορφη", "Ότι έχει πια σκιά"], 0, "μάθαμε επιτέλους τα ονόματα των γειτόνων μας"),
 ],
 "gloss": {"στάθμευσης": "στάθμευση — parking", "παγκάκια": "παγκάκι — bench", "ψηφοφορία": "ψηφοφορία — vote", "βρύση": "βρύση — (drinking) fountain, tap", "παιδική χαρά": "παιδική χαρά — playground", "υλικά": "υλικό — material", "φύτεψαν": "φυτεύω — to plant", "έβαψαν": "βάφω — to paint", "έστρωσαν": "στρώνω — to lay (a surface)", "βότσαλα": "βότσαλο — pebble"}
})

ITEMS.append({
 "id": "l118-mon-iaponia-choris-glossa", "title": "Ένας μήνας στην Ιαπωνία χωρίς να ξέρω τη γλώσσα", "title_en": "A month in Japan without knowing the language", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν νεαρό να διηγείται ένα ταξίδι του σε ένα ταξιδιωτικό podcast.",
 "script": [
  L("Ταξιδιώτης", "m", "Πριν φύγω για την Ιαπωνία, είχα μάθει μόνο τρεις λέξεις: καλημέρα, ευχαριστώ και συγγνώμη. Αποδείχτηκε ότι η τρίτη ήταν η πιο χρήσιμη. Τις πρώτες μέρες χανόμουν συνέχεια στους σταθμούς του μετρό, που ήταν τεράστιοι σαν πόλεις.", "Before I left for Japan, I had learned only three words: good morning, thank you and sorry. The third turned out to be the most useful. In the first days I kept getting lost in the metro stations, which were as huge as cities."),
  L("Ταξιδιώτης", "m", "Αυτό που με εντυπωσίασε περισσότερο ήταν η ησυχία. Στα τρένα κανείς δεν μιλούσε στο κινητό, και όταν εγώ γέλασα δυνατά με κάτι, ένιωσα δέκα βλέμματα πάνω μου. Από τότε μάθαινα παρατηρώντας τι έκαναν οι άλλοι.", "What impressed me most was the quiet. On the trains nobody spoke on their phone, and when I laughed loudly at something, I felt ten pairs of eyes on me. From then on I learned by watching what the others did."),
  L("Ταξιδιώτης", "m", "Μια μέρα ξέχασα την ομπρέλα μου σε ένα καφέ. Γύρισα δύο ώρες αργότερα, χωρίς πολλές ελπίδες, και η σερβιτόρα μού την έδωσε τυλιγμένη σε σακούλα, με ένα χαμόγελο. Εκεί κατάλαβα ότι μπορείς να συνεννοηθείς με τους ανθρώπους και χωρίς κοινή γλώσσα.", "One day I left my umbrella in a café. I went back two hours later, without much hope, and the waitress handed it to me wrapped in a bag, with a smile. That's when I realised you can communicate with people even without a common language."),
 ],
 "questions": [
  Q("Ποια λέξη αποδείχτηκε η πιο χρήσιμη;", ["Το «καλημέρα»", "Το «συγγνώμη»", "Το «ευχαριστώ»", "Το «αντίο»"], 1, "Αποδείχτηκε ότι η τρίτη ήταν η πιο χρήσιμη"),
  Q("Τι τον εντυπωσίασε περισσότερο;", ["Οι τιμές", "Το φαγητό", "Η ησυχία", "Τα ψηλά κτίρια"], 2, "Αυτό που με εντυπωσίασε περισσότερο ήταν η ησυχία"),
  Q("Τι έγινε με την ομπρέλα του;", ["Η σερβιτόρα τού την έδωσε τυλιγμένη σε σακούλα", "Την έκλεψαν", "Τη βρήκε στο μετρό", "Αγόρασε καινούργια"], 0, "η σερβιτόρα μού την έδωσε τυλιγμένη σε σακούλα"),
 ],
 "gloss": {"Αποδείχτηκε": "αποδεικνύομαι — to turn out, prove to be", "χρήσιμη": "χρήσιμος — useful", "χανόμουν": "χάνομαι — to get lost", "τεράστιοι": "τεράστιος — huge", "εντυπωσίασε": "εντυπωσιάζω — to impress", "ησυχία": "ησυχία — quiet, peace", "βλέμματα": "βλέμμα — look, gaze", "παρατηρώντας": "παρατηρώ — to observe, watch", "τυλιγμένη": "τυλιγμένος — wrapped", "συνεννοηθείς": "συνεννοούμαι — to communicate, make oneself understood"}
})

ITEMS.append({
 "id": "l118-mon-chelonaki", "title": "Η νύχτα που ένα χελωνάκι βρήκε τη θάλασσα", "title_en": "The night a baby turtle found the sea", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια φοιτήτρια να μιλά για την εμπειρία της ως εθελόντρια σε ένα πρόγραμμα προστασίας της θαλάσσιας χελώνας.",
 "script": [
  L("Φοιτήτρια", "f", "Το περασμένο καλοκαίρι πέρασα έναν μήνα ως εθελόντρια σε μια παραλία όπου γεννάει η θαλάσσια χελώνα καρέτα. Κάθε πρωί περπατούσαμε την ακτή πριν ξημερώσει, για να βρούμε τα ίχνη που αφήνουν οι χελώνες στην άμμο όταν βγαίνουν να γεννήσουν.", "Last summer I spent a month as a volunteer on a beach where the loggerhead sea turtle lays its eggs. Every morning we walked the shore before dawn, to find the tracks the turtles leave in the sand when they come out to lay."),
  L("Φοιτήτρια", "f", "Όταν βρίσκαμε μια φωλιά, τη σημαδεύαμε και βάζαμε από πάνω ένα προστατευτικό πλέγμα. Ο μεγαλύτερος κίνδυνος για τα χελωνάκια είναι τα φώτα: όταν βγαίνουν από το αυγό, κινούνται προς το πιο φωτεινό σημείο, που κανονικά είναι η θάλασσα. Αν όμως υπάρχει ένα φωτισμένο μπαρ, πηγαίνουν προς τα εκεί.", "When we found a nest, we marked it and put a protective grid over it. The biggest danger for the hatchlings is lights: when they come out of the egg, they move towards the brightest point, which is normally the sea. But if there's a lit-up bar, they head that way."),
  L("Φοιτήτρια", "f", "Μια νύχτα είδα ένα χελωνάκι που είχε πάρει λάθος δρόμο. Δεν επιτρέπεται να τα σηκώνουμε με τα χέρια, οπότε στάθηκα ανάμεσα σε αυτό και στα φώτα, για να του κρύψω τη λάμψη. Όταν επιτέλους το είδα να το παίρνει το πρώτο κύμα, έκλαψα σαν μικρό παιδί.", "One night I saw a hatchling that had taken the wrong way. We're not allowed to pick them up by hand, so I stood between it and the lights, to hide the glare from it. When I finally saw the first wave take it, I cried like a little child."),
 ],
 "questions": [
  Q("Γιατί περπατούσαν την ακτή κάθε πρωί πριν ξημερώσει;", ["Για να μαζέψουν σκουπίδια", "Για να βρουν τα ίχνη των χελωνών στην άμμο", "Για να μετρήσουν τους λουόμενους", "Για να ταΐσουν τις χελώνες"], 1, "για να βρούμε τα ίχνη που αφήνουν οι χελώνες στην άμμο"),
  Q("Ποιος είναι ο μεγαλύτερος κίνδυνος για τα χελωνάκια, σύμφωνα με τη φοιτήτρια;", ["Οι γλάροι", "Τα κύματα", "Τα φώτα", "Οι ομπρέλες της παραλίας"], 2, "Ο μεγαλύτερος κίνδυνος για τα χελωνάκια είναι τα φώτα"),
  Q("Τι έκανε όταν είδε ένα χελωνάκι να παίρνει λάθος δρόμο;", ["Στάθηκε ανάμεσα σε αυτό και στα φώτα", "Το σήκωσε και το πήγε στη θάλασσα", "Φώναξε τον υπεύθυνο", "Έσβησε τα φώτα του μπαρ"], 0, "στάθηκα ανάμεσα σε αυτό και στα φώτα"),
 ],
 "gloss": {"εθελόντρια": "εθελόντρια — volunteer (female)", "γεννάει": "γεννάω — to lay (eggs); to give birth", "καρέτα": "καρέτα — loggerhead turtle", "ξημερώσει": "ξημερώνει — dawn breaks", "ίχνη": "ίχνος — track, trace", "φωλιά": "φωλιά — nest", "πλέγμα": "πλέγμα — grid, mesh", "χελωνάκια": "χελωνάκι — baby turtle, hatchling", "λάμψη": "λάμψη — glare, glow", "κύμα": "κύμα — wave"}
})

ITEMS.append({
 "id": "l118-c1-cheironomies", "title": "Γιατί χειρονομούμε όταν μιλάμε;", "title_en": "Why do we gesture when we speak?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια γλωσσολόγο σε μια διάλεξη για την επικοινωνία.",
 "script": [
  L("Γλωσσολόγος", "f", "Παρατηρήστε κάποιον που μιλά στο τηλέφωνο: κουνά τα χέρια του, παρόλο που ο συνομιλητής του δεν μπορεί να τον δει. Αν οι χειρονομίες υπήρχαν μόνο για τους άλλους, αυτό δεν θα είχε κανένα νόημα. Το γεγονός ότι το κάνουμε ούτως ή άλλως δείχνει ότι χειρονομούμε, σε μεγάλο βαθμό, και για τον εαυτό μας.", "Watch someone talking on the phone: they move their hands, even though the person they're talking to can't see them. If gestures existed only for others, that would make no sense. The fact that we do it anyway shows that we gesture, to a large extent, for ourselves too."),
  L("Γλωσσολόγος", "f", "Ακόμη πιο εντυπωσιακό είναι ότι άνθρωποι τυφλοί από τη γέννησή τους χειρονομούν όταν μιλούν, ακόμη και σε άλλους τυφλούς. Δεν έχουν δει ποτέ κανέναν να χειρονομεί. Αυτό υποδηλώνει ότι η κίνηση των χεριών είναι στενά δεμένη με την ίδια τη σκέψη και την ομιλία.", "Even more striking is that people blind from birth gesture when they speak, even to other blind people. They have never seen anyone gesture. This suggests that hand movement is closely tied to thought and speech themselves."),
  L("Γλωσσολόγος", "f", "Σε ορισμένα πειράματα, όταν οι συμμετέχοντες δεν μπορούσαν να κουνήσουν τα χέρια τους, φάνηκε να δυσκολεύονται περισσότερο να βρουν τις λέξεις, κυρίως όταν περιέγραφαν χώρους και κινήσεις. Τα αποτελέσματα δεν είναι πάντα ομόφωνα, αλλά η τάση είναι σαφής.", "In some experiments, when participants couldn't move their hands, they seemed to have more trouble finding words, especially when describing spaces and movements. The results are not always unanimous, but the trend is clear."),
  L("Γλωσσολόγος", "f", "Βέβαια, οι χειρονομίες έχουν και πολιτισμικές διαστάσεις. Η ίδια κίνηση μπορεί να είναι αθώα σε μια χώρα και βαριά προσβολή σε μια άλλη. Γι’ αυτό, όταν μαθαίνουμε μια ξένη γλώσσα, αξίζει να μαθαίνουμε και τα χέρια της.", "Of course, gestures also have cultural dimensions. The same movement can be innocent in one country and a grave insult in another. That's why, when we learn a foreign language, it's worth learning its hands too."),
 ],
 "questions": [
  Q("Τι δείχνει, κατά την ομιλήτρια, το ότι χειρονομούμε στο τηλέφωνο;", ["Ότι είμαστε αγχωμένοι", "Ότι χειρονομούμε σε μεγάλο βαθμό και για τον εαυτό μας", "Ότι θέλουμε να μας δουν", "Ότι μιλάμε πιο δυνατά"], 1, "χειρονομούμε, σε μεγάλο βαθμό, και για τον εαυτό μας"),
  Q("Τι υποδηλώνει το παράδειγμα των ανθρώπων που είναι τυφλοί από τη γέννησή τους;", ["Ότι οι χειρονομίες μαθαίνονται μόνο με την παρατήρηση", "Ότι οι τυφλοί χειρονομούν λιγότερο", "Ότι η κίνηση των χεριών είναι στενά δεμένη με τη σκέψη και την ομιλία", "Ότι οι χειρονομίες είναι ίδιες σε όλο τον κόσμο"], 2, "η κίνηση των χεριών είναι στενά δεμένη με την ίδια τη σκέψη και την ομιλία"),
  Q("Τι συνέβαινε σε ορισμένα πειράματα όταν οι συμμετέχοντες δεν μπορούσαν να κουνήσουν τα χέρια τους;", ["Μιλούσαν πιο γρήγορα", "Ξεχνούσαν την ερώτηση", "Δεν άλλαζε τίποτα", "Φαίνονταν να δυσκολεύονται περισσότερο να βρουν τις λέξεις"], 3, "φάνηκε να δυσκολεύονται περισσότερο να βρουν τις λέξεις"),
  Q("Τι συμβουλεύει η ομιλήτρια όσους μαθαίνουν μια ξένη γλώσσα;", ["Να μαθαίνουν και τις χειρονομίες της", "Να μη χειρονομούν καθόλου", "Να μιλούν μόνο στο τηλέφωνο", "Να αποφεύγουν τις χώρες με διαφορετικές χειρονομίες"], 0, "αξίζει να μαθαίνουμε και τα χέρια της"),
 ],
 "gloss": {"χειρονομούμε": "χειρονομώ — to gesture", "συνομιλητής": "συνομιλητής — interlocutor, the person one is talking to", "χειρονομίες": "χειρονομία — gesture", "ούτως ή άλλως": "ούτως ή άλλως — anyway, in any case", "εντυπωσιακό": "εντυπωσιακός — striking, impressive", "τυφλοί": "τυφλός — blind", "υποδηλώνει": "υποδηλώνω — to suggest, indicate", "ομόφωνα": "ομόφωνος — unanimous", "τάση": "τάση — trend, tendency", "πολιτισμικές": "πολιτισμικός — cultural", "προσβολή": "προσβολή — insult"}
})

ITEMS.append({
 "id": "l118-c1-trapezounta", "title": "Η αυτοκρατορία της Τραπεζούντας", "title_en": "The Empire of Trebizond", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια βυζαντινολόγο σε εκπομπή για τον μεσαιωνικό ελληνισμό.",
 "script": [
  L("Δημοσιογράφος", "m", "Όταν λέμε «τέλος του Βυζαντίου», σκεφτόμαστε το 1453. Εσείς όμως υποστηρίζετε ότι η ιστορία δεν τελειώνει εκεί.", "When we say \"the end of Byzantium\", we think of 1453. But you argue that the story doesn't end there."),
  L("Βυζαντινολόγος", "f", "Πράγματι. Το 1204, όταν οι σταυροφόροι κατέλαβαν την Κωνσταντινούπολη, η αυτοκρατορία διασπάστηκε σε μικρότερα κράτη. Ένα από αυτά ιδρύθηκε στην Τραπεζούντα, στις νότιες ακτές του Εύξεινου Πόντου, από δύο εγγονούς του αυτοκράτορα Ανδρόνικου Α΄ Κομνηνού, τον Αλέξιο και τον Δαβίδ. Τους βοήθησε η βασίλισσα Θάμαρ της Γεωργίας, με την οποία είχαν συγγένεια.", "Indeed. In 1204, when the Crusaders captured Constantinople, the empire broke up into smaller states. One of them was founded at Trebizond, on the southern shores of the Black Sea, by two grandsons of the emperor Andronikos I Komnenos, Alexios and David. They were helped by Queen Tamar of Georgia, to whom they were related."),
  L("Δημοσιογράφος", "m", "Και πώς κατάφερε να επιβιώσει τόσο καιρό ένα τόσο μικρό κράτος;", "And how did such a small state manage to survive for so long?"),
  L("Βυζαντινολόγος", "f", "Κυρίως με την οικονομία και τη διπλωματία. Η Τραπεζούντα βρισκόταν στο τέρμα εμπορικών δρόμων από την Περσία και την Κεντρική Ασία, και οι Γενουάτες και οι Βενετοί είχαν εκεί εμπορικούς σταθμούς. Οι αυτοκράτορές της, εξάλλου, πάντρευαν τις κόρες τους, που ήταν φημισμένες για την ομορφιά τους, με γειτονικούς ηγεμόνες, εξασφαλίζοντας έτσι συμμαχίες.", "Mainly through trade and diplomacy. Trebizond lay at the end of trade routes from Persia and Central Asia, and the Genoese and the Venetians had trading posts there. Its emperors, moreover, married their daughters, who were famed for their beauty, to neighbouring rulers, thus securing alliances."),
  L("Δημοσιογράφος", "m", "Πότε έπεσε τελικά;", "When did it finally fall?"),
  L("Βυζαντινολόγος", "f", "Το 1461, οκτώ χρόνια μετά την Κωνσταντινούπολη, όταν ο Μωάμεθ ο Πορθητής την κατέλαβε χωρίς μάχη. Ο ελληνισμός του Πόντου όμως επέζησε για αιώνες. Χαρακτηριστικό είναι το μοναστήρι της Παναγίας Σουμελά, κοντά στην Τραπεζούντα. Μετά την ανταλλαγή των πληθυσμών του 1923, οι πρόσφυγες ίδρυσαν μια νέα Παναγία Σουμελά στο Βέρμιο, στη Μακεδονία, όπου φυλάσσεται σήμερα η εικόνα της. Η μνήμη, όπως βλέπετε, μπορεί να ταξιδέψει μαζί με τους ανθρώπους.", "In 1461, eight years after Constantinople, when Mehmed the Conqueror took it without a battle. But the Hellenism of Pontus survived for centuries. A telling example is the monastery of Panagia Soumela, near Trebizond. After the population exchange of 1923, the refugees founded a new Panagia Soumela on Mount Vermio, in Macedonia, where its icon is kept today. Memory, as you see, can travel with people."),
 ],
 "questions": [
  Q("Ποιοι ίδρυσαν το κράτος της Τραπεζούντας;", ["Οι σταυροφόροι", "Δύο εγγονοί του αυτοκράτορα Ανδρόνικου Α΄ Κομνηνού", "Η βασίλισσα Θάμαρ", "Έμποροι από τη Γένουα"], 1, "από δύο εγγονούς του αυτοκράτορα Ανδρόνικου Α΄ Κομνηνού"),
  Q("Πώς επιβίωσε τόσο καιρό, σύμφωνα με τη βυζαντινολόγο;", ["Χάρη στον ισχυρό στρατό του", "Χάρη στα ψηλά τείχη", "Κυρίως με την οικονομία και τη διπλωματία", "Χάρη στη βοήθεια του Πάπα"], 2, "Κυρίως με την οικονομία και τη διπλωματία"),
  Q("Πώς έπεσε η Τραπεζούντα το 1461;", ["Ο Μωάμεθ ο Πορθητής την κατέλαβε χωρίς μάχη", "Μετά από πολιορκία δέκα χρόνων", "Από σεισμό", "Την πούλησαν στους Βενετούς"], 0, "ο Μωάμεθ ο Πορθητής την κατέλαβε χωρίς μάχη"),
  Q("Τι δείχνει, κατά την ομιλήτρια, η ιστορία της Παναγίας Σουμελά;", ["Ότι τα μοναστήρια είναι πάντα πλούσια", "Ότι η εικόνα χάθηκε το 1923", "Ότι το μοναστήρι χτίστηκε πρώτα στη Μακεδονία", "Ότι η μνήμη μπορεί να ταξιδέψει μαζί με τους ανθρώπους"], 3, "Η μνήμη, όπως βλέπετε, μπορεί να ταξιδέψει μαζί με τους ανθρώπους"),
 ],
 "gloss": {"σταυροφόροι": "σταυροφόρος — crusader", "κατέλαβαν": "καταλαμβάνω — to capture, seize", "διασπάστηκε": "διασπώμαι — to break up, split", "Εύξεινου Πόντου": "Εύξεινος Πόντος — the Black Sea", "εγγονούς": "εγγονός — grandson", "συγγένεια": "συγγένεια — kinship", "επιβιώσει": "επιβιώνω — to survive", "τέρμα": "τέρμα — end, terminus", "Γενουάτες": "Γενουάτης — Genoese", "ηγεμόνες": "ηγεμόνας — ruler", "Πορθητής": "πορθητής — conqueror", "ανταλλαγή των πληθυσμών": "ανταλλαγή των πληθυσμών — the population exchange (1923)"}
})

rnd = random.Random(118)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-118.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
