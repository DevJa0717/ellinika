# Source for library/listening/listening-93.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l93.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l93-ann-allagi-oras", "title": "Γυρίζουμε τα ρολόγια μία ώρα πίσω", "title_en": "Turning the clocks back an hour", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στο ραδιόφωνο ένα Σάββατο του Οκτωβρίου.",
 "script": [
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε στους ακροατές μας ότι αυτή τη νύχτα, ξημερώματα Κυριακής, τελειώνει η θερινή ώρα. Στις τέσσερις τα ξημερώματα οι δείκτες των ρολογιών θα γυρίσουν μία ώρα πίσω, δηλαδή στις τρεις.", "We remind our listeners that tonight, in the early hours of Sunday, summer time ends. At four in the morning the hands of the clocks will go back one hour, that is, to three."),
  L("Εκφωνήτρια", "f", "Τα κινητά τηλέφωνα και οι υπολογιστές θα αλλάξουν ώρα αυτόματα. Θα πρέπει, όμως, να ρυθμίσετε μόνοι σας τα ρολόγια τοίχου, τα ξυπνητήρια, τον φούρνο και το ρολόι του αυτοκινήτου. Όσοι εργάζονται σε νυχτερινή βάρδια θα δουλέψουν μία ώρα περισσότερο.", "Mobile phones and computers will change the time automatically. You will, however, have to adjust wall clocks, alarm clocks, the oven and the car clock yourselves. Those working the night shift will work one hour longer."),
  L("Εκφωνήτρια", "f", "Τα δρομολόγια των πλοίων, των τρένων και των αεροπλάνων της Κυριακής θα εκτελεστούν κανονικά, σύμφωνα με τη νέα ώρα. Και μην ξεχνάτε: από αύριο θα νυχτώνει νωρίτερα, γι’ αυτό οι οδηγοί καλό είναι να ανάβουν τα φώτα έγκαιρα. Η θερινή ώρα θα επιστρέψει την τελευταία Κυριακή του Μαρτίου.", "Sunday's ferry, train and flight services will run normally, according to the new time. And don't forget: from tomorrow it will get dark earlier, so drivers would do well to switch their lights on in good time. Summer time will return on the last Sunday of March."),
 ],
 "questions": [
  Q("Τι θα γίνει στις τέσσερις τα ξημερώματα;", ["Τα ρολόγια θα πάνε μία ώρα μπροστά", "Τα ρολόγια θα γυρίσουν μία ώρα πίσω", "Θα κοπεί το ρεύμα", "Θα σταματήσουν τα τρένα"], 1, "οι δείκτες των ρολογιών θα γυρίσουν μία ώρα πίσω"),
  Q("Ποια ρολόγια πρέπει να ρυθμίσουν μόνοι τους οι ακροατές;", ["Τα κινητά", "Τους υπολογιστές", "Τα ρολόγια τοίχου και τα ξυπνητήρια", "Κανένα"], 2, "να ρυθμίσετε μόνοι σας τα ρολόγια τοίχου, τα ξυπνητήρια"),
  Q("Τι συμβουλεύει η εκφωνήτρια τους οδηγούς;", ["Να οδηγούν πιο αργά", "Να ανάβουν τα φώτα έγκαιρα", "Να μην οδηγούν τη νύχτα", "Να ελέγξουν τα λάστιχα"], 1, "οι οδηγοί καλό είναι να ανάβουν τα φώτα έγκαιρα"),
 ],
 "gloss": {"ξημερώματα": "ξημερώματα — early hours of the morning", "θερινή ώρα": "θερινή ώρα — summer time", "δείκτες": "δείκτης — (clock) hand", "αυτόματα": "αυτόματα — automatically", "ρυθμίσετε": "ρυθμίζω — to set, adjust", "ξυπνητήρια": "ξυπνητήρι — alarm clock", "βάρδια": "βάρδια — shift", "εκτελεστούν": "εκτελούμαι — to be carried out, run", "νυχτώνει": "νυχτώνει — it gets dark", "έγκαιρα": "έγκαιρα — in good time"}
})
ITEMS.append({
 "id": "l93-vm-xechasmeno-kinito", "title": "Ξεχάσατε το κινητό σας", "title_en": "You left your phone behind", "type": "voicemail", "level": "B2",
 "context_el": "Χθες το βράδυ φάγατε σε μια ταβέρνα με φίλους. Σήμερα το πρωί ακούτε ένα μήνυμα στον σταθερό σας.",
 "script": [
  L("Ιδιοκτήτρια", "f", "Καλημέρα σας, από την ταβέρνα «Το Πλατάνι» σας παίρνω, στην Κηφισιά. Χθες το βράδυ, όταν μαζεύαμε, βρήκαμε ένα κινητό κάτω από το τραπέζι στο οποίο καθόσασταν, ένα μαύρο με μπλε θήκη. Πήραμε το τελευταίο νούμερο που σας είχε καλέσει, και η φίλη σας μάς έδωσε αυτόν τον αριθμό.", "Good morning, I'm calling from the Platani taverna in Kifisia. Last night, when we were clearing up, we found a mobile under the table where you were sitting, a black one with a blue case. We rang the last number that had called it, and your friend gave us this number."),
  L("Ιδιοκτήτρια", "f", "Το κρατάμε στο ταμείο. Μπορείτε να περάσετε να το πάρετε από τις δώδεκα το μεσημέρι μέχρι τις δώδεκα το βράδυ, κάθε μέρα εκτός από Δευτέρα, που είμαστε κλειστά. Θα σας ζητήσουμε μόνο να μας πείτε τον κωδικό ή να μας δείξετε μια φωτογραφία σας μέσα στο τηλέφωνο, για να είμαστε σίγουροι ότι είναι δικό σας.", "We're keeping it at the till. You can drop by and collect it from twelve noon to midnight, every day except Monday, when we're closed. We'll only ask you to tell us the code or show us a photo of yourself on the phone, so we can be sure it's yours."),
  L("Ιδιοκτήτρια", "f", "Α, και κάτι ακόμα: το κινητό είχε σχεδόν αδειάσει, οπότε το βάλαμε να φορτίσει. Αν δεν μπορείτε να έρθετε εσείς, μπορεί να το πάρει κάποιος φίλος σας, αρκεί να μας τηλεφωνήσετε πρώτα. Καλή σας μέρα!", "Oh, and one more thing: the phone had almost run out, so we put it on charge. If you can't come yourself, a friend of yours can collect it, as long as you phone us first. Have a good day!"),
 ],
 "questions": [
  Q("Πώς βρήκε η ιδιοκτήτρια τον αριθμό;", ["Από τον λογαριασμό", "Από τη φίλη που είχε καλέσει τελευταία το κινητό", "Από την αστυνομία", "Από την κράτηση"], 1, "Πήραμε το τελευταίο νούμερο που σας είχε καλέσει, και η φίλη σας μάς έδωσε αυτόν τον αριθμό"),
  Q("Πότε δεν μπορεί να περάσει να το πάρει;", ["Το Σάββατο", "Την Κυριακή", "Τη Δευτέρα", "Την Παρασκευή"], 2, "κάθε μέρα εκτός από Δευτέρα, που είμαστε κλειστά"),
  Q("Τι θα του ζητήσουν για να του το δώσουν;", ["Την ταυτότητά του", "Τον κωδικό ή μια φωτογραφία του μέσα στο τηλέφωνο", "Την απόδειξη αγοράς", "Να πληρώσει κάτι"], 1, "να μας πείτε τον κωδικό ή να μας δείξετε μια φωτογραφία σας μέσα στο τηλέφωνο"),
 ],
 "gloss": {"σταθερό": "σταθερό (τηλέφωνο) — landline", "μαζεύαμε": "μαζεύω — to clear up", "θήκη": "θήκη — case, cover", "ταμείο": "ταμείο — till, cash desk", "κωδικό": "κωδικός — code, PIN", "αδειάσει": "αδειάζω — to run out (of battery)", "φορτίσει": "φορτίζω — to charge", "αρκεί": "αρκεί να — as long as"}
})
ITEMS.append({
 "id": "l93-dia-tsimpima-melissas", "title": "Ένα τσίμπημα μέλισσας", "title_en": "A bee sting", "type": "dialogue", "level": "B2",
 "context_el": "Μια μητέρα μπαίνει βιαστικά σε ένα φαρμακείο ενός νησιού με τον εννιάχρονο γιο της.",
 "script": [
  L("Μητέρα", "f", "Καλημέρα. Τον γιο μου τον τσίμπησε μια μέλισσα στο χέρι, πριν από δέκα λεπτά, στην παραλία. Πρήστηκε πολύ και τον πονάει.", "Good morning. A bee stung my son on the hand ten minutes ago, at the beach. It's swollen a lot and it hurts him."),
  L("Φαρμακοποιός", "m", "Για να δω… Βλέπετε αυτό το μικρό μαύρο σημαδάκι; Είναι το κεντρί, έχει μείνει μέσα. Θα το βγάλω ξύνοντας απαλά με μια κάρτα· με τσιμπιδάκι δεν είναι καλό, γιατί πιέζεις το δηλητήριο προς τα μέσα. Εντάξει, φίλε μου, τελείωσε!", "Let me see... Can you see this little black mark? That's the sting; it's stayed in. I'll take it out by gently scraping with a card; tweezers aren't good, because you squeeze the venom further in. There you go, my friend, all done!"),
  L("Μητέρα", "f", "Ευχαριστώ. Είναι επικίνδυνο; Δεν τον έχει τσιμπήσει ποτέ μέλισσα.", "Thank you. Is it dangerous? He's never been stung by a bee before."),
  L("Φαρμακοποιός", "m", "Συνήθως όχι. Ο πόνος και το πρήξιμο είναι φυσιολογικά. Βάλτε του πάγο τυλιγμένο σε μια πετσέτα, για δέκα λεπτά κάθε φορά, και θα σας δώσω μια αντιισταμινική κρέμα για τη φαγούρα. Πρέπει, όμως, να τον προσέχετε την επόμενη μισή ώρα.", "Usually not. The pain and swelling are normal. Put ice wrapped in a towel on it, for ten minutes at a time, and I'll give you an antihistamine cream for the itching. You must, however, keep an eye on him for the next half hour."),
  L("Μητέρα", "f", "Τι να προσέχω;", "What should I watch for?"),
  L("Φαρμακοποιός", "m", "Αν δυσκολευτεί να αναπνεύσει, αν πρηστούν τα χείλη ή το πρόσωπο, ή αν βγάλει κόκκινα σημάδια σε όλο το σώμα, πηγαίνετε αμέσως στο Κέντρο Υγείας ή καλέστε το εκατόν εξήντα έξι. Αυτά είναι σημάδια αλλεργίας και δεν περιμένουμε.", "If he has trouble breathing, if his lips or face swell, or if he gets red marks all over his body, go straight to the Health Centre or call one six six. Those are signs of an allergy and we don't wait."),
 ],
 "questions": [
  Q("Πώς βγάζει ο φαρμακοποιός το κεντρί;", ["Με τσιμπιδάκι", "Ξύνοντας απαλά με μια κάρτα", "Με τα δάχτυλα", "Με μια βελόνα"], 1, "Θα το βγάλω ξύνοντας απαλά με μια κάρτα"),
  Q("Τι πρέπει να βάλει η μητέρα στο χέρι του παιδιού;", ["Ζεστό νερό", "Αλάτι", "Πάγο τυλιγμένο σε πετσέτα", "Λεμόνι"], 2, "Βάλτε του πάγο τυλιγμένο σε μια πετσέτα"),
  Q("Πότε πρέπει να πάνε αμέσως στο Κέντρο Υγείας;", ["Αν το χέρι πονάει ακόμα το βράδυ", "Αν δυσκολευτεί να αναπνεύσει ή πρηστεί το πρόσωπο", "Αν το παιδί κλαίει", "Αν δεν περάσει η φαγούρα"], 1, "Αν δυσκολευτεί να αναπνεύσει, αν πρηστούν τα χείλη ή το πρόσωπο"),
 ],
 "gloss": {"τσίμπησε": "τσιμπάω — to sting, bite", "Πρήστηκε": "πρήζομαι — to swell", "κεντρί": "κεντρί — sting (of a bee)", "ξύνοντας": "ξύνω — to scrape", "τσιμπιδάκι": "τσιμπιδάκι — tweezers", "δηλητήριο": "δηλητήριο — venom, poison", "πρήξιμο": "πρήξιμο — swelling", "τυλιγμένο": "τυλιγμένος — wrapped", "αντιισταμινική": "αντιισταμινικός — antihistamine", "φαγούρα": "φαγούρα — itching", "Κέντρο Υγείας": "Κέντρο Υγείας — health centre", "αλλεργίας": "αλλεργία — allergy"}
})
ITEMS.append({
 "id": "l93-int-seismologos", "title": "Τι κάνουμε σε έναν σεισμό", "title_en": "What to do in an earthquake", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, ένας δημοσιογράφος μιλά με μια σεισμολόγο, μετά από έναν μικρό σεισμό που έγινε αισθητός στην πόλη.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί ακροατές τρόμαξαν χθες το βράδυ. Πρέπει να ανησυχούμε;", "Many listeners were frightened last night. Should we be worried?"),
  L("Σεισμολόγος", "f", "Ήταν ένας σεισμός τεσσάρων ρίχτερ, χωρίς ζημιές. Η Ελλάδα είναι η πιο σεισμογενής χώρα της Ευρώπης: κάθε χρόνο καταγράφουμε χιλιάδες σεισμούς, οι περισσότεροι τόσο μικροί που δεν τους νιώθει κανείς. Γι’ αυτό και οι κτιριακοί κανονισμοί μας είναι από τους πιο αυστηρούς.", "It was a magnitude four earthquake, with no damage. Greece is the most earthquake-prone country in Europe: every year we record thousands of earthquakes, most so small that no one feels them. That's also why our building regulations are among the strictest."),
  L("Δημοσιογράφος", "m", "Μπορούν οι επιστήμονες να προβλέψουν έναν μεγάλο σεισμό;", "Can scientists predict a big earthquake?"),
  L("Σεισμολόγος", "f", "Όχι, και πρέπει να το λέμε καθαρά. Ξέρουμε ποιες περιοχές έχουν μεγαλύτερο κίνδυνο, αλλά κανείς δεν μπορεί να πει πότε ακριβώς θα γίνει ένας σεισμός. Όποιος ισχυρίζεται το αντίθετο στα μέσα κοινωνικής δικτύωσης απλώς σκορπίζει πανικό.", "No, and we have to say it clearly. We know which areas are at greater risk, but no one can say exactly when an earthquake will happen. Anyone who claims otherwise on social media is simply spreading panic."),
  L("Δημοσιογράφος", "m", "Τι πρέπει να κάνουμε, λοιπόν, τη στιγμή του σεισμού;", "So what should we do at the moment of the earthquake?"),
  L("Σεισμολόγος", "f", "Τρεις λέξεις: σκύψε, κάλυψε, κρατήσου. Σκύβουμε κάτω από ένα γερό τραπέζι, καλύπτουμε το κεφάλι μας και κρατιόμαστε από το πόδι του τραπεζιού μέχρι να σταματήσει η δόνηση. Δεν τρέχουμε στις σκάλες, και ποτέ δεν χρησιμοποιούμε τον ανελκυστήρα. Και καλό είναι κάθε σπίτι να έχει έτοιμο ένα σακίδιο με νερό, φακό και φάρμακα.", "Three words: drop, cover, hold on. We crouch under a sturdy table, cover our head and hold on to the table leg until the shaking stops. We don't run to the stairs, and we never use the lift. And it's a good idea for every home to have a bag ready with water, a torch and medicines."),
 ],
 "questions": [
  Q("Τι λέει η σεισμολόγος για τον χθεσινό σεισμό;", ["Ότι προκάλεσε ζημιές", "Ότι ήταν τεσσάρων ρίχτερ, χωρίς ζημιές", "Ότι θα ακολουθήσει μεγαλύτερος", "Ότι δεν έγινε αισθητός"], 1, "Ήταν ένας σεισμός τεσσάρων ρίχτερ, χωρίς ζημιές"),
  Q("Μπορούν οι επιστήμονες να προβλέψουν έναν σεισμό;", ["Ναι, με ακρίβεια", "Μόνο τους μεγάλους", "Όχι, κανείς δεν μπορεί να πει πότε ακριβώς θα γίνει", "Ναι, λίγες ώρες πριν"], 2, "κανείς δεν μπορεί να πει πότε ακριβώς θα γίνει ένας σεισμός"),
  Q("Τι δεν πρέπει να κάνουμε τη στιγμή του σεισμού;", ["Να σκύψουμε κάτω από ένα τραπέζι", "Να καλύψουμε το κεφάλι μας", "Να χρησιμοποιήσουμε τον ανελκυστήρα", "Να κρατηθούμε από το τραπέζι"], 2, "ποτέ δεν χρησιμοποιούμε τον ανελκυστήρα"),
 ],
 "gloss": {"σεισμολόγο": "σεισμολόγος — seismologist", "αισθητός": "αισθητός — felt, noticeable", "ρίχτερ": "ρίχτερ — (on the) Richter (scale)", "σεισμογενής": "σεισμογενής — earthquake-prone", "κτιριακοί": "κτιριακός — building (adjective)", "κανονισμοί": "κανονισμός — regulation", "προβλέψουν": "προβλέπω — to predict", "σκορπίζει": "σκορπίζω — to spread", "σκύψε": "σκύβω — to crouch, bend down", "κρατήσου": "κρατιέμαι — to hold on", "δόνηση": "δόνηση — shaking, tremor", "σακίδιο": "σακίδιο — backpack"}
})
ITEMS.append({
 "id": "l93-rep-amorgos", "title": "Αμοργός, το νησί του Απέραντου Γαλάζιου", "title_en": "Amorgos, the island of The Big Blue", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ταξιδιωτικό ρεπορτάζ στο ραδιόφωνο.",
 "script": [
  L("Ρεπόρτερ", "f", "Η Αμοργός, το ανατολικότερο νησί των Κυκλάδων, έγινε γνωστή σε όλο τον κόσμο το 1988, όταν γυρίστηκε εδώ η ταινία του Λικ Μπεσόν «Το Απέραντο Γαλάζιο». Το ναυάγιο του πλοίου «Ολυμπία», που φαίνεται στην ταινία, βρίσκεται ακόμη μισοβυθισμένο σε έναν κόλπο στο νότιο άκρο του νησιού.", "Amorgos, the easternmost island of the Cyclades, became known all over the world in 1988, when Luc Besson's film The Big Blue was shot here. The wreck of the ship Olympia, which appears in the film, still lies half-sunk in a bay at the southern tip of the island."),
  L("Ρεπόρτερ", "f", "Το πιο εντυπωσιακό αξιοθέατο, όμως, είναι η Μονή της Χοζοβιώτισσας, ένα κάτασπρο μοναστήρι του ενδέκατου αιώνα, χτισμένο κυριολεκτικά μέσα στον βράχο, τριακόσια μέτρα πάνω από τη θάλασσα. Για να φτάσει κανείς εκεί, πρέπει να ανέβει μερικές εκατοντάδες σκαλιά. Στην είσοδο οι μοναχοί υποδέχονται τους επισκέπτες με ένα ποτηράκι ρακόμελο.", "The most impressive sight, however, is the Monastery of Chozoviotissa, a snow-white eleventh-century monastery built literally into the rock, three hundred metres above the sea. To get there, you have to climb a few hundred steps. At the entrance the monks welcome visitors with a small glass of rakomelo."),
  L("Ρεπόρτερ", "f", "Η Αμοργός είναι επίσης παράδεισος για τους πεζοπόρους. Τα παλιά μονοπάτια που ένωναν τα χωριά έχουν καθαριστεί και σηματοδοτηθεί, και η πιο γνωστή διαδρομή, η «Παλιά Στράτα», διασχίζει όλο το νησί κατά μήκος της κορυφογραμμής. Την άνοιξη, όταν τα λουλούδια ανθίζουν, είναι η καλύτερη εποχή για να την περπατήσει κανείς.", "Amorgos is also a paradise for walkers. The old paths that linked the villages have been cleared and waymarked, and the best-known route, the Old Strata, crosses the whole island along the ridge. In spring, when the flowers are in bloom, is the best time to walk it."),
 ],
 "questions": [
  Q("Πότε έγινε η Αμοργός γνωστή σε όλο τον κόσμο;", ["Όταν ανακαλύφθηκε ένα ναυάγιο", "Όταν γυρίστηκε εκεί μια γνωστή ταινία", "Όταν χτίστηκε το μοναστήρι", "Όταν άνοιξε το αεροδρόμιο"], 1, "όταν γυρίστηκε εδώ η ταινία του Λικ Μπεσόν"),
  Q("Τι είναι ξεχωριστό στη Μονή της Χοζοβιώτισσας;", ["Είναι το μεγαλύτερο μοναστήρι της Ελλάδας", "Είναι χτισμένη μέσα στον βράχο, ψηλά πάνω από τη θάλασσα", "Βρίσκεται σε ένα νησάκι", "Δεν επιτρέπονται επισκέπτες"], 1, "χτισμένο κυριολεκτικά μέσα στον βράχο, τριακόσια μέτρα πάνω από τη θάλασσα"),
  Q("Ποια είναι η καλύτερη εποχή για την «Παλιά Στράτα»;", ["Το καλοκαίρι", "Το φθινόπωρο", "Ο χειμώνας", "Η άνοιξη"], 3, "Την άνοιξη, όταν τα λουλούδια ανθίζουν, είναι η καλύτερη εποχή"),
 ],
 "gloss": {"ανατολικότερο": "ανατολικότερος — easternmost", "γυρίστηκε": "γυρίζομαι (ταινία) — to be filmed", "ναυάγιο": "ναυάγιο — wreck", "μισοβυθισμένο": "μισοβυθισμένος — half-sunk", "αξιοθέατο": "αξιοθέατο — sight, attraction", "κάτασπρο": "κάτασπρος — snow-white", "μοναχοί": "μοναχός — monk", "ρακόμελο": "ρακόμελο — raki with honey", "πεζοπόρους": "πεζοπόρος — walker, hiker", "σηματοδοτηθεί": "σηματοδοτούμαι — to be waymarked", "κορυφογραμμής": "κορυφογραμμή — ridge", "ανθίζουν": "ανθίζω — to bloom"}
})
ITEMS.append({
 "id": "l93-rep-thasos", "title": "Θάσος, το πράσινο νησί", "title_en": "Thasos, the green island", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια τηλεοπτική εκπομπή για τα νησιά του βόρειου Αιγαίου.",
 "script": [
  L("Ρεπόρτερ", "m", "Μόλις σαράντα λεπτά με το φέρι από την Κεραμωτή, η Θάσος είναι ένα από τα πιο πράσινα νησιά της Ελλάδας. Πευκοδάση κατεβαίνουν μέχρι τη θάλασσα, και στο εσωτερικό τα ορεινά χωριά, όπως η Παναγία και η Θεολόγος, διατηρούν τα πέτρινα σπίτια με τις σχιστόπλακες στις στέγες.", "Just forty minutes by ferry from Keramoti, Thasos is one of the greenest islands in Greece. Pine forests come down to the sea, and inland the mountain villages, such as Panagia and Theologos, keep their stone houses with slate roofs."),
  L("Ρεπόρτερ", "m", "Στην αρχαιότητα η Θάσος ήταν μια πλούσια πόλη, χάρη στα ορυχεία χρυσού και κυρίως στο λευκό της μάρμαρο, που εξαγόταν σε όλο τον αρχαίο κόσμο. Τα λατομεία λειτουργούν ακόμη και σήμερα. Στο σημερινό λιμάνι, τον Λιμένα, οι επισκέπτες μπορούν να περπατήσουν στην αρχαία αγορά και να δουν το θέατρο, πάνω από την πόλη.", "In antiquity Thasos was a rich city, thanks to its gold mines and above all its white marble, which was exported throughout the ancient world. The quarries still operate today. In the present-day port, Limenas, visitors can walk through the ancient agora and see the theatre above the town."),
  L("Ρεπόρτερ", "m", "Το νησί φημίζεται επίσης για το μέλι του, το ελαιόλαδο και τις ελιές του. Και για όσους ψάχνουν κάτι διαφορετικό, στη νότια ακτή υπάρχει η Γκιόλα, μια φυσική πισίνα ανάμεσα στους βράχους, όπου το νερό είναι πάντα ήρεμο, ακόμα κι όταν η θάλασσα έξω είναι φουρτουνιασμένη.", "The island is also famous for its honey, olive oil and olives. And for those looking for something different, on the south coast there is Giola, a natural pool among the rocks, where the water is always calm, even when the sea outside is rough."),
 ],
 "questions": [
  Q("Πώς φτάνει κανείς στη Θάσο, σύμφωνα με το ρεπορτάζ;", ["Με αεροπλάνο από τη Θεσσαλονίκη", "Με το φέρι από την Κεραμωτή", "Από μια γέφυρα", "Με πλοίο από τον Πειραιά"], 1, "Μόλις σαράντα λεπτά με το φέρι από την Κεραμωτή"),
  Q("Από τι προερχόταν ο πλούτος της αρχαίας Θάσου;", ["Από το εμπόριο κρασιού", "Από τα ορυχεία χρυσού και το μάρμαρο", "Από το ψάρεμα", "Από τη ναυπηγική"], 1, "χάρη στα ορυχεία χρυσού και κυρίως στο λευκό της μάρμαρο"),
  Q("Τι είναι η Γκιόλα;", ["Ένα ορεινό χωριό", "Ένα αρχαίο θέατρο", "Μια φυσική πισίνα ανάμεσα στους βράχους", "Ένα λατομείο"], 2, "μια φυσική πισίνα ανάμεσα στους βράχους"),
 ],
 "gloss": {"φέρι": "φέρι — ferry", "Πευκοδάση": "πευκοδάσος — pine forest", "σχιστόπλακες": "σχιστόπλακα — slate", "ορυχεία": "ορυχείο — mine", "μάρμαρο": "μάρμαρο — marble", "εξαγόταν": "εξάγομαι — to be exported", "λατομεία": "λατομείο — quarry", "αγορά": "αρχαία αγορά — ancient agora, marketplace", "φημίζεται": "φημίζομαι — to be famous", "φουρτουνιασμένη": "φουρτουνιασμένος — rough, stormy"}
})
ITEMS.append({
 "id": "l93-mono-egina-pappous", "title": "Έγινα παππούς", "title_en": "I became a grandfather", "type": "monologue", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή με ιστορίες ακροατών, ένας άντρας εξήντα πέντε χρόνων μιλά για μια καινούργια εμπειρία.",
 "script": [
  L("Ακροατής", "m", "Όταν γεννήθηκαν τα παιδιά μου, δούλευα δώδεκα ώρες τη μέρα. Έφευγα πριν ξυπνήσουν και γύριζα όταν είχαν ήδη κοιμηθεί. Τα πρώτα τους βήματα, τις πρώτες τους λέξεις, τα έμαθα από τη γυναίκα μου στο τηλέφωνο. Τότε νόμιζα ότι έτσι πρέπει να είναι ένας πατέρας.", "When my children were born, I was working twelve hours a day. I left before they woke up and came home when they were already asleep. Their first steps, their first words, I heard about from my wife on the phone. Back then I thought that's how a father had to be."),
  L("Ακροατής", "m", "Πριν από έναν χρόνο, η κόρη μου γέννησε έναν γιο, και επειδή εγώ είχα μόλις βγει στη σύνταξη, προσφέρθηκα να τον κρατάω τρία πρωινά την εβδομάδα. Η κόρη μου με κοίταξε με δυσπιστία· δεν θυμόταν να με έχει δει ποτέ να αλλάζω πάνα. Είχε δίκιο: τις πρώτες φορές χρειαζόμουν ένα βίντεο στο κινητό και πολλή υπομονή.", "A year ago, my daughter had a son, and because I had just retired, I offered to look after him three mornings a week. My daughter looked at me doubtfully; she couldn't remember ever having seen me change a nappy. She was right: the first few times I needed a video on my phone and a lot of patience."),
  L("Ακροατής", "m", "Τώρα ξέρω να του ετοιμάζω τον χυλό, να τον κοιμίζω με ένα τραγούδι που μου έλεγε η μάνα μου και να τον βγάζω βόλτα στο πάρκο. Χθες έκανε τα πρώτα του βήματα, και ήμουν εγώ εκεί να τον πιάσω. Δεν μπορώ να γυρίσω τον χρόνο πίσω για τα παιδιά μου. Μπορώ, όμως, να είμαι εκεί για τον εγγονό μου.", "Now I know how to make his porridge, how to get him to sleep with a song my mother used to sing to me, and how to take him out for a walk in the park. Yesterday he took his first steps, and I was there to catch him. I can't turn back time for my children. But I can be there for my grandson."),
 ],
 "questions": [
  Q("Γιατί ο ακροατής δεν είδε τα παιδιά του να μεγαλώνουν;", ["Γιατί ζούσε στο εξωτερικό", "Γιατί δούλευε δώδεκα ώρες τη μέρα", "Γιατί ήταν άρρωστος", "Γιατί είχε χωρίσει"], 1, "δούλευα δώδεκα ώρες τη μέρα"),
  Q("Πώς αντέδρασε η κόρη του όταν προσφέρθηκε να κρατάει το μωρό;", ["Χάρηκε αμέσως", "Τον κοίταξε με δυσπιστία", "Αρνήθηκε", "Του ζήτησε να το κρατάει κάθε μέρα"], 1, "Η κόρη μου με κοίταξε με δυσπιστία"),
  Q("Τι έγινε χθες;", ["Ο εγγονός είπε την πρώτη του λέξη", "Ο εγγονός έκανε τα πρώτα του βήματα", "Ο εγγονός αρρώστησε", "Γιόρτασαν τα γενέθλιά του"], 1, "Χθες έκανε τα πρώτα του βήματα"),
 ],
 "gloss": {"βήματα": "βήμα — step", "σύνταξη": "σύνταξη — retirement, pension", "προσφέρθηκα": "προσφέρομαι — to offer (to do)", "δυσπιστία": "δυσπιστία — disbelief, doubt", "πάνα": "πάνα — nappy", "υπομονή": "υπομονή — patience", "χυλό": "χυλός — porridge, baby cereal", "κοιμίζω": "κοιμίζω — to put to sleep", "εγγονό": "εγγονός — grandson"}
})
ITEMS.append({
 "id": "l93-mono-tilergasia", "title": "Δουλεύω από το σπίτι", "title_en": "I work from home", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για τον κόσμο της εργασίας, μια μεταφράστρια μιλά για την καθημερινότητά της.",
 "script": [
  L("Μεταφράστρια", "f", "Δουλεύω από το σπίτι εδώ και τρία χρόνια, για μια εταιρεία με έδρα στη Βιέννη. Στην αρχή μού φαινόταν όνειρο: δεν έχανα μιάμιση ώρα την ημέρα στην κίνηση, μπορούσα να δουλεύω με τις παντόφλες και να βάζω πλυντήριο ανάμεσα σε δύο μεταφράσεις.", "I've been working from home for three years, for a company based in Vienna. At first it seemed like a dream: I didn't lose an hour and a half a day in traffic, I could work in my slippers and put a wash on between two translations."),
  L("Μεταφράστρια", "f", "Μετά από μερικούς μήνες, όμως, άρχισαν τα προβλήματα. Η δουλειά δεν τελείωνε ποτέ, γιατί ο υπολογιστής ήταν πάντα εκεί, στο τραπέζι της κουζίνας. Απαντούσα σε μηνύματα στις έντεκα το βράδυ. Και κάποιες μέρες συνειδητοποιούσα ότι δεν είχα μιλήσει με κανέναν άνθρωπο από κοντά.", "After a few months, though, the problems began. Work never ended, because the computer was always there, on the kitchen table. I was answering messages at eleven at night. And some days I realised I hadn't spoken to a single person face to face."),
  L("Μεταφράστρια", "f", "Έτσι έβαλα κανόνες. Μετέτρεψα ένα μικρό δωμάτιο σε γραφείο, και όταν τελειώνω, κλείνω την πόρτα. Το πρωί κάνω μια βόλτα στο τετράγωνο, σαν να πηγαίνω στη δουλειά. Και δύο μέρες την εβδομάδα δουλεύω σε έναν κοινόχρηστο χώρο γραφείων στη γειτονιά, απλώς για να βλέπω ανθρώπους. Δεν θα γύριζα ποτέ σε γραφείο, αλλά έμαθα ότι η ελευθερία χρειάζεται όρια.", "So I set rules. I turned a small room into an office, and when I finish, I close the door. In the morning I walk round the block, as if I were going to work. And two days a week I work in a shared office space in the neighbourhood, just to see people. I'd never go back to an office, but I've learned that freedom needs limits."),
 ],
 "questions": [
  Q("Τι της άρεσε στην αρχή στην τηλεργασία;", ["Ο μεγαλύτερος μισθός", "Ότι δεν έχανε χρόνο στην κίνηση", "Ότι γνώριζε νέους ανθρώπους", "Ότι ταξίδευε στη Βιέννη"], 1, "δεν έχανα μιάμιση ώρα την ημέρα στην κίνηση"),
  Q("Ποιο πρόβλημα παρουσιάστηκε μετά από μερικούς μήνες;", ["Η δουλειά δεν τελείωνε ποτέ", "Χάλασε ο υπολογιστής", "Η εταιρεία μείωσε τον μισθό της", "Οι γείτονες έκαναν θόρυβο"], 0, "Η δουλειά δεν τελείωνε ποτέ"),
  Q("Γιατί πηγαίνει δύο μέρες την εβδομάδα σε κοινόχρηστο χώρο γραφείων;", ["Γιατί το σπίτι της είναι μικρό", "Γιατί το ζητά η εταιρεία", "Για να βλέπει ανθρώπους", "Γιατί εκεί έχει καλύτερο ίντερνετ"], 2, "απλώς για να βλέπω ανθρώπους"),
 ],
 "gloss": {"μεταφράστρια": "μεταφράστρια — translator", "έδρα": "έδρα — headquarters, base", "κίνηση": "κίνηση — traffic", "παντόφλες": "παντόφλα — slipper", "πλυντήριο": "βάζω πλυντήριο — to put a wash on", "συνειδητοποιούσα": "συνειδητοποιώ — to realise", "από κοντά": "από κοντά — face to face, in person", "Μετέτρεψα": "μετατρέπω — to turn into, convert", "τετράγωνο": "τετράγωνο — block", "κοινόχρηστο": "κοινόχρηστος — shared", "όρια": "όριο — limit", "podcast": "podcast — podcast"}
})
ITEMS.append({
 "id": "l93-c1-barnum", "title": "Γιατί πιστεύουμε τα ωροσκόπια", "title_en": "Why we believe horoscopes", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την επιστήμη και τις ψευδοεπιστήμες, η παρουσιάστρια συζητά με έναν ψυχολόγο.",
 "script": [
  L("Παρουσιάστρια", "f", "Εκατομμύρια άνθρωποι διαβάζουν κάθε μέρα το ωροσκόπιό τους και πολλοί ορκίζονται ότι «πέφτει μέσα». Πώς το εξηγείτε;", "Millions of people read their horoscope every day and many swear that it is spot on. How do you explain that?"),
  L("Ψυχολόγος", "m", "Με ένα φαινόμενο που οι ψυχολόγοι ονομάζουν «φαινόμενο Μπάρνουμ», από τον διάσημο Αμερικανό επιχειρηματία του τσίρκου, που υποτίθεται ότι έλεγε πως είχε «κάτι για τον καθένα». Είναι η τάση μας να θεωρούμε ότι γενικόλογες περιγραφές, που ταιριάζουν σχεδόν σε όλους, αφορούν ειδικά εμάς.", "With a phenomenon psychologists call the 'Barnum effect', after the famous American circus showman, who supposedly said he had 'something for everyone'. It is our tendency to believe that vague descriptions, which fit almost everyone, apply specifically to us."),
  L("Παρουσιάστρια", "f", "Έχει αποδειχθεί πειραματικά;", "Has it been proven experimentally?"),
  L("Ψυχολόγος", "m", "Ναι, από το 1948. Ο ψυχολόγος Μπέρτραμ Φόρερ έδωσε στους φοιτητές του ένα τεστ προσωπικότητας και μια εβδομάδα αργότερα στον καθένα μια «εξατομικευμένη» ανάλυση. Τους ζήτησε να βαθμολογήσουν πόσο ακριβής ήταν, σε μια κλίμακα από το μηδέν ως το πέντε. Ο μέσος όρος ήταν πάνω από τέσσερα. Μόνο που όλοι είχαν πάρει ακριβώς το ίδιο κείμενο, με φράσεις από βιβλία αστρολογίας, όπως «Έχετε μεγάλη ανάγκη να σας συμπαθούν και να σας θαυμάζουν οι άλλοι».", "Yes, since 1948. The psychologist Bertram Forer gave his students a personality test and, a week later, each of them a 'personalised' analysis. He asked them to rate how accurate it was on a scale from zero to five. The average was over four. Except that they had all received exactly the same text, with phrases from astrology books, such as 'You have a great need for other people to like and admire you'."),
  L("Παρουσιάστρια", "f", "Γιατί πέφτουμε τόσο εύκολα σε αυτή την παγίδα;", "Why do we fall into this trap so easily?"),
  L("Ψυχολόγος", "m", "Επειδή αυτές οι περιγραφές είναι συνήθως κολακευτικές και αρκετά ασαφείς ώστε ο καθένας να βρίσκει μέσα τους κάτι δικό του. Θυμόμαστε όσα επιβεβαιώνονται και ξεχνάμε όσα δεν ταιριάζουν. Το ίδιο μηχανισμό εκμεταλλεύονται, εκτός από τους αστρολόγους, και πολλά διαδικτυακά τεστ προσωπικότητας, αλλά και ορισμένοι διαφημιστές.", "Because these descriptions are usually flattering and vague enough for everyone to find something of their own in them. We remember what is confirmed and forget what doesn't fit. The same mechanism is exploited not only by astrologers but also by many online personality tests, and by some advertisers."),
 ],
 "questions": [
  Q("Τι είναι το φαινόμενο Μπάρνουμ;", ["Η τάση να εμπιστευόμαστε τους ειδικούς", "Η τάση να θεωρούμε ότι γενικόλογες περιγραφές αφορούν ειδικά εμάς", "Ο φόβος για το μέλλον", "Η αγάπη για το τσίρκο"], 1, "Είναι η τάση μας να θεωρούμε ότι γενικόλογες περιγραφές, που ταιριάζουν σχεδόν σε όλους, αφορούν ειδικά εμάς"),
  Q("Τι έκανε ο Φόρερ στο πείραμά του;", ["Έδωσε σε κάθε φοιτητή διαφορετική ανάλυση", "Έδωσε σε όλους τους φοιτητές το ίδιο κείμενο ως εξατομικευμένη ανάλυση", "Ζήτησε από τους φοιτητές να γράψουν ωροσκόπια", "Σύγκρινε αστρολόγους και ψυχολόγους"], 1, "όλοι είχαν πάρει ακριβώς το ίδιο κείμενο"),
  Q("Πόσο ακριβή βαθμολόγησαν οι φοιτητές την ανάλυση;", ["Κάτω από δύο στα πέντε", "Περίπου δυόμισι στα πέντε", "Πάνω από τέσσερα στα πέντε", "Πέντε στα πέντε"], 2, "Ο μέσος όρος ήταν πάνω από τέσσερα"),
  Q("Γιατί, κατά τον ψυχολόγο, πέφτουμε εύκολα σε αυτή την παγίδα;", ["Γιατί δεν διαβάζουμε προσεκτικά", "Γιατί οι περιγραφές είναι κολακευτικές και ασαφείς", "Γιατί οι αστρολόγοι έχουν πάντα δίκιο", "Γιατί μας αρέσουν τα τεστ"], 1, "αυτές οι περιγραφές είναι συνήθως κολακευτικές και αρκετά ασαφείς"),
 ],
 "gloss": {"ψευδοεπιστήμες": "ψευδοεπιστήμη — pseudoscience", "ωροσκόπιό": "ωροσκόπιο — horoscope", "ορκίζονται": "ορκίζομαι — to swear", "πέφτει μέσα": "πέφτω μέσα — to be spot on", "τσίρκου": "τσίρκο — circus", "γενικόλογες": "γενικόλογος — vague, general", "εξατομικευμένη": "εξατομικευμένος — personalised", "βαθμολογήσουν": "βαθμολογώ — to rate, mark", "κλίμακα": "κλίμακα — scale", "κολακευτικές": "κολακευτικός — flattering", "ασαφείς": "ασαφής — vague, unclear", "εκμεταλλεύονται": "εκμεταλλεύομαι — to exploit"}
})
ITEMS.append({
 "id": "l93-c1-chronotypoi", "title": "Κορυδαλλοί και κουκουβάγιες", "title_en": "Larks and owls", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας διάλεξης για τη χρονοβιολογία σε ένα πανεπιστήμιο.",
 "script": [
  L("Καθηγήτρια", "f", "Όλοι γνωρίζουμε ανθρώπους που ξυπνούν στις έξι γεμάτοι ενέργεια, και άλλους που δεν μπορούν να σκεφτούν καθαρά πριν από το μεσημέρι, αλλά ζωντανεύουν μετά τις δέκα το βράδυ. Στην καθομιλουμένη τούς λέμε «πρωινούς» και «νυχτερινούς»· οι επιστήμονες μιλούν για χρονότυπους, και χρησιμοποιούν συχνά τις εικόνες του κορυδαλλού και της κουκουβάγιας.", "We all know people who wake at six full of energy, and others who can't think clearly before noon but come alive after ten at night. In everyday speech we call them 'morning people' and 'night people'; scientists talk about chronotypes, and often use the images of the lark and the owl."),
  L("Καθηγήτρια", "f", "Ο χρονότυπος δεν είναι θέμα πειθαρχίας ή τεμπελιάς. Καθορίζεται σε μεγάλο βαθμό από το βιολογικό μας ρολόι, το οποίο επηρεάζεται από τα γονίδιά μας, και αλλάζει με την ηλικία. Τα παιδιά είναι συνήθως πρωινά· στην εφηβεία το ρολόι μετατοπίζεται προς τα αργότερα, γι’ αυτό οι έφηβοι δυσκολεύονται τόσο να σηκωθούν για το σχολείο· και με τα χρόνια επιστρέφουμε σταδιακά σε πιο πρωινές συνήθειες.", "Chronotype is not a matter of discipline or laziness. It is largely determined by our biological clock, which is influenced by our genes, and it changes with age. Children are usually early risers; in adolescence the clock shifts later, which is why teenagers find it so hard to get up for school; and over the years we gradually return to earlier habits."),
  L("Καθηγήτρια", "f", "Το πρόβλημα είναι ότι η κοινωνία είναι οργανωμένη κυρίως για τους κορυδαλλούς. Όταν οι νυχτερινοί αναγκάζονται να ξυπνούν νωρίς για τη δουλειά τους και κοιμούνται αργά τα Σαββατοκύριακα, ζουν σε μια μόνιμη διαφορά ώρας, σαν να ταξίδευαν κάθε εβδομάδα σε άλλη ζώνη ώρας. Ο Γερμανός ερευνητής Τιλ Ρένεμπεργκ ονόμασε το φαινόμενο αυτό «κοινωνικό τζετ λαγκ» και το συνέδεσε με την κόπωση, την κακή διάθεση, ακόμη και με προβλήματα υγείας.", "The problem is that society is organised mainly for larks. When owls are forced to wake early for work and sleep late at weekends, they live with a permanent time difference, as if they travelled to another time zone every week. The German researcher Till Roenneberg called this phenomenon 'social jet lag' and linked it to fatigue, low mood and even health problems."),
 ],
 "questions": [
  Q("Τι είναι ο χρονότυπος, σύμφωνα με την καθηγήτρια;", ["Θέμα πειθαρχίας", "Μια συνήθεια που αλλάζει εύκολα", "Κάτι που καθορίζεται σε μεγάλο βαθμό από το βιολογικό μας ρολόι", "Μια επιλογή του καθενός"], 2, "Καθορίζεται σε μεγάλο βαθμό από το βιολογικό μας ρολόι"),
  Q("Γιατί οι έφηβοι δυσκολεύονται να σηκωθούν για το σχολείο;", ["Γιατί κοιμούνται με το κινητό", "Γιατί το βιολογικό τους ρολόι μετατοπίζεται προς τα αργότερα", "Γιατί είναι τεμπέληδες", "Γιατί τρώνε αργά το βράδυ"], 1, "στην εφηβεία το ρολόι μετατοπίζεται προς τα αργότερα"),
  Q("Για ποιους είναι οργανωμένη κυρίως η κοινωνία;", ["Για τους νυχτερινούς", "Για τους εφήβους", "Για τους κορυδαλλούς", "Για τους ηλικιωμένους"], 2, "η κοινωνία είναι οργανωμένη κυρίως για τους κορυδαλλούς"),
  Q("Τι είναι το «κοινωνικό τζετ λαγκ»;", ["Η κούραση μετά από ένα ταξίδι", "Η μόνιμη διαφορά ανάμεσα στο βιολογικό ρολόι και στο πρόγραμμα της δουλειάς", "Η αλλαγή της ώρας δύο φορές τον χρόνο", "Η αϋπνία των ταξιδιωτών"], 1, "ζουν σε μια μόνιμη διαφορά ώρας"),
 ],
 "gloss": {"χρονοβιολογία": "χρονοβιολογία — chronobiology", "ζωντανεύουν": "ζωντανεύω — to come alive", "καθομιλουμένη": "καθομιλουμένη — everyday speech", "χρονότυπους": "χρονότυπος — chronotype", "κορυδαλλού": "κορυδαλλός — lark", "κουκουβάγιας": "κουκουβάγια — owl", "πειθαρχίας": "πειθαρχία — discipline", "γονίδιά": "γονίδιο — gene", "εφηβεία": "εφηβεία — adolescence", "μετατοπίζεται": "μετατοπίζομαι — to shift", "ζώνη ώρας": "ζώνη ώρας — time zone", "κόπωση": "κόπωση — fatigue"}
})

rnd = random.Random(93)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-93.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
