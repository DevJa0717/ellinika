# Source for library/listening/listening-194.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l194.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l194-ann-kameres-tachytitas", "title": "Κάμερες ελέγχου ταχύτητας στη λεωφόρο", "title_en": "Speed cameras on the avenue", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Ο δήμος ενημερώνει τους οδηγούς ότι από την πρώτη του επόμενου μήνα θα λειτουργήσουν έξι κάμερες ελέγχου ταχύτητας στην παραλιακή λεωφόρο, από το λιμάνι μέχρι την είσοδο της πόλης. Το όριο ταχύτητας στο τμήμα αυτό είναι πενήντα χιλιόμετρα την ώρα.", "The municipality informs drivers that from the first of next month six speed cameras will be operating on the coastal avenue, from the port to the entrance of the town. The speed limit on this section is fifty kilometres an hour."),
  L("Εκφωνητής", "m", "Τον πρώτο μήνα οι κάμερες θα λειτουργούν δοκιμαστικά. Οι οδηγοί που θα ξεπερνούν το όριο δεν θα πληρώνουν πρόστιμο, αλλά θα λαμβάνουν μια ειδοποίηση στο σπίτι τους. Από τον δεύτερο μήνα, τα πρόστιμα θα στέλνονται κανονικά.", "In the first month the cameras will operate on a trial basis. Drivers who exceed the limit will not pay a fine, but will receive a notice at home. From the second month, fines will be sent as normal."),
  L("Εκφωνητής", "m", "Σύμφωνα με τα στοιχεία της τροχαίας, στη λεωφόρο έγιναν πέρσι δεκαεννιά τροχαία, τα περισσότερα τα βράδια του Σαββάτου. Παράλληλα, ο δήμος θα φτιάξει δύο νέες φωτεινές διαβάσεις για τους πεζούς, κοντά στο σχολείο και στην πλατεία. Για περισσότερες πληροφορίες, οι δημότες μπορούν να επισκεφθούν την ιστοσελίδα του δήμου.", "According to the traffic police figures, there were nineteen accidents on the avenue last year, most of them on Saturday nights. At the same time, the municipality will build two new pedestrian crossings with lights, near the school and the square. For more information, residents can visit the municipality's website."),
 ],
 "questions": [
  Q("Τι θα γίνει τον πρώτο μήνα;", ["Οι κάμερες δεν θα λειτουργούν", "Οι οδηγοί θα παίρνουν μόνο ειδοποίηση, χωρίς πρόστιμο", "Τα πρόστιμα θα είναι διπλά", "Το όριο θα είναι εξήντα"], 1, "δεν θα πληρώνουν πρόστιμο, αλλά θα λαμβάνουν μια ειδοποίηση"),
  Q("Πότε έγιναν τα περισσότερα τροχαία;", ["Τα πρωινά", "Τα βράδια του Σαββάτου", "Τον χειμώνα", "Στις ώρες των σχολείων"], 1, "τα περισσότερα τα βράδια του Σαββάτου"),
  Q("Τι άλλο θα κάνει ο δήμος;", ["Θα κλείσει τη λεωφόρο", "Θα φτιάξει δύο νέες φωτεινές διαβάσεις", "Θα φτιάξει ποδηλατόδρομο", "Θα βάλει περισσότερους τροχονόμους"], 1, "θα φτιάξει δύο νέες φωτεινές διαβάσεις για τους πεζούς"),
 ],
 "gloss": {"ταχύτητας": "ταχύτητα — speed", "παραλιακή": "παραλιακός — coastal", "δοκιμαστικά": "δοκιμαστικά — on a trial basis", "πρόστιμο": "πρόστιμο — fine", "ειδοποίηση": "ειδοποίηση — notice", "τροχαίας": "τροχαία — traffic police", "δημότες": "δημότης — resident of a municipality"},
})

ITEMS.append({
 "id": "l194-int-simatodotis-monopation", "title": "Ο άνθρωπος που σημαδεύει τα μονοπάτια", "title_en": "The man who waymarks the trails", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν εθελοντή που καθαρίζει και σημαδεύει ορεινά μονοπάτια.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι ακριβώς κάνετε στα μονοπάτια;", "What exactly do you do on the trails?"),
  L("Εθελοντής", "m", "Με μια ομάδα από δέκα άτομα καθαρίζουμε παλιά μονοπάτια που είχαν κλείσει από τα πουρνάρια και τα βάτα, και τα σημαδεύουμε, για να μη χάνονται οι πεζοπόροι. Βάφουμε μικρά κόκκινα και άσπρα σημάδια πάνω σε πέτρες και κορμούς, περίπου κάθε πενήντα μέτρα, και στις διασταυρώσεις βάζουμε ξύλινες πινακίδες.", "With a group of ten people we clear old trails that had been closed by kermes oak and brambles, and we waymark them so that hikers don't get lost. We paint small red and white marks on stones and tree trunks, roughly every fifty metres, and at junctions we put wooden signs."),
  L("Δημοσιογράφος", "f", "Πώς ξέρετε πού περνούσε ένα μονοπάτι που δεν το έχει περπατήσει κανείς για χρόνια;", "How do you know where a trail went if nobody has walked it for years?"),
  L("Εθελοντής", "m", "Ρωτάμε τους ηλικιωμένους των χωριών. Εκείνοι θυμούνται κάθε στροφή, γιατί από εκεί πήγαιναν στα χωράφια ή στο διπλανό χωριό για να παντρευτούν. Μια γιαγιά ογδόντα πέντε χρονών μάς οδήγησε μια ολόκληρη μέρα, και στο τέλος ήταν λιγότερο κουρασμένη από εμάς.", "We ask the old people in the villages. They remember every bend, because that was the way they went to the fields or to the next village to get married. An eighty-five-year-old grandmother guided us for a whole day, and at the end she was less tired than we were."),
  L("Δημοσιογράφος", "f", "Τι σας ενοχλεί περισσότερο;", "What bothers you most?"),
  L("Εθελοντής", "m", "Όταν κάποιος ανοίγει έναν χωματόδρομο για αυτοκίνητα και καταστρέφει ένα μονοπάτι πεντακοσίων χρόνων μέσα σε μια μέρα. Τα καλντερίμια φτιάχτηκαν με τα χέρια, με πέτρες από τον ίδιο τόπο. Αν χαθούν, δεν ξαναγίνονται.", "When someone opens a dirt road for cars and destroys a five-hundred-year-old trail in a single day. The cobbled paths were made by hand, with stones from the place itself. If they're lost, they can't be made again."),
 ],
 "questions": [
  Q("Πώς σημαδεύουν τα μονοπάτια;", ["Με κορδέλες στα δέντρα", "Με κόκκινα και άσπρα σημάδια και ξύλινες πινακίδες", "Με μεταλλικές ταμπέλες κάθε χιλιόμετρο", "Με εφαρμογή στο κινητό"], 1, "Βάφουμε μικρά κόκκινα και άσπρα σημάδια πάνω σε πέτρες και κορμούς"),
  Q("Πώς βρίσκουν πού περνούσαν τα παλιά μονοπάτια;", ["Από παλιούς χάρτες", "Ρωτώντας τους ηλικιωμένους των χωριών", "Με δορυφορικές φωτογραφίες", "Από τα αρχεία του δήμου"], 1, "Ρωτάμε τους ηλικιωμένους των χωριών"),
  Q("Τι τον ενοχλεί περισσότερο;", ["Οι πεζοπόροι που πετούν σκουπίδια", "Όταν ένας χωματόδρομος καταστρέφει ένα παλιό μονοπάτι", "Η έλλειψη εθελοντών", "Ο καιρός"], 1, "Όταν κάποιος ανοίγει έναν χωματόδρομο για αυτοκίνητα και καταστρέφει ένα μονοπάτι"),
 ],
 "gloss": {"σημαδεύει": "σημαδεύω — to mark, waymark", "πουρνάρια": "πουρνάρι — kermes oak", "βάτα": "βάτος — bramble", "πεζοπόροι": "πεζοπόρος — hiker", "διασταυρώσεις": "διασταύρωση — junction", "χωματόδρομο": "χωματόδρομος — dirt road", "καλντερίμια": "καλντερίμι — cobbled path"},
})

ITEMS.append({
 "id": "l194-vm-studio-ichografisis", "title": "Μήνυμα από το στούντιο ηχογράφησης", "title_en": "A message from the recording studio", "type": "voicemail", "level": "B2",
 "context_el": "Το συγκρότημά σας έχει κλείσει ώρες σε ένα στούντιο για να ηχογραφήσει τρία τραγούδια. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Ηχολήπτρια", "f", "Γεια σας, η Μυρτώ είμαι από το στούντιο, για την ηχογράφηση του Σαββάτου. Δυστυχώς ο ηχολήπτης που θα σας είχε, ο Άρης, έσπασε το χέρι του στο μπάσκετ και δεν θα μπορεί να δουλέψει για έναν μήνα. Μπορώ να αναλάβω εγώ την ηχογράφηση την ίδια μέρα, αλλά μόνο από τις δύο το μεσημέρι και μετά, όχι από τις δέκα το πρωί όπως είχαμε πει.", "Hello, it's Myrto from the studio, about Saturday's recording. Unfortunately the sound engineer you would have had, Aris, broke his arm playing basketball and won't be able to work for a month. I can take over the recording on the same day, but only from two in the afternoon onwards, not from ten in the morning as we'd agreed."),
  L("Ηχολήπτρια", "f", "Με έξι ώρες αντί για οχτώ, σας προτείνω να γράψουμε τα τύμπανα και το μπάσο όλοι μαζί, ζωντανά, και τις φωνές να τις κάνουμε σε δεύτερη συνεδρία, χωρίς επιπλέον χρέωση για τις δύο ώρες που χάνετε. Αν προτιμάτε να μείνει το πρωινό ωράριο, η επόμενη ελεύθερη μέρα είναι σε τρεις εβδομάδες.", "With six hours instead of eight, I suggest we record the drums and the bass all together, live, and do the vocals in a second session, at no extra charge for the two hours you lose. If you'd rather keep the morning slot, the next free day is in three weeks."),
  L("Ηχολήπτρια", "f", "Κάτι ακόμα: ο ντράμερ σας να φέρει τα δικά του πιατίνια, γιατί τα δικά μας είναι στο επισκευαστήριο. Και καλό θα ήταν να έχετε κάνει πρόβα με μετρονόμο, γλιτώνουμε πολύ χρόνο. Πείτε μου μέχρι την Πέμπτη τι αποφασίσατε.", "One more thing: your drummer should bring his own cymbals, because ours are at the repair shop. And it would be good if you've rehearsed with a metronome; it saves us a lot of time. Let me know by Thursday what you've decided."),
 ],
 "questions": [
  Q("Γιατί αλλάζει η ώρα της ηχογράφησης;", ["Γιατί το στούντιο έχει βλάβη", "Γιατί ο ηχολήπτης τραυματίστηκε και αναλαμβάνει η Μυρτώ, αλλά μόνο το απόγευμα", "Γιατί το συγκρότημα ζήτησε αλλαγή", "Γιατί το στούντιο είναι κλειστό το πρωί"], 1, "Μπορώ να αναλάβω εγώ την ηχογράφηση την ίδια μέρα, αλλά μόνο από τις δύο το μεσημέρι"),
  Q("Τι προτείνει για τις φωνές;", ["Να ηχογραφηθούν σε δεύτερη συνεδρία χωρίς επιπλέον χρέωση", "Να ηχογραφηθούν σε άλλο στούντιο", "Να μην ηχογραφηθούν καθόλου", "Να ηχογραφηθούν πρώτες"], 0, "τις φωνές να τις κάνουμε σε δεύτερη συνεδρία, χωρίς επιπλέον χρέωση"),
  Q("Τι πρέπει να φέρει ο ντράμερ;", ["Τα δικά του τύμπανα", "Τα δικά του πιατίνια", "Έναν μετρονόμο", "Τις παρτιτούρες"], 1, "ο ντράμερ σας να φέρει τα δικά του πιατίνια"),
 ],
 "gloss": {"ηχογράφηση": "ηχογράφηση — recording", "ηχολήπτης": "ηχολήπτης — sound engineer", "συνεδρία": "συνεδρία — session", "πιατίνια": "πιατίνι — cymbal", "επισκευαστήριο": "επισκευαστήριο — repair shop", "μετρονόμο": "μετρονόμος — metronome"},
})

ITEMS.append({
 "id": "l194-mono-pali-me-tous-goneis", "title": "Ξανά στο πατρικό στα τριάντα τέσσερα", "title_en": "Back in my parents' home at thirty-four", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα μιλά σε ένα podcast για το πώς είναι να ξαναζεί με τους γονείς της.",
 "script": [
  L("Ελπίδα", "f", "Πριν από ενάμιση χρόνο το σπίτι που νοίκιαζα πουλήθηκε, και το καινούργιο ενοίκιο που μου ζητούσαν για ένα αντίστοιχο διαμέρισμα ήταν σχεδόν ο μισός μου μισθός. Έτσι, στα τριάντα τέσσερα, μάζεψα τα πράγματά μου και γύρισα στο πατρικό, στο ίδιο δωμάτιο με τις αφίσες του λυκείου.", "A year and a half ago the house I was renting was sold, and the new rent they were asking for a similar flat was almost half my salary. So, at thirty-four, I packed my things and went back to my parents' home, to the same room with the posters from secondary school."),
  L("Ελπίδα", "f", "Τις πρώτες εβδομάδες ένιωθα σαν να είχα αποτύχει. Η μητέρα μου με ρωτούσε τι ώρα θα γυρίσω και ο πατέρας μου έκλεινε τα φώτα πίσω μου. Χρειάστηκε μια σοβαρή κουβέντα και στους τρεις μας: ότι είμαι ενήλικη, ότι πληρώνω ένα μέρος από τους λογαριασμούς, και ότι το δωμάτιό μου είναι δικός μου χώρος.", "In the first weeks I felt as if I had failed. My mother would ask me what time I'd be back and my father would turn the lights off behind me. It took a serious conversation among the three of us: that I'm an adult, that I pay part of the bills, and that my room is my own space."),
  L("Ελπίδα", "f", "Σήμερα βλέπω και τα καλά. Τώρα αποταμιεύω κάθε μήνα, και ελπίζω σε δύο χρόνια να έχω την προκαταβολή για ένα μικρό διαμέρισμα. Και γνώρισα τους γονείς μου ως ανθρώπους, όχι μόνο ως γονείς. Ξέρω πια ότι ο πατέρας μου γράφει ποιήματα και ότι η μητέρα μου ήθελε να γίνει αρχιτέκτονας. Δεν θα το ήξερα ποτέ αν δεν είχαμε ξαναζήσει μαζί.", "Today I also see the good side. I now save every month, and I hope in two years to have the deposit for a small flat. And I got to know my parents as people, not just as parents. I now know that my father writes poems and that my mother wanted to become an architect. I would never have known if we hadn't lived together again."),
 ],
 "questions": [
  Q("Γιατί γύρισε η Ελπίδα στο πατρικό;", ["Γιατί έχασε τη δουλειά της", "Γιατί το σπίτι της πουλήθηκε και τα ενοίκια ήταν πολύ ακριβά", "Γιατί αρρώστησαν οι γονείς της", "Γιατί χώρισε"], 1, "το σπίτι που νοίκιαζα πουλήθηκε"),
  Q("Πώς λύθηκαν τα πρώτα προβλήματα;", ["Με μια σοβαρή κουβέντα και των τριών", "Η Ελπίδα έφυγε για λίγο", "Οι γονείς της πήγαν στο χωριό", "Δεν λύθηκαν ακόμα"], 0, "Χρειάστηκε μια σοβαρή κουβέντα και στους τρεις μας"),
  Q("Τι ανακάλυψε για τη μητέρα της;", ["Ότι γράφει ποιήματα", "Ότι ήθελε να γίνει αρχιτέκτονας", "Ότι ζωγραφίζει", "Ότι είχε ζήσει στο εξωτερικό"], 1, "η μητέρα μου ήθελε να γίνει αρχιτέκτονας"),
 ],
 "gloss": {"πατρικό": "πατρικό — parents' home, family home", "αντίστοιχο": "αντίστοιχος — equivalent, similar", "ενήλικη": "ενήλικος — adult", "αποταμιεύω": "αποταμιεύω — to save (money)", "προκαταβολή": "προκαταβολή — deposit, down payment"},
})

ITEMS.append({
 "id": "l194-dia-deftero-aftokinito", "title": "Χρειαζόμαστε δεύτερο αυτοκίνητο;", "title_en": "Do we need a second car?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι που μετακόμισε έξω από την πόλη συζητά αν πρέπει να αγοράσει δεύτερο αυτοκίνητο.",
 "script": [
  L("Βασίλης", "m", "Από τότε που μετακομίσαμε εδώ, κάθε πρωί είναι μια περιπέτεια. Εγώ πρέπει να είμαι στο εργοστάσιο στις επτά, εσύ στο γραφείο στις εννιά, και τα παιδιά στο σχολείο στις οχτώ. Με ένα αυτοκίνητο δεν βγαίνει.", "Since we moved here, every morning is an adventure. I have to be at the factory at seven, you at the office at nine, and the children at school at eight. With one car it doesn't work."),
  L("Χαρά", "f", "Το ξέρω, αλλά ένα δεύτερο αυτοκίνητο σημαίνει δεύτερη ασφάλεια, δεύτερα τέλη κυκλοφορίας, βενζίνη, σέρβις. Υπολόγισα ότι θα μας κοστίζει πάνω από διακόσια ευρώ τον μήνα, ακόμα κι αν πάρουμε ένα μεταχειρισμένο.", "I know, but a second car means a second insurance, second road tax, petrol, servicing. I worked out it would cost us over two hundred euros a month, even if we buy a second-hand one."),
  L("Βασίλης", "m", "Τι άλλο να κάνουμε; Το λεωφορείο περνάει μόνο τρεις φορές τη μέρα.", "What else can we do? The bus only comes three times a day."),
  L("Χαρά", "f", "Ο Νίκος, ο γείτονας, δουλεύει κι αυτός στη βιομηχανική περιοχή και ξεκινά στις επτά. Θα μπορούσατε να πηγαίνετε μαζί, μια εβδομάδα με το δικό του και μια με το δικό μας. Και για τα παιδιά, υπάρχει σχολικό λεωφορείο, αν κάνουμε αίτηση στον δήμο ως το τέλος του μήνα.", "Nikos, the neighbour, also works in the industrial area and starts at seven. You could go together, one week in his car and one in ours. And for the children, there's a school bus, if we apply to the municipality by the end of the month."),
  L("Βασίλης", "m", "Με τον Νίκο; Ακούει ραδιόφωνο στη διαπασών από το πρωί. Αλλά εντάξει, για διακόσια ευρώ τον μήνα, θα το αντέξω. Ας το δοκιμάσουμε μέχρι το καλοκαίρι, και τότε ξαναβλέπουμε.", "With Nikos? He plays the radio at full blast from the morning. But all right, for two hundred euros a month, I'll put up with it. Let's try it until the summer, and then we'll see again."),
 ],
 "questions": [
  Q("Γιατί πιστεύει ο Βασίλης ότι χρειάζονται δεύτερο αυτοκίνητο;", ["Γιατί το αυτοκίνητό τους χάλασε", "Γιατί όλοι πρέπει να είναι σε διαφορετικά μέρη το πρωί", "Γιατί η Χαρά άλλαξε δουλειά", "Γιατί το λεωφορείο ακρίβυνε"], 1, "Εγώ πρέπει να είμαι στο εργοστάσιο στις επτά, εσύ στο γραφείο στις εννιά, και τα παιδιά στο σχολείο στις οχτώ"),
  Q("Τι προτείνει η Χαρά;", ["Να πηγαίνει ο Βασίλης στη δουλειά με τον γείτονα", "Να αγοράσουν ποδήλατα", "Να μετακομίσουν πάλι στην πόλη", "Να αλλάξει δουλειά ο Βασίλης"], 0, "Θα μπορούσατε να πηγαίνετε μαζί"),
  Q("Τι πρέπει να κάνουν για το σχολικό λεωφορείο;", ["Να πληρώσουν συνδρομή", "Να κάνουν αίτηση στον δήμο ως το τέλος του μήνα", "Να μιλήσουν με τον διευθυντή", "Τίποτα, είναι αυτόματο"], 1, "αν κάνουμε αίτηση στον δήμο ως το τέλος του μήνα"),
 ],
 "gloss": {"περιπέτεια": "περιπέτεια — adventure", "τέλη": "τέλη κυκλοφορίας — road tax", "μεταχειρισμένο": "μεταχειρισμένος — second-hand", "βιομηχανική": "βιομηχανικός — industrial", "διαπασών": "στη διαπασών — at full blast"},
})

ITEMS.append({
 "id": "l194-rep-piano-sto-stathmo", "title": "Ένα πιάνο στον σιδηροδρομικό σταθμό", "title_en": "A piano at the railway station", "type": "report", "level": "B2",
 "context_el": "Ρεπορτάζ για ένα πιάνο που τοποθετήθηκε στην αίθουσα αναμονής ενός σιδηροδρομικού σταθμού.",
 "script": [
  L("Ρεπόρτερ", "f", "Στην αίθουσα αναμονής του σταθμού, ανάμεσα στα εκδοτήρια και στο κιόσκι με τα περιοδικά, υπάρχει εδώ και δύο μήνες ένα παλιό όρθιο πιάνο. Δεν ανήκει σε κανέναν. Πάνω του μια πινακίδα γράφει μόνο: «Παίξτε ελεύθερα».", "In the station waiting room, between the ticket offices and the magazine kiosk, there has been an old upright piano for two months. It doesn't belong to anyone. On it a sign says only: 'Play freely.'"),
  L("Ρεπόρτερ", "f", "Το πιάνο το δώρισε μια συνταξιούχος δασκάλα μουσικής, που μετακόμισε σε μικρότερο σπίτι και δεν ήθελε να το πουλήσει. Ο σιδηρόδρομος δέχτηκε να το φιλοξενήσει δοκιμαστικά για έξι μήνες. Ένας κουρδιστής το περνάει δωρεάν κάθε τρεις εβδομάδες.", "The piano was donated by a retired music teacher, who moved to a smaller house and didn't want to sell it. The railway agreed to host it on a trial basis for six months. A tuner goes over it free of charge every three weeks."),
  L("Ρεπόρτερ", "f", "Ποιοι παίζουν; Λίγο πολύ όλοι. Ένας φοιτητής που περιμένει το τρένο για τη Θεσσαλονίκη παίζει Σοπέν. Ένα κοριτσάκι επτά χρονών παίζει με ένα δάχτυλο μια μελωδία από κινούμενα σχέδια. Ένας οδηγός ταξί, που δεν είχε αγγίξει πιάνο από παιδί, κάθεται κάθε Πέμπτη στο διάλειμμά του και ξαναμαθαίνει.", "Who plays? More or less everyone. A student waiting for the train to Thessaloniki plays Chopin. A seven-year-old girl plays a tune from cartoons with one finger. A taxi driver, who hadn't touched a piano since childhood, sits down every Thursday on his break and is learning again."),
  L("Ρεπόρτερ", "f", "Υπήρξαν και παράπονα: κάποιοι εργαζόμενοι στα εκδοτήρια λένε ότι μετά από οχτώ ώρες η ίδια μελωδία γίνεται κουραστική. Γι' αυτό το πιάνο κλειδώνεται πια στις δέκα το βράδυ. Αν η δοκιμή πετύχει, ο σιδηρόδρομος σκέφτεται να βάλει πιάνα και σε άλλους σταθμούς.", "There have also been complaints: some ticket-office staff say that after eight hours the same tune becomes tiring. That's why the piano is now locked at ten in the evening. If the trial succeeds, the railway is thinking of putting pianos in other stations too."),
 ],
 "questions": [
  Q("Από πού προήλθε το πιάνο;", ["Το αγόρασε ο σιδηρόδρομος", "Το δώρισε μια συνταξιούχος δασκάλα μουσικής", "Το βρήκαν σε αποθήκη του σταθμού", "Το έφερε ένας φοιτητής"], 1, "Το πιάνο το δώρισε μια συνταξιούχος δασκάλα μουσικής"),
  Q("Τι κάνει ο οδηγός ταξί;", ["Παίζει Σοπέν κάθε πρωί", "Ξαναμαθαίνει πιάνο κάθε Πέμπτη στο διάλειμμά του", "Κουρδίζει το πιάνο", "Διδάσκει παιδιά"], 1, "κάθεται κάθε Πέμπτη στο διάλειμμά του και ξαναμαθαίνει"),
  Q("Γιατί κλειδώνεται το πιάνο στις δέκα το βράδυ;", ["Για να μην το κλέψουν", "Λόγω παραπόνων από εργαζόμενους", "Γιατί κλείνει ο σταθμός", "Για να το κουρδίζουν"], 1, "Γι' αυτό το πιάνο κλειδώνεται πια στις δέκα το βράδυ"),
 ],
 "gloss": {"εκδοτήρια": "εκδοτήριο — ticket office", "όρθιο": "όρθιος — upright", "δοκιμαστικά": "δοκιμαστικά — on a trial basis", "κουρδιστής": "κουρδιστής — (piano) tuner", "κλειδώνεται": "κλειδώνομαι — to be locked"},
})

ITEMS.append({
 "id": "l194-rep-voyvo-me-zontani-mousiki", "title": "Βωβός κινηματογράφος με ζωντανή μουσική", "title_en": "Silent films with live music", "type": "report", "level": "B2",
 "context_el": "Ρεπορτάζ από μια προβολή βωβής ταινίας με ορχήστρα που παίζει ζωντανά.",
 "script": [
  L("Ρεπόρτερ", "m", "Η αίθουσα είναι γεμάτη, αλλά κανείς δεν κοιτάζει το κινητό του. Στην οθόνη, ένας άντρας με μουστάκι κρέμεται από τους δείκτες ενός ρολογιού. Και κάτω από την οθόνη, σε ένα μικρό σκοτεινό χώρο, ένα πιάνο, ένα βιολί και ένα κρουστό ακολουθούν κάθε του κίνηση.", "The hall is full, but nobody is looking at their phone. On the screen, a man with a moustache hangs from the hands of a clock. And below the screen, in a small dark space, a piano, a violin and a percussion instrument follow his every move."),
  L("Ρεπόρτερ", "m", "Η ομάδα παρουσιάζει κάθε μήνα μια ταινία από την εποχή του βωβού κινηματογράφου, πριν από το 1930. Τη μουσική τη γράφουν οι ίδιοι, αφού παρακολουθήσουν την ταινία δεκάδες φορές. Σε πολλά σημεία όμως αυτοσχεδιάζουν, γιατί, όπως λέει ο πιανίστας, «κάθε κοινό γελάει σε άλλο σημείο, και πρέπει να περιμένουμε το γέλιο».", "The group presents a film from the silent era, before 1930, every month. They write the music themselves, after watching the film dozens of times. In many places, though, they improvise, because, as the pianist says, 'every audience laughs at a different point, and we have to wait for the laugh.'"),
  L("Ρεπόρτερ", "m", "Αυτό που κάνουν δεν είναι καινούργιο. Στα πρώτα χρόνια του σινεμά, οι ταινίες σπάνια προβάλλονταν σε απόλυτη σιωπή: σε πολλές αίθουσες έπαιζε ένας πιανίστας ή και ολόκληρη ορχήστρα. Όταν ήρθε ο ήχος, πολλοί μουσικοί έμειναν χωρίς δουλειά από τη μια μέρα στην άλλη.", "What they do isn't new. In the early years of cinema, films were rarely shown in complete silence: in many halls a pianist or even a whole orchestra played. When sound arrived, many musicians were left without work overnight."),
  L("Ρεπόρτερ", "m", "Το κοινό είναι απροσδόκητα νεανικό. Μια φοιτήτρια μου λέει ότι ήρθε για πρώτη φορά από περιέργεια και τώρα δεν χάνει καμία προβολή. «Είναι σαν να βλέπεις συναυλία και ταινία μαζί, και καμία βραδιά δεν είναι ίδια με την άλλη».", "The audience is unexpectedly young. A student tells me she came for the first time out of curiosity and now never misses a screening. 'It's like seeing a concert and a film together, and no evening is the same as another.'"),
 ],
 "questions": [
  Q("Πώς δημιουργεί η ομάδα τη μουσική;", ["Χρησιμοποιεί την αρχική μουσική της ταινίας", "Τη γράφει μόνη της και σε πολλά σημεία αυτοσχεδιάζει", "Παίζει γνωστά κλασικά έργα", "Παίζει μόνο αυτοσχεδιασμούς"], 1, "Τη μουσική τη γράφουν οι ίδιοι"),
  Q("Γιατί πρέπει να «περιμένουν το γέλιο»;", ["Γιατί η ταινία είναι πολύ αργή", "Γιατί κάθε κοινό γελάει σε διαφορετικό σημείο", "Γιατί ο πιανίστας γελάει κι αυτός", "Γιατί η μουσική είναι πολύ δυνατή"], 1, "κάθε κοινό γελάει σε άλλο σημείο"),
  Q("Τι έγινε με τους μουσικούς όταν ήρθε ο ήχος στο σινεμά;", ["Έγιναν ηθοποιοί", "Πολλοί έμειναν χωρίς δουλειά", "Άρχισαν να ηχογραφούν ταινίες", "Πήγαν στο θέατρο"], 1, "πολλοί μουσικοί έμειναν χωρίς δουλειά από τη μια μέρα στην άλλη"),
 ],
 "gloss": {"βωβού": "βωβός — silent, mute", "δείκτες": "δείκτης — hand (of a clock)", "κρουστό": "κρουστό — percussion instrument", "αυτοσχεδιάζουν": "αυτοσχεδιάζω — to improvise", "απροσδόκητα": "απροσδόκητα — unexpectedly"},
})

ITEMS.append({
 "id": "l194-news-arkouda-stin-plateia", "title": "Αρκούδα στην πλατεία του χωριού", "title_en": "A bear in the village square", "type": "news", "level": "B2",
 "context_el": "Είδηση από τοπικό ραδιόφωνο της Δυτικής Μακεδονίας.",
 "script": [
  L("Εκφωνήτρια", "f", "Ασυνήθιστος επισκέπτης στην κεντρική πλατεία ορεινού χωριού της Καστοριάς τα ξημερώματα της Τρίτης. Μια νεαρή αρκούδα κατέβηκε από το δάσος, πέρασε δίπλα από την εκκλησία και σταμάτησε στους κάδους απορριμμάτων πίσω από την ταβέρνα, όπου έψαξε για τροφή για περίπου είκοσι λεπτά.", "An unusual visitor in the central square of a mountain village in Kastoria in the early hours of Tuesday. A young bear came down from the forest, walked past the church and stopped at the rubbish bins behind the tavern, where it searched for food for about twenty minutes."),
  L("Εκφωνήτρια", "f", "Τη σκηνή κατέγραψε η κάμερα ασφαλείας του καφενείου. Κανείς δεν τραυματίστηκε, και το ζώο απομακρύνθηκε μόνο του προς το δάσος όταν άρχισαν να γαβγίζουν τα σκυλιά του χωριού.", "The scene was recorded by the café's security camera. No one was injured, and the animal moved away on its own towards the forest when the village dogs began to bark."),
  L("Εκφωνήτρια", "f", "Σύμφωνα με περιβαλλοντική οργάνωση που παρακολουθεί τον πληθυσμό της αρκούδας στην περιοχή, τέτοιες επισκέψεις γίνονται πιο συχνές το φθινόπωρο, όταν τα ζώα τρώνε όσο περισσότερο μπορούν πριν από τον χειμώνα. Η οργάνωση συνιστά στους κατοίκους να μην αφήνουν σκουπίδια ή φρούτα έξω τη νύχτα και, αν συναντήσουν αρκούδα, να μην τρέξουν αλλά να απομακρυνθούν αργά.", "According to an environmental organisation that monitors the bear population in the area, such visits become more frequent in autumn, when the animals eat as much as they can before winter. The organisation advises residents not to leave rubbish or fruit outside at night and, if they meet a bear, not to run but to move away slowly."),
  L("Εκφωνήτρια", "f", "Ο δήμος ανακοίνωσε ότι θα τοποθετήσει ειδικούς κάδους που δεν ανοίγουν εύκολα από ζώα στα τρία χωριά που είναι πιο κοντά στο δάσος.", "The municipality announced that it will install special bins that animals can't open easily in the three villages closest to the forest."),
 ],
 "questions": [
  Q("Τι έκανε η αρκούδα στην πλατεία;", ["Μπήκε στην ταβέρνα", "Έψαξε για τροφή στους κάδους απορριμμάτων", "Επιτέθηκε σε σκυλιά", "Κοιμήθηκε δίπλα στην εκκλησία"], 1, "σταμάτησε στους κάδους απορριμμάτων πίσω από την ταβέρνα, όπου έψαξε για τροφή"),
  Q("Γιατί είναι πιο συχνές τέτοιες επισκέψεις το φθινόπωρο;", ["Γιατί κόβονται δέντρα", "Γιατί τα ζώα τρώνε όσο μπορούν πριν από τον χειμώνα", "Γιατί υπάρχουν περισσότεροι τουρίστες", "Γιατί κάνει κρύο στο δάσος"], 1, "όταν τα ζώα τρώνε όσο περισσότερο μπορούν πριν από τον χειμώνα"),
  Q("Τι θα κάνει ο δήμος;", ["Θα περιφράξει το δάσος", "Θα τοποθετήσει ειδικούς κάδους", "Θα μεταφέρει την αρκούδα αλλού", "Θα κλείσει την πλατεία τη νύχτα"], 1, "θα τοποθετήσει ειδικούς κάδους"),
 ],
 "gloss": {"ξημερώματα": "ξημερώματα — early morning hours, dawn", "απορριμμάτων": "απορρίμματα — rubbish, refuse", "απομακρύνθηκε": "απομακρύνομαι — to move away", "γαβγίζουν": "γαβγίζω — to bark", "συνιστά": "συνιστώ — to advise, recommend"},
})

ITEMS.append({
 "id": "l194-c1-int-glossologos-vrisies", "title": "Μια γλωσσολόγος μιλά για τις βρισιές", "title_en": "A linguist on swearing", "type": "interview", "level": "C1",
 "context_el": "Ραδιοφωνική συνέντευξη με γλωσσολόγο που μελετά τις βρισιές και τη λειτουργία τους στον προφορικό λόγο.",
 "script": [
  L("Δημοσιογράφος", "m", "Δεν είναι λίγο παράξενο να αφιερώνει κανείς την επιστημονική του καριέρα στις βρισιές;", "Isn't it a bit strange to devote one's scientific career to swear words?"),
  L("Γλωσσολόγος", "f", "Μόνο αν θεωρήσουμε ότι η γλωσσολογία ασχολείται με τη γλώσσα όπως θα έπρεπε να είναι, και όχι όπως είναι. Οι βρισιές υπάρχουν, απ' ό,τι γνωρίζουμε, σε όλες τις γλώσσες που έχουν μελετηθεί, και αυτό από μόνο του δείχνει ότι εξυπηρετούν κάποια ανάγκη. Το ερώτημα είναι ποια.", "Only if we consider that linguistics deals with language as it ought to be, and not as it is. Swear words exist, as far as we know, in all the languages that have been studied, and that in itself shows that they serve some need. The question is which one."),
  L("Δημοσιογράφος", "m", "Και ποια είναι;", "And what is it?"),
  L("Γλωσσολόγος", "f", "Περισσότερες από μία. Η πιο προφανής είναι η εκτόνωση: όταν χτυπάμε το δάχτυλό μας στην πόρτα, η βρισιά βγαίνει σχεδόν αντανακλαστικά. Υπάρχουν μάλιστα πειράματα που δείχνουν ότι οι συμμετέχοντες άντεχαν περισσότερο με το χέρι μέσα σε παγωμένο νερό όταν τους επιτρεπόταν να βρίζουν, αν και τα ευρήματα αυτά δεν πρέπει να γενικεύονται βιαστικά. Μετά υπάρχει η επιτατική χρήση, όπου η βρισιά απλώς δίνει έμφαση, χωρίς να προσβάλλει κανέναν. Και, ίσως το πιο ενδιαφέρον, η κοινωνική: ανάμεσα σε φίλους, μια βρισιά μπορεί να λειτουργεί σχεδόν ως έκφραση οικειότητας.", "More than one. The most obvious is release: when we stub our toe on the door, the swear word comes out almost reflexively. There are in fact experiments showing that participants held out longer with their hand in ice-cold water when they were allowed to swear, although these findings shouldn't be generalised hastily. Then there's the intensifying use, where the swear word simply adds emphasis, without insulting anyone. And, perhaps the most interesting, the social one: among friends, a swear word can function almost as an expression of intimacy."),
  L("Δημοσιογράφος", "m", "Δηλαδή η ίδια λέξη μπορεί να είναι προσβολή ή χάδι;", "So the same word can be an insult or a caress?"),
  L("Γλωσσολόγος", "f", "Ακριβώς. Αυτό που μετράει δεν είναι η λέξη αλλά η σχέση, ο τόνος και το πλαίσιο. Γι' αυτό και οι μαθητές μιας ξένης γλώσσας δυσκολεύονται τόσο: μαθαίνουν τη λέξη από ένα λεξικό, αλλά όχι το πότε, το με ποιον και το πώς. Η συμβουλή μου προς αυτούς είναι απλή: να τις καταλαβαίνουν όλες, αλλά να τις χρησιμοποιούν πολύ προσεκτικά, μέχρι να νιώσουν το βάρος τους.", "Exactly. What matters isn't the word but the relationship, the tone and the context. That's also why learners of a foreign language find it so hard: they learn the word from a dictionary, but not the when, the with whom and the how. My advice to them is simple: understand them all, but use them very carefully, until they feel their weight."),
 ],
 "questions": [
  Q("Τι συμπεραίνει η γλωσσολόγος από το ότι οι βρισιές υπάρχουν σε όλες τις γλώσσες που έχουν μελετηθεί;", ["Ότι είναι αδύνατο να εξαλειφθούν", "Ότι εξυπηρετούν κάποια ανάγκη", "Ότι προέρχονται από μια κοινή γλώσσα", "Ότι δεν αξίζουν μελέτη"], 1, "αυτό από μόνο του δείχνει ότι εξυπηρετούν κάποια ανάγκη"),
  Q("Πώς παρουσιάζει τα ευρήματα για το παγωμένο νερό;", ["Ως αποδεδειγμένο γενικό νόμο", "Ως ενδιαφέροντα, αλλά όχι για βιαστική γενίκευση", "Ως λανθασμένα", "Ως δικά της πειράματα"], 1, "αν και τα ευρήματα αυτά δεν πρέπει να γενικεύονται βιαστικά"),
  Q("Γιατί δυσκολεύονται οι μαθητές ξένων γλωσσών με τις βρισιές;", ["Γιατί δεν υπάρχουν στα λεξικά", "Γιατί δεν μαθαίνουν πότε, με ποιον και πώς χρησιμοποιούνται", "Γιατί οι δάσκαλοι τις απαγορεύουν", "Γιατί είναι δύσκολες στην προφορά"], 1, "μαθαίνουν τη λέξη από ένα λεξικό, αλλά όχι το πότε, το με ποιον και το πώς"),
 ],
 "gloss": {"εκτόνωση": "εκτόνωση — release (of tension), letting off steam", "αντανακλαστικά": "αντανακλαστικά — reflexively", "επιτατική": "επιτατικός — intensifying, emphatic", "οικειότητας": "οικειότητα — intimacy, familiarity", "πλαίσιο": "πλαίσιο — context, frame"},
})

ITEMS.append({
 "id": "l194-c1-mono-pagoto-ponokefalos", "title": "Γιατί πονάει το κεφάλι όταν τρώμε παγωτό;", "title_en": "Why does ice cream give us a headache?", "type": "monologue", "level": "C1",
 "context_el": "Απόσπασμα από εκπομπή εκλαΐκευσης της επιστήμης για τον λεγόμενο «πονοκέφαλο του παγωτού».",
 "script": [
  L("Παρουσιαστής", "m", "Όλοι το έχουμε ζήσει: μια γενναία κουταλιά παγωτό ή μια γρήγορη γουλιά από παγωμένο ρόφημα, και ξαφνικά ένας οξύς πόνος στο μέτωπο, σαν να μας τρύπησε κάτι, που χάνεται σε λίγα δευτερόλεπτα. Στη βιβλιογραφία έχει και επίσημο, αρκετά δύσκολο, όνομα, αλλά οι περισσότεροι τον λέμε απλώς «πονοκέφαλο του παγωτού».", "We've all experienced it: a generous spoonful of ice cream or a quick sip of an ice-cold drink, and suddenly a sharp pain in the forehead, as if something pierced us, which vanishes in a few seconds. In the literature it even has an official, rather difficult, name, but most of us simply call it 'ice-cream headache'."),
  L("Παρουσιαστής", "m", "Η επικρατέστερη εξήγηση είναι η εξής. Όταν κάτι πολύ κρύο ακουμπήσει τον ουρανίσκο, τα αιμοφόρα αγγεία της περιοχής συστέλλονται απότομα και αμέσως μετά διαστέλλονται, καθώς ο οργανισμός προσπαθεί να ζεστάνει ξανά τον χώρο. Αυτή η γρήγορη μεταβολή φαίνεται να ενεργοποιεί υποδοχείς πόνου που συνδέονται με το τρίδυμο νεύρο, ένα από τα κύρια νεύρα του προσώπου.", "The prevailing explanation is as follows. When something very cold touches the palate, the blood vessels in the area constrict abruptly and immediately afterwards dilate, as the body tries to warm the space up again. This rapid change seems to activate pain receptors connected to the trigeminal nerve, one of the main nerves of the face."),
  L("Παρουσιαστής", "m", "Και γιατί πονάει το μέτωπο και όχι το στόμα; Επειδή ο εγκέφαλος δεν είναι πάντα ακριβής στο να εντοπίζει από πού έρχεται ένα σήμα. Το τρίδυμο νεύρο εξυπηρετεί και το μέτωπο, κι έτσι ο πόνος «μεταφέρεται» εκεί. Οφείλω πάντως να πω ότι ο μηχανισμός δεν έχει διευκρινιστεί πλήρως και ότι οι μελέτες στο θέμα είναι σχετικά λίγες.", "And why does the forehead hurt and not the mouth? Because the brain isn't always precise in locating where a signal comes from. The trigeminal nerve also serves the forehead, and so the pain is 'referred' there. I must say, though, that the mechanism hasn't been fully clarified and that studies on the subject are relatively few."),
  L("Παρουσιαστής", "m", "Τι μπορούμε να κάνουμε; Το πιο απλό είναι να τρώμε πιο αργά, αφήνοντας το παγωτό να μαλακώσει λίγο στο μπροστινό μέρος του στόματος. Και αν ο πόνος έρθει, πιέστε τη γλώσσα σας στον ουρανίσκο για να τον ζεστάνετε. Δεν είναι θαύμα, αλλά συνήθως βοηθά, και σίγουρα είναι καλύτερο από το να παραιτηθείτε από το παγωτό.", "What can we do? The simplest thing is to eat more slowly, letting the ice cream soften a little at the front of the mouth. And if the pain comes, press your tongue against your palate to warm it up. It's not a miracle, but it usually helps, and it's certainly better than giving up ice cream."),
 ],
 "questions": [
  Q("Τι συμβαίνει στα αιμοφόρα αγγεία σύμφωνα με την επικρατέστερη εξήγηση;", ["Σπάνε από το κρύο", "Συστέλλονται απότομα και μετά διαστέλλονται", "Γεμίζουν με παγωμένο αίμα", "Μένουν σταθερά"], 1, "τα αιμοφόρα αγγεία της περιοχής συστέλλονται απότομα και αμέσως μετά διαστέλλονται"),
  Q("Γιατί ο πόνος γίνεται αισθητός στο μέτωπο;", ["Γιατί εκεί πηγαίνει το κρύο", "Γιατί το τρίδυμο νεύρο εξυπηρετεί και το μέτωπο", "Γιατί εκεί βρίσκεται ο ουρανίσκος", "Γιατί το μέτωπο είναι πιο ευαίσθητο"], 1, "Το τρίδυμο νεύρο εξυπηρετεί και το μέτωπο"),
  Q("Πώς παρουσιάζει ο ομιλητής τη γνώση μας για τον μηχανισμό;", ["Ως πλήρη και οριστική", "Ως όχι πλήρως διευκρινισμένη", "Ως εντελώς άγνωστη", "Ως μύθο"], 1, "ο μηχανισμός δεν έχει διευκρινιστεί πλήρως"),
 ],
 "gloss": {"ουρανίσκο": "ουρανίσκος — palate", "συστέλλονται": "συστέλλομαι — to constrict, contract", "διαστέλλονται": "διαστέλλομαι — to dilate, expand", "τρίδυμο": "τρίδυμο νεύρο — trigeminal nerve", "υποδοχείς": "υποδοχέας — receptor"},
})

rnd = random.Random(194)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-194.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
