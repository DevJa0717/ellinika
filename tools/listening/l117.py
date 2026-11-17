# Source for library/listening/listening-117.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l117.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l117-ann-enydreio", "title": "Ανακοίνωση στο ενυδρείο", "title_en": "An announcement at the aquarium", "type": "announcement", "level": "B2",
 "context_el": "Επισκέπτεστε ένα ενυδρείο με τα παιδιά σας. Ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνητής", "m", "Αγαπητοί επισκέπτες, καλώς ήρθατε στο ενυδρείο μας. Σας ενημερώνουμε ότι το τάισμα των καρχαριών στη μεγάλη δεξαμενή θα γίνει σήμερα στις δώδεκα και μισή, αντί για τις έντεκα, λόγω μιας μικρής τεχνικής εργασίας.", "Dear visitors, welcome to our aquarium. We would like to inform you that the shark feeding in the large tank will take place today at half past twelve, instead of eleven, because of some minor technical work."),
  L("Εκφωνητής", "m", "Η δεξαμενή αφής, όπου τα παιδιά μπορούν να αγγίξουν αστερίες και αχινούς, παραμένει κλειστή όλη την ημέρα, για να ξεκουραστούν τα ζώα μετά την πολυσύχναστη εβδομάδα. Ζητούμε την κατανόησή σας.", "The touch pool, where children can touch starfish and sea urchins, remains closed all day, so that the animals can rest after the busy week. We ask for your understanding."),
  L("Εκφωνητής", "m", "Υπενθυμίζουμε ότι η χρήση φλας απαγορεύεται σε όλους τους χώρους, γιατί ενοχλεί τα ψάρια. Στο ισόγειο λειτουργεί καφετέρια, ενώ στο κατάστημα δώρων όσοι έχουν εισιτήριο έχουν έκπτωση δέκα τοις εκατό.", "We remind you that the use of flash is forbidden in all areas, because it disturbs the fish. On the ground floor there is a café, while in the gift shop ticket holders get a ten per cent discount."),
 ],
 "questions": [
  Q("Πότε θα γίνει σήμερα το τάισμα των καρχαριών;", ["Στις έντεκα", "Στις δώδεκα και μισή", "Στις δώδεκα", "Στη μία"], 1, "θα γίνει σήμερα στις δώδεκα και μισή"),
  Q("Γιατί είναι κλειστή η δεξαμενή αφής;", ["Για να ξεκουραστούν τα ζώα", "Λόγω βλάβης", "Γιατί καθαρίζεται", "Γιατί έρχονται καινούργια ζώα"], 0, "για να ξεκουραστούν τα ζώα μετά την πολυσύχναστη εβδομάδα"),
  Q("Γιατί απαγορεύεται το φλας;", ["Γιατί χαλάει τα τζάμια", "Γιατί ενοχλεί τους άλλους επισκέπτες", "Λόγω πνευματικών δικαιωμάτων", "Γιατί ενοχλεί τα ψάρια"], 3, "γιατί ενοχλεί τα ψάρια"),
 ],
 "gloss": {"ενυδρείο": "ενυδρείο — aquarium", "τάισμα": "τάισμα — feeding", "καρχαριών": "καρχαρίας — shark", "δεξαμενή": "δεξαμενή — tank, pool", "αφής": "αφή — touch", "αστερίες": "αστερίας — starfish", "αχινούς": "αχινός — sea urchin", "πολυσύχναστη": "πολυσύχναστος — busy, crowded", "φλας": "φλας — (camera) flash", "έκπτωση": "έκπτωση — discount"}
})

ITEMS.append({
 "id": "l117-vm-orthodontikos", "title": "Μήνυμα από την ορθοδοντικό", "title_en": "A message from the orthodontist", "type": "voicemail", "level": "B2",
 "context_el": "Ο γιος σας φοράει σιδεράκια. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Ορθοδοντικός", "f", "Καλησπέρα σας, η Αλεξάνδρα Νικολαΐδου είμαι, η ορθοδοντικός του Στέλιου. Σας τηλεφωνώ γιατί η αυριανή του επίσκεψη πρέπει να μετακινηθεί. Έχω ένα επείγον χειρουργείο και δεν θα είμαι στο ιατρείο.", "Good evening, this is Alexandra Nikolaidou, Stelios's orthodontist. I'm calling because his appointment tomorrow has to be moved. I have an urgent operation and won't be at the surgery."),
  L("Ορθοδοντικός", "f", "Μπορώ να τον δω είτε την Πέμπτη στις πέντε είτε το Σάββατο το πρωί. Αν ο σύρμα που του έβαλα την προηγούμενη φορά τον τρυπάει, βάλτε λίγο από το κερί που σας έδωσα πάνω στο σημείο. Δεν είναι επείγον, απλώς ενοχλεί.", "I can see him either on Thursday at five or on Saturday morning. If the wire I put in last time is poking him, put a little of the wax I gave you on the spot. It's not urgent, it's just annoying."),
  L("Ορθοδοντικός", "f", "Επίσης, θυμίστε του, σας παρακαλώ, να φοράει τα λαστιχάκια και τη νύχτα, γιατί αλλιώς η θεραπεία θα κρατήσει περισσότερο. Πείτε μου στη γραμματεία ποια μέρα σας βολεύει. Ευχαριστώ.", "Also, please remind him to wear the elastics at night too, because otherwise the treatment will take longer. Tell the reception which day suits you. Thank you."),
 ],
 "questions": [
  Q("Γιατί πρέπει να αλλάξει η επίσκεψη;", ["Γιατί η γιατρός είναι άρρωστη", "Γιατί η γιατρός έχει ένα επείγον χειρουργείο", "Γιατί το ιατρείο θα είναι κλειστό για διακοπές", "Γιατί χάλασε ένα μηχάνημα"], 1, "Έχω ένα επείγον χειρουργείο"),
  Q("Τι πρέπει να κάνουν αν το σύρμα τρυπάει τον Στέλιο;", ["Να έρθουν αμέσως στο ιατρείο", "Να κόψουν το σύρμα", "Να βάλουν λίγο κερί πάνω στο σημείο", "Να του δώσουν παυσίπονο"], 2, "βάλτε λίγο από το κερί που σας έδωσα πάνω στο σημείο"),
  Q("Τι πρέπει να θυμίσουν στον Στέλιο;", ["Να φοράει τα λαστιχάκια και τη νύχτα", "Να μην τρώει γλυκά", "Να βουρτσίζει τα δόντια του πιο συχνά", "Να φέρει την ακτινογραφία"], 0, "να φοράει τα λαστιχάκια και τη νύχτα"),
 ],
 "gloss": {"ορθοδοντικός": "ορθοδοντικός — orthodontist", "σιδεράκια": "σιδεράκια — braces", "μετακινηθεί": "μετακινούμαι — to be moved, rescheduled", "επείγον": "επείγων — urgent", "χειρουργείο": "χειρουργείο — operation; operating theatre", "σύρμα": "σύρμα — wire", "τρυπάει": "τρυπάω — to prick, poke", "κερί": "κερί — wax", "λαστιχάκια": "λαστιχάκι — (orthodontic) elastic band", "βολεύει": "με βολεύει — it suits me"}
})

ITEMS.append({
 "id": "l117-dial-ntoulapa", "title": "Συναρμολογώντας την καινούργια ντουλάπα", "title_en": "Assembling the new wardrobe", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι, ο Θοδωρής και η Μαρίνα, προσπαθεί να συναρμολογήσει μια ντουλάπα που αγόρασε.",
 "script": [
  L("Θοδωρής", "m", "Μαρίνα, μας περισσεύουν τέσσερις βίδες. Αυτό είναι καλό ή κακό σημάδι;", "Marina, we've got four screws left over. Is that a good sign or a bad one?"),
  L("Μαρίνα", "f", "Κακό, σίγουρα. Σου είπα να διαβάσουμε πρώτα τις οδηγίες, αλλά εσύ είπες ότι «αυτά τα φτιάχνεις με τα μάτια κλειστά».", "Bad, definitely. I told you we should read the instructions first, but you said you \"can build these with your eyes closed\"."),
  L("Θοδωρής", "m", "Εντάξει, παραδέχομαι ότι βιάστηκα. Κοίτα, στο σχέδιο έξι τα ράφια μπαίνουν πριν από την πλάτη. Εμείς βάλαμε πρώτα την πλάτη.", "OK, I admit I rushed. Look, in diagram six the shelves go in before the back panel. We put the back panel in first."),
  L("Μαρίνα", "f", "Δηλαδή πρέπει να ξεβιδώσουμε τη μισή ντουλάπα. Θαυμάσια. Μήπως να καλέσουμε τελικά τον τεχνικό του καταστήματος; Ζητούσε μόνο τριάντα ευρώ.", "So we have to unscrew half the wardrobe. Wonderful. Shall we call the shop's fitter after all? He was only asking thirty euros."),
  L("Θοδωρής", "m", "Όχι, θα το τελειώσουμε μόνοι μας, είναι θέμα αξιοπρέπειας πια. Εσύ κράτα την πόρτα σταθερή κι εγώ βιδώνω. Και αυτή τη φορά διαβάζουμε κάθε βήμα.", "No, we'll finish it ourselves, it's a matter of dignity now. You hold the door steady and I'll screw. And this time we read every step."),
  L("Μαρίνα", "f", "Καλά. Αλλά αν στις δέκα δεν έχει κλείσει η πόρτα, τηλεφωνώ στον τεχνικό, και την πληρώνεις εσύ.", "Fine. But if the door hasn't closed by ten, I'm phoning the fitter, and you're paying."),
 ],
 "questions": [
  Q("Ποιο ήταν το λάθος τους;", ["Αγόρασαν λάθος ντουλάπα", "Έβαλαν την πλάτη πριν από τα ράφια", "Έχασαν τις οδηγίες", "Χρησιμοποίησαν λάθος εργαλεία"], 1, "Εμείς βάλαμε πρώτα την πλάτη"),
  Q("Τι προτείνει η Μαρίνα;", ["Να επιστρέψουν τη ντουλάπα", "Να ζητήσουν βοήθεια από έναν γείτονα", "Να καλέσουν τον τεχνικό του καταστήματος", "Να αγοράσουν καινούργιες βίδες"], 2, "Μήπως να καλέσουμε τελικά τον τεχνικό του καταστήματος;"),
  Q("Τι θα γίνει αν η πόρτα δεν έχει κλείσει στις δέκα;", ["Η Μαρίνα θα τηλεφωνήσει στον τεχνικό και θα πληρώσει ο Θοδωρής", "Θα συνεχίσουν την επόμενη μέρα", "Θα πάνε για ύπνο", "Ο Θοδωρής θα τα παρατήσει"], 0, "τηλεφωνώ στον τεχνικό, και την πληρώνεις εσύ"),
 ],
 "gloss": {"συναρμολογήσει": "συναρμολογώ — to assemble", "ντουλάπα": "ντουλάπα — wardrobe", "περισσεύουν": "περισσεύω — to be left over", "βίδες": "βίδα — screw", "οδηγίες": "οδηγίες — instructions", "παραδέχομαι": "παραδέχομαι — to admit", "ράφια": "ράφι — shelf", "ξεβιδώσουμε": "ξεβιδώνω — to unscrew", "αξιοπρέπειας": "αξιοπρέπεια — dignity", "βιδώνω": "βιδώνω — to screw (in)"}
})

ITEMS.append({
 "id": "l117-int-ichitika-efe", "title": "Η δημιουργός ηχητικών εφέ", "title_en": "The sound-effects artist", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια δημιουργό ηχητικών εφέ σε ραδιοφωνική εκπομπή για τον κινηματογράφο.",
 "script": [
  L("Δημοσιογράφος", "m", "Η δουλειά σας λέγεται «φόλεϊ». Τι ακριβώς κάνετε;", "Your job is called \"foley\". What exactly do you do?"),
  L("Ηχολήπτρια", "f", "Φτιάχνω σε στούντιο τους καθημερινούς ήχους μιας ταινίας: βήματα, πόρτες, ρούχα που θροΐζουν. Στα γυρίσματα, το μικρόφωνο γράφει κυρίως τους διαλόγους. Όλα τα υπόλοιπα τα ξαναδημιουργούμε εμείς, βλέποντας την εικόνα σε μια οθόνη. Το όνομα το πήρε από τον Τζακ Φόλεϊ, έναν Αμερικανό που άρχισε να το κάνει όταν οι ταινίες απέκτησαν ήχο.", "I create a film's everyday sounds in a studio: footsteps, doors, rustling clothes. On set, the microphone mainly records the dialogue. We recreate everything else, watching the picture on a screen. The name comes from Jack Foley, an American who started doing it when films got sound."),
  L("Δημοσιογράφος", "m", "Και ποια υλικά χρησιμοποιείτε;", "And what materials do you use?"),
  L("Ηχολήπτρια", "f", "Ό,τι φανταστείτε. Για τα βήματα στο χιόνι, πατάω ένα σακουλάκι γεμάτο κορν φλάουρ. Για ένα κόκαλο που σπάει, σπάω ένα κοτσάνι σέλινο. Και το κλασικό: δύο μισά καρύδας για τις οπλές των αλόγων.", "Anything you can imagine. For footsteps in snow, I press a little bag full of cornflour. For a breaking bone, I snap a stick of celery. And the classic: two coconut halves for horses' hooves."),
  L("Δημοσιογράφος", "m", "Δεν θα ήταν πιο εύκολο να χρησιμοποιείτε έτοιμους ήχους από υπολογιστή;", "Wouldn't it be easier to use ready-made sounds from a computer?"),
  L("Ηχολήπτρια", "f", "Πιο γρήγορο, ναι. Αλλά ένας έτοιμος ήχος δεν ταιριάζει ποτέ ακριβώς με τον ρυθμό του ηθοποιού. Όταν περπατάω μαζί του, ακολουθώ τη διάθεσή του: αν είναι κουρασμένος, θυμωμένος, ερωτευμένος. Ο θεατής δεν το καταλαβαίνει, αλλά το νιώθει.", "Faster, yes. But a ready-made sound never matches the actor's rhythm exactly. When I walk with him, I follow his mood: whether he's tired, angry, in love. The viewer doesn't notice it, but feels it."),
 ],
 "questions": [
  Q("Τι γράφει κυρίως το μικρόφωνο στα γυρίσματα;", ["Τη μουσική", "Τους διαλόγους", "Τους ήχους του δρόμου", "Τα βήματα των ηθοποιών"], 1, "το μικρόφωνο γράφει κυρίως τους διαλόγους"),
  Q("Τι χρησιμοποιεί για τα βήματα στο χιόνι;", ["Ένα σακουλάκι γεμάτο κορν φλάουρ", "Αλάτι", "Ζάχαρη", "Τριμμένο πάγο"], 0, "πατάω ένα σακουλάκι γεμάτο κορν φλάουρ"),
  Q("Γιατί προτιμά να μη χρησιμοποιεί έτοιμους ήχους;", ["Γιατί είναι ακριβοί", "Γιατί δεν ακούγονται καθαρά", "Γιατί δεν ταιριάζουν ακριβώς με τον ρυθμό του ηθοποιού", "Γιατί δεν της το επιτρέπει ο σκηνοθέτης"], 2, "ένας έτοιμος ήχος δεν ταιριάζει ποτέ ακριβώς με τον ρυθμό του ηθοποιού"),
 ],
 "gloss": {"ηχητικών": "ηχητικός — sound (adj.)", "θροΐζουν": "θροΐζω — to rustle", "γυρίσματα": "γύρισμα — shooting (of a film)", "ξαναδημιουργούμε": "ξαναδημιουργώ — to recreate", "κορν φλάουρ": "κορν φλάουρ — cornflour", "κόκαλο": "κόκαλο — bone", "κοτσάνι": "κοτσάνι — stalk, stick", "σέλινο": "σέλινο — celery", "οπλές": "οπλή — hoof", "διάθεσή": "διάθεση — mood"}
})

ITEMS.append({
 "id": "l117-rep-apografi-dentron", "title": "Μια πόλη μετράει τα δέντρα της", "title_en": "A town counts its trees", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Ρεπόρτερ", "f", "Πόσα δέντρα έχει η πόλη μας; Μέχρι πέρσι κανείς δεν ήξερε. Φέτος, περισσότεροι από διακόσιοι εθελοντές, κυρίως φοιτητές και συνταξιούχοι, γύρισαν όλους τους δρόμους και τα πάρκα με ένα κινητό και μια μεζούρα, για να καταγράψουν κάθε δέντρο ένα ένα.", "How many trees does our town have? Until last year, nobody knew. This year, more than two hundred volunteers, mostly students and pensioners, went round all the streets and parks with a mobile phone and a tape measure, to record every tree one by one."),
  L("Ρεπόρτερ", "f", "Για κάθε δέντρο σημείωναν το είδος, το ύψος, την περίμετρο του κορμού και την κατάστασή του. Το αποτέλεσμα: περίπου δεκαοκτώ χιλιάδες δέντρα, από τα οποία τα περισσότερα είναι νεραντζιές και πλατάνια. Περίπου ένα στα δέκα, όμως, είναι άρρωστο ή ξερό.", "For each tree they noted the species, the height, the trunk circumference and its condition. The result: about eighteen thousand trees, most of them bitter orange trees and plane trees. About one in ten, however, is diseased or dead."),
  L("Ρεπόρτερ", "f", "Ο χάρτης που προέκυψε είναι ανοιχτός στο κοινό στην ιστοσελίδα του δήμου. Δείχνει καθαρά ότι οι φτωχότερες γειτονιές έχουν πολύ λιγότερη σκιά. Ο δήμος δεσμεύτηκε να φυτέψει εκεί πρώτα τα επόμενα χίλια δέντρα.", "The resulting map is open to the public on the council's website. It clearly shows that the poorer neighbourhoods have much less shade. The council has committed to plant the next thousand trees there first."),
 ],
 "questions": [
  Q("Ποιοι έκαναν την καταγραφή;", ["Υπάλληλοι του δήμου", "Μια ιδιωτική εταιρεία", "Πάνω από διακόσιοι εθελοντές", "Μαθητές ενός σχολείου"], 2, "περισσότεροι από διακόσιοι εθελοντές"),
  Q("Τι ποσοστό των δέντρων είναι άρρωστο ή ξερό;", ["Περίπου ένα στα δέκα", "Περίπου τα μισά", "Περίπου ένα στα τρία", "Σχεδόν κανένα"], 0, "Περίπου ένα στα δέκα, όμως, είναι άρρωστο ή ξερό"),
  Q("Τι δείχνει ο χάρτης;", ["Ότι το κέντρο δεν έχει καθόλου δέντρα", "Ότι οι φτωχότερες γειτονιές έχουν πολύ λιγότερη σκιά", "Ότι τα πάρκα είναι εγκαταλειμμένα", "Ότι τα πλατάνια είναι άρρωστα"], 1, "οι φτωχότερες γειτονιές έχουν πολύ λιγότερη σκιά"),
 ],
 "gloss": {"εθελοντές": "εθελοντής — volunteer", "συνταξιούχοι": "συνταξιούχος — pensioner", "μεζούρα": "μεζούρα — tape measure", "καταγράψουν": "καταγράφω — to record, list", "περίμετρο": "περίμετρος — circumference, perimeter", "κορμού": "κορμός — trunk", "νεραντζιές": "νεραντζιά — bitter orange tree", "πλατάνια": "πλάτανος/πλατάνι — plane tree", "προέκυψε": "προκύπτω — to result, emerge", "δεσμεύτηκε": "δεσμεύομαι — to commit oneself"}
})

ITEMS.append({
 "id": "l117-rep-kagiak-plastiko", "title": "Καγιάκ από πλαστικό της θάλασσας", "title_en": "Kayaks made from sea plastic", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε εκπομπή για το περιβάλλον.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε ένα μικρό εργαστήριο σε νησί των Κυκλάδων, τρεις φίλοι κατασκευάζουν καγιάκ από πλαστικό που μαζεύεται από τις παραλίες και από παλιά δίχτυα ψαράδων. Η ιδέα γεννήθηκε ένα καλοκαίρι, όταν, μετά από έναν εθελοντικό καθαρισμό, είχαν γεμίσει πενήντα σακούλες και δεν ήξεραν πού να τις πάνε.", "In a small workshop on a Cycladic island, three friends make kayaks from plastic collected from beaches and from old fishing nets. The idea was born one summer when, after a volunteer clean-up, they had filled fifty bags and didn't know where to take them."),
  L("Ρεπόρτερ", "m", "Το πλαστικό πλένεται, τεμαχίζεται και λιώνει σε καλούπια. Για κάθε καγιάκ χρειάζονται περίπου είκοσι κιλά. Το πιο δύσκολο, λένε, δεν είναι η κατασκευή αλλά η διαλογή: δεν μπορούν να χρησιμοποιηθούν όλα τα είδη πλαστικού μαζί.", "The plastic is washed, shredded and melted in moulds. Each kayak needs about twenty kilos. The hardest part, they say, isn't the building but the sorting: not all kinds of plastic can be used together."),
  L("Ρεπόρτερ", "m", "Τα πρώτα καγιάκ τα νοικιάζουν σε επισκέπτες, μαζί με μια ξενάγηση στις ακτές του νησιού. Το καλοκαίρι, κάθε ομάδα που νοικιάζει καγιάκ μαζεύει και μια σακούλα σκουπίδια κατά τη διαδρομή. «Έτσι η δουλειά μας τροφοδοτεί τον εαυτό της», λέει γελώντας ένας από τους τρεις.", "They rent the first kayaks to visitors, together with a guided tour of the island's coast. In summer, every group that rents a kayak also collects a bag of rubbish along the way. \"That way our work feeds itself\", one of the three says, laughing."),
 ],
 "questions": [
  Q("Πώς γεννήθηκε η ιδέα;", ["Από ένα σχολικό πρόγραμμα", "Μετά από έναν εθελοντικό καθαρισμό με πενήντα σακούλες", "Από ένα ταξίδι στο εξωτερικό", "Από μια ιδέα του δήμου"], 1, "μετά από έναν εθελοντικό καθαρισμό, είχαν γεμίσει πενήντα σακούλες"),
  Q("Ποιο είναι το πιο δύσκολο μέρος της δουλειάς;", ["Η διαλογή του πλαστικού", "Η πώληση", "Η μεταφορά", "Το λιώσιμο"], 0, "Το πιο δύσκολο, λένε, δεν είναι η κατασκευή αλλά η διαλογή"),
  Q("Τι κάνει κάθε ομάδα που νοικιάζει καγιάκ το καλοκαίρι;", ["Πληρώνει διπλάσιο ενοίκιο", "Βοηθά στην κατασκευή", "Παίρνει ένα δώρο", "Μαζεύει μια σακούλα σκουπίδια κατά τη διαδρομή"], 3, "μαζεύει και μια σακούλα σκουπίδια κατά τη διαδρομή"),
 ],
 "gloss": {"καγιάκ": "καγιάκ — kayak", "κατασκευάζουν": "κατασκευάζω — to make, build", "δίχτυα": "δίχτυ — net", "καθαρισμό": "καθαρισμός — clean-up", "τεμαχίζεται": "τεμαχίζω — to shred, cut into pieces", "λιώνει": "λιώνω — to melt", "καλούπια": "καλούπι — mould", "διαλογή": "διαλογή — sorting", "ξενάγηση": "ξενάγηση — guided tour", "τροφοδοτεί": "τροφοδοτώ — to feed, supply"}
})

ITEMS.append({
 "id": "l117-mon-stamatisa-na-argo", "title": "Πώς σταμάτησα να αργώ παντού", "title_en": "How I stopped being late for everything", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νέα γυναίκα να μιλά σε ένα podcast για τις καθημερινές συνήθειες.",
 "script": [
  L("Ομιλήτρια", "f", "Για χρόνια ήμουν η φίλη που αργεί. Στα ραντεβού, στη δουλειά, ακόμα και στον γάμο της αδερφής μου έφτασα την ώρα που έβγαινε η νύφη από την εκκλησία. Οι φίλοι μου είχαν αρχίσει να μου λένε ότι η συνάντηση είναι στις οκτώ, ενώ ήταν στις οκτώ και μισή.", "For years I was the friend who's late. At meetings, at work, even at my sister's wedding I arrived just as the bride was coming out of the church. My friends had started telling me the meeting was at eight when it was at half past eight."),
  L("Ομιλήτρια", "f", "Κάποια στιγμή κατάλαβα ότι το πρόβλημά μου δεν ήταν η τεμπελιά. Υπολόγιζα λάθος τον χρόνο: πίστευα ότι η διαδρομή κρατά δεκαπέντε λεπτά, ενώ με την κίνηση κρατούσε τριάντα. Άρχισα λοιπόν να χρονομετρώ τα πάντα, από το ντους μέχρι το πάρκινγκ.", "At some point I realised that my problem wasn't laziness. I miscalculated time: I thought the journey took fifteen minutes, whereas with the traffic it took thirty. So I started timing everything, from the shower to parking."),
  L("Ομιλήτρια", "f", "Το δεύτερο κόλπο ήταν να σκέφτομαι την ώρα που πρέπει να φύγω, όχι την ώρα που πρέπει να φτάσω. Σήμερα φτάνω συνήθως πέντε λεπτά νωρίτερα, και ξέρετε κάτι; Αυτά τα πέντε λεπτά, με έναν καφέ στο χέρι, είναι η πιο ήρεμη στιγμή της μέρας μου.", "The second trick was to think about the time I have to leave, not the time I have to arrive. Today I usually arrive five minutes early, and do you know what? Those five minutes, with a coffee in my hand, are the calmest moment of my day."),
 ],
 "questions": [
  Q("Τι είχαν αρχίσει να κάνουν οι φίλοι της;", ["Να μην την καλούν πια", "Να της λένε ότι η συνάντηση είναι νωρίτερα από ό,τι ήταν", "Να την περιμένουν στο σπίτι της", "Να της τηλεφωνούν το πρωί"], 1, "Οι φίλοι μου είχαν αρχίσει να μου λένε ότι η συνάντηση είναι στις οκτώ, ενώ ήταν στις οκτώ και μισή"),
  Q("Ποιο ήταν, τελικά, το πρόβλημά της;", ["Η τεμπελιά", "Η κίνηση στους δρόμους", "Υπολόγιζε λάθος τον χρόνο", "Δεν είχε ρολόι"], 2, "Υπολόγιζα λάθος τον χρόνο"),
  Q("Ποιο ήταν το δεύτερο κόλπο της;", ["Να σκέφτεται την ώρα που πρέπει να φύγει", "Να βάζει πολλά ξυπνητήρια", "Να μένει κοντά στη δουλειά", "Να πίνει καφέ στο σπίτι"], 0, "να σκέφτομαι την ώρα που πρέπει να φύγω"),
 ],
 "gloss": {"αργεί": "αργώ — to be late", "ραντεβού": "ραντεβού — appointment, meeting", "νύφη": "νύφη — bride", "τεμπελιά": "τεμπελιά — laziness", "Υπολόγιζα": "υπολογίζω — to calculate, estimate", "διαδρομή": "διαδρομή — journey, route", "κίνηση": "κίνηση — traffic", "χρονομετρώ": "χρονομετρώ — to time", "κόλπο": "κόλπο — trick", "ήρεμη": "ήρεμος — calm"}
})

ITEMS.append({
 "id": "l117-mon-michani-sta-peninta", "title": "Μαθαίνοντας να οδηγώ μηχανή στα πενήντα", "title_en": "Learning to ride a motorbike at fifty", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να διηγείται μια εμπειρία της σε ραδιοφωνική εκπομπή.",
 "script": [
  L("Ακροάτρια", "f", "Όταν έκλεισα τα πενήντα, τα παιδιά μου μού χάρισαν ένα κράνος. Ήταν αστείο, γιατί δεν είχα ανέβει ποτέ σε μηχανή. Όμως από μικρή ζήλευα τον θείο μου, που γύριζε όλη την Πελοπόννησο με μια παλιά μοτοσικλέτα.", "When I turned fifty, my children gave me a helmet. It was a joke, because I had never been on a motorbike. But since I was little I'd envied my uncle, who toured the whole Peloponnese on an old motorbike."),
  L("Ακροάτρια", "f", "Γράφτηκα σε σχολή οδηγών. Στα πρώτα μαθήματα έπεσα δύο φορές, ευτυχώς χωρίς σοβαρό τραυματισμό. Ο εκπαιδευτής μου, ένας νεαρός είκοσι πέντε χρονών, μου είπε κάτι που δεν θα ξεχάσω: «Η μηχανή πηγαίνει εκεί που κοιτάς. Μην κοιτάς το εμπόδιο, κοίτα τον δρόμο.»", "I enrolled at a driving school. In the first lessons I fell twice, fortunately without serious injury. My instructor, a young man of twenty-five, told me something I won't forget: \"The bike goes where you look. Don't look at the obstacle, look at the road.\""),
  L("Ακροάτρια", "f", "Πήρα το δίπλωμα με την πρώτη. Το περασμένο καλοκαίρι έκανα μόνη μου τη διαδρομή που έκανε ο θείος μου, από την Πάτρα ως τη Μονεμβασιά. Η συμβουλή του εκπαιδευτή μου, πάντως, μου χρησιμεύει και στη ζωή.", "I got my licence first time. Last summer I rode on my own the route my uncle used to do, from Patras to Monemvasia. My instructor's advice, by the way, also helps me in life."),
 ],
 "questions": [
  Q("Γιατί ήταν αστείο το δώρο των παιδιών της;", ["Γιατί το κράνος ήταν πολύ μικρό", "Γιατί δεν είχε ανέβει ποτέ σε μηχανή", "Γιατί είχε ήδη τρία κράνη", "Γιατί φοβόταν τις μηχανές"], 1, "δεν είχα ανέβει ποτέ σε μηχανή"),
  Q("Τι της είπε ο εκπαιδευτής της;", ["Ότι είναι πολύ μεγάλη για μηχανή", "Ότι πρέπει να οδηγεί αργά", "Ότι η μηχανή πηγαίνει εκεί που κοιτάς", "Ότι πρέπει να αγοράσει καινούργια μηχανή"], 2, "Η μηχανή πηγαίνει εκεί που κοιτάς"),
  Q("Τι έκανε το περασμένο καλοκαίρι;", ["Έκανε μόνη της τη διαδρομή του θείου της", "Έγινε εκπαιδεύτρια", "Αγόρασε τη μοτοσικλέτα του θείου της", "Ταξίδεψε με τα παιδιά της"], 0, "έκανα μόνη μου τη διαδρομή που έκανε ο θείος μου"),
 ],
 "gloss": {"κράνος": "κράνος — helmet", "ζήλευα": "ζηλεύω — to envy", "μοτοσικλέτα": "μοτοσικλέτα — motorbike", "σχολή οδηγών": "σχολή οδηγών — driving school", "τραυματισμό": "τραυματισμός — injury", "εκπαιδευτής": "εκπαιδευτής — instructor", "εμπόδιο": "εμπόδιο — obstacle", "δίπλωμα": "δίπλωμα — (driving) licence", "με την πρώτη": "με την πρώτη — at the first attempt", "χρησιμεύει": "χρησιμεύω — to be useful"}
})

ITEMS.append({
 "id": "l117-c1-chirokrotima", "title": "Γιατί χειροκροτούμε;", "title_en": "Why do we applaud?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν κοινωνικό ψυχολόγο σε μια διάλεξη για τη συμπεριφορά του πλήθους.",
 "script": [
  L("Ψυχολόγος", "m", "Χτυπάμε τις παλάμες μας για να δείξουμε ενθουσιασμό, ευγνωμοσύνη ή απλώς ευγένεια. Η συνήθεια είναι πανάρχαια: στο ρωμαϊκό θέατρο, το κοινό καλούνταν στο τέλος να χειροκροτήσει, και οι πηγές αναφέρουν ότι ο Νέρωνας είχε ομάδες νέων εκπαιδευμένων να τον επευφημούν. Τον δέκατο ένατο αιώνα, στις όπερες του Παρισιού, πληρωμένοι «κλακαδόροι» έδιναν το σύνθημα για τα χειροκροτήματα.", "We clap our palms to show enthusiasm, gratitude or simply politeness. The habit is ancient: in the Roman theatre, the audience was invited at the end to applaud, and the sources report that Nero had groups of young men trained to cheer him. In the nineteenth century, at the Paris operas, paid \"claqueurs\" gave the signal for applause."),
  L("Ψυχολόγος", "m", "Μια μελέτη του 2013 κατέγραψε με κάμερες φοιτητές που παρακολουθούσαν μικρές παρουσιάσεις. Διαπίστωσε ότι το χειροκρότημα εξαπλώνεται σαν μεταδοτικό: αρκεί ένα ή δύο άτομα να ξεκινήσουν για να ακολουθήσουν οι υπόλοιποι. Και, το πιο ενδιαφέρον, η διάρκειά του φαινόταν να εξαρτάται λιγότερο από την ποιότητα της παρουσίασης και περισσότερο από το πότε θα σταματήσουν οι άλλοι.", "A 2013 study filmed students watching short presentations. It found that applause spreads as if contagious: it takes only one or two people starting for the rest to follow. And, most interestingly, its length seemed to depend less on the quality of the presentation and more on when the others would stop."),
  L("Ψυχολόγος", "m", "Με άλλα λόγια, χειροκροτούμε συχνά όχι επειδή μας άρεσε τόσο, αλλά επειδή κανείς δεν θέλει να είναι ο πρώτος που θα σταματήσει, ούτε ο τελευταίος. Αυτό δεν κάνει το χειροκρότημα ψεύτικο. Δείχνει όμως ότι είναι, πάνω απ’ όλα, μια κοινωνική πράξη: ένας τρόπος να νιώσουμε για λίγα δευτερόλεπτα μέρος μιας ομάδας.", "In other words, we often applaud not because we liked it so much, but because nobody wants to be the first to stop, or the last. That doesn't make applause fake. But it shows that it is, above all, a social act: a way to feel part of a group for a few seconds."),
 ],
 "questions": [
  Q("Τι έκαναν οι «κλακαδόροι» στις όπερες του Παρισιού;", ["Πουλούσαν εισιτήρια", "Έδιναν το σύνθημα για τα χειροκροτήματα", "Έγραφαν κριτικές", "Τραγουδούσαν στη χορωδία"], 1, "πληρωμένοι «κλακαδόροι» έδιναν το σύνθημα για τα χειροκροτήματα"),
  Q("Τι διαπίστωσε η μελέτη του 2013 για την εξάπλωση του χειροκροτήματος;", ["Ότι αρκεί ένα ή δύο άτομα να ξεκινήσουν για να ακολουθήσουν οι υπόλοιποι", "Ότι ξεκινά πάντα από τις μπροστινές σειρές", "Ότι οι νέοι χειροκροτούν περισσότερο", "Ότι εξαρτάται από τον ομιλητή"], 0, "αρκεί ένα ή δύο άτομα να ξεκινήσουν για να ακολουθήσουν οι υπόλοιποι"),
  Q("Από τι φαινόταν να εξαρτάται κυρίως η διάρκεια του χειροκροτήματος;", ["Από την ποιότητα της παρουσίασης", "Από το μέγεθος της αίθουσας", "Από το πότε θα σταματήσουν οι άλλοι", "Από την ώρα της ημέρας"], 2, "περισσότερο από το πότε θα σταματήσουν οι άλλοι"),
  Q("Ποιο είναι το συμπέρασμα του ομιλητή;", ["Ότι το χειροκρότημα είναι ψεύτικο", "Ότι πρέπει να καταργηθεί", "Ότι είναι μια ρωμαϊκή εφεύρεση", "Ότι είναι πάνω απ’ όλα μια κοινωνική πράξη"], 3, "είναι, πάνω απ’ όλα, μια κοινωνική πράξη"),
 ],
 "gloss": {"χειροκροτούμε": "χειροκροτώ — to applaud", "παλάμες": "παλάμη — palm", "ευγνωμοσύνη": "ευγνωμοσύνη — gratitude", "πανάρχαια": "πανάρχαιος — ancient, age-old", "επευφημούν": "επευφημώ — to cheer, acclaim", "κλακαδόροι": "κλακαδόρος — claqueur, paid applauder", "σύνθημα": "σύνθημα — signal, cue", "εξαπλώνεται": "εξαπλώνομαι — to spread", "μεταδοτικό": "μεταδοτικός — contagious", "ψεύτικο": "ψεύτικος — fake", "πράξη": "πράξη — act"}
})

ITEMS.append({
 "id": "l117-c1-venetokratia-kritis", "title": "Η Βενετοκρατία στην Κρήτη", "title_en": "Venetian rule in Crete", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν ιστορικό σε εκπομπή για την ιστορία της Κρήτης.",
 "script": [
  L("Δημοσιογράφος", "f", "Περπατώντας στο Ηράκλειο ή στα Χανιά, βλέπει κανείς παντού ίχνη της Βενετίας. Πόσο κράτησε η βενετική κυριαρχία στο νησί;", "Walking around Heraklion or Chania, you see traces of Venice everywhere. How long did Venetian rule on the island last?"),
  L("Ιστορικός", "m", "Πάνω από τέσσερις αιώνες. Μετά την Τέταρτη Σταυροφορία, το 1204, η Βενετία απέκτησε την Κρήτη και την κράτησε ως το 1669. Ήταν για εκείνη πολύτιμη βάση στον δρόμο προς την Ανατολή. Η αρχή δεν ήταν ειρηνική: οι Κρητικοί ξεσηκώθηκαν πολλές φορές, ιδίως τους πρώτους αιώνες, και οι εξεγέρσεις καταστέλλονταν σκληρά.", "More than four centuries. After the Fourth Crusade, in 1204, Venice acquired Crete and kept it until 1669. For Venice it was a precious base on the route to the East. The beginning was not peaceful: the Cretans rose up many times, especially in the first centuries, and the revolts were harshly suppressed."),
  L("Δημοσιογράφος", "f", "Κι όμως, μιλάμε και για μια «κρητική αναγέννηση».", "And yet we also speak of a \"Cretan Renaissance\"."),
  L("Ιστορικός", "m", "Ακριβώς. Με τον καιρό, οι δύο κόσμοι πλησίασαν. Τον δέκατο έκτο και τον δέκατο έβδομο αιώνα, η επαφή με την ιταλική τέχνη γέννησε κάτι μοναδικό. Από τον Χάνδακα, το σημερινό Ηράκλειο, ξεκίνησε ο Δομήνικος Θεοτοκόπουλος, που έγινε γνωστός ως Ελ Γκρέκο. Στην ίδια εποχή ανήκει ο «Ερωτόκριτος» του Βιτσέντζου Κορνάρου, ένα έμμετρο ερωτικό έπος σε κρητική διάλεκτο που οι Κρητικοί τραγουδούν ακόμη και σήμερα.", "Exactly. Over time, the two worlds drew closer. In the sixteenth and seventeenth centuries, contact with Italian art gave birth to something unique. From Candia, today's Heraklion, came Domenikos Theotokopoulos, who became known as El Greco. To the same era belongs the \"Erotokritos\" by Vitsentzos Kornaros, a verse romance in the Cretan dialect that Cretans still sing today."),
  L("Δημοσιογράφος", "f", "Και πώς τελείωσε αυτή η περίοδος;", "And how did this period end?"),
  L("Ιστορικός", "m", "Με μια από τις μεγαλύτερες πολιορκίες της ιστορίας. Οι Οθωμανοί πολιόρκησαν τον Χάνδακα για περίπου είκοσι ένα χρόνια, ώσπου η πόλη παραδόθηκε το 1669. Πολλοί λόγιοι και καλλιτέχνες κατέφυγαν τότε στα Επτάνησα, που έμειναν βενετικά ως το 1797, και μετέφεραν εκεί την κρητική παράδοση. Έτσι, κατά κάποιον τρόπο, η κρητική αναγέννηση δεν έσβησε· άλλαξε απλώς νησί.", "With one of the longest sieges in history. The Ottomans besieged Candia for about twenty-one years, until the city surrendered in 1669. Many scholars and artists then fled to the Ionian Islands, which remained Venetian until 1797, and took the Cretan tradition there. So, in a way, the Cretan Renaissance did not die out; it simply changed islands."),
 ],
 "questions": [
  Q("Γιατί ήταν πολύτιμη η Κρήτη για τη Βενετία;", ["Για τα ορυχεία της", "Ως βάση στον δρόμο προς την Ανατολή", "Για τα δάση της", "Ως τόπος εξορίας"], 1, "Ήταν για εκείνη πολύτιμη βάση στον δρόμο προς την Ανατολή"),
  Q("Πώς ήταν οι πρώτοι αιώνες της βενετικής κυριαρχίας;", ["Ειρηνικοί και ήσυχοι", "Χωρίς καμία επαφή ανάμεσα στους δύο λαούς", "Με πολλές εξεγέρσεις που καταστέλλονταν σκληρά", "Με μεγάλη οικονομική άνθηση για όλους"], 2, "οι Κρητικοί ξεσηκώθηκαν πολλές φορές, ιδίως τους πρώτους αιώνες"),
  Q("Τι είναι ο «Ερωτόκριτος»;", ["Ένα έμμετρο ερωτικό έπος σε κρητική διάλεκτο", "Ένας πίνακας του Ελ Γκρέκο", "Μια βενετική εκκλησία", "Ένα ιστορικό χρονικό της πολιορκίας"], 0, "ένα έμμετρο ερωτικό έπος σε κρητική διάλεκτο"),
  Q("Τι εννοεί ο ιστορικός λέγοντας ότι η κρητική αναγέννηση «άλλαξε απλώς νησί»;", ["Ότι οι Βενετοί την έφεραν στη Βενετία", "Ότι ξεχάστηκε εντελώς", "Ότι συνεχίστηκε στη Ρόδο", "Ότι λόγιοι και καλλιτέχνες τη μετέφεραν στα Επτάνησα"], 3, "μετέφεραν εκεί την κρητική παράδοση"),
 ],
 "gloss": {"ίχνη": "ίχνος — trace", "κυριαρχία": "κυριαρχία — rule, domination", "Σταυροφορία": "Σταυροφορία — Crusade", "ξεσηκώθηκαν": "ξεσηκώνομαι — to rise up, revolt", "εξεγέρσεις": "εξέγερση — revolt, uprising", "καταστέλλονταν": "καταστέλλω — to suppress", "αναγέννηση": "αναγέννηση — renaissance", "Χάνδακα": "Χάνδακας — Candia (Venetian name of Heraklion)", "έμμετρο": "έμμετρος — in verse", "έπος": "έπος — epic", "πολιορκίες": "πολιορκία — siege", "κατέφυγαν": "καταφεύγω — to take refuge, flee"}
})

rnd = random.Random(117)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-117.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
