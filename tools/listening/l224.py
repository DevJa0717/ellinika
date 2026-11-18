# Source for library/listening/listening-224.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l224.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l224-news-kameres-kinito", "title": "Κάμερες που «βλέπουν» το κινητό στο τιμόνι", "title_en": "Cameras that spot the phone at the wheel", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο ραδιόφωνο για νέες κάμερες κυκλοφορίας σε κεντρικούς δρόμους.",
 "script": [
  L("Εκφωνήτρια", "f", "Σε δοκιμαστική λειτουργία μπαίνουν από τη Δευτέρα νέες κάμερες σε μεγάλους δρόμους της πόλης, που δεν ελέγχουν μόνο την ταχύτητα. Με τη βοήθεια λογισμικού αναγνώρισης εικόνας, εντοπίζουν οδηγούς που κρατούν το κινητό τους ή δεν φορούν ζώνη ασφαλείας.", "From Monday, new cameras go into trial operation on major city roads, and they don't only check speed. With the help of image-recognition software, they spot drivers who are holding their phone or not wearing a seat belt."),
  L("Εκφωνήτρια", "f", "Κάθε φωτογραφία που επισημαίνει το σύστημα ελέγχεται στη συνέχεια από έναν τροχονόμο, πριν σταλεί οποιοδήποτε πρόστιμο. Οι υπεύθυνοι τονίζουν ότι τα πρόσωπα των επιβατών θολώνονται αυτόματα και ότι οι εικόνες χωρίς παράβαση διαγράφονται μέσα σε λίγες ώρες.", "Every photo the system flags is then checked by a traffic officer before any fine is sent. Those in charge stress that passengers' faces are blurred automatically and that images without a violation are deleted within a few hours."),
  L("Εκφωνήτρια", "f", "Τον πρώτο μήνα οι οδηγοί που θα εντοπιστούν θα λάβουν μόνο μια προειδοποίηση. Οι οργανώσεις για την οδική ασφάλεια χαιρετίζουν το μέτρο, ενώ ένας σύλλογος για τα προσωπικά δεδομένα ζητά να δημοσιευτεί αναλυτικά πώς λειτουργεί το λογισμικό.", "In the first month, drivers who are caught will receive only a warning. Road-safety organisations welcome the measure, while an association for personal data is asking for a detailed account of how the software works to be published."),
 ],
 "questions": [
  Q("Τι εντοπίζουν οι νέες κάμερες εκτός από την ταχύτητα;", ["Παλιά αυτοκίνητα", "Οδηγούς με κινητό στο χέρι ή χωρίς ζώνη", "Παράνομο παρκάρισμα", "Οδηγούς χωρίς δίπλωμα"], 1, "εντοπίζουν οδηγούς που κρατούν το κινητό τους ή δεν φορούν ζώνη ασφαλείας"),
  Q("Τι γίνεται πριν σταλεί πρόστιμο;", ["Ο οδηγός καλείται στο τμήμα", "Ένας τροχονόμος ελέγχει τη φωτογραφία", "Το σύστημα στέλνει μήνυμα στον οδηγό", "Η φωτογραφία δημοσιεύεται"], 1, "ελέγχεται στη συνέχεια από έναν τροχονόμο, πριν σταλεί οποιοδήποτε πρόστιμο"),
  Q("Τι θα γίνει τον πρώτο μήνα;", ["Τα πρόστιμα θα είναι διπλά", "Οι κάμερες θα είναι κλειστές", "Οι οδηγοί θα λάβουν μόνο προειδοποίηση", "Θα ελέγχονται μόνο τα ταξί"], 2, "θα λάβουν μόνο μια προειδοποίηση"),
  Q("Τι ζητά ο σύλλογος για τα προσωπικά δεδομένα;", ["Να καταργηθούν οι κάμερες", "Να δημοσιευτεί πώς λειτουργεί το λογισμικό", "Να μειωθούν τα πρόστιμα", "Να μπουν κάμερες και σε άλλους δρόμους"], 1, "ζητά να δημοσιευτεί αναλυτικά πώς λειτουργεί το λογισμικό"),
 ],
 "gloss": {"δοκιμαστική": "δοκιμαστικός — trial, test (adj.)", "λογισμικού": "λογισμικό — software", "εντοπίζουν": "εντοπίζω — to locate, to spot", "επισημαίνει": "επισημαίνω — to flag, to point out", "τροχονόμο": "τροχονόμος — traffic officer", "πρόστιμο": "πρόστιμο — fine", "θολώνονται": "θολώνω — to blur", "παράβαση": "παράβαση — violation, offence", "χαιρετίζουν": "χαιρετίζω — to welcome (a measure)"},
})
ITEMS.append({
 "id": "l224-vm-syntiritria-eikona", "title": "Μήνυμα από τη συντηρήτρια για την εικόνα της γιαγιάς", "title_en": "Message from the conservator about grandmother's icon", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τη συντηρήτρια στην οποία δώσατε μια παλιά εικόνα της γιαγιάς σας.",
 "script": [
  L("Συντηρήτρια", "f", "Καλησπέρα, κύριε Λαμπράκη, η Ελένη Βογιατζή είμαι, από το εργαστήριο συντήρησης. Τελείωσα την πρώτη εξέταση της εικόνας του Αγίου Νικολάου και ήθελα να σας πω τι βρήκα, πριν προχωρήσω.", "Good evening, Mr Lambrakis, it's Eleni Vogiatzi from the conservation workshop. I've finished the first examination of the icon of Saint Nicholas and wanted to tell you what I found before going ahead."),
  L("Συντηρήτρια", "f", "Τα καλά νέα είναι ότι το ξύλο είναι γερό. Υπάρχουν κάποιες παλιές τρύπες από σαράκι, αλλά δεν βρήκα ζωντανά έντομα, οπότε δεν χρειάζεται απεντόμωση. Το πρόβλημα είναι το βερνίκι: έχει κιτρινίσει τόσο πολύ από τον καπνό των κεριών, που το πρόσωπο του αγίου σχεδόν δεν φαίνεται.", "The good news is that the wood is sound. There are some old woodworm holes, but I found no live insects, so no pest treatment is needed. The problem is the varnish: it has yellowed so much from candle smoke that the saint's face is barely visible."),
  L("Συντηρήτρια", "f", "Σας προτείνω δύο λύσεις. Η πρώτη είναι ένας απλός καθαρισμός της επιφάνειας, που κοστίζει γύρω στα εκατόν πενήντα ευρώ και τελειώνει σε δύο εβδομάδες. Η δεύτερη είναι να αφαιρέσω όλο το παλιό βερνίκι· είναι πιο ακριβό, περίπου τετρακόσια, και θέλει δύο μήνες, αλλά τα χρώματα θα φανούν όπως ήταν αρχικά.", "I suggest two solutions. The first is a simple surface cleaning, which costs around one hundred and fifty euros and is finished in two weeks. The second is for me to remove all the old varnish; it's more expensive, about four hundred, and takes two months, but the colours will show as they originally were."),
  L("Συντηρήτρια", "f", "Δεν βιάζομαι, σκεφτείτε το με την ησυχία σας. Αν θέλετε, περάστε από το εργαστήριο να σας δείξω ένα μικρό σημείο στη γωνία που καθάρισα δοκιμαστικά. Καλό βράδυ!", "I'm in no hurry, think about it at your leisure. If you like, drop by the workshop so I can show you a small spot in the corner that I cleaned as a test. Good evening!"),
 ],
 "questions": [
  Q("Σε τι κατάσταση είναι το ξύλο της εικόνας;", ["Είναι σάπιο", "Είναι γερό, με παλιές τρύπες από σαράκι", "Έχει ζωντανά έντομα", "Έχει σπάσει στη μέση"], 1, "το ξύλο είναι γερό. Υπάρχουν κάποιες παλιές τρύπες από σαράκι"),
  Q("Ποιο είναι το κύριο πρόβλημα της εικόνας;", ["Λείπει ένα κομμάτι", "Τα χρώματα έχουν ξεβάψει από τον ήλιο", "Το βερνίκι έχει κιτρινίσει από τον καπνό των κεριών", "Η κορνίζα έχει χαλάσει"], 2, "έχει κιτρινίσει τόσο πολύ από τον καπνό των κεριών"),
  Q("Τι πλεονέκτημα έχει η δεύτερη λύση;", ["Είναι φθηνότερη", "Τελειώνει πιο γρήγορα", "Τα χρώματα θα φανούν όπως ήταν αρχικά", "Δεν χρειάζεται να αφήσει την εικόνα"], 2, "τα χρώματα θα φανούν όπως ήταν αρχικά"),
  Q("Τι προτείνει η συντηρήτρια στο τέλος;", ["Να αποφασίσει μέχρι αύριο", "Να περάσει να δει ένα σημείο που καθάρισε δοκιμαστικά", "Να πάρει πίσω την εικόνα", "Να ρωτήσει έναν άλλο συντηρητή"], 1, "περάστε από το εργαστήριο να σας δείξω ένα μικρό σημείο στη γωνία που καθάρισα δοκιμαστικά"),
 ],
 "gloss": {"συντηρήτρια": "συντηρήτρια — conservator, restorer (f.)", "συντήρησης": "συντήρηση — conservation, restoration", "εικόνας": "εικόνα — icon; picture", "σαράκι": "σαράκι — woodworm", "έντομα": "έντομο — insect", "απεντόμωση": "απεντόμωση — pest control, disinfestation", "βερνίκι": "βερνίκι — varnish", "κιτρινίσει": "κιτρινίζω — to turn yellow", "δοκιμαστικά": "δοκιμαστικά — as a test"},
})
ITEMS.append({
 "id": "l224-c1-mono-arxi-telos-listas", "title": "Γιατί θυμόμαστε την αρχή και το τέλος μιας λίστας", "title_en": "Why we remember the beginning and the end of a list", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή ψυχολογίας για τη μνήμη.",
 "script": [
  L("Ομιλήτρια", "f", "Κάντε ένα απλό πείραμα: ζητήστε από κάποιον να ακούσει μια λίστα με δεκαπέντε λέξεις και μετά να σας πει όσες θυμάται, με όποια σειρά θέλει. Σχεδόν πάντα θα θυμηθεί περισσότερες από τις πρώτες και από τις τελευταίες λέξεις, ενώ οι μεσαίες θα χαθούν. Οι ψυχολόγοι το ονομάζουν φαινόμενο της σειριακής θέσης.", "Try a simple experiment: ask someone to listen to a list of fifteen words and then tell you as many as they remember, in any order they like. Almost always they will remember more of the first and the last words, while the middle ones will be lost. Psychologists call this the serial position effect."),
  L("Ομιλήτρια", "f", "Το φαινόμενο έχει δύο σκέλη, και εξηγούνται διαφορετικά. Οι πρώτες λέξεις ωφελούνται επειδή ο ακροατής έχει χρόνο να τις επαναλάβει νοερά, πριν αρχίσουν να συσσωρεύονται οι υπόλοιπες· έτσι περνούν πιο εύκολα στη μακροπρόθεσμη μνήμη. Οι τελευταίες, αντίθετα, θυμούνται απλώς επειδή βρίσκονται ακόμη στη βραχυπρόθεσμη μνήμη τη στιγμή της ανάκλησης.", "The effect has two parts, and they are explained differently. The first words benefit because the listener has time to rehearse them mentally before the rest begin to pile up; that way they pass more easily into long-term memory. The last ones, by contrast, are remembered simply because they are still in short-term memory at the moment of recall."),
  L("Ομιλήτρια", "f", "Πώς το ξέρουμε αυτό; Αν βάλουμε τους συμμετέχοντες να μετρούν αντίστροφα για μισό λεπτό πριν απαντήσουν, το πλεονέκτημα των τελευταίων λέξεων σχεδόν εξαφανίζεται, ενώ των πρώτων μένει. Αν, πάλι, διαβάσουμε τη λίστα πιο γρήγορα, χάνεται κυρίως το πλεονέκτημα των πρώτων, γιατί δεν μένει χρόνος για επανάληψη.", "How do we know this? If we make participants count backwards for half a minute before answering, the advantage of the last words almost disappears, while that of the first remains. If, on the other hand, we read the list faster, it is mainly the advantage of the first ones that is lost, because there is no time left for rehearsal."),
  L("Ομιλήτρια", "f", "Οι συνέπειες ξεπερνούν το εργαστήριο. Σε μια συνέντευξη για δουλειά, σε μια σειρά από ομιλίες ή όταν μαθαίνετε λεξιλόγιο, ό,τι βρίσκεται στη μέση κινδυνεύει να ξεχαστεί. Γι’ αυτό, όταν μελετάτε, αξίζει να ανακατεύετε τη σειρά των λέξεων κάθε φορά, ώστε καμία να μην είναι μονίμως καταδικασμένη στη μέση.", "The consequences go beyond the laboratory. In a job interview, in a series of talks or when you learn vocabulary, whatever is in the middle risks being forgotten. That is why, when you study, it is worth shuffling the order of the words each time, so that none is permanently condemned to the middle."),
 ],
 "questions": [
  Q("Ποιες λέξεις μιας λίστας ξεχνιούνται συνήθως;", ["Οι πρώτες", "Οι τελευταίες", "Οι μεσαίες", "Οι μεγαλύτερες"], 2, "οι μεσαίες θα χαθούν"),
  Q("Γιατί θυμόμαστε καλύτερα τις πρώτες λέξεις;", ["Γιατί είναι πιο εύκολες", "Γιατί προλαβαίνουμε να τις επαναλάβουμε νοερά", "Γιατί είναι ακόμη στη βραχυπρόθεσμη μνήμη", "Γιατί τις ακούμε πιο δυνατά"], 1, "ο ακροατής έχει χρόνο να τις επαναλάβει νοερά"),
  Q("Τι συμβαίνει αν οι συμμετέχοντες μετρούν αντίστροφα πριν απαντήσουν;", ["Ξεχνούν όλες τις λέξεις", "Χάνεται σχεδόν το πλεονέκτημα των τελευταίων λέξεων", "Θυμούνται καλύτερα τις μεσαίες", "Χάνεται το πλεονέκτημα των πρώτων λέξεων"], 1, "το πλεονέκτημα των τελευταίων λέξεων σχεδόν εξαφανίζεται"),
  Q("Τι συμβουλεύει η ομιλήτρια όσους μαθαίνουν λεξιλόγιο;", ["Να μαθαίνουν λίγες λέξεις τη φορά", "Να ανακατεύουν τη σειρά των λέξεων κάθε φορά", "Να διαβάζουν τη λίστα πιο γρήγορα", "Να ξεκινούν πάντα από το τέλος"], 1, "αξίζει να ανακατεύετε τη σειρά των λέξεων κάθε φορά"),
 ],
 "gloss": {"σειριακής": "σειριακός — serial", "σκέλη": "σκέλος — part, component; leg", "νοερά": "νοερά — mentally, in one's head", "συσσωρεύονται": "συσσωρεύομαι — to pile up, accumulate", "μακροπρόθεσμη": "μακροπρόθεσμος — long-term", "βραχυπρόθεσμη": "βραχυπρόθεσμος — short-term", "ανάκλησης": "ανάκληση — recall", "αντίστροφα": "αντίστροφα — backwards, in reverse", "καταδικασμένη": "καταδικασμένος — condemned, doomed"},
})
ITEMS.append({
 "id": "l224-c1-int-spilaiodytis", "title": "Ο δύτης των υποβρύχιων σπηλαίων", "title_en": "The underwater cave diver", "type": "interview", "level": "C1",
 "context_el": "Ένας σπηλαιοδύτης μιλά σε μια ραδιοφωνική εκπομπή για τη χαρτογράφηση υποβρύχιων σπηλαίων.",
 "script": [
  L("Δημοσιογράφος", "f", "Οι περισσότεροι δύτες κατεβαίνουν για να δουν ψάρια και κοράλλια. Εσείς επιλέγετε να μπαίνετε σε στενά, κατασκότεινα περάσματα κάτω από τα βουνά. Γιατί;", "Most divers go down to see fish and corals. You choose to go into narrow, pitch-dark passages under the mountains. Why?"),
  L("Σπηλαιοδύτης", "m", "Γιατί εκεί υπάρχουν ακόμη μέρη που κανένας άνθρωπος δεν έχει δει. Η Ελλάδα είναι γεμάτη ασβεστόλιθο, και το νερό της βροχής έχει σκάψει μέσα του, μέσα σε χιλιάδες χρόνια, ολόκληρα δίκτυα από στοές. Πολλές από αυτές καταλήγουν σε πηγές κοντά στη θάλασσα, όπου το γλυκό νερό ανακατεύεται με το αλμυρό.", "Because there are still places there that no human has seen. Greece is full of limestone, and over thousands of years rainwater has carved whole networks of tunnels inside it. Many of them end in springs near the sea, where fresh water mixes with salt water."),
  L("Δημοσιογράφος", "f", "Δεν είναι επικίνδυνο;", "Isn't it dangerous?"),
  L("Σπηλαιοδύτης", "m", "Είναι, αν δεν σέβεσαι τους κανόνες. Ο πιο σημαντικός είναι το νήμα-οδηγός: ένα σκοινί που απλώνουμε από την είσοδο και το ακολουθούμε για να βγούμε. Αν σηκωθεί λάσπη από τον βυθό, η ορατότητα πέφτει στο μηδέν σε δευτερόλεπτα, και τότε το νήμα είναι το μόνο που σε συνδέει με την έξοδο. Ο άλλος κανόνας είναι ο κανόνας των τρίτων: το ένα τρίτο του αέρα για να μπεις, ένα τρίτο για να βγεις, και ένα τρίτο για ό,τι στραβό συμβεί.", "It is, if you don't respect the rules. The most important is the guideline: a rope we lay from the entrance and follow to get out. If silt is stirred up from the bottom, visibility drops to zero in seconds, and then the line is the only thing connecting you to the exit. The other rule is the rule of thirds: one third of the air to go in, one third to come out, and one third for whatever goes wrong."),
  L("Δημοσιογράφος", "f", "Και τι κερδίζει η επιστήμη από αυτές τις καταδύσεις;", "And what does science gain from these dives?"),
  L("Σπηλαιοδύτης", "m", "Πολλά. Οι χάρτες μας δείχνουν από πού έρχεται το νερό που πίνουν πολλά χωριά, και πού κινδυνεύει να μολυνθεί. Βρίσκουμε επίσης μικροσκοπικά ζώα, τυφλά και χωρίς χρώμα, που ζουν μόνο σε αυτό το σκοτάδι. Και κάποιες φορές, σε σπήλαια που κάποτε ήταν στεγνά, πριν ανέβει η στάθμη της θάλασσας, βρίσκονται ίχνη από ζώα ή ανθρώπους. Εκεί πια δεν αγγίζουμε τίποτα· φωτογραφίζουμε και ειδοποιούμε τους αρχαιολόγους.", "A lot. Our maps show where the water that many villages drink comes from, and where it is at risk of pollution. We also find tiny animals, blind and colourless, that live only in this darkness. And sometimes, in caves that were once dry, before the sea level rose, traces of animals or people are found. There we touch nothing; we take photographs and notify the archaeologists."),
 ],
 "questions": [
  Q("Γιατί προτιμά ο σπηλαιοδύτης τα υποβρύχια σπήλαια;", ["Γιατί έχουν περισσότερα ψάρια", "Γιατί εκεί υπάρχουν μέρη που δεν έχει δει κανένας", "Γιατί είναι πιο ασφαλή", "Γιατί πληρώνεται καλύτερα"], 1, "εκεί υπάρχουν ακόμη μέρη που κανένας άνθρωπος δεν έχει δει"),
  Q("Σε τι χρησιμεύει το νήμα-οδηγός;", ["Μετρά το βάθος", "Δένει τους δύτες μεταξύ τους", "Είναι ο δρόμος προς την έξοδο όταν χαθεί η ορατότητα", "Δείχνει πόσος αέρας απομένει"], 2, "το νήμα είναι το μόνο που σε συνδέει με την έξοδο"),
  Q("Τι ορίζει ο κανόνας των τρίτων;", ["Ότι κατεβαίνουν πάντα τρεις δύτες", "Ότι ένα τρίτο του αέρα μένει για απρόοπτα", "Ότι μένουν μέσα το πολύ τρεις ώρες", "Ότι εξερευνούν το ένα τρίτο του σπηλαίου κάθε φορά"], 1, "ένα τρίτο για ό,τι στραβό συμβεί"),
  Q("Τι κάνουν όταν βρίσκουν ίχνη ζώων ή ανθρώπων;", ["Τα μαζεύουν για το μουσείο", "Δεν αγγίζουν τίποτα· φωτογραφίζουν και ειδοποιούν τους αρχαιολόγους", "Κλείνουν την είσοδο του σπηλαίου", "Τα δημοσιεύουν αμέσως στο διαδίκτυο"], 1, "δεν αγγίζουμε τίποτα· φωτογραφίζουμε και ειδοποιούμε τους αρχαιολόγους"),
 ],
 "gloss": {"κατασκότεινα": "κατασκότεινος — pitch-dark", "περάσματα": "πέρασμα — passage", "ασβεστόλιθο": "ασβεστόλιθος — limestone", "στοές": "στοά — tunnel, gallery", "νήμα-οδηγός": "νήμα-οδηγός — guideline (diving)", "λάσπη": "λάσπη — mud, silt", "ορατότητα": "ορατότητα — visibility", "στραβό": "στραβός — crooked; (here) something going wrong", "μολυνθεί": "μολύνομαι — to be polluted, contaminated", "στάθμη": "στάθμη — level (of water)"},
})
rnd = random.Random(224)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-224.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
