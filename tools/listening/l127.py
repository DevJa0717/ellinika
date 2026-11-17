# Source for library/listening/listening-127.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l127.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l127-ann-imera-karieras", "title": "Ημέρα καριέρας στο πανεπιστήμιο", "title_en": "Careers day at the university", "type": "announcement", "level": "B2",
 "context_el": "Είστε φοιτητής. Ακούτε μια ανακοίνωση από τα μεγάφωνα στο κεντρικό κτίριο του πανεπιστημίου.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί φοιτητές, την Τετάρτη από τις δέκα το πρωί ως τις τέσσερις το απόγευμα θα γίνει στο αμφιθέατρο και στο φουαγιέ η ετήσια Ημέρα Καριέρας. Περισσότερες από σαράντα εταιρείες και οργανισμοί θα έχουν περίπτερα, όπου μπορείτε να ενημερωθείτε για θέσεις εργασίας και πρακτικής άσκησης.", "Dear students, on Wednesday from ten in the morning until four in the afternoon the annual Careers Day will take place in the lecture theatre and the foyer. More than forty companies and organisations will have stands, where you can find out about jobs and internships."),
  L("Εκφωνήτρια", "f", "Σας συμβουλεύουμε να φέρετε μαζί σας αρκετά αντίγραφα του βιογραφικού σας. Αν θέλετε να το ελέγξει κάποιος πριν από την εκδήλωση, το Γραφείο Διασύνδεσης δέχεται φοιτητές χωρίς ραντεβού, από Δευτέρα ως Τρίτη, στον πρώτο όροφο.", "We advise you to bring several copies of your CV. If you'd like someone to check it before the event, the Careers Office sees students without an appointment, Monday to Tuesday, on the first floor."),
  L("Εκφωνήτρια", "f", "Στις δώδεκα, στην αίθουσα δύο, θα γίνει εργαστήριο για τις συνεντεύξεις εργασίας. Οι θέσεις είναι περιορισμένες, γι' αυτό απαιτείται δήλωση συμμετοχής μέσω της ηλεκτρονικής πλατφόρμας του πανεπιστημίου. Σας περιμένουμε!", "At twelve, in room two, there will be a workshop on job interviews. Places are limited, so you need to register through the university's online platform. We look forward to seeing you!"),
 ],
 "questions": [
  Q("Τι θα βρουν οι φοιτητές στα περίπτερα;", ["Βιβλία σε χαμηλές τιμές", "Πληροφορίες για θέσεις εργασίας και πρακτικής άσκησης", "Δωρεάν φαγητό", "Πληροφορίες για μεταπτυχιακά στο εξωτερικό"], 1, "θέσεις εργασίας και πρακτικής άσκησης"),
  Q("Τι προσφέρει το Γραφείο Διασύνδεσης πριν από την εκδήλωση;", ["Δωρεάν φωτογραφίες για το βιογραφικό", "Μαθήματα ξένων γλωσσών", "Έλεγχο του βιογραφικού χωρίς ραντεβού", "Εισιτήρια για την εκδήλωση"], 2, "το Γραφείο Διασύνδεσης δέχεται φοιτητές χωρίς ραντεβού"),
  Q("Τι χρειάζεται για το εργαστήριο των συνεντεύξεων;", ["Δήλωση συμμετοχής μέσω της ηλεκτρονικής πλατφόρμας", "Ένα βιογραφικό στα αγγλικά", "Συστατική επιστολή από καθηγητή", "Πληρωμή μικρού ποσού"], 0, "απαιτείται δήλωση συμμετοχής μέσω της ηλεκτρονικής πλατφόρμας του πανεπιστημίου"),
 ],
 "gloss": {"αμφιθέατρο": "αμφιθέατρο — lecture theatre", "φουαγιέ": "φουαγιέ — foyer", "ετήσια": "ετήσιος — annual", "Ημέρα Καριέρας": "Ημέρα Καριέρας — careers day", "περίπτερα": "περίπτερο — stand, stall", "πρακτικής άσκησης": "πρακτική άσκηση — internship, work placement", "αντίγραφα": "αντίγραφο — copy", "βιογραφικού": "βιογραφικό — CV", "Γραφείο Διασύνδεσης": "Γραφείο Διασύνδεσης — university careers office", "εργαστήριο": "εργαστήριο — workshop", "συνεντεύξεις εργασίας": "συνέντευξη εργασίας — job interview", "πλατφόρμας": "πλατφόρμα — platform"}
})

ITEMS.append({
 "id": "l127-vm-fysiotherapeftria", "title": "Μήνυμα από τη φυσιοθεραπεύτρια", "title_en": "A message from the physiotherapist", "type": "voicemail", "level": "B2",
 "context_el": "Κάνετε φυσιοθεραπεία για τον ώμο σας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Φυσιοθεραπεύτρια", "f", "Καλησπέρα σας, η Αλεξάνδρα είμαι, από το φυσιοθεραπευτήριο. Σας πήρα γιατί αύριο έχω ένα σεμινάριο και πρέπει να μεταφέρουμε τη συνεδρία σας. Μπορώ να σας δω είτε την Πέμπτη στις έξι το απόγευμα είτε την Παρασκευή στις εννιά το πρωί.", "Good evening, it's Alexandra from the physiotherapy clinic. I'm calling because tomorrow I have a seminar and we need to move your session. I can see you either on Thursday at six in the evening or on Friday at nine in the morning."),
  L("Φυσιοθεραπεύτρια", "f", "Στο μεταξύ, συνεχίστε κανονικά τις ασκήσεις με το λάστιχο, δύο φορές τη μέρα. Αν όμως νιώσετε οξύ πόνο, σταματήστε αμέσως και βάλτε πάγο για δέκα λεπτά. Μην κουβαλάτε ακόμα βάρη με το δεξί χέρι, ούτε καν τις σακούλες από το σούπερ μάρκετ.", "In the meantime, carry on with the exercises with the band as usual, twice a day. But if you feel sharp pain, stop immediately and apply ice for ten minutes. Don't carry weights with your right arm yet, not even the supermarket bags."),
  L("Φυσιοθεραπεύτρια", "f", "Και κάτι ακόμα: για την επόμενη συνεδρία φέρτε μου τη μαγνητική τομογραφία, γιατί θέλω να τη δω πριν προχωρήσουμε σε πιο δύσκολες ασκήσεις. Πείτε μου ποια μέρα σας βολεύει. Ευχαριστώ!", "And one more thing: for the next session bring me the MRI scan, because I want to look at it before we move on to harder exercises. Tell me which day suits you. Thank you!"),
 ],
 "questions": [
  Q("Γιατί πρέπει να μεταφερθεί η συνεδρία;", ["Γιατί η φυσιοθεραπεύτρια είναι άρρωστη", "Γιατί η φυσιοθεραπεύτρια έχει σεμινάριο", "Γιατί κλείνει το φυσιοθεραπευτήριο", "Γιατί ο ασθενής ζήτησε αλλαγή"], 1, "αύριο έχω ένα σεμινάριο"),
  Q("Τι πρέπει να κάνει ο ασθενής αν νιώσει οξύ πόνο;", ["Να πάρει ένα παυσίπονο", "Να τηλεφωνήσει στον γιατρό", "Να σταματήσει και να βάλει πάγο για δέκα λεπτά", "Να κάνει τις ασκήσεις πιο αργά"], 2, "σταματήστε αμέσως και βάλτε πάγο για δέκα λεπτά"),
  Q("Τι πρέπει να φέρει στην επόμενη συνεδρία;", ["Τη μαγνητική τομογραφία", "Το λάστιχο των ασκήσεων", "Μια πετσέτα", "Τη συνταγή του γιατρού"], 0, "φέρτε μου τη μαγνητική τομογραφία"),
 ],
 "gloss": {"φυσιοθεραπεία": "φυσιοθεραπεία — physiotherapy", "ώμο": "ώμος — shoulder", "φυσιοθεραπευτήριο": "φυσιοθεραπευτήριο — physiotherapy clinic", "σεμινάριο": "σεμινάριο — seminar", "συνεδρία": "συνεδρία — session", "λάστιχο": "λάστιχο — (resistance) band", "οξύ πόνο": "οξύς πόνος — sharp pain", "πάγο": "πάγος — ice", "βάρη": "βάρος — weight", "μαγνητική τομογραφία": "μαγνητική τομογραφία — MRI scan", "βολεύει": "βολεύει — it suits"}
})

ITEMS.append({
 "id": "l127-dial-enydreio", "title": "Ένα ενυδρείο για το σαλόνι;", "title_en": "An aquarium for the living room?", "type": "dialogue", "level": "B2",
 "context_el": "Ο Παύλος θέλει να αγοράσει ένα ενυδρείο. Το συζητά με τη σύντροφό του, τη Δέσποινα.",
 "script": [
  L("Παύλος", "m", "Δέσποινα, σκέφτομαι να πάρουμε ένα ενυδρείο για το σαλόνι. Έχω διαβάσει ότι το να κοιτάζεις τα ψάρια χαλαρώνει, και θα ήταν ωραίο και για τον μικρό, να μάθει να φροντίζει ένα ζωντανό πλάσμα.", "Despina, I'm thinking we should get an aquarium for the living room. I've read that watching fish is relaxing, and it would be nice for the little one too, to learn to look after a living creature."),
  L("Δέσποινα", "f", "Ωραία ακούγεται, αλλά ποιος θα το καθαρίζει; Θυμάσαι το χρυσόψαρο που είχαμε στη φοιτητική εστία; Μετά από δύο εβδομάδες το νερό ήταν πράσινο, και το καημένο το ψάρι επέζησε μόνο χάρη στη συγκάτοικό μου.", "Sounds nice, but who's going to clean it? Do you remember the goldfish we had in the student residence? After two weeks the water was green, and the poor fish only survived thanks to my flatmate."),
  L("Παύλος", "m", "Ήμουν είκοσι χρονών τότε! Τώρα έχω ρωτήσει σε ένα κατάστημα. Μου είπαν ότι με ένα καλό φίλτρο αρκεί να αλλάζεις το ένα τέταρτο του νερού κάθε δύο εβδομάδες. Και προτείνουν να ξεκινήσουμε με λίγα, ανθεκτικά ψάρια.", "I was twenty then! Now I've asked at a shop. They told me that with a good filter it's enough to change a quarter of the water every two weeks. And they suggest we start with a few hardy fish."),
  L("Δέσποινα", "f", "Εντάξει, αλλά με έναν όρο: θα φτιάξεις ένα πρόγραμμα με τις δουλειές του ενυδρείου και θα το κρεμάσεις στο ψυγείο. Αν ο μικρός ταΐζει τα ψάρια και εσύ καθαρίζεις, συμφωνώ.", "OK, but on one condition: you'll make a schedule of the aquarium chores and hang it on the fridge. If the little one feeds the fish and you do the cleaning, I agree."),
 ],
 "questions": [
  Q("Γιατί θέλει ο Παύλος ένα ενυδρείο;", ["Γιατί του το χάρισε ένας φίλος", "Γιατί χαλαρώνει και θα μάθει στο παιδί να φροντίζει ένα ζωντανό πλάσμα", "Γιατί το σαλόνι είναι άδειο", "Γιατί η Δέσποινα αγαπά τα ψάρια"], 1, "θα ήταν ωραίο και για τον μικρό, να μάθει να φροντίζει ένα ζωντανό πλάσμα"),
  Q("Τι θυμίζει η Δέσποινα στον Παύλο;", ["Ότι είναι αλλεργικός", "Ότι το σπίτι είναι μικρό", "Το χρυσόψαρο της φοιτητικής εστίας και το πράσινο νερό", "Ότι τα ενυδρεία είναι ακριβά"], 2, "Μετά από δύο εβδομάδες το νερό ήταν πράσινο"),
  Q("Με ποιον όρο συμφωνεί η Δέσποινα;", ["Να φτιάξει ο Παύλος ένα πρόγραμμα με τις δουλειές και να καθαρίζει εκείνος", "Να πάρουν μόνο ένα ψάρι", "Να μπει το ενυδρείο στο δωμάτιο του παιδιού", "Να το πληρώσει ο Παύλος"], 0, "θα φτιάξεις ένα πρόγραμμα με τις δουλειές του ενυδρείου"),
 ],
 "gloss": {"ενυδρείο": "ενυδρείο — aquarium", "χαλαρώνει": "χαλαρώνω — to relax", "πλάσμα": "πλάσμα — creature", "χρυσόψαρο": "χρυσόψαρο — goldfish", "φοιτητική εστία": "φοιτητική εστία — student residence", "επέζησε": "επιζώ — to survive", "συγκάτοικό": "συγκάτοικος — flatmate", "φίλτρο": "φίλτρο — filter", "τέταρτο": "τέταρτο — quarter", "ανθεκτικά": "ανθεκτικός — hardy, resistant", "όρο": "όρος — condition", "ταΐζει": "ταΐζω — to feed"}
})

ITEMS.append({
 "id": "l127-int-gerakaris", "title": "Ο γερακάρης του αεροδρομίου", "title_en": "The airport falconer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια εκπομπή για ασυνήθιστα επαγγέλματα. Καλεσμένος είναι ο Λευτέρης, που δουλεύει με γεράκια σε ένα περιφερειακό αεροδρόμιο.",
 "script": [
  L("Δημοσιογράφος", "f", "Λευτέρη, τι ακριβώς κάνει ένας γερακάρης σε ένα αεροδρόμιο;", "Lefteris, what exactly does a falconer do at an airport?"),
  L("Λευτέρης", "m", "Κρατάω τα πουλιά μακριά από τους διαδρόμους. Ένα κοπάδι γλάρων ή περιστεριών μπορεί να προκαλέσει σοβαρή ζημιά, αν μπει στη μηχανή ενός αεροπλάνου. Όταν τα πουλιά βλέπουν τακτικά ένα αρπακτικό να πετάει πάνω από την περιοχή, μαθαίνουν ότι εκεί δεν είναι ασφαλή και πάνε αλλού.", "I keep birds away from the runways. A flock of gulls or pigeons can cause serious damage if it gets into an aeroplane's engine. When birds regularly see a bird of prey flying over the area, they learn that it isn't safe there and go elsewhere."),
  L("Δημοσιογράφος", "f", "Δηλαδή τα γεράκια σας κυνηγούν τα πουλιά;", "So your hawks hunt the birds?"),
  L("Λευτέρης", "m", "Σπάνια. Ο σκοπός δεν είναι να τα σκοτώσουν, αλλά να τα τρομάξουν. Έχω τέσσερα πουλιά, και το καθένα έχει τον χαρακτήρα του. Πετάνε μόνο όταν δεν υπάρχει κίνηση στον διάδρομο, και πάντα σε συνεννόηση με τον πύργο ελέγχου.", "Rarely. The aim isn't to kill them, but to scare them. I have four birds, and each one has its own character. They fly only when there is no traffic on the runway, and always in coordination with the control tower."),
  L("Δημοσιογράφος", "f", "Πώς εκπαιδεύεται ένα γεράκι;", "How is a hawk trained?"),
  L("Λευτέρης", "m", "Με πολλή υπομονή και με φαγητό. Τους πρώτους μήνες το πουλί μαθαίνει να έρχεται στο γάντι μου από όλο και μεγαλύτερη απόσταση. Δεν γίνεται ποτέ κατοικίδιο· απλώς μαθαίνει ότι η συνεργασία μαζί μου το συμφέρει.", "With a lot of patience and with food. In the first months the bird learns to come to my glove from a greater and greater distance. It never becomes a pet; it simply learns that working with me is in its interest."),
 ],
 "questions": [
  Q("Γιατί είναι επικίνδυνα τα πουλιά για τα αεροπλάνα;", ["Γιατί λερώνουν τους διαδρόμους", "Γιατί μπορεί να μπουν στη μηχανή και να προκαλέσουν ζημιά", "Γιατί ενοχλούν τους επιβάτες", "Γιατί χαλάνε τα φώτα του διαδρόμου"], 1, "μπορεί να προκαλέσει σοβαρή ζημιά, αν μπει στη μηχανή ενός αεροπλάνου"),
  Q("Ποιος είναι ο σκοπός των γερακιών;", ["Να σκοτώνουν όσο περισσότερα πουλιά μπορούν", "Να διασκεδάζουν τους επιβάτες", "Να τρομάζουν τα πουλιά, όχι να τα σκοτώνουν", "Να φυλάνε τα αεροπλάνα τη νύχτα"], 2, "Ο σκοπός δεν είναι να τα σκοτώσουν, αλλά να τα τρομάξουν"),
  Q("Πώς εκπαιδεύεται ένα γεράκι, σύμφωνα με τον Λευτέρη;", ["Με υπομονή και φαγητό, μαθαίνοντας να έρχεται στο γάντι", "Με αυστηρές τιμωρίες", "Μεγαλώνοντας μέσα στο σπίτι σαν κατοικίδιο", "Παρακολουθώντας άλλα γεράκια"], 0, "Με πολλή υπομονή και με φαγητό"),
 ],
 "gloss": {"ασυνήθιστα": "ασυνήθιστος — unusual", "επαγγέλματα": "επάγγελμα — profession", "γεράκια": "γεράκι — hawk, falcon", "περιφερειακό": "περιφερειακός — regional", "γερακάρης": "γερακάρης — falconer", "διαδρόμους": "διάδρομος — runway", "κοπάδι": "κοπάδι — flock", "γλάρων": "γλάρος — gull", "αρπακτικό": "αρπακτικό — bird of prey", "συνεννόηση": "συνεννόηση — coordination", "πύργο ελέγχου": "πύργος ελέγχου — control tower", "γάντι": "γάντι — glove", "συμφέρει": "με συμφέρει — it's in my interest"}
})

ITEMS.append({
 "id": "l127-rep-asvestis", "title": "Ασβέστης στις ταράτσες", "title_en": "Whitewash on the rooftops", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις ειδήσεις για ένα πρόγραμμα ενός δήμου ενάντια στη ζέστη.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε μια γειτονιά με πυκνές πολυκατοικίες, δεκάδες κάτοικοι ανέβηκαν το Σάββατο στις ταράτσες με κουβάδες και ρολά. Στο πλαίσιο ενός προγράμματος του δήμου, βάφουν τις ταράτσες τους με ασβέστη ή με ειδική λευκή βαφή που αντανακλά το φως του ήλιου.", "In a neighbourhood of densely packed apartment blocks, dozens of residents went up onto the rooftops on Saturday with buckets and rollers. As part of a municipal programme, they are painting their rooftops with whitewash or a special white paint that reflects sunlight."),
  L("Ρεπόρτερ", "m", "Η ιδέα δεν είναι καινούργια· στις Κυκλάδες τα σπίτια ασβεστώνονται εδώ και αιώνες. Οι σκούρες ταράτσες απορροφούν τη θερμότητα και τη μεταφέρουν στα διαμερίσματα του τελευταίου ορόφου. Μια λευκή επιφάνεια, αντίθετα, μπορεί να μειώσει τη θερμοκρασία στο εσωτερικό κατά μερικούς βαθμούς.", "The idea isn't new; in the Cyclades houses have been whitewashed for centuries. Dark rooftops absorb heat and pass it on to the top-floor flats. A white surface, by contrast, can lower the temperature inside by a few degrees."),
  L("Ρεπόρτερ", "m", "Ο δήμος δίνει δωρεάν τα υλικά, και εθελοντές βοηθούν τους ηλικιωμένους. Η κυρία Ρούλα, που μένει στο ρετιρέ, λέει ότι πέρσι το καλοκαίρι δεν μπορούσε να κοιμηθεί χωρίς κλιματιστικό. Φέτος ελπίζει να το ανοίγει λιγότερο και να πληρώσει μικρότερο λογαριασμό ρεύματος.", "The municipality provides the materials for free, and volunteers help the elderly. Mrs Roula, who lives in the penthouse, says that last summer she couldn't sleep without air conditioning. This year she hopes to turn it on less and to pay a smaller electricity bill."),
 ],
 "questions": [
  Q("Με τι βάφουν τις ταράτσες οι κάτοικοι;", ["Με γκρίζα βαφή", "Με ασβέστη ή ειδική λευκή βαφή", "Με πράσινα φυτά", "Με ηλιακά πάνελ"], 1, "βάφουν τις ταράτσες τους με ασβέστη ή με ειδική λευκή βαφή"),
  Q("Γιατί οι σκούρες ταράτσες είναι πρόβλημα;", ["Γιατί σπάνε εύκολα", "Γιατί δεν αφήνουν το νερό να φύγει", "Γιατί απορροφούν τη θερμότητα και τη μεταφέρουν στα διαμερίσματα", "Γιατί είναι άσχημες"], 2, "Οι σκούρες ταράτσες απορροφούν τη θερμότητα"),
  Q("Τι ελπίζει η κυρία Ρούλα;", ["Να ανοίγει λιγότερο το κλιματιστικό και να πληρώσει μικρότερο λογαριασμό", "Να μετακομίσει σε άλλο όροφο", "Να φυτέψει έναν κήπο στην ταράτσα", "Να βρει δουλειά στον δήμο"], 0, "Φέτος ελπίζει να το ανοίγει λιγότερο και να πληρώσει μικρότερο λογαριασμό ρεύματος"),
 ],
 "gloss": {"ασβέστη": "ασβέστης — lime, whitewash", "ταράτσες": "ταράτσα — flat roof, rooftop", "πυκνές": "πυκνός — dense", "κουβάδες": "κουβάς — bucket", "ρολά": "ρολό — (paint) roller", "αντανακλά": "αντανακλώ — to reflect", "ασβεστώνονται": "ασβεστώνω — to whitewash", "σκούρες": "σκούρος — dark", "απορροφούν": "απορροφώ — to absorb", "θερμότητα": "θερμότητα — heat", "ρετιρέ": "ρετιρέ — penthouse (top-floor flat)", "κλιματιστικό": "κλιματιστικό — air conditioner"}
})

ITEMS.append({
 "id": "l127-rep-plyntirio-astegon", "title": "Ένα πλυντήριο ρούχων για τους άστεγους", "title_en": "A laundry for the homeless", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για την αλληλεγγύη στην πόλη.",
 "script": [
  L("Ρεπόρτερ", "f", "Κάθε Τρίτη και Παρασκευή, ένα βανάκι σταθμεύει δίπλα σε μια πλατεία του κέντρου. Μέσα έχει δύο πλυντήρια και δύο στεγνωτήρια, και οι άστεγοι της περιοχής μπορούν να πλύνουν δωρεάν τα ρούχα τους. Η ιδέα ήταν τριών φοιτητών, που συγκέντρωσαν τα χρήματα μέσα από μια διαδικτυακή καμπάνια.", "Every Tuesday and Friday, a small van parks next to a square in the centre. Inside it has two washing machines and two dryers, and the homeless people of the area can wash their clothes for free. The idea came from three students, who raised the money through an online campaign."),
  L("Ρεπόρτερ", "f", "Όσο περιμένουν το πλύσιμο, που κρατά περίπου μία ώρα, οι επισκέπτες κάθονται σε πτυσσόμενες καρέκλες, πίνουν καφέ και μιλούν με τους εθελοντές. «Το πλυντήριο είναι η αφορμή», λέει μία από τις ιδρύτριες. «Αυτό που μετράει περισσότερο είναι η κουβέντα».", "While they wait for the wash, which takes about an hour, visitors sit on folding chairs, drink coffee and talk with the volunteers. 'The laundry is the excuse,' says one of the founders. 'What counts most is the conversation.'"),
  L("Ρεπόρτερ", "f", "Ο Μανώλης, που ζει στον δρόμο εδώ και δύο χρόνια, λέει ότι με καθαρά ρούχα νιώθει πιο σίγουρος όταν πηγαίνει σε συνέντευξη για δουλειά. Η ομάδα ψάχνει τώρα χορηγό για ένα δεύτερο βανάκι, ώστε να καλύψει και άλλες γειτονιές.", "Manolis, who has been living on the street for two years, says that with clean clothes he feels more confident when he goes to a job interview. The group is now looking for a sponsor for a second van, so as to cover other neighbourhoods too."),
 ],
 "questions": [
  Q("Πώς βρήκαν τα χρήματα οι φοιτητές;", ["Από τον δήμο", "Μέσα από μια διαδικτυακή καμπάνια", "Από μια τράπεζα", "Από τους γονείς τους"], 1, "συγκέντρωσαν τα χρήματα μέσα από μια διαδικτυακή καμπάνια"),
  Q("Τι λέει η ιδρύτρια ότι μετράει περισσότερο;", ["Τα καθαρά ρούχα", "Ο καφές", "Η κουβέντα", "Η καθαριότητα της πλατείας"], 2, "Αυτό που μετράει περισσότερο είναι η κουβέντα"),
  Q("Γιατί βοηθούν τα καθαρά ρούχα τον Μανώλη;", ["Νιώθει πιο σίγουρος όταν πηγαίνει σε συνέντευξη για δουλειά", "Μπορεί να μπαίνει σε καταστήματα", "Δεν κρυώνει τον χειμώνα", "Μπορεί να τα πουλήσει"], 0, "νιώθει πιο σίγουρος όταν πηγαίνει σε συνέντευξη για δουλειά"),
 ],
 "gloss": {"αλληλεγγύη": "αλληλεγγύη — solidarity", "βανάκι": "βανάκι — small van", "σταθμεύει": "σταθμεύω — to park", "πλυντήρια": "πλυντήριο — washing machine", "στεγνωτήρια": "στεγνωτήριο — dryer", "άστεγοι": "άστεγος — homeless person", "καμπάνια": "καμπάνια — campaign", "πτυσσόμενες": "πτυσσόμενος — folding", "αφορμή": "αφορμή — pretext, occasion", "ιδρύτριες": "ιδρύτρια — founder (f.)", "κουβέντα": "κουβέντα — conversation, chat", "χορηγό": "χορηγός — sponsor"}
})

ITEMS.append({
 "id": "l127-mono-dialogismos", "title": "Δέκα λεπτά σιωπής τη μέρα", "title_en": "Ten minutes of silence a day", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε τον Κοσμά, οδηγό ταξί, να μιλάει σε ένα podcast για μια συνήθεια που απέκτησε.",
 "script": [
  L("Κοσμάς", "m", "Πριν από έναν χρόνο, αν μου έλεγες ότι θα έκανα διαλογισμό, θα γελούσα. Δουλεύω δώδεκα ώρες τη μέρα στην κίνηση της Αθήνας, με κόρνες, φασαρία και πελάτες που βιάζονται. Ήμουν συνέχεια τσιτωμένος και φώναζα στο σπίτι για το παραμικρό.", "A year ago, if you had told me I would meditate, I'd have laughed. I work twelve hours a day in Athens traffic, with horns, noise and customers in a hurry. I was constantly tense and shouted at home over the slightest thing."),
  L("Κοσμάς", "m", "Η κόρη μου μού έδειξε μια εφαρμογή στο κινητό. Ξεκίνησα με πέντε λεπτά το πρωί, πριν βγω με το ταξί. Απλώς κάθεσαι, κλείνεις τα μάτια και προσέχεις την αναπνοή σου. Στην αρχή το μυαλό μου πήγαινε συνέχεια στους λογαριασμούς και στη βενζίνη.", "My daughter showed me an app on my phone. I started with five minutes in the morning, before I went out with the taxi. You just sit, close your eyes and pay attention to your breathing. At first my mind kept wandering to the bills and the petrol."),
  L("Κοσμάς", "m", "Σιγά σιγά όμως κατάφερα να φτάσω τα δέκα λεπτά. Δεν έγινα άλλος άνθρωπος· ακόμα θυμώνω στο μποτιλιάρισμα. Τώρα όμως το καταλαβαίνω πιο γρήγορα, παίρνω μια βαθιά ανάσα και δεν το κουβαλάω μαζί μου στο σπίτι.", "But gradually I managed to reach ten minutes. I didn't become a different person; I still get angry in traffic jams. But now I notice it more quickly, take a deep breath and don't carry it home with me."),
 ],
 "questions": [
  Q("Πώς ήταν ο Κοσμάς πριν από έναν χρόνο;", ["Ήρεμος και χαρούμενος", "Συνέχεια τσιτωμένος, φώναζε στο σπίτι για το παραμικρό", "Άνεργος", "Άρρωστος"], 1, "Ήμουν συνέχεια τσιτωμένος"),
  Q("Ποιος του έδειξε την εφαρμογή;", ["Ένας πελάτης", "Ένας γιατρός", "Η κόρη του", "Ένας συνάδελφος"], 2, "Η κόρη μου μού έδειξε μια εφαρμογή στο κινητό"),
  Q("Τι έχει αλλάξει σήμερα;", ["Καταλαβαίνει πιο γρήγορα τον θυμό του και δεν τον κουβαλά στο σπίτι", "Δεν θυμώνει ποτέ πια", "Άλλαξε δουλειά", "Οδηγεί λιγότερες ώρες"], 0, "δεν το κουβαλάω μαζί μου στο σπίτι"),
 ],
 "gloss": {"διαλογισμό": "διαλογισμός — meditation", "κόρνες": "κόρνα — (car) horn", "φασαρία": "φασαρία — noise, fuss", "τσιτωμένος": "τσιτωμένος — tense, wound up", "παραμικρό": "για το παραμικρό — over the slightest thing", "εφαρμογή": "εφαρμογή — app", "αναπνοή": "αναπνοή — breathing", "θυμώνω": "θυμώνω — to get angry", "μποτιλιάρισμα": "μποτιλιάρισμα — traffic jam", "ανάσα": "ανάσα — breath"}
})

ITEMS.append({
 "id": "l127-mono-o-per-lyon", "title": "Ένας χρόνος ως οπέρ στη Λιόν", "title_en": "A year as an au pair in Lyon", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε την Ιφιγένεια, φοιτήτρια, να μιλάει σε μαθητές λυκείου για τη χρονιά που πέρασε στη Γαλλία.",
 "script": [
  L("Ιφιγένεια", "f", "Όταν τελείωσα το λύκειο, δεν ήξερα τι ήθελα να σπουδάσω. Αποφάσισα να πάω για έναν χρόνο στη Λιόν ως οπέρ, δηλαδή να μένω με μια οικογένεια, να προσέχω τα παιδιά τους και σε αντάλλαγμα να έχω δωμάτιο, φαγητό και ένα μικρό χαρτζιλίκι.", "When I finished school, I didn't know what I wanted to study. I decided to go to Lyon for a year as an au pair, that is, to live with a family, look after their children and in return have a room, food and a little pocket money."),
  L("Ιφιγένεια", "f", "Οι πρώτες εβδομάδες ήταν δύσκολες. Τα γαλλικά του σχολείου δεν με βοηθούσαν να καταλάβω δύο πεντάχρονα δίδυμα που μιλούσαν ταυτόχρονα. Τα απογεύματα όμως πήγαινα σε μαθήματα γλώσσας, και μέσα σε λίγους μήνες άρχισα να ονειρεύομαι στα γαλλικά.", "The first weeks were hard. School French didn't help me understand five-year-old twins who talked at the same time. But in the afternoons I went to language classes, and within a few months I began to dream in French."),
  L("Ιφιγένεια", "f", "Το πιο σημαντικό που έμαθα δεν ήταν η γλώσσα. Περνώντας τόσες ώρες με τα παιδιά, κατάλαβα ότι μου αρέσει να εξηγώ πράγματα και να βλέπω κάποιον να μαθαίνει. Έτσι, όταν γύρισα, έδωσα εξετάσεις για το παιδαγωγικό τμήμα, και σήμερα σπουδάζω για να γίνω δασκάλα.", "The most important thing I learned wasn't the language. Spending so many hours with the children, I realised that I like explaining things and seeing someone learn. So, when I came back, I sat the exams for the education department, and today I'm studying to become a primary teacher."),
 ],
 "questions": [
  Q("Τι έπαιρνε η Ιφιγένεια σε αντάλλαγμα για τη φροντίδα των παιδιών;", ["Έναν κανονικό μισθό", "Δωμάτιο, φαγητό και ένα μικρό χαρτζιλίκι", "Δωρεάν σπουδές στο πανεπιστήμιο", "Εισιτήρια για ταξίδια"], 1, "σε αντάλλαγμα να έχω δωμάτιο, φαγητό και ένα μικρό χαρτζιλίκι"),
  Q("Τι ήταν δύσκολο τις πρώτες εβδομάδες;", ["Το φαγητό", "Ο καιρός", "Να καταλάβει τα δίδυμα που μιλούσαν ταυτόχρονα", "Να βρει φίλους"], 2, "Τα γαλλικά του σχολείου δεν με βοηθούσαν να καταλάβω δύο πεντάχρονα δίδυμα"),
  Q("Πώς επηρέασε η χρονιά αυτή τις σπουδές της;", ["Κατάλαβε ότι της αρέσει να εξηγεί και σπουδάζει για δασκάλα", "Αποφάσισε να σπουδάσει γαλλική φιλολογία", "Έμεινε στη Γαλλία για σπουδές", "Αποφάσισε να μη σπουδάσει"], 0, "σήμερα σπουδάζω για να γίνω δασκάλα"),
 ],
 "gloss": {"οπέρ": "οπέρ — au pair", "λυκείου": "λύκειο — upper secondary school", "αντάλλαγμα": "σε αντάλλαγμα — in return", "χαρτζιλίκι": "χαρτζιλίκι — pocket money", "δίδυμα": "δίδυμο — twin", "ταυτόχρονα": "ταυτόχρονα — at the same time", "ονειρεύομαι": "ονειρεύομαι — to dream", "παιδαγωγικό τμήμα": "παιδαγωγικό τμήμα — education department (teacher training)", "δασκάλα": "δασκάλα — primary teacher (f.)"}
})

ITEMS.append({
 "id": "l127-c1-petrichor", "title": "Η μυρωδιά της πρώτης βροχής", "title_en": "The smell of the first rain", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή εκλαΐκευσης της επιστήμης για τη μυρωδιά που αναδύεται όταν βρέχει μετά από ξηρασία.",
 "script": [
  L("Παρουσιάστρια", "f", "Όλοι τη γνωρίζουμε: εκείνη τη γήινη, σχεδόν γλυκιά μυρωδιά που γεμίζει τον αέρα όταν πέφτουν οι πρώτες σταγόνες μετά από μια μακριά περίοδο ξηρασίας. Το 1964 δύο Αυστραλοί ερευνητές, η Ιζαμπέλ Μπερ και ο Ρίτσαρντ Τόμας, της έδωσαν ένα όνομα με ελληνικές ρίζες: «πετριχώρ», από την πέτρα και τον ιχώρα, το υγρό που, σύμφωνα με την αρχαία μυθολογία, κυλούσε στις φλέβες των θεών.", "We all know it: that earthy, almost sweet smell that fills the air when the first drops fall after a long dry spell. In 1964 two Australian researchers, Isabel Bear and Richard Thomas, gave it a name with Greek roots: 'petrichor', from petra, stone, and ichor, the fluid that, according to ancient mythology, flowed in the veins of the gods."),
  L("Παρουσιάστρια", "f", "Από πού προέρχεται όμως; Ένα μέρος της οφείλεται σε έλαια που εκκρίνουν τα φυτά σε περιόδους ξηρασίας και που συσσωρεύονται στο χώμα και στις πέτρες. Το πιο χαρακτηριστικό συστατικό, ωστόσο, είναι η γεοσμίνη, μια ουσία που παράγουν ορισμένα βακτήρια του εδάφους. Η ανθρώπινη μύτη είναι εντυπωσιακά ευαίσθητη σε αυτήν: μπορεί να την ανιχνεύσει σε συγκεντρώσεις λίγων μορίων ανά τρισεκατομμύριο.", "But where does it come from? Part of it is due to oils that plants secrete during dry periods and that accumulate in the soil and on stones. The most characteristic component, however, is geosmin, a substance produced by certain soil bacteria. The human nose is impressively sensitive to it: it can detect it at concentrations of a few parts per trillion."),
  L("Παρουσιάστρια", "f", "Το 2015 ερευνητές στη Μασαχουσέτη κατέγραψαν με κάμερες υψηλής ταχύτητας τι συμβαίνει όταν μια σταγόνα πέφτει σε πορώδες έδαφος: εγκλωβίζει μικροσκοπικές φυσαλίδες αέρα, οι οποίες ανεβαίνουν και σκάνε, απελευθερώνοντας στον αέρα αερολύματα με τις αρωματικές ουσίες. Γιατί όμως είμαστε τόσο ευαίσθητοι σε αυτή τη μυρωδιά; Ορισμένοι επιστήμονες υποθέτουν ότι για τους προγόνους μας η μυρωδιά της βροχής μπορεί να σήμαινε νερό και ζωή, αν και η υπόθεση αυτή δεν έχει αποδειχθεί.", "In 2015 researchers in Massachusetts recorded with high-speed cameras what happens when a drop falls on porous ground: it traps tiny air bubbles, which rise and burst, releasing into the air aerosols carrying the aromatic substances. But why are we so sensitive to this smell? Some scientists speculate that for our ancestors the smell of rain may have meant water and life, although this hypothesis has not been proven."),
 ],
 "questions": [
  Q("Από πού προέρχεται η λέξη «πετριχώρ»;", ["Από ένα αυστραλιανό τοπωνύμιο", "Από την πέτρα και τον ιχώρα, το υγρό στις φλέβες των θεών", "Από το όνομα ενός βακτηρίου", "Από μια λατινική λέξη για τη βροχή"], 1, "από την πέτρα και τον ιχώρα"),
  Q("Τι είναι η γεοσμίνη;", ["Ένα έλαιο που εκκρίνουν οι πέτρες", "Ένα αέριο που βγαίνει από τα σύννεφα", "Μια ουσία που παράγουν ορισμένα βακτήρια του εδάφους", "Ένα συστατικό του νερού της βροχής"], 2, "μια ουσία που παράγουν ορισμένα βακτήρια του εδάφους"),
  Q("Τι έδειξαν οι κάμερες υψηλής ταχύτητας το 2015;", ["Ότι οι σταγόνες εγκλωβίζουν φυσαλίδες που σκάνε και απελευθερώνουν αερολύματα", "Ότι η μυρωδιά βγαίνει μόνο από τα φυτά", "Ότι οι σταγόνες εξατμίζονται πριν φτάσουν στο έδαφος", "Ότι η μυρωδιά προέρχεται από τον κεραυνό"], 0, "εγκλωβίζει μικροσκοπικές φυσαλίδες αέρα"),
  Q("Τι λέει η παρουσιάστρια για την εξήγηση της ευαισθησίας μας;", ["Ότι έχει αποδειχθεί πλήρως", "Ότι οφείλεται στη μόλυνση της ατμόσφαιρας", "Ότι αφορά μόνο τους κατοίκους ξηρών περιοχών", "Ότι είναι μια υπόθεση που δεν έχει αποδειχθεί"], 3, "η υπόθεση αυτή δεν έχει αποδειχθεί"),
 ],
 "gloss": {"εκλαΐκευσης": "εκλαΐκευση — popularisation", "αναδύεται": "αναδύομαι — to emerge, arise", "ξηρασία": "ξηρασία — drought, dry spell", "γήινη": "γήινος — earthy", "σταγόνες": "σταγόνα — drop", "ιχώρα": "ιχώρ — ichor (the gods' blood in myth)", "φλέβες": "φλέβα — vein", "εκκρίνουν": "εκκρίνω — to secrete", "συσσωρεύονται": "συσσωρεύομαι — to accumulate", "γεοσμίνη": "γεοσμίνη — geosmin", "ανιχνεύσει": "ανιχνεύω — to detect", "πορώδες": "πορώδης — porous", "εγκλωβίζει": "εγκλωβίζω — to trap", "φυσαλίδες": "φυσαλίδα — bubble", "αερολύματα": "αερόλυμα — aerosol", "προγόνους": "πρόγονος — ancestor"}
})

ITEMS.append({
 "id": "l127-c1-androutsos", "title": "Από το Χάνι της Γραβιάς στον πύργο της Ακρόπολης", "title_en": "From the Inn of Gravia to the Acropolis tower", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια ιστορικό για τον Οδυσσέα Ανδρούτσο.",
 "script": [
  L("Δημοσιογράφος", "m", "Ο Οδυσσέας Ανδρούτσος είναι από τις πιο αμφιλεγόμενες μορφές του Αγώνα. Ας ξεκινήσουμε από τα πρώτα του χρόνια.", "Odysseas Androutsos is one of the most controversial figures of the Struggle. Let's start with his early years."),
  L("Ιστορικός", "f", "Γεννήθηκε γύρω στο 1788, σύμφωνα με τις περισσότερες πηγές στην Ιθάκη, γιος ενός γνωστού κλεφτοκαπετάνιου της Ρούμελης. Μεγάλωσε στην αυλή του Αλή Πασά στα Γιάννενα, όπου έμαθε την τέχνη του πολέμου αλλά και της πολιτικής, και αργότερα έγινε αρματολός της Λιβαδειάς.", "He was born around 1788, according to most sources on Ithaca, the son of a well-known klepht captain of Roumeli. He grew up at the court of Ali Pasha in Ioannina, where he learned the art of war but also of politics, and later became armatolos of Livadeia."),
  L("Δημοσιογράφος", "m", "Και φυσικά, το Χάνι της Γραβιάς.", "And of course, the Inn of Gravia."),
  L("Ιστορικός", "f", "Ναι. Τον Μάιο του 1821, μαζί με λίγο περισσότερους από εκατό άνδρες, οχυρώθηκε σε ένα πέτρινο χάνι και αντιμετώπισε έναν οθωμανικό στρατό πολλές φορές μεγαλύτερο. Η αντίσταση κράτησε ως το βράδυ, και τη νύχτα οι πολιορκημένοι κατάφεραν να διαφύγουν. Η μάχη καθυστέρησε την προέλαση του εχθρού προς την Πελοπόννησο σε μια κρίσιμη στιγμή και έγινε σύμβολο της Επανάστασης.", "Yes. In May 1821, with a little over a hundred men, he barricaded himself in a stone inn and faced an Ottoman army many times larger. The resistance lasted until evening, and at night the besieged managed to escape. The battle delayed the enemy's advance towards the Peloponnese at a critical moment and became a symbol of the Revolution."),
  L("Ιστορικός", "f", "Το τέλος του όμως είναι τραγικό. Σε σύγκρουση με την κυβέρνηση και με άλλους οπλαρχηγούς, ήρθε σε διαπραγματεύσεις με τους Οθωμανούς, κάτι που οι αντίπαλοί του θεώρησαν προδοσία. Το 1825 παραδόθηκε στον πρώην πρωτοπαλίκαρό του, τον Γκούρα, και φυλακίστηκε στον λεγόμενο Ενετικό πύργο της Ακρόπολης. Τον Ιούνιο βρέθηκε νεκρός στη βάση του πύργου. Η επίσημη εκδοχή μίλησε για απόπειρα απόδρασης, οι περισσότεροι ιστορικοί όμως θεωρούν ότι δολοφονήθηκε.", "His end, however, is tragic. In conflict with the government and other chieftains, he entered into negotiations with the Ottomans, which his opponents considered treason. In 1825 he surrendered to his former lieutenant, Gouras, and was imprisoned in the so-called Venetian tower of the Acropolis. In June he was found dead at the foot of the tower. The official version spoke of an escape attempt, but most historians believe he was murdered."),
 ],
 "questions": [
  Q("Πού μεγάλωσε ο Ανδρούτσος;", ["Στην Ιθάκη, με τη μητέρα του", "Στην αυλή του Αλή Πασά στα Γιάννενα", "Στη Λιβαδειά, σε μοναστήρι", "Στην Αθήνα"], 1, "Μεγάλωσε στην αυλή του Αλή Πασά στα Γιάννενα"),
  Q("Τι πέτυχε η μάχη στο Χάνι της Γραβιάς;", ["Κατέστρεψε ολοκληρωτικά τον οθωμανικό στρατό", "Απελευθέρωσε τη Λιβαδειά", "Καθυστέρησε την προέλαση του εχθρού προς την Πελοπόννησο", "Οδήγησε σε ανακωχή"], 2, "Η μάχη καθυστέρησε την προέλαση του εχθρού προς την Πελοπόννησο"),
  Q("Γιατί οι αντίπαλοί του τον κατηγόρησαν για προδοσία;", ["Γιατί ήρθε σε διαπραγματεύσεις με τους Οθωμανούς", "Γιατί εγκατέλειψε τη μάχη στη Γραβιά", "Γιατί έκλεψε χρήματα της κυβέρνησης", "Γιατί συνεργάστηκε με ξένους"], 0, "ήρθε σε διαπραγματεύσεις με τους Οθωμανούς"),
  Q("Τι πιστεύουν οι περισσότεροι ιστορικοί για τον θάνατό του;", ["Ότι σκοτώθηκε προσπαθώντας να δραπετεύσει", "Ότι πέθανε από αρρώστια", "Ότι αυτοκτόνησε", "Ότι δολοφονήθηκε"], 3, "οι περισσότεροι ιστορικοί όμως θεωρούν ότι δολοφονήθηκε"),
 ],
 "gloss": {"αμφιλεγόμενες": "αμφιλεγόμενος — controversial", "κλεφτοκαπετάνιου": "κλεφτοκαπετάνιος — klepht captain", "αυλή": "αυλή — court", "αρματολός": "αρματολός — armatolos (Christian militia captain)", "χάνι": "χάνι — inn", "οχυρώθηκε": "οχυρώνομαι — to entrench oneself", "διαφύγουν": "διαφεύγω — to escape", "προέλαση": "προέλαση — advance", "διαπραγματεύσεις": "διαπραγμάτευση — negotiation", "προδοσία": "προδοσία — treason, betrayal", "πρωτοπαλίκαρό": "πρωτοπαλίκαρο — chief lieutenant", "εκδοχή": "εκδοχή — version", "απόπειρα": "απόπειρα — attempt", "απόδρασης": "απόδραση — escape", "δολοφονήθηκε": "δολοφονούμαι — to be murdered"}
})

rnd = random.Random(127)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-127.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
