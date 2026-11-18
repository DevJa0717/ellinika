# Source for library/listening/listening-246.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l246.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l246-news-orneo-pompos", "title": "Νεαρό όρνιο με δορυφορικό πομπό πέταξε από την Κρήτη ως τη Λιβύη", "title_en": "A young griffon vulture with a satellite tag flew from Crete to Libya", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός περιφερειακού ραδιοφωνικού σταθμού της Κρήτης.",
 "script": [
  L("Εκφωνητής", "m", "Ένα νεαρό όρνιο, που είχε εφοδιαστεί τον Ιούνιο με δορυφορικό πομπό, πέταξε πάνω από το Λιβυκό Πέλαγος και έφτασε ως τις ακτές της Λιβύης. Οι ερευνητές παρακολουθούσαν το ταξίδι του σε πραγματικό χρόνο από τον υπολογιστή τους.", "A young griffon vulture, which was fitted with a satellite transmitter in June, flew over the Libyan Sea and reached the coast of Libya. The researchers followed its journey in real time from their computer."),
  L("Εκφωνητής", "m", "Η διαδρομή πάνω από τη θάλασσα είναι εξαιρετικά επικίνδυνη για τα όρνια, γιατί πετούν κυρίως εκμεταλλευόμενα τα θερμά ρεύματα του αέρα, που σχηματίζονται πάνω από τη στεριά. Πάνω από το νερό πρέπει να χτυπούν συνεχώς τα φτερά τους, και κουράζονται γρήγορα.", "The route over the sea is extremely dangerous for griffon vultures, because they fly mainly by using warm air currents, which form over land. Over water they have to flap their wings constantly, and they tire quickly."),
  L("Εκφωνητής", "m", "Το πουλί έμεινε στη Βόρεια Αφρική περίπου τρεις εβδομάδες και στη συνέχεια επέστρεψε στην Κρήτη, στην ίδια περιοχή όπου είχε γεννηθεί. Οι επιστήμονες λένε ότι τέτοια ταξίδια είναι σπάνια και ότι μάλλον τα κάνουν μόνο τα νεαρά όρνια, που εξερευνούν νέα εδάφη.", "The bird stayed in North Africa for about three weeks and then returned to Crete, to the same area where it had hatched. The scientists say such journeys are rare and that probably only young vultures make them, as they explore new territory."),
  L("Εκφωνητής", "m", "Η Κρήτη φιλοξενεί σήμερα τον μεγαλύτερο πληθυσμό ορνέων στην Ελλάδα. Οι ερευνητές ζητούν από τους κτηνοτρόφους να μη χρησιμοποιούν δηλητηριασμένα δολώματα, που είναι η πιο σοβαρή απειλή για τα πουλιά αυτά.", "Crete is today home to the largest population of griffon vultures in Greece. The researchers are asking livestock farmers not to use poisoned baits, which are the most serious threat to these birds."),
 ],
 "questions": [
  Q("Πώς παρακολουθούσαν οι ερευνητές το ταξίδι του ορνέου;", ["Με κιάλια από ένα πλοίο", "Σε πραγματικό χρόνο από τον υπολογιστή, χάρη στον δορυφορικό πομπό", "Από φωτογραφίες ψαράδων", "Με ένα αεροπλάνο"], 1, "Οι ερευνητές παρακολουθούσαν το ταξίδι του σε πραγματικό χρόνο από τον υπολογιστή τους"),
  Q("Γιατί είναι επικίνδυνη για τα όρνια η διαδρομή πάνω από τη θάλασσα;", ["Γιατί εκεί κυνηγούν οι γλάροι", "Γιατί δεν υπάρχουν θερμά ρεύματα και πρέπει να χτυπούν συνεχώς τα φτερά τους", "Γιατί η θάλασσα είναι πολύ κρύα", "Γιατί πετούν πολύ χαμηλά"], 1, "Πάνω από το νερό πρέπει να χτυπούν συνεχώς τα φτερά τους, και κουράζονται γρήγορα"),
  Q("Τι έκανε το όρνιο μετά από τρεις εβδομάδες;", ["Έμεινε για πάντα στη Λιβύη", "Επέστρεψε στην περιοχή της Κρήτης όπου είχε γεννηθεί", "Πέταξε στην Κύπρο", "Χάθηκε το σήμα του"], 1, "επέστρεψε στην Κρήτη, στην ίδια περιοχή όπου είχε γεννηθεί"),
  Q("Ποια είναι η πιο σοβαρή απειλή για τα όρνια, σύμφωνα με την είδηση;", ["Οι ανεμογεννήτριες", "Τα δηλητηριασμένα δολώματα", "Η έλλειψη τροφής", "Οι τουρίστες"], 1, "δηλητηριασμένα δολώματα, που είναι η πιο σοβαρή απειλή"),
 ],
 "gloss": {"όρνιο": "όρνιο — griffon vulture", "πομπό": "πομπός — transmitter", "εφοδιαστεί": "εφοδιάζομαι — to be fitted, equipped", "Λιβυκό Πέλαγος": "Λιβυκό Πέλαγος — the Libyan Sea", "θερμά ρεύματα": "θερμό ρεύμα — thermal (air current)", "εκμεταλλευόμενα": "εκμεταλλεύομαι — to exploit, make use of", "εξερευνούν": "εξερευνώ — to explore", "εδάφη": "έδαφος — territory, ground", "κτηνοτρόφους": "κτηνοτρόφος — livestock farmer", "δηλητηριασμένα": "δηλητηριασμένος — poisoned", "δολώματα": "δόλωμα — bait"},
})

ITEMS.append({
 "id": "l246-vm-antikeri-komota", "title": "Μήνυμα από τον αντικέρ: «Η κομότα σας δεν είναι αυτό που νομίζατε»", "title_en": "A message from the antiques dealer: 'Your chest of drawers isn't what you thought'", "type": "voicemail", "level": "B2",
 "context_el": "Πήγατε σε ένα κατάστημα με αντίκες μια παλιά κομότα που κληρονομήσατε, για να σας πουν πόσο αξίζει. Ακούτε ένα μήνυμα που σας άφησε ο αντικέρ στον τηλεφωνητή.",
 "script": [
  L("Αντικέρ", "m", "Καλησπέρα σας, ο Φίλιππος είμαι, από το κατάστημα με τις αντίκες στην Πλάκα. Εξέτασα προσεκτικά την κομότα σας. Λυπάμαι, αλλά δεν είναι του 19ου αιώνα, όπως πίστευε η οικογένειά σας. Είναι μια πολύ καλή απομίμηση, φτιαγμένη μάλλον στη δεκαετία του 1950.", "Good evening, it's Filippos, from the antiques shop in Plaka. I've examined your chest of drawers carefully. I'm sorry, but it isn't from the 19th century, as your family believed. It's a very good imitation, probably made in the 1950s."),
  L("Αντικέρ", "m", "Το κατάλαβα από τις βίδες και από τον τρόπο που είναι ενωμένα τα συρτάρια: τα μηχανήματα που τα έκοψαν δεν υπήρχαν πριν από τον πόλεμο. Παρ' όλα αυτά, το ξύλο είναι καρυδιά, μασίφ, και η δουλειά είναι προσεγμένη. Ένας ξυλουργός της εποχής ήξερε πολύ καλά τι έκανε.", "I could tell from the screws and from the way the drawers are joined: the machines that cut them didn't exist before the war. Nevertheless, the wood is solid walnut, and the workmanship is careful. A carpenter of that time knew very well what he was doing."),
  L("Αντικέρ", "m", "Η αξία της, στην κατάσταση που είναι, είναι γύρω στα τριακόσια ευρώ. Αν τη συντηρήσουμε, δηλαδή καθάρισμα, κερί και καινούργια πόμολα στο ίδιο στιλ, θα κοστίσει περίπου εκατόν πενήντα, αλλά θα είναι ένα πολύ ωραίο έπιπλο για το σπίτι σας. Εγώ δεν θα σας συμβούλευα να την πουλήσετε.", "Its value, in its present condition, is around three hundred euros. If we restore it, that is cleaning, wax and new knobs in the same style, it will cost about a hundred and fifty, but it will be a very nice piece of furniture for your home. I wouldn't advise you to sell it."),
  L("Αντικέρ", "m", "Και κάτι ακόμα: στο πίσω μέρος του κάτω συρταριού βρήκα κολλημένο έναν φάκελο με παλιά γράμματα. Δεν τον άνοιξα. Σας τον κρατάω σε ένα συρτάρι του γραφείου μου, για να τον πάρετε όταν περάσετε. Καλό βράδυ.", "And one more thing: at the back of the bottom drawer I found an envelope of old letters stuck there. I didn't open it. I'm keeping it for you in a drawer of my desk, so you can collect it when you drop by. Good evening."),
 ],
 "questions": [
  Q("Τι ανακάλυψε ο αντικέρ για την κομότα;", ["Ότι είναι του 18ου αιώνα", "Ότι είναι μια καλή απομίμηση, μάλλον της δεκαετίας του 1950", "Ότι είναι ιταλική", "Ότι είναι κλεμμένη"], 1, "Είναι μια πολύ καλή απομίμηση, φτιαγμένη μάλλον στη δεκαετία του 1950"),
  Q("Πώς το κατάλαβε;", ["Από μια υπογραφή στο ξύλο", "Από τις βίδες και τον τρόπο που είναι ενωμένα τα συρτάρια", "Από το χρώμα", "Από μια παλιά απόδειξη"], 1, "Το κατάλαβα από τις βίδες και από τον τρόπο που είναι ενωμένα τα συρτάρια"),
  Q("Τι συμβουλεύει ο αντικέρ;", ["Να την πουλήσουν αμέσως", "Να τη συντηρήσουν και να την κρατήσουν", "Να τη δωρίσουν σε ένα μουσείο", "Να τη βάψουν άσπρη"], 1, "Εγώ δεν θα σας συμβούλευα να την πουλήσετε"),
  Q("Τι βρήκε στο κάτω συρτάρι;", ["Χρήματα", "Έναν φάκελο με παλιά γράμματα", "Ένα κόσμημα", "Μια παλιά φωτογραφία"], 1, "βρήκα κολλημένο έναν φάκελο με παλιά γράμματα"),
 ],
 "gloss": {"αντικέρ": "αντικέρ — antiques dealer", "κομότα": "κομότα — chest of drawers", "αντίκες": "αντίκα — antique", "απομίμηση": "απομίμηση — imitation, copy", "βίδες": "βίδα — screw", "συρτάρια": "συρτάρι — drawer", "μασίφ": "μασίφ — solid (wood)", "προσεγμένη": "προσεγμένος — careful, well-made", "συντηρήσουμε": "συντηρώ — to restore, maintain", "κερί": "κερί — wax", "πόμολα": "πόμολο — knob, handle", "φάκελο": "φάκελος — envelope"},
})

ITEMS.append({
 "id": "l246-c1-mono-koumpi", "title": "Από στολίδι σε εργαλείο: η ιστορία του κουμπιού", "title_en": "From ornament to tool: the history of the button", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ιστορικό σε μια ραδιοφωνική εκπομπή για τα αντικείμενα της καθημερινής ζωής.",
 "script": [
  L("Ιστορικός", "m", "Τα κουμπιά είναι πολύ παλιότερα από τις κουμπότρυπες. Αρχαιολόγοι έχουν βρει μικρούς δίσκους από όστρακο, κόκαλο ή μέταλλο, με μια τρύπα στη μέση, που είναι χιλιάδες χρόνια παλιοί. Όμως οι περισσότεροι από αυτούς ήταν μάλλον στολίδια, που ράβονταν πάνω στα ρούχα, και όχι κουμπιά που κλείνουν ένα ρούχο.", "Buttons are much older than buttonholes. Archaeologists have found small discs of shell, bone or metal, with a hole in the middle, that are thousands of years old. But most of them were probably ornaments sewn onto clothes, not buttons that close a garment."),
  L("Ιστορικός", "m", "Για αιώνες τα ρούχα στερεώνονταν με πόρπες, ζώνες και κορδόνια. Η κουμπότρυπα, που μοιάζει τόσο αυτονόητη, εμφανίστηκε στην Ευρώπη μόλις τον 13ο αιώνα. Η αλλαγή ήταν μεγάλη: τα ρούχα μπορούσαν πια να εφαρμόζουν στενά πάνω στο σώμα, και η μόδα άλλαξε ριζικά.", "For centuries clothes were fastened with brooches, belts and laces. The buttonhole, which seems so obvious, appeared in Europe only in the 13th century. The change was huge: clothes could now fit tightly to the body, and fashion changed radically."),
  L("Ιστορικός", "m", "Σύντομα τα κουμπιά έγιναν σύμβολο πλούτου. Οι ευγενείς φορούσαν δεκάδες, ακόμη και εκατοντάδες, από χρυσό, ασήμι ή πολύτιμους λίθους. Λέγεται ότι ένας Γάλλος βασιλιάς του 16ου αιώνα παρήγγειλε χιλιάδες χρυσά κουμπιά για ένα μόνο ένδυμα, αν και τέτοιες ιστορίες πρέπει να τις ακούμε με κάποια επιφύλαξη.", "Soon buttons became a symbol of wealth. Nobles wore dozens, even hundreds, made of gold, silver or precious stones. It is said that a 16th-century French king ordered thousands of gold buttons for a single garment, although we should take such stories with some caution."),
  L("Ιστορικός", "m", "Κι ένα μυστήριο που μας απασχολεί ακόμη: γιατί τα αντρικά ρούχα κουμπώνουν από τη μία πλευρά και τα γυναικεία από την άλλη; Έχουν προταθεί πολλές εξηγήσεις, για παράδειγμα ότι τις πλούσιες κυρίες τις έντυναν υπηρέτριες, που στέκονταν απέναντί τους. Καμία όμως δεν έχει αποδειχθεί.", "And a mystery that still puzzles us: why do men's clothes button on one side and women's on the other? Many explanations have been proposed, for example that wealthy ladies were dressed by maids standing opposite them. But none has been proven."),
 ],
 "questions": [
  Q("Τι ήταν μάλλον οι πολύ παλιοί δίσκοι με τρύπα που βρήκαν οι αρχαιολόγοι;", ["Νομίσματα", "Στολίδια που ράβονταν πάνω στα ρούχα", "Κουμπιά για παλτά", "Παιχνίδια"], 1, "οι περισσότεροι από αυτούς ήταν μάλλον στολίδια, που ράβονταν πάνω στα ρούχα"),
  Q("Τι άλλαξε όταν εμφανίστηκε η κουμπότρυπα;", ["Τα ρούχα έγιναν φθηνότερα", "Τα ρούχα μπορούσαν να εφαρμόζουν στενά πάνω στο σώμα", "Οι άνθρωποι σταμάτησαν να φορούν ζώνες", "Τα κουμπιά έγιναν πλαστικά"], 1, "τα ρούχα μπορούσαν πια να εφαρμόζουν στενά πάνω στο σώμα"),
  Q("Πώς κρίνει ο ιστορικός την ιστορία για τα χρυσά κουμπιά του Γάλλου βασιλιά;", ["Ως απόλυτα αποδεδειγμένη", "Λέει ότι πρέπει να την ακούμε με κάποια επιφύλαξη", "Λέει ότι είναι σίγουρα ψέματα", "Δεν σχολιάζει"], 1, "τέτοιες ιστορίες πρέπει να τις ακούμε με κάποια επιφύλαξη"),
  Q("Τι ισχύει για τις εξηγήσεις σχετικά με την πλευρά που κουμπώνουν τα ρούχα;", ["Μία έχει αποδειχθεί", "Καμία δεν έχει αποδειχθεί", "Δεν έχει προταθεί καμία", "Όλες είναι σωστές"], 1, "Καμία όμως δεν έχει αποδειχθεί"),
 ],
 "gloss": {"κουμπότρυπες": "κουμπότρυπα — buttonhole", "δίσκους": "δίσκος — disc", "όστρακο": "όστρακο — shell", "στολίδια": "στολίδι — ornament", "στερεώνονταν": "στερεώνομαι — to be fastened", "κορδόνια": "κορδόνι — lace, cord", "αυτονόητη": "αυτονόητος — self-evident, obvious", "εφαρμόζουν": "εφαρμόζω — to fit (closely)", "ριζικά": "ριζικά — radically", "ευγενείς": "ευγενής — noble(man)", "ένδυμα": "ένδυμα — garment", "επιφύλαξη": "επιφύλαξη — reservation, caution", "κουμπώνουν": "κουμπώνω — to button"},
})

ITEMS.append({
 "id": "l246-c1-int-astroviologos", "title": "Μια αστροβιολόγος για τη ζωή που μπορεί να κρύβεται κάτω από τους πάγους", "title_en": "An astrobiologist on the life that may be hiding beneath the ice", "type": "interview", "level": "C1",
 "context_el": "Μια αστροβιολόγος, δηλαδή μια επιστήμονας που μελετά αν μπορεί να υπάρχει ζωή έξω από τη Γη, μιλά σε μια ραδιοφωνική εκπομπή για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "m", "Όταν σκεφτόμαστε ζωή σε άλλους κόσμους, οι περισσότεροι φανταζόμαστε μικρά πράσινα ανθρωπάκια. Εσείς τι ψάχνετε;", "When we think of life on other worlds, most of us imagine little green men. What are you looking for?"),
  L("Αστροβιολόγος", "f", "Κάτι πολύ πιο ταπεινό: μικροοργανισμούς. Στη Γη έχουμε βρει ζωή σε μέρη που κάποτε θεωρούσαμε αδύνατα: σε θερμές πηγές του βυθού, όπου το νερό ξεπερνά τους εκατό βαθμούς, σε πολύ αλμυρές λίμνες, ακόμη και βαθιά μέσα στα πετρώματα. Αυτοί οι «εξτρεμόφιλοι» οργανισμοί μάς έμαθαν ότι η ζωή είναι πολύ πιο ανθεκτική απ' όσο πιστεύαμε.", "Something much more humble: micro-organisms. On Earth we have found life in places we once considered impossible: in hot springs on the seabed, where the water exceeds a hundred degrees, in very salty lakes, even deep inside rocks. These 'extremophile' organisms taught us that life is much tougher than we thought."),
  L("Δημοσιογράφος", "m", "Και πού στο ηλιακό μας σύστημα έχει νόημα να ψάξουμε;", "And where in our solar system does it make sense to look?"),
  L("Αστροβιολόγος", "f", "Εκτός από τον Άρη, τα πιο ενδιαφέροντα μέρη είναι μερικοί δορυφόροι του Δία και του Κρόνου. Η Ευρώπη, δορυφόρος του Δία, και ο Εγκέλαδος, δορυφόρος του Κρόνου, φαίνεται ότι έχουν κάτω από τον πάγο τους ωκεανούς από υγρό νερό. Από τον Εγκέλαδο, μάλιστα, ένα διαστημόπλοιο κατέγραψε πίδακες νερού να εκτινάσσονται στο διάστημα, και πέρασε μέσα από αυτούς.", "Apart from Mars, the most interesting places are some moons of Jupiter and Saturn. Europa, a moon of Jupiter, and Enceladus, a moon of Saturn, appear to have oceans of liquid water beneath their ice. From Enceladus, in fact, a spacecraft recorded jets of water shooting out into space, and flew through them."),
  L("Δημοσιογράφος", "m", "Αν βρίσκατε ζωή εκεί, τι θα σήμαινε;", "If you found life there, what would it mean?"),
  L("Αστροβιολόγος", "f", "Αν βρίσκαμε ζωή που γεννήθηκε ανεξάρτητα, σε δύο σημεία μόνο του δικού μας ηλιακού συστήματος, θα ήταν πολύ πιθανό η ζωή να είναι κάτι συνηθισμένο στο σύμπαν. Πρέπει όμως να είμαστε προσεκτικοί: κάθε «ένδειξη» πρέπει να ελεγχθεί αυστηρά, γιατί υπάρχουν και χημικές διεργασίες χωρίς ζωή που μπορούν να μας ξεγελάσουν.", "If we found life that arose independently, in two places in our own solar system alone, it would be very likely that life is something common in the universe. But we must be careful: every 'sign' has to be checked strictly, because there are also chemical processes without life that can fool us."),
 ],
 "questions": [
  Q("Τι ψάχνει κυρίως η αστροβιολόγος;", ["Νοήμονα όντα", "Μικροοργανισμούς", "Αρχαίους πολιτισμούς", "Νέους πλανήτες"], 1, "Κάτι πολύ πιο ταπεινό: μικροοργανισμούς"),
  Q("Τι μας έμαθαν οι «εξτρεμόφιλοι» οργανισμοί;", ["Ότι η ζωή υπάρχει μόνο σε ήπιες συνθήκες", "Ότι η ζωή είναι πολύ πιο ανθεκτική απ' όσο πιστεύαμε", "Ότι δεν υπάρχει ζωή στον βυθό", "Ότι η ζωή ήρθε από το διάστημα"], 1, "η ζωή είναι πολύ πιο ανθεκτική απ' όσο πιστεύαμε"),
  Q("Γιατί ενδιαφέρουν την επιστήμη η Ευρώπη και ο Εγκέλαδος;", ["Γιατί έχουν ατμόσφαιρα σαν της Γης", "Γιατί φαίνεται ότι έχουν ωκεανούς από υγρό νερό κάτω από τον πάγο", "Γιατί είναι πολύ ζεστοί", "Γιατί είναι οι πιο κοντινοί στη Γη"], 1, "φαίνεται ότι έχουν κάτω από τον πάγο τους ωκεανούς από υγρό νερό"),
  Q("Γιατί πρέπει να είναι προσεκτικοί οι επιστήμονες με κάθε «ένδειξη»;", ["Γιατί τα διαστημόπλοια χαλάνε συχνά", "Γιατί χημικές διεργασίες χωρίς ζωή μπορούν να τους ξεγελάσουν", "Γιατί το κοινό δεν ενδιαφέρεται", "Γιατί οι μετρήσεις είναι πολύ ακριβές"], 1, "υπάρχουν και χημικές διεργασίες χωρίς ζωή που μπορούν να μας ξεγελάσουν"),
 ],
 "gloss": {"αστροβιολόγος": "αστροβιολόγος — astrobiologist", "ταπεινό": "ταπεινός — humble", "μικροοργανισμούς": "μικροοργανισμός — micro-organism", "πετρώματα": "πέτρωμα — rock (geology)", "εξτρεμόφιλοι": "εξτρεμόφιλος — extremophile", "ανθεκτική": "ανθεκτικός — tough, resistant", "δορυφόροι": "δορυφόρος — moon, satellite", "πίδακες": "πίδακας — jet", "εκτινάσσονται": "εκτινάσσομαι — to shoot out, be ejected", "διαστημόπλοιο": "διαστημόπλοιο — spacecraft", "ένδειξη": "ένδειξη — sign, indication", "διεργασίες": "διεργασία — process", "ξεγελάσουν": "ξεγελώ — to fool, deceive"},
})
rnd = random.Random(246)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-246.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
