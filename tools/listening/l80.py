# Source for library/listening/listening-80.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l80.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l80-ann-basket", "title": "Ανακοίνωση πριν από αγώνα μπάσκετ", "title_en": "Announcement before a basketball game", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα κλειστό γήπεδο μπάσκετ, λίγο πριν από την έναρξη ενός αγώνα. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνητής", "m", "Καλησπέρα σας και καλώς ήρθατε στο κλειστό γήπεδο. Ο σημερινός αγώνας ξεκινά στις οχτώ και μισή ακριβώς. Παρακαλούνται οι φίλαθλοι να καθίσουν στη θέση που αναγράφεται στο εισιτήριό τους και να μην στέκονται στους διαδρόμους των κερκίδων.", "Good evening and welcome to the indoor arena. Tonight's game starts at exactly half past eight. Fans are asked to sit in the seat printed on their ticket and not to stand in the aisles of the stands."),
  L("Εκφωνητής", "m", "Υπενθυμίζουμε ότι απαγορεύεται η ρίψη αντικειμένων στον αγωνιστικό χώρο, καθώς και η χρήση φωτοβολίδων. Κάθε παράβαση μπορεί να οδηγήσει σε τιμωρία της ομάδας και σε διεξαγωγή των επόμενων αγώνων χωρίς θεατές.", "We remind you that throwing objects onto the court is forbidden, as is the use of flares. Any violation may lead to the team being penalised and to the next games being played without spectators."),
  L("Εκφωνητής", "m", "Στο ημίχρονο θα γίνει κλήρωση για δύο φανέλες υπογεγραμμένες από τους παίκτες. Ο αριθμός που συμμετέχει στην κλήρωση είναι τυπωμένος στο πίσω μέρος του εισιτηρίου σας, οπότε μην το πετάξετε. Καλή διασκέδαση!", "At half-time there will be a draw for two shirts signed by the players. The number taking part in the draw is printed on the back of your ticket, so don't throw it away. Enjoy the game!"),
 ],
 "questions": [
  Q("Τι ζητείται από τους φιλάθλους;", ["Να έρθουν νωρίτερα", "Να καθίσουν στη θέση του εισιτηρίου τους", "Να μην φωνάζουν", "Να αγοράσουν φανέλες"], 1, "να καθίσουν στη θέση που αναγράφεται στο εισιτήριό τους"),
  Q("Ποια μπορεί να είναι η συνέπεια μιας παράβασης;", ["Η ακύρωση του εισιτηρίου", "Οι επόμενοι αγώνες να γίνουν χωρίς θεατές", "Η αλλαγή της ώρας του αγώνα", "Η αποβολή ενός παίκτη"], 1, "διεξαγωγή των επόμενων αγώνων χωρίς θεατές"),
  Q("Γιατί δεν πρέπει να πετάξουν το εισιτήριο;", ["Γιατί θα το ελέγξουν στην έξοδο", "Γιατί έχει τον αριθμό για την κλήρωση", "Γιατί ισχύει και για τον επόμενο αγώνα", "Γιατί δίνει έκπτωση στο κυλικείο"], 1, "Ο αριθμός που συμμετέχει στην κλήρωση είναι τυπωμένος στο πίσω μέρος του εισιτηρίου σας"),
 ],
 "gloss": {"κλειστό γήπεδο": "κλειστό γήπεδο — indoor arena", "φίλαθλοι": "φίλαθλος — sports fan", "αναγράφεται": "αναγράφομαι — to be printed, stated", "κερκίδων": "κερκίδα — stand (in a stadium)", "ρίψη": "ρίψη — throwing", "αγωνιστικό χώρο": "αγωνιστικός χώρος — court, pitch", "φωτοβολίδων": "φωτοβολίδα — flare", "παράβαση": "παράβαση — violation, offence", "ημίχρονο": "ημίχρονο — half-time", "κλήρωση": "κλήρωση — draw, raffle", "φανέλες": "φανέλα — (team) shirt, jersey"},
})
ITEMS.append({
 "id": "l80-vm-charaktiki", "title": "Μήνυμα από το εργαστήριο χαρακτικής", "title_en": "Voicemail from a printmaking workshop", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δηλώσει ενδιαφέρον για ένα μάθημα χαρακτικής. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Φωτεινή", "f", "Καλημέρα, είμαι η Φωτεινή από το εργαστήριο χαρακτικής στο Μεταξουργείο. Σας τηλεφωνώ για το μάθημα λινόλεουμ που ρωτήσατε. Ο κύκλος ξεκινά την Τετάρτη δεκαοχτώ του μήνα και διαρκεί οχτώ εβδομάδες, κάθε Τετάρτη από τις έξι μέχρι τις εννιά.", "Good morning, this is Foteini from the printmaking workshop in Metaxourgeio. I'm calling about the linocut class you asked about. The course starts on Wednesday the eighteenth and lasts eight weeks, every Wednesday from six to nine."),
  L("Φωτεινή", "f", "Τα βασικά υλικά, δηλαδή τα μελάνια, το χαρτί και τα κομμάτια λινόλεουμ, περιλαμβάνονται στην τιμή. Τα εργαλεία χάραξης, όμως, θα πρέπει να τα αγοράσετε μόνος σας. Μπορούμε να σας προτείνουμε ένα κατάστημα που κάνει έκπτωση στους μαθητές μας.", "The basic materials, that is the inks, the paper and the pieces of lino, are included in the price. The carving tools, though, you'll need to buy yourself. We can recommend a shop that gives our students a discount."),
  L("Φωτεινή", "f", "Οι θέσεις είναι μόνο οχτώ, γιατί έχουμε μία πρέσα, και έχουν μείνει δύο. Αν σας ενδιαφέρει, στείλτε μου ένα μήνυμα μέχρι την Παρασκευή. Καλό είναι να φοράτε ρούχα που δεν σας πειράζει να λερωθούν. Ευχαριστώ!", "There are only eight places, because we have one press, and two are left. If you're interested, send me a message by Friday. It's a good idea to wear clothes you don't mind getting dirty. Thank you!"),
 ],
 "questions": [
  Q("Πόσο διαρκεί ο κύκλος μαθημάτων;", ["Τέσσερις εβδομάδες", "Οχτώ εβδομάδες", "Δύο μήνες και μισό", "Ένα εξάμηνο"], 1, "διαρκεί οχτώ εβδομάδες"),
  Q("Τι δεν περιλαμβάνεται στην τιμή;", ["Τα μελάνια", "Τα εργαλεία χάραξης", "Το χαρτί", "Τα κομμάτια λινόλεουμ"], 1, "Τα εργαλεία χάραξης, όμως, θα πρέπει να τα αγοράσετε μόνος σας"),
  Q("Γιατί οι θέσεις είναι λίγες;", ["Γιατί η αίθουσα είναι μικρή", "Γιατί το εργαστήριο έχει μόνο μία πρέσα", "Γιατί υπάρχει μόνο μία δασκάλα", "Γιατί τα υλικά είναι ακριβά"], 1, "Οι θέσεις είναι μόνο οχτώ, γιατί έχουμε μία πρέσα"),
 ],
 "gloss": {"χαρακτικής": "χαρακτική — printmaking", "λινόλεουμ": "λινόλεουμ — lino, linoleum", "κύκλος": "κύκλος (μαθημάτων) — course, series of classes", "μελάνια": "μελάνι — ink", "εργαλεία χάραξης": "εργαλεία χάραξης — carving tools", "χάραξης": "χάραξη — carving, engraving", "πρέσα": "πρέσα — (printing) press", "λερωθούν": "λερώνομαι — to get dirty"},
})
ITEMS.append({
 "id": "l80-dia-trapezi", "title": "Το τραπέζι ήρθε χαραγμένο", "title_en": "The table arrived scratched", "type": "dialogue", "level": "B2",
 "context_el": "Μια πελάτισσα τηλεφωνεί στο κατάστημα επίπλων από το οποίο αγόρασε ένα τραπέζι. Θα ακούσετε τη συνομιλία της με έναν υπάλληλο.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Χθες μου παρέδωσαν ένα τραπέζι τραπεζαρίας που αγόρασα από εσάς, και όταν το ξετυλίξαμε είδαμε μια βαθιά χαρακιά στην επιφάνεια. Οι μεταφορείς είχαν ήδη φύγει.", "Good morning. Yesterday a dining table I bought from you was delivered, and when we unwrapped it we saw a deep scratch on the surface. The delivery men had already left."),
  L("Υπάλληλος", "m", "Λυπάμαι πολύ γι’ αυτό. Υπογράψατε το δελτίο παράδοσης χωρίς παρατηρήσεις;", "I'm very sorry about that. Did you sign the delivery note without any remarks?"),
  L("Πελάτισσα", "f", "Ναι, γιατί ήταν ακόμα τυλιγμένο στο νάιλον. Δεν μπορούσα να ξέρω.", "Yes, because it was still wrapped in plastic. I couldn't have known."),
  L("Υπάλληλος", "m", "Καταλαβαίνω. Στείλτε μας, παρακαλώ, φωτογραφίες της ζημιάς και της συσκευασίας μέσα σε σαράντα οχτώ ώρες από την παράδοση, στο email που υπάρχει στην απόδειξη. Χωρίς φωτογραφίες ο κατασκευαστής δεν δέχεται την αντικατάσταση.", "I understand. Please send us photos of the damage and of the packaging within forty-eight hours of delivery, to the email on the receipt. Without photos the manufacturer won't accept a replacement."),
  L("Πελάτισσα", "f", "Και μετά; Θα πρέπει να περιμένω πολύ;", "And then? Will I have to wait long?"),
  L("Υπάλληλος", "m", "Αν το ίδιο μοντέλο υπάρχει στην αποθήκη, θα σας φέρουμε καινούργιο μέσα σε μία εβδομάδα και θα πάρουμε το χαλασμένο. Αν δεν υπάρχει, μπορείτε να διαλέξετε άλλο ή να πάρετε πίσω τα χρήματά σας.", "If the same model is in the warehouse, we'll bring you a new one within a week and take away the damaged one. If not, you can choose another or get your money back."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με το τραπέζι;", ["Του λείπει ένα πόδι", "Έχει μια βαθιά χαρακιά", "Είναι λάθος χρώμα", "Είναι μικρότερο απ’ ό,τι παρήγγειλε"], 1, "είδαμε μια βαθιά χαρακιά στην επιφάνεια"),
  Q("Γιατί υπέγραψε το δελτίο χωρίς παρατηρήσεις;", ["Γιατί βιαζόταν", "Γιατί το τραπέζι ήταν ακόμα τυλιγμένο", "Γιατί δεν είχε στυλό", "Γιατί οι μεταφορείς επέμεναν"], 1, "ήταν ακόμα τυλιγμένο στο νάιλον"),
  Q("Τι πρέπει να κάνει μέσα σε σαράντα οχτώ ώρες;", ["Να επιστρέψει το τραπέζι", "Να στείλει φωτογραφίες της ζημιάς και της συσκευασίας", "Να πάει στο κατάστημα", "Να πληρώσει τα μεταφορικά"], 1, "Στείλτε μας, παρακαλώ, φωτογραφίες της ζημιάς και της συσκευασίας μέσα σε σαράντα οχτώ ώρες"),
 ],
 "gloss": {"επίπλων": "έπιπλο — piece of furniture", "τραπεζαρίας": "τραπεζαρία — dining room", "ξετυλίξαμε": "ξετυλίγω — to unwrap", "χαρακιά": "χαρακιά — scratch, score mark", "μεταφορείς": "μεταφορέας — removal/delivery man", "δελτίο παράδοσης": "δελτίο παράδοσης — delivery note", "παρατηρήσεις": "παρατήρηση — remark, note", "τυλιγμένο": "τυλιγμένος — wrapped", "συσκευασίας": "συσκευασία — packaging", "αντικατάσταση": "αντικατάσταση — replacement"},
})
ITEMS.append({
 "id": "l80-int-geranos", "title": "Χειρίστρια γερανού στο λιμάνι", "title_en": "A crane operator at the port", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για ασυνήθιστα επαγγέλματα, η δημοσιογράφος μιλά με τη Δέσποινα, που δουλεύει ως χειρίστρια γερανού στο λιμάνι του Πειραιά.",
 "script": [
  L("Δημοσιογράφος", "f", "Δέσποινα, πώς βρεθήκατε στην καμπίνα ενός γερανού;", "Despina, how did you end up in the cab of a crane?"),
  L("Δέσποινα", "f", "Τελείως τυχαία. Δούλευα στα γραφεία της εταιρείας, στο τμήμα προγραμματισμού, και έβλεπα κάθε μέρα από το παράθυρο τους γερανούς να φορτώνουν κοντέινερ. Όταν άνοιξε μια εκπαίδευση για χειριστές, έκανα αίτηση σχεδόν για πλάκα. Ήμουν η μόνη γυναίκα στην τάξη.", "Completely by chance. I worked in the company's offices, in the planning department, and every day I watched the cranes loading containers from the window. When a training course for operators opened, I applied almost as a joke. I was the only woman in the class."),
  L("Δημοσιογράφος", "f", "Τι είναι το πιο δύσκολο στη δουλειά σας;", "What is the hardest thing about your job?"),
  L("Δέσποινα", "f", "Η συγκέντρωση. Κάθεσαι σαράντα μέτρα πάνω από το έδαφος και σηκώνεις κοντέινερ που ζυγίζουν μέχρι τριάντα τόνους. Ένα λάθος λίγων εκατοστών μπορεί να προκαλέσει ζημιά ή, ακόμα χειρότερα, ατύχημα. Γι’ αυτό δουλεύουμε σε βάρδιες και κάνουμε διάλειμμα κάθε δύο ώρες.", "Concentration. You sit forty metres above the ground and lift containers weighing up to thirty tonnes. A mistake of a few centimetres can cause damage or, even worse, an accident. That's why we work in shifts and take a break every two hours."),
  L("Δημοσιογράφος", "f", "Και ο αέρας;", "And the wind?"),
  L("Δέσποινα", "f", "Ο αέρας είναι ο μεγαλύτερος εχθρός μας. Όταν ξεπεράσει ένα όριο, σταματάμε τη δουλειά, όσο κι αν βιάζεται το πλοίο. Αλλά να σας πω την αλήθεια, όταν η μέρα είναι καθαρή και βλέπεις από ψηλά όλο τον Σαρωνικό, νιώθεις ότι έχεις την καλύτερη θέα της Αθήνας.", "The wind is our biggest enemy. When it goes over a limit, we stop work, however much of a hurry the ship is in. But to tell you the truth, when the day is clear and you see the whole Saronic Gulf from above, you feel you have the best view in Athens."),
 ],
 "questions": [
  Q("Πού δούλευε η Δέσποινα πριν γίνει χειρίστρια;", ["Σε ένα πλοίο", "Στα γραφεία της εταιρείας", "Σε ένα εργοτάξιο", "Σε μια τράπεζα"], 1, "Δούλευα στα γραφεία της εταιρείας, στο τμήμα προγραμματισμού"),
  Q("Γιατί κάνουν διάλειμμα κάθε δύο ώρες;", ["Γιατί το λέει ο νόμος για τον θόρυβο", "Γιατί η δουλειά απαιτεί μεγάλη συγκέντρωση", "Γιατί αλλάζουν τα πλοία", "Γιατί κάνει πολλή ζέστη"], 1, "Ένα λάθος λίγων εκατοστών μπορεί να προκαλέσει ζημιά"),
  Q("Τι γίνεται όταν ο αέρας ξεπεράσει ένα όριο;", ["Δουλεύουν πιο αργά", "Σταματούν τη δουλειά", "Φορτώνουν μόνο άδεια κοντέινερ", "Καλούν δεύτερο χειριστή"], 1, "Όταν ξεπεράσει ένα όριο, σταματάμε τη δουλειά"),
 ],
 "gloss": {"χειρίστρια": "χειρίστρια / χειριστής — operator", "γερανού": "γερανός — crane", "καμπίνα": "καμπίνα — cab, cabin", "τμήμα προγραμματισμού": "τμήμα προγραμματισμού — planning department", "φορτώνουν": "φορτώνω — to load", "για πλάκα": "για πλάκα — as a joke, for fun", "συγκέντρωση": "συγκέντρωση — concentration", "τόνους": "τόνος — tonne", "βάρδιες": "βάρδια — shift", "Σαρωνικό": "Σαρωνικός — the Saronic Gulf"},
})
ITEMS.append({
 "id": "l80-rep-foloi", "title": "Το δρυοδάσος της Φολόης", "title_en": "The oak forest of Foloi", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για το δρυοδάσος της Φολόης σε μια ραδιοφωνική εκπομπή για τη φύση της Πελοποννήσου.",
 "script": [
  L("Ρεπόρτερ", "m", "Λίγα χιλιόμετρα από την Αρχαία Ολυμπία, σε ένα οροπέδιο της Ηλείας, απλώνεται το δάσος της Φολόης, ένα από τα μεγαλύτερα δάση με βελανιδιές στη νότια Ελλάδα. Εδώ τα δέντρα δεν είναι πυκνά, όπως σε ένα έλατο δάσος: στέκονται σε απόσταση το ένα από το άλλο, και ανάμεσά τους απλώνονται λιβάδια.", "A few kilometres from Ancient Olympia, on a plateau in Ilia, stretches the forest of Foloi, one of the largest oak forests in southern Greece. Here the trees are not dense, as in a fir forest: they stand at a distance from one another, and meadows spread out between them."),
  L("Ρεπόρτερ", "m", "Για αιώνες οι κάτοικοι των γύρω χωριών έβοσκαν εδώ τα ζώα τους και μάζευαν τα βελανίδια, που χρησιμοποιούνταν ως τροφή για τα γουρούνια αλλά και για τη βυρσοδεψία. Σήμερα η κτηνοτροφία έχει περιοριστεί, και οι ντόπιοι ελπίζουν σε έναν ήπιο τουρισμό, με πεζοπορία, ποδήλατο και ιππασία.", "For centuries the inhabitants of the surrounding villages grazed their animals here and gathered the acorns, which were used as food for pigs and also for tanning. Today livestock farming has declined, and the locals are hoping for gentle tourism, with hiking, cycling and horse riding."),
  L("Ρεπόρτερ", "m", "Η μεγαλύτερη απειλή για το δάσος είναι η φωτιά. Το καλοκαίρι του 2007, οι μεγάλες πυρκαγιές της Ηλείας έφτασαν πολύ κοντά. Από τότε, ομάδες εθελοντών κάνουν περιπολίες κάθε καλοκαίρι, ενώ το δασαρχείο καθαρίζει τα ξερά χόρτα γύρω από τους δρόμους.", "The greatest threat to the forest is fire. In the summer of 2007, the great fires of Ilia came very close. Since then, volunteer groups patrol every summer, while the forestry office clears the dry grass along the roads."),
 ],
 "questions": [
  Q("Τι ξεχωρίζει το δάσος της Φολόης από ένα δάσος με έλατα;", ["Τα δέντρα είναι πολύ ψηλότερα", "Τα δέντρα απέχουν μεταξύ τους και ανάμεσά τους υπάρχουν λιβάδια", "Δεν έχει καθόλου μονοπάτια", "Είναι πάντα πράσινο"], 1, "στέκονται σε απόσταση το ένα από το άλλο, και ανάμεσά τους απλώνονται λιβάδια"),
  Q("Σε τι χρησιμοποιούνταν τα βελανίδια;", ["Μόνο στη μαγειρική", "Ως τροφή για τα γουρούνια και στη βυρσοδεψία", "Για την παραγωγή λαδιού", "Ως καύσιμο"], 1, "ως τροφή για τα γουρούνια αλλά και για τη βυρσοδεψία"),
  Q("Τι κάνουν οι εθελοντές κάθε καλοκαίρι;", ["Φυτεύουν δέντρα", "Κάνουν περιπολίες", "Μαζεύουν βελανίδια", "Οργανώνουν ξεναγήσεις"], 1, "ομάδες εθελοντών κάνουν περιπολίες κάθε καλοκαίρι"),
 ],
 "gloss": {"δρυοδάσος": "δρυοδάσος — oak forest", "οροπέδιο": "οροπέδιο — plateau", "βελανιδιές": "βελανιδιά — oak tree", "έλατο": "έλατο — fir", "λιβάδια": "λιβάδι — meadow", "έβοσκαν": "βόσκω — to graze", "βελανίδια": "βελανίδι — acorn", "βυρσοδεψία": "βυρσοδεψία — tanning (of leather)", "κτηνοτροφία": "κτηνοτροφία — livestock farming", "περιπολίες": "περιπολία — patrol", "δασαρχείο": "δασαρχείο — forestry office"},
})
ITEMS.append({
 "id": "l80-rep-nestos-kano", "title": "Με κανό στα στενά του Νέστου", "title_en": "By canoe through the Nestos gorge", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ταξιδιωτικό ρεπορτάζ από τη Βόρεια Ελλάδα.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρισκόμαστε στο χωριό Γαλάνη, ανάμεσα στην Ξάνθη και την Καβάλα, στο σημείο απ’ όπου ξεκινούν οι διαδρομές με κανό στα στενά του Νέστου. Το ποτάμι εδώ κάνει μαιάνδρους μέσα σε ένα βαθύ φαράγγι, με πλατάνια και βράχια που υψώνονται και από τις δύο πλευρές.", "We're in the village of Galani, between Xanthi and Kavala, at the point where canoe routes through the Nestos gorge begin. Here the river meanders through a deep gorge, with plane trees and rocks rising on both sides."),
  L("Ρεπόρτερ", "f", "Η διαδρομή διαρκεί περίπου τρεις ώρες και, σύμφωνα με τους οδηγούς, είναι κατάλληλη και για αρχάριους, γιατί το νερό κυλά ήρεμα τους περισσότερους μήνες. Πριν μπουν στο νερό, όλοι παίρνουν σωσίβιο και κράνος και κάνουν ένα σύντομο μάθημα κουπιού στην όχθη.", "The route takes about three hours and, according to the guides, is suitable even for beginners, because the water flows calmly most months. Before getting into the water, everyone is given a life jacket and helmet and has a short paddling lesson on the bank."),
  L("Ρεπόρτερ", "f", "Υπάρχει όμως μια ιδιαιτερότητα: η ροή του Νέστου εξαρτάται από τα φράγματα που βρίσκονται πιο πάνω. Όταν ανοίγουν οι θυρίδες, η στάθμη μπορεί να ανέβει γρήγορα. Γι’ αυτό οι εταιρείες επικοινωνούν κάθε πρωί με τη διοίκηση του φράγματος πριν αποφασίσουν αν θα γίνει η κατάβαση.", "There is one peculiarity, though: the flow of the Nestos depends on the dams further upstream. When the gates open, the water level can rise quickly. That's why the companies contact the dam management every morning before deciding whether the descent will go ahead."),
 ],
 "questions": [
  Q("Γιατί η διαδρομή είναι κατάλληλη και για αρχάριους;", ["Γιατί είναι πολύ σύντομη", "Γιατί το νερό κυλά ήρεμα τους περισσότερους μήνες", "Γιατί δεν χρειάζεται κουπί", "Γιατί γίνεται μόνο το καλοκαίρι"], 1, "το νερό κυλά ήρεμα τους περισσότερους μήνες"),
  Q("Τι κάνουν όλοι πριν μπουν στο νερό;", ["Υπογράφουν ένα συμβόλαιο", "Παίρνουν σωσίβιο και κράνος και κάνουν σύντομο μάθημα", "Κολυμπούν στο ποτάμι", "Περπατούν μέχρι το φράγμα"], 1, "όλοι παίρνουν σωσίβιο και κράνος και κάνουν ένα σύντομο μάθημα κουπιού"),
  Q("Γιατί οι εταιρείες επικοινωνούν κάθε πρωί με τη διοίκηση του φράγματος;", ["Για να πληρώσουν ένα τέλος", "Γιατί η στάθμη μπορεί να ανέβει γρήγορα όταν ανοίγουν οι θυρίδες", "Για να κλείσουν τον δρόμο", "Για να ζητήσουν περισσότερο νερό"], 1, "Όταν ανοίγουν οι θυρίδες, η στάθμη μπορεί να ανέβει γρήγορα"),
 ],
 "gloss": {"κανό": "κανό — canoe", "στενά": "στενά — gorge, narrows", "μαιάνδρους": "μαίανδρος — meander", "φαράγγι": "φαράγγι — gorge", "πλατάνια": "πλάτανος — plane tree", "σωσίβιο": "σωσίβιο — life jacket", "κράνος": "κράνος — helmet", "κουπιού": "κουπί — paddle, oar", "όχθη": "όχθη — (river) bank", "φράγματα": "φράγμα — dam", "θυρίδες": "θυρίδα — sluice gate", "στάθμη": "στάθμη — (water) level", "κατάβαση": "κατάβαση — descent"},
})
ITEMS.append({
 "id": "l80-mono-tango", "title": "Ταγκό στα εξήντα", "title_en": "Tango at sixty", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για όσους αλλάζουν τη ζωή τους μετά τη σύνταξη, ο Στέλιος μιλά για το πώς άρχισε να χορεύει ταγκό.",
 "script": [
  L("Στέλιος", "m", "Όταν πέθανε η γυναίκα μου, πέρασα έναν χρόνο σχεδόν κλεισμένος στο σπίτι. Η κόρη μου ανησυχούσε και μια μέρα μού έφερε ένα φυλλάδιο από μια σχολή ταγκό στην Κυψέλη. «Δεν χρειάζεται να έχεις παρτενέρ», μου είπε. «Εκεί αλλάζουν συνέχεια.» Πήγα μόνο και μόνο για να μην τη στενοχωρήσω.", "When my wife died, I spent a year almost shut up at home. My daughter was worried, and one day she brought me a leaflet from a tango school in Kypseli. 'You don't need a partner,' she told me. 'They change all the time there.' I went only so as not to upset her."),
  L("Στέλιος", "m", "Το πρώτο μάθημα ήταν καταστροφή. Πατούσα συνέχεια τις ντάμες μου και δεν καταλάβαινα πότε έπρεπε να περιμένω. Η δασκάλα μού είπε κάτι που δεν θα ξεχάσω: «Στο ταγκό το πιο σημαντικό βήμα είναι η παύση.» Χρειάστηκα μήνες για να καταλάβω τι εννοούσε.", "The first lesson was a disaster. I kept stepping on my partners' feet and didn't understand when I was supposed to wait. The teacher told me something I won't forget: 'In tango the most important step is the pause.' It took me months to understand what she meant."),
  L("Στέλιος", "m", "Τώρα πηγαίνω δύο φορές την εβδομάδα, και τα Σάββατα σε μια μιλόνγκα, δηλαδή μια βραδιά όπου χορεύει όποιος θέλει. Δεν έγινα σπουδαίος χορευτής. Αλλά ξαναβρήκα κάτι που νόμιζα ότι είχα χάσει: τη χαρά να περιμένω κάτι μέσα στη βδομάδα.", "Now I go twice a week, and on Saturdays to a milonga, that is, an evening where anyone who wants can dance. I didn't become a great dancer. But I found again something I thought I had lost: the joy of looking forward to something during the week."),
 ],
 "questions": [
  Q("Γιατί πήγε ο Στέλιος στο πρώτο μάθημα;", ["Γιατί πάντα ήθελε να μάθει ταγκό", "Για να μην στενοχωρήσει την κόρη του", "Γιατί του το πρότεινε ο γιατρός", "Γιατί η σχολή ήταν δίπλα στο σπίτι του"], 1, "Πήγα μόνο και μόνο για να μην τη στενοχωρήσω"),
  Q("Τι του είπε η δασκάλα;", ["Ότι χρειάζεται μόνιμη παρτενέρ", "Ότι το πιο σημαντικό βήμα είναι η παύση", "Ότι είναι πολύ μεγάλος για ταγκό", "Ότι πρέπει να κάνει ιδιαίτερα μαθήματα"], 1, "Στο ταγκό το πιο σημαντικό βήμα είναι η παύση"),
  Q("Τι λέει ότι ξαναβρήκε;", ["Τους παλιούς του φίλους", "Τη χαρά να περιμένει κάτι μέσα στη βδομάδα", "Την υγεία του", "Την αγάπη για τη μουσική"], 1, "τη χαρά να περιμένω κάτι μέσα στη βδομάδα"),
 ],
 "gloss": {"σύνταξη": "σύνταξη — retirement, pension", "κλεισμένος": "κλεισμένος — shut in", "φυλλάδιο": "φυλλάδιο — leaflet", "παρτενέρ": "παρτενέρ — (dance) partner", "στενοχωρήσω": "στενοχωρώ — to upset", "ντάμες": "ντάμα — (dance) partner (female)", "παύση": "παύση — pause", "μιλόνγκα": "μιλόνγκα — milonga (tango social evening)"},
})
ITEMS.append({
 "id": "l80-mono-eisitiria", "title": "Το κουτί με τα παλιά εισιτήρια", "title_en": "The box of old tickets", "type": "monologue", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, οι ακροατές μιλούν για αντικείμενα που φυλάνε. Ακούτε τη Βάσω.",
 "script": [
  L("Βάσω", "f", "Από τότε που ήμουν φοιτήτρια, κρατάω κάθε εισιτήριο: τρένου, πλοίου, κινηματογράφου, συναυλιών. Τα ρίχνω σε ένα παλιό κουτί από μπισκότα που ήταν της γιαγιάς μου. Έχουν περάσει τριάντα χρόνια, και το κουτί έχει γεμίσει τόσο που δεν κλείνει πια.", "Since I was a student, I've kept every ticket: train, ferry, cinema, concerts. I throw them into an old biscuit tin that belonged to my grandmother. Thirty years have passed, and the tin is so full that it doesn't close any more."),
  L("Βάσω", "f", "Κάθε χρόνο, την Πρωτοχρονιά, το αδειάζω στο τραπέζι και τα ξαναδιαβάζω. Ένα εισιτήριο πλοίου για την Ικαρία μού θυμίζει το καλοκαίρι που γνώρισα τον άντρα μου. Ένα εισιτήριο από μια συναυλία που ακυρώθηκε λόγω βροχής μού θυμίζει ότι και οι αποτυχημένες βραδιές έχουν τη θέση τους.", "Every year, on New Year's Day, I empty it onto the table and read them again. A ferry ticket to Ikaria reminds me of the summer I met my husband. A ticket from a concert that was cancelled because of rain reminds me that failed evenings have their place too."),
  L("Βάσω", "f", "Το πρόβλημα είναι ότι πια τα περισσότερα εισιτήρια είναι ηλεκτρονικά. Τα αποθηκεύω στο κινητό, αλλά δεν είναι το ίδιο. Ένα αρχείο δεν ξεθωριάζει, δεν τσαλακώνεται, δεν μυρίζει τίποτα. Γι’ αυτό, όταν μπορώ, ζητάω ακόμα να μου το τυπώσουν.", "The problem is that most tickets are electronic now. I save them on my phone, but it's not the same. A file doesn't fade, doesn't get crumpled, doesn't smell of anything. That's why, when I can, I still ask for it to be printed for me."),
 ],
 "questions": [
  Q("Πού φυλάει η Βάσω τα εισιτήρια;", ["Σε ένα άλμπουμ", "Σε ένα παλιό κουτί από μπισκότα", "Σε ένα συρτάρι του γραφείου", "Σε έναν φάκελο"], 1, "Τα ρίχνω σε ένα παλιό κουτί από μπισκότα που ήταν της γιαγιάς μου"),
  Q("Πότε τα ξαναδιαβάζει;", ["Στα γενέθλιά της", "Την Πρωτοχρονιά", "Κάθε καλοκαίρι", "Όταν μετακομίζει"], 1, "Κάθε χρόνο, την Πρωτοχρονιά, το αδειάζω στο τραπέζι"),
  Q("Γιατί ζητάει ακόμα να της τυπώνουν τα εισιτήρια;", ["Γιατί δεν έχει κινητό", "Γιατί ένα ηλεκτρονικό αρχείο δεν είναι το ίδιο", "Γιατί είναι φθηνότερα", "Γιατί το απαιτεί ο νόμος"], 1, "Τα αποθηκεύω στο κινητό, αλλά δεν είναι το ίδιο"),
 ],
 "gloss": {"φυλάνε": "φυλάω — to keep", "κουτί": "κουτί — box, tin", "μπισκότα": "μπισκότο — biscuit", "Πρωτοχρονιά": "Πρωτοχρονιά — New Year's Day", "αδειάζω": "αδειάζω — to empty", "ακυρώθηκε": "ακυρώνομαι — to be cancelled", "ξεθωριάζει": "ξεθωριάζω — to fade", "τσαλακώνεται": "τσαλακώνομαι — to get crumpled"},
})
ITEMS.append({
 "id": "l80-c1-oures", "title": "Η επιστήμη των ουρών αναμονής", "title_en": "The science of queues", "type": "interview", "level": "C1",
 "context_el": "Σε μια επιστημονική εκπομπή, ο δημοσιογράφος συζητά με μια καθηγήτρια επιχειρησιακής έρευνας για τις ουρές αναμονής.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία καθηγήτρια, γιατί μας φαίνεται πάντα ότι η διπλανή ουρά στο σούπερ μάρκετ προχωρά πιο γρήγορα;", "Professor, why does it always seem to us that the queue next to ours at the supermarket is moving faster?"),
  L("Καθηγήτρια", "f", "Εν μέρει είναι θέμα πιθανοτήτων. Αν υπάρχουν τρία ταμεία, οι πιθανότητες να είναι η δική σας ουρά η πιο γρήγορη είναι μία στις τρεις. Άρα, τις περισσότερες φορές, κάποια άλλη θα κινείται πιο γρήγορα. Επιπλέον, θυμόμαστε πολύ πιο έντονα τις φορές που χάσαμε απ’ ό,τι εκείνες που κερδίσαμε.", "Partly it's a question of probability. If there are three tills, the chances of your queue being the fastest are one in three. So, most of the time, some other one will be moving faster. Moreover, we remember the times we lost much more vividly than those we won."),
  L("Δημοσιογράφος", "m", "Υπάρχει πιο δίκαιο σύστημα;", "Is there a fairer system?"),
  L("Καθηγήτρια", "f", "Η μία κοινή ουρά που τροφοδοτεί πολλά ταμεία, όπως στις τράπεζες ή στα ταχυδρομεία, είναι κατά μέσο όρο πιο αποτελεσματική και, κυρίως, πιο δίκαιη: κανείς δεν προσπερνά κανέναν επειδή διάλεξε τυχερά. Παραδόξως, όμως, οι πελάτες συχνά την αποφεύγουν, γιατί μια μακριά ουρά μοιάζει τρομακτική, ακόμα κι αν κινείται γρηγορότερα.", "A single shared queue feeding several tills, as in banks or post offices, is on average more efficient and, above all, fairer: nobody overtakes anybody because they chose luckily. Paradoxically, though, customers often avoid it, because a long queue looks daunting, even if it moves faster."),
  L("Δημοσιογράφος", "m", "Και η ψυχολογία της αναμονής;", "And the psychology of waiting?"),
  L("Καθηγήτρια", "f", "Αυτή είναι ίσως πιο σημαντική από τα μαθηματικά. Η αβέβαιη αναμονή φαίνεται μεγαλύτερη από τη γνωστή, γι’ αυτό οι πινακίδες που δείχνουν τον υπολειπόμενο χρόνο μειώνουν τον εκνευρισμό. Και η άπραγη αναμονή φαίνεται ατελείωτη. Δεν είναι τυχαίο ότι σε πολλά αεροδρόμια οι διάδρομοι μέχρι την παραλαβή αποσκευών είναι επίτηδες μακριοί: όσο περπατάς, δεν περιμένεις.", "That is perhaps more important than the mathematics. Uncertain waiting seems longer than known waiting, which is why signs showing the remaining time reduce irritation. And idle waiting seems endless. It's no accident that in many airports the corridors to baggage claim are deliberately long: while you're walking, you're not waiting."),
 ],
 "questions": [
  Q("Πώς εξηγεί η καθηγήτρια την εντύπωση ότι η διπλανή ουρά είναι πάντα πιο γρήγορη;", ["Οι ταμίες δουλεύουν με διαφορετικό ρυθμό", "Με τις πιθανότητες και με το ότι θυμόμαστε πιο έντονα τις φορές που χάσαμε", "Οι πελάτες διαλέγουν πάντα τη χειρότερη ουρά", "Τα σούπερ μάρκετ το κάνουν επίτηδες"], 1, "θυμόμαστε πολύ πιο έντονα τις φορές που χάσαμε απ’ ό,τι εκείνες που κερδίσαμε"),
  Q("Γιατί οι πελάτες συχνά αποφεύγουν τη μία κοινή ουρά;", ["Γιατί είναι πραγματικά πιο αργή", "Γιατί μια μακριά ουρά μοιάζει τρομακτική", "Γιατί δεν τη γνωρίζουν", "Γιατί δεν επιτρέπει να διαλέξουν ταμία"], 1, "μια μακριά ουρά μοιάζει τρομακτική, ακόμα κι αν κινείται γρηγορότερα"),
  Q("Γιατί σε πολλά αεροδρόμια οι διάδρομοι μέχρι τις αποσκευές είναι μακριοί;", ["Για λόγους ασφαλείας", "Γιατί όσο περπατάς δεν νιώθεις ότι περιμένεις", "Για να περάσουν οι επιβάτες από τα καταστήματα", "Λόγω κακού σχεδιασμού"], 1, "όσο περπατάς, δεν περιμένεις"),
 ],
 "gloss": {"ουρές αναμονής": "ουρά αναμονής — queue", "επιχειρησιακής έρευνας": "επιχειρησιακή έρευνα — operations research", "ταμεία": "ταμείο — till, checkout", "πιθανοτήτων": "πιθανότητα — probability, chance", "τροφοδοτεί": "τροφοδοτώ — to feed, supply", "αποτελεσματική": "αποτελεσματικός — efficient", "προσπερνά": "προσπερνώ — to overtake", "υπολειπόμενο": "υπολειπόμενος — remaining", "εκνευρισμό": "εκνευρισμός — irritation", "άπραγη": "άπραγος — idle, inactive", "παραλαβή αποσκευών": "παραλαβή αποσκευών — baggage claim", "επίτηδες": "επίτηδες — on purpose"},
})
ITEMS.append({
 "id": "l80-c1-nevmata", "title": "Ένα νεύμα για το «όχι»: η γλώσσα του κεφαλιού", "title_en": "A nod for 'no': the language of the head", "type": "monologue", "level": "C1",
 "context_el": "Σε μια διάλεξη για τη μη λεκτική επικοινωνία, μια γλωσσολόγος μιλά για τις κινήσεις του κεφαλιού στην Ελλάδα.",
 "script": [
  L("Γλωσσολόγος", "f", "Οι ξένοι που επισκέπτονται την Ελλάδα μπερδεύονται συχνά με ένα απλό νεύμα: όταν ένας Έλληνας θέλει να πει «όχι», συχνά δεν κουνάει το κεφάλι δεξιά αριστερά, αλλά το γέρνει ελαφρά προς τα πίσω, σηκώνοντας τα φρύδια, και καμιά φορά συνοδεύει την κίνηση με ένα «τσου» της γλώσσας. Για κάποιον που δεν το ξέρει, η κίνηση μοιάζει ύποπτα με ένα «ναι».", "Foreigners visiting Greece are often confused by a simple gesture: when a Greek wants to say 'no', he often doesn't shake his head from side to side, but tilts it slightly back, raising his eyebrows, and sometimes accompanies the movement with a 'tsk' of the tongue. To someone who doesn't know it, the movement looks suspiciously like a 'yes'."),
  L("Γλωσσολόγος", "f", "Το νεύμα αυτό δεν είναι αποκλειστικά ελληνικό. Το συναντάμε σε ένα μεγάλο τόξο γύρω από την ανατολική Μεσόγειο, από τη νότια Ιταλία ως την Τουρκία και τη Βουλγαρία. Ορισμένοι ερευνητές το συνδέουν με τις περιοχές όπου μιλήθηκαν τα ελληνικά στην αρχαιότητα, αλλά πρόκειται για υπόθεση, όχι για αποδεδειγμένο γεγονός.", "This gesture is not exclusively Greek. We find it in a large arc around the eastern Mediterranean, from southern Italy to Turkey and Bulgaria. Some researchers link it to the areas where Greek was spoken in antiquity, but this is a hypothesis, not a proven fact."),
  L("Γλωσσολόγος", "f", "Αυτό που μας δείχνει το παράδειγμα είναι ότι ακόμα και οι πιο «αυτονόητες» κινήσεις του σώματος είναι μαθημένες, όχι έμφυτες. Γι’ αυτό, όταν μαθαίνουμε μια ξένη γλώσσα, δεν αρκεί να μάθουμε λέξεις. Πρέπει να μάθουμε και να διαβάζουμε τα σώματα των ανθρώπων, αλλιώς κινδυνεύουμε να καταλάβουμε το ακριβώς αντίθετο από αυτό που μας λένε.", "What the example shows us is that even the most 'self-evident' movements of the body are learned, not innate. That's why, when we learn a foreign language, it isn't enough to learn words. We also have to learn to read people's bodies, otherwise we risk understanding exactly the opposite of what we're being told."),
 ],
 "questions": [
  Q("Πώς λένε συχνά «όχι» οι Έλληνες με το κεφάλι;", ["Κουνώντας το δεξιά αριστερά", "Γέρνοντάς το ελαφρά προς τα πίσω και σηκώνοντας τα φρύδια", "Γέρνοντάς το προς τα κάτω", "Γυρίζοντάς το προς τα πλάγια"], 1, "το γέρνει ελαφρά προς τα πίσω, σηκώνοντας τα φρύδια"),
  Q("Τι λέει η γλωσσολόγος για την προέλευση του νεύματος;", ["Είναι αποδεδειγμένα αρχαιοελληνικό", "Η σύνδεση με την αρχαία ελληνική γλώσσα είναι υπόθεση", "Ήρθε από την Ιταλία", "Είναι πολύ πρόσφατο"], 1, "πρόκειται για υπόθεση, όχι για αποδεδειγμένο γεγονός"),
  Q("Ποιο είναι το γενικό συμπέρασμα της ομιλήτριας;", ["Οι κινήσεις του σώματος είναι ίδιες παντού", "Οι κινήσεις του σώματος είναι μαθημένες, και πρέπει να μαθαίνουμε να τις διαβάζουμε", "Οι λέξεις είναι πιο σημαντικές από τις κινήσεις", "Οι Έλληνες δεν χρησιμοποιούν νεύματα"], 1, "ακόμα και οι πιο «αυτονόητες» κινήσεις του σώματος είναι μαθημένες, όχι έμφυτες"),
 ],
 "gloss": {"νεύμα": "νεύμα — nod, gesture of the head", "μη λεκτική επικοινωνία": "μη λεκτική επικοινωνία — non-verbal communication", "μπερδεύονται": "μπερδεύομαι — to get confused", "γέρνει": "γέρνω — to tilt, lean", "φρύδια": "φρύδι — eyebrow", "ύποπτα": "ύποπτα — suspiciously", "τόξο": "τόξο — arc", "υπόθεση": "υπόθεση — hypothesis", "αυτονόητες": "αυτονόητος — self-evident", "έμφυτες": "έμφυτος — innate"},
})

rnd = random.Random(80)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-80.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
