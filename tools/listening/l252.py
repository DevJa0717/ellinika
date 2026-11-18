# Source for library/listening/listening-252.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l252.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l252-news-peristeri-se-psarovarko", "title": "Περιστέρι αγώνων προσγειώθηκε σε ψαροκάικο στη μέση του Αιγαίου", "title_en": "A racing pigeon lands on a fishing boat in the middle of the Aegean", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο πρωινό δελτίο ενός περιφερειακού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Έναν απρόσμενο επιβάτη απέκτησε την Τρίτη το πλήρωμα ενός ψαροκάικου από την Κάλυμνο. Ενώ το σκάφος ψάρευε ανάμεσα στην Αμοργό και τη Νάξο, ένα εξαντλημένο περιστέρι κάθισε στην πλώρη του και αρνήθηκε να φύγει.", "On Tuesday the crew of a fishing boat from Kalymnos acquired an unexpected passenger. While the boat was fishing between Amorgos and Naxos, an exhausted pigeon landed on its bow and refused to leave."),
  L("Εκφωνητής", "m", "Οι ψαράδες πρόσεξαν ότι το πουλί φορούσε στο πόδι ένα δαχτυλίδι με αριθμό. Τηλεφώνησαν στο λιμεναρχείο, και από εκεί σε έναν σύλλογο περιστεριών αγώνων, ο οποίος βρήκε τον ιδιοκτήτη μέσα σε λίγες ώρες: έναν συνταξιούχο από τη Θεσσαλονίκη.", "The fishermen noticed that the bird wore a numbered ring on its leg. They phoned the port authority, and from there a racing-pigeon club, which found the owner within a few hours: a pensioner from Thessaloniki."),
  L("Εκφωνητής", "m", "Το περιστέρι είχε ξεκινήσει πριν από τρεις μέρες σε έναν αγώνα από τη Ρόδο προς τη Θεσσαλονίκη, αλλά ένας δυνατός βοριάς φαίνεται ότι το έβγαλε εκτός πορείας. «Δεν περίμενα ποτέ να το ξαναδώ», είπε ο ιδιοκτήτης του, που θα πάει ο ίδιος να το παραλάβει.", "The pigeon had set off three days earlier in a race from Rhodes to Thessaloniki, but a strong north wind apparently blew it off course. 'I never expected to see it again,' said its owner, who will go to collect it himself."),
  L("Εκφωνητής", "m", "Μέχρι τότε, το περιστέρι ταξιδεύει με το καΐκι. Οι ψαράδες του έφτιαξαν μια φωλιά από ένα καφάσι και του δίνουν νερό και ψίχουλα. Όπως λένε, έχει γίνει πια η μασκότ του πληρώματος.", "Until then, the pigeon is travelling on the boat. The fishermen have made it a nest out of a crate and are giving it water and crumbs. As they say, it has now become the crew's mascot."),
 ],
 "questions": [
  Q("Πού κάθισε το περιστέρι;", ["Στο λιμάνι της Καλύμνου", "Στην πλώρη ενός ψαροκάικου", "Σε ένα πλοίο της γραμμής", "Σε μια βραχονησίδα"], 1, "ένα εξαντλημένο περιστέρι κάθισε στην πλώρη του"),
  Q("Πώς βρέθηκε ο ιδιοκτήτης;", ["Από μια ανάρτηση στα κοινωνικά δίκτυα", "Από ένα τσιπάκι", "Από τον αριθμό στο δαχτυλίδι, μέσω ενός συλλόγου περιστεριών αγώνων", "Από έναν κτηνίατρο της Νάξου"], 2, "ένα δαχτυλίδι με αριθμό"),
  Q("Γιατί βγήκε το περιστέρι εκτός πορείας;", ["Εξαιτίας ενός δυνατού βοριά", "Γιατί το κυνήγησε ένα γεράκι", "Γιατί ήταν άρρωστο", "Γιατί ακολούθησε το καΐκι"], 0, "ένας δυνατός βοριάς φαίνεται ότι το έβγαλε εκτός πορείας"),
  Q("Τι έφτιαξαν οι ψαράδες για το περιστέρι;", ["Ένα κλουβί από σύρμα", "Μια φωλιά από ένα καφάσι", "Μια ταΐστρα", "Ένα μικρό σπιτάκι από ξύλο"], 1, "του έφτιαξαν μια φωλιά από ένα καφάσι"),
 ],
 "gloss": {"απρόσμενο": "απρόσμενος — unexpected", "πλήρωμα": "πλήρωμα — crew", "ψαροκάικου": "ψαροκάικο — fishing boat", "εξαντλημένο": "εξαντλημένος — exhausted", "πλώρη": "πλώρη — bow (of a boat)", "λιμεναρχείο": "λιμεναρχείο — port authority", "εκτός πορείας": "εκτός πορείας — off course", "παραλάβει": "παραλαμβάνω — to collect, receive", "καφάσι": "καφάσι — crate", "ψίχουλα": "ψίχουλο — crumb", "μασκότ": "μασκότ — mascot"}
})

ITEMS.append({
 "id": "l252-vm-elaiotriveio-seira", "title": "Μήνυμα από το ελαιοτριβείο για τη σειρά σας", "title_en": "A message from the olive mill about your slot", "type": "voicemail", "level": "B2",
 "context_el": "Μαζεύετε φέτος τις ελιές του χωραφιού σας και έχετε κλείσει σειρά στο ελαιοτριβείο του χωριού. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Σταύρος", "m", "Καλημέρα σας, ο Σταύρος είμαι, από το ελαιοτριβείο. Σας παίρνω για τη σειρά σας. Την είχαμε κλείσει για την Πέμπτη το πρωί, αλλά μας χάλασε ένας από τους δύο διαχωριστές και δουλεύουμε με μισή ταχύτητα μέχρι να έρθει το ανταλλακτικό.", "Good morning, it's Stavros from the olive mill. I'm calling about your slot. We had booked it for Thursday morning, but one of our two separators has broken down and we're working at half speed until the spare part arrives."),
  L("Σταύρος", "m", "Γι' αυτό σας προτείνω να έρθετε την Παρασκευή, γύρω στις τέσσερις το απόγευμα. Ξέρω ότι θέλετε να μην περιμένουν πολλές μέρες οι ελιές στα τσουβάλια, και έχετε δίκιο, αλλά μία μέρα παραπάνω δεν θα τις πειράξει, αρκεί να τις έχετε σε δροσερό μέρος, όχι στον ήλιο.", "So I suggest you come on Friday, around four in the afternoon. I know you don't want the olives to wait in the sacks for many days, and you're right, but one more day won't harm them, as long as you keep them somewhere cool, not in the sun."),
  L("Σταύρος", "m", "Κάτι ακόμα: φέρτε τις ελιές σε τελάρα αν μπορείτε, όχι σε πλαστικές σακούλες, γιατί εκεί ζεσταίνονται και χαλάει η ποιότητα του λαδιού. Και καθαρίστε τες από τα φύλλα και τα κλαδάκια όσο γίνεται, θα τελειώσουμε πιο γρήγορα.", "One more thing: bring the olives in crates if you can, not in plastic bags, because they heat up in there and the quality of the oil suffers. And clean them of leaves and twigs as far as possible; we'll finish faster."),
  L("Σταύρος", "m", "Για το ξεμάτωμα, όπως κάθε χρόνο, κρατάμε ένα ποσοστό λάδι ή πληρώνετε σε μετρητά, όπως προτιμάτε. Αν η Παρασκευή δεν σας βολεύει, πάρτε με μέχρι αύριο το μεσημέρι στο 6974 302 118, να σας βάλω Σάββατο πρωί. Καλή συνέχεια στο μάζεμα!", "As for the milling fee, as every year, we keep a percentage of oil or you pay cash, whichever you prefer. If Friday doesn't suit you, call me by tomorrow midday on 6974 302 118 and I'll put you down for Saturday morning. Good luck with the rest of the harvest!"),
 ],
 "questions": [
  Q("Γιατί αλλάζει η σειρά;", ["Γιατί το ελαιοτριβείο κλείνει την Πέμπτη", "Γιατί χάλασε ένας διαχωριστής και δουλεύουν με μισή ταχύτητα", "Γιατί έχουν πολλούς πελάτες από άλλα χωριά", "Γιατί ο Σταύρος είναι άρρωστος"], 1, "μας χάλασε ένας από τους δύο διαχωριστές και δουλεύουμε με μισή ταχύτητα"),
  Q("Πού πρέπει να κρατηθούν οι ελιές μέχρι την Παρασκευή;", ["Σε δροσερό μέρος, όχι στον ήλιο", "Στο ψυγείο", "Σε πλαστικές σακούλες", "Στο χωράφι, κάτω από τα δέντρα"], 0, "αρκεί να τις έχετε σε δροσερό μέρος, όχι στον ήλιο"),
  Q("Γιατί δεν πρέπει να φέρουν τις ελιές σε πλαστικές σακούλες;", ["Γιατί σκίζονται", "Γιατί απαγορεύεται", "Γιατί οι ελιές ζεσταίνονται και χαλάει η ποιότητα του λαδιού", "Γιατί είναι βαριές"], 2, "εκεί ζεσταίνονται και χαλάει η ποιότητα του λαδιού"),
  Q("Τι μπορούν να κάνουν, αν δεν τους βολεύει η Παρασκευή;", ["Να έρθουν την Κυριακή", "Να τηλεφωνήσουν μέχρι αύριο το μεσημέρι για Σάββατο πρωί", "Να πάνε σε άλλο ελαιοτριβείο", "Να στείλουν μήνυμα το βράδυ"], 1, "πάρτε με μέχρι αύριο το μεσημέρι στο 6974 302 118, να σας βάλω Σάββατο πρωί"),
 ],
 "gloss": {"ελαιοτριβείο": "ελαιοτριβείο — olive mill", "σειρά": "σειρά — turn, slot", "διαχωριστές": "διαχωριστής — separator (machine)", "ανταλλακτικό": "ανταλλακτικό — spare part", "τσουβάλια": "τσουβάλι — sack", "πειράξει": "πειράζω — to harm, bother", "τελάρα": "τελάρο — crate", "κλαδάκια": "κλαδάκι — twig", "ξεμάτωμα": "ξεμάτωμα — milling fee (paid to the mill)", "ποσοστό": "ποσοστό — percentage", "μάζεμα": "μάζεμα — harvest, picking"}
})

ITEMS.append({
 "id": "l252-c1-mono-goma", "title": "Ψίχα ψωμιού και καουτσούκ: η ιστορία της γόμας", "title_en": "Breadcrumbs and rubber: the history of the eraser", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για την ιστορία των καθημερινών αντικειμένων.",
 "script": [
  L("Παρουσιαστής", "m", "Για αιώνες, όποιος ήθελε να σβήσει μια γραμμή από μολύβι χρησιμοποιούσε κάτι που είχε πάντα πάνω στο τραπέζι: ψίχα ψωμιού. Οι ζωγράφοι και οι σχεδιαστές έπλαθαν ένα μπαλάκι από μαλακό ψωμί και το περνούσαν πάνω από το χαρτί. Ήταν φτηνό, αλλά λέρωνε, θρυμματιζόταν και, φυσικά, μούχλιαζε.", "For centuries, anyone who wanted to rub out a pencil line used something that was always on the table: breadcrumb. Painters and draughtsmen would knead a little ball of soft bread and pass it over the paper. It was cheap, but it smudged, crumbled and, of course, went mouldy."),
  L("Παρουσιαστής", "m", "Το καουτσούκ, το γαλακτώδες υγρό ορισμένων τροπικών δέντρων, ήταν γνωστό στους λαούς της Κεντρικής και της Νότιας Αμερικής πολύ πριν φτάσει στην Ευρώπη. Το 1770 ο Άγγλος επιστήμονας Τζόζεφ Πρίστλεϊ σημείωσε ότι ένα κομμάτι από αυτό σβήνει θαυμάσια τα σημάδια του μολυβιού. Από αυτή τη χρήση, άλλωστε, πήρε το υλικό το αγγλικό του όνομα, «rubber», δηλαδή «αυτό που τρίβει».", "Rubber, the milky fluid of certain tropical trees, was known to the peoples of Central and South America long before it reached Europe. In 1770 the English scientist Joseph Priestley noted that a piece of it rubs out pencil marks wonderfully. It was from this use, indeed, that the material got its English name, 'rubber', that is, 'the thing that rubs'."),
  L("Παρουσιαστής", "m", "Την ίδια περίπου εποχή, ένας Λονδρέζος κατασκευαστής οργάνων άρχισε να πουλά μικρούς κύβους καουτσούκ για σβήσιμο. Λέγεται ότι ανακάλυψε την ιδιότητα κατά λάθος, όταν έπιασε ένα κομμάτι καουτσούκ αντί για την ψίχα του. Η ιστορία είναι μάλλον πολύ καλή για να είναι αληθινή, αλλά δείχνει πόσο τυχαίες φαντάζουν συχνά οι εφευρέσεις εκ των υστέρων.", "At around the same time, a London instrument maker began selling small cubes of rubber for erasing. He is said to have discovered the property by accident, when he picked up a piece of rubber instead of his breadcrumb. The story is probably too good to be true, but it shows how accidental inventions often seem with hindsight."),
  L("Παρουσιαστής", "m", "Το φυσικό καουτσούκ, όμως, είχε ένα σοβαρό ελάττωμα: το καλοκαίρι γινόταν κολλώδες και τον χειμώνα σκληρό, και με τον καιρό σάπιζε. Το πρόβλημα λύθηκε τον δέκατο ένατο αιώνα με τον βουλκανισμό, μια επεξεργασία με θείο και θερμότητα που έκανε το υλικό ανθεκτικό. Λίγα χρόνια αργότερα, κάποιος είχε την ιδέα να στερεώσει τη γόμα στην άκρη του μολυβιού, και έτσι γεννήθηκε ένας συνδυασμός που κρατάμε ακόμη στα χέρια μας.", "Natural rubber, however, had a serious flaw: in summer it became sticky and in winter hard, and over time it rotted. The problem was solved in the nineteenth century with vulcanisation, a treatment with sulphur and heat that made the material durable. A few years later, someone had the idea of fixing the eraser to the end of the pencil, and so a combination was born that we still hold in our hands."),
 ],
 "questions": [
  Q("Ποιο ήταν το μειονέκτημα της ψίχας ψωμιού;", ["Ήταν πολύ ακριβή", "Λέρωνε, θρυμματιζόταν και μούχλιαζε", "Έσκιζε το χαρτί", "Δεν έσβηνε καθόλου το μολύβι"], 1, "λέρωνε, θρυμματιζόταν και, φυσικά, μούχλιαζε"),
  Q("Από πού πήρε, σύμφωνα με τον παρουσιαστή, το καουτσούκ το αγγλικό του όνομα;", ["Από το δέντρο που το παράγει", "Από τον επιστήμονα που το ανακάλυψε", "Από τη χρήση του για να τρίβει και να σβήνει", "Από μια λέξη των λαών της Αμερικής"], 2, "Από αυτή τη χρήση, άλλωστε, πήρε το υλικό το αγγλικό του όνομα"),
  Q("Πώς κρίνει ο παρουσιαστής την ιστορία για την τυχαία ανακάλυψη;", ["Τη θεωρεί αποδεδειγμένη", "Πιστεύει ότι μάλλον είναι πολύ καλή για να είναι αληθινή", "Λέει ότι την επινόησε ο Πρίστλεϊ", "Δεν εκφράζει καμία άποψη"], 1, "Η ιστορία είναι μάλλον πολύ καλή για να είναι αληθινή"),
  Q("Τι πέτυχε ο βουλκανισμός;", ["Έκανε το καουτσούκ φθηνότερο", "Έδωσε στη γόμα χρώμα", "Έκανε το υλικό ανθεκτικό, ώστε να μην κολλάει, να μη σκληραίνει και να μη σαπίζει", "Επέτρεψε την παραγωγή μολυβιών χωρίς ξύλο"], 2, "μια επεξεργασία με θείο και θερμότητα που έκανε το υλικό ανθεκτικό"),
 ],
 "gloss": {"γόμα": "γόμα — eraser, rubber", "ψίχα": "ψίχα — crumb (soft inside of bread)", "έπλαθαν": "πλάθω — to knead, mould", "θρυμματιζόταν": "θρυμματίζομαι — to crumble", "μούχλιαζε": "μουχλιάζω — to go mouldy", "καουτσούκ": "καουτσούκ — rubber (natural)", "γαλακτώδες": "γαλακτώδης — milky", "φαντάζουν": "φαντάζω — to seem, look", "εκ των υστέρων": "εκ των υστέρων — with hindsight", "ελάττωμα": "ελάττωμα — flaw", "κολλώδες": "κολλώδης — sticky", "βουλκανισμό": "βουλκανισμός — vulcanisation", "θείο": "θείο — sulphur", "στερεώσει": "στερεώνω — to fix, attach"}
})

ITEMS.append({
 "id": "l252-c1-int-koralli-mesogeiou", "title": "Κοράλλια στη Μεσόγειο; Μια θαλάσσια βιολόγος εξηγεί", "title_en": "Corals in the Mediterranean? A marine biologist explains", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια επιστημονική εκπομπή του ραδιοφώνου.",
 "script": [
  L("Δημοσιογράφος", "f", "Όταν λέμε «κοράλλια», οι περισσότεροι σκεφτόμαστε τροπικές θάλασσες. Υπάρχουν πραγματικά κοράλλια στις ελληνικές θάλασσες;", "When we say 'corals', most of us think of tropical seas. Are there really corals in Greek seas?"),
  L("Βιολόγος", "m", "Υπάρχουν, και μάλιστα αρκετά είδη. Το πιο γνωστό είναι το κόκκινο κοράλλι, που ζει σε σκοτεινές σπηλιές και κάτω από βράχους και μεγαλώνει εξαιρετικά αργά, λίγα χιλιοστά τον χρόνο. Γι' αυτό η αλιεία του επιτρέπεται μόνο με ειδική άδεια και με αυστηρούς περιορισμούς.", "There are, and quite a few species at that. The best known is red coral, which lives in dark caves and under rocks and grows extremely slowly, a few millimetres a year. That is why harvesting it is allowed only with a special licence and under strict restrictions."),
  L("Δημοσιογράφος", "f", "Χτίζουν και ύφαλους, όπως στους τροπικούς;", "Do they build reefs too, as in the tropics?"),
  L("Βιολόγος", "m", "Σε πολύ μικρότερη κλίμακα. Υπάρχει ένα είδος, το λεγόμενο κοράλλι-μαξιλάρι, που σχηματίζει μικρές αποικίες σαν στρογγυλά μαξιλάρια και σε ορισμένα σημεία ενώνονται σε πάγκους αρκετών μέτρων. Είναι ουσιαστικά το μόνο κοράλλι της Μεσογείου που μπορεί να φτιάξει κάτι σαν ύφαλο, και δίνει καταφύγιο σε δεκάδες άλλους οργανισμούς.", "On a much smaller scale. There is a species, the so-called cushion coral, that forms small colonies like round cushions, and in some places they join into banks several metres long. It is essentially the only coral in the Mediterranean that can build something like a reef, and it shelters dozens of other organisms."),
  L("Δημοσιογράφος", "f", "Ποιος είναι ο μεγαλύτερος κίνδυνος γι' αυτά σήμερα;", "What is the greatest danger to them today?"),
  L("Βιολόγος", "m", "Οι θαλάσσιοι καύσωνες. Όταν το νερό μένει πολύ ζεστό για εβδομάδες, τα κοράλλια λευκαίνουν και πολλές αποικίες πεθαίνουν. Σε μερικές περιοχές έχουμε καταγράψει μαζικούς θανάτους μετά από ζεστά καλοκαίρια. Οι δύτες μπορούν να βοηθήσουν, αν φωτογραφίζουν τις αποικίες που βλέπουν και στέλνουν τις φωτογραφίες σε προγράμματα επιστήμης των πολιτών· έτσι μαθαίνουμε πού αντέχουν και πού χάνονται.", "Marine heatwaves. When the water stays very warm for weeks, corals bleach and many colonies die. In some areas we have recorded mass die-offs after hot summers. Divers can help if they photograph the colonies they see and send the photos to citizen-science projects; that way we learn where they hold out and where they are being lost."),
 ],
 "questions": [
  Q("Γιατί η αλιεία του κόκκινου κοραλλιού επιτρέπεται μόνο με ειδική άδεια;", ["Γιατί είναι δηλητηριώδες", "Γιατί μεγαλώνει εξαιρετικά αργά", "Γιατί ζει μόνο στην Κρήτη", "Γιατί χρησιμοποιείται στην ιατρική"], 1, "μεγαλώνει εξαιρετικά αργά, λίγα χιλιοστά τον χρόνο"),
  Q("Τι ξεχωρίζει το κοράλλι-μαξιλάρι;", ["Είναι το μεγαλύτερο κοράλλι του κόσμου", "Ζει μόνο σε σκοτεινές σπηλιές", "Είναι ουσιαστικά το μόνο κοράλλι της Μεσογείου που φτιάχνει κάτι σαν ύφαλο", "Έχει κόκκινο χρώμα"], 2, "Είναι ουσιαστικά το μόνο κοράλλι της Μεσογείου που μπορεί να φτιάξει κάτι σαν ύφαλο"),
  Q("Τι συμβαίνει στα κοράλλια όταν το νερό μένει πολύ ζεστό για εβδομάδες;", ["Μεγαλώνουν πιο γρήγορα", "Λευκαίνουν και πολλές αποικίες πεθαίνουν", "Μετακινούνται σε βαθύτερα νερά", "Αλλάζουν χρώμα και γίνονται κόκκινα"], 1, "τα κοράλλια λευκαίνουν και πολλές αποικίες πεθαίνουν"),
  Q("Πώς μπορούν να βοηθήσουν οι δύτες;", ["Μαζεύοντας τα νεκρά κοράλλια", "Φυτεύοντας νέες αποικίες", "Φωτογραφίζοντας τις αποικίες και στέλνοντας τις φωτογραφίες σε προγράμματα επιστήμης των πολιτών", "Αποφεύγοντας τις καταδύσεις το καλοκαίρι"], 2, "αν φωτογραφίζουν τις αποικίες που βλέπουν και στέλνουν τις φωτογραφίες σε προγράμματα επιστήμης των πολιτών"),
 ],
 "gloss": {"κοράλλια": "κοράλλι — coral", "αλιεία": "αλιεία — fishing, harvesting", "περιορισμούς": "περιορισμός — restriction", "ύφαλους": "ύφαλος — reef", "κλίμακα": "κλίμακα — scale", "αποικίες": "αποικία — colony", "πάγκους": "πάγκος — bank (of coral); bench", "καταφύγιο": "καταφύγιο — shelter", "καύσωνες": "καύσωνας — heatwave", "λευκαίνουν": "λευκαίνω — to bleach, whiten", "καταγράψει": "καταγράφω — to record", "μαζικούς": "μαζικός — mass"}
})
rnd = random.Random(252)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-252.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
