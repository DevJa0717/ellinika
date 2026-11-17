# Source for library/listening/listening-126.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l126.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l126-ann-bowling", "title": "Τουρνουά μπόουλινγκ για καλό σκοπό", "title_en": "A bowling tournament for a good cause", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα εμπορικό κέντρο. Ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί επισκέπτες, την Κυριακή στις πέντε το απόγευμα το κέντρο μπόουλινγκ του δεύτερου ορόφου διοργανώνει φιλανθρωπικό τουρνουά. Όλα τα έσοδα θα διατεθούν στον σύλλογο γονέων παιδιών με διαβήτη, για την αγορά αισθητήρων γλυκόζης.", "Dear visitors, on Sunday at five in the afternoon the bowling centre on the second floor is organising a charity tournament. All proceeds will go to the association of parents of children with diabetes, to buy glucose sensors."),
  L("Εκφωνητής", "m", "Μπορούν να συμμετάσχουν ομάδες των τεσσάρων ατόμων, ακόμη και αρχάριοι, αφού οι κανόνες θα εξηγηθούν πριν από την έναρξη. Η συμμετοχή κοστίζει σαράντα ευρώ ανά ομάδα και περιλαμβάνει την ενοικίαση παπουτσιών και ένα αναψυκτικό για κάθε παίκτη.", "Teams of four can take part, even beginners, since the rules will be explained before the start. Entry costs forty euros per team and includes shoe hire and a soft drink for each player."),
  L("Εκφωνητής", "m", "Η ομάδα με τους περισσότερους πόντους θα κερδίσει ένα δείπνο για τέσσερις στο εστιατόριο του τελευταίου ορόφου. Δηλώσεις συμμετοχής γίνονται στο ταμείο του μπόουλινγκ μέχρι το Σάββατο το βράδυ, ή μέχρι να καλυφθούν οι δεκαέξι διάδρομοι.", "The team with the most points will win dinner for four at the restaurant on the top floor. Entries are taken at the bowling desk until Saturday evening, or until the sixteen lanes are filled."),
 ],
 "questions": [
  Q("Πού θα πάνε τα έσοδα του τουρνουά;", ["Σε ένα νοσοκομείο", "Στον σύλλογο γονέων παιδιών με διαβήτη", "Σε ένα αθλητικό σωματείο", "Σε ένα καταφύγιο ζώων"], 1, "Όλα τα έσοδα θα διατεθούν στον σύλλογο γονέων παιδιών με διαβήτη"),
  Q("Τι περιλαμβάνει η συμμετοχή;", ["Ένα δείπνο για όλους", "Μαθήματα μπόουλινγκ", "Ενοικίαση παπουτσιών και ένα αναψυκτικό για κάθε παίκτη", "Ένα μπλουζάκι του τουρνουά"], 2, "περιλαμβάνει την ενοικίαση παπουτσιών και ένα αναψυκτικό για κάθε παίκτη"),
  Q("Μέχρι πότε γίνονται οι δηλώσεις;", ["Μέχρι το Σάββατο το βράδυ ή μέχρι να καλυφθούν οι διάδρομοι", "Μέχρι την Κυριακή το πρωί", "Μέχρι την Παρασκευή", "Λίγο πριν από την έναρξη"], 0, "μέχρι το Σάββατο το βράδυ, ή μέχρι να καλυφθούν οι δεκαέξι διάδρομοι"),
 ],
 "gloss": {"εμπορικό κέντρο": "εμπορικό κέντρο — shopping centre", "μπόουλινγκ": "μπόουλινγκ — bowling", "ορόφου": "όροφος — floor, storey", "φιλανθρωπικό": "φιλανθρωπικός — charity (adj.)", "έσοδα": "έσοδα — proceeds, takings", "διαβήτη": "διαβήτης — diabetes", "αισθητήρων": "αισθητήρας — sensor", "γλυκόζης": "γλυκόζη — glucose", "αρχάριοι": "αρχάριος — beginner", "έναρξη": "έναρξη — start", "ενοικίαση": "ενοικίαση — hire, rental", "αναψυκτικό": "αναψυκτικό — soft drink", "διάδρομοι": "διάδρομος — lane"}
})

ITEMS.append({
 "id": "l126-vm-tai-tsi", "title": "Μήνυμα από τη δασκάλα του τάι τσι", "title_en": "A message from the tai chi teacher", "type": "voicemail", "level": "B2",
 "context_el": "Κάνετε τάι τσι σε ένα πάρκο με μια ομάδα. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Δασκάλα", "f", "Καλημέρα, η Ευγενία είμαι, από το τάι τσι στο πάρκο. Επειδή η πρόγνωση δίνει βροχές και κρύο για όλη την εβδομάδα, από την Τρίτη τα μαθήματα θα γίνονται στην αίθουσα του πολιτιστικού κέντρου, πίσω από τη βιβλιοθήκη. Η ώρα μένει η ίδια, οκτώ το πρωί.", "Good morning, it's Evgenia, from tai chi in the park. Because the forecast says rain and cold for the whole week, from Tuesday the lessons will take place in the hall of the cultural centre, behind the library. The time stays the same, eight in the morning."),
  L("Δασκάλα", "f", "Η αίθουσα έχει ξύλινο πάτωμα, οπότε φέρτε κάλτσες ή μαλακά παπούτσια, όχι τα παπούτσια που φοράτε στον δρόμο. Επίσης, το πολιτιστικό κέντρο ζητά να είμαστε έξω μέχρι τις εννιά, γιατί μετά έχει μάθημα ζωγραφικής, γι' αυτό θα τελειώνουμε δέκα λεπτά νωρίτερα.", "The hall has a wooden floor, so bring socks or soft shoes, not the shoes you wear in the street. Also, the cultural centre asks us to be out by nine, because there's a painting class after us, so we'll finish ten minutes earlier."),
  L("Δασκάλα", "f", "Μόλις ο καιρός φτιάξει, γυρίζουμε στο πάρκο, θα σας ενημερώσω με μήνυμα. Και μην ξεχάσετε ότι την άλλη Κυριακή κάνουμε την επίδειξη στη γιορτή του δήμου. Τα λέμε!", "As soon as the weather improves, we'll go back to the park; I'll let you know by text. And don't forget that next Sunday we're doing the demonstration at the municipal festival. See you!"),
 ],
 "questions": [
  Q("Γιατί αλλάζει ο χώρος των μαθημάτων;", ["Γιατί το πάρκο κλείνει για εργασίες", "Επειδή η πρόγνωση δίνει βροχές και κρύο", "Γιατί η ομάδα μεγάλωσε", "Γιατί η δασκάλα μετακόμισε"], 1, "Επειδή η πρόγνωση δίνει βροχές και κρύο για όλη την εβδομάδα"),
  Q("Τι πρέπει να φέρουν οι μαθητές;", ["Ένα στρώμα γυμναστικής", "Νερό και πετσέτα", "Κάλτσες ή μαλακά παπούτσια", "Ένα ζεστό μπουφάν"], 2, "φέρτε κάλτσες ή μαλακά παπούτσια"),
  Q("Γιατί θα τελειώνουν δέκα λεπτά νωρίτερα;", ["Γιατί μετά έχει μάθημα ζωγραφικής στην αίθουσα", "Γιατί η δασκάλα έχει άλλη δουλειά", "Γιατί η αίθουσα είναι κρύα", "Γιατί κλείνει η βιβλιοθήκη"], 0, "μετά έχει μάθημα ζωγραφικής"),
 ],
 "gloss": {"τάι τσι": "τάι τσι — tai chi", "πρόγνωση": "πρόγνωση — (weather) forecast", "πολιτιστικού κέντρου": "πολιτιστικό κέντρο — cultural centre", "πάτωμα": "πάτωμα — floor", "κάλτσες": "κάλτσα — sock", "μαλακά": "μαλακός — soft", "φτιάξει": "φτιάχνει ο καιρός — the weather improves", "ενημερώσω": "ενημερώνω — to inform", "επίδειξη": "επίδειξη — demonstration", "γιορτή του δήμου": "γιορτή του δήμου — municipal festival"}
})

ITEMS.append({
 "id": "l126-dial-podosfairo-perpatontas", "title": "Ποδόσφαιρο περπατώντας για τον μπαμπά;", "title_en": "Walking football for Dad?", "type": "dialogue", "level": "B2",
 "context_el": "Η Νεφέλη μιλάει με τον αδερφό της, τον Μάριο, για τον πατέρα τους, που βγήκε πρόσφατα στη σύνταξη.",
 "script": [
  L("Νεφέλη", "f", "Μάριε, ανησυχώ για τον μπαμπά. Από τότε που βγήκε στη σύνταξη, κάθεται όλη μέρα στον καναπέ και βλέπει ειδήσεις. Διάβασα ότι ένας σύλλογος στη γειτονιά του κάνει «ποδόσφαιρο περπατώντας» για άντρες άνω των εξήντα. Δεν τρέχει κανείς, και απαγορεύονται τα μαρκαρίσματα.", "Marios, I'm worried about Dad. Since he retired, he sits on the sofa all day watching the news. I read that a club in his neighbourhood does 'walking football' for men over sixty. Nobody runs, and tackles are not allowed."),
  L("Μάριος", "m", "Ο μπαμπάς; Μετά την εγχείρηση στο γόνατο, ο γιατρός του είπε να προσέχει. Και ξέρεις πόσο πεισματάρης είναι· αν του το προτείνουμε εμείς, θα πει όχι μόνο και μόνο για να μας πάει κόντρα.", "Dad? After the knee operation, his doctor told him to be careful. And you know how stubborn he is; if we suggest it, he'll say no just to go against us."),
  L("Νεφέλη", "f", "Γι' αυτό ακριβώς είναι κατάλληλο: χωρίς τρέξιμο και χωρίς επαφή. Πρώτα ας ρωτήσουμε τον γιατρό του. Κι αν συμφωνήσει, ας του το πει ο κυρ Θανάσης, ο γείτονας, που παίζει ήδη στην ομάδα. Από εκείνον θα το δεχτεί πιο εύκολα.", "That's exactly why it's suitable: no running and no contact. First let's ask his doctor. And if he agrees, let Mr Thanasis, the neighbour, who already plays in the team, tell him about it. He'll accept it more easily from him."),
  L("Μάριος", "m", "Έξυπνο. Και αν πάει, του χρωστάω ένα καινούργιο ζευγάρι αθλητικά παπούτσια· τα παλιά του είναι από την εποχή του Μουντιάλ του '94.", "Clever. And if he goes, I owe him a new pair of trainers; his old ones are from the time of the '94 World Cup."),
 ],
 "questions": [
  Q("Τι ιδιαίτερο έχει το «ποδόσφαιρο περπατώντας»;", ["Παίζεται μόνο σε κλειστά γήπεδα", "Δεν τρέχει κανείς και απαγορεύονται τα μαρκαρίσματα", "Παίζεται χωρίς μπάλα", "Είναι μόνο για γυναίκες"], 1, "Δεν τρέχει κανείς, και απαγορεύονται τα μαρκαρίσματα"),
  Q("Γιατί ο Μάριος πιστεύει ότι ο πατέρας τους θα αρνηθεί;", ["Γιατί δεν του αρέσει το ποδόσφαιρο", "Γιατί δεν έχει χρόνο", "Γιατί είναι πεισματάρης και θα τους πάει κόντρα", "Γιατί ο σύλλογος είναι μακριά"], 2, "αν του το προτείνουμε εμείς, θα πει όχι μόνο και μόνο για να μας πάει κόντρα"),
  Q("Τι προτείνει τελικά η Νεφέλη;", ["Να ρωτήσουν τον γιατρό και μετά να του το πει ο γείτονας", "Να τον γράψουν χωρίς να του το πουν", "Να πάνε μαζί του στο πρώτο παιχνίδι", "Να του αγοράσουν μια συνδρομή σε γυμναστήριο"], 0, "Πρώτα ας ρωτήσουμε τον γιατρό του"),
 ],
 "gloss": {"σύνταξη": "βγαίνω στη σύνταξη — to retire", "ανησυχώ": "ανησυχώ — to worry", "μαρκαρίσματα": "μαρκάρισμα — tackle, marking (football)", "εγχείρηση": "εγχείρηση — operation, surgery", "γόνατο": "γόνατο — knee", "πεισματάρης": "πεισματάρης — stubborn", "κόντρα": "πάω κόντρα σε κάποιον — to go against someone", "κατάλληλο": "κατάλληλος — suitable", "επαφή": "επαφή — contact", "χρωστάω": "χρωστάω — to owe", "αθλητικά παπούτσια": "αθλητικά παπούτσια — trainers", "Μουντιάλ": "Μουντιάλ — the (football) World Cup"}
})

ITEMS.append({
 "id": "l126-int-zogkler", "title": "Ένας ζογκλέρ στους δρόμους της πόλης", "title_en": "A juggler in the city streets", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή για τους καλλιτέχνες του δρόμου. Καλεσμένος είναι ο Άλκης, ζογκλέρ.",
 "script": [
  L("Δημοσιογράφος", "f", "Άλκη, πώς έγινες ζογκλέρ;", "Alkis, how did you become a juggler?"),
  L("Άλκης", "m", "Κατά τύχη. Στα δεκαέξι μου έσπασα το πόδι και έμεινα δύο μήνες στο σπίτι. Ένας φίλος μού έφερε τρία μπαλάκια κι ένα βιβλίο με οδηγίες, για να μη βαριέμαι. Όταν έβγαλα τον γύψο, μπορούσα να κρατάω πέντε μπαλάκια στον αέρα.", "By chance. At sixteen I broke my leg and stayed at home for two months. A friend brought me three balls and a book of instructions, so I wouldn't get bored. When the cast came off, I could keep five balls in the air."),
  L("Δημοσιογράφος", "f", "Και πώς είναι να δουλεύεις στον δρόμο;", "And what's it like to work in the street?"),
  L("Άλκης", "m", "Είναι η πιο τίμια σκηνή που υπάρχει. Στο θέατρο ο κόσμος έχει πληρώσει εισιτήριο και θα καθίσει ως το τέλος. Στον δρόμο, αν δεν τους κερδίσεις μέσα στα πρώτα τριάντα δευτερόλεπτα, απλώς προσπερνούν. Γι' αυτό ξεκινάω πάντα με το πιο δύσκολο κόλπο, με τους αναμμένους πυρσούς.", "It's the most honest stage there is. In the theatre people have paid for a ticket and will sit until the end. In the street, if you don't win them over in the first thirty seconds, they just walk past. That's why I always start with the hardest trick, with the lit torches."),
  L("Δημοσιογράφος", "f", "Χρειάζεσαι άδεια από τον δήμο;", "Do you need a permit from the municipality?"),
  L("Άλκης", "m", "Ναι, και καλά κάνουν που τη ζητάνε. Η άδεια ορίζει σε ποια σημεία και ποιες ώρες μπορούμε να παίζουμε, ώστε να μην ενοχλούμε τους κατοίκους. Με τους μαγαζάτορες έχουμε συνήθως καλές σχέσεις· ξέρουν ότι όπου μαζεύεται κόσμος, κερδίζουν κι εκείνοι.", "Yes, and they're right to require it. The permit sets at which spots and at what times we can perform, so that we don't disturb the residents. With shopkeepers we usually get on well; they know that wherever a crowd gathers, they benefit too."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε ο Άλκης να κάνει ζογκλερικά;", ["Σε μια σχολή τσίρκου", "Όταν έσπασε το πόδι του και ένας φίλος του έφερε μπαλάκια", "Βλέποντας βίντεο στο διαδίκτυο", "Από τον πατέρα του"], 1, "Στα δεκαέξι μου έσπασα το πόδι"),
  Q("Γιατί ξεκινάει πάντα με το πιο δύσκολο κόλπο;", ["Γιατί είναι πιο φρέσκος στην αρχή", "Γιατί το ζητά ο δήμος", "Γιατί πρέπει να κερδίσει τον κόσμο μέσα στα πρώτα δευτερόλεπτα", "Γιατί οι πυρσοί σβήνουν γρήγορα"], 2, "αν δεν τους κερδίσεις μέσα στα πρώτα τριάντα δευτερόλεπτα, απλώς προσπερνούν"),
  Q("Τι ορίζει η άδεια του δήμου;", ["Σε ποια σημεία και ποιες ώρες μπορούν να παίζουν", "Πόσα χρήματα μπορούν να μαζεύουν", "Ποια κόλπα επιτρέπονται", "Πόσοι καλλιτέχνες μπορούν να παίζουν μαζί"], 0, "Η άδεια ορίζει σε ποια σημεία και ποιες ώρες μπορούμε να παίζουμε"),
 ],
 "gloss": {"ζογκλέρ": "ζογκλέρ — juggler", "καλλιτέχνες του δρόμου": "καλλιτέχνης του δρόμου — street performer", "μπαλάκια": "μπαλάκι — small ball", "γύψο": "γύψος — plaster cast", "τίμια": "τίμιος — honest", "προσπερνούν": "προσπερνάω — to walk past", "κόλπο": "κόλπο — trick", "αναμμένους": "αναμμένος — lit", "πυρσούς": "πυρσός — torch", "άδεια": "άδεια — permit", "ενοχλούμε": "ενοχλώ — to disturb", "μαγαζάτορες": "μαγαζάτορας — shopkeeper"}
})

ITEMS.append({
 "id": "l126-rep-ilektrika-kaikia", "title": "Ηλεκτρικά καΐκια στο λιμάνι", "title_en": "Electric caiques in the harbour", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στις περιφερειακές ειδήσεις για μια αλλαγή σε ένα μικρό νησί.",
 "script": [
  L("Ρεπόρτερ", "f", "Στο μικρό λιμάνι του νησιού, τα καΐκια που μεταφέρουν λουόμενους στις απομονωμένες παραλίες δεν ακούγονται πια. Τρεις από τους πέντε καπεταναίους αντικατέστησαν τις μηχανές πετρελαίου με ηλεκτρικούς κινητήρες, με τη βοήθεια ενός προγράμματος επιδότησης.", "In the island's small harbour, the caiques that carry bathers to the isolated beaches can no longer be heard. Three of the five skippers have replaced their diesel engines with electric motors, with the help of a subsidy programme."),
  L("Ρεπόρτερ", "f", "Ο καπετάν Μιχάλης λέει ότι στην αρχή ήταν διστακτικός. Φοβόταν ότι οι μπαταρίες δεν θα άντεχαν όλη μέρα. Τελικά, οι διαδρομές είναι σύντομες, και το καΐκι φορτίζει το βράδυ, στο ρεύμα του λιμανιού. «Γλιτώνω τα καύσιμα, και δεν μυρίζω πια πετρέλαιο όλο το καλοκαίρι», λέει.", "Captain Michalis says that at first he was hesitant. He was afraid the batteries wouldn't last all day. In the end, the routes are short, and the caique charges at night, from the harbour's power supply. 'I save on fuel, and I no longer smell of diesel all summer,' he says."),
  L("Ρεπόρτερ", "f", "Οι επιβάτες φαίνεται να εκτιμούν την ησυχία: πολλοί λένε ότι τώρα ακούν τα κύματα και βλέπουν καλύτερα τα ψάρια στα καθαρά νερά. Ο δήμος σκοπεύει να εγκαταστήσει φωτοβολταϊκά στο λιμάνι, ώστε η φόρτιση να γίνεται με ενέργεια από τον ήλιο.", "Passengers seem to appreciate the quiet: many say that now they can hear the waves and see the fish better in the clear water. The municipality plans to install solar panels at the harbour, so that charging is done with energy from the sun."),
 ],
 "questions": [
  Q("Πώς κατάφεραν οι καπεταναίοι να αλλάξουν τις μηχανές;", ["Με δάνειο από την τράπεζα", "Με τη βοήθεια ενός προγράμματος επιδότησης", "Με χρήματα από τους επιβάτες", "Τις έφτιαξαν μόνοι τους"], 1, "με τη βοήθεια ενός προγράμματος επιδότησης"),
  Q("Τι φοβόταν στην αρχή ο καπετάν Μιχάλης;", ["Ότι οι επιβάτες δεν θα ήθελαν να ταξιδέψουν", "Ότι το καΐκι θα ήταν πιο αργό", "Ότι οι μπαταρίες δεν θα άντεχαν όλη μέρα", "Ότι θα χάλαγε στη θάλασσα"], 2, "Φοβόταν ότι οι μπαταρίες δεν θα άντεχαν όλη μέρα"),
  Q("Τι σκοπεύει να κάνει ο δήμος;", ["Να εγκαταστήσει φωτοβολταϊκά στο λιμάνι", "Να αγοράσει δικό του καΐκι", "Να απαγορεύσει τις μηχανές πετρελαίου", "Να φτιάξει νέο λιμάνι"], 0, "Ο δήμος σκοπεύει να εγκαταστήσει φωτοβολταϊκά στο λιμάνι"),
 ],
 "gloss": {"περιφερειακές": "περιφερειακός — regional", "καΐκια": "καΐκι — caique (small wooden boat)", "απομονωμένες": "απομονωμένος — isolated", "καπεταναίους": "καπετάνιος — skipper", "αντικατέστησαν": "αντικαθιστώ — to replace", "κινητήρες": "κινητήρας — motor, engine", "επιδότησης": "επιδότηση — subsidy", "διστακτικός": "διστακτικός — hesitant", "φορτίζει": "φορτίζω — to charge", "καύσιμα": "καύσιμα — fuel", "εκτιμούν": "εκτιμώ — to appreciate", "φωτοβολταϊκά": "φωτοβολταϊκά — solar panels", "φόρτιση": "φόρτιση — charging"}
})

ITEMS.append({
 "id": "l126-rep-gaidouria", "title": "Ένα καταφύγιο για γαϊδουράκια", "title_en": "A sanctuary for donkeys", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για τα ζώα.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε ένα κτήμα έξω από το χωριό ζουν σήμερα σαράντα δύο γαϊδούρια. Τα περισσότερα είναι ηλικιωμένα ή άρρωστα και έχουν δουλέψει μια ζωή κουβαλώντας φορτία στα χωράφια και στα βουνά. Όταν οι ιδιοκτήτες τους δεν μπορούσαν πια να τα φροντίσουν, τα έφεραν εδώ.", "On an estate outside the village there now live forty-two donkeys. Most of them are old or ill and have worked their whole lives carrying loads in the fields and the mountains. When their owners could no longer look after them, they brought them here."),
  L("Ρεπόρτερ", "m", "Το καταφύγιο το ίδρυσε μια κτηνίατρος, που επί χρόνια έβλεπε γαϊδούρια εγκαταλελειμμένα στους δρόμους. Σήμερα τη βοηθούν δύο υπάλληλοι και πολλοί εθελοντές, οι οποίοι καθαρίζουν τους στάβλους, κόβουν τις οπλές και βουρτσίζουν τα ζώα.", "The sanctuary was founded by a vet who for years saw donkeys abandoned on the roads. Today two employees and many volunteers help her, cleaning the stables, trimming the hooves and brushing the animals."),
  L("Ρεπόρτερ", "m", "Το καταφύγιο δεν παίρνει κρατική χρηματοδότηση. Ζει από δωρεές και από τις «υιοθεσίες»: όποιος θέλει, πληρώνει ένα μικρό ποσό κάθε μήνα για ένα συγκεκριμένο γαϊδουράκι και λαμβάνει φωτογραφίες και νέα του. Τα Σαββατοκύριακα οι επισκέπτες μπορούν να έρθουν, αλλά απαγορεύεται να ταΐζουν τα ζώα χωρίς άδεια.", "The sanctuary gets no state funding. It lives on donations and 'adoptions': anyone who wants pays a small amount every month for a particular donkey and receives photos and news of it. At weekends visitors can come, but it's forbidden to feed the animals without permission."),
 ],
 "questions": [
  Q("Γιατί έφεραν τα γαϊδούρια στο καταφύγιο;", ["Γιατί πουλήθηκαν σε μια φάρμα", "Γιατί οι ιδιοκτήτες τους δεν μπορούσαν πια να τα φροντίσουν", "Γιατί τα βρήκε η αστυνομία", "Για να γεννήσουν"], 1, "Όταν οι ιδιοκτήτες τους δεν μπορούσαν πια να τα φροντίσουν, τα έφεραν εδώ"),
  Q("Ποια δουλειά ΔΕΝ αναφέρεται ότι κάνουν οι εθελοντές;", ["Καθαρίζουν τους στάβλους", "Κόβουν τις οπλές", "Οδηγούν τους επισκέπτες σε βόλτες", "Βουρτσίζουν τα ζώα"], 2, "καθαρίζουν τους στάβλους, κόβουν τις οπλές και βουρτσίζουν τα ζώα"),
  Q("Τι είναι οι «υιοθεσίες»;", ["Πληρώνεις μηνιαία για ένα γαϊδουράκι και παίρνεις φωτογραφίες και νέα του", "Παίρνεις ένα γαϊδουράκι στο σπίτι σου", "Δουλεύεις εθελοντικά ένα Σαββατοκύριακο", "Αγοράζεις τρόφιμα για το καταφύγιο"], 0, "πληρώνει ένα μικρό ποσό κάθε μήνα για ένα συγκεκριμένο γαϊδουράκι και λαμβάνει φωτογραφίες και νέα του"),
 ],
 "gloss": {"καταφύγιο": "καταφύγιο — sanctuary, shelter", "γαϊδουράκι": "γαϊδουράκι — little donkey", "κτήμα": "κτήμα — estate, farm", "γαϊδούρια": "γαϊδούρι — donkey", "φορτία": "φορτίο — load", "εγκαταλελειμμένα": "εγκαταλελειμμένος — abandoned", "στάβλους": "στάβλος — stable", "οπλές": "οπλή — hoof", "βουρτσίζουν": "βουρτσίζω — to brush", "χρηματοδότηση": "χρηματοδότηση — funding", "υιοθεσίες": "υιοθεσία — adoption", "ταΐζουν": "ταΐζω — to feed"}
})

ITEMS.append({
 "id": "l126-mono-xoris-zachari", "title": "Ένας μήνας χωρίς πρόσθετη ζάχαρη", "title_en": "A month without added sugar", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε τη Χαρά, γραφίστρια, να μιλάει σε ένα podcast για ένα πείραμα που έκανε.",
 "script": [
  L("Χαρά", "f", "Τον Ιανουάριο αποφάσισα να μη φάω καθόλου πρόσθετη ζάχαρη για έναν μήνα. Όχι επειδή μου το είπε γιατρός, αλλά επειδή συνειδητοποίησα ότι κάθε απόγευμα, στις τέσσερις, έτρωγα σοκολάτα στο γραφείο χωρίς καν να το σκέφτομαι.", "In January I decided not to eat any added sugar for a month. Not because a doctor told me to, but because I realised that every afternoon, at four, I was eating chocolate at the office without even thinking about it."),
  L("Χαρά", "f", "Το πιο δύσκολο δεν ήταν τα γλυκά, αλλά να διαβάζω τις ετικέτες στο σούπερ μάρκετ. Βρήκα ζάχαρη σε ψωμί του τοστ, σε σάλτσες, ακόμα και σε ένα αλλαντικό. Τις πρώτες δέκα μέρες είχα πονοκεφάλους και ήμουν νευρική με όλους.", "The hardest thing wasn't the sweets, but reading the labels in the supermarket. I found sugar in sandwich bread, in sauces, even in a cold meat. For the first ten days I had headaches and was irritable with everyone."),
  L("Χαρά", "f", "Μετά όμως κάτι άλλαξε: ένα μήλο μού φαινόταν πιο γλυκό από ποτέ, και το απογευματινό κενό ενέργειας σχεδόν εξαφανίστηκε. Δεν έκοψα τα γλυκά για πάντα, γιατί μου αρέσουν πολύ. Τώρα όμως τρώω γλυκό όταν το απολαμβάνω πραγματικά, όχι από συνήθεια.", "But then something changed: an apple seemed sweeter to me than ever, and the afternoon energy slump almost disappeared. I didn't give up sweets for ever, because I like them a lot. But now I eat something sweet when I really enjoy it, not out of habit."),
 ],
 "questions": [
  Q("Γιατί αποφάσισε η Χαρά να κόψει την πρόσθετη ζάχαρη;", ["Γιατί της το είπε ο γιατρός", "Γιατί κατάλαβε ότι έτρωγε σοκολάτα κάθε απόγευμα χωρίς να το σκέφτεται", "Για να χάσει βάρος πριν από έναν γάμο", "Για ένα στοίχημα με συναδέλφους"], 1, "έτρωγα σοκολάτα στο γραφείο χωρίς καν να το σκέφτομαι"),
  Q("Τι ήταν, σύμφωνα με την ίδια, το πιο δύσκολο;", ["Να αντισταθεί στα γλυκά", "Να μαγειρεύει κάθε μέρα", "Να διαβάζει τις ετικέτες στο σούπερ μάρκετ", "Να εξηγεί την απόφασή της στους φίλους"], 2, "Το πιο δύσκολο δεν ήταν τα γλυκά, αλλά να διαβάζω τις ετικέτες στο σούπερ μάρκετ"),
  Q("Τι κάνει σήμερα;", ["Τρώει γλυκό μόνο όταν το απολαμβάνει πραγματικά", "Δεν τρώει ποτέ γλυκά", "Τρώει σοκολάτα κάθε απόγευμα όπως πριν", "Τρώει μόνο σπιτικά γλυκά"], 0, "τρώω γλυκό όταν το απολαμβάνω πραγματικά, όχι από συνήθεια"),
 ],
 "gloss": {"γραφίστρια": "γραφίστρια — graphic designer (f.)", "πρόσθετη": "πρόσθετος — added", "συνειδητοποίησα": "συνειδητοποιώ — to realise", "ετικέτες": "ετικέτα — label", "ψωμί του τοστ": "ψωμί του τοστ — sandwich bread", "αλλαντικό": "αλλαντικό — cold meat, cured meat", "πονοκεφάλους": "πονοκέφαλος — headache", "νευρική": "νευρικός — irritable, nervous", "κενό ενέργειας": "κενό ενέργειας — energy slump", "απολαμβάνω": "απολαμβάνω — to enjoy", "συνήθεια": "συνήθεια — habit"}
})

ITEMS.append({
 "id": "l126-mono-orinos-xenonas", "title": "Ένας χειμώνας σε ορεινό ξενώνα", "title_en": "A winter at a mountain guesthouse", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε τον Ορέστη, φοιτητή, να μιλάει για μια δουλειά που έκανε τον περασμένο χειμώνα.",
 "script": [
  L("Ορέστης", "m", "Πέρσι διέκοψα για ένα εξάμηνο τις σπουδές μου και δούλεψα σε έναν ξενώνα σε ένα ορεινό χωριό, κοντά σε ένα χιονοδρομικό. Έκανα λίγο απ' όλα: σέρβιρα πρωινό, άναβα τα τζάκια, καθάριζα τα δωμάτια και το απόγευμα έφτιαχνα τσάι του βουνού για τους πελάτες.", "Last year I interrupted my studies for a semester and worked at a guesthouse in a mountain village, near a ski resort. I did a bit of everything: I served breakfast, lit the fireplaces, cleaned the rooms and in the afternoon made mountain tea for the guests."),
  L("Ορέστης", "m", "Η πιο δύσκολη μέρα ήταν όταν μια χιονοθύελλα έκλεισε τον δρόμο για τρεις μέρες. Είχαμε δεκαπέντε πελάτες, και το ρεύμα κοβόταν συνέχεια. Μαγειρεύαμε στο τζάκι και παίζαμε επιτραπέζια με κεριά. Παραδόξως, αυτές ήταν οι μέρες που οι πελάτες θυμούνται περισσότερο.", "The hardest day was when a blizzard closed the road for three days. We had fifteen guests, and the power kept going off. We cooked in the fireplace and played board games by candlelight. Paradoxically, those were the days the guests remember most."),
  L("Ορέστης", "m", "Γύρισα στη σχολή με λιγότερα χρήματα απ' ό,τι υπολόγιζα, αλλά με κάτι πιο πολύτιμο: έμαθα να λύνω προβλήματα χωρίς να περιμένω να μου πει κάποιος τι να κάνω. Και φυσικά, έμαθα επιτέλους να κάνω σκι.", "I went back to university with less money than I'd reckoned, but with something more valuable: I learned to solve problems without waiting for someone to tell me what to do. And of course, I finally learned to ski."),
 ],
 "questions": [
  Q("Τι δουλειές έκανε ο Ορέστης στον ξενώνα;", ["Μόνο δουλειά ρεσεψιόν", "Λίγο απ' όλα: πρωινό, τζάκια, δωμάτια, τσάι", "Ήταν δάσκαλος σκι", "Ήταν μάγειρας στο εστιατόριο"], 1, "Έκανα λίγο απ' όλα"),
  Q("Τι έγινε όταν η χιονοθύελλα έκλεισε τον δρόμο;", ["Οι πελάτες έφυγαν με ελικόπτερο", "Ο ξενώνας έκλεισε", "Μαγείρευαν στο τζάκι και έπαιζαν επιτραπέζια με κεριά", "Ο Ορέστης έμεινε μόνος του"], 2, "Μαγειρεύαμε στο τζάκι και παίζαμε επιτραπέζια με κεριά"),
  Q("Ποιο ήταν, κατά τον ίδιο, το πιο πολύτιμο που κέρδισε;", ["Έμαθε να λύνει προβλήματα χωρίς να περιμένει οδηγίες", "Μάζεψε πολλά χρήματα", "Βρήκε μόνιμη δουλειά", "Γνώρισε τη σύντροφό του"], 0, "έμαθα να λύνω προβλήματα χωρίς να περιμένω να μου πει κάποιος τι να κάνω"),
 ],
 "gloss": {"ξενώνα": "ξενώνας — guesthouse", "διέκοψα": "διακόπτω — to interrupt", "εξάμηνο": "εξάμηνο — semester", "χιονοδρομικό": "χιονοδρομικό (κέντρο) — ski resort", "σέρβιρα": "σερβίρω — to serve", "τζάκια": "τζάκι — fireplace", "τσάι του βουνού": "τσάι του βουνού — Greek mountain tea", "χιονοθύελλα": "χιονοθύελλα — blizzard", "επιτραπέζια": "επιτραπέζιο (παιχνίδι) — board game", "Παραδόξως": "παραδόξως — paradoxically", "υπολόγιζα": "υπολογίζω — to reckon, calculate", "πολύτιμο": "πολύτιμος — valuable"}
})

ITEMS.append({
 "id": "l126-c1-abilene", "title": "Ένα ταξίδι που δεν ήθελε κανείς", "title_en": "A trip nobody wanted", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ομιλία για τη λήψη αποφάσεων σε ομάδες, σε ένα συνέδριο για στελέχη επιχειρήσεων.",
 "script": [
  L("Ομιλητής", "m", "Επιτρέψτε μου να ξεκινήσω με μια ιστορία που έκανε γνωστή ο Αμερικανός καθηγητής διοίκησης Τζέρι Χάρβεϊ, το 1974. Ένα ζεστό απόγευμα στο Τέξας, μια οικογένεια κάθεται στη βεράντα και παίζει ντόμινο. Ξαφνικά ο πεθερός προτείνει: «Γιατί δεν πάμε να φάμε στο Άμπιλιν;», μια πόλη που απέχει περίπου ογδόντα πέντε χιλιόμετρα. Η κόρη του λέει «Καλή ιδέα», ο γαμπρός λέει ότι δεν έχει αντίρρηση, και η πεθερά συμφωνεί κι εκείνη.", "Allow me to begin with a story made famous by the American management professor Jerry Harvey in 1974. On a hot afternoon in Texas, a family sits on the porch playing dominoes. Suddenly the father-in-law suggests: 'Why don't we go and eat in Abilene?', a town about eighty-five kilometres away. His daughter says 'Good idea', the son-in-law says he has no objection, and the mother-in-law agrees too."),
  L("Ομιλητής", "m", "Το ταξίδι, με ένα αυτοκίνητο χωρίς κλιματισμό, μέσα στη σκόνη, είναι εξαντλητικό, και το φαγητό απογοητευτικό. Όταν επιστρέφουν, ο ένας λέει διστακτικά ότι δεν ήθελε καθόλου να πάει. Και τότε αποκαλύπτεται το παράδοξο: κανείς δεν ήθελε να πάει στο Άμπιλιν, ούτε καν ο πεθερός, που το είχε προτείνει μόνο επειδή νόμιζε ότι οι άλλοι βαριούνταν. Όλοι συμφώνησαν με μια απόφαση που ο καθένας ιδιωτικά απέρριπτε.", "The journey, in a car without air conditioning, through the dust, is exhausting, and the food disappointing. When they return, one of them says hesitantly that he didn't want to go at all. And then the paradox is revealed: nobody wanted to go to Abilene, not even the father-in-law, who had suggested it only because he thought the others were bored. Everyone agreed to a decision that each of them privately rejected."),
  L("Ομιλητής", "m", "Ο Χάρβεϊ ονόμασε το φαινόμενο «παράδοξο του Άμπιλιν» και υποστήριξε ότι οι οργανισμοί συχνά δεν αποτυγχάνουν επειδή δεν μπορούν να διαχειριστούν τη διαφωνία, αλλά επειδή δεν μπορούν να διαχειριστούν τη συμφωνία. Σε αντίθεση με την ομαδική σκέψη, όπου η πίεση της ομάδας είναι ορατή, εδώ η πίεση είναι σχεδόν φανταστική: ο καθένας φοβάται μια αποδοκιμασία που ίσως δεν θα ερχόταν ποτέ. Το αντίδοτο, κατά τον Χάρβεϊ, είναι απλό στη διατύπωση και δύσκολο στην πράξη: να έχει κανείς το θάρρος να πει πρώτος τι πραγματικά πιστεύει.", "Harvey named the phenomenon 'the Abilene paradox' and argued that organisations often fail not because they cannot manage disagreement, but because they cannot manage agreement. Unlike groupthink, where the pressure of the group is visible, here the pressure is almost imaginary: each person fears a disapproval that might never have come. The antidote, according to Harvey, is simple to state and hard to practise: to have the courage to be the first to say what one really believes."),
 ],
 "questions": [
  Q("Γιατί πρότεινε ο πεθερός το ταξίδι;", ["Γιατί ήθελε να δοκιμάσει ένα εστιατόριο", "Γιατί νόμιζε ότι οι άλλοι βαριούνταν", "Γιατί είχε δουλειά στο Άμπιλιν", "Γιατί το ζήτησε η κόρη του"], 1, "το είχε προτείνει μόνο επειδή νόμιζε ότι οι άλλοι βαριούνταν"),
  Q("Ποιο είναι το «παράδοξο» της ιστορίας;", ["Ότι το ταξίδι κράτησε λιγότερο απ' ό,τι περίμεναν", "Ότι το φαγητό ήταν καλύτερο απ' ό,τι περίμεναν", "Ότι όλοι συμφώνησαν με μια απόφαση που ο καθένας ιδιωτικά απέρριπτε", "Ότι κανείς δεν θυμόταν ποιος πρότεινε το ταξίδι"], 2, "Όλοι συμφώνησαν με μια απόφαση που ο καθένας ιδιωτικά απέρριπτε"),
  Q("Σύμφωνα με τον Χάρβεϊ, γιατί αποτυγχάνουν συχνά οι οργανισμοί;", ["Γιατί δεν μπορούν να διαχειριστούν τη συμφωνία", "Γιατί έχουν πάρα πολλές διαφωνίες", "Γιατί οι ηγέτες τους είναι αυταρχικοί", "Γιατί δεν έχουν αρκετά χρήματα"], 0, "δεν μπορούν να διαχειριστούν τη συμφωνία"),
  Q("Σε τι διαφέρει το φαινόμενο από την ομαδική σκέψη, κατά τον ομιλητή;", ["Εμφανίζεται μόνο σε οικογένειες", "Αφορά μόνο σημαντικές αποφάσεις", "Οδηγεί πάντα σε σωστές αποφάσεις", "Η πίεση είναι σχεδόν φανταστική, όχι ορατή"], 3, "εδώ η πίεση είναι σχεδόν φανταστική"),
 ],
 "gloss": {"λήψη αποφάσεων": "λήψη αποφάσεων — decision-making", "στελέχη": "στέλεχος — executive, manager", "διοίκησης": "διοίκηση (επιχειρήσεων) — management", "ντόμινο": "ντόμινο — dominoes", "πεθερός": "πεθερός — father-in-law", "γαμπρός": "γαμπρός — son-in-law", "αντίρρηση": "αντίρρηση — objection", "πεθερά": "πεθερά — mother-in-law", "εξαντλητικό": "εξαντλητικός — exhausting", "απογοητευτικό": "απογοητευτικός — disappointing", "αποκαλύπτεται": "αποκαλύπτομαι — to be revealed", "απέρριπτε": "απορρίπτω — to reject", "αποδοκιμασία": "αποδοκιμασία — disapproval", "αντίδοτο": "αντίδοτο — antidote", "διατύπωση": "διατύπωση — wording, formulation"}
})

ITEMS.append({
 "id": "l126-c1-manto-mavrogenous", "title": "Η αρχόντισσα που έδωσε τα πάντα", "title_en": "The noblewoman who gave everything", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με έναν ιστορικό για τη Μαντώ Μαυρογένους, ηρωίδα του 1821.",
 "script": [
  L("Δημοσιογράφος", "f", "Η Μαντώ Μαυρογένους είναι γνωστή σε όλους από τα σχολικά βιβλία, συχνά όμως μόνο ως όνομα. Ποια ήταν πραγματικά;", "Manto Mavrogenous is known to everyone from school books, but often only as a name. Who was she really?"),
  L("Ιστορικός", "m", "Γεννήθηκε στην Τεργέστη, πιθανότατα το 1796, σε μια πλούσια οικογένεια εμπόρων με καταγωγή από τη Μύκονο. Είχε μορφωθεί πολύ καλά για γυναίκα της εποχής της: μιλούσε γαλλικά και ιταλικά και είχε διαβάσει αρχαία ελληνική ιστορία. Όταν ξέσπασε η Επανάσταση, βρισκόταν στη Μύκονο, και αποφάσισε να διαθέσει την περιουσία της στον αγώνα. Εξόπλισε πλοία και πλήρωσε στρατιώτες με δικά της χρήματα.", "She was born in Trieste, most probably in 1796, into a wealthy merchant family from Mykonos. She was very well educated for a woman of her time: she spoke French and Italian and had read ancient Greek history. When the Revolution broke out, she was on Mykonos, and she decided to devote her fortune to the struggle. She equipped ships and paid soldiers with her own money."),
  L("Δημοσιογράφος", "f", "Λέγεται ότι πήρε μέρος και η ίδια σε μάχες.", "It is said that she took part in battles herself."),
  L("Ιστορικός", "m", "Το πιο γνωστό επεισόδιο είναι το φθινόπωρο του 1822, όταν οι κάτοικοι της Μυκόνου, με τη συμμετοχή της, απέκρουσαν μια απόβαση Αλγερινών στο νησί. Πέρα όμως από τα όπλα, η Μαντώ είχε καταλάβει τη δύναμη της κοινής γνώμης. Έγραψε επιστολή προς τις γυναίκες του Παρισιού, ζητώντας τη στήριξή τους για τον αγώνα των Ελλήνων, σε μια εποχή που το φιλελληνικό κίνημα διαμορφωνόταν στην Ευρώπη.", "The best-known episode is in the autumn of 1822, when the inhabitants of Mykonos, with her participation, repelled a landing by Algerians on the island. Beyond weapons, however, Manto had understood the power of public opinion. She wrote a letter to the women of Paris, asking for their support for the Greeks' struggle, at a time when the philhellenic movement was taking shape in Europe."),
  L("Ιστορικός", "m", "Το τέλος της είναι από τα πιο θλιβερά της περιόδου. Ο Καποδίστριας τής απένειμε τιμητικά τον βαθμό του αντιστράτηγου, η περιουσία της όμως είχε χαθεί, και οι αιτήσεις της για αποζημίωση έμειναν σε μεγάλο βαθμό αναπάντητες. Πέθανε φτωχή στην Πάρο το 1848. Η ιστορία της θυμίζει ότι το νέο κράτος δεν φέρθηκε πάντα γενναιόδωρα σε όσους θυσιάστηκαν για αυτό.", "Her end is one of the saddest of the period. Kapodistrias awarded her the honorary rank of lieutenant general, but her fortune had been lost, and her requests for compensation largely went unanswered. She died poor on Paros in 1848. Her story reminds us that the new state did not always treat generously those who sacrificed themselves for it."),
 ],
 "questions": [
  Q("Τι έκανε η Μαντώ με την περιουσία της όταν ξέσπασε η Επανάσταση;", ["Την έστειλε στην Τεργέστη για ασφάλεια", "Τη διέθεσε στον αγώνα, εξοπλίζοντας πλοία και πληρώνοντας στρατιώτες", "Αγόρασε κτήματα στη Μύκονο", "Τη δώρισε σε ένα μοναστήρι"], 1, "αποφάσισε να διαθέσει την περιουσία της στον αγώνα"),
  Q("Τι συνέβη στη Μύκονο το φθινόπωρο του 1822;", ["Η Μαντώ εξορίστηκε από το νησί", "Υπογράφηκε συνθήκη ειρήνης", "Οι κάτοικοι απέκρουσαν μια απόβαση Αλγερινών", "Ένας σεισμός κατέστρεψε το νησί"], 2, "απέκρουσαν μια απόβαση Αλγερινών στο νησί"),
  Q("Γιατί έγραψε στις γυναίκες του Παρισιού;", ["Για να ζητήσει τη στήριξή τους για τον αγώνα των Ελλήνων", "Για να βρει σύζυγο", "Για να πουλήσει την περιουσία της", "Για να ζητήσει άσυλο στη Γαλλία"], 0, "ζητώντας τη στήριξή τους για τον αγώνα των Ελλήνων"),
  Q("Ποιο συμπέρασμα βγάζει ο ιστορικός από το τέλος της;", ["Ότι η Μαντώ δεν ζήτησε ποτέ βοήθεια", "Ότι ο Καποδίστριας την αγνόησε εντελώς", "Ότι η Πάρος ήταν ο τόπος καταγωγής της", "Ότι το νέο κράτος δεν φέρθηκε πάντα γενναιόδωρα σε όσους θυσιάστηκαν"], 3, "το νέο κράτος δεν φέρθηκε πάντα γενναιόδωρα σε όσους θυσιάστηκαν για αυτό"),
 ],
 "gloss": {"ηρωίδα": "ηρωίδα — heroine", "Τεργέστη": "Τεργέστη — Trieste", "καταγωγή": "καταγωγή — origin, descent", "μορφωθεί": "μορφώνομαι — to be educated", "ξέσπασε": "ξεσπάω — to break out", "διαθέσει": "διαθέτω — to devote, make available", "περιουσία": "περιουσία — fortune, property", "Εξόπλισε": "εξοπλίζω — to equip, arm", "απέκρουσαν": "αποκρούω — to repel", "απόβαση": "απόβαση — landing", "κοινής γνώμης": "κοινή γνώμη — public opinion", "φιλελληνικό κίνημα": "φιλελληνικό κίνημα — philhellenic movement", "απένειμε": "απονέμω — to award", "αντιστράτηγου": "αντιστράτηγος — lieutenant general", "αποζημίωση": "αποζημίωση — compensation", "γενναιόδωρα": "γενναιόδωρα — generously"}
})

rnd = random.Random(126)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-126.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
