# Source for library/listening/listening-208.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l208.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l208-news-pityokampi", "title": "Προσοχή στις κάμπιες των πεύκων", "title_en": "Watch out for pine processionary caterpillars", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων σε έναν τοπικό ραδιοφωνικό σταθμό στα τέλη του χειμώνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Σε επιφυλακή βρίσκονται οι κτηνίατροι της πόλης, καθώς με τις πρώτες ζέστες εμφανίστηκαν στα πάρκα οι γνωστές κάμπιες των πεύκων, η πιτυοκάμπη. Οι κάμπιες ζουν τον χειμώνα σε λευκές, μεταξένιες φωλιές στα κλαδιά και τώρα κατεβαίνουν στο έδαφος, η μία πίσω από την άλλη, σαν μικρό τρένο.", "The city's vets are on alert, because with the first warm days the familiar pine caterpillars, the processionary caterpillars, have appeared in the parks. The caterpillars spend the winter in white, silky nests on the branches and are now coming down to the ground, one behind the other, like a little train."),
  L("Εκφωνήτρια", "f", "Οι τρίχες τους είναι ιδιαίτερα ερεθιστικές. Στους ανθρώπους προκαλούν φαγούρα και κοκκινίλες στο δέρμα ή στα μάτια. Για τα σκυλιά, όμως, ο κίνδυνος είναι πολύ μεγαλύτερος: αν μυρίσουν ή γλείψουν μια κάμπια, η γλώσσα τους μπορεί να πρηστεί επικίνδυνα, και χρειάζονται αμέσως κτηνίατρο.", "Their hairs are particularly irritating. In people they cause itching and red patches on the skin or in the eyes. For dogs, however, the danger is much greater: if they sniff or lick a caterpillar, their tongue can swell dangerously, and they need a vet immediately."),
  L("Εκφωνήτρια", "f", "Ο δήμος ξεκίνησε την αφαίρεση των φωλιών από τα δέντρα και ζητά από τους πολίτες να μην τις αγγίζουν μόνοι τους. Στους ιδιοκτήτες σκύλων συνιστάται να κρατούν τα ζώα τους δεμένα στα πάρκα με πεύκα τουλάχιστον μέχρι τα τέλη Απριλίου.", "The municipality has started removing the nests from the trees and asks citizens not to touch them themselves. Dog owners are advised to keep their animals on a lead in parks with pine trees at least until the end of April."),
 ],
 "questions": [
  Q("Πού περνούν οι κάμπιες τον χειμώνα;", ["Μέσα στο χώμα", "Σε λευκές, μεταξένιες φωλιές στα κλαδιά των πεύκων", "Στους κορμούς των δέντρων", "Σε σπηλιές"], 1, "ζουν τον χειμώνα σε λευκές, μεταξένιες φωλιές στα κλαδιά"),
  Q("Τι προκαλούν οι τρίχες τους στους ανθρώπους;", ["Πυρετό", "Φαγούρα και κοκκινίλες στο δέρμα ή στα μάτια", "Πονοκέφαλο", "Βήχα"], 1, "προκαλούν φαγούρα και κοκκινίλες στο δέρμα ή στα μάτια"),
  Q("Γιατί κινδυνεύουν περισσότερο τα σκυλιά;", ["Γιατί τρώνε τα πευκοβελόνα", "Γιατί αν μυρίσουν ή γλείψουν μια κάμπια, η γλώσσα τους μπορεί να πρηστεί", "Γιατί οι κάμπιες τα δαγκώνουν", "Γιατί σκαρφαλώνουν στα δέντρα"], 1, "η γλώσσα τους μπορεί να πρηστεί επικίνδυνα"),
  Q("Τι ζητά ο δήμος από τους ιδιοκτήτες σκύλων;", ["Να μην πηγαίνουν καθόλου στα πάρκα", "Να αφαιρούν οι ίδιοι τις φωλιές", "Να κρατούν τα σκυλιά δεμένα στα πάρκα με πεύκα μέχρι τα τέλη Απριλίου", "Να εμβολιάσουν τα σκυλιά"], 2, "να κρατούν τα ζώα τους δεμένα στα πάρκα με πεύκα τουλάχιστον μέχρι τα τέλη Απριλίου"),
 ],
 "gloss": {"επιφυλακή": "σε επιφυλακή — on alert", "πιτυοκάμπη": "πιτυοκάμπη — pine processionary caterpillar", "μεταξένιες": "μεταξένιος — silky", "ερεθιστικές": "ερεθιστικός — irritating", "φαγούρα": "φαγούρα — itching", "κοκκινίλες": "κοκκινίλα — red patch, redness", "γλείψουν": "γλείφω — to lick", "πρηστεί": "πρήζομαι — to swell"},
})
ITEMS.append({
 "id": "l208-dia-koudouni-kamera", "title": "Ένα κουδούνι με κάμερα", "title_en": "A doorbell with a camera", "type": "dialogue", "level": "B2",
 "context_el": "Δύο συγκάτοικοι συζητούν αν θα βάλουν στην πόρτα τους ένα έξυπνο κουδούνι με κάμερα.",
 "script": [
  L("Νικόλας", "m", "Είδα μια προσφορά για ένα έξυπνο κουδούνι με κάμερα. Όταν χτυπάει κάποιος, σου στέλνει ειδοποίηση στο κινητό και μπορείς να του μιλήσεις, ακόμα κι αν είσαι στη δουλειά.", "I saw an offer for a smart doorbell with a camera. When someone rings, it sends you a notification on your phone and you can talk to them, even if you're at work."),
  L("Δανάη", "f", "Και σε τι θα μας χρησιμεύσει; Δεν περιμένουμε και κανέναν σπουδαίο επισκέπτη.", "And what use would it be to us? We're hardly expecting any important visitors."),
  L("Νικόλας", "m", "Για τα δέματα, κυρίως. Τρεις φορές αυτόν τον μήνα ο κούριερ άφησε χαρτάκι ότι δεν βρήκε κανέναν. Έτσι θα του λέω από το κινητό να το αφήσει στον θυρωρό ή στη γειτόνισσα.", "For parcels, mainly. Three times this month the courier left a note saying he found nobody in. This way I'll tell him from my phone to leave it with the concierge or with the neighbour."),
  L("Δανάη", "f", "Εντάξει, αλλά η κάμερα θα βλέπει όλο τον διάδρομο, την πόρτα της κυρίας Ζωής απέναντι, όποιον περνάει. Απ' ό,τι έχω διαβάσει, δεν επιτρέπεται να καταγράφεις τους κοινόχρηστους χώρους χωρίς να ρωτήσεις τους άλλους ενοίκους.", "OK, but the camera will see the whole corridor, Mrs Zoi's door opposite, whoever passes by. From what I've read, you're not allowed to record the common areas without asking the other residents."),
  L("Νικόλας", "m", "Έχεις δίκιο, δεν το είχα σκεφτεί. Τα περισσότερα μοντέλα, πάντως, έχουν ρύθμιση για να θολώνει ένα μέρος της εικόνας. Θα το ρυθμίσω να βλέπει μόνο το χαλάκι μας, και θα ενημερώσουμε και τη διαχείριση της πολυκατοικίας πριν το βάλουμε.", "You're right, I hadn't thought of that. Most models, though, have a setting to blur part of the picture. I'll set it to see only our doormat, and we'll tell the building management before we put it in."),
  L("Δανάη", "f", "Έτσι ναι. Και να μην το ρυθμίσεις να σου στέλνει ειδοποίηση κάθε φορά που περνάει η γάτα της κυρίας Ζωής.", "Like that, yes. And don't set it to send you a notification every time Mrs Zoi's cat walks past."),
 ],
 "questions": [
  Q("Τι μπορεί να κάνει το κουδούνι που είδε ο Νικόλας;", ["Να ανοίγει μόνο του την πόρτα", "Να στέλνει ειδοποίηση στο κινητό και να μιλάς στον επισκέπτη", "Να παίζει μουσική", "Να καλεί την αστυνομία"], 1, "σου στέλνει ειδοποίηση στο κινητό και μπορείς να του μιλήσεις"),
  Q("Για ποιον λόγο το θέλει κυρίως ο Νικόλας;", ["Για τους κλέφτες", "Για να βλέπει τη γάτα", "Για τα δέματα, που δεν τα παραλαμβάνει κανείς", "Για τους φίλους του"], 2, "Για τα δέματα, κυρίως"),
  Q("Ποια αντίρρηση έχει η Δανάη;", ["Ότι είναι ακριβό", "Ότι η κάμερα θα καταγράφει τους κοινόχρηστους χώρους και τους γείτονες", "Ότι δεν ξέρουν να το εγκαταστήσουν", "Ότι θα χαλάσει την πόρτα"], 1, "δεν επιτρέπεται να καταγράφεις τους κοινόχρηστους χώρους"),
  Q("Πώς λύνουν το πρόβλημα;", ["Δεν αγοράζουν το κουδούνι", "Το βάζουν στο μπαλκόνι", "Ρυθμίζουν την κάμερα να βλέπει μόνο το χαλάκι τους και ενημερώνουν τη διαχείριση", "Ζητούν από την κυρία Ζωή να βάλει κι εκείνη"], 2, "Θα το ρυθμίσω να βλέπει μόνο το χαλάκι μας, και θα ενημερώσουμε και τη διαχείριση"),
 ],
 "gloss": {"ειδοποίηση": "ειδοποίηση — notification", "δέματα": "δέμα — parcel", "κούριερ": "κούριερ — courier", "θυρωρό": "θυρωρός — concierge, doorman", "κοινόχρηστους": "κοινόχρηστος — communal, shared", "θολώνει": "θολώνω — to blur", "χαλάκι": "χαλάκι — doormat, small rug", "διαχείριση": "διαχείριση — management"},
})
ITEMS.append({
 "id": "l208-c1-mono-dyschromatopsia", "title": "Όταν το κόκκινο μοιάζει με πράσινο", "title_en": "When red looks like green: colour blindness", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια οφθαλμίατρο σε μια ραδιοφωνική εκπομπή για την υγεία.",
 "script": [
  L("Οφθαλμίατρος", "f", "Αυτό που στην καθημερινή γλώσσα λέμε «αχρωματοψία» είναι στην πραγματικότητα, στη συντριπτική πλειονότητα των περιπτώσεων, μια δυσχρωματοψία: ο άνθρωπος βλέπει χρώματα, αλλά δυσκολεύεται να ξεχωρίσει ορισμένα, συνήθως το κόκκινο από το πράσινο. Η ολική αχρωματοψία, ένας κόσμος μόνο σε αποχρώσεις του γκρι, είναι εξαιρετικά σπάνια.", "What in everyday language we call 'colour blindness' is in reality, in the overwhelming majority of cases, a colour vision deficiency: the person sees colours but has difficulty telling some apart, usually red from green. Total colour blindness, a world only in shades of grey, is extremely rare."),
  L("Οφθαλμίατρος", "f", "Η πιο συνηθισμένη μορφή είναι κληρονομική και συνδέεται με το χρωμόσωμα Χ. Γι' αυτό αφορά κυρίως τους άνδρες: σε πληθυσμούς ευρωπαϊκής καταγωγής περίπου ένας στους δώδεκα άνδρες έχει κάποιου βαθμού δυσκολία με το κόκκινο και το πράσινο, ενώ στις γυναίκες το ποσοστό είναι πολύ μικρότερο, περίπου μία στις διακόσιες.", "The most common form is hereditary and linked to the X chromosome. That is why it mainly affects men: in populations of European descent about one in twelve men has some degree of difficulty with red and green, while in women the rate is much lower, about one in two hundred."),
  L("Οφθαλμίατρος", "f", "Πρώτος την περιέγραψε επιστημονικά, στα τέλη του 18ου αιώνα, ο Άγγλος χημικός Τζον Ντάλτον, που είχε και ο ίδιος το πρόβλημα· γι' αυτό σε πολλές γλώσσες λέγεται και «δαλτονισμός». Η διάγνωση γίνεται σήμερα συνήθως με τους πίνακες Ισιχάρα, τους κύκλους με τις χρωματιστές κουκκίδες, μέσα στους οποίους κρύβεται ένας αριθμός.", "The first to describe it scientifically, at the end of the 18th century, was the English chemist John Dalton, who had the problem himself; that is why in many languages it is also called 'daltonism'. Diagnosis today is usually made with the Ishihara plates, the circles of coloured dots in which a number is hidden."),
  L("Οφθαλμίατρος", "f", "Θεραπεία δεν υπάρχει, αλλά οι περισσότεροι προσαρμόζονται τόσο καλά, που συχνά το ανακαλύπτουν αργά, π.χ. όταν ένας δάσκαλος παρατηρεί ότι το παιδί ζωγραφίζει πάντα τα δέντρα καφέ. Εκεί που χρειάζεται προσοχή είναι στον σχεδιασμό: ένας χάρτης ή ένα γράφημα που στηρίζεται μόνο στη διάκριση κόκκινου και πράσινου αποκλείει, χωρίς να το καταλαβαίνουμε, ένα σημαντικό μέρος του κοινού.", "There is no cure, but most people adapt so well that they often discover it late, for example when a teacher notices that the child always paints the trees brown. Where care is needed is in design: a map or a chart that relies only on distinguishing red from green excludes, without our realising it, a significant part of the audience."),
 ],
 "questions": [
  Q("Τι είναι στις περισσότερες περιπτώσεις αυτό που λέμε «αχρωματοψία»;", ["Ολική απώλεια της όρασης", "Δυσκολία να ξεχωρίζει κανείς ορισμένα χρώματα, συνήθως το κόκκινο από το πράσινο", "Ένας κόσμος μόνο σε αποχρώσεις του γκρι", "Μια προσωρινή μόλυνση των ματιών"], 1, "βλέπει χρώματα, αλλά δυσκολεύεται να ξεχωρίσει ορισμένα, συνήθως το κόκκινο από το πράσινο"),
  Q("Γιατί αφορά κυρίως τους άνδρες;", ["Γιατί συνδέεται με το χρωμόσωμα Χ", "Γιατί οι άνδρες δουλεύουν περισσότερο σε οθόνες", "Γιατί οφείλεται στο κάπνισμα", "Γιατί οι γυναίκες δεν εξετάζονται"], 0, "συνδέεται με το χρωμόσωμα Χ. Γι' αυτό αφορά κυρίως τους άνδρες"),
  Q("Γιατί λέγεται σε πολλές γλώσσες «δαλτονισμός»;", ["Από μια πόλη της Αγγλίας", "Από το όνομα του χημικού που την περιέγραψε και την είχε ο ίδιος", "Από το όνομα ενός φαρμάκου", "Από μια λατινική λέξη για το χρώμα"], 1, "ο Άγγλος χημικός Τζον Ντάλτον, που είχε και ο ίδιος το πρόβλημα"),
  Q("Πού, κατά την ομιλήτρια, χρειάζεται ιδιαίτερη προσοχή;", ["Στη διατροφή των παιδιών", "Στην οδήγηση τη νύχτα", "Στον σχεδιασμό χαρτών και γραφημάτων που στηρίζονται μόνο στο κόκκινο και στο πράσινο", "Στην επιλογή γυαλιών ηλίου"], 2, "Εκεί που χρειάζεται προσοχή είναι στον σχεδιασμό"),
 ],
 "gloss": {"συντριπτική": "συντριπτικός — overwhelming", "δυσχρωματοψία": "δυσχρωματοψία — colour vision deficiency", "αποχρώσεις": "απόχρωση — shade", "κληρονομική": "κληρονομικός — hereditary", "χρωμόσωμα": "χρωμόσωμα — chromosome", "καταγωγής": "καταγωγή — descent, origin", "δαλτονισμός": "δαλτονισμός — daltonism, colour blindness", "κουκκίδες": "κουκκίδα — dot", "αποκλείει": "αποκλείω — to exclude"},
})
ITEMS.append({
 "id": "l208-c1-int-koliandro", "title": "Γιατί σε κάποιους ο κόλιανδρος έχει γεύση σαπουνιού", "title_en": "Why coriander tastes of soap to some people", "type": "interview", "level": "C1",
 "context_el": "Ένας δημοσιογράφος συζητά με μια ερευνήτρια της γεύσης και της όσφρησης σε μια εκπομπή για τη διατροφή.",
 "script": [
  L("Δημοσιογράφος", "m", "Ο κόλιανδρος, ή κόλιαντρο όπως το λέμε συχνά, είναι από τα πιο αγαπημένα μυρωδικά στον κόσμο, από το Μεξικό μέχρι την Ταϊλάνδη. Κι όμως, κάποιοι λένε ότι τους θυμίζει σαπούνι ή και κοριό. Είναι απλώς θέμα γούστου;", "Coriander, or 'koliandro' as we often call it, is one of the most loved herbs in the world, from Mexico to Thailand. And yet some people say it reminds them of soap or even of bedbugs. Is it simply a matter of taste?"),
  L("Ερευνήτρια", "f", "Εν μέρει, ναι, αλλά όχι μόνο. Τα φρέσκα φύλλα περιέχουν ορισμένες αρωματικές ουσίες, τις λεγόμενες αλδεΰδες, που βρίσκονται και σε σαπούνια και σε κάποια έντομα. Οι περισσότεροι άνθρωποι τις αντιλαμβάνονται ως φρέσκες, σχεδόν λεμονάτες. Μια μειοψηφία, όμως, τις αισθάνεται έντονα δυσάρεστες.", "Partly, yes, but not only. The fresh leaves contain certain aromatic substances, so-called aldehydes, which are also found in soaps and in some insects. Most people perceive them as fresh, almost lemony. A minority, however, finds them intensely unpleasant."),
  L("Δημοσιογράφος", "m", "Και από τι εξαρτάται σε ποια ομάδα ανήκει κανείς;", "And what does it depend on which group one belongs to?"),
  L("Ερευνήτρια", "f", "Γενετικές μελέτες έχουν εντοπίσει μια παραλλαγή κοντά σε ένα γονίδιο που σχετίζεται με έναν οσφρητικό υποδοχέα, ο οποίος ανιχνεύει ακριβώς αυτές τις αλδεΰδες. Το γονίδιο δεν εξηγεί τα πάντα· το ποσοστό όσων αντιπαθούν το φυτό διαφέρει πολύ από πληθυσμό σε πληθυσμό, και ρόλο παίζει σίγουρα και το πόσο συχνά το τρώγαμε από παιδιά.", "Genetic studies have identified a variant near a gene linked to an olfactory receptor that detects precisely these aldehydes. The gene doesn't explain everything; the proportion of people who dislike the plant varies greatly from population to population, and how often we ate it as children certainly plays a part as well."),
  L("Δημοσιογράφος", "m", "Δηλαδή όποιος το μισεί, μπορεί να το συνηθίσει;", "So whoever hates it can get used to it?"),
  L("Ερευνήτρια", "f", "Αρκετοί το καταφέρνουν. Βοηθάει να το ψιλοκόβεις ή να το λιώνεις, για παράδειγμα σε ένα πέστο, γιατί έτσι οι ουσίες αυτές διασπώνται γρηγορότερα και η γεύση γίνεται πιο ήπια. Και, βέβαια, οι σπόροι του έχουν εντελώς διαφορετικό άρωμα· πολλοί που αποφεύγουν τα φύλλα δεν έχουν κανένα πρόβλημα με τον αλεσμένο κόλιανδρο στα κεφτεδάκια.", "Quite a few manage. It helps to chop it finely or crush it, for example in a pesto, because that way these substances break down faster and the taste becomes milder. And of course its seeds have a completely different aroma; many who avoid the leaves have no problem with ground coriander in meatballs."),
 ],
 "questions": [
  Q("Τι περιέχουν τα φρέσκα φύλλα του κόλιανδρου, σύμφωνα με την ερευνήτρια;", ["Μια τοξική ουσία", "Αρωματικές ουσίες που βρίσκονται και σε σαπούνια και σε κάποια έντομα", "Πολύ αλάτι", "Μια ουσία που προκαλεί αλλεργία σε όλους"], 1, "αλδεΰδες, που βρίσκονται και σε σαπούνια και σε κάποια έντομα"),
  Q("Πώς αντιλαμβάνονται αυτές τις ουσίες οι περισσότεροι άνθρωποι;", ["Ως πικρές", "Ως φρέσκες, σχεδόν λεμονάτες", "Ως καυτερές", "Δεν τις αντιλαμβάνονται καθόλου"], 1, "τις αντιλαμβάνονται ως φρέσκες, σχεδόν λεμονάτες"),
  Q("Τι λέει για τον ρόλο των γονιδίων;", ["Ότι εξηγούν πλήρως την αντιπάθεια", "Ότι δεν παίζουν κανέναν ρόλο", "Ότι μια παραλλαγή σχετίζεται με την αντιπάθεια, αλλά δεν εξηγεί τα πάντα", "Ότι η αντιπάθεια αφορά μόνο μία χώρα"], 2, "Το γονίδιο δεν εξηγεί τα πάντα"),
  Q("Τι συμβουλεύει όσους θέλουν να το συνηθίσουν;", ["Να το τρώνε μόνο ωμό και ολόκληρο", "Να το ψιλοκόβουν ή να το λιώνουν, π.χ. σε πέστο", "Να το βράζουν πολλές ώρες", "Να το συνδυάζουν με ζάχαρη"], 1, "Βοηθάει να το ψιλοκόβεις ή να το λιώνεις, για παράδειγμα σε ένα πέστο"),
 ],
 "gloss": {"κόλιανδρος": "κόλιανδρος / κόλιαντρο — coriander", "μυρωδικά": "μυρωδικό — herb", "κοριό": "κοριός — bedbug", "αλδεΰδες": "αλδεΰδη — aldehyde", "μειοψηφία": "μειοψηφία — minority", "παραλλαγή": "παραλλαγή — variant", "οσφρητικό": "οσφρητικός — olfactory", "υποδοχέα": "υποδοχέας — receptor", "ψιλοκόβεις": "ψιλοκόβω — to chop finely", "διασπώνται": "διασπώμαι — to break down"},
})
rnd = random.Random(208)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-208.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
