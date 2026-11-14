# Source for library/listening/listening-13.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l13.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l13-ann-marathonios", "title": "Κλειστοί δρόμοι για τον Μαραθώνιο", "title_en": "Roads closed for the Marathon", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση της Τροχαίας στο ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Η Τροχαία Αττικής ενημερώνει ότι, λόγω της διεξαγωγής του Αυθεντικού Μαραθωνίου της Αθήνας, την Κυριακή θα ισχύσουν εκτεταμένες κυκλοφοριακές ρυθμίσεις. Από τις πέντε το πρωί θα διακοπεί η κυκλοφορία στη λεωφόρο Μαραθώνος και στη Μεσογείων, καθώς και στους δρόμους γύρω από το Παναθηναϊκό Στάδιο.", "Attica Traffic Police announce that, because the Athens Authentic Marathon is taking place, extensive traffic arrangements will apply on Sunday. From five in the morning traffic will be stopped on Marathonos Avenue and on Mesogeion, as well as on the streets around the Panathenaic Stadium."),
  L("Εκφωνητής", "m", "Οι δρόμοι θα ανοίγουν σταδιακά, μόλις περάσει και ο τελευταίος δρομέας, οπότε η κυκλοφορία στο κέντρο αναμένεται να αποκατασταθεί πλήρως μετά τις τέσσερις το απόγευμα. Οι οδηγοί παρακαλούνται να μη σταθμεύουν τα οχήματά τους κατά μήκος της διαδρομής από το Σάββατο το βράδυ· όσα αυτοκίνητα βρεθούν σταθμευμένα θα απομακρυνθούν με γερανό.", "The roads will reopen gradually, as soon as the last runner has passed, so traffic in the centre is expected to be fully restored after four in the afternoon. Drivers are asked not to park their vehicles along the route from Saturday evening; any cars found parked will be towed away."),
  L("Εκφωνητής", "m", "Το μετρό θα λειτουργεί κανονικά και με πυκνότερα δρομολόγια, και το κοινό ενθαρρύνεται να το προτιμήσει για τις μετακινήσεις του.", "The metro will run normally and with more frequent services, and the public is encouraged to use it for their journeys."),
 ],
 "questions": [
  Q("Πότε αναμένεται να αποκατασταθεί πλήρως η κυκλοφορία στο κέντρο;", ["Στις πέντε το πρωί", "Το μεσημέρι", "Μετά τις τέσσερις το απόγευμα", "Τη Δευτέρα το πρωί"], 2, "μετά τις τέσσερις το απόγευμα"),
  Q("Τι θα συμβεί στα αυτοκίνητα που θα είναι παρκαρισμένα στη διαδρομή;", ["Θα πάρουν κλήση", "Θα απομακρυνθούν με γερανό", "Θα μείνουν εκεί μέχρι το βράδυ", "Θα μετακινηθούν από τους ιδιοκτήτες"], 1, "όσα αυτοκίνητα βρεθούν σταθμευμένα θα απομακρυνθούν με γερανό"),
  Q("Τι συνιστάται στο κοινό;", ["Να μείνει στο σπίτι", "Να χρησιμοποιήσει το μετρό", "Να μετακινηθεί με ταξί", "Να παρκάρει κοντά στο Στάδιο"], 1, "το κοινό ενθαρρύνεται να το προτιμήσει για τις μετακινήσεις του"),
 ],
 "gloss": {"Τροχαία": "Τροχαία — traffic police", "διεξαγωγής": "διεξαγωγή — holding, conduct (of an event)", "εκτεταμένες": "εκτεταμένος — extensive", "κυκλοφοριακές ρυθμίσεις": "κυκλοφοριακές ρυθμίσεις — traffic arrangements", "θα διακοπεί": "διακόπτομαι — to be interrupted, stopped", "σταδιακά": "σταδιακά — gradually", "δρομέας": "δρομέας — runner", "να αποκατασταθεί": "αποκαθίσταμαι — to be restored", "να μη σταθμεύουν": "σταθμεύω — to park (formal)", "κατά μήκος": "κατά μήκος — along", "γερανό": "γερανός — tow truck; crane", "πυκνότερα δρομολόγια": "πυκνά δρομολόγια — frequent services"},
})

ITEMS.append({
 "id": "l13-ann-laiki", "title": "Η λαϊκή αλλάζει δρόμο", "title_en": "The street market is moving", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση του δήμου από ένα αυτοκίνητο με μεγάφωνο.",
 "script": [
  L("Υπάλληλος", "m", "Ο Δήμος ενημερώνει τους κατοίκους ότι, λόγω των έργων αντικατάστασης του αγωγού ύδρευσης στην οδό Αγίου Νικολάου, η λαϊκή αγορά της Παρασκευής θα μεταφερθεί προσωρινά στην οδό Κύπρου, από την πλατεία έως το γυμναστήριο.", "The Municipality informs residents that, because of the works to replace the water main on Agiou Nikolaou Street, the Friday street market will be moved temporarily to Kyprou Street, from the square to the gym."),
  L("Υπάλληλος", "m", "Η μεταφορά θα ισχύσει από την επόμενη Παρασκευή και για τουλάχιστον έξι εβδομάδες. Οι κάτοικοι της οδού Κύπρου παρακαλούνται να μη σταθμεύουν τα αυτοκίνητά τους εκεί από τις πέντε το πρωί της Παρασκευής έως τις τρεις το απόγευμα.", "The move will apply from next Friday and for at least six weeks. Residents of Kyprou Street are asked not to park their cars there from five in the morning on Friday until three in the afternoon."),
  L("Υπάλληλος", "m", "Για τη διευκόλυνση των ηλικιωμένων, θα λειτουργεί δωρεάν δημοτικό λεωφορείο από το ΚΑΠΗ προς τη λαϊκή, κάθε μισή ώρα. Ο Δήμος ζητά την κατανόηση όλων για την προσωρινή ταλαιπωρία.", "To help elderly people, a free municipal bus will run from the senior citizens' centre to the market every half hour. The Municipality asks for everyone's understanding for the temporary inconvenience."),
 ],
 "questions": [
  Q("Γιατί μεταφέρεται η λαϊκή αγορά;", ["Λόγω παραπόνων των κατοίκων", "Λόγω έργων στον αγωγό ύδρευσης", "Γιατί η πλατεία ανακαινίζεται", "Γιατί αυξήθηκαν οι πάγκοι"], 1, "λόγω των έργων αντικατάστασης του αγωγού ύδρευσης"),
  Q("Τι ζητείται από τους κατοίκους της οδού Κύπρου;", ["Να μη σταθμεύουν στον δρόμο την Παρασκευή", "Να βοηθήσουν τους πωλητές", "Να κλείνουν τα παράθυρα", "Να πληρώσουν ένα τέλος"], 0, "παρακαλούνται να μη σταθμεύουν τα αυτοκίνητά τους εκεί"),
  Q("Τι θα προσφέρει ο Δήμος στους ηλικιωμένους;", ["Δωρεάν φρούτα", "Δωρεάν λεωφορείο προς τη λαϊκή", "Παράδοση των ψωνιών στο σπίτι", "Έκπτωση στους πάγκους"], 1, "θα λειτουργεί δωρεάν δημοτικό λεωφορείο από το ΚΑΠΗ προς τη λαϊκή"),
 ],
 "gloss": {"μεγάφωνο": "μεγάφωνο — loudspeaker", "αντικατάστασης": "αντικατάσταση — replacement", "αγωγού ύδρευσης": "αγωγός ύδρευσης — water main", "λαϊκή αγορά": "λαϊκή (αγορά) — weekly street market", "θα μεταφερθεί": "μεταφέρομαι — to be moved", "προσωρινά": "προσωρινά — temporarily", "σταθμεύουν": "σταθμεύω — to park (formal)", "διευκόλυνση": "διευκόλυνση — assistance, making easier", "ΚΑΠΗ": "ΚΑΠΗ — municipal day centre for older people", "κατανόηση": "κατανόηση — understanding", "ταλαιπωρία": "ταλαιπωρία — inconvenience, hassle"},
})

ITEMS.append({
 "id": "l13-vm-sxoleio", "title": "Τηλεφώνημα από το σχολείο", "title_en": "A call from school", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από τη διευθύντρια ενός δημοτικού σχολείου προς έναν πατέρα.",
 "script": [
  L("Διευθύντρια", "f", "Καλημέρα, κύριε Παπαδάκη, από το Τρίτο Δημοτικό σας παίρνω, είμαι η διευθύντρια, η κυρία Λιάπη. Μην ανησυχείτε, δεν είναι κάτι σοβαρό. Ο Γιαννάκης ανέβασε λίγο πυρετό στο δεύτερο διάλειμμα και λέει ότι πονάει ο λαιμός του.", "Good morning, Mr Papadakis, I'm calling from the Third Primary School, I'm the head teacher, Mrs Liapi. Don't worry, it's nothing serious. Giannakis developed a slight temperature in the second break and says his throat hurts."),
  L("Διευθύντρια", "f", "Τον έχουμε στο γραφείο μου, ξαπλωμένο, και του δώσαμε νερό. Σύμφωνα με τον κανονισμό, όμως, δεν μπορεί να μείνει στην τάξη με πυρετό, οπότε θα πρέπει κάποιος να έρθει να τον πάρει όσο το δυνατόν συντομότερα.", "We have him in my office, lying down, and we've given him water. According to the rules, though, he can't stay in class with a temperature, so someone will need to come and collect him as soon as possible."),
  L("Διευθύντρια", "f", "Δοκίμασα και στο κινητό της μητέρας του, αλλά δεν απαντάει. Αν δεν μπορείτε να έρθετε εσείς, πείτε μας ποιος θα έρθει, γιατί το παιδί το παραδίδουμε μόνο σε άτομα που έχετε δηλώσει στη φόρμα της αρχής της χρονιάς.", "I also tried his mother's mobile, but she isn't answering. If you can't come yourself, tell us who will come, because we only hand the child over to people you listed on the form at the start of the year."),
 ],
 "questions": [
  Q("Τι συμβαίνει στον Γιαννάκη;", ["Χτύπησε στο διάλειμμα", "Έχει λίγο πυρετό και πονάει ο λαιμός του", "Τσακώθηκε με έναν συμμαθητή", "Ξέχασε το φαγητό του"], 1, "ανέβασε λίγο πυρετό ... πονάει ο λαιμός του"),
  Q("Γιατί πρέπει να φύγει από το σχολείο;", ["Γιατί το ζήτησε ο ίδιος", "Γιατί ο κανονισμός δεν επιτρέπει να μείνει στην τάξη με πυρετό", "Γιατί τελείωσαν τα μαθήματα", "Γιατί πρέπει να πάει στο νοσοκομείο"], 1, "Σύμφωνα με τον κανονισμό ... δεν μπορεί να μείνει στην τάξη με πυρετό"),
  Q("Σε ποιον μπορεί να παραδοθεί το παιδί;", ["Σε οποιονδήποτε συγγενή", "Μόνο στη μητέρα", "Σε άτομα που έχουν δηλωθεί στη φόρμα του σχολείου", "Σε έναν δάσκαλο"], 2, "μόνο σε άτομα που έχετε δηλώσει στη φόρμα της αρχής της χρονιάς"),
 ],
 "gloss": {"διευθύντρια": "διευθύντρια — head teacher (f.)", "Δημοτικό": "δημοτικό (σχολείο) — primary school", "ανέβασε λίγο πυρετό": "ανεβάζω πυρετό — to run a temperature", "διάλειμμα": "διάλειμμα — break, recess", "πονάει ο λαιμός του": "με πονάει ο λαιμός — I have a sore throat", "ξαπλωμένο": "ξαπλωμένος — lying down", "κανονισμό": "κανονισμός — regulation, rules", "όσο το δυνατόν συντομότερα": "όσο το δυνατόν συντομότερα — as soon as possible", "παραδίδουμε": "παραδίδω — to hand over", "φόρμα": "φόρμα — form (document); tracksuit"},
})

ITEMS.append({
 "id": "l13-dia-metaxeirismeno", "title": "Ένα μεταχειρισμένο αυτοκίνητο", "title_en": "A used car", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση ανάμεσα σε έναν αγοραστή και μια πωλήτρια μεταχειρισμένων αυτοκινήτων.",
 "script": [
  L("Πωλήτρια", "f", "Αυτό εδώ είναι από τα καλύτερα που έχουμε. Δώδεκα χρονών, αλλά μόνο ενενήντα χιλιάδες χιλιόμετρα. Ένας ιδιοκτήτης, πάντα σε σέρβις.", "This one is one of the best we have. Twelve years old, but only ninety thousand kilometres. One owner, always serviced."),
  L("Τάσος", "m", "Ωραίο φαίνεται. Έχετε το βιβλίο του σέρβις; Θα ήθελα να δω πότε άλλαξε τελευταία φορά ο ιμάντας.", "It looks nice. Do you have the service book? I'd like to see when the timing belt was last changed."),
  L("Πωλήτρια", "f", "Βεβαίως. Πριν από δύο χρόνια, μαζί με τα λάστιχα. Θέλετε να το οδηγήσετε λίγο;", "Of course. Two years ago, together with the tyres. Would you like to drive it a bit?"),
  L("Τάσος", "m", "Ναι, αλλά πρώτα θα ήθελα να το δει και ένας μηχανικός της εμπιστοσύνης μου. Έχω ακούσει πολλές ιστορίες για χιλιόμετρα που «γυρίζουν πίσω».", "Yes, but first I'd like a mechanic I trust to look at it too. I've heard a lot of stories about kilometres that get \"turned back\"."),
  L("Πωλήτρια", "f", "Κανένα πρόβλημα, φέρτε όποιον θέλετε. Για την τιμή, τα τέσσερα χιλιάρικα είναι τελική τιμή, αλλά σας κάνουμε δώρο τη μεταβίβαση και τα τέλη κυκλοφορίας του επόμενου χρόνου.", "No problem, bring whoever you like. As for the price, four thousand is the final price, but we'll cover the transfer of ownership and next year's road tax for you."),
  L("Τάσος", "m", "Εντάξει. Θα έρθω το Σάββατο με τον μηχανικό, και αν όλα είναι εντάξει, κλείνουμε.", "OK. I'll come on Saturday with the mechanic, and if everything is fine, we have a deal."),
 ],
 "questions": [
  Q("Τι θέλει να ελέγξει ο Τάσος στο βιβλίο του σέρβις;", ["Πόσους ιδιοκτήτες είχε το αυτοκίνητο", "Πότε άλλαξε τελευταία φορά ο ιμάντας", "Αν το αυτοκίνητο έχει τρακάρει", "Την κατανάλωση καυσίμου"], 1, "Θα ήθελα να δω πότε άλλαξε τελευταία φορά ο ιμάντας."),
  Q("Γιατί θέλει να φέρει μηχανικό;", ["Γιατί δεν ξέρει να οδηγεί", "Γιατί φοβάται ότι τα χιλιόμετρα μπορεί να έχουν αλλοιωθεί", "Γιατί το ζήτησε η πωλήτρια", "Γιατί το αυτοκίνητο δεν παίρνει μπροστά"], 1, "Έχω ακούσει πολλές ιστορίες για χιλιόμετρα που «γυρίζουν πίσω»."),
  Q("Τι προσφέρει η πωλήτρια;", ["Έκπτωση πεντακοσίων ευρώ", "Τη μεταβίβαση και τα τέλη κυκλοφορίας του επόμενου χρόνου", "Καινούργια λάστιχα", "Δωρεάν σέρβις για δύο χρόνια"], 1, "σας κάνουμε δώρο τη μεταβίβαση και τα τέλη κυκλοφορίας του επόμενου χρόνου"),
 ],
 "gloss": {"μεταχειρισμένων": "μεταχειρισμένος — used, second-hand", "σέρβις": "σέρβις — service (of a car)", "ιμάντας": "ιμάντας — (timing) belt", "λάστιχα": "λάστιχο — tyre; rubber", "της εμπιστοσύνης μου": "της εμπιστοσύνης μου — whom I trust", "γυρίζουν πίσω": "γυρίζω πίσω τα χιλιόμετρα — to roll back the odometer", "χιλιάρικα": "χιλιάρικο — a thousand euros (colloquial)", "τελική τιμή": "τελική τιμή — final price", "μεταβίβαση": "μεταβίβαση — transfer of ownership", "τέλη κυκλοφορίας": "τέλη κυκλοφορίας — road tax", "κλείνουμε": "κλείνω (μια συμφωνία) — to close a deal"},
})

ITEMS.append({
 "id": "l13-dia-giorti", "title": "Η γιορτή του Γιώργου", "title_en": "Giorgos's name day", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση ανάμεσα σε δύο φίλες για μια ονομαστική γιορτή.",
 "script": [
  L("Σοφία", "f", "Μαρίνα, ξέρεις ότι την Πέμπτη είναι του Αγίου Γεωργίου; Γιορτάζει ο Γιώργος. Θα ανοίξει το σπίτι του;", "Marina, do you know that Thursday is St George's Day? Giorgos is celebrating his name day. Will he have an open house?"),
  L("Μαρίνα", "f", "Μου είπε ότι φέτος δεν θα κάνει τραπέζι, γιατί έχει πολλή δουλειά. Αλλά ξέρεις πώς είναι: θα πει «δεν γιορτάζω» και το βράδυ θα έχει σαράντα άτομα στο σπίτι.", "He told me he won't host a meal this year because he has a lot of work. But you know how it is: he'll say \"I'm not celebrating\" and in the evening he'll have forty people at home."),
  L("Σοφία", "f", "Χα! Σωστό. Τι λες να του πάρουμε; Πέρσι του πήραμε κρασί και έμεινε στο ντουλάπι μέχρι σήμερα.", "Ha! True. What do you say we get him? Last year we got him wine and it's still in the cupboard."),
  L("Μαρίνα", "f", "Σκεφτόμουν ένα βιβλίο. Είχε πει ότι θέλει να διαβάσει το καινούργιο μυθιστόρημα του Μάρκαρη. Ή να μαζευτούμε όλοι και να του κάνουμε δώρο ένα μάθημα καταδύσεων, που λέει χρόνια ότι θα κάνει.", "I was thinking of a book. He'd said he wants to read Markaris's new novel. Or we could all chip in and give him a diving lesson, which he's been saying for years he'll do."),
  L("Σοφία", "f", "Το μάθημα είναι τέλεια ιδέα! Θα στείλω μήνυμα στην παρέα να μαζέψουμε από είκοσι ευρώ. Και την Πέμπτη περνάμε το απόγευμα, έστω για λίγο, να του πούμε χρόνια πολλά.", "The lesson is a perfect idea! I'll message the group so we each put in twenty euros. And on Thursday we'll drop by in the afternoon, even just for a bit, to wish him many happy returns."),
 ],
 "questions": [
  Q("Τι πιστεύει η Μαρίνα ότι θα γίνει τελικά;", ["Ο Γιώργος θα φύγει ταξίδι", "Ο Γιώργος θα έχει πολύ κόσμο στο σπίτι, παρόλο που λέει ότι δεν γιορτάζει", "Ο Γιώργος θα δουλεύει όλο το βράδυ", "Ο Γιώργος θα γιορτάσει σε ταβέρνα"], 1, "θα πει «δεν γιορτάζω» και το βράδυ θα έχει σαράντα άτομα στο σπίτι"),
  Q("Γιατί δεν θέλουν να του πάρουν ξανά κρασί;", ["Γιατί δεν πίνει καθόλου", "Γιατί το περσινό κρασί δεν το άνοιξε ποτέ", "Γιατί είναι πολύ ακριβό", "Γιατί του πήραν ήδη άλλοι"], 1, "Πέρσι του πήραμε κρασί και έμεινε στο ντουλάπι μέχρι σήμερα."),
  Q("Τι αποφασίζουν τελικά;", ["Να του πάρουν ένα βιβλίο", "Να του κάνουν όλοι μαζί δώρο ένα μάθημα καταδύσεων", "Να του οργανώσουν πάρτι έκπληξη", "Να μην του πάρουν τίποτα"], 1, "Το μάθημα είναι τέλεια ιδέα!"),
 ],
 "gloss": {"ονομαστική γιορτή": "ονομαστική γιορτή — name day", "του Αγίου Γεωργίου": "του Αγίου Γεωργίου — St George's day (genitive: the feast of)", "Γιορτάζει": "γιορτάζω — to celebrate one's name day", "Θα ανοίξει το σπίτι του": "ανοίγω το σπίτι μου — to have an open house", "θα κάνει τραπέζι": "κάνω τραπέζι — to host a meal", "ντουλάπι": "ντουλάπι — cupboard", "να μαζευτούμε": "μαζεύομαι — to get together; (here) to chip in together", "καταδύσεων": "κατάδυση — dive, diving", "να μαζέψουμε από είκοσι ευρώ": "μαζεύω από … ευρώ — to collect … euros each", "έστω για λίγο": "έστω — even if only", "χρόνια πολλά": "χρόνια πολλά — many happy returns"},
})

ITEMS.append({
 "id": "l13-mon-xorio", "title": "Από την Αθήνα στα Σφακιά", "title_en": "From Athens to Sfakia", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν προγραμματιστή να μιλά για τη μετακόμισή του σε ένα χωριό της Κρήτης.",
 "script": [
  L("Κωστής", "m", "Πριν από τρία χρόνια ζούσα σε ένα δυάρι στα Πατήσια και δούλευα για μια εταιρεία λογισμικού. Όταν η εταιρεία μάς είπε ότι μπορούμε να δουλεύουμε μόνιμα από το σπίτι, σκέφτηκα: αφού δεν χρειάζεται να είμαι στην Αθήνα, γιατί να μένω εδώ;", "Three years ago I was living in a two-room flat in Patissia and working for a software company. When the company told us we could work from home permanently, I thought: since I don't need to be in Athens, why stay here?"),
  L("Κωστής", "m", "Νοίκιασα ένα πέτρινο σπίτι σε ένα χωριό στα Σφακιά, όπου έμενε η γιαγιά μου. Το ενοίκιο είναι το ένα τρίτο από ό,τι πλήρωνα στην Αθήνα. Το πρώτο πρόβλημα ήταν το ίντερνετ: τους πρώτους μήνες έκοβε κάθε φορά που φυσούσε, και ανέβαινα στην πλατεία για να κάνω τις τηλεδιασκέψεις μου.", "I rented a stone house in a village in Sfakia, where my grandmother used to live. The rent is a third of what I paid in Athens. The first problem was the internet: for the first months it cut out every time the wind blew, and I would go up to the square to do my video calls."),
  L("Κωστής", "m", "Η ζωή εδώ δεν είναι ειδυλλιακή, όπως τη φαντάζονται κάποιοι. Τον χειμώνα το χωριό έχει τριάντα κατοίκους και το πιο κοντινό σούπερ μάρκετ είναι μισή ώρα μακριά. Αλλά το απόγευμα, όταν κλείνω τον υπολογιστή, κατεβαίνω στη θάλασσα ή βοηθάω τον γείτονα με τις ελιές. Αυτό δεν το αλλάζω με τίποτα.", "Life here is not idyllic, as some imagine it. In winter the village has thirty inhabitants and the nearest supermarket is half an hour away. But in the afternoon, when I close my computer, I go down to the sea or help my neighbour with the olives. I wouldn't trade that for anything."),
 ],
 "questions": [
  Q("Τι έκανε δυνατή τη μετακόμιση του Κωστή;", ["Μια μετάθεση από την εταιρεία", "Η δυνατότητα να δουλεύει μόνιμα από το σπίτι", "Μια κληρονομιά", "Μια καινούργια δουλειά στην Κρήτη"], 1, "η εταιρεία μάς είπε ότι μπορούμε να δουλεύουμε μόνιμα από το σπίτι"),
  Q("Ποιο ήταν το πρώτο πρόβλημα στο χωριό;", ["Το ακριβό ενοίκιο", "Η κακή σύνδεση στο ίντερνετ", "Οι γείτονες", "Η έλλειψη νερού"], 1, "Το πρώτο πρόβλημα ήταν το ίντερνετ"),
  Q("Πώς περιγράφει ο Κωστής τη ζωή στο χωριό;", ["Τέλεια και χωρίς δυσκολίες", "Δύσκολη, αλλά με απολαύσεις που δεν θα άλλαζε", "Βαρετή και μοναχική", "Πολύ ακριβή"], 1, "Η ζωή εδώ δεν είναι ειδυλλιακή ... Αυτό δεν το αλλάζω με τίποτα."),
 ],
 "gloss": {"προγραμματιστή": "προγραμματιστής — programmer", "δυάρι": "δυάρι — two-room flat", "εταιρεία λογισμικού": "εταιρεία λογισμικού — software company", "μόνιμα": "μόνιμα — permanently", "πέτρινο": "πέτρινος — made of stone", "το ένα τρίτο": "το ένα τρίτο — one third", "έκοβε": "κόβει (το ίντερνετ) — (the internet) cuts out", "τηλεδιασκέψεις": "τηλεδιάσκεψη — video conference", "ειδυλλιακή": "ειδυλλιακός — idyllic", "κοντινό": "κοντινός — nearby", "δεν το αλλάζω με τίποτα": "δεν το αλλάζω με τίποτα — I wouldn't trade it for anything"},
})

ITEMS.append({
 "id": "l13-rep-karetta", "title": "Οι χελώνες της Ζακύνθου", "title_en": "The turtles of Zakynthos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για την προστασία της θαλάσσιας χελώνας καρέτα καρέτα στη Ζάκυνθο.",
 "script": [
  L("Δημοσιογράφος", "f", "Κάθε καλοκαίρι, τις νύχτες, οι θηλυκές χελώνες καρέτα καρέτα βγαίνουν στις αμμουδιές του κόλπου του Λαγανά για να γεννήσουν τα αυγά τους. Η Ζάκυνθος είναι μία από τις σημαντικότερες περιοχές ωοτοκίας τους σε όλη τη Μεσόγειο.", "Every summer, at night, female loggerhead turtles come out onto the sandy beaches of Laganas Bay to lay their eggs. Zakynthos is one of their most important nesting areas in the whole Mediterranean."),
  L("Δημοσιογράφος", "f", "Για να προστατευτούν οι φωλιές, το Εθνικό Θαλάσσιο Πάρκο Ζακύνθου έχει θεσπίσει αυστηρούς κανόνες: οι παραλίες κλείνουν μετά τη δύση του ήλιου, οι ομπρέλες επιτρέπονται μόνο σε συγκεκριμένα σημεία και τα σκάφη πρέπει να κινούνται αργά στον κόλπο. Εθελοντές από όλο τον κόσμο σημαδεύουν τις φωλιές και ενημερώνουν τους λουόμενους.", "To protect the nests, the National Marine Park of Zakynthos has laid down strict rules: the beaches close after sunset, umbrellas are only allowed in specific places and boats must move slowly in the bay. Volunteers from all over the world mark the nests and inform swimmers."),
  L("Δημοσιογράφος", "f", "Η συνύπαρξη με τον τουρισμό δεν είναι πάντα εύκολη. Τα φώτα των ξενοδοχείων αποπροσανατολίζουν τα χελωνάκια, που μόλις βγουν από το αυγό πρέπει να βρουν τον δρόμο προς τη θάλασσα ακολουθώντας τη λάμψη του ορίζοντα. Γι' αυτό οι επιστήμονες ζητούν από τις επιχειρήσεις να χαμηλώνουν τα φώτα τους τη νύχτα.", "Coexistence with tourism is not always easy. The lights of hotels disorient the hatchlings, which as soon as they leave the egg must find their way to the sea by following the glow of the horizon. That is why scientists ask businesses to dim their lights at night."),
 ],
 "questions": [
  Q("Γιατί βγαίνουν οι χελώνες στις παραλίες της Ζακύνθου;", ["Για να βρουν τροφή", "Για να γεννήσουν τα αυγά τους", "Για να ξεκουραστούν από τη ζέστη", "Για να αποφύγουν τα σκάφη"], 1, "για να γεννήσουν τα αυγά τους"),
  Q("Ποιος από τους παρακάτω κανόνες αναφέρεται;", ["Απαγορεύεται το κολύμπι", "Οι παραλίες κλείνουν μετά τη δύση του ήλιου", "Τα σκάφη απαγορεύονται εντελώς", "Οι τουρίστες πρέπει να πληρώνουν εισιτήριο"], 1, "οι παραλίες κλείνουν μετά τη δύση του ήλιου"),
  Q("Ποιο πρόβλημα προκαλούν τα φώτα των ξενοδοχείων;", ["Ζεσταίνουν την άμμο", "Αποπροσανατολίζουν τα μικρά χελωνάκια", "Τρομάζουν τα ψάρια", "Ενοχλούν τους εθελοντές"], 1, "Τα φώτα των ξενοδοχείων αποπροσανατολίζουν τα χελωνάκια"),
 ],
 "gloss": {"χελώνας": "χελώνα — turtle, tortoise", "θηλυκές": "θηλυκός — female", "αμμουδιές": "αμμουδιά — sandy beach", "κόλπου": "κόλπος — bay, gulf", "ωοτοκίας": "ωοτοκία — egg-laying, nesting", "έχει θεσπίσει": "θεσπίζω — to lay down, enact (rules)", "δύση του ήλιου": "δύση του ήλιου — sunset", "σημαδεύουν": "σημαδεύω — to mark", "λουόμενους": "λουόμενος — swimmer, bather", "συνύπαρξη": "συνύπαρξη — coexistence", "αποπροσανατολίζουν": "αποπροσανατολίζω — to disorient", "χελωνάκια": "χελωνάκι — baby turtle, hatchling", "λάμψη": "λάμψη — glow, brightness"},
})

ITEMS.append({
 "id": "l13-int-organopoios", "title": "Ο οργανοποιός", "title_en": "The instrument maker", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν οργανοποιό, κατασκευαστή μπουζουκιών, στον Πειραιά.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσος χρόνος χρειάζεται για να φτιάξετε ένα μπουζούκι;", "How long does it take you to make a bouzouki?"),
  L("Λευτέρης", "m", "Περίπου ενάμιση μήνα, αν δουλεύω μόνο σε αυτό. Το σκάφος, δηλαδή το πίσω μέρος, φτιάχνεται από είκοσι ή και περισσότερες λεπτές λωρίδες ξύλου, τις «ντούγιες», που τις λυγίζω μία μία με ζέστη. Αυτό θέλει υπομονή· αν βιαστείς, το ξύλο σπάει.", "About a month and a half, if I work only on that. The bowl, that is the back, is made from twenty or more thin strips of wood, the \"staves\", which I bend one by one with heat. That takes patience; if you rush, the wood breaks."),
  L("Δημοσιογράφος", "m", "Ποιοι είναι οι πελάτες σας;", "Who are your customers?"),
  L("Λευτέρης", "m", "Επαγγελματίες μουσικοί, φυσικά, αλλά όλο και περισσότερο νέοι που μαθαίνουν ρεμπέτικο, και πολλοί ξένοι. Πέρσι έστειλα όργανα στην Ιαπωνία και στη Βραζιλία. Κάθε όργανο το φτιάχνω για τον συγκεκριμένο μουσικό: κοιτάζω πώς παίζει, πόσο μεγάλα είναι τα χέρια του, τι ήχο ψάχνει.", "Professional musicians, of course, but more and more young people learning rebetiko, and many foreigners. Last year I sent instruments to Japan and Brazil. I make each instrument for the specific musician: I watch how they play, how big their hands are, what sound they're looking for."),
  L("Δημοσιογράφος", "m", "Υπάρχουν νέοι που θέλουν να μάθουν την τέχνη;", "Are there young people who want to learn the craft?"),
  L("Λευτέρης", "m", "Έχω δύο μαθητές τώρα. Τους λέω πάντα ότι τα πρώτα πέντε όργανα θα είναι κακά, και ότι αυτό είναι φυσιολογικό. Η τέχνη αυτή μαθαίνεται με τα χέρια, όχι από βίντεο.", "I have two apprentices now. I always tell them that the first five instruments will be bad, and that this is normal. This craft is learned with the hands, not from videos."),
 ],
 "questions": [
  Q("Γιατί χρειάζεται υπομονή η κατασκευή του σκάφους;", ["Γιατί το ξύλο είναι ακριβό", "Γιατί οι λωρίδες λυγίζουν μία μία με ζέστη και σπάνε αν βιαστείς", "Γιατί πρέπει να στεγνώσει η κόλλα", "Γιατί το ξύλο έρχεται από το εξωτερικό"], 1, "τις λυγίζω μία μία με ζέστη ... αν βιαστείς, το ξύλο σπάει"),
  Q("Πώς προσαρμόζει ο Λευτέρης κάθε όργανο;", ["Ανάλογα με την τιμή", "Ανάλογα με το πώς παίζει ο μουσικός και τι ήχο θέλει", "Ανάλογα με τη χώρα του πελάτη", "Δεν το προσαρμόζει, όλα είναι ίδια"], 1, "κοιτάζω πώς παίζει, πόσο μεγάλα είναι τα χέρια του, τι ήχο ψάχνει"),
  Q("Τι λέει στους μαθητές του;", ["Ότι θα γίνουν πλούσιοι", "Ότι τα πρώτα όργανα θα είναι κακά και αυτό είναι φυσιολογικό", "Να μάθουν από βίντεο", "Να σπουδάσουν πρώτα μουσική"], 1, "τα πρώτα πέντε όργανα θα είναι κακά, και ... αυτό είναι φυσιολογικό"),
 ],
 "gloss": {"οργανοποιό": "οργανοποιός — instrument maker", "ενάμιση μήνα": "ενάμισης μήνας — a month and a half", "σκάφος": "σκάφος — (of a bouzouki) bowl; (usually) boat, hull", "λωρίδες": "λωρίδα — strip", "ντούγιες": "ντούγια — stave (of a bowl or barrel)", "λυγίζω": "λυγίζω — to bend", "αν βιαστείς": "βιάζομαι — to be in a hurry", "συγκεκριμένο": "συγκεκριμένος — specific", "τέχνη": "τέχνη — craft; art", "φυσιολογικό": "φυσιολογικός — normal"},
})

ITEMS.append({
 "id": "l13-mon-vyzantio", "title": "Το Βυζάντιο και εμείς", "title_en": "Byzantium and us", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε έναν ιστορικό να μιλά σε μια διάλεξη για τη θέση του Βυζαντίου στη νεοελληνική ταυτότητα.",
 "script": [
  L("Ιστορικός", "m", "Όταν το νεοσύστατο ελληνικό κράτος αναζητούσε την ταυτότητά του, τον δέκατο ένατο αιώνα, το βλέμμα του στράφηκε κυρίως προς την κλασική αρχαιότητα. Το Βυζάντιο, αντίθετα, αντιμετωπιζόταν με καχυποψία· πολλοί λόγιοι, επηρεασμένοι από τον ευρωπαϊκό Διαφωτισμό, το έβλεπαν ως μια μακρά περίοδο σκοταδισμού και παρακμής.", "When the newly founded Greek state was seeking its identity, in the nineteenth century, its gaze turned mainly towards classical antiquity. Byzantium, by contrast, was regarded with suspicion; many scholars, influenced by the European Enlightenment, saw it as a long period of obscurantism and decline."),
  L("Ιστορικός", "m", "Η στάση αυτή άλλαξε σταδιακά, κυρίως χάρη στον ιστορικό Κωνσταντίνο Παπαρρηγόπουλο, ο οποίος διατύπωσε την ιδέα μιας αδιάσπαστης συνέχειας του ελληνισμού από την αρχαιότητα, μέσω του Βυζαντίου, έως τη σύγχρονη εποχή. Το σχήμα αυτό είχε τεράστια επιρροή και διαμόρφωσε για πάνω από έναν αιώνα τη σχολική ιστορία.", "This attitude changed gradually, mainly thanks to the historian Konstantinos Paparrigopoulos, who formulated the idea of an unbroken continuity of Hellenism from antiquity, through Byzantium, to the modern era. This scheme had enormous influence and shaped school history for more than a century."),
  L("Ιστορικός", "m", "Σήμερα οι ιστορικοί είναι πιο επιφυλακτικοί απέναντι σε κάθε αφήγημα αδιάσπαστης συνέχειας. Υπογραμμίζουν ότι το Βυζάντιο ήταν μια πολυεθνική αυτοκρατορία, της οποίας οι κάτοικοι αυτοαποκαλούνταν «Ρωμαίοι», και ότι η ελληνική εθνική ταυτότητα, με τη σύγχρονη έννοια, διαμορφώθηκε πολύ αργότερα.", "Today historians are more cautious towards any narrative of unbroken continuity. They stress that Byzantium was a multi-ethnic empire whose inhabitants called themselves \"Romans\", and that Greek national identity, in the modern sense, was formed much later."),
  L("Ιστορικός", "m", "Αυτό δεν μειώνει τη βυζαντινή κληρονομιά, που είναι ορατή παντού: στη γλώσσα, στη θρησκευτική ζωή, στη μουσική, ακόμη και σε εκφράσεις της καθημερινότητας. Σημαίνει απλώς ότι οφείλουμε να την κατανοήσουμε με τους δικούς της όρους, και όχι ως ένα απλό ενδιάμεσο κεφάλαιο ανάμεσα στον Περικλή και στο 1821.", "This does not diminish the Byzantine heritage, which is visible everywhere: in the language, in religious life, in music, even in everyday expressions. It simply means that we must understand it on its own terms, and not as a mere intermediate chapter between Pericles and 1821."),
 ],
 "questions": [
  Q("Πώς έβλεπαν πολλοί λόγιοι του 19ου αιώνα το Βυζάντιο;", ["Ως πρότυπο για το νέο κράτος", "Ως περίοδο σκοταδισμού και παρακμής", "Ως τη χρυσή εποχή του ελληνισμού", "Με αδιαφορία"], 1, "το έβλεπαν ως μια μακρά περίοδο σκοταδισμού και παρακμής"),
  Q("Ποια ιδέα διατύπωσε ο Παπαρρηγόπουλος;", ["Ότι οι νέοι Έλληνες δεν έχουν σχέση με τους αρχαίους", "Ότι ο ελληνισμός έχει αδιάσπαστη συνέχεια από την αρχαιότητα ως σήμερα, μέσω του Βυζαντίου", "Ότι το Βυζάντιο ήταν ξένη κατάκτηση", "Ότι η ιστορία πρέπει να διδάσκεται χωρίς το Βυζάντιο"], 1, "την ιδέα μιας αδιάσπαστης συνέχειας του ελληνισμού από την αρχαιότητα, μέσω του Βυζαντίου, έως τη σύγχρονη εποχή"),
  Q("Τι υπογραμμίζουν οι σημερινοί ιστορικοί;", ["Ότι το Βυζάντιο ήταν αμιγώς ελληνικό κράτος", "Ότι το Βυζάντιο ήταν πολυεθνική αυτοκρατορία και η εθνική ταυτότητα διαμορφώθηκε αργότερα", "Ότι οι Βυζαντινοί αυτοαποκαλούνταν Έλληνες", "Ότι η συνέχεια είναι αποδεδειγμένη"], 1, "το Βυζάντιο ήταν μια πολυεθνική αυτοκρατορία ... η ελληνική εθνική ταυτότητα ... διαμορφώθηκε πολύ αργότερα"),
  Q("Ποιο είναι το συμπέρασμα του ομιλητή;", ["Η βυζαντινή κληρονομιά είναι ασήμαντη", "Το Βυζάντιο πρέπει να κατανοηθεί με τους δικούς του όρους", "Το 1821 δεν έχει σχέση με το Βυζάντιο", "Πρέπει να επιστρέψουμε στο σχήμα του Παπαρρηγόπουλου"], 1, "οφείλουμε να την κατανοήσουμε με τους δικούς της όρους"),
 ],
 "gloss": {"νεοσύστατο": "νεοσύστατος — newly founded", "στράφηκε": "στρέφομαι — to turn (towards)", "καχυποψία": "καχυποψία — suspicion", "λόγιοι": "λόγιος — scholar, man of letters", "Διαφωτισμό": "Διαφωτισμός — the Enlightenment", "σκοταδισμού": "σκοταδισμός — obscurantism", "παρακμής": "παρακμή — decline", "διατύπωσε": "διατυπώνω — to formulate", "αδιάσπαστης": "αδιάσπαστος — unbroken", "επιφυλακτικοί": "επιφυλακτικός — cautious, reserved", "αφήγημα": "αφήγημα — narrative", "πολυεθνική αυτοκρατορία": "πολυεθνική αυτοκρατορία — multi-ethnic empire", "αυτοαποκαλούνταν": "αυτοαποκαλούμαι — to call oneself", "κληρονομιά": "κληρονομιά — heritage", "με τους δικούς της όρους": "με τους δικούς του όρους — on its own terms"},
})

ITEMS.append({
 "id": "l13-int-klima", "title": "Η Μεσόγειος ζεσταίνεται", "title_en": "The Mediterranean is warming", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια κλιματολόγο για τις επιπτώσεις της κλιματικής αλλαγής στην Ελλάδα.",
 "script": [
  L("Δημοσιογράφος", "m", "Συχνά ακούμε ότι η Μεσόγειος είναι «θερμό σημείο» της κλιματικής αλλαγής. Τι σημαίνει αυτό;", "We often hear that the Mediterranean is a \"hotspot\" of climate change. What does that mean?"),
  L("Κλιματολόγος", "f", "Σημαίνει ότι η περιοχή μας θερμαίνεται ταχύτερα από τον παγκόσμιο μέσο όρο. Ταυτόχρονα, οι περισσότερες κλιματικές προβολές δείχνουν μείωση των βροχοπτώσεων, ιδίως στη νότια και ανατολική Ελλάδα. Ο συνδυασμός αυτός σημαίνει μακρύτερα και θερμότερα καλοκαίρια και αυξημένο κίνδυνο ξηρασίας και πυρκαγιών.", "It means that our region is warming faster than the global average. At the same time, most climate projections show a decrease in rainfall, especially in southern and eastern Greece. This combination means longer and hotter summers and an increased risk of drought and wildfires."),
  L("Δημοσιογράφος", "m", "Κι όμως, τα τελευταία χρόνια είχαμε και καταστροφικές πλημμύρες. Δεν είναι αντίφαση;", "And yet, in recent years we have also had catastrophic floods. Isn't that a contradiction?"),
  L("Κλιματολόγος", "f", "Φαινομενικά μόνο. Μια θερμότερη ατμόσφαιρα συγκρατεί περισσότερους υδρατμούς, οπότε, όταν βρέχει, οι βροχοπτώσεις μπορεί να είναι πιο έντονες. Μπορεί δηλαδή να έχουμε λιγότερη βροχή συνολικά μέσα στον χρόνο, αλλά πιο ακραία επεισόδια. Η θέρμανση της θάλασσας, επιπλέον, τροφοδοτεί με ενέργεια ορισμένα ισχυρά καιρικά συστήματα.", "Only on the surface. A warmer atmosphere holds more water vapour, so when it rains, rainfall can be more intense. In other words, we may have less rain overall during the year, but more extreme episodes. The warming of the sea, moreover, feeds energy into certain powerful weather systems."),
  L("Δημοσιογράφος", "m", "Τι πρέπει να γίνει;", "What needs to be done?"),
  L("Κλιματολόγος", "f", "Δύο πράγματα παράλληλα. Πρώτον, μείωση των εκπομπών, που είναι παγκόσμια ευθύνη. Δεύτερον, προσαρμογή: πόλεις με περισσότερο πράσινο και σκιά, καλύτερη διαχείριση του νερού, αντιπλημμυρικά έργα, και χωροταξικό σχεδιασμό που να μην επιτρέπει τη δόμηση σε κοίτες ποταμών. Η προσαρμογή δεν είναι πολυτέλεια· είναι ζήτημα ασφάλειας.", "Two things in parallel. First, cutting emissions, which is a global responsibility. Second, adaptation: cities with more greenery and shade, better water management, flood-protection works, and spatial planning that does not allow building in riverbeds. Adaptation is not a luxury; it is a matter of safety."),
 ],
 "questions": [
  Q("Τι σημαίνει ότι η Μεσόγειος είναι «θερμό σημείο»;", ["Ότι έχει τις υψηλότερες θερμοκρασίες στον κόσμο", "Ότι θερμαίνεται ταχύτερα από τον παγκόσμιο μέσο όρο", "Ότι έχει πολλά ηφαίστεια", "Ότι προσελκύει πολλούς τουρίστες"], 1, "η περιοχή μας θερμαίνεται ταχύτερα από τον παγκόσμιο μέσο όρο"),
  Q("Πώς εξηγεί η κλιματολόγος τις πλημμύρες, παρά τη μείωση των βροχοπτώσεων;", ["Είναι τυχαία γεγονότα χωρίς σχέση με το κλίμα", "Μια θερμότερη ατμόσφαιρα συγκρατεί περισσότερους υδρατμούς και προκαλεί πιο έντονες βροχές", "Οφείλονται μόνο σε κακή συντήρηση των δρόμων", "Η βροχή στην πραγματικότητα αυξάνεται συνολικά"], 1, "Μια θερμότερη ατμόσφαιρα συγκρατεί περισσότερους υδρατμούς ... πιο έντονες"),
  Q("Ποιο από τα παρακάτω ΔΕΝ αναφέρεται ως μέτρο προσαρμογής;", ["Περισσότερο πράσινο στις πόλεις", "Καλύτερη διαχείριση του νερού", "Απαγόρευση δόμησης σε κοίτες ποταμών", "Κατασκευή νέων αεροδρομίων"], 3, "Αναφέρει πράσινο, νερό, αντιπλημμυρικά και χωροταξία· όχι αεροδρόμια."),
 ],
 "gloss": {"κλιματολόγο": "κλιματολόγος — climatologist", "θερμό σημείο": "θερμό σημείο — hotspot", "θερμαίνεται": "θερμαίνομαι — to warm up", "μέσο όρο": "μέσος όρος — average", "κλιματικές προβολές": "κλιματική προβολή — climate projection", "βροχοπτώσεων": "βροχόπτωση — rainfall", "αντίφαση": "αντίφαση — contradiction", "Φαινομενικά": "φαινομενικά — seemingly, on the surface", "υδρατμούς": "υδρατμός — water vapour", "τροφοδοτεί": "τροφοδοτώ — to feed, supply", "εκπομπών": "εκπομπή — emission; broadcast", "προσαρμογή": "προσαρμογή — adaptation", "αντιπλημμυρικά έργα": "αντιπλημμυρικά έργα — flood-protection works", "χωροταξικό σχεδιασμό": "χωροταξικός σχεδιασμός — spatial planning", "κοίτες ποταμών": "κοίτη ποταμού — riverbed", "πολυτέλεια": "πολυτέλεια — luxury"},
})
rnd = random.Random(13)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-13.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
