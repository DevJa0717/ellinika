# Source for library/listening/listening-92.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l92.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l92-ann-leoforeia-anti-trena", "title": "Λεωφορεία αντί για τρένα", "title_en": "Buses instead of trains", "type": "announcement", "level": "B2",
 "context_el": "Περιμένετε στην αποβάθρα ενός σιδηροδρομικού σταθμού και ακούτε μια ανακοίνωση.",
 "script": [
  L("Εκφωνητής", "m", "Κυρίες και κύριοι, σας ενημερώνουμε ότι, λόγω εργασιών συντήρησης στη γραμμή, από σήμερα και μέχρι την Κυριακή δεν θα πραγματοποιούνται δρομολόγια τρένων ανάμεσα στους σταθμούς Λιανοκλαδίου και Δομοκού.", "Ladies and gentlemen, please be informed that, because of maintenance work on the line, from today until Sunday there will be no train services between Lianokladi and Domokos stations."),
  L("Εκφωνητής", "m", "Οι επιβάτες θα μεταφέρονται με λεωφορεία, τα οποία αναχωρούν από τον χώρο στάθμευσης μπροστά στον σταθμό, δεκαπέντε λεπτά μετά την άφιξη κάθε τρένου. Τα εισιτήρια που έχετε ήδη αγοράσει ισχύουν κανονικά και για τα λεωφορεία. Η διαδρομή θα διαρκεί περίπου σαράντα λεπτά περισσότερο από το συνηθισμένο.", "Passengers will be taken by bus; the buses leave from the car park in front of the station fifteen minutes after each train arrives. Tickets you have already bought are valid for the buses as normal. The journey will take about forty minutes longer than usual."),
  L("Εκφωνητής", "m", "Επιβάτες με ποδήλατα ή ογκώδεις αποσκευές παρακαλούνται να απευθυνθούν στο εκδοτήριο, καθώς ο χώρος στα λεωφορεία είναι περιορισμένος. Ζητούμε συγγνώμη για την ταλαιπωρία.", "Passengers with bicycles or bulky luggage are asked to go to the ticket office, as space on the buses is limited. We apologise for the inconvenience."),
 ],
 "questions": [
  Q("Γιατί δεν θα κινούνται τρένα ανάμεσα στους δύο σταθμούς;", ["Λόγω απεργίας", "Λόγω εργασιών συντήρησης στη γραμμή", "Λόγω κακοκαιρίας", "Λόγω ατυχήματος"], 1, "λόγω εργασιών συντήρησης στη γραμμή"),
  Q("Τι ισχύει για τα εισιτήρια;", ["Πρέπει να αγοράσουν καινούργια", "Επιστρέφονται τα χρήματα", "Ισχύουν κανονικά και για τα λεωφορεία", "Ισχύουν μόνο μέχρι την Κυριακή"], 2, "Τα εισιτήρια που έχετε ήδη αγοράσει ισχύουν κανονικά και για τα λεωφορεία"),
  Q("Τι πρέπει να κάνουν όσοι έχουν ποδήλατο;", ["Να το αφήσουν στον σταθμό", "Να απευθυνθούν στο εκδοτήριο", "Να πάρουν ταξί", "Να περιμένουν το επόμενο τρένο"], 1, "παρακαλούνται να απευθυνθούν στο εκδοτήριο"),
 ],
 "gloss": {"αποβάθρα": "αποβάθρα — platform", "σιδηροδρομικού": "σιδηροδρομικός — railway (adjective)", "συντήρησης": "συντήρηση — maintenance", "πραγματοποιούνται": "πραγματοποιούμαι — to take place, run", "δρομολόγια": "δρομολόγιο — service, scheduled trip", "χώρο στάθμευσης": "χώρος στάθμευσης — car park", "άφιξη": "άφιξη — arrival", "ισχύουν": "ισχύω — to be valid", "ογκώδεις": "ογκώδης — bulky", "αποσκευές": "αποσκευές — luggage", "εκδοτήριο": "εκδοτήριο — ticket office", "ταλαιπωρία": "ταλαιπωρία — inconvenience"}
})
ITEMS.append({
 "id": "l92-vm-kourdistis", "title": "Μήνυμα από τον κουρδιστή πιάνων", "title_en": "A message from the piano tuner", "type": "voicemail", "level": "B2",
 "context_el": "Είχατε κλείσει ραντεβού με έναν κουρδιστή για το παλιό πιάνο σας. Ακούτε ένα μήνυμα στο κινητό σας.",
 "script": [
  L("Κουρδιστής", "m", "Καλημέρα σας, ο Σπύρος Ζαχαρίου είμαι, ο κουρδιστής. Είχαμε κανονίσει να έρθω την Τετάρτη για το πιάνο σας, αλλά δυστυχώς ένα παλιό πιάνο σε ένα σχολείο χρειάζεται επείγουσα επισκευή πριν από τη συναυλία τους, οπότε θα σας παρακαλέσω να το μεταθέσουμε για την επόμενη Δευτέρα, στις έντεκα, αν σας βολεύει.", "Good morning, this is Spyros Zachariou, the tuner. We had arranged for me to come on Wednesday for your piano, but unfortunately an old piano at a school needs an urgent repair before their concert, so I'd ask you to move it to next Monday at eleven, if that suits you."),
  L("Κουρδιστής", "m", "Από όσα μου είπατε στο τηλέφωνο, ότι το πιάνο έχει να κουρδιστεί πάνω από δέκα χρόνια, μάλλον θα χρειαστούν δύο επισκέψεις: στην πρώτη θα το ανεβάσω σιγά σιγά στο σωστό τόνισμα, και μετά από έναν μήνα θα το ξανακουρδίσω, γιατί οι χορδές θα έχουν χαλαρώσει πάλι.", "From what you told me on the phone, that the piano hasn't been tuned for more than ten years, it will probably need two visits: on the first I'll bring it up slowly to the right pitch, and after a month I'll tune it again, because the strings will have slackened again."),
  L("Κουρδιστής", "m", "Μια παράκληση: μην το έχετε κοντά στο καλοριφέρ ή σε παράθυρο με ήλιο, γιατί η ζέστη και η υγρασία το χαλάνε γρήγορα. Πάρτε με όποτε μπορείτε να μου πείτε για τη Δευτέρα. Ευχαριστώ!", "One request: don't keep it near the radiator or by a sunny window, because heat and humidity ruin it quickly. Call me whenever you can to tell me about Monday. Thank you!"),
 ],
 "questions": [
  Q("Γιατί ο κουρδιστής θέλει να αλλάξει το ραντεβού;", ["Γιατί είναι άρρωστος", "Γιατί ένα πιάνο σχολείου χρειάζεται επείγουσα επισκευή", "Γιατί θα λείπει σε ταξίδι", "Γιατί δεν έχει τα εργαλεία του"], 1, "ένα παλιό πιάνο σε ένα σχολείο χρειάζεται επείγουσα επισκευή"),
  Q("Γιατί θα χρειαστούν μάλλον δύο επισκέψεις;", ["Γιατί το πιάνο έχει να κουρδιστεί πάνω από δέκα χρόνια", "Γιατί λείπουν χορδές", "Γιατί το πιάνο είναι πολύ μεγάλο", "Γιατί πρέπει να το μεταφέρει"], 0, "το πιάνο έχει να κουρδιστεί πάνω από δέκα χρόνια"),
  Q("Τι συμβουλεύει για τη θέση του πιάνου;", ["Να είναι κοντά σε παράθυρο", "Να μην είναι κοντά στο καλοριφέρ ή σε παράθυρο με ήλιο", "Να είναι σε υπόγειο", "Να σκεπάζεται πάντα"], 1, "μην το έχετε κοντά στο καλοριφέρ ή σε παράθυρο με ήλιο"),
 ],
 "gloss": {"κουρδιστή": "κουρδιστής — (piano) tuner", "επείγουσα": "επείγων — urgent", "μεταθέσουμε": "μεταθέτω — to postpone, move", "βολεύει": "με βολεύει — it suits me", "κουρδιστεί": "κουρδίζομαι — to be tuned", "τόνισμα": "τόνισμα — pitch, tuning", "ξανακουρδίσω": "ξανακουρδίζω — to retune", "χορδές": "χορδή — string", "χαλαρώσει": "χαλαρώνω — to slacken", "καλοριφέρ": "καλοριφέρ — radiator", "υγρασία": "υγρασία — humidity"}
})
ITEMS.append({
 "id": "l92-dia-katharistirio-lekes", "title": "Ένας λεκές που δεν έφυγε", "title_en": "A stain that didn't come out", "type": "dialogue", "level": "B2",
 "context_el": "Μια γυναίκα επιστρέφει στο καθαριστήριο για να παραλάβει ένα φόρεμα.",
 "script": [
  L("Πελάτισσα", "f", "Καλησπέρα. Ήρθα να πάρω το φόρεμα που σας έφερα την Παρασκευή. Ορίστε η απόδειξη.", "Good evening. I've come to collect the dress I brought you on Friday. Here's the receipt."),
  L("Υπάλληλος", "m", "Καλησπέρα. Μισό λεπτό… Α, ναι, το μπλε μεταξωτό. Πρέπει να σας πω ότι ο λεκές του κρασιού δεν έφυγε εντελώς. Δοκιμάσαμε δύο φορές, αλλά το ύφασμα είναι πολύ λεπτό και δεν θέλαμε να το καταστρέψουμε.", "Good evening. Just a moment... Ah yes, the blue silk one. I have to tell you that the wine stain didn't come out completely. We tried twice, but the fabric is very delicate and we didn't want to ruin it."),
  L("Πελάτισσα", "f", "Αχ, κρίμα. Το θέλω για έναν γάμο το Σάββατο. Φαίνεται πολύ;", "Oh, what a shame. I want it for a wedding on Saturday. Is it very noticeable?"),
  L("Υπάλληλος", "m", "Κοιτάξτε κι εσείς: έχει μείνει μια ελαφριά σκιά, στο κάτω μέρος της φούστας. Αν θέλετε, μπορούμε να το στείλουμε σε ένα εξειδικευμένο εργαστήριο που συνεργαζόμαστε, αλλά θα κάνει μία εβδομάδα και κοστίζει δεκαοχτώ ευρώ επιπλέον.", "Have a look yourself: a faint shadow has remained, at the bottom of the skirt. If you like, we can send it to a specialist workshop we work with, but it will take a week and costs eighteen euros extra."),
  L("Πελάτισσα", "f", "Μία εβδομάδα δεν με βολεύει. Θα το πάρω έτσι, και ίσως το καλύψω με μια ζώνη ή ένα σάλι. Μου κάνετε όμως μια μικρή έκπτωση, αφού δεν καθάρισε τελείως;", "A week doesn't suit me. I'll take it as it is, and maybe cover it with a belt or a shawl. But will you give me a small discount, since it didn't come completely clean?"),
  L("Υπάλληλος", "m", "Δίκιο έχετε. Θα σας χρεώσω μόνο το σιδέρωμα. Και την επόμενη φορά, αν λερωθεί κάτι, φέρτε το όσο πιο γρήγορα γίνεται: ένας φρέσκος λεκές βγαίνει πολύ πιο εύκολα.", "You're right. I'll only charge you for the ironing. And next time, if something gets stained, bring it in as quickly as possible: a fresh stain comes out much more easily."),
 ],
 "questions": [
  Q("Γιατί ο λεκές δεν έφυγε εντελώς;", ["Γιατί ήταν πολύ παλιός", "Γιατί το ύφασμα είναι πολύ λεπτό", "Γιατί χάλασε το μηχάνημα", "Γιατί η πελάτισσα το έφερε αργά"], 1, "το ύφασμα είναι πολύ λεπτό"),
  Q("Γιατί η πελάτισσα δεν στέλνει το φόρεμα στο εξειδικευμένο εργαστήριο;", ["Γιατί κοστίζει πολύ", "Γιατί δεν εμπιστεύεται το εργαστήριο", "Γιατί θα κάνει μία εβδομάδα και το θέλει για το Σάββατο", "Γιατί ο λεκές δεν φαίνεται καθόλου"], 2, "Μία εβδομάδα δεν με βολεύει"),
  Q("Τι θα πληρώσει τελικά;", ["Ολόκληρο το καθάρισμα", "Τίποτα", "Μόνο το σιδέρωμα", "Δεκαοχτώ ευρώ"], 2, "Θα σας χρεώσω μόνο το σιδέρωμα"),
 ],
 "gloss": {"καθαριστήριο": "καθαριστήριο — dry cleaner's", "απόδειξη": "απόδειξη — receipt", "μεταξωτό": "μεταξωτός — silk", "λεκές": "λεκές — stain", "ύφασμα": "ύφασμα — fabric", "σκιά": "σκιά — shadow, faint mark", "φούστας": "φούστα — skirt", "εξειδικευμένο": "εξειδικευμένος — specialised", "σάλι": "σάλι — shawl", "έκπτωση": "έκπτωση — discount", "σιδέρωμα": "σιδέρωμα — ironing", "λερωθεί": "λερώνομαι — to get dirty, stained"}
})
ITEMS.append({
 "id": "l92-int-fylakas-archaiotiton", "title": "Η φύλακας αρχαιοτήτων", "title_en": "The antiquities guard", "type": "interview", "level": "B2",
 "context_el": "Σε μια εκπομπή για επαγγέλματα, ένας δημοσιογράφος μιλά με μια φύλακα αρχαιοτήτων σε έναν μεγάλο αρχαιολογικό χώρο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί πιστεύουν ότι η δουλειά σας είναι να κάθεστε σε μια καρέκλα και να κόβετε εισιτήρια. Ισχύει;", "Many people think your job is to sit on a chair and tear tickets. Is that true?"),
  L("Φύλακας", "f", "Καθόλου. Τα εισιτήρια τα κόβουν άλλοι συνάδελφοι. Εμείς κάνουμε περιπολίες σε όλο τον χώρο, προσέχουμε να μην ανεβαίνει κανείς στα μνημεία, να μην αγγίζει τα γλυπτά και να μην παίρνει πέτρες για ενθύμιο. Και κάθε καλοκαίρι βοηθάμε δεκάδες επισκέπτες που παθαίνουν θερμοπληξία.", "Not at all. Other colleagues tear the tickets. We patrol the whole site, we make sure no one climbs on the monuments, touches the sculptures or takes stones as a souvenir. And every summer we help dozens of visitors who get heatstroke."),
  L("Δημοσιογράφος", "m", "Παίρνουν πράγματι πέτρες οι επισκέπτες;", "Do visitors really take stones?"),
  L("Φύλακας", "f", "Δυστυχώς, ναι. Οι περισσότεροι δεν καταλαβαίνουν ότι ένα μικρό κομμάτι μάρμαρο είναι κι αυτό αρχαιότητα. Όταν τους το εξηγήσω, συνήθως ντρέπονται και το επιστρέφουν. Κάποιοι μάλιστα μας στέλνουν πέτρες με το ταχυδρομείο, χρόνια αργότερα, με ένα γράμμα που ζητούν συγγνώμη.", "Unfortunately, yes. Most don't realise that a small piece of marble is also an antiquity. When I explain it to them, they're usually embarrassed and give it back. Some even send us stones by post, years later, with a letter apologising."),
  L("Δημοσιογράφος", "m", "Ποια είναι η αγαπημένη σας ώρα στον χώρο;", "What is your favourite time of day at the site?"),
  L("Φύλακας", "f", "Το πρωί, πριν ανοίξουμε. Κάνω τον πρώτο γύρο μόνη μου, όταν ο ήλιος μόλις έχει βγει και τα μάρμαρα έχουν ένα ροζ χρώμα. Τότε νιώθω ότι φυλάω κάτι που δεν ανήκει μόνο σε εμάς, αλλά και σε όσους θα έρθουν μετά από εμάς.", "In the morning, before we open. I do the first round alone, when the sun has just come up and the marble has a pink colour. Then I feel that I'm guarding something that belongs not only to us but also to those who will come after us."),
 ],
 "questions": [
  Q("Τι λέει η φύλακας για τα εισιτήρια;", ["Ότι τα κόβει η ίδια", "Ότι τα κόβουν άλλοι συνάδελφοι", "Ότι είναι πολύ ακριβά", "Ότι πωλούνται μόνο ηλεκτρονικά"], 1, "Τα εισιτήρια τα κόβουν άλλοι συνάδελφοι"),
  Q("Πώς αντιδρούν συνήθως οι επισκέπτες όταν τους εξηγεί ότι η πέτρα είναι αρχαιότητα;", ["Θυμώνουν", "Ντρέπονται και την επιστρέφουν", "Την κρύβουν", "Ζητούν να την αγοράσουν"], 1, "συνήθως ντρέπονται και το επιστρέφουν"),
  Q("Ποια είναι η αγαπημένη της ώρα;", ["Το μεσημέρι", "Το απόγευμα, όταν φεύγουν οι επισκέπτες", "Το πρωί, πριν ανοίξει ο χώρος", "Το βράδυ, όταν φωτίζονται τα μνημεία"], 2, "Το πρωί, πριν ανοίξουμε"),
 ],
 "gloss": {"φύλακα": "φύλακας — guard", "αρχαιοτήτων": "αρχαιότητα — antiquity", "περιπολίες": "περιπολία — patrol", "μνημεία": "μνημείο — monument", "γλυπτά": "γλυπτό — sculpture", "ενθύμιο": "ενθύμιο — souvenir, keepsake", "θερμοπληξία": "θερμοπληξία — heatstroke", "μάρμαρο": "μάρμαρο — marble", "ντρέπονται": "ντρέπομαι — to be embarrassed", "φυλάω": "φυλάω — to guard"}
})
ITEMS.append({
 "id": "l92-rep-lefkada", "title": "Λευκάδα, το νησί που φτάνεις με το αυτοκίνητο", "title_en": "Lefkada, the island you can drive to", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ταξιδιωτικό ρεπορτάζ στο ραδιόφωνο.",
 "script": [
  L("Ρεπόρτερ", "m", "Η Λευκάδα είναι ένα από τα λίγα ελληνικά νησιά όπου μπορείς να φτάσεις χωρίς πλοίο. Μια μικρή πλωτή γέφυρα τη συνδέει με την Αιτωλοακαρνανία, και κάθε ώρα ανοίγει για να περάσουν τα ιστιοφόρα, ενώ τα αυτοκίνητα περιμένουν υπομονετικά.", "Lefkada is one of the few Greek islands you can reach without a ferry. A small floating bridge links it to Aetolia-Acarnania, and every hour it opens to let the sailing boats through, while the cars wait patiently."),
  L("Ρεπόρτερ", "m", "Η δυτική ακτή είναι γνωστή για τις παραλίες της με τα άσπρα βράχια και τα τιρκουάζ νερά, όπως το Πόρτο Κατσίκι. Στο νότιο άκρο του νησιού, στο ακρωτήριο Λευκάτας, ένας φάρος στέκεται πάνω σε έναν γκρεμό εξήντα μέτρων. Σύμφωνα με την παράδοση, από εκεί έπεσε στη θάλασσα η ποιήτρια Σαπφώ, από έναν έρωτα χωρίς ανταπόκριση.", "The west coast is known for its beaches with white cliffs and turquoise water, such as Porto Katsiki. At the southern tip of the island, on Cape Lefkatas, a lighthouse stands on a sixty-metre cliff. According to tradition, it was from there that the poet Sappho threw herself into the sea, over an unrequited love."),
  L("Ρεπόρτερ", "m", "Το νησί έχει και πλούσια πνευματική ζωή. Εδώ γεννήθηκαν οι ποιητές Αριστοτέλης Βαλαωρίτης και Άγγελος Σικελιανός, αλλά και ο συγγραφέας Λευκάδιος Χερν, που πήρε το όνομά του από το νησί. Κάθε Αύγουστο, εδώ και πάνω από εξήντα χρόνια, η πόλη φιλοξενεί ένα διεθνές φεστιβάλ φολκλόρ, με χορευτικά συγκροτήματα από όλο τον κόσμο.", "The island also has a rich intellectual life. The poets Aristotelis Valaoritis and Angelos Sikelianos were born here, as was the writer Lafcadio Hearn, who took his name from the island. Every August, for over sixty years now, the town has hosted an international folklore festival, with dance groups from all over the world."),
 ],
 "questions": [
  Q("Τι είναι ξεχωριστό στη Λευκάδα;", ["Έχει αεροδρόμιο στο κέντρο της", "Μπορείς να φτάσεις χωρίς πλοίο", "Δεν επιτρέπονται αυτοκίνητα", "Έχει τρένο"], 1, "μπορείς να φτάσεις χωρίς πλοίο"),
  Q("Τι λέει η παράδοση για το ακρωτήριο Λευκάτας;", ["Ότι εκεί γεννήθηκε η Σαπφώ", "Ότι εκεί ναυάγησε ένα πλοίο", "Ότι από εκεί έπεσε στη θάλασσα η Σαπφώ", "Ότι εκεί έζησε ο Σικελιανός"], 2, "από εκεί έπεσε στη θάλασσα η ποιήτρια Σαπφώ"),
  Q("Τι γίνεται κάθε Αύγουστο;", ["Ένα φεστιβάλ κινηματογράφου", "Ένα διεθνές φεστιβάλ φολκλόρ", "Αγώνες ιστιοπλοΐας", "Ένα φεστιβάλ ποίησης"], 1, "η πόλη φιλοξενεί ένα διεθνές φεστιβάλ φολκλόρ"),
 ],
 "gloss": {"πλωτή": "πλωτός — floating", "γέφυρα": "γέφυρα — bridge", "ιστιοφόρα": "ιστιοφόρο — sailing boat", "υπομονετικά": "υπομονετικά — patiently", "βράχια": "βράχος — rock, cliff", "τιρκουάζ": "τιρκουάζ — turquoise", "ακρωτήριο": "ακρωτήριο — cape", "γκρεμό": "γκρεμός — cliff, precipice", "ανταπόκριση": "ανταπόκριση — response (love returned)", "πνευματική": "πνευματικός — intellectual", "φολκλόρ": "φολκλόρ — folklore", "συγκροτήματα": "συγκρότημα — group, ensemble"}
})
ITEMS.append({
 "id": "l92-rep-kastoria", "title": "Καστοριά, η πόλη της λίμνης", "title_en": "Kastoria, the lake town", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια τηλεοπτική εκπομπή για ταξίδια στη βόρεια Ελλάδα.",
 "script": [
  L("Ρεπόρτερ", "f", "Η Καστοριά είναι χτισμένη σε μια χερσόνησο που μπαίνει βαθιά στη λίμνη Ορεστιάδα. Το πρωί, όταν η ομίχλη σηκώνεται πάνω από το νερό, οι πελεκάνοι και οι κύκνοι πλησιάζουν τόσο κοντά στην ακτή, που οι περαστικοί σταματούν για να τους φωτογραφίσουν.", "Kastoria is built on a peninsula that reaches deep into Lake Orestiada. In the morning, when the mist lifts over the water, the pelicans and swans come so close to the shore that passers-by stop to photograph them."),
  L("Ρεπόρτερ", "f", "Για αιώνες, η πόλη ζούσε από τη γούνα. Οι γουναράδες της ταξίδευαν σε όλη την Ευρώπη, και με τα κέρδη τους έχτισαν τα επιβλητικά αρχοντικά που βλέπουμε σήμερα στις γειτονιές Ντολτσό και Απόζαρι. Η Καστοριά είναι επίσης γνωστή για τις δεκάδες βυζαντινές εκκλησίες της, μερικές πολύ μικρές, με τοιχογραφίες που χρονολογούνται από τον ενδέκατο αιώνα.", "For centuries, the town lived from fur. Its furriers travelled all over Europe, and with their profits they built the imposing mansions we see today in the Doltso and Apozari neighbourhoods. Kastoria is also known for its dozens of Byzantine churches, some very small, with wall paintings dating from the eleventh century."),
  L("Ρεπόρτερ", "f", "Ο καλύτερος τρόπος για να γνωρίσει κανείς την πόλη είναι ο περίπατος γύρω από τη χερσόνησο, μια διαδρομή περίπου οχτώ χιλιομέτρων δίπλα στο νερό. Στη μέση της βρίσκεται το Σπήλαιο του Δράκου, με υπόγειες λίμνες. Και όποιος έρθει στις αρχές Ιανουαρίου, θα ζήσει τα Ραγκουτσάρια, ένα καρναβάλι τριών ημερών με μάσκες, μουσική και χορό στους δρόμους.", "The best way to get to know the town is the walk around the peninsula, a route of about eight kilometres beside the water. Halfway along is the Dragon's Cave, with underground lakes. And anyone who comes at the beginning of January will experience the Ragoutsaria, a three-day carnival with masks, music and dancing in the streets."),
 ],
 "questions": [
  Q("Τι βλέπουν οι περαστικοί το πρωί κοντά στην ακτή;", ["Ψαράδες με βάρκες", "Πελεκάνους και κύκνους", "Δελφίνια", "Κολυμβητές"], 1, "οι πελεκάνοι και οι κύκνοι πλησιάζουν τόσο κοντά στην ακτή"),
  Q("Από πού προήλθε ο πλούτος για τα αρχοντικά;", ["Από το εμπόριο κρασιού", "Από τη γούνα", "Από το ψάρεμα", "Από τον τουρισμό"], 1, "Για αιώνες, η πόλη ζούσε από τη γούνα"),
  Q("Τι είναι τα Ραγκουτσάρια;", ["Ένα βυζαντινό μοναστήρι", "Ένα σπήλαιο", "Ένα καρναβάλι τριών ημερών", "Ένα παραδοσιακό φαγητό"], 2, "ένα καρναβάλι τριών ημερών με μάσκες, μουσική και χορό στους δρόμους"),
 ],
 "gloss": {"χερσόνησο": "χερσόνησος — peninsula", "ομίχλη": "ομίχλη — mist, fog", "πελεκάνοι": "πελεκάνος — pelican", "κύκνοι": "κύκνος — swan", "γούνα": "γούνα — fur", "γουναράδες": "γουναράς — furrier", "επιβλητικά": "επιβλητικός — imposing", "αρχοντικά": "αρχοντικό — mansion", "χρονολογούνται": "χρονολογούμαι — to date (from)", "περίπατος": "περίπατος — walk, stroll", "Σπήλαιο": "σπήλαιο — cave", "μάσκες": "μάσκα — mask"}
})
ITEMS.append({
 "id": "l92-mono-choris-aftokinito", "title": "Ζω χωρίς αυτοκίνητο", "title_en": "I live without a car", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για την καθημερινότητα στην πόλη, ένας ακροατής διηγείται μια απόφασή του.",
 "script": [
  L("Ακροατής", "m", "Πριν από δύο χρόνια το αυτοκίνητό μου χάλασε για τρίτη φορά μέσα σε έναν χρόνο. Ο μηχανικός μού είπε ότι η επισκευή θα κόστιζε σχεδόν όσο αξίζει όλο το αυτοκίνητο. Τότε κάθισα και λογάριασα πόσα ξόδευα τον χρόνο: βενζίνη, ασφάλεια, τέλη κυκλοφορίας, σέρβις, πάρκινγκ. Το ποσό με τρόμαξε.", "Two years ago my car broke down for the third time in a year. The mechanic told me the repair would cost almost as much as the whole car is worth. So I sat down and worked out how much I was spending a year: petrol, insurance, road tax, servicing, parking. The amount frightened me."),
  L("Ακροατής", "m", "Αποφάσισα να δοκιμάσω για έναν μήνα να ζήσω χωρίς αυτοκίνητο. Αγόρασα κάρτα για τα μέσα μεταφοράς και ένα μεταχειρισμένο ποδήλατο. Τις πρώτες εβδομάδες ήταν δύσκολο: έπρεπε να οργανώνω καλύτερα τα ψώνια μου, και μια φορά βράχηκα μέχρι το κόκαλο περιμένοντας ένα λεωφορείο που δεν ήρθε ποτέ.", "I decided to try living without a car for a month. I bought a public transport card and a second-hand bicycle. The first weeks were hard: I had to organise my shopping better, and once I got soaked to the skin waiting for a bus that never came."),
  L("Ακροατής", "m", "Ο μήνας έγινε δύο χρόνια. Για τα μεγάλα ψώνια ή για ένα ταξίδι, νοικιάζω αυτοκίνητο για μία μέρα. Έχασα έξι κιλά χωρίς να πατήσω το πόδι μου σε γυμναστήριο, και διαβάζω ένα βιβλίο τον μήνα στο μετρό. Δεν λέω ότι είναι για όλους, ειδικά για όσους μένουν έξω από την πόλη. Για μένα, όμως, ήταν η καλύτερη απόφαση των τελευταίων χρόνων.", "The month became two years. For big shopping trips or a journey, I rent a car for a day. I've lost six kilos without setting foot in a gym, and I read a book a month on the metro. I'm not saying it's for everyone, especially for people who live outside the city. For me, though, it was the best decision of recent years."),
 ],
 "questions": [
  Q("Γιατί ο ακροατής σκέφτηκε να ζήσει χωρίς αυτοκίνητο;", ["Γιατί έχασε το δίπλωμά του", "Γιατί η επισκευή θα κόστιζε σχεδόν όσο αξίζει το αυτοκίνητο", "Γιατί μετακόμισε στο κέντρο", "Γιατί του το πρότεινε ο γιατρός του"], 1, "η επισκευή θα κόστιζε σχεδόν όσο αξίζει όλο το αυτοκίνητο"),
  Q("Τι ήταν δύσκολο τις πρώτες εβδομάδες;", ["Να βρει ποδήλατο", "Να οργανώνει καλύτερα τα ψώνια του", "Να πηγαίνει στη δουλειά", "Να πουλήσει το αυτοκίνητο"], 1, "έπρεπε να οργανώνω καλύτερα τα ψώνια μου"),
  Q("Τι κάνει όταν χρειάζεται αυτοκίνητο για ένα ταξίδι;", ["Δανείζεται από φίλους", "Παίρνει ταξί", "Νοικιάζει αυτοκίνητο για μία μέρα", "Δεν ταξιδεύει πια"], 2, "νοικιάζω αυτοκίνητο για μία μέρα"),
 ],
 "gloss": {"μηχανικός": "μηχανικός — mechanic", "λογάριασα": "λογαριάζω — to work out, calculate", "ασφάλεια": "ασφάλεια — insurance", "τέλη κυκλοφορίας": "τέλη κυκλοφορίας — road tax", "σέρβις": "σέρβις — servicing", "μέσα μεταφοράς": "μέσα μεταφοράς — public transport", "μεταχειρισμένο": "μεταχειρισμένος — second-hand", "βράχηκα": "βρέχομαι — to get wet", "μέχρι το κόκαλο": "μέχρι το κόκαλο — to the bone (soaked through)", "νοικιάζω": "νοικιάζω — to rent", "πατήσω το πόδι μου": "δεν πατάω το πόδι μου — not to set foot", "podcast": "podcast — podcast"}
})
ITEMS.append({
 "id": "l92-mono-stoudio", "title": "Από το μεγάλο σπίτι σε ένα στούντιο", "title_en": "From a big house to a studio flat", "type": "monologue", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, μια συνταξιούχος δασκάλα μιλά για μια μεγάλη αλλαγή στη ζωή της.",
 "script": [
  L("Συνταξιούχος", "f", "Σαράντα χρόνια ζούσαμε σε ένα διώροφο σπίτι με κήπο. Εκεί μεγάλωσαν τα παιδιά μας, εκεί κάναμε όλες τις γιορτές. Όταν έφυγαν τα παιδιά και πέθανε ο άντρας μου, βρέθηκα μόνη σε εκατόν ογδόντα τετραγωνικά. Καθάριζα δωμάτια που δεν έμπαινε κανείς και πλήρωνα θέρμανση για άδειους χώρους.", "For forty years we lived in a two-storey house with a garden. That's where our children grew up, where we held all our celebrations. When the children left and my husband died, I found myself alone in a hundred and eighty square metres. I was cleaning rooms nobody went into and paying heating for empty spaces."),
  L("Συνταξιούχος", "f", "Η απόφαση να το πουλήσω μου πήρε δύο χρόνια. Το πιο δύσκολο δεν ήταν το σπίτι, αλλά τα πράγματα: έπιπλα, βιβλία, πιάτα για σαράντα άτομα, τα σχολικά τετράδια των παιδιών. Έκανα έναν κανόνα: κράτησα μόνο ό,τι χρησιμοποιούσα ή αγαπούσα πραγματικά. Τα υπόλοιπα τα μοίρασα στα παιδιά, σε φίλους και σε μια φιλανθρωπική οργάνωση.", "The decision to sell it took me two years. The hardest thing wasn't the house but the things: furniture, books, plates for forty people, the children's school exercise books. I made a rule: I kept only what I really used or loved. I gave the rest to the children, to friends and to a charity."),
  L("Συνταξιούχος", "f", "Τώρα μένω σε ένα στούντιο σαράντα τετραγωνικών στο κέντρο, με ένα μπαλκόνι γεμάτο γλάστρες. Το καθαρίζω σε μισή ώρα, και με τα χρήματα που περίσσεψαν ταξιδεύω δύο φορές τον χρόνο. Μου λείπει ο κήπος, δεν το κρύβω. Αλλά έχω ανακαλύψει ότι οι αναμνήσεις δεν χρειάζονται τετραγωνικά· τις κουβαλάω μαζί μου όπου κι αν πάω.", "Now I live in a forty-square-metre studio in the centre, with a balcony full of pots. I clean it in half an hour, and with the money left over I travel twice a year. I miss the garden, I won't hide it. But I've discovered that memories don't need square metres; I carry them with me wherever I go."),
 ],
 "questions": [
  Q("Γιατί αποφάσισε να πουλήσει το σπίτι;", ["Γιατί χρειαζόταν χρήματα για τα παιδιά", "Γιατί έμενε μόνη σε ένα πολύ μεγάλο σπίτι", "Γιατί το σπίτι είχε ζημιές", "Γιατί ήθελε να μετακομίσει σε χωριό"], 1, "βρέθηκα μόνη σε εκατόν ογδόντα τετραγωνικά"),
  Q("Ποιο ήταν το πιο δύσκολο κομμάτι;", ["Να βρει αγοραστή", "Να αποφασίσει τι θα κάνει με τα πράγματα", "Να βρει καινούργιο σπίτι", "Να πείσει τα παιδιά της"], 1, "Το πιο δύσκολο δεν ήταν το σπίτι, αλλά τα πράγματα"),
  Q("Τι κάνει με τα χρήματα που περίσσεψαν;", ["Τα έδωσε στα παιδιά της", "Αγόρασε αυτοκίνητο", "Ταξιδεύει δύο φορές τον χρόνο", "Τα έχει στην τράπεζα"], 2, "με τα χρήματα που περίσσεψαν ταξιδεύω δύο φορές τον χρόνο"),
 ],
 "gloss": {"διώροφο": "διώροφος — two-storey", "τετραγωνικά": "τετραγωνικά (μέτρα) — square metres", "θέρμανση": "θέρμανση — heating", "έπιπλα": "έπιπλο — piece of furniture", "τετράδια": "τετράδιο — exercise book", "φιλανθρωπική": "φιλανθρωπικός — charitable", "οργάνωση": "οργάνωση — organisation", "στούντιο": "στούντιο — studio flat", "γλάστρες": "γλάστρα — flowerpot", "περίσσεψαν": "περισσεύω — to be left over", "αναμνήσεις": "ανάμνηση — memory", "κουβαλάω": "κουβαλάω — to carry"}
})
ITEMS.append({
 "id": "l92-c1-paradoxo-epilogis", "title": "Το παράδοξο της επιλογής", "title_en": "The paradox of choice", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την οικονομία και την ψυχολογία, η παρουσιάστρια μιλά με έναν ερευνητή της συμπεριφοράς των καταναλωτών.",
 "script": [
  L("Παρουσιάστρια", "f", "Θεωρούμε αυτονόητο ότι όσο περισσότερες επιλογές έχουμε, τόσο καλύτερα. Εσείς υποστηρίζετε το αντίθετο;", "We take it for granted that the more choices we have, the better. Are you arguing the opposite?"),
  L("Ερευνητής", "m", "Όχι ακριβώς το αντίθετο. Η δυνατότητα επιλογής είναι πολύτιμη. Όμως, πέρα από ένα σημείο, οι πολλές επιλογές δεν μας ελευθερώνουν, αλλά μας παραλύουν. Αυτό ο ψυχολόγος Μπάρι Σβαρτς το ονόμασε «παράδοξο της επιλογής».", "Not exactly the opposite. Having a choice is valuable. But beyond a certain point, many choices don't free us; they paralyse us. The psychologist Barry Schwartz called this the 'paradox of choice'."),
  L("Παρουσιάστρια", "f", "Υπάρχει κάποιο πείραμα που το δείχνει;", "Is there an experiment that shows it?"),
  L("Ερευνητής", "m", "Το πιο γνωστό έγινε σε ένα σούπερ μάρκετ στην Καλιφόρνια. Σε έναν πάγκο γευσιγνωσίας, οι ερευνήτριες έβαζαν άλλοτε είκοσι τέσσερις γεύσεις μαρμελάδας και άλλοτε μόνο έξι. Ο μεγάλος πάγκος τραβούσε περισσότερο κόσμο, αλλά από όσους δοκίμαζαν στον μικρό, περίπου το ένα τρίτο αγόραζε μαρμελάδα, ενώ στον μεγάλο αγόραζαν μόλις τρεις στους εκατό.", "The best known took place in a supermarket in California. At a tasting stand, the researchers set out sometimes twenty-four flavours of jam and sometimes only six. The big stand attracted more people, but of those who tasted at the small one, about a third bought jam, while at the big one only three in a hundred bought."),
  L("Παρουσιάστρια", "f", "Και όταν τελικά διαλέγουμε, είμαστε πιο ικανοποιημένοι;", "And when we finally choose, are we more satisfied?"),
  L("Ερευνητής", "m", "Συχνά όχι. Όσο περισσότερες είναι οι εναλλακτικές, τόσο πιο εύκολα φανταζόμαστε ότι κάποια από αυτές που απορρίψαμε θα ήταν καλύτερη, και η χαρά μας μειώνεται. Ιδιαίτερα δυστυχισμένοι είναι οι λεγόμενοι «μεγιστοποιητές», όσοι θέλουν πάντα το απόλυτα καλύτερο. Αντίθετα, όσοι αρκούνται σε κάτι που είναι «αρκετά καλό» δηλώνουν, κατά κανόνα, πιο ευχαριστημένοι.", "Often not. The more alternatives there are, the more easily we imagine that one of those we rejected would have been better, and our pleasure diminishes. Particularly unhappy are the so-called 'maximisers', those who always want the absolute best. By contrast, those who settle for something 'good enough' say, as a rule, that they are more satisfied."),
 ],
 "questions": [
  Q("Τι υποστηρίζει ο ερευνητής για τις πολλές επιλογές;", ["Ότι είναι πάντα επιζήμιες", "Ότι πέρα από ένα σημείο μας παραλύουν", "Ότι μας κάνουν πάντα πιο ελεύθερους", "Ότι δεν έχουν καμία επίδραση"], 1, "πέρα από ένα σημείο, οι πολλές επιλογές δεν μας ελευθερώνουν, αλλά μας παραλύουν"),
  Q("Τι έδειξε το πείραμα με τις μαρμελάδες;", ["Ότι ο μεγάλος πάγκος πουλούσε περισσότερο", "Ότι στον μικρό πάγκο αγόραζε περίπου το ένα τρίτο, ενώ στον μεγάλο τρεις στους εκατό", "Ότι κανείς δεν αγόραζε μαρμελάδα", "Ότι ο μικρός πάγκος τραβούσε περισσότερο κόσμο"], 1, "περίπου το ένα τρίτο αγόραζε μαρμελάδα, ενώ στον μεγάλο αγόραζαν μόλις τρεις στους εκατό"),
  Q("Γιατί, κατά τον ερευνητή, μειώνεται η ικανοποίηση όταν οι επιλογές είναι πολλές;", ["Γιατί τα προϊόντα είναι χειρότερης ποιότητας", "Γιατί φανταζόμαστε ότι κάποια επιλογή που απορρίψαμε θα ήταν καλύτερη", "Γιατί ξοδεύουμε περισσότερα χρήματα", "Γιατί κουραζόμαστε σωματικά"], 1, "τόσο πιο εύκολα φανταζόμαστε ότι κάποια από αυτές που απορρίψαμε θα ήταν καλύτερη"),
  Q("Ποιοι δηλώνουν, κατά κανόνα, πιο ευχαριστημένοι;", ["Οι μεγιστοποιητές", "Όσοι έχουν τις περισσότερες επιλογές", "Όσοι αρκούνται σε κάτι αρκετά καλό", "Όσοι ψωνίζουν σε μικρά καταστήματα"], 2, "όσοι αρκούνται σε κάτι που είναι «αρκετά καλό» δηλώνουν, κατά κανόνα, πιο ευχαριστημένοι"),
 ],
 "gloss": {"καταναλωτών": "καταναλωτής — consumer", "αυτονόητο": "αυτονόητος — self-evident", "παραλύουν": "παραλύω — to paralyse", "παράδοξο": "παράδοξο — paradox", "πάγκο": "πάγκος — stand, counter", "γευσιγνωσίας": "γευσιγνωσία — tasting", "μαρμελάδας": "μαρμελάδα — jam", "εναλλακτικές": "εναλλακτική — alternative", "απορρίψαμε": "απορρίπτω — to reject", "μεγιστοποιητές": "μεγιστοποιητής — maximiser", "αρκούνται": "αρκούμαι σε — to settle for", "κατά κανόνα": "κατά κανόνα — as a rule"}
})
ITEMS.append({
 "id": "l92-c1-pseudeis-anamniseis", "title": "Όταν η μνήμη μάς ξεγελά", "title_en": "When memory deceives us", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας διάλεξης για τη γνωστική ψυχολογία σε ένα πανεπιστήμιο.",
 "script": [
  L("Καθηγήτρια", "f", "Οι περισσότεροι φανταζόμαστε τη μνήμη σαν μια βιντεοκάμερα: καταγράφει ό,τι ζούμε, και όταν θυμόμαστε, απλώς ξαναπαίζουμε την ταινία. Δεκαετίες έρευνας δείχνουν ότι η εικόνα αυτή είναι λανθασμένη. Κάθε φορά που ανακαλούμε μια ανάμνηση, στην ουσία την ξαναχτίζουμε, και στη διαδικασία αυτή μπορούν να παρεισφρήσουν λάθη.", "Most of us imagine memory as a video camera: it records what we live through, and when we remember, we simply replay the film. Decades of research show that this picture is wrong. Every time we recall a memory, we are in essence rebuilding it, and errors can creep in during this process."),
  L("Καθηγήτρια", "f", "Η Αμερικανίδα ψυχολόγος Ελίζαμπεθ Λόφτους έδειξε στη δεκαετία του 1970 πόσο εύκολα επηρεάζεται η μνήμη από τη διατύπωση μιας ερώτησης. Έδειχνε σε ανθρώπους ένα βίντεο με τη σύγκρουση δύο αυτοκινήτων και ύστερα ρωτούσε με τι ταχύτητα κινούνταν όταν «χτύπησαν» ή όταν «συνετρίβησαν» το ένα πάνω στο άλλο. Όσοι άκουγαν το δεύτερο ρήμα υπολόγιζαν μεγαλύτερη ταχύτητα και, μια εβδομάδα αργότερα, πολλοί «θυμούνταν» σπασμένα τζάμια που δεν υπήρχαν στο βίντεο.", "In the 1970s the American psychologist Elizabeth Loftus showed how easily memory is influenced by the wording of a question. She showed people a video of two cars colliding and then asked how fast they were going when they 'hit' or 'smashed into' each other. Those who heard the second verb estimated a higher speed and, a week later, many 'remembered' broken glass that wasn't in the video."),
  L("Καθηγήτρια", "f", "Σε μεταγενέστερες μελέτες, η Λόφτους και οι συνεργάτες της κατάφεραν να εμφυτεύσουν σε ορισμένους συμμετέχοντες ολόκληρες ψευδείς αναμνήσεις, όπως ότι είχαν χαθεί σε ένα εμπορικό κέντρο ως παιδιά. Τα ευρήματα αυτά έχουν σοβαρές συνέπειες, ιδίως για τις μαρτυρίες στα δικαστήρια. Μια ανάμνηση μπορεί να είναι ζωντανή, λεπτομερής και απολύτως ειλικρινής, και παρ’ όλα αυτά να είναι λανθασμένη.", "In later studies, Loftus and her colleagues managed to implant whole false memories in some participants, such as that they had been lost in a shopping centre as children. These findings have serious consequences, especially for witness testimony in the courts. A memory can be vivid, detailed and entirely sincere, and nevertheless be wrong."),
 ],
 "questions": [
  Q("Ποια εικόνα της μνήμης χαρακτηρίζει η καθηγήτρια λανθασμένη;", ["Ότι η μνήμη ξεχνά με τον χρόνο", "Ότι η μνήμη λειτουργεί σαν βιντεοκάμερα", "Ότι η μνήμη επηρεάζεται από τα συναισθήματα", "Ότι η μνήμη βελτιώνεται με την εξάσκηση"], 1, "φανταζόμαστε τη μνήμη σαν μια βιντεοκάμερα"),
  Q("Τι συμβαίνει, κατά την καθηγήτρια, όταν ανακαλούμε μια ανάμνηση;", ["Την ξαναχτίζουμε", "Τη σβήνουμε", "Την αντιγράφουμε ακριβώς", "Την ξεχνάμε πιο γρήγορα"], 0, "στην ουσία την ξαναχτίζουμε"),
  Q("Τι έδειξε το πείραμα με τη σύγκρουση των αυτοκινήτων;", ["Ότι οι άνθρωποι θυμούνται τα πάντα σωστά", "Ότι η διατύπωση της ερώτησης επηρεάζει τη μνήμη", "Ότι κανείς δεν πρόσεξε τη σύγκρουση", "Ότι οι άνθρωποι υποτιμούν την ταχύτητα"], 1, "πόσο εύκολα επηρεάζεται η μνήμη από τη διατύπωση μιας ερώτησης"),
  Q("Γιατί τα ευρήματα έχουν σοβαρές συνέπειες για τα δικαστήρια;", ["Γιατί οι μάρτυρες λένε συχνά ψέματα", "Γιατί μια ειλικρινής και λεπτομερής ανάμνηση μπορεί να είναι λανθασμένη", "Γιατί τα βίντεο δεν γίνονται δεκτά", "Γιατί οι δικαστές δεν εμπιστεύονται τους ψυχολόγους"], 1, "Μια ανάμνηση μπορεί να είναι ζωντανή, λεπτομερής και απολύτως ειλικρινής, και παρ’ όλα αυτά να είναι λανθασμένη"),
 ],
 "gloss": {"γνωστική": "γνωστικός — cognitive", "βιντεοκάμερα": "βιντεοκάμερα — video camera", "λανθασμένη": "λανθασμένος — mistaken", "ανακαλούμε": "ανακαλώ — to recall", "παρεισφρήσουν": "παρεισφρέω — to creep in", "διατύπωση": "διατύπωση — wording", "συνετρίβησαν": "συντρίβομαι — to smash, crash", "μεταγενέστερες": "μεταγενέστερος — later, subsequent", "εμφυτεύσουν": "εμφυτεύω — to implant", "ψευδείς": "ψευδής — false", "μαρτυρίες": "μαρτυρία — testimony", "ειλικρινής": "ειλικρινής — sincere"}
})

rnd = random.Random(92)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-92.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
