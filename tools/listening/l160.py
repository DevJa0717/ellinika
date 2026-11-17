# Source for library/listening/listening-160.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l160.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l160-ann-agora", "title": "Ανακοίνωση στη δημοτική αγορά", "title_en": "An announcement at the municipal market", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα μιας σκεπαστής δημοτικής αγοράς.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί πελάτες, καλημέρα σας. Σας ενημερώνουμε ότι από την ερχόμενη Δευτέρα η αγορά θα λειτουργεί και τα απογεύματα, από τις πέντε ως τις εννιά, εκτός από την Τετάρτη και το Σάββατο.", "Dear customers, good morning. Please note that from next Monday the market will also be open in the afternoons, from five to nine, except on Wednesday and Saturday."),
  L("Εκφωνητής", "m", "Λόγω των εργασιών στη στέγη, η πτέρυγα με τα ψάρια μεταφέρεται προσωρινά στον εσωτερικό χώρο δίπλα στην είσοδο της οδού Ερμού. Οι πάγκοι με τα φρούτα και τα λαχανικά παραμένουν στη θέση τους.", "Because of the work on the roof, the fish section is temporarily moving to the indoor area next to the entrance on Ermou Street. The fruit and vegetable stalls stay where they are."),
  L("Εκφωνητής", "m", "Υπενθυμίζουμε ότι η αγορά δεν δίνει πλέον πλαστικές σακούλες. Υφασμάτινες τσάντες μπορείτε να αγοράσετε στο γραφείο πληροφοριών με ένα ευρώ, και για κάθε αγορά πάνω από είκοσι ευρώ η τσάντα δίνεται δωρεάν.", "We remind you that the market no longer gives out plastic bags. You can buy cloth bags at the information desk for one euro, and for every purchase over twenty euros the bag is given free."),
 ],
 "questions": [
  Q("Ποιες μέρες ΔΕΝ θα λειτουργεί η αγορά το απόγευμα;", ["Δευτέρα και Παρασκευή", "Τετάρτη και Σάββατο", "Τρίτη και Πέμπτη", "Μόνο την Κυριακή"], 1, "εκτός από την Τετάρτη και το Σάββατο"),
  Q("Γιατί μεταφέρεται η πτέρυγα με τα ψάρια;", ["Λόγω των εργασιών στη στέγη", "Γιατί χάλασαν τα ψυγεία", "Γιατί θα έρθουν νέοι πάγκοι", "Για λόγους υγιεινής"], 0, "Λόγω των εργασιών στη στέγη"),
  Q("Πότε δίνεται δωρεάν η υφασμάτινη τσάντα;", ["Σε όλους τους πελάτες", "Τις Δευτέρες", "Για κάθε αγορά πάνω από είκοσι ευρώ", "Σε όσους φέρνουν πλαστική σακούλα"], 2, "για κάθε αγορά πάνω από είκοσι ευρώ η τσάντα δίνεται δωρεάν"),
 ],
 "gloss": {"σκεπαστής": "σκεπαστός — covered, roofed", "δημοτικής αγοράς": "δημοτική αγορά — municipal market", "στέγη": "στέγη — roof", "πτέρυγα": "πτέρυγα — wing, section", "προσωρινά": "προσωρινά — temporarily", "πάγκοι": "πάγκος — stall, counter", "σακούλες": "σακούλα — bag", "Υφασμάτινες": "υφασμάτινος — (made of) cloth"},
})

ITEMS.append({
 "id": "l160-int-meteorites", "title": "Ο κυνηγός μετεωριτών", "title_en": "The meteorite hunter", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν ερασιτέχνη που ψάχνει μετεωρίτες στον ελεύθερο χρόνο του.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς ξεκινήσατε να ψάχνετε πέτρες από το διάστημα;", "How did you start looking for stones from space?"),
  L("Ερασιτέχνης", "m", "Από περιέργεια. Είδα κάποτε σε ένα μουσείο έναν μετεωρίτη που μπορούσες να τον αγγίξεις και σκέφτηκα ότι κρατούσα στο χέρι κάτι πιο παλιό από τη Γη. Οι περισσότεροι μετεωρίτες είναι κομμάτια από αστεροειδείς, ηλικίας περίπου τεσσεράμισι δισεκατομμυρίων χρόνων.", "Out of curiosity. I once saw a meteorite in a museum that you could touch, and I thought I was holding something older than the Earth. Most meteorites are pieces of asteroids, about four and a half billion years old."),
  L("Δημοσιογράφος", "f", "Πού τους βρίσκει κανείς;", "Where does one find them?"),
  L("Ερασιτέχνης", "m", "Πέφτουν παντού, αλλά βρίσκονται πιο εύκολα σε ερήμους και στους πάγους της Ανταρκτικής, όπου μια σκούρα πέτρα ξεχωρίζει αμέσως. Εδώ, σε ένα χωράφι, είναι σχεδόν αδύνατο να τους ξεχωρίσεις από τις κοινές πέτρες.", "They fall everywhere, but they're found more easily in deserts and on the ice of Antarctica, where a dark stone stands out immediately. Here, in a field, it's almost impossible to tell them apart from ordinary stones."),
  L("Δημοσιογράφος", "f", "Πώς καταλαβαίνετε ότι μια πέτρα είναι μετεωρίτης;", "How can you tell that a stone is a meteorite?"),
  L("Ερασιτέχνης", "m", "Οι περισσότεροι περιέχουν σίδηρο, οπότε ένας μαγνήτης κολλάει πάνω τους, και είναι βαρύτεροι απ' όσο περιμένεις για το μέγεθός τους. Έχουν συχνά και μια λεπτή μαύρη κρούστα, από το κάψιμο στην ατμόσφαιρα. Πάντως, εννιά στις δέκα πέτρες που μου φέρνουν οι γείτονες είναι απλώς σκουριές από παλιά σίδερα.", "Most contain iron, so a magnet sticks to them, and they are heavier than you would expect for their size. They often also have a thin black crust, from burning in the atmosphere. Still, nine out of ten stones the neighbours bring me are just slag from old iron."),
 ],
 "questions": [
  Q("Τι είναι οι περισσότεροι μετεωρίτες, σύμφωνα με τον ερασιτέχνη;", ["Κομμάτια από τη Σελήνη", "Κομμάτια από αστεροειδείς", "Λάβα από ηφαίστεια", "Κομμάτια από δορυφόρους"], 1, "Οι περισσότεροι μετεωρίτες είναι κομμάτια από αστεροειδείς"),
  Q("Γιατί βρίσκονται πιο εύκολα σε ερήμους και στην Ανταρκτική;", ["Γιατί πέφτουν μόνο εκεί", "Γιατί εκεί μια σκούρα πέτρα ξεχωρίζει αμέσως", "Γιατί εκεί υπάρχουν πολλοί ερευνητές", "Γιατί εκεί δεν λιώνουν"], 1, "όπου μια σκούρα πέτρα ξεχωρίζει αμέσως"),
  Q("Τι είναι συνήθως οι πέτρες που του φέρνουν οι γείτονες;", ["Πραγματικοί μετεωρίτες", "Αρχαία εργαλεία", "Σκουριές από παλιά σίδερα", "Κομμάτια από τούβλα"], 2, "είναι απλώς σκουριές από παλιά σίδερα"),
 ],
 "gloss": {"ερασιτέχνη": "ερασιτέχνης — amateur", "μετεωρίτες": "μετεωρίτης — meteorite", "διάστημα": "διάστημα — (outer) space", "περιέργεια": "περιέργεια — curiosity", "αστεροειδείς": "αστεροειδής — asteroid", "ερήμους": "έρημος — desert", "πάγους": "πάγος — ice", "ξεχωρίζει": "ξεχωρίζω — to stand out; to tell apart", "μαγνήτης": "μαγνήτης — magnet", "κρούστα": "κρούστα — crust", "σκουριές": "σκουριά — slag; rust"},
})

ITEMS.append({
 "id": "l160-int-kaskanter", "title": "Μια κασκαντέρ στον κινηματογράφο", "title_en": "A stuntwoman in the cinema", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που δουλεύει ως κασκαντέρ σε ταινίες και σειρές.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς γίνεται κανείς κασκαντέρ;", "How does one become a stunt performer?"),
  L("Κασκαντέρ", "f", "Οι περισσότεροι από εμάς ερχόμαστε από τον αθλητισμό. Εγώ έκανα ενόργανη γυμναστική δώδεκα χρόνια. Μετά έμαθα να πέφτω από σκάλες, να οδηγώ μηχανή και να παίζω σκηνές πάλης χωρίς να χτυπάω κανέναν.", "Most of us come from sport. I did artistic gymnastics for twelve years. Then I learned to fall down stairs, ride a motorbike and act fight scenes without hitting anyone."),
  L("Δημοσιογράφος", "m", "Δεν φοβάστε;", "Aren't you afraid?"),
  L("Κασκαντέρ", "f", "Ο φόβος είναι χρήσιμος· σε κάνει προσεκτικό. Κάθε σκηνή την προβάρουμε ξανά και ξανά, πρώτα αργά, με στρώματα και σχοινιά. Αυτό που ο θεατής βλέπει να διαρκεί τρία δευτερόλεπτα έχει πίσω του μέρες προετοιμασίας.", "Fear is useful; it makes you careful. We rehearse every scene again and again, slowly at first, with mats and ropes. What the viewer sees lasting three seconds has days of preparation behind it."),
  L("Δημοσιογράφος", "m", "Σας αναγνωρίζει ποτέ ο κόσμος;", "Do people ever recognise you?"),
  L("Κασκαντέρ", "f", "Σχεδόν ποτέ, και αυτό είναι το νόημα: αν ο θεατής καταλάβει ότι δεν είναι η πρωταγωνίστρια, έχω κάνει κακή δουλειά. Φοράω την ίδια περούκα και τα ίδια ρούχα, και η κάμερα με τραβάει από πίσω ή από μακριά.", "Almost never, and that's the point: if the viewer realises it isn't the leading actress, I've done a bad job. I wear the same wig and the same clothes, and the camera films me from behind or from far away."),
 ],
 "questions": [
  Q("Από πού έρχονται οι περισσότεροι κασκαντέρ, σύμφωνα με τη συνομιλήτρια;", ["Από το θέατρο", "Από τον αθλητισμό", "Από τον στρατό", "Από το τσίρκο"], 1, "Οι περισσότεροι από εμάς ερχόμαστε από τον αθλητισμό"),
  Q("Γιατί θεωρεί τον φόβο χρήσιμο;", ["Γιατί κάνει τις σκηνές πιο αληθινές", "Γιατί σε κάνει προσεκτικό", "Γιατί βοηθάει να τρέχεις γρήγορα", "Γιατί αρέσει στους σκηνοθέτες"], 1, "σε κάνει προσεκτικό"),
  Q("Πότε θεωρεί ότι έχει κάνει κακή δουλειά;", ["Όταν χτυπήσει", "Όταν η σκηνή κρατήσει πολύ", "Όταν ο θεατής καταλάβει ότι δεν είναι η πρωταγωνίστρια", "Όταν χρειαστεί δεύτερη λήψη"], 2, "αν ο θεατής καταλάβει ότι δεν είναι η πρωταγωνίστρια, έχω κάνει κακή δουλειά"),
 ],
 "gloss": {"κασκαντέρ": "κασκαντέρ — stunt performer", "ενόργανη γυμναστική": "ενόργανη γυμναστική — artistic gymnastics", "πάλης": "πάλη — fight, wrestling", "προβάρουμε": "προβάρω — to rehearse", "στρώματα": "στρώμα — mat, mattress", "σχοινιά": "σχοινί — rope", "προετοιμασίας": "προετοιμασία — preparation", "πρωταγωνίστρια": "πρωταγωνίστρια — leading actress", "περούκα": "περούκα — wig", "τραβάει": "τραβάω — to film; to pull"},
})

ITEMS.append({
 "id": "l160-dia-toursi", "title": "Τουρσί από τον κήπο", "title_en": "Pickles from the garden", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέρφια να συζητούν τι θα κάνουν με τα πολλά λαχανικά του κήπου τους.",
 "script": [
  L("Αλέκα", "f", "Ο κήπος φέτος μας τρέλανε. Έχουμε τόσες πιπεριές και τόσα αγγούρια που δεν θα τα φάμε ποτέ.", "The garden has gone mad this year. We have so many peppers and cucumbers that we'll never eat them all."),
  L("Στέλιος", "m", "Να τα κάνουμε τουρσί, όπως η μάνα μας. Θυμάσαι τα βάζα στο κελάρι;", "Let's pickle them, like our mother did. Remember the jars in the cellar?"),
  L("Αλέκα", "f", "Θυμάμαι, αλλά δεν θυμάμαι τις αναλογίες. Πόσο ξίδι και πόσο αλάτι;", "I remember, but I don't remember the proportions. How much vinegar and how much salt?"),
  L("Στέλιος", "m", "Τη ρώτησα χθες στο τηλέφωνο. Ένα ποτήρι ξίδι για κάθε δύο ποτήρια νερό, και μια κουταλιά αλάτι χοντρό. Λίγο σκόρδο, λίγο σέλινο, και τα βάζα πρέπει πρώτα να τα βράσουμε, για να μη μουχλιάσουν.", "I asked her yesterday on the phone. One glass of vinegar for every two glasses of water, and a spoonful of coarse salt. A little garlic, a little celery, and we have to boil the jars first so they don't go mouldy."),
  L("Αλέκα", "f", "Και πότε τρώγονται;", "And when can you eat them?"),
  L("Στέλιος", "m", "Θέλουν τουλάχιστον τρεις εβδομάδες σε δροσερό και σκοτεινό μέρος. Αν τα ανοίξουμε νωρίτερα, θα είναι ακόμη άνοστα. Τα Χριστούγεννα θα είναι τέλεια, με τα φασόλια.", "They need at least three weeks in a cool, dark place. If we open them earlier, they'll still be tasteless. At Christmas they'll be perfect, with the beans."),
 ],
 "questions": [
  Q("Τι πρότεινε ο Στέλιος να κάνουν με τα λαχανικά;", ["Να τα πουλήσουν", "Να τα κάνουν τουρσί", "Να τα μοιράσουν στους γείτονες", "Να τα καταψύξουν"], 1, "Να τα κάνουμε τουρσί"),
  Q("Γιατί πρέπει να βράσουν πρώτα τα βάζα;", ["Για να μη σπάσουν", "Για να μη μουχλιάσουν", "Για να κλείνουν καλά", "Για να μείνει το χρώμα"], 1, "για να μη μουχλιάσουν"),
  Q("Πόσο καιρό χρειάζεται το τουρσί πριν φαγωθεί;", ["Μία μέρα", "Μία εβδομάδα", "Τουλάχιστον τρεις εβδομάδες", "Έξι μήνες"], 2, "Θέλουν τουλάχιστον τρεις εβδομάδες σε δροσερό και σκοτεινό μέρος"),
 ],
 "gloss": {"τουρσί": "τουρσί — pickle(s)", "αγγούρια": "αγγούρι — cucumber", "βάζα": "βάζο — jar", "κελάρι": "κελάρι — cellar, larder", "αναλογίες": "αναλογία — proportion", "ξίδι": "ξίδι — vinegar", "χοντρό": "χοντρός — coarse; thick", "σέλινο": "σέλινο — celery", "μουχλιάσουν": "μουχλιάζω — to go mouldy", "δροσερό": "δροσερός — cool", "άνοστα": "άνοστος — tasteless"},
})

ITEMS.append({
 "id": "l160-dia-didymides", "title": "Πάμε να δούμε τις Διδυμίδες;", "title_en": "Shall we go and see the Geminids?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους να κανονίζουν μια βραδιά παρατήρησης των διαττόντων αστέρων τον Δεκέμβριο.",
 "script": [
  L("Πέτρος", "m", "Διάβασα ότι στα μέσα Δεκεμβρίου έχουμε τις Διδυμίδες, μια από τις πιο πλούσιες βροχές διαττόντων της χρονιάς. Λέω να ανέβουμε στο βουνό.", "I read that in mid-December we have the Geminids, one of the richest meteor showers of the year. I'm thinking we go up the mountain."),
  L("Ιωάννα", "f", "Τον Δεκέμβριο; Θα ξεπαγιάσουμε! Γιατί δεν πάμε τον Αύγουστο, που είναι ζέστη;", "In December? We'll freeze! Why don't we go in August, when it's warm?"),
  L("Πέτρος", "m", "Τον Αύγουστο είναι άλλη βροχή. Αυτή γίνεται μόνο τώρα. Και το καλό είναι ότι φέτος η Σελήνη δεν θα είναι γεμάτη, οπότε ο ουρανός θα είναι σκοτεινός.", "In August it's a different shower. This one only happens now. And the good thing is that this year the Moon won't be full, so the sky will be dark."),
  L("Ιωάννα", "f", "Και πρέπει να έχουμε τηλεσκόπιο;", "And do we need a telescope?"),
  L("Πέτρος", "m", "Καθόλου. Τα μάτια σου είναι το καλύτερο όργανο, γιατί βλέπεις όλο τον ουρανό μαζί. Το μόνο που θέλει είναι να μην κοιτάς το κινητό, ώστε να συνηθίσουν τα μάτια στο σκοτάδι.", "Not at all. Your eyes are the best instrument, because you see the whole sky at once. All it takes is not looking at your phone, so that your eyes get used to the dark."),
  L("Ιωάννα", "f", "Καλά, έρχομαι. Αλλά φέρνω δύο κουβέρτες κι ένα θερμός με τσάι.", "Fine, I'm coming. But I'm bringing two blankets and a thermos of tea."),
 ],
 "questions": [
  Q("Γιατί διστάζει αρχικά η Ιωάννα;", ["Γιατί δεν της αρέσει το βουνό", "Γιατί φοβάται ότι θα κάνει πολύ κρύο", "Γιατί δουλεύει το βράδυ", "Γιατί δεν έχει αυτοκίνητο"], 1, "Θα ξεπαγιάσουμε"),
  Q("Γιατί, κατά τον Πέτρο, θα είναι καλή η φετινή παρατήρηση;", ["Γιατί θα έχει πανσέληνο", "Γιατί η Σελήνη δεν θα είναι γεμάτη και ο ουρανός θα είναι σκοτεινός", "Γιατί θα έχουν τηλεσκόπιο", "Γιατί δεν θα έχει σύννεφα όλο τον μήνα"], 1, "η Σελήνη δεν θα είναι γεμάτη, οπότε ο ουρανός θα είναι σκοτεινός"),
  Q("Γιατί δεν πρέπει να κοιτάζουν το κινητό;", ["Για να μην τελειώσει η μπαταρία", "Για να μην ενοχλούν τους άλλους", "Για να συνηθίσουν τα μάτια στο σκοτάδι", "Γιατί δεν έχει σήμα στο βουνό"], 2, "ώστε να συνηθίσουν τα μάτια στο σκοτάδι"),
 ],
 "gloss": {"διαττόντων αστέρων": "διάττων αστέρας — shooting star, meteor", "Διδυμίδες": "Διδυμίδες — the Geminids (meteor shower)", "βροχές διαττόντων": "βροχή διαττόντων — meteor shower", "ξεπαγιάσουμε": "ξεπαγιάζω — to freeze (with cold)", "Σελήνη": "Σελήνη — the Moon", "τηλεσκόπιο": "τηλεσκόπιο — telescope", "όργανο": "όργανο — instrument", "συνηθίσουν": "συνηθίζω — to get used to", "κουβέρτες": "κουβέρτα — blanket", "θερμός": "θερμός — thermos (flask)"},
})

ITEMS.append({
 "id": "l160-mon-perouka", "title": "Ο περουκιέρης του θεάτρου", "title_en": "The theatre wigmaker", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα που φτιάχνει περούκες για το θέατρο να μιλάει για τη δουλειά του σε μια εκπομπή.",
 "script": [
  L("Περουκιέρης", "m", "Μια καλή περούκα θέλει από σαράντα ως ογδόντα ώρες δουλειάς. Τις τρίχες τις περνάω μία προς μία, ή ανά δύο, σε ένα λεπτό δίχτυ που έχει πάρει το σχήμα του κεφαλιού του ηθοποιού. Γι' αυτό πρώτα παίρνω μέτρα, όπως ο ράφτης.", "A good wig takes from forty to eighty hours of work. I thread the hairs one at a time, or in pairs, into a fine net that has taken the shape of the actor's head. That's why I first take measurements, like a tailor."),
  L("Περουκιέρης", "m", "Για τις παραστάσεις προτιμώ αληθινά μαλλιά. Οι συνθετικές περούκες γυαλίζουν κάτω από τους προβολείς και λιώνουν αν πλησιάσεις ζεστό σίδερο. Τα αληθινά μαλλιά τα χτενίζεις, τα βάφεις, τα κατσαρώνεις, και κρατάνε χρόνια.", "For performances I prefer real hair. Synthetic wigs shine under the spotlights and melt if you bring a hot iron near them. Real hair you can comb, dye and curl, and it lasts for years."),
  L("Περουκιέρης", "m", "Το πιο δύσκολο είναι να μη φαίνεται η άκρη στο μέτωπο. Εκεί το δίχτυ είναι σχεδόν διάφανο, και πριν από κάθε παράσταση το κολλάω με ειδική κόλλα για το δέρμα. Όταν από την πρώτη σειρά κανείς δεν καταλαβαίνει ότι ο βασιλιάς φοράει περούκα, τότε είμαι ευχαριστημένος.", "The hardest thing is to keep the edge on the forehead from showing. There the net is almost transparent, and before every performance I glue it with special skin glue. When nobody in the front row realises that the king is wearing a wig, then I'm satisfied."),
 ],
 "questions": [
  Q("Πόσες ώρες δουλειάς θέλει μια καλή περούκα;", ["Από τέσσερις ως οκτώ", "Από σαράντα ως ογδόντα", "Περίπου διακόσιες", "Μία μέρα"], 1, "Μια καλή περούκα θέλει από σαράντα ως ογδόντα ώρες δουλειάς"),
  Q("Γιατί προτιμά αληθινά μαλλιά για τις παραστάσεις;", ["Γιατί είναι φθηνότερα", "Γιατί οι συνθετικές περούκες γυαλίζουν κάτω από τους προβολείς και λιώνουν με τη ζέστη", "Γιατί είναι πιο ελαφριά", "Γιατί τα ζητούν οι σκηνοθέτες"], 1, "Οι συνθετικές περούκες γυαλίζουν κάτω από τους προβολείς"),
  Q("Ποιο είναι το πιο δύσκολο μέρος της δουλειάς του;", ["Να βρει αληθινά μαλλιά", "Να βάψει τα μαλλιά", "Να μη φαίνεται η άκρη στο μέτωπο", "Να πάρει μέτρα"], 2, "Το πιο δύσκολο είναι να μη φαίνεται η άκρη στο μέτωπο"),
 ],
 "gloss": {"περούκες": "περούκα — wig", "τρίχες": "τρίχα — (a single) hair", "δίχτυ": "δίχτυ — net", "ράφτης": "ράφτης — tailor", "συνθετικές": "συνθετικός — synthetic", "γυαλίζουν": "γυαλίζω — to shine", "προβολείς": "προβολέας — spotlight", "κατσαρώνεις": "κατσαρώνω — to curl", "μέτωπο": "μέτωπο — forehead", "διάφανο": "διάφανος — transparent", "κόλλα": "κόλλα — glue"},
})

ITEMS.append({
 "id": "l160-vm-kiniti", "title": "Μήνυμα από την κινητή βιβλιοθήκη", "title_en": "A message from the mobile library", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη βιβλιοθηκονόμο της κινητής βιβλιοθήκης του δήμου.",
 "script": [
  L("Βιβλιοθηκονόμος", "f", "Καλησπέρα σας, κυρία Ραφαηλίδου, σας τηλεφωνώ από την κινητή βιβλιοθήκη του δήμου. Το βιβλίο που είχατε ζητήσει, το μυθιστόρημα με τις μεγάλες γραμματοσειρές, έφτασε επιτέλους από την κεντρική βιβλιοθήκη.", "Good afternoon, Mrs Rafailidou, I'm calling from the municipal mobile library. The book you had asked for, the large-print novel, has finally arrived from the central library."),
  L("Βιβλιοθηκονόμος", "f", "Το λεωφορείο μας δεν θα περάσει από το χωριό σας την Πέμπτη, όπως συνήθως, γιατί έχουμε βλάβη στη μηχανή. Θα έρθουμε το Σάββατο το πρωί, από τις δέκα ως τις δώδεκα, στην πλατεία δίπλα στο καφενείο.", "Our bus won't come through your village on Thursday as usual, because we have an engine fault. We'll come on Saturday morning, from ten to twelve, to the square next to the café."),
  L("Βιβλιοθηκονόμος", "f", "Αν δεν μπορείτε να έρθετε, πείτε μου και θα σας το αφήσει ο εγγονός σας στο σπίτι, αφού μου είπατε ότι κι εκείνος είναι μέλος. Θυμίζω επίσης ότι έχετε ακόμη δύο βιβλία από τον προηγούμενο μήνα· δεν υπάρχει πρόστιμο, αλλά τα περιμένει άλλος αναγνώστης.", "If you can't come, let me know and your grandson can drop it off at your house, since you told me he is a member too. I also remind you that you still have two books from last month; there's no fine, but another reader is waiting for them."),
 ],
 "questions": [
  Q("Γιατί δεν θα έρθει το λεωφορείο την Πέμπτη;", ["Λόγω απεργίας", "Γιατί έχει βλάβη στη μηχανή", "Γιατί είναι αργία", "Λόγω κακοκαιρίας"], 1, "γιατί έχουμε βλάβη στη μηχανή"),
  Q("Πού θα σταματήσει το λεωφορείο το Σάββατο;", ["Μπροστά στο σχολείο", "Στην πλατεία δίπλα στο καφενείο", "Στο σπίτι της κυρίας Ραφαηλίδου", "Στην κεντρική βιβλιοθήκη"], 1, "στην πλατεία δίπλα στο καφενείο"),
  Q("Τι λέει η βιβλιοθηκονόμος για τα δύο βιβλία του προηγούμενου μήνα;", ["Ότι υπάρχει πρόστιμο", "Ότι μπορεί να τα κρατήσει όσο θέλει", "Ότι δεν υπάρχει πρόστιμο, αλλά τα περιμένει άλλος αναγνώστης", "Ότι χάθηκαν"], 2, "δεν υπάρχει πρόστιμο, αλλά τα περιμένει άλλος αναγνώστης"),
 ],
 "gloss": {"κινητή βιβλιοθήκη": "κινητή βιβλιοθήκη — mobile library", "βιβλιοθηκονόμο": "βιβλιοθηκονόμος — librarian", "μυθιστόρημα": "μυθιστόρημα — novel", "γραμματοσειρές": "γραμματοσειρά — font, typeface", "βλάβη": "βλάβη — fault, breakdown", "εγγονός": "εγγονός — grandson", "πρόστιμο": "πρόστιμο — fine", "αναγνώστης": "αναγνώστης — reader"},
})

ITEMS.append({
 "id": "l160-vm-pasteli", "title": "Μήνυμα για μια παραγγελία παστελιού", "title_en": "A message about a pasteli order", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από έναν μικρό παραγωγό παστελιού.",
 "script": [
  L("Παραγωγός", "m", "Γεια σας, κύριε Μαυρίδη, ο Γιάννης είμαι, από το εργαστήριο με το παστέλι. Πήρα την παραγγελία σας για τα εκατό παστέλια για τον γάμο, και σας ευχαριστώ πολύ.", "Hello, Mr Mavridis, it's Giannis, from the pasteli workshop. I got your order for the hundred pasteli bars for the wedding, and thank you very much."),
  L("Παραγωγός", "m", "Ένα πρόβλημα μόνο: το μέλι θυμαριού φέτος ήταν λίγο, λόγω της ξηρασίας, και δεν μου φτάνει για όλη την ποσότητα. Μπορώ να φτιάξω τα μισά με μέλι θυμαριού και τα άλλα μισά με μέλι από πεύκο, που είναι λίγο πιο σκούρο και λιγότερο γλυκό.", "Just one problem: thyme honey was scarce this year because of the drought, and I don't have enough for the whole quantity. I can make half with thyme honey and the other half with pine honey, which is a little darker and less sweet."),
  L("Παραγωγός", "m", "Αν θέλετε, μπορώ να βάλω και αμύγδαλο στο πεύκινο, για να έχουν οι καλεσμένοι δύο γεύσεις. Τα στέλνω με κούριερ την Πέμπτη, για να είναι φρέσκα. Πάρτε με όταν μπορέσετε να μου πείτε τι αποφασίσατε.", "If you like, I can also put almonds in the pine-honey ones, so the guests have two flavours. I'm sending them by courier on Thursday, so they're fresh. Call me when you can to tell me what you've decided."),
 ],
 "questions": [
  Q("Για ποια περίσταση είναι τα παστέλια;", ["Για βάφτιση", "Για γάμο", "Για γιορτή σχολείου", "Για γενέθλια"], 1, "για τον γάμο"),
  Q("Γιατί δεν φτάνει το μέλι θυμαριού;", ["Γιατί πουλήθηκε όλο", "Λόγω της ξηρασίας", "Γιατί άρρωστησαν οι μέλισσες", "Γιατί άργησε ο προμηθευτής"], 1, "λόγω της ξηρασίας"),
  Q("Τι προτείνει να προσθέσει στα παστέλια με πεύκινο μέλι;", ["Σοκολάτα", "Πορτοκάλι", "Αμύγδαλο", "Κανέλα"], 2, "μπορώ να βάλω και αμύγδαλο στο πεύκινο"),
 ],
 "gloss": {"παστελιού": "παστέλι — sesame-and-honey bar", "παραγωγό": "παραγωγός — producer", "εργαστήριο": "εργαστήριο — workshop", "θυμαριού": "θυμάρι — thyme", "ξηρασίας": "ξηρασία — drought", "ποσότητα": "ποσότητα — quantity", "σκούρο": "σκούρος — dark", "αμύγδαλο": "αμύγδαλο — almond", "πεύκινο": "πεύκινος — pine (adj.)", "καλεσμένοι": "καλεσμένος — guest", "κούριερ": "κούριερ — courier"},
})

ITEMS.append({
 "id": "l160-c1-leidenfrost", "title": "Σταγόνες που χορεύουν στο τηγάνι", "title_en": "Drops that dance in the frying pan", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια φυσικό για το λεγόμενο φαινόμενο Λάιντενφροστ.",
 "script": [
  L("Δημοσιογράφος", "m", "Όλοι έχουμε δει σταγόνες νερού να τρέχουν πάνω σε ένα πολύ ζεστό τηγάνι. Τι ακριβώς συμβαίνει;", "We've all seen water drops racing across a very hot frying pan. What exactly is happening?"),
  L("Φυσικός", "f", "Θα περίμενε κανείς ότι όσο πιο ζεστό είναι το μέταλλο, τόσο πιο γρήγορα θα εξατμιστεί η σταγόνα. Μέχρι ένα σημείο ισχύει. Πάνω όμως από μια κρίσιμη θερμοκρασία, που για το νερό είναι γύρω στους διακόσιους βαθμούς, η κάτω επιφάνεια της σταγόνας εξατμίζεται τόσο ακαριαία, ώστε σχηματίζεται ένα λεπτό στρώμα ατμού. Η σταγόνα αιωρείται πάνω του, σαν σε μαξιλάρι, και γλιστράει σχεδόν χωρίς τριβή.", "One would expect that the hotter the metal, the faster the drop will evaporate. Up to a point that holds. But above a critical temperature, which for water is around two hundred degrees, the underside of the drop evaporates so instantly that a thin layer of vapour forms. The drop floats on it, as if on a cushion, and slides almost without friction."),
  L("Δημοσιογράφος", "m", "Και γι' αυτό κρατάει περισσότερο;", "And that's why it lasts longer?"),
  L("Φυσικός", "f", "Ακριβώς. Ο ατμός είναι κακός αγωγός της θερμότητας, οπότε μονώνει τη σταγόνα από το καυτό μέταλλο. Έτσι, παράδοξα, μια σταγόνα σε τηγάνι στους τριακόσιους βαθμούς μπορεί να επιζήσει πολύ περισσότερο απ' ό,τι σε τηγάνι στους εκατόν πενήντα. Το φαινόμενο το περιέγραψε ο Γερμανός γιατρός Γιόχαν Γκότλομπ Λάιντενφροστ το 1756, αν και το είχαν παρατηρήσει και άλλοι πριν από αυτόν.", "Exactly. Vapour is a poor conductor of heat, so it insulates the drop from the scorching metal. So, paradoxically, a drop in a pan at three hundred degrees can survive much longer than in a pan at one hundred and fifty. The phenomenon was described by the German doctor Johann Gottlob Leidenfrost in 1756, although others had observed it before him."),
  L("Δημοσιογράφος", "m", "Έχει και πρακτική σημασία;", "Does it have practical importance too?"),
  L("Φυσικός", "f", "Μεγάλη, και όχι πάντα ευχάριστη. Όταν ψύχεις ένα καυτό κομμάτι μετάλλου βυθίζοντάς το σε νερό, το στρώμα ατμού καθυστερεί την ψύξη, και οι μηχανικοί πρέπει να το λάβουν υπόψη. Το ίδιο ισχύει στους πυρηνικούς αντιδραστήρες. Από την άλλη, πολλοί μάγειρες το χρησιμοποιούν χωρίς να ξέρουν το όνομά του: ρίχνουν λίγες σταγόνες νερό στο τηγάνι, και αν χορεύουν αντί να τσιτσιρίζουν, ξέρουν ότι είναι έτοιμο.", "Great importance, and not always pleasant. When you cool a red-hot piece of metal by plunging it into water, the vapour layer delays the cooling, and engineers have to take it into account. The same applies in nuclear reactors. On the other hand, many cooks use it without knowing its name: they sprinkle a few drops of water into the pan, and if they dance instead of sizzling, they know it is ready."),
 ],
 "questions": [
  Q("Τι συμβαίνει πάνω από την κρίσιμη θερμοκρασία;", ["Η σταγόνα εξατμίζεται αμέσως", "Σχηματίζεται ένα λεπτό στρώμα ατμού πάνω στο οποίο αιωρείται η σταγόνα", "Το μέταλλο αλλάζει χρώμα", "Η σταγόνα παγώνει"], 1, "σχηματίζεται ένα λεπτό στρώμα ατμού"),
  Q("Γιατί η σταγόνα κρατάει περισσότερο σε πολύ ζεστό τηγάνι;", ["Γιατί ο ατμός είναι κακός αγωγός της θερμότητας και τη μονώνει", "Γιατί το νερό βράζει σε υψηλότερη θερμοκρασία", "Γιατί η σταγόνα γίνεται μεγαλύτερη", "Γιατί το τηγάνι κρυώνει"], 0, "Ο ατμός είναι κακός αγωγός της θερμότητας, οπότε μονώνει τη σταγόνα από το καυτό μέταλλο"),
  Q("Ποιο πρόβλημα δημιουργεί το φαινόμενο στους μηχανικούς;", ["Σκουριάζει τα μέταλλα", "Καθυστερεί την ψύξη όταν βυθίζουν καυτό μέταλλο σε νερό", "Προκαλεί εκρήξεις", "Αυξάνει την κατανάλωση νερού"], 1, "το στρώμα ατμού καθυστερεί την ψύξη"),
  Q("Πώς χρησιμοποιούν οι μάγειρες το φαινόμενο;", ["Για να βράσουν πιο γρήγορα το νερό", "Για να καθαρίσουν το τηγάνι", "Για να καταλάβουν αν το τηγάνι είναι έτοιμο", "Για να μην κολλάει το φαγητό"], 2, "αν χορεύουν αντί να τσιτσιρίζουν, ξέρουν ότι είναι έτοιμο"),
 ],
 "gloss": {"φυσικό": "φυσικός — physicist", "σταγόνες": "σταγόνα — drop", "τηγάνι": "τηγάνι — frying pan", "εξατμιστεί": "εξατμίζομαι — to evaporate", "κρίσιμη": "κρίσιμος — critical", "ακαριαία": "ακαριαία — instantly", "ατμού": "ατμός — vapour, steam", "αιωρείται": "αιωρούμαι — to float, to hover", "τριβή": "τριβή — friction", "αγωγός": "αγωγός — conductor", "μονώνει": "μονώνω — to insulate", "παράδοξα": "παράδοξα — paradoxically", "ψύχεις": "ψύχω — to cool", "βυθίζοντάς": "βυθίζω — to plunge, to immerse", "αντιδραστήρες": "αντιδραστήρας — reactor", "τσιτσιρίζουν": "τσιτσιρίζω — to sizzle"},
})

ITEMS.append({
 "id": "l160-c1-coriolis", "title": "Προς τα πού στροβιλίζεται το νερό του νιπτήρα;", "title_en": "Which way does the water in the sink swirl?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκλαϊκευτική διάλεξη για τη δύναμη Κοριόλις και έναν διαδεδομένο μύθο.",
 "script": [
  L("Ομιλητής", "m", "Ίσως σας έχουν πει ότι στο βόρειο ημισφαίριο το νερό του νιπτήρα αδειάζει πάντα στρίβοντας αριστερόστροφα και στο νότιο δεξιόστροφα. Σε ορισμένες χώρες του ισημερινού, μάλιστα, ξεναγοί δείχνουν στους τουρίστες μια λεκάνη που αλλάζει φορά μόλις τη μετακινήσουν λίγα μέτρα βόρεια ή νότια της γραμμής. Είναι ένα ωραίο θέαμα, αλλά πρόκειται για τέχνασμα.", "You may have been told that in the northern hemisphere the water in the sink always drains turning anticlockwise, and in the southern hemisphere clockwise. In some equatorial countries, in fact, guides show tourists a basin that changes direction as soon as they move it a few metres north or south of the line. It's a nice spectacle, but it's a trick."),
  L("Ομιλητής", "m", "Η δύναμη που επικαλείται ο μύθος υπάρχει. Την περιέγραψε μαθηματικά ο Γάλλος μηχανικός Γκασπάρ-Γκυστάβ Κοριόλις το 1835, και οφείλεται στην περιστροφή της Γης: σε ό,τι κινείται στο βόρειο ημισφαίριο, φαίνεται να το εκτρέπει προς τα δεξιά. Σε κλίμακα χιλιάδων χιλιομέτρων είναι καθοριστική· γι' αυτό οι τυφώνες στο βόρειο ημισφαίριο περιστρέφονται αριστερόστροφα.", "The force the myth invokes does exist. The French engineer Gaspard-Gustave Coriolis described it mathematically in 1835, and it is due to the Earth's rotation: anything moving in the northern hemisphere appears to be deflected to the right. On a scale of thousands of kilometres it is decisive; that's why hurricanes in the northern hemisphere rotate anticlockwise."),
  L("Ομιλητής", "m", "Σε έναν νιπτήρα, όμως, η επίδρασή της είναι εκατομμύρια φορές ασθενέστερη από τις μικρές κινήσεις που έχει ήδη το νερό, από το σχήμα της λεκάνης ή από τον τρόπο που τη γεμίσαμε. Για να φανεί, χρειάζονται ακραίες συνθήκες. Το 1962, ο Άσερ Σαπίρο στο ΜΙΤ γέμισε μια μεγάλη στρογγυλή δεξαμενή, την άφησε να ηρεμήσει ένα ολόκληρο εικοσιτετράωρο και μετά άνοιξε προσεκτικά την τάπα. Μόνο τότε το νερό έφευγε σταθερά αριστερόστροφα. Το δίδαγμα είναι γενικότερο: ένας πραγματικός νόμος της φύσης δεν σημαίνει ότι εξηγεί κάθε φαινόμενο που του φορτώνουμε.", "In a sink, however, its effect is millions of times weaker than the small movements the water already has, from the shape of the basin or from the way we filled it. For it to show, extreme conditions are needed. In 1962, Ascher Shapiro at MIT filled a large round tank, left it to settle for a whole twenty-four hours, and then carefully opened the plug. Only then did the water drain consistently anticlockwise. The lesson is more general: a real law of nature does not mean that it explains every phenomenon we load onto it."),
 ],
 "questions": [
  Q("Τι λέει ο ομιλητής για τη λεκάνη που δείχνουν οι ξεναγοί στον ισημερινό;", ["Ότι αποδεικνύει τη δύναμη Κοριόλις", "Ότι πρόκειται για τέχνασμα", "Ότι λειτουργεί μόνο το καλοκαίρι", "Ότι χρησιμοποιείται σε επιστημονικά πειράματα"], 1, "πρόκειται για τέχνασμα"),
  Q("Σε ποια κλίμακα είναι καθοριστική η δύναμη Κοριόλις;", ["Σε κλίμακα χιλιάδων χιλιομέτρων", "Σε έναν νιπτήρα", "Σε μια μπανιέρα", "Σε κάθε κίνηση νερού"], 0, "Σε κλίμακα χιλιάδων χιλιομέτρων είναι καθοριστική"),
  Q("Γιατί δεν καθορίζει η δύναμη Κοριόλις τη φορά του νερού σε έναν νιπτήρα;", ["Γιατί δεν υπάρχει στην πραγματικότητα", "Γιατί είναι εκατομμύρια φορές ασθενέστερη από τις μικρές κινήσεις που έχει ήδη το νερό", "Γιατί οι νιπτήρες είναι μεταλλικοί", "Γιατί ισχύει μόνο στον ισημερινό"], 1, "η επίδρασή της είναι εκατομμύρια φορές ασθενέστερη"),
  Q("Τι έκανε ο Σαπίρο για να φανεί το φαινόμενο;", ["Χρησιμοποίησε έναν πολύ μικρό νιπτήρα", "Ταξίδεψε στον ισημερινό", "Άφησε μια μεγάλη στρογγυλή δεξαμενή να ηρεμήσει ένα εικοσιτετράωρο πριν ανοίξει την τάπα", "Ανακάτεψε το νερό προς τα αριστερά"], 2, "την άφησε να ηρεμήσει ένα ολόκληρο εικοσιτετράωρο"),
 ],
 "gloss": {"νιπτήρα": "νιπτήρας — washbasin, sink", "εκλαϊκευτική": "εκλαϊκευτικός — popular-science", "ημισφαίριο": "ημισφαίριο — hemisphere", "αριστερόστροφα": "αριστερόστροφα — anticlockwise", "δεξιόστροφα": "δεξιόστροφα — clockwise", "ισημερινού": "ισημερινός — equator", "λεκάνη": "λεκάνη — basin", "φορά": "φορά — direction (of rotation)", "τέχνασμα": "τέχνασμα — trick", "επικαλείται": "επικαλούμαι — to invoke", "εκτρέπει": "εκτρέπω — to deflect", "κλίμακα": "κλίμακα — scale", "τυφώνες": "τυφώνας — hurricane", "δεξαμενή": "δεξαμενή — tank", "τάπα": "τάπα — plug, stopper", "δίδαγμα": "δίδαγμα — lesson"},
})

rnd = random.Random(160)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-160.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
