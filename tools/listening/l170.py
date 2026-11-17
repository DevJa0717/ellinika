# Source for library/listening/listening-170.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l170.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l170-ann-tachyploo", "title": "Ανακοίνωση στο ταχύπλοο", "title_en": "An announcement on the fast ferry", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τον καπετάνιο ενός ταχύπλοου λίγο μετά την αναχώρηση.",
 "script": [
  L("Καπετάνιος", "m", "Κυρίες και κύριοι, καλησπέρα σας. Σας μιλάει ο καπετάνιος. Μόλις βγήκαμε από το λιμάνι και σας ενημερώνουμε ότι στο ανοιχτό πέλαγος πνέουν άνεμοι έξι μποφόρ. Θα υπάρξει έντονος κυματισμός για περίπου μία ώρα, μέχρι να μπούμε στο στενό ανάμεσα στα δύο νησιά.", "Ladies and gentlemen, good evening. This is the captain speaking. We have just left the harbour and we inform you that in the open sea winds of force six are blowing. There will be heavy swell for about an hour, until we enter the strait between the two islands."),
  L("Καπετάνιος", "m", "Για την ασφάλειά σας, παρακαλούμε να παραμείνετε στις θέσεις σας και να μην κυκλοφορείτε στους διαδρόμους. Η καφετέρια θα μείνει κλειστή μέχρι να ηρεμήσει η θάλασσα. Όσοι ζαλίζονται εύκολα, καλό είναι να κοιτάζουν μακριά, προς τον ορίζοντα, και όχι το κινητό τους.", "For your safety, please remain in your seats and do not walk about in the aisles. The café will stay closed until the sea calms down. Those who get seasick easily would do well to look into the distance, towards the horizon, and not at their phones."),
  L("Καπετάνιος", "m", "Σακούλες υπάρχουν στην τσέπη του μπροστινού καθίσματος, και το πλήρωμα είναι στη διάθεσή σας για οτιδήποτε χρειαστείτε. Λόγω του καιρού, η άφιξή μας θα καθυστερήσει περίπου είκοσι λεπτά. Σας ευχαριστούμε για την κατανόηση.", "Bags are in the pocket of the seat in front of you, and the crew are at your disposal for anything you need. Because of the weather, our arrival will be delayed by about twenty minutes. Thank you for your understanding."),
 ],
 "questions": [
  Q("Για πόση ώρα περίπου θα κρατήσει ο έντονος κυματισμός;", ["Για δέκα λεπτά", "Για περίπου μία ώρα", "Σε όλο το ταξίδι", "Για τρεις ώρες"], 1, "Θα υπάρξει έντονος κυματισμός για περίπου μία ώρα"),
  Q("Τι συμβουλεύει ο καπετάνιος όσους ζαλίζονται εύκολα;", ["Να πάνε στην καφετέρια", "Να βγουν στο κατάστρωμα", "Να κοιτάζουν μακριά, προς τον ορίζοντα", "Να ξαπλώσουν στους διαδρόμους"], 2, "καλό είναι να κοιτάζουν μακριά, προς τον ορίζοντα"),
  Q("Τι θα γίνει με την άφιξη;", ["Θα καθυστερήσει περίπου είκοσι λεπτά", "Θα γίνει σε άλλο λιμάνι", "Θα γίνει νωρίτερα", "Θα ακυρωθεί"], 0, "η άφιξή μας θα καθυστερήσει περίπου είκοσι λεπτά"),
 ],
 "gloss": {"ταχύπλοου": "ταχύπλοο — fast ferry", "πέλαγος": "πέλαγος — open sea", "πνέουν": "πνέω — to blow", "μποφόρ": "μποφόρ — Beaufort (wind force)", "κυματισμός": "κυματισμός — swell, waves", "στενό": "στενό — strait", "διαδρόμους": "διάδρομος — aisle", "ζαλίζονται": "ζαλίζομαι — to feel dizzy, seasick", "ορίζοντα": "ορίζοντας — horizon", "πλήρωμα": "πλήρωμα — crew", "στη διάθεσή σας": "στη διάθεσή σας — at your disposal", "κατανόηση": "κατανόηση — understanding"},
})

ITEMS.append({
 "id": "l170-int-miniatoures", "title": "Η κατασκευάστρια μινιατούρων", "title_en": "The miniature maker", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που φτιάχνει μινιατούρες από παλιά μαγαζιά και σπίτια.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς φτιάχνετε;", "What exactly do you make?"),
  L("Κατασκευάστρια", "f", "Μικρά αντίγραφα από παλιά μαγαζιά της Αθήνας, σε κλίμακα ένα προς δώδεκα. Ένα παντοπωλείο της δεκαετίας του '60, ένα κουρείο, ένα καφενείο με τα τραπεζάκια του. Μέσα βάζω τα πάντα: ζυγαριές, βάζα με καραμέλες, εφημερίδες με πραγματικούς τίτλους της εποχής. Μια εφημερίδα είναι μικρότερη από ένα γραμματόσημο.", "Small replicas of old Athenian shops, at a scale of one to twelve. A 1960s grocery, a barber's, a coffee house with its little tables. Inside I put everything: scales, jars of sweets, newspapers with real headlines from the period. A newspaper is smaller than a postage stamp."),
  L("Δημοσιογράφος", "m", "Πόσο χρόνο σας παίρνει ένα μαγαζί;", "How long does one shop take you?"),
  L("Κατασκευάστρια", "f", "Από τρεις έως έξι μήνες. Το πιο χρονοβόρο δεν είναι η κατασκευή, αλλά η έρευνα. Ψάχνω φωτογραφίες, μιλάω με ηλικιωμένους που θυμούνται τα μαγαζιά. Μια κυρία μού περιέγραψε το χρώμα από τα πλακάκια του φούρνου της γειτονιάς της με τέτοια ακρίβεια, που όταν της έδειξα τη μινιατούρα έβαλε τα κλάματα.", "From three to six months. The most time-consuming part isn't the building but the research. I look for photographs, I talk to elderly people who remember the shops. One lady described to me the colour of the tiles of her neighbourhood bakery so precisely that when I showed her the miniature she burst into tears."),
  L("Δημοσιογράφος", "m", "Τις πουλάτε;", "Do you sell them?"),
  L("Κατασκευάστρια", "f", "Σπάνια. Τις περισσότερες τις δανείζω σε εκθέσεις και σε σχολεία. Τα παιδιά σκύβουν πάνω από τις βιτρίνες και ρωτάνε τι είναι το ένα και τι το άλλο. Έτσι οι παππούδες τους βρίσκουν ευκαιρία να τους διηγηθούν ιστορίες.", "Rarely. I lend most of them to exhibitions and schools. Children bend over the display cases and ask what this and that is. That way their grandparents get a chance to tell them stories."),
 ],
 "questions": [
  Q("Τι βάζει μέσα στις μινιατούρες της;", ["Μόνο έπιπλα", "Τα πάντα, ακόμη και εφημερίδες με πραγματικούς τίτλους της εποχής", "Μικρές φωτογραφίες της οικογένειάς της", "Ηλεκτρικά φωτάκια"], 1, "εφημερίδες με πραγματικούς τίτλους της εποχής"),
  Q("Ποιο είναι, κατά την ίδια, το πιο χρονοβόρο μέρος της δουλειάς;", ["Η βαφή", "Η κατασκευή των επίπλων", "Η έρευνα", "Η αγορά των υλικών"], 2, "Το πιο χρονοβόρο δεν είναι η κατασκευή, αλλά η έρευνα"),
  Q("Τι κάνει συνήθως με τις μινιατούρες της;", ["Τις δανείζει σε εκθέσεις και σε σχολεία", "Τις πουλάει σε συλλέκτες", "Τις κρατάει στο σπίτι της", "Τις χαρίζει στους ηλικιωμένους"], 0, "Τις περισσότερες τις δανείζω σε εκθέσεις και σε σχολεία"),
 ],
 "gloss": {"μινιατούρες": "μινιατούρα — miniature", "αντίγραφα": "αντίγραφο — replica, copy", "κλίμακα": "κλίμακα — scale", "παντοπωλείο": "παντοπωλείο — grocery", "ζυγαριές": "ζυγαριά — scales", "γραμματόσημο": "γραμματόσημο — postage stamp", "χρονοβόρο": "χρονοβόρος — time-consuming", "πλακάκια": "πλακάκι — tile", "ακρίβεια": "ακρίβεια — precision", "βιτρίνες": "βιτρίνα — display case", "διηγηθούν": "διηγούμαι — to narrate, tell"},
})

ITEMS.append({
 "id": "l170-int-taxidiotikoi-odigoi", "title": "Ο συγγραφέας ταξιδιωτικών οδηγών", "title_en": "The travel guidebook writer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν άντρα που γράφει ταξιδιωτικούς οδηγούς για τα ελληνικά νησιά.",
 "script": [
  L("Δημοσιογράφος", "f", "Πολλοί θα ζήλευαν τη δουλειά σας. Είναι τόσο ωραία όσο ακούγεται;", "Many people would envy your job. Is it as nice as it sounds?"),
  L("Συγγραφέας", "m", "Ακούγεται σαν διακοπές, αλλά δεν είναι. Σε ένα νησί μένω συνήθως τέσσερις μέρες και πρέπει να δω τα πάντα: δεκαπέντε παραλίες, είκοσι ταβέρνες, όλα τα ξενοδοχεία, τα δρομολόγια των λεωφορείων. Κολυμπάω σπάνια. Και τρώω τρεις φορές το μεσημέρι, σε τρεις διαφορετικές ταβέρνες, τρώγοντας λίγες μπουκιές σε καθεμία.", "It sounds like a holiday, but it isn't. On an island I usually stay four days and have to see everything: fifteen beaches, twenty tavernas, all the hotels, the bus timetables. I rarely swim. And I have lunch three times, in three different tavernas, eating a few bites in each."),
  L("Δημοσιογράφος", "f", "Οι ιδιοκτήτες ξέρουν ποιος είστε;", "Do the owners know who you are?"),
  L("Συγγραφέας", "m", "Ποτέ. Πληρώνω πάντα κανονικά και δεν δέχομαι δώρα. Αν μάθουν ποιος είμαι, θα μου φερθούν διαφορετικά και η κριτική μου δεν θα είναι αξιόπιστη. Μια φορά ένας ταβερνιάρης με αναγνώρισε από μια φωτογραφία και μου έφερε δωρεάν γλυκό. Το έφαγα, το πλήρωσα και δεν έγραψα τίποτα γι' αυτό.", "Never. I always pay normally and I don't accept gifts. If they find out who I am, they'll treat me differently and my review won't be reliable. Once a taverna owner recognised me from a photo and brought me a free dessert. I ate it, paid for it and wrote nothing about it."),
  L("Δημοσιογράφος", "f", "Έχει νόημα ένας τυπωμένος οδηγός σήμερα, με το διαδίκτυο;", "Does a printed guide make sense today, with the internet?"),
  L("Συγγραφέας", "m", "Στο διαδίκτυο βρίσκεις χίλιες γνώμες. Ο οδηγός σού δίνει μία, αλλά από κάποιον που τα είδε όλα και μπορεί να συγκρίνει. Και, να είμαστε ειλικρινείς, σε ένα χωριό χωρίς σήμα το βιβλίο δεν ξεμένει ποτέ από μπαταρία.", "On the internet you find a thousand opinions. The guide gives you one, but from someone who has seen everything and can compare. And, let's be honest, in a village without signal the book never runs out of battery."),
 ],
 "questions": [
  Q("Γιατί λέει ότι η δουλειά του δεν είναι διακοπές;", ["Γιατί ταξιδεύει μόνο τον χειμώνα", "Γιατί σε λίγες μέρες πρέπει να δει τα πάντα σε ένα νησί", "Γιατί δεν του αρέσουν τα νησιά", "Γιατί πληρώνεται πολύ λίγο"], 1, "Σε ένα νησί μένω συνήθως τέσσερις μέρες και πρέπει να δω τα πάντα"),
  Q("Γιατί δεν θέλει να ξέρουν οι ιδιοκτήτες ποιος είναι;", ["Γιατί είναι ντροπαλός", "Για να μην πληρώνει", "Για να μείνει αξιόπιστη η κριτική του", "Γιατί δεν του αρέσουν οι φωτογραφίες"], 2, "η κριτική μου δεν θα είναι αξιόπιστη"),
  Q("Ποιο πλεονέκτημα του βιβλίου αναφέρει στο τέλος;", ["Ότι δεν χρειάζεται μπαταρία σε ένα χωριό χωρίς σήμα", "Ότι είναι φθηνότερο", "Ότι έχει περισσότερες φωτογραφίες", "Ότι είναι πιο ελαφρύ"], 0, "σε ένα χωριό χωρίς σήμα το βιβλίο δεν ξεμένει ποτέ από μπαταρία"),
 ],
 "gloss": {"ταξιδιωτικούς οδηγούς": "ταξιδιωτικός οδηγός — travel guidebook", "ζήλευαν": "ζηλεύω — to envy", "δρομολόγια": "δρομολόγιο — timetable, route", "μπουκιές": "μπουκιά — mouthful, bite", "φερθούν": "φέρομαι — to behave, treat", "αξιόπιστη": "αξιόπιστος — reliable", "ταβερνιάρης": "ταβερνιάρης — taverna owner", "τυπωμένος": "τυπωμένος — printed", "συγκρίνει": "συγκρίνω — to compare", "ειλικρινείς": "ειλικρινής — honest", "σήμα": "σήμα — (phone) signal", "ξεμένει": "ξεμένω — to run out"},
})

ITEMS.append({
 "id": "l170-dia-kouketa-i-kathisma", "title": "Κουκέτα ή κάθισμα;", "title_en": "Cabin or seat?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά τι εισιτήρια θα κλείσει για ένα νυχτερινό πλοίο προς την Κρήτη.",
 "script": [
  L("Νίκος", "m", "Λοιπόν, για το πλοίο της Παρασκευής: παίρνουμε απλά καθίσματα ή καμπίνα;", "So, for Friday's ship: do we get plain seats or a cabin?"),
  L("Ελένη", "f", "Το πλοίο φεύγει στις εννιά το βράδυ και φτάνει στις έξι το πρωί. Αν κάτσουμε σε πολυθρόνες, θα φτάσουμε σαν ζόμπι και θα χάσουμε όλη την πρώτη μέρα.", "The ship leaves at nine in the evening and arrives at six in the morning. If we sit in armchairs, we'll arrive like zombies and lose the whole first day."),
  L("Νίκος", "m", "Η δίκλινη καμπίνα όμως κοστίζει σχεδόν όσο ένα δωμάτιο ξενοδοχείου. Υπάρχει και η τετράκλινη με κουκέτες, που τη μοιράζεσαι με αγνώστους. Βγαίνει πολύ φθηνότερα.", "But the two-berth cabin costs almost as much as a hotel room. There's also the four-berth with bunks, which you share with strangers. It works out much cheaper."),
  L("Ελένη", "f", "Με αγνώστους; Κι αν ροχαλίζει κάποιος; Τότε καλύτερα πολυθρόνα.", "With strangers? And what if someone snores? Then I'd rather have an armchair."),
  L("Νίκος", "m", "Για στάσου. Βλέπω εδώ ότι αν κλείσουμε και τις δύο διαδρομές, πήγαινε και έλα, έχουμε έκπτωση είκοσι τοις εκατό. Με την έκπτωση, η δίκλινη κοστίζει όσο η τετράκλινη χωρίς έκπτωση.", "Hang on. I see here that if we book both legs, there and back, we get a twenty per cent discount. With the discount, the two-berth costs as much as the four-berth without it."),
  L("Ελένη", "f", "Τέλεια, τότε δίκλινη με επιστροφή. Και κλείσ' την τώρα, πριν μας την πάρει κάποιος άλλος.", "Perfect, then a two-berth with return. And book it now, before someone else takes it."),
 ],
 "questions": [
  Q("Γιατί η Ελένη δεν θέλει απλά καθίσματα;", ["Γιατί είναι ακριβά", "Γιατί θα φτάσουν κουρασμένοι και θα χάσουν την πρώτη μέρα", "Γιατί δεν υπάρχουν ελεύθερα", "Γιατί ζαλίζεται στο πλοίο"], 1, "θα φτάσουμε σαν ζόμπι και θα χάσουμε όλη την πρώτη μέρα"),
  Q("Γιατί δεν θέλει την τετράκλινη καμπίνα;", ["Γιατί είναι πολύ μικρή", "Γιατί δεν έχει παράθυρο", "Γιατί θα τη μοιράζονται με αγνώστους που μπορεί να ροχαλίζουν", "Γιατί είναι στο κάτω κατάστρωμα"], 2, "Κι αν ροχαλίζει κάποιος;"),
  Q("Τι κάνει τελικά τη δίκλινη καμπίνα συμφέρουσα;", ["Η έκπτωση αν κλείσουν και την επιστροφή", "Μια προσφορά για φοιτητές", "Ότι ταξιδεύουν Παρασκευή", "Ότι έχουν κάρτα μέλους"], 0, "αν κλείσουμε και τις δύο διαδρομές, πήγαινε και έλα, έχουμε έκπτωση"),
 ],
 "gloss": {"κουκέτες": "κουκέτα — bunk, berth", "καμπίνα": "καμπίνα — cabin", "πολυθρόνες": "πολυθρόνα — armchair (seat on a ship)", "δίκλινη": "δίκλινος — two-berth", "τετράκλινη": "τετράκλινος — four-berth", "αγνώστους": "άγνωστος — stranger", "ροχαλίζει": "ροχαλίζω — to snore", "πήγαινε και έλα": "πήγαινε και έλα — there and back, return", "έκπτωση": "έκπτωση — discount"},
})

ITEMS.append({
 "id": "l170-dia-pisteveis-sta-zodia", "title": "Πιστεύεις στα ζώδια;", "title_en": "Do you believe in horoscopes?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο συναδέλφους να συζητούν για τα ζώδια στο διάλειμμα του καφέ.",
 "script": [
  L("Ρένα", "f", "Άκου τι λέει το ζώδιό σου σήμερα: «Μια απρόσμενη συνάντηση θα αλλάξει τα σχέδιά σας.»", "Listen to what your horoscope says today: 'An unexpected meeting will change your plans.'"),
  L("Τάσος", "m", "Ρένα, το ίδιο λέει σε όλους, κάθε μέρα. Κάποιον θα συναντήσεις, κάποιο σχέδιο θα αλλάξει. Αυτό ισχύει για οποιονδήποτε.", "Rena, it says the same thing to everyone, every day. You'll meet someone, some plan will change. That applies to anyone."),
  L("Ρένα", "f", "Κι όμως, εγώ είμαι τυπικός Ταύρος: πεισματάρα, μου αρέσει το καλό φαγητό και δεν αλλάζω εύκολα γνώμη.", "And yet I'm a typical Taurus: stubborn, I like good food and I don't change my mind easily."),
  L("Τάσος", "m", "Σε ποιον δεν αρέσει το καλό φαγητό; Έχω διαβάσει ότι σε πειράματα έδωσαν σε ανθρώπους την ίδια περιγραφή χαρακτήρα και σχεδόν όλοι είπαν ότι τους ταιριάζει απόλυτα. Βλέπουμε αυτό που θέλουμε να δούμε.", "Who doesn't like good food? I've read that in experiments they gave people the same character description and almost everyone said it fitted them perfectly. We see what we want to see."),
  L("Ρένα", "f", "Εντάξει, ίσως δεν είναι επιστήμη. Αλλά μου αρέσει να τα διαβάζω το πρωί, σαν παιχνίδι. Δεν αποφασίζω τίποτα με βάση τα ζώδια.", "OK, maybe it isn't science. But I like reading them in the morning, as a game. I don't decide anything based on horoscopes."),
  L("Τάσος", "m", "Ε, σαν παιχνίδι το δέχομαι. Τι λέει, λοιπόν, για τον Λέοντα; Μήπως έρχεται καμιά αύξηση;", "Well, as a game I'll accept it. So what does it say for Leo? Is a pay rise coming, perhaps?"),
 ],
 "questions": [
  Q("Ποιο είναι το επιχείρημα του Τάσου για τις προβλέψεις;", ["Ότι είναι πάντα λάθος", "Ότι λένε πράγματα που ισχύουν για οποιονδήποτε", "Ότι τις γράφουν υπολογιστές", "Ότι αλλάζουν κάθε ώρα"], 1, "Αυτό ισχύει για οποιονδήποτε"),
  Q("Τι έδειξαν, σύμφωνα με τον Τάσο, τα πειράματα;", ["Ότι οι Ταύροι είναι πεισματάρηδες", "Ότι τα ζώδια επηρεάζουν τη διάθεση", "Ότι σχεδόν όλοι βρίσκουν ότι η ίδια περιγραφή χαρακτήρα τούς ταιριάζει", "Ότι οι γυναίκες πιστεύουν περισσότερο στα ζώδια"], 2, "σχεδόν όλοι είπαν ότι τους ταιριάζει απόλυτα"),
  Q("Πώς βλέπει τελικά η Ρένα τα ζώδια;", ["Σαν ένα παιχνίδι για το πρωί", "Σαν επιστήμη", "Σαν οδηγό για τις αποφάσεις της", "Σαν χάσιμο χρόνου"], 0, "μου αρέσει να τα διαβάζω το πρωί, σαν παιχνίδι"),
 ],
 "gloss": {"ζώδια": "ζώδιο — star sign; horoscope", "απρόσμενη": "απρόσμενος — unexpected", "οποιονδήποτε": "οποιοσδήποτε — anyone", "Ταύρος": "Ταύρος — Taurus", "πεισματάρα": "πεισματάρης — stubborn", "πειράματα": "πείραμα — experiment", "περιγραφή": "περιγραφή — description", "Λέοντα": "Λέων — Leo", "αύξηση": "αύξηση — pay rise"},
})

ITEMS.append({
 "id": "l170-mon-bonsai-tou-patera", "title": "Το μπονσάι του πατέρα μου", "title_en": "My father's bonsai", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλάει σε ένα ραδιοφωνικό πρόγραμμα για ένα μπονσάι που του άφησε ο πατέρας του.",
 "script": [
  L("Άντρας", "m", "Ο πατέρας μου ήταν ναυτικός. Από ένα ταξίδι στην Ιαπωνία έφερε ένα μικρό πεύκο σε μια ρηχή γλάστρα. Όλοι γελούσαν: ένα δέντρο που χωράει στο τραπέζι της κουζίνας! Εκείνος όμως το φρόντιζε κάθε μέρα, το κλάδευε με ένα ψαλίδι σαν του νυχιού και μιλούσε μαζί του.", "My father was a sailor. From a trip to Japan he brought back a small pine in a shallow pot. Everyone laughed: a tree that fits on the kitchen table! But he looked after it every day, pruned it with scissors like nail scissors and talked to it."),
  L("Άντρας", "m", "Όταν πέθανε, το μπονσάι ήρθε σε μένα. Τον πρώτο χρόνο κόντεψα να το σκοτώσω. Το πότιζα πάρα πολύ, νομίζοντας ότι το περιποιούμαι. Ένας φίλος μου εξήγησε ότι το μπονσάι δεν είναι φυτό εσωτερικού χώρου, όπως πιστεύουν πολλοί· τα περισσότερα θέλουν ήλιο, αέρα και τον χειμώνα το κρύο τους. Το έβγαλα στο μπαλκόνι και άρχισε να πετάει καινούργιες βελόνες.", "When he died, the bonsai came to me. The first year I nearly killed it. I watered it far too much, thinking I was taking care of it. A friend explained that a bonsai is not an indoor plant, as many believe; most need sun, air and, in winter, their share of cold. I put it out on the balcony and it started putting out new needles."),
  L("Άντρας", "m", "Έχουν περάσει δεκαπέντε χρόνια. Το δέντρο είναι πια πάνω από πενήντα χρονών και έχει σχεδόν το ίδιο ύψος με τότε. Κάθε πρωί πίνω τον καφέ μου δίπλα του. Δεν του μιλάω, όπως ο πατέρας μου. Αλλά καμιά φορά πιάνω τον εαυτό μου να του λέει «καλημέρα».", "Fifteen years have passed. The tree is now more than fifty years old and is almost the same height as back then. Every morning I drink my coffee next to it. I don't talk to it, like my father did. But sometimes I catch myself saying 'good morning' to it."),
 ],
 "questions": [
  Q("Από πού είχε φέρει ο πατέρας του το μπονσάι;", ["Από την Κίνα", "Από ένα ταξίδι στην Ιαπωνία", "Από ένα φυτώριο της Αθήνας", "Από έναν φίλο του"], 1, "Από ένα ταξίδι στην Ιαπωνία έφερε ένα μικρό πεύκο"),
  Q("Ποιο λάθος έκανε τον πρώτο χρόνο;", ["Το ξέχασε στον ήλιο", "Το έκοψε πολύ", "Το πότιζε πάρα πολύ", "Το άλλαξε γλάστρα"], 2, "Το πότιζα πάρα πολύ"),
  Q("Τι του εξήγησε ο φίλος του;", ["Ότι τα περισσότερα μπονσάι θέλουν ήλιο, αέρα και κρύο τον χειμώνα", "Ότι το δέντρο ήταν άρρωστο", "Ότι έπρεπε να του μιλάει", "Ότι έπρεπε να το βάλει σε μεγαλύτερη γλάστρα"], 0, "τα περισσότερα θέλουν ήλιο, αέρα και τον χειμώνα το κρύο τους"),
 ],
 "gloss": {"μπονσάι": "μπονσάι — bonsai", "ναυτικός": "ναυτικός — sailor", "πεύκο": "πεύκο — pine", "ρηχή": "ρηχός — shallow", "γλάστρα": "γλάστρα — flowerpot", "κλάδευε": "κλαδεύω — to prune", "ψαλίδι": "ψαλίδι — scissors", "κόντεψα": "κοντεύω — to nearly (do sth)", "πότιζα": "ποτίζω — to water", "εσωτερικού χώρου": "εσωτερικού χώρου — indoor", "βελόνες": "βελόνα — (pine) needle"},
})

ITEMS.append({
 "id": "l170-vm-to-spiti-tis-theias", "title": "Μήνυμα από τον δικηγόρο για το σπίτι της θείας", "title_en": "A message from the lawyer about the aunt's house", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από έναν δικηγόρο σχετικά με τη διαθήκη μιας θείας σας.",
 "script": [
  L("Δικηγόρος", "m", "Καλημέρα σας, ονομάζομαι Παπαγεωργίου και είμαι δικηγόρος στην Τρίπολη. Σας τηλεφωνώ σχετικά με τη διαθήκη της θείας σας, της κυρίας Αγγελικής, που απεβίωσε τον περασμένο μήνα. Πρώτα απ' όλα, τα θερμά μου συλλυπητήρια.", "Good morning, my name is Papageorgiou and I'm a lawyer in Tripoli. I'm calling about the will of your aunt, Mrs Angeliki, who passed away last month. First of all, my sincere condolences."),
  L("Δικηγόρος", "m", "Σύμφωνα με τη διαθήκη, σας αφήνει το πατρικό της σπίτι στο χωριό, μαζί με τον κήπο. Υπάρχει μόνο ένας όρος: η θεία σας ζητά να μην πουληθεί το σπίτι για τουλάχιστον πέντε χρόνια.", "According to the will, she leaves you her family home in the village, together with the garden. There is only one condition: your aunt asks that the house not be sold for at least five years."),
  L("Δικηγόρος", "m", "Για να προχωρήσουμε, θα πρέπει να περάσετε από το γραφείο μου να υπογράψετε την αποδοχή της κληρονομιάς. Έχετε προθεσμία τέσσερις μήνες. Αν δεν μπορείτε να έρθετε στην Τρίπολη, μπορείτε να δώσετε πληρεξούσιο σε κάποιον που εμπιστεύεστε. Θα σας στείλω τα στοιχεία μου με μήνυμα.", "To proceed, you will need to come by my office to sign the acceptance of the inheritance. You have a deadline of four months. If you can't come to Tripoli, you can give power of attorney to someone you trust. I'll send you my details by message."),
 ],
 "questions": [
  Q("Τι αφήνει η θεία στον ακροατή;", ["Ένα διαμέρισμα στην Τρίπολη", "Το πατρικό της σπίτι στο χωριό, μαζί με τον κήπο", "Ένα χρηματικό ποσό", "Ένα χωράφι με ελιές"], 1, "σας αφήνει το πατρικό της σπίτι στο χωριό, μαζί με τον κήπο"),
  Q("Ποιος είναι ο όρος της διαθήκης;", ["Να μείνει μόνιμα στο χωριό", "Να φροντίζει τη γάτα της", "Να μην πουληθεί το σπίτι για τουλάχιστον πέντε χρόνια", "Να το ανακαινίσει μέσα σε έναν χρόνο"], 2, "να μην πουληθεί το σπίτι για τουλάχιστον πέντε χρόνια"),
  Q("Τι μπορεί να κάνει αν δεν μπορεί να πάει στην Τρίπολη;", ["Να δώσει πληρεξούσιο σε κάποιον που εμπιστεύεται", "Να υπογράψει ηλεκτρονικά", "Να στείλει ένα γράμμα", "Να ζητήσει παράταση"], 0, "μπορείτε να δώσετε πληρεξούσιο σε κάποιον που εμπιστεύεστε"),
 ],
 "gloss": {"διαθήκη": "διαθήκη — will", "απεβίωσε": "αποβιώνω — to pass away", "συλλυπητήρια": "συλλυπητήρια — condolences", "πατρικό": "πατρικό (σπίτι) — family home", "όρος": "όρος — condition", "πουληθεί": "πουλιέμαι — to be sold", "αποδοχή": "αποδοχή — acceptance", "κληρονομιάς": "κληρονομιά — inheritance", "προθεσμία": "προθεσμία — deadline", "πληρεξούσιο": "πληρεξούσιο — power of attorney", "εμπιστεύεστε": "εμπιστεύομαι — to trust"},
})

ITEMS.append({
 "id": "l170-vm-metafora-pianou", "title": "Μήνυμα για τη μεταφορά του πιάνου", "title_en": "A message about moving the piano", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από μια εταιρεία που μεταφέρει πιάνα.",
 "script": [
  L("Υπάλληλος", "f", "Καλησπέρα σας, από την εταιρεία μεταφορών σας παίρνουμε, για το πιάνο που θέλετε να μεταφέρουμε το Σάββατο. Είδαμε τις φωτογραφίες που μας στείλατε. Επειδή το καινούργιο σας σπίτι είναι στον τέταρτο όροφο χωρίς ασανσέρ, το πιάνο δεν θα ανέβει από τη σκάλα.", "Good evening, we're calling from the removal company about the piano you want us to move on Saturday. We've seen the photos you sent us. Because your new home is on the fourth floor without a lift, the piano won't go up the stairs."),
  L("Υπάλληλος", "f", "Θα χρειαστεί ανυψωτικό μηχάνημα, που θα το ανεβάσει από το μπαλκόνι. Αυτό σημαίνει επιπλέον χρέωση εκατόν πενήντα ευρώ. Χρειάζεται επίσης άδεια από τον δήμο για να σταθμεύσει το φορτηγό στο πεζοδρόμιο. Αυτήν την αναλαμβάνουμε εμείς.", "We'll need a lifting machine to raise it through the balcony. That means an extra charge of one hundred and fifty euros. A permit from the municipality is also needed for the lorry to park on the pavement. We'll take care of that."),
  L("Υπάλληλος", "f", "Σας παρακαλώ να μετρήσετε το άνοιγμα της μπαλκονόπορτας και να μας στείλετε τις διαστάσεις μέχρι αύριο το μεσημέρι. Αν είναι μικρότερο από ενενήντα εκατοστά, θα χρειαστεί να βγάλουμε την πόρτα. Και μην ξεχάσετε να κλείσετε ραντεβού με τον κουρδιστή μία εβδομάδα μετά τη μεταφορά, όχι νωρίτερα.", "Please measure the opening of the balcony door and send us the dimensions by tomorrow at noon. If it's less than ninety centimetres, we'll need to take the door off. And don't forget to book the tuner for a week after the move, not earlier."),
 ],
 "questions": [
  Q("Πώς θα ανέβει το πιάνο στο καινούργιο σπίτι;", ["Από τη σκάλα", "Με ένα ανυψωτικό μηχάνημα από το μπαλκόνι", "Με το ασανσέρ", "Από το παράθυρο της κουζίνας με σκοινιά"], 1, "Θα χρειαστεί ανυψωτικό μηχάνημα, που θα το ανεβάσει από το μπαλκόνι"),
  Q("Τι πρέπει να κάνει ο ακροατής μέχρι αύριο το μεσημέρι;", ["Να πληρώσει προκαταβολή", "Να βγάλει την πόρτα", "Να μετρήσει το άνοιγμα της μπαλκονόπορτας και να στείλει τις διαστάσεις", "Να βγάλει άδεια από τον δήμο"], 2, "να μετρήσετε το άνοιγμα της μπαλκονόπορτας"),
  Q("Πότε πρέπει να έρθει ο κουρδιστής;", ["Μία εβδομάδα μετά τη μεταφορά", "Την ίδια μέρα", "Πριν από τη μεταφορά", "Έναν μήνα μετά"], 0, "μία εβδομάδα μετά τη μεταφορά, όχι νωρίτερα"),
 ],
 "gloss": {"μεταφέρει": "μεταφέρω — to move, transport", "πιάνα": "πιάνο — piano", "εταιρεία μεταφορών": "εταιρεία μεταφορών — removal company", "όροφο": "όροφος — floor", "ασανσέρ": "ασανσέρ — lift", "ανυψωτικό μηχάνημα": "ανυψωτικό μηχάνημα — lifting machine", "χρέωση": "χρέωση — charge", "σταθμεύσει": "σταθμεύω — to park", "άνοιγμα": "άνοιγμα — opening", "μπαλκονόπορτας": "μπαλκονόπορτα — balcony door", "διαστάσεις": "διάσταση — dimension", "κουρδιστή": "κουρδιστής — (piano) tuner"},
})

ITEMS.append({
 "id": "l170-c1-gkrizes-tryches", "title": "Γιατί γκριζάρουν τα μαλλιά", "title_en": "Why hair turns grey", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια δερματολόγο σε μια εκπομπή για την υγεία.",
 "script": [
  L("Δημοσιογράφος", "m", "Από πού παίρνουν τα μαλλιά το χρώμα τους;", "Where does hair get its colour from?"),
  L("Δερματολόγος", "f", "Από μια χρωστική, τη μελανίνη, που την παράγουν ειδικά κύτταρα στη ρίζα της τρίχας, τα μελανοκύτταρα. Τα κύτταρα αυτά ανανεώνονται από ένα απόθεμα βλαστοκυττάρων. Με τα χρόνια, το απόθεμα εξαντλείται ή, σύμφωνα με νεότερες έρευνες, τα βλαστοκύτταρα «κολλάνε» και δεν ωριμάζουν όπως πριν. Η τρίχα που φυτρώνει τότε είναι χωρίς χρωστική, δηλαδή λευκή. Στην πραγματικότητα, γκρίζες τρίχες δεν υπάρχουν: το γκρίζο είναι η εντύπωση που δίνει η ανάμειξη λευκών και χρωματισμένων τριχών.", "From a pigment, melanin, produced by special cells at the root of the hair, the melanocytes. These cells are renewed from a reserve of stem cells. Over the years the reserve runs out or, according to more recent research, the stem cells get 'stuck' and don't mature as before. The hair that then grows has no pigment, that is, it's white. In fact, grey hairs don't exist: grey is the impression given by a mixture of white and coloured hairs."),
  L("Δημοσιογράφος", "m", "Και το άγχος; Λένε ότι κάποιος άσπρισε σε μια νύχτα.", "And stress? They say someone went white overnight."),
  L("Δερματολόγος", "f", "Η τρίχα που έχει ήδη φυτρώσει είναι νεκρός ιστός· δεν μπορεί να αλλάξει χρώμα από τη μια μέρα στην άλλη. Αυτές οι ιστορίες είναι μάλλον υπερβολές, ή εξηγούνται από μια πάθηση που ρίχνει απότομα τις χρωματισμένες τρίχες και αφήνει τις λευκές. Πειράματα σε ποντίκια όμως έδειξαν ότι το έντονο στρες μπορεί πράγματι να καταστρέψει τα βλαστοκύτταρα του χρώματος. Πόσο ισχύει αυτό στους ανθρώπους, ερευνάται ακόμη.", "Hair that has already grown is dead tissue; it can't change colour from one day to the next. These stories are probably exaggerations, or are explained by a condition that suddenly sheds the coloured hairs and leaves the white ones. Experiments on mice, however, showed that intense stress can indeed destroy the colour stem cells. How far this holds in humans is still being researched."),
  L("Δημοσιογράφος", "m", "Τι καθορίζει πότε θα γκριζάρουμε;", "What determines when we'll go grey?"),
  L("Δερματολόγος", "f", "Κυρίως τα γονίδια. Αν οι γονείς σας γκρίζαραν νωρίς, είναι πιθανό να συμβεί και σε εσάς. Το κάπνισμα και ορισμένες ελλείψεις βιταμινών φαίνεται να το επιταχύνουν, αλλά η κληρονομικότητα παραμένει ο σημαντικότερος παράγοντας.", "Mainly genes. If your parents went grey early, it's likely to happen to you too. Smoking and certain vitamin deficiencies seem to speed it up, but heredity remains the most important factor."),
 ],
 "questions": [
  Q("Τι λέει η δερματολόγος για τις «γκρίζες» τρίχες;", ["Ότι έχουν λιγότερη μελανίνη από τις άλλες", "Ότι στην πραγματικότητα το γκρίζο είναι ανάμειξη λευκών και χρωματισμένων τριχών", "Ότι οφείλονται στον ήλιο", "Ότι γίνονται λευκές μετά από χρόνια"], 1, "το γκρίζο είναι η εντύπωση που δίνει η ανάμειξη λευκών και χρωματισμένων τριχών"),
  Q("Γιατί είναι μάλλον υπερβολή ότι κάποιος άσπρισε σε μια νύχτα;", ["Γιατί το άγχος δεν επηρεάζει τα μαλλιά", "Γιατί οι τρίχες μεγαλώνουν πολύ αργά", "Γιατί η τρίχα που έχει ήδη φυτρώσει είναι νεκρός ιστός και δεν αλλάζει χρώμα", "Γιατί η μελανίνη καταστρέφεται μόνο από τον ήλιο"], 2, "Η τρίχα που έχει ήδη φυτρώσει είναι νεκρός ιστός"),
  Q("Ποιος είναι, κατά τη δερματολόγο, ο σημαντικότερος παράγοντας;", ["Η κληρονομικότητα", "Το κάπνισμα", "Το στρες", "Οι ελλείψεις βιταμινών"], 0, "η κληρονομικότητα παραμένει ο σημαντικότερος παράγοντας"),
 ],
 "gloss": {"δερματολόγο": "δερματολόγος — dermatologist", "χρωστική": "χρωστική — pigment", "μελανίνη": "μελανίνη — melanin", "τρίχας": "τρίχα — (a single) hair", "μελανοκύτταρα": "μελανοκύτταρο — melanocyte", "απόθεμα": "απόθεμα — reserve, stock", "βλαστοκυττάρων": "βλαστοκύτταρο — stem cell", "εξαντλείται": "εξαντλούμαι — to be exhausted, run out", "ωριμάζουν": "ωριμάζω — to mature", "ανάμειξη": "ανάμειξη — mixture", "άσπρισε": "ασπρίζω — to go white", "ιστός": "ιστός — tissue", "πάθηση": "πάθηση — condition, disorder", "γονίδια": "γονίδιο — gene", "ελλείψεις": "έλλειψη — deficiency", "επιταχύνουν": "επιταχύνω — to speed up", "κληρονομικότητα": "κληρονομικότητα — heredity"},
})

ITEMS.append({
 "id": "l170-c1-ichos-ti-nychta", "title": "Γιατί ο ήχος ακούγεται πιο μακριά τη νύχτα", "title_en": "Why sound carries further at night", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν φυσικό της ατμόσφαιρας να εξηγεί σε ένα ψηφιακό ραδιοφωνικό πρόγραμμα γιατί τη νύχτα ακούμε ήχους από πολύ μακριά.",
 "script": [
  L("Φυσικός", "m", "Πολλοί έχετε παρατηρήσει ότι τη νύχτα ακούτε το τρένο ή τις καμπάνες ενός χωριού που τη μέρα δεν φτάνουν ως εσάς. Ένα μέρος της εξήγησης είναι προφανές: τη νύχτα υπάρχει λιγότερος θόρυβος γύρω μας. Αλλά αυτό δεν είναι όλο. Το σημαντικότερο το κάνει η θερμοκρασία του αέρα.", "Many of you have noticed that at night you hear the train or a village's church bells which during the day don't reach you. Part of the explanation is obvious: at night there is less noise around us. But that's not all. The most important part is played by the temperature of the air."),
  L("Φυσικός", "m", "Ο ήχος ταξιδεύει πιο γρήγορα στον ζεστό αέρα παρά στον κρύο. Τη μέρα το έδαφος ζεσταίνει τον αέρα από κάτω, οπότε κοντά στη γη ο αέρας είναι πιο ζεστός και ψηλότερα πιο κρύος. Τα ηχητικά κύματα λυγίζουν προς τον πιο κρύο αέρα, δηλαδή προς τα πάνω, και χάνονται στον ουρανό. Τη νύχτα, ιδίως όταν είναι αίθριος ο καιρός, το έδαφος ψύχεται γρήγορα και δημιουργείται το αντίθετο: ένα στρώμα κρύου αέρα κάτω από ένα στρώμα θερμότερου. Αυτό το φαινόμενο λέγεται θερμοκρασιακή αναστροφή.", "Sound travels faster in warm air than in cold. During the day the ground warms the air from below, so near the earth the air is warmer and higher up colder. The sound waves bend towards the colder air, that is, upwards, and are lost in the sky. At night, especially when the weather is clear, the ground cools quickly and the opposite forms: a layer of cold air beneath a layer of warmer air. This phenomenon is called temperature inversion."),
  L("Φυσικός", "m", "Σε αυτή την περίπτωση τα κύματα που ξεκινούν προς τα πάνω λυγίζουν και γυρίζουν πίσω προς το έδαφος, σαν να τα αντανακλά ένα αόρατο ταβάνι. Έτσι ο ήχος «πατάει» πάνω στη γη και φτάνει πολύ πιο μακριά. Ρόλο παίζει και ο άνεμος: όταν φυσάει από την πηγή του ήχου προς εσάς, ο ήχος έρχεται πιο καθαρός, ενώ αντίθετα μπορεί να μην τον ακούσετε καθόλου.", "In this case the waves that set off upwards bend and turn back towards the ground, as if reflected by an invisible ceiling. So the sound 'keeps to' the earth and travels much further. The wind also plays a role: when it blows from the source of the sound towards you, the sound comes more clearly, whereas against it you may not hear it at all."),
 ],
 "questions": [
  Q("Πού ταξιδεύει πιο γρήγορα ο ήχος;", ["Στον κρύο αέρα", "Στον ζεστό αέρα", "Στον υγρό αέρα", "Το ίδιο παντού"], 1, "Ο ήχος ταξιδεύει πιο γρήγορα στον ζεστό αέρα παρά στον κρύο"),
  Q("Τι συμβαίνει με τον ήχο τη μέρα;", ["Ανακλάται από τα σύννεφα", "Ταξιδεύει πιο μακριά", "Λυγίζει προς τα πάνω και χάνεται στον ουρανό", "Απορροφάται από το έδαφος"], 2, "Τα ηχητικά κύματα λυγίζουν προς τον πιο κρύο αέρα, δηλαδή προς τα πάνω"),
  Q("Τι είναι η θερμοκρασιακή αναστροφή;", ["Ένα στρώμα κρύου αέρα κάτω από ένα στρώμα θερμότερου", "Ένας δυνατός άνεμος τη νύχτα", "Η απότομη άνοδος της θερμοκρασίας το πρωί", "Η ομίχλη πάνω από τα ποτάμια"], 0, "ένα στρώμα κρύου αέρα κάτω από ένα στρώμα θερμότερου"),
 ],
 "gloss": {"φυσικό": "φυσικός — physicist", "ατμόσφαιρας": "ατμόσφαιρα — atmosphere", "καμπάνες": "καμπάνα — church bell", "προφανές": "προφανής — obvious", "θερμοκρασία": "θερμοκρασία — temperature", "έδαφος": "έδαφος — ground", "λυγίζουν": "λυγίζω — to bend", "αίθριος": "αίθριος — clear, fair", "ψύχεται": "ψύχομαι — to cool", "στρώμα": "στρώμα — layer", "θερμοκρασιακή αναστροφή": "θερμοκρασιακή αναστροφή — temperature inversion", "αντανακλά": "αντανακλώ — to reflect", "αόρατο": "αόρατος — invisible", "πηγή": "πηγή — source"},
})

rnd = random.Random(170)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-170.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
