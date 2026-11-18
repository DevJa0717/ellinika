# Source for library/listening/listening-240.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l240.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l240-news-ftero-anemogennitrias", "title": "Νυχτερινή μεταφορά πτερυγίων ανεμογεννήτριας: κλειστοί δρόμοι για τρεις νύχτες", "title_en": "Night transport of wind-turbine blades: roads closed for three nights", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός περιφερειακού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνήτρια", "f", "Από απόψε και για τρεις νύχτες θα γίνει η μεταφορά των πτερυγίων για το νέο αιολικό πάρκο στο βουνό πάνω από την πόλη. Κάθε πτερύγιο έχει μήκος πάνω από εξήντα μέτρα, και γι' αυτό τα ειδικά οχήματα θα κινούνται μόνο από τα μεσάνυχτα ως τις πέντε το πρωί.", "From tonight and for three nights the blades for the new wind farm on the mountain above the town will be transported. Each blade is over sixty metres long, so the special vehicles will move only from midnight to five in the morning."),
  L("Εκφωνήτρια", "f", "Η πομπή θα ξεκινά από το λιμάνι, όπου ξεφορτώθηκαν τα πτερύγια την περασμένη εβδομάδα, και θα περνά από την παραλιακή λεωφόρο και την παλιά εθνική οδό. Στα σημεία αυτά η κυκλοφορία θα διακόπτεται για περίπου είκοσι λεπτά κάθε φορά που περνά ένα όχημα.", "The convoy will set off from the port, where the blades were unloaded last week, and will go along the seafront avenue and the old national road. At those points traffic will be stopped for about twenty minutes each time a vehicle passes."),
  L("Εκφωνήτρια", "f", "Για να χωρέσουν τα οχήματα στις στροφές, το συνεργείο του δήμου αφαίρεσε προσωρινά πινακίδες, φανάρια και κάποια παγκάκια, που θα ξαναμπούν στη θέση τους μόλις τελειώσει η μεταφορά. Οι κάτοικοι παρακαλούνται να μην αφήνουν τα αυτοκίνητά τους παρκαρισμένα στη διαδρομή.", "So that the vehicles fit round the bends, the municipal crew has temporarily removed signs, traffic lights and some benches, which will go back in place as soon as the transport is over. Residents are asked not to leave their cars parked along the route."),
  L("Εκφωνήτρια", "f", "Η τροχαία συνιστά στους οδηγούς που ταξιδεύουν τη νύχτα να υπολογίζουν καθυστερήσεις ή να χρησιμοποιούν τη νέα εθνική οδό, όπου δεν θα υπάρξουν διακοπές.", "The traffic police advise drivers travelling at night to allow for delays or to use the new national road, where there will be no interruptions."),
 ],
 "questions": [
  Q("Γιατί τα οχήματα θα κινούνται μόνο τη νύχτα;", ["Γιατί κάνει λιγότερη ζέστη", "Γιατί τα πτερύγια είναι πολύ μεγάλα, πάνω από εξήντα μέτρα", "Γιατί το λιμάνι λειτουργεί μόνο τη νύχτα", "Γιατί το ζήτησαν οι κάτοικοι"], 1, "Κάθε πτερύγιο έχει μήκος πάνω από εξήντα μέτρα, και γι' αυτό τα ειδικά οχήματα θα κινούνται μόνο από τα μεσάνυχτα"),
  Q("Πόσο θα διακόπτεται η κυκλοφορία κάθε φορά;", ["Περίπου πέντε λεπτά", "Περίπου είκοσι λεπτά", "Μία ώρα", "Όλη τη νύχτα"], 1, "η κυκλοφορία θα διακόπτεται για περίπου είκοσι λεπτά κάθε φορά"),
  Q("Τι έκανε το συνεργείο του δήμου για να περάσουν τα οχήματα;", ["Έφτιαξε έναν καινούργιο δρόμο", "Αφαίρεσε προσωρινά πινακίδες, φανάρια και παγκάκια", "Έκοψε δέντρα", "Φάρδυνε τις στροφές"], 1, "αφαίρεσε προσωρινά πινακίδες, φανάρια και κάποια παγκάκια"),
  Q("Τι συνιστά η τροχαία στους οδηγούς;", ["Να μην οδηγούν καθόλου τη νύχτα", "Να χρησιμοποιούν τη νέα εθνική οδό", "Να ακολουθούν την πομπή", "Να παρκάρουν στην παραλιακή"], 1, "να χρησιμοποιούν τη νέα εθνική οδό, όπου δεν θα υπάρξουν διακοπές"),
 ],
 "gloss": {"πτερυγίων": "πτερύγιο — blade (of a turbine)", "αιολικό πάρκο": "αιολικό πάρκο — wind farm", "μήκος": "μήκος — length", "πομπή": "πομπή — convoy, procession", "ξεφορτώθηκαν": "ξεφορτώνω — to unload", "διακόπτεται": "διακόπτομαι — to be interrupted", "χωρέσουν": "χωράω — to fit", "στροφές": "στροφή — bend, turn", "αφαίρεσε": "αφαιρώ — to remove", "τροχαία": "τροχαία — traffic police", "καθυστερήσεις": "καθυστέρηση — delay"},
})
ITEMS.append({
 "id": "l240-vm-pinakothiki-ekthesi", "title": "Μήνυμα από τη δημοτική πινακοθήκη: ο πίνακάς σας θα εκτεθεί", "title_en": "A message from the municipal gallery: your painting will be shown", "type": "voicemail", "level": "B2",
 "context_el": "Ζωγραφίζετε ως ερασιτέχνης και στείλατε έναν πίνακα σε έναν διαγωνισμό. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Επιμελήτρια", "f", "Καλημέρα σας, σας παίρνω από τη Δημοτική Πινακοθήκη, η Μαρίνα είμαι, η επιμελήτρια της έκθεσης ερασιτεχνών ζωγράφων. Έχω καλά νέα: η επιτροπή διάλεξε τον πίνακά σας με το λιμάνι για την έκθεση του Δεκεμβρίου.", "Good morning, I'm calling from the Municipal Gallery, it's Marina, the curator of the amateur painters' exhibition. I have good news: the panel has chosen your painting of the harbour for the December exhibition."),
  L("Επιμελήτρια", "f", "Χρειαζόμαστε τον πίνακα εδώ ως τις είκοσι του μήνα, πλαισιωμένο και με ένα άγκιστρο στο πίσω μέρος για να κρεμαστεί. Αν δεν έχετε κορνίζα, μπορούμε να σας προτείνουμε ένα κορνιζάδικο που κάνει έκπτωση στους συμμετέχοντες.", "We need the painting here by the twentieth of the month, framed and with a hook on the back so it can be hung. If you don't have a frame, we can suggest a framer's shop that gives participants a discount."),
  L("Επιμελήτρια", "f", "Θα σας ζητήσουμε επίσης ένα σύντομο κείμενο, όχι πάνω από πενήντα λέξεις, για τον εαυτό σας και για το έργο, που θα μπει σε μια καρτελίτσα δίπλα στον πίνακα. Αν θέλετε να πουληθεί, γράψτε και την τιμή. Η πινακοθήκη δεν κρατά ποσοστό από τις πωλήσεις.", "We'll also ask you for a short text, no longer than fifty words, about yourself and the work, which will go on a small label next to the painting. If you want it to be sold, write the price too. The gallery doesn't take a percentage of sales."),
  L("Επιμελήτρια", "f", "Τα εγκαίνια θα γίνουν στις τρεις Δεκεμβρίου, στις επτά το απόγευμα, και φυσικά μπορείτε να φέρετε όποιον θέλετε. Συγχαρητήρια και πάλι, και πάρτε με αν έχετε οποιαδήποτε ερώτηση.", "The opening will be on the third of December, at seven in the evening, and of course you can bring whoever you like. Congratulations again, and call me if you have any questions."),
 ],
 "questions": [
  Q("Ποιο είναι το καλό νέο;", ["Ότι κερδίσατε ένα χρηματικό βραβείο", "Ότι ο πίνακάς σας επιλέχθηκε για την έκθεση", "Ότι πουλήθηκε ο πίνακάς σας", "Ότι σας προσλαμβάνουν στην πινακοθήκη"], 1, "η επιτροπή διάλεξε τον πίνακά σας με το λιμάνι για την έκθεση του Δεκεμβρίου"),
  Q("Πώς πρέπει να παραδοθεί ο πίνακας;", ["Τυλιγμένος σε χαρτί", "Πλαισιωμένος και με άγκιστρο στο πίσω μέρος", "Χωρίς κορνίζα", "Μαζί με τα πινέλα"], 1, "πλαισιωμένο και με ένα άγκιστρο στο πίσω μέρος για να κρεμαστεί"),
  Q("Τι θα γράφει η καρτελίτσα δίπλα στον πίνακα;", ["Μόνο τον τίτλο", "Ένα σύντομο κείμενο για τον ζωγράφο και το έργο", "Τη γνώμη της επιτροπής", "Τα στοιχεία της πινακοθήκης"], 1, "ένα σύντομο κείμενο … για τον εαυτό σας και για το έργο, που θα μπει σε μια καρτελίτσα"),
  Q("Τι ισχύει για τις πωλήσεις;", ["Η πινακοθήκη κρατά το μισό ποσό", "Η πινακοθήκη δεν κρατά ποσοστό", "Οι πίνακες δεν πωλούνται", "Την τιμή την ορίζει η επιτροπή"], 1, "Η πινακοθήκη δεν κρατά ποσοστό από τις πωλήσεις"),
 ],
 "gloss": {"πινακοθήκη": "πινακοθήκη — art gallery", "επιμελήτρια": "επιμελήτρια — curator", "ερασιτεχνών": "ερασιτέχνης — amateur", "πλαισιωμένο": "πλαισιωμένος — framed", "άγκιστρο": "άγκιστρο — hook", "κρεμαστεί": "κρεμιέμαι — to be hung", "κορνίζα": "κορνίζα — frame", "κορνιζάδικο": "κορνιζάδικο — framer's shop", "καρτελίτσα": "καρτελίτσα — small label", "ποσοστό": "ποσοστό — percentage", "εγκαίνια": "εγκαίνια — opening (of an exhibition)"},
})
ITEMS.append({
 "id": "l240-c1-mono-gyalia", "title": "Δύο φακοί πάνω στη μύτη: πώς επινοήθηκαν τα γυαλιά οράσεως", "title_en": "Two lenses on the nose: how spectacles were invented", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ιστορικό της επιστήμης σε μια ραδιοφωνική εκπομπή για τις εφευρέσεις που άλλαξαν την καθημερινότητα.",
 "script": [
  L("Ιστορικός", "f", "Για χιλιάδες χρόνια, όποιος έφτανε τα σαράντα πέντε ή τα πενήντα και άρχιζε να μη βλέπει καλά από κοντά, απλώς δεν μπορούσε πια να διαβάσει ή να κάνει λεπτές δουλειές. Για έναν γραφέα ή έναν τεχνίτη αυτό σήμαινε, στην ουσία, το τέλος της επαγγελματικής του ζωής.", "For thousands of years, anyone who reached forty-five or fifty and began to have trouble seeing close up simply could no longer read or do fine work. For a scribe or a craftsman this meant, in effect, the end of his working life."),
  L("Ιστορικός", "f", "Οι πρώτες πηγές που μιλούν καθαρά για γυαλιά έρχονται από την Ιταλία, στα τέλη του δέκατου τρίτου αιώνα. Ένας μοναχός στην Πίζα, σε ένα κήρυγμα των αρχών του δέκατου τέταρτου αιώνα, αναφέρει ότι η τέχνη των γυαλιών είχε βρεθεί λιγότερο από είκοσι χρόνια νωρίτερα. Τον εφευρέτη, όμως, δεν τον ξέρουμε.", "The first sources that speak clearly of spectacles come from Italy, at the end of the thirteenth century. A friar in Pisa, in a sermon from the early fourteenth century, mentions that the art of making spectacles had been found less than twenty years earlier. The inventor, though, we do not know."),
  L("Ιστορικός", "f", "Τα πρώτα γυαλιά είχαν κυρτούς φακούς και βοηθούσαν μόνο όσους δεν έβλεπαν από κοντά. Οι φακοί για τη μυωπία, που είναι κοίλοι, εμφανίστηκαν αρκετά αργότερα. Και για αιώνες τα γυαλιά δεν είχαν βραχίονες: τα κρατούσες στο χέρι ή τα στερέωνες πάνω στη μύτη, όπου συχνά γλιστρούσαν.", "The first spectacles had convex lenses and helped only those who couldn't see close up. Lenses for short-sightedness, which are concave, appeared considerably later. And for centuries spectacles had no arms: you held them in your hand or balanced them on your nose, where they often slipped."),
  L("Ιστορικός", "f", "Αν σκεφτεί κανείς ότι τα γυαλιά διπλασίασαν σχεδόν τα χρόνια που ένας άνθρωπος μπορούσε να διαβάζει, καταλαβαίνει γιατί ορισμένοι ιστορικοί τα θεωρούν μία από τις πιο υποτιμημένες εφευρέσεις του Μεσαίωνα. Χωρίς αυτά, η τυπογραφία ίσως να μην είχε βρει τόσους αναγνώστες.", "If you consider that spectacles almost doubled the years in which a person could read, you understand why some historians regard them as one of the most underrated inventions of the Middle Ages. Without them, printing might not have found so many readers."),
 ],
 "questions": [
  Q("Τι σήμαινε παλιά για έναν τεχνίτη η αδυναμία να βλέπει από κοντά;", ["Ότι έπρεπε να δουλεύει μόνο τη μέρα", "Ουσιαστικά το τέλος της επαγγελματικής του ζωής", "Ότι χρειαζόταν βοηθό", "Ότι έπρεπε να αλλάξει πόλη"], 1, "αυτό σήμαινε, στην ουσία, το τέλος της επαγγελματικής του ζωής"),
  Q("Τι γνωρίζουμε για τον εφευρέτη των γυαλιών;", ["Ότι ήταν μοναχός στην Πίζα", "Τίποτα, γιατί δεν ξέρουμε ποιος ήταν", "Ότι ήταν γιατρός", "Ότι ήταν Άραβας επιστήμονας"], 1, "Τον εφευρέτη, όμως, δεν τον ξέρουμε"),
  Q("Ποιους βοηθούσαν τα πρώτα γυαλιά;", ["Όσους είχαν μυωπία", "Όσους δεν έβλεπαν από κοντά", "Όσους δεν έβλεπαν τη νύχτα", "Όσους δεν ξεχώριζαν τα χρώματα"], 1, "βοηθούσαν μόνο όσους δεν έβλεπαν από κοντά"),
  Q("Γιατί ορισμένοι ιστορικοί θεωρούν τα γυαλιά υποτιμημένη εφεύρεση;", ["Γιατί ήταν πολύ φτηνά", "Γιατί σχεδόν διπλασίασαν τα χρόνια που μπορούσε κανείς να διαβάζει", "Γιατί τα χρησιμοποιούσαν μόνο οι μοναχοί", "Γιατί εμφανίστηκαν μετά την τυπογραφία"], 1, "τα γυαλιά διπλασίασαν σχεδόν τα χρόνια που ένας άνθρωπος μπορούσε να διαβάζει"),
 ],
 "gloss": {"γραφέα": "γραφέας — scribe", "τεχνίτη": "τεχνίτης — craftsman", "κήρυγμα": "κήρυγμα — sermon", "εφευρέτη": "εφευρέτης — inventor", "κυρτούς": "κυρτός — convex", "φακούς": "φακός — lens", "μυωπία": "μυωπία — short-sightedness", "κοίλοι": "κοίλος — concave", "βραχίονες": "βραχίονας — arm (of spectacles)", "στερέωνες": "στερεώνω — to fix, balance", "υποτιμημένες": "υποτιμημένος — underrated", "τυπογραφία": "τυπογραφία — printing"},
})
ITEMS.append({
 "id": "l240-c1-int-pygolampides", "title": "Μια εντομολόγος για τις πυγολαμπίδες που χάνονται από τις νύχτες μας", "title_en": "An entomologist on the fireflies disappearing from our nights", "type": "interview", "level": "C1",
 "context_el": "Μια εντομολόγος, που μελετά τα έντομα της υπαίθρου, μιλά σε μια ραδιοφωνική εκπομπή για τη φύση.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί ακροατές μάς γράφουν ότι θυμούνται πυγολαμπίδες από τα παιδικά τους χρόνια, αλλά δεν τις βλέπουν πια. Τι είναι ακριβώς αυτά τα έντομα;", "Many listeners write to tell us they remember fireflies from their childhood but don't see them any more. What exactly are these insects?"),
  L("Εντομολόγος", "f", "Είναι σκαθάρια, όχι μύγες, όπως νομίζουν πολλοί. Το φως τους παράγεται από μια χημική αντίδραση στην κοιλιά τους: μια ουσία ενώνεται με το οξυγόνο, με τη βοήθεια ενός ενζύμου, και σχεδόν όλη η ενέργεια γίνεται φως και όχι θερμότητα. Γι' αυτό λέμε ότι είναι «ψυχρό φως».", "They're beetles, not flies, as many people think. Their light is produced by a chemical reaction in their abdomen: a substance combines with oxygen, with the help of an enzyme, and almost all the energy becomes light rather than heat. That's why we call it 'cold light'."),
  L("Δημοσιογράφος", "m", "Και σε τι τους χρησιμεύει;", "And what is it for?"),
  L("Εντομολόγος", "f", "Κυρίως για να βρουν ταίρι. Κάθε είδος έχει τον δικό του κώδικα: διαφορετικό ρυθμό, διαφορετική διάρκεια αναλαμπής. Τα αρσενικά πετούν και αναβοσβήνουν, και τα θηλυκά απαντούν από το χορτάρι. Υπάρχουν μάλιστα είδη στην Αμερική όπου τα θηλυκά μιμούνται τον κώδικα άλλων ειδών, για να προσελκύσουν αρσενικά και να τα φάνε.", "Mainly to find a mate. Each species has its own code: a different rhythm, a different length of flash. The males fly and blink, and the females answer from the grass. There are even species in America where the females imitate the code of other species, to lure males and eat them."),
  L("Δημοσιογράφος", "m", "Γιατί όμως λιγοστεύουν;", "But why are they getting fewer?"),
  L("Εντομολόγος", "f", "Οι αιτίες είναι κυρίως τρεις: η καταστροφή των υγρών λιβαδιών και των όχθεων όπου ζουν οι προνύμφες τους, τα φυτοφάρμακα και, ίσως το πιο ύπουλο, ο τεχνητός φωτισμός. Αν η νύχτα είναι γεμάτη φώτα, τα σήματά τους χάνονται και δεν μπορούν να συναντηθούν. Ένας απλός τρόπος να βοηθήσουμε είναι να σβήνουμε τα εξωτερικά φώτα του κήπου τις νύχτες του καλοκαιριού. Μερικές φορές αρκεί αυτό για να ξαναφανούν.", "There are three main causes: the destruction of the wet meadows and riverbanks where their larvae live, pesticides and, perhaps the most insidious, artificial lighting. If the night is full of lights, their signals get lost and they can't find each other. A simple way to help is to switch off outdoor garden lights on summer nights. Sometimes that's enough for them to reappear."),
 ],
 "questions": [
  Q("Τι είναι στην πραγματικότητα οι πυγολαμπίδες;", ["Μύγες", "Σκαθάρια", "Πεταλούδες της νύχτας", "Μέλισσες"], 1, "Είναι σκαθάρια, όχι μύγες"),
  Q("Γιατί το φως τους λέγεται «ψυχρό»;", ["Γιατί έχει γαλάζιο χρώμα", "Γιατί σχεδόν όλη η ενέργεια γίνεται φως και όχι θερμότητα", "Γιατί φαίνεται μόνο τον χειμώνα", "Γιατί το παράγουν μόνο όταν κάνει κρύο"], 1, "σχεδόν όλη η ενέργεια γίνεται φως και όχι θερμότητα"),
  Q("Σε τι χρησιμεύει κυρίως το φως τους;", ["Για να βλέπουν πού πετούν", "Για να βρουν ταίρι", "Για να τρομάζουν τα πουλιά", "Για να ζεσταίνονται"], 1, "Κυρίως για να βρουν ταίρι"),
  Q("Γιατί ο τεχνητός φωτισμός βλάπτει τις πυγολαμπίδες;", ["Γιατί τις ζεσταίνει υπερβολικά", "Γιατί τα σήματά τους χάνονται και δεν μπορούν να συναντηθούν", "Γιατί προσελκύει τους εχθρούς τους", "Γιατί καίει τα φυτά όπου ζουν"], 1, "τα σήματά τους χάνονται και δεν μπορούν να συναντηθούν"),
 ],
 "gloss": {"πυγολαμπίδες": "πυγολαμπίδα — firefly", "εντομολόγος": "εντομολόγος — entomologist", "σκαθάρια": "σκαθάρι — beetle", "αντίδραση": "αντίδραση — reaction", "ενζύμου": "ένζυμο — enzyme", "ταίρι": "ταίρι — mate", "αναλαμπής": "αναλαμπή — flash", "αναβοσβήνουν": "αναβοσβήνω — to blink, flash on and off", "μιμούνται": "μιμούμαι — to imitate", "λιγοστεύουν": "λιγοστεύω — to dwindle", "προνύμφες": "προνύμφη — larva", "φυτοφάρμακα": "φυτοφάρμακο — pesticide", "ύπουλο": "ύπουλος — insidious"},
})

rnd = random.Random(240)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-240.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
