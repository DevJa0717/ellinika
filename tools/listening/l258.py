# Source for library/listening/listening-258.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l258.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l258-news-olympiada-mathimatikon", "title": "Χρυσό μετάλλιο για μια μαθήτρια στη Διεθνή Ολυμπιάδα Μαθηματικών", "title_en": "A gold medal for a schoolgirl at the International Mathematical Olympiad", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο μεσημεριανό δελτίο ενός περιφερειακού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Με μεγάλη χαρά υποδέχτηκε χθες το βράδυ η Κομοτηνή τη δεκαεπτάχρονη Δανάη, που κέρδισε χρυσό μετάλλιο στη Διεθνή Ολυμπιάδα Μαθηματικών. Στον φετινό διαγωνισμό συμμετείχαν πάνω από εξακόσιοι μαθητές από περισσότερες από εκατό χώρες.", "Komotini gave a joyful welcome last night to seventeen-year-old Danai, who won a gold medal at the International Mathematical Olympiad. More than six hundred students from over a hundred countries took part in this year's competition."),
  L("Εκφωνητής", "m", "Οι διαγωνιζόμενοι έλυσαν έξι προβλήματα σε δύο μέρες, με τεσσερισήμισι ώρες στη διάθεσή τους κάθε μέρα. «Το τρίτο πρόβλημα με παίδεψε σχεδόν τρεις ώρες», είπε η Δανάη. «Τη λύση τη βρήκα δέκα λεπτά πριν τελειώσει ο χρόνος.»", "The contestants solved six problems over two days, with four and a half hours available each day. 'The third problem gave me trouble for almost three hours,' said Danai. 'I found the solution ten minutes before time ran out.'"),
  L("Εκφωνητής", "m", "Η μαθήτρια δεν πήγε ποτέ σε φροντιστήριο για τους διαγωνισμούς. Προετοιμαζόταν μόνη της με παλιά θέματα που έβρισκε στο ίντερνετ, και κάθε Σάββατο συναντιόταν με έναν συνταξιούχο καθηγητή μαθηματικών, που τη βοηθούσε αφιλοκερδώς.", "The student never went to a tutoring school for the competitions. She prepared on her own with past papers she found online, and every Saturday she met a retired maths teacher who helped her for free."),
  L("Εκφωνητής", "m", "Τον Σεπτέμβριο η Δανάη θα ξεκινήσει την τελευταία τάξη του λυκείου. Όταν τη ρώτησαν τι θέλει να σπουδάσει, απάντησε γελώντας: «Μαθηματικά, φυσικά. Αλλά πρώτα θέλω να κοιμηθώ μια εβδομάδα.»", "In September Danai will start her final year of upper secondary school. When asked what she wants to study, she laughed: 'Maths, of course. But first I want to sleep for a week.'"),
 ],
 "questions": [
  Q("Πόσοι μαθητές συμμετείχαν στον διαγωνισμό;", ["Περίπου εκατό", "Πάνω από εξακόσιοι", "Έξι", "Χίλιοι"], 1, "συμμετείχαν πάνω από εξακόσιοι μαθητές"),
  Q("Τι λέει η Δανάη για το τρίτο πρόβλημα;", ["Ότι το έλυσε σε δέκα λεπτά", "Ότι δεν το έλυσε", "Ότι τη δυσκόλεψε σχεδόν τρεις ώρες", "Ότι ήταν το πιο εύκολο"], 2, "Το τρίτο πρόβλημα με παίδεψε σχεδόν τρεις ώρες"),
  Q("Πώς προετοιμάστηκε για τους διαγωνισμούς;", ["Σε ένα ακριβό φροντιστήριο", "Με παλιά θέματα και με τη βοήθεια ενός συνταξιούχου καθηγητή", "Σε ένα θερινό σχολείο στο εξωτερικό", "Με τη μητέρα της, που είναι μαθηματικός"], 1, "Προετοιμαζόταν μόνη της με παλιά θέματα … συναντιόταν με έναν συνταξιούχο καθηγητή"),
  Q("Τι θέλει να κάνει πρώτα, όπως λέει;", ["Να ταξιδέψει", "Να κοιμηθεί μια εβδομάδα", "Να γράψει ένα βιβλίο", "Να διδάξει μαθηματικά"], 1, "πρώτα θέλω να κοιμηθώ μια εβδομάδα"),
 ],
 "gloss": {"υποδέχτηκε": "υποδέχομαι — to welcome", "μετάλλιο": "μετάλλιο — medal", "Ολυμπιάδα": "Ολυμπιάδα — Olympiad", "διαγωνιζόμενοι": "διαγωνιζόμενος — contestant", "παίδεψε": "παιδεύω — to give someone trouble, torment", "φροντιστήριο": "φροντιστήριο — tutoring school, cram school", "αφιλοκερδώς": "αφιλοκερδώς — for free, without profit", "λυκείου": "λύκειο — upper secondary school"}
})

ITEMS.append({
 "id": "l258-vm-leschi-anagnosis", "title": "Μήνυμα από τη λέσχη ανάγνωσης για την επόμενη συνάντηση", "title_en": "A message from the book club about the next meeting", "type": "voicemail", "level": "B2",
 "context_el": "Μόλις γραφτήκατε σε μια λέσχη ανάγνωσης. Ακούτε ένα μήνυμα που σας άφησε στον τηλεφωνητή η συντονίστρια.",
 "script": [
  L("Μυρτώ", "f", "Γεια σας, η Μυρτώ είμαι, από τη λέσχη ανάγνωσης της γειτονιάς. Χαίρομαι πολύ που θα έρθετε κι εσείς! Η επόμενη συνάντηση είναι την Πέμπτη στις επτά, όχι στο καφέ όπως συνήθως, αλλά στο σπίτι της Αλίκης, γιατί το καφέ κλείνει για ανακαίνιση.", "Hello, it's Myrto from the neighbourhood book club. I'm so glad you'll be coming too! The next meeting is on Thursday at seven, not at the café as usual but at Alíki's house, because the café is closing for renovation."),
  L("Μυρτώ", "f", "Το βιβλίο του μήνα είναι ένα μυθιστόρημα που διαδραματίζεται στη Σμύρνη στις αρχές του εικοστού αιώνα. Αν δεν προλάβετε να το τελειώσετε, μην ανησυχείτε· οι μισοί από εμάς δεν το τελειώνουμε ποτέ. Σας παρακαλώ μόνο να μη μας πείτε το τέλος, αν το έχετε διαβάσει ήδη.", "The book of the month is a novel set in Smyrna at the beginning of the twentieth century. If you don't manage to finish it, don't worry; half of us never finish. I'd only ask you not to tell us the ending if you've already read it."),
  L("Μυρτώ", "f", "Ο καθένας φέρνει κάτι μικρό να φάμε. Όσοι έρχονται για πρώτη φορά, όμως, δεν χρειάζεται να φέρουν τίποτα. Η Αλίκη έχει δύο γάτες, οπότε, αν έχετε αλλεργία, πείτε μου, να το κανονίσουμε αλλιώς.", "Everyone brings something small to eat. But people coming for the first time don't need to bring anything. Alíki has two cats, so if you have an allergy, tell me and we'll arrange things differently."),
  L("Μυρτώ", "f", "Στο τέλος της συνάντησης ψηφίζουμε το βιβλίο του επόμενου μήνα, οπότε, αν έχετε κάποια πρόταση, φέρτε τη. Θα σας στείλω τη διεύθυνση της Αλίκης με μήνυμα. Τα λέμε την Πέμπτη!", "At the end of the meeting we vote on next month's book, so if you have a suggestion, bring it. I'll text you Alíki's address. See you on Thursday!"),
 ],
 "questions": [
  Q("Γιατί η συνάντηση δεν θα γίνει στο καφέ;", ["Γιατί είναι ακριβό", "Γιατί κλείνει για ανακαίνιση", "Γιατί έχει πολύ θόρυβο", "Γιατί άλλαξε ιδιοκτήτη"], 1, "γιατί το καφέ κλείνει για ανακαίνιση"),
  Q("Τι ζητά η Μυρτώ από όσους έχουν ήδη διαβάσει το βιβλίο;", ["Να το δανείσουν στους άλλους", "Να μην πουν το τέλος", "Να ετοιμάσουν μια παρουσίαση", "Να διαβάσουν ένα απόσπασμα δυνατά"], 1, "να μη μας πείτε το τέλος"),
  Q("Τι πρέπει να φέρετε εσείς, που έρχεστε για πρώτη φορά;", ["Κάτι μικρό να φάμε", "Ένα ποτό", "Τίποτα", "Ένα βιβλίο για ανταλλαγή"], 2, "Όσοι έρχονται για πρώτη φορά … δεν χρειάζεται να φέρουν τίποτα"),
  Q("Γιατί να της πείτε αν έχετε αλλεργία;", ["Γιατί θα υπάρχουν λουλούδια", "Γιατί η Αλίκη έχει δύο γάτες", "Γιατί θα έχει γλυκά με ξηρούς καρπούς", "Γιατί το σπίτι έχει σκόνη"], 1, "Η Αλίκη έχει δύο γάτες"),
 ],
 "gloss": {"λέσχη": "λέσχη — club", "ανάγνωσης": "ανάγνωση — reading", "συντονίστρια": "συντονίστρια — coordinator (f.)", "ανακαίνιση": "ανακαίνιση — renovation", "μυθιστόρημα": "μυθιστόρημα — novel", "διαδραματίζεται": "διαδραματίζομαι — to take place, be set", "προλάβετε": "προλαβαίνω — to manage (in time)", "αλλεργία": "αλλεργία — allergy", "ψηφίζουμε": "ψηφίζω — to vote"}
})

ITEMS.append({
 "id": "l258-c1-mono-klepsydra-ammou", "title": "Λίγη άμμος για να μετρήσεις τον χρόνο: η ιστορία της κλεψύδρας της άμμου", "title_en": "A little sand to measure time: the history of the hourglass", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας ομιλίας σε έναν κύκλο εκδηλώσεων για την ιστορία της τεχνολογίας.",
 "script": [
  L("Ομιλητής", "m", "Η λέξη «κλεψύδρα» είναι αρχαία και σημαίνει κατά λέξη «αυτή που κλέβει το νερό»: οι πρώτες κλεψύδρες μετρούσαν τον χρόνο με νερό που έτρεχε από ένα δοχείο σε ένα άλλο. Η κλεψύδρα της άμμου, το γνωστό μας γυάλινο σχήμα με τη στενή μέση, είναι πολύ νεότερη.", "The word 'clepsydra' is ancient and literally means 'the one that steals water': the first clepsydras measured time with water flowing from one vessel to another. The sand-glass, the familiar glass shape with the narrow waist, is much more recent."),
  L("Ομιλητής", "m", "Η πρώτη σαφής απεικόνισή της στην Ευρώπη βρίσκεται σε μια τοιχογραφία της Σιένας του 1338, όπου η μορφή της Εγκράτειας κρατά στο χέρι μια κλεψύδρα άμμου. Πιθανότατα όμως χρησιμοποιούνταν ήδη νωρίτερα, κυρίως στα πλοία.", "Its first clear depiction in Europe is in a fresco in Siena from 1338, where the figure of Temperance holds a sand-glass in her hand. But it was very probably already in use earlier, mainly on ships."),
  L("Ομιλητής", "m", "Γιατί στα πλοία; Επειδή, σε αντίθεση με την κλεψύδρα του νερού, η άμμος δεν επηρεάζεται από το κούνημα των κυμάτων ούτε παγώνει με το κρύο. Οι ναυτικοί έριχναν στη θάλασσα ένα κομμάτι ξύλο δεμένο σε ένα σχοινί με κόμπους σε ίσες αποστάσεις, και μετρούσαν πόσοι κόμποι ξετυλίγονταν όσο έτρεχε μια μικρή κλεψύδρα. Από εκεί προέρχεται ο «κόμβος», η μονάδα ταχύτητας των πλοίων.", "Why on ships? Because, unlike the water clock, sand is not affected by the rocking of the waves, nor does it freeze in the cold. Sailors threw into the sea a piece of wood tied to a rope with knots at equal intervals, and counted how many knots unwound while a small sand-glass ran. That is where the 'knot', the unit of speed for ships, comes from."),
  L("Ομιλητής", "m", "Λέγεται ότι κάθε πλοίο του Μαγγελάνου κουβαλούσε δεκαοχτώ κλεψύδρες. Και η «άμμος» δεν ήταν πάντα άμμος: συχνά ήταν σκόνη από μάρμαρο ή από τσόφλια αυγών, που κυλούσε πιο ομαλά. Σήμερα, βέβαια, την κλεψύδρα τη συναντάμε κυρίως σε επιτραπέζια παιχνίδια και ως σύμβολο του χρόνου που περνά.", "It is said that each of Magellan's ships carried eighteen sand-glasses. And the 'sand' was not always sand: it was often powdered marble or eggshell, which flowed more smoothly. Today, of course, we meet the sand-glass mostly in board games and as a symbol of passing time."),
 ],
 "questions": [
  Q("Τι σημαίνει κατά λέξη η λέξη «κλεψύδρα»;", ["Αυτή που μετρά τις ώρες", "Αυτή που κλέβει το νερό", "Το ρολόι των ναυτικών", "Το γυάλινο δοχείο"], 1, "σημαίνει κατά λέξη «αυτή που κλέβει το νερό»"),
  Q("Πού βρίσκεται η πρώτη σαφής απεικόνιση της κλεψύδρας της άμμου στην Ευρώπη;", ["Σε ένα χειρόγραφο της Βενετίας", "Σε μια τοιχογραφία της Σιένας", "Σε έναν χάρτη του Μαγγελάνου", "Σε ένα αγγείο της Αθήνας"], 1, "σε μια τοιχογραφία της Σιένας του 1338"),
  Q("Γιατί η κλεψύδρα της άμμου ήταν χρήσιμη στα πλοία;", ["Γιατί ήταν φτηνή", "Γιατί δεν την επηρέαζε το κούνημα ούτε το κρύο", "Γιατί έδειχνε την κατεύθυνση", "Γιατί ήταν πολύ μεγάλη"], 1, "η άμμος δεν επηρεάζεται από το κούνημα των κυμάτων ούτε παγώνει με το κρύο"),
  Q("Από πού προέρχεται η μονάδα ταχύτητας «κόμβος»;", ["Από το όνομα ενός καπετάνιου", "Από τους κόμπους σε ένα σχοινί που ξετυλιγόταν στη θάλασσα", "Από τους κόμβους των δρόμων", "Από τα κύματα"], 1, "μετρούσαν πόσοι κόμποι ξετυλίγονταν όσο έτρεχε μια μικρή κλεψύδρα"),
 ],
 "gloss": {"κλεψύδρα": "κλεψύδρα — water clock; hourglass", "δοχείο": "δοχείο — vessel, container", "απεικόνισή": "απεικόνιση — depiction", "τοιχογραφία": "τοιχογραφία — fresco", "Εγκράτειας": "εγκράτεια — temperance, self-restraint", "κούνημα": "κούνημα — rocking", "κόμπους": "κόμπος — knot (in a rope)", "ξετυλίγονταν": "ξετυλίγομαι — to unwind", "κόμβος": "κόμβος — knot (unit of speed)", "τσόφλια": "τσόφλι — shell (of an egg)", "ομαλά": "ομαλά — smoothly"}
})

ITEMS.append({
 "id": "l258-c1-int-antidaneia", "title": "Λέξεις που έφυγαν και γύρισαν: μια γλωσσολόγος για τα αντιδάνεια", "title_en": "Words that left and came back: a linguist on 'return loans'", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια εκπομπή του ραδιοφώνου για τη γλώσσα.",
 "script": [
  L("Δημοσιογράφος", "f", "Μιλάμε συχνά για τις ξένες λέξεις που μπαίνουν στα ελληνικά. Εσείς μελετάτε μια ιδιαίτερη κατηγορία, τα αντιδάνεια. Τι είναι;", "We often talk about foreign words entering Greek. You study a special category, 'return loans'. What are they?"),
  L("Γλωσσολόγος", "f", "Είναι λέξεις ελληνικής προέλευσης που πέρασαν σε άλλες γλώσσες, άλλαξαν εκεί μορφή ή σημασία, και ύστερα γύρισαν πίσω στα ελληνικά. Πάρτε την «κάμερα». Η αρχαία «καμάρα» σήμαινε θολωτό χώρο. Πέρασε στα λατινικά ως camera, που σήμαινε δωμάτιο, και αιώνες αργότερα, μέσω της «σκοτεινής αίθουσας» των φωτογράφων, έγινε η συσκευή που ξέρουμε. Και έτσι επέστρεψε σε εμάς.", "They are words of Greek origin that passed into other languages, changed form or meaning there, and then came back into Greek. Take 'kamera'. Ancient 'kamara' meant a vaulted space. It passed into Latin as camera, meaning a room, and centuries later, through the photographers' 'dark chamber', it became the device we know. And so it came back to us."),
  L("Δημοσιογράφος", "f", "Υπάρχουν κι άλλα τόσο γνωστά παραδείγματα;", "Are there other equally well-known examples?"),
  L("Γλωσσολόγος", "f", "Πολλά. Το «ταλέντο» προέρχεται από το αρχαίο «τάλαντον», που ήταν μονάδα βάρους και νομίσματος. Χάρη σε μια παραβολή του Ευαγγελίου, όπου ένας δούλος θάβει το τάλαντο που του εμπιστεύτηκαν αντί να το αξιοποιήσει, η λέξη πήρε στις ευρωπαϊκές γλώσσες τη σημασία του χαρίσματος, και με αυτή τη σημασία ήρθε πίσω από τα ιταλικά. Και το «πιάτο» ανάγεται τελικά στο αρχαίο επίθετο «πλατύς».", "Many. 'Talento' comes from the ancient 'talanton', which was a unit of weight and currency. Thanks to a parable in the Gospel, where a servant buries the talent entrusted to him instead of putting it to use, the word took on the meaning of a gift in European languages, and with that meaning it came back from Italian. And 'piato', plate, ultimately goes back to the ancient adjective 'platys', broad."),
  L("Δημοσιογράφος", "f", "Και οι επιστημονικοί όροι, όπως το «τηλέφωνο»;", "And scientific terms, like 'telephone'?"),
  L("Γλωσσολόγος", "f", "Εκεί η περίπτωση είναι λίγο διαφορετική. Το «τηλέφωνο» δεν υπήρξε ποτέ στα αρχαία ελληνικά· το έπλασαν Ευρωπαίοι τον δέκατο ένατο αιώνα από ελληνικές ρίζες. Πολλοί γλωσσολόγοι, πάντως, το κατατάσσουν κι αυτό στα αντιδάνεια, γιατί οι λέξεις αυτές γεννήθηκαν έξω από τη χώρα. Το ενδιαφέρον είναι ότι ο μέσος ομιλητής δεν τις νιώθει καθόλου ξένες.", "There the case is a little different. 'Telephone' never existed in ancient Greek; Europeans coined it in the nineteenth century from Greek roots. Many linguists, though, classify these as return loans too, because the words were born outside the country. What's interesting is that the average speaker doesn't feel them to be foreign at all."),
 ],
 "questions": [
  Q("Τι είναι, σύμφωνα με τη γλωσσολόγο, τα αντιδάνεια;", ["Ξένες λέξεις που δεν μεταφράζονται", "Λέξεις ελληνικής προέλευσης που γύρισαν πίσω από άλλες γλώσσες", "Αρχαίες λέξεις που χάθηκαν", "Λέξεις με αντίθετη σημασία"], 1, "λέξεις ελληνικής προέλευσης που πέρασαν σε άλλες γλώσσες … και ύστερα γύρισαν πίσω στα ελληνικά"),
  Q("Τι σήμαινε η αρχαία λέξη «καμάρα»;", ["Συσκευή", "Θολωτό χώρο", "Φωτογραφία", "Σκοτάδι"], 1, "Η αρχαία «καμάρα» σήμαινε θολωτό χώρο"),
  Q("Πώς πήρε το «τάλαντο» τη σημασία του χαρίσματος;", ["Από ένα αρχαίο θεατρικό έργο", "Από μια παραβολή του Ευαγγελίου", "Από έναν Ιταλό ζωγράφο", "Από ένα νόμισμα της Αθήνας"], 1, "Χάρη σε μια παραβολή του Ευαγγελίου"),
  Q("Τι λέει για το «τηλέφωνο»;", ["Ότι το χρησιμοποιούσε ο Αριστοτέλης", "Ότι το έπλασαν Ευρωπαίοι από ελληνικές ρίζες", "Ότι είναι λατινική λέξη", "Ότι ο μέσος ομιλητής το νιώθει ξένο"], 1, "το έπλασαν Ευρωπαίοι τον δέκατο ένατο αιώνα από ελληνικές ρίζες"),
 ],
 "gloss": {"αντιδάνεια": "αντιδάνειο — return loan (a word that comes back to its original language)", "προέλευσης": "προέλευση — origin", "θολωτό": "θολωτός — vaulted", "παραβολή": "παραβολή — parable", "αξιοποιήσει": "αξιοποιώ — to put to good use", "χαρίσματος": "χάρισμα — gift, talent", "ανάγεται": "ανάγομαι — to go back to, derive from", "έπλασαν": "πλάθω — to coin, shape", "κατατάσσουν": "κατατάσσω — to classify"}
})
rnd = random.Random(258)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-258.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
