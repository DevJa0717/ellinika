# Source for library/listening/listening-260.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l260.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l260-news-plota-fotovoltaika", "title": "Φωτοβολταϊκά πάνελ επιπλέουν σε έναν ταμιευτήρα της Θεσσαλίας", "title_en": "Solar panels float on a reservoir in Thessaly", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο μεσημεριανό δελτίο ενός περιφερειακού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Σε λειτουργία μπήκε χθες ένα πλωτό φωτοβολταϊκό πάρκο σε έναν ταμιευτήρα άρδευσης της Θεσσαλίας. Περίπου τρεις χιλιάδες πάνελ στηρίζονται σε πλωτήρες και καλύπτουν ένα μικρό μέρος της επιφάνειας του νερού.", "A floating solar park went into operation yesterday on an irrigation reservoir in Thessaly. About three thousand panels rest on floats and cover a small part of the water's surface."),
  L("Εκφωνητής", "m", "Το έργο ανήκει στον αγροτικό συνεταιρισμό της περιοχής. Το ρεύμα που παράγει θα κινεί τις αντλίες που ποτίζουν τα χωράφια το καλοκαίρι, ώστε να μειωθεί το κόστος της άρδευσης για τους αγρότες.", "The project belongs to the local farmers' cooperative. The electricity it produces will power the pumps that water the fields in summer, so as to reduce the cost of irrigation for the farmers."),
  L("Εκφωνητής", "m", "Σύμφωνα με τους μηχανικούς, τα πλωτά πάνελ έχουν δύο πλεονεκτήματα: το νερό τα δροσίζει, οπότε αποδίδουν περισσότερο τις ζεστές μέρες, και η σκιά τους περιορίζει την εξάτμιση του νερού του ταμιευτήρα.", "According to the engineers, floating panels have two advantages: the water cools them, so they perform better on hot days, and their shade limits the evaporation of the reservoir's water."),
  L("Εκφωνητής", "m", "Επιφυλάξεις έχει εκφράσει ένας τοπικός περιβαλλοντικός σύλλογος, που ζητά να παρακολουθείται η επίδραση του έργου στα πουλιά και στα ψάρια. Ο συνεταιρισμός απάντησε ότι θα δημοσιεύει κάθε χρόνο τα αποτελέσματα των μετρήσεων.", "A local environmental group has expressed reservations and is asking for the project's effect on birds and fish to be monitored. The cooperative replied that it will publish the results of the measurements every year."),
 ],
 "questions": [
  Q("Σε ποιον ανήκει το έργο;", ["Στον δήμο", "Σε μια ξένη εταιρεία", "Στον αγροτικό συνεταιρισμό της περιοχής", "Στο κράτος"], 2, "Το έργο ανήκει στον αγροτικό συνεταιρισμό της περιοχής"),
  Q("Για ποιο σκοπό θα χρησιμοποιηθεί κυρίως το ρεύμα;", ["Για να φωτίζονται τα χωριά", "Για να κινούνται οι αντλίες της άρδευσης", "Για να πουληθεί στην πόλη", "Για τα ψυγεία των αγροτών"], 1, "θα κινεί τις αντλίες που ποτίζουν τα χωράφια"),
  Q("Ποιο πλεονέκτημα των πλωτών πάνελ αναφέρουν οι μηχανικοί;", ["Κοστίζουν λιγότερο από τα άλλα", "Η σκιά τους περιορίζει την εξάτμιση", "Δεν χρειάζονται καθάρισμα", "Δουλεύουν και τη νύχτα"], 1, "η σκιά τους περιορίζει την εξάτμιση του νερού"),
  Q("Τι ζητά ο περιβαλλοντικός σύλλογος;", ["Να σταματήσει το έργο", "Να μεταφερθούν τα πάνελ", "Να παρακολουθείται η επίδραση στα πουλιά και στα ψάρια", "Να γίνει δημοψήφισμα"], 2, "ζητά να παρακολουθείται η επίδραση του έργου στα πουλιά και στα ψάρια"),
 ],
 "gloss": {"πλωτό": "πλωτός — floating", "φωτοβολταϊκό": "φωτοβολταϊκός — photovoltaic, solar", "ταμιευτήρα": "ταμιευτήρας — reservoir", "άρδευσης": "άρδευση — irrigation", "πλωτήρες": "πλωτήρας — float", "συνεταιρισμό": "συνεταιρισμός — cooperative", "αντλίες": "αντλία — pump", "αποδίδουν": "αποδίδω — to perform, yield", "εξάτμιση": "εξάτμιση — evaporation", "Επιφυλάξεις": "επιφύλαξη — reservation, doubt"}
})

ITEMS.append({
 "id": "l260-vm-potisma-fyton", "title": "Μήνυμα από τη φίλη που θα ποτίζει τα φυτά σας", "title_en": "A message from the friend who will water your plants", "type": "voicemail", "level": "B2",
 "context_el": "Λείπετε για δύο εβδομάδες και μια φίλη σας προσφέρθηκε να σας ποτίζει τα φυτά. Ακούτε ένα μήνυμα που σας άφησε στον τηλεφωνητή.",
 "script": [
  L("Νεφέλη", "f", "Γεια σου, η Νεφέλη είμαι! Πήρα τα κλειδιά από τη θυρωρό, όλα εντάξει. Πέρασα σήμερα το απόγευμα και πότισα τα φυτά του μπαλκονιού. Σκέφτομαι να έρχομαι Δευτέρα, Τετάρτη και Παρασκευή, εκτός αν μου πεις ότι η λεμονιά θέλει νερό κάθε μέρα με αυτή τη ζέστη.", "Hi, it's Nefeli! I got the keys from the concierge, all fine. I came by this afternoon and watered the plants on the balcony. I'm thinking of coming on Monday, Wednesday and Friday, unless you tell me the lemon tree needs water every day in this heat."),
  L("Νεφέλη", "f", "Για την ορχιδέα στο σαλόνι, μου είχες πει να της βάζω μόνο δύο παγάκια την εβδομάδα και όχι νερό. Το κάνω, αλλά ομολογώ ότι μου φαίνεται λίγο παράξενο, οπότε αν έκανα λάθος και εννοούσες κάτι άλλο, στείλε μου ένα μήνυμα.", "As for the orchid in the living room, you told me to give it just two ice cubes a week and no water. I'm doing that, but I admit it seems a bit strange to me, so if I got it wrong and you meant something else, send me a message."),
  L("Νεφέλη", "f", "Δύο πράγματα ακόμη. Η μπαλκονόπορτα δεν κλειδώνει καλά, πρέπει να τη σπρώξεις δυνατά, αλλιώς μένει ανοιχτή. Την έκλεισα με προσοχή, αλλά καλό θα ήταν να το κοιτάξεις όταν γυρίσεις. Και τα γράμματα από το γραμματοκιβώτιο τα μαζεύω και τα αφήνω στο τραπέζι της κουζίνας.", "Two more things. The balcony door doesn't lock properly; you have to push it hard, otherwise it stays open. I closed it carefully, but it would be good for you to look at it when you're back. And I'm collecting the letters from the letterbox and leaving them on the kitchen table."),
  L("Νεφέλη", "f", "Α, και το πιο απρόσμενο: ένα περιστέρι έχει κάνει φωλιά στη μεγάλη γλάστρα με τον βασιλικό και κάθεται πάνω σε δύο αυγά! Δεν το πείραξα. Πες μου τι θέλεις να κάνω. Καλά να περνάς!", "Oh, and the most unexpected thing: a pigeon has made a nest in the big pot with the basil and is sitting on two eggs! I didn't disturb it. Tell me what you want me to do. Have a good time!"),
 ],
 "questions": [
  Q("Πόσο συχνά σκέφτεται να έρχεται η Νεφέλη;", ["Κάθε μέρα", "Τρεις φορές την εβδομάδα", "Μία φορά την εβδομάδα", "Μόνο τα Σαββατοκύριακα"], 1, "Σκέφτομαι να έρχομαι Δευτέρα, Τετάρτη και Παρασκευή"),
  Q("Τι της φαίνεται παράξενο;", ["Ότι η λεμονιά θέλει πολύ νερό", "Ότι η ορχιδέα παίρνει μόνο παγάκια", "Ότι τα φυτά είναι στο σαλόνι", "Ότι η θυρωρός είχε τα κλειδιά"], 1, "να της βάζω μόνο δύο παγάκια την εβδομάδα … μου φαίνεται λίγο παράξενο"),
  Q("Ποιο πρόβλημα υπάρχει με την μπαλκονόπορτα;", ["Είναι σπασμένο το τζάμι", "Δεν κλειδώνει καλά αν δεν τη σπρώξεις δυνατά", "Χάθηκε το κλειδί της", "Τρίζει πολύ"], 1, "δεν κλειδώνει καλά, πρέπει να τη σπρώξεις δυνατά"),
  Q("Τι βρήκε στη γλάστρα με τον βασιλικό;", ["Ένα σαλιγκάρι", "Μια γάτα που κοιμόταν", "Ένα περιστέρι πάνω σε αυγά", "Ένα ξεχασμένο κλειδί"], 2, "ένα περιστέρι έχει κάνει φωλιά … και κάθεται πάνω σε δύο αυγά"),
 ],
 "gloss": {"θυρωρό": "θυρωρός — concierge", "πότισα": "ποτίζω — to water", "λεμονιά": "λεμονιά — lemon tree", "ορχιδέα": "ορχιδέα — orchid", "παγάκια": "παγάκι — ice cube", "ομολογώ": "ομολογώ — to admit", "μπαλκονόπορτα": "μπαλκονόπορτα — balcony door", "γραμματοκιβώτιο": "γραμματοκιβώτιο — letterbox", "απρόσμενο": "απρόσμενος — unexpected", "φωλιά": "φωλιά — nest", "γλάστρα": "γλάστρα — flowerpot", "πείραξα": "πειράζω — to disturb, touch"}
})

ITEMS.append({
 "id": "l260-c1-mono-mikroskopio", "title": "Ένας κόσμος μέσα σε μια σταγόνα: η ιστορία του μικροσκοπίου", "title_en": "A world in a drop: the history of the microscope", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας ομιλίας σε έναν κύκλο εκδηλώσεων για την ιστορία της επιστήμης.",
 "script": [
  L("Ομιλήτρια", "f", "Τα πρώτα σύνθετα μικροσκόπια, με δύο φακούς σε έναν σωλήνα, εμφανίστηκαν στην Ολλανδία στα τέλη του δέκατου έκτου αιώνα, στα εργαστήρια κατασκευαστών γυαλιών οράσεως. Ποιος ακριβώς τα εφηύρε δεν το ξέρουμε με βεβαιότητα. Ξέρουμε όμως ποιος τους έδωσε το όνομά τους: το 1625 ένα μέλος μιας ιταλικής επιστημονικής ακαδημίας έπλασε από τα ελληνικά τη λέξη «μικροσκόπιο».", "The first compound microscopes, with two lenses in a tube, appeared in the Netherlands at the end of the sixteenth century, in the workshops of spectacle makers. Exactly who invented them we do not know for certain. But we do know who gave them their name: in 1625 a member of an Italian scientific academy coined the word 'microscope' from Greek."),
  L("Ομιλήτρια", "f", "Το 1665 ο Άγγλος Ρόμπερτ Χουκ δημοσίευσε ένα βιβλίο με εντυπωσιακά σχέδια από όσα είδε στο μικροσκόπιό του: το μάτι μιας μύγας, το κεντρί μιας μέλισσας, έναν ψύλλο σε τεράστιο μέγεθος. Κοιτάζοντας ένα λεπτό κομμάτι φελλού, είδε μικρούς χώρους που του θύμισαν τα κελιά των μοναχών, και τους ονόμασε cells, κελιά. Από εκεί προέρχεται ο όρος που στα ελληνικά αποδίδουμε ως «κύτταρο».", "In 1665 the Englishman Robert Hooke published a book with striking drawings of what he had seen through his microscope: a fly's eye, a bee's sting, a flea at enormous size. Looking at a thin slice of cork, he saw small spaces that reminded him of monks' cells, and called them cells. That is where the term comes from that in Greek we render as 'kyttaro'."),
  L("Ομιλήτρια", "f", "Η μεγαλύτερη έκπληξη ήρθε όμως από έναν ερασιτέχνη. Ο Αντόνι φαν Λέβενχουκ ήταν έμπορος υφασμάτων στο Ντελφτ και έφτιαχνε μόνος του μικροσκόπια με έναν μόνο, μικροσκοπικό φακό, που μεγέθυνε πάνω από διακόσιες φορές. Στη δεκαετία του 1670 είδε σε μια σταγόνα νερό από τη βροχή ζωντανά πλάσματα που κανείς δεν είχε φανταστεί, και τα ονόμασε «ζωάκια».", "But the greatest surprise came from an amateur. Antonie van Leeuwenhoek was a cloth merchant in Delft who made his own microscopes with a single, tiny lens that magnified more than two hundred times. In the 1670s he saw in a drop of rainwater living creatures no one had imagined, and called them 'little animals'."),
  L("Ομιλήτρια", "f", "Έστειλε δεκάδες επιστολές στη Βασιλική Εταιρεία του Λονδίνου, που στην αρχή δυσκολευόταν να τον πιστέψει. Σήμερα θεωρείται ο πρώτος άνθρωπος που είδε βακτήρια. Και ήταν ένας έμπορος που δεν είχε πάει ποτέ στο πανεπιστήμιο και δεν μιλούσε καμία άλλη γλώσσα εκτός από τα ολλανδικά.", "He sent dozens of letters to the Royal Society in London, which at first found it hard to believe him. Today he is considered the first person to have seen bacteria. And he was a merchant who had never been to university and spoke no language other than Dutch."),
 ],
 "questions": [
  Q("Πού εμφανίστηκαν τα πρώτα σύνθετα μικροσκόπια;", ["Σε πανεπιστήμια της Ιταλίας", "Σε εργαστήρια κατασκευαστών γυαλιών στην Ολλανδία", "Σε μοναστήρια της Αγγλίας", "Στη Βασιλική Εταιρεία"], 1, "στην Ολλανδία … στα εργαστήρια κατασκευαστών γυαλιών οράσεως"),
  Q("Γιατί ο Χουκ ονόμασε cells αυτό που είδε στον φελλό;", ["Γιατί έμοιαζαν με κελιά μοναχών", "Γιατί ήταν ζωντανά", "Γιατί έμοιαζαν με μέλισσες", "Γιατί ήταν πολύ σκληρά"], 0, "είδε μικρούς χώρους που του θύμισαν τα κελιά των μοναχών"),
  Q("Ποιος ήταν ο Λέβενχουκ;", ["Καθηγητής ιατρικής", "Έμπορος υφασμάτων και ερασιτέχνης", "Κατασκευαστής γυαλιών", "Μέλος της ιταλικής ακαδημίας"], 1, "ήταν έμπορος υφασμάτων στο Ντελφτ"),
  Q("Τι είδε ο Λέβενχουκ σε μια σταγόνα βρόχινο νερό;", ["Κρυστάλλους", "Ζωντανά πλάσματα", "Σκόνη", "Κύτταρα φυτών"], 1, "είδε … ζωντανά πλάσματα που κανείς δεν είχε φανταστεί"),
 ],
 "gloss": {"σύνθετα": "σύνθετος — compound", "φακούς": "φακός — lens", "οράσεως": "όραση — sight (γυαλιά οράσεως = spectacles)", "έπλασε": "πλάθω — to coin, shape", "κεντρί": "κεντρί — sting", "ψύλλο": "ψύλλος — flea", "φελλού": "φελλός — cork", "κελιά": "κελί — cell (of a monk)", "κύτταρο": "κύτταρο — cell (biology)", "ερασιτέχνη": "ερασιτέχνης — amateur", "μεγέθυνε": "μεγεθύνω — to magnify", "βακτήρια": "βακτήριο — bacterium"}
})

ITEMS.append({
 "id": "l260-c1-int-triiris", "title": "Ξαναφτιάχνοντας μια τριήρη: μια αρχαιολόγος για την πειραματική αρχαιολογία", "title_en": "Rebuilding a trireme: an archaeologist on experimental archaeology", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια εκπομπή του ραδιοφώνου για την αρχαιολογία.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι περισσότεροι φανταζόμαστε τους αρχαιολόγους να σκάβουν. Εσείς ασχολείστε με κάτι λιγότερο γνωστό, την πειραματική αρχαιολογία. Τι είναι;", "Most of us imagine archaeologists digging. You work on something less well known, experimental archaeology. What is it?"),
  L("Αρχαιολόγος", "f", "Είναι η προσπάθεια να ελέγξουμε τις θεωρίες μας στην πράξη. Δεν αρκεί να βρούμε ένα εργαλείο ή ένα κομμάτι από ένα πλοίο· θέλουμε να καταλάβουμε πώς φτιάχτηκε και πώς χρησιμοποιήθηκε. Γι’ αυτό το ξαναφτιάχνουμε, με τα υλικά και τις τεχνικές της εποχής όσο γίνεται, και το δοκιμάζουμε.", "It's the attempt to test our theories in practice. It's not enough to find a tool or a piece of a ship; we want to understand how it was made and how it was used. So we make it again, with the materials and techniques of the period as far as possible, and we test it."),
  L("Δημοσιογράφος", "m", "Το πιο φιλόδοξο τέτοιο πείραμα στην Ελλάδα ήταν η «Ολυμπιάς», σωστά;", "The most ambitious experiment of this kind in Greece was the 'Olympias', right?"),
  L("Αρχαιολόγος", "f", "Ναι. Η «Ολυμπιάς» είναι μια ανακατασκευή αθηναϊκής τριήρους, που ναυπηγήθηκε στον Πειραιά στα μέσα της δεκαετίας του 1980, σε συνεργασία Ελλήνων και Βρετανών ειδικών. Το πρόβλημα ήταν ότι δεν έχει βρεθεί ποτέ ναυάγιο τριήρους. Οι σχεδιαστές στηρίχτηκαν σε αρχαία κείμενα, σε αγγειογραφίες και στα ερείπια των νεωσοίκων όπου φυλάσσονταν τα πλοία.", "Yes. The Olympias is a reconstruction of an Athenian trireme, built in Piraeus in the mid-1980s, in cooperation between Greek and British specialists. The problem was that no trireme wreck has ever been found. The designers relied on ancient texts, vase paintings and the ruins of the ship sheds where the ships were kept."),
  L("Δημοσιογράφος", "m", "Και τι έμαθαν όταν την έβαλαν στη θάλασσα;", "And what did they learn when they put her to sea?"),
  L("Αρχαιολόγος", "f", "Πολλά. Με εκατόν εβδομήντα κωπηλάτες, εθελοντές τις περισσότερες φορές, το πλοίο έφτασε για λίγα λεπτά κοντά στους εννέα κόμβους. Είδαν όμως και πόσο δύσκολος ήταν ο συντονισμός σε τρεις σειρές κουπιών, και πόσο ζέστη έκανε στην κατώτερη σειρά. Κάποια αρχαία κείμενα, που μέχρι τότε έμοιαζαν υπερβολικά, ξαφνικά απέκτησαν νόημα. Αυτή είναι, για μένα, η μεγαλύτερη αξία ενός πειράματος: σε αναγκάζει να ξαναδιαβάσεις τις πηγές.", "A lot. With a hundred and seventy rowers, volunteers most of the time, the ship briefly reached nearly nine knots. But they also saw how difficult coordination was across three rows of oars, and how hot it was in the lowest row. Some ancient texts that had until then seemed exaggerated suddenly made sense. That, for me, is the greatest value of an experiment: it forces you to reread the sources."),
 ],
 "questions": [
  Q("Τι είναι, σύμφωνα με την αρχαιολόγο, η πειραματική αρχαιολογία;", ["Η ανασκαφή με νέα μηχανήματα", "Ο έλεγχος των θεωριών στην πράξη, με ανακατασκευές", "Η μελέτη των αρχαίων κειμένων", "Η προστασία των μνημείων"], 1, "Είναι η προσπάθεια να ελέγξουμε τις θεωρίες μας στην πράξη"),
  Q("Ποιο ήταν το βασικό πρόβλημα στον σχεδιασμό της «Ολυμπιάδας»;", ["Δεν υπήρχαν χρήματα", "Δεν έχει βρεθεί ποτέ ναυάγιο τριήρους", "Δεν υπήρχε κατάλληλο ξύλο", "Δεν βρίσκονταν κωπηλάτες"], 1, "δεν έχει βρεθεί ποτέ ναυάγιο τριήρους"),
  Q("Σε τι στηρίχτηκαν οι σχεδιαστές;", ["Σε ένα ναυάγιο στη Σικελία", "Σε αρχαία κείμενα, αγγειογραφίες και ερείπια νεωσοίκων", "Σε σχέδια του 19ου αιώνα", "Μόνο σε υπολογιστικά μοντέλα"], 1, "στηρίχτηκαν σε αρχαία κείμενα, σε αγγειογραφίες και στα ερείπια των νεωσοίκων"),
  Q("Ποια είναι, κατά την αρχαιολόγο, η μεγαλύτερη αξία ενός πειράματος;", ["Ότι προσελκύει τουρίστες", "Ότι σε αναγκάζει να ξαναδιαβάσεις τις πηγές", "Ότι αποδεικνύει πάντα τις θεωρίες", "Ότι είναι φτηνότερο από μια ανασκαφή"], 1, "σε αναγκάζει να ξαναδιαβάσεις τις πηγές"),
 ],
 "gloss": {"πειραματική": "πειραματικός — experimental", "ανακατασκευή": "ανακατασκευή — reconstruction", "τριήρους": "τριήρης — trireme", "ναυπηγήθηκε": "ναυπηγούμαι — to be built (of a ship)", "ναυάγιο": "ναυάγιο — shipwreck", "αγγειογραφίες": "αγγειογραφία — vase painting", "νεωσοίκων": "νεώσοικος — ship shed", "κωπηλάτες": "κωπηλάτης — rower", "κόμβους": "κόμβος — knot (unit of speed)", "συντονισμός": "συντονισμός — coordination", "κουπιών": "κουπί — oar"}
})

rnd = random.Random(260)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-260.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
