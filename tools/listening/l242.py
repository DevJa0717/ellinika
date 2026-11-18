# Source for library/listening/listening-242.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l242.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l242-news-ilektriko-ferry", "title": "Ηλεκτρικό πλοίο δοκιμάζεται στη γραμμή του στενού", "title_en": "An electric ferry is being tested on the strait crossing", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός περιφερειακού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Από τη Δευτέρα, στη μικρή γραμμή που συνδέει το νησί με την απέναντι ακτή, θα κάνει δρομολόγια ένα πλοίο που δεν καίει ούτε σταγόνα πετρέλαιο. Το ηλεκτρικό πορθμείο θα λειτουργήσει πιλοτικά για έναν χρόνο, δίπλα στα δύο συμβατικά πλοία της γραμμής.", "From Monday, on the short route linking the island to the opposite coast, a ship that doesn't burn a single drop of diesel will run services. The electric ferry will operate on a trial basis for a year, alongside the route's two conventional ships."),
  L("Εκφωνητής", "m", "Το πλοίο χωράει εξήντα αυτοκίνητα και τριακόσιους επιβάτες. Η διαδρομή κρατά δεκαπέντε λεπτά, και οι μπαταρίες φορτίζουν στο λιμάνι κάθε φορά που το πλοίο φορτώνει και ξεφορτώνει, σε περίπου είκοσι λεπτά. Για τον σκοπό αυτό εγκαταστάθηκε στην προβλήτα ένας ειδικός σταθμός φόρτισης.", "The ship holds sixty cars and three hundred passengers. The crossing takes fifteen minutes, and the batteries charge in port every time the ship loads and unloads, in about twenty minutes. For this purpose, a special charging station has been installed on the quay."),
  L("Εκφωνητής", "m", "Οι κάτοικοι του λιμανιού περιμένουν κυρίως λιγότερο θόρυβο και λιγότερες αναθυμιάσεις. Η εταιρεία, από την πλευρά της, παραδέχεται ότι το πλοίο κόστισε σχεδόν διπλάσια από ένα συμβατικό, αλλά υπολογίζει ότι η διαφορά θα καλυφθεί σε λίγα χρόνια από τη φθηνότερη ενέργεια και τη μικρότερη συντήρηση.", "Residents of the port mainly expect less noise and fewer fumes. The company, for its part, admits that the ship cost almost twice as much as a conventional one, but calculates that the difference will be covered in a few years by cheaper energy and less maintenance."),
  L("Εκφωνητής", "m", "Αν η δοκιμή πετύχει, παρόμοια πλοία θα μπορούσαν να μπουν και σε άλλες μικρές γραμμές. Για μεγαλύτερες αποστάσεις, όμως, οι μπαταρίες δεν αρκούν ακόμη.", "If the trial succeeds, similar ships could also be put on other short routes. For longer distances, however, batteries are not yet enough."),
 ],
 "questions": [
  Q("Για πόσο καιρό θα λειτουργήσει πιλοτικά το ηλεκτρικό πλοίο;", ["Για έναν μήνα", "Για έναν χρόνο", "Μόνο το καλοκαίρι", "Για πέντε χρόνια"], 1, "θα λειτουργήσει πιλοτικά για έναν χρόνο"),
  Q("Πότε φορτίζουν οι μπαταρίες;", ["Τη νύχτα, όταν δεν υπάρχουν δρομολόγια", "Στο λιμάνι, κάθε φορά που το πλοίο φορτώνει και ξεφορτώνει", "Κατά τη διάρκεια της διαδρομής", "Μία φορά την εβδομάδα"], 1, "οι μπαταρίες φορτίζουν στο λιμάνι κάθε φορά που το πλοίο φορτώνει και ξεφορτώνει"),
  Q("Τι περιμένουν κυρίως οι κάτοικοι του λιμανιού;", ["Φθηνότερα εισιτήρια", "Λιγότερο θόρυβο και λιγότερες αναθυμιάσεις", "Περισσότερα δρομολόγια", "Νέες θέσεις εργασίας"], 1, "περιμένουν κυρίως λιγότερο θόρυβο και λιγότερες αναθυμιάσεις"),
  Q("Γιατί δεν χρησιμοποιούνται ακόμη τέτοια πλοία σε μεγάλες αποστάσεις;", ["Γιατί είναι πολύ αργά", "Γιατί οι μπαταρίες δεν αρκούν ακόμη", "Γιατί το απαγορεύει ο νόμος", "Γιατί δεν χωρούν αυτοκίνητα"], 1, "Για μεγαλύτερες αποστάσεις, όμως, οι μπαταρίες δεν αρκούν ακόμη"),
 ],
 "gloss": {"δρομολόγια": "δρομολόγιο — (scheduled) service, run", "σταγόνα": "σταγόνα — drop", "πορθμείο": "πορθμείο — ferry", "πιλοτικά": "πιλοτικά — on a trial basis", "συμβατικά": "συμβατικός — conventional", "μπαταρίες": "μπαταρία — battery", "προβλήτα": "προβλήτα — quay, pier", "αναθυμιάσεις": "αναθυμίαση — fumes", "παραδέχεται": "παραδέχομαι — to admit", "συντήρηση": "συντήρηση — maintenance"},
})

ITEMS.append({
 "id": "l242-vm-tyrokomos-graviera", "title": "Μήνυμα από τον τυροκόμο για τη γραβιέρα της βάφτισης", "title_en": "A message from the cheesemaker about the graviera for the christening", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε παραγγείλει τυρί από ένα μικρό τυροκομείο για το τραπέζι μιας βάφτισης. Ακούτε ένα μήνυμα που σας άφησε ο τυροκόμος στον τηλεφωνητή.",
 "script": [
  L("Τυροκόμος", "m", "Γεια σας, ο Μανώλης είμαι, από το τυροκομείο στο χωριό. Σας παίρνω για την παραγγελία της βάφτισης. Μου είχατε ζητήσει δύο κεφάλια γραβιέρα των οχτώ μηνών, αλλά δυστυχώς από αυτή την ηλικία μου έχει μείνει μόνο ένα.", "Hello, it's Manolis, from the cheese dairy in the village. I'm calling about the christening order. You'd asked me for two wheels of eight-month graviera, but unfortunately I've only got one left of that age."),
  L("Τυροκόμος", "m", "Σας προτείνω για το δεύτερο κεφάλι μια γραβιέρα των τεσσάρων μηνών. Είναι πιο μαλακή και λιγότερο αλμυρή, και πολλοί τη θεωρούν καλύτερη για να τρώγεται σκέτη, με λίγο μέλι. Η παλιά, αντίθετα, ταιριάζει περισσότερο με κρασί ή για τρίψιμο στα μακαρόνια.", "For the second wheel, I suggest a four-month graviera. It's softer and less salty, and many people think it's better for eating on its own, with a little honey. The aged one, on the other hand, goes better with wine or for grating over pasta."),
  L("Τυροκόμος", "m", "Η νεότερη κοστίζει λίγο φθηνότερα το κιλό, οπότε θα σας κάνω και μια μικρή έκπτωση στο σύνολο. Το κάθε κεφάλι ζυγίζει γύρω στα έξι κιλά, και θα σας τα στείλω κομμένα σε κομμάτια, τυλιγμένα σε λαδόχαρτο, αν θέλετε.", "The younger one costs a bit less per kilo, so I'll also give you a small discount on the total. Each wheel weighs around six kilos, and I'll send them cut into pieces, wrapped in greaseproof paper, if you like."),
  L("Τυροκόμος", "m", "Για να προλάβει το ΚΤΕΛ της Πέμπτης, πρέπει να ξέρω ως αύριο το βράδυ τι αποφασίσατε. Και θυμηθείτε να βγάλετε το τυρί από το ψυγείο μία ώρα πριν το σερβίρετε, για να βγάλει όλο το άρωμά του. Καλή συνέχεια.", "To make Thursday's intercity bus, I need to know by tomorrow evening what you've decided. And remember to take the cheese out of the fridge an hour before serving it, so it gives off all its aroma. All the best."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με την παραγγελία;", ["Το τυρί χάλασε", "Έχει μείνει μόνο ένα κεφάλι γραβιέρα των οχτώ μηνών", "Η τιμή ανέβηκε πολύ", "Το ΚΤΕΛ δεν πάει στο χωριό"], 1, "από αυτή την ηλικία μου έχει μείνει μόνο ένα"),
  Q("Πώς είναι η γραβιέρα των τεσσάρων μηνών, σε σχέση με την παλιά;", ["Πιο σκληρή και πιο αλμυρή", "Πιο μαλακή και λιγότερο αλμυρή", "Πιο ακριβή", "Καλύτερη για τρίψιμο"], 1, "Είναι πιο μαλακή και λιγότερο αλμυρή"),
  Q("Τι προσφέρει ο τυροκόμος για την αλλαγή;", ["Δωρεάν μεταφορά", "Μια μικρή έκπτωση στο σύνολο", "Ένα βάζο μέλι", "Ένα τρίτο κεφάλι"], 1, "θα σας κάνω και μια μικρή έκπτωση στο σύνολο"),
  Q("Τι συμβουλεύει για το σερβίρισμα;", ["Να κοπεί το τυρί την προηγούμενη μέρα", "Να βγει από το ψυγείο μία ώρα πριν", "Να σερβιριστεί ζεστό", "Να μείνει τυλιγμένο ως το τέλος"], 1, "να βγάλετε το τυρί από το ψυγείο μία ώρα πριν το σερβίρετε"),
 ],
 "gloss": {"τυροκομείο": "τυροκομείο — cheese dairy", "κεφάλια": "κεφάλι (τυριού) — wheel (of cheese)", "γραβιέρα": "γραβιέρα — graviera (hard Greek cheese)", "σκέτη": "σκέτος — on its own, plain", "τρίψιμο": "τρίψιμο — grating", "έκπτωση": "έκπτωση — discount", "ζυγίζει": "ζυγίζω — to weigh", "λαδόχαρτο": "λαδόχαρτο — greaseproof paper", "ΚΤΕΛ": "ΚΤΕΛ — intercity bus service", "άρωμά": "άρωμα — aroma"},
})

ITEMS.append({
 "id": "l242-c1-mono-syndetiras", "title": "Ένα σύρμα με δύο στροφές: η ιστορία του συνδετήρα", "title_en": "A wire with two turns: the history of the paperclip", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ιστορικό του σχεδιασμού σε μια ραδιοφωνική εκπομπή για τα αντικείμενα της καθημερινής ζωής.",
 "script": [
  L("Ιστορικός", "f", "Πριν από τον συνδετήρα, τα χαρτιά τα κρατούσαν μαζί με καρφίτσες ή τα έραβαν με κλωστή. Και τα δύο είχαν μειονεκτήματα: οι καρφίτσες σκούριαζαν και τρυπούσαν το χαρτί, και η κλωστή ήθελε χρόνο. Όταν, τον δέκατο ένατο αιώνα, έγινε φθηνό το ατσάλινο σύρμα, ήταν θέμα χρόνου να βρεθεί κάτι καλύτερο.", "Before the paperclip, papers were held together with pins or sewn with thread. Both had drawbacks: pins rusted and pierced the paper, and thread took time. When steel wire became cheap in the nineteenth century, it was a matter of time before something better was found."),
  L("Ιστορικός", "f", "Στα τέλη του αιώνα κατοχυρώθηκαν με δίπλωμα ευρεσιτεχνίας δεκάδες σχέδια. Το πιο γνωστό σήμερα, με τις δύο οβάλ στροφές, συνδέεται με το όνομα μιας βρετανικής εταιρείας, της «Gem», αλλά, απ' όσο ξέρουμε, δεν κατοχυρώθηκε ποτέ, και κανείς δεν ξέρει με βεβαιότητα ποιος το σχεδίασε πρώτος.", "At the end of the century dozens of designs were patented. The best known today, with the two oval turns, is linked with the name of a British company, 'Gem', but as far as we know it was never patented, and nobody knows for sure who designed it first."),
  L("Ιστορικός", "f", "Στη Νορβηγία, πάντως, πολλοί μεγάλωσαν πιστεύοντας ότι τον συνδετήρα τον εφηύρε ένας συμπατριώτης τους, ο Γιόχαν Βόλερ. Ο Βόλερ πράγματι πήρε δίπλωμα για ένα σχέδιο, αλλά ήταν διαφορετικό και λιγότερο πρακτικό. Ο μύθος, ωστόσο, απέκτησε άλλη δύναμη στον Δεύτερο Παγκόσμιο Πόλεμο, όταν κάποιοι Νορβηγοί φορούσαν συνδετήρες στο πέτο τους, ως σιωπηλό σύμβολο ενότητας απέναντι στην κατοχή.", "In Norway, though, many grew up believing that the paperclip was invented by a fellow countryman, Johan Vaaler. Vaaler did get a patent for a design, but it was different and less practical. The myth, however, gained new force in the Second World War, when some Norwegians wore paperclips on their lapels as a silent symbol of unity against the occupation."),
  L("Ιστορικός", "f", "Η ιστορία του συνδετήρα, λοιπόν, μας θυμίζει δύο πράγματα. Πρώτον, ότι τα πιο απλά αντικείμενα είναι συχνά τα πιο δύσκολα να τα αποδώσεις σε έναν εφευρέτη. Και δεύτερον, ότι ένα μικρό κομμάτι σύρμα μπορεί να κουβαλήσει πολύ περισσότερο νόημα απ' όσο μερικά φύλλα χαρτί.", "The history of the paperclip, then, reminds us of two things. First, that the simplest objects are often the hardest to attribute to a single inventor. And second, that a small piece of wire can carry much more meaning than a few sheets of paper."),
 ],
 "questions": [
  Q("Ποιο ήταν το μειονέκτημα των καρφιτσών;", ["Ήταν πολύ ακριβές", "Σκούριαζαν και τρυπούσαν το χαρτί", "Χάνονταν εύκολα", "Δεν κρατούσαν πολλά φύλλα"], 1, "οι καρφίτσες σκούριαζαν και τρυπούσαν το χαρτί"),
  Q("Τι λέει η ιστορικός για το σχέδιο με τις δύο οβάλ στροφές;", ["Ότι το σχεδίασε ο Βόλερ", "Ότι, απ' όσο ξέρουμε, δεν κατοχυρώθηκε ποτέ", "Ότι εφευρέθηκε στην Αμερική", "Ότι είναι το πιο πρόσφατο σχέδιο"], 1, "απ' όσο ξέρουμε, δεν κατοχυρώθηκε ποτέ"),
  Q("Τι ισχύει για το σχέδιο του Γιόχαν Βόλερ;", ["Ήταν ίδιο με τον σημερινό συνδετήρα", "Ήταν διαφορετικό και λιγότερο πρακτικό", "Δεν κατοχυρώθηκε ποτέ", "Χρησιμοποιήθηκε στον πόλεμο"], 1, "ήταν διαφορετικό και λιγότερο πρακτικό"),
  Q("Γιατί φορούσαν κάποιοι Νορβηγοί συνδετήρες στον πόλεμο;", ["Για να κρατούν τα έγγραφά τους", "Ως σιωπηλό σύμβολο ενότητας απέναντι στην κατοχή", "Ως διακριτικό του στρατού", "Για να τιμήσουν τον Βόλερ"], 1, "ως σιωπηλό σύμβολο ενότητας απέναντι στην κατοχή"),
 ],
 "gloss": {"συνδετήρα": "συνδετήρας — paperclip", "καρφίτσες": "καρφίτσα — pin", "έραβαν": "ράβω — to sew", "κλωστή": "κλωστή — thread", "μειονεκτήματα": "μειονέκτημα — drawback", "σκούριαζαν": "σκουριάζω — to rust", "ατσάλινο": "ατσάλινος — steel", "σύρμα": "σύρμα — wire", "κατοχυρώθηκαν": "κατοχυρώνω — to patent, secure legally", "δίπλωμα ευρεσιτεχνίας": "δίπλωμα ευρεσιτεχνίας — patent", "συμπατριώτης": "συμπατριώτης — fellow countryman", "πέτο": "πέτο — lapel", "αποδώσεις": "αποδίδω — to attribute"},
})

ITEMS.append({
 "id": "l242-c1-int-erpetologos", "title": "Ένας ερπετολόγος για τα φίδια της Ελλάδας", "title_en": "A herpetologist on the snakes of Greece", "type": "interview", "level": "C1",
 "context_el": "Ένας ερπετολόγος, δηλαδή ένας βιολόγος που μελετά τα ερπετά, μιλά σε μια ραδιοφωνική εκπομπή για τη φύση.",
 "script": [
  L("Δημοσιογράφος", "f", "Τα φίδια τα φοβούνται πολλοί. Πόσο δικαιολογημένος είναι αυτός ο φόβος στην Ελλάδα;", "Many people are afraid of snakes. How justified is this fear in Greece?"),
  L("Ερπετολόγος", "m", "Πολύ λιγότερο απ' όσο νομίζουμε. Στη χώρα μας ζουν περίπου είκοσι είδη φιδιών, και η μεγάλη πλειονότητα είναι εντελώς ακίνδυνη για τον άνθρωπο. Τα μόνα που μπορούν να προκαλέσουν σοβαρό πρόβλημα με το δάγκωμά τους είναι οι οχιές, και ακόμη κι αυτές σπάνια σκοτώνουν, ειδικά αν ο τραυματίας πάει γρήγορα στο νοσοκομείο.", "Much less than we think. Around twenty species of snakes live in our country, and the vast majority are completely harmless to humans. The only ones that can cause a serious problem with their bite are the vipers, and even they rarely kill, especially if the injured person goes quickly to hospital."),
  L("Δημοσιογράφος", "f", "Πότε δαγκώνει ένα φίδι;", "When does a snake bite?"),
  L("Ερπετολόγος", "m", "Σχεδόν πάντα όταν νιώθει ότι απειλείται. Τα περισσότερα δαγκώματα συμβαίνουν όταν κάποιος προσπαθεί να πιάσει ή να σκοτώσει το φίδι, ή όταν βάζει το χέρι του κάπου χωρίς να κοιτάξει, σε μια ξερολιθιά, για παράδειγμα. Αν συναντήσετε ένα φίδι στο μονοπάτι, το καλύτερο που έχετε να κάνετε είναι να σταθείτε και να το αφήσετε να φύγει. Δεν σας κυνηγάει· θέλει απλώς να ξεφύγει.", "Almost always when it feels threatened. Most bites happen when someone tries to catch or kill the snake, or puts their hand somewhere without looking, in a dry-stone wall, for example. If you meet a snake on the path, the best thing you can do is to stand still and let it go away. It isn't chasing you; it just wants to escape."),
  L("Δημοσιογράφος", "f", "Υπάρχουν φίδια που κινδυνεύουν;", "Are there snakes that are endangered?"),
  L("Ερπετολόγος", "m", "Ναι. Το πιο χαρακτηριστικό παράδειγμα είναι η οχιά της Μήλου, που ζει μόνο στη Μήλο και σε μερικά γειτονικά νησάκια. Είναι προστατευόμενο είδος, αλλά απειλείται από την καταστροφή του βιότοπού της, από τα αυτοκίνητα και, δυστυχώς, από ανθρώπους που τη σκοτώνουν από φόβο. Λέω συχνά ότι το φίδι κινδυνεύει από εμάς πολύ περισσότερο απ' ό,τι εμείς από αυτό.", "Yes. The most typical example is the Milos viper, which lives only on Milos and a few neighbouring islets. It is a protected species, but it is threatened by the destruction of its habitat, by cars and, unfortunately, by people who kill it out of fear. I often say that the snake is in much more danger from us than we are from it."),
 ],
 "questions": [
  Q("Πόσο επικίνδυνα είναι τα περισσότερα φίδια της Ελλάδας, σύμφωνα με τον ερπετολόγο;", ["Πολύ επικίνδυνα", "Η μεγάλη πλειονότητα είναι εντελώς ακίνδυνη", "Επικίνδυνα μόνο το καλοκαίρι", "Επικίνδυνα για τα παιδιά"], 1, "η μεγάλη πλειονότητα είναι εντελώς ακίνδυνη για τον άνθρωπο"),
  Q("Πότε συμβαίνουν τα περισσότερα δαγκώματα;", ["Τη νύχτα", "Όταν κάποιος προσπαθεί να πιάσει ή να σκοτώσει το φίδι", "Όταν το φίδι πεινάει", "Στο κολύμπι"], 1, "όταν κάποιος προσπαθεί να πιάσει ή να σκοτώσει το φίδι"),
  Q("Τι συμβουλεύει αν συναντήσει κανείς φίδι στο μονοπάτι;", ["Να τρέξει μακριά", "Να σταθεί και να το αφήσει να φύγει", "Να το διώξει με ένα ξύλο", "Να κάνει θόρυβο"], 1, "να σταθείτε και να το αφήσετε να φύγει"),
  Q("Πού ζει η οχιά της Μήλου;", ["Σε όλες τις Κυκλάδες", "Μόνο στη Μήλο και σε μερικά γειτονικά νησάκια", "Στην Κρήτη", "Στα βουνά της Πίνδου"], 1, "ζει μόνο στη Μήλο και σε μερικά γειτονικά νησάκια"),
 ],
 "gloss": {"ερπετολόγος": "ερπετολόγος — herpetologist", "ερπετά": "ερπετό — reptile", "πλειονότητα": "πλειονότητα — majority", "ακίνδυνη": "ακίνδυνος — harmless", "δάγκωμά": "δάγκωμα — bite", "οχιές": "οχιά — viper", "τραυματίας": "τραυματίας — injured person", "απειλείται": "απειλούμαι — to be threatened", "ξερολιθιά": "ξερολιθιά — dry-stone wall", "ξεφύγει": "ξεφεύγω — to escape", "βιότοπού": "βιότοπος — habitat", "προστατευόμενο": "προστατευόμενος — protected"},
})

rnd = random.Random(242)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-242.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
