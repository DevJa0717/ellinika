# Source for library/listening/listening-116.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l116.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l116-ann-allagi-apovathras", "title": "Αλλαγή αποβάθρας στον σταθμό", "title_en": "A platform change at the station", "type": "announcement", "level": "B2",
 "context_el": "Περιμένετε το τρένο για την Αθήνα στον σιδηροδρομικό σταθμό της Λάρισας. Ακούτε μια ανακοίνωση.",
 "script": [
  L("Εκφωνήτρια", "f", "Προσοχή, παρακαλώ. Ο συρμός για την Αθήνα, με αναχώρηση στις δέκα και είκοσι, δεν θα αναχωρήσει από την αποβάθρα δύο, όπως είχε ανακοινωθεί, αλλά από την αποβάθρα πέντε, λόγω εργασιών συντήρησης στις γραμμές.", "Attention, please. The train to Athens, departing at ten twenty, will not leave from platform two, as had been announced, but from platform five, because of maintenance work on the tracks."),
  L("Εκφωνήτρια", "f", "Οι επιβάτες παρακαλούνται να χρησιμοποιήσουν την υπόγεια διάβαση και όχι να διασχίσουν τις γραμμές. Για άτομα με κινητικές δυσκολίες, υπάρχει ανελκυστήρας δίπλα στο εκδοτήριο εισιτηρίων.", "Passengers are asked to use the underpass and not to cross the tracks. For people with mobility difficulties, there is a lift next to the ticket office."),
  L("Εκφωνήτρια", "f", "Λόγω της αλλαγής, ο συρμός θα αναχωρήσει με καθυστέρηση περίπου δέκα λεπτών. Τα εισιτήρια και οι κρατήσεις θέσεων ισχύουν κανονικά. Ευχαριστούμε για την κατανόηση.", "Because of the change, the train will leave about ten minutes late. Tickets and seat reservations remain valid as normal. Thank you for your understanding."),
 ],
 "questions": [
  Q("Από ποια αποβάθρα θα αναχωρήσει τελικά το τρένο;", ["Από την αποβάθρα δύο", "Από την αποβάθρα τρία", "Από την αποβάθρα πέντε", "Από την αποβάθρα έξι"], 2, "αλλά από την αποβάθρα πέντε"),
  Q("Τι ζητείται από τους επιβάτες;", ["Να χρησιμοποιήσουν την υπόγεια διάβαση", "Να αλλάξουν τα εισιτήριά τους", "Να περιμένουν στο εκδοτήριο", "Να πάρουν το επόμενο τρένο"], 0, "παρακαλούνται να χρησιμοποιήσουν την υπόγεια διάβαση"),
  Q("Τι ισχύει για τις κρατήσεις θέσεων;", ["Ακυρώνονται", "Πρέπει να επιβεβαιωθούν ξανά", "Ισχύουν μόνο για την πρώτη θέση", "Ισχύουν κανονικά"], 3, "Τα εισιτήρια και οι κρατήσεις θέσεων ισχύουν κανονικά"),
 ],
 "gloss": {"συρμός": "συρμός — train", "αποβάθρα": "αποβάθρα — platform", "συντήρησης": "συντήρηση — maintenance", "διάβαση": "υπόγεια διάβαση — underpass", "διασχίσουν": "διασχίζω — to cross", "κινητικές": "κινητικές δυσκολίες — mobility difficulties", "ανελκυστήρας": "ανελκυστήρας — lift, elevator", "εκδοτήριο": "εκδοτήριο εισιτηρίων — ticket office", "κρατήσεις": "κράτηση θέσης — seat reservation", "κατανόηση": "κατανόηση — understanding"}
})

ITEMS.append({
 "id": "l116-vm-grammateia-dikaiologitiko", "title": "Μήνυμα από τη γραμματεία της σχολής", "title_en": "A message from the faculty office", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κάνει αίτηση για μεταπτυχιακό. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, ο Παύλος είμαι από τη γραμματεία του μεταπτυχιακού προγράμματος. Σας τηλεφωνώ για την αίτησή σας. Την παραλάβαμε, αλλά λείπει ένα δικαιολογητικό: η βεβαίωση γλωσσομάθειας για τα αγγλικά.", "Good morning, this is Pavlos from the postgraduate programme office. I'm calling about your application. We've received it, but one supporting document is missing: the certificate of English proficiency."),
  L("Υπάλληλος", "m", "Αν δεν έχετε ακόμη το πτυχίο, μπορείτε προσωρινά να στείλετε τη βεβαίωση επιτυχίας από τον φορέα των εξετάσεων. Το πρωτότυπο θα το φέρετε αργότερα, πριν από την εγγραφή.", "If you don't have the certificate yet, you can temporarily send the confirmation of passing from the examination body. You'll bring the original later, before enrolment."),
  L("Υπάλληλος", "m", "Η προθεσμία λήγει την Παρασκευή στις δύο το μεσημέρι. Μπορείτε να το στείλετε ηλεκτρονικά, αρκεί να είναι σκαναρισμένο και όχι φωτογραφία από το κινητό. Οι συνεντεύξεις θα γίνουν στις αρχές του επόμενου μήνα. Καλή συνέχεια.", "The deadline expires on Friday at two in the afternoon. You can send it electronically, as long as it is scanned and not a photo from your mobile. The interviews will take place at the beginning of next month. All the best."),
 ],
 "questions": [
  Q("Τι λείπει από την αίτηση;", ["Το βιογραφικό", "Η βεβαίωση γλωσσομάθειας", "Οι συστατικές επιστολές", "Η φωτογραφία ταυτότητας"], 1, "λείπει ένα δικαιολογητικό: η βεβαίωση γλωσσομάθειας για τα αγγλικά"),
  Q("Τι μπορεί να στείλει προσωρινά όποιος δεν έχει ακόμη το πτυχίο;", ["Τη βεβαίωση επιτυχίας από τον φορέα των εξετάσεων", "Μια υπεύθυνη δήλωση", "Το πρόγραμμα των μαθημάτων", "Μια φωτογραφία από το κινητό"], 0, "μπορείτε προσωρινά να στείλετε τη βεβαίωση επιτυχίας από τον φορέα των εξετάσεων"),
  Q("Με ποια προϋπόθεση γίνεται δεκτή η ηλεκτρονική αποστολή;", ["Να σταλεί πριν από τη Δευτέρα", "Να υπογραφεί από τον καθηγητή", "Να είναι σκαναρισμένο το έγγραφο", "Να σταλεί και με ταχυδρομείο"], 2, "αρκεί να είναι σκαναρισμένο και όχι φωτογραφία από το κινητό"),
 ],
 "gloss": {"γραμματεία": "γραμματεία — (administrative) office", "μεταπτυχιακού": "μεταπτυχιακό — postgraduate programme", "δικαιολογητικό": "δικαιολογητικό — supporting document", "βεβαίωση": "βεβαίωση — certificate, confirmation", "γλωσσομάθειας": "γλωσσομάθεια — knowledge of foreign languages", "φορέα": "φορέας — body, organisation", "πρωτότυπο": "πρωτότυπο — original (document)", "εγγραφή": "εγγραφή — enrolment, registration", "προθεσμία": "προθεσμία — deadline", "σκαναρισμένο": "σκαναρισμένος — scanned"}
})

ITEMS.append({
 "id": "l116-dial-tatouaz", "title": "Να κάνω τατουάζ;", "title_en": "Should I get a tattoo?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φίλες, η Δανάη και η Ζωή, συζητούν σε ένα καφέ.",
 "script": [
  L("Δανάη", "f", "Ζωή, πήρα την απόφαση. Τα γενέθλιά μου θα τα γιορτάσω με ένα τατουάζ. Ένα μικρό χελιδόνι, εδώ, στον καρπό.", "Zoi, I've made the decision. I'll celebrate my birthday with a tattoo. A small swallow, here, on my wrist."),
  L("Ζωή", "f", "Ωραίο σχέδιο, αλλά στον καρπό; Θα φαίνεται συνέχεια. Στη δουλειά σου, στην τράπεζα, δεν θα έχεις πρόβλημα;", "Nice design, but on your wrist? It'll show all the time. At your work, at the bank, won't you have a problem?"),
  L("Δανάη", "f", "Ρώτησα ήδη. Η διευθύντριά μου έχει τρία, και μάλιστα πιο μεγάλα. Εκείνο που με απασχολεί περισσότερο είναι αν θα πονέσει.", "I've already asked. My manager has three, and bigger ones too. What worries me more is whether it'll hurt."),
  L("Ζωή", "f", "Ο καρπός είναι από τα πιο ευαίσθητα σημεία, έτσι λένε. Εγώ πάντως θα σκεφτόμουν πρώτα αν θα μου αρέσει και σε είκοσι χρόνια. Η αφαίρεση με λέιζερ είναι ακριβή και θέλει πολλές συνεδρίες.", "The wrist is one of the most sensitive spots, so they say. In any case, I'd first think about whether I'll still like it in twenty years. Laser removal is expensive and takes many sessions."),
  L("Δανάη", "f", "Το χελιδόνι μου θυμίζει τη γιαγιά μου, που μου έλεγε ότι φέρνει την άνοιξη. Δεν νομίζω ότι θα το βαρεθώ. Θα έρθεις μαζί μου όμως; Μόνη μου θα το βάλω στα πόδια.", "The swallow reminds me of my grandmother, who used to tell me it brings the spring. I don't think I'll get tired of it. But will you come with me? On my own I'll run away."),
  L("Ζωή", "f", "Εντάξει, θα έρθω. Αλλά διάλεξε ένα στούντιο με άδεια και καλές κριτικές, όχι το πιο φτηνό.", "OK, I'll come. But choose a studio with a licence and good reviews, not the cheapest one."),
 ],
 "questions": [
  Q("Τι ανησυχεί περισσότερο τη Δανάη;", ["Τι θα πει η διευθύντριά της", "Αν θα πονέσει", "Πόσο θα κοστίσει", "Αν θα αρέσει στη Ζωή"], 1, "Εκείνο που με απασχολεί περισσότερο είναι αν θα πονέσει"),
  Q("Τι συμβουλεύει η Ζωή να σκεφτεί πρώτα;", ["Αν θα της αρέσει και σε είκοσι χρόνια", "Αν θα φαίνεται στις φωτογραφίες", "Αν θα το εγκρίνει η οικογένειά της", "Αν υπάρχει πιο μικρό σχέδιο"], 0, "αν θα μου αρέσει και σε είκοσι χρόνια"),
  Q("Γιατί διάλεξε η Δανάη ένα χελιδόνι;", ["Γιατί είναι της μόδας", "Γιατί είναι το σήμα της τράπεζας", "Γιατί της θυμίζει τη γιαγιά της", "Γιατί το πρότεινε η Ζωή"], 2, "Το χελιδόνι μου θυμίζει τη γιαγιά μου"),
 ],
 "gloss": {"τατουάζ": "τατουάζ — tattoo", "χελιδόνι": "χελιδόνι — swallow (bird)", "καρπό": "καρπός — wrist", "απασχολεί": "με απασχολεί — it concerns/worries me", "ευαίσθητα": "ευαίσθητος — sensitive", "αφαίρεση": "αφαίρεση — removal", "συνεδρίες": "συνεδρία — session", "βαρεθώ": "βαριέμαι — to get bored/tired of", "στα πόδια": "το βάζω στα πόδια — to run away, bolt", "κριτικές": "κριτική — review"}
})

ITEMS.append({
 "id": "l116-int-skinografos", "title": "Μια σκηνογράφος στο θέατρο", "title_en": "A set designer at the theatre", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια σκηνογράφο σε ραδιοφωνική εκπομπή για τον πολιτισμό.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί θεατές δεν ξέρουν τι ακριβώς κάνει ένας σκηνογράφος. Πώς θα το εξηγούσατε;", "Many theatregoers don't know exactly what a set designer does. How would you explain it?"),
  L("Σκηνογράφος", "f", "Σχεδιάζω τον χώρο όπου θα ζήσουν οι ήρωες για δύο ώρες. Μπορεί να είναι ένα σαλόνι, ένα πλοίο ή απλώς μια καρέκλα στο σκοτάδι. Δουλεύω μαζί με τον σκηνοθέτη από την αρχή, πολλούς μήνες πριν από την πρεμιέρα.", "I design the space where the characters will live for two hours. It could be a living room, a ship or simply a chair in the dark. I work with the director from the beginning, many months before the premiere."),
  L("Δημοσιογράφος", "m", "Από πού ξεκινάτε;", "Where do you start?"),
  L("Σκηνογράφος", "f", "Από το κείμενο, πάντα. Το διαβάζω πολλές φορές και μετά φτιάχνω μια μακέτα, ένα μικρό μοντέλο της σκηνής σε κλίμακα. Πάνω σε αυτή δοκιμάζουμε με τον σκηνοθέτη πού θα κινούνται οι ηθοποιοί.", "From the text, always. I read it many times and then make a maquette, a small scale model of the stage. On it, the director and I try out where the actors will move."),
  L("Δημοσιογράφος", "m", "Τι είναι το πιο δύσκολο;", "What is the hardest thing?"),
  L("Σκηνογράφος", "f", "Ο προϋπολογισμός. Συχνά έχω ιδέες για ένα παλάτι και χρήματα για ένα δωμάτιο. Έχω μάθει όμως ότι οι περιορισμοί σε κάνουν πιο εφευρετικό. Στην τελευταία μας παράσταση, η θάλασσα ήταν ένα τεράστιο κομμάτι μπλε ύφασμα που το κουνούσαν δύο τεχνικοί, και το κοινό ενθουσιάστηκε.", "The budget. I often have ideas for a palace and money for a room. But I've learned that limitations make you more inventive. In our last show, the sea was a huge piece of blue fabric that two technicians shook, and the audience loved it."),
 ],
 "questions": [
  Q("Πότε αρχίζει να δουλεύει η σκηνογράφος με τον σκηνοθέτη;", ["Λίγες μέρες πριν από την πρεμιέρα", "Πολλούς μήνες πριν από την πρεμιέρα", "Μετά τις πρώτες πρόβες", "Αφού επιλεγούν οι ηθοποιοί"], 1, "πολλούς μήνες πριν από την πρεμιέρα"),
  Q("Σε τι χρησιμεύει η μακέτα;", ["Για να δοκιμάσουν πού θα κινούνται οι ηθοποιοί", "Για να τη δείξουν στους χορηγούς", "Για να υπολογίσουν τα εισιτήρια", "Για να την εκθέσουν στο φουαγιέ"], 0, "δοκιμάζουμε με τον σκηνοθέτη πού θα κινούνται οι ηθοποιοί"),
  Q("Τι έχει μάθει η σκηνογράφος για τους περιορισμούς;", ["Ότι καταστρέφουν τις καλές ιδέες", "Ότι πρέπει να τους αποφεύγει", "Ότι την κάνουν πιο εφευρετική", "Ότι αφορούν μόνο τα μεγάλα θέατρα"], 2, "οι περιορισμοί σε κάνουν πιο εφευρετικό"),
 ],
 "gloss": {"σκηνογράφος": "σκηνογράφος — set designer", "σκηνοθέτη": "σκηνοθέτης — director", "πρεμιέρα": "πρεμιέρα — premiere, opening night", "μακέτα": "μακέτα — maquette, scale model", "κλίμακα": "κλίμακα — scale", "προϋπολογισμός": "προϋπολογισμός — budget", "περιορισμοί": "περιορισμός — limitation, constraint", "εφευρετικό": "εφευρετικός — inventive", "ύφασμα": "ύφασμα — fabric, cloth", "ενθουσιάστηκε": "ενθουσιάζομαι — to be thrilled"}
})

ITEMS.append({
 "id": "l116-rep-kafe-episkevon", "title": "Ένα καφέ επισκευών στη γειτονιά", "title_en": "A repair café in the neighbourhood", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Ρεπόρτερ", "f", "Κάθε δεύτερο Σάββατο του μήνα, το πνευματικό κέντρο της γειτονιάς γεμίζει τοστιέρες, φορέματα με σκισμένες ραφές και ραδιόφωνα που έχουν σωπάσει. Είναι το «καφέ επισκευών», όπου εθελοντές βοηθούν τους κατοίκους να φτιάξουν τα χαλασμένα αντικείμενά τους αντί να τα πετάξουν.", "Every second Saturday of the month, the neighbourhood cultural centre fills with toasters, dresses with torn seams and radios that have fallen silent. It's the \"repair café\", where volunteers help residents fix their broken things instead of throwing them away."),
  L("Ρεπόρτερ", "f", "Η ιδέα δεν είναι καινούργια· τα πρώτα τέτοια καφέ εμφανίστηκαν στην Ολλανδία το 2009. Εδώ, όμως, την έφερε ένας συνταξιούχος ηλεκτρολόγος, ο κύριος Μιλτιάδης, που, όπως λέει, δεν άντεχε να βλέπει συσκευές στα σκουπίδια για ένα καμένο καλώδιο.", "The idea isn't new; the first such cafés appeared in the Netherlands in 2009. Here, though, it was brought by a retired electrician, Mr Miltiadis, who, as he says, couldn't bear to see appliances in the rubbish because of one burnt-out wire."),
  L("Ρεπόρτερ", "f", "Οι επισκευές είναι δωρεάν, αλλά υπάρχει ένας κανόνας: ο ιδιοκτήτης κάθεται δίπλα στον εθελοντή και μαθαίνει. Οι διοργανωτές υπολογίζουν ότι περίπου επτά στα δέκα αντικείμενα φεύγουν από εδώ λειτουργώντας ξανά.", "The repairs are free, but there is one rule: the owner sits next to the volunteer and learns. The organisers estimate that about seven out of ten items leave here working again."),
 ],
 "questions": [
  Q("Ποιος έφερε την ιδέα στη γειτονιά;", ["Ένας δάσκαλος", "Ένας συνταξιούχος ηλεκτρολόγος", "Μια Ολλανδή φοιτήτρια", "Ο δήμαρχος"], 1, "την έφερε ένας συνταξιούχος ηλεκτρολόγος"),
  Q("Ποιος είναι ο κανόνας του καφέ επισκευών;", ["Ο ιδιοκτήτης πληρώνει τα ανταλλακτικά", "Δεν επισκευάζονται ηλεκτρικές συσκευές", "Ο ιδιοκτήτης κάθεται δίπλα στον εθελοντή και μαθαίνει", "Κάθε κάτοικος φέρνει μόνο ένα αντικείμενο"], 2, "ο ιδιοκτήτης κάθεται δίπλα στον εθελοντή και μαθαίνει"),
  Q("Πόσα αντικείμενα φεύγουν λειτουργώντας ξανά, σύμφωνα με τους διοργανωτές;", ["Περίπου τα μισά", "Σχεδόν όλα", "Περίπου τρία στα δέκα", "Περίπου επτά στα δέκα"], 3, "περίπου επτά στα δέκα αντικείμενα φεύγουν από εδώ λειτουργώντας ξανά"),
 ],
 "gloss": {"πνευματικό κέντρο": "πνευματικό κέντρο — cultural centre", "τοστιέρες": "τοστιέρα — sandwich toaster", "ραφές": "ραφή — seam", "σωπάσει": "σωπαίνω — to fall silent", "επισκευών": "επισκευή — repair", "εθελοντές": "εθελοντής — volunteer", "συνταξιούχος": "συνταξιούχος — retired person, pensioner", "ηλεκτρολόγος": "ηλεκτρολόγος — electrician", "καλώδιο": "καλώδιο — wire, cable", "διοργανωτές": "διοργανωτής — organiser"}
})

ITEMS.append({
 "id": "l116-rep-skoteinos-ouranos", "title": "Ένα χωριό που θέλει να κρατήσει τον ουρανό σκοτεινό", "title_en": "A village that wants to keep its sky dark", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις ειδήσεις ενός περιφερειακού σταθμού.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε ένα ορεινό χωριό της περιοχής μας, οι κάτοικοι αποφάσισαν να αλλάξουν τα φώτα του δρόμου. Οι παλιές λάμπες, που έριχναν φως προς κάθε κατεύθυνση, αντικαθίστανται με φωτιστικά που φωτίζουν μόνο προς τα κάτω και έχουν πιο ζεστό, κιτρινωπό χρώμα.", "In a mountain village in our area, the residents have decided to change the street lights. The old lamps, which threw light in every direction, are being replaced with fittings that light only downwards and have a warmer, yellowish colour."),
  L("Ρεπόρτερ", "m", "Ο στόχος είναι να μειωθεί η φωτορρύπανση και να φαίνεται ξανά ο Γαλαξίας. Η πρόεδρος της κοινότητας ελπίζει ότι ο καθαρός ουρανός θα φέρει επισκέπτες εκτός τουριστικής περιόδου: ερασιτέχνες αστρονόμους, φωτογράφους, σχολεία.", "The aim is to reduce light pollution so that the Milky Way can be seen again. The community president hopes that the clear sky will bring visitors outside the tourist season: amateur astronomers, photographers, schools."),
  L("Ρεπόρτερ", "m", "Δεν συμφωνούν όλοι. Κάποιοι ηλικιωμένοι κάτοικοι φοβούνται ότι οι δρόμοι θα είναι λιγότερο ασφαλείς τη νύχτα. Η κοινότητα απαντά ότι ο φωτισμός δεν θα μειωθεί στα σκαλιά και στις διασταυρώσεις, και ότι οι νέοι λαμπτήρες θα μειώσουν επιπλέον τον λογαριασμό του ρεύματος.", "Not everyone agrees. Some elderly residents fear that the streets will be less safe at night. The community replies that lighting will not be reduced on steps and at junctions, and that the new bulbs will also cut the electricity bill."),
 ],
 "questions": [
  Q("Πώς διαφέρουν τα νέα φωτιστικά από τα παλιά;", ["Είναι πιο φωτεινά", "Φωτίζουν μόνο προς τα κάτω", "Ανάβουν μόνο τα Σαββατοκύριακα", "Έχουν λευκό, ψυχρό φως"], 1, "φωτίζουν μόνο προς τα κάτω"),
  Q("Ποιους επισκέπτες ελπίζει να προσελκύσει η κοινότητα;", ["Ερασιτέχνες αστρονόμους, φωτογράφους και σχολεία", "Ορειβάτες και σκιέρ", "Ταξιδιώτες κρουαζιέρας", "Επιχειρηματίες"], 0, "ερασιτέχνες αστρονόμους, φωτογράφους, σχολεία"),
  Q("Τι απαντά η κοινότητα στους ηλικιωμένους που ανησυχούν;", ["Ότι θα τοποθετηθούν κάμερες", "Ότι τα φώτα θα σβήνουν μετά τα μεσάνυχτα", "Ότι ο φωτισμός δεν θα μειωθεί στα σκαλιά και στις διασταυρώσεις", "Ότι το σχέδιο είναι προσωρινό"], 2, "ο φωτισμός δεν θα μειωθεί στα σκαλιά και στις διασταυρώσεις"),
 ],
 "gloss": {"κατεύθυνση": "κατεύθυνση — direction", "αντικαθίστανται": "αντικαθίσταμαι — to be replaced", "φωτιστικά": "φωτιστικό — light fitting, lamp", "κιτρινωπό": "κιτρινωπός — yellowish", "φωτορρύπανση": "φωτορρύπανση — light pollution", "Γαλαξίας": "Γαλαξίας — the Milky Way", "κοινότητας": "κοινότητα — (village) community", "ερασιτέχνες": "ερασιτέχνης — amateur", "διασταυρώσεις": "διασταύρωση — junction, crossroads", "λαμπτήρες": "λαμπτήρας — light bulb"}
})

ITEMS.append({
 "id": "l116-mon-portofoli-romi", "title": "Η μέρα που έχασα το πορτοφόλι μου στη Ρώμη", "title_en": "The day I lost my wallet in Rome", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να διηγείται μια ιστορία από ένα ταξίδι του σε εκπομπή με ιστορίες ακροατών.",
 "script": [
  L("Ακροατής", "m", "Ήταν η δεύτερη μέρα μας στη Ρώμη. Είχαμε μπει σε ένα γεμάτο λεωφορείο για το Βατικανό, και όταν κατεβήκαμε, έβαλα το χέρι στην τσέπη και πάγωσα: το πορτοφόλι είχε εξαφανιστεί. Μέσα είχα μετρητά, δύο κάρτες και, το χειρότερο, την ταυτότητά μου.", "It was our second day in Rome. We had got on a crowded bus to the Vatican, and when we got off, I put my hand in my pocket and froze: the wallet had vanished. Inside I had cash, two cards and, worst of all, my ID card."),
  L("Ακροατής", "m", "Το πρώτο που έκανα ήταν να μπλοκάρω τις κάρτες από το κινητό. Μετά πήγαμε στο αστυνομικό τμήμα για να κάνουμε δήλωση κλοπής, γιατί χωρίς αυτήν δεν θα μπορούσα να πάρω προσωρινό ταξιδιωτικό έγγραφο από το προξενείο. Περιμέναμε τρεις ώρες, αλλά ο αστυνομικός ήταν ευγενέστατος.", "The first thing I did was block the cards from my phone. Then we went to the police station to report the theft, because without that report I couldn't get a temporary travel document from the consulate. We waited three hours, but the police officer was extremely polite."),
  L("Ακροατής", "m", "Και το απίστευτο: δύο μέρες αργότερα μου τηλεφώνησαν από το ξενοδοχείο. Κάποιος είχε βρει το πορτοφόλι σε έναν κάδο και το είχε φέρει, επειδή μέσα υπήρχε η κάρτα του ξενοδοχείου. Τα χρήματα έλειπαν, αλλά η ταυτότητα ήταν εκεί. Από τότε, κρατάω πάντα φωτοτυπίες των εγγράφων μου σε άλλη τσέπη.", "And the incredible part: two days later the hotel phoned me. Someone had found the wallet in a bin and brought it, because the hotel's card was inside. The money was missing, but the ID was there. Since then, I always keep photocopies of my documents in another pocket."),
 ],
 "questions": [
  Q("Τι έκανε πρώτα ο αφηγητής όταν κατάλαβε την κλοπή;", ["Πήγε στο προξενείο", "Μπλόκαρε τις κάρτες από το κινητό", "Γύρισε στο λεωφορείο", "Τηλεφώνησε στο ξενοδοχείο"], 1, "Το πρώτο που έκανα ήταν να μπλοκάρω τις κάρτες από το κινητό"),
  Q("Γιατί χρειαζόταν τη δήλωση κλοπής;", ["Για να πάρει πίσω τα χρήματα από την ασφάλεια", "Για να αλλάξει ξενοδοχείο", "Για να πάρει προσωρινό ταξιδιωτικό έγγραφο από το προξενείο", "Για να μπορεί να μπει στο Βατικανό"], 2, "χωρίς αυτήν δεν θα μπορούσα να πάρω προσωρινό ταξιδιωτικό έγγραφο από το προξενείο"),
  Q("Γιατί έφεραν το πορτοφόλι στο ξενοδοχείο;", ["Επειδή μέσα υπήρχε η κάρτα του ξενοδοχείου", "Επειδή το ξενοδοχείο είχε δώσει αμοιβή", "Επειδή το βρήκε ένας υπάλληλος του ξενοδοχείου", "Επειδή η αστυνομία το έστειλε εκεί"], 0, "επειδή μέσα υπήρχε η κάρτα του ξενοδοχείου"),
 ],
 "gloss": {"πορτοφόλι": "πορτοφόλι — wallet", "πάγωσα": "παγώνω — to freeze (with shock)", "μετρητά": "μετρητά — cash", "ταυτότητά": "ταυτότητα — identity card", "μπλοκάρω": "μπλοκάρω — to block", "δήλωση κλοπής": "δήλωση κλοπής — theft report", "προξενείο": "προξενείο — consulate", "ευγενέστατος": "ευγενέστατος — extremely polite", "κάδο": "κάδος — (rubbish) bin", "φωτοτυπίες": "φωτοτυπία — photocopy"}
})

ITEMS.append({
 "id": "l116-mon-daskala-oreino", "title": "Η πρώτη μου χρονιά σε ένα ορεινό σχολείο", "title_en": "My first year at a mountain school", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νέα δασκάλα να μιλά για την πρώτη της χρονιά σε εκπομπή για την εκπαίδευση.",
 "script": [
  L("Δασκάλα", "f", "Όταν πήρα τον διορισμό μου, έψαξα το χωριό στον χάρτη και δεν το βρήκα αμέσως. Ήταν ένα μονοθέσιο σχολείο στα βουνά της Ηπείρου, με εννιά μαθητές από την πρώτη ως την έκτη τάξη, όλοι στην ίδια αίθουσα.", "When I got my appointment, I looked for the village on the map and didn't find it straight away. It was a one-teacher school in the mountains of Epirus, with nine pupils from first to sixth grade, all in the same classroom."),
  L("Δασκάλα", "f", "Στην αρχή πανικοβλήθηκα. Πώς διδάσκεις κλάσματα στον έναν και την αλφαβήτα στον άλλον την ίδια ώρα; Γρήγορα όμως κατάλαβα ότι τα μεγαλύτερα παιδιά ήταν οι καλύτεροί μου βοηθοί. Όταν εξηγούσαν κάτι στα μικρά, το μάθαιναν και τα ίδια καλύτερα.", "At first I panicked. How do you teach fractions to one child and the alphabet to another at the same time? But I soon realised that the older children were my best helpers. When they explained something to the little ones, they learned it better themselves."),
  L("Δασκάλα", "f", "Τον χειμώνα, όταν χιόνιζε, ο δρόμος έκλεινε και μέναμε μέρες αποκλεισμένοι. Τότε οι γονείς μού έφερναν φαγητό και ξύλα για τη σόμπα. Στο τέλος της χρονιάς, όταν έφυγα, έκλαιγα περισσότερο από τα παιδιά. Ζήτησα να μείνω και δεύτερη χρονιά.", "In winter, when it snowed, the road closed and we were cut off for days. Then the parents would bring me food and wood for the stove. At the end of the year, when I left, I cried more than the children. I asked to stay a second year."),
 ],
 "questions": [
  Q("Πώς ήταν οργανωμένο το σχολείο;", ["Είχε έξι αίθουσες", "Όλοι οι μαθητές ήταν στην ίδια αίθουσα", "Λειτουργούσε μόνο το πρωί του Σαββάτου", "Είχε δύο δασκάλους"], 1, "όλοι στην ίδια αίθουσα"),
  Q("Τι κατάλαβε γρήγορα η δασκάλα;", ["Ότι τα μεγαλύτερα παιδιά ήταν οι καλύτεροί της βοηθοί", "Ότι έπρεπε να χωρίσει τους μαθητές", "Ότι τα μικρά παιδιά δεν μάθαιναν τίποτα", "Ότι οι γονείς δεν ενδιαφέρονταν"], 0, "τα μεγαλύτερα παιδιά ήταν οι καλύτεροί μου βοηθοί"),
  Q("Τι έκανε η δασκάλα στο τέλος της χρονιάς;", ["Ζήτησε μετάθεση στην πόλη", "Έγραψε ένα βιβλίο", "Ζήτησε να μείνει και δεύτερη χρονιά", "Οργάνωσε μια γιορτή στο χωριό"], 2, "Ζήτησα να μείνω και δεύτερη χρονιά"),
 ],
 "gloss": {"διορισμό": "διορισμός — (job) appointment", "μονοθέσιο": "μονοθέσιο σχολείο — one-teacher school", "αίθουσα": "αίθουσα — classroom, hall", "πανικοβλήθηκα": "πανικοβάλλομαι — to panic", "κλάσματα": "κλάσμα — fraction", "αλφαβήτα": "αλφαβήτα — alphabet", "βοηθοί": "βοηθός — helper, assistant", "αποκλεισμένοι": "αποκλεισμένος — cut off, snowed in", "ξύλα": "ξύλα — firewood", "σόμπα": "σόμπα — stove, heater"}
})

ITEMS.append({
 "id": "l116-c1-lypitera-tragoudia", "title": "Γιατί μας αρέσουν τα λυπητερά τραγούδια;", "title_en": "Why do we like sad songs?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια μουσικολόγο σε μια διάλεξη για τη μουσική και τα συναισθήματα.",
 "script": [
  L("Μουσικολόγος", "f", "Αν η μουσική υπάρχει για να μας ευχαριστεί, γιατί επιλέγουμε τόσο συχνά να ακούμε τραγούδια που μας κάνουν να δακρύζουμε; Από τους αμανέδες ως τις μπαλάντες της ποπ, η θλίψη είναι ίσως το πιο σταθερό θέμα της μουσικής. Οι ψυχολόγοι μιλούν για το «παράδοξο της τραγικής απόλαυσης».", "If music exists to give us pleasure, why do we so often choose to listen to songs that make us tear up? From amanedes to pop ballads, sadness is perhaps music's most constant theme. Psychologists speak of the \"paradox of tragic pleasure\"."),
  L("Μουσικολόγος", "f", "Μια πρώτη εξήγηση είναι ότι η θλίψη της μουσικής είναι, ας πούμε, θλίψη χωρίς κόστος. Δεν έχουμε χάσει πραγματικά κάποιον· ζούμε το συναίσθημα από ασφαλή απόσταση. Σε έρευνες, πολλοί ακροατές περιγράφουν όχι σκέτη λύπη αλλά ένα μείγμα: νοσταλγία, τρυφερότητα, ακόμη και γαλήνη.", "A first explanation is that the sadness of music is, so to speak, sadness without cost. We haven't really lost anyone; we experience the emotion from a safe distance. In studies, many listeners describe not plain sorrow but a mixture: nostalgia, tenderness, even serenity."),
  L("Μουσικολόγος", "f", "Έχει διατυπωθεί και μια βιολογική υπόθεση: ότι η θλίψη ενεργοποιεί ορμόνες που κανονικά μας παρηγορούν μετά από μια απώλεια, και ότι η μουσική μάς χαρίζει την παρηγοριά χωρίς την απώλεια. Πρέπει όμως να τονίσω ότι αυτό δεν έχει αποδειχθεί.", "A biological hypothesis has also been put forward: that sadness activates hormones that normally comfort us after a loss, and that music gives us the comfort without the loss. But I must stress that this has not been proven."),
  L("Μουσικολόγος", "f", "Υπάρχει, τέλος, και η κοινωνική διάσταση. Όταν είμαστε στενοχωρημένοι, ένα λυπητερό τραγούδι λειτουργεί σαν ένας φίλος που καταλαβαίνει. Δεν μας λέει «χαμογέλα», μας λέει «σε καταλαβαίνω». Ίσως γι’ αυτό, σε τέτοιες στιγμές, ένα χαρούμενο τραγούδι μάς φαίνεται σχεδόν προσβλητικό.", "Finally, there is also the social dimension. When we are upset, a sad song works like a friend who understands. It doesn't tell us \"smile\", it tells us \"I understand you\". Perhaps that is why, at such moments, a cheerful song seems almost offensive to us."),
 ],
 "questions": [
  Q("Τι εννοεί η ομιλήτρια λέγοντας ότι η θλίψη της μουσικής είναι «χωρίς κόστος»;", ["Ότι η μουσική είναι δωρεάν", "Ότι ζούμε το συναίσθημα από ασφαλή απόσταση, χωρίς πραγματική απώλεια", "Ότι τα λυπητερά τραγούδια πουλάνε λιγότερο", "Ότι η θλίψη δεν διαρκεί πολύ"], 1, "ζούμε το συναίσθημα από ασφαλή απόσταση"),
  Q("Τι περιγράφουν πολλοί ακροατές σε έρευνες;", ["Μόνο βαθιά λύπη", "Θυμό και ενόχληση", "Ένα μείγμα από νοσταλγία, τρυφερότητα και γαλήνη", "Αδιαφορία"], 2, "νοσταλγία, τρυφερότητα, ακόμη και γαλήνη"),
  Q("Πώς παρουσιάζει η ομιλήτρια τη βιολογική υπόθεση;", ["Ως αποδεδειγμένο γεγονός", "Ως κάτι που έχει απορριφθεί", "Ως τη μόνη σωστή εξήγηση", "Ως υπόθεση που δεν έχει αποδειχθεί"], 3, "αυτό δεν έχει αποδειχθεί"),
  Q("Γιατί, σύμφωνα με την ομιλήτρια, ένα χαρούμενο τραγούδι μπορεί να μας ενοχλεί όταν είμαστε στενοχωρημένοι;", ["Γιατί μοιάζει να μας λέει «χαμογέλα» αντί για «σε καταλαβαίνω»", "Γιατί είναι συνήθως πιο δυνατό", "Γιατί μας θυμίζει τη δουλειά", "Γιατί έχει πολύ γρήγορο ρυθμό"], 0, "Δεν μας λέει «χαμογέλα», μας λέει «σε καταλαβαίνω»"),
 ],
 "gloss": {"δακρύζουμε": "δακρύζω — to tear up", "αμανέδες": "αμανές — amanes (improvised lament-like song)", "θλίψη": "θλίψη — sadness, grief", "παράδοξο": "παράδοξο — paradox", "απόλαυσης": "απόλαυση — enjoyment, pleasure", "τρυφερότητα": "τρυφερότητα — tenderness", "γαλήνη": "γαλήνη — serenity, calm", "διατυπωθεί": "διατυπώνω — to formulate, put forward", "παρηγορούν": "παρηγορώ — to comfort, console", "απώλεια": "απώλεια — loss", "διάσταση": "διάσταση — dimension", "προσβλητικό": "προσβλητικός — offensive"}
})

ITEMS.append({
 "id": "l116-c1-kryfo-scholeio", "title": "Το Κρυφό Σχολειό: ανάμεσα στον μύθο και την ιστορία", "title_en": "The Secret School: between myth and history", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια ιστορικό σε εκπομπή για την ελληνική ιστορία.",
 "script": [
  L("Δημοσιογράφος", "m", "Όλοι μάθαμε στο σχολείο για το Κρυφό Σχολειό: παιδιά που μάθαιναν γράμματα τη νύχτα, σε εκκλησίες, κρυφά από τους Οθωμανούς. Τι λένε σήμερα οι ιστορικοί;", "We all learned at school about the Secret School: children learning to read at night, in churches, hidden from the Ottomans. What do historians say today?"),
  L("Ιστορικός", "f", "Οι περισσότεροι ιστορικοί που έχουν μελετήσει το θέμα δεν έχουν βρει τεκμήρια ότι υπήρχε γενική απαγόρευση της ελληνικής εκπαίδευσης από τις οθωμανικές αρχές. Αντίθετα, γνωρίζουμε ότι λειτουργούσαν φανερά σχολεία, συχνά με τη στήριξη της Εκκλησίας και πλούσιων ομογενών, ιδίως τον δέκατο όγδοο αιώνα.", "Most historians who have studied the subject have not found evidence of a general ban on Greek education by the Ottoman authorities. On the contrary, we know that schools operated openly, often with the support of the Church and wealthy diaspora Greeks, especially in the eighteenth century."),
  L("Δημοσιογράφος", "m", "Από πού προέρχεται λοιπόν η εικόνα που όλοι έχουμε στο μυαλό μας;", "So where does the image we all have in our minds come from?"),
  L("Ιστορικός", "f", "Σε μεγάλο βαθμό διαμορφώθηκε τον δέκατο ένατο αιώνα, μετά την Επανάσταση, όταν το νέο κράτος αναζητούσε σύμβολα. Ένα γνωστό τραγουδάκι, το «Φεγγαράκι μου λαμπρό», και κυρίως ο γνωστός πίνακας του Νικολάου Γύζη, ζωγραφισμένος το 1885 περίπου, έδωσαν στον θρύλο μια εικόνα που όλοι αναγνωρίζουμε.", "To a large extent it took shape in the nineteenth century, after the Revolution, when the new state was looking for symbols. A well-known little song, \"Fengaraki mou lambro\", and above all the famous painting by Nikolaos Gyzis, painted around 1885, gave the legend an image we all recognise."),
  L("Δημοσιογράφος", "m", "Δηλαδή πρόκειται απλώς για ψέμα;", "So is it simply a lie?"),
  L("Ιστορικός", "f", "Θα ήμουν προσεκτική με αυτή τη λέξη. Σε ορισμένες περιοχές και περιόδους, η μόρφωση ήταν πράγματι δύσκολη, φτωχή, και γινόταν συχνά από ιερείς, στα κελιά και στους νάρθηκες. Ο μύθος δεν περιγράφει πιστά τα γεγονότα, εκφράζει όμως κάτι αληθινό για τη συλλογική μνήμη: την ανάγκη ενός λαού να πιστεύει ότι κράτησε τη γλώσσα του ζωντανή μέσα στις δυσκολίες. Η δουλειά του ιστορικού δεν είναι να γκρεμίζει τους μύθους, αλλά να εξηγεί πώς γεννήθηκαν.", "I'd be careful with that word. In certain areas and periods, education was indeed difficult and poor, and was often given by priests, in cells and in church narthexes. The myth does not faithfully describe events, but it expresses something true about collective memory: a people's need to believe that it kept its language alive through hardship. The historian's job is not to tear down myths, but to explain how they were born."),
 ],
 "questions": [
  Q("Τι δεν έχουν βρει οι περισσότεροι ιστορικοί, σύμφωνα με την ομιλήτρια;", ["Σχολικά βιβλία της εποχής", "Τεκμήρια για γενική απαγόρευση της ελληνικής εκπαίδευσης", "Ονόματα δασκάλων", "Εκκλησίες της περιόδου"], 1, "δεν έχουν βρει τεκμήρια ότι υπήρχε γενική απαγόρευση της ελληνικής εκπαίδευσης"),
  Q("Πότε διαμορφώθηκε κυρίως η εικόνα του Κρυφού Σχολειού;", ["Τον δέκατο ένατο αιώνα, μετά την Επανάσταση", "Στα βυζαντινά χρόνια", "Τον εικοστό αιώνα, με τον κινηματογράφο", "Τον δέκατο έκτο αιώνα"], 0, "τον δέκατο ένατο αιώνα, μετά την Επανάσταση"),
  Q("Γιατί είναι προσεκτική η ιστορικός με τη λέξη «ψέμα»;", ["Γιατί ο μύθος είναι απολύτως ακριβής", "Γιατί δεν θέλει να δυσαρεστήσει το κοινό", "Γιατί η μόρφωση ήταν πράγματι δύσκολη σε ορισμένες περιοχές και ο μύθος εκφράζει κάτι αληθινό για τη συλλογική μνήμη", "Γιατί δεν έχει μελετήσει αρκετά το θέμα"], 2, "εκφράζει όμως κάτι αληθινό για τη συλλογική μνήμη"),
  Q("Ποια είναι, κατά την ομιλήτρια, η δουλειά του ιστορικού;", ["Να γκρεμίζει τους μύθους", "Να γράφει σχολικά βιβλία", "Να προστατεύει τα εθνικά σύμβολα", "Να εξηγεί πώς γεννήθηκαν οι μύθοι"], 3, "να εξηγεί πώς γεννήθηκαν"),
 ],
 "gloss": {"Κρυφό Σχολειό": "Κρυφό Σχολειό — the 'Secret School' (legend of the Ottoman period)", "τεκμήρια": "τεκμήριο — evidence, proof", "απαγόρευση": "απαγόρευση — ban, prohibition", "φανερά": "φανερά — openly", "ομογενών": "ομογενής — Greek of the diaspora", "διαμορφώθηκε": "διαμορφώνομαι — to take shape", "θρύλο": "θρύλος — legend", "μόρφωση": "μόρφωση — education", "κελιά": "κελί — (monk's) cell", "νάρθηκες": "νάρθηκας — narthex (church porch)", "συλλογική μνήμη": "συλλογική μνήμη — collective memory", "γκρεμίζει": "γκρεμίζω — to tear down, demolish"}
})

rnd = random.Random(116)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-116.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
