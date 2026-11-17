# Source for library/listening/listening-87.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l87.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l87-ann-kataigida", "title": "Καταιγίδα στο φεστιβάλ", "title_en": "A storm at the festival", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα υπαίθριο μουσικό φεστιβάλ σε ένα πάρκο. Ξαφνικά ακούτε μια ανακοίνωση από τη σκηνή.",
 "script": [
  L("Παρουσιαστής", "m", "Παρακαλώ, λίγη προσοχή. Σύμφωνα με την Πολιτική Προστασία, μια ισχυρή καταιγίδα με κεραυνούς και δυνατούς ανέμους πλησιάζει την περιοχή και αναμένεται να φτάσει εδώ σε περίπου είκοσι λεπτά. Για την ασφάλειά σας, το πρόγραμμα της βραδιάς διακόπτεται.", "Your attention, please. According to Civil Protection, a strong storm with lightning and high winds is approaching the area and is expected to arrive here in about twenty minutes. For your safety, tonight's programme is suspended."),
  L("Παρουσιαστής", "m", "Παρακαλούμε απομακρυνθείτε από τη σκηνή, τα ψηλά δέντρα και τις μεταλλικές κατασκευές. Μην τρέχετε. Όσοι δεν μπορούν να φύγουν αμέσως μπορούν να προστατευτούν στο κλειστό γυμναστήριο του σχολείου, απέναντι από την κεντρική πύλη. Οι εθελοντές με τα πορτοκαλί μπλουζάκια θα σας δείξουν τον δρόμο.", "Please move away from the stage, the tall trees and the metal structures. Don't run. Anyone who can't leave straight away can take shelter in the school's indoor gym, opposite the main gate. Volunteers in orange T-shirts will show you the way."),
  L("Παρουσιαστής", "m", "Οι συναυλίες που δεν πραγματοποιήθηκαν απόψε θα γίνουν αύριο, από τις επτά το απόγευμα. Τα αποψινά εισιτήρια ισχύουν και για αύριο· κρατήστε τα. Όσοι δεν μπορούν να έρθουν αύριο θα πάρουν πίσω τα χρήματά τους από την ιστοσελίδα του φεστιβάλ. Ευχαριστούμε για την κατανόηση.", "The concerts that didn't take place tonight will be held tomorrow, from seven in the evening. Tonight's tickets are also valid for tomorrow; keep them. Anyone who can't come tomorrow will get their money back through the festival website. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί διακόπτεται το πρόγραμμα;", ["Λόγω τεχνικού προβλήματος", "Γιατί πλησιάζει μια ισχυρή καταιγίδα", "Γιατί αρρώστησε ένας τραγουδιστής", "Γιατί υπάρχει πολύς κόσμος"], 1, "μια ισχυρή καταιγίδα με κεραυνούς και δυνατούς ανέμους πλησιάζει την περιοχή"),
  Q("Πού μπορούν να προστατευτούν όσοι δεν φεύγουν αμέσως;", ["Κάτω από τα δέντρα", "Πίσω από τη σκηνή", "Στο κλειστό γυμναστήριο του σχολείου", "Στα αυτοκίνητά τους"], 2, "μπορούν να προστατευτούν στο κλειστό γυμναστήριο του σχολείου"),
  Q("Τι πρέπει να κάνουν όσοι έχουν εισιτήριο;", ["Να το πετάξουν", "Να το κρατήσουν, γιατί ισχύει και για αύριο", "Να το αλλάξουν στο ταμείο απόψε", "Να το δώσουν στους εθελοντές"], 1, "Τα αποψινά εισιτήρια ισχύουν και για αύριο· κρατήστε τα"),
 ],
 "gloss": {"υπαίθριο": "υπαίθριος — open-air", "Πολιτική Προστασία": "Πολιτική Προστασία — Civil Protection", "καταιγίδα": "καταιγίδα — storm", "κεραυνούς": "κεραυνός — lightning bolt", "αναμένεται": "αναμένεται — is expected", "διακόπτεται": "διακόπτομαι — to be interrupted, suspended", "απομακρυνθείτε": "απομακρύνομαι — to move away", "κατασκευές": "κατασκευή — structure", "προστατευτούν": "προστατεύομαι — to take shelter, protect oneself", "πραγματοποιήθηκαν": "πραγματοποιούμαι — to take place", "κατανόηση": "κατανόηση — understanding"},
})
ITEMS.append({
 "id": "l87-vm-diarroi-nerou", "title": "Νερό στο ταβάνι του γείτονα", "title_en": "Water on the neighbour's ceiling", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στο κινητό σας από τον γείτονα που μένει στο διαμέρισμα κάτω από το δικό σας.",
 "script": [
  L("Γείτονας", "m", "Καλησπέρα, ο Παύλος είμαι, από τον δεύτερο, ακριβώς από κάτω σας. Συγγνώμη που σας ενοχλώ, αλλά από το μεσημέρι στάζει νερό από το ταβάνι του μπάνιου μου. Στην αρχή ήταν λίγες σταγόνες, τώρα έχει γίνει μια μεγάλη κηλίδα και φοβάμαι μήπως πέσουν οι σοβάδες.", "Good evening, it's Pavlos, from the second floor, directly below you. Sorry to bother you, but since midday water has been dripping from my bathroom ceiling. At first it was a few drops; now it's become a big patch and I'm afraid the plaster might come down."),
  L("Γείτονας", "m", "Φαντάζομαι ότι κάτι συμβαίνει με κάποιον σωλήνα στο δικό σας μπάνιο. Επειδή δεν σας βρήκα στο σπίτι, σας παρακαλώ, μόλις ακούσετε το μήνυμα, κλείστε τον γενικό διακόπτη του νερού. Είναι στο ντουλάπι κάτω από τον νεροχύτη της κουζίνας, στο βάθος.", "I imagine something's wrong with a pipe in your bathroom. As I didn't find you at home, please, as soon as you hear this message, turn off the main water valve. It's in the cupboard under the kitchen sink, at the back."),
  L("Γείτονας", "m", "Έχω ήδη μιλήσει με έναν υδραυλικό που ξέρω· μπορεί να έρθει αύριο στις εννιά το πρωί, αν μας ανοίξετε. Αν προτιμάτε δικό σας τεχνικό, κανένα πρόβλημα, απλώς πείτε μου. Και κάτι ακόμα: ενημερώστε την ασφαλιστική σας εταιρεία, γιατί ίσως χρειαστεί να βάψω το ταβάνι. Πάρτε με όποτε μπορείτε. Ευχαριστώ.", "I've already spoken to a plumber I know; he can come tomorrow at nine in the morning, if you let us in. If you'd rather have your own technician, no problem, just tell me. And one more thing: let your insurance company know, because I might need to repaint the ceiling. Call me whenever you can. Thanks."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα;", ["Δεν έχει νερό στο σπίτι του", "Στάζει νερό από το ταβάνι του μπάνιου του", "Πλημμύρισε η κουζίνα του", "Χάλασε ο θερμοσίφωνας"], 1, "στάζει νερό από το ταβάνι του μπάνιου μου"),
  Q("Πού βρίσκεται ο γενικός διακόπτης του νερού;", ["Στο μπάνιο", "Στην ταράτσα", "Στο ντουλάπι κάτω από τον νεροχύτη της κουζίνας", "Στην είσοδο της πολυκατοικίας"], 2, "Είναι στο ντουλάπι κάτω από τον νεροχύτη της κουζίνας"),
  Q("Γιατί ζητά να ενημερωθεί η ασφαλιστική εταιρεία;", ["Γιατί θα πληρώσει τον υδραυλικό", "Γιατί ίσως χρειαστεί να βάψει το ταβάνι", "Γιατί το ζητάει ο διαχειριστής", "Γιατί είναι υποχρεωτικό από τον νόμο"], 1, "γιατί ίσως χρειαστεί να βάψω το ταβάνι"),
 ],
 "gloss": {"ταβάνι": "ταβάνι — ceiling", "στάζει": "στάζω — to drip", "σταγόνες": "σταγόνα — drop", "κηλίδα": "κηλίδα — patch, stain", "σοβάδες": "σοβάς — plaster", "σωλήνα": "σωλήνας — pipe", "γενικό διακόπτη": "γενικός διακόπτης — main valve, main switch", "νεροχύτη": "νεροχύτης — sink", "υδραυλικό": "υδραυλικός — plumber", "ασφαλιστική": "ασφαλιστική (εταιρεία) — insurance company"},
})
ITEMS.append({
 "id": "l87-dia-adeia-diamonis", "title": "Ανανέωση της άδειας διαμονής", "title_en": "Renewing a residence permit", "type": "dialogue", "level": "B2",
 "context_el": "Μια νεαρή γυναίκα από το εξωτερικό πηγαίνει σε μια υπηρεσία αλλοδαπών για να ανανεώσει την άδεια διαμονής της.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα. Έχετε κλείσει ραντεβού;", "Good morning. Have you booked an appointment?"),
  L("Αιτούσα", "f", "Ναι, για τις δέκα και μισή. Η άδεια διαμονής μου λήγει τον άλλο μήνα και θέλω να την ανανεώσω. Έφερα το διαβατήριο, δύο φωτογραφίες και τη βεβαίωση από τη δουλειά μου.", "Yes, for half past ten. My residence permit expires next month and I want to renew it. I've brought my passport, two photographs and the certificate from my job."),
  L("Υπάλληλος", "m", "Ωραία. Χρειάζομαι επίσης την ασφαλιστική σας ενημερότητα και το αποδεικτικό ότι πληρώσατε το παράβολο. Το έχετε πληρώσει;", "Good. I also need your social insurance certificate and the proof that you've paid the fee. Have you paid it?"),
  L("Αιτούσα", "f", "Ωχ, όχι. Νόμιζα ότι το πληρώνω εδώ.", "Oh, no. I thought I'd pay it here."),
  L("Υπάλληλος", "m", "Όχι, πληρώνεται ηλεκτρονικά ή σε τράπεζα. Μπορείτε να το κάνετε από το κινητό σας τώρα, είναι πέντε λεπτά. Μόλις μου δείξετε την απόδειξη, θα καταθέσουμε την αίτηση και θα σας δώσω μια βεβαίωση κατάθεσης.", "No, it's paid online or at a bank. You can do it from your phone now; it takes five minutes. As soon as you show me the receipt, we'll submit the application and I'll give you a certificate of submission."),
  L("Αιτούσα", "f", "Και μέχρι να βγει η καινούργια άδεια; Τον Δεκέμβριο θέλω να πάω στους γονείς μου.", "And until the new permit comes out? In December I want to go and see my parents."),
  L("Υπάλληλος", "m", "Η βεβαίωση κατάθεσης αποδεικνύει ότι η διαμονή σας είναι νόμιμη. Για ταξίδια στο εξωτερικό, όμως, να έχετε πάντα μαζί και την παλιά άδεια, και ρωτήστε πριν φύγετε για τους κανόνες της χώρας που επισκέπτεστε. Η νέα άδεια συνήθως βγαίνει σε δύο με τρεις μήνες, και θα σας στείλουμε μήνυμα.", "The certificate of submission proves that your residence is legal. For travel abroad, though, always carry the old permit too, and before you leave ask about the rules of the country you're visiting. The new permit usually comes out in two to three months, and we'll send you a message."),
 ],
 "questions": [
  Q("Τι ξέχασε να κάνει η αιτούσα;", ["Να κλείσει ραντεβού", "Να φέρει φωτογραφίες", "Να πληρώσει το παράβολο", "Να φέρει το διαβατήριο"], 2, "Νόμιζα ότι το πληρώνω εδώ"),
  Q("Πώς μπορεί να πληρώσει το παράβολο;", ["Μόνο με μετρητά στο γκισέ", "Ηλεκτρονικά ή σε τράπεζα", "Με επιταγή", "Στο ταχυδρομείο"], 1, "πληρώνεται ηλεκτρονικά ή σε τράπεζα"),
  Q("Σε πόσο καιρό βγαίνει συνήθως η νέα άδεια;", ["Σε μία εβδομάδα", "Σε δύο με τρεις μήνες", "Σε έναν χρόνο", "Την ίδια μέρα"], 1, "Η νέα άδεια συνήθως βγαίνει σε δύο με τρεις μήνες"),
 ],
 "gloss": {"υπηρεσία αλλοδαπών": "υπηρεσία αλλοδαπών — immigration office", "άδεια διαμονής": "άδεια διαμονής — residence permit", "λήγει": "λήγω — to expire", "βεβαίωση": "βεβαίωση — certificate", "ασφαλιστική σας ενημερότητα": "ασφαλιστική ενημερότητα — certificate of paid social insurance", "αποδεικτικό": "αποδεικτικό — proof", "παράβολο": "παράβολο — (government) fee", "καταθέσουμε": "καταθέτω — to submit", "αίτηση": "αίτηση — application", "βεβαίωση κατάθεσης": "βεβαίωση κατάθεσης — certificate of submission", "νόμιμη": "νόμιμος — legal"},
})
ITEMS.append({
 "id": "l87-int-fotografos-agrias-zois", "title": "Η φωτογράφος της άγριας ζωής", "title_en": "The wildlife photographer", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή για τη φύση, ένας δημοσιογράφος μιλά με μια φωτογράφο που φωτογραφίζει άγρια ζώα στην Ελλάδα.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Αναστασίου, οι φωτογραφίες σας με τις φώκιες του Αιγαίου έχουν κάνει τον γύρο του κόσμου. Πόσο χρόνο χρειάζεται μια τέτοια φωτογραφία;", "Ms Anastasiou, your photographs of the Aegean seals have been all over the world. How much time does a photograph like that take?"),
  L("Φωτογράφος", "f", "Περισσότερο απ’ όσο φαντάζεστε. Για τη φωτογραφία με τη μητέρα φώκια και το μικρό της, περίμενα σε ένα κρυφό σημείο στα βράχια σχεδόν τρεις εβδομάδες, έξι με οχτώ ώρες τη μέρα. Τις περισσότερες μέρες δεν έβλεπα απολύτως τίποτα.", "More than you imagine. For the photograph of the mother seal and her pup, I waited at a hidden spot on the rocks for almost three weeks, six to eight hours a day. Most days I saw absolutely nothing."),
  L("Δημοσιογράφος", "m", "Δεν βαριέστε;", "Don't you get bored?"),
  L("Φωτογράφος", "f", "Καθόλου. Η αναμονή είναι μέρος της δουλειάς. Μαθαίνεις τον ρυθμό του τόπου: πότε φυσάει, πότε περνάνε οι ψαράδες, πότε βγαίνουν τα πουλιά. Και όταν επιτέλους εμφανιστεί το ζώο, έχεις μόνο λίγα δευτερόλεπτα. Αν εκείνη τη στιγμή είσαι κουρασμένος ή αφηρημένος, τα χάνεις όλα.", "Not at all. Waiting is part of the job. You learn the rhythm of the place: when the wind blows, when the fishermen go by, when the birds come out. And when the animal finally appears, you have only a few seconds. If at that moment you're tired or distracted, you lose everything."),
  L("Δημοσιογράφος", "m", "Υπάρχουν κανόνες που ακολουθείτε;", "Are there rules you follow?"),
  L("Φωτογράφος", "f", "Ο πρώτος κανόνας είναι ότι το ζώο είναι πιο σημαντικό από τη φωτογραφία. Δεν πλησιάζω ποτέ σε φωλιές, δεν χρησιμοποιώ τροφή για να προσελκύσω ζώα και, αν δω ότι ένα ζώο αγχώνεται, φεύγω αμέσως. Ειδικά οι φώκιες είναι προστατευόμενο είδος· αν τις ενοχλήσεις στις σπηλιές όπου γεννούν, μπορεί να εγκαταλείψουν τα μικρά τους.", "The first rule is that the animal is more important than the photograph. I never go near nests, I don't use food to attract animals, and if I see that an animal is getting stressed, I leave immediately. Seals in particular are a protected species; if you disturb them in the caves where they give birth, they may abandon their pups."),
 ],
 "questions": [
  Q("Πόσο περίμενε για τη φωτογραφία με τη φώκια και το μικρό της;", ["Μία μέρα", "Σχεδόν τρεις εβδομάδες", "Έξι μήνες", "Ένα απόγευμα"], 1, "σχεδόν τρεις εβδομάδες"),
  Q("Γιατί, σύμφωνα με τη φωτογράφο, δεν πρέπει να είναι κανείς κουρασμένος;", ["Γιατί ο εξοπλισμός είναι βαρύς", "Γιατί το ζώο εμφανίζεται μόνο για λίγα δευτερόλεπτα", "Γιατί τα βράχια είναι επικίνδυνα", "Γιατί η φωτογράφιση γίνεται τη νύχτα"], 1, "έχεις μόνο λίγα δευτερόλεπτα"),
  Q("Τι κάνει όταν βλέπει ότι ένα ζώο αγχώνεται;", ["Του δίνει τροφή", "Πλησιάζει πιο αργά", "Φεύγει αμέσως", "Αλλάζει φακό"], 2, "αν δω ότι ένα ζώο αγχώνεται, φεύγω αμέσως"),
 ],
 "gloss": {"άγρια": "άγριος — wild", "φώκιες": "φώκια — seal", "κρυφό": "κρυφός — hidden", "αναμονή": "αναμονή — waiting", "αφηρημένος": "αφηρημένος — distracted, absent-minded", "φωλιές": "φωλιά — nest, den", "προσελκύσω": "προσελκύω — to attract", "αγχώνεται": "αγχώνομαι — to get stressed", "προστατευόμενο είδος": "προστατευόμενο είδος — protected species", "γεννούν": "γεννώ — to give birth", "εγκαταλείψουν": "εγκαταλείπω — to abandon"},
})
ITEMS.append({
 "id": "l87-rep-serifos", "title": "Η Σέριφος", "title_en": "Serifos", "type": "report", "level": "B2",
 "context_el": "Σε μια ταξιδιωτική εκπομπή, μια δημοσιογράφος παρουσιάζει τη Σέριφο, στις δυτικές Κυκλάδες.",
 "script": [
  L("Δημοσιογράφος", "f", "Καθώς το πλοίο πλησιάζει στη Σέριφο, το πρώτο που βλέπει κανείς είναι η Χώρα: λευκά σπίτια σκαρφαλωμένα σε έναν απότομο λόφο, πάνω από το λιμάνι του Λιβαδιού. Σύμφωνα με τη μυθολογία, σε αυτό το νησί ο Περσέας έφερε το κεφάλι της Μέδουσας και μετέτρεψε σε πέτρα τον κακό βασιλιά Πολυδέκτη.", "As the ship approaches Serifos, the first thing you see is the Chora: white houses perched on a steep hill above the port of Livadi. According to mythology, it was to this island that Perseus brought the head of Medusa and turned the wicked king Polydectes to stone."),
  L("Δημοσιογράφος", "f", "Η πραγματική ιστορία του νησιού, όμως, είναι γραμμένη στο σίδερο. Για δεκαετίες η Σέριφος ήταν ένα μεγάλο μεταλλείο. Στο Μεγάλο Λιβάδι σώζονται ακόμη τα κτίρια της εταιρείας και μια σιδερένια σκάλα φόρτωσης που μπαίνει μέσα στη θάλασσα, από όπου τα καράβια φόρτωναν το μετάλλευμα.", "The island's real history, however, is written in iron. For decades Serifos was a large mine. At Megalo Livadi the company buildings still survive, along with an iron loading pier that runs out into the sea, from where ships loaded the ore."),
  L("Δημοσιογράφος", "f", "Εκεί, το 1916, οι μεταλλωρύχοι κατέβηκαν σε απεργία ζητώντας οκτάωρη δουλειά και καλύτερες συνθήκες. Η σύγκρουση με τις αρχές είχε τραγικό τέλος: τέσσερις εργάτες σκοτώθηκαν. Η απεργία της Σερίφου θεωρείται σήμερα ένας από τους πρώτους μεγάλους εργατικούς αγώνες στην Ελλάδα, και ένα μνημείο στην παραλία θυμίζει τα θύματα.", "There, in 1916, the miners went on strike, demanding an eight-hour working day and better conditions. The clash with the authorities had a tragic end: four workers were killed. The Serifos strike is now considered one of the first great labour struggles in Greece, and a monument on the beach commemorates the victims."),
 ],
 "questions": [
  Q("Τι βλέπει κανείς πρώτα καθώς πλησιάζει στη Σέριφο;", ["Το μεταλλείο", "Τη Χώρα πάνω σε έναν απότομο λόφο", "Ένα μνημείο στην παραλία", "Έναν φάρο"], 1, "το πρώτο που βλέπει κανείς είναι η Χώρα"),
  Q("Τι σώζεται στο Μεγάλο Λιβάδι;", ["Ένας αρχαίος ναός", "Τα κτίρια της εταιρείας και μια σιδερένια σκάλα φόρτωσης", "Το παλάτι του Πολυδέκτη", "Ένα βενετσιάνικο κάστρο"], 1, "σώζονται ακόμη τα κτίρια της εταιρείας και μια σιδερένια σκάλα φόρτωσης"),
  Q("Τι ζητούσαν οι μεταλλωρύχοι το 1916;", ["Να κλείσει το μεταλλείο", "Οκτάωρη δουλειά και καλύτερες συνθήκες", "Να γίνουν ιδιοκτήτες του μεταλλείου", "Να φύγουν από το νησί"], 1, "ζητώντας οκτάωρη δουλειά και καλύτερες συνθήκες"),
 ],
 "gloss": {"σκαρφαλωμένα": "σκαρφαλωμένος — perched", "απότομο": "απότομος — steep", "μετέτρεψε": "μετατρέπω — to turn into", "μεταλλείο": "μεταλλείο — mine", "σκάλα φόρτωσης": "σκάλα φόρτωσης — loading pier", "μετάλλευμα": "μετάλλευμα — ore", "μεταλλωρύχοι": "μεταλλωρύχος — miner", "απεργία": "απεργία — strike", "οκτάωρη": "οκτάωρος — eight-hour", "αρχές": "αρχές — the authorities", "εργατικούς αγώνες": "εργατικός αγώνας — labour struggle", "θύματα": "θύμα — victim"},
})
ITEMS.append({
 "id": "l87-rep-karystos", "title": "Η Κάρυστος και τα δρακόσπιτα", "title_en": "Karystos and the dragon houses", "type": "report", "level": "B2",
 "context_el": "Σε μια εκπομπή για τη νότια Εύβοια, ένας δημοσιογράφος παρουσιάζει την Κάρυστο και τα βουνά γύρω της.",
 "script": [
  L("Δημοσιογράφος", "m", "Η Κάρυστος, στη νότια άκρη της Εύβοιας, είναι μια ήσυχη παραθαλάσσια πόλη με φαρδιούς δρόμους και μια μεγάλη πλατεία πάνω στο λιμάνι. Στην παραλία δεσπόζει το Μπούρτζι, ένας βενετσιάνικος πύργος, ενώ πάνω από το χωριό Μύλοι υψώνεται το Κόκκινο Κάστρο, που πήρε το όνομά του από το χρώμα των πετρών του.", "Karystos, at the southern tip of Euboea, is a quiet seaside town with wide streets and a large square by the harbour. The Bourtzi, a Venetian tower, dominates the waterfront, while above the village of Myloi rises the Red Castle, which took its name from the colour of its stones."),
  L("Δημοσιογράφος", "m", "Στην αρχαιότητα η περιοχή ήταν γνωστή για το μάρμαρό της, με τα χαρακτηριστικά πράσινα και λευκά νερά. Οι Ρωμαίοι το λάτρευαν και το μετέφεραν μέχρι τη Ρώμη για να διακοσμήσουν ναούς και επαύλεις.", "In antiquity the area was known for its marble, with its characteristic green and white veins. The Romans loved it and transported it all the way to Rome to decorate temples and villas."),
  L("Δημοσιογράφος", "m", "Το μεγαλύτερο μυστήριο, όμως, βρίσκεται ψηλά, στο βουνό Όχη. Εκεί σώζονται τα λεγόμενα δρακόσπιτα, κτίρια από τεράστιες πέτρες χωρίς λάσπη, με στέγες από πλάκες. Οι ντόπιοι πίστευαν ότι μόνο δράκοι θα μπορούσαν να σηκώσουν τέτοιους όγκους. Οι αρχαιολόγοι ακόμη συζητούν ποιος τα έχτισε και για ποιο σκοπό: ναοί, παρατηρητήρια ή καταφύγια για τους εργάτες των λατομείων;", "The greatest mystery, though, lies high up, on Mount Ochi. There survive the so-called dragon houses, buildings of huge stones without mortar, with roofs of slabs. The locals believed that only dragons could lift such masses. Archaeologists still debate who built them and for what purpose: temples, lookout posts or shelters for the quarry workers?"),
 ],
 "questions": [
  Q("Από πού πήρε το όνομά του το Κόκκινο Κάστρο;", ["Από μια μάχη", "Από το χρώμα των πετρών του", "Από τα κόκκινα λουλούδια γύρω του", "Από έναν Βενετό άρχοντα"], 1, "πήρε το όνομά του από το χρώμα των πετρών του"),
  Q("Για ποιο λόγο ήταν γνωστή η Κάρυστος στην αρχαιότητα;", ["Για το κρασί της", "Για το μάρμαρό της", "Για τα καράβια της", "Για τους φιλοσόφους της"], 1, "η περιοχή ήταν γνωστή για το μάρμαρό της"),
  Q("Τι δεν γνωρίζουμε ακόμη για τα δρακόσπιτα;", ["Πού βρίσκονται", "Από τι υλικό είναι", "Ποιος τα έχτισε και για ποιο σκοπό", "Πόσο μεγάλα είναι"], 2, "ποιος τα έχτισε και για ποιο σκοπό"),
 ],
 "gloss": {"δρακόσπιτα": "δρακόσπιτο — 'dragon house', ancient stone building", "παραθαλάσσια": "παραθαλάσσιος — seaside", "δεσπόζει": "δεσπόζω — to dominate", "πύργος": "πύργος — tower", "υψώνεται": "υψώνομαι — to rise", "νερά": "νερά — veins (in marble)", "επαύλεις": "έπαυλη — villa", "πλάκες": "πλάκα — slab", "όγκους": "όγκος — mass, bulk", "παρατηρητήρια": "παρατηρητήριο — lookout post", "λατομείων": "λατομείο — quarry"},
})
ITEMS.append({
 "id": "l87-mono-anaskafi", "title": "Ένα καλοκαίρι σε ανασκαφή", "title_en": "A summer on an excavation", "type": "monologue", "level": "B2",
 "context_el": "Σε μια εκδήλωση του πανεπιστημίου, μια φοιτήτρια αρχαιολογίας μιλά για την πρώτη της συμμετοχή σε ανασκαφή.",
 "script": [
  L("Δανάη", "f", "Πέρσι το καλοκαίρι πέρασα έξι εβδομάδες σε μια ανασκαφή στην ανατολική Κρήτη. Είχα φανταστεί κάτι σαν ταινία περιπέτειας. Η πραγματικότητα ήταν λίγο διαφορετική: ξυπνούσαμε στις πέντε, για να δουλεύουμε πριν πιάσει η ζέστη, και σταματούσαμε στη μία το μεσημέρι.", "Last summer I spent six weeks on an excavation in eastern Crete. I had imagined something like an adventure film. The reality was a little different: we woke up at five, to work before the heat set in, and stopped at one in the afternoon."),
  L("Δανάη", "f", "Τις πρώτες μέρες δεν μου επέτρεψαν καν να σκάψω. Κοσκίνιζα το χώμα που έβγαζαν οι άλλοι και έψαχνα για μικρά κομμάτια από κεραμικά ή κόκαλα. Μετά μου έδωσαν ένα μικρό μυστρί και ένα πινέλο. Μάθαινα να αφαιρώ το χώμα σε λεπτά διαδοχικά στρώματα, πολύ αργά, και να γράφω στο ημερολόγιο κάθε λεπτομέρεια, ακόμα και το χρώμα του χώματος.", "For the first few days they didn't even let me dig. I sieved the soil the others brought up and looked for small pieces of pottery or bone. Then they gave me a small trowel and a brush. I learnt to remove the soil layer by layer, very slowly, and to write every detail in the logbook, even the colour of the soil."),
  L("Δανάη", "f", "Την τέταρτη εβδομάδα, εκεί που καθάριζα μια γωνία ενός δωματίου, είδα κάτι να γυαλίζει. Ήταν ένα μικρό πήλινο ειδώλιο, ενός ζώου, μάλλον ενός βοδιού. Δεν ήταν κάτι εντυπωσιακό για τα μουσεία, αλλά για μένα ήταν το πιο συγκινητικό αντικείμενο του κόσμου: κάποιος το είχε κρατήσει στα χέρια του πριν από τρεισήμισι χιλιάδες χρόνια.", "In the fourth week, while I was cleaning a corner of a room, I saw something shining. It was a small clay figurine of an animal, probably an ox. It wasn't anything impressive for museums, but for me it was the most moving object in the world: someone had held it in their hands three and a half thousand years ago."),
 ],
 "questions": [
  Q("Γιατί ξυπνούσαν στις πέντε το πρωί;", ["Για να προλάβουν το λεωφορείο", "Για να δουλεύουν πριν πιάσει η ζέστη", "Γιατί το ζητούσε ο νόμος", "Για να δουν την ανατολή"], 1, "για να δουλεύουμε πριν πιάσει η ζέστη"),
  Q("Τι έκανε η Δανάη τις πρώτες μέρες;", ["Έσκαβε μόνη της", "Κοσκίνιζε το χώμα και έψαχνε μικρά κομμάτια", "Μαγείρευε για την ομάδα", "Φωτογράφιζε τα ευρήματα"], 1, "Κοσκίνιζα το χώμα που έβγαζαν οι άλλοι"),
  Q("Τι βρήκε την τέταρτη εβδομάδα;", ["Ένα χρυσό κόσμημα", "Ένα αρχαίο νόμισμα", "Ένα μικρό πήλινο ειδώλιο ζώου", "Μια επιγραφή"], 2, "Ήταν ένα μικρό πήλινο ειδώλιο, ενός ζώου"),
 ],
 "gloss": {"ανασκαφή": "ανασκαφή — excavation", "σκάψω": "σκάβω — to dig", "Κοσκίνιζα": "κοσκινίζω — to sieve", "κεραμικά": "κεραμικά — pottery", "κόκαλα": "κόκαλο — bone", "μυστρί": "μυστρί — trowel", "πινέλο": "πινέλο — brush", "στρώμα": "στρώμα — layer", "ημερολόγιο": "ημερολόγιο — logbook, diary", "γυαλίζει": "γυαλίζω — to shine", "πήλινο": "πήλινος — clay", "ειδώλιο": "ειδώλιο — figurine", "βοδιού": "βόδι — ox", "συγκινητικό": "συγκινητικός — moving"},
})
ITEMS.append({
 "id": "l87-mono-psychologos", "title": "Η πρώτη μου φορά σε ψυχολόγο", "title_en": "My first time at a psychologist's", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για την ψυχική υγεία, ένας άντρας σαράντα πέντε χρονών μιλά για την απόφασή του να ζητήσει βοήθεια από ψυχολόγο.",
 "script": [
  L("Γιώργος", "m", "Μεγάλωσα σε ένα χωριό όπου ο ψυχολόγος ήταν «για τους τρελούς». Ο πατέρας μου έλεγε ότι ένας άντρας λύνει μόνος του τα προβλήματά του. Έτσι, όταν πριν από δύο χρόνια έχασα τη δουλειά μου και άρχισα να μην κοιμάμαι, να θυμώνω με όλους και να μη θέλω να βγω από το σπίτι, δεν το είπα σε κανέναν.", "I grew up in a village where the psychologist was 'for crazy people'. My father used to say that a man solves his problems on his own. So when, two years ago, I lost my job and started not sleeping, getting angry with everyone and not wanting to leave the house, I didn't tell anyone."),
  L("Γιώργος", "m", "Η γυναίκα μου ήταν αυτή που επέμεινε. Μου έκλεισε η ίδια ραντεβού, και πήγα σχεδόν θυμωμένος, για να της αποδείξω ότι δεν χρειαζόμουν τίποτα. Στην πρώτη συνεδρία δεν είπα σχεδόν τίποτα. Η ψυχολόγος δεν με πίεσε. Μου είπε μόνο ότι δεν χρειάζεται να είμαι έτοιμος, αρκεί να ξανάρθω.", "It was my wife who insisted. She booked the appointment for me herself, and I went almost angry, to prove to her that I didn't need anything. In the first session I said almost nothing. The psychologist didn't push me. She only told me that I didn't need to be ready, as long as I came back."),
  L("Γιώργος", "m", "Ξαναπήγα. Την τρίτη ή την τέταρτη φορά, μιλώντας για τον πατέρα μου, έβαλα τα κλάματα, κάτι που δεν είχε συμβεί από τότε που ήμουν παιδί. Δεν άλλαξαν όλα από τη μια μέρα στην άλλη, αλλά σιγά σιγά άρχισα να καταλαβαίνω τι μου συνέβαινε. Σήμερα το λέω ανοιχτά, γιατί ίσως κάποιος που με ακούει να είναι εκεί που ήμουν εγώ. Το να ζητάς βοήθεια δεν είναι αδυναμία· χρειάζεται θάρρος.", "I went back. The third or fourth time, talking about my father, I burst into tears, something that hadn't happened since I was a child. Not everything changed overnight, but little by little I began to understand what was happening to me. Today I say it openly, because perhaps someone listening is where I was. Asking for help isn't weakness; it takes courage."),
 ],
 "questions": [
  Q("Τι πίστευαν στο χωριό του Γιώργου για τον ψυχολόγο;", ["Ότι είναι πολύ ακριβός", "Ότι είναι «για τους τρελούς»", "Ότι βοηθάει μόνο τα παιδιά", "Ότι είναι σαν γιατρός"], 1, "ο ψυχολόγος ήταν «για τους τρελούς»"),
  Q("Ποιος έκλεισε το πρώτο ραντεβού;", ["Ο ίδιος", "Ο πατέρας του", "Η γυναίκα του", "Ένας φίλος του"], 2, "Μου έκλεισε η ίδια ραντεβού"),
  Q("Τι πιστεύει σήμερα ο Γιώργος για το να ζητάς βοήθεια;", ["Ότι είναι αδυναμία", "Ότι χρειάζεται θάρρος", "Ότι δεν βοηθάει", "Ότι είναι μόνο για τις γυναίκες"], 1, "Το να ζητάς βοήθεια δεν είναι αδυναμία· χρειάζεται θάρρος"),
 ],
 "gloss": {"ψυχική υγεία": "ψυχική υγεία — mental health", "θυμώνω": "θυμώνω — to get angry", "επέμεινε": "επιμένω — to insist", "αποδείξω": "αποδεικνύω — to prove", "συνεδρία": "συνεδρία — session", "πίεσε": "πιέζω — to pressure, push", "έβαλα τα κλάματα": "βάζω τα κλάματα — to burst into tears", "ανοιχτά": "ανοιχτά — openly", "αδυναμία": "αδυναμία — weakness", "θάρρος": "θάρρος — courage"},
})
ITEMS.append({
 "id": "l87-c1-fainomeno-katoxis", "title": "Γιατί αξίζουν περισσότερο όσα έχουμε;", "title_en": "Why do the things we own seem worth more?", "type": "interview", "level": "C1",
 "context_el": "Σε μια οικονομική εκπομπή, ένας δημοσιογράφος συζητά με μια ερευνήτρια της συμπεριφορικής οικονομίας για το λεγόμενο «φαινόμενο της κατοχής».",
 "script": [
  L("Δημοσιογράφος", "m", "Όλοι έχουμε δυσκολευτεί να πουλήσουμε ένα παλιό αυτοκίνητο ή να πετάξουμε ένα ρούχο που δεν φοράμε πια. Είναι απλώς συναισθηματισμός;", "We've all found it hard to sell an old car or throw away a piece of clothing we no longer wear. Is it just sentimentality?"),
  L("Ερευνήτρια", "f", "Όχι μόνο. Οι οικονομολόγοι το ονομάζουν «φαινόμενο της κατοχής»: μόλις ένα πράγμα γίνει δικό μας, του αποδίδουμε μεγαλύτερη αξία απ’ ό,τι πριν το αποκτήσουμε. Σε ένα κλασικό πείραμα, οι ερευνητές μοίρασαν στους μισούς φοιτητές μιας τάξης μια απλή κούπα του πανεπιστημίου. Ύστερα ρώτησαν τους κατόχους πόσα θα ζητούσαν για να την πουλήσουν και τους υπόλοιπους πόσα θα πλήρωναν για να την αγοράσουν.", "Not only. Economists call it the 'endowment effect': as soon as something becomes ours, we attribute more value to it than before we acquired it. In a classic experiment, the researchers gave half the students in a class a simple university mug. Then they asked the owners how much they would want to sell it and the others how much they would pay to buy it."),
  L("Δημοσιογράφος", "m", "Και η διαφορά ήταν μεγάλη;", "And was the difference large?"),
  L("Ερευνήτρια", "f", "Εντυπωσιακή. Όσοι είχαν την κούπα ζητούσαν περίπου τα διπλάσια χρήματα από όσα ήταν διατεθειμένοι να πληρώσουν οι αγοραστές, παρόλο που την είχαν στα χέρια τους μόνο λίγα λεπτά. Μια βασική εξήγηση είναι η λεγόμενη αποστροφή στην απώλεια: ο πόνος του να χάσουμε κάτι είναι πιο έντονος από τη χαρά του να κερδίσουμε κάτι ισοδύναμο.", "Striking. Those who had the mug asked for about twice as much money as the buyers were willing to pay, even though they had held it for only a few minutes. One basic explanation is so-called loss aversion: the pain of losing something is more intense than the pleasure of gaining something equivalent."),
  L("Δημοσιογράφος", "m", "Το εκμεταλλεύονται οι εταιρείες;", "Do companies exploit it?"),
  L("Ερευνήτρια", "f", "Συστηματικά. Σκεφτείτε τις «δωρεάν δοκιμές» για έναν μήνα ή τα καταστήματα που σας αφήνουν να κρατήσετε ένα προϊόν στο σπίτι πριν αποφασίσετε. Όταν κάτι έχει μπει στη ζωή μας, η επιστροφή του μοιάζει με απώλεια. Η καλύτερη άμυνα είναι να αναρωτιόμαστε: αν δεν το είχα ήδη, θα το αγόραζα σήμερα σε αυτή την τιμή;", "Systematically. Think of 'free trials' for a month, or shops that let you keep a product at home before you decide. Once something has entered our lives, returning it feels like a loss. The best defence is to ask ourselves: if I didn't already have it, would I buy it today at this price?"),
 ],
 "questions": [
  Q("Τι είναι το «φαινόμενο της κατοχής»;", ["Η τάση να αγοράζουμε περισσότερα απ’ όσα χρειαζόμαστε", "Η τάση να δίνουμε μεγαλύτερη αξία σε κάτι μόλις γίνει δικό μας", "Η δυσκολία να αποταμιεύουμε", "Η προτίμηση για ακριβά προϊόντα"], 1, "μόλις ένα πράγμα γίνει δικό μας, του αποδίδουμε μεγαλύτερη αξία"),
  Q("Τι έδειξε το πείραμα με τις κούπες;", ["Ότι οι αγοραστές πλήρωναν περισσότερα", "Ότι οι κάτοχοι ζητούσαν περίπου τα διπλάσια χρήματα", "Ότι κανείς δεν ήθελε την κούπα", "Ότι οι τιμές ήταν ίδιες"], 1, "ζητούσαν περίπου τα διπλάσια χρήματα"),
  Q("Ποια ερώτηση προτείνει η ερευνήτρια ως άμυνα;", ["«Πόσο κοστίζει στο διαδίκτυο;»", "«Θα το αγόραζα σήμερα σε αυτή την τιμή, αν δεν το είχα;»", "«Τι θα πουν οι άλλοι;»", "«Πόσο καιρό το έχω;»"], 1, "αν δεν το είχα ήδη, θα το αγόραζα σήμερα σε αυτή την τιμή"),
 ],
 "gloss": {"συμπεριφορικής οικονομίας": "συμπεριφορική οικονομία — behavioural economics", "κατοχής": "κατοχή — possession, ownership", "συναισθηματισμός": "συναισθηματισμός — sentimentality", "αποδίδουμε": "αποδίδω — to attribute", "αποκτήσουμε": "αποκτώ — to acquire", "κούπα": "κούπα — mug", "κατόχους": "κάτοχος — owner, holder", "διατεθειμένοι": "διατεθειμένος — willing", "αποστροφή στην απώλεια": "αποστροφή στην απώλεια — loss aversion", "ισοδύναμο": "ισοδύναμος — equivalent", "εκμεταλλεύονται": "εκμεταλλεύομαι — to exploit", "άμυνα": "άμυνα — defence"},
})
ITEMS.append({
 "id": "l87-c1-to-ixera", "title": "«Το ήξερα από την αρχή!»", "title_en": "'I knew it all along!'", "type": "monologue", "level": "C1",
 "context_el": "Σε μια διάλεξη για τις παγίδες της σκέψης, ένας ψυχολόγος μιλά για τη μεροληψία της εκ των υστέρων γνώσης.",
 "script": [
  L("Ψυχολόγος", "m", "Μετά από κάθε εκλογή, κάθε οικονομική κρίση ή κάθε ποδοσφαιρικό αγώνα, ακούμε την ίδια φράση: «Ήταν προφανές, το ήξερα από την αρχή». Οι ψυχολόγοι ονομάζουν αυτή την τάση μεροληψία της εκ των υστέρων γνώσης. Μόλις μάθουμε πώς τελείωσε κάτι, το αποτέλεσμα μάς φαίνεται πολύ πιο προβλέψιμο απ’ ό,τι ήταν στην πραγματικότητα.", "After every election, every economic crisis or every football match, we hear the same phrase: 'It was obvious, I knew it all along.' Psychologists call this tendency hindsight bias. As soon as we learn how something ended, the outcome seems much more predictable to us than it really was."),
  L("Ψυχολόγος", "m", "Στις αρχές της δεκαετίας του ’70, μια ερευνήτρια ζήτησε από φοιτητές να εκτιμήσουν τις πιθανότητες για διάφορα πιθανά αποτελέσματα ενός σημαντικού διπλωματικού ταξιδιού, πριν αυτό γίνει. Μετά το ταξίδι, τους ζήτησε να θυμηθούν τι είχαν απαντήσει. Οι περισσότεροι «θυμούνταν» ότι είχαν δώσει μεγαλύτερες πιθανότητες στα γεγονότα που τελικά συνέβησαν. Η μνήμη τους είχε ξαναγραφτεί, χωρίς να το καταλάβουν.", "In the early 1970s, a researcher asked students to estimate the probabilities of various possible outcomes of an important diplomatic trip, before it took place. After the trip, she asked them to remember what they had answered. Most 'remembered' that they had given higher probabilities to the events that actually happened. Their memory had been rewritten without their noticing."),
  L("Ψυχολόγος", "m", "Γιατί είναι επικίνδυνο αυτό; Πρώτον, γιατί μας κάνει υπερβολικά σίγουρους για την ικανότητά μας να προβλέπουμε το μέλλον. Δεύτερον, γιατί κρίνουμε άδικα τους άλλους: τον γιατρό, τον δικαστή ή τον μάνατζερ που πήρε μια απόφαση με τα στοιχεία που είχε τότε, όχι με όσα μάθαμε εμείς αργότερα. Μια απλή άσκηση βοηθά: πριν από μια σημαντική απόφαση, σημειώστε τι περιμένετε να συμβεί και γιατί. Όταν, αργότερα, ξαναδιαβάσετε τις σημειώσεις σας, θα εκπλαγείτε.", "Why is this dangerous? First, because it makes us overconfident in our ability to predict the future. Second, because we judge others unfairly: the doctor, the judge or the manager who made a decision with the information they had at the time, not with what we learnt later. A simple exercise helps: before an important decision, write down what you expect to happen and why. When you reread your notes later, you'll be surprised."),
 ],
 "questions": [
  Q("Τι είναι η μεροληψία της εκ των υστέρων γνώσης;", ["Η δυσκολία να θυμόμαστε το παρελθόν", "Η τάση να θεωρούμε ένα αποτέλεσμα πιο προβλέψιμο αφού το μάθουμε", "Η τάση να φοβόμαστε το μέλλον", "Η συνήθεια να αλλάζουμε γνώμη συχνά"], 1, "το αποτέλεσμα μάς φαίνεται πολύ πιο προβλέψιμο απ’ ό,τι ήταν στην πραγματικότητα"),
  Q("Τι «θυμούνταν» οι φοιτητές μετά το ταξίδι;", ["Ότι δεν είχαν απαντήσει", "Ότι είχαν δώσει μεγαλύτερες πιθανότητες σε όσα τελικά συνέβησαν", "Ότι είχαν κάνει λάθος σε όλα", "Ότι είχαν αντιγράψει από τους συμφοιτητές τους"], 1, "είχαν δώσει μεγαλύτερες πιθανότητες στα γεγονότα που τελικά συνέβησαν"),
  Q("Ποια άσκηση προτείνει ο ομιλητής;", ["Να μη λαμβάνουμε σημαντικές αποφάσεις", "Να σημειώνουμε τι περιμένουμε να συμβεί πριν από μια απόφαση", "Να ρωτάμε πάντα έναν ειδικό", "Να ξεχνάμε τις παλιές μας προβλέψεις"], 1, "σημειώστε τι περιμένετε να συμβεί και γιατί"),
 ],
 "gloss": {"παγίδες": "παγίδα — trap", "μεροληψία": "μεροληψία — bias", "εκ των υστέρων": "εκ των υστέρων — in hindsight", "προβλέψιμο": "προβλέψιμος — predictable", "εκτιμήσουν": "εκτιμώ — to estimate", "πιθανότητες": "πιθανότητα — probability", "διπλωματικού": "διπλωματικός — diplomatic", "ξαναγραφτεί": "ξαναγράφομαι — to be rewritten", "υπερβολικά": "υπερβολικά — excessively", "ικανότητά": "ικανότητα — ability", "άδικα": "άδικα — unfairly", "στοιχεία": "στοιχεία — data, information", "εκπλαγείτε": "εκπλήσσομαι — to be surprised"},
})

rnd = random.Random(87)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-87.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
