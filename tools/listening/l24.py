# Source for library/listening/listening-24.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l24.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l24-ann-grippi", "title": "Εμβόλιο για τη γρίπη", "title_en": "The flu jab", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση στο ραδιόφωνο για τον αντιγριπικό εμβολιασμό.",
 "script": [
  L("Εκφωνητής", "m", "Ξεκίνησε η φετινή εκστρατεία αντιγριπικού εμβολιασμού. Το εμβόλιο διατίθεται δωρεάν σε όλους τους πολίτες άνω των εξήντα ετών, στις εγκύους, στους χρόνια πάσχοντες και στους εργαζόμενους στον χώρο της υγείας.", "This year's flu vaccination campaign has started. The vaccine is available free of charge to all citizens over sixty, to pregnant women, to the chronically ill and to health workers."),
  L("Εκφωνητής", "m", "Ο εμβολιασμός γίνεται στα φαρμακεία και στα κέντρα υγείας, χωρίς ραντεβού. Χρειάζεται μόνο η ηλεκτρονική συνταγή, την οποία μπορείτε να ζητήσετε από τον γιατρό σας, και ο αριθμός μητρώου κοινωνικής ασφάλισης.", "Vaccination takes place in pharmacies and health centres, without an appointment. All you need is the electronic prescription, which you can ask your doctor for, and your social security number."),
  L("Εκφωνητής", "m", "Οι ειδικοί συνιστούν να γίνει το εμβόλιο έως τα τέλη Νοεμβρίου, καθώς ο οργανισμός χρειάζεται περίπου δύο εβδομάδες για να αναπτύξει προστασία, πριν κορυφωθεί η γρίπη τον Ιανουάριο.", "Experts recommend getting the vaccine by the end of November, as the body needs about two weeks to develop protection before flu peaks in January."),
 ],
 "questions": [
  Q("Σε ποιους διατίθεται δωρεάν το εμβόλιο;", ["Σε όλους τους πολίτες", "Σε όσους είναι άνω των εξήντα, σε εγκύους, σε χρόνια πάσχοντες και σε υγειονομικούς", "Μόνο στα παιδιά", "Μόνο στους εργαζόμενους"], 1, "σε όλους τους πολίτες άνω των εξήντα ετών, στις εγκύους, στους χρόνια πάσχοντες"),
  Q("Τι χρειάζεται κανείς για να εμβολιαστεί;", ["Ραντεβού στο νοσοκομείο", "Την ηλεκτρονική συνταγή και τον αριθμό κοινωνικής ασφάλισης", "Βεβαίωση από τον εργοδότη", "Τίποτα"], 1, "Χρειάζεται μόνο η ηλεκτρονική συνταγή ... και ο αριθμός μητρώου κοινωνικής ασφάλισης"),
  Q("Γιατί προτείνεται να γίνει το εμβόλιο έως τα τέλη Νοεμβρίου;", ["Γιατί μετά τελειώνουν τα εμβόλια", "Γιατί ο οργανισμός χρειάζεται δύο εβδομάδες για να αναπτύξει προστασία", "Γιατί μετά πληρώνεται", "Γιατί κλείνουν τα φαρμακεία"], 1, "ο οργανισμός χρειάζεται περίπου δύο εβδομάδες για να αναπτύξει προστασία"),
 ],
 "gloss": {"αντιγριπικού": "αντιγριπικός — flu (vaccine)", "εκστρατεία": "εκστρατεία — campaign", "εμβολιασμού": "εμβολιασμός — vaccination", "διατίθεται": "διατίθεμαι — to be available", "εγκύους": "έγκυος — pregnant woman", "χρόνια πάσχοντες": "χρόνια πάσχων — chronically ill person", "ηλεκτρονική συνταγή": "ηλεκτρονική συνταγή — e-prescription", "αριθμός μητρώου κοινωνικής ασφάλισης": "ΑΜΚΑ — social security number", "οργανισμός": "οργανισμός — body, organism", "να αναπτύξει": "αναπτύσσω — to develop", "κορυφωθεί": "κορυφώνομαι — to peak"},
})

ITEMS.append({
 "id": "l24-vm-mesitis", "title": "Μήνυμα από τον μεσίτη", "title_en": "A message from the estate agent", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από έναν μεσίτη.",
 "script": [
  L("Μεσίτης", "m", "Καλησπέρα, κυρία Αλεξίου, ο Θοδωρής είμαι από το μεσιτικό γραφείο. Σας παίρνω για το διαμέρισμα στο Παγκράτι που είδαμε την Τρίτη. Μίλησα με τον ιδιοκτήτη και δέχεται να κατεβάσει το ενοίκιο στα επτακόσια πενήντα, αν υπογράψετε συμβόλαιο για τρία χρόνια.", "Good evening, Mrs Alexiou, it's Thodoris from the estate agency. I'm calling about the flat in Pangrati we saw on Tuesday. I spoke to the owner and he agrees to lower the rent to seven hundred and fifty, if you sign a contract for three years."),
  L("Μεσίτης", "m", "Για το θέμα του κλιματιστικού που σας απασχολούσε: θα το αντικαταστήσει ο ίδιος πριν μπείτε. Θα χρειαστεί μια εγγύηση δύο ενοικίων, και η δική μας αμοιβή είναι ένα ενοίκιο, όπως σας είχα πει.", "About the air conditioner that concerned you: he'll replace it himself before you move in. A deposit of two months' rent will be needed, and our fee is one month's rent, as I told you."),
  L("Μεσίτης", "m", "Έχει δει το διαμέρισμα και ένα άλλο ζευγάρι, οπότε αν σας ενδιαφέρει, θα σας πρότεινα να μου απαντήσετε μέχρι αύριο το μεσημέρι.", "Another couple has also seen the flat, so if you're interested, I'd suggest you answer me by tomorrow midday."),
 ],
 "questions": [
  Q("Με ποια προϋπόθεση θα κατεβάσει ο ιδιοκτήτης το ενοίκιο;", ["Αν πληρώσει έξι μήνες μπροστά", "Αν υπογράψει συμβόλαιο για τρία χρόνια", "Αν αναλάβει η ίδια τις επισκευές", "Αν μπει αμέσως"], 1, "αν υπογράψετε συμβόλαιο για τρία χρόνια"),
  Q("Τι θα κάνει ο ιδιοκτήτης με το κλιματιστικό;", ["Θα το αφαιρέσει", "Θα το αντικαταστήσει πριν μπει η ενοικιάστρια", "Θα το επισκευάσει αργότερα", "Θα της ζητήσει να το πληρώσει"], 1, "θα το αντικαταστήσει ο ίδιος πριν μπείτε"),
  Q("Γιατί πρέπει να απαντήσει γρήγορα;", ["Γιατί ο μεσίτης φεύγει για διακοπές", "Γιατί το έχει δει και ένα άλλο ζευγάρι", "Γιατί θα ανέβει το ενοίκιο", "Γιατί ο ιδιοκτήτης θα το πουλήσει"], 1, "Έχει δει το διαμέρισμα και ένα άλλο ζευγάρι"),
 ],
 "gloss": {"μεσίτη": "μεσίτης — estate agent", "μεσιτικό γραφείο": "μεσιτικό γραφείο — estate agency", "να κατεβάσει": "κατεβάζω — to lower", "συμβόλαιο": "συμβόλαιο — contract", "κλιματιστικού": "κλιματιστικό — air conditioner", "σας απασχολούσε": "με απασχολεί — it concerns me", "θα το αντικαταστήσει": "αντικαθιστώ — to replace", "εγγύηση": "εγγύηση — deposit", "αμοιβή": "αμοιβή — fee"},
})

ITEMS.append({
 "id": "l24-dia-doro", "title": "Ένα δώρο χωρίς απόδειξη", "title_en": "A present without a receipt", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα κατάστημα ειδών σπιτιού.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Μου έκαναν δώρο αυτή την καφετιέρα στα γενέθλιά μου, αλλά έχω ήδη μία. Θα ήθελα να την αλλάξω με κάτι άλλο. Δυστυχώς, δεν έχω την απόδειξη.", "Good morning. I was given this coffee maker as a birthday present, but I already have one. I'd like to exchange it for something else. Unfortunately, I don't have the receipt."),
  L("Πωλήτρια", "f", "Χωρίς απόδειξη είναι λίγο δύσκολο, αλλά βλέπω ότι η συσκευασία είναι κλειστή και το προϊόν είναι δικό μας. Μπορώ να σας δώσω ένα πιστωτικό σημείωμα με την τρέχουσα τιμή του, που ισχύει για έξι μήνες. Χρήματα όμως δεν μπορώ να σας επιστρέψω.", "Without a receipt it's a bit difficult, but I see the packaging is sealed and the product is ours. I can give you a credit note at its current price, valid for six months. But I can't give you money back."),
  L("Πελάτης", "m", "Δεν με πειράζει, θα πάρω κάτι άλλο. Η τρέχουσα τιμή είναι η ίδια με αυτή που πλήρωσε ο φίλος μου;", "I don't mind, I'll take something else. Is the current price the same as what my friend paid?"),
  L("Πωλήτρια", "f", "Όχι ακριβώς. Αυτή τη στιγμή έχει έκπτωση είκοσι τοις εκατό, οπότε το σημείωμα θα είναι λίγο μικρότερο από την αρχική τιμή. Αν ο φίλος σας βρει την απόδειξη μέσα στον μήνα, φέρτε τη μου και θα σας δώσω τη διαφορά.", "Not exactly. At the moment it has a twenty per cent discount, so the note will be a bit less than the original price. If your friend finds the receipt within the month, bring it to me and I'll give you the difference."),
 ],
 "questions": [
  Q("Γιατί θέλει να αλλάξει την καφετιέρα;", ["Γιατί είναι χαλασμένη", "Γιατί έχει ήδη μία", "Γιατί δεν του αρέσει το χρώμα", "Γιατί είναι πολύ μεγάλη"], 1, "αλλά έχω ήδη μία"),
  Q("Τι του προσφέρει η πωλήτρια;", ["Επιστροφή χρημάτων", "Ένα πιστωτικό σημείωμα που ισχύει για έξι μήνες", "Μια άλλη καφετιέρα", "Τίποτα, γιατί δεν έχει απόδειξη"], 1, "ένα πιστωτικό σημείωμα με την τρέχουσα τιμή του, που ισχύει για έξι μήνες"),
  Q("Γιατί το σημείωμα θα είναι μικρότερο από την αρχική τιμή;", ["Γιατί η συσκευασία είναι ανοιγμένη", "Γιατί το προϊόν έχει τώρα έκπτωση είκοσι τοις εκατό", "Γιατί χρεώνεται προμήθεια", "Γιατί πέρασε πολύς καιρός"], 1, "Αυτή τη στιγμή έχει έκπτωση είκοσι τοις εκατό"),
 ],
 "gloss": {"ειδών σπιτιού": "είδη σπιτιού — homeware", "καφετιέρα": "καφετιέρα — coffee maker", "απόδειξη": "απόδειξη — receipt", "συσκευασία": "συσκευασία — packaging", "πιστωτικό σημείωμα": "πιστωτικό σημείωμα — credit note", "τρέχουσα": "τρέχων — current", "ισχύει": "ισχύω — to be valid", "έκπτωση": "έκπτωση — discount", "τοις εκατό": "τοις εκατό — per cent", "αρχική": "αρχικός — original", "διαφορά": "διαφορά — difference"},
})

ITEMS.append({
 "id": "l24-dia-internet", "title": "Χωρίς ίντερνετ", "title_en": "No internet", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε ένα τηλεφώνημα στην εξυπηρέτηση πελατών μιας εταιρείας τηλεπικοινωνιών.",
 "script": [
  L("Υπάλληλος", "f", "Εξυπηρέτηση πελατών, καλημέρα σας. Πώς μπορώ να βοηθήσω;", "Customer service, good morning. How can I help?"),
  L("Πελάτης", "m", "Από χθες το απόγευμα δεν έχω καθόλου ίντερνετ στο σπίτι. Δουλεύω από απόσταση, οπότε είναι πολύ σοβαρό πρόβλημα. Έχω ήδη κλείσει και ανοίξει το ρούτερ τρεις φορές.", "Since yesterday afternoon I've had no internet at all at home. I work remotely, so it's a very serious problem. I've already switched the router off and on three times."),
  L("Υπάλληλος", "f", "Λυπάμαι πολύ. Βλέπω ότι υπάρχει βλάβη σε ένα καλώδιο στην περιοχή σας, λόγω εργασιών του δήμου. Οι τεχνικοί μας εκτιμούν ότι η σύνδεση θα αποκατασταθεί μέχρι αύριο το μεσημέρι.", "I'm very sorry. I see there's a fault in a cable in your area, due to council works. Our technicians estimate that the connection will be restored by tomorrow midday."),
  L("Πελάτης", "m", "Αύριο; Και τι θα κάνω μέχρι τότε; Πληρώνω κάθε μήνα για μια υπηρεσία που δεν παίρνω.", "Tomorrow? And what will I do until then? I pay every month for a service I'm not getting."),
  L("Υπάλληλος", "f", "Έχετε δίκιο. Θα σας ενεργοποιήσω τώρα δωρεάν πενήντα γιγαμπάιτ στο κινητό σας, ώστε να μπορείτε να δουλέψετε μέσω αυτού. Επίσης, οι ημέρες χωρίς σύνδεση θα αφαιρεθούν αυτόματα από τον επόμενο λογαριασμό σας.", "You're right. I'll activate fifty gigabytes free on your mobile now, so you can work through it. Also, the days without a connection will be automatically deducted from your next bill."),
 ],
 "questions": [
  Q("Γιατί είναι σοβαρό το πρόβλημα για τον πελάτη;", ["Γιατί έχει παιδιά που κάνουν μάθημα", "Γιατί δουλεύει από απόσταση", "Γιατί βλέπει αγώνα", "Γιατί περιμένει ένα σημαντικό email"], 1, "Δουλεύω από απόσταση"),
  Q("Ποια είναι η αιτία της βλάβης;", ["Το χαλασμένο ρούτερ του πελάτη", "Μια βλάβη σε καλώδιο λόγω εργασιών του δήμου", "Η κακοκαιρία", "Ένας απλήρωτος λογαριασμός"], 1, "υπάρχει βλάβη σε ένα καλώδιο στην περιοχή σας, λόγω εργασιών του δήμου"),
  Q("Τι του προσφέρει η υπάλληλος;", ["Καινούργιο ρούτερ", "Δωρεάν δεδομένα στο κινητό και έκπτωση στον επόμενο λογαριασμό", "Επίσκεψη τεχνικού σήμερα", "Αλλαγή πακέτου"], 1, "πενήντα γιγαμπάιτ στο κινητό σας ... οι ημέρες χωρίς σύνδεση θα αφαιρεθούν"),
 ],
 "gloss": {"εξυπηρέτηση πελατών": "εξυπηρέτηση πελατών — customer service", "τηλεπικοινωνιών": "τηλεπικοινωνίες — telecommunications", "από απόσταση": "από απόσταση — remotely", "ρούτερ": "ρούτερ — router", "βλάβη": "βλάβη — fault", "καλώδιο": "καλώδιο — cable", "εκτιμούν": "εκτιμώ — to estimate", "σύνδεση": "σύνδεση — connection", "θα αποκατασταθεί": "αποκαθίσταμαι — to be restored", "υπηρεσία": "υπηρεσία — service", "σας ενεργοποιήσω": "ενεργοποιώ — to activate", "θα αφαιρεθούν": "αφαιρούμαι — to be deducted"},
})

ITEMS.append({
 "id": "l24-mon-mpalkoni", "title": "Ένας κήπος στο μπαλκόνι", "title_en": "A garden on the balcony", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλάει για τον κήπο που έφτιαξε στο μπαλκόνι της.",
 "script": [
  L("Γυναίκα", "f", "Μένω σε ένα διαμέρισμα στον πέμπτο όροφο, στο κέντρο της Θεσσαλονίκης. Πριν από τρία χρόνια, στο λοκντάουν, ένιωθα ότι πνίγομαι ανάμεσα στο τσιμέντο. Έτσι αγόρασα μερικές γλάστρες και φύτεψα βασιλικό και ντομάτες, χωρίς να έχω ιδέα από κηπουρική.", "I live in a flat on the fifth floor, in the centre of Thessaloniki. Three years ago, in lockdown, I felt I was suffocating among the concrete. So I bought a few pots and planted basil and tomatoes, without any idea about gardening."),
  L("Γυναίκα", "f", "Οι πρώτες ντομάτες ξεράθηκαν, γιατί τις πότιζα το μεσημέρι, στον καυτό ήλιο. Μια ηλικιωμένη γειτόνισσα, που με έβλεπε από απέναντι, μου φώναξε μια μέρα: «Κορίτσι μου, το πρωί τα ποτίζουμε, όχι το μεσημέρι!» Από τότε μου δίνει συμβουλές και σπόρους από το χωριό της.", "My first tomatoes dried up, because I watered them at midday in the scorching sun. An elderly neighbour who watched me from across the street shouted to me one day: 'My girl, we water in the morning, not at midday!' Since then she gives me advice and seeds from her village."),
  L("Γυναίκα", "f", "Σήμερα έχω πάνω από τριάντα γλάστρες: μυρωδικά, πιπεριές, φράουλες, ακόμη και μια μικρή λεμονιά. Δεν τρέφω την οικογένειά μου, φυσικά, αλλά κάθε πρωί πίνω τον καφέ μου ανάμεσα σε πεταλούδες και μέλισσες, στη μέση της πόλης. Και έκανα μια φίλη απέναντι.", "Today I have more than thirty pots: herbs, peppers, strawberries, even a little lemon tree. I don't feed my family, of course, but every morning I drink my coffee among butterflies and bees, in the middle of the city. And I made a friend across the street."),
 ],
 "questions": [
  Q("Γιατί ξεκίνησε να φτιάχνει κήπο στο μπαλκόνι;", ["Για να εξοικονομήσει χρήματα", "Γιατί ένιωθε ότι πνίγεται ανάμεσα στο τσιμέντο", "Γιατί σπούδασε γεωπονία", "Για έναν διαγωνισμό"], 1, "ένιωθα ότι πνίγομαι ανάμεσα στο τσιμέντο"),
  Q("Γιατί ξεράθηκαν οι πρώτες ντομάτες;", ["Γιατί δεν τις πότιζε", "Γιατί τις πότιζε το μεσημέρι στον καυτό ήλιο", "Γιατί έκανε κρύο", "Γιατί τις έφαγαν πουλιά"], 1, "τις πότιζα το μεσημέρι, στον καυτό ήλιο"),
  Q("Τι κέρδισε, εκτός από τα φυτά;", ["Ένα βραβείο", "Μια φίλη, τη γειτόνισσα απέναντι", "Χρήματα από πωλήσεις", "Μια δουλειά σε φυτώριο"], 1, "Και έκανα μια φίλη απέναντι"),
 ],
 "gloss": {"πνίγομαι": "πνίγομαι — to suffocate, drown", "τσιμέντο": "τσιμέντο — concrete", "γλάστρες": "γλάστρα — flowerpot", "φύτεψα": "φυτεύω — to plant", "κηπουρική": "κηπουρική — gardening", "ξεράθηκαν": "ξεραίνομαι — to dry up, wither", "πότιζα": "ποτίζω — to water", "καυτό": "καυτός — scorching", "σπόρους": "σπόρος — seed", "μυρωδικά": "μυρωδικά — herbs", "λεμονιά": "λεμονιά — lemon tree", "τρέφω": "τρέφω — to feed"},
})

ITEMS.append({
 "id": "l24-rep-mani", "title": "Η Μάνη", "title_en": "Mani", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ταξιδιωτικό ρεπορτάζ από τη Μάνη.",
 "script": [
  L("Ρεπόρτερ", "f", "Η Μάνη, η μεσαία χερσόνησος της Πελοποννήσου, είναι ένας τόπος σκληρός και ταυτόχρονα μαγευτικός. Πέτρα, θάλασσα και ελιές: αυτά είναι σχεδόν όλα όσα βλέπει κανείς. Τα χωριά της είναι γεμάτα πέτρινους πύργους, που χτίζονταν από τις οικογένειες για να προστατεύονται στις βεντέτες που κρατούσαν για γενιές.", "Mani, the middle peninsula of the Peloponnese, is a harsh and at the same time enchanting place. Stone, sea and olive trees: that's almost all one sees. Its villages are full of stone towers, which were built by families to protect themselves in feuds that lasted for generations."),
  L("Ρεπόρτερ", "f", "Οι Μανιάτες είναι περήφανοι για την ιστορία τους. Στην Αρεόπολη, στις 17 Μαρτίου 1821, κηρύχθηκε η επανάσταση στη Μάνη, λίγες μέρες πριν από τη γνωστή ημερομηνία της 25ης Μαρτίου. Κάθε χρόνο η επέτειος γιορτάζεται με αναπαράσταση στην πλατεία.", "The Maniots are proud of their history. In Areopoli, on 17 March 1821, the revolution in Mani was declared, a few days before the well-known date of 25 March. Every year the anniversary is celebrated with a re-enactment in the square."),
  L("Ρεπόρτερ", "f", "Λίγα χιλιόμετρα νότια βρίσκονται τα σπήλαια του Διρού, όπου ο επισκέπτης μπαίνει σε βάρκα και διασχίζει υπόγειες λίμνες ανάμεσα σε σταλακτίτες. Τα τελευταία χρόνια πολλοί παλιοί πύργοι έχουν αναστηλωθεί και έχουν γίνει ξενώνες.", "A few kilometres south are the Diros caves, where visitors get into a boat and cross underground lakes among stalactites. In recent years many old towers have been restored and turned into guesthouses."),
 ],
 "questions": [
  Q("Γιατί χτίζονταν οι πέτρινοι πύργοι;", ["Για να φυλάγονται τα σιτηρά", "Για να προστατεύονται οι οικογένειες στις βεντέτες", "Ως φάροι για τα πλοία", "Ως εκκλησίες"], 1, "για να προστατεύονται στις βεντέτες"),
  Q("Τι έγινε στην Αρεόπολη στις 17 Μαρτίου 1821;", ["Υπογράφηκε μια συνθήκη", "Κηρύχθηκε η επανάσταση στη Μάνη", "Χτίστηκε ο πρώτος πύργος", "Έγινε μια μεγάλη μάχη με τους Βενετούς"], 1, "κηρύχθηκε η επανάσταση στη Μάνη"),
  Q("Πώς επισκέπτεται κανείς τα σπήλαια του Διρού;", ["Με τα πόδια", "Με βάρκα", "Με τελεφερίκ", "Κολυμπώντας"], 1, "ο επισκέπτης μπαίνει σε βάρκα"),
 ],
 "gloss": {"χερσόνησος": "χερσόνησος — peninsula", "σκληρός": "σκληρός — harsh", "μαγευτικός": "μαγευτικός — enchanting", "πύργους": "πύργος — tower", "βεντέτες": "βεντέτα — (blood) feud", "κηρύχθηκε": "κηρύσσομαι — to be declared", "επέτειος": "επέτειος — anniversary", "αναπαράσταση": "αναπαράσταση — re-enactment", "σπήλαια": "σπήλαιο — cave", "διασχίζει": "διασχίζω — to cross", "υπόγειες": "υπόγειος — underground", "σταλακτίτες": "σταλακτίτης — stalactite", "έχουν αναστηλωθεί": "αναστηλώνομαι — to be restored"},
})

ITEMS.append({
 "id": "l24-rep-spinalonga", "title": "Η Σπιναλόγκα", "title_en": "Spinalonga", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τη Σπιναλόγκα, ένα νησάκι κοντά στην Ελούντα της Κρήτης.",
 "script": [
  L("Ρεπόρτερ", "m", "Από την Πλάκα, απέναντι από την Ελούντα, μια βάρκα χρειάζεται λίγα λεπτά για να φτάσει στη Σπιναλόγκα. Οι Βενετοί έχτισαν εδώ ένα ισχυρό φρούριο τον δέκατο έκτο αιώνα, που άντεξε για δεκαετίες ακόμη και μετά την κατάκτηση της υπόλοιπης Κρήτης από τους Οθωμανούς.", "From Plaka, opposite Elounda, a boat needs a few minutes to reach Spinalonga. The Venetians built a strong fortress here in the sixteenth century, which held out for decades even after the rest of Crete was conquered by the Ottomans."),
  L("Ρεπόρτερ", "m", "Η πιο σκοτεινή σελίδα της ιστορίας του, όμως, γράφτηκε τον εικοστό αιώνα. Από το 1903 ως το 1957, το νησάκι λειτούργησε ως λεπροκομείο. Οι ασθενείς απομονώνονταν εδώ, μακριά από τις οικογένειές τους, και πολλοί δεν έφυγαν ποτέ. Η λειτουργία του σταμάτησε όταν η ασθένεια άρχισε να θεραπεύεται με φάρμακα.", "The darkest page of its history, however, was written in the twentieth century. From 1903 to 1957 the islet operated as a leper colony. Patients were isolated here, far from their families, and many never left. It stopped operating when the disease began to be treated with medicines."),
  L("Ρεπόρτερ", "m", "Σήμερα η Σπιναλόγκα είναι ένας από τους πιο πολυσύχναστους αρχαιολογικούς χώρους της Κρήτης. Τον αριθμό των επισκεπτών τον αύξησε πολύ ένα μυθιστόρημα της Βρετανίδας συγγραφέως Βικτόρια Χίσλοπ, που έγινε στη συνέχεια και τηλεοπτική σειρά. Οι ξεναγοί, πάντως, ζητούν από τους επισκέπτες να θυμούνται ότι περπατούν σε έναν τόπο πόνου.", "Today Spinalonga is one of the busiest archaeological sites in Crete. The number of visitors was greatly increased by a novel by the British author Victoria Hislop, which was later also made into a television series. The guides, however, ask visitors to remember that they are walking in a place of suffering."),
 ],
 "questions": [
  Q("Τι ήταν ιδιαίτερο στο βενετικό φρούριο;", ["Ότι χτίστηκε από τους Οθωμανούς", "Ότι άντεξε για δεκαετίες μετά την κατάκτηση της υπόλοιπης Κρήτης", "Ότι καταστράφηκε από σεισμό", "Ότι ήταν το μεγαλύτερο της Ευρώπης"], 1, "άντεξε για δεκαετίες ακόμη και μετά την κατάκτηση της υπόλοιπης Κρήτης"),
  Q("Γιατί σταμάτησε η λειτουργία του λεπροκομείου;", ["Γιατί έκλεισε το νησί για τουρισμό", "Γιατί η ασθένεια άρχισε να θεραπεύεται με φάρμακα", "Λόγω πολέμου", "Γιατί οι ασθενείς μεταφέρθηκαν στην Αθήνα"], 1, "όταν η ασθένεια άρχισε να θεραπεύεται με φάρμακα"),
  Q("Τι ζητούν οι ξεναγοί από τους επισκέπτες;", ["Να μη βγάζουν φωτογραφίες", "Να θυμούνται ότι περπατούν σε έναν τόπο πόνου", "Να διαβάσουν το μυθιστόρημα", "Να μείνουν όλη μέρα"], 1, "να θυμούνται ότι περπατούν σε έναν τόπο πόνου"),
 ],
 "gloss": {"νησάκι": "νησάκι — islet", "φρούριο": "φρούριο — fortress", "άντεξε": "αντέχω — to hold out", "κατάκτηση": "κατάκτηση — conquest", "σκοτεινή": "σκοτεινός — dark", "λεπροκομείο": "λεπροκομείο — leper colony", "απομονώνονταν": "απομονώνομαι — to be isolated", "ασθένεια": "ασθένεια — disease", "να θεραπεύεται": "θεραπεύομαι — to be cured, treated", "πολυσύχναστους": "πολυσύχναστος — busy, much-visited", "μυθιστόρημα": "μυθιστόρημα — novel", "τηλεοπτική σειρά": "τηλεοπτική σειρά — TV series", "πόνου": "πόνος — pain, suffering"},
})

ITEMS.append({
 "id": "l24-int-sezon", "title": "Μια σεζόν στο νησί", "title_en": "A season on the island", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια νέα που δουλεύει κάθε καλοκαίρι σε ένα νησί.",
 "script": [
  L("Δημοσιογράφος", "m", "Εδώ και πέντε καλοκαίρια δουλεύεις σερβιτόρα στη Μύκονο. Γιατί;", "For five summers you've been working as a waitress on Mykonos. Why?"),
  L("Σερβιτόρα", "f", "Σπουδάζω νοσηλευτική στα Γιάννενα, και με τα χρήματα της σεζόν πληρώνω το ενοίκιο και τα έξοδά μου για όλο τον χειμώνα. Τα φιλοδωρήματα είναι καλά, και μαθαίνω γλώσσες χωρίς να το καταλάβω: τώρα μιλάω αγγλικά, λίγα ιταλικά και μερικές φράσεις στα εβραϊκά.", "I'm studying nursing in Ioannina, and with the money from the season I pay my rent and expenses for the whole winter. The tips are good, and I learn languages without noticing: now I speak English, a little Italian and a few phrases of Hebrew."),
  L("Δημοσιογράφος", "m", "Ποια είναι η πιο δύσκολη πλευρά;", "What's the hardest side of it?"),
  L("Σερβιτόρα", "f", "Η στέγη. Τα ενοίκια στο νησί είναι τρελά, και ένα δωμάτιο μπορεί να κοστίζει όσο ο μισθός σου. Φέτος μένουμε τέσσερις κοπέλες σε ένα δωμάτιο που παρέχει το εστιατόριο. Δουλεύουμε δώδεκα ώρες την ημέρα, χωρίς ρεπό τον Αύγουστο. Τον Σεπτέμβριο είμαι εξαντλημένη, αλλά όταν γυρίζω στη σχολή νιώθω ότι έχω κερδίσει την ανεξαρτησία μου.", "Accommodation. Rents on the island are crazy, and a room can cost as much as your salary. This year four of us girls are staying in one room provided by the restaurant. We work twelve hours a day, with no day off in August. By September I'm exhausted, but when I go back to university I feel I've earned my independence."),
 ],
 "questions": [
  Q("Τι πληρώνει με τα χρήματα της σεζόν;", ["Ένα ταξίδι στο εξωτερικό", "Το ενοίκιο και τα έξοδά της για όλο τον χειμώνα", "Ένα αυτοκίνητο", "Τα δίδακτρα ενός ιδιωτικού πανεπιστημίου"], 1, "πληρώνω το ενοίκιο και τα έξοδά μου για όλο τον χειμώνα"),
  Q("Ποια θεωρεί την πιο δύσκολη πλευρά της δουλειάς;", ["Τους πελάτες", "Τη στέγη", "Τα φιλοδωρήματα", "Τη ζέστη"], 1, "Η στέγη"),
  Q("Πώς νιώθει όταν γυρίζει στη σχολή;", ["Ότι έχασε το καλοκαίρι", "Ότι έχει κερδίσει την ανεξαρτησία της", "Ότι θέλει να αφήσει τις σπουδές", "Ότι δεν θα ξαναπάει"], 1, "νιώθω ότι έχω κερδίσει την ανεξαρτησία μου"),
 ],
 "gloss": {"σεζόν": "σεζόν — (tourist) season", "νοσηλευτική": "νοσηλευτική — nursing", "έξοδά": "έξοδα — expenses", "φιλοδωρήματα": "φιλοδώρημα — tip", "εβραϊκά": "εβραϊκά — Hebrew", "στέγη": "στέγη — accommodation, housing", "παρέχει": "παρέχω — to provide", "ρεπό": "ρεπό — day off", "εξαντλημένη": "εξαντλημένος — exhausted", "ανεξαρτησία": "ανεξαρτησία — independence"},
})

ITEMS.append({
 "id": "l24-mon-venizelos", "title": "Ο Ελευθέριος Βενιζέλος", "title_en": "Eleftherios Venizelos", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για τον Ελευθέριο Βενιζέλο.",
 "script": [
  L("Ιστορικός", "f", "Λίγοι πολιτικοί άφησαν τόσο βαθύ αποτύπωμα στη σύγχρονη Ελλάδα όσο ο Ελευθέριος Βενιζέλος, και λίγοι δίχασαν τόσο έντονα τη χώρα. Γεννημένος το 1864 στις Μουρνιές, κοντά στα Χανιά, έγινε γνωστός ως ηγέτης του κρητικού αγώνα για την ένωση με την Ελλάδα.", "Few politicians left such a deep mark on modern Greece as Eleftherios Venizelos, and few divided the country so sharply. Born in 1864 in Mournies near Chania, he became known as a leader of the Cretan struggle for union with Greece."),
  L("Ιστορικός", "f", "Το 1910 κλήθηκε στην Αθήνα, και μέσα σε λίγα χρόνια μεταμόρφωσε το κράτος: αναθεώρησε το σύνταγμα, αναδιοργάνωσε τον στρατό και τη διοίκηση. Στους Βαλκανικούς πολέμους του 1912 και του 1913 η Ελλάδα σχεδόν διπλασίασε την έκτασή της, προσαρτώντας τη Μακεδονία, την Ήπειρο, την Κρήτη και πολλά νησιά του Αιγαίου.", "In 1910 he was called to Athens, and within a few years he transformed the state: he revised the constitution and reorganised the army and the administration. In the Balkan Wars of 1912 and 1913 Greece almost doubled its territory, annexing Macedonia, Epirus, Crete and many Aegean islands."),
  L("Ιστορικός", "f", "Ο Πρώτος Παγκόσμιος Πόλεμος, ωστόσο, τον έφερε σε μετωπική σύγκρουση με τον βασιλιά Κωνσταντίνο. Ο Βενιζέλος ήθελε την είσοδο της χώρας στον πόλεμο στο πλευρό της Αντάντ, ενώ ο βασιλιάς επέμενε στην ουδετερότητα. Η σύγκρουση οδήγησε στον Εθνικό Διχασμό, με δύο κυβερνήσεις, μία στην Αθήνα και μία στη Θεσσαλονίκη, και άφησε πληγές που δεν έκλεισαν για δεκαετίες.", "The First World War, however, brought him into head-on conflict with King Constantine. Venizelos wanted the country to enter the war on the side of the Entente, while the king insisted on neutrality. The conflict led to the National Schism, with two governments, one in Athens and one in Thessaloniki, and left wounds that did not heal for decades."),
  L("Ιστορικός", "f", "Το 1920, λίγους μήνες αφού υπέγραψε τη Συνθήκη των Σεβρών, που φαινόταν να πραγματοποιεί το όραμα της «Μεγάλης Ιδέας», έχασε τις εκλογές. Το παράδοξο αυτό λέει πολλά για τα όρια της προσωπικής ακτινοβολίας: ένας λαός κουρασμένος από δέκα χρόνια πολέμων ψήφισε την ειρήνη, ή αυτό που νόμιζε ότι ήταν ειρήνη.", "In 1920, a few months after signing the Treaty of Sèvres, which seemed to fulfil the vision of the 'Great Idea', he lost the elections. This paradox says a lot about the limits of personal charisma: a people tired of ten years of wars voted for peace, or for what it thought was peace."),
 ],
 "questions": [
  Q("Πώς έγινε αρχικά γνωστός ο Βενιζέλος;", ["Ως στρατιωτικός στη Θεσσαλονίκη", "Ως ηγέτης του κρητικού αγώνα για την ένωση με την Ελλάδα", "Ως δικηγόρος στην Αθήνα", "Ως διπλωμάτης στο Λονδίνο"], 1, "έγινε γνωστός ως ηγέτης του κρητικού αγώνα για την ένωση με την Ελλάδα"),
  Q("Ποιο ήταν το αποτέλεσμα των Βαλκανικών πολέμων για την Ελλάδα;", ["Έχασε εδάφη", "Σχεδόν διπλασίασε την έκτασή της", "Έγινε δημοκρατία", "Χάθηκε η Κρήτη"], 1, "η Ελλάδα σχεδόν διπλασίασε την έκτασή της"),
  Q("Ποια ήταν η αιτία της σύγκρουσης με τον βασιλιά Κωνσταντίνο;", ["Η διαφωνία για το σύνταγμα", "Η διαφωνία για την είσοδο της χώρας στον Α΄ Παγκόσμιο Πόλεμο", "Η Μικρασιατική Καταστροφή", "Το εκλογικό σύστημα"], 1, "Ο Βενιζέλος ήθελε την είσοδο της χώρας στον πόλεμο ... ενώ ο βασιλιάς επέμενε στην ουδετερότητα"),
  Q("Πώς εξηγεί η ιστορικός την ήττα του στις εκλογές του 1920;", ["Με σκάνδαλα διαφθοράς", "Με την κούραση ενός λαού από δέκα χρόνια πολέμων", "Με την παρέμβαση ξένων δυνάμεων", "Με την αρρώστια του"], 1, "ένας λαός κουρασμένος από δέκα χρόνια πολέμων ψήφισε την ειρήνη"),
 ],
 "gloss": {"αποτύπωμα": "αποτύπωμα — mark, imprint", "δίχασαν": "διχάζω — to divide", "ένωση": "ένωση — union", "αναθεώρησε": "αναθεωρώ — to revise", "αναδιοργάνωσε": "αναδιοργανώνω — to reorganise", "διπλασίασε": "διπλασιάζω — to double", "έκτασή": "έκταση — area, territory", "προσαρτώντας": "προσαρτώ — to annex", "μετωπική": "μετωπικός — head-on", "Αντάντ": "Αντάντ — the Entente", "ουδετερότητα": "ουδετερότητα — neutrality", "Εθνικό Διχασμό": "Εθνικός Διχασμός — National Schism", "πληγές": "πληγή — wound", "όραμα": "όραμα — vision", "Μεγάλης Ιδέας": "Μεγάλη Ιδέα — the 'Great Idea' (irredentist vision)", "παράδοξο": "παράδοξο — paradox", "ακτινοβολίας": "ακτινοβολία — radiance, charisma"},
})

ITEMS.append({
 "id": "l24-int-anavoli", "title": "Γιατί τα αφήνουμε για αύριο;", "title_en": "Why do we put things off?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν ψυχολόγο για την αναβλητικότητα.",
 "script": [
  L("Δημοσιογράφος", "f", "Οι περισσότεροι πιστεύουν ότι η αναβλητικότητα είναι απλώς τεμπελιά. Έχουν δίκιο;", "Most people believe procrastination is simply laziness. Are they right?"),
  L("Ψυχολόγος", "m", "Όχι. Ο τεμπέλης δεν θέλει να κάνει τίποτα και δεν ανησυχεί γι' αυτό. Ο αναβλητικός θέλει να κάνει κάτι, ξέρει ότι πρέπει, και όμως το αναβάλλει, νιώθοντας συχνά ενοχές. Οι έρευνες δείχνουν ότι η αναβλητικότητα είναι κυρίως πρόβλημα διαχείρισης συναισθημάτων, όχι χρόνου. Αποφεύγουμε μια εργασία επειδή μας προκαλεί άγχος, βαρεμάρα ή φόβο αποτυχίας, και στρεφόμαστε σε κάτι που μας ανακουφίζει άμεσα.", "No. The lazy person doesn't want to do anything and doesn't worry about it. The procrastinator wants to do something, knows they must, and yet puts it off, often feeling guilty. Research shows procrastination is mainly a problem of managing emotions, not time. We avoid a task because it causes us anxiety, boredom or fear of failure, and we turn to something that gives us immediate relief."),
  L("Δημοσιογράφος", "f", "Και ο φόβος της αποτυχίας πώς συνδέεται;", "And how is the fear of failure connected?"),
  L("Ψυχολόγος", "m", "Πολύ συχνά οι αναβλητικοί είναι τελειομανείς. Αν δεν ξεκινήσω, δεν μπορώ να αποτύχω· και αν τελικά δουλέψω την τελευταία νύχτα και το αποτέλεσμα δεν είναι καλό, έχω μια έτοιμη δικαιολογία: «Δεν είχα χρόνο». Είναι ένας μηχανισμός προστασίας της αυτοεκτίμησης, που όμως μακροπρόθεσμα την υπονομεύει.", "Very often procrastinators are perfectionists. If I don't start, I can't fail; and if I end up working the last night and the result isn't good, I have a ready excuse: 'I didn't have time.' It's a mechanism for protecting self-esteem which in the long run undermines it."),
  L("Ψυχολόγος", "m", "Η πιο αποτελεσματική συμβουλή είναι απλή: μην προσπαθείτε να τελειώσετε, προσπαθήστε να ξεκινήσετε. Δεσμευτείτε για δέκα λεπτά μόνο. Συνήθως το δυσκολότερο κομμάτι είναι η αρχή· όταν ξεκινήσουμε, το άγχος μειώνεται. Και να είστε επιεικείς με τον εαυτό σας: όσοι συγχωρούν τον εαυτό τους για μια αναβολή, αναβάλλουν λιγότερο την επόμενη φορά.", "The most effective advice is simple: don't try to finish, try to start. Commit to ten minutes only. Usually the hardest part is the beginning; once we start, the anxiety drops. And be lenient with yourselves: those who forgive themselves for putting something off procrastinate less the next time."),
 ],
 "questions": [
  Q("Ποια είναι η διαφορά ανάμεσα στον τεμπέλη και στον αναβλητικό;", ["Δεν υπάρχει διαφορά", "Ο αναβλητικός θέλει να κάνει κάτι και νιώθει ενοχές όταν το αναβάλλει", "Ο τεμπέλης νιώθει περισσότερες ενοχές", "Ο αναβλητικός δεν ανησυχεί καθόλου"], 1, "Ο αναβλητικός θέλει να κάνει κάτι ... νιώθοντας συχνά ενοχές"),
  Q("Σύμφωνα με τις έρευνες, η αναβλητικότητα είναι κυρίως πρόβλημα", ["διαχείρισης χρόνου", "διαχείρισης συναισθημάτων", "νοημοσύνης", "κούρασης"], 1, "είναι κυρίως πρόβλημα διαχείρισης συναισθημάτων, όχι χρόνου"),
  Q("Γιατί, κατά τον ψυχολόγο, οι τελειομανείς αναβάλλουν;", ["Γιατί έχουν πολλή δουλειά", "Για να προστατεύσουν την αυτοεκτίμησή τους από την αποτυχία", "Γιατί βαριούνται", "Γιατί δουλεύουν καλύτερα τη νύχτα"], 1, "Είναι ένας μηχανισμός προστασίας της αυτοεκτίμησης"),
  Q("Ποια είναι η πιο αποτελεσματική συμβουλή του;", ["Να φτιάχνουμε λεπτομερή προγράμματα", "Να προσπαθούμε να ξεκινήσουμε, δεσμευόμενοι για δέκα λεπτά", "Να δουλεύουμε μόνο τη νύχτα", "Να τιμωρούμε τον εαυτό μας"], 1, "μην προσπαθείτε να τελειώσετε, προσπαθήστε να ξεκινήσετε. Δεσμευτείτε για δέκα λεπτά μόνο"),
 ],
 "gloss": {"αναβλητικότητα": "αναβλητικότητα — procrastination", "τεμπελιά": "τεμπελιά — laziness", "αναβάλλει": "αναβάλλω — to put off, postpone", "ενοχές": "ενοχή — guilt", "διαχείρισης": "διαχείριση — management", "αποτυχίας": "αποτυχία — failure", "ανακουφίζει": "ανακουφίζω — to relieve", "τελειομανείς": "τελειομανής — perfectionist", "δικαιολογία": "δικαιολογία — excuse", "αυτοεκτίμησης": "αυτοεκτίμηση — self-esteem", "μακροπρόθεσμα": "μακροπρόθεσμα — in the long run", "υπονομεύει": "υπονομεύω — to undermine", "Δεσμευτείτε": "δεσμεύομαι — to commit", "επιεικείς": "επιεικής — lenient", "συγχωρούν": "συγχωρώ — to forgive"},
})
rnd = random.Random(24)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-24.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
