# Source for library/listening/listening-196.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l196.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l196-ann-koini-metakinisi", "title": "Κοινή μετακίνηση για τους φοιτητές", "title_en": "Car-sharing for students", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στον ραδιοφωνικό σταθμό του πανεπιστημίου.",
 "script": [
  L("Εκφωνήτρια", "f", "Ανακοίνωση από το Γραφείο Φοιτητικής Μέριμνας. Από τη Δευτέρα λειτουργεί η νέα πλατφόρμα κοινής μετακίνησης του πανεπιστημίου. Φοιτητές και εργαζόμενοι που έρχονται στην πανεπιστημιούπολη με αυτοκίνητο μπορούν να δηλώνουν τις διαδρομές τους και τις ελεύθερες θέσεις, και όσοι δεν έχουν αυτοκίνητο να κλείνουν θέση.", "An announcement from the Student Welfare Office. From Monday the university's new car-sharing platform is running. Students and staff who come to the campus by car can register their routes and free seats, and those without a car can book a seat."),
  L("Εκφωνήτρια", "f", "Οι επιβάτες δεν πληρώνουν τον οδηγό απευθείας. Συμμετέχουν στα έξοδα με ένα ποσό που υπολογίζει η πλατφόρμα ανάλογα με την απόσταση, και που δεν μπορεί να ξεπερνά τα δύο ευρώ για μια διαδρομή μέσα στην πόλη. Για να εγγραφείτε, χρειάζεστε τον ιδρυματικό σας λογαριασμό.", "Passengers don't pay the driver directly. They contribute to costs with an amount the platform calculates according to distance, which cannot exceed two euros for a trip within the city. To register, you need your institutional account."),
  L("Εκφωνήτρια", "f", "Όσοι οδηγοί κάνουν τουλάχιστον δέκα κοινές διαδρομές τον μήνα θα έχουν δωρεάν θέση στο νέο πάρκινγκ πίσω από τη βιβλιοθήκη. Η πρώτη ενημερωτική συνάντηση θα γίνει την Τετάρτη στις δώδεκα, στο αμφιθέατρο της Φιλοσοφικής.", "Drivers who make at least ten shared trips a month will get a free space in the new car park behind the library. The first information meeting will take place on Wednesday at twelve, in the Philosophy School lecture hall."),
 ],
 "questions": [
  Q("Τι μπορούν να κάνουν όσοι δεν έχουν αυτοκίνητο;", ["Να νοικιάσουν αυτοκίνητο", "Να κλείνουν θέση σε μια διαδρομή", "Να παίρνουν δωρεάν λεωφορείο", "Να παρκάρουν δωρεάν"], 1, "όσοι δεν έχουν αυτοκίνητο να κλείνουν θέση"),
  Q("Πόσο πληρώνουν οι επιβάτες για μια διαδρομή μέσα στην πόλη;", ["Τίποτα", "Όσο θέλουν", "Το πολύ δύο ευρώ", "Πέντε ευρώ"], 2, "δεν μπορεί να ξεπερνά τα δύο ευρώ"),
  Q("Τι κερδίζουν οι οδηγοί που κάνουν δέκα κοινές διαδρομές τον μήνα;", ["Δωρεάν βενζίνη", "Δωρεάν θέση στο νέο πάρκινγκ", "Ένα δώρο από τη βιβλιοθήκη", "Μια βεβαίωση"], 1, "θα έχουν δωρεάν θέση στο νέο πάρκινγκ"),
 ],
 "gloss": {"Μέριμνας": "Φοιτητική Μέριμνα — student welfare (office)", "πανεπιστημιούπολη": "πανεπιστημιούπολη — university campus", "ξεπερνά": "ξεπερνώ — to exceed", "ιδρυματικό": "ιδρυματικός λογαριασμός — institutional (university) account", "αμφιθέατρο": "αμφιθέατρο — lecture hall"},
})

ITEMS.append({
 "id": "l196-int-nyfika", "title": "Η μοδίστρα των νυφικών", "title_en": "The wedding-dress maker", "type": "interview", "level": "B2",
 "context_el": "Συνέντευξη με μια μοδίστρα που ράβει νυφικά σε ένα ατελιέ στον Πειραιά.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσος καιρός χρειάζεται για να ραφτεί ένα νυφικό;", "How long does it take to make a wedding dress?"),
  L("Μοδίστρα", "f", "Από την πρώτη συνάντηση ως την τελευταία πρόβα περνούν συνήθως έξι μήνες. Η ραφή αυτή καθαυτή είναι γύρω στις ογδόντα ώρες, αλλά ο περισσότερος χρόνος πάει στις πρόβες. Μια νύφη μπορεί να αλλάξει πολύ μέσα σε λίγους μήνες, από το άγχος ή από τη γυμναστική.", "From the first meeting to the last fitting, six months usually pass. The sewing itself is around eighty hours, but most of the time goes on fittings. A bride can change a lot in a few months, from stress or from exercise."),
  L("Δημοσιογράφος", "m", "Έχετε δει πολλές νύφες να αλλάζουν γνώμη;", "Have you seen many brides change their minds?"),
  L("Μοδίστρα", "f", "Πάρα πολλές. Μια κοπέλα ήρθε με φωτογραφίες από ένα φόρεμα με τεράστια φούστα και, στην τρίτη πρόβα, μου είπε ότι νιώθει σαν τούρτα. Ξεκινήσαμε από την αρχή, με κάτι απλό και ίσιο. Ήταν η πιο ευτυχισμένη νύφη της χρονιάς. Γι' αυτό πάντα λέω: φέρτε μου φωτογραφίες, αλλά να είστε έτοιμες να τις ξεχάσετε.", "Very many. One young woman came with photos of a dress with a huge skirt and, at the third fitting, told me she felt like a cake. We started from scratch, with something simple and straight. She was the happiest bride of the year. That's why I always say: bring me photos, but be ready to forget them."),
  L("Δημοσιογράφος", "m", "Τι γίνεται με τα νυφικά μετά τον γάμο;", "What happens to the dresses after the wedding?"),
  L("Μοδίστρα", "f", "Όλο και περισσότερες γυναίκες μού τα φέρνουν πίσω για να τα μετατρέψω: σε βραδινό φόρεμα, σε φόρεμα βάπτισης για το παιδί τους, μια φορά και σε κουρτίνες. Μου αρέσει αυτό. Ένα ύφασμα που κουβαλά τόσες αναμνήσεις δεν πρέπει να μένει σε ένα κουτί.", "More and more women bring them back to me to transform them: into an evening dress, a christening gown for their child, once even into curtains. I like that. A fabric that carries so many memories shouldn't stay in a box."),
 ],
 "questions": [
  Q("Πού πηγαίνει ο περισσότερος χρόνος;", ["Στη ραφή", "Στις πρόβες", "Στην αγορά υφάσματος", "Στο κέντημα"], 1, "ο περισσότερος χρόνος πάει στις πρόβες"),
  Q("Τι έγινε με τη νύφη που ένιωθε «σαν τούρτα»;", ["Αγόρασε έτοιμο φόρεμα", "Ξεκίνησαν από την αρχή με ένα απλό φόρεμα", "Ακύρωσε τον γάμο", "Κράτησε το ίδιο φόρεμα"], 1, "Ξεκινήσαμε από την αρχή, με κάτι απλό και ίσιο"),
  Q("Τι κάνουν όλο και περισσότερες γυναίκες μετά τον γάμο;", ["Πουλάνε το νυφικό", "Το δανείζουν σε φίλες", "Το φέρνουν πίσω για να μετατραπεί σε κάτι άλλο", "Το δωρίζουν σε μουσείο"], 2, "μού τα φέρνουν πίσω για να τα μετατρέψω"),
 ],
 "gloss": {"νυφικό": "νυφικό — wedding dress", "πρόβα": "πρόβα — fitting", "ραφή": "ραφή — sewing", "μετατρέψω": "μετατρέπω — to convert, transform", "βάπτισης": "βάπτιση — christening"},
})

ITEMS.append({
 "id": "l196-vm-tatouaz", "title": "Μήνυμα από το στούντιο τατουάζ", "title_en": "A message from the tattoo studio", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει ραντεβού για το πρώτο σας τατουάζ. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "m", "Γεια σας, ο Μάριος είμαι από το στούντιο, για το ραντεβού σας την Πέμπτη στις πέντε. Η Δάφνη, που θα σας έκανε το τατουάζ, είχε ένα μικρό ατύχημα με το ποδήλατο και έχει το δεξί χέρι δεμένο, οπότε δεν μπορεί να δουλέψει αυτή την εβδομάδα. Μην ανησυχείτε, είναι καλά.", "Hi, it's Marios from the studio, about your appointment on Thursday at five. Dafni, who was going to do your tattoo, had a small bicycle accident and has her right hand bandaged, so she can't work this week. Don't worry, she's fine."),
  L("Υπάλληλος", "m", "Έχετε δύο επιλογές. Μπορούμε να μεταφέρουμε το ραντεβού για την επόμενη Πέμπτη, την ίδια ώρα, με τη Δάφνη, που έχει ήδη το σχέδιό σας. Ή μπορεί να το κάνει ο Στράτος αυτή την Πέμπτη, αλλά θα χρειαστεί να ξαναδεί μαζί σας το σχέδιο, γιατί δουλεύει με λίγο διαφορετικό στυλ.", "You have two options. We can move the appointment to next Thursday, same time, with Dafni, who already has your design. Or Stratos can do it this Thursday, but he'll need to go over the design with you again, because he works in a slightly different style."),
  L("Υπάλληλος", "m", "Και κάτι που ξεχάσαμε να σας πούμε: αν σκοπεύετε να πάτε διακοπές, υπολογίστε ότι για δύο εβδομάδες μετά το τατουάζ δεν πρέπει να μπείτε στη θάλασσα ούτε να το εκθέσετε στον ήλιο. Η προκαταβολή σας ισχύει όποια λύση κι αν διαλέξετε. Στείλτε μας ένα μήνυμα.", "And something we forgot to tell you: if you're planning to go on holiday, bear in mind that for two weeks after the tattoo you shouldn't go in the sea or expose it to the sun. Your deposit stands whichever option you choose. Send us a message."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να δουλέψει η Δάφνη;", ["Είναι σε διακοπές", "Έχει το χέρι της δεμένο μετά από ατύχημα με το ποδήλατο", "Είναι άρρωστη", "Άλλαξε δουλειά"], 1, "είχε ένα μικρό ατύχημα με το ποδήλατο και έχει το δεξί χέρι δεμένο"),
  Q("Τι πρέπει να γίνει αν διαλέξετε τον Στράτο;", ["Να πληρώσετε ξανά προκαταβολή", "Να ξαναδείτε μαζί του το σχέδιο", "Να έρθετε πιο νωρίς", "Να φέρετε φωτογραφία"], 1, "θα χρειαστεί να ξαναδεί μαζί σας το σχέδιο"),
  Q("Τι πρέπει να αποφύγετε για δύο εβδομάδες μετά το τατουάζ;", ["Τη γυμναστική", "Τη θάλασσα και τον ήλιο", "Το ποδήλατο", "Το ντους"], 1, "δεν πρέπει να μπείτε στη θάλασσα ούτε να το εκθέσετε στον ήλιο"),
 ],
 "gloss": {"τατουάζ": "τατουάζ — tattoo", "δεμένο": "δεμένος — bandaged, tied", "μεταφέρουμε": "μεταφέρω — to move, transfer", "εκθέσετε": "εκθέτω — to expose", "προκαταβολή": "προκαταβολή — deposit"},
})

ITEMS.append({
 "id": "l196-mono-ilektrostatiko", "title": "Γιατί με «χτυπάει» η πόρτα του αυτοκινήτου;", "title_en": "Why does the car door give me a shock?", "type": "monologue", "level": "B2",
 "context_el": "Ένας καθηγητής Φυσικής απαντά σε ερώτηση ακροατή σε μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Καθηγητής", "m", "Ένας ακροατής μας ρωτάει γιατί, κάθε φορά που βγαίνει από το αυτοκίνητο τον χειμώνα, νιώθει ένα μικρό τσίμπημα όταν ακουμπά την πόρτα. Δεν είναι βλάβη του αυτοκινήτου, μην ανησυχείτε. Είναι στατικός ηλεκτρισμός, το ίδιο φαινόμενο που κάνει τα μαλλιά να σηκώνονται όταν βγάζουμε ένα μάλλινο πουλόβερ.", "A listener asks us why, every time he gets out of the car in winter, he feels a little sting when he touches the door. It isn't a fault in the car, don't worry. It's static electricity, the same phenomenon that makes your hair stand up when you take off a woollen jumper."),
  L("Καθηγητής", "m", "Όταν οδηγούμε, το ρούχο μας τρίβεται συνεχώς στο κάθισμα. Με την τριβή, φορτία περνούν από το ένα υλικό στο άλλο, και το σώμα μας φορτίζεται. Όσο καθόμαστε, δεν συμβαίνει τίποτα. Όταν όμως σηκωθούμε και ακουμπήσουμε το μέταλλο της πόρτας, το φορτίο εκφορτίζεται απότομα, και αυτό είναι το τσίμπημα.", "When we drive, our clothes rub constantly against the seat. Through friction, charges pass from one material to the other, and our body becomes charged. While we're sitting, nothing happens. But when we stand up and touch the metal of the door, the charge discharges abruptly, and that's the sting."),
  L("Καθηγητής", "m", "Γιατί τον χειμώνα; Γιατί ο αέρας είναι πιο ξηρός, και η υγρασία, που κανονικά βοηθά τα φορτία να διαφεύγουν σιγά σιγά, λείπει. Η λύση είναι απλή: πριν σηκωθείτε από το κάθισμα, πιάστε με το χέρι ένα μεταλλικό σημείο της πόρτας και κρατήστε το καθώς βγαίνετε. Έτσι το φορτίο φεύγει σταδιακά, χωρίς να το νιώσετε.", "Why in winter? Because the air is drier, and the moisture, which normally helps charges escape little by little, is missing. The solution is simple: before you get up from the seat, hold a metal part of the door with your hand and keep holding it as you get out. That way the charge leaves gradually, without you feeling it."),
 ],
 "questions": [
  Q("Πώς φορτίζεται το σώμα μας στο αυτοκίνητο;", ["Από τη μπαταρία", "Από την τριβή του ρούχου με το κάθισμα", "Από το ραδιόφωνο", "Από τον κλιματισμό"], 1, "Με την τριβή, φορτία περνούν από το ένα υλικό στο άλλο"),
  Q("Γιατί το φαινόμενο είναι πιο συχνό τον χειμώνα;", ["Γιατί φοράμε γάντια", "Γιατί ο αέρας είναι πιο ξηρός", "Γιατί οδηγούμε περισσότερο", "Γιατί το μέταλλο είναι πιο κρύο"], 1, "ο αέρας είναι πιο ξηρός"),
  Q("Τι συμβουλεύει ο καθηγητής;", ["Να φοράμε μάλλινα ρούχα", "Να πιάνουμε ένα μεταλλικό σημείο πριν σηκωθούμε και να το κρατάμε καθώς βγαίνουμε", "Να βγαίνουμε πολύ γρήγορα", "Να πάμε το αυτοκίνητο σε συνεργείο"], 1, "πιάστε με το χέρι ένα μεταλλικό σημείο της πόρτας"),
 ],
 "gloss": {"τσίμπημα": "τσίμπημα — sting, pinch", "στατικός": "στατικός ηλεκτρισμός — static electricity", "τριβή": "τριβή — friction", "φορτίο": "φορτίο — (electric) charge", "εκφορτίζεται": "εκφορτίζομαι — to discharge", "σταδιακά": "σταδιακά — gradually"},
})

ITEMS.append({
 "id": "l196-dia-giagia-diakopes", "title": "Να πάρουμε τη γιαγιά μαζί στις διακοπές;", "title_en": "Shall we take Grandma on holiday with us?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι συζητά αν θα πάρει μαζί τη μητέρα της γυναίκας στις καλοκαιρινές διακοπές.",
 "script": [
  L("Κατερίνα", "f", "Η μαμά μου είναι μόνη της από τότε που πέθανε ο μπαμπάς, και φέτος δεν έχει πού να πάει τον Αύγουστο. Σκέφτηκα να την πάρουμε μαζί μας στη Σκόπελο.", "My mum has been alone since Dad died, and this year she has nowhere to go in August. I thought we could take her with us to Skopelos."),
  L("Θάνος", "m", "Τη μαμά σου την αγαπώ, το ξέρεις. Αλλά το σπιτάκι που κλείσαμε έχει δύο δωμάτια, και τα παιδιά δεν θα χωράνε. Και η μαμά σου δεν περπατάει εύκολα· το σπίτι είναι πάνω στον λόφο, με σκαλιά παντού.", "I love your mum, you know that. But the little house we booked has two rooms, and the kids won't fit. And your mum doesn't walk easily; the house is up on the hill, with steps everywhere."),
  L("Κατερίνα", "f", "Το σκέφτηκα. Η ιδιοκτήτρια έχει κι ένα στούντιο στο ισόγειο, δίπλα στο λιμάνι, χωρίς σκαλιά. Είναι δέκα λεπτά με τα πόδια από εμάς. Θα έχει τη δική της ησυχία, κι εμείς τη δική μας.", "I've thought about it. The owner also has a studio on the ground floor, next to the harbour, with no steps. It's ten minutes on foot from us. She'll have her own peace and quiet, and we'll have ours."),
  L("Θάνος", "m", "Και τα έξοδα; Ένα δεύτερο κατάλυμα τον Αύγουστο δεν είναι φτηνό.", "And the costs? A second place to stay in August isn't cheap."),
  L("Κατερίνα", "f", "Η μαμά επιμένει να πληρώσει μόνη της το στούντιο. Και σκέψου: τα πρωινά θα κρατάει τα παιδιά, κι εμείς θα μπορούμε να πάμε επιτέλους εκείνη τη βόλτα με το καΐκι που λέμε τρία χρόνια.", "Mum insists on paying for the studio herself. And think about it: in the mornings she'll look after the kids, and we'll finally be able to go on that boat trip we've been talking about for three years."),
  L("Θάνος", "m", "Εντάξει, με έπεισες. Αλλά τα βράδια, ψαροταβέρνα όλοι μαζί, και κερνάω εγώ.", "All right, you've convinced me. But in the evenings, fish taverna all together, and it's on me."),
 ],
 "questions": [
  Q("Ποιο πρόβλημα βλέπει αρχικά ο Θάνος;", ["Η πεθερά του δεν του αρέσει", "Το σπίτι είναι μικρό και έχει πολλά σκαλιά", "Η Σκόπελος είναι μακριά", "Τα παιδιά δεν θέλουν"], 1, "το σπιτάκι που κλείσαμε έχει δύο δωμάτια"),
  Q("Ποια λύση έχει βρει η Κατερίνα;", ["Να μείνει η μητέρα της σε ένα στούντιο στο ισόγειο, κοντά στο λιμάνι", "Να κλείσουν μεγαλύτερο σπίτι", "Να πάνε σε ξενοδοχείο", "Να πάει η μητέρα της με μια φίλη"], 0, "έχει κι ένα στούντιο στο ισόγειο, δίπλα στο λιμάνι"),
  Q("Ποιος θα πληρώσει το στούντιο;", ["Ο Θάνος", "Η Κατερίνα", "Η μητέρα της Κατερίνας", "Η ιδιοκτήτρια"], 2, "Η μαμά επιμένει να πληρώσει μόνη της το στούντιο"),
 ],
 "gloss": {"σπιτάκι": "σπιτάκι — little house", "κατάλυμα": "κατάλυμα — accommodation", "επιμένει": "επιμένω — to insist", "καΐκι": "καΐκι — caique, fishing boat", "κερνάω": "κερνάω — to treat, pay for others"},
})

ITEMS.append({
 "id": "l196-rep-silent-disco", "title": "Ένα σιωπηλό πάρτι στην πλατεία", "title_en": "A silent disco in the square", "type": "report", "level": "B2",
 "context_el": "Ρεπορτάζ από ένα πάρτι όπου όλοι χορεύουν με ακουστικά.",
 "script": [
  L("Ρεπόρτερ", "f", "Είναι έντεκα το βράδυ και στην πλατεία χορεύουν πάνω από διακόσιοι άνθρωποι. Κι όμως, το μόνο που ακούγεται είναι γέλια και τα βήματα στις πλάκες. Όλοι φορούν ασύρματα ακουστικά που ανάβουν σε τρία χρώματα: μπλε, πράσινο ή κόκκινο.", "It's eleven at night and more than two hundred people are dancing in the square. And yet, the only thing you can hear is laughter and footsteps on the paving. Everyone is wearing wireless headphones that light up in three colours: blue, green or red."),
  L("Ρεπόρτερ", "f", "Κάθε χρώμα αντιστοιχεί σε έναν διαφορετικό DJ. Στο μπλε κανάλι παίζει ροκ, στο πράσινο ελληνικά της δεκαετίας του ογδόντα, στο κόκκινο ηλεκτρονική μουσική. Ο καθένας αλλάζει κανάλι όποτε θέλει, κι έτσι δύο άνθρωποι που χορεύουν ο ένας δίπλα στον άλλον μπορεί να ακούνε εντελώς διαφορετικά τραγούδια.", "Each colour corresponds to a different DJ. On the blue channel there's rock, on the green Greek songs from the eighties, on the red electronic music. Everyone changes channel whenever they like, and so two people dancing side by side may be hearing completely different songs."),
  L("Ρεπόρτερ", "f", "Η ιδέα ήταν του δήμου, μετά από χρόνια παραπόνων για τον θόρυβο από τα καλοκαιρινά πάρτι. Οι κάτοικοι της πλατείας δέχτηκαν με ενθουσιασμό. Μια ηλικιωμένη κυρία, που παρακολουθεί από το μπαλκόνι της, λέει ότι είναι το πρώτο καλοκαίρι εδώ και χρόνια που κοιμάται με ανοιχτά παράθυρα.", "The idea was the municipality's, after years of complaints about the noise from summer parties. The residents of the square welcomed it enthusiastically. An elderly lady, watching from her balcony, says it's the first summer in years that she sleeps with the windows open."),
  L("Ρεπόρτερ", "f", "Το πιο αστείο, λένε οι διοργανωτές, είναι όταν κάποιος βγάζει τα ακουστικά για λίγα δευτερόλεπτα και βλέπει ξαφνικά διακόσια άτομα να χορεύουν και να τραγουδούν δυνατά... χωρίς μουσική.", "The funniest thing, say the organisers, is when someone takes off their headphones for a few seconds and suddenly sees two hundred people dancing and singing loudly... without music."),
 ],
 "questions": [
  Q("Τι δείχνει το χρώμα των ακουστικών;", ["Την ηλικία του χορευτή", "Ποιον DJ ακούει ο καθένας", "Πόσο δυνατά ακούει", "Αν έχει πληρώσει εισιτήριο"], 1, "Κάθε χρώμα αντιστοιχεί σε έναν διαφορετικό DJ"),
  Q("Γιατί οργάνωσε ο δήμος αυτό το πάρτι;", ["Για να βγάλει χρήματα", "Μετά από χρόνια παραπόνων για τον θόρυβο", "Για να προσελκύσει τουρίστες", "Γιατί το ζήτησαν οι DJ"], 1, "μετά από χρόνια παραπόνων για τον θόρυβο"),
  Q("Τι λέει η ηλικιωμένη κυρία;", ["Ότι θέλει να χορέψει κι εκείνη", "Ότι φέτος κοιμάται με ανοιχτά παράθυρα", "Ότι η μουσική είναι πολύ δυνατή", "Ότι δεν της αρέσουν τα πάρτι"], 1, "κοιμάται με ανοιχτά παράθυρα"),
 ],
 "gloss": {"ασύρματα": "ασύρματος — wireless", "ακουστικά": "ακουστικά — headphones", "αντιστοιχεί": "αντιστοιχώ — to correspond", "διοργανωτές": "διοργανωτής — organiser", "ενθουσιασμό": "ενθουσιασμός — enthusiasm"},
})

ITEMS.append({
 "id": "l196-rep-daneistiki-organon", "title": "Μια δανειστική βιβλιοθήκη μουσικών οργάνων", "title_en": "A library that lends musical instruments", "type": "report", "level": "B2",
 "context_el": "Ρεπορτάζ για μια δημοτική βιβλιοθήκη που δανείζει μουσικά όργανα.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο υπόγειο της δημοτικής βιβλιοθήκης, ανάμεσα στα ράφια με τα παλιά περιοδικά, κρέμονται κιθάρες, βιολιά, ένα τσέλο, δύο μπουζούκια και ένα ακορντεόν. Δεν είναι έκθεση: όλα αυτά δανείζονται, όπως τα βιβλία, για τρεις εβδομάδες.", "In the basement of the municipal library, among the shelves of old magazines, hang guitars, violins, a cello, two bouzoukis and an accordion. It isn't an exhibition: all of these are lent out, like books, for three weeks."),
  L("Ρεπόρτερ", "m", "Τα περισσότερα όργανα τα δώρισαν κάτοικοι της πόλης, που τα είχαν ξεχάσει σε ντουλάπες και πατάρια. Ένας μουσικός του τοπικού ωδείου τα επισκευάζει εθελοντικά και τα ελέγχει κάθε φορά που επιστρέφουν.", "Most of the instruments were donated by residents of the town, who had forgotten them in wardrobes and lofts. A musician from the local music school repairs them voluntarily and checks them every time they come back."),
  L("Ρεπόρτερ", "m", "Η ιδέα είναι απλή: πολλά παιδιά θέλουν να δοκιμάσουν ένα όργανο, αλλά οι γονείς διστάζουν να αγοράσουν ένα βιολί τριακοσίων ευρώ που μπορεί να μείνει στη γωνία μετά από δύο μήνες. Με τον δανεισμό, το παιδί δοκιμάζει χωρίς κόστος. Αν του αρέσει, συνεχίζει· αν όχι, το όργανο πάει σε κάποιον άλλο.", "The idea is simple: many children want to try an instrument, but parents hesitate to buy a three-hundred-euro violin that might stay in the corner after two months. With lending, the child tries without cost. If they like it, they continue; if not, the instrument goes to someone else."),
  L("Ρεπόρτερ", "m", "Δεν δανείζονται μόνο παιδιά. Η πιο πιστή «αναγνώστρια» είναι μια συνταξιούχος, που δανείζεται το ίδιο ακορντεόν για πέμπτη φορά. Η βιβλιοθήκη σκέφτεται να της το χαρίσει.", "It isn't only children who borrow. The most loyal 'reader' is a pensioner who is borrowing the same accordion for the fifth time. The library is thinking of giving it to her."),
 ],
 "questions": [
  Q("Για πόσο καιρό δανείζονται τα όργανα;", ["Για μία εβδομάδα", "Για τρεις εβδομάδες", "Για έναν μήνα", "Για ένα καλοκαίρι"], 1, "δανείζονται, όπως τα βιβλία, για τρεις εβδομάδες"),
  Q("Από πού προέρχονται τα περισσότερα όργανα;", ["Τα αγόρασε ο δήμος", "Τα δώρισαν κάτοικοι της πόλης", "Τα έδωσε το ωδείο", "Τα έφτιαξε ένας μουσικός"], 1, "Τα περισσότερα όργανα τα δώρισαν κάτοικοι της πόλης"),
  Q("Ποιο πρόβλημα λύνει ο δανεισμός;", ["Οι γονείς διστάζουν να αγοράσουν ακριβό όργανο που μπορεί να μη χρησιμοποιηθεί", "Δεν υπάρχουν δάσκαλοι μουσικής", "Τα όργανα πιάνουν χώρο στο σπίτι", "Το ωδείο είναι μακριά"], 0, "οι γονείς διστάζουν να αγοράσουν ένα βιολί τριακοσίων ευρώ"),
 ],
 "gloss": {"υπόγειο": "υπόγειο — basement", "τσέλο": "τσέλο — cello", "πατάρια": "πατάρι — loft, storage space above", "εθελοντικά": "εθελοντικά — voluntarily", "διστάζουν": "διστάζω — to hesitate", "πιστή": "πιστός — loyal, faithful"},
})

ITEMS.append({
 "id": "l196-news-teleftaia-trapeza", "title": "Κλείνει το τελευταίο υποκατάστημα τράπεζας του νησιού", "title_en": "The island's last bank branch is closing", "type": "news", "level": "B2",
 "context_el": "Είδηση από περιφερειακό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Μεγάλη αναστάτωση επικρατεί σε μικρό νησί των Κυκλάδων, μετά την ανακοίνωση ότι το μοναδικό υποκατάστημα τράπεζας θα κλείσει στο τέλος του μήνα. Η τράπεζα αναφέρει ότι οι περισσότερες συναλλαγές γίνονται πλέον ηλεκτρονικά και ότι το κόστος λειτουργίας είναι πολύ υψηλό για τον μικρό αριθμό πελατών.", "There is turmoil on a small island in the Cyclades, after the announcement that the only bank branch will close at the end of the month. The bank states that most transactions are now done electronically and that the operating cost is too high for the small number of customers."),
  L("Εκφωνήτρια", "f", "Οι κάτοικοι, πολλοί από τους οποίους είναι ηλικιωμένοι, λένε ότι δεν χρησιμοποιούν εφαρμογές στο κινητό και ότι θα αναγκάζονται να ταξιδεύουν με το πλοίο ως τη Νάξο για μια απλή ανάληψη. Ο πρόεδρος της κοινότητας έστειλε επιστολή στην τράπεζα και ζητά να παραμείνει τουλάχιστον το ΑΤΜ.", "The residents, many of whom are elderly, say they don't use mobile apps and that they will be forced to travel by ferry to Naxos for a simple withdrawal. The community president has sent a letter to the bank and is asking for at least the ATM to remain."),
  L("Εκφωνήτρια", "f", "Σύμφωνα με πληροφορίες, η τράπεζα εξετάζει να στέλνει ένα κινητό υποκατάστημα, ένα ειδικά διαμορφωμένο φορτηγάκι, μία φορά την εβδομάδα. Παράλληλα, ο δήμος οργανώνει δωρεάν μαθήματα ηλεκτρονικής τραπεζικής για όσους ενδιαφέρονται, στο κοινοτικό γραφείο.", "According to reports, the bank is considering sending a mobile branch, a specially fitted van, once a week. At the same time, the municipality is organising free online banking lessons for anyone interested, at the community office."),
 ],
 "questions": [
  Q("Γιατί κλείνει το υποκατάστημα σύμφωνα με την τράπεζα;", ["Λόγω ληστείας", "Γιατί οι συναλλαγές γίνονται πια ηλεκτρονικά και το κόστος είναι υψηλό", "Γιατί το κτίριο είναι παλιό", "Γιατί δεν βρίσκουν υπαλλήλους"], 1, "οι περισσότερες συναλλαγές γίνονται πλέον ηλεκτρονικά"),
  Q("Τι ζητά ο πρόεδρος της κοινότητας;", ["Να μείνει τουλάχιστον το ΑΤΜ", "Να ανοίξει νέο υποκατάστημα", "Δωρεάν εισιτήρια για τη Νάξο", "Χρήματα για τον δήμο"], 0, "ζητά να παραμείνει τουλάχιστον το ΑΤΜ"),
  Q("Τι οργανώνει ο δήμος;", ["Δρομολόγια για τη Νάξο", "Δωρεάν μαθήματα ηλεκτρονικής τραπεζικής", "Μια διαμαρτυρία", "Ένα δεύτερο ΑΤΜ"], 1, "ο δήμος οργανώνει δωρεάν μαθήματα ηλεκτρονικής τραπεζικής"),
 ],
 "gloss": {"υποκατάστημα": "υποκατάστημα — branch", "αναστάτωση": "αναστάτωση — turmoil, upset", "συναλλαγές": "συναλλαγή — transaction", "ανάληψη": "ανάληψη — withdrawal", "διαμορφωμένο": "διαμορφωμένος — fitted out, adapted"},
})

ITEMS.append({
 "id": "l196-c1-int-mesimerianos-ypnos", "title": "Η επιστήμη του μεσημεριανού ύπνου", "title_en": "The science of the afternoon nap", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με μια ερευνήτρια του ύπνου σε εκπομπή για την υγεία.",
 "script": [
  L("Δημοσιογράφος", "m", "Ο μεσημεριανός ύπνος ήταν κάποτε θεσμός στην Ελλάδα. Σήμερα πολλοί τον θεωρούν πολυτέλεια ή και τεμπελιά. Τι λέει η επιστήμη;", "The afternoon nap was once an institution in Greece. Today many consider it a luxury or even laziness. What does science say?"),
  L("Ερευνήτρια", "f", "Λέει ότι η τάση να νυστάζουμε νωρίς το απόγευμα δεν οφείλεται μόνο στο φαγητό, όπως συχνά νομίζουμε. Ο βιολογικός μας ρυθμός φαίνεται να έχει μια μικρή «βύθιση» της εγρήγορσης εκείνες τις ώρες, ακόμα κι αν δεν έχουμε φάει. Ο μεσημεριανός ύπνος, με άλλα λόγια, δεν είναι πολιτισμική ιδιοτροπία· ανταποκρίνεται σε κάτι που συμβαίνει στο σώμα.", "It says that the tendency to feel sleepy early in the afternoon isn't due only to food, as we often think. Our biological rhythm seems to have a small 'dip' in alertness at those hours, even if we haven't eaten. The afternoon nap, in other words, isn't a cultural quirk; it responds to something happening in the body."),
  L("Δημοσιογράφος", "m", "Πόσο πρέπει να κρατά;", "How long should it last?"),
  L("Ερευνήτρια", "f", "Εδώ είναι το κρίσιμο σημείο. Ένας σύντομος ύπνος, είκοσι περίπου λεπτών, φαίνεται να βελτιώνει την προσοχή και τη διάθεση χωρίς παρενέργειες. Αν όμως κοιμηθούμε μιάμιση ώρα, είναι πιθανό να ξυπνήσουμε μέσα από βαθύ ύπνο, βαριοί και μπερδεμένοι, και να δυσκολευτούμε να κοιμηθούμε το βράδυ. Γι' αυτό πολλοί που λένε «ο μεσημεριανός ύπνος δεν μου κάνει» απλώς κοιμούνται πολύ.", "This is the crucial point. A short sleep, about twenty minutes, seems to improve attention and mood without side effects. But if we sleep for an hour and a half, we're likely to wake up out of deep sleep, heavy and confused, and to have trouble falling asleep at night. That's why many who say 'naps don't agree with me' are simply sleeping too long."),
  L("Δημοσιογράφος", "m", "Υπάρχουν μελέτες που τον συνδέουν με την υγεία της καρδιάς. Ισχύει;", "There are studies that link it to heart health. Is that true?"),
  L("Ερευνήτρια", "f", "Υπάρχουν, και μάλιστα μία γνωστή μελέτη έγινε σε Έλληνες. Πρέπει όμως να είμαστε προσεκτικοί: τέτοιες μελέτες δείχνουν συσχέτιση, όχι απαραίτητα αιτία. Άλλες έρευνες έχουν βρει ότι ο συχνός και μακρύς μεσημεριανός ύπνος σε ηλικιωμένους μπορεί να είναι σημάδι ότι ο νυχτερινός τους ύπνος δεν είναι καλός. Η εικόνα, λοιπόν, δεν είναι ακόμα ξεκάθαρη. Αυτό που μπορώ να πω με βεβαιότητα είναι ότι ένας σύντομος υπνάκος δεν βλάπτει κανέναν.", "There are, and in fact one well-known study was done on Greeks. But we must be careful: such studies show correlation, not necessarily cause. Other research has found that frequent, long naps in older people may be a sign that their night-time sleep isn't good. So the picture isn't clear yet. What I can say with certainty is that a short nap doesn't harm anyone."),
 ],
 "questions": [
  Q("Σε τι οφείλεται, σύμφωνα με την ερευνήτρια, η νύστα του απογεύματος;", ["Μόνο στο φαγητό", "Και σε μια φυσική πτώση της εγρήγορσης στον βιολογικό μας ρυθμό", "Στην τεμπελιά", "Στη ζέστη"], 1, "Ο βιολογικός μας ρυθμός φαίνεται να έχει μια μικρή «βύθιση» της εγρήγορσης"),
  Q("Γιατί πολλοί νιώθουν άσχημα μετά τον μεσημεριανό ύπνο;", ["Γιατί κοιμούνται πολύ και ξυπνούν μέσα από βαθύ ύπνο", "Γιατί κοιμούνται πολύ λίγο", "Γιατί τρώνε πριν κοιμηθούν", "Γιατί κοιμούνται σε καναπέ"], 0, "απλώς κοιμούνται πολύ"),
  Q("Πώς αντιμετωπίζει τις μελέτες για την καρδιά;", ["Ως απόδειξη ότι ο μεσημεριανός ύπνος προστατεύει την καρδιά", "Με προσοχή, γιατί δείχνουν συσχέτιση και όχι απαραίτητα αιτία", "Ως λανθασμένες", "Ως άσχετες με τους Έλληνες"], 1, "τέτοιες μελέτες δείχνουν συσχέτιση, όχι απαραίτητα αιτία"),
 ],
 "gloss": {"θεσμός": "θεσμός — institution", "εγρήγορσης": "εγρήγορση — alertness", "ιδιοτροπία": "ιδιοτροπία — quirk, whim", "παρενέργειες": "παρενέργεια — side effect", "συσχέτιση": "συσχέτιση — correlation", "υπνάκος": "υπνάκος — nap, short sleep"},
})

ITEMS.append({
 "id": "l196-c1-mono-i-foni-mas", "title": "Γιατί η φωνή μας ακούγεται παράξενη στις ηχογραφήσεις;", "title_en": "Why does our voice sound strange on recordings?", "type": "monologue", "level": "C1",
 "context_el": "Απόσπασμα από podcast εκλαΐκευσης της επιστήμης.",
 "script": [
  L("Παρουσιαστής", "m", "Είναι μια από τις πιο κοινές μικρές ταπεινώσεις της σύγχρονης ζωής: ακούμε ένα φωνητικό μήνυμα που στείλαμε και αναρωτιόμαστε ποιος είναι αυτός ο άνθρωπος με τη λεπτή, σχεδόν ξένη φωνή. Κι όμως, αυτή είναι η φωνή που ακούνε όλοι οι άλλοι κάθε μέρα.", "It's one of the most common small humiliations of modern life: we listen to a voice message we sent and wonder who this person with the thin, almost foreign voice is. And yet that's the voice everyone else hears every day."),
  L("Παρουσιαστής", "m", "Η εξήγηση βρίσκεται στον δρόμο που ακολουθεί ο ήχος. Όταν μιλάμε, ακούμε τη φωνή μας με δύο τρόπους ταυτόχρονα: μέσα από τον αέρα, όπως όλοι, αλλά και μέσα από τα οστά του κρανίου, που μεταφέρουν τις δονήσεις κατευθείαν στο εσωτερικό αυτί. Τα οστά ευνοούν τις χαμηλές συχνότητες, κι έτσι η φωνή που ακούμε μέσα μας είναι πιο βαθιά και πιο γεμάτη από την πραγματική.", "The explanation lies in the path the sound takes. When we speak, we hear our voice in two ways at once: through the air, like everyone else, but also through the bones of the skull, which carry the vibrations straight to the inner ear. Bones favour low frequencies, and so the voice we hear inside is deeper and fuller than the real one."),
  L("Παρουσιαστής", "m", "Η ηχογράφηση μάς στερεί αυτό το μπάσο συμπλήρωμα και μας φέρνει αντιμέτωπους με τη φωνή όπως τη μεταφέρει μόνο ο αέρας. Υπάρχει όμως και ένας ψυχολογικός παράγοντας: κάποιοι ερευνητές υποστηρίζουν ότι μας ενοχλεί η απόσταση ανάμεσα στην εικόνα που έχουμε για τον εαυτό μας και σε αυτό που ακούμε. Ενδιαφέρον είναι ότι, σε ορισμένα πειράματα, όταν οι συμμετέχοντες άκουγαν τη φωνή τους χωρίς να την αναγνωρίζουν, τη βαθμολογούσαν πιο θετικά απ' ό,τι όταν ήξεραν ότι ήταν δική τους.", "The recording deprives us of that bass supplement and confronts us with the voice as air alone carries it. But there's also a psychological factor: some researchers argue that what bothers us is the gap between the image we have of ourselves and what we hear. Interestingly, in some experiments, when participants heard their voice without recognising it, they rated it more positively than when they knew it was theirs."),
  L("Παρουσιαστής", "m", "Η καλή είδηση είναι ότι η δυσφορία μειώνεται με τη συνήθεια. Οι εκφωνητές, οι ηθοποιοί και όσοι κάνουν podcast, όπως εγώ, κάποια στιγμή σταματούν να τρομάζουν. Ή, τουλάχιστον, το κρύβουν καλύτερα.", "The good news is that the discomfort decreases with habit. Announcers, actors and those who do podcasts, like me, at some point stop being startled. Or at least they hide it better."),
 ],
 "questions": [
  Q("Γιατί η φωνή που ακούμε μέσα μας είναι πιο βαθιά;", ["Γιατί τα οστά του κρανίου ευνοούν τις χαμηλές συχνότητες", "Γιατί μιλάμε πιο δυνατά απ' ό,τι νομίζουμε", "Γιατί τα μικρόφωνα παραμορφώνουν τον ήχο", "Γιατί ο αέρας απορροφά τις χαμηλές συχνότητες"], 0, "Τα οστά ευνοούν τις χαμηλές συχνότητες"),
  Q("Ποιον ψυχολογικό παράγοντα αναφέρει;", ["Τον φόβο της κριτικής", "Την απόσταση ανάμεσα στην εικόνα που έχουμε για τον εαυτό μας και σε αυτό που ακούμε", "Την κούραση", "Την έλλειψη συνήθειας με την τεχνολογία"], 1, "μας ενοχλεί η απόσταση ανάμεσα στην εικόνα που έχουμε για τον εαυτό μας"),
  Q("Τι έδειξαν ορισμένα πειράματα;", ["Ότι κανείς δεν αναγνωρίζει τη φωνή του", "Ότι όταν οι συμμετέχοντες δεν αναγνώριζαν τη φωνή τους, τη βαθμολογούσαν πιο θετικά", "Ότι οι γυναίκες ενοχλούνται περισσότερο", "Ότι η ενόχληση δεν μειώνεται ποτέ"], 1, "τη βαθμολογούσαν πιο θετικά απ' ό,τι όταν ήξεραν ότι ήταν δική τους"),
 ],
 "gloss": {"ταπεινώσεις": "ταπείνωση — humiliation", "κρανίου": "κρανίο — skull", "δονήσεις": "δόνηση — vibration", "συχνότητες": "συχνότητα — frequency", "στερεί": "στερώ — to deprive", "δυσφορία": "δυσφορία — discomfort, unease"},
})

rnd = random.Random(196)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-196.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
