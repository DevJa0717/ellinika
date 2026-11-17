# Source for library/listening/listening-109.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l109.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l109-ann-kleisto-kastro", "title": "Κλειστό το κάστρο για εργασίες αποκατάστασης", "title_en": "The castle closed for restoration works", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση της εφορείας αρχαιοτήτων στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Η εφορεία αρχαιοτήτων ενημερώνει το κοινό ότι το βυζαντινό κάστρο της πόλης θα παραμείνει κλειστό για τους επισκέπτες από την πρώτη Δεκεμβρίου ως το τέλος Μαρτίου, λόγω εργασιών αποκατάστασης στο βόρειο τείχος.", "The ephorate of antiquities informs the public that the town's Byzantine castle will remain closed to visitors from the first of December until the end of March, due to restoration works on the north wall."),
  L("Εκφωνητής", "m", "Κατά τη διάρκεια των εργασιών θα παραμείνει ανοιχτό μόνο το μικρό μουσείο στην είσοδο του κάστρου, από Τρίτη ως Κυριακή, από τις εννιά ως τις τρεις. Η είσοδος στο μουσείο θα είναι δωρεάν όσο το κάστρο μένει κλειστό.", "During the works only the small museum at the castle entrance will remain open, from Tuesday to Sunday, from nine to three. Entry to the museum will be free while the castle stays closed."),
  L("Εκφωνητής", "m", "Τα σχολεία που είχαν κλείσει εκπαιδευτικές επισκέψεις στο κάστρο μπορούν να επικοινωνήσουν με την εφορεία για να τις μεταφέρουν σε άλλη ημερομηνία ή να παρακολουθήσουν μια ειδική παρουσίαση για τις εργασίες, που θα γίνεται στο μουσείο κάθε Πέμπτη.", "Schools that had booked educational visits to the castle can contact the ephorate to move them to another date or to attend a special presentation about the works, which will take place in the museum every Thursday."),
 ],
 "questions": [
  Q("Γιατί θα κλείσει το κάστρο;", ["Λόγω του κρύου", "Λόγω εργασιών αποκατάστασης στο βόρειο τείχος", "Λόγω έλλειψης προσωπικού", "Λόγω μιας ανασκαφής"], 1, "λόγω εργασιών αποκατάστασης στο βόρειο τείχος"),
  Q("Τι θα ισχύει για το μουσείο όσο το κάστρο μένει κλειστό;", ["Θα κλείσει κι αυτό", "Θα ανοίγει μόνο τα Σαββατοκύριακα", "Η είσοδος θα είναι δωρεάν", "Θα μεταφερθεί σε άλλο κτίριο"], 2, "Η είσοδος στο μουσείο θα είναι δωρεάν όσο το κάστρο μένει κλειστό"),
  Q("Τι μπορούν να κάνουν τα σχολεία;", ["Να μεταφέρουν την επίσκεψη ή να παρακολουθήσουν μια ειδική παρουσίαση", "Να επισκεφθούν το κάστρο με ειδική άδεια", "Να πάρουν πίσω τα χρήματά τους", "Να βοηθήσουν στις εργασίες"], 0, "να τις μεταφέρουν σε άλλη ημερομηνία ή να παρακολουθήσουν μια ειδική παρουσίαση"),
 ],
 "gloss": {"εφορεία": "εφορεία αρχαιοτήτων — ephorate (regional office) of antiquities", "αποκατάστασης": "αποκατάσταση — restoration", "τείχος": "τείχος — (city) wall", "εκπαιδευτικές": "εκπαιδευτικός — educational", "μεταφέρουν": "μεταφέρω — to move, transfer", "παρουσίαση": "παρουσίαση — presentation"}
})

ITEMS.append({
 "id": "l109-vm-ptychiaki", "title": "Μήνυμα από τη γραμματεία για την πτυχιακή", "title_en": "A message from the department office about your dissertation", "type": "voicemail", "level": "B2",
 "context_el": "Είστε φοιτητής. Ακούτε ένα μήνυμα από τη γραμματεία του τμήματος στον τηλεφωνητή.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα, κύριε Παπαδάκη, από τη γραμματεία του τμήματος Ιστορίας σας καλώ. Λάβαμε την πτυχιακή σας εργασία, αλλά λείπει η υπεύθυνη δήλωση ότι το κείμενο είναι δικό σας, υπογεγραμμένη. Χωρίς αυτήν δεν μπορούμε να ορίσουμε ημερομηνία παρουσίασης.", "Good morning, Mr Papadakis, I'm calling from the History department office. We received your dissertation, but the signed declaration that the text is your own is missing. Without it we can't set a date for your presentation."),
  L("Γραμματέας", "f", "Τη δήλωση μπορείτε να την κατεβάσετε από την ιστοσελίδα του τμήματος. Πρέπει να έχει γνήσιο υπογραφής, το οποίο γίνεται ηλεκτρονικά ή σε οποιοδήποτε ΚΕΠ. Στείλτε τη μας με ηλεκτρονικό ταχυδρομείο μέχρι την Παρασκευή.", "You can download the declaration from the department's website. It must have the signature certified, which can be done online or at any citizens' service centre. Send it to us by email by Friday."),
  L("Γραμματέας", "f", "Αν τη στείλετε έγκαιρα, η παρουσίαση θα γίνει στις δεκαοχτώ του μήνα, μαζί με τους άλλους φοιτητές του επιβλέποντα καθηγητή σας. Αλλιώς, η επόμενη ευκαιρία είναι τον Φεβρουάριο. Για οποιαδήποτε απορία, η γραμματεία δέχεται τηλεφωνήματα από τις έντεκα ως τη μία.", "If you send it in time, the presentation will be on the eighteenth of the month, together with your supervisor's other students. Otherwise, the next chance is in February. For any questions, the office takes calls from eleven to one."),
 ],
 "questions": [
  Q("Τι λείπει από τον φάκελο του φοιτητή;", ["Το αντίγραφο της ταυτότητας", "Η υπογεγραμμένη υπεύθυνη δήλωση ότι το κείμενο είναι δικό του", "Η περίληψη της εργασίας", "Η υπογραφή του καθηγητή"], 1, "λείπει η υπεύθυνη δήλωση ότι το κείμενο είναι δικό σας, υπογεγραμμένη"),
  Q("Πώς πρέπει να στείλει τη δήλωση;", ["Με ηλεκτρονικό ταχυδρομείο μέχρι την Παρασκευή", "Ταχυδρομικά", "Αυτοπροσώπως στη γραμματεία", "Μέσω του καθηγητή του"], 0, "Στείλτε τη μας με ηλεκτρονικό ταχυδρομείο μέχρι την Παρασκευή"),
  Q("Τι θα γίνει αν δεν τη στείλει έγκαιρα;", ["Θα χάσει το πτυχίο", "Θα πληρώσει πρόστιμο", "Η επόμενη ευκαιρία για παρουσίαση είναι τον Φεβρουάριο", "Θα πρέπει να ξαναγράψει την εργασία"], 2, "η επόμενη ευκαιρία είναι τον Φεβρουάριο"),
 ],
 "gloss": {"πτυχιακή": "πτυχιακή (εργασία) — undergraduate dissertation", "υπεύθυνη": "υπεύθυνη δήλωση — formal declaration", "υπογεγραμμένη": "υπογεγραμμένος — signed", "γνήσιο": "γνήσιο υπογραφής — certification of signature", "έγκαιρα": "έγκαιρα — in time", "επιβλέποντα": "επιβλέπων καθηγητής — supervisor"}
})

ITEMS.append({
 "id": "l109-dia-poio-athlima", "title": "Ποιο άθλημα θα κάνει ο μικρός;", "title_en": "Which sport should our son do?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο γονείς συζητούν σε ποιο άθλημα θα γράψουν τον εννιάχρονο γιο τους.",
 "script": [
  L("Βάσω", "f", "Ο Άγγελος θέλει να γραφτεί στο ποδόσφαιρο, όπως όλοι οι φίλοι του. Ο σύλλογος της γειτονιάς κάνει προπονήσεις τρεις φορές την εβδομάδα.", "Angelos wants to sign up for football, like all his friends. The neighbourhood club trains three times a week."),
  L("Λευτέρης", "m", "Τρεις φορές; Και τα αγγλικά και το πιάνο; Δεν θα του μένει χρόνος ούτε να ανασάνει. Εγώ θα προτιμούσα το κολύμπι. Είναι δύο φορές την εβδομάδα και κάνει καλό στην πλάτη του.", "Three times? What about English and piano? He won't have time to breathe. I'd prefer swimming. It's twice a week and it's good for his back."),
  L("Βάσω", "f", "Ναι, αλλά στο κολύμπι δεν έχει κανέναν φίλο. Πήγε πέρσι δύο μήνες και βαριόταν αφάνταστα. Το σημαντικό είναι να του αρέσει, αλλιώς θα το παρατήσει.", "Yes, but he has no friends at swimming. He went for two months last year and was bored stiff. The important thing is that he enjoys it, otherwise he'll give it up."),
  L("Λευτέρης", "m", "Έχεις δίκιο σε αυτό. Και το πιάνο; Ο ίδιος λέει ότι δεν θέλει να συνεχίσει.", "You're right about that. And the piano? He says himself he doesn't want to carry on."),
  L("Βάσω", "f", "Τότε ας σταματήσει το πιάνο φέτος και ας κάνει ποδόσφαιρο. Αν του λείψει η μουσική, το ξαναπιάνει του χρόνου.", "Then let him stop piano this year and do football. If he misses music, he can take it up again next year."),
  L("Λευτέρης", "m", "Εντάξει. Αλλά αν οι βαθμοί του πέσουν, το ξανασυζητάμε.", "OK. But if his marks drop, we'll discuss it again."),
 ],
 "questions": [
  Q("Γιατί ο Λευτέρης προτιμά το κολύμπι;", ["Γιατί είναι φθηνότερο", "Γιατί είναι δύο φορές την εβδομάδα και κάνει καλό στην πλάτη", "Γιατί το κάνουν οι φίλοι του Άγγελου", "Γιατί ο ίδιος ήταν κολυμβητής"], 1, "Είναι δύο φορές την εβδομάδα και κάνει καλό στην πλάτη του"),
  Q("Τι έγινε όταν ο Άγγελος πήγε κολύμπι πέρσι;", ["Βαριόταν αφάνταστα", "Κέρδισε έναν αγώνα", "Τραυματίστηκε", "Έκανε πολλούς φίλους"], 0, "βαριόταν αφάνταστα"),
  Q("Τι αποφασίζουν τελικά;", ["Να κάνει κολύμπι και πιάνο", "Να μην κάνει κανένα άθλημα φέτος", "Να σταματήσει το πιάνο φέτος και να κάνει ποδόσφαιρο", "Να κάνει ποδόσφαιρο και κολύμπι"], 2, "ας σταματήσει το πιάνο φέτος και ας κάνει ποδόσφαιρο"),
 ],
 "gloss": {"γραφτεί": "γράφομαι — to sign up, enrol", "προπονήσεις": "προπόνηση — training session", "ανασάνει": "ανασαίνω — to breathe", "αφάνταστα": "αφάνταστα — unimaginably", "παρατήσει": "παρατάω — to give up, quit", "ξαναπιάνει": "ξαναπιάνω — to take up again"}
})

ITEMS.append({
 "id": "l109-int-seismologos", "title": "Μια σεισμολόγος", "title_en": "A seismologist", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια σεισμολόγο σε μια εκπομπή για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αθανασίου, η Ελλάδα είναι από τις πιο σεισμογενείς χώρες της Ευρώπης. Πώς είναι η μέρα ενός σεισμολόγου;", "Mrs Athanasiou, Greece is one of the most earthquake-prone countries in Europe. What is a seismologist's day like?"),
  L("Σεισμολόγος", "f", "Τις περισσότερες μέρες είναι ήσυχη: αναλύουμε δεδομένα από τους σταθμούς που έχουμε σε όλη τη χώρα. Καταγράφουμε κάθε μέρα δεκάδες μικρούς σεισμούς, που δεν τους αισθάνεται κανείς. Όταν όμως γίνει ένας αισθητός σεισμός, το τηλέφωνο δεν σταματά να χτυπά.", "Most days are quiet: we analyse data from the stations we have all over the country. Every day we record dozens of small earthquakes that nobody feels. But when a noticeable earthquake happens, the phone doesn't stop ringing."),
  L("Δημοσιογράφος", "m", "Το ερώτημα που σας κάνουν όλοι είναι αν μπορούν να προβλεφθούν οι σεισμοί.", "The question everyone asks you is whether earthquakes can be predicted."),
  L("Σεισμολόγος", "f", "Η ειλικρινής απάντηση είναι όχι, τουλάχιστον όχι με ακρίβεια. Ξέρουμε ποιες περιοχές κινδυνεύουν περισσότερο, αλλά δεν μπορούμε να πούμε «την Τρίτη στις πέντε θα γίνει σεισμός». Όποιος το ισχυρίζεται, δεν λέει την αλήθεια.", "The honest answer is no, at least not precisely. We know which areas are most at risk, but we can't say 'on Tuesday at five there will be an earthquake'. Anyone who claims that is not telling the truth."),
  L("Δημοσιογράφος", "m", "Τι συμβουλεύετε λοιπόν τους πολίτες;", "So what do you advise citizens?"),
  L("Σεισμολόγος", "f", "Να είναι προετοιμασμένοι. Να στερεώσουν τις βαριές βιβλιοθήκες στον τοίχο, να έχουν ένα σακίδιο με νερό, φακό και φάρμακα, και να ξέρουν τι θα κάνουν: «σκύψε, καλύψου, κρατήσου». Η προετοιμασία σώζει ζωές περισσότερο από οποιαδήποτε πρόβλεψη.", "To be prepared. To fix heavy bookcases to the wall, to have a backpack with water, a torch and medicines, and to know what to do: 'drop, cover, hold on'. Preparation saves more lives than any prediction."),
 ],
 "questions": [
  Q("Πώς είναι οι περισσότερες μέρες της;", ["Πολύ αγχωτικές", "Ήσυχες, αναλύοντας δεδομένα από τους σταθμούς", "Γεμάτες ταξίδια", "Αφιερωμένες σε διαλέξεις"], 1, "Τις περισσότερες μέρες είναι ήσυχη"),
  Q("Τι απαντά για την πρόβλεψη των σεισμών;", ["Ότι δεν μπορούν να προβλεφθούν με ακρίβεια", "Ότι σύντομα θα είναι δυνατή", "Ότι γίνεται μόνο για μεγάλους σεισμούς", "Ότι τα ζώα τους προβλέπουν"], 0, "Η ειλικρινής απάντηση είναι όχι, τουλάχιστον όχι με ακρίβεια"),
  Q("Τι σώζει ζωές, κατά τη γνώμη της;", ["Οι νέοι σεισμογράφοι", "Η μετακόμιση σε ασφαλείς περιοχές", "Η προετοιμασία", "Οι εφαρμογές στο κινητό"], 2, "Η προετοιμασία σώζει ζωές περισσότερο από οποιαδήποτε πρόβλεψη"),
 ],
 "gloss": {"σεισμογενείς": "σεισμογενής — earthquake-prone", "δεδομένα": "δεδομένα — data", "αισθητός": "αισθητός — noticeable, felt", "ισχυρίζεται": "ισχυρίζομαι — to claim", "στερεώσουν": "στερεώνω — to fix, secure", "σακίδιο": "σακίδιο — backpack"}
})

ITEMS.append({
 "id": "l109-rep-topika-geumata", "title": "Σχολικά γεύματα με τοπικά προϊόντα", "title_en": "School meals with local produce", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για την εκπαίδευση.",
 "script": [
  L("Ρεπόρτερ", "f", "Στα δημοτικά σχολεία ενός δήμου της Κρήτης, το μεσημεριανό γεύμα μαγειρεύεται πλέον καθημερινά σε μια κεντρική κουζίνα, με προϊόντα από αγρότες της περιοχής: λαχανικά, όσπρια, ελαιόλαδο, τυρί και εποχικά φρούτα.", "In the primary schools of a municipality in Crete, the midday meal is now cooked every day in a central kitchen, with produce from local farmers: vegetables, pulses, olive oil, cheese and seasonal fruit."),
  L("Διατροφολόγος", "m", "Στην αρχή τα παιδιά άφηναν τα φασολάκια και τις φακές στο πιάτο. Αρχίσαμε λοιπόν να τα φέρνουμε στα χωράφια, να δουν πώς μεγαλώνουν τα λαχανικά, και να μαγειρεύουν μαζί μας μία φορά τον μήνα. Σήμερα το φαγητό που πετιέται έχει μειωθεί σχεδόν στο μισό.", "At first the children left the green beans and lentils on their plates. So we started taking them to the fields to see how vegetables grow, and to cook with us once a month. Today the amount of food thrown away has fallen by almost half."),
  L("Ρεπόρτερ", "f", "Το πρόγραμμα ωφελεί και την τοπική οικονομία, αφού είκοσι δύο παραγωγοί έχουν σταθερό εισόδημα όλο τον χρόνο. Το υπουργείο εξετάζει να το εφαρμόσει και σε άλλες περιοχές, αν και ορισμένοι δήμοι λένε ότι δεν έχουν τον χώρο για κεντρική κουζίνα.", "The scheme also benefits the local economy, since twenty-two producers have a steady income all year round. The ministry is considering applying it in other areas too, although some municipalities say they don't have the space for a central kitchen."),
 ],
 "questions": [
  Q("Πού μαγειρεύεται το φαγητό;", ["Σε κάθε σχολείο χωριστά", "Σε μια κεντρική κουζίνα", "Στα σπίτια των αγροτών", "Σε ένα εστιατόριο της πόλης"], 1, "μαγειρεύεται πλέον καθημερινά σε μια κεντρική κουζίνα"),
  Q("Τι έκαναν για να τρώνε τα παιδιά τα όσπρια και τα λαχανικά;", ["Πρόσθεσαν περισσότερο αλάτι", "Τα έφεραν στα χωράφια και μαγείρευαν μαζί τους μία φορά τον μήνα", "Τα τιμωρούσαν όταν άφηναν φαγητό", "Τα αντικατέστησαν με μακαρόνια"], 1, "Αρχίσαμε λοιπόν να τα φέρνουμε στα χωράφια"),
  Q("Ποια δυσκολία αναφέρουν ορισμένοι δήμοι;", ["Δεν έχουν αγρότες στην περιοχή", "Δεν έχουν χρήματα για τα προϊόντα", "Δεν έχουν τον χώρο για κεντρική κουζίνα", "Οι γονείς δεν συμφωνούν"], 2, "δεν έχουν τον χώρο για κεντρική κουζίνα"),
 ],
 "gloss": {"όσπρια": "όσπρια — pulses (beans, lentils, chickpeas)", "εποχικά": "εποχικός — seasonal", "κεντρική": "κεντρικός — central", "φακές": "φακές — lentils", "πετιέται": "πετιέμαι — to be thrown away", "παραγωγοί": "παραγωγός — producer"}
})

ITEMS.append({
 "id": "l109-rep-dentro-gia-kathe-moro", "title": "Ένα δέντρο για κάθε νέο μωρό", "title_en": "A tree for every newborn", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για το περιβάλλον.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε μια μικρή πόλη της Μακεδονίας, κάθε οικογένεια που αποκτά παιδί λαμβάνει από τον δήμο μια πρόσκληση: να φυτέψει ένα δέντρο στο νέο πάρκο της πόλης, με το όνομα του μωρού γραμμένο σε ένα μικρό ξύλινο ταμπελάκι.", "In a small town in Macedonia, every family that has a baby receives an invitation from the municipality: to plant a tree in the town's new park, with the baby's name written on a small wooden sign."),
  L("Δήμαρχος", "f", "Ξεκινήσαμε πριν από πέντε χρόνια, μετά από τη μεγάλη πυρκαγιά που έκαψε το δάσος πάνω από την πόλη. Θέλαμε να συνδέσουμε τη νέα ζωή με το πράσινο. Οι γονείς διαλέγουν ανάμεσα σε πλατάνια, βελανιδιές και κουτσουπιές, και αναλαμβάνουν να ποτίζουν το δέντρο τα δύο πρώτα καλοκαίρια.", "We started five years ago, after the big fire that burnt the forest above the town. We wanted to connect new life with greenery. Parents choose between plane trees, oaks and Judas trees, and take on watering the tree for the first two summers."),
  L("Ρεπόρτερ", "m", "Σήμερα στο πάρκο μεγαλώνουν πάνω από τετρακόσια δέντρα. Κάθε Απρίλιο γίνεται μια γιορτή όπου τα παιδιά μετρούν πόσο ψήλωσαν τα ίδια και πόσο ψήλωσαν τα δέντρα τους. Μερικές οικογένειες που μετακόμισαν σε άλλες πόλεις επιστρέφουν ειδικά γι' αυτή τη μέρα.", "Today over four hundred trees are growing in the park. Every April there's a celebration where the children measure how much they've grown and how much their trees have grown. Some families who moved to other towns come back specially for that day."),
 ],
 "questions": [
  Q("Τι έκανε τον δήμο να ξεκινήσει το πρόγραμμα;", ["Μια ευρωπαϊκή χρηματοδότηση", "Η μεγάλη πυρκαγιά που έκαψε το δάσος πάνω από την πόλη", "Η πρόταση ενός σχολείου", "Η αύξηση των γεννήσεων"], 1, "μετά από τη μεγάλη πυρκαγιά που έκαψε το δάσος πάνω από την πόλη"),
  Q("Τι αναλαμβάνουν οι γονείς;", ["Να ποτίζουν το δέντρο τα δύο πρώτα καλοκαίρια", "Να πληρώσουν το δέντρο", "Να καθαρίζουν το πάρκο", "Να φυτέψουν δύο δέντρα"], 0, "αναλαμβάνουν να ποτίζουν το δέντρο τα δύο πρώτα καλοκαίρια"),
  Q("Τι γίνεται κάθε Απρίλιο;", ["Φυτεύονται καινούργια δέντρα από τον δήμο", "Βραβεύεται το ψηλότερο δέντρο", "Μια γιορτή όπου τα παιδιά μετρούν πόσο ψήλωσαν τα ίδια και τα δέντρα τους", "Μια εκστρατεία καθαρισμού του δάσους"], 2, "Κάθε Απρίλιο γίνεται μια γιορτή"),
 ],
 "gloss": {"ταμπελάκι": "ταμπελάκι — small sign, label", "πυρκαγιά": "πυρκαγιά — fire, wildfire", "πλατάνια": "πλάτανος — plane tree", "βελανιδιές": "βελανιδιά — oak", "κουτσουπιές": "κουτσουπιά — Judas tree", "ψήλωσαν": "ψηλώνω — to grow taller"}
})

ITEMS.append({
 "id": "l109-mono-dimosia-omilia", "title": "Πώς έμαθα να μιλάω δημόσια", "title_en": "How I learned to speak in public", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν νέο άνθρωπο να μιλά σε μια εκπομπή για την προσωπική ανάπτυξη.",
 "script": [
  L("Θοδωρής", "m", "Στο σχολείο, όταν έπρεπε να παρουσιάσω μια εργασία μπροστά στην τάξη, έτρεμαν τα γόνατά μου και ξεχνούσα όλα όσα είχα ετοιμάσει. Στο πανεπιστήμιο έκανα ό,τι μπορούσα για να το αποφύγω. Όταν όμως πήρα την πρώτη μου δουλειά, η προϊσταμένη μου μού ζήτησε να παρουσιάζω κάθε μήνα τα αποτελέσματα της ομάδας.", "At school, when I had to present a project in front of the class, my knees shook and I forgot everything I'd prepared. At university I did everything I could to avoid it. But when I got my first job, my boss asked me to present the team's results every month."),
  L("Θοδωρής", "m", "Γράφτηκα σε μια ομάδα που συναντιέται κάθε Τετάρτη βράδυ σε ένα καφέ, όπου ο καθένας μιλάει για πέντε λεπτά σε ένα θέμα που του δίνουν επί τόπου. Οι άλλοι σημειώνουν τι πήγε καλά και τι όχι. Την πρώτη φορά μίλησα ενάμισι λεπτό και κάθισα κατακόκκινος.", "I joined a group that meets every Wednesday evening in a café, where everyone speaks for five minutes on a topic they're given on the spot. The others note what went well and what didn't. The first time I spoke for a minute and a half and sat down bright red."),
  L("Θοδωρής", "m", "Μετά από έναν χρόνο, ακόμα αγχώνομαι, αλλά έχω μάθει να χρησιμοποιώ το άγχος. Το πιο σημαντικό που έμαθα είναι ότι το κοινό δεν περιμένει να αποτύχεις· θέλει να πετύχεις. Τον περασμένο μήνα μίλησα σε ένα συνέδριο μπροστά σε διακόσια άτομα, και στο τέλος με χειροκρότησαν.", "After a year, I still get nervous, but I've learned to use the nerves. The most important thing I've learned is that the audience isn't waiting for you to fail; they want you to succeed. Last month I spoke at a conference in front of two hundred people, and at the end they applauded me."),
 ],
 "questions": [
  Q("Τι τον ανάγκασε να αντιμετωπίσει τον φόβο του;", ["Ένα μάθημα στο πανεπιστήμιο", "Η προϊσταμένη του τού ζήτησε να παρουσιάζει κάθε μήνα τα αποτελέσματα της ομάδας", "Ο γάμος ενός φίλου του", "Μια συνέντευξη για δουλειά"], 1, "η προϊσταμένη μου μού ζήτησε να παρουσιάζω κάθε μήνα τα αποτελέσματα της ομάδας"),
  Q("Τι γίνεται στην ομάδα της Τετάρτης;", ["Ο καθένας μιλάει πέντε λεπτά σε ένα θέμα που του δίνουν επί τόπου", "Παρακολουθούν βίντεο με διάσημους ομιλητές", "Γράφουν ομιλίες για άλλους", "Κάνουν μαθήματα θεάτρου"], 0, "ο καθένας μιλάει για πέντε λεπτά σε ένα θέμα που του δίνουν επί τόπου"),
  Q("Ποιο είναι το πιο σημαντικό που έμαθε;", ["Ότι το άγχος εξαφανίζεται με τον καιρό", "Ότι πρέπει να μαθαίνει την ομιλία απέξω", "Ότι το κοινό θέλει να πετύχεις", "Ότι οι σύντομες ομιλίες είναι καλύτερες"], 2, "το κοινό δεν περιμένει να αποτύχεις· θέλει να πετύχεις"),
 ],
 "gloss": {"γόνατά": "γόνατο — knee", "αποφύγω": "αποφεύγω — to avoid", "προϊσταμένη": "προϊσταμένη — boss, supervisor (f.)", "επί": "επί τόπου — on the spot", "κατακόκκινος": "κατακόκκινος — bright red", "συνέδριο": "συνέδριο — conference"}
})

ITEMS.append({
 "id": "l109-mono-podilato-sta-saranta", "title": "Έμαθα ποδήλατο στα σαράντα", "title_en": "I learned to ride a bike at forty", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλά σε μια ραδιοφωνική εκπομπή για όσα μαθαίνουμε αργά στη ζωή.",
 "script": [
  L("Ρούλα", "f", "Μεγάλωσα σε μια πολυκατοικία στο κέντρο της Αθήνας, χωρίς αυλή και με πολλή κίνηση στους δρόμους. Οι γονείς μου φοβούνταν και δεν μου αγόρασαν ποτέ ποδήλατο. Όταν μεγάλωσα, ντρεπόμουν να ομολογήσω ότι δεν ήξερα.", "I grew up in an apartment block in the centre of Athens, with no yard and lots of traffic in the streets. My parents were afraid and never bought me a bike. When I grew up, I was ashamed to admit that I couldn't ride."),
  L("Ρούλα", "f", "Πέρσι, η κόρη μου, που είναι επτά χρονών, έμαθε μέσα σε ένα απόγευμα. Με κοίταξε και μου είπε: «Μαμά, τώρα σειρά σου». Έτσι γράφτηκα σε ένα δωρεάν πρόγραμμα του δήμου για ενήλικες. Ήμασταν οχτώ άτομα, από είκοσι πέντε ως εξήντα οχτώ χρονών.", "Last year my daughter, who is seven, learned in one afternoon. She looked at me and said: 'Mum, now it's your turn.' So I signed up for a free municipal programme for adults. There were eight of us, aged from twenty-five to sixty-eight."),
  L("Ρούλα", "f", "Ο εκπαιδευτής μάς έβγαλε πρώτα τα πετάλια, για να μάθουμε να ισορροπούμε σπρώχνοντας με τα πόδια. Την τρίτη εβδομάδα έκανα τον πρώτο μου γύρο χωρίς να πέσω, και φώναζα σαν μικρό παιδί. Τώρα κάνουμε βόλτες με την κόρη μου κάθε Κυριακή στην παραλία.", "The instructor first took the pedals off, so that we'd learn to balance by pushing with our feet. In the third week I did my first lap without falling, and I was shouting like a little child. Now my daughter and I go for rides every Sunday on the seafront."),
 ],
 "questions": [
  Q("Γιατί δεν είχε μάθει ποδήλατο ως παιδί;", ["Γιατί δεν της άρεσε", "Γιατί οι γονείς της φοβούνταν και δεν της αγόρασαν ποτέ ποδήλατο", "Γιατί είχε ένα ατύχημα", "Γιατί ζούσε σε νησί"], 1, "Οι γονείς μου φοβούνταν και δεν μου αγόρασαν ποτέ ποδήλατο"),
  Q("Τι την έκανε να αποφασίσει να μάθει;", ["Της είπε η κόρη της ότι ήταν η σειρά της", "Ο γιατρός της", "Μια διαφήμιση του δήμου", "Ήθελε να πηγαίνει με ποδήλατο στη δουλειά"], 0, "«Μαμά, τώρα σειρά σου»"),
  Q("Πώς ξεκίνησε η εκπαίδευση;", ["Με βοηθητικές ρόδες", "Σε ένα στατικό ποδήλατο", "Χωρίς πετάλια, για να μάθουν να ισορροπούν", "Με βίντεο στο διαδίκτυο"], 2, "Ο εκπαιδευτής μάς έβγαλε πρώτα τα πετάλια"),
 ],
 "gloss": {"ντρεπόμουν": "ντρέπομαι — to be ashamed, embarrassed", "ομολογήσω": "ομολογώ — to admit", "σειρά": "σειρά — turn", "πετάλια": "πετάλι — pedal", "ισορροπούμε": "ισορροπώ — to balance", "γύρο": "γύρος — lap, round"}
})

ITEMS.append({
 "id": "l109-c1-fotorypansi", "title": "Γιατί οι πόλεις χρειάζονται σκοτάδι;", "title_en": "Why do cities need darkness?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για το περιβάλλον.",
 "script": [
  L("Παρουσιάστρια", "f", "Πότε είδατε τελευταία φορά τον Γαλαξία μας, εκείνη τη γαλακτερή λωρίδα που διασχίζει τον νυχτερινό ουρανό; Για πολλούς κατοίκους των πόλεων η απάντηση είναι «ποτέ». Σύμφωνα με μια διεθνή μελέτη του 2016, περίπου ένας στους τρεις ανθρώπους στον πλανήτη δεν μπορεί πια να τον δει από τον τόπο όπου ζει, εξαιτίας του τεχνητού φωτισμού.", "When did you last see our Galaxy, that milky band that crosses the night sky? For many city dwellers the answer is 'never'. According to an international study from 2016, roughly one in three people on the planet can no longer see it from where they live, because of artificial lighting."),
  L("Παρουσιάστρια", "f", "Η φωτορύπανση, όμως, δεν είναι μόνο αισθητικό ζήτημα. Πολλά αποδημητικά πουλιά ταξιδεύουν τη νύχτα και προσανατολίζονται με τα αστέρια· τα φωτισμένα κτίρια μπορεί να τα αποπροσανατολίσουν. Στις ελληνικές παραλίες, τα χελωνάκια της καρέτα, όταν βγαίνουν από τα αυγά, κατευθύνονται κανονικά προς τη φωτεινότερη πλευρά του ορίζοντα, δηλαδή τη θάλασσα. Αν πίσω από την παραλία υπάρχουν δυνατά φώτα, πηγαίνουν προς τη λάθος κατεύθυνση.", "Light pollution, however, is not only an aesthetic issue. Many migratory birds travel at night and navigate by the stars; lit-up buildings can disorient them. On Greek beaches, loggerhead hatchlings, when they emerge from their eggs, normally head towards the brightest side of the horizon, that is, the sea. If there are strong lights behind the beach, they go the wrong way."),
  L("Παρουσιάστρια", "f", "Οι λύσεις είναι συχνά απλές και φθηνές: φωτιστικά που ρίχνουν το φως προς τα κάτω και όχι προς τον ουρανό, θερμότερα χρώματα αντί για το έντονο λευκό φως, και χρονοδιακόπτες που σβήνουν τα φώτα όταν δεν χρειάζονται. Μερικές περιοχές στον κόσμο έχουν μάλιστα αναγνωριστεί ως «πάρκα σκοτεινού ουρανού». Δεν χρειάζεται να σβήσουμε τις πόλεις· χρειάζεται να φωτίζουμε μόνο ό,τι πρέπει, όσο πρέπει.", "The solutions are often simple and cheap: light fittings that direct light downwards and not towards the sky, warmer colours instead of harsh white light, and timers that switch lights off when they are not needed. Some areas of the world have even been recognised as 'dark sky parks'. We don't need to switch off our cities; we need to light only what is necessary, as much as is necessary."),
 ],
 "questions": [
  Q("Τι έδειξε, σύμφωνα με την παρουσιάστρια, η μελέτη του 2016;", ["Ότι ο Γαλαξίας φαίνεται από όλες τις πόλεις", "Ότι περίπου ένας στους τρεις ανθρώπους δεν μπορεί πια να δει τον Γαλαξία από τον τόπο όπου ζει", "Ότι ο τεχνητός φωτισμός μειώνεται", "Ότι τα αστέρια λιγοστεύουν"], 1, "περίπου ένας στους τρεις ανθρώπους στον πλανήτη δεν μπορεί πια να τον δει"),
  Q("Γιατί επηρεάζονται τα αποδημητικά πουλιά;", ["Γιατί ταξιδεύουν τη νύχτα και προσανατολίζονται με τα αστέρια", "Γιατί τα φώτα τα ζεσταίνουν", "Γιατί δεν βρίσκουν τροφή", "Γιατί φοβούνται τους ανθρώπους"], 0, "ταξιδεύουν τη νύχτα και προσανατολίζονται με τα αστέρια"),
  Q("Τι συμβαίνει στα χελωνάκια όταν υπάρχουν δυνατά φώτα πίσω από την παραλία;", ["Μένουν μέσα στα αυγά", "Κολυμπούν πιο γρήγορα", "Πηγαίνουν προς τη λάθος κατεύθυνση", "Κρύβονται στην άμμο"], 2, "πηγαίνουν προς τη λάθος κατεύθυνση"),
  Q("Ποια είναι η βασική πρόταση στο τέλος;", ["Να σβήσουμε εντελώς τα φώτα των πόλεων", "Να φωτίζουμε μόνο ό,τι πρέπει, όσο πρέπει", "Να χρησιμοποιούμε μόνο λευκό φως", "Να μετακομίσουμε στην ύπαιθρο"], 1, "χρειάζεται να φωτίζουμε μόνο ό,τι πρέπει, όσο πρέπει"),
 ],
 "gloss": {"γαλακτερή": "γαλακτερός — milky", "φωτορύπανση": "φωτορύπανση — light pollution", "αποδημητικά": "αποδημητικός — migratory", "προσανατολίζονται": "προσανατολίζομαι — to navigate, orient oneself", "αποπροσανατολίσουν": "αποπροσανατολίζω — to disorient", "φωτιστικά": "φωτιστικό — light fitting", "χρονοδιακόπτες": "χρονοδιακόπτης — timer switch"}
})

ITEMS.append({
 "id": "l109-c1-afantasia", "title": "Όταν το μυαλό δεν βλέπει εικόνες", "title_en": "When the mind sees no pictures", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια νευροψυχολόγο σε μια εκπομπή για τον εγκέφαλο.",
 "script": [
  L("Δημοσιογράφος", "m", "Αν σας ζητήσω να φανταστείτε ένα μήλο, οι περισσότεροι από εμάς «βλέπουμε» κάτι στο μυαλό μας. Υπάρχουν όμως άνθρωποι που δεν βλέπουν τίποτα;", "If I ask you to imagine an apple, most of us 'see' something in our mind. But are there people who see nothing?"),
  L("Νευροψυχολόγος", "f", "Ναι. Το φαινόμενο ονομάστηκε «αφαντασία» το 2015 από μια ομάδα Βρετανών ερευνητών. Οι άνθρωποι αυτοί ξέρουν πώς είναι ένα μήλο, μπορούν να το περιγράψουν με ακρίβεια, αλλά δεν σχηματίζουν καμία νοερή εικόνα. Οι εκτιμήσεις διαφέρουν, αλλά πιστεύεται ότι αφορά λίγα τοις εκατό του πληθυσμού.", "Yes. The phenomenon was named 'aphantasia' in 2015 by a team of British researchers. These people know what an apple looks like and can describe it accurately, but they form no mental image. Estimates vary, but it is thought to affect a few per cent of the population."),
  L("Δημοσιογράφος", "m", "Και το καταλαβαίνουν από μικροί;", "And do they realise it from childhood?"),
  L("Νευροψυχολόγος", "f", "Συνήθως όχι, και αυτό είναι το πιο εντυπωσιακό. Πολλοί το ανακαλύπτουν στην ενήλικη ζωή, συχνά τυχαία, σε μια συζήτηση. Νόμιζαν ότι η φράση «μέτρα προβατάκια για να κοιμηθείς» ήταν απλώς σχήμα λόγου, και ξαφνιάζονται όταν μαθαίνουν ότι οι άλλοι βλέπουν πραγματικά προβατάκια.", "Usually not, and that is the most striking thing. Many discover it in adult life, often by chance, in a conversation. They thought the phrase 'count sheep to fall asleep' was just a figure of speech, and are surprised to learn that others actually see sheep."),
  L("Δημοσιογράφος", "m", "Είναι πρόβλημα;", "Is it a problem?"),
  L("Νευροψυχολόγος", "f", "Δεν θεωρείται ασθένεια. Οι περισσότεροι ζουν κανονικά, και ανάμεσά τους υπάρχουν επιστήμονες, συγγραφείς, ακόμη και καλλιτέχνες. Ορισμένες μελέτες δείχνουν ότι μπορεί να θυμούνται λιγότερο ζωντανά προσωπικές τους αναμνήσεις, αλλά η έρευνα είναι ακόμη στην αρχή. Αυτό που μας διδάσκει κυρίως η αφαντασία είναι ότι ο εσωτερικός κόσμος του καθενός είναι πολύ πιο διαφορετικός από όσο νομίζαμε.", "It is not considered an illness. Most live normally, and among them there are scientists, writers, even artists. Some studies suggest they may remember their personal memories less vividly, but the research is still in its early stages. What aphantasia mainly teaches us is that each person's inner world is far more different than we thought."),
 ],
 "questions": [
  Q("Τι συμβαίνει στους ανθρώπους με αφαντασία;", ["Δεν ξέρουν πώς είναι ένα μήλο", "Μπορούν να περιγράψουν ένα αντικείμενο, αλλά δεν σχηματίζουν νοερή εικόνα", "Δεν μπορούν να ονειρευτούν", "Βλέπουν εικόνες μόνο με κλειστά μάτια"], 1, "δεν σχηματίζουν καμία νοερή εικόνα"),
  Q("Πότε ανακαλύπτουν συνήθως ότι έχουν αφαντασία;", ["Στην ενήλικη ζωή, συχνά τυχαία", "Στο νηπιαγωγείο", "Όταν πάνε σε οφθαλμίατρο", "Μετά από ένα ατύχημα"], 0, "Πολλοί το ανακαλύπτουν στην ενήλικη ζωή, συχνά τυχαία"),
  Q("Τι νόμιζαν για τη φράση «μέτρα προβατάκια»;", ["Ότι είναι παλιά παροιμία", "Ότι είναι αστείο για παιδιά", "Ότι ήταν απλώς σχήμα λόγου", "Ότι είναι ιατρική συμβουλή"], 2, "ήταν απλώς σχήμα λόγου"),
  Q("Τι λέει η νευροψυχολόγος για τις προσωπικές αναμνήσεις;", ["Ότι χάνονται εντελώς", "Ότι είναι πιο ζωντανές", "Ότι δεν επηρεάζονται καθόλου", "Ότι ορισμένες μελέτες δείχνουν ότι μπορεί να είναι λιγότερο ζωντανές, αλλά η έρευνα είναι στην αρχή"], 3, "η έρευνα είναι ακόμη στην αρχή"),
 ],
 "gloss": {"αφαντασία": "αφαντασία — aphantasia", "νοερή": "νοερός — mental, imagined", "πληθυσμού": "πληθυσμός — population", "σχήμα": "σχήμα λόγου — figure of speech", "ξαφνιάζονται": "ξαφνιάζομαι — to be surprised", "ζωντανά": "ζωντανά — vividly"}
})

rnd = random.Random(109)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-109.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
