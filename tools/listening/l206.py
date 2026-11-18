# Source for library/listening/listening-206.json: five more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l206.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l206-news-challoumi", "title": "Το χαλλούμι αποκτά προστατευμένη ονομασία", "title_en": "Halloumi gets a protected name", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων σε έναν κυπριακό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Μετά από χρόνια διαπραγματεύσεων, το χαλλούμι καταχωρίστηκε επίσημα στην Ευρωπαϊκή Ένωση ως προϊόν προστατευόμενης ονομασίας προέλευσης. Αυτό σημαίνει ότι μόνο το τυρί που παράγεται στην Κύπρο, με συγκεκριμένη συνταγή, μπορεί να πωλείται με αυτό το όνομα.", "After years of negotiations, halloumi has been officially registered in the European Union as a product with a protected designation of origin. This means that only cheese produced in Cyprus, to a specific recipe, may be sold under this name."),
  L("Εκφωνήτρια", "f", "Το μεγαλύτερο πρόβλημα των συζητήσεων ήταν το γάλα. Παραδοσιακά το χαλλούμι φτιαχνόταν από πρόβειο και κατσικίσιο γάλα, σήμερα όμως οι περισσότερες μεγάλες μονάδες χρησιμοποιούν και αγελαδινό. Οι κτηνοτρόφοι ζητούσαν μεγαλύτερο ποσοστό αιγοπρόβειου γάλακτος, ενώ οι βιομηχανίες φοβούνταν ότι δεν θα υπήρχε αρκετό για τη ζήτηση.", "The biggest problem in the talks was the milk. Traditionally halloumi was made from sheep's and goat's milk, but today most large plants also use cow's milk. Livestock farmers wanted a higher share of sheep and goat milk, while the industry feared there would not be enough for demand."),
  L("Εκφωνήτρια", "f", "Το χαλλούμι είναι σήμερα ένα από τα σημαντικότερα εξαγώγιμα προϊόντα της Κύπρου. Η ιδιαιτερότητά του είναι ότι δεν λιώνει εύκολα, γι' αυτό ψήνεται στη σχάρα ή στο τηγάνι και τρώγεται ζεστό, συχνά με καρπούζι το καλοκαίρι.", "Halloumi is today one of Cyprus's most important export products. Its special feature is that it does not melt easily, which is why it is grilled or fried and eaten hot, often with watermelon in summer."),
 ],
 "questions": [
  Q("Τι σημαίνει η νέα καταχώριση για το χαλλούμι;", ["Ότι θα πωλείται φθηνότερα", "Ότι μόνο το τυρί που παράγεται στην Κύπρο με συγκεκριμένη συνταγή μπορεί να έχει αυτό το όνομα", "Ότι απαγορεύεται η εξαγωγή του", "Ότι θα φτιάχνεται μόνο από αγελαδινό γάλα"], 1, "μόνο το τυρί που παράγεται στην Κύπρο, με συγκεκριμένη συνταγή"),
  Q("Ποιο ήταν το μεγαλύτερο πρόβλημα των διαπραγματεύσεων;", ["Η τιμή", "Η συσκευασία", "Το γάλα", "Η ονομασία στα αγγλικά"], 2, "Το μεγαλύτερο πρόβλημα των συζητήσεων ήταν το γάλα"),
  Q("Τι ζητούσαν οι κτηνοτρόφοι;", ["Μεγαλύτερο ποσοστό αιγοπρόβειου γάλακτος", "Μόνο αγελαδινό γάλα", "Επιδοτήσεις για αγελάδες", "Κατάργηση της συνταγής"], 0, "Οι κτηνοτρόφοι ζητούσαν μεγαλύτερο ποσοστό αιγοπρόβειου γάλακτος"),
  Q("Γιατί το χαλλούμι ψήνεται στη σχάρα;", ["Γιατί είναι πολύ αλμυρό", "Γιατί δεν λιώνει εύκολα", "Γιατί έτσι διατηρείται περισσότερο", "Γιατί είναι ωμό"], 1, "δεν λιώνει εύκολα, γι' αυτό ψήνεται στη σχάρα"),
 ],
 "gloss": {"διαπραγματεύσεων": "διαπραγμάτευση — negotiation", "καταχωρίστηκε": "καταχωρίζω — to register", "προστατευόμενης ονομασίας προέλευσης": "προστατευόμενη ονομασία προέλευσης — protected designation of origin (PDO)", "πρόβειο": "πρόβειος — sheep's", "κατσικίσιο": "κατσικίσιος — goat's", "αγελαδινό": "αγελαδινός — cow's", "αιγοπρόβειου": "αιγοπρόβειος — sheep-and-goat", "εξαγώγιμα": "εξαγώγιμος — exportable, for export"},
})
ITEMS.append({
 "id": "l206-dia-taxidi-kypro", "title": "Μια εβδομάδα στην Κύπρο", "title_en": "A week in Cyprus", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φίλοι σχεδιάζουν ένα ταξίδι στην Κύπρο τον Οκτώβριο.",
 "script": [
  L("Μάρκος", "m", "Λοιπόν, έχουμε επτά μέρες. Εγώ λέω να μείνουμε όλη την εβδομάδα στην Πάφο: θάλασσα, ψηφιδωτά, ηλιοβασιλέματα.", "Right, we've got seven days. I say we stay the whole week in Paphos: sea, mosaics, sunsets."),
  L("Σοφία", "f", "Και να μη δούμε τίποτα άλλο; Θέλω οπωσδήποτε να ανέβουμε στο Τρόοδος, να δούμε τις ζωγραφισμένες εκκλησίες στα χωριά. Είναι μνημεία της UNESCO, και τον Οκτώβριο ο καιρός στο βουνό είναι ιδανικός.", "And see nothing else? I definitely want to go up to Troodos and see the painted churches in the villages. They're UNESCO monuments, and in October the weather in the mountains is ideal."),
  L("Μάρκος", "m", "Εντάξει, αλλά οι δρόμοι εκεί πάνω έχουν πολλές στροφές, και θα οδηγούμε στα αριστερά. Δεν το έχω ξανακάνει.", "OK, but the roads up there have lots of bends, and we'll be driving on the left. I've never done it before."),
  L("Σοφία", "f", "Θα οδηγώ εγώ στο βουνό. Προτείνω τέσσερις μέρες στην Πάφο και τρεις στο Τρόοδος, με μια στάση στη Λευκωσία στον γυρισμό. Θέλω να περπατήσω στην παλιά πόλη, μέσα στα ενετικά τείχη.", "I'll drive in the mountains. I suggest four days in Paphos and three in Troodos, with a stop in Nicosia on the way back. I want to walk in the old town, inside the Venetian walls."),
  L("Μάρκος", "m", "Σύμφωνοι. Αλλά την τελευταία βραδιά τη θέλω σε ταβέρνα με μεζέ. Μου είπαν ότι φέρνουν πάνω από είκοσι πιάτα και στο τέλος δεν μπορείς να σηκωθείς.", "Agreed. But I want the last evening in a tavern with meze. I've been told they bring more than twenty dishes and at the end you can't get up."),
 ],
 "questions": [
  Q("Τι πρότεινε αρχικά ο Μάρκος;", ["Να μείνουν όλη την εβδομάδα στην Πάφο", "Να μείνουν στη Λευκωσία", "Να πάνε μόνο στο Τρόοδος", "Να αλλάζουν πόλη κάθε μέρα"], 0, "να μείνουμε όλη την εβδομάδα στην Πάφο"),
  Q("Γιατί θέλει η Σοφία να πάνε στο Τρόοδος;", ["Για να κάνουν σκι", "Για να δουν τις ζωγραφισμένες εκκλησίες στα χωριά", "Για να επισκεφθούν συγγενείς", "Για να κολυμπήσουν σε λίμνες"], 1, "να δούμε τις ζωγραφισμένες εκκλησίες στα χωριά"),
  Q("Τι ανησυχεί τον Μάρκο για την οδήγηση;", ["Η κίνηση στην πόλη", "Οι στροφές και ότι θα οδηγούν στα αριστερά", "Η τιμή της βενζίνης", "Ότι δεν έχει δίπλωμα"], 1, "οι δρόμοι εκεί πάνω έχουν πολλές στροφές, και θα οδηγούμε στα αριστερά"),
  Q("Τι θέλει να κάνει η Σοφία στη Λευκωσία;", ["Να ψωνίσει", "Να επισκεφθεί ένα μουσείο", "Να περπατήσει στην παλιά πόλη μέσα στα ενετικά τείχη", "Να δει έναν φίλο"], 2, "Θέλω να περπατήσω στην παλιά πόλη, μέσα στα ενετικά τείχη"),
 ],
 "gloss": {"ψηφιδωτά": "ψηφιδωτό — mosaic", "ηλιοβασιλέματα": "ηλιοβασίλεμα — sunset", "οπωσδήποτε": "οπωσδήποτε — definitely, by all means", "ζωγραφισμένες": "ζωγραφισμένος — painted", "στροφές": "στροφή — bend, turn", "ενετικά": "ενετικός — Venetian", "τείχη": "τείχος — (city) wall", "μεζέ": "μεζές — meze, small dishes"},
})
ITEMS.append({
 "id": "l206-rep-odos-lidras", "title": "Η οδός Λήδρας στη Λευκωσία", "title_en": "Ledra Street in Nicosia", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια ταξιδιωτική εκπομπή για τη Λευκωσία.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρίσκομαι στην οδό Λήδρας, τον πιο γνωστό πεζόδρομο της παλιάς Λευκωσίας. Δεξιά κι αριστερά υπάρχουν καφετέριες, βιβλιοπωλεία και μαγαζιά με ρούχα, όπως σε κάθε εμπορικό δρόμο. Στο τέλος του δρόμου όμως υπάρχει κάτι που δεν θα βρείτε σε άλλη ευρωπαϊκή πρωτεύουσα: ένα σημείο ελέγχου.", "I'm in Ledra Street, the best-known pedestrian street in old Nicosia. On the right and left there are cafés, bookshops and clothes shops, as in any shopping street. At the end of the street, though, there is something you won't find in any other European capital: a checkpoint."),
  L("Ρεπόρτερ", "f", "Από το 1974 η πόλη είναι χωρισμένη στα δύο από τη λεγόμενη Πράσινη Γραμμή, μια νεκρή ζώνη που ελέγχουν τα Ηνωμένα Έθνη. Για πολλά χρόνια ο δρόμος κατέληγε σε έναν τοίχο με σακιά άμμου. Το 2008 άνοιξε εδώ ένα πέρασμα για πεζούς, και σήμερα κάθε μέρα εκατοντάδες άνθρωποι περνούν από τη μία πλευρά στην άλλη, δείχνοντας την ταυτότητα ή το διαβατήριό τους.", "Since 1974 the city has been divided in two by the so-called Green Line, a buffer zone controlled by the United Nations. For many years the street ended in a wall of sandbags. In 2008 a pedestrian crossing opened here, and today hundreds of people cross every day from one side to the other, showing their identity card or passport."),
  L("Ρεπόρτερ", "f", "Ένας ηλικιωμένος καταστηματάρχης μού λέει ότι θυμάται τον δρόμο ενιαίο, πριν από το 1974. «Τότε ψωνίζαμε όλοι στα ίδια μαγαζιά», λέει. Για τους νεότερους, το πέρασμα είναι πια κομμάτι της καθημερινότητας· για τους μεγαλύτερους, κάθε φορά που το διασχίζουν, ξυπνούν αναμνήσεις.", "An elderly shopkeeper tells me he remembers the street as one, before 1974. 'Back then we all shopped in the same shops,' he says. For younger people the crossing is now part of everyday life; for older people, every time they cross it, memories are awakened."),
 ],
 "questions": [
  Q("Τι υπάρχει στο τέλος της οδού Λήδρας;", ["Ένα μουσείο", "Ένα σημείο ελέγχου", "Μια εκκλησία", "Ένας σταθμός λεωφορείων"], 1, "Στο τέλος του δρόμου όμως υπάρχει ... ένα σημείο ελέγχου"),
  Q("Ποιος ελέγχει τη νεκρή ζώνη;", ["Η αστυνομία της πόλης", "Τα Ηνωμένα Έθνη", "Ο δήμος", "Η Ευρωπαϊκή Ένωση"], 1, "μια νεκρή ζώνη που ελέγχουν τα Ηνωμένα Έθνη"),
  Q("Τι άλλαξε το 2008;", ["Γκρεμίστηκε όλη η Πράσινη Γραμμή", "Άνοιξε ένα πέρασμα για πεζούς", "Ο δρόμος έγινε πεζόδρομος", "Κατασκευάστηκε ένας τοίχος"], 1, "Το 2008 άνοιξε εδώ ένα πέρασμα για πεζούς"),
  Q("Τι σημαίνει το πέρασμα για τους μεγαλύτερους, σύμφωνα με τη ρεπόρτερ;", ["Είναι απλώς ένας δρόμος για ψώνια", "Τους ξυπνά αναμνήσεις κάθε φορά που το διασχίζουν", "Δεν το χρησιμοποιούν ποτέ", "Τους ενοχλεί ο θόρυβος"], 1, "κάθε φορά που το διασχίζουν, ξυπνούν αναμνήσεις"),
 ],
 "gloss": {"πεζόδρομο": "πεζόδρομος — pedestrian street", "σημείο ελέγχου": "σημείο ελέγχου — checkpoint", "νεκρή ζώνη": "νεκρή ζώνη — buffer zone", "σακιά άμμου": "σακί άμμου — sandbag", "πέρασμα": "πέρασμα — crossing (point)", "ταυτότητα": "ταυτότητα — identity card", "καταστηματάρχης": "καταστηματάρχης — shopkeeper", "ενιαίο": "ενιαίος — single, undivided"},
})
ITEMS.append({
 "id": "l206-c1-int-psifidota-pafou", "title": "Ένα χωράφι πάνω από τα ψηφιδωτά της Πάφου", "title_en": "A field above the mosaics of Paphos", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με μια αρχαιολόγο σε μια εκπομπή για τα μνημεία της Κύπρου.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς ανακαλύφθηκαν τα περίφημα ψηφιδωτά της Πάφου;", "How were the famous mosaics of Paphos discovered?"),
  L("Αρχαιολόγος", "f", "Με τον πιο απλό τρόπο: το 1962 ένας αγρότης όργωνε το χωράφι του και το αλέτρι του χτύπησε σε κάτι σκληρό. Ήταν ένα κομμάτι ψηφιδωτού δαπέδου. Οι ανασκαφές που ακολούθησαν έφεραν στο φως μια μεγάλη ρωμαϊκή έπαυλη, που ονομάστηκε Οικία του Διονύσου, από τις παραστάσεις με τον θεό του κρασιού. Αργότερα βρέθηκαν και άλλες επαύλεις, όπως η Οικία του Θησέα και η Οικία του Αιώνα.", "In the simplest way: in 1962 a farmer was ploughing his field and his plough hit something hard. It was a piece of mosaic floor. The excavations that followed brought to light a large Roman villa, which was named the House of Dionysus, after the scenes with the god of wine. Later other villas were found, such as the House of Theseus and the House of Aion."),
  L("Δημοσιογράφος", "m", "Τι κάνει αυτά τα ψηφιδωτά τόσο σημαντικά;", "What makes these mosaics so important?"),
  L("Αρχαιολόγος", "f", "Πρώτα η ποιότητα: οι τεχνίτες χρησιμοποιούσαν μικροσκοπικές ψηφίδες σε δεκάδες αποχρώσεις, ώστε να αποδίδουν σκιές και όγκους σχεδόν σαν ζωγραφική. Έπειτα η χρονολογική τους έκταση, από τον 2ο μέχρι τον 5ο περίπου αιώνα μ.Χ., που μας επιτρέπει να δούμε πώς οι παγανιστικοί μύθοι συνυπάρχουν σιγά σιγά με χριστιανικά θέματα. Η περιοχή έχει ενταχθεί στον κατάλογο της UNESCO από το 1980.", "First the quality: the craftsmen used tiny tesserae in dozens of shades, so as to render shadows and volumes almost like painting. Then their chronological range, from roughly the 2nd to the 5th century AD, which lets us see how pagan myths gradually coexist with Christian themes. The area has been on the UNESCO list since 1980."),
  L("Δημοσιογράφος", "m", "Και ο μεγαλύτερος κίνδυνος σήμερα;", "And the greatest danger today?"),
  L("Αρχαιολόγος", "f", "Η επιτυχία τους. Χιλιάδες επισκέπτες περπατούν κάθε μέρα δίπλα τους, ο ήλιος και η αλμύρα τα φθείρουν, και τα στέγαστρα δεν αρκούν πάντα. Η προστασία ενός μνημείου που όλοι θέλουν να δουν είναι πάντα ένας λεπτός συμβιβασμός.", "Their success. Thousands of visitors walk beside them every day, the sun and the salt wear them down, and the shelters are not always enough. Protecting a monument that everyone wants to see is always a delicate compromise."),
 ],
 "questions": [
  Q("Πώς ανακαλύφθηκαν τα ψηφιδωτά;", ["Σε ανασκαφή ενός πανεπιστημίου", "Ένας αγρότης χτύπησε κάτι σκληρό με το αλέτρι του", "Μετά από έναν σεισμό", "Κατά την κατασκευή ενός ξενοδοχείου"], 1, "ένας αγρότης όργωνε το χωράφι του και το αλέτρι του χτύπησε σε κάτι σκληρό"),
  Q("Γιατί η πρώτη έπαυλη ονομάστηκε Οικία του Διονύσου;", ["Από το όνομα του αγρότη", "Από τις παραστάσεις με τον θεό του κρασιού", "Γιατί βρέθηκαν εκεί αμφορείς κρασιού", "Από το όνομα του ιδιοκτήτη της"], 1, "από τις παραστάσεις με τον θεό του κρασιού"),
  Q("Τι επιτρέπει η χρονολογική έκταση των ψηφιδωτών;", ["Να χρονολογηθούν άλλες αρχαιότητες", "Να δούμε πώς οι παγανιστικοί μύθοι συνυπάρχουν σιγά σιγά με χριστιανικά θέματα", "Να μάθουμε τα ονόματα των τεχνιτών", "Να συγκρίνουμε την Κύπρο με την Αίγυπτο"], 1, "οι παγανιστικοί μύθοι συνυπάρχουν σιγά σιγά με χριστιανικά θέματα"),
  Q("Ποιος είναι ο μεγαλύτερος κίνδυνος για τα ψηφιδωτά, σύμφωνα με την αρχαιολόγο;", ["Οι κλοπές", "Οι σεισμοί", "Η επιτυχία τους: οι πολλοί επισκέπτες, ο ήλιος και η αλμύρα", "Η έλλειψη χρημάτων για ανασκαφές"], 2, "Η επιτυχία τους"),
 ],
 "gloss": {"όργωνε": "οργώνω — to plough", "αλέτρι": "αλέτρι — plough", "ανασκαφές": "ανασκαφή — excavation", "έπαυλη": "έπαυλη — villa", "ψηφίδες": "ψηφίδα — tessera (mosaic piece)", "αποχρώσεις": "απόχρωση — shade, hue", "παγανιστικοί": "παγανιστικός — pagan", "αλμύρα": "αλμύρα — saltiness, sea salt", "στέγαστρα": "στέγαστρο — shelter, canopy", "συμβιβασμός": "συμβιβασμός — compromise"},
})
ITEMS.append({
 "id": "l206-c1-mono-kypriaki-dialektos", "title": "«Έν πολλά ωραίο»: λίγα λόγια για την κυπριακή διάλεκτο", "title_en": "A few words about the Cypriot dialect", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια γλωσσολόγο σε μια ραδιοφωνική εκπομπή για τις διαλέκτους της ελληνικής.",
 "script": [
  L("Γλωσσολόγος", "f", "Όποιος Ελλαδίτης πρωτοακούει Κύπριους να μιλούν μεταξύ τους συχνά δυσκολεύεται να τους καταλάβει, παρόλο που μιλούν ελληνικά. Η κυπριακή είναι η πιο ζωντανή ελληνική διάλεκτος σήμερα: δεν τη μιλούν μόνο οι ηλικιωμένοι στα χωριά, αλλά και οι νέοι στις πόλεις, στο σπίτι, στην παρέα, ακόμα και στα μέσα κοινωνικής δικτύωσης.", "Any Greek from Greece who hears Cypriots talking among themselves for the first time often struggles to understand them, even though they speak Greek. Cypriot is the most alive Greek dialect today: it isn't spoken only by the elderly in villages but also by young people in the towns, at home, among friends, even on social media."),
  L("Γλωσσολόγος", "f", "Ας πάρουμε μερικά χαρακτηριστικά. Τα διπλά σύμφωνα προφέρονται πραγματικά διπλά: το «άλλος» ακούγεται με παρατεταμένο λάμδα. Το «και» γίνεται «τζαι», γιατί το κάππα πριν από ορισμένα φωνήεντα αλλάζει προφορά. Το «είναι» συχνά συντομεύεται σε «έν», και το «πολλά» χρησιμοποιείται με τη σημασία του «πολύ». Έτσι, «έν πολλά ωραίο» σημαίνει απλώς «είναι πολύ ωραίο».", "Let's take a few features. Double consonants are really pronounced double: «άλλος» is heard with a lengthened lambda. «Και» becomes «τζαι», because kappa changes its pronunciation before certain vowels. «Είναι» is often shortened to «έν», and «πολλά» is used to mean «very». So «έν πολλά ωραίο» simply means «it's very nice»."),
  L("Γλωσσολόγος", "f", "Οι περισσότεροι Κύπριοι, βέβαια, περνούν άνετα στην κοινή νεοελληνική, όταν γράφουν ή μιλούν επίσημα, και ξαναγυρίζουν στη διάλεκτο μόλις η κουβέντα γίνει οικεία. Οι γλωσσολόγοι το ονομάζουν διγλωσσία. Δεν πρόκειται για «κακά ελληνικά», όπως πίστευαν κάποτε, αλλά για ένα πλούσιο σύστημα με τους δικούς του κανόνες, που κρατά λέξεις και τύπους που αλλού έχουν χαθεί.", "Most Cypriots, of course, switch easily to standard Modern Greek when they write or speak formally, and go back to the dialect as soon as the conversation becomes familiar. Linguists call this diglossia. It isn't 'bad Greek', as people once believed, but a rich system with its own rules, which keeps words and forms that have been lost elsewhere."),
 ],
 "questions": [
  Q("Γιατί η γλωσσολόγος χαρακτηρίζει την κυπριακή «την πιο ζωντανή ελληνική διάλεκτο»;", ["Γιατί έχει τις περισσότερες λέξεις", "Γιατί τη μιλούν και οι νέοι στις πόλεις, όχι μόνο οι ηλικιωμένοι", "Γιατί διδάσκεται στα σχολεία της Ελλάδας", "Γιατί είναι η παλαιότερη"], 1, "δεν τη μιλούν μόνο οι ηλικιωμένοι στα χωριά, αλλά και οι νέοι στις πόλεις"),
  Q("Πώς προφέρονται τα διπλά σύμφωνα στην κυπριακή;", ["Σαν ένα απλό σύμφωνο", "Πραγματικά διπλά, παρατεταμένα", "Δεν προφέρονται καθόλου", "Σαν φωνήεντα"], 1, "Τα διπλά σύμφωνα προφέρονται πραγματικά διπλά"),
  Q("Τι σημαίνει «έν πολλά ωραίο»;", ["Υπάρχουν πολλά ωραία", "Ήταν ωραίο", "Είναι πολύ ωραίο", "Δεν είναι ωραίο"], 2, "«έν πολλά ωραίο» σημαίνει απλώς «είναι πολύ ωραίο»"),
  Q("Τι ονομάζουν οι γλωσσολόγοι «διγλωσσία» εδώ;", ["Ότι οι Κύπριοι μιλούν και αγγλικά", "Ότι περνούν από την κοινή νεοελληνική στη διάλεκτο ανάλογα με την περίσταση", "Ότι η διάλεκτος έχει δύο αλφάβητα", "Ότι κάθε χωριό έχει άλλη διάλεκτο"], 1, "περνούν άνετα στην κοινή νεοελληνική ... και ξαναγυρίζουν στη διάλεκτο"),
 ],
 "gloss": {"Ελλαδίτης": "Ελλαδίτης — Greek from Greece (as opposed to Cyprus)", "διάλεκτος": "διάλεκτος — dialect", "σύμφωνα": "σύμφωνο — consonant", "παρατεταμένο": "παρατεταμένος — lengthened, prolonged", "φωνήεντα": "φωνήεν — vowel", "συντομεύεται": "συντομεύομαι — to be shortened", "οικεία": "οικείος — familiar, intimate", "διγλωσσία": "διγλωσσία — diglossia"},
})
rnd = random.Random(206)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-206.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
