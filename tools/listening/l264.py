# Source for library/listening/listening-264.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l264.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l264-news-ichitika-fanaria", "title": "Ηχητικά φανάρια για τυφλούς πεζούς σε εξήντα διασταυρώσεις της Θεσσαλονίκης", "title_en": "Audible traffic lights for blind pedestrians at sixty junctions in Thessaloniki", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο απογευματινό δελτίο ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Εξήντα διασταυρώσεις στο κέντρο της Θεσσαλονίκης θα αποκτήσουν μέσα στους επόμενους μήνες ηχητικά φανάρια για τυφλούς και άτομα με προβλήματα όρασης. Όταν ανάβει το πράσινο για τους πεζούς, ένας ήχος θα δείχνει ότι μπορούν να περάσουν με ασφάλεια.", "Sixty junctions in central Thessaloniki will get audible traffic lights for blind and partially sighted people in the coming months. When the light turns green for pedestrians, a sound will show that they can cross safely."),
  L("Εκφωνητής", "m", "Στα φανάρια θα υπάρχει επίσης ένα κουμπί που δονείται όσο διαρκεί το πράσινο, για όσους έχουν και προβλήματα ακοής. Η ένταση του ήχου θα ρυθμίζεται αυτόματα ανάλογα με τον θόρυβο του δρόμου, ώστε να μην ενοχλούνται οι κάτοικοι τη νύχτα.", "The lights will also have a button that vibrates as long as the green lasts, for those who also have hearing problems. The volume of the sound will be adjusted automatically according to the noise of the street, so that residents are not disturbed at night."),
  L("Εκφωνητής", "m", "Οι διασταυρώσεις επιλέχθηκαν μαζί με τον τοπικό σύλλογο τυφλών, με κριτήριο την κίνηση των πεζών και την ύπαρξη κοντινών νοσοκομείων, σχολών και δημόσιων υπηρεσιών. Ο σύλλογος ζητούσε το μέτρο εδώ και χρόνια.", "The junctions were chosen together with the local association of the blind, based on pedestrian traffic and the presence of nearby hospitals, colleges and public services. The association had been asking for the measure for years."),
  L("Εκφωνητής", "m", "Παράλληλα, ο δήμος ζητά από τους οδηγούς να μην παρκάρουν πάνω στις λωρίδες με τις ανάγλυφες πλάκες στα πεζοδρόμια, που καθοδηγούν τους τυφλούς πεζούς. Όπως τονίζει, ένα αυτοκίνητο πάνω στη λωρίδα μπορεί να κάνει άχρηστο ολόκληρο το σύστημα.", "At the same time, the municipality is asking drivers not to park on the strips of raised tiles on the pavements that guide blind pedestrians. As it stresses, one car on the strip can make the whole system useless."),
 ],
 "questions": [
  Q("Τι θα δείχνει ο ήχος στα φανάρια;", ["Ότι το φανάρι είναι χαλασμένο", "Ότι οι πεζοί μπορούν να περάσουν με ασφάλεια", "Ότι πλησιάζει λεωφορείο", "Ότι ο δρόμος κλείνει"], 1, "ένας ήχος θα δείχνει ότι μπορούν να περάσουν με ασφάλεια"),
  Q("Για ποιους είναι το κουμπί που δονείται;", ["Για τα παιδιά", "Για τους ποδηλάτες", "Για όσους έχουν και προβλήματα ακοής", "Για τους ηλικιωμένους"], 2, "για όσους έχουν και προβλήματα ακοής"),
  Q("Γιατί θα ρυθμίζεται αυτόματα η ένταση του ήχου;", ["Για να μην ενοχλούνται οι κάτοικοι τη νύχτα", "Για να εξοικονομείται ρεύμα", "Για να ακούγεται από τα αυτοκίνητα", "Για να μη χαλάει το σύστημα"], 0, "ώστε να μην ενοχλούνται οι κάτοικοι τη νύχτα"),
  Q("Τι ζητά ο δήμος από τους οδηγούς;", ["Να οδηγούν πιο αργά", "Να μην κορνάρουν", "Να σταματούν σε κάθε φανάρι", "Να μην παρκάρουν πάνω στις ανάγλυφες λωρίδες"], 3, "να μην παρκάρουν πάνω στις λωρίδες με τις ανάγλυφες πλάκες"),
 ],
 "gloss": {"ηχητικά": "ηχητικός — audible, sound (adj.)", "διασταυρώσεις": "διασταύρωση — junction, crossroads", "όρασης": "όραση — sight, vision", "δονείται": "δονούμαι — to vibrate", "ακοής": "ακοή — hearing", "ένταση": "ένταση — volume; intensity", "ρυθμίζεται": "ρυθμίζομαι — to be adjusted", "σύλλογο": "σύλλογος — association, club", "κριτήριο": "κριτήριο — criterion", "ανάγλυφες": "ανάγλυφος — raised, embossed", "καθοδηγούν": "καθοδηγώ — to guide", "άχρηστο": "άχρηστος — useless"}
})

ITEMS.append({
 "id": "l264-vm-koini-diadromi", "title": "Μήνυμα από τον οδηγό της κοινής διαδρομής για τη συναυλία", "title_en": "A message from the driver of your shared ride to the concert", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει θέση σε αυτοκίνητο μέσω μιας εφαρμογής κοινής διαδρομής, για να πάτε σε μια συναυλία. Ακούτε ένα μήνυμα από τον οδηγό.",
 "script": [
  L("Οδηγός", "m", "Γεια σου, ο Θοδωρής είμαι, ο οδηγός για το Σάββατο, από Λάρισα για Θεσσαλονίκη. Σε παίρνω γιατί αλλάζει λίγο το πρόγραμμα. Αντί για τις τέσσερις, θα ξεκινήσουμε στις τρεις και μισή, γιατί λένε ότι θα έχει πολλή κίνηση στην εθνική λόγω της συναυλίας.", "Hi, it's Thodoris, the driver for Saturday, from Larissa to Thessaloniki. I'm calling because the plan is changing a bit. Instead of four o'clock, we'll set off at half past three, because they say there will be a lot of traffic on the motorway because of the concert."),
  L("Οδηγός", "m", "Το σημείο συνάντησης μένει το ίδιο, έξω από τον σταθμό των τρένων, αλλά θα σταματήσω στην πλευρά με το πάρκινγκ, όχι στην κεντρική είσοδο, γιατί εκεί δεν επιτρέπεται η στάση. Έχω ένα γκρι αυτοκίνητο με μια μπλε σανίδα σέρφινγκ στη σχάρα, δεν θα με χάσεις.", "The meeting point stays the same, outside the railway station, but I'll stop on the side with the car park, not at the main entrance, because stopping isn't allowed there. I have a grey car with a blue surfboard on the roof rack, you won't miss me."),
  L("Οδηγός", "m", "Είμαστε τέσσερις συνολικά, οπότε το πορτμπαγκάζ είναι λίγο γεμάτο· αν γίνεται, φέρε μόνο ένα σακίδιο, όχι βαλίτσα. Τα δώδεκα ευρώ για τα καύσιμα και τα διόδια μπορείς να μου τα δώσεις στο αυτοκίνητο, μετρητά ή μέσω της εφαρμογής, όπως σε βολεύει.", "There are four of us in total, so the boot is a bit full; if possible, bring just a backpack, not a suitcase. You can give me the twelve euros for fuel and tolls in the car, in cash or through the app, whichever suits you."),
  L("Οδηγός", "m", "Για την επιστροφή, φεύγουμε μία ώρα μετά το τέλος της συναυλίας από το ίδιο σημείο όπου θα σας αφήσω. Αν αποφασίσεις να μείνεις το βράδυ στη Θεσσαλονίκη, απλώς στείλε μου ένα μήνυμα, να μη σε περιμένουμε. Τα λέμε το Σάββατο!", "For the return, we leave an hour after the end of the concert from the same spot where I'll drop you off. If you decide to stay the night in Thessaloniki, just send me a message, so we don't wait for you. See you on Saturday!"),
 ],
 "questions": [
  Q("Γιατί αλλάζει η ώρα αναχώρησης;", ["Γιατί ο οδηγός έχει δουλειά", "Γιατί αναμένεται πολλή κίνηση λόγω της συναυλίας", "Γιατί η συναυλία αρχίζει νωρίτερα", "Γιατί θα βρέξει"], 1, "λένε ότι θα έχει πολλή κίνηση στην εθνική λόγω της συναυλίας"),
  Q("Πού ακριβώς θα σταματήσει ο οδηγός;", ["Στην κεντρική είσοδο του σταθμού", "Έξω από το σπίτι σας", "Στην πλευρά του σταθμού με το πάρκινγκ", "Σε ένα βενζινάδικο"], 2, "θα σταματήσω στην πλευρά με το πάρκινγκ"),
  Q("Γιατί σας ζητά να φέρετε μόνο ένα σακίδιο;", ["Γιατί το πορτμπαγκάζ είναι λίγο γεμάτο", "Γιατί στη συναυλία δεν επιτρέπονται βαλίτσες", "Γιατί το αυτοκίνητο είναι μικρό", "Γιατί θα πάρετε το τρένο στην επιστροφή"], 0, "το πορτμπαγκάζ είναι λίγο γεμάτο"),
  Q("Τι πρέπει να κάνετε αν μείνετε το βράδυ στη Θεσσαλονίκη;", ["Να πληρώσετε μόνο τα μισά", "Να βρείτε άλλον οδηγό", "Να τηλεφωνήσετε στην εφαρμογή", "Να στείλετε ένα μήνυμα στον οδηγό"], 3, "απλώς στείλε μου ένα μήνυμα, να μη σε περιμένουμε"),
 ],
 "gloss": {"κοινής διαδρομής": "κοινή διαδρομή — shared ride, car-pooling", "εθνική": "εθνική (οδός) — motorway, national road", "σημείο συνάντησης": "σημείο συνάντησης — meeting point", "στάση": "στάση — stopping; stop", "σανίδα σέρφινγκ": "σανίδα σέρφινγκ — surfboard", "σχάρα": "σχάρα — roof rack; grill", "πορτμπαγκάζ": "πορτμπαγκάζ — (car) boot, trunk", "σακίδιο": "σακίδιο — backpack", "καύσιμα": "καύσιμα — fuel", "διόδια": "διόδια — tolls", "μετρητά": "μετρητά — cash", "βολεύει": "βολεύω — to suit, be convenient"}
})

ITEMS.append({
 "id": "l264-c1-mono-karotsi-souper-market", "title": "Ένα καροτσάκι που κανείς δεν ήθελε να σπρώξει: η ιστορία του καροτσιού του σούπερ μάρκετ", "title_en": "A cart nobody wanted to push: the history of the supermarket trolley", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας ομιλίας σε έναν κύκλο εκδηλώσεων για την ιστορία των καθημερινών αντικειμένων.",
 "script": [
  L("Ομιλήτρια", "f", "Στη δεκαετία του 1930, στις Ηνωμένες Πολιτείες, τα πρώτα σούπερ μάρκετ είχαν ένα πρόβλημα που δεν το είχαν τα παλιά μπακάλικα: ο πελάτης έπαιρνε μόνος του τα προϊόντα από τα ράφια, αλλά σταματούσε να ψωνίζει μόλις γέμιζε το καλάθι του ή κουραζόταν το χέρι του.", "In the 1930s, in the United States, the first supermarkets had a problem that the old grocery shops had not: customers took the products off the shelves themselves, but stopped shopping as soon as their basket was full or their arm got tired."),
  L("Ομιλήτρια", "f", "Ο Σίλβαν Γκόλντμαν, ιδιοκτήτης μιας αλυσίδας καταστημάτων στην Οκλαχόμα, είχε, όπως λέει η ιστορία, μια ιδέα κοιτάζοντας μια πτυσσόμενη καρέκλα: τι θα γινόταν αν έβαζε δύο καλάθια πάνω σε έναν μεταλλικό σκελετό με ρόδες; Το 1937 τα πρώτα καροτσάκια του μπήκαν στα μαγαζιά του.", "Sylvan Goldman, the owner of a chain of stores in Oklahoma, had, as the story goes, an idea while looking at a folding chair: what if he put two baskets on a metal frame with wheels? In 1937 his first trolleys appeared in his shops."),
  L("Ομιλήτρια", "f", "Η αρχή ήταν αποτυχία. Οι άντρες θεωρούσαν ότι ένα καροτσάκι τους έκανε να φαίνονται αδύναμοι, και οι γυναίκες έλεγαν ότι είχαν σπρώξει αρκετά καροτσάκια μωρών στη ζωή τους. Ο Γκόλντμαν προσέλαβε τότε άντρες και γυναίκες κάθε ηλικίας για να κάνουν ότι ψωνίζουν με καροτσάκι, και μια υπάλληλος στην είσοδο τα πρόσφερε με ένα χαμόγελο. Λίγους μήνες αργότερα, όλοι τα ήθελαν.", "The start was a failure. Men felt a trolley made them look weak, and women said they had pushed enough prams in their lives. Goldman then hired men and women of all ages to pretend to shop with trolleys, and an employee at the entrance offered them with a smile. A few months later, everyone wanted one."),
  L("Ομιλήτρια", "f", "Το επόμενο βήμα ήταν το καροτσάκι που μπαίνει το ένα μέσα στο άλλο, για να πιάνει λιγότερο χώρο, και αυτό, σύμφωνα με τα δικαστήρια που έκριναν μια διαμάχη για τα δικαιώματα, δεν ήταν εφεύρεση του Γκόλντμαν αλλά ενός άλλου εφευρέτη. Σήμερα, οι μελετητές του λιανεμπορίου θυμίζουν ότι, όσο μεγαλύτερο είναι το καροτσάκι, τόσο περισσότερα αγοράζουμε, κάτι που οι αλυσίδες το γνωρίζουν πολύ καλά.", "The next step was the trolley that nests one inside the other, to take up less space, and that, according to the courts that ruled on a dispute over the rights, was not Goldman's invention but another inventor's. Today, retail researchers point out that the bigger the trolley, the more we buy, something the chains know very well."),
 ],
 "questions": [
  Q("Ποιο πρόβλημα είχαν τα πρώτα σούπερ μάρκετ;", ["Οι πελάτες έκλεβαν προϊόντα", "Οι πελάτες σταματούσαν να ψωνίζουν όταν γέμιζε ή κουραζόταν το χέρι τους", "Τα ράφια ήταν πολύ ψηλά", "Δεν είχαν αρκετούς υπαλλήλους"], 1, "σταματούσε να ψωνίζει μόλις γέμιζε το καλάθι του ή κουραζόταν το χέρι του"),
  Q("Τι ενέπνευσε, σύμφωνα με την ιστορία, τον Γκόλντμαν;", ["Ένα καροτσάκι μωρού", "Ένα ποδήλατο", "Μια πτυσσόμενη καρέκλα", "Ένα τρένο"], 2, "μια ιδέα κοιτάζοντας μια πτυσσόμενη καρέκλα"),
  Q("Γιατί στην αρχή οι άντρες δεν ήθελαν τα καροτσάκια;", ["Γιατί πίστευαν ότι τους έκαναν να φαίνονται αδύναμοι", "Γιατί ήταν ακριβά", "Γιατί χαλούσαν εύκολα", "Γιατί δεν χωρούσαν στους διαδρόμους"], 0, "Οι άντρες θεωρούσαν ότι ένα καροτσάκι τους έκανε να φαίνονται αδύναμοι"),
  Q("Τι γνωρίζουν πολύ καλά, κατά την ομιλήτρια, οι αλυσίδες;", ["Ότι οι πελάτες προτιμούν τα καλάθια", "Ότι τα καροτσάκια κλέβονται συχνά", "Ότι οι πελάτες ψωνίζουν πιο γρήγορα", "Ότι με μεγαλύτερο καροτσάκι αγοράζουμε περισσότερα"], 3, "όσο μεγαλύτερο είναι το καροτσάκι, τόσο περισσότερα αγοράζουμε"),
 ],
 "gloss": {"μπακάλικα": "μπακάλικο — grocery shop", "ράφια": "ράφι — shelf", "αλυσίδας καταστημάτων": "αλυσίδα καταστημάτων — chain of stores", "πτυσσόμενη": "πτυσσόμενος — folding", "σκελετό": "σκελετός — frame; skeleton", "ρόδες": "ρόδα — wheel", "αδύναμοι": "αδύναμος — weak", "προσέλαβε": "προσλαμβάνω — to hire", "διαμάχη": "διαμάχη — dispute", "δικαιώματα": "δικαίωμα — right (legal)", "εφευρέτη": "εφευρέτης — inventor", "λιανεμπορίου": "λιανεμπόριο — retail trade"}
})

ITEMS.append({
 "id": "l264-c1-int-kairos-ponoi", "title": "Νιώθουν πράγματι κάποιοι τον καιρό στις αρθρώσεις τους; Μια ρευματολόγος απαντά", "title_en": "Can some people really feel the weather in their joints? A rheumatologist answers", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή για την επιστήμη της καθημερινής ζωής.",
 "script": [
  L("Δημοσιογράφος", "m", "Η γιαγιά μου έλεγε «θα βρέξει, με πονάει το γόνατο», και συνήθως έβρεχε. Είναι λαϊκή δοξασία ή υπάρχει κάτι πίσω από αυτό;", "My grandmother used to say 'it's going to rain, my knee hurts', and it usually did rain. Is it a folk belief or is there something behind it?"),
  L("Ρευματολόγος", "f", "Είναι ένα από τα ερωτήματα που ακούω πιο συχνά στο ιατρείο. Πολλοί ασθενείς με αρθρίτιδα ή με παλιούς τραυματισμούς είναι απόλυτα πεπεισμένοι ότι προβλέπουν τον καιρό. Το δύσκολο είναι να το ελέγξεις επιστημονικά, γιατί ο πόνος επηρεάζεται από πάρα πολλά πράγματα: τον ύπνο, τη διάθεση, την κίνηση.", "It's one of the questions I hear most often in my practice. Many patients with arthritis or old injuries are absolutely convinced they can forecast the weather. The difficult part is testing it scientifically, because pain is affected by a great many things: sleep, mood, movement."),
  L("Δημοσιογράφος", "m", "Και τι λένε οι μελέτες;", "And what do the studies say?"),
  L("Ρευματολόγος", "f", "Τα αποτελέσματα είναι ανάμεικτα. Μια μεγάλη βρετανική μελέτη, με χιλιάδες συμμετέχοντες που κατέγραφαν τον πόνο τους κάθε μέρα σε μια εφαρμογή στο κινητό, βρήκε μια μέτρια σχέση: ο πόνος ήταν λίγο εντονότερος τις μέρες με υψηλή υγρασία, χαμηλή ατμοσφαιρική πίεση και δυνατό αέρα. Άλλες έρευνες, όμως, που εξέτασαν εκατομμύρια επισκέψεις σε γιατρούς, δεν βρήκαν καμία σύνδεση με τη βροχή.", "The results are mixed. A large British study, with thousands of participants who recorded their pain every day in a phone app, found a modest relationship: pain was slightly worse on days with high humidity, low atmospheric pressure and strong wind. Other research, however, which examined millions of doctor visits, found no link with rain."),
  L("Δημοσιογράφος", "m", "Και αν υπάρχει σχέση, πώς εξηγείται;", "And if there is a link, how is it explained?"),
  L("Ρευματολόγος", "f", "Η πιο συνηθισμένη υπόθεση είναι ότι, όταν πέφτει η πίεση, οι ιστοί γύρω από μια φλεγμένη άρθρωση διαστέλλονται ελάχιστα και πιέζουν τα νεύρα. Δεν πρέπει όμως να ξεχνάμε και την ψυχολογία: θυμόμαστε τις φορές που το γόνατο «έπεσε μέσα» και ξεχνάμε τις φορές που πόνεσε και έλαμπε ο ήλιος. Γι' αυτό λέω στους ασθενείς μου να κρατούν ημερολόγιο· συχνά εκπλήσσονται με το τι δείχνει.", "The most common hypothesis is that, when pressure drops, the tissues around an inflamed joint expand very slightly and press on the nerves. But we mustn't forget psychology either: we remember the times the knee 'got it right' and forget the times it hurt and the sun was shining. That's why I tell my patients to keep a diary; they are often surprised by what it shows."),
 ],
 "questions": [
  Q("Γιατί είναι δύσκολο να ελεγχθεί επιστημονικά το φαινόμενο;", ["Γιατί οι ασθενείς δεν θέλουν να συμμετάσχουν", "Γιατί ο πόνος επηρεάζεται από πολλά πράγματα", "Γιατί ο καιρός αλλάζει πολύ γρήγορα", "Γιατί δεν υπάρχουν όργανα για να μετρηθεί ο πόνος"], 1, "ο πόνος επηρεάζεται από πάρα πολλά πράγματα"),
  Q("Τι βρήκε η μεγάλη βρετανική μελέτη;", ["Καμία σχέση ανάμεσα στον καιρό και τον πόνο", "Ότι ο πόνος αυξάνεται με τη ζέστη", "Μια μέτρια σχέση με την υγρασία, τη χαμηλή πίεση και τον αέρα", "Ότι η βροχή προκαλεί αρθρίτιδα"], 2, "βρήκε μια μέτρια σχέση … υψηλή υγρασία, χαμηλή ατμοσφαιρική πίεση και δυνατό αέρα"),
  Q("Τι δείχνουν άλλες έρευνες με εκατομμύρια επισκέψεις σε γιατρούς;", ["Καμία σύνδεση με τη βροχή", "Ότι οι επισκέψεις αυξάνονται τον χειμώνα", "Ότι η υγρασία είναι ο βασικός παράγοντας", "Ότι οι ηλικιωμένοι προβλέπουν τον καιρό"], 0, "δεν βρήκαν καμία σύνδεση με τη βροχή"),
  Q("Γιατί η ρευματολόγος συστήνει ημερολόγιο;", ["Για να μετρούν τα φάρμακα", "Για να κανονίζουν τα ραντεβού", "Για να προβλέπουν τον καιρό καλύτερα", "Για να μην παρασύρονται από το ότι θυμόμαστε μόνο τις «επιτυχίες»"], 3, "θυμόμαστε τις φορές που το γόνατο «έπεσε μέσα» και ξεχνάμε τις φορές που πόνεσε"),
 ],
 "gloss": {"δοξασία": "δοξασία — (popular) belief", "αρθρίτιδα": "αρθρίτιδα — arthritis", "τραυματισμούς": "τραυματισμός — injury", "πεπεισμένοι": "πεπεισμένος — convinced", "ανάμεικτα": "ανάμεικτος — mixed", "μέτρια": "μέτριος — modest, moderate", "υγρασία": "υγρασία — humidity", "ατμοσφαιρική πίεση": "ατμοσφαιρική πίεση — atmospheric pressure", "ιστοί": "ιστός — tissue", "φλεγμένη": "φλεγμένος — inflamed", "άρθρωση": "άρθρωση — joint", "διαστέλλονται": "διαστέλλομαι — to expand", "εκπλήσσονται": "εκπλήσσομαι — to be surprised"}
})

rnd = random.Random(264)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-264.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
