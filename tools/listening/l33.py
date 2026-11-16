# Source for library/listening/listening-33.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l33.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l33-ann-psifoforia", "title": "Οδηγίες για την ψηφοφορία", "title_en": "Instructions for voting", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση στο ραδιόφωνο λίγες μέρες πριν από τις εκλογές.",
 "script": [
  L("Εκφωνήτρια", "f", "Το Υπουργείο Εσωτερικών υπενθυμίζει ότι την ερχόμενη Κυριακή τα εκλογικά τμήματα θα λειτουργήσουν από τις επτά το πρωί έως τις επτά το απόγευμα. Οι ψηφοφόροι μπορούν να βρουν πού ψηφίζουν στην ειδική ιστοσελίδα του υπουργείου, πληκτρολογώντας τα στοιχεία τους.", "The Ministry of the Interior reminds you that next Sunday polling stations will be open from seven in the morning until seven in the evening. Voters can find out where they vote on the ministry's special website by typing in their details."),
  L("Εκφωνήτρια", "f", "Για να ψηφίσετε, πρέπει να έχετε μαζί σας την αστυνομική σας ταυτότητα ή το διαβατήριό σας. Τα εκλογικά βιβλιάρια δεν χρειάζονται πια. Όσοι έχουν κινητικά προβλήματα μπορούν να ζητήσουν βοήθεια από την εφορευτική επιτροπή, ενώ πολλά τμήματα βρίσκονται σε ισόγεια με ράμπα.", "To vote, you must have your police ID card or passport with you. Electoral booklets are no longer needed. Those with mobility problems can ask the polling committee for help, while many stations are on ground floors with a ramp."),
  L("Εκφωνήτρια", "f", "Θυμίζουμε ότι απαγορεύεται η χρήση κινητού τηλεφώνου μέσα στο παραβάν και η φωτογράφιση του ψηφοδελτίου. Η ψήφος είναι μυστική.", "We remind you that using a mobile phone inside the voting booth and photographing the ballot paper are forbidden. The vote is secret."),
 ],
 "questions": [
  Q("Πώς μπορούν οι ψηφοφόροι να μάθουν πού ψηφίζουν;", ["Τηλεφωνώντας στον δήμο", "Από μια ειδική ιστοσελίδα του υπουργείου", "Από ένα γράμμα που θα λάβουν", "Ρωτώντας στο αστυνομικό τμήμα"], 1, "στην ειδική ιστοσελίδα του υπουργείου"),
  Q("Τι χρειάζεται κανείς για να ψηφίσει;", ["Το εκλογικό βιβλιάριο", "Την ταυτότητα ή το διαβατήριο", "Το δίπλωμα οδήγησης", "Μια βεβαίωση από τον δήμο"], 1, "την αστυνομική σας ταυτότητα ή το διαβατήριό σας"),
  Q("Τι απαγορεύεται μέσα στο παραβάν;", ["Να μιλάει κανείς", "Η χρήση κινητού και η φωτογράφιση του ψηφοδελτίου", "Να μπαίνουν δύο άτομα", "Να χρησιμοποιεί κανείς στυλό"], 1, "απαγορεύεται η χρήση κινητού τηλεφώνου μέσα στο παραβάν"),
 ],
 "gloss": {"εκλογές": "εκλογές — elections", "εκλογικά τμήματα": "εκλογικό τμήμα — polling station", "ψηφοφόροι": "ψηφοφόρος — voter", "πληκτρολογώντας": "πληκτρολογώ — to type", "εκλογικά βιβλιάρια": "εκλογικό βιβλιάριο — electoral booklet", "εφορευτική επιτροπή": "εφορευτική επιτροπή — polling committee", "ράμπα": "ράμπα — ramp", "παραβάν": "παραβάν — voting booth, screen", "ψηφοδελτίου": "ψηφοδέλτιο — ballot paper", "μυστική": "μυστικός — secret"},
})

ITEMS.append({
 "id": "l33-vm-thermosifonas", "title": "Μήνυμα για τον ηλιακό θερμοσίφωνα", "title_en": "A message about the solar water heater", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από έναν τεχνικό.",
 "script": [
  L("Τεχνικός", "m", "Καλημέρα σας, ο Παύλος είμαι, ο τεχνικός που ήρθε την Τρίτη για τον ηλιακό σας θερμοσίφωνα. Βρήκα το πρόβλημα: το νερό δεν ζεσταίνεται γιατί έχει χαλάσει η ηλεκτρική αντίσταση, και επιπλέον υπάρχουν πολλά άλατα στο μπόιλερ, επειδή το νερό στην περιοχή σας είναι πολύ σκληρό.", "Good morning, it's Pavlos, the technician who came on Tuesday about your solar water heater. I've found the problem: the water isn't heating because the electric element has broken, and on top of that there's a lot of limescale in the boiler, because the water in your area is very hard."),
  L("Τεχνικός", "m", "Η αντίσταση κοστίζει σαράντα ευρώ και ο καθαρισμός του μπόιλερ άλλα εξήντα, μαζί με την εργασία. Επειδή όμως ο θερμοσίφωνάς σας είναι δεκαοχτώ χρονών, σκεφτείτε μήπως αξίζει να τον αλλάξετε. Ένας καινούργιος κοστίζει γύρω στα οχτακόσια, αλλά υπάρχει επιδότηση από το πρόγραμμα του κράτους, που καλύπτει μέρος του κόστους.", "The element costs forty euros and cleaning the boiler another sixty, including labour. But since your water heater is eighteen years old, consider whether it's worth replacing. A new one costs around eight hundred, but there's a subsidy from the state programme, which covers part of the cost."),
  L("Τεχνικός", "m", "Αν θέλετε να κάνουμε μόνο την επισκευή, μπορώ να έρθω την Πέμπτη το πρωί. Πείτε μου όμως μέχρι αύριο, για να παραγγείλω το ανταλλακτικό.", "If you want us to do just the repair, I can come on Thursday morning. But let me know by tomorrow, so I can order the spare part."),
 ],
 "questions": [
  Q("Γιατί υπάρχουν πολλά άλατα στο μπόιλερ;", ["Γιατί δεν καθαρίστηκε ποτέ", "Γιατί το νερό στην περιοχή είναι πολύ σκληρό", "Γιατί έχει σπάσει ο σωλήνας", "Γιατί δεν έχει ήλιο"], 1, "το νερό στην περιοχή σας είναι πολύ σκληρό"),
  Q("Τι προτείνει ο τεχνικός να σκεφτεί ο πελάτης;", ["Να βάλει κλιματιστικό", "Μήπως αξίζει να αλλάξει τον θερμοσίφωνα", "Να μετακομίσει", "Να καθαρίζει μόνος του το μπόιλερ"], 1, "σκεφτείτε μήπως αξίζει να τον αλλάξετε"),
  Q("Γιατί θέλει απάντηση μέχρι αύριο;", ["Για να κλείσει το ραντεβού με άλλον πελάτη", "Για να παραγγείλει το ανταλλακτικό", "Για να κάνει αίτηση για την επιδότηση", "Γιατί φεύγει διακοπές"], 1, "για να παραγγείλω το ανταλλακτικό"),
 ],
 "gloss": {"ηλιακό": "ηλιακός — solar", "θερμοσίφωνα": "θερμοσίφωνας — water heater", "ζεσταίνεται": "ζεσταίνομαι — to heat up", "αντίσταση": "αντίσταση — heating element", "άλατα": "άλατα — limescale", "μπόιλερ": "μπόιλερ — boiler, tank", "σκληρό": "σκληρός (νερό) — hard (water)", "εργασία": "εργασία — labour", "επιδότηση": "επιδότηση — subsidy", "επισκευή": "επισκευή — repair", "ανταλλακτικό": "ανταλλακτικό — spare part"},
})

ITEMS.append({
 "id": "l33-dia-afxisi", "title": "Ζητώντας αύξηση", "title_en": "Asking for a pay rise", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο ανάμεσα σε μια υπάλληλο και τον προϊστάμενό της.",
 "script": [
  L("Άννα", "f", "Κύριε Δημητρίου, ευχαριστώ που βρήκατε χρόνο. Ήθελα να συζητήσουμε τον μισθό μου. Δουλεύω στην εταιρεία τρία χρόνια, και τον τελευταίο χρόνο έχω αναλάβει και την εξυπηρέτηση των πελατών του εξωτερικού, χωρίς καμία αλλαγή στις αποδοχές μου.", "Mr Dimitriou, thank you for finding the time. I wanted to discuss my salary. I've worked at the company for three years, and in the last year I've also taken on serving our foreign customers, without any change in my pay."),
  L("Προϊστάμενος", "m", "Το ξέρω, Άννα, και είμαι πολύ ικανοποιημένος από τη δουλειά σου. Οι πωλήσεις στο εξωτερικό αυξήθηκαν σχεδόν είκοσι τοις εκατό. Ο προϋπολογισμός όμως για φέτος έχει ήδη κλείσει.", "I know, Anna, and I'm very satisfied with your work. Foreign sales rose almost twenty per cent. But this year's budget has already been closed."),
  L("Άννα", "f", "Το καταλαβαίνω. Θα μπορούσαμε τότε να συμφωνήσουμε τώρα σε μια αύξηση από τον Ιανουάριο; Και στο μεταξύ, ίσως δύο μέρες τηλεργασίας την εβδομάδα, που για μένα θα σήμαινε πολύ λιγότερες ώρες στον δρόμο.", "I understand. Could we then agree now on a raise from January? And in the meantime, perhaps two days of remote work a week, which for me would mean far fewer hours on the road."),
  L("Προϊστάμενος", "m", "Η τηλεργασία δεν είναι πρόβλημα, μπορούμε να την ξεκινήσουμε από τον επόμενο μήνα. Για την αύξηση, θα το θέσω στη διοίκηση με τη δική μου θετική εισήγηση. Ετοίμασέ μου ένα σύντομο σημείωμα με τα αποτελέσματά σου, για να το έχω μαζί μου στη συνάντηση.", "Remote work isn't a problem; we can start it next month. As for the raise, I'll put it to management with my own positive recommendation. Prepare me a short note with your results, so I have it with me at the meeting."),
 ],
 "questions": [
  Q("Γιατί πιστεύει η Άννα ότι αξίζει αύξηση;", ["Γιατί δουλεύει εκεί δέκα χρόνια", "Γιατί έχει αναλάβει επιπλέον ευθύνες χωρίς αλλαγή μισθού", "Γιατί της πρότειναν δουλειά αλλού", "Γιατί μετακόμισε"], 1, "έχω αναλάβει και την εξυπηρέτηση των πελατών του εξωτερικού, χωρίς καμία αλλαγή στις αποδοχές μου"),
  Q("Γιατί δεν μπορεί να δοθεί αύξηση αμέσως;", ["Γιατί η εταιρεία έχει ζημιές", "Γιατί ο προϋπολογισμός για φέτος έχει κλείσει", "Γιατί ο προϊστάμενος δεν είναι ικανοποιημένος", "Γιατί μειώθηκαν οι πωλήσεις"], 1, "Ο προϋπολογισμός όμως για φέτος έχει ήδη κλείσει"),
  Q("Τι ζητάει ο προϊστάμενος από την Άννα;", ["Να δουλέψει περισσότερες ώρες", "Ένα σύντομο σημείωμα με τα αποτελέσματά της", "Να μιλήσει η ίδια στη διοίκηση", "Να περιμένει έναν χρόνο"], 1, "Ετοίμασέ μου ένα σύντομο σημείωμα με τα αποτελέσματά σου"),
 ],
 "gloss": {"προϊστάμενό": "προϊστάμενος — manager, boss", "μισθό": "μισθός — salary", "έχω αναλάβει": "αναλαμβάνω — to take on", "αποδοχές": "αποδοχές — pay, earnings", "πωλήσεις": "πωλήσεις — sales", "προϋπολογισμός": "προϋπολογισμός — budget", "αύξηση": "αύξηση — rise, raise", "τηλεργασίας": "τηλεργασία — remote work", "διοίκηση": "διοίκηση — management", "εισήγηση": "εισήγηση — recommendation, proposal", "σημείωμα": "σημείωμα — note, memo"},
})

ITEMS.append({
 "id": "l33-dia-katadyseis", "title": "Εγγραφή σε σχολή καταδύσεων", "title_en": "Signing up at a diving school", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε μια σχολή καταδύσεων στη Χαλκιδική.",
 "script": [
  L("Πελάτης", "m", "Γεια σας. Θα ήθελα να κάνω το βασικό σεμινάριο καταδύσεων. Δεν έχω βουτήξει ποτέ με φιάλη, αλλά κολυμπάω αρκετά καλά.", "Hello. I'd like to do the basic diving course. I've never dived with a tank, but I swim quite well."),
  L("Εκπαιδεύτρια", "f", "Ωραία. Το σεμινάριο διαρκεί τέσσερις μέρες. Τις δύο πρώτες κάνουμε θεωρία και ασκήσεις σε ρηχά νερά, κοντά στην ακτή, και τις άλλες δύο τέσσερις καταδύσεις στη θάλασσα, μέχρι δώδεκα μέτρα βάθος. Στο τέλος παίρνετε δίπλωμα που ισχύει σε όλο τον κόσμο.", "Great. The course lasts four days. For the first two we do theory and exercises in shallow water, close to the shore, and for the other two four dives in the sea, down to twelve metres deep. At the end you get a certificate valid all over the world."),
  L("Πελάτης", "m", "Χρειάζεται κάτι από μένα;", "Do you need anything from me?"),
  L("Εκπαιδεύτρια", "f", "Θα συμπληρώσετε ένα ερωτηματολόγιο υγείας. Αν απαντήσετε «ναι» σε κάποια ερώτηση, για παράδειγμα για άσθμα ή προβλήματα στα αυτιά, θα χρειαστεί βεβαίωση από γιατρό πριν μπείτε στο νερό. Και κάτι σημαντικό: μετά την τελευταία κατάδυση πρέπει να περιμένετε τουλάχιστον μία μέρα πριν πετάξετε με αεροπλάνο.", "You'll fill in a health questionnaire. If you answer «yes» to any question, for example about asthma or ear problems, you'll need a certificate from a doctor before you go in the water. And something important: after the last dive you must wait at least one day before flying."),
 ],
 "questions": [
  Q("Τι κάνουν οι μαθητές τις δύο πρώτες μέρες;", ["Καταδύσεις σε βαθιά νερά", "Θεωρία και ασκήσεις σε ρηχά νερά", "Μόνο θεωρία στο γραφείο", "Κολύμπι στην πισίνα"], 1, "Τις δύο πρώτες κάνουμε θεωρία και ασκήσεις σε ρηχά νερά"),
  Q("Πότε χρειάζεται βεβαίωση από γιατρό;", ["Πάντα", "Αν απαντήσει «ναι» σε κάποια ερώτηση υγείας", "Αν είναι πάνω από πενήντα χρονών", "Μόνο για καταδύσεις κάτω από δώδεκα μέτρα"], 1, "Αν απαντήσετε «ναι» σε κάποια ερώτηση"),
  Q("Τι πρέπει να προσέξει μετά την τελευταία κατάδυση;", ["Να μην κολυμπήσει", "Να περιμένει τουλάχιστον μία μέρα πριν πετάξει", "Να μην τρώει για δύο ώρες", "Να επιστρέψει τη φιάλη την ίδια μέρα"], 1, "πρέπει να περιμένετε τουλάχιστον μία μέρα πριν πετάξετε με αεροπλάνο"),
 ],
 "gloss": {"καταδύσεων": "κατάδυση — dive, diving", "σεμινάριο": "σεμινάριο — course", "βουτήξει": "βουτάω — to dive", "φιάλη": "φιάλη — (air) tank", "ρηχά": "ρηχός — shallow", "ακτή": "ακτή — shore", "βάθος": "βάθος — depth", "ισχύει": "ισχύω — to be valid", "ερωτηματολόγιο": "ερωτηματολόγιο — questionnaire", "άσθμα": "άσθμα — asthma", "πετάξετε": "πετάω — to fly"},
})

ITEMS.append({
 "id": "l33-mono-xorodia", "title": "Τραγουδώντας σε χορωδία", "title_en": "Singing in a choir", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλάει για τη δημοτική χορωδία της πόλης του.",
 "script": [
  L("Θοδωρής", "m", "Πριν από πέντε χρόνια, όταν πήρα σύνταξη, η κόρη μου με γράφτηκε σχεδόν με το ζόρι στη δημοτική χορωδία. Φοβόταν ότι θα καθόμουν όλη μέρα μπροστά στην τηλεόραση. Εγώ δεν είχα τραγουδήσει ποτέ, εκτός από το μπάνιο.", "Five years ago, when I retired, my daughter signed me up, almost by force, for the municipal choir. She was afraid I'd sit in front of the television all day. I'd never sung, except in the shower."),
  L("Θοδωρής", "m", "Στην πρώτη πρόβα ήθελα να ανοίξει η γη να με καταπιεί. Η μαέστρος, όμως, μια νεαρή μουσικός με απίστευτη υπομονή, μου εξήγησε ότι σε μια χορωδία κανείς δεν τραγουδάει μόνος: ακούς τους διπλανούς σου και προσαρμόζεσαι. Με έβαλε στους βαρύτονους, δίπλα σε έναν ηλικιωμένο ψάλτη, που με βοήθησε πολύ.", "At the first rehearsal I wanted the ground to open and swallow me. The conductor, though, a young musician with incredible patience, explained to me that in a choir no one sings alone: you listen to those next to you and adjust. She put me with the baritones, next to an elderly church cantor, who helped me a lot."),
  L("Θοδωρής", "m", "Σήμερα κάνουμε πρόβες δύο φορές την εβδομάδα και δίνουμε συναυλίες σε εκκλησίες, σε πλατείες, ακόμη και σε γηροκομεία. Έχω κάνει φίλους που δεν θα γνώριζα ποτέ, και ο γιατρός μου λέει ότι η αναπνοή μου βελτιώθηκε. Το πιο σπουδαίο όμως είναι η στιγμή που σαράντα φωνές γίνονται μία.", "Today we rehearse twice a week and give concerts in churches, in squares, even in care homes. I've made friends I'd never have met, and my doctor says my breathing has improved. But the greatest thing is the moment when forty voices become one."),
 ],
 "questions": [
  Q("Γιατί τον έγραψε η κόρη του στη χορωδία;", ["Γιατί τραγουδούσε πολύ ωραία", "Γιατί φοβόταν ότι θα καθόταν όλη μέρα μπροστά στην τηλεόραση", "Γιατί ήθελε να έρθει κι εκείνη", "Γιατί το πρότεινε ο γιατρός"], 1, "Φοβόταν ότι θα καθόμουν όλη μέρα μπροστά στην τηλεόραση"),
  Q("Τι του εξήγησε η μαέστρος;", ["Ότι πρέπει να κάνει μαθήματα φωνητικής", "Ότι σε μια χορωδία ακούς τους διπλανούς σου και προσαρμόζεσαι", "Ότι θα τραγουδήσει σόλο", "Ότι πρέπει να μάθει νότες"], 1, "ακούς τους διπλανούς σου και προσαρμόζεσαι"),
  Q("Ποιο είναι για τον Θοδωρή το πιο σπουδαίο;", ["Οι συναυλίες στις πλατείες", "Η στιγμή που σαράντα φωνές γίνονται μία", "Η βελτίωση της αναπνοής του", "Τα ταξίδια της χορωδίας"], 1, "η στιγμή που σαράντα φωνές γίνονται μία"),
 ],
 "gloss": {"χορωδία": "χορωδία — choir", "πήρα σύνταξη": "παίρνω σύνταξη — to retire", "με το ζόρι": "με το ζόρι — by force, reluctantly", "πρόβα": "πρόβα — rehearsal", "να με καταπιεί": "καταπίνω — to swallow", "μαέστρος": "μαέστρος — conductor", "προσαρμόζεσαι": "προσαρμόζομαι — to adjust, adapt", "βαρύτονους": "βαρύτονος — baritone", "ψάλτη": "ψάλτης — church cantor", "γηροκομεία": "γηροκομείο — care home", "αναπνοή": "αναπνοή — breathing"},
})

ITEMS.append({
 "id": "l33-rep-kalymnos", "title": "Αναρρίχηση στην Κάλυμνο", "title_en": "Climbing on Kalymnos", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ για την Κάλυμνο.",
 "script": [
  L("Ρεπόρτερ", "m", "Για αιώνες η Κάλυμνος ήταν το νησί των σφουγγαράδων. Οι άντρες έφευγαν κάθε άνοιξη για μήνες, για να βουτήξουν στα βάθη της Μεσογείου, και πολλοί δεν γύριζαν ποτέ. Όταν η σφουγγαραλιεία παρήκμασε, το νησί άρχισε να χάνει τους νέους του.", "For centuries Kalymnos was the island of sponge divers. The men left every spring for months to dive in the depths of the Mediterranean, and many never returned. When sponge fishing declined, the island began to lose its young people."),
  L("Ρεπόρτερ", "m", "Τη δεκαετία του '90 ένας Ιταλός ορειβάτης ανακάλυψε ότι οι ασβεστολιθικοί βράχοι του νησιού ήταν ιδανικοί για αναρρίχηση. Σήμερα υπάρχουν πάνω από τρεις χιλιάδες διαδρομές, και η Κάλυμνος θεωρείται ένας από τους καλύτερους προορισμούς αναρρίχησης στον κόσμο.", "In the 1990s an Italian climber discovered that the island's limestone cliffs were ideal for climbing. Today there are more than three thousand routes, and Kalymnos is considered one of the best climbing destinations in the world."),
  L("Ρεπόρτερ", "m", "Το σημαντικότερο είναι ότι οι αναρριχητές έρχονται κυρίως την άνοιξη και το φθινόπωρο, όταν ο καύσωνας δεν επιτρέπει το σκαρφάλωμα σε άλλα μέρη. Έτσι, η τουριστική περίοδος έχει μεγαλώσει, και αρκετοί νέοι Καλύμνιοι έγιναν οι ίδιοι οδηγοί αναρρίχησης αντί να μεταναστεύσουν.", "Most importantly, climbers come mainly in spring and autumn, when heat doesn't prevent climbing elsewhere. So the tourist season has grown longer, and quite a few young Kalymnians have become climbing guides themselves instead of emigrating."),
 ],
 "questions": [
  Q("Τι συνέβη όταν παρήκμασε η σφουγγαραλιεία;", ["Το νησί γέμισε τουρίστες", "Το νησί άρχισε να χάνει τους νέους του", "Οι σφουγγαράδες έγιναν ψαράδες", "Άνοιξε ένα μουσείο"], 1, "το νησί άρχισε να χάνει τους νέους του"),
  Q("Τι ανακάλυψε ένας Ιταλός ορειβάτης;", ["Ένα αρχαίο ναυάγιο", "Ότι οι βράχοι ήταν ιδανικοί για αναρρίχηση", "Μια σπηλιά με σφουγγάρια", "Ένα νέο μονοπάτι"], 1, "οι ασβεστολιθικοί βράχοι του νησιού ήταν ιδανικοί για αναρρίχηση"),
  Q("Γιατί η αναρρίχηση βοήθησε την τοπική οικονομία;", ["Γιατί οι αναρριχητές ξοδεύουν πολλά", "Γιατί οι αναρριχητές έρχονται την άνοιξη και το φθινόπωρο και μεγάλωσε η τουριστική περίοδος", "Γιατί χτίστηκαν μεγάλα ξενοδοχεία", "Γιατί το κράτος έδωσε επιδοτήσεις"], 1, "η τουριστική περίοδος έχει μεγαλώσει"),
 ],
 "gloss": {"σφουγγαράδων": "σφουγγαράς — sponge diver", "βάθη": "βάθος — depth", "σφουγγαραλιεία": "σφουγγαραλιεία — sponge fishing", "παρήκμασε": "παρακμάζω — to decline", "ορειβάτης": "ορειβάτης — mountaineer, climber", "ασβεστολιθικοί": "ασβεστολιθικός — limestone", "βράχοι": "βράχος — rock, cliff", "αναρρίχηση": "αναρρίχηση — (rock) climbing", "διαδρομές": "διαδρομή — route", "αναρριχητές": "αναρριχητής — climber", "σκαρφάλωμα": "σκαρφάλωμα — climbing"},
})

ITEMS.append({
 "id": "l33-rep-apografi", "title": "Τι έδειξε η απογραφή", "title_en": "What the census showed", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τα αποτελέσματα της απογραφής του 2021.",
 "script": [
  L("Ρεπόρτερ", "f", "Σύμφωνα με την απογραφή του 2021, ο πληθυσμός της Ελλάδας ήταν περίπου δέκα εκατομμύρια τετρακόσιες χιλιάδες, δηλαδή μειώθηκε κατά περίπου τρία τοις εκατό σε σχέση με το 2011. Οι ειδικοί αποδίδουν τη μείωση σε δύο κυρίως αιτίες: στη χαμηλή γεννητικότητα και στη μετανάστευση χιλιάδων νέων στα χρόνια της κρίσης.", "According to the 2021 census, Greece's population was about ten million four hundred thousand, that is, it fell by about three per cent compared with 2011. Experts attribute the decline mainly to two causes: the low birth rate and the emigration of thousands of young people during the crisis years."),
  L("Ρεπόρτερ", "f", "Η μείωση δεν είναι ίδια παντού. Ενώ η Αττική και ορισμένα νησιά διατήρησαν ή και αύξησαν τον πληθυσμό τους, πολλές ορεινές περιοχές χάνουν κατοίκους με ταχύ ρυθμό. Υπάρχουν χωριά όπου τον χειμώνα μένουν λιγότεροι από δέκα άνθρωποι, όλοι ηλικιωμένοι.", "The decline is not the same everywhere. While Attica and certain islands kept or even increased their population, many mountain areas are losing residents at a fast rate. There are villages where in winter fewer than ten people remain, all of them elderly."),
  L("Ρεπόρτερ", "f", "Οι δημογράφοι προειδοποιούν ότι, χωρίς μέτρα για τη στήριξη των οικογενειών και την επιστροφή όσων έφυγαν, ο πληθυσμός θα συνεχίσει να μειώνεται και να γερνάει τις επόμενες δεκαετίες, με σοβαρές συνέπειες για τις συντάξεις και το σύστημα υγείας.", "Demographers warn that without measures to support families and bring back those who left, the population will keep shrinking and ageing in the coming decades, with serious consequences for pensions and the health system."),
 ],
 "questions": [
  Q("Πώς άλλαξε ο πληθυσμός σε σχέση με το 2011;", ["Αυξήθηκε κατά τρία τοις εκατό", "Μειώθηκε κατά περίπου τρία τοις εκατό", "Έμεινε ίδιος", "Μειώθηκε στο μισό"], 1, "μειώθηκε κατά περίπου τρία τοις εκατό σε σχέση με το 2011"),
  Q("Ποιες περιοχές χάνουν κατοίκους με ταχύ ρυθμό;", ["Η Αττική", "Πολλές ορεινές περιοχές", "Όλα τα νησιά", "Οι μεγάλες πόλεις"], 1, "πολλές ορεινές περιοχές χάνουν κατοίκους με ταχύ ρυθμό"),
  Q("Για τι προειδοποιούν οι δημογράφοι;", ["Για υπερπληθυσμό", "Ότι ο πληθυσμός θα συνεχίσει να μειώνεται και να γερνάει", "Ότι οι νέοι θα επιστρέψουν σύντομα", "Ότι θα κλείσουν τα σχολεία των πόλεων"], 1, "ο πληθυσμός θα συνεχίσει να μειώνεται και να γερνάει"),
 ],
 "gloss": {"απογραφής": "απογραφή — census", "πληθυσμός": "πληθυσμός — population", "μείωση": "μείωση — decline, reduction", "αποδίδουν": "αποδίδω — to attribute", "γεννητικότητα": "γεννητικότητα — birth rate", "μετανάστευση": "μετανάστευση — emigration", "ορεινές": "ορεινός — mountainous", "ρυθμό": "ρυθμός — rate, pace", "δημογράφοι": "δημογράφος — demographer", "στήριξη": "στήριξη — support", "γερνάει": "γερνάω — to age, grow old", "συντάξεις": "σύνταξη — pension"},
})

ITEMS.append({
 "id": "l33-int-diaititria", "title": "Μια γυναίκα διαιτητής", "title_en": "A woman referee", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια διαιτητή ποδοσφαίρου.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς αποφασίσατε να γίνετε διαιτητής;", "How did you decide to become a referee?"),
  L("Κατερίνα", "f", "Έπαιζα ποδόσφαιρο από μικρή, αλλά στα δεκαεννιά τραυματίστηκα στο γόνατο και δεν μπορούσα πια να παίζω σε υψηλό επίπεδο. Ένας προπονητής μού πρότεινε να δοκιμάσω τη διαιτησία, για να μείνω κοντά στο γήπεδο. Στην αρχή το είδα σαν παρηγοριά· σήμερα είναι το πάθος μου.", "I played football from a young age, but at nineteen I injured my knee and could no longer play at a high level. A coach suggested I try refereeing, to stay close to the pitch. At first I saw it as a consolation; today it's my passion."),
  L("Δημοσιογράφος", "m", "Αντιμετωπίσατε δυσκολίες επειδή είστε γυναίκα;", "Did you face difficulties because you're a woman?"),
  L("Κατερίνα", "f", "Φυσικά. Στους πρώτους αγώνες άκουγα από την κερκίδα σχόλια που δεν θα άκουγε ποτέ ένας άντρας συνάδελφος. Έμαθα όμως να μην τα παίρνω προσωπικά. Οι παίκτες, εξάλλου, με κρίνουν από τις αποφάσεις μου, όχι από το φύλο μου. Αν σφυρίξω σωστά, με σέβονται.", "Of course. In the first matches I heard comments from the stands that a male colleague would never hear. But I learned not to take them personally. The players, after all, judge me by my decisions, not my gender. If I whistle correctly, they respect me."),
  L("Δημοσιογράφος", "m", "Τι συμβουλή θα δίνατε σε ένα κορίτσι που θέλει να ακολουθήσει τον δρόμο σας;", "What advice would you give a girl who wants to follow your path?"),
  L("Κατερίνα", "f", "Να προπονείται σκληρά, γιατί ένας διαιτητής τρέχει πάνω από δέκα χιλιόμετρα σε κάθε αγώνα, και να μελετάει τους κανονισμούς σαν να δίνει εξετάσεις. Και να θυμάται ότι τα λάθη είναι μέρος της δουλειάς· το σημαντικό είναι να μαθαίνεις από αυτά.", "To train hard, because a referee runs more than ten kilometres in every match, and to study the rules as if sitting exams. And to remember that mistakes are part of the job; the important thing is to learn from them."),
 ],
 "questions": [
  Q("Γιατί η Κατερίνα σταμάτησε να παίζει σε υψηλό επίπεδο;", ["Γιατί προτίμησε τις σπουδές", "Γιατί τραυματίστηκε στο γόνατο", "Γιατί διαλύθηκε η ομάδα της", "Γιατί μετακόμισε"], 1, "στα δεκαεννιά τραυματίστηκα στο γόνατο"),
  Q("Πώς την κρίνουν οι παίκτες, σύμφωνα με την ίδια;", ["Από την εμφάνισή της", "Από τις αποφάσεις της", "Από την ηλικία της", "Από την ομάδα όπου έπαιζε"], 1, "με κρίνουν από τις αποφάσεις μου, όχι από το φύλο μου"),
  Q("Τι λέει για τα λάθη;", ["Ότι δεν πρέπει να γίνονται ποτέ", "Ότι είναι μέρος της δουλειάς και μαθαίνεις από αυτά", "Ότι φταίνε οι παίκτες", "Ότι τα διορθώνει η τεχνολογία"], 1, "τα λάθη είναι μέρος της δουλειάς"),
 ],
 "gloss": {"διαιτητή": "διαιτητής — referee", "τραυματίστηκα": "τραυματίζομαι — to be injured", "γόνατο": "γόνατο — knee", "διαιτησία": "διαιτησία — refereeing", "γήπεδο": "γήπεδο — pitch, ground", "παρηγοριά": "παρηγοριά — consolation", "κερκίδα": "κερκίδα — stand(s)", "συνάδελφος": "συνάδελφος — colleague", "φύλο": "φύλο — gender, sex", "σφυρίξω": "σφυρίζω — to whistle", "κανονισμούς": "κανονισμός — rule, regulation"},
})

ITEMS.append({
 "id": "l33-mono-erotokritos", "title": "Ο Ερωτόκριτος", "title_en": "The Erotokritos", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε έναν φιλόλογο να μιλάει σε μια διάλεξη για τον «Ερωτόκριτο».",
 "script": [
  L("Φιλόλογος", "m", "Ο «Ερωτόκριτος» γράφτηκε στην Κρήτη γύρω στο 1600, όταν το νησί βρισκόταν ακόμη υπό βενετική κυριαρχία, από τον Βιτσέντζο Κορνάρο, για τον οποίο ελάχιστα γνωρίζουμε με βεβαιότητα. Πρόκειται για ένα έμμετρο μυθιστόρημα με περισσότερους από δέκα χιλιάδες ομοιοκατάληκτους δεκαπεντασύλλαβους, γραμμένους στην κρητική διάλεκτο.", "The «Erotokritos» was written in Crete around 1600, while the island was still under Venetian rule, by Vitsentzos Kornaros, about whom we know very little with certainty. It is a verse romance of more than ten thousand rhyming fifteen-syllable lines, written in the Cretan dialect."),
  L("Φιλόλογος", "m", "Η υπόθεση, η αγάπη του Ερωτόκριτου για την Αρετούσα, την κόρη του βασιλιά της Αθήνας, δεν είναι πρωτότυπη: ο Κορνάρος βασίστηκε σε ένα γαλλικό ιπποτικό μυθιστόρημα, πιθανότατα μέσω μιας ιταλικής διασκευής. Η πρωτοτυπία του βρίσκεται αλλού: στη γλώσσα, που είναι ταυτόχρονα λαϊκή και εξαιρετικά καλλιεργημένη, και στην ψυχολογική βαθύτητα των χαρακτήρων.", "The plot, Erotokritos's love for Aretousa, daughter of the king of Athens, is not original: Kornaros drew on a French chivalric romance, most probably via an Italian adaptation. His originality lies elsewhere: in the language, which is at once popular and exceptionally refined, and in the psychological depth of the characters."),
  L("Φιλόλογος", "m", "Το πιο συναρπαστικό, ωστόσο, είναι η ζωή του έργου μετά τον δημιουργό του. Μετά την πτώση του Χάνδακα, οι Κρητικοί πρόσφυγες το μετέφεραν στα Επτάνησα και στη Βενετία, όπου τυπώθηκε για πρώτη φορά το 1713. Για αιώνες, όμως, διαδόθηκε κυρίως προφορικά: αγράμματοι βοσκοί και αγρότες απήγγελλαν από μνήμης χιλιάδες στίχους στα γλέντια και στα νυχτέρια.", "Most fascinating, however, is the life of the work after its creator. After the fall of Candia, Cretan refugees carried it to the Ionian Islands and to Venice, where it was first printed in 1713. For centuries, though, it spread mainly orally: illiterate shepherds and farmers recited thousands of lines from memory at festivities and evening gatherings."),
  L("Φιλόλογος", "m", "Έτσι, ένα έργο λόγιας προέλευσης έγινε κτήμα του λαού, και αργότερα πηγή έμπνευσης για ποιητές όπως ο Σολωμός και ο Σεφέρης, αλλά και για μουσικούς, όπως ο Νίκος Ξυλούρης, που το έκανε ξανά τραγούδι. Λίγα κείμενα της λογοτεχνίας μας γεφυρώνουν τόσο φυσικά το λόγιο με το λαϊκό.", "Thus a work of learned origin became the people's own, and later a source of inspiration for poets such as Solomos and Seferis, but also for musicians, such as Nikos Xylouris, who turned it into song again. Few texts in our literature bridge the learned and the popular so naturally."),
 ],
 "questions": [
  Q("Τι γνωρίζουμε για τον Βιτσέντζο Κορνάρο;", ["Πολλά, χάρη στα γράμματά του", "Ελάχιστα με βεβαιότητα", "Ότι ήταν βοσκός", "Ότι έζησε στη Βενετία όλη του τη ζωή"], 1, "για τον οποίο ελάχιστα γνωρίζουμε με βεβαιότητα"),
  Q("Πού βρίσκεται, κατά τον ομιλητή, η πρωτοτυπία του έργου;", ["Στην υπόθεση", "Στη γλώσσα και στην ψυχολογική βαθύτητα των χαρακτήρων", "Στο ότι γράφτηκε σε πεζό λόγο", "Στο ιστορικό του θέμα"], 1, "Η πρωτοτυπία του βρίσκεται αλλού: στη γλώσσα"),
  Q("Πώς διαδόθηκε κυρίως το έργο για αιώνες;", ["Μέσα από τα σχολεία", "Προφορικά, από βοσκούς και αγρότες που το απήγγελλαν από μνήμης", "Μέσα από θεατρικές παραστάσεις", "Μέσα από φθηνές εκδόσεις"], 1, "διαδόθηκε κυρίως προφορικά"),
  Q("Ποιο είναι το συμπέρασμα του ομιλητή;", ["Ότι ο Ερωτόκριτος είναι έργο αποκλειστικά λαϊκό", "Ότι λίγα κείμενα γεφυρώνουν τόσο φυσικά το λόγιο με το λαϊκό", "Ότι το έργο ξεχάστηκε μετά το 1713", "Ότι ο Σεφέρης το μετέφρασε"], 1, "Λίγα κείμενα της λογοτεχνίας μας γεφυρώνουν τόσο φυσικά το λόγιο με το λαϊκό"),
 ],
 "gloss": {"κυριαρχία": "κυριαρχία — rule, dominion", "έμμετρο": "έμμετρος — in verse", "ομοιοκατάληκτους": "ομοιοκατάληκτος — rhyming", "δεκαπεντασύλλαβους": "δεκαπεντασύλλαβος — fifteen-syllable line", "διάλεκτο": "διάλεκτος — dialect", "ιπποτικό": "ιπποτικός — chivalric", "διασκευής": "διασκευή — adaptation", "βαθύτητα": "βαθύτητα — depth", "πρόσφυγες": "πρόσφυγας — refugee", "απήγγελλαν": "απαγγέλλω — to recite", "νυχτέρια": "νυχτέρι — evening gathering (for work and talk)", "λόγιας": "λόγιος — learned", "κτήμα": "κτήμα — possession, property", "γεφυρώνουν": "γεφυρώνω — to bridge"},
})

ITEMS.append({
 "id": "l33-int-sfyria", "title": "Η σφυριχτή γλώσσα της Αντιάς", "title_en": "The whistled language of Antia", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια γλωσσολόγο για τη σφυριχτή γλώσσα ενός χωριού της Εύβοιας.",
 "script": [
  L("Δημοσιογράφος", "m", "Στο χωριό Αντιά, στη νότια Εύβοια, υπάρχει μια γλώσσα που δεν μιλιέται αλλά σφυρίζεται. Τι ακριβώς είναι;", "In the village of Antia, in southern Euboea, there is a language that isn't spoken but whistled. What exactly is it?"),
  L("Γλωσσολόγος", "f", "Δεν είναι, αυστηρά, ξεχωριστή γλώσσα, αλλά ένας τρόπος να μεταφέρεις τα ελληνικά σε σφυρίγματα. Οι κάτοικοι τη λένε «σφυριά». Το ύψος και η διάρκεια του σφυρίγματος αναπαράγουν τη μελωδία και τον ρυθμό των λέξεων, έτσι ώστε ένας έμπειρος ακροατής να μπορεί να καταλάβει ολόκληρες προτάσεις.", "Strictly, it isn't a separate language, but a way of transferring Greek into whistles. The residents call it «sfyria». The pitch and length of the whistle reproduce the melody and rhythm of words, so that an experienced listener can understand whole sentences."),
  L("Δημοσιογράφος", "m", "Γιατί αναπτύχθηκε εκεί;", "Why did it develop there?"),
  L("Γλωσσολόγος", "f", "Η περιοχή είναι απότομη, με βαθιές χαράδρες. Οι βοσκοί και οι αγρότες χρειάζονταν να επικοινωνούν από απόσταση, και ένα δυνατό σφύριγμα ακούγεται πολύ πιο μακριά από τη φωνή, ακόμη και σε δυνατό αέρα. Παρόμοια συστήματα υπάρχουν, άλλωστε, σε ορεινές περιοχές σε όλο τον κόσμο, όπως στα Κανάρια Νησιά ή στην Τουρκία.", "The area is steep, with deep ravines. Shepherds and farmers needed to communicate at a distance, and a loud whistle carries much further than the voice, even in a strong wind. Similar systems exist, after all, in mountain areas all over the world, such as the Canary Islands or Turkey."),
  L("Δημοσιογράφος", "m", "Υπάρχει ακόμη κόσμος που τη γνωρίζει;", "Are there still people who know it?"),
  L("Γλωσσολόγος", "f", "Ελάχιστοι, και όλοι μεγάλης ηλικίας. Με τους δρόμους και τα κινητά τηλέφωνα, η ανάγκη που τη γέννησε εξαφανίστηκε. Τα τελευταία χρόνια γίνονται ηχογραφήσεις και προσπάθειες να διδαχτεί στα παιδιά του σχολείου. Δεν ξέρω αν θα σωθεί ως ζωντανό μέσο επικοινωνίας, αλλά τουλάχιστον δεν θα χαθεί χωρίς να έχει καταγραφεί.", "Very few, and all of them elderly. With roads and mobile phones, the need that gave birth to it disappeared. In recent years recordings have been made and efforts to teach it to schoolchildren. I don't know if it will be saved as a living means of communication, but at least it won't be lost without having been recorded."),
 ],
 "questions": [
  Q("Πώς περιγράφει η γλωσσολόγος τη «σφυριά»;", ["Ως εντελώς ξεχωριστή γλώσσα με δικό της λεξιλόγιο", "Ως τρόπο να μεταφέρονται τα ελληνικά σε σφυρίγματα", "Ως μουσικό είδος", "Ως κώδικα των ψαράδων"], 1, "ένας τρόπος να μεταφέρεις τα ελληνικά σε σφυρίγματα"),
  Q("Τι αναπαράγει το σφύριγμα;", ["Τα γράμματα της λέξης", "Τη μελωδία και τον ρυθμό των λέξεων", "Μόνο τα φωνήεντα", "Τους ήχους των ζώων"], 1, "αναπαράγουν τη μελωδία και τον ρυθμό των λέξεων"),
  Q("Γιατί αναπτύχθηκε η σφυριχτή γλώσσα στην Αντιά;", ["Για να μην καταλαβαίνουν οι ξένοι", "Γιατί η περιοχή είναι απότομη και χρειαζόταν επικοινωνία από απόσταση", "Για θρησκευτικούς λόγους", "Γιατί οι κάτοικοι δεν μιλούσαν ελληνικά"], 1, "χρειάζονταν να επικοινωνούν από απόσταση"),
  Q("Τι ελπίζει τουλάχιστον η γλωσσολόγος;", ["Ότι θα τη μάθουν όλοι οι Έλληνες", "Ότι δεν θα χαθεί χωρίς να έχει καταγραφεί", "Ότι θα αντικαταστήσει τα κινητά", "Ότι θα αναγνωριστεί ως επίσημη γλώσσα"], 1, "δεν θα χαθεί χωρίς να έχει καταγραφεί"),
 ],
 "gloss": {"σφυριχτή": "σφυριχτός — whistled", "γλωσσολόγο": "γλωσσολόγος — linguist", "σφυρίζεται": "σφυρίζομαι — to be whistled", "σφυρίγματα": "σφύριγμα — whistle", "ύψος": "ύψος — pitch; height", "αναπαράγουν": "αναπαράγω — to reproduce", "ακροατής": "ακροατής — listener", "απότομη": "απότομος — steep", "χαράδρες": "χαράδρα — ravine", "ηχογραφήσεις": "ηχογράφηση — recording", "να διδαχτεί": "διδάσκομαι — to be taught", "να έχει καταγραφεί": "καταγράφομαι — to be recorded"},
})

rnd = random.Random(33)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-33.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
