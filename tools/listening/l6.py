# Source for library/listening/listening-6.json: ten B2 listening items (script + questions + gloss).
# Build: python3 tools/listening/l6.py  (writes the JSON; checks that every answer is one of its options).
import json, os

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why):
    assert opts[ans] if isinstance(ans, int) else ans in opts
    a = opts[ans] if isinstance(ans, int) else ans
    return {"q": q, "options": opts, "answer": a, "why": why}

ITEMS = []

ITEMS.append({
 "id": "l6-ann-ktel", "title": "Αλλαγή διαδρομής στο ΚΤΕΛ", "title_en": "A route change at the coach station", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα ενός σταθμού υπεραστικών λεωφορείων.",
 "script": [
  L("Εκφωνητής", "m", "Παρακαλείται το επιβατικό κοινό να προσέξει την παρακάτω ανακοίνωση.", "Passengers are kindly asked to pay attention to the following announcement."),
  L("Εκφωνητής", "m", "Λόγω εργασιών στην εθνική οδό, τα δρομολόγια προς Ναύπλιο θα ακολουθούν από σήμερα και για τις επόμενες δύο εβδομάδες την παλιά επαρχιακή οδό. Η διάρκεια του ταξιδιού αναμένεται να αυξηθεί κατά είκοσι περίπου λεπτά.", "Because of roadworks on the motorway, services to Nafplio will use the old provincial road from today and for the next two weeks. The journey is expected to take about twenty minutes longer."),
  L("Εκφωνητής", "m", "Επίσης, το δρομολόγιο των έντεκα και μισή καταργείται προσωρινά. Οι επιβάτες που έχουν ήδη εισιτήριο για αυτό μπορούν να ταξιδέψουν με το λεωφορείο των δώδεκα χωρίς επιπλέον χρέωση.", "Also, the half past eleven service is temporarily cancelled. Passengers who already have a ticket for it may travel on the twelve o'clock coach at no extra charge."),
  L("Εκφωνητής", "m", "Για αλλαγή ή επιστροφή εισιτηρίου απευθυνθείτε στο εκδοτήριο νούμερο τρία. Ευχαριστούμε για την κατανόηση και σας ευχόμαστε καλό ταξίδι.", "To change or refund a ticket, please go to ticket window number three. Thank you for your understanding and have a good journey."),
 ],
 "questions": [
  Q("Γιατί αλλάζει η διαδρομή των λεωφορείων;", ["Γίνονται έργα στην εθνική οδό", "Έχει χιονίσει στο βουνό", "Υπάρχει απεργία των οδηγών", "Το Ναύπλιο έχει κλειστή είσοδο"], 0, "Λόγω εργασιών στην εθνική οδό"),
  Q("Τι θα γίνει με τη διάρκεια του ταξιδιού;", ["Θα μειωθεί κατά είκοσι λεπτά", "Θα μείνει η ίδια", "Θα αυξηθεί κατά είκοσι λεπτά περίπου", "Θα διπλασιαστεί"], 2, "Η διάρκεια του ταξιδιού αναμένεται να αυξηθεί κατά είκοσι περίπου λεπτά."),
  Q("Τι μπορούν να κάνουν όσοι έχουν εισιτήριο για τις 11:30;", ["Να πάρουν πίσω διπλάσια χρήματα", "Να ταξιδέψουν με το λεωφορείο των 12:00 χωρίς να πληρώσουν κάτι παραπάνω", "Να ταξιδέψουν μόνο την επόμενη μέρα", "Να πάρουν ταξί με έξοδα της εταιρείας"], 1, "μπορούν να ταξιδέψουν με το λεωφορείο των δώδεκα χωρίς επιπλέον χρέωση"),
 ],
 "gloss": {"επιβατικό κοινό": "επιβατικό κοινό — the travelling public, passengers", "εργασιών": "εργασίες — (road)works", "επαρχιακή οδό": "επαρχιακή οδός — provincial (secondary) road", "αναμένεται": "αναμένομαι — to be expected", "καταργείται": "καταργούμαι — to be cancelled, abolished", "προσωρινά": "προσωρινά — temporarily", "χρέωση": "χρέωση — charge", "εκδοτήριο": "εκδοτήριο — ticket office, ticket window"},
})

ITEMS.append({
 "id": "l6-vm-odontiatros", "title": "Μήνυμα από το οδοντιατρείο", "title_en": "A message from the dentist's", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα που άφησε η γραμματέας ενός οδοντιατρείου στον τηλεφωνητή μιας ασθενούς.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα σας, κυρία Ζαχαρίου, σας τηλεφωνώ από το οδοντιατρείο του κυρίου Μπαλτά.", "Good morning, Ms Zachariou, I'm calling from Mr Baltas's dental practice."),
  L("Γραμματέας", "f", "Δυστυχώς ο γιατρός θα λείπει σε συνέδριο την Τετάρτη, οπότε το ραντεβού σας για το σφράγισμα πρέπει να μετατεθεί. Μπορούμε να σας εξυπηρετήσουμε είτε την Πέμπτη στις έξι το απόγευμα είτε τη Δευτέρα στις δέκα το πρωί.", "Unfortunately the dentist will be away at a conference on Wednesday, so your appointment for the filling has to be moved. We can see you either on Thursday at six in the evening or on Monday at ten in the morning."),
  L("Γραμματέας", "f", "Αν σας βολεύει, φέρτε μαζί σας και την πανοραμική ακτινογραφία που κάνατε τον Μάρτιο, για να μη χρειαστεί να την ξανακάνετε.", "If it suits you, bring along the panoramic X-ray you had in March as well, so that you won't need to have it done again."),
  L("Γραμματέας", "f", "Θα είμαι στο ιατρείο μέχρι τις δύο. Μπορείτε να με πάρετε στο σταθερό ή να μου στείλετε μήνυμα. Ευχαριστώ πολύ και συγγνώμη για την αναστάτωση.", "I'll be at the practice until two. You can ring me on the landline or send me a message. Thank you very much, and sorry for the inconvenience."),
 ],
 "questions": [
  Q("Γιατί πρέπει να αλλάξει το ραντεβού;", ["Ο οδοντίατρος θα είναι σε συνέδριο", "Το ιατρείο θα κάνει ανακαίνιση", "Η ασθενής το ζήτησε", "Ο οδοντίατρος είναι άρρωστος"], 0, "ο γιατρός θα λείπει σε συνέδριο την Τετάρτη"),
  Q("Ποια νέα ραντεβού προτείνει η γραμματέας;", ["Τετάρτη απόγευμα ή Πέμπτη πρωί", "Πέμπτη απόγευμα ή Δευτέρα πρωί", "Μόνο Δευτέρα απόγευμα", "Παρασκευή πρωί ή Σάββατο"], 1, "είτε την Πέμπτη στις έξι το απόγευμα είτε τη Δευτέρα στις δέκα το πρωί"),
  Q("Γιατί να φέρει η ασθενής την ακτινογραφία;", ["Για να την πάρει πίσω ο γιατρός", "Γιατί τη ζητά η ασφάλεια", "Για να μη χρειαστεί νέα ακτινογραφία", "Για να δει αν έγινε σωστά το σφράγισμα"], 2, "για να μη χρειαστεί να την ξανακάνετε"),
 ],
 "gloss": {"σφράγισμα": "σφράγισμα — (tooth) filling", "μετατεθεί": "μετατίθεμαι — to be moved, rescheduled", "εξυπηρετήσουμε": "εξυπηρετώ — to serve, see (a client)", "σας βολεύει": "με βολεύει — it suits me, it's convenient for me", "ακτινογραφία": "ακτινογραφία — X-ray", "σταθερό": "σταθερό (τηλέφωνο) — landline", "αναστάτωση": "αναστάτωση — disruption, inconvenience"},
})

ITEMS.append({
 "id": "l6-dia-enoikio", "title": "Ο ιδιοκτήτης και το νοίκι", "title_en": "The landlord and the rent", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση ανάμεσα σε μια ενοικιάστρια, τη Μυρτώ, και τον ιδιοκτήτη του διαμερίσματός της, τον κύριο Αποστόλου.",
 "script": [
  L("Κύριος Αποστόλου", "m", "Μυρτώ, σε πήρα γιατί λήγει το συμβόλαιο τον Σεπτέμβριο και ήθελα να το συζητήσουμε από τώρα. Όπως ξέρεις, όλα έχουν ακριβύνει. Σκέφτομαι να ανεβάσω το νοίκι στα πεντακόσια πενήντα.", "Myrto, I called you because the lease ends in September and I wanted us to discuss it now. As you know, everything has got more expensive. I'm thinking of raising the rent to five hundred and fifty."),
  L("Μυρτώ", "f", "Από τετρακόσια ογδόντα; Κύριε Αποστόλου, αυτό είναι σχεδόν δεκαπέντε τοις εκατό. Και να σας θυμίσω ότι ο θερμοσίφωνας χαλάει κάθε δυο μήνες και η μπαλκονόπορτα δεν κλείνει καλά από πέρσι τον χειμώνα.", "From four hundred and eighty? Mr Apostolou, that's almost fifteen per cent. And may I remind you that the water heater breaks down every couple of months and the balcony door hasn't closed properly since last winter."),
  L("Κύριος Αποστόλου", "m", "Έχεις δίκιο για την μπαλκονόπορτα, το παραδέχομαι. Θα στείλω τον μάστορα την άλλη εβδομάδα. Αλλά καταλαβαίνεις, κι εγώ πληρώνω φόρους, κοινόχρηστα για τον ακάλυπτο, ασφάλεια…", "You're right about the balcony door, I admit it. I'll send the handyman next week. But you understand, I pay taxes too, shared costs for the courtyard, insurance…"),
  L("Μυρτώ", "f", "Το καταλαβαίνω. Να σας κάνω μια πρόταση; Αν αλλάξετε τον θερμοσίφωνα και φτιάξετε την πόρτα πριν από την ανανέωση, δέχομαι να πάμε στα πεντακόσια είκοσι. Και υπογράφουμε για τρία χρόνια, για να είστε κι εσείς σίγουρος.", "I understand. Can I make you a proposal? If you replace the water heater and fix the door before the renewal, I'll agree to go to five hundred and twenty. And we sign for three years, so that you can feel secure too."),
  L("Κύριος Αποστόλου", "m", "Τρία χρόνια… Δεν είναι κακή ιδέα. Ένας σταθερός ενοικιαστής που πληρώνει στην ώρα του αξίζει κάτι. Άσε με να το σκεφτώ μέχρι την Παρασκευή και θα σου πω.", "Three years… That's not a bad idea. A stable tenant who pays on time is worth something. Let me think it over until Friday and I'll let you know."),
  L("Μυρτώ", "f", "Εντάξει. Αλλά το θέμα με τον θερμοσίφωνα δεν μπορεί να περιμένει την Παρασκευή, ειλικρινά. Σήμερα το πρωί έκανα μπάνιο με κρύο νερό.", "All right. But the water heater can't wait until Friday, honestly. This morning I had a cold shower."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί ο κύριος Αποστόλου;", ["Για να ζητήσει από τη Μυρτώ να φύγει", "Για να συζητήσουν το νέο ενοίκιο πριν λήξει το συμβόλαιο", "Για να της πει ότι πουλάει το διαμέρισμα", "Για να παραπονεθεί για θόρυβο"], 1, "λήγει το συμβόλαιο τον Σεπτέμβριο και ήθελα να το συζητήσουμε από τώρα ... να ανεβάσω το νοίκι"),
  Q("Ποιο επιχείρημα χρησιμοποιεί πρώτα η Μυρτώ;", ["Ότι το διαμέρισμα έχει προβλήματα που δεν έχουν διορθωθεί", "Ότι βρήκε φθηνότερο σπίτι", "Ότι έχασε τη δουλειά της", "Ότι τα ενοίκια στη γειτονιά έπεσαν"], 0, "ο θερμοσίφωνας χαλάει κάθε δυο μήνες και η μπαλκονόπορτα δεν κλείνει καλά"),
  Q("Τι προτείνει η Μυρτώ;", ["Να μείνει το ενοίκιο ίδιο για πάντα", "Να πληρώνει 550 € αλλά να φτιάξει εκείνη τις βλάβες", "520 € και συμβόλαιο τριών χρόνων, αν γίνουν πρώτα οι επισκευές", "Να πληρώνει κάθε τρεις μήνες αντί για κάθε μήνα"], 2, "Αν αλλάξετε τον θερμοσίφωνα και φτιάξετε την πόρτα πριν από την ανανέωση, δέχομαι να πάμε στα πεντακόσια είκοσι. Και υπογράφουμε για τρία χρόνια"),
  Q("Πώς αντιδρά ο ιδιοκτήτης στην πρόταση;", ["Την απορρίπτει αμέσως", "Τη δέχεται αμέσως", "Τη βρίσκει ενδιαφέρουσα και θέλει χρόνο να σκεφτεί", "Ζητά να μιλήσει με δικηγόρο"], 2, "Δεν είναι κακή ιδέα ... Άσε με να το σκεφτώ μέχρι την Παρασκευή"),
  Q("Γιατί η Μυρτώ επιμένει στο τέλος;", ["Γιατί ο θερμοσίφωνας πρέπει να επισκευαστεί αμέσως", "Γιατί θέλει απάντηση για το ενοίκιο σήμερα", "Γιατί φεύγει διακοπές την Παρασκευή", "Γιατί ο μάστορας δεν ήρθε ποτέ"], 0, "το θέμα με τον θερμοσίφωνα δεν μπορεί να περιμένει την Παρασκευή"),
 ],
 "gloss": {"λήγει": "λήγω — to expire, end", "συμβόλαιο": "συμβόλαιο — contract, lease", "νοίκι": "νοίκι (ενοίκιο) — rent", "θερμοσίφωνας": "θερμοσίφωνας — (electric) water heater", "μπαλκονόπορτα": "μπαλκονόπορτα — balcony door", "παραδέχομαι": "παραδέχομαι — to admit", "μάστορα": "μάστορας — handyman, craftsman", "κοινόχρηστα": "κοινόχρηστα — shared building costs", "ακάλυπτο": "ακάλυπτος — the open courtyard behind a block of flats", "ανανέωση": "ανανέωση — renewal", "στην ώρα του": "στην ώρα του — on time"},
})

ITEMS.append({
 "id": "l6-int-navagosostis", "title": "Ναυαγοσώστρια σε πολυσύχναστη παραλία", "title_en": "A lifeguard on a busy beach", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με τη Δέσποινα, που δουλεύει κάθε καλοκαίρι ως ναυαγοσώστρια σε μια παραλία της Χαλκιδικής.",
 "script": [
  L("Δημοσιογράφος", "m", "Δέσποινα, πόσα καλοκαίρια κάθεσαι σε αυτόν τον πύργο παρατήρησης;", "Despoina, how many summers have you been sitting in this lookout tower?"),
  L("Δέσποινα", "f", "Έξι. Ξεκίνησα όταν ήμουν φοιτήτρια στη Γυμναστική Ακαδημία, για να βγάλω κάποια χρήματα, και τελικά μου έγινε πάθος. Τον χειμώνα είμαι προπονήτρια κολύμβησης.", "Six. I started when I was a student at the sports academy, to earn some money, and in the end it became a passion. In winter I'm a swimming coach."),
  L("Δημοσιογράφος", "m", "Οι περισσότεροι φαντάζονται ότι η δουλειά σου είναι κυρίως ήλιος και θάλασσα.", "Most people imagine your job is mainly sun and sea."),
  L("Δέσποινα", "f", "Ναι, αυτό ακούω συνέχεια. Στην πραγματικότητα, είμαι οκτώ ώρες συγκεντρωμένη και δεν επιτρέπεται να κοιτάξω ούτε το κινητό. Ένας άνθρωπος που πνίγεται σπάνια φωνάζει ή κουνάει τα χέρια, όπως στις ταινίες. Συνήθως απλώς βουλιάζει αθόρυβα. Αν χαθείς για ένα λεπτό, μπορεί να είναι αργά.", "Yes, I hear that all the time. In reality I'm concentrating for eight hours and I'm not allowed to look even at my phone. A person who is drowning rarely shouts or waves their arms, as in the films. Usually they just sink silently. If you lose focus for a minute, it may be too late."),
  L("Δημοσιογράφος", "m", "Ποια είναι τα πιο συνηθισμένα περιστατικά;", "What are the most common incidents?"),
  L("Δέσποινα", "f", "Όχι τόσο οι πνιγμοί, ευτυχώς. Είναι παιδιά που χάνονται στην παραλία, τσιμπήματα από μέδουσες, άνθρωποι που κολυμπούν αμέσως μετά το φαγητό και παθαίνουν κράμπα, και πολλοί που ανοίγονται πολύ με το στρώμα και τους παίρνει ο αέρας.", "Not drownings so much, luckily. It's children who get lost on the beach, jellyfish stings, people who swim straight after eating and get cramp, and lots who go out too far on an inflatable and get carried off by the wind."),
  L("Δημοσιογράφος", "m", "Αν είχες να δώσεις μία συμβουλή στους λουόμενους;", "If you had to give bathers one piece of advice?"),
  L("Δέσποινα", "f", "Να κοιτάνε τη σημαία. Όταν είναι κόκκινη, δεν είναι για να μας χαλάσει τη μέρα. Σημαίνει ότι υπάρχουν ρεύματα που δεν φαίνονται από την ακτή.", "To look at the flag. When it's red, it's not there to ruin our day. It means there are currents you can't see from the shore."),
 ],
 "questions": [
  Q("Τι κάνει η Δέσποινα τον χειμώνα;", ["Σπουδάζει στη Γυμναστική Ακαδημία", "Προπονεί κολυμβητές", "Δουλεύει σε ξενοδοχείο", "Ξεκουράζεται"], 1, "Τον χειμώνα είμαι προπονήτρια κολύμβησης."),
  Q("Τι λέει για τους ανθρώπους που πνίγονται;", ["Φωνάζουν πάντα για βοήθεια", "Συνήθως κουνάνε τα χέρια τους", "Συχνά βουλιάζουν χωρίς να κάνουν θόρυβο", "Είναι κυρίως παιδιά"], 2, "Ένας άνθρωπος που πνίγεται σπάνια φωνάζει ή κουνάει τα χέρια ... Συνήθως απλώς βουλιάζει αθόρυβα."),
  Q("Ποιο από τα παρακάτω ΔΕΝ αναφέρει ως συνηθισμένο περιστατικό;", ["Παιδιά που χάνονται", "Τσιμπήματα από μέδουσες", "Ηλίαση", "Λουόμενους που τους παρασύρει ο αέρας με το στρώμα"], 2, "Αναφέρει χαμένα παιδιά, μέδουσες, κράμπες και στρώματα, όχι ηλίαση."),
  Q("Τι σημαίνει, κατά τη Δέσποινα, η κόκκινη σημαία;", ["Ότι η παραλία είναι γεμάτη", "Ότι υπάρχουν επικίνδυνα ρεύματα", "Ότι ο ναυαγοσώστης κάνει διάλειμμα", "Ότι έχει μέδουσες"], 1, "Σημαίνει ότι υπάρχουν ρεύματα που δεν φαίνονται από την ακτή."),
 ],
 "gloss": {"ναυαγοσώστρια": "ναυαγοσώστης/ναυαγοσώστρια — lifeguard", "πύργο παρατήρησης": "πύργος παρατήρησης — lookout tower", "προπονήτρια": "προπονητής/προπονήτρια — coach", "πνίγεται": "πνίγομαι — to drown", "βουλιάζει": "βουλιάζω — to sink", "περιστατικά": "περιστατικό — incident, case", "τσιμπήματα": "τσίμπημα — sting, bite", "μέδουσες": "μέδουσα — jellyfish", "κράμπα": "κράμπα — cramp", "ανοίγονται": "ανοίγομαι — to go out (too far) to sea", "λουόμενους": "λουόμενος — bather", "ρεύματα": "ρεύμα — current"},
})

ITEMS.append({
 "id": "l6-rep-kafe-kados", "title": "Ο καφέ κάδος", "title_en": "The brown bin", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από τοπικό ραδιοφωνικό σταθμό για ένα νέο πρόγραμμα ανακύκλωσης σε έναν δήμο.",
 "script": [
  L("Ρεπόρτερ", "f", "Από τον επόμενο μήνα, οι κάτοικοι του δήμου μας θα βρίσκουν στις γειτονιές τους έναν καινούργιο κάδο, καφέ χρώματος. Σε αυτόν θα πετάμε τα υπολείμματα φαγητών, τις φλούδες από φρούτα και λαχανικά, το κατακάθι του καφέ, ακόμα και τα κομμένα φύλλα από τον κήπο.", "From next month, residents of our municipality will find a new bin in their neighbourhoods, brown in colour. In it we'll throw food leftovers, fruit and vegetable peel, coffee grounds, even cut leaves from the garden."),
  L("Ρεπόρτερ", "f", "Σύμφωνα με τον αντιδήμαρχο καθαριότητας, σχεδόν τα μισά σκουπίδια ενός νοικοκυριού είναι οργανικά. Αν τα ξεχωρίσουμε, μπορούν να γίνουν κομπόστ, δηλαδή λίπασμα, αντί να καταλήγουν στη χωματερή.", "According to the deputy mayor for sanitation, almost half of a household's rubbish is organic. If we separate it, it can become compost, that is fertiliser, instead of ending up in the landfill."),
  L("Ρεπόρτερ", "f", "Ο δήμος θα μοιράσει δωρεάν σε κάθε σπίτι ένα μικρό καλαθάκι για την κουζίνα και σακούλες που διαλύονται στο χώμα. Οι πλαστικές σακούλες, προσοχή, δεν πρέπει να μπαίνουν στον καφέ κάδο.", "The municipality will give every home a small kitchen caddy free of charge, along with bags that break down in the soil. Plastic bags, note, must not go into the brown bin."),
  L("Ρεπόρτερ", "f", "Στη λαϊκή αγορά ρωτήσαμε τους πολίτες τι πιστεύουν. Οι περισσότεροι δήλωσαν θετικοί, με μία ένσταση: ότι οι μπλε κάδοι ανακύκλωσης συχνά ξεχειλίζουν και φοβούνται ότι το ίδιο θα συμβεί και με τους καινούργιους. Ο δήμος απαντά ότι οι καφέ κάδοι θα αδειάζουν τρεις φορές την εβδομάδα.", "At the street market we asked people what they think. Most said they were positive, with one objection: that the blue recycling bins often overflow and they're afraid the same will happen with the new ones. The municipality replies that the brown bins will be emptied three times a week."),
 ],
 "questions": [
  Q("Τι θα πετάμε στον καφέ κάδο;", ["Γυαλί και αλουμίνιο", "Οργανικά υπολείμματα, όπως φαγητά και φλούδες", "Χαρτί και χαρτόνι", "Παλιές ηλεκτρικές συσκευές"], 1, "τα υπολείμματα φαγητών, τις φλούδες από φρούτα και λαχανικά, το κατακάθι του καφέ"),
  Q("Γιατί είναι σημαντικό το πρόγραμμα, σύμφωνα με τον αντιδήμαρχο;", ["Γιατί τα οργανικά είναι περίπου το μισό των σκουπιδιών και μπορούν να γίνουν λίπασμα", "Γιατί η χωματερή έκλεισε", "Γιατί θα μειωθούν οι δημοτικοί φόροι", "Γιατί το επέβαλε η κυβέρνηση"], 0, "σχεδόν τα μισά σκουπίδια ενός νοικοκυριού είναι οργανικά ... μπορούν να γίνουν κομπόστ"),
  Q("Τι δεν πρέπει να μπαίνει στον καφέ κάδο;", ["Το κατακάθι του καφέ", "Τα φύλλα από τον κήπο", "Οι πλαστικές σακούλες", "Οι σακούλες που δίνει ο δήμος"], 2, "Οι πλαστικές σακούλες, προσοχή, δεν πρέπει να μπαίνουν στον καφέ κάδο."),
  Q("Ποια ανησυχία εκφράζουν οι πολίτες;", ["Ότι οι κάδοι θα μυρίζουν", "Ότι οι νέοι κάδοι θα γεμίζουν και δεν θα αδειάζουν αρκετά συχνά", "Ότι το πρόγραμμα θα κοστίζει ακριβά", "Ότι δεν θα υπάρχει χώρος στις κουζίνες"], 1, "οι μπλε κάδοι ανακύκλωσης συχνά ξεχειλίζουν και φοβούνται ότι το ίδιο θα συμβεί και με τους καινούργιους"),
 ],
 "gloss": {"κάδο": "κάδος — (rubbish) bin", "υπολείμματα": "υπόλειμμα — leftover, remnant", "φλούδες": "φλούδα — peel, skin", "κατακάθι": "κατακάθι — grounds, sediment", "αντιδήμαρχο": "αντιδήμαρχος — deputy mayor", "νοικοκυριού": "νοικοκυριό — household", "λίπασμα": "λίπασμα — fertiliser", "χωματερή": "χωματερή — landfill, rubbish dump", "ένσταση": "ένσταση — objection", "ξεχειλίζουν": "ξεχειλίζω — to overflow"},
})

ITEMS.append({
 "id": "l6-dia-goneis-xorio", "title": "Οι γονείς φεύγουν για το χωριό", "title_en": "The parents are moving to the village", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε δύο αδέρφια, την Κατερίνα και τον Στάθη, να συζητούν την απόφαση των γονιών τους να μετακομίσουν μόνιμα στο χωριό τώρα που πήραν σύνταξη.",
 "script": [
  L("Κατερίνα", "f", "Σου το είπε η μαμά; Αποφάσισαν να νοικιάσουν το διαμέρισμα στην Αθήνα και να ανέβουν μόνιμα στο χωριό από τον Οκτώβριο.", "Did Mum tell you? They've decided to let the flat in Athens and move up to the village permanently from October."),
  L("Στάθης", "m", "Μου το είπε χθες. Δεν ξέρω τι να πω. Από τη μια τους καταλαβαίνω· ο μπαμπάς ονειρευόταν το περιβόλι του σαράντα χρόνια. Από την άλλη, ο πλησιέστερος γιατρός είναι στην κωμόπολη, μισή ώρα με το αυτοκίνητο.", "She told me yesterday. I don't know what to say. On the one hand I understand them; Dad has been dreaming of his vegetable garden for forty years. On the other, the nearest doctor is in the small town, half an hour by car."),
  L("Κατερίνα", "f", "Αυτό με ανησυχεί κι εμένα. Και τον χειμώνα; Θυμάσαι πριν από δύο χρόνια που έκλεισε ο δρόμος από το χιόνι για τρεις μέρες;", "That worries me too. And in winter? Do you remember two years ago when the road was closed by snow for three days?"),
  L("Στάθης", "m", "Ναι, αλλά να είμαστε δίκαιοι: είναι και οι δύο υγιείς, οδηγούν, και στο χωριό έχουν κόσμο, τη θεία, τους γείτονες. Στην Αθήνα, ειλικρινά, η μαμά δεν έβγαινε από το σπίτι για μέρες.", "Yes, but let's be fair: they're both healthy, they drive, and in the village they have people around, our aunt, the neighbours. In Athens, honestly, Mum didn't leave the house for days."),
  L("Κατερίνα", "f", "Αυτό ισχύει. Τότε ίσως να μην προσπαθήσουμε να τους αλλάξουμε γνώμη, αλλά να το οργανώσουμε σωστά. Να βάλουν σόμπα πέλετ, να έχουν πάντα φάρμακα για ένα μήνα, να μάθει η μαμά να κάνει βιντεοκλήση με τον γιατρό.", "That's true. Then maybe we shouldn't try to change their minds, but organise it properly. They could put in a pellet stove, always have a month's worth of medicine, Mum could learn to do video calls with the doctor."),
  L("Στάθης", "m", "Συμφωνώ. Κι εγώ μπορώ να ανεβαίνω ένα Σαββατοκύριακο τον μήνα. Άλλωστε, τα παιδιά θα ενθουσιαστούν που θα έχουν παππού και γιαγιά στο βουνό.", "I agree. And I can go up one weekend a month. Besides, the kids will be thrilled to have a grandad and grandma in the mountains."),
 ],
 "questions": [
  Q("Τι αποφάσισαν οι γονείς;", ["Να πουλήσουν το σπίτι στο χωριό", "Να ζήσουν μόνιμα στο χωριό και να νοικιάσουν το διαμέρισμα της Αθήνας", "Να μετακομίσουν κοντά στα παιδιά τους", "Να περνούν μόνο τα καλοκαίρια στο χωριό"], 1, "Αποφάσισαν να νοικιάσουν το διαμέρισμα στην Αθήνα και να ανέβουν μόνιμα στο χωριό"),
  Q("Τι ανησυχεί τα δύο αδέρφια;", ["Η απόσταση από γιατρό και ο χειμώνας", "Το κόστος της μετακόμισης", "Ότι οι γονείς δεν έχουν φίλους στο χωριό", "Ότι το σπίτι στο χωριό είναι μικρό"], 0, "ο πλησιέστερος γιατρός είναι στην κωμόπολη ... Και τον χειμώνα;"),
  Q("Ποιο επιχείρημα υπέρ της μετακόμισης φέρνει ο Στάθης;", ["Ότι στο χωριό είναι όλα φθηνότερα", "Ότι στην Αθήνα η μητέρα τους ήταν απομονωμένη, ενώ στο χωριό έχουν συντροφιά", "Ότι ο γιατρός του χωριού είναι πολύ καλός", "Ότι ο δρόμος δεν κλείνει ποτέ"], 1, "στο χωριό έχουν κόσμο ... Στην Αθήνα ... η μαμά δεν έβγαινε από το σπίτι για μέρες"),
  Q("Σε τι καταλήγουν τελικά;", ["Να πείσουν τους γονείς να μείνουν στην Αθήνα", "Να μετακομίσουν κι εκείνοι στο χωριό", "Να βοηθήσουν τους γονείς να οργανωθούν σωστά για τη νέα ζωή", "Να το συζητήσουν ξανά τον Οκτώβριο"], 2, "ίσως να μην προσπαθήσουμε να τους αλλάξουμε γνώμη, αλλά να το οργανώσουμε σωστά"),
 ],
 "gloss": {"σύνταξη": "σύνταξη — pension", "μόνιμα": "μόνιμα — permanently", "περιβόλι": "περιβόλι — vegetable garden, orchard", "πλησιέστερος": "πλησιέστερος — nearest", "κωμόπολη": "κωμόπολη — small town", "να είμαστε δίκαιοι": "είμαι δίκαιος — to be fair", "σόμπα πέλετ": "σόμπα πέλετ — pellet stove", "βιντεοκλήση": "βιντεοκλήση — video call", "θα ενθουσιαστούν": "ενθουσιάζομαι — to be thrilled, delighted"},
})

ITEMS.append({
 "id": "l6-mon-podilato", "title": "Με το ποδήλατο στη δουλειά", "title_en": "Cycling to work", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε τη Δέσποινα, που ζει στη Θεσσαλονίκη, να μιλάει σε μια εκδήλωση για το πώς άρχισε να πηγαίνει στη δουλειά με ποδήλατο.",
 "script": [
  L("Δέσποινα", "f", "Πριν από τρία χρόνια έκανα κάθε πρωί σαράντα λεπτά με το αυτοκίνητο για μια απόσταση έξι χιλιομέτρων. Σαράντα λεπτά! Έφτανα στο γραφείο εκνευρισμένη, πριν καν αρχίσει η μέρα.", "Three years ago I spent forty minutes every morning in the car for a distance of six kilometres. Forty minutes! I'd arrive at the office irritated before the day had even started."),
  L("Δέσποινα", "f", "Ένα φθινόπωρο το αυτοκίνητο χάλασε και μπήκε στο συνεργείο για δύο εβδομάδες. Δανείστηκα το ποδήλατο της ανιψιάς μου, κυρίως από ανάγκη. Δεν περίμενα ότι θα μου άρεσε.", "One autumn the car broke down and went into the garage for two weeks. I borrowed my niece's bicycle, mostly out of necessity. I didn't expect to like it."),
  L("Δέσποινα", "f", "Την πρώτη μέρα φοβόμουν τα αυτοκίνητα και κατέβηκα στο πεζοδρόμιο τουλάχιστον πέντε φορές. Μετά ανακάλυψα ότι, αν πάω από την παραλία, έχω ποδηλατόδρομο σχεδόν όλη τη διαδρομή. Έκανα είκοσι λεπτά, με θέα τη θάλασσα.", "On the first day I was afraid of the cars and got off onto the pavement at least five times. Then I discovered that if I went along the seafront, I had a cycle lane almost the whole way. It took me twenty minutes, with a view of the sea."),
  L("Δέσποινα", "f", "Όταν μου επέστρεψαν το αυτοκίνητο, το άφησα στο πάρκινγκ. Δεν θα σας πω ότι όλα είναι ρόδινα. Όταν βρέχει, βρέχομαι. Τον Ιούλιο φτάνω ιδρωμένη και κρατάω ένα καθαρό μπλουζάκι στο συρτάρι. Και ναι, κάποιοι οδηγοί δεν μας σέβονται.", "When I got the car back, I left it in the car park. I won't tell you everything is rosy. When it rains, I get wet. In July I arrive sweaty and I keep a clean T-shirt in the drawer. And yes, some drivers don't respect us."),
  L("Δέσποινα", "f", "Αλλά κερδίζω σχεδόν μία ώρα κάθε μέρα, γλιτώνω τα λεφτά της βενζίνης και του πάρκινγκ, και δεν πηγαίνω πια στο γυμναστήριο, γιατί δεν το χρειάζομαι. Αυτό που θα ζητούσα από τον δήμο είναι περισσότεροι ποδηλατόδρομοι και ασφαλή σημεία για να δένουμε τα ποδήλατα.", "But I gain almost an hour every day, I save the money for petrol and parking, and I don't go to the gym any more, because I don't need it. What I'd ask of the municipality is more cycle lanes and safe places to lock up our bikes."),
 ],
 "questions": [
  Q("Γιατί άρχισε η Δέσποινα να πηγαίνει με ποδήλατο;", ["Το αποφάσισε για λόγους υγείας", "Το αυτοκίνητό της ήταν στο συνεργείο", "Της το πρότεινε ο εργοδότης της", "Μετακόμισε πιο κοντά στη δουλειά"], 1, "το αυτοκίνητο χάλασε και μπήκε στο συνεργείο για δύο εβδομάδες"),
  Q("Τι άλλαξε όταν βρήκε τη διαδρομή από την παραλία;", ["Η διαδρομή έγινε πιο σύντομη και πιο ευχάριστη", "Άρχισε να πηγαίνει με τα πόδια", "Σταμάτησε να φοβάται τη βροχή", "Η απόσταση έγινε δέκα χιλιόμετρα"], 0, "έχω ποδηλατόδρομο σχεδόν όλη τη διαδρομή. Έκανα είκοσι λεπτά, με θέα τη θάλασσα."),
  Q("Ποιο από τα παρακάτω ΔΕΝ αναφέρει ως μειονέκτημα;", ["Τη βροχή", "Τη ζέστη του καλοκαιριού", "Τη συμπεριφορά ορισμένων οδηγών", "Το κόστος του ποδηλάτου"], 3, "Όταν βρέχει, βρέχομαι. Τον Ιούλιο φτάνω ιδρωμένη ... κάποιοι οδηγοί δεν μας σέβονται."),
  Q("Τι ζητά από τον δήμο;", ["Δωρεάν ποδήλατα για όλους", "Περισσότερους ποδηλατοδρόμους και ασφαλή σημεία στάθμευσης για ποδήλατα", "Λιγότερα αυτοκίνητα στην παραλία", "Φθηνότερο πάρκινγκ"], 1, "περισσότεροι ποδηλατόδρομοι και ασφαλή σημεία για να δένουμε τα ποδήλατα"),
 ],
 "gloss": {"εκνευρισμένη": "εκνευρισμένος — irritated", "συνεργείο": "συνεργείο — (car) repair shop, garage", "Δανείστηκα": "δανείζομαι — to borrow", "ανιψιάς": "ανιψιά — niece", "πεζοδρόμιο": "πεζοδρόμιο — pavement", "ποδηλατόδρομο": "ποδηλατόδρομος — cycle lane", "ρόδινα": "ρόδινος — rosy", "ιδρωμένη": "ιδρωμένος — sweaty", "γλιτώνω": "γλιτώνω — to save, be spared", "να δένουμε": "δένω — to tie, lock up"},
})

ITEMS.append({
 "id": "l6-ann-mouseio", "title": "Στο μουσείο, πριν κλείσει", "title_en": "At the museum, before closing time", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα ενός αρχαιολογικού μουσείου.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί επισκέπτες, σας ενημερώνουμε ότι το μουσείο θα κλείσει σε τριάντα λεπτά. Το πωλητήριο και το καφέ του ισογείου θα παραμείνουν ανοιχτά για μισή ώρα ακόμα μετά το κλείσιμο των αιθουσών.", "Dear visitors, we inform you that the museum will close in thirty minutes. The shop and the café on the ground floor will stay open for another half hour after the galleries close."),
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε ότι η αίθουσα δεκατέσσερα, με τα ευρήματα από το ναυάγιο, παραμένει κλειστή λόγω συντήρησης. Τα πιο σημαντικά αντικείμενά της εκτίθενται προσωρινά στον πρώτο όροφο, δίπλα στις σκάλες.", "We remind you that gallery fourteen, with the finds from the shipwreck, remains closed for conservation work. Its most important objects are on temporary display on the first floor, next to the stairs."),
  L("Εκφωνήτρια", "f", "Αύριο, Κυριακή, η είσοδος είναι ελεύθερη για όλους. Λόγω της αναμενόμενης προσέλευσης, συνιστούμε να έρθετε νωρίς το πρωί. Ευχαριστούμε που μας επισκεφθήκατε.", "Tomorrow, Sunday, admission is free for everyone. Because of the expected number of visitors, we recommend coming early in the morning. Thank you for visiting us."),
 ],
 "questions": [
  Q("Τι θα μείνει ανοιχτό μετά το κλείσιμο των αιθουσών;", ["Η αίθουσα δεκατέσσερα", "Το πωλητήριο και το καφέ", "Ο πρώτος όροφος", "Τίποτα"], 1, "Το πωλητήριο και το καφέ του ισογείου θα παραμείνουν ανοιχτά για μισή ώρα ακόμα"),
  Q("Πού μπορούν να δουν οι επισκέπτες τα σημαντικότερα ευρήματα του ναυαγίου;", ["Στην αίθουσα δεκατέσσερα", "Στο καφέ", "Στον πρώτο όροφο, δίπλα στις σκάλες", "Μόνο στον κατάλογο του πωλητηρίου"], 2, "εκτίθενται προσωρινά στον πρώτο όροφο, δίπλα στις σκάλες"),
  Q("Γιατί συνιστούν να έρθει κανείς νωρίς την Κυριακή;", ["Γιατί το μουσείο κλείνει το μεσημέρι", "Γιατί η είσοδος είναι δωρεάν και αναμένεται πολύς κόσμος", "Γιατί θα γίνει ξενάγηση", "Γιατί ανοίγει ξανά η αίθουσα δεκατέσσερα"], 1, "η είσοδος είναι ελεύθερη για όλους. Λόγω της αναμενόμενης προσέλευσης"),
 ],
 "gloss": {"πωλητήριο": "πωλητήριο — museum shop", "αιθουσών": "αίθουσα — gallery, hall", "Υπενθυμίζουμε": "υπενθυμίζω — to remind", "ευρήματα": "εύρημα — find", "ναυάγιο": "ναυάγιο — shipwreck", "συντήρησης": "συντήρηση — conservation, maintenance", "εκτίθενται": "εκτίθεμαι — to be exhibited", "ελεύθερη": "ελεύθερη είσοδος — free admission", "προσέλευσης": "προσέλευση — turnout, attendance"},
})

ITEMS.append({
 "id": "l6-int-tyrokomos", "title": "Μια νέα τυροκόμος στα Γιάννενα", "title_en": "A young cheesemaker in Ioannina", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με την Ευανθία, που άφησε τη δουλειά της στην Αθήνα και άνοιξε ένα μικρό τυροκομείο στην Ήπειρο.",
 "script": [
  L("Δημοσιογράφος", "m", "Ευανθία, ήσουν γραφίστρια σε διαφημιστική εταιρεία στην Αθήνα. Πώς βρέθηκες να φτιάχνεις τυρί;", "Evanthia, you were a graphic designer at an advertising agency in Athens. How did you end up making cheese?"),
  L("Ευανθία", "f", "Ο παππούς μου είχε πρόβατα και κάθε καλοκαίρι τον βοηθούσα. Όταν πέθανε, το μαντρί θα έκλεινε. Δεν άντεχα την ιδέα ότι όλη αυτή η γνώση θα χανόταν. Έτσι, πήρα μια απόφαση που όλοι τη θεώρησαν τρελή.", "My grandfather had sheep and every summer I helped him. When he died, the sheepfold was going to close. I couldn't bear the idea that all that knowledge would be lost. So I made a decision that everyone thought was crazy."),
  L("Δημοσιογράφος", "m", "Ήταν δύσκολη η αρχή;", "Was the beginning difficult?"),
  L("Ευανθία", "f", "Πολύ. Η γραφειοκρατία για τις άδειες κράτησε σχεδόν ενάμιση χρόνο. Και την πρώτη χρονιά πέταξα πολλά κιλά τυρί, γιατί δεν είχε την υφή που ήθελα. Οι γέροι τυροκόμοι του χωριού στην αρχή γελούσαν. Μετά άρχισαν να μου δίνουν συμβουλές.", "Very. The red tape for the permits took almost a year and a half. And in the first year I threw away many kilos of cheese, because it didn't have the texture I wanted. The old cheesemakers in the village laughed at first. Then they started giving me advice."),
  L("Δημοσιογράφος", "m", "Και η γραφίστρια μέσα σου; Χάθηκε;", "And the graphic designer inside you? Has she disappeared?"),
  L("Ευανθία", "f", "Καθόλου! Εγώ σχεδίασα τις ετικέτες και την ιστοσελίδα. Σήμερα το ένα τρίτο των πωλήσεων γίνεται μέσω ίντερνετ, σε όλη την Ελλάδα. Χωρίς αυτό, ένα τόσο μικρό τυροκομείο δύσκολα θα επιβίωνε.", "Not at all! I designed the labels and the website. Today a third of sales are made online, all over Greece. Without that, such a small cheese dairy would hardly survive."),
 ],
 "questions": [
  Q("Γιατί η Ευανθία άνοιξε το τυροκομείο;", ["Γιατί έχασε τη δουλειά της στην Αθήνα", "Για να μη χαθεί η παράδοση και η γνώση του παππού της", "Γιατί της το ζήτησε ο δήμος", "Γιατί η τυροκομία είναι πολύ κερδοφόρα"], 1, "Δεν άντεχα την ιδέα ότι όλη αυτή η γνώση θα χανόταν."),
  Q("Ποιο από τα παρακάτω ήταν πρόβλημα στην αρχή;", ["Η έλλειψη γάλακτος", "Οι γείτονες που δεν ήθελαν το τυροκομείο", "Η καθυστέρηση στις άδειες και η ποιότητα του τυριού", "Το κόστος της ιστοσελίδας"], 2, "Η γραφειοκρατία για τις άδειες κράτησε σχεδόν ενάμιση χρόνο ... δεν είχε την υφή που ήθελα"),
  Q("Πώς άλλαξε η στάση των παλιών τυροκόμων;", ["Από την κοροϊδία πέρασαν στη βοήθεια", "Από τη βοήθεια πέρασαν στον ανταγωνισμό", "Δεν άλλαξε ποτέ", "Της ζήτησαν να συνεργαστούν"], 0, "στην αρχή γελούσαν. Μετά άρχισαν να μου δίνουν συμβουλές"),
  Q("Τι ρόλο παίζει σήμερα η παλιά της δουλειά;", ["Κανέναν· την έχει ξεχάσει εντελώς", "Χάρη σε αυτήν φτιάχνει τις ετικέτες και την ιστοσελίδα, που φέρνει πωλήσεις", "Δουλεύει ακόμα ως γραφίστρια τα βράδια", "Διδάσκει γραφιστική στο χωριό"], 1, "Εγώ σχεδίασα τις ετικέτες και την ιστοσελίδα. Σήμερα το ένα τρίτο των πωλήσεων γίνεται μέσω ίντερνετ"),
 ],
 "gloss": {"τυροκόμοι": "τυροκόμος — cheesemaker", "τυροκομείο": "τυροκομείο — cheese dairy", "γραφίστρια": "γραφίστρια — graphic designer (f)", "πρόβατα": "πρόβατο — sheep", "μαντρί": "μαντρί — sheepfold", "Δεν άντεχα": "αντέχω — to bear, stand", "γραφειοκρατία": "γραφειοκρατία — bureaucracy, red tape", "άδειες": "άδεια — permit, licence", "υφή": "υφή — texture", "ετικέτες": "ετικέτα — label", "επιβίωνε": "επιβιώνω — to survive"},
})

ITEMS.append({
 "id": "l6-dia-tilergasia", "title": "Πίσω στο γραφείο;", "title_en": "Back to the office?", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε δύο συναδέλφους, τον Άρη και τη Σοφία, να συζητούν για την απόφαση της εταιρείας τους να επιστρέψουν όλοι στο γραφείο τέσσερις μέρες την εβδομάδα.",
 "script": [
  L("Άρης", "m", "Είδες το email από τη διεύθυνση; Από τον Ιανουάριο, τέσσερις μέρες στο γραφείο και μία από το σπίτι. Τέλος η τηλεργασία όπως την ξέραμε.", "Did you see the email from management? From January, four days in the office and one from home. That's the end of remote work as we knew it."),
  L("Σοφία", "f", "Το είδα και, για να είμαι ειλικρινής, δεν στενοχωρήθηκα τόσο. Δουλεύοντας από το σπίτι είχα αρχίσει να νιώθω ότι δεν ξεχωρίζει η δουλειά από την προσωπική μου ζωή. Απαντούσα σε μηνύματα στις έντεκα το βράδυ.", "I saw it and, to be honest, I wasn't that upset. Working from home I'd started to feel that work and my private life weren't separate any more. I was answering messages at eleven at night."),
  L("Άρης", "m", "Εσύ μένεις δέκα λεπτά από εδώ. Εγώ χρειάζομαι μιάμιση ώρα για να έρθω, με δύο μέσα. Τρεις ώρες τη μέρα στον δρόμο, τέσσερις μέρες την εβδομάδα. Κάνε τον λογαριασμό.", "You live ten minutes from here. I need an hour and a half to get in, with two changes. Three hours a day on the road, four days a week. Do the maths."),
  L("Σοφία", "f", "Δίκιο έχεις, για σένα είναι άλλο πράγμα. Γιατί δεν το θέτεις στη διευθύντρια; Νομίζω ότι η απόφαση αφήνει περιθώριο για εξαιρέσεις, αν υπάρχει σοβαρός λόγος.", "You're right, for you it's a different matter. Why don't you raise it with the director? I think the decision leaves room for exceptions if there's a good reason."),
  L("Άρης", "m", "Δεν θέλω να φανεί ότι ζητάω ειδική μεταχείριση. Αλλά ίσως να προτείνω κάτι άλλο: να έρχομαι τρεις μέρες, αλλά νωρίτερα, στις επτά, για να αποφεύγω την κίνηση.", "I don't want it to look as if I'm asking for special treatment. But maybe I'll propose something else: to come in three days, but earlier, at seven, to avoid the traffic."),
  L("Σοφία", "f", "Αυτό ακούγεται λογικό. Και να τους πεις ότι οι αποδόσεις σου τα τελευταία δύο χρόνια ήταν από τις καλύτερες της ομάδας. Τα νούμερα μιλάνε από μόνα τους.", "That sounds reasonable. And tell them that your results over the last two years have been among the best in the team. The numbers speak for themselves."),
 ],
 "questions": [
  Q("Τι αποφάσισε η εταιρεία;", ["Να καταργήσει εντελώς την τηλεργασία", "Οι υπάλληλοι να δουλεύουν τέσσερις μέρες στο γραφείο και μία από το σπίτι", "Να μειώσει το ωράριο", "Να μετακομίσει σε άλλο κτίριο"], 1, "τέσσερις μέρες στο γραφείο και μία από το σπίτι"),
  Q("Γιατί η Σοφία δεν είναι δυσαρεστημένη;", ["Γιατί στο σπίτι δεν είχε καλό ίντερνετ", "Γιατί η δουλειά από το σπίτι μπέρδευε τη δουλειά με την προσωπική της ζωή", "Γιατί της αρέσει να ταξιδεύει με το μετρό", "Γιατί θα πάρει αύξηση"], 1, "είχα αρχίσει να νιώθω ότι δεν ξεχωρίζει η δουλειά από την προσωπική μου ζωή"),
  Q("Ποιο είναι το πρόβλημα του Άρη;", ["Δεν συμπαθεί τους συναδέλφους του", "Χρειάζεται πολύ χρόνο για να πάει στο γραφείο", "Δεν έχει αυτοκίνητο", "Έχει μικρά παιδιά"], 1, "χρειάζομαι μιάμιση ώρα για να έρθω, με δύο μέσα"),
  Q("Τι σκέφτεται να προτείνει ο Άρης;", ["Να δουλεύει μόνο από το σπίτι", "Να παραιτηθεί", "Τρεις μέρες στο γραφείο, με νωρίτερη ώρα έναρξης", "Να μετακομίσει πιο κοντά"], 2, "να έρχομαι τρεις μέρες, αλλά νωρίτερα, στις επτά"),
  Q("Τι τον συμβουλεύει η Σοφία να τονίσει;", ["Τις καλές του επιδόσεις", "Την οικογενειακή του κατάσταση", "Το κόστος των εισιτηρίων", "Ότι κι άλλοι συνάδελφοι διαφωνούν"], 0, "οι αποδόσεις σου τα τελευταία δύο χρόνια ήταν από τις καλύτερες της ομάδας"),
 ],
 "gloss": {"διεύθυνση": "διεύθυνση — management", "τηλεργασία": "τηλεργασία — remote working", "στενοχωρήθηκα": "στενοχωριέμαι — to be upset", "ξεχωρίζει": "ξεχωρίζω — to be separate, stand apart", "μέσα": "μέσο (μεταφοράς) — means of transport", "Κάνε τον λογαριασμό": "κάνω τον λογαριασμό — to do the maths", "το θέτεις": "θέτω — to raise (an issue)", "περιθώριο": "περιθώριο — room, margin", "μεταχείριση": "μεταχείριση — treatment", "αποδόσεις": "απόδοση — performance, results"},
})

import random
rnd = random.Random(6)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
out = {"items": ITEMS}
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]: assert any(k in s["el"] for s in it["script"]) or k in it["context_el"], (it["id"], k)
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-6.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
