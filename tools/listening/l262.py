# Source for library/listening/listening-262.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l262.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l262-news-epistrefomena-potiria", "title": "Επιστρεφόμενα ποτήρια για τον καφέ σε καφετέριες της Πάτρας", "title_en": "Returnable cups for takeaway coffee in cafés in Patras", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο μεσημεριανό δελτίο ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Από τη Δευτέρα πενήντα καφετέριες της Πάτρας συμμετέχουν σε ένα πρόγραμμα με επιστρεφόμενα ποτήρια για τον καφέ σε πακέτο. Ο πελάτης πληρώνει ένα ευρώ εγγύηση για το ποτήρι και το παίρνει πίσω όταν το επιστρέψει, σε οποιαδήποτε από τις καφετέριες του προγράμματος.", "From Monday fifty cafés in Patras are taking part in a scheme with returnable cups for takeaway coffee. The customer pays a one-euro deposit for the cup and gets it back on returning it to any of the cafés in the scheme."),
  L("Εκφωνητής", "m", "Τα ποτήρια είναι από ανθεκτικό πλαστικό, που αντέχει, σύμφωνα με τον κατασκευαστή, πάνω από πεντακόσια πλυσίματα. Οι καφετέριες τα πλένουν σε επαγγελματικά πλυντήρια, και μια ειδική ετικέτα στην πόρτα τους δείχνει ότι συμμετέχουν στο πρόγραμμα.", "The cups are made of durable plastic which, according to the manufacturer, withstands more than five hundred washes. The cafés wash them in commercial dishwashers, and a special sticker on their door shows that they are part of the scheme."),
  L("Εκφωνητής", "m", "Η πρωτοβουλία ξεκίνησε από μια ομάδα φοιτητών του πανεπιστημίου, που υπολόγισαν ότι στην πόλη πετιούνται κάθε μέρα δεκάδες χιλιάδες ποτήρια μιας χρήσης. Τα περισσότερα έχουν εσωτερική επένδυση από πλαστικό, γι’ αυτό δεν ανακυκλώνονται εύκολα μαζί με το χαρτί.", "The initiative was started by a group of university students, who calculated that tens of thousands of single-use cups are thrown away in the city every day. Most have a plastic inner lining, which is why they are not easily recycled with paper."),
  L("Εκφωνητής", "m", "Ορισμένοι ιδιοκτήτες καφετεριών εκφράζουν επιφυλάξεις για τον χώρο και τον χρόνο που απαιτεί το πλύσιμο. Οι διοργανωτές απαντούν ότι, αν το πρόγραμμα πετύχει, ο δήμος θα εξετάσει την τοποθέτηση αυτόματων μηχανημάτων επιστροφής σε κεντρικά σημεία της πόλης.", "Some café owners have reservations about the space and time the washing requires. The organisers reply that, if the scheme succeeds, the municipality will consider installing automatic return machines at central points in the city."),
 ],
 "questions": [
  Q("Πώς λειτουργεί το πρόγραμμα;", ["Ο καφές είναι φθηνότερος με δικό σου ποτήρι", "Πληρώνεις εγγύηση ένα ευρώ και την παίρνεις πίσω όταν επιστρέψεις το ποτήρι", "Τα ποτήρια πουλιούνται στα σούπερ μάρκετ", "Ο δήμος μοιράζει δωρεάν ποτήρια"], 1, "Ο πελάτης πληρώνει ένα ευρώ εγγύηση … και το παίρνει πίσω όταν το επιστρέψει"),
  Q("Πόσα πλυσίματα αντέχουν τα ποτήρια σύμφωνα με τον κατασκευαστή;", ["Περίπου πενήντα", "Περίπου εκατό", "Πάνω από πεντακόσια", "Απεριόριστα"], 2, "αντέχει … πάνω από πεντακόσια πλυσίματα"),
  Q("Γιατί δεν ανακυκλώνονται εύκολα τα ποτήρια μιας χρήσης;", ["Γιατί είναι λερωμένα με καφέ", "Γιατί έχουν εσωτερική επένδυση από πλαστικό", "Γιατί δεν υπάρχουν κάδοι στην πόλη", "Γιατί είναι πολύ μικρά"], 1, "Τα περισσότερα έχουν εσωτερική επένδυση από πλαστικό"),
  Q("Τι θα εξετάσει ο δήμος αν το πρόγραμμα πετύχει;", ["Να απαγορεύσει τα ποτήρια μιας χρήσης", "Να τοποθετήσει αυτόματα μηχανήματα επιστροφής", "Να μειώσει τους φόρους των καφετεριών", "Να επεκτείνει το πρόγραμμα στα σχολεία"], 1, "θα εξετάσει την τοποθέτηση αυτόματων μηχανημάτων επιστροφής"),
 ],
 "gloss": {"επιστρεφόμενα": "επιστρεφόμενος — returnable", "εγγύηση": "εγγύηση — deposit; guarantee", "ανθεκτικό": "ανθεκτικός — durable", "κατασκευαστή": "κατασκευαστής — manufacturer", "πλυσίματα": "πλύσιμο — wash(ing)", "ετικέτα": "ετικέτα — label, sticker", "πρωτοβουλία": "πρωτοβουλία — initiative", "μιας χρήσης": "μιας χρήσης — single-use", "επένδυση": "επένδυση — lining; investment", "επιφυλάξεις": "επιφύλαξη — reservation, doubt", "διοργανωτές": "διοργανωτής — organiser"}
})

ITEMS.append({
 "id": "l262-vm-eforeftiki-epitropi", "title": "Μήνυμα από τον δήμο: κληρωθήκατε μέλος εφορευτικής επιτροπής", "title_en": "A message from the town hall: you have been drawn to serve on a polling-station committee", "type": "voicemail", "level": "B2",
 "context_el": "Λίγες εβδομάδες πριν από τις εκλογές, ακούτε ένα μήνυμα που σας άφησε μια υπάλληλος του δήμου σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, από το Τμήμα Δημοτικής Κατάστασης του δήμου. Σας ενημερώνουμε ότι στην κλήρωση της περασμένης εβδομάδας κληρωθήκατε τακτικό μέλος της εφορευτικής επιτροπής στο εκλογικό τμήμα δεκαεπτά, που βρίσκεται στο τρίτο δημοτικό σχολείο.", "Good morning, this is the civil registry department of the town hall. We are informing you that in last week's draw you were selected as a full member of the polling-station committee at polling station seventeen, which is at the Third Primary School."),
  L("Υπάλληλος", "f", "Την ημέρα των εκλογών θα πρέπει να βρίσκεστε στο σχολείο στις έξι το πρωί, μία ώρα πριν ανοίξουν οι κάλπες. Η δουλειά τελειώνει όταν ολοκληρωθεί η καταμέτρηση των ψήφων, κάτι που συνήθως γίνεται αργά το βράδυ, οπότε φροντίστε να έχετε ξεκουραστεί.", "On election day you will need to be at the school at six in the morning, one hour before the polls open. The work ends when the counting of the votes is complete, which usually happens late in the evening, so make sure you have rested well."),
  L("Υπάλληλος", "f", "Για τη συμμετοχή σας προβλέπεται αποζημίωση, που θα καταβληθεί στον τραπεζικό σας λογαριασμό μέσα σε λίγους μήνες. Θα χρειαστεί λοιπόν να μας στείλετε το ΙΒΑΝ σας με ηλεκτρονικό ταχυδρομείο, μαζί με ένα αντίγραφο της ταυτότητάς σας.", "Compensation is provided for your participation and will be paid into your bank account within a few months. So you will need to email us your IBAN, together with a copy of your identity card."),
  L("Υπάλληλος", "f", "Αν υπάρχει σοβαρός λόγος που δεν μπορείτε να συμμετάσχετε, για παράδειγμα λόγος υγείας, πρέπει να το δηλώσετε εγγράφως, με τα σχετικά δικαιολογητικά, το αργότερο μέσα σε πέντε ημέρες. Για οποιαδήποτε απορία, το τηλέφωνό μας είναι στην πρόσκληση που θα λάβετε ταχυδρομικά. Ευχαριστούμε.", "If there is a serious reason why you cannot take part, for example a health reason, you must declare it in writing, with the relevant supporting documents, within five days at the latest. For any questions, our phone number is on the notice you will receive by post. Thank you."),
 ],
 "questions": [
  Q("Πού θα πρέπει να βρίσκεστε την ημέρα των εκλογών;", ["Στο δημαρχείο", "Στο τρίτο δημοτικό σχολείο", "Στο εκλογικό σας τμήμα στο χωριό", "Στο γυμνάσιο"], 1, "στο εκλογικό τμήμα δεκαεπτά, που βρίσκεται στο τρίτο δημοτικό σχολείο"),
  Q("Πότε τελειώνει η δουλειά;", ["Στις επτά το απόγευμα", "Το μεσημέρι", "Όταν ολοκληρωθεί η καταμέτρηση των ψήφων", "Την επόμενη μέρα το πρωί"], 2, "Η δουλειά τελειώνει όταν ολοκληρωθεί η καταμέτρηση των ψήφων"),
  Q("Τι πρέπει να στείλετε στον δήμο;", ["Το ΙΒΑΝ σας και αντίγραφο της ταυτότητας", "Μια φωτογραφία", "Το εκλογικό σας βιβλιάριο", "Ένα πιστοποιητικό υγείας"], 0, "να μας στείλετε το ΙΒΑΝ σας … μαζί με ένα αντίγραφο της ταυτότητάς σας"),
  Q("Τι πρέπει να κάνετε αν δεν μπορείτε να συμμετάσχετε;", ["Να τηλεφωνήσετε την ημέρα των εκλογών", "Να στείλετε κάποιον στη θέση σας", "Να το δηλώσετε εγγράφως με δικαιολογητικά μέσα σε πέντε ημέρες", "Να πληρώσετε πρόστιμο"], 2, "πρέπει να το δηλώσετε εγγράφως, με τα σχετικά δικαιολογητικά, το αργότερο μέσα σε πέντε ημέρες"),
 ],
 "gloss": {"Δημοτικής Κατάστασης": "δημοτική κατάσταση — civil (municipal) registry", "κλήρωση": "κλήρωση — draw (by lot)", "κληρωθήκατε": "κληρώνομαι — to be drawn by lot", "εφορευτικής επιτροπής": "εφορευτική επιτροπή — polling-station committee", "εκλογικό τμήμα": "εκλογικό τμήμα — polling station", "κάλπες": "κάλπη — ballot box", "καταμέτρηση": "καταμέτρηση — count(ing)", "αποζημίωση": "αποζημίωση — compensation", "καταβληθεί": "καταβάλλω — to pay", "εγγράφως": "εγγράφως — in writing", "δικαιολογητικά": "δικαιολογητικά — supporting documents"}
})

ITEMS.append({
 "id": "l262-c1-mono-roloi-cheiros", "title": "Από το βραχιόλι της βασίλισσας στα χαρακώματα: η ιστορία του ρολογιού χειρός", "title_en": "From a queen's bracelet to the trenches: the history of the wristwatch", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας ομιλίας σε έναν κύκλο εκδηλώσεων για την ιστορία των καθημερινών αντικειμένων.",
 "script": [
  L("Ομιλήτρια", "f", "Για περίπου τρεις αιώνες, ένας κύριος που σεβόταν τον εαυτό του κρατούσε την ώρα στην τσέπη του γιλέκου του, δεμένη με μια αλυσίδα. Το ρολόι τσέπης ήταν σύμβολο κύρους, συχνά δώρο για μια αποφοίτηση ή για μια συνταξιοδότηση, και περνούσε από τον πατέρα στον γιο.", "For about three centuries, a self-respecting gentleman kept the time in his waistcoat pocket, attached to a chain. The pocket watch was a status symbol, often a gift for a graduation or a retirement, and passed from father to son."),
  L("Ομιλήτρια", "f", "Το πρώτο ρολόι που σχεδιάστηκε ειδικά για τον καρπό αποδίδεται συνήθως στον ωρολογοποιό Μπρεγκέ, που το έφτιαξε στις αρχές του δέκατου ένατου αιώνα για τη βασίλισσα της Νάπολης. Για δεκαετίες μετά, τα ρολόγια χειρός θεωρούνταν κοσμήματα για γυναίκες, «βραχιόλια», και κανένας άντρας δεν θα φορούσε κάτι τέτοιο.", "The first watch designed specifically for the wrist is usually attributed to the watchmaker Breguet, who made it in the early nineteenth century for the Queen of Naples. For decades afterwards, wristwatches were considered women's jewellery, 'bracelets', and no man would wear such a thing."),
  L("Ομιλήτρια", "f", "Αυτό το άλλαξε ο πόλεμος. Στα χαρακώματα του Πρώτου Παγκοσμίου Πολέμου, οι αξιωματικοί έπρεπε να συντονίζουν επιθέσεις με ακρίβεια λεπτού, και ήταν αδύνατο να ψάχνουν στην τσέπη τους κάτω από τα πυρά. Έδεναν λοιπόν το ρολόι στον καρπό με ένα λουρί. Όταν γύρισαν στο σπίτι, το «γυναικείο βραχιόλι» είχε γίνει σύμβολο ανδρείας.", "War changed that. In the trenches of the First World War, officers had to coordinate attacks to the minute, and it was impossible to rummage in their pockets under fire. So they strapped the watch to their wrist. When they came home, the 'ladies' bracelet' had become a symbol of courage."),
  L("Ομιλήτρια", "f", "Η επόμενη επανάσταση ήρθε το 1969, όταν μια ιαπωνική εταιρεία έβγαλε στην αγορά το πρώτο ρολόι χαλαζία, πιο ακριβές και πολύ φθηνότερο από τα μηχανικά. Η ελβετική ωρολογοποιία πέρασε τότε μια βαθιά κρίση, από την οποία βγήκε στρέφοντας την προσοχή της στην πολυτέλεια. Σήμερα, ειρωνικά, πολλοί από εμάς έχουμε πάλι στον καρπό έναν μικρό υπολογιστή, που απλώς μας λέει και την ώρα.", "The next revolution came in 1969, when a Japanese company put on the market the first quartz watch, more accurate and much cheaper than mechanical ones. Swiss watchmaking then went through a deep crisis, from which it emerged by turning its attention to luxury. Today, ironically, many of us again have on our wrist a small computer that also happens to tell us the time."),
 ],
 "questions": [
  Q("Τι συμβόλιζε το ρολόι τσέπης;", ["Τη στρατιωτική ζωή", "Το κύρος", "Τη φτώχεια", "Τη γυναικεία κομψότητα"], 1, "Το ρολόι τσέπης ήταν σύμβολο κύρους"),
  Q("Για ποιον φτιάχτηκε, σύμφωνα με την παράδοση, το πρώτο ρολόι χειρός;", ["Για έναν Γάλλο στρατηγό", "Για τη βασίλισσα της Νάπολης", "Για έναν αεροπόρο", "Για τον ίδιο τον ωρολογοποιό"], 1, "το έφτιαξε … για τη βασίλισσα της Νάπολης"),
  Q("Γιατί οι αξιωματικοί έδεναν το ρολόι στον καρπό;", ["Για να μην τους το κλέψουν", "Γιατί ήταν της μόδας", "Για να βλέπουν την ώρα χωρίς να ψάχνουν στην τσέπη κάτω από τα πυρά", "Γιατί ήταν πιο φθηνό"], 2, "ήταν αδύνατο να ψάχνουν στην τσέπη τους κάτω από τα πυρά"),
  Q("Πώς βγήκε η ελβετική ωρολογοποιία από την κρίση;", ["Φτιάχνοντας ρολόγια χαλαζία", "Στρέφοντας την προσοχή της στην πολυτέλεια", "Μεταφέροντας τα εργοστάσια στην Ιαπωνία", "Κατασκευάζοντας υπολογιστές"], 1, "βγήκε στρέφοντας την προσοχή της στην πολυτέλεια"),
 ],
 "gloss": {"γιλέκου": "γιλέκο — waistcoat", "κύρους": "κύρος — prestige, status", "συνταξιοδότηση": "συνταξιοδότηση — retirement", "καρπό": "καρπός — wrist", "ωρολογοποιό": "ωρολογοποιός — watchmaker", "χαρακώματα": "χαράκωμα — trench", "συντονίζουν": "συντονίζω — to coordinate", "πυρά": "πυρά — (gun)fire", "λουρί": "λουρί — strap", "ανδρείας": "ανδρεία — bravery, courage", "χαλαζία": "χαλαζίας — quartz", "ειρωνικά": "ειρωνικά — ironically"}
})

ITEMS.append({
 "id": "l262-c1-int-fotiko-ftarnisma", "title": "Γιατί κάποιοι φταρνίζονται στον ήλιο; Μια γενετίστρια εξηγεί", "title_en": "Why do some people sneeze in sunlight? A geneticist explains", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή για την επιστήμη της καθημερινής ζωής.",
 "script": [
  L("Δημοσιογράφος", "m", "Βγαίνω από ένα σκοτεινό σινεμά στον ήλιο και φταρνίζομαι δύο-τρεις φορές. Οι φίλοι μου γελάνε. Είμαι παράξενος;", "I come out of a dark cinema into the sun and sneeze two or three times. My friends laugh. Am I strange?"),
  L("Γενετίστρια", "f", "Καθόλου. Το φαινόμενο λέγεται φωτικό αντανακλαστικό του φταρνίσματος, και ανάλογα με τη μελέτη αφορά περίπου έναν στους τέσσερις ή έναν στους τρεις ανθρώπους. Δεν είναι καν καινούρια παρατήρηση: ήδη ένα αρχαίο κείμενο από τον κύκλο του Αριστοτέλη αναρωτιέται γιατί η ζέστη του ήλιου μάς κάνει να φταρνιζόμαστε.", "Not at all. The phenomenon is called the photic sneeze reflex, and depending on the study it affects about one in four or one in three people. It isn't even a new observation: an ancient text from Aristotle's circle already wonders why the heat of the sun makes us sneeze."),
  L("Δημοσιογράφος", "m", "Και ποια είναι η απάντηση; Η ζέστη;", "And what is the answer? The heat?"),
  L("Γενετίστρια", "f", "Όχι, το φως. Η επικρατέστερη υπόθεση είναι ότι το οπτικό νεύρο, όταν δέχεται ξαφνικά πολύ φως, διεγείρει κατά λάθος και ένα γειτονικό νεύρο, που ελέγχει την αίσθηση στη μύτη. Ο εγκέφαλος «μπερδεύει» τα σήματα και απαντά με φτάρνισμα. Είναι μια υπόθεση, όχι ακόμη αποδεδειγμένη θεωρία.", "No, the light. The prevailing hypothesis is that the optic nerve, when it suddenly receives a lot of light, accidentally also stimulates a neighbouring nerve that controls sensation in the nose. The brain 'confuses' the signals and responds with a sneeze. It is a hypothesis, not yet a proven theory."),
  L("Δημοσιογράφος", "m", "Και γιατί εγώ ναι και η γυναίκα μου όχι;", "And why me and not my wife?"),
  L("Γενετίστρια", "f", "Εδώ μπαίνει η γενετική. Το χαρακτηριστικό τρέχει στις οικογένειες· αν το έχει ένας γονιός, υπάρχουν πολλές πιθανότητες να το έχουν και τα παιδιά. Μεγάλες γενετικές μελέτες έχουν εντοπίσει περιοχές του DNA που συνδέονται μαζί του, αν και δεν έχουμε βρει «το» γονίδιο. Συνήθως είναι αθώο, με μία εξαίρεση: για έναν πιλότο ή έναν οδηγό που βγαίνει από ένα τούνελ, ένα ξαφνικό φτάρνισμα δεν είναι καθόλου αστείο.", "This is where genetics comes in. The trait runs in families; if one parent has it, there is a good chance the children have it too. Large genetic studies have located regions of DNA linked to it, although we haven't found 'the' gene. It is usually harmless, with one exception: for a pilot, or a driver coming out of a tunnel, a sudden sneeze is no joke at all."),
 ],
 "questions": [
  Q("Πόσους ανθρώπους αφορά περίπου το φαινόμενο;", ["Έναν στους εκατό", "Έναν στους δέκα", "Έναν στους τέσσερις ή στους τρεις", "Τους μισούς"], 2, "αφορά περίπου έναν στους τέσσερις ή έναν στους τρεις ανθρώπους"),
  Q("Τι προκαλεί, κατά την επικρατέστερη υπόθεση, το φτάρνισμα;", ["Η ζέστη του ήλιου", "Το φως, που διεγείρει κατά λάθος ένα γειτονικό νεύρο", "Η σκόνη στον αέρα", "Μια αλλεργία στο φως"], 1, "το οπτικό νεύρο … διεγείρει κατά λάθος και ένα γειτονικό νεύρο"),
  Q("Τι λέει για τη γενετική του φαινομένου;", ["Ότι βρέθηκε το γονίδιο που το προκαλεί", "Ότι δεν έχει σχέση με τη γενετική", "Ότι τρέχει στις οικογένειες, αλλά δεν βρέθηκε «το» γονίδιο", "Ότι το έχουν μόνο οι άντρες"], 2, "Το χαρακτηριστικό τρέχει στις οικογένειες … αν και δεν έχουμε βρει «το» γονίδιο"),
  Q("Πότε μπορεί το φαινόμενο να είναι επικίνδυνο;", ["Όταν κάποιος κοιμάται", "Για έναν πιλότο ή έναν οδηγό που βγαίνει από τούνελ", "Όταν κάποιος έχει πυρετό", "Για τα μικρά παιδιά"], 1, "για έναν πιλότο ή έναν οδηγό που βγαίνει από ένα τούνελ"),
 ],
 "gloss": {"φταρνίζομαι": "φταρνίζομαι — to sneeze", "αντανακλαστικό": "αντανακλαστικό — reflex", "αναρωτιέται": "αναρωτιέμαι — to wonder", "επικρατέστερη": "επικρατέστερος — prevailing", "υπόθεση": "υπόθεση — hypothesis", "οπτικό νεύρο": "οπτικό νεύρο — optic nerve", "διεγείρει": "διεγείρω — to stimulate", "αποδεδειγμένη": "αποδεδειγμένος — proven", "χαρακτηριστικό": "χαρακτηριστικό — trait", "εντοπίσει": "εντοπίζω — to locate, identify", "γονίδιο": "γονίδιο — gene", "αθώο": "αθώος — harmless, innocent"}
})

rnd = random.Random(262)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-262.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
