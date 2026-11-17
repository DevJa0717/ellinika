# Source for library/listening/listening-158.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l158.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l158-ann-pyrotechnimata", "title": "Πυροτεχνήματα στο λιμάνι", "title_en": "Fireworks at the harbour", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο τοπικό ραδιόφωνο για τη βραδιά της Πρωτοχρονιάς.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος ενημερώνει ότι την παραμονή της Πρωτοχρονιάς, στις δώδεκα ακριβώς, θα γίνει επίδειξη πυροτεχνημάτων από μια φορτηγίδα μέσα στο λιμάνι. Η επίδειξη θα διαρκέσει δέκα λεπτά.", "The municipality announces that on New Year's Eve, at exactly midnight, there will be a fireworks display from a barge inside the harbour. The display will last ten minutes."),
  L("Εκφωνήτρια", "f", "Από τις εννιά το βράδυ η παραλιακή λεωφόρος θα είναι κλειστή για τα αυτοκίνητα, από το τελωνείο μέχρι τον φάρο. Οι κάτοικοι μπορούν να σταθμεύσουν δωρεάν στο πάρκινγκ του σταδίου, από όπου θα ξεκινούν λεωφορεία για το κέντρο κάθε δέκα λεπτά.", "From nine in the evening the seafront avenue will be closed to cars, from the customs house to the lighthouse. Residents can park free of charge at the stadium car park, from where buses will leave for the centre every ten minutes."),
  L("Εκφωνήτρια", "f", "Παρακαλούμε τους ιδιοκτήτες κατοικίδιων να κρατήσουν τα ζώα τους μέσα στο σπίτι εκείνη την ώρα, γιατί ο θόρυβος τα τρομάζει. Επίσης, απαγορεύεται αυστηρά να ρίχνει κανείς δικά του βεγγαλικά στον χώρο της προκυμαίας.", "We ask pet owners to keep their animals indoors at that time, because the noise frightens them. Also, it is strictly forbidden for anyone to set off their own fireworks on the quayside."),
 ],
 "questions": [
  Q("Από πού θα ριχτούν τα πυροτεχνήματα;", ["Από τον φάρο", "Από μια φορτηγίδα μέσα στο λιμάνι", "Από το στάδιο", "Από την ταράτσα του δημαρχείου"], 1, "από μια φορτηγίδα μέσα στο λιμάνι"),
  Q("Πού μπορούν να παρκάρουν δωρεάν οι κάτοικοι;", ["Στο λιμάνι", "Στην παραλιακή λεωφόρο", "Στο πάρκινγκ του σταδίου", "Δίπλα στο τελωνείο"], 2, "στο πάρκινγκ του σταδίου"),
  Q("Τι ζητάει ο δήμος από τους ιδιοκτήτες κατοικίδιων;", ["Να φέρουν τα ζώα με λουρί", "Να κρατήσουν τα ζώα τους μέσα στο σπίτι", "Να μην πάνε στην προκυμαία", "Να δηλώσουν τα ζώα τους"], 1, "να κρατήσουν τα ζώα τους μέσα στο σπίτι"),
 ],
 "gloss": {"παραμονή": "παραμονή — eve", "επίδειξη": "επίδειξη — display, show", "πυροτεχνημάτων": "πυροτέχνημα — firework", "φορτηγίδα": "φορτηγίδα — barge", "παραλιακή": "παραλιακός — seafront (adj.)", "τελωνείο": "τελωνείο — customs house", "σταθμεύσουν": "σταθμεύω — to park", "κατοικίδιων": "κατοικίδιο — pet", "τρομάζει": "τρομάζω — to frighten", "βεγγαλικά": "βεγγαλικό — firework, flare", "προκυμαίας": "προκυμαία — quayside, waterfront"},
})

ITEMS.append({
 "id": "l158-int-komikos", "title": "Η κωμικός που γελάει με την οικογένειά της", "title_en": "The comedian who laughs at her family", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια ραδιοφωνική συνέντευξη με μια νέα κωμικό που κάνει στάνταπ κωμωδία.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς ξεκινήσατε τη στάνταπ κωμωδία;", "How did you start doing stand-up comedy?"),
  L("Κωμικός", "f", "Δούλευα σε τηλεφωνικό κέντρο και έλεγα στους συναδέλφους ιστορίες από το σπίτι μου, για τη μάνα μου και τη θεία μου. Γελούσαν τόσο πολύ, που μια φίλη μου με έγραψε κρυφά σε μια βραδιά ανοιχτού μικροφώνου. Είχα πέντε λεπτά. Έτρεμαν τα γόνατά μου, αλλά ο κόσμος γέλασε.", "I worked at a call centre and used to tell my colleagues stories from home, about my mum and my aunt. They laughed so much that a friend secretly signed me up for an open-mic night. I had five minutes. My knees were shaking, but people laughed."),
  L("Δημοσιογράφος", "m", "Δεν θυμώνει η οικογένειά σας που τους βάζετε στα κείμενά σας;", "Doesn't your family get angry that you put them in your material?"),
  L("Κωμικός", "f", "Η μάνα μου έρχεται σε κάθε παράσταση και κάθεται στην πρώτη σειρά. Το μόνο που μου ζήτησε είναι να μην αναφέρω ποτέ την ηλικία της. Η θεία μου, αντίθετα, παραπονιέται όταν δεν μιλάω γι' αυτήν!", "My mum comes to every show and sits in the front row. The only thing she asked me is never to mention her age. My aunt, on the other hand, complains when I don't talk about her!"),
  L("Δημοσιογράφος", "m", "Πόσο χρόνο χρειάζεστε για ένα καινούργιο κείμενο;", "How long do you need for a new piece?"),
  L("Κωμικός", "f", "Γράφω κάθε πρωί, αλλά ένα αστείο το δοκιμάζω τουλάχιστον δέκα φορές μπροστά σε κοινό πριν το κρατήσω. Το κοινό είναι ο καλύτερος δάσκαλος: αν δεν γελάσει, δεν φταίει εκείνο.", "I write every morning, but I try out a joke at least ten times in front of an audience before I keep it. The audience is the best teacher: if it doesn't laugh, it's not the audience's fault."),
 ],
 "questions": [
  Q("Πώς βρέθηκε για πρώτη φορά στη σκηνή;", ["Τη βρήκε ένας παραγωγός", "Μια φίλη της την έγραψε κρυφά σε μια βραδιά ανοιχτού μικροφώνου", "Κέρδισε έναν διαγωνισμό", "Σπούδασε θέατρο"], 1, "μια φίλη μου με έγραψε κρυφά σε μια βραδιά ανοιχτού μικροφώνου"),
  Q("Τι της ζήτησε η μητέρα της;", ["Να μην μιλάει για τη θεία", "Να μην αναφέρει ποτέ την ηλικία της", "Να αλλάξει δουλειά", "Να μην την καλεί στις παραστάσεις"], 1, "να μην αναφέρω ποτέ την ηλικία της"),
  Q("Πόσες φορές δοκιμάζει ένα αστείο πριν το κρατήσει;", ["Μία", "Τρεις", "Τουλάχιστον δέκα", "Όσες της πει ο παραγωγός"], 2, "τουλάχιστον δέκα φορές"),
 ],
 "gloss": {"κωμικό": "κωμικός — comedian", "στάνταπ κωμωδία": "στάνταπ κωμωδία — stand-up comedy", "τηλεφωνικό κέντρο": "τηλεφωνικό κέντρο — call centre", "κρυφά": "κρυφά — secretly", "ανοιχτού μικροφώνου": "ανοιχτό μικρόφωνο — open mic", "γόνατά": "γόνατο — knee", "κείμενά": "κείμενο — text; (comedy) material", "παραπονιέται": "παραπονιέμαι — to complain", "αστείο": "αστείο — joke", "κοινό": "κοινό — audience"},
})

ITEMS.append({
 "id": "l158-mon-thermokipio", "title": "Βομβίνοι στο θερμοκήπιο", "title_en": "Bumblebees in the greenhouse", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν παραγωγό ντομάτας να μιλάει σε μια αγροτική εκπομπή για τον τρόπο που δουλεύει στο θερμοκήπιό του.",
 "script": [
  L("Παραγωγός", "m", "Πριν από χρόνια, για να γονιμοποιηθούν τα λουλούδια της ντομάτας στο θερμοκήπιο, τα δονούσαμε ένα ένα με ένα μικρό μηχάνημα ή ψεκάζαμε ορμόνες. Ήταν κουραστική δουλειά και το αποτέλεσμα δεν ήταν πάντα καλό.", "Years ago, to get the tomato flowers in the greenhouse pollinated, we vibrated them one by one with a small machine or sprayed hormones. It was tiring work and the result wasn't always good."),
  L("Παραγωγός", "m", "Σήμερα αγοράζουμε κυψέλες με βομβίνους. Οι βομβίνοι είναι συγγενείς της μέλισσας, πιο χοντροί και τριχωτοί, και δουλεύουν ακόμη και όταν κάνει κρύο ή έχει συννεφιά. Πιάνονται από το λουλούδι και το κουνάνε με τα φτερά τους, κι έτσι πέφτει η γύρη.", "Today we buy hives of bumblebees. Bumblebees are relatives of the honeybee, plumper and hairier, and they work even when it's cold or cloudy. They grab hold of the flower and shake it with their wings, and that way the pollen falls."),
  L("Παραγωγός", "m", "Το μόνο που μας ζητάνε είναι να μη χρησιμοποιούμε δυνατά φάρμακα. Γι' αυτό, για τα έντομα που καταστρέφουν τα φυτά, βάζουμε άλλα, μικρότερα έντομα που τα τρώνε. Έτσι, χωρίς να το σχεδιάσουμε, γίναμε σχεδόν βιολογική καλλιέργεια.", "The only thing they ask of us is not to use strong pesticides. That's why, for the insects that damage the plants, we release other, smaller insects that eat them. So, without planning it, we've become almost an organic farm."),
 ],
 "questions": [
  Q("Πώς γονιμοποιούσαν παλιά τα λουλούδια της ντομάτας;", ["Με μέλισσες", "Τα δονούσαν ένα ένα με ένα μηχάνημα ή ψέκαζαν ορμόνες", "Με τον αέρα από τα παράθυρα", "Δεν χρειαζόταν γονιμοποίηση"], 1, "τα δονούσαμε ένα ένα με ένα μικρό μηχάνημα ή ψεκάζαμε ορμόνες"),
  Q("Τι πλεονέκτημα έχουν οι βομβίνοι, σύμφωνα με τον παραγωγό;", ["Κάνουν περισσότερο μέλι", "Δεν τσιμπάνε ποτέ", "Δουλεύουν ακόμη και όταν κάνει κρύο ή έχει συννεφιά", "Είναι φθηνότεροι από τις μέλισσες"], 2, "δουλεύουν ακόμη και όταν κάνει κρύο ή έχει συννεφιά"),
  Q("Πώς αντιμετωπίζουν τα έντομα που καταστρέφουν τα φυτά;", ["Με δυνατά φάρμακα", "Βάζουν άλλα, μικρότερα έντομα που τα τρώνε", "Με παγίδες", "Κόβουν τα άρρωστα φυτά"], 1, "βάζουμε άλλα, μικρότερα έντομα που τα τρώνε"),
 ],
 "gloss": {"θερμοκήπιο": "θερμοκήπιο — greenhouse", "γονιμοποιηθούν": "γονιμοποιούμαι — to be pollinated, fertilised", "δονούσαμε": "δονώ — to vibrate", "ψεκάζαμε": "ψεκάζω — to spray", "κυψέλες": "κυψέλη — hive", "βομβίνους": "βομβίνος — bumblebee", "τριχωτοί": "τριχωτός — hairy", "γύρη": "γύρη — pollen", "φάρμακα": "φάρμακο — (here) pesticide", "έντομα": "έντομο — insect", "βιολογική καλλιέργεια": "βιολογική καλλιέργεια — organic farming"},
})

ITEMS.append({
 "id": "l158-vm-enorgani", "title": "Μήνυμα από την προπονήτρια ενόργανης", "title_en": "A message from the gymnastics coach", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από την προπονήτρια ενόργανης γυμναστικής της κόρης σας.",
 "script": [
  L("Προπονήτρια", "f", "Καλησπέρα σας, η Κατερίνα, η προπονήτρια της Ζωής. Σας παίρνω για τους αγώνες της Κυριακής. Η Ζωή θα αγωνιστεί στη δοκό και στο έδαφος. Στο δίζυγο δεν τη δηλώσαμε, γιατί ακόμα πονάει λίγο ο καρπός της και δεν θέλουμε να το ρισκάρουμε.", "Good evening, it's Katerina, Zoi's coach. I'm calling about Sunday's competition. Zoi will compete on the beam and the floor. We didn't enter her on the bars, because her wrist still hurts a little and we don't want to risk it."),
  L("Προπονήτρια", "f", "Το πούλμαν του συλλόγου φεύγει στις επτά το πρωί από το γυμναστήριο. Τα παιδιά πρέπει να έχουν μαζί τους το κορμάκι του συλλόγου, την κάρτα υγείας τους και ένα ελαφρύ φαγητό, όχι σοκολάτες.", "The club coach leaves at seven in the morning from the gym. The children must have with them the club leotard, their health card and a light meal, not chocolate."),
  L("Προπονήτρια", "f", "Οι γονείς μπορούν να έρθουν, αλλά παρακαλώ να μη φωνάζετε οδηγίες από την κερκίδα· τα παιδιά αγχώνονται. Αν θέλετε να ρωτήσετε κάτι, στείλτε μου ένα μήνυμα.", "Parents can come, but please don't shout instructions from the stands; the children get stressed. If you want to ask anything, send me a message."),
 ],
 "questions": [
  Q("Γιατί η Ζωή δεν θα αγωνιστεί στο δίζυγο;", ["Γιατί δεν έχει προπονηθεί αρκετά", "Γιατί ακόμα πονάει λίγο ο καρπός της", "Γιατί δεν της αρέσει", "Γιατί δεν υπάρχει θέση"], 1, "ακόμα πονάει λίγο ο καρπός της"),
  Q("Τι δεν πρέπει να έχουν μαζί τους τα παιδιά;", ["Την κάρτα υγείας", "Το κορμάκι του συλλόγου", "Σοκολάτες", "Ένα ελαφρύ φαγητό"], 2, "όχι σοκολάτες"),
  Q("Τι ζητάει η προπονήτρια από τους γονείς;", ["Να μην έρθουν στους αγώνες", "Να μη φωνάζουν οδηγίες από την κερκίδα", "Να φέρουν τα παιδιά με το αυτοκίνητο", "Να πληρώσουν το πούλμαν"], 1, "να μη φωνάζετε οδηγίες από την κερκίδα"),
 ],
 "gloss": {"ενόργανης γυμναστικής": "ενόργανη γυμναστική — artistic gymnastics", "προπονήτρια": "προπονήτρια — (female) coach", "δοκό": "δοκός — (balance) beam", "έδαφος": "έδαφος — floor (exercise)", "δίζυγο": "δίζυγο — (uneven) bars", "καρπός": "καρπός — wrist", "ρισκάρουμε": "ρισκάρω — to risk", "πούλμαν": "πούλμαν — coach (bus)", "κορμάκι": "κορμάκι — leotard", "κερκίδα": "κερκίδα — stand(s)", "αγχώνονται": "αγχώνομαι — to get stressed"},
})

ITEMS.append({
 "id": "l158-vm-balonia", "title": "Τα μπαλόνια για το πάρτι", "title_en": "The balloons for the party", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από το κατάστημα όπου παραγγείλατε διακόσμηση για ένα παιδικό πάρτι.",
 "script": [
  L("Υπάλληλος", "m", "Γεια σας, από το κατάστημα με τα είδη πάρτι σας παίρνω, για την παραγγελία σας για το Σάββατο. Δυστυχώς, ο προμηθευτής μας δεν έχει αυτή την εβδομάδα ήλιο, οπότε δεν μπορούμε να σας δώσουμε τα μπαλόνια που πετάνε.", "Hello, I'm calling from the party shop about your order for Saturday. Unfortunately our supplier has no helium this week, so we can't give you the balloons that float."),
  L("Υπάλληλος", "m", "Σας προτείνω δύο λύσεις. Μπορούμε να φτιάξουμε μια αψίδα με μπαλόνια γεμάτα αέρα, που στηρίζεται σε μια βάση και μπαίνει στην είσοδο. Ή μπορούμε να κρεμάσουμε τα μπαλόνια από το ταβάνι με διάφανη κλωστή, κι έτσι μοιάζουν σαν να πετάνε.", "I can suggest two solutions. We can make an arch of air-filled balloons, which stands on a base and goes at the entrance. Or we can hang the balloons from the ceiling with clear thread, so they look as if they're floating."),
  L("Υπάλληλος", "m", "Και οι δύο λύσεις κοστίζουν το ίδιο με την αρχική παραγγελία. Επιπλέον, τα μπαλόνια με αέρα κρατάνε πολύ περισσότερο, ενώ με το ήλιο πέφτουν σε μία με δύο μέρες. Πείτε μου τι προτιμάτε ως την Πέμπτη το μεσημέρι.", "Both solutions cost the same as the original order. What's more, air-filled balloons last much longer, while with helium they drop in a day or two. Tell me which you prefer by Thursday midday."),
 ],
 "questions": [
  Q("Γιατί δεν μπορούν να δώσουν τα μπαλόνια που πετάνε;", ["Γιατί το κατάστημα είναι κλειστό το Σάββατο", "Γιατί ο προμηθευτής δεν έχει ήλιο αυτή την εβδομάδα", "Γιατί τα μπαλόνια τελείωσαν", "Γιατί είναι επικίνδυνα για παιδιά"], 1, "ο προμηθευτής μας δεν έχει αυτή την εβδομάδα ήλιο"),
  Q("Πώς μπορούν να δώσουν την εντύπωση ότι τα μπαλόνια πετάνε;", ["Κρεμώντας τα από το ταβάνι με διάφανη κλωστή", "Δένοντάς τα στις καρέκλες", "Γεμίζοντάς τα με ζεστό αέρα", "Βάζοντάς τα σε μια αψίδα"], 0, "να κρεμάσουμε τα μπαλόνια από το ταβάνι με διάφανη κλωστή"),
  Q("Ποιο πλεονέκτημα έχουν τα μπαλόνια με αέρα;", ["Είναι φθηνότερα", "Έχουν περισσότερα χρώματα", "Κρατάνε πολύ περισσότερο", "Δεν σκάνε"], 2, "τα μπαλόνια με αέρα κρατάνε πολύ περισσότερο"),
 ],
 "gloss": {"διακόσμηση": "διακόσμηση — decoration", "είδη πάρτι": "είδη πάρτι — party supplies", "προμηθευτής": "προμηθευτής — supplier", "ήλιο": "ήλιο — helium", "μπαλόνια": "μπαλόνι — balloon", "αψίδα": "αψίδα — arch", "ταβάνι": "ταβάνι — ceiling", "διάφανη": "διάφανος — clear, transparent", "κλωστή": "κλωστή — thread", "αρχική": "αρχικός — original, initial"},
})

ITEMS.append({
 "id": "l158-dia-exypno-roloi", "title": "Ένα έξυπνο ρολόι για τη γιαγιά", "title_en": "A smartwatch for grandma", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε μια γιαγιά να συζητάει με τον εγγονό της για ένα έξυπνο ρολόι που της έκαναν δώρο.",
 "script": [
  L("Γιαγιά", "f", "Πέτρο μου, αυτό το ρολόι που μου πήρατε δεν σταματάει να βουίζει. Το ένα λεπτό μού λέει να σηκωθώ, το άλλο να πιω νερό. Σαν τη μητέρα μου είναι!", "Petros dear, this watch you got me never stops buzzing. One minute it tells me to get up, the next to drink water. It's like my mother!"),
  L("Πέτρος", "m", "Αυτές τις ειδοποιήσεις μπορώ να τις κλείσω, γιαγιά. Το ρολόι σού το πήραμε για άλλο λόγο: αν πέσεις και δεν σηκωθείς, το καταλαβαίνει και στέλνει μόνο του μήνυμα στη μαμά και σε μένα, με το πού βρίσκεσαι.", "I can turn those notifications off, grandma. We got you the watch for another reason: if you fall and don't get up, it notices and sends a message by itself to mum and me, with where you are."),
  L("Γιαγιά", "f", "Δηλαδή θα ξέρετε πού πηγαίνω όλη μέρα; Ούτε στο καφενείο δεν θα μπορώ να πάω χωρίς να το μάθετε;", "So you'll know where I go all day? I won't even be able to go to the café without you finding out?"),
  L("Πέτρος", "m", "Όχι, η τοποθεσία στέλνεται μόνο όταν υπάρχει πρόβλημα. Και αν θέλεις να μας ειδοποιήσεις εσύ, πατάς αυτό το κουμπί στο πλάι για τρία δευτερόλεπτα.", "No, the location is only sent when there's a problem. And if you want to alert us yourself, you press this button on the side for three seconds."),
  L("Γιαγιά", "f", "Καλά, θα το φοράω. Αλλά το βράδυ το βγάζω, να το ξέρεις· δεν κοιμάμαι με χειροπέδες!", "All right, I'll wear it. But I take it off at night, I'm telling you; I don't sleep in handcuffs!"),
 ],
 "questions": [
  Q("Τι ενοχλεί τη γιαγιά στο ρολόι;", ["Ότι είναι βαρύ", "Ότι δεν σταματάει να βουίζει με ειδοποιήσεις", "Ότι δείχνει λάθος ώρα", "Ότι δεν βλέπει τα γράμματα"], 1, "δεν σταματάει να βουίζει"),
  Q("Για ποιον λόγο της πήραν το ρολόι;", ["Για να μετράει τα βήματά της", "Για να της θυμίζει τα φάρμακα", "Για να ειδοποιεί την οικογένεια αν πέσει και δεν σηκωθεί", "Για να μιλάει στο τηλέφωνο"], 2, "αν πέσεις και δεν σηκωθείς, το καταλαβαίνει"),
  Q("Πότε στέλνεται η τοποθεσία της;", ["Συνέχεια", "Μόνο όταν υπάρχει πρόβλημα", "Κάθε βράδυ", "Όταν πηγαίνει στο καφενείο"], 1, "η τοποθεσία στέλνεται μόνο όταν υπάρχει πρόβλημα"),
 ],
 "gloss": {"έξυπνο ρολόι": "έξυπνο ρολόι — smartwatch", "βουίζει": "βουίζω — to buzz", "ειδοποιήσεις": "ειδοποίηση — notification", "τοποθεσία": "τοποθεσία — location", "κουμπί": "κουμπί — button", "δευτερόλεπτα": "δευτερόλεπτο — second", "χειροπέδες": "χειροπέδες — handcuffs"},
})

ITEMS.append({
 "id": "l158-dia-lista-gamou", "title": "Λίστα γάμου ή φάκελος;", "title_en": "Wedding list or an envelope?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους να συζητούν τι δώρο θα κάνουν σε ένα ζευγάρι που παντρεύεται.",
 "script": [
  L("Κατερίνα", "f", "Ο Άγγελος και η Νεφέλη έχουν λίστα γάμου σε ένα κατάστημα με είδη σπιτιού. Μπήκα στη σελίδα και τα φτηνά πράγματα τα έχουν πάρει ήδη. Έμειναν μια κατσαρόλα των διακοσίων ευρώ και ένα σερβίτσιο.", "Angelos and Nefeli have a wedding list at a homeware shop. I went on the website and the cheap things have already been taken. What's left is a two-hundred-euro saucepan and a dinner service."),
  L("Ηλίας", "m", "Διακόσια ευρώ για μια κατσαρόλα; Εγώ λέω να τους δώσουμε χρήματα σε φάκελο. Έτσι κι αλλιώς μαζεύουν για το ταξίδι του μέλιτος.", "Two hundred euros for a saucepan? I say we give them money in an envelope. They're saving for the honeymoon anyway."),
  L("Κατερίνα", "f", "Το σκέφτηκα, αλλά μου φαίνεται λίγο απρόσωπο. Θέλω να έχουν κάτι στο σπίτι και να θυμούνται ότι είναι από εμάς.", "I thought about it, but it seems a bit impersonal to me. I want them to have something in the house and remember that it's from us."),
  L("Ηλίας", "m", "Τότε ας μοιραστούμε την κατσαρόλα οι δυο μας. Εκατό ο καθένας, και γράφουμε και μια κάρτα με μια συνταγή που να τη μαγειρεύουν σε αυτήν.", "Then let's split the saucepan between the two of us. A hundred each, and we'll write a card too, with a recipe for them to cook in it."),
  L("Κατερίνα", "f", "Τέλεια ιδέα. Τη συνταγή για το γιουβέτσι της γιαγιάς μου, που ο Άγγελος τρώει πάντα δύο πιάτα.", "Perfect idea. The recipe for my grandmother's giouvetsi, which Angelos always has two plates of."),
 ],
 "questions": [
  Q("Τι έχει μείνει στη λίστα γάμου;", ["Μόνο φτηνά πράγματα", "Μια ακριβή κατσαρόλα και ένα σερβίτσιο", "Ένα ταξίδι", "Τίποτα"], 1, "Έμειναν μια κατσαρόλα των διακοσίων ευρώ και ένα σερβίτσιο"),
  Q("Γιατί η Κατερίνα δεν θέλει να δώσει χρήματα;", ["Γιατί δεν έχει", "Γιατί της φαίνεται λίγο απρόσωπο", "Γιατί το ζευγάρι το απαγόρευσε", "Γιατί το θεωρεί αγένεια"], 1, "μου φαίνεται λίγο απρόσωπο"),
  Q("Τι αποφασίζουν τελικά;", ["Να δώσει ο καθένας φάκελο", "Να αγοράσουν το σερβίτσιο", "Να μοιραστούν την κατσαρόλα και να γράψουν μια κάρτα με μια συνταγή", "Να πληρώσουν μέρος του ταξιδιού"], 2, "ας μοιραστούμε την κατσαρόλα οι δυο μας"),
 ],
 "gloss": {"λίστα γάμου": "λίστα γάμου — wedding list", "φάκελο": "φάκελος — envelope", "κατσαρόλα": "κατσαρόλα — saucepan, pot", "σερβίτσιο": "σερβίτσιο — dinner service", "ταξίδι του μέλιτος": "ταξίδι του μέλιτος — honeymoon", "απρόσωπο": "απρόσωπος — impersonal", "μοιραστούμε": "μοιράζομαι — to share, to split", "συνταγή": "συνταγή — recipe", "γιουβέτσι": "γιουβέτσι — giouvetsi (meat baked with orzo)"},
})

ITEMS.append({
 "id": "l158-int-ammoglyptis", "title": "Γλυπτά από άμμο", "title_en": "Sculptures made of sand", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν καλλιτέχνη που φτιάχνει γλυπτά από άμμο σε φεστιβάλ.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι χρειάζεται για να φτιάξει κανείς ένα γλυπτό από άμμο;", "What does it take to make a sculpture from sand?"),
  L("Γλύπτης", "m", "Πρώτα απ' όλα, τη σωστή άμμο. Η άμμος της παραλίας είναι συνήθως πολύ στρογγυλή, γιατί τη γυαλίζει η θάλασσα, και δεν κολλάει καλά. Εμείς χρησιμοποιούμε άμμο από ποτάμι ή από λατομείο, με κόκκους που έχουν γωνίες.", "First of all, the right sand. Beach sand is usually too round, because the sea polishes it, and it doesn't stick well. We use sand from a river or a quarry, with grains that have corners."),
  L("Δημοσιογράφος", "f", "Και πώς στέκεται τόσο ψηλά;", "And how does it stand so tall?"),
  L("Γλύπτης", "m", "Βάζουμε την άμμο με νερό σε μεγάλα ξύλινα καλούπια και την πατάμε σε διαδοχικά στρώματα, μέχρι να γίνει σκληρή σαν πέτρα. Μετά βγάζουμε τα καλούπια και σκαλίζουμε από πάνω προς τα κάτω, για να μην πέφτει η άμμος πάνω σε ό,τι έχουμε ήδη τελειώσει.", "We put the sand with water into large wooden moulds and tamp it down, in successive layers, until it becomes as hard as stone. Then we remove the moulds and carve from top to bottom, so that the sand doesn't fall onto what we've already finished."),
  L("Δημοσιογράφος", "f", "Δεν σας στενοχωρεί που όλα αυτά χάνονται;", "Doesn't it upset you that all this disappears?"),
  L("Γλύπτης", "m", "Στο τέλος τα ψεκάζουμε με νερό και λίγη κόλλα, κι έτσι αντέχουν μερικές εβδομάδες, εκτός αν πέσει δυνατή βροχή. Αλλά αυτό είναι και η ομορφιά τους: ο κόσμος ξέρει ότι πρέπει να έρθει να τα δει τώρα.", "At the end we spray them with water and a little glue, so they last a few weeks, unless there's heavy rain. But that's also their beauty: people know they have to come and see them now."),
 ],
 "questions": [
  Q("Γιατί η άμμος της παραλίας δεν είναι κατάλληλη;", ["Γιατί έχει αλάτι", "Γιατί είναι πολύ στρογγυλή και δεν κολλάει καλά", "Γιατί είναι πολύ βρεγμένη", "Γιατί απαγορεύεται να την πάρεις"], 1, "Η άμμος της παραλίας είναι συνήθως πολύ στρογγυλή"),
  Q("Γιατί σκαλίζουν από πάνω προς τα κάτω;", ["Για να μην πέφτει η άμμος πάνω σε ό,τι έχουν ήδη τελειώσει", "Γιατί έτσι είναι πιο γρήγορο", "Γιατί η κορυφή είναι πιο μαλακή", "Για να το βλέπει το κοινό"], 0, "για να μην πέφτει η άμμος πάνω σε ό,τι έχουμε ήδη τελειώσει"),
  Q("Πόσο αντέχουν τα γλυπτά;", ["Μία μέρα", "Μερικές εβδομάδες, εκτός αν πέσει δυνατή βροχή", "Χρόνια", "Μέχρι το επόμενο καλοκαίρι"], 1, "αντέχουν μερικές εβδομάδες, εκτός αν πέσει δυνατή βροχή"),
 ],
 "gloss": {"γλυπτά": "γλυπτό — sculpture", "γλυπτό": "γλυπτό — sculpture", "γυαλίζει": "γυαλίζω — to polish", "λατομείο": "λατομείο — quarry", "κόκκους": "κόκκος — grain", "καλούπια": "καλούπι — mould, form", "στρώματα": "στρώμα — layer", "σκαλίζουμε": "σκαλίζω — to carve", "στενοχωρεί": "στενοχωρώ — to upset", "ψεκάζουμε": "ψεκάζω — to spray", "κόλλα": "κόλλα — glue"},
})

ITEMS.append({
 "id": "l158-c1-el-farol", "title": "Θα πάω απόψε στο μπαρ;", "title_en": "Shall I go to the bar tonight?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από διάλεξη για τη θεωρία παιγνίων και την οικονομία της πολυπλοκότητας.",
 "script": [
  L("Καθηγητής", "m", "Το 1994 ο οικονομολόγος Μπράιαν Άρθουρ, που δούλευε στο Ινστιτούτο της Σάντα Φε, δημοσίευσε ένα πρόβλημα εμπνευσμένο από ένα μπαρ της πόλης, το Ελ Φαρόλ, όπου τις Πέμπτες έπαιζε ιρλανδική μουσική. Ας υποθέσουμε ότι εκατό άνθρωποι θέλουν να πάνε. Αν πάνε λιγότεροι από εξήντα, περνούν υπέροχα· αν πάνε περισσότεροι, το μαγαζί είναι ασφυκτικά γεμάτο και θα ήταν καλύτερα να είχαν μείνει σπίτι.", "In 1994 the economist Brian Arthur, who worked at the Santa Fe Institute, published a problem inspired by a bar in the city, El Farol, where Irish music was played on Thursdays. Suppose that a hundred people want to go. If fewer than sixty go, they have a wonderful time; if more go, the place is packed to suffocation and they would have been better off staying at home."),
  L("Καθηγητής", "m", "Κανείς δεν ξέρει από πριν τι θα κάνουν οι άλλοι. Το ενδιαφέρον είναι ότι δεν υπάρχει καμία πρόβλεψη που να μπορούν να ακολουθήσουν όλοι με επιτυχία. Αν όλοι πιστέψουν ότι θα πάει λίγος κόσμος, θα πάνε όλοι, και το μπαρ θα γεμίσει· αν όλοι πιστέψουν ότι θα γεμίσει, θα μείνουν όλοι σπίτι, και το μπαρ θα αδειάσει. Κάθε κοινή πρόβλεψη αναιρεί τον εαυτό της.", "No one knows in advance what the others will do. The interesting thing is that there is no forecast that everyone can follow successfully. If everyone believes that few people will go, everyone will go, and the bar will fill up; if everyone believes it will fill up, everyone will stay home, and the bar will be empty. Every shared forecast defeats itself."),
  L("Καθηγητής", "m", "Ο Άρθουρ ήθελε να δείξει ότι σε τέτοιες καταστάσεις η κλασική υπόθεση του απόλυτα ορθολογικού ατόμου, που βρίσκει τη λύση με καθαρή λογική, δεν βοηθάει. Στις προσομοιώσεις του έδωσε σε κάθε άτομο διαφορετικούς απλούς κανόνες πρόβλεψης, που τους εγκατέλειπε όταν αποτύγχαναν. Το αποτέλεσμα ήταν ότι η προσέλευση κυμαινόταν γύρω από τους εξήντα, χωρίς κανείς να το έχει σχεδιάσει.", "Arthur wanted to show that in such situations the classical assumption of the perfectly rational individual, who finds the solution by pure logic, does not help. In his simulations he gave each individual different simple forecasting rules, which they abandoned when they failed. The result was that attendance fluctuated around sixty, without anyone having planned it."),
  L("Καθηγητής", "m", "Το πρόβλημα μοιάζει παιχνίδι, αλλά περιγράφει πολλές πραγματικές καταστάσεις: ποιον δρόμο θα πάρουμε για να αποφύγουμε την κίνηση, πότε θα πάμε στο σούπερ μάρκετ, ακόμη και πότε θα αγοράσουμε ή θα πουλήσουμε μετοχές. Παντού όπου η καλύτερη επιλογή είναι να κάνεις ό,τι δεν κάνουν οι περισσότεροι.", "The problem looks like a game, but it describes many real situations: which road to take to avoid traffic, when to go to the supermarket, even when to buy or sell shares. Anywhere the best choice is to do what most people are not doing."),
 ],
 "questions": [
  Q("Τι συμβαίνει, σύμφωνα με το πρόβλημα, αν πάνε στο μπαρ περισσότεροι από εξήντα;", ["Περνούν υπέροχα", "Το μαγαζί είναι ασφυκτικά γεμάτο και θα ήταν καλύτερα να είχαν μείνει σπίτι", "Το μπαρ κλείνει", "Πληρώνουν περισσότερα"], 1, "το μαγαζί είναι ασφυκτικά γεμάτο"),
  Q("Γιατί δεν υπάρχει πρόβλεψη που να μπορούν να ακολουθήσουν όλοι με επιτυχία;", ["Γιατί κανείς δεν ξέρει πόσοι χωράνε", "Γιατί κάθε κοινή πρόβλεψη αναιρεί τον εαυτό της", "Γιατί η μουσική αλλάζει κάθε εβδομάδα", "Γιατί οι άνθρωποι δεν σκέφτονται λογικά"], 1, "Κάθε κοινή πρόβλεψη αναιρεί τον εαυτό της"),
  Q("Τι έδειξαν οι προσομοιώσεις του Άρθουρ;", ["Ότι η προσέλευση κυμαινόταν γύρω από τους εξήντα χωρίς κανείς να το έχει σχεδιάσει", "Ότι το μπαρ γέμιζε κάθε φορά", "Ότι κανείς δεν πήγαινε ποτέ", "Ότι οι ορθολογικοί παίκτες έβρισκαν πάντα τη λύση"], 0, "η προσέλευση κυμαινόταν γύρω από τους εξήντα"),
  Q("Πού αλλού, κατά τον καθηγητή, εμφανίζεται το ίδιο πρόβλημα;", ["Μόνο στα μπαρ", "Στις εκλογές", "Όπου η καλύτερη επιλογή είναι να κάνεις ό,τι δεν κάνουν οι περισσότεροι", "Όπου όλοι συμφωνούν"], 2, "η καλύτερη επιλογή είναι να κάνεις ό,τι δεν κάνουν οι περισσότεροι"),
 ],
 "gloss": {"θεωρία παιγνίων": "θεωρία παιγνίων — game theory", "πολυπλοκότητας": "πολυπλοκότητα — complexity", "εμπνευσμένο": "εμπνευσμένος — inspired", "ασφυκτικά": "ασφυκτικά — suffocatingly; ασφυκτικά γεμάτο = packed", "πρόβλεψη": "πρόβλεψη — forecast, prediction", "αναιρεί": "αναιρώ — to cancel out, to refute", "ορθολογικού": "ορθολογικός — rational", "προσομοιώσεις": "προσομοίωση — simulation", "εγκατέλειπε": "εγκαταλείπω — to abandon", "προσέλευση": "προσέλευση — attendance, turnout", "κυμαινόταν": "κυμαίνομαι — to fluctuate", "μετοχές": "μετοχή — share (stock)"},
})

ITEMS.append({
 "id": "l158-c1-proteus", "title": "Γινόμαστε αυτό που δείχνει η οθόνη;", "title_en": "Do we become what the screen shows?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια ερευνήτρια της ψυχολογίας των μέσων για το λεγόμενο φαινόμενο του Πρωτέα.",
 "script": [
  L("Δημοσιογράφος", "m", "Από πού πήρε το όνομά του αυτό το φαινόμενο;", "Where did this effect get its name?"),
  L("Ερευνήτρια", "f", "Από τον Πρωτέα, τον θαλάσσιο θεό της Οδύσσειας που άλλαζε μορφή όποτε ήθελε. Το όρισαν το 2007 δύο ερευνητές του Στάνφορντ, ο Νικ Γι και ο Τζέρεμι Μπέιλενσον. Παρατήρησαν ότι η εμφάνιση του ψηφιακού μας ομοιώματος, του άβαταρ, επηρεάζει το πώς συμπεριφερόμαστε μέσα στον εικονικό κόσμο.", "From Proteus, the sea god of the Odyssey who changed shape whenever he wished. It was defined in 2007 by two Stanford researchers, Nick Yee and Jeremy Bailenson. They observed that the appearance of our digital likeness, the avatar, affects how we behave inside the virtual world."),
  L("Δημοσιογράφος", "m", "Δηλαδή;", "Meaning?"),
  L("Ερευνήτρια", "f", "Σε ένα πείραμα, όσοι είχαν πιο ελκυστικό άβαταρ πλησίαζαν περισσότερο έναν άγνωστο και αποκάλυπταν περισσότερα για τον εαυτό τους. Σε ένα άλλο, όσοι είχαν ψηλότερο άβαταρ διαπραγματεύονταν πιο σκληρά για το πώς θα μοιραστεί ένα χρηματικό ποσό. Το εντυπωσιακό είναι ότι οι συμμετέχοντες δεν ήξεραν ότι αυτό εξεταζόταν, και η εμφάνιση του άβαταρ τους είχε δοθεί τυχαία.", "In one experiment, those who had a more attractive avatar moved closer to a stranger and disclosed more about themselves. In another, those with a taller avatar negotiated harder over how a sum of money would be shared. What's striking is that the participants didn't know this was being examined, and their avatar's appearance had been assigned at random."),
  L("Δημοσιογράφος", "m", "Και έξω από την οθόνη;", "And outside the screen?"),
  L("Ερευνήτρια", "f", "Εκεί τα στοιχεία είναι πιο αμφιλεγόμενα. Σε μια μελέτη, όσοι είχαν δει ένα ψηφιακά γερασμένο πρόσωπο του εαυτού τους δήλωναν διατεθειμένοι να αποταμιεύουν περισσότερα για τη σύνταξή τους. Αλλά δεν ξέρουμε πόσο διαρκούν τέτοιες επιδράσεις. Το βέβαιο είναι ότι η εικόνα που υιοθετούμε δεν είναι απλώς μια μάσκα· μας λέει, σε κάποιον βαθμό, ποιοι υποτίθεται ότι είμαστε.", "There the evidence is more contested. In one study, people who had seen a digitally aged face of themselves said they were willing to save more for their retirement. But we don't know how long such effects last. What is certain is that the image we adopt is not just a mask; it tells us, to some degree, who we are supposed to be."),
 ],
 "questions": [
  Q("Γιατί το φαινόμενο πήρε το όνομα του Πρωτέα;", ["Γιατί ήταν θεός της τεχνολογίας", "Γιατί άλλαζε μορφή όποτε ήθελε", "Γιατί ήταν ο πρώτος θεός", "Γιατί ζούσε σε έναν εικονικό κόσμο"], 1, "άλλαζε μορφή όποτε ήθελε"),
  Q("Τι έκαναν όσοι είχαν πιο ελκυστικό άβαταρ;", ["Απέφευγαν τους άλλους", "Πλησίαζαν περισσότερο έναν άγνωστο και αποκάλυπταν περισσότερα για τον εαυτό τους", "Διαπραγματεύονταν πιο σκληρά", "Έπαιζαν περισσότερη ώρα"], 1, "πλησίαζαν περισσότερο έναν άγνωστο και αποκάλυπταν περισσότερα για τον εαυτό τους"),
  Q("Γιατί είναι εντυπωσιακά τα αποτελέσματα, κατά την ερευνήτρια;", ["Γιατί οι συμμετέχοντες διάλεγαν μόνοι τους το άβαταρ", "Γιατί οι συμμετέχοντες δεν ήξεραν τι εξεταζόταν και το άβαταρ είχε δοθεί τυχαία", "Γιατί τα πειράματα κράτησαν χρόνια", "Γιατί όλοι οι συμμετέχοντες ήταν παίκτες βιντεοπαιχνιδιών"], 1, "οι συμμετέχοντες δεν ήξεραν ότι αυτό εξεταζόταν"),
  Q("Τι λέει η ερευνήτρια για τις επιδράσεις έξω από την οθόνη;", ["Ότι είναι αποδεδειγμένες και μόνιμες", "Ότι δεν υπάρχουν καθόλου", "Ότι τα στοιχεία είναι πιο αμφιλεγόμενα και δεν ξέρουμε πόσο διαρκούν", "Ότι αφορούν μόνο τα παιδιά"], 2, "τα στοιχεία είναι πιο αμφιλεγόμενα"),
 ],
 "gloss": {"ψυχολογίας των μέσων": "ψυχολογία των μέσων — media psychology", "μορφή": "μορφή — shape, form", "όρισαν": "ορίζω — to define", "ομοιώματος": "ομοίωμα — likeness, effigy", "άβαταρ": "άβαταρ — avatar", "εικονικό": "εικονικός — virtual", "ελκυστικό": "ελκυστικός — attractive", "αποκάλυπταν": "αποκαλύπτω — to reveal, to disclose", "διαπραγματεύονταν": "διαπραγματεύομαι — to negotiate", "αμφιλεγόμενα": "αμφιλεγόμενος — contested, controversial", "γερασμένο": "γερασμένος — aged", "διατεθειμένοι": "διατεθειμένος — willing", "αποταμιεύουν": "αποταμιεύω — to save (money)", "υιοθετούμε": "υιοθετώ — to adopt"},
})

rnd = random.Random(158)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-158.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
