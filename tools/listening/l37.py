# Source for library/listening/listening-37.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l37.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l37-ann-vivliothiki", "title": "Η βιβλιοθήκη κλείνει σε λίγο", "title_en": "The library is closing soon", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα μιας δημοτικής βιβλιοθήκης.",
 "script": [
  L("Βιβλιοθηκονόμος", "f", "Αγαπητοί επισκέπτες, η βιβλιοθήκη θα κλείσει σε δεκαπέντε λεπτά. Παρακαλούμε να ολοκληρώσετε τους δανεισμούς σας και να αφήσετε τα βιβλία που δεν θα πάρετε μαζί σας στα καρότσια, όχι πίσω στα ράφια, για να τα τακτοποιήσει το προσωπικό.", "Dear visitors, the library will close in fifteen minutes. Please complete your loans and leave the books you won't take with you on the trolleys, not back on the shelves, so that the staff can put them away."),
  L("Βιβλιοθηκονόμος", "f", "Σας υπενθυμίζουμε ότι από τη Δευτέρα λειτουργεί στην είσοδο το νέο μηχάνημα αυτόματου δανεισμού. Αρκεί να σκανάρετε την κάρτα μέλους και τα βιβλία, και η απόδειξη με την ημερομηνία επιστροφής στέλνεται στο ηλεκτρονικό σας ταχυδρομείο.", "We remind you that from Monday the new self-service loan machine is operating at the entrance. You only need to scan your membership card and the books, and the receipt with the return date is sent to your email."),
  L("Βιβλιοθηκονόμος", "f", "Η διάρκεια του δανεισμού αυξάνεται από δύο σε τρεις εβδομάδες, ενώ τα πρόστιμα για καθυστερημένες επιστροφές καταργούνται για τα παιδικά βιβλία. Τα βιβλία μπορείτε να τα επιστρέφετε και όταν η βιβλιοθήκη είναι κλειστή, στο κουτί δίπλα στην κεντρική πόρτα. Καλό σας βράδυ.", "The loan period is increasing from two to three weeks, while fines for late returns are being abolished for children's books. You can also return books when the library is closed, in the box next to the main door. Good evening."),
 ],
 "questions": [
  Q("Πού πρέπει να αφήσουν οι επισκέπτες τα βιβλία που δεν θα δανειστούν;", ["Πίσω στα ράφια", "Στα καρότσια", "Στο γκισέ", "Στα τραπέζια"], 1, "στα καρότσια, όχι πίσω στα ράφια"),
  Q("Πώς λειτουργεί το νέο μηχάνημα;", ["Χρειάζεται βοήθεια από το προσωπικό", "Σκανάρεις την κάρτα και τα βιβλία και παίρνεις την απόδειξη με email", "Δέχεται μόνο επιστροφές", "Λειτουργεί μόνο τη νύχτα"], 1, "Αρκεί να σκανάρετε την κάρτα μέλους και τα βιβλία"),
  Q("Τι αλλάζει για τα παιδικά βιβλία;", ["Δανείζονται μόνο για μία εβδομάδα", "Καταργούνται τα πρόστιμα για καθυστέρηση", "Δεν δανείζονται πια", "Επιστρέφονται μόνο το πρωί"], 1, "τα πρόστιμα για καθυστερημένες επιστροφές καταργούνται για τα παιδικά βιβλία"),
 ],
 "gloss": {"βιβλιοθήκης": "βιβλιοθήκη — library", "δανεισμούς": "δανεισμός — loan", "καρότσια": "καρότσι — trolley", "να τα τακτοποιήσει": "τακτοποιώ — to tidy, put away", "κάρτα μέλους": "κάρτα μέλους — membership card", "ηλεκτρονικό σας ταχυδρομείο": "ηλεκτρονικό ταχυδρομείο — email", "διάρκεια": "διάρκεια — duration", "πρόστιμα": "πρόστιμο — fine", "καταργούνται": "καταργούμαι — to be abolished"},
})

ITEMS.append({
 "id": "l37-vm-syllogos-goneon", "title": "Μήνυμα από τον σύλλογο γονέων", "title_en": "A message from the parents' association", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από την πρόεδρο του συλλόγου γονέων του σχολείου.",
 "script": [
  L("Πρόεδρος", "f", "Καλησπέρα, η Κατερίνα είμαι, από τον σύλλογο γονέων. Σας τηλεφωνώ για την τριήμερη εκδρομή της έκτης τάξης στο Ναύπλιο. Δυστυχώς το ξενοδοχείο που είχαμε κλείσει ακύρωσε την κράτηση, γιατί κάνει ανακαίνιση, και βρήκαμε ένα άλλο, λίγο πιο έξω από την πόλη.", "Good evening, it's Katerina, from the parents' association. I'm calling about the sixth grade's three-day trip to Nafplio. Unfortunately the hotel we'd booked cancelled the reservation because it's being renovated, and we've found another one, a little outside the town."),
  L("Πρόεδρος", "f", "Το νέο ξενοδοχείο είναι λίγο ακριβότερο, οπότε το κόστος ανεβαίνει κατά δεκαπέντε ευρώ ανά παιδί. Ο σύλλογος θα καλύψει τη διαφορά για τις οικογένειες που το χρειάζονται· αρκεί να μου στείλετε ένα μήνυμα, και φυσικά θα μείνει μεταξύ μας.", "The new hotel is a bit more expensive, so the cost goes up by fifteen euros per child. The association will cover the difference for families who need it; just send me a message, and of course it will stay between us."),
  L("Πρόεδρος", "f", "Επίσης, ψάχνουμε ακόμη έναν γονιό για συνοδό, γιατί ένας από τους δασκάλους δεν μπορεί να έρθει. Αν μπορείτε να πάρετε άδεια από τη δουλειά σας εκείνες τις μέρες, πείτε μου μέχρι την Τετάρτη. Ευχαριστώ πολύ!", "Also, we're still looking for one more parent as a chaperone, because one of the teachers can't come. If you can take leave from work on those days, let me know by Wednesday. Thanks very much!"),
 ],
 "questions": [
  Q("Γιατί άλλαξε το ξενοδοχείο;", ["Γιατί ήταν πολύ ακριβό", "Γιατί το πρώτο ακύρωσε την κράτηση λόγω ανακαίνισης", "Γιατί ήταν μακριά από την πόλη", "Γιατί δεν δεχόταν παιδιά"], 1, "ακύρωσε την κράτηση, γιατί κάνει ανακαίνιση"),
  Q("Τι θα κάνει ο σύλλογος για τις οικογένειες που δυσκολεύονται;", ["Θα ακυρώσει την εκδρομή", "Θα καλύψει τη διαφορά στο κόστος", "Θα ζητήσει δάνειο", "Θα μειώσει τις μέρες της εκδρομής"], 1, "Ο σύλλογος θα καλύψει τη διαφορά"),
  Q("Τι ζητάει η πρόεδρος μέχρι την Τετάρτη;", ["Να πληρωθούν τα χρήματα", "Έναν γονιό που μπορεί να συνοδεύσει τα παιδιά", "Τις ταυτότητες των παιδιών", "Ιδέες για δραστηριότητες"], 1, "ψάχνουμε ακόμη έναν γονιό για συνοδό"),
 ],
 "gloss": {"συλλόγου γονέων": "σύλλογος γονέων — parents' association", "πρόεδρο": "πρόεδρος — chair, president", "τριήμερη": "τριήμερος — three-day", "εκδρομή": "εκδρομή — school trip, excursion", "ακύρωσε": "ακυρώνω — to cancel", "ανακαίνιση": "ανακαίνιση — renovation", "θα καλύψει": "καλύπτω — to cover", "διαφορά": "διαφορά — difference", "συνοδό": "συνοδός — chaperone", "άδεια": "άδεια — leave (from work)"},
})

ITEMS.append({
 "id": "l37-dia-akoustika", "title": "Επιστροφή ελαττωματικών ακουστικών", "title_en": "Returning faulty headphones", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα κατάστημα ηλεκτρονικών ειδών, όπου μια πελάτισσα φέρνει πίσω ελαττωματικά ακουστικά.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Αγόρασα αυτά τα ασύρματα ακουστικά πριν από τρεις εβδομάδες, και το αριστερό έχει σταματήσει να λειτουργεί. Το φόρτισα, το επανέφερα στις εργοστασιακές ρυθμίσεις, τίποτα.", "Good morning. I bought these wireless headphones three weeks ago, and the left one has stopped working. I charged it, reset it to factory settings, nothing."),
  L("Υπάλληλος", "m", "Λυπάμαι πολύ. Έχετε την απόδειξη; Επειδή έχουν περάσει πάνω από δεκαπέντε μέρες από την αγορά, δεν μπορώ να σας τα αλλάξω επιτόπου. Θα πρέπει να σταλούν στο τμήμα επισκευών του κατασκευαστή, στο πλαίσιο της εγγύησης.", "I'm very sorry. Do you have the receipt? Because more than fifteen days have passed since the purchase, I can't exchange them on the spot. They'll have to be sent to the manufacturer's repair department, under the warranty."),
  L("Πελάτισσα", "f", "Και πόσο θα πάρει αυτό; Τα χρειάζομαι καθημερινά για τη δουλειά, κάνω πολλές βιντεοκλήσεις.", "And how long will that take? I need them every day for work; I make a lot of video calls."),
  L("Υπάλληλος", "m", "Συνήθως δέκα με δεκαπέντε εργάσιμες. Αν δεν μπορούν να επισκευαστούν, θα σας δοθούν καινούργια. Μέχρι τότε, μπορώ να σας δανείσω ένα ζευγάρι ενσύρματα ακουστικά από το κατάστημα, χωρίς χρέωση. Θα σας ενημερώσουμε με μήνυμα μόλις επιστρέψουν.", "Usually ten to fifteen working days. If they can't be repaired, you'll be given new ones. Until then, I can lend you a pair of wired headphones from the shop, free of charge. We'll let you know by text as soon as they're back."),
 ],
 "questions": [
  Q("Τι πρόβλημα έχουν τα ακουστικά;", ["Δεν φορτίζουν καθόλου", "Το αριστερό ακουστικό σταμάτησε να λειτουργεί", "Ο ήχος είναι πολύ χαμηλός", "Έσπασε η θήκη"], 1, "το αριστερό έχει σταματήσει να λειτουργεί"),
  Q("Γιατί ο υπάλληλος δεν μπορεί να τα αλλάξει αμέσως;", ["Γιατί δεν έχει απόδειξη", "Γιατί έχουν περάσει πάνω από δεκαπέντε μέρες από την αγορά", "Γιατί η εγγύηση έληξε", "Γιατί δεν υπάρχουν άλλα στο απόθεμα"], 1, "έχουν περάσει πάνω από δεκαπέντε μέρες από την αγορά"),
  Q("Τι προσφέρει ο υπάλληλος μέχρι να γυρίσουν τα ακουστικά;", ["Έκπτωση σε νέα αγορά", "Δανεικά ενσύρματα ακουστικά χωρίς χρέωση", "Επιστροφή χρημάτων", "Δωροεπιταγή"], 1, "μπορώ να σας δανείσω ένα ζευγάρι ενσύρματα ακουστικά"),
 ],
 "gloss": {"ελαττωματικά": "ελαττωματικός — faulty", "ηλεκτρονικών ειδών": "ηλεκτρονικά είδη — electronics", "ασύρματα": "ασύρματος — wireless", "ακουστικά": "ακουστικά — headphones", "Το φόρτισα": "φορτίζω — to charge", "εργοστασιακές ρυθμίσεις": "εργοστασιακές ρυθμίσεις — factory settings", "επιτόπου": "επιτόπου — on the spot", "κατασκευαστή": "κατασκευαστής — manufacturer", "εγγύησης": "εγγύηση — warranty, guarantee", "εργάσιμες": "εργάσιμη (μέρα) — working day", "ενσύρματα": "ενσύρματος — wired", "χρέωση": "χρέωση — charge"},
})

ITEMS.append({
 "id": "l37-dia-paroxos-revmatos", "title": "Αλλάζοντας πάροχο ρεύματος", "title_en": "Switching electricity supplier", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο ανάμεσα σε δύο φίλους που συζητούν τους λογαριασμούς του ρεύματος.",
 "script": [
  L("Μάρκος", "m", "Είδες τον λογαριασμό του ρεύματος αυτόν τον μήνα; Εκατόν σαράντα ευρώ, για ένα δυάρι! Σκέφτομαι σοβαρά να αλλάξω πάροχο, αλλά φοβάμαι μήπως μείνω χωρίς ρεύμα για μέρες.", "Did you see the electricity bill this month? A hundred and forty euros, for a two-room flat! I'm seriously thinking of switching supplier, but I'm afraid I'll be left without power for days."),
  L("Ελένη", "f", "Όχι, δεν κόβεται τίποτα. Εγώ άλλαξα πέρσι. Κάνεις αίτηση στον νέο πάροχο, συνήθως ηλεκτρονικά, και εκείνος αναλαμβάνει όλη τη διαδικασία. Το ρεύμα περνάει από τα ίδια καλώδια· αλλάζει μόνο ποιος σου στέλνει τον λογαριασμό.", "No, nothing gets cut off. I switched last year. You apply to the new supplier, usually online, and they handle the whole process. The electricity goes through the same cables; only who sends you the bill changes."),
  L("Μάρκος", "m", "Και πώς διαλέγεις; Όλοι λένε ότι είναι οι φθηνότεροι.", "And how do you choose? They all say they're the cheapest."),
  L("Ελένη", "f", "Υπάρχει ένα εργαλείο σύγκρισης στην ιστοσελίδα της Ρυθμιστικής Αρχής, όπου βάζεις την κατανάλωσή σου και βλέπεις τα τιμολόγια το ένα δίπλα στο άλλο. Πρόσεξε όμως τα ψιλά γράμματα: κάποια τιμολόγια έχουν χαμηλή τιμή μόνο για λίγους μήνες, ή πάγια χρέωση που δεν φαίνεται με την πρώτη ματιά. Και διάβασε αν υπάρχει ρήτρα αποχώρησης, για να μην πληρώσεις αν θελήσεις να ξαναλλάξεις.", "There's a comparison tool on the Regulatory Authority's website, where you enter your consumption and see the tariffs side by side. But watch the small print: some tariffs have a low price only for a few months, or a standing charge you don't see at first glance. And check whether there's an exit clause, so you don't pay if you want to switch again."),
 ],
 "questions": [
  Q("Τι φοβάται ο Μάρκος;", ["Ότι θα πληρώσει περισσότερα", "Ότι θα μείνει χωρίς ρεύμα για μέρες", "Ότι θα χρειαστεί νέα καλώδια", "Ότι θα χάσει το διαμέρισμα"], 1, "φοβάμαι μήπως μείνω χωρίς ρεύμα για μέρες"),
  Q("Τι εξηγεί η Ελένη για τη διαδικασία;", ["Ότι πρέπει να έρθει τεχνικός", "Ότι ο νέος πάροχος αναλαμβάνει τα πάντα και αλλάζει μόνο ο λογαριασμός", "Ότι κρατάει έναν μήνα χωρίς ρεύμα", "Ότι γίνεται μόνο σε κατάστημα"], 1, "αλλάζει μόνο ποιος σου στέλνει τον λογαριασμό"),
  Q("Για ποιο από τα παρακάτω ΔΕΝ προειδοποιεί η Ελένη;", ["Για χαμηλές τιμές που ισχύουν λίγους μήνες", "Για τον κίνδυνο διακοπής ρεύματος", "Για κρυφές πάγιες χρεώσεις", "Για ρήτρα αποχώρησης"], 1, "Πρόσεξε όμως τα ψιλά γράμματα"),
 ],
 "gloss": {"πάροχο": "πάροχος — supplier, provider", "λογαριασμό": "λογαριασμός — bill", "δυάρι": "δυάρι — two-room flat", "αναλαμβάνει": "αναλαμβάνω — to take on, handle", "καλώδια": "καλώδιο — cable", "εργαλείο σύγκρισης": "εργαλείο σύγκρισης — comparison tool", "κατανάλωσή": "κατανάλωση — consumption", "τιμολόγια": "τιμολόγιο — tariff", "ψιλά γράμματα": "ψιλά γράμματα — small print", "πάγια χρέωση": "πάγια χρέωση — standing charge", "ρήτρα αποχώρησης": "ρήτρα αποχώρησης — exit clause"},
})

ITEMS.append({
 "id": "l37-mono-nychterini-vardia", "title": "Νυχτερινή βάρδια", "title_en": "Night shift", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια νοσηλεύτρια να μιλάει για τη δουλειά της στη νυχτερινή βάρδια ενός νοσοκομείου.",
 "script": [
  L("Δέσποινα", "f", "Είμαι νοσηλεύτρια στην παθολογική κλινική εδώ και δεκαοχτώ χρόνια, και τις μισές περίπου νύχτες του μήνα τις περνάω στο νοσοκομείο. Η βάρδια ξεκινάει στις δέκα το βράδυ και τελειώνει στις έξι το πρωί. Είμαστε δύο νοσηλεύτριες για τριάντα ασθενείς.", "I've been a nurse in the internal medicine ward for eighteen years, and I spend about half the nights of the month at the hospital. The shift starts at ten at night and ends at six in the morning. There are two of us nurses for thirty patients."),
  L("Δέσποινα", "f", "Ο κόσμος φαντάζεται ότι τη νύχτα οι ασθενείς κοιμούνται και εμείς πίνουμε καφέ. Η αλήθεια είναι ότι η νύχτα είναι η πιο δύσκολη ώρα. Οι ηλικιωμένοι μπερδεύονται στο σκοτάδι, ο πόνος μοιάζει χειρότερος, και ο φόβος μεγαλώνει όταν δεν υπάρχει κανείς δικός τους δίπλα. Πολλές φορές το πιο σημαντικό που κάνω δεν είναι να δώσω ένα φάρμακο, αλλά να καθίσω πέντε λεπτά και να κρατήσω ένα χέρι.", "People imagine that at night the patients sleep and we drink coffee. The truth is that night is the hardest time. Elderly people get confused in the dark, pain seems worse, and fear grows when none of their own people are beside them. Often the most important thing I do isn't giving a medicine, but sitting for five minutes and holding a hand."),
  L("Δέσποινα", "f", "Το τίμημα το πληρώνει ο οργανισμός. Κοιμάμαι τη μέρα με κουρτίνες σκοτεινές και ωτοασπίδες, αλλά ποτέ δεν είναι το ίδιο. Και βέβαια χάνω γιορτές και γενέθλια. Αν με ρωτήσετε όμως αν θα το ξαναδιάλεγα, η απάντηση είναι ναι.", "The body pays the price. I sleep in the day with blackout curtains and earplugs, but it's never the same. And of course I miss celebrations and birthdays. But if you ask me whether I'd choose it again, the answer is yes."),
 ],
 "questions": [
  Q("Πόσες νοσηλεύτριες δουλεύουν τη νύχτα στην κλινική;", ["Μία", "Δύο, για τριάντα ασθενείς", "Πέντε", "Δέκα"], 1, "Είμαστε δύο νοσηλεύτριες για τριάντα ασθενείς"),
  Q("Γιατί η νύχτα είναι, κατά τη Δέσποινα, η πιο δύσκολη ώρα;", ["Γιατί έρχονται πολλά επείγοντα", "Γιατί οι ασθενείς μπερδεύονται, πονούν και φοβούνται περισσότερο", "Γιατί δεν υπάρχουν γιατροί", "Γιατί κλείνει το φαρμακείο"], 1, "η νύχτα είναι η πιο δύσκολη ώρα"),
  Q("Τι θεωρεί συχνά πιο σημαντικό από τα φάρμακα;", ["Να καθαρίσει τους θαλάμους", "Να καθίσει λίγο με τον ασθενή και να του κρατήσει το χέρι", "Να ενημερώσει τους συγγενείς", "Να συμπληρώσει τα χαρτιά"], 1, "να καθίσω πέντε λεπτά και να κρατήσω ένα χέρι"),
 ],
 "gloss": {"νοσηλεύτρια": "νοσηλεύτρια — nurse", "βάρδια": "βάρδια — shift", "παθολογική κλινική": "παθολογική κλινική — internal medicine ward", "ασθενείς": "ασθενής — patient", "μπερδεύονται": "μπερδεύομαι — to get confused", "τίμημα": "τίμημα — price, cost", "οργανισμός": "οργανισμός — body, organism", "ωτοασπίδες": "ωτοασπίδα — earplug", "θα το ξαναδιάλεγα": "ξαναδιαλέγω — to choose again"},
})

ITEMS.append({
 "id": "l37-rep-karnavali", "title": "Το καρναβάλι της Πάτρας", "title_en": "The Patras Carnival", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από τη μεγάλη παρέλαση του καρναβαλιού της Πάτρας.",
 "script": [
  L("Δημοσιογράφος", "m", "Είναι η τελευταία Κυριακή της Αποκριάς, και η Πάτρα έχει μετατραπεί σε μια τεράστια γιορτή. Χιλιάδες καρναβαλιστές, χωρισμένοι σε πληρώματα, παρελαύνουν στους κεντρικούς δρόμους με στολές που ετοίμαζαν επί μήνες, ενώ ανάμεσά τους προχωρούν τα γιγάντια άρματα.", "It's the last Sunday of Carnival, and Patras has turned into a huge celebration. Thousands of carnival-goers, divided into crews, parade through the central streets in costumes they spent months preparing, while the giant floats move among them."),
  L("Καρναβαλίστρια", "f", "Το πλήρωμά μας είναι σαράντα άτομα, φίλοι από το σχολείο. Φέτος είμαστε ντυμένοι αστροναύτες. Ράβαμε τις στολές κάθε βράδυ από τον Ιανουάριο. Το καρναβάλι για εμάς δεν είναι μία μέρα· είναι δύο μήνες πρόβες, πάρτι και κούραση. Και του χρόνου πάλι!", "Our crew is forty people, friends from school. This year we're dressed as astronauts. We sewed the costumes every evening from January. For us the carnival isn't one day; it's two months of rehearsals, parties and exhaustion. And again next year!"),
  L("Δημοσιογράφος", "m", "Τα άρματα, που συχνά σατιρίζουν πολιτικούς και την επικαιρότητα, τα κατασκευάζουν εδώ και δεκαετίες ειδικοί τεχνίτες σε ένα μεγάλο εργαστήριο της πόλης. Το βράδυ η γιορτή κορυφώνεται στο λιμάνι, με το κάψιμο του καρνάβαλου, του μεγάλου ομοιώματος που συμβολίζει το τέλος της Αποκριάς, και με πυροτεχνήματα. Την επομένη, Καθαρά Δευτέρα, η πόλη θα ξυπνήσει κουρασμένη και θα πάει να πετάξει χαρταετό.", "The floats, which often satirise politicians and current affairs, have been built for decades by specialist craftsmen in a large workshop in the city. In the evening the celebration reaches its climax at the harbour, with the burning of the carnival king, the large effigy that symbolises the end of Carnival, and with fireworks. The next day, Clean Monday, the city will wake up tired and go to fly kites."),
 ],
 "questions": [
  Q("Πώς είναι οργανωμένοι οι καρναβαλιστές;", ["Σε σχολικές τάξεις", "Σε πληρώματα", "Σε ομάδες ανά γειτονιά", "Ατομικά"], 1, "χωρισμένοι σε πληρώματα"),
  Q("Τι σημαίνει για την καρναβαλίστρια το καρναβάλι;", ["Μία μέρα διασκέδασης", "Δύο μήνες προετοιμασίας, πρόβες και πάρτι", "Μια ευκαιρία να βγάλει χρήματα", "Μια σχολική υποχρέωση"], 1, "είναι δύο μήνες πρόβες, πάρτι και κούραση"),
  Q("Πώς κορυφώνεται η γιορτή το βράδυ;", ["Με μια συναυλία στην πλατεία", "Με το κάψιμο του καρνάβαλου και πυροτεχνήματα στο λιμάνι", "Με χαρταετούς", "Με έναν αγώνα στολών"], 1, "κορυφώνεται στο λιμάνι, με το κάψιμο του καρνάβαλου"),
 ],
 "gloss": {"καρναβαλιού": "καρναβάλι — carnival", "Αποκριάς": "Αποκριά — Carnival season", "πληρώματα": "πλήρωμα — crew", "παρελαύνουν": "παρελαύνω — to parade", "στολές": "στολή — costume", "άρματα": "άρμα — float", "πρόβες": "πρόβα — rehearsal", "σατιρίζουν": "σατιρίζω — to satirise", "κορυφώνεται": "κορυφώνομαι — to reach a climax", "ομοιώματος": "ομοίωμα — effigy", "πυροτεχνήματα": "πυροτέχνημα — firework", "χαρταετό": "χαρταετός — kite"},
})

ITEMS.append({
 "id": "l37-rep-mastichochoria", "title": "Τα Μαστιχοχώρια της Χίου", "title_en": "The mastic villages of Chios", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από ένα χωριό της νότιας Χίου την εποχή της συλλογής της μαστίχας.",
 "script": [
  L("Δημοσιογράφος", "f", "Είναι Αύγουστος, και στα κτήματα γύρω από τα Μαστιχοχώρια της νότιας Χίου οι παραγωγοί σκύβουν από το πρωί κάτω από τους σχίνους. Με ένα μικρό εργαλείο χαράζουν τον κορμό, και από τις πληγές τρέχει ένα διάφανο ρετσίνι, που σε λίγες μέρες στερεοποιείται σε μικρά κομμάτια: τα «δάκρυα» της μαστίχας.", "It's August, and in the fields around the mastic villages of southern Chios the growers have been bending under the mastic trees since morning. With a small tool they score the trunk, and from the wounds runs a clear resin, which in a few days hardens into small pieces: the 'tears' of mastic."),
  L("Παραγωγός", "m", "Πριν χαράξουμε, καθαρίζουμε και στρώνουμε το χώμα κάτω από το δέντρο με άσπρο χώμα, για να πέφτουν τα δάκρυα καθαρά. Μετά τα μαζεύουμε με το χέρι και τα καθαρίζουμε στο σπίτι, όλη η οικογένεια, τα βράδια του χειμώνα. Είναι δουλειά υπομονής. Ο σχίνος βγάζει μαστίχα μόνο εδώ, στη νότια Χίο· τον έχουν φυτέψει και αλλού, αλλά δεν δίνει.", "Before scoring, we clean and level the ground under the tree with white earth, so that the tears fall clean. Then we collect them one by one and clean them at home, the whole family, on winter evenings. It's work that needs patience. The mastic tree only produces mastic here, in southern Chios; it's been planted elsewhere too, but it doesn't yield."),
  L("Δημοσιογράφος", "f", "Η μαστίχα Χίου είναι προϊόν προστατευόμενης ονομασίας προέλευσης, και η τεχνογνωσία της καλλιέργειάς της έχει ενταχθεί στον κατάλογο της UNESCO για την άυλη πολιτιστική κληρονομιά. Χρησιμοποιείται σε γλυκά, ποτά και καλλυντικά, αλλά και στη φαρμακευτική. Τα χωριά όπως το Πυργί, με τα ασπρόμαυρα σχέδια στους τοίχους των σπιτιών, τα ξυστά, προσελκύουν όλο και περισσότερους επισκέπτες.", "Chios mastic is a product of protected designation of origin, and the know-how of its cultivation has been included in UNESCO's list of intangible cultural heritage. It is used in sweets, drinks and cosmetics, but also in pharmaceuticals. Villages like Pyrgi, with the black-and-white patterns on the walls of the houses, the xysta, attract more and more visitors."),
 ],
 "questions": [
  Q("Πώς βγαίνει η μαστίχα από το δέντρο;", ["Κόβοντας τα κλαδιά", "Χαράζοντας τον κορμό, από όπου τρέχει ρετσίνι", "Βράζοντας τα φύλλα", "Μαζεύοντας τους καρπούς"], 1, "χαράζουν τον κορμό, και από τις πληγές τρέχει ένα διάφανο ρετσίνι"),
  Q("Γιατί στρώνουν άσπρο χώμα κάτω από τα δέντρα;", ["Για να μη φυτρώνουν χόρτα", "Για να πέφτουν τα δάκρυα καθαρά", "Για να μην καίγεται το δέντρο", "Για διακόσμηση"], 1, "για να πέφτουν τα δάκρυα καθαρά"),
  Q("Τι λέει ο παραγωγός για τον σχίνο σε άλλες περιοχές;", ["Δίνει περισσότερη μαστίχα", "Δεν δίνει μαστίχα έξω από τη νότια Χίο", "Δεν μπορεί να φυτευτεί", "Δίνει μαστίχα άλλου χρώματος"], 1, "τον έχουν φυτέψει και αλλού, αλλά δεν δίνει"),
 ],
 "gloss": {"μαστίχας": "μαστίχα — mastic", "Μαστιχοχώρια": "Μαστιχοχώρια — the mastic villages", "σχίνους": "σχίνος — mastic tree", "χαράζουν": "χαράζω — to score, cut", "κορμό": "κορμός — trunk", "ρετσίνι": "ρετσίνι — resin", "στερεοποιείται": "στερεοποιούμαι — to harden, solidify", "προστατευόμενης ονομασίας προέλευσης": "προστατευόμενη ονομασία προέλευσης — protected designation of origin", "τεχνογνωσία": "τεχνογνωσία — know-how", "άυλη πολιτιστική κληρονομιά": "άυλη πολιτιστική κληρονομιά — intangible cultural heritage", "ξυστά": "ξυστά — sgraffito wall decorations (Chios)"},
})

ITEMS.append({
 "id": "l37-int-metafrastria", "title": "Μια μεταφράστρια λογοτεχνίας", "title_en": "A literary translator", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια μεταφράστρια που μεταφράζει ελληνική λογοτεχνία στα ισπανικά.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς αποφασίσατε να γίνετε μεταφράστρια ελληνικής λογοτεχνίας;", "How did you decide to become a translator of Greek literature?"),
  L("Μεταφράστρια", "f", "Τυχαία. Γεννήθηκα στη Μαδρίτη και ήρθα στην Αθήνα για ένα εξάμηνο Erasmus. Ένας φίλος μού χάρισε τις «Ποιήσεις» του Καβάφη, και κάθισα ένα ολόκληρο χειμώνα να τις μεταφράζω για μένα, με ένα λεξικό στο ένα χέρι. Δεν ήξερα τότε ότι αυτό θα γινόταν το επάγγελμά μου.", "By chance. I was born in Madrid and came to Athens for an Erasmus semester. A friend gave me Cavafy's 'Poems' as a gift, and I spent a whole winter translating them for myself, with a dictionary in one hand. I didn't know then that this would become my profession."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο δύσκολο στη μετάφραση;", "What is the hardest thing in translation?"),
  L("Μεταφράστρια", "f", "Όχι οι δύσκολες λέξεις, αυτές τις βρίσκεις στο λεξικό. Το δύσκολο είναι ο ρυθμός, το χιούμορ και όσα εννοούνται χωρίς να λέγονται. Πώς μεταφράζεις το «φιλότιμο» ή ένα «άντε γεια» που σημαίνει δέκα πράγματα μαζί; Συχνά πρέπει να απομακρυνθείς από τις λέξεις για να μείνεις πιστή στο νόημα. Ένας καλός μεταφραστής δεν είναι αόρατος· είναι ένας προσεκτικός συγγραφέας που ξέρει να κρύβεται.", "Not the difficult words; those you find in the dictionary. The difficult thing is the rhythm, the humour and everything that's meant without being said. How do you translate 'filotimo', or an 'ánte geia' that means ten things at once? Often you have to move away from the words in order to stay faithful to the meaning. A good translator isn't invisible; they are a careful writer who knows how to hide."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε να μεταφράζει;", ["Σπούδασε μετάφραση στη Μαδρίτη", "Μετέφραζε για τον εαυτό της ποιήματα του Καβάφη που της χάρισε ένας φίλος", "Της το ζήτησε ένας εκδοτικός οίκος", "Δούλευε σε πρεσβεία"], 1, "Ένας φίλος μού χάρισε τις «Ποιήσεις» του Καβάφη"),
  Q("Τι θεωρεί πιο δύσκολο στη μετάφραση;", ["Τις σπάνιες λέξεις", "Τον ρυθμό, το χιούμορ και όσα εννοούνται χωρίς να λέγονται", "Τη γραμματική", "Τις προθεσμίες"], 1, "Το δύσκολο είναι ο ρυθμός, το χιούμορ και όσα εννοούνται χωρίς να λέγονται"),
  Q("Πώς περιγράφει τον καλό μεταφραστή;", ["Ως αόρατο", "Ως προσεκτικό συγγραφέα που ξέρει να κρύβεται", "Ως ζωντανό λεξικό", "Ως δεύτερο συγγραφέα του βιβλίου"], 1, "είναι ένας προσεκτικός συγγραφέας που ξέρει να κρύβεται"),
 ],
 "gloss": {"μεταφράστρια": "μεταφράστρια — translator (f.)", "λογοτεχνίας": "λογοτεχνία — literature", "εξάμηνο": "εξάμηνο — semester", "μού χάρισε": "χαρίζω — to give as a gift", "λεξικό": "λεξικό — dictionary", "επάγγελμά": "επάγγελμα — profession", "ρυθμός": "ρυθμός — rhythm", "εννοούνται": "εννοούμαι — to be meant, implied", "φιλότιμο": "φιλότιμο — sense of honour and duty", "να απομακρυνθείς": "απομακρύνομαι — to move away", "πιστή": "πιστός — faithful", "αόρατος": "αόρατος — invisible"},
})

ITEMS.append({
 "id": "l37-mono-eikonomachia", "title": "Η Εικονομαχία", "title_en": "Iconoclasm", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια βυζαντινολόγο να μιλάει σε μια διάλεξη για την Εικονομαχία.",
 "script": [
  L("Βυζαντινολόγος", "f", "Για περισσότερο από έναν αιώνα, τον όγδοο και τις αρχές του ένατου, η Βυζαντινή Αυτοκρατορία διχάστηκε γύρω από ένα ερώτημα που σήμερα μπορεί να μας φαίνεται θεολογικό και απόμακρυ: επιτρέπεται να απεικονίζεται ο Χριστός και οι άγιοι, και να τιμώνται οι εικόνες τους;", "For more than a century, the eighth and the beginning of the ninth, the Byzantine Empire was divided over a question that today may seem theological and remote to us: is it permitted for Christ and the saints to be depicted, and for their images to be venerated?"),
  L("Βυζαντινολόγος", "f", "Οι εικονομάχοι αυτοκράτορες, με πρώτο τον Λέοντα τον Γ΄, θεωρούσαν τη λατρεία των εικόνων μορφή ειδωλολατρίας. Οι λόγοι της στάσης τους συζητούνται ακόμη: κάποιοι ιστορικοί δίνουν έμφαση στις στρατιωτικές ήττες, που ερμηνεύτηκαν ως θεϊκή τιμωρία, άλλοι στην επιθυμία του κράτους να περιορίσει τη δύναμη των μοναστηριών, τα οποία ήταν οι κύριοι υπερασπιστές των εικόνων.", "The iconoclast emperors, beginning with Leo III, considered the veneration of icons a form of idolatry. The reasons for their stance are still debated: some historians emphasise military defeats, which were interpreted as divine punishment, others the state's desire to limit the power of the monasteries, which were the main defenders of the icons."),
  L("Βυζαντινολόγος", "f", "Οφείλω να σημειώσω ότι οι πηγές μας είναι σχεδόν αποκλειστικά γραμμένες από τους νικητές, δηλαδή τους εικονόφιλους. Τα κείμενα των εικονομάχων καταστράφηκαν, και η εικόνα που έχουμε για εκείνους είναι αναπόφευκτα μονόπλευρη. Αυτό καθιστά την ιστορική κρίση ιδιαίτερα δύσκολη.", "I must note that our sources were written almost exclusively by the winners, that is the iconophiles. The iconoclasts' texts were destroyed, and the picture we have of them is inevitably one-sided. This makes historical judgement particularly difficult."),
  L("Βυζαντινολόγος", "f", "Η διαμάχη έληξε οριστικά το 843, με την αναστήλωση των εικόνων, που η Ορθόδοξη Εκκλησία γιορτάζει μέχρι σήμερα την πρώτη Κυριακή της Σαρακοστής, την Κυριακή της Ορθοδοξίας. Η κληρονομιά της Εικονομαχίας, πάντως, ξεπερνά τη θεολογία: έθεσε με οξύτητα ερωτήματα για τη σχέση της εικόνας με την πραγματικότητα, που παραμένουν επίκαιρα στην εποχή των οθονών.", "The conflict ended definitively in 843, with the restoration of the icons, which the Orthodox Church celebrates to this day on the first Sunday of Lent, the Sunday of Orthodoxy. The legacy of Iconoclasm, however, goes beyond theology: it raised sharply questions about the relationship of the image to reality, which remain topical in the age of screens."),
 ],
 "questions": [
  Q("Ποιο ήταν το κεντρικό ερώτημα της Εικονομαχίας;", ["Αν πρέπει να χτίζονται νέες εκκλησίες", "Αν επιτρέπεται η απεικόνιση και η τιμή των αγίων", "Ποια θα είναι η πρωτεύουσα της αυτοκρατορίας", "Αν οι μοναχοί πρέπει να πληρώνουν φόρους"], 1, "επιτρέπεται να απεικονίζεται ο Χριστός και οι άγιοι, και να τιμώνται οι εικόνες τους"),
  Q("Ποια εξήγηση για τη στάση των εικονομάχων αναφέρεται;", ["Η επιρροή της Δύσης", "Η επιθυμία να περιοριστεί η δύναμη των μοναστηριών", "Η έλλειψη ζωγράφων", "Η οικονομική ευημερία"], 1, "άλλοι στην επιθυμία του κράτους να περιορίσει τη δύναμη των μοναστηριών"),
  Q("Γιατί η ιστορική κρίση είναι δύσκολη, κατά την ομιλήτρια;", ["Γιατί δεν υπάρχουν καθόλου πηγές", "Γιατί οι πηγές γράφτηκαν σχεδόν μόνο από τους εικονόφιλους", "Γιατί οι πηγές είναι στα λατινικά", "Γιατί οι ιστορικοί δεν ενδιαφέρονται"], 1, "οι πηγές μας είναι σχεδόν αποκλειστικά γραμμένες από τους νικητές"),
  Q("Γιατί, κατά την ομιλήτρια, η Εικονομαχία παραμένει επίκαιρη;", ["Γιατί η διαμάχη συνεχίζεται στην Εκκλησία", "Γιατί έθεσε ερωτήματα για τη σχέση εικόνας και πραγματικότητας", "Γιατί οι εικόνες είναι πολύ ακριβές", "Γιατί απαγορεύονται ακόμη οι εικόνες"], 1, "έθεσε με οξύτητα ερωτήματα για τη σχέση της εικόνας με την πραγματικότητα"),
 ],
 "gloss": {"βυζαντινολόγο": "βυζαντινολόγος — Byzantinist", "Εικονομαχία": "Εικονομαχία — Iconoclasm", "διχάστηκε": "διχάζομαι — to be divided", "απόμακρυ": "απόμακρος — remote, distant", "να απεικονίζεται": "απεικονίζομαι — to be depicted", "εικονομάχοι": "εικονομάχος — iconoclast", "ειδωλολατρίας": "ειδωλολατρία — idolatry", "θεϊκή τιμωρία": "θεϊκή τιμωρία — divine punishment", "υπερασπιστές": "υπερασπιστής — defender", "εικονόφιλους": "εικονόφιλος — iconophile", "μονόπλευρη": "μονόπλευρος — one-sided", "αναστήλωση": "αναστήλωση — restoration", "Σαρακοστής": "Σαρακοστή — Lent", "οξύτητα": "οξύτητα — sharpness, acuteness"},
})

ITEMS.append({
 "id": "l37-int-stegastiko", "title": "Η στεγαστική κρίση", "title_en": "The housing crisis", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν οικονομολόγο για την άνοδο των ενοικίων στις ελληνικές πόλεις.",
 "script": [
  L("Δημοσιογράφος", "f", "Τα ενοίκια στην Αθήνα έχουν αυξηθεί δραματικά την τελευταία δεκαετία. Πολλοί νέοι μένουν με τους γονείς τους μέχρι τα τριάντα. Ποιες είναι οι αιτίες;", "Rents in Athens have risen dramatically over the last decade. Many young people live with their parents until thirty. What are the causes?"),
  L("Οικονομολόγος", "m", "Δεν υπάρχει μία αιτία, αλλά ένας συνδυασμός. Κατά τη διάρκεια της οικονομικής κρίσης η κατασκευή νέων κατοικιών σχεδόν σταμάτησε, οπότε η προσφορά έμεινε στάσιμη. Ταυτόχρονα, ένα σημαντικό μέρος του υπάρχοντος αποθέματος αποσύρθηκε από τη μακροχρόνια μίσθωση και διατέθηκε σε βραχυχρόνιες μισθώσεις για τουρίστες. Προσθέστε τα προγράμματα που δίνουν άδεια διαμονής σε ξένους επενδυτές που αγοράζουν ακίνητα, και έχετε μια αγορά όπου η ζήτηση ξεπερνά κατά πολύ την προσφορά.", "There isn't one cause, but a combination. During the economic crisis the construction of new homes almost stopped, so supply stagnated. At the same time, a significant part of the existing stock was withdrawn from long-term renting and made available for short-term lets to tourists. Add the schemes that grant residence permits to foreign investors who buy property, and you have a market where demand far exceeds supply."),
  L("Δημοσιογράφος", "f", "Θα έπρεπε, λοιπόν, να απαγορευτούν οι βραχυχρόνιες μισθώσεις;", "Should short-term lets be banned, then?"),
  L("Οικονομολόγος", "m", "Οι απαγορεύσεις σπάνια λειτουργούν όπως ελπίζουμε. Για πολλές οικογένειες, το εισόδημα από ένα διαμέρισμα στον τουρισμό είναι σημαντικό συμπλήρωμα σε χαμηλούς μισθούς. Πιστεύω περισσότερο σε στοχευμένα μέτρα: περιορισμούς στις πιο επιβαρυμένες γειτονιές, κίνητρα για να επιστρέψουν τα κλειστά σπίτια στην αγορά, και κυρίως κοινωνική κατοικία, που στην Ελλάδα είναι σχεδόν ανύπαρκτη σε σύγκριση με άλλες ευρωπαϊκές χώρες.", "Bans rarely work as we hope. For many families, income from a flat in tourism is an important supplement to low wages. I believe more in targeted measures: restrictions in the most overburdened neighbourhoods, incentives for closed-up homes to return to the market, and above all social housing, which in Greece is almost non-existent compared with other European countries."),
  L("Δημοσιογράφος", "f", "Γιατί είναι τόσο σημαντική η κοινωνική κατοικία;", "Why is social housing so important?"),
  L("Οικονομολόγος", "m", "Γιατί η στέγη δεν είναι απλώς ένα εμπόρευμα. Όταν ένας νέος δεν μπορεί να βρει σπίτι, αναβάλλει την οικογένεια, την αλλαγή δουλειάς, πολλές φορές φεύγει στο εξωτερικό. Το κόστος, δηλαδή, δεν το πληρώνει μόνο ο ίδιος, αλλά ολόκληρη η κοινωνία.", "Because housing isn't simply a commodity. When a young person can't find a home, they postpone a family, a change of job, and often they leave for abroad. The cost, in other words, isn't paid only by them, but by society as a whole."),
 ],
 "questions": [
  Q("Τι συνέβη στην κατασκευή κατοικιών κατά την κρίση;", ["Αυξήθηκε σημαντικά", "Σχεδόν σταμάτησε", "Έμεινε σταθερή", "Πέρασε στο κράτος"], 1, "η κατασκευή νέων κατοικιών σχεδόν σταμάτησε"),
  Q("Ποιο από τα παρακάτω ΔΕΝ αναφέρεται ως αιτία της ανόδου των ενοικίων;", ["Οι βραχυχρόνιες μισθώσεις", "Η αύξηση του πληθυσμού λόγω γεννήσεων", "Η στάσιμη προσφορά", "Οι άδειες διαμονής για επενδυτές"], 1, "Δεν υπάρχει μία αιτία, αλλά ένας συνδυασμός"),
  Q("Γιατί ο οικονομολόγος δεν υποστηρίζει γενική απαγόρευση;", ["Γιατί θα έβλαπτε τον τουρισμό των νησιών", "Γιατί για πολλές οικογένειες είναι σημαντικό συμπληρωματικό εισόδημα", "Γιατί είναι αντισυνταγματική", "Γιατί δεν θα άλλαζε τίποτα"], 1, "το εισόδημα από ένα διαμέρισμα στον τουρισμό είναι σημαντικό συμπλήρωμα"),
  Q("Γιατί, κατά τον οικονομολόγο, η στέγη «δεν είναι απλώς ένα εμπόρευμα»;", ["Γιατί ανήκει στο κράτος", "Γιατί όταν οι νέοι δεν βρίσκουν σπίτι, το κόστος το πληρώνει όλη η κοινωνία", "Γιατί δεν μπορεί να πουληθεί", "Γιατί οι τιμές της δεν αλλάζουν"], 1, "Το κόστος, δηλαδή, δεν το πληρώνει μόνο ο ίδιος, αλλά ολόκληρη η κοινωνία"),
 ],
 "gloss": {"οικονομολόγο": "οικονομολόγος — economist", "ενοικίων": "ενοίκιο — rent", "κατοικιών": "κατοικία — dwelling, home", "προσφορά": "προσφορά — supply", "στάσιμη": "στάσιμος — stagnant", "αποθέματος": "απόθεμα — stock", "αποσύρθηκε": "αποσύρομαι — to be withdrawn", "άδεια διαμονής": "άδεια διαμονής — residence permit", "ακίνητα": "ακίνητο — property", "ζήτηση": "ζήτηση — demand", "στοχευμένα": "στοχευμένος — targeted", "επιβαρυμένες": "επιβαρυμένος — overburdened", "κοινωνική κατοικία": "κοινωνική κατοικία — social housing", "εμπόρευμα": "εμπόρευμα — commodity"},
})

rnd = random.Random(37)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-37.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
