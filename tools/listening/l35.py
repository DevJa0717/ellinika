# Source for library/listening/listening-35.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l35.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l35-ann-lykavittos", "title": "Αλλαγή στη συναυλία του Λυκαβηττού", "title_en": "A change to the Lycabettus concert", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση πριν από μια συναυλία στο θέατρο του Λυκαβηττού.",
 "script": [
  L("Εκφωνητής", "m", "Καλησπέρα σας και καλώς ήρθατε. Λόγω των ισχυρών ανέμων που πνέουν απόψε στην κορυφή του λόφου, η έναρξη της συναυλίας καθυστερεί κατά σαράντα πέντε λεπτά. Οι τεχνικοί μας ελέγχουν αυτή τη στιγμή τη σκηνή και τα φωτιστικά, για να είναι όλα απολύτως ασφαλή.", "Good evening and welcome. Because of the strong winds blowing tonight at the top of the hill, the start of the concert is delayed by forty-five minutes. Our technicians are checking the stage and the lighting right now, so that everything is completely safe."),
  L("Εκφωνητής", "m", "Παρακαλούμε να παραμείνετε στις θέσεις σας ή στον χώρο του κυλικείου και να μην κατεβαίνετε προς την είσοδο, γιατί τα σκαλιά είναι στενά. Τα εισιτήρια ισχύουν κανονικά· δεν χρειάζεται να τα σκανάρετε ξανά.", "Please remain in your seats or in the snack-bar area and do not go down towards the entrance, because the steps are narrow. Tickets remain valid; there is no need to scan them again."),
  L("Εκφωνητής", "m", "Αν ο άνεμος δεν κοπάσει μέχρι τις δέκα, η συναυλία θα αναβληθεί για την Πέμπτη, και τα εισιτήρια θα ισχύουν για τη νέα ημερομηνία. Όσοι δεν μπορούν να έρθουν την Πέμπτη θα πάρουν πίσω τα χρήματά τους από το σημείο όπου τα αγόρασαν. Σας ευχαριστούμε για την υπομονή σας.", "If the wind doesn't die down by ten, the concert will be postponed to Thursday, and the tickets will be valid for the new date. Those who can't come on Thursday will get their money back from the place where they bought them. Thank you for your patience."),
 ],
 "questions": [
  Q("Γιατί καθυστερεί η συναυλία;", ["Γιατί αρρώστησε ο τραγουδιστής", "Λόγω ισχυρών ανέμων", "Γιατί χάλασε το ηχητικό", "Γιατί άργησαν οι θεατές"], 1, "Λόγω των ισχυρών ανέμων που πνέουν απόψε"),
  Q("Τι ζητείται από το κοινό;", ["Να φύγει προσωρινά από το θέατρο", "Να μείνει στις θέσεις του ή στο κυλικείο", "Να σκανάρει ξανά τα εισιτήρια", "Να μετακινηθεί στις μπροστινές σειρές"], 1, "να παραμείνετε στις θέσεις σας ή στον χώρο του κυλικείου"),
  Q("Τι θα γίνει αν ο άνεμος δεν κοπάσει μέχρι τις δέκα;", ["Η συναυλία θα γίνει σε κλειστό χώρο", "Θα αναβληθεί για την Πέμπτη", "Θα ακυρωθεί χωρίς επιστροφή χρημάτων", "Θα γίνει μόνο το πρώτο μέρος"], 1, "η συναυλία θα αναβληθεί για την Πέμπτη"),
 ],
 "gloss": {"ανέμων": "άνεμος — wind", "πνέουν": "πνέω — to blow", "έναρξη": "έναρξη — start, opening", "φωτιστικά": "φωτιστικό — light fitting", "να παραμείνετε": "παραμένω — to remain", "κυλικείου": "κυλικείο — snack bar", "σκαλιά": "σκαλί — step", "ισχύουν": "ισχύω — to be valid", "κοπάσει": "κοπάζω — to die down, abate", "θα αναβληθεί": "αναβάλλομαι — to be postponed", "υπομονή": "υπομονή — patience"},
})

ITEMS.append({
 "id": "l35-vm-logotherapeftria", "title": "Μήνυμα από τη λογοθεραπεύτρια", "title_en": "A message from the speech therapist", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τη λογοθεραπεύτρια του παιδιού σας.",
 "script": [
  L("Λογοθεραπεύτρια", "f", "Καλημέρα σας, η Ελένη Μαργαρίτη είμαι, η λογοθεραπεύτρια του Νικόλα. Ήθελα να σας πω ότι είμαι πολύ ικανοποιημένη από την πρόοδό του. Το «ρο» το λέει πια σωστά σχεδόν σε όλες τις λέξεις, και στο σχολείο η δασκάλα του λέει ότι συμμετέχει πολύ περισσότερο.", "Good morning, it's Eleni Margariti, Nikolas's speech therapist. I wanted to tell you that I'm very pleased with his progress. He now says the 'r' correctly in almost all words, and at school his teacher says he takes part much more."),
  L("Λογοθεραπεύτρια", "f", "Γι' αυτό σκέφτομαι από τον επόμενο μήνα να κάνουμε μία συνεδρία την εβδομάδα αντί για δύο. Θα κρατήσουμε την Τρίτη στις πέντε, αν σας βολεύει ακόμη, και την Παρασκευή θα την αφήσουμε ελεύθερη.", "So I'm thinking that from next month we'll do one session a week instead of two. We'll keep Tuesday at five, if it still suits you, and leave Friday free."),
  L("Λογοθεραπεύτρια", "f", "Είναι σημαντικό όμως να συνεχίσετε τις ασκήσεις στο σπίτι, δέκα λεπτά κάθε μέρα, με το τετράδιο που σας έδωσα. Μέσα στον Μάιο θα κάνουμε μια νέα αξιολόγηση και θα αποφασίσουμε μαζί αν χρειάζεται να συνεχίσουμε. Καλή σας μέρα.", "But it's important that you continue the exercises at home, ten minutes every day, with the workbook I gave you. During May we'll do a new assessment and decide together whether we need to continue. Have a good day."),
 ],
 "questions": [
  Q("Τι λέει η λογοθεραπεύτρια για τον Νικόλα;", ["Ότι χρειάζεται περισσότερες συνεδρίες", "Ότι έχει προοδεύσει πολύ", "Ότι δυσκολεύεται στο σχολείο", "Ότι πρέπει να αλλάξει θεραπεύτρια"], 1, "είμαι πολύ ικανοποιημένη από την πρόοδό του"),
  Q("Τι προτείνει για τον επόμενο μήνα;", ["Δύο συνεδρίες την Παρασκευή", "Μία συνεδρία την εβδομάδα αντί για δύο", "Να σταματήσουν τις συνεδρίες", "Συνεδρίες μέσω υπολογιστή"], 1, "μία συνεδρία την εβδομάδα αντί για δύο"),
  Q("Τι πρέπει να κάνουν οι γονείς;", ["Να μιλήσουν με τη δασκάλα", "Να συνεχίσουν τις ασκήσεις στο σπίτι κάθε μέρα", "Να αγοράσουν νέο τετράδιο", "Να κλείσουν ραντεβού για τον Μάιο"], 1, "να συνεχίσετε τις ασκήσεις στο σπίτι, δέκα λεπτά κάθε μέρα"),
 ],
 "gloss": {"λογοθεραπεύτρια": "λογοθεραπεύτρια — speech therapist", "ικανοποιημένη": "ικανοποιημένος — satisfied, pleased", "πρόοδό": "πρόοδος — progress", "συμμετέχει": "συμμετέχω — to take part", "συνεδρία": "συνεδρία — session", "σας βολεύει": "βολεύει — it suits", "ασκήσεις": "άσκηση — exercise", "αξιολόγηση": "αξιολόγηση — assessment"},
})

ITEMS.append({
 "id": "l35-dia-keramiki", "title": "Μαθήματα κεραμικής", "title_en": "Pottery classes", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα εργαστήριο κεραμικής.",
 "script": [
  L("Πελάτης", "m", "Καλησπέρα. Είδα την αφίσα σας για τα μαθήματα κεραμικής. Δεν έχω πιάσει ποτέ πηλό στα χέρια μου· είναι για αρχάριους;", "Good evening. I saw your poster about the pottery classes. I've never held clay in my hands; are they for beginners?"),
  L("Κεραμίστρια", "f", "Βεβαίως. Το τμήμα της Τετάρτης είναι για αρχάριους. Τον πρώτο μήνα δουλεύουμε μόνο με τα χέρια, φτιάχνουμε μπολ και μικρά βάζα με τη μέθοδο των κορδονιών. Στον τροχό περνάμε αργότερα, όταν έχετε καταλάβει πώς συμπεριφέρεται ο πηλός.", "Of course. The Wednesday group is for beginners. In the first month we work only with our hands, making bowls and small vases with the coil method. We move on to the wheel later, once you've understood how the clay behaves."),
  L("Πελάτης", "m", "Κι αυτά που φτιάχνουμε, τα παίρνουμε σπίτι;", "And the things we make, do we take them home?"),
  L("Κεραμίστρια", "f", "Ναι, αλλά όχι αμέσως. Πρέπει πρώτα να στεγνώσουν καλά, μετά τα ψήνουμε στον φούρνο, τα σμαλτώνετε εσείς και ακολουθεί δεύτερο ψήσιμο. Συνολικά παίρνει περίπου τρεις εβδομάδες. Το κόστος είναι ογδόντα ευρώ τον μήνα, και τα υλικά και τα ψησίματα περιλαμβάνονται. Φέρτε μόνο ρούχα που δεν σας πειράζει να λερωθούν.", "Yes, but not right away. First they must dry well, then we fire them in the kiln, you glaze them yourself and there's a second firing. Altogether it takes about three weeks. The cost is eighty euros a month, and materials and firings are included. Just bring clothes you don't mind getting dirty."),
 ],
 "questions": [
  Q("Τι κάνουν οι αρχάριοι τον πρώτο μήνα;", ["Δουλεύουν αμέσως στον τροχό", "Δουλεύουν μόνο με τα χέρια", "Ζωγραφίζουν έτοιμα αντικείμενα", "Παρακολουθούν θεωρία"], 1, "Τον πρώτο μήνα δουλεύουμε μόνο με τα χέρια"),
  Q("Γιατί δεν παίρνουν αμέσως σπίτι τα έργα τους;", ["Γιατί μένουν για έκθεση", "Γιατί πρέπει να στεγνώσουν και να ψηθούν δύο φορές", "Γιατί πρέπει πρώτα να πληρώσουν", "Γιατί τα κρατάει η δασκάλα για βαθμολογία"], 1, "Πρέπει πρώτα να στεγνώσουν καλά, μετά τα ψήνουμε"),
  Q("Τι περιλαμβάνει το μηνιαίο κόστος;", ["Μόνο τα μαθήματα", "Τα υλικά και τα ψησίματα", "Μια ποδιά εργασίας", "Έναν δικό σας τροχό"], 1, "τα υλικά και τα ψησίματα περιλαμβάνονται"),
 ],
 "gloss": {"κεραμικής": "κεραμική — pottery, ceramics", "πηλό": "πηλός — clay", "αρχάριους": "αρχάριος — beginner", "μπολ": "μπολ — bowl", "κορδονιών": "κορδόνι — cord, coil", "τροχό": "τροχός — (potter's) wheel", "συμπεριφέρεται": "συμπεριφέρομαι — to behave", "να στεγνώσουν": "στεγνώνω — to dry", "φούρνο": "φούρνος — oven, kiln", "σμαλτώνετε": "σμαλτώνω — to glaze", "ψήσιμο": "ψήσιμο — firing, baking", "να λερωθούν": "λερώνομαι — to get dirty"},
})

ITEMS.append({
 "id": "l35-dia-oinopoieio", "title": "Σε ένα οινοποιείο της Νεμέας", "title_en": "At a winery in Nemea", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο ανάμεσα σε μια επισκέπτρια και έναν οινοποιό σε ένα οινοποιείο της Νεμέας.",
 "script": [
  L("Επισκέπτρια", "f", "Ευχαριστούμε για την ξενάγηση. Μου έκανε εντύπωση ότι όλα τα κόκκινα κρασιά σας είναι από ένα μόνο σταφύλι.", "Thank you for the tour. I was struck that all your red wines are from a single grape."),
  L("Οινοποιός", "m", "Ναι, το Αγιωργίτικο, η ποικιλία της Νεμέας. Το ενδιαφέρον είναι ότι από το ίδιο σταφύλι βγαίνουν πολύ διαφορετικά κρασιά, ανάλογα με το υψόμετρο. Τα αμπέλια στον κάμπο δίνουν κρασί πιο φρουτώδες, για να το πιείτε νέο, ενώ από τις πλαγιές, στα εξακόσια, οκτακόσια μέτρα, βγάζουμε κρασιά που αντέχουν χρόνια στο βαρέλι.", "Yes, Agiorgitiko, the Nemea variety. The interesting thing is that very different wines come from the same grape, depending on the altitude. The vineyards on the plain give a fruitier wine, to drink young, while from the slopes, at six or eight hundred metres, we make wines that can age for years in the barrel."),
  L("Επισκέπτρια", "f", "Και ο τρύγος πότε γίνεται; Θα ήθελα πολύ να έρθω να βοηθήσω.", "And when is the harvest? I'd really like to come and help."),
  L("Οινοποιός", "m", "Συνήθως από τα τέλη Αυγούστου ως τα μέσα Σεπτεμβρίου, αλλά τα τελευταία χρόνια, με τη ζέστη, αρχίζουμε όλο και νωρίτερα. Κάθε Σεπτέμβριο κάνουμε ένα Σαββατοκύριακο ανοιχτού τρύγου· μαζεύετε το πρωί, και το μεσημέρι τρώμε όλοι μαζί κάτω από τις ελιές. Αφήστε μας το τηλέφωνό σας και θα σας ειδοποιήσουμε.", "Usually from the end of August to mid-September, but in recent years, with the heat, we start earlier and earlier. Every September we hold an open-harvest weekend; you pick in the morning, and at midday we all eat together under the olive trees. Leave us your phone number and we'll let you know."),
 ],
 "questions": [
  Q("Τι έκανε εντύπωση στην επισκέπτρια;", ["Η τιμή των κρασιών", "Ότι όλα τα κόκκινα κρασιά είναι από ένα σταφύλι", "Το μέγεθος του οινοποιείου", "Ότι δεν φτιάχνουν λευκό κρασί"], 1, "όλα τα κόκκινα κρασιά σας είναι από ένα μόνο σταφύλι"),
  Q("Από τι εξαρτάται, κατά τον οινοποιό, ο χαρακτήρας του κρασιού;", ["Από το είδος του βαρελιού", "Από το υψόμετρο του αμπελιού", "Από την ηλικία του οινοποιού", "Από τον μήνα της εμφιάλωσης"], 1, "ανάλογα με το υψόμετρο"),
  Q("Τι έχει αλλάξει τα τελευταία χρόνια;", ["Ο τρύγος γίνεται με μηχανήματα", "Ο τρύγος αρχίζει νωρίτερα λόγω ζέστης", "Δεν επιτρέπονται πια επισκέπτες", "Φυτεύουν ξένες ποικιλίες"], 1, "με τη ζέστη, αρχίζουμε όλο και νωρίτερα"),
 ],
 "gloss": {"οινοποιείο": "οινοποιείο — winery", "οινοποιό": "οινοποιός — winemaker", "ξενάγηση": "ξενάγηση — guided tour", "σταφύλι": "σταφύλι — grape", "ποικιλία": "ποικιλία — variety", "υψόμετρο": "υψόμετρο — altitude", "αμπέλια": "αμπέλι — vineyard", "φρουτώδες": "φρουτώδης — fruity", "πλαγιές": "πλαγιά — slope", "βαρέλι": "βαρέλι — barrel", "τρύγος": "τρύγος — grape harvest", "θα σας ειδοποιήσουμε": "ειδοποιώ — to notify"},
})

ITEMS.append({
 "id": "l35-mono-chania", "title": "Ένα βιβλιοπωλείο στα Χανιά", "title_en": "A bookshop in Chania", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλάει για τη ζωή της στα Χανιά.",
 "script": [
  L("Αριάδνη", "f", "Ήρθα στα Χανιά πριν από δώδεκα χρόνια για ένα καλοκαίρι, για να δουλέψω σε ένα ξενοδοχείο. Στο τέλος του Σεπτεμβρίου δεν μπορούσα να φανταστώ τον εαυτό μου πίσω στην Αθήνα, και έτσι έμεινα. Δύο χρόνια αργότερα άνοιξα ένα μικρό βιβλιοπωλείο σε ένα στενό της παλιάς πόλης, κοντά στο ενετικό λιμάνι.", "I came to Chania twelve years ago for one summer, to work in a hotel. At the end of September I couldn't imagine myself back in Athens, and so I stayed. Two years later I opened a small bookshop in a narrow street of the old town, near the Venetian harbour."),
  L("Αριάδνη", "f", "Όλοι μου έλεγαν ότι θα κλείσω σε έναν χρόνο. Τα καλοκαίρια, βέβαια, ζω από τους τουρίστες, που αγοράζουν οδηγούς και μυθιστορήματα στα αγγλικά και στα γερμανικά. Αλλά αυτό που με κράτησε είναι οι ντόπιοι. Κάθε Πέμπτη το βράδυ μαζευόμαστε μια λέσχη ανάγνωσης, δεκαπέντε άτομα, από φοιτητές του Πολυτεχνείου μέχρι συνταξιούχους.", "Everyone told me I'd close within a year. In the summers, of course, I live off the tourists, who buy guidebooks and novels in English and German. But what kept me going is the locals. Every Thursday evening a reading club gathers, fifteen people, from Polytechnic students to pensioners."),
  L("Αριάδνη", "f", "Το δυσκολότερο είναι το ενοίκιο. Με τις βραχυχρόνιες μισθώσεις, οι τιμές στην παλιά πόλη έχουν ανέβει τόσο, που πολλά μαγαζάκια σαν το δικό μου έχουν κλείσει. Αν χρειαστεί, θα μετακομίσω σε μια γειτονιά πιο έξω. Το βιβλιοπωλείο δεν είναι οι τοίχοι· είναι οι άνθρωποι που έρχονται.", "The hardest thing is the rent. With short-term lets, prices in the old town have risen so much that many little shops like mine have closed. If necessary, I'll move to a neighbourhood further out. The bookshop isn't the walls; it's the people who come."),
 ],
 "questions": [
  Q("Γιατί ήρθε αρχικά η Αριάδνη στα Χανιά;", ["Για να σπουδάσει", "Για να δουλέψει ένα καλοκαίρι σε ξενοδοχείο", "Για να ανοίξει βιβλιοπωλείο", "Για να ζήσει με την οικογένειά της"], 1, "για ένα καλοκαίρι, για να δουλέψω σε ένα ξενοδοχείο"),
  Q("Τι λέει ότι κράτησε ανοιχτό το βιβλιοπωλείο;", ["Οι τουρίστες του καλοκαιριού", "Οι ντόπιοι πελάτες και η λέσχη ανάγνωσης", "Μια κρατική επιδότηση", "Οι διαδικτυακές πωλήσεις"], 1, "αυτό που με κράτησε είναι οι ντόπιοι"),
  Q("Ποιο είναι το μεγαλύτερο πρόβλημά της σήμερα;", ["Ο ανταγωνισμός από μεγάλα βιβλιοπωλεία", "Το ψηλό ενοίκιο λόγω βραχυχρόνιων μισθώσεων", "Η έλλειψη πελατών τον χειμώνα", "Η κούραση"], 1, "Το δυσκολότερο είναι το ενοίκιο"),
 ],
 "gloss": {"βιβλιοπωλείο": "βιβλιοπωλείο — bookshop", "ενετικό": "ενετικός — Venetian", "οδηγούς": "οδηγός — guidebook", "μυθιστορήματα": "μυθιστόρημα — novel", "ντόπιοι": "ντόπιος — local", "λέσχη ανάγνωσης": "λέσχη ανάγνωσης — reading club", "συνταξιούχους": "συνταξιούχος — pensioner", "ενοίκιο": "ενοίκιο — rent", "βραχυχρόνιες μισθώσεις": "βραχυχρόνια μίσθωση — short-term let", "θα μετακομίσω": "μετακομίζω — to move house"},
})

ITEMS.append({
 "id": "l35-rep-kazania", "title": "Τα καζάνια του τσίπουρου", "title_en": "The tsipouro stills", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από ένα χωριό της Θεσσαλίας την εποχή της απόσταξης.",
 "script": [
  L("Δημοσιογράφος", "f", "Είναι Νοέμβριος, και στα χωριά γύρω από τον Τύρναβο η μυρωδιά από τα καζάνια γεμίζει τους δρόμους. Μετά τον τρύγο και το κρασί, έρχεται η σειρά των στέμφυλων, δηλαδή των φλουδών και των κουκουτσιών του σταφυλιού, που αποστάζονται για να γίνουν τσίπουρο.", "It is November, and in the villages around Tyrnavos the smell from the stills fills the streets. After the harvest and the wine, it's the turn of the pomace, that is the skins and seeds of the grape, which are distilled to become tsipouro."),
  L("Καζανάρης", "m", "Το καζάνι είναι δικό μου, αλλά έρχονται εδώ οι αμπελουργοί του χωριού, ο καθένας με τα δικά του στέμφυλα, και βγάζουν το τσίπουρο της χρονιάς τους. Παίρνουν άδεια για συγκεκριμένες μέρες και πληρώνουν φόρο για κάθε λίτρο. Το πρώτο που τρέχει από τον λουλά είναι πολύ δυνατό, δεν πίνεται· το μαζεύουμε χωριστά.", "The still is mine, but the village winegrowers come here, each with his own pomace, and make their tsipouro for the year. They get a licence for specific days and pay tax on every litre. The first that runs from the spout is very strong and can't be drunk; we collect it separately."),
  L("Δημοσιογράφος", "f", "Τα καζανέματα όμως δεν είναι μόνο δουλειά. Γύρω από τη φωτιά στήνονται τραπέζια, ψήνονται κάστανα και λουκάνικα, και η απόσταξη, που κρατάει όλη τη νύχτα, γίνεται γιορτή για όλο το χωριό. Τα τελευταία χρόνια μάλιστα έρχονται και επισκέπτες από τις πόλεις, για να ζήσουν από κοντά μια παράδοση αιώνων.", "But the distilling sessions aren't only work. Tables are set up around the fire, chestnuts and sausages are roasted, and the distillation, which lasts all night, becomes a celebration for the whole village. In recent years visitors even come from the cities, to experience at first hand a centuries-old tradition."),
 ],
 "questions": [
  Q("Από τι φτιάχνεται το τσίπουρο, σύμφωνα με το ρεπορτάζ;", ["Από φρέσκο χυμό σταφυλιού", "Από τα στέμφυλα, δηλαδή φλούδες και κουκούτσια", "Από σύκα και κάστανα", "Από παλιό κρασί"], 1, "των φλουδών και των κουκουτσιών του σταφυλιού"),
  Q("Τι ισχύει για τους αμπελουργούς που φέρνουν τα στέμφυλα;", ["Πουλάνε τα στέμφυλα στον καζανάρη", "Παίρνουν άδεια για συγκεκριμένες μέρες και πληρώνουν φόρο", "Αποστάζουν χωρίς κανέναν έλεγχο", "Χρησιμοποιούν όλοι το ίδιο καζάνι μία μέρα τον χρόνο"], 1, "Παίρνουν άδεια για συγκεκριμένες μέρες και πληρώνουν φόρο"),
  Q("Πώς περιγράφονται τα καζανέματα;", ["Ως μια μοναχική, κουραστική δουλειά", "Ως γιορτή για όλο το χωριό", "Ως παράδοση που χάνεται", "Ως τουριστική παράσταση"], 1, "γίνεται γιορτή για όλο το χωριό"),
 ],
 "gloss": {"καζάνια": "καζάνι — still, cauldron", "Τύρναβο": "Τύρναβος — Tyrnavos (town in Thessaly)", "στέμφυλων": "στέμφυλα — grape pomace", "φλουδών": "φλούδα — skin, peel", "κουκουτσιών": "κουκούτσι — seed, pip", "αποστάζονται": "αποστάζομαι — to be distilled", "αμπελουργοί": "αμπελουργός — winegrower", "λουλά": "λουλάς — spout of a still", "καζανέματα": "καζάνεμα — distilling session", "κάστανα": "κάστανο — chestnut", "απόσταξη": "απόσταξη — distillation"},
})

ITEMS.append({
 "id": "l35-rep-pansilinos", "title": "Αρχαιολογικοί χώροι στο φως της πανσελήνου", "title_en": "Archaeological sites by the light of the full moon", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από την αυγουστιάτικη πανσέληνο σε έναν αρχαιολογικό χώρο.",
 "script": [
  L("Δημοσιογράφος", "m", "Απόψε είναι η πανσέληνος του Αυγούστου, και, όπως κάθε χρόνο, δεκάδες αρχαιολογικοί χώροι και μουσεία σε όλη τη χώρα μένουν ανοιχτά ως αργά το βράδυ, με ελεύθερη είσοδο. Εδώ, στο Σούνιο, η ουρά για τον ναό του Ποσειδώνα άρχισε να σχηματίζεται από τις επτά.", "Tonight is the August full moon, and, as every year, dozens of archaeological sites and museums all over the country stay open until late in the evening, with free entry. Here at Sounion, the queue for the temple of Poseidon started forming at seven."),
  L("Επισκέπτρια", "f", "Έχω δει το Σούνιο πολλές φορές το μεσημέρι, με τον ήλιο να καίει. Τώρα, με το φεγγάρι να ανεβαίνει πάνω από τη θάλασσα, είναι σαν άλλος τόπος. Έφερα και τα παιδιά μου· είναι η πρώτη φορά που βλέπουν αρχαίο ναό, και νομίζω ότι δεν θα το ξεχάσουν.", "I've seen Sounion many times at midday, with the sun burning. Now, with the moon rising over the sea, it's like another place. I brought my children too; it's the first time they've seen an ancient temple, and I don't think they'll forget it."),
  L("Δημοσιογράφος", "m", "Σε πολλούς χώρους το πρόγραμμα περιλαμβάνει και συναυλίες ή απαγγελίες ποίησης. Οι αρχαιοφύλακες πάντως ζητούν από το κοινό να μένει στα μονοπάτια και να μην αγγίζει τα μνημεία, και θυμίζουν ότι η είσοδος σταματά μία ώρα πριν κλείσει ο χώρος.", "At many sites the programme also includes concerts or poetry readings. The site guards, however, ask the public to stay on the paths and not to touch the monuments, and remind people that entry stops an hour before the site closes."),
 ],
 "questions": [
  Q("Τι γίνεται κάθε χρόνο την πανσέληνο του Αυγούστου;", ["Κλείνουν οι αρχαιολογικοί χώροι νωρίς", "Πολλοί χώροι μένουν ανοιχτοί ως αργά με ελεύθερη είσοδο", "Γίνεται μόνο μία συναυλία στο Σούνιο", "Ανοίγουν νέα μουσεία"], 1, "μένουν ανοιχτά ως αργά το βράδυ, με ελεύθερη είσοδο"),
  Q("Τι νιώθει η επισκέπτρια απόψε στο Σούνιο;", ["Ότι είναι πολύ κόσμος για να το χαρεί", "Ότι ο τόπος μοιάζει διαφορετικός με το φεγγάρι", "Ότι προτιμά το Σούνιο το μεσημέρι", "Ότι τα παιδιά βαριούνται"], 1, "είναι σαν άλλος τόπος"),
  Q("Τι ζητούν οι αρχαιοφύλακες;", ["Να μη βγάζουν φωτογραφίες", "Να μένει το κοινό στα μονοπάτια και να μην αγγίζει τα μνημεία", "Να φύγουν όλοι πριν βγει το φεγγάρι", "Να κλείνουν θέση από πριν"], 1, "να μένει στα μονοπάτια και να μην αγγίζει τα μνημεία"),
 ],
 "gloss": {"πανσέληνο": "πανσέληνος — full moon", "αρχαιολογικό χώρο": "αρχαιολογικός χώρος — archaeological site", "ελεύθερη είσοδο": "ελεύθερη είσοδος — free entry", "ουρά": "ουρά — queue", "να σχηματίζεται": "σχηματίζομαι — to form", "καίει": "καίω — to burn", "απαγγελίες": "απαγγελία — recitation", "αρχαιοφύλακες": "αρχαιοφύλακας — site guard", "μονοπάτια": "μονοπάτι — path", "να μην αγγίζει": "αγγίζω — to touch", "μνημεία": "μνημείο — monument"},
})

ITEMS.append({
 "id": "l35-int-kapetanissa", "title": "Μια καπετάνισσα στις Μικρές Κυκλάδες", "title_en": "A woman captain in the Small Cyclades", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια γυναίκα που είναι καπετάνισσα σε ένα μικρό πλοίο των Μικρών Κυκλάδων.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσο συνηθισμένο είναι να βλέπει κανείς γυναίκα στη γέφυρα ενός πλοίου;", "How common is it to see a woman on the bridge of a ship?"),
  L("Καπετάνισσα", "f", "Λιγότερο απ' όσο θα έπρεπε, αλλά περισσότερο απ' ό,τι πριν από είκοσι χρόνια. Όταν ξεκίνησα ως δόκιμη, κάποιοι επιβάτες ζητούσαν να μιλήσουν «με τον καπετάνιο». Τώρα στα νησιά με ξέρουν όλοι. Στην Ηρακλειά και στο Κουφονήσι οι γιαγιάδες μού φέρνουν γλυκά του κουταλιού.", "Less than it should be, but more than twenty years ago. When I started as a cadet, some passengers asked to speak 'to the captain'. Now on the islands everyone knows me. On Irakleia and Koufonisi the grannies bring me spoon sweets."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το δυσκολότερο κομμάτι της δουλειάς;", "What's the hardest part of the job?"),
  L("Καπετάνισσα", "f", "Ο χειμώνας. Το καλοκαίρι μεταφέρουμε τουρίστες, αλλά τον χειμώνα είμαστε η μόνη σύνδεση των νησιών με τη Νάξο. Φέρνουμε το ψωμί, τα φάρμακα, τον γιατρό, τα παιδιά που πηγαίνουν στο λύκειο. Όταν φυσάει εννιά μποφόρ και πρέπει να αποφασίσω αν θα βγούμε ή όχι, ξέρω ότι από μένα εξαρτάται αν ένα νησί θα μείνει αποκομμένο. Αυτή η ευθύνη δεν σε αφήνει να κοιμηθείς.", "Winter. In summer we carry tourists, but in winter we are the islands' only link with Naxos. We bring the bread, the medicines, the doctor, the children who go to the upper secondary school. When it's blowing force nine and I have to decide whether we go out or not, I know that it depends on me whether an island will be cut off. That responsibility doesn't let you sleep."),
 ],
 "questions": [
  Q("Πώς έχει αλλάξει η στάση των επιβατών απέναντί της;", ["Δεν έχει αλλάξει καθόλου", "Παλιά ζητούσαν «τον καπετάνιο», τώρα την ξέρουν όλοι", "Παλιά την ήξεραν όλοι, τώρα όχι", "Οι επιβάτες παραπονιούνται συχνά"], 1, "Τώρα στα νησιά με ξέρουν όλοι"),
  Q("Τι ρόλο παίζει το πλοίο τον χειμώνα;", ["Μεταφέρει κυρίως τουρίστες", "Είναι η μόνη σύνδεση των νησιών με τη Νάξο", "Δεν ταξιδεύει καθόλου", "Κάνει μόνο ταξίδια για ψάρεμα"], 1, "τον χειμώνα είμαστε η μόνη σύνδεση των νησιών με τη Νάξο"),
  Q("Τι της προκαλεί τη μεγαλύτερη ανησυχία;", ["Η χαμηλή αμοιβή", "Η απόφαση αν θα ταξιδέψουν με κακοκαιρία", "Οι απαιτητικοί τουρίστες", "Η συντήρηση του πλοίου"], 1, "πρέπει να αποφασίσω αν θα βγούμε ή όχι"),
 ],
 "gloss": {"καπετάνισσα": "καπετάνισσα — woman captain", "γέφυρα": "γέφυρα — bridge (of a ship)", "δόκιμη": "δόκιμος — cadet", "επιβάτες": "επιβάτης — passenger", "γλυκά του κουταλιού": "γλυκό του κουταλιού — spoon sweet", "σύνδεση": "σύνδεση — link, connection", "λύκειο": "λύκειο — upper secondary school", "μποφόρ": "μποφόρ — Beaufort (wind force)", "αποκομμένο": "αποκομμένος — cut off", "ευθύνη": "ευθύνη — responsibility"},
})

ITEMS.append({
 "id": "l35-mono-algorithmoi", "title": "Οι αλγόριθμοι και η ενημέρωσή μας", "title_en": "Algorithms and how we get our news", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε έναν καθηγητή επικοινωνίας να μιλάει σε μια διάλεξη για τα μέσα κοινωνικής δικτύωσης και την ενημέρωση.",
 "script": [
  L("Καθηγητής", "m", "Για τους περισσότερους νέους σήμερα, η πρώτη επαφή με την επικαιρότητα δεν είναι μια εφημερίδα ούτε ένα δελτίο ειδήσεων, αλλά η ροή μιας εφαρμογής στο κινητό. Και η ροή αυτή δεν είναι ουδέτερη. Την καθορίζουν αλγόριθμοι, σχεδιασμένοι με έναν βασικό στόχο: να μας κρατούν όσο το δυνατόν περισσότερη ώρα μπροστά στην οθόνη.", "For most young people today, the first contact with current affairs is not a newspaper or a news bulletin, but the feed of an app on their phone. And that feed is not neutral. It is determined by algorithms designed with one basic aim: to keep us in front of the screen for as long as possible."),
  L("Καθηγητής", "m", "Επειδή το περιεχόμενο που προκαλεί θυμό ή φόβο κρατάει την προσοχή μας περισσότερο από το ψύχραιμο και τεκμηριωμένο, οι αλγόριθμοι τείνουν, χωρίς κανείς να το έχει αποφασίσει ρητά, να το προβάλλουν περισσότερο. Έχει γίνει πολύς λόγος για τις λεγόμενες «φούσκες φίλτρων», δηλαδή για το ότι βλέπουμε μόνο απόψεις που επιβεβαιώνουν τις δικές μας.", "Because content that provokes anger or fear holds our attention more than calm, well-documented content, algorithms tend, without anyone having explicitly decided it, to promote it more. There has been much talk of so-called 'filter bubbles', that is, that we see only opinions that confirm our own."),
  L("Καθηγητής", "m", "Οφείλω πάντως να σας πω ότι η έρευνα εδώ είναι λιγότερο ξεκάθαρη απ' όσο υποθέτει ο δημόσιος διάλογος. Αρκετές μελέτες δείχνουν ότι οι χρήστες των μέσων κοινωνικής δικτύωσης έρχονται σε επαφή με περισσότερες, όχι λιγότερες, αντίθετες απόψεις από όσους δεν τα χρησιμοποιούν. Το πρόβλημα, ίσως, δεν είναι ότι δεν βλέπουμε την άλλη πλευρά, αλλά ότι τη βλέπουμε σχεδόν πάντα στην πιο ακραία και προκλητική εκδοχή της.", "I must tell you, however, that the research here is less clear-cut than public debate assumes. Several studies show that social media users come into contact with more, not fewer, opposing views than those who don't use them. The problem, perhaps, is not that we don't see the other side, but that we almost always see it in its most extreme and provocative version."),
  L("Καθηγητής", "m", "Τι μπορούμε λοιπόν να κάνουμε; Η απάντηση δεν είναι να πετάξουμε τα κινητά μας. Είναι να αποκτήσουμε αυτό που ονομάζουμε ψηφιακό γραμματισμό: να ρωτάμε ποιος παρήγαγε μια είδηση, γιατί μας εμφανίζεται εκείνη τη στιγμή και τι συναίσθημα προσπαθεί να μας προκαλέσει.", "So what can we do? The answer is not to throw away our phones. It is to acquire what we call digital literacy: to ask who produced a piece of news, why it appears to us at that moment, and what emotion it is trying to provoke in us."),
 ],
 "questions": [
  Q("Ποιος είναι, κατά τον ομιλητή, ο βασικός στόχος των αλγορίθμων;", ["Να μας ενημερώνουν αντικειμενικά", "Να μας κρατούν όσο περισσότερη ώρα γίνεται στην οθόνη", "Να προωθούν συγκεκριμένα κόμματα", "Να περιορίζουν τις ψευδείς ειδήσεις"], 1, "να μας κρατούν όσο το δυνατόν περισσότερη ώρα μπροστά στην οθόνη"),
  Q("Γιατί προβάλλεται περισσότερο το περιεχόμενο που προκαλεί θυμό ή φόβο;", ["Γιατί το επιλέγουν σκόπιμα οι δημοσιογράφοι", "Γιατί κρατάει την προσοχή μας περισσότερο", "Γιατί είναι πιο φθηνό στην παραγωγή", "Γιατί το απαιτεί ο νόμος"], 1, "κρατάει την προσοχή μας περισσότερο από το ψύχραιμο και τεκμηριωμένο"),
  Q("Τι λέει ο ομιλητής για τις «φούσκες φίλτρων»;", ["Ότι έχουν αποδειχθεί πέρα από κάθε αμφιβολία", "Ότι η έρευνα είναι λιγότερο ξεκάθαρη απ' όσο πιστεύεται", "Ότι αφορούν μόνο τους ηλικιωμένους", "Ότι δεν έχουν μελετηθεί καθόλου"], 1, "η έρευνα εδώ είναι λιγότερο ξεκάθαρη απ' όσο υποθέτει ο δημόσιος διάλογος"),
  Q("Ποια λύση προτείνει;", ["Να σταματήσουμε να χρησιμοποιούμε κινητά", "Να αποκτήσουμε ψηφιακό γραμματισμό", "Να απαγορευτούν οι αλγόριθμοι", "Να διαβάζουμε μόνο έντυπες εφημερίδες"], 1, "Είναι να αποκτήσουμε αυτό που ονομάζουμε ψηφιακό γραμματισμό"),
 ],
 "gloss": {"επικαιρότητα": "επικαιρότητα — current affairs", "δελτίο ειδήσεων": "δελτίο ειδήσεων — news bulletin", "ροή": "ροή — feed, flow", "ουδέτερη": "ουδέτερος — neutral", "Την καθορίζουν": "καθορίζω — to determine", "ψύχραιμο": "ψύχραιμος — calm", "τεκμηριωμένο": "τεκμηριωμένος — well-documented", "ρητά": "ρητά — explicitly", "να το προβάλλουν": "προβάλλω — to promote, display", "φούσκες φίλτρων": "φούσκα φίλτρων — filter bubble", "επιβεβαιώνουν": "επιβεβαιώνω — to confirm", "προκλητική": "προκλητικός — provocative", "εκδοχή": "εκδοχή — version", "ψηφιακό γραμματισμό": "ψηφιακός γραμματισμός — digital literacy"},
})

ITEMS.append({
 "id": "l35-int-leipsydria", "title": "Το νερό της Αθήνας", "title_en": "Athens' water", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν υδρολόγο για το πρόβλημα της λειψυδρίας στην Αττική.",
 "script": [
  L("Δημοσιογράφος", "f", "Τα τελευταία χρόνια ακούμε όλο και συχνότερα ότι τα αποθέματα νερού της Αθήνας μειώνονται ανησυχητικά. Πόσο σοβαρή είναι η κατάσταση;", "In recent years we hear more and more often that Athens' water reserves are falling alarmingly. How serious is the situation?"),
  L("Υδρολόγος", "m", "Σοβαρή, αλλά όχι απρόβλεπτη. Η Αθήνα υδροδοτείται κυρίως από τους ταμιευτήρες του Μόρνου και του Ευήνου, που βρίσκονται πολύ μακριά, στη Στερεά Ελλάδα, καθώς και από την Υλίκη και τον Μαραθώνα. Μετά από αρκετούς χειμώνες με λίγες βροχές και χιόνια, η στάθμη τους έπεσε σε επίπεδα που είχαμε να δούμε από τις αρχές της δεκαετίας του ενενήντα.", "Serious, but not unforeseeable. Athens is supplied mainly by the Mornos and Evinos reservoirs, which are very far away, in Central Greece, as well as by Yliki and Marathon. After several winters with little rain and snow, their level fell to levels we hadn't seen since the early nineties."),
  L("Δημοσιογράφος", "f", "Τι μπορεί να γίνει; Συζητείται η μεταφορά νερού από άλλα ποτάμια, αλλά και η αφαλάτωση.", "What can be done? Transferring water from other rivers is being discussed, as well as desalination."),
  L("Υδρολόγος", "m", "Τα μεγάλα έργα είναι πιθανότατα αναγκαία, όμως χρειάζονται χρόνια και έχουν περιβαλλοντικό κόστος για τις περιοχές από τις οποίες παίρνουμε το νερό. Η αφαλάτωση είναι λύση για τα νησιά, αλλά για μια πόλη τεσσάρων εκατομμυρίων απαιτεί τεράστια ποσά ενέργειας. Θα έλεγα ότι το φθηνότερο νερό είναι αυτό που δεν χάνουμε. Ένα σημαντικό ποσοστό χάνεται από διαρροές σε παλιούς αγωγούς, ενώ τα επεξεργασμένα λύματα, που θα μπορούσαν να ποτίζουν πάρκα και καλλιέργειες, καταλήγουν στη θάλασσα.", "Major projects are probably necessary, but they take years and carry an environmental cost for the areas we take the water from. Desalination is a solution for the islands, but for a city of four million it requires huge amounts of energy. I would say the cheapest water is the water we don't lose. A significant share is lost through leaks in old pipes, while treated wastewater, which could water parks and crops, ends up in the sea."),
  L("Δημοσιογράφος", "f", "Και ο απλός πολίτης;", "And the ordinary citizen?"),
  L("Υδρολόγος", "m", "Ο πολίτης μπορεί να βοηθήσει, και πρέπει, αλλά δεν θα ήθελα να μεταθέσουμε την ευθύνη στα ντους των νοικοκυριών. Η γεωργία καταναλώνει στη χώρα μας το μεγαλύτερο μέρος του νερού. Χωρίς σύγχρονα αρδευτικά συστήματα, όσο κι αν κλείνουμε τη βρύση όταν βουρτσίζουμε τα δόντια μας, το πρόβλημα δεν θα λυθεί.", "Citizens can help, and must, but I wouldn't want us to shift the responsibility onto households' showers. Agriculture consumes the largest share of water in our country. Without modern irrigation systems, however much we turn off the tap when we brush our teeth, the problem won't be solved."),
 ],
 "questions": [
  Q("Πώς χαρακτηρίζει ο υδρολόγος την κατάσταση;", ["Ως απρόβλεπτη καταστροφή", "Ως σοβαρή, αλλά όχι απρόβλεπτη", "Ως υπερβολή των μέσων ενημέρωσης", "Ως πρόβλημα που έχει ήδη λυθεί"], 1, "Σοβαρή, αλλά όχι απρόβλεπτη"),
  Q("Ποιο είναι το βασικό μειονέκτημα της αφαλάτωσης για την Αθήνα;", ["Ότι το νερό δεν πίνεται", "Ότι απαιτεί τεράστια ποσά ενέργειας", "Ότι απαγορεύεται από την ΕΕ", "Ότι η Αθήνα δεν έχει θάλασσα"], 1, "απαιτεί τεράστια ποσά ενέργειας"),
  Q("Τι εννοεί λέγοντας «το φθηνότερο νερό είναι αυτό που δεν χάνουμε»;", ["Ότι πρέπει να αυξηθεί η τιμή του νερού", "Ότι πρέπει να περιοριστούν οι διαρροές και να αξιοποιηθούν τα λύματα", "Ότι πρέπει να χτιστούν νέοι ταμιευτήρες", "Ότι το εμφιαλωμένο νερό είναι ακριβό"], 1, "Ένα σημαντικό ποσοστό χάνεται από διαρροές σε παλιούς αγωγούς"),
  Q("Γιατί δεν θέλει να επικεντρωθεί η ευθύνη στα νοικοκυριά;", ["Γιατί τα νοικοκυριά δεν πληρώνουν νερό", "Γιατί η γεωργία καταναλώνει το μεγαλύτερο μέρος του νερού", "Γιατί οι πολίτες κάνουν ήδη ό,τι μπορούν", "Γιατί τα ντους δεν καταναλώνουν νερό"], 1, "Η γεωργία καταναλώνει στη χώρα μας το μεγαλύτερο μέρος του νερού"),
 ],
 "gloss": {"υδρολόγο": "υδρολόγος — hydrologist", "λειψυδρίας": "λειψυδρία — water shortage", "αποθέματα": "απόθεμα — reserve, stock", "ανησυχητικά": "ανησυχητικά — alarmingly", "απρόβλεπτη": "απρόβλεπτος — unforeseeable", "υδροδοτείται": "υδροδοτούμαι — to be supplied with water", "ταμιευτήρες": "ταμιευτήρας — reservoir", "στάθμη": "στάθμη — level", "αφαλάτωση": "αφαλάτωση — desalination", "διαρροές": "διαρροή — leak", "αγωγούς": "αγωγός — pipe", "επεξεργασμένα λύματα": "επεξεργασμένα λύματα — treated wastewater", "να μεταθέσουμε": "μεταθέτω — to shift", "αρδευτικά": "αρδευτικός — irrigation (adj.)"},
})

rnd = random.Random(35)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-35.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
