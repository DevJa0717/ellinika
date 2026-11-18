# Source for library/listening/listening-195.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l195.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l195-ann-efimerevonta-farmakeia", "title": "Εφημερεύοντα φαρμακεία το Σαββατοκύριακο", "title_en": "Pharmacies on duty this weekend", "type": "announcement", "level": "B2",
 "context_el": "Τηλεφωνείτε στη γραμμή του φαρμακευτικού συλλόγου της πόλης σας και ακούτε ένα ηχογραφημένο μήνυμα.",
 "script": [
  L("Ηχογραφημένη φωνή", "f", "Καλωσορίσατε στην ενημερωτική γραμμή του Φαρμακευτικού Συλλόγου. Το Σάββατο, από τις οχτώ το πρωί έως τις δύο το μεσημέρι, είναι ανοιχτά όλα τα φαρμακεία της πόλης. Από τις δύο και μετά, εφημερεύουν τα φαρμακεία της οδού Κολοκοτρώνη 12 και της πλατείας Ελευθερίας 3.", "Welcome to the Pharmaceutical Association's information line. On Saturday, from eight in the morning until two in the afternoon, all the city's pharmacies are open. From two onwards, the pharmacies at 12 Kolokotroni Street and 3 Eleftherias Square are on duty."),
  L("Ηχογραφημένη φωνή", "f", "Την Κυριακή εφημερεύει όλο το εικοσιτετράωρο το φαρμακείο της λεωφόρου Δημοκρατίας 45, απέναντι από το νοσοκομείο. Σας υπενθυμίζουμε ότι μετά τις έντεκα το βράδυ το φαρμακείο εξυπηρετεί μόνο από το παραθυράκι και μόνο για συνταγές και επείγοντα περιστατικά.", "On Sunday the pharmacy at 45 Dimokratias Avenue, opposite the hospital, is on duty around the clock. We remind you that after eleven at night the pharmacy serves only through the small window and only for prescriptions and emergencies."),
  L("Ηχογραφημένη φωνή", "f", "Για ηλεκτρονικές συνταγές, έχετε μαζί σας τον ΑΜΚΑ σας ή το κινητό στο οποίο λάβατε τον κωδικό. Για να ακούσετε ξανά το μήνυμα, πατήστε το ένα. Για τα εφημερεύοντα φαρμακεία των γύρω χωριών, πατήστε το δύο.", "For electronic prescriptions, have your social security number with you or the mobile on which you received the code. To hear the message again, press one. For the pharmacies on duty in the surrounding villages, press two."),
 ],
 "questions": [
  Q("Πότε είναι ανοιχτά όλα τα φαρμακεία το Σάββατο;", ["Όλη μέρα", "Από τις οχτώ ως τις δύο", "Μόνο το απόγευμα", "Καθόλου"], 1, "από τις οχτώ το πρωί έως τις δύο το μεσημέρι, είναι ανοιχτά όλα τα φαρμακεία"),
  Q("Πού βρίσκεται το φαρμακείο που εφημερεύει την Κυριακή;", ["Στην πλατεία Ελευθερίας", "Απέναντι από το νοσοκομείο", "Στην οδό Κολοκοτρώνη", "Σε ένα γύρω χωριό"], 1, "απέναντι από το νοσοκομείο"),
  Q("Τι ισχύει μετά τις έντεκα το βράδυ;", ["Το φαρμακείο κλείνει", "Εξυπηρετεί μόνο από το παραθυράκι για συνταγές και επείγοντα", "Χρειάζεται ραντεβού", "Πουλάει μόνο καλλυντικά"], 1, "μετά τις έντεκα το βράδυ το φαρμακείο εξυπηρετεί μόνο από το παραθυράκι"),
 ],
 "gloss": {"εφημερεύουν": "εφημερεύω — to be on duty (pharmacy, hospital)", "εικοσιτετράωρο": "εικοσιτετράωρο — twenty-four hours, around the clock", "συνταγές": "συνταγή — prescription", "επείγοντα": "επείγων — urgent; επείγοντα περιστατικά = emergencies", "ΑΜΚΑ": "ΑΜΚΑ — social security number"},
})

ITEMS.append({
 "id": "l195-int-episkevastis-akordeon", "title": "Ο άνθρωπος που επισκευάζει ακορντεόν", "title_en": "The accordion repairer", "type": "interview", "level": "B2",
 "context_el": "Ραδιοφωνική συνέντευξη με έναν τεχνίτη που επισκευάζει ακορντεόν σε ένα μικρό εργαστήριο στη Θεσσαλονίκη.",
 "script": [
  L("Δημοσιογράφος", "f", "Πόσο δύσκολο όργανο είναι το ακορντεόν για έναν επισκευαστή;", "How difficult an instrument is the accordion for a repairer?"),
  L("Τεχνίτης", "m", "Πολύ. Ένα ακορντεόν έχει μέσα του χιλιάδες κομμάτια: γλωττίδες, βαλβίδες, ελατήρια, δέρματα. Αν χαλάσει έστω και ένα, το όργανο ξεκουρδίζεται ή χάνει αέρα. Μερικές φορές για να βρω ένα πρόβλημα χρειάζομαι μια ολόκληρη μέρα, και για να το διορθώσω δέκα λεπτά.", "Very. An accordion has thousands of parts inside: reeds, valves, springs, leathers. If even one breaks, the instrument goes out of tune or loses air. Sometimes I need a whole day to find a problem, and ten minutes to fix it."),
  L("Δημοσιογράφος", "f", "Ποιοι σας φέρνουν τα όργανά τους;", "Who brings you their instruments?"),
  L("Τεχνίτης", "m", "Κάθε λογής άνθρωποι. Μουσικοί από πανηγύρια, φοιτητές του ωδείου, αλλά και πολλοί που βρήκαν ένα παλιό ακορντεόν στη σοφίτα του παππού. Αυτοί είναι οι πιο συγκινητικοί πελάτες. Δεν τους ενδιαφέρει τόσο αν θα παίζει τέλεια· θέλουν να ξανακούσουν τον ήχο που θυμούνται από παιδιά.", "All sorts of people. Musicians from village festivals, conservatory students, but also many who found an old accordion in their grandfather's attic. Those are the most moving customers. They don't care so much whether it will play perfectly; they want to hear again the sound they remember from childhood."),
  L("Δημοσιογράφος", "f", "Υπάρχουν νέοι που θέλουν να μάθουν την τέχνη σας;", "Are there young people who want to learn your craft?"),
  L("Τεχνίτης", "m", "Λίγοι. Η δουλειά θέλει υπομονή και καλό αυτί, και δεν βγάζεις πολλά χρήματα. Πέρσι όμως ήρθε ένα κορίτσι από τη Δράμα, που σπουδάζει μουσική, και μου ζήτησε να μάθει. Έρχεται κάθε Σάββατο. Σε δύο χρόνια ελπίζω να μπορεί να δουλεύει μόνη της.", "Few. The work needs patience and a good ear, and you don't earn much money. But last year a girl from Drama, who studies music, came and asked me to learn. She comes every Saturday. In two years I hope she'll be able to work on her own."),
 ],
 "questions": [
  Q("Γιατί είναι δύσκολη η επισκευή του ακορντεόν;", ["Γιατί είναι πολύ βαρύ", "Γιατί έχει χιλιάδες κομμάτια, και αν χαλάσει ένα, επηρεάζεται όλο το όργανο", "Γιατί δεν υπάρχουν ανταλλακτικά", "Γιατί είναι πολύ ακριβό"], 1, "Ένα ακορντεόν έχει μέσα του χιλιάδες κομμάτια"),
  Q("Τι θέλουν κυρίως όσοι φέρνουν το ακορντεόν του παππού τους;", ["Να το πουλήσουν", "Να παίζει τέλεια", "Να ξανακούσουν τον ήχο που θυμούνται", "Να το βάψουν"], 2, "θέλουν να ξανακούσουν τον ήχο που θυμούνται από παιδιά"),
  Q("Ποια είναι η νέα του μαθήτρια;", ["Η κόρη του", "Μια φοιτήτρια μουσικής από τη Δράμα", "Μια μουσικός από πανηγύρια", "Μια πελάτισσα"], 1, "ήρθε ένα κορίτσι από τη Δράμα, που σπουδάζει μουσική"),
 ],
 "gloss": {"γλωττίδες": "γλωττίδα — reed (of an instrument)", "βαλβίδες": "βαλβίδα — valve", "ελατήρια": "ελατήριο — spring", "ξεκουρδίζεται": "ξεκουρδίζομαι — to go out of tune", "σοφίτα": "σοφίτα — attic", "ωδείου": "ωδείο — music school, conservatory"},
})

ITEMS.append({
 "id": "l195-vm-plyntirio", "title": "Μήνυμα από το πλυντήριο αυτοκινήτων", "title_en": "A message from the car wash", "type": "voicemail", "level": "B2",
 "context_el": "Αφήσατε το αυτοκίνητό σας για εσωτερικό και εξωτερικό καθαρισμό. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, από το πλυντήριο της οδού Τσιμισκή σας παίρνω, για το γκρι αυτοκίνητο που μας αφήσατε το πρωί. Καθαρίζοντας το εσωτερικό, βρήκαμε κάτω από το κάθισμα του οδηγού ένα χρυσό σκουλαρίκι. Το έχουμε βάλει σε ένα φακελάκι στο ταμείο, για να μη χαθεί.", "Good morning, I'm calling from the car wash on Tsimiski Street, about the grey car you left with us this morning. While cleaning the interior, we found a gold earring under the driver's seat. We've put it in a little envelope at the till, so it doesn't get lost."),
  L("Υπάλληλος", "m", "Επίσης, όταν το πλύναμε, είδαμε ότι στο παρμπρίζ, κάτω δεξιά, υπάρχει μια μικρή ρωγμή, σαν από πετραδάκι. Δεν την κάναμε εμείς, ήταν ήδη εκεί, αλλά σας το λέμε γιατί με το κρύο τέτοιες ρωγμές συχνά μεγαλώνουν. Ένα συνεργείο μπορεί να τη γεμίσει με ειδική ρητίνη, χωρίς να αλλάξετε όλο το τζάμι.", "Also, when we washed it, we saw that on the windscreen, at the bottom right, there's a small crack, as if from a little stone. We didn't do it, it was already there, but we're telling you because in the cold such cracks often grow. A garage can fill it with special resin, without you having to change the whole glass."),
  L("Υπάλληλος", "m", "Το αυτοκίνητο θα είναι έτοιμο στις δώδεκα, όχι στις έντεκα όπως σας είχαμε πει, γιατί καθυστέρησε ο καθαρισμός των καθισμάτων. Κλείνουμε στις οχτώ. Ευχαριστούμε.", "The car will be ready at twelve, not at eleven as we told you, because cleaning the seats took longer. We close at eight. Thank you."),
 ],
 "questions": [
  Q("Τι βρήκαν στο αυτοκίνητο;", ["Ένα πορτοφόλι", "Ένα χρυσό σκουλαρίκι", "Ένα κλειδί", "Ένα κινητό"], 1, "βρήκαμε κάτω από το κάθισμα του οδηγού ένα χρυσό σκουλαρίκι"),
  Q("Τι λέει ο υπάλληλος για τη ρωγμή στο παρμπρίζ;", ["Ότι την έκαναν κατά λάθος", "Ότι ήταν ήδη εκεί και μπορεί να μεγαλώσει με το κρύο", "Ότι πρέπει να αλλάξει όλο το τζάμι", "Ότι δεν είναι τίποτα σοβαρό"], 1, "με το κρύο τέτοιες ρωγμές συχνά μεγαλώνουν"),
  Q("Γιατί καθυστερεί το αυτοκίνητο;", ["Γιατί δεν υπάρχει προσωπικό", "Γιατί καθυστέρησε ο καθαρισμός των καθισμάτων", "Γιατί χάλασε το μηχάνημα", "Γιατί έψαχναν τον ιδιοκτήτη του σκουλαρικιού"], 1, "γιατί καθυστέρησε ο καθαρισμός των καθισμάτων"),
 ],
 "gloss": {"σκουλαρίκι": "σκουλαρίκι — earring", "παρμπρίζ": "παρμπρίζ — windscreen", "ρωγμή": "ρωγμή — crack", "ρητίνη": "ρητίνη — resin", "ταμείο": "ταμείο — till, cash desk"},
})

ITEMS.append({
 "id": "l195-mono-jet-lag", "title": "Πώς νίκησα το τζετ λαγκ", "title_en": "How I beat jet lag", "type": "monologue", "level": "B2",
 "context_el": "Μια νοσηλεύτρια μιλά σε ένα ταξιδιωτικό podcast για το ταξίδι της στον Καναδά.",
 "script": [
  L("Ζωή", "f", "Πέρσι τα Χριστούγεννα πήγα να δω την αδελφή μου στο Βανκούβερ. Δέκα ώρες διαφορά. Την πρώτη εβδομάδα ξυπνούσα στις τρεις τα ξημερώματα, πεινασμένη και ολόξυπνη, και στις έξι το απόγευμα κοιμόμουν πάνω στο πιάτο μου. Η αδελφή μου γελούσε, εγώ καθόλου.", "Last Christmas I went to see my sister in Vancouver. Ten hours' difference. The first week I would wake up at three in the morning, hungry and wide awake, and at six in the evening I'd fall asleep over my plate. My sister laughed; I didn't at all."),
  L("Ζωή", "f", "Στην επιστροφή αποφάσισα να το πάρω πιο σοβαρά. Δουλεύω σε βάρδιες, οπότε ξέρω κάτι για τον ύπνο. Τρεις μέρες πριν φύγω, άρχισα να πηγαίνω για ύπνο λίγο νωρίτερα κάθε βράδυ. Στο αεροπλάνο έβαλα το ρολόι μου αμέσως στην ώρα της Ελλάδας και έφαγα και κοιμήθηκα σύμφωνα με αυτήν.", "On the way back I decided to take it more seriously. I work shifts, so I know something about sleep. Three days before leaving, I started going to bed a little earlier every evening. On the plane I set my watch straight away to Greek time and ate and slept according to it."),
  L("Ζωή", "f", "Το πιο σημαντικό όμως ήταν το φως. Την πρώτη μέρα στην Αθήνα, όσο κι αν νύσταζα, βγήκα για περπάτημα στον ήλιο το πρωί και δεν κοιμήθηκα το μεσημέρι. Και τον καφέ τον σταμάτησα μετά τις δύο. Μέσα σε τρεις μέρες ήμουν εντάξει. Δεν λέω ότι είναι μαγική συνταγή, αλλά σε μένα δούλεψε.", "But the most important thing was light. On the first day in Athens, however sleepy I was, I went out for a walk in the sun in the morning and didn't sleep at midday. And I stopped coffee after two. Within three days I was fine. I'm not saying it's a magic recipe, but it worked for me."),
 ],
 "questions": [
  Q("Τι της συνέβαινε την πρώτη εβδομάδα στο Βανκούβερ;", ["Δεν μπορούσε να φάει", "Ξυπνούσε τα ξημερώματα και νύσταζε νωρίς το απόγευμα", "Αρρώστησε", "Δεν κοιμόταν καθόλου"], 1, "ξυπνούσα στις τρεις τα ξημερώματα, πεινασμένη και ολόξυπνη, και στις έξι το απόγευμα κοιμόμουν"),
  Q("Τι έκανε στο αεροπλάνο της επιστροφής;", ["Κοιμήθηκε όλη την ώρα", "Έβαλε το ρολόι της στην ώρα της Ελλάδας", "Ήπιε πολλούς καφέδες", "Δεν έφαγε τίποτα"], 1, "Στο αεροπλάνο έβαλα το ρολόι μου αμέσως στην ώρα της Ελλάδας"),
  Q("Τι θεωρεί πιο σημαντικό;", ["Το φως", "Τα χάπια", "Το φαγητό", "Τον μεσημεριανό ύπνο"], 0, "Το πιο σημαντικό όμως ήταν το φως"),
 ],
 "gloss": {"ξημερώματα": "ξημερώματα — early morning hours", "ολόξυπνη": "ολόξυπνος — wide awake", "βάρδιες": "βάρδια — shift", "νύσταζα": "νυστάζω — to be sleepy", "συνταγή": "συνταγή — recipe"},
})

ITEMS.append({
 "id": "l195-dia-chronos-diakopis", "title": "Ένας χρόνος διάλειμμα πριν από το πανεπιστήμιο;", "title_en": "A gap year before university?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο γονείς συζητούν την ιδέα του γιου τους να κάνει ένα χρόνο διάλειμμα πριν αρχίσει τις σπουδές του.",
 "script": [
  L("Αργύρης", "m", "Ο Στέλιος μού είπε χθες ότι θέλει να αναβάλει την εγγραφή του στο πανεπιστήμιο για έναν χρόνο. Λέει ότι θέλει να δουλέψει σε μια φάρμα στη Νέα Ζηλανδία. Νομίζω ότι θα χάσει τον ρυθμό του και δεν θα ξαναγυρίσει στο διάβασμα.", "Stelios told me yesterday that he wants to postpone his enrolment at university for a year. He says he wants to work on a farm in New Zealand. I think he'll lose his rhythm and won't go back to studying."),
  L("Μαρίνα", "f", "Κι εγώ ανησύχησα στην αρχή. Αλλά σκέψου πώς πέρασε τους τελευταίους δύο χρόνους: φροντιστήριο ως τις δέκα το βράδυ, Σαββατοκύριακα με βιβλία. Είναι εξαντλημένος. Και δεν είναι καν σίγουρος ότι του αρέσει η σχολή που πέρασε.", "I was worried too at first. But think how he spent the last two years: cram school until ten at night, weekends with books. He's exhausted. And he isn't even sure he likes the department he got into."),
  L("Αργύρης", "m", "Κι αν δεν του αρέσει, τι θα κάνει; Θα ξαναδώσει εξετάσεις;", "And if he doesn't like it, what will he do? Sit the exams again?"),
  L("Μαρίνα", "f", "Ίσως. Αλλά καλύτερα να το καταλάβει τώρα παρά στο τρίτο έτος. Ρώτησα στη γραμματεία της σχολής: μπορεί να ζητήσει αναστολή φοίτησης, και η θέση του κρατιέται. Και τα έξοδα του ταξιδιού θα τα βγάλει μόνος του, από τη δουλειά στη φάρμα.", "Maybe. But better he realises it now than in the third year. I asked at the department office: he can request a suspension of studies, and his place is kept. And he'll cover the travel costs himself, from the farm job."),
  L("Αργύρης", "m", "Καλά. Αλλά με έναν όρο: να μας στέλνει νέα κάθε εβδομάδα, και τον Σεπτέμβριο του χρόνου να είναι στο αμφιθέατρο.", "All right. But on one condition: he sends us news every week, and next September he's in the lecture hall."),
 ],
 "questions": [
  Q("Τι φοβάται ο Αργύρης;", ["Ότι ο γιος του θα μείνει για πάντα στη Νέα Ζηλανδία", "Ότι θα χάσει τον ρυθμό του και δεν θα ξαναγυρίσει στο διάβασμα", "Ότι το ταξίδι θα είναι πολύ ακριβό", "Ότι θα χάσει τη θέση του"], 1, "θα χάσει τον ρυθμό του και δεν θα ξαναγυρίσει στο διάβασμα"),
  Q("Τι έμαθε η Μαρίνα από τη γραμματεία;", ["Ότι πρέπει να ξαναδώσει εξετάσεις", "Ότι μπορεί να ζητήσει αναστολή φοίτησης και η θέση του κρατιέται", "Ότι δεν επιτρέπεται διάλειμμα", "Ότι πρέπει να πληρώσει δίδακτρα"], 1, "μπορεί να ζητήσει αναστολή φοίτησης, και η θέση του κρατιέται"),
  Q("Ποιον όρο βάζει ο Αργύρης;", ["Να μην ταξιδέψει μόνος", "Να στέλνει νέα κάθε εβδομάδα και να γυρίσει για τις σπουδές τον Σεπτέμβριο", "Να του στέλνει χρήματα", "Να μείνει μόνο έξι μήνες"], 1, "να μας στέλνει νέα κάθε εβδομάδα"),
 ],
 "gloss": {"αναβάλει": "αναβάλλω — to postpone", "εγγραφή": "εγγραφή — enrolment, registration", "εξαντλημένος": "εξαντλημένος — exhausted", "αναστολή": "αναστολή φοίτησης — suspension of studies", "αμφιθέατρο": "αμφιθέατρο — lecture hall"},
})

ITEMS.append({
 "id": "l195-rep-scholeio-choris-ergasies", "title": "Ένα σχολείο χωρίς εργασίες για το σπίτι", "title_en": "A school without homework", "type": "report", "level": "B2",
 "context_el": "Ρεπορτάζ για ένα δημοτικό σχολείο που δοκιμάζει να μη δίνει εργασίες για το σπίτι.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο δημοτικό σχολείο μιας μικρής πόλης της Αχαΐας, οι μαθητές φεύγουν το μεσημέρι με ελαφριές τσάντες. Από τον Σεπτέμβριο, ο σύλλογος διδασκόντων αποφάσισε, σε συνεννόηση με τους γονείς, να καταργήσει δοκιμαστικά τις γραπτές εργασίες για το σπίτι.", "At the primary school of a small town in Achaea, the pupils leave at midday with light bags. Since September, the teachers' council has decided, in agreement with the parents, to abolish written homework on a trial basis."),
  L("Ρεπόρτερ", "m", "Αυτό δεν σημαίνει ότι τα παιδιά δεν κάνουν τίποτα στο σπίτι. Η διευθύντρια εξηγεί ότι τους ζητούν να διαβάζουν είκοσι λεπτά την ημέρα ένα βιβλίο της επιλογής τους, και να βοηθούν σε μια δουλειά του σπιτιού. Τις ασκήσεις τις κάνουν στην τάξη, όπου ο δάσκαλος μπορεί να δει αμέσως πού δυσκολεύεται ο καθένας.", "That doesn't mean the children do nothing at home. The head teacher explains that they ask them to read a book of their choice for twenty minutes a day, and to help with a household chore. They do the exercises in class, where the teacher can see straight away where each one is struggling."),
  L("Ρεπόρτερ", "m", "Οι γονείς είναι μοιρασμένοι. Μια μητέρα λέει ότι τα απογεύματα στο σπίτι της έγιναν επιτέλους ήρεμα, χωρίς καβγάδες πάνω από τα τετράδια. Ένας πατέρας όμως ανησυχεί ότι η κόρη του δεν θα είναι έτοιμη για το γυμνάσιο, όπου οι εργασίες είναι πολλές.", "The parents are divided. A mother says afternoons at her home have finally become calm, without arguments over exercise books. A father, though, worries that his daughter won't be ready for secondary school, where there's a lot of homework."),
  L("Ρεπόρτερ", "m", "Οι έρευνες για το θέμα δεν δίνουν ξεκάθαρη απάντηση, και γι' αυτό το σχολείο θα αξιολογήσει την προσπάθεια στο τέλος της χρονιάς, με τεστ και ερωτηματολόγια για μαθητές και γονείς.", "Research on the subject doesn't give a clear answer, which is why the school will evaluate the effort at the end of the year, with tests and questionnaires for pupils and parents."),
 ],
 "questions": [
  Q("Τι ζητούν από τους μαθητές να κάνουν στο σπίτι;", ["Τίποτα απολύτως", "Να διαβάζουν είκοσι λεπτά και να βοηθούν σε μια δουλειά του σπιτιού", "Να λύνουν ασκήσεις μαθηματικών", "Να γράφουν έκθεση κάθε μέρα"], 1, "τους ζητούν να διαβάζουν είκοσι λεπτά την ημέρα"),
  Q("Γιατί κάνουν τις ασκήσεις στην τάξη;", ["Για να τελειώνουν πιο γρήγορα", "Για να βλέπει ο δάσκαλος αμέσως πού δυσκολεύεται ο καθένας", "Γιατί δεν έχουν βιβλία στο σπίτι", "Γιατί το ζήτησε το υπουργείο"], 1, "ο δάσκαλος μπορεί να δει αμέσως πού δυσκολεύεται ο καθένας"),
  Q("Τι ανησυχεί έναν πατέρα;", ["Ότι η κόρη του βαριέται", "Ότι η κόρη του δεν θα είναι έτοιμη για το γυμνάσιο", "Ότι δεν βλέπει τα τετράδια", "Ότι το σχολείο θα κλείσει"], 1, "η κόρη του δεν θα είναι έτοιμη για το γυμνάσιο"),
 ],
 "gloss": {"διδασκόντων": "σύλλογος διδασκόντων — teachers' council", "καταργήσει": "καταργώ — to abolish", "δοκιμαστικά": "δοκιμαστικά — on a trial basis", "μοιρασμένοι": "μοιρασμένος — divided", "αξιολογήσει": "αξιολογώ — to evaluate", "ερωτηματολόγια": "ερωτηματολόγιο — questionnaire"},
})

ITEMS.append({
 "id": "l195-rep-skeitparko-efivon", "title": "Το σκέιτπαρκ που έφτιαξαν οι έφηβοι", "title_en": "The skatepark the teenagers built", "type": "report", "level": "B2",
 "context_el": "Ρεπορτάζ για ένα σκέιτπαρκ που σχεδίασαν και έφτιαξαν οι ίδιοι οι νέοι μιας γειτονιάς.",
 "script": [
  L("Ρεπόρτερ", "f", "Για χρόνια, τα παιδιά με τα σκέιτμπορντ έκαναν τα κόλπα τους στα σκαλιά του δημαρχείου, και οι υπάλληλοι τα έδιωχναν σχεδόν κάθε απόγευμα. Πριν από δύο χρόνια, μια παρέα δεκαπεντάχρονων πήγε στο δημοτικό συμβούλιο με ένα σχέδιο ζωγραφισμένο σε χαρτόνι.", "For years, the kids with skateboards did their tricks on the town hall steps, and the staff chased them away almost every afternoon. Two years ago, a group of fifteen-year-olds went to the town council with a plan drawn on cardboard."),
  L("Ρεπόρτερ", "f", "Ο δήμος τούς παραχώρησε ένα εγκαταλελειμμένο γήπεδο μπάσκετ και πλήρωσε το τσιμέντο. Τα υπόλοιπα τα έκαναν οι ίδιοι, με τη βοήθεια ενός πολιτικού μηχανικού, πατέρα ενός από τα παιδιά. Δούλευαν τα Σαββατοκύριακα για έναν ολόκληρο χειμώνα.", "The municipality gave them an abandoned basketball court and paid for the cement. They did the rest themselves, with the help of a civil engineer, the father of one of the kids. They worked at weekends for a whole winter."),
  L("Ρεπόρτερ", "f", "Σήμερα το σκέιτπαρκ είναι γεμάτο από το μεσημέρι ως το βράδυ, και όχι μόνο με αγόρια. Οι ίδιοι οι νέοι έχουν γράψει τους κανόνες: κράνος για τους κάτω των δώδεκα, κανένα σκουπίδι στο έδαφος, και οι μεγαλύτεροι μαθαίνουν τους μικρότερους.", "Today the skatepark is full from midday until the evening, and not only with boys. The young people themselves have written the rules: helmets for under-twelves, no rubbish on the ground, and the older ones teach the younger ones."),
  L("Ρεπόρτερ", "f", "Η μόνη που λείπει είναι η ησυχία στο δημαρχείο, λέει χαμογελώντας ένας υπάλληλος. Ο δήμαρχος σκέφτεται τώρα να ρωτήσει τους εφήβους και για τη νέα παιδική χαρά.", "The only thing missing is the noise at the town hall, says one of the staff with a smile. The mayor is now thinking of asking the teenagers about the new playground too."),
 ],
 "questions": [
  Q("Πού έκαναν παλιά τα κόλπα τους τα παιδιά;", ["Στην παιδική χαρά", "Στα σκαλιά του δημαρχείου", "Στο γήπεδο του σχολείου", "Στην παραλία"], 1, "έκαναν τα κόλπα τους στα σκαλιά του δημαρχείου"),
  Q("Τι έδωσε ο δήμος;", ["Ένα εγκαταλελειμμένο γήπεδο και το τσιμέντο", "Χρήματα για σκέιτμπορντ", "Έναν προπονητή", "Τίποτα"], 0, "Ο δήμος τούς παραχώρησε ένα εγκαταλελειμμένο γήπεδο μπάσκετ και πλήρωσε το τσιμέντο"),
  Q("Ποιος από τους κανόνες αναφέρεται;", ["Κανείς κάτω των δώδεκα δεν μπαίνει", "Οι μεγαλύτεροι μαθαίνουν τους μικρότερους", "Το πάρκο κλείνει στις έξι", "Απαγορεύεται η μουσική"], 1, "οι μεγαλύτεροι μαθαίνουν τους μικρότερους"),
 ],
 "gloss": {"κόλπα": "κόλπο — trick", "παραχώρησε": "παραχωρώ — to grant, hand over", "εγκαταλελειμμένο": "εγκαταλελειμμένος — abandoned", "τσιμέντο": "τσιμέντο — cement", "κράνος": "κράνος — helmet"},
})

ITEMS.append({
 "id": "l195-news-chalazi-stin-poli", "title": "Χαλάζι στην πόλη: ζημιές σε εκατοντάδες αυτοκίνητα", "title_en": "Hail in the city: hundreds of cars damaged", "type": "news", "level": "B2",
 "context_el": "Είδηση από τοπικό δελτίο ειδήσεων μετά από μια σύντομη αλλά έντονη χαλαζόπτωση.",
 "script": [
  L("Εκφωνητής", "m", "Σύντομη αλλά πολύ έντονη χαλαζόπτωση έπληξε χθες το απόγευμα το κέντρο της Λάρισας. Για περίπου δέκα λεπτά έπεφταν κόκκοι χαλαζιού σε μέγεθος καρυδιού, που προκάλεσαν ζημιές σε εκατοντάδες σταθμευμένα αυτοκίνητα και έσπασαν τζάμια σε καταστήματα.", "A short but very intense hailstorm hit the centre of Larissa yesterday afternoon. For about ten minutes hailstones the size of walnuts fell, causing damage to hundreds of parked cars and breaking shop windows."),
  L("Εκφωνητής", "m", "Η πυροσβεστική δέχτηκε πάνω από ογδόντα κλήσεις, κυρίως για πλημμυρισμένα υπόγεια και φρεάτια που βούλωσαν από τα φύλλα και τον πάγο. Δεν αναφέρθηκαν τραυματισμοί.", "The fire service received more than eighty calls, mainly for flooded basements and drains blocked by leaves and ice. No injuries were reported."),
  L("Εκφωνητής", "m", "Η Ένωση Ασφαλιστικών Εταιρειών υπενθυμίζει ότι οι ζημιές από χαλάζι καλύπτονται μόνο αν το συμβόλαιο περιλαμβάνει την κάλυψη για φυσικά φαινόμενα. Οι ιδιοκτήτες συνιστάται να φωτογραφίσουν τις ζημιές πριν από οποιαδήποτε επισκευή και να τις δηλώσουν μέσα σε λίγες ημέρες.", "The Association of Insurance Companies reminds that hail damage is covered only if the policy includes cover for natural phenomena. Owners are advised to photograph the damage before any repair and to report it within a few days."),
  L("Εκφωνητής", "m", "Σύμφωνα με τους μετεωρολόγους, ο καιρός θα παραμείνει άστατος και αύριο, με πιθανότητα για καταιγίδες κυρίως τις απογευματινές ώρες.", "According to meteorologists, the weather will remain unsettled tomorrow too, with a chance of storms, mainly in the afternoon."),
 ],
 "questions": [
  Q("Πόσο κράτησε η χαλαζόπτωση;", ["Περίπου δέκα λεπτά", "Μία ώρα", "Όλο το απόγευμα", "Όλη τη νύχτα"], 0, "Για περίπου δέκα λεπτά έπεφταν κόκκοι χαλαζιού"),
  Q("Για ποιο λόγο κλήθηκε κυρίως η πυροσβεστική;", ["Για φωτιές", "Για πλημμυρισμένα υπόγεια και βουλωμένα φρεάτια", "Για τραυματίες", "Για πεσμένα δέντρα"], 1, "κυρίως για πλημμυρισμένα υπόγεια και φρεάτια"),
  Q("Πότε καλύπτονται οι ζημιές από χαλάζι;", ["Πάντα", "Ποτέ", "Μόνο αν το συμβόλαιο περιλαμβάνει κάλυψη για φυσικά φαινόμενα", "Μόνο για καινούργια αυτοκίνητα"], 2, "καλύπτονται μόνο αν το συμβόλαιο περιλαμβάνει την κάλυψη για φυσικά φαινόμενα"),
 ],
 "gloss": {"χαλαζόπτωση": "χαλαζόπτωση — hailstorm", "χαλαζιού": "χαλάζι — hail", "φρεάτια": "φρεάτιο — drain, manhole", "συμβόλαιο": "συμβόλαιο — (insurance) policy, contract", "άστατος": "άστατος — unsettled, changeable"},
})

ITEMS.append({
 "id": "l195-c1-int-giati-gourgourizei-to-stomachi", "title": "Γιατί γουργουρίζει το στομάχι;", "title_en": "Why does the stomach rumble?", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με γαστρεντερολόγο σε ραδιοφωνική εκπομπή για την υγεία.",
 "script": [
  L("Δημοσιογράφος", "f", "Γιατρέ, όλοι έχουμε βρεθεί σε μια σιωπηλή αίθουσα συσκέψεων όταν το στομάχι μας αποφασίζει να μιλήσει. Τι ακριβώς συμβαίνει;", "Doctor, we've all found ourselves in a silent meeting room when our stomach decides to speak. What exactly is happening?"),
  L("Γαστρεντερολόγος", "m", "Το γουργουρητό είναι απλώς ο ήχος από τη μετακίνηση αερίων και υγρών μέσα στο έντερο και στο στομάχι. Τα τοιχώματά τους συσπώνται ρυθμικά, για να προωθούν την τροφή, και όπου υπάρχει αέρας μαζί με υγρό, η κίνηση αυτή ακούγεται. Δεν είναι, λοιπόν, ένδειξη ότι κάτι πάει στραβά.", "The rumbling is simply the sound of gas and fluids moving inside the intestine and the stomach. Their walls contract rhythmically to push food along, and wherever there's air together with fluid, that movement is audible. So it's not a sign that something is wrong."),
  L("Δημοσιογράφος", "f", "Τότε γιατί το συνδέουμε με την πείνα;", "Then why do we associate it with hunger?"),
  L("Γαστρεντερολόγος", "m", "Γιατί όταν το στομάχι είναι άδειο για αρκετές ώρες, ενεργοποιείται ένα κύμα συσπάσεων που λειτουργεί σαν σκούπα: καθαρίζει ό,τι υπολείμματα έχουν μείνει. Επειδή δεν υπάρχει τροφή να «απορροφήσει» τον ήχο, το γουργουρητό είναι πιο δυνατό. Ταυτόχρονα, ορμόνες που σχετίζονται με την πείνα φαίνεται ότι ενισχύουν αυτές τις κινήσεις. Θα έλεγα όμως ότι η σχέση πείνας και ήχου δεν είναι τόσο απλή όσο νομίζουμε: το στομάχι γουργουρίζει και μετά το φαγητό, απλώς τότε δεν το ακούμε τόσο καθαρά.", "Because when the stomach has been empty for several hours, a wave of contractions is triggered that works like a vacuum cleaner: it clears out whatever remnants are left. Since there's no food to 'absorb' the sound, the rumbling is louder. At the same time, hormones linked to hunger seem to strengthen these movements. I would say, though, that the relationship between hunger and sound isn't as simple as we think: the stomach rumbles after eating too, we just don't hear it as clearly then."),
  L("Δημοσιογράφος", "f", "Και πότε πρέπει να ανησυχήσουμε;", "And when should we worry?"),
  L("Γαστρεντερολόγος", "m", "Το γουργουρητό από μόνο του σχεδόν ποτέ δεν είναι πρόβλημα. Αν όμως συνοδεύεται από πόνο, φούσκωμα που δεν περνά, διάρροια ή απώλεια βάρους, τότε αξίζει να το δει ένας γιατρός. Και για τη σύσκεψη, η καλύτερη συμβουλή είναι η πιο απλή: ένα μικρό σνακ μία ώρα πριν.", "Rumbling on its own is almost never a problem. But if it comes with pain, bloating that doesn't go away, diarrhoea or weight loss, then it's worth having a doctor look at it. And for the meeting, the best advice is the simplest: a small snack an hour before."),
 ],
 "questions": [
  Q("Τι είναι, σύμφωνα με τον γιατρό, το γουργουρητό;", ["Ένδειξη ασθένειας", "Ο ήχος από τη μετακίνηση αερίων και υγρών στο έντερο και στο στομάχι", "Ο ήχος της πέψης των λιπαρών", "Μια αντίδραση στο άγχος"], 1, "είναι απλώς ο ήχος από τη μετακίνηση αερίων και υγρών"),
  Q("Γιατί το γουργουρητό είναι πιο δυνατό όταν το στομάχι είναι άδειο;", ["Γιατί το στομάχι μικραίνει", "Γιατί δεν υπάρχει τροφή να απορροφήσει τον ήχο", "Γιατί πίνουμε περισσότερο νερό", "Γιατί σταματούν οι συσπάσεις"], 1, "Επειδή δεν υπάρχει τροφή να «απορροφήσει» τον ήχο"),
  Q("Πώς παρουσιάζει ο γιατρός τη σχέση πείνας και γουργουρητού;", ["Ως απόλυτα απλή", "Ως ανύπαρκτη", "Ως πιο περίπλοκη απ' ό,τι νομίζουμε", "Ως άγνωστη στην επιστήμη"], 2, "η σχέση πείνας και ήχου δεν είναι τόσο απλή όσο νομίζουμε"),
 ],
 "gloss": {"γουργουρητό": "γουργουρητό — rumbling", "συσπώνται": "συσπώμαι — to contract", "προωθούν": "προωθώ — to push forward, propel", "υπολείμματα": "υπόλειμμα — remnant, residue", "φούσκωμα": "φούσκωμα — bloating"},
})

ITEMS.append({
 "id": "l195-c1-mono-anatrichila", "title": "Ανατριχίλα: μια κληρονομιά από τους προγόνους μας", "title_en": "Goosebumps: a legacy from our ancestors", "type": "monologue", "level": "C1",
 "context_el": "Απόσπασμα από εκπομπή εκλαΐκευσης της επιστήμης για την ανατριχίλα.",
 "script": [
  L("Παρουσιάστρια", "f", "Βγαίνουμε από τη θάλασσα και φυσάει, ή ακούμε ένα τραγούδι που μας συγκινεί, και ξαφνικά το δέρμα μας γεμίζει μικρά εξογκώματα και οι τρίχες σηκώνονται. Τα ελληνικά έχουν για αυτό μια ωραία έκφραση: «μου σηκώθηκε η τρίχα».", "We come out of the sea and the wind is blowing, or we hear a song that moves us, and suddenly our skin is covered in little bumps and the hairs stand up. Greek has a nice expression for this: 'my hair stood up'."),
  L("Παρουσιάστρια", "f", "Ο μηχανισμός είναι απλός. Στη βάση κάθε τρίχας υπάρχει ένας μικροσκοπικός μυς. Όταν το νευρικό σύστημα δώσει το σήμα, αυτός ο μυς συσπάται, η τρίχα ορθώνεται και το δέρμα γύρω της φουσκώνει λίγο. Το σήμα δεν το ελέγχουμε εμείς· είναι μέρος του λεγόμενου αυτόνομου νευρικού συστήματος, του ίδιου που επιταχύνει την καρδιά όταν τρομάζουμε.", "The mechanism is simple. At the base of each hair there's a tiny muscle. When the nervous system gives the signal, this muscle contracts, the hair stands up and the skin around it swells a little. We don't control the signal; it's part of the so-called autonomic nervous system, the same one that speeds up the heart when we're frightened."),
  L("Παρουσιάστρια", "f", "Σε ζώα με πυκνό τρίχωμα, η αντίδραση αυτή έχει νόημα: οι τρίχες που σηκώνονται παγιδεύουν ένα στρώμα αέρα και κρατούν τη ζέστη, ή κάνουν το ζώο να φαίνεται μεγαλύτερο μπροστά σε έναν εχθρό. Σε εμάς, που έχουμε χάσει το μεγαλύτερο μέρος του τριχώματος, πιθανότατα πρόκειται για ένα κατάλοιπο χωρίς ιδιαίτερη χρησιμότητα.", "In animals with thick fur, this reaction makes sense: the raised hairs trap a layer of air and keep in the warmth, or make the animal look bigger in front of an enemy. In us, who have lost most of our body hair, it's probably a leftover without any particular use."),
  L("Παρουσιάστρια", "f", "Πιο αινιγματική είναι η ανατριχίλα από τη μουσική. Γιατί μια μελωδία να ενεργοποιεί έναν μηχανισμό που φτιάχτηκε για το κρύο και τον φόβο; Υπάρχουν διάφορες υποθέσεις, για παράδειγμα ότι συνδέεται με το σύστημα ανταμοιβής του εγκεφάλου, αλλά καμία δεν έχει ακόμα επιβεβαιωθεί οριστικά. Ίσως αυτό να είναι και το πιο ωραίο: ότι ένα κομμάτι της συγκίνησης μένει μυστήριο.", "More puzzling are the chills from music. Why should a melody trigger a mechanism made for cold and fear? There are various hypotheses, for example that it's linked to the brain's reward system, but none has yet been definitively confirmed. Perhaps that's the nicest thing: that a part of emotion remains a mystery."),
 ],
 "questions": [
  Q("Τι προκαλεί τη σήκωση της τρίχας;", ["Η αλλαγή της θερμοκρασίας του αίματος", "Η σύσπαση ενός μικροσκοπικού μυός στη βάση της τρίχας", "Η εφίδρωση", "Η ξηρότητα του δέρματος"], 1, "αυτός ο μυς συσπάται, η τρίχα ορθώνεται"),
  Q("Ποια χρησιμότητα έχει η αντίδραση στα ζώα με πυκνό τρίχωμα;", ["Τα βοηθά να βλέπουν καλύτερα", "Κρατά τη ζέστη ή τα κάνει να φαίνονται μεγαλύτερα", "Τα βοηθά να τρέχουν πιο γρήγορα", "Δεν έχει καμία χρησιμότητα"], 1, "παγιδεύουν ένα στρώμα αέρα και κρατούν τη ζέστη, ή κάνουν το ζώο να φαίνεται μεγαλύτερο"),
  Q("Τι λέει για την ανατριχίλα από τη μουσική;", ["Ότι έχει εξηγηθεί πλήρως", "Ότι υπάρχουν υποθέσεις, αλλά καμία δεν έχει επιβεβαιωθεί οριστικά", "Ότι συμβαίνει μόνο σε μουσικούς", "Ότι είναι επικίνδυνη"], 1, "καμία δεν έχει ακόμα επιβεβαιωθεί οριστικά"),
 ],
 "gloss": {"ανατριχίλα": "ανατριχίλα — goosebumps, shiver", "εξογκώματα": "εξόγκωμα — bump, swelling", "ορθώνεται": "ορθώνομαι — to stand upright", "τρίχωμα": "τρίχωμα — fur, body hair", "κατάλοιπο": "κατάλοιπο — remnant, leftover", "αινιγματική": "αινιγματικός — puzzling, enigmatic"},
})

rnd = random.Random(195)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-195.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
