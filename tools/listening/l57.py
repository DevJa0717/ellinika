# Source for library/listening/listening-57.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l57.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l57-ann-synedrio", "title": "Αλλαγές στο πρόγραμμα του συνεδρίου", "title_en": "Changes to the conference programme", "type": "announcement", "level": "B2",
 "context_el": "Παρακολουθείτε ένα επιστημονικό συνέδριο σε ένα ξενοδοχείο της Θεσσαλονίκης. Θα ακούσετε μια ανακοίνωση πριν από την έναρξη της πρωινής συνεδρίας.",
 "script": [
  L("Ανακοίνωση", "f", "Καλημέρα σας και καλώς ήρθατε στη δεύτερη μέρα του συνεδρίου. Πριν ξεκινήσουμε, θα ήθελα να σας ενημερώσω για δύο αλλαγές στο πρόγραμμα. Η ομιλία του καθηγητή Ραφαήλ Δούκα, που ήταν προγραμματισμένη για τις έντεκα, μεταφέρεται στις τέσσερις το απόγευμα, λόγω καθυστέρησης της πτήσης του.", "Good morning and welcome to the second day of the conference. Before we begin, I'd like to inform you of two changes to the programme. Professor Rafail Doukas's talk, scheduled for eleven, is moved to four in the afternoon because of a delay to his flight."),
  L("Ανακοίνωση", "f", "Επίσης, το εργαστήριο για τη συγγραφή επιστημονικών άρθρων δεν θα γίνει στην αίθουσα «Αριστοτέλης», αλλά στην αίθουσα «Θερμαϊκός», στον πρώτο όροφο, γιατί δηλώθηκαν περισσότεροι συμμετέχοντες από όσους περιμέναμε.", "Also, the workshop on writing scientific articles will not take place in the Aristotelis room but in the Thermaikos room, on the first floor, because more participants signed up than we expected."),
  L("Ανακοίνωση", "f", "Υπενθυμίζουμε ότι οι βεβαιώσεις παρακολούθησης θα δοθούν αύριο μετά τη λήξη των εργασιών, στη γραμματεία του συνεδρίου. Σας ευχόμαστε μια δημιουργική μέρα.", "We remind you that certificates of attendance will be handed out tomorrow after the close of proceedings, at the conference secretariat. We wish you a productive day."),
 ],
 "questions": [
  Q("Γιατί μεταφέρεται η ομιλία του καθηγητή Δούκα;", ["Γιατί είναι άρρωστος", "Γιατί καθυστέρησε η πτήση του", "Γιατί άλλαξε η αίθουσα", "Γιατί ζητήθηκε από τους συμμετέχοντες"], 1, "μεταφέρεται στις τέσσερις το απόγευμα, λόγω καθυστέρησης της πτήσης του"),
  Q("Γιατί αλλάζει αίθουσα το εργαστήριο;", ["Γιατί η αίθουσα «Αριστοτέλης» έχει βλάβη", "Γιατί δηλώθηκαν περισσότεροι συμμετέχοντες από όσους περίμεναν", "Γιατί ακυρώθηκε μια άλλη ομιλία", "Γιατί ο πρώτος όροφος είναι πιο ήσυχος"], 1, "γιατί δηλώθηκαν περισσότεροι συμμετέχοντες από όσους περιμέναμε"),
  Q("Πότε θα δοθούν οι βεβαιώσεις παρακολούθησης;", ["Σήμερα το απόγευμα", "Αύριο μετά τη λήξη των εργασιών", "Με ηλεκτρονικό ταχυδρομείο", "Στην αρχή κάθε συνεδρίας"], 1, "οι βεβαιώσεις παρακολούθησης θα δοθούν αύριο μετά τη λήξη των εργασιών"),
 ],
 "gloss": {"συνεδρίου": "συνέδριο — conference", "συνεδρίας": "συνεδρία — session", "εργαστήριο": "εργαστήριο — workshop", "συγγραφή": "συγγραφή — writing", "δηλώθηκαν": "δηλώνομαι — to sign up, register", "βεβαιώσεις παρακολούθησης": "βεβαίωση παρακολούθησης — certificate of attendance", "λήξη": "λήξη — end, close", "γραμματεία": "γραμματεία — secretariat"},
})

ITEMS.append({
 "id": "l57-vm-katharistria", "title": "Μήνυμα από την καθαρίστρια", "title_en": "A message from the cleaner", "type": "voicemail", "level": "B2",
 "context_el": "Μια κυρία έρχεται να καθαρίσει το σπίτι σας κάθε Παρασκευή. Θα ακούσετε ένα μήνυμα που σας άφησε στον τηλεφωνητή.",
 "script": [
  L("Καθαρίστρια", "f", "Καλησπέρα, κύριε Βασιλείου, η Λιλιάνα είμαι. Ήθελα να σας πω ότι αυτή την Παρασκευή δεν θα μπορέσω να έρθω, γιατί πρέπει να συνοδεύσω την κόρη μου στο νοσοκομείο για κάποιες εξετάσεις. Τίποτα σοβαρό, μην ανησυχείτε.", "Good evening, Mr Vasileiou, it's Liliana. I wanted to tell you that this Friday I won't be able to come, because I have to go with my daughter to the hospital for some tests. Nothing serious, don't worry."),
  L("Καθαρίστρια", "f", "Αν σας βολεύει, μπορώ να έρθω το Σάββατο το πρωί αντί για την Παρασκευή. Αν όχι, έρχομαι κανονικά την επόμενη εβδομάδα. Επίσης, την προηγούμενη φορά πρόσεξα ότι το απορροφητικό σας χάλασε, δεν ανάβει το λαμπάκι. Και τελείωσε το υγρό για τα τζάμια, αν μπορείτε να πάρετε.", "If it suits you, I can come on Saturday morning instead of Friday. If not, I'll come as usual next week. Also, last time I noticed that your cooker hood has broken; the little light doesn't come on. And the glass cleaner has run out, if you can buy some."),
  L("Καθαρίστρια", "f", "Στείλτε μου ένα μήνυμα για το Σάββατο. Ευχαριστώ πολύ και καλό βράδυ.", "Send me a message about Saturday. Thank you very much and good evening."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να έρθει η Λιλιάνα την Παρασκευή;", ["Γιατί είναι η ίδια άρρωστη", "Γιατί πρέπει να συνοδεύσει την κόρη της στο νοσοκομείο", "Γιατί έχει άλλη δουλειά", "Γιατί φεύγει διακοπές"], 1, "πρέπει να συνοδεύσω την κόρη μου στο νοσοκομείο για κάποιες εξετάσεις"),
  Q("Τι προτείνει;", ["Να έρθει την Πέμπτη", "Να έρθει το Σάββατο το πρωί", "Να στείλει μια φίλη της", "Να μην έρθει για έναν μήνα"], 1, "μπορώ να έρθω το Σάββατο το πρωί αντί για την Παρασκευή"),
  Q("Τι πρόσεξε την προηγούμενη φορά;", ["Ότι χάλασε το πλυντήριο", "Ότι χάλασε το απορροφητικό", "Ότι έσπασε ένα τζάμι", "Ότι έλειπε ένα κλειδί"], 1, "πρόσεξα ότι το απορροφητικό σας χάλασε"),
 ],
 "gloss": {"συνοδεύσω": "συνοδεύω — to accompany", "εξετάσεις": "εξετάσεις — (medical) tests", "βολεύει": "βολεύει — it suits", "απορροφητικό": "απορροφητικός (απορροφητήρας) — cooker hood", "λαμπάκι": "λαμπάκι — little light", "τζάμια": "τζάμι — window pane, glass"},
})

ITEMS.append({
 "id": "l57-dia-theatro", "title": "Εισιτήρια για το θέατρο", "title_en": "Theatre tickets", "type": "dialogue", "level": "B2",
 "context_el": "Ένας θεατής αγοράζει εισιτήρια στο ταμείο ενός θεάτρου. Θα ακούσετε τη συζήτησή του με την ταμία.",
 "script": [
  L("Θεατής", "m", "Καλησπέρα. Θα ήθελα δύο εισιτήρια για τον «Γλάρο» του Τσέχοφ, για το Σάββατο το βράδυ, αν υπάρχουν.", "Good evening. I'd like two tickets for Chekhov's The Seagull for Saturday evening, if there are any."),
  L("Ταμίας", "f", "Για το Σάββατο έχουν μείνει ελάχιστες θέσεις, μόνο στον εξώστη, στις τελευταίες σειρές. Η ορατότητα είναι καλή, αλλά είναι αρκετά ψηλά. Αν θέλετε πλατεία, έχω καλές θέσεις για την Κυριακή το απόγευμα.", "For Saturday there are very few seats left, only in the balcony, in the back rows. The view is good, but it's quite high up. If you want the stalls, I have good seats for Sunday afternoon."),
  L("Θεατής", "m", "Η γυναίκα μου ζαλίζεται στα ύψη, οπότε προτιμώ την Κυριακή. Πόσο κοστίζουν;", "My wife gets dizzy at heights, so I'd rather have Sunday. How much are they?"),
  L("Ταμίας", "f", "Είκοσι δύο ευρώ το κανονικό. Υπάρχει μειωμένο για φοιτητές, ανέργους και άτομα άνω των εξήντα πέντε, με την επίδειξη της σχετικής ταυτότητας.", "Twenty-two euros full price. There's a reduced ticket for students, the unemployed and people over sixty-five, on showing the relevant ID."),
  L("Θεατής", "m", "Η γυναίκα μου είναι εξήντα επτά, άρα δικαιούται μειωμένο. Α, και πόσο διαρκεί η παράσταση;", "My wife is sixty-seven, so she's entitled to a reduced ticket. Oh, and how long is the performance?"),
  L("Ταμίας", "f", "Δύο ώρες και είκοσι λεπτά, με ένα διάλειμμα. Σας παρακαλώ να είστε εδώ τουλάχιστον ένα τέταρτο νωρίτερα, γιατί μετά την έναρξη δεν επιτρέπεται η είσοδος.", "Two hours and twenty minutes, with one interval. Please be here at least a quarter of an hour early, because once it starts no entry is allowed."),
 ],
 "questions": [
  Q("Γιατί ο θεατής δεν παίρνει εισιτήρια για το Σάββατο;", ["Γιατί είναι πολύ ακριβά", "Γιατί υπάρχουν μόνο ψηλά θέσεις στον εξώστη και η γυναίκα του ζαλίζεται", "Γιατί η παράσταση ακυρώθηκε", "Γιατί δουλεύει το Σάββατο"], 1, "Η γυναίκα μου ζαλίζεται στα ύψη, οπότε προτιμώ την Κυριακή"),
  Q("Ποιοι δικαιούνται μειωμένο εισιτήριο;", ["Μόνο τα παιδιά", "Φοιτητές, άνεργοι και άτομα άνω των εξήντα πέντε", "Όσοι αγοράζουν πάνω από δύο εισιτήρια", "Οι συνδρομητές του θεάτρου"], 1, "Υπάρχει μειωμένο για φοιτητές, ανέργους και άτομα άνω των εξήντα πέντε"),
  Q("Τι πρέπει να προσέξουν την ημέρα της παράστασης;", ["Να φέρουν φαγητό", "Να έρθουν τουλάχιστον ένα τέταρτο νωρίτερα", "Να κλείσουν τα κινητά στο διάλειμμα", "Να ντυθούν επίσημα"], 1, "Σας παρακαλώ να είστε εδώ τουλάχιστον ένα τέταρτο νωρίτερα"),
 ],
 "gloss": {"ταμείο": "ταμείο — box office", "εξώστη": "εξώστης — balcony (in a theatre)", "ορατότητα": "ορατότητα — view, visibility", "πλατεία": "πλατεία — stalls", "ζαλίζεται": "ζαλίζομαι — to feel dizzy", "μειωμένο": "μειωμένο (εισιτήριο) — reduced ticket", "επίδειξη": "επίδειξη — showing, display", "διάλειμμα": "διάλειμμα — interval"},
})

ITEMS.append({
 "id": "l57-dia-syntagi", "title": "Η συνταγή της γιαγιάς", "title_en": "Grandma's recipe", "type": "dialogue", "level": "B2",
 "context_el": "Μια νεαρή γυναίκα τηλεφωνεί στη γιαγιά της για να της ζητήσει μια συνταγή. Θα ακούσετε τη συζήτησή τους.",
 "script": [
  L("Δανάη", "f", "Γιαγιά, καλησπέρα! Θέλω να φτιάξω τα γεμιστά σου για τους φίλους μου το Σάββατο. Μου λες πώς τα κάνεις;", "Grandma, good evening! I want to make your stuffed vegetables for my friends on Saturday. Will you tell me how you make them?"),
  L("Γιαγιά", "f", "Χαρά μου, κορίτσι μου! Λοιπόν, παίρνεις ντομάτες και πιπεριές, όχι πολύ μεγάλες. Κόβεις το καπάκι από πάνω και τις αδειάζεις με ένα κουταλάκι. Την ψίχα της ντομάτας μην την πετάξεις, θα τη χρειαστείς για τη γέμιση.", "My pleasure, my girl! Well, you take tomatoes and peppers, not too big. You cut the lid off the top and hollow them out with a teaspoon. Don't throw away the tomato pulp; you'll need it for the filling."),
  L("Δανάη", "f", "Και τι βάζεις στη γέμιση; Βάζεις κιμά;", "And what do you put in the filling? Mince?"),
  L("Γιαγιά", "f", "Εγώ τα κάνω νηστίσιμα, μόνο με ρύζι. Πρώτα τσιγαρίζεις κρεμμύδι στο λάδι, ρίχνεις το ρύζι, την ψίχα, πολύ μαϊντανό και δυόσμο. Το μυστικό είναι να μη μαγειρέψεις το ρύζι εντελώς, γιατί θα τελειώσει στον φούρνο. Γεμίζεις τα λαχανικά ως τα τρία τέταρτα, όχι μέχρι πάνω, γιατί το ρύζι φουσκώνει.", "I make them meatless, with just rice. You fry onion in oil, add the rice, the pulp, lots of parsley and mint. The secret is not to cook the rice completely, because it will finish in the oven. You fill the vegetables three-quarters full, not to the top, because the rice swells."),
  L("Δανάη", "f", "Και πόση ώρα στον φούρνο;", "And how long in the oven?"),
  L("Γιαγιά", "f", "Γύρω στη μιάμιση ώρα, στους εκατόν ογδόντα. Βάλε και πατάτες ανάμεσα. Και να τα αφήσεις να κρυώσουν λίγο πριν τα σερβίρεις· είναι πιο νόστιμα χλιαρά.", "About an hour and a half, at a hundred and eighty. Put some potatoes in between too. And let them cool a little before you serve them; they're tastier lukewarm."),
 ],
 "questions": [
  Q("Τι πρέπει να κάνει η Δανάη με την ψίχα της ντομάτας;", ["Να την πετάξει", "Να τη χρησιμοποιήσει στη γέμιση", "Να τη βάλει στη σαλάτα", "Να τη φυλάξει για σάλτσα"], 1, "Την ψίχα της ντομάτας μην την πετάξεις, θα τη χρειαστείς για τη γέμιση"),
  Q("Γιατί δεν πρέπει να μαγειρέψει το ρύζι εντελώς;", ["Γιατί θα κολλήσει", "Γιατί θα τελειώσει το μαγείρεμα στον φούρνο", "Γιατί θα χάσει τη γεύση του", "Γιατί δεν θα χωράει"], 1, "να μη μαγειρέψεις το ρύζι εντελώς, γιατί θα τελειώσει στον φούρνο"),
  Q("Πώς πιστεύει η γιαγιά ότι είναι πιο νόστιμα τα γεμιστά;", ["Πολύ ζεστά", "Χλιαρά", "Κρύα από το ψυγείο", "Την επόμενη μέρα"], 1, "είναι πιο νόστιμα χλιαρά"),
 ],
 "gloss": {"γεμιστά": "γεμιστά — stuffed vegetables", "ψίχα": "ψίχα — pulp, flesh", "γέμιση": "γέμιση — filling", "κιμά": "κιμάς — mince", "νηστίσιμα": "νηστίσιμος — meatless (suitable for fasting)", "τσιγαρίζεις": "τσιγαρίζω — to sauté, fry lightly", "δυόσμο": "δυόσμος — mint", "φουσκώνει": "φουσκώνω — to swell", "χλιαρά": "χλιαρός — lukewarm"},
})

ITEMS.append({
 "id": "l57-int-kosmimatopoios", "title": "Μια κοσμηματοποιός", "title_en": "A jewellery maker", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια νεαρή κοσμηματοποιό.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Καλλέργη, τα κοσμήματά σας είναι εμπνευσμένα από την αρχαία ελληνική τέχνη. Πώς ξεκίνησε αυτή η ιδέα;", "Ms Kallergi, your jewellery is inspired by ancient Greek art. How did this idea begin?"),
  L("Κοσμηματοποιός", "f", "Σπούδαζα αρχαιολογία και περνούσα ώρες στα μουσεία. Με μάγευαν τα χρυσά στεφάνια και τα σκουλαρίκια της ελληνιστικής εποχής. Κάποια στιγμή σκέφτηκα: γιατί να μη φτιάξω κάτι παρόμοιο, αλλά που να φοριέται σήμερα; Έτσι γράφτηκα σε μια σχολή αργυροχρυσοχοΐας, παράλληλα με τις σπουδές μου.", "I was studying archaeology and spent hours in museums. I was fascinated by the gold wreaths and earrings of the Hellenistic period. At some point I thought: why not make something similar, but wearable today? So I enrolled in a gold- and silversmithing school alongside my studies."),
  L("Δημοσιογράφος", "m", "Πώς δουλεύετε;", "How do you work?"),
  L("Κοσμηματοποιός", "f", "Όλα γίνονται με το χέρι, στο μικρό μου εργαστήριο στο Ψυρρή. Ένα δαχτυλίδι μπορεί να μου πάρει μια μέρα, ένα περιδέραιο και μια εβδομάδα. Χρησιμοποιώ κυρίως ανακυκλωμένο ασήμι, γιατί η εξόρυξη μετάλλων έχει τεράστιο περιβαλλοντικό κόστος.", "Everything is done by hand, in my small workshop in Psyrri. A ring can take me a day, a necklace even a week. I mainly use recycled silver, because metal mining has a huge environmental cost."),
  L("Δημοσιογράφος", "m", "Ποιοι είναι οι πελάτες σας;", "Who are your customers?"),
  L("Κοσμηματοποιός", "f", "Πολλοί τουρίστες, φυσικά, αλλά και Έλληνες που θέλουν ένα δώρο με νόημα. Το πιο συγκινητικό ήταν ένα ζευγάρι που μου ζήτησε βέρες με ένα μοτίβο από ένα αγγείο που είχαν δει στο πρώτο τους ραντεβού, στο Εθνικό Αρχαιολογικό Μουσείο.", "Many tourists, of course, but also Greeks who want a meaningful gift. The most moving was a couple who asked me for wedding rings with a pattern from a vase they had seen on their first date, at the National Archaeological Museum."),
 ],
 "questions": [
  Q("Τι σπούδαζε η κοσμηματοποιός;", ["Καλές τέχνες", "Αρχαιολογία", "Αρχιτεκτονική", "Ιστορία της μόδας"], 1, "Σπούδαζα αρχαιολογία και περνούσα ώρες στα μουσεία"),
  Q("Γιατί χρησιμοποιεί κυρίως ανακυκλωμένο ασήμι;", ["Γιατί είναι φτηνότερο", "Γιατί η εξόρυξη μετάλλων έχει μεγάλο περιβαλλοντικό κόστος", "Γιατί το ζητούν οι τουρίστες", "Γιατί είναι πιο εύκολο στη δουλειά"], 1, "η εξόρυξη μετάλλων έχει τεράστιο περιβαλλοντικό κόστος"),
  Q("Τι της ζήτησε το ζευγάρι;", ["Ένα αντίγραφο αρχαίου στεφανιού", "Βέρες με ένα μοτίβο από ένα αγγείο του μουσείου", "Σκουλαρίκια για τον γάμο", "Ένα περιδέραιο για επέτειο"], 1, "μου ζήτησε βέρες με ένα μοτίβο από ένα αγγείο που είχαν δει στο πρώτο τους ραντεβού"),
 ],
 "gloss": {"εμπνευσμένα": "εμπνευσμένος — inspired", "στεφάνια": "στεφάνι — wreath", "σκουλαρίκια": "σκουλαρίκι — earring", "αργυροχρυσοχοΐας": "αργυροχρυσοχοΐα — gold- and silversmithing", "περιδέραιο": "περιδέραιο — necklace", "εξόρυξη": "εξόρυξη — mining", "βέρες": "βέρα — wedding ring", "μοτίβο": "μοτίβο — pattern, motif"},
})

ITEMS.append({
 "id": "l57-rep-myloi", "title": "Οι ανεμόμυλοι της Μυκόνου", "title_en": "The windmills of Mykonos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από τους ανεμόμυλους της Μυκόνου.",
 "script": [
  L("Ρεπόρτερ", "f", "Στέκομαι στον λόφο πάνω από τη Μικρή Βενετία, μπροστά στους περίφημους ανεμόμυλους της Μυκόνου, τους Κάτω Μύλους, όπως τους λένε οι ντόπιοι. Είναι ίσως το πιο φωτογραφημένο σημείο του νησιού, ειδικά την ώρα του ηλιοβασιλέματος.", "I'm standing on the hill above Little Venice, in front of the famous windmills of Mykonos, the Kato Myloi, as the locals call them. It is perhaps the most photographed spot on the island, especially at sunset."),
  L("Ρεπόρτερ", "f", "Οι πρώτοι μύλοι χτίστηκαν τον 16ο αιώνα, την εποχή της βενετοκρατίας, και για τρεις αιώνες άλεθαν το σιτάρι όχι μόνο του νησιού, αλλά και των καραβιών που περνούσαν. Χάρη στους δυνατούς βόρειους ανέμους, τα μελτέμια, η Μύκονος ήταν ιδανική για αυτή τη δουλειά.", "The first mills were built in the 16th century, under Venetian rule, and for three centuries they ground the wheat not only of the island but also of the passing ships. Thanks to the strong northerly winds, the meltemia, Mykonos was ideal for this work."),
  L("Ρεπόρτερ", "f", "Με την εμφάνιση των ηλεκτρικών μύλων, στις αρχές του εικοστού αιώνα, οι ανεμόμυλοι σταμάτησαν να λειτουργούν και πολλοί ερειπώθηκαν. Σήμερα κάποιοι έχουν αναστηλωθεί, και ένας από αυτούς λειτουργεί ως μικρό μουσείο, όπου ο επισκέπτης μπορεί να δει πώς γινόταν το άλεσμα. Όπως μου είπε ο φύλακας, «οι μύλοι δεν αλέθουν πια σιτάρι· αλέθουν αναμνήσεις».", "With the arrival of electric mills, in the early twentieth century, the windmills stopped working and many fell into ruin. Today some have been restored, and one of them operates as a small museum, where visitors can see how milling was done. As the guard told me, \"the mills no longer grind wheat; they grind memories\"."),
 ],
 "questions": [
  Q("Πότε χτίστηκαν οι πρώτοι ανεμόμυλοι;", ["Στην αρχαιότητα", "Τον 16ο αιώνα, την εποχή της βενετοκρατίας", "Τον 19ο αιώνα", "Μετά τον Δεύτερο Παγκόσμιο Πόλεμο"], 1, "Οι πρώτοι μύλοι χτίστηκαν τον 16ο αιώνα, την εποχή της βενετοκρατίας"),
  Q("Γιατί η Μύκονος ήταν ιδανική για ανεμόμυλους;", ["Γιατί είχε πολύ σιτάρι", "Χάρη στους δυνατούς βόρειους ανέμους", "Γιατί είχε πολλά ποτάμια", "Γιατί ήταν κοντά στη Βενετία"], 1, "Χάρη στους δυνατούς βόρειους ανέμους, τα μελτέμια"),
  Q("Πώς χρησιμοποιείται σήμερα ένας από τους μύλους;", ["Ως ξενοδοχείο", "Ως μικρό μουσείο", "Ως εστιατόριο", "Ως αρτοποιείο"], 1, "ένας από αυτούς λειτουργεί ως μικρό μουσείο"),
 ],
 "gloss": {"ανεμόμυλους": "ανεμόμυλος — windmill", "ηλιοβασιλέματος": "ηλιοβασίλεμα — sunset", "βενετοκρατίας": "βενετοκρατία — Venetian rule", "άλεθαν": "αλέθω — to grind", "μελτέμια": "μελτέμι — meltemi (summer north wind)", "ερειπώθηκαν": "ερειπώνομαι — to fall into ruin", "αναστηλωθεί": "αναστηλώνομαι — to be restored", "άλεσμα": "άλεσμα — milling"},
})

ITEMS.append({
 "id": "l57-dia-palaiopoleio", "title": "Στο παλαιοπωλείο", "title_en": "At the antique shop", "type": "dialogue", "level": "B2",
 "context_el": "Μια πελάτισσα μπαίνει σε ένα παλαιοπωλείο στο Μοναστηράκι. Θα ακούσετε τη συζήτησή της με τον ιδιοκτήτη.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Μου άρεσε πολύ αυτό το ξύλινο κουτί στη βιτρίνα. Μπορώ να το δω από κοντά;", "Good morning. I really liked that wooden box in the window. May I see it close up?"),
  L("Παλαιοπώλης", "m", "Βεβαίως, ορίστε. Είναι ένα κουτί για κοσμήματα από τη Σμύρνη, γύρω στο 1900. Δείτε τα σκαλίσματα στο καπάκι, όλα με το χέρι. Ήρθε από μια οικογένεια προσφύγων του '22.", "Of course, here you are. It's a jewellery box from Smyrna, around 1900. Look at the carving on the lid, all by hand. It came from a family of refugees from '22."),
  L("Πελάτισσα", "f", "Είναι υπέροχο. Πόσο κάνει;", "It's wonderful. How much is it?"),
  L("Παλαιοπώλης", "m", "Εκατόν ογδόντα ευρώ. Ξέρω, δεν είναι λίγα, αλλά τέτοια κομμάτια δεν βρίσκονται εύκολα πια.", "A hundred and eighty euros. I know it's not cheap, but pieces like this aren't easy to find any more."),
  L("Πελάτισσα", "f", "Είναι λίγο πάνω από αυτό που σκόπευα να δώσω. Βλέπω επίσης ότι η κλειδαριά λείπει. Θα μου κάνατε μια καλύτερη τιμή; Ας πούμε, εκατόν τριάντα;", "It's a bit over what I meant to spend. I also see the lock is missing. Would you give me a better price? Say, a hundred and thirty?"),
  L("Παλαιοπώλης", "m", "Εκατόν τριάντα είναι πολύ χαμηλά. Ας το κλείσουμε στα εκατόν πενήντα, και σας δίνω και ένα πιστοποιητικό με την προέλευσή του. Σύμφωνοι;", "A hundred and thirty is too low. Let's settle at a hundred and fifty, and I'll also give you a certificate of its provenance. Agreed?"),
  L("Πελάτισσα", "f", "Σύμφωνοι!", "Agreed!"),
 ],
 "questions": [
  Q("Από πού προέρχεται το κουτί;", ["Από τη Βενετία", "Από τη Σμύρνη", "Από την Κωνσταντινούπολη", "Από τη Θεσσαλονίκη"], 1, "Είναι ένα κουτί για κοσμήματα από τη Σμύρνη"),
  Q("Ποιο ελάττωμα παρατηρεί η πελάτισσα;", ["Ότι έχει σπάσει το καπάκι", "Ότι λείπει η κλειδαριά", "Ότι έχει ξεβάψει", "Ότι δεν είναι γνήσιο"], 1, "Βλέπω επίσης ότι η κλειδαριά λείπει"),
  Q("Σε ποια τιμή συμφωνούν τελικά;", ["Εκατόν τριάντα ευρώ", "Εκατόν πενήντα ευρώ", "Εκατόν ογδόντα ευρώ", "Εκατό ευρώ"], 1, "Ας το κλείσουμε στα εκατόν πενήντα"),
 ],
 "gloss": {"παλαιοπωλείο": "παλαιοπωλείο — antique shop", "βιτρίνα": "βιτρίνα — shop window", "σκαλίσματα": "σκάλισμα — carving", "προσφύγων": "πρόσφυγας — refugee", "σκόπευα": "σκοπεύω — to intend", "κλειδαριά": "κλειδαριά — lock", "πιστοποιητικό": "πιστοποιητικό — certificate", "προέλευσή": "προέλευση — provenance, origin"},
})

ITEMS.append({
 "id": "l57-mono-magistros", "title": "Ξενάγηση στο Παλάτι του Μεγάλου Μαγίστρου", "title_en": "A tour of the Palace of the Grand Master", "type": "monologue", "level": "B2",
 "context_el": "Επισκέπτεστε την παλιά πόλη της Ρόδου με μια ομάδα. Θα ακούσετε τον ξεναγό μπροστά στο Παλάτι του Μεγάλου Μαγίστρου.",
 "script": [
  L("Ξεναγός", "m", "Βρισκόμαστε μπροστά στο Παλάτι του Μεγάλου Μαγίστρου, στο ψηλότερο σημείο της μεσαιωνικής πόλης της Ρόδου. Το παλάτι χτίστηκε τον 14ο αιώνα από τους Ιωαννίτες Ιππότες, που κυβέρνησαν το νησί για περισσότερα από διακόσια χρόνια, και ήταν η κατοικία του αρχηγού τους, του Μεγάλου Μαγίστρου.", "We are standing in front of the Palace of the Grand Master, at the highest point of the medieval town of Rhodes. The palace was built in the 14th century by the Knights of St John, who ruled the island for more than two hundred years, and it was the residence of their leader, the Grand Master."),
  L("Ξεναγός", "m", "Αυτό που ίσως δεν ξέρετε είναι ότι το κτίριο που βλέπετε δεν είναι εντελώς αυθεντικό. Το 1856 ένας κεραυνός χτύπησε μια κοντινή εκκλησία, όπου ήταν αποθηκευμένη πυρίτιδα, και η έκρηξη κατέστρεψε σχεδόν ολοκληρωτικά το παλάτι.", "What you may not know is that the building you see is not entirely authentic. In 1856 lightning struck a nearby church where gunpowder was stored, and the explosion almost completely destroyed the palace."),
  L("Ξεναγός", "m", "Το ξανάχτισαν οι Ιταλοί, τη δεκαετία του 1930, όταν τα Δωδεκάνησα ήταν υπό ιταλική κατοχή, με σκοπό να γίνει θερινή κατοικία του βασιλιά της Ιταλίας και του Μουσολίνι. Μέσα θα δείτε υπέροχα ψηφιδωτά δάπεδα, τα οποία όμως μεταφέρθηκαν εδώ από την Κω. Είναι, λοιπόν, ένα μνημείο που διηγείται πολλές ιστορίες ταυτόχρονα.", "It was rebuilt by the Italians in the 1930s, when the Dodecanese was under Italian occupation, to be a summer residence for the king of Italy and Mussolini. Inside you will see wonderful mosaic floors, which, however, were brought here from Kos. It is, then, a monument that tells many stories at once."),
 ],
 "questions": [
  Q("Ποιοι έχτισαν αρχικά το παλάτι;", ["Οι Βενετοί", "Οι Ιωαννίτες Ιππότες", "Οι Οθωμανοί", "Οι Ιταλοί"], 1, "Το παλάτι χτίστηκε τον 14ο αιώνα από τους Ιωαννίτες Ιππότες"),
  Q("Τι κατέστρεψε το παλάτι το 1856;", ["Ένας σεισμός", "Μια έκρηξη πυρίτιδας μετά από κεραυνό", "Μια πολιορκία", "Μια πυρκαγιά από αμέλεια"], 1, "ένας κεραυνός χτύπησε μια κοντινή εκκλησία, όπου ήταν αποθηκευμένη πυρίτιδα, και η έκρηξη κατέστρεψε σχεδόν ολοκληρωτικά το παλάτι"),
  Q("Από πού προέρχονται τα ψηφιδωτά δάπεδα;", ["Από τη Ρώμη", "Από την Κω", "Από την Αθήνα", "Από την Κρήτη"], 1, "υπέροχα ψηφιδωτά δάπεδα, τα οποία όμως μεταφέρθηκαν εδώ από την Κω"),
 ],
 "gloss": {"μεσαιωνικής": "μεσαιωνικός — medieval", "Ιωαννίτες Ιππότες": "Ιωαννίτες Ιππότες — Knights of St John (Hospitallers)", "κατοικία": "κατοικία — residence", "κεραυνός": "κεραυνός — lightning bolt", "πυρίτιδα": "πυρίτιδα — gunpowder", "ολοκληρωτικά": "ολοκληρωτικά — completely", "ψηφιδωτά δάπεδα": "ψηφιδωτό δάπεδο — mosaic floor", "ταυτόχρονα": "ταυτόχρονα — at the same time"},
})

ITEMS.append({
 "id": "l57-c1-gmo", "title": "Γενετικά τροποποιημένα φυτά: φόβοι και δεδομένα", "title_en": "Genetically modified crops: fears and facts", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια βιολόγο φυτών για τα γενετικά τροποποιημένα φυτά.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Νικολαΐδου, η φράση «γενετικά τροποποιημένα» προκαλεί σε πολλούς αμέσως καχυποψία. Είναι δικαιολογημένη;", "Ms Nikolaidou, the phrase \"genetically modified\" immediately makes many people suspicious. Is that justified?"),
  L("Βιολόγος", "f", "Η καχυποψία είναι κατανοητή, αλλά πρέπει να ξεχωρίσουμε δύο ζητήματα. Το πρώτο είναι η ασφάλεια για την υγεία. Εδώ, οι μεγάλοι επιστημονικοί οργανισμοί έχουν καταλήξει, ύστερα από δεκαετίες ερευνών, ότι τα εγκεκριμένα γενετικά τροποποιημένα τρόφιμα δεν είναι πιο επικίνδυνα από τα συμβατικά. Το δεύτερο ζήτημα, όμως, είναι πολιτικό και οικονομικό, και εκεί οι ανησυχίες είναι πολύ πιο βάσιμες.", "Suspicion is understandable, but we have to separate two issues. The first is safety for health. Here, the major scientific bodies have concluded, after decades of research, that approved genetically modified foods are no more dangerous than conventional ones. The second issue, though, is political and economic, and there the concerns are much more well-founded."),
  L("Δημοσιογράφος", "m", "Τι εννοείτε;", "What do you mean?"),
  L("Βιολόγος", "f", "Ότι λίγες πολυεθνικές εταιρείες κατέχουν τα διπλώματα ευρεσιτεχνίας για τους σπόρους, και οι αγρότες γίνονται εξαρτημένοι από αυτές. Υπάρχει επίσης ο κίνδυνος της μονοκαλλιέργειας, που μειώνει τη βιοποικιλότητα. Η Ελλάδα, όπως αρκετές ευρωπαϊκές χώρες, έχει επιλέξει να απαγορεύσει την καλλιέργειά τους, εν μέρει και για να προστατέψει τις τοπικές ποικιλίες.", "That a few multinational companies hold the patents on the seeds, and farmers become dependent on them. There's also the risk of monoculture, which reduces biodiversity. Greece, like several European countries, has chosen to ban growing them, partly to protect local varieties."),
  L("Δημοσιογράφος", "m", "Και οι νέες τεχνικές «γονιδιακής επεξεργασίας»;", "And the new \"gene editing\" techniques?"),
  L("Βιολόγος", "f", "Εκεί η συζήτηση είναι ανοιχτή. Αυτές οι τεχνικές επιτρέπουν πολύ πιο στοχευμένες αλλαγές, χωρίς να εισάγεται γενετικό υλικό από άλλο είδος. Θα μπορούσαν, για παράδειγμα, να βοηθήσουν τις καλλιέργειες να αντέξουν την ξηρασία, κάτι κρίσιμο για τη Μεσόγειο. Το ερώτημα είναι αν θα τις ρυθμίσουμε με τους ίδιους αυστηρούς κανόνες. Κατά τη γνώμη μου, η απάντηση πρέπει να βασιστεί στα δεδομένα, όχι στον φόβο.", "There the debate is open. These techniques allow much more targeted changes, without introducing genetic material from another species. They could, for example, help crops withstand drought, which is crucial for the Mediterranean. The question is whether we will regulate them with the same strict rules. In my view, the answer must be based on data, not on fear."),
 ],
 "questions": [
  Q("Τι έχουν καταλήξει οι επιστημονικοί οργανισμοί για την ασφάλεια των εγκεκριμένων γενετικά τροποποιημένων τροφίμων;", ["Ότι είναι επικίνδυνα", "Ότι δεν είναι πιο επικίνδυνα από τα συμβατικά", "Ότι δεν έχουν μελετηθεί αρκετά", "Ότι είναι πιο υγιεινά"], 1, "τα εγκεκριμένα γενετικά τροποποιημένα τρόφιμα δεν είναι πιο επικίνδυνα από τα συμβατικά"),
  Q("Ποια ανησυχία θεωρεί η βιολόγος βάσιμη;", ["Ότι προκαλούν αλλεργίες", "Την εξάρτηση των αγροτών από λίγες πολυεθνικές", "Ότι αλλάζουν τη γεύση", "Ότι είναι ακριβά για τους καταναλωτές"], 1, "λίγες πολυεθνικές εταιρείες κατέχουν τα διπλώματα ευρεσιτεχνίας για τους σπόρους, και οι αγρότες γίνονται εξαρτημένοι"),
  Q("Γιατί, εν μέρει, η Ελλάδα απαγόρευσε την καλλιέργειά τους;", ["Για να προστατέψει τις τοπικές ποικιλίες", "Γιατί το ζήτησαν οι πολυεθνικές", "Γιατί είναι παράνομα σε όλη την Ευρώπη", "Λόγω της ξηρασίας"], 0, "εν μέρει και για να προστατέψει τις τοπικές ποικιλίες"),
  Q("Πώς θα μπορούσαν να βοηθήσουν οι νέες τεχνικές γονιδιακής επεξεργασίας;", ["Να μειώσουν τις τιμές", "Να βοηθήσουν τις καλλιέργειες να αντέξουν την ξηρασία", "Να καταργήσουν τα λιπάσματα", "Να αυξήσουν τις εξαγωγές"], 1, "Θα μπορούσαν, για παράδειγμα, να βοηθήσουν τις καλλιέργειες να αντέξουν την ξηρασία"),
 ],
 "gloss": {"καχυποψία": "καχυποψία — suspicion", "εγκεκριμένα": "εγκεκριμένος — approved", "συμβατικά": "συμβατικός — conventional", "βάσιμες": "βάσιμος — well-founded", "διπλώματα ευρεσιτεχνίας": "δίπλωμα ευρεσιτεχνίας — patent", "εξαρτημένοι": "εξαρτημένος — dependent", "μονοκαλλιέργειας": "μονοκαλλιέργεια — monoculture", "βιοποικιλότητα": "βιοποικιλότητα — biodiversity", "ποικιλίες": "ποικιλία — variety (of a crop)", "στοχευμένες": "στοχευμένος — targeted", "ξηρασία": "ξηρασία — drought"},
})

ITEMS.append({
 "id": "l57-c1-dichasmos", "title": "Ο Εθνικός Διχασμός", "title_en": "The National Schism", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια ομιλία μιας ιστορικού για τον Εθνικό Διχασμό στα χρόνια του Πρώτου Παγκοσμίου Πολέμου.",
 "script": [
  L("Ιστορικός", "f", "Όταν ξέσπασε ο Πρώτος Παγκόσμιος Πόλεμος, το 1914, η Ελλάδα βγήκε από τους Βαλκανικούς Πολέμους μεγαλύτερη και αισιόδοξη. Πολύ σύντομα, όμως, η ηγεσία της χώρας διχάστηκε για ένα κρίσιμο ερώτημα: έπρεπε η Ελλάδα να μπει στον πόλεμο στο πλευρό της Αντάντ ή να μείνει ουδέτερη;", "When the First World War broke out in 1914, Greece had come out of the Balkan Wars larger and optimistic. Very soon, however, the country's leadership split over a crucial question: should Greece enter the war on the side of the Entente or remain neutral?"),
  L("Ιστορικός", "f", "Ο πρωθυπουργός Ελευθέριος Βενιζέλος πίστευε ότι η νίκη της Αντάντ θα έφερνε στην Ελλάδα νέα εδάφη. Ο βασιλιάς Κωνσταντίνος, αντίθετα, υποστήριζε την ουδετερότητα, εν μέρει επειδή θεωρούσε τη Γερμανία στρατιωτικά ανώτερη. Η σύγκρουση των δύο ανδρών οδήγησε σε δύο παραιτήσεις του Βενιζέλου μέσα στο 1915 και σε μια βαθιά συνταγματική κρίση.", "Prime Minister Eleftherios Venizelos believed an Entente victory would bring Greece new territory. King Constantine, by contrast, supported neutrality, partly because he considered Germany militarily superior. The clash between the two men led to two resignations by Venizelos during 1915 and a deep constitutional crisis."),
  L("Ιστορικός", "f", "Το 1916 ο Βενιζέλος σχημάτισε στη Θεσσαλονίκη μια προσωρινή κυβέρνηση, την Κυβέρνηση Εθνικής Αμύνης. Η χώρα είχε πλέον, κυριολεκτικά, δύο κυβερνήσεις. Τον Νοέμβριο του ίδιου χρόνου, στην Αθήνα, οι συγκρούσεις με αγγλογαλλικά στρατεύματα, τα λεγόμενα Νοεμβριανά, συνοδεύτηκαν από βίαιες διώξεις βενιζελικών. Τελικά, το 1917, ο Κωνσταντίνος αναγκάστηκε να εγκαταλείψει τη χώρα, και η Ελλάδα μπήκε στον πόλεμο.", "In 1916 Venizelos formed a provisional government in Thessaloniki, the Government of National Defence. The country now had, literally, two governments. In November of that year, in Athens, clashes with Anglo-French troops, the so-called Noemvriana, were accompanied by violent persecution of Venizelists. Finally, in 1917, Constantine was forced to leave the country and Greece entered the war."),
  L("Ιστορικός", "f", "Οι συνέπειες, όμως, ξεπέρασαν κατά πολύ τον πόλεμο. Ο διχασμός ανάμεσα σε βενιζελικούς και αντιβενιζελικούς διαπέρασε την ελληνική κοινωνία για δεκαετίες: χώρισε οικογένειες, στρατό και διοίκηση, και άφησε τη χώρα αδύναμη απέναντι στις κρίσεις που ακολούθησαν, με πρώτη τη Μικρασιατική Καταστροφή.", "The consequences, however, went far beyond the war. The split between Venizelists and anti-Venizelists ran through Greek society for decades: it divided families, the army and the administration, and left the country weak in the face of the crises that followed, starting with the Asia Minor Catastrophe."),
 ],
 "questions": [
  Q("Για ποιο ερώτημα διχάστηκε η ηγεσία της χώρας;", ["Για το πολίτευμα", "Αν η Ελλάδα έπρεπε να μπει στον πόλεμο με την Αντάντ ή να μείνει ουδέτερη", "Για τα σύνορα με τη Βουλγαρία", "Για την οικονομική πολιτική"], 1, "έπρεπε η Ελλάδα να μπει στον πόλεμο στο πλευρό της Αντάντ ή να μείνει ουδέτερη;"),
  Q("Γιατί, εν μέρει, ο Κωνσταντίνος υποστήριζε την ουδετερότητα;", ["Γιατί η Ελλάδα δεν είχε στρατό", "Γιατί θεωρούσε τη Γερμανία στρατιωτικά ανώτερη", "Γιατί το ζητούσε η Βουλή", "Γιατί ήθελε να παραιτηθεί ο Βενιζέλος"], 1, "εν μέρει επειδή θεωρούσε τη Γερμανία στρατιωτικά ανώτερη"),
  Q("Τι ήταν η Κυβέρνηση Εθνικής Αμύνης;", ["Η κυβέρνηση του βασιλιά στην Αθήνα", "Μια προσωρινή κυβέρνηση του Βενιζέλου στη Θεσσαλονίκη", "Μια στρατιωτική δικτατορία", "Μια κυβέρνηση της Αντάντ"], 1, "ο Βενιζέλος σχημάτισε στη Θεσσαλονίκη μια προσωρινή κυβέρνηση, την Κυβέρνηση Εθνικής Αμύνης"),
  Q("Ποια μακροπρόθεσμη συνέπεια του διχασμού αναφέρει η ιστορικός;", ["Την ανάπτυξη της οικονομίας", "Ότι χώρισε την κοινωνία για δεκαετίες και αποδυνάμωσε τη χώρα", "Την κατάργηση της μοναρχίας το 1917", "Τη γρήγορη συμφιλίωση των δύο παρατάξεων"], 1, "διαπέρασε την ελληνική κοινωνία για δεκαετίες … και άφησε τη χώρα αδύναμη"),
 ],
 "gloss": {"ξέσπασε": "ξεσπώ — to break out", "διχάστηκε": "διχάζομαι — to be split, divided", "Αντάντ": "Αντάντ — the Entente", "ουδέτερη": "ουδέτερος — neutral", "ουδετερότητα": "ουδετερότητα — neutrality", "ανώτερη": "ανώτερος — superior", "παραιτήσεις": "παραίτηση — resignation", "συνταγματική κρίση": "συνταγματική κρίση — constitutional crisis", "κυριολεκτικά": "κυριολεκτικά — literally", "διώξεις": "δίωξη — persecution", "διαπέρασε": "διαπερνώ — to run through, pervade"},
})

rnd = random.Random(57)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-57.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
