# Source for library/listening/listening-53.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l53.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l53-ann-ethniki-chioni", "title": "Κλειστή η εθνική οδός λόγω χιονιού", "title_en": "The motorway closed because of snow", "type": "announcement", "level": "B2",
 "context_el": "Οδηγείτε προς τα Γιάννενα και ακούτε στο ραδιόφωνο ένα δελτίο κυκλοφορίας.",
 "script": [
  L("Εκφωνήτρια", "f", "Και τώρα τα νέα της κυκλοφορίας. Λόγω της έντονης χιονόπτωσης, η Εγνατία Οδός παραμένει κλειστή για όλα τα οχήματα στο τμήμα από τα Γρεβενά μέχρι τα Γιάννενα. Η Τροχαία ζητά από τους οδηγούς να αποφύγουν κάθε μη αναγκαία μετακίνηση στην περιοχή.", "And now the traffic news. Because of heavy snowfall, the Egnatia motorway remains closed to all vehicles on the section from Grevena to Ioannina. The traffic police ask drivers to avoid all non-essential travel in the area."),
  L("Εκφωνήτρια", "f", "Όσοι ταξιδεύουν προς την Ήπειρο μπορούν να χρησιμοποιήσουν την εθνική οδό Αντιρρίου – Ιωαννίνων. Στον ορεινό δρόμο από την Καλαμπάκα προς το Μέτσοβο η κυκλοφορία επιτρέπεται μόνο σε οχήματα με αντιολισθητικές αλυσίδες.", "Those travelling to Epirus can use the Antirrio – Ioannina highway. On the mountain road from Kalambaka to Metsovo, traffic is allowed only for vehicles with snow chains."),
  L("Εκφωνήτρια", "f", "Τα εκχιονιστικά μηχανήματα εργάζονται συνεχώς, και η Εγνατία αναμένεται να ανοίξει ξανά αύριο το πρωί, εφόσον σταματήσει η χιονόπτωση. Θα σας ενημερώνουμε κάθε μισή ώρα.", "Snowploughs are working non-stop, and the Egnatia is expected to reopen tomorrow morning, provided the snowfall stops. We'll keep you updated every half hour."),
 ],
 "questions": [
  Q("Ποιο τμήμα της Εγνατίας είναι κλειστό;", ["Από τη Θεσσαλονίκη μέχρι τα Γρεβενά", "Από τα Γρεβενά μέχρι τα Γιάννενα", "Από την Καλαμπάκα μέχρι το Μέτσοβο", "Όλη η Εγνατία"], 1, "στο τμήμα από τα Γρεβενά μέχρι τα Γιάννενα"),
  Q("Ποια οχήματα μπορούν να κινηθούν από την Καλαμπάκα προς το Μέτσοβο;", ["Μόνο τα φορτηγά", "Μόνο όσα έχουν αντιολισθητικές αλυσίδες", "Όλα τα οχήματα", "Κανένα όχημα"], 1, "η κυκλοφορία επιτρέπεται μόνο σε οχήματα με αντιολισθητικές αλυσίδες"),
  Q("Πότε αναμένεται να ανοίξει ξανά η Εγνατία;", ["Απόψε", "Αύριο το πρωί, αν σταματήσει η χιονόπτωση", "Σε μία εβδομάδα", "Σε μισή ώρα"], 1, "αναμένεται να ανοίξει ξανά αύριο το πρωί, εφόσον σταματήσει η χιονόπτωση"),
 ],
 "gloss": {"δελτίο κυκλοφορίας": "δελτίο κυκλοφορίας — traffic bulletin", "χιονόπτωσης": "χιονόπτωση — snowfall", "Τροχαία": "Τροχαία — traffic police", "μη αναγκαία μετακίνηση": "μη αναγκαία μετακίνηση — non-essential travel", "αντιολισθητικές αλυσίδες": "αντιολισθητικές αλυσίδες — snow chains", "εκχιονιστικά μηχανήματα": "εκχιονιστικό μηχάνημα — snowplough", "εφόσον": "εφόσον — provided that, as long as"},
})

ITEMS.append({
 "id": "l53-vm-dikigoros", "title": "Μήνυμα από τη δικηγόρο", "title_en": "A message from the lawyer", "type": "voicemail", "level": "B2",
 "context_el": "Μετά τον θάνατο της θείας σας, ασχολείστε με την κληρονομιά της. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τη δικηγόρο σας.",
 "script": [
  L("Δικηγόρος", "f", "Καλημέρα, κύριε Ζαχαρίου, η Νικολέτα Ρούσσου είμαι, από το δικηγορικό γραφείο. Σας τηλεφωνώ για την κληρονομιά της θείας σας. Πήραμε επιτέλους το πιστοποιητικό από το ληξιαρχείο, οπότε μπορούμε να προχωρήσουμε στην αποδοχή της κληρονομιάς.", "Good morning, Mr Zachariou, it's Nikoleta Roussou from the law office. I'm calling about your aunt's inheritance. We've finally got the certificate from the registry office, so we can proceed with accepting the inheritance."),
  L("Δικηγόρος", "f", "Για να ετοιμάσει ο συμβολαιογράφος την πράξη, χρειάζομαι ακόμη δύο έγγραφα: το πιστοποιητικό πλησιεστέρων συγγενών και ένα πρόσφατο αντίγραφο του εκκαθαριστικού σας. Το πρώτο το βγάζετε από τον δήμο, το δεύτερο το κατεβάζετε από το διαδίκτυο.", "For the notary to prepare the deed, I still need two documents: the certificate of next of kin and a recent copy of your tax assessment. You get the first from the town hall; you can download the second from the internet."),
  L("Δικηγόρος", "f", "Προσέξτε μόνο ότι η προθεσμία για τη δήλωση στην εφορία λήγει στο τέλος του μήνα. Αν μου τα στείλετε μέχρι την Παρασκευή, προλαβαίνουμε άνετα. Για οποιαδήποτε απορία, είμαι στο γραφείο μέχρι τις τρεις.", "Just note that the deadline for the declaration to the tax office expires at the end of the month. If you send them to me by Friday, we'll comfortably make it. For any questions, I'm in the office until three."),
 ],
 "questions": [
  Q("Τι πήρε επιτέλους η δικηγόρος;", ["Την πράξη του συμβολαιογράφου", "Το πιστοποιητικό από το ληξιαρχείο", "Το εκκαθαριστικό", "Τα κλειδιά του σπιτιού"], 1, "Πήραμε επιτέλους το πιστοποιητικό από το ληξιαρχείο"),
  Q("Από πού βγαίνει το πιστοποιητικό πλησιεστέρων συγγενών;", ["Από την εφορία", "Από τον δήμο", "Από το διαδίκτυο", "Από τον συμβολαιογράφο"], 1, "Το πρώτο το βγάζετε από τον δήμο"),
  Q("Γιατί πρέπει να βιαστεί ο κ. Ζαχαρίου;", ["Γιατί η δικηγόρος φεύγει για διακοπές", "Γιατί η προθεσμία για τη δήλωση στην εφορία λήγει στο τέλος του μήνα", "Γιατί το σπίτι θα πουληθεί", "Γιατί ο συμβολαιογράφος κλείνει"], 1, "η προθεσμία για τη δήλωση στην εφορία λήγει στο τέλος του μήνα"),
 ],
 "gloss": {"κληρονομιά": "κληρονομιά — inheritance", "δικηγορικό γραφείο": "δικηγορικό γραφείο — law office", "ληξιαρχείο": "ληξιαρχείο — registry office (births, deaths, marriages)", "αποδοχή": "αποδοχή — acceptance", "συμβολαιογράφος": "συμβολαιογράφος — notary", "πράξη": "πράξη — (notarial) deed; act", "πλησιεστέρων συγγενών": "πλησιέστεροι συγγενείς — next of kin", "εκκαθαριστικού": "εκκαθαριστικό — tax assessment notice", "προθεσμία": "προθεσμία — deadline", "εφορία": "εφορία — tax office"},
})

ITEMS.append({
 "id": "l53-dia-exoda", "title": "Μοιράζοντας τα έξοδα των διακοπών", "title_en": "Splitting the holiday costs", "type": "dialogue", "level": "B2",
 "context_el": "Η Ιωάννα και ο Φώτης γύρισαν από διακοπές στην Κρήτη με δύο ακόμη φίλους και λογαριάζουν τα έξοδα.",
 "script": [
  L("Ιωάννα", "f", "Λοιπόν, ας τα λογαριάσουμε να τελειώνουμε. Το σπίτι ήταν οχτακόσια ευρώ για τη βδομάδα, και το πλήρωσα εγώ με την κάρτα μου.", "Right, let's work it out and get it over with. The house was eight hundred euros for the week, and I paid it with my card."),
  L("Φώτης", "m", "Εντάξει. Εγώ πλήρωσα το αυτοκίνητο, διακόσια σαράντα, και τη βενζίνη, γύρω στα ογδόντα. Ο Στέλιος πλήρωσε τα περισσότερα σούπερ μάρκετ.", "OK. I paid for the car, two hundred and forty, and the petrol, about eighty. Stelios paid for most of the supermarket shopping."),
  L("Ιωάννα", "f", "Και η Ρένα; Αυτή δεν πλήρωσε σχεδόν τίποτα, εκτός από ένα δυο τραπέζια σε ταβέρνες.", "And Rena? She paid almost nothing, apart from one or two meals at tavernas."),
  L("Φώτης", "m", "Ναι, αλλά μην ξεχνάς ότι έμεινε μόνο πέντε μέρες, όχι επτά. Δεν είναι δίκαιο να πληρώσει όσο εμείς για το σπίτι.", "Yes, but don't forget she only stayed five days, not seven. It isn't fair for her to pay as much as us for the house."),
  L("Ιωάννα", "f", "Σωστό. Τότε προτείνω το σπίτι να το μοιράσουμε ανάλογα με τις μέρες, και όλα τα άλλα στα τέσσερα. Θα τα βάλω σε μια εφαρμογή που τα υπολογίζει μόνη της, για να μη μαλώνουμε.", "Fair point. Then I suggest we split the house according to the days, and everything else four ways. I'll put it all into an app that calculates it by itself, so we don't argue."),
  L("Φώτης", "m", "Τέλεια. Και την επόμενη φορά ας ανοίξουμε έναν κοινό κουμπαρά από την αρχή.", "Perfect. And next time let's set up a shared kitty from the start."),
 ],
 "questions": [
  Q("Τι πλήρωσε η Ιωάννα;", ["Το αυτοκίνητο", "Το σπίτι", "Τα σούπερ μάρκετ", "Τη βενζίνη"], 1, "Το σπίτι ήταν οχτακόσια ευρώ για τη βδομάδα, και το πλήρωσα εγώ"),
  Q("Γιατί η Ρένα δεν πρέπει να πληρώσει όσο οι άλλοι για το σπίτι;", ["Γιατί πλήρωσε τις ταβέρνες", "Γιατί έμεινε πέντε μέρες αντί για επτά", "Γιατί δεν έχει χρήματα", "Γιατί κοιμόταν στο σαλόνι"], 1, "έμεινε μόνο πέντε μέρες, όχι επτά"),
  Q("Τι θα κάνει η Ιωάννα για να μη μαλώσουν;", ["Θα πληρώσει η ίδια τη διαφορά", "Θα βάλει τα έξοδα σε μια εφαρμογή που τα υπολογίζει", "Θα ζητήσει από τον Στέλιο να τα λογαριάσει", "Θα στείλει μήνυμα στη Ρένα"], 1, "Θα τα βάλω σε μια εφαρμογή που τα υπολογίζει μόνη της, για να μη μαλώνουμε"),
 ],
 "gloss": {"λογαριάζουν": "λογαριάζω — to work out, reckon up", "να τελειώνουμε": "να τελειώνουμε — (and) get it over with", "δίκαιο": "δίκαιος — fair", "ανάλογα με": "ανάλογα με — according to, depending on", "στα τέσσερα": "στα τέσσερα — four ways", "εφαρμογή": "εφαρμογή — app", "κοινό κουμπαρά": "κοινός κουμπαράς — shared kitty"},
})

ITEMS.append({
 "id": "l53-dia-apokries", "title": "Μια στολή για τις Απόκριες", "title_en": "A carnival costume", "type": "dialogue", "level": "B2",
 "context_el": "Η Μαρίνα και ο Γιώργος συζητούν τι στολή θα φορέσει ο εξάχρονος γιος τους στο αποκριάτικο πάρτι του σχολείου.",
 "script": [
  L("Μαρίνα", "f", "Ο Άγγελος θέλει να ντυθεί δεινόσαυρος. Είδα μια στολή στο διαδίκτυο, αλλά κοστίζει πενήντα ευρώ και θα τη φορέσει μία φορά.", "Angelos wants to dress up as a dinosaur. I saw a costume online, but it costs fifty euros and he'll wear it once."),
  L("Γιώργος", "m", "Πενήντα ευρώ; Μα δεν γίνεται να τη φτιάξουμε μόνοι μας; Ένα πράσινο φούτερ με κουκούλα, λίγο τσόχινο ύφασμα για τα αγκάθια στην πλάτη, και είμαστε έτοιμοι.", "Fifty euros? Can't we make it ourselves? A green hoodie, a bit of felt for the spikes on the back, and we're done."),
  L("Μαρίνα", "f", "Θα το έκανα με χαρά, αλλά το πάρτι είναι την Παρασκευή, και εγώ δουλεύω μέχρι αργά όλη την εβδομάδα.", "I'd do it gladly, but the party is on Friday, and I'm working late all week."),
  L("Γιώργος", "m", "Αναλαμβάνω εγώ. Το Σάββατο θα τη φτιάξουμε μαζί με τον Άγγελο. Θα του αρέσει περισσότερο αν τη φτιάξει κι ο ίδιος.", "I'll take care of it. On Saturday we'll make it together with Angelos. He'll like it more if he makes it himself too."),
  L("Μαρίνα", "f", "Το Σάββατο είναι μετά το πάρτι, Γιώργο!", "Saturday is after the party, Giorgos!"),
  L("Γιώργος", "m", "Α, σωστά... Τότε την Τετάρτη το απόγευμα. Θα φύγω νωρίτερα από τη δουλειά. Πάντως το φούτερ θα του χρησιμεύσει και μετά, για το σχολείο.", "Ah, right... Then on Wednesday afternoon. I'll leave work earlier. Anyway, the hoodie will be useful for school afterwards too."),
 ],
 "questions": [
  Q("Γιατί η Μαρίνα διστάζει να αγοράσει τη στολή;", ["Γιατί δεν αρέσει στον Άγγελο", "Γιατί είναι ακριβή και θα τη φορέσει μία φορά", "Γιατί δεν υπάρχει στο μέγεθός του", "Γιατί θα αργήσει να έρθει"], 1, "κοστίζει πενήντα ευρώ και θα τη φορέσει μία φορά"),
  Q("Ποιο λάθος κάνει ο Γιώργος;", ["Ξεχνάει ότι ο Άγγελος θέλει να γίνει πειρατής", "Προτείνει το Σάββατο, που είναι μετά το πάρτι", "Αγοράζει λάθος ύφασμα", "Μπερδεύει το σχολείο"], 1, "Το Σάββατο είναι μετά το πάρτι"),
  Q("Γιατί, κατά τον Γιώργο, δεν θα πάνε χαμένα τα χρήματα για το φούτερ;", ["Γιατί θα το φορέσει ο ίδιος", "Γιατί ο Άγγελος θα το φοράει και μετά στο σχολείο", "Γιατί θα το επιστρέψουν", "Γιατί θα το χαρίσουν σε έναν φίλο"], 1, "το φούτερ θα του χρησιμεύσει και μετά, για το σχολείο"),
 ],
 "gloss": {"αποκριάτικο": "αποκριάτικος — carnival (adj.)", "ντυθεί": "ντύνομαι — to dress up (as)", "φούτερ με κουκούλα": "φούτερ με κουκούλα — hoodie", "τσόχινο": "τσόχινος — (made of) felt", "αγκάθια": "αγκάθι — thorn, spike", "Αναλαμβάνω": "αναλαμβάνω — to take on, take charge of", "θα του χρησιμεύσει": "χρησιμεύω — to be useful, serve"},
})

ITEMS.append({
 "id": "l53-int-icholiptria", "title": "Η ηχολήπτρια", "title_en": "The sound engineer", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με την Αλεξάνδρα, ηχολήπτρια σε συναυλίες και θεατρικές παραστάσεις.",
 "script": [
  L("Δημοσιογράφος", "m", "Αλεξάνδρα, τι ακριβώς κάνει μια ηχολήπτρια;", "Alexandra, what exactly does a sound engineer do?"),
  L("Αλεξάνδρα", "f", "Φροντίζω ώστε ο ήχος να φτάνει καθαρός σε κάθε θέση της αίθουσας, από την πρώτη σειρά μέχρι την τελευταία. Σε μια συναυλία ρυθμίζω την ένταση κάθε οργάνου και κάθε φωνής, ώστε να μην καλύπτει το ένα το άλλο. Αν κάνω καλά τη δουλειά μου, κανείς δεν με προσέχει.", "I make sure the sound reaches every seat in the hall clearly, from the front row to the back. At a concert I adjust the volume of each instrument and each voice so that none covers the others. If I do my job well, nobody notices me."),
  L("Δημοσιογράφος", "m", "Είναι ένα επάγγελμα όπου οι γυναίκες είναι λίγες. Το έχετε νιώσει;", "It's a profession where there are few women. Have you felt that?"),
  L("Αλεξάνδρα", "f", "Στην αρχή, πολύ. Θυμάμαι μουσικούς που ρωτούσαν πού είναι ο ηχολήπτης, ενώ εγώ στεκόμουν δίπλα τους με τα καλώδια στο χέρι. Σήμερα τα πράγματα έχουν αλλάξει, και στις σχολές ήχου βλέπω όλο και περισσότερες κοπέλες.", "At first, very much. I remember musicians asking where the sound engineer was while I was standing next to them with the cables in my hand. Things have changed today, and in sound schools I see more and more young women."),
  L("Δημοσιογράφος", "m", "Ποια είναι η πιο δύσκολη στιγμή που έχετε ζήσει;", "What's the most difficult moment you've experienced?"),
  L("Αλεξάνδρα", "f", "Μια συναυλία στο αρχαίο θέατρο της Επιδαύρου. Εκεί η ακουστική είναι τόσο τέλεια, που κάθε λάθος ακούγεται μέχρι την κορυφή. Πριν από την παράσταση δεν κοιμήθηκα όλο το βράδυ. Στο τέλος, όμως, ήταν η πιο όμορφη βραδιά της ζωής μου.", "A concert at the ancient theatre of Epidaurus. The acoustics there are so perfect that every mistake can be heard right up to the top. I didn't sleep all night before the performance. In the end, though, it was the most beautiful evening of my life."),
 ],
 "questions": [
  Q("Πότε, κατά την Αλεξάνδρα, έχει κάνει καλά τη δουλειά της;", ["Όταν το κοινό τη χειροκροτεί", "Όταν κανείς δεν την προσέχει", "Όταν ο ήχος είναι πολύ δυνατός", "Όταν τελειώνει νωρίς"], 1, "Αν κάνω καλά τη δουλειά μου, κανείς δεν με προσέχει"),
  Q("Τι συνέβαινε στην αρχή της καριέρας της;", ["Δεν έβρισκε δουλειά", "Οι μουσικοί ρωτούσαν πού είναι ο ηχολήπτης, ενώ εκείνη ήταν δίπλα τους", "Της χάλαγαν τα μηχανήματα", "Δούλευε χωρίς πληρωμή"], 1, "μουσικούς που ρωτούσαν πού είναι ο ηχολήπτης, ενώ εγώ στεκόμουν δίπλα τους"),
  Q("Γιατί ήταν δύσκολη η συναυλία στην Επίδαυρο;", ["Γιατί έβρεχε", "Γιατί η ακουστική είναι τόσο τέλεια που ακούγεται κάθε λάθος", "Γιατί δεν υπήρχε ρεύμα", "Γιατί ήταν η πρώτη της συναυλία"], 1, "η ακουστική είναι τόσο τέλεια, που κάθε λάθος ακούγεται μέχρι την κορυφή"),
 ],
 "gloss": {"ηχολήπτρια": "ηχολήπτρια — sound engineer (woman)", "ρυθμίζω": "ρυθμίζω — to adjust, set", "ένταση": "ένταση — volume; intensity", "καλύπτει": "καλύπτω — to cover", "καλώδια": "καλώδιο — cable", "σχολές ήχου": "σχολή ήχου — sound-engineering school", "ακουστική": "ακουστική — acoustics", "κορυφή": "κορυφή — top, summit"},
})

ITEMS.append({
 "id": "l53-rep-fotismos", "title": "Ο νέος φωτισμός της Ακρόπολης", "title_en": "The new lighting of the Acropolis", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ για τον φωτισμό της Ακρόπολης.",
 "script": [
  L("Ρεπόρτερ", "m", "Είναι εννιά το βράδυ και βρίσκομαι στον λόφο του Φιλοπάππου, απέναντι από την Ακρόπολη. Ο Παρθενώνας λάμπει μέσα στο σκοτάδι με ένα απαλό, ζεστό φως, που αφήνει να φαίνονται οι λεπτομέρειες του μαρμάρου.", "It's nine in the evening and I'm on Philopappos Hill, opposite the Acropolis. The Parthenon is glowing in the dark with a soft, warm light that lets the details of the marble show."),
  L("Ρεπόρτερ", "m", "Ο σημερινός φωτισμός εγκαινιάστηκε το 2020 και αντικατέστησε τους παλιούς προβολείς, που έριχναν ένα έντονο κιτρινωπό φως και έκαναν το μνημείο να μοιάζει επίπεδο. Τα νέα φωτιστικά, τεχνολογίας LED, φωτίζουν κάθε κίονα και κάθε τοίχο χωριστά, έτσι ώστε να αναδεικνύεται ο όγκος των κτιρίων.", "Today's lighting was inaugurated in 2020 and replaced the old floodlights, which cast a harsh yellowish light and made the monument look flat. The new LED fixtures light each column and each wall separately, so that the volume of the buildings stands out."),
  L("Ρεπόρτερ", "m", "Το έργο σχεδιάστηκε έτσι ώστε να καταναλώνει πολύ λιγότερη ενέργεια από το παλιό σύστημα. Και όπως μου είπε ένας ηλικιωμένος Αθηναίος που κάθεται δίπλα μου στο παγκάκι, «Τώρα η Ακρόπολη μοιάζει πιο κοντινή. Σαν να μπορείς να την αγγίξεις.»", "The project was designed to consume much less energy than the old system. And as an elderly Athenian sitting next to me on the bench told me, 'Now the Acropolis looks closer. As if you could touch it.'"),
 ],
 "questions": [
  Q("Από πού κάνει το ρεπορτάζ ο δημοσιογράφος;", ["Από το Μουσείο της Ακρόπολης", "Από τον λόφο του Φιλοπάππου", "Από την Πλάκα", "Από το Σύνταγμα"], 1, "βρίσκομαι στον λόφο του Φιλοπάππου, απέναντι από την Ακρόπολη"),
  Q("Ποιο ήταν το πρόβλημα με τον παλιό φωτισμό;", ["Ήταν πολύ σκοτεινός", "Έριχνε έντονο κιτρινωπό φως και έκανε το μνημείο να μοιάζει επίπεδο", "Χαλούσε συχνά", "Ενοχλούσε τους κατοίκους"], 1, "έριχναν ένα έντονο κιτρινωπό φως και έκαναν το μνημείο να μοιάζει επίπεδο"),
  Q("Τι πλεονέκτημα έχει το νέο σύστημα εκτός από την εμφάνιση;", ["Είναι πιο φτηνό στην κατασκευή", "Καταναλώνει πολύ λιγότερη ενέργεια", "Αλλάζει χρώματα", "Λειτουργεί όλη τη νύχτα"], 1, "σχεδιάστηκε έτσι ώστε να καταναλώνει πολύ λιγότερη ενέργεια από το παλιό σύστημα"),
 ],
 "gloss": {"φωτισμός": "φωτισμός — lighting", "λάμπει": "λάμπω — to shine, glow", "απαλό": "απαλός — soft, gentle", "εγκαινιάστηκε": "εγκαινιάζομαι — to be inaugurated", "προβολείς": "προβολέας — floodlight, spotlight", "κιτρινωπό": "κιτρινωπός — yellowish", "φωτιστικά": "φωτιστικό — light fixture", "κίονα": "κίονας — column", "αναδεικνύεται": "αναδεικνύομαι — to be brought out, highlighted", "όγκος": "όγκος — volume, mass"},
})

ITEMS.append({
 "id": "l53-dia-nipiagogeio", "title": "Η πρώτη μέρα στο νηπιαγωγείο", "title_en": "The first day at nursery school", "type": "dialogue", "level": "B2",
 "context_el": "Η Κατερίνα πηγαίνει την τετράχρονη κόρη της στο νηπιαγωγείο για πρώτη φορά και μιλάει με τη νηπιαγωγό.",
 "script": [
  L("Κατερίνα", "f", "Καλημέρα. Είμαι η μητέρα της Δάφνης. Είναι η πρώτη της μέρα, και να σας πω την αλήθεια, ανησυχώ περισσότερο εγώ από εκείνη.", "Good morning. I'm Daphne's mother. It's her first day, and to tell you the truth, I'm more worried than she is."),
  L("Νηπιαγωγός", "f", "Είναι απόλυτα φυσικό. Τις πρώτες μέρες σας προτείνω να μένετε μαζί της μισή ώρα στην τάξη, και σιγά σιγά να φεύγετε πιο νωρίς. Το σημαντικό είναι να της λέτε πάντα ότι φεύγετε. Μην εξαφανίζεστε κρυφά, γιατί τότε χάνει την εμπιστοσύνη της.", "That's perfectly natural. For the first few days I suggest you stay with her in the classroom for half an hour, and gradually leave earlier. The important thing is to always tell her you're leaving. Don't disappear secretly, because then she loses her trust."),
  L("Κατερίνα", "f", "Καταλαβαίνω. Και αν κλάψει;", "I understand. And if she cries?"),
  L("Νηπιαγωγός", "f", "Μάλλον θα κλάψει, και αυτό δεν είναι κακό. Συνήθως ηρεμούν λίγα λεπτά αφού φύγει ο γονιός. Αν δεν ηρεμήσει, θα σας τηλεφωνήσω, σας το υπόσχομαι.", "She probably will cry, and that's not a bad thing. They usually calm down a few minutes after the parent leaves. If she doesn't calm down, I'll call you, I promise."),
  L("Κατερίνα", "f", "Να της φέρω κάτι από το σπίτι; Έχει ένα λαγουδάκι που το παίρνει παντού.", "Should I bring her something from home? She has a little rabbit she takes everywhere."),
  L("Νηπιαγωγός", "f", "Φυσικά, φέρτε το. Ένα γνώριμο αντικείμενο βοηθάει πολύ. Μόνο γράψτε πάνω του το όνομά της, γιατί εδώ έχουμε τρία ίδια λαγουδάκια!", "Of course, bring it. A familiar object helps a lot. Just write her name on it, because we have three identical rabbits here!"),
 ],
 "questions": [
  Q("Τι συμβουλεύει η νηπιαγωγός για τις πρώτες μέρες;", ["Να φεύγει η μητέρα αμέσως", "Να μένει η μητέρα μισή ώρα και σιγά σιγά να φεύγει νωρίτερα", "Να μην έρθει η Δάφνη όλη την ημέρα", "Να τη φέρνει ο πατέρας"], 1, "να μένετε μαζί της μισή ώρα στην τάξη, και σιγά σιγά να φεύγετε πιο νωρίς"),
  Q("Γιατί δεν πρέπει να φεύγει η μητέρα κρυφά;", ["Γιατί η Δάφνη θα χαθεί", "Γιατί το παιδί χάνει την εμπιστοσύνη του", "Γιατί απαγορεύεται από τον κανονισμό", "Γιατί η νηπιαγωγός πρέπει να υπογράψει"], 1, "Μην εξαφανίζεστε κρυφά, γιατί τότε χάνει την εμπιστοσύνη της"),
  Q("Γιατί πρέπει να γράψει το όνομα της Δάφνης στο λαγουδάκι;", ["Για να μην το πάρει άλλο παιδί στο σπίτι", "Γιατί στην τάξη υπάρχουν τρία ίδια λαγουδάκια", "Γιατί το ζητάει ο κανονισμός", "Για να μάθει η Δάφνη να διαβάζει"], 1, "εδώ έχουμε τρία ίδια λαγουδάκια"),
 ],
 "gloss": {"νηπιαγωγείο": "νηπιαγωγείο — nursery school, kindergarten", "νηπιαγωγό": "νηπιαγωγός — nursery-school teacher", "σιγά σιγά": "σιγά σιγά — gradually, little by little", "εξαφανίζεστε": "εξαφανίζομαι — to disappear", "εμπιστοσύνη": "εμπιστοσύνη — trust", "ηρεμούν": "ηρεμώ — to calm down", "λαγουδάκι": "λαγουδάκι — little rabbit, bunny", "γνώριμο": "γνώριμος — familiar"},
})

ITEMS.append({
 "id": "l53-mono-katharismos", "title": "Πριν από τον καθαρισμό της παραλίας", "title_en": "Before the beach clean-up", "type": "monologue", "level": "B2",
 "context_el": "Συμμετέχετε ως εθελοντής σε έναν καθαρισμό παραλίας. Θα ακούσετε τη συντονίστρια να δίνει οδηγίες πριν ξεκινήσετε.",
 "script": [
  L("Συντονίστρια", "f", "Καλημέρα σε όλους και ευχαριστούμε που ήρθατε! Σήμερα θα καθαρίσουμε την παραλία από τον φάρο μέχρι το ρέμα, περίπου ενάμισι χιλιόμετρο. Χωριζόμαστε σε ομάδες των πέντε ατόμων, και κάθε ομάδα αναλαμβάνει ένα κομμάτι.", "Good morning everyone and thank you for coming! Today we'll clean the beach from the lighthouse to the stream, about one and a half kilometres. We're splitting into groups of five, and each group takes on a section."),
  L("Συντονίστρια", "f", "Κάθε ομάδα θα πάρει δύο σακούλες: την μπλε για τα πλαστικά και τα μέταλλα, και τη μαύρη για όλα τα υπόλοιπα. Φοράτε πάντα γάντια. Αν βρείτε σύριγγες ή σπασμένα γυαλιά, μην τα αγγίζετε· φωνάξτε έναν από εμάς με τα κίτρινα γιλέκα.", "Each group will take two bags: the blue one for plastics and metals, and the black one for everything else. Always wear gloves. If you find syringes or broken glass, don't touch them; call one of us in the yellow vests."),
  L("Συντονίστρια", "f", "Κάτι ακόμα: σημειώνουμε σε αυτό το έντυπο τι βρίσκουμε, π.χ. πόσα καπάκια ή πόσα αποτσίγαρα. Τα στοιχεία αυτά τα στέλνουμε σε ένα πανεπιστήμιο που μελετά τη ρύπανση των θαλασσών. Στις δώδεκα τελειώνουμε, και ο δήμος μάς κερνάει φαγητό στην ταβέρνα του λιμανιού.", "One more thing: we note on this form what we find, for example how many bottle caps or how many cigarette butts. We send this data to a university that studies marine pollution. We finish at twelve, and the town council is treating us to food at the harbour taverna."),
 ],
 "questions": [
  Q("Πώς θα οργανωθούν οι εθελοντές;", ["Θα δουλέψουν όλοι μαζί", "Σε ομάδες των πέντε, με ένα κομμάτι η καθεμία", "Σε ζευγάρια", "Ο καθένας μόνος του"], 1, "Χωριζόμαστε σε ομάδες των πέντε ατόμων, και κάθε ομάδα αναλαμβάνει ένα κομμάτι"),
  Q("Τι πρέπει να κάνουν αν βρουν σύριγγες;", ["Να τις βάλουν στη μαύρη σακούλα", "Να μην τις αγγίξουν και να φωνάξουν κάποιον με κίτρινο γιλέκο", "Να τις θάψουν στην άμμο", "Να τις φωτογραφίσουν"], 1, "μην τα αγγίζετε· φωνάξτε έναν από εμάς με τα κίτρινα γιλέκα"),
  Q("Γιατί σημειώνουν τι βρίσκουν;", ["Για να κερδίσει η καλύτερη ομάδα", "Για ένα πανεπιστήμιο που μελετά τη ρύπανση των θαλασσών", "Για να πληρωθούν", "Για τον δήμο, που θα βάλει πρόστιμα"], 1, "Τα στοιχεία αυτά τα στέλνουμε σε ένα πανεπιστήμιο που μελετά τη ρύπανση των θαλασσών"),
 ],
 "gloss": {"καθαρισμό": "καθαρισμός — cleaning, clean-up", "συντονίστρια": "συντονίστρια — coordinator (woman)", "ρέμα": "ρέμα — stream", "Χωριζόμαστε": "χωρίζομαι — to split up, separate", "σύριγγες": "σύριγγα — syringe", "γιλέκα": "γιλέκο — vest, waistcoat", "έντυπο": "έντυπο — form (to fill in)", "καπάκια": "καπάκι — cap, lid", "αποτσίγαρα": "αποτσίγαρο — cigarette butt", "ρύπανση": "ρύπανση — pollution"},
})

ITEMS.append({
 "id": "l53-c1-apexartisi", "title": "Ψηφιακή αποτοξίνωση: λύση ή άλλοθι;", "title_en": "Digital detox: a solution or an alibi?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια ψυχολόγο για τη σχέση μας με τα κινητά τηλέφωνα και την τάση της «ψηφιακής αποτοξίνωσης».",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αλεξίου, όλο και περισσότεροι άνθρωποι μιλούν για «ψηφιακή αποτοξίνωση»: διακοπές χωρίς κινητό, Σαββατοκύριακα εκτός σύνδεσης. Είναι κάτι που λειτουργεί;", "Ms Alexiou, more and more people talk about 'digital detox': holidays without a phone, weekends offline. Is it something that works?"),
  L("Ψυχολόγος", "f", "Βραχυπρόθεσμα, ναι. Οι περισσότεροι αναφέρουν ότι κοιμούνται καλύτερα και νιώθουν λιγότερο άγχος. Το πρόβλημα είναι ότι, μόλις επιστρέψουν, ξαναπέφτουν στις ίδιες συνήθειες, συχνά με ακόμη μεγαλύτερη ένταση, σαν να θέλουν να αναπληρώσουν τον χαμένο χρόνο. Μια σύντομη αποχή δεν αλλάζει από μόνη της τη σχέση μας με την τεχνολογία.", "In the short term, yes. Most report that they sleep better and feel less anxious. The problem is that as soon as they return, they fall back into the same habits, often even more intensely, as if they wanted to make up for lost time. A brief abstinence does not in itself change our relationship with technology."),
  L("Δημοσιογράφος", "m", "Τι προτείνετε, λοιπόν;", "So what do you suggest?"),
  L("Ψυχολόγος", "f", "Μικρές αλλαγές που μπορούν να διατηρηθούν: να απενεργοποιήσουμε τις περισσότερες ειδοποιήσεις, να μη φέρνουμε το κινητό στο υπνοδωμάτιο, να ορίσουμε ώρες της ημέρας χωρίς οθόνες, για παράδειγμα στο φαγητό. Δεν είναι εντυπωσιακές λύσεις, αλλά είναι αυτές που αντέχουν στον χρόνο.", "Small changes that can be sustained: turning off most notifications, not bringing the phone into the bedroom, setting times of day without screens, for example at meals. They aren't spectacular solutions, but they are the ones that stand the test of time."),
  L("Δημοσιογράφος", "m", "Στον τίτλο της ομιλίας σας χρησιμοποιείτε τη λέξη «άλλοθι». Γιατί;", "In the title of your talk you use the word 'alibi'. Why?"),
  L("Ψυχολόγος", "f", "Γιατί φοβάμαι ότι η έννοια της αποτοξίνωσης μεταθέτει όλη την ευθύνη στο άτομο. Μας λέει ότι, αν δεν μπορούμε να αφήσουμε το κινητό, φταίει η δική μας έλλειψη θέλησης. Ξεχνάμε όμως ότι οι εφαρμογές σχεδιάζονται σκόπιμα από ομάδες ειδικών ώστε να μας κρατούν όσο το δυνατόν περισσότερο. Χωρίς κανόνες για τον σχεδιασμό τους, η αποτοξίνωση κινδυνεύει να γίνει άλλο ένα προϊόν που μας πουλάνε για να γιατρέψουμε ένα πρόβλημα που μας πούλησαν.", "Because I fear that the notion of detox shifts all responsibility onto the individual. It tells us that if we can't put the phone down, it's our own lack of willpower that's to blame. But we forget that apps are deliberately designed by teams of experts to keep us hooked as long as possible. Without rules on how they are designed, detox risks becoming yet another product sold to us to cure a problem they sold us."),
 ],
 "questions": [
  Q("Τι συμβαίνει συχνά μετά από μια περίοδο αποτοξίνωσης, σύμφωνα με την ψυχολόγο;", ["Οι άνθρωποι εγκαταλείπουν οριστικά το κινητό", "Ξαναπέφτουν στις ίδιες συνήθειες, συχνά πιο έντονα", "Κοιμούνται χειρότερα", "Αγοράζουν καινούργιο κινητό"], 1, "μόλις επιστρέψουν, ξαναπέφτουν στις ίδιες συνήθειες, συχνά με ακόμη μεγαλύτερη ένταση"),
  Q("Ποια από τις παρακάτω ΔΕΝ είναι μία από τις αλλαγές που προτείνει;", ["Να απενεργοποιήσουμε τις περισσότερες ειδοποιήσεις", "Να διαγράψουμε όλες τις εφαρμογές κοινωνικής δικτύωσης", "Να μη φέρνουμε το κινητό στο υπνοδωμάτιο", "Να ορίσουμε ώρες χωρίς οθόνες"], 1, "Προτείνει ειδοποιήσεις, υπνοδωμάτιο και ώρες χωρίς οθόνες· δεν μιλά για διαγραφή εφαρμογών"),
  Q("Γιατί χαρακτηρίζει την αποτοξίνωση «άλλοθι»;", ["Γιατί δεν έχει επιστημονική βάση", "Γιατί μεταθέτει όλη την ευθύνη στο άτομο, ενώ οι εφαρμογές σχεδιάζονται για να μας κρατούν", "Γιατί είναι πολύ ακριβή", "Γιατί οι νέοι δεν τη δέχονται"], 1, "η έννοια της αποτοξίνωσης μεταθέτει όλη την ευθύνη στο άτομο"),
  Q("Τι εννοεί με τη φράση «ένα προϊόν που μας πουλάνε για να γιατρέψουμε ένα πρόβλημα που μας πούλησαν»;", ["Ότι τα κινητά είναι πολύ ακριβά", "Ότι η ίδια αγορά που δημιούργησε την εξάρτηση πουλάει και τη «θεραπεία» της", "Ότι οι ψυχολόγοι κερδίζουν από το πρόβλημα", "Ότι τα φάρμακα για το άγχος είναι επικίνδυνα"], 1, "οι εφαρμογές σχεδιάζονται σκόπιμα ... η αποτοξίνωση κινδυνεύει να γίνει άλλο ένα προϊόν"),
 ],
 "gloss": {"αποτοξίνωσης": "αποτοξίνωση — detox", "άλλοθι": "άλλοθι — alibi, excuse", "εκτός σύνδεσης": "εκτός σύνδεσης — offline", "Βραχυπρόθεσμα": "βραχυπρόθεσμα — in the short term", "αναπληρώσουν": "αναπληρώνω — to make up for", "αποχή": "αποχή — abstinence, abstaining", "απενεργοποιήσουμε": "απενεργοποιώ — to switch off, disable", "ειδοποιήσεις": "ειδοποίηση — notification", "αντέχουν στον χρόνο": "αντέχω στον χρόνο — to stand the test of time", "μεταθέτει": "μεταθέτω — to shift, transfer", "έλλειψη θέλησης": "έλλειψη θέλησης — lack of willpower", "σκόπιμα": "σκόπιμα — deliberately"},
})

ITEMS.append({
 "id": "l53-c1-sapfo", "title": "Σαπφώ, η δέκατη Μούσα", "title_en": "Sappho, the tenth Muse", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια ομιλία μιας φιλολόγου για την ποιήτρια Σαπφώ.",
 "script": [
  L("Φιλόλογος", "f", "Η Σαπφώ γεννήθηκε στη Λέσβο γύρω στο 630 π.Χ., πιθανότατα στην Ερεσό, και έζησε το μεγαλύτερο μέρος της ζωής της στη Μυτιλήνη. Για τη ζωή της ξέρουμε ελάχιστα με βεβαιότητα: ότι ανήκε σε αριστοκρατική οικογένεια, ότι είχε αδελφούς και μια κόρη, την Κλεΐδα, και ότι για ένα διάστημα έζησε εξόριστη στη Σικελία, πιθανότατα εξαιτίας των πολιτικών συγκρούσεων της εποχής.", "Sappho was born on Lesbos around 630 BC, most probably in Eresos, and lived most of her life in Mytilene. We know very little of her life with certainty: that she belonged to an aristocratic family, that she had brothers and a daughter, Kleis, and that for a time she lived in exile in Sicily, most probably because of the political conflicts of the period."),
  L("Φιλόλογος", "f", "Οι φιλόλογοι της Αλεξάνδρειας συγκέντρωσαν αργότερα τα ποιήματά της σε εννέα βιβλία. Από αυτά, όμως, μόνο ένα ποίημα έχει σωθεί ολόκληρο, ο Ύμνος στην Αφροδίτη· τα υπόλοιπα τα γνωρίζουμε από αποσπάσματα, από παραθέματα άλλων συγγραφέων και από κομμάτια παπύρων που βρέθηκαν στην Αίγυπτο. Μάλιστα, το 2014 ένας πάπυρος έφερε στο φως ένα σχεδόν πλήρες ποίημα που ήταν άγνωστο ως τότε.", "The scholars of Alexandria later collected her poems in nine books. Of these, however, only one poem has survived complete, the Hymn to Aphrodite; we know the rest from fragments, from quotations by other authors and from pieces of papyrus found in Egypt. Indeed, in 2014 a papyrus brought to light an almost complete poem that had been unknown until then."),
  L("Φιλόλογος", "f", "Τι κάνει την ποίησή της τόσο ξεχωριστή; Σε μια εποχή που η ποίηση υμνούσε κυρίως θεούς και ήρωες, η Σαπφώ μίλησε σε πρώτο πρόσωπο για τον έρωτα, τη ζήλια, τη νοσταλγία. Η περιγραφή της για τα σωματικά συμπτώματα του πάθους, η φωνή που σβήνει, η φωτιά κάτω από το δέρμα, το βουητό στα αυτιά, θεωρείται από τις πιο δυνατές στην παγκόσμια λογοτεχνία.", "What makes her poetry so special? At a time when poetry mainly praised gods and heroes, Sappho spoke in the first person about love, jealousy and longing. Her description of the physical symptoms of passion, the voice that fails, the fire under the skin, the ringing in the ears, is considered one of the most powerful in world literature."),
  L("Φιλόλογος", "f", "Οι αρχαίοι τη θαύμαζαν τόσο, ώστε ένα επίγραμμα που αποδίδεται στον Πλάτωνα την ονομάζει «δέκατη Μούσα». Από την άλλη πλευρά, οι μεταγενέστεροι συχνά παραμόρφωσαν την εικόνα της με θρύλους και κουτσομπολιά. Σήμερα το έργο της διαβάζεται ξανά χωρίς προκαταλήψεις, ως η φωνή μιας ποιήτριας που, μέσα από λίγα σπαράγματα, εξακολουθεί να μας μιλάει με εκπληκτική αμεσότητα.", "The ancients admired her so much that an epigram attributed to Plato calls her the 'tenth Muse'. On the other hand, later generations often distorted her image with legends and gossip. Today her work is read again without prejudice, as the voice of a poet who, through a few scraps, still speaks to us with astonishing immediacy."),
 ],
 "questions": [
  Q("Τι ξέρουμε με βεβαιότητα για τη ζωή της Σαπφώς;", ["Σχεδόν τα πάντα", "Ελάχιστα, όπως ότι ανήκε σε αριστοκρατική οικογένεια και έζησε εξόριστη στη Σικελία", "Ότι γεννήθηκε στην Αθήνα", "Ότι δεν είχε οικογένεια"], 1, "Για τη ζωή της ξέρουμε ελάχιστα με βεβαιότητα"),
  Q("Πόσα ποιήματά της έχουν σωθεί ολόκληρα;", ["Εννέα βιβλία", "Ένα, ο Ύμνος στην Αφροδίτη", "Κανένα", "Περίπου εκατό"], 1, "μόνο ένα ποίημα έχει σωθεί ολόκληρο, ο Ύμνος στην Αφροδίτη"),
  Q("Τι ήταν καινούργιο στην ποίησή της, σύμφωνα με τη φιλόλογο;", ["Ότι έγραφε σε πεζό λόγο", "Ότι μίλησε σε πρώτο πρόσωπο για τον έρωτα και τα συναισθήματα", "Ότι υμνούσε τους ήρωες του Τρωικού πολέμου", "Ότι έγραφε για παιδιά"], 1, "η Σαπφώ μίλησε σε πρώτο πρόσωπο για τον έρωτα, τη ζήλια, τη νοσταλγία"),
  Q("Τι λέει η φιλόλογος για τους μεταγενέστερους;", ["Ότι έσωσαν όλα τα ποιήματά της", "Ότι συχνά παραμόρφωσαν την εικόνα της με θρύλους και κουτσομπολιά", "Ότι την αγνόησαν τελείως", "Ότι την ονόμασαν «δέκατη Μούσα»"], 1, "οι μεταγενέστεροι συχνά παραμόρφωσαν την εικόνα της με θρύλους και κουτσομπολιά"),
 ],
 "gloss": {"Μούσα": "Μούσα — Muse", "εξόριστη": "εξόριστος — exiled", "συγκέντρωσαν": "συγκεντρώνω — to collect, gather", "αποσπάσματα": "απόσπασμα — fragment, excerpt", "παραθέματα": "παράθεμα — quotation", "παπύρων": "πάπυρος — papyrus", "έφερε στο φως": "φέρνω στο φως — to bring to light", "υμνούσε": "υμνώ — to praise, sing of", "νοσταλγία": "νοσταλγία — longing, nostalgia", "βουητό": "βουητό — buzzing, ringing", "επίγραμμα": "επίγραμμα — epigram", "αποδίδεται": "αποδίδομαι — to be attributed", "μεταγενέστεροι": "μεταγενέστερος — later (generation)", "παραμόρφωσαν": "παραμορφώνω — to distort", "σπαράγματα": "σπάραγμα — fragment, scrap", "αμεσότητα": "αμεσότητα — immediacy"},
})

rnd = random.Random(53)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-53.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
