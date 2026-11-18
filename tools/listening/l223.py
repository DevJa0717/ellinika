# Source for library/listening/listening-223.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l223.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l223-news-tilefonikes-apates", "title": "Μαθήματα για να μην πέφτουν θύματα τηλεφωνικής απάτης", "title_en": "Classes so that older people don't fall for phone scams", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο ραδιόφωνο για σεμινάρια που οργανώνει ένας δήμος για ηλικιωμένους.",
 "script": [
  L("Εκφωνητής", "m", "Με σεμινάρια στα κέντρα ηλικιωμένων ένας δήμος της Θεσσαλονίκης προσπαθεί να προστατέψει τους μεγαλύτερους κατοίκους από τις τηλεφωνικές απάτες, που τον τελευταίο χρόνο έχουν αυξηθεί. Τα μαθήματα γίνονται σε συνεργασία με την αστυνομία και είναι δωρεάν.", "With seminars at senior centres, a Thessaloniki municipality is trying to protect older residents from phone scams, which have increased over the past year. The classes are run in cooperation with the police and are free."),
  L("Εκφωνητής", "m", "Οι αστυνομικοί εξηγούν τα πιο συνηθισμένα σενάρια. Στο πιο γνωστό, κάποιος τηλεφωνεί και λέει ότι ένα παιδί ή ένα εγγόνι είχε ατύχημα και χρειάζεται αμέσως χρήματα για το νοσοκομείο. Σε άλλα, ο απατεώνας παριστάνει τον υπάλληλο της τράπεζας και ζητά τους κωδικούς της κάρτας.", "The police officers explain the most common scenarios. In the best known, someone phones and says that a child or grandchild has had an accident and needs money immediately for the hospital. In others, the fraudster pretends to be a bank employee and asks for the card's codes."),
  L("Εκφωνητής", "m", "Ο βασικός κανόνας, λένε, είναι απλός: κλείστε το τηλέφωνο και καλέστε εσείς τον συγγενή σας ή την τράπεζα στον αριθμό που ήδη γνωρίζετε. Καμία τράπεζα δεν ζητά κωδικούς τηλεφωνικά, και κανένα νοσοκομείο δεν στέλνει κάποιον στο σπίτι για να πάρει μετρητά. Οι συμμετέχοντες κάνουν και πρόβες, με εθελοντές που παίζουν τον ρόλο του απατεώνα.", "The basic rule, they say, is simple: hang up and call your relative or the bank yourself on the number you already know. No bank asks for codes over the phone, and no hospital sends someone to your home to collect cash. Participants also do rehearsals, with volunteers playing the role of the fraudster."),
 ],
 "questions": [
  Q("Με ποιον συνεργάζεται ο δήμος για τα μαθήματα;", ["Με τις τράπεζες", "Με την αστυνομία", "Με ένα νοσοκομείο", "Με μια εταιρεία κινητής τηλεφωνίας"], 1, "Τα μαθήματα γίνονται σε συνεργασία με την αστυνομία"),
  Q("Τι λέει ο απατεώνας στο πιο γνωστό σενάριο;", ["Ότι κέρδισαν ένα δώρο", "Ότι ένα παιδί ή εγγόνι είχε ατύχημα και χρειάζεται χρήματα", "Ότι πρέπει να πληρώσουν έναν λογαριασμό", "Ότι η σύνταξή τους θα κοπεί"], 1, "ένα παιδί ή ένα εγγόνι είχε ατύχημα και χρειάζεται αμέσως χρήματα για το νοσοκομείο"),
  Q("Ποιος είναι ο βασικός κανόνας;", ["Να μην απαντούν ποτέ στο τηλέφωνο", "Να κλείνουν και να καλούν οι ίδιοι στον αριθμό που ήδη γνωρίζουν", "Να ζητούν το όνομα του απατεώνα", "Να δίνουν μόνο μέρος των χρημάτων"], 1, "κλείστε το τηλέφωνο και καλέστε εσείς τον συγγενή σας ή την τράπεζα στον αριθμό που ήδη γνωρίζετε"),
  Q("Τι κάνουν οι συμμετέχοντες στις πρόβες;", ["Γράφουν τεστ", "Εξασκούνται με εθελοντές που παίζουν τον απατεώνα", "Επισκέπτονται την τράπεζα", "Μαθαίνουν να χρησιμοποιούν εφαρμογές"], 1, "με εθελοντές που παίζουν τον ρόλο του απατεώνα"),
 ],
 "gloss": {"σεμινάρια": "σεμινάριο — seminar, workshop", "απάτες": "απάτη — fraud, scam", "σενάρια": "σενάριο — scenario; script", "απατεώνας": "απατεώνας — fraudster, con man", "παριστάνει": "παριστάνω — to pretend to be", "κωδικούς": "κωδικός — code, PIN", "μετρητά": "μετρητά — cash", "πρόβες": "πρόβα — rehearsal"},
})
ITEMS.append({
 "id": "l223-vm-xylourgos-vivliothiki", "title": "Μήνυμα από τον ξυλουργό για τη βιβλιοθήκη", "title_en": "Message from the carpenter about the bookcase", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον ξυλουργό που φτιάχνει μια βιβλιοθήκη για το σαλόνι σας.",
 "script": [
  L("Ξυλουργός", "m", "Καλημέρα σας, κυρία Ζαχαρίου, ο Παύλος είμαι, ο ξυλουργός, για τη βιβλιοθήκη του σαλονιού. Σας παίρνω για τρία πράγματα, και συγγνώμη που το μήνυμα θα είναι λίγο μεγάλο.", "Good morning, Ms Zachariou, it's Pavlos, the carpenter, about the living-room bookcase. I'm calling about three things, and sorry that the message will be a bit long."),
  L("Ξυλουργός", "m", "Πρώτον, η καρυδιά που είχαμε διαλέξει άργησε από τον προμηθευτή και θα έρθει σε δύο εβδομάδες. Αν βιάζεστε, μπορώ να τη φτιάξω από δρυ, που την έχω ήδη στο εργαστήριο· είναι λίγο πιο ανοιχτόχρωμη, αλλά εξίσου γερή, και θα σας κοστίσει περίπου εκατό ευρώ λιγότερο.", "First, the walnut we had chosen was delayed by the supplier and will arrive in two weeks. If you're in a hurry, I can make it from oak, which I already have in the workshop; it's a little lighter in colour but just as sturdy, and it will cost you about a hundred euros less."),
  L("Ξυλουργός", "m", "Δεύτερον, ξαναείδα τις μετρήσεις και νομίζω ότι το καλοριφέρ κάτω από το παράθυρο θα μας χαλάσει το τελευταίο ράφι. Προτείνω να κάνουμε εκεί ένα πιο κοντό κομμάτι, για να μη στεγνώνουν τα βιβλία από τη ζέστη.", "Second, I looked at the measurements again and I think the radiator under the window will spoil the last shelf for us. I suggest we make a shorter section there, so the books don't dry out from the heat."),
  L("Ξυλουργός", "m", "Και τρίτον, για το βερνίκι: ματ ή γυαλιστερό; Εγώ θα σας πρότεινα ματ, γιατί δεν φαίνονται τόσο τα δαχτυλιά. Πάρτε με όποτε μπορείτε, μέχρι την Παρασκευή αν γίνεται, για να ξέρω τι να παραγγείλω. Ευχαριστώ!", "And third, about the varnish: matt or glossy? I'd suggest matt, because fingerprints don't show as much. Call me whenever you can, by Friday if possible, so I know what to order. Thanks!"),
 ],
 "questions": [
  Q("Γιατί καθυστερεί η καρυδιά;", ["Γιατί ο ξυλουργός είναι άρρωστος", "Γιατί άργησε από τον προμηθευτή", "Γιατί είναι πολύ ακριβή", "Γιατί δεν βρίσκεται πια στην αγορά"], 1, "η καρυδιά ... άργησε από τον προμηθευτή"),
  Q("Ποια λύση προτείνει αν η πελάτισσα βιάζεται;", ["Να αγοράσει μια έτοιμη βιβλιοθήκη", "Να τη φτιάξει από δρυ, που είναι φθηνότερη", "Να περιμένει έναν μήνα", "Να τη φτιάξει από πεύκο"], 1, "μπορώ να τη φτιάξω από δρυ ... θα σας κοστίσει περίπου εκατό ευρώ λιγότερο"),
  Q("Τι πρόβλημα δημιουργεί το καλοριφέρ;", ["Δεν χωράει η βιβλιοθήκη στον τοίχο", "Θα χαλάσει το τελευταίο ράφι και θα στεγνώνουν τα βιβλία", "Θα πρέπει να μετακινηθεί", "Θα κάψει το βερνίκι"], 1, "το καλοριφέρ ... θα μας χαλάσει το τελευταίο ράφι ... για να μη στεγνώνουν τα βιβλία"),
  Q("Γιατί προτείνει ματ βερνίκι;", ["Γιατί στεγνώνει πιο γρήγορα", "Γιατί είναι πιο φθηνό", "Γιατί δεν φαίνονται τόσο τα δαχτυλιά", "Γιατί είναι πιο μοντέρνο"], 2, "γιατί δεν φαίνονται τόσο τα δαχτυλιά"),
 ],
 "gloss": {"ξυλουργός": "ξυλουργός — carpenter", "καρυδιά": "καρυδιά — walnut (tree, wood)", "προμηθευτή": "προμηθευτής — supplier", "δρυ": "δρυς — oak", "ανοιχτόχρωμη": "ανοιχτόχρωμος — light-coloured", "γερή": "γερός — sturdy, strong", "καλοριφέρ": "καλοριφέρ — radiator", "βερνίκι": "βερνίκι — varnish", "δαχτυλιά": "δαχτυλιά — fingerprint, smudge"},
})
ITEMS.append({
 "id": "l223-c1-mono-meltemi", "title": "Το μελτέμι: πώς γεννιέται ο άνεμος του Αιγαίου", "title_en": "The meltemi: how the Aegean wind is born", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για τον καιρό και το κλίμα της Ελλάδας.",
 "script": [
  L("Ομιλήτρια", "f", "Όποιος έχει ταξιδέψει στις Κυκλάδες τον Αύγουστο ξέρει το μελτέμι: τον δυνατό βοριά που κάνει τα πλοία να χορεύουν, ξεριζώνει τις ομπρέλες της παραλίας και, μερικές φορές, ακυρώνει τα δρομολόγια. Είναι ένας από τους πιο σταθερούς ανέμους της Μεσογείου: επιστρέφει κάθε καλοκαίρι, με αποκορύφωμα τον Ιούλιο και τον Αύγουστο.", "Anyone who has travelled to the Cyclades in August knows the meltemi: the strong north wind that makes ships dance, uproots beach umbrellas and sometimes cancels sailings. It is one of the most regular winds of the Mediterranean: it returns every summer, peaking in July and August."),
  L("Ομιλήτρια", "f", "Από πού προέρχεται; Το καλοκαίρι, πάνω από τα Βαλκάνια επικρατούν συχνά υψηλές πιέσεις, ενώ πάνω από την Τουρκία και τη Μέση Ανατολή σχηματίζεται ένα εκτεταμένο θερμικό χαμηλό. Ο αέρας κινείται από την υψηλή προς τη χαμηλή πίεση, και το Αιγαίο, ανάμεσα στα βουνά της Ελλάδας και της Μικράς Ασίας, λειτουργεί σαν διάδρομος που τον επιταχύνει. Γι’ αυτό το μελτέμι φυσά πιο δυνατά στα στενά ανάμεσα στα νησιά.", "Where does it come from? In summer, high pressure often prevails over the Balkans, while an extensive thermal low forms over Turkey and the Middle East. Air moves from high to low pressure, and the Aegean, between the mountains of Greece and Asia Minor, acts as a corridor that accelerates it. That is why the meltemi blows harder in the straits between the islands."),
  L("Ομιλήτρια", "f", "Συνήθως δυναμώνει το απόγευμα και εξασθενεί τη νύχτα, και μπορεί να κρατήσει από μία μέρα μέχρι και μια ολόκληρη εβδομάδα. Για τους ναυτικούς είναι εχθρός, για τους ιστιοσανιδιστές παράδεισος. Δεν είναι τυχαίο ότι οι παλιοί ανεμόμυλοι των Κυκλάδων κοιτάζουν συνήθως προς τον βορρά.", "It usually strengthens in the afternoon and weakens at night, and can last from one day to a whole week. For sailors it is an enemy, for windsurfers a paradise. It is no coincidence that the old windmills of the Cyclades usually face north."),
  L("Ομιλήτρια", "f", "Το μελτέμι έχει όμως και μια σκοτεινή πλευρά. Ο ξηρός, δυνατός άνεμος μπορεί να μετατρέψει μια μικρή φωτιά σε καταστροφή μέσα σε λίγες ώρες. Και την ίδια στιγμή, είναι αυτό που κάνει το Αιγαίο υποφερτό στη μέση του καλοκαιριού. Χωρίς το μελτέμι, πολλά νησιά θα ήταν σχεδόν αφόρητα τον Αύγουστο.", "But the meltemi also has a dark side. The dry, strong wind can turn a small fire into a disaster within a few hours. And at the same time, it is what makes the Aegean bearable in the middle of summer. Without the meltemi, many islands would be almost unbearable in August."),
 ],
 "questions": [
  Q("Πότε φυσά κυρίως το μελτέμι;", ["Τον χειμώνα", "Το καλοκαίρι, με αποκορύφωμα τον Ιούλιο και τον Αύγουστο", "Την άνοιξη", "Όλο τον χρόνο εξίσου"], 1, "επιστρέφει κάθε καλοκαίρι, με αποκορύφωμα τον Ιούλιο και τον Αύγουστο"),
  Q("Ποιος είναι ο ρόλος του Αιγαίου στη δημιουργία του μελτεμιού;", ["Ζεσταίνει τον αέρα", "Λειτουργεί σαν διάδρομος που επιταχύνει τον άνεμο", "Σταματά τον άνεμο", "Δημιουργεί τις υψηλές πιέσεις"], 1, "το Αιγαίο ... λειτουργεί σαν διάδρομος που τον επιταχύνει"),
  Q("Πότε συνήθως δυναμώνει το μελτέμι;", ["Το πρωί", "Το απόγευμα", "Τα μεσάνυχτα", "Μόνο όταν βρέχει"], 1, "Συνήθως δυναμώνει το απόγευμα και εξασθενεί τη νύχτα"),
  Q("Ποια είναι η «σκοτεινή πλευρά» του μελτεμιού;", ["Φέρνει καταιγίδες", "Μπορεί να μετατρέψει μια μικρή φωτιά σε καταστροφή", "Ανεβάζει τη θερμοκρασία", "Μολύνει τη θάλασσα"], 1, "μπορεί να μετατρέψει μια μικρή φωτιά σε καταστροφή μέσα σε λίγες ώρες"),
 ],
 "gloss": {"βοριά": "βοριάς — north wind", "ξεριζώνει": "ξεριζώνω — to uproot", "αποκορύφωμα": "αποκορύφωμα — peak, climax", "επικρατούν": "επικρατώ — to prevail", "θερμικό χαμηλό": "θερμικό χαμηλό — thermal low (pressure)", "επιταχύνει": "επιταχύνω — to accelerate", "εξασθενεί": "εξασθενώ — to weaken", "ιστιοσανιδιστές": "ιστιοσανιδιστής — windsurfer", "υποφερτό": "υποφερτός — bearable", "αφόρητα": "αφόρητος — unbearable"},
})
ITEMS.append({
 "id": "l223-c1-int-foustanela", "title": "Μια ιστορικός της ενδυμασίας για τη φουστανέλα", "title_en": "A costume historian on the fustanella", "type": "interview", "level": "C1",
 "context_el": "Μια ιστορικός της ενδυμασίας μιλά σε μια ραδιοφωνική εκπομπή για την ιστορία της φουστανέλας.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Βλάχου, για πολλούς ξένους η φουστανέλα είναι «η ελληνική φούστα» των ευζώνων. Από πού ξεκινά πραγματικά;", "Ms Vlachou, for many foreigners the fustanella is the 'Greek skirt' of the evzones. Where does it really begin?"),
  L("Βλάχου", "f", "Η αλήθεια είναι ότι δεν ήταν ποτέ αποκλειστικά ελληνική. Τη φορούσαν σε μεγάλο μέρος των Βαλκανίων, Έλληνες, Αλβανοί, Βλάχοι, ιδιαίτερα στις ορεινές περιοχές. Κάποιοι μελετητές τη συνδέουν με πολύ παλαιότερα ενδύματα, αλλά μια συνεχής γραμμή από την αρχαιότητα είναι δύσκολο να αποδειχτεί. Στην Ελλάδα έγινε σύμβολο γιατί τη φορούσαν οι κλέφτες, οι αρματολοί και πολλοί αγωνιστές του Εικοσιένα.", "The truth is that it was never exclusively Greek. It was worn across much of the Balkans, by Greeks, Albanians, Vlachs, especially in mountain areas. Some scholars link it with much older garments, but a continuous line from antiquity is hard to prove. In Greece it became a symbol because it was worn by the klephts, the armatoloi and many fighters of 1821."),
  L("Δημοσιογράφος", "m", "Και πώς έγινε επίσημη ενδυμασία;", "And how did it become official dress?"),
  L("Βλάχου", "f", "Ο Όθωνας, ο πρώτος βασιλιάς της Ελλάδας, έκανε μια συμβολική κίνηση: φορούσε ο ίδιος φουστανέλα σε επίσημες περιστάσεις, για να δείξει ότι ταυτίζεται με τον λαό που κυβερνούσε. Έτσι, η φουστανέλα έγινε κάτι σαν «εθνική ενδυμασία» των ανδρών, ενώ την ίδια εποχή οι κάτοικοι των πόλεων ντύνονταν όλο και περισσότερο «φράγκικα», δηλαδή με ευρωπαϊκά ρούχα. Υπήρχε μια παράξενη ένταση: το έθνος έβλεπε τον εαυτό του στη φουστανέλα, αλλά η αστική τάξη την έβγαζε από την ντουλάπα μόνο στις γιορτές.", "Otto, the first king of Greece, made a symbolic gesture: he himself wore the fustanella on official occasions, to show that he identified with the people he ruled. So the fustanella became something like the men's 'national costume', while at the same time city dwellers increasingly dressed 'in the Frankish way', that is, in European clothes. There was a strange tension: the nation saw itself in the fustanella, but the middle class took it out of the wardrobe only on holidays."),
  L("Δημοσιογράφος", "m", "Ακούμε συχνά ότι οι πιέτες της φουστανέλας των ευζώνων είναι τετρακόσιες, όσα και τα χρόνια της Τουρκοκρατίας. Ισχύει;", "We often hear that the pleats of the evzones' fustanella number four hundred, as many as the years of Ottoman rule. Is that true?"),
  L("Βλάχου", "f", "Είναι μια όμορφη ιστορία που λέγεται πολύ, αλλά εγώ θα την έλεγα περισσότερο ερμηνεία παρά ιστορικό γεγονός. Οι πιέτες είναι πράγματι πάρα πολλές, και ο συμβολισμός αυτός ταιριάζει στη στολή μιας τιμητικής φρουράς. Αυτό που με ενδιαφέρει εμένα είναι κάτι άλλο: ότι ένα ρούχο των βουνών έγινε, μέσα σε λίγες δεκαετίες, εικόνα ενός ολόκληρου κράτους.", "It's a lovely story that is told a lot, but I would call it more an interpretation than a historical fact. The pleats are indeed very many, and that symbolism suits the uniform of an honour guard. What interests me is something else: that a garment of the mountains became, within a few decades, the image of a whole state."),
 ],
 "questions": [
  Q("Τι λέει η κ. Βλάχου για την προέλευση της φουστανέλας;", ["Ότι είναι αποκλειστικά ελληνική", "Ότι τη φορούσαν σε μεγάλο μέρος των Βαλκανίων, όχι μόνο οι Έλληνες", "Ότι την έφερε ο Όθωνας από τη Βαυαρία", "Ότι είναι ρωμαϊκή στολή"], 1, "δεν ήταν ποτέ αποκλειστικά ελληνική. Τη φορούσαν σε μεγάλο μέρος των Βαλκανίων"),
  Q("Γιατί έγινε σύμβολο στην Ελλάδα;", ["Γιατί ήταν φθηνή", "Γιατί τη φορούσαν οι κλέφτες, οι αρματολοί και αγωνιστές του Εικοσιένα", "Γιατί την επέβαλε η Εκκλησία", "Γιατί ήταν της μόδας στην Ευρώπη"], 1, "τη φορούσαν οι κλέφτες, οι αρματολοί και πολλοί αγωνιστές του Εικοσιένα"),
  Q("Τι έκανε ο Όθωνας;", ["Απαγόρευσε τη φουστανέλα", "Φορούσε ο ίδιος φουστανέλα σε επίσημες περιστάσεις", "Έφτιαξε εργοστάσιο φουστανέλας", "Την έκανε στολή των σχολείων"], 1, "φορούσε ο ίδιος φουστανέλα σε επίσημες περιστάσεις"),
  Q("Πώς κρίνει την ιστορία με τις τετρακόσιες πιέτες;", ["Ως αποδεδειγμένο ιστορικό γεγονός", "Περισσότερο ως ερμηνεία παρά ως ιστορικό γεγονός", "Ως εντελώς ψεύτικη και ενοχλητική", "Δεν την έχει ακούσει ποτέ"], 1, "θα την έλεγα περισσότερο ερμηνεία παρά ιστορικό γεγονός"),
 ],
 "gloss": {"ευζώνων": "εύζωνας — evzone (Presidential Guard soldier)", "αποκλειστικά": "αποκλειστικά — exclusively", "ενδύματα": "ένδυμα — garment", "κλέφτες": "κλέφτης — klepht (mountain fighter); thief", "αρματολοί": "αρματολός — armatolos (Christian militiaman under Ottoman rule)", "ταυτίζεται": "ταυτίζομαι — to identify (with)", "φράγκικα": "φράγκικα — in Western/European style (old)", "ένταση": "ένταση — tension", "πιέτες": "πιέτα — pleat", "τιμητικής φρουράς": "τιμητική φρουρά — honour guard"},
})

rnd = random.Random(223)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-223.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
