# Source for library/listening/listening-259.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l259.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l259-news-ekato-pente-chronia", "title": "Τα εκατόν πέμπτα γενέθλιά της γιόρτασε η γηραιότερη κάτοικος ενός χωριού της Λέσβου", "title_en": "The oldest resident of a village on Lesbos celebrates her 105th birthday", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο πρωινό δελτίο ενός περιφερειακού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνήτρια", "f", "Με τραγούδια και μια τούρτα με εκατόν πέντε κεράκια γιόρτασε χθες τα γενέθλιά της η κυρία Ευανθία, η γηραιότερη κάτοικος ενός ορεινού χωριού της Λέσβου. Στη γιορτή, που έγινε στο καφενείο της πλατείας, ήρθαν σχεδόν όλοι οι κάτοικοι, αλλά και ο δήμαρχος.", "With songs and a cake with a hundred and five candles, Mrs Evanthia, the oldest resident of a mountain village on Lesbos, celebrated her birthday yesterday. Almost all the villagers came to the party, which was held at the café on the square, and so did the mayor."),
  L("Εκφωνήτρια", "f", "Η κυρία Ευανθία έχει πέντε παιδιά, δώδεκα εγγόνια και εννιά δισέγγονα, και ζει ακόμη μόνη της στο σπίτι όπου γεννήθηκε. Κάθε πρωί ποτίζει τον κήπο της και το απόγευμα πλέκει κάλτσες για τα δισέγγονά της.", "Mrs Evanthia has five children, twelve grandchildren and nine great-grandchildren, and still lives alone in the house where she was born. Every morning she waters her garden, and in the afternoon she knits socks for her great-grandchildren."),
  L("Εκφωνήτρια", "f", "Όταν τη ρώτησαν ποιο είναι το μυστικό της, απάντησε ότι περπατούσε κάθε μέρα ως το εκκλησάκι του λόφου και ότι δεν κράτησε ποτέ κακία σε κανέναν. «Ο θυμός σε γερνάει πιο γρήγορα από τα χρόνια», είπε.", "When asked what her secret is, she replied that she used to walk every day to the little church on the hill and that she never held a grudge against anyone. 'Anger ages you faster than the years,' she said."),
  L("Εκφωνήτρια", "f", "Η μεγαλύτερη ευχή της, όπως είπε, είναι να ξαναδεί το χωριό γεμάτο παιδιά, όπως ήταν όταν εκείνη πήγαινε στο σχολείο. Το δημοτικό σχολείο του χωριού έκλεισε πριν από δεκαπέντε χρόνια.", "Her greatest wish, she said, is to see the village full of children again, as it was when she went to school. The village primary school closed fifteen years ago."),
 ],
 "questions": [
  Q("Πού έγινε η γιορτή;", ["Στο σπίτι της", "Στο καφενείο της πλατείας", "Στο δημαρχείο", "Στο σχολείο"], 1, "Στη γιορτή, που έγινε στο καφενείο της πλατείας"),
  Q("Πώς ζει σήμερα η κυρία Ευανθία;", ["Με την κόρη της στην πόλη", "Σε ένα γηροκομείο", "Μόνη της στο σπίτι όπου γεννήθηκε", "Με τα εγγόνια της"], 2, "ζει ακόμη μόνη της στο σπίτι όπου γεννήθηκε"),
  Q("Ποιο είναι, κατά τη γνώμη της, το μυστικό της;", ["Το λάδι και τα χόρτα", "Το περπάτημα και το ότι δεν κράτησε κακία", "Ο πολύς ύπνος", "Το καθημερινό κολύμπι"], 1, "περπατούσε κάθε μέρα … και … δεν κράτησε ποτέ κακία σε κανέναν"),
  Q("Ποια είναι η μεγαλύτερη ευχή της;", ["Να ταξιδέψει στην Αθήνα", "Να γιορτάσει τα εκατόν δέκα", "Να δει ξανά το χωριό γεμάτο παιδιά", "Να ξανανοίξει το καφενείο"], 2, "είναι να ξαναδεί το χωριό γεμάτο παιδιά"),
 ],
 "gloss": {"γηραιότερη": "γηραιότερος — oldest", "κεράκια": "κεράκι — little candle", "δισέγγονα": "δισέγγονο — great-grandchild", "πλέκει": "πλέκω — to knit", "εκκλησάκι": "εκκλησάκι — little church, chapel", "κακία": "κακία — malice, grudge (κρατώ κακία = to bear a grudge)", "γερνάει": "γερνώ — to age, make old", "ευχή": "ευχή — wish"}
})

ITEMS.append({
 "id": "l259-vm-fysikotherapeftria", "title": "Μήνυμα από τη φυσικοθεραπεύτρια για το πρώτο ραντεβού", "title_en": "A message from the physiotherapist about the first appointment", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει ραντεβού σε ένα φυσικοθεραπευτήριο για έναν πόνο στον ώμο. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Φυσικοθεραπεύτρια", "f", "Καλημέρα σας, η Κατερίνα είμαι, από το φυσικοθεραπευτήριο. Σας τηλεφωνώ για το ραντεβού σας της Δευτέρας. Δυστυχώς, εκείνο το πρωί θα λείπω σε ένα σεμινάριο, οπότε σας προτείνω να έρθετε την ίδια μέρα στις έξι το απόγευμα, ή την Τρίτη στις εννιά το πρωί.", "Good morning, this is Katerina from the physiotherapy clinic. I'm calling about your appointment on Monday. Unfortunately I'll be away at a seminar that morning, so I suggest you come the same day at six in the evening, or on Tuesday at nine in the morning."),
  L("Φυσικοθεραπεύτρια", "f", "Στο πρώτο ραντεβού θα κάνουμε κυρίως αξιολόγηση: θα δούμε πόσο κινείται ο ώμος σας και πού ακριβώς πονάτε. Φέρτε μαζί σας τη μαγνητική τομογραφία που κάνατε και, αν την έχετε, τη γνωμάτευση του ορθοπεδικού. Χωρίς παραπεμπτικό από γιατρό, το ασφαλιστικό ταμείο δεν καλύπτει τις συνεδρίες.", "At the first appointment we'll mainly do an assessment: we'll see how much your shoulder moves and exactly where it hurts. Bring the MRI scan you had and, if you have it, the orthopaedist's report. Without a referral from a doctor, the insurance fund doesn't cover the sessions."),
  L("Φυσικοθεραπεύτρια", "f", "Καλό είναι να φορέσετε άνετα ρούχα, ιδανικά ένα αμάνικο μπλουζάκι, για να μπορώ να δω τον ώμο. Και κάτι ακόμη: μέχρι τότε μην κάνετε ασκήσεις που βρήκατε στο ίντερνετ. Με τον πόνο που μου περιγράψατε, μπορεί να κάνουν περισσότερο κακό παρά καλό.", "It's a good idea to wear comfortable clothes, ideally a sleeveless top, so that I can see the shoulder. And one more thing: until then, don't do exercises you found on the internet. With the pain you described to me, they may do more harm than good."),
  L("Φυσικοθεραπεύτρια", "f", "Η συνεδρία κρατά περίπου μία ώρα. Πείτε μου με ένα μήνυμα ποια από τις δύο ώρες σας βολεύει, για να κρατήσω τη θέση. Ευχαριστώ, και περαστικά!", "The session lasts about an hour. Let me know by text which of the two times suits you, so that I can hold the slot. Thank you, and get well soon!"),
 ],
 "questions": [
  Q("Γιατί αλλάζει το ραντεβού της Δευτέρας το πρωί;", ["Γιατί το φυσικοθεραπευτήριο κλείνει", "Γιατί η φυσικοθεραπεύτρια θα είναι σε ένα σεμινάριο", "Γιατί είναι αργία", "Γιατί χάλασε ένα μηχάνημα"], 1, "εκείνο το πρωί θα λείπω σε ένα σεμινάριο"),
  Q("Τι θα γίνει κυρίως στο πρώτο ραντεβού;", ["Μασάζ", "Αξιολόγηση της κίνησης και του πόνου", "Μια ακτινογραφία", "Ασκήσεις στο γυμναστήριο"], 1, "θα κάνουμε κυρίως αξιολόγηση"),
  Q("Γιατί χρειάζεται παραπεμπτικό από γιατρό;", ["Για να κλείσετε δεύτερο ραντεβού", "Για να καλύψει το ασφαλιστικό ταμείο τις συνεδρίες", "Για να κάνετε μαγνητική", "Για να μπείτε στο κτίριο"], 1, "Χωρίς παραπεμπτικό από γιατρό, το ασφαλιστικό ταμείο δεν καλύπτει τις συνεδρίες"),
  Q("Τι σας συμβουλεύει να μην κάνετε μέχρι το ραντεβού;", ["Να μην κολυμπάτε", "Να μην παίρνετε παυσίπονα", "Να μην κάνετε ασκήσεις από το ίντερνετ", "Να μην οδηγείτε"], 2, "μην κάνετε ασκήσεις που βρήκατε στο ίντερνετ"),
 ],
 "gloss": {"φυσικοθεραπευτήριο": "φυσικοθεραπευτήριο — physiotherapy clinic", "σεμινάριο": "σεμινάριο — seminar, training course", "αξιολόγηση": "αξιολόγηση — assessment", "τομογραφία": "τομογραφία — scan (μαγνητική τομογραφία = MRI)", "γνωμάτευση": "γνωμάτευση — medical report, opinion", "ορθοπεδικού": "ορθοπεδικός — orthopaedist", "παραπεμπτικό": "παραπεμπτικό — referral", "συνεδρίες": "συνεδρία — session", "αμάνικο": "αμάνικος — sleeveless", "περαστικά": "περαστικά — get well soon"}
})

ITEMS.append({
 "id": "l259-c1-mono-varometro", "title": "Το βάρος του αέρα: η ιστορία του βαρόμετρου", "title_en": "The weight of the air: the history of the barometer", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας ομιλίας σε έναν κύκλο εκδηλώσεων για την ιστορία της επιστήμης.",
 "script": [
  L("Ομιλητής", "m", "Στις αρχές του δέκατου έβδομου αιώνα οι τεχνίτες της Φλωρεντίας αντιμετώπιζαν ένα παράξενο πρόβλημα: οι αντλίες τους δεν μπορούσαν να ανεβάσουν το νερό από ένα πηγάδι ψηλότερα από δέκα μέτρα περίπου. Η εξήγηση που κυριαρχούσε τότε, από την εποχή του Αριστοτέλη, ήταν ότι «η φύση απεχθάνεται το κενό».", "In the early seventeenth century the craftsmen of Florence faced a strange problem: their pumps could not raise water from a well higher than about ten metres. The explanation that prevailed then, since the time of Aristotle, was that 'nature abhors a vacuum'."),
  L("Ομιλητής", "m", "Το 1643 ένας μαθητής του Γαλιλαίου, ο Εβαντζελίστα Τοριτσέλι, σκέφτηκε διαφορετικά. Γέμισε έναν γυάλινο σωλήνα με υδράργυρο, που είναι πολύ βαρύτερος από το νερό, και τον αναποδογύρισε σε μια λεκάνη. Ο υδράργυρος κατέβηκε και σταμάτησε σε ύψος περίπου εβδομήντα έξι εκατοστών, αφήνοντας από πάνω ένα κενό. Τον υδράργυρο, συμπέρανε, τον κρατούσε το βάρος του αέρα που πιέζει τη λεκάνη.", "In 1643 a pupil of Galileo, Evangelista Torricelli, thought differently. He filled a glass tube with mercury, which is much heavier than water, and turned it upside down in a basin. The mercury fell and stopped at a height of about seventy-six centimetres, leaving an empty space above it. The mercury, he concluded, was held up by the weight of the air pressing on the basin."),
  L("Ομιλητής", "m", "Λίγα χρόνια αργότερα, ο Γάλλος Μπλεζ Πασκάλ ζήτησε από τον γαμπρό του να ανεβάσει ένα τέτοιο όργανο σε ένα βουνό της κεντρικής Γαλλίας. Όσο ανέβαινε, η στήλη του υδραργύρου χαμήλωνε, γιατί από πάνω υπήρχε λιγότερος αέρας. Ήταν η απόδειξη ότι η ατμόσφαιρα έχει βάρος.", "A few years later, the Frenchman Blaise Pascal asked his brother-in-law to carry such an instrument up a mountain in central France. As he climbed, the column of mercury dropped, because there was less air above it. It was the proof that the atmosphere has weight."),
  L("Ομιλητής", "m", "Σύντομα οι παρατηρητές πρόσεξαν κάτι ακόμη: η στήλη ανεβοκατέβαινε και με τον καιρό, και συνήθως έπεφτε πριν από τις καταιγίδες. Το όργανο πήρε το όνομα «βαρόμετρο», από τις ελληνικές λέξεις «βάρος» και «μέτρο», και έγινε για δύο αιώνες το βασικό εργαλείο της πρόγνωσης του καιρού, πρώτα στα πλοία και ύστερα σε κάθε αστικό σαλόνι.", "Soon observers noticed something else: the column also rose and fell with the weather, and it usually dropped before storms. The instrument was named 'barometer', from the Greek words 'baros', weight, and 'metron', measure, and for two centuries it became the basic tool of weather forecasting, first on ships and then in every middle-class drawing room."),
 ],
 "questions": [
  Q("Ποιο πρόβλημα είχαν οι τεχνίτες της Φλωρεντίας;", ["Οι αντλίες τους δεν ανέβαζαν το νερό ψηλότερα από δέκα μέτρα περίπου", "Τα πηγάδια τους στέρευαν", "Ο υδράργυρος ήταν πολύ ακριβός", "Δεν μπορούσαν να προβλέψουν τις καταιγίδες"], 0, "οι αντλίες τους δεν μπορούσαν να ανεβάσουν το νερό … ψηλότερα από δέκα μέτρα περίπου"),
  Q("Τι συμπέρανε ο Τοριτσέλι;", ["Ότι η φύση απεχθάνεται το κενό", "Ότι τον υδράργυρο τον κρατούσε το βάρος του αέρα", "Ότι ο υδράργυρος είναι ελαφρύτερος από το νερό", "Ότι ο σωλήνας ήταν σπασμένος"], 1, "Τον υδράργυρο … τον κρατούσε το βάρος του αέρα"),
  Q("Τι έδειξε το πείραμα στο βουνό;", ["Ότι στο βουνό κάνει πιο κρύο", "Ότι η στήλη του υδραργύρου χαμήλωνε όσο ανέβαινε", "Ότι το όργανο δεν λειτουργεί στο ύψος", "Ότι ο αέρας είναι πιο βαρύς στις κορυφές"], 1, "Όσο ανέβαινε, η στήλη του υδραργύρου χαμήλωνε"),
  Q("Τι πρόσεξαν αργότερα οι παρατηρητές;", ["Ότι η στήλη έπεφτε συνήθως πριν από τις καταιγίδες", "Ότι ο υδράργυρος εξατμιζόταν", "Ότι το όργανο έδειχνε την ώρα", "Ότι στα πλοία δεν λειτουργούσε"], 0, "συνήθως έπεφτε πριν από τις καταιγίδες"),
 ],
 "gloss": {"αντλίες": "αντλία — pump", "απεχθάνεται": "απεχθάνομαι — to abhor", "κενό": "κενό — vacuum, empty space", "υδράργυρο": "υδράργυρος — mercury", "αναποδογύρισε": "αναποδογυρίζω — to turn upside down", "λεκάνη": "λεκάνη — basin", "συμπέρανε": "συμπεραίνω — to conclude", "γαμπρό": "γαμπρός — son-in-law; brother-in-law", "στήλη": "στήλη — column", "ανεβοκατέβαινε": "ανεβοκατεβαίνω — to go up and down", "πρόγνωσης": "πρόγνωση — forecast"}
})

ITEMS.append({
 "id": "l259-c1-int-onomata-kakokairion", "title": "Γιατί δίνουμε ονόματα στις κακοκαιρίες; Μια μετεωρολόγος εξηγεί", "title_en": "Why do we give names to storms? A meteorologist explains", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια ενημερωτική εκπομπή του ραδιοφώνου.",
 "script": [
  L("Δημοσιογράφος", "m", "Τα τελευταία χρόνια οι κακοκαιρίες έχουν ονόματα, όπως οι άνθρωποι. Πότε ξεκίνησε αυτή η συνήθεια;", "In recent years storms have names, like people. When did this habit begin?"),
  L("Μετεωρολόγος", "f", "Στις Ηνωμένες Πολιτείες οι τυφώνες παίρνουν επίσημα ονόματα από τη δεκαετία του 1950. Στην αρχή ήταν μόνο γυναικεία, κάτι που σήμερα ακούγεται απαράδεκτο· τα αντρικά ονόματα προστέθηκαν στα τέλη της δεκαετίας του 1970. Στην Ευρώπη η πρακτική γενικεύτηκε πολύ αργότερα. Η Βρετανία και η Ιρλανδία άρχισαν να ονομάζουν τις καταιγίδες το 2015, και σιγά σιγά ακολούθησαν κι άλλες χώρες, ανάμεσά τους και η Ελλάδα.", "In the United States hurricanes have had official names since the 1950s. At first they were only women's names, which sounds unacceptable today; men's names were added in the late 1970s. In Europe the practice spread much later. Britain and Ireland began naming storms in 2015, and gradually other countries followed, Greece among them."),
  L("Δημοσιογράφος", "m", "Και ποιος διαλέγει τα ονόματα;", "And who chooses the names?"),
  L("Μετεωρολόγος", "f", "Οι εθνικές μετεωρολογικές υπηρεσίες συνεργάζονται σε ομάδες γειτονικών χωρών και ετοιμάζουν από πριν έναν κατάλογο για κάθε χειμώνα. Τα ονόματα ακολουθούν συνήθως αλφαβητική σειρά, και ένα γυναικείο εναλλάσσεται με ένα αντρικό. Μια κακοκαιρία παίρνει όνομα μόνο όταν αναμένεται να προκαλέσει σοβαρά προβλήματα, όχι για κάθε μπόρα.", "National meteorological services work together in groups of neighbouring countries and prepare a list in advance for each winter. The names usually follow alphabetical order, and a woman's name alternates with a man's. A storm gets a name only when it is expected to cause serious problems, not for every shower."),
  L("Δημοσιογράφος", "m", "Δεν είναι λίγο θεατρικό όλο αυτό;", "Isn't all this a bit theatrical?"),
  L("Μετεωρολόγος", "f", "Το ερώτημα είναι λογικό, αλλά ο σκοπός είναι πρακτικός. Ένα όνομα το θυμάται κανείς πολύ πιο εύκολα από μια τεχνική περιγραφή, και οι πολίτες παίρνουν πιο σοβαρά μια προειδοποίηση όταν το φαινόμενο έχει ταυτότητα. Υπάρχει, βέβαια, και ο κίνδυνος του αντίθετου: αν τα μέσα ενημέρωσης παρουσιάζουν κάθε ονομασμένη κακοκαιρία σαν καταστροφή, ο κόσμος κουράζεται και στο τέλος δεν δίνει σημασία.", "The question is reasonable, but the purpose is practical. A name is much easier to remember than a technical description, and citizens take a warning more seriously when the phenomenon has an identity. There is, of course, also the opposite risk: if the media present every named storm as a disaster, people get tired and in the end stop paying attention."),
 ],
 "questions": [
  Q("Τι ίσχυε στην αρχή για τα ονόματα των τυφώνων στις Ηνωμένες Πολιτείες;", ["Ήταν αριθμοί", "Ήταν μόνο γυναικεία", "Ήταν ονόματα πόλεων", "Ήταν μόνο αντρικά"], 1, "Στην αρχή ήταν μόνο γυναικεία"),
  Q("Πότε άρχισαν η Βρετανία και η Ιρλανδία να ονομάζουν τις καταιγίδες;", ["Τη δεκαετία του 1950", "Στα τέλη της δεκαετίας του 1970", "Το 2015", "Το 2023"], 2, "άρχισαν να ονομάζουν τις καταιγίδες το 2015"),
  Q("Πότε παίρνει όνομα μια κακοκαιρία;", ["Για κάθε μπόρα", "Όταν αναμένεται να προκαλέσει σοβαρά προβλήματα", "Μόνο όταν έχει περάσει", "Όταν το ζητήσουν οι πολίτες"], 1, "μόνο όταν αναμένεται να προκαλέσει σοβαρά προβλήματα"),
  Q("Ποιον κίνδυνο αναφέρει η μετεωρολόγος;", ["Να μπερδευτούν τα ονόματα με ανθρώπους", "Να κουραστεί ο κόσμος και να μη δίνει σημασία", "Να τελειώσουν τα ονόματα", "Να ακριβύνουν οι προβλέψεις"], 1, "ο κόσμος κουράζεται και στο τέλος δεν δίνει σημασία"),
 ],
 "gloss": {"κακοκαιρίες": "κακοκαιρία — bad weather, storm", "τυφώνες": "τυφώνας — hurricane, typhoon", "απαράδεκτο": "απαράδεκτος — unacceptable", "γενικεύτηκε": "γενικεύομαι — to become widespread", "εναλλάσσεται": "εναλλάσσομαι — to alternate", "μπόρα": "μπόρα — shower, downpour", "θεατρικό": "θεατρικός — theatrical", "προειδοποίηση": "προειδοποίηση — warning", "φαινόμενο": "φαινόμενο — phenomenon"}
})
rnd = random.Random(259)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-259.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
