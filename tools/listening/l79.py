# Source for library/listening/listening-79.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l79.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l79-ann-dimoprasia", "title": "Ανακοίνωση σε δημοπρασία έργων τέχνης", "title_en": "Announcement at an art auction", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε έναν οίκο δημοπρασιών στην Αθήνα, λίγο πριν αρχίσει μια δημοπρασία έργων τέχνης. Θα ακούσετε μια ανακοίνωση.",
 "script": [
  L("Υπεύθυνη", "f", "Καλησπέρα σας και καλώς ήρθατε στη σημερινή δημοπρασία. Παρακαλούμε όσους δεν έχουν πάρει ακόμα πινακίδα με αριθμό να περάσουν από το γραφείο εγγραφών, στα αριστερά της εισόδου. Χωρίς πινακίδα δεν είναι δυνατή η συμμετοχή στην πλειοδοσία.", "Good evening and welcome to today's auction. Will those who have not yet taken a numbered paddle please go to the registration desk, to the left of the entrance. Without a paddle it is not possible to take part in the bidding."),
  L("Υπεύθυνη", "f", "Σας υπενθυμίζουμε ότι στην τιμή κατακύρωσης προστίθεται προμήθεια του οίκου, είκοσι τοις εκατό, καθώς και ο αντίστοιχος ΦΠΑ. Στη δημοπρασία συμμετέχουν και πλειοδότες μέσω τηλεφώνου και διαδικτύου, οπότε μπορεί να υπάρξουν σύντομες παύσεις ανάμεσα στις προσφορές.", "We remind you that the house's commission, twenty per cent, plus the applicable VAT, is added to the hammer price. Bidders by telephone and online are also taking part in the auction, so there may be short pauses between bids."),
  L("Υπεύθυνη", "f", "Η πληρωμή γίνεται μέσα σε επτά ημέρες, και τα έργα παραλαμβάνονται από την αποθήκη μας μόνο μετά την εξόφληση. Παρακαλούμε να θέσετε τα κινητά σας σε αθόρυβη λειτουργία. Η δημοπρασία ξεκινά σε πέντε λεπτά.", "Payment is made within seven days, and works are collected from our warehouse only after full payment. Please put your mobile phones on silent. The auction starts in five minutes."),
 ],
 "questions": [
  Q("Τι χρειάζεται κάποιος για να πάρει μέρος στην πλειοδοσία;", ["Μια πρόσκληση", "Μια πινακίδα με αριθμό", "Ένα εισιτήριο", "Μια κάρτα μέλους"], 1, "Χωρίς πινακίδα δεν είναι δυνατή η συμμετοχή στην πλειοδοσία"),
  Q("Τι προστίθεται στην τιμή κατακύρωσης;", ["Μόνο ο ΦΠΑ", "Προμήθεια είκοσι τοις εκατό και ΦΠΑ", "Τα έξοδα μεταφοράς", "Τίποτα"], 1, "προστίθεται προμήθεια του οίκου, είκοσι τοις εκατό, καθώς και ο αντίστοιχος ΦΠΑ"),
  Q("Πότε μπορούν να παραλάβουν τα έργα οι αγοραστές;", ["Αμέσως μετά τη δημοπρασία", "Μόνο μετά την εξόφληση", "Μετά από ένα μήνα", "Την επόμενη μέρα"], 1, "τα έργα παραλαμβάνονται από την αποθήκη μας μόνο μετά την εξόφληση"),
 ],
 "gloss": {"δημοπρασία": "δημοπρασία — auction", "οίκο δημοπρασιών": "οίκος δημοπρασιών — auction house", "πινακίδα": "πινακίδα — (bidding) paddle, sign", "εγγραφών": "εγγραφή — registration", "πλειοδοσία": "πλειοδοσία — bidding", "τιμή κατακύρωσης": "τιμή κατακύρωσης — hammer price", "προμήθεια": "προμήθεια — commission", "πλειοδότες": "πλειοδότης — bidder", "εξόφληση": "εξόφληση — full payment", "αθόρυβη λειτουργία": "αθόρυβη λειτουργία — silent mode"},
})

ITEMS.append({
 "id": "l79-vm-xenonas-katoikidion", "title": "Μήνυμα από τον ξενώνα κατοικιδίων", "title_en": "Message from the pet hotel", "type": "voicemail", "level": "B2",
 "context_el": "Θα λείψετε δέκα μέρες για διακοπές και έχετε κλείσει θέση για τον σκύλο σας σε έναν ξενώνα κατοικιδίων. Θα ακούσετε ένα μήνυμα που σας άφησαν.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, από τον ξενώνα κατοικιδίων «Φιλόζωος» σας παίρνω, για την κράτηση του Ρεξ από τις δώδεκα μέχρι τις είκοσι δύο Αυγούστου. Η θέση είναι επιβεβαιωμένη. Χρειαζόμαστε όμως το βιβλιάριο υγείας του, για να δούμε ότι έχει κάνει όλα τα εμβόλια, και ειδικά της λύσσας και του βήχα του κυνοτροφείου.", "Good morning, I'm calling from the Filozoos pet hotel, about Rex's booking from the twelfth to the twenty-second of August. The place is confirmed. But we need his health booklet, to check he's had all his vaccinations, especially rabies and kennel cough."),
  L("Υπάλληλος", "m", "Αν τρώει ειδική τροφή, φέρτε τη δική του για όλες τις μέρες, γιατί η απότομη αλλαγή φαγητού συχνά τους πειράζει το στομάχι. Μπορείτε να φέρετε και ένα παιχνίδι ή μια κουβέρτα με τη μυρωδιά του σπιτιού· βοηθάει πολύ τα πρώτα βράδια.", "If he eats special food, bring his own for all the days, because a sudden change of food often upsets their stomach. You can also bring a toy or a blanket that smells of home; it helps a lot on the first nights."),
  L("Υπάλληλος", "m", "Για να κλειδώσει η κράτηση, παρακαλούμε να καταθέσετε προκαταβολή πενήντα ευρώ μέχρι την Παρασκευή. Θα σας στείλω τα στοιχεία του λογαριασμού με μήνυμα. Ευχαριστώ!", "To secure the booking, please pay a deposit of fifty euros by Friday. I'll send you the account details by text. Thank you!"),
 ],
 "questions": [
  Q("Γιατί χρειάζεται ο ξενώνας το βιβλιάριο υγείας;", ["Για να δει την ηλικία του σκύλου", "Για να ελέγξει ότι ο σκύλος έχει κάνει όλα τα εμβόλια", "Για να βρει τον κτηνίατρο", "Για να υπολογίσει την τιμή"], 1, "για να δούμε ότι έχει κάνει όλα τα εμβόλια"),
  Q("Γιατί πρέπει να φέρουν τη δική του τροφή;", ["Γιατί ο ξενώνας δεν δίνει φαγητό", "Γιατί η απότομη αλλαγή φαγητού συχνά πειράζει το στομάχι", "Γιατί είναι φθηνότερο", "Γιατί ο σκύλος είναι άρρωστος"], 1, "η απότομη αλλαγή φαγητού συχνά τους πειράζει το στομάχι"),
  Q("Τι πρέπει να γίνει μέχρι την Παρασκευή;", ["Να φέρουν τον σκύλο", "Να καταθέσουν προκαταβολή πενήντα ευρώ", "Να στείλουν φωτογραφία", "Να ακυρώσουν την κράτηση"], 1, "να καταθέσετε προκαταβολή πενήντα ευρώ μέχρι την Παρασκευή"),
 ],
 "gloss": {"ξενώνα κατοικιδίων": "ξενώνας κατοικιδίων — pet hotel, boarding kennel", "επιβεβαιωμένη": "επιβεβαιωμένος — confirmed", "βιβλιάριο υγείας": "βιβλιάριο υγείας — health booklet", "εμβόλια": "εμβόλιο — vaccine, vaccination", "λύσσας": "λύσσα — rabies", "βήχα του κυνοτροφείου": "βήχας του κυνοτροφείου — kennel cough", "τροφή": "τροφή — (pet) food", "πειράζει": "πειράζω — to upset, disagree with", "κουβέρτα": "κουβέρτα — blanket", "προκαταβολή": "προκαταβολή — deposit"},
})

ITEMS.append({
 "id": "l79-dia-epistrofi-dorou", "title": "Επιστροφή ενός δώρου", "title_en": "Returning a present", "type": "dialogue", "level": "B2",
 "context_el": "Μια πελάτισσα πηγαίνει σε ένα κατάστημα ρούχων για να αλλάξει ένα πουλόβερ που της έκαναν δώρο.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Μου έκαναν δώρο αυτό το πουλόβερ για τη γιορτή μου, αλλά μου είναι μικρό. Θα ήθελα να το αλλάξω, αν γίνεται, με ένα μεγαλύτερο νούμερο.", "Good morning. I was given this jumper as a present for my name day, but it's too small for me. I'd like to exchange it, if possible, for a bigger size."),
  L("Πωλητής", "m", "Βεβαίως. Έχετε την απόδειξη ή μια απόδειξη δώρου;", "Of course. Do you have the receipt or a gift receipt?"),
  L("Πελάτισσα", "f", "Όχι, δυστυχώς. Το καρτελάκι όμως είναι ακόμα πάνω, και δεν το έχω φορέσει καθόλου. Δεν θέλω να ρωτήσω τη θεία μου πόσο το πλήρωσε, θα ήταν λίγο άβολο.", "No, unfortunately. But the tag is still on, and I haven't worn it at all. I don't want to ask my aunt how much she paid for it, it'd be a bit awkward."),
  L("Πωλητής", "m", "Καταλαβαίνω. Χωρίς απόδειξη δεν μπορούμε να σας επιστρέψουμε χρήματα, αλλά αλλαγή γίνεται, αφού το προϊόν είναι δικό μας και σε άριστη κατάσταση. Το μεγαλύτερο νούμερο σε αυτό το χρώμα, όμως, έχει τελειώσει. Αν δεν σας αρέσει κάποιο άλλο χρώμα, μπορώ να σας δώσω ένα πιστωτικό σημείωμα, που ισχύει για έξι μήνες.", "I understand. Without a receipt we can't give you a refund, but an exchange is possible, since the product is ours and in perfect condition. The bigger size in this colour, though, has sold out. If you don't like another colour, I can give you a credit note, valid for six months."),
  L("Πελάτισσα", "f", "Το γκρι είναι ωραίο, θα πάρω αυτό. Και να μη μάθει ποτέ η θεία μου ότι το άλλαξα!", "The grey is nice, I'll take that. And my aunt must never find out I exchanged it!"),
 ],
 "questions": [
  Q("Γιατί θέλει η πελάτισσα να αλλάξει το πουλόβερ;", ["Δεν της αρέσει το χρώμα", "Της είναι μικρό", "Έχει ένα ελάττωμα", "Έχει ήδη ένα ίδιο"], 1, "μου είναι μικρό"),
  Q("Γιατί δεν μπορεί να πάρει πίσω χρήματα;", ["Γιατί το έχει φορέσει", "Γιατί δεν έχει απόδειξη", "Γιατί ήταν σε έκπτωση", "Γιατί πέρασαν πολλές μέρες"], 1, "Χωρίς απόδειξη δεν μπορούμε να σας επιστρέψουμε χρήματα"),
  Q("Τι αποφασίζει τελικά η πελάτισσα;", ["Να πάρει πιστωτικό σημείωμα", "Να πάρει το πουλόβερ σε γκρι χρώμα", "Να κρατήσει το μικρό πουλόβερ", "Να ρωτήσει τη θεία της"], 1, "Το γκρι είναι ωραίο, θα πάρω αυτό"),
 ],
 "gloss": {"πουλόβερ": "πουλόβερ — jumper, sweater", "γιορτή": "γιορτή — name day", "νούμερο": "νούμερο — size", "απόδειξη δώρου": "απόδειξη δώρου — gift receipt", "καρτελάκι": "καρτελάκι — (price) tag", "άβολο": "άβολος — awkward", "άριστη κατάσταση": "άριστη κατάσταση — perfect condition", "έχει τελειώσει": "τελειώνω — to run out, sell out", "πιστωτικό σημείωμα": "πιστωτικό σημείωμα — credit note", "ισχύει": "ισχύω — to be valid"},
})

ITEMS.append({
 "id": "l79-int-gefsignostria", "title": "Η γευσιγνώστρια ελαιολάδου", "title_en": "The olive oil taster", "type": "interview", "level": "B2",
 "context_el": "Σε μια εκπομπή για τη γεωργία μιλά μια γευσιγνώστρια ελαιολάδου.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς δοκιμάζει κανείς επαγγελματικά το ελαιόλαδο; Με ψωμί;", "How do you taste olive oil professionally? With bread?"),
  L("Γευσιγνώστρια", "f", "Όχι, το ψωμί αλλοιώνει τη γεύση. Βάζουμε λίγο λάδι σε ένα μικρό μπλε ποτήρι, για να μη μας επηρεάζει το χρώμα, και το ζεσταίνουμε με την παλάμη. Πρώτα το μυρίζουμε, μετά παίρνουμε μια γουλιά και ρουφάμε αέρα από τα πλάγια του στόματος, για να απλωθούν τα αρώματα.", "No, bread alters the taste. We put a little oil in a small blue glass, so the colour doesn't influence us, and warm it in our palm. First we smell it, then we take a sip and suck in air at the sides of the mouth, so the aromas spread."),
  L("Δημοσιογράφος", "m", "Και τι ψάχνετε;", "And what are you looking for?"),
  L("Γευσιγνώστρια", "f", "Τρία θετικά χαρακτηριστικά: το φρουτώδες, το πικρό και το πικάντικο, εκείνο το τσίμπημα στον λαιμό που σε κάνει να βήξεις. Πολλοί καταναλωτές νομίζουν ότι η πικράδα είναι ελάττωμα, ενώ στην πραγματικότητα δείχνει φρέσκο λάδι, πλούσιο σε αντιοξειδωτικά. Ελαττώματα είναι, για παράδειγμα, η μυρωδιά μούχλας ή ταγκίλας.", "Three positive characteristics: fruitiness, bitterness and pungency, that tickle in the throat that makes you cough. Many consumers think bitterness is a defect, whereas in fact it shows fresh oil, rich in antioxidants. Defects are, for example, a smell of mould or rancidness."),
 ],
 "questions": [
  Q("Γιατί δοκιμάζουν το λάδι σε μπλε ποτήρι;", ["Γιατί είναι πιο φτηνό", "Για να μην τους επηρεάζει το χρώμα", "Για να μένει ζεστό", "Γιατί είναι παράδοση"], 1, "για να μη μας επηρεάζει το χρώμα"),
  Q("Ποια από τα παρακάτω είναι θετικά χαρακτηριστικά;", ["Η μούχλα και η ταγκίλα", "Το φρουτώδες, το πικρό και το πικάντικο", "Το γλυκό και το αλμυρό", "Το πυκνό και το σκούρο χρώμα"], 1, "το φρουτώδες, το πικρό και το πικάντικο"),
  Q("Τι δείχνει, κατά τη γευσιγνώστρια, η πικράδα;", ["Ότι το λάδι είναι παλιό", "Φρέσκο λάδι, πλούσιο σε αντιοξειδωτικά", "Ότι το λάδι έχει χαλάσει", "Ότι το λάδι είναι ανακατεμένο"], 1, "δείχνει φρέσκο λάδι, πλούσιο σε αντιοξειδωτικά"),
 ],
 "gloss": {"γευσιγνώστρια": "γευσιγνώστρια — taster (woman)", "αλλοιώνει": "αλλοιώνω — to alter, spoil", "παλάμη": "παλάμη — palm (of the hand)", "γουλιά": "γουλιά — sip", "ρουφάμε": "ρουφάω — to suck in, slurp", "φρουτώδες": "φρουτώδης — fruity", "πικάντικο": "πικάντικος — pungent, spicy", "τσίμπημα": "τσίμπημα — sting, tickle", "αντιοξειδωτικά": "αντιοξειδωτικό — antioxidant", "μούχλας": "μούχλα — mould", "ταγκίλας": "ταγκίλα — rancidness"},
})

ITEMS.append({
 "id": "l79-rep-kri-kri", "title": "Το κρι-κρι, το αγρίμι της Κρήτης", "title_en": "The kri-kri, Crete's wild goat", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για ένα σπάνιο ζώο της Κρήτης.",
 "script": [
  L("Ρεπόρτερ", "m", "Αν περπατήσετε νωρίς το πρωί στο φαράγγι της Σαμαριάς, με λίγη τύχη θα δείτε ένα κρι-κρι να στέκεται ακίνητο πάνω σε έναν βράχο που μοιάζει αδύνατο να τον πατήσει κανείς. Οι Κρητικοί το λένε απλώς «αγρίμι». Είναι ένα άγριο κατσίκι με μακριά, κυρτά κέρατα, που ζει σχεδόν αποκλειστικά στα Λευκά Όρη.", "If you walk early in the morning in the Samaria gorge, with a little luck you'll see a kri-kri standing motionless on a rock it seems impossible for anyone to step on. Cretans simply call it 'agrimi'. It's a wild goat with long, curved horns that lives almost exclusively in the White Mountains."),
  L("Ρεπόρτερ", "m", "Πριν από μερικές δεκαετίες, το κρι-κρι κινδύνευε σοβαρά με εξαφάνιση, κυρίως λόγω του κυνηγιού. Για να το προστατέψουν, οι αρχές μετέφεραν ορισμένα ζώα σε μικρά ακατοίκητα νησάκια, όπως η Δία, κοντά στο Ηράκλειο, όπου δεν είχαν εχθρούς. Σήμερα το κυνήγι του απαγορεύεται αυστηρά.", "A few decades ago, the kri-kri was in serious danger of extinction, mainly because of hunting. To protect it, the authorities moved some animals to small uninhabited islets, such as Dia, near Heraklion, where they had no enemies. Today hunting it is strictly banned."),
  L("Ρεπόρτερ", "m", "Ένας νέος κίνδυνος, όμως, είναι η διασταύρωση με τις κατσίκες των βοσκών, που απειλεί την καθαρότητα του είδους. Οι επιστήμονες παρακολουθούν τους πληθυσμούς με κάμερες και δείγματα γενετικού υλικού. Για τους Κρητικούς, πάντως, το αγρίμι παραμένει σύμβολο λεβεντιάς και ελευθερίας, και εμφανίζεται σε αμέτρητες μαντινάδες.", "A new danger, however, is cross-breeding with shepherds' goats, which threatens the purity of the species. Scientists monitor the populations with cameras and samples of genetic material. For Cretans, in any case, the agrimi remains a symbol of gallantry and freedom, and appears in countless mantinades."),
 ],
 "questions": [
  Q("Πού ζει κυρίως το κρι-κρι;", ["Σε όλη την Ελλάδα", "Στα Λευκά Όρη της Κρήτης", "Στις παραλίες της Κρήτης", "Στα νησιά του Ιονίου"], 1, "ζει σχεδόν αποκλειστικά στα Λευκά Όρη"),
  Q("Γιατί μετέφεραν κάποια ζώα σε μικρά νησάκια;", ["Για να τα δουν οι τουρίστες", "Για να τα προστατέψουν, γιατί εκεί δεν είχαν εχθρούς", "Γιατί δεν είχαν τροφή στο βουνό", "Για επιστημονικά πειράματα"], 1, "Για να το προστατέψουν, οι αρχές μετέφεραν ορισμένα ζώα σε μικρά ακατοίκητα νησάκια"),
  Q("Ποιος είναι ο νέος κίνδυνος για το είδος;", ["Το κυνήγι", "Η διασταύρωση με τις κατσίκες των βοσκών", "Οι πυρκαγιές", "Ο τουρισμός"], 1, "η διασταύρωση με τις κατσίκες των βοσκών"),
 ],
 "gloss": {"αγρίμι": "αγρίμι — wild goat (Cretan name of the kri-kri); wild animal", "φαράγγι": "φαράγγι — gorge", "ακίνητο": "ακίνητος — motionless", "κυρτά": "κυρτός — curved", "κέρατα": "κέρατο — horn", "εξαφάνιση": "εξαφάνιση — extinction, disappearance", "ακατοίκητα": "ακατοίκητος — uninhabited", "διασταύρωση": "διασταύρωση — cross-breeding", "βοσκών": "βοσκός — shepherd", "λεβεντιάς": "λεβεντιά — gallantry, manliness", "μαντινάδες": "μαντινάδα — Cretan rhyming couplet"},
})

ITEMS.append({
 "id": "l79-rep-neromyloi", "title": "Οι νερόμυλοι του χωριού", "title_en": "The village watermills", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για την αναστήλωση των παλιών νερόμυλων σε ένα χωριό της Ηπείρου.",
 "script": [
  L("Ρεπόρτερ", "f", "Κατά μήκος του ποταμού, κάτω από τα πλατάνια, στέκονται ακόμα τα ερείπια επτά πέτρινων νερόμυλων. Μέχρι τη δεκαετία του πενήντα, εδώ άλεθαν το σιτάρι και το καλαμπόκι όλα τα χωριά της περιοχής. Οι αγρότες έφερναν τα σακιά με τα μουλάρια και περίμεναν συχνά ολόκληρη μέρα τη σειρά τους.", "Along the river, under the plane trees, the ruins of seven stone watermills still stand. Until the fifties, all the villages of the area ground their wheat and maize here. Farmers brought the sacks on mules and often waited a whole day for their turn."),
  L("Ρεπόρτερ", "f", "Ο μηχανισμός ήταν απλός και έξυπνος. Το νερό έπεφτε από ψηλά μέσα από ένα στενό ξύλινο κανάλι και γύριζε μια οριζόντια φτερωτή, που κινούσε την πάνω μυλόπετρα. Ο μυλωνάς δεν πληρωνόταν σε χρήματα· κρατούσε ένα μέρος από το αλεύρι ως αμοιβή.", "The mechanism was simple and clever. The water fell from a height through a narrow wooden channel and turned a horizontal wheel, which drove the upper millstone. The miller wasn't paid in money; he kept part of the flour as his fee."),
  L("Ρεπόρτερ", "f", "Με την έλευση των ηλεκτρικών μύλων, οι νερόμυλοι εγκαταλείφθηκαν. Τώρα ένας σύλλογος απόδημων χωριανών, με τη βοήθεια ενός ευρωπαϊκού προγράμματος, αναστήλωσε τον πρώτο. Από το καλοκαίρι, οι επισκέπτες θα μπορούν να τον δουν να λειτουργεί και να αγοράσουν αλεύρι αλεσμένο όπως παλιά.", "With the arrival of electric mills, the watermills were abandoned. Now an association of villagers living away from the village, with the help of a European programme, has restored the first one. From the summer, visitors will be able to see it working and buy flour ground the old way."),
 ],
 "questions": [
  Q("Τι άλεθαν στους νερόμυλους;", ["Ελιές", "Σιτάρι και καλαμπόκι", "Καφέ", "Αλάτι"], 1, "άλεθαν το σιτάρι και το καλαμπόκι"),
  Q("Πώς πληρωνόταν ο μυλωνάς;", ["Με χρήματα", "Κρατούσε ένα μέρος από το αλεύρι", "Με ζώα", "Δεν πληρωνόταν καθόλου"], 1, "κρατούσε ένα μέρος από το αλεύρι ως αμοιβή"),
  Q("Ποιος αναστήλωσε τον πρώτο νερόμυλο;", ["Ο δήμος", "Ένας σύλλογος απόδημων χωριανών με τη βοήθεια ευρωπαϊκού προγράμματος", "Ένας ιδιώτης επιχειρηματίας", "Το Υπουργείο Πολιτισμού"], 1, "ένας σύλλογος απόδημων χωριανών, με τη βοήθεια ενός ευρωπαϊκού προγράμματος"),
 ],
 "gloss": {"νερόμυλων": "νερόμυλος — watermill", "αναστήλωση": "αναστήλωση — restoration", "άλεθαν": "αλέθω — to grind, mill", "καλαμπόκι": "καλαμπόκι — maize, corn", "σακιά": "σακί — sack", "φτερωτή": "φτερωτή — (water) wheel, impeller", "μυλόπετρα": "μυλόπετρα — millstone", "μυλωνάς": "μυλωνάς — miller", "έλευση": "έλευση — arrival, advent", "απόδημων": "απόδημος — living away from one's birthplace, emigrant"},
})

ITEMS.append({
 "id": "l79-mono-syntaxi", "title": "Η πρώτη μου χρονιά στη σύνταξη", "title_en": "My first year of retirement", "type": "monologue", "level": "B2",
 "context_el": "Ένας πρώην εκπαιδευτικός διηγείται σε ένα podcast πώς πέρασε τον πρώτο χρόνο της σύνταξής του.",
 "script": [
  L("Κυρ Φώτης", "m", "Τριάντα πέντε χρόνια ξυπνούσα στις έξι και μισή για να πάω στο σχολείο. Ονειρευόμουν τη σύνταξη σαν μια ατέλειωτη Κυριακή. Τον πρώτο μήνα κοιμόμουν μέχρι αργά, διάβαζα εφημερίδες στο καφενείο και έλεγα ότι ζω τον παράδεισο.", "For thirty-five years I woke at half past six to go to school. I dreamed of retirement as an endless Sunday. The first month I slept late, read newspapers at the café and said I was living in paradise."),
  L("Κυρ Φώτης", "m", "Τον τρίτο μήνα άρχισα να νιώθω άχρηστος. Η γυναίκα μου δούλευε ακόμα, τα παιδιά είχαν τις ζωές τους, και εγώ περιφερόμουν στο σπίτι χωρίς λόγο. Μου έλειπαν οι μαθητές, οι φωνές στο διάλειμμα, ακόμα και οι συνεδριάσεις που τόσο βαριόμουν.", "By the third month I began to feel useless. My wife was still working, the children had their own lives, and I wandered around the house for no reason. I missed the pupils, the shouting at break, even the staff meetings that used to bore me so much."),
  L("Κυρ Φώτης", "m", "Η λύση ήρθε από έναν παλιό μαθητή μου, που δουλεύει σε ένα κέντρο για προσφυγόπουλα. Μου πρότεινε να κάνω εθελοντικά μαθήματα ελληνικών δύο φορές την εβδομάδα. Τώρα έχω πάλι πρόγραμμα, αλλά αυτή τη φορά το διαλέγω εγώ. Και κάθε φορά που ένα παιδί διαβάζει την πρώτη του πρόταση, νιώθω σαν να ξεκινάω από την αρχή.", "The solution came from a former pupil of mine, who works at a centre for refugee children. He suggested I give volunteer Greek lessons twice a week. Now I have a timetable again, but this time I choose it. And every time a child reads their first sentence, I feel as if I'm starting from the beginning."),
 ],
 "questions": [
  Q("Πώς φανταζόταν ο κυρ Φώτης τη σύνταξη;", ["Σαν μια δύσκολη περίοδο", "Σαν μια ατέλειωτη Κυριακή", "Σαν ένα μεγάλο ταξίδι", "Σαν μια νέα δουλειά"], 1, "Ονειρευόμουν τη σύνταξη σαν μια ατέλειωτη Κυριακή"),
  Q("Πώς ένιωθε τον τρίτο μήνα;", ["Ξεκούραστος", "Άχρηστος", "Ενθουσιασμένος", "Άρρωστος"], 1, "Τον τρίτο μήνα άρχισα να νιώθω άχρηστος"),
  Q("Τι κάνει τώρα;", ["Δουλεύει ξανά στο σχολείο", "Κάνει εθελοντικά μαθήματα ελληνικών σε προσφυγόπουλα", "Γράφει ένα βιβλίο", "Ταξιδεύει με τη γυναίκα του"], 1, "Μου πρότεινε να κάνω εθελοντικά μαθήματα ελληνικών δύο φορές την εβδομάδα"),
 ],
 "gloss": {"σύνταξη": "σύνταξη — retirement, pension", "εκπαιδευτικός": "εκπαιδευτικός — teacher", "ατέλειωτη": "ατέλειωτος — endless", "άχρηστος": "άχρηστος — useless", "περιφερόμουν": "περιφέρομαι — to wander around", "διάλειμμα": "διάλειμμα — (school) break", "συνεδριάσεις": "συνεδρίαση — (staff) meeting", "βαριόμουν": "βαριέμαι — to be bored by", "προσφυγόπουλα": "προσφυγόπουλο — refugee child", "εθελοντικά": "εθελοντικά — voluntarily, as a volunteer"},
})

ITEMS.append({
 "id": "l79-mono-skaki-parko", "title": "Το σκάκι στο πάρκο", "title_en": "Chess in the park", "type": "monologue", "level": "B2",
 "context_el": "Μια φοιτήτρια διηγείται πώς έμαθε σκάκι από μια παρέα ηλικιωμένων σε ένα πάρκο της Θεσσαλονίκης.",
 "script": [
  L("Αλίκη", "f", "Κάθε απόγευμα, στο πάρκο κάτω από το σπίτι μου, μια παρέα από συνταξιούχους έπαιζε σκάκι σε δύο πέτρινα τραπέζια. Περνούσα από εκεί για να πάω στη σχολή και τους άκουγα να μαλώνουν δυνατά για κάθε κίνηση. Μια μέρα σταμάτησα να κοιτάξω, και ο κυρ Παύλος με ρώτησε αν ξέρω να παίζω.", "Every afternoon, in the park below my flat, a group of pensioners played chess at two stone tables. I passed by on the way to university and heard them arguing loudly about every move. One day I stopped to watch, and Mr Pavlos asked me if I knew how to play."),
  L("Αλίκη", "f", "Ήξερα μόνο πώς κινούνται τα κομμάτια. Με έβαλαν να παίξω με τον πιο αδύναμο της παρέας και έχασα σε δέκα λεπτά. Αντί να γελάσουν, μου εξήγησαν με υπομονή τι έκανα λάθος: ότι έβγαζα τη βασίλισσα πολύ νωρίς και ότι άφηνα τον βασιλιά απροστάτευτο.", "I only knew how the pieces move. They had me play against the weakest of the group and I lost in ten minutes. Instead of laughing, they patiently explained what I'd done wrong: that I brought the queen out too early and left the king unprotected."),
  L("Αλίκη", "f", "Πάνε δύο χρόνια από τότε. Πηγαίνω σχεδόν κάθε μέρα, και πέρσι κέρδισα για πρώτη φορά τον κυρ Παύλο. Εκείνος σηκώθηκε, μου έσφιξε το χέρι και είπε: «Τώρα πρέπει να βρεις κι εσύ κάποιον να του μάθεις.» Νομίζω ότι αυτό είναι το πιο σπουδαίο μάθημα που μου έδωσαν.", "It's been two years since then. I go almost every day, and last year I beat Mr Pavlos for the first time. He stood up, shook my hand and said: 'Now you have to find someone to teach too.' I think that's the most important lesson they gave me."),
 ],
 "questions": [
  Q("Πού έπαιζαν σκάκι οι συνταξιούχοι;", ["Σε ένα καφενείο", "Σε δύο πέτρινα τραπέζια σε ένα πάρκο", "Σε μια σκακιστική λέσχη", "Στο σπίτι του κυρ Παύλου"], 1, "έπαιζε σκάκι σε δύο πέτρινα τραπέζια"),
  Q("Τι έκανε λάθος η Αλίκη στις πρώτες παρτίδες;", ["Δεν ήξερε πώς κινούνται τα κομμάτια", "Έβγαζε τη βασίλισσα πολύ νωρίς και άφηνε τον βασιλιά απροστάτευτο", "Έπαιζε πολύ αργά", "Μιλούσε την ώρα του παιχνιδιού"], 1, "ότι έβγαζα τη βασίλισσα πολύ νωρίς και ότι άφηνα τον βασιλιά απροστάτευτο"),
  Q("Τι της είπε ο κυρ Παύλος όταν έχασε από εκείνη;", ["Να μην ξαναέρθει", "Να βρει κι εκείνη κάποιον να του μάθει", "Να παίξει σε αγώνες", "Να του κάνει μια ρεβάνς"], 1, "Τώρα πρέπει να βρεις κι εσύ κάποιον να του μάθεις"),
 ],
 "gloss": {"σκάκι": "σκάκι — chess", "κίνηση": "κίνηση — move", "κομμάτια": "κομμάτι — (chess) piece", "αδύναμο": "αδύναμος — weak", "βασίλισσα": "βασίλισσα — queen", "βασιλιά": "βασιλιάς — king", "απροστάτευτο": "απροστάτευτος — unprotected", "έσφιξε το χέρι": "σφίγγω το χέρι — to shake hands", "σπουδαίο": "σπουδαίος — important, great"},
})

ITEMS.append({
 "id": "l79-c1-emoji", "title": "Είναι τα emoji γλώσσα;", "title_en": "Are emoji a language?", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για τη γλώσσα, μια γλωσσολόγος μιλά για τα emoji, τα μικρά εικονίδια που χρησιμοποιούμε στα γραπτά μηνύματα.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί γονείς ανησυχούν ότι τα παιδιά τους «μιλούν» πια με εικονίδια. Είναι τα emoji μια νέα γλώσσα;", "Many parents worry that their children now 'speak' in icons. Are emoji a new language?"),
  L("Γλωσσολόγος", "f", "Όχι με την αυστηρή έννοια. Μια γλώσσα έχει γραμματική, σύνταξη, τη δυνατότητα να εκφράσει αφηρημένες έννοιες ή το παρελθόν και το μέλλον. Τα emoji δεν έχουν τίποτα από αυτά. Η λειτουργία τους μοιάζει περισσότερο με αυτήν του τόνου της φωνής ή των χειρονομιών: συμπληρώνουν το γραπτό κείμενο με όσα στον προφορικό λόγο μεταδίδει το σώμα. Ένα «εντάξει» σκέτο μπορεί να ακουστεί ψυχρό· με ένα χαμογελαστό προσωπάκι, η ένταση εξαφανίζεται.", "Not in the strict sense. A language has grammar, syntax, the capacity to express abstract concepts or the past and the future. Emoji have none of that. Their function resembles that of tone of voice or gestures more: they supplement written text with what the body conveys in speech. A bare 'OK' can sound cold; with a smiley face, the tension disappears."),
  L("Δημοσιογράφος", "m", "Και η σημασία τους είναι πάντα σαφής;", "And is their meaning always clear?"),
  L("Γλωσσολόγος", "f", "Κάθε άλλο. Η ερμηνεία τους διαφέρει από γενιά σε γενιά και από πολιτισμό σε πολιτισμό. Για πολλούς μεγαλύτερους, ο σηκωμένος αντίχειρας σημαίνει απλώς «συμφωνώ»· για αρκετούς νέους, ακούγεται ξερός, σχεδόν επιθετικός. Οι παρεξηγήσεις έχουν φτάσει μέχρι και στα δικαστήρια: στον Καναδά, ένα δικαστήριο έκρινε ότι ένας αντίχειρας σε απάντηση ενός συμβολαίου ισοδυναμούσε με αποδοχή. Το συμπέρασμα δεν είναι ότι τα emoji φτωχαίνουν τη γλώσσα, αλλά ότι, όπως κάθε μέσο επικοινωνίας, απαιτούν κοινούς κώδικες.", "Far from it. Their interpretation differs from generation to generation and from culture to culture. For many older people, the raised thumb simply means 'I agree'; for quite a few young people, it sounds curt, almost aggressive. Misunderstandings have even reached the courts: in Canada, a court ruled that a thumb in reply to a contract amounted to acceptance. The conclusion is not that emoji impoverish language, but that, like every means of communication, they require shared codes."),
 ],
 "questions": [
  Q("Γιατί, κατά τη γλωσσολόγο, τα emoji δεν είναι γλώσσα με την αυστηρή έννοια;", ["Γιατί είναι πολύ καινούργια", "Γιατί δεν έχουν γραμματική, σύνταξη ούτε δυνατότητα για αφηρημένες έννοιες", "Γιατί τα χρησιμοποιούν μόνο οι νέοι", "Γιατί δεν τα καταλαβαίνει κανείς"], 1, "Τα emoji δεν έχουν τίποτα από αυτά"),
  Q("Με τι μοιάζει η λειτουργία των emoji;", ["Με τα σημεία στίξης", "Με τον τόνο της φωνής ή τις χειρονομίες", "Με τα αρχαία ιερογλυφικά", "Με τις συντομογραφίες"], 1, "Η λειτουργία τους μοιάζει περισσότερο με αυτήν του τόνου της φωνής ή των χειρονομιών"),
  Q("Τι συμπέρασμα βγάζει η γλωσσολόγος;", ["Ότι τα emoji φτωχαίνουν τη γλώσσα", "Ότι τα emoji, όπως κάθε μέσο επικοινωνίας, απαιτούν κοινούς κώδικες", "Ότι πρέπει να απαγορευτούν στα σχολεία", "Ότι θα αντικαταστήσουν τις λέξεις"], 1, "όπως κάθε μέσο επικοινωνίας, απαιτούν κοινούς κώδικες"),
 ],
 "gloss": {"εικονίδια": "εικονίδιο — icon", "αφηρημένες έννοιες": "αφηρημένη έννοια — abstract concept", "χειρονομιών": "χειρονομία — gesture", "συμπληρώνουν": "συμπληρώνω — to supplement, complete", "σκέτο": "σκέτος — bare, plain", "Κάθε άλλο": "κάθε άλλο — far from it", "αντίχειρας": "αντίχειρας — thumb", "ξερός": "ξερός — curt, dry", "ισοδυναμούσε": "ισοδυναμώ — to be equivalent to", "αποδοχή": "αποδοχή — acceptance", "κώδικες": "κώδικας — code"},
})

ITEMS.append({
 "id": "l79-c1-oikonomia-diamoirasmou", "title": "Η οικονομία του διαμοιρασμού: υπόσχεση και πραγματικότητα", "title_en": "The sharing economy: promise and reality", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε απόσπασμα από μια διάλεξη ενός οικονομολόγου για την οικονομία του διαμοιρασμού.",
 "script": [
  L("Οικονομολόγος", "m", "Πριν από περίπου δεκαπέντε χρόνια, η λεγόμενη οικονομία του διαμοιρασμού παρουσιάστηκε σχεδόν ως κοινωνικό κίνημα. Η ιδέα ήταν γοητευτική: γιατί να έχει ο καθένας μας ένα δράπανο που χρησιμοποιεί δέκα λεπτά τον χρόνο, ένα αυτοκίνητο που μένει παρκαρισμένο το ενενήντα τοις εκατό του χρόνου, ένα δωμάτιο που μένει άδειο; Η τεχνολογία θα μας επέτρεπε να μοιραζόμαστε, να εξοικονομούμε πόρους και, παράλληλα, να γνωρίζουμε ο ένας τον άλλον.", "About fifteen years ago, the so-called sharing economy was presented almost as a social movement. The idea was appealing: why should each of us have a drill we use ten minutes a year, a car that stays parked ninety per cent of the time, a room that stays empty? Technology would allow us to share, to save resources and, at the same time, to get to know one another."),
  L("Οικονομολόγος", "m", "Η πραγματικότητα αποδείχθηκε πιο σύνθετη. Οι μεγαλύτερες πλατφόρμες δεν διευκόλυναν τόσο τον διαμοιρασμό όσο τη μετατροπή κάθε ιδιωτικού αγαθού σε εμπόρευμα. Στα κέντρα πολλών ευρωπαϊκών πόλεων, ανάμεσά τους και της Αθήνας, ολόκληρες πολυκατοικίες μετατράπηκαν σε καταλύματα βραχυχρόνιας μίσθωσης, με αποτέλεσμα τα ενοίκια να αυξηθούν και οι μόνιμοι κάτοικοι να εκτοπιστούν.", "Reality proved more complex. The biggest platforms facilitated not so much sharing as the conversion of every private good into a commodity. In the centres of many European cities, among them Athens, whole apartment blocks were turned into short-term rental accommodation, with the result that rents rose and permanent residents were displaced."),
  L("Οικονομολόγος", "m", "Παράλληλα, οι οδηγοί και οι διανομείς που εργάζονται μέσω εφαρμογών θεωρούνται συχνά «συνεργάτες» και όχι εργαζόμενοι, χωρίς ασφάλιση ή άδεια. Δεν υποστηρίζω ότι το μοντέλο είναι εξ ορισμού καταδικαστέο. Υποστηρίζω ότι μια τεχνολογία δεν είναι ποτέ ουδέτερη: το αν θα εξυπηρετήσει την κοινότητα ή μόνο τους μετόχους εξαρτάται από τους κανόνες που θα θέσουμε.", "At the same time, drivers and couriers working through apps are often regarded as 'partners' and not employees, without insurance or leave. I am not arguing that the model is by definition to be condemned. I am arguing that a technology is never neutral: whether it serves the community or only the shareholders depends on the rules we set."),
 ],
 "questions": [
  Q("Ποια ήταν η αρχική ιδέα της οικονομίας του διαμοιρασμού;", ["Να αυξηθούν τα κέρδη των εταιρειών", "Να μοιραζόμαστε αγαθά που μένουν αχρησιμοποίητα και να εξοικονομούμε πόρους", "Να αντικατασταθούν τα καταστήματα", "Να μειωθούν οι φόροι"], 1, "Η τεχνολογία θα μας επέτρεπε να μοιραζόμαστε, να εξοικονομούμε πόρους"),
  Q("Τι συνέβη, κατά τον ομιλητή, στα κέντρα πολλών πόλεων;", ["Μειώθηκαν τα ενοίκια", "Πολυκατοικίες μετατράπηκαν σε καταλύματα βραχυχρόνιας μίσθωσης και οι κάτοικοι εκτοπίστηκαν", "Χτίστηκαν νέες κατοικίες", "Αυξήθηκε ο πληθυσμός"], 1, "οι μόνιμοι κάτοικοι να εκτοπιστούν"),
  Q("Ποια είναι η βασική θέση του ομιλητή;", ["Ότι το μοντέλο πρέπει να απαγορευτεί", "Ότι μια τεχνολογία δεν είναι ουδέτερη και εξαρτάται από τους κανόνες που θέτουμε", "Ότι οι πλατφόρμες είναι πάντα ωφέλιμες", "Ότι οι διανομείς πρέπει να γίνουν μέτοχοι"], 1, "μια τεχνολογία δεν είναι ποτέ ουδέτερη"),
 ],
 "gloss": {"διαμοιρασμού": "διαμοιρασμός — sharing", "κίνημα": "κίνημα — movement", "δράπανο": "δράπανο — (power) drill", "εξοικονομούμε": "εξοικονομώ — to save (resources)", "εμπόρευμα": "εμπόρευμα — commodity", "καταλύματα": "κατάλυμα — accommodation", "βραχυχρόνιας μίσθωσης": "βραχυχρόνια μίσθωση — short-term rental", "εκτοπιστούν": "εκτοπίζομαι — to be displaced", "διανομείς": "διανομέας — courier, delivery rider", "καταδικαστέο": "καταδικαστέος — to be condemned", "μετόχους": "μέτοχος — shareholder"},
})

rnd = random.Random(79)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-79.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
