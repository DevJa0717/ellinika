# Source for library/listening/listening-74.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l74.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l74-ann-katolisthisi", "title": "Κλειστός δρόμος μετά από κατολίσθηση", "title_en": "Road closed after a landslide", "type": "announcement", "level": "B2",
 "context_el": "Οδηγείτε στο Πήλιο και ακούτε το δελτίο κυκλοφορίας σε έναν τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνητής", "m", "Καλημέρα σας. Λόγω των έντονων βροχοπτώσεων της νύχτας, σημειώθηκε κατολίσθηση στον επαρχιακό δρόμο προς τη Ζαγορά, λίγο μετά το χωριό Χάνια. Βράχια και χώματα έχουν καλύψει και τις δύο λωρίδες.", "Good morning. Because of the heavy rainfall overnight, there has been a landslide on the provincial road to Zagora, just after the village of Chania. Rocks and earth have covered both lanes."),
  L("Εκφωνητής", "m", "Ο δρόμος παραμένει κλειστός μέχρι νεωτέρας. Συνεργεία του δήμου εργάζονται ήδη για την απομάκρυνση των φερτών υλικών, αλλά οι γεωλόγοι πρέπει πρώτα να ελέγξουν αν το πρανές είναι σταθερό. Οι οδηγοί που κατευθύνονται προς τη Ζαγορά να χρησιμοποιήσουν την παραλιακή διαδρομή μέσω Αγριάς, η οποία είναι μεγαλύτερη κατά σαράντα περίπου λεπτά.", "The road remains closed until further notice. Municipal crews are already working to remove the debris, but geologists must first check whether the slope is stable. Drivers heading to Zagora should use the coastal route via Agria, which is about forty minutes longer."),
  L("Εκφωνητής", "m", "Τα σχολικά λεωφορεία της περιοχής θα ακολουθήσουν σήμερα την ίδια παρακαμπτήριο, γι' αυτό οι γονείς ενημερώνονται ότι οι μαθητές ενδέχεται να φτάσουν με καθυστέρηση. Η Πολιτική Προστασία συνιστά να αποφεύγονται οι μη αναγκαίες μετακινήσεις στα ορεινά.", "The area's school buses will follow the same detour today, so parents are informed that pupils may arrive late. Civil Protection advises avoiding unnecessary journeys in the mountains."),
 ],
 "questions": [
  Q("Τι προκάλεσε την κατολίσθηση;", ["Ένας σεισμός", "Οι έντονες βροχοπτώσεις της νύχτας", "Έργα στον δρόμο", "Μια πυρκαγιά"], 1, "Λόγω των έντονων βροχοπτώσεων της νύχτας"),
  Q("Τι πρέπει να γίνει πριν ανοίξει ο δρόμος;", ["Να έρθει η αστυνομία", "Να ελέγξουν οι γεωλόγοι αν το πρανές είναι σταθερό", "Να σταματήσει η βροχή", "Να ασφαλτοστρωθεί ξανά"], 1, "οι γεωλόγοι πρέπει πρώτα να ελέγξουν αν το πρανές είναι σταθερό"),
  Q("Τι ισχύει για την παραλιακή διαδρομή;", ["Είναι κι αυτή κλειστή", "Είναι μεγαλύτερη κατά σαράντα περίπου λεπτά", "Είναι μόνο για λεωφορεία", "Είναι πιο σύντομη"], 1, "είναι μεγαλύτερη κατά σαράντα περίπου λεπτά"),
 ],
 "gloss": {"κατολίσθηση": "κατολίσθηση — landslide", "βροχοπτώσεων": "βροχόπτωση — rainfall", "επαρχιακό": "επαρχιακός — provincial", "λωρίδες": "λωρίδα — lane", "μέχρι νεωτέρας": "μέχρι νεωτέρας — until further notice", "φερτών υλικών": "φερτά υλικά — debris", "πρανές": "πρανές — slope, embankment", "παρακαμπτήριο": "παρακαμπτήριος — detour, bypass", "ενδέχεται": "ενδέχεται — may, it is possible"},
})

ITEMS.append({
 "id": "l74-vm-tapetsieris", "title": "Η πολυθρόνα της γιαγιάς στον ταπετσιέρη", "title_en": "Grandmother's armchair at the upholsterer's", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε πάει την παλιά πολυθρόνα της γιαγιάς σας σε έναν ταπετσιέρη για επιδιόρθωση. Θα ακούσετε ένα μήνυμα που σας άφησε στον τηλεφωνητή.",
 "script": [
  L("Ταπετσιέρης", "m", "Γεια σας, από το εργαστήριο του Στέλιου σας παίρνω, για την πολυθρόνα. Την ξηλώσαμε σήμερα και, να σας πω την αλήθεια, ο σκελετός είναι σε πολύ καλή κατάσταση, από γερό καρυδένιο ξύλο. Τέτοια έπιπλα δεν φτιάχνονται πια.", "Hello, I'm calling from Stelios's workshop, about the armchair. We stripped it today and, to tell you the truth, the frame is in very good condition, made of solid walnut. Furniture like this isn't made any more."),
  L("Ταπετσιέρης", "m", "Το πρόβλημα είναι τα ελατήρια: τα μισά έχουν σπάσει και τα υπόλοιπα έχουν χαλαρώσει. Προτείνω να τα αλλάξουμε όλα, αλλιώς σε δυο χρόνια θα βουλιάξει πάλι. Αυτό ανεβάζει το κόστος κατά ογδόντα ευρώ περίπου.", "The problem is the springs: half of them have broken and the rest have gone slack. I suggest we replace them all, otherwise it will sag again in two years. That raises the cost by about eighty euros."),
  L("Ταπετσιέρης", "m", "Για το ύφασμα, περάστε όποτε μπορείτε να διαλέξετε από τα δείγματα. Αν θέλετε να κρατήσουμε το παλιό κέντημα της γιαγιάς σας στην πλάτη, γίνεται, αλλά θα χρειαστεί να το καθαρίσει πρώτα μια συνεργάτιδά μου. Πείτε μου τι αποφασίσατε μέχρι την Παρασκευή.", "As for the fabric, come by whenever you can to choose from the samples. If you want us to keep your grandmother's old embroidery on the back, it can be done, but a colleague of mine will need to clean it first. Let me know what you've decided by Friday."),
 ],
 "questions": [
  Q("Σε τι κατάσταση είναι ο σκελετός της πολυθρόνας;", ["Έχει σαπίσει", "Σε πολύ καλή κατάσταση", "Χρειάζεται καινούργια πόδια", "Είναι από φτηνό ξύλο"], 1, "ο σκελετός είναι σε πολύ καλή κατάσταση"),
  Q("Γιατί προτείνει να αλλάξουν όλα τα ελατήρια;", ["Γιατί είναι φτηνά", "Γιατί αλλιώς σε δυο χρόνια θα βουλιάξει πάλι", "Γιατί το ζήτησε η γιαγιά", "Γιατί είναι σκουριασμένα"], 1, "αλλιώς σε δυο χρόνια θα βουλιάξει πάλι"),
  Q("Τι χρειάζεται για να κρατηθεί το παλιό κέντημα;", ["Να το καθαρίσει πρώτα μια συνεργάτιδά του", "Να ραφτεί από την αρχή", "Να μπει σε κορνίζα", "Να βαφτεί"], 0, "θα χρειαστεί να το καθαρίσει πρώτα μια συνεργάτιδά μου"),
 ],
 "gloss": {"πολυθρόνα": "πολυθρόνα — armchair", "ταπετσιέρη": "ταπετσιέρης — upholsterer", "ξηλώσαμε": "ξηλώνω — to strip, unpick", "σκελετός": "σκελετός — frame", "καρυδένιο": "καρυδένιος — (made of) walnut", "ελατήρια": "ελατήριο — spring", "βουλιάξει": "βουλιάζω — to sag, sink", "δείγματα": "δείγμα — sample", "κέντημα": "κέντημα — embroidery"},
})

ITEMS.append({
 "id": "l74-dia-theia-melvourni", "title": "Η θεία από τη Μελβούρνη έρχεται για έναν μήνα", "title_en": "The aunt from Melbourne is coming for a month", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι συζητά πώς θα φιλοξενήσει μια θεία που ζει στην Αυστραλία και έρχεται στην Ελλάδα τον Ιανουάριο.",
 "script": [
  L("Κατερίνα", "f", "Πήρε τηλέφωνο η θεία Ευανθία από τη Μελβούρνη. Έκλεισε εισιτήριο για τις δέκα Ιανουαρίου και θέλει να μείνει έναν μήνα. Πρώτη φορά έρχεται μετά από δεκαπέντε χρόνια.", "Aunt Evanthia rang from Melbourne. She has booked a ticket for the tenth of January and wants to stay a month. It's the first time she's coming in fifteen years."),
  L("Γιώργος", "m", "Χαίρομαι πολύ, αλλά πού θα κοιμηθεί; Το γραφείο είναι γεμάτο κούτες, και εγώ δουλεύω από το σπίτι τρεις μέρες την εβδομάδα.", "I'm very glad, but where will she sleep? The study is full of boxes, and I work from home three days a week."),
  L("Κατερίνα", "f", "Το σκέφτηκα. Αδειάζουμε το γραφείο, βάζουμε τον καναπέ-κρεβάτι, κι εσύ δουλεύεις αυτόν τον μήνα από το τραπέζι της κουζίνας. Θα είναι και ευκαιρία να ξεφορτωθούμε επιτέλους όλα αυτά τα πράγματα.", "I've thought about it. We empty the study, put in the sofa bed, and you work from the kitchen table that month. It will also be a chance to finally get rid of all that stuff."),
  L("Γιώργος", "m", "Εντάξει. Μόνο μην της υποσχεθείς ότι θα τη γυρίσουμε όλη την Ελλάδα. Εμείς δουλεύουμε. Μήπως να της προτείνουμε να περάσει και μια βδομάδα στο χωριό, με τον αδερφό της; Εκεί έχει μεγαλώσει, θα το χαρεί.", "Fine. Just don't promise her we'll take her all over Greece. We work. Why don't we suggest she spends a week in the village too, with her brother? That's where she grew up, she'll enjoy it."),
 ],
 "questions": [
  Q("Πόσο καιρό θέλει να μείνει η θεία;", ["Μια εβδομάδα", "Έναν μήνα", "Δεκαπέντε μέρες", "Ως το Πάσχα"], 1, "θέλει να μείνει έναν μήνα"),
  Q("Πού θα δουλεύει ο Γιώργος όσο μένει η θεία;", ["Σε ένα καφέ", "Στο τραπέζι της κουζίνας", "Στο γραφείο της εταιρείας", "Στο υπνοδωμάτιο"], 1, "εσύ δουλεύεις αυτόν τον μήνα από το τραπέζι της κουζίνας"),
  Q("Τι προτείνει ο Γιώργος;", ["Να μείνει η θεία σε ξενοδοχείο", "Να περάσει μια βδομάδα στο χωριό με τον αδερφό της", "Να πάρουν άδεια από τη δουλειά", "Να την πάνε σε όλη την Ελλάδα"], 1, "να περάσει και μια βδομάδα στο χωριό, με τον αδερφό της"),
 ],
 "gloss": {"φιλοξενήσει": "φιλοξενώ — to host, put up", "Έκλεισε": "κλείνω (εισιτήριο) — to book", "κούτες": "κούτα — cardboard box", "καναπέ-κρεβάτι": "καναπές-κρεβάτι — sofa bed", "ξεφορτωθούμε": "ξεφορτώνομαι — to get rid of", "υποσχεθείς": "υπόσχομαι — to promise"},
})

ITEMS.append({
 "id": "l74-dia-kleidia-exochikou", "title": "Τα κλειδιά του εξοχικού", "title_en": "The keys to the country house", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέρφια, που έχουν κληρονομήσει μαζί ένα εξοχικό στην Εύβοια, συζητούν στο τηλέφωνο.",
 "script": [
  L("Νίκος", "m", "Άκου, ο Παύλος, ο συνάδελφός μου, με ρώτησε αν μπορεί να μείνει στο εξοχικό ένα Σαββατοκύριακο με τη γυναίκα του. Του είπα ότι πρέπει να ρωτήσω πρώτα εσένα.", "Listen, Pavlos, my colleague, asked me if he can stay at the country house for a weekend with his wife. I told him I had to ask you first."),
  L("Ελένη", "f", "Καλά έκανες. Δεν έχω πρόβλημα με τον Παύλο, αλλά θυμάσαι τι έγινε πέρσι με τους φίλους της ξαδέρφης μας; Άφησαν το θερμοσίφωνο αναμμένο μια εβδομάδα και ήρθε λογαριασμός διακόσια ευρώ.", "You did the right thing. I've no problem with Pavlos, but do you remember what happened last year with our cousin's friends? They left the water heater on for a week and a bill of two hundred euros came."),
  L("Νίκος", "m", "Το θυμάμαι, πώς να το ξεχάσω. Λέω να γράψουμε μια λίστα με τα βασικά: νερό, ρεύμα, πού είναι ο γενικός διακόπτης, τι να κλείνουν φεύγοντας. Και να την κολλήσουμε στο ψυγείο.", "I remember, how could I forget. I suggest we write a list of the basics: water, electricity, where the main switch is, what to turn off when leaving. And stick it on the fridge."),
  L("Ελένη", "f", "Συμφωνώ. Και να συμφωνήσουμε από τώρα ότι όποιος έρχεται πληρώνει τουλάχιστον τα κοινόχρηστα εκείνου του μήνα. Δεν είναι θέμα χρημάτων, είναι θέμα να σέβονται το σπίτι.", "Agreed. And let's agree now that whoever comes pays at least that month's shared charges. It's not about money, it's about respecting the house."),
 ],
 "questions": [
  Q("Τι ζήτησε ο συνάδελφος του Νίκου;", ["Να αγοράσει το σπίτι", "Να μείνει στο εξοχικό ένα Σαββατοκύριακο", "Να το νοικιάσει το καλοκαίρι", "Να δανειστεί το αυτοκίνητο"], 1, "αν μπορεί να μείνει στο εξοχικό ένα Σαββατοκύριακο"),
  Q("Τι συνέβη πέρσι;", ["Χάθηκαν τα κλειδιά", "Άφησαν το θερμοσίφωνο αναμμένο μια εβδομάδα", "Έσπασε ένα παράθυρο", "Πλημμύρισε η κουζίνα"], 1, "Άφησαν το θερμοσίφωνο αναμμένο μια εβδομάδα"),
  Q("Γιατί θέλει η Ελένη να πληρώνουν οι επισκέπτες τα κοινόχρηστα;", ["Γιατί χρειάζεται χρήματα", "Για να σέβονται το σπίτι", "Γιατί το λέει ο νόμος", "Για να επισκευάσουν τη στέγη"], 1, "είναι θέμα να σέβονται το σπίτι"),
 ],
 "gloss": {"κληρονομήσει": "κληρονομώ — to inherit", "εξοχικό": "εξοχικό — country/holiday house", "θερμοσίφωνο": "θερμοσίφωνας — water heater", "γενικός διακόπτης": "γενικός διακόπτης — main switch", "κοινόχρηστα": "κοινόχρηστα — shared building charges", "σέβονται": "σέβομαι — to respect"},
})

ITEMS.append({
 "id": "l74-int-chartografos", "title": "Μια χαρτογράφος", "title_en": "A cartographer", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια χαρτογράφο σε μια ραδιοφωνική εκπομπή για επαγγέλματα.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αλεξίου, στην εποχή των δορυφόρων και των εφαρμογών στο κινητό, χρειαζόμαστε ακόμα χαρτογράφους;", "Ms Alexiou, in the age of satellites and phone apps, do we still need cartographers?"),
  L("Χαρτογράφος", "f", "Περισσότερο από ποτέ. Οι δορυφόροι μάς δίνουν τεράστιο όγκο δεδομένων, αλλά κάποιος πρέπει να αποφασίσει τι θα φαίνεται στον χάρτη και τι όχι. Ένας χάρτης που δείχνει τα πάντα δεν δείχνει τίποτα.", "More than ever. Satellites give us a huge volume of data, but someone has to decide what will appear on the map and what won't. A map that shows everything shows nothing."),
  L("Δημοσιογράφος", "m", "Με τι ασχολείστε εσείς συγκεκριμένα;", "What do you work on specifically?"),
  L("Χαρτογράφος", "f", "Φτιάχνω πεζοπορικούς χάρτες για ορεινές περιοχές. Περπατάω η ίδια κάθε μονοπάτι με ένα GPS, γιατί οι δορυφορικές εικόνες δεν βλέπουν κάτω από τα δέντρα. Σημειώνω πηγές, εκκλησάκια, σημεία όπου το μονοπάτι χάνεται. Μιλάω και με τους βοσκούς· αυτοί ξέρουν τα τοπωνύμια που δεν έχει γράψει κανείς.", "I make hiking maps for mountain areas. I walk every path myself with a GPS, because satellite images can't see under the trees. I mark springs, small chapels, points where the path disappears. I also talk to shepherds; they know the place names nobody has written down."),
  L("Δημοσιογράφος", "m", "Τα τοπωνύμια είναι σημαντικά;", "Are place names important?"),
  L("Χαρτογράφος", "f", "Είναι η μνήμη ενός τόπου. Όταν πεθάνει ο τελευταίος που ξέρει ότι μια ρεματιά λέγεται «του Λύκου», χάνεται μαζί του και μια ιστορία. Γι' αυτό τα καταγράφω, ακόμα κι αν δεν χωράνε όλα στον χάρτη.", "They are the memory of a place. When the last person who knows that a ravine is called 'the Wolf's' dies, a story is lost with him. That's why I record them, even if they don't all fit on the map."),
 ],
 "questions": [
  Q("Τι πρέπει, κατά τη χαρτογράφο, να αποφασίσει κάποιος;", ["Πόσο θα κοστίζει ο χάρτης", "Τι θα φαίνεται στον χάρτη και τι όχι", "Ποιος δορυφόρος είναι καλύτερος", "Σε ποια γλώσσα θα γραφτεί"], 1, "κάποιος πρέπει να αποφασίσει τι θα φαίνεται στον χάρτη και τι όχι"),
  Q("Γιατί περπατάει η ίδια τα μονοπάτια;", ["Γιατί της αρέσει η γυμναστική", "Γιατί οι δορυφορικές εικόνες δεν βλέπουν κάτω από τα δέντρα", "Γιατί δεν έχει αυτοκίνητο", "Γιατί το ζητούν οι βοσκοί"], 1, "οι δορυφορικές εικόνες δεν βλέπουν κάτω από τα δέντρα"),
  Q("Γιατί καταγράφει τα τοπωνύμια;", ["Για να τα πουλήσει", "Γιατί είναι η μνήμη ενός τόπου", "Γιατί το απαιτεί ο νόμος", "Για να αλλάξει τα ονόματα"], 1, "Είναι η μνήμη ενός τόπου"),
 ],
 "gloss": {"χαρτογράφο": "χαρτογράφος — cartographer", "δορυφόρων": "δορυφόρος — satellite", "όγκο": "όγκος — volume", "πεζοπορικούς": "πεζοπορικός — hiking", "μονοπάτι": "μονοπάτι — path", "πηγές": "πηγή — spring", "βοσκούς": "βοσκός — shepherd", "τοπωνύμια": "τοπωνύμιο — place name", "ρεματιά": "ρεματιά — ravine"},
})

ITEMS.append({
 "id": "l74-rep-flamingo", "title": "Τα φλαμίνγκο των αλυκών", "title_en": "The flamingos of the salt pans", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από μια εκπομπή για το περιβάλλον, γυρισμένο σε μια αλυκή στη Λέσβο.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρισκόμαστε στις αλυκές της Καλλονής, στη Λέσβο. Μπροστά μας, στα ρηχά νερά, εκατοντάδες ροζ πουλιά περπατούν αργά με το κεφάλι μέσα στο νερό. Είναι τα φοινικόπτερα, όπως λέγονται επίσημα, ή φλαμίνγκο, όπως τα λέμε όλοι.", "We are at the Kalloni salt pans, on Lesvos. In front of us, in the shallow water, hundreds of pink birds walk slowly with their heads in the water. They are greater flamingos, phoinikoptera as they are officially called, or flamingos, as we all call them."),
  L("Ρεπόρτερ", "f", "Το ροζ χρώμα τους, μας εξηγεί ένας ορνιθολόγος, δεν είναι έμφυτο. Προέρχεται από τις χρωστικές ουσίες που περιέχουν τα μικρά καρκινοειδή και τα φύκια με τα οποία τρέφονται. Ένα φλαμίνγκο που δεν βρίσκει αυτή την τροφή σιγά σιγά ξεθωριάζει.", "Their pink colour, an ornithologist explains to us, is not innate. It comes from the pigments contained in the tiny crustaceans and algae they feed on. A flamingo that cannot find this food slowly fades."),
  L("Ρεπόρτερ", "f", "Παλιότερα τα φλαμίνγκο περνούσαν από εδώ μόνο στη μετανάστευση. Τα τελευταία χρόνια όλο και περισσότερα μένουν όλο τον χειμώνα. Οι ορνιθολόγοι χαίρονται, αλλά ανησυχούν για την ανεξέλεγκτη δόμηση γύρω από τους υγροτόπους και για τους επισκέπτες που πλησιάζουν πολύ για μια φωτογραφία. Ένα κοπάδι που τρομάζει, μας λένε, ξοδεύει πολύτιμη ενέργεια.", "In the past, flamingos only passed through here on migration. In recent years more and more stay the whole winter. Ornithologists are pleased, but worry about uncontrolled building around the wetlands and about visitors who get too close for a photo. A flock that is frightened, they tell us, wastes precious energy."),
 ],
 "questions": [
  Q("Από πού προέρχεται το ροζ χρώμα των φλαμίνγκο;", ["Από τον ήλιο", "Από τις χρωστικές ουσίες της τροφής τους", "Από το αλάτι", "Είναι έμφυτο"], 1, "Προέρχεται από τις χρωστικές ουσίες"),
  Q("Τι έχει αλλάξει τα τελευταία χρόνια;", ["Τα φλαμίνγκο δεν έρχονται πια", "Όλο και περισσότερα μένουν όλο τον χειμώνα", "Οι αλυκές έκλεισαν", "Απαγορεύτηκαν οι επισκέπτες"], 1, "όλο και περισσότερα μένουν όλο τον χειμώνα"),
  Q("Γιατί είναι πρόβλημα να πλησιάζουν οι επισκέπτες;", ["Γιατί τα πουλιά επιτίθενται", "Γιατί ένα κοπάδι που τρομάζει ξοδεύει πολύτιμη ενέργεια", "Γιατί χαλάνε το αλάτι", "Γιατί είναι επικίνδυνο το νερό"], 1, "Ένα κοπάδι που τρομάζει, μας λένε, ξοδεύει πολύτιμη ενέργεια"),
 ],
 "gloss": {"αλυκές": "αλυκή — salt pan", "ρηχά": "ρηχός — shallow", "φοινικόπτερα": "φοινικόπτερο — flamingo", "ορνιθολόγος": "ορνιθολόγος — ornithologist", "έμφυτο": "έμφυτος — innate", "χρωστικές ουσίες": "χρωστική ουσία — pigment", "καρκινοειδή": "καρκινοειδές — crustacean", "ξεθωριάζει": "ξεθωριάζω — to fade", "υγροτόπους": "υγρότοπος — wetland", "κοπάδι": "κοπάδι — flock"},
})

ITEMS.append({
 "id": "l74-mono-propappous", "title": "Ψάχνοντας τον προπάππου μου", "title_en": "Looking for my great-grandfather", "type": "monologue", "level": "B2",
 "context_el": "Ένας άντρας μιλάει σε μια ραδιοφωνική εκπομπή για την έρευνα που έκανε για την ιστορία της οικογένειάς του.",
 "script": [
  L("Αντώνης", "m", "Όλα ξεκίνησαν από μια φωτογραφία που βρήκα στο συρτάρι της γιαγιάς μου: ένας νέος με στρατιωτική στολή και στην πίσω πλευρά μόνο ένα όνομα και μια χρονολογία, 1912. Κανείς στην οικογένεια δεν ήξερε να μου πει πολλά γι' αυτόν.", "It all started with a photo I found in my grandmother's drawer: a young man in military uniform and on the back only a name and a date, 1912. No one in the family could tell me much about him."),
  L("Αντώνης", "m", "Πήγα πρώτα στο δημοτολόγιο του χωριού και μετά στα ληξιαρχικά βιβλία της ενορίας, όπου ο παπάς κατέγραφε βαφτίσεις και γάμους. Έτσι βρήκα ότι ο προπάππους μου είχε γεννηθεί το 1890 και είχε πολεμήσει στους Βαλκανικούς Πολέμους. Το πιο συγκινητικό ήταν ένα γράμμα που είχε στείλει από το μέτωπο στη μητέρα του, φυλαγμένο σε ένα αρχείο στην πόλη.", "I went first to the village's municipal register and then to the parish books, where the priest recorded baptisms and weddings. That's how I found that my great-grandfather had been born in 1890 and had fought in the Balkan Wars. The most moving thing was a letter he had sent from the front to his mother, kept in an archive in the town."),
  L("Αντώνης", "m", "Χρειάστηκα σχεδόν δύο χρόνια. Πολλές φορές τα στοιχεία δεν ταίριαζαν, γιατί τα ονόματα γράφονταν με διαφορετική ορθογραφία κάθε φορά. Αλλά τώρα, όταν κοιτάζω τη φωτογραφία, δεν βλέπω έναν άγνωστο. Βλέπω έναν άνθρωπο που φοβόταν, ήλπιζε και έγραφε στη μάνα του να μην ανησυχεί.", "It took me almost two years. Many times the details didn't match, because names were written with a different spelling each time. But now, when I look at the photo, I don't see a stranger. I see a man who was afraid, who hoped and wrote to his mother not to worry."),
 ],
 "questions": [
  Q("Τι ξεκίνησε την έρευνα του Αντώνη;", ["Ένα γράμμα από την Αμερική", "Μια φωτογραφία στο συρτάρι της γιαγιάς του", "Μια τηλεοπτική εκπομπή", "Μια διαθήκη"], 1, "Όλα ξεκίνησαν από μια φωτογραφία που βρήκα στο συρτάρι της γιαγιάς μου"),
  Q("Τι ήταν το πιο συγκινητικό εύρημα;", ["Ένα μετάλλιο", "Ένα γράμμα από το μέτωπο στη μητέρα του", "Η στολή του", "Ένα ημερολόγιο"], 1, "ένα γράμμα που είχε στείλει από το μέτωπο στη μητέρα του"),
  Q("Γιατί πολλές φορές τα στοιχεία δεν ταίριαζαν;", ["Γιατί είχαν καεί αρχεία", "Γιατί τα ονόματα γράφονταν με διαφορετική ορθογραφία", "Γιατί ο παπάς έκανε λάθη στις ημερομηνίες", "Γιατί η οικογένεια είχε αλλάξει επώνυμο"], 1, "τα ονόματα γράφονταν με διαφορετική ορθογραφία κάθε φορά"),
 ],
 "gloss": {"προπάππου": "προπάππους — great-grandfather", "συρτάρι": "συρτάρι — drawer", "στολή": "στολή — uniform", "δημοτολόγιο": "δημοτολόγιο — municipal register", "ληξιαρχικά": "ληξιαρχικός — of civil records", "ενορίας": "ενορία — parish", "βαφτίσεις": "βάφτιση — baptism", "μέτωπο": "μέτωπο — front (in war)", "αρχείο": "αρχείο — archive"},
})

ITEMS.append({
 "id": "l74-mono-enorkos", "title": "Ένορκος σε μια δίκη", "title_en": "A juror at a trial", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα περιγράφει σε ένα podcast την εμπειρία της ως ένορκη σε ένα μικτό ορκωτό δικαστήριο.",
 "script": [
  L("Σοφία", "f", "Όταν έλαβα την κλήση, νόμιζα ότι ήταν λάθος. Είχα κληρωθεί ένορκη. Στην Ελλάδα, στα μικτά ορκωτά δικαστήρια, τρεις δικαστές κρίνουν μαζί με τέσσερις απλούς πολίτες, και εκείνη τη φορά ένας από αυτούς τους πολίτες ήμουν εγώ.", "When I received the summons, I thought it was a mistake. I had been drawn by lot as a juror. In Greece, in the mixed jury courts, three judges decide together with four ordinary citizens, and that time one of those citizens was me."),
  L("Σοφία", "f", "Η δίκη κράτησε τρεις εβδομάδες. Άκουγα μάρτυρες, κοίταζα τον κατηγορούμενο και αναρωτιόμουν αν έχω το δικαίωμα να αποφασίσω για τη ζωή ενός ανθρώπου. Οι δικαστές μάς εξηγούσαν τους νόμους με υπομονή, αλλά επέμεναν σε ένα πράγμα: να κρίνουμε μόνο με βάση όσα ακούσαμε στην αίθουσα, όχι όσα γράφτηκαν στις εφημερίδες.", "The trial lasted three weeks. I listened to witnesses, looked at the defendant and wondered whether I had the right to decide about a person's life. The judges explained the laws to us patiently, but they insisted on one thing: that we judge only on the basis of what we heard in the courtroom, not what was written in the newspapers."),
  L("Σοφία", "f", "Βγήκα από εκεί κουρασμένη, αλλά με μεγαλύτερο σεβασμό για τη δικαιοσύνη. Κατάλαβα πόσο εύκολα βγάζουμε συμπεράσματα από έναν τίτλο στο κινητό, και πόσο δύσκολο είναι να κρίνεις κάποιον όταν τον έχεις μπροστά σου και ξέρεις όλες τις λεπτομέρειες.", "I came out of there tired, but with greater respect for justice. I understood how easily we draw conclusions from a headline on our phone, and how hard it is to judge someone when you have them in front of you and know all the details."),
 ],
 "questions": [
  Q("Ποιοι κρίνουν σε ένα μικτό ορκωτό δικαστήριο;", ["Μόνο δικαστές", "Τρεις δικαστές μαζί με τέσσερις απλούς πολίτες", "Δώδεκα ένορκοι", "Ένας δικαστής και δύο δικηγόροι"], 1, "τρεις δικαστές κρίνουν μαζί με τέσσερις απλούς πολίτες"),
  Q("Σε τι επέμεναν οι δικαστές;", ["Να διαβάζουν τις εφημερίδες", "Να κρίνουν μόνο με βάση όσα άκουσαν στην αίθουσα", "Να μη μιλούν στους μάρτυρες", "Να τελειώσουν γρήγορα"], 1, "να κρίνουμε μόνο με βάση όσα ακούσαμε στην αίθουσα"),
  Q("Τι κατάλαβε η Σοφία από την εμπειρία;", ["Ότι οι δικαστές κάνουν λάθη", "Πόσο εύκολα βγάζουμε συμπεράσματα από έναν τίτλο στο κινητό", "Ότι δεν θέλει να ξαναγίνει ένορκη", "Ότι οι νόμοι είναι άδικοι"], 1, "πόσο εύκολα βγάζουμε συμπεράσματα από έναν τίτλο στο κινητό"),
 ],
 "gloss": {"ένορκη": "ένορκος — juror", "μικτό ορκωτό δικαστήριο": "μικτό ορκωτό δικαστήριο — mixed jury court", "κλήση": "κλήση — summons", "κληρωθεί": "κληρώνομαι — to be drawn by lot", "μάρτυρες": "μάρτυρας — witness", "κατηγορούμενο": "κατηγορούμενος — defendant", "αίθουσα": "αίθουσα — (court)room", "δικαιοσύνη": "δικαιοσύνη — justice", "συμπεράσματα": "συμπέρασμα — conclusion"},
})

ITEMS.append({
 "id": "l74-c1-evangelika", "title": "Τα Ευαγγελικά του 1901", "title_en": "The Gospel riots of 1901", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε έναν ιστορικό της γλώσσας να μιλάει σε μια σειρά διαλέξεων για το γλωσσικό ζήτημα.",
 "script": [
  L("Ιστορικός", "m", "Τον Νοέμβριο του 1901 η Αθήνα έζησε κάτι που σήμερα μοιάζει απίστευτο: ανθρώπους να σκοτώνονται στους δρόμους εξαιτίας μιας μετάφρασης. Η εφημερίδα «Ακρόπολις» είχε αρχίσει να δημοσιεύει σε συνέχειες τα Ευαγγέλια μεταφρασμένα στη δημοτική από τον Αλέξανδρο Πάλλη.", "In November 1901 Athens experienced something that seems unbelievable today: people being killed in the streets because of a translation. The newspaper Akropolis had begun publishing in instalments the Gospels translated into demotic by Alexandros Pallis."),
  L("Ιστορικός", "m", "Για τους υπερασπιστές της καθαρεύουσας, και για μεγάλο μέρος της Εκκλησίας, η απόδοση του ιερού κειμένου στη γλώσσα του λαού ισοδυναμούσε με βεβήλωση. Φοιτητές του Πανεπιστημίου, υποκινούμενοι από καθηγητές τους, βγήκαν στους δρόμους. Οι συγκρούσεις με τον στρατό άφησαν πίσω τους τουλάχιστον οκτώ νεκρούς.", "For the defenders of katharevousa, and for a large part of the Church, rendering the sacred text in the language of the people amounted to desecration. University students, incited by their professors, took to the streets. The clashes with the army left at least eight dead."),
  L("Ιστορικός", "m", "Οι πολιτικές συνέπειες ήταν άμεσες: παραιτήθηκαν ο μητροπολίτης Αθηνών Προκόπιος και η κυβέρνηση Θεοτόκη. Η μετάφραση των Γραφών απαγορεύτηκε, και η απαγόρευση αυτή κατοχυρώθηκε αργότερα και στο Σύνταγμα.", "The political consequences were immediate: the Metropolitan of Athens, Prokopios, and the Theotokis government resigned. Translation of the Scriptures was banned, and that ban was later enshrined in the Constitution as well."),
  L("Ιστορικός", "m", "Αξίζει να σταθούμε σε μια ειρωνεία. Όσοι πολεμούσαν τη δημοτική στο όνομα της παράδοσης την ίδια τη μιλούσαν κάθε μέρα στο σπίτι τους. Το γλωσσικό ζήτημα δεν αφορούσε ποτέ μόνο τη γλώσσα· αφορούσε το ποιος έχει το δικαίωμα να μιλά για το έθνος και με ποια φωνή. Χρειάστηκαν ακόμα εβδομήντα πέντε χρόνια, ως το 1976, για να καθιερωθεί η δημοτική ως επίσημη γλώσσα του κράτους.", "It is worth dwelling on an irony. Those who fought demotic in the name of tradition spoke it themselves every day at home. The language question was never only about language; it was about who has the right to speak for the nation and in what voice. It took another seventy-five years, until 1976, for demotic to be established as the official language of the state."),
 ],
 "questions": [
  Q("Τι είχε αρχίσει να δημοσιεύει η «Ακρόπολις»;", ["Ποιήματα στην καθαρεύουσα", "Τα Ευαγγέλια μεταφρασμένα στη δημοτική", "Άρθρα κατά της Εκκλησίας", "Ένα μυθιστόρημα του Πάλλη"], 1, "τα Ευαγγέλια μεταφρασμένα στη δημοτική"),
  Q("Πώς έβλεπαν τη μετάφραση οι υπερασπιστές της καθαρεύουσας;", ["Ως χρήσιμη για τον λαό", "Ως βεβήλωση", "Ως ασήμαντη υπόθεση", "Ως ευκαιρία για μεταρρύθμιση"], 1, "ισοδυναμούσε με βεβήλωση"),
  Q("Ποια ήταν μία από τις πολιτικές συνέπειες;", ["Έγιναν εκλογές", "Παραιτήθηκε η κυβέρνηση Θεοτόκη", "Έκλεισε το Πανεπιστήμιο", "Καθιερώθηκε η δημοτική"], 1, "παραιτήθηκαν ο μητροπολίτης Αθηνών Προκόπιος και η κυβέρνηση Θεοτόκη"),
  Q("Ποια ειρωνεία επισημαίνει ο ιστορικός;", ["Ότι ο Πάλλης δεν ήξερε δημοτική", "Ότι όσοι πολεμούσαν τη δημοτική τη μιλούσαν κάθε μέρα στο σπίτι τους", "Ότι η εφημερίδα γράφτηκε στην καθαρεύουσα", "Ότι οι φοιτητές δεν είχαν διαβάσει τη μετάφραση"], 1, "Όσοι πολεμούσαν τη δημοτική στο όνομα της παράδοσης την ίδια τη μιλούσαν κάθε μέρα στο σπίτι τους"),
 ],
 "gloss": {"συνέχειες": "σε συνέχειες — in instalments", "δημοτική": "δημοτική — demotic (spoken) Greek", "καθαρεύουσας": "καθαρεύουσα — katharevousa (formal Greek)", "απόδοση": "απόδοση — rendering, translation", "ισοδυναμούσε": "ισοδυναμώ — to amount to", "βεβήλωση": "βεβήλωση — desecration", "υποκινούμενοι": "υποκινούμαι — to be incited", "κατοχυρώθηκε": "κατοχυρώνομαι — to be enshrined, secured", "καθιερωθεί": "καθιερώνομαι — to be established"},
})

ITEMS.append({
 "id": "l74-c1-amethos-paratiritis", "title": "Το φαινόμενο του αμέτοχου παρατηρητή", "title_en": "The bystander effect", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν κοινωνικό ψυχολόγο σε μια επιστημονική εκπομπή του ραδιοφώνου.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Παπαδάκη, τι ονομάζουμε «φαινόμενο του αμέτοχου παρατηρητή»;", "Mr Papadakis, what do we call the 'bystander effect'?"),
  L("Ψυχολόγος", "m", "Την τάση να βοηθάμε λιγότερο όταν υπάρχουν κι άλλοι γύρω μας. Όσο περισσότεροι είναι οι παρόντες, τόσο πιο εύκολα ο καθένας υποθέτει ότι κάποιος άλλος θα αναλάβει δράση. Η ευθύνη, θα λέγαμε, διαχέεται.", "The tendency to help less when there are others around us. The more people present, the more easily each one assumes that someone else will take action. Responsibility, one might say, is diffused."),
  L("Δημοσιογράφος", "f", "Πώς προέκυψε η ιδέα;", "How did the idea come about?"),
  L("Ψυχολόγος", "m", "Από έναν φόνο στη Νέα Υόρκη το 1964. Οι εφημερίδες έγραψαν ότι τριάντα οκτώ γείτονες άκουγαν και δεν έκαναν τίποτα. Δύο ψυχολόγοι σχεδίασαν τότε πειράματα που έδειξαν ότι ένας άνθρωπος μόνος του σπεύδει να βοηθήσει πολύ συχνότερα απ' ό,τι μέσα σε ομάδα. Αργότερα, βέβαια, αποδείχθηκε ότι το δημοσίευμα για τους τριάντα οκτώ μάρτυρες ήταν σε μεγάλο βαθμό υπερβολικό.", "From a murder in New York in 1964. The newspapers wrote that thirty-eight neighbours heard and did nothing. Two psychologists then designed experiments showing that a person alone rushes to help much more often than within a group. Later, of course, it emerged that the report about the thirty-eight witnesses was largely exaggerated."),
  L("Δημοσιογράφος", "f", "Ισχύει λοιπόν το φαινόμενο ή όχι;", "So does the effect hold or not?"),
  L("Ψυχολόγος", "m", "Ισχύει στο εργαστήριο, αλλά η πραγματικότητα είναι πιο αισιόδοξη. Μια μελέτη που ανέλυσε βίντεο από κάμερες ασφαλείας σε τρεις χώρες βρήκε ότι σε εννιά στις δέκα δημόσιες συγκρούσεις τουλάχιστον ένας περαστικός παρενέβη. Αν θέλετε μια πρακτική συμβουλή: όταν χρειάζεστε βοήθεια, μην απευθύνεστε στο πλήθος. Δείξτε έναν συγκεκριμένο άνθρωπο και πείτε του «εσείς, με το μπλε μπουφάν, καλέστε το εκατό».", "It holds in the laboratory, but reality is more optimistic. A study that analysed footage from security cameras in three countries found that in nine out of ten public conflicts at least one passer-by intervened. If you want a practical tip: when you need help, don't address the crowd. Point to a specific person and tell them 'you, in the blue jacket, call the police'."),
 ],
 "questions": [
  Q("Τι συμβαίνει, σύμφωνα με τον ψυχολόγο, όταν είναι παρόντες πολλοί;", ["Ο καθένας υποθέτει ότι κάποιος άλλος θα αναλάβει δράση", "Όλοι βοηθούν μαζί", "Καλούν αμέσως την αστυνομία", "Φεύγουν από τον χώρο"], 0, "ο καθένας υποθέτει ότι κάποιος άλλος θα αναλάβει δράση"),
  Q("Τι αποδείχθηκε αργότερα για το περιστατικό του 1964;", ["Ότι δεν έγινε ποτέ", "Ότι το δημοσίευμα για τους τριάντα οκτώ μάρτυρες ήταν σε μεγάλο βαθμό υπερβολικό", "Ότι οι γείτονες είχαν καλέσει όλοι την αστυνομία", "Ότι έγινε σε άλλη πόλη"], 1, "το δημοσίευμα για τους τριάντα οκτώ μάρτυρες ήταν σε μεγάλο βαθμό υπερβολικό"),
  Q("Τι βρήκε η μελέτη με τις κάμερες ασφαλείας;", ["Ότι κανείς δεν παρεμβαίνει", "Ότι σε εννιά στις δέκα συγκρούσεις τουλάχιστον ένας περαστικός παρενέβη", "Ότι οι γυναίκες βοηθούν περισσότερο", "Ότι οι κάμερες αποτρέπουν τις συγκρούσεις"], 1, "σε εννιά στις δέκα δημόσιες συγκρούσεις τουλάχιστον ένας περαστικός παρενέβη"),
  Q("Ποια πρακτική συμβουλή δίνει;", ["Να φωνάζουμε δυνατά", "Να απευθυνόμαστε σε έναν συγκεκριμένο άνθρωπο", "Να περιμένουμε την αστυνομία", "Να τραβάμε βίντεο"], 1, "Δείξτε έναν συγκεκριμένο άνθρωπο"),
 ],
 "gloss": {"αμέτοχου": "αμέτοχος — uninvolved", "παρατηρητή": "παρατηρητής — observer, bystander", "παρόντες": "παρών — present", "διαχέεται": "διαχέομαι — to be diffused", "σπεύδει": "σπεύδω — to hasten, rush", "δημοσίευμα": "δημοσίευμα — press report", "περαστικός": "περαστικός — passer-by", "παρενέβη": "παρεμβαίνω — to intervene", "απευθύνεστε": "απευθύνομαι — to address"},
})

rnd = random.Random(74)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-74.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
