# Source for library/listening/listening-114.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l114.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l114-ann-perseides", "title": "Βραδιά παρατήρησης των Περσεΐδων", "title_en": "An evening watching the Perseids", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο τοπικό ραδιόφωνο, στις αρχές Αυγούστου.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος, σε συνεργασία με τον σύλλογο ερασιτεχνών αστρονόμων, διοργανώνει βραδιά παρατήρησης των Περσεΐδων, της βροχής διαττόντων που κορυφώνεται κάθε χρόνο γύρω στις δώδεκα Αυγούστου. Τα «πεφταστέρια» αυτά είναι μικρά κομμάτια σκόνης από έναν κομήτη, που καίγονται μόλις μπουν στην ατμόσφαιρα.", "The municipality, together with the amateur astronomers' club, is organising an evening watching the Perseids, the meteor shower that peaks every year around the twelfth of August. These \"shooting stars\" are small pieces of dust from a comet, which burn up as soon as they enter the atmosphere."),
  L("Εκφωνήτρια", "f", "Η εκδήλωση θα γίνει στο ύψωμα του Προφήτη Ηλία, μακριά από τα φώτα της πόλης. Λεωφορείο του δήμου θα αναχωρεί από την κεντρική πλατεία στις δέκα το βράδυ. Δεν χρειάζεται τηλεσκόπιο: τα διάττοντα φαίνονται με γυμνό μάτι, και η καλύτερη ώρα είναι μετά τα μεσάνυχτα.", "The event will take place on the hill of Profitis Ilias, far from the city lights. A municipal bus will leave from the central square at ten in the evening. No telescope is needed: the meteors are visible to the naked eye, and the best time is after midnight."),
  L("Εκφωνήτρια", "f", "Φέρτε μαζί σας μια κουβέρτα ή ένα στρωματάκι, κάτι ζεστό να φορέσετε και νερό. Παρακαλούμε να μη χρησιμοποιείτε φακούς ή κινητά με φωτεινή οθόνη, γιατί τα μάτια χρειάζονται περίπου είκοσι λεπτά για να συνηθίσουν στο σκοτάδι.", "Bring a blanket or a mat, something warm to wear and water. Please don't use torches or phones with a bright screen, because the eyes need about twenty minutes to get used to the dark."),
 ],
 "questions": [
  Q("Τι είναι τα «πεφταστέρια», σύμφωνα με την ανακοίνωση;", ["Αστέρια που σβήνουν", "Μικρά κομμάτια σκόνης από έναν κομήτη", "Δορυφόροι που πέφτουν", "Φώτα από αεροπλάνα"], 1, "μικρά κομμάτια σκόνης από έναν κομήτη"),
  Q("Ποια είναι η καλύτερη ώρα για παρατήρηση;", ["Στις δέκα το βράδυ", "Μόλις δύσει ο ήλιος", "Μετά τα μεσάνυχτα", "Λίγο πριν από την αυγή"], 2, "η καλύτερη ώρα είναι μετά τα μεσάνυχτα"),
  Q("Γιατί δεν πρέπει να χρησιμοποιούν φακούς ή κινητά;", ["Γιατί τα μάτια χρειάζονται χρόνο για να συνηθίσουν στο σκοτάδι", "Γιατί ενοχλούν τους γείτονες", "Γιατί δεν υπάρχει σήμα", "Γιατί απαγορεύεται στο ύψωμα"], 0, "τα μάτια χρειάζονται περίπου είκοσι λεπτά για να συνηθίσουν στο σκοτάδι"),
 ],
 "gloss": {"ερασιτεχνών": "ερασιτέχνης — amateur", "Περσεΐδων": "Περσεΐδες — the Perseids (meteor shower)", "διαττόντων": "διάττων (αστέρας) — meteor, shooting star", "πεφταστέρια": "πεφταστέρι — shooting star", "κομήτη": "κομήτης — comet", "ύψωμα": "ύψωμα — hill, high ground", "γυμνό μάτι": "με γυμνό μάτι — with the naked eye", "στρωματάκι": "στρωματάκι — (small) mat"}
})

ITEMS.append({
 "id": "l114-vm-symvolaiografos", "title": "Μήνυμα από τη συμβολαιογράφο", "title_en": "A message from the notary", "type": "voicemail", "level": "B2",
 "context_el": "Αγοράζετε ένα διαμέρισμα. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Συμβολαιογράφος", "f", "Καλημέρα, κυρία Αντωνίου, η Δέσποινα Κουτρούλη είμαι, η συμβολαιογράφος. Σας τηλεφωνώ για το συμβόλαιο του διαμερίσματος. Ο πωλητής έφερε χθες όλα τα δικά του έγγραφα, οπότε μπορούμε να ορίσουμε την υπογραφή για την επόμενη Πέμπτη στις έντεκα.", "Good morning, Mrs Antoniou, it's Despoina Koutrouli, the notary. I'm calling about the contract for the flat. The seller brought all his documents yesterday, so we can set the signing for next Thursday at eleven."),
  L("Συμβολαιογράφος", "f", "Από εσάς χρειάζομαι ακόμα δύο πράγματα: τη βεβαίωση από την τράπεζα για το δάνειο και το αποδεικτικό ότι πληρώσατε τον φόρο μεταβίβασης. Αν μου τα στείλετε με ηλεκτρονικό ταχυδρομείο μέχρι τη Δευτέρα, θα έχω τον χρόνο να ετοιμάσω το σχέδιο του συμβολαίου.", "From you I still need two things: the bank's confirmation of the loan and the proof that you've paid the transfer tax. If you email them to me by Monday, I'll have time to prepare the draft contract."),
  L("Συμβολαιογράφος", "f", "Την ημέρα της υπογραφής φέρτε την αστυνομική σας ταυτότητα, όχι το διαβατήριο, γιατί η ταυτότητά σας είναι αυτή που αναφέρεται σε όλα τα έγγραφα. Το σχέδιο θα σας το στείλω την Τρίτη, για να το διαβάσετε με την ησυχία σας.", "On the day of the signing bring your identity card, not your passport, because your identity card is the one mentioned in all the documents. I'll send you the draft on Tuesday, so you can read it at your leisure."),
 ],
 "questions": [
  Q("Γιατί μπορεί πλέον να οριστεί η υπογραφή;", ["Γιατί εγκρίθηκε το δάνειο", "Γιατί ο πωλητής έφερε όλα τα έγγραφά του", "Γιατί η αγοράστρια πλήρωσε τον φόρο", "Γιατί ελευθερώθηκε το διαμέρισμα"], 1, "Ο πωλητής έφερε χθες όλα τα δικά του έγγραφα"),
  Q("Τι πρέπει να στείλει η αγοράστρια μέχρι τη Δευτέρα;", ["Το σχέδιο του συμβολαίου", "Την αστυνομική της ταυτότητα", "Τη βεβαίωση για το δάνειο και το αποδεικτικό πληρωμής του φόρου", "Τα κλειδιά του διαμερίσματος"], 2, "τη βεβαίωση από την τράπεζα για το δάνειο και το αποδεικτικό ότι πληρώσατε τον φόρο μεταβίβασης"),
  Q("Γιατί πρέπει να φέρει την ταυτότητα και όχι το διαβατήριο;", ["Γιατί η ταυτότητα αναφέρεται σε όλα τα έγγραφα", "Γιατί το διαβατήριό της έχει λήξει", "Γιατί το ζητά η τράπεζα", "Γιατί η υπογραφή γίνεται σε άλλη πόλη"], 0, "η ταυτότητά σας είναι αυτή που αναφέρεται σε όλα τα έγγραφα"),
 ],
 "gloss": {"συμβολαιογράφο": "συμβολαιογράφος — notary", "συμβόλαιο": "συμβόλαιο — contract, deed", "πωλητής": "πωλητής — seller", "έγγραφα": "έγγραφο — document", "βεβαίωση": "βεβαίωση — certificate, confirmation", "αποδεικτικό": "αποδεικτικό — proof, receipt", "μεταβίβασης": "φόρος μεταβίβασης — property transfer tax", "σχέδιο": "σχέδιο — draft", "με την ησυχία σας": "με την ησυχία σας — at your leisure"}
})

ITEMS.append({
 "id": "l114-dia-skylos-i-gata", "title": "Σκύλο ή γάτα;", "title_en": "A dog or a cat?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά αν θα πάρει κατοικίδιο.",
 "script": [
  L("Μάρκος", "m", "Τα παιδιά πάλι ζητούν σκύλο. Η Ζωή είπε ότι θα τον βγάζει βόλτα κάθε πρωί πριν από το σχολείο. Εγώ πάντως δεν την πιστεύω· δεν ξυπνάει ούτε για να φάει πρωινό.", "The kids are asking for a dog again. Zoe said she'd take it for a walk every morning before school. I don't believe her, though; she doesn't even wake up to have breakfast."),
  L("Κατερίνα", "f", "Κι εγώ το σκέφτομαι. Ο σκύλος θέλει βόλτα δύο και τρεις φορές τη μέρα, και εμείς λείπουμε από το σπίτι εννιά ώρες. Θα έμενε μόνος του όλη μέρα σε ένα διαμέρισμα. Μια γάτα είναι πιο ανεξάρτητη.", "I've been thinking about it too. A dog needs walks two or three times a day, and we're out of the house nine hours. It would be alone all day in a flat. A cat is more independent."),
  L("Μάρκος", "m", "Ναι, αλλά ο Νίκος έχει αλλεργία, θυμάσαι; Κάθε φορά που πάμε στη θεία σου, που έχει δύο γάτες, φταρνίζεται όλο το βράδυ. Γάτα δεν γίνεται.", "Yes, but Nikos has an allergy, remember? Every time we go to your aunt's, who has two cats, he sneezes all evening. A cat is out of the question."),
  L("Κατερίνα", "f", "Τότε ας κάνουμε κάτι άλλο: το καταφύγιο ζώων ψάχνει οικογένειες για να φιλοξενούν σκύλους τα Σαββατοκύριακα. Ας το δοκιμάσουμε για δύο μήνες. Αν τα παιδιά ανταποκριθούν, το ξανασυζητάμε.", "Then let's do something else: the animal shelter is looking for families to host dogs at the weekends. Let's try it for two months. If the kids live up to it, we'll discuss it again."),
 ],
 "questions": [
  Q("Γιατί ο Μάρκος δεν πιστεύει τη Ζωή;", ["Γιατί δεν της αρέσουν τα ζώα", "Γιατί δυσκολεύεται να ξυπνήσει το πρωί", "Γιατί έχει πολλά μαθήματα", "Γιατί φοβάται τους σκύλους"], 1, "δεν ξυπνάει ούτε για να φάει πρωινό"),
  Q("Γιατί η Κατερίνα έχει αμφιβολίες για τον σκύλο;", ["Γιατί κοστίζει πολύ", "Γιατί το διαμέρισμα είναι μικρό", "Γιατί θα έμενε μόνος του όλη μέρα", "Γιατί οι γείτονες θα παραπονιούνται"], 2, "Θα έμενε μόνος του όλη μέρα σε ένα διαμέρισμα"),
  Q("Τι προτείνει τελικά η Κατερίνα;", ["Να φιλοξενούν σκύλους από το καταφύγιο τα Σαββατοκύριακα", "Να πάρουν μια γάτα", "Να πάρουν ένα ψάρι", "Να περιμένουν να μεγαλώσουν τα παιδιά"], 0, "το καταφύγιο ζώων ψάχνει οικογένειες για να φιλοξενούν σκύλους τα Σαββατοκύριακα"),
 ],
 "gloss": {"κατοικίδιο": "κατοικίδιο — pet", "ανεξάρτητη": "ανεξάρτητος — independent", "αλλεργία": "αλλεργία — allergy", "φταρνίζεται": "φταρνίζομαι — to sneeze", "καταφύγιο": "καταφύγιο ζώων — animal shelter", "φιλοξενούν": "φιλοξενώ — to host, put up", "ανταποκριθούν": "ανταποκρίνομαι — to respond; to live up to"}
})

ITEMS.append({
 "id": "l114-int-xerolithies", "title": "Ο τεχνίτης της ξερολιθιάς", "title_en": "The dry-stone waller", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν τεχνίτη σε εκπομπή για τις παραδοσιακές τέχνες.",
 "script": [
  L("Δημοσιογράφος", "m", "Κύριε Βασιλείου, τι είναι ακριβώς η ξερολιθιά;", "Mr Vasileiou, what exactly is dry-stone walling?"),
  L("Τεχνίτης", "m", "Είναι ο τρόπος να χτίζεις με πέτρες χωρίς λάσπη ή τσιμέντο. Οι πέτρες κρατιούνται μόνο από το βάρος τους και από το πώς τις τοποθετείς. Στα νησιά μας, με αυτόν τον τρόπο έχουν χτιστεί χιλιάδες χιλιόμετρα από πεζούλες, μάντρες και καλύβες.", "It's the way of building with stones without mortar or cement. The stones are held together only by their weight and by how you place them. On our islands, thousands of kilometres of terraces, enclosures and huts have been built this way."),
  L("Δημοσιογράφος", "m", "Σε τι χρησίμευαν οι πεζούλες;", "What were the terraces for?"),
  L("Τεχνίτης", "m", "Σε απότομες πλαγιές δεν μπορείς να καλλιεργήσεις τίποτα. Οι πεζούλες κρατούν το χώμα, που αλλιώς θα το παρέσερνε η βροχή, και δημιουργούν μικρά επίπεδα χωράφια. Επιπλέον, το νερό περνά ανάμεσα από τις πέτρες και δεν γκρεμίζει τον τοίχο.", "On steep slopes you can't grow anything. The terraces hold the soil, which the rain would otherwise wash away, and create small flat fields. What's more, water passes between the stones and doesn't bring the wall down."),
  L("Δημοσιογράφος", "m", "Η τέχνη αυτή έχει αναγνωριστεί και από την UNESCO, έτσι δεν είναι;", "This craft has also been recognised by UNESCO, hasn't it?"),
  L("Τεχνίτης", "m", "Ναι, από το 2018, μαζί με άλλες ευρωπαϊκές χώρες. Αυτό βοήθησε να ξαναγίνουν σεμινάρια. Το καλοκαίρι έρχονται νέοι, ακόμα και αρχιτέκτονες, για να μάθουν. Τους λέω πάντα το ίδιο: η πέτρα σού δείχνει πού θέλει να μπει, αρκεί να την κοιτάξεις αρκετή ώρα.", "Yes, since 2018, together with other European countries. That helped workshops start again. In summer young people come, even architects, to learn. I always tell them the same thing: the stone shows you where it wants to go, as long as you look at it long enough."),
 ],
 "questions": [
  Q("Τι κρατά τις πέτρες στη θέση τους στην ξερολιθιά;", ["Λάσπη και άχυρο", "Το βάρος τους και ο τρόπος που τοποθετούνται", "Τσιμέντο ανάμεσα στις πέτρες", "Ξύλινα δοκάρια"], 1, "Οι πέτρες κρατιούνται μόνο από το βάρος τους και από το πώς τις τοποθετείς"),
  Q("Γιατί δεν γκρεμίζει το νερό τους τοίχους;", ["Γιατί οι τοίχοι είναι πολύ χοντροί", "Γιατί στα νησιά βρέχει λίγο", "Γιατί περνά ανάμεσα από τις πέτρες", "Γιατί οι πέτρες καλύπτονται με χώμα"], 2, "το νερό περνά ανάμεσα από τις πέτρες και δεν γκρεμίζει τον τοίχο"),
  Q("Τι βοήθησε η αναγνώριση από την UNESCO;", ["Να ξαναγίνουν σεμινάρια", "Να χτιστούν νέοι δρόμοι", "Να πουληθούν οι πέτρες", "Να έρθουν περισσότεροι τουρίστες τον χειμώνα"], 0, "Αυτό βοήθησε να ξαναγίνουν σεμινάρια"),
 ],
 "gloss": {"τεχνίτη": "τεχνίτης — craftsman", "ξερολιθιά": "ξερολιθιά — dry-stone walling", "λάσπη": "λάσπη — mud; mortar", "πεζούλες": "πεζούλα — terrace (on a slope)", "μάντρες": "μάντρα — enclosure, (stone) pen", "πλαγιές": "πλαγιά — slope", "καλλιεργήσεις": "καλλιεργώ — to cultivate", "παρέσερνε": "παρασέρνω — to sweep away, wash away", "γκρεμίζει": "γκρεμίζω — to knock down"}
})

ITEMS.append({
 "id": "l114-rep-psygeio-allileggyis", "title": "Ένα ψυγείο αλληλεγγύης στη γειτονιά", "title_en": "A solidarity fridge in the neighbourhood", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε ενημερωτική εκπομπή του ραδιοφώνου.",
 "script": [
  L("Ρεπόρτερ", "f", "Στη γωνία μιας πλατείας στην Καλλιθέα στέκεται ένα ψυγείο ζωγραφισμένο με λουλούδια, ένα «ψυγείο αλληλεγγύης». Πάνω του γράφει: «Άφησε ό,τι περισσεύει, πάρε ό,τι χρειάζεσαι». Το έβαλε εκεί πριν από έναν χρόνο μια ομάδα γειτόνων, με τη βοήθεια ενός μίνι μάρκετ που του δίνει ρεύμα.", "On the corner of a square in Kallithea stands a fridge painted with flowers, a \"solidarity fridge\". On it is written: \"Leave what you don't need, take what you need.\" A group of neighbours put it there a year ago, with the help of a mini-market that gives it electricity."),
  L("Ρεπόρτερ", "f", "Κάθε μέρα φούρνοι, μανάβικα και νοικοκυριά αφήνουν μέσα ψωμί, φρούτα, γιαούρτια και φαγητό σε κλειστά δοχεία. Υπάρχουν όμως κανόνες: όχι ωμό κρέας, όχι αλκοόλ και όχι προϊόντα που έχουν λήξει. Κάθε απόγευμα ένας εθελοντής ελέγχει τις ημερομηνίες και καθαρίζει το ψυγείο.", "Every day bakeries, greengrocers and households leave bread, fruit, yoghurts and food in sealed containers. But there are rules: no raw meat, no alcohol and no products past their expiry date. Every afternoon a volunteer checks the dates and cleans the fridge."),
  L("Ρεπόρτερ", "f", "Όπως λέει μια από τις εμπνεύστριες της ιδέας, δεν το χρησιμοποιούν μόνο άνθρωποι που έχουν ανάγκη. «Έρχονται και φοιτητές στο τέλος του μήνα, και συνταξιούχοι που δεν θέλουν να πετάξουν το φαγητό που μαγείρεψαν. Δεν ρωτάμε ποτέ κανέναν γιατί παίρνει.»", "As one of the people behind the idea says, it isn't only used by people in need. \"Students come at the end of the month, and pensioners who don't want to throw away food they've cooked. We never ask anyone why they're taking something.\""),
 ],
 "questions": [
  Q("Ποιος δίνει ρεύμα στο ψυγείο;", ["Ο δήμος", "Ένα μίνι μάρκετ", "Οι γείτονες με τη σειρά", "Ένα φωτοβολταϊκό"], 1, "με τη βοήθεια ενός μίνι μάρκετ που του δίνει ρεύμα"),
  Q("Ποιο από τα παρακάτω δεν επιτρέπεται να αφήσει κανείς στο ψυγείο;", ["Φρούτα", "Γιαούρτια", "Ωμό κρέας", "Φαγητό σε κλειστά δοχεία"], 2, "όχι ωμό κρέας"),
  Q("Τι κάνει κάθε απόγευμα ένας εθελοντής;", ["Ελέγχει τις ημερομηνίες και καθαρίζει το ψυγείο", "Μοιράζει φαγητό στα σπίτια", "Μαγειρεύει για όσους έχουν ανάγκη", "Κλειδώνει το ψυγείο"], 0, "ένας εθελοντής ελέγχει τις ημερομηνίες και καθαρίζει το ψυγείο"),
 ],
 "gloss": {"αλληλεγγύης": "αλληλεγγύη — solidarity", "περισσεύει": "περισσεύω — to be left over, be surplus", "νοικοκυριά": "νοικοκυριό — household", "δοχεία": "δοχείο — container", "ωμό": "ωμός — raw", "λήξει": "λήγω — to expire", "εμπνεύστριες": "εμπνεύστρια — (female) originator, the person behind an idea", "συνταξιούχοι": "συνταξιούχος — pensioner"}
})

ITEMS.append({
 "id": "l114-rep-kokkino-skathari", "title": "Οι φοίνικες της πόλης κινδυνεύουν", "title_en": "The city's palm trees are in danger", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις τοπικές ειδήσεις μιας παραθαλάσσιας πόλης.",
 "script": [
  L("Ρεπόρτερ", "m", "Οι φοίνικες της παραλιακής λεωφόρου, σύμβολο της πόλης εδώ και έναν αιώνα, απειλούνται από ένα έντομο λίγων εκατοστών: το κόκκινο σκαθάρι των φοινικοειδών. Το σκαθάρι αυτό ήρθε από την Ασία και εντοπίστηκε στην Ελλάδα για πρώτη φορά πριν από περίπου είκοσι χρόνια.", "The palm trees on the seafront avenue, a symbol of the city for a century, are threatened by an insect a few centimetres long: the red palm weevil. This beetle came from Asia and was first detected in Greece about twenty years ago."),
  L("Ρεπόρτερ", "m", "Το δύσκολο είναι ότι η ζημιά δεν φαίνεται εγκαίρως. Οι προνύμφες τρώνε το δέντρο από μέσα, και όταν τα φύλλα της κορυφής αρχίσουν να γέρνουν σαν ανοιχτή ομπρέλα, συνήθως είναι πια αργά. Ήδη έντεκα φοίνικες έχουν κοπεί μέσα στη χρονιά.", "The difficult thing is that the damage isn't visible in time. The larvae eat the tree from the inside, and when the leaves at the top begin to droop like an open umbrella, it's usually too late. Eleven palm trees have already been cut down this year."),
  L("Ρεπόρτερ", "m", "Ο δήμος ξεκίνησε πρόγραμμα με ενέσεις στους κορμούς των υγιών δέντρων κάθε δύο μήνες. Ζητά επίσης από τους κατοίκους που έχουν φοίνικες στους κήπους τους να ειδοποιούν την υπηρεσία πρασίνου μόλις δουν κιτρινισμένα ή πεσμένα φύλλα, και να μην πετούν μόνοι τους τα κομμένα κλαδιά, γιατί μπορεί να μεταφέρουν το έντομο.", "The municipality has started a programme of injections into the trunks of healthy trees every two months. It is also asking residents who have palm trees in their gardens to notify the parks department as soon as they see yellowed or drooping leaves, and not to dispose of cut fronds themselves, because they may carry the insect."),
 ],
 "questions": [
  Q("Γιατί είναι δύσκολο να σωθούν οι φοίνικες;", ["Γιατί είναι πολύ ψηλοί", "Γιατί η ζημιά δεν φαίνεται εγκαίρως", "Γιατί δεν υπάρχει φάρμακο", "Γιατί είναι πολύ παλιοί"], 1, "η ζημιά δεν φαίνεται εγκαίρως"),
  Q("Ποιο είναι το σημάδι ότι είναι πια αργά;", ["Το δέντρο βγάζει λουλούδια", "Ο κορμός γίνεται κόκκινος", "Τα φύλλα της κορυφής γέρνουν σαν ανοιχτή ομπρέλα", "Πέφτουν οι καρποί"], 2, "τα φύλλα της κορυφής αρχίσουν να γέρνουν σαν ανοιχτή ομπρέλα"),
  Q("Γιατί δεν πρέπει οι κάτοικοι να πετούν μόνοι τους τα κομμένα κλαδιά;", ["Γιατί μπορεί να μεταφέρουν το έντομο", "Γιατί είναι πολύ βαριά", "Γιατί υπάρχει πρόστιμο", "Γιατί ο δήμος τα χρησιμοποιεί για λίπασμα"], 0, "μπορεί να μεταφέρουν το έντομο"),
 ],
 "gloss": {"φοίνικες": "φοίνικας — palm tree", "λεωφόρου": "λεωφόρος — avenue", "σκαθάρι": "σκαθάρι — beetle", "φοινικοειδών": "φοινικοειδή — palms (the palm family)", "εντοπίστηκε": "εντοπίζω — to detect, locate", "εγκαίρως": "εγκαίρως — in time", "προνύμφες": "προνύμφη — larva", "γέρνουν": "γέρνω — to lean, droop", "κορμούς": "κορμός — trunk", "πρασίνου": "υπηρεσία πρασίνου — parks department"}
})

ITEMS.append({
 "id": "l114-mono-allaxa-douleia", "title": "Άλλαξα επάγγελμα στα σαράντα οχτώ", "title_en": "I changed careers at forty-eight", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλά σε ραδιοφωνική εκπομπή για ανθρώπους που άλλαξαν ζωή.",
 "script": [
  L("Αφηγητής", "m", "Για είκοσι δύο χρόνια δούλευα σε ασφαλιστική εταιρεία· ήταν το μόνο επάγγελμα που ήξερα. Είχα καλό μισθό, σταθερό ωράριο και ένα γραφείο με θέα στο πάρκινγκ. Δεν ήμουν δυστυχισμένος· απλώς κάθε Κυριακή βράδυ ένιωθα ένα βάρος στο στομάχι.", "For twenty-two years I worked at an insurance company; it was the only profession I knew. I had a good salary, fixed hours and an office with a view of the car park. I wasn't unhappy; it's just that every Sunday evening I felt a weight in my stomach."),
  L("Αφηγητής", "m", "Όταν η εταιρεία συγχωνεύτηκε με μια άλλη και πρότεινε εθελουσία έξοδο, η γυναίκα μου μού είπε: «Αν δεν το κάνεις τώρα, δεν θα το κάνεις ποτέ». Από παιδί μου άρεσε να φτιάχνω πράγματα με τα χέρια, οπότε γράφτηκα σε μια σχολή ηλεκτρολόγων. Ήμουν ο μεγαλύτερος στην τάξη κατά είκοσι πέντε χρόνια.", "When the company merged with another and offered voluntary redundancy, my wife said to me: \"If you don't do it now, you'll never do it.\" Since childhood I'd liked making things with my hands, so I enrolled in a school for electricians. I was the oldest in the class by twenty-five years."),
  L("Αφηγητής", "m", "Τα πρώτα δύο χρόνια βγάζαμε δύσκολα τον μήνα, και δεν θα πω ψέματα, κάποια βράδια αναρωτιόμουν τι είχα κάνει. Σήμερα έχω δικό μου μικρό συνεργείο. Βγάζω λιγότερα απ' ό,τι στην ασφαλιστική, αλλά οι Κυριακές μου είναι πια ήσυχες.", "The first two years we struggled to make ends meet, and I won't lie, some evenings I wondered what I'd done. Today I have my own small business. I earn less than at the insurance company, but my Sundays are peaceful now."),
 ],
 "questions": [
  Q("Τι ένιωθε ο αφηγητής κάθε Κυριακή βράδυ;", ["Χαρά για τη νέα εβδομάδα", "Ένα βάρος στο στομάχι", "Κούραση από το Σαββατοκύριακο", "Τίποτα ιδιαίτερο"], 1, "κάθε Κυριακή βράδυ ένιωθα ένα βάρος στο στομάχι"),
  Q("Τι του έδωσε την ευκαιρία να αλλάξει δουλειά;", ["Μια κληρονομιά", "Μια απόλυση χωρίς αποζημίωση", "Η εθελουσία έξοδος μετά τη συγχώνευση της εταιρείας", "Μια προαγωγή"], 2, "Όταν η εταιρεία συγχωνεύτηκε με μια άλλη και πρότεινε εθελουσία έξοδο"),
  Q("Πώς είναι σήμερα τα οικονομικά του σε σχέση με πριν;", ["Βγάζει λιγότερα απ' ό,τι στην ασφαλιστική", "Βγάζει πολύ περισσότερα", "Βγάζει τα ίδια", "Δεν βγάζει ακόμα τίποτα"], 0, "Βγάζω λιγότερα απ' ό,τι στην ασφαλιστική"),
 ],
 "gloss": {"επάγγελμα": "επάγγελμα — profession, career", "ασφαλιστική": "ασφαλιστική (εταιρεία) — insurance company", "ωράριο": "ωράριο — working hours", "δυστυχισμένος": "δυστυχισμένος — unhappy", "συγχωνεύτηκε": "συγχωνεύομαι — to merge", "εθελουσία": "εθελουσία έξοδος — voluntary redundancy", "ηλεκτρολόγων": "ηλεκτρολόγος — electrician", "βγάζαμε δύσκολα τον μήνα": "βγάζω δύσκολα τον μήνα — to struggle to make ends meet", "συνεργείο": "συνεργείο — workshop, small business (of a tradesman)"}
})

ITEMS.append({
 "id": "l114-mono-kollisa-asanser", "title": "Δύο ώρες κλεισμένη στο ασανσέρ", "title_en": "Two hours stuck in the lift", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να διηγείται μια ιστορία σε ραδιοφωνική εκπομπή με ιστορίες ακροατών.",
 "script": [
  L("Αφηγήτρια", "f", "Ήταν Παρασκευή απόγευμα, ο πρώτος ζεστός Ιούνιος που μέναμε στην καινούργια πολυκατοικία. Μπήκα στο ασανσέρ με δύο σακούλες από το σούπερ μάρκετ, και ανάμεσα στον τρίτο και τον τέταρτο όροφο ακούστηκε ένα «κλακ» και όλα σταμάτησαν. Το φως έμεινε αναμμένο, ευτυχώς.", "It was a Friday afternoon, the first hot June we lived in the new block of flats. I got into the lift with two bags from the supermarket, and between the third and the fourth floor there was a \"click\" and everything stopped. The light stayed on, fortunately."),
  L("Αφηγήτρια", "f", "Πάτησα το κουμπί του συναγερμού και μου απάντησε μια ηχογραφημένη φωνή ότι ο τεχνικός θα ερχόταν «το συντομότερο δυνατό». Το «συντομότερο δυνατό» αποδείχτηκε δύο ώρες. Στην αρχή πανικοβλήθηκα, μετά θύμωσα και στο τέλος κάθισα στο πάτωμα κι άνοιξα ένα πακέτο μπισκότα.", "I pressed the alarm button and a recorded voice told me the technician would come \"as soon as possible\". \"As soon as possible\" turned out to be two hours. At first I panicked, then I got angry, and in the end I sat on the floor and opened a packet of biscuits."),
  L("Αφηγήτρια", "f", "Το πιο απρόσμενο ήταν οι γείτονες. Μαζεύτηκαν στον διάδρομο του τέταρτου ορόφου, μου μιλούσαν από τη χαραμάδα της πόρτας και μου πέρασαν ένα μπουκάλι νερό με ένα καλαμάκι. Πριν από εκείνη τη μέρα δεν ήξερα ούτε τα ονόματά τους· τώρα κάνουμε μαζί το τραπέζι της πολυκατοικίας κάθε Σεπτέμβριο.", "The most unexpected thing was the neighbours. They gathered in the fourth-floor corridor, talked to me through the gap in the door and passed me a bottle of water with a straw. Before that day I didn't even know their names; now we hold the building's get-together dinner every September."),
 ],
 "questions": [
  Q("Πού σταμάτησε το ασανσέρ;", ["Στο ισόγειο", "Ανάμεσα στον τρίτο και τον τέταρτο όροφο", "Στον τελευταίο όροφο", "Στο υπόγειο"], 1, "ανάμεσα στον τρίτο και τον τέταρτο όροφο"),
  Q("Πώς αντέδρασε τελικά η αφηγήτρια στην αναμονή;", ["Φώναζε συνέχεια", "Προσπάθησε να ανοίξει την πόρτα", "Κάθισε στο πάτωμα κι άνοιξε ένα πακέτο μπισκότα", "Κοιμήθηκε"], 2, "στο τέλος κάθισα στο πάτωμα κι άνοιξα ένα πακέτο μπισκότα"),
  Q("Τι άλλαξε μετά από εκείνη τη μέρα;", ["Γνώρισε τους γείτονές της και κάνουν μαζί το τραπέζι της πολυκατοικίας", "Μετακόμισε σε άλλη πολυκατοικία", "Δεν παίρνει πια ποτέ το ασανσέρ", "Έγινε διαχειρίστρια της πολυκατοικίας"], 0, "τώρα κάνουμε μαζί το τραπέζι της πολυκατοικίας κάθε Σεπτέμβριο"),
 ],
 "gloss": {"πολυκατοικία": "πολυκατοικία — block of flats", "συναγερμού": "συναγερμός — alarm", "ηχογραφημένη": "ηχογραφημένος — recorded", "αποδείχτηκε": "αποδεικνύομαι — to turn out, prove to be", "πανικοβλήθηκα": "πανικοβάλλομαι — to panic", "απρόσμενο": "απρόσμενος — unexpected", "χαραμάδα": "χαραμάδα — gap, crack", "καλαμάκι": "καλαμάκι — (drinking) straw"}
})

ITEMS.append({
 "id": "l114-c1-deka-chiliades-ores", "title": "Ο μύθος των δέκα χιλιάδων ωρών", "title_en": "The myth of the ten thousand hours", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ομιλία σε συνέδριο για την εκπαίδευση.",
 "script": [
  L("Ομιλητής", "m", "Θα έχετε ακούσει τον «κανόνα των δέκα χιλιάδων ωρών»: αν εξασκηθείτε σε οτιδήποτε για δέκα χιλιάδες ώρες, θα γίνετε κορυφαίοι. Ο κανόνας έγινε δημοφιλής το 2008, χάρη σε ένα βιβλίο του δημοσιογράφου Μάλκολμ Γκλάντγουελ. Η πηγή του, όμως, είναι μια έρευνα του 1993, που λέει κάτι αρκετά διαφορετικό.", "You'll have heard of the \"ten-thousand-hour rule\": if you practise anything for ten thousand hours, you'll become one of the best. The rule became popular in 2008, thanks to a book by the journalist Malcolm Gladwell. Its source, however, is a 1993 study, which says something rather different."),
  L("Ομιλητής", "m", "Ο ψυχολόγος Άντερς Έρικσον και οι συνεργάτες του μελέτησαν βιολονίστες σε μια μουσική ακαδημία του Βερολίνου. Βρήκαν ότι οι καλύτεροι είχαν συγκεντρώσει μέχρι τα είκοσί τους, κατά μέσο όρο, γύρω στις δέκα χιλιάδες ώρες εξάσκησης. Κατά μέσο όρο: κάποιοι πολύ λιγότερες. Και ο αριθμός δεν ήταν κάποιο μαγικό όριο· απλώς η στιγμή στην οποία έτυχε να γίνει η μέτρηση.", "The psychologist Anders Ericsson and his colleagues studied violinists at a music academy in Berlin. They found that the best had accumulated by the age of twenty, on average, around ten thousand hours of practice. On average: some considerably fewer. And the number wasn't some magic threshold; simply the point at which the measurement happened to be taken."),
  L("Ομιλητής", "m", "Ο ίδιος ο Έρικσον επέμενε ότι αυτό που μετρά δεν είναι ο αριθμός των ωρών αλλά το είδος τους. Το ονόμασε «σκόπιμη εξάσκηση»: δουλειά στα σημεία όπου αποτυγχάνεις, με σαφείς στόχους και άμεση ανατροφοδότηση, συνήθως από έναν δάσκαλο. Δέκα χιλιάδες ώρες που επαναλαμβάνεις όσα ήδη ξέρεις δεν σε κάνουν καλύτερο· σε κάνουν απλώς πιο σίγουρο για τα λάθη σου.", "Ericsson himself insisted that what counts is not the number of hours but their kind. He called it \"deliberate practice\": working on the points where you fail, with clear goals and immediate feedback, usually from a teacher. Ten thousand hours repeating what you already know don't make you better; they just make you more confident about your mistakes."),
  L("Ομιλητής", "m", "Μεταγενέστερες έρευνες έδειξαν, επιπλέον, ότι η εξάσκηση εξηγεί μόνο ένα μέρος των διαφορών ανάμεσα στους ανθρώπους· ρόλο παίζουν και η ηλικία έναρξης, η προσωπικότητα, ακόμα και η τύχη. Αυτό δεν είναι απογοητευτικό. Σημαίνει ότι δεν χρειάζεται να μετράτε ώρες· χρειάζεται να μετράτε τα λάθη που διορθώσατε.", "Later studies also showed that practice explains only part of the differences between people; starting age, personality and even luck play a role too. That isn't discouraging. It means you don't need to count hours; you need to count the mistakes you've corrected."),
 ],
 "questions": [
  Q("Πώς έγινε δημοφιλής ο κανόνας των δέκα χιλιάδων ωρών;", ["Από μια έρευνα του 1993", "Από ένα βιβλίο του 2008", "Από μια μουσική ακαδημία", "Από ένα τηλεοπτικό ντοκιμαντέρ"], 1, "Ο κανόνας έγινε δημοφιλής το 2008, χάρη σε ένα βιβλίο"),
  Q("Τι λέει ο ομιλητής για τον αριθμό των δέκα χιλιάδων ωρών στην αρχική έρευνα;", ["Ότι ήταν το ελάχιστο για να γίνει κανείς κορυφαίος", "Ότι ίσχυε για όλους τους βιολονίστες", "Ότι ήταν μέσος όρος και όχι μαγικό όριο", "Ότι τον υπολόγισε ο Γκλάντγουελ"], 2, "ο αριθμός δεν ήταν κάποιο μαγικό όριο"),
  Q("Τι είναι, σύμφωνα με τον Έρικσον, η «σκόπιμη εξάσκηση»;", ["Δουλειά στα σημεία όπου αποτυγχάνεις, με σαφείς στόχους και άμεση ανατροφοδότηση", "Επανάληψη όσων ήδη ξέρεις", "Εξάσκηση πολλές ώρες χωρίς διάλειμμα", "Εξάσκηση μόνο με άλλους μαθητές"], 0, "δουλειά στα σημεία όπου αποτυγχάνεις, με σαφείς στόχους και άμεση ανατροφοδότηση"),
  Q("Ποιο είναι το τελικό μήνυμα του ομιλητή;", ["Ότι η εξάσκηση δεν έχει αξία", "Ότι πρέπει να μετράμε τα λάθη που διορθώσαμε, όχι τις ώρες", "Ότι μετράει μόνο η τύχη", "Ότι πρέπει να ξεκινάμε από μικρή ηλικία"], 1, "χρειάζεται να μετράτε τα λάθη που διορθώσατε"),
 ],
 "gloss": {"εξασκηθείτε": "εξασκούμαι — to practise", "κορυφαίοι": "κορυφαίος — top, leading", "βιολονίστες": "βιολονίστας — violinist", "συγκεντρώσει": "συγκεντρώνω — to accumulate, gather", "έτυχε": "τυχαίνω — to happen (by chance)", "επέμενε": "επιμένω — to insist", "σκόπιμη": "σκόπιμος — deliberate, purposeful", "ανατροφοδότηση": "ανατροφοδότηση — feedback", "Μεταγενέστερες": "μεταγενέστερος — later, subsequent", "απογοητευτικό": "απογοητευτικός — discouraging, disappointing"}
})

ITEMS.append({
 "id": "l114-c1-frape", "title": "Ο φραπές: ένα ατύχημα που έγινε εθνικό ποτό", "title_en": "The frappé: an accident that became a national drink", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια ιστορικό της διατροφής σε εκπομπή για την καθημερινή ζωή.",
 "script": [
  L("Δημοσιογράφος", "m", "Λένε ότι ο φραπές γεννήθηκε κατά λάθος. Ισχύει;", "They say the frappé was born by accident. Is that true?"),
  L("Ιστορικός", "f", "Έτσι λέει τουλάχιστον η ιστορία που επαναλαμβάνεται εδώ και δεκαετίες, και δεν έχουμε λόγο να την αμφισβητήσουμε. Το 1957, στη Διεθνή Έκθεση Θεσσαλονίκης, η Nestlé παρουσίαζε ένα σοκολατούχο ρόφημα που χτυπιόταν με κρύο νερό σε σέικερ. Ένας υπάλληλός της, ο Δημήτρης Βακόνδιος, ήθελε να πιει τον στιγμιαίο καφέ του στο διάλειμμα, αλλά δεν βρήκε ζεστό νερό. Έριξε λοιπόν τον καφέ στο σέικερ με κρύο νερό και πάγο, και το αποτέλεσμα τού άρεσε.", "That's what the story repeated for decades says, at least, and we have no reason to doubt it. In 1957, at the Thessaloniki International Fair, Nestlé was presenting a chocolate drink that was shaken with cold water in a shaker. One of its employees, Dimitris Vakondios, wanted to drink his instant coffee during the break, but couldn't find hot water. So he put the coffee in the shaker with cold water and ice, and he liked the result."),
  L("Δημοσιογράφος", "m", "Και πώς έγινε από ένα αυτοσχέδιο ποτό σύμβολο μιας ολόκληρης χώρας;", "And how did an improvised drink become the symbol of an entire country?"),
  L("Ιστορικός", "f", "Ο φραπές ταίριαζε απόλυτα στο ελληνικό καλοκαίρι και, κυρίως, στον ελληνικό τρόπο να πίνεις καφέ: αργά, με παρέα, για ώρες. Ένας φραπές με πολύ πάγο μπορεί να «κρατήσει» ένα ολόκληρο απόγευμα συζήτησης. Από τη δεκαετία του '80, με την ανάπτυξη του τουρισμού και των καφετεριών, έγινε σχεδόν σήμα κατατεθέν της χώρας, σε σημείο που πολλοί ξένοι τον θεωρούσαν ελληνική εφεύρεση με βαθιές ρίζες.", "The frappé suited the Greek summer perfectly and, above all, the Greek way of drinking coffee: slowly, in company, for hours. A frappé with lots of ice can \"last\" a whole afternoon of conversation. From the 1980s, with the growth of tourism and cafés, it became almost a trademark of the country, to the point that many foreigners took it for a Greek invention with deep roots."),
  L("Δημοσιογράφος", "m", "Σήμερα όμως οι νέοι προτιμούν τον φρέντο εσπρέσο.", "Today, though, young people prefer the freddo espresso."),
  L("Ιστορικός", "f", "Πράγματι, τα τελευταία χρόνια ο φρέντο έχει κερδίσει έδαφος, ιδίως στις πόλεις. Δεν θα έλεγα όμως ότι ο φραπές πεθαίνει. Μάλλον περνά από την καθημερινότητα στη νοσταλγία: για πολλούς είναι η γεύση της εφηβείας, των διακοπών στο χωριό, των πρώτων ραντεβού. Και τα ποτά που φορτώνονται αναμνήσεις σπάνια εξαφανίζονται εντελώς.", "Indeed, in recent years the freddo has gained ground, especially in the cities. But I wouldn't say the frappé is dying. It's rather moving from everyday life into nostalgia: for many it's the taste of adolescence, of holidays in the village, of first dates. And drinks that get loaded with memories rarely disappear completely."),
 ],
 "questions": [
  Q("Γιατί ο Βακόνδιος έφτιαξε τον πρώτο φραπέ;", ["Γιατί ήθελε να παρουσιάσει ένα νέο προϊόν", "Γιατί δεν βρήκε ζεστό νερό για τον καφέ του", "Γιατί έκανε πολλή ζέστη", "Γιατί το ζήτησε ένας πελάτης"], 1, "δεν βρήκε ζεστό νερό"),
  Q("Γιατί, κατά την ιστορικό, ο φραπές ταίριαξε στον ελληνικό τρόπο ζωής;", ["Γιατί ήταν φτηνός", "Γιατί φτιαχνόταν γρήγορα", "Γιατί μπορεί να «κρατήσει» ένα ολόκληρο απόγευμα συζήτησης", "Γιατί τον διαφήμιζαν πολύ"], 2, "Ένας φραπές με πολύ πάγο μπορεί να «κρατήσει» ένα ολόκληρο απόγευμα συζήτησης"),
  Q("Τι πίστευαν πολλοί ξένοι για τον φραπέ;", ["Ότι ήταν ελληνική εφεύρεση με βαθιές ρίζες", "Ότι ήταν ιταλικός", "Ότι ήταν ποτό μόνο για τουρίστες", "Ότι ήταν πολύ δυνατός"], 0, "πολλοί ξένοι τον θεωρούσαν ελληνική εφεύρεση με βαθιές ρίζες"),
  Q("Τι πιστεύει η ιστορικός για το μέλλον του φραπέ;", ["Ότι θα εξαφανιστεί σύντομα", "Ότι περνά από την καθημερινότητα στη νοσταλγία", "Ότι θα ξαναγίνει το πιο δημοφιλές ποτό", "Ότι θα τον πίνουν μόνο οι τουρίστες"], 1, "Μάλλον περνά από την καθημερινότητα στη νοσταλγία"),
 ],
 "gloss": {"αμφισβητήσουμε": "αμφισβητώ — to question, dispute", "σοκολατούχο": "σοκολατούχος — chocolate (containing chocolate)", "ρόφημα": "ρόφημα — drink, beverage", "στιγμιαίο": "στιγμιαίος — instant", "αυτοσχέδιο": "αυτοσχέδιος — improvised", "σήμα κατατεθέν": "σήμα κατατεθέν — trademark", "εφεύρεση": "εφεύρεση — invention", "έδαφος": "κερδίζω έδαφος — to gain ground", "εφηβείας": "εφηβεία — adolescence", "φορτώνονται": "φορτώνομαι — to be loaded (with)"}
})

rnd = random.Random(114)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-114.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
