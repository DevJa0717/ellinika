# Source for library/listening/listening-73.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l73.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l73-ann-askisi-tsounami", "title": "Άσκηση για τσουνάμι στην παραλία", "title_en": "A tsunami drill on the beach", "type": "announcement", "level": "B2",
 "context_el": "Κάνετε μπάνιο σε μια παραλία της Κρήτης. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα της Πολιτικής Προστασίας.",
 "script": [
  L("Εκφωνήτρια", "f", "Προσοχή, προσοχή. Αυτή είναι μια άσκηση. Επαναλαμβάνω: πρόκειται για άσκηση. Σε λίγα λεπτά θα ακουστεί σειρήνα και θα λάβετε στο κινητό σας μήνυμα από το 112 για πιθανό τσουνάμι.", "Attention, attention. This is a drill. I repeat: this is a drill. In a few minutes a siren will sound and you will receive a message from 112 on your mobile about a possible tsunami."),
  L("Εκφωνήτρια", "f", "Μόλις ακούσετε τη σειρήνα, βγείτε αμέσως από το νερό και απομακρυνθείτε από την ακτή. Ακολουθήστε τις πινακίδες με το πράσινο βέλος προς τον λόφο πίσω από το χωριό. Μην πάρετε το αυτοκίνητο· ο δρόμος πρέπει να μείνει ελεύθερος για τα οχήματα έκτακτης ανάγκης.", "As soon as you hear the siren, get out of the water immediately and move away from the shore. Follow the signs with the green arrow towards the hill behind the village. Don't take your car; the road must stay clear for emergency vehicles."),
  L("Εκφωνήτρια", "f", "Η άσκηση θα διαρκέσει περίπου μισή ώρα. Εθελοντές με κίτρινα γιλέκα θα βοηθήσουν τους ηλικιωμένους και τις οικογένειες με μικρά παιδιά. Σας ευχαριστούμε για τη συμμετοχή σας.", "The drill will last about half an hour. Volunteers in yellow vests will help elderly people and families with small children. Thank you for taking part."),
 ],
 "questions": [
  Q("Τι θα λάβουν οι λουόμενοι στο κινητό τους;", ["Μια φωτογραφία της παραλίας", "Μήνυμα από το 112 για πιθανό τσουνάμι", "Έναν χάρτη του χωριού", "Τηλεφώνημα από την αστυνομία"], 1, "θα λάβετε στο κινητό σας μήνυμα από το 112"),
  Q("Πού πρέπει να πάνε μόλις ακούσουν τη σειρήνα;", ["Στο λιμάνι", "Στον λόφο πίσω από το χωριό", "Στο πάρκινγκ", "Μέσα στο νερό"], 1, "προς τον λόφο πίσω από το χωριό"),
  Q("Γιατί δεν πρέπει να πάρουν το αυτοκίνητο;", ["Γιατί δεν υπάρχει βενζίνη", "Γιατί ο δρόμος πρέπει να μείνει ελεύθερος για τα οχήματα έκτακτης ανάγκης", "Γιατί η άσκηση γίνεται με τα πόδια", "Γιατί ο δρόμος είναι κλειστός για έργα"], 1, "ο δρόμος πρέπει να μείνει ελεύθερος για τα οχήματα έκτακτης ανάγκης"),
 ],
 "gloss": {"Πολιτικής Προστασίας": "Πολιτική Προστασία — Civil Protection", "άσκηση": "άσκηση — drill, exercise", "σειρήνα": "σειρήνα — siren", "τσουνάμι": "τσουνάμι — tsunami", "απομακρυνθείτε": "απομακρύνομαι — to move away", "ακτή": "ακτή — shore", "πινακίδες": "πινακίδα — sign", "έκτακτης ανάγκης": "έκτακτη ανάγκη — emergency", "γιλέκα": "γιλέκο — vest"},
})

ITEMS.append({
 "id": "l73-vm-tzaki", "title": "Καθάρισμα τζακιού πριν από τον χειμώνα", "title_en": "Sweeping the chimney before winter", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε ζητήσει να έρθει κάποιος να καθαρίσει το τζάκι σας. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τον τεχνικό.",
 "script": [
  L("Τεχνικός", "m", "Καλησπέρα, ο Μανώλης είμαι, για το τζάκι σας. Μπορώ να έρθω την Πέμπτη στις εννιά το πρωί. Η δουλειά κρατάει περίπου δύο ώρες, γιατί καθαρίζουμε όλη την καμινάδα μέχρι πάνω, όχι μόνο την εστία.", "Good evening, it's Manolis, about your fireplace. I can come on Thursday at nine in the morning. The job takes about two hours, because we clean the whole chimney right to the top, not just the hearth."),
  L("Τεχνικός", "m", "Σας παρακαλώ, μην ανάψετε φωτιά από την Τετάρτη το απόγευμα, για να είναι κρύο το τζάκι όταν φτάσω. Καλό θα ήταν επίσης να απομακρύνετε από κοντά χαλιά και έπιπλα, γιατί, όσο κι αν προσέχουμε, η καπνιά πάει παντού.", "Please don't light a fire from Wednesday afternoon, so that the fireplace is cold when I arrive. It would also be good to move rugs and furniture away from it, because however careful we are, the soot gets everywhere."),
  L("Τεχνικός", "m", "Πέρσι, αν θυμάστε, σας είχα πει ότι το καπάκι στην κορυφή της καμινάδας είχε σκουριάσει. Αν θέλετε να το αλλάξουμε, πείτε μου από πριν, να φέρω καινούργιο. Κοστίζει γύρω στα εξήντα ευρώ.", "Last year, if you remember, I told you that the cap at the top of the chimney had rusted. If you want us to replace it, tell me in advance so I can bring a new one. It costs around sixty euros."),
 ],
 "questions": [
  Q("Γιατί η δουλειά κρατάει δύο ώρες;", ["Γιατί ο τεχνικός δουλεύει μόνος", "Γιατί καθαρίζουν όλη την καμινάδα μέχρι πάνω", "Γιατί το τζάκι είναι πολύ μεγάλο", "Γιατί πρέπει να περιμένουν να κρυώσει"], 1, "καθαρίζουμε όλη την καμινάδα μέχρι πάνω"),
  Q("Τι ζητάει ο τεχνικός να μην κάνει ο πελάτης;", ["Να μην ανάψει φωτιά από την Τετάρτη το απόγευμα", "Να μη βρίσκεται στο σπίτι", "Να μην καθαρίσει το σαλόνι", "Να μην ανοίξει τα παράθυρα"], 0, "μην ανάψετε φωτιά από την Τετάρτη το απόγευμα"),
  Q("Τι πρόβλημα είχε βρει πέρσι;", ["Μια ρωγμή στην εστία", "Ότι το καπάκι της καμινάδας είχε σκουριάσει", "Μια φωλιά πουλιών", "Ότι η καμινάδα ήταν πολύ στενή"], 1, "το καπάκι στην κορυφή της καμινάδας είχε σκουριάσει"),
 ],
 "gloss": {"τζάκι": "τζάκι — fireplace", "καμινάδα": "καμινάδα — chimney", "εστία": "εστία — hearth", "ανάψετε": "ανάβω — to light", "απομακρύνετε": "απομακρύνω — to move (something) away", "καπνιά": "καπνιά — soot", "καπάκι": "καπάκι — cap, lid", "σκουριάσει": "σκουριάζω — to rust"},
})

ITEMS.append({
 "id": "l73-dia-kamera-eisodos", "title": "Κάμερα στην είσοδο της πολυκατοικίας;", "title_en": "A camera at the building entrance?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο ένοικοι μιας πολυκατοικίας συζητούν πριν από τη γενική συνέλευση για μια πρόταση του διαχειριστή.",
 "script": [
  L("Θανάσης", "m", "Είδες την πρόταση του διαχειριστή; Θέλει να βάλουμε κάμερα στην είσοδο, μετά τις δύο κλοπές ποδηλάτων. Εγώ θα ψηφίσω υπέρ.", "Did you see the manager's proposal? He wants us to put a camera at the entrance, after the two bike thefts. I'll vote in favour."),
  L("Μαρίνα", "f", "Εγώ έχω αμφιβολίες. Δεν μου αρέσει η ιδέα να καταγράφεται κάθε φορά που μπαίνω και βγαίνω, ποιος έρχεται να με δει, τι ώρα γυρίζω. Ποιος θα βλέπει αυτές τις εικόνες;", "I have doubts. I don't like the idea of being recorded every time I come in and go out, who comes to see me, what time I get home. Who will watch those images?"),
  L("Θανάσης", "m", "Κανείς, εκτός αν γίνει κάποιο περιστατικό. Ο διαχειριστής λέει ότι η εταιρεία κρατάει το υλικό μόνο για λίγες μέρες και μετά σβήνεται αυτόματα. Και η κάμερα θα δείχνει μόνο την είσοδο, όχι τον δρόμο.", "Nobody, unless there's an incident. The manager says the company keeps the footage only for a few days and then it's deleted automatically. And the camera will show only the entrance, not the street."),
  L("Μαρίνα", "f", "Αν είναι έτσι, ίσως. Αλλά προτιμώ να ξεκινήσουμε από κάτι πιο απλό: μια κλειδαριά στην πόρτα της αποθήκης, όπου είναι τα ποδήλατα. Οι κλέφτες μπήκαν από εκεί, όχι από την κεντρική είσοδο. Ας το προτείνουμε μαζί στη συνέλευση.", "If that's the case, maybe. But I'd rather we started with something simpler: a lock on the door of the storeroom where the bikes are. The thieves got in that way, not through the main entrance. Let's propose it together at the meeting."),
 ],
 "questions": [
  Q("Γιατί προτείνει ο διαχειριστής την κάμερα;", ["Λόγω θορύβου", "Μετά από δύο κλοπές ποδηλάτων", "Για να ελέγχει τους ενοίκους", "Γιατί το ζήτησε η αστυνομία"], 1, "μετά τις δύο κλοπές ποδηλάτων"),
  Q("Τι ανησυχεί τη Μαρίνα;", ["Το κόστος της κάμερας", "Ότι θα καταγράφεται κάθε φορά που μπαίνει και βγαίνει", "Ότι η κάμερα θα χαλάσει", "Ότι δεν θα δείχνει καθαρά"], 1, "Δεν μου αρέσει η ιδέα να καταγράφεται κάθε φορά που μπαίνω και βγαίνω"),
  Q("Τι προτείνει τελικά η Μαρίνα;", ["Να μπει φύλακας", "Να μπει κλειδαριά στην πόρτα της αποθήκης", "Να μπουν δύο κάμερες", "Να μη γίνει τίποτα"], 1, "μια κλειδαριά στην πόρτα της αποθήκης"),
 ],
 "gloss": {"ένοικοι": "ένοικος — resident", "διαχειριστή": "διαχειριστής — building manager", "κλοπές": "κλοπή — theft", "υπέρ": "υπέρ — in favour", "καταγράφεται": "καταγράφομαι — to be recorded", "περιστατικό": "περιστατικό — incident", "υλικό": "υλικό — footage, material", "σβήνεται": "σβήνομαι — to be deleted", "αποθήκης": "αποθήκη — storeroom"},
})

ITEMS.append({
 "id": "l73-dia-pazari-scholeiou", "title": "Το χριστουγεννιάτικο παζάρι του σχολείου", "title_en": "The school Christmas bazaar", "type": "dialogue", "level": "B2",
 "context_el": "Δύο μέλη του συλλόγου γονέων ενός δημοτικού σχολείου οργανώνουν ένα παζάρι.",
 "script": [
  L("Βίκυ", "f", "Λοιπόν, για το παζάρι: η διευθύντρια μάς δίνει το γυμναστήριο το Σάββατο πριν από τα Χριστούγεννα, από τις δέκα ως τις δύο. Τα έσοδα θα πάνε για τη βιβλιοθήκη του σχολείου.", "So, about the bazaar: the head teacher is giving us the gym on the Saturday before Christmas, from ten to two. The proceeds will go to the school library."),
  L("Κώστας", "m", "Ωραία. Πέρσι το πρόβλημα ήταν ότι οι μισοί γονείς έφεραν κουλουράκια και κανείς δεν έφερε τίποτα αλμυρό. Φέτος να φτιάξουμε έναν πίνακα, να γράφει ο καθένας τι θα φέρει.", "Great. Last year the problem was that half the parents brought biscuits and nobody brought anything savoury. This year let's make a list, so that everyone writes down what they'll bring."),
  L("Βίκυ", "f", "Συμφωνώ. Και σκεφτόμουν να φτιάξουν τα παιδιά στο μάθημα των εικαστικών στολίδια και κάρτες, να τα πουλήσουν τα ίδια. Τους αρέσει πολύ να κάνουν τους πωλητές.", "Agreed. And I was thinking the children could make decorations and cards in art class and sell them themselves. They love playing shopkeeper."),
  L("Κώστας", "m", "Τέλεια ιδέα. Μόνο να βάλουμε σταθερές, χαμηλές τιμές, ένα ή δύο ευρώ, για να μη χρειάζονται ρέστα και να μπορούν να αγοράσουν και τα ίδια τα παιδιά με το χαρτζιλίκι τους.", "Perfect idea. Only let's set fixed, low prices, one or two euros, so that no change is needed and the children themselves can buy with their pocket money."),
 ],
 "questions": [
  Q("Πού θα πάνε τα έσοδα του παζαριού;", ["Σε μια σχολική εκδρομή", "Στη βιβλιοθήκη του σχολείου", "Σε μια φιλανθρωπική οργάνωση", "Στο γυμναστήριο"], 1, "Τα έσοδα θα πάνε για τη βιβλιοθήκη του σχολείου"),
  Q("Ποιο ήταν το πρόβλημα πέρσι;", ["Δεν ήρθε κανείς", "Όλοι έφεραν γλυκά και κανείς αλμυρό", "Έβρεξε", "Τα πράγματα ήταν πολύ ακριβά"], 1, "οι μισοί γονείς έφεραν κουλουράκια και κανείς δεν έφερε τίποτα αλμυρό"),
  Q("Γιατί θέλει ο Κώστας σταθερές, χαμηλές τιμές;", ["Για να βγάλουν περισσότερα χρήματα", "Για να μη χρειάζονται ρέστα και να αγοράζουν και τα παιδιά", "Γιατί το ζήτησε η διευθύντρια", "Γιατί τα πράγματα είναι παλιά"], 1, "για να μη χρειάζονται ρέστα"),
 ],
 "gloss": {"συλλόγου γονέων": "σύλλογος γονέων — parents' association", "παζάρι": "παζάρι — bazaar, fair", "διευθύντρια": "διευθύντρια — head teacher (female)", "έσοδα": "έσοδα — proceeds, income", "αλμυρό": "αλμυρός — savoury, salty", "εικαστικών": "εικαστικά — art (school subject)", "στολίδια": "στολίδι — decoration", "ρέστα": "ρέστα — change (money)", "χαρτζιλίκι": "χαρτζιλίκι — pocket money"},
})

ITEMS.append({
 "id": "l73-int-sideras", "title": "Μια νεαρή σιδεράς", "title_en": "A young blacksmith", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη σε ραδιοφωνική εκπομπή με μια νέα γυναίκα που δουλεύει ως σιδεράς σε ένα χωριό της Ηπείρου.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Γκόγκου, δεν είναι συνηθισμένο να βλέπει κανείς μια γυναίκα μπροστά σε ένα αμόνι. Πώς ξεκινήσατε;", "Ms Gkogkou, it's not usual to see a woman in front of an anvil. How did you start?"),
  L("Ρούλα", "f", "Το εργαστήριο ήταν του παππού μου. Όταν πέθανε, έμεινε κλειστό για χρόνια. Εγώ σπούδαζα γραφιστική στην Αθήνα, αλλά κάθε καλοκαίρι που ερχόμουν στο χωριό, άνοιγα την πόρτα και κοίταζα τα εργαλεία του. Μια μέρα αποφάσισα να μάθω να τα χρησιμοποιώ.", "The workshop was my grandfather's. When he died, it stayed closed for years. I was studying graphic design in Athens, but every summer when I came to the village, I would open the door and look at his tools. One day I decided to learn how to use them."),
  L("Δημοσιογράφος", "m", "Ποιος σας έμαθε;", "Who taught you?"),
  L("Ρούλα", "f", "Ένας ηλικιωμένος σιδεράς από το διπλανό χωριό, φίλος του παππού. Στην αρχή γελούσε· έλεγε ότι δεν θα αντέξω ούτε μια βδομάδα. Η δουλειά είναι βαριά, αλλά δεν είναι μόνο θέμα δύναμης. Είναι θέμα τεχνικής: να ξέρεις πότε το σίδερο είναι έτοιμο, από το χρώμα του.", "An elderly blacksmith from the next village, a friend of my grandfather's. At first he laughed; he said I wouldn't last a week. The work is heavy, but it's not only a matter of strength. It's a matter of technique: knowing when the iron is ready, from its colour."),
  L("Δημοσιογράφος", "m", "Τι φτιάχνετε σήμερα;", "What do you make today?"),
  L("Ρούλα", "f", "Πεταλώνω ακόμη άλογα και μουλάρια, γιατί στα χωριά τα χρειάζονται. Αλλά φτιάχνω και κάγκελα, φωτιστικά και μαχαίρια κουζίνας, που τα πουλάω μέσω διαδικτύου. Εκεί βοηθάει η γραφιστική: τα σχέδια είναι δικά μου.", "I still shoe horses and mules, because the villages need them. But I also make railings, lamps and kitchen knives, which I sell online. That's where graphic design helps: the designs are my own."),
 ],
 "questions": [
  Q("Τι σπούδαζε η Ρούλα στην Αθήνα;", ["Αρχιτεκτονική", "Γραφιστική", "Μηχανολογία", "Καλές τέχνες"], 1, "Εγώ σπούδαζα γραφιστική στην Αθήνα"),
  Q("Τι πίστευε στην αρχή ο ηλικιωμένος σιδεράς;", ["Ότι θα γίνει καλύτερη από τον παππού της", "Ότι δεν θα αντέξει ούτε μια βδομάδα", "Ότι πρέπει να ανοίξει μαγαζί στην Αθήνα", "Ότι η δουλειά είναι εύκολη"], 1, "έλεγε ότι δεν θα αντέξω ούτε μια βδομάδα"),
  Q("Πώς τη βοηθάει σήμερα η γραφιστική;", ["Στο πετάλωμα των αλόγων", "Στα σχέδια των αντικειμένων που πουλάει", "Στη λογιστική", "Στο να βρίσκει σίδερο"], 1, "Εκεί βοηθάει η γραφιστική: τα σχέδια είναι δικά μου"),
 ],
 "gloss": {"σιδεράς": "σιδεράς — blacksmith", "αμόνι": "αμόνι — anvil", "εργαστήριο": "εργαστήριο — workshop", "γραφιστική": "γραφιστική — graphic design", "αντέξω": "αντέχω — to last, endure", "σίδερο": "σίδερο — iron", "Πεταλώνω": "πεταλώνω — to shoe (a horse)", "μουλάρια": "μουλάρι — mule", "φωτιστικά": "φωτιστικό — lamp"},
})

ITEMS.append({
 "id": "l73-rep-krina-ammou", "title": "Τα κρίνα της άμμου", "title_en": "The sea daffodils", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από ραδιοφωνική εκπομπή για τη φύση.",
 "script": [
  L("Ρεπόρτερ", "f", "Στα τέλη του καλοκαιριού, σε πολλές αμμουδιές της Ελλάδας, ανθίζει ένα λευκό λουλούδι με έντονο άρωμα: ο κρίνος της θάλασσας ή, όπως τον λένε αλλού, το κρίνο της άμμου. Φυτρώνει μέσα στην άμμο, εκεί όπου λίγα φυτά καταφέρνουν να ζήσουν.", "At the end of summer, on many sandy beaches in Greece, a white flower with a strong scent blooms: the sea daffodil or, as it is called elsewhere, the sand lily. It grows in the sand, where few plants manage to live."),
  L("Ρεπόρτερ", "f", "Τα άνθη του ανοίγουν κυρίως το βράδυ, και τα επισκέπτονται νυχτερινές πεταλούδες, που μεταφέρουν τη γύρη από λουλούδι σε λουλούδι. Οι βολβοί του βρίσκονται βαθιά μέσα στην άμμο, και έτσι αντέχουν τη ζέστη και την ξηρασία.", "Its flowers open mainly in the evening, and they are visited by moths, which carry the pollen from flower to flower. Its bulbs lie deep in the sand, and so they withstand heat and drought."),
  L("Ρεπόρτερ", "f", "Τα τελευταία χρόνια, όμως, ο κρίνος της θάλασσας χάνεται από πολλές παραλίες. Οι ξαπλώστρες, τα μηχανήματα που καθαρίζουν την άμμο και το ποδοπάτημα καταστρέφουν τα φυτά. Περιβαλλοντικές ομάδες ζητούν από τους λουόμενους να μην κόβουν τα λουλούδια και να μην απλώνουν τις πετσέτες τους πάνω τους.", "In recent years, however, the sea daffodil has been disappearing from many beaches. Sunbeds, the machines that clean the sand and trampling destroy the plants. Environmental groups ask bathers not to pick the flowers and not to spread their towels on them."),
 ],
 "questions": [
  Q("Πότε ανθίζει ο κρίνος της θάλασσας;", ["Την άνοιξη", "Στα τέλη του καλοκαιριού", "Τον χειμώνα", "Όλο τον χρόνο"], 1, "Στα τέλη του καλοκαιριού"),
  Q("Ποιοι επισκέπτονται τα άνθη του;", ["Μέλισσες το μεσημέρι", "Νυχτερινές πεταλούδες", "Γλάροι", "Μυρμήγκια"], 1, "τα επισκέπτονται νυχτερινές πεταλούδες"),
  Q("Τι ζητούν οι περιβαλλοντικές ομάδες από τους λουόμενους;", ["Να φυτεύουν κρίνους", "Να μην κόβουν τα λουλούδια και να μην απλώνουν πετσέτες πάνω τους", "Να μην πηγαίνουν στην παραλία", "Να μαζεύουν τους βολβούς"], 1, "να μην κόβουν τα λουλούδια και να μην απλώνουν τις πετσέτες τους πάνω τους"),
 ],
 "gloss": {"αμμουδιές": "αμμουδιά — sandy beach", "ανθίζει": "ανθίζω — to bloom", "άρωμα": "άρωμα — scent", "κρίνος": "κρίνος (or το κρίνο) — lily", "άνθη": "άνθος — flower, bloom", "νυχτερινές πεταλούδες": "νυχτερινή πεταλούδα — moth", "γύρη": "γύρη — pollen", "βολβοί": "βολβός — bulb", "ξηρασία": "ξηρασία — drought", "ποδοπάτημα": "ποδοπάτημα — trampling", "λουόμενους": "λουόμενος — bather"},
})

ITEMS.append({
 "id": "l73-mono-kinezika", "title": "Κινέζικα στα πενήντα", "title_en": "Chinese at fifty", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλά σε μια εκδήλωση ενός κέντρου ξένων γλωσσών.",
 "script": [
  L("Αντώνης", "m", "Άρχισα να μαθαίνω κινέζικα στα πενήντα δύο μου. Όλοι με ρωτούσαν γιατί. Η αλήθεια είναι ότι η εταιρεία μου είχε αρχίσει να συνεργάζεται με έναν προμηθευτή από τη Σαγκάη, και ντρεπόμουν που δεν μπορούσα να πω ούτε «ευχαριστώ» στους συνεργάτες μου.", "I started learning Chinese at fifty-two. Everyone asked me why. The truth is that my company had started working with a supplier from Shanghai, and I was embarrassed that I couldn't even say 'thank you' to my colleagues."),
  L("Αντώνης", "m", "Το πιο δύσκολο δεν ήταν οι χαρακτήρες, όπως νόμιζα, αλλά οι τόνοι. Στα κινέζικα η ίδια συλλαβή, με διαφορετικό τόνο, σημαίνει εντελώς άλλο πράγμα. Τους πρώτους μήνες ζήτησα από τη δασκάλα μου «μητέρα» και της είπα «άλογο».", "The hardest thing wasn't the characters, as I'd thought, but the tones. In Chinese the same syllable, with a different tone, means something completely different. In the first months I meant to say 'mother' to my teacher and said 'horse'."),
  L("Αντώνης", "m", "Μελετάω είκοσι λεπτά κάθε πρωί, πριν από τη δουλειά, και ακούω κινέζικα podcast στο αυτοκίνητο. Πέρσι πήγα στη Σαγκάη και μπόρεσα να παραγγείλω μόνος μου σε εστιατόριο. Οι σερβιτόροι χειροκρότησαν. Δεν θα γίνω ποτέ άπταιστος, αλλά δεν είναι αυτός ο στόχος. Ο στόχος είναι να μη σταματήσω να μαθαίνω.", "I study twenty minutes every morning before work, and I listen to Chinese podcasts in the car. Last year I went to Shanghai and managed to order by myself in a restaurant. The waiters applauded. I'll never be fluent, but that isn't the goal. The goal is not to stop learning."),
 ],
 "questions": [
  Q("Γιατί άρχισε να μαθαίνει κινέζικα ο Αντώνης;", ["Γιατί μετακόμισε στην Κίνα", "Γιατί η εταιρεία του συνεργαζόταν με έναν προμηθευτή από τη Σαγκάη", "Γιατί η γυναίκα του είναι Κινέζα", "Για να γίνει μεταφραστής"], 1, "η εταιρεία μου είχε αρχίσει να συνεργάζεται με έναν προμηθευτή από τη Σαγκάη"),
  Q("Τι βρήκε πιο δύσκολο;", ["Τους χαρακτήρες", "Τους τόνους", "Τη γραμματική", "Το λεξιλόγιο"], 1, "Το πιο δύσκολο δεν ήταν οι χαρακτήρες, όπως νόμιζα, αλλά οι τόνοι"),
  Q("Ποιος είναι ο στόχος του;", ["Να γίνει άπταιστος", "Να περάσει εξετάσεις", "Να μη σταματήσει να μαθαίνει", "Να μετακομίσει στη Σαγκάη"], 2, "Ο στόχος είναι να μη σταματήσω να μαθαίνω"),
 ],
 "gloss": {"κινέζικα": "κινέζικα — Chinese (language)", "προμηθευτή": "προμηθευτής — supplier", "συνεργάτες": "συνεργάτης — colleague, partner", "χαρακτήρες": "χαρακτήρας — character (in writing)", "τόνοι": "τόνος — tone", "συλλαβή": "συλλαβή — syllable", "χειροκρότησαν": "χειροκροτώ — to applaud", "άπταιστος": "άπταιστος — fluent, flawless"},
})

ITEMS.append({
 "id": "l73-mono-gamos-dimarcheio", "title": "Παντρευτήκαμε στο δημαρχείο", "title_en": "We got married at the town hall", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια νεαρή γυναίκα να μιλά σε ένα podcast για τον γάμο της.",
 "script": [
  L("Χαρά", "f", "Όταν ανακοινώσαμε ότι θα παντρευτούμε στο δημαρχείο, με δεκαπέντε καλεσμένους, η γιαγιά μου στενοχωρήθηκε πολύ. Περίμενε εκκλησία, νυφικό με ουρά και τριακόσια άτομα στο τραπέζι. Ο πολιτικός γάμος ισχύει στην Ελλάδα από το 1982, αλλά για τη γενιά της παραμένει κάτι «μισό».", "When we announced that we would marry at the town hall, with fifteen guests, my grandmother was very upset. She expected a church, a wedding dress with a train and three hundred people at the table. Civil marriage has been valid in Greece since 1982, but for her generation it remains something 'half-done'."),
  L("Χαρά", "f", "Οι λόγοι μας ήταν δύο. Ο ένας ήταν οικονομικός: με τα χρήματα που θα ξοδεύαμε σε μια βραδιά, δώσαμε την προκαταβολή για το διαμέρισμά μας. Ο άλλος ήταν ότι κανείς από τους δύο δεν είναι θρησκευόμενος, και δεν θέλαμε να κάνουμε κάτι μόνο για τα μάτια του κόσμου.", "We had two reasons. One was financial: with the money we would have spent on one evening, we paid the deposit on our flat. The other was that neither of us is religious, and we didn't want to do something just for appearances."),
  L("Χαρά", "f", "Η τελετή κράτησε δέκα λεπτά. Μετά πήγαμε όλοι σε μια ταβέρνα δίπλα στη θάλασσα. Και ξέρετε ποια χόρευε πρώτη και τελευταία έφυγε; Η γιαγιά μου. Στο τέλος μού ψιθύρισε: «Καλύτερα έτσι, παιδί μου. Στον δικό μου γάμο δεν γνώριζα ούτε τους μισούς.»", "The ceremony lasted ten minutes. Afterwards we all went to a taverna by the sea. And do you know who was first to dance and last to leave? My grandmother. At the end she whispered to me: 'Better this way, my child. At my own wedding I didn't know even half of them.'"),
 ],
 "questions": [
  Q("Γιατί στενοχωρήθηκε η γιαγιά της Χαράς;", ["Γιατί δεν της άρεσε ο γαμπρός", "Γιατί περίμενε γάμο σε εκκλησία με πολλούς καλεσμένους", "Γιατί δεν την κάλεσαν", "Γιατί ο γάμος έγινε στο εξωτερικό"], 1, "Περίμενε εκκλησία, νυφικό με ουρά και τριακόσια άτομα στο τραπέζι"),
  Q("Τι έκαναν με τα χρήματα που δεν ξόδεψαν στον γάμο;", ["Πήγαν ταξίδι", "Έδωσαν την προκαταβολή για το διαμέρισμά τους", "Τα έδωσαν σε φιλανθρωπία", "Αγόρασαν αυτοκίνητο"], 1, "δώσαμε την προκαταβολή για το διαμέρισμά μας"),
  Q("Πώς αντέδρασε τελικά η γιαγιά;", ["Δεν ήρθε στη γιορτή", "Χόρεψε πρώτη, έφυγε τελευταία και είπε «Καλύτερα έτσι»", "Έφυγε νωρίς", "Ζήτησε να γίνει και θρησκευτικός γάμος"], 1, "Καλύτερα έτσι, παιδί μου"),
 ],
 "gloss": {"δημαρχείο": "δημαρχείο — town hall", "καλεσμένους": "καλεσμένος — guest", "νυφικό": "νυφικό — wedding dress", "ουρά": "ουρά — train (of a dress)", "πολιτικός γάμος": "πολιτικός γάμος — civil marriage", "προκαταβολή": "προκαταβολή — deposit", "θρησκευόμενος": "θρησκευόμενος — religious (person)", "τελετή": "τελετή — ceremony", "ψιθύρισε": "ψιθυρίζω — to whisper"},
})

ITEMS.append({
 "id": "l73-c1-syndromo-apateona", "title": "Το σύνδρομο του απατεώνα", "title_en": "Impostor syndrome", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια ψυχολόγο σε εκπομπή του ραδιοφώνου για την εργασία.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Νικολαΐδου, τι εννοούμε όταν μιλάμε για «σύνδρομο του απατεώνα»;", "Ms Nikolaidou, what do we mean when we talk about 'impostor syndrome'?"),
  L("Ψυχολόγος", "f", "Περιγράφουμε ανθρώπους που, παρά τις αντικειμενικές επιτυχίες τους, είναι πεπεισμένοι ότι δεν τις αξίζουν. Αποδίδουν ό,τι πετυχαίνουν στην τύχη, στις γνωριμίες ή σε ένα λάθος των άλλων, και ζουν με τον μόνιμο φόβο ότι κάποια μέρα θα «αποκαλυφθούν». Να διευκρινίσω ότι δεν πρόκειται για κλινική διάγνωση, αλλά για ένα μοτίβο σκέψης.", "We are describing people who, despite their objective successes, are convinced that they don't deserve them. They attribute whatever they achieve to luck, to connections or to other people's mistake, and they live in constant fear that some day they will be 'found out'. I should clarify that it is not a clinical diagnosis, but a pattern of thinking."),
  L("Δημοσιογράφος", "m", "Από πού προέρχεται ο όρος;", "Where does the term come from?"),
  L("Ψυχολόγος", "f", "Τον εισήγαγαν δύο Αμερικανίδες ψυχολόγοι στα τέλη της δεκαετίας του 1970, μελετώντας γυναίκες με εξαιρετικές επιδόσεις στην εκπαίδευση και στην καριέρα. Σήμερα ξέρουμε ότι το φαινόμενο αφορά και τα δύο φύλα, και ότι είναι ιδιαίτερα συχνό σε όσους είναι οι πρώτοι της οικογένειάς τους που σπουδάζουν ή σε όσους ανήκουν σε μια μειοψηφία μέσα στον χώρο εργασίας τους.", "It was introduced by two American psychologists in the late 1970s, while studying women with outstanding achievements in education and careers. Today we know that the phenomenon affects both sexes, and that it is especially common among those who are the first in their family to go to university or who belong to a minority in their workplace."),
  L("Δημοσιογράφος", "m", "Υπάρχει κάτι θετικό σε αυτή την ανασφάλεια;", "Is there anything positive about this insecurity?"),
  L("Ψυχολόγος", "f", "Σε μικρές δόσεις, μια υγιής αμφιβολία μάς κρατά σε εγρήγορση και μας κάνει να προετοιμαζόμαστε. Το πρόβλημα αρχίζει όταν οδηγεί σε εξάντληση από την υπερπροσπάθεια ή όταν μας κάνει να αρνούμαστε ευκαιρίες. Το πρώτο βήμα είναι να το ονομάσουμε· το δεύτερο, να μιλήσουμε γι’ αυτό. Οι περισσότεροι ανακαλύπτουν με έκπληξη ότι οι συνάδελφοι που θαυμάζουν νιώθουν ακριβώς το ίδιο.", "In small doses, a healthy doubt keeps us alert and makes us prepare. The problem begins when it leads to exhaustion from overwork or when it makes us turn down opportunities. The first step is to name it; the second, to talk about it. Most people discover with surprise that the colleagues they admire feel exactly the same."),
 ],
 "questions": [
  Q("Σε τι αποδίδουν τις επιτυχίες τους όσοι έχουν το σύνδρομο;", ["Στην εξυπνάδα τους", "Στην τύχη, στις γνωριμίες ή σε λάθος των άλλων", "Στη σκληρή δουλειά", "Στους γονείς τους"], 1, "Αποδίδουν ό,τι πετυχαίνουν στην τύχη, στις γνωριμίες ή σε ένα λάθος των άλλων"),
  Q("Τι διευκρινίζει η ψυχολόγος;", ["Ότι είναι σοβαρή ψυχική ασθένεια", "Ότι δεν πρόκειται για κλινική διάγνωση, αλλά για μοτίβο σκέψης", "Ότι αφορά μόνο γυναίκες", "Ότι θεραπεύεται με φάρμακα"], 1, "δεν πρόκειται για κλινική διάγνωση, αλλά για ένα μοτίβο σκέψης"),
  Q("Σε ποιους είναι ιδιαίτερα συχνό το φαινόμενο;", ["Στους ηλικιωμένους", "Σε όσους είναι οι πρώτοι της οικογένειάς τους που σπουδάζουν", "Στους καλλιτέχνες", "Στους ανέργους"], 1, "σε όσους είναι οι πρώτοι της οικογένειάς τους που σπουδάζουν"),
  Q("Ποιο είναι, κατά την ψυχολόγο, το πρώτο βήμα;", ["Να αλλάξουμε δουλειά", "Να το ονομάσουμε", "Να δουλέψουμε περισσότερο", "Να το κρατήσουμε κρυφό"], 1, "Το πρώτο βήμα είναι να το ονομάσουμε"),
 ],
 "gloss": {"απατεώνα": "απατεώνας — impostor, fraud", "πεπεισμένοι": "πεπεισμένος — convinced", "Αποδίδουν": "αποδίδω — to attribute", "γνωριμίες": "γνωριμία — connection, acquaintance", "αποκαλυφθούν": "αποκαλύπτομαι — to be exposed, found out", "διευκρινίσω": "διευκρινίζω — to clarify", "μοτίβο": "μοτίβο — pattern", "μειοψηφία": "μειοψηφία — minority", "εγρήγορση": "εγρήγορση — alertness", "εξάντληση": "εξάντληση — exhaustion"},
})

ITEMS.append({
 "id": "l73-c1-dimopsifisma-1974", "title": "Το δημοψήφισμα του 1974", "title_en": "The 1974 referendum", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε απόσπασμα από μια διάλεξη για την ιστορία της Μεταπολίτευσης.",
 "script": [
  L("Ιστορικός", "m", "Στις 8 Δεκεμβρίου 1974, λίγους μήνες μετά την πτώση της δικτατορίας, οι Έλληνες κλήθηκαν να αποφασίσουν σε δημοψήφισμα αν θέλουν βασιλευόμενη ή αβασίλευτη δημοκρατία. Περίπου επτά στους δέκα ψήφισαν υπέρ της αβασίλευτης, και η μοναρχία καταργήθηκε οριστικά.", "On 8 December 1974, a few months after the fall of the dictatorship, Greeks were called to decide in a referendum whether they wanted a crowned or an uncrowned democracy, that is, a monarchy or a republic. About seven in ten voted for the republic, and the monarchy was abolished for good."),
  L("Ιστορικός", "m", "Το ζήτημα του πολιτεύματος δίχαζε την ελληνική κοινωνία για μισό αιώνα. Η μοναρχία είχε καταργηθεί και επαναφερθεί αρκετές φορές, συχνά μέσα από δημοψηφίσματα των οποίων η εγκυρότητα ήταν, το λιγότερο, αμφίβολη. Πολλοί θεωρούσαν ότι το παλάτι είχε ευθύνη για την πολιτική αστάθεια που οδήγησε στη δικτατορία του 1967.", "The question of the form of government had divided Greek society for half a century. The monarchy had been abolished and restored several times, often through referendums whose validity was, to say the least, doubtful. Many believed that the palace bore responsibility for the political instability that led to the dictatorship of 1967."),
  L("Ιστορικός", "m", "Αξίζει να σημειωθεί η στάση του τότε πρωθυπουργού, Κωνσταντίνου Καραμανλή. Αν και προερχόταν από τον συντηρητικό χώρο, δεν πήρε δημόσια θέση υπέρ του θρόνου και άφησε την απόφαση στον λαό. Η επιλογή αυτή ενίσχυσε το κύρος του αποτελέσματος.", "The stance of the then prime minister, Konstantinos Karamanlis, is worth noting. Although he came from the conservative camp, he took no public position in favour of the throne and left the decision to the people. This choice strengthened the authority of the result."),
  L("Ιστορικός", "m", "Το δημοψήφισμα του 1974 θεωρείται από πολλούς το πρώτο απολύτως ελεύθερο δημοψήφισμα στην ιστορία του ελληνικού κράτους. Έκλεισε ένα από τα πιο διχαστικά κεφάλαια της νεότερης ιστορίας και άνοιξε τον δρόμο για το Σύνταγμα του 1975, που ισχύει, με αναθεωρήσεις, μέχρι σήμερα.", "The 1974 referendum is considered by many to be the first completely free referendum in the history of the Greek state. It closed one of the most divisive chapters of modern history and opened the way for the Constitution of 1975, which, with revisions, is still in force today."),
 ],
 "questions": [
  Q("Τι αποφάσισαν οι Έλληνες στο δημοψήφισμα του 1974;", ["Την επιστροφή του βασιλιά", "Την κατάργηση της μοναρχίας", "Την ένταξη στην ΕΟΚ", "Νέες εκλογές"], 1, "η μοναρχία καταργήθηκε οριστικά"),
  Q("Τι ισχύει για τα προηγούμενα δημοψηφίσματα για το πολίτευμα;", ["Ήταν όλα απολύτως ελεύθερα", "Η εγκυρότητά τους ήταν συχνά αμφίβολη", "Δεν έγιναν ποτέ", "Τα κέρδισαν πάντα οι δημοκρατικοί"], 1, "δημοψηφίσματα των οποίων η εγκυρότητα ήταν, το λιγότερο, αμφίβολη"),
  Q("Ποια ήταν η στάση του Καραμανλή;", ["Υποστήριξε δημόσια τον θρόνο", "Δεν πήρε δημόσια θέση υπέρ του θρόνου και άφησε την απόφαση στον λαό", "Πρότεινε να αναβληθεί το δημοψήφισμα", "Παραιτήθηκε"], 1, "δεν πήρε δημόσια θέση υπέρ του θρόνου και άφησε την απόφαση στον λαό"),
  Q("Πώς χαρακτηρίζεται σήμερα από πολλούς το δημοψήφισμα του 1974;", ["Ως το πρώτο απολύτως ελεύθερο δημοψήφισμα του ελληνικού κράτους", "Ως ένα ακόμη αμφίβολο δημοψήφισμα", "Ως αποτυχία", "Ως το τελευταίο δημοψήφισμα στην Ελλάδα"], 0, "το πρώτο απολύτως ελεύθερο δημοψήφισμα στην ιστορία του ελληνικού κράτους"),
 ],
 "gloss": {"Μεταπολίτευσης": "Μεταπολίτευση — the transition to democracy after 1974", "δικτατορίας": "δικτατορία — dictatorship", "δημοψήφισμα": "δημοψήφισμα — referendum", "βασιλευόμενη": "βασιλευόμενη δημοκρατία — constitutional monarchy", "αβασίλευτη": "αβασίλευτη δημοκρατία — republic", "πολιτεύματος": "πολίτευμα — form of government", "δίχαζε": "διχάζω — to divide", "εγκυρότητα": "εγκυρότητα — validity", "κύρος": "κύρος — authority, prestige", "διχαστικά": "διχαστικός — divisive", "αναθεωρήσεις": "αναθεώρηση — revision"},
})

rnd = random.Random(73)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-73.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
