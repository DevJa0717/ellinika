# Source for library/listening/listening-188.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l188.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l188-ann-agries-orchidees", "title": "Περίπατος για τις άγριες ορχιδέες", "title_en": "A walk to see the wild orchids", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση ενός συλλόγου φίλων της φύσης στο τοπικό ραδιόφωνο, στις αρχές της άνοιξης.",
 "script": [
  L("Εκφωνητής", "m", "Ο σύλλογος φίλων του Υμηττού διοργανώνει την Κυριακή 23 Μαρτίου περίπατο για να δούμε τις άγριες ορχιδέες του βουνού, που ανθίζουν αυτές τις εβδομάδες. Θα μας συνοδεύει μια βοτανολόγος, η οποία θα μας εξηγήσει πώς ξεχωρίζουν τα διάφορα είδη.", "The Friends of Hymettus association is organising a walk on Sunday 23 March to see the mountain's wild orchids, which are blooming these weeks. We will be accompanied by a botanist, who will explain how to tell the different species apart."),
  L("Εκφωνητής", "m", "Η συνάντηση είναι στις εννιά το πρωί στην πύλη της Καισαριανής. Η διαδρομή είναι εύκολη, διαρκεί περίπου τρεις ώρες και είναι κατάλληλη και για παιδιά πάνω από οχτώ χρονών. Χρειάζεστε κλειστά παπούτσια, νερό και καπέλο.", "We meet at nine in the morning at the Kaisariani gate. The route is easy, lasts about three hours and is suitable for children over eight as well. You need closed shoes, water and a hat."),
  L("Εκφωνητής", "m", "Σας θυμίζουμε ότι οι άγριες ορχιδέες προστατεύονται: απαγορεύεται να τις κόβετε ή να τις ξεριζώνετε. Μπορείτε όμως να τις φωτογραφίζετε όσο θέλετε, αρκεί να μην πατάτε έξω από το μονοπάτι. Η συμμετοχή είναι δωρεάν, αλλά οι θέσεις είναι σαράντα, γι' αυτό χρειάζεται δήλωση στο τηλέφωνο του συλλόγου.", "We remind you that wild orchids are protected: it is forbidden to pick them or uproot them. You can, however, photograph them as much as you like, as long as you don't step off the path. Participation is free, but there are forty places, so you need to register by phone with the association."),
 ],
 "questions": [
  Q("Ποιος θα συνοδεύει τους συμμετέχοντες;", ["Ένας δασοφύλακας", "Μια βοτανολόγος", "Ένας φωτογράφος", "Ο δήμαρχος"], 1, "Θα μας συνοδεύει μια βοτανολόγος"),
  Q("Για ποιους είναι κατάλληλη η διαδρομή;", ["Μόνο για έμπειρους πεζοπόρους", "Μόνο για ενήλικες", "Και για παιδιά πάνω από οχτώ χρονών", "Για παιδιά κάθε ηλικίας"], 2, "είναι κατάλληλη και για παιδιά πάνω από οχτώ χρονών"),
  Q("Τι επιτρέπεται να κάνουν οι συμμετέχοντες με τις ορχιδέες;", ["Να κόψουν μία η καθεμία", "Να τις ξεριζώσουν για τον κήπο τους", "Να πατήσουν έξω από το μονοπάτι για να τις δουν", "Να τις φωτογραφίσουν"], 3, "Μπορείτε όμως να τις φωτογραφίζετε όσο θέλετε"),
 ],
 "gloss": {"ορχιδέες": "ορχιδέα — orchid", "βοτανολόγος": "βοτανολόγος — botanist", "ξεχωρίζουν": "ξεχωρίζω — to distinguish, tell apart", "ξεριζώνετε": "ξεριζώνω — to uproot", "προστατεύονται": "προστατεύομαι — to be protected", "αρκεί να": "αρκεί να — as long as"},
})

ITEMS.append({
 "id": "l188-int-odigos-vounou", "title": "Ένας οδηγός βουνού στον Όλυμπο", "title_en": "A mountain guide on Olympus", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν οδηγό βουνού που ανεβάζει ομάδες στον Όλυμπο.",
 "script": [
  L("Δημοσιογράφος", "f", "Πόσες φορές έχετε ανέβει στον Μύτικα, την ψηλότερη κορυφή του Ολύμπου;", "How many times have you climbed Mytikas, the highest peak of Olympus?"),
  L("Οδηγός", "m", "Έχω σταματήσει να μετράω· πάνω από τριακόσιες, σίγουρα. Κάθε καλοκαίρι ανεβαίνω σχεδόν κάθε εβδομάδα με μια ομάδα. Και κάθε φορά το βουνό είναι διαφορετικό, ανάλογα με τον καιρό και τους ανθρώπους.", "I've stopped counting; over three hundred, certainly. Every summer I go up almost every week with a group. And every time the mountain is different, depending on the weather and the people."),
  L("Δημοσιογράφος", "f", "Ποιο είναι το πιο συνηθισμένο λάθος των επισκεπτών;", "What is the most common mistake visitors make?"),
  L("Οδηγός", "m", "Υποτιμούν το βουνό επειδή είναι στην Ελλάδα. Έρχονται με αθλητικά παπούτσια και ένα μπουκαλάκι νερό, λες και πάνε για μπάνιο. Στην κορυφή όμως η θερμοκρασία μπορεί να πέσει κοντά στο μηδέν ακόμα και τον Ιούλιο, και μια καταιγίδα έρχεται μέσα σε μισή ώρα.", "They underestimate the mountain because it's in Greece. They come in trainers with a little bottle of water, as if they were going for a swim. At the top, though, the temperature can drop close to zero even in July, and a storm can arrive within half an hour."),
  L("Δημοσιογράφος", "f", "Έχετε γυρίσει ποτέ πίσω χωρίς να φτάσετε στην κορυφή;", "Have you ever turned back without reaching the summit?"),
  L("Οδηγός", "m", "Πολλές φορές, και δεν το μετανιώνω. Οι πελάτες στεναχωριούνται, αλλά εγώ τους λέω ότι η κορυφή δεν φεύγει· θα είναι εκεί και του χρόνου. Η δουλειά μου δεν είναι να τους ανεβάσω, αλλά να τους κατεβάσω.", "Many times, and I don't regret it. The clients get upset, but I tell them the summit isn't going anywhere; it will be there next year too. My job isn't to get them up, but to get them down."),
 ],
 "questions": [
  Q("Πόσο συχνά ανεβαίνει ο οδηγός στον Όλυμπο το καλοκαίρι;", ["Μία φορά τον μήνα", "Σχεδόν κάθε εβδομάδα", "Κάθε μέρα", "Μόνο τον Αύγουστο"], 1, "Κάθε καλοκαίρι ανεβαίνω σχεδόν κάθε εβδομάδα με μια ομάδα"),
  Q("Ποιο είναι, κατά τον οδηγό, το πιο συνηθισμένο λάθος;", ["Ξεκινούν πολύ αργά το πρωί", "Δεν τρώνε αρκετά", "Υποτιμούν το βουνό και έρχονται απροετοίμαστοι", "Δεν ακούνε τον οδηγό"], 2, "Υποτιμούν το βουνό επειδή είναι στην Ελλάδα"),
  Q("Τι λέει για τις φορές που γύρισαν πίσω;", ["Ότι δεν το μετανιώνει", "Ότι ντρέπεται ακόμα", "Ότι συμβαίνει μόνο με αρχάριους", "Ότι επιστρέφει τα χρήματα"], 0, "Πολλές φορές, και δεν το μετανιώνω"),
 ],
 "gloss": {"Μύτικα": "Μύτικας — Mytikas, the highest peak of Olympus", "Υποτιμούν": "υποτιμώ — to underestimate", "καταιγίδα": "καταιγίδα — storm", "μετανιώνω": "μετανιώνω — to regret", "στεναχωριούνται": "στεναχωριέμαι — to be upset", "λες και": "λες και — as if"},
})

ITEMS.append({
 "id": "l188-vm-portokalia-apo-ton-paragogo", "title": "Τα πορτοκάλια θα αργήσουν λίγο", "title_en": "The oranges will be a little late", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε παραγγείλει πορτοκάλια απευθείας από έναν παραγωγό της Αργολίδας. Ακούτε ένα μήνυμα που σας άφησε στον τηλεφωνητή.",
 "script": [
  L("Παραγωγός", "m", "Καλησπέρα, ο Θοδωρής είμαι, από το κτήμα στο Άργος, για την παραγγελία σας με τα είκοσι κιλά πορτοκάλια. Λυπάμαι, αλλά θα αργήσουμε μία εβδομάδα. Την Κυριακή έπεσε χαλάζι στην περιοχή και χρειάστηκε να σταματήσουμε το μάζεμα για μερικές μέρες.", "Good evening, it's Thodoris, from the farm in Argos, about your order of twenty kilos of oranges. I'm sorry, but we'll be a week late. On Sunday hail fell in the area and we had to stop picking for a few days."),
  L("Παραγωγός", "m", "Τα περισσότερα πορτοκάλια είναι μια χαρά. Μερικά όμως έχουν μικρά σημάδια στη φλούδα από το χαλάζι. Μέσα είναι το ίδιο ζουμερά και γλυκά, απλώς δεν είναι τόσο όμορφα. Αν δεν σας πειράζει να πάρετε και τέτοια, θα σας κάνω έκπτωση τριάντα τοις εκατό σε όλη την παραγγελία.", "Most of the oranges are fine. Some, though, have small marks on the peel from the hail. Inside they are just as juicy and sweet, they just aren't as pretty. If you don't mind taking some of those too, I'll give you a thirty per cent discount on the whole order."),
  L("Παραγωγός", "m", "Αν πάλι τα θέλετε όλα χωρίς σημάδια, κανένα πρόβλημα, αλλά τότε θα περιμένετε άλλες δέκα μέρες. Στείλτε μου ένα μήνυμα μέχρι την Πέμπτη να ξέρω τι να βάλω στο κιβώτιο. Ευχαριστώ για την υπομονή!", "If, on the other hand, you want them all without marks, no problem, but then you'll wait another ten days. Send me a message by Thursday so I know what to put in the crate. Thanks for your patience!"),
 ],
 "questions": [
  Q("Γιατί θα αργήσει η παραγγελία;", ["Γιατί χάλασε το φορτηγό", "Γιατί έπεσε χαλάζι και σταμάτησε το μάζεμα", "Γιατί ο παραγωγός ήταν άρρωστος", "Γιατί είχε απεργία η εταιρεία μεταφορών"], 1, "Την Κυριακή έπεσε χαλάζι στην περιοχή και χρειάστηκε να σταματήσουμε το μάζεμα"),
  Q("Τι ισχύει για τα πορτοκάλια με σημάδια;", ["Είναι λιγότερο γλυκά", "Δεν τρώγονται", "Είναι το ίδιο ζουμερά και γλυκά μέσα", "Είναι μόνο για χυμό"], 2, "Μέσα είναι το ίδιο ζουμερά και γλυκά"),
  Q("Τι πρέπει να κάνει ο πελάτης μέχρι την Πέμπτη;", ["Να στείλει μήνυμα για το τι θέλει στο κιβώτιο", "Να πληρώσει την παραγγελία", "Να πάει στο κτήμα", "Να ακυρώσει την παραγγελία"], 0, "Στείλτε μου ένα μήνυμα μέχρι την Πέμπτη να ξέρω τι να βάλω στο κιβώτιο"),
 ],
 "gloss": {"παραγωγό": "παραγωγός — producer, grower", "χαλάζι": "χαλάζι — hail", "φλούδα": "φλούδα — peel", "ζουμερά": "ζουμερός — juicy", "κιβώτιο": "κιβώτιο — crate, box", "υπομονή": "υπομονή — patience"},
})

ITEMS.append({
 "id": "l188-mon-naftikoi-kompoi", "title": "Οι κόμποι του πατέρα μου", "title_en": "My father's knots", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλά σε μια ραδιοφωνική εκπομπή για κάτι που της έμαθε ο πατέρας της.",
 "script": [
  L("Γυναίκα", "f", "Ο πατέρας μου ήταν ψαράς στην Κάλυμνο, και το πρώτο πράγμα που μου έμαθε, πριν ακόμα μάθω να κολυμπάω, ήταν να δένω κόμπους. Μου έλεγε ότι ένας καλός κόμπος πρέπει να κάνει δύο πράγματα: να κρατάει όσο χρειάζεται και να λύνεται εύκολα όταν δεν χρειάζεται πια.", "My father was a fisherman on Kalymnos, and the first thing he taught me, before I had even learned to swim, was to tie knots. He used to tell me that a good knot must do two things: hold for as long as needed and come undone easily when it is no longer needed."),
  L("Γυναίκα", "f", "Σήμερα δουλεύω σε γραφείο και δεν έχω βάρκα, αλλά χρησιμοποιώ αυτούς τους κόμπους σχεδόν κάθε εβδομάδα. Δένω τις ντομάτες στο μπαλκόνι, δένω τις βαλίτσες στη σχάρα του αυτοκινήτου, κρεμάω την αιώρα στο χωριό. Οι φίλοι μου με φωνάζουν κάθε φορά που μετακομίζουν.", "Today I work in an office and don't have a boat, but I use these knots almost every week. I tie up the tomatoes on the balcony, I tie the suitcases onto the car's roof rack, I hang the hammock in the village. My friends call me every time they move house."),
  L("Γυναίκα", "f", "Τα τελευταία χρόνια διδάσκω κόμπους στους προσκόπους της γειτονιάς. Τα παιδιά στην αρχή βαριούνται, αλλά όταν καταφέρνουν να δέσουν τον πρώτο τους κόμπο με κλειστά μάτια, όπως μου έμαθε κι εμένα ο πατέρας μου, λάμπουν από περηφάνια.", "In recent years I've been teaching knots to the neighbourhood scouts. The children get bored at first, but when they manage to tie their first knot with their eyes closed, the way my father taught me too, they glow with pride."),
 ],
 "questions": [
  Q("Τι πρέπει να κάνει ένας καλός κόμπος, σύμφωνα με τον πατέρα της;", ["Να είναι όμορφος", "Να κρατάει όσο χρειάζεται και να λύνεται εύκολα", "Να μη λύνεται ποτέ", "Να δένεται γρήγορα"], 1, "να κρατάει όσο χρειάζεται και να λύνεται εύκολα όταν δεν χρειάζεται πια"),
  Q("Πού χρησιμοποιεί σήμερα τους κόμπους;", ["Μόνο στη βάρκα της", "Στη δουλειά της στο γραφείο", "Σε καθημερινές δουλειές, όπως στις ντομάτες και στις βαλίτσες", "Μόνο στις διακοπές"], 2, "Δένω τις ντομάτες στο μπαλκόνι"),
  Q("Πότε νιώθουν περήφανα τα παιδιά;", ["Όταν κερδίζουν σε αγώνα", "Όταν βγαίνουν με βάρκα", "Όταν παίρνουν δίπλωμα", "Όταν δένουν τον πρώτο τους κόμπο με κλειστά μάτια"], 3, "όταν καταφέρνουν να δέσουν τον πρώτο τους κόμπο με κλειστά μάτια"),
 ],
 "gloss": {"κόμπους": "κόμπος — knot", "λύνεται": "λύνομαι — to come undone", "σχάρα": "σχάρα — roof rack", "αιώρα": "αιώρα — hammock", "προσκόπους": "πρόσκοπος — scout", "περηφάνια": "περηφάνια — pride"},
})

ITEMS.append({
 "id": "l188-dia-skylos-tou-geitona", "title": "Θα κρατήσουμε τον σκύλο του γείτονα;", "title_en": "Shall we look after the neighbour's dog?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά αν θα φιλοξενήσουν τον σκύλο του γείτονά τους για μια εβδομάδα.",
 "script": [
  L("Γιώργος", "m", "Ο κύριος Παύλος από τον τρίτο με ρώτησε αν μπορούμε να κρατήσουμε τον Μπόμπο για μια εβδομάδα. Πρέπει να μπει στο νοσοκομείο για μια εγχείρηση και δεν έχει σε ποιον να τον αφήσει.", "Mr Pavlos from the third floor asked me whether we can keep Bobos for a week. He has to go into hospital for an operation and has no one to leave him with."),
  L("Δάφνη", "f", "Τον καημένο. Αλλά ο Μπόμπος είναι τεράστιος, και το διαμέρισμά μας είναι μικρό. Και ποιος θα τον βγάζει βόλτα το μεσημέρι; Εμείς δουλεύουμε και οι δύο ως τις πέντε.", "Poor man. But Bobos is huge, and our flat is small. And who will take him for a walk at midday? We both work until five."),
  L("Γιώργος", "m", "Το σκέφτηκα. Η κόρη της κυρίας Ρένας κάνει βόλτες σε σκύλους για χαρτζιλίκι. Θα της δώσουμε κλειδί και θα τον βγάζει στη μία. Ο κύριος Παύλος είπε ότι θα την πληρώσει εκείνος.", "I've thought about it. Mrs Rena's daughter walks dogs for pocket money. We'll give her a key and she'll take him out at one. Mr Pavlos said he'll pay her himself."),
  L("Δάφνη", "f", "Και η γάτα μας; Η Μέλι δεν έχει δει ποτέ σκύλο από κοντά. Θα κρυφτεί κάτω από το κρεβάτι για μια εβδομάδα.", "And our cat? Meli has never seen a dog up close. She'll hide under the bed for a week."),
  L("Γιώργος", "m", "Ο Μπόμπος μεγάλωσε με γάτες, μου το είπε ο ίδιος. Ας τον φέρουμε πρώτα ένα απόγευμα να γνωριστούν. Αν δεν πάει καλά, θα βρούμε κάτι άλλο.", "Bobos grew up with cats, he told me himself. Let's bring him over for an afternoon first so they can meet. If it doesn't go well, we'll find something else."),
 ],
 "questions": [
  Q("Γιατί χρειάζεται ο γείτονας κάποιον να κρατήσει τον σκύλο;", ["Θα πάει διακοπές", "Θα μπει στο νοσοκομείο για εγχείρηση", "Μετακομίζει", "Ξεκινά καινούργια δουλειά"], 1, "Πρέπει να μπει στο νοσοκομείο για μια εγχείρηση"),
  Q("Ποια λύση προτείνει ο Γιώργος για τη βόλτα του μεσημεριού;", ["Θα γυρίζει ο ίδιος από τη δουλειά", "Θα πάρει άδεια", "Η κόρη μιας γειτόνισσας θα βγάζει τον σκύλο", "Θα τον αφήνουν στην αυλή"], 2, "Η κόρη της κυρίας Ρένας κάνει βόλτες σε σκύλους για χαρτζιλίκι"),
  Q("Τι προτείνει τελικά ο Γιώργος;", ["Να πουν όχι στον γείτονα", "Να δώσουν τη γάτα σε φίλους", "Να πάρουν μεγαλύτερο σπίτι", "Να φέρουν πρώτα τον σκύλο ένα απόγευμα να γνωριστεί με τη γάτα"], 3, "Ας τον φέρουμε πρώτα ένα απόγευμα να γνωριστούν"),
 ],
 "gloss": {"εγχείρηση": "εγχείρηση — operation, surgery", "καημένο": "καημένος — poor (pitied)", "χαρτζιλίκι": "χαρτζιλίκι — pocket money", "κρυφτεί": "κρύβομαι — to hide", "γνωριστούν": "γνωρίζομαι — to get to know each other"},
})

ITEMS.append({
 "id": "l188-news-klopi-melission", "title": "Κλοπή μελισσιών στη Χαλκιδική", "title_en": "Beehives stolen in Halkidiki", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο περιφερειακό δελτίο ειδήσεων.",
 "script": [
  L("Παρουσιάστρια", "f", "Εξήντα μελίσσια εξαφανίστηκαν μέσα σε μία νύχτα από ένα μελισσοκομείο κοντά στον Πολύγυρο. Ο ιδιοκτήτης τους, ένας μελισσοκόμος σαράντα δύο χρονών, κατήγγειλε την κλοπή στην αστυνομία το πρωί της Τρίτης, όταν πήγε να ελέγξει τις κυψέλες του.", "Sixty beehives disappeared in a single night from an apiary near Polygyros. Their owner, a forty-two-year-old beekeeper, reported the theft to the police on Tuesday morning, when he went to check his hives."),
  L("Παρουσιάστρια", "f", "Σύμφωνα με τον μελισσοκομικό σύλλογο της περιοχής, είναι η τρίτη τέτοια κλοπή από την αρχή της χρονιάς. Οι κλέφτες, όπως λένε οι μελισσοκόμοι, ξέρουν τη δουλειά: μετακινούν τις κυψέλες τη νύχτα, όταν οι μέλισσες είναι όλες μέσα, και τις φορτώνουν σε φορτηγό.", "According to the area's beekeepers' association, it is the third such theft since the start of the year. The thieves, the beekeepers say, know the trade: they move the hives at night, when all the bees are inside, and load them onto a truck."),
  L("Παρουσιάστρια", "f", "Ο σύλλογος ζητά από τα μέλη του να σημαδεύουν τις κυψέλες με τον αριθμό μητρώου τους και εξετάζει την τοποθέτηση μικρών συσκευών εντοπισμού. Η ζημιά για τον μελισσοκόμο υπολογίζεται σε περίπου δεκαπέντε χιλιάδες ευρώ.", "The association is asking its members to mark their hives with their registration number and is considering fitting small tracking devices. The beekeeper's loss is estimated at about fifteen thousand euros."),
 ],
 "questions": [
  Q("Πότε κατάλαβε ο μελισσοκόμος την κλοπή;", ["Την Τρίτη το πρωί, όταν πήγε να ελέγξει τις κυψέλες", "Το βράδυ της Δευτέρας", "Όταν του τηλεφώνησε η αστυνομία", "Μετά από μια εβδομάδα"], 0, "όταν πήγε να ελέγξει τις κυψέλες του"),
  Q("Γιατί οι κλέφτες μετακινούν τις κυψέλες τη νύχτα;", ["Γιατί κάνει λιγότερη ζέστη", "Γιατί τότε οι μέλισσες είναι όλες μέσα", "Γιατί δεν υπάρχει αστυνομία", "Γιατί οι μέλισσες κοιμούνται βαθιά"], 1, "όταν οι μέλισσες είναι όλες μέσα"),
  Q("Τι εξετάζει ο σύλλογος;", ["Να προσλάβει φύλακες", "Να μεταφέρει τα μελίσσια σε άλλο νομό", "Να τοποθετήσει μικρές συσκευές εντοπισμού", "Να ασφαλίσει όλα τα μελίσσια"], 2, "εξετάζει την τοποθέτηση μικρών συσκευών εντοπισμού"),
 ],
 "gloss": {"μελίσσια": "μελίσσι — beehive (colony)", "μελισσοκομείο": "μελισσοκομείο — apiary", "κατήγγειλε": "καταγγέλλω — to report (a crime)", "κυψέλες": "κυψέλη — hive", "μητρώου": "μητρώο — register", "εντοπισμού": "εντοπισμός — tracking, locating"},
})

ITEMS.append({
 "id": "l188-rep-archaia-sous-delfous", "title": "Αρχαία ελληνικά για ενήλικες στους Δελφούς", "title_en": "Ancient Greek for adults at Delphi", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα θερινό σχολείο αρχαίων ελληνικών.",
 "script": [
  L("Ρεπόρτερ", "m", "Είναι επτά το πρωί και, σε μια αίθουσα με θέα στον κόλπο της Ιτέας, είκοσι πέντε ενήλικες από δώδεκα χώρες διαβάζουν δυνατά Όμηρο. Βρισκόμαστε σε ένα θερινό σχολείο αρχαίων ελληνικών στους Δελφούς, που διαρκεί τρεις εβδομάδες.", "It's seven in the morning and, in a room overlooking the Gulf of Itea, twenty-five adults from twelve countries are reading Homer aloud. We are at a summer school of Ancient Greek at Delphi, which lasts three weeks."),
  L("Ρεπόρτερ", "m", "Οι μαθητές είναι κάθε ηλικίας: φοιτητές, συνταξιούχοι δάσκαλοι, ένας γιατρός από τη Βραζιλία. Τα μαθήματα γίνονται το πρωί, γιατί το απόγευμα η ζέστη είναι αφόρητη. Το βράδυ, όσοι θέλουν, διαβάζουν μαζί αποσπάσματα από τραγωδίες στο αρχαίο στάδιο.", "The students are of all ages: university students, retired teachers, a doctor from Brazil. Lessons are in the morning, because in the afternoon the heat is unbearable. In the evening, whoever wants to reads passages from tragedies together at the ancient stadium."),
  L("Ρεπόρτερ", "m", "Οι διοργανωτές λένε ότι πολλοί μαθητές έρχονται για τα αρχαία και φεύγουν μαθαίνοντας και νέα ελληνικά, από τις κουβέντες στο καφενείο και στον φούρνο. Μια Ιαπωνέζα μάς λέει γελώντας ότι μπορεί να διαβάσει την Ιλιάδα, αλλά δυσκολεύεται ακόμα να παραγγείλει έναν φραπέ.", "The organisers say that many students come for Ancient Greek and leave having learned Modern Greek too, from chats at the café and at the bakery. A Japanese woman tells us laughing that she can read the Iliad but still struggles to order a frappé."),
 ],
 "questions": [
  Q("Γιατί τα μαθήματα γίνονται το πρωί;", ["Γιατί το απόγευμα οι μαθητές κάνουν εκδρομές", "Γιατί το απόγευμα η ζέστη είναι αφόρητη", "Γιατί οι καθηγητές δουλεύουν αλλού", "Γιατί η αίθουσα κλείνει το μεσημέρι"], 1, "γιατί το απόγευμα η ζέστη είναι αφόρητη"),
  Q("Τι κάνουν μερικοί μαθητές το βράδυ;", ["Βλέπουν παραστάσεις στην Αθήνα", "Μαθαίνουν παραδοσιακούς χορούς", "Διαβάζουν αποσπάσματα από τραγωδίες στο αρχαίο στάδιο", "Κάνουν πρόβες για μια παράσταση"], 2, "διαβάζουν μαζί αποσπάσματα από τραγωδίες στο αρχαίο στάδιο"),
  Q("Τι λέει η Ιαπωνέζα μαθήτρια;", ["Ότι θέλει να μείνει στους Δελφούς", "Ότι τα νέα ελληνικά είναι πιο εύκολα", "Ότι δεν της αρέσει ο Όμηρος", "Ότι διαβάζει την Ιλιάδα, αλλά δυσκολεύεται να παραγγείλει φραπέ"], 3, "μπορεί να διαβάσει την Ιλιάδα, αλλά δυσκολεύεται ακόμα να παραγγείλει έναν φραπέ"),
 ],
 "gloss": {"κόλπο": "κόλπος — gulf, bay", "αφόρητη": "αφόρητος — unbearable", "αποσπάσματα": "απόσπασμα — passage, extract", "τραγωδίες": "τραγωδία — tragedy", "διοργανωτές": "διοργανωτής — organiser"},
})

ITEMS.append({
 "id": "l188-c1-akoustikos-michanikos", "title": "Ο μηχανικός που σχεδιάζει τον ήχο των αιθουσών", "title_en": "The engineer who designs how halls sound", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν μηχανικό ακουστικής που σχεδιάζει αίθουσες συναυλιών.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι σημαίνει ότι μια αίθουσα συναυλιών έχει «καλή ακουστική»;", "What does it mean that a concert hall has \"good acoustics\"?"),
  L("Μηχανικός", "m", "Πρώτα απ' όλα, ότι ο ήχος δεν σβήνει ούτε πολύ γρήγορα ούτε πολύ αργά. Αυτό το μετράμε με τον χρόνο αντήχησης. Για μια συμφωνική ορχήστρα θέλουμε γύρω στα δύο δευτερόλεπτα· για μια αίθουσα όπου κυρίως μιλάμε, πολύ λιγότερο, αλλιώς οι λέξεις μπερδεύονται μεταξύ τους.", "First of all, that the sound dies away neither too quickly nor too slowly. We measure this with the reverberation time. For a symphony orchestra we want around two seconds; for a hall where mostly speech happens, much less, otherwise the words blur into each other."),
  L("Δημοσιογράφος", "f", "Γιατί πολλές από τις πιο φημισμένες αίθουσες έχουν σχήμα κουτιού παπουτσιών;", "Why do many of the most famous halls have a shoebox shape?"),
  L("Μηχανικός", "m", "Επειδή στις στενές, ψηλές αίθουσες ο ήχος ανακλάται από τους πλαϊνούς τοίχους και φτάνει στον ακροατή και από τα δύο αυτιά, ελαφρώς διαφορετικός. Αυτό μας δίνει την αίσθηση ότι η μουσική μάς τυλίγει. Οι παλιοί αρχιτέκτονες το πέτυχαν σε μεγάλο βαθμό εμπειρικά, χωρίς υπολογιστές.", "Because in narrow, tall halls the sound reflects off the side walls and reaches the listener at both ears, slightly different. That gives us the sense that the music envelops us. The old architects largely achieved this empirically, without computers."),
  L("Δημοσιογράφος", "f", "Και ποιο είναι το πιο συχνό πρόβλημα που σας καλούν να λύσετε;", "And what is the most common problem you are called in to solve?"),
  L("Μηχανικός", "m", "Αίθουσες που σχεδιάστηκαν πρώτα για να είναι όμορφες στη φωτογραφία. Γυαλί, μάρμαρο, τέλεια λείες επιφάνειες. Ο ήχος χτυπά πάνω τους σαν μπάλα και δημιουργεί ηχώ. Η λύση είναι συνήθως να «σπάσουμε» τις επιφάνειες με ανάγλυφα ή καμπύλα πάνελ, ώστε ο ήχος να διαχέεται προς όλες τις κατευθύνσεις.", "Halls that were designed first to look beautiful in photographs. Glass, marble, perfectly smooth surfaces. The sound hits them like a ball and creates echoes. The solution is usually to \"break up\" the surfaces with relief or curved panels, so the sound is diffused in all directions."),
 ],
 "questions": [
  Q("Πόσος χρόνος αντήχησης είναι κατάλληλος για μια συμφωνική ορχήστρα, σύμφωνα με τον μηχανικό;", ["Γύρω στα δύο δευτερόλεπτα", "Μισό δευτερόλεπτο", "Πέντε δευτερόλεπτα", "Όσο το δυνατόν λιγότερος"], 0, "Για μια συμφωνική ορχήστρα θέλουμε γύρω στα δύο δευτερόλεπτα"),
  Q("Γιατί πετυχαίνουν οι αίθουσες σε σχήμα κουτιού παπουτσιών;", ["Γιατί χωράνε περισσότερους θεατές", "Γιατί είναι πιο φτηνές", "Γιατί ο ήχος ανακλάται από τους πλαϊνούς τοίχους και μας τυλίγει", "Γιατί η ορχήστρα κάθεται πιο ψηλά"], 2, "ο ήχος ανακλάται από τους πλαϊνούς τοίχους"),
  Q("Ποια είναι συνήθως η λύση για αίθουσες με λείες επιφάνειες;", ["Να γκρεμιστούν και να ξαναχτιστούν", "Να μπουν μικρόφωνα", "Να βαφτούν οι τοίχοι", "Να «σπάσουν» οι επιφάνειες με ανάγλυφα ή καμπύλα πάνελ"], 3, "να «σπάσουμε» τις επιφάνειες με ανάγλυφα ή καμπύλα πάνελ"),
 ],
 "gloss": {"ακουστικής": "ακουστική — acoustics", "αντήχησης": "αντήχηση — reverberation", "ανακλάται": "ανακλώμαι — to be reflected", "εμπειρικά": "εμπειρικά — empirically", "ηχώ": "ηχώ — echo", "ανάγλυφα": "ανάγλυφος — in relief, textured", "διαχέεται": "διαχέομαι — to be diffused"},
})

ITEMS.append({
 "id": "l188-c1-giati-anatrichiazoume-me-tin-kimolia", "title": "Γιατί δεν αντέχουμε το τρίξιμο στον πίνακα", "title_en": "Why we can't stand a squeak on the blackboard", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια επιστημονική εκπομπή στο ραδιόφωνο που εξηγεί ένα καθημερινό φαινόμενο.",
 "script": [
  L("Παρουσιαστής", "m", "Τα νύχια πάνω σε έναν μαυροπίνακα, ένα πιρούνι που γλιστράει στο πιάτο, η κιμωλία που τρίζει: λίγοι ήχοι μάς προκαλούν τόσο έντονη αποστροφή. Δεν είναι καν δυνατοί ήχοι. Γιατί λοιπόν μας ενοχλούν τόσο;", "Fingernails on a blackboard, a fork sliding on a plate, squeaking chalk: few sounds cause us such intense revulsion. They aren't even loud sounds. So why do they bother us so much?"),
  L("Παρουσιαστής", "m", "Μια εξήγηση που προτείνουν οι ερευνητές έχει να κάνει με το σχήμα του αυτιού μας. Ο ακουστικός πόρος φαίνεται να ενισχύει ιδιαίτερα τις συχνότητες ανάμεσα στα δύο και στα τέσσερα χιλιάδες χερτζ, και αυτοί οι ήχοι έχουν πολλή ενέργεια ακριβώς σε αυτή την περιοχή. Σε πειράματα, όταν οι ερευνητές αφαιρούσαν αυτές τις συχνότητες, οι συμμετέχοντες έβρισκαν τον ήχο πολύ λιγότερο δυσάρεστο.", "One explanation researchers suggest has to do with the shape of our ear. The ear canal seems to particularly amplify frequencies between two and four thousand hertz, and these sounds have a lot of energy exactly in that range. In experiments, when researchers removed those frequencies, participants found the sound much less unpleasant."),
  L("Παρουσιαστής", "m", "Το ενδιαφέρον είναι ότι στην ίδια περιοχή συχνοτήτων βρίσκονται και πολλές κραυγές, όπως το κλάμα ενός μωρού. Κάποιοι υποθέτουν ότι η αντίδρασή μας είναι ένα κατάλοιπο ενός μηχανισμού συναγερμού. Αυτό, πάντως, δεν έχει αποδειχτεί· όπως λένε και οι ίδιοι οι επιστήμονες, για την ώρα είναι μια ελκυστική υπόθεση.", "Interestingly, many screams, such as a baby's cry, also fall within the same frequency range. Some speculate that our reaction is a remnant of an alarm mechanism. This, however, has not been proven; as the scientists themselves say, for now it is an attractive hypothesis."),
 ],
 "questions": [
  Q("Τι κοινό έχουν οι ήχοι που αναφέρει ο παρουσιαστής;", ["Είναι πολύ δυνατοί", "Μας προκαλούν έντονη αποστροφή, αν και δεν είναι δυνατοί", "Τους ακούμε μόνο στο σχολείο", "Ενοχλούν μόνο τα παιδιά"], 1, "Δεν είναι καν δυνατοί ήχοι"),
  Q("Τι έδειξαν τα πειράματα;", ["Ότι χωρίς ορισμένες συχνότητες ο ήχος ήταν λιγότερο δυσάρεστος", "Ότι οι γυναίκες ενοχλούνται περισσότερο", "Ότι ο ήχος δεν ενοχλεί όσους δεν τον βλέπουν", "Ότι η κιμωλία είναι χειρότερη από τα νύχια"], 0, "οι συμμετέχοντες έβρισκαν τον ήχο πολύ λιγότερο δυσάρεστο"),
  Q("Πώς χαρακτηρίζει ο παρουσιαστής την ιδέα του μηχανισμού συναγερμού;", ["Ως αποδεδειγμένο γεγονός", "Ως παλιά, λανθασμένη θεωρία", "Ως ελκυστική υπόθεση που δεν έχει αποδειχτεί", "Ως ανέκδοτο"], 2, "για την ώρα είναι μια ελκυστική υπόθεση"),
 ],
 "gloss": {"μαυροπίνακα": "μαυροπίνακας — blackboard", "κιμωλία": "κιμωλία — chalk", "τρίζει": "τρίζω — to squeak, creak", "αποστροφή": "αποστροφή — revulsion", "ακουστικός πόρος": "ακουστικός πόρος — ear canal", "κατάλοιπο": "κατάλοιπο — remnant", "συναγερμού": "συναγερμός — alarm"},
})

ITEMS.append({
 "id": "l188-rep-aisthitires-aera-sta-scholeia", "title": "Αισθητήρες για τον αέρα των σχολείων", "title_en": "Air sensors for schools", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα πρόγραμμα σε σχολεία μιας πόλης.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε κάθε τάξη των δεκαοχτώ σχολείων του δήμου κρέμεται από φέτος ένα μικρό λευκό κουτί. Είναι ένας αισθητήρας που μετρά το διοξείδιο του άνθρακα στον αέρα. Όταν η τιμή ανεβαίνει πολύ, ένα λαμπάκι γίνεται κόκκινο, και αυτό σημαίνει ένα πράγμα: ανοίξτε τα παράθυρα.", "In every classroom of the municipality's eighteen schools, a small white box has been hanging since this year. It's a sensor that measures carbon dioxide in the air. When the level rises too high, a little light turns red, and that means one thing: open the windows."),
  L("Ρεπόρτερ", "f", "Οι δάσκαλοι λένε ότι το κόκκινο λαμπάκι ανάβει πιο συχνά απ' ό,τι περίμεναν, κυρίως τον χειμώνα, όταν όλοι κρατούν τα παράθυρα κλειστά για το κρύο. «Σε μια γεμάτη τάξη, μετά από σαράντα λεπτά, τα παιδιά νυστάζουν και δεν συγκεντρώνονται», μας λέει μια δασκάλα.", "Teachers say the red light comes on more often than they expected, mostly in winter, when everyone keeps the windows closed because of the cold. \"In a full classroom, after forty minutes, the children get sleepy and can't concentrate,\" a teacher tells us."),
  L("Ρεπόρτερ", "f", "Οι μαθητές έχουν αναλάβει οι ίδιοι την παρακολούθηση: κάθε εβδομάδα ένας «υπεύθυνος αέρα» ανοίγει τα παράθυρα όταν χρειάζεται. Τα στοιχεία από όλα τα σχολεία θα σταλούν στο πανεπιστήμιο της πόλης, που θα προτείνει πού χρειάζονται συστήματα εξαερισμού.", "The pupils have taken on the monitoring themselves: every week an \"air monitor\" opens the windows when needed. The data from all the schools will be sent to the city's university, which will recommend where ventilation systems are needed."),
 ],
 "questions": [
  Q("Τι μετρά ο αισθητήρας;", ["Τη θερμοκρασία", "Τον θόρυβο", "Την υγρασία", "Το διοξείδιο του άνθρακα"], 3, "Είναι ένας αισθητήρας που μετρά το διοξείδιο του άνθρακα στον αέρα"),
  Q("Πότε ανάβει πιο συχνά το κόκκινο λαμπάκι;", ["Τον χειμώνα, με τα παράθυρα κλειστά", "Το καλοκαίρι", "Στο διάλειμμα", "Όταν η τάξη είναι άδεια"], 0, "κυρίως τον χειμώνα, όταν όλοι κρατούν τα παράθυρα κλειστά για το κρύο"),
  Q("Τι θα γίνει με τα στοιχεία;", ["Θα δημοσιευτούν στην εφημερίδα", "Θα σταλούν στο πανεπιστήμιο, που θα προτείνει πού χρειάζεται εξαερισμός", "Θα τα κρατήσουν οι μαθητές", "Θα σβηστούν στο τέλος της χρονιάς"], 1, "που θα προτείνει πού χρειάζονται συστήματα εξαερισμού"),
 ],
 "gloss": {"αισθητήρας": "αισθητήρας — sensor", "διοξείδιο του άνθρακα": "διοξείδιο του άνθρακα — carbon dioxide", "νυστάζουν": "νυστάζω — to feel sleepy", "συγκεντρώνονται": "συγκεντρώνομαι — to concentrate", "εξαερισμού": "εξαερισμός — ventilation"},
})

rnd = random.Random(188)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-188.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
