# Source for library/listening/listening-162.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l162.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l162-ann-xionopedila", "title": "Ανακοίνωση πριν από την πεζοπορία με χιονοπέδιλα", "title_en": "An announcement before the snowshoe hike", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε τον αρχηγό ενός ορειβατικού συλλόγου να μιλάει στους συμμετέχοντες πριν από μια χειμερινή πεζοπορία.",
 "script": [
  L("Αρχηγός", "m", "Καλημέρα σε όλους. Πριν ξεκινήσουμε, ελέγξτε ότι τα χιονοπέδιλα είναι καλά δεμένα στα παπούτσια σας. Αν κάποιο λουρί είναι χαλαρό, θα το καταλάβετε μετά από διακόσια μέτρα, και τότε θα είναι αργά.", "Good morning, everyone. Before we set off, check that the snowshoes are tightly fastened to your boots. If a strap is loose, you'll notice it after two hundred metres, and then it will be too late."),
  L("Αρχηγός", "m", "Η διαδρομή είναι οκτώ χιλιόμετρα και θα κρατήσει περίπου τέσσερις ώρες. Θα κάνουμε στάση για φαγητό στο καταφύγιο, όπου υπάρχει τζάκι και ζεστό τσάι. Μην περιμένετε να διψάσετε για να πιείτε νερό· στο κρύο ο οργανισμός χάνει υγρά χωρίς να το καταλαβαίνουμε.", "The route is eight kilometres and will take about four hours. We'll stop to eat at the refuge, where there is a fireplace and hot tea. Don't wait until you're thirsty to drink water; in the cold the body loses fluids without our noticing."),
  L("Αρχηγός", "m", "Κανείς δεν προσπερνά τον πρώτο της ομάδας και κανείς δεν μένει πίσω από τον τελευταίο, που είναι η Ελπίδα με το κόκκινο μπουφάν. Αν ο καιρός χαλάσει, γυρίζουμε πίσω χωρίς συζήτηση· το βουνό θα είναι εδώ και την επόμενη Κυριακή.", "Nobody overtakes the leader of the group and nobody stays behind the last person, who is Elpida in the red jacket. If the weather turns bad, we turn back without discussion; the mountain will still be here next Sunday."),
 ],
 "questions": [
  Q("Τι πρέπει να ελέγξουν οι πεζοπόροι πριν ξεκινήσουν;", ["Ότι έχουν φακό", "Ότι τα χιονοπέδιλα είναι καλά δεμένα", "Ότι έχουν φορτίσει το κινητό", "Ότι έχουν χάρτη"], 1, "ελέγξτε ότι τα χιονοπέδιλα είναι καλά δεμένα στα παπούτσια σας"),
  Q("Γιατί πρέπει να πίνουν νερό ακόμη κι αν δεν διψάνε;", ["Γιατί στο κρύο ο οργανισμός χάνει υγρά χωρίς να το καταλαβαίνουμε", "Γιατί το καταφύγιο δεν έχει νερό", "Γιατί η διαδρομή είναι ανηφορική", "Γιατί το νερό θα παγώσει"], 0, "στο κρύο ο οργανισμός χάνει υγρά χωρίς να το καταλαβαίνουμε"),
  Q("Τι θα γίνει αν χαλάσει ο καιρός;", ["Θα περιμένουν στο καταφύγιο", "Θα συνεχίσουν πιο αργά", "Θα γυρίσουν πίσω χωρίς συζήτηση", "Θα πάρουν άλλη διαδρομή"], 2, "γυρίζουμε πίσω χωρίς συζήτηση"),
 ],
 "gloss": {"αρχηγό": "αρχηγός — leader", "χειμερινή": "χειμερινός — winter (adj.)", "πεζοπορία": "πεζοπορία — hike", "χιονοπέδιλα": "χιονοπέδιλο — snowshoe", "δεμένα": "δεμένος — tied, fastened", "λουρί": "λουρί — strap", "χαλαρό": "χαλαρός — loose", "καταφύγιο": "καταφύγιο — (mountain) refuge", "τζάκι": "τζάκι — fireplace", "οργανισμός": "οργανισμός — body, organism", "υγρά": "υγρά — fluids", "μπουφάν": "μπουφάν — jacket"},
})

ITEMS.append({
 "id": "l162-int-3d", "title": "Χέρια από τον εκτυπωτή", "title_en": "Hands from the printer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν εθελοντή που φτιάχνει προσθετικά χέρια για παιδιά με τρισδιάστατο εκτυπωτή.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς ξεκίνησε όλο αυτό;", "How did all this start?"),
  L("Εθελοντής", "m", "Είχα έναν τρισδιάστατο εκτυπωτή για να φτιάχνω ανταλλακτικά για μοντέλα αεροπλάνων. Κάποια στιγμή διάβασα ότι υπάρχει ένα διεθνές δίκτυο εθελοντών που μοιράζεται δωρεάν σχέδια για απλά πλαστικά χέρια. Το πρώτο το έφτιαξα για ένα κορίτσι επτά χρονών από τη γειτονιά μου.", "I had a 3D printer to make spare parts for model aeroplanes. At some point I read that there is an international network of volunteers that shares free designs for simple plastic hands. I made the first one for a seven-year-old girl from my neighbourhood."),
  L("Δημοσιογράφος", "f", "Πώς λειτουργεί ένα τέτοιο χέρι;", "How does such a hand work?"),
  L("Εθελοντής", "m", "Δεν έχει μπαταρίες ούτε ηλεκτρονικά. Όταν το παιδί λυγίζει τον καρπό, κάτι κορδόνια μέσα στα δάχτυλα τεντώνονται και το χέρι κλείνει. Έτσι μπορεί να πιάσει ένα μπουκάλι ή μια μπάλα. Δεν αντικαθιστά ένα ιατρικό πρόσθετο μέλος, αλλά κοστίζει ελάχιστα και τυπώνεται σε μια μέρα.", "It has no batteries or electronics. When the child bends the wrist, some cords inside the fingers tighten and the hand closes. That way they can grab a bottle or a ball. It doesn't replace a medical prosthetic limb, but it costs very little and is printed in a day."),
  L("Δημοσιογράφος", "f", "Γιατί είναι σημαντικό για τα παιδιά;", "Why is it important for children?"),
  L("Εθελοντής", "m", "Γιατί μεγαλώνουν γρήγορα και ένα ακριβό πρόσθετο μέλος σε έναν χρόνο δεν τους κάνει πια. Και κάτι ακόμα: τα παιδιά διαλέγουν το χρώμα. Πολλά το θέλουν σαν χέρι υπερήρωα, και στο σχολείο οι συμμαθητές τους, αντί να τα λυπούνται, τα ζηλεύουν.", "Because they grow quickly and an expensive prosthetic limb no longer fits them after a year. And one more thing: the children choose the colour. Many want it like a superhero's hand, and at school their classmates, instead of feeling sorry for them, envy them."),
 ],
 "questions": [
  Q("Για ποιον λόγο είχε αρχικά τον τρισδιάστατο εκτυπωτή;", ["Για τη δουλειά του σε ένα νοσοκομείο", "Για να φτιάχνει ανταλλακτικά για μοντέλα αεροπλάνων", "Για να τυπώνει παιχνίδια για τα παιδιά του", "Για ένα μάθημα στο πανεπιστήμιο"], 1, "για να φτιάχνω ανταλλακτικά για μοντέλα αεροπλάνων"),
  Q("Πώς κλείνει το πλαστικό χέρι;", ["Με ένα μικρό μοτέρ", "Όταν το παιδί λυγίζει τον καρπό και τεντώνονται κορδόνια μέσα στα δάχτυλα", "Με ένα κουμπί", "Με τη βοήθεια του άλλου χεριού"], 1, "Όταν το παιδί λυγίζει τον καρπό, κάτι κορδόνια μέσα στα δάχτυλα τεντώνονται"),
  Q("Γιατί, κατά τον εθελοντή, οι συμμαθητές ζηλεύουν τα παιδιά;", ["Γιατί δεν κάνουν γυμναστική", "Γιατί παίρνουν δώρα", "Γιατί το χέρι τους μοιάζει με χέρι υπερήρωα", "Γιατί βγαίνουν στην τηλεόραση"], 2, "Πολλά το θέλουν σαν χέρι υπερήρωα"),
 ],
 "gloss": {"εθελοντή": "εθελοντής — volunteer", "προσθετικά": "προσθετικός — prosthetic", "τρισδιάστατο": "τρισδιάστατος — three-dimensional", "εκτυπωτή": "εκτυπωτής — printer", "ανταλλακτικά": "ανταλλακτικό — spare part", "δίκτυο": "δίκτυο — network", "λυγίζει": "λυγίζω — to bend", "καρπό": "καρπός — wrist", "κορδόνια": "κορδόνι — cord, lace", "τεντώνονται": "τεντώνομαι — to tighten, to stretch", "πρόσθετο μέλος": "πρόσθετο μέλος — prosthetic limb", "τυπώνεται": "τυπώνομαι — to be printed", "υπερήρωα": "υπερήρωας — superhero"},
})

ITEMS.append({
 "id": "l162-int-ydrogono", "title": "Λεωφορεία που βγάζουν μόνο νερό", "title_en": "Buses that emit only water", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια μηχανικό συγκοινωνιών για τα λεωφορεία με υδρογόνο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς κινείται ένα λεωφορείο με υδρογόνο;", "How does a hydrogen bus move?"),
  L("Μηχανικός", "f", "Στην ουσία είναι ηλεκτρικό λεωφορείο. Η διαφορά είναι ότι τον ηλεκτρισμό δεν τον παίρνει από μια μεγάλη μπαταρία, αλλά τον παράγει μόνο του, σε μια κυψέλη καυσίμου, όπου το υδρογόνο ενώνεται με το οξυγόνο του αέρα. Από την εξάτμιση βγαίνει μόνο υδρατμός.", "Essentially it's an electric bus. The difference is that it doesn't take the electricity from a big battery, but produces it itself, in a fuel cell, where hydrogen combines with oxygen from the air. Only water vapour comes out of the exhaust."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πλεονέκτημα σε σχέση με τα λεωφορεία με μπαταρία;", "What is the advantage compared with battery buses?"),
  L("Μηχανικός", "f", "Ο ανεφοδιασμός γίνεται σε λίγα λεπτά, όπως με το πετρέλαιο, ενώ μια μεγάλη μπαταρία θέλει ώρες για να φορτίσει. Γι' αυτό τα λεωφορεία με υδρογόνο ταιριάζουν σε μεγάλες διαδρομές ή σε ορεινές γραμμές, όπου η μπαταρία αδειάζει γρήγορα.", "Refuelling takes a few minutes, as with diesel, whereas a big battery needs hours to charge. That's why hydrogen buses suit long routes or mountain lines, where the battery runs down quickly."),
  L("Δημοσιογράφος", "m", "Και τα μειονεκτήματα;", "And the disadvantages?"),
  L("Μηχανικός", "f", "Είναι ακόμη ακριβά, και χρειάζονται ειδικούς σταθμούς ανεφοδιασμού. Το σημαντικότερο όμως είναι από πού έρχεται το υδρογόνο. Σήμερα το περισσότερο παράγεται από φυσικό αέριο, με εκπομπές διοξειδίου του άνθρακα. Το λεωφορείο είναι πραγματικά καθαρό μόνο αν το υδρογόνο παράγεται με ενέργεια από τον ήλιο ή τον αέρα.", "They're still expensive, and they need special refuelling stations. The most important thing, though, is where the hydrogen comes from. Today most of it is produced from natural gas, with carbon dioxide emissions. The bus is truly clean only if the hydrogen is produced with energy from the sun or the wind."),
 ],
 "questions": [
  Q("Τι βγαίνει από την εξάτμιση ενός λεωφορείου με υδρογόνο;", ["Καπνός", "Μόνο υδρατμός", "Διοξείδιο του άνθρακα", "Τίποτα"], 1, "Από την εξάτμιση βγαίνει μόνο υδρατμός"),
  Q("Ποιο είναι το πλεονέκτημα σε σχέση με τα λεωφορεία με μπαταρία;", ["Είναι φθηνότερα", "Ο ανεφοδιασμός γίνεται σε λίγα λεπτά", "Είναι πιο αθόρυβα", "Χωρούν περισσότερους επιβάτες"], 1, "Ο ανεφοδιασμός γίνεται σε λίγα λεπτά"),
  Q("Πότε είναι το λεωφορείο πραγματικά καθαρό, κατά τη μηχανικό;", ["Πάντα", "Όταν είναι καινούργιο", "Μόνο αν το υδρογόνο παράγεται με ενέργεια από τον ήλιο ή τον αέρα", "Όταν κινείται σε ορεινές γραμμές"], 2, "μόνο αν το υδρογόνο παράγεται με ενέργεια από τον ήλιο ή τον αέρα"),
 ],
 "gloss": {"συγκοινωνιών": "συγκοινωνίες — public transport", "υδρογόνο": "υδρογόνο — hydrogen", "κυψέλη καυσίμου": "κυψέλη καυσίμου — fuel cell", "οξυγόνο": "οξυγόνο — oxygen", "εξάτμιση": "εξάτμιση — exhaust (pipe)", "υδρατμός": "υδρατμός — water vapour", "πλεονέκτημα": "πλεονέκτημα — advantage", "ανεφοδιασμός": "ανεφοδιασμός — refuelling", "μειονεκτήματα": "μειονέκτημα — disadvantage", "φυσικό αέριο": "φυσικό αέριο — natural gas", "εκπομπές": "εκπομπή — emission", "διοξειδίου του άνθρακα": "διοξείδιο του άνθρακα — carbon dioxide"},
})

ITEMS.append({
 "id": "l162-dia-komitis", "title": "Ένας κομήτης με γυμνό μάτι;", "title_en": "A comet with the naked eye?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο συναδέλφους να συζητούν για έναν κομήτη που μπορεί να φανεί στον ουρανό.",
 "script": [
  L("Σταύρος", "m", "Είδες στις ειδήσεις για τον κομήτη; Λένε ότι ίσως φανεί με γυμνό μάτι την επόμενη εβδομάδα, λίγο μετά τη δύση του ήλιου.", "Did you see the news about the comet? They say it might be visible to the naked eye next week, just after sunset."),
  L("Ρούλα", "f", "Το «ίσως» με χαλάει. Θυμάμαι πριν από μερικά χρόνια, πάλι έλεγαν για ένα θέαμα του αιώνα, και τελικά δεν είδαμε τίποτα.", "The 'might' puts me off. I remember a few years ago, they were again talking about the spectacle of the century, and in the end we saw nothing."),
  L("Σταύρος", "m", "Οι κομήτες είναι απρόβλεπτοι. Είναι κομμάτια πάγου και σκόνης· όταν πλησιάζουν τον Ήλιο, ο πάγος εξατμίζεται και σχηματίζεται η ουρά. Κάποιοι λάμπουν περισσότερο απ' ό,τι περιμένουμε, άλλοι διαλύονται πριν φτάσουν.", "Comets are unpredictable. They're chunks of ice and dust; when they get close to the Sun, the ice evaporates and the tail forms. Some shine more than we expect, others break up before they arrive."),
  L("Ρούλα", "f", "Και πού πρέπει να κοιτάξουμε;", "And where should we look?"),
  L("Σταύρος", "m", "Χαμηλά στον ορίζοντα, προς τη δύση. Γι' αυτό λέω να πάμε στον λόφο πάνω από την πόλη, όπου δεν μας κρύβουν τα κτίρια και δεν υπάρχουν πολλά φώτα. Θα πάρω και τα κιάλια του πατέρα μου.", "Low on the horizon, towards the west. That's why I suggest we go to the hill above the town, where the buildings don't block our view and there aren't many lights. I'll bring my father's binoculars too."),
  L("Ρούλα", "f", "Εντάξει, αλλά αν δεν φανεί, κερνάς εσύ σουβλάκια.", "OK, but if it doesn't show up, you're buying the souvlaki."),
 ],
 "questions": [
  Q("Γιατί είναι επιφυλακτική η Ρούλα;", ["Γιατί δεν της αρέσει η αστρονομία", "Γιατί πριν από μερικά χρόνια περίμεναν ένα θέαμα και δεν είδαν τίποτα", "Γιατί θα δουλεύει εκείνο το βράδυ", "Γιατί φοβάται το σκοτάδι"], 1, "τελικά δεν είδαμε τίποτα"),
  Q("Πώς σχηματίζεται η ουρά ενός κομήτη, σύμφωνα με τον Σταύρο;", ["Από τη φωτιά της ατμόσφαιρας", "Ο πάγος εξατμίζεται όταν ο κομήτης πλησιάζει τον Ήλιο", "Από το φως της Σελήνης", "Από τη σύγκρουση με αστεροειδείς"], 1, "όταν πλησιάζουν τον Ήλιο, ο πάγος εξατμίζεται και σχηματίζεται η ουρά"),
  Q("Γιατί προτείνει ο Σταύρος να πάνε στον λόφο;", ["Γιατί εκεί είναι πιο ζεστά", "Γιατί εκεί υπάρχει τηλεσκόπιο", "Γιατί εκεί δεν τους κρύβουν τα κτίρια και δεν υπάρχουν πολλά φώτα", "Γιατί εκεί είναι ένα καλό σουβλατζίδικο"], 2, "όπου δεν μας κρύβουν τα κτίρια και δεν υπάρχουν πολλά φώτα"),
 ],
 "gloss": {"κομήτη": "κομήτης — comet", "κομήτες": "κομήτης — comet", "γυμνό μάτι": "με γυμνό μάτι — with the naked eye", "δύση": "δύση — sunset; west", "θέαμα": "θέαμα — spectacle", "απρόβλεπτοι": "απρόβλεπτος — unpredictable", "σκόνης": "σκόνη — dust", "εξατμίζεται": "εξατμίζομαι — to evaporate", "ουρά": "ουρά — tail", "λάμπουν": "λάμπω — to shine", "διαλύονται": "διαλύομαι — to break up, to disintegrate", "ορίζοντα": "ορίζοντας — horizon", "κερνάς": "κερνάω — to treat (someone to something)"},
})

ITEMS.append({
 "id": "l162-dia-elies", "title": "Ποιος θα μαζέψει τις ελιές;", "title_en": "Who will pick the olives?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέρφια να συζητούν τι θα κάνουν με τις ελιές του πατρικού τους κτήματος.",
 "script": [
  L("Μανώλης", "m", "Ο μπαμπάς λέει ότι φέτος δεν μπορεί να μαζέψει τις ελιές μόνος του. Τα γόνατά του δεν αντέχουν.", "Dad says that this year he can't pick the olives on his own. His knees can't take it."),
  L("Βασιλική", "f", "Να πληρώσουμε συνεργείο; Ο κυρ Αντρέας στο χωριό παίρνει ένα μέρος από το λάδι αντί για χρήματα.", "Shall we pay a crew? Mr Andreas in the village takes a share of the oil instead of money."),
  L("Μανώλης", "m", "Το σκέφτηκα. Αλλά τι λες να κατέβουμε κι εμείς ένα Σαββατοκύριακο με τα παιδιά; Απλώνουμε τα δίχτυα, ραβδίζουμε τα κλαδιά, και το βράδυ ψήνουμε στο τζάκι. Τα παιδιά δεν έχουν δει ποτέ πώς γίνεται το λάδι.", "I thought about it. But what if we went down too for a weekend with the kids? We spread the nets, beat the branches, and in the evening we grill in the fireplace. The kids have never seen how oil is made."),
  L("Βασιλική", "f", "Ένα Σαββατοκύριακο δεν φτάνει για διακόσια δέντρα.", "One weekend isn't enough for two hundred trees."),
  L("Μανώλης", "m", "Όχι, γι' αυτό λέω να κάνουμε και τα δύο: το συνεργείο θα μαζέψει τα περισσότερα, κι εμείς τα δέντρα κοντά στο σπίτι. Και την τελευταία μέρα πάμε όλοι μαζί στο ελαιοτριβείο, να δοκιμάσουν το καινούργιο λάδι πάνω σε ψωμί.", "No, that's why I suggest we do both: the crew will pick most of them, and we'll do the trees near the house. And on the last day we all go together to the olive press, so they can taste the new oil on bread."),
  L("Βασιλική", "f", "Αυτό μου αρέσει. Και ο μπαμπάς θα κάθεται στην καρέκλα και θα μας λέει τι κάνουμε λάθος.", "I like that. And Dad will sit in his chair and tell us what we're doing wrong."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί ο πατέρας να μαζέψει τις ελιές μόνος του;", ["Γιατί λείπει στο εξωτερικό", "Γιατί τα γόνατά του δεν αντέχουν", "Γιατί πούλησε το κτήμα", "Γιατί δεν έχει εργαλεία"], 1, "Τα γόνατά του δεν αντέχουν"),
  Q("Πώς πληρώνεται ο κυρ Αντρέας;", ["Με χρήματα", "Με ένα μέρος από το λάδι", "Με ελιές", "Δεν πληρώνεται"], 1, "παίρνει ένα μέρος από το λάδι αντί για χρήματα"),
  Q("Τι προτείνει τελικά ο Μανώλης;", ["Να μαζέψουν όλες τις ελιές μόνοι τους", "Να πουλήσουν τις ελιές στα δέντρα", "Να μαζέψει τα περισσότερα το συνεργείο κι εκείνοι τα δέντρα κοντά στο σπίτι", "Να μη μαζέψουν φέτος"], 2, "το συνεργείο θα μαζέψει τα περισσότερα, κι εμείς τα δέντρα κοντά στο σπίτι"),
 ],
 "gloss": {"πατρικού": "πατρικός — family, parental", "κτήματος": "κτήμα — estate, farm", "αντέχουν": "αντέχω — to bear, to withstand", "συνεργείο": "συνεργείο — (work) crew; garage", "δίχτυα": "δίχτυ — net", "ραβδίζουμε": "ραβδίζω — to beat (branches) with a stick", "κλαδιά": "κλαδί — branch", "ελαιοτριβείο": "ελαιοτριβείο — olive press, olive mill"},
})

ITEMS.append({
 "id": "l162-mon-nistisima", "title": "Νηστίσιμα όλο τον χρόνο", "title_en": "Lenten dishes all year round", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια μαγείρισσα που έχει ένα μικρό εστιατόριο χωρίς κρέας να μιλάει σε μια εκπομπή.",
 "script": [
  L("Μαγείρισσα", "f", "Όταν άνοιξα το μαγαζί, πολλοί μου είπαν ότι ένα εστιατόριο χωρίς κρέας και χωρίς τυρί δεν θα κρατούσε ούτε έναν χρόνο. Σήμερα κλείνουμε οκτώ. Το μυστικό μου δεν είναι κάποια μόδα από το εξωτερικό· είναι η κουζίνα των γιαγιάδων μας στις περιόδους της νηστείας.", "When I opened the place, many people told me that a restaurant without meat and without cheese wouldn't last even a year. Today we're completing eight. My secret isn't some fashion from abroad; it's our grandmothers' cooking during the fasting periods."),
  L("Μαγείρισσα", "f", "Φασολάδα, φακές, ρεβίθια στον φούρνο, γεμιστά, φάβα, χορτόπιτες με φύλλο χωρίς βούτυρο. Η ελληνική κουζίνα έχει εκατοντάδες πιάτα που ήταν βίγκαν πριν καν υπάρξει η λέξη. Οι πελάτες μου συχνά δεν καταλαβαίνουν καν ότι λείπει το κρέας.", "Bean soup, lentils, oven-baked chickpeas, stuffed vegetables, fava, greens pies with pastry made without butter. Greek cuisine has hundreds of dishes that were vegan before the word even existed. My customers often don't even notice that the meat is missing."),
  L("Μαγείρισσα", "f", "Το μόνο που προσέχω είναι η ποικιλία, για να παίρνει ο οργανισμός ό,τι χρειάζεται. Συνδυάζω όσπρια με δημητριακά, χρησιμοποιώ πολλούς ξηρούς καρπούς και, φυσικά, άφθονο ελαιόλαδο. Δεν λέω σε κανέναν να κόψει το κρέας· λέω μόνο να θυμηθούμε τι ξέραμε ήδη.", "The only thing I pay attention to is variety, so that the body gets what it needs. I combine pulses with grains, I use lots of nuts and, of course, plenty of olive oil. I don't tell anyone to give up meat; I just say we should remember what we already knew."),
 ],
 "questions": [
  Q("Τι της έλεγαν πολλοί όταν άνοιξε το εστιατόριο;", ["Ότι θα έχει μεγάλη επιτυχία", "Ότι δεν θα κρατούσε ούτε έναν χρόνο", "Ότι πρέπει να ανοίξει στο εξωτερικό", "Ότι πρέπει να σερβίρει και ψάρι"], 1, "δεν θα κρατούσε ούτε έναν χρόνο"),
  Q("Από πού εμπνέεται τη μαγειρική της;", ["Από τη μόδα του εξωτερικού", "Από την κουζίνα των γιαγιάδων στις περιόδους της νηστείας", "Από την ιταλική κουζίνα", "Από βιβλία μαγειρικής"], 1, "είναι η κουζίνα των γιαγιάδων μας στις περιόδους της νηστείας"),
  Q("Τι προσέχει περισσότερο;", ["Να είναι φθηνά τα πιάτα", "Να μαγειρεύει γρήγορα", "Την ποικιλία, για να παίρνει ο οργανισμός ό,τι χρειάζεται", "Να μη χρησιμοποιεί λάδι"], 2, "Το μόνο που προσέχω είναι η ποικιλία"),
 ],
 "gloss": {"μαγείρισσα": "μαγείρισσα — (female) cook", "νηστείας": "νηστεία — fasting", "Φασολάδα": "φασολάδα — bean soup", "ρεβίθια": "ρεβίθι — chickpea", "γεμιστά": "γεμιστά — stuffed vegetables", "φάβα": "φάβα — fava (split-pea purée)", "χορτόπιτες": "χορτόπιτα — greens pie", "ποικιλία": "ποικιλία — variety", "όσπρια": "όσπρια — pulses, legumes", "δημητριακά": "δημητριακά — cereals, grains", "ξηρούς καρπούς": "ξηροί καρποί — nuts"},
})

ITEMS.append({
 "id": "l162-vm-diagnostiko", "title": "Μήνυμα από το διαγνωστικό κέντρο", "title_en": "A message from the diagnostic centre", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη γραμματεία ενός διαγνωστικού κέντρου.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα σας, κυρία Θεοδωροπούλου, σας καλώ από το διαγνωστικό κέντρο για τις αιματολογικές εξετάσεις που κάνατε τη Δευτέρα. Τα αποτελέσματα είναι έτοιμα, εκτός από μία εξέταση για τη βιταμίνη, που θα βγει σε δύο μέρες.", "Good morning, Mrs Theodoropoulou, I'm calling from the diagnostic centre about the blood tests you had on Monday. The results are ready, except for one test for the vitamin, which will be out in two days."),
  L("Γραμματέας", "f", "Μπορείτε να τα δείτε στην ιστοσελίδα μας με τον κωδικό που σας δώσαμε, ή να έρθετε να τα παραλάβετε από τη ρεσεψιόν. Αν τα θέλετε σε χαρτί, φέρτε μαζί σας την ταυτότητά σας, γιατί χωρίς αυτήν δεν μπορούμε να δώσουμε ιατρικά έγγραφα.", "You can see them on our website with the code we gave you, or come and collect them from reception. If you want them on paper, bring your ID card with you, because without it we cannot hand over medical documents."),
  L("Γραμματέας", "f", "Ο γιατρός σας ζήτησε να σας πούμε ότι δεν υπάρχει τίποτα ανησυχητικό, αλλά θέλει να επαναλάβετε μία εξέταση σε τρεις μήνες, νηστική. Αν θέλετε, κλείνουμε από τώρα το ραντεβού. Το τηλέφωνό μας είναι το ίδιο, και είμαστε ανοιχτά ως τις οκτώ το βράδυ.", "Your doctor asked us to tell you that there is nothing worrying, but he wants you to repeat one test in three months, on an empty stomach. If you like, we can book the appointment now. Our phone number is the same, and we're open until eight in the evening."),
 ],
 "questions": [
  Q("Ποια εξέταση δεν είναι ακόμη έτοιμη;", ["Η εξέταση για τη χοληστερίνη", "Η εξέταση για τη βιταμίνη", "Η εξέταση για τον σίδηρο", "Όλες είναι έτοιμες"], 1, "εκτός από μία εξέταση για τη βιταμίνη"),
  Q("Τι πρέπει να φέρει η κυρία Θεοδωροπούλου αν θέλει τα αποτελέσματα σε χαρτί;", ["Το παραπεμπτικό", "Την ταυτότητά της", "Τον κωδικό", "Την κάρτα υγείας"], 1, "φέρτε μαζί σας την ταυτότητά σας"),
  Q("Τι ζήτησε ο γιατρός;", ["Να πάει αμέσως στο νοσοκομείο", "Να αλλάξει φάρμακα", "Να επαναλάβει μία εξέταση σε τρεις μήνες, νηστική", "Να του τηλεφωνήσει απόψε"], 2, "θέλει να επαναλάβετε μία εξέταση σε τρεις μήνες, νηστική"),
 ],
 "gloss": {"διαγνωστικού κέντρου": "διαγνωστικό κέντρο — diagnostic centre", "διαγνωστικό": "διαγνωστικός — diagnostic", "γραμματεία": "γραμματεία — front office, secretariat", "αιματολογικές": "αιματολογικός — blood (test)", "εξετάσεις": "εξέταση — (medical) test", "βιταμίνη": "βιταμίνη — vitamin", "παραλάβετε": "παραλαμβάνω — to collect, to receive", "ταυτότητά": "ταυτότητα — ID card", "ανησυχητικό": "ανησυχητικός — worrying", "επαναλάβετε": "επαναλαμβάνω — to repeat", "νηστική": "νηστικός — on an empty stomach"},
})

ITEMS.append({
 "id": "l162-vm-geitonas", "title": "Μήνυμα από τον γείτονα στο χωριό", "title_en": "A message from the neighbour in the village", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον γείτονα του σπιτιού σας στο χωριό, μετά από μια καταιγίδα.",
 "script": [
  L("Γείτονας", "m", "Γεια σου, Κατερίνα, ο Μιχάλης είμαι, ο γείτονας. Σε παίρνω για να σου πω ότι χθες το βράδυ είχαμε μεγάλη καταιγίδα εδώ στο χωριό, με χαλάζι και πολύ αέρα. Μην ανησυχείς, το σπίτι σου είναι καλά.", "Hi, Katerina, it's Michalis, your neighbour. I'm calling to tell you that last night we had a big storm here in the village, with hail and strong wind. Don't worry, your house is fine."),
  L("Γείτονας", "m", "Ο αέρας όμως έριξε ένα μεγάλο κλαδί από την καρυδιά πάνω στον φράχτη, και έσπασαν δυο τρία κεραμίδια από την αποθήκη. Το κλαδί το έκοψα σήμερα το πρωί με τον γιο μου, και τα ξύλα τα έβαλα στην αυλή σου, να τα έχεις για το τζάκι.", "The wind, though, brought down a big branch from the walnut tree onto the fence, and two or three tiles broke on the storeroom. I cut up the branch this morning with my son, and I put the wood in your yard, so you have it for the fireplace."),
  L("Γείτονας", "m", "Για τα κεραμίδια, ξέρω έναν μάστορα που μπορεί να έρθει την άλλη εβδομάδα, αλλά πρέπει να μου πεις εσύ αν θέλεις. Μέχρι τότε σκέπασα την τρύπα με ένα νάιλον, για να μην μπει νερό. Πάρε με όποτε μπορείς, και πες στη μητέρα σου πολλά χαιρετίσματα.", "As for the tiles, I know a builder who can come next week, but you have to tell me if you want him. Until then I covered the hole with a plastic sheet so that no water gets in. Call me whenever you can, and give your mother my best regards."),
 ],
 "questions": [
  Q("Τι έγινε χθες το βράδυ στο χωριό;", ["Σεισμός", "Μεγάλη καταιγίδα με χαλάζι και αέρα", "Πλημμύρα", "Διακοπή ρεύματος"], 1, "είχαμε μεγάλη καταιγίδα εδώ στο χωριό, με χαλάζι και πολύ αέρα"),
  Q("Τι έκανε ο Μιχάλης με το κλαδί;", ["Το πέταξε", "Το έκοψε και έβαλε τα ξύλα στην αυλή της Κατερίνας", "Το άφησε πάνω στον φράχτη", "Το πήρε για το δικό του τζάκι"], 1, "τα ξύλα τα έβαλα στην αυλή σου"),
  Q("Τι έκανε προσωρινά για την τρύπα στη στέγη της αποθήκης;", ["Τίποτα", "Έβαλε καινούργια κεραμίδια", "Τη σκέπασε με ένα νάιλον", "Κάλεσε τον μάστορα"], 2, "σκέπασα την τρύπα με ένα νάιλον"),
 ],
 "gloss": {"καταιγίδα": "καταιγίδα — storm", "χαλάζι": "χαλάζι — hail", "κλαδί": "κλαδί — branch", "καρυδιά": "καρυδιά — walnut tree", "φράχτη": "φράχτης — fence", "κεραμίδια": "κεραμίδι — roof tile", "αποθήκη": "αποθήκη — storeroom, shed", "μάστορα": "μάστορας — builder, craftsman", "σκέπασα": "σκεπάζω — to cover", "νάιλον": "νάιλον — plastic sheet", "χαιρετίσματα": "χαιρετίσματα — regards, greetings"},
})

ITEMS.append({
 "id": "l162-c1-kessler", "title": "Σκουπίδια σε τροχιά", "title_en": "Rubbish in orbit", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια αστροφυσικό για τα διαστημικά σκουπίδια και το λεγόμενο σύνδρομο Κέσλερ.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσα αντικείμενα βρίσκονται σήμερα σε τροχιά γύρω από τη Γη;", "How many objects are in orbit around the Earth today?"),
  L("Αστροφυσικός", "f", "Οι υπηρεσίες που τα παρακολουθούν καταγράφουν δεκάδες χιλιάδες κομμάτια μεγαλύτερα από μια μπάλα του τένις, και τα μικρότερα υπολογίζονται σε εκατομμύρια: παλιοί δορυφόροι, κομμάτια από πυραύλους, ακόμη και ένα γάντι που ξέφυγε από αστροναύτη. Το πρόβλημα είναι η ταχύτητα. Σε χαμηλή τροχιά κινούνται με περίπου οκτώ χιλιόμετρα το δευτερόλεπτο, οπότε ακόμη και ένα μικρό θραύσμα χτυπά σαν βλήμα.", "The agencies that track them record tens of thousands of pieces larger than a tennis ball, and the smaller ones are estimated in the millions: old satellites, pieces of rockets, even a glove that got away from an astronaut. The problem is speed. In low orbit they move at about eight kilometres per second, so even a small fragment hits like a projectile."),
  L("Δημοσιογράφος", "m", "Τι είναι το σύνδρομο Κέσλερ;", "What is Kessler syndrome?"),
  L("Αστροφυσικός", "f", "Το 1978 ο Ντόναλντ Κέσλερ, επιστήμονας της NASA, περιέγραψε ένα σενάριο αλυσιδωτής αντίδρασης: μια σύγκρουση δημιουργεί χιλιάδες θραύσματα, αυτά προκαλούν νέες συγκρούσεις, και κάποια στιγμή ορισμένες τροχιές γίνονται τόσο επικίνδυνες που δεν μπορούμε πια να τις χρησιμοποιήσουμε. Το 2009 ένας ενεργός αμερικανικός δορυφόρος συγκρούστηκε τυχαία με έναν παλιό ρωσικό, και τα δύο διαλύθηκαν σε χιλιάδες κομμάτια. Ήταν η πρώτη τέτοια σύγκρουση ανάμεσα σε ολόκληρους δορυφόρους.", "In 1978 Donald Kessler, a NASA scientist, described a chain-reaction scenario: one collision creates thousands of fragments, these cause new collisions, and at some point certain orbits become so dangerous that we can no longer use them. In 2009 an active American satellite collided by accident with an old Russian one, and both broke up into thousands of pieces. It was the first such collision between whole satellites."),
  L("Δημοσιογράφος", "m", "Μπορούμε να καθαρίσουμε το διάστημα;", "Can we clean up space?"),
  L("Αστροφυσικός", "f", "Δοκιμάζονται διάφορες ιδέες, από δίχτυα και μαγνήτες μέχρι μικρά διαστημόπλοια που θα «αρπάζουν» τα παλιά αντικείμενα και θα τα οδηγούν να καούν στην ατμόσφαιρα. Όλες όμως είναι ακριβές και αργές. Το πιο αποτελεσματικό είναι η πρόληψη: κάθε νέος δορυφόρος πρέπει να έχει σχέδιο για το τέλος της ζωής του. Η κατάσταση μοιάζει λίγο με τη ρύπανση των θαλασσών· είναι πολύ ευκολότερο να μην πετάξεις κάτι παρά να το ψαρέψεις μετά.", "Various ideas are being tested, from nets and magnets to small spacecraft that will 'grab' old objects and steer them to burn up in the atmosphere. But all of them are expensive and slow. The most effective thing is prevention: every new satellite must have a plan for the end of its life. The situation is a bit like pollution of the seas; it is much easier not to throw something away than to fish it out afterwards."),
 ],
 "questions": [
  Q("Γιατί είναι επικίνδυνο ακόμη και ένα μικρό θραύσμα;", ["Γιατί είναι ραδιενεργό", "Γιατί κινείται με τεράστια ταχύτητα και χτυπά σαν βλήμα", "Γιατί δεν φαίνεται στα ραντάρ", "Γιατί πέφτει στη Γη"], 1, "ακόμη και ένα μικρό θραύσμα χτυπά σαν βλήμα"),
  Q("Τι περιέγραψε ο Κέσλερ το 1978;", ["Μια μέθοδο καθαρισμού του διαστήματος", "Ένα σενάριο αλυσιδωτής αντίδρασης συγκρούσεων", "Έναν νέο τύπο δορυφόρου", "Τον πρώτο διαστημικό σταθμό"], 1, "περιέγραψε ένα σενάριο αλυσιδωτής αντίδρασης"),
  Q("Τι συνέβη το 2009;", ["Καταστράφηκε ένας διαστημικός σταθμός", "Ένας αστροναύτης τραυματίστηκε", "Ένας ενεργός αμερικανικός δορυφόρος συγκρούστηκε τυχαία με έναν παλιό ρωσικό", "Εκτοξεύτηκε το πρώτο διαστημόπλοιο καθαρισμού"], 2, "ένας ενεργός αμερικανικός δορυφόρος συγκρούστηκε τυχαία με έναν παλιό ρωσικό"),
  Q("Ποια λύση θεωρεί η αστροφυσικός πιο αποτελεσματική;", ["Τα δίχτυα", "Τους μαγνήτες", "Να σταματήσουν οι εκτοξεύσεις", "Την πρόληψη, με σχέδιο για το τέλος κάθε δορυφόρου"], 3, "Το πιο αποτελεσματικό είναι η πρόληψη"),
 ],
 "gloss": {"τροχιά": "τροχιά — orbit", "αστροφυσικό": "αστροφυσικός — astrophysicist", "διαστημικά": "διαστημικός — space (adj.)", "σύνδρομο": "σύνδρομο — syndrome", "δορυφόροι": "δορυφόρος — satellite", "πυραύλους": "πύραυλος — rocket", "θραύσμα": "θραύσμα — fragment", "βλήμα": "βλήμα — projectile", "αλυσιδωτής αντίδρασης": "αλυσιδωτή αντίδραση — chain reaction", "σύγκρουση": "σύγκρουση — collision", "ενεργός": "ενεργός — active", "διαστημόπλοια": "διαστημόπλοιο — spacecraft", "πρόληψη": "πρόληψη — prevention", "ρύπανση": "ρύπανση — pollution"},
})

ITEMS.append({
 "id": "l162-c1-carrington", "title": "Η μέρα που ο Ήλιος έκαψε τον τηλέγραφο", "title_en": "The day the Sun burned the telegraph", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκλαϊκευτική διάλεξη για τη μεγάλη ηλιακή καταιγίδα του 1859.",
 "script": [
  L("Ομιλητής", "m", "Το πρωί της 1ης Σεπτεμβρίου 1859, ο Βρετανός αστρονόμος Ρίτσαρντ Κάρινγκτον σχεδίαζε τις ηλιακές κηλίδες στο ιδιωτικό του αστεροσκοπείο, όταν είδε δύο εκτυφλωτικά σημεία φωτός να εμφανίζονται πάνω στον Ήλιο και να σβήνουν μέσα σε λίγα λεπτά. Ήταν η πρώτη καταγεγραμμένη παρατήρηση μιας ηλιακής έκλαμψης.", "On the morning of 1 September 1859, the British astronomer Richard Carrington was drawing sunspots in his private observatory when he saw two blinding points of light appear on the Sun and fade within a few minutes. It was the first recorded observation of a solar flare."),
  L("Ομιλητής", "m", "Περίπου δεκαοκτώ ώρες αργότερα, ένα τεράστιο νέφος φορτισμένων σωματιδίων έφτασε στη Γη. Το σέλας, που συνήθως φαίνεται κοντά στους πόλους, φάνηκε μέχρι την Καραϊβική, και σε ορισμένες περιοχές ήταν τόσο φωτεινό που κάποιοι ξύπνησαν νομίζοντας ότι ξημέρωσε. Τα τηλεγραφικά δίκτυα τρελάθηκαν: από τα καλώδια πετάγονταν σπίθες, χειριστές δέχτηκαν ηλεκτρικά χτυπήματα, και κάποιες γραμμές συνέχισαν να στέλνουν μηνύματα ακόμη κι όταν αποσυνδέθηκαν οι μπαταρίες.", "About eighteen hours later, a huge cloud of charged particles reached the Earth. The aurora, which is usually seen near the poles, was visible as far as the Caribbean, and in some areas it was so bright that some people woke up thinking it was dawn. The telegraph networks went haywire: sparks flew from the wires, operators received electric shocks, and some lines kept sending messages even when the batteries were disconnected."),
  L("Ομιλητής", "m", "Το 1859 ο κόσμος είχε μόνο τηλέγραφο. Σήμερα ένα αντίστοιχο γεγονός θα μπορούσε να καταστρέψει μετασχηματιστές του ηλεκτρικού δικτύου, να βγάλει εκτός λειτουργίας δορυφόρους και να διαταράξει το σύστημα εντοπισμού θέσης, από το οποίο εξαρτώνται από τα αεροπλάνα μέχρι οι τράπεζες. Τον Ιούλιο του 2012 μια εξίσου ισχυρή έκρηξη στον Ήλιο πέρασε από το σημείο της τροχιάς μας όπου η Γη είχε βρεθεί μόλις εννιά μέρες νωρίτερα. Το ερώτημα δεν είναι αν θα ξανασυμβεί, αλλά πότε· και γι' αυτό σήμερα οι δορυφόροι παρακολουθούν τον Ήλιο συνεχώς, για να μας δώσουν λίγες ώρες προειδοποίηση.", "In 1859 the world had only the telegraph. Today an equivalent event could destroy transformers in the electricity grid, knock out satellites and disrupt the positioning system on which everything from aeroplanes to banks depends. In July 2012 an equally powerful eruption on the Sun crossed the point in our orbit where the Earth had been just nine days earlier. The question is not whether it will happen again, but when; and that is why satellites now watch the Sun constantly, to give us a few hours' warning."),
 ],
 "questions": [
  Q("Τι παρατήρησε ο Κάρινγκτον το πρωί της 1ης Σεπτεμβρίου 1859;", ["Μια έκλειψη Ηλίου", "Δύο εκτυφλωτικά σημεία φωτός πάνω στον Ήλιο", "Έναν κομήτη", "Το σέλας"], 1, "είδε δύο εκτυφλωτικά σημεία φωτός να εμφανίζονται πάνω στον Ήλιο"),
  Q("Πού φάνηκε το σέλας εκείνες τις μέρες;", ["Μόνο κοντά στους πόλους", "Μέχρι την Καραϊβική", "Μόνο στη Βρετανία", "Πουθενά"], 1, "φάνηκε μέχρι την Καραϊβική"),
  Q("Τι συνέβη στα τηλεγραφικά δίκτυα;", ["Λειτουργούσαν πιο γρήγορα", "Σταμάτησαν για εβδομάδες", "Πετάγονταν σπίθες και κάποιες γραμμές λειτουργούσαν χωρίς μπαταρίες", "Δεν επηρεάστηκαν"], 2, "κάποιες γραμμές συνέχισαν να στέλνουν μηνύματα ακόμη κι όταν αποσυνδέθηκαν οι μπαταρίες"),
  Q("Τι λέει ο ομιλητής για την έκρηξη του Ιουλίου 2012;", ["Ότι χτύπησε τη Γη", "Ότι ήταν πολύ ασθενέστερη", "Ότι προκάλεσε σέλας στην Ελλάδα", "Ότι πέρασε από σημείο της τροχιάς όπου η Γη είχε βρεθεί μόλις εννιά μέρες νωρίτερα"], 3, "πέρασε από το σημείο της τροχιάς μας όπου η Γη είχε βρεθεί μόλις εννιά μέρες νωρίτερα"),
 ],
 "gloss": {"ηλιακή": "ηλιακός — solar", "καταιγίδα": "καταιγίδα — storm", "κηλίδες": "κηλίδα — spot", "αστεροσκοπείο": "αστεροσκοπείο — observatory", "εκτυφλωτικά": "εκτυφλωτικός — blinding", "έκλαμψης": "έκλαμψη — flare", "νέφος": "νέφος — cloud", "φορτισμένων σωματιδίων": "φορτισμένο σωματίδιο — charged particle", "σέλας": "σέλας — aurora", "τηλεγραφικά": "τηλεγραφικός — telegraph (adj.)", "σπίθες": "σπίθα — spark", "χειριστές": "χειριστής — operator", "αποσυνδέθηκαν": "αποσυνδέομαι — to be disconnected", "μετασχηματιστές": "μετασχηματιστής — transformer", "διαταράξει": "διαταράσσω — to disrupt", "εντοπισμού θέσης": "σύστημα εντοπισμού θέσης — positioning system (GPS)", "προειδοποίηση": "προειδοποίηση — warning"},
})

rnd = random.Random(162)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-162.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
