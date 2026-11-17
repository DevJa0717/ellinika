# Source for library/listening/listening-161.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l161.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l161-ann-agonas", "title": "Ανακοίνωση πριν από τον αγώνα δρόμου", "title_en": "An announcement before the road race", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα στην αφετηρία ενός αγώνα δρόμου στην πόλη.",
 "script": [
  L("Εκφωνήτρια", "f", "Καλημέρα σε όλους τους δρομείς! Η εκκίνηση του αγώνα των δέκα χιλιομέτρων θα δοθεί στις εννιά ακριβώς. Ο αγώνας των πέντε χιλιομέτρων και ο περίπατος για τις οικογένειες θα ξεκινήσουν μισή ώρα αργότερα.", "Good morning to all runners! The start of the ten-kilometre race will be given at nine o'clock sharp. The five-kilometre race and the family walk will start half an hour later."),
  L("Εκφωνήτρια", "f", "Λόγω της ζέστης, έχουμε προσθέσει έναν ακόμη σταθμό με νερό, στο έβδομο χιλιόμετρο, δίπλα στο λιμάνι. Αν νιώσετε ζάλη ή αδιαθεσία, σταματήστε αμέσως και ζητήστε βοήθεια από τους εθελοντές με τα κίτρινα γιλέκα.", "Because of the heat, we have added one more water station, at the seventh kilometre, next to the harbour. If you feel dizzy or unwell, stop immediately and ask for help from the volunteers in yellow vests."),
  L("Εκφωνήτρια", "f", "Θυμίζουμε ότι ο αριθμός σας πρέπει να είναι καρφιτσωμένος μπροστά, ώστε να φαίνεται στις κάμερες του τερματισμού. Τα μετάλλια και τα φρούτα θα μοιράζονται μετά τη γραμμή τερματισμού, και τα αποτελέσματα θα αναρτηθούν στην ιστοσελίδα μας μέχρι το μεσημέρι.", "We remind you that your number must be pinned on the front, so that it is visible to the finish-line cameras. Medals and fruit will be handed out after the finish line, and the results will be posted on our website by midday."),
 ],
 "questions": [
  Q("Πότε θα ξεκινήσει ο αγώνας των πέντε χιλιομέτρων;", ["Στις εννιά ακριβώς", "Μισή ώρα μετά τον αγώνα των δέκα χιλιομέτρων", "Το μεσημέρι", "Μία ώρα νωρίτερα"], 1, "θα ξεκινήσουν μισή ώρα αργότερα"),
  Q("Γιατί προστέθηκε ένας ακόμη σταθμός με νερό;", ["Λόγω της ζέστης", "Γιατί η διαδρομή άλλαξε", "Γιατί ήρθαν περισσότεροι δρομείς", "Για τα παιδιά"], 0, "Λόγω της ζέστης"),
  Q("Γιατί πρέπει ο αριθμός να είναι καρφιτσωμένος μπροστά;", ["Για να τον βλέπουν οι θεατές", "Για να μη χαθεί", "Για να φαίνεται στις κάμερες του τερματισμού", "Για να πάρουν μετάλλιο"], 2, "ώστε να φαίνεται στις κάμερες του τερματισμού"),
 ],
 "gloss": {"αφετηρία": "αφετηρία — starting line", "δρομείς": "δρομέας — runner", "εκκίνηση": "εκκίνηση — start", "περίπατος": "περίπατος — walk, stroll", "ζάλη": "ζάλη — dizziness", "αδιαθεσία": "αδιαθεσία — feeling unwell", "γιλέκα": "γιλέκο — vest, waistcoat", "καρφιτσωμένος": "καρφιτσωμένος — pinned", "τερματισμού": "τερματισμός — finish (of a race)", "αναρτηθούν": "αναρτώ — to post, to put up"},
})

ITEMS.append({
 "id": "l161-int-skyloi", "title": "Σκύλοι που βλέπουν για άλλους", "title_en": "Dogs that see for others", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που εκπαιδεύει σκύλους-οδηγούς για τυφλούς.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσος χρόνος χρειάζεται για να γίνει ένα κουτάβι σκύλος-οδηγός;", "How much time does it take for a puppy to become a guide dog?"),
  L("Εκπαιδεύτρια", "f", "Περίπου δύο χρόνια. Τον πρώτο χρόνο το κουτάβι ζει με μια εθελοντική οικογένεια, για να συνηθίσει τους θορύβους της πόλης, τα λεωφορεία, τα καταστήματα. Μετά έρχεται σε εμάς για την κυρίως εκπαίδευση.", "About two years. In the first year the puppy lives with a volunteer family, to get used to the noises of the city, the buses, the shops. Then it comes to us for the main training."),
  L("Δημοσιογράφος", "m", "Τι είναι το πιο δύσκολο να μάθει;", "What is the hardest thing for it to learn?"),
  L("Εκπαιδεύτρια", "f", "Η λεγόμενη «έξυπνη ανυπακοή». Ο σκύλος πρέπει να υπακούει, αλλά να αρνείται μια εντολή όταν είναι επικίνδυνη. Αν ο άνθρωπος του πει «εμπρός» και έρχεται αυτοκίνητο, ο σκύλος δεν προχωράει. Αυτό δεν το μαθαίνουν όλα τα σκυλιά· περίπου τα μισά δεν περνούν τις τελικές εξετάσεις.", "So-called 'intelligent disobedience'. The dog has to obey, but refuse a command when it is dangerous. If its person says 'forward' and a car is coming, the dog doesn't move. Not all dogs learn this; about half don't pass the final tests."),
  L("Δημοσιογράφος", "m", "Τι γίνεται με αυτά;", "What happens to them?"),
  L("Εκπαιδεύτρια", "f", "Υιοθετούνται, συνήθως από τις οικογένειες που τα μεγάλωσαν. Και κάτι που θέλω να πω στους ακροατές: όταν βλέπετε έναν σκύλο-οδηγό με το λουρί του, μην τον χαϊδεύετε και μην του δίνετε φαγητό. Δουλεύει, και κάθε διάσπαση της προσοχής του μπορεί να είναι επικίνδυνη.", "They are adopted, usually by the families that raised them. And something I want to tell the listeners: when you see a guide dog in its harness, don't stroke it and don't give it food. It is working, and every distraction can be dangerous."),
 ],
 "questions": [
  Q("Γιατί το κουτάβι ζει τον πρώτο χρόνο με μια εθελοντική οικογένεια;", ["Για να μάθει να κολυμπάει", "Για να συνηθίσει τους θορύβους της πόλης", "Για να μεγαλώσει με άλλα σκυλιά", "Γιατί η σχολή δεν έχει χώρο"], 1, "για να συνηθίσει τους θορύβους της πόλης"),
  Q("Τι είναι η «έξυπνη ανυπακοή»;", ["Να μην υπακούει ποτέ ο σκύλος", "Να αρνείται ο σκύλος μια εντολή όταν είναι επικίνδυνη", "Να βρίσκει μόνος του τον δρόμο για το σπίτι", "Να γαβγίζει όταν πλησιάζει ξένος"], 1, "να αρνείται μια εντολή όταν είναι επικίνδυνη"),
  Q("Τι ζητά η εκπαιδεύτρια από τους ακροατές;", ["Να γίνουν εθελοντές", "Να υιοθετήσουν σκυλιά", "Να μη χαϊδεύουν και να μην ταΐζουν έναν σκύλο-οδηγό που δουλεύει", "Να κάνουν δωρεές"], 2, "μην τον χαϊδεύετε και μην του δίνετε φαγητό"),
 ],
 "gloss": {"εκπαιδεύει": "εκπαιδεύω — to train", "σκύλους-οδηγούς": "σκύλος-οδηγός — guide dog", "τυφλούς": "τυφλός — blind", "κουτάβι": "κουτάβι — puppy", "εθελοντική": "εθελοντικός — volunteer (adj.)", "ανυπακοή": "ανυπακοή — disobedience", "υπακούει": "υπακούω — to obey", "εντολή": "εντολή — command", "Υιοθετούνται": "υιοθετούμαι — to be adopted", "λουρί": "λουρί — harness, lead", "χαϊδεύετε": "χαϊδεύω — to stroke, to pet", "διάσπαση": "διάσπαση (της προσοχής) — distraction"},
})

ITEMS.append({
 "id": "l161-int-fylakas", "title": "Ο φύλακας του αρχαίου θεάτρου", "title_en": "The guard of the ancient theatre", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν αρχαιοφύλακα που δουλεύει σε ένα αρχαίο θέατρο.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι ακριβώς κάνει ένας αρχαιοφύλακας;", "What exactly does a guard of antiquities do?"),
  L("Αρχαιοφύλακας", "m", "Ο κόσμος νομίζει ότι απλώς κόβουμε εισιτήρια. Στην πραγματικότητα, προστατεύουμε τον χώρο: προσέχουμε να μην ανεβαίνουν οι επισκέπτες σε σημεία που κινδυνεύουν, να μην παίρνουν πέτρες για ενθύμιο, να μη χαράζουν τα ονόματά τους στα μάρμαρα.", "People think we just sell tickets. In reality, we protect the site: we make sure visitors don't climb on parts that are at risk, don't take stones as souvenirs, don't carve their names into the marble."),
  L("Δημοσιογράφος", "f", "Συμβαίνουν τέτοια πράγματα;", "Do such things happen?"),
  L("Αρχαιοφύλακας", "m", "Δυστυχώς ναι. Πέρσι πιάσαμε έναν τουρίστα με ένα κομμάτι από αρχαίο κεραμίδι στην τσέπη. Δεν ήξερε ότι είναι αδίκημα. Τις περισσότερες φορές, όμως, οι άνθρωποι σέβονται τον χώρο, αρκεί να τους εξηγήσεις γιατί.", "Unfortunately, yes. Last year we caught a tourist with a piece of ancient roof tile in his pocket. He didn't know it was an offence. Most of the time, though, people respect the site, as long as you explain why."),
  L("Δημοσιογράφος", "f", "Ποια είναι η αγαπημένη σας ώρα;", "What is your favourite time?"),
  L("Αρχαιοφύλακας", "m", "Το πρωί, πριν ανοίξουμε. Κάθομαι στην τελευταία σειρά και ακούω τα πουλιά. Η ακουστική είναι τόσο καλή που, αν ένας συνάδελφος ρίξει ένα νόμισμα στη σκηνή, το ακούω μέχρι επάνω.", "In the morning, before we open. I sit in the top row and listen to the birds. The acoustics are so good that if a colleague drops a coin on the stage, I hear it all the way up."),
 ],
 "questions": [
  Q("Τι νομίζει ο κόσμος ότι κάνουν οι αρχαιοφύλακες;", ["Ότι κάνουν ανασκαφές", "Ότι απλώς κόβουν εισιτήρια", "Ότι ξεναγούν τους επισκέπτες", "Ότι καθαρίζουν τα μάρμαρα"], 1, "απλώς κόβουμε εισιτήρια"),
  Q("Τι βρήκαν πέρσι στην τσέπη ενός τουρίστα;", ["Ένα νόμισμα", "Ένα κομμάτι από αρχαίο κεραμίδι", "Ένα μαχαίρι", "Ένα κομμάτι μάρμαρο"], 1, "ένα κομμάτι από αρχαίο κεραμίδι"),
  Q("Γιατί του αρέσει το πρωί πριν ανοίξουν;", ["Γιατί κάνει δροσιά", "Γιατί δεν έχει δουλειά", "Γιατί κάθεται στην τελευταία σειρά και ακούει τα πουλιά", "Γιατί βλέπει την ανατολή"], 2, "Κάθομαι στην τελευταία σειρά και ακούω τα πουλιά"),
 ],
 "gloss": {"αρχαιοφύλακα": "αρχαιοφύλακας — guard of antiquities", "ενθύμιο": "ενθύμιο — souvenir, keepsake", "χαράζουν": "χαράζω — to carve, to engrave", "μάρμαρα": "μάρμαρο — marble", "κεραμίδι": "κεραμίδι — roof tile", "αδίκημα": "αδίκημα — offence", "σέβονται": "σέβομαι — to respect", "ακουστική": "ακουστική — acoustics", "νόμισμα": "νόμισμα — coin", "σκηνή": "σκηνή — stage"},
})

ITEMS.append({
 "id": "l161-dia-amaxi", "title": "Ένα αυτοκίνητο για δύο οικογένειες", "title_en": "One car for two families", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο γείτονες να συζητούν αν θα μοιράζονται ένα αυτοκίνητο.",
 "script": [
  L("Θοδωρής", "m", "Λοιπόν, το σκέφτηκες; Το δικό μας αυτοκίνητο μένει παρκαρισμένο έξι μέρες την εβδομάδα. Το δικό σας, απ' ό,τι βλέπω, το ίδιο.", "So, have you thought about it? Our car stays parked six days a week. Yours, from what I can see, the same."),
  L("Νεφέλη", "f", "Η ιδέα μού αρέσει. Θα πουλήσουμε το δικό μας, που είναι παλιό, και θα μοιράζουμε στη μέση την ασφάλεια και το σέρβις του δικού σας. Με ανησυχεί μόνο τι θα γίνει τα Σαββατοκύριακα, που το χρειαζόμαστε όλοι.", "I like the idea. We'll sell ours, which is old, and we'll split the insurance and servicing of yours half and half. The only thing that worries me is what happens at weekends, when we all need it."),
  L("Θοδωρής", "m", "Γι' αυτό λέω να φτιάξουμε ένα κοινό ημερολόγιο στο κινητό. Όποιος το κλείσει πρώτος, το παίρνει. Και κάθε δεύτερο Σάββατο προτεραιότητα έχει η άλλη οικογένεια.", "That's why I suggest we set up a shared calendar on our phones. Whoever books it first gets it. And every other Saturday the other family has priority."),
  L("Νεφέλη", "f", "Και η βενζίνη;", "And the petrol?"),
  L("Θοδωρής", "m", "Ο καθένας γεμίζει το ρεζερβουάρ όσο το βρήκε. Απλός κανόνας, για να μη μετράμε χιλιόμετρα και να μη μαλώνουμε.", "Everyone fills the tank back to the level they found it. A simple rule, so we don't count kilometres and don't argue."),
  L("Νεφέλη", "f", "Εντάξει. Ας το δοκιμάσουμε τρεις μήνες, και αν δεν πάει καλά, τουλάχιστον θα έχουμε μείνει φίλοι.", "OK. Let's try it for three months, and if it doesn't work, at least we'll still be friends."),
 ],
 "questions": [
  Q("Τι θα κάνει η Νεφέλη με το δικό της αυτοκίνητο;", ["Θα το χαρίσει", "Θα το πουλήσει", "Θα το κρατήσει για τα Σαββατοκύριακα", "Θα το νοικιάσει"], 1, "Θα πουλήσουμε το δικό μας"),
  Q("Πώς προτείνει ο Θοδωρής να οργανώνουν ποιος θα παίρνει το αυτοκίνητο;", ["Με κλήρωση", "Με ένα κοινό ημερολόγιο στο κινητό", "Θα το έχει ο καθένας μία εβδομάδα", "Θα αποφασίζουν κάθε βράδυ"], 1, "να φτιάξουμε ένα κοινό ημερολόγιο στο κινητό"),
  Q("Ποιος είναι ο κανόνας για τη βενζίνη;", ["Θα μοιράζονται το κόστος στη μέση", "Θα μετρούν τα χιλιόμετρα", "Ο καθένας γεμίζει το ρεζερβουάρ όσο το βρήκε", "Θα πληρώνει ο ιδιοκτήτης"], 2, "Ο καθένας γεμίζει το ρεζερβουάρ όσο το βρήκε"),
 ],
 "gloss": {"μοιράζονται": "μοιράζομαι — to share", "παρκαρισμένο": "παρκαρισμένος — parked", "ασφάλεια": "ασφάλεια — insurance; safety", "σέρβις": "σέρβις — (car) service", "ημερολόγιο": "ημερολόγιο — calendar", "κλείσει": "κλείνω — to book; to close", "προτεραιότητα": "προτεραιότητα — priority", "ρεζερβουάρ": "ρεζερβουάρ — (fuel) tank", "μαλώνουμε": "μαλώνω — to argue, to quarrel"},
})

ITEMS.append({
 "id": "l161-dia-xoros", "title": "Μαθήματα χορού πριν από τον γάμο", "title_en": "Dance lessons before the wedding", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι που παντρεύεται σε δύο μήνες να συζητάει για τον πρώτο χορό στο γλέντι.",
 "script": [
  L("Δανάη", "f", "Η μητέρα μου ρωτάει τι θα χορέψουμε στην αρχή του γλεντιού. Λέει ότι όλοι θα μας κοιτάζουν.", "My mother is asking what we'll dance at the start of the reception. She says everyone will be watching us."),
  L("Κυριάκος", "m", "Αυτό ακριβώς με τρομάζει. Εγώ χορεύω μόνο συρτό, και αυτό με το μαντήλι, πίσω από κάποιον που ξέρει.", "That's exactly what scares me. I only dance the syrtos, and even that holding a handkerchief, behind someone who knows how."),
  L("Δανάη", "f", "Γι' αυτό βρήκα μια σχολή που κάνει μαθήματα για ζευγάρια πριν από τον γάμο. Οκτώ μαθήματα, μία φορά την εβδομάδα. Ο δάσκαλος φτιάχνει μια απλή χορογραφία πάνω στο τραγούδι που διαλέγεις.", "That's why I found a school that does lessons for couples before the wedding. Eight lessons, once a week. The teacher makes a simple choreography to the song you choose."),
  L("Κυριάκος", "m", "Και ποιο τραγούδι θα διαλέξουμε; Εσύ θέλεις βαλς, εγώ θέλω ένα ζεϊμπέκικο.", "And which song will we choose? You want a waltz, I want a zeibekiko."),
  L("Δανάη", "f", "Το ζεϊμπέκικο το χορεύει ένας, Κυριάκο, όχι ζευγάρι! Ας κάνουμε ένα αργό λαϊκό στην αρχή, και μετά, όταν ανοίξει η πίστα, χορεύεις όσα ζεϊμπέκικα θέλεις.", "The zeibekiko is danced by one person, Kyriakos, not a couple! Let's do a slow laiko song at the start, and then, when the dance floor opens, you can dance as many zeibekikos as you like."),
  L("Κυριάκος", "m", "Συμφωνώ, αρκεί να μη μας τραβάει βίντεο ο θείος σου από την πρώτη πρόβα.", "Agreed, as long as your uncle doesn't film us from the first rehearsal."),
 ],
 "questions": [
  Q("Γιατί ανησυχεί ο Κυριάκος;", ["Γιατί δεν του αρέσει η μουσική", "Γιατί χορεύει μόνο συρτό και φοβάται ότι όλοι θα τους κοιτάζουν", "Γιατί δεν έχει χρόνο για μαθήματα", "Γιατί τα μαθήματα είναι ακριβά"], 1, "Αυτό ακριβώς με τρομάζει"),
  Q("Τι κάνει ο δάσκαλος στη σχολή που βρήκε η Δανάη;", ["Τους μαθαίνει όλους τους παραδοσιακούς χορούς", "Φτιάχνει μια απλή χορογραφία πάνω στο τραγούδι που διαλέγει το ζευγάρι", "Χορεύει μαζί τους στον γάμο", "Τους δίνει βίντεο για να μάθουν στο σπίτι"], 1, "Ο δάσκαλος φτιάχνει μια απλή χορογραφία πάνω στο τραγούδι που διαλέγεις"),
  Q("Γιατί η Δανάη δεν θέλει ζεϊμπέκικο για τον πρώτο χορό;", ["Γιατί είναι πολύ γρήγορο", "Γιατί δεν το ξέρει", "Γιατί το χορεύει ένας και όχι ζευγάρι", "Γιατί δεν αρέσει στη μητέρα της"], 2, "Το ζεϊμπέκικο το χορεύει ένας, Κυριάκο, όχι ζευγάρι"),
 ],
 "gloss": {"γλέντι": "γλέντι — party, (wedding) reception", "γλεντιού": "γλέντι — party, (wedding) reception", "τρομάζει": "τρομάζω — to frighten; to be frightened", "συρτό": "συρτός — syrtos (a circle dance)", "μαντήλι": "μαντήλι — handkerchief", "χορογραφία": "χορογραφία — choreography", "βαλς": "βαλς — waltz", "ζεϊμπέκικο": "ζεϊμπέκικο — zeibekiko (solo dance)", "πίστα": "πίστα — dance floor", "πρόβα": "πρόβα — rehearsal"},
})

ITEMS.append({
 "id": "l161-mon-sxoliko", "title": "Η οδηγός του σχολικού λεωφορείου", "title_en": "The school bus driver", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα που οδηγεί σχολικό λεωφορείο σε ορεινή περιοχή να μιλάει για τη δουλειά της.",
 "script": [
  L("Οδηγός", "f", "Ξεκινάω στις έξι και μισή, όταν έξω είναι ακόμη σκοτάδι. Μαζεύω είκοσι τρία παιδιά από εννιά χωριά, και η διαδρομή ως το σχολείο κρατάει σχεδόν μία ώρα, με στροφές και ανηφόρες.", "I start at half past six, when it's still dark outside. I pick up twenty-three children from nine villages, and the route to the school takes almost an hour, with bends and uphill stretches."),
  L("Οδηγός", "f", "Τον χειμώνα το πιο δύσκολο είναι ο πάγος. Αν ο δρόμος δεν έχει καθαριστεί, ειδοποιώ τον διευθυντή και τους γονείς πριν από τις έξι, και το λεωφορείο δεν ξεκινά. Καλύτερα να χάσουν τα παιδιά μια μέρα μάθημα παρά να πάρουμε το παραμικρό ρίσκο.", "In winter the hardest thing is the ice. If the road hasn't been cleared, I notify the head teacher and the parents before six, and the bus doesn't leave. Better for the children to miss a day of lessons than for us to take the slightest risk."),
  L("Οδηγός", "f", "Τα παιδιά τα ξέρω ένα ένα. Ξέρω ποιο ζαλίζεται και πρέπει να κάθεται μπροστά, ποιο ξεχνάει πάντα την τσάντα του. Οι μεγάλοι μού λένε τα μυστικά τους, γιατί δεν είμαι ούτε δασκάλα ούτε μάνα τους. Όταν τελειώνουν το δημοτικό, κλαίω πιο πολύ από τους γονείς.", "I know the children one by one. I know which one gets carsick and has to sit at the front, which one always forgets their bag. The older ones tell me their secrets, because I'm neither their teacher nor their mother. When they finish primary school, I cry more than their parents."),
 ],
 "questions": [
  Q("Πόσο κρατάει η διαδρομή ως το σχολείο;", ["Δέκα λεπτά", "Σχεδόν μία ώρα", "Δύο ώρες", "Μισή ώρα"], 1, "η διαδρομή ως το σχολείο κρατάει σχεδόν μία ώρα"),
  Q("Τι κάνει όταν ο δρόμος έχει πάγο και δεν έχει καθαριστεί;", ["Οδηγεί πολύ αργά", "Ειδοποιεί τον διευθυντή και τους γονείς και το λεωφορείο δεν ξεκινά", "Ζητά από τους γονείς να φέρουν τα παιδιά", "Περιμένει μέχρι το μεσημέρι"], 1, "ειδοποιώ τον διευθυντή και τους γονείς πριν από τις έξι, και το λεωφορείο δεν ξεκινά"),
  Q("Γιατί οι μεγάλοι μαθητές τής λένε τα μυστικά τους;", ["Γιατί είναι συγγενής τους", "Γιατί τους δίνει γλυκά", "Γιατί δεν είναι ούτε δασκάλα ούτε μάνα τους", "Γιατί τους φοβάται"], 2, "γιατί δεν είμαι ούτε δασκάλα ούτε μάνα τους"),
 ],
 "gloss": {"σχολικό λεωφορείο": "σχολικό λεωφορείο — school bus", "ορεινή": "ορεινός — mountainous", "στροφές": "στροφή — bend, turn", "ανηφόρες": "ανηφόρα — uphill slope", "πάγος": "πάγος — ice", "καθαριστεί": "καθαρίζομαι — to be cleared, to be cleaned", "παραμικρό": "παραμικρός — slightest", "ρίσκο": "ρίσκο — risk", "ζαλίζεται": "ζαλίζομαι — to get dizzy, to get carsick", "δημοτικό": "δημοτικό — primary school"},
})

ITEMS.append({
 "id": "l161-vm-optikes", "title": "Μήνυμα για τη σύνδεση οπτικών ινών", "title_en": "A message about the fibre-optic connection", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από έναν τεχνικό της εταιρείας τηλεπικοινωνιών.",
 "script": [
  L("Τεχνικός", "m", "Καλημέρα σας, κύριε Αντωνίου, σας καλώ από την εταιρεία για την εγκατάσταση των οπτικών ινών στο διαμέρισμά σας. Το ραντεβού μας είναι αύριο, Πέμπτη, μεταξύ δέκα και δώδεκα.", "Good morning, Mr Antoniou, I'm calling from the company about installing the fibre optics in your flat. Our appointment is tomorrow, Thursday, between ten and twelve."),
  L("Τεχνικός", "m", "Για να γίνει η σύνδεση, θα χρειαστεί να περάσω το καλώδιο από το υπόγειο της πολυκατοικίας. Παρακαλώ ενημερώστε τον διαχειριστή να μου ανοίξει, γιατί την προηγούμενη φορά βρήκαμε κλειστά και χάσαμε το ραντεβού.", "For the connection to be made, I'll need to run the cable through the building's basement. Please let the building manager know to open it for me, because last time we found it locked and missed the appointment."),
  L("Τεχνικός", "m", "Η εγκατάσταση θα κρατήσει περίπου δύο ώρες και θα χρειαστεί να ανοίξω μια μικρή τρύπα στον τοίχο δίπλα στο παράθυρο. Αν προτιμάτε άλλο σημείο, σκεφτείτε το από πριν. Αν δεν σας βολεύει η ώρα, πάρτε στο κέντρο εξυπηρέτησης, όχι σε μένα, γιατί αυτοί κανονίζουν το πρόγραμμα.", "The installation will take about two hours, and I'll need to make a small hole in the wall next to the window. If you prefer another spot, think about it beforehand. If the time doesn't suit you, call the customer service centre, not me, because they arrange the schedule."),
 ],
 "questions": [
  Q("Πότε είναι το ραντεβού;", ["Σήμερα το απόγευμα", "Αύριο, Πέμπτη, μεταξύ δέκα και δώδεκα", "Τη Δευτέρα το πρωί", "Την Πέμπτη το βράδυ"], 1, "αύριο, Πέμπτη, μεταξύ δέκα και δώδεκα"),
  Q("Γιατί χάθηκε το προηγούμενο ραντεβού;", ["Γιατί ο τεχνικός αρρώστησε", "Γιατί βρήκαν κλειστό το υπόγειο", "Γιατί ο κύριος Αντωνίου έλειπε", "Γιατί δεν υπήρχε καλώδιο"], 1, "βρήκαμε κλειστά και χάσαμε το ραντεβού"),
  Q("Ποιον πρέπει να πάρει ο κύριος Αντωνίου αν δεν τον βολεύει η ώρα;", ["Τον τεχνικό", "Τον διαχειριστή", "Το κέντρο εξυπηρέτησης", "Τον ιδιοκτήτη"], 2, "πάρτε στο κέντρο εξυπηρέτησης, όχι σε μένα"),
 ],
 "gloss": {"οπτικών ινών": "οπτική ίνα — optical fibre", "τηλεπικοινωνιών": "τηλεπικοινωνίες — telecommunications", "εγκατάσταση": "εγκατάσταση — installation", "καλώδιο": "καλώδιο — cable", "υπόγειο": "υπόγειο — basement", "διαχειριστή": "διαχειριστής — building manager", "τρύπα": "τρύπα — hole", "βολεύει": "βολεύει — it suits, it is convenient", "εξυπηρέτησης": "εξυπηρέτηση (πελατών) — customer service"},
})

ITEMS.append({
 "id": "l161-vm-symmathitria", "title": "Μήνυμα από μια παλιά συμμαθήτρια", "title_en": "A message from an old classmate", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από μια συμμαθήτρια του λυκείου που είχατε χρόνια να δείτε.",
 "script": [
  L("Συμμαθήτρια", "f", "Γεια σου, Λευτέρη! Είμαι η Χαρά, η Χαρά Ζαφειρίου, καθόμουν πίσω σου στη δευτέρα λυκείου, θυμάσαι; Βρήκα το τηλέφωνό σου από την αδερφή σου.", "Hi, Lefteris! It's Chara, Chara Zafeiriou, I sat behind you in the second year of lyceum, remember? I got your number from your sister."),
  L("Συμμαθήτρια", "f", "Φέτος κλείνουμε είκοσι πέντε χρόνια από την αποφοίτηση, και κάποιοι από την τάξη οργανώνουμε μια συνάντηση. Θα είναι το Σάββατο δεκαπέντε Ιουνίου, στην αυλή του παλιού μας σχολείου· ο διευθυντής μάς έδωσε άδεια. Μετά θα πάμε για φαγητό στην ταβέρνα δίπλα στο γήπεδο.", "This year it's twenty-five years since we graduated, and some of us from the class are organising a get-together. It'll be on Saturday the fifteenth of June, in the yard of our old school; the head teacher gave us permission. Afterwards we'll go for a meal at the taverna next to the sports ground."),
  L("Συμμαθήτρια", "f", "Θέλουμε να φέρει ο καθένας μια φωτογραφία από εκείνα τα χρόνια, για να φτιάξουμε έναν πίνακα. Αν έχεις ακόμη την κιθάρα σου, φέρ' την· όλοι θυμούνται τις εκδρομές με τα τραγούδια σου. Πάρε με να μου πεις αν έρχεσαι, για να κλείσουμε τραπέζι.", "We'd like everyone to bring a photo from those years, so we can make a board. If you still have your guitar, bring it; everyone remembers the school trips with your songs. Call me to tell me if you're coming, so we can book a table."),
 ],
 "questions": [
  Q("Από πού βρήκε η Χαρά το τηλέφωνο του Λευτέρη;", ["Από το σχολείο", "Από την αδερφή του", "Από το διαδίκτυο", "Από έναν συμμαθητή"], 1, "Βρήκα το τηλέφωνό σου από την αδερφή σου"),
  Q("Πού θα γίνει η συνάντηση;", ["Σε ένα ξενοδοχείο", "Στην αυλή του παλιού σχολείου", "Στο γήπεδο", "Στο σπίτι της Χαράς"], 1, "στην αυλή του παλιού μας σχολείου"),
  Q("Γιατί ζητά από τον Λευτέρη να φέρει την κιθάρα του;", ["Γιατί θα υπάρχει διαγωνισμός", "Γιατί η ταβέρνα δεν έχει μουσική", "Γιατί όλοι θυμούνται τις εκδρομές με τα τραγούδια του", "Γιατί θέλει να την αγοράσει"], 2, "όλοι θυμούνται τις εκδρομές με τα τραγούδια σου"),
 ],
 "gloss": {"συμμαθήτρια": "συμμαθήτρια — (female) classmate", "λυκείου": "λύκειο — upper secondary school", "αποφοίτηση": "αποφοίτηση — graduation", "οργανώνουμε": "οργανώνω — to organise", "αυλή": "αυλή — yard, courtyard", "άδεια": "άδεια — permission", "γήπεδο": "γήπεδο — sports ground", "πίνακα": "πίνακας — board; painting", "εκδρομές": "εκδρομή — (school) trip, excursion"},
})

ITEMS.append({
 "id": "l161-c1-doppler", "title": "Γιατί αλλάζει η σειρήνα όταν περνά;", "title_en": "Why does the siren change as it passes?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με έναν φυσικό για το φαινόμενο Ντόπλερ.",
 "script": [
  L("Δημοσιογράφος", "f", "Όλοι έχουμε ακούσει τη σειρήνα ενός ασθενοφόρου να ακούγεται πιο ψηλή όσο πλησιάζει και πιο χαμηλή μόλις μας προσπεράσει. Η σειρήνα όμως δεν αλλάζει. Τι αλλάζει;", "We've all heard an ambulance siren sound higher as it approaches and lower as soon as it has passed us. But the siren doesn't change. What changes?"),
  L("Φυσικός", "m", "Αλλάζει η απόσταση ανάμεσα στα κύματα του ήχου που φτάνουν στο αυτί μας. Όταν η πηγή κινείται προς το μέρος μας, κάθε κύμα ξεκινά λίγο πιο κοντά από το προηγούμενο, οπότε τα κύματα «συμπιέζονται» και φτάνουν πιο πυκνά: ακούμε υψηλότερη συχνότητα. Όταν απομακρύνεται, συμβαίνει το αντίθετο. Την εξήγηση τη διατύπωσε ο Αυστριακός φυσικός Κρίστιαν Ντόπλερ το 1842, αρχικά για το φως των άστρων.", "The spacing between the sound waves reaching our ear changes. When the source moves towards us, each wave starts a little closer than the previous one, so the waves are 'compressed' and arrive more densely: we hear a higher frequency. When it moves away, the opposite happens. The explanation was formulated by the Austrian physicist Christian Doppler in 1842, originally for the light of stars."),
  L("Δημοσιογράφος", "f", "Πώς αποδείχτηκε;", "How was it proven?"),
  L("Φυσικός", "m", "Με ένα πείραμα που έχει κάτι κωμικό. Το 1845 ο Ολλανδός επιστήμονας Μπάις Μπάλοτ έβαλε μουσικούς να παίζουν μια σταθερή νότα με την τρομπέτα πάνω σε ένα κινούμενο τρένο, ενώ άλλοι μουσικοί, με απόλυτη ακοή, στέκονταν δίπλα στις γραμμές και σημείωναν τι άκουγαν. Η νότα άλλαζε ακριβώς όπως είχε προβλέψει ο Ντόπλερ.", "With an experiment that has something comic about it. In 1845 the Dutch scientist Buys Ballot had musicians play a steady note on the trumpet on a moving train, while other musicians with perfect pitch stood beside the tracks and noted what they heard. The note changed exactly as Doppler had predicted."),
  L("Δημοσιογράφος", "f", "Και πού το χρησιμοποιούμε σήμερα;", "And where do we use it today?"),
  L("Φυσικός", "m", "Παντού, χωρίς να το ξέρουμε. Τα ραντάρ της τροχαίας μετρούν την ταχύτητα των αυτοκινήτων από τη μεταβολή της συχνότητας. Οι γιατροί βλέπουν με τον υπέρηχο Ντόπλερ πόσο γρήγορα κυλάει το αίμα στις φλέβες. Και οι αστρονόμοι, παρατηρώντας ότι το φως των μακρινών γαλαξιών μετατοπίζεται προς το κόκκινο, συμπέραναν ότι απομακρύνονται από εμάς, δηλαδή ότι το σύμπαν διαστέλλεται.", "Everywhere, without our knowing it. Traffic police radar measures the speed of cars from the change in frequency. Doctors use Doppler ultrasound to see how fast blood flows in the veins. And astronomers, observing that the light from distant galaxies is shifted towards red, concluded that they are moving away from us, in other words that the universe is expanding."),
 ],
 "questions": [
  Q("Γιατί ακούμε τη σειρήνα πιο ψηλή όσο πλησιάζει;", ["Γιατί ο οδηγός την αλλάζει", "Γιατί τα κύματα του ήχου συμπιέζονται και φτάνουν πιο πυκνά", "Γιατί ο ήχος γίνεται πιο δυνατός", "Γιατί ο αέρας ζεσταίνεται"], 1, "τα κύματα «συμπιέζονται» και φτάνουν πιο πυκνά"),
  Q("Για ποιο φαινόμενο διατύπωσε αρχικά ο Ντόπλερ την εξήγησή του;", ["Για τον ήχο των τρένων", "Για τη μουσική", "Για τη θάλασσα", "Για το φως των άστρων"], 3, "αρχικά για το φως των άστρων"),
  Q("Πώς έγινε το πείραμα του Μπάις Μπάλοτ;", ["Με ηχογραφήσεις στο εργαστήριο", "Με μουσικούς που έπαιζαν τρομπέτα πάνω σε κινούμενο τρένο", "Με σειρήνες ασθενοφόρων", "Με τηλεσκόπια"], 1, "έβαλε μουσικούς να παίζουν μια σταθερή νότα με την τρομπέτα πάνω σε ένα κινούμενο τρένο"),
  Q("Τι συμπέραναν οι αστρονόμοι από τη μετατόπιση του φωτός προς το κόκκινο;", ["Ότι οι γαλαξίες πλησιάζουν", "Ότι τα άστρα σβήνουν", "Ότι το σύμπαν διαστέλλεται", "Ότι ο Ήλιος ψύχεται"], 2, "το σύμπαν διαστέλλεται"),
 ],
 "gloss": {"σειρήνα": "σειρήνα — siren", "ασθενοφόρου": "ασθενοφόρο — ambulance", "προσπεράσει": "προσπερνώ — to pass, to overtake", "κύματα": "κύμα — wave", "πηγή": "πηγή — source", "συμπιέζονται": "συμπιέζομαι — to be compressed", "πυκνά": "πυκνά — densely", "συχνότητα": "συχνότητα — frequency", "απομακρύνεται": "απομακρύνομαι — to move away", "απόλυτη ακοή": "απόλυτη ακοή — perfect pitch", "ραντάρ": "ραντάρ — radar", "υπέρηχο": "υπέρηχος — ultrasound", "φλέβες": "φλέβα — vein", "γαλαξιών": "γαλαξίας — galaxy", "μετατοπίζεται": "μετατοπίζομαι — to shift", "διαστέλλεται": "διαστέλλομαι — to expand"},
})

ITEMS.append({
 "id": "l161-c1-giffen", "title": "Όταν η τιμή ανεβαίνει και αγοράζουμε περισσότερο", "title_en": "When the price goes up and we buy more", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από διάλεξη οικονομικών για τα λεγόμενα αγαθά Γκίφεν.",
 "script": [
  L("Καθηγήτρια", "f", "Ο πρώτος νόμος που μαθαίνει κάθε φοιτητής οικονομικών είναι ο νόμος της ζήτησης: όταν η τιμή ενός προϊόντος ανεβαίνει, αγοράζουμε λιγότερο. Υπάρχει όμως μια θεωρητική εξαίρεση, που ο Άλφρεντ Μάρσαλ απέδωσε στα τέλη του δέκατου ένατου αιώνα στον Βρετανό οικονομολόγο Ρόμπερτ Γκίφεν, και γι' αυτό ονομάζεται «αγαθό Γκίφεν».", "The first law every economics student learns is the law of demand: when the price of a product rises, we buy less. There is, however, a theoretical exception, which Alfred Marshall attributed at the end of the nineteenth century to the British economist Robert Giffen, and that is why it is called a 'Giffen good'."),
  L("Καθηγήτρια", "f", "Φανταστείτε μια πολύ φτωχή οικογένεια που ζει κυρίως με ψωμί και τρώει λίγο κρέας όποτε μπορεί. Αν ανέβει η τιμή του ψωμιού, το εισόδημα που της μένει δεν φτάνει πια για το κρέας. Για να μην πεινάσει, κόβει εντελώς το κρέας και αγοράζει ακόμη περισσότερο ψωμί, το φθηνότερο αγαθό που της δίνει θερμίδες. Η ακρίβεια, λοιπόν, αυξάνει τη ζήτηση.", "Imagine a very poor family that lives mainly on bread and eats a little meat whenever it can. If the price of bread goes up, the income left over is no longer enough for meat. In order not to go hungry, it cuts out meat completely and buys even more bread, the cheapest good that gives it calories. Higher prices, then, increase demand."),
  L("Καθηγήτρια", "f", "Για δεκαετίες το παράδειγμα που έδιναν τα εγχειρίδια ήταν οι πατάτες στον μεγάλο λιμό της Ιρλανδίας, αλλά οι ιστορικοί δεν βρήκαν στοιχεία που να το στηρίζουν. Η πρώτη πειστική ένδειξη ήρθε μόλις το 2008: δύο οικονομολόγοι μελέτησαν φτωχά νοικοκυριά σε μια επαρχία της Κίνας και βρήκαν ότι, όταν το ρύζι γινόταν ακριβότερο, τα πιο φτωχά από αυτά αγόραζαν πράγματι περισσότερο. Το δίδαγμα είναι ότι οι νόμοι της οικονομίας περιγράφουν το συνηθισμένο, όχι το αναπόφευκτο· στα όρια της φτώχειας, η λογική των επιλογών μπορεί να αντιστραφεί.", "For decades the example given by textbooks was potatoes in the Great Famine in Ireland, but historians found no evidence to support it. The first convincing evidence came only in 2008: two economists studied poor households in a province of China and found that, when rice became more expensive, the poorest of them did indeed buy more. The lesson is that the laws of economics describe the usual, not the inevitable; at the edge of poverty, the logic of choices can be reversed."),
 ],
 "questions": [
  Q("Τι λέει ο νόμος της ζήτησης;", ["Ότι όταν η τιμή ανεβαίνει, αγοράζουμε λιγότερο", "Ότι όταν η τιμή ανεβαίνει, αγοράζουμε περισσότερο", "Ότι η ζήτηση δεν εξαρτάται από την τιμή", "Ότι οι φτωχοί αγοράζουν πάντα τα φθηνότερα"], 0, "όταν η τιμή ενός προϊόντος ανεβαίνει, αγοράζουμε λιγότερο"),
  Q("Γιατί η φτωχή οικογένεια του παραδείγματος αγοράζει περισσότερο ψωμί όταν ακριβαίνει;", ["Γιατί της αρέσει περισσότερο", "Γιατί φοβάται ότι θα ακριβύνει κι άλλο", "Γιατί κόβει εντελώς το κρέας και χρειάζεται τις θερμίδες από το φθηνότερο αγαθό", "Γιατί παίρνει επίδομα"], 2, "κόβει εντελώς το κρέας και αγοράζει ακόμη περισσότερο ψωμί"),
  Q("Τι λέει η καθηγήτρια για το παράδειγμα με τις πατάτες στην Ιρλανδία;", ["Ότι είναι η καλύτερη απόδειξη", "Ότι οι ιστορικοί δεν βρήκαν στοιχεία που να το στηρίζουν", "Ότι το ανακάλυψε ο Γκίφεν", "Ότι αφορούσε το ρύζι"], 1, "οι ιστορικοί δεν βρήκαν στοιχεία που να το στηρίζουν"),
  Q("Ποιο είναι το δίδαγμα, κατά την καθηγήτρια;", ["Ότι ο νόμος της ζήτησης είναι λάθος", "Ότι η Κίνα είναι εξαίρεση", "Ότι οι φτωχοί δεν κάνουν λογικές επιλογές", "Ότι οι νόμοι της οικονομίας περιγράφουν το συνηθισμένο, όχι το αναπόφευκτο"], 3, "οι νόμοι της οικονομίας περιγράφουν το συνηθισμένο, όχι το αναπόφευκτο"),
 ],
 "gloss": {"αγαθά": "αγαθό — good, commodity", "ζήτησης": "ζήτηση — demand", "εξαίρεση": "εξαίρεση — exception", "απέδωσε": "αποδίδω — to attribute", "αγαθό": "αγαθό — good, commodity", "εισόδημα": "εισόδημα — income", "πεινάσει": "πεινάω — to be hungry", "θερμίδες": "θερμίδα — calorie", "ακρίβεια": "ακρίβεια — high prices; precision", "εγχειρίδια": "εγχειρίδιο — textbook", "λιμό": "λιμός — famine", "ένδειξη": "ένδειξη — evidence, indication", "νοικοκυριά": "νοικοκυριό — household", "επαρχία": "επαρχία — province", "αναπόφευκτο": "αναπόφευκτος — inevitable", "αντιστραφεί": "αντιστρέφομαι — to be reversed"},
})

rnd = random.Random(161)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-161.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
