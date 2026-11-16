# Source for library/listening/listening-56.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l56.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l56-ann-teleferik", "title": "Διακοπή λειτουργίας του τελεφερίκ", "title_en": "The funicular is out of service", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στον κάτω σταθμό του τελεφερίκ του Λυκαβηττού. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Ανακοίνωση", "f", "Αγαπητοί επισκέπτες, σας ενημερώνουμε ότι λόγω των ισχυρών ανέμων που πνέουν αυτή τη στιγμή στην περιοχή, η λειτουργία του τελεφερίκ διακόπτεται προσωρινά για λόγους ασφαλείας. Σύμφωνα με την πρόγνωση, οι άνεμοι αναμένεται να εξασθενήσουν μετά τις τέσσερις το απόγευμα.", "Dear visitors, we inform you that because of the strong winds currently blowing in the area, the funicular is temporarily suspended for safety reasons. According to the forecast, the winds are expected to weaken after four in the afternoon."),
  L("Ανακοίνωση", "f", "Όσοι έχουν ήδη αγοράσει εισιτήριο μπορούν να το χρησιμοποιήσουν οποιαδήποτε άλλη μέρα μέσα στον επόμενο μήνα ή να ζητήσουν επιστροφή χρημάτων από το εκδοτήριο. Για όσους επιθυμούν να ανέβουν με τα πόδια, το μονοπάτι ξεκινά από την οδό Αριστίππου και η ανάβαση διαρκεί περίπου τριάντα λεπτά.", "Those who have already bought a ticket can use it on any other day within the next month or ask for a refund at the ticket office. For those who wish to walk up, the path starts from Aristippou Street and the climb takes about thirty minutes."),
  L("Ανακοίνωση", "f", "Σας παρακαλούμε να μη χρησιμοποιήσετε το μονοπάτι αν έχετε μικρά παιδιά ή κινητικές δυσκολίες, γιατί σε ορισμένα σημεία είναι απότομο. Ευχαριστούμε για την κατανόηση.", "Please do not use the path if you have small children or reduced mobility, because in places it is steep. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί διακόπτεται η λειτουργία του τελεφερίκ;", ["Λόγω βλάβης", "Λόγω ισχυρών ανέμων", "Λόγω απεργίας", "Λόγω εργασιών συντήρησης"], 1, "λόγω των ισχυρών ανέμων … η λειτουργία του τελεφερίκ διακόπτεται προσωρινά"),
  Q("Τι μπορούν να κάνουν όσοι έχουν ήδη εισιτήριο;", ["Να ανέβουν με ταξί δωρεάν", "Να το χρησιμοποιήσουν άλλη μέρα μέσα σε έναν μήνα ή να πάρουν πίσω τα χρήματα", "Να περιμένουν μέχρι το βράδυ", "Τίποτα, δεν επιστρέφονται χρήματα"], 1, "μπορούν να το χρησιμοποιήσουν οποιαδήποτε άλλη μέρα μέσα στον επόμενο μήνα ή να ζητήσουν επιστροφή χρημάτων"),
  Q("Ποιοι δεν πρέπει να ανέβουν από το μονοπάτι;", ["Οι τουρίστες", "Όσοι έχουν μικρά παιδιά ή κινητικές δυσκολίες", "Όσοι δεν έχουν εισιτήριο", "Όσοι έχουν σκύλο"], 1, "να μη χρησιμοποιήσετε το μονοπάτι αν έχετε μικρά παιδιά ή κινητικές δυσκολίες"),
 ],
 "gloss": {"τελεφερίκ": "τελεφερίκ — cable railway, funicular (colloquial)", "πνέουν": "πνέω — to blow (of wind)", "διακόπτεται": "διακόπτομαι — to be suspended, interrupted", "εξασθενήσουν": "εξασθενώ — to weaken", "επιστροφή χρημάτων": "επιστροφή χρημάτων — refund", "ανάβαση": "ανάβαση — climb, ascent", "απότομο": "απότομος — steep"},
})

ITEMS.append({
 "id": "l56-vm-ekdotis", "title": "Μήνυμα από τον εκδότη", "title_en": "A message from the publisher", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε γράψει ένα βιβλίο με παιδικά παραμύθια. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τον εκδότη σας.",
 "script": [
  L("Εκδότης", "m", "Καλημέρα, Ρούλα, ο Τηλέμαχος από τις εκδόσεις «Πυξίδα». Έχω καλά νέα! Διαβάσαμε όλοι το χειρόγραφό σου και ενθουσιαστήκαμε. Θέλουμε να εκδώσουμε τα παραμύθια σου την άνοιξη, για την Έκθεση Βιβλίου.", "Good morning, Roula, it's Tilemachos from Pyxida publishers. I have good news! We have all read your manuscript and we loved it. We want to publish your fairy tales in the spring, for the Book Fair."),
  L("Εκδότης", "m", "Έχουμε, βέβαια, και δύο-τρεις προτάσεις. Η επιμελήτριά μας πιστεύει ότι το τρίτο παραμύθι είναι λίγο μεγάλο για παιδιά πέντε χρονών και θα ήθελε να το συντομεύσεις. Επίσης, σκεφτόμαστε να αναθέσουμε την εικονογράφηση στη Νεφέλη Σταύρου, αν συμφωνείς. Θα σου στείλω με ηλεκτρονικό ταχυδρομείο μερικά σχέδιά της να τα δεις.", "We do, of course, have two or three suggestions. Our editor thinks the third tale is a bit long for five-year-olds and would like you to shorten it. Also, we're thinking of giving the illustrations to Nefeli Stavrou, if you agree. I'll email you some of her drawings to look at."),
  L("Εκδότης", "m", "Θα ήθελα να συναντηθούμε την επόμενη εβδομάδα στα γραφεία μας για να υπογράψουμε το συμβόλαιο. Πες μου ποια μέρα σε βολεύει. Και συγχαρητήρια!", "I'd like us to meet next week at our offices to sign the contract. Tell me which day suits you. And congratulations!"),
 ],
 "questions": [
  Q("Πότε θέλει ο εκδότης να κυκλοφορήσει το βιβλίο;", ["Τα Χριστούγεννα", "Την άνοιξη, για την Έκθεση Βιβλίου", "Το καλοκαίρι", "Τον επόμενο μήνα"], 1, "Θέλουμε να εκδώσουμε τα παραμύθια σου την άνοιξη, για την Έκθεση Βιβλίου"),
  Q("Τι ζητά η επιμελήτρια;", ["Να προστεθεί ένα παραμύθι", "Να συντομευτεί το τρίτο παραμύθι", "Να αλλάξει ο τίτλος", "Να γραφτεί ένας πρόλογος"], 1, "το τρίτο παραμύθι είναι λίγο μεγάλο για παιδιά πέντε χρονών και θα ήθελε να το συντομεύσεις"),
  Q("Γιατί θέλει να συναντηθούν την επόμενη εβδομάδα;", ["Για να γνωρίσει την εικονογράφο", "Για να υπογράψουν το συμβόλαιο", "Για μια παρουσίαση του βιβλίου", "Για να διορθώσουν το κείμενο"], 1, "να συναντηθούμε την επόμενη εβδομάδα στα γραφεία μας για να υπογράψουμε το συμβόλαιο"),
 ],
 "gloss": {"χειρόγραφό": "χειρόγραφο — manuscript", "ενθουσιαστήκαμε": "ενθουσιάζομαι — to be thrilled", "εκδώσουμε": "εκδίδω — to publish", "επιμελήτριά": "επιμελήτρια — (female) editor", "συντομεύσεις": "συντομεύω — to shorten", "αναθέσουμε": "αναθέτω — to assign, entrust", "εικονογράφηση": "εικονογράφηση — illustration", "συμβόλαιο": "συμβόλαιο — contract"},
})

ITEMS.append({
 "id": "l56-dia-piata", "title": "Ποιος θα πλύνει τα πιάτα;", "title_en": "Who's going to do the dishes?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φοιτητές που μοιράζονται ένα διαμέρισμα συζητούν για τις δουλειές του σπιτιού. Θα ακούσετε τη συζήτησή τους.",
 "script": [
  L("Ζωή", "f", "Αντώνη, πρέπει να μιλήσουμε. Ο νεροχύτης είναι πάλι γεμάτος πιάτα από χθες. Και δεν είναι δικά μου.", "Antonis, we need to talk. The sink is full of dishes again from yesterday. And they aren't mine."),
  L("Αντώνης", "m", "Συγγνώμη, είχα εξεταστική όλη την εβδομάδα. Θα τα πλύνω απόψε, το υπόσχομαι.", "Sorry, I've had exams all week. I'll wash them tonight, I promise."),
  L("Ζωή", "f", "Αυτό είπες και την προηγούμενη φορά. Δεν θέλω να μαλώνουμε κάθε τρεις και λίγο. Λέω να φτιάξουμε ένα πρόγραμμα: ποιος κάνει τι και ποια μέρα. Να το κολλήσουμε στο ψυγείο.", "That's what you said last time. I don't want us to argue every five minutes. I say we make a schedule: who does what and on which day. We can stick it on the fridge."),
  L("Αντώνης", "m", "Εντάξει, καλή ιδέα. Εγώ προτιμώ να αναλάβω τα ψώνια και τα σκουπίδια, κι αν θέλεις, το μπάνιο κάθε Σάββατο. Τα πιάτα να τα πλένει όποιος μαγειρεύει;", "OK, good idea. I'd rather take on the shopping and the rubbish, and if you like, the bathroom every Saturday. Whoever cooks washes the dishes?"),
  L("Ζωή", "f", "Όχι, ανάποδα: όποιος μαγειρεύει δεν πλένει. Αλλιώς δεν θα μαγειρεύει κανείς! Και να βάζουμε κι ένα πλυντήριο πιάτων κάθε βράδυ, να μη μαζεύονται.", "No, the other way round: whoever cooks doesn't wash up. Otherwise nobody will cook! And let's run the dishwasher every evening, so they don't pile up."),
 ],
 "questions": [
  Q("Γιατί είναι θυμωμένη η Ζωή;", ["Γιατί ο Αντώνης έκανε θόρυβο", "Γιατί ο νεροχύτης είναι πάλι γεμάτος πιάτα του Αντώνη", "Γιατί χάλασε το πλυντήριο", "Γιατί ο Αντώνης δεν πλήρωσε το νοίκι"], 1, "Ο νεροχύτης είναι πάλι γεμάτος πιάτα από χθες. Και δεν είναι δικά μου"),
  Q("Τι προτείνει η Ζωή;", ["Να πάρουν καθαρίστρια", "Να φτιάξουν ένα πρόγραμμα με τις δουλειές", "Να τρώνε έξω", "Να αλλάξουν σπίτι"], 1, "Λέω να φτιάξουμε ένα πρόγραμμα: ποιος κάνει τι και ποια μέρα"),
  Q("Ποιος κανόνας ισχύει τελικά για τα πιάτα;", ["Τα πλένει όποιος μαγειρεύει", "Δεν τα πλένει όποιος μαγειρεύει", "Τα πλένει πάντα ο Αντώνης", "Τα πλένουν μαζί κάθε βράδυ"], 1, "όποιος μαγειρεύει δεν πλένει"),
 ],
 "gloss": {"νεροχύτης": "νεροχύτης — (kitchen) sink", "εξεταστική": "εξεταστική — exam period", "κάθε τρεις και λίγο": "κάθε τρεις και λίγο — every five minutes, constantly", "αναλάβω": "αναλαμβάνω — to take on", "ανάποδα": "ανάποδα — the other way round", "πλυντήριο πιάτων": "πλυντήριο πιάτων — dishwasher"},
})

ITEMS.append({
 "id": "l56-dia-papoutsia", "title": "Επιστροφή παπουτσιών", "title_en": "Returning shoes", "type": "dialogue", "level": "B2",
 "context_el": "Μια πελάτισσα επιστρέφει σε ένα κατάστημα υποδημάτων. Θα ακούσετε τη συζήτησή της με τον υπάλληλο.",
 "script": [
  L("Πελάτισσα", "f", "Καλησπέρα. Αγόρασα αυτά τα παπούτσια πριν από δέκα μέρες, αλλά ήδη ξεκόλλησε η σόλα στο αριστερό. Τα φόρεσα μόνο τρεις φορές.", "Good afternoon. I bought these shoes ten days ago, but the sole on the left one has already come unstuck. I've only worn them three times."),
  L("Υπάλληλος", "m", "Ας τα δω... Ναι, πράγματι, είναι κατασκευαστικό ελάττωμα. Έχετε την απόδειξη;", "Let me see... Yes, indeed, it's a manufacturing defect. Do you have the receipt?"),
  L("Πελάτισσα", "f", "Ορίστε. Θα ήθελα να μου επιστρέψετε τα χρήματα, γιατί δεν εμπιστεύομαι πια αυτό το μοντέλο.", "Here you are. I'd like you to give me my money back, because I don't trust this model any more."),
  L("Υπάλληλος", "m", "Καταλαβαίνω. Η πολιτική του καταστήματος είναι να δίνουμε πιστωτικό σημείωμα, αλλά στην περίπτωση ελαττωματικού προϊόντος δικαιούστε επιστροφή χρημάτων. Θα σας τα επιστρέψω στην κάρτα με την οποία πληρώσατε.", "I understand. The shop's policy is to give a credit note, but in the case of a defective product you are entitled to a refund. I'll refund it to the card you paid with."),
  L("Πελάτισσα", "f", "Τέλεια, ευχαριστώ. Και σε πόσες μέρες θα φανούν τα χρήματα στον λογαριασμό μου;", "Perfect, thank you. And in how many days will the money show up in my account?"),
  L("Υπάλληλος", "m", "Συνήθως σε τρεις με πέντε εργάσιμες. Αν δεν εμφανιστούν, πάρτε μας τηλέφωνο.", "Usually in three to five working days. If it doesn't appear, give us a call."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με τα παπούτσια;", ["Είναι μικρά", "Ξεκόλλησε η σόλα στο αριστερό", "Δεν της αρέσει το χρώμα", "Της χτυπάνε"], 1, "ήδη ξεκόλλησε η σόλα στο αριστερό"),
  Q("Γιατί δικαιούται η πελάτισσα επιστροφή χρημάτων;", ["Γιατί έχει κάρτα πελάτη", "Γιατί το προϊόν είναι ελαττωματικό", "Γιατί είναι ακόμη εκπτώσεις", "Γιατί δεν τα φόρεσε ποτέ"], 1, "στην περίπτωση ελαττωματικού προϊόντος δικαιούστε επιστροφή χρημάτων"),
  Q("Σε πόσο καιρό θα δει τα χρήματα στον λογαριασμό της;", ["Αμέσως", "Σε τρεις με πέντε εργάσιμες", "Σε έναν μήνα", "Την επόμενη εβδομάδα, μόνο αν τηλεφωνήσει"], 1, "Συνήθως σε τρεις με πέντε εργάσιμες"),
 ],
 "gloss": {"υποδημάτων": "υπόδημα — shoe (formal)", "ξεκόλλησε": "ξεκολλάω — to come unstuck", "σόλα": "σόλα — sole", "κατασκευαστικό ελάττωμα": "κατασκευαστικό ελάττωμα — manufacturing defect", "απόδειξη": "απόδειξη — receipt", "πιστωτικό σημείωμα": "πιστωτικό σημείωμα — credit note", "δικαιούστε": "δικαιούμαι — to be entitled to", "εργάσιμες": "εργάσιμη (μέρα) — working day"},
})

ITEMS.append({
 "id": "l56-int-magos", "title": "Ένας ταχυδακτυλουργός", "title_en": "A magician", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν ταχυδακτυλουργό.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Μαυρίδη, πώς γίνεται κανείς ταχυδακτυλουργός;", "Mr Mavridis, how does one become a magician?"),
  L("Ταχυδακτυλουργός", "m", "Στην περίπτωσή μου, όλα ξεκίνησαν με ένα δώρο. Στα δέκα μου γενέθλια ο θείος μου μού χάρισε ένα κουτί με μαγικά κόλπα. Από τότε δεν σταμάτησα ποτέ να εξασκούμαι. Πήγαινα σε σεμινάρια, διάβαζα βιβλία, και φυσικά περνούσα ώρες μπροστά στον καθρέφτη.", "In my case, it all started with a present. On my tenth birthday my uncle gave me a box of magic tricks. Since then I've never stopped practising. I went to seminars, read books and of course spent hours in front of the mirror."),
  L("Δημοσιογράφος", "f", "Πόσο χρόνο χρειάζεται για να μάθει κανείς ένα καινούργιο κόλπο;", "How long does it take to learn a new trick?"),
  L("Ταχυδακτυλουργός", "m", "Εξαρτάται. Ένα απλό κόλπο με τράπουλα μπορεί να το μάθεις σε μια εβδομάδα. Για να το κάνεις όμως τόσο φυσικά ώστε να μην το καταλάβει κανείς, χρειάζονται μήνες. Το μυστικό δεν είναι τα γρήγορα χέρια, όπως πιστεύουν οι περισσότεροι. Είναι η ψυχολογία: να ξέρεις πού κοιτάζει ο θεατής και να του αποσπάς την προσοχή.", "It depends. A simple card trick you might learn in a week. But to do it so naturally that nobody notices, you need months. The secret isn't quick hands, as most people think. It's psychology: knowing where the spectator is looking and distracting their attention."),
  L("Δημοσιογράφος", "f", "Ποιο είναι το αγαπημένο σας κοινό;", "What is your favourite audience?"),
  L("Ταχυδακτυλουργός", "m", "Τα παιδιά, χωρίς αμφιβολία, αλλά είναι και το πιο δύσκολο. Οι μεγάλοι προσπαθούν να καταλάβουν το κόλπο· τα παιδιά απλώς σου λένε δυνατά «το έκρυψες στο μανίκι!» Δεν μπορείς να τα ξεγελάσεις εύκολα.", "Children, without a doubt, but they're also the hardest. Grown-ups try to work out the trick; children just tell you loudly \"you hid it up your sleeve!\" You can't fool them easily."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε να ασχολείται με τα μαγικά;", ["Είδε μια παράσταση στην τηλεόραση", "Ο θείος του τού χάρισε ένα κουτί με μαγικά κόλπα", "Ο πατέρας του ήταν ταχυδακτυλουργός", "Πήγε σε μια σχολή στο εξωτερικό"], 1, "ο θείος μου μού χάρισε ένα κουτί με μαγικά κόλπα"),
  Q("Ποιο είναι, κατά τον ίδιο, το μυστικό ενός καλού κόλπου;", ["Τα γρήγορα χέρια", "Η ψυχολογία και η απόσπαση της προσοχής", "Τα ακριβά αντικείμενα", "Η μουσική"], 1, "Το μυστικό δεν είναι τα γρήγορα χέρια … Είναι η ψυχολογία"),
  Q("Γιατί τα παιδιά είναι το πιο δύσκολο κοινό;", ["Γιατί βαριούνται γρήγορα", "Γιατί λένε δυνατά ό,τι υποψιάζονται και δεν ξεγελιούνται εύκολα", "Γιατί φοβούνται", "Γιατί δεν καταλαβαίνουν τα κόλπα"], 1, "τα παιδιά απλώς σου λένε δυνατά «το έκρυψες στο μανίκι!» Δεν μπορείς να τα ξεγελάσεις εύκολα"),
 ],
 "gloss": {"κόλπα": "κόλπο — trick", "εξασκούμαι": "εξασκούμαι — to practise", "τράπουλα": "τράπουλα — pack of cards", "αποσπάς την προσοχή": "αποσπώ την προσοχή — to distract", "μανίκι": "μανίκι — sleeve", "ξεγελάσεις": "ξεγελάω — to fool, trick"},
})

ITEMS.append({
 "id": "l56-rep-aidipsos", "title": "Τα λουτρά της Αιδηψού", "title_en": "The baths of Aidipsos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από τα Λουτρά Αιδηψού, στη βόρεια Εύβοια.",
 "script": [
  L("Ρεπόρτερ", "m", "Είναι Νοέμβριος, και όμως, εδώ στην παραλία της Αιδηψού, αρκετοί άνθρωποι κολυμπούν στη θάλασσα. Το μυστικό; Ζεστό νερό που αναβλύζει από τη γη και χύνεται στη θάλασσα, δημιουργώντας φυσικές πισίνες με θερμοκρασία που ξεπερνά τους τριάντα πέντε βαθμούς.", "It's November, and yet here on the beach at Aidipsos quite a few people are swimming in the sea. The secret? Hot water that gushes up from the ground and pours into the sea, creating natural pools at temperatures above thirty-five degrees."),
  L("Ρεπόρτερ", "m", "Οι ιαματικές πηγές της Αιδηψού είναι γνωστές από την αρχαιότητα· τις αναφέρει ήδη ο Αριστοτέλης. Το νερό τους είναι πλούσιο σε μεταλλικά στοιχεία και, σύμφωνα με τους ειδικούς, βοηθά σε παθήσεις των αρθρώσεων και του δέρματος. Στις αρχές του εικοστού αιώνα η πόλη έγινε ένα από τα πιο κοσμικά θέρετρα της χώρας.", "The healing springs of Aidipsos have been known since antiquity; Aristotle already mentions them. Their water is rich in minerals and, according to specialists, helps with joint and skin conditions. In the early twentieth century the town became one of the most fashionable resorts in the country."),
  L("Ρεπόρτερ", "m", "Σήμερα, εκτός από τα πολυτελή ξενοδοχεία με ιδιωτικά λουτρά, υπάρχουν και δημόσιες εγκαταστάσεις με προσιτές τιμές. Οι περισσότεροι επισκέπτες είναι ηλικιωμένοι, αλλά τελευταία έρχονται όλο και περισσότεροι νέοι, ειδικά τα χειμωνιάτικα Σαββατοκύριακα. Ένας από αυτούς μου είπε γελώντας: «Πού αλλού μπορείς να κάνεις μπάνιο στη θάλασσα τον Δεκέμβριο;»", "Today, besides the luxury hotels with private baths, there are also public facilities at affordable prices. Most visitors are elderly, but lately more and more young people are coming, especially on winter weekends. One of them told me, laughing: \"Where else can you swim in the sea in December?\""),
 ],
 "questions": [
  Q("Γιατί κολυμπούν άνθρωποι στη θάλασσα τον Νοέμβριο;", ["Γιατί είναι χειμερινοί κολυμβητές", "Γιατί ζεστό νερό από τη γη χύνεται στη θάλασσα", "Γιατί υπάρχει θερμαινόμενη πισίνα στην παραλία", "Γιατί ο καιρός είναι πολύ ζεστός"], 1, "Ζεστό νερό που αναβλύζει από τη γη και χύνεται στη θάλασσα"),
  Q("Σε τι βοηθά, κατά τους ειδικούς, το νερό των πηγών;", ["Στον ύπνο", "Σε παθήσεις των αρθρώσεων και του δέρματος", "Στην πέψη", "Στην όραση"], 1, "βοηθά σε παθήσεις των αρθρώσεων και του δέρματος"),
  Q("Τι έχει αλλάξει τελευταία στους επισκέπτες;", ["Έρχονται μόνο το καλοκαίρι", "Έρχονται όλο και περισσότεροι νέοι", "Έρχονται λιγότεροι ξένοι", "Έρχονται μόνο ηλικιωμένοι"], 1, "τελευταία έρχονται όλο και περισσότεροι νέοι"),
 ],
 "gloss": {"αναβλύζει": "αναβλύζω — to gush up, well up", "ιαματικές πηγές": "ιαματικές πηγές — healing (thermal) springs", "μεταλλικά στοιχεία": "μεταλλικά στοιχεία — minerals", "παθήσεις": "πάθηση — condition, ailment", "αρθρώσεων": "άρθρωση — joint", "κοσμικά": "κοσμικός — fashionable, society", "θέρετρα": "θέρετρο — resort", "προσιτές": "προσιτός — affordable"},
})

ITEMS.append({
 "id": "l56-dia-ekloges", "title": "Στο εκλογικό τμήμα", "title_en": "At the polling station", "type": "dialogue", "level": "B2",
 "context_el": "Μια νέα ψηφοφόρος πηγαίνει να ψηφίσει για πρώτη φορά. Θα ακούσετε τη συζήτησή της με τον δικαστικό αντιπρόσωπο.",
 "script": [
  L("Ψηφοφόρος", "f", "Καλημέρα. Είναι η πρώτη φορά που ψηφίζω και δεν ξέρω ακριβώς τι πρέπει να κάνω. Είμαι στο σωστό εκλογικό τμήμα;", "Good morning. It's the first time I'm voting and I don't know exactly what I have to do. Am I at the right polling station?"),
  L("Αντιπρόσωπος", "m", "Καλημέρα σας, και καλώς ήρθατε! Δώστε μου την ταυτότητά σας να σας βρω στον εκλογικό κατάλογο. Μάλιστα, είστε εδώ. Υπογράψτε, παρακαλώ, δίπλα στο όνομά σας.", "Good morning, and welcome! Give me your ID card so I can find you on the electoral roll. Yes, you're here. Please sign next to your name."),
  L("Ψηφοφόρος", "f", "Και μετά;", "And then?"),
  L("Αντιπρόσωπος", "m", "Θα σας δώσω έναν φάκελο και τα ψηφοδέλτια. Πηγαίνετε πίσω από το παραβάν, εκεί κανείς δεν σας βλέπει. Βάζετε στον φάκελο ένα μόνο ψηφοδέλτιο, κλείνετε τον φάκελο και τον ρίχνετε στην κάλπη. Τα υπόλοιπα ψηφοδέλτια τα πετάτε στο καλάθι που είναι μέσα, όχι έξω.", "I'll give you an envelope and the ballot papers. Go behind the screen; nobody can see you there. You put just one ballot paper in the envelope, seal the envelope and drop it into the ballot box. The other ballot papers you throw in the basket that's inside, not outside."),
  L("Ψηφοφόρος", "f", "Κι αν θέλω να βάλω σταυρό προτίμησης;", "And if I want to mark a preference cross?"),
  L("Αντιπρόσωπος", "m", "Τον βάζετε με στιλό δίπλα στο όνομα του υποψηφίου, πάνω στο ψηφοδέλτιο, πριν το βάλετε στον φάκελο. Αν βάλετε περισσότερους σταυρούς από όσους επιτρέπονται, το ψηφοδέλτιο είναι άκυρο, οπότε προσέξτε.", "You mark it with a pen next to the candidate's name, on the ballot paper, before you put it in the envelope. If you mark more crosses than are allowed, the ballot is invalid, so be careful."),
 ],
 "questions": [
  Q("Τι ζητά πρώτα ο αντιπρόσωπος από την ψηφοφόρο;", ["Το διαβατήριό της", "Την ταυτότητά της", "Το εκλογικό της βιβλιάριο", "Τη διεύθυνσή της"], 1, "Δώστε μου την ταυτότητά σας να σας βρω στον εκλογικό κατάλογο"),
  Q("Πού πρέπει να πετάξει τα ψηφοδέλτια που δεν χρησιμοποιεί;", ["Στον κάδο έξω από το τμήμα", "Στο καλάθι πίσω από το παραβάν", "Να τα δώσει στον αντιπρόσωπο", "Να τα πάρει μαζί της"], 1, "Τα υπόλοιπα ψηφοδέλτια τα πετάτε στο καλάθι που είναι μέσα, όχι έξω"),
  Q("Πότε το ψηφοδέλτιο είναι άκυρο;", ["Όταν δεν έχει κανέναν σταυρό", "Όταν έχει περισσότερους σταυρούς από όσους επιτρέπονται", "Όταν ο σταυρός είναι με μολύβι", "Όταν ο φάκελος δεν είναι κλειστός"], 1, "Αν βάλετε περισσότερους σταυρούς από όσους επιτρέπονται, το ψηφοδέλτιο είναι άκυρο"),
 ],
 "gloss": {"εκλογικό τμήμα": "εκλογικό τμήμα — polling station", "εκλογικό κατάλογο": "εκλογικός κατάλογος — electoral roll", "ψηφοδέλτια": "ψηφοδέλτιο — ballot paper", "παραβάν": "παραβάν — (voting) screen", "κάλπη": "κάλπη — ballot box", "σταυρό προτίμησης": "σταυρός προτίμησης — preference vote (cross)", "υποψηφίου": "υποψήφιος — candidate", "άκυρο": "άκυρος — invalid"},
})

ITEMS.append({
 "id": "l56-mono-amth", "title": "Ξενάγηση στο Αρχαιολογικό Μουσείο Θεσσαλονίκης", "title_en": "A tour of the Archaeological Museum of Thessaloniki", "type": "monologue", "level": "B2",
 "context_el": "Επισκέπτεστε το Αρχαιολογικό Μουσείο Θεσσαλονίκης με μια ομάδα. Θα ακούσετε την ξεναγό στην αρχή της ξενάγησης.",
 "script": [
  L("Ξεναγός", "f", "Καλώς ήρθατε στο Αρχαιολογικό Μουσείο Θεσσαλονίκης. Το κτίριο, ένα από τα πιο χαρακτηριστικά δείγματα μοντέρνας αρχιτεκτονικής στην Ελλάδα, σχεδιάστηκε από τον αρχιτέκτονα Πάτροκλο Καραντινό και εγκαινιάστηκε το 1962.", "Welcome to the Archaeological Museum of Thessaloniki. The building, one of the most characteristic examples of modern architecture in Greece, was designed by the architect Patroklos Karantinos and opened in 1962."),
  L("Ξεναγός", "f", "Το μουσείο φιλοξενεί ευρήματα από όλη τη Μακεδονία, από την προϊστορία μέχρι τη ρωμαϊκή εποχή. Το πιο εντυπωσιακό, ίσως, είναι ο κρατήρας του Δερβενίου, ένα χάλκινο αγγείο του 4ου αιώνα π.Χ., διακοσμημένο με σκηνές από τη λατρεία του Διονύσου. Βρέθηκε σε έναν τάφο, γεμάτο με τα καμένα οστά του νεκρού.", "The museum houses finds from all over Macedonia, from prehistory to Roman times. The most impressive, perhaps, is the Derveni krater, a bronze vessel from the 4th century BC decorated with scenes from the cult of Dionysus. It was found in a tomb, filled with the burnt bones of the deceased."),
  L("Ξεναγός", "f", "Στην ίδια περιοχή βρέθηκε και ο πάπυρος του Δερβενίου, που θεωρείται το αρχαιότερο σωζόμενο χειρόγραφο της Ευρώπης. Σώθηκε επειδή απανθρακώθηκε μερικώς σε μια νεκρική πυρά. Στο τέλος της ξενάγησης θα δούμε και την αίθουσα με τον χρυσό της Μακεδονίας: κοσμήματα και στεφάνια που θα σας κόψουν την ανάσα.", "In the same area the Derveni papyrus was found, which is considered the oldest surviving manuscript in Europe. It survived because it was partly carbonised on a funeral pyre. At the end of the tour we will also see the room with the gold of Macedonia: jewellery and wreaths that will take your breath away."),
 ],
 "questions": [
  Q("Πότε εγκαινιάστηκε το κτίριο του μουσείου;", ["Το 1912", "Το 1962", "Το 2004", "Το 1980"], 1, "σχεδιάστηκε από τον αρχιτέκτονα Πάτροκλο Καραντινό και εγκαινιάστηκε το 1962"),
  Q("Τι ήταν μέσα στον κρατήρα του Δερβενίου όταν βρέθηκε;", ["Χρυσά νομίσματα", "Τα καμένα οστά του νεκρού", "Ένας πάπυρος", "Κρασί"], 1, "Βρέθηκε σε έναν τάφο, γεμάτο με τα καμένα οστά του νεκρού"),
  Q("Γιατί σώθηκε ο πάπυρος του Δερβενίου;", ["Γιατί ήταν θαμμένος σε άμμο", "Γιατί απανθρακώθηκε μερικώς σε μια νεκρική πυρά", "Γιατί ήταν μέσα σε ένα χάλκινο κουτί", "Γιατί τον αντέγραψαν οι μοναχοί"], 1, "Σώθηκε επειδή απανθρακώθηκε μερικώς σε μια νεκρική πυρά"),
 ],
 "gloss": {"κρατήρας": "κρατήρας — krater (mixing bowl)", "αγγείο": "αγγείο — vessel, vase", "λατρεία": "λατρεία — cult, worship", "οστά": "οστά — bones", "πάπυρος": "πάπυρος — papyrus", "σωζόμενο": "σωζόμενος — surviving", "απανθρακώθηκε": "απανθρακώνομαι — to be carbonised", "πυρά": "πυρά — pyre", "στεφάνια": "στεφάνι — wreath"},
})

ITEMS.append({
 "id": "l56-c1-mousikotherapeia", "title": "Η μουσικοθεραπεία", "title_en": "Music therapy", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια μουσικοθεραπεύτρια.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αλεξίου, πολλοί πιστεύουν ότι μουσικοθεραπεία σημαίνει απλώς να ακούς χαλαρωτική μουσική. Ισχύει;", "Ms Alexiou, many people think that music therapy simply means listening to relaxing music. Is that true?"),
  L("Μουσικοθεραπεύτρια", "f", "Είναι μια πολύ διαδεδομένη παρανόηση. Η μουσικοθεραπεία είναι μια κλινική παρέμβαση, που την ασκούν ειδικά εκπαιδευμένοι θεραπευτές. Το κεντρικό στοιχείο δεν είναι η μουσική καθαυτή, αλλά η θεραπευτική σχέση που χτίζεται μέσα από αυτήν. Συχνά οι θεραπευόμενοι δεν ακούν απλώς· αυτοσχεδιάζουν, παίζουν κρουστά, τραγουδούν, ακόμη κι αν δεν έχουν καμία μουσική γνώση.", "It's a very widespread misconception. Music therapy is a clinical intervention practised by specially trained therapists. The central element is not the music in itself, but the therapeutic relationship built through it. Often the clients don't just listen; they improvise, play percussion, sing, even if they have no musical knowledge at all."),
  L("Δημοσιογράφος", "m", "Σε ποιες περιπτώσεις εφαρμόζεται;", "In which cases is it used?"),
  L("Μουσικοθεραπεύτρια", "f", "Σε ένα ευρύ φάσμα. Σε παιδιά στο φάσμα του αυτισμού, για παράδειγμα, η μουσική μπορεί να γίνει ένας δίαυλος επικοινωνίας όταν ο λόγος δυσκολεύεται. Στην άνοια, είναι συγκινητικό να βλέπεις ανθρώπους που δεν αναγνωρίζουν πια τα παιδιά τους να θυμούνται ολόκληρους στίχους από τραγούδια της νιότης τους, γιατί η μουσική μνήμη φαίνεται να διατηρείται περισσότερο. Και στην αποκατάσταση μετά από εγκεφαλικό, ο ρυθμός βοηθά τους ασθενείς να ξαναβρούν τον βηματισμό τους.", "Across a wide range. In children on the autism spectrum, for example, music can become a channel of communication when speech is difficult. In dementia, it's moving to see people who no longer recognise their children remember entire verses of songs from their youth, because musical memory seems to be preserved longer. And in rehabilitation after a stroke, rhythm helps patients regain their gait."),
  L("Δημοσιογράφος", "m", "Υπάρχουν όρια;", "Are there limits?"),
  L("Μουσικοθεραπεύτρια", "f", "Βεβαίως. Η μουσικοθεραπεία δεν υποκαθιστά την ιατρική θεραπεία· τη συμπληρώνει. Και πρέπει να είμαστε προσεκτικοί με τις υπερβολές που κυκλοφορούν στο διαδίκτυο, όπως ότι ένα συγκεκριμένο κομμάτι «θεραπεύει» την κατάθλιψη. Τέτοιοι ισχυρισμοί βλάπτουν την αξιοπιστία ενός σοβαρού επαγγέλματος.", "Of course. Music therapy does not replace medical treatment; it complements it. And we must be careful with the exaggerations circulating on the internet, such as that a particular piece \"cures\" depression. Claims like that damage the credibility of a serious profession."),
 ],
 "questions": [
  Q("Ποια παρανόηση διορθώνει η μουσικοθεραπεύτρια;", ["Ότι η μουσικοθεραπεία είναι ακριβή", "Ότι μουσικοθεραπεία σημαίνει απλώς να ακούς χαλαρωτική μουσική", "Ότι είναι μόνο για παιδιά", "Ότι χρειάζεται μουσικές γνώσεις"], 1, "πολλοί πιστεύουν ότι μουσικοθεραπεία σημαίνει απλώς να ακούς χαλαρωτική μουσική … Είναι μια πολύ διαδεδομένη παρανόηση"),
  Q("Ποιο είναι, κατά την ίδια, το κεντρικό στοιχείο της μουσικοθεραπείας;", ["Η ποιότητα της μουσικής", "Η θεραπευτική σχέση που χτίζεται μέσα από τη μουσική", "Τα μουσικά όργανα", "Η διάρκεια των συνεδριών"], 1, "Το κεντρικό στοιχείο δεν είναι η μουσική καθαυτή, αλλά η θεραπευτική σχέση"),
  Q("Τι παρατηρείται σε ανθρώπους με άνοια;", ["Ξεχνούν πρώτα τα τραγούδια", "Θυμούνται στίχους από τραγούδια της νιότης τους", "Δεν αντιδρούν καθόλου στη μουσική", "Μαθαίνουν εύκολα καινούργια τραγούδια"], 1, "θυμούνται ολόκληρους στίχους από τραγούδια της νιότης τους, γιατί η μουσική μνήμη φαίνεται να διατηρείται περισσότερο"),
  Q("Γιατί είναι επικίνδυνοι οι ισχυρισμοί του διαδικτύου;", ["Γιατί διαφημίζουν ακριβά προγράμματα", "Γιατί βλάπτουν την αξιοπιστία του επαγγέλματος", "Γιατί απαγορεύονται από τον νόμο", "Γιατί προτείνουν λάθος μουσική"], 1, "Τέτοιοι ισχυρισμοί βλάπτουν την αξιοπιστία ενός σοβαρού επαγγέλματος"),
 ],
 "gloss": {"παρανόηση": "παρανόηση — misconception", "κλινική παρέμβαση": "κλινική παρέμβαση — clinical intervention", "καθαυτή": "καθαυτός — in itself", "θεραπευόμενοι": "θεραπευόμενος — client, patient (in therapy)", "αυτοσχεδιάζουν": "αυτοσχεδιάζω — to improvise", "κρουστά": "κρουστά — percussion", "δίαυλος": "δίαυλος — channel", "άνοια": "άνοια — dementia", "αποκατάσταση": "αποκατάσταση — rehabilitation", "εγκεφαλικό": "εγκεφαλικό — stroke", "βηματισμό": "βηματισμός — gait, step", "υποκαθιστά": "υποκαθιστώ — to replace", "ισχυρισμοί": "ισχυρισμός — claim"},
})

ITEMS.append({
 "id": "l56-c1-enosi-kritis", "title": "Η Ένωση της Κρήτης με την Ελλάδα", "title_en": "The union of Crete with Greece", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια ομιλία ενός ιστορικού για τον μακρύ δρόμο της Κρήτης προς την ένωση με την Ελλάδα.",
 "script": [
  L("Ιστορικός", "m", "Όταν ιδρύθηκε το ελληνικό κράτος, η Κρήτη, παρά τη συμμετοχή της στην Επανάσταση του 1821, έμεινε έξω από τα σύνορά του. Τις επόμενες δεκαετίες οι Κρητικοί εξεγέρθηκαν επανειλημμένα. Η πιο γνωστή εξέγερση, του 1866, έμεινε στην ιστορία για το ολοκαύτωμα της Μονής Αρκαδίου, όπου οι πολιορκημένοι προτίμησαν να ανατινάξουν την πυριτιδαποθήκη παρά να παραδοθούν.", "When the Greek state was founded, Crete, despite its participation in the Revolution of 1821, was left outside its borders. In the following decades the Cretans rose up repeatedly. The best-known revolt, of 1866, went down in history for the holocaust of the Arkadi Monastery, where the besieged chose to blow up the powder magazine rather than surrender."),
  L("Ιστορικός", "m", "Το 1898, μετά από νέες ταραχές και την παρέμβαση των Μεγάλων Δυνάμεων, δημιουργήθηκε η αυτόνομη Κρητική Πολιτεία, υπό την τυπική κυριαρχία του σουλτάνου, με ύπατο αρμοστή τον πρίγκιπα Γεώργιο της Ελλάδας. Η αυτονομία, ωστόσο, δεν ικανοποίησε όσους ήθελαν την ένωση.", "In 1898, after new unrest and the intervention of the Great Powers, the autonomous Cretan State was created, under the nominal sovereignty of the sultan, with Prince George of Greece as High Commissioner. Autonomy, however, did not satisfy those who wanted union."),
  L("Ιστορικός", "m", "Ανάμεσά τους ξεχώρισε ένας νέος δικηγόρος από τα Χανιά, ο Ελευθέριος Βενιζέλος, που το 1905 ηγήθηκε του κινήματος του Θερίσου εναντίον της πολιτικής του πρίγκιπα. Τρία χρόνια αργότερα η κρητική βουλή κήρυξε μονομερώς την ένωση, αλλά η Αθήνα, φοβούμενη διεθνείς επιπλοκές, δεν τόλμησε να την αποδεχτεί επίσημα.", "Among them stood out a young lawyer from Chania, Eleftherios Venizelos, who in 1905 led the Theriso movement against the prince's policy. Three years later the Cretan assembly unilaterally declared union, but Athens, fearing international complications, did not dare to accept it officially."),
  L("Ιστορικός", "m", "Η ένωση έγινε πραγματικότητα μόνο μετά τους Βαλκανικούς Πολέμους, όταν με τη Συνθήκη του Λονδίνου, το 1913, η Οθωμανική Αυτοκρατορία παραιτήθηκε από κάθε δικαίωμα στο νησί. Την 1η Δεκεμβρίου του 1913 υψώθηκε η ελληνική σημαία στο φρούριο Φιρκά των Χανίων, παρουσία του Βενιζέλου, πλέον πρωθυπουργού της Ελλάδας. Ήταν το τέλος ενός αγώνα σχεδόν έναν αιώνα.", "Union became a reality only after the Balkan Wars, when by the Treaty of London in 1913 the Ottoman Empire renounced all rights to the island. On 1 December 1913 the Greek flag was raised at the Firkas fortress in Chania, in the presence of Venizelos, by then prime minister of Greece. It was the end of a struggle of almost a century."),
 ],
 "questions": [
  Q("Γιατί έμεινε στην ιστορία η εξέγερση του 1866;", ["Για τη νίκη των Κρητικών στα Χανιά", "Για το ολοκαύτωμα της Μονής Αρκαδίου", "Για την ένωση με την Ελλάδα", "Για τη δολοφονία ενός πασά"], 1, "έμεινε στην ιστορία για το ολοκαύτωμα της Μονής Αρκαδίου"),
  Q("Τι ήταν η Κρητική Πολιτεία;", ["Ένα ανεξάρτητο κράτος χωρίς σχέση με τον σουλτάνο", "Ένα αυτόνομο κράτος υπό την τυπική κυριαρχία του σουλτάνου", "Μια ελληνική νομαρχία", "Μια βρετανική αποικία"], 1, "δημιουργήθηκε η αυτόνομη Κρητική Πολιτεία, υπό την τυπική κυριαρχία του σουλτάνου"),
  Q("Γιατί η Αθήνα δεν αποδέχτηκε την ένωση το 1908;", ["Γιατί δεν την ήθελε ο Βενιζέλος", "Γιατί φοβόταν διεθνείς επιπλοκές", "Γιατί δεν είχε στρατό", "Γιατί την απέρριψαν οι Κρητικοί"], 1, "η Αθήνα, φοβούμενη διεθνείς επιπλοκές, δεν τόλμησε να την αποδεχτεί επίσημα"),
  Q("Τι συνέβη την 1η Δεκεμβρίου 1913;", ["Υπογράφηκε η Συνθήκη του Λονδίνου", "Υψώθηκε η ελληνική σημαία στο φρούριο Φιρκά", "Ξεκίνησαν οι Βαλκανικοί Πόλεμοι", "Ο Βενιζέλος έγινε πρωθυπουργός"], 1, "Την 1η Δεκεμβρίου του 1913 υψώθηκε η ελληνική σημαία στο φρούριο Φιρκά των Χανίων"),
 ],
 "gloss": {"εξεγέρθηκαν": "εξεγείρομαι — to rise up, revolt", "επανειλημμένα": "επανειλημμένα — repeatedly", "ολοκαύτωμα": "ολοκαύτωμα — holocaust, self-sacrifice", "πολιορκημένοι": "πολιορκημένος — besieged", "ανατινάξουν": "ανατινάζω — to blow up", "πυριτιδαποθήκη": "πυριτιδαποθήκη — powder magazine", "κυριαρχία": "κυριαρχία — sovereignty", "ύπατο αρμοστή": "ύπατος αρμοστής — High Commissioner", "ηγήθηκε": "ηγούμαι — to lead", "μονομερώς": "μονομερώς — unilaterally", "επιπλοκές": "επιπλοκή — complication", "παραιτήθηκε": "παραιτούμαι — to renounce, resign"},
})

rnd = random.Random(56)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-56.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
