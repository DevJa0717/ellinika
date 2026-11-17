# Source for library/listening/listening-164.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l164.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l164-ann-imeroploio", "title": "Ανακοίνωση στο ημερόπλοιο πριν από τη στάση για κολύμπι", "title_en": "An announcement on the day-trip boat before the swimming stop", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε τον καπετάνιο ενός ημερόπλοιου να μιλάει στους επιβάτες λίγο πριν από τη στάση σε έναν κόλπο.",
 "script": [
  L("Καπετάνιος", "m", "Κυρίες και κύριοι, σε δέκα λεπτά θα αγκυροβολήσουμε στον κόλπο που βλέπετε μπροστά μας, όπου θα μείνουμε μία ώρα για κολύμπι. Το νερό εδώ έχει βάθος περίπου έξι μέτρα και είναι πολύ καθαρό, αλλά ρεύματα δεν υπάρχουν.", "Ladies and gentlemen, in ten minutes we'll anchor in the bay you see in front of us, where we'll stay for an hour for swimming. The water here is about six metres deep and very clear, but there are no currents."),
  L("Καπετάνιος", "m", "Για την ασφάλειά σας, βουτάτε μόνο από την πλατφόρμα στο πίσω μέρος του σκάφους και ποτέ από το πάνω κατάστρωμα. Μην απομακρύνεστε πέρα από τις κίτρινες σημαδούρες, γιατί από εκεί και πέρα περνούν ταχύπλοα. Τα παιδιά κάτω των δώδεκα κολυμπούν μόνο με σωσίβιο, και έχουμε σωσίβια για όλους στο κάτω σαλόνι.", "For your safety, dive only from the platform at the back of the boat and never from the upper deck. Don't go beyond the yellow buoys, because speedboats pass from there on. Children under twelve swim only with a life jacket, and we have life jackets for everyone in the lower lounge."),
  L("Καπετάνιος", "m", "Όταν ακούσετε τρία σύντομα σφυρίγματα, παρακαλούμε να επιστρέψετε στο σκάφος, γιατί αναχωρούμε δέκα λεπτά αργότερα. Το μεσημεριανό θα σερβιριστεί μόλις ξεκινήσουμε για το λιμάνι. Καλό μπάνιο!", "When you hear three short whistles, please return to the boat, because we'll leave ten minutes later. Lunch will be served as soon as we set off for the harbour. Enjoy your swim!"),
 ],
 "questions": [
  Q("Πόσο θα μείνει το σκάφος στον κόλπο;", ["Μισή ώρα", "Μία ώρα", "Δύο ώρες", "Δέκα λεπτά"], 1, "όπου θα μείνουμε μία ώρα για κολύμπι"),
  Q("Γιατί δεν πρέπει να περάσουν τις κίτρινες σημαδούρες;", ["Γιατί από εκεί και πέρα περνούν ταχύπλοα", "Γιατί υπάρχουν ρεύματα", "Γιατί το νερό είναι βρόμικο", "Γιατί υπάρχουν τσούχτρες"], 0, "γιατί από εκεί και πέρα περνούν ταχύπλοα"),
  Q("Τι σημαίνουν τα τρία σύντομα σφυρίγματα;", ["Ότι σερβίρεται το φαγητό", "Ότι πρέπει να βγουν από το νερό αμέσως λόγω κινδύνου", "Ότι πρέπει να επιστρέψουν στο σκάφος", "Ότι μπορούν να βουτήξουν"], 2, "παρακαλούμε να επιστρέψετε στο σκάφος"),
 ],
 "gloss": {"ημερόπλοιου": "ημερόπλοιο — day-trip boat", "επιβάτες": "επιβάτης — passenger", "κόλπο": "κόλπος — bay", "αγκυροβολήσουμε": "αγκυροβολώ — to anchor", "βάθος": "βάθος — depth", "ρεύματα": "ρεύμα — current", "πλατφόρμα": "πλατφόρμα — platform", "κατάστρωμα": "κατάστρωμα — deck", "σημαδούρες": "σημαδούρα — buoy", "ταχύπλοα": "ταχύπλοο — speedboat", "σωσίβιο": "σωσίβιο — life jacket", "σφυρίγματα": "σφύριγμα — whistle", "σερβιριστεί": "σερβίρομαι — to be served"},
})

ITEMS.append({
 "id": "l164-int-grammatoseires", "title": "Η σχεδιάστρια γραμματοσειρών", "title_en": "The type designer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γραφίστρια που σχεδιάζει γραμματοσειρές με ελληνικούς χαρακτήρες.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνει μια σχεδιάστρια γραμματοσειρών;", "What exactly does a type designer do?"),
  L("Σχεδιάστρια", "f", "Σχεδιάζω τα γράμματα που βλέπετε στις οθόνες, στα βιβλία και στις πινακίδες. Μια πλήρης γραμματοσειρά δεν είναι μόνο είκοσι τέσσερα γράμματα. Είναι κεφαλαία και πεζά, αριθμοί, σημεία στίξης, τόνοι, και συχνά λατινικοί και κυριλλικοί χαρακτήρες. Μπορεί να φτάσει τα δύο χιλιάδες σχήματα.", "I design the letters you see on screens, in books and on signs. A complete typeface isn't just twenty-four letters. It's capitals and lower case, numbers, punctuation marks, accents, and often Latin and Cyrillic characters. It can reach two thousand shapes."),
  L("Δημοσιογράφος", "m", "Ποια είναι η δυσκολία με τα ελληνικά;", "What's the difficulty with Greek?"),
  L("Σχεδιάστρια", "f", "Πολλές ξένες γραμματοσειρές έχουν ελληνικά που φτιάχτηκαν βιαστικά, σαν να είναι λατινικά μεταμφιεσμένα. Ο Έλληνας αναγνώστης το καταλαβαίνει αμέσως, ακόμα κι αν δεν ξέρει να πει τι φταίει. Το μικρό λάμδα, για παράδειγμα, ή το ζήτα, δεν έχουν αντίστοιχο στα λατινικά, και πρέπει να τα σχεδιάσεις από την αρχή. Και οι τόνοι θέλουν προσοχή, γιατί αν είναι πολύ μικροί χάνονται, ενώ αν είναι πολύ μεγάλοι η σελίδα γεμίζει θόρυβο.", "Many foreign typefaces have Greek that was made in a hurry, as if it were disguised Latin. Greek readers notice immediately, even if they can't say what's wrong. The small lambda, for example, or the zeta, has no equivalent in Latin, and you have to design them from scratch. And the accents need care, because if they're too small they get lost, while if they're too big the page fills with noise."),
  L("Δημοσιογράφος", "m", "Πόσο χρόνο θέλει μια γραμματοσειρά;", "How long does a typeface take?"),
  L("Σχεδιάστρια", "f", "Η τελευταία μου, για μια εφημερίδα, μου πήρε δεκαοκτώ μήνες. Το πιο ωραίο κομπλιμέντο δεν είναι να μου πουν ότι είναι όμορφη. Είναι να διαβάσει κάποιος ένα ολόκληρο άρθρο χωρίς να προσέξει καθόλου τα γράμματα.", "My last one, for a newspaper, took me eighteen months. The nicest compliment isn't being told it's beautiful. It's when someone reads a whole article without noticing the letters at all."),
 ],
 "questions": [
  Q("Πόσα σχήματα μπορεί να έχει μια πλήρης γραμματοσειρά;", ["Είκοσι τέσσερα", "Περίπου διακόσια", "Έως δύο χιλιάδες", "Δέκα χιλιάδες"], 2, "Μπορεί να φτάσει τα δύο χιλιάδες σχήματα"),
  Q("Ποιο είναι το πρόβλημα με πολλές ξένες γραμματοσειρές;", ["Δεν έχουν τόνους", "Τα ελληνικά τους φτιάχτηκαν βιαστικά, σαν λατινικά μεταμφιεσμένα", "Είναι πολύ ακριβές", "Δεν διαβάζονται στις οθόνες"], 1, "έχουν ελληνικά που φτιάχτηκαν βιαστικά, σαν να είναι λατινικά μεταμφιεσμένα"),
  Q("Ποιο θεωρεί το καλύτερο κομπλιμέντο;", ["Να της πουν ότι η γραμματοσειρά είναι όμορφη", "Να κερδίσει ένα βραβείο", "Να διαβάσει κάποιος ένα ολόκληρο άρθρο χωρίς να προσέξει τα γράμματα", "Να τη χρησιμοποιήσει μια μεγάλη εφημερίδα"], 2, "Είναι να διαβάσει κάποιος ένα ολόκληρο άρθρο χωρίς να προσέξει καθόλου τα γράμματα"),
 ],
 "gloss": {"σχεδιάστρια": "σχεδιάστρια — designer (f.)", "γραμματοσειρών": "γραμματοσειρά — typeface, font", "γραφίστρια": "γραφίστρια — graphic designer (f.)", "χαρακτήρες": "χαρακτήρας — character (letter)", "πινακίδες": "πινακίδα — sign", "κεφαλαία": "κεφαλαίο — capital letter", "πεζά": "πεζό — lower-case letter", "σημεία στίξης": "σημεία στίξης — punctuation marks", "τόνοι": "τόνος — accent", "κυριλλικοί": "κυριλλικός — Cyrillic", "βιαστικά": "βιαστικά — hastily", "μεταμφιεσμένα": "μεταμφιεσμένος — disguised", "αντίστοιχο": "αντίστοιχος — equivalent", "κομπλιμέντο": "κομπλιμέντο — compliment"},
})

ITEMS.append({
 "id": "l164-int-lithoxoos", "title": "Μια λιθοξόος στην Τήνο", "title_en": "A marble carver on Tinos", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια νεαρή λιθοξόο που δουλεύει το μάρμαρο σε ένα χωριό της Τήνου.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς αποφασίσατε να γίνετε λιθοξόος;", "How did you decide to become a marble carver?"),
  L("Λιθοξόος", "f", "Μεγάλωσα στην Αθήνα, αλλά τα καλοκαίρια τα περνούσα στην Τήνο, στη γιαγιά μου. Στο χωριό της, σχεδόν κάθε σπίτι έχει κάτι μαρμάρινο πάνω από την πόρτα, ένα πουλί, ένα λουλούδι, ένα καράβι. Στα δεκαοκτώ γράφτηκα στη Σχολή Καλών Τεχνών του νησιού, και από τότε δεν έφυγα.", "I grew up in Athens, but I spent the summers on Tinos, at my grandmother's. In her village, almost every house has something in marble above the door, a bird, a flower, a ship. At eighteen I enrolled in the island's School of Fine Arts, and I haven't left since."),
  L("Δημοσιογράφος", "f", "Είναι βαριά δουλειά για μια γυναίκα;", "Is it heavy work for a woman?"),
  L("Λιθοξόος", "f", "Αυτή την ερώτηση μού την κάνουν συνέχεια. Η δύναμη μετράει λιγότερο απ' όσο νομίζουν· πιο σημαντική είναι η υπομονή. Το μάρμαρο δεν συγχωρεί. Αν χτυπήσεις λίγο πιο δυνατά, μπορεί να σπάσει ένα κομμάτι που δούλευες τρεις εβδομάδες, και τότε ξεκινάς από την αρχή.", "I get asked that question all the time. Strength matters less than people think; patience is more important. Marble doesn't forgive. If you hit a little too hard, a piece you've been working on for three weeks can break, and then you start again from the beginning."),
  L("Δημοσιογράφος", "f", "Τι παραγγελίες έχετε σήμερα;", "What orders do you have today?"),
  L("Λιθοξόος", "f", "Κυρίως υπέρθυρα για σπίτια που ανακαινίζονται, και κρήνες για πλατείες. Πριν από λίγα χρόνια η μαρμαροτεχνία της Τήνου γράφτηκε στον κατάλογο της UNESCO για την άυλη πολιτιστική κληρονομιά, και από τότε έρχονται και ξένοι πελάτες. Μου αρέσει να σκέφτομαι ότι κάποιο σχέδιό μου θα βρίσκεται πάνω από μια πόρτα σε εκατό χρόνια.", "Mainly lintels for houses being renovated, and fountains for squares. A few years ago Tinian marble craftsmanship was inscribed on UNESCO's list of intangible cultural heritage, and since then foreign clients come too. I like to think that one of my designs will be above a door in a hundred years."),
 ],
 "questions": [
  Q("Τι υπάρχει πάνω από την πόρτα σχεδόν κάθε σπιτιού στο χωριό της γιαγιάς της;", ["Ένα μαρμάρινο σχέδιο, όπως ένα πουλί ή ένα καράβι", "Μια εικόνα αγίου", "Ένα φανάρι", "Ένα ξύλινο σήμα"], 0, "σχεδόν κάθε σπίτι έχει κάτι μαρμάρινο πάνω από την πόρτα"),
  Q("Τι θεωρεί πιο σημαντικό από τη δύναμη σε αυτή τη δουλειά;", ["Τα καλά εργαλεία", "Την υπομονή", "Το ταλέντο στο σχέδιο", "Την εμπειρία"], 1, "πιο σημαντική είναι η υπομονή"),
  Q("Τι άλλαξε μετά την εγγραφή της μαρμαροτεχνίας στον κατάλογο της UNESCO;", ["Άνοιξαν νέες σχολές", "Αυξήθηκαν οι τιμές του μαρμάρου", "Έρχονται και ξένοι πελάτες", "Η ίδια πήρε βραβείο"], 2, "από τότε έρχονται και ξένοι πελάτες"),
 ],
 "gloss": {"λιθοξόος": "λιθοξόος — stone carver", "λιθοξόο": "λιθοξόος — stone carver", "μάρμαρο": "μάρμαρο — marble", "μαρμάρινο": "μαρμάρινος — (made of) marble", "Σχολή Καλών Τεχνών": "Σχολή Καλών Τεχνών — School of Fine Arts", "υπομονή": "υπομονή — patience", "συγχωρεί": "συγχωρώ — to forgive", "υπέρθυρα": "υπέρθυρο — lintel, carving above a door", "ανακαινίζονται": "ανακαινίζομαι — to be renovated", "κρήνες": "κρήνη — (public) fountain", "μαρμαροτεχνία": "μαρμαροτεχνία — marble craftsmanship", "άυλη": "άυλος — intangible", "κληρονομιά": "κληρονομιά — heritage"},
})

ITEMS.append({
 "id": "l164-dia-mpanio", "title": "Ποιος θα καθαρίσει το μπάνιο;", "title_en": "Who will clean the bathroom?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φοιτητές που μένουν μαζί να συζητούν πώς θα μοιράσουν τις δουλειές του σπιτιού.",
 "script": [
  L("Ορέστης", "m", "Δάφνη, μπορούμε να μιλήσουμε λίγο; Τρεις εβδομάδες τώρα καθαρίζω εγώ το μπάνιο. Δεν το λέω για να μαλώσουμε, αλλά κάτι πρέπει να αλλάξει.", "Dafni, can we talk for a bit? For three weeks now I've been cleaning the bathroom. I'm not saying it to argue, but something has to change."),
  L("Δάφνη", "f", "Έχεις δίκιο, και ζητώ συγγνώμη. Με την εξεταστική ξέχασα τελείως ότι υπάρχει σπίτι. Αλλά κι εσύ, για να είμαστε δίκαιοι, δεν έχεις πλύνει ούτε ένα πιάτο από την Κυριακή.", "You're right, and I apologise. With exam period I completely forgot the flat exists. But you too, to be fair, haven't washed a single dish since Sunday."),
  L("Ορέστης", "m", "Εντάξει, ισοπαλία. Τι λες να κάνουμε ένα πρόγραμμα και να το κολλήσουμε στο ψυγείο; Μία εβδομάδα εσύ μπάνιο και εγώ κουζίνα, την άλλη ανάποδα.", "OK, a draw. What do you say we make a schedule and stick it on the fridge? One week you do the bathroom and I do the kitchen, the next week the other way round."),
  L("Δάφνη", "f", "Μου αρέσει. Και τα σκουπίδια; Αυτά δεν περιμένουν μια εβδομάδα.", "I like it. And the rubbish? That can't wait a week."),
  L("Ορέστης", "m", "Τα σκουπίδια τα κατεβάζει όποιος φεύγει πρώτος το πρωί. Και την ανακύκλωση την Πέμπτη, που περνάει το φορτηγό.", "Whoever leaves first in the morning takes the rubbish down. And the recycling on Thursday, when the lorry comes."),
  L("Δάφνη", "f", "Συμφωνώ. Αλλά αν κάποιος δεν κάνει τη δουλειά του, να κερνάει πίτσα την Παρασκευή. Έτσι θα έχουμε κίνητρο.", "Agreed. But if someone doesn't do their job, they buy pizza on Friday. That way we'll have an incentive."),
 ],
 "questions": [
  Q("Γιατί η Δάφνη δεν είχε καθαρίσει τίποτα;", ["Γιατί έλειπε στο χωριό της", "Γιατί ήταν άρρωστη", "Γιατί με την εξεταστική ξέχασε τελείως το σπίτι", "Γιατί δούλευε μέχρι αργά"], 2, "Με την εξεταστική ξέχασα τελείως ότι υπάρχει σπίτι"),
  Q("Τι προτείνει ο Ορέστης;", ["Να πληρώσουν μια καθαρίστρια", "Ένα πρόγραμμα με εβδομάδες εναλλάξ για μπάνιο και κουζίνα", "Να καθαρίζουν μαζί κάθε Σάββατο", "Να καθαρίζει ο καθένας το δωμάτιό του μόνο"], 1, "Μία εβδομάδα εσύ μπάνιο και εγώ κουζίνα, την άλλη ανάποδα"),
  Q("Τι θα γίνεται αν κάποιος δεν κάνει τη δουλειά του;", ["Θα κερνάει πίτσα την Παρασκευή", "Θα πληρώνει πρόστιμο", "Θα καθαρίζει δύο εβδομάδες", "Θα βγάζει τα σκουπίδια έναν μήνα"], 0, "να κερνάει πίτσα την Παρασκευή"),
 ],
 "gloss": {"μοιράσουν": "μοιράζω — to share out", "μαλώσουμε": "μαλώνω — to argue, to quarrel", "εξεταστική": "εξεταστική — exam period", "δίκαιοι": "δίκαιος — fair", "ισοπαλία": "ισοπαλία — draw, tie", "κολλήσουμε": "κολλάω — to stick", "ανάποδα": "ανάποδα — the other way round", "σκουπίδια": "σκουπίδια — rubbish", "κατεβάζει": "κατεβάζω — to take down", "ανακύκλωση": "ανακύκλωση — recycling", "κερνάει": "κερνάω — to treat, to buy (for someone)", "κίνητρο": "κίνητρο — incentive"},
})

ITEMS.append({
 "id": "l164-dia-sakidio", "title": "Ένα σακίδιο για δύο εβδομάδες", "title_en": "One backpack for two weeks", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλες να ετοιμάζουν τις αποσκευές τους για ένα ταξίδι δύο εβδομάδων με τρένο στην Ευρώπη.",
 "script": [
  L("Χαρά", "f", "Μαρίνα, σου το είπα από την αρχή: μόνο ένα σακίδιο η καθεμία. Θα αλλάζουμε τρένο σχεδόν κάθε δεύτερη μέρα, και δεν θέλω να σέρνουμε βαλίτσες στις σκάλες των σταθμών.", "Marina, I told you from the start: just one backpack each. We'll be changing trains almost every other day, and I don't want us dragging suitcases up the station stairs."),
  L("Μαρίνα", "f", "Το ξέρω, αλλά δες: έξι μπλούζες, δύο παντελόνια, ένα φόρεμα για το βράδυ, τα αθλητικά, και τα σανδάλια. Δεν χωράνε όλα.", "I know, but look: six tops, two pairs of trousers, a dress for the evening, the trainers, and the sandals. They don't all fit."),
  L("Χαρά", "f", "Τρεις μπλούζες φτάνουν. Θα πλένουμε στο νεροχύτη του ξενοδοχείου, και τον Ιούλιο στεγνώνουν μέσα σε μια νύχτα. Το φόρεμα κράτησέ το, αλλά τα σανδάλια τα αφήνεις.", "Three tops are enough. We'll wash them in the hotel sink, and in July they dry overnight. Keep the dress, but you're leaving the sandals."),
  L("Μαρίνα", "f", "Και πού θα βάλω τα καλλυντικά; Μόνο η κρέμα μου είναι ένα ολόκληρο μπουκάλι.", "And where will I put my toiletries? My cream alone is a whole bottle."),
  L("Χαρά", "f", "Αγόρασε τα μικρά μπουκαλάκια του ταξιδιού. Και ό,τι ξεχάσουμε, υπάρχουν φαρμακεία και στη Βιέννη, σε διαβεβαιώ.", "Buy the small travel bottles. And whatever we forget, there are pharmacies in Vienna too, I assure you."),
  L("Μαρίνα", "f", "Καλά, θα κάνω μια δοκιμή απόψε. Αν δεν κλείνει το φερμουάρ, όμως, θα σου ζητήσω χώρο στο δικό σου.", "OK, I'll do a trial tonight. But if the zip won't close, I'll ask you for space in yours."),
 ],
 "questions": [
  Q("Γιατί η Χαρά θέλει να πάρουν μόνο σακίδια;", ["Γιατί οι αεροπορικές χρεώνουν τις βαλίτσες", "Γιατί θα αλλάζουν συχνά τρένο και δεν θέλει να σέρνουν βαλίτσες στις σκάλες", "Γιατί θα κάνουν πεζοπορία", "Γιατί δεν έχουν βαλίτσες"], 1, "δεν θέλω να σέρνουμε βαλίτσες στις σκάλες των σταθμών"),
  Q("Πώς σκοπεύει η Χαρά να λύσει το πρόβλημα των ρούχων;", ["Θα αγοράσουν ρούχα εκεί", "Θα πλένουν στο νεροχύτη του ξενοδοχείου", "Θα στέλνουν τα άπλυτα με το ταχυδρομείο", "Θα πάνε σε πλυντήριο κάθε μέρα"], 1, "Θα πλένουμε στο νεροχύτη του ξενοδοχείου"),
  Q("Τι θα κάνει η Μαρίνα απόψε;", ["Θα αγοράσει καινούργιο σακίδιο", "Θα αφήσει το φόρεμα", "Θα κάνει μια δοκιμή να δει αν χωράνε όλα", "Θα ακυρώσει το ταξίδι"], 2, "θα κάνω μια δοκιμή απόψε"),
 ],
 "gloss": {"σακίδιο": "σακίδιο — backpack", "αποσκευές": "αποσκευή — luggage", "σέρνουμε": "σέρνω — to drag", "βαλίτσες": "βαλίτσα — suitcase", "χωράνε": "χωράω — to fit", "νεροχύτη": "νεροχύτης — sink", "στεγνώνουν": "στεγνώνω — to dry", "καλλυντικά": "καλλυντικά — toiletries, cosmetics", "μπουκαλάκια": "μπουκαλάκι — small bottle", "διαβεβαιώ": "διαβεβαιώνω — to assure", "δοκιμή": "δοκιμή — trial, test", "φερμουάρ": "φερμουάρ — zip"},
})

ITEMS.append({
 "id": "l164-mon-xoros", "title": "Ξεκίνησα παραδοσιακούς χορούς στα πενήντα", "title_en": "I started traditional dancing at fifty", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλάει σε ένα ραδιοφωνικό πρόγραμμα για το πώς άρχισε μαθήματα παραδοσιακών χορών.",
 "script": [
  L("Άντρας", "m", "Σε όλα τα πανηγύρια και τους γάμους της ζωής μου καθόμουν στο τραπέζι και κοίταζα τους άλλους να χορεύουν. Έλεγα ότι δεν μου αρέσει, αλλά η αλήθεια ήταν ότι ντρεπόμουν. Δεν ήξερα ούτε τα βήματα του συρτού.", "At every village festival and wedding of my life I sat at the table and watched the others dance. I said I didn't like it, but the truth was that I was embarrassed. I didn't even know the steps of the syrtos."),
  L("Άντρας", "m", "Όταν έκλεισα τα πενήντα, η κόρη μου μού έκανε δώρο μια εγγραφή στον πολιτιστικό σύλλογο της γειτονιάς. Την πρώτη βραδιά ήμουν ο μόνος άντρας ανάμεσα σε δεκαπέντε γυναίκες και ο μόνος που πατούσε τα πόδια των άλλων. Η δασκάλα όμως μου είπε κάτι που δεν το ξεχνώ: ότι ο χορός μαθαίνεται με τα αυτιά πριν από τα πόδια. Πρώτα να ακούσω τον ρυθμό, και μετά να μετρήσω.", "When I turned fifty, my daughter gave me a membership at the neighbourhood cultural association as a present. On the first evening I was the only man among fifteen women and the only one treading on the others' feet. But the teacher told me something I don't forget: that dancing is learned with the ears before the feet. First listen to the rhythm, and then count."),
  L("Άντρας", "m", "Δύο χρόνια μετά, ξέρω καμιά τριανταριά χορούς από όλη την Ελλάδα. Τον Αύγουστο, στο πανηγύρι του χωριού, σηκώθηκα πρώτος και έσυρα τον χορό. Η μητέρα μου, ογδόντα πέντε χρονών, έκλαιγε. Μου είπε ότι χόρευα σαν τον πατέρα μου.", "Two years later, I know about thirty dances from all over Greece. In August, at the village festival, I got up first and led the dance. My mother, eighty-five years old, was crying. She told me I danced like my father."),
 ],
 "questions": [
  Q("Γιατί δεν χόρευε στα πανηγύρια;", ["Γιατί δεν του άρεσε η μουσική", "Γιατί ντρεπόταν", "Γιατί είχε πρόβλημα στο πόδι", "Γιατί δεν τον άφηνε η γυναίκα του"], 1, "η αλήθεια ήταν ότι ντρεπόμουν"),
  Q("Τι του είπε η δασκάλα που δεν ξεχνά;", ["Ότι είναι πολύ μεγάλος για να μάθει", "Ότι πρέπει να έρχεται δύο φορές την εβδομάδα", "Ότι ο χορός μαθαίνεται με τα αυτιά πριν από τα πόδια", "Ότι χρειάζεται καινούργια παπούτσια"], 2, "ο χορός μαθαίνεται με τα αυτιά πριν από τα πόδια"),
  Q("Τι του είπε η μητέρα του στο πανηγύρι;", ["Ότι χόρευε σαν τον πατέρα του", "Ότι ήταν ο καλύτερος χορευτής του χωριού", "Ότι έπρεπε να είχε αρχίσει νωρίτερα", "Ότι ντράπηκε για εκείνον"], 0, "Μου είπε ότι χόρευα σαν τον πατέρα μου"),
 ],
 "gloss": {"ραδιοφωνικό": "ραδιοφωνικός — radio (adj.)", "πανηγύρια": "πανηγύρι — village festival", "ντρεπόμουν": "ντρέπομαι — to be embarrassed, shy", "βήματα": "βήμα — step", "συρτού": "συρτός — syrtos (a Greek dance)", "εγγραφή": "εγγραφή — enrolment, membership", "πολιτιστικό σύλλογο": "πολιτιστικός σύλλογος — cultural association", "πατούσε": "πατάω — to tread on", "ρυθμό": "ρυθμός — rhythm", "καμιά τριανταριά": "καμιά τριανταριά — about thirty", "έσυρα τον χορό": "σέρνω τον χορό — to lead the dance"},
})

ITEMS.append({
 "id": "l164-vm-nosileftria", "title": "Μήνυμα από τη σχολική νοσηλεύτρια", "title_en": "A message from the school nurse", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη νοσηλεύτρια του σχολείου όπου πηγαίνει ο γιος σας.",
 "script": [
  L("Νοσηλεύτρια", "f", "Καλημέρα σας, είμαι η Κατερίνα, η νοσηλεύτρια του σχολείου. Σας καλώ για τον Άγγελο. Μην ανησυχείτε, είναι καλά. Στο διάλειμμα έπεσε στην αυλή και χτύπησε ελαφρά το γόνατο. Του καθάρισα την πληγή και του έβαλα γάζα.", "Good morning, I'm Katerina, the school nurse. I'm calling about Angelos. Don't worry, he's fine. During break he fell in the playground and grazed his knee slightly. I cleaned the wound and put a gauze on it."),
  L("Νοσηλεύτρια", "f", "Δεν χρειάζεται να έρθετε να τον πάρετε· γύρισε κανονικά στην τάξη και παίζει. Ελέγξτε μόνο το βράδυ αν η πληγή είναι καθαρή, και αλλάξτε τη γάζα. Αν δείτε ότι κοκκινίζει ή πρήζεται, καλό θα ήταν να τον δει ένας γιατρός.", "There's no need to come and pick him up; he went back to class as normal and is playing. Just check this evening that the wound is clean, and change the gauze. If you see it going red or swelling, it would be good for a doctor to see him."),
  L("Νοσηλεύτρια", "f", "Και κάτι ακόμη: στο αρχείο μας δεν βρίσκω το βιβλιάριο εμβολίων του. Αν μπορείτε, στείλτε μου μια φωτοτυπία με τον Άγγελο μέσα στην εβδομάδα. Ευχαριστώ, καλή σας μέρα.", "And one more thing: I can't find his vaccination record in our files. If you can, send me a photocopy with Angelos within the week. Thank you, have a nice day."),
 ],
 "questions": [
  Q("Τι έπαθε ο Άγγελος;", ["Έπεσε στην αυλή και χτύπησε ελαφρά το γόνατο", "Είχε πυρετό", "Τον τσίμπησε μέλισσα", "Πόνεσε η κοιλιά του"], 0, "Στο διάλειμμα έπεσε στην αυλή και χτύπησε ελαφρά το γόνατο"),
  Q("Χρειάζεται να πάτε να τον πάρετε από το σχολείο;", ["Ναι, αμέσως", "Ναι, στο τέλος του διαλείμματος", "Όχι, γύρισε κανονικά στην τάξη", "Όχι, θα τον φέρει η νοσηλεύτρια"], 2, "Δεν χρειάζεται να έρθετε να τον πάρετε"),
  Q("Τι σας ζητά να στείλετε;", ["Μια βεβαίωση γιατρού", "Μια φωτοτυπία του βιβλιαρίου εμβολίων", "Μια φωτογραφία του", "Καινούργιες γάζες"], 1, "στείλτε μου μια φωτοτυπία με τον Άγγελο μέσα στην εβδομάδα"),
 ],
 "gloss": {"νοσηλεύτρια": "νοσηλεύτρια — nurse (f.)", "διάλειμμα": "διάλειμμα — break (at school)", "ελαφρά": "ελαφρά — slightly", "γόνατο": "γόνατο — knee", "πληγή": "πληγή — wound", "γάζα": "γάζα — gauze", "κοκκινίζει": "κοκκινίζω — to go red", "πρήζεται": "πρήζομαι — to swell", "αρχείο": "αρχείο — file, records", "βιβλιάριο εμβολίων": "βιβλιάριο εμβολίων — vaccination record", "φωτοτυπία": "φωτοτυπία — photocopy"},
})

ITEMS.append({
 "id": "l164-vm-praktoreio", "title": "Μήνυμα από το ταξιδιωτικό πρακτορείο", "title_en": "A message from the travel agency", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από το ταξιδιωτικό πρακτορείο όπου κλείσατε μια εκδρομή.",
 "script": [
  L("Υπάλληλος", "m", "Καλησπέρα, εδώ Γιώργος από το ταξιδιωτικό πρακτορείο. Σας παίρνω για την εκδρομή στα Μετέωρα το Σάββατο. Επειδή δηλώθηκαν λιγότερα άτομα απ' όσα περιμέναμε, δεν θα πάμε με το μεγάλο πούλμαν αλλά με ένα μικρότερο, είκοσι θέσεων.", "Good evening, this is Giorgos from the travel agency. I'm calling about the trip to Meteora on Saturday. Because fewer people signed up than we expected, we won't go by the big coach but by a smaller one, with twenty seats."),
  L("Υπάλληλος", "m", "Αυτό σημαίνει ότι η αναχώρηση αλλάζει: δεν θα φύγουμε από την πλατεία, αλλά από τον σταθμό του μετρό, στις επτά ακριβώς, όχι επτά και μισή. Το πρόγραμμα της εκδρομής μένει ίδιο, με επίσκεψη σε δύο μοναστήρια και φαγητό στην Καλαμπάκα.", "This means the departure changes: we won't leave from the square, but from the metro station, at seven sharp, not half past seven. The trip programme stays the same, with a visit to two monasteries and lunch in Kalambaka."),
  L("Υπάλληλος", "m", "Να σας θυμίσω ότι στα μοναστήρια οι γυναίκες πρέπει να φορούν φούστα κάτω από το γόνατο και οι άντρες μακρύ παντελόνι. Αν η νέα ώρα δεν σας βολεύει, μπορούμε να σας επιστρέψουμε ολόκληρο το ποσό. Πείτε μας μόνο μέχρι την Πέμπτη.", "Let me remind you that in the monasteries women must wear a skirt below the knee and men long trousers. If the new time doesn't suit you, we can refund the whole amount. Just let us know by Thursday."),
 ],
 "questions": [
  Q("Γιατί αλλάζει το λεωφορείο;", ["Γιατί χάλασε το μεγάλο πούλμαν", "Γιατί δηλώθηκαν λιγότερα άτομα απ' όσα περίμεναν", "Γιατί ο δρόμος είναι στενός", "Γιατί άλλαξε η εταιρεία"], 1, "Επειδή δηλώθηκαν λιγότερα άτομα απ' όσα περιμέναμε"),
  Q("Από πού και πότε θα γίνει η αναχώρηση;", ["Από την πλατεία στις επτά και μισή", "Από τον σταθμό του μετρό στις επτά ακριβώς", "Από το πρακτορείο στις οκτώ", "Από τον σταθμό του μετρό στις επτά και μισή"], 1, "από τον σταθμό του μετρό, στις επτά ακριβώς"),
  Q("Τι γίνεται αν η νέα ώρα δεν σας βολεύει;", ["Μπορείτε να πάτε σε άλλη εκδρομή", "Πρέπει να πληρώσετε πρόστιμο", "Σας επιστρέφουν ολόκληρο το ποσό, αν το πείτε ως την Πέμπτη", "Σας επιστρέφουν το μισό ποσό"], 2, "μπορούμε να σας επιστρέψουμε ολόκληρο το ποσό"),
 ],
 "gloss": {"ταξιδιωτικό πρακτορείο": "ταξιδιωτικό πρακτορείο — travel agency", "εκδρομή": "εκδρομή — excursion, trip", "Μετέωρα": "Μετέωρα — Meteora", "δηλώθηκαν": "δηλώνομαι — to be registered, to sign up", "πούλμαν": "πούλμαν — coach", "αναχώρηση": "αναχώρηση — departure", "μοναστήρια": "μοναστήρι — monastery", "Καλαμπάκα": "Καλαμπάκα — Kalambaka", "φούστα": "φούστα — skirt", "ποσό": "ποσό — amount, sum"},
})

ITEMS.append({
 "id": "l164-c1-foucault", "title": "Ένα εκκρεμές που αποδεικνύει ότι η Γη γυρίζει", "title_en": "A pendulum that proves the Earth turns", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν φυσικό για το εκκρεμές του Φουκώ, που εκτίθεται σε πολλά μουσεία επιστημών.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι ακριβώς έδειξε ο Λεόν Φουκώ το 1851;", "What exactly did Léon Foucault show in 1851?"),
  L("Φυσικός", "m", "Έδειξε, για πρώτη φορά με ένα απλό πείραμα που μπορούσε να δει ο καθένας, ότι η Γη περιστρέφεται γύρω από τον άξονά της. Την ίδια χρονιά κρέμασε από τον τρούλο του Πανθέου, στο Παρίσι, μια μεταλλική σφαίρα στην άκρη ενός σύρματος μήκους εξήντα επτά μέτρων και την έβαλε να ταλαντεύεται.", "He showed, for the first time with a simple experiment that anyone could see, that the Earth rotates on its axis. That same year he hung from the dome of the Panthéon, in Paris, a metal sphere at the end of a wire sixty-seven metres long and set it swinging."),
  L("Δημοσιογράφος", "f", "Και τι είδαν οι θεατές;", "And what did the spectators see?"),
  L("Φυσικός", "m", "Ότι το επίπεδο στο οποίο ταλαντευόταν το εκκρεμές μετατοπιζόταν αργά, ώρα με την ώρα, σαν να το έσπρωχνε ένα αόρατο χέρι. Στην πραγματικότητα το εκκρεμές διατηρεί σταθερό το επίπεδο της ταλάντωσής του· αυτό που κινείται είναι το πάτωμα από κάτω του, μαζί με όλη τη Γη. Ένας παρατηρητής πάνω στη Γη, όμως, ερμηνεύει την κίνηση ανάποδα.", "That the plane in which the pendulum swung shifted slowly, hour by hour, as if an invisible hand were pushing it. In reality the pendulum keeps the plane of its swing constant; what moves is the floor beneath it, along with the whole Earth. An observer on the Earth, however, interprets the motion the other way round."),
  L("Δημοσιογράφος", "f", "Πόσο χρόνο χρειάζεται για να κάνει μια πλήρη στροφή;", "How long does it need to make a full turn?"),
  L("Φυσικός", "m", "Εξαρτάται από το γεωγραφικό πλάτος. Σε έναν από τους πόλους, μια πλήρης στροφή θα διαρκούσε περίπου μία μέρα. Στο Παρίσι χρειάζονται γύρω στις τριάντα δύο ώρες, και όσο πλησιάζουμε προς τον ισημερινό ο χρόνος μεγαλώνει, ώσπου πάνω στον ισημερινό το επίπεδο δεν μετατοπίζεται καθόλου. Αυτή η εξάρτηση από το πλάτος ήταν άλλωστε ένα από τα πιο πειστικά στοιχεία ότι η εξήγηση του Φουκώ ήταν σωστή.", "It depends on the latitude. At one of the poles, a full turn would last about one day. In Paris it takes around thirty-two hours, and the closer we get to the equator, the longer the time, until on the equator the plane doesn't shift at all. This dependence on latitude was, moreover, one of the most convincing pieces of evidence that Foucault's explanation was right."),
 ],
 "questions": [
  Q("Πού έγινε η διάσημη επίδειξη του 1851;", ["Στο Αστεροσκοπείο του Παρισιού", "Στον τρούλο του Πανθέου, στο Παρίσι", "Σε ένα πανεπιστήμιο του Λονδίνου", "Στον Πύργο του Άιφελ"], 1, "κρέμασε από τον τρούλο του Πανθέου, στο Παρίσι"),
  Q("Τι πραγματικά κινείται, κατά τον φυσικό;", ["Το επίπεδο ταλάντωσης του εκκρεμούς", "Ο αέρας γύρω από τη σφαίρα", "Το πάτωμα από κάτω, μαζί με όλη τη Γη", "Το σύρμα"], 2, "αυτό που κινείται είναι το πάτωμα από κάτω του, μαζί με όλη τη Γη"),
  Q("Τι συμβαίνει πάνω στον ισημερινό;", ["Το επίπεδο κάνει μια στροφή σε μία μέρα", "Το επίπεδο δεν μετατοπίζεται καθόλου", "Το εκκρεμές σταματά", "Η στροφή διαρκεί τριάντα δύο ώρες"], 1, "πάνω στον ισημερινό το επίπεδο δεν μετατοπίζεται καθόλου"),
  Q("Γιατί η εξάρτηση από το γεωγραφικό πλάτος ήταν σημαντική;", ["Γιατί επέτρεψε τη μέτρηση της απόστασης από τον Ήλιο", "Γιατί ήταν ένα από τα πιο πειστικά στοιχεία ότι η εξήγηση ήταν σωστή", "Γιατί έδειξε ότι η Γη δεν είναι σφαιρική", "Γιατί βοήθησε στην κατασκευή ρολογιών"], 1, "ήταν άλλωστε ένα από τα πιο πειστικά στοιχεία ότι η εξήγηση του Φουκώ ήταν σωστή"),
 ],
 "gloss": {"εκκρεμές": "εκκρεμές — pendulum", "Φουκώ": "Φουκώ — Foucault", "εκτίθεται": "εκτίθεμαι — to be exhibited", "άξονά": "άξονας — axis", "τρούλο": "τρούλος — dome", "Πανθέου": "Πάνθεον — the Panthéon", "σφαίρα": "σφαίρα — sphere", "σύρματος": "σύρμα — wire", "ταλαντεύεται": "ταλαντεύομαι — to swing, to oscillate", "επίπεδο": "επίπεδο — plane", "μετατοπιζόταν": "μετατοπίζομαι — to shift", "αόρατο": "αόρατος — invisible", "ταλάντωσής": "ταλάντωση — oscillation", "ερμηνεύει": "ερμηνεύω — to interpret", "γεωγραφικό πλάτος": "γεωγραφικό πλάτος — latitude", "πόλους": "πόλος — pole", "ισημερινό": "ισημερινός — equator", "πειστικά": "πειστικός — convincing"},
})

ITEMS.append({
 "id": "l164-c1-ouranio-toxo", "title": "Η γεωμετρία του ουράνιου τόξου", "title_en": "The geometry of the rainbow", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια καθηγήτρια φυσικής να εξηγεί σε μια εκλαϊκευτική ομιλία πώς σχηματίζεται το ουράνιο τόξο.",
 "script": [
  L("Καθηγήτρια", "f", "Όλοι έχουμε δει ουράνιο τόξο, λίγοι όμως έχουν προσέξει πότε ακριβώς εμφανίζεται. Πρώτη προϋπόθεση: ο ήλιος πρέπει να βρίσκεται πίσω μας και η βροχή μπροστά μας. Δεύτερη: ο ήλιος πρέπει να είναι σχετικά χαμηλά, γι' αυτό τα ουράνια τόξα τα βλέπουμε συνήθως νωρίς το πρωί ή αργά το απόγευμα, σπάνια το καλοκαιρινό μεσημέρι.", "We've all seen a rainbow, but few have noticed exactly when it appears. First condition: the sun must be behind us and the rain in front of us. Second: the sun must be relatively low, which is why we usually see rainbows early in the morning or late in the afternoon, rarely at midday in summer."),
  L("Καθηγήτρια", "f", "Τι συμβαίνει μέσα σε κάθε σταγόνα; Το φως μπαίνει, διαθλάται, ανακλάται στο πίσω μέρος της σταγόνας και βγαίνει ξανά προς τα πίσω. Επειδή κάθε χρώμα διαθλάται λίγο διαφορετικά, το λευκό φως αναλύεται στα χρώματά του. Το αποτέλεσμα είναι ότι βλέπουμε το τόξο πάντα υπό γωνία περίπου σαράντα δύο μοιρών από το σημείο που βρίσκεται ακριβώς απέναντι από τον ήλιο. Γι' αυτό το ουράνιο τόξο δεν έχει συγκεκριμένη θέση: κάθε παρατηρητής βλέπει το δικό του, σχηματισμένο από διαφορετικές σταγόνες.", "What happens inside each drop? Light enters, is refracted, is reflected at the back of the drop and comes out again backwards. Because each colour is refracted slightly differently, white light is split into its colours. The result is that we always see the bow at an angle of about forty-two degrees from the point directly opposite the sun. That's why the rainbow has no fixed position: each observer sees their own, formed by different drops."),
  L("Καθηγήτρια", "f", "Αν είστε τυχεροί, θα δείτε και ένα δεύτερο, πιο αχνό τόξο, πιο ψηλά, με τα χρώματα σε ανάποδη σειρά. Εκεί το φως έχει ανακλαστεί δύο φορές μέσα στη σταγόνα. Και ανάμεσα στα δύο τόξα ο ουρανός είναι εμφανώς πιο σκοτεινός. Η σκοτεινή αυτή ζώνη ονομάζεται ζώνη του Αλεξάνδρου, από τον Αλέξανδρο τον Αφροδισιέα, έναν φιλόσοφο που την περιέγραψε γύρω στο 200 μ.Χ. Είναι ωραίο να σκέφτεται κανείς ότι κάτι που εξηγείται με τη γεωμετρία είχε παρατηρηθεί με προσοχή πριν από δεκαοκτώ αιώνες.", "If you're lucky, you'll also see a second, fainter bow, higher up, with the colours in reverse order. There the light has been reflected twice inside the drop. And between the two bows the sky is noticeably darker. This dark band is called Alexander's band, after Alexander of Aphrodisias, a philosopher who described it around 200 AD. It's nice to think that something explained by geometry was carefully observed eighteen centuries ago."),
 ],
 "questions": [
  Q("Ποια είναι η πρώτη προϋπόθεση για να δούμε ουράνιο τόξο;", ["Να έχει σταματήσει η βροχή", "Ο ήλιος να είναι πίσω μας και η βροχή μπροστά μας", "Να είναι μεσημέρι", "Να βρισκόμαστε σε ύψωμα"], 1, "ο ήλιος πρέπει να βρίσκεται πίσω μας και η βροχή μπροστά μας"),
  Q("Γιατί σπάνια βλέπουμε ουράνιο τόξο το καλοκαιρινό μεσημέρι;", ["Γιατί ο ήλιος είναι πολύ ψηλά", "Γιατί δεν βρέχει το καλοκαίρι", "Γιατί υπάρχει πολλή υγρασία", "Γιατί ο ουρανός είναι πολύ φωτεινός"], 0, "ο ήλιος πρέπει να είναι σχετικά χαμηλά"),
  Q("Γιατί, κατά την καθηγήτρια, κάθε παρατηρητής βλέπει το δικό του ουράνιο τόξο;", ["Γιατί κάθε μάτι βλέπει τα χρώματα διαφορετικά", "Γιατί το τόξο κινείται με τον άνεμο", "Γιατί σχηματίζεται από διαφορετικές σταγόνες για τον καθένα", "Γιατί το τόξο υπάρχει μόνο στη φαντασία μας"], 2, "κάθε παρατηρητής βλέπει το δικό του, σχηματισμένο από διαφορετικές σταγόνες"),
  Q("Τι είναι η ζώνη του Αλεξάνδρου;", ["Το πιο φωτεινό τμήμα του τόξου", "Η σκοτεινή ζώνη ανάμεσα στα δύο τόξα", "Το εσωτερικό του πρώτου τόξου", "Το κόκκινο χρώμα του δεύτερου τόξου"], 1, "ανάμεσα στα δύο τόξα ο ουρανός είναι εμφανώς πιο σκοτεινός"),
 ],
 "gloss": {"ουράνιο τόξο": "ουράνιο τόξο — rainbow", "εκλαϊκευτική": "εκλαϊκευτικός — popular-science", "προϋπόθεση": "προϋπόθεση — condition, prerequisite", "σταγόνα": "σταγόνα — drop", "διαθλάται": "διαθλώμαι — to be refracted", "ανακλάται": "ανακλώμαι — to be reflected", "αναλύεται": "αναλύομαι — to be split up", "γωνία": "γωνία — angle", "μοιρών": "μοίρα — degree", "αχνό": "αχνός — faint", "ανακλαστεί": "ανακλώμαι — to be reflected", "εμφανώς": "εμφανώς — noticeably", "ζώνη": "ζώνη — band, zone", "Αφροδισιέα": "Αφροδισιεύς — of Aphrodisias"},
})

rnd = random.Random(164)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-164.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
