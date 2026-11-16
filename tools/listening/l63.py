# Source for library/listening/listening-63.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l63.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l63-ann-mouseio-glypta", "title": "Κλειστή η αίθουσα των γλυπτών", "title_en": "The sculpture gallery is closed", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα αρχαιολογικό μουσείο. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Ανακοίνωση", "f", "Αγαπητοί επισκέπτες, σας ενημερώνουμε ότι η αίθουσα των αρχαϊκών γλυπτών, στον πρώτο όροφο, θα παραμείνει κλειστή σήμερα, λόγω εργασιών συντήρησης. Τα γλυπτά θα είναι ξανά προσβάσιμα από αύριο το πρωί. Ζητούμε συγγνώμη για την ταλαιπωρία.", "Dear visitors, please note that the gallery of Archaic sculpture, on the first floor, will remain closed today for conservation work. The sculptures will be accessible again from tomorrow morning. We apologise for the inconvenience."),
  L("Ανακοίνωση", "f", "Οι επισκέπτες που έχουν εισιτήριο με ξενάγηση μπορούν, αν το επιθυμούν, να παρακολουθήσουν την ξενάγηση στη συλλογή των αγγείων, που ξεκινά στις έντεκα από την κεντρική είσοδο. Υπενθυμίζουμε ότι η φωτογράφηση επιτρέπεται, αλλά χωρίς φλας.", "Visitors with a guided-tour ticket may, if they wish, join the tour of the vase collection, which starts at eleven from the main entrance. We remind you that photography is allowed, but without flash."),
  L("Ανακοίνωση", "f", "Το πωλητήριο και το καφέ του μουσείου, στο ισόγειο, λειτουργούν κανονικά. Σας ευχόμαστε καλή περιήγηση.", "The museum shop and café, on the ground floor, are open as usual. Enjoy your visit."),
 ],
 "questions": [
  Q("Γιατί είναι κλειστή η αίθουσα των γλυπτών;", ["Λόγω απεργίας", "Λόγω εργασιών συντήρησης", "Γιατί μεταφέρονται τα γλυπτά σε άλλο μουσείο", "Λόγω βλάβης στο ρεύμα"], 1, "λόγω εργασιών συντήρησης"),
  Q("Τι μπορούν να κάνουν όσοι έχουν εισιτήριο με ξενάγηση;", ["Να πάρουν πίσω τα χρήματά τους", "Να έρθουν άλλη μέρα δωρεάν", "Να παρακολουθήσουν την ξενάγηση στη συλλογή των αγγείων", "Να μπουν στην αίθουσα με συνοδεία φύλακα"], 2, "να παρακολουθήσουν την ξενάγηση στη συλλογή των αγγείων"),
  Q("Τι ισχύει για τη φωτογράφηση;", ["Απαγορεύεται παντού", "Επιτρέπεται, αλλά χωρίς φλας", "Επιτρέπεται μόνο στο ισόγειο", "Χρειάζεται ειδικό εισιτήριο"], 1, "η φωτογράφηση επιτρέπεται, αλλά χωρίς φλας"),
 ],
 "gloss": {"αρχαϊκών": "αρχαϊκός — Archaic (c. 700–480 BC)", "γλυπτών": "γλυπτό — sculpture", "συντήρησης": "συντήρηση — conservation", "προσβάσιμα": "προσβάσιμος — accessible", "ταλαιπωρία": "ταλαιπωρία — inconvenience", "ξενάγηση": "ξενάγηση — guided tour", "αγγείων": "αγγείο — vase", "φλας": "φλας — flash", "πωλητήριο": "πωλητήριο — museum shop"},
})

ITEMS.append({
 "id": "l63-vm-ogkodi", "title": "Παραλαβή ογκωδών αντικειμένων", "title_en": "Collection of bulky items", "type": "voicemail", "level": "B2",
 "context_el": "Ζητήσατε από τον δήμο να παραλάβει ένα παλιό έπιπλο. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, κυρία Ξενάκη, σας καλώ από την υπηρεσία καθαριότητας του δήμου, σχετικά με το αίτημά σας για την παραλαβή ενός καναπέ και ενός παλιού στρώματος. Το συνεργείο μας θα περάσει από τη διεύθυνσή σας την Τετάρτη το πρωί, μεταξύ επτά και δέκα.", "Good morning, Mrs Xenaki, I'm calling from the municipal sanitation department about your request for the collection of a sofa and an old mattress. Our crew will come by your address on Wednesday morning, between seven and ten."),
  L("Υπάλληλος", "m", "Παρακαλούμε να αφήσετε τα αντικείμενα στο πεζοδρόμιο το βράδυ της Τρίτης, μετά τις εννιά, και όχι νωρίτερα, ώστε να μην εμποδίζουν τους πεζούς. Να ξέρετε επίσης ότι δεν παραλαμβάνουμε οικοδομικά υλικά ούτε ηλεκτρικές συσκευές· για αυτές υπάρχει ξεχωριστό πρόγραμμα ανακύκλωσης.", "Please leave the items on the pavement on Tuesday evening, after nine, and not earlier, so that they don't obstruct pedestrians. Please also note that we do not collect building materials or electrical appliances; there is a separate recycling programme for those."),
  L("Υπάλληλος", "m", "Η υπηρεσία είναι δωρεάν. Για οποιαδήποτε αλλαγή, καλέστε μας στο ένα-εννιά-πέντε. Ευχαριστώ.", "The service is free. For any change, call us on one-nine-five. Thank you."),
 ],
 "questions": [
  Q("Πότε θα περάσει το συνεργείο;", ["Την Τρίτη το βράδυ", "Την Τετάρτη το πρωί, μεταξύ επτά και δέκα", "Την Πέμπτη το μεσημέρι", "Την Τετάρτη το απόγευμα"], 1, "την Τετάρτη το πρωί, μεταξύ επτά και δέκα"),
  Q("Γιατί δεν πρέπει να αφήσει νωρίτερα τα αντικείμενα στο πεζοδρόμιο;", ["Γιατί θα τα πάρει κάποιος άλλος", "Για να μην εμποδίζουν τους πεζούς", "Γιατί υπάρχει πρόστιμο", "Γιατί μπορεί να βρέξει"], 1, "ώστε να μην εμποδίζουν τους πεζούς"),
  Q("Τι δεν παραλαμβάνει η υπηρεσία;", ["Έπιπλα", "Στρώματα", "Οικοδομικά υλικά και ηλεκτρικές συσκευές", "Χαλιά"], 2, "δεν παραλαμβάνουμε οικοδομικά υλικά ούτε ηλεκτρικές συσκευές"),
 ],
 "gloss": {"υπηρεσία καθαριότητας": "υπηρεσία καθαριότητας — sanitation department", "παραλαβή": "παραλαβή — collection, pickup", "στρώματος": "στρώμα — mattress", "συνεργείο": "συνεργείο — (work) crew", "πεζοδρόμιο": "πεζοδρόμιο — pavement", "εμποδίζουν": "εμποδίζω — to obstruct", "πεζούς": "πεζός — pedestrian", "οικοδομικά υλικά": "οικοδομικά υλικά — building materials"},
})

ITEMS.append({
 "id": "l63-dia-trypani", "title": "Ένα δανεικό τρυπάνι", "title_en": "A borrowed drill", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο ανάμεσα σε δύο γείτονες στη σκάλα της πολυκατοικίας.",
 "script": [
  L("Θοδωρής", "m", "Καλησπέρα, κυρία Ελένη. Συγγνώμη για την ενόχληση. Μήπως έχετε ένα τρυπάνι να μου δανείσετε; Θέλω να κρεμάσω ένα ράφι στην κουζίνα, και το δικό μου χάλασε.", "Good evening, Mrs Eleni. Sorry to bother you. Do you happen to have a drill you could lend me? I want to hang a shelf in the kitchen, and mine is broken."),
  L("Ελένη", "f", "Βεβαίως, του άντρα μου είναι, αλλά δεν το χρησιμοποιεί σχεδόν ποτέ. Μόνο προσέξτε: ο τοίχος της κουζίνας σας είναι από μπετόν, θα χρειαστείτε το ειδικό τρυπάνι, όχι το απλό. Είναι μέσα στην μπλε θήκη.", "Of course, it's my husband's, but he hardly ever uses it. Just be careful: your kitchen wall is concrete, so you'll need the special bit, not the ordinary one. It's in the blue case."),
  L("Θοδωρής", "m", "Ευχαριστώ πολύ. Θα σας το φέρω πίσω αύριο το πρωί. Και μην ανησυχείτε για τον θόρυβο· θα τελειώσω πριν από τις εννιά.", "Thank you very much. I'll bring it back tomorrow morning. And don't worry about the noise; I'll finish before nine."),
  L("Ελένη", "f", "Μην βιάζεστε. Αλλά σας παρακαλώ, όχι μετά τις τρεις το μεσημέρι αύριο, γιατί ο κύριος του τρίτου έχει μωρό και κοιμάται. Α, και αν θέλετε βοήθεια, ο γιος μου είναι ηλεκτρολόγος· να προσέχετε μην τρυπήσετε κανένα καλώδιο.", "No rush. But please, not after three tomorrow afternoon, because the man on the third floor has a baby who naps then. Oh, and if you want help, my son is an electrician; be careful not to drill into a cable."),
 ],
 "questions": [
  Q("Γιατί θέλει ο Θοδωρής το τρυπάνι;", ["Για να φτιάξει την πόρτα", "Για να κρεμάσει ένα ράφι στην κουζίνα", "Για να βάλει κουρτίνες", "Για να κρεμάσει έναν πίνακα"], 1, "Θέλω να κρεμάσω ένα ράφι στην κουζίνα"),
  Q("Τι συμβουλεύει η κυρία Ελένη για τον τοίχο;", ["Να μην τον τρυπήσει καθόλου", "Να χρησιμοποιήσει το ειδικό τρυπάνι, γιατί είναι από μπετόν", "Να ζητήσει άδεια από τον διαχειριστή", "Να χρησιμοποιήσει κόλλα αντί για βίδες"], 1, "ο τοίχος της κουζίνας σας είναι από μπετόν, θα χρειαστείτε το ειδικό τρυπάνι"),
  Q("Γιατί δεν πρέπει να κάνει θόρυβο μετά τις τρεις αύριο;", ["Γιατί η κυρία Ελένη ξεκουράζεται", "Γιατί το μωρό του γείτονα του τρίτου κοιμάται", "Γιατί το απαγορεύει ο κανονισμός", "Γιατί θα έρθει ο ηλεκτρολόγος"], 1, "ο κύριος του τρίτου έχει μωρό και κοιμάται"),
 ],
 "gloss": {"τρυπάνι": "τρυπάνι — drill; also drill bit", "δανείσετε": "δανείζω — to lend", "ράφι": "ράφι — shelf", "μπετόν": "μπετόν — concrete", "θήκη": "θήκη — case", "ηλεκτρολόγος": "ηλεκτρολόγος — electrician", "τρυπήσετε": "τρυπώ — to drill, pierce", "καλώδιο": "καλώδιο — cable"},
})

ITEMS.append({
 "id": "l63-dia-leschi-anagnosis", "title": "Η λέσχη ανάγνωσης", "title_en": "The book club", "type": "dialogue", "level": "B2",
 "context_el": "Δύο μέλη μιας λέσχης ανάγνωσης συζητούν ποιο βιβλίο θα προτείνουν για τον επόμενο μήνα.",
 "script": [
  L("Ναταλία", "f", "Τον επόμενο μήνα είναι η σειρά μας να προτείνουμε βιβλίο. Εγώ σκεφτόμουν «Το Νησί» της Βικτόρια Χίσλοπ. Το έχουν διαβάσει πολλοί, αλλά θα είχε ενδιαφέρον να το συζητήσουμε.", "Next month it's our turn to suggest a book. I was thinking of 'The Island' by Victoria Hislop. Lots of people have read it, but it would be interesting to discuss."),
  L("Παύλος", "m", "Ακριβώς γι’ αυτό δεν μου αρέσει η ιδέα· οι μισοί το έχουν ήδη διαβάσει. Προτιμώ κάτι ελληνικό που δεν το ξέρουν. Τι λες για «Τα ψάθινα καπέλα» της Μαργαρίτας Λυμπεράκη; Είναι σύντομο και πολύ ατμοσφαιρικό.", "That's exactly why I don't like the idea; half of them have already read it. I'd prefer something Greek they don't know. What about 'The Straw Hats' by Margarita Lymberaki? It's short and very atmospheric."),
  L("Ναταλία", "f", "Καλή ιδέα. Και είναι εύκολο να βρεθεί στις βιβλιοθήκες. Να το προτείνουμε, τότε, και στη συνάντηση να φέρουμε φωτογραφίες από την Κηφισιά της εποχής, όπου διαδραματίζεται η ιστορία.", "Good idea. And it's easy to find in libraries. Let's suggest it, then, and bring photos of Kifisia from that era, where the story takes place, to the meeting."),
  L("Παύλος", "m", "Τέλεια. Και να ρωτήσουμε αν μπορούμε να κάνουμε τη συνάντηση στο καφέ της πλατείας, γιατί στο σπίτι της Δέσποινας δεν χωράμε πια.", "Perfect. And let's ask if we can hold the meeting at the café on the square, because we no longer fit in Despina's house."),
 ],
 "questions": [
  Q("Γιατί δεν του αρέσει του Παύλου η πρόταση της Ναταλίας;", ["Γιατί το βιβλίο είναι πολύ μεγάλο", "Γιατί πολλά μέλη το έχουν ήδη διαβάσει", "Γιατί δεν του αρέσει η συγγραφέας", "Γιατί δεν είναι μεταφρασμένο"], 1, "οι μισοί το έχουν ήδη διαβάσει"),
  Q("Τι θα φέρουν στη συνάντηση;", ["Γλυκά", "Φωτογραφίες από την Κηφισιά της εποχής", "Ένα δεύτερο βιβλίο", "Ψάθινα καπέλα"], 1, "να φέρουμε φωτογραφίες από την Κηφισιά της εποχής"),
  Q("Γιατί θέλουν να αλλάξουν τόπο συνάντησης;", ["Γιατί το καφέ είναι πιο φθηνό", "Γιατί δεν χωρούν πια στο σπίτι της Δέσποινας", "Γιατί η Δέσποινα μετακομίζει", "Γιατί το καφέ έχει βιβλιοθήκη"], 1, "στο σπίτι της Δέσποινας δεν χωράμε πια"),
 ],
 "gloss": {"λέσχης ανάγνωσης": "λέσχη ανάγνωσης — book club", "σειρά": "σειρά — turn", "ψάθινα": "ψάθινος — straw (adj.)", "ατμοσφαιρικό": "ατμοσφαιρικός — atmospheric", "διαδραματίζεται": "διαδραματίζομαι — to take place (of a story)", "χωράμε": "χωρώ — to fit"},
})

ITEMS.append({
 "id": "l63-int-architektonas-topiou", "title": "Η αρχιτέκτονας τοπίου", "title_en": "The landscape architect", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για την πόλη, μια δημοσιογράφος μιλά με μια αρχιτέκτονα τοπίου.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί δεν ξέρουν τι κάνει ένας αρχιτέκτονας τοπίου. Θα μας το εξηγήσετε;", "Many people don't know what a landscape architect does. Would you explain it to us?"),
  L("Αρχιτέκτονας", "f", "Σχεδιάζουμε τους ανοιχτούς χώρους: πάρκα, πλατείες, αυλές σχολείων, ακόμη και ταράτσες. Δεν φυτεύουμε απλώς δέντρα· σκεφτόμαστε πώς θα κινούνται οι άνθρωποι, πού θα κάθονται, πού θα υπάρχει σκιά το καλοκαίρι και ήλιος τον χειμώνα.", "We design open spaces: parks, squares, schoolyards, even roof terraces. We don't just plant trees; we think about how people will move, where they will sit, where there will be shade in summer and sun in winter."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το μεγαλύτερο λάθος που βλέπετε στις ελληνικές πλατείες;", "What is the biggest mistake you see in Greek squares?"),
  L("Αρχιτέκτονας", "f", "Το πολύ μάρμαρο και το λίγο χώμα. Οι πλακοστρωμένες πλατείες καίνε το καλοκαίρι και, όταν βρέχει, το νερό δεν απορροφάται. Εμείς προτιμάμε ντόπια φυτά, που αντέχουν την ξηρασία και χρειάζονται λίγο πότισμα, όπως η λεβάντα, το δεντρολίβανο και η κουμαριά. Και ζητάμε πάντα τη γνώμη των κατοίκων, πριν ξεκινήσουμε.", "Too much marble and too little soil. Paved squares burn in summer and, when it rains, the water isn't absorbed. We prefer native plants, which withstand drought and need little watering, like lavender, rosemary and the strawberry tree. And we always ask residents for their opinion before we start."),
 ],
 "questions": [
  Q("Τι σχεδιάζει ένας αρχιτέκτονας τοπίου;", ["Μόνο ιδιωτικούς κήπους", "Ανοιχτούς χώρους, όπως πάρκα, πλατείες και αυλές", "Εσωτερικούς χώρους σπιτιών", "Δρόμους και γέφυρες"], 1, "Σχεδιάζουμε τους ανοιχτούς χώρους"),
  Q("Ποιο λάθος βλέπει στις ελληνικές πλατείες;", ["Τα πολλά δέντρα", "Το πολύ μάρμαρο και το λίγο χώμα", "Τα λίγα παγκάκια", "Τον κακό φωτισμό"], 1, "Το πολύ μάρμαρο και το λίγο χώμα"),
  Q("Γιατί προτιμά ντόπια φυτά;", ["Γιατί είναι φθηνότερα", "Γιατί αντέχουν την ξηρασία και χρειάζονται λίγο πότισμα", "Γιατί μεγαλώνουν γρήγορα", "Γιατί έχουν ωραίο άρωμα"], 1, "αντέχουν την ξηρασία και χρειάζονται λίγο πότισμα"),
 ],
 "gloss": {"αρχιτέκτονας τοπίου": "αρχιτέκτονας τοπίου — landscape architect", "ανοιχτούς χώρους": "ανοιχτός χώρος — open space", "ταράτσες": "ταράτσα — roof terrace", "πλακοστρωμένες": "πλακόστρωτος — paved", "απορροφάται": "απορροφώμαι — to be absorbed", "ντόπια": "ντόπιος — native, local", "ξηρασία": "ξηρασία — drought", "πότισμα": "πότισμα — watering", "κουμαριά": "κουμαριά — strawberry tree"},
})

ITEMS.append({
 "id": "l63-rep-kitro-naxou", "title": "Το κίτρο της Νάξου", "title_en": "The citron of Naxos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από μια ραδιοφωνική εκπομπή για τα τοπικά προϊόντα.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρισκόμαστε στη Χαλκί, ένα όμορφο χωριό στο κέντρο της Νάξου, με νεοκλασικά σπίτια και πύργους. Εδώ λειτουργεί από τα τέλη του δέκατου ένατου αιώνα ένα από τα πιο γνωστά αποστακτήρια του νησιού, όπου παράγεται το περίφημο λικέρ κίτρο.", "We are in Chalki, a beautiful village in the centre of Naxos, with neoclassical houses and towers. Here, since the late nineteenth century, one of the island's best-known distilleries has been operating, where the famous citron liqueur is produced."),
  L("Ρεπόρτερ", "f", "Το κίτρο είναι ένα εσπεριδοειδές που μοιάζει με μεγάλο, ανώμαλο λεμόνι. Η ιδιαιτερότητα του ναξιώτικου λικέρ είναι ότι δεν φτιάχνεται κυρίως από τον καρπό, αλλά από τα αρωματικά φύλλα του δέντρου, που αποστάζονται. Από τον καρπό οι νοικοκυρές φτιάχνουν γλυκό του κουταλιού.", "The citron is a citrus fruit that looks like a large, lumpy lemon. What is special about the Naxian liqueur is that it is not made mainly from the fruit, but from the fragrant leaves of the tree, which are distilled. Housewives make spoon sweets from the fruit."),
  L("Ρεπόρτερ", "f", "Το λικέρ κυκλοφορεί σε τρεις εκδοχές, με διαφορετικό χρώμα και διαφορετική γλυκύτητα. Στο παλιό αποστακτήριο, ο επισκέπτης μπορεί να δει τους χάλκινους άμβυκες και, φυσικά, να δοκιμάσει.", "The liqueur comes in three versions, with different colours and different levels of sweetness. At the old distillery, visitors can see the copper stills and, of course, have a taste."),
 ],
 "questions": [
  Q("Πού βρίσκεται η Χαλκί;", ["Στο λιμάνι της Νάξου", "Στο κέντρο της Νάξου", "Σε ένα γειτονικό νησί", "Στη νότια ακτή"], 1, "ένα όμορφο χωριό στο κέντρο της Νάξου"),
  Q("Από τι φτιάχνεται κυρίως το λικέρ κίτρο;", ["Από τον χυμό του καρπού", "Από τα αρωματικά φύλλα του δέντρου", "Από τη φλούδα του καρπού", "Από μέλι και λεμόνι"], 1, "από τα αρωματικά φύλλα του δέντρου, που αποστάζονται"),
  Q("Σε πόσες εκδοχές κυκλοφορεί το λικέρ;", ["Σε μία", "Σε δύο", "Σε τρεις", "Σε πέντε"], 2, "κυκλοφορεί σε τρεις εκδοχές"),
 ],
 "gloss": {"νεοκλασικά": "νεοκλασικός — neoclassical", "αποστακτήρια": "αποστακτήριο — distillery", "λικέρ": "λικέρ — liqueur", "εσπεριδοειδές": "εσπεριδοειδές — citrus fruit", "ανώμαλο": "ανώμαλος — uneven, lumpy", "αποστάζονται": "αποστάζομαι — to be distilled", "γλυκό του κουταλιού": "γλυκό του κουταλιού — spoon sweet (fruit preserve)", "εκδοχές": "εκδοχή — version", "άμβυκες": "άμβυκας — still (for distilling)"},
})

ITEMS.append({
 "id": "l63-dia-forologiki", "title": "Η φορολογική δήλωση", "title_en": "The tax return", "type": "dialogue", "level": "B2",
 "context_el": "Μια νεαρή εργαζόμενη πηγαίνει σε έναν λογιστή για να κάνει την πρώτη της φορολογική δήλωση.",
 "script": [
  L("Λογιστής", "m", "Καθίστε, παρακαλώ. Είναι η πρώτη σας δήλωση, σωστά; Φέρατε τους κωδικούς σας για την ηλεκτρονική πλατφόρμα;", "Have a seat, please. It's your first return, right? Did you bring your passwords for the online platform?"),
  L("Φαίη", "f", "Ναι, τους έχω εδώ. Δούλευα έξι μήνες με σύμβαση σε μια εταιρεία και μετά ξεκίνησα ως ελεύθερη επαγγελματίας. Δεν ξέρω αν αυτό κάνει τα πράγματα πιο περίπλοκα.", "Yes, I have them here. I worked for six months on a contract at a company and then started as a freelancer. I don't know if that makes things more complicated."),
  L("Λογιστής", "m", "Λίγο, αλλά δεν είναι κάτι ασυνήθιστο. Το σημαντικό είναι να έχετε πληρώσει με κάρτα ένα μέρος των εξόδων σας. Αν δεν φτάσετε το απαιτούμενο ποσό ηλεκτρονικών πληρωμών, υπάρχει επιπλέον φόρος.", "A bit, but it's nothing unusual. The important thing is to have paid part of your expenses by card. If you don't reach the required amount of electronic payments, there's an extra tax."),
  L("Φαίη", "f", "Ευτυχώς πληρώνω σχεδόν τα πάντα με κάρτα. Και το ενοίκιο; Μπορώ να το δηλώσω;", "Luckily, I pay for almost everything by card. And the rent? Can I declare it?"),
  L("Λογιστής", "m", "Βεβαίως, και καλά κάνετε, γιατί μπορεί να πάρετε πίσω ένα μέρος του. Η προθεσμία λήγει τον Ιούλιο, αλλά αν την υποβάλουμε νωρίς, θα έχετε έκπτωση στον φόρο.", "Of course, and you'd be right to, because you may get part of it back. The deadline is in July, but if we submit it early, you'll get a discount on the tax."),
 ],
 "questions": [
  Q("Τι δουλειά κάνει η Φαίη σήμερα;", ["Δουλεύει σε εταιρεία με σύμβαση", "Είναι ελεύθερη επαγγελματίας", "Είναι φοιτήτρια", "Είναι άνεργη"], 1, "μετά ξεκίνησα ως ελεύθερη επαγγελματίας"),
  Q("Τι γίνεται αν δεν φτάσει το απαιτούμενο ποσό ηλεκτρονικών πληρωμών;", ["Δεν μπορεί να κάνει δήλωση", "Υπάρχει επιπλέον φόρος", "Χάνει την έκπτωση στο ενοίκιο", "Πληρώνει πρόστιμο στην τράπεζα"], 1, "Αν δεν φτάσετε το απαιτούμενο ποσό ηλεκτρονικών πληρωμών, υπάρχει επιπλέον φόρος"),
  Q("Τι πλεονέκτημα έχει η έγκαιρη υποβολή της δήλωσης;", ["Γρηγορότερη επιστροφή του ενοικίου", "Έκπτωση στον φόρο", "Δωρεάν λογιστής", "Καμία πληρωμή φέτος"], 1, "αν την υποβάλουμε νωρίς, θα έχετε έκπτωση στον φόρο"),
 ],
 "gloss": {"φορολογική δήλωση": "φορολογική δήλωση — tax return", "λογιστή": "λογιστής — accountant", "κωδικούς": "κωδικός — password, code", "σύμβαση": "σύμβαση — contract", "ελεύθερη επαγγελματίας": "ελεύθερος επαγγελματίας — freelancer, self-employed", "εξόδων": "έξοδα — expenses", "απαιτούμενο": "απαιτούμενος — required", "υποβάλουμε": "υποβάλλω — to submit", "έκπτωση": "έκπτωση — discount"},
})

ITEMS.append({
 "id": "l63-mono-koinonika-diktya", "title": "Έκλεισα τους λογαριασμούς μου", "title_en": "I closed my accounts", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν νέο άντρα να μιλά σε ένα podcast για την απόφασή του να φύγει από τα κοινωνικά δίκτυα.",
 "script": [
  L("Ορέστης", "m", "Πριν από έναν χρόνο, ένα βράδυ, κοίταξα στο κινητό πόσο χρόνο περνούσα στα κοινωνικά δίκτυα: τέσσερις ώρες τη μέρα. Τέσσερις ώρες! Την επόμενη μέρα έκλεισα όλους τους λογαριασμούς μου, εκτός από την εφαρμογή μηνυμάτων, που τη χρειάζομαι για τη δουλειά.", "A year ago, one evening, I checked on my phone how much time I was spending on social networks: four hours a day. Four hours! The next day I closed all my accounts, except for the messaging app, which I need for work."),
  L("Ορέστης", "m", "Οι πρώτες δύο εβδομάδες ήταν δύσκολες. Έπιανα το κινητό χωρίς λόγο, από συνήθεια. Ένιωθα ότι χάνω νέα, πάρτι, αστεία. Μετά, όμως, κάτι άλλαξε. Άρχισα να διαβάζω πάλι βιβλία, κοιμόμουν καλύτερα και, το πιο περίεργο, τηλεφωνούσα στους φίλους μου αντί να βλέπω απλώς τις φωτογραφίες τους.", "The first two weeks were hard. I'd pick up my phone for no reason, out of habit. I felt I was missing news, parties, jokes. But then something changed. I started reading books again, I slept better and, strangest of all, I phoned my friends instead of just looking at their photos."),
  L("Ορέστης", "m", "Δεν λέω ότι όλοι πρέπει να κάνουν το ίδιο. Για κάποιους τα δίκτυα είναι εργαλείο. Για μένα, όμως, ήταν μια συνήθεια που μου έτρωγε τη ζωή χωρίς να το καταλαβαίνω.", "I'm not saying everyone should do the same. For some people the networks are a tool. For me, though, they were a habit that was eating up my life without my realising it."),
 ],
 "questions": [
  Q("Τι τον έκανε να πάρει την απόφαση;", ["Ένα άρθρο που διάβασε", "Ότι είδε πως περνούσε τέσσερις ώρες τη μέρα στα δίκτυα", "Μια συμβουλή του γιατρού του", "Ένας καβγάς στο διαδίκτυο"], 1, "πόσο χρόνο περνούσα στα κοινωνικά δίκτυα: τέσσερις ώρες τη μέρα"),
  Q("Τι κράτησε;", ["Τον λογαριασμό με τις φωτογραφίες", "Την εφαρμογή μηνυμάτων για τη δουλειά", "Ένα επαγγελματικό δίκτυο", "Τίποτα"], 1, "εκτός από την εφαρμογή μηνυμάτων, που τη χρειάζομαι για τη δουλειά"),
  Q("Ποια αλλαγή χαρακτηρίζει «το πιο περίεργο»;", ["Ότι διάβαζε περισσότερα βιβλία", "Ότι κοιμόταν καλύτερα", "Ότι τηλεφωνούσε στους φίλους του αντί να βλέπει τις φωτογραφίες τους", "Ότι έχασε βάρος"], 2, "τηλεφωνούσα στους φίλους μου αντί να βλέπω απλώς τις φωτογραφίες τους"),
 ],
 "gloss": {"κοινωνικά δίκτυα": "κοινωνικά δίκτυα — social networks", "λογαριασμούς": "λογαριασμός — account", "εφαρμογή μηνυμάτων": "εφαρμογή μηνυμάτων — messaging app", "από συνήθεια": "από συνήθεια — out of habit", "εργαλείο": "εργαλείο — tool", "έτρωγε": "τρώω — to eat up, consume"},
})

ITEMS.append({
 "id": "l63-c1-energeiaki-ftocheia", "title": "Η ενεργειακή φτώχεια", "title_en": "Energy poverty", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την κοινωνία, μια δημοσιογράφος συζητά με έναν ερευνητή για την ενεργειακή φτώχεια.",
 "script": [
  L("Δημοσιογράφος", "f", "Ακούμε όλο και συχνότερα τον όρο «ενεργειακή φτώχεια». Τι ακριβώς σημαίνει;", "We hear the term 'energy poverty' more and more often. What exactly does it mean?"),
  L("Ερευνητής", "m", "Είναι η αδυναμία ενός νοικοκυριού να εξασφαλίσει βασικές ενεργειακές υπηρεσίες, όπως επαρκή θέρμανση τον χειμώνα ή δροσιά το καλοκαίρι, σε τιμή που μπορεί να αντέξει. Δεν αφορά μόνο το εισόδημα. Ένα νοικοκυριό με μέτριο εισόδημα μπορεί να βρεθεί σε αυτή τη θέση, αν ζει σε ένα παλιό, κακώς μονωμένο κτίριο, όπου η ενέργεια κυριολεκτικά διαφεύγει από τα παράθυρα.", "It is a household's inability to secure basic energy services, such as adequate heating in winter or cooling in summer, at a price it can afford. It isn't only about income. A household with a modest income can find itself in this position if it lives in an old, poorly insulated building, where energy literally escapes through the windows."),
  L("Δημοσιογράφος", "f", "Και ποιες είναι οι συνέπειες;", "And what are the consequences?"),
  L("Ερευνητής", "m", "Είναι πολύ πιο σοβαρές από όσο νομίζουμε. Οι κρύες και υγρές κατοικίες συνδέονται με αναπνευστικά προβλήματα, ιδίως στα παιδιά και στους ηλικιωμένους. Υπάρχει και μια αθέατη πλευρά: πολλές οικογένειες περιορίζουν άλλες βασικές δαπάνες, ακόμη και τη διατροφή, για να πληρώσουν τον λογαριασμό του ρεύματος. Τα επιδόματα θέρμανσης ανακουφίζουν προσωρινά, αλλά η μόνιμη λύση είναι η ενεργειακή αναβάθμιση των κτιρίων: μόνωση, καινούργια κουφώματα, αποδοτικά συστήματα θέρμανσης. Το πρόβλημα είναι ότι τα προγράμματα επιδότησης απαιτούν συνήθως μια αρχική συμμετοχή, που οι πιο ευάλωτοι δεν μπορούν να καλύψουν· έτσι, συχνά ωφελούνται εκείνοι που τα χρειάζονται λιγότερο.", "They are much more serious than we think. Cold, damp homes are linked to respiratory problems, especially in children and the elderly. There's also a hidden side: many families cut back on other basic expenses, even food, in order to pay the electricity bill. Heating allowances provide temporary relief, but the permanent solution is the energy upgrade of buildings: insulation, new window frames, efficient heating systems. The problem is that subsidy programmes usually require an initial contribution that the most vulnerable cannot cover; so those who need them least often benefit."),
 ],
 "questions": [
  Q("Πώς ορίζει ο ερευνητής την ενεργειακή φτώχεια;", ["Ως την έλλειψη ρεύματος σε απομακρυσμένες περιοχές", "Ως την αδυναμία ενός νοικοκυριού να εξασφαλίσει βασικές ενεργειακές υπηρεσίες σε προσιτή τιμή", "Ως την υπερβολική κατανάλωση ενέργειας", "Ως την ανεργία στον τομέα της ενέργειας"], 1, "Είναι η αδυναμία ενός νοικοκυριού να εξασφαλίσει βασικές ενεργειακές υπηρεσίες"),
  Q("Γιατί μπορεί να επηρεαστεί και ένα νοικοκυριό με μέτριο εισόδημα;", ["Γιατί πληρώνει υψηλούς φόρους", "Γιατί ζει σε παλιό, κακώς μονωμένο κτίριο", "Γιατί έχει πολλά παιδιά", "Γιατί χρησιμοποιεί πολλές συσκευές"], 1, "αν ζει σε ένα παλιό, κακώς μονωμένο κτίριο"),
  Q("Ποια είναι η «αθέατη πλευρά» του προβλήματος;", ["Ότι οι οικογένειες περιορίζουν άλλες βασικές δαπάνες, ακόμη και τη διατροφή", "Ότι τα κτίρια χάνουν την αξία τους", "Ότι αυξάνεται η ρύπανση", "Ότι οι λογαριασμοί δεν είναι κατανοητοί"], 0, "πολλές οικογένειες περιορίζουν άλλες βασικές δαπάνες, ακόμη και τη διατροφή"),
  Q("Ποιο πρόβλημα βλέπει στα προγράμματα επιδότησης;", ["Ότι χρηματοδοτούν μόνο καινούργια κτίρια", "Ότι απαιτούν αρχική συμμετοχή που οι πιο ευάλωτοι δεν μπορούν να καλύψουν", "Ότι καθυστερούν πολλά χρόνια", "Ότι αφορούν μόνο τα νησιά"], 1, "απαιτούν συνήθως μια αρχική συμμετοχή, που οι πιο ευάλωτοι δεν μπορούν να καλύψουν"),
 ],
 "gloss": {"ενεργειακή φτώχεια": "ενεργειακή φτώχεια — energy poverty", "νοικοκυριού": "νοικοκυριό — household", "επαρκή": "επαρκής — adequate", "μονωμένο": "μονωμένος — insulated", "διαφεύγει": "διαφεύγω — to escape", "αναπνευστικά": "αναπνευστικός — respiratory", "αθέατη": "αθέατος — hidden, unseen", "δαπάνες": "δαπάνη — expense", "επιδόματα θέρμανσης": "επίδομα θέρμανσης — heating allowance", "κουφώματα": "κούφωμα — window/door frame", "επιδότησης": "επιδότηση — subsidy", "ευάλωτοι": "ευάλωτος — vulnerable"},
})

ITEMS.append({
 "id": "l63-c1-megali-idea", "title": "Η Μεγάλη Ιδέα", "title_en": "The Great Idea", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για την ιδεολογία που καθόρισε την ελληνική εξωτερική πολιτική για σχεδόν έναν αιώνα.",
 "script": [
  L("Ιστορικός", "f", "Ο όρος «Μεγάλη Ιδέα» συνδέεται με έναν λόγο του Ιωάννη Κωλέττη στην Εθνοσυνέλευση του 1844. Το μικρό ελληνικό κράτος της εποχής περιλάμβανε μόνο ένα μέρος των Ελλήνων· οι περισσότεροι ζούσαν ακόμη στην Οθωμανική Αυτοκρατορία, στη Μακεδονία, στην Ήπειρο, στην Κρήτη, στη Μικρά Ασία και στην Κωνσταντινούπολη.", "The term 'Great Idea' is associated with a speech by Ioannis Kolettis at the National Assembly of 1844. The small Greek state of the time included only part of the Greeks; most still lived in the Ottoman Empire, in Macedonia, Epirus, Crete, Asia Minor and Constantinople."),
  L("Ιστορικός", "f", "Η Μεγάλη Ιδέα ήταν το όραμα της ένωσης όλων αυτών των περιοχών σε ένα κράτος, με πρωτεύουσα, για πολλούς, την Κωνσταντινούπολη. Λειτούργησε ως συνεκτικός ιστός της εθνικής ταυτότητας, αλλά είχε και κόστος: απορρόφησε πόρους που θα μπορούσαν να διατεθούν στην εσωτερική ανάπτυξη και οδήγησε σε περιπέτειες, όπως ο ατυχής πόλεμος του 1897.", "The Great Idea was the vision of uniting all these regions in a single state, with Constantinople, for many, as its capital. It served as the connective tissue of national identity, but it also had a cost: it absorbed resources that could have gone to internal development and led to misadventures, such as the ill-fated war of 1897."),
  L("Ιστορικός", "f", "Η Ιδέα φάνηκε να πλησιάζει την πραγματοποίησή της με τη Συνθήκη των Σεβρών το 1920, που μιλούσε για την «Ελλάδα των δύο ηπείρων και των πέντε θαλασσών». Δύο χρόνια αργότερα, όμως, η Μικρασιατική Καταστροφή έβαλε οριστικό τέλος στο όραμα. Η ανταλλαγή πληθυσμών που ακολούθησε άλλαξε για πάντα τον χάρτη και την κοινωνία της χώρας.", "The Idea seemed close to fulfilment with the Treaty of Sèvres in 1920, which spoke of the 'Greece of two continents and five seas'. Two years later, however, the Asia Minor Catastrophe put a definitive end to the vision. The population exchange that followed changed the country's map and society forever."),
 ],
 "questions": [
  Q("Με ποιο γεγονός συνδέεται ο όρος «Μεγάλη Ιδέα»;", ["Με την Επανάσταση του 1821", "Με έναν λόγο του Κωλέττη στην Εθνοσυνέλευση του 1844", "Με τη Συνθήκη των Σεβρών", "Με τους Βαλκανικούς Πολέμους"], 1, "συνδέεται με έναν λόγο του Ιωάννη Κωλέττη στην Εθνοσυνέλευση του 1844"),
  Q("Τι ήταν η Μεγάλη Ιδέα;", ["Ένα σχέδιο οικονομικής ανάπτυξης", "Το όραμα της ένωσης όλων των περιοχών με ελληνικούς πληθυσμούς σε ένα κράτος", "Μια συμμαχία με τις Μεγάλες Δυνάμεις", "Ένα εκπαιδευτικό πρόγραμμα"], 1, "το όραμα της ένωσης όλων αυτών των περιοχών σε ένα κράτος"),
  Q("Ποιο κόστος της Μεγάλης Ιδέας αναφέρει η ομιλήτρια;", ["Την απώλεια της Κρήτης", "Την απορρόφηση πόρων από την εσωτερική ανάπτυξη και πολέμους όπως του 1897", "Τη διάλυση της Εθνοσυνέλευσης", "Τη μετανάστευση στην Αμερική"], 1, "απορρόφησε πόρους που θα μπορούσαν να διατεθούν στην εσωτερική ανάπτυξη"),
  Q("Τι έβαλε οριστικό τέλος στο όραμα;", ["Η Συνθήκη των Σεβρών", "Ο πόλεμος του 1897", "Η Μικρασιατική Καταστροφή", "Η ανταλλαγή πληθυσμών του 1844"], 2, "η Μικρασιατική Καταστροφή έβαλε οριστικό τέλος στο όραμα"),
 ],
 "gloss": {"Εθνοσυνέλευση": "Εθνοσυνέλευση — National Assembly", "όραμα": "όραμα — vision", "συνεκτικός ιστός": "συνεκτικός ιστός — connective tissue", "πόρους": "πόρος — resource", "διατεθούν": "διατίθεμαι — to be allocated", "ατυχής": "ατυχής — ill-fated", "πραγματοποίησή": "πραγματοποίηση — fulfilment", "Σεβρών": "Σέβρες — Sèvres", "ηπείρων": "ήπειρος — continent", "ανταλλαγή πληθυσμών": "ανταλλαγή πληθυσμών — population exchange"},
})

rnd = random.Random(63)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-63.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
