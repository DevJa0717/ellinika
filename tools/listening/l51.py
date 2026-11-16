# Source for library/listening/listening-51.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l51.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l51-ann-ilektrikos", "title": "Βλάβη στη γραμμή του ηλεκτρικού", "title_en": "A fault on the electric railway line", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε έναν σταθμό του ηλεκτρικού σιδηροδρόμου στην Αθήνα. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Ανακοίνωση", "f", "Αγαπητοί επιβάτες, λόγω τεχνικής βλάβης στη γραμμή ανάμεσα στους σταθμούς Φάληρο και Μοσχάτο, οι συρμοί κινούνται με μεγάλες καθυστερήσεις. Τα δρομολόγια από τον Πειραιά προς την Κηφισιά πραγματοποιούνται μόνο από τον σταθμό Μοσχάτο και μετά.", "Dear passengers, due to a technical fault on the line between Faliro and Moschato stations, trains are running with long delays. Services from Piraeus to Kifisia are running only from Moschato station onwards."),
  L("Ανακοίνωση", "f", "Για την εξυπηρέτηση του επιβατικού κοινού, έχουν διατεθεί λεωφορεία που εκτελούν τη διαδρομή Πειραιάς – Φάληρο – Μοσχάτο. Τα λεωφορεία αναχωρούν από την έξοδο του σταθμού, στην πλευρά του λιμανιού, κάθε δέκα λεπτά. Το εισιτήριό σας ισχύει κανονικά και για αυτά.", "To serve the travelling public, buses have been provided on the route Piraeus – Faliro – Moschato. The buses leave from the station exit, on the port side, every ten minutes. Your ticket is also valid for them."),
  L("Ανακοίνωση", "f", "Τα συνεργεία εργάζονται για την αποκατάσταση της βλάβης, η οποία αναμένεται να ολοκληρωθεί μέχρι τις έξι το απόγευμα. Επιβάτες που ταξιδεύουν προς το κέντρο μπορούν εναλλακτικά να χρησιμοποιήσουν το τραμ. Ζητούμε συγγνώμη για την ταλαιπωρία.", "Crews are working to repair the fault, which is expected to be completed by six in the evening. Passengers travelling to the centre can alternatively use the tram. We apologise for the inconvenience."),
 ],
 "questions": [
  Q("Πού βρίσκεται η βλάβη;", ["Στον σταθμό της Κηφισιάς", "Ανάμεσα στους σταθμούς Φάληρο και Μοσχάτο", "Στο κέντρο της Αθήνας", "Στο λιμάνι"], 1, "λόγω τεχνικής βλάβης στη γραμμή ανάμεσα στους σταθμούς Φάληρο και Μοσχάτο"),
  Q("Πόσο συχνά αναχωρούν τα λεωφορεία;", ["Κάθε πέντε λεπτά", "Κάθε δέκα λεπτά", "Κάθε μισή ώρα", "Μία φορά την ώρα"], 1, "κάθε δέκα λεπτά"),
  Q("Τι μπορούν να κάνουν όσοι πηγαίνουν προς το κέντρο;", ["Να περιμένουν μέχρι τις έξι", "Να χρησιμοποιήσουν το τραμ", "Να πάρουν ταξί με έκπτωση", "Να πάνε με τα πόδια"], 1, "μπορούν εναλλακτικά να χρησιμοποιήσουν το τραμ"),
 ],
 "gloss": {"ηλεκτρικού σιδηροδρόμου": "ηλεκτρικός σιδηρόδρομος — electric railway (Athens line 1)", "τεχνικής βλάβης": "τεχνική βλάβη — technical fault", "συρμοί": "συρμός — train", "δρομολόγια": "δρομολόγιο — service, scheduled run", "επιβατικού κοινού": "επιβατικό κοινό — the travelling public", "έχουν διατεθεί": "διατίθεμαι — to be made available", "εκτελούν": "εκτελώ — to carry out, run", "συνεργεία": "συνεργείο — repair crew; garage", "αποκατάσταση": "αποκατάσταση — repair, restoration", "εναλλακτικά": "εναλλακτικά — alternatively"},
})

ITEMS.append({
 "id": "l51-vm-epipla", "title": "Η παράδοση των επίπλων", "title_en": "The furniture delivery", "type": "voicemail", "level": "B2",
 "context_el": "Αγοράσατε έναν καναπέ και μια βιβλιοθήκη από ένα κατάστημα επίπλων. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα, κυρία Κωνσταντίνου, από το κατάστημα επίπλων «Δρυς» σας τηλεφωνώ. Η παράδοση του καναπέ και της βιβλιοθήκης σας ήταν προγραμματισμένη για την Τρίτη. Ο καναπές είναι έτοιμος, αλλά η βιβλιοθήκη καθυστέρησε στο εργοστάσιο και θα φτάσει σε δέκα μέρες περίπου.", "Good morning, Mrs Konstantinou, I'm calling from the Drys furniture shop. Delivery of your sofa and bookcase was scheduled for Tuesday. The sofa is ready, but the bookcase has been held up at the factory and will arrive in about ten days."),
  L("Υπάλληλος", "m", "Μπορούμε να σας φέρουμε τον καναπέ την Τρίτη, όπως είχαμε πει, και τη βιβλιοθήκη σε δεύτερη παράδοση, χωρίς καμία επιπλέον χρέωση. Ή, αν προτιμάτε, να τα φέρουμε όλα μαζί όταν έρθει η βιβλιοθήκη. Η συναρμολόγηση γίνεται από τους τεχνικούς μας και περιλαμβάνεται στην τιμή.", "We can bring you the sofa on Tuesday, as we'd said, and the bookcase in a second delivery, at no extra charge. Or, if you prefer, we can bring everything together when the bookcase arrives. Assembly is done by our technicians and is included in the price."),
  L("Υπάλληλος", "m", "Επειδή μένετε στον πέμπτο όροφο, θα σας παρακαλούσα να μας πείτε αν ο καναπές χωράει στο ασανσέρ. Αν όχι, θα χρειαστεί να τον ανεβάσουμε από τη σκάλα, και αυτό κοστίζει τριάντα ευρώ. Περιμένω το τηλεφώνημά σας. Ευχαριστώ.", "Since you live on the fifth floor, I'd ask you to tell us whether the sofa fits in the lift. If not, we'll have to carry it up the stairs, and that costs thirty euros. I look forward to your call. Thank you."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με την παραγγελία;", ["Ο καναπές ήρθε σε λάθος χρώμα", "Η βιβλιοθήκη καθυστέρησε στο εργοστάσιο", "Η τιμή αυξήθηκε", "Το κατάστημα κλείνει"], 1, "η βιβλιοθήκη καθυστέρησε στο εργοστάσιο"),
  Q("Πόσο κοστίζει η συναρμολόγηση;", ["Τριάντα ευρώ", "Περιλαμβάνεται στην τιμή", "Δέκα ευρώ ανά έπιπλο", "Εξαρτάται από τον όροφο"], 1, "Η συναρμολόγηση ... περιλαμβάνεται στην τιμή"),
  Q("Γιατί μπορεί να χρειαστεί επιπλέον χρέωση;", ["Επειδή θα έρθουν δύο φορές", "Επειδή ίσως ο καναπές δεν χωράει στο ασανσέρ", "Επειδή μένει μακριά", "Επειδή η παράδοση είναι Σάββατο"], 1, "Αν όχι, θα χρειαστεί να τον ανεβάσουμε από τη σκάλα, και αυτό κοστίζει τριάντα ευρώ"),
 ],
 "gloss": {"καναπέ": "καναπές — sofa", "βιβλιοθήκη": "βιβλιοθήκη — bookcase; library", "επίπλων": "έπιπλο — piece of furniture", "παράδοση": "παράδοση — delivery; tradition", "προγραμματισμένη": "προγραμματισμένος — scheduled", "εργοστάσιο": "εργοστάσιο — factory", "επιπλέον χρέωση": "επιπλέον χρέωση — extra charge", "συναρμολόγηση": "συναρμολόγηση — assembly", "περιλαμβάνεται": "περιλαμβάνομαι — to be included", "χωράει": "χωράω — to fit"},
})

ITEMS.append({
 "id": "l51-dia-giorti-mamas", "title": "Ένα δώρο για τη γιορτή της μαμάς", "title_en": "A present for Mum's name day", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε δύο αδέλφια να συζητούν τι δώρο θα κάνουν στη μητέρα τους για τη γιορτή της.",
 "script": [
  L("Δήμητρα", "f", "Ηλία, την Κυριακή γιορτάζει η μαμά. Έχεις σκεφτεί τίποτα για δώρο; Φέτος δεν θέλω να της πάρουμε πάλι λουλούδια και ένα κουτί σοκολατάκια.", "Ilias, Mum's name day is on Sunday. Have you thought of anything for a present? This year I don't want to get her flowers and a box of chocolates again."),
  L("Ηλίας", "m", "Συμφωνώ. Σκεφτόμουν κάτι που να το χρησιμοποιεί. Ξέρεις ότι παραπονιέται συνέχεια ότι δεν βλέπει καλά τα μηνύματα στο κινητό. Τι λες για ένα καινούργιο κινητό, με μεγαλύτερη οθόνη;", "I agree. I was thinking of something she'd use. You know she keeps complaining that she can't see the messages on her phone well. What about a new phone with a bigger screen?"),
  L("Δήμητρα", "f", "Καλή ιδέα, αλλά η μαμά μισεί τις αλλαγές. Θα της πάρει μήνες να μάθει το καινούργιο. Εγώ σκέφτηκα κάτι άλλο: να της κλείσουμε ένα Σαββατοκύριακο σε μια ιαματική πηγή, στα Λουτρά Πόζαρ. Πάντα έλεγε ότι θέλει να πάει.", "Good idea, but Mum hates change. It'll take her months to learn a new one. I thought of something else: we could book her a weekend at a spa, at the Pozar baths. She's always said she wants to go."),
  L("Ηλίας", "m", "Αυτό είναι τέλειο! Και να πάει μαζί με τη θεία Ελένη, για να έχει παρέα. Το πληρώνουμε μισό-μισό. Και το κινητό το αφήνουμε για τα Χριστούγεννα, και θα της το στήσω εγώ για να μην ταλαιπωρηθεί.", "That's perfect! And she can go with Aunt Eleni, so she has company. We'll split it half and half. And we'll leave the phone for Christmas, and I'll set it up for her so she doesn't have any hassle."),
 ],
 "questions": [
  Q("Γιατί ο Ηλίας σκέφτεται ένα καινούργιο κινητό;", ["Επειδή το παλιό χάλασε", "Επειδή η μητέρα τους δεν βλέπει καλά τα μηνύματα", "Επειδή είναι σε προσφορά", "Επειδή το ζήτησε η μητέρα"], 1, "παραπονιέται συνέχεια ότι δεν βλέπει καλά τα μηνύματα στο κινητό"),
  Q("Γιατί η Δήμητρα έχει αμφιβολίες για το κινητό;", ["Επειδή είναι ακριβό", "Επειδή η μητέρα τους μισεί τις αλλαγές", "Επειδή η μητέρα έχει ήδη καινούργιο", "Επειδή δεν ξέρουν ποιο να διαλέξουν"], 1, "η μαμά μισεί τις αλλαγές"),
  Q("Τι αποφασίζουν τελικά;", ["Να της πάρουν λουλούδια", "Ένα Σαββατοκύριακο σε ιαματική πηγή με τη θεία Ελένη", "Ένα κινητό για τη γιορτή της", "Ένα ταξίδι στο εξωτερικό"], 1, "να της κλείσουμε ένα Σαββατοκύριακο σε μια ιαματική πηγή ... Και να πάει μαζί με τη θεία Ελένη"),
 ],
 "gloss": {"γιορτή": "γιορτή — name day; holiday", "γιορτάζει": "γιορτάζω — to celebrate (a name day)", "σοκολατάκια": "σοκολατάκι — chocolate (piece)", "παραπονιέται": "παραπονιέμαι — to complain", "οθόνη": "οθόνη — screen", "μισεί": "μισώ — to hate", "ιαματική πηγή": "ιαματική πηγή — thermal spring, spa", "μισό-μισό": "μισό-μισό — half and half", "θα της το στήσω": "στήνω — to set up", "για να μην ταλαιπωρηθεί": "ταλαιπωρούμαι — to be put to trouble"},
})

ITEMS.append({
 "id": "l51-dia-trochospito", "title": "Διακοπές με τροχόσπιτο", "title_en": "A holiday in a camper van", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε ένα ζευγάρι να συζητάει με έναν υπάλληλο εταιρείας που νοικιάζει τροχόσπιτα.",
 "script": [
  L("Στέλιος", "m", "Καλημέρα. Θέλουμε να νοικιάσουμε ένα τροχόσπιτο για δέκα μέρες τον Ιούνιο, για να κάνουμε τον γύρο της Πελοποννήσου. Είμαστε δύο ενήλικες και ένα παιδί οχτώ χρονών.", "Good morning. We'd like to rent a camper van for ten days in June to do a tour of the Peloponnese. We're two adults and an eight-year-old child."),
  L("Υπάλληλος", "m", "Για τρία άτομα σας προτείνω το μικρότερο μοντέλο μας. Έχει κουζίνα, ψυγείο, τουαλέτα και κρεβάτια για τέσσερις. Μπορείτε να το οδηγήσετε με απλό δίπλωμα αυτοκινήτου. Η τιμή τον Ιούνιο είναι ενενήντα ευρώ τη μέρα, με την ασφάλεια.", "For three people I'd suggest our smallest model. It has a kitchen, a fridge, a toilet and beds for four. You can drive it with an ordinary car licence. The price in June is ninety euros a day, including insurance."),
  L("Μαρίνα", "f", "Μπορούμε να σταθμεύουμε όπου θέλουμε; Για παράδειγμα, σε μια παραλία;", "Can we park wherever we like? On a beach, for example?"),
  L("Υπάλληλος", "m", "Όχι, αυτό απαγορεύεται, και τα πρόστιμα είναι μεγάλα. Πρέπει να μένετε σε οργανωμένα κάμπινγκ, όπου θα βρείτε και ρεύμα και νερό. Σας δίνουμε έναν χάρτη με όλα τα κάμπινγκ της Πελοποννήσου. Τον Ιούνιο δεν χρειάζεται κράτηση, αλλά τον Αύγουστο είναι απαραίτητη.", "No, that's not allowed, and the fines are high. You have to stay in organised campsites, where you'll also find electricity and water. We give you a map of all the campsites in the Peloponnese. In June you don't need to book, but in August it's essential."),
  L("Στέλιος", "m", "Εντάξει. Και κάτι τελευταίο: πρέπει να το επιστρέψουμε καθαρό;", "Okay. And one last thing: do we have to return it clean?"),
  L("Υπάλληλος", "m", "Το εσωτερικό ναι, και με άδεια τη δεξαμενή της τουαλέτας. Το εξωτερικό το πλένουμε εμείς. Και με γεμάτο ρεζερβουάρ, όπως το παραλάβατε.", "The inside yes, and with the toilet tank emptied. We wash the outside. And with a full tank, as you received it."),
 ],
 "questions": [
  Q("Τι δίπλωμα χρειάζεται για το μικρότερο μοντέλο;", ["Δίπλωμα φορτηγού", "Απλό δίπλωμα αυτοκινήτου", "Διεθνές δίπλωμα", "Δεν χρειάζεται δίπλωμα"], 1, "Μπορείτε να το οδηγήσετε με απλό δίπλωμα αυτοκινήτου"),
  Q("Πού πρέπει να σταθμεύουν το βράδυ;", ["Όπου θέλουν", "Σε οργανωμένα κάμπινγκ", "Μόνο σε παραλίες", "Σε χώρους στάθμευσης ξενοδοχείων"], 1, "Πρέπει να μένετε σε οργανωμένα κάμπινγκ"),
  Q("Τι δεν χρειάζεται να κάνουν πριν το επιστρέψουν;", ["Να καθαρίσουν το εσωτερικό", "Να πλύνουν το εξωτερικό", "Να αδειάσουν τη δεξαμενή της τουαλέτας", "Να γεμίσουν το ρεζερβουάρ"], 1, "Το εξωτερικό το πλένουμε εμείς"),
 ],
 "gloss": {"τροχόσπιτο": "τροχόσπιτο — camper van, caravan", "τροχόσπιτα": "τροχόσπιτο — camper van, caravan", "ενήλικες": "ενήλικας — adult", "δίπλωμα": "δίπλωμα (οδήγησης) — driving licence", "ασφάλεια": "ασφάλεια — insurance; safety", "να σταθμεύουμε": "σταθμεύω — to park", "πρόστιμα": "πρόστιμο — fine", "απαραίτητη": "απαραίτητος — essential", "δεξαμενή": "δεξαμενή — tank", "ρεζερβουάρ": "ρεζερβουάρ — fuel tank", "το παραλάβατε": "παραλαμβάνω — to receive, collect"},
})

ITEMS.append({
 "id": "l51-int-michanodigos", "title": "Η μηχανοδηγός", "title_en": "The train driver", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια γυναίκα μηχανοδηγό τρένων.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αντωνίου, είστε μία από τις ελάχιστες γυναίκες μηχανοδηγούς στην Ελλάδα. Πώς ξεκίνησε αυτό;", "Ms Antoniou, you are one of the very few women train drivers in Greece. How did this start?"),
  L("Ευαγγελία", "f", "Ο πατέρας μου δούλευε στον σιδηρόδρομο, σε έναν μικρό σταθμό της Θεσσαλίας. Μεγάλωσα ακούγοντας τα τρένα να περνούν. Όταν τελείωσα το σχολείο, όλοι περίμεναν να γίνω νηπιαγωγός. Εγώ όμως έκανα αίτηση στη σχολή μηχανοδηγών. Ήμουν η μόνη γυναίκα στην τάξη.", "My father worked on the railway, at a small station in Thessaly. I grew up hearing the trains go by. When I finished school, everyone expected me to become a nursery teacher. But I applied to the train drivers' school. I was the only woman in the class."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο δύσκολο κομμάτι της δουλειάς;", "What's the hardest part of the job?"),
  L("Ευαγγελία", "f", "Η συγκέντρωση. Για ώρες πρέπει να είσαι απόλυτα προσεκτικός, να παρακολουθείς τα σήματα, την ταχύτητα, τη γραμμή. Ένα δευτερόλεπτο απροσεξίας μπορεί να κοστίσει πολύ. Επίσης, οι βάρδιες είναι δύσκολες: πολλές φορές ξεκινάω στις τέσσερις τα ξημερώματα.", "Concentration. For hours you have to be completely alert, to watch the signals, the speed, the track. A second of inattention can cost a lot. Also, the shifts are hard: I often start at four in the morning."),
  L("Δημοσιογράφος", "m", "Και τι αγαπάτε περισσότερο;", "And what do you love most?"),
  L("Ευαγγελία", "f", "Τη θέα. Η διαδρομή από τη Λάρισα προς τη Θεσσαλονίκη, μέσα από τα Τέμπη, το πρωί, με την ομίχλη πάνω από το ποτάμι, είναι κάτι που δεν το βαριέμαι ποτέ. Και τα παιδιά που μου κουνάνε το χέρι από τις διαβάσεις. Πάντα τους απαντάω με την κόρνα.", "The view. The route from Larissa to Thessaloniki, through the Tempi valley, in the morning, with the mist over the river, is something I never get tired of. And the children who wave at me from the level crossings. I always answer them with the horn."),
 ],
 "questions": [
  Q("Τι περίμεναν όλοι να γίνει η Ευαγγελία;", ["Μηχανικός", "Νηπιαγωγός", "Σταθμάρχης", "Γιατρός"], 1, "όλοι περίμεναν να γίνω νηπιαγωγός"),
  Q("Ποιο είναι, κατά την ίδια, το πιο δύσκολο κομμάτι της δουλειάς;", ["Οι επιβάτες", "Η συγκέντρωση για ώρες", "Ο μισθός", "Οι συνάδελφοι"], 1, "Η συγκέντρωση. Για ώρες πρέπει να είσαι απόλυτα προσεκτικός"),
  Q("Πώς απαντάει στα παιδιά που της κουνάνε το χέρι;", ["Τους κουνάει κι εκείνη το χέρι", "Με την κόρνα", "Σταματάει το τρένο", "Τους φωνάζει"], 1, "Πάντα τους απαντάω με την κόρνα"),
 ],
 "gloss": {"μηχανοδηγό": "μηχανοδηγός — train driver", "μηχανοδηγούς": "μηχανοδηγός — train driver", "σιδηρόδρομο": "σιδηρόδρομος — railway", "νηπιαγωγός": "νηπιαγωγός — nursery-school teacher", "έκανα αίτηση": "κάνω αίτηση — to apply", "συγκέντρωση": "συγκέντρωση — concentration", "σήματα": "σήμα — signal", "απροσεξίας": "απροσεξία — inattention", "βάρδιες": "βάρδια — shift", "ξημερώματα": "ξημερώματα — early morning, dawn", "δεν το βαριέμαι": "βαριέμαι — to get bored of", "διαβάσεις": "διάβαση — level crossing; crossing", "κόρνα": "κόρνα — horn"},
})

ITEMS.append({
 "id": "l51-rep-odontotos", "title": "Ο Οδοντωτός του Βουραϊκού", "title_en": "The rack railway of the Vouraikos gorge", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από μια ραδιοφωνική εκπομπή για τον σιδηρόδρομο Διακοφτού – Καλαβρύτων.",
 "script": [
  L("Ρεπόρτερ", "f", "Ο Οδοντωτός σιδηρόδρομος, που συνδέει το Διακοφτό, στις ακτές του Κορινθιακού, με τα Καλάβρυτα, είναι ένα από τα πιο εντυπωσιακά τρένα της Ευρώπης. Η γραμμή, μήκους περίπου είκοσι δύο χιλιομέτρων, κατασκευάστηκε στα τέλη του δέκατου ένατου αιώνα από Ιταλούς μηχανικούς.", "The rack railway, which links Diakopto on the shores of the Gulf of Corinth with Kalavryta, is one of the most impressive trains in Europe. The line, about twenty-two kilometres long, was built at the end of the nineteenth century by Italian engineers."),
  L("Ρεπόρτερ", "f", "Το όνομά του το οφείλει στον οδοντωτό κανόνα που βρίσκεται ανάμεσα στις ράγες σε ορισμένα σημεία. Εκεί, ένας οδοντωτός τροχός του τρένου «πιάνεται» από τον κανόνα, ώστε ο συρμός να μπορεί να ανεβαίνει τις πολύ απότομες κλίσεις χωρίς να γλιστράει.", "It owes its name to the toothed rack that lies between the rails at certain points. There, a toothed wheel on the train engages with the rack, so the train can climb the very steep gradients without slipping."),
  L("Ρεπόρτερ", "f", "Η διαδρομή περνάει μέσα από το φαράγγι του Βουραϊκού, ανάμεσα σε κάθετους βράχους, τούνελ και γέφυρες. Οι επισκέπτες μπορούν να κατέβουν στον σταθμό της Ζαχλωρούς και να περπατήσουν μέχρι τη μονή του Μεγάλου Σπηλαίου. Οι κάτοικοι της περιοχής ζητούν να αυξηθούν τα δρομολόγια τον χειμώνα, όταν το τρένο είναι για πολλούς ο μόνος ασφαλής τρόπος να φτάσουν στα Καλάβρυτα.", "The route runs through the Vouraikos gorge, between sheer rock faces, tunnels and bridges. Visitors can get off at Zachlorou station and walk to the monastery of Mega Spilaio. Local residents are asking for more services in winter, when the train is for many the only safe way to reach Kalavryta."),
 ],
 "questions": [
  Q("Ποιοι κατασκεύασαν τη γραμμή;", ["Γερμανοί μηχανικοί", "Ιταλοί μηχανικοί", "Ο ελληνικός στρατός", "Μια γαλλική εταιρεία"], 1, "κατασκευάστηκε στα τέλη του δέκατου ένατου αιώνα από Ιταλούς μηχανικούς"),
  Q("Σε τι χρησιμεύει ο οδοντωτός κανόνας;", ["Να σταματάει το τρένο στους σταθμούς", "Να ανεβαίνει το τρένο απότομες κλίσεις χωρίς να γλιστράει", "Να δίνει ρεύμα στο τρένο", "Να μειώνει τον θόρυβο"], 1, "ώστε ο συρμός να μπορεί να ανεβαίνει τις πολύ απότομες κλίσεις χωρίς να γλιστράει"),
  Q("Τι ζητούν οι κάτοικοι;", ["Να κλείσει η γραμμή τον χειμώνα", "Περισσότερα δρομολόγια τον χειμώνα", "Φθηνότερα εισιτήρια για τους τουρίστες", "Έναν νέο σταθμό στη Ζαχλωρού"], 1, "ζητούν να αυξηθούν τα δρομολόγια τον χειμώνα"),
 ],
 "gloss": {"Οδοντωτός": "Οδοντωτός — the rack railway (Diakopto–Kalavryta)", "οδοντωτό κανόνα": "οδοντωτός κανόνας — toothed rack (rail)", "ράγες": "ράγα — rail", "οδοντωτός τροχός": "οδοντωτός τροχός — toothed wheel, cog", "συρμός": "συρμός — train", "απότομες κλίσεις": "απότομη κλίση — steep gradient", "να γλιστράει": "γλιστράω — to slip", "φαράγγι": "φαράγγι — gorge", "κάθετους": "κάθετος — vertical, sheer", "τούνελ": "τούνελ — tunnel", "μονή": "μονή — monastery", "δρομολόγια": "δρομολόγιο — scheduled service"},
})

ITEMS.append({
 "id": "l51-dia-epeteios", "title": "Κλείνοντας τραπέζι για την επέτειο", "title_en": "Booking a table for the anniversary", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να τηλεφωνεί σε ένα εστιατόριο για να κλείσει τραπέζι για την επέτειο του γάμου του.",
 "script": [
  L("Υπάλληλος", "f", "Εστιατόριο «Θαλασσινό», καλησπέρα σας.", "Thalassino restaurant, good evening."),
  L("Τάσος", "m", "Καλησπέρα. Θα ήθελα να κλείσω ένα τραπέζι για δύο άτομα το Σάββατο το βράδυ, γύρω στις εννιά. Είναι η επέτειος του γάμου μας, δέκα χρόνια, και θα ήθελα, αν γίνεται, ένα τραπέζι δίπλα στη θάλασσα.", "Good evening. I'd like to book a table for two on Saturday evening, around nine. It's our wedding anniversary, ten years, and if possible I'd like a table by the sea."),
  L("Υπάλληλος", "f", "Χρόνια πολλά! Για τις εννιά τα τραπέζια δίπλα στη θάλασσα είναι δυστυχώς όλα κλεισμένα. Έχω ένα ελεύθερο στις οχτώ, ή στις δέκα και μισή. Αλλιώς, στις εννιά μπορώ να σας δώσω ένα τραπέζι στη βεράντα, με θέα, αλλά λίγο πιο μέσα.", "Congratulations! At nine, the tables by the sea are unfortunately all booked. I have one free at eight, or at half past ten. Otherwise, at nine I can give you a table on the terrace, with a view, but a little further in."),
  L("Τάσος", "m", "Θα πάρω αυτό στις οχτώ, δίπλα στη θάλασσα. Και κάτι ακόμα: θέλω να της κάνω μια έκπληξη. Μπορώ να σας φέρω το απόγευμα μια τούρτα, να τη σερβίρετε στο τέλος;", "I'll take the one at eight by the sea. And one more thing: I want to surprise her. Can I bring you a cake in the afternoon for you to serve at the end?"),
  L("Υπάλληλος", "f", "Βεβαίως. Χρεώνουμε πέντε ευρώ για το σερβίρισμα, και μπορούμε να βάλουμε και ένα κερί. Αν θέλετε, ετοιμάζουμε και ένα μπουκάλι σαμπάνια στον πάγο. Να σας γράψω σε ποιο όνομα;", "Of course. We charge five euros for serving it, and we can add a candle too. If you like, we'll also prepare a bottle of champagne on ice. What name shall I put it under?"),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να πάρει τραπέζι δίπλα στη θάλασσα στις εννιά;", ["Επειδή το εστιατόριο κλείνει νωρίς", "Επειδή είναι όλα κλεισμένα", "Επειδή φυσάει", "Επειδή γίνεται ένα πάρτι"], 1, "Για τις εννιά τα τραπέζια δίπλα στη θάλασσα είναι δυστυχώς όλα κλεισμένα"),
  Q("Τι ώρα κλείνει τελικά το τραπέζι ο Τάσος;", ["Στις εννιά", "Στις οχτώ", "Στις δέκα και μισή", "Στις επτά"], 1, "Θα πάρω αυτό στις οχτώ"),
  Q("Πόσο χρεώνει το εστιατόριο για να σερβίρει την τούρτα;", ["Τίποτα", "Πέντε ευρώ", "Δέκα ευρώ", "Είκοσι ευρώ με τη σαμπάνια"], 1, "Χρεώνουμε πέντε ευρώ για το σερβίρισμα"),
 ],
 "gloss": {"επέτειο": "επέτειος — anniversary", "επέτειος": "επέτειος — anniversary", "Χρόνια πολλά": "Χρόνια πολλά! — congratulations, many happy returns", "κλεισμένα": "κλεισμένος — booked, reserved", "βεράντα": "βεράντα — terrace, veranda", "έκπληξη": "έκπληξη — surprise", "τούρτα": "τούρτα — (layer) cake", "σερβίρισμα": "σερβίρισμα — serving", "κερί": "κερί — candle", "στον πάγο": "στον πάγο — on ice"},
})

ITEMS.append({
 "id": "l51-mono-kagiak", "title": "Πριν από τη βόλτα με καγιάκ", "title_en": "Before the kayak trip", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν οδηγό να δίνει οδηγίες σε μια ομάδα πριν από μια εκδρομή με θαλάσσιο καγιάκ στη Μήλο.",
 "script": [
  L("Οδηγός", "m", "Καλημέρα σε όλους! Σήμερα θα κωπηλατήσουμε περίπου δώδεκα χιλιόμετρα κατά μήκος της ακτής, μέχρι τις σπηλιές του Κλέφτικου. Θα κάνουμε δύο στάσεις για μπάνιο και μία για φαγητό σε μια μικρή παραλία που δεν φτάνει κανείς με αυτοκίνητο.", "Good morning, everyone! Today we'll paddle about twelve kilometres along the coast, to the caves of Kleftiko. We'll make two stops for a swim and one for lunch on a small beach that nobody can reach by car."),
  L("Οδηγός", "m", "Πρώτα απ' όλα, το σωσίβιο το φοράτε όλη την ώρα, ακόμα κι αν είστε καλοί κολυμβητές. Τα καγιάκ είναι διθέσια: αυτός που κάθεται πίσω κατευθύνει με το πηδάλιο, και αυτός που κάθεται μπροστά δίνει τον ρυθμό. Αν αναποδογυρίσετε, μην πανικοβληθείτε. Κρατηθείτε από το καγιάκ και περιμένετε, θα έρθω αμέσως.", "First of all, you wear your life jacket the whole time, even if you're good swimmers. The kayaks are two-seaters: the person in the back steers with the rudder, and the person in front sets the rhythm. If you capsize, don't panic. Hold on to the kayak and wait; I'll come straight away."),
  L("Οδηγός", "m", "Μείνετε πάντα πίσω από εμένα και μην μπαίνετε στις σπηλιές χωρίς να σας πω, γιατί με το κύμα μπορεί να χτυπήσετε στα βράχια. Βάλτε αντηλιακό και στα πόδια, γιατί είναι το σημείο που καίγεται περισσότερο. Τα κινητά σας μπαίνουν στις αδιάβροχες τσάντες. Έτοιμοι;", "Always stay behind me and don't go into the caves unless I tell you, because with the swell you could hit the rocks. Put sunscreen on your legs too, because that's where you burn most. Your phones go in the waterproof bags. Ready?"),
 ],
 "questions": [
  Q("Πώς είναι η παραλία όπου θα σταματήσουν για φαγητό;", ["Πολυσύχναστη, με ταβέρνες", "Δεν φτάνει κανείς σε αυτήν με αυτοκίνητο", "Είναι μέσα σε μια σπηλιά", "Είναι δίπλα στο λιμάνι"], 1, "μια μικρή παραλία που δεν φτάνει κανείς με αυτοκίνητο"),
  Q("Τι κάνει αυτός που κάθεται πίσω στο καγιάκ;", ["Δίνει τον ρυθμό", "Κατευθύνει με το πηδάλιο", "Φωτογραφίζει", "Ξεκουράζεται"], 1, "αυτός που κάθεται πίσω κατευθύνει με το πηδάλιο"),
  Q("Γιατί δεν πρέπει να μπαίνουν μόνοι τους στις σπηλιές;", ["Επειδή απαγορεύεται από τον νόμο", "Επειδή με το κύμα μπορεί να χτυπήσουν στα βράχια", "Επειδή είναι σκοτεινές", "Επειδή υπάρχουν φώκιες"], 1, "με το κύμα μπορεί να χτυπήσετε στα βράχια"),
 ],
 "gloss": {"καγιάκ": "καγιάκ — kayak", "θα κωπηλατήσουμε": "κωπηλατώ — to paddle, row", "κατά μήκος": "κατά μήκος — along", "σπηλιές": "σπηλιά — cave", "σωσίβιο": "σωσίβιο — life jacket", "κολυμβητές": "κολυμβητής — swimmer", "διθέσια": "διθέσιος — two-seater", "πηδάλιο": "πηδάλιο — rudder", "αναποδογυρίσετε": "αναποδογυρίζω — to capsize, turn over", "μην πανικοβληθείτε": "πανικοβάλλομαι — to panic", "καίγεται": "καίγομαι — to burn", "αδιάβροχες": "αδιάβροχος — waterproof"},
})

ITEMS.append({
 "id": "l51-c1-akriveia", "title": "Η ακρίβεια και το καλάθι του νοικοκυριού", "title_en": "The cost of living and the household basket", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συζήτηση με μια οικονομολόγο για την αύξηση των τιμών και τις επιπτώσεις της στα νοικοκυριά.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Βλάχου, οι ακροατές μας λένε ότι, ενώ οι επίσημοι δείκτες δείχνουν ότι ο πληθωρισμός έχει υποχωρήσει, οι ίδιοι στο σούπερ μάρκετ δεν βλέπουν καμία διαφορά. Πώς εξηγείται αυτή η αντίφαση;", "Ms Vlachou, our listeners say that although the official indicators show inflation has eased, they themselves see no difference at the supermarket. How can this contradiction be explained?"),
  L("Οικονομολόγος", "f", "Η αντίφαση είναι μόνο φαινομενική. Όταν λέμε ότι ο πληθωρισμός υποχώρησε, εννοούμε ότι οι τιμές αυξάνονται πιο αργά, όχι ότι μειώνονται. Το ψωμί, το γάλα ή το λάδι δεν έγιναν φθηνότερα· απλώς δεν ακριβαίνουν με τον ίδιο ρυθμό. Οι τιμές έχουν «κλειδώσει» σε ένα υψηλότερο επίπεδο, και οι μισθοί δεν έχουν προλάβει να καλύψουν τη διαφορά.", "The contradiction is only apparent. When we say inflation has eased, we mean prices are rising more slowly, not that they are falling. Bread, milk or olive oil haven't become cheaper; they're just not going up at the same rate. Prices have 'locked in' at a higher level, and wages haven't caught up to cover the difference."),
  L("Δημοσιογράφος", "m", "Ποιοι πλήττονται περισσότερο;", "Who is hit hardest?"),
  L("Οικονομολόγος", "f", "Τα νοικοκυριά με χαμηλά εισοδήματα, γιατί ξοδεύουν μεγαλύτερο μέρος του εισοδήματός τους σε τρόφιμα, ενέργεια και ενοίκιο, δηλαδή ακριβώς στα αγαθά που ακρίβυναν περισσότερο. Ένα πλούσιο νοικοκυριό μπορεί να περιορίσει τις διακοπές του. Ένα φτωχό δεν μπορεί να περιορίσει το φαγητό του χωρίς να υποστεί πραγματική στέρηση. Γι' αυτό λέμε ότι ο πληθωρισμός λειτουργεί σαν ένας άδικος, αόρατος φόρος.", "Low-income households, because they spend a larger share of their income on food, energy and rent, which are exactly the goods that have gone up most. A wealthy household can cut back on holidays. A poor one can't cut back on food without suffering real deprivation. That's why we say inflation works like an unfair, invisible tax."),
  L("Δημοσιογράφος", "m", "Τι μπορεί να γίνει;", "What can be done?"),
  L("Οικονομολόγος", "f", "Τα γενικά επιδόματα, που δίνονται σε όλους, έχουν περιορισμένη αποτελεσματικότητα και μπορεί να τροφοδοτήσουν περαιτέρω τον πληθωρισμό. Πιο αποτελεσματικά είναι τα στοχευμένα μέτρα για τα πιο ευάλωτα νοικοκυριά, καθώς και η ενίσχυση του ανταγωνισμού στην αγορά τροφίμων, όπου συχνά λίγες εταιρείες ελέγχουν μεγάλο μέρος της αγοράς. Χρειάζονται επίσης μακροπρόθεσμες λύσεις, όπως η αύξηση της παραγωγικότητας, ώστε οι μισθοί να αυξάνονται χωρίς να ανεβαίνουν οι τιμές.", "General benefits, given to everyone, have limited effectiveness and may further fuel inflation. More effective are targeted measures for the most vulnerable households, as well as strengthening competition in the food market, where often a few companies control a large part of the market. Long-term solutions are also needed, such as raising productivity, so that wages can rise without prices going up."),
 ],
 "questions": [
  Q("Τι σημαίνει, κατά την οικονομολόγο, ότι «ο πληθωρισμός υποχώρησε»;", ["Ότι οι τιμές μειώνονται", "Ότι οι τιμές αυξάνονται πιο αργά", "Ότι οι μισθοί αυξήθηκαν", "Ότι τα τρόφιμα έγιναν φθηνότερα"], 1, "εννοούμε ότι οι τιμές αυξάνονται πιο αργά, όχι ότι μειώνονται"),
  Q("Γιατί πλήττονται περισσότερο τα φτωχά νοικοκυριά;", ["Επειδή πληρώνουν περισσότερους φόρους", "Επειδή ξοδεύουν μεγαλύτερο μέρος του εισοδήματός τους στα αγαθά που ακρίβυναν περισσότερο", "Επειδή δεν έχουν τραπεζικό λογαριασμό", "Επειδή ζουν στις πόλεις"], 1, "ξοδεύουν μεγαλύτερο μέρος του εισοδήματός τους σε τρόφιμα, ενέργεια και ενοίκιο"),
  Q("Γιατί ο πληθωρισμός χαρακτηρίζεται «αόρατος φόρος»;", ["Επειδή τον εισπράττει το κράτος", "Επειδή επιβαρύνει άδικα, χωρίς να φαίνεται, κυρίως τους φτωχότερους", "Επειδή δεν τον καταλαβαίνει κανείς", "Επειδή αφορά μόνο τις επιχειρήσεις"], 1, "λειτουργεί σαν ένας άδικος, αόρατος φόρος"),
  Q("Ποια μέτρα θεωρεί πιο αποτελεσματικά;", ["Γενικά επιδόματα για όλους", "Στοχευμένα μέτρα για τα ευάλωτα νοικοκυριά και ενίσχυση του ανταγωνισμού", "Πάγωμα όλων των τιμών", "Μείωση των μισθών"], 1, "Πιο αποτελεσματικά είναι τα στοχευμένα μέτρα ... καθώς και η ενίσχυση του ανταγωνισμού"),
 ],
 "gloss": {"οικονομολόγο": "οικονομολόγος — economist", "επιπτώσεις": "επίπτωση — effect, consequence", "νοικοκυριά": "νοικοκυριό — household", "ακροατές": "ακροατής — listener", "δείκτες": "δείκτης — indicator, index", "πληθωρισμός": "πληθωρισμός — inflation", "έχει υποχωρήσει": "υποχωρώ — to ease, recede", "αντίφαση": "αντίφαση — contradiction", "φαινομενική": "φαινομενικός — apparent", "ακριβαίνουν": "ακριβαίνω — to become more expensive", "πλήττονται": "πλήττομαι — to be hit, affected", "εισοδήματα": "εισόδημα — income", "αγαθά": "αγαθό — good, commodity", "στέρηση": "στέρηση — deprivation", "επιδόματα": "επίδομα — benefit, allowance", "να τροφοδοτήσουν": "τροφοδοτώ — to fuel, feed", "στοχευμένα": "στοχευμένος — targeted", "ευάλωτα": "ευάλωτος — vulnerable", "ανταγωνισμού": "ανταγωνισμός — competition", "μακροπρόθεσμες": "μακροπρόθεσμος — long-term", "παραγωγικότητας": "παραγωγικότητα — productivity"},
})

ITEMS.append({
 "id": "l51-c1-bouboulina", "title": "Λασκαρίνα Μπουμπουλίνα", "title_en": "Laskarina Bouboulina", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια ξενάγηση στο αρχοντικό της Μπουμπουλίνας στις Σπέτσες.",
 "script": [
  L("Ξεναγός", "f", "Καλώς ήρθατε στο αρχοντικό της Λασκαρίνας Μπουμπουλίνας, μιας από τις πιο εμβληματικές μορφές της Επανάστασης του 1821. Σύμφωνα με την παράδοση, γεννήθηκε το 1771 σε μια φυλακή της Κωνσταντινούπολης, όπου η μητέρα της είχε πάει να επισκεφθεί τον φυλακισμένο πατέρα της, έναν Υδραίο καπετάνιο. Μεγάλωσε στην Ύδρα και αργότερα εγκαταστάθηκε εδώ, στις Σπέτσες.", "Welcome to the mansion of Laskarina Bouboulina, one of the most iconic figures of the 1821 Revolution. According to tradition, she was born in 1771 in a prison in Constantinople, where her mother had gone to visit her imprisoned father, a captain from Hydra. She grew up on Hydra and later settled here on Spetses."),
  L("Ξεναγός", "f", "Η ζωή της σημαδεύτηκε από απώλειες. Παντρεύτηκε δύο φορές, και οι δύο σύζυγοί της, καπετάνιοι, σκοτώθηκαν σε συγκρούσεις με πειρατές. Από αυτούς κληρονόμησε μια μεγάλη περιουσία, την οποία διαχειρίστηκε η ίδια με εξαιρετική ικανότητα, σε μια εποχή που οι γυναίκες σπάνια είχαν λόγο στις επιχειρήσεις. Έγινε μία από τις πλουσιότερες πλοιοκτήτριες του νησιού.", "Her life was marked by losses. She married twice, and both her husbands, ship captains, were killed in clashes with pirates. From them she inherited a large fortune, which she managed herself with exceptional skill, at a time when women rarely had a say in business. She became one of the richest shipowners on the island."),
  L("Ξεναγός", "f", "Λίγο πριν από την Επανάσταση, ναυπήγησε με δικά της έξοδα ένα μεγάλο πολεμικό πλοίο, τον «Αγαμέμνονα». Όταν ξέσπασε ο Αγώνας, τα πλοία της συμμετείχαν στον ναυτικό αποκλεισμό του Ναυπλίου, και η ίδια βρέθηκε στην πολιορκία της Τριπολιτσάς. Διέθεσε σχεδόν ολόκληρη την περιουσία της για την υπόθεση της ανεξαρτησίας.", "Shortly before the Revolution, she had a large warship, the Agamemnon, built at her own expense. When the struggle broke out, her ships took part in the naval blockade of Nafplio, and she herself was present at the siege of Tripolitsa. She devoted almost her entire fortune to the cause of independence."),
  L("Ξεναγός", "f", "Το τέλος της ήταν απροσδόκητα πεζό: σκοτώθηκε το 1825, εδώ στις Σπέτσες, κατά τη διάρκεια μιας οικογενειακής διαμάχης. Σήμερα η μορφή της έχει περάσει στον θρύλο, και συχνά είναι δύσκολο να ξεχωρίσει κανείς την ιστορία από τον μύθο. Αυτό που μένει αδιαμφισβήτητο είναι ότι μια γυναίκα, σε έναν κόσμο ανδρών, διαδραμάτισε καθοριστικό ρόλο στη γέννηση του νεοελληνικού κράτους.", "Her end was unexpectedly mundane: she was killed in 1825, here on Spetses, during a family dispute. Today her figure has passed into legend, and it is often hard to separate history from myth. What remains undisputed is that a woman, in a world of men, played a decisive role in the birth of the modern Greek state."),
 ],
 "questions": [
  Q("Πού γεννήθηκε, σύμφωνα με την παράδοση, η Μπουμπουλίνα;", ["Στις Σπέτσες", "Σε μια φυλακή της Κωνσταντινούπολης", "Στην Ύδρα", "Σε ένα πλοίο"], 1, "γεννήθηκε το 1771 σε μια φυλακή της Κωνσταντινούπολης"),
  Q("Πώς απέκτησε την περιουσία της;", ["Από τον πατέρα της", "Την κληρονόμησε από τους δύο συζύγους της", "Από το εμπόριο κρασιού", "Από τη Φιλική Εταιρεία"], 1, "Από αυτούς κληρονόμησε μια μεγάλη περιουσία"),
  Q("Τι έκανε λίγο πριν από την Επανάσταση;", ["Ταξίδεψε στη Ρωσία", "Ναυπήγησε με δικά της έξοδα ένα πολεμικό πλοίο", "Πούλησε τα πλοία της", "Έφυγε από τις Σπέτσες"], 1, "ναυπήγησε με δικά της έξοδα ένα μεγάλο πολεμικό πλοίο"),
  Q("Τι θεωρεί η ξεναγός «αδιαμφισβήτητο»;", ["Ότι γεννήθηκε σε φυλακή", "Ότι διαδραμάτισε καθοριστικό ρόλο στη γέννηση του νεοελληνικού κράτους", "Ότι ήταν η πλουσιότερη γυναίκα της Ευρώπης", "Ότι σκοτώθηκε σε μάχη"], 1, "Αυτό που μένει αδιαμφισβήτητο είναι ότι μια γυναίκα ... διαδραμάτισε καθοριστικό ρόλο"),
 ],
 "gloss": {"αρχοντικό": "αρχοντικό — mansion", "εμβληματικές": "εμβληματικός — iconic, emblematic", "φυλακισμένο": "φυλακισμένος — imprisoned", "Υδραίο": "Υδραίος — from Hydra", "απώλειες": "απώλεια — loss", "σύζυγοί": "σύζυγος — spouse", "πειρατές": "πειρατής — pirate", "κληρονόμησε": "κληρονομώ — to inherit", "περιουσία": "περιουσία — fortune, property", "διαχειρίστηκε": "διαχειρίζομαι — to manage", "πλοιοκτήτριες": "πλοιοκτήτρια — (female) shipowner", "ναυπήγησε": "ναυπηγώ — to build (a ship)", "αποκλεισμό": "αποκλεισμός — blockade", "πολιορκία": "πολιορκία — siege", "πεζό": "πεζός — mundane, prosaic", "διαμάχης": "διαμάχη — dispute, feud", "θρύλο": "θρύλος — legend", "αδιαμφισβήτητο": "αδιαμφισβήτητος — undisputed", "διαδραμάτισε": "διαδραματίζω — to play (a role)"},
})

rnd = random.Random(51)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-51.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
