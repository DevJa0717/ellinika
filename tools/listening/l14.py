# Source for library/listening/listening-14.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l14.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l14-ann-kolymvitirio", "title": "Κλειστό το κολυμβητήριο", "title_en": "The swimming pool is closed", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ηχογραφημένη ανακοίνωση στο τηλέφωνο του δημοτικού κολυμβητηρίου.",
 "script": [
  L("Εκφωνήτρια", "f", "Καλέσατε το Δημοτικό Κολυμβητήριο. Σας ενημερώνουμε ότι η μεγάλη πισίνα θα παραμείνει κλειστή από τη Δευτέρα δεκαέξι έως την Κυριακή τριάντα Νοεμβρίου, λόγω εργασιών συντήρησης στο σύστημα θέρμανσης και καθαρισμού του νερού.", "You have called the Municipal Swimming Pool. We inform you that the large pool will remain closed from Monday the sixteenth to Sunday the thirtieth of November, because of maintenance work on the heating and water-cleaning system."),
  L("Εκφωνήτρια", "f", "Τα τμήματα εκμάθησης για παιδιά θα συνεχιστούν κανονικά στη μικρή πισίνα, με τις ίδιες ώρες. Τα μαθήματα ενηλίκων και η ελεύθερη κολύμβηση αναστέλλονται για αυτό το διάστημα.", "Children's swimming classes will continue as normal in the small pool, at the same times. Adult classes and free swimming are suspended for this period."),
  L("Εκφωνήτρια", "f", "Οι κάτοχοι μηνιαίας κάρτας θα αποζημιωθούν με δύο επιπλέον εβδομάδες, χωρίς χρέωση, που θα προστεθούν αυτόματα στην κάρτα τους. Για περισσότερες πληροφορίες, πατήστε το ένα για να μιλήσετε με τη γραμματεία.", "Holders of a monthly card will be compensated with two extra weeks, free of charge, which will be added automatically to their card. For more information, press one to speak to the office."),
 ],
 "questions": [
  Q("Γιατί κλείνει η μεγάλη πισίνα;", ["Λόγω απεργίας", "Λόγω εργασιών συντήρησης", "Λόγω αγώνων κολύμβησης", "Λόγω έλλειψης νερού"], 1, "λόγω εργασιών συντήρησης"),
  Q("Ποια δραστηριότητα θα συνεχιστεί κανονικά;", ["Η ελεύθερη κολύμβηση", "Τα μαθήματα ενηλίκων", "Τα παιδικά τμήματα στη μικρή πισίνα", "Οι προπονήσεις της ομάδας"], 2, "Τα τμήματα εκμάθησης για παιδιά θα συνεχιστούν κανονικά στη μικρή πισίνα"),
  Q("Πώς θα αποζημιωθούν οι κάτοχοι μηνιαίας κάρτας;", ["Θα πάρουν πίσω τα χρήματά τους", "Θα πάρουν δύο επιπλέον εβδομάδες δωρεάν", "Θα έχουν έκπτωση τον επόμενο μήνα", "Πρέπει να κάνουν αίτηση στη γραμματεία"], 1, "θα αποζημιωθούν με δύο επιπλέον εβδομάδες, χωρίς χρέωση"),
 ],
 "gloss": {"κολυμβητηρίου": "κολυμβητήριο — swimming pool (complex)", "θα παραμείνει": "παραμένω — to remain", "εργασιών συντήρησης": "εργασίες συντήρησης — maintenance work", "θέρμανσης": "θέρμανση — heating", "τμήματα εκμάθησης": "τμήμα εκμάθησης — learners' class", "ελεύθερη κολύμβηση": "ελεύθερη κολύμβηση — free (public) swimming", "αναστέλλονται": "αναστέλλομαι — to be suspended", "κάτοχοι": "κάτοχος — holder", "θα αποζημιωθούν": "αποζημιώνομαι — to be compensated", "θα προστεθούν": "προστίθεμαι — to be added"},
})

ITEMS.append({
 "id": "l14-vm-metakomisi", "title": "Η μετακόμιση", "title_en": "The move", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα από μια εταιρεία μεταφορών προς έναν πελάτη.",
 "script": [
  L("Υπάλληλος", "m", "Καλησπέρα, κύριε Δημητρίου, από τις Μεταφορές Αστέρι σας παίρνουμε, για τη μετακόμιση του Σαββάτου. Θέλαμε να επιβεβαιώσουμε ότι το συνεργείο θα είναι στο σπίτι σας στις οχτώ το πρωί, με το μεγάλο φορτηγό και τον ανυψωτικό.", "Good evening, Mr Dimitriou, we're calling from Asteri Removals about Saturday's move. We wanted to confirm that the crew will be at your home at eight in the morning, with the large truck and the furniture lift."),
  L("Υπάλληλος", "m", "Επειδή το νέο σας διαμέρισμα είναι στον πέμπτο όροφο και το ασανσέρ είναι μικρό, τα μεγάλα έπιπλα θα ανέβουν από το μπαλκόνι. Θα χρειαστούμε άδεια από τον δήμο για να κλείσουμε για δύο ώρες μια λωρίδα του δρόμου· αυτό το αναλαμβάνουμε εμείς.", "Because your new flat is on the fifth floor and the lift is small, the large furniture will go up via the balcony. We'll need a permit from the municipality to close one lane of the street for two hours; we'll take care of that."),
  L("Υπάλληλος", "m", "Ένα πράγμα μόνο: τα κουτιά με τα εύθραυστα, τα ποτήρια και τα πιάτα, γράψτε τα από έξω με μαρκαδόρο, για να τα προσέξουν τα παιδιά. Και αν έχετε κατοικίδιο, καλό θα είναι να μην είναι στο σπίτι εκείνη την ώρα. Ευχαριστούμε!", "Just one thing: the boxes with fragile items, the glasses and plates, write on the outside with a marker, so the lads take care with them. And if you have a pet, it would be good for it not to be in the house at that time. Thank you!"),
 ],
 "questions": [
  Q("Πώς θα ανέβουν τα μεγάλα έπιπλα στο νέο διαμέρισμα;", ["Με το ασανσέρ", "Από τη σκάλα", "Από το μπαλκόνι, με ανυψωτικό", "Θα τα συναρμολογήσουν μέσα"], 2, "τα μεγάλα έπιπλα θα ανέβουν από το μπαλκόνι"),
  Q("Ποιος θα φροντίσει για την άδεια του δήμου;", ["Ο κύριος Δημητρίου", "Η εταιρεία μεταφορών", "Ο διαχειριστής της πολυκατοικίας", "Δεν χρειάζεται άδεια"], 1, "αυτό το αναλαμβάνουμε εμείς"),
  Q("Τι ζητάει ο υπάλληλος για τα εύθραυστα αντικείμενα;", ["Να τα μεταφέρει ο πελάτης μόνος του", "Να γραφτεί πάνω στα κουτιά ότι είναι εύθραυστα", "Να ασφαλιστούν χωριστά", "Να τυλιχτούν σε κουβέρτες"], 1, "γράψτε τα από έξω με μαρκαδόρο"),
 ],
 "gloss": {"εταιρεία μεταφορών": "εταιρεία μεταφορών — removal company", "μετακόμιση": "μετακόμιση — house move", "συνεργείο": "συνεργείο — crew, team; (also) garage", "ανυψωτικό": "ανυψωτικό — (furniture) lift", "έπιπλα": "έπιπλο — piece of furniture", "λωρίδα": "λωρίδα — lane; strip", "το αναλαμβάνουμε": "αναλαμβάνω — to take on, take care of", "εύθραυστα": "εύθραυστος — fragile", "μαρκαδόρο": "μαρκαδόρος — marker pen", "τα παιδιά": "τα παιδιά — (colloquial) the lads, the team", "κατοικίδιο": "κατοικίδιο — pet"},
})

ITEMS.append({
 "id": "l14-dia-optikos", "title": "Στο οπτικό κατάστημα", "title_en": "At the optician's", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα οπτικό κατάστημα, ανάμεσα σε μια πελάτισσα και έναν οπτικό.",
 "script": [
  L("Οπτικός", "m", "Λοιπόν, κυρία Ράπτη, με βάση τη συνταγή του οφθαλμίατρου, χρειάζεστε πολυεστιακούς φακούς. Έχετε ξαναφορέσει;", "So, Mrs Rapti, based on the ophthalmologist's prescription, you need varifocal lenses. Have you worn them before?"),
  L("Ράπτη", "f", "Όχι, πρώτη φορά. Μέχρι τώρα φορούσα γυαλιά μόνο για το διάβασμα, αλλά βαριέμαι να τα βγάζω και να τα βάζω συνέχεια. Είναι δύσκολο να τα συνηθίσει κανείς;", "No, first time. Until now I only wore glasses for reading, but I'm tired of taking them off and putting them on all the time. Is it hard to get used to them?"),
  L("Οπτικός", "m", "Χρειάζονται μερικές μέρες. Στην αρχή μπορεί να νιώθετε ότι το πάτωμα «κουνιέται» όταν κατεβαίνετε σκάλες. Γι' αυτό σας συμβουλεύω να μην οδηγήσετε την πρώτη μέρα και να τα φοράτε όσο περισσότερο μπορείτε, για να προσαρμοστεί το μάτι.", "It takes a few days. At first you may feel the floor is \"moving\" when you go down stairs. That's why I advise you not to drive on the first day and to wear them as much as you can, so the eye adapts."),
  L("Ράπτη", "f", "Και ο σκελετός; Μου αρέσει αυτός ο στρογγυλός, αλλά δεν ξέρω αν μου πηγαίνει.", "And the frame? I like this round one, but I don't know if it suits me."),
  L("Οπτικός", "m", "Σας πηγαίνει πολύ. Μόνο που για πολυεστιακούς χρειαζόμαστε λίγο μεγαλύτερο ύψος φακού, οπότε θα σας πρότεινα αυτόν εδώ, που είναι παρόμοιος αλλά λίγο πιο ψηλός. Τα γυαλιά θα είναι έτοιμα σε μία εβδομάδα, και αν μέσα στον πρώτο μήνα δεν τα συνηθίσετε, αλλάζουμε τους φακούς δωρεάν.", "It suits you very well. It's just that for varifocals we need a slightly taller lens, so I'd suggest this one here, which is similar but a bit taller. The glasses will be ready in a week, and if you don't get used to them within the first month, we change the lenses for free."),
 ],
 "questions": [
  Q("Γιατί θέλει η κυρία Ράπτη πολυεστιακούς φακούς;", ["Γιατί έσπασε τα παλιά της γυαλιά", "Γιατί βαριέται να βγάζει και να βάζει τα γυαλιά του διαβάσματος", "Γιατί της το ζήτησε η εργασία της", "Γιατί είναι φθηνότεροι"], 1, "βαριέμαι να τα βγάζω και να τα βάζω συνέχεια"),
  Q("Τι συμβουλεύει ο οπτικός για τις πρώτες μέρες;", ["Να φοράει τα γυαλιά μόνο το βράδυ", "Να μην οδηγήσει την πρώτη μέρα και να τα φοράει πολύ", "Να επιστρέψει μετά από μία μέρα", "Να μην κατεβαίνει σκάλες"], 1, "να μην οδηγήσετε την πρώτη μέρα και να τα φοράτε όσο περισσότερο μπορείτε"),
  Q("Γιατί ο οπτικός προτείνει άλλον σκελετό;", ["Γιατί ο στρογγυλός δεν της πηγαίνει", "Γιατί οι πολυεστιακοί φακοί χρειάζονται μεγαλύτερο ύψος", "Γιατί ο στρογγυλός είναι πολύ ακριβός", "Γιατί δεν τον έχει σε απόθεμα"], 1, "για πολυεστιακούς χρειαζόμαστε λίγο μεγαλύτερο ύψος φακού"),
 ],
 "gloss": {"οπτικό κατάστημα": "οπτικό κατάστημα — optician's shop", "οπτικό": "οπτικός — optician", "συνταγή": "συνταγή — prescription; recipe", "οφθαλμίατρου": "οφθαλμίατρος — ophthalmologist", "πολυεστιακούς φακούς": "πολυεστιακοί φακοί — varifocal lenses", "βαριέμαι": "βαριέμαι — to be bored of, can't be bothered to", "να τα συνηθίσει": "συνηθίζω — to get used to", "κουνιέται": "κουνιέμαι — to move, sway", "να προσαρμοστεί": "προσαρμόζομαι — to adapt", "σκελετός": "σκελετός — (glasses) frame; skeleton", "μου πηγαίνει": "μου πηγαίνει — it suits me"},
})

ITEMS.append({
 "id": "l14-dia-geitones", "title": "Το κλιματιστικό που στάζει", "title_en": "The dripping air conditioner", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση ανάμεσα σε δύο γείτονες σε μια πολυκατοικία.",
 "script": [
  L("Κυρία Βέρα", "f", "Κύριε Σωτήρη, συγγνώμη που σας ενοχλώ. Το κλιματιστικό σας στάζει όλη μέρα στο μπαλκόνι μου. Έχει γεμίσει ο τοίχος μούχλα και δεν μπορώ να απλώσω ρούχα.", "Mr Sotiris, sorry to bother you. Your air conditioner drips onto my balcony all day. The wall is full of mould and I can't hang out washing."),
  L("Κύριος Σωτήρης", "m", "Αλήθεια; Δεν το είχα καταλάβει καθόλου. Ο σωλήνας υποτίθεται ότι πάει στην υδρορροή. Μάλλον θα έχει βγει από τη θέση του με τον αέρα των προηγούμενων ημερών.", "Really? I hadn't noticed at all. The pipe is supposed to go into the drainpipe. It must have come out of place with the wind of the last few days."),
  L("Κυρία Βέρα", "f", "Μπορεί. Δεν θέλω να γίνει θέμα στη γενική συνέλευση, γι' αυτό ήρθα πρώτα σε εσάς.", "Maybe. I don't want it to become an issue at the general meeting, that's why I came to you first."),
  L("Κύριος Σωτήρης", "m", "Καλά κάνατε. Θα φωνάξω αύριο τον τεχνικό να το φτιάξει σωστά, και αν έχει πάθει ζημιά ο τοίχος σας, θα πληρώσω εγώ το βάψιμο. Δεν είναι σωστό να ταλαιπωρείστε εσείς για κάτι δικό μου.", "You did the right thing. I'll call the technician tomorrow to fix it properly, and if your wall has been damaged, I'll pay for the painting. It isn't right that you should be inconvenienced for something of mine."),
  L("Κυρία Βέρα", "f", "Σας ευχαριστώ πολύ. Ελάτε κάποια στιγμή για καφέ, να γνωριστούμε καλύτερα. Τόσα χρόνια μένουμε ο ένας πάνω από τον άλλον και μιλάμε μόνο στο ασανσέρ!", "Thank you very much. Come over for coffee sometime, so we get to know each other better. All these years we've lived one above the other and we only talk in the lift!"),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα της κυρίας Βέρας;", ["Ο θόρυβος από το κλιματιστικό", "Το νερό από το κλιματιστικό του γείτονα στάζει στο μπαλκόνι της", "Ο γείτονας απλώνει ρούχα στο μπαλκόνι της", "Το ασανσέρ είναι χαλασμένο"], 1, "Το κλιματιστικό σας στάζει όλη μέρα στο μπαλκόνι μου."),
  Q("Γιατί η κυρία Βέρα μίλησε πρώτα στον κύριο Σωτήρη;", ["Γιατί είναι φίλοι", "Γιατί δεν ήθελε να γίνει θέμα στη γενική συνέλευση", "Γιατί το ζήτησε ο διαχειριστής", "Γιατί ο τεχνικός ήταν απασχολημένος"], 1, "Δεν θέλω να γίνει θέμα στη γενική συνέλευση"),
  Q("Τι προσφέρεται να κάνει ο κύριος Σωτήρης;", ["Να μετακινήσει το κλιματιστικό", "Να φωνάξει τεχνικό και να πληρώσει το βάψιμο", "Να αγοράσει καινούργιο κλιματιστικό", "Να μην το χρησιμοποιεί πια"], 1, "Θα φωνάξω αύριο τον τεχνικό ... θα πληρώσω εγώ το βάψιμο"),
 ],
 "gloss": {"κλιματιστικό": "κλιματιστικό — air conditioner", "στάζει": "στάζω — to drip", "μούχλα": "μούχλα — mould", "να απλώσω ρούχα": "απλώνω ρούχα — to hang out washing", "σωλήνας": "σωλήνας — pipe", "υποτίθεται": "υποτίθεται ότι — it is supposed to", "υδρορροή": "υδρορροή — drainpipe, gutter", "γενική συνέλευση": "γενική συνέλευση — general meeting (of residents)", "έχει πάθει ζημιά": "παθαίνω ζημιά — to be damaged", "βάψιμο": "βάψιμο — painting", "να ταλαιπωρείστε": "ταλαιπωρούμαι — to be inconvenienced, put to trouble", "να γνωριστούμε": "γνωρίζομαι — to get to know each other"},
})

ITEMS.append({
 "id": "l14-mon-pasxa", "title": "Πάσχα στο χωριό", "title_en": "Easter in the village", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια νεαρή Αμερικανίδα, που ζει στην Ελλάδα, να περιγράφει το πρώτο της Πάσχα σε ένα χωριό.",
 "script": [
  L("Τζένη", "f", "Το πρώτο μου ελληνικό Πάσχα το πέρασα στο χωριό της πεθεράς μου, στη Μεσσηνία. Μου είχαν πει ότι είναι η μεγαλύτερη γιορτή της χρονιάς, αλλά δεν ήμουν προετοιμασμένη για τόση ένταση. Από τη Μεγάλη Πέμπτη όλο το σπίτι ήταν σε κίνηση: βάψαμε κόκκινα αυγά, πλάσαμε κουλούρια, και η πεθερά μου ετοίμαζε τη μαγειρίτσα από το Σάββατο το πρωί.", "I spent my first Greek Easter in my mother-in-law's village in Messinia. They had told me it was the biggest celebration of the year, but I wasn't prepared for such intensity. From Holy Thursday the whole house was in motion: we dyed red eggs, shaped biscuits, and my mother-in-law was preparing the magiritsa soup from Saturday morning."),
  L("Τζένη", "f", "Η πιο δυνατή στιγμή ήταν η Ανάσταση. Λίγο πριν από τα μεσάνυχτα, η εκκλησία έσβησε όλα τα φώτα. Ύστερα ο παπάς βγήκε με ένα κερί και είπε «Δεύτε λάβετε φως», και το φως πέρασε από κερί σε κερί, ώσπου όλη η πλατεία φωτίστηκε. Όλοι φιλιούνταν και έλεγαν «Χριστός Ανέστη». Και μετά, τα βεγγαλικά, τόσο δυνατά που νόμιζα ότι γινόταν πόλεμος!", "The most powerful moment was the Resurrection. Just before midnight, the church turned off all the lights. Then the priest came out with a candle and said \"Come, receive the light\", and the light passed from candle to candle until the whole square was lit up. Everyone was kissing and saying \"Christ is risen\". And then the fireworks, so loud I thought a war had started!"),
  L("Τζένη", "f", "Την Κυριακή ψήναμε αρνί στη σούβλα από τις έξι το πρωί, με μουσική και κρασί, και φάγαμε μέχρι το βράδυ. Αυτό που μου έμεινε δεν είναι τόσο το θρησκευτικό κομμάτι όσο η αίσθηση ότι όλο το χωριό, ακόμα και όσοι ζουν μακριά, γυρίζει για να είναι μαζί.", "On Sunday we were roasting lamb on the spit from six in the morning, with music and wine, and we ate until the evening. What stayed with me is not so much the religious part as the feeling that the whole village, even those who live far away, comes back to be together."),
 ],
 "questions": [
  Q("Τι έκαναν στο σπίτι από τη Μεγάλη Πέμπτη;", ["Έφυγαν για την Αθήνα", "Έβαψαν αυγά και έφτιαξαν κουλούρια", "Έψησαν το αρνί", "Πήγαν στη θάλασσα"], 1, "βάψαμε κόκκινα αυγά, πλάσαμε κουλούρια"),
  Q("Τι συνέβη στην εκκλησία λίγο πριν από τα μεσάνυχτα;", ["Άρχισαν τα βεγγαλικά", "Έσβησαν όλα τα φώτα", "Έφυγε ο κόσμος", "Ο παπάς μοίρασε αυγά"], 1, "η εκκλησία έσβησε όλα τα φώτα"),
  Q("Τι εντυπωσίασε περισσότερο την Τζένη;", ["Το φαγητό", "Τα βεγγαλικά", "Η αίσθηση ότι όλο το χωριό ξαναβρίσκεται μαζί", "Η θρησκευτική λειτουργία"], 2, "η αίσθηση ότι όλο το χωριό, ακόμα και όσοι ζουν μακριά, γυρίζει για να είναι μαζί"),
 ],
 "gloss": {"πεθεράς": "πεθερά — mother-in-law", "Μεγάλη Πέμπτη": "Μεγάλη Πέμπτη — Holy (Maundy) Thursday", "πλάσαμε": "πλάθω — to shape, knead", "μαγειρίτσα": "μαγειρίτσα — Easter soup made from lamb offal, eaten after the midnight service", "Ανάσταση": "Ανάσταση — the Resurrection (midnight Easter service)", "Δεύτε λάβετε φως": "Δεύτε λάβετε φως — 'Come, receive the light' (church Greek)", "φιλιούνταν": "φιλιέμαι — to kiss (each other)", "Χριστός Ανέστη": "Χριστός Ανέστη — 'Christ is risen' (reply: Αληθώς Ανέστη)", "βεγγαλικά": "βεγγαλικά — fireworks", "σούβλα": "σούβλα — spit (for roasting)"},
})

ITEMS.append({
 "id": "l14-rep-trygos", "title": "Τρύγος στη Νεμέα", "title_en": "Grape harvest in Nemea", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από τον τρύγο στη Νεμέα της Πελοποννήσου.",
 "script": [
  L("Δημοσιογράφος", "m", "Είναι επτά το πρωί και στους αμπελώνες της Νεμέας ο τρύγος έχει ήδη αρχίσει. Οι εργάτες κόβουν τα τσαμπιά με μικρά ψαλίδια και τα ρίχνουν σε πλαστικά τελάρα, πριν ανέβει πολύ η θερμοκρασία. Εδώ καλλιεργείται κυρίως το Αγιωργίτικο, μια ερυθρή ποικιλία που δίνει ένα από τα πιο γνωστά ελληνικά κρασιά.", "It is seven in the morning and in the vineyards of Nemea the harvest has already begun. The workers cut the bunches with small shears and toss them into plastic crates before the temperature rises too much. Here the main variety grown is Agiorgitiko, a red grape that produces one of the best-known Greek wines."),
  L("Δημοσιογράφος", "m", "Φέτος η σοδειά είναι μικρότερη από άλλες χρονιές. Ο ζεστός και ξερός Ιούλιος έκανε τα σταφύλια να ωριμάσουν νωρίτερα και με λιγότερο χυμό. Οι οινοπαραγωγοί, ωστόσο, είναι αισιόδοξοι για την ποιότητα: λιγότερος χυμός σημαίνει συχνά πιο συμπυκνωμένα αρώματα.", "This year the harvest is smaller than in other years. The hot, dry July made the grapes ripen earlier and with less juice. Winemakers, however, are optimistic about the quality: less juice often means more concentrated aromas."),
  L("Δημοσιογράφος", "m", "Ο τρύγος έχει γίνει και τουριστικό γεγονός. Πολλά οινοποιεία καλούν επισκέπτες να συμμετάσχουν, να πατήσουν σταφύλια με τα πόδια, όπως παλιά, και να δοκιμάσουν τα κρασιά της περιοχής. Για τους μικρούς παραγωγούς, ο οινοτουρισμός αποτελεί πλέον ένα σημαντικό συμπληρωματικό εισόδημα.", "The harvest has also become a tourist event. Many wineries invite visitors to take part, to tread grapes with their feet, as in the old days, and to taste the region's wines. For small producers, wine tourism is now an important supplementary income."),
 ],
 "questions": [
  Q("Γιατί οι εργάτες ξεκινούν νωρίς το πρωί;", ["Για να τελειώσουν πριν από τη βροχή", "Για να προλάβουν πριν ανέβει πολύ η θερμοκρασία", "Γιατί έρχονται οι τουρίστες", "Γιατί το απαιτεί ο νόμος"], 1, "πριν ανέβει πολύ η θερμοκρασία"),
  Q("Γιατί η φετινή σοδειά είναι μικρότερη;", ["Λόγω χαλαζιού", "Λόγω του ζεστού και ξερού Ιουλίου", "Γιατί φυτεύτηκαν λιγότερα αμπέλια", "Λόγω έλλειψης εργατών"], 1, "Ο ζεστός και ξερός Ιούλιος έκανε τα σταφύλια να ωριμάσουν νωρίτερα και με λιγότερο χυμό"),
  Q("Τι σημαίνει ο οινοτουρισμός για τους μικρούς παραγωγούς;", ["Ένα σημαντικό συμπληρωματικό εισόδημα", "Περισσότερη δουλειά χωρίς όφελος", "Το τέλος του παραδοσιακού τρύγου", "Ένα πρόβλημα για τα αμπέλια"], 0, "ο οινοτουρισμός αποτελεί πλέον ένα σημαντικό συμπληρωματικό εισόδημα"),
 ],
 "gloss": {"τρύγο": "τρύγος — grape harvest", "αμπελώνες": "αμπελώνας — vineyard", "τσαμπιά": "τσαμπί — bunch (of grapes)", "ψαλίδια": "ψαλίδι — scissors, shears", "τελάρα": "τελάρο — crate", "ερυθρή ποικιλία": "ερυθρή ποικιλία — red variety", "σοδειά": "σοδειά — harvest, crop", "να ωριμάσουν": "ωριμάζω — to ripen", "οινοπαραγωγοί": "οινοπαραγωγός — winemaker", "συμπυκνωμένα": "συμπυκνωμένος — concentrated", "οινοποιεία": "οινοποιείο — winery", "να πατήσουν": "πατάω — to tread", "συμπληρωματικό εισόδημα": "συμπληρωματικό εισόδημα — supplementary income"},
})

ITEMS.append({
 "id": "l14-rep-metro-thess", "title": "Επιτέλους μετρό στη Θεσσαλονίκη", "title_en": "A metro for Thessaloniki at last", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για το μετρό της Θεσσαλονίκης.",
 "script": [
  L("Δημοσιογράφος", "f", "Για δεκαετίες, το μετρό της Θεσσαλονίκης ήταν το αγαπημένο αστείο των κατοίκων της. Τα έργα ξεκίνησαν το 2006, σταμάτησαν, ξανάρχισαν, και οι λαμαρίνες γύρω από τα εργοτάξια έγιναν μέρος του τοπίου της πόλης. Τον Νοέμβριο του 2024, όμως, οι πρώτοι συρμοί άρχισαν επιτέλους να κυκλοφορούν.", "For decades, the Thessaloniki metro was the city's favourite joke. Work began in 2006, stopped, started again, and the metal hoardings around the building sites became part of the city's landscape. In November 2024, however, the first trains finally began to run."),
  L("Δημοσιογράφος", "f", "Μία από τις αιτίες των καθυστερήσεων ήταν οι αρχαιότητες. Κάτω από την οδό Εγνατία βρέθηκε ένα τμήμα της βυζαντινής κεντρικής οδού της πόλης, με πλακόστρωτα, καταστήματα και εργαστήρια. Μετά από μεγάλη διαμάχη, αποφασίστηκε να παραμείνουν τα ευρήματα στη θέση τους, στον σταθμό Βενιζέλου.", "One of the causes of the delays was the antiquities. Beneath Egnatia Street a section of the city's Byzantine main street was found, with paving stones, shops and workshops. After a long dispute, it was decided that the finds would remain in place, at Venizelou station."),
  L("Δημοσιογράφος", "f", "Σήμερα οι επιβάτες περνούν καθημερινά δίπλα από μνημεία χιλίων και πλέον ετών, πηγαίνοντας στη δουλειά τους. Οι κάτοικοι, πάντως, δεν έχουν σταματήσει να αστειεύονται· τώρα λένε ότι το επόμενο θαύμα θα είναι να φτάσει το μετρό και στο αεροδρόμιο.", "Today passengers pass daily beside monuments more than a thousand years old on their way to work. The residents, however, haven't stopped joking; now they say the next miracle will be for the metro to reach the airport too."),
 ],
 "questions": [
  Q("Πότε άρχισε να λειτουργεί το μετρό της Θεσσαλονίκης;", ["Το 2006", "Τον Νοέμβριο του 2024", "Πριν από δέκα χρόνια", "Δεν λειτουργεί ακόμη"], 1, "Τον Νοέμβριο του 2024 ... οι πρώτοι συρμοί άρχισαν επιτέλους να κυκλοφορούν"),
  Q("Τι βρέθηκε κάτω από την οδό Εγνατία;", ["Ένα αρχαίο θέατρο", "Τμήμα της βυζαντινής κεντρικής οδού", "Ένας ρωμαϊκός ναός", "Ένα νεκροταφείο"], 1, "ένα τμήμα της βυζαντινής κεντρικής οδού της πόλης"),
  Q("Τι αποφασίστηκε για τα ευρήματα;", ["Να μεταφερθούν σε μουσείο", "Να παραμείνουν στη θέση τους, στον σταθμό", "Να καλυφθούν ξανά", "Να πουληθούν"], 1, "αποφασίστηκε να παραμείνουν τα ευρήματα στη θέση τους"),
 ],
 "gloss": {"λαμαρίνες": "λαμαρίνα — metal sheet; (here) hoarding", "εργοτάξια": "εργοτάξιο — building site", "συρμοί": "συρμός — train (set of carriages)", "καθυστερήσεων": "καθυστέρηση — delay", "αρχαιότητες": "αρχαιότητες — antiquities", "τμήμα": "τμήμα — section", "πλακόστρωτα": "πλακόστρωτο — paving, paved surface", "διαμάχη": "διαμάχη — dispute", "ευρήματα": "εύρημα — find", "επιβάτες": "επιβάτης — passenger", "να αστειεύονται": "αστειεύομαι — to joke"},
})

ITEMS.append({
 "id": "l14-int-taxi", "title": "Γυναίκα στο τιμόνι του ταξί", "title_en": "A woman behind the wheel of a taxi", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια οδηγό ταξί στην Αθήνα.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσα χρόνια οδηγείτε ταξί;", "How many years have you been driving a taxi?"),
  L("Ρούλα", "f", "Δώδεκα. Το ταξί ήταν του πατέρα μου. Όταν βγήκε στη σύνταξη, κανείς από τους αδελφούς μου δεν το ήθελε, και είπα: θα το πάρω εγώ. Ο πατέρας μου στην αρχή γέλασε· τώρα λέει σε όλους ότι οδηγώ καλύτερα από εκείνον.", "Twelve. The taxi was my father's. When he retired, none of my brothers wanted it, and I said: I'll take it. My father laughed at first; now he tells everyone that I drive better than him."),
  L("Δημοσιογράφος", "m", "Πώς αντιδρούν οι πελάτες όταν βλέπουν γυναίκα οδηγό;", "How do customers react when they see a woman driver?"),
  L("Ρούλα", "f", "Οι περισσότεροι ευχάριστα. Οι γυναίκες, ιδίως τη νύχτα, νιώθουν πιο ασφαλείς και κάποιες με ζητούν συγκεκριμένα μέσω της εφαρμογής. Υπάρχουν και κάποιοι κύριοι που μου δίνουν οδηγίες για το πώς να πάω, λες και δεν ξέρω την πόλη. Τους αφήνω να μιλάνε και πάω από τον δικό μου δρόμο.", "Most react pleasantly. Women, especially at night, feel safer, and some ask for me specifically through the app. There are also some gentlemen who give me directions on how to go, as if I don't know the city. I let them talk and go my own way."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο δύσκολο κομμάτι της δουλειάς;", "What is the hardest part of the job?"),
  L("Ρούλα", "f", "Η κίνηση και οι ώρες. Δουλεύω δέκα ώρες τη μέρα, και υπάρχουν μέρες που κάνω μιάμιση ώρα για να πάω από το Σύνταγμα στο αεροδρόμιο. Αλλά μου αρέσει που κάθε μέρα γνωρίζω καινούργιους ανθρώπους. Το ταξί είναι σαν μικρό εξομολογητήριο: σε είκοσι λεπτά σού λένε όλη τους τη ζωή.", "The traffic and the hours. I work ten hours a day, and there are days when it takes me an hour and a half to get from Syntagma to the airport. But I like meeting new people every day. The taxi is like a little confessional: in twenty minutes they tell you their whole life."),
 ],
 "questions": [
  Q("Πώς έγινε η Ρούλα οδηγός ταξί;", ["Πήρε το ταξί του πατέρα της όταν εκείνος βγήκε στη σύνταξη", "Το αγόρασε με δάνειο", "Της το πρότεινε μια εταιρεία", "Το κέρδισε σε διαγωνισμό"], 0, "Το ταξί ήταν του πατέρα μου. Όταν βγήκε στη σύνταξη ... θα το πάρω εγώ."),
  Q("Γιατί κάποιες γυναίκες τη ζητούν συγκεκριμένα;", ["Γιατί είναι φθηνότερη", "Γιατί νιώθουν πιο ασφαλείς, ιδίως τη νύχτα", "Γιατί μιλάει αγγλικά", "Γιατί έχει καινούργιο αυτοκίνητο"], 1, "Οι γυναίκες, ιδίως τη νύχτα, νιώθουν πιο ασφαλείς"),
  Q("Τι της αρέσει στη δουλειά της;", ["Οι λίγες ώρες", "Ότι γνωρίζει καινούργιους ανθρώπους", "Η κίνηση", "Τα πολλά χρήματα"], 1, "μου αρέσει που κάθε μέρα γνωρίζω καινούργιους ανθρώπους"),
 ],
 "gloss": {"βγήκε στη σύνταξη": "βγαίνω στη σύνταξη — to retire", "αντιδρούν": "αντιδρώ — to react", "ευχάριστα": "ευχάριστα — pleasantly", "ασφαλείς": "ασφαλής — safe", "συγκεκριμένα": "συγκεκριμένα — specifically", "λες και": "λες και — as if", "κίνηση": "κίνηση — traffic; movement", "μιάμιση ώρα": "μιάμιση ώρα — an hour and a half", "εξομολογητήριο": "εξομολογητήριο — confessional"},
})

ITEMS.append({
 "id": "l14-mon-tragodia", "title": "Η τραγωδία και η δημοκρατία", "title_en": "Tragedy and democracy", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια φιλόλογο να μιλά σε μια διάλεξη για τη σχέση του αρχαίου θεάτρου με την αθηναϊκή δημοκρατία.",
 "script": [
  L("Φιλόλογος", "f", "Συχνά σκεφτόμαστε το αρχαίο θέατρο ως καλλιτεχνικό γεγονός, κάτι ανάλογο με μια σημερινή παράσταση. Στην Αθήνα του πέμπτου αιώνα, όμως, οι δραματικοί αγώνες ήταν πρωτίστως θεσμός της πόλης. Γίνονταν στο πλαίσιο των Μεγάλων Διονυσίων, μιας θρησκευτικής γιορτής, και η οργάνωσή τους αποτελούσε δημόσια υπόθεση.", "We often think of ancient theatre as an artistic event, something like a performance today. In fifth-century Athens, however, the dramatic competitions were first and foremost an institution of the city. They took place within the Great Dionysia, a religious festival, and their organisation was a public matter."),
  L("Φιλόλογος", "f", "Τα έξοδα μιας παράστασης τα αναλάμβανε ένας εύπορος πολίτης, ο χορηγός, ως μια μορφή φορολογίας και ταυτόχρονα κοινωνικού κύρους. Και η κρίση των έργων δεν ανήκε σε ειδικούς, αλλά σε κριτές που κληρώνονταν από τις φυλές των πολιτών, όπως ακριβώς κληρώνονταν και πολλοί άρχοντες.", "The costs of a production were taken on by a wealthy citizen, the choregos, as a form of taxation and at the same time of social prestige. And the judging of the plays belonged not to experts but to judges drawn by lot from the citizens' tribes, exactly as many officials were drawn by lot."),
  L("Φιλόλογος", "f", "Αυτό που κάνει όμως την τραγωδία βαθιά δημοκρατική είναι το περιεχόμενό της. Τα έργα θέτουν ερωτήματα που δεν έχουν εύκολη απάντηση: τη σύγκρουση ανάμεσα στον νόμο της πόλης και στον άγραφο ηθικό νόμο, όπως στην «Αντιγόνη», ή την ευθύνη του ηγέτη για τις αποφάσεις του. Ο θεατής δεν παίρνει έτοιμες λύσεις· καλείται να σκεφτεί, όπως θα σκεφτόταν στην Εκκλησία του Δήμου.", "But what makes tragedy deeply democratic is its content. The plays raise questions that have no easy answer: the conflict between the law of the city and the unwritten moral law, as in Antigone, or the leader's responsibility for his decisions. The spectator does not get ready-made solutions; he is called upon to think, as he would think in the Assembly."),
  L("Φιλόλογος", "f", "Θα έλεγα, λοιπόν, ότι το θέατρο λειτουργούσε ως ένα σχολείο της πόλης για τον εαυτό της: ένας χώρος όπου η κοινότητα έβλεπε τις συγκρούσεις της να παίρνουν μορφή και μάθαινε να ζει με την αμφιβολία.", "I would say, then, that the theatre functioned as a school of the city for itself: a space where the community saw its conflicts take shape and learned to live with doubt."),
 ],
 "questions": [
  Q("Σύμφωνα με την ομιλήτρια, τι ήταν πρωτίστως οι δραματικοί αγώνες στην αρχαία Αθήνα;", ["Ιδιωτική ψυχαγωγία", "Θεσμός της πόλης στο πλαίσιο μιας θρησκευτικής γιορτής", "Εμπορική επιχείρηση", "Μάθημα για τα παιδιά"], 1, "οι δραματικοί αγώνες ήταν πρωτίστως θεσμός της πόλης"),
  Q("Ποιος ήταν ο ρόλος του χορηγού;", ["Έγραφε τα έργα", "Έκρινε τις παραστάσεις", "Αναλάμβανε τα έξοδα της παράστασης", "Έπαιζε τον πρωταγωνιστή"], 2, "Τα έξοδα μιας παράστασης τα αναλάμβανε ένας εύπορος πολίτης, ο χορηγός"),
  Q("Πώς επιλέγονταν οι κριτές;", ["Από τους ποιητές", "Με κλήρωση από τις φυλές των πολιτών", "Από τον άρχοντα", "Με ψηφοφορία του κοινού"], 1, "κριτές που κληρώνονταν από τις φυλές των πολιτών"),
  Q("Γιατί η τραγωδία ήταν, κατά την ομιλήτρια, βαθιά δημοκρατική;", ["Γιατί η είσοδος ήταν δωρεάν", "Γιατί έθετε δύσκολα ερωτήματα και καλούσε τον θεατή να σκεφτεί", "Γιατί οι ηθοποιοί ήταν απλοί πολίτες", "Γιατί υμνούσε τους ηγέτες της πόλης"], 1, "Τα έργα θέτουν ερωτήματα που δεν έχουν εύκολη απάντηση ... καλείται να σκεφτεί"),
 ],
 "gloss": {"φιλόλογο": "φιλόλογος — philologist; teacher of Greek and literature", "δραματικοί αγώνες": "δραματικοί αγώνες — drama competitions", "πρωτίστως": "πρωτίστως — first and foremost", "θεσμός": "θεσμός — institution", "Μεγάλων Διονυσίων": "Μεγάλα Διονύσια — the Great Dionysia festival", "εύπορος": "εύπορος — wealthy", "χορηγός": "χορηγός — choregos, citizen who funded a production; (today) sponsor", "κύρους": "κύρος — prestige", "κληρώνονταν": "κληρώνομαι — to be drawn by lot", "φυλές": "φυλή — tribe (civic division of Athens)", "άρχοντες": "άρχοντας — magistrate, official", "άγραφο": "άγραφος — unwritten", "Εκκλησία του Δήμου": "Εκκλησία του Δήμου — the Assembly of the Athenian people", "αμφιβολία": "αμφιβολία — doubt"},
})

ITEMS.append({
 "id": "l14-int-naftilia", "title": "Οι Έλληνες εφοπλιστές", "title_en": "Greek shipowners", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν οικονομολόγο για την ελληνική ναυτιλία.",
 "script": [
  L("Δημοσιογράφος", "f", "Λέγεται συχνά ότι οι Έλληνες ελέγχουν τον μεγαλύτερο εμπορικό στόλο του κόσμου. Ισχύει;", "It is often said that Greeks control the world's largest merchant fleet. Is that true?"),
  L("Οικονομολόγος", "m", "Ισχύει, αν μετρήσουμε τη χωρητικότητα των πλοίων που ανήκουν σε Έλληνες, ανεξάρτητα από τη σημαία τους. Οι ελληνικών συμφερόντων εταιρείες ελέγχουν περίπου το ένα πέμπτο της παγκόσμιας χωρητικότητας. Πολλά από αυτά τα πλοία, ωστόσο, φέρουν σημαίες άλλων κρατών, όπως της Λιβερίας ή των Νήσων Μάρσαλ, για φορολογικούς και διοικητικούς λόγους.", "It is true, if we measure the tonnage of ships owned by Greeks, regardless of their flag. Greek-owned companies control about one fifth of world tonnage. Many of these ships, however, fly the flags of other states, such as Liberia or the Marshall Islands, for tax and administrative reasons."),
  L("Δημοσιογράφος", "f", "Πώς εξηγείται αυτή η κυριαρχία μιας τόσο μικρής χώρας;", "How can this dominance by such a small country be explained?"),
  L("Οικονομολόγος", "m", "Η ναυτική παράδοση παίζει ρόλο, ιδίως σε νησιά όπως η Χίος, η Άνδρος ή η Κεφαλονιά, από όπου κατάγονται πολλές εφοπλιστικές οικογένειες. Εξίσου σημαντικό, όμως, είναι το επιχειρηματικό μοντέλο: οικογενειακές εταιρείες, με μεγάλη ευελιξία, που αγοράζουν πλοία όταν οι τιμές πέφτουν και τα πουλούν όταν ανεβαίνουν, αναλαμβάνοντας ρίσκα που οι μεγάλοι όμιλοι συνήθως αποφεύγουν.", "Naval tradition plays a role, especially on islands such as Chios, Andros or Kefalonia, where many shipowning families come from. Just as important, however, is the business model: family companies, very flexible, that buy ships when prices fall and sell them when they rise, taking on risks that large corporate groups usually avoid."),
  L("Δημοσιογράφος", "f", "Και τι κερδίζει η ελληνική οικονομία;", "And what does the Greek economy gain?"),
  L("Οικονομολόγος", "m", "Αυτό είναι το πιο αμφιλεγόμενο ζήτημα. Η ναυτιλία φέρνει σημαντικό συνάλλαγμα και δημιουργεί θέσεις εργασίας στα γραφεία του Πειραιά και στις συναφείς υπηρεσίες. Από την άλλη, οι Έλληνες ναυτικοί είναι πολύ λιγότεροι από παλιά, και το ειδικό φορολογικό καθεστώς της ναυτιλίας προκαλεί συχνά δημόσια συζήτηση για το αν οι εφοπλιστές συνεισφέρουν αρκετά.", "That is the most controversial issue. Shipping brings in significant foreign currency and creates jobs in the offices of Piraeus and related services. On the other hand, Greek seafarers are far fewer than in the past, and shipping's special tax regime often sparks public debate about whether shipowners contribute enough."),
 ],
 "questions": [
  Q("Γιατί πολλά πλοία ελληνικών συμφερόντων έχουν ξένες σημαίες;", ["Γιατί δεν τα δέχονται τα ελληνικά λιμάνια", "Για φορολογικούς και διοικητικούς λόγους", "Γιατί τα πληρώματα είναι ξένα", "Γιατί το απαιτεί η Ευρωπαϊκή Ένωση"], 1, "για φορολογικούς και διοικητικούς λόγους"),
  Q("Ποιο χαρακτηριστικό του επιχειρηματικού μοντέλου τονίζει ο οικονομολόγος;", ["Οι μεγάλοι όμιλοι με αυστηρή γραφειοκρατία", "Η ευελιξία των οικογενειακών εταιρειών και η ανάληψη ρίσκου", "Η κρατική χρηματοδότηση", "Η ναυπήγηση πλοίων στην Ελλάδα"], 1, "οικογενειακές εταιρείες, με μεγάλη ευελιξία ... αναλαμβάνοντας ρίσκα"),
  Q("Γιατί το όφελος για την ελληνική οικονομία είναι αμφιλεγόμενο;", ["Γιατί η ναυτιλία δεν φέρνει καθόλου συνάλλαγμα", "Γιατί οι Έλληνες ναυτικοί λιγόστεψαν και συζητιέται αν οι εφοπλιστές συνεισφέρουν αρκετά", "Γιατί τα γραφεία μεταφέρθηκαν στο εξωτερικό", "Γιατί τα πλοία είναι παλιά"], 1, "οι Έλληνες ναυτικοί είναι πολύ λιγότεροι από παλιά ... αν οι εφοπλιστές συνεισφέρουν αρκετά"),
 ],
 "gloss": {"εφοπλιστές": "εφοπλιστής — shipowner", "ναυτιλία": "ναυτιλία — shipping", "εμπορικό στόλο": "εμπορικός στόλος — merchant fleet", "χωρητικότητα": "χωρητικότητα — tonnage, capacity", "σημαία": "σημαία — flag", "ελληνικών συμφερόντων": "ελληνικών συμφερόντων — Greek-owned (lit. of Greek interests)", "κυριαρχία": "κυριαρχία — dominance", "κατάγονται": "κατάγομαι — to come from, originate", "ευελιξία": "ευελιξία — flexibility", "όμιλοι": "όμιλος — (corporate) group", "αμφιλεγόμενο": "αμφιλεγόμενος — controversial", "συνάλλαγμα": "συνάλλαγμα — foreign currency", "συναφείς": "συναφής — related", "ναυτικοί": "ναυτικός — seafarer, sailor", "φορολογικό καθεστώς": "φορολογικό καθεστώς — tax regime", "συνεισφέρουν": "συνεισφέρω — to contribute"},
})
rnd = random.Random(14)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-14.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
