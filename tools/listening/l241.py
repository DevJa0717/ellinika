# Source for library/listening/listening-241.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l241.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l241-news-palia-grammi-diadromi", "title": "Η παλιά σιδηροδρομική γραμμή γίνεται διαδρομή για πεζούς και ποδήλατα", "title_en": "The old railway line becomes a route for walkers and cyclists", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός περιφερειακού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνήτρια", "f", "Η παλιά μετρική σιδηροδρομική γραμμή ανάμεσα σε δύο κωμοπόλεις του νομού, όπου δεν περνάει τρένο εδώ και περισσότερα από δεκαπέντε χρόνια, θα μετατραπεί σε διαδρομή για πεζούς και ποδηλάτες. Η σύμβαση για το έργο υπογράφηκε χθες στο δημαρχείο.", "The old narrow-gauge railway line between two small towns in the prefecture, where no train has run for more than fifteen years, will be turned into a route for walkers and cyclists. The contract for the project was signed yesterday at the town hall."),
  L("Εκφωνήτρια", "f", "Η διαδρομή θα έχει μήκος είκοσι δύο χιλιόμετρα. Οι ράγες και οι τραβέρσες θα αφαιρεθούν, αλλά οι πέτρινες γέφυρες και η μικρή σήραγγα θα διατηρηθούν και θα φωτιστούν. Οι δύο παλιοί σταθμοί θα γίνουν σημεία ξεκούρασης, με νερό, τουαλέτες και ενοικίαση ποδηλάτων.", "The route will be twenty-two kilometres long. The rails and the sleepers will be removed, but the stone bridges and the small tunnel will be preserved and lit. The two old stations will become rest stops, with water, toilets and bicycle hire."),
  L("Εκφωνήτρια", "f", "Η δήμαρχος δήλωσε ότι η κλίση της γραμμής δεν ξεπερνά πουθενά το τρία τοις εκατό, οπότε η διαδρομή θα είναι κατάλληλη και για οικογένειες με μικρά παιδιά και για ανθρώπους με αναπηρικό αμαξίδιο. Σύλλογοι φίλων του σιδηροδρόμου, πάντως, εξέφρασαν την αντίθεσή τους, γιατί ελπίζουν ότι κάποτε το τρένο θα ξαναπεράσει.", "The mayor stated that the gradient of the line nowhere exceeds three per cent, so the route will also be suitable for families with small children and for wheelchair users. Railway enthusiasts' associations, however, expressed their opposition, because they hope the train will one day run again."),
  L("Εκφωνήτρια", "f", "Οι εργασίες αναμένεται να ξεκινήσουν την άνοιξη και να διαρκέσουν περίπου δεκαοκτώ μήνες.", "Work is expected to begin in the spring and to last about eighteen months."),
 ],
 "questions": [
  Q("Πόσο καιρό δεν περνάει τρένο από τη γραμμή;", ["Δύο χρόνια", "Περισσότερα από δεκαπέντε χρόνια", "Δεκαοκτώ μήνες", "Πάνω από πενήντα χρόνια"], 1, "δεν περνάει τρένο εδώ και περισσότερα από δεκαπέντε χρόνια"),
  Q("Τι θα γίνει με τις πέτρινες γέφυρες;", ["Θα κατεδαφιστούν", "Θα διατηρηθούν και θα φωτιστούν", "Θα αντικατασταθούν από μεταλλικές", "Θα κλείσουν για το κοινό"], 1, "οι πέτρινες γέφυρες και η μικρή σήραγγα θα διατηρηθούν και θα φωτιστούν"),
  Q("Γιατί η διαδρομή θα είναι κατάλληλη και για αναπηρικά αμαξίδια;", ["Γιατί θα στρωθεί με άσφαλτο", "Γιατί η κλίση δεν ξεπερνά πουθενά το τρία τοις εκατό", "Γιατί είναι πολύ σύντομη", "Γιατί θα υπάρχει ειδικό λεωφορείο"], 1, "η κλίση της γραμμής δεν ξεπερνά πουθενά το τρία τοις εκατό"),
  Q("Γιατί αντιδρούν οι σύλλογοι φίλων του σιδηροδρόμου;", ["Γιατί το έργο κοστίζει πολύ", "Γιατί ελπίζουν ότι κάποτε θα ξαναπεράσει τρένο", "Γιατί θα κλείσουν οι σταθμοί", "Γιατί δεν τους ρώτησε κανείς"], 1, "ελπίζουν ότι κάποτε το τρένο θα ξαναπεράσει"),
 ],
 "gloss": {"μετρική": "μετρική (γραμμή) — narrow-gauge (metre-gauge) railway", "κωμοπόλεις": "κωμόπολη — small town", "σύμβαση": "σύμβαση — contract", "ράγες": "ράγα — rail", "τραβέρσες": "τραβέρσα — (railway) sleeper, tie", "σήραγγα": "σήραγγα — tunnel", "κλίση": "κλίση — gradient, slope", "αναπηρικό αμαξίδιο": "αναπηρικό αμαξίδιο — wheelchair", "αντίθεσή": "αντίθεση — opposition"},
})

ITEMS.append({
 "id": "l241-vm-melissokomos-sminos", "title": "Μήνυμα από τον μελισσοκόμο: «Ένα σμήνος κάθισε στο μπαλκόνι σας»", "title_en": "A message from the beekeeper: 'A swarm has settled on your balcony'", "type": "voicemail", "level": "B2",
 "context_el": "Λείπετε από το σπίτι σας για μια μέρα. Ακούτε ένα μήνυμα που σας άφησε ένας γείτονας μελισσοκόμος στον τηλεφωνητή.",
 "script": [
  L("Μελισσοκόμος", "m", "Καλημέρα, ο Θανάσης είμαι, από το διπλανό σπίτι, αυτός με τα μελίσσια. Μη φοβηθείς με αυτό που θα σου πω. Πριν από μισή ώρα ένα σμήνος μέλισσες έφυγε από μια κυψέλη μου και κάθισε στο μπαλκόνι σου, πάνω στη γλάστρα με τη λεμονιά.", "Good morning, it's Thanasis, from next door, the one with the beehives. Don't be alarmed by what I'm about to tell you. Half an hour ago a swarm of bees left one of my hives and settled on your balcony, on the pot with the lemon tree."),
  L("Μελισσοκόμος", "m", "Δεν είναι επικίνδυνες. Όταν οι μέλισσες σμηνουργούν, έχουν φάει πολύ μέλι πριν φύγουν και σπάνια τσιμπάνε. Απλώς ψάχνουν καινούργιο σπίτι, και στο μεταξύ ξεκουράζονται κάπου, σαν μια μεγάλη μπάλα γύρω από τη βασίλισσα.", "They're not dangerous. When bees swarm, they've eaten a lot of honey before leaving and they rarely sting. They're just looking for a new home, and meanwhile they rest somewhere, like a big ball around the queen."),
  L("Μελισσοκόμος", "m", "Θα ήθελα να τις μαζέψω απόψε, όταν θα έχουν μαζευτεί όλες και θα έχει δροσίσει. Θα χρειαστώ να ανέβω στο μπαλκόνι σου γύρω στις εννιά, με ένα άδειο κουτί και τη στολή μου. Σε παρακαλώ, μέχρι τότε κράτα κλειστή την μπαλκονόπορτα και μην τις ψεκάσεις με τίποτα.", "I'd like to collect them tonight, when they've all gathered and it's cooled down. I'll need to come up onto your balcony at around nine, with an empty box and my suit. Please, until then, keep the balcony door shut and don't spray them with anything."),
  L("Μελισσοκόμος", "m", "Αν δεν είσαι σπίτι απόψε, άφησέ μου το κλειδί στην κυρία Ρένα στο ισόγειο. Και για την ταλαιπωρία, το πρώτο βάζο μέλι από αυτό το σμήνος είναι δικό σου. Πάρε με όταν ακούσεις το μήνυμα.", "If you're not home tonight, leave the key for me with Mrs Rena on the ground floor. And for the trouble, the first jar of honey from this swarm is yours. Call me when you hear the message."),
 ],
 "questions": [
  Q("Πού κάθισε το σμήνος;", ["Στη στέγη της πολυκατοικίας", "Σε μια γλάστρα με λεμονιά στο μπαλκόνι", "Μέσα στο σαλόνι", "Σε ένα δέντρο στον δρόμο"], 1, "κάθισε στο μπαλκόνι σου, πάνω στη γλάστρα με τη λεμονιά"),
  Q("Γιατί, κατά τον μελισσοκόμο, οι μέλισσες σπάνια τσιμπάνε όταν σμηνουργούν;", ["Γιατί είναι κουρασμένες", "Γιατί έχουν φάει πολύ μέλι πριν φύγουν", "Γιατί δεν έχουν βασίλισσα", "Γιατί κάνει κρύο"], 1, "έχουν φάει πολύ μέλι πριν φύγουν και σπάνια τσιμπάνε"),
  Q("Τι ζητά από τον/την ακροατή/τρια μέχρι το βράδυ;", ["Να ανάψει το φως στο μπαλκόνι", "Να κρατά κλειστή την μπαλκονόπορτα και να μην τις ψεκάσει", "Να ποτίσει τη λεμονιά", "Να καλέσει την πυροσβεστική"], 1, "κράτα κλειστή την μπαλκονόπορτα και μην τις ψεκάσεις με τίποτα"),
  Q("Τι προσφέρει για την ταλαιπωρία;", ["Μια καινούργια γλάστρα", "Το πρώτο βάζο μέλι από το σμήνος", "Ένα δείπνο", "Μια κυψέλη"], 1, "το πρώτο βάζο μέλι από αυτό το σμήνος είναι δικό σου"),
 ],
 "gloss": {"μελίσσια": "μελίσσι — beehive, colony", "σμήνος": "σμήνος — swarm", "κυψέλη": "κυψέλη — hive", "γλάστρα": "γλάστρα — flowerpot", "σμηνουργούν": "σμηνουργώ — to swarm", "τσιμπάνε": "τσιμπώ — to sting", "βασίλισσα": "βασίλισσα — queen (bee)", "δροσίσει": "δροσίζει — it cools down", "μπαλκονόπορτα": "μπαλκονόπορτα — balcony door", "ψεκάσεις": "ψεκάζω — to spray", "ταλαιπωρία": "ταλαιπωρία — trouble, inconvenience"},
})

ITEMS.append({
 "id": "l241-c1-mono-odontovourtsa", "title": "Από το κλαδάκι στη βούρτσα: η ιστορία της οδοντόβουρτσας", "title_en": "From the twig to the brush: the history of the toothbrush", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ιστορικό της ιατρικής σε μια ραδιοφωνική εκπομπή για τα αντικείμενα της καθημερινής ζωής.",
 "script": [
  L("Ιστορικός", "m", "Πολύ πριν από την οδοντόβουρτσα, οι άνθρωποι καθάριζαν τα δόντια τους με κλαδάκια. Μασούσαν την άκρη ενός λεπτού κλαδιού μέχρι να ξεφτίσει και να γίνει σαν πινέλο, και μ' αυτό έτριβαν τα δόντια. Σε ορισμένες περιοχές της Αφρικής και της Μέσης Ανατολής η συνήθεια αυτή επιβιώνει μέχρι σήμερα.", "Long before the toothbrush, people cleaned their teeth with twigs. They chewed the end of a thin twig until it frayed and became like a paintbrush, and they rubbed their teeth with it. In some regions of Africa and the Middle East this habit survives to this day."),
  L("Ιστορικός", "m", "Η βούρτσα με τρίχες, όπως την ξέρουμε, φαίνεται ότι εμφανίστηκε στην Κίνα. Οι πηγές συνήθως αναφέρουν το τέλος του δέκατου πέμπτου αιώνα: χοντρές τρίχες από τον λαιμό του γουρουνιού, στερεωμένες σε λαβή από κόκαλο ή μπαμπού. Στην Ευρώπη έφτασε αργότερα, και για πολύ καιρό ήταν πολυτέλεια.", "The bristle brush as we know it seems to have appeared in China. Sources usually cite the end of the fifteenth century: coarse bristles from the neck of the pig, fixed in a handle of bone or bamboo. It reached Europe later, and for a long time it was a luxury."),
  L("Ιστορικός", "m", "Η μαζική παραγωγή ξεκίνησε στην Αγγλία, στα τέλη του δέκατου όγδοου αιώνα, με έναν άνθρωπο που λεγόταν Γουίλιαμ Άντις. Σύμφωνα με μια ιστορία που επαναλαμβάνεται συχνά, αλλά δύσκολα επιβεβαιώνεται, του ήρθε η ιδέα στη φυλακή: κράτησε ένα κόκαλο από το φαγητό του, άνοιξε τρύπες και πέρασε μέσα τρίχες που ζήτησε από τον φύλακα.", "Mass production began in England at the end of the eighteenth century, with a man called William Addis. According to a story that is often repeated but hard to confirm, the idea came to him in prison: he kept a bone from his food, made holes in it and threaded through bristles he asked the guard for."),
  L("Ιστορικός", "m", "Η μεγάλη αλλαγή ήρθε το 1938, με τις πρώτες νάιλον τρίχες, που στέγνωναν γρήγορα και δεν μαλάκωναν όπως οι φυσικές. Κι όμως, η καθημερινή χρήση της οδοντόβουρτσας έγινε κανόνας σε πολλές χώρες μόλις μετά τον Δεύτερο Παγκόσμιο Πόλεμο. Με άλλα λόγια, ένα αντικείμενο που μας φαίνεται αυτονόητο είναι, ως συνήθεια, πολύ πιο καινούργιο απ' όσο νομίζουμε.", "The big change came in 1938, with the first nylon bristles, which dried quickly and didn't go soft like natural ones. And yet, daily use of the toothbrush became the norm in many countries only after the Second World War. In other words, an object that seems self-evident to us is, as a habit, much newer than we think."),
 ],
 "questions": [
  Q("Πώς καθάριζαν τα δόντια τους οι άνθρωποι πριν από την οδοντόβουρτσα;", ["Με αλάτι και νερό", "Με κλαδάκια που μασούσαν μέχρι να ξεφτίσουν", "Με κομμάτια ύφασμα", "Δεν τα καθάριζαν καθόλου"], 1, "Μασούσαν την άκρη ενός λεπτού κλαδιού μέχρι να ξεφτίσει"),
  Q("Από τι ήταν οι τρίχες της πρώτης κινεζικής βούρτσας;", ["Από τρίχες αλόγου", "Από τον λαιμό του γουρουνιού", "Από φτερά πουλιών", "Από φυτικές ίνες"], 1, "χοντρές τρίχες από τον λαιμό του γουρουνιού"),
  Q("Τι λέει ο ομιλητής για την ιστορία του Γουίλιαμ Άντις στη φυλακή;", ["Ότι είναι αποδεδειγμένη από έγγραφα", "Ότι επαναλαμβάνεται συχνά αλλά δύσκολα επιβεβαιώνεται", "Ότι την επινόησε ο ίδιος ο Άντις", "Ότι είναι σίγουρα ψεύτικη"], 1, "μια ιστορία που επαναλαμβάνεται συχνά, αλλά δύσκολα επιβεβαιώνεται"),
  Q("Ποιο είναι το συμπέρασμα του ομιλητή;", ["Ότι οι φυσικές τρίχες ήταν καλύτερες", "Ότι η καθημερινή χρήση της οδοντόβουρτσας είναι πιο καινούργια συνήθεια απ' όσο νομίζουμε", "Ότι η οδοντόβουρτσα εφευρέθηκε στην Αγγλία", "Ότι τα κλαδάκια καθαρίζουν καλύτερα"], 1, "ως συνήθεια, πολύ πιο καινούργιο απ' όσο νομίζουμε"),
 ],
 "gloss": {"κλαδάκια": "κλαδάκι — twig", "ξεφτίσει": "ξεφτίζω — to fray", "πινέλο": "πινέλο — paintbrush", "τρίχες": "τρίχα — bristle, hair", "στερεωμένες": "στερεωμένος — fixed, fastened", "λαβή": "λαβή — handle", "πολυτέλεια": "πολυτέλεια — luxury", "μαζική παραγωγή": "μαζική παραγωγή — mass production", "επιβεβαιώνεται": "επιβεβαιώνω — to confirm", "μαλάκωναν": "μαλακώνω — to soften, go soft", "αυτονόητο": "αυτονόητος — self-evident"},
})

ITEMS.append({
 "id": "l241-c1-int-malakologos", "title": "Μια μαλακολόγος για τα σαλιγκάρια της Ελλάδας", "title_en": "A malacologist on the snails of Greece", "type": "interview", "level": "C1",
 "context_el": "Μια μαλακολόγος, δηλαδή μια βιολόγος που μελετά τα μαλάκια, μιλά για τα χερσαία σαλιγκάρια σε μια ραδιοφωνική εκπομπή για τη φύση.",
 "script": [
  L("Δημοσιογράφος", "m", "Τα σαλιγκάρια δεν είναι ακριβώς το πιο δημοφιλές ζώο. Γιατί αξίζει να τα μελετά κανείς;", "Snails aren't exactly the most popular animal. Why is it worth studying them?"),
  L("Μαλακολόγος", "f", "Γιατί η Ελλάδα είναι ένας μικρός θησαυρός γι' αυτά. Έχουμε εκατοντάδες είδη χερσαίων σαλιγκαριών που δεν ζουν πουθενά αλλού στον κόσμο. Κάποια βρίσκονται μόνο σε ένα νησάκι, ή ακόμη και σε μία μόνο πλαγιά. Τα σαλιγκάρια κινούνται τόσο λίγο, ώστε κάθε απομονωμένος πληθυσμός εξελίσσεται, σιγά σιγά, με τον δικό του τρόπο.", "Because Greece is a small treasure trove for them. We have hundreds of species of land snails that live nowhere else in the world. Some are found on only one islet, or even on a single slope. Snails move so little that every isolated population evolves, slowly, in its own way."),
  L("Δημοσιογράφος", "m", "Πώς αντέχουν το ελληνικό καλοκαίρι, με τόση ζέστη και τόσο λίγο νερό;", "How do they survive the Greek summer, with so much heat and so little water?"),
  L("Μαλακολόγος", "f", "Πέφτουν σε θερινή νάρκη. Μαζεύονται μέσα στο κέλυφος και κλείνουν το άνοιγμα με μια λεπτή μεμβράνη από βλέννα που ξεραίνεται, το επίφραγμα. Έτσι χάνουν ελάχιστη υγρασία και μπορούν να περιμένουν εβδομάδες, ή και μήνες, μέχρι την πρώτη βροχή. Γι' αυτό, μετά από μια φθινοπωρινή μπόρα, βλέπετε ξαφνικά σαλιγκάρια παντού.", "They go into summer dormancy. They withdraw into the shell and close the opening with a thin membrane of mucus that dries, the epiphragm. That way they lose very little moisture and can wait for weeks, or even months, until the first rain. That's why, after an autumn shower, you suddenly see snails everywhere."),
  L("Δημοσιογράφος", "m", "Κινδυνεύουν;", "Are they in danger?"),
  L("Μαλακολόγος", "f", "Κάποια είδη, ναι. Χρειάζονται ασβέστιο για το κέλυφός τους, γι' αυτό πολλά ζουν σε ασβεστολιθικούς βράχους. Όταν ανοίγει ένα λατομείο σε μια τέτοια πλαγιά, μπορεί να εξαφανιστεί ένα ολόκληρο είδος, χωρίς να το καταλάβει κανείς. Δεν έχει τη χάρη μιας αρκούδας ή μιας χελώνας για να συγκινήσει τον κόσμο. Γι' αυτό λέω ότι η δική μας δουλειά είναι να μιλάμε για όσους δεν έχουν φωνή, ούτε, ας πούμε, ωραία μάτια.", "Some species, yes. They need calcium for their shell, so many live on limestone rocks. When a quarry opens on such a slope, a whole species can disappear without anyone noticing. It doesn't have the charm of a bear or a turtle to move people. That's why I say our job is to speak for those who have no voice, nor, let's say, pretty eyes."),
 ],
 "questions": [
  Q("Γιατί, κατά τη μαλακολόγο, η Ελλάδα είναι «θησαυρός» για τα σαλιγκάρια;", ["Γιατί έχει πολλή βροχή", "Γιατί έχει εκατοντάδες είδη που δεν ζουν πουθενά αλλού", "Γιατί εκεί ζουν τα μεγαλύτερα σαλιγκάρια", "Γιατί δεν έχει θηρευτές"], 1, "εκατοντάδες είδη χερσαίων σαλιγκαριών που δεν ζουν πουθενά αλλού στον κόσμο"),
  Q("Γιατί κάθε απομονωμένος πληθυσμός εξελίσσεται με τον δικό του τρόπο;", ["Γιατί τρέφεται με διαφορετικά φυτά", "Γιατί τα σαλιγκάρια κινούνται πολύ λίγο", "Γιατί ζει πολλά χρόνια", "Γιατί αλλάζει το κλίμα"], 1, "Τα σαλιγκάρια κινούνται τόσο λίγο, ώστε κάθε απομονωμένος πληθυσμός εξελίσσεται"),
  Q("Τι είναι το επίφραγμα;", ["Ένα είδος σαλιγκαριού", "Μια μεμβράνη από ξεραμένη βλέννα που κλείνει το κέλυφος", "Το πόδι του σαλιγκαριού", "Ένα φυτό που τρώνε τα σαλιγκάρια"], 1, "κλείνουν το άνοιγμα με μια λεπτή μεμβράνη από βλέννα που ξεραίνεται, το επίφραγμα"),
  Q("Γιατί ένα λατομείο μπορεί να εξαφανίσει ένα είδος;", ["Γιατί ο θόρυβος τα τρομάζει", "Γιατί πολλά είδη ζουν μόνο σε συγκεκριμένους ασβεστολιθικούς βράχους", "Γιατί η σκόνη τα δηλητηριάζει", "Γιατί οι εργάτες τα μαζεύουν για φαγητό"], 1, "πολλά ζουν σε ασβεστολιθικούς βράχους. Όταν ανοίγει ένα λατομείο σε μια τέτοια πλαγιά"),
 ],
 "gloss": {"μαλακολόγος": "μαλακολόγος — malacologist (scientist who studies molluscs)", "χερσαίων": "χερσαίος — terrestrial, land", "πλαγιά": "πλαγιά — slope, hillside", "εξελίσσεται": "εξελίσσομαι — to evolve", "θερινή νάρκη": "θερινή νάρκη — summer dormancy, aestivation", "κέλυφος": "κέλυφος — shell", "μεμβράνη": "μεμβράνη — membrane", "βλέννα": "βλέννα — mucus, slime", "επίφραγμα": "επίφραγμα — epiphragm", "μπόρα": "μπόρα — shower, downpour", "ασβέστιο": "ασβέστιο — calcium", "ασβεστολιθικούς": "ασβεστολιθικός — limestone", "λατομείο": "λατομείο — quarry"},
})

rnd = random.Random(241)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-241.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
