# Source for library/listening/listening-200.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l200.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l200-ann-psychosavvato", "title": "Ψυχοσάββατο: έκτακτα μέτρα στο κοιμητήριο", "title_en": "All Souls' Saturday: special arrangements at the cemetery", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο ραδιόφωνο της πόλης.",
 "script": [
  L("Εκφωνητής", "m", "Ο δήμος ενημερώνει ότι, επειδή το Σάββατο είναι Ψυχοσάββατο, το δημοτικό κοιμητήριο θα είναι ανοιχτό από τις έξι το πρωί ως τις οχτώ το βράδυ, δύο ώρες περισσότερο από το συνηθισμένο. Πέρσι, την ίδια μέρα, ο χώρος γέμισε τόσο πολύ, που σχηματίστηκαν ουρές στην είσοδο.", "The municipality announces that, because Saturday is All Souls' Saturday, the municipal cemetery will be open from six in the morning until eight in the evening, two hours longer than usual. Last year, on the same day, the grounds filled up so much that queues formed at the entrance."),
  L("Εκφωνητής", "m", "Ο χώρος στάθμευσης μπροστά στην κεντρική πύλη θα είναι κλειστός, για να διευκολυνθεί η κίνηση των πεζών. Από την πλατεία θα ξεκινά κάθε δεκαπέντε λεπτά δωρεάν λεωφορείο, ενώ για άτομα με κινητικά προβλήματα θα υπάρχει ηλεκτρικό αυτοκινητάκι μέσα στο κοιμητήριο.", "The car park in front of the main gate will be closed to make it easier for pedestrians to get around. A free bus will leave from the square every fifteen minutes, and for people with mobility problems there will be a small electric vehicle inside the cemetery."),
  L("Εκφωνητής", "m", "Παρακαλούμε τους επισκέπτες να μην αφήνουν αναμμένα κεριά χωρίς προστασία, λόγω του ανέμου, και να ρίχνουν τα κόλλυβα και τα χαρτιά στους ειδικούς κάδους.", "We ask visitors not to leave lit candles unprotected, because of the wind, and to put kollyva and paper in the special bins."),
 ],
 "questions": [
  Q("Πόσο περισσότερο από το συνηθισμένο θα είναι ανοιχτό το κοιμητήριο;", ["Μία ώρα", "Δύο ώρες", "Όλη τη νύχτα", "Μισή ώρα"], 1, "δύο ώρες περισσότερο από το συνηθισμένο"),
  Q("Γιατί θα είναι κλειστός ο χώρος στάθμευσης;", ["Για επισκευές", "Για να διευκολυνθεί η κίνηση των πεζών", "Γιατί είναι μικρός", "Για μια τελετή"], 1, "για να διευκολυνθεί η κίνηση των πεζών"),
  Q("Τι ζητείται για τα κεριά;", ["Να μην ανάβονται καθόλου", "Να αγοράζονται στην είσοδο", "Να μη μένουν αναμμένα χωρίς προστασία", "Να σβήνουν πριν από τις οχτώ"], 2, "να μην αφήνουν αναμμένα κεριά χωρίς προστασία"),
 ],
 "gloss": {"Ψυχοσάββατο": "Ψυχοσάββατο — Saturday of the dead, when the departed are remembered", "κοιμητήριο": "κοιμητήριο — cemetery", "πύλη": "πύλη — gate", "κινητικά": "κινητικός — mobility (κινητικά προβλήματα)", "κόλλυβα": "κόλλυβα — boiled wheat offered in memory of the dead"},
})

ITEMS.append({
 "id": "l200-int-filotelistis", "title": "Ένας φιλοτελιστής", "title_en": "A stamp collector", "type": "interview", "level": "B2",
 "context_el": "Συνέντευξη με έναν συνταξιούχο που συλλέγει γραμματόσημα εδώ και πενήντα χρόνια.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς ξεκινήσατε;", "How did you start?"),
  L("Συλλέκτης", "m", "Ο θείος μου ήταν ναυτικός και έστελνε γράμματα από λιμάνια σε όλο τον κόσμο. Η μητέρα μου κρατούσε τους φακέλους σε ένα κουτί παπουτσιών. Στα δέκα μου το βρήκα, ξεκόλλησα τα γραμματόσημα με ατμό από την κατσαρόλα και έτσι άρχισαν όλα.", "My uncle was a sailor and sent letters from ports all over the world. My mother kept the envelopes in a shoebox. When I was ten I found it, steamed the stamps off over a saucepan, and that's how it all began."),
  L("Δημοσιογράφος", "f", "Ποιο είναι το πιο πολύτιμο κομμάτι της συλλογής σας;", "What is the most valuable piece in your collection?"),
  L("Συλλέκτης", "m", "Σε χρήματα, ένα γραμματόσημο από την πρώτη ελληνική σειρά, το 1861, με το κεφάλι του Ερμή. Για μένα όμως το πιο πολύτιμο είναι ένας φάκελος του θείου μου από τη Βομβάη, με μια γραμμή στο πίσω μέρος: «Πες στον μικρό να μην τα πετάξει».", "In money, a stamp from the first Greek series, 1861, with the head of Hermes. For me, though, the most valuable is an envelope from my uncle in Bombay, with a line on the back: 'Tell the little one not to throw them away.'"),
  L("Δημοσιογράφος", "f", "Έχει μέλλον η φιλοτελία, τώρα που δεν στέλνουμε γράμματα;", "Does stamp collecting have a future, now that we don't send letters?"),
  L("Συλλέκτης", "m", "Οι νέοι συλλέκτες είναι λιγότεροι, αυτό είναι αλήθεια. Αλλά κάθε φορά που πηγαίνω σε ένα σχολείο και δείχνω ένα γραμματόσημο από μια χώρα που δεν υπάρχει πια, κάποιο παιδί ρωτάει «πού είναι αυτό;». Από εκεί ξεκινά η περιέργεια.", "There are fewer young collectors, that's true. But every time I go to a school and show a stamp from a country that no longer exists, some child asks 'where is that?'. That's where curiosity begins."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η συλλογή του;", ["Του χάρισε ένα άλμπουμ ο παππούς του", "Βρήκε τους φακέλους που έστελνε ο θείος του", "Δούλευε στο ταχυδρομείο", "Αγόρασε γραμματόσημα σε μια έκθεση"], 1, "Η μητέρα μου κρατούσε τους φακέλους σε ένα κουτί παπουτσιών"),
  Q("Ποιο κομμάτι θεωρεί το πιο πολύτιμο για τον ίδιο;", ["Το γραμματόσημο του 1861", "Ένα γραμματόσημο από χώρα που δεν υπάρχει", "Έναν φάκελο του θείου του με ένα μήνυμα στο πίσω μέρος", "Το πρώτο του άλμπουμ"], 2, "Για μένα όμως το πιο πολύτιμο είναι ένας φάκελος του θείου μου"),
  Q("Τι κάνει τα παιδιά περίεργα, κατά τον ίδιο;", ["Η αξία των γραμματοσήμων", "Τα χρώματα", "Τα γραμματόσημα από χώρες που δεν υπάρχουν πια", "Οι φωτογραφίες ζώων"], 2, "δείχνω ένα γραμματόσημο από μια χώρα που δεν υπάρχει πια"),
 ],
 "gloss": {"γραμματόσημα": "γραμματόσημο — postage stamp", "ξεκόλλησα": "ξεκολλάω — to unstick, peel off", "ατμό": "ατμός — steam", "φιλοτελία": "φιλοτελία — stamp collecting, philately", "περιέργεια": "περιέργεια — curiosity"},
})

ITEMS.append({
 "id": "l200-vm-mouseio-dorea", "title": "Μήνυμα από το λαογραφικό μουσείο για μια δωρεά", "title_en": "A message from the folk museum about a donation", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από την υπεύθυνη ενός λαογραφικού μουσείου.",
 "script": [
  L("Υπεύθυνη μουσείου", "f", "Καλημέρα σας, κυρία Σταυροπούλου, σας τηλεφωνώ από το Λαογραφικό Μουσείο. Θέλαμε να σας ευχαριστήσουμε για τον αργαλειό της γιαγιάς σας. Τον εξέτασε η συντηρήτριά μας και είναι σε πολύ καλή κατάσταση, παρά την ηλικία του.", "Good morning, Mrs Stavropoulou, I'm calling from the Folk Museum. We wanted to thank you for your grandmother's loom. Our conservator has examined it and it is in very good condition, despite its age."),
  L("Υπεύθυνη μουσείου", "f", "Για να τον εκθέσουμε, θα χρειαζόμασταν και λίγες πληροφορίες: από ποιο χωριό είναι, πότε περίπου φτιάχτηκε και αν υπάρχουν φωτογραφίες της γιαγιάς σας να υφαίνει. Αν έχετε και κάποιο υφαντό που έφτιαξε η ίδια, θα ήταν υπέροχο να το δείξουμε δίπλα στον αργαλειό, ακόμα και ως δάνειο.", "To exhibit it, we would also need some information: which village it comes from, roughly when it was made, and whether there are photographs of your grandmother weaving. If you also have a piece she wove herself, it would be wonderful to show it next to the loom, even as a loan."),
  L("Υπεύθυνη μουσείου", "f", "Τα εγκαίνια της νέας αίθουσας θα γίνουν στις είκοσι Μαρτίου, και θα θέλαμε πολύ να είστε εκεί. Πάρτε με όποτε μπορείτε, στο εσωτερικό τέσσερα.", "The opening of the new room will be on the twentieth of March, and we would very much like you to be there. Call me whenever you can, on extension four."),
 ],
 "questions": [
  Q("Τι δώρισε η κυρία Σταυροπούλου στο μουσείο;", ["Μια φορεσιά", "Τον αργαλειό της γιαγιάς της", "Ένα υφαντό", "Φωτογραφίες του χωριού"], 1, "για τον αργαλειό της γιαγιάς σας"),
  Q("Τι θα ήθελε να δείξει το μουσείο δίπλα στον αργαλειό;", ["Ένα υφαντό της γιαγιάς, έστω και ως δάνειο", "Ένα βίντεο", "Τα εργαλεία της συντηρήτριας", "Έναν χάρτη του χωριού"], 0, "θα ήταν υπέροχο να το δείξουμε δίπλα στον αργαλειό, ακόμα και ως δάνειο"),
  Q("Τι θα γίνει στις είκοσι Μαρτίου;", ["Θα κλείσει το μουσείο", "Θα παραληφθεί ο αργαλειός", "Τα εγκαίνια μιας νέας αίθουσας", "Μια συνάντηση με τη συντηρήτρια"], 2, "Τα εγκαίνια της νέας αίθουσας θα γίνουν στις είκοσι Μαρτίου"),
 ],
 "gloss": {"αργαλειό": "αργαλειός — loom", "συντηρήτριά": "συντηρήτρια — (female) conservator", "υφαίνει": "υφαίνω — to weave", "υφαντό": "υφαντό — woven piece", "εγκαίνια": "εγκαίνια — opening, inauguration"},
})

ITEMS.append({
 "id": "l200-mono-tsambouna", "title": "Τσαμπούνα στα σαράντα", "title_en": "Learning the island bagpipe at forty", "type": "monologue", "level": "B2",
 "context_el": "Μια λογίστρια από τη Νάξο μιλάει σε μια ραδιοφωνική εκπομπή για ένα όργανο που άρχισε να μαθαίνει.",
 "script": [
  L("Λογίστρια", "f", "Η τσαμπούνα είναι το όργανο των παππούδων μου. Φτιάχνεται από δέρμα κατσίκας και έναν ξύλινο αυλό με τρύπες. Όταν ήμουν παιδί, την άκουγα σε κάθε πανηγύρι, αλλά ποτέ δεν φανταζόμουν ότι θα την έπαιζα εγώ. Θεωρούνταν όργανο για άντρες, και μάλιστα για βοσκούς.", "The tsambouna is my grandparents' instrument. It is made from goatskin and a wooden pipe with holes. As a child I heard it at every village festival, but I never imagined I would play it myself. It was considered an instrument for men, and shepherds at that."),
  L("Λογίστρια", "f", "Στα σαράντα μου, μετά από μια δύσκολη χρονιά, βρήκα έναν ηλικιωμένο οργανοπαίχτη που δέχτηκε να μου κάνει μάθημα. Τους πρώτους δύο μήνες δεν έβγαζα ούτε μία νότα. Το δύσκολο δεν είναι τα δάχτυλα, είναι η ανάσα: πρέπει να φουσκώνεις το ασκί και ταυτόχρονα να το πιέζεις με τον αγκώνα, για να μη σταματήσει ο ήχος.", "At forty, after a difficult year, I found an elderly folk musician who agreed to teach me. For the first two months I couldn't get a single note out. The hard part isn't the fingers, it's the breath: you have to fill the bag and at the same time squeeze it with your elbow so the sound doesn't stop."),
  L("Λογίστρια", "f", "Πέρσι το καλοκαίρι έπαιξα για πρώτη φορά σε πανηγύρι, δίπλα στον δάσκαλό μου. Μια γιαγιά ήρθε μετά και μου είπε: «Παιδί μου, σε άκουσα και θυμήθηκα τον άντρα μου». Δεν ξέρω αν ήταν κομπλιμέντο, αλλά έκλαψα όλο το βράδυ.", "Last summer I played at a festival for the first time, next to my teacher. An old woman came up afterwards and said to me: 'My child, I heard you and remembered my husband.' I don't know if it was a compliment, but I cried all evening."),
 ],
 "questions": [
  Q("Γιατί δεν φανταζόταν ότι θα έπαιζε τσαμπούνα;", ["Γιατί δεν της άρεσε ο ήχος", "Γιατί θεωρούνταν όργανο για άντρες και βοσκούς", "Γιατί ήταν πολύ ακριβή", "Γιατί δεν υπήρχαν δάσκαλοι"], 1, "Θεωρούνταν όργανο για άντρες, και μάλιστα για βοσκούς"),
  Q("Τι είναι το πιο δύσκολο στην τσαμπούνα, κατά την ίδια;", ["Τα δάχτυλα", "Η ανάσα και η πίεση του ασκιού", "Να μάθει τα τραγούδια", "Να κουρδίσει το όργανο"], 1, "Το δύσκολο δεν είναι τα δάχτυλα, είναι η ανάσα"),
  Q("Πώς αντέδρασε στα λόγια της γιαγιάς στο πανηγύρι;", ["Γέλασε", "Της ζήτησε συγγνώμη", "Έκλαψε όλο το βράδυ", "Σταμάτησε να παίζει"], 2, "έκλαψα όλο το βράδυ"),
 ],
 "gloss": {"τσαμπούνα": "τσαμπούνα — island bagpipe", "αυλό": "αυλός — pipe", "οργανοπαίχτη": "οργανοπαίχτης — folk musician", "ασκί": "ασκί — skin bag", "αγκώνα": "αγκώνας — elbow"},
})

ITEMS.append({
 "id": "l200-dia-dentro-christougennon", "title": "Αληθινό ή ψεύτικο δέντρο;", "title_en": "A real or an artificial Christmas tree?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι συζητά τι χριστουγεννιάτικο δέντρο θα πάρει φέτος.",
 "script": [
  L("Μαρίνα", "f", "Φέτος θέλω αληθινό έλατο. Μου λείπει η μυρωδιά. Το πλαστικό μας έχει χάσει τα μισά του κλαδιά, και κάθε χρόνο βρίσκουμε πράσινα πλαστικά βελονάκια μέχρι το Πάσχα.", "This year I want a real fir tree. I miss the smell. Our plastic one has lost half its branches, and every year we find little green plastic needles until Easter."),
  L("Στέλιος", "m", "Και τι θα κάνουμε το αληθινό μετά τα Φώτα; Θα το πετάξουμε; Μου φαίνεται κρίμα να κόβουμε ένα δέντρο για τρεις εβδομάδες.", "And what will we do with the real one after Epiphany? Throw it away? It seems a pity to me to cut down a tree for three weeks."),
  L("Μαρίνα", "f", "Τα έλατα που πουλάνε στις λαϊκές τα καλλιεργούν σε φυτώρια, δεν τα κόβουν από το δάσος. Και ο δήμος τα μαζεύει μετά και τα κάνει κομπόστ για τα πάρκα.", "The firs they sell at the street markets are grown in nurseries; they aren't cut from the forest. And the municipality collects them afterwards and turns them into compost for the parks."),
  L("Στέλιος", "m", "Εντάξει, αλλά το διαμέρισμα είναι ζεστό. Θα ξεραθεί σε δέκα μέρες. Τι λες για ένα έλατο σε γλάστρα; Το βάζουμε στο μπαλκόνι μετά τις γιορτές και το ξαναβάζουμε μέσα του χρόνου.", "All right, but the flat is warm. It'll dry out in ten days. What about a fir in a pot? We put it on the balcony after the holidays and bring it back in next year."),
  L("Μαρίνα", "f", "Αν επιζήσει στο μπαλκόνι μας, που δεν επιζεί ούτε ο βασιλικός… Καλά, ας δοκιμάσουμε. Αλλά αν ξεραθεί, του χρόνου διαλέγω εγώ.", "If it survives on our balcony, where not even the basil survives… Fine, let's try. But if it dries out, next year I choose."),
 ],
 "questions": [
  Q("Γιατί θέλει η Μαρίνα αληθινό δέντρο;", ["Γιατί είναι φθηνότερο", "Γιατί της λείπει η μυρωδιά", "Γιατί το θέλουν τα παιδιά", "Γιατί είναι μεγαλύτερο"], 1, "Μου λείπει η μυρωδιά"),
  Q("Τι κάνει ο δήμος με τα δέντρα μετά τις γιορτές, κατά τη Μαρίνα;", ["Τα πουλάει ξανά", "Τα φυτεύει στο δάσος", "Τα καίει", "Τα κάνει κομπόστ για τα πάρκα"], 3, "τα κάνει κομπόστ για τα πάρκα"),
  Q("Τι αποφασίζουν τελικά;", ["Να κρατήσουν το πλαστικό", "Να δοκιμάσουν ένα έλατο σε γλάστρα", "Να μην πάρουν δέντρο", "Να αγοράσουν δύο δέντρα"], 1, "Καλά, ας δοκιμάσουμε"),
 ],
 "gloss": {"έλατο": "έλατο — fir tree", "βελονάκια": "βελονάκι — little needle", "Φώτα": "Φώτα — Epiphany (6 January)", "φυτώρια": "φυτώριο — plant nursery", "επιζήσει": "επιζώ — to survive"},
})

ITEMS.append({
 "id": "l200-rep-koino-aftokinito", "title": "Ένα αυτοκίνητο για όλο το χωριό", "title_en": "One car shared by the whole village", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από ένα ορεινό χωριό της Αρκαδίας.",
 "script": [
  L("Ρεπόρτερ", "f", "Στο χωριό μένουν όλο τον χρόνο περίπου εξήντα άνθρωποι, οι περισσότεροι πάνω από εβδομήντα. Το λεωφορείο για την πόλη περνά δύο φορές την εβδομάδα. Πέρσι ο πολιτιστικός σύλλογος αγόρασε, με δωρεές από ξενιτεμένους, ένα μικρό ηλεκτρικό αυτοκίνητο που το μοιράζονται όλοι.", "About sixty people live in the village all year round, most of them over seventy. The bus to town comes twice a week. Last year the cultural association bought, with donations from emigrants, a small electric car that everyone shares."),
  L("Ρεπόρτερ", "f", "Το σύστημα είναι απλό: στο καφενείο υπάρχει ένα τετράδιο, όπου γράφει κανείς τη μέρα και την ώρα που χρειάζεται το αυτοκίνητο. Όσοι δεν οδηγούν σημειώνουν ότι χρειάζονται οδηγό, και κάποιος από τους εθελοντές, συνήθως ο νεότερος, ο εξηντάχρονος πρόεδρος, τους πηγαίνει στον γιατρό ή στην τράπεζα.", "The system is simple: in the café there is a notebook where you write the day and time you need the car. Those who don't drive note that they need a driver, and one of the volunteers, usually the youngest, the sixty-year-old president, takes them to the doctor or the bank."),
  L("Ρεπόρτερ", "f", "Το αυτοκίνητο φορτίζει με ηλιακά πάνελ στη στέγη του παλιού σχολείου. Οι χρήστες αφήνουν σε ένα κουτί όσα χρήματα θέλουν για τη συντήρηση. Μια κάτοικος μάς είπε ότι το μεγαλύτερο κέρδος δεν είναι οι διαδρομές: «Τώρα πηγαίνουμε μαζί στην πόλη και πίνουμε και έναν καφέ».", "The car charges from solar panels on the roof of the old school. Users leave in a box as much money as they like for maintenance. One resident told us that the biggest gain isn't the trips: 'Now we go to town together and have a coffee too.'"),
 ],
 "questions": [
  Q("Πώς αγοράστηκε το αυτοκίνητο;", ["Από τον δήμο", "Με δωρεές από ξενιτεμένους", "Με δάνειο", "Από μια εταιρεία"], 1, "με δωρεές από ξενιτεμένους"),
  Q("Πώς κλείνει κανείς το αυτοκίνητο;", ["Με μια εφαρμογή", "Τηλεφωνώντας στον πρόεδρο", "Γράφοντας σε ένα τετράδιο στο καφενείο", "Στο δημαρχείο"], 2, "στο καφενείο υπάρχει ένα τετράδιο"),
  Q("Ποιο είναι το μεγαλύτερο κέρδος, κατά μια κάτοικο;", ["Ότι γλιτώνουν χρήματα", "Ότι πηγαίνουν μαζί στην πόλη και πίνουν καφέ", "Ότι δεν περιμένουν το λεωφορείο", "Ότι το αυτοκίνητο είναι οικολογικό"], 1, "Τώρα πηγαίνουμε μαζί στην πόλη και πίνουμε και έναν καφέ"),
 ],
 "gloss": {"σύλλογος": "σύλλογος — association, club", "ξενιτεμένους": "ξενιτεμένος — emigrant (living abroad)", "τετράδιο": "τετράδιο — notebook", "φορτίζει": "φορτίζω — to charge (a battery)", "συντήρηση": "συντήρηση — maintenance"},
})

ITEMS.append({
 "id": "l200-rep-paradosiaka-paichnidia", "title": "Οι παππούδες μαθαίνουν στα παιδιά παλιά παιχνίδια", "title_en": "Grandparents teach children the games of the past", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από ένα δημοτικό σχολείο στη Λάρισα.",
 "script": [
  L("Ρεπόρτερ", "m", "Κάθε Παρασκευή, στο μεγάλο διάλειμμα, η αυλή του σχολείου γεμίζει παππούδες και γιαγιάδες. Δεν έρχονται να πάρουν τα εγγόνια τους, αλλά να τους μάθουν τα παιχνίδια που έπαιζαν οι ίδιοι: κουτσό, τυφλόμυγα, μήλα, σκοινάκι.", "Every Friday, during the long break, the schoolyard fills with grandfathers and grandmothers. They don't come to pick up their grandchildren, but to teach them the games they themselves played: hopscotch, blind man's buff, dodgeball, skipping rope."),
  L("Ρεπόρτερ", "m", "Η ιδέα ήταν μιας δασκάλας της πέμπτης τάξης, που παρατήρησε ότι στα διαλείμματα πολλά παιδιά στέκονταν σε μια γωνία χωρίς να ξέρουν τι να κάνουν. «Δεν τους λείπουν τα παιχνίδια», μας είπε, «τους λείπουν οι κανόνες. Κανείς δεν τους έμαθε ποτέ κανόνες».", "The idea came from a fifth-grade teacher who noticed that during breaks many children stood in a corner not knowing what to do. 'It's not games they lack,' she told us, 'it's rules. Nobody ever taught them.'"),
  L("Ρεπόρτερ", "m", "Οι παππούδες δεν συμφωνούν πάντα μεταξύ τους. Ο κύριος Βαγγέλης, από ένα χωριό του Ολύμπου, επιμένει ότι στο κουτσό η πέτρα πρέπει να είναι πλακουτσωτή, ενώ η κυρία Ρούλα, από τον Βόλο, λέει ότι αρκεί ένα καπάκι από μπουκάλι. Τα παιδιά, πάντως, έχουν ήδη επινοήσει τη δική τους εκδοχή: με ένα σβηστήρι.", "The grandparents don't always agree with each other. Mr Vangelis, from a village on Olympus, insists that in hopscotch the stone must be flat, while Mrs Roula, from Volos, says a bottle cap is enough. The children, anyway, have already invented their own version: with an eraser."),
 ],
 "questions": [
  Q("Πότε έρχονται οι παππούδες στο σχολείο;", ["Κάθε πρωί", "Κάθε Παρασκευή στο μεγάλο διάλειμμα", "Στο τέλος της χρονιάς", "Μία φορά τον μήνα"], 1, "Κάθε Παρασκευή, στο μεγάλο διάλειμμα"),
  Q("Τι λείπει στα παιδιά, κατά τη δασκάλα;", ["Τα παιχνίδια", "Ο χώρος", "Οι κανόνες", "Ο χρόνος"], 2, "τους λείπουν οι κανόνες"),
  Q("Με τι παίζουν τα παιδιά το κουτσό στη δική τους εκδοχή;", ["Με ένα σβηστήρι", "Με ένα καπάκι", "Με μια πλακουτσωτή πέτρα", "Με ένα κέρμα"], 0, "με ένα σβηστήρι"),
 ],
 "gloss": {"κουτσό": "κουτσό — hopscotch", "τυφλόμυγα": "τυφλόμυγα — blind man's buff", "πλακουτσωτή": "πλακουτσωτός — flat", "επινοήσει": "επινοώ — to invent", "σβηστήρι": "σβηστήρι — eraser"},
})

ITEMS.append({
 "id": "l200-news-portofoli-meta-apo-20-chronia", "title": "Πορτοφόλι βρέθηκε μέσα σε τοίχο μετά από είκοσι χρόνια", "title_en": "A wallet found inside a wall after twenty years", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση σε ένα τοπικό δελτίο ειδήσεων.",
 "script": [
  L("Παρουσιάστρια", "f", "Ένα πορτοφόλι που είχε χαθεί πριν από είκοσι χρόνια επέστρεψε χθες στον ιδιοκτήτη του, στην Πάτρα. Το βρήκαν εργάτες που ανακαίνιζαν ένα παλιό κτίριο, όταν γκρέμισαν έναν ψεύτικο τοίχο πίσω από το ταμείο ενός πρώην σινεμά.", "A wallet lost twenty years ago was returned yesterday to its owner in Patras. It was found by workers renovating an old building, when they knocked down a false wall behind the ticket office of a former cinema."),
  L("Παρουσιάστρια", "f", "Μέσα υπήρχαν μια ταυτότητα, δύο εισιτήρια για μια ταινία του 2004 και χαρτονομίσματα που σήμερα έχουν μόνο συλλεκτική αξία. Οι εργάτες το παρέδωσαν στο αστυνομικό τμήμα, και οι αστυνομικοί βρήκαν τον ιδιοκτήτη μέσω της ταυτότητας.", "Inside were an identity card, two tickets for a 2004 film and banknotes that today have only collector's value. The workers handed it in to the police station, and the police traced the owner through the identity card."),
  L("Παρουσιάστρια", "f", "Ο ιδιοκτήτης, σήμερα πενήντα πέντε ετών, είπε ότι θυμάται καλά εκείνο το βράδυ: ήταν το πρώτο του ραντεβού με τη γυναίκα του. «Της είχα πει ότι κερνάω εγώ», δήλωσε γελώντας, «και τελικά πλήρωσε εκείνη. Είκοσι χρόνια μετά, μπορώ επιτέλους να της αποδείξω ότι δεν είπα ψέματα».", "The owner, now fifty-five, said he remembers that evening well: it was his first date with his wife. 'I had told her it was my treat,' he said, laughing, 'and in the end she paid. Twenty years later, I can finally prove to her that I didn't lie.'"),
 ],
 "questions": [
  Q("Πού βρέθηκε το πορτοφόλι;", ["Σε ένα ταξί", "Πίσω από έναν ψεύτικο τοίχο σε ένα πρώην σινεμά", "Σε ένα πάρκο", "Σε μια τράπεζα"], 1, "όταν γκρέμισαν έναν ψεύτικο τοίχο πίσω από το ταμείο ενός πρώην σινεμά"),
  Q("Πώς βρέθηκε ο ιδιοκτήτης;", ["Μέσω της ταυτότητας", "Από τα εισιτήρια", "Μέσω μιας ανάρτησης στο διαδίκτυο", "Ήρθε ο ίδιος στο κτίριο"], 0, "οι αστυνομικοί βρήκαν τον ιδιοκτήτη μέσω της ταυτότητας"),
  Q("Τι μπορεί τώρα να αποδείξει ο ιδιοκτήτης στη γυναίκα του;", ["Ότι είχε αγοράσει εισιτήρια", "Ότι δεν είπε ψέματα ότι θα κερνούσε", "Ότι ήξερε την ταινία", "Ότι είχε πολλά χρήματα"], 1, "μπορώ επιτέλους να της αποδείξω ότι δεν είπα ψέματα"),
 ],
 "gloss": {"ανακαίνιζαν": "ανακαινίζω — to renovate", "γκρέμισαν": "γκρεμίζω — to knock down", "ταμείο": "ταμείο — ticket office, till", "χαρτονομίσματα": "χαρτονόμισμα — banknote", "κερνάω": "κερνάω — to treat (someone to something)"},
})

ITEMS.append({
 "id": "l200-c1-mono-symmetria", "title": "Γιατί μας αρέσει η συμμετρία;", "title_en": "Why do we like symmetry?", "type": "monologue", "level": "C1",
 "context_el": "Μια ψυχολόγος μιλάει σε μια σειρά διαλέξεων για την αισθητική.",
 "script": [
  L("Ψυχολόγος", "f", "Από τις πεταλούδες ως τον Παρθενώνα, η συμμετρία φαίνεται να μας γοητεύει σχεδόν παντού. Μια συνηθισμένη εξήγηση είναι η λεγόμενη «ευχέρεια επεξεργασίας»: ο εγκέφαλος αναγνωρίζει ένα συμμετρικό σχήμα πιο γρήγορα, γιατί αρκεί να επεξεργαστεί το μισό, και αυτή η ευκολία βιώνεται ως ευχαρίστηση.", "From butterflies to the Parthenon, symmetry seems to fascinate us almost everywhere. A common explanation is so-called 'processing fluency': the brain recognises a symmetrical shape faster, because it is enough to process half of it, and this ease is experienced as pleasure."),
  L("Ψυχολόγος", "f", "Για τα πρόσωπα έχει προταθεί και μια εξελικτική ερμηνεία: η συμμετρία θα μπορούσε να είναι ένδειξη καλής υγείας κατά την ανάπτυξη. Οφείλω όμως να πω ότι τα ερευνητικά δεδομένα εδώ είναι αντιφατικά, και η σχέση συμμετρίας και υγείας κάθε άλλο παρά αποδεδειγμένη θεωρείται.", "For faces an evolutionary interpretation has also been proposed: symmetry could be a sign of good health during development. I must say, however, that the research data here are contradictory, and the link between symmetry and health is considered anything but proven."),
  L("Ψυχολόγος", "f", "Και κάτι που ξαφνιάζει πάντα το ακροατήριο: αν φτιάξετε ψηφιακά ένα πρόσωπο απόλυτα συμμετρικό, ενώνοντας δύο φορές τη μία πλευρά του, το αποτέλεσμα συνήθως μας φαίνεται παράξενο, σχεδόν ψυχρό. Μας αρέσει, φαίνεται, η σχεδόν τέλεια συμμετρία, όχι η τέλεια. Ίσως γιατί η ζωή, όπως και η ομορφιά, βρίσκεται στις μικρές αποκλίσεις.", "And something that always surprises the audience: if you digitally create a perfectly symmetrical face by joining one side of it twice, the result usually looks strange to us, almost cold. We like, it seems, almost-perfect symmetry, not perfect symmetry. Perhaps because life, like beauty, lies in small deviations."),
 ],
 "questions": [
  Q("Τι υποστηρίζει η εξήγηση της «ευχέρειας επεξεργασίας»;", ["Ότι η συμμετρία είναι σημάδι υγείας", "Ότι ο εγκέφαλος αναγνωρίζει πιο γρήγορα τα συμμετρικά σχήματα και αυτό του προκαλεί ευχαρίστηση", "Ότι μαθαίνουμε να αγαπάμε τη συμμετρία στο σχολείο", "Ότι η συμμετρία είναι πιο σπάνια στη φύση"], 1, "ο εγκέφαλος αναγνωρίζει ένα συμμετρικό σχήμα πιο γρήγορα"),
  Q("Πώς κρίνει η ψυχολόγος την εξελικτική ερμηνεία για τα πρόσωπα;", ["Τη θεωρεί αποδεδειγμένη", "Λέει ότι τα δεδομένα είναι αντιφατικά", "Την απορρίπτει εντελώς", "Λέει ότι ισχύει μόνο για τα ζώα"], 1, "τα ερευνητικά δεδομένα εδώ είναι αντιφατικά"),
  Q("Πώς μας φαίνεται συνήθως ένα απόλυτα συμμετρικό πρόσωπο;", ["Πιο όμορφο", "Πιο νεανικό", "Παράξενο, σχεδόν ψυχρό", "Πιο οικείο"], 2, "το αποτέλεσμα συνήθως μας φαίνεται παράξενο, σχεδόν ψυχρό"),
  Q("Ποιο είναι το συμπέρασμά της;", ["Μας αρέσει η σχεδόν τέλεια συμμετρία, όχι η τέλεια", "Η συμμετρία δεν παίζει κανέναν ρόλο", "Μόνο η τέλεια συμμετρία είναι όμορφη", "Οι αρχαίοι Έλληνες δεν αγαπούσαν τη συμμετρία"], 0, "Μας αρέσει, φαίνεται, η σχεδόν τέλεια συμμετρία, όχι η τέλεια"),
 ],
 "gloss": {"γοητεύει": "γοητεύω — to fascinate", "ευχέρεια": "ευχέρεια — ease, fluency", "εξελικτική": "εξελικτικός — evolutionary", "αντιφατικά": "αντιφατικός — contradictory", "αποκλίσεις": "απόκλιση — deviation"},
})

ITEMS.append({
 "id": "l200-c1-int-tragoudi-sto-myalo", "title": "Γιατί κάποια τραγούδια «κολλάνε» στο μυαλό μας;", "title_en": "Why do some songs get stuck in our heads?", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με έναν ερευνητή της μουσικής γνωστικής επιστήμης σε μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "f", "Όλοι το έχουμε ζήσει: ένα τραγουδάκι από μια διαφήμιση παίζει στο μυαλό μας όλη μέρα. Πόσο συχνό είναι αυτό;", "We've all experienced it: a little tune from an advertisement plays in our head all day. How common is that?"),
  L("Ερευνητής", "m", "Εξαιρετικά συχνό. Σε έρευνες, η μεγάλη πλειονότητα των ανθρώπων δηλώνει ότι το παθαίνει τουλάχιστον μία φορά την εβδομάδα. Συνήθως δεν «κολλάει» ολόκληρο το τραγούδι, αλλά ένα μικρό κομμάτι του, συχνά το ρεφρέν, που επαναλαμβάνεται ξανά και ξανά, σαν δίσκος που έχει γρατζουνιστεί.", "Extremely common. In surveys, the great majority of people say they experience it at least once a week. Usually it isn't the whole song that 'sticks', but a small piece of it, often the chorus, which repeats again and again, like a scratched record."),
  L("Δημοσιογράφος", "f", "Τι κοινό έχουν αυτά τα τραγούδια;", "What do these songs have in common?"),
  L("Ερευνητής", "m", "Είναι συνήθως γρήγορα, με απλή μελωδία, αλλά με κάποιο μικρό απρόβλεπτο στοιχείο, ένα ασυνήθιστο διάστημα ή έναν ρυθμό που ξαφνιάζει. Παίζει ρόλο επίσης το πόσο πρόσφατα και πόσο συχνά τα ακούσαμε. Και υπάρχει μια ενδιαφέρουσα υπόθεση: ότι ο εγκέφαλος επιστρέφει σε κάτι που έμεινε ανολοκλήρωτο, όπως ένα κομμάτι που διακόπηκε στη μέση.", "They are usually fast, with a simple melody, but with some small unpredictable element, an unusual interval or a rhythm that surprises. How recently and how often we heard them also plays a role. And there is an interesting hypothesis: that the brain returns to something that was left unfinished, like a piece interrupted in the middle."),
  L("Δημοσιογράφος", "f", "Υπάρχει τρόπος να το διώξουμε;", "Is there a way to get rid of it?"),
  L("Ερευνητής", "m", "Μια βρετανική μελέτη έδειξε ότι το μάσημα τσίχλας μειώνει κάπως τη συχνότητα, ίσως γιατί απασχολεί τους μυς που θα χρησιμοποιούσαμε για να το σιγοτραγουδήσουμε. Άλλοι προτείνουν να ακούσουμε το τραγούδι ολόκληρο, για να «κλείσει». Η δική μου συμβουλή είναι πιο απλή: μην προσπαθείτε να μην το σκέφτεστε. Όσο πιο πολύ το διώχνετε, τόσο πιο πεισματικά επιστρέφει.", "A British study showed that chewing gum somewhat reduces the frequency, perhaps because it occupies the muscles we would use to hum it under our breath. Others suggest listening to the whole song so that it 'closes'. My own advice is simpler: don't try not to think about it. The more you push it away, the more stubbornly it comes back."),
 ],
 "questions": [
  Q("Τι «κολλάει» συνήθως στο μυαλό μας;", ["Ολόκληρο το τραγούδι", "Ένα μικρό κομμάτι, συχνά το ρεφρέν", "Μόνο οι στίχοι", "Μόνο ο ρυθμός"], 1, "αλλά ένα μικρό κομμάτι του, συχνά το ρεφρέν"),
  Q("Ποιο χαρακτηριστικό έχουν συνήθως αυτά τα τραγούδια;", ["Είναι αργά και θλιμμένα", "Έχουν πολύπλοκη μελωδία", "Έχουν απλή μελωδία με κάποιο μικρό απρόβλεπτο στοιχείο", "Είναι πάντα παλιά"], 2, "με απλή μελωδία, αλλά με κάποιο μικρό απρόβλεπτο στοιχείο"),
  Q("Γιατί ίσως βοηθά η τσίχλα, σύμφωνα με τη μελέτη;", ["Γιατί αποσπά την προσοχή με τη γεύση της", "Γιατί απασχολεί τους μυς που θα χρησιμοποιούσαμε για να το σιγοτραγουδήσουμε", "Γιατί μας ηρεμεί", "Γιατί μας κάνει να μιλάμε"], 1, "ίσως γιατί απασχολεί τους μυς που θα χρησιμοποιούσαμε για να το σιγοτραγουδήσουμε"),
  Q("Ποια είναι η συμβουλή του ερευνητή;", ["Να ακούμε άλλο τραγούδι", "Να τραγουδάμε δυνατά", "Να μην προσπαθούμε να διώξουμε τη σκέψη", "Να κοιμόμαστε περισσότερο"], 2, "μην προσπαθείτε να μην το σκέφτεστε"),
 ],
 "gloss": {"πλειονότητα": "πλειονότητα — majority", "ρεφρέν": "ρεφρέν — chorus, refrain", "γρατζουνιστεί": "γρατζουνίζομαι — to get scratched", "απρόβλεπτο": "απρόβλεπτος — unpredictable", "σιγοτραγουδήσουμε": "σιγοτραγουδώ — to hum, sing softly", "πεισματικά": "πεισματικά — stubbornly"},
})

rnd = random.Random(200)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-200.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
