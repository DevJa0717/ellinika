# Source for library/listening/listening-153.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l153.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l153-vm-mathima-pianou", "title": "Αλλαγή στο μάθημα πιάνου", "title_en": "A change to the piano lesson", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη δασκάλα πιάνου της κόρης σας.",
 "script": [
  L("Δασκάλα", "f", "Καλησπέρα, η Ρένα είμαι, η δασκάλα του πιάνου της Δάφνης. Σας παίρνω γιατί την Πέμπτη πρέπει να πάω σε μια συναυλία μαθητών στη Λάρισα, οπότε δεν θα μπορέσω να κάνουμε μάθημα στις πέντε.", "Good evening, it's Rena, Dafni's piano teacher. I'm calling because on Thursday I have to go to a student concert in Larissa, so I won't be able to give the lesson at five."),
  L("Δασκάλα", "f", "Μπορούμε να το μεταφέρουμε στο Σάββατο το πρωί, στις έντεκα, αν σας βολεύει. Αλλιώς, την επόμενη εβδομάδα κάνουμε ένα μάθημα μιάμισης ώρας αντί για μίας.", "We can move it to Saturday morning at eleven, if that suits you. Otherwise, next week we'll do a lesson of an hour and a half instead of one."),
  L("Δασκάλα", "f", "Και κάτι ακόμα: η Δάφνη έχει προχωρήσει πολύ και θα ήθελα να τη δηλώσω στις εξετάσεις του ωδείου τον Μάιο. Πείτε μου τι σκέφτεστε, γιατί οι δηλώσεις κλείνουν στο τέλος του μήνα.", "And one more thing: Dafni has made great progress and I'd like to enter her for the conservatory exams in May. Tell me what you think, because entries close at the end of the month."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να γίνει το μάθημα την Πέμπτη;", ["Η δασκάλα είναι άρρωστη", "Η δασκάλα πηγαίνει σε μια συναυλία μαθητών στη Λάρισα", "Το πιάνο χάλασε", "Η Δάφνη έχει εξετάσεις"], 1, "την Πέμπτη πρέπει να πάω σε μια συναυλία μαθητών στη Λάρισα"),
  Q("Ποια είναι η εναλλακτική αν δεν βολεύει το Σάββατο;", ["Ένα μάθημα μιάμισης ώρας την επόμενη εβδομάδα", "Ένα μάθημα μέσω διαδικτύου", "Δύο μαθήματα την Κυριακή", "Επιστροφή των χρημάτων"], 0, "την επόμενη εβδομάδα κάνουμε ένα μάθημα μιάμισης ώρας αντί για μίας"),
  Q("Τι θέλει να κάνει η δασκάλα τον Μάιο;", ["Να κάνει διακοπές", "Να οργανώσει μια συναυλία στο σπίτι της", "Να δηλώσει τη Δάφνη στις εξετάσεις του ωδείου", "Να αλλάξει ώρα στα μαθήματα"], 2, "θα ήθελα να τη δηλώσω στις εξετάσεις του ωδείου τον Μάιο"),
 ],
 "gloss": {"συναυλία": "συναυλία — concert", "μεταφέρουμε": "μεταφέρω — to move, reschedule", "βολεύει": "βολεύω — to suit", "μιάμισης": "μιάμιση — one and a half", "προχωρήσει": "προχωράω — to make progress", "δηλώσω": "δηλώνω — to enter, register", "ωδείου": "ωδείο — conservatory, music school", "δηλώσεις": "δήλωση — entry, registration"}
})

ITEMS.append({
 "id": "l153-ann-synavlia-vrochi", "title": "Η συναυλία καθυστερεί λόγω βροχής", "title_en": "The concert is delayed by rain", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση σε ένα υπαίθριο θέατρο λίγο πριν από μια συναυλία.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητό κοινό, εξαιτίας της βροχής η αποψινή συναυλία θα ξεκινήσει με καθυστέρηση περίπου σαράντα πέντε λεπτών. Οι τεχνικοί πρέπει να στεγνώσουν τη σκηνή και να ελέγξουν τα ηλεκτρικά καλώδια για λόγους ασφαλείας.", "Dear audience, because of the rain tonight's concert will start about forty-five minutes late. The technicians need to dry the stage and check the electric cables for safety reasons."),
  L("Εκφωνητής", "m", "Μέχρι τότε μπορείτε να περιμένετε στο σκεπαστό φουαγιέ, δίπλα στην είσοδο, όπου το κυλικείο θα προσφέρει δωρεάν ζεστό τσάι. Σας παρακαλούμε να κρατήσετε τα εισιτήριά σας, γιατί θα ελεγχθούν ξανά.", "Until then you can wait in the covered foyer next to the entrance, where the snack bar will offer free hot tea. Please keep your tickets, because they will be checked again."),
  L("Εκφωνητής", "m", "Αν η βροχή συνεχιστεί μετά τις δέκα, η συναυλία θα αναβληθεί για την Κυριακή και τα εισιτήρια θα ισχύουν κανονικά. Όσοι δεν μπορούν να έρθουν την Κυριακή θα πάρουν πίσω τα χρήματά τους.", "If the rain continues after ten, the concert will be postponed to Sunday and tickets will be valid as normal. Those who can't come on Sunday will get their money back."),
 ],
 "questions": [
  Q("Γιατί καθυστερεί η συναυλία;", ["Γιατί αργεί ο τραγουδιστής", "Γιατί πρέπει να στεγνώσει η σκηνή και να ελεγχθούν τα καλώδια", "Γιατί δεν έχει έρθει αρκετός κόσμος", "Γιατί κόπηκε το ρεύμα"], 1, "Οι τεχνικοί πρέπει να στεγνώσουν τη σκηνή και να ελέγξουν τα ηλεκτρικά καλώδια"),
  Q("Τι προσφέρει το κυλικείο;", ["Δωρεάν ζεστό τσάι", "Ομπρέλες", "Έκπτωση στα σάντουιτς", "Κουβέρτες"], 0, "το κυλικείο θα προσφέρει δωρεάν ζεστό τσάι"),
  Q("Τι θα γίνει αν η βροχή συνεχιστεί μετά τις δέκα;", ["Η συναυλία θα γίνει σε κλειστό χώρο", "Θα ακυρωθεί χωρίς επιστροφή χρημάτων", "Η συναυλία θα αναβληθεί για την Κυριακή", "Θα παίξει μόνο ένα τραγούδι"], 2, "η συναυλία θα αναβληθεί για την Κυριακή"),
 ],
 "gloss": {"καθυστέρηση": "καθυστέρηση — delay", "τεχνικοί": "τεχνικός — technician", "στεγνώσουν": "στεγνώνω — to dry", "καλώδια": "καλώδιο — cable", "σκεπαστό": "σκεπαστός — covered", "φουαγιέ": "φουαγιέ — foyer", "κυλικείο": "κυλικείο — snack bar", "αναβληθεί": "αναβάλλομαι — to be postponed", "ισχύουν": "ισχύω — to be valid"}
})

ITEMS.append({
 "id": "l153-dia-doro-neogennito", "title": "Ένα δώρο για το μωρό", "title_en": "A present for the baby", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλες να συζητούν τι δώρο θα πάρουν για το μωρό μιας φίλης τους.",
 "script": [
  L("Μαρίνα", "f", "Η Κατερίνα γέννησε την Τρίτη! Αγοράκι, τρία κιλά και διακόσια. Λέω να περάσουμε από το μαιευτήριο το Σάββατο. Τι λες να της πάρουμε;", "Katerina gave birth on Tuesday! A boy, three kilos two hundred. I'm thinking we drop by the maternity hospital on Saturday. What do you think we should get her?"),
  L("Σοφία", "f", "Ρούχα δεν θέλω, θα της έχουν πάρει όλοι. Και τα μωρά μεγαλώνουν τόσο γρήγορα, που τα φοράνε δυο φορές.", "I don't want clothes, everyone will have got her those. And babies grow so fast that they wear them twice."),
  L("Μαρίνα", "f", "Έχεις δίκιο. Μήπως ένα μάρσιπο; Η Κατερίνα περπατάει πολύ, θα της είναι χρήσιμο.", "You're right. Maybe a baby carrier? Katerina walks a lot, it would be useful to her."),
  L("Σοφία", "f", "Το σκέφτηκα, αλλά της το έχει ήδη χαρίσει η πεθερά της. Εγώ σκεφτόμουν κάτι για την ίδια: μια κάρτα για δέκα γεύματα από ένα εστιατόριο που κάνει παράδοση στο σπίτι. Τις πρώτες εβδομάδες δεν έχεις χρόνο ούτε να μαγειρέψεις.", "I thought of that, but her mother-in-law has already given her one. I was thinking of something for her: a voucher for ten meals from a restaurant that delivers. In the first weeks you don't even have time to cook."),
  L("Μαρίνα", "f", "Τέλεια ιδέα! Και για το μωρό ένα βιβλίο με υφασμάτινες σελίδες, για να έχει κάτι κι αυτό.", "Perfect idea! And for the baby a book with cloth pages, so it has something too."),
 ],
 "questions": [
  Q("Γιατί δεν θέλει η Σοφία να πάρουν ρούχα;", ["Γιατί είναι ακριβά", "Γιατί θα πάρουν όλοι και τα μωρά μεγαλώνουν γρήγορα", "Γιατί δεν ξέρουν το νούμερο", "Γιατί η Κατερίνα δεν τα θέλει"], 1, "Ρούχα δεν θέλω, θα της έχουν πάρει όλοι"),
  Q("Γιατί δεν παίρνουν μάρσιπο;", ["Γιατί της το έχει ήδη χαρίσει η πεθερά της", "Γιατί δεν είναι ασφαλές", "Γιατί η Κατερίνα δεν περπατάει", "Γιατί δεν βρήκαν στο μαγαζί"], 0, "της το έχει ήδη χαρίσει η πεθερά της"),
  Q("Τι αποφασίζουν τελικά;", ["Ένα καρότσι", "Ένα παιχνίδι για το μπάνιο", "Μια κάρτα για δέκα γεύματα με παράδοση και ένα υφασμάτινο βιβλίο", "Λουλούδια και σοκολάτες"], 2, "μια κάρτα για δέκα γεύματα από ένα εστιατόριο που κάνει παράδοση στο σπίτι"),
 ],
 "gloss": {"γέννησε": "γεννάω — to give birth", "μαιευτήριο": "μαιευτήριο — maternity hospital", "μάρσιπο": "μάρσιπος — baby carrier (sling)", "χρήσιμο": "χρήσιμος — useful", "πεθερά": "πεθερά — mother-in-law", "γεύματα": "γεύμα — meal", "παράδοση": "παράδοση — delivery", "υφασμάτινες": "υφασμάτινος — made of cloth"}
})

ITEMS.append({
 "id": "l153-int-nanourismata", "title": "Η συλλέκτρια των νανουρισμάτων", "title_en": "The lullaby collector", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή για την παραδοσιακή μουσική.",
 "script": [
  L("Δημοσιογράφος", "m", "Η Χαρά είναι μουσικολόγος και τα τελευταία έξι χρόνια γυρίζει τα χωριά της Ηπείρου και ηχογραφεί νανουρίσματα. Χαρά, πώς ξεκίνησε αυτή η ιστορία;", "Chara is a musicologist, and for the last six years she has been touring the villages of Epirus recording lullabies. Chara, how did this story begin?"),
  L("Χαρά", "f", "Όταν γεννήθηκε η κόρη μου, κατάλαβα ότι δεν θυμόμουν ούτε ένα νανούρισμα ολόκληρο. Ρώτησα τη γιαγιά μου, κι εκείνη μου τραγούδησε δέκα, όλα διαφορετικά από αυτά που ξέρουμε από τους δίσκους.", "When my daughter was born, I realised I couldn't remember a single whole lullaby. I asked my grandmother, and she sang me ten, all different from the ones we know from records."),
  L("Δημοσιογράφος", "m", "Τι σας κάνει εντύπωση στους στίχους;", "What strikes you in the lyrics?"),
  L("Χαρά", "f", "Πολλά νανουρίσματα δεν είναι καθόλου γλυκά. Οι μητέρες τραγουδούσαν για την ξενιτιά του άντρα τους, για τη φτώχεια, για την κούραση. Το μωρό δεν καταλάβαινε τα λόγια, κι έτσι το νανούρισμα ήταν η μόνη στιγμή που μπορούσαν να πουν τον πόνο τους φωναχτά.", "Many lullabies aren't sweet at all. Mothers sang about their husbands working abroad, about poverty, about tiredness. The baby didn't understand the words, so the lullaby was the only moment they could say their pain out loud."),
  L("Χαρά", "f", "Μέχρι σήμερα έχω ηχογραφήσει πάνω από τριακόσια. Τα ανεβάζω σε ένα ελεύθερο ψηφιακό αρχείο, μαζί με τους στίχους και το όνομα της γυναίκας που τα τραγούδησε, για να μη χαθούν.", "So far I have recorded more than three hundred. I upload them to a free digital archive, together with the lyrics and the name of the woman who sang them, so they won't be lost."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η Χαρά να μαζεύει νανουρίσματα;", ["Της το ζήτησε το πανεπιστήμιο", "Όταν γεννήθηκε η κόρη της, κατάλαβε ότι δεν θυμόταν κανένα ολόκληρο", "Βρήκε παλιούς δίσκους στη σοφίτα", "Άκουσε ένα στο ραδιόφωνο"], 1, "Όταν γεννήθηκε η κόρη μου, κατάλαβα ότι δεν θυμόμουν ούτε ένα νανούρισμα ολόκληρο"),
  Q("Γιατί πολλά νανουρίσματα δεν είναι γλυκά, σύμφωνα με τη Χαρά;", ["Γιατί ήταν η μόνη στιγμή που οι μητέρες μπορούσαν να πουν τον πόνο τους φωναχτά", "Γιατί τα έγραφαν άντρες", "Γιατί προορίζονταν για μεγάλα παιδιά", "Γιατί ήταν πολεμικά τραγούδια"], 0, "το νανούρισμα ήταν η μόνη στιγμή που μπορούσαν να πουν τον πόνο τους φωναχτά"),
  Q("Τι κάνει τις ηχογραφήσεις της;", ["Τις πουλάει σε δίσκους", "Τις κρατάει για την οικογένειά της", "Τις ανεβάζει σε ένα ελεύθερο ψηφιακό αρχείο με τους στίχους και το όνομα της τραγουδίστριας", "Τις δίνει σε ένα μουσείο"], 2, "Τα ανεβάζω σε ένα ελεύθερο ψηφιακό αρχείο"),
 ],
 "gloss": {"μουσικολόγος": "μουσικολόγος — musicologist", "ηχογραφεί": "ηχογραφώ — to record", "νανουρίσματα": "νανούρισμα — lullaby", "δίσκους": "δίσκος — record (music)", "στίχους": "στίχος — line of verse; στίχοι = lyrics", "ξενιτιά": "ξενιτιά — living/working abroad", "κούραση": "κούραση — tiredness", "φωναχτά": "φωναχτά — out loud", "αρχείο": "αρχείο — archive"}
})

ITEMS.append({
 "id": "l153-news-pezogefyra", "title": "Μια πεζογέφυρα ενώνει δύο γειτονιές", "title_en": "A footbridge joins two neighbourhoods", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων από τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνήτρια", "f", "Παραδόθηκε σήμερα στους πολίτες η νέα πεζογέφυρα πάνω από την εθνική οδό, που ενώνει τις δύο γειτονιές του δήμου. Μέχρι τώρα οι κάτοικοι έπρεπε να κάνουν έναν κύκλο δύο χιλιομέτρων ή να διασχίζουν επικίνδυνα τον δρόμο.", "The new footbridge over the national road, which joins the municipality's two neighbourhoods, was handed over to the public today. Until now residents had to make a two-kilometre detour or cross the road dangerously."),
  L("Εκφωνήτρια", "f", "Η γέφυρα έχει ράμπες με μικρή κλίση και δύο ανελκυστήρες, ώστε να μπορούν να τη χρησιμοποιούν άνθρωποι με αναπηρικό αμαξίδιο και γονείς με καρότσια. Έχει επίσης ξεχωριστή λωρίδα για ποδήλατα.", "The bridge has gently sloping ramps and two lifts, so that people in wheelchairs and parents with pushchairs can use it. It also has a separate lane for bicycles."),
  L("Εκφωνήτρια", "f", "Ο δήμαρχος ανακοίνωσε ότι τη νύχτα η γέφυρα θα φωτίζεται με λάμπες χαμηλής κατανάλωσης, που τροφοδοτούνται από φωτοβολταϊκά πάνελ στο στέγαστρό της. Το έργο κόστισε δύο εκατομμύρια ευρώ και χρηματοδοτήθηκε από ευρωπαϊκά κονδύλια.", "The mayor announced that at night the bridge will be lit by low-energy lamps powered by solar panels on its roof. The project cost two million euros and was funded by European money."),
 ],
 "questions": [
  Q("Τι έκαναν οι κάτοικοι πριν από τη γέφυρα;", ["Έπαιρναν λεωφορείο", "Έκαναν κύκλο δύο χιλιομέτρων ή διέσχιζαν επικίνδυνα τον δρόμο", "Χρησιμοποιούσαν ένα υπόγειο πέρασμα", "Πήγαιναν με βάρκα"], 1, "οι κάτοικοι έπρεπε να κάνουν έναν κύκλο δύο χιλιομέτρων ή να διασχίζουν επικίνδυνα τον δρόμο"),
  Q("Γιατί η γέφυρα έχει ράμπες και ανελκυστήρες;", ["Για να τη χρησιμοποιούν άνθρωποι με αναπηρικό αμαξίδιο και γονείς με καρότσια", "Για τα φορτηγά", "Για να είναι πιο όμορφη", "Για τους ποδηλάτες μόνο"], 0, "ώστε να μπορούν να τη χρησιμοποιούν άνθρωποι με αναπηρικό αμαξίδιο και γονείς με καρότσια"),
  Q("Από πού θα παίρνουν ρεύμα οι λάμπες;", ["Από το δίκτυο της πόλης", "Από μια γεννήτρια", "Από φωτοβολταϊκά πάνελ στο στέγαστρο της γέφυρας", "Από μπαταρίες που αλλάζουν κάθε μήνα"], 2, "τροφοδοτούνται από φωτοβολταϊκά πάνελ στο στέγαστρό της"),
 ],
 "gloss": {"πεζογέφυρα": "πεζογέφυρα — footbridge", "Παραδόθηκε": "παραδίδομαι — to be handed over", "εθνική οδό": "εθνική οδός — national road, motorway", "ράμπες": "ράμπα — ramp", "κλίση": "κλίση — slope", "ανελκυστήρες": "ανελκυστήρας — lift", "αναπηρικό αμαξίδιο": "αναπηρικό αμαξίδιο — wheelchair", "λωρίδα": "λωρίδα — lane", "κατανάλωσης": "κατανάλωση — consumption", "φωτοβολταϊκά": "φωτοβολταϊκός — solar (photovoltaic)", "κονδύλια": "κονδύλι — funds"}
})

ITEMS.append({
 "id": "l153-mono-dentro-genethlia", "title": "Ένα δέντρο για κάθε χρόνο", "title_en": "A tree for every year", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλάει σε μια εκπομπή για τις μικρές συνήθειες που αλλάζουν τη ζωή.",
 "script": [
  L("Θοδωρής", "m", "Από τα τριάντα μου, κάθε χρόνο στα γενέθλιά μου φυτεύω ένα δέντρο. Την ιδέα την πήρα από τον παππού μου, που φύτευε μια ελιά για κάθε εγγόνι που γεννιόταν.", "Since I turned thirty, every year on my birthday I plant a tree. I got the idea from my grandfather, who planted an olive tree for every grandchild that was born."),
  L("Θοδωρής", "m", "Τα πρώτα τα φύτεψα στο χωράφι της οικογένειας. Μετά ζήτησα άδεια από τον δήμο και φύτευα σε ένα γυμνό πάρκο κοντά στο σπίτι μου. Τώρα μου κάνουν παρέα και φίλοι, και κάθε φορά καταλήγουμε σε ένα μικρό πικνίκ.", "I planted the first ones in the family field. Then I asked the municipality for permission and planted in a bare park near my home. Now friends keep me company, and every time we end up with a little picnic."),
  L("Θοδωρής", "m", "Δεν πιάνουν όλα. Δύο ξεράθηκαν σε ένα πολύ ζεστό καλοκαίρι, και έμαθα με τον δύσκολο τρόπο ότι πρέπει να διαλέγω είδη που αντέχουν στην ξηρασία. Όταν όμως περνάω από το πάρκο και βλέπω τη σκιά από τις πρώτες μου μουριές, νιώθω ότι τα χρόνια μου δεν πέρασαν άδικα.", "Not all of them take. Two dried up in a very hot summer, and I learned the hard way that I need to choose species that withstand drought. But when I walk through the park and see the shade from my first mulberry trees, I feel my years haven't passed in vain."),
 ],
 "questions": [
  Q("Από πού πήρε την ιδέα ο Θοδωρής;", ["Από ένα βιβλίο", "Από τον παππού του, που φύτευε μια ελιά για κάθε εγγόνι", "Από μια περιβαλλοντική οργάνωση", "Από τον δήμο"], 1, "Την ιδέα την πήρα από τον παππού μου, που φύτευε μια ελιά για κάθε εγγόνι"),
  Q("Πού φυτεύει τώρα τα δέντρα;", ["Στον κήπο του", "Σε ένα δάσος έξω από την πόλη", "Σε ένα γυμνό πάρκο κοντά στο σπίτι του, με άδεια του δήμου", "Στην αυλή ενός σχολείου"], 2, "ζήτησα άδεια από τον δήμο και φύτευα σε ένα γυμνό πάρκο κοντά στο σπίτι μου"),
  Q("Τι έμαθε όταν ξεράθηκαν δύο δέντρα;", ["Ότι πρέπει να διαλέγει είδη που αντέχουν στην ξηρασία", "Ότι πρέπει να φυτεύει τον χειμώνα", "Ότι οι μουριές δεν πιάνουν", "Ότι χρειάζεται λίπασμα"], 0, "πρέπει να διαλέγω είδη που αντέχουν στην ξηρασία"),
 ],
 "gloss": {"γενέθλιά": "γενέθλια — birthday", "φυτεύω": "φυτεύω — to plant", "χωράφι": "χωράφι — field", "γυμνό": "γυμνός — bare", "πιάνουν": "πιάνω (για φυτό) — to take root", "ξεράθηκαν": "ξεραίνομαι — to dry up", "είδη": "είδος — species, kind", "ξηρασία": "ξηρασία — drought", "μουριές": "μουριά — mulberry tree", "άδικα": "άδικα — in vain"}
})

ITEMS.append({
 "id": "l153-rep-scholeio-chwris-kinita", "title": "Ένας χρόνος χωρίς κινητά στο σχολείο", "title_en": "A year without mobiles at school", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για την εκπαίδευση.",
 "script": [
  L("Ρεπόρτερ", "m", "Από το σχολικό έτος 2024–2025, στα ελληνικά σχολεία οι μαθητές πρέπει να κρατούν το κινητό τους κλειστό μέσα στην τσάντα όσο βρίσκονται στο σχολείο. Επισκεφθήκαμε ένα γυμνάσιο της Πάτρας για να δούμε τι άλλαξε.", "Since the 2024–2025 school year, pupils in Greek schools have to keep their mobile switched off in their bag while they are at school. We visited a lower secondary school in Patras to see what has changed."),
  L("Ρεπόρτερ", "m", "Η διευθύντρια λέει ότι στα διαλείμματα τα παιδιά παίζουν ξανά μπάλα και επιτραπέζια, και ότι τα περιστατικά διαδικτυακού εκφοβισμού μέσα στο σχολείο έχουν μειωθεί. «Στην αρχή διαμαρτυρήθηκαν, τώρα δεν το συζητάνε καν», λέει.", "The head says that at break time the children play football and board games again, and that incidents of online bullying inside the school have decreased. \"At first they protested, now they don't even talk about it,\" she says."),
  L("Ρεπόρτερ", "m", "Δεν συμφωνούν όλοι. Κάποιοι γονείς ανησυχούν ότι δεν μπορούν να επικοινωνήσουν με τα παιδιά τους σε περίπτωση ανάγκης. Το σχολείο απαντά ότι το τηλέφωνο της γραμματείας είναι πάντα διαθέσιμο, και ότι κανένα παιδί δεν έχει μείνει χωρίς επικοινωνία.", "Not everyone agrees. Some parents worry that they can't contact their children in an emergency. The school replies that the office phone is always available, and that no child has been left without contact."),
 ],
 "questions": [
  Q("Τι ισχύει για τα κινητά στα σχολεία από το 2024–2025;", ["Επιτρέπονται μόνο στα διαλείμματα", "Πρέπει να μένουν κλειστά μέσα στην τσάντα", "Τα κρατούν οι καθηγητές", "Επιτρέπονται για μουσική"], 1, "οι μαθητές πρέπει να κρατούν το κινητό τους κλειστό μέσα στην τσάντα"),
  Q("Τι άλλαξε στα διαλείμματα, σύμφωνα με τη διευθύντρια;", ["Τα παιδιά παίζουν ξανά μπάλα και επιτραπέζια", "Τα παιδιά μένουν στις τάξεις", "Τα διαλείμματα έγιναν πιο σύντομα", "Τα παιδιά διαβάζουν περισσότερο"], 0, "στα διαλείμματα τα παιδιά παίζουν ξανά μπάλα και επιτραπέζια"),
  Q("Τι ανησυχεί κάποιους γονείς;", ["Ότι τα παιδιά θα χάσουν τα κινητά", "Ότι οι βαθμοί θα πέσουν", "Ότι δεν μπορούν να επικοινωνήσουν με τα παιδιά σε περίπτωση ανάγκης", "Ότι τα παιδιά θα βαρεθούν"], 2, "δεν μπορούν να επικοινωνήσουν με τα παιδιά τους σε περίπτωση ανάγκης"),
 ],
 "gloss": {"σχολικό έτος": "σχολικό έτος — school year", "διευθύντρια": "διευθύντρια — head teacher", "επιτραπέζια": "επιτραπέζιο (παιχνίδι) — board game", "περιστατικά": "περιστατικό — incident", "εκφοβισμού": "εκφοβισμός — bullying", "διαμαρτυρήθηκαν": "διαμαρτύρομαι — to protest", "ανάγκης": "σε περίπτωση ανάγκης — in an emergency", "γραμματείας": "γραμματεία — (school) office", "διαθέσιμο": "διαθέσιμος — available"}
})

ITEMS.append({
 "id": "l153-dia-thesi-parking", "title": "Ποιανού είναι η θέση στην πυλωτή;", "title_en": "Whose space is it under the building?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο γείτονες να συζητούν στην πυλωτή της πολυκατοικίας τους.",
 "script": [
  L("Κυρία Ρούλα", "f", "Κύριε Στέλιο, συγγνώμη, αλλά το αυτοκίνητό σας είναι πάλι στη δική μου θέση. Χθες το βράδυ γύρισα στις έντεκα και έψαχνα μισή ώρα να παρκάρω στον δρόμο.", "Mr Stelios, excuse me, but your car is in my space again. Last night I came back at eleven and spent half an hour looking for parking in the street."),
  L("Κύριος Στέλιος", "m", "Δεν είναι η θέση τρία; Εγώ νόμιζα ότι η τρία είναι του διαμερίσματός μου. Ο προηγούμενος ιδιοκτήτης μού είπε ότι πάρκαρε πάντα εκεί.", "Isn't it space three? I thought three belonged to my flat. The previous owner told me he always parked there."),
  L("Κυρία Ρούλα", "f", "Ο προηγούμενος ιδιοκτήτης παρκάριζε εκεί γιατί εγώ τότε δεν είχα αυτοκίνητο και του το επέτρεπα. Στο συμβόλαιο του δικού μου διαμερίσματος γράφει καθαρά τη θέση τρία.", "The previous owner parked there because I didn't have a car then and I let him. The contract for my flat clearly states space three."),
  L("Κύριος Στέλιος", "m", "Τότε έχετε δίκιο, και ζητώ συγγνώμη. Θα ρωτήσω τον διαχειριστή ποια θέση μού αναλογεί. Και για να μη γίνει πάλι παρεξήγηση, να βάλουμε αριθμούς στον τοίχο;", "Then you're right, and I apologise. I'll ask the building manager which space is mine. And so there's no misunderstanding again, shall we put numbers on the wall?"),
  L("Κυρία Ρούλα", "f", "Πολύ καλή ιδέα. Έχω και μπογιά από τότε που βάψαμε το μπαλκόνι.", "Very good idea. I even have paint from when we painted the balcony."),
 ],
 "questions": [
  Q("Τι πρόβλημα είχε η κυρία Ρούλα χθες το βράδυ;", ["Της έκλεψαν το αυτοκίνητο", "Έψαχνε μισή ώρα να παρκάρει στον δρόμο", "Δεν άνοιγε η γκαραζόπορτα", "Χάλασε το αυτοκίνητό της"], 1, "έψαχνα μισή ώρα να παρκάρω στον δρόμο"),
  Q("Γιατί ο προηγούμενος ιδιοκτήτης πάρκαρε στη θέση τρία;", ["Γιατί ήταν δική του", "Γιατί η κυρία Ρούλα δεν είχε τότε αυτοκίνητο και του το επέτρεπε", "Γιατί ήταν πιο κοντά στην είσοδο", "Γιατί το είπε ο διαχειριστής"], 1, "εγώ τότε δεν είχα αυτοκίνητο και του το επέτρεπα"),
  Q("Τι προτείνει ο κύριος Στέλιος για το μέλλον;", ["Να πουλήσει το αυτοκίνητο", "Να μοιράζονται τη θέση", "Να βάλουν αριθμούς στον τοίχο", "Να κλειδώνουν την πυλωτή"], 2, "να βάλουμε αριθμούς στον τοίχο"),
 ],
 "gloss": {"πυλωτή": "πυλωτή — open ground-floor parking under a building", "παρκάρω": "παρκάρω — to park", "διαμερίσματός": "διαμέρισμα — flat", "ιδιοκτήτης": "ιδιοκτήτης — owner", "επέτρεπα": "επιτρέπω — to allow", "συμβόλαιο": "συμβόλαιο — contract, deed", "διαχειριστή": "διαχειριστής — building manager", "αναλογεί": "αναλογώ — to be due to", "παρεξήγηση": "παρεξήγηση — misunderstanding", "μπογιά": "μπογιά — paint"}
})

ITEMS.append({
 "id": "l153-c1-psevdaisthisi-elegxou", "title": "Γιατί ρίχνουμε πιο δυνατά τα ζάρια", "title_en": "Why we throw the dice harder", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη ψυχολογίας για τις γνωστικές προκαταλήψεις.",
 "script": [
  L("Ομιλήτρια", "f", "Το 1975 η Αμερικανίδα ψυχολόγος Έλεν Λάνγκερ δημοσίευσε μια σειρά πειραμάτων με έναν εύγλωττο τίτλο: «Η ψευδαίσθηση του ελέγχου». Σε ένα από αυτά, οι συμμετέχοντες αγόραζαν λαχεία. Οι μισοί διάλεγαν μόνοι τους το λαχείο, στους άλλους μισούς το έδιναν οι ερευνητές.", "In 1975 the American psychologist Ellen Langer published a series of experiments under an eloquent title: \"The illusion of control\". In one of them, participants bought lottery tickets. Half chose their ticket themselves, the other half were handed one by the researchers."),
  L("Ομιλήτρια", "f", "Όταν αργότερα τους ζήτησαν να πουλήσουν το λαχείο τους, όσοι το είχαν διαλέξει μόνοι τους ζητούσαν κατά μέσο όρο πολύ περισσότερα χρήματα. Η πιθανότητα να κερδίσουν ήταν ακριβώς η ίδια. Η επιλογή όμως τους έδινε την αίσθηση ότι είχαν κάποιον έλεγχο στο αποτέλεσμα.", "When they were later asked to sell their ticket, those who had chosen it themselves asked on average for much more money. The chance of winning was exactly the same. But choosing gave them the feeling that they had some control over the outcome."),
  L("Ομιλήτρια", "f", "Παρόμοιες παρατηρήσεις υπάρχουν και από τα καζίνα: παίκτες που θέλουν μεγάλο αριθμό ρίχνουν συχνά τα ζάρια πιο δυνατά, ενώ για μικρό αριθμό τα ρίχνουν απαλά. Ο νους μας δυσκολεύεται να δεχτεί ότι κάποια πράγματα είναι απλώς τυχαία.", "Similar observations exist from casinos: players who want a high number often throw the dice harder, while for a low number they throw them gently. Our mind finds it hard to accept that some things are simply random."),
  L("Ομιλήτρια", "f", "Η ψευδαίσθηση αυτή δεν είναι πάντα κακή. Μας δίνει κίνητρο να προσπαθούμε. Γίνεται επικίνδυνη όταν μας κάνει να υποτιμούμε τον ρόλο της τύχης, για παράδειγμα στις επενδύσεις ή στα τυχερά παιχνίδια.", "This illusion isn't always bad. It gives us motivation to keep trying. It becomes dangerous when it makes us underestimate the role of luck, for example in investments or in gambling."),
 ],
 "questions": [
  Q("Τι έκαναν οι συμμετέχοντες στο πείραμα της Λάνγκερ;", ["Έπαιζαν ζάρια", "Αγόραζαν λαχεία, που άλλοι τα διάλεγαν μόνοι τους και άλλοι τα έπαιρναν από τους ερευνητές", "Πουλούσαν μετοχές", "Μάντευαν αριθμούς"], 1, "οι συμμετέχοντες αγόραζαν λαχεία"),
  Q("Τι ζητούσαν όσοι είχαν διαλέξει μόνοι τους το λαχείο;", ["Λιγότερα χρήματα", "Ένα δεύτερο λαχείο", "Πολύ περισσότερα χρήματα για να το πουλήσουν", "Να τους το αλλάξουν"], 2, "ζητούσαν κατά μέσο όρο πολύ περισσότερα χρήματα"),
  Q("Τι κάνουν συχνά οι παίκτες στα καζίνα;", ["Ρίχνουν τα ζάρια πιο δυνατά όταν θέλουν μεγάλο αριθμό", "Κλείνουν τα μάτια", "Αλλάζουν τραπέζι", "Ρίχνουν πάντα με το αριστερό χέρι"], 0, "παίκτες που θέλουν μεγάλο αριθμό ρίχνουν συχνά τα ζάρια πιο δυνατά"),
  Q("Πότε γίνεται επικίνδυνη η ψευδαίσθηση του ελέγχου;", ["Όταν μας δίνει κίνητρο", "Όταν παίζουμε με φίλους", "Όταν είμαστε κουρασμένοι", "Όταν μας κάνει να υποτιμούμε τον ρόλο της τύχης"], 3, "Γίνεται επικίνδυνη όταν μας κάνει να υποτιμούμε τον ρόλο της τύχης"),
 ],
 "gloss": {"εύγλωττο": "εύγλωττος — eloquent, telling", "ψευδαίσθηση": "ψευδαίσθηση — illusion", "συμμετέχοντες": "συμμετέχων — participant", "λαχεία": "λαχείο — lottery ticket", "πιθανότητα": "πιθανότητα — probability, chance", "καζίνα": "καζίνο — casino", "ζάρια": "ζάρι — die (dice)", "απαλά": "απαλά — gently", "τυχαία": "τυχαίος — random", "κίνητρο": "κίνητρο — motivation", "υποτιμούμε": "υποτιμώ — to underestimate", "τυχερά παιχνίδια": "τυχερά παιχνίδια — gambling"}
})

ITEMS.append({
 "id": "l153-c1-nomos-veber", "title": "Πόσο πρέπει να αλλάξει κάτι για να το προσέξουμε;", "title_en": "How much must something change for us to notice?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από συνέντευξη ενός νευροεπιστήμονα σε μια εκπομπή για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "f", "Μας είπατε ότι ένας νόμος του 19ου αιώνα εξηγεί γιατί δεν καταλαβαίνουμε τις μικρές ανατιμήσεις. Ποιος είναι αυτός ο νόμος;", "You told us that a 19th-century law explains why we don't notice small price rises. What is this law?"),
  L("Νευροεπιστήμονας", "m", "Είναι ο λεγόμενος νόμος του Βέμπερ, από τον Γερμανό φυσιολόγο Ερνστ Χάινριχ Βέμπερ. Ο Βέμπερ έβαζε τους εθελοντές του να κρατούν βάρη και μετρούσε πόσο έπρεπε να αυξηθεί ένα βάρος για να καταλάβουν τη διαφορά. Διαπίστωσε ότι αυτό που μετράει δεν είναι η απόλυτη αλλαγή, αλλά η αναλογία.", "It's the so-called Weber's law, after the German physiologist Ernst Heinrich Weber. Weber had his volunteers hold weights and measured how much a weight had to increase for them to notice the difference. He found that what matters is not the absolute change but the proportion."),
  L("Νευροεπιστήμονας", "m", "Αν κρατάτε ένα γράμμα και σας προσθέσω δέκα γραμμάρια, θα το νιώσετε αμέσως. Αν κρατάτε μια βαλίτσα είκοσι κιλών, δέκα γραμμάρια δεν θα τα καταλάβετε ποτέ. Το ίδιο ισχύει, σε γενικές γραμμές, για το φως, τον ήχο, ακόμα και για τις τιμές.", "If you're holding a letter and I add ten grams, you'll feel it immediately. If you're holding a twenty-kilo suitcase, you'll never notice ten grams. The same broadly holds for light, for sound, even for prices."),
  L("Νευροεπιστήμονας", "m", "Γι' αυτό μια αύξηση πέντε λεπτών στον καφέ μάς ενοχλεί, ενώ η ίδια αύξηση στην τιμή ενός αυτοκινήτου περνάει απαρατήρητη. Πρέπει να πω όμως ότι ο νόμος είναι μια προσέγγιση: στις πολύ ασθενείς και στις πολύ ισχυρές εντάσεις δεν λειτουργεί τόσο καλά.", "That's why a five-cent rise in the price of coffee annoys us, while the same rise in the price of a car goes unnoticed. I must say, though, that the law is an approximation: at very weak and very strong intensities it doesn't work so well."),
 ],
 "questions": [
  Q("Τι έκανε ο Βέμπερ στα πειράματά του;", ["Μετρούσε πόσο έπρεπε να αυξηθεί ένα βάρος για να καταλάβουν οι εθελοντές τη διαφορά", "Μελετούσε τις τιμές στην αγορά", "Μετρούσε την ακοή των ζώων", "Ζύγιζε βαλίτσες στο αεροδρόμιο"], 0, "μετρούσε πόσο έπρεπε να αυξηθεί ένα βάρος για να καταλάβουν τη διαφορά"),
  Q("Τι μετράει, σύμφωνα με τον νόμο του Βέμπερ;", ["Η απόλυτη αλλαγή", "Η αναλογία της αλλαγής", "Η ταχύτητα της αλλαγής", "Η ηλικία του ανθρώπου"], 1, "αυτό που μετράει δεν είναι η απόλυτη αλλαγή, αλλά η αναλογία"),
  Q("Γιατί δεν καταλαβαίνουμε δέκα γραμμάρια σε μια βαλίτσα είκοσι κιλών;", ["Γιατί τα χέρια μας κουράζονται", "Γιατί η βαλίτσα είναι άδεια", "Γιατί η αλλαγή είναι πολύ μικρή σε σχέση με το συνολικό βάρος", "Γιατί δεν προσέχουμε"], 2, "δέκα γραμμάρια δεν θα τα καταλάβετε ποτέ"),
  Q("Ποια επιφύλαξη διατυπώνει ο επιστήμονας;", ["Ότι ο νόμος δεν ισχύει για τις τιμές", "Ότι τα πειράματα δεν επαναλήφθηκαν", "Ότι ο Βέμπερ έκανε λάθος στους υπολογισμούς", "Ότι ο νόμος είναι μια προσέγγιση που δεν λειτουργεί καλά στις πολύ ασθενείς και πολύ ισχυρές εντάσεις"], 3, "ο νόμος είναι μια προσέγγιση"),
 ],
 "gloss": {"ανατιμήσεις": "ανατίμηση — price rise", "λεγόμενος": "λεγόμενος — so-called", "φυσιολόγο": "φυσιολόγος — physiologist", "βάρη": "βάρος — weight", "απόλυτη": "απόλυτος — absolute", "αναλογία": "αναλογία — proportion, ratio", "γραμμάρια": "γραμμάριο — gram", "απαρατήρητη": "απαρατήρητος — unnoticed", "προσέγγιση": "προσέγγιση — approximation", "ασθενείς": "ασθενής — weak", "εντάσεις": "ένταση — intensity"}
})

rnd = random.Random(153)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-153.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
