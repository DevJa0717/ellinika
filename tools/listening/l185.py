# Source for library/listening/listening-185.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l185.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l185-ann-perifora-epitafiou", "title": "Η περιφορά του Επιταφίου και οι κλειστοί δρόμοι", "title_en": "The Epitaphios procession and the closed roads", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου σε τοπικό ραδιοφωνικό σταθμό τη Μεγάλη Πέμπτη.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος ενημερώνει ότι αύριο, Μεγάλη Παρασκευή, οι Επιτάφιοι των τριών ενοριών του κέντρου θα βγουν από τις εκκλησίες στις εννιά το βράδυ και θα συναντηθούν στην κεντρική πλατεία γύρω στις δέκα. Από τις οχτώ και μισή ως τα μεσάνυχτα, οι δρόμοι της περιφοράς θα είναι κλειστοί για τα αυτοκίνητα.", "The municipality announces that tomorrow, Good Friday, the Epitaphios biers of the three central parishes will leave the churches at nine in the evening and will meet in the main square at around ten. From half past eight until midnight, the procession routes will be closed to cars."),
  L("Εκφωνήτρια", "f", "Παρακαλούνται οι κάτοικοι να μη σταθμεύσουν στους δρόμους αυτούς από το απόγευμα, γιατί τα αυτοκίνητα θα ρυμουλκηθούν. Τα λεωφορεία των γραμμών δύο και πέντε θα κάνουν παράκαμψη από την παραλιακή.", "Residents are asked not to park on these streets from the afternoon, because cars will be towed. Buses on routes two and five will make a detour along the seafront."),
  L("Εκφωνήτρια", "f", "Για την ασφάλεια όλων, ο δήμος ζητά από τους γονείς να προσέχουν τα παιδιά με τα κεριά, και υπενθυμίζει ότι απαγορεύονται αυστηρά τα βεγγαλικά και οι κροτίδες σε όλη τη διαδρομή.", "For everyone's safety, the municipality asks parents to watch the children with the candles, and reminds everyone that sparklers and bangers are strictly forbidden along the whole route."),
 ],
 "questions": [
  Q("Πού θα συναντηθούν οι Επιτάφιοι;", ["Στο λιμάνι", "Στην κεντρική πλατεία", "Μπροστά στο δημαρχείο", "Στη μεγαλύτερη εκκλησία"], 1, "θα συναντηθούν στην κεντρική πλατεία γύρω στις δέκα"),
  Q("Γιατί δεν πρέπει να σταθμεύσουν οι κάτοικοι στους δρόμους της περιφοράς;", ["Γιατί θα πλυθούν οι δρόμοι", "Γιατί τα αυτοκίνητα θα ρυμουλκηθούν", "Γιατί θα στηθούν πάγκοι", "Γιατί θα περάσει η μπάντα"], 1, "γιατί τα αυτοκίνητα θα ρυμουλκηθούν"),
  Q("Τι απαγορεύεται σε όλη τη διαδρομή;", ["Τα κεριά", "Οι φωτογραφίες", "Τα βεγγαλικά και οι κροτίδες", "Τα καροτσάκια"], 2, "απαγορεύονται αυστηρά τα βεγγαλικά και οι κροτίδες σε όλη τη διαδρομή"),
 ],
 "gloss": {"περιφοράς": "περιφορά — procession", "Επιτάφιοι": "Επιτάφιος — Epitaphios (decorated bier of Good Friday)", "ενοριών": "ενορία — parish", "σταθμεύσουν": "σταθμεύω — to park", "ρυμουλκηθούν": "ρυμουλκούμαι — to be towed", "παράκαμψη": "παράκαμψη — detour", "βεγγαλικά": "βεγγαλικό — sparkler, firework", "κροτίδες": "κροτίδα — banger, firecracker"},
})

ITEMS.append({
 "id": "l185-int-loukoumatzis-syrou", "title": "Ο λουκουματζής της Σύρου", "title_en": "The loukoumi maker of Syros", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν άνθρωπο που φτιάχνει λουκούμια σε ένα παλιό εργαστήριο στην Ερμούπολη.",
 "script": [
  L("Δημοσιογράφος", "f", "Από τι φτιάχνεται ένα λουκούμι;", "What is a loukoumi made of?"),
  L("Λουκουματζής", "m", "Από πολύ λίγα πράγματα: ζάχαρη, νερό και άμυλο. Το μυστικό δεν είναι τα υλικά, είναι ο χρόνος. Το μείγμα βράζει σε ένα μεγάλο χάλκινο καζάνι για ώρες, και πρέπει να ανακατεύεται συνέχεια, για να μην κολλήσει. Παλιά το ανακάτευαν με το χέρι· σήμερα έχουμε ένα μηχάνημα, αλλά το πότε είναι έτοιμο το καταλαβαίνω ακόμα με το μάτι.", "From very few things: sugar, water and starch. The secret isn't the ingredients, it's time. The mixture boils in a big copper cauldron for hours, and it has to be stirred constantly so that it doesn't stick. In the old days they stirred it by hand; today we have a machine, but I still tell when it's ready by eye."),
  L("Δημοσιογράφος", "f", "Και μετά;", "And then?"),
  L("Λουκουματζής", "m", "Το ρίχνουμε σε ξύλινες θήκες με άμυλο και το αφήνουμε να «ξεκουραστεί» μια ολόκληρη μέρα. Ύστερα το κόβουμε σε κομματάκια και το πασπαλίζουμε με ζάχαρη άχνη. Το πιο κλασικό είναι το τριαντάφυλλο, αλλά οι νέοι ζητούν και καινούργιες γεύσεις, όπως μαστίχα ή περγαμόντο.", "We pour it into wooden trays with starch and leave it to 'rest' for a whole day. Then we cut it into little pieces and dust it with icing sugar. The most classic is rose, but young people also ask for new flavours, like mastic or bergamot."),
  L("Δημοσιογράφος", "f", "Πώς άρχισε η παράδοση στο νησί;", "How did the tradition begin on the island?"),
  L("Λουκουματζής", "m", "Λένε ότι την έφεραν πρόσφυγες που ήρθαν στο νησί τον 19ο αιώνα, και ότι οι ναυτικοί που περνούσαν από το λιμάνι το έκαναν γνωστό σε όλη την Ελλάδα. Εγώ ξέρω μόνο ότι ο παππούς μου έστελνε κουτιά στους συγγενείς στην Αθήνα, και όλοι τα περίμεναν σαν δώρο.", "They say refugees who came to the island in the 19th century brought it, and that the sailors passing through the port made it known all over Greece. All I know is that my grandfather sent boxes to relatives in Athens, and everyone waited for them like a present."),
 ],
 "questions": [
  Q("Ποιο είναι, κατά τον λουκουματζή, το μυστικό του λουκουμιού;", ["Τα ακριβά υλικά", "Ο χρόνος", "Το νερό του νησιού", "Μια κρυφή συνταγή"], 1, "Το μυστικό δεν είναι τα υλικά, είναι ο χρόνος"),
  Q("Γιατί πρέπει το μείγμα να ανακατεύεται συνέχεια;", ["Για να μην κολλήσει", "Για να κρυώσει πιο γρήγορα", "Για να πάρει χρώμα", "Για να μη βγάλει αφρό"], 0, "πρέπει να ανακατεύεται συνέχεια, για να μην κολλήσει"),
  Q("Τι ζητούν οι νέοι πελάτες;", ["Λουκούμια χωρίς ζάχαρη", "Μεγαλύτερα κομμάτια", "Καινούργιες γεύσεις, όπως μαστίχα ή περγαμόντο", "Πιο φτηνά κουτιά"], 2, "οι νέοι ζητούν και καινούργιες γεύσεις, όπως μαστίχα ή περγαμόντο"),
 ],
 "gloss": {"άμυλο": "άμυλο — starch", "χάλκινο καζάνι": "χάλκινο καζάνι — copper cauldron", "ανακατεύεται": "ανακατεύομαι — to be stirred", "θήκες": "θήκη — tray, case", "πασπαλίζουμε": "πασπαλίζω — to sprinkle, dust", "ζάχαρη άχνη": "ζάχαρη άχνη — icing sugar", "περγαμόντο": "περγαμόντο — bergamot", "πρόσφυγες": "πρόσφυγας — refugee"},
})

ITEMS.append({
 "id": "l185-int-taxithetria", "title": "Η ταξιθέτρια του θεάτρου", "title_en": "The theatre usher", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια ταξιθέτρια που δουλεύει εδώ και είκοσι χρόνια σε ένα μεγάλο θέατρο.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι κάνει μια ταξιθέτρια, εκτός από το να δείχνει τις θέσεις;", "What does an usher do, apart from showing people to their seats?"),
  L("Ταξιθέτρια", "f", "Πολύ περισσότερα. Ελέγχουμε τα εισιτήρια, βοηθάμε τους ηλικιωμένους και όσους έχουν αναπηρικό αμαξίδιο, και ξέρουμε πού είναι οι έξοδοι κινδύνου, για κάθε ενδεχόμενο. Πριν ανοίξουν οι πόρτες, περνάμε όλη την αίθουσα, μήπως έχει ξεχαστεί κάτι από την προηγούμενη παράσταση.", "Much more. We check tickets, help elderly people and those in wheelchairs, and we know where the emergency exits are, just in case. Before the doors open, we go through the whole auditorium in case something has been left from the previous performance."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο δύσκολο κομμάτι;", "What's the hardest part?"),
  L("Ταξιθέτρια", "f", "Οι αργοπορημένοι. Όταν η παράσταση έχει αρχίσει, δεν μπορώ να τους βάλω στη θέση τους, γιατί θα ενοχλήσουν όλη τη σειρά. Τους κρατάω στην πόρτα ως το πρώτο διάλειμμα ή ως μια αλλαγή σκηνής. Μερικοί θυμώνουν, αλλά οι περισσότεροι καταλαβαίνουν.", "Latecomers. When the performance has started, I can't take them to their seats, because they'll disturb the whole row. I keep them at the door until the first interval or a scene change. Some get angry, but most understand."),
  L("Δημοσιογράφος", "m", "Βλέπετε τις παραστάσεις;", "Do you watch the performances?"),
  L("Ταξιθέτρια", "f", "Από την πόρτα, κομμάτια, εκατό φορές την καθεμιά. Ξέρω πολλά έργα απέξω. Κάποτε ένας ηθοποιός ξέχασε τα λόγια του, και τον βοήθησα ψιθυριστά από το βάθος της αίθουσας. Δεν το έμαθε ποτέ κανείς.", "From the door, in pieces, a hundred times each. I know many plays by heart. Once an actor forgot his lines, and I helped him in a whisper from the back of the auditorium. Nobody ever found out."),
 ],
 "questions": [
  Q("Τι κάνουν οι ταξιθέτες πριν ανοίξουν οι πόρτες;", ["Πουλάνε προγράμματα", "Περνούν όλη την αίθουσα, μήπως έχει ξεχαστεί κάτι", "Καθαρίζουν τη σκηνή", "Δοκιμάζουν τα φώτα"], 1, "περνάμε όλη την αίθουσα, μήπως έχει ξεχαστεί κάτι από την προηγούμενη παράσταση"),
  Q("Τι κάνει με όσους έρχονται αργά;", ["Τους βάζει αμέσως στη θέση τους", "Τους στέλνει σπίτι", "Τους κρατάει στην πόρτα ως το διάλειμμα ή μια αλλαγή σκηνής", "Τους δίνει άλλες θέσεις στον εξώστη"], 2, "Τους κρατάω στην πόρτα ως το πρώτο διάλειμμα ή ως μια αλλαγή σκηνής"),
  Q("Τι έκανε κάποτε όταν ένας ηθοποιός ξέχασε τα λόγια του;", ["Τον βοήθησε ψιθυριστά από το βάθος της αίθουσας", "Άναψε τα φώτα", "Ειδοποίησε τον σκηνοθέτη", "Χειροκρότησε για να κερδίσει χρόνο"], 0, "τον βοήθησα ψιθυριστά από το βάθος της αίθουσας"),
 ],
 "gloss": {"ταξιθέτρια": "ταξιθέτρια — (female) usher", "αναπηρικό αμαξίδιο": "αναπηρικό αμαξίδιο — wheelchair", "έξοδοι κινδύνου": "έξοδος κινδύνου — emergency exit", "ενδεχόμενο": "ενδεχόμενο — eventuality", "αίθουσα": "αίθουσα — auditorium, hall", "αργοπορημένοι": "αργοπορημένος — latecomer", "διάλειμμα": "διάλειμμα — interval", "ψιθυριστά": "ψιθυριστά — in a whisper"},
})

ITEMS.append({
 "id": "l185-vm-scholiki-fotografisi", "title": "Μήνυμα για τη μέρα της σχολικής φωτογράφισης", "title_en": "A message about school photo day", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα από τη γραμματεία του σχολείου του παιδιού σας στον τηλεφωνητή σας.",
 "script": [
  L("Γραμματέας", "f", "Καλησπέρα σας, σας τηλεφωνώ από τη γραμματεία του 4ου Δημοτικού. Σας θυμίζουμε ότι την Πέμπτη έρχεται ο φωτογράφος για τις ατομικές και τις ομαδικές φωτογραφίες. Ο Άγγελος είναι στη δεύτερη ομάδα, άρα θα φωτογραφηθεί μετά το πρώτο διάλειμμα.", "Good afternoon, I'm calling from the office of the 4th Primary School. We'd like to remind you that on Thursday the photographer is coming for the individual and group photos. Angelos is in the second group, so he'll be photographed after the first break."),
  L("Γραμματέας", "f", "Η δασκάλα παρακαλεί να μη φορέσει το παιδί ρούχα με μεγάλα γράμματα ή σχέδια, γιατί στην ομαδική φωτογραφία ξεχωρίζουν πολύ. Επίσης, αν φοράει γυαλιά, να τα έχει μαζί του· ο φωτογράφος ξέρει πώς να αποφύγει τις αντανακλάσεις.", "The teacher asks that your child not wear clothes with big letters or designs, because they stand out a lot in the group photo. Also, if he wears glasses, he should have them with him; the photographer knows how to avoid reflections."),
  L("Γραμματέας", "f", "Οι φωτογραφίες δεν είναι υποχρεωτικές. Αν δεν θέλετε να φωτογραφηθεί το παιδί σας, στείλτε μας ένα σημείωμα ως την Τετάρτη. Τις φωτογραφίες θα τις δείτε πρώτα και θα αποφασίσετε μετά αν θα τις αγοράσετε.", "The photos aren't compulsory. If you don't want your child to be photographed, send us a note by Wednesday. You'll see the photos first and decide afterwards whether to buy them."),
 ],
 "questions": [
  Q("Πότε θα φωτογραφηθεί ο Άγγελος;", ["Πρώτος, το πρωί", "Μετά το πρώτο διάλειμμα", "Στο τέλος της μέρας", "Την Τετάρτη"], 1, "θα φωτογραφηθεί μετά το πρώτο διάλειμμα"),
  Q("Γιατί δεν πρέπει να φορέσει ρούχα με μεγάλα γράμματα ή σχέδια;", ["Γιατί το απαγορεύει ο κανονισμός", "Γιατί ξεχωρίζουν πολύ στην ομαδική φωτογραφία", "Γιατί θα φορέσουν όλοι στολή", "Γιατί λερώνονται εύκολα"], 1, "γιατί στην ομαδική φωτογραφία ξεχωρίζουν πολύ"),
  Q("Τι πρέπει να κάνουν οι γονείς που δεν θέλουν φωτογραφίες;", ["Να κρατήσουν το παιδί στο σπίτι", "Να τηλεφωνήσουν στον φωτογράφο", "Να στείλουν ένα σημείωμα ως την Τετάρτη", "Να μη πληρώσουν"], 2, "στείλτε μας ένα σημείωμα ως την Τετάρτη"),
 ],
 "gloss": {"γραμματεία": "γραμματεία — school office", "ατομικές": "ατομικός — individual", "ομαδικές": "ομαδικός — group", "φωτογραφηθεί": "φωτογραφίζομαι — to be photographed", "ξεχωρίζουν": "ξεχωρίζω — to stand out", "αντανακλάσεις": "αντανάκλαση — reflection", "υποχρεωτικές": "υποχρεωτικός — compulsory", "σημείωμα": "σημείωμα — note"},
})

ITEMS.append({
 "id": "l185-mon-nychia", "title": "Πώς σταμάτησα να τρώω τα νύχια μου", "title_en": "How I stopped biting my nails", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλά σε ένα podcast για μια συνήθεια που είχε από παιδί.",
 "script": [
  L("Δέσποινα", "f", "Έτρωγα τα νύχια μου από τότε που θυμάμαι τον εαυτό μου. Στις εξετάσεις, στα φανάρια, μπροστά στην τηλεόραση. Η μητέρα μου δοκίμασε τα πάντα, ακόμα και ένα πικρό βερνίκι, αλλά εγώ απλώς συνήθισα την πίκρα.", "I bit my nails for as long as I can remember. In exams, at traffic lights, in front of the TV. My mother tried everything, even a bitter nail varnish, but I just got used to the bitterness."),
  L("Δέσποινα", "f", "Στα τριάντα πέντε μου μια φίλη ψυχολόγος μού είπε κάτι που με βοήθησε: ότι δεν αρκεί να σταματήσεις μια συνήθεια, πρέπει να βάλεις κάτι άλλο στη θέση της. Αγόρασα ένα μικρό μπαλάκι από λάστιχο και το είχα πάντα στην τσέπη. Κάθε φορά που το χέρι μου πήγαινε στο στόμα, το έπιανα και το έσφιγγα.", "At thirty-five a psychologist friend told me something that helped: that it isn't enough to stop a habit, you have to put something else in its place. I bought a small rubber ball and always had it in my pocket. Every time my hand went to my mouth, I grabbed it and squeezed it."),
  L("Δέσποινα", "f", "Χρειάστηκαν σχεδόν τρεις μήνες. Το πιο δύσκολο ήταν να καταλάβω πότε το έκανα, γιατί το έκανα χωρίς να το σκέφτομαι. Σήμερα τα νύχια μου έχουν μεγαλώσει, και την πρώτη φορά που τα έβαψα, τα φωτογράφισα σαν να ήταν κάποιο βραβείο.", "It took almost three months. The hardest part was noticing when I did it, because I did it without thinking. Today my nails have grown, and the first time I painted them, I photographed them as if they were some prize."),
 ],
 "questions": [
  Q("Γιατί δεν βοήθησε το πικρό βερνίκι;", ["Γιατί έφευγε γρήγορα", "Γιατί η Δέσποινα συνήθισε την πίκρα", "Γιατί της έκανε αλλεργία", "Γιατί η μητέρα της σταμάτησε να το αγοράζει"], 1, "εγώ απλώς συνήθισα την πίκρα"),
  Q("Τι συμβουλή της έδωσε η φίλη της;", ["Να πάει σε γιατρό", "Να βάψει τα νύχια της", "Να βάλει κάτι άλλο στη θέση της συνήθειας", "Να φοράει γάντια"], 2, "πρέπει να βάλεις κάτι άλλο στη θέση της"),
  Q("Ποιο ήταν, κατά τη Δέσποινα, το πιο δύσκολο;", ["Να καταλάβει πότε το έκανε", "Να βρει χρόνο", "Να κρατήσει το μπαλάκι μαζί της", "Να το πει στους φίλους της"], 0, "Το πιο δύσκολο ήταν να καταλάβω πότε το έκανα"),
 ],
 "gloss": {"νύχια": "νύχι — nail", "βερνίκι": "βερνίκι — (nail) varnish", "πίκρα": "πίκρα — bitterness", "συνήθεια": "συνήθεια — habit", "έσφιγγα": "σφίγγω — to squeeze", "έβαψα": "βάφω — to paint"},
})

ITEMS.append({
 "id": "l185-dia-monos-sto-scholeio", "title": "Θα τον αφήσουμε να πηγαίνει μόνος στο σχολείο;", "title_en": "Shall we let him walk to school on his own?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο γονείς να συζητούν αν ο γιος τους μπορεί να πηγαίνει μόνος του στο σχολείο.",
 "script": [
  L("Μαρίνα", "f", "Ο Πέτρος μού ζήτησε πάλι να πηγαίνει μόνος του στο σχολείο. Λέει ότι όλοι οι φίλοι του πάνε μόνοι τους και ότι νιώθει μωρό.", "Petros asked me again if he can go to school on his own. He says all his friends go on their own and that he feels like a baby."),
  L("Κώστας", "m", "Είναι έντεκα χρονών και το σχολείο είναι δέκα λεπτά με τα πόδια. Το μόνο που με ανησυχεί είναι η διάβαση στη λεωφόρο. Εκεί τα αυτοκίνητα τρέχουν.", "He's eleven and the school is ten minutes' walk. The only thing that worries me is the crossing on the avenue. The cars go fast there."),
  L("Μαρίνα", "f", "Τότε ας κάνουμε μια δοκιμή. Την πρώτη εβδομάδα θα περπατάμε πίσω του, χωρίς να του μιλάμε, για να δούμε πώς περνάει τη λεωφόρο. Αν τα πάει καλά, από τη Δευτέρα πηγαίνει μόνος.", "Then let's do a trial. The first week we'll walk behind him without talking to him, to see how he crosses the avenue. If he does well, from Monday he goes alone."),
  L("Κώστας", "m", "Και να του πούμε να μας στέλνει ένα μήνυμα όταν φτάνει. Όχι για να τον ελέγχουμε, αλλά για να είμαστε κι εμείς ήσυχοι.", "And let's tell him to send us a message when he gets there. Not to check up on him, but so that we can be at ease too."),
  L("Μαρίνα", "f", "Συμφωνώ. Και κάτι ακόμα: θα πηγαίνει μαζί με τον Άρη από τον τρίτο. Δύο παιδιά μαζί προσέχουν περισσότερο.", "Agreed. And one more thing: he'll go together with Aris from the third floor. Two children together are more careful."),
 ],
 "questions": [
  Q("Τι ανησυχεί τον Κώστα;", ["Η απόσταση ως το σχολείο", "Η διάβαση στη λεωφόρο", "Ότι ο Πέτρος θα αργεί", "Ότι θα χάσει τα κλειδιά"], 1, "Το μόνο που με ανησυχεί είναι η διάβαση στη λεωφόρο"),
  Q("Τι θα κάνουν οι γονείς την πρώτη εβδομάδα;", ["Θα τον πηγαίνουν με το αυτοκίνητο", "Θα περπατούν πίσω του χωρίς να του μιλάνε", "Θα του τηλεφωνούν κάθε πέντε λεπτά", "Θα τον συνοδεύει η γιαγιά"], 1, "Την πρώτη εβδομάδα θα περπατάμε πίσω του, χωρίς να του μιλάμε"),
  Q("Γιατί θέλει η Μαρίνα να πηγαίνει μαζί με τον Άρη;", ["Γιατί ο Άρης ξέρει τον δρόμο", "Γιατί είναι μεγαλύτερος", "Γιατί δύο παιδιά μαζί προσέχουν περισσότερο", "Γιατί το ζήτησε η μητέρα του Άρη"], 2, "Δύο παιδιά μαζί προσέχουν περισσότερο"),
 ],
 "gloss": {"διάβαση": "διάβαση — (pedestrian) crossing", "λεωφόρο": "λεωφόρος — avenue", "δοκιμή": "δοκιμή — trial", "ελέγχουμε": "ελέγχω — to check up on", "ήσυχοι": "ήσυχος — at ease, calm"},
})

ITEMS.append({
 "id": "l185-news-patinia-pezodromia", "title": "Εκτός πεζοδρομίων τα ηλεκτρικά πατίνια", "title_en": "Electric scooters banned from pavements", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων σε τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Από την 1η του επόμενου μήνα, τα ηλεκτρικά πατίνια δεν θα επιτρέπεται να κυκλοφορούν στα πεζοδρόμια και στους πεζόδρομους της πόλης. Το δημοτικό συμβούλιο πήρε την απόφαση μετά από δεκάδες παράπονα κατοίκων, κυρίως ηλικιωμένων και γονιών με καρότσια.", "From the 1st of next month, electric scooters will not be allowed on the town's pavements and pedestrian streets. The town council took the decision after dozens of complaints from residents, mainly elderly people and parents with pushchairs."),
  L("Εκφωνήτρια", "f", "Οι χρήστες θα μπορούν να κινούνται στους ποδηλατόδρομους και στους δρόμους με όριο ταχύτητας τα τριάντα χιλιόμετρα. Τα πατίνια που νοικιάζονται μέσω εφαρμογής θα πρέπει να αφήνονται μόνο σε ειδικά σημαδεμένες θέσεις, και όχι στη μέση του πεζοδρομίου.", "Users will be able to ride on cycle lanes and on streets with a thirty-kilometre speed limit. Scooters rented through an app will have to be left only in specially marked spaces, not in the middle of the pavement."),
  L("Εκφωνήτρια", "f", "Το πρόστιμο για όσους δεν τηρούν τους κανόνες θα είναι πενήντα ευρώ. Η εταιρεία ενοικίασης δήλωσε ότι θα στείλει ειδοποίηση σε όλους τους χρήστες της και ότι θα χρεώνει επιπλέον όποιον αφήνει το πατίνι εκτός θέσης.", "The fine for those who don't follow the rules will be fifty euros. The rental company said it will send a notification to all its users and will charge extra to anyone who leaves the scooter outside a marked space."),
 ],
 "questions": [
  Q("Γιατί πήρε την απόφαση το δημοτικό συμβούλιο;", ["Μετά από ένα σοβαρό ατύχημα", "Μετά από δεκάδες παράπονα κατοίκων", "Γιατί το ζήτησε η αστυνομία", "Γιατί άλλαξε ο νόμος"], 1, "μετά από δεκάδες παράπονα κατοίκων"),
  Q("Πού θα μπορούν να κινούνται τα πατίνια;", ["Μόνο στους πεζόδρομους", "Στους ποδηλατόδρομους και σε δρόμους με όριο τα τριάντα χιλιόμετρα", "Σε όλους τους δρόμους", "Μόνο στην παραλιακή"], 1, "Οι χρήστες θα μπορούν να κινούνται στους ποδηλατόδρομους"),
  Q("Τι θα κάνει η εταιρεία ενοικίασης;", ["Θα κλείσει", "Θα μειώσει τις τιμές", "Θα χρεώνει επιπλέον όποιον αφήνει το πατίνι εκτός θέσης", "Θα βάλει δικούς της ελεγκτές"], 2, "θα χρεώνει επιπλέον όποιον αφήνει το πατίνι εκτός θέσης"),
 ],
 "gloss": {"πατίνια": "πατίνι — (electric) scooter", "πεζοδρόμια": "πεζοδρόμιο — pavement", "πεζόδρομους": "πεζόδρομος — pedestrian street", "παράπονα": "παράπονο — complaint", "καρότσια": "καρότσι — pushchair", "ποδηλατόδρομους": "ποδηλατόδρομος — cycle lane", "σημαδεμένες": "σημαδεμένος — marked", "τηρούν": "τηρώ — to observe, follow (rules)"},
})

ITEMS.append({
 "id": "l185-rep-antallagi-fyton", "title": "Ανταλλάσσουμε φυτά και μοσχεύματα", "title_en": "We swap plants and cuttings", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από μια γιορτή ανταλλαγής φυτών σε μια πλατεία της πόλης.",
 "script": [
  L("Ρεπόρτερ", "m", "Κάθε πρώτη Κυριακή του μήνα, η πλατεία της γειτονιάς γεμίζει γλάστρες, βάζα με νερό και κουτιά του γιαουρτιού γεμάτα χώμα. Εδώ κανείς δεν πουλάει και κανείς δεν αγοράζει· όλοι ανταλλάσσουν. Ένα μόσχευμα από βασιλικό για ένα κομμάτι από αλόη, ένα φυτό που μεγάλωσε πολύ για δύο μικρότερα.", "Every first Sunday of the month, the neighbourhood square fills with pots, jars of water and yoghurt pots full of soil. Here nobody sells and nobody buys; everyone swaps. A basil cutting for a piece of aloe, a plant that has grown too big for two smaller ones."),
  L("Ρεπόρτερ", "m", "Η ιδέα ήταν μιας συνταξιούχου βοτανολόγου, της κυρίας Ελπίδας. «Τα φυτά πολλαπλασιάζονται μόνα τους», μας λέει. «Αν κόψεις ένα κλαδάκι από ένα γεράνι και το βάλεις σε νερό, σε δύο εβδομάδες βγάζει ρίζες. Δεν έχει νόημα να αγοράζουμε ό,τι μπορούμε να μοιραστούμε.»", "The idea came from a retired botanist, Mrs Elpida. 'Plants multiply by themselves,' she tells us. 'If you cut a sprig from a geranium and put it in water, in two weeks it puts out roots. There's no point buying what we can share.'"),
  L("Ρεπόρτερ", "m", "Στο τραπέζι της, η κυρία Ελπίδα δίνει και συμβουλές: πόσο νερό θέλει ο κάκτος, πού να μπει η φτέρη, γιατί κιτρινίζουν τα φύλλα. Τα παιδιά παίρνουν δωρεάν ένα σπόρο φασολιού σε ένα βαμβάκι, για να τον δουν να φυτρώνει στο σπίτι.", "At her table, Mrs Elpida also gives advice: how much water the cactus needs, where to put the fern, why leaves turn yellow. The children get a bean seed on cotton wool for free, to watch it sprout at home."),
 ],
 "questions": [
  Q("Τι γίνεται στην πλατεία κάθε πρώτη Κυριακή του μήνα;", ["Μια λαϊκή αγορά με φυτά", "Μια ανταλλαγή φυτών χωρίς χρήματα", "Ένας διαγωνισμός κήπων", "Μαθήματα κηπουρικής"], 1, "Εδώ κανείς δεν πουλάει και κανείς δεν αγοράζει· όλοι ανταλλάσσουν"),
  Q("Τι λέει η κυρία Ελπίδα για το γεράνι;", ["Ότι χρειάζεται πολύ ήλιο", "Ότι ένα κλαδάκι του σε νερό βγάζει ρίζες σε δύο εβδομάδες", "Ότι δεν αντέχει το κρύο", "Ότι είναι το πιο φτηνό φυτό"], 1, "Αν κόψεις ένα κλαδάκι από ένα γεράνι και το βάλεις σε νερό, σε δύο εβδομάδες βγάζει ρίζες"),
  Q("Τι παίρνουν δωρεάν τα παιδιά;", ["Μια μικρή γλάστρα με λουλούδια", "Ένα βιβλίο για τα φυτά", "Ένα σπόρο φασολιού σε ένα βαμβάκι", "Ένα κουτί χώμα"], 2, "Τα παιδιά παίρνουν δωρεάν ένα σπόρο φασολιού σε ένα βαμβάκι"),
 ],
 "gloss": {"μόσχευμα": "μόσχευμα — cutting (of a plant)", "γλάστρες": "γλάστρα — flowerpot", "ανταλλάσσουν": "ανταλλάσσω — to swap, exchange", "βοτανολόγου": "βοτανολόγος — botanist", "πολλαπλασιάζονται": "πολλαπλασιάζομαι — to multiply", "κλαδάκι": "κλαδάκι — sprig, twig", "γεράνι": "γεράνι — geranium", "ρίζες": "ρίζα — root", "φτέρη": "φτέρη — fern", "κιτρινίζουν": "κιτρινίζω — to turn yellow", "φυτρώνει": "φυτρώνω — to sprout"},
})

ITEMS.append({
 "id": "l185-c1-pos-koimountai-ta-delfinia", "title": "Πώς κοιμούνται τα δελφίνια", "title_en": "How dolphins sleep", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια θαλάσσια βιολόγο σε μια εκπομπή για τη φύση.",
 "script": [
  L("Παρουσιαστής", "m", "Τα δελφίνια ζουν στο νερό αλλά αναπνέουν αέρα. Πώς κοιμούνται χωρίς να πνιγούν;", "Dolphins live in water but breathe air. How do they sleep without drowning?"),
  L("Βιολόγος", "f", "Η απάντηση είναι εντυπωσιακή: κοιμάται μόνο το μισό τους μυαλό τη φορά. Το ένα ημισφαίριο του εγκεφάλου περνά σε βαθύ ύπνο, ενώ το άλλο μένει ξύπνιο και φροντίζει να ανεβαίνει το ζώο στην επιφάνεια για να πάρει ανάσα. Στα δελφίνια, βλέπετε, η αναπνοή δεν είναι αυτόματη όπως σε εμάς· κάθε ανάσα είναι μια συνειδητή απόφαση.", "The answer is impressive: only half their brain sleeps at a time. One hemisphere of the brain goes into deep sleep while the other stays awake and makes sure the animal rises to the surface to take a breath. In dolphins, you see, breathing isn't automatic as it is in us; every breath is a conscious decision."),
  L("Παρουσιαστής", "m", "Και φαίνεται αυτό απ' έξω;", "And can you see that from the outside?"),
  L("Βιολόγος", "f", "Συχνά, ναι. Το μάτι που αντιστοιχεί στο ξύπνιο ημισφαίριο μένει συνήθως ανοιχτό, και πολλές φορές είναι στραμμένο προς τα άλλα μέλη της ομάδας. Μετά από λίγη ώρα τα ημισφαίρια αλλάζουν ρόλους. Έτσι το ζώο ξεκουράζεται, αλλά δεν χάνει ποτέ εντελώς την επαφή με το περιβάλλον του, κάτι πολύτιμο σε μια θάλασσα με θηρευτές.", "Often, yes. The eye linked to the awake hemisphere usually stays open, and is often turned towards the other members of the group. After a while the hemispheres swap roles. That way the animal rests, but never completely loses contact with its surroundings, which is precious in a sea with predators."),
  L("Παρουσιαστής", "m", "Μόνο τα δελφίνια το κάνουν αυτό;", "Is it only dolphins that do this?"),
  L("Βιολόγος", "f", "Όχι. Κάτι ανάλογο έχει παρατηρηθεί και σε φάλαινες, σε φώκιες, αλλά και σε πουλιά, όπως οι πάπιες, που κοιμούνται με το ένα μάτι ανοιχτό όταν βρίσκονται στην άκρη μιας ομάδας. Το πώς ακριβώς εξελίχθηκε αυτή η ικανότητα είναι ακόμα αντικείμενο έρευνας.", "No. Something similar has been observed in whales and seals, but also in birds, such as ducks, which sleep with one eye open when they are at the edge of a group. Exactly how this ability evolved is still a subject of research."),
 ],
 "questions": [
  Q("Πώς κοιμούνται τα δελφίνια, σύμφωνα με τη βιολόγο;", ["Στον βυθό, κρατώντας την ανάσα τους", "Με το ένα ημισφαίριο του εγκεφάλου τη φορά", "Μόνο για λίγα δευτερόλεπτα τη μέρα", "Επιπλέοντας χωρίς να αναπνέουν"], 1, "κοιμάται μόνο το μισό τους μυαλό τη φορά"),
  Q("Σε τι διαφέρει η αναπνοή των δελφινιών από τη δική μας;", ["Είναι πιο γρήγορη", "Γίνεται μόνο τη νύχτα", "Δεν είναι αυτόματη· κάθε ανάσα είναι συνειδητή απόφαση", "Γίνεται από το δέρμα"], 2, "κάθε ανάσα είναι μια συνειδητή απόφαση"),
  Q("Γιατί είναι πολύτιμος αυτός ο τρόπος ύπνου;", ["Γιατί το ζώο δεν χάνει ποτέ εντελώς την επαφή με το περιβάλλον του", "Γιατί καταναλώνει λιγότερη τροφή", "Γιατί μεγαλώνει πιο γρήγορα", "Γιατί ζεσταίνεται"], 0, "δεν χάνει ποτέ εντελώς την επαφή με το περιβάλλον του"),
 ],
 "gloss": {"πνιγούν": "πνίγομαι — to drown", "ημισφαίριο": "ημισφαίριο — hemisphere", "επιφάνεια": "επιφάνεια — surface", "ανάσα": "ανάσα — breath", "συνειδητή": "συνειδητός — conscious", "αντιστοιχεί": "αντιστοιχώ — to correspond", "στραμμένο": "στραμμένος — turned (towards)", "θηρευτές": "θηρευτής — predator", "εξελίχθηκε": "εξελίσσομαι — to evolve"},
})

ITEMS.append({
 "id": "l185-c1-giati-den-thymomaste-ta-prota-chronia", "title": "Γιατί δεν θυμόμαστε τα πρώτα μας χρόνια", "title_en": "Why we don't remember our first years", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια νευροψυχολόγο να μιλά σε μια ραδιοφωνική εκπομπή για τη μνήμη.",
 "script": [
  L("Νευροψυχολόγος", "f", "Οι περισσότεροι ενήλικες δεν έχουν σχεδόν καμία ανάμνηση από τα πρώτα τρία ή τέσσερα χρόνια της ζωής τους. Κι όμως, εκείνη την περίοδο μαθαίνουμε να περπατάμε, να μιλάμε, να αναγνωρίζουμε πρόσωπα. Το φαινόμενο ονομάζεται παιδική ή βρεφική αμνησία, και ήταν ήδη γνωστό στον Φρόιντ.", "Most adults have almost no memories from the first three or four years of their life. And yet, in that period we learn to walk, to talk, to recognise faces. The phenomenon is called childhood or infantile amnesia, and it was already known to Freud."),
  L("Νευροψυχολόγος", "f", "Δεν υπάρχει μία μόνο εξήγηση. Μια περιοχή του εγκεφάλου που παίζει κεντρικό ρόλο στη δημιουργία αναμνήσεων, ο ιππόκαμπος, ωριμάζει σταδιακά στα πρώτα χρόνια. Κάποιοι ερευνητές πιστεύουν ότι οι νέοι νευρώνες που σχηματίζονται τότε με πολύ γρήγορο ρυθμό ίσως «σβήνουν» τις παλιότερες συνδέσεις. Άλλοι τονίζουν τη γλώσσα: χωρίς λέξεις, είναι δύσκολο να οργανώσουμε μια εμπειρία σε ιστορία που μπορούμε να ανακαλέσουμε.", "There isn't just one explanation. An area of the brain that plays a central role in forming memories, the hippocampus, matures gradually in the first years. Some researchers believe that the new neurons formed at a very fast rate then may 'erase' older connections. Others stress language: without words, it's hard to organise an experience into a story we can recall."),
  L("Νευροψυχολόγος", "f", "Υπάρχει και μια παγίδα. Πολλές από τις «πρώτες αναμνήσεις» που νομίζουμε ότι έχουμε είναι στην πραγματικότητα ανασυνθέσεις, φτιαγμένες από φωτογραφίες και από ιστορίες που μας είπαν οι γονείς μας. Τις θυμόμαστε ζωντανά, αλλά δεν τις θυμόμαστε από την αρχή.", "There's also a trap. Many of the 'first memories' we think we have are in fact reconstructions, made from photographs and from stories our parents told us. We remember them vividly, but we don't remember them from the start."),
 ],
 "questions": [
  Q("Τι είναι η βρεφική αμνησία;", ["Μια ασθένεια των ηλικιωμένων", "Η απουσία σχεδόν κάθε ανάμνησης από τα πρώτα τρία ή τέσσερα χρόνια", "Η δυσκολία των παιδιών να μάθουν να μιλούν", "Η απώλεια μνήμης μετά από ατύχημα"], 1, "Οι περισσότεροι ενήλικες δεν έχουν σχεδόν καμία ανάμνηση από τα πρώτα τρία ή τέσσερα χρόνια"),
  Q("Ποια εξήγηση δίνουν όσοι τονίζουν τη γλώσσα;", ["Ότι τα παιδιά ξεχνούν τις λέξεις", "Ότι χωρίς λέξεις είναι δύσκολο να οργανώσουμε μια εμπειρία σε ιστορία", "Ότι οι γονείς δεν μιλούν αρκετά στα παιδιά", "Ότι η μητρική γλώσσα σβήνει τις αναμνήσεις"], 1, "χωρίς λέξεις, είναι δύσκολο να οργανώσουμε μια εμπειρία σε ιστορία"),
  Q("Τι είναι συχνά οι «πρώτες αναμνήσεις» μας;", ["Ακριβείς καταγραφές της πραγματικότητας", "Όνειρα", "Ανασυνθέσεις από φωτογραφίες και ιστορίες των γονιών", "Αναμνήσεις από την εφηβεία"], 2, "είναι στην πραγματικότητα ανασυνθέσεις, φτιαγμένες από φωτογραφίες"),
 ],
 "gloss": {"ανάμνηση": "ανάμνηση — memory", "αναγνωρίζουμε": "αναγνωρίζω — to recognise", "βρεφική αμνησία": "βρεφική αμνησία — infantile amnesia", "ιππόκαμπος": "ιππόκαμπος — hippocampus", "ωριμάζει": "ωριμάζω — to mature", "νευρώνες": "νευρώνας — neuron", "ανακαλέσουμε": "ανακαλώ — to recall", "παγίδα": "παγίδα — trap", "ανασυνθέσεις": "ανασύνθεση — reconstruction"},
})

rnd = random.Random(185)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-185.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
