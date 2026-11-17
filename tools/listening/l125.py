# Source for library/listening/listening-125.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l125.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l125-ann-asteroskopeio", "title": "Ανοιχτή βραδιά στο αστεροσκοπείο", "title_en": "An open night at the observatory", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στον τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος σας προσκαλεί την Παρασκευή το βράδυ σε μια ανοιχτή βραδιά στο αστεροσκοπείο του λόφου. Από τις οκτώ ως τα μεσάνυχτα, οι επισκέπτες θα μπορούν να παρατηρήσουν τη Σελήνη και τον Κρόνο με το μεγάλο τηλεσκόπιο, με τη βοήθεια μελών του τοπικού συλλόγου ερασιτεχνών αστρονόμων.", "The municipality invites you on Friday evening to an open night at the hilltop observatory. From eight until midnight, visitors will be able to observe the Moon and Saturn through the large telescope, with the help of members of the local amateur astronomers' club."),
  L("Εκφωνήτρια", "f", "Η είσοδος είναι ελεύθερη, αλλά λόγω του περιορισμένου χώρου απαιτείται κράτηση θέσης στην ιστοσελίδα του δήμου. Οι επισκέπτες θα χωρίζονται σε ομάδες των δεκαπέντε ατόμων, και κάθε ομάδα θα μένει στον θόλο περίπου μισή ώρα.", "Admission is free, but because of the limited space a booking is required on the municipality's website. Visitors will be divided into groups of fifteen, and each group will stay in the dome for about half an hour."),
  L("Εκφωνήτρια", "f", "Σε περίπτωση συννεφιάς, η παρατήρηση θα αντικατασταθεί από μια ομιλία για τους πλανήτες του ηλιακού μας συστήματος. Επειδή το πάρκινγκ στον λόφο είναι μικρό, συνιστάται η χρήση του δωρεάν λεωφορείου που θα ξεκινά κάθε μισή ώρα από την κεντρική πλατεία.", "If it is cloudy, the observation will be replaced by a talk on the planets of our solar system. Because the car park on the hill is small, people are advised to use the free bus that will leave every half hour from the central square."),
 ],
 "questions": [
  Q("Τι χρειάζεται για να πάει κανείς στη βραδιά;", ["Εισιτήριο από το ταμείο", "Κράτηση θέσης στην ιστοσελίδα του δήμου", "Να είναι μέλος του συλλόγου", "Δικό του τηλεσκόπιο"], 1, "απαιτείται κράτηση θέσης στην ιστοσελίδα του δήμου"),
  Q("Τι θα γίνει αν έχει συννεφιά;", ["Η βραδιά θα αναβληθεί", "Θα προβληθεί ταινία", "Θα γίνει ομιλία για τους πλανήτες", "Θα επιστραφούν τα χρήματα"], 2, "η παρατήρηση θα αντικατασταθεί από μια ομιλία για τους πλανήτες του ηλιακού μας συστήματος"),
  Q("Γιατί συνιστάται το δωρεάν λεωφορείο;", ["Γιατί το πάρκινγκ στον λόφο είναι μικρό", "Γιατί ο δρόμος είναι επικίνδυνος", "Γιατί απαγορεύονται τα αυτοκίνητα το βράδυ", "Γιατί το φως των αυτοκινήτων ενοχλεί την παρατήρηση"], 0, "το πάρκινγκ στον λόφο είναι μικρό"),
 ],
 "gloss": {"αστεροσκοπείο": "αστεροσκοπείο — observatory", "παρατηρήσουν": "παρατηρώ — to observe", "Σελήνη": "Σελήνη — the Moon", "Κρόνο": "Κρόνος — Saturn", "τηλεσκόπιο": "τηλεσκόπιο — telescope", "ερασιτεχνών": "ερασιτέχνης — amateur", "περιορισμένου": "περιορισμένος — limited", "απαιτείται": "απαιτούμαι — to be required", "θόλο": "θόλος — dome", "συννεφιάς": "συννεφιά — cloudy weather", "αντικατασταθεί": "αντικαθίσταμαι — to be replaced", "συνιστάται": "συνιστάται — it is recommended"}
})

ITEMS.append({
 "id": "l125-vm-toxovolia", "title": "Μήνυμα από τον σύλλογο τοξοβολίας", "title_en": "A message from the archery club", "type": "voicemail", "level": "B2",
 "context_el": "Γραφτήκατε πρόσφατα σε έναν σύλλογο τοξοβολίας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Γραμματέας", "f", "Γεια σας, η Μαρίνα είμαι από τον σύλλογο τοξοβολίας. Σας πήρα για το μάθημα γνωριμίας του Σαββάτου. Λόγω των έργων στο γήπεδο, το μάθημα δεν θα γίνει στο ανοιχτό πεδίο αλλά στο κλειστό γυμναστήριο του σχολείου, απέναντι από τον σύλλογο. Η ώρα μένει η ίδια, στις δέκα.", "Hello, it's Marina from the archery club. I'm calling about Saturday's introductory lesson. Because of the works at the ground, the lesson won't take place on the open range but in the school's indoor gym, opposite the club. The time stays the same, at ten."),
  L("Γραμματέας", "f", "Δεν χρειάζεται να φέρετε δικό σας εξοπλισμό· τόξα, βέλη και προστατευτικά θα σας δώσει ο σύλλογος. Φορέστε μόνο άνετα ρούχα, χωρίς φαρδιά μανίκια, γιατί μπορεί να πιαστούν στη χορδή. Επίσης, μην ξεχάσετε να φέρετε την ιατρική βεβαίωση· χωρίς αυτήν δεν μπορούμε να σας ασφαλίσουμε.", "You don't need to bring your own equipment; the club will give you bows, arrows and guards. Just wear comfortable clothes, without wide sleeves, because they can catch on the string. Also, don't forget to bring the medical certificate; without it we can't insure you."),
  L("Γραμματέας", "f", "Αν θέλετε να συνεχίσετε μετά το πρώτο μάθημα, η συνδρομή είναι τριάντα ευρώ τον μήνα. Για οποιαδήποτε ερώτηση, πάρτε με σε αυτό το νούμερο. Καλή σας μέρα!", "If you'd like to continue after the first lesson, the membership fee is thirty euros a month. For any question, call me on this number. Have a good day!"),
 ],
 "questions": [
  Q("Τι αλλάζει στο μάθημα του Σαββάτου;", ["Η ώρα", "Ο χώρος: θα γίνει στο κλειστό γυμναστήριο του σχολείου", "Ο προπονητής", "Η τιμή"], 1, "στο κλειστό γυμναστήριο του σχολείου"),
  Q("Γιατί δεν πρέπει να φορέσει κανείς φαρδιά μανίκια;", ["Γιατί κάνει ζέστη στο γυμναστήριο", "Γιατί απαγορεύεται από τον κανονισμό", "Γιατί μπορεί να πιαστούν στη χορδή", "Γιατί λερώνονται εύκολα"], 2, "μπορεί να πιαστούν στη χορδή"),
  Q("Γιατί είναι απαραίτητη η ιατρική βεβαίωση;", ["Χωρίς αυτήν ο σύλλογος δεν μπορεί να τον ασφαλίσει", "Για να πάρει έκπτωση στη συνδρομή", "Για να συμμετάσχει σε αγώνες", "Γιατί το ζητά το σχολείο"], 0, "χωρίς αυτήν δεν μπορούμε να σας ασφαλίσουμε"),
 ],
 "gloss": {"τοξοβολίας": "τοξοβολία — archery", "μάθημα γνωριμίας": "μάθημα γνωριμίας — introductory lesson", "πεδίο": "πεδίο — range, field", "γυμναστήριο": "γυμναστήριο — gym", "εξοπλισμό": "εξοπλισμός — equipment", "τόξα": "τόξο — bow", "βέλη": "βέλος — arrow", "προστατευτικά": "προστατευτικό — guard, protective gear", "φαρδιά": "φαρδύς — wide, loose", "χορδή": "χορδή — string", "ιατρική βεβαίωση": "ιατρική βεβαίωση — medical certificate", "ασφαλίσουμε": "ασφαλίζω — to insure", "συνδρομή": "συνδρομή — membership fee"}
})

ITEMS.append({
 "id": "l125-dial-agonas-dromou", "title": "Δέκα χιλιόμετρα με την εταιρεία;", "title_en": "Ten kilometres with the company?", "type": "dialogue", "level": "B2",
 "context_el": "Η Στέλλα προσπαθεί να πείσει τον συνάδελφό της, τον Άρη, να τρέξει μαζί με την ομάδα της εταιρείας σε έναν αγώνα δρόμου.",
 "script": [
  L("Στέλλα", "f", "Άρη, η εταιρεία δηλώνει ομάδα στον αγώνα δρόμου της πόλης, τον Απρίλιο. Υπάρχει διαδρομή των πέντε και των δέκα χιλιομέτρων, και για κάθε συμμετοχή η εταιρεία δίνει είκοσι ευρώ σε ένα παιδικό νοσοκομείο. Γράψου κι εσύ!", "Aris, the company is entering a team in the city's road race in April. There's a five- and a ten-kilometre route, and for every entry the company gives twenty euros to a children's hospital. Sign up too!"),
  L("Άρης", "m", "Στέλλα, εγώ τελευταία φορά έτρεξα για να προλάβω το λεωφορείο, και λαχάνιασα στα πενήντα μέτρα. Δέκα χιλιόμετρα; Θα με μαζεύουν με φορείο.", "Stella, the last time I ran was to catch the bus, and I was out of breath after fifty metres. Ten kilometres? They'll be carrying me off on a stretcher."),
  L("Στέλλα", "f", "Ποιος είπε δέκα; Ξεκίνα με τα πέντε. Έχουμε τέσσερις μήνες, και μια συνάδελφος που τρέχει μαραθώνιους θα κάνει προπονήσεις για αρχάριους δύο φορές την εβδομάδα, μετά τη δουλειά, στο πάρκο. Ακόμα και περπάτημα να κάνεις στην αρχή, μετράει.", "Who said ten? Start with the five. We have four months, and a colleague who runs marathons will do training sessions for beginners twice a week, after work, in the park. Even if you just walk at the start, it counts."),
  L("Άρης", "m", "Εντάξει, θα έρθω στην πρώτη προπόνηση. Αν αντέξω, γράφομαι για τα πέντε. Αλλά αν τερματίσω τελευταίος, θα κερνάς εσύ καφέ για έναν μήνα.", "OK, I'll come to the first training session. If I survive, I'll sign up for the five. But if I finish last, you're buying the coffee for a month."),
 ],
 "questions": [
  Q("Τι κάνει η εταιρεία για κάθε συμμετοχή;", ["Δίνει μια μέρα άδεια", "Δίνει είκοσι ευρώ σε ένα παιδικό νοσοκομείο", "Πληρώνει τα αθλητικά παπούτσια", "Δίνει μπόνους στον μισθό"], 1, "για κάθε συμμετοχή η εταιρεία δίνει είκοσι ευρώ σε ένα παιδικό νοσοκομείο"),
  Q("Τι προτείνει η Στέλλα στον Άρη;", ["Να τρέξει αμέσως τα δέκα χιλιόμετρα", "Να γραφτεί σε γυμναστήριο", "Να ξεκινήσει με τα πέντε και να πάει στις προπονήσεις για αρχάριους", "Να βοηθήσει στην οργάνωση αντί να τρέξει"], 2, "Ξεκίνα με τα πέντε"),
  Q("Τι θα γίνει αν ο Άρης τερματίσει τελευταίος;", ["Η Στέλλα θα κερνάει καφέ για έναν μήνα", "Ο Άρης θα πληρώσει δωρεά", "Θα σταματήσει τις προπονήσεις", "Θα τρέξει ξανά του χρόνου"], 0, "αν τερματίσω τελευταίος, θα κερνάς εσύ καφέ για έναν μήνα"),
 ],
 "gloss": {"συνάδελφό": "συνάδελφος — colleague", "αγώνα δρόμου": "αγώνας δρόμου — road race", "διαδρομή": "διαδρομή — route, course", "συμμετοχή": "συμμετοχή — entry, participation", "προλάβω": "προλαβαίνω — to catch (in time)", "λαχάνιασα": "λαχανιάζω — to get out of breath", "φορείο": "φορείο — stretcher", "μαραθώνιους": "μαραθώνιος — marathon", "αρχάριους": "αρχάριος — beginner", "αντέξω": "αντέχω — to last, to cope", "τερματίσω": "τερματίζω — to finish (a race)", "κερνάς": "κερνάω — to treat, buy (a drink) for"}
})

ITEMS.append({
 "id": "l125-int-keria", "title": "Κεριά από κερί μέλισσας", "title_en": "Candles from beeswax", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια εκπομπή για τις παραδοσιακές τέχνες. Καλεσμένος είναι ο κυρ Παντελής, που φτιάχνει κεριά.",
 "script": [
  L("Δημοσιογράφος", "f", "Κυρ Παντελή, πόσα χρόνια φτιάχνετε κεριά;", "Mr Pantelis, how many years have you been making candles?"),
  L("Παντελής", "m", "Από δεκαπέντε χρονών, στο εργαστήριο του πατέρα μου. Τότε τα περισσότερα κεριά πήγαιναν στις εκκλησίες. Η δουλειά ήταν όλη στο χέρι: λιώναμε το κερί σε ένα μεγάλο καζάνι και βουτούσαμε το φιτίλι ξανά και ξανά, ώσπου το κερί να πάρει το σωστό πάχος.", "Since I was fifteen, in my father's workshop. Back then most candles went to the churches. The work was all by hand: we melted the wax in a big cauldron and dipped the wick again and again, until the candle reached the right thickness."),
  L("Δημοσιογράφος", "f", "Γιατί επιμένετε στο κερί μέλισσας; Η παραφίνη δεν είναι πιο φθηνή;", "Why do you insist on beeswax? Isn't paraffin cheaper?"),
  L("Παντελής", "m", "Είναι, πολύ πιο φθηνή. Όμως το κερί μέλισσας καίγεται πιο αργά, βγάζει λιγότερο καπνό και έχει αυτή τη γλυκιά μυρωδιά του μελιού. Το αγοράζω από μελισσοκόμους της περιοχής, κι έτσι στηρίζουμε ο ένας τον άλλον.", "It is, much cheaper. But beeswax burns more slowly, gives off less smoke and has that sweet smell of honey. I buy it from beekeepers in the area, and so we support each other."),
  L("Δημοσιογράφος", "f", "Και ποιος αγοράζει σήμερα τα κεριά σας;", "And who buys your candles today?"),
  L("Παντελής", "m", "Οι εκκλησίες ακόμα, αλλά όλο και περισσότεροι νέοι, που θέλουν κάτι φυσικό για το σπίτι τους. Η εγγονή μου άνοιξε ένα ηλεκτρονικό κατάστημα, και τώρα στέλνουμε κεριά μέχρι τη Σουηδία.", "The churches still, but more and more young people, who want something natural for their home. My granddaughter opened an online shop, and now we send candles as far as Sweden."),
 ],
 "questions": [
  Q("Πώς φτιάχνονταν τα κεριά στο εργαστήριο του πατέρα του;", ["Με μηχανήματα από το εξωτερικό", "Βουτούσαν το φιτίλι ξανά και ξανά στο λιωμένο κερί", "Με καλούπια από πηλό", "Τα αγόραζαν έτοιμα και τα στόλιζαν"], 1, "βουτούσαμε το φιτίλι ξανά και ξανά"),
  Q("Ποιο πλεονέκτημα του κεριού μέλισσας ΔΕΝ αναφέρει;", ["Καίγεται πιο αργά", "Βγάζει λιγότερο καπνό", "Είναι πιο φθηνό", "Έχει τη μυρωδιά του μελιού"], 2, "Είναι, πολύ πιο φθηνή"),
  Q("Πώς φτάνουν σήμερα τα κεριά του μέχρι τη Σουηδία;", ["Μέσα από το ηλεκτρονικό κατάστημα της εγγονής του", "Μέσα από τις εκκλησίες", "Μέσα από μια έκθεση στο εξωτερικό", "Μέσα από έναν χονδρέμπορο"], 0, "Η εγγονή μου άνοιξε ένα ηλεκτρονικό κατάστημα"),
 ],
 "gloss": {"κεριά": "κερί — candle", "εργαστήριο": "εργαστήριο — workshop", "λιώναμε": "λιώνω — to melt", "καζάνι": "καζάνι — cauldron", "βουτούσαμε": "βουτάω — to dip", "φιτίλι": "φιτίλι — wick", "πάχος": "πάχος — thickness", "επιμένετε": "επιμένω — to insist", "παραφίνη": "παραφίνη — paraffin", "καπνό": "καπνός — smoke", "μελισσοκόμους": "μελισσοκόμος — beekeeper", "στηρίζουμε": "στηρίζω — to support", "ηλεκτρονικό κατάστημα": "ηλεκτρονικό κατάστημα — online shop"}
})

ITEMS.append({
 "id": "l125-rep-kiniti-vivliothiki", "title": "Η βιβλιοθήκη που έρχεται με φορτηγάκι", "title_en": "The library that comes by van", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις τοπικές ειδήσεις για μια κινητή βιβλιοθήκη σε ορεινά χωριά.",
 "script": [
  L("Ρεπόρτερ", "m", "Κάθε δεύτερη Τετάρτη, ένα μικρό φορτηγάκι γεμάτο βιβλία ανεβαίνει τους στενούς δρόμους προς τα ορεινά χωριά του νομού. Είναι η κινητή βιβλιοθήκη της δημοτικής βιβλιοθήκης, που επισκέπτεται δώδεκα χωριά όπου δεν υπάρχει ούτε βιβλιοπωλείο ούτε σχολείο.", "Every other Wednesday, a small van full of books climbs the narrow roads to the mountain villages of the prefecture. It's the mobile library of the municipal library, which visits twelve villages where there is neither a bookshop nor a school."),
  L("Ρεπόρτερ", "m", "Η βιβλιοθηκονόμος, η κυρία Ελπίδα, ξέρει τους αναγνώστες της με το όνομα. Οι περισσότεροι είναι ηλικιωμένοι, που προτιμούν βιβλία με μεγάλα γράμματα και ιστορικά μυθιστορήματα. Το καλοκαίρι, όταν έρχονται τα εγγόνια, ζητούνται και πολλά παιδικά βιβλία.", "The librarian, Mrs Elpida, knows her readers by name. Most of them are elderly people, who prefer large-print books and historical novels. In summer, when the grandchildren come, a lot of children's books are requested too."),
  L("Ρεπόρτερ", "m", "Η κινητή βιβλιοθήκη όμως δεν δανείζει μόνο βιβλία. Η κυρία Ελπίδα βοηθά τους κατοίκους να κλείσουν ραντεβού με γιατρό μέσω διαδικτύου ή να συμπληρώσουν αιτήσεις, κι έτσι το φορτηγάκι έχει γίνει, όπως λένε, το πιο πολυσύχναστο σημείο του χωριού για μία ώρα.", "But the mobile library doesn't only lend books. Mrs Elpida helps residents book doctor's appointments online or fill in applications, and so the van has become, as they say, the busiest spot in the village for an hour."),
 ],
 "questions": [
  Q("Τι κοινό έχουν τα χωριά που επισκέπτεται η κινητή βιβλιοθήκη;", ["Είναι όλα κοντά στη θάλασσα", "Δεν υπάρχει ούτε βιβλιοπωλείο ούτε σχολείο", "Δεν έχουν δρόμο", "Έχουν μόνο παιδιά"], 1, "δεν υπάρχει ούτε βιβλιοπωλείο ούτε σχολείο"),
  Q("Τι βιβλία ζητούνται περισσότερο το καλοκαίρι;", ["Οδηγοί μαγειρικής", "Βιβλία με μεγάλα γράμματα", "Παιδικά βιβλία", "Τουριστικοί οδηγοί"], 2, "ζητούνται και πολλά παιδικά βιβλία"),
  Q("Με τι άλλο βοηθά η βιβλιοθηκονόμος τους κατοίκους;", ["Να κλείσουν ραντεβού με γιατρό μέσω διαδικτύου ή να συμπληρώσουν αιτήσεις", "Να ψωνίσουν τρόφιμα", "Να πάρουν τα φάρμακά τους", "Να μάθουν ξένες γλώσσες"], 0, "βοηθά τους κατοίκους να κλείσουν ραντεβού με γιατρό μέσω διαδικτύου ή να συμπληρώσουν αιτήσεις"),
 ],
 "gloss": {"κινητή βιβλιοθήκη": "κινητή βιβλιοθήκη — mobile library", "ορεινά": "ορεινός — mountain (adj.)", "φορτηγάκι": "φορτηγάκι — small van, small truck", "νομού": "νομός — prefecture", "βιβλιοπωλείο": "βιβλιοπωλείο — bookshop", "βιβλιοθηκονόμος": "βιβλιοθηκονόμος — librarian", "ηλικιωμένοι": "ηλικιωμένος — elderly person", "μυθιστορήματα": "μυθιστόρημα — novel", "δανείζει": "δανείζω — to lend", "αιτήσεις": "αίτηση — application", "πολυσύχναστο": "πολυσύχναστος — busy, much-frequented"}
})

ITEMS.append({
 "id": "l125-rep-sapouni", "title": "Το σαπούνι της γιαγιάς γίνεται επιχείρηση", "title_en": "Grandma's soap becomes a business", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για τη νέα επιχειρηματικότητα στην ύπαιθρο.",
 "script": [
  L("Ρεπόρτερ", "f", "Η Κατερίνα σπούδασε χημεία και δούλευε σε ένα εργαστήριο στην Αθήνα. Όταν έχασε τη δουλειά της, γύρισε στο χωριό της και θυμήθηκε τη γιαγιά της, που έφτιαχνε κάθε φθινόπωρο πράσινο σαπούνι από το λάδι της χρονιάς.", "Katerina studied chemistry and worked in a laboratory in Athens. When she lost her job, she returned to her village and remembered her grandmother, who made green soap every autumn from that year's olive oil."),
  L("Ρεπόρτερ", "f", "Ξεκίνησε στην κουζίνα της, με τη συνταγή της γιαγιάς και τις γνώσεις της από το πανεπιστήμιο. Σήμερα έχει ένα μικρό εργαστήριο, δύο υπαλλήλους και παράγει σαπούνια με ελαιόλαδο, μέλι και βότανα από τα γύρω βουνά. Το λάδι το αγοράζει από τους ελαιοπαραγωγούς του χωριού.", "She started in her kitchen, with her grandmother's recipe and her knowledge from university. Today she has a small workshop, two employees and produces soaps with olive oil, honey and herbs from the surrounding mountains. She buys the oil from the village's olive growers."),
  L("Ρεπόρτερ", "f", "Η Κατερίνα λέει ότι το πιο δύσκολο δεν ήταν η παραγωγή αλλά η γραφειοκρατία: χρειάστηκε σχεδόν έναν χρόνο για να πάρει όλες τις άδειες. Τώρα σκέφτεται να οργανώνει εργαστήρια για επισκέπτες, ώστε να μαθαίνουν κι εκείνοι πώς γίνεται το σαπούνι.", "Katerina says the hardest thing wasn't production but the bureaucracy: it took almost a year to get all the permits. Now she's thinking of organising workshops for visitors, so that they too can learn how soap is made."),
 ],
 "questions": [
  Q("Γιατί γύρισε η Κατερίνα στο χωριό;", ["Γιατί αρρώστησε η γιαγιά της", "Γιατί έχασε τη δουλειά της", "Για να τελειώσει τις σπουδές της", "Για να παντρευτεί"], 1, "Όταν έχασε τη δουλειά της, γύρισε στο χωριό της"),
  Q("Από πού αγοράζει το λάδι;", ["Από ένα σούπερ μάρκετ", "Από την Κρήτη", "Από τους ελαιοπαραγωγούς του χωριού", "Το εισάγει από την Ισπανία"], 2, "Το λάδι το αγοράζει από τους ελαιοπαραγωγούς του χωριού"),
  Q("Ποιο ήταν, σύμφωνα με την Κατερίνα, το πιο δύσκολο;", ["Η γραφειοκρατία και οι άδειες", "Η εύρεση πελατών", "Η συνταγή", "Η εύρεση υπαλλήλων"], 0, "το πιο δύσκολο δεν ήταν η παραγωγή αλλά η γραφειοκρατία"),
 ],
 "gloss": {"επιχειρηματικότητα": "επιχειρηματικότητα — entrepreneurship", "ύπαιθρο": "ύπαιθρος — countryside", "χημεία": "χημεία — chemistry", "εργαστήριο": "εργαστήριο — laboratory; workshop", "συνταγή": "συνταγή — recipe", "υπαλλήλους": "υπάλληλος — employee", "παράγει": "παράγω — to produce", "βότανα": "βότανο — herb", "ελαιοπαραγωγούς": "ελαιοπαραγωγός — olive grower", "γραφειοκρατία": "γραφειοκρατία — bureaucracy", "άδειες": "άδεια — permit, licence"}
})

ITEMS.append({
 "id": "l125-mono-kalligrafia", "title": "Πώς με ηρέμησε η καλλιγραφία", "title_en": "How calligraphy calmed me down", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε τον Σπύρο, λογιστή, να μιλάει σε ένα podcast για ένα χόμπι που ανακάλυψε.",
 "script": [
  L("Σπύρος", "m", "Πριν από δύο χρόνια ήμουν εξαντλημένος. Η δουλειά μου είναι όλη αριθμοί και προθεσμίες, και το βράδυ δεν μπορούσα να κοιμηθώ. Μια φίλη μού χάρισε ένα σετ με πένες και μελάνια και μου είπε: «Δοκίμασε να γράφεις αργά».", "Two years ago I was exhausted. My job is all numbers and deadlines, and at night I couldn't sleep. A friend gave me a set of nibs and inks and told me: 'Try writing slowly.'"),
  L("Σπύρος", "m", "Στην αρχή τα γράμματά μου ήταν στραβά και το μελάνι λέρωνε τα πάντα. Γράφτηκα σε ένα εργαστήριο καλλιγραφίας, όπου μάθαμε πρώτα να κρατάμε σωστά την πένα και να κάνουμε απλές γραμμές, σελίδες ολόκληρες, πριν φτάσουμε στα γράμματα.", "At first my letters were crooked and the ink got everywhere. I signed up for a calligraphy workshop, where we first learned to hold the pen correctly and to make simple lines, whole pages of them, before we got to the letters."),
  L("Σπύρος", "m", "Αυτό που μου άρεσε είναι ότι δεν μπορείς να βιαστείς. Αν σκέφτεσαι τη δουλειά, το χέρι τρέμει και η γραμμή χαλάει. Έτσι, για μία ώρα κάθε βράδυ, το μυαλό μου αδειάζει. Δεν θα γίνω ποτέ καλλιτέχνης, αλλά κοιμάμαι πολύ καλύτερα.", "What I liked is that you can't rush. If you're thinking about work, your hand trembles and the line is spoiled. So, for one hour every evening, my mind empties. I'll never be an artist, but I sleep much better."),
 ],
 "questions": [
  Q("Ποιο ήταν το πρόβλημα του Σπύρου πριν από δύο χρόνια;", ["Είχε χάσει τη δουλειά του", "Ήταν εξαντλημένος και δεν μπορούσε να κοιμηθεί", "Είχε πόνους στο χέρι", "Βαριόταν στο σπίτι"], 1, "το βράδυ δεν μπορούσα να κοιμηθώ"),
  Q("Τι έμαθαν πρώτα στο εργαστήριο;", ["Να γράφουν το όνομά τους", "Να φτιάχνουν δικά τους μελάνια", "Να κρατάνε σωστά την πένα και να κάνουν απλές γραμμές", "Να αντιγράφουν παλιά χειρόγραφα"], 2, "μάθαμε πρώτα να κρατάμε σωστά την πένα και να κάνουμε απλές γραμμές"),
  Q("Γιατί τον βοηθά η καλλιγραφία;", ["Γιατί δεν μπορείς να βιαστείς και το μυαλό αδειάζει", "Γιατί κερδίζει χρήματα", "Γιατί γνώρισε νέους φίλους", "Γιατί τη χρησιμοποιεί στη δουλειά του"], 0, "δεν μπορείς να βιαστείς"),
 ],
 "gloss": {"λογιστή": "λογιστής — accountant", "χόμπι": "χόμπι — hobby", "εξαντλημένος": "εξαντλημένος — exhausted", "προθεσμίες": "προθεσμία — deadline", "πένες": "πένα — nib, pen", "μελάνια": "μελάνι — ink", "στραβά": "στραβός — crooked", "λέρωνε": "λερώνω — to stain, make dirty", "καλλιγραφίας": "καλλιγραφία — calligraphy", "βιαστείς": "βιάζομαι — to hurry", "τρέμει": "τρέμω — to tremble", "αδειάζει": "αδειάζω — to empty"}
})

ITEMS.append({
 "id": "l125-mono-ydroponia", "title": "Ντομάτες χωρίς χώμα", "title_en": "Tomatoes without soil", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε τη Βασιλική, γεωπόνο, να μιλάει σε μαθητές για τη δουλειά της σε ένα υδροπονικό θερμοκήπιο.",
 "script": [
  L("Βασιλική", "f", "Παιδιά, στο θερμοκήπιο όπου δουλεύω, οι ντομάτες δεν φυτρώνουν στο χώμα. Οι ρίζες τους βρίσκονται σε ένα υλικό σαν σφουγγάρι, και ένα σύστημα από σωλήνες τους δίνει νερό με όλα τα θρεπτικά συστατικά που χρειάζονται. Αυτό λέγεται υδροπονία.", "Children, in the greenhouse where I work, the tomatoes don't grow in soil. Their roots are in a material like a sponge, and a system of pipes gives them water with all the nutrients they need. This is called hydroponics."),
  L("Βασιλική", "f", "Το μεγάλο πλεονέκτημα είναι το νερό. Επειδή το νερό που περισσεύει μαζεύεται και ξαναχρησιμοποιείται, ξοδεύουμε πολύ λιγότερο από ό,τι σε ένα χωράφι. Σε μια χώρα με ξηρά καλοκαίρια, όπως η δική μας, αυτό έχει μεγάλη σημασία.", "The big advantage is water. Because the water left over is collected and reused, we use much less than in a field. In a country with dry summers, like ours, that matters a great deal."),
  L("Βασιλική", "f", "Βέβαια, υπάρχουν και μειονεκτήματα. Το θερμοκήπιο χρειάζεται ρεύμα για τις αντλίες και τον έλεγχο της θερμοκρασίας, και αν χαλάσει κάτι, τα φυτά μπορεί να πάθουν ζημιά μέσα σε λίγες ώρες. Γι' αυτό έχω πάντα το κινητό μου ανοιχτό, ακόμα και την Κυριακή.", "Of course, there are disadvantages too. The greenhouse needs electricity for the pumps and the temperature control, and if something breaks down, the plants can be damaged within a few hours. That's why I always keep my phone on, even on Sundays."),
 ],
 "questions": [
  Q("Πού βρίσκονται οι ρίζες των φυτών στην υδροπονία;", ["Σε χώμα από το βουνό", "Σε ένα υλικό σαν σφουγγάρι", "Μέσα σε θαλασσινό νερό", "Σε άμμο"], 1, "Οι ρίζες τους βρίσκονται σε ένα υλικό σαν σφουγγάρι"),
  Q("Γιατί ξοδεύουν λιγότερο νερό;", ["Γιατί ποτίζουν μόνο τη νύχτα", "Γιατί τα φυτά είναι μικρότερα", "Γιατί το νερό που περισσεύει μαζεύεται και ξαναχρησιμοποιείται", "Γιατί χρησιμοποιούν βρόχινο νερό"], 2, "το νερό που περισσεύει μαζεύεται και ξαναχρησιμοποιείται"),
  Q("Γιατί έχει πάντα το κινητό της ανοιχτό;", ["Γιατί αν χαλάσει κάτι, τα φυτά μπορεί να πάθουν ζημιά μέσα σε λίγες ώρες", "Γιατί περιμένει παραγγελίες", "Γιατί είναι υπεύθυνη για τους μαθητές", "Γιατί συνεργάζεται με πανεπιστήμιο"], 0, "αν χαλάσει κάτι, τα φυτά μπορεί να πάθουν ζημιά μέσα σε λίγες ώρες"),
 ],
 "gloss": {"γεωπόνο": "γεωπόνος — agronomist", "υδροπονικό": "υδροπονικός — hydroponic", "θερμοκήπιο": "θερμοκήπιο — greenhouse", "φυτρώνουν": "φυτρώνω — to grow, sprout", "ρίζες": "ρίζα — root", "σφουγγάρι": "σφουγγάρι — sponge", "σωλήνες": "σωλήνας — pipe", "θρεπτικά συστατικά": "θρεπτικά συστατικά — nutrients", "περισσεύει": "περισσεύω — to be left over", "ξηρά": "ξηρός — dry", "μειονεκτήματα": "μειονέκτημα — disadvantage", "αντλίες": "αντλία — pump"}
})

ITEMS.append({
 "id": "l125-c1-ringelmann", "title": "Όταν η ομάδα τραβάει λιγότερο", "title_en": "When the team pulls less", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από διάλεξη κοινωνικής ψυχολογίας για το φαινόμενο της κοινωνικής οκνηρίας.",
 "script": [
  L("Καθηγήτρια", "f", "Στα τέλη του 19ου αιώνα, ένας Γάλλος γεωπόνος μηχανικός, ο Μαξιμιλιέν Ρινγκελμάν, ζήτησε από ανθρώπους να τραβήξουν ένα σχοινί, άλλοτε μόνοι τους και άλλοτε σε ομάδες. Θα περίμενε κανείς ότι οκτώ άτομα θα τραβούσαν με οκταπλάσια δύναμη. Δεν συνέβη αυτό: όσο μεγάλωνε η ομάδα, τόσο μικρότερη ήταν η προσπάθεια που κατέβαλλε ο καθένας. Στις ομάδες των οκτώ, η συνολική δύναμη έφτανε, σύμφωνα με τους υπολογισμούς του, περίπου το μισό από το άθροισμα των ατομικών επιδόσεων.", "At the end of the 19th century, a French agricultural engineer, Maximilien Ringelmann, asked people to pull a rope, sometimes alone and sometimes in groups. One would expect eight people to pull with eight times the force. That is not what happened: the bigger the group grew, the less effort each person made. In groups of eight, the total force reached, by his calculations, about half the sum of the individual performances."),
  L("Καθηγήτρια", "f", "Ο ίδιος ο Ρινγκελμάν απέδωσε το φαινόμενο εν μέρει στον κακό συντονισμό: οι άνθρωποι δεν τραβούν όλοι την ίδια στιγμή. Μεταγενέστερα πειράματα όμως έδειξαν ότι αυτό δεν αρκεί. Όταν οι συμμετέχοντες πίστευαν ότι τραβούν μαζί με άλλους, ενώ στην πραγματικότητα τραβούσαν μόνοι, και πάλι κατέβαλλαν λιγότερη προσπάθεια. Το πρόβλημα, επομένως, δεν ήταν μόνο τεχνικό αλλά και ψυχολογικό. Το 1979, ο Μπιμπ Λατανέ και οι συνεργάτες του ονόμασαν το φαινόμενο «κοινωνική οκνηρία».", "Ringelmann himself attributed the phenomenon partly to poor coordination: people don't all pull at the same moment. Later experiments, however, showed that this is not enough. When participants believed they were pulling together with others, while in reality they were pulling alone, they still made less effort. The problem, therefore, was not only technical but also psychological. In 1979, Bibb Latané and his colleagues named the phenomenon 'social loafing'."),
  L("Καθηγήτρια", "f", "Γιατί συμβαίνει; Όταν η συνεισφορά του καθενός χάνεται μέσα στο σύνολο, ο καθένας νιώθει ότι η δική του προσπάθεια δεν μετράει, ούτε θα αξιολογηθεί. Η έρευνα δείχνει ότι η οκνηρία μειώνεται όταν η ατομική συμβολή είναι ορατή, όταν οι ομάδες είναι μικρές και όταν τα μέλη θεωρούν το έργο σημαντικό. Με άλλα λόγια, δεν φταίει η τεμπελιά των ανθρώπων, αλλά ο τρόπος που οργανώνουμε τη συνεργασία.", "Why does it happen? When each person's contribution is lost in the whole, each person feels that their own effort doesn't count, nor will it be assessed. Research shows that loafing decreases when individual contribution is visible, when groups are small and when members consider the task important. In other words, it is not people's laziness that is to blame, but the way we organise cooperation."),
 ],
 "questions": [
  Q("Τι διαπίστωσε ο Ρινγκελμάν στα πειράματά του;", ["Ότι οι ομάδες τραβούσαν με περισσότερη δύναμη από το άθροισμα των ατόμων", "Ότι όσο μεγάλωνε η ομάδα, τόσο λιγότερη προσπάθεια κατέβαλλε ο καθένας", "Ότι οι γυναίκες τραβούσαν πιο δυνατά από τους άνδρες", "Ότι η δύναμη δεν άλλαζε με το μέγεθος της ομάδας"], 1, "όσο μεγάλωνε η ομάδα, τόσο μικρότερη ήταν η προσπάθεια που κατέβαλλε ο καθένας"),
  Q("Τι έδειξαν τα μεταγενέστερα πειράματα;", ["Ότι ο Ρινγκελμάν είχε κάνει λάθος στους υπολογισμούς", "Ότι το φαινόμενο εμφανίζεται μόνο σε σωματική εργασία", "Ότι οι άνθρωποι κατέβαλλαν λιγότερη προσπάθεια ακόμη κι όταν απλώς πίστευαν ότι τραβούν με άλλους", "Ότι ο κακός συντονισμός εξηγεί πλήρως το φαινόμενο"], 2, "Όταν οι συμμετέχοντες πίστευαν ότι τραβούν μαζί με άλλους, ενώ στην πραγματικότητα τραβούσαν μόνοι, και πάλι κατέβαλλαν λιγότερη προσπάθεια"),
  Q("Ποιος έδωσε στο φαινόμενο το όνομα «κοινωνική οκνηρία»;", ["Ο Μπιμπ Λατανέ και οι συνεργάτες του", "Ο ίδιος ο Ρινγκελμάν", "Η καθηγήτρια της διάλεξης", "Μια ομάδα Γάλλων γεωπόνων"], 0, "ο Μπιμπ Λατανέ και οι συνεργάτες του ονόμασαν το φαινόμενο «κοινωνική οκνηρία»"),
  Q("Ποιο είναι το συμπέρασμα της ομιλήτριας;", ["Οι άνθρωποι είναι από τη φύση τους τεμπέληδες", "Η ομαδική εργασία πρέπει να αποφεύγεται", "Οι μεγάλες ομάδες είναι πάντα πιο αποδοτικές", "Το πρόβλημα βρίσκεται στον τρόπο που οργανώνεται η συνεργασία"], 3, "δεν φταίει η τεμπελιά των ανθρώπων, αλλά ο τρόπος που οργανώνουμε τη συνεργασία"),
 ],
 "gloss": {"κοινωνικής οκνηρίας": "κοινωνική οκνηρία — social loafing", "γεωπόνος": "γεωπόνος — agronomist, agricultural engineer", "σχοινί": "σχοινί — rope", "οκταπλάσια": "οκταπλάσιος — eightfold", "κατέβαλλε": "καταβάλλω (προσπάθεια) — to make (an effort)", "άθροισμα": "άθροισμα — sum", "επιδόσεων": "επίδοση — performance", "απέδωσε": "αποδίδω — to attribute", "συντονισμό": "συντονισμός — coordination", "Μεταγενέστερα": "μεταγενέστερος — later, subsequent", "συνεισφορά": "συνεισφορά — contribution", "αξιολογηθεί": "αξιολογούμαι — to be assessed", "συμβολή": "συμβολή — contribution", "τεμπελιά": "τεμπελιά — laziness"}
})

ITEMS.append({
 "id": "l125-c1-karaiskakis", "title": "Ο γιος της καλογριάς", "title_en": "The nun's son", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια ιστορικό για τον οπλαρχηγό του 1821 Γεώργιο Καραϊσκάκη.",
 "script": [
  L("Δημοσιογράφος", "m", "Ο Καραϊσκάκης είναι από τις πιο αγαπητές μορφές της Επανάστασης. Από πού πηγάζει αυτή η αγάπη;", "Karaiskakis is one of the best-loved figures of the Revolution. Where does this affection come from?"),
  L("Ιστορικός", "f", "Εν μέρει από τη ζωή του, που μοιάζει με μυθιστόρημα. Γεννήθηκε γύρω στο 1780 στην περιοχή των Αγράφων· η μητέρα του ήταν καλογριά, γι' αυτό τον αποκαλούσαν «γιο της καλογριάς». Μεγάλωσε φτωχός, έγινε κλέφτης και αρματολός, και για ένα διάστημα βρέθηκε στην αυλή του Αλή Πασά. Ήταν οξύθυμος, αθυρόστομος, και τον ταλαιπωρούσε σχεδόν σε όλη του τη ζωή η φυματίωση. Κι όμως, οι στρατιώτες τον λάτρευαν, γιατί μοιραζόταν μαζί τους τις κακουχίες.", "Partly from his life, which reads like a novel. He was born around 1780 in the Agrafa region; his mother was a nun, which is why they called him 'the nun's son'. He grew up poor, became a klepht and an armatolos, and for a time found himself at the court of Ali Pasha. He was hot-tempered, foul-mouthed, and tuberculosis plagued him for almost all his life. And yet the soldiers adored him, because he shared their hardships."),
  L("Δημοσιογράφος", "m", "Ποια ήταν η σημαντικότερη συμβολή του στον αγώνα;", "What was his most important contribution to the struggle?"),
  L("Ιστορικός", "f", "Το 1826, όταν η Ακρόπολη πολιορκούνταν από τον Κιουταχή, η κυβέρνηση τον διόρισε αρχιστράτηγο της Ρούμελης. Αντί να επιτεθεί κατευθείαν στην Αθήνα, εκστράτευσε στη Στερεά για να αποκόψει τις γραμμές ανεφοδιασμού του εχθρού. Η νίκη του στην Αράχωβα, τον Νοέμβριο του 1826, αναπτέρωσε το ηθικό των Ελλήνων σε μια περίοδο που η Επανάσταση έμοιαζε να σβήνει.", "In 1826, when the Acropolis was under siege by Kütahi, the government appointed him commander-in-chief of Roumeli. Instead of attacking Athens directly, he campaigned in Central Greece to cut the enemy's supply lines. His victory at Arachova, in November 1826, revived the morale of the Greeks at a time when the Revolution seemed to be dying out."),
  L("Ιστορικός", "f", "Τον Απρίλιο του 1827, κοντά στο Φάληρο, τραυματίστηκε θανάσιμα σε μια αψιμαχία και πέθανε την επόμενη μέρα. Λίγες μέρες αργότερα οι Έλληνες ηττήθηκαν βαριά στον Ανάλατο, και λίγες εβδομάδες αργότερα η Ακρόπολη παραδόθηκε. Πολλοί ιστορικοί πιστεύουν ότι ο θάνατός του στέρησε από την επιχείρηση τον μόνο άνθρωπο που μπορούσε να κρατήσει ενωμένους τους οπλαρχηγούς. Δεν είναι τυχαίο ότι το γήπεδο στο Φάληρο φέρει σήμερα το όνομά του.", "In April 1827, near Phaleron, he was mortally wounded in a skirmish and died the next day. A few days later the Greeks were heavily defeated at Analatos, and a few weeks later the Acropolis surrendered. Many historians believe that his death deprived the operation of the only man who could keep the chieftains united. It is no coincidence that the stadium at Phaleron bears his name today."),
 ],
 "questions": [
  Q("Γιατί τον αποκαλούσαν «γιο της καλογριάς»;", ["Γιατί μεγάλωσε σε μοναστήρι", "Γιατί η μητέρα του ήταν καλογριά", "Γιατί ήθελε να γίνει μοναχός", "Γιατί τον βάφτισε μια καλογριά"], 1, "η μητέρα του ήταν καλογριά"),
  Q("Γιατί, σύμφωνα με την ιστορικό, τον λάτρευαν οι στρατιώτες;", ["Γιατί τους πλήρωνε καλά", "Γιατί ήταν ήπιος και ευγενικός", "Γιατί μοιραζόταν μαζί τους τις κακουχίες", "Γιατί δεν έχασε ποτέ μάχη"], 2, "μοιραζόταν μαζί τους τις κακουχίες"),
  Q("Ποια ήταν η στρατηγική του το 1826;", ["Να αποκόψει τις γραμμές ανεφοδιασμού του εχθρού στη Στερεά", "Να επιτεθεί αμέσως στην Ακρόπολη", "Να διαπραγματευτεί με τον Κιουταχή", "Να ζητήσει βοήθεια από τις Μεγάλες Δυνάμεις"], 0, "εκστράτευσε στη Στερεά για να αποκόψει τις γραμμές ανεφοδιασμού του εχθρού"),
  Q("Τι πιστεύουν πολλοί ιστορικοί για τον θάνατό του;", ["Ότι ήταν αποτέλεσμα προδοσίας", "Ότι δεν επηρέασε την έκβαση των επιχειρήσεων", "Ότι οφειλόταν στη φυματίωση", "Ότι στέρησε από την επιχείρηση τον μόνο που μπορούσε να κρατήσει ενωμένους τους οπλαρχηγούς"], 3, "ο θάνατός του στέρησε από την επιχείρηση τον μόνο άνθρωπο που μπορούσε να κρατήσει ενωμένους τους οπλαρχηγούς"),
 ],
 "gloss": {"οπλαρχηγό": "οπλαρχηγός — (armed) chieftain", "πηγάζει": "πηγάζω — to stem, spring from", "καλογριά": "καλογριά — nun", "αρματολός": "αρματολός — armatolos (Christian militia captain)", "αυλή": "αυλή — court", "οξύθυμος": "οξύθυμος — hot-tempered", "αθυρόστομος": "αθυρόστομος — foul-mouthed", "φυματίωση": "φυματίωση — tuberculosis", "κακουχίες": "κακουχίες — hardships", "πολιορκούνταν": "πολιορκούμαι — to be besieged", "αρχιστράτηγο": "αρχιστράτηγος — commander-in-chief", "ανεφοδιασμού": "ανεφοδιασμός — supply", "αναπτέρωσε": "αναπτερώνω — to revive, boost", "αψιμαχία": "αψιμαχία — skirmish", "θανάσιμα": "θανάσιμα — mortally"}
})

rnd = random.Random(125)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-125.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
