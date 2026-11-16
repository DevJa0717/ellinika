# Source for library/listening/listening-55.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l55.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l55-ann-apovathra", "title": "Αλλαγή αποβάθρας στον σταθμό", "title_en": "Platform change at the station", "type": "announcement", "level": "B2",
 "context_el": "Περιμένετε το τρένο για τη Θεσσαλονίκη στον σιδηροδρομικό σταθμό της Αθήνας. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Ανακοίνωση", "m", "Προσοχή, παρακαλώ. Το τρένο Intercity για Θεσσαλονίκη, με προγραμματισμένη αναχώρηση στις δέκα και είκοσι, δεν θα αναχωρήσει από την αποβάθρα τρία, όπως αναγράφεται στους πίνακες, αλλά από την αποβάθρα επτά. Παρακαλούνται οι επιβάτες να μεταβούν στην αποβάθρα επτά μέσω της υπόγειας διάβασης.", "Attention, please. The Intercity train to Thessaloniki, scheduled to depart at ten twenty, will not leave from platform three, as shown on the boards, but from platform seven. Passengers are requested to go to platform seven via the underpass."),
  L("Ανακοίνωση", "m", "Λόγω εργασιών στο δίκτυο, το τρένο θα αναχωρήσει με καθυστέρηση περίπου δεκαπέντε λεπτών. Οι επιβάτες με θέσεις στα βαγόνια ένα έως τρία παρακαλούνται να επιβιβαστούν από το μπροστινό τμήμα της αποβάθρας.", "Because of works on the network, the train will depart about fifteen minutes late. Passengers with seats in carriages one to three are requested to board from the front section of the platform."),
  L("Ανακοίνωση", "m", "Για επιβάτες με κινητικές δυσκολίες, υπάρχει ανελκυστήρας δίπλα στο εκδοτήριο εισιτηρίων. Ζητούμε συγγνώμη για την ταλαιπωρία.", "For passengers with reduced mobility, there is a lift next to the ticket office. We apologise for the inconvenience."),
 ],
 "questions": [
  Q("Από ποια αποβάθρα θα αναχωρήσει τελικά το τρένο;", ["Από την αποβάθρα τρία", "Από την αποβάθρα επτά", "Από την αποβάθρα ένα", "Δεν έχει ανακοινωθεί ακόμη"], 1, "δεν θα αναχωρήσει από την αποβάθρα τρία … αλλά από την αποβάθρα επτά"),
  Q("Γιατί θα καθυστερήσει το τρένο;", ["Λόγω απεργίας", "Λόγω εργασιών στο δίκτυο", "Λόγω κακοκαιρίας", "Λόγω βλάβης στο τρένο"], 1, "Λόγω εργασιών στο δίκτυο, το τρένο θα αναχωρήσει με καθυστέρηση περίπου δεκαπέντε λεπτών"),
  Q("Πού βρίσκεται ο ανελκυστήρας;", ["Στην αποβάθρα τρία", "Δίπλα στο εκδοτήριο εισιτηρίων", "Στο μπροστινό τμήμα της αποβάθρας", "Στην υπόγεια διάβαση"], 1, "υπάρχει ανελκυστήρας δίπλα στο εκδοτήριο εισιτηρίων"),
 ],
 "gloss": {"αποβάθρα": "αποβάθρα — platform", "αναγράφεται": "αναγράφομαι — to be shown, written", "μεταβούν": "μεταβαίνω — to go, proceed", "υπόγειας διάβασης": "υπόγεια διάβαση — underpass", "επιβιβαστούν": "επιβιβάζομαι — to board", "κινητικές δυσκολίες": "κινητικές δυσκολίες — reduced mobility", "ανελκυστήρας": "ανελκυστήρας — lift, elevator", "εκδοτήριο": "εκδοτήριο — ticket office", "ταλαιπωρία": "ταλαιπωρία — inconvenience"},
})

ITEMS.append({
 "id": "l55-vm-proponitis", "title": "Μήνυμα από τον προπονητή", "title_en": "A message from the coach", "type": "voicemail", "level": "B2",
 "context_el": "Ο γιος σας παίζει μπάσκετ σε μια ομάδα της γειτονιάς. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τον προπονητή του.",
 "script": [
  L("Προπονητής", "m", "Καλησπέρα, κύριε Αντωνίου, ο Λευτέρης είμαι, ο προπονητής του Φίλιππου. Σας παίρνω για δύο πράγματα. Πρώτα, το Σάββατο έχουμε αγώνα στη Νέα Σμύρνη, και επειδή το γήπεδο είναι μακριά, θα πάμε όλοι μαζί με ένα μικρό λεωφορείο. Θα φύγουμε στις εννιά ακριβώς από το κλειστό γυμναστήριο.", "Good evening, Mr Antoniou, it's Lefteris, Filippos's coach. I'm calling about two things. First, on Saturday we have a game in Nea Smyrni, and because the court is far away, we'll all go together in a minibus. We'll leave at nine sharp from the indoor sports hall."),
  L("Προπονητής", "m", "Δεύτερον, ήθελα να σας πω ότι ο Φίλιππος έχει βελτιωθεί πάρα πολύ. Είναι από τα πιο συνεπή παιδιά της ομάδας, δεν λείπει ποτέ από προπόνηση. Σκεφτόμαστε να τον προτείνουμε για την ομάδα της περιφέρειας, που κάνει προπονήσεις και την Κυριακή το πρωί.", "Secondly, I wanted to tell you that Filippos has improved a great deal. He's one of the most consistent kids on the team; he never misses training. We're thinking of putting him forward for the regional team, which also trains on Sunday mornings."),
  L("Προπονητής", "m", "Θα ήθελα να το συζητήσουμε πρώτα μαζί σας, γιατί είναι μια επιπλέον δέσμευση. Πάρτε με όποτε μπορείτε, εκτός από την Πέμπτη, που έχω προπονήσεις όλο το απόγευμα. Γεια σας.", "I'd like to discuss it with you first, because it's an extra commitment. Call me whenever you can, except Thursday, when I have training sessions all afternoon. Goodbye."),
 ],
 "questions": [
  Q("Πώς θα πάει η ομάδα στον αγώνα του Σαββάτου;", ["Με τα αυτοκίνητα των γονιών", "Όλοι μαζί με ένα μικρό λεωφορείο", "Με το μετρό", "Με τα πόδια"], 1, "θα πάμε όλοι μαζί με ένα μικρό λεωφορείο"),
  Q("Τι λέει ο προπονητής για τον Φίλιππο;", ["Ότι λείπει συχνά από τις προπονήσεις", "Ότι έχει βελτιωθεί πολύ και είναι συνεπής", "Ότι πρέπει να αλλάξει ομάδα", "Ότι τραυματίστηκε"], 1, "ο Φίλιππος έχει βελτιωθεί πάρα πολύ. Είναι από τα πιο συνεπή παιδιά της ομάδας"),
  Q("Πότε δεν μπορεί να μιλήσει ο προπονητής;", ["Το Σάββατο", "Την Πέμπτη", "Την Κυριακή το πρωί", "Κάθε πρωί"], 1, "εκτός από την Πέμπτη, που έχω προπονήσεις όλο το απόγευμα"),
 ],
 "gloss": {"γήπεδο": "γήπεδο — court, pitch", "κλειστό γυμναστήριο": "κλειστό γυμναστήριο — indoor sports hall", "βελτιωθεί": "βελτιώνομαι — to improve", "συνεπή": "συνεπής — consistent, reliable", "περιφέρειας": "περιφέρεια — region", "δέσμευση": "δέσμευση — commitment"},
})

ITEMS.append({
 "id": "l55-dia-asanser", "title": "Το ασανσέρ χάλασε πάλι", "title_en": "The lift has broken down again", "type": "dialogue", "level": "B2",
 "context_el": "Δύο γείτονες συναντιούνται στην είσοδο της πολυκατοικίας τους. Θα ακούσετε τη συζήτησή τους.",
 "script": [
  L("Κατερίνα", "f", "Καλημέρα, κύριε Στάθη. Μην πατάτε το κουμπί, δεν λειτουργεί. Το ασανσέρ χάλασε πάλι από χθες το βράδυ. Τρίτη φορά μέσα σε δύο μήνες!", "Good morning, Mr Stathis. Don't press the button, it isn't working. The lift has broken down again since last night. Third time in two months!"),
  L("Στάθης", "m", "Πάλι; Κι εγώ μένω στον έκτο, με το γόνατό μου σε αυτή την κατάσταση... Ειδοποίησε κανείς τον διαχειριστή;", "Again? And I live on the sixth floor, with my knee in this state... Has anyone told the building manager?"),
  L("Κατερίνα", "f", "Τον πήρα εγώ το πρωί. Λέει ότι ο τεχνικός θα έρθει το απόγευμα, αλλά ότι το μηχάνημα είναι πολύ παλιό και ότι κάποια στιγμή θα πρέπει να το αλλάξουμε. Το κόστος, βέβαια, θα το μοιραστούμε όλοι.", "I called him this morning. He says the technician will come in the afternoon, but that the machinery is very old and at some point we'll have to replace it. The cost, of course, we'll all share."),
  L("Στάθης", "m", "Καλύτερα να το αλλάξουμε μια και καλή, παρά να πληρώνουμε επισκευές κάθε μήνα. Να το προτείνουμε στη γενική συνέλευση την άλλη εβδομάδα.", "Better to replace it once and for all than pay for repairs every month. Let's propose it at the general meeting next week."),
  L("Κατερίνα", "f", "Συμφωνώ. Και μέχρι τότε, αν χρειάζεστε κάτι από το σούπερ μάρκετ, πείτε μου. Θα σας το ανεβάσω εγώ, δεν με πειράζει.", "I agree. And until then, if you need anything from the supermarket, tell me. I'll bring it up for you, I don't mind."),
 ],
 "questions": [
  Q("Πόσες φορές έχει χαλάσει το ασανσέρ τους τελευταίους δύο μήνες;", ["Μία", "Τρεις", "Δύο", "Τέσσερις"], 1, "Τρίτη φορά μέσα σε δύο μήνες"),
  Q("Τι είπε ο διαχειριστής για το μηχάνημα;", ["Ότι είναι καινούργιο", "Ότι είναι πολύ παλιό και κάποια στιγμή πρέπει να αλλάξει", "Ότι δεν χρειάζεται επισκευή", "Ότι θα το πληρώσει ο ίδιος"], 1, "το μηχάνημα είναι πολύ παλιό και ότι κάποια στιγμή θα πρέπει να το αλλάξουμε"),
  Q("Τι προσφέρεται να κάνει η Κατερίνα;", ["Να καλέσει η ίδια τον τεχνικό", "Να του ανεβάζει ό,τι χρειάζεται από το σούπερ μάρκετ", "Να πληρώσει την επισκευή", "Να τον πάει στον γιατρό"], 1, "αν χρειάζεστε κάτι από το σούπερ μάρκετ, πείτε μου. Θα σας το ανεβάσω εγώ"),
 ],
 "gloss": {"διαχειριστή": "διαχειριστής — building manager", "τεχνικός": "τεχνικός — technician", "μηχάνημα": "μηχάνημα — machine, machinery", "μοιραστούμε": "μοιράζομαι — to share", "μια και καλή": "μια και καλή — once and for all", "γενική συνέλευση": "γενική συνέλευση — general meeting", "δεν με πειράζει": "δεν με πειράζει — I don't mind"},
})

ITEMS.append({
 "id": "l55-dia-souvlaki", "title": "Σούσι ή σουβλάκι;", "title_en": "Sushi or souvlaki?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι αποφασίζει τι θα παραγγείλει για βραδινό. Θα ακούσετε τη συζήτησή τους.",
 "script": [
  L("Νίκος", "m", "Δεν έχω καμία όρεξη να μαγειρέψω απόψε. Λέω να παραγγείλουμε. Τι λες για σουβλάκια από το μαγαζί της γωνίας;", "I really don't feel like cooking tonight. I say we order. What about souvlaki from the place on the corner?"),
  L("Ελένη", "f", "Πάλι σουβλάκια; Τα φάγαμε και την Τρίτη. Εγώ θα ήθελα κάτι πιο ελαφρύ. Έχει ανοίξει ένα καινούργιο ιαπωνικό στην πλατεία, και η Δέσποινα λέει ότι το σούσι τους είναι εξαιρετικό.", "Souvlaki again? We had them on Tuesday too. I'd like something lighter. A new Japanese place has opened on the square, and Despoina says their sushi is excellent."),
  L("Νίκος", "m", "Σούσι; Είναι τριπλάσια τιμή και μετά από μία ώρα πεινάω ξανά. Και η παράδοση από εκεί αργεί σίγουρα, είναι Παρασκευή βράδυ.", "Sushi? It's three times the price and an hour later I'm hungry again. And delivery from there is bound to be slow, it's Friday night."),
  L("Ελένη", "f", "Ε, τότε ας κάνουμε έναν συμβιβασμό. Παίρνουμε μια μεγάλη σαλάτα και καλαμάκια κοτόπουλο από το ψητοπωλείο, και την Κυριακή πάμε μαζί να δοκιμάσουμε το σούσι από κοντά.", "Well, then let's compromise. We get a big salad and chicken skewers from the grill house, and on Sunday we go together to try the sushi in person."),
  L("Νίκος", "m", "Σύμφωνοι. Αλλά την Κυριακή κερνάς εσύ!", "Deal. But on Sunday it's your treat!"),
 ],
 "questions": [
  Q("Γιατί η Ελένη δεν θέλει σουβλάκια;", ["Γιατί είναι ακριβά", "Γιατί τα έφαγαν και την Τρίτη", "Γιατί είναι χορτοφάγος", "Γιατί το μαγαζί είναι κλειστό"], 1, "Πάλι σουβλάκια; Τα φάγαμε και την Τρίτη"),
  Q("Ποια αντίρρηση έχει ο Νίκος για το σούσι;", ["Δεν του αρέσει το ψάρι", "Είναι ακριβό και δεν τον χορταίνει", "Το μαγαζί είναι μακριά", "Δεν κάνει παράδοση"], 1, "Είναι τριπλάσια τιμή και μετά από μία ώρα πεινάω ξανά"),
  Q("Τι αποφασίζουν τελικά;", ["Να μαγειρέψουν μαζί", "Σαλάτα και καλαμάκια κοτόπουλο απόψε, σούσι την Κυριακή", "Σούσι απόψε", "Να βγουν σε ταβέρνα"], 1, "Παίρνουμε μια μεγάλη σαλάτα και καλαμάκια κοτόπουλο … και την Κυριακή πάμε μαζί να δοκιμάσουμε το σούσι"),
 ],
 "gloss": {"όρεξη": "όρεξη — appetite; mood (to do something)", "ελαφρύ": "ελαφρύς — light", "τριπλάσια": "τριπλάσιος — triple, three times as much", "παράδοση": "παράδοση — delivery", "συμβιβασμό": "συμβιβασμός — compromise", "ψητοπωλείο": "ψητοπωλείο — grill house", "κερνάς": "κερνάω — to treat (someone)"},
})

ITEMS.append({
 "id": "l55-int-meteorologos", "title": "Μια μετεωρολόγος", "title_en": "A meteorologist", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια μετεωρολόγο για τη δουλειά της.",
 "script": [
  L("Δημοσιογράφος", "m", "Μαζί μας σήμερα η μετεωρολόγος Ιφιγένεια Ραφαηλίδου. Κυρία Ραφαηλίδου, πώς γίνεται στην πράξη μια πρόγνωση καιρού;", "With us today is the meteorologist Ifigeneia Rafailidou. Ms Rafailidou, how is a weather forecast actually made?"),
  L("Μετεωρολόγος", "f", "Συλλέγουμε δεδομένα από μετεωρολογικούς σταθμούς, δορυφόρους και ραντάρ σε όλο τον κόσμο. Αυτά τα δεδομένα τα επεξεργάζονται ισχυροί υπολογιστές, που τρέχουν μαθηματικά μοντέλα της ατμόσφαιρας. Η δική μας δουλειά είναι να ερμηνεύσουμε τα αποτελέσματα και να τα κάνουμε κατανοητά στο κοινό.", "We collect data from weather stations, satellites and radar all over the world. Powerful computers process this data, running mathematical models of the atmosphere. Our job is to interpret the results and make them understandable to the public."),
  L("Δημοσιογράφος", "m", "Πόσο αξιόπιστες είναι οι προγνώσεις σήμερα;", "How reliable are forecasts today?"),
  L("Μετεωρολόγος", "f", "Πολύ πιο αξιόπιστες από ό,τι πριν από είκοσι χρόνια. Για τις επόμενες τρεις μέρες η ακρίβεια είναι πολύ υψηλή. Μετά από επτά με δέκα μέρες, όμως, η αβεβαιότητα μεγαλώνει πολύ. Όποιος σας λέει τι καιρό θα κάνει σε έναν μήνα, απλώς μαντεύει.", "Much more reliable than twenty years ago. For the next three days accuracy is very high. After seven to ten days, though, uncertainty grows a great deal. Anyone who tells you what the weather will be like in a month is simply guessing."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο δύσκολο κομμάτι της δουλειάς σας;", "What is the hardest part of your job?"),
  L("Μετεωρολόγος", "f", "Οι προειδοποιήσεις για ακραία φαινόμενα. Αν προειδοποιήσεις και τελικά δεν γίνει τίποτα, ο κόσμος σε κατηγορεί για πανικό. Αν δεν προειδοποιήσεις, μπορεί να κινδυνεύσουν ζωές. Είναι μια μεγάλη ευθύνη.", "Warnings about extreme weather. If you issue a warning and in the end nothing happens, people accuse you of causing panic. If you don't warn, lives may be at risk. It's a great responsibility."),
 ],
 "questions": [
  Q("Ποιος επεξεργάζεται τα δεδομένα από τους σταθμούς και τους δορυφόρους;", ["Οι ίδιοι οι μετεωρολόγοι με το χέρι", "Ισχυροί υπολογιστές με μαθηματικά μοντέλα", "Οι δημοσιογράφοι", "Οι πιλότοι"], 1, "Αυτά τα δεδομένα τα επεξεργάζονται ισχυροί υπολογιστές, που τρέχουν μαθηματικά μοντέλα"),
  Q("Για πόσες μέρες, κατά τη μετεωρολόγο, η ακρίβεια είναι πολύ υψηλή;", ["Για έναν μήνα", "Για τις επόμενες τρεις μέρες", "Για δέκα μέρες", "Για μία εβδομάδα"], 1, "Για τις επόμενες τρεις μέρες η ακρίβεια είναι πολύ υψηλή"),
  Q("Γιατί είναι δύσκολες οι προειδοποιήσεις για ακραία φαινόμενα;", ["Γιατί δεν υπάρχουν δεδομένα", "Γιατί, αν δεν γίνει τίποτα, την κατηγορούν για πανικό, κι αν δεν προειδοποιήσει, κινδυνεύουν ζωές", "Γιατί απαγορεύονται από τον νόμο", "Γιατί δεν τις ακούει κανείς"], 1, "Αν προειδοποιήσεις και τελικά δεν γίνει τίποτα, ο κόσμος σε κατηγορεί για πανικό. Αν δεν προειδοποιήσεις, μπορεί να κινδυνεύσουν ζωές"),
 ],
 "gloss": {"πρόγνωση": "πρόγνωση — forecast", "δεδομένα": "δεδομένα — data", "δορυφόρους": "δορυφόρος — satellite", "επεξεργάζονται": "επεξεργάζομαι — to process", "ερμηνεύσουμε": "ερμηνεύω — to interpret", "αξιόπιστες": "αξιόπιστος — reliable", "αβεβαιότητα": "αβεβαιότητα — uncertainty", "μαντεύει": "μαντεύω — to guess", "ακραία φαινόμενα": "ακραία φαινόμενα — extreme weather events"},
})

ITEMS.append({
 "id": "l55-rep-festival", "title": "Το Φεστιβάλ Κινηματογράφου Θεσσαλονίκης", "title_en": "The Thessaloniki Film Festival", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από το λιμάνι της Θεσσαλονίκης, όπου γίνεται το Φεστιβάλ Κινηματογράφου.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρίσκομαι στις παλιές αποθήκες του λιμανιού της Θεσσαλονίκης, εκεί όπου χτυπά αυτές τις μέρες η καρδιά του Φεστιβάλ Κινηματογράφου. Το φεστιβάλ, που πρωτοοργανώθηκε το 1960 ως Εβδομάδα Ελληνικού Κινηματογράφου, είναι σήμερα ένα από τα σημαντικότερα της νοτιοανατολικής Ευρώπης.", "I'm at the old warehouses of Thessaloniki port, where the heart of the Film Festival beats these days. The festival, first organised in 1960 as the Week of Greek Cinema, is today one of the most important in south-eastern Europe."),
  L("Ρεπόρτερ", "f", "Φέτος προβάλλονται πάνω από διακόσιες ταινίες από όλο τον κόσμο, ανάμεσά τους πολλές πρώτες ταινίες νέων σκηνοθετών. Οι ουρές έξω από τις αίθουσες ξεκινούν από νωρίς το πρωί, και τα εισιτήρια για τις πιο πολυσυζητημένες προβολές εξαντλούνται μέσα σε λίγα λεπτά.", "This year over two hundred films from all over the world are being screened, among them many first films by young directors. The queues outside the cinemas start early in the morning, and tickets for the most talked-about screenings sell out within minutes."),
  L("Ρεπόρτερ", "f", "Το φεστιβάλ δεν απευθύνεται μόνο στους επαγγελματίες. Οι φοιτητές έχουν μειωμένο εισιτήριο, και κάθε βράδυ, μετά την προβολή, το κοινό μπορεί να συζητήσει με τους συντελεστές της ταινίας. Όπως μου είπε μια θεατής, «εδώ δεν βλέπεις απλώς ταινίες· ζεις μέσα σε αυτές για δέκα μέρες».", "The festival is not aimed only at professionals. Students get reduced tickets, and every evening, after the screening, the audience can talk with the film's cast and crew. As one viewer told me, \"here you don't just watch films; you live inside them for ten days\"."),
 ],
 "questions": [
  Q("Πώς ονομαζόταν το φεστιβάλ όταν πρωτοοργανώθηκε;", ["Φεστιβάλ Ντοκιμαντέρ", "Εβδομάδα Ελληνικού Κινηματογράφου", "Διεθνής Έκθεση Θεσσαλονίκης", "Φεστιβάλ Νέων Σκηνοθετών"], 1, "πρωτοοργανώθηκε το 1960 ως Εβδομάδα Ελληνικού Κινηματογράφου"),
  Q("Τι συμβαίνει με τα εισιτήρια για τις πιο πολυσυζητημένες προβολές;", ["Είναι δωρεάν", "Εξαντλούνται μέσα σε λίγα λεπτά", "Πωλούνται μόνο σε επαγγελματίες", "Είναι πολύ ακριβά"], 1, "τα εισιτήρια για τις πιο πολυσυζητημένες προβολές εξαντλούνται μέσα σε λίγα λεπτά"),
  Q("Τι μπορεί να κάνει το κοινό μετά την προβολή;", ["Να ψηφίσει την καλύτερη ταινία", "Να συζητήσει με τους συντελεστές της ταινίας", "Να δει την ταινία ξανά δωρεάν", "Να γνωρίσει τους κριτικούς"], 1, "μετά την προβολή, το κοινό μπορεί να συζητήσει με τους συντελεστές της ταινίας"),
 ],
 "gloss": {"αποθήκες": "αποθήκη — warehouse", "πρωτοοργανώθηκε": "πρωτοοργανώνομαι — to be organised for the first time", "προβάλλονται": "προβάλλομαι — to be screened", "σκηνοθετών": "σκηνοθέτης — director", "πολυσυζητημένες": "πολυσυζητημένος — much talked-about", "εξαντλούνται": "εξαντλούμαι — to sell out, run out", "απευθύνεται": "απευθύνομαι — to be aimed at", "συντελεστές": "συντελεστές — cast and crew (of a film)"},
})

ITEMS.append({
 "id": "l55-dia-plaka", "title": "Χαμένοι στα στενά της Πλάκας", "title_en": "Lost in the alleys of Plaka", "type": "dialogue", "level": "B2",
 "context_el": "Μια τουρίστρια που μιλάει ελληνικά ζητάει οδηγίες από έναν περαστικό στην Πλάκα. Θα ακούσετε τη συζήτησή τους.",
 "script": [
  L("Μάγκνταλενα", "f", "Συγγνώμη, μπορείτε να με βοηθήσετε; Ψάχνω το Μουσείο Ελληνικών Λαϊκών Μουσικών Οργάνων, αλλά ο χάρτης στο κινητό μου με έχει φέρει τρεις φορές στο ίδιο σημείο.", "Excuse me, can you help me? I'm looking for the Museum of Greek Folk Musical Instruments, but the map on my phone has brought me back to the same spot three times."),
  L("Περαστικός", "m", "Συμβαίνει συχνά εδώ, τα στενά μπερδεύουν και τους Αθηναίους. Λοιπόν, είστε πολύ κοντά. Ανεβείτε αυτά τα σκαλάκια, και στην κορυφή στρίψτε δεξιά. Θα βγείτε σε μια μικρή πλατεία με μια εκκλησία.", "It happens a lot here; the alleys confuse even Athenians. Well, you're very close. Go up these little steps, and at the top turn right. You'll come out into a small square with a church."),
  L("Μάγκνταλενα", "f", "Σκαλάκια, δεξιά, πλατεία με εκκλησία. Και μετά;", "Steps, right, square with a church. And then?"),
  L("Περαστικός", "m", "Από την πλατεία πάρτε τον δρόμο δίπλα στο καφενείο, όχι εκείνον που κατεβαίνει. Το μουσείο είναι στο τρίτο κτίριο αριστερά, ένα παλιό αρχοντικό με πράσινη πόρτα. Αλλά προσέξτε, κλείνει στις δύο και μισή, και είναι ήδη δύο.", "From the square take the street next to the café, not the one going down. The museum is the third building on the left, an old mansion with a green door. But be careful, it closes at half past two, and it's already two."),
  L("Μάγκνταλενα", "f", "Τότε πρέπει να βιαστώ! Ευχαριστώ πάρα πολύ, ήσασταν πολύ ευγενικός.", "Then I'd better hurry! Thank you very much, you were very kind."),
 ],
 "questions": [
  Q("Ποιο πρόβλημα έχει η Μάγκνταλενα με τον χάρτη;", ["Δεν έχει μπαταρία", "Την έχει φέρει τρεις φορές στο ίδιο σημείο", "Είναι στα αγγλικά", "Δεν δείχνει το μουσείο"], 1, "ο χάρτης στο κινητό μου με έχει φέρει τρεις φορές στο ίδιο σημείο"),
  Q("Πώς θα αναγνωρίσει το κτίριο του μουσείου;", ["Είναι δίπλα στην εκκλησία", "Είναι ένα παλιό αρχοντικό με πράσινη πόρτα", "Έχει μια μεγάλη πινακίδα", "Είναι απέναντι από το καφενείο"], 1, "ένα παλιό αρχοντικό με πράσινη πόρτα"),
  Q("Γιατί πρέπει να βιαστεί;", ["Γιατί θα βρέξει", "Γιατί το μουσείο κλείνει σε μισή ώρα", "Γιατί την περιμένουν φίλοι", "Γιατί φεύγει το πλοίο της"], 1, "κλείνει στις δύο και μισή, και είναι ήδη δύο"),
 ],
 "gloss": {"στενά": "στενά — alleys, narrow streets", "μπερδεύουν": "μπερδεύω — to confuse", "σκαλάκια": "σκαλάκια — little steps", "στρίψτε": "στρίβω — to turn", "αρχοντικό": "αρχοντικό — mansion", "βιαστώ": "βιάζομαι — to hurry"},
})

ITEMS.append({
 "id": "l55-mono-kykladiko", "title": "Ξενάγηση στο Μουσείο Κυκλαδικής Τέχνης", "title_en": "A tour of the Museum of Cycladic Art", "type": "monologue", "level": "B2",
 "context_el": "Επισκέπτεστε το Μουσείο Κυκλαδικής Τέχνης στην Αθήνα με μια ομάδα. Θα ακούσετε τον ξεναγό στην αρχή της ξενάγησης.",
 "script": [
  L("Ξεναγός", "m", "Καλώς ήρθατε στο Μουσείο Κυκλαδικής Τέχνης. Το μουσείο ιδρύθηκε το 1986, για να στεγάσει τη συλλογή του Νικόλα και της Ντόλλης Γουλανδρή, που είχαν συγκεντρώσει αρχαιότητες από τις Κυκλάδες για πολλές δεκαετίες.", "Welcome to the Museum of Cycladic Art. The museum was founded in 1986 to house the collection of Nikolas and Dolly Goulandris, who had gathered antiquities from the Cyclades over many decades."),
  L("Ξεναγός", "m", "Στον πρώτο όροφο θα δείτε τα περίφημα κυκλαδικά ειδώλια, μαρμάρινες μορφές από την τρίτη χιλιετία π.Χ. Τα περισσότερα παριστάνουν γυναίκες με τα χέρια διπλωμένα πάνω στην κοιλιά. Η απλότητά τους εντυπωσίασε καλλιτέχνες του εικοστού αιώνα, όπως ο Πικάσο και ο Μοντιλιάνι.", "On the first floor you will see the famous Cycladic figurines, marble figures from the third millennium BC. Most of them depict women with their arms folded over the belly. Their simplicity impressed twentieth-century artists such as Picasso and Modigliani."),
  L("Ξεναγός", "m", "Αξίζει να ξέρετε ότι αρχικά τα ειδώλια δεν ήταν λευκά. Έρευνες έχουν δείξει ίχνη χρώματος, που σημαίνει ότι είχαν ζωγραφισμένα μάτια, κοσμήματα και άλλες λεπτομέρειες. Τη χρήση τους, πάντως, ακόμη δεν την ξέρουμε με βεβαιότητα. Μετά τον πρώτο όροφο, θα περάσουμε στο αρχοντικό Σταθάτου, που συνδέεται με το κυρίως κτίριο με έναν γυάλινο διάδρομο.", "It is worth knowing that originally the figurines were not white. Research has shown traces of paint, which means they had painted eyes, jewellery and other details. Their use, however, we still do not know for certain. After the first floor, we will move on to the Stathatos mansion, which is connected to the main building by a glass corridor."),
 ],
 "questions": [
  Q("Ποια συλλογή στεγάζει το μουσείο;", ["Του Υπουργείου Πολιτισμού", "Του Νικόλα και της Ντόλλης Γουλανδρή", "Του Αντώνη Μπενάκη", "Ενός Γάλλου αρχαιολόγου"], 1, "για να στεγάσει τη συλλογή του Νικόλα και της Ντόλλης Γουλανδρή"),
  Q("Τι παριστάνουν τα περισσότερα ειδώλια;", ["Ζώα", "Γυναίκες με τα χέρια διπλωμένα πάνω στην κοιλιά", "Πολεμιστές", "Μουσικούς"], 1, "Τα περισσότερα παριστάνουν γυναίκες με τα χέρια διπλωμένα πάνω στην κοιλιά"),
  Q("Τι έχουν δείξει οι έρευνες για τα ειδώλια;", ["Ότι είναι αντίγραφα", "Ότι αρχικά είχαν χρώμα", "Ότι φτιάχτηκαν στην Αθήνα", "Ότι ήταν παιχνίδια"], 1, "Έρευνες έχουν δείξει ίχνη χρώματος"),
 ],
 "gloss": {"στεγάσει": "στεγάζω — to house", "αρχαιότητες": "αρχαιότητες — antiquities", "ειδώλια": "ειδώλιο — figurine", "χιλιετία": "χιλιετία — millennium", "παριστάνουν": "παριστάνω — to depict", "ίχνη": "ίχνος — trace", "βεβαιότητα": "βεβαιότητα — certainty", "διάδρομο": "διάδρομος — corridor"},
})

ITEMS.append({
 "id": "l55-c1-synomosia", "title": "Γιατί πιστεύουμε σε θεωρίες συνωμοσίας;", "title_en": "Why do we believe in conspiracy theories?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν κοινωνικό ψυχολόγο για τις θεωρίες συνωμοσίας.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Παπαγεωργίου, γιατί οι θεωρίες συνωμοσίας βρίσκουν τόσο πρόσφορο έδαφος, ακόμη και σε μορφωμένους ανθρώπους;", "Mr Papageorgiou, why do conspiracy theories find such fertile ground, even among educated people?"),
  L("Ψυχολόγος", "m", "Γιατί ικανοποιούν βαθιές ψυχολογικές ανάγκες, που δεν έχουν σχέση με το μορφωτικό επίπεδο. Η πρώτη είναι η ανάγκη για έλεγχο. Όταν συμβαίνει κάτι τρομακτικό και χαοτικό, όπως μια πανδημία, είναι παραδόξως πιο καθησυχαστικό να πιστεύουμε ότι κάποιος το σχεδίασε, παρά να δεχτούμε ότι οφείλεται στην τύχη ή σε μια αλυσίδα συμπτώσεων.", "Because they satisfy deep psychological needs that have nothing to do with level of education. The first is the need for control. When something frightening and chaotic happens, such as a pandemic, it is paradoxically more reassuring to believe that someone planned it than to accept that it is due to chance or a chain of coincidences."),
  L("Δημοσιογράφος", "f", "Και οι άλλες ανάγκες;", "And the other needs?"),
  L("Ψυχολόγος", "m", "Η ανάγκη να ξεχωρίζουμε: όποιος πιστεύει ότι γνωρίζει την «κρυφή αλήθεια» νιώθει ότι ανήκει σε μια μειοψηφία διορατικών, σε αντίθεση με τους «αφελείς». Και, βέβαια, η δυσπιστία προς τους θεσμούς. Όπου οι πολίτες έχουν βιώσει πραγματικά σκάνδαλα και συγκαλύψεις, η καχυποψία δεν είναι παράλογη· γίνεται επικίνδυνη όταν γενικεύεται και δεν δέχεται καμία διάψευση.", "The need to stand out: whoever believes they know the \"hidden truth\" feels they belong to a minority of the perceptive, as opposed to the \"naive\". And, of course, distrust of institutions. Where citizens have experienced real scandals and cover-ups, suspicion is not irrational; it becomes dangerous when it is generalised and accepts no refutation."),
  L("Δημοσιογράφος", "f", "Πώς πρέπει να συζητάμε με κάποιον που πιστεύει σε τέτοιες θεωρίες;", "How should we talk to someone who believes in such theories?"),
  L("Ψυχολόγος", "m", "Σίγουρα όχι με χλευασμό· αυτό τον ωθεί ακόμη πιο βαθιά. Οι έρευνες δείχνουν ότι αποδίδει περισσότερο να κάνουμε ερωτήσεις, να ζητάμε από τον συνομιλητή μας να εξηγήσει πώς ακριβώς θα λειτουργούσε η υποτιθέμενη συνωμοσία. Συχνά, προσπαθώντας να την εξηγήσει, συνειδητοποιεί μόνος του τα κενά της.", "Certainly not with mockery; that pushes them even deeper. Research shows that it works better to ask questions, to ask the person to explain exactly how the supposed conspiracy would work. Often, in trying to explain it, they realise its gaps on their own."),
 ],
 "questions": [
  Q("Γιατί, σύμφωνα με τον ψυχολόγο, οι θεωρίες συνωμοσίας πείθουν και μορφωμένους ανθρώπους;", ["Γιατί είναι επιστημονικά τεκμηριωμένες", "Γιατί ικανοποιούν βαθιές ψυχολογικές ανάγκες", "Γιατί τις διαδίδουν τα μέσα ενημέρωσης", "Γιατί οι μορφωμένοι διαβάζουν περισσότερο"], 1, "Γιατί ικανοποιούν βαθιές ψυχολογικές ανάγκες, που δεν έχουν σχέση με το μορφωτικό επίπεδο"),
  Q("Γιατί είναι «καθησυχαστικό» να πιστεύουμε ότι κάποιος σχεδίασε ένα χαοτικό γεγονός;", ["Γιατί έτσι μπορούμε να τιμωρήσουμε τους υπευθύνους", "Γιατί είναι πιο εύκολο από το να δεχτούμε την τύχη ή τις συμπτώσεις", "Γιατί έτσι δεν χρειάζεται να κάνουμε τίποτα", "Γιατί το πιστεύουν όλοι"], 1, "είναι παραδόξως πιο καθησυχαστικό να πιστεύουμε ότι κάποιος το σχεδίασε, παρά να δεχτούμε ότι οφείλεται στην τύχη"),
  Q("Πότε, κατά τον ψυχολόγο, η καχυποψία γίνεται επικίνδυνη;", ["Όταν στρέφεται κατά της κυβέρνησης", "Όταν γενικεύεται και δεν δέχεται καμία διάψευση", "Όταν βασίζεται σε πραγματικά σκάνδαλα", "Όταν τη μοιράζονται πολλοί"], 1, "γίνεται επικίνδυνη όταν γενικεύεται και δεν δέχεται καμία διάψευση"),
  Q("Τι προτείνει για τη συζήτηση με κάποιον που πιστεύει σε τέτοιες θεωρίες;", ["Να τον γελοιοποιούμε", "Να του ζητάμε να εξηγήσει πώς ακριβώς θα λειτουργούσε η συνωμοσία", "Να αποφεύγουμε το θέμα", "Να του στέλνουμε επιστημονικά άρθρα"], 1, "αποδίδει περισσότερο να κάνουμε ερωτήσεις, να ζητάμε από τον συνομιλητή μας να εξηγήσει πώς ακριβώς θα λειτουργούσε"),
 ],
 "gloss": {"πρόσφορο έδαφος": "πρόσφορο έδαφος — fertile ground", "καθησυχαστικό": "καθησυχαστικός — reassuring", "συμπτώσεων": "σύμπτωση — coincidence", "διορατικών": "διορατικός — perceptive, far-sighted", "αφελείς": "αφελής — naive", "δυσπιστία": "δυσπιστία — distrust", "συγκαλύψεις": "συγκάλυψη — cover-up", "καχυποψία": "καχυποψία — suspicion", "διάψευση": "διάψευση — refutation, denial", "χλευασμό": "χλευασμός — mockery", "ωθεί": "ωθώ — to push"},
})

ITEMS.append({
 "id": "l55-c1-goudi", "title": "Το κίνημα στο Γουδί", "title_en": "The Goudi coup of 1909", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια ομιλία ενός ιστορικού για το στρατιωτικό κίνημα στο Γουδί το 1909 και τις συνέπειές του.",
 "script": [
  L("Ιστορικός", "f", "Στις αρχές του εικοστού αιώνα, η Ελλάδα βρισκόταν σε βαθιά κρίση. Η ταπεινωτική ήττα του 1897 από τους Οθωμανούς είχε κλονίσει την εμπιστοσύνη στο πολιτικό σύστημα, ενώ η χώρα, υπό διεθνή οικονομικό έλεγχο, δεν φαινόταν ικανή να διεκδικήσει τους εθνικούς της στόχους.", "At the beginning of the twentieth century, Greece was in deep crisis. The humiliating defeat of 1897 by the Ottomans had shaken confidence in the political system, while the country, under international financial control, did not seem capable of pursuing its national aims."),
  L("Ιστορικός", "f", "Μέσα σε αυτό το κλίμα δημιουργήθηκε ο Στρατιωτικός Σύνδεσμος, μια οργάνωση κατώτερων αξιωματικών. Τον Αύγουστο του 1909 οι αξιωματικοί συγκεντρώθηκαν στους στρατώνες του Γουδιού, στην Αθήνα, και ζήτησαν από την κυβέρνηση και τον βασιλιά ριζικές μεταρρυθμίσεις στον στρατό, στη διοίκηση και στα οικονομικά. Η κυβέρνηση παραιτήθηκε, και ο θρόνος υποχώρησε.", "In this climate the Military League was formed, an organisation of junior officers. In August 1909 the officers gathered at the Goudi barracks in Athens and demanded from the government and the king radical reforms in the army, the administration and the economy. The government resigned, and the throne gave way."),
  L("Ιστορικός", "f", "Οι αξιωματικοί, ωστόσο, δεν είχαν ούτε την εμπειρία ούτε τη διάθεση να κυβερνήσουν οι ίδιοι. Γι' αυτό κάλεσαν από την Κρήτη έναν πολιτικό που είχε ήδη διακριθεί εκεί: τον Ελευθέριο Βενιζέλο. Το 1910 ο Βενιζέλος έγινε πρωθυπουργός, και ο Σύνδεσμος διαλύθηκε.", "The officers, however, had neither the experience nor the inclination to govern themselves. So they invited from Crete a politician who had already distinguished himself there: Eleftherios Venizelos. In 1910 Venizelos became prime minister, and the League was dissolved."),
  L("Ιστορικός", "f", "Οι μεταρρυθμίσεις που ακολούθησαν, με την αναθεώρηση του Συντάγματος το 1911 και την αναδιοργάνωση του στρατού, προετοίμασαν τη χώρα για τους Βαλκανικούς Πολέμους, που διπλασίασαν σχεδόν την έκτασή της. Το Γουδί, λοιπόν, θεωρείται συχνά τομή στη νεότερη ελληνική ιστορία, αν και άνοιξε επίσης τον δρόμο για τις συχνές επεμβάσεις του στρατού στην πολιτική τις επόμενες δεκαετίες.", "The reforms that followed, with the revision of the Constitution in 1911 and the reorganisation of the army, prepared the country for the Balkan Wars, which almost doubled its territory. Goudi, then, is often seen as a turning point in modern Greek history, although it also paved the way for the army's frequent interventions in politics in the following decades."),
 ],
 "questions": [
  Q("Τι είχε κλονίσει την εμπιστοσύνη στο πολιτικό σύστημα;", ["Η Μικρασιατική Καταστροφή", "Η ήττα του 1897 από τους Οθωμανούς", "Οι Βαλκανικοί Πόλεμοι", "Η πτώχευση του 1932"], 1, "Η ταπεινωτική ήττα του 1897 από τους Οθωμανούς είχε κλονίσει την εμπιστοσύνη στο πολιτικό σύστημα"),
  Q("Τι ζήτησαν οι αξιωματικοί στο Γουδί;", ["Να γίνουν οι ίδιοι κυβέρνηση", "Ριζικές μεταρρυθμίσεις στον στρατό, στη διοίκηση και στα οικονομικά", "Να φύγει ο βασιλιάς", "Να κηρυχθεί πόλεμος"], 1, "ζήτησαν από την κυβέρνηση και τον βασιλιά ριζικές μεταρρυθμίσεις στον στρατό, στη διοίκηση και στα οικονομικά"),
  Q("Γιατί οι αξιωματικοί κάλεσαν τον Βενιζέλο;", ["Γιατί ήταν και αυτός αξιωματικός", "Γιατί δεν είχαν την εμπειρία ούτε τη διάθεση να κυβερνήσουν οι ίδιοι", "Γιατί τον πρότεινε ο βασιλιάς", "Γιατί είχε κερδίσει τις εκλογές"], 1, "δεν είχαν ούτε την εμπειρία ούτε τη διάθεση να κυβερνήσουν οι ίδιοι"),
  Q("Ποια αρνητική συνέπεια του κινήματος αναφέρει η ιστορικός;", ["Τη διάλυση του στρατού", "Ότι άνοιξε τον δρόμο για συχνές επεμβάσεις του στρατού στην πολιτική", "Την ήττα στους Βαλκανικούς Πολέμους", "Την κατάργηση του Συντάγματος"], 1, "άνοιξε επίσης τον δρόμο για τις συχνές επεμβάσεις του στρατού στην πολιτική"),
 ],
 "gloss": {"ταπεινωτική": "ταπεινωτικός — humiliating", "κλονίσει": "κλονίζω — to shake, undermine", "διεκδικήσει": "διεκδικώ — to claim, pursue", "Στρατιωτικός Σύνδεσμος": "Στρατιωτικός Σύνδεσμος — the Military League (1909)", "στρατώνες": "στρατώνας — barracks", "μεταρρυθμίσεις": "μεταρρύθμιση — reform", "υποχώρησε": "υποχωρώ — to give way", "διακριθεί": "διακρίνομαι — to distinguish oneself", "αναθεώρηση": "αναθεώρηση — revision", "τομή": "τομή — turning point", "επεμβάσεις": "επέμβαση — intervention"},
})

rnd = random.Random(55)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-55.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
