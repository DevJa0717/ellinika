# Source for library/listening/listening-173.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l173.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l173-ann-ekthesiako-kentro", "title": "Ανακοίνωση στο εκθεσιακό κέντρο", "title_en": "An announcement at the exhibition centre", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός εκθεσιακού κέντρου την τελευταία μέρα μιας μεγάλης έκθεσης.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί επισκέπτες, σας ενημερώνουμε ότι σήμερα, τελευταία ημέρα της έκθεσης, τα περίπτερα θα κλείσουν μία ώρα νωρίτερα, στις οχτώ το βράδυ.", "Dear visitors, we inform you that today, the last day of the exhibition, the stands will close one hour earlier, at eight in the evening."),
  L("Εκφωνητής", "m", "Τα δωρεάν λεωφορεία προς τον σταθμό του μετρό αναχωρούν κάθε δεκαπέντε λεπτά από την πύλη δύο. Παρακαλούμε όσους έχουν αφήσει πράγματα στην γκαρνταρόμπα να τα παραλάβουν πριν από τις οχτώ και μισή, γιατί μετά θα κλείσει.", "The free buses to the metro station leave every fifteen minutes from gate two. We ask those who have left things in the cloakroom to collect them before half past eight, because it will close after that."),
  L("Εκφωνητής", "m", "Τέλος, ένα μικρό αγόρι, περίπου έξι χρονών, με κόκκινο μπουφάν, περιμένει τους γονείς του στο σημείο πληροφοριών, δίπλα στην κεντρική είσοδο. Λέει ότι τον λένε Οδυσσέα. Ευχαριστούμε.", "Finally, a little boy, about six years old, in a red jacket, is waiting for his parents at the information point, next to the main entrance. He says his name is Odysseas. Thank you."),
 ],
 "questions": [
  Q("Τι αλλάζει σήμερα στο ωράριο;", ["Τα περίπτερα θα ανοίξουν αργότερα", "Τα περίπτερα θα κλείσουν μία ώρα νωρίτερα", "Η έκθεση θα κρατήσει μία μέρα ακόμα", "Το μετρό θα σταματήσει νωρίτερα"], 1, "τα περίπτερα θα κλείσουν μία ώρα νωρίτερα"),
  Q("Από πού φεύγουν τα δωρεάν λεωφορεία;", ["Από την κεντρική είσοδο", "Από τον σταθμό του μετρό", "Από την πύλη δύο", "Από τη γκαρνταρόμπα"], 2, "από την πύλη δύο"),
  Q("Πού περιμένει το μικρό αγόρι;", ["Στο σημείο πληροφοριών, δίπλα στην κεντρική είσοδο", "Στην πύλη δύο", "Στη γκαρνταρόμπα", "Στο λεωφορείο"], 0, "περιμένει τους γονείς του στο σημείο πληροφοριών"),
 ],
 "gloss": {"εκθεσιακού": "εκθεσιακός — exhibition (adj.)", "έκθεσης": "έκθεση — exhibition, fair", "περίπτερα": "περίπτερο — stand, pavilion", "αναχωρούν": "αναχωρώ — to depart", "πύλη": "πύλη — gate", "γκαρνταρόμπα": "γκαρνταρόμπα — cloakroom", "παραλάβουν": "παραλαμβάνω — to collect", "μπουφάν": "μπουφάν — jacket", "σημείο πληροφοριών": "σημείο πληροφοριών — information point"},
})

ITEMS.append({
 "id": "l173-int-odigos-trakter", "title": "Η οδηγός τρακτέρ", "title_en": "The tractor driver", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια νέα γυναίκα που δουλεύει στο κτήμα της οικογένειάς της στον θεσσαλικό κάμπο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς βρεθήκατε στο τιμόνι ενός τρακτέρ;", "How did you end up behind the wheel of a tractor?"),
  L("Αγρότισσα", "f", "Σπούδασα λογιστική στη Λάρισα και δούλευα σε γραφείο. Όταν ο πατέρας μου χτύπησε τη μέση του, κάποιος έπρεπε να οργώσει τα χωράφια. Τον πρώτο μήνα έκανα στραβές αυλακιές και οι γείτονες γελούσαν. Σήμερα μου ζητάνε να οργώσω και τα δικά τους.", "I studied accounting in Larissa and worked in an office. When my father hurt his back, someone had to plough the fields. The first month I made crooked furrows and the neighbours laughed. Today they ask me to plough theirs too."),
  L("Δημοσιογράφος", "m", "Έχει αλλάξει η δουλειά από την εποχή του πατέρα σας;", "Has the work changed since your father's time?"),
  L("Αγρότισσα", "f", "Πάρα πολύ. Το καινούργιο τρακτέρ έχει δορυφορικό σύστημα και πηγαίνει μόνο του σε ευθεία γραμμή. Εγώ προσέχω τις στροφές και τα μηχανήματα πίσω. Έτσι δεν πατάμε δύο φορές το ίδιο χώμα και ξοδεύουμε λιγότερο πετρέλαιο και λίπασμα.", "Very much. The new tractor has a satellite system and goes by itself in a straight line. I take care of the turns and the machinery behind. That way we don't drive over the same soil twice and we spend less diesel and fertiliser."),
  L("Δημοσιογράφος", "m", "Θα μένατε για πάντα στο χωριό;", "Would you stay in the village for ever?"),
  L("Αγρότισσα", "f", "Τον χειμώνα, όταν ο κάμπος είναι γκρίζος και λασπωμένος, δεν είμαι σίγουρη. Αλλά τον Ιούνιο, όταν θερίζουμε το σιτάρι και μυρίζει όλος ο κάμπος, δεν θα το άλλαζα με κανένα γραφείο.", "In winter, when the plain is grey and muddy, I'm not sure. But in June, when we harvest the wheat and the whole plain smells of it, I wouldn't change it for any office."),
 ],
 "questions": [
  Q("Γιατί άρχισε να δουλεύει στα χωράφια;", ["Γιατί έχασε τη δουλειά της", "Γιατί ο πατέρας της χτύπησε τη μέση του", "Γιατί σπούδασε γεωπονία", "Γιατί της το ζήτησαν οι γείτονες"], 1, "Όταν ο πατέρας μου χτύπησε τη μέση του"),
  Q("Ποιο πλεονέκτημα έχει το δορυφορικό σύστημα του τρακτέρ;", ["Πηγαίνει πιο γρήγορα", "Δεν χρειάζεται οδηγό καθόλου", "Δεν πατάνε δύο φορές το ίδιο χώμα και ξοδεύουν λιγότερα", "Δουλεύει και τη νύχτα"], 2, "δεν πατάμε δύο φορές το ίδιο χώμα"),
  Q("Πότε είναι σίγουρη ότι της αρέσει η ζωή στο χωριό;", ["Τον Ιούνιο, στο θέρισμα του σιταριού", "Τον χειμώνα", "Όταν πηγαίνει στη Λάρισα", "Όταν βρέχει"], 0, "τον Ιούνιο, όταν θερίζουμε το σιτάρι"),
 ],
 "gloss": {"κτήμα": "κτήμα — farm, estate", "κάμπο": "κάμπος — plain", "τρακτέρ": "τρακτέρ — tractor", "λογιστική": "λογιστική — accounting", "οργώσει": "οργώνω — to plough", "αυλακιές": "αυλακιά — furrow", "δορυφορικό": "δορυφορικός — satellite (adj.)", "χώμα": "χώμα — soil", "πετρέλαιο": "πετρέλαιο — diesel, oil", "λίπασμα": "λίπασμα — fertiliser", "λασπωμένος": "λασπωμένος — muddy", "θερίζουμε": "θερίζω — to harvest, reap", "σιτάρι": "σιτάρι — wheat"},
})

ITEMS.append({
 "id": "l173-int-maskot-tis-omadas", "title": "Μέσα στη στολή της μασκότ", "title_en": "Inside the mascot costume", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν νέο που φοράει τη στολή της μασκότ μιας ομάδας μπάσκετ στους αγώνες.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς είναι να είσαι ένας γαλάζιος αετός ύψους δύο μέτρων;", "What's it like to be a two-metre-tall blue eagle?"),
  L("Νέος", "m", "Ζεστό. Η στολή ζυγίζει σχεδόν δεκαπέντε κιλά και μέσα η θερμοκρασία ανεβαίνει πολύ. Στα διαλείμματα πίνω ένα λίτρο νερό. Το άλλο πρόβλημα είναι ότι βλέπω μόνο από μια μικρή σχισμή στο ράμφος, οπότε πρέπει να προσέχω πού πατάω, ειδικά στις σκάλες της κερκίδας.", "Hot. The costume weighs almost fifteen kilos and inside the temperature rises a lot. During breaks I drink a litre of water. The other problem is that I can only see through a small slit in the beak, so I have to watch where I step, especially on the stairs of the stands."),
  L("Δημοσιογράφος", "f", "Επιτρέπεται να μιλάς;", "Are you allowed to speak?"),
  L("Νέος", "m", "Ποτέ. Η μασκότ δεν έχει φωνή. Όλα γίνονται με κινήσεις: χορεύω, κάνω ότι κλαίω όταν χάνουμε, αγκαλιάζω τα παιδιά. Δεν πρέπει επίσης να βγάλω ποτέ το κεφάλι μπροστά στο κοινό, γιατί τα μικρά πιστεύουν ότι ο αετός είναι αληθινός.", "Never. The mascot has no voice. Everything is done with movements: I dance, I pretend to cry when we lose, I hug the children. I must also never take off the head in front of the audience, because the little ones believe the eagle is real."),
  L("Δημοσιογράφος", "f", "Ποια είναι η πιο ωραία στιγμή;", "What is the best moment?"),
  L("Νέος", "m", "Όταν ένα παιδί που φοβόταν στην αρχή έρχεται στο τέλος του αγώνα και μου δίνει μια ζωγραφιά. Έχω μια ολόκληρη κούτα με ζωγραφιές αετών στο σπίτι.", "When a child who was scared at first comes at the end of the match and gives me a drawing. I have a whole box of eagle drawings at home."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με την όραση μέσα στη στολή;", ["Η στολή δεν έχει καθόλου άνοιγμα", "Βλέπει μόνο από μια μικρή σχισμή στο ράμφος", "Τα φώτα του γηπέδου τον τυφλώνουν", "Θολώνουν τα γυαλιά του"], 1, "βλέπω μόνο από μια μικρή σχισμή στο ράμφος"),
  Q("Γιατί δεν βγάζει ποτέ το κεφάλι μπροστά στο κοινό;", ["Γιατί είναι πολύ βαρύ", "Γιατί απαγορεύεται από τον νόμο", "Γιατί τα μικρά παιδιά πιστεύουν ότι ο αετός είναι αληθινός", "Γιατί ντρέπεται"], 2, "τα μικρά πιστεύουν ότι ο αετός είναι αληθινός"),
  Q("Τι κρατάει στο σπίτι του;", ["Μια κούτα με ζωγραφιές αετών", "Φωτογραφίες από τους αγώνες", "Μια μπάλα με υπογραφές", "Μια δεύτερη στολή"], 0, "Έχω μια ολόκληρη κούτα με ζωγραφιές αετών"),
 ],
 "gloss": {"στολή": "στολή — costume, uniform", "μασκότ": "μασκότ — mascot", "αετός": "αετός — eagle", "ζυγίζει": "ζυγίζω — to weigh", "θερμοκρασία": "θερμοκρασία — temperature", "σχισμή": "σχισμή — slit", "ράμφος": "ράμφος — beak", "κερκίδας": "κερκίδα — stand", "κινήσεις": "κίνηση — movement", "αγκαλιάζω": "αγκαλιάζω — to hug", "κοινό": "κοινό — audience", "κούτα": "κούτα — cardboard box"},
})

ITEMS.append({
 "id": "l173-dia-enas-minas-choris-psonia", "title": "Ένας μήνας χωρίς ψώνια;", "title_en": "A month without shopping?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο συγκατοίκους να συζητούν αν θα κάνουν ένα μήνα χωρίς να αγοράσουν τίποτα καινούργιο.",
 "script": [
  L("Ηλέκτρα", "f", "Διάβασα για μια πρόκληση: ένας μήνας χωρίς να αγοράσεις τίποτα καινούργιο, εκτός από τρόφιμα και φάρμακα. Λες να το δοκιμάσουμε;", "I read about a challenge: a month without buying anything new, except food and medicine. Shall we try it?"),
  L("Λευτέρης", "m", "Και τι θα γίνει αν χαλάσει κάτι; Αν μου σκιστούν τα παπούτσια, θα περπατάω ξυπόλυτος;", "And what happens if something breaks? If my shoes tear, will I walk barefoot?"),
  L("Ηλέκτρα", "f", "Επιτρέπεται να επισκευάσεις κάτι ή να το πάρεις μεταχειρισμένο. Ο σκοπός είναι να δεις πόσα πράγματα αγοράζεις χωρίς να τα χρειάζεσαι. Εγώ, για παράδειγμα, έχω τέσσερα μαύρα μπλουζάκια που δεν φοράω ποτέ.", "You're allowed to repair something or get it second-hand. The point is to see how many things you buy without needing them. I, for example, have four black T-shirts I never wear."),
  L("Λευτέρης", "m", "Εντάξει, αλλά τα βιβλία; Δεν μπορώ ένα μήνα χωρίς καινούργιο βιβλίο.", "OK, but what about books? I can't go a month without a new book."),
  L("Ηλέκτρα", "f", "Υπάρχει η δημοτική βιβλιοθήκη, δύο δρόμους πιο κάτω. Και αν στο τέλος του μήνα σού λείπει ακόμα κάτι, τότε το αγοράζεις, αλλά θα ξέρεις ότι το χρειάζεσαι πραγματικά.", "There's the municipal library, two streets down. And if at the end of the month you still miss something, then you buy it, but you'll know you really need it."),
  L("Λευτέρης", "m", "Καλά, δέχομαι. Αλλά αρχίζουμε από την πρώτη του μήνα. Πρώτα πρέπει να πάρω τα γάντια που κοίταζα.", "Fine, I accept. But we start on the first of the month. First I have to buy the gloves I was looking at."),
 ],
 "questions": [
  Q("Τι επιτρέπεται να αγοράσουν κατά τη διάρκεια της πρόκλησης;", ["Μόνο ρούχα", "Τρόφιμα και φάρμακα", "Ό,τι κοστίζει λιγότερο από δέκα ευρώ", "Μόνο βιβλία"], 1, "εκτός από τρόφιμα και φάρμακα"),
  Q("Ποια λύση προτείνει η Ηλέκτρα για τα βιβλία;", ["Να τα αγοράσει μεταχειρισμένα", "Να διαβάσει ξανά τα παλιά", "Τη δημοτική βιβλιοθήκη", "Να τα κατεβάσει από το διαδίκτυο"], 2, "Υπάρχει η δημοτική βιβλιοθήκη"),
  Q("Τι θέλει να κάνει ο Λευτέρης πριν αρχίσουν;", ["Να αγοράσει τα γάντια που κοίταζε", "Να πάει στη βιβλιοθήκη", "Να επισκευάσει τα παπούτσια του", "Να πουλήσει τα μπλουζάκια"], 0, "Πρώτα πρέπει να πάρω τα γάντια που κοίταζα"),
 ],
 "gloss": {"συγκατοίκους": "συγκάτοικος — flatmate", "πρόκληση": "πρόκληση — challenge", "τρόφιμα": "τρόφιμα — food", "σκιστούν": "σκίζομαι — to tear", "ξυπόλυτος": "ξυπόλυτος — barefoot", "επισκευάσεις": "επισκευάζω — to repair", "μεταχειρισμένο": "μεταχειρισμένος — second-hand", "σκοπός": "σκοπός — aim, point", "δέχομαι": "δέχομαι — to accept"},
})

ITEMS.append({
 "id": "l173-dia-sosivio-i-mpratsakia", "title": "Σωσίβιο ή μπρατσάκια;", "title_en": "Life jacket or armbands?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο γονείς σε ένα κατάστημα με είδη θαλάσσης να συζητούν τι θα πάρουν για την τετράχρονη κόρη τους.",
 "script": [
  L("Κώστας", "m", "Πάρουμε τα μπρατσάκια με τα ψαράκια; Της άρεσαν πολύ.", "Shall we get the armbands with the little fish? She liked them a lot."),
  L("Νίκη", "f", "Διάβασα ότι τα μπρατσάκια δεν είναι τόσο ασφαλή. Αν το παιδί γυρίσει μπρούμυτα, δεν το κρατούν με το κεφάλι έξω από το νερό. Και μπορεί να γλιστρήσουν από τα χέρια του.", "I read that armbands aren't so safe. If the child turns face down, they don't keep her head out of the water. And they can slip off her arms."),
  L("Κώστας", "m", "Δηλαδή το γιλέκο-σωσίβιο; Είναι πιο ακριβό και πιο άβολο.", "So the life vest? It's more expensive and less comfortable."),
  L("Νίκη", "f", "Είναι, αλλά κρατάει το σώμα σωστά και έχει και ένα λουρί ανάμεσα στα πόδια, για να μη βγαίνει από το κεφάλι. Ο υπάλληλος είπε ότι πρέπει να έχει την ένδειξη για το βάρος της.", "It is, but it holds the body properly and it also has a strap between the legs, so it doesn't come off over her head. The assistant said it has to be marked for her weight."),
  L("Κώστας", "m", "Εντάξει, πείστηκα. Αλλά να ξέρεις, κανένα σωσίβιο δεν αντικαθιστά τα μάτια μας. Όταν είναι στο νερό, ένας από τους δύο θα είναι πάντα δίπλα της, όχι στην ξαπλώστρα με το κινητό.", "OK, I'm convinced. But you know, no life jacket replaces our eyes. When she's in the water, one of us will always be next to her, not on the sunbed with a phone."),
  L("Νίκη", "f", "Συμφωνώ. Και του χρόνου μαθήματα κολύμβησης.", "Agreed. And next year swimming lessons."),
 ],
 "questions": [
  Q("Γιατί η Νίκη δεν θέλει μπρατσάκια;", ["Γιατί είναι πολύ ακριβά", "Γιατί δεν κρατούν το κεφάλι έξω από το νερό αν το παιδί γυρίσει μπρούμυτα", "Γιατί δεν αρέσουν στην κόρη τους", "Γιατί σκίζονται εύκολα"], 1, "Αν το παιδί γυρίσει μπρούμυτα, δεν το κρατούν με το κεφάλι έξω από το νερό"),
  Q("Σε τι χρησιμεύει το λουρί ανάμεσα στα πόδια;", ["Για να μην πνίγεται", "Για να είναι πιο άνετο", "Για να μη βγαίνει το γιλέκο από το κεφάλι", "Για να κρέμεται στην ξαπλώστρα"], 2, "για να μη βγαίνει από το κεφάλι"),
  Q("Τι τονίζει ο Κώστας στο τέλος;", ["Ότι κανένα σωσίβιο δεν αντικαθιστά την προσοχή των γονιών", "Ότι η κόρη τους κολυμπάει ήδη καλά", "Ότι θα πάρουν και τα δύο", "Ότι η θάλασσα είναι επικίνδυνη"], 0, "κανένα σωσίβιο δεν αντικαθιστά τα μάτια μας"),
 ],
 "gloss": {"σωσίβιο": "σωσίβιο — life jacket", "μπρατσάκια": "μπρατσάκια — armbands", "είδη θαλάσσης": "είδη θαλάσσης — beach goods", "μπρούμυτα": "μπρούμυτα — face down", "γλιστρήσουν": "γλιστράω — to slip", "γιλέκο-σωσίβιο": "γιλέκο-σωσίβιο — life vest", "άβολο": "άβολος — uncomfortable", "λουρί": "λουρί — strap", "ένδειξη": "ένδειξη — marking, label", "πείστηκα": "πείθομαι — to be convinced", "αντικαθιστά": "αντικαθιστώ — to replace", "ξαπλώστρα": "ξαπλώστρα — sunbed"},
})

ITEMS.append({
 "id": "l173-mon-kolympi-gia-ti-mitera-mou", "title": "Μαθήματα κολύμβησης για τη μητέρα μου", "title_en": "Swimming lessons for my mother", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να διηγείται πώς έμαθε στη μητέρα της να κολυμπάει στα εβδομήντα.",
 "script": [
  L("Γυναίκα", "f", "Η μητέρα μου μεγάλωσε σε ένα ορεινό χωριό της Ευρυτανίας και είδε τη θάλασσα πρώτη φορά στα είκοσι. Πενήντα χρόνια έμπαινε μόνο ως τη μέση και πανικοβαλλόταν αν τη χτυπούσε κύμα.", "My mother grew up in a mountain village in Evrytania and saw the sea for the first time at twenty. For fifty years she only went in up to her waist and panicked if a wave hit her."),
  L("Γυναίκα", "f", "Πέρσι το καλοκαίρι, στα εβδομήντα της, μου είπε ξαφνικά: «Θέλω να μάθω, πριν να είναι αργά». Αρχίσαμε σε μια ήσυχη παραλία, νωρίς το πρωί, όταν δεν υπήρχε κανείς να μας κοιτάζει.", "Last summer, at seventy, she suddenly told me: 'I want to learn, before it's too late.' We started on a quiet beach, early in the morning, when there was no one to watch us."),
  L("Γυναίκα", "f", "Το πρώτο που μάθαμε δεν ήταν το κολύμπι, αλλά η ανάσα: να βάζει το πρόσωπο στο νερό και να βγάζει φυσαλίδες. Μετά, να επιπλέει ανάσκελα, με το χέρι μου κάτω από την πλάτη της. Τη μέρα που τράβηξα το χέρι χωρίς να το καταλάβει, έμεινε στην επιφάνεια μόνη της.", "The first thing we learned wasn't swimming but breathing: putting her face in the water and blowing bubbles. Then floating on her back, with my hand under her back. The day I pulled my hand away without her noticing, she stayed on the surface by herself."),
  L("Γυναίκα", "f", "Στο τέλος του καλοκαιριού κολύμπησε δέκα μέτρα ως μια σημαδούρα. Δεν ήταν πολύ, αλλά όταν βγήκε, έκλαιγε και γελούσε μαζί. Φέτος λέει ότι θα κολυμπήσει ως τον βράχο.", "At the end of the summer she swam ten metres to a buoy. It wasn't much, but when she came out she was crying and laughing at the same time. This year she says she'll swim to the rock."),
 ],
 "questions": [
  Q("Πώς φερόταν η μητέρα στη θάλασσα πριν από τα μαθήματα;", ["Κολυμπούσε μακριά", "Έμπαινε μόνο ως τη μέση και πανικοβαλλόταν με τα κύματα", "Δεν πήγαινε ποτέ στη θάλασσα", "Έκανε μόνο βουτιές"], 1, "έμπαινε μόνο ως τη μέση"),
  Q("Ποιο ήταν το πρώτο που έμαθε;", ["Να κολυμπάει πρόσθιο", "Να βουτάει από τον βράχο", "Να βάζει το πρόσωπο στο νερό και να βγάζει φυσαλίδες", "Να φοράει μάσκα"], 2, "να βάζει το πρόσωπο στο νερό και να βγάζει φυσαλίδες"),
  Q("Τι πέτυχε στο τέλος του καλοκαιριού;", ["Κολύμπησε δέκα μέτρα ως μια σημαδούρα", "Κολύμπησε ως τον βράχο", "Έμαθε να κάνει καταδύσεις", "Κέρδισε έναν αγώνα"], 0, "κολύμπησε δέκα μέτρα ως μια σημαδούρα"),
 ],
 "gloss": {"ορεινό": "ορεινός — mountain (adj.)", "πανικοβαλλόταν": "πανικοβάλλομαι — to panic", "κύμα": "κύμα — wave", "ανάσα": "ανάσα — breath", "φυσαλίδες": "φυσαλίδα — bubble", "επιπλέει": "επιπλέω — to float", "ανάσκελα": "ανάσκελα — on one's back", "επιφάνεια": "επιφάνεια — surface", "σημαδούρα": "σημαδούρα — buoy", "βράχο": "βράχος — rock"},
})

ITEMS.append({
 "id": "l173-vm-mixanikos-rogmes", "title": "Μήνυμα από τον μηχανικό για τις ρωγμές", "title_en": "A message from the engineer about the cracks", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από έναν πολιτικό μηχανικό που ήρθε να δει τις ρωγμές στον τοίχο του σπιτιού σας.",
 "script": [
  L("Μηχανικός", "m", "Καλημέρα, κυρία Παπαδάκη, ο Στάθης ο μηχανικός. Σας τηλεφωνώ για τις ρωγμές που είδαμε χθες στο σαλόνι. Τις κοίταξα ξανά στις φωτογραφίες, και έχω καλά νέα: είναι στον σοβά, όχι στο μπετό.", "Good morning, Mrs Papadaki, it's Stathis the engineer. I'm calling about the cracks we saw yesterday in the living room. I looked at them again in the photos, and I have good news: they're in the plaster, not in the concrete."),
  L("Μηχανικός", "m", "Πιθανότατα οφείλονται στην υγρασία και στις αλλαγές της θερμοκρασίας, όχι σε κάποιο πρόβλημα του κτιρίου. Για σιγουριά, όμως, θα σας πρότεινα να κολλήσουμε δύο μικρά γυάλινα σημάδια πάνω στις ρωγμές. Αν σε δύο μήνες είναι ακόμα ακέραια, σημαίνει ότι οι ρωγμές δεν μεγαλώνουν.", "They're most likely due to damp and temperature changes, not to a structural problem. To be sure, though, I'd suggest we stick two small glass markers over the cracks. If in two months they're still intact, it means the cracks aren't growing."),
  L("Μηχανικός", "m", "Μπορώ να περάσω την Πέμπτη το απόγευμα για να τα βάλω. Μέχρι τότε μην βάψετε τον τοίχο, γιατί θα κρύψετε τις ρωγμές και δεν θα μπορούμε να τις παρακολουθήσουμε. Πείτε μου αν σας βολεύει.", "I can come by on Thursday afternoon to put them on. Until then don't paint the wall, because you'll hide the cracks and we won't be able to monitor them. Let me know if that suits you."),
 ],
 "questions": [
  Q("Τι διαπίστωσε ο μηχανικός για τις ρωγμές;", ["Ότι είναι στο μπετό και είναι επικίνδυνες", "Ότι είναι στον σοβά, όχι στο μπετό", "Ότι οφείλονται σε σεισμό", "Ότι πρέπει να γκρεμιστεί ο τοίχος"], 1, "είναι στον σοβά, όχι στο μπετό"),
  Q("Σε τι θα χρησιμεύσουν τα γυάλινα σημάδια;", ["Να στολίσουν τον τοίχο", "Να σταματήσουν την υγρασία", "Να δείξουν αν οι ρωγμές μεγαλώνουν", "Να κλείσουν τις ρωγμές"], 2, "σημαίνει ότι οι ρωγμές δεν μεγαλώνουν"),
  Q("Τι δεν πρέπει να κάνει η κυρία Παπαδάκη μέχρι την Πέμπτη;", ["Να βάψει τον τοίχο", "Να ανοίξει τα παράθυρα", "Να μπει στο σαλόνι", "Να ανάψει το καλοριφέρ"], 0, "μην βάψετε τον τοίχο"),
 ],
 "gloss": {"πολιτικό μηχανικό": "πολιτικός μηχανικός — civil engineer", "ρωγμές": "ρωγμή — crack", "σοβά": "σοβάς — plaster", "μπετό": "μπετό — concrete", "υγρασία": "υγρασία — damp, humidity", "σιγουριά": "σιγουριά — certainty", "ακέραια": "ακέραιος — intact", "παρακολουθήσουμε": "παρακολουθώ — to monitor", "βολεύει": "βολεύω — to suit"},
})

ITEMS.append({
 "id": "l173-vm-tavli-tournoua", "title": "Μήνυμα για το τουρνουά τάβλι του καφενείου", "title_en": "A message about the café backgammon tournament", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον ιδιοκτήτη του καφενείου της γειτονιάς σας.",
 "script": [
  L("Καφετζής", "m", "Γεια σου, Περικλή, ο Θανάσης από το καφενείο. Σε παίρνω για το τουρνουά τάβλι του Σαββάτου. Γράφτηκαν τριάντα δύο παίκτες, οπότε θα αρχίσουμε νωρίτερα, στις δέκα το πρωί αντί για τις δώδεκα.", "Hi, Pericles, it's Thanasis from the café. I'm calling about Saturday's backgammon tournament. Thirty-two players signed up, so we'll start earlier, at ten in the morning instead of twelve."),
  L("Θανάσης", "m", "Θα παίξουμε και τα τρία παιχνίδια, πόρτες, πλακωτό και φεύγα, και κερδίζει όποιος φτάσει πρώτος τους πέντε πόντους. Τα ζάρια τα δίνουμε εμείς, για να μην έχουμε φασαρίες σαν πέρσι.", "We'll play all three games, portes, plakoto and fevga, and whoever reaches five points first wins. We provide the dice, so we don't have rows like last year."),
  L("Θανάσης", "m", "Το έπαθλο είναι ένα ξύλινο τάβλι με σκαλιστά λουλούδια, που το έφτιαξε ένας μάστορας από τη Ζαγορά. Και κάτι ακόμα: αν δεν μπορείς να έρθεις, πες μου μέχρι την Πέμπτη, γιατί έχω τρεις στη λίστα αναμονής.", "The prize is a wooden backgammon board with carved flowers, made by a craftsman from Zagora. And one more thing: if you can't come, tell me by Thursday, because I have three people on the waiting list."),
 ],
 "questions": [
  Q("Γιατί το τουρνουά θα αρχίσει νωρίτερα;", ["Γιατί το καφενείο κλείνει νωρίς", "Γιατί γράφτηκαν πολλοί παίκτες", "Γιατί θα βρέξει το απόγευμα", "Γιατί υπάρχει αγώνας ποδοσφαίρου"], 1, "Γράφτηκαν τριάντα δύο παίκτες, οπότε θα αρχίσουμε νωρίτερα"),
  Q("Γιατί θα δίνει τα ζάρια το καφενείο;", ["Γιατί οι παίκτες τα ξεχνούν", "Για να είναι όλα ίδια στις φωτογραφίες", "Για να μην υπάρξουν φασαρίες όπως πέρσι", "Γιατί είναι καινούργια"], 2, "για να μην έχουμε φασαρίες σαν πέρσι"),
  Q("Τι πρέπει να κάνει ο Περικλής αν δεν μπορεί να έρθει;", ["Να το πει μέχρι την Πέμπτη", "Να στείλει κάποιον άλλον", "Να πληρώσει πρόστιμο", "Να φέρει δικό του τάβλι"], 0, "πες μου μέχρι την Πέμπτη"),
 ],
 "gloss": {"καφενείου": "καφενείο — traditional café", "τουρνουά": "τουρνουά — tournament", "τάβλι": "τάβλι — backgammon", "παίκτες": "παίκτης — player", "πόρτες": "πόρτες — portes (a backgammon game)", "πλακωτό": "πλακωτό — plakoto (a backgammon game)", "φεύγα": "φεύγα — fevga (a backgammon game)", "πόντους": "πόντος — point", "ζάρια": "ζάρι — die (dice)", "φασαρίες": "φασαρία — fuss, row", "έπαθλο": "έπαθλο — prize", "σκαλιστά": "σκαλιστός — carved", "λίστα αναμονής": "λίστα αναμονής — waiting list"},
})

ITEMS.append({
 "id": "l173-c1-giati-idronoume", "title": "Γιατί ιδρώνουμε", "title_en": "Why we sweat", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε επιστημονική εκπομπή με έναν φυσιολόγο για τον ιδρώτα.",
 "script": [
  L("Παρουσιάστρια", "f", "Ο ιδρώτας μάς φαίνεται ενοχλητικός. Τι ρόλο παίζει στην πραγματικότητα;", "Sweat seems annoying to us. What role does it actually play?"),
  L("Φυσιολόγος", "m", "Είναι ένα από τα πιο αποτελεσματικά συστήματα ψύξης στη φύση. Όταν η θερμοκρασία του σώματος ανεβαίνει, ο εγκέφαλος στέλνει σήμα σε εκατομμύρια ιδρωτοποιούς αδένες στο δέρμα. Ο ιδρώτας βγαίνει στην επιφάνεια και, καθώς εξατμίζεται, παίρνει μαζί του θερμότητα. Δεν μας δροσίζει, λοιπόν, ο ίδιος ο ιδρώτας, αλλά η εξάτμισή του.", "It's one of the most efficient cooling systems in nature. When body temperature rises, the brain sends a signal to millions of sweat glands in the skin. Sweat comes to the surface and, as it evaporates, takes heat with it. So it isn't the sweat itself that cools us, but its evaporation."),
  L("Παρουσιάστρια", "f", "Γι' αυτό η υγρασία είναι τόσο αφόρητη;", "Is that why humidity is so unbearable?"),
  L("Φυσιολόγος", "m", "Ακριβώς. Όταν ο αέρας είναι ήδη κορεσμένος με υδρατμούς, ο ιδρώτας δεν εξατμίζεται εύκολα. Τρέχει στο δέρμα, μας μουσκεύει, αλλά δεν μας δροσίζει. Γι' αυτό τριάντα πέντε βαθμοί με ξηρό αέρα είναι πιο υποφερτοί από τριάντα με πολλή υγρασία.", "Exactly. When the air is already saturated with water vapour, sweat doesn't evaporate easily. It runs down the skin, soaks us, but doesn't cool us. That's why thirty-five degrees in dry air is more bearable than thirty with a lot of humidity."),
  L("Παρουσιάστρια", "f", "Και η μυρωδιά;", "And the smell?"),
  L("Φυσιολόγος", "m", "Εδώ υπάρχει μια παρεξήγηση. Ο φρέσκος ιδρώτας είναι σχεδόν άοσμος. Τη μυρωδιά την προκαλούν τα βακτήρια του δέρματος, που διασπούν ορισμένες ουσίες του ιδρώτα, κυρίως στις μασχάλες, όπου υπάρχει ένας άλλος τύπος αδένων. Και κάτι ακόμη: όσο πιο γυμνασμένος είναι κανείς, τόσο πιο νωρίς αρχίζει να ιδρώνει. Δεν είναι αδυναμία· είναι ένδειξη ότι το σύστημα ψύξης έχει εκπαιδευτεί.", "Here there's a misunderstanding. Fresh sweat is almost odourless. The smell is caused by skin bacteria, which break down certain substances in sweat, mainly in the armpits, where there's another type of gland. And one more thing: the fitter one is, the earlier one starts to sweat. It's not a weakness; it's a sign that the cooling system has been trained."),
 ],
 "questions": [
  Q("Τι ακριβώς μας δροσίζει σύμφωνα με τον φυσιολόγο;", ["Ο ίδιος ο ιδρώτας", "Η εξάτμιση του ιδρώτα", "Το αλάτι του ιδρώτα", "Ο αέρας που φυσάει"], 1, "Δεν μας δροσίζει, λοιπόν, ο ίδιος ο ιδρώτας, αλλά η εξάτμισή του"),
  Q("Τι προκαλεί τη μυρωδιά του ιδρώτα;", ["Ο φρέσκος ιδρώτας", "Η ζέστη", "Τα βακτήρια του δέρματος", "Το φαγητό"], 2, "Τη μυρωδιά την προκαλούν τα βακτήρια του δέρματος"),
  Q("Τι δείχνει το ότι ένας γυμνασμένος άνθρωπος ιδρώνει νωρίτερα;", ["Ότι το σύστημα ψύξης του έχει εκπαιδευτεί", "Ότι είναι κουρασμένος", "Ότι πίνει πολύ νερό", "Ότι είναι άρρωστος"], 0, "είναι ένδειξη ότι το σύστημα ψύξης έχει εκπαιδευτεί"),
 ],
 "gloss": {"φυσιολόγο": "φυσιολόγος — physiologist", "ιδρώτα": "ιδρώτας — sweat", "ψύξης": "ψύξη — cooling", "ιδρωτοποιούς αδένες": "ιδρωτοποιός αδένας — sweat gland", "εξατμίζεται": "εξατμίζομαι — to evaporate", "θερμότητα": "θερμότητα — heat", "εξάτμισή": "εξάτμιση — evaporation", "αφόρητη": "αφόρητος — unbearable", "κορεσμένος": "κορεσμένος — saturated", "υδρατμούς": "υδρατμός — water vapour", "υποφερτοί": "υποφερτός — bearable", "παρεξήγηση": "παρεξήγηση — misunderstanding", "άοσμος": "άοσμος — odourless", "διασπούν": "διασπώ — to break down", "μασχάλες": "μασχάλη — armpit", "γυμνασμένος": "γυμνασμένος — fit"},
})

ITEMS.append({
 "id": "l173-c1-pos-mas-xypna-i-kafeini", "title": "Πώς μας ξυπνά η καφεΐνη", "title_en": "How caffeine wakes us up", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια φαρμακολόγο σε μια ομιλία για το πώς δρα η καφεΐνη στον εγκέφαλο.",
 "script": [
  L("Φαρμακολόγος", "f", "Όσο είμαστε ξύπνιοι, στον εγκέφαλό μας συσσωρεύεται σιγά σιγά μια ουσία που λέγεται αδενοσίνη. Όσο περισσότερη αδενοσίνη μαζεύεται, τόσο πιο νυσταγμένοι νιώθουμε. Είναι, θα λέγαμε, ένα εσωτερικό μέτρο της κούρασης.", "As long as we are awake, a substance called adenosine slowly builds up in our brain. The more adenosine accumulates, the sleepier we feel. It is, one might say, an internal measure of tiredness."),
  L("Φαρμακολόγος", "f", "Η καφεΐνη μοιάζει χημικά με την αδενοσίνη. Έτσι, πιάνει τη θέση της στους υποδοχείς των νευρικών κυττάρων, χωρίς όμως να στέλνει το μήνυμα της κούρασης. Η καφεΐνη, με άλλα λόγια, δεν μας δίνει ενέργεια· απλώς εμποδίζει τον εγκέφαλο να καταλάβει πόσο κουρασμένος είναι.", "Caffeine resembles adenosine chemically. So it takes its place on the receptors of nerve cells, but without sending the message of tiredness. Caffeine, in other words, doesn't give us energy; it simply prevents the brain from realising how tired it is."),
  L("Φαρμακολόγος", "f", "Γι' αυτό, όταν η δράση της περάσει, η αδενοσίνη που περίμενε στην ουρά βρίσκει ξαφνικά ελεύθερους τους υποδοχείς, και η κούραση επιστρέφει απότομα. Ο χρόνος ημιζωής της καφεΐνης στους ενήλικες είναι κατά μέσο όρο γύρω στις πέντε ώρες, με μεγάλες διαφορές από άνθρωπο σε άνθρωπο. Ένας καφές στις πέντε το απόγευμα, λοιπόν, βρίσκεται ακόμη κατά το ήμισυ στον οργανισμό μας στις δέκα το βράδυ.", "That's why, when its effect wears off, the adenosine that was waiting in the queue suddenly finds the receptors free, and tiredness returns abruptly. The half-life of caffeine in adults is on average around five hours, with large differences from person to person. So a coffee at five in the afternoon is still half in our body at ten at night."),
  L("Φαρμακολόγος", "f", "Όσοι πίνουν καφέ κάθε μέρα αναπτύσσουν ανοχή: ο εγκέφαλος φτιάχνει περισσότερους υποδοχείς, και χρειάζεται περισσότερη καφεΐνη για το ίδιο αποτέλεσμα. Γι' αυτό ο πονοκέφαλος της πρώτης μέρας χωρίς καφέ δεν είναι φαντασία· είναι ο εγκέφαλος που προσαρμόζεται ξανά.", "Those who drink coffee every day develop tolerance: the brain makes more receptors, and more caffeine is needed for the same result. That's why the headache on the first day without coffee isn't imaginary; it's the brain readjusting."),
 ],
 "questions": [
  Q("Τι κάνει, σύμφωνα με τη φαρμακολόγο, η καφεΐνη;", ["Μας δίνει περισσότερη ενέργεια", "Εμποδίζει τον εγκέφαλο να καταλάβει πόσο κουρασμένος είναι", "Καταστρέφει την αδενοσίνη", "Αυξάνει τη ροή του αίματος"], 1, "απλώς εμποδίζει τον εγκέφαλο να καταλάβει πόσο κουρασμένος είναι"),
  Q("Γιατί η κούραση επιστρέφει απότομα όταν περάσει η δράση της καφεΐνης;", ["Γιατί η καφεΐνη προκαλεί υπνηλία", "Γιατί πίνουμε λιγότερο νερό", "Γιατί η αδενοσίνη που περίμενε βρίσκει ελεύθερους τους υποδοχείς", "Γιατί πέφτει το σάκχαρο"], 2, "η αδενοσίνη που περίμενε στην ουρά βρίσκει ξαφνικά ελεύθερους τους υποδοχείς"),
  Q("Πώς εξηγεί τον πονοκέφαλο της πρώτης μέρας χωρίς καφέ;", ["Ο εγκέφαλος προσαρμόζεται ξανά, αφού έχει φτιάξει περισσότερους υποδοχείς", "Είναι φαντασία", "Οφείλεται στην αφυδάτωση", "Οφείλεται στην έλλειψη ζάχαρης"], 0, "είναι ο εγκέφαλος που προσαρμόζεται ξανά"),
 ],
 "gloss": {"φαρμακολόγο": "φαρμακολόγος — pharmacologist", "καφεΐνη": "καφεΐνη — caffeine", "συσσωρεύεται": "συσσωρεύομαι — to build up", "αδενοσίνη": "αδενοσίνη — adenosine", "νυσταγμένοι": "νυσταγμένος — sleepy", "υποδοχείς": "υποδοχέας — receptor", "νευρικών κυττάρων": "νευρικό κύτταρο — nerve cell", "δράση": "δράση — effect, action", "χρόνος ημιζωής": "χρόνος ημιζωής — half-life", "κατά το ήμισυ": "κατά το ήμισυ — by half", "οργανισμό": "οργανισμός — body, organism", "ανοχή": "ανοχή — tolerance", "προσαρμόζεται": "προσαρμόζομαι — to adapt"},
})

rnd = random.Random(173)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-173.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
