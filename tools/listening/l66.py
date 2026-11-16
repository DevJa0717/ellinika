# Source for library/listening/listening-66.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l66.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l66-ann-kopadi", "title": "Ένα κοπάδι στις ράγες", "title_en": "A flock on the tracks", "type": "announcement", "level": "B2",
 "context_el": "Ταξιδεύετε με τρένο από την Αθήνα προς τη Θεσσαλονίκη. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα του συρμού.",
 "script": [
  L("Συνοδός", "m", "Κυρίες και κύριοι, σας ενημερώνουμε ότι ο συρμός έχει σταματήσει προσωρινά έξω από τη Λάρισα, επειδή ένα κοπάδι πρόβατα βρίσκεται πάνω στις ράγες. Ο βοσκός έχει ειδοποιηθεί και προσπαθεί να απομακρύνει τα ζώα.", "Ladies and gentlemen, we'd like to inform you that the train has stopped temporarily outside Larisa because a flock of sheep is on the tracks. The shepherd has been notified and is trying to move the animals away."),
  L("Συνοδός", "m", "Εκτιμούμε ότι η καθυστέρηση δεν θα ξεπεράσει τα είκοσι λεπτά. Παρακαλούμε να μην κατεβαίνετε από τον συρμό για κανέναν λόγο. Οι επιβάτες που έχουν ανταπόκριση στη Θεσσαλονίκη μπορούν να απευθυνθούν στον συνοδό του βαγονιού τους.", "We estimate that the delay will not exceed twenty minutes. Please do not get off the train for any reason. Passengers with a connection in Thessaloniki can speak to the attendant in their carriage."),
  L("Συνοδός", "m", "Στο κυλικείο, στο βαγόνι τέσσερα, προσφέρεται δωρεάν νερό. Ευχαριστούμε για την υπομονή σας.", "Free water is available at the snack bar in carriage four. Thank you for your patience."),
 ],
 "questions": [
  Q("Γιατί σταμάτησε το τρένο;", ["Λόγω βλάβης", "Επειδή ένα κοπάδι πρόβατα βρίσκεται στις ράγες", "Λόγω κακοκαιρίας", "Επειδή αρρώστησε ένας επιβάτης"], 1, "ένα κοπάδι πρόβατα βρίσκεται πάνω στις ράγες"),
  Q("Τι πρέπει να κάνουν όσοι έχουν ανταπόκριση στη Θεσσαλονίκη;", ["Να κατέβουν στη Λάρισα", "Να τηλεφωνήσουν στην εταιρεία", "Να απευθυνθούν στον συνοδό του βαγονιού τους", "Να αγοράσουν νέο εισιτήριο"], 2, "μπορούν να απευθυνθούν στον συνοδό του βαγονιού τους"),
  Q("Τι προσφέρεται δωρεάν;", ["Καφές", "Νερό", "Σάντουιτς", "Ένα νέο εισιτήριο"], 1, "προσφέρεται δωρεάν νερό"),
 ],
 "gloss": {"συρμού": "συρμός — train", "κοπάδι": "κοπάδι — flock, herd", "ράγες": "ράγα — rail, track", "βοσκός": "βοσκός — shepherd", "ανταπόκριση": "ανταπόκριση — connection (transport)", "βαγονιού": "βαγόνι — carriage", "κυλικείο": "κυλικείο — snack bar, canteen"},
})

ITEMS.append({
 "id": "l66-vm-architektonas", "title": "Μήνυμα από τον αρχιτέκτονα", "title_en": "A message from the architect", "type": "voicemail", "level": "B2",
 "context_el": "Ετοιμάζετε την ανακαίνιση του διαμερίσματός σας. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Αρχιτέκτονας", "m", "Καλησπέρα, κυρία Δημητρίου, ο Σωτήρης είμαι, ο αρχιτέκτονας. Σας τηλεφωνώ για τον τοίχο ανάμεσα στην κουζίνα και το σαλόνι. Δυστυχώς, ο πολιτικός μηχανικός διαπίστωσε ότι είναι φέρων τοίχος, οπότε δεν μπορούμε να τον γκρεμίσουμε ολόκληρο.", "Good evening, Mrs Dimitriou, it's Sotiris, the architect. I'm calling about the wall between the kitchen and the living room. Unfortunately, the civil engineer found that it's a load-bearing wall, so we can't knock all of it down."),
  L("Αρχιτέκτονας", "m", "Υπάρχει, όμως, μια λύση: να ανοίξουμε ένα μεγάλο άνοιγμα στη μέση, με ένα μεταλλικό δοκάρι από πάνω. Έτσι θα έχετε σχεδόν την ίδια αίσθηση ανοιχτού χώρου. Το κόστος αυξάνεται περίπου κατά οκτακόσια ευρώ, και θα χρειαστεί μια μικρή άδεια από την πολεοδομία.", "But there is a solution: to make a large opening in the middle, with a metal beam above it. That way you'll have almost the same open-plan feeling. The cost goes up by about eight hundred euros, and we'll need a small permit from the planning office."),
  L("Αρχιτέκτονας", "m", "Θα σας στείλω τα σχέδια με email απόψε. Αν συμφωνείτε, θα ήθελα να μου το πείτε μέχρι την Πέμπτη, για να καταθέσουμε τα χαρτιά. Ευχαριστώ.", "I'll email you the plans tonight. If you agree, I'd like you to let me know by Thursday so that we can submit the papers. Thank you."),
 ],
 "questions": [
  Q("Γιατί δεν μπορούν να γκρεμίσουν ολόκληρο τον τοίχο;", ["Γιατί κοστίζει πολύ", "Γιατί είναι φέρων τοίχος", "Γιατί το απαγορεύει ο διαχειριστής", "Γιατί υπάρχουν σωλήνες μέσα"], 1, "είναι φέρων τοίχος"),
  Q("Ποια λύση προτείνει ο αρχιτέκτονας;", ["Να μείνει ο τοίχος όπως είναι", "Να μετακινηθεί η κουζίνα", "Ένα μεγάλο άνοιγμα στη μέση με μεταλλικό δοκάρι", "Μια συρόμενη πόρτα"], 2, "να ανοίξουμε ένα μεγάλο άνοιγμα στη μέση, με ένα μεταλλικό δοκάρι από πάνω"),
  Q("Μέχρι πότε πρέπει να απαντήσει η κυρία Δημητρίου;", ["Μέχρι απόψε", "Μέχρι την Πέμπτη", "Μέχρι το τέλος του μήνα", "Μέχρι τη Δευτέρα"], 1, "μέχρι την Πέμπτη"),
 ],
 "gloss": {"ανακαίνιση": "ανακαίνιση — renovation", "πολιτικός μηχανικός": "πολιτικός μηχανικός — civil engineer", "φέρων τοίχος": "φέρων τοίχος — load-bearing wall", "γκρεμίσουμε": "γκρεμίζω — to knock down, demolish", "άνοιγμα": "άνοιγμα — opening", "δοκάρι": "δοκάρι — beam", "πολεοδομία": "πολεοδομία — planning office", "καταθέσουμε": "καταθέτω — to submit (papers)"},
})

ITEMS.append({
 "id": "l66-dia-koumparos", "title": "Ποιος θα γίνει κουμπάρος;", "title_en": "Who will be best man?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι που ετοιμάζει τον γάμο του συζητά για τους κουμπάρους.",
 "script": [
  L("Δανάη", "f", "Πρέπει να αποφασίσουμε επιτέλους για τους κουμπάρους. Ο παπάς θέλει τα ονόματα μέχρι το τέλος του μήνα.", "We've finally got to decide about the koumbaroi. The priest wants the names by the end of the month."),
  L("Φώτης", "m", "Εγώ σκεφτόμουν τον Άρη. Είμαστε φίλοι από το δημοτικό. Το πρόβλημα είναι ότι η μάνα μου περιμένει να διαλέξω τον ξάδερφό μου, γιατί ο πατέρας του ήταν κουμπάρος στον γάμο των γονιών μου.", "I was thinking of Aris. We've been friends since primary school. The problem is that my mum expects me to choose my cousin, because his father was best man at my parents' wedding."),
  L("Δανάη", "f", "Μπορούμε να έχουμε δύο κουμπάρους. Πολλά ζευγάρια το κάνουν πια. Εγώ θα ήθελα τη Μυρτώ, αλλά θα πρέπει να είναι ορθόδοξη για να μπορεί να στέψει, και εκείνη είναι καθολική.", "We can have two koumbaroi. Lots of couples do that now. I'd like Myrto, but she'd have to be Orthodox to be able to crown us, and she's Catholic."),
  L("Φώτης", "m", "Τότε ας στέψουν ο Άρης και ο ξάδερφός μου, και η Μυρτώ ας είναι δίπλα σου σε όλη την προετοιμασία και στη γιορτή. Το σημαντικό είναι να είναι εκεί.", "Then let Aris and my cousin do the crowning, and Myrto can be by your side for all the preparations and at the party. What matters is that she's there."),
 ],
 "questions": [
  Q("Γιατί η μητέρα του Φώτη θέλει τον ξάδερφό του για κουμπάρο;", ["Γιατί είναι ο καλύτερος φίλος του", "Γιατί ο πατέρας του ξαδέρφου ήταν κουμπάρος στον γάμο των γονιών του", "Γιατί είναι ορθόδοξος", "Γιατί μένει κοντά"], 1, "γιατί ο πατέρας του ήταν κουμπάρος στον γάμο των γονιών μου"),
  Q("Γιατί δεν μπορεί η Μυρτώ να στέψει;", ["Γιατί μένει στο εξωτερικό", "Γιατί είναι καθολική", "Γιατί είναι πολύ νέα", "Γιατί δεν τη θέλει ο παπάς"], 1, "θα πρέπει να είναι ορθόδοξη για να μπορεί να στέψει, και εκείνη είναι καθολική"),
  Q("Ποια λύση προτείνει ο Φώτης;", ["Να μην έχουν κουμπάρους", "Να στέψει μόνο η Μυρτώ", "Να στέψουν ο Άρης και ο ξάδερφός του, και η Μυρτώ να είναι δίπλα στη Δανάη", "Να αναβάλουν τον γάμο"], 2, "ας στέψουν ο Άρης και ο ξάδερφός μου, και η Μυρτώ ας είναι δίπλα σου"),
 ],
 "gloss": {"κουμπάρους": "κουμπάρος — best man, sponsor at a wedding or baptism", "παπάς": "παπάς — priest", "ξάδερφό": "ξάδερφος — cousin", "ορθόδοξη": "ορθόδοξος — Orthodox", "στέψει": "στέφω — to crown (the couple, in an Orthodox wedding)", "καθολική": "καθολικός — Catholic", "προετοιμασία": "προετοιμασία — preparation"},
})

ITEMS.append({
 "id": "l66-dia-prosklitiria", "title": "Προσκλητήρια για τη βάφτιση", "title_en": "Invitations for the christening", "type": "dialogue", "level": "B2",
 "context_el": "Μια μητέρα μιλά με έναν υπάλληλο σε ένα τυπογραφείο.",
 "script": [
  L("Μητέρα", "f", "Καλημέρα. Βαφτίζουμε την κόρη μας τον Ιούνιο και θα θέλαμε προσκλητήρια. Κάτι απλό, όχι πολύ φανταχτερό.", "Good morning. We're christening our daughter in June and we'd like invitations. Something simple, not too flashy."),
  L("Υπάλληλος", "m", "Βεβαίως. Έχουμε αυτά εδώ, σε ανακυκλωμένο χαρτί, με ένα μικρό σχέδιο από λουλούδια. Το ελάχιστο είναι πενήντα κομμάτια, και η τιμή είναι ένα ευρώ και είκοσι το ένα, μαζί με τον φάκελο.", "Of course. We have these here, on recycled paper, with a small floral design. The minimum is fifty, and the price is one euro twenty each, envelope included."),
  L("Μητέρα", "f", "Ωραία. Μπορείτε να τυπώσετε και το όνομα του νονού; Δεν έχει αποφασιστεί ακόμη το όνομα της μικρής, όμως. Θα το μάθουν όλοι στην εκκλησία.", "Lovely. Can you also print the godfather's name? But the little one's name hasn't been decided yet. Everyone will find out in church."),
  L("Υπάλληλος", "m", "Κανένα πρόβλημα, συνηθίζεται. Θα γράψουμε «τη βάφτιση της κόρης μας» χωρίς όνομα. Θα σας στείλω ένα δοκίμιο με email αύριο, και αν το εγκρίνετε, τα προσκλητήρια θα είναι έτοιμα σε μία εβδομάδα.", "No problem, that's common. We'll write 'the christening of our daughter' without a name. I'll email you a proof tomorrow, and if you approve it, the invitations will be ready in a week."),
 ],
 "questions": [
  Q("Τι είδους προσκλητήρια θέλει η μητέρα;", ["Πολύ φανταχτερά", "Κάτι απλό", "Χρυσά", "Ηλεκτρονικά"], 1, "Κάτι απλό, όχι πολύ φανταχτερό"),
  Q("Πόσο κοστίζει κάθε προσκλητήριο;", ["Ένα ευρώ και είκοσι, μαζί με τον φάκελο", "Πενήντα λεπτά", "Δύο ευρώ χωρίς τον φάκελο", "Ένα ευρώ, χωρίς τον φάκελο"], 0, "η τιμή είναι ένα ευρώ και είκοσι το ένα, μαζί με τον φάκελο"),
  Q("Γιατί δεν θα γραφτεί το όνομα του μωρού;", ["Γιατί δεν χωράει", "Γιατί δεν έχει αποφασιστεί ακόμη", "Γιατί κοστίζει επιπλέον", "Γιατί το απαγορεύει η εκκλησία"], 1, "Δεν έχει αποφασιστεί ακόμη το όνομα της μικρής"),
 ],
 "gloss": {"προσκλητήρια": "προσκλητήριο — invitation card", "βάφτιση": "βάφτιση — christening", "τυπογραφείο": "τυπογραφείο — print shop", "φανταχτερό": "φανταχτερός — flashy, showy", "ανακυκλωμένο": "ανακυκλωμένος — recycled", "φάκελο": "φάκελος — envelope", "νονού": "νονός — godfather", "δοκίμιο": "δοκίμιο — proof (printing)", "εγκρίνετε": "εγκρίνω — to approve"},
})

ITEMS.append({
 "id": "l66-int-ifaisteiologos", "title": "Η ηφαιστειολόγος της Σαντορίνης", "title_en": "The volcanologist of Santorini", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, ένας δημοσιογράφος μιλά με μια ηφαιστειολόγο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί επισκέπτες δεν ξέρουν ότι η Σαντορίνη είναι ένα ενεργό ηφαίστειο. Πρέπει να ανησυχούν;", "Many visitors don't know that Santorini is an active volcano. Should they be worried?"),
  L("Ηφαιστειολόγος", "f", "Όχι, αλλά πρέπει να το σέβονται. Η καλντέρα που θαυμάζουν δημιουργήθηκε από μια τεράστια έκρηξη την εποχή του Χαλκού, πριν από περίπου τρεισήμισι χιλιάδες χρόνια. Από τότε το ηφαίστειο έχει εκραγεί αρκετές φορές, όμως με πολύ μικρότερη ένταση.", "No, but they should respect it. The caldera they admire was created by a huge eruption in the Bronze Age, about three and a half thousand years ago. Since then the volcano has erupted several times, but with much less intensity."),
  L("Δημοσιογράφος", "m", "Πώς παρακολουθείτε το ηφαίστειο;", "How do you monitor the volcano?"),
  L("Ηφαιστειολόγος", "f", "Έχουμε σεισμογράφους σε όλο το νησί, όργανα που μετρούν την παραμόρφωση του εδάφους και αισθητήρες για τα αέρια. Ο χειμώνας του 2025, με τους χιλιάδες σεισμούς ανάμεσα στη Σαντορίνη και την Αμοργό, μας θύμισε πόσο σημαντικό είναι να ενημερώνουμε σωστά τον κόσμο, χωρίς να προκαλούμε πανικό.", "We have seismographs all over the island, instruments that measure ground deformation and sensors for gases. The winter of 2025, with the thousands of earthquakes between Santorini and Amorgos, reminded us how important it is to inform people properly, without causing panic."),
 ],
 "questions": [
  Q("Πώς δημιουργήθηκε η καλντέρα;", ["Από έναν σεισμό το 2025", "Από μια τεράστια έκρηξη την εποχή του Χαλκού", "Από τη διάβρωση της θάλασσας", "Από ανθρώπινα έργα"], 1, "δημιουργήθηκε από μια τεράστια έκρηξη την εποχή του Χαλκού"),
  Q("Τι μετρούν τα όργανα, εκτός από τους σεισμούς;", ["Τη θερμοκρασία της θάλασσας", "Την παραμόρφωση του εδάφους και τα αέρια", "Τον αριθμό των τουριστών", "Την ταχύτητα του ανέμου"], 1, "όργανα που μετρούν την παραμόρφωση του εδάφους και αισθητήρες για τα αέρια"),
  Q("Τι τους θύμισε ο χειμώνας του 2025;", ["Ότι το ηφαίστειο δεν είναι πια ενεργό", "Ότι πρέπει να κλείσουν το νησί", "Πόσο σημαντικό είναι να ενημερώνουν σωστά τον κόσμο χωρίς πανικό", "Ότι χρειάζονται περισσότερους τουρίστες"], 2, "πόσο σημαντικό είναι να ενημερώνουμε σωστά τον κόσμο, χωρίς να προκαλούμε πανικό"),
 ],
 "gloss": {"ηφαιστειολόγο": "ηφαιστειολόγος — volcanologist", "ενεργό": "ενεργός — active", "καλντέρα": "καλντέρα — caldera", "έκρηξη": "έκρηξη — eruption, explosion", "εποχή του Χαλκού": "εποχή του Χαλκού — Bronze Age", "σεισμογράφους": "σεισμογράφος — seismograph", "παραμόρφωση": "παραμόρφωση — deformation", "αισθητήρες": "αισθητήρας — sensor"},
})

ITEMS.append({
 "id": "l66-rep-megaro-voulis", "title": "Το Μέγαρο της Βουλής", "title_en": "The Parliament building", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από μια εκπομπή για τα κτίρια της Αθήνας.",
 "script": [
  L("Ρεπόρτερ", "m", "Το επιβλητικό κτίριο πάνω από την πλατεία Συντάγματος δεν χτίστηκε για τη Βουλή. Χτίστηκε στα χρόνια του βασιλιά Όθωνα, για να χρησιμεύσει ως ανάκτορο, σε σχέδια του Βαυαρού αρχιτέκτονα Φρίντριχ φον Γκέρτνερ.", "The imposing building above Syntagma Square was not built for Parliament. It was built in the reign of King Otto to serve as a palace, to designs by the Bavarian architect Friedrich von Gärtner."),
  L("Ρεπόρτερ", "m", "Η Βουλή των Ελλήνων εγκαταστάθηκε εδώ μόλις το 1935. Μπροστά από το κτίριο βρίσκεται το Μνημείο του Άγνωστου Στρατιώτη, που φυλάσσεται μέρα και νύχτα από τους εύζωνες της Προεδρικής Φρουράς.", "The Hellenic Parliament only moved here in 1935. In front of the building is the Tomb of the Unknown Soldier, guarded day and night by the evzones of the Presidential Guard."),
  L("Ρεπόρτερ", "m", "Η αλλαγή της φρουράς γίνεται κάθε ώρα και προσελκύει πλήθος τουριστών. Την Κυριακή το πρωί η τελετή είναι πιο επίσημη, με μπάντα και περισσότερους εύζωνες. Οι επισκέπτες μπορούν επίσης να ξεναγηθούν μέσα στο κτίριο, αφού κλείσουν ραντεβού.", "The changing of the guard takes place every hour and draws crowds of tourists. On Sunday morning the ceremony is more formal, with a band and more evzones. Visitors can also take a guided tour inside the building after booking an appointment."),
 ],
 "questions": [
  Q("Για ποιον σκοπό χτίστηκε αρχικά το κτίριο;", ["Ως Βουλή", "Ως ανάκτορο", "Ως μουσείο", "Ως πανεπιστήμιο"], 1, "για να χρησιμεύσει ως ανάκτορο"),
  Q("Πότε εγκαταστάθηκε εκεί η Βουλή;", ["Το 1835", "Το 1935", "Το 1975", "Στα χρόνια του Όθωνα"], 1, "εγκαταστάθηκε εδώ μόλις το 1935"),
  Q("Τι διαφέρει την Κυριακή το πρωί;", ["Δεν γίνεται αλλαγή φρουράς", "Η τελετή είναι πιο επίσημη, με μπάντα", "Το κτίριο είναι κλειστό", "Η είσοδος είναι δωρεάν"], 1, "Την Κυριακή το πρωί η τελετή είναι πιο επίσημη, με μπάντα"),
 ],
 "gloss": {"επιβλητικό": "επιβλητικός — imposing", "χρησιμεύσει": "χρησιμεύω — to serve (as)", "ανάκτορο": "ανάκτορο — palace", "Βαυαρού": "Βαυαρός — Bavarian", "εύζωνες": "εύζωνας — evzone (Presidential Guard soldier)", "αλλαγή της φρουράς": "αλλαγή της φρουράς — changing of the guard", "ξεναγηθούν": "ξεναγούμαι — to be given a guided tour"},
})

ITEMS.append({
 "id": "l66-dia-spasmeno-donti", "title": "Ένα σπασμένο δόντι την Κυριακή", "title_en": "A broken tooth on a Sunday", "type": "dialogue", "level": "B2",
 "context_el": "Ένας άντρας τηλεφωνεί σε ένα εφημερεύον οδοντιατρείο.",
 "script": [
  L("Ασθενής", "m", "Καλημέρα. Έσπασε ένα κομμάτι από ένα πίσω δόντι, ενώ έτρωγα παξιμάδι. Δεν πονάει πολύ, αλλά έχει μείνει μια αιχμηρή άκρη που μου κόβει τη γλώσσα.", "Good morning. A piece broke off one of my back teeth while I was eating a rusk. It doesn't hurt much, but there's a sharp edge left that's cutting my tongue."),
  L("Οδοντίατρος", "f", "Καταλαβαίνω. Πονάει όταν πίνετε κάτι κρύο ή ζεστό;", "I see. Does it hurt when you drink something cold or hot?"),
  L("Ασθενής", "m", "Λίγο με το κρύο νερό, ναι.", "A little with cold water, yes."),
  L("Οδοντίατρος", "f", "Δεν φαίνεται επείγον, αλλά καλό είναι να το δούμε σήμερα, για να καλύψουμε προσωρινά την άκρη. Ελάτε στις δώδεκα. Μέχρι τότε, μασάτε από την άλλη πλευρά και αποφύγετε τα πολύ κρύα ποτά. Τη μόνιμη αποκατάσταση θα την κάνει ο οδοντίατρός σας μέσα στην εβδομάδα.", "It doesn't sound urgent, but it's best to see it today so that we can cover the edge temporarily. Come at twelve. Until then, chew on the other side and avoid very cold drinks. Your own dentist will do the permanent repair during the week."),
 ],
 "questions": [
  Q("Πώς έσπασε το δόντι;", ["Σε ένα ατύχημα", "Ενώ έτρωγε παξιμάδι", "Ενώ έπαιζε ποδόσφαιρο", "Στον ύπνο του"], 1, "ενώ έτρωγα παξιμάδι"),
  Q("Ποιο είναι το κύριο πρόβλημα του ασθενούς;", ["Έχει πολύ δυνατό πόνο", "Μια αιχμηρή άκρη που του κόβει τη γλώσσα", "Πρήστηκε το πρόσωπό του", "Έχει πυρετό"], 1, "έχει μείνει μια αιχμηρή άκρη που μου κόβει τη γλώσσα"),
  Q("Τι θα γίνει σήμερα στο οδοντιατρείο;", ["Η μόνιμη αποκατάσταση", "Θα βγει το δόντι", "Θα καλυφθεί προσωρινά η άκρη", "Μόνο μια ακτινογραφία"], 2, "για να καλύψουμε προσωρινά την άκρη"),
 ],
 "gloss": {"εφημερεύον": "εφημερεύων — on duty (pharmacy, clinic)", "παξιμάδι": "παξιμάδι — rusk, twice-baked bread", "αιχμηρή": "αιχμηρός — sharp", "επείγον": "επείγων — urgent", "μασάτε": "μασάω — to chew", "μόνιμη": "μόνιμος — permanent", "αποκατάσταση": "αποκατάσταση — repair, restoration"},
})

ITEMS.append({
 "id": "l66-mono-pleximo", "title": "Γιατί έμαθα να πλέκω", "title_en": "Why I learnt to knit", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για χόμπι, ένας νεαρός άντρας μιλά για το πλέξιμο.",
 "script": [
  L("Νικηφόρος", "m", "Έμαθα να πλέκω στα είκοσι οκτώ μου, όταν έκοψα το κάπνισμα. Τα χέρια μου ήθελαν κάτι να κάνουν, και η γιαγιά μου μού έδωσε δύο βελόνες κι ένα κουβάρι μαλλί. Στην αρχή οι φίλοι μου γελούσαν.", "I learnt to knit at twenty-eight, when I gave up smoking. My hands wanted something to do, and my grandmother gave me two needles and a ball of wool. At first my friends laughed."),
  L("Νικηφόρος", "m", "Το πρώτο μου κασκόλ ήταν στραβό και γεμάτο τρύπες, αλλά το φόρεσα όλο τον χειμώνα με περηφάνια. Σήμερα πλέκω πουλόβερ, και μάλιστα με σχέδια.", "My first scarf was crooked and full of holes, but I wore it all winter with pride. Today I knit jumpers, and with patterns at that."),
  L("Νικηφόρος", "m", "Αυτό που μου αρέσει περισσότερο είναι ότι το πλέξιμο με ηρεμεί. Ο ρυθμός των βελονών λειτουργεί σαν διαλογισμός. Και, παρεμπιπτόντως, δύο από τους φίλους που γελούσαν μου ζήτησαν πέρσι να τους μάθω.", "What I like most is that knitting calms me down. The rhythm of the needles works like meditation. And, by the way, two of the friends who laughed asked me last year to teach them."),
 ],
 "questions": [
  Q("Γιατί άρχισε να πλέκει ο Νικηφόρος;", ["Γιατί του το ζήτησε η γιαγιά του", "Γιατί έκοψε το κάπνισμα και τα χέρια του ήθελαν κάτι να κάνουν", "Γιατί ήθελε να πουλάει πουλόβερ", "Γιατί βαριόταν στη δουλειά"], 1, "όταν έκοψα το κάπνισμα. Τα χέρια μου ήθελαν κάτι να κάνουν"),
  Q("Πώς ήταν το πρώτο του κασκόλ;", ["Τέλειο", "Στραβό και γεμάτο τρύπες", "Πολύ μακρύ", "Δεν το τελείωσε ποτέ"], 1, "ήταν στραβό και γεμάτο τρύπες"),
  Q("Τι ζήτησαν πέρσι δύο από τους φίλους του;", ["Να τους πλέξει πουλόβερ", "Να σταματήσει να πλέκει", "Να τους μάθει να πλέκουν", "Να τους δανείσει βελόνες"], 2, "μου ζήτησαν πέρσι να τους μάθω"),
 ],
 "gloss": {"πλέκω": "πλέκω — to knit", "βελόνες": "βελόνα — needle", "κουβάρι": "κουβάρι — ball (of wool)", "κασκόλ": "κασκόλ — scarf", "στραβό": "στραβός — crooked", "περηφάνια": "περηφάνια — pride", "διαλογισμός": "διαλογισμός — meditation", "παρεμπιπτόντως": "παρεμπιπτόντως — by the way"},
})

ITEMS.append({
 "id": "l66-c1-epitirisi", "title": "Ο εργοδότης που βλέπει τα πάντα", "title_en": "The employer who sees everything", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή λόγου, μια δημοσιογράφος συζητά με μια δικηγόρο για την ψηφιακή παρακολούθηση των εργαζομένων.",
 "script": [
  L("Δημοσιογράφος", "f", "Με την τηλεργασία, πολλές εταιρείες εγκατέστησαν προγράμματα που καταγράφουν τι κάνουν οι εργαζόμενοι στον υπολογιστή τους. Είναι νόμιμο αυτό;", "With remote working, many companies installed programs that record what employees do on their computers. Is that legal?"),
  L("Δικηγόρος", "f", "Εξαρτάται από το πώς γίνεται. Ο Γενικός Κανονισμός για την Προστασία Δεδομένων δεν απαγορεύει κάθε μορφή ελέγχου, απαιτεί όμως να είναι αναλογικός, δηλαδή να μην υπερβαίνει αυτό που είναι πραγματικά απαραίτητο. Ένα πρόγραμμα που τραβάει στιγμιότυπα της οθόνης κάθε πέντε λεπτά ή καταγράφει κάθε πλήκτρο δύσκολα θα θεωρηθεί αναλογικό.", "It depends on how it's done. The General Data Protection Regulation doesn't forbid every form of monitoring, but it requires it to be proportionate, that is, not to go beyond what is genuinely necessary. A program that takes screenshots every five minutes or records every keystroke will hardly be considered proportionate."),
  L("Δημοσιογράφος", "f", "Και ο εργαζόμενος πρέπει να ενημερώνεται;", "And does the employee have to be informed?"),
  L("Δικηγόρος", "f", "Οπωσδήποτε. Η κρυφή παρακολούθηση είναι κατά κανόνα παράνομη. Ο εργαζόμενος πρέπει να γνωρίζει τι συλλέγεται, για ποιον σκοπό και για πόσο καιρό. Πέρα από τη νομική πλευρά, όμως, υπάρχει και το ζήτημα της εμπιστοσύνης. Έρευνες δείχνουν ότι η υπερβολική επιτήρηση συχνά μειώνει την απόδοση, αντί να την αυξάνει, γιατί οι εργαζόμενοι νιώθουν ότι αντιμετωπίζονται ως ύποπτοι.", "Absolutely. Covert monitoring is, as a rule, illegal. Employees must know what is being collected, for what purpose and for how long. Beyond the legal side, though, there's also the issue of trust. Research shows that excessive surveillance often reduces productivity instead of increasing it, because employees feel they are being treated as suspects."),
 ],
 "questions": [
  Q("Τι απαιτεί ο Κανονισμός για τον έλεγχο των εργαζομένων;", ["Να απαγορεύεται κάθε έλεγχος", "Να είναι αναλογικός", "Να γίνεται μόνο στο γραφείο", "Να εγκρίνεται από τα δικαστήρια"], 1, "απαιτεί όμως να είναι αναλογικός"),
  Q("Ποιο παράδειγμα δίνει για μη αναλογικό έλεγχο;", ["Τον έλεγχο των ωρών άφιξης", "Ένα πρόγραμμα που τραβάει στιγμιότυπα της οθόνης κάθε πέντε λεπτά", "Τη χρήση εταιρικού email", "Τις ετήσιες αξιολογήσεις"], 1, "Ένα πρόγραμμα που τραβάει στιγμιότυπα της οθόνης κάθε πέντε λεπτά"),
  Q("Τι ισχύει για την κρυφή παρακολούθηση;", ["Επιτρέπεται πάντα", "Είναι κατά κανόνα παράνομη", "Επιτρέπεται στην τηλεργασία", "Επιτρέπεται για έναν μήνα"], 1, "Η κρυφή παρακολούθηση είναι κατά κανόνα παράνομη"),
  Q("Γιατί η υπερβολική επιτήρηση μειώνει συχνά την απόδοση;", ["Γιατί τα προγράμματα επιβραδύνουν τους υπολογιστές", "Γιατί οι εργαζόμενοι νιώθουν ότι αντιμετωπίζονται ως ύποπτοι", "Γιατί κοστίζει πολύ", "Γιατί οι διευθυντές δεν τη χρησιμοποιούν"], 1, "οι εργαζόμενοι νιώθουν ότι αντιμετωπίζονται ως ύποπτοι"),
 ],
 "gloss": {"παρακολούθηση": "παρακολούθηση — monitoring, surveillance", "τηλεργασία": "τηλεργασία — remote working", "Γενικός Κανονισμός για την Προστασία Δεδομένων": "Γενικός Κανονισμός για την Προστασία Δεδομένων — General Data Protection Regulation (GDPR)", "αναλογικός": "αναλογικός — proportionate", "υπερβαίνει": "υπερβαίνω — to exceed", "στιγμιότυπα της οθόνης": "στιγμιότυπο οθόνης — screenshot", "πλήκτρο": "πλήκτρο — key (keyboard)", "επιτήρηση": "επιτήρηση — surveillance", "ύποπτοι": "ύποπτος — suspect"},
})

ITEMS.append({
 "id": "l66-c1-polytechneio", "title": "Η εξέγερση του Πολυτεχνείου", "title_en": "The Polytechnic uprising", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού για την εξέγερση του Πολυτεχνείου τον Νοέμβριο του 1973.",
 "script": [
  L("Ιστορικός", "m", "Το φθινόπωρο του 1973 η δικτατορία των συνταγματαρχών επιχειρούσε μια ελεγχόμενη «φιλελευθεροποίηση». Στις 14 Νοεμβρίου, φοιτητές κατέλαβαν το Πολυτεχνείο της Αθήνας. Μέσα σε λίγες ώρες, το κτίριο της οδού Πατησίων έγινε σύμβολο της αντίστασης, και χιλιάδες πολίτες συγκεντρώθηκαν έξω από τα κάγκελα.", "In the autumn of 1973 the colonels' dictatorship was attempting a controlled 'liberalisation'. On 14 November, students occupied the Athens Polytechnic. Within a few hours the building on Patision Street became a symbol of resistance, and thousands of citizens gathered outside the railings."),
  L("Ιστορικός", "m", "Οι φοιτητές έστησαν έναν αυτοσχέδιο ραδιοφωνικό σταθμό, που μετέδιδε το σύνθημα «Ψωμί, Παιδεία, Ελευθερία». Τα ξημερώματα της 17ης Νοεμβρίου, ένα άρμα μάχης γκρέμισε την κεντρική πύλη, και ο στρατός εκκένωσε το κτίριο. Η έρευνα των ιστορικών κατέγραψε τουλάχιστον είκοσι τέσσερις νεκρούς στις ταραχές εκείνων των ημερών, ενώ ο ακριβής απολογισμός αμφισβητήθηκε για χρόνια.", "The students set up a makeshift radio station, which broadcast the slogan 'Bread, Education, Freedom'. In the early hours of 17 November, a tank brought down the main gate, and the army cleared the building. Historians' research recorded at least twenty-four dead in the unrest of those days, while the exact toll was disputed for years."),
  L("Ιστορικός", "m", "Παραδόξως, το άμεσο αποτέλεσμα δεν ήταν η πτώση της χούντας, αλλά η σκλήρυνσή της: λίγες μέρες αργότερα, ο Ιωαννίδης ανέτρεψε τον Παπαδόπουλο. Η δικτατορία κατέρρευσε τον Ιούλιο του 1974, μετά την τραγωδία της Κύπρου. Ωστόσο, το Πολυτεχνείο έμεινε στη συλλογική μνήμη ως η στιγμή που η κοινωνία ύψωσε ανοιχτά το ανάστημά της.", "Paradoxically, the immediate result was not the fall of the junta but its hardening: a few days later, Ioannidis overthrew Papadopoulos. The dictatorship collapsed in July 1974, after the tragedy of Cyprus. Nevertheless, the Polytechnic remained in collective memory as the moment when society openly stood up."),
 ],
 "questions": [
  Q("Τι επιχειρούσε η δικτατορία το φθινόπωρο του 1973;", ["Να κλείσει τα πανεπιστήμια", "Μια ελεγχόμενη «φιλελευθεροποίηση»", "Να προκηρύξει άμεσα εκλογές", "Να καταργήσει τη μοναρχία"], 1, "επιχειρούσε μια ελεγχόμενη «φιλελευθεροποίηση»"),
  Q("Τι έκαναν οι φοιτητές μέσα στο Πολυτεχνείο;", ["Έγραφαν εφημερίδα", "Έστησαν έναν αυτοσχέδιο ραδιοφωνικό σταθμό", "Οργάνωσαν εκλογές", "Έδιναν εξετάσεις"], 1, "Οι φοιτητές έστησαν έναν αυτοσχέδιο ραδιοφωνικό σταθμό"),
  Q("Τι λέει ο ιστορικός για τον αριθμό των νεκρών;", ["Ότι δεν υπήρξαν νεκροί", "Ότι καταγράφηκαν τουλάχιστον είκοσι τέσσερις, ενώ ο ακριβής απολογισμός αμφισβητήθηκε", "Ότι ήταν εκατοντάδες", "Ότι δεν έγινε ποτέ έρευνα"], 1, "κατέγραψε τουλάχιστον είκοσι τέσσερις νεκρούς"),
  Q("Ποιο ήταν, παραδόξως, το άμεσο αποτέλεσμα;", ["Η πτώση της χούντας", "Η σκλήρυνση της χούντας", "Η επιστροφή του βασιλιά", "Η ένταξη στην ΕΟΚ"], 1, "δεν ήταν η πτώση της χούντας, αλλά η σκλήρυνσή της"),
 ],
 "gloss": {"συνταγματαρχών": "συνταγματάρχης — colonel", "φιλελευθεροποίηση": "φιλελευθεροποίηση — liberalisation", "κατέλαβαν": "καταλαμβάνω — to occupy", "αυτοσχέδιο": "αυτοσχέδιος — makeshift, improvised", "μετέδιδε": "μεταδίδω — to broadcast", "άρμα μάχης": "άρμα μάχης — tank", "απολογισμός": "απολογισμός — toll, tally", "σκλήρυνσή": "σκλήρυνση — hardening", "ανέτρεψε": "ανατρέπω — to overthrow", "κατέρρευσε": "καταρρέω — to collapse", "ύψωσε ανοιχτά το ανάστημά": "υψώνω το ανάστημά μου — to stand up (to someone)"},
})

rnd = random.Random(66)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-66.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
