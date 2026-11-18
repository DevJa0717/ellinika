# Source for library/listening/listening-186.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l186.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l186-ann-anemoi-parka", "title": "Κλειστά τα πάρκα λόγω ισχυρών ανέμων", "title_en": "Parks closed because of strong winds", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο ραδιόφωνο ένα πρωί με έκτακτο δελτίο καιρού.",
 "script": [
  L("Εκφωνητής", "m", "Λόγω των θυελλωδών ανέμων που προβλέπονται από το μεσημέρι ως αύριο το πρωί, ο δήμος ανακοινώνει ότι τα πάρκα, οι παιδικές χαρές και τα δημοτικά νεκροταφεία θα μείνουν κλειστά από τις δώδεκα το μεσημέρι.", "Because of the gale-force winds forecast from midday until tomorrow morning, the municipality announces that parks, playgrounds and municipal cemeteries will be closed from twelve noon."),
  L("Εκφωνητής", "m", "Ο κίνδυνος από σπασμένα κλαδιά και δέντρα που μπορεί να ξεριζωθούν είναι μεγάλος, ιδιαίτερα στα πάρκα με ψηλά πεύκα. Οι υπαίθριες αθλητικές δραστηριότητες των σχολείων αναβάλλονται, ενώ η λαϊκή αγορά της Παρασκευής θα γίνει κανονικά, αλλά χωρίς τέντες.", "The danger from broken branches and trees that may be uprooted is high, especially in parks with tall pines. Outdoor school sports activities are postponed, while Friday's street market will go ahead as normal, but without awnings."),
  L("Εκφωνητής", "m", "Οι πολίτες παρακαλούνται να δέσουν ή να μαζέψουν από τα μπαλκόνια γλάστρες, ομπρέλες και ό,τι άλλο μπορεί να παρασυρθεί από τον αέρα, και να μη σταθμεύουν κάτω από δέντρα. Για πτώσεις κλαδιών μπορείτε να καλείτε όλο το εικοσιτετράωρο το τηλέφωνο της πολιτικής προστασίας του δήμου.", "Residents are asked to tie down or take in from their balconies pots, umbrellas and anything else the wind could carry off, and not to park under trees. For fallen branches you can call the municipality's civil protection line around the clock."),
 ],
 "questions": [
  Q("Από πότε θα είναι κλειστά τα πάρκα;", ["Από αύριο το πρωί", "Από τις δώδεκα το μεσημέρι", "Από το απόγευμα", "Από την Παρασκευή"], 1, "θα μείνουν κλειστά από τις δώδεκα το μεσημέρι"),
  Q("Τι θα γίνει με τη λαϊκή αγορά της Παρασκευής;", ["Θα ακυρωθεί", "Θα γίνει σε άλλο δρόμο", "Θα γίνει κανονικά, αλλά χωρίς τέντες", "Θα γίνει τη Δευτέρα"], 2, "η λαϊκή αγορά της Παρασκευής θα γίνει κανονικά, αλλά χωρίς τέντες"),
  Q("Τι ζητά ο δήμος από τους πολίτες;", ["Να μη βγαίνουν καθόλου από το σπίτι", "Να κόψουν τα κλαδιά των δέντρων τους", "Να καλούν την αστυνομία για κάθε πρόβλημα", "Να μαζέψουν από τα μπαλκόνια ό,τι μπορεί να παρασυρθεί"], 3, "να μαζέψουν από τα μπαλκόνια γλάστρες, ομπρέλες και ό,τι άλλο μπορεί να παρασυρθεί από τον αέρα"),
 ],
 "gloss": {"θυελλωδών": "θυελλώδης — gale-force, stormy", "ξεριζωθούν": "ξεριζώνομαι — to be uprooted", "υπαίθριες": "υπαίθριος — outdoor", "αναβάλλονται": "αναβάλλομαι — to be postponed", "τέντες": "τέντα — awning", "παρασυρθεί": "παρασύρομαι — to be carried away", "πολιτικής προστασίας": "πολιτική προστασία — civil protection"},
})

ITEMS.append({
 "id": "l186-int-psaras-achinon", "title": "Ο ψαράς των αχινών", "title_en": "The sea-urchin fisherman", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν ψαρά από ένα νησί του Αιγαίου που μαζεύει αχινούς.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς μαζεύετε τους αχινούς;", "How do you gather the sea urchins?"),
  L("Ψαράς", "m", "Με μάσκα, βατραχοπέδιλα και ένα μικρό μαχαίρι. Βουτάω σε βάθος τριών με πέντε μέτρων, εκεί που ο βυθός έχει βράχια, και τους ξεκολλάω από την πέτρα, τον καθένα χωριστά. Φοράω πάντα χοντρά γάντια, γιατί τα αγκάθια τους σπάνε μέσα στο δέρμα και πονάνε για μέρες.", "With a mask, flippers and a small knife. I dive to a depth of three to five metres, where the seabed is rocky, and prise them off the stone one at a time. I always wear thick gloves, because their spines break off in the skin and hurt for days."),
  L("Δημοσιογράφος", "f", "Τι ακριβώς τρώμε από τον αχινό;", "What exactly do we eat of the sea urchin?"),
  L("Ψαράς", "m", "Ο κόσμος λέει «τα αβγά», αλλά στην πραγματικότητα τρώμε τους γεννητικούς αδένες, και του αρσενικού και του θηλυκού. Είναι πέντε πορτοκαλί λωρίδες μέσα στο κέλυφος. Τους ανοίγω με ψαλίδι, τους πλένω στο θαλασσινό νερό και τους τρώμε με λίγο λεμόνι και ψωμί.", "People say 'the eggs', but in fact we eat the gonads, of both the male and the female. They are five orange strips inside the shell. I open them with scissors, rinse them in seawater and we eat them with a little lemon and bread."),
  L("Δημοσιογράφος", "f", "Υπάρχουν εποχές που δεν επιτρέπεται να τους μαζεύετε;", "Are there seasons when you are not allowed to gather them?"),
  L("Ψαράς", "m", "Ναι, την εποχή που αναπαράγονται, κάπου στα τέλη της άνοιξης, απαγορεύεται. Και καλά κάνουν. Όταν ήμουν παιδί, οι αχινοί ήταν παντού. Σήμερα, σε πολλά μέρη που μαζεύουν πολλοί, ψάχνεις πολλή ώρα για να βρεις μια χούφτα.", "Yes, in the season when they reproduce, somewhere at the end of spring, it is forbidden. And rightly so. When I was a child, sea urchins were everywhere. Today, in many places where lots of people gather them, you search for a long time to find a handful."),
 ],
 "questions": [
  Q("Γιατί φοράει πάντα χοντρά γάντια;", ["Γιατί το νερό είναι κρύο", "Γιατί τα αγκάθια σπάνε μέσα στο δέρμα και πονάνε", "Γιατί το ζητά ο νόμος", "Για να μη γλιστράει το μαχαίρι"], 1, "τα αγκάθια τους σπάνε μέσα στο δέρμα και πονάνε για μέρες"),
  Q("Τι λέει για το μέρος του αχινού που τρώμε;", ["Ότι είναι μόνο τα αβγά του θηλυκού", "Ότι τρώγεται μόνο μαγειρεμένο", "Ότι είναι οι γεννητικοί αδένες αρσενικού και θηλυκού", "Ότι είναι το κέλυφος"], 2, "τρώμε τους γεννητικούς αδένες, και του αρσενικού και του θηλυκού"),
  Q("Πώς βλέπει την απαγόρευση την εποχή της αναπαραγωγής;", ["Τη θεωρεί υπερβολική", "Λέει ότι δεν την τηρεί κανείς", "Λέει ότι ισχύει μόνο για τους τουρίστες", "Πιστεύει ότι είναι σωστή"], 3, "Και καλά κάνουν"),
 ],
 "gloss": {"αχινούς": "αχινός — sea urchin", "βατραχοπέδιλα": "βατραχοπέδιλο — flipper", "βυθός": "βυθός — seabed", "ξεκολλάω": "ξεκολλάω — to prise off, unstick", "γεννητικούς αδένες": "γεννητικός αδένας — gonad", "κέλυφος": "κέλυφος — shell", "αναπαράγονται": "αναπαράγομαι — to reproduce", "χούφτα": "χούφτα — handful"},
})

ITEMS.append({
 "id": "l186-rep-varkes-apo-chartoni", "title": "Αγώνας με βάρκες από χαρτόνι", "title_en": "A race of cardboard boats", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από έναν αγώνα στο λιμάνι μιας μικρής πόλης, όπου οι βάρκες είναι φτιαγμένες από χαρτόνι.",
 "script": [
  L("Ρεπόρτερ", "f", "Στο λιμάνι έχουν μαζευτεί εκατοντάδες θεατές. Στην αμμουδιά περιμένουν είκοσι δύο βάρκες, φτιαγμένες μόνο από χαρτόνι, κολλητική ταινία και αδιάβροχη μπογιά. Οι κανόνες είναι απλοί: απαγορεύονται το ξύλο, το πλαστικό και το φελιζόλ, και κάθε βάρκα πρέπει να κάνει μια διαδρομή διακοσίων μέτρων με δύο ανθρώπους μέσα.", "Hundreds of spectators have gathered at the harbour. On the beach, twenty-two boats are waiting, made only of cardboard, tape and waterproof paint. The rules are simple: wood, plastic and polystyrene are banned, and each boat must cover a two-hundred-metre course with two people in it."),
  L("Ρεπόρτερ", "f", "Η ομάδα ενός γυμνασίου έχει φτιάξει μια βάρκα σε σχήμα δελφινιού. «Δουλεύαμε τρεις εβδομάδες, μετά το σχολείο», λέει η Ιφιγένεια. «Το πιο δύσκολο ήταν ο πάτος. Βάλαμε τέσσερα στρώματα χαρτόνι, γιατί στη δοκιμή στην πισίνα η πρώτη μας βάρκα βούλιαξε σε δύο λεπτά».", "A secondary-school team has built a boat shaped like a dolphin. 'We worked for three weeks, after school,' says Ifigeneia. 'The hardest part was the bottom. We put in four layers of cardboard, because in the test in the pool our first boat sank in two minutes.'"),
  L("Ρεπόρτερ", "f", "Με το σφύριγμα της αφετηρίας, οι κωπηλάτες αρχίζουν να κωπηλατούν με όλη τους τη δύναμη. Πέντε βάρκες βουλιάζουν πριν από τη μέση της διαδρομής, μέσα στα γέλια και στα χειροκροτήματα. Νικήτρια βγαίνει μια ομάδα συνταξιούχων ψαράδων, αλλά το πιο αγαπημένο βραβείο, το βραβείο του «πιο εντυπωσιακού ναυαγίου», το παίρνει το δελφίνι των μαθητών.", "At the starting whistle, the rowers begin to paddle with all their strength. Five boats sink before the halfway point, amid laughter and applause. The winners are a team of retired fishermen, but the best-loved prize, the prize for the 'most spectacular shipwreck', goes to the pupils' dolphin."),
 ],
 "questions": [
  Q("Ποιο υλικό επιτρέπεται στις βάρκες;", ["Το ξύλο", "Η κολλητική ταινία", "Το φελιζόλ", "Το πλαστικό"], 1, "φτιαγμένες μόνο από χαρτόνι, κολλητική ταινία και αδιάβροχη μπογιά"),
  Q("Γιατί έβαλαν οι μαθητές τέσσερα στρώματα χαρτόνι στον πάτο;", ["Για να πάει η βάρκα πιο γρήγορα", "Για να μοιάζει με δελφίνι", "Γιατί η πρώτη τους βάρκα βούλιαξε στη δοκιμή", "Γιατί το ζητούσαν οι κανόνες"], 2, "στη δοκιμή στην πισίνα η πρώτη μας βάρκα βούλιαξε σε δύο λεπτά"),
  Q("Ποιο βραβείο κέρδισαν οι μαθητές;", ["Το πρώτο βραβείο", "Το βραβείο της πιο όμορφης βάρκας", "Το βραβείο της πιο γρήγορης ομάδας", "Το βραβείο του πιο εντυπωσιακού ναυαγίου"], 3, "το βραβείο του «πιο εντυπωσιακού ναυαγίου», το παίρνει το δελφίνι των μαθητών"),
 ],
 "gloss": {"κολλητική ταινία": "κολλητική ταινία — adhesive tape", "αδιάβροχη": "αδιάβροχος — waterproof", "φελιζόλ": "φελιζόλ — polystyrene", "βούλιαξε": "βουλιάζω — to sink", "αφετηρίας": "αφετηρία — start (of a race)", "κωπηλάτες": "κωπηλάτης — rower", "κωπηλατούν": "κωπηλατώ — to row, paddle", "ναυαγίου": "ναυάγιο — shipwreck"},
})

ITEMS.append({
 "id": "l186-vm-nona-vaftisi", "title": "Μήνυμα από τη νονά για τη βάφτιση", "title_en": "A message from the godmother about the christening", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα που άφησε στον τηλεφωνητή η μελλοντική νονά ενός μωρού στη μητέρα του.",
 "script": [
  L("Αλεξάνδρα", "f", "Γεια σου, Ρένα μου, η Αλεξάνδρα είμαι. Σε παίρνω για τη βάφτιση της μικρής. Πήγα σήμερα στο μαγαζί και διάλεξα τα βαφτιστικά ρούχα, ένα άσπρο φορεματάκι με κεντημένα λουλουδάκια, και παρήγγειλα και τη λαμπάδα. Τα λαδόπανα και το σταυρουδάκι τα έχω ήδη πάρει.", "Hi, Rena dear, it's Alexandra. I'm calling about the little one's christening. I went to the shop today and chose the christening clothes, a white little dress with embroidered flowers, and I also ordered the candle. I've already bought the oil cloths and the little cross."),
  L("Αλεξάνδρα", "f", "Θέλω να σε ρωτήσω δύο πράγματα. Πρώτον, πόσα μαρτυρικά να παραγγείλω; Ο παπάς είπε ότι η εκκλησία χωράει γύρω στα εκατό άτομα, αλλά δεν ξέρω πόσους έχετε καλέσει εσείς. Δεύτερον, πες μου αν είναι οριστικό το όνομα. Το ξέρω ότι το κανονικό είναι να το διαλέξει η νονά, αλλά δεν θέλω να σε στεναχωρήσω.", "I want to ask you two things. First, how many witness favours should I order? The priest said the church holds about a hundred people, but I don't know how many you have invited. Second, tell me whether the name is final. I know that traditionally the godmother chooses it, but I don't want to upset you."),
  L("Αλεξάνδρα", "f", "Πάρε με όποτε μπορείς, εγώ θα είμαι στο σπίτι όλο το απόγευμα. Και φίλα μου τη μικρή!", "Call me whenever you can, I'll be at home all afternoon. And give the little one a kiss from me!"),
 ],
 "questions": [
  Q("Τι έχει ήδη πάρει η Αλεξάνδρα;", ["Τα μαρτυρικά", "Τα λαδόπανα και το σταυρουδάκι", "Το φόρεμα της μητέρας", "Τα προσκλητήρια"], 1, "Τα λαδόπανα και το σταυρουδάκι τα έχω ήδη πάρει"),
  Q("Γιατί δεν ξέρει πόσα μαρτυρικά να παραγγείλει;", ["Γιατί ο παπάς δεν της απάντησε", "Γιατί το μαγαζί είναι κλειστό", "Γιατί δεν ξέρει πόσους καλεσμένους έχουν οι γονείς", "Γιατί δεν έχει αποφασίσει για την εκκλησία"], 2, "δεν ξέρω πόσους έχετε καλέσει εσείς"),
  Q("Τι λέει για το όνομα του μωρού;", ["Ότι το έχει ήδη διαλέξει", "Ότι θα το αποφασίσει ο παπάς", "Ότι δεν της αρέσει", "Ότι παραδοσιακά το διαλέγει η νονά, αλλά δεν θέλει να στεναχωρήσει τη μητέρα"], 3, "Το ξέρω ότι το κανονικό είναι να το διαλέξει η νονά, αλλά δεν θέλω να σε στεναχωρήσω"),
 ],
 "gloss": {"νονά": "νονά — godmother", "βάφτιση": "βάφτιση — christening", "βαφτιστικά": "βαφτιστικός — christening (adj.)", "κεντημένα": "κεντημένος — embroidered", "λαμπάδα": "λαμπάδα — large candle", "λαδόπανα": "λαδόπανα — white cloths used after the anointing", "σταυρουδάκι": "σταυρουδάκι — little cross", "μαρτυρικά": "μαρτυρικά — small favours given to christening guests"},
})

ITEMS.append({
 "id": "l186-mon-deka-daktyla", "title": "Έμαθα να γράφω με δέκα δάχτυλα στα εξήντα", "title_en": "I learned to touch-type at sixty", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια συνταξιούχο να μιλά σε μια ραδιοφωνική εκπομπή για κάτι που έμαθε πρόσφατα.",
 "script": [
  L("Ευανθία", "f", "Σε όλη μου τη ζωή έγραφα στον υπολογιστή με δύο δάχτυλα, κοιτάζοντας συνέχεια το πληκτρολόγιο. Όταν βγήκα στη σύνταξη, αποφάσισα να γράψω τις αναμνήσεις μου για τα εγγόνια μου, και κατάλαβα ότι με αυτόν τον ρυθμό θα χρειαζόμουν δέκα χρόνια.", "All my life I typed on the computer with two fingers, constantly looking at the keyboard. When I retired, I decided to write my memories down for my grandchildren, and I realised that at that pace I would need ten years."),
  L("Ευανθία", "f", "Βρήκα ένα δωρεάν πρόγραμμα στο διαδίκτυο για το τυφλό σύστημα. Το πρώτο μάθημα είναι μόνο η μεσαία σειρά: «α, σ, δ, φ» με το αριστερό χέρι και «ξ, κ, λ» με το δεξί. Στο Φ και στο Ξ υπάρχει ένα μικρό εξόγκωμα, για να βρίσκουν τα δάχτυλα τη θέση τους χωρίς να κοιτάζεις. Τις πρώτες εβδομάδες ήμουν πιο αργή από πριν και ήθελα να τα παρατήσω.", "I found a free online programme for touch-typing. The first lesson is just the middle row: 'a, s, d, f' with the left hand and 'j, k, l' with the right. On the F and the J there is a small bump, so that your fingers find their place without you looking. In the first weeks I was slower than before and wanted to give up."),
  L("Ευανθία", "f", "Έκανα όμως δεκαπέντε λεπτά κάθε πρωί, με τον καφέ μου, και μετά από τρεις μήνες έγραφα τριπλάσιες λέξεις το λεπτό. Το βιβλίο με τις αναμνήσεις έχει φτάσει ήδη τις ογδόντα σελίδες. Η εγγονή μου λέει ότι γράφω πιο γρήγορα από εκείνη στο κινητό.", "But I did fifteen minutes every morning, with my coffee, and after three months I was typing three times as many words a minute. The memoir has already reached eighty pages. My granddaughter says I type faster than she does on her phone."),
 ],
 "questions": [
  Q("Γιατί αποφάσισε να μάθει να γράφει πιο γρήγορα;", ["Για να βρει δουλειά", "Για να γράψει τις αναμνήσεις της για τα εγγόνια της", "Για να στέλνει μηνύματα στους φίλους της", "Γιατί της το ζήτησε η κόρη της"], 1, "αποφάσισα να γράψω τις αναμνήσεις μου για τα εγγόνια μου"),
  Q("Σε τι χρησιμεύει το μικρό εξόγκωμα στο Φ και στο Ξ;", ["Δείχνει ποια πλήκτρα είναι χαλασμένα", "Βοηθά να πατάς πιο δυνατά", "Βοηθά τα δάχτυλα να βρίσκουν τη θέση τους χωρίς να κοιτάζεις", "Δείχνει τα κεφαλαία γράμματα"], 2, "για να βρίσκουν τα δάχτυλα τη θέση τους χωρίς να κοιτάζεις"),
  Q("Πώς τα κατάφερε τελικά;", ["Πήγε σε ένα φροντιστήριο", "Της έκανε μαθήματα η εγγονή της", "Εξασκούνταν μία ώρα κάθε βράδυ", "Εξασκούνταν δεκαπέντε λεπτά κάθε πρωί"], 3, "Έκανα όμως δεκαπέντε λεπτά κάθε πρωί, με τον καφέ μου"),
 ],
 "gloss": {"πληκτρολόγιο": "πληκτρολόγιο — keyboard", "τυφλό σύστημα": "τυφλό σύστημα — touch-typing", "εξόγκωμα": "εξόγκωμα — bump", "παρατήσω": "παρατάω — to give up", "τριπλάσιες": "τριπλάσιος — three times as many"},
})

ITEMS.append({
 "id": "l186-dia-pappous-mazi-mas", "title": "Θα έρθει ο παππούς να μείνει μαζί μας;", "title_en": "Will Grandad come to live with us?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά αν ο πατέρας του άντρα θα μετακομίσει στο σπίτι τους.",
 "script": [
  L("Σοφία", "f", "Μίλησα πάλι με τον πατέρα σου σήμερα. Έπεσε δεύτερη φορά μέσα στον μήνα, Γιάννη. Δεν μπορεί να μένει άλλο μόνος του στο χωριό.", "I spoke to your father again today. He fell for the second time this month, Giannis. He can't go on living alone in the village."),
  L("Γιάννης", "m", "Το ξέρω. Αλλά πού να τον βάλουμε; Το σπίτι μας έχει τρία δωμάτια και τα παιδιά μοιράζονται ήδη το ένα. Και εκείνος δεν θέλει να ακούσει ούτε για γηροκομείο ούτε για Αθήνα.", "I know. But where would we put him? Our house has three rooms and the children already share one. And he won't hear of either a care home or Athens."),
  L("Σοφία", "f", "Σκέφτηκα κάτι. Το γραφείο σου μπορεί να γίνει δωμάτιο για τον παππού, κι εσύ να δουλεύεις από το σαλόνι τις μέρες που δεν πας στο γραφείο. Τα παιδιά τον λατρεύουν, και θα μας βοηθάει κι αυτός με το σχολείο τους.", "I've thought of something. Your study could become a room for Grandad, and you could work from the living room on the days you don't go to the office. The children adore him, and he'd help us with their schooling too."),
  L("Γιάννης", "m", "Κι αν δεν αντέξουμε όλοι μαζί; Ο πατέρας μου έχει τις ιδιοτροπίες του.", "And what if we can't stand all being together? My father has his quirks."),
  L("Σοφία", "f", "Ας το δοκιμάσουμε για τρεις μήνες, ως το καλοκαίρι. Αν δεν πάει καλά, θα βρούμε μια κυρία να μένει μαζί του στο χωριό.", "Let's try it for three months, until the summer. If it doesn't work out, we'll find a woman to live with him in the village."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί πια ο παππούς να μένει μόνος;", ["Γιατί πουλήθηκε το σπίτι του", "Γιατί έπεσε δεύτερη φορά μέσα στον μήνα", "Γιατί δεν έχει γιατρό στο χωριό", "Γιατί ζήτησε ο ίδιος να φύγει"], 1, "Έπεσε δεύτερη φορά μέσα στον μήνα"),
  Q("Τι προτείνει η Σοφία για το δωμάτιο;", ["Να μετακομίσουν σε μεγαλύτερο σπίτι", "Να μοιραστεί ο παππούς το δωμάτιο με τα παιδιά", "Να γίνει το γραφείο του Γιάννη δωμάτιο για τον παππού", "Να κοιμάται ο παππούς στο σαλόνι"], 2, "Το γραφείο σου μπορεί να γίνει δωμάτιο για τον παππού"),
  Q("Τι θα κάνουν αν η συγκατοίκηση δεν πάει καλά;", ["Θα πάει ο παππούς σε γηροκομείο", "Θα μετακομίσει ο παππούς στην Αθήνα", "Θα πάει η Σοφία στο χωριό", "Θα βρουν μια κυρία να μένει μαζί του στο χωριό"], 3, "θα βρούμε μια κυρία να μένει μαζί του στο χωριό"),
 ],
 "gloss": {"γηροκομείο": "γηροκομείο — care home", "λατρεύουν": "λατρεύω — to adore", "ιδιοτροπίες": "ιδιοτροπία — quirk, whim", "αντέξουμε": "αντέχω — to bear, stand"},
})

ITEMS.append({
 "id": "l186-news-drones-paralies", "title": "Χωρίς drones πάνω από τις παραλίες", "title_en": "No drones over the beaches", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων σε τοπικό ραδιοφωνικό σταθμό μιας παραθαλάσσιας πόλης.",
 "script": [
  L("Εκφωνήτρια", "f", "Με απόφαση του δημοτικού συμβουλίου, από την 1η Ιουνίου ως το τέλος Σεπτεμβρίου απαγορεύονται οι πτήσεις drones πάνω από τις οργανωμένες παραλίες του δήμου, από τις εννιά το πρωί ως τις οχτώ το βράδυ. Η απόφαση πάρθηκε μετά από δεκάδες παράπονα λουομένων, που έλεγαν ότι τους φωτογράφιζαν χωρίς να το ξέρουν.", "By decision of the municipal council, from 1 June to the end of September drone flights are banned over the municipality's organised beaches, from nine in the morning to eight in the evening. The decision was taken after dozens of complaints from bathers, who said they were being photographed without knowing it."),
  L("Εκφωνήτρια", "f", "Η δημοτική αστυνομία θα μπορεί να επιβάλλει πρόστιμο. Ο δήμαρχος θύμισε ότι, σύμφωνα με τους ευρωπαϊκούς κανόνες, οι χειριστές των περισσότερων drones με κάμερα πρέπει να είναι εγγεγραμμένοι, ενώ σε καμία περίπτωση δεν επιτρέπεται να πετούν πάνω από συγκεντρώσεις ανθρώπων.", "The municipal police will be able to impose fines. The mayor pointed out that, under European rules, operators of most drones with a camera must be registered, while in no case are they allowed to fly over gatherings of people."),
  L("Εκφωνήτρια", "f", "Αντιδράσεις εξέφρασαν οι φωτογράφοι γάμων, που χρησιμοποιούν συχνά drones για λήψεις στο ηλιοβασίλεμα. Ο δήμος απάντησε ότι μπορούν να ζητούν ειδική άδεια για τις ώρες μετά τις οχτώ.", "Wedding photographers, who often use drones for sunset shots, voiced objections. The municipality replied that they can apply for a special permit for the hours after eight."),
 ],
 "questions": [
  Q("Γιατί πάρθηκε η απόφαση;", ["Λόγω ατυχημάτων με drones", "Μετά από παράπονα λουομένων που τους φωτογράφιζαν χωρίς να το ξέρουν", "Γιατί τα drones ενοχλούσαν τα πουλιά", "Μετά από αίτημα των ξενοδόχων"], 1, "Η απόφαση πάρθηκε μετά από δεκάδες παράπονα λουομένων, που έλεγαν ότι τους φωτογράφιζαν χωρίς να το ξέρουν"),
  Q("Τι θύμισε ο δήμαρχος για τους ευρωπαϊκούς κανόνες;", ["Ότι τα drones απαγορεύονται παντού το καλοκαίρι", "Ότι επιτρέπονται μόνο σε επαγγελματίες", "Ότι δεν επιτρέπεται να πετούν πάνω από συγκεντρώσεις ανθρώπων", "Ότι πρέπει να πετούν μόνο το βράδυ"], 2, "σε καμία περίπτωση δεν επιτρέπεται να πετούν πάνω από συγκεντρώσεις ανθρώπων"),
  Q("Τι μπορούν να κάνουν οι φωτογράφοι γάμων;", ["Να πετούν ελεύθερα όλη μέρα", "Να πληρώνουν ένα μικρό τέλος", "Να φωτογραφίζουν μόνο από τη θάλασσα", "Να ζητούν ειδική άδεια για τις ώρες μετά τις οχτώ"], 3, "μπορούν να ζητούν ειδική άδεια για τις ώρες μετά τις οχτώ"),
 ],
 "gloss": {"πτήσεις": "πτήση — flight", "λουομένων": "λουόμενος — bather", "επιβάλλει": "επιβάλλω — to impose", "χειριστές": "χειριστής — operator, pilot", "εγγεγραμμένοι": "εγγεγραμμένος — registered", "λήψεις": "λήψη — shot (photo, film)"},
})

ITEMS.append({
 "id": "l186-rep-agora-paliatzidikon", "title": "Μια Κυριακή στο παζάρι του Μοναστηρακίου", "title_en": "A Sunday at the Monastiraki flea market", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από την υπαίθρια αγορά παλαιών αντικειμένων στο Μοναστηράκι της Αθήνας.",
 "script": [
  L("Ρεπόρτερ", "m", "Από τις επτά το πρωί, οι πάγκοι στην πλατεία Αβησσυνίας και στους γύρω δρόμους γεμίζουν παλιά ραδιόφωνα, πικάπ, δίσκους βινυλίου, κορνίζες, πιατικά και έπιπλα που έχουν δει καλύτερες μέρες. Οι πιο έμπειροι αγοραστές έρχονται νωρίς, με φακό, πριν φτάσουν οι τουρίστες.", "From seven in the morning, the stalls in Avyssinias Square and the surrounding streets fill with old radios, record players, vinyl records, frames, crockery and furniture that has seen better days. The most experienced buyers come early, with a torch, before the tourists arrive."),
  L("Ρεπόρτερ", "m", "Ο κύριος Στέλιος πουλάει εδώ παλιά αντικείμενα εδώ και σαράντα χρόνια. «Τα περισσότερα τα βρίσκω όταν αδειάζουν σπίτια μετά από θάνατο», λέει. «Οι κληρονόμοι συνήθως δεν θέλουν τίποτα. Εγώ ψάχνω και στο τελευταίο συρτάρι· μια φορά βρήκα μέσα σε ένα βιβλίο γράμματα από το μέτωπο του '40».", "Mr Stelios has been selling old objects here for forty years. 'I find most of them when houses are cleared after a death,' he says. 'The heirs usually don't want anything. I search even the last drawer; once I found letters from the 1940 front inside a book.'"),
  L("Ρεπόρτερ", "m", "Εδώ τίποτα δεν έχει σταθερή τιμή. Μια νεαρή αρχιτέκτονας παζαρεύει για ένα μπρούντζινο φωτιστικό και το παίρνει στη μισή τιμή από αυτήν που ζητούσε ο πωλητής. «Το παζάρι είναι μέρος του παιχνιδιού», μας λέει χαμογελώντας ο κύριος Στέλιος. «Αν δεν παζαρέψεις, με προσβάλλεις».", "Here nothing has a fixed price. A young architect haggles over a brass lamp and gets it at half the price the seller was asking. 'Haggling is part of the game,' Mr Stelios tells us with a smile. 'If you don't haggle, you insult me.'"),
 ],
 "questions": [
  Q("Γιατί έρχονται νωρίς οι πιο έμπειροι αγοραστές;", ["Γιατί οι τιμές είναι πιο χαμηλές το πρωί", "Για να φτάσουν πριν από τους τουρίστες", "Γιατί η αγορά κλείνει στις δέκα", "Για να βρουν πού να παρκάρουν"], 1, "Οι πιο έμπειροι αγοραστές έρχονται νωρίς, με φακό, πριν φτάσουν οι τουρίστες"),
  Q("Πού βρίσκει ο κύριος Στέλιος τα περισσότερα αντικείμενα;", ["Σε δημοπρασίες", "Στο εξωτερικό", "Όταν αδειάζουν σπίτια μετά από θάνατο", "Από άλλους πωλητές της αγοράς"], 2, "Τα περισσότερα τα βρίσκω όταν αδειάζουν σπίτια μετά από θάνατο"),
  Q("Τι λέει ο κύριος Στέλιος για το παζάρεμα;", ["Ότι δεν του αρέσει", "Ότι το κάνουν μόνο οι τουρίστες", "Ότι οι τιμές του είναι σταθερές", "Ότι είναι μέρος του παιχνιδιού"], 3, "Το παζάρι είναι μέρος του παιχνιδιού"),
 ],
 "gloss": {"παζάρι": "παζάρι — flea market; haggling", "πάγκοι": "πάγκος — stall", "πικάπ": "πικάπ — record player", "πιατικά": "πιατικά — crockery", "κληρονόμοι": "κληρονόμος — heir", "μέτωπο": "μέτωπο — (war) front", "παζαρεύει": "παζαρεύω — to haggle", "μπρούντζινο": "μπρούντζινος — brass, bronze", "προσβάλλεις": "προσβάλλω — to insult"},
})

ITEMS.append({
 "id": "l186-c1-ti-mas-lene-ta-dachtylidia-ton-dentron", "title": "Τι μας λένε τα δαχτυλίδια των δέντρων", "title_en": "What tree rings tell us", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια ερευνήτρια της δενδροχρονολογίας σε μια επιστημονική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς είναι τα «δαχτυλίδια» ενός δέντρου;", "What exactly are a tree's 'rings'?"),
  L("Ερευνήτρια", "f", "Σε κλίματα με εναλλαγή εποχών, όπως το δικό μας, ο κορμός προσθέτει κάθε χρόνο ένα καινούργιο στρώμα ξύλου κάτω από τον φλοιό. Την άνοιξη το ξύλο που σχηματίζεται είναι ανοιχτόχρωμο και πορώδες· προς το τέλος του καλοκαιριού γίνεται πιο σκούρο και πυκνό. Αυτή η εναλλαγή δημιουργεί τους ετήσιους δακτυλίους που βλέπουμε σε ένα κομμένο κούτσουρο. Ένας φαρδύς δακτύλιος σημαίνει συνήθως μια χρονιά με αρκετή βροχή· ένας στενός, μια χρονιά ξηρασίας.", "In climates with distinct seasons, like ours, the trunk adds a new layer of wood under the bark every year. In spring the wood that forms is light and porous; towards the end of summer it becomes darker and denser. This alternation creates the annual rings we see in a cut log. A wide ring usually means a year with plenty of rain; a narrow one, a year of drought."),
  L("Δημοσιογράφος", "m", "Και πώς γίνεται αυτό εργαλείο χρονολόγησης;", "And how does that become a dating tool?"),
  L("Ερευνήτρια", "f", "Επειδή όλα τα δέντρα μιας περιοχής ζουν τις ίδιες καλές και κακές χρονιές, σχηματίζουν το ίδιο μοτίβο από φαρδιούς και στενούς δακτυλίους, κάτι σαν γραμμωτό κώδικα. Αν συνδέσουμε τα μοτίβα από ζωντανά δέντρα, από παλιά δοκάρια και από ξύλα που βρέθηκαν σε ανασκαφές, χτίζουμε αλυσίδες που φτάνουν χιλιάδες χρόνια πίσω. Έτσι μπορούμε να πούμε σε ποια χρονιά κόπηκε το ξύλο μιας στέγης ή ενός πλοίου, και να ελέγξουμε την ακρίβεια της χρονολόγησης με άνθρακα-14.", "Because all the trees in an area live through the same good and bad years, they form the same pattern of wide and narrow rings, something like a barcode. If we link the patterns from living trees, from old beams and from wood found in excavations, we build chains that reach back thousands of years. That way we can say in which year the timber of a roof or a ship was cut, and check the accuracy of radiocarbon dating."),
  L("Δημοσιογράφος", "m", "Υπάρχουν πολύ γέρικα δέντρα στην Ελλάδα;", "Are there very old trees in Greece?"),
  L("Ερευνήτρια", "f", "Ναι. Το 2016 μια ερευνητική ομάδα χρονολόγησε στη Βόρεια Πίνδο ένα ρόμπολο, ένα είδος πεύκου των βουνών, με πάνω από χίλιους εβδομήντα πέντε δακτυλίους, και το ονόμασε «Άδωνι». Και δεν χρειάστηκε να το κόψουν: παίρνουμε από τον κορμό ένα λεπτό δείγμα, σαν μολύβι, με ένα ειδικό τρυπάνι, και το δέντρο συνεχίζει να ζει κανονικά.", "Yes. In 2016 a research team dated a Bosnian pine, a kind of mountain pine, in the northern Pindus with more than one thousand and seventy-five rings, and named it 'Adonis'. And they did not need to cut it down: we take a thin sample from the trunk, like a pencil, with a special drill, and the tree goes on living normally."),
 ],
 "questions": [
  Q("Τι σημαίνει συνήθως ένας στενός δακτύλιος;", ["Ότι το δέντρο ήταν άρρωστο", "Ότι η χρονιά είχε ξηρασία", "Ότι το δέντρο ήταν πολύ νέο", "Ότι ο χειμώνας ήταν ζεστός"], 1, "ένας στενός, μια χρονιά ξηρασίας"),
  Q("Γιατί τα δέντρα μιας περιοχής έχουν το ίδιο μοτίβο δακτυλίων;", ["Γιατί είναι του ίδιου είδους", "Γιατί φυτεύτηκαν την ίδια χρονιά", "Γιατί ζουν τις ίδιες καλές και κακές χρονιές", "Γιατί έχουν το ίδιο ύψος"], 2, "όλα τα δέντρα μιας περιοχής ζουν τις ίδιες καλές και κακές χρονιές"),
  Q("Πώς παίρνουν οι ερευνητές δείγμα από ένα ζωντανό δέντρο;", ["Κόβουν ένα κλαδί", "Κόβουν το δέντρο στη βάση του", "Μετρούν τον φλοιό", "Παίρνουν ένα λεπτό δείγμα από τον κορμό με ειδικό τρυπάνι"], 3, "παίρνουμε από τον κορμό ένα λεπτό δείγμα, σαν μολύβι, με ένα ειδικό τρυπάνι"),
 ],
 "gloss": {"δενδροχρονολογίας": "δενδροχρονολογία — dendrochronology, tree-ring dating", "φλοιό": "φλοιός — bark", "πορώδες": "πορώδης — porous", "δακτυλίους": "δακτύλιος — ring", "κούτσουρο": "κούτσουρο — log, stump", "γραμμωτό κώδικα": "γραμμωτός κώδικας — barcode", "δοκάρια": "δοκάρι — beam", "ρόμπολο": "ρόμπολο — Bosnian pine (Pinus heldreichii)", "τρυπάνι": "τρυπάνι — drill, borer"},
})

ITEMS.append({
 "id": "l186-c1-giati-ta-kounoupia-dialegoun-kapoious", "title": "Γιατί τα κουνούπια διαλέγουν κάποιους από εμάς", "title_en": "Why mosquitoes pick some of us", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν εντομολόγο να μιλά σε μια ραδιοφωνική εκπομπή για τα κουνούπια.",
 "script": [
  L("Εντομολόγος", "m", "Πρώτα απ' όλα, μόνο τα θηλυκά κουνούπια τσιμπούν· χρειάζονται τις πρωτεΐνες του αίματος για να ωριμάσουν τα αβγά τους. Τα αρσενικά τρέφονται με νέκταρ. Για να βρει το θύμα της, η θηλυκιά ακολουθεί πρώτα το διοξείδιο του άνθρακα που εκπνέουμε, το οποίο μπορεί να το αντιληφθεί από αρκετά μέτρα μακριά. Όσο πλησιάζει, την καθοδηγούν η θερμότητα του σώματος και, κυρίως, η μυρωδιά του δέρματος.", "First of all, only female mosquitoes bite; they need the proteins in blood for their eggs to mature. The males feed on nectar. To find her victim, the female first follows the carbon dioxide we breathe out, which she can detect from several metres away. As she gets closer, she is guided by body heat and, above all, by the smell of the skin."),
  L("Εντομολόγος", "m", "Και εδώ βρίσκεται το μυστικό των λεγόμενων «μαγνητών για κουνούπια». Η μυρωδιά μας οφείλεται σε μεγάλο βαθμό στα βακτήρια που ζουν στο δέρμα και διασπούν τον ιδρώτα και το λίπος του. Σε μια μελέτη του 2022, οι άνθρωποι που προσέλκυαν περισσότερο τα κουνούπια είχαν στο δέρμα τους πολύ μεγαλύτερες ποσότητες από ορισμένα λιπαρά οξέα, και παρέμεναν ελκυστικοί για χρόνια. Δηλαδή, δεν φταίει το τι φάγατε χθες· είναι κάτι πιο σταθερό, σαν προσωπική υπογραφή.", "And here lies the secret of so-called 'mosquito magnets'. Our smell is largely due to the bacteria that live on the skin and break down its sweat and oils. In a 2022 study, the people who attracted mosquitoes most had much larger amounts of certain fatty acids on their skin, and they stayed attractive for years. In other words, it isn't what you ate yesterday; it is something more stable, like a personal signature."),
  L("Εντομολόγος", "m", "Για τη θεωρία ότι προτιμούν μια συγκεκριμένη ομάδα αίματος, τα στοιχεία είναι αντιφατικά και δεν θα τη θεωρούσα αποδεδειγμένη. Οι έγκυες πάντως φαίνεται να τσιμπιούνται συχνότερα, πιθανότατα επειδή αναπνέουν περισσότερο και έχουν λίγο υψηλότερη θερμοκρασία. Η καλύτερη προστασία παραμένει η απλή: σίτες, ανεμιστήρας, γιατί τα κουνούπια πετούν δύσκολα στον αέρα, και εντομοαπωθητικό με εγκεκριμένη δραστική ουσία.", "As for the theory that they prefer a particular blood group, the evidence is contradictory and I would not consider it proven. Pregnant women, however, seem to be bitten more often, probably because they breathe more and have a slightly higher temperature. The best protection is still the simple kind: screens, a fan, because mosquitoes struggle to fly in moving air, and repellent with an approved active ingredient."),
 ],
 "questions": [
  Q("Γιατί τσιμπούν μόνο τα θηλυκά κουνούπια;", ["Γιατί τα αρσενικά δεν έχουν προβοσκίδα", "Γιατί χρειάζονται τις πρωτεΐνες του αίματος για τα αβγά τους", "Γιατί ζουν περισσότερο", "Γιατί δεν μπορούν να βρουν νέκταρ"], 1, "χρειάζονται τις πρωτεΐνες του αίματος για να ωριμάσουν τα αβγά τους"),
  Q("Τι έδειξε η μελέτη του 2022;", ["Ότι η διατροφή καθορίζει ποιον τσιμπούν", "Ότι τα κουνούπια προτιμούν την ομάδα αίματος Ο", "Ότι όσοι προσελκύουν τα κουνούπια έχουν περισσότερα ορισμένα λιπαρά οξέα στο δέρμα", "Ότι τα κουνούπια βλέπουν τα σκούρα χρώματα"], 2, "είχαν στο δέρμα τους πολύ μεγαλύτερες ποσότητες από ορισμένα λιπαρά οξέα"),
  Q("Γιατί βοηθά ο ανεμιστήρας;", ["Γιατί διώχνει τη μυρωδιά", "Γιατί ρίχνει τη θερμοκρασία του σώματος", "Γιατί ο θόρυβός του τα τρομάζει", "Γιατί τα κουνούπια πετούν δύσκολα στον αέρα"], 3, "τα κουνούπια πετούν δύσκολα στον αέρα"),
 ],
 "gloss": {"εντομολόγο": "εντομολόγος — entomologist", "εκπνέουμε": "εκπνέω — to breathe out", "αντιληφθεί": "αντιλαμβάνομαι — to perceive, detect", "διασπούν": "διασπώ — to break down", "λιπαρά οξέα": "λιπαρό οξύ — fatty acid", "αντιφατικά": "αντιφατικός — contradictory", "σίτες": "σίτα — (insect) screen", "εντομοαπωθητικό": "εντομοαπωθητικό — insect repellent", "δραστική ουσία": "δραστική ουσία — active ingredient"},
})

rnd = random.Random(186)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-186.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
