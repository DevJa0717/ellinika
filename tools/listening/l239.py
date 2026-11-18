# Source for library/listening/listening-239.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l239.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l239-news-metafyteusi-platanou", "title": "Ένας αιωνόβιος πλάτανος αλλάζει θέση για να σωθεί από τα έργα του μετρό", "title_en": "A century-old plane tree is moved to save it from the metro works", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Μια ασυνήθιστη επιχείρηση ξεκινά σήμερα στην κεντρική πλατεία της πόλης: ένας αιωνόβιος πλάτανος, ηλικίας περίπου εκατόν πενήντα χρόνων, μεταφυτεύεται σε ένα πάρκο τριακόσια μέτρα πιο μακριά, για να μη χαθεί εξαιτίας των έργων για τον νέο σταθμό του μετρό.", "An unusual operation starts today in the city's central square: a plane tree about a hundred and fifty years old is being transplanted to a park three hundred metres away, so that it isn't lost because of the works for the new metro station."),
  L("Εκφωνητής", "m", "Τις τελευταίες εβδομάδες οι γεωπόνοι του δήμου έσκαψαν γύρω από τις ρίζες και κλάδεψαν προσεκτικά τα κλαδιά, ώστε το δέντρο να χάνει όσο το δυνατόν λιγότερο νερό. Σήμερα ένας ειδικός γερανός θα σηκώσει τον πλάτανο μαζί με την μπάλα του χώματος γύρω από τις ρίζες, που ζυγίζει περίπου σαράντα τόνους.", "In recent weeks the municipality's agronomists dug around the roots and carefully pruned the branches, so that the tree loses as little water as possible. Today a special crane will lift the plane tree together with the ball of soil around its roots, which weighs about forty tonnes."),
  L("Εκφωνητής", "m", "Η μεταφορά θα γίνει τη νύχτα, με πολύ χαμηλή ταχύτητα, και οι γύρω δρόμοι θα μείνουν κλειστοί από τις δέκα το βράδυ ως τις έξι το πρωί. Οι οδηγοί καλούνται να χρησιμοποιήσουν την παραλιακή λεωφόρο.", "The move will take place at night, at very low speed, and the surrounding streets will stay closed from ten at night until six in the morning. Drivers are asked to use the seafront avenue."),
  L("Εκφωνητής", "m", "Οι ειδικοί προειδοποιούν ότι η επιτυχία δεν είναι εγγυημένη: θα χρειαστούν τουλάχιστον δύο χρόνια για να φανεί αν ο πλάτανος ρίζωσε στο καινούργιο του σπίτι.", "Experts warn that success is not guaranteed: it will take at least two years to see whether the plane tree has taken root in its new home."),
 ],
 "questions": [
  Q("Γιατί μεταφυτεύεται ο πλάτανος;", ["Γιατί είναι άρρωστος", "Για να μη χαθεί εξαιτίας των έργων του μετρό", "Γιατί το ζήτησαν οι κάτοικοι του πάρκου", "Γιατί εμποδίζει την κυκλοφορία"], 1, "για να μη χαθεί εξαιτίας των έργων για τον νέο σταθμό του μετρό"),
  Q("Γιατί κλάδεψαν οι γεωπόνοι τα κλαδιά;", ["Για να χωρέσει στο φορτηγό", "Για να χάνει το δέντρο όσο το δυνατόν λιγότερο νερό", "Για να μη ζυγίζει πολύ", "Για να μπει φως στην πλατεία"], 1, "ώστε το δέντρο να χάνει όσο το δυνατόν λιγότερο νερό"),
  Q("Πότε θα γίνει η μεταφορά;", ["Το μεσημέρι", "Τη νύχτα", "Την Κυριακή το πρωί", "Μετά από δύο χρόνια"], 1, "Η μεταφορά θα γίνει τη νύχτα"),
  Q("Πότε θα φανεί αν η μεταφύτευση πέτυχε;", ["Την επόμενη μέρα", "Σε τουλάχιστον δύο χρόνια", "Την άνοιξη", "Όταν τελειώσουν τα έργα"], 1, "θα χρειαστούν τουλάχιστον δύο χρόνια για να φανεί αν ο πλάτανος ρίζωσε"),
 ],
 "gloss": {"αιωνόβιος": "αιωνόβιος — century-old", "επιχείρηση": "επιχείρηση — operation", "πλάτανος": "πλάτανος — plane tree", "μεταφυτεύεται": "μεταφυτεύω — to transplant", "γεωπόνοι": "γεωπόνος — agronomist", "κλάδεψαν": "κλαδεύω — to prune", "γερανός": "γερανός — crane", "ζυγίζει": "ζυγίζω — to weigh", "λεωφόρο": "λεωφόρος — avenue", "εγγυημένη": "εγγυημένος — guaranteed", "ρίζωσε": "ριζώνω — to take root"},
})
ITEMS.append({
 "id": "l239-vm-akroasi-orchistras", "title": "Μήνυμα από την ορχήστρα για την ακρόασή σας", "title_en": "A message from the orchestra about your audition", "type": "voicemail", "level": "B2",
 "context_el": "Παίζετε βιολί και κάνατε αίτηση για μια θέση σε μια ορχήστρα. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Γραμματεία", "f", "Καλησπέρα σας, σας παίρνω από τη Δημοτική Συμφωνική Ορχήστρα, η Κατερίνα είμαι, από τη γραμματεία. Σας τηλεφωνώ για την ακρόαση για τη θέση του δεύτερου βιολιού, για την οποία κάνατε αίτηση.", "Good evening, I'm calling from the Municipal Symphony Orchestra, it's Katerina, from the office. I'm phoning about the audition for the second violin position you applied for."),
  L("Γραμματεία", "f", "Η ακρόαση θα γίνει στις δεκαπέντε του μήνα, στις έντεκα το πρωί, στην αίθουσα του δημοτικού ωδείου. Θα παίξετε πίσω από ένα παραβάν, ώστε η επιτροπή να μη βλέπει ποιος παίζει, μόνο να ακούει.", "The audition will be on the fifteenth of the month, at eleven in the morning, in the hall of the municipal conservatory. You will play behind a screen, so that the panel doesn't see who is playing, only hears."),
  L("Γραμματεία", "f", "Θα χρειαστεί να παίξετε ένα κομμάτι της επιλογής σας, όχι πάνω από δέκα λεπτά, και δύο αποσπάσματα από το ρεπερτόριο της ορχήστρας, που θα σας τα στείλουμε αύριο με ηλεκτρονικό ταχυδρομείο. Πιανίστα για συνοδεία δεν θα χρειαστείτε.", "You'll need to play a piece of your choice, no longer than ten minutes, and two excerpts from the orchestra's repertoire, which we'll send you by email tomorrow. You won't need a pianist to accompany you."),
  L("Γραμματεία", "f", "Παρακαλώ επιβεβαιώστε τη συμμετοχή σας ως την Παρασκευή. Και, αν γίνεται, ελάτε μισή ώρα νωρίτερα, γιατί η αίθουσα είναι κρύα και θα θέλετε χρόνο να ζεσταθείτε και να κουρδίσετε.", "Please confirm your participation by Friday. And, if possible, come half an hour early, because the hall is cold and you'll want time to warm up and tune."),
 ],
 "questions": [
  Q("Για ποια θέση είναι η ακρόαση;", ["Για τη θέση του πιανίστα", "Για τη θέση του δεύτερου βιολιού", "Για τη θέση του μαέστρου", "Για μια θέση στη γραμματεία"], 1, "για τη θέση του δεύτερου βιολιού"),
  Q("Γιατί θα παίξετε πίσω από ένα παραβάν;", ["Για να μην αγχωθείτε", "Για να μη βλέπει η επιτροπή ποιος παίζει", "Γιατί η αίθουσα είναι μικρή", "Για να ακούγεται καλύτερα ο ήχος"], 1, "ώστε η επιτροπή να μη βλέπει ποιος παίζει, μόνο να ακούει"),
  Q("Τι θα σας στείλουν αύριο;", ["Το πρόγραμμα των συναυλιών", "Δύο αποσπάσματα από το ρεπερτόριο της ορχήστρας", "Το συμβόλαιο", "Τα στοιχεία του πιανίστα"], 1, "δύο αποσπάσματα από το ρεπερτόριο της ορχήστρας, που θα σας τα στείλουμε αύριο"),
  Q("Γιατί σας ζητούν να έρθετε μισή ώρα νωρίτερα;", ["Για να συμπληρώσετε έντυπα", "Γιατί η αίθουσα είναι κρύα και θα θέλετε να ζεσταθείτε και να κουρδίσετε", "Για να γνωρίσετε τον μαέστρο", "Γιατί η ακρόαση μπορεί να αρχίσει νωρίτερα"], 1, "η αίθουσα είναι κρύα και θα θέλετε χρόνο να ζεσταθείτε και να κουρδίσετε"),
 ],
 "gloss": {"ακρόαση": "ακρόαση — audition", "βιολιού": "βιολί — violin", "ωδείου": "ωδείο — conservatory, music school", "παραβάν": "παραβάν — (folding) screen", "επιτροπή": "επιτροπή — panel, committee", "αποσπάσματα": "απόσπασμα — excerpt", "ρεπερτόριο": "ρεπερτόριο — repertoire", "συνοδεία": "συνοδεία — accompaniment", "επιβεβαιώστε": "επιβεβαιώνω — to confirm", "κουρδίσετε": "κουρδίζω — to tune"},
})
ITEMS.append({
 "id": "l239-c1-mono-pagoto", "title": "Από το χιόνι των βουνών στη μηχανή με τη μανιβέλα: η ιστορία του παγωτού", "title_en": "From mountain snow to the hand-cranked machine: the history of ice cream", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ιστορικό της διατροφής σε μια ραδιοφωνική εκπομπή για τη γαστρονομία.",
 "script": [
  L("Ιστορικός", "m", "Πολύ πριν από τα ψυγεία, οι άνθρωποι έβρισκαν τρόπους να απολαμβάνουν κάτι παγωμένο το καλοκαίρι. Στην αρχαία Περσία έχτιζαν ψηλές θολωτές κατασκευές, όπου φύλαγαν τον πάγο του χειμώνα, και σε πολλές περιοχές της Μεσογείου μάζευαν χιόνι από τα βουνά και το έθαβαν σε λάκκους σκεπασμένους με άχυρα.", "Long before refrigerators, people found ways to enjoy something frozen in summer. In ancient Persia they built tall domed structures where they stored the winter's ice, and in many parts of the Mediterranean they gathered snow from the mountains and buried it in pits covered with straw."),
  L("Ιστορικός", "m", "Αυτό που έτρωγαν, όμως, δεν ήταν παγωτό με τη σημερινή έννοια. Ήταν χιόνι ή πάγος με σιρόπι, χυμό φρούτων ή μέλι. Η λέξη «σορμπέ» μάς θυμίζει αυτή την παράδοση: προέρχεται, μέσω των ιταλικών και των τουρκικών, από μια αραβική λέξη που σημαίνει ποτό.", "What they ate, however, wasn't ice cream in today's sense. It was snow or ice with syrup, fruit juice or honey. The word 'sorbet' reminds us of that tradition: it comes, via Italian and Turkish, from an Arabic word meaning a drink."),
  L("Ιστορικός", "m", "Η μεγάλη ανακάλυψη ήταν μάλλον τεχνική. Κάποια στιγμή, πιθανότατα τον δέκατο έκτο αιώνα, οι Ευρωπαίοι έμαθαν ότι, αν ανακατέψεις πάγο με αλάτι, η θερμοκρασία πέφτει πολύ κάτω από το μηδέν. Ένα δοχείο με γάλα ή κρέμα, βυθισμένο σε αυτό το μείγμα, μπορούσε πια να παγώσει. Έτσι γεννήθηκε το παγωτό όπως το ξέρουμε.", "The great discovery was really a technical one. At some point, probably in the sixteenth century, Europeans learned that if you mix ice with salt, the temperature drops well below zero. A container of milk or cream, sunk into that mixture, could now freeze. That's how ice cream as we know it was born."),
  L("Ιστορικός", "m", "Για αιώνες ήταν πολυτέλεια των αυλών και των ακριβών καφενείων. Μόνο τον δέκατο ένατο αιώνα, με τη βιομηχανική παραγωγή πάγου και τις πρώτες μηχανές με μανιβέλα, έγινε ένα φτηνό καλοκαιρινό γλυκό για όλους. Κι όμως, ο βασικός κανόνας δεν άλλαξε ποτέ: για να παγώσει κάτι, πρέπει κάτι άλλο να του πάρει τη θερμότητα.", "For centuries it was a luxury of royal courts and expensive cafés. Only in the nineteenth century, with industrial ice production and the first hand-cranked machines, did it become a cheap summer treat for everyone. And yet the basic rule never changed: for something to freeze, something else has to take its heat away."),
 ],
 "questions": [
  Q("Πού φύλαγαν τον πάγο στην αρχαία Περσία;", ["Σε βαθιά πηγάδια", "Σε ψηλές θολωτές κατασκευές", "Σε σπηλιές των βουνών", "Σε ξύλινα βαρέλια"], 1, "έχτιζαν ψηλές θολωτές κατασκευές, όπου φύλαγαν τον πάγο του χειμώνα"),
  Q("Τι έτρωγαν παλιότερα αντί για παγωτό;", ["Παγωμένο γάλα", "Χιόνι ή πάγο με σιρόπι, χυμό ή μέλι", "Παγωμένα φρούτα", "Κρέμα με ζάχαρη"], 1, "Ήταν χιόνι ή πάγος με σιρόπι, χυμό φρούτων ή μέλι"),
  Q("Ποια ήταν, κατά τον ομιλητή, η μεγάλη ανακάλυψη;", ["Η ζάχαρη από τα ζαχαροκάλαμα", "Ότι ο πάγος με αλάτι κατεβάζει τη θερμοκρασία πολύ κάτω από το μηδέν", "Το ηλεκτρικό ψυγείο", "Η κρέμα γάλακτος"], 1, "αν ανακατέψεις πάγο με αλάτι, η θερμοκρασία πέφτει πολύ κάτω από το μηδέν"),
  Q("Πότε έγινε το παγωτό φτηνό γλυκό για όλους;", ["Στην αρχαιότητα", "Τον δέκατο ένατο αιώνα", "Τον δέκατο έκτο αιώνα", "Μετά τον Δεύτερο Παγκόσμιο Πόλεμο"], 1, "Μόνο τον δέκατο ένατο αιώνα … έγινε ένα φτηνό καλοκαιρινό γλυκό για όλους"),
 ],
 "gloss": {"θολωτές": "θολωτός — domed, vaulted", "κατασκευές": "κατασκευή — structure", "λάκκους": "λάκκος — pit", "άχυρα": "άχυρο — straw", "σιρόπι": "σιρόπι — syrup", "σορμπέ": "σορμπέ — sorbet", "δοχείο": "δοχείο — container", "βυθισμένο": "βυθισμένος — sunk, immersed", "μείγμα": "μείγμα — mixture", "πολυτέλεια": "πολυτέλεια — luxury", "αυλών": "αυλή — (royal) court", "μανιβέλα": "μανιβέλα — crank, handle"},
})
ITEMS.append({
 "id": "l239-c1-int-leichines", "title": "Μια λειχηνολόγος για τις μικρές κηλίδες στους βράχους που μετρούν τη ρύπανση", "title_en": "A lichenologist on the little patches on rocks that measure pollution", "type": "interview", "level": "C1",
 "context_el": "Μια λειχηνολόγος, που διδάσκει βοτανική σε ένα πανεπιστήμιο, μιλά σε μια ραδιοφωνική εκπομπή για το περιβάλλον.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί δεν ξέρουν καν τι είναι οι λειχήνες. Πώς θα τις περιγράφατε;", "Many people don't even know what lichens are. How would you describe them?"),
  L("Λειχηνολόγος", "f", "Είναι αυτές οι κηλίδες, γκρίζες, κίτρινες ή πορτοκαλί, που βλέπουμε πάνω σε βράχους, σε κεραμίδια ή στον κορμό των δέντρων. Δεν είναι ένα φυτό. Είναι μια συνεργασία ανάμεσα σε έναν μύκητα και σε ένα φύκι ή ένα βακτήριο που κάνει φωτοσύνθεση. Ο μύκητας προσφέρει προστασία και νερό, και ο συνεργάτης του παράγει την τροφή.", "They're those patches, grey, yellow or orange, that we see on rocks, on roof tiles or on tree trunks. They aren't a plant. They're a partnership between a fungus and an alga or a bacterium that photosynthesises. The fungus provides protection and water, and its partner produces the food."),
  L("Δημοσιογράφος", "m", "Γιατί ενδιαφέρουν τόσο τους επιστήμονες;", "Why do they interest scientists so much?"),
  L("Λειχηνολόγος", "f", "Για πολλούς λόγους, αλλά ο πιο πρακτικός είναι ότι είναι εξαιρετικοί δείκτες της ποιότητας του αέρα. Δεν έχουν ρίζες, απορροφούν νερό και ουσίες απευθείας από την ατμόσφαιρα, και πολλά είδη είναι πολύ ευαίσθητα στη ρύπανση, ιδίως στο διοξείδιο του θείου. Τον δέκατο ένατο αιώνα, στις βιομηχανικές πόλεις της Αγγλίας, οι λειχήνες σχεδόν εξαφανίστηκαν από τα δέντρα. Όταν ο αέρας καθάρισε, άρχισαν σιγά σιγά να επιστρέφουν.", "For many reasons, but the most practical one is that they're excellent indicators of air quality. They have no roots, they absorb water and substances directly from the atmosphere, and many species are very sensitive to pollution, especially to sulphur dioxide. In the nineteenth century, in the industrial cities of England, lichens almost disappeared from the trees. When the air was cleaned up, they gradually began to return."),
  L("Δημοσιογράφος", "m", "Και πόσο γρήγορα μεγαλώνουν;", "And how fast do they grow?"),
  L("Λειχηνολόγος", "f", "Πάρα πολύ αργά. Ορισμένα είδη που ζουν πάνω σε βράχους μεγαλώνουν μόλις ένα ή δύο χιλιοστά τον χρόνο. Γι' αυτό τις χρησιμοποιούν ακόμη και οι γεωλόγοι, για να υπολογίσουν πόσο καιρό έχει μείνει εκτεθειμένη μια επιφάνεια, για παράδειγμα μετά την υποχώρηση ενός παγετώνα. Και θα έλεγα στους ακροατές: την επόμενη φορά που θα δείτε μια κίτρινη κηλίδα σε έναν παλιό τοίχο, μη βιαστείτε να την καθαρίσετε. Μπορεί να είναι μεγαλύτερη σε ηλικία από εσάς.", "Extremely slowly. Some species that live on rocks grow only one or two millimetres a year. That's why even geologists use them, to estimate how long a surface has been exposed, for example after a glacier has retreated. And I'd say to listeners: next time you see a yellow patch on an old wall, don't rush to clean it off. It may be older than you are."),
 ],
 "questions": [
  Q("Τι είναι, σύμφωνα με τη λειχηνολόγο, μια λειχήνα;", ["Ένα είδος βρύου", "Μια συνεργασία ανάμεσα σε έναν μύκητα και σε έναν οργανισμό που κάνει φωτοσύνθεση", "Ένα μικρό φυτό χωρίς φύλλα", "Ένα είδος μούχλας"], 1, "Είναι μια συνεργασία ανάμεσα σε έναν μύκητα και σε ένα φύκι ή ένα βακτήριο που κάνει φωτοσύνθεση"),
  Q("Γιατί οι λειχήνες είναι καλοί δείκτες της ποιότητας του αέρα;", ["Γιατί αλλάζουν χρώμα με τη θερμοκρασία", "Γιατί απορροφούν ουσίες απευθείας από τον αέρα και είναι ευαίσθητες στη ρύπανση", "Γιατί καθαρίζουν τον αέρα", "Γιατί ζουν μόνο στις πόλεις"], 1, "απορροφούν νερό και ουσίες απευθείας από την ατμόσφαιρα, και πολλά είδη είναι πολύ ευαίσθητα στη ρύπανση"),
  Q("Τι συνέβη στις λειχήνες των βιομηχανικών πόλεων της Αγγλίας;", ["Έγιναν πιο μεγάλες", "Σχεδόν εξαφανίστηκαν και επέστρεψαν όταν καθάρισε ο αέρας", "Άλλαξαν χρώμα", "Μεταφέρθηκαν στην εξοχή"], 1, "οι λειχήνες σχεδόν εξαφανίστηκαν από τα δέντρα. Όταν ο αέρας καθάρισε, άρχισαν σιγά σιγά να επιστρέφουν"),
  Q("Γιατί χρησιμοποιούν τις λειχήνες οι γεωλόγοι;", ["Για να βρουν νερό", "Γιατί μεγαλώνουν τόσο αργά που δείχνουν πόσο καιρό είναι εκτεθειμένη μια επιφάνεια", "Για να προβλέψουν σεισμούς", "Για να χρονολογήσουν αρχαία κτίρια"], 1, "για να υπολογίσουν πόσο καιρό έχει μείνει εκτεθειμένη μια επιφάνεια"),
 ],
 "gloss": {"λειχηνολόγος": "λειχηνολόγος — lichenologist", "λειχήνες": "λειχήνα — lichen", "κηλίδες": "κηλίδα — patch, spot", "κεραμίδια": "κεραμίδι — roof tile", "μύκητα": "μύκητας — fungus", "φύκι": "φύκι — alga, seaweed", "φωτοσύνθεση": "φωτοσύνθεση — photosynthesis", "δείκτες": "δείκτης — indicator", "ευαίσθητα": "ευαίσθητος — sensitive", "διοξείδιο του θείου": "διοξείδιο του θείου — sulphur dioxide", "εκτεθειμένη": "εκτεθειμένος — exposed", "υποχώρηση": "υποχώρηση — retreat", "παγετώνα": "παγετώνας — glacier"},
})

rnd = random.Random(239)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-239.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
