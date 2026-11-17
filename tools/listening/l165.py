# Source for library/listening/listening-165.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l165.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l165-ann-ora-tis-gis", "title": "Ανακοίνωση για την Ώρα της Γης", "title_en": "An announcement about Earth Hour", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στον τοπικό ραδιοφωνικό σταθμό λίγες μέρες πριν από την Ώρα της Γης.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος μας συμμετέχει και φέτος στην Ώρα της Γης, την παγκόσμια εκστρατεία για το κλίμα, που ξεκίνησε στο Σίδνεϊ το 2007. Το Σάββατο, από τις οχτώμισι ως τις εννιάμισι το βράδυ, θα σβήσουν τα φώτα του δημαρχείου, του κάστρου και της γέφυρας του λιμανιού.", "Our municipality is taking part in Earth Hour again this year, the worldwide climate campaign that began in Sydney in 2007. On Saturday, from half past eight to half past nine in the evening, the lights of the town hall, the castle and the harbour bridge will be switched off."),
  L("Εκφωνήτρια", "f", "Καλούμε όλους τους κατοίκους να σβήσουν κι εκείνοι για μία ώρα τα φώτα και τις συσκευές που δεν χρειάζονται. Για λόγους ασφαλείας, τα φώτα των δρόμων και των φαναριών θα μείνουν κανονικά αναμμένα, όπως και ο φωτισμός στα νοσοκομεία.", "We invite all residents to switch off for one hour the lights and appliances they don't need as well. For safety reasons, street lights and traffic lights will stay on as normal, as will the lighting in hospitals."),
  L("Εκφωνήτρια", "f", "Στην κεντρική πλατεία θα γίνει μια ακουστική συναυλία με κεριά, από τη σχολική ορχήστρα, και εθελοντές θα μοιράζουν φακούς που λειτουργούν με το χέρι, χωρίς μπαταρίες. Φέρτε μαζί σας ένα μαξιλάρι για να καθίσετε στα σκαλιά του δημαρχείου.", "In the central square there will be an acoustic candlelit concert by the school orchestra, and volunteers will hand out wind-up torches that work without batteries. Bring a cushion with you to sit on the steps of the town hall."),
 ],
 "questions": [
  Q("Πόσο διαρκεί η Ώρα της Γης;", ["Μισή ώρα", "Μία ώρα", "Δύο ώρες", "Όλη τη νύχτα"], 1, "από τις οχτώμισι ως τις εννιάμισι το βράδυ"),
  Q("Ποια φώτα θα μείνουν αναμμένα;", ["Τα φώτα του δημαρχείου", "Τα φώτα του κάστρου", "Τα φώτα των δρόμων και των φαναριών", "Τα φώτα της γέφυρας"], 2, "τα φώτα των δρόμων και των φαναριών θα μείνουν κανονικά αναμμένα"),
  Q("Τι θα μοιράζουν οι εθελοντές;", ["Κεριά", "Φακούς που λειτουργούν με το χέρι", "Μαξιλάρια", "Φυλλάδια για το κλίμα"], 1, "εθελοντές θα μοιράζουν φακούς που λειτουργούν με το χέρι"),
 ],
 "gloss": {"εκστρατεία": "εκστρατεία — campaign", "κλίμα": "κλίμα — climate", "Σίδνεϊ": "Σίδνεϊ — Sydney", "σβήσουν": "σβήνω — to switch off", "δημαρχείου": "δημαρχείο — town hall", "συσκευές": "συσκευή — appliance", "φαναριών": "φανάρι — traffic light", "αναμμένα": "αναμμένος — switched on, lit", "ακουστική": "ακουστικός — acoustic", "κεριά": "κερί — candle", "φακούς": "φακός — torch", "μαξιλάρι": "μαξιλάρι — cushion"},
})

ITEMS.append({
 "id": "l165-int-mimos", "title": "Ο μίμος που δεν λέει λέξη", "title_en": "A mime artist on the city streets", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν μίμο που κάνει παραστάσεις παντομίμας σε πλατείες και σε σχολεία.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς γίνεται κανείς μίμος;", "How does one become a mime artist?"),
  L("Μίμος", "m", "Εγώ σπούδασα θέατρο, αλλά στη σχολή ήμουν ο ηθοποιός που ξεχνούσε πάντα τα λόγια του. Μια καθηγήτρια μού είπε, μισοαστεία μισοσοβαρά, ότι το σώμα μου θυμάται καλύτερα από το μυαλό μου. Πήγα σε ένα σεμινάριο παντομίμας και από τότε δεν έχω πει ούτε λέξη πάνω στη σκηνή.", "I studied theatre, but at drama school I was the actor who always forgot his lines. One teacher told me, half joking, half serious, that my body remembers better than my mind. I went to a mime workshop and since then I haven't said a single word on stage."),
  L("Δημοσιογράφος", "f", "Ποιο είναι το πιο δύσκολο στην παντομίμα;", "What is the hardest thing in mime?"),
  L("Μίμος", "m", "Να κάνεις τον θεατή να δει κάτι που δεν υπάρχει. Αν ακουμπήσω έναν αόρατο τοίχο, πρέπει το χέρι μου να σταματά ακριβώς στο ίδιο σημείο κάθε φορά. Αν μετακινηθεί έστω και ένα εκατοστό, ο τοίχος χάνεται. Γι' αυτό κάνω ασκήσεις μπροστά στον καθρέφτη δύο ώρες κάθε μέρα, όπως ένας μουσικός κάνει κλίμακες.", "Making the spectator see something that doesn't exist. If I touch an invisible wall, my hand has to stop at exactly the same point every time. If it moves even a centimetre, the wall disappears. That's why I do exercises in front of the mirror two hours every day, like a musician practising scales."),
  L("Δημοσιογράφος", "f", "Ποιο είναι το καλύτερο κοινό σας;", "Who is your best audience?"),
  L("Μίμος", "m", "Τα παιδιά, χωρίς αμφιβολία. Οι μεγάλοι ψάχνουν το νόημα, ενώ τα παιδιά απλώς μπαίνουν στο παιχνίδι. Μια φορά ένα κορίτσι ήρθε μετά την παράσταση και μου έδωσε κάτι «αόρατο» στο χέρι. Μου είπε ότι ήταν ένα κλειδί για να βγω από το κουτί μου. Το κρατάω ακόμα.", "Children, without a doubt. Adults look for the meaning, while children just join in the game. Once a girl came after the show and gave me something 'invisible' in my hand. She told me it was a key to get out of my box. I still keep it."),
 ],
 "questions": [
  Q("Τι του είπε μια καθηγήτρια στη δραματική σχολή;", ["Ότι πρέπει να αλλάξει επάγγελμα", "Ότι το σώμα του θυμάται καλύτερα από το μυαλό του", "Ότι έχει ωραία φωνή", "Ότι πρέπει να γράφει θεατρικά έργα"], 1, "το σώμα μου θυμάται καλύτερα από το μυαλό μου"),
  Q("Γιατί κάνει ασκήσεις μπροστά στον καθρέφτη κάθε μέρα;", ["Για να γυμνάζεται", "Για να μαθαίνει νέα κείμενα", "Γιατί οι κινήσεις του πρέπει να είναι ακριβείς, αλλιώς ο αόρατος τοίχος χάνεται", "Για να βελτιώσει το μακιγιάζ του"], 2, "Αν μετακινηθεί έστω και ένα εκατοστό, ο τοίχος χάνεται"),
  Q("Γιατί θεωρεί τα παιδιά το καλύτερο κοινό;", ["Γιατί μπαίνουν απλώς στο παιχνίδι, ενώ οι μεγάλοι ψάχνουν το νόημα", "Γιατί γελάνε δυνατά", "Γιατί πληρώνουν λιγότερο", "Γιατί κάθονται ήσυχα"], 0, "Οι μεγάλοι ψάχνουν το νόημα, ενώ τα παιδιά απλώς μπαίνουν στο παιχνίδι"),
 ],
 "gloss": {"μίμος": "μίμος — mime artist", "μίμο": "μίμος — mime artist", "παντομίμας": "παντομίμα — mime", "παραστάσεις": "παράσταση — performance, show", "σχολή": "σχολή — (drama) school", "λόγια": "λόγια — lines (of a role)", "μισοαστεία μισοσοβαρά": "μισοαστεία μισοσοβαρά — half joking, half serious", "σεμινάριο": "σεμινάριο — workshop", "θεατή": "θεατής — spectator", "αόρατο": "αόρατος — invisible", "ακουμπήσω": "ακουμπάω — to touch", "εκατοστό": "εκατοστό — centimetre", "κλίμακες": "κλίμακα — scale (music)", "αμφιβολία": "αμφιβολία — doubt", "νόημα": "νόημα — meaning"},
})

ITEMS.append({
 "id": "l165-int-sxoleio-fylakis", "title": "Ένα σχολείο μέσα στη φυλακή", "title_en": "A school inside the prison", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν εκπαιδευτικό που διδάσκει σε ένα σχολείο δεύτερης ευκαιρίας μέσα σε φυλακή.",
 "script": [
  L("Δημοσιογράφος", "f", "Ποιοι είναι οι μαθητές σας;", "Who are your students?"),
  L("Εκπαιδευτικός", "m", "Είναι άντρες από είκοσι ως εξήντα χρονών που, για διάφορους λόγους, δεν τελείωσαν το σχολείο. Κάποιοι μόλις που ήξεραν να γράψουν το όνομά τους. Το σχολείο διαρκεί δύο χρόνια και στο τέλος παίρνουν απολυτήριο γυμνασίου, όπως σε κάθε άλλο σχολείο.", "They're men from twenty to sixty who, for various reasons, didn't finish school. Some could barely write their own name. The school lasts two years, and at the end they get a lower secondary school certificate, as in any other school."),
  L("Δημοσιογράφος", "f", "Γιατί έρχονται στο σχολείο;", "Why do they come to school?"),
  L("Εκπαιδευτικός", "m", "Στην αρχή πολλοί έρχονται επειδή κάθε μέρα σχολείου μετράει ως μέρα έκτισης της ποινής τους. Δεν το κρύβουν. Μετά από λίγους μήνες όμως κάτι αλλάζει. Ένας μαθητής μού είπε ότι στην τάξη είναι η μόνη ώρα της μέρας που νιώθει άνθρωπος και όχι αριθμός.", "At first many come because every school day counts as a day served of their sentence. They don't hide it. After a few months, though, something changes. One student told me that the classroom is the only time of the day he feels like a person and not a number."),
  L("Δημοσιογράφος", "f", "Τι σας έχει μείνει περισσότερο;", "What has stayed with you most?"),
  L("Εκπαιδευτικός", "m", "Ένας μαθητής πενήντα πέντε χρονών έγραψε το πρώτο γράμμα της ζωής του στην εγγονή του. Μου ζήτησε να το διορθώσω, κι εγώ αρνήθηκα. Του είπα ότι ένα παιδί δεν διαβάζει τα ορθογραφικά λάθη, διαβάζει τον παππού του.", "A fifty-five-year-old student wrote the first letter of his life to his granddaughter. He asked me to correct it, and I refused. I told him that a child doesn't read the spelling mistakes, she reads her grandfather."),
 ],
 "questions": [
  Q("Τι παίρνουν οι μαθητές στο τέλος των δύο χρόνων;", ["Ένα πτυχίο πανεπιστημίου", "Απολυτήριο γυμνασίου", "Άδεια οδήγησης", "Μια βεβαίωση παρακολούθησης χωρίς αξία"], 1, "στο τέλος παίρνουν απολυτήριο γυμνασίου"),
  Q("Γιατί έρχονται πολλοί στο σχολείο στην αρχή;", ["Γιατί κάθε μέρα σχολείου μετράει ως μέρα έκτισης της ποινής τους", "Γιατί είναι υποχρεωτικό", "Γιατί παίρνουν χρήματα", "Γιατί τους το ζητά η οικογένειά τους"], 0, "κάθε μέρα σχολείου μετράει ως μέρα έκτισης της ποινής τους"),
  Q("Γιατί ο εκπαιδευτικός αρνήθηκε να διορθώσει το γράμμα;", ["Γιατί δεν είχε χρόνο", "Γιατί δεν επιτρέπεται", "Γιατί ένα παιδί δεν διαβάζει τα ορθογραφικά λάθη αλλά τον παππού του", "Γιατί το γράμμα δεν είχε λάθη"], 2, "ένα παιδί δεν διαβάζει τα ορθογραφικά λάθη, διαβάζει τον παππού του"),
 ],
 "gloss": {"φυλακή": "φυλακή — prison", "εκπαιδευτικό": "εκπαιδευτικός — teacher, educator", "δεύτερης ευκαιρίας": "σχολείο δεύτερης ευκαιρίας — second-chance school", "μόλις που": "μόλις που — barely", "απολυτήριο": "απολυτήριο — school-leaving certificate", "γυμνασίου": "γυμνάσιο — lower secondary school", "έκτισης": "έκτιση — serving (a sentence)", "ποινής": "ποινή — sentence, penalty", "αριθμός": "αριθμός — number", "εγγονή": "εγγονή — granddaughter", "αρνήθηκα": "αρνούμαι — to refuse", "ορθογραφικά": "ορθογραφικός — spelling (adj.)"},
})

ITEMS.append({
 "id": "l165-dia-tablet", "title": "Τάμπλετ ή βιβλίο για τον παππού;", "title_en": "A tablet or a book for grandad?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέλφια να συζητούν τι δώρο θα πάρουν στον παππού τους για τα ογδοηκοστά του γενέθλια.",
 "script": [
  L("Ηλίας", "m", "Σκέφτηκα να του πάρουμε ένα τάμπλετ. Θα μπορεί να μας βλέπει σε βιντεοκλήση, να διαβάζει εφημερίδες με μεγάλα γράμματα και να ακούει τα παλιά του τραγούδια.", "I thought we could get him a tablet. He'll be able to see us on video calls, read newspapers in big letters and listen to his old songs."),
  L("Αθηνά", "f", "Ιδέα καλή, αλλά θυμάσαι τι έγινε με το κινητό που του πήρε η μαμά; Το έχει ακόμα στο κουτί του. Λέει ότι τα κουμπιά είναι πολύ μικρά και ότι δεν θέλει να το χαλάσει.", "Good idea, but do you remember what happened with the mobile phone Mum got him? He still has it in its box. He says the buttons are too small and that he doesn't want to break it."),
  L("Ηλίας", "m", "Γι' αυτό ακριβώς. Το τάμπλετ έχει μεγάλη οθόνη. Και αν το ρυθμίσουμε από πριν, με τρία εικονίδια μόνο, δεν θα χρειάζεται να κάνει τίποτα άλλο από το να πατάει τη φωτογραφία μας.", "That's exactly why. The tablet has a big screen. And if we set it up beforehand, with only three icons, he won't need to do anything other than press our photo."),
  L("Αθηνά", "f", "Εγώ σκεφτόμουν ένα βιβλίο με τις παλιές φωτογραφίες του χωριού. Ο θείος Κώστας έχει σκανάρει πάνω από διακόσιες. Ο παππούς θα καθόταν με τις ώρες να μας λέει ιστορίες για τον καθένα.", "I was thinking of a book with the old photos of the village. Uncle Kostas has scanned over two hundred. Grandad would sit for hours telling us stories about each person."),
  L("Ηλίας", "m", "Ξέρεις κάτι; Ας κάνουμε και τα δύο. Το βιβλίο για τα γενέθλια, και το τάμπλετ τα Χριστούγεννα, μαζί με μαθήματα από εμάς κάθε Κυριακή.", "You know what? Let's do both. The book for his birthday, and the tablet at Christmas, along with lessons from us every Sunday."),
  L("Αθηνά", "f", "Συμφωνώ. Και βάλε τις φωτογραφίες του βιβλίου και στο τάμπλετ. Έτσι θα έχει λόγο να το ανοίγει.", "Agreed. And put the photos from the book on the tablet too. That way he'll have a reason to open it."),
 ],
 "questions": [
  Q("Τι έγινε με το κινητό που του πήρε η μαμά;", ["Το έχασε", "Το χάλασε", "Το έχει ακόμα στο κουτί του", "Το χάρισε σε έναν γείτονα"], 2, "Το έχει ακόμα στο κουτί του"),
  Q("Τι προτείνει η Αθηνά ως δώρο;", ["Ένα ρολόι", "Ένα βιβλίο με τις παλιές φωτογραφίες του χωριού", "Ένα ραδιόφωνο", "Ένα ταξίδι στο χωριό"], 1, "ένα βιβλίο με τις παλιές φωτογραφίες του χωριού"),
  Q("Τι αποφασίζουν στο τέλος;", ["Να του πάρουν μόνο το τάμπλετ", "Το βιβλίο για τα γενέθλια και το τάμπλετ τα Χριστούγεννα", "Να ρωτήσουν τη μαμά τους", "Να του πάρουν ένα καινούργιο κινητό"], 1, "Το βιβλίο για τα γενέθλια, και το τάμπλετ τα Χριστούγεννα"),
 ],
 "gloss": {"τάμπλετ": "τάμπλετ — tablet", "ογδοηκοστά": "ογδοηκοστός — eightieth", "βιντεοκλήση": "βιντεοκλήση — video call", "κουμπιά": "κουμπί — button", "χαλάσει": "χαλάω — to break, to spoil", "οθόνη": "οθόνη — screen", "ρυθμίσουμε": "ρυθμίζω — to set up", "εικονίδια": "εικονίδιο — icon", "σκανάρει": "σκανάρω — to scan", "με τις ώρες": "με τις ώρες — for hours"},
})

ITEMS.append({
 "id": "l165-dia-skini", "title": "Σκηνή ή δωμάτιο;", "title_en": "Tent or room?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητά πού θα μείνει στις καλοκαιρινές διακοπές σε ένα νησί.",
 "script": [
  L("Πάνος", "m", "Βρήκα ένα κάμπινγκ πάνω στην παραλία, με σκιά από αλμυρίκια. Δεκαπέντε ευρώ τη βραδιά για τους δυο μας και τη σκηνή. Σκέψου να ξυπνάμε και να βουτάμε κατευθείαν στη θάλασσα.", "I found a campsite right on the beach, with shade from tamarisks. Fifteen euros a night for the two of us and the tent. Imagine waking up and diving straight into the sea."),
  L("Δέσποινα", "f", "Ακούγεται ρομαντικό, αλλά θυμάσαι την τελευταία φορά; Δεν κοιμήθηκα ούτε μία νύχτα από τα κουνούπια και τη ζέστη, και το πρωί η σκηνή γινόταν φούρνος από τις επτά.", "It sounds romantic, but do you remember last time? I didn't sleep a single night because of the mosquitoes and the heat, and in the morning the tent turned into an oven by seven."),
  L("Πάνος", "m", "Εκείνο ήταν ένα κάμπινγκ χωρίς ούτε ένα δέντρο. Και τα δωμάτια στο νησί τον Αύγουστο κοστίζουν πάνω από εκατό ευρώ. Με τη διαφορά, μπορούμε να τρώμε κάθε βράδυ σε ταβέρνα.", "That was a campsite without a single tree. And rooms on the island in August cost over a hundred euros. With the difference, we can eat at a taverna every evening."),
  L("Δέσποινα", "f", "Να κάνουμε έναν συμβιβασμό; Πέντε βράδια στο κάμπινγκ και τα δύο τελευταία σε δωμάτιο, για να κάνουμε ένα κανονικό μπάνιο και να κοιμηθούμε πριν από το ταξίδι της επιστροφής.", "Shall we compromise? Five nights at the campsite and the last two in a room, so we can have a proper shower and sleep before the journey back."),
  L("Πάνος", "m", "Δεκτό. Και θα αγοράσω μια σίτα για τα κουνούπια, να μην έχεις δικαιολογία.", "Accepted. And I'll buy a mosquito net, so you have no excuse."),
 ],
 "questions": [
  Q("Τι θυμάται η Δέσποινα από την τελευταία φορά στο κάμπινγκ;", ["Ότι έβρεξε όλη την εβδομάδα", "Ότι δεν κοιμήθηκε από τα κουνούπια και τη ζέστη", "Ότι τους έκλεψαν τη σκηνή", "Ότι είχε πολύ θόρυβο"], 1, "Δεν κοιμήθηκα ούτε μία νύχτα από τα κουνούπια και τη ζέστη"),
  Q("Τι λέει ο Πάνος για τη διαφορά στην τιμή;", ["Ότι θα αγοράσουν καινούργια σκηνή", "Ότι μπορούν να τρώνε κάθε βράδυ σε ταβέρνα", "Ότι θα μείνουν περισσότερες μέρες", "Ότι θα νοικιάσουν αυτοκίνητο"], 1, "μπορούμε να τρώμε κάθε βράδυ σε ταβέρνα"),
  Q("Ποιος είναι ο συμβιβασμός;", ["Όλες τις νύχτες σε δωμάτιο", "Όλες τις νύχτες στο κάμπινγκ", "Πέντε βράδια στο κάμπινγκ και δύο σε δωμάτιο", "Να πάνε σε άλλο νησί"], 2, "Πέντε βράδια στο κάμπινγκ και τα δύο τελευταία σε δωμάτιο"),
 ],
 "gloss": {"σκηνή": "σκηνή — tent", "ζευγάρι": "ζευγάρι — couple", "κάμπινγκ": "κάμπινγκ — campsite", "αλμυρίκια": "αλμυρίκι — tamarisk", "κουνούπια": "κουνούπι — mosquito", "φούρνος": "φούρνος — oven", "συμβιβασμό": "συμβιβασμός — compromise", "Δεκτό": "δεκτός — accepted", "σίτα": "σίτα — (mosquito) net, screen", "δικαιολογία": "δικαιολογία — excuse"},
})

ITEMS.append({
 "id": "l165-mon-allilografia", "title": "Τριάντα χρόνια αλληλογραφίας", "title_en": "Thirty years of letters", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλάει σε ένα ραδιοφωνικό πρόγραμμα για μια φιλία που ξεκίνησε με ένα γράμμα.",
 "script": [
  L("Γυναίκα", "f", "Ήμουν δώδεκα χρονών όταν η καθηγήτρια των αγγλικών μάς μοίρασε διευθύνσεις παιδιών από άλλες χώρες, για να τους γράψουμε. Εμένα μου έτυχε ένα κορίτσι από την Ιαπωνία, η Γιούκο. Της έγραψα τρεις σελίδες με λάθη, και ύστερα από έναν μήνα ήρθε η απάντηση, σε ένα γαλάζιο φάκελο με ένα αποξηραμένο λουλούδι μέσα.", "I was twelve when our English teacher handed out addresses of children from other countries, so we could write to them. I got a girl from Japan, Yuko. I wrote her three pages full of mistakes, and after a month the reply came, in a light blue envelope with a dried flower inside."),
  L("Γυναίκα", "f", "Από τότε δεν σταματήσαμε. Μεγαλώσαμε μέσα από τα γράμματα: τα πρώτα ερωτικά απογοητεύματα, οι σπουδές, οι γάμοι, τα παιδιά. Όταν ήρθε το ηλεκτρονικό ταχυδρομείο, συμφωνήσαμε να συνεχίσουμε με χαρτί και στυλό, γιατί ένα γράμμα το περιμένεις, και αυτή η αναμονή είναι μέρος της χαράς.", "Since then we haven't stopped. We grew up through the letters: the first romantic disappointments, our studies, our weddings, our children. When email came, we agreed to carry on with paper and pen, because you wait for a letter, and that waiting is part of the joy."),
  L("Γυναίκα", "f", "Πέρσι, μετά από τριάντα χρόνια, γνωριστήκαμε επιτέλους από κοντά, στο Κιότο. Φοβόμουν ότι θα είμαστε δύο ξένες που δεν ξέρουν τι να πουν. Μόλις όμως με είδε στο σταθμό, έβγαλε από την τσάντα της το πρώτο μου γράμμα, με όλα τα λάθη του. Γελάσαμε τόσο πολύ που ο κόσμος γύριζε να μας κοιτάξει.", "Last year, after thirty years, we finally met in person, in Kyoto. I was afraid we'd be two strangers who didn't know what to say. But as soon as she saw me at the station, she took out of her bag my first letter, with all its mistakes. We laughed so much that people turned to look at us."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η αλληλογραφία;", ["Η καθηγήτρια των αγγλικών μοίρασε διευθύνσεις παιδιών από άλλες χώρες", "Γνωρίστηκαν σε ένα ταξίδι", "Μέσα από μια εφημερίδα", "Μέσω μιας φίλης της μητέρας της"], 0, "η καθηγήτρια των αγγλικών μάς μοίρασε διευθύνσεις παιδιών από άλλες χώρες"),
  Q("Γιατί συνέχισαν με χαρτί και στυλό όταν ήρθε το ηλεκτρονικό ταχυδρομείο;", ["Γιατί δεν είχαν υπολογιστή", "Γιατί η αναμονή για ένα γράμμα είναι μέρος της χαράς", "Γιατί ήταν φθηνότερο", "Γιατί το ζήτησαν τα παιδιά τους"], 1, "ένα γράμμα το περιμένεις, και αυτή η αναμονή είναι μέρος της χαράς"),
  Q("Τι έκανε η Γιούκο μόλις την είδε στον σταθμό;", ["Της έδωσε ένα λουλούδι", "Έβαλε τα κλάματα", "Έβγαλε από την τσάντα της το πρώτο της γράμμα", "Της μίλησε ελληνικά"], 2, "έβγαλε από την τσάντα της το πρώτο μου γράμμα"),
 ],
 "gloss": {"μοίρασε": "μοιράζω — to hand out", "διευθύνσεις": "διεύθυνση — address", "μου έτυχε": "μου τυχαίνει — I happen to get", "φάκελο": "φάκελος — envelope", "αποξηραμένο": "αποξηραμένος — dried", "απογοητεύματα": "απογοήτευμα — disappointment", "ηλεκτρονικό ταχυδρομείο": "ηλεκτρονικό ταχυδρομείο — email", "αναμονή": "αναμονή — waiting", "επιτέλους": "επιτέλους — at last", "από κοντά": "από κοντά — in person", "ξένες": "ξένος — stranger"},
})

ITEMS.append({
 "id": "l165-vm-psygeio", "title": "Μήνυμα από τον τεχνικό για το ψυγείο", "title_en": "A message from the technician about the fridge", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον τεχνικό που ήρθε το πρωί να δει το ψυγείο σας.",
 "script": [
  L("Τεχνικός", "m", "Καλησπέρα, ο Βαγγέλης είμαι, ο τεχνικός. Έλεγξα το ψυγείο σας στο εργαστήριο. Το πρόβλημα είναι στον θερμοστάτη, όχι στο μοτέρ, οπότε τα νέα είναι καλά. Αν ήταν το μοτέρ, θα σας έλεγα να αγοράσετε καινούργιο.", "Good evening, it's Vangelis, the technician. I checked your fridge at the workshop. The problem is the thermostat, not the motor, so the news is good. If it were the motor, I'd tell you to buy a new one."),
  L("Τεχνικός", "m", "Η επισκευή θα κοστίσει γύρω στα ογδόντα ευρώ, μαζί με το ανταλλακτικό. Το ανταλλακτικό όμως δεν το έχω, και θα το φέρω από την αντιπροσωπεία την Πέμπτη. Μέχρι τότε, μην βάζετε στην κατάψυξη φαγητά που χαλάνε εύκολα, γιατί η θερμοκρασία ανεβοκατεβαίνει.", "The repair will cost around eighty euros, including the part. But I don't have the part, and I'll bring it from the dealer on Thursday. Until then, don't put food that spoils easily in the freezer, because the temperature goes up and down."),
  L("Τεχνικός", "m", "Αν θέλετε, μπορώ να έρθω την Πέμπτη το απόγευμα, μετά τις πέντε, για να μη χάσετε μέρα από τη δουλειά. Η επισκευή θα έχει εγγύηση έξι μηνών. Πάρτε με όταν μπορέσετε να το κανονίσουμε.", "If you like, I can come on Thursday afternoon, after five, so you don't lose a day off work. The repair will have a six-month guarantee. Call me when you can so we can arrange it."),
 ],
 "questions": [
  Q("Πού είναι το πρόβλημα του ψυγείου;", ["Στο μοτέρ", "Στον θερμοστάτη", "Στην πόρτα", "Στο καλώδιο"], 1, "Το πρόβλημα είναι στον θερμοστάτη, όχι στο μοτέρ"),
  Q("Τι σας συμβουλεύει να μην κάνετε μέχρι την Πέμπτη;", ["Να μην ανοίγετε το ψυγείο", "Να μη βάζετε στην κατάψυξη φαγητά που χαλάνε εύκολα", "Να μην το βγάζετε από την πρίζα", "Να μην αγοράσετε καινούργιο"], 1, "μην βάζετε στην κατάψυξη φαγητά που χαλάνε εύκολα"),
  Q("Γιατί προτείνει να έρθει μετά τις πέντε;", ["Γιατί το πρωί δουλεύει αλλού", "Για να μη χάσετε μέρα από τη δουλειά", "Γιατί τότε θα έχει το ανταλλακτικό", "Γιατί είναι φθηνότερο"], 1, "για να μη χάσετε μέρα από τη δουλειά"),
 ],
 "gloss": {"τεχνικό": "τεχνικός — technician", "εργαστήριο": "εργαστήριο — workshop", "θερμοστάτη": "θερμοστάτης — thermostat", "μοτέρ": "μοτέρ — motor", "επισκευή": "επισκευή — repair", "ανταλλακτικό": "ανταλλακτικό — spare part", "αντιπροσωπεία": "αντιπροσωπεία — dealer, dealership", "κατάψυξη": "κατάψυξη — freezer", "ανεβοκατεβαίνει": "ανεβοκατεβαίνω — to go up and down", "εγγύηση": "εγγύηση — guarantee"},
})

ITEMS.append({
 "id": "l165-vm-ydrometro", "title": "Μήνυμα για την αλλαγή του υδρομέτρου", "title_en": "A message about replacing the water meter", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από την εταιρεία ύδρευσης της πόλης σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, σας καλούμε από την εταιρεία ύδρευσης. Στο πλαίσιο της αντικατάστασης των παλιών υδρομέτρων, ένα συνεργείο μας θα περάσει από την πολυκατοικία σας την ερχόμενη Τρίτη, μεταξύ εννιά και μίας.", "Good morning, we're calling from the water company. As part of the replacement of old water meters, one of our crews will come by your block of flats next Tuesday, between nine and one."),
  L("Υπάλληλος", "m", "Τα καινούργια υδρόμετρα είναι ψηφιακά και στέλνουν την ένδειξη αυτόματα, οπότε δεν θα χρειάζεται πια να περνάει υπάλληλος για να τα διαβάζει. Η αντικατάσταση είναι δωρεάν και διαρκεί περίπου είκοσι λεπτά για κάθε διαμέρισμα. Όσο διαρκεί, το νερό θα είναι κομμένο.", "The new water meters are digital and send the reading automatically, so an employee will no longer need to come by to read them. The replacement is free and takes about twenty minutes for each flat. While it lasts, the water will be cut off."),
  L("Υπάλληλος", "m", "Επειδή το υδρόμετρό σας βρίσκεται μέσα στο διαμέρισμα, πρέπει να είναι κάποιος στο σπίτι για να ανοίξει. Αν η Τρίτη δεν σας βολεύει, καλέστε μας στο τηλέφωνο της εξυπηρέτησης πελατών για να κλείσετε άλλη μέρα. Σας ευχαριστούμε.", "Because your water meter is inside the flat, someone must be at home to open the door. If Tuesday doesn't suit you, call our customer service number to book another day. Thank you."),
 ],
 "questions": [
  Q("Ποιο είναι το πλεονέκτημα των καινούργιων υδρομέτρων;", ["Είναι φθηνότερα", "Στέλνουν την ένδειξη αυτόματα", "Μειώνουν την κατανάλωση", "Δεν χαλάνε ποτέ"], 1, "στέλνουν την ένδειξη αυτόματα"),
  Q("Τι θα συμβεί όσο διαρκεί η αντικατάσταση;", ["Θα κοπεί το ρεύμα", "Το νερό θα είναι κομμένο", "Θα κλείσει η είσοδος της πολυκατοικίας", "Δεν θα λειτουργεί το ασανσέρ"], 1, "Όσο διαρκεί, το νερό θα είναι κομμένο"),
  Q("Γιατί πρέπει να είναι κάποιος στο σπίτι;", ["Γιατί πρέπει να υπογράψει", "Γιατί πρέπει να πληρώσει", "Γιατί το υδρόμετρο βρίσκεται μέσα στο διαμέρισμα", "Γιατί θα γίνει έλεγχος για διαρροές"], 2, "Επειδή το υδρόμετρό σας βρίσκεται μέσα στο διαμέρισμα"),
 ],
 "gloss": {"υδρομέτρων": "υδρόμετρο — water meter", "ύδρευσης": "ύδρευση — water supply", "αντικατάστασης": "αντικατάσταση — replacement", "συνεργείο": "συνεργείο — (work) crew", "ένδειξη": "ένδειξη — reading", "κομμένο": "κομμένος — cut off", "εξυπηρέτησης πελατών": "εξυπηρέτηση πελατών — customer service"},
})

ITEMS.append({
 "id": "l165-c1-antikatoptrismos", "title": "Νερό που δεν υπάρχει", "title_en": "Water that isn't there", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν μετεωρολόγο για τους αντικατοπτρισμούς.",
 "script": [
  L("Δημοσιογράφος", "f", "Όλοι έχουμε δει το καλοκαίρι στην άσφαλτο κάτι που μοιάζει με λακκούβες νερού και εξαφανίζεται όταν πλησιάζουμε. Τι είναι αυτό;", "We've all seen on the asphalt in summer something that looks like puddles of water and disappears when we get closer. What is it?"),
  L("Μετεωρολόγος", "m", "Είναι ο πιο συνηθισμένος αντικατοπτρισμός. Πάνω από τον καυτό δρόμο σχηματίζεται ένα λεπτό στρώμα πολύ ζεστού αέρα, και από πάνω του ο αέρας είναι πιο δροσερός. Το φως ταξιδεύει λίγο διαφορετικά στον ζεστό και στον κρύο αέρα, και έτσι οι ακτίνες που έρχονται από τον ουρανό καμπυλώνονται προς τα πάνω λίγο πριν φτάσουν στο έδαφος. Αυτό που βλέπουμε δηλαδή δεν είναι νερό, αλλά ένα κομμάτι του ουρανού.", "It's the most common mirage. Above the hot road a thin layer of very hot air forms, and above it the air is cooler. Light travels slightly differently in hot and in cold air, and so the rays coming from the sky curve upwards just before they reach the ground. In other words, what we see isn't water but a piece of the sky."),
  L("Δημοσιογράφος", "f", "Υπάρχουν και αντικατοπτρισμοί προς τα πάνω;", "Are there mirages upwards as well?"),
  L("Μετεωρολόγος", "m", "Ναι, όταν συμβαίνει το αντίθετο: όταν πάνω από μια κρύα θάλασσα βρίσκεται ένα στρώμα ζεστότερου αέρα. Τότε τα πλοία στον ορίζοντα μπορεί να φαίνονται σαν να αιωρούνται, ή ακόμη να εμφανίζονται ανάποδα πάνω από το πραγματικό τους είδωλο. Είναι πολύ πιθανό αρκετοί θρύλοι για φαντάσματα πλοία να ξεκίνησαν έτσι.", "Yes, when the opposite happens: when there's a layer of warmer air above a cold sea. Then ships on the horizon may appear to float, or even appear upside down above their real image. It's quite likely that several legends about ghost ships started that way."),
  L("Δημοσιογράφος", "f", "Και η περίφημη Φάτα Μοργκάνα;", "And the famous Fata Morgana?"),
  L("Μετεωρολόγος", "m", "Είναι μια πιο σύνθετη μορφή, όπου πολλά στρώματα αέρα δημιουργούν εικόνες που αλλάζουν συνεχώς: ακτές που μοιάζουν με ψηλά κάστρα, βράχοι που τεντώνονται και ξαναμαζεύονται. Το όνομα προέρχεται από τη νεράιδα Μοργκάνα των θρύλων του Αρθούρου, γιατί οι ναυτικοί στα στενά της Μεσσήνης πίστευαν ότι εκείνη έχτιζε αυτά τα κάστρα για να τους παρασύρει. Είναι ένα ωραίο παράδειγμα για το πώς η φυσική εξηγεί έναν μύθο χωρίς να τον κάνει λιγότερο γοητευτικό.", "It's a more complex form, in which many layers of air create images that keep changing: coasts that look like tall castles, rocks that stretch and shrink back. The name comes from the fairy Morgan of the Arthurian legends, because sailors in the Strait of Messina believed she built these castles to lure them. It's a fine example of how physics explains a myth without making it any less fascinating."),
 ],
 "questions": [
  Q("Τι βλέπουμε στην πραγματικότητα όταν φαίνεται νερό στην άσφαλτο;", ["Υδρατμούς από τον δρόμο", "Ένα κομμάτι του ουρανού", "Λάδι από τα αυτοκίνητα", "Την αντανάκλαση των δέντρων"], 1, "Αυτό που βλέπουμε δηλαδή δεν είναι νερό, αλλά ένα κομμάτι του ουρανού"),
  Q("Πότε εμφανίζονται αντικατοπτρισμοί προς τα πάνω;", ["Όταν ένα στρώμα ζεστότερου αέρα βρίσκεται πάνω από μια κρύα θάλασσα", "Όταν βρέχει", "Μόνο τη νύχτα", "Όταν φυσάει δυνατός άνεμος"], 0, "όταν πάνω από μια κρύα θάλασσα βρίσκεται ένα στρώμα ζεστότερου αέρα"),
  Q("Τι πιστεύει ο μετεωρολόγος για τους θρύλους με φαντάσματα πλοία;", ["Ότι είναι αληθινές ιστορίες", "Ότι τους έγραψαν ποιητές", "Ότι αρκετοί πιθανότατα ξεκίνησαν από αντικατοπτρισμούς", "Ότι δεν έχουν καμία σχέση με τη φύση"], 2, "Είναι πολύ πιθανό αρκετοί θρύλοι για φαντάσματα πλοία να ξεκίνησαν έτσι"),
  Q("Από πού πήρε το όνομά της η Φάτα Μοργκάνα;", ["Από μια πόλη της Ιταλίας", "Από τη νεράιδα Μοργκάνα των θρύλων του Αρθούρου", "Από έναν επιστήμονα", "Από ένα πλοίο"], 1, "Το όνομα προέρχεται από τη νεράιδα Μοργκάνα των θρύλων του Αρθούρου"),
 ],
 "gloss": {"αντικατοπτρισμούς": "αντικατοπτρισμός — mirage", "αντικατοπτρισμός": "αντικατοπτρισμός — mirage", "άσφαλτο": "άσφαλτος — asphalt, road surface", "λακκούβες": "λακκούβα — puddle, pothole", "καυτό": "καυτός — scorching", "καμπυλώνονται": "καμπυλώνομαι — to curve", "ορίζοντα": "ορίζοντας — horizon", "αιωρούνται": "αιωρούμαι — to float, to hover", "είδωλο": "είδωλο — image", "θρύλοι": "θρύλος — legend", "σύνθετη": "σύνθετος — complex", "τεντώνονται": "τεντώνομαι — to stretch", "νεράιδα": "νεράιδα — fairy", "παρασύρει": "παρασύρω — to lure, to lead astray", "γοητευτικό": "γοητευτικός — fascinating"},
})

ITEMS.append({
 "id": "l165-c1-anthrakas", "title": "Το ρολόι του άνθρακα", "title_en": "The carbon clock", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια αρχαιομετρική να εξηγεί σε μια διάλεξη πώς λειτουργεί η χρονολόγηση με ραδιενεργό άνθρακα.",
 "script": [
  L("Αρχαιομετρικός", "f", "Όταν οι αρχαιολόγοι λένε ότι ένα κομμάτι ξύλο από μια ανασκαφή είναι τεσσάρων χιλιάδων ετών, συνήθως η πληροφορία προέρχεται από τη μέθοδο του άνθρακα δεκατέσσερα. Τη μέθοδο ανέπτυξε στα τέλη της δεκαετίας του 1940 ο Αμερικανός χημικός Γουίλαρντ Λίμπι, ο οποίος τιμήθηκε γι' αυτήν με βραβείο Νόμπελ.", "When archaeologists say that a piece of wood from an excavation is four thousand years old, the information usually comes from the carbon-fourteen method. The method was developed in the late 1940s by the American chemist Willard Libby, who was awarded a Nobel Prize for it."),
  L("Αρχαιομετρικός", "f", "Η αρχή είναι απλή. Στην ατμόσφαιρα υπάρχει, σε πολύ μικρή ποσότητα, μια ραδιενεργή μορφή άνθρακα. Όσο ένας οργανισμός ζει, την προσλαμβάνει συνεχώς, με την αναπνοή ή με την τροφή. Μόλις πεθάνει, η πρόσληψη σταματά, και ο ραδιενεργός άνθρακας αρχίζει να διασπάται με σταθερό ρυθμό: κάθε πέντε χιλιάδες επτακόσια περίπου χρόνια μένει ο μισός. Μετρώντας πόσος έχει απομείνει, υπολογίζουμε πόσος χρόνος πέρασε από τον θάνατο.", "The principle is simple. In the atmosphere there is, in a very small amount, a radioactive form of carbon. As long as an organism lives, it takes it in continuously, through breathing or food. As soon as it dies, the intake stops, and the radioactive carbon begins to decay at a steady rate: roughly every five thousand seven hundred years, half of it remains. By measuring how much is left, we calculate how much time has passed since death."),
  L("Αρχαιομετρικός", "f", "Η μέθοδος έχει όμως όρια. Πέρα από τα πενήντα χιλιάδες περίπου χρόνια, η ποσότητα που απομένει είναι τόσο μικρή που δεν μετριέται αξιόπιστα. Επιπλέον, η ποσότητα του ραδιενεργού άνθρακα στην ατμόσφαιρα δεν ήταν πάντα ίδια, γι' αυτό οι μετρήσεις διορθώνονται με βάση τους δακτυλίους δέντρων, των οποίων η ηλικία είναι γνωστή με ακρίβεια έτους. Και κάτι παράδοξο: οι πυρηνικές δοκιμές των δεκαετιών του '50 και του '60 σχεδόν διπλασίασαν προσωρινά τον ραδιενεργό άνθρακα στην ατμόσφαιρα, και αυτό το «σημάδι» χρησιμοποιείται σήμερα ακόμη και για να χρονολογηθούν σύγχρονα δείγματα.", "The method has limits, though. Beyond about fifty thousand years, the amount remaining is so small that it can't be measured reliably. Moreover, the amount of radioactive carbon in the atmosphere wasn't always the same, which is why measurements are corrected on the basis of tree rings, whose age is known to the year. And something paradoxical: the nuclear tests of the '50s and '60s temporarily almost doubled the radioactive carbon in the atmosphere, and this 'mark' is used today even to date modern samples."),
 ],
 "questions": [
  Q("Ποιος ανέπτυξε τη μέθοδο;", ["Ένας Γάλλος φυσικός", "Ο Αμερικανός χημικός Γουίλαρντ Λίμπι", "Μια ομάδα αρχαιολόγων", "Ένας Βρετανός γεωλόγος"], 1, "ο Αμερικανός χημικός Γουίλαρντ Λίμπι"),
  Q("Τι συμβαίνει όταν ένας οργανισμός πεθαίνει;", ["Ο ραδιενεργός άνθρακας αυξάνεται", "Η πρόσληψη σταματά και ο ραδιενεργός άνθρακας αρχίζει να διασπάται", "Ο άνθρακας μετατρέπεται σε οξυγόνο", "Τίποτα δεν αλλάζει"], 1, "Μόλις πεθάνει, η πρόσληψη σταματά, και ο ραδιενεργός άνθρακας αρχίζει να διασπάται"),
  Q("Γιατί οι μετρήσεις διορθώνονται με βάση τους δακτυλίους δέντρων;", ["Γιατί η ποσότητα του ραδιενεργού άνθρακα στην ατμόσφαιρα δεν ήταν πάντα ίδια", "Γιατί τα δέντρα δεν περιέχουν άνθρακα", "Γιατί τα όργανα είναι ανακριβή", "Γιατί η μέθοδος δεν λειτουργεί για ξύλο"], 0, "η ποσότητα του ραδιενεργού άνθρακα στην ατμόσφαιρα δεν ήταν πάντα ίδια"),
  Q("Τι «παράδοξο» αναφέρει η ομιλήτρια στο τέλος;", ["Ότι η μέθοδος δεν λειτουργεί για σύγχρονα δείγματα", "Ότι οι πυρηνικές δοκιμές άφησαν ένα σημάδι που βοηθά να χρονολογηθούν σύγχρονα δείγματα", "Ότι ο άνθρακας διασπάται πιο γρήγορα στη θάλασσα", "Ότι οι δακτύλιοι των δέντρων ψεύδονται"], 1, "αυτό το «σημάδι» χρησιμοποιείται σήμερα ακόμη και για να χρονολογηθούν σύγχρονα δείγματα"),
 ],
 "gloss": {"αρχαιομετρική": "αρχαιομετρικός — archaeometrist (scientist dating finds)", "χρονολόγηση": "χρονολόγηση — dating", "ραδιενεργό": "ραδιενεργός — radioactive", "ανασκαφή": "ανασκαφή — excavation", "Λίμπι": "Λίμπι — Libby", "προσλαμβάνει": "προσλαμβάνω — to take in", "πρόσληψη": "πρόσληψη — intake", "διασπάται": "διασπώμαι — to decay, to break down", "απομείνει": "απομένω — to remain", "αξιόπιστα": "αξιόπιστα — reliably", "δακτυλίους": "δακτύλιος — ring", "πυρηνικές δοκιμές": "πυρηνικές δοκιμές — nuclear tests", "διπλασίασαν": "διπλασιάζω — to double", "δείγματα": "δείγμα — sample"},
})

rnd = random.Random(165)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-165.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
