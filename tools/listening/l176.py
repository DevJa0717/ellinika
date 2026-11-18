# Source for library/listening/listening-176.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l176.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l176-ann-labyrinthos-kalampokiou", "title": "Ανακοίνωση στην είσοδο ενός λαβύρινθου από καλαμπόκι", "title_en": "An announcement at the entrance to a maize maze", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στην είσοδο ενός λαβύρινθου που έχει φτιαχτεί μέσα σε ένα χωράφι με καλαμπόκι, σε ένα αγρόκτημα έξω από τη Λάρισα.",
 "script": [
  L("Υπεύθυνος", "m", "Καλώς ήρθατε στον λαβύρινθο του αγροκτήματος! Φέτος οι διάδρομοι έχουν συνολικό μήκος τρία χιλιόμετρα και, αν τον δείτε από ψηλά, έχει το σχήμα ενός μεγάλου ηλιοτρόπιου. Οι περισσότερες οικογένειες χρειάζονται περίπου μία ώρα για να βρουν την έξοδο.", "Welcome to the farm's maze! This year the paths have a total length of three kilometres and, if you see it from above, it has the shape of a big sunflower. Most families need about an hour to find the exit."),
  L("Υπεύθυνος", "m", "Μέσα στον λαβύρινθο υπάρχουν οκτώ σταθμοί με ερωτήσεις για τη ζωή στο αγρόκτημα. Σε κάθε σταθμό σφραγίζετε τον χάρτη σας· όσοι συγκεντρώσουν και τις οκτώ σφραγίδες παίρνουν στην έξοδο ένα βαζάκι μέλι. Παρακαλούμε να μην κόβετε δρόμο μέσα από τα φυτά: το καλαμπόκι θα το μαζέψουμε τον Οκτώβριο και θα γίνει ζωοτροφή.", "Inside the maze there are eight stations with questions about life on the farm. At each station you stamp your map; those who collect all eight stamps get a little jar of honey at the exit. Please don't take shortcuts through the plants: we will harvest the maize in October and it will become animal feed."),
  L("Υπεύθυνος", "m", "Αν χαθείτε ή χρειαστείτε βοήθεια, σηκώστε ψηλά τη σημαία που θα σας δώσουμε, και κάποιος από τους βοηθούς μας στους πύργους παρατήρησης θα έρθει να σας βρει. Καλή διασκέδαση!", "If you get lost or need help, raise high the flag we will give you, and one of our helpers in the observation towers will come and find you. Have fun!"),
 ],
 "questions": [
  Q("Πόσο χρόνο χρειάζονται συνήθως οι οικογένειες;", ["Δέκα λεπτά", "Περίπου μία ώρα", "Τρεις ώρες", "Όλο το πρωί"], 1, "Οι περισσότερες οικογένειες χρειάζονται περίπου μία ώρα"),
  Q("Τι παίρνουν όσοι συγκεντρώσουν όλες τις σφραγίδες;", ["Ένα ηλιοτρόπιο", "Δωρεάν είσοδο του χρόνου", "Ένα βαζάκι μέλι", "Ένα σακί καλαμπόκι"], 2, "παίρνουν στην έξοδο ένα βαζάκι μέλι"),
  Q("Τι πρέπει να κάνει όποιος χαθεί;", ["Να σηκώσει ψηλά τη σημαία", "Να τηλεφωνήσει στο γραφείο", "Να περάσει μέσα από τα φυτά", "Να φωνάξει δυνατά"], 0, "σηκώστε ψηλά τη σημαία"),
 ],
 "gloss": {"λαβύρινθου": "λαβύρινθος — maze, labyrinth", "καλαμπόκι": "καλαμπόκι — maize, corn", "αγρόκτημα": "αγρόκτημα — farm", "διάδρομοι": "διάδρομος — path, corridor", "ηλιοτρόπιου": "ηλιοτρόπιο — sunflower", "σφραγίζετε": "σφραγίζω — to stamp", "σφραγίδες": "σφραγίδα — stamp", "κόβετε δρόμο": "κόβω δρόμο — to take a shortcut", "ζωοτροφή": "ζωοτροφή — animal feed", "πύργους παρατήρησης": "πύργος παρατήρησης — observation tower"},
})

ITEMS.append({
 "id": "l176-int-epitheoritria-trofimon", "title": "Η επιθεωρήτρια υγειονομικού ελέγχου", "title_en": "The food safety inspector", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που ελέγχει εστιατόρια και καταστήματα τροφίμων για λογαριασμό της περιφέρειας.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι ιδιοκτήτες σάς περιμένουν ή έρχεστε απροειδοποίητα;", "Do the owners expect you, or do you come unannounced?"),
  L("Επιθεωρήτρια", "f", "Σχεδόν πάντα απροειδοποίητα. Αλλιώς θα βλέπαμε μόνο την κουζίνα της καλής μέρας. Μπαίνω, δείχνω την ταυτότητά μου και ζητάω να δω πρώτα τα ψυγεία. Από ένα ψυγείο καταλαβαίνεις πολλά: τη θερμοκρασία, αν τα τρόφιμα έχουν ετικέτες με ημερομηνία, αν το ωμό κρέας είναι κάτω από τα έτοιμα φαγητά.", "Almost always unannounced. Otherwise we would only see the kitchen on its good day. I go in, show my ID and ask to see the fridges first. You learn a lot from a fridge: the temperature, whether the food has labels with dates, whether the raw meat is below the ready meals."),
  L("Δημοσιογράφος", "m", "Γιατί έχει σημασία πού μπαίνει το ωμό κρέας;", "Why does it matter where the raw meat goes?"),
  L("Επιθεωρήτρια", "f", "Γιατί αν στάξει, μολύνει ό,τι είναι από κάτω. Αν από κάτω είναι μια σαλάτα που δεν θα μαγειρευτεί, το μικρόβιο φτάνει κατευθείαν στο πιάτο του πελάτη. Τα περισσότερα λάθη δεν γίνονται από κακή πρόθεση, αλλά από βιασύνη.", "Because if it drips, it contaminates whatever is underneath. If underneath there's a salad that won't be cooked, the germ goes straight to the customer's plate. Most mistakes don't happen out of bad intent, but out of haste."),
  L("Δημοσιογράφος", "m", "Τρώτε έξω, με όσα βλέπετε;", "Do you eat out, with everything you see?"),
  L("Επιθεωρήτρια", "f", "Βέβαια! Αλλά πριν καθίσω, ρίχνω μια ματιά στις τουαλέτες. Αν οι τουαλέτες είναι καθαρές, συνήθως είναι καθαρή και η κουζίνα.", "Of course! But before I sit down, I take a look at the toilets. If the toilets are clean, the kitchen is usually clean too."),
 ],
 "questions": [
  Q("Γιατί οι έλεγχοι γίνονται συνήθως απροειδοποίητα;", ["Γιατί το ορίζει η Ευρωπαϊκή Ένωση", "Για να δουν την κουζίνα όπως είναι πραγματικά", "Γιατί οι ιδιοκτήτες δεν απαντούν στο τηλέφωνο", "Για να γλιτώσουν χρόνο"], 1, "Αλλιώς θα βλέπαμε μόνο την κουζίνα της καλής μέρας"),
  Q("Γιατί το ωμό κρέας πρέπει να μπαίνει κάτω από τα έτοιμα φαγητά;", ["Γιατί είναι βαρύ", "Για να μένει πιο κρύο", "Γιατί αν στάξει, μολύνει ό,τι είναι από κάτω", "Για να το βρίσκουν εύκολα οι μάγειρες"], 2, "αν στάξει, μολύνει ό,τι είναι από κάτω"),
  Q("Τι κοιτάζει η ίδια πριν καθίσει σε ένα εστιατόριο;", ["Τις τουαλέτες", "Τον κατάλογο", "Τις τιμές", "Τα ψυγεία"], 0, "ρίχνω μια ματιά στις τουαλέτες"),
 ],
 "gloss": {"περιφέρειας": "περιφέρεια — region (administrative)", "απροειδοποίητα": "απροειδοποίητα — without warning, unannounced", "ταυτότητά": "ταυτότητα — identity card", "ετικέτες": "ετικέτα — label", "ωμό": "ωμός — raw", "στάξει": "στάζω — to drip", "μολύνει": "μολύνω — to contaminate", "μικρόβιο": "μικρόβιο — germ", "πρόθεση": "πρόθεση — intention", "βιασύνη": "βιασύνη — haste"},
})

ITEMS.append({
 "id": "l176-int-skyloi-anichnefsis", "title": "Ο εκπαιδευτής σκύλων ανίχνευσης", "title_en": "The detection-dog trainer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν άντρα που εκπαιδεύει σκύλους για το τελωνείο ενός μεγάλου λιμανιού.",
 "script": [
  L("Δημοσιογράφος", "f", "Ποια ράτσα κάνει για αυτή τη δουλειά;", "Which breed is right for this job?"),
  L("Εκπαιδευτής", "m", "Η ράτσα μετράει λιγότερο απ' όσο νομίζουν οι περισσότεροι. Αυτό που ψάχνω είναι ένα σκυλί που δεν βαριέται να παίζει. Αν ένα κουτάβι κυνηγάει το ίδιο μπαλάκι για μισή ώρα χωρίς να σταματήσει, είναι ο ιδανικός υποψήφιος.", "The breed matters less than most people think. What I'm looking for is a dog that never gets bored of playing. If a puppy chases the same little ball for half an hour without stopping, it's the ideal candidate."),
  L("Δημοσιογράφος", "f", "Τι σχέση έχει το παιχνίδι με την ανίχνευση;", "What does play have to do with detection?"),
  L("Εκπαιδευτής", "m", "Όλη η εκπαίδευση είναι ένα παιχνίδι. Στην αρχή βάζουμε τη μυρωδιά που θέλουμε να βρίσκει μέσα στο αγαπημένο του παιχνίδι. Σιγά σιγά το σκυλί μαθαίνει ότι όταν βρει αυτή τη μυρωδιά, κερδίζει το παιχνίδι. Για τον σκύλο δεν υπάρχει δουλειά· υπάρχει μόνο κυνήγι θησαυρού.", "All the training is a game. At first we put the scent we want it to find inside its favourite toy. Little by little the dog learns that when it finds that scent, it wins the toy. For the dog there is no work; there is only a treasure hunt."),
  L("Δημοσιογράφος", "f", "Και όταν γεράσει;", "And when it gets old?"),
  L("Εκπαιδευτής", "m", "Γύρω στα εννιά, βγαίνει στη σύνταξη. Οι περισσότεροι μένουν με τον συνοδό τους. Ο δικός μου ο πρώτος σκύλος κοιμάται ακόμα στον καναπέ μου και, όταν ανοίγω μια βαλίτσα, έρχεται να τη μυρίσει από συνήθεια.", "At around nine, it retires. Most of them stay with their handler. My own first dog still sleeps on my sofa and, when I open a suitcase, comes to sniff it out of habit."),
 ],
 "questions": [
  Q("Τι ψάχνει ο εκπαιδευτής σε ένα κουτάβι;", ["Μια συγκεκριμένη ράτσα", "Ένα σκυλί που δεν βαριέται να παίζει", "Ένα πολύ ήσυχο σκυλί", "Ένα μεγαλόσωμο σκυλί"], 1, "ένα σκυλί που δεν βαριέται να παίζει"),
  Q("Πώς μαθαίνει το σκυλί να βρίσκει μια μυρωδιά;", ["Με τιμωρίες", "Με φαγητό", "Του ανταμείβουν τη μυρωδιά με το αγαπημένο του παιχνίδι", "Μιμείται άλλα σκυλιά"], 2, "όταν βρει αυτή τη μυρωδιά, κερδίζει το παιχνίδι"),
  Q("Τι γίνεται συνήθως με τα σκυλιά όταν βγαίνουν στη σύνταξη;", ["Μένουν με τον συνοδό τους", "Πηγαίνουν σε καταφύγιο", "Δίνονται για υιοθεσία στο εξωτερικό", "Συνεχίζουν να δουλεύουν λιγότερες ώρες"], 0, "Οι περισσότεροι μένουν με τον συνοδό τους"),
 ],
 "gloss": {"τελωνείο": "τελωνείο — customs", "ράτσα": "ράτσα — breed", "βαριέται": "βαριέμαι — to get bored", "κουτάβι": "κουτάβι — puppy", "υποψήφιος": "υποψήφιος — candidate", "ανίχνευση": "ανίχνευση — detection", "κυνήγι θησαυρού": "κυνήγι θησαυρού — treasure hunt", "βγαίνει στη σύνταξη": "βγαίνω στη σύνταξη — to retire", "συνοδό": "συνοδός — handler, companion", "από συνήθεια": "από συνήθεια — out of habit"},
})

ITEMS.append({
 "id": "l176-dia-metathesi-sti-rodo", "title": "Να δεχτώ τη μετάθεση στη Ρόδο;", "title_en": "Should I accept the transfer to Rhodes?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά μια πρόταση μετάθεσης που πήρε η γυναίκα από τη δουλειά της.",
 "script": [
  L("Ιωάννα", "f", "Μου πρότειναν να αναλάβω το υποκατάστημα της Ρόδου. Με προαγωγή και καλύτερο μισθό. Πρέπει να απαντήσω μέχρι την Παρασκευή.", "They've offered me the Rhodes branch. With a promotion and a better salary. I have to answer by Friday."),
  L("Στέλιος", "m", "Συγχαρητήρια! Αλλά εγώ τι θα κάνω στη Ρόδο; Η δουλειά μου είναι εδώ.", "Congratulations! But what would I do in Rhodes? My job is here."),
  L("Ιωάννα", "f", "Εσύ δουλεύεις από το σπίτι τρεις μέρες την εβδομάδα. Θα μπορούσες να ζητήσεις να δουλεύεις από εκεί όλη την εβδομάδα, και να ανεβαίνεις στην Αθήνα μία φορά τον μήνα.", "You work from home three days a week. You could ask to work from there the whole week, and come up to Athens once a month."),
  L("Στέλιος", "m", "Μπορεί. Με απασχολούν περισσότερο οι γονείς μου. Είναι μεγάλοι, και αν συμβεί κάτι, από τη Ρόδο θέλουμε ένα αεροπλάνο για να έρθουμε.", "Maybe. What worries me more is my parents. They're old, and if something happens, from Rhodes we need a plane to get here."),
  L("Ιωάννα", "f", "Το ξέρω. Γι' αυτό σκέφτομαι να ζητήσω να είναι για δύο χρόνια και όχι μόνιμα. Αν δεν μας αρέσει, γυρίζουμε.", "I know. That's why I'm thinking of asking for it to be for two years and not permanent. If we don't like it, we come back."),
  L("Στέλιος", "m", "Με δύο χρόνια συμφωνώ να το δοκιμάσουμε. Αλλά πρώτα μίλα με τον διευθυντή σου, και μετά εγώ με τον δικό μου.", "For two years I agree to give it a try. But first talk to your manager, and then I'll talk to mine."),
 ],
 "questions": [
  Q("Τι της προσφέρουν μαζί με τη μετάθεση;", ["Ένα σπίτι στη Ρόδο", "Προαγωγή και καλύτερο μισθό", "Περισσότερες μέρες άδειας", "Ένα εταιρικό αυτοκίνητο"], 1, "Με προαγωγή και καλύτερο μισθό"),
  Q("Τι ανησυχεί περισσότερο τον Στέλιο;", ["Η δουλειά του", "Το κόστος της ζωής στη Ρόδο", "Οι ηλικιωμένοι γονείς του", "Ο καιρός"], 2, "Με απασχολούν περισσότερο οι γονείς μου"),
  Q("Σε τι καταλήγουν;", ["Να το δοκιμάσουν για δύο χρόνια, αν συμφωνήσουν και οι δουλειές τους", "Να πει η Ιωάννα όχι", "Να πάει μόνη της η Ιωάννα", "Να μετακομίσουν μόνιμα"], 0, "Με δύο χρόνια συμφωνώ να το δοκιμάσουμε"),
 ],
 "gloss": {"μετάθεσης": "μετάθεση — (job) transfer", "υποκατάστημα": "υποκατάστημα — branch", "προαγωγή": "προαγωγή — promotion", "μισθό": "μισθός — salary", "Με απασχολούν": "με απασχολεί — it concerns me, it's on my mind", "μόνιμα": "μόνιμα — permanently", "διευθυντή": "διευθυντής — manager, director"},
})

ITEMS.append({
 "id": "l176-dia-dyo-prosfores-gia-to-mpanio", "title": "Δύο προσφορές για το μπάνιο", "title_en": "Two quotes for the bathroom", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέλφια που ανακαινίζουν το διαμέρισμα της μητέρας τους να συζητούν δύο προσφορές από τεχνίτες.",
 "script": [
  L("Μαρίνα", "f", "Ήρθαν και οι δύο προσφορές για το μπάνιο. Ο κύριος Παύλος ζητάει τέσσερις χιλιάδες και ο νεαρός με την εταιρεία τρεις χιλιάδες διακόσια.", "Both quotes for the bathroom have come in. Mr Pavlos is asking four thousand and the young man with the company three thousand two hundred."),
  L("Άρης", "m", "Οκτακόσια ευρώ διαφορά δεν είναι λίγα. Τι περιλαμβάνει η καθεμία;", "Eight hundred euros' difference isn't nothing. What does each one include?"),
  L("Μαρίνα", "f", "Αυτό είναι το θέμα. Του Παύλου περιλαμβάνει και τα πλακάκια και τα είδη υγιεινής. Του νεαρού είναι μόνο η εργασία· τα υλικά τα αγοράζουμε εμείς.", "That's the point. Pavlos's includes the tiles and the bathroom fittings. The young man's is labour only; we buy the materials ourselves."),
  L("Άρης", "m", "Τότε ο νεαρός βγαίνει ακριβότερος. Και χρόνος;", "Then the young man works out more expensive. And time?"),
  L("Μαρίνα", "f", "Ο Παύλος λέει τρεις εβδομάδες, αλλά μπορεί να αρχίσει μόνο τον Μάρτιο. Ο νεαρός μπορεί να αρχίσει αύριο. Και η μαμά θέλει να έχει μπάνιο πριν από το Πάσχα.", "Pavlos says three weeks, but he can only start in March. The young man can start tomorrow. And Mum wants to have a bathroom before Easter."),
  L("Άρης", "m", "Ο Παύλος έφτιαξε την κουζίνα της κυρίας Σοφίας και είναι ακόμα σαν καινούργια. Ας του ζητήσουμε να μας δώσει γραπτή ημερομηνία παράδοσης. Αν τελειώνει πριν από το Πάσχα, πάμε με αυτόν.", "Pavlos did Mrs Sofia's kitchen and it's still like new. Let's ask him to give us a delivery date in writing. If he finishes before Easter, we go with him."),
 ],
 "questions": [
  Q("Τι δεν περιλαμβάνει η προσφορά του νεαρού;", ["Την εργασία", "Τα υλικά", "Την αποκομιδή των μπάζων", "Τον ΦΠΑ"], 1, "Του νεαρού είναι μόνο η εργασία· τα υλικά τα αγοράζουμε εμείς"),
  Q("Ποιο είναι το μειονέκτημα του κυρίου Παύλου;", ["Είναι ακριβότερος συνολικά", "Δεν έχει εμπειρία", "Μπορεί να αρχίσει μόνο τον Μάρτιο", "Δεν δίνει εγγύηση"], 2, "μπορεί να αρχίσει μόνο τον Μάρτιο"),
  Q("Τι προτείνει τελικά ο Άρης;", ["Να ζητήσουν από τον Παύλο γραπτή ημερομηνία παράδοσης", "Να πάρουν τον νεαρό αμέσως", "Να ζητήσουν τρίτη προσφορά", "Να περιμένουν μέχρι το καλοκαίρι"], 0, "Ας του ζητήσουμε να μας δώσει γραπτή ημερομηνία παράδοσης"),
 ],
 "gloss": {"ανακαινίζουν": "ανακαινίζω — to renovate", "προσφορές": "προσφορά — quote, offer", "τεχνίτες": "τεχνίτης — tradesman, craftsman", "περιλαμβάνει": "περιλαμβάνω — to include", "πλακάκια": "πλακάκι — tile", "είδη υγιεινής": "είδη υγιεινής — bathroom fittings, sanitary ware", "εργασία": "εργασία — labour, work", "υλικά": "υλικό — material", "ημερομηνία παράδοσης": "ημερομηνία παράδοσης — completion (delivery) date"},
})

ITEMS.append({
 "id": "l176-mon-kalathi-lachanikon", "title": "Ένα καλάθι λαχανικών κάθε εβδομάδα", "title_en": "A box of vegetables every week", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλάει για μια ομάδα οικογενειών που αγοράζουν απευθείας από έναν αγρότη.",
 "script": [
  L("Κωστής", "m", "Πριν από τρία χρόνια, δεκαπέντε οικογένειες της γειτονιάς κάναμε μια συμφωνία με έναν νεαρό αγρότη από τα Μέγαρα. Τον Φεβρουάριο του πληρώνουμε από πριν ένα ποσό για όλη τη χρονιά, κι εκείνος κάθε Πέμπτη μάς φέρνει ένα καλάθι με ό,τι έχει βγάλει το χωράφι εκείνη την εβδομάδα.", "Three years ago, fifteen families in the neighbourhood made an agreement with a young farmer from Megara. In February we pay him in advance a sum for the whole year, and every Thursday he brings us a basket with whatever the field has produced that week."),
  L("Κωστής", "m", "Η αλήθεια είναι ότι δεν διαλέγεις. Τον Ιούλιο πνιγόμαστε στα κολοκυθάκια και στις ντομάτες, και τον Ιανουάριο τρώμε λάχανο, πράσα και σέσκουλα μέχρι να μας βγουν από τα αυτιά. Η γυναίκα μου έχει μάθει εκατό τρόπους να μαγειρεύει το λάχανο.", "The truth is that you don't choose. In July we're drowning in courgettes and tomatoes, and in January we eat cabbage, leeks and chard until they come out of our ears. My wife has learned a hundred ways to cook cabbage."),
  L("Κωστής", "m", "Πέρσι το χαλάζι κατέστρεψε μισές ντομάτες, και τα καλάθια του Ιουνίου ήταν μισοάδεια. Κανείς δεν ζήτησε τα λεφτά του πίσω· αυτή είναι η ουσία της συμφωνίας: το ρίσκο το μοιραζόμαστε με τον αγρότη.", "Last year hail destroyed half the tomatoes, and the June baskets were half empty. Nobody asked for their money back; that is the essence of the agreement: we share the risk with the farmer."),
  L("Κωστής", "m", "Το καλύτερο όμως είναι τα παιδιά. Μία φορά τον μήνα πηγαίνουμε όλοι στο χωράφι να βοηθήσουμε. Ο γιος μου, που παλιά δεν άγγιζε τίποτα πράσινο, τώρα τρώει καρότα σαν κουνέλι, αρκεί να τα έχει βγάλει ο ίδιος από το χώμα.", "But the best thing is the children. Once a month we all go to the field to help. My son, who used to touch nothing green, now eats carrots like a rabbit, as long as he has pulled them out of the soil himself."),
 ],
 "questions": [
  Q("Πώς πληρώνουν οι οικογένειες τον αγρότη;", ["Κάθε Πέμπτη, για ό,τι παίρνουν", "Από πριν, ένα ποσό για όλη τη χρονιά", "Μόνο όταν η σοδειά είναι καλή", "Με εθελοντική δουλειά αντί για χρήματα"], 1, "του πληρώνουμε από πριν ένα ποσό για όλη τη χρονιά"),
  Q("Τι έγινε όταν το χαλάζι κατέστρεψε τις ντομάτες;", ["Ο αγρότης επέστρεψε χρήματα", "Αγόρασαν ντομάτες από τη λαϊκή", "Κανείς δεν ζήτησε τα λεφτά του πίσω", "Η συμφωνία σταμάτησε"], 2, "Κανείς δεν ζήτησε τα λεφτά του πίσω"),
  Q("Τι άλλαξε στον γιο του;", ["Τρώει λαχανικά, αν τα έχει βγάλει ο ίδιος από το χώμα", "Θέλει να γίνει αγρότης", "Δεν τρώει πια λάχανο", "Πηγαίνει κάθε μέρα στο χωράφι"], 0, "αρκεί να τα έχει βγάλει ο ίδιος από το χώμα"),
 ],
 "gloss": {"απευθείας": "απευθείας — directly", "από πριν": "από πριν — in advance", "πνιγόμαστε": "πνίγομαι — to drown (fig. to be swamped)", "κολοκυθάκια": "κολοκυθάκι — courgette", "λάχανο": "λάχανο — cabbage", "πράσα": "πράσο — leek", "σέσκουλα": "σέσκουλο — chard", "χαλάζι": "χαλάζι — hail", "ρίσκο": "ρίσκο — risk", "χώμα": "χώμα — soil"},
})

ITEMS.append({
 "id": "l176-vm-dimotiki-pinakothiki", "title": "Μήνυμα από τη δημοτική πινακοθήκη", "title_en": "A message from the municipal art gallery", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από μια υπάλληλο της δημοτικής πινακοθήκης.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, κυρία Ρήγα, σας τηλεφωνώ από τη Δημοτική Πινακοθήκη για τον πίνακα του παππού σας, που μας δανείσατε για την έκθεση τοπίων. Η έκθεση πήγε πολύ καλά και ο δήμος αποφάσισε να την παρατείνει μέχρι το τέλος Φεβρουαρίου, αντί για το τέλος Ιανουαρίου.", "Good morning, Mrs Riga, I'm calling from the Municipal Art Gallery about your grandfather's painting, which you lent us for the landscape exhibition. The exhibition went very well and the municipality has decided to extend it until the end of February, instead of the end of January."),
  L("Υπάλληλος", "f", "Θα χρειαστούμε τη συγκατάθεσή σας για την παράταση, γραπτώς. Σας έστειλα ένα έντυπο με email· αρκεί να το υπογράψετε και να μας το στείλετε πίσω. Η ασφάλιση του πίνακα ισχύει και για τον επιπλέον μήνα.", "We'll need your consent for the extension, in writing. I've sent you a form by email; you just need to sign it and send it back to us. The painting's insurance also covers the extra month."),
  L("Υπάλληλος", "f", "Επίσης, ένας συλλέκτης ρώτησε αν ο πίνακας πωλείται. Του είπα ότι δεν το γνωρίζουμε· αν σας ενδιαφέρει, μπορούμε να του δώσουμε το τηλέφωνό σας, μόνο με τη δική σας άδεια. Το τηλέφωνό μου είναι 2310 455 718. Ευχαριστώ πολύ.", "Also, a collector asked whether the painting is for sale. I told him we don't know; if you're interested, we can give him your phone number, only with your permission. My number is 2310 455 718. Thank you very much."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί η υπάλληλος;", ["Ο πίνακας έπαθε ζημιά", "Η έκθεση παρατείνεται μέχρι το τέλος Φεβρουαρίου", "Η έκθεση ακυρώθηκε", "Θέλουν να αγοράσουν τον πίνακα"], 1, "αποφάσισε να την παρατείνει μέχρι το τέλος Φεβρουαρίου"),
  Q("Τι πρέπει να κάνει η κυρία Ρήγα;", ["Να πάει στην πινακοθήκη", "Να πληρώσει την ασφάλιση", "Να υπογράψει ένα έντυπο και να το στείλει πίσω", "Να τηλεφωνήσει στον συλλέκτη"], 2, "αρκεί να το υπογράψετε και να μας το στείλετε πίσω"),
  Q("Τι θα γίνει με το τηλέφωνό της;", ["Θα δοθεί στον συλλέκτη μόνο αν το επιτρέψει", "Δόθηκε ήδη στον συλλέκτη", "Θα δημοσιευτεί στον κατάλογο της έκθεσης", "Δεν θα δοθεί σε κανέναν, ό,τι κι αν γίνει"], 0, "μόνο με τη δική σας άδεια"),
 ],
 "gloss": {"πινακοθήκης": "πινακοθήκη — art gallery", "δανείσατε": "δανείζω — to lend", "τοπίων": "τοπίο — landscape", "παρατείνει": "παρατείνω — to extend", "συγκατάθεσή": "συγκατάθεση — consent", "παράταση": "παράταση — extension", "έντυπο": "έντυπο — form", "ασφάλιση": "ασφάλιση — insurance", "συλλέκτης": "συλλέκτης — collector", "πωλείται": "πωλείται — it is for sale"},
})

ITEMS.append({
 "id": "l176-vm-diagonismos-fotografias", "title": "Μήνυμα από την επιτροπή ενός διαγωνισμού φωτογραφίας", "title_en": "A message from a photography competition committee", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από την οργανώτρια ενός διαγωνισμού φωτογραφίας στον οποίο λάβατε μέρος.",
 "script": [
  L("Οργανώτρια", "f", "Καλησπέρα, κύριε Αντωνίου, σας τηλεφωνώ από τον Φωτογραφικό Όμιλο της πόλης για τον διαγωνισμό με θέμα «Το νερό». Έχω καλά νέα: η φωτογραφία σας με τα παιδιά στη βρύση της πλατείας πήρε το δεύτερο βραβείο, ανάμεσα σε τριακόσιες συμμετοχές.", "Good afternoon, Mr Antoniou, I'm calling from the city's Photography Club about the competition on the theme 'Water'. I have good news: your photograph of the children at the fountain in the square won second prize, among three hundred entries."),
  L("Οργανώτρια", "f", "Η απονομή θα γίνει την Κυριακή στις επτά το απόγευμα στο Πνευματικό Κέντρο, όπου θα εγκαινιαστεί και η έκθεση με τις τριάντα καλύτερες φωτογραφίες. Για την έκθεση χρειαζόμαστε το αρχείο σας σε υψηλή ανάλυση· η φωτογραφία θα τυπωθεί σε μεγάλο μέγεθος, και αυτό που μας στείλατε είναι πολύ μικρό.", "The award ceremony will take place on Sunday at seven in the evening at the Cultural Centre, where the exhibition of the thirty best photographs will also open. For the exhibition we need your file in high resolution; the photograph will be printed in a large size, and the one you sent us is too small."),
  L("Οργανώτρια", "f", "Κάτι ακόμα: επειδή στη φωτογραφία φαίνονται παιδιά, χρειαζόμαστε υπογεγραμμένη άδεια από τους γονείς τους πριν την εκθέσουμε. Αν δεν τη βρείτε έως την Παρασκευή, θα κρατήσετε το βραβείο, αλλά η φωτογραφία δεν θα μπει στην έκθεση. Συγχαρητήρια ξανά!", "One more thing: because children can be seen in the photograph, we need signed permission from their parents before we exhibit it. If you can't get it by Friday, you will keep the prize, but the photograph won't go into the exhibition. Congratulations again!"),
 ],
 "questions": [
  Q("Ποιο είναι το καλό νέο;", ["Η φωτογραφία του πήρε το πρώτο βραβείο", "Η φωτογραφία του πήρε το δεύτερο βραβείο", "Έγινε μέλος του ομίλου", "Θα γίνει μέλος της επιτροπής"], 1, "πήρε το δεύτερο βραβείο"),
  Q("Γιατί χρειάζονται ξανά το αρχείο της φωτογραφίας;", ["Γιατί χάθηκε", "Γιατί ήταν θολή", "Γιατί χρειάζονται υψηλή ανάλυση για να την τυπώσουν μεγάλη", "Γιατί θέλουν να τη δημοσιεύσουν σε εφημερίδα"], 2, "χρειαζόμαστε το αρχείο σας σε υψηλή ανάλυση"),
  Q("Τι θα γίνει αν δεν φέρει την άδεια των γονιών έως την Παρασκευή;", ["Θα κρατήσει το βραβείο, αλλά η φωτογραφία δεν θα εκτεθεί", "Θα χάσει το βραβείο", "Η έκθεση θα αναβληθεί", "Θα πληρώσει πρόστιμο"], 0, "θα κρατήσετε το βραβείο, αλλά η φωτογραφία δεν θα μπει στην έκθεση"),
 ],
 "gloss": {"διαγωνισμού": "διαγωνισμός — competition", "βρύση": "βρύση — (drinking) fountain, tap", "βραβείο": "βραβείο — prize", "συμμετοχές": "συμμετοχή — entry, participation", "απονομή": "απονομή — award ceremony", "εγκαινιαστεί": "εγκαινιάζομαι — to be opened (inaugurated)", "υψηλή ανάλυση": "υψηλή ανάλυση — high resolution", "τυπωθεί": "τυπώνομαι — to be printed", "υπογεγραμμένη": "υπογεγραμμένος — signed", "εκθέσουμε": "εκθέτω — to exhibit"},
})

ITEMS.append({
 "id": "l176-c1-gps-kai-schetikotita", "title": "Γιατί το GPS χρειάζεται τη θεωρία της σχετικότητας", "title_en": "Why GPS needs the theory of relativity", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν φυσικό για το πώς λειτουργεί το σύστημα δορυφορικού εντοπισμού.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς ξέρει το κινητό μου πού βρίσκομαι;", "How does my phone know where I am?"),
  L("Φυσικός", "m", "Οι δορυφόροι του GPS εκπέμπουν συνεχώς σήματα που λένε, στην ουσία, «είμαι εδώ και η ώρα είναι αυτή». Το κινητό σας υπολογίζει πόσο χρόνο χρειάστηκε κάθε σήμα για να φτάσει και, από τέσσερις τουλάχιστον δορυφόρους, βρίσκει τη θέση σας. Επειδή τα σήματα ταξιδεύουν με την ταχύτητα του φωτός, ένα λάθος ενός εκατομμυριοστού του δευτερολέπτου στο ρολόι σημαίνει λάθος περίπου τριακοσίων μέτρων στο έδαφος.", "The GPS satellites constantly broadcast signals that say, essentially, 'I am here and the time is this'. Your phone calculates how long each signal took to arrive and, from at least four satellites, finds your position. Because the signals travel at the speed of light, an error of one millionth of a second in the clock means an error of about three hundred metres on the ground."),
  L("Δημοσιογράφος", "f", "Και πού μπαίνει ο Αϊνστάιν;", "And where does Einstein come in?"),
  L("Φυσικός", "m", "Στα ρολόγια των δορυφόρων. Σύμφωνα με την ειδική σχετικότητα, ένα ρολόι που κινείται γρήγορα πηγαίνει πιο αργά· αυτό κοστίζει στους δορυφόρους περίπου επτά μικροδευτερόλεπτα την ημέρα. Σύμφωνα με τη γενική σχετικότητα, όμως, όσο πιο ασθενής είναι η βαρύτητα, τόσο πιο γρήγορα κυλάει ο χρόνος, και στα είκοσι χιλιάδες χιλιόμετρα ύψος τα ρολόγια κερδίζουν περίπου σαράντα πέντε. Το αποτέλεσμα είναι ότι πηγαίνουν μπροστά περίπου τριάντα οκτώ μικροδευτερόλεπτα κάθε μέρα.", "In the satellites' clocks. According to special relativity, a clock that moves fast runs slower; this costs the satellites about seven microseconds a day. According to general relativity, however, the weaker gravity is, the faster time flows, and at twenty thousand kilometres up the clocks gain about forty-five. The result is that they run fast by about thirty-eight microseconds every day."),
  L("Φυσικός", "m", "Αν δεν διορθωνόταν αυτή η διαφορά, το σφάλμα θα συσσωρευόταν κατά περίπου δέκα χιλιόμετρα την ημέρα. Γι' αυτό τα ρολόγια ρυθμίζονται ώστε να πηγαίνουν ελάχιστα πιο αργά πριν καν εκτοξευτούν. Κάθε φορά που ανοίγετε έναν χάρτη στο κινητό, επιβεβαιώνετε, χωρίς να το ξέρετε, μια θεωρία του 1915.", "If this difference weren't corrected, the error would build up by about ten kilometres a day. That's why the clocks are adjusted to run very slightly slower before they are even launched. Every time you open a map on your phone, you confirm, without knowing it, a theory from 1915."),
 ],
 "questions": [
  Q("Γιατί ένα μικρό λάθος στο ρολόι προκαλεί μεγάλο λάθος στη θέση;", ["Γιατί οι δορυφόροι κινούνται αργά", "Γιατί τα σήματα ταξιδεύουν με την ταχύτητα του φωτός", "Γιατί το κινητό έχει μικρή κεραία", "Γιατί υπάρχουν λίγοι δορυφόροι"], 1, "τα σήματα ταξιδεύουν με την ταχύτητα του φωτός"),
  Q("Ποιο είναι το συνολικό αποτέλεσμα των δύο φαινομένων στα ρολόγια των δορυφόρων;", ["Πηγαίνουν πίσω επτά μικροδευτερόλεπτα την ημέρα", "Δεν αλλάζει τίποτα, γιατί τα φαινόμενα αλληλοαναιρούνται", "Πηγαίνουν μπροστά περίπου τριάντα οκτώ μικροδευτερόλεπτα την ημέρα", "Σταματούν για λίγο κάθε μέρα"], 2, "πηγαίνουν μπροστά περίπου τριάντα οκτώ μικροδευτερόλεπτα κάθε μέρα"),
  Q("Πώς αντιμετωπίζεται το πρόβλημα;", ["Τα ρολόγια ρυθμίζονται να πηγαίνουν ελάχιστα πιο αργά πριν από την εκτόξευση", "Οι δορυφόροι κατεβαίνουν χαμηλότερα", "Το κινητό διορθώνει τη θέση με την πυξίδα", "Δεν αντιμετωπίζεται· το λάθος είναι αμελητέο"], 0, "τα ρολόγια ρυθμίζονται ώστε να πηγαίνουν ελάχιστα πιο αργά πριν καν εκτοξευτούν"),
 ],
 "gloss": {"δορυφορικού εντοπισμού": "δορυφορικός εντοπισμός — satellite positioning", "εκπέμπουν": "εκπέμπω — to broadcast, emit", "εκατομμυριοστού": "εκατομμυριοστό — millionth", "ειδική σχετικότητα": "ειδική σχετικότητα — special relativity", "μικροδευτερόλεπτα": "μικροδευτερόλεπτο — microsecond", "γενική σχετικότητα": "γενική σχετικότητα — general relativity", "ασθενής": "ασθενής — weak (also: patient)", "βαρύτητα": "βαρύτητα — gravity", "κυλάει": "κυλάω — to flow, roll (of time)", "συσσωρευόταν": "συσσωρεύομαι — to accumulate", "εκτοξευτούν": "εκτοξεύομαι — to be launched"},
})

ITEMS.append({
 "id": "l176-c1-giati-vrazei-nerotera-sto-vouno", "title": "Γιατί το νερό βράζει πιο εύκολα στο βουνό", "title_en": "Why water boils more easily in the mountains", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια χημικό να εξηγεί σε μια ραδιοφωνική εκπομπή γιατί το σημείο βρασμού του νερού αλλάζει με το υψόμετρο.",
 "script": [
  L("Χημικός", "f", "Μαθαίνουμε στο σχολείο ότι το νερό βράζει στους εκατό βαθμούς. Αυτό ισχύει, αλλά μόνο στο επίπεδο της θάλασσας. Το νερό βράζει όταν η πίεση των υδρατμών που σχηματίζονται μέσα του γίνει ίση με την πίεση της ατμόσφαιρας που το πιέζει από πάνω. Όσο ανεβαίνουμε, ο αέρας αραιώνει και η πίεση μειώνεται, οπότε το νερό φτάνει σε αυτό το σημείο πιο γρήγορα, σε χαμηλότερη θερμοκρασία.", "We learn at school that water boils at a hundred degrees. That's true, but only at sea level. Water boils when the pressure of the vapour forming inside it becomes equal to the pressure of the atmosphere pressing on it from above. The higher we go, the thinner the air and the lower the pressure, so water reaches that point sooner, at a lower temperature."),
  L("Χημικός", "f", "Ένας πρακτικός κανόνας είναι ότι το σημείο βρασμού πέφτει περίπου έναν βαθμό για κάθε τριακόσια μέτρα υψόμετρο. Στην κορυφή του Ολύμπου, λοιπόν, το νερό βράζει γύρω στους ενενήντα βαθμούς, και στην κορυφή του Έβερεστ κάπου κοντά στους εβδομήντα.", "A rule of thumb is that the boiling point drops by about one degree for every three hundred metres of altitude. At the top of Olympus, then, water boils at around ninety degrees, and at the top of Everest somewhere close to seventy."),
  L("Χημικός", "f", "Το παράδοξο είναι ότι το νερό βράζει πιο εύκολα, αλλά το φαγητό μαγειρεύεται πιο δύσκολα. Τα μακαρόνια και τα όσπρια χρειάζονται θερμοκρασία, όχι φυσαλίδες. Γι' αυτό οι ορειβάτες χρησιμοποιούν συχνά χύτρες ταχύτητας: η χύτρα κλείνει ερμητικά, η πίεση μέσα ανεβαίνει και το νερό βράζει πάνω από τους εκατό βαθμούς, γύρω στους εκατόν είκοσι. Με άλλα λόγια, η χύτρα ταχύτητας είναι ένα μικρό κομμάτι επιπέδου θάλασσας, ή και καλύτερο, που το κουβαλάμε στην πλάτη μας.", "The paradox is that water boils more easily, but food cooks with more difficulty. Pasta and pulses need temperature, not bubbles. That's why mountaineers often use pressure cookers: the cooker seals hermetically, the pressure inside rises and the water boils above a hundred degrees, at around a hundred and twenty. In other words, the pressure cooker is a little piece of sea level, or even better, that we carry on our backs."),
 ],
 "questions": [
  Q("Πότε βράζει το νερό;", ["Όταν φτάσει πάντα στους εκατό βαθμούς", "Όταν η πίεση των υδρατμών γίνει ίση με την ατμοσφαιρική πίεση", "Όταν ο αέρας γίνει πιο πυκνός", "Όταν προστεθεί αλάτι"], 1, "όταν η πίεση των υδρατμών που σχηματίζονται μέσα του γίνει ίση με την πίεση της ατμόσφαιρας"),
  Q("Γιατί το φαγητό μαγειρεύεται πιο δύσκολα στο βουνό;", ["Γιατί το νερό δεν βράζει καθόλου", "Γιατί η φωτιά καίει πιο αδύναμα", "Γιατί το νερό βράζει σε χαμηλότερη θερμοκρασία", "Γιατί τα τρόφιμα είναι παγωμένα"], 2, "Τα μακαρόνια και τα όσπρια χρειάζονται θερμοκρασία, όχι φυσαλίδες"),
  Q("Πώς βοηθά η χύτρα ταχύτητας;", ["Ανεβάζει την πίεση, οπότε το νερό βράζει πάνω από τους εκατό βαθμούς", "Μειώνει την πίεση για να βράσει πιο γρήγορα το νερό", "Ζεσταίνει το φαγητό χωρίς νερό", "Κρατάει το φαγητό ζεστό για ώρες"], 0, "η πίεση μέσα ανεβαίνει και το νερό βράζει πάνω από τους εκατό βαθμούς"),
 ],
 "gloss": {"σημείο βρασμού": "σημείο βρασμού — boiling point", "υψόμετρο": "υψόμετρο — altitude", "υδρατμών": "υδρατμός — water vapour", "αραιώνει": "αραιώνω — to thin out", "πρακτικός κανόνας": "πρακτικός κανόνας — rule of thumb", "παράδοξο": "παράδοξο — paradox", "όσπρια": "όσπρια — pulses, legumes", "φυσαλίδες": "φυσαλίδα — bubble", "ορειβάτες": "ορειβάτης — mountaineer", "χύτρες ταχύτητας": "χύτρα ταχύτητας — pressure cooker", "ερμητικά": "ερμητικά — hermetically, airtight"},
})

rnd = random.Random(176)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-176.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
