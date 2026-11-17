# Source for library/listening/listening-147.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l147.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l147-vm-elaiochromatistis", "title": "Ο ελαιοχρωματιστής", "title_en": "The painter and decorator", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον ελαιοχρωματιστή που θα βάψει το διαμέρισμά σας.",
 "script": [
  L("Ελαιοχρωματιστής", "m", "Καλημέρα, ο Τάσος είμαι, για το βάψιμο του διαμερίσματος. Σας άφησα χθες στο γραμματοκιβώτιο ένα δειγματολόγιο με χρώματα. Διαλέξτε με την ησυχία σας και πείτε μου μέχρι την Παρασκευή, για να προλάβω να παραγγείλω τις μπογιές.", "Good morning, it's Tasos, about painting the flat. Yesterday I left a colour sample book in your letterbox. Choose at your leisure and tell me by Friday, so I have time to order the paints."),
  L("Ελαιοχρωματιστής", "m", "Μια συμβουλή: για την κουζίνα και το μπάνιο προτείνω πλενόμενο χρώμα, γιατί εκεί υπάρχει υγρασία και λερώνονται πιο εύκολα οι τοίχοι.", "One piece of advice: for the kitchen and bathroom I suggest a washable paint, because there's humidity there and the walls get dirty more easily."),
  L("Ελαιοχρωματιστής", "m", "Τη Δευτέρα που θα ξεκινήσουμε, καλό θα ήταν να έχετε μαζέψει τα μικρά αντικείμενα και τους πίνακες από τους τοίχους. Τα μεγάλα έπιπλα θα τα σκεπάσουμε εμείς με νάιλον. Η δουλειά θα κρατήσει τέσσερις μέρες.", "On the Monday we start, it would be good if you'd collected the small objects and the pictures from the walls. We'll cover the big furniture with plastic sheeting. The job will take four days."),
 ],
 "questions": [
  Q("Τι άφησε ο ελαιοχρωματιστής στο γραμματοκιβώτιο;", ["Ένα δειγματολόγιο με χρώματα", "Ένα τιμολόγιο", "Τα κλειδιά", "Ένα κουτί μπογιά"], 0, "Σας άφησα χθες στο γραμματοκιβώτιο ένα δειγματολόγιο με χρώματα"),
  Q("Γιατί προτείνει πλενόμενο χρώμα για την κουζίνα και το μπάνιο;", ["Γιατί είναι φθηνότερο", "Γιατί εκεί υπάρχει υγρασία και οι τοίχοι λερώνονται πιο εύκολα", "Γιατί στεγνώνει πιο γρήγορα", "Γιατί δεν μυρίζει"], 1, "εκεί υπάρχει υγρασία και λερώνονται πιο εύκολα οι τοίχοι"),
  Q("Τι πρέπει να έχετε κάνει πριν από τη Δευτέρα;", ["Να έχετε σκεπάσει τα έπιπλα", "Να έχετε αγοράσει τις μπογιές", "Να έχετε μαζέψει τα μικρά αντικείμενα και τους πίνακες", "Να έχετε φύγει από το σπίτι"], 2, "να έχετε μαζέψει τα μικρά αντικείμενα και τους πίνακες από τους τοίχους"),
 ],
 "gloss": {"ελαιοχρωματιστή": "ελαιοχρωματιστής — painter and decorator", "βάψιμο": "βάψιμο — painting", "γραμματοκιβώτιο": "γραμματοκιβώτιο — letterbox", "δειγματολόγιο": "δειγματολόγιο — sample book", "μπογιές": "μπογιά — paint", "πλενόμενο": "πλενόμενος — washable", "υγρασία": "υγρασία — damp, humidity", "σκεπάσουμε": "σκεπάζω — to cover", "νάιλον": "νάιλον — plastic sheeting"}
})

ITEMS.append({
 "id": "l147-ann-ekleipsi", "title": "Βραδιά παρατήρησης της έκλειψης", "title_en": "An evening to watch the eclipse", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στο ραδιόφωνο για μια εκδήλωση ενός αστρονομικού συλλόγου.",
 "script": [
  L("Εκφωνητής", "m", "Την Κυριακή το βράδυ θα γίνει ολική έκλειψη Σελήνης, και ο αστρονομικός σύλλογος της πόλης διοργανώνει βραδιά παρατήρησης στον λόφο του Αγίου Γεωργίου. Η είσοδος είναι ελεύθερη.", "On Sunday evening there will be a total lunar eclipse, and the city's astronomy club is organising an observation evening on the hill of Agios Georgios. Entry is free."),
  L("Εκφωνητής", "m", "Η έκλειψη ξεκινά λίγο μετά τις εννιά, ενώ η ολική φάση, όταν η Σελήνη παίρνει ένα κοκκινωπό χρώμα, θα διαρκέσει περίπου μία ώρα. Μέλη του συλλόγου θα έχουν στήσει τηλεσκόπια και θα εξηγούν τι συμβαίνει.", "The eclipse begins shortly after nine, while the total phase, when the Moon takes on a reddish colour, will last about an hour. Club members will have set up telescopes and will explain what is happening."),
  L("Εκφωνητής", "m", "Σε αντίθεση με την έκλειψη Ηλίου, η έκλειψη Σελήνης μπορεί να παρατηρηθεί με γυμνό μάτι χωρίς κανέναν κίνδυνο. Φέρτε μαζί σας ζεστά ρούχα και, αν θέλετε, ένα κιάλι. Σε περίπτωση συννεφιάς, η εκδήλωση θα γίνει στην αίθουσα του συλλόγου, με ζωντανή μετάδοση.", "Unlike a solar eclipse, a lunar eclipse can be observed with the naked eye without any risk. Bring warm clothes and, if you like, binoculars. In case of cloud, the event will take place in the club's hall, with a live broadcast."),
 ],
 "questions": [
  Q("Πόσο θα διαρκέσει η ολική φάση;", ["Δέκα λεπτά", "Περίπου μία ώρα", "Όλη τη νύχτα", "Τρεις ώρες"], 1, "θα διαρκέσει περίπου μία ώρα"),
  Q("Τι ισχύει για την παρατήρηση της έκλειψης Σελήνης;", ["Χρειάζονται ειδικά γυαλιά", "Επιτρέπεται μόνο με τηλεσκόπιο", "Μπορεί να γίνει με γυμνό μάτι χωρίς κίνδυνο", "Είναι επικίνδυνη για τα παιδιά"], 2, "μπορεί να παρατηρηθεί με γυμνό μάτι χωρίς κανέναν κίνδυνο"),
  Q("Τι θα γίνει αν έχει συννεφιά;", ["Η εκδήλωση θα γίνει στην αίθουσα του συλλόγου με ζωντανή μετάδοση", "Η εκδήλωση θα ακυρωθεί", "Θα μεταφερθεί την επόμενη Κυριακή", "Θα γίνει σε άλλον λόφο"], 0, "η εκδήλωση θα γίνει στην αίθουσα του συλλόγου, με ζωντανή μετάδοση"),
 ],
 "gloss": {"αστρονομικού": "αστρονομικός — astronomical", "ολική": "ολικός — total", "έκλειψη": "έκλειψη — eclipse", "διοργανώνει": "διοργανώνω — to organise", "κοκκινωπό": "κοκκινωπός — reddish", "τηλεσκόπια": "τηλεσκόπιο — telescope", "γυμνό μάτι": "γυμνό μάτι — naked eye", "κιάλι": "κιάλι — binoculars", "συννεφιάς": "συννεφιά — cloud cover", "μετάδοση": "μετάδοση — broadcast"}
})

ITEMS.append({
 "id": "l147-dia-taratsa-kipos", "title": "Ένας κήπος στην ταράτσα", "title_en": "A garden on the roof", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο ανάμεσα σε δύο γείτονες σε μια πολυκατοικία.",
 "script": [
  L("Ρένα", "f", "Κύριε Γιώργο, σκεφτόμουν να φτιάξουμε έναν μικρό κήπο στην ταράτσα. Είναι τόσος χώρος άδειος, και το καλοκαίρι καίγεται από τον ήλιο.", "Mr Giorgos, I was thinking we could make a small garden on the roof. There's so much empty space, and in summer it's baking in the sun."),
  L("Γιώργος", "m", "Καλή ιδέα, αλλά πρέπει να συμφωνήσουν όλοι οι ένοικοι στη γενική συνέλευση. Και πρέπει να ρωτήσουμε έναν μηχανικό πόσο βάρος αντέχει η ταράτσα, γιατί το χώμα με το νερό είναι πολύ βαρύ.", "Good idea, but all the residents have to agree at the general meeting. And we need to ask an engineer how much weight the roof can take, because soil with water is very heavy."),
  L("Ρένα", "f", "Σκέφτηκα να βάλουμε μεγάλες γλάστρες και όχι χώμα παντού. Και ένα σύστημα που ποτίζει αυτόματα, για να μην εξαρτόμαστε από κανέναν τον Αύγουστο.", "I thought we'd use big pots and not soil everywhere. And a system that waters automatically, so we don't depend on anyone in August."),
  L("Γιώργος", "m", "Τότε ετοίμασε μια πρόταση με το κόστος, και να τη συζητήσουμε στη συνέλευση τον άλλο μήνα. Αν θέλεις, σε βοηθάω με τις τιμές· ο ανιψιός μου έχει φυτώριο.", "Then prepare a proposal with the cost, and let's discuss it at the meeting next month. If you like, I'll help you with prices; my nephew has a plant nursery."),
 ],
 "questions": [
  Q("Τι πρέπει να γίνει πρώτα, σύμφωνα με τον κύριο Γιώργο;", ["Να αγοράσουν φυτά", "Να συμφωνήσουν όλοι οι ένοικοι στη γενική συνέλευση", "Να βάψουν την ταράτσα", "Να πληρώσει η Ρένα"], 1, "πρέπει να συμφωνήσουν όλοι οι ένοικοι στη γενική συνέλευση"),
  Q("Γιατί πρέπει να ρωτήσουν έναν μηχανικό;", ["Γιατί το χώμα με το νερό είναι πολύ βαρύ", "Γιατί η ταράτσα έχει ρωγμές", "Γιατί χρειάζεται άδεια από τον δήμο", "Γιατί θέλουν να βάλουν πισίνα"], 0, "το χώμα με το νερό είναι πολύ βαρύ"),
  Q("Πώς μπορεί να βοηθήσει ο κύριος Γιώργος;", ["Θα ποτίζει τον Αύγουστο", "Θα πληρώσει τις γλάστρες", "Θα βοηθήσει με τις τιμές, γιατί ο ανιψιός του έχει φυτώριο", "Θα μιλήσει στον μηχανικό"], 2, "ο ανιψιός μου έχει φυτώριο"),
 ],
 "gloss": {"ταράτσα": "ταράτσα — flat roof", "ένοικοι": "ένοικος — resident, tenant", "γενική συνέλευση": "γενική συνέλευση — general meeting", "μηχανικό": "μηχανικός — engineer", "αντέχει": "αντέχω — to bear, withstand", "γλάστρες": "γλάστρα — flowerpot", "ποτίζει": "ποτίζω — to water", "εξαρτόμαστε": "εξαρτώμαι — to depend", "ανιψιός": "ανιψιός — nephew", "φυτώριο": "φυτώριο — plant nursery"}
})

ITEMS.append({
 "id": "l147-int-skylos-odigos", "title": "Η εκπαιδεύτρια σκύλων-οδηγών", "title_en": "The guide-dog trainer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε ραδιοφωνική εκπομπή με μια γυναίκα που εκπαιδεύει σκύλους-οδηγούς για τυφλούς.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσο κρατάει η εκπαίδευση ενός σκύλου-οδηγού;", "How long does a guide dog's training take?"),
  L("Εκπαιδεύτρια", "f", "Συνολικά γύρω στα δύο χρόνια. Τον πρώτο χρόνο το κουτάβι μένει σε μια εθελοντική οικογένεια, που του μαθαίνει να ζει ανάμεσα σε ανθρώπους, σε λεωφορεία, σε μαγαζιά. Μετά έρχεται σε εμάς για την κανονική εκπαίδευση.", "About two years in total. In the first year the puppy stays with a volunteer family, who teach it to live among people, on buses, in shops. Then it comes to us for the proper training."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο δύσκολο που πρέπει να μάθει;", "What's the hardest thing it has to learn?"),
  L("Εκπαιδεύτρια", "f", "Αυτό που λέμε «έξυπνη ανυπακοή». Αν ο άνθρωπος του πει «εμπρός» αλλά έρχεται αυτοκίνητο, ο σκύλος πρέπει να αρνηθεί να προχωρήσει. Δεν είναι εύκολο να μάθεις σε ένα ζώο πότε να μην υπακούει.", "What we call \"intelligent disobedience\". If its person tells it \"forward\" but a car is coming, the dog must refuse to go on. It isn't easy to teach an animal when not to obey."),
  L("Δημοσιογράφος", "m", "Τι θα θέλατε να ξέρει το κοινό;", "What would you like the public to know?"),
  L("Εκπαιδεύτρια", "f", "Ότι όταν ο σκύλος φοράει το λουρί εργασίας, δουλεύει. Μην τον χαϊδεύετε και μην του δίνετε φαγητό, γιατί αποσπάται η προσοχή του. Και ότι, σύμφωνα με τον νόμο, οι σκύλοι-οδηγοί μπορούν να μπαίνουν παντού, και στα εστιατόρια.", "That when the dog is wearing its working harness, it's working. Don't stroke it and don't give it food, because it gets distracted. And that, by law, guide dogs can go everywhere, restaurants included."),
 ],
 "questions": [
  Q("Τι γίνεται τον πρώτο χρόνο;", ["Το κουτάβι μένει σε μια εθελοντική οικογένεια", "Το κουτάβι μένει με τη μητέρα του", "Ξεκινά αμέσως η κανονική εκπαίδευση", "Το κουτάβι μένει με τον τυφλό"], 0, "Τον πρώτο χρόνο το κουτάβι μένει σε μια εθελοντική οικογένεια"),
  Q("Τι είναι η «έξυπνη ανυπακοή»;", ["Όταν ο σκύλος δεν θέλει να δουλέψει", "Όταν ο σκύλος αρνείται να προχωρήσει γιατί υπάρχει κίνδυνος", "Όταν ο σκύλος παίζει", "Όταν ο σκύλος γαβγίζει σε ξένους"], 1, "ο σκύλος πρέπει να αρνηθεί να προχωρήσει"),
  Q("Γιατί δεν πρέπει να χαϊδεύουμε έναν σκύλο-οδηγό που δουλεύει;", ["Γιατί μπορεί να δαγκώσει", "Γιατί απαγορεύεται από τον νόμο", "Γιατί αποσπάται η προσοχή του", "Γιατί δεν του αρέσει"], 2, "γιατί αποσπάται η προσοχή του"),
 ],
 "gloss": {"εκπαιδεύει": "εκπαιδεύω — to train", "σκύλους-οδηγούς": "σκύλος-οδηγός — guide dog", "τυφλούς": "τυφλός — blind", "κουτάβι": "κουτάβι — puppy", "ανυπακοή": "ανυπακοή — disobedience", "αρνηθεί": "αρνούμαι — to refuse", "υπακούει": "υπακούω — to obey", "λουρί": "λουρί — harness, strap", "χαϊδεύετε": "χαϊδεύω — to stroke", "αποσπάται": "αποσπάται η προσοχή — to be distracted"}
})

ITEMS.append({
 "id": "l147-news-dytes-limani", "title": "Δύτες καθάρισαν τον βυθό του λιμανιού", "title_en": "Divers cleaned the harbour floor", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός τοπικού ραδιοφώνου.",
 "script": [
  L("Εκφωνήτρια", "f", "Πάνω από δύο τόνους σκουπίδια έβγαλαν το Σάββατο εθελοντές δύτες από τον βυθό του λιμανιού της Καλαμάτας. Ανάμεσά τους ήταν λάστιχα αυτοκινήτων, καρέκλες, ένα ποδήλατο και εκατοντάδες πλαστικά μπουκάλια.", "On Saturday volunteer divers brought up more than two tonnes of rubbish from the floor of Kalamata harbour. Among it were car tyres, chairs, a bicycle and hundreds of plastic bottles."),
  L("Εκφωνήτρια", "f", "Τη δράση οργάνωσε ένας τοπικός σύλλογος καταδύσεων, με τη συνεργασία του λιμεναρχείου, που απαγόρευσε την κίνηση των σκαφών στην περιοχή για όλη τη διάρκεια του καθαρισμού. Στην προβλήτα, μαθητές ξεχώριζαν τα σκουπίδια για ανακύκλωση.", "The action was organised by a local diving club, with the cooperation of the port authority, which banned boat traffic in the area for the whole duration of the clean-up. On the pier, pupils sorted the rubbish for recycling."),
  L("Εκφωνήτρια", "f", "Οι διοργανωτές τόνισαν ότι τα περισσότερα σκουπίδια δεν πετάχτηκαν στη θάλασσα από τα σκάφη, αλλά τα παρέσυρε ο αέρας και η βροχή από τους δρόμους της πόλης.", "The organisers stressed that most of the rubbish was not thrown into the sea from boats, but was carried by wind and rain from the city's streets."),
 ],
 "questions": [
  Q("Τι έβγαλαν οι δύτες από τον βυθό;", ["Πάνω από δύο τόνους σκουπίδια", "Ένα αρχαίο άγαλμα", "Ένα βυθισμένο σκάφος", "Μόνο πλαστικά μπουκάλια"], 0, "Πάνω από δύο τόνους σκουπίδια"),
  Q("Τι έκανε το λιμεναρχείο;", ["Πλήρωσε τους δύτες", "Απαγόρευσε την κίνηση των σκαφών στην περιοχή", "Έφερε σκάφη για τα σκουπίδια", "Δεν συμμετείχε"], 1, "απαγόρευσε την κίνηση των σκαφών στην περιοχή"),
  Q("Από πού προέρχονταν τα περισσότερα σκουπίδια, σύμφωνα με τους διοργανωτές;", ["Από τα σκάφη", "Από τους τουρίστες της παραλίας", "Από τους δρόμους της πόλης, με τον αέρα και τη βροχή", "Από άλλες χώρες"], 2, "τα παρέσυρε ο αέρας και η βροχή από τους δρόμους της πόλης"),
 ],
 "gloss": {"τόνους": "τόνος — tonne", "δύτες": "δύτης — diver", "βυθό": "βυθός — seabed", "λάστιχα": "λάστιχο — tyre", "καταδύσεων": "κατάδυση — diving", "λιμεναρχείου": "λιμεναρχείο — port authority", "σκαφών": "σκάφος — boat", "προβλήτα": "προβλήτα — pier", "ξεχώριζαν": "ξεχωρίζω — to sort, separate", "παρέσυρε": "παρασύρω — to carry away"}
})

ITEMS.append({
 "id": "l147-mon-karpouzi", "title": "Πώς διαλέγουμε καρπούζι", "title_en": "How to choose a watermelon", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε ένα απόσπασμα από μια καλοκαιρινή εκπομπή με πρακτικές συμβουλές.",
 "script": [
  L("Παρουσιάστρια", "f", "Όλοι έχουμε φέρει κάποια φορά στο σπίτι ένα καρπούζι άνοστο και άγουρο. Μερικά απλά σημάδια όμως μας βοηθούν να διαλέξουμε σωστά. Πρώτα κοιτάξτε από κάτω: ένα καρπούζι που ωρίμασε στο χωράφι έχει μια κιτρινωπή κηλίδα στο σημείο όπου ακουμπούσε στο χώμα.", "We've all brought home a tasteless, unripe watermelon at some point. A few simple signs, though, help us choose correctly. First look underneath: a watermelon that ripened in the field has a yellowish patch where it rested on the soil."),
  L("Παρουσιάστρια", "f", "Αν η κηλίδα είναι άσπρη ή δεν υπάρχει καθόλου, μάλλον το έκοψαν νωρίς. Δεύτερον, σηκώστε το: ένα καλό καρπούζι είναι βαρύ για το μέγεθός του, γιατί έχει πολύ ζουμί.", "If the patch is white or there isn't one at all, it was probably picked early. Second, lift it: a good watermelon is heavy for its size, because it's very juicy."),
  L("Παρουσιάστρια", "f", "Και τρίτον, το γνωστό χτύπημα. Χτυπήστε το ελαφρά με τα δάχτυλα. Αν ο ήχος είναι βαθύς, σαν τύμπανο, είναι έτοιμο. Αν είναι μουντός, μάλλον έχει παραωριμάσει. Και θυμηθείτε: το καρπούζι δεν ωριμάζει άλλο αφού κοπεί.", "And third, the well-known tap. Tap it lightly with your fingers. If the sound is deep, like a drum, it's ready. If it's dull, it's probably overripe. And remember: a watermelon doesn't ripen any further once it's been picked."),
 ],
 "questions": [
  Q("Τι δείχνει η κιτρινωπή κηλίδα από κάτω;", ["Ότι το καρπούζι ωρίμασε στο χωράφι", "Ότι το καρπούζι είναι χαλασμένο", "Ότι είναι εισαγόμενο", "Ότι έχει πολλά κουκούτσια"], 0, "ένα καρπούζι που ωρίμασε στο χωράφι έχει μια κιτρινωπή κηλίδα"),
  Q("Γιατί ένα καλό καρπούζι είναι βαρύ για το μέγεθός του;", ["Γιατί έχει χοντρή φλούδα", "Γιατί έχει πολύ ζουμί", "Γιατί έχει πολλή ζάχαρη", "Γιατί είναι μεγάλο"], 1, "γιατί έχει πολύ ζουμί"),
  Q("Τι ισχύει αφού κοπεί το καρπούζι;", ["Ωριμάζει γρηγορότερα στο ψυγείο", "Γίνεται πιο γλυκό", "Δεν ωριμάζει άλλο", "Πρέπει να μείνει στον ήλιο"], 2, "το καρπούζι δεν ωριμάζει άλλο αφού κοπεί"),
 ],
 "gloss": {"καρπούζι": "καρπούζι — watermelon", "άνοστο": "άνοστος — tasteless", "άγουρο": "άγουρος — unripe", "ωρίμασε": "ωριμάζω — to ripen", "κιτρινωπή": "κιτρινωπός — yellowish", "κηλίδα": "κηλίδα — patch, spot", "ζουμί": "ζουμί — juice", "μουντός": "μουντός — dull", "παραωριμάσει": "παραωριμάζω — to become overripe"}
})

ITEMS.append({
 "id": "l147-rep-skylia-grafeio", "title": "Σκυλιά στο γραφείο", "title_en": "Dogs at the office", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για τον χώρο εργασίας.",
 "script": [
  L("Ρεπόρτερ", "f", "Όλο και περισσότερες εταιρείες, κυρίως στον χώρο της τεχνολογίας, επιτρέπουν στους υπαλλήλους τους να φέρνουν τον σκύλο τους στη δουλειά. Σε ένα γραφείο στο Μαρούσι, κάτω από τα γραφεία κοιμούνται τέσσερα σκυλιά, ενώ ένα πέμπτο περιφέρεται ζητώντας χάδια.", "More and more companies, mainly in the technology sector, allow their employees to bring their dog to work. In an office in Marousi, four dogs sleep under the desks, while a fifth wanders around asking to be stroked."),
  L("Ρεπόρτερ", "f", "Η υπεύθυνη προσωπικού λέει ότι οι εργαζόμενοι νιώθουν λιγότερο άγχος και κάνουν περισσότερα διαλείμματα για να περπατήσουν, κάτι που κάνει καλό και στους ίδιους. Υπάρχουν όμως κανόνες: κάθε σκύλος πρέπει να είναι εμβολιασμένος και ήρεμος, και κάποιες αίθουσες μένουν χωρίς ζώα.", "The HR manager says employees feel less stress and take more breaks to walk, which does them good too. But there are rules: every dog must be vaccinated and calm, and some rooms stay animal-free."),
  L("Ρεπόρτερ", "f", "Δεν είναι όλοι ενθουσιασμένοι. Ένας προγραμματιστής μάς είπε ότι έχει αλλεργία, και ότι η εταιρεία τού έδωσε ένα γραφείο σε άλλον όροφο. «Αγαπώ τα ζώα», είπε, «αλλά προτιμώ να τα βλέπω από μακριά.»", "Not everyone is thrilled. A programmer told us he has an allergy, and the company gave him an office on another floor. \"I love animals,\" he said, \"but I prefer to see them from a distance.\""),
 ],
 "questions": [
  Q("Τι λέει η υπεύθυνη προσωπικού για τους εργαζόμενους;", ["Ότι δουλεύουν λιγότερο", "Ότι νιώθουν λιγότερο άγχος και κάνουν περισσότερα διαλείμματα για περπάτημα", "Ότι ζητούν μεγαλύτερο μισθό", "Ότι μένουν περισσότερες ώρες"], 1, "οι εργαζόμενοι νιώθουν λιγότερο άγχος"),
  Q("Ποιος από τους παρακάτω είναι κανόνας της εταιρείας;", ["Κάθε σκύλος πρέπει να είναι εμβολιασμένος και ήρεμος", "Οι σκύλοι μπαίνουν σε όλες τις αίθουσες", "Επιτρέπονται μόνο μικρά σκυλιά", "Οι σκύλοι έρχονται μόνο την Παρασκευή"], 0, "κάθε σκύλος πρέπει να είναι εμβολιασμένος και ήρεμος"),
  Q("Πώς λύθηκε το πρόβλημα του προγραμματιστή με την αλλεργία;", ["Του έδωσαν άδεια", "Του επέτρεψαν να δουλεύει από το σπίτι", "Του έδωσαν ένα γραφείο σε άλλον όροφο", "Απαγόρευσαν τους σκύλους"], 2, "η εταιρεία τού έδωσε ένα γραφείο σε άλλον όροφο"),
 ],
 "gloss": {"υπαλλήλους": "υπάλληλος — employee", "περιφέρεται": "περιφέρομαι — to wander around", "χάδια": "χάδι — caress, stroke", "υπεύθυνη προσωπικού": "υπεύθυνη προσωπικού — HR manager", "άγχος": "άγχος — stress", "εμβολιασμένος": "εμβολιασμένος — vaccinated", "ενθουσιασμένοι": "ενθουσιασμένος — thrilled", "προγραμματιστής": "προγραμματιστής — programmer", "αλλεργία": "αλλεργία — allergy"}
})

ITEMS.append({
 "id": "l147-dia-chartziliki", "title": "Πόσο χαρτζιλίκι;", "title_en": "How much pocket money?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο ανάμεσα σε δύο γονείς για το χαρτζιλίκι της κόρης τους.",
 "script": [
  L("Μητέρα", "f", "Η Δανάη μού ζήτησε σήμερα χαρτζιλίκι. Λέει ότι όλες οι φίλες της παίρνουν, και ότι ντρέπεται να μας ζητάει λεφτά κάθε φορά που βγαίνει.", "Danai asked me for pocket money today. She says all her friends get some, and that she's embarrassed to ask us for money every time she goes out."),
  L("Πατέρας", "m", "Στα δώδεκα; Δεν είναι νωρίς; Και πόσα θέλει;", "At twelve? Isn't that early? And how much does she want?"),
  L("Μητέρα", "f", "Είπε δέκα ευρώ την εβδομάδα. Εγώ πιστεύω ότι θα της κάνει καλό. Θα μάθει να υπολογίζει, να κάνει οικονομία, και αν τα ξοδέψει όλα τη Δευτέρα, θα περιμένει μέχρι την άλλη εβδομάδα.", "She said ten euros a week. I think it'll be good for her. She'll learn to budget, to save, and if she spends it all on Monday, she'll wait until the next week."),
  L("Πατέρας", "m", "Εντάξει, αλλά να συμφωνήσουμε από την αρχή τι θα πληρώνει μόνη της. Τα σχολικά και τα ρούχα θα τα πληρώνουμε εμείς, τα σινεμά και τα γλυκά εκείνη. Και να μην της δίνουμε έξτρα κάθε φορά που τελειώνουν.", "OK, but let's agree from the start what she'll pay for herself. School things and clothes we'll pay for, cinema and sweets she will. And we shouldn't give her extra every time it runs out."),
 ],
 "questions": [
  Q("Γιατί ζητάει η Δανάη χαρτζιλίκι;", ["Θέλει να αγοράσει κινητό", "Όλες οι φίλες της παίρνουν και ντρέπεται να ζητάει λεφτά", "Θέλει να πάει εκδρομή", "Της το πρότεινε ο δάσκαλος"], 1, "όλες οι φίλες της παίρνουν"),
  Q("Τι πιστεύει η μητέρα;", ["Ότι η Δανάη είναι πολύ μικρή", "Ότι δέκα ευρώ είναι πολλά", "Ότι θα μάθει να υπολογίζει και να κάνει οικονομία", "Ότι πρέπει να δουλέψει για τα λεφτά"], 2, "Θα μάθει να υπολογίζει, να κάνει οικονομία"),
  Q("Τι θα πληρώνει η Δανάη μόνη της;", ["Τα σινεμά και τα γλυκά", "Τα ρούχα", "Τα σχολικά", "Όλα τα έξοδά της"], 0, "τα σινεμά και τα γλυκά εκείνη"),
 ],
 "gloss": {"χαρτζιλίκι": "χαρτζιλίκι — pocket money", "ντρέπεται": "ντρέπομαι — to be embarrassed", "υπολογίζει": "υπολογίζω — to calculate, budget", "οικονομία": "κάνω οικονομία — to save", "ξοδέψει": "ξοδεύω — to spend", "σχολικά": "σχολικά — school supplies", "έξτρα": "έξτρα — extra"}
})

ITEMS.append({
 "id": "l147-c1-lemons", "title": "Η αγορά των «λεμονιών»", "title_en": "The market for lemons", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη για την οικονομία της πληροφορίας.",
 "script": [
  L("Ομιλητής", "m", "Το 1970 ο οικονομολόγος Τζορτζ Άκερλοφ δημοσίευσε ένα άρθρο με τίτλο «Η αγορά των λεμονιών». Στην αμερικανική αργκό, «λεμόνι» λέγεται ένα μεταχειρισμένο αυτοκίνητο που αποδεικνύεται ελαττωματικό. Το άρθρο απορρίφθηκε αρχικά από αρκετά περιοδικά, και χρόνια αργότερα συνέβαλε στο να τιμηθεί ο συγγραφέας του με το Νόμπελ.", "In 1970 the economist George Akerlof published an article entitled \"The Market for Lemons\". In American slang, a \"lemon\" is a used car that turns out to be defective. The article was initially rejected by several journals, and years later it helped earn its author the Nobel Prize."),
  L("Ομιλητής", "m", "Η ιδέα είναι η εξής: ο πωλητής ξέρει αν το αυτοκίνητο είναι καλό ή «λεμόνι», ο αγοραστής όχι. Επειδή ο αγοραστής δεν μπορεί να τα ξεχωρίσει, προσφέρει μια μέση τιμή. Όσοι όμως έχουν καλά αυτοκίνητα θεωρούν αυτή την τιμή χαμηλή και αποσύρονται από την αγορά.", "The idea is this: the seller knows whether the car is good or a \"lemon\", the buyer doesn't. Because the buyer can't tell them apart, he offers an average price. But those who have good cars consider this price low and withdraw from the market."),
  L("Ομιλητής", "m", "Έτσι, η μέση ποιότητα των αυτοκινήτων που μένουν πέφτει, οι αγοραστές προσφέρουν ακόμα λιγότερα, και σε ακραίες περιπτώσεις η αγορά μπορεί σχεδόν να καταρρεύσει. Το φαινόμενο ονομάζεται «δυσμενής επιλογή» και εμφανίζεται παντού όπου υπάρχει ασύμμετρη πληροφόρηση, από τις ασφάλειες υγείας μέχρι την αγορά εργασίας.", "So the average quality of the cars that remain falls, buyers offer even less, and in extreme cases the market can almost collapse. The phenomenon is called \"adverse selection\" and appears wherever there is asymmetric information, from health insurance to the labour market."),
  L("Ομιλητής", "m", "Οι αγορές έχουν αναπτύξει μηχανισμούς για να το αντιμετωπίσουν: εγγυήσεις, πιστοποιήσεις, αξιολογήσεις από άλλους πελάτες. Όλα αυτά είναι, στην ουσία, τρόποι να μεταφερθεί πληροφορία από αυτόν που την έχει σε αυτόν που τη χρειάζεται.", "Markets have developed mechanisms to deal with it: warranties, certifications, reviews by other customers. All these are, in essence, ways of transferring information from the one who has it to the one who needs it."),
 ],
 "questions": [
  Q("Τι είναι ένα «λεμόνι» στην αμερικανική αργκό;", ["Ένα καινούργιο αυτοκίνητο", "Ένα μεταχειρισμένο αυτοκίνητο που αποδεικνύεται ελαττωματικό", "Ένας κακός πωλητής", "Ένα φθηνό φρούτο"], 1, "ένα μεταχειρισμένο αυτοκίνητο που αποδεικνύεται ελαττωματικό"),
  Q("Γιατί αποσύρονται όσοι έχουν καλά αυτοκίνητα;", ["Γιατί θεωρούν τη μέση τιμή χαμηλή", "Γιατί δεν θέλουν να πουλήσουν", "Γιατί φοβούνται τους αγοραστές", "Γιατί πληρώνουν πολλούς φόρους"], 0, "θεωρούν αυτή την τιμή χαμηλή και αποσύρονται από την αγορά"),
  Q("Πού εμφανίζεται η «δυσμενής επιλογή»;", ["Μόνο στα μεταχειρισμένα αυτοκίνητα", "Μόνο στην Αμερική", "Όπου υπάρχει ασύμμετρη πληροφόρηση", "Μόνο στις τράπεζες"], 2, "εμφανίζεται παντού όπου υπάρχει ασύμμετρη πληροφόρηση"),
  Q("Τι κοινό έχουν οι εγγυήσεις και οι αξιολογήσεις;", ["Κάνουν τα προϊόντα φθηνότερα", "Τις επιβάλλει το κράτος", "Αυξάνουν τα κέρδη των πωλητών", "Μεταφέρουν πληροφορία σε αυτόν που τη χρειάζεται"], 3, "τρόποι να μεταφερθεί πληροφορία από αυτόν που την έχει σε αυτόν που τη χρειάζεται"),
 ],
 "gloss": {"αργκό": "αργκό — slang", "μεταχειρισμένο": "μεταχειρισμένος — used, second-hand", "ελαττωματικό": "ελαττωματικός — defective", "απορρίφθηκε": "απορρίπτομαι — to be rejected", "συνέβαλε": "συμβάλλω — to contribute", "ξεχωρίσει": "ξεχωρίζω — to tell apart", "αποσύρονται": "αποσύρομαι — to withdraw", "καταρρεύσει": "καταρρέω — to collapse", "δυσμενής": "δυσμενής — adverse", "ασύμμετρη": "ασύμμετρος — asymmetric", "εγγυήσεις": "εγγύηση — warranty", "πιστοποιήσεις": "πιστοποίηση — certification"}
})

ITEMS.append({
 "id": "l147-c1-petalouda", "title": "Το φαινόμενο της πεταλούδας", "title_en": "The butterfly effect", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή για την επιστήμη, με καλεσμένη μια μετεωρολόγο.",
 "script": [
  L("Δημοσιογράφος", "m", "Από πού προέρχεται η έκφραση «φαινόμενο της πεταλούδας»;", "Where does the expression \"butterfly effect\" come from?"),
  L("Μετεωρολόγος", "f", "Από τον Αμερικανό μετεωρολόγο Έντουαρντ Λόρεντζ. Στις αρχές της δεκαετίας του 1960 έτρεχε ένα απλό μοντέλο καιρού σε υπολογιστή. Κάποια μέρα ξανάτρεξε μια προσομοίωση, στρογγυλεύοντας έναν αριθμό στο τρίτο δεκαδικό ψηφίο αντί για το έκτο, και το αποτέλεσμα μετά από λίγο καιρό ήταν εντελώς διαφορετικό.", "From the American meteorologist Edward Lorenz. In the early 1960s he was running a simple weather model on a computer. One day he re-ran a simulation, rounding a number to the third decimal place instead of the sixth, and after a while the result was completely different."),
  L("Δημοσιογράφος", "m", "Και η πεταλούδα;", "And the butterfly?"),
  L("Μετεωρολόγος", "f", "Ήρθε αργότερα, σε μια ομιλία του το 1972, με τον τίτλο αν το φτερούγισμα μιας πεταλούδας στη Βραζιλία μπορεί να προκαλέσει ανεμοστρόβιλο στο Τέξας. Η ουσία είναι ότι σε ορισμένα συστήματα, που τα λέμε χαοτικά, μια ελάχιστη διαφορά στις αρχικές συνθήκες μεγαλώνει με τον χρόνο μέχρι να αλλάξει ριζικά την έκβαση.", "It came later, in a talk of his in 1972, entitled whether the flap of a butterfly's wings in Brazil can set off a tornado in Texas. The essence is that in certain systems, which we call chaotic, a tiny difference in the initial conditions grows over time until it radically changes the outcome."),
  L("Δημοσιογράφος", "m", "Γι' αυτό δεν μπορούμε να προβλέψουμε τον καιρό για έναν μήνα;", "Is that why we can't forecast the weather a month ahead?"),
  L("Μετεωρολόγος", "f", "Ακριβώς. Δεν φταίνε μόνο οι υπολογιστές· ακόμα και με τέλειο μοντέλο, δεν θα μετρούσαμε ποτέ την ατμόσφαιρα με απόλυτη ακρίβεια. Γι' αυτό σήμερα τρέχουμε δεκάδες προσομοιώσεις με ελαφρώς διαφορετικά δεδομένα και μιλάμε για πιθανότητες, όχι για βεβαιότητες. Και, βέβαια, καμία συγκεκριμένη πεταλούδα δεν «φταίει» για έναν ανεμοστρόβιλο· η εικόνα είναι μεταφορική.", "Exactly. It's not just the computers' fault; even with a perfect model, we would never measure the atmosphere with absolute precision. That's why today we run dozens of simulations with slightly different data and speak of probabilities, not certainties. And of course no particular butterfly is \"to blame\" for a tornado; the image is metaphorical."),
 ],
 "questions": [
  Q("Τι παρατήρησε ο Λόρεντζ;", ["Ότι μια μικρή στρογγυλοποίηση άλλαξε εντελώς το αποτέλεσμα", "Ότι ο υπολογιστής του είχε χαλάσει", "Ότι οι πεταλούδες επηρεάζουν τον καιρό", "Ότι τα μοντέλα ήταν πάντα ακριβή"], 0, "το αποτέλεσμα μετά από λίγο καιρό ήταν εντελώς διαφορετικό"),
  Q("Τι χαρακτηρίζει τα χαοτικά συστήματα;", ["Είναι εντελώς τυχαία", "Μια ελάχιστη διαφορά στις αρχικές συνθήκες μεγαλώνει με τον χρόνο", "Δεν αλλάζουν ποτέ", "Υπάρχουν μόνο στην ατμόσφαιρα"], 1, "μια ελάχιστη διαφορά στις αρχικές συνθήκες μεγαλώνει με τον χρόνο"),
  Q("Γιατί τρέχουν σήμερα δεκάδες προσομοιώσεις;", ["Για να βρουν την πεταλούδα", "Γιατί οι υπολογιστές είναι φθηνοί", "Για να μιλούν για πιθανότητες, αφού δεν μετράμε την ατμόσφαιρα με απόλυτη ακρίβεια", "Για να προβλέψουν τον καιρό για έναν χρόνο"], 2, "μιλάμε για πιθανότητες, όχι για βεβαιότητες"),
  Q("Τι λέει η μετεωρολόγος για την εικόνα της πεταλούδας;", ["Ότι είναι επιστημονικά αποδεδειγμένη", "Ότι την επινόησε ένας δημοσιογράφος", "Ότι αφορά μόνο τη Βραζιλία", "Ότι είναι μεταφορική"], 3, "η εικόνα είναι μεταφορική"),
 ],
 "gloss": {"μετεωρολόγο": "μετεωρολόγος — meteorologist", "μοντέλο": "μοντέλο — model", "προσομοίωση": "προσομοίωση — simulation", "στρογγυλεύοντας": "στρογγυλεύω — to round (a number)", "δεκαδικό ψηφίο": "δεκαδικό ψηφίο — decimal place", "φτερούγισμα": "φτερούγισμα — flapping of wings", "ανεμοστρόβιλο": "ανεμοστρόβιλος — tornado", "χαοτικά": "χαοτικός — chaotic", "έκβαση": "έκβαση — outcome", "βεβαιότητες": "βεβαιότητα — certainty", "μεταφορική": "μεταφορικός — metaphorical"}
})

rnd = random.Random(147)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-147.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
