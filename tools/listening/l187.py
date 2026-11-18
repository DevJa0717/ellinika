# Source for library/listening/listening-187.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l187.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l187-ann-syllogi-christougenniatikon-dentron", "title": "Πού πάνε τα χριστουγεννιάτικα δέντρα", "title_en": "Where the Christmas trees go", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο ραδιόφωνο λίγες μέρες μετά τα Φώτα.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος ενημερώνει ότι από τη Δευτέρα 8 ως την Κυριακή 21 Ιανουαρίου θα συλλέγει τα φυσικά χριστουγεννιάτικα δέντρα των κατοίκων. Τα δέντρα θα τεμαχίζονται και θα γίνονται λίπασμα για τα πάρκα και τις παιδικές χαρές της πόλης, αντί να καταλήγουν στη χωματερή.", "The municipality announces that from Monday 8 to Sunday 21 January it will collect residents' real Christmas trees. The trees will be shredded and turned into mulch for the city's parks and playgrounds, instead of ending up in the landfill."),
  L("Εκφωνήτρια", "f", "Μπορείτε να αφήνετε τα δέντρα σε ένα από τα έξι σημεία συλλογής, που θα βρείτε στην ιστοσελίδα του δήμου, ή δίπλα στους κάδους απορριμμάτων τη νύχτα της Τετάρτης. Παρακαλούμε να αφαιρείτε πρώτα όλα τα στολίδια, τα λαμπάκια και τη βάση, και να μη βάζετε τα δέντρα μέσα σε πλαστικές σακούλες.", "You can leave the trees at one of the six collection points, which you will find on the municipality's website, or next to the rubbish bins on Wednesday night. Please first remove all decorations, lights and the stand, and do not put the trees in plastic bags."),
  L("Εκφωνήτρια", "f", "Όσοι έχουν δέντρο σε γλάστρα με ρίζες μπορούν να το φέρουν στο δημοτικό φυτώριο. Οι γεωπόνοι του δήμου θα ελέγξουν αν είναι σε καλή κατάσταση και, αν ναι, θα το φυτέψουν στο άλσος της πόλης τον Φεβρουάριο.", "Those who have a potted tree with roots can bring it to the municipal nursery. The municipality's agronomists will check whether it is in good condition and, if so, will plant it in the town's grove in February."),
 ],
 "questions": [
  Q("Τι θα γίνουν τα δέντρα που θα συλλεχθούν;", ["Θα πουληθούν για καυσόξυλα", "Θα γίνουν λίπασμα για τα πάρκα", "Θα πεταχτούν στη χωματερή", "Θα στολίσουν την πλατεία του χρόνου"], 1, "Τα δέντρα θα τεμαχίζονται και θα γίνονται λίπασμα για τα πάρκα και τις παιδικές χαρές της πόλης"),
  Q("Τι πρέπει να κάνουν οι κάτοικοι πριν αφήσουν το δέντρο;", ["Να το κόψουν σε κομμάτια", "Να το βάλουν σε πλαστική σακούλα", "Να αφαιρέσουν τα στολίδια, τα λαμπάκια και τη βάση", "Να τηλεφωνήσουν στον δήμο"], 2, "να αφαιρείτε πρώτα όλα τα στολίδια, τα λαμπάκια και τη βάση"),
  Q("Τι θα γίνει με τα δέντρα σε γλάστρα με ρίζες;", ["Θα επιστραφούν στους κατοίκους", "Θα πουληθούν στο φυτώριο", "Θα γίνουν και αυτά λίπασμα", "Αν είναι σε καλή κατάσταση, θα φυτευτούν στο άλσος"], 3, "θα το φυτέψουν στο άλσος της πόλης τον Φεβρουάριο"),
 ],
 "gloss": {"Φώτα": "Φώτα — Epiphany (6 January)", "συλλέγει": "συλλέγω — to collect", "τεμαχίζονται": "τεμαχίζομαι — to be cut up, shredded", "χωματερή": "χωματερή — landfill", "στολίδια": "στολίδι — decoration, ornament", "λαμπάκια": "λαμπάκι — fairy light", "φυτώριο": "φυτώριο — (plant) nursery", "άλσος": "άλσος — grove, small wood"},
})

ITEMS.append({
 "id": "l187-int-chorografos", "title": "Η χορογράφος της παράστασης", "title_en": "The show's choreographer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια χορογράφο που ετοιμάζει τους χορούς για μια θεατρική παράσταση.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνει μια χορογράφος σε μια θεατρική παράσταση;", "What exactly does a choreographer do in a theatre production?"),
  L("Χορογράφος", "f", "Σχεδιάζω κάθε κίνηση που γίνεται πάνω στη σκηνή με τη μουσική: όχι μόνο τους χορούς, αλλά και το πώς μπαίνει ένας χορός ανθρώπων, πώς πέφτει ένας ηθοποιός, πώς τρέχουν δέκα άτομα χωρίς να πέσουν το ένα πάνω στο άλλο. Στη συγκεκριμένη παράσταση οι περισσότεροι ηθοποιοί δεν έχουν χορέψει ποτέ επαγγελματικά.", "I design every movement that happens on stage to music: not just the dances, but also how a crowd enters, how an actor falls, how ten people run without crashing into each other. In this particular production most of the actors have never danced professionally."),
  L("Δημοσιογράφος", "m", "Αυτό δεν είναι δύσκολο;", "Isn't that difficult?"),
  L("Χορογράφος", "f", "Είναι, αλλά έχει και πλεονεκτήματα. Οι επαγγελματίες χορευτές έχουν ωραία τεχνική, αλλά καμιά φορά κινούνται όλοι το ίδιο. Οι ηθοποιοί κινούνται σαν άνθρωποι, και αυτό στη σκηνή συγκινεί. Δεν τους ζητάω ποτέ να μιμηθούν εμένα. Τους δίνω μια εικόνα, για παράδειγμα «περπατάτε σε πάγο» ή «σας κυνηγάει ο άνεμος», και αφήνω το σώμα τους να βρει τη δική του λύση.", "It is, but it also has advantages. Professional dancers have beautiful technique, but sometimes they all move the same way. Actors move like people, and on stage that is moving. I never ask them to copy me. I give them an image, for example 'you're walking on ice' or 'the wind is chasing you', and let their body find its own solution."),
  L("Δημοσιογράφος", "m", "Πόσο κρατούν οι πρόβες;", "How long do rehearsals last?"),
  L("Χορογράφος", "f", "Έξι εβδομάδες, τέσσερις ώρες τη μέρα. Ξεκινάμε πάντα με μισή ώρα ζέσταμα, γιατί ο τραυματισμός ενός ηθοποιού μπορεί να ακυρώσει όλη την παράσταση. Και την τελευταία εβδομάδα δεν προσθέτω τίποτα καινούργιο· μόνο καθαρίζουμε όσα έχουμε ήδη.", "Six weeks, four hours a day. We always start with half an hour of warm-up, because one actor's injury can cancel the whole show. And in the last week I add nothing new; we only polish what we already have."),
 ],
 "questions": [
  Q("Τι σχεδιάζει η χορογράφος σε μια θεατρική παράσταση;", ["Μόνο τους χορούς", "Κάθε κίνηση πάνω στη σκηνή με τη μουσική", "Τα κοστούμια", "Τον φωτισμό"], 1, "Σχεδιάζω κάθε κίνηση που γίνεται πάνω στη σκηνή με τη μουσική"),
  Q("Πώς δουλεύει με τους ηθοποιούς;", ["Τους ζητά να μιμηθούν τις κινήσεις της", "Τους δείχνει βίντεο επαγγελματιών", "Τους δίνει μια εικόνα και αφήνει το σώμα τους να βρει λύση", "Τους στέλνει σε μαθήματα χορού"], 2, "Τους δίνω μια εικόνα"),
  Q("Γιατί ξεκινούν πάντα με ζέσταμα;", ["Γιατί η αίθουσα είναι κρύα", "Για να μάθουν τη μουσική", "Για να γνωριστούν μεταξύ τους", "Γιατί ένας τραυματισμός μπορεί να ακυρώσει την παράσταση"], 3, "ο τραυματισμός ενός ηθοποιού μπορεί να ακυρώσει όλη την παράσταση"),
 ],
 "gloss": {"χορογράφος": "χορογράφος — choreographer", "χορός ανθρώπων": "χορός (ανθρώπων) — chorus, crowd (on stage)", "πλεονεκτήματα": "πλεονέκτημα — advantage", "συγκινεί": "συγκινώ — to move, touch", "μιμηθούν": "μιμούμαι — to imitate", "πρόβες": "πρόβα — rehearsal", "ζέσταμα": "ζέσταμα — warm-up", "τραυματισμός": "τραυματισμός — injury"},
})

ITEMS.append({
 "id": "l187-vm-gamos-stin-kriti", "title": "Μήνυμα για τον γάμο στην Κρήτη", "title_en": "A message about the wedding in Crete", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα που άφησε μια ξαδέρφη στον τηλεφωνητή για έναν γάμο στην Κρήτη.",
 "script": [
  L("Κατερίνα", "f", "Γεια σου, Μάνο, η Κατερίνα είμαι. Σε παίρνω για τον γάμο του Στέλιου τον Ιούνιο. Η θεία θέλει να ξέρει ως το τέλος του μήνα πόσοι θα έρθετε, γιατί το κέντρο ζητάει τον τελικό αριθμό για το φαγητό. Θα φέρετε και τα παιδιά;", "Hi, Manos, it's Katerina. I'm calling about Stelios's wedding in June. Auntie wants to know by the end of the month how many of you are coming, because the reception venue is asking for the final number for the food. Will you bring the children too?"),
  L("Κατερίνα", "f", "Για το ταξίδι: τα εισιτήρια για το πλοίο του Σαββάτου ακριβαίνουν πολύ, οπότε σου προτείνω να κλείσεις από τώρα. Το γλέντι θα γίνει στο χωριό, σε ένα κτήμα με λυράρηδες, και κανονικά θα κρατήσει ως το πρωί. Για τη διαμονή, ο θείος έχει ετοιμάσει το πατρικό σπίτι για όσους έρχονται από μακριά, οπότε δεν χρειάζεται να πληρώσετε ξενοδοχείο.", "About the trip: tickets for the Saturday ferry get very expensive, so I suggest you book now. The party will be in the village, at an estate with lyre players, and it will normally go on until the morning. For accommodation, uncle has got the family house ready for those coming from far away, so you don't need to pay for a hotel."),
  L("Κατερίνα", "f", "Α, και κάτι τελευταίο: η νύφη δεν θέλει δώρα, θα έχουν λίστα γάμου σε μια τράπεζα. Πάρε με όταν μπορέσεις!", "Oh, and one last thing: the bride doesn't want presents, they'll have a wedding list at a bank. Call me when you can!"),
 ],
 "questions": [
  Q("Γιατί θέλει η θεία να ξέρει πόσοι θα πάνε;", ["Για να κλείσει δωμάτια σε ξενοδοχείο", "Γιατί το κέντρο ζητάει τον τελικό αριθμό για το φαγητό", "Για να κλείσει εισιτήρια για το πλοίο", "Για να ετοιμάσει τις προσκλήσεις"], 1, "το κέντρο ζητάει τον τελικό αριθμό για το φαγητό"),
  Q("Τι λέει η Κατερίνα για τα εισιτήρια του πλοίου;", ["Ότι είναι πάντα φτηνά", "Ότι θα τα πληρώσει ο θείος", "Ότι ακριβαίνουν πολύ, γι' αυτό καλό είναι να τα κλείσει τώρα", "Ότι το πλοίο του Σαββάτου ακυρώθηκε"], 2, "τα εισιτήρια για το πλοίο του Σαββάτου ακριβαίνουν πολύ, οπότε σου προτείνω να κλείσεις από τώρα"),
  Q("Πού θα μείνουν όσοι έρχονται από μακριά;", ["Σε ξενοδοχείο στο χωριό", "Στο κτήμα του γλεντιού", "Στο σπίτι της Κατερίνας", "Στο πατρικό σπίτι που ετοίμασε ο θείος"], 3, "ο θείος έχει ετοιμάσει το πατρικό σπίτι για όσους έρχονται από μακριά"),
 ],
 "gloss": {"κέντρο": "κέντρο — (reception) venue", "ακριβαίνουν": "ακριβαίνω — to become more expensive", "γλέντι": "γλέντι — party, feast", "κτήμα": "κτήμα — estate", "λυράρηδες": "λυράρης — lyre player", "πατρικό": "πατρικό (σπίτι) — family home", "νύφη": "νύφη — bride", "λίστα γάμου": "λίστα γάμου — wedding list"},
})

ITEMS.append({
 "id": "l187-mon-akouareles", "title": "Ακουαρέλες στα εβδομήντα", "title_en": "Watercolours at seventy", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν συνταξιούχο να μιλά σε μια τοπική εκπομπή για τη ζωγραφική που ξεκίνησε πρόσφατα.",
 "script": [
  L("Σταμάτης", "m", "Δούλεψα σαράντα χρόνια σε τράπεζα. Αριθμοί, αριθμοί, αριθμοί. Όταν βγήκα στη σύνταξη, η κόρη μου μού χάρισε ένα κουτί με ακουαρέλες και ένα μπλοκ. «Μπαμπά, κάτι πρέπει να κάνεις με τα χέρια σου», μου είπε. Γέλασα· στο σχολείο ο δάσκαλος μού έβαζε πάντα χαμηλό βαθμό στα καλλιτεχνικά.", "I worked in a bank for forty years. Numbers, numbers, numbers. When I retired, my daughter gave me a box of watercolours and a sketchpad. 'Dad, you need to do something with your hands,' she told me. I laughed; at school the teacher always gave me a low mark in art."),
  L("Σταμάτης", "m", "Η ακουαρέλα είναι δύσκολη τεχνική, γιατί δεν διορθώνεται. Αν βάλεις πολύ νερό, το χρώμα απλώνεται όπου θέλει. Στην αρχή αυτό με θύμωνε. Μετά κατάλαβα ότι αυτή είναι η ομορφιά της: πρέπει να αφήσεις το νερό να κάνει ένα μέρος της δουλειάς. Για έναν πρώην τραπεζικό υπάλληλο, που ήθελε τα πάντα υπό έλεγχο, ήταν μεγάλο μάθημα.", "Watercolour is a difficult technique, because it can't be corrected. If you add too much water, the colour spreads wherever it likes. At first that made me angry. Then I understood that this is its beauty: you have to let the water do part of the work. For a former bank clerk who wanted everything under control, it was a big lesson."),
  L("Σταμάτης", "m", "Τώρα ζωγραφίζω κάθε πρωί στο μπαλκόνι, πριν ζεστάνει: το βουνό απέναντι, τις γλάστρες, τις γάτες της γειτονιάς. Τον περασμένο μήνα το πνευματικό κέντρο του δήμου έκανε μια έκθεση με έργα ερασιτεχνών, και πούλησα δύο πίνακες. Τα λεφτά τα έδωσα στην εγγονή μου, για να αγοράσει τα δικά της χρώματα.", "Now I paint every morning on the balcony, before it gets hot: the mountain opposite, the flowerpots, the neighbourhood cats. Last month the municipal cultural centre held an exhibition of amateurs' work, and I sold two paintings. I gave the money to my granddaughter, so she could buy her own paints."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε ο Σταμάτης να ζωγραφίζει;", ["Γράφτηκε σε μια σχολή", "Η κόρη του τού χάρισε ένα κουτί με ακουαρέλες", "Τον έπεισε ένας φίλος του", "Το ήθελε από παιδί"], 1, "η κόρη μου μού χάρισε ένα κουτί με ακουαρέλες και ένα μπλοκ"),
  Q("Τι έμαθε από την ακουαρέλα;", ["Να δουλεύει πιο γρήγορα", "Να χρησιμοποιεί λιγότερα χρώματα", "Να αφήνει το νερό να κάνει ένα μέρος της δουλειάς", "Να διορθώνει εύκολα τα λάθη του"], 2, "πρέπει να αφήσεις το νερό να κάνει ένα μέρος της δουλειάς"),
  Q("Τι έκανε με τα λεφτά από τους πίνακες;", ["Αγόρασε καινούργια χρώματα", "Τα έδωσε στο πνευματικό κέντρο", "Πήγε ένα ταξίδι", "Τα έδωσε στην εγγονή του για να αγοράσει χρώματα"], 3, "Τα λεφτά τα έδωσα στην εγγονή μου, για να αγοράσει τα δικά της χρώματα"),
 ],
 "gloss": {"ακουαρέλες": "ακουαρέλα — watercolour", "μπλοκ": "μπλοκ — sketchpad, pad", "καλλιτεχνικά": "καλλιτεχνικά — art (school subject)", "απλώνεται": "απλώνομαι — to spread", "υπό έλεγχο": "υπό έλεγχο — under control", "έκθεση": "έκθεση — exhibition", "ερασιτεχνών": "ερασιτέχνης — amateur"},
})

ITEMS.append({
 "id": "l187-dia-to-aftokinito-ston-gio", "title": "Θα του δώσουμε το αυτοκίνητο;", "title_en": "Shall we let him have the car?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο γονείς να συζητούν αν θα δανείσουν το αυτοκίνητο στον γιο τους, που μόλις πήρε δίπλωμα.",
 "script": [
  L("Ελένη", "f", "Ο Άρης θέλει το αυτοκίνητο το Σάββατο, για να πάει με τους φίλους του στη θάλασσα. Πήρε το δίπλωμα πριν από δέκα μέρες, Θοδωρή.", "Aris wants the car on Saturday, to go to the seaside with his friends. He got his licence ten days ago, Thodoris."),
  L("Θοδωρής", "m", "Ακριβώς γι' αυτό πρέπει να οδηγεί. Αν δεν οδηγήσει τώρα, θα ξεχάσει ό,τι έμαθε. Εμένα ο πατέρας μου μού έδωσε το φορτηγάκι του την επόμενη μέρα από τις εξετάσεις.", "That's exactly why he needs to drive. If he doesn't drive now, he'll forget everything he learned. My father gave me his pick-up the day after my test."),
  L("Ελένη", "f", "Άλλες εποχές, άλλοι δρόμοι. Δεν με ανησυχεί η οδήγηση, με ανησυχούν οι τέσσερις φίλοι μέσα στο αυτοκίνητο, η μουσική στη διαπασών και το κινητό.", "Different times, different roads. It's not the driving that worries me, it's the four friends in the car, the music at full blast and the phone."),
  L("Θοδωρής", "m", "Να του βάλουμε όρους, τότε. Την πρώτη φορά να πάει μόνο με έναν φίλο, όχι στην εθνική οδό, και να γυρίσει πριν νυχτώσει. Αν τα καταφέρει, την επόμενη φορά του δίνουμε περισσότερη ελευθερία.", "Let's set him conditions, then. The first time he goes with just one friend, not on the motorway, and he comes back before dark. If he manages that, next time we give him more freedom."),
  L("Ελένη", "f", "Εντάξει. Και το κινητό στο ντουλαπάκι. Αυτό δεν το συζητάω.", "All right. And the phone in the glove compartment. That's not up for discussion."),
 ],
 "questions": [
  Q("Γιατί πιστεύει ο Θοδωρής ότι ο Άρης πρέπει να οδηγήσει τώρα;", ["Γιατί είναι πολύ καλός οδηγός", "Γιατί αν δεν οδηγήσει τώρα, θα ξεχάσει ό,τι έμαθε", "Γιατί το ζήτησαν οι φίλοι του", "Γιατί ο ίδιος δεν μπορεί να τον πάει"], 1, "Αν δεν οδηγήσει τώρα, θα ξεχάσει ό,τι έμαθε"),
  Q("Τι ανησυχεί κυρίως την Ελένη;", ["Η κατάσταση του αυτοκινήτου", "Ότι ο Άρης δεν ξέρει τον δρόμο", "Οι φίλοι μέσα στο αυτοκίνητο, η δυνατή μουσική και το κινητό", "Το κόστος της βενζίνης"], 2, "με ανησυχούν οι τέσσερις φίλοι μέσα στο αυτοκίνητο, η μουσική στη διαπασών και το κινητό"),
  Q("Ποιον όρο προσθέτει η Ελένη στο τέλος;", ["Να μην οδηγήσει στην εθνική οδό", "Να πάρει μαζί του τον πατέρα του", "Να γυρίσει πριν νυχτώσει", "Να βάλει το κινητό στο ντουλαπάκι"], 3, "Και το κινητό στο ντουλαπάκι"),
 ],
 "gloss": {"δίπλωμα": "δίπλωμα (οδήγησης) — driving licence", "φορτηγάκι": "φορτηγάκι — pick-up, small truck", "διαπασών": "στη διαπασών — at full volume", "όρους": "όρος — condition, term", "εθνική οδό": "εθνική οδός — motorway, national road", "νυχτώσει": "νυχτώνει — it gets dark", "ντουλαπάκι": "ντουλαπάκι — glove compartment"},
})

ITEMS.append({
 "id": "l187-news-timi-elaiolado", "title": "Πέφτει η τιμή του ελαιολάδου", "title_en": "The price of olive oil is falling", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων σε έναν περιφερειακό ραδιοφωνικό σταθμό της Πελοποννήσου.",
 "script": [
  L("Εκφωνητής", "m", "Μετά από δύο χρονιές με τιμές ρεκόρ, η τιμή του ελαιολάδου πέφτει αισθητά φέτος, σύμφωνα με τον συνεταιρισμό ελαιοπαραγωγών της περιοχής. Η αιτία είναι η καλή σοδειά όχι μόνο στην Ελλάδα αλλά και στην Ισπανία, τη μεγαλύτερη παραγωγό χώρα του κόσμου, όπου η ξηρασία είχε μειώσει δραματικά την παραγωγή τα προηγούμενα χρόνια.", "After two years of record prices, the price of olive oil is falling noticeably this year, according to the region's olive growers' cooperative. The reason is the good harvest not only in Greece but also in Spain, the world's largest producer, where drought had dramatically reduced production in previous years."),
  L("Εκφωνητής", "m", "Οι καταναλωτές θα δουν τη διαφορά στα ράφια μέσα στους επόμενους μήνες. Οι παραγωγοί όμως δεν χαίρονται: όπως λένε, το κόστος για λιπάσματα, πετρέλαιο και εργάτες για το μάζεμα παραμένει υψηλό, και με τις νέες τιμές πολλοί μικροί ελαιώνες δεν βγάζουν πια κέρδος.", "Consumers will see the difference on the shelves over the next few months. Producers, however, are not pleased: as they say, the cost of fertiliser, fuel and workers for the harvest remains high, and at the new prices many small olive groves no longer make a profit."),
  L("Εκφωνητής", "m", "Ο συνεταιρισμός ζητά από την πολιτεία ενίσχυση για τους μικρούς παραγωγούς και προτείνει στους καταναλωτές να προτιμούν τυποποιημένο λάδι με σαφή ένδειξη προέλευσης, αντί για χύμα λάδι αγνώστου προέλευσης.", "The cooperative is asking the state for support for small producers and suggests that consumers choose bottled oil with a clear indication of origin, rather than loose oil of unknown origin."),
 ],
 "questions": [
  Q("Γιατί πέφτει φέτος η τιμή του ελαιολάδου;", ["Γιατί μειώθηκαν οι εξαγωγές", "Λόγω καλής σοδειάς στην Ελλάδα και στην Ισπανία", "Γιατί οι καταναλωτές αγοράζουν λιγότερο", "Λόγω νέων φόρων"], 1, "Η αιτία είναι η καλή σοδειά όχι μόνο στην Ελλάδα αλλά και στην Ισπανία"),
  Q("Γιατί δεν χαίρονται οι παραγωγοί;", ["Γιατί η ποιότητα του λαδιού είναι χαμηλή", "Γιατί δεν βρίσκουν αγοραστές", "Γιατί το κόστος παραγωγής παραμένει υψηλό", "Γιατί ο καιρός ήταν κακός"], 2, "το κόστος για λιπάσματα, πετρέλαιο και εργάτες για το μάζεμα παραμένει υψηλό"),
  Q("Τι προτείνει ο συνεταιρισμός στους καταναλωτές;", ["Να αγοράζουν λάδι απευθείας από τον συνεταιρισμό", "Να αγοράζουν περισσότερο λάδι τώρα που είναι φτηνό", "Να προτιμούν χύμα λάδι", "Να προτιμούν τυποποιημένο λάδι με σαφή ένδειξη προέλευσης"], 3, "να προτιμούν τυποποιημένο λάδι με σαφή ένδειξη προέλευσης"),
 ],
 "gloss": {"αισθητά": "αισθητά — noticeably", "συνεταιρισμό": "συνεταιρισμός — cooperative", "σοδειά": "σοδειά — harvest, crop", "λιπάσματα": "λίπασμα — fertiliser", "ελαιώνες": "ελαιώνας — olive grove", "ενίσχυση": "ενίσχυση — support, subsidy", "τυποποιημένο": "τυποποιημένος — bottled, packaged", "χύμα": "χύμα — loose, unpackaged"},
})

ITEMS.append({
 "id": "l187-rep-oreinos-agonas", "title": "Είκοσι πέντε χιλιόμετρα στο βουνό", "title_en": "Twenty-five kilometres on the mountain", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από έναν ορεινό αγώνα δρόμου σε ένα χωριό της Ευρυτανίας.",
 "script": [
  L("Ρεπόρτερ", "m", "Είναι επτά το πρωί και η πλατεία του χωριού είναι γεμάτη δρομείς με φωσφοριζέ παπούτσια και μικρά σακίδια με νερό. Η διαδρομή έχει μήκος είκοσι πέντε χιλιόμετρα και ανεβαίνει σχεδόν χίλια πεντακόσια μέτρα, μέσα από έλατα, πέτρινα γεφύρια και μονοπάτια που χρησιμοποιούσαν παλιά οι βοσκοί.", "It is seven in the morning and the village square is full of runners with fluorescent shoes and small backpacks of water. The course is twenty-five kilometres long and climbs almost one thousand five hundred metres, through firs, stone bridges and paths that shepherds once used."),
  L("Ρεπόρτερ", "m", "Οι διοργανωτές είναι ένας τοπικός σύλλογος, που καθαρίζει και σημαδεύει τα μονοπάτια όλο τον χρόνο. «Ο αγώνας έφερε ζωή στο χωριό», λέει ο πρόεδρος. «Το Σαββατοκύριακο του αγώνα οι ξενώνες είναι γεμάτοι, και πολλοί δρομείς ξαναγυρίζουν το καλοκαίρι με τις οικογένειές τους».", "The organisers are a local association, which clears and marks the paths all year round. 'The race has brought life to the village,' says the president. 'On race weekend the guesthouses are full, and many runners come back in the summer with their families.'"),
  L("Ρεπόρτερ", "m", "Ο νικητής τερματίζει σε λίγο περισσότερο από δυόμισι ώρες. Οι τελευταίοι φτάνουν μετά από επτά ώρες, κουρασμένοι αλλά χαμογελαστοί, και τους υποδέχονται με χειροκροτήματα οι γιαγιάδες του χωριού, που έχουν στήσει ένα τραπέζι με τυρόπιτες και τσάι του βουνού.", "The winner finishes in a little over two and a half hours. The last ones arrive after seven hours, tired but smiling, and are welcomed with applause by the village grandmothers, who have set up a table with cheese pies and mountain tea."),
 ],
 "questions": [
  Q("Από πού περνά η διαδρομή του αγώνα;", ["Από την άσφαλτο του κεντρικού δρόμου", "Από έλατα, πέτρινα γεφύρια και παλιά μονοπάτια βοσκών", "Από τις όχθες μιας λίμνης", "Μόνο από την πλατεία του χωριού"], 1, "μέσα από έλατα, πέτρινα γεφύρια και μονοπάτια που χρησιμοποιούσαν παλιά οι βοσκοί"),
  Q("Πώς έχει βοηθήσει ο αγώνας το χωριό, σύμφωνα με τον πρόεδρο;", ["Χτίστηκε καινούργιος δρόμος", "Άνοιξε σχολείο", "Οι ξενώνες γεμίζουν και πολλοί δρομείς ξαναγυρίζουν το καλοκαίρι", "Ήρθαν νέοι κάτοικοι να μείνουν μόνιμα"], 2, "Το Σαββατοκύριακο του αγώνα οι ξενώνες είναι γεμάτοι, και πολλοί δρομείς ξαναγυρίζουν το καλοκαίρι με τις οικογένειές τους"),
  Q("Ποιοι υποδέχονται τους τελευταίους δρομείς;", ["Ο δήμαρχος", "Οι άλλοι δρομείς", "Τα παιδιά του σχολείου", "Οι γιαγιάδες του χωριού"], 3, "τους υποδέχονται με χειροκροτήματα οι γιαγιάδες του χωριού"),
 ],
 "gloss": {"ορεινό": "ορεινός — mountain (adj.)", "δρομείς": "δρομέας — runner", "φωσφοριζέ": "φωσφοριζέ — fluorescent", "σακίδια": "σακίδιο — backpack", "έλατα": "έλατο — fir", "γεφύρια": "γεφύρι — (stone) bridge", "σημαδεύει": "σημαδεύω — to mark", "τερματίζει": "τερματίζω — to finish (a race)"},
})

ITEMS.append({
 "id": "l187-c1-pos-vriskoun-oi-solomoi-to-potami-tous", "title": "Πώς βρίσκουν οι σολομοί το ποτάμι τους", "title_en": "How salmon find their river", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν θαλάσσιο βιολόγο σε μια επιστημονική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "f", "Είναι αλήθεια ότι οι σολομοί γυρίζουν να γεννήσουν στο ίδιο ποτάμι όπου γεννήθηκαν;", "Is it true that salmon return to spawn in the same river where they were born?"),
  L("Βιολόγος", "m", "Ναι, και μάλιστα συχνά στο ίδιο παρακλάδι του ποταμού. Οι σολομοί γεννιούνται στο γλυκό νερό, κατεβαίνουν στη θάλασσα όταν είναι ακόμα μικροί, περνούν εκεί από ένα ως πέντε χρόνια, ανάλογα με το είδος, και ταξιδεύουν μερικές φορές χιλιάδες χιλιόμετρα. Κι όμως, όταν έρθει η ώρα, οι περισσότεροι βρίσκουν τον δρόμο της επιστροφής με εκπληκτική ακρίβεια.", "Yes, and often to the same tributary of the river. Salmon are born in fresh water, go down to the sea while still young, spend between one and five years there depending on the species, and sometimes travel thousands of kilometres. And yet, when the time comes, most of them find their way back with astonishing accuracy."),
  L("Δημοσιογράφος", "f", "Πώς το καταφέρνουν;", "How do they manage it?"),
  L("Βιολόγος", "m", "Φαίνεται ότι χρησιμοποιούν δύο διαφορετικά «εργαλεία». Στον ανοιχτό ωκεανό προσανατολίζονται κυρίως με το μαγνητικό πεδίο της Γης· κάθε σημείο της ακτής έχει μια χαρακτηριστική μαγνητική «υπογραφή», την οποία οι νεαροί σολομοί φαίνεται να απομνημονεύουν όταν φεύγουν. Όταν πλησιάσουν στις εκβολές, αναλαμβάνει η όσφρηση. Κάθε ποτάμι έχει μια μοναδική χημική μυρωδιά, από το έδαφος, τα φυτά και τα μικρόβιά του, και οι σολομοί τη θυμούνται από τη νεότητά τους. Ήδη από τη δεκαετία του 1950, πειράματα έδειξαν ότι, αν τους φράξει κανείς τη μύτη, χάνουν τον δρόμο.", "It seems they use two different 'tools'. In the open ocean they orient themselves mainly by the Earth's magnetic field; every point on the coast has a characteristic magnetic 'signature', which young salmon seem to memorise when they leave. When they get close to the river mouth, the sense of smell takes over. Every river has a unique chemical scent, from its soil, plants and microbes, and the salmon remember it from their youth. As early as the 1950s, experiments showed that if you block their nostrils, they lose their way."),
  L("Δημοσιογράφος", "f", "Και τι γίνεται μετά την αναπαραγωγή;", "And what happens after spawning?"),
  L("Βιολόγος", "m", "Οι σολομοί του Ειρηνικού πεθαίνουν σχεδόν όλοι λίγο μετά την ωοτοκία, εξαντλημένοι από το ταξίδι κόντρα στο ρεύμα. Τα σώματά τους όμως δεν πάνε χαμένα: λιπαίνουν το ποτάμι και τα δάση γύρω του, και τρέφουν αρκούδες, αετούς και, τελικά, τα ίδια τους τα μικρά. Ο σολομός του Ατλαντικού, αντίθετα, μπορεί να επιστρέψει στη θάλασσα και να ξαναγεννήσει.", "Pacific salmon almost all die shortly after spawning, exhausted by the journey against the current. But their bodies are not wasted: they fertilise the river and the forests around it, and feed bears, eagles and, in the end, their own young. Atlantic salmon, by contrast, can return to the sea and spawn again."),
 ],
 "questions": [
  Q("Πόσο καιρό περνούν οι σολομοί στη θάλασσα;", ["Λίγους μήνες", "Από ένα ως πέντε χρόνια, ανάλογα με το είδος", "Δέκα χρόνια", "Όλη τους τη ζωή"], 1, "περνούν εκεί από ένα ως πέντε χρόνια, ανάλογα με το είδος"),
  Q("Τι χρησιμοποιούν οι σολομοί όταν πλησιάζουν στις εκβολές;", ["Το μαγνητικό πεδίο της Γης", "Τη θέση του ήλιου", "Την όσφρηση", "Τους άλλους σολομούς"], 2, "Όταν πλησιάσουν στις εκβολές, αναλαμβάνει η όσφρηση"),
  Q("Τι λέει ο βιολόγος για τα σώματα των σολομών του Ειρηνικού;", ["Ότι τα τρώνε μόνο οι αρκούδες", "Ότι μολύνουν το ποτάμι", "Ότι τα παρασύρει το ρεύμα στη θάλασσα", "Ότι λιπαίνουν το ποτάμι και τρέφουν πολλά άλλα ζώα"], 3, "λιπαίνουν το ποτάμι και τα δάση γύρω του, και τρέφουν αρκούδες, αετούς και, τελικά, τα ίδια τους τα μικρά"),
 ],
 "gloss": {"σολομοί": "σολομός — salmon", "παρακλάδι": "παρακλάδι — tributary, branch", "προσανατολίζονται": "προσανατολίζομαι — to orient oneself", "απομνημονεύουν": "απομνημονεύω — to memorise", "εκβολές": "εκβολές — river mouth", "όσφρηση": "όσφρηση — sense of smell", "ωοτοκία": "ωοτοκία — spawning, egg-laying", "εξαντλημένοι": "εξαντλημένος — exhausted", "λιπαίνουν": "λιπαίνω — to fertilise"},
})

ITEMS.append({
 "id": "l187-c1-giati-ta-poulia-den-pathainoun-ilektroplixia", "title": "Γιατί τα πουλιά στα καλώδια δεν παθαίνουν ηλεκτροπληξία", "title_en": "Why birds on power lines don't get electrocuted", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ηλεκτρολόγο μηχανικό να απαντά σε ερώτηση ακροατή για την ηλεκτροπληξία σε μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Μηχανικός", "m", "Η ερώτηση είναι πολύ καλή, γιατί τα καλώδια της μέσης τάσης έχουν χιλιάδες βολτ. Το μυστικό είναι ότι το ηλεκτρικό ρεύμα δεν κυλά απλώς επειδή υπάρχει τάση· κυλά όταν υπάρχει διαφορά δυναμικού ανάμεσα σε δύο σημεία και ένας δρόμος που τα ενώνει. Ένα πουλί που κάθεται με τα δύο πόδια πάνω σε ένα μόνο καλώδιο βρίσκεται ολόκληρο στο ίδιο δυναμικό. Δεν υπάρχει διαφορά ανάμεσα στο ένα πόδι και στο άλλο, άρα το ρεύμα συνεχίζει τον δρόμο του μέσα στο μέταλλο, που είναι άλλωστε πολύ καλύτερος αγωγός από το σώμα του πουλιού.", "The question is a very good one, because medium-voltage lines carry thousands of volts. The secret is that electric current does not flow simply because there is voltage; it flows when there is a potential difference between two points and a path connecting them. A bird sitting with both feet on a single wire is entirely at the same potential. There is no difference between one foot and the other, so the current continues on its way through the metal, which is in any case a far better conductor than the bird's body."),
  L("Μηχανικός", "m", "Το πρόβλημα αρχίζει όταν το πουλί ακουμπήσει ταυτόχρονα δύο καλώδια ή ένα καλώδιο και τη γειωμένη κολόνα. Τότε το σώμα του γίνεται η γέφυρα ανάμεσα σε δύο διαφορετικά δυναμικά, και το αποτέλεσμα είναι μοιραίο. Γι' αυτό κινδυνεύουν κυρίως τα μεγάλα πουλιά, όπως οι πελαργοί, οι αετοί και οι γύπες, που με τα ανοιχτά τους φτερά μπορούν να καλύψουν την απόσταση ανάμεσα στους αγωγούς.", "The problem starts when the bird touches two wires at the same time, or a wire and the earthed pole. Then its body becomes the bridge between two different potentials, and the result is fatal. That is why it is mainly large birds that are at risk, such as storks, eagles and vultures, which with their wings spread can span the distance between the conductors."),
  L("Μηχανικός", "m", "Σε πολλές περιοχές, οι εταιρείες ηλεκτρισμού τοποθετούν πλέον μονωτικά καλύμματα στις κολόνες ή ειδικές βάσεις για φωλιές, πιο ψηλά από τους αγωγούς, ώστε οι πελαργοί να μη χτίζουν πάνω στα καλώδια. Και μια συμβουλή για εμάς: αν δείτε πεσμένο καλώδιο, μην πλησιάσετε. Εμείς, σε αντίθεση με τα πουλιά, πατάμε στο έδαφος.", "In many areas, electricity companies now fit insulating covers on poles or special nesting platforms, higher than the conductors, so that storks do not build on the wires. And a piece of advice for us: if you see a fallen cable, do not go near it. We, unlike birds, are standing on the ground."),
 ],
 "questions": [
  Q("Γιατί δεν παθαίνει τίποτα ένα πουλί πάνω σε ένα καλώδιο;", ["Γιατί τα πόδια του είναι μονωμένα από φτερά", "Γιατί όλο το σώμα του βρίσκεται στο ίδιο δυναμικό", "Γιατί το ρεύμα είναι πολύ ασθενές", "Γιατί τα καλώδια είναι πάντα μονωμένα"], 1, "βρίσκεται ολόκληρο στο ίδιο δυναμικό"),
  Q("Γιατί κινδυνεύουν κυρίως τα μεγάλα πουλιά;", ["Γιατί είναι βαρύτερα", "Γιατί πετούν πιο ψηλά", "Γιατί με τα ανοιχτά φτερά μπορούν να ακουμπήσουν δύο αγωγούς", "Γιατί χτίζουν φωλιές μακριά από τις κολόνες"], 2, "με τα ανοιχτά τους φτερά μπορούν να καλύψουν την απόσταση ανάμεσα στους αγωγούς"),
  Q("Τι συμβουλεύει ο μηχανικός τους ακροατές;", ["Να διώχνουν τα πουλιά από τα καλώδια", "Να καλούν την εταιρεία όταν δουν φωλιά", "Να μην αγγίζουν τις κολόνες", "Να μην πλησιάζουν ένα πεσμένο καλώδιο"], 3, "αν δείτε πεσμένο καλώδιο, μην πλησιάσετε"),
 ],
 "gloss": {"ηλεκτροπληξία": "ηλεκτροπληξία — electric shock, electrocution", "τάσης": "τάση — voltage", "διαφορά δυναμικού": "διαφορά δυναμικού — potential difference", "αγωγός": "αγωγός — conductor", "γειωμένη": "γειωμένος — earthed, grounded", "μοιραίο": "μοιραίος — fatal", "πελαργοί": "πελαργός — stork", "γύπες": "γύπας — vulture", "μονωτικά": "μονωτικός — insulating"},
})

ITEMS.append({
 "id": "l187-rep-katafygio-adespoton", "title": "Μια μέρα στο καταφύγιο αδέσποτων", "title_en": "A day at the stray-animal shelter", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από ένα καταφύγιο για αδέσποτα ζώα έξω από μια πόλη, όπου δουλεύουν εθελοντές.",
 "script": [
  L("Ρεπόρτερ", "f", "Στις οχτώ το πρωί, πριν φτάσουμε καν στην πόρτα, ακούμε τα γαβγίσματα. Στο καταφύγιο ζουν αυτή τη στιγμή εκατόν είκοσι σκύλοι και περίπου σαράντα γάτες. Οι περισσότεροι βρέθηκαν παρατημένοι σε δρόμους ή σε χωράφια, μερικοί με σοβαρά τραύματα.", "At eight in the morning, before we even reach the gate, we hear the barking. At the moment a hundred and twenty dogs and about forty cats live at the shelter. Most were found abandoned on roads or in fields, some with serious injuries."),
  L("Ρεπόρτερ", "f", "Η μέρα ξεκινά με καθάρισμα και τάισμα. Οι εθελοντές, φοιτητές, συνταξιούχοι και εργαζόμενοι που έρχονται πριν από τη δουλειά τους, έχουν ο καθένας τα «δικά του» ζώα. «Ο Μπόμπος ήταν τόσο φοβισμένος όταν ήρθε, που δεν έτρωγε μπροστά σε άνθρωπο», λέει η Νεφέλη. «Χρειάστηκαν δύο μήνες για να μου φάει από το χέρι».", "The day begins with cleaning and feeding. The volunteers, students, pensioners and working people who come before their jobs, each have their 'own' animals. 'Bobos was so frightened when he arrived that he wouldn't eat in front of a person,' says Nefeli. 'It took two months for him to eat from my hand.'"),
  L("Ρεπόρτερ", "f", "Κάθε Κυριακή το καταφύγιο ανοίγει για το κοινό. Όποιος θέλει μπορεί να βγάλει έναν σκύλο βόλτα, και πολλές υιοθεσίες ξεκινούν ακριβώς έτσι. Πριν δοθεί ένα ζώο, οι εθελοντές επισκέπτονται το σπίτι της νέας οικογένειας. «Δεν θέλουμε να ξαναγυρίσει κανένα εδώ», εξηγεί η υπεύθυνη.", "Every Sunday the shelter opens to the public. Anyone who wants can take a dog for a walk, and many adoptions start exactly that way. Before an animal is handed over, the volunteers visit the new family's home. 'We don't want any of them to come back here,' the manager explains."),
 ],
 "questions": [
  Q("Πού βρέθηκαν τα περισσότερα ζώα του καταφυγίου;", ["Σε άλλα καταφύγια", "Παρατημένα σε δρόμους ή σε χωράφια", "Σε καταστήματα κατοικίδιων", "Σε σπίτια ηλικιωμένων"], 1, "Οι περισσότεροι βρέθηκαν παρατημένοι σε δρόμους ή σε χωράφια"),
  Q("Τι λέει η Νεφέλη για τον Μπόμπο;", ["Ότι ήταν επιθετικός", "Ότι υιοθετήθηκε αμέσως", "Ότι χρειάστηκαν δύο μήνες για να φάει από το χέρι της", "Ότι ήταν άρρωστος"], 2, "Χρειάστηκαν δύο μήνες για να μου φάει από το χέρι"),
  Q("Τι κάνουν οι εθελοντές πριν δώσουν ένα ζώο για υιοθεσία;", ["Ζητούν χρήματα", "Κάνουν συνέντευξη στο τηλέφωνο", "Ζητούν συστάσεις από κτηνίατρο", "Επισκέπτονται το σπίτι της νέας οικογένειας"], 3, "οι εθελοντές επισκέπτονται το σπίτι της νέας οικογένειας"),
 ],
 "gloss": {"αδέσποτα": "αδέσποτος — stray", "γαβγίσματα": "γάβγισμα — barking", "παρατημένοι": "παρατημένος — abandoned", "τραύματα": "τραύμα — injury, wound", "τάισμα": "τάισμα — feeding", "υιοθεσίες": "υιοθεσία — adoption"},
})

rnd = random.Random(187)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-187.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
