# Source for library/listening/listening-192.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l192.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l192-ann-drone-sto-aerodromio", "title": "Καθυστερήσεις λόγω drone πάνω από το αεροδρόμιο", "title_en": "Delays because of a drone over the airport", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε στην αίθουσα αναμονής ενός αεροδρομίου και ακούτε μια ανακοίνωση.",
 "script": [
  L("Εκφωνήτρια", "f", "Κυρίες και κύριοι, σας ενημερώνουμε ότι πριν από λίγα λεπτά εντοπίστηκε ένα μη επανδρωμένο αεροσκάφος, ένα drone, κοντά στον διάδρομο προσγείωσης. Για λόγους ασφαλείας, όλες οι απογειώσεις και οι προσγειώσεις έχουν σταματήσει προσωρινά, μέχρι να απομακρυνθεί.", "Ladies and gentlemen, we inform you that a few minutes ago an unmanned aircraft, a drone, was spotted near the runway. For safety reasons, all take-offs and landings have been temporarily suspended until it is removed."),
  L("Εκφωνήτρια", "f", "Οι αρχές ερευνούν την περιοχή γύρω από το αεροδρόμιο. Αναμένονται καθυστερήσεις τουλάχιστον μίας ώρας, και ορισμένες πτήσεις που πλησίαζαν το αεροδρόμιο έχουν εκτραπεί σε γειτονικά αεροδρόμια. Παρακαλούμε να παρακολουθείτε τις οθόνες για τις νέες ώρες αναχώρησης.", "The authorities are searching the area around the airport. Delays of at least one hour are expected, and some flights that were approaching the airport have been diverted to neighbouring airports. Please follow the screens for the new departure times."),
  L("Εκφωνήτρια", "f", "Οι επιβάτες που θα χάσουν την ανταπόκρισή τους μπορούν να απευθυνθούν στο γκισέ της εταιρείας τους. Υπενθυμίζουμε ότι η πτήση drone σε απόσταση μικρότερη από οχτώ χιλιόμετρα από αεροδρόμιο απαγορεύεται και τιμωρείται αυστηρά. Ευχαριστούμε για την υπομονή σας.", "Passengers who will miss their connection can go to their airline's desk. We remind you that flying a drone less than eight kilometres from an airport is prohibited and severely punished. Thank you for your patience."),
 ],
 "questions": [
  Q("Γιατί σταμάτησαν οι πτήσεις;", ["Λόγω κακοκαιρίας", "Επειδή εντοπίστηκε ένα drone κοντά στον διάδρομο", "Λόγω απεργίας", "Επειδή χάλασε ένα αεροπλάνο"], 1, "εντοπίστηκε ένα μη επανδρωμένο αεροσκάφος, ένα drone, κοντά στον διάδρομο προσγείωσης"),
  Q("Τι έγινε με ορισμένες πτήσεις που πλησίαζαν;", ["Ακυρώθηκαν", "Προσγειώθηκαν κανονικά", "Εκτράπηκαν σε γειτονικά αεροδρόμια", "Γύρισαν στο αεροδρόμιο αναχώρησης"], 2, "ορισμένες πτήσεις που πλησίαζαν το αεροδρόμιο έχουν εκτραπεί σε γειτονικά αεροδρόμια"),
  Q("Πού πρέπει να πάνε όσοι χάσουν την ανταπόκρισή τους;", ["Στο γκισέ της εταιρείας τους", "Στο γραφείο πληροφοριών", "Στην αστυνομία του αεροδρομίου", "Στην πύλη αναχώρησης"], 0, "μπορούν να απευθυνθούν στο γκισέ της εταιρείας τους"),
 ],
 "gloss": {"επανδρωμένο": "επανδρωμένος — manned", "διάδρομο": "διάδρομος — runway", "απογειώσεις": "απογείωση — take-off", "εκτραπεί": "εκτρέπομαι — to be diverted", "ανταπόκρισή": "ανταπόκριση — connection (flight)", "γκισέ": "γκισέ — desk, counter"},
})

ITEMS.append({
 "id": "l192-int-akrovatissa-yfasmaton", "title": "Η ακροβάτισσα των εναέριων υφασμάτων", "title_en": "The aerial silks acrobat", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια ακροβάτισσα που δουλεύει σε ένα σύγχρονο τσίρκο.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνετε στην παράσταση;", "What exactly do you do in the show?"),
  L("Ακροβάτισσα", "f", "Κάνω το νούμερο των εναέριων υφασμάτων. Ανεβαίνω σε δύο μακριά υφάσματα που κρέμονται από την οροφή, σε ύψος οχτώ μέτρων, και κάνω φιγούρες χωρίς δίχτυ από κάτω. Τυλίγομαι στο ύφασμα και μετά αφήνομαι να πέσω, ώσπου να με σταματήσει ο κόμπος λίγο πριν από το έδαφος. Το κοινό πάντα φωνάζει σ' εκείνο το σημείο.", "I climb two long pieces of fabric that hang from the ceiling, at a height of eight metres, and I do figures with no net below. I wrap myself in the fabric and then let myself drop, until the knot stops me just above the ground. The audience always shouts at that point."),
  L("Δημοσιογράφος", "m", "Πώς ξεκινήσατε;", "How did you start?"),
  L("Ακροβάτισσα", "f", "Ήμουν αθλήτρια της ενόργανης γυμναστικής, αλλά στα δεκαεννιά τραυματίστηκα στον ώμο και σταμάτησα. Ένας φίλος με πήγε σε ένα μάθημα εναέριας ακροβατικής για να ξεσκάσω, και από την πρώτη μέρα ένιωσα ότι είχα βρει τον δρόμο μου. Η διαφορά είναι ότι εδώ δεν σε βαθμολογεί κανείς. Πρέπει να συγκινήσεις, όχι να είσαι τέλεια.", "I was an artistic gymnast, but at nineteen I injured my shoulder and stopped. A friend took me to an aerial acrobatics class to take my mind off it, and from the first day I felt I'd found my path. The difference is that here nobody scores you. You have to move people, not be perfect."),
  L("Δημοσιογράφος", "m", "Φοβάστε ποτέ;", "Are you ever afraid?"),
  L("Ακροβάτισσα", "f", "Όχι το ύψος. Φοβάμαι την κούραση, γιατί τα λάθη γίνονται στο τέλος μιας μεγάλης περιοδείας, όταν τα χέρια δεν έχουν πια δύναμη. Γι' αυτό ελέγχω κάθε βράδυ μόνη μου τα σχοινιά και το ύφασμα, ακόμα κι αν το έχει κάνει ήδη ο τεχνικός. Είναι η ζωή μου, δεν την αφήνω σε άλλους.", "Not the height. I'm afraid of tiredness, because mistakes happen at the end of a long tour, when your arms have no strength left. That's why I check the ropes and the fabric myself every night, even if the technician has already done it. It's my life, I don't leave it to others."),
 ],
 "questions": [
  Q("Τι γίνεται στο σημείο όπου φωνάζει το κοινό;", ["Η ακροβάτισσα πέφτει στο δίχτυ", "Αφήνεται να πέσει ώσπου τη σταματά ο κόμπος", "Σκίζεται το ύφασμα", "Ανεβαίνει στην οροφή"], 1, "αφήνομαι να πέσω, ώσπου να με σταματήσει ο κόμπος λίγο πριν από το έδαφος"),
  Q("Γιατί σταμάτησε τη γυμναστική;", ["Γιατί βαρέθηκε τους αγώνες", "Γιατί τραυματίστηκε στον ώμο", "Γιατί δεν είχε χρήματα", "Γιατί μετακόμισε"], 1, "στα δεκαεννιά τραυματίστηκα στον ώμο και σταμάτησα"),
  Q("Τι φοβάται περισσότερο;", ["Το ύψος", "Το κοινό", "Την κούραση στο τέλος μιας περιοδείας", "Τους τεχνικούς"], 2, "Φοβάμαι την κούραση"),
 ],
 "gloss": {"ακροβάτισσα": "ακροβάτισσα — acrobat (f.)", "εναέριων": "εναέριος — aerial", "υφάσματα": "ύφασμα — fabric", "δίχτυ": "δίχτυ — net", "κόμπος": "κόμπος — knot", "ενόργανης": "ενόργανη γυμναστική — artistic gymnastics", "ξεσκάσω": "ξεσκάω — to unwind, take one's mind off things", "περιοδείας": "περιοδεία — tour"},
})

ITEMS.append({
 "id": "l192-vm-scholi-istiosanidas", "title": "Μήνυμα από τη σχολή ιστιοσανίδας", "title_en": "A message from the windsurfing school", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει μαθήματα ιστιοσανίδας στις διακοπές σας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Εκπαιδευτής", "m", "Γεια σας, ο Μάρκος είμαι από τη σχολή ιστιοσανίδας στην παραλία. Σας παίρνω για το αυριανό σας μάθημα στις δέκα. Η πρόγνωση δίνει μελτέμι επτά μποφόρ από το πρωί, και αυτό είναι πολύ για αρχάριους. Δεν θα μπορέσετε ούτε να σηκώσετε το πανί.", "Hello, it's Markos from the windsurfing school on the beach. I'm calling about your lesson tomorrow at ten. The forecast says a seven-Beaufort meltemi from the morning, and that's too much for beginners. You wouldn't even be able to lift the sail."),
  L("Εκπαιδευτής", "m", "Σας προτείνω δύο λύσεις. Μπορούμε να μεταφέρουμε το μάθημα στις επτά το πρωί, πριν δυναμώσει ο αέρας, ή να το κάνουμε μεθαύριο, που η θάλασσα θα είναι πιο ήσυχη. Αν δεν σας βολεύει τίποτα από τα δύο, σας επιστρέφουμε φυσικά τα χρήματα.", "I suggest two options. We can move the lesson to seven in the morning, before the wind picks up, or do it the day after tomorrow, when the sea will be calmer. If neither suits you, we will of course refund your money."),
  L("Εκπαιδευτής", "m", "Αν διαλέξετε το πρωινό, φέρτε μαζί σας ένα αντιανεμικό, γιατί τόσο νωρίς κάνει ψύχρα, και αντηλιακό για μετά. Τη στολή και το σωσίβιο τα δίνουμε εμείς. Στείλτε μου απλώς ένα μήνυμα με αυτό που προτιμάτε.", "If you choose the early one, bring a windbreaker, because it's chilly that early, and sunscreen for afterwards. We provide the wetsuit and the life jacket. Just send me a message with what you prefer."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να γίνει το μάθημα στην ώρα του;", ["Γιατί ο εκπαιδευτής είναι άρρωστος", "Γιατί ο αέρας θα είναι πολύ δυνατός για αρχάριους", "Γιατί η παραλία θα είναι κλειστή", "Γιατί δεν υπάρχει καθόλου αέρας"], 1, "Η πρόγνωση δίνει μελτέμι επτά μποφόρ από το πρωί, και αυτό είναι πολύ για αρχάριους"),
  Q("Ποια λύση ΔΕΝ προτείνει ο εκπαιδευτής;", ["Μάθημα στις επτά το πρωί", "Μάθημα μεθαύριο", "Επιστροφή χρημάτων", "Μάθημα σε πισίνα"], 3, "Μπορούμε να μεταφέρουμε το μάθημα στις επτά το πρωί"),
  Q("Τι πρέπει να φέρετε αν διαλέξετε το πρωινό μάθημα;", ["Στολή και σωσίβιο", "Αντιανεμικό και αντηλιακό", "Τη δική σας σανίδα", "Πρωινό"], 1, "φέρτε μαζί σας ένα αντιανεμικό, γιατί τόσο νωρίς κάνει ψύχρα, και αντηλιακό"),
 ],
 "gloss": {"ιστιοσανίδας": "ιστιοσανίδα — windsurfing (board)", "μελτέμι": "μελτέμι — meltemi (strong summer north wind)", "μποφόρ": "μποφόρ — Beaufort (wind force)", "πανί": "πανί — sail", "αντιανεμικό": "αντιανεμικό — windbreaker", "σωσίβιο": "σωσίβιο — life jacket"},
})

ITEMS.append({
 "id": "l192-mono-cheimonas-erasmus-finlandia", "title": "Ένας χειμώνας με Έρασμους στη Φινλανδία", "title_en": "An Erasmus winter in Finland", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια φοιτήτρια να μιλάει σε ένα ραδιοφωνικό πρόγραμμα για το εξάμηνο που πέρασε στο εξωτερικό.",
 "script": [
  L("Ιωάννα", "f", "Όταν διάλεξα τη Φινλανδία για το Έρασμους, όλοι στην Κρήτη με κοίταζαν σαν να είχα τρελαθεί. Έφτασα στις αρχές Ιανουαρίου, σε μια πόλη στο κέντρο της χώρας, και ο ήλιος έβγαινε μόνο για λίγες ώρες. Την πρώτη εβδομάδα κοιμόμουν όλη την ώρα, γιατί το σώμα μου δεν καταλάβαινε πότε είναι μέρα.", "When I chose Finland for Erasmus, everyone in Crete looked at me as if I'd gone mad. I arrived in early January, in a town in the centre of the country, and the sun came out only for a few hours. The first week I slept all the time, because my body couldn't tell when it was day."),
  L("Ιωάννα", "f", "Αυτό που με έσωσε ήταν οι Φινλανδοί συμφοιτητές μου. Μου έμαθαν να ντύνομαι σε στρώσεις, να κάνω σκι αντοχής στο δάσος και, το πιο απίστευτο, να βουτάω σε μια τρύπα στον πάγο της λίμνης μετά τη σάουνα. Την πρώτη φορά ούρλιαξα τόσο δυνατά, που ήρθε τρέχοντας ο φύλακας.", "What saved me were my Finnish fellow students. They taught me to dress in layers, to go cross-country skiing in the forest and, most unbelievably, to plunge into a hole in the lake ice after the sauna. The first time I screamed so loudly that the caretaker came running."),
  L("Ιωάννα", "f", "Στην αρχή νόμιζα ότι οι Φινλανδοί είναι ψυχροί, γιατί μιλάνε λίγο και δεν πιάνουν κουβέντα στο λεωφορείο. Μετά κατάλαβα ότι απλώς δεν λένε τίποτα που δεν το εννοούν. Όταν ένας από αυτούς σού λέει «θα σε βοηθήσω», να είσαι σίγουρη ότι θα έρθει. Αυτό το έφερα μαζί μου στην Κρήτη, μαζί με ένα ζευγάρι μάλλινες κάλτσες.", "At first I thought Finns were cold, because they speak little and don't strike up conversations on the bus. Then I realised they simply don't say anything they don't mean. When one of them tells you 'I'll help you', you can be sure they'll come. I brought that back with me to Crete, along with a pair of woollen socks."),
 ],
 "questions": [
  Q("Γιατί κοιμόταν πολύ την πρώτη εβδομάδα;", ["Γιατί ήταν άρρωστη", "Γιατί το σώμα της δεν καταλάβαινε πότε είναι μέρα", "Γιατί δεν είχε μαθήματα", "Γιατί έκανε πολύ κρύο"], 1, "το σώμα μου δεν καταλάβαινε πότε είναι μέρα"),
  Q("Τι έγινε την πρώτη φορά που βούτηξε στη λίμνη;", ["Ούρλιαξε και ήρθε τρέχοντας ο φύλακας", "Αρρώστησε", "Δεν μπόρεσε να μπει στο νερό", "Γλίστρησε στον πάγο"], 0, "ούρλιαξα τόσο δυνατά, που ήρθε τρέχοντας ο φύλακας"),
  Q("Τι κατάλαβε τελικά για τους Φινλανδούς;", ["Ότι είναι πράγματι ψυχροί", "Ότι μιλούν πολύ", "Ότι δεν λένε τίποτα που δεν το εννοούν", "Ότι δεν βοηθούν τους ξένους"], 2, "απλώς δεν λένε τίποτα που δεν το εννοούν"),
 ],
 "gloss": {"εξάμηνο": "εξάμηνο — semester", "συμφοιτητές": "συμφοιτητής — fellow student", "στρώσεις": "στρώση — layer", "αντοχής": "σκι αντοχής — cross-country skiing", "ούρλιαξα": "ουρλιάζω — to scream, howl", "μάλλινες": "μάλλινος — woollen"},
})

ITEMS.append({
 "id": "l192-dia-lizingk-i-agora", "title": "Λίζινγκ ή αγορά αυτοκινήτου;", "title_en": "Leasing or buying a car?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φίλοι συζητούν αν αξίζει να αγοράσει κανείς αυτοκίνητο ή να το νοικιάσει με λίζινγκ.",
 "script": [
  L("Στέλιος", "m", "Το παλιό μου αυτοκίνητο πέθανε οριστικά. Ο συνάδελφός μου μού λέει να μην αγοράσω, να πάρω ένα με λίζινγκ. Πληρώνεις ένα σταθερό ποσό τον μήνα και μέσα είναι η ασφάλεια, το σέρβις, ακόμα και τα λάστιχα.", "My old car has died for good. My colleague tells me not to buy, to get one on a lease. You pay a fixed amount a month and it includes the insurance, the servicing, even the tyres."),
  L("Ρένα", "f", "Ακούγεται βολικό, αλλά στο τέλος του συμβολαίου επιστρέφεις το αυτοκίνητο και δεν σου μένει τίποτα. Αν το αγοράσεις, μετά από πέντε χρόνια έχεις τουλάχιστον κάτι να πουλήσεις.", "It sounds convenient, but at the end of the contract you hand the car back and you're left with nothing. If you buy it, after five years you at least have something to sell."),
  L("Στέλιος", "m", "Ναι, αλλά για να το αγοράσω πρέπει να πάρω δάνειο, και με αυτά τα επιτόκια δεν το βλέπω. Με το λίζινγκ δεν δίνω προκαταβολή.", "Yes, but to buy it I'd have to take out a loan, and with these interest rates I don't see it. With leasing I don't pay a deposit."),
  L("Ρένα", "f", "Πρόσεξε μόνο τα ψιλά γράμματα. Τα περισσότερα συμβόλαια έχουν όριο χιλιομέτρων τον χρόνο, και αν το ξεπεράσεις, πληρώνεις για κάθε επιπλέον χιλιόμετρο. Εσύ που πηγαίνεις κάθε Σαββατοκύριακο στο χωριό, θα το ξεπεράσεις σίγουρα. Και αν το επιστρέψεις με γρατζουνιές, θα σου τις χρεώσουν.", "Just watch out for the small print. Most contracts have a yearly mileage limit, and if you exceed it, you pay for every extra kilometre. You go to the village every weekend, so you'll certainly exceed it. And if you return it with scratches, they'll charge you for them."),
  L("Στέλιος", "m", "Δεν το είχα σκεφτεί αυτό με τα χιλιόμετρα. Θα ζητήσω προσφορά με μεγαλύτερο όριο και θα τη συγκρίνω με το κόστος ενός δανείου. Μετά αποφασίζω.", "I hadn't thought about the kilometres. I'll ask for an offer with a higher limit and compare it with the cost of a loan. Then I'll decide."),
 ],
 "questions": [
  Q("Τι περιλαμβάνει, σύμφωνα με τον Στέλιο, η μηνιαία δόση του λίζινγκ;", ["Μόνο το αυτοκίνητο", "Την ασφάλεια, το σέρβις και τα λάστιχα", "Τα καύσιμα", "Τα διόδια"], 1, "μέσα είναι η ασφάλεια, το σέρβις, ακόμα και τα λάστιχα"),
  Q("Ποιο μειονέκτημα του λίζινγκ αναφέρει πρώτα η Ρένα;", ["Είναι πολύ ακριβό", "Στο τέλος επιστρέφεις το αυτοκίνητο και δεν σου μένει τίποτα", "Θέλει μεγάλη προκαταβολή", "Δεν μπορείς να διαλέξεις μοντέλο"], 1, "στο τέλος του συμβολαίου επιστρέφεις το αυτοκίνητο και δεν σου μένει τίποτα"),
  Q("Γιατί πιστεύει η Ρένα ότι ο Στέλιος θα ξεπεράσει το όριο χιλιομέτρων;", ["Γιατί δουλεύει ως οδηγός", "Γιατί πηγαίνει κάθε Σαββατοκύριακο στο χωριό", "Γιατί θα μετακομίσει", "Γιατί κάνει μεγάλα ταξίδια στο εξωτερικό"], 1, "πηγαίνεις κάθε Σαββατοκύριακο στο χωριό"),
 ],
 "gloss": {"λίζινγκ": "λίζινγκ — leasing", "σέρβις": "σέρβις — servicing", "συμβολαίου": "συμβόλαιο — contract", "επιτόκια": "επιτόκιο — interest rate", "προκαταβολή": "προκαταβολή — deposit, down payment", "γρατζουνιές": "γρατζουνιά — scratch", "χρεώσουν": "χρεώνω — to charge"},
})

ITEMS.append({
 "id": "l192-news-minyma-se-boukali", "title": "Μήνυμα σε μπουκάλι βρέθηκε μετά από τριάντα χρόνια", "title_en": "A message in a bottle found after thirty years", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση σε ένα τοπικό ραδιοφωνικό δελτίο.",
 "script": [
  L("Εκφωνητής", "m", "Ένα γυάλινο μπουκάλι με ένα χειρόγραφο μήνυμα μέσα βρήκε την περασμένη Κυριακή ένας ψαράς σε μια απόμερη παραλία της Κεφαλονιάς. Το χαρτί είχε κιτρινίσει, αλλά τα γράμματα διαβάζονταν ακόμη καθαρά.", "Last Sunday a fisherman found a glass bottle with a handwritten message inside on a remote beach in Kefalonia. The paper had turned yellow, but the letters could still be read clearly."),
  L("Εκφωνητής", "m", "Το μήνυμα είχε γραφτεί το καλοκαίρι του ενενήντα τέσσερα από ένα δεκάχρονο κορίτσι από την Ιταλία, που ταξίδευε με το πλοίο προς την Πάτρα. Έγραφε το όνομά της, τη διεύθυνσή της και ζητούσε από όποιον το βρει να της στείλει μια κάρτα.", "The message had been written in the summer of ninety-four by a ten-year-old girl from Italy, who was travelling on the ferry to Patras. She wrote her name and her address and asked whoever found it to send her a card."),
  L("Εκφωνητής", "m", "Ο ψαράς δημοσίευσε τη φωτογραφία του μηνύματος στο διαδίκτυο, και μέσα σε δύο μέρες εντοπίστηκε η γυναίκα, που σήμερα είναι σαράντα χρονών και δασκάλα στο Μπάρι. Όπως δήλωσε, είχε ξεχάσει εντελώς το μπουκάλι, και σκοπεύει να επισκεφθεί το νησί το καλοκαίρι μαζί με τα παιδιά της, για να γνωρίσει τον ψαρά από κοντά.", "The fisherman posted the photo of the message online, and within two days the woman was traced; today she is forty and a teacher in Bari. She said she had completely forgotten the bottle, and she plans to visit the island in the summer with her children to meet the fisherman in person."),
 ],
 "questions": [
  Q("Σε τι κατάσταση ήταν το μήνυμα;", ["Είχε σβηστεί εντελώς", "Το χαρτί είχε κιτρινίσει, αλλά διαβαζόταν", "Ήταν βρεγμένο και σκισμένο", "Ήταν σαν καινούργιο"], 1, "Το χαρτί είχε κιτρινίσει, αλλά τα γράμματα διαβάζονταν ακόμη καθαρά"),
  Q("Τι ζητούσε το κορίτσι στο μήνυμα;", ["Να της στείλουν μια κάρτα", "Να της τηλεφωνήσουν", "Να ξαναρίξουν το μπουκάλι στη θάλασσα", "Βοήθεια"], 0, "ζητούσε από όποιον το βρει να της στείλει μια κάρτα"),
  Q("Πώς εντοπίστηκε η γυναίκα;", ["Μέσω της ιταλικής πρεσβείας", "Μέσω της εταιρείας του πλοίου", "Αφού ο ψαράς δημοσίευσε φωτογραφία στο διαδίκτυο", "Από την αστυνομία"], 2, "Ο ψαράς δημοσίευσε τη φωτογραφία του μηνύματος στο διαδίκτυο"),
 ],
 "gloss": {"χειρόγραφο": "χειρόγραφος — handwritten", "απόμερη": "απόμερος — remote, secluded", "κιτρινίσει": "κιτρινίζω — to turn yellow", "εντοπίστηκε": "εντοπίζομαι — to be traced, located", "δήλωσε": "δηλώνω — to state, declare"},
})

ITEMS.append({
 "id": "l192-rep-ethelontes-xoklisia", "title": "Εθελοντές ασβεστώνουν τα ξωκλήσια", "title_en": "Volunteers whitewash the country chapels", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από ένα νησί των Κυκλάδων.",
 "script": [
  L("Ρεπόρτερ", "f", "Είναι επτά το πρωί, και μια παρέα από είκοσι εθελοντές ανεβαίνει το μονοπάτι με κουβάδες, πινέλα και σακιά ασβέστη στην πλάτη. Ο προορισμός τους είναι ένα μικρό ξωκλήσι στην κορυφή του λόφου, που έχει να βαφτεί πάνω από δέκα χρόνια.", "It is seven in the morning, and a group of twenty volunteers is climbing the path with buckets, brushes and sacks of lime on their backs. Their destination is a small country chapel on top of the hill, which hasn't been painted for over ten years."),
  L("Ρεπόρτερ", "f", "Η πρωτοβουλία ξεκίνησε πριν από τρία χρόνια από δύο συνταξιούχους δασκάλους. Στο νησί υπάρχουν πάνω από διακόσια ξωκλήσια, πολλά από τα οποία ανήκουν σε οικογένειες που έχουν φύγει στην Αθήνα ή στο εξωτερικό. Χωρίς φροντίδα, ο ασβέστης ξεφλουδίζει και η υγρασία μπαίνει στους τοίχους.", "The initiative was started three years ago by two retired teachers. On the island there are over two hundred country chapels, many of which belong to families who have left for Athens or abroad. Without care, the whitewash peels and damp gets into the walls."),
  L("Ρεπόρτερ", "f", "Οι εθελοντές δουλεύουν μόνο πρωί και απόγευμα, γιατί το μεσημέρι ο ασβέστης στεγνώνει πολύ γρήγορα και σκάει. Πριν ξεκινήσουν, ζητούν πάντα την άδεια των ιδιοκτητών. Μέχρι σήμερα έχουν ασβεστώσει σαράντα δύο εκκλησάκια, και στο τέλος κάθε δουλειάς ο παπάς του χωριού κάνει μια μικρή λειτουργία.", "The volunteers work only in the morning and the afternoon, because at midday the lime dries too fast and cracks. Before they start, they always ask the owners' permission. So far they have whitewashed forty-two little churches, and at the end of each job the village priest holds a short service."),
 ],
 "questions": [
  Q("Ποιοι ξεκίνησαν την πρωτοβουλία;", ["Ο δήμος του νησιού", "Δύο συνταξιούχοι δάσκαλοι", "Ο παπάς του χωριού", "Οι ιδιοκτήτες των ξωκλησιών"], 1, "ξεκίνησε πριν από τρία χρόνια από δύο συνταξιούχους δασκάλους"),
  Q("Γιατί δεν δουλεύουν το μεσημέρι;", ["Γιατί κάνει πολλή ζέστη για τους εθελοντές", "Γιατί ο ασβέστης στεγνώνει πολύ γρήγορα και σκάει", "Γιατί τότε γίνεται η λειτουργία", "Γιατί κλείνει το μονοπάτι"], 1, "το μεσημέρι ο ασβέστης στεγνώνει πολύ γρήγορα και σκάει"),
  Q("Τι κάνουν πάντα πριν ξεκινήσουν;", ["Ζητούν την άδεια των ιδιοκτητών", "Πληρώνουν τα υλικά", "Φωτογραφίζουν το ξωκλήσι", "Ενημερώνουν την αστυνομία"], 0, "ζητούν πάντα την άδεια των ιδιοκτητών"),
 ],
 "gloss": {"ξωκλήσι": "ξωκλήσι — country chapel", "ασβέστη": "ασβέστης — lime, whitewash", "κουβάδες": "κουβάς — bucket", "ξεφλουδίζει": "ξεφλουδίζω — to peel", "ασβεστώσει": "ασβεστώνω — to whitewash", "σκάει": "σκάω — to crack, burst"},
})

ITEMS.append({
 "id": "l192-c1-int-ypokoristika", "title": "Γλωσσολόγος για τα υποκοριστικά", "title_en": "A linguist on diminutives", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια ραδιοφωνική συνέντευξη με μια γλωσσολόγο για τη χρήση των υποκοριστικών στα ελληνικά.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι ξένοι που μαθαίνουν ελληνικά παραξενεύονται όταν ακούνε έναν μεγάλο άνδρα να ζητάει «ένα καφεδάκι». Γιατί μιλάμε έτσι;", "Foreigners learning Greek are puzzled when they hear a grown man ask for 'a little coffee'. Why do we talk like that?"),
  L("Γλωσσολόγος", "f", "Γιατί το υποκοριστικό στα ελληνικά δεν δηλώνει σχεδόν ποτέ μόνο το μικρό μέγεθος. Το «καφεδάκι» δεν είναι μικρότερος καφές. Είναι ένας καφές που προσφέρεται ή ζητιέται με οικειότητα, χωρίς πίεση. Λειτουργεί ως μηχανισμός ευγένειας, μαλακώνει το αίτημα, όπως στα αγγλικά θα προσθέτατε ένα «just» ή ένα «please».", "Because the diminutive in Greek hardly ever indicates small size alone. 'Kafedaki' isn't a smaller coffee. It's a coffee offered or requested with familiarity, without pressure. It works as a politeness mechanism, it softens the request, the way in English you'd add a 'just' or a 'please'."),
  L("Δημοσιογράφος", "m", "Δηλαδή έχει πάντα θετική χροιά;", "So it always has a positive tone?"),
  L("Γλωσσολόγος", "f", "Καθόλου. Η ίδια κατάληξη μπορεί να εκφράσει τρυφερότητα, «το παιδάκι μου», αλλά και υποτίμηση. Αν πείτε για κάποιον ότι έχει «ένα μαγαζάκι», ή για μια συνάδελφο ότι έγραψε «ένα αρθράκι», μπορεί να τον μειώνετε. Το νόημα το κρίνουν ο τόνος της φωνής και η σχέση των ομιλητών.", "Not at all. The same ending can express tenderness, 'my little child', but also belittling. If you say of someone that they have 'a little shop', or of a colleague that she wrote 'a little article', you may be diminishing them. The meaning is decided by the tone of voice and the relationship between the speakers."),
  L("Δημοσιογράφος", "m", "Υπάρχει διαφορά ανάμεσα στις καταλήξεις, ας πούμε -άκι, -ίτσα, -ούλης;", "Is there a difference between the endings, say -aki, -itsa, -oulis?"),
  L("Γλωσσολόγος", "f", "Υπάρχουν τάσεις, όχι αυστηροί κανόνες. Το -άκι είναι το πιο παραγωγικό και μπορεί να κολλήσει σχεδόν σε κάθε ουσιαστικό. Το -ούλης, το -ούλα, ακούγονται πιο χαϊδευτικά, τα συναντάμε συχνά στη γλώσσα που απευθύνεται σε μωρά. Υπάρχουν και λέξεις που ξεκίνησαν ως υποκοριστικά και έχασαν αυτή τη σημασία: το «σπίτι» και το «παιδί» προέρχονται από αρχαία υποκοριστικά, αλλά σήμερα κανείς δεν τα νιώθει έτσι.", "There are tendencies, not strict rules. -aki is the most productive and can attach to almost any noun. -oulis and -oula sound more affectionate; we often meet them in language addressed to babies. There are also words that started as diminutives and lost that meaning: 'spiti' and 'paidi' come from ancient diminutives, but nobody feels them that way today."),
 ],
 "questions": [
  Q("Τι λειτουργία έχει, κατά τη γλωσσολόγο, το «καφεδάκι»;", ["Δηλώνει μικρότερη ποσότητα καφέ", "Μαλακώνει το αίτημα, ως μηχανισμός ευγένειας", "Δείχνει ότι ο ομιλητής βιάζεται", "Είναι διαλεκτικός τύπος"], 1, "Λειτουργεί ως μηχανισμός ευγένειας, μαλακώνει το αίτημα"),
  Q("Τι μπορεί να εκφράσει το υποκοριστικό στη φράση «έγραψε ένα αρθράκι»;", ["Θαυμασμό", "Υποτίμηση", "Έκπληξη", "Ακρίβεια"], 1, "μπορεί να τον μειώνετε"),
  Q("Ποιο από τα παρακάτω ισχύει για την κατάληξη -άκι;", ["Χρησιμοποιείται μόνο για μωρά", "Είναι η πιο παραγωγική κατάληξη", "Ακούγεται πάντα υποτιμητικά", "Έχει χαθεί από τη σύγχρονη γλώσσα"], 1, "Το -άκι είναι το πιο παραγωγικό"),
  Q("Τι λέει για τις λέξεις «σπίτι» και «παιδί»;", ["Ότι είναι δάνεια", "Ότι ξεκίνησαν ως υποκοριστικά αλλά έχασαν αυτή τη σημασία", "Ότι έχουν δύο υποκοριστικά", "Ότι δεν έχουν υποκοριστικό"], 1, "προέρχονται από αρχαία υποκοριστικά, αλλά σήμερα κανείς δεν τα νιώθει έτσι"),
 ],
 "gloss": {"υποκοριστικά": "υποκοριστικό — diminutive", "παραξενεύονται": "παραξενεύομαι — to be puzzled", "οικειότητα": "οικειότητα — familiarity", "χροιά": "χροιά — tone, shade (of meaning)", "υποτίμηση": "υποτίμηση — belittling", "παραγωγικό": "παραγωγικός — productive", "χαϊδευτικά": "χαϊδευτικός — affectionate"},
})

ITEMS.append({
 "id": "l192-c1-mono-tholoi-pagakia", "title": "Γιατί τα παγάκια βγαίνουν θολά", "title_en": "Why ice cubes come out cloudy", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια εκπομπή επιστήμης για καθημερινά φαινόμενα.",
 "script": [
  L("Παρουσιαστής", "m", "Αν κοιτάξετε ένα παγάκι από την κατάψυξή σας, θα δείτε ότι είναι διάφανο στις άκρες και θολό, σχεδόν άσπρο, στο κέντρο. Τα κρυστάλλινα παγάκια των μπαρ δεν είναι μαγικά, απλώς έχουν παγώσει με διαφορετικό τρόπο.", "If you look at an ice cube from your freezer, you'll see that it is transparent at the edges and cloudy, almost white, in the centre. The crystal-clear cubes in bars aren't magic, they've simply frozen in a different way."),
  L("Παρουσιαστής", "m", "Το νερό της βρύσης περιέχει διαλυμένο αέρα και μικρές ποσότητες αλάτων. Στη θήκη του πάγου, το νερό παγώνει από έξω προς τα μέσα, από όλες τις πλευρές ταυτόχρονα. Καθώς σχηματίζονται οι κρύσταλλοι, σπρώχνουν τον αέρα και τις προσμείξεις προς το κομμάτι που μένει υγρό, δηλαδή προς το κέντρο. Όταν παγώσει κι αυτό, οι φυσαλίδες εγκλωβίζονται, και αυτές σκεδάζουν το φως.", "Tap water contains dissolved air and small amounts of salts. In the ice tray, the water freezes from the outside in, from all sides at once. As the crystals form, they push the air and the impurities towards the part that stays liquid, that is, towards the centre. When that freezes too, the bubbles are trapped, and they scatter the light."),
  L("Παρουσιαστής", "m", "Συχνά θα ακούσετε ότι αρκεί να βράσετε το νερό πρώτα. Το βράσιμο διώχνει ένα μέρος του αέρα, αλλά οι περισσότερες δοκιμές δείχνουν ότι η βελτίωση είναι μικρή, γιατί το νερό ξαναπαίρνει αέρα καθώς κρυώνει. Το μυστικό είναι η κατευθυνόμενη ψύξη: αν το νερό παγώνει μόνο από πάνω προς τα κάτω, για παράδειγμα σε ένα μονωμένο δοχείο, οι φυσαλίδες μαζεύονται στο κάτω μέρος, που το κόβετε και το πετάτε. Έτσι φτιάχνουν τον διάφανο πάγο οι επαγγελματίες.", "You'll often hear that it's enough to boil the water first. Boiling drives out some of the air, but most tests show the improvement is small, because the water takes up air again as it cools. The secret is directional freezing: if the water freezes only from the top down, for example in an insulated container, the bubbles collect at the bottom, which you cut off and throw away. That's how professionals make clear ice."),
 ],
 "questions": [
  Q("Γιατί το θολό μέρος βρίσκεται στο κέντρο του παγακιού;", ["Γιατί εκεί το νερό είναι πιο κρύο", "Γιατί οι κρύσταλλοι σπρώχνουν τον αέρα και τις προσμείξεις προς το μέρος που μένει υγρό", "Γιατί η κατάψυξη δεν κλείνει καλά", "Γιατί το κέντρο παγώνει πρώτο"], 1, "σπρώχνουν τον αέρα και τις προσμείξεις προς το κομμάτι που μένει υγρό, δηλαδή προς το κέντρο"),
  Q("Τι προκαλεί τη θολή εμφάνιση;", ["Τα άλατα που αλλάζουν χρώμα", "Οι εγκλωβισμένες φυσαλίδες που σκεδάζουν το φως", "Η πολύ χαμηλή θερμοκρασία", "Το πλαστικό της θήκης"], 1, "οι φυσαλίδες εγκλωβίζονται, και αυτές σκεδάζουν το φως"),
  Q("Τι λέει ο παρουσιαστής για το βράσιμο του νερού;", ["Ότι λύνει εντελώς το πρόβλημα", "Ότι κάνει τον πάγο πιο θολό", "Ότι βοηθά λίγο, γιατί το νερό ξαναπαίρνει αέρα καθώς κρυώνει", "Ότι είναι επικίνδυνο"], 2, "η βελτίωση είναι μικρή, γιατί το νερό ξαναπαίρνει αέρα καθώς κρυώνει"),
  Q("Πώς φτιάχνουν οι επαγγελματίες διάφανο πάγο;", ["Με απεσταγμένο νερό μόνο", "Παγώνοντας το νερό πολύ γρήγορα", "Με κατευθυνόμενη ψύξη από πάνω προς τα κάτω και κόβοντας το κάτω μέρος", "Προσθέτοντας αλάτι"], 2, "οι φυσαλίδες μαζεύονται στο κάτω μέρος, που το κόβετε και το πετάτε"),
 ],
 "gloss": {"διάφανο": "διάφανος — transparent", "διαλυμένο": "διαλυμένος — dissolved", "προσμείξεις": "πρόσμειξη — impurity", "φυσαλίδες": "φυσαλίδα — bubble", "εγκλωβίζονται": "εγκλωβίζομαι — to be trapped", "σκεδάζουν": "σκεδάζω — to scatter", "κατευθυνόμενη": "κατευθυνόμενος — directed, directional"},
})

ITEMS.append({
 "id": "l192-rep-plosto-sinema-limni", "title": "Θερινό σινεμά πάνω στη λίμνη", "title_en": "A summer cinema on the lake", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για μια καλοκαιρινή εκδήλωση σε μια πόλη της Βόρειας Ελλάδας.",
 "script": [
  L("Ρεπόρτερ", "m", "Τα θερινά σινεμά τα ξέρουμε όλοι: καρέκλες σε μια αυλή, γιασεμί και ο θόρυβος από τα μηχανάκια. Φέτος όμως μια πολιτιστική ομάδα στην Καστοριά πήγε την ιδέα ένα βήμα παραπέρα και έστησε την οθόνη πάνω σε μια πλωτή εξέδρα στη λίμνη.", "We all know open-air summer cinemas: chairs in a courtyard, jasmine and the noise of the scooters. This year, though, a cultural group in Kastoria took the idea a step further and set up the screen on a floating platform on the lake."),
  L("Ρεπόρτερ", "m", "Οι θεατές παρακολουθούν από βάρκες, που τις νοικιάζουν στην προκυμαία, ή από ξαπλώστρες στην όχθη. Ο ήχος δεν βγαίνει από μεγάφωνα, για να μην ενοχλούνται οι κάτοικοι και τα πουλιά της λίμνης, αλλά μεταδίδεται σε μια συχνότητα του ραδιοφώνου, και ο καθένας τον ακούει από το κινητό του με ακουστικά.", "Viewers watch from boats, which they rent on the waterfront, or from sun loungers on the shore. The sound doesn't come out of loudspeakers, so as not to disturb the residents and the birds of the lake, but is broadcast on a radio frequency, and everyone listens on their mobile with headphones."),
  L("Ρεπόρτερ", "m", "Οι διοργανωτές είχαν μόνο ένα πρόβλημα: τα κουνούπια. Τη δεύτερη βραδιά μοίρασαν δωρεάν εντομοαπωθητικό, και από τότε, όπως λένε, δεν έχει παραπονεθεί κανείς. Οι προβολές γίνονται κάθε Παρασκευή και Σάββατο ως το τέλος Αυγούστου, και αν φυσάει πολύ, αναβάλλονται για την επόμενη μέρα.", "The organisers had just one problem: the mosquitoes. On the second night they handed out free insect repellent, and since then, they say, no one has complained. Screenings take place every Friday and Saturday until the end of August, and if it's very windy, they are postponed to the next day."),
 ],
 "questions": [
  Q("Πού βρίσκεται η οθόνη;", ["Σε μια αυλή", "Πάνω σε πλωτή εξέδρα στη λίμνη", "Στην προκυμαία", "Σε ένα πλοίο"], 1, "έστησε την οθόνη πάνω σε μια πλωτή εξέδρα στη λίμνη"),
  Q("Γιατί δεν χρησιμοποιούν μεγάφωνα;", ["Γιατί είναι πολύ ακριβά", "Για να μην ενοχλούνται οι κάτοικοι και τα πουλιά", "Γιατί χάλασαν", "Γιατί απαγορεύονται στη λίμνη"], 1, "για να μην ενοχλούνται οι κάτοικοι και τα πουλιά της λίμνης"),
  Q("Πώς έλυσαν το πρόβλημα με τα κουνούπια;", ["Μετέφεραν τις προβολές", "Μοίρασαν δωρεάν εντομοαπωθητικό", "Έκλεισαν τα φώτα", "Ψέκασαν τη λίμνη"], 1, "μοίρασαν δωρεάν εντομοαπωθητικό"),
 ],
 "gloss": {"πλωτή": "πλωτός — floating", "εξέδρα": "εξέδρα — platform", "προκυμαία": "προκυμαία — waterfront, quay", "όχθη": "όχθη — shore, bank", "μεγάφωνα": "μεγάφωνο — loudspeaker", "εντομοαπωθητικό": "εντομοαπωθητικό — insect repellent", "αναβάλλονται": "αναβάλλομαι — to be postponed"},
})

rnd = random.Random(192)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-192.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
