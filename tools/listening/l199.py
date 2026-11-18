# Source for library/listening/listening-199.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l199.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l199-ann-faros-anoiktos", "title": "Ο φάρος ανοίγει για το κοινό", "title_en": "The lighthouse opens to the public", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στο λιμάνι ενός νησιού.",
 "script": [
  L("Εκφωνήτρια", "f", "Ανακοίνωση του Λιμεναρχείου. Το Σάββατο και την Κυριακή ο φάρος στο ακρωτήρι θα είναι ανοιχτός για το κοινό, από τις δέκα το πρωί ως τη δύση του ηλίου. Είναι η μόνη φορά μέσα στη χρονιά που οι επισκέπτες μπορούν να ανέβουν στον πύργο και να δουν από κοντά τον μηχανισμό του φακού.", "An announcement from the Port Authority. On Saturday and Sunday the lighthouse on the cape will be open to the public, from ten in the morning until sunset. It is the only time in the year when visitors can climb the tower and see the lens mechanism up close."),
  L("Εκφωνήτρια", "f", "Η είσοδος είναι δωρεάν, αλλά στον πύργο μπορούν να βρίσκονται ταυτόχρονα μόνο δέκα άτομα. Γι' αυτό οι επισκέπτες θα μπαίνουν σε ομάδες, κάθε είκοσι λεπτά. Η σκάλα είναι στενή και απότομη, και δεν συνιστάται σε άτομα με προβλήματα καρδιάς ή σε παιδιά κάτω των οχτώ ετών.", "Entry is free, but only ten people can be in the tower at the same time. For that reason visitors will go in in groups, every twenty minutes. The staircase is narrow and steep, and is not recommended for people with heart problems or for children under eight."),
  L("Εκφωνήτρια", "f", "Δεν υπάρχει χώρος στάθμευσης κοντά στον φάρο. Συνιστούμε να έρθετε με το δημοτικό λεωφορείο, που θα κάνει έκτακτα δρομολόγια από την πλατεία κάθε μισή ώρα.", "There is no parking near the lighthouse. We recommend coming by the municipal bus, which will run extra services from the square every half hour."),
 ],
 "questions": [
  Q("Πόσο συχνά ανοίγει ο φάρος για το κοινό;", ["Κάθε Σαββατοκύριακο", "Μία φορά τον χρόνο", "Κάθε καλοκαίρι", "Μόνο για σχολεία"], 1, "Είναι η μόνη φορά μέσα στη χρονιά"),
  Q("Γιατί οι επισκέπτες θα μπαίνουν σε ομάδες;", ["Για να έχουν ξεναγό", "Γιατί στον πύργο χωρούν ταυτόχρονα μόνο δέκα άτομα", "Γιατί πληρώνουν εισιτήριο", "Γιατί κλείνει νωρίς"], 1, "στον πύργο μπορούν να βρίσκονται ταυτόχρονα μόνο δέκα άτομα"),
  Q("Πώς συνιστάται να έρθουν οι επισκέπτες;", ["Με το αυτοκίνητο", "Με τα πόδια από το λιμάνι", "Με το δημοτικό λεωφορείο", "Με ταξί"], 2, "να έρθετε με το δημοτικό λεωφορείο"),
 ],
 "gloss": {"Λιμεναρχείου": "λιμεναρχείο — port authority", "ακρωτήρι": "ακρωτήρι — cape", "φακού": "φακός — lens", "απότομη": "απότομος — steep", "έκτακτα": "έκτακτος — extra, special"},
})

ITEMS.append({
 "id": "l199-int-ekpaideftria-odigon", "title": "Η εκπαιδεύτρια οδηγών", "title_en": "The driving instructor", "type": "interview", "level": "B2",
 "context_el": "Συνέντευξη με μια εκπαιδεύτρια οδηγών που δουλεύει σε μια σχολή οδηγών στον Βόλο.",
 "script": [
  L("Δημοσιογράφος", "m", "Ποιοι μαθητές είναι οι πιο δύσκολοι;", "Which learners are the most difficult?"),
  L("Εκπαιδεύτρια", "f", "Όχι αυτοί που φαντάζεστε. Οι δεκαοχτάχρονοι μαθαίνουν γρήγορα, γιατί δεν φοβούνται. Οι πιο δύσκολοι είναι όσοι έχουν οδηγήσει «λίγο» με τον πατέρα τους σε κάποιο χωράφι. Έρχονται με κακές συνήθειες και είναι σίγουροι ότι τα ξέρουν όλα. Πρώτα πρέπει να ξεμάθουν και μετά να μάθουν.", "Not the ones you'd imagine. Eighteen-year-olds learn quickly, because they aren't afraid. The most difficult are those who've driven 'a bit' with their father in some field. They come with bad habits and are sure they know it all. First they have to unlearn and then learn."),
  L("Δημοσιογράφος", "m", "Έχετε μαθητές μεγαλύτερης ηλικίας;", "Do you have older learners?"),
  L("Εκπαιδεύτρια", "f", "Αρκετούς, και τους αγαπώ ιδιαίτερα. Πέρσι είχα μια κυρία εβδομήντα ενός χρονών που έμεινε χήρα και δεν ήθελε να εξαρτάται από τα παιδιά της για να πάει στο χωριό. Χρειάστηκε σαράντα μαθήματα αντί για είκοσι, αλλά πέρασε με την πρώτη. Την ημέρα της εξέτασης έφερε γλυκό του κουταλιού για όλη τη σχολή.", "Quite a few, and I'm especially fond of them. Last year I had a lady of seventy-one who had been widowed and didn't want to depend on her children to go to her village. She needed forty lessons instead of twenty, but she passed first time. On the day of the test she brought spoon sweets for the whole school."),
  L("Δημοσιογράφος", "m", "Τι είναι το πιο σημαντικό που προσπαθείτε να τους μάθετε;", "What's the most important thing you try to teach them?"),
  L("Εκπαιδεύτρια", "f", "Να κοιτάζουν μακριά. Οι αρχάριοι κοιτάζουν το καπό του αυτοκινήτου. Όταν μάθεις να βλέπεις τι γίνεται εκατό μέτρα μπροστά σου, προλαβαίνεις σχεδόν τα πάντα.", "To look far ahead. Beginners look at the bonnet of the car. When you learn to see what's happening a hundred metres ahead of you, you can react in time to almost everything."),
 ],
 "questions": [
  Q("Ποιοι μαθητές είναι οι πιο δύσκολοι, σύμφωνα με την εκπαιδεύτρια;", ["Οι δεκαοχτάχρονοι", "Όσοι έχουν οδηγήσει λίγο με τον πατέρα τους και έχουν κακές συνήθειες", "Οι ηλικιωμένοι", "Όσοι φοβούνται πολύ"], 1, "Έρχονται με κακές συνήθειες"),
  Q("Γιατί η κυρία των εβδομήντα ενός ήθελε να μάθει να οδηγεί;", ["Για να βρει δουλειά", "Για να μην εξαρτάται από τα παιδιά της", "Για να ταξιδέψει στο εξωτερικό", "Γιατί της το ζήτησε ο γιατρός"], 1, "δεν ήθελε να εξαρτάται από τα παιδιά της"),
  Q("Τι προσπαθεί κυρίως να μάθει στους μαθητές της;", ["Να παρκάρουν γρήγορα", "Να κοιτάζουν μακριά μπροστά τους", "Να οδηγούν αργά", "Να μη μιλούν στο κινητό"], 1, "Να κοιτάζουν μακριά"),
 ],
 "gloss": {"ξεμάθουν": "ξεμαθαίνω — to unlearn", "χήρα": "χήρα — widow", "εξαρτάται": "εξαρτώμαι — to depend", "καπό": "καπό — bonnet, hood (of a car)", "προλαβαίνεις": "προλαβαίνω — to be in time (to react)"},
})

ITEMS.append({
 "id": "l199-vm-apothikeftikos-choros", "title": "Μήνυμα από την εταιρεία αποθηκευτικών χώρων", "title_en": "A message from the self-storage company", "type": "voicemail", "level": "B2",
 "context_el": "Νοικιάζετε έναν αποθηκευτικό χώρο για τα έπιπλά σας όσο ανακαινίζεται το σπίτι σας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλησπέρα σας, από την εταιρεία αποθηκευτικών χώρων «Κλειδί» σας καλώ, για την αποθήκη 214. Η σύμβασή σας λήγει στο τέλος του μήνα. Αν θέλετε να την ανανεώσετε, μπορείτε να το κάνετε ηλεκτρονικά, και αν την ανανεώσετε για έξι μήνες, έχετε έκπτωση δεκαπέντε τοις εκατό.", "Good evening, I'm calling from the 'Kleidi' self-storage company, about unit 214. Your contract expires at the end of the month. If you'd like to renew it, you can do so online, and if you renew for six months, you get a fifteen per cent discount."),
  L("Υπάλληλος", "m", "Επίσης, σας ενημερώνω ότι από τη Δευτέρα αλλάζει το σύστημα εισόδου. Δεν θα χρειάζεστε πια την κάρτα, αλλά έναν προσωπικό κωδικό, που θα σας σταλεί με μήνυμα. Τις πρώτες μέρες θα υπάρχει υπάλληλος στην είσοδο για να βοηθάει.", "Also, I'd like to let you know that from Monday the entry system is changing. You won't need the card any more, but a personal code, which will be sent to you by text. For the first few days there'll be a member of staff at the entrance to help."),
  L("Υπάλληλος", "m", "Και κάτι τελευταίο: όταν ήρθατε την προηγούμενη φορά, αφήσατε ένα φωτιστικό στον διάδρομο, έξω από την αποθήκη σας. Το έχουμε κρατήσει στη ρεσεψιόν. Περάστε να το πάρετε όποτε σας βολεύει.", "And one last thing: when you came last time, you left a lamp in the corridor, outside your unit. We've kept it at reception. Drop by and pick it up whenever it suits you."),
 ],
 "questions": [
  Q("Τι έκπτωση παίρνει ο πελάτης αν ανανεώσει για έξι μήνες;", ["Πέντε τοις εκατό", "Δέκα τοις εκατό", "Δεκαπέντε τοις εκατό", "Έναν μήνα δωρεάν"], 2, "έχετε έκπτωση δεκαπέντε τοις εκατό"),
  Q("Τι αλλάζει από τη Δευτέρα;", ["Το ωράριο", "Το σύστημα εισόδου", "Η τιμή", "Ο αριθμός της αποθήκης"], 1, "από τη Δευτέρα αλλάζει το σύστημα εισόδου"),
  Q("Τι ξέχασε ο πελάτης την προηγούμενη φορά;", ["Την κάρτα του", "Ένα φωτιστικό στον διάδρομο", "Τα κλειδιά του", "Ένα κουτί με βιβλία"], 1, "αφήσατε ένα φωτιστικό στον διάδρομο"),
 ],
 "gloss": {"αποθηκευτικό": "αποθηκευτικός χώρος — storage unit", "ανακαινίζεται": "ανακαινίζομαι — to be renovated", "σύμβασή": "σύμβαση — contract", "ανανεώσετε": "ανανεώνω — to renew", "φωτιστικό": "φωτιστικό — lamp, light fitting"},
})

ITEMS.append({
 "id": "l199-mono-otoaspides", "title": "Κοιμάμαι με ωτοασπίδες", "title_en": "I sleep with earplugs", "type": "monologue", "level": "B2",
 "context_el": "Ένας ακροατής μιλάει σε μια ραδιοφωνική εκπομπή για τον ύπνο του.",
 "script": [
  L("Ηλίας", "m", "Μένω σε έναν κεντρικό δρόμο της Θεσσαλονίκης, στον δεύτερο όροφο. Τα πρώτα χρόνια ξυπνούσα με κάθε μηχανάκι, με κάθε απορριμματοφόρο, με κάθε παρέα που γύριζε από το μπαρ στις τρεις τα ξημερώματα. Το πρωί πήγαινα στη δουλειά σαν να μην είχα κοιμηθεί καθόλου.", "I live on a main road in Thessaloniki, on the second floor. The first few years I woke up with every motorbike, every rubbish truck, every group coming back from the bar at three in the morning. In the morning I went to work as if I hadn't slept at all."),
  L("Ηλίας", "m", "Δοκίμασα τα πάντα: διπλά τζάμια, βαριές κουρτίνες, ακόμα και μια εφαρμογή με ήχους βροχής. Στο τέλος ένας φίλος μού έδωσε ένα ζευγάρι ωτοασπίδες από σιλικόνη. Την πρώτη νύχτα ένιωθα σαν να είχα το κεφάλι μέσα σε ένα ενυδρείο. Άκουγα την καρδιά μου και την αναπνοή μου, και αυτό με ενοχλούσε περισσότερο από τον δρόμο.", "I tried everything: double glazing, heavy curtains, even an app with rain sounds. In the end a friend gave me a pair of silicone earplugs. The first night I felt as if my head was inside an aquarium. I could hear my heart and my breathing, and that bothered me more than the road."),
  L("Ηλίας", "m", "Μετά από μία εβδομάδα όμως συνήθισα. Τώρα δεν μπορώ να κοιμηθώ χωρίς αυτές, ούτε καν στο χωριό, όπου ο μόνος θόρυβος είναι ο κόκορας. Το μόνο πρόβλημα είναι το ξυπνητήρι. Έχω βάλει το κινητό να δονείται κάτω από το μαξιλάρι.", "But after a week I got used to it. Now I can't sleep without them, not even in the village, where the only noise is the rooster. The only problem is the alarm clock. I've set the phone to vibrate under the pillow."),
 ],
 "questions": [
  Q("Τι τον ξυπνούσε τα πρώτα χρόνια;", ["Ο κόκορας", "Ο θόρυβος του δρόμου", "Οι γείτονες του επάνω ορόφου", "Το ξυπνητήρι"], 1, "ξυπνούσα με κάθε μηχανάκι, με κάθε απορριμματοφόρο"),
  Q("Τι τον ενοχλούσε την πρώτη νύχτα με τις ωτοασπίδες;", ["Ότι πονούσαν τα αυτιά του", "Ότι άκουγε την καρδιά και την αναπνοή του", "Ότι έπεφταν", "Ότι άκουγε ακόμα τον δρόμο"], 1, "Άκουγα την καρδιά μου και την αναπνοή μου"),
  Q("Πώς λύνει το πρόβλημα με το ξυπνητήρι;", ["Ζητάει από κάποιον να τον ξυπνάει", "Βάζει το κινητό να δονείται κάτω από το μαξιλάρι", "Βγάζει τις ωτοασπίδες νωρίς το πρωί", "Δεν βάζει ξυπνητήρι"], 1, "Έχω βάλει το κινητό να δονείται κάτω από το μαξιλάρι"),
 ],
 "gloss": {"ωτοασπίδες": "ωτοασπίδα — earplug", "απορριμματοφόρο": "απορριμματοφόρο — rubbish truck", "ενυδρείο": "ενυδρείο — aquarium", "κόκορας": "κόκορας — rooster", "δονείται": "δονούμαι — to vibrate"},
})

ITEMS.append({
 "id": "l199-dia-thesi-sto-parathyro", "title": "Ποιος θα κάτσει στο παράθυρο;", "title_en": "Who gets the window seat?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέλφια ετοιμάζονται για ένα ταξίδι με λεωφορείο από την Αθήνα στα Γιάννενα.",
 "script": [
  L("Νεφέλη", "f", "Λοιπόν, πριν μπούμε, να το ξεκαθαρίσουμε: εγώ κάθομαι στο παράθυρο. Την προηγούμενη φορά κάθισες εσύ όλο το ταξίδι.", "Right, before we get on, let's get this straight: I'm sitting by the window. Last time you sat there the whole journey."),
  L("Οδυσσέας", "m", "Ναι, αλλά την προηγούμενη φορά ήταν νύχτα και δεν έβλεπες τίποτα. Σήμερα θα περάσουμε από τη γέφυρα Ρίου-Αντιρρίου με φως. Θέλω να τη φωτογραφίσω.", "Yes, but last time it was night and you couldn't see anything. Today we'll cross the Rio–Antirrio bridge in daylight. I want to photograph it."),
  L("Νεφέλη", "f", "Κι εγώ θέλω να τη δω. Και ξέρεις ότι ζαλίζομαι αν δεν κοιτάζω έξω. Θες να περάσω τέσσερις ώρες με μια σακούλα στο χέρι;", "I want to see it too. And you know I get travel-sick if I don't look out. Do you want me to spend four hours with a bag in my hand?"),
  L("Οδυσσέας", "m", "Καλά, καλά. Πρόταση: εσύ κάθεσαι στο παράθυρο ως τη στάση στην Αμφιλοχία, και μετά αλλάζουμε. Όταν περνάμε τη γέφυρα, μου δίνεις το κινητό σου να φωτογραφίσω από τη μεριά σου.", "All right, all right. Proposal: you sit by the window as far as the stop at Amfilochia, and then we swap. When we cross the bridge, you give me your phone so I can take a photo from your side."),
  L("Νεφέλη", "f", "Σύμφωνοι. Αλλά αν κοιμηθείς μετά την Αμφιλοχία, το παράθυρο ξαναγίνεται δικό μου.", "Deal. But if you fall asleep after Amfilochia, the window becomes mine again."),
 ],
 "questions": [
  Q("Γιατί θέλει ο Οδυσσέας να καθίσει στο παράθυρο;", ["Γιατί ζαλίζεται", "Για να φωτογραφίσει τη γέφυρα Ρίου-Αντιρρίου", "Γιατί θέλει να κοιμηθεί", "Γιατί έχει περισσότερο χώρο"], 1, "Θέλω να τη φωτογραφίσω"),
  Q("Γιατί η Νεφέλη χρειάζεται να κοιτάζει έξω;", ["Γιατί βαριέται", "Γιατί ζαλίζεται αν δεν κοιτάζει έξω", "Γιατί θέλει να δει το χωριό τους", "Γιατί δεν έχει βιβλίο"], 1, "ζαλίζομαι αν δεν κοιτάζω έξω"),
  Q("Τι συμφωνούν τελικά;", ["Να κάθεται ο Οδυσσέας στο παράθυρο όλο το ταξίδι", "Να αλλάξουν θέσεις στη στάση στην Αμφιλοχία", "Να πάρουν άλλο λεωφορείο", "Να κάθονται στο παράθυρο εναλλάξ κάθε ώρα"], 1, "εσύ κάθεσαι στο παράθυρο ως τη στάση στην Αμφιλοχία, και μετά αλλάζουμε"),
 ],
 "gloss": {"ξεκαθαρίσουμε": "ξεκαθαρίζω — to clear up, settle", "ζαλίζομαι": "ζαλίζομαι — to feel dizzy, travel-sick", "μεριά": "μεριά — side", "Σύμφωνοι": "σύμφωνος — agreed"},
})

ITEMS.append({
 "id": "l199-rep-psarades-plastika", "title": "Ψαράδες που ψαρεύουν πλαστικά", "title_en": "Fishermen who fish for plastic", "type": "report", "level": "B2",
 "context_el": "Ρεπορτάζ από μια ραδιοφωνική εκπομπή για το περιβάλλον.",
 "script": [
  L("Ρεπόρτερ", "f", "Κάθε φορά που ανεβάζουν τα δίχτυα, οι ψαράδες του μικρού λιμανιού βρίσκουν ανάμεσα στα ψάρια και κάτι άλλο: μπουκάλια, σακούλες, κομμάτια από παλιά δίχτυα. Μέχρι πριν από λίγα χρόνια τα πετούσαν πάλι στη θάλασσα. Σήμερα τα μαζεύουν σε μεγάλους σάκους.", "Every time they haul up their nets, the fishermen of the small harbour find something else among the fish: bottles, bags, pieces of old nets. Until a few years ago they threw them back into the sea. Today they collect them in big sacks."),
  L("Ρεπόρτερ", "f", "Το πρόγραμμα ξεκίνησε μια περιβαλλοντική οργάνωση, σε συνεργασία με τον δήμο. Στο λιμάνι υπάρχει ένας ειδικός κάδος, και κάθε μήνα τα πλαστικά ζυγίζονται. Οι ψαράδες δεν πληρώνονται για αυτή τη δουλειά, αλλά η οργάνωση τούς δίνει καινούργια εργαλεία και τους βοηθάει να επισκευάζουν τα δίχτυα τους.", "The programme was started by an environmental organisation, in cooperation with the municipality. In the harbour there is a special bin, and every month the plastic is weighed. The fishermen aren't paid for this work, but the organisation gives them new gear and helps them repair their nets."),
  L("Ρεπόρτερ", "f", "Μέσα σε έναν χρόνο μαζεύτηκαν πάνω από τρεις τόνοι πλαστικά. Ένα μέρος από τα παλιά δίχτυα γίνεται νήμα για ρούχα και τσάντες. Ο γηραιότερος ψαράς του λιμανιού λέει ότι στα νιάτα του έβγαζε περισσότερα ψάρια και λιγότερα σκουπίδια. «Τώρα», λέει, «τουλάχιστον καθαρίζουμε λίγο το σπίτι μας».", "Within a year more than three tonnes of plastic were collected. Part of the old nets becomes yarn for clothes and bags. The oldest fisherman in the harbour says that in his youth he brought up more fish and less rubbish. 'Now,' he says, 'at least we're cleaning our house a little.'"),
 ],
 "questions": [
  Q("Τι έκαναν παλιά οι ψαράδες με τα πλαστικά που έβρισκαν;", ["Τα πουλούσαν", "Τα πετούσαν πάλι στη θάλασσα", "Τα έδιναν στον δήμο", "Τα έκαιγαν"], 1, "τα πετούσαν πάλι στη θάλασσα"),
  Q("Τι παίρνουν οι ψαράδες για αυτή τη δουλειά;", ["Μισθό", "Καινούργια εργαλεία και βοήθεια στην επισκευή των διχτυών", "Δωρεάν καύσιμα", "Τίποτα απολύτως"], 1, "η οργάνωση τούς δίνει καινούργια εργαλεία"),
  Q("Τι γίνεται με ένα μέρος από τα παλιά δίχτυα;", ["Γίνεται νήμα για ρούχα και τσάντες", "Πηγαίνει σε μουσείο", "Χρησιμοποιείται ξανά για ψάρεμα", "Καίγεται"], 0, "Ένα μέρος από τα παλιά δίχτυα γίνεται νήμα για ρούχα και τσάντες"),
 ],
 "gloss": {"δίχτυα": "δίχτυ — fishing net", "σάκους": "σάκος — sack", "ζυγίζονται": "ζυγίζομαι — to be weighed", "νήμα": "νήμα — yarn, thread", "γηραιότερος": "γηραιότερος — oldest, eldest"},
})

ITEMS.append({
 "id": "l199-rep-mathites-girokomeio", "title": "Μαθητές διαβάζουν σε ηλικιωμένους", "title_en": "Pupils read to elderly people", "type": "report", "level": "B2",
 "context_el": "Ρεπορτάζ από την εκπομπή ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Ρεπόρτερ", "m", "Κάθε Τετάρτη μεσημέρι, μια ομάδα μαθητών του γυμνασίου περπατά δύο τετράγωνα ως το γηροκομείο της γειτονιάς. Στην αίθουσα τους περιμένουν περίπου δεκαπέντε ηλικιωμένοι, πολλοί από τους οποίους δεν βλέπουν πια καλά για να διαβάσουν μόνοι τους.", "Every Wednesday at midday, a group of secondary-school pupils walks two blocks to the neighbourhood care home. In the hall about fifteen elderly people are waiting for them, many of whom can no longer see well enough to read on their own."),
  L("Ρεπόρτερ", "m", "Τα παιδιά διαβάζουν δυνατά εφημερίδες, διηγήματα και μερικές φορές ποιήματα που διαλέγουν οι ίδιοι οι ακροατές τους. Μετά ακολουθεί συζήτηση. Μια κυρία ενενήντα χρονών διορθώνει συχνά την προφορά τους· ήταν δασκάλα για σαράντα χρόνια.", "The children read aloud newspapers, short stories and sometimes poems chosen by their listeners themselves. Then comes a discussion. A ninety-year-old lady often corrects their pronunciation; she was a teacher for forty years."),
  L("Ρεπόρτερ", "m", "Η φιλόλογος που οργάνωσε το πρόγραμμα λέει ότι οι μαθητές έγιναν πιο σίγουροι όταν μιλούν μπροστά σε κόσμο. Οι ηλικιωμένοι, από την άλλη, περιμένουν την Τετάρτη όλη την εβδομάδα. Και κάτι που δεν είχε προβλέψει κανείς: πολλοί μαθητές συνεχίζουν να επισκέπτονται τους «ακροατές» τους και στις διακοπές.", "The Greek teacher who organised the programme says the pupils have become more confident speaking in front of people. The elderly, on the other hand, wait all week for Wednesday. And something nobody had predicted: many pupils keep visiting their 'listeners' during the holidays too."),
 ],
 "questions": [
  Q("Γιατί πολλοί ηλικιωμένοι δεν διαβάζουν μόνοι τους;", ["Γιατί δεν ξέρουν γράμματα", "Γιατί δεν βλέπουν πια καλά", "Γιατί δεν έχουν βιβλία", "Γιατί βαριούνται"], 1, "δεν βλέπουν πια καλά για να διαβάσουν μόνοι τους"),
  Q("Τι κάνει η κυρία των ενενήντα χρονών;", ["Διαβάζει ποιήματα", "Διορθώνει την προφορά των μαθητών", "Φέρνει γλυκά", "Γράφει διηγήματα"], 1, "διορθώνει συχνά την προφορά τους"),
  Q("Τι δεν είχε προβλέψει κανείς;", ["Ότι θα έρχονταν τόσοι μαθητές", "Ότι πολλοί μαθητές θα συνέχιζαν τις επισκέψεις και στις διακοπές", "Ότι οι ηλικιωμένοι θα ήθελαν ποιήματα", "Ότι το πρόγραμμα θα έκλεινε"], 1, "πολλοί μαθητές συνεχίζουν να επισκέπτονται τους «ακροατές» τους και στις διακοπές"),
 ],
 "gloss": {"γηροκομείο": "γηροκομείο — care home, old people's home", "τετράγωνα": "τετράγωνο — (city) block", "διηγήματα": "διήγημα — short story", "προφορά": "προφορά — pronunciation", "προβλέψει": "προβλέπω — to foresee, predict"},
})

ITEMS.append({
 "id": "l199-news-spanio-psari", "title": "Σπάνιο ψάρι των βαθέων υδάτων στα δίχτυα ψαράδων", "title_en": "A rare deep-sea fish in fishermen's nets", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων του ραδιοφώνου.",
 "script": [
  L("Εκφωνητής", "m", "Ένα σπάνιο ψάρι των βαθέων υδάτων, με μακρύ ασημένιο σώμα και κόκκινο λοφίο, πιάστηκε χθες στα δίχτυα ψαράδων ανοιχτά της νότιας Κρήτης. Το ψάρι είχε μήκος σχεδόν τρία μέτρα και, σύμφωνα με τους ψαράδες, ήταν ήδη νεκρό όταν το ανέβασαν στο σκάφος.", "A rare deep-sea fish, with a long silver body and a red crest, was caught yesterday in fishermen's nets off southern Crete. The fish was almost three metres long and, according to the fishermen, was already dead when they brought it aboard."),
  L("Εκφωνητής", "m", "Τα ψάρια αυτού του είδους ζουν συνήθως σε βάθος εκατοντάδων μέτρων και σπάνια εμφανίζονται κοντά στην επιφάνεια. Γι' αυτό γύρω τους έχουν δημιουργηθεί πολλοί θρύλοι, ενώ κάποιοι ναυτικοί τα θεωρούσαν παλιότερα σημάδι κακοκαιρίας.", "Fish of this species usually live at depths of hundreds of metres and rarely appear near the surface. That's why many legends have grown up around them, and some sailors used to consider them a sign of bad weather."),
  L("Εκφωνητής", "m", "Οι ψαράδες ειδοποίησαν αμέσως ένα ερευνητικό ινστιτούτο, και το ψάρι μεταφέρθηκε σε εργαστήριο για μελέτη. Οι επιστήμονες ζητούν από όποιον εντοπίσει παρόμοιο ψάρι να το φωτογραφίσει και να ενημερώσει τις αρχές.", "The fishermen immediately notified a research institute, and the fish was taken to a laboratory for study. The scientists ask anyone who spots a similar fish to photograph it and inform the authorities."),
 ],
 "questions": [
  Q("Πόσο μήκος είχε το ψάρι;", ["Ένα μέτρο", "Σχεδόν τρία μέτρα", "Πέντε μέτρα", "Μισό μέτρο"], 1, "Το ψάρι είχε μήκος σχεδόν τρία μέτρα"),
  Q("Γιατί έχουν δημιουργηθεί θρύλοι γύρω από αυτά τα ψάρια;", ["Γιατί είναι επικίνδυνα", "Γιατί σπάνια εμφανίζονται κοντά στην επιφάνεια", "Γιατί είναι νόστιμα", "Γιατί είναι πολύ μικρά"], 1, "σπάνια εμφανίζονται κοντά στην επιφάνεια"),
  Q("Τι ζητούν οι επιστήμονες;", ["Να μην ψαρεύει κανείς στην περιοχή", "Να φωτογραφίζουν τα παρόμοια ψάρια και να ενημερώνουν τις αρχές", "Να τα ξαναρίχνουν στη θάλασσα", "Να τα φέρνουν στο εργαστήριο"], 1, "να το φωτογραφίσει και να ενημερώσει τις αρχές"),
 ],
 "gloss": {"βαθέων": "βαθέων υδάτων — deep-sea", "λοφίο": "λοφίο — crest", "θρύλοι": "θρύλος — legend", "κακοκαιρίας": "κακοκαιρία — bad weather", "ινστιτούτο": "ινστιτούτο — institute"},
})

ITEMS.append({
 "id": "l199-c1-mono-strogyloi-arithmoi", "title": "Γιατί οι στρογγυλοί αριθμοί μάς επηρεάζουν;", "title_en": "Why do round numbers affect us?", "type": "monologue", "level": "C1",
 "context_el": "Απόσπασμα από podcast για την ψυχολογία της καθημερινής ζωής.",
 "script": [
  L("Παρουσιάστρια", "f", "Τα τριάντα, τα σαράντα, τα πενήντα: τα γενέθλια με το μηδέν στο τέλος μοιάζουν να έχουν ένα βάρος που δεν έχουν τα τριάντα τρία ή τα σαράντα επτά. Λογικά δεν υπάρχει καμία διαφορά· είναι απλώς μια μέρα μετά την προηγούμενη. Κι όμως, οι στρογγυλοί αριθμοί λειτουργούν σαν ορόσημα, σαν μικρές γραμμές τερματισμού μέσα στη ζωή μας.", "Thirty, forty, fifty: birthdays with a zero at the end seem to carry a weight that thirty-three or forty-seven don't. Logically there's no difference; it's just one day after the previous one. And yet round numbers work like milestones, like little finishing lines within our lives."),
  L("Παρουσιάστρια", "f", "Μια γνωστή μελέτη πρότεινε μάλιστα ότι οι άνθρωποι αλλάζουν συμπεριφορά λίγο πριν από ένα τέτοιο ορόσημο, όταν η ηλικία τους τελειώνει σε εννιά. Οι ερευνητές βρήκαν, για παράδειγμα, ότι ανάμεσα σε όσους έτρεχαν τον πρώτο τους μαραθώνιο, οι εικοσιεννιάχρονοι, οι τριανταεννιάχρονοι και οι σαρανταεννιάχρονοι ήταν περισσότεροι απ' ό,τι θα περίμενε κανείς. Η ερμηνεία τους ήταν ότι η επερχόμενη αλλαγή δεκαετίας μάς κάνει να αναρωτιόμαστε αν η ζωή μας έχει νόημα.", "One well-known study even suggested that people change their behaviour just before such a milestone, when their age ends in nine. The researchers found, for example, that among people running their first marathon, twenty-nine-, thirty-nine- and forty-nine-year-olds were more numerous than one would expect. Their interpretation was that the coming change of decade makes us wonder whether our life has meaning."),
  L("Παρουσιάστρια", "f", "Η ίδια αδυναμία μας για τα στρογγυλά νούμερα εξηγεί γιατί οι τιμές στα μαγαζιά τελειώνουν σε ενενήντα εννιά λεπτά: το πρώτο ψηφίο μετράει δυσανάλογα, και τα εννιά ευρώ και ενενήντα εννιά μας φαίνονται πιο κοντά στα εννιά παρά στα δέκα. Αξίζει λοιπόν, την επόμενη φορά που θα πλησιάζουμε ένα «μεγάλο» νούμερο, να θυμηθούμε ότι το μηδέν δεν το έβαλε η φύση· το βάλαμε εμείς.", "The same weakness of ours for round numbers explains why shop prices end in ninety-nine cents: the first digit counts disproportionately, and nine euros ninety-nine seems closer to nine than to ten. So it's worth remembering, the next time we approach a 'big' number, that the zero wasn't put there by nature; we put it there."),
 ],
 "questions": [
  Q("Πώς λειτουργούν οι στρογγυλοί αριθμοί, κατά την παρουσιάστρια;", ["Σαν τυχεροί αριθμοί", "Σαν ορόσημα, μικρές γραμμές τερματισμού", "Σαν προειδοποιήσεις", "Δεν έχουν καμία επίδραση"], 1, "οι στρογγυλοί αριθμοί λειτουργούν σαν ορόσημα"),
  Q("Τι βρήκε η μελέτη για τους μαραθωνοδρόμους;", ["Ότι οι νέοι τρέχουν πιο γρήγορα", "Ότι όσοι η ηλικία τους τελείωνε σε εννιά ήταν περισσότεροι απ' ό,τι αναμενόταν", "Ότι λίγοι τρέχουν μετά τα πενήντα", "Ότι οι γυναίκες τρέχουν περισσότερο"], 1, "οι εικοσιεννιάχρονοι, οι τριανταεννιάχρονοι και οι σαρανταεννιάχρονοι ήταν περισσότεροι απ' ό,τι θα περίμενε κανείς"),
  Q("Πώς ερμήνευσαν οι ερευνητές το αποτέλεσμα;", ["Η αλλαγή δεκαετίας μάς κάνει να αναρωτιόμαστε για το νόημα της ζωής μας", "Οι άνθρωποι έχουν περισσότερο ελεύθερο χρόνο", "Οι μαραθώνιοι γίνονται πιο εύκολοι", "Οι γιατροί το συστήνουν"], 0, "η επερχόμενη αλλαγή δεκαετίας μάς κάνει να αναρωτιόμαστε αν η ζωή μας έχει νόημα"),
  Q("Γιατί οι τιμές τελειώνουν σε ενενήντα εννιά λεπτά;", ["Λόγω φόρων", "Γιατί το πρώτο ψηφίο μετράει δυσανάλογα", "Για να υπάρχουν ρέστα", "Από παλιά συνήθεια χωρίς λόγο"], 1, "το πρώτο ψηφίο μετράει δυσανάλογα"),
 ],
 "gloss": {"ορόσημα": "ορόσημο — milestone", "τερματισμού": "τερματισμός — finish (of a race)", "επερχόμενη": "επερχόμενος — forthcoming, coming", "ψηφίο": "ψηφίο — digit", "δυσανάλογα": "δυσανάλογα — disproportionately", "αδυναμία": "αδυναμία — weakness, soft spot"},
})

ITEMS.append({
 "id": "l199-c1-int-chronos-se-kindyno", "title": "Γιατί ο χρόνος μοιάζει να επιβραδύνεται όταν κινδυνεύουμε;", "title_en": "Why does time seem to slow down when we're in danger?", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με μια νευροεπιστήμονα σε μια εκπομπή για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί που έχουν ζήσει ένα τροχαίο ή μια πτώση λένε ότι όλα έγιναν «σε αργή κίνηση». Βλέπουμε πράγματι τον κόσμο πιο αργά σε τέτοιες στιγμές;", "Many people who've been through a car accident or a fall say everything happened 'in slow motion'. Do we really see the world more slowly at such moments?"),
  L("Νευροεπιστήμονας", "f", "Αυτό ακριβώς θέλησαν να ελέγξουν κάποιοι ερευνητές με ένα αρκετά τολμηρό πείραμα. Εθελοντές έπεφταν ελεύθερα από ένα ψηλό ικρίωμα σε ένα δίχτυ ασφαλείας, φορώντας στον καρπό μια μικρή οθόνη που έδειχνε αριθμούς να αναβοσβήνουν τόσο γρήγορα που, σε κανονικές συνθήκες, δεν μπορούσε κανείς να τους διαβάσει. Αν ο χρόνος πραγματικά «επιβραδυνόταν» για τον εγκέφαλο, θα έπρεπε να τους διαβάζουν κατά τη διάρκεια της πτώσης.", "That's exactly what some researchers wanted to test with a fairly daring experiment. Volunteers fell freely from a tall scaffold into a safety net, wearing on their wrist a small display that showed numbers flashing so fast that, under normal conditions, no one could read them. If time really 'slowed down' for the brain, they should have been able to read them during the fall."),
  L("Δημοσιογράφος", "m", "Και τους διάβαζαν;", "And could they read them?"),
  L("Νευροεπιστήμονας", "f", "Όχι. Η αντίληψή τους δεν είχε γίνει ταχύτερη. Όταν όμως τους ζήτησαν να εκτιμήσουν πόσο κράτησε η πτώση τους, την υπολόγισαν σημαντικά μεγαλύτερη απ' ό,τι υπολόγιζαν την πτώση των άλλων. Η εξήγηση που προτάθηκε είναι ότι η επιβράδυνση δεν συμβαίνει τη στιγμή του κινδύνου αλλά στη μνήμη. Σε μια τρομακτική κατάσταση, ο εγκέφαλος καταγράφει πολύ περισσότερες λεπτομέρειες, και όταν ανατρέχουμε σε αυτή την πυκνή ανάμνηση, μας φαίνεται ότι κράτησε περισσότερο.", "No. Their perception hadn't become faster. But when they were asked to estimate how long their fall lasted, they judged it considerably longer than they judged other people's falls. The explanation proposed is that the slowing down doesn't happen at the moment of danger but in memory. In a frightening situation, the brain records many more details, and when we go back to that dense memory, it seems to us that it lasted longer."),
  L("Δημοσιογράφος", "m", "Δηλαδή η «αργή κίνηση» είναι μια ψευδαίσθηση;", "So 'slow motion' is an illusion?"),
  L("Νευροεπιστήμονας", "f", "Είναι μια ανακατασκευή. Δεν ζήσαμε τη στιγμή πιο αργά· τη θυμόμαστε πιο πλούσια. Το ίδιο εξηγεί εν μέρει γιατί οι πρώτες μέρες σε ένα καινούργιο μέρος, γεμάτες νέες εντυπώσεις, μοιάζουν στο τέλος των διακοπών πολύ μεγαλύτερες από τις τελευταίες.", "It's a reconstruction. We didn't live the moment more slowly; we remember it more richly. The same partly explains why the first days in a new place, full of new impressions, seem much longer at the end of the holiday than the last ones."),
 ],
 "questions": [
  Q("Τι φορούσαν οι εθελοντές στον καρπό;", ["Ένα ρολόι χειρός", "Μια μικρή οθόνη με αριθμούς που αναβόσβηναν πολύ γρήγορα", "Έναν μετρητή καρδιακών παλμών", "Μια κάμερα"], 1, "μια μικρή οθόνη που έδειχνε αριθμούς να αναβοσβήνουν"),
  Q("Τι έδειξε το πείραμα για την αντίληψη;", ["Ότι γίνεται ταχύτερη σε κίνδυνο", "Ότι δεν είχε γίνει ταχύτερη", "Ότι σταματά εντελώς", "Ότι γίνεται πιο αργή"], 1, "Η αντίληψή τους δεν είχε γίνει ταχύτερη"),
  Q("Πού συμβαίνει, σύμφωνα με την εξήγηση, η «επιβράδυνση»;", ["Στα μάτια", "Στη μνήμη", "Στους μύες", "Στην καρδιά"], 1, "η επιβράδυνση δεν συμβαίνει τη στιγμή του κινδύνου αλλά στη μνήμη"),
  Q("Ποιο καθημερινό παράδειγμα δίνει στο τέλος;", ["Τις πρώτες μέρες των διακοπών που μοιάζουν μεγαλύτερες", "Την αναμονή στο γιατρό", "Τις εξετάσεις στο σχολείο", "Τα ταξίδια με αεροπλάνο"], 0, "οι πρώτες μέρες σε ένα καινούργιο μέρος, γεμάτες νέες εντυπώσεις, μοιάζουν στο τέλος των διακοπών πολύ μεγαλύτερες"),
 ],
 "gloss": {"επιβράδυνση": "επιβράδυνση — slowing down", "νευροεπιστήμονα": "νευροεπιστήμονας — neuroscientist", "τολμηρό": "τολμηρός — daring", "ικρίωμα": "ικρίωμα — scaffold", "αναβοσβήνουν": "αναβοσβήνω — to flash, blink", "ανατρέχουμε": "ανατρέχω — to go back to, refer back", "ανακατασκευή": "ανακατασκευή — reconstruction"},
})

rnd = random.Random(199)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-199.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
