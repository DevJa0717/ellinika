# Source for library/listening/listening-235.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l235.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l235-news-peristeriones", "title": "Περιστερώνες για λιγότερα περιστέρια στο κέντρο", "title_en": "Pigeon lofts for fewer pigeons in the centre", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Τρεις ξύλινοι περιστερώνες θα τοποθετηθούν τις επόμενες εβδομάδες σε ταράτσες δημοτικών κτιρίων στο κέντρο της πόλης. Ο δήμος ελπίζει ότι έτσι θα μειωθεί σιγά σιγά ο αριθμός των περιστεριών, που έχει αυξηθεί πολύ τα τελευταία χρόνια.", "Three wooden pigeon lofts will be placed in the coming weeks on the roof terraces of municipal buildings in the city centre. The municipality hopes that this will gradually reduce the number of pigeons, which has risen a lot in recent years."),
  L("Εκφωνητής", "m", "Η ιδέα ακούγεται παράξενη, αλλά έχει δοκιμαστεί σε αρκετές ευρωπαϊκές πόλεις, κυρίως στη Γερμανία. Στους περιστερώνες τα πουλιά βρίσκουν τροφή, νερό και ασφαλές μέρος για να φωλιάσουν. Οι εθελοντές που τους φροντίζουν αντικαθιστούν τα αυγά με ψεύτικα, από γύψο, ώστε να γεννιούνται λιγότερα νεαρά.", "The idea sounds strange, but it has been tried in several European cities, mainly in Germany. In the lofts the birds find food, water and a safe place to nest. The volunteers who look after them replace the eggs with fake plaster ones, so that fewer young are born."),
  L("Εκφωνητής", "m", "Επειδή τα περιστέρια περνούν πολλές ώρες μέσα στους περιστερώνες, αφήνουν εκεί και μεγάλο μέρος από τις κουτσουλιές τους, που προκαλούν ζημιές στα μνημεία και στις προσόψεις των κτιρίων. Ο δήμος υπολογίζει ότι θα εξοικονομήσει χρήματα από τους καθαρισμούς.", "Because the pigeons spend many hours inside the lofts, they also leave a large share of their droppings there, which damage monuments and building façades. The municipality estimates it will save money on cleaning."),
  L("Εκφωνητής", "m", "Παράλληλα, ζητά από τους κατοίκους να μην ταΐζουν τα περιστέρια στις πλατείες, γιατί η άφθονη τροφή είναι ο κύριος λόγος που πολλαπλασιάζονται. Όσοι θέλουν να γίνουν εθελοντές μπορούν να δηλώσουν συμμετοχή στο δημαρχείο ως το τέλος του μήνα.", "At the same time, it is asking residents not to feed the pigeons in the squares, because plentiful food is the main reason they multiply. Anyone who wants to volunteer can sign up at the town hall by the end of the month."),
 ],
 "questions": [
  Q("Πού θα τοποθετηθούν οι περιστερώνες;", ["Σε πάρκα της πόλης", "Σε ταράτσες δημοτικών κτιρίων", "Στο λιμάνι", "Σε καμπαναριά εκκλησιών"], 1, "θα τοποθετηθούν … σε ταράτσες δημοτικών κτιρίων στο κέντρο της πόλης"),
  Q("Πώς γεννιούνται λιγότερα νεαρά περιστέρια;", ["Οι εθελοντές αντικαθιστούν τα αυγά με ψεύτικα", "Τα πουλιά παίρνουν φάρμακο με την τροφή", "Τα περιστέρια μεταφέρονται στην εξοχή", "Οι φωλιές καταστρέφονται"], 0, "αντικαθιστούν τα αυγά με ψεύτικα, από γύψο"),
  Q("Πώς ελπίζει ο δήμος να εξοικονομήσει χρήματα;", ["Πουλώντας τα αυγά", "Από τους καθαρισμούς μνημείων και προσόψεων", "Κλείνοντας τις πλατείες", "Χρησιμοποιώντας μόνο εθελοντές στον δήμο"], 1, "Ο δήμος υπολογίζει ότι θα εξοικονομήσει χρήματα από τους καθαρισμούς"),
  Q("Τι ζητά ο δήμος από τους κατοίκους;", ["Να φτιάξουν περιστερώνες στα μπαλκόνια", "Να μην ταΐζουν τα περιστέρια στις πλατείες", "Να πληρώσουν ένα μικρό τέλος", "Να φωτογραφίζουν τις φωλιές"], 1, "ζητά από τους κατοίκους να μην ταΐζουν τα περιστέρια στις πλατείες"),
 ],
 "gloss": {"περιστερώνες": "περιστερώνας — pigeon loft, dovecote", "ταράτσες": "ταράτσα — flat roof, roof terrace", "φωλιάσουν": "φωλιάζω — to nest", "αντικαθιστούν": "αντικαθιστώ — to replace", "γύψο": "γύψος — plaster", "νεαρά": "νεαρός — young", "κουτσουλιές": "κουτσουλιά — bird dropping", "προσόψεις": "πρόσοψη — façade", "εξοικονομήσει": "εξοικονομώ — to save", "ταΐζουν": "ταΐζω — to feed", "πολλαπλασιάζονται": "πολλαπλασιάζομαι — to multiply"},
})
ITEMS.append({
 "id": "l235-vm-typografeio-prosklitiria", "title": "Μήνυμα από το τυπογραφείο για τα προσκλητήρια", "title_en": "A message from the print shop about the invitations", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε παραγγείλει σε ένα τυπογραφείο προσκλητήρια για τη βάπτιση του παιδιού σας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, η Ρένα είμαι από το τυπογραφείο στην οδό Ερμού, για τα προσκλητήρια της βάπτισης. Σας έστειλα χθες το δοκιμαστικό με ηλεκτρονικό ταχυδρομείο, αλλά δεν έχω πάρει απάντηση, γι' αυτό σας τηλεφωνώ.", "Good morning, this is Rena from the print shop on Ermou Street, about the christening invitations. I sent you the proof by email yesterday, but I haven't had an answer, so I'm phoning you."),
  L("Υπάλληλος", "f", "Πριν τα τυπώσουμε, θέλω να ελέγξετε δύο πράγματα. Στο κείμενο που μας δώσατε, η εκκλησία γράφεται «Αγίου Νικολάου», αλλά στον χάρτη στο πίσω μέρος γράφει «Αγίας Παρασκευής». Ένα από τα δύο είναι λάθος και δεν θέλω να το μαντέψω.", "Before we print them, I'd like you to check two things. In the text you gave us, the church is written as 'Agios Nikolaos', but on the map on the back it says 'Agia Paraskevi'. One of the two is wrong and I don't want to guess."),
  L("Υπάλληλος", "f", "Το δεύτερο: το χαρτί που διαλέξατε, το κρεμ με την ανάγλυφη υφή, έχει τελειώσει στον προμηθευτή και θα έρθει σε δέκα μέρες. Αν βιάζεστε, έχουμε ένα πολύ παρόμοιο σε λευκό, στην ίδια τιμή, και μπορούμε να σας τα παραδώσουμε την Παρασκευή.", "Second: the paper you chose, the cream one with the embossed texture, has run out at the supplier and will arrive in ten days. If you're in a hurry, we have a very similar one in white, at the same price, and we can deliver them to you on Friday."),
  L("Υπάλληλος", "f", "Επειδή η βάπτιση είναι σε τρεις εβδομάδες και τα προσκλητήρια πρέπει να μοιραστούν νωρίτερα, θα σας πρότεινα το λευκό. Πάντως η απόφαση είναι δική σας. Πάρτε με όταν μπορέσετε, μέχρι τις δύο είμαι στο μαγαζί.", "Since the christening is in three weeks and the invitations need to go out earlier, I'd suggest the white. But the decision is yours. Call me when you can, I'm in the shop until two."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί η υπάλληλος;", ["Γιατί δεν πήρε απάντηση στο ηλεκτρονικό μήνυμα με το δοκιμαστικό", "Γιατί τα προσκλητήρια είναι έτοιμα", "Γιατί η παραγγελία δεν έχει πληρωθεί", "Γιατί το τυπογραφείο μετακομίζει"], 0, "Σας έστειλα χθες το δοκιμαστικό … αλλά δεν έχω πάρει απάντηση"),
  Q("Ποιο λάθος βρήκε στο προσκλητήριο;", ["Λάθος ημερομηνία", "Δύο διαφορετικά ονόματα εκκλησίας", "Λάθος όνομα του παιδιού", "Λάθος ώρα"], 1, "η εκκλησία γράφεται «Αγίου Νικολάου», αλλά στον χάρτη … γράφει «Αγίας Παρασκευής»"),
  Q("Τι πρόβλημα υπάρχει με το χαρτί;", ["Είναι πιο ακριβό απ' ό,τι υπολόγισαν", "Έχει τελειώσει στον προμηθευτή", "Δεν τυπώνεται καλά", "Είναι πολύ λεπτό"], 1, "έχει τελειώσει στον προμηθευτή και θα έρθει σε δέκα μέρες"),
  Q("Γιατί προτείνει η υπάλληλος το λευκό χαρτί;", ["Γιατί είναι φθηνότερο", "Γιατί τα προσκλητήρια πρέπει να μοιραστούν νωρίς", "Γιατί είναι πιο κομψό", "Γιατί το προτιμούν οι περισσότεροι πελάτες"], 1, "Επειδή η βάπτιση είναι σε τρεις εβδομάδες και τα προσκλητήρια πρέπει να μοιραστούν νωρίτερα"),
 ],
 "gloss": {"τυπογραφείο": "τυπογραφείο — print shop", "προσκλητήρια": "προσκλητήριο — invitation card", "βάπτισης": "βάπτιση — christening", "δοκιμαστικό": "δοκιμαστικό — proof, sample", "τυπώσουμε": "τυπώνω — to print", "μαντέψω": "μαντεύω — to guess", "ανάγλυφη": "ανάγλυφος — embossed", "υφή": "υφή — texture", "προμηθευτή": "προμηθευτής — supplier", "μοιραστούν": "μοιράζομαι — to be handed out"},
})
ITEMS.append({
 "id": "l235-c1-mono-pyxida", "title": "Η βελόνα που δείχνει (σχεδόν) τον βορρά: η ιστορία της πυξίδας", "title_en": "The needle that points (almost) north: the history of the compass", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια εκπομπή για την ιστορία των εφευρέσεων.",
 "script": [
  L("Ομιλητής", "m", "Ότι ο μαγνητίτης, μια σιδηρούχα πέτρα, έλκει το σίδερο, το ήξεραν ήδη οι αρχαίοι Έλληνες και οι αρχαίοι Κινέζοι. Το όνομα «μαγνήτης» το συνδέουμε συνήθως με τη Μαγνησία. Όμως το να καταλάβεις ότι μια μαγνητισμένη βελόνα στρέφεται πάντα προς την ίδια κατεύθυνση ήταν ένα βήμα που χρειάστηκε αιώνες.", "That magnetite, an iron-bearing stone, attracts iron was already known to the ancient Greeks and the ancient Chinese. We usually link the name 'magnet' with Magnesia. But realising that a magnetised needle always turns in the same direction was a step that took centuries."),
  L("Ομιλητής", "m", "Η πρώτη σαφής περιγραφή μιας πυξίδας με βελόνα βρίσκεται σε ένα κινεζικό βιβλίο του ενδέκατου αιώνα, γραμμένο από τον λόγιο Σεν Κούο. Και εκεί υπάρχει μια λεπτομέρεια που εντυπωσιάζει: ο Σεν Κούο σημειώνει ότι η βελόνα δεν δείχνει ακριβώς τον νότο, αλλά αποκλίνει λίγο. Είχε δηλαδή παρατηρήσει αυτό που σήμερα λέμε μαγνητική απόκλιση.", "The first clear description of a compass with a needle is found in an eleventh-century Chinese book written by the scholar Shen Kuo. And there's a striking detail there: Shen Kuo notes that the needle doesn't point exactly south, but deviates slightly. In other words, he had observed what we now call magnetic declination."),
  L("Ομιλητής", "m", "Λίγες δεκαετίες αργότερα, ένα άλλο κινεζικό κείμενο αναφέρει ότι οι ναυτικοί χρησιμοποιούσαν την πυξίδα όταν ο ουρανός ήταν συννεφιασμένος. Στην Ευρώπη, οι πρώτες γραπτές μαρτυρίες εμφανίζονται στα τέλη του δωδέκατου αιώνα. Αν η ιδέα ταξίδεψε από την Ανατολή ή αν ανακαλύφθηκε ξανά ανεξάρτητα, οι ιστορικοί ακόμη το συζητούν.", "A few decades later, another Chinese text mentions that sailors used the compass when the sky was overcast. In Europe, the first written evidence appears at the end of the twelfth century. Whether the idea travelled from the East or was rediscovered independently, historians are still debating."),
  L("Ομιλητής", "m", "Αυτό που αξίζει να κρατήσουμε είναι ότι η πυξίδα δεν έκανε τους ναυτικούς πιο τολμηρούς απλώς επειδή τους έδειχνε τον δρόμο. Τους επέτρεψε να ταξιδεύουν και τον χειμώνα, με κακό καιρό, όταν τα αστέρια και ο ήλιος δεν φαίνονταν. Με άλλα λόγια, άλλαξε το ημερολόγιο του εμπορίου περισσότερο απ' ό,τι τον χάρτη του.", "What's worth remembering is that the compass didn't make sailors bolder simply because it showed them the way. It allowed them to sail in winter too, in bad weather, when the stars and the sun couldn't be seen. In other words, it changed the calendar of trade more than its map."),
 ],
 "questions": [
  Q("Τι ήξεραν ήδη οι αρχαίοι Έλληνες και Κινέζοι;", ["Ότι η βελόνα δείχνει τον βορρά", "Ότι ο μαγνητίτης έλκει το σίδερο", "Πώς να φτιάχνουν πυξίδες", "Τι είναι η μαγνητική απόκλιση"], 1, "Ότι ο μαγνητίτης, μια σιδηρούχα πέτρα, έλκει το σίδερο, το ήξεραν ήδη"),
  Q("Τι εντυπωσιάζει στην περιγραφή του Σεν Κούο;", ["Ότι η πυξίδα του ήταν από χρυσό", "Ότι παρατήρησε ότι η βελόνα αποκλίνει λίγο από τον νότο", "Ότι τη χρησιμοποίησε σε πόλεμο", "Ότι δεν πίστευε ότι λειτουργεί"], 1, "η βελόνα δεν δείχνει ακριβώς τον νότο, αλλά αποκλίνει λίγο"),
  Q("Τι λέει ο ομιλητής για την πυξίδα στην Ευρώπη;", ["Ότι σίγουρα ήρθε από την Κίνα", "Ότι δεν είναι σαφές αν ήρθε από την Ανατολή ή ανακαλύφθηκε ξανά", "Ότι εμφανίστηκε πριν από την Κίνα", "Ότι την έφεραν οι Βυζαντινοί"], 1, "Αν η ιδέα ταξίδεψε από την Ανατολή ή αν ανακαλύφθηκε ξανά ανεξάρτητα, οι ιστορικοί ακόμη το συζητούν"),
  Q("Ποια ήταν, κατά τον ομιλητή, η πιο σημαντική συνέπεια της πυξίδας;", ["Ότι οι χάρτες έγιναν πιο ακριβείς", "Ότι οι ναυτικοί μπορούσαν να ταξιδεύουν και τον χειμώνα με κακό καιρό", "Ότι τα πλοία έγιναν μεγαλύτερα", "Ότι μειώθηκαν οι πειρατές"], 1, "Τους επέτρεψε να ταξιδεύουν και τον χειμώνα, με κακό καιρό"),
 ],
 "gloss": {"μαγνητίτης": "μαγνητίτης — magnetite, lodestone", "σιδηρούχα": "σιδηρούχος — iron-bearing", "έλκει": "έλκω — to attract", "μαγνητισμένη": "μαγνητισμένος — magnetised", "στρέφεται": "στρέφομαι — to turn", "λόγιο": "λόγιος — scholar", "αποκλίνει": "αποκλίνω — to deviate", "απόκλιση": "απόκλιση — deviation, declination", "συννεφιασμένος": "συννεφιασμένος — overcast, cloudy", "μαρτυρίες": "μαρτυρία — testimony, evidence", "ανεξάρτητα": "ανεξάρτητα — independently", "τολμηρούς": "τολμηρός — bold, daring"},
})
ITEMS.append({
 "id": "l235-c1-int-xtapodi", "title": "Μια θαλάσσια βιολόγος για τη νοημοσύνη του χταποδιού", "title_en": "A marine biologist on the intelligence of the octopus", "type": "interview", "level": "C1",
 "context_el": "Μια θαλάσσια βιολόγος που μελετά τα κεφαλόποδα μιλά σε μια ραδιοφωνική εκπομπή επιστήμης.",
 "script": [
  L("Δημοσιογράφος", "f", "Για τους περισσότερους Έλληνες, το χταπόδι είναι κυρίως ένας μεζές. Εσείς λέτε ότι είναι από τα πιο έξυπνα ζώα της θάλασσας. Τι εννοείτε;", "For most Greeks, the octopus is mainly a meze. You say it's one of the cleverest animals in the sea. What do you mean?"),
  L("Βιολόγος", "f", "Εννοώ ότι λύνει προβλήματα. Στο εργαστήριο, ένα χταπόδι μαθαίνει να ξεβιδώνει το καπάκι ενός βάζου για να φτάσει σε ένα καβούρι. Μερικά μαθαίνουν πιο γρήγορα αν δουν πρώτα ένα άλλο χταπόδι να το κάνει. Ορισμένα έχουν δραπετεύσει από ενυδρεία, γλιστρώντας από απίστευτα στενά ανοίγματα.", "I mean that it solves problems. In the laboratory, an octopus learns to unscrew the lid of a jar to get at a crab. Some learn faster if they first see another octopus do it. Some have escaped from aquariums, slipping through incredibly narrow openings."),
  L("Δημοσιογράφος", "f", "Και πού βρίσκεται αυτή η εξυπνάδα; Στο κεφάλι;", "And where is this cleverness located? In the head?"),
  L("Βιολόγος", "f", "Εδώ είναι το πιο παράξενο. Το χταπόδι έχει περίπου μισό δισεκατομμύριο νευρώνες, αλλά τα δύο τρίτα από αυτούς βρίσκονται στα πλοκάμια, όχι στον εγκέφαλο. Κάθε πλοκάμι μπορεί, ως έναν βαθμό, να ψηλαφίζει και να αντιδρά μόνο του. Είναι μια οργάνωση της νοημοσύνης τελείως διαφορετική από τη δική μας, και γι' αυτό μας ενδιαφέρει τόσο.", "Here's the strangest part. The octopus has about half a billion neurons, but two-thirds of them are in the arms, not in the brain. Each arm can, to some extent, feel its way and react on its own. It's an organisation of intelligence completely different from ours, and that's why it interests us so much."),
  L("Δημοσιογράφος", "f", "Έχει και κάποιο αδύνατο σημείο;", "Does it have a weak point too?"),
  L("Βιολόγος", "f", "Ζει πολύ λίγο. Τα περισσότερα είδη ζουν ένα ή δύο χρόνια. Η μητέρα φυλάει τα αυγά της για εβδομάδες χωρίς να τρώει, και συνήθως πεθαίνει λίγο αφότου εκκολαφθούν. Άρα όλα όσα ξέρει ένα χταπόδι τα μαθαίνει μόνο του, μέσα σε ελάχιστο χρόνο. Αυτό, για μένα, το κάνει ακόμη πιο εντυπωσιακό. Και, ναι, μου δημιουργεί κάποια αμηχανία όταν το βλέπω στο μενού.", "It lives very briefly. Most species live one or two years. The mother guards her eggs for weeks without eating, and usually dies shortly after they hatch. So everything an octopus knows it learns on its own, in very little time. To me, that makes it even more impressive. And yes, I feel a certain awkwardness when I see it on the menu."),
 ],
 "questions": [
  Q("Ποιο παράδειγμα δίνει η βιολόγος για τη νοημοσύνη του χταποδιού;", ["Ότι αναγνωρίζει τον εαυτό του στον καθρέφτη", "Ότι μαθαίνει να ξεβιδώνει το καπάκι ενός βάζου", "Ότι μετρά ως το δέκα", "Ότι χρησιμοποιεί ήχους για να επικοινωνεί"], 1, "ένα χταπόδι μαθαίνει να ξεβιδώνει το καπάκι ενός βάζου για να φτάσει σε ένα καβούρι"),
  Q("Πού βρίσκονται οι περισσότεροι νευρώνες του χταποδιού;", ["Στον εγκέφαλο", "Στα πλοκάμια", "Στα μάτια", "Στο δέρμα"], 1, "τα δύο τρίτα από αυτούς βρίσκονται στα πλοκάμια, όχι στον εγκέφαλο"),
  Q("Γιατί η βιολόγος βρίσκει το χταπόδι «ακόμη πιο εντυπωσιακό»;", ["Γιατί ζει πολλές δεκαετίες", "Γιατί μαθαίνει τα πάντα μόνο του μέσα σε ελάχιστο χρόνο", "Γιατί η μητέρα το εκπαιδεύει χρόνια", "Γιατί ζει σε ομάδες"], 1, "όλα όσα ξέρει ένα χταπόδι τα μαθαίνει μόνο του, μέσα σε ελάχιστο χρόνο"),
  Q("Πώς νιώθει η βιολόγος όταν βλέπει χταπόδι στο μενού;", ["Αδιάφορη", "Κάποια αμηχανία", "Θυμό", "Χαρά"], 1, "μου δημιουργεί κάποια αμηχανία όταν το βλέπω στο μενού"),
 ],
 "gloss": {"κεφαλόποδα": "κεφαλόποδο — cephalopod", "νοημοσύνη": "νοημοσύνη — intelligence", "ξεβιδώνει": "ξεβιδώνω — to unscrew", "καπάκι": "καπάκι — lid", "δραπετεύσει": "δραπετεύω — to escape", "ενυδρεία": "ενυδρείο — aquarium", "γλιστρώντας": "γλιστρώ — to slip, slide", "νευρώνες": "νευρώνας — neuron", "πλοκάμια": "πλοκάμι — tentacle, arm", "ψηλαφίζει": "ψηλαφίζω — to feel by touch", "εκκολαφθούν": "εκκολάπτομαι — to hatch", "αμηχανία": "αμηχανία — awkwardness, unease"},
})
rnd = random.Random(235)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-235.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
