# Source for library/listening/listening-91.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l91.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l91-ann-kokkini-simaia", "title": "Κόκκινη σημαία στην παραλία", "title_en": "Red flag on the beach", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε μια οργανωμένη παραλία ένα απόγευμα του Αυγούστου και ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Ναυαγοσώστης", "m", "Προσοχή, παρακαλώ. Από αυτή τη στιγμή στον πύργο του ναυαγοσώστη έχει υψωθεί κόκκινη σημαία. Λόγω του δυνατού βοριά, έχουν δημιουργηθεί επικίνδυνα ρεύματα, που μπορούν να παρασύρουν ακόμη και έμπειρους κολυμβητές προς τα ανοιχτά.", "Attention, please. As of this moment a red flag has been raised on the lifeguard tower. Because of the strong north wind, dangerous currents have formed, which can carry even experienced swimmers out to sea."),
  L("Ναυαγοσώστης", "m", "Παρακαλούνται όλοι οι λουόμενοι να βγουν αμέσως από το νερό. Απαγορεύονται επίσης τα θαλάσσια σπορ, τα στρώματα και τα φουσκωτά παιχνίδια, που ο αέρας μπορεί να τα πάρει μακριά μέσα σε λίγα δευτερόλεπτα. Οι γονείς να προσέχουν ιδιαίτερα τα μικρά παιδιά κοντά στην ακτή.", "All bathers are asked to get out of the water immediately. Water sports, airbeds and inflatable toys are also prohibited, as the wind can carry them far away within a few seconds. Parents should keep a particularly close eye on small children near the shore."),
  L("Ναυαγοσώστης", "m", "Αν σας παρασύρει ρεύμα, μην προσπαθήσετε να κολυμπήσετε κόντρα σε αυτό. Κολυμπήστε παράλληλα με την ακτή, μέχρι να βγείτε από το ρεύμα, και σηκώστε το χέρι σας για να σας δούμε. Θα σας ενημερώσουμε μόλις ο καιρός επιτρέψει να ξαναμπείτε στη θάλασσα. Ευχαριστούμε.", "If a current carries you away, don't try to swim against it. Swim parallel to the shore until you are out of the current, and raise your hand so that we can see you. We will let you know as soon as the weather allows you to go back into the sea. Thank you."),
 ],
 "questions": [
  Q("Γιατί υψώθηκε κόκκινη σημαία;", ["Λόγω μεδουσών", "Λόγω επικίνδυνων ρευμάτων από τον δυνατό βοριά", "Λόγω ρύπανσης του νερού", "Λόγω καταιγίδας με κεραυνούς"], 1, "Λόγω του δυνατού βοριά, έχουν δημιουργηθεί επικίνδυνα ρεύματα"),
  Q("Τι απαγορεύεται εκτός από το κολύμπι;", ["Το ψάρεμα", "Οι ομπρέλες", "Τα θαλάσσια σπορ και τα φουσκωτά παιχνίδια", "Το φαγητό στην παραλία"], 2, "Απαγορεύονται επίσης τα θαλάσσια σπορ, τα στρώματα και τα φουσκωτά παιχνίδια"),
  Q("Τι πρέπει να κάνει κανείς αν τον παρασύρει ρεύμα;", ["Να κολυμπήσει κόντρα στο ρεύμα", "Να κολυμπήσει παράλληλα με την ακτή", "Να μείνει ακίνητος", "Να βουτήξει κάτω από το νερό"], 1, "Κολυμπήστε παράλληλα με την ακτή"),
 ],
 "gloss": {"οργανωμένη": "οργανωμένη παραλία — beach with facilities", "μεγάφωνα": "μεγάφωνο — loudspeaker", "υψωθεί": "υψώνομαι — to be raised", "ναυαγοσώστη": "ναυαγοσώστης — lifeguard", "βοριά": "βοριάς — north wind", "ρεύματα": "ρεύμα — current", "παρασύρουν": "παρασύρω — to sweep away", "ανοιχτά": "τα ανοιχτά — the open sea", "λουόμενοι": "λουόμενος — bather", "στρώματα": "στρώμα — (air)bed, mattress", "φουσκωτά": "φουσκωτός — inflatable", "παράλληλα": "παράλληλα — parallel"}
})
ITEMS.append({
 "id": "l91-vm-kleidaras", "title": "Μήνυμα από τον κλειδαρά", "title_en": "A message from the locksmith", "type": "voicemail", "level": "B2",
 "context_el": "Χθες το βράδυ κλειδωθήκατε έξω από το σπίτι σας και καλέσατε έναν κλειδαρά. Σήμερα ακούτε ένα μήνυμα στο κινητό σας.",
 "script": [
  L("Κλειδαράς", "m", "Καλησπέρα σας, ο Θανάσης είμαι, ο κλειδαράς που ήρθε χθες το βράδυ. Σας παίρνω για την κλειδαριά που λέγαμε. Όπως σας εξήγησα, η παλιά είναι πολύ φθαρμένη, και με την πρώτη ευκαιρία μπορεί να κολλήσει ξανά.", "Good evening, it's Thanasis, the locksmith who came last night. I'm calling about the lock we talked about. As I explained, the old one is very worn, and it could jam again at the first opportunity."),
  L("Κλειδαράς", "m", "Βρήκα λοιπόν μια κλειδαριά ασφαλείας που ταιριάζει στην πόρτα σας χωρίς να χρειαστεί να την τρυπήσουμε από την αρχή. Κοστίζει εκατόν είκοσι ευρώ, μαζί με την τοποθέτηση, και σας δίνω πέντε κλειδιά. Τα εξήντα ευρώ για το χθεσινό άνοιγμα δεν θα σας τα χρεώσω, αν την αλλάξουμε αυτή την εβδομάδα.", "So I've found a security lock that fits your door without us having to drill it from scratch. It costs a hundred and twenty euros, including fitting, and I'll give you five keys. I won't charge you the sixty euros for last night's call-out if we change it this week."),
  L("Κλειδαράς", "m", "Μπορώ να έρθω την Πέμπτη μετά τις πέντε ή το Σάββατο το πρωί. Πείτε μου τι σας βολεύει. Και μια συμβουλή: αφήστε ένα κλειδί σε κάποιον γείτονα που εμπιστεύεστε, για να μη χρειαστεί να με ξαναπάρετε μεσάνυχτα!", "I can come on Thursday after five or on Saturday morning. Tell me what suits you. And a piece of advice: leave a key with a neighbour you trust, so you don't have to call me again at midnight!"),
 ],
 "questions": [
  Q("Γιατί προτείνει ο κλειδαράς να αλλάξει η κλειδαριά;", ["Γιατί έσπασε χθες", "Γιατί η παλιά είναι πολύ φθαρμένη", "Γιατί έγινε διάρρηξη", "Γιατί χάθηκαν τα κλειδιά"], 1, "η παλιά είναι πολύ φθαρμένη"),
  Q("Τι θα γίνει αν αλλάξουν την κλειδαριά αυτή την εβδομάδα;", ["Θα πάρει δέκα κλειδιά", "Δεν θα πληρώσει το χθεσινό άνοιγμα", "Θα έχει έκπτωση στην κλειδαριά", "Η τοποθέτηση θα είναι δωρεάν"], 1, "Τα εξήντα ευρώ για το χθεσινό άνοιγμα δεν θα σας τα χρεώσω"),
  Q("Τι συμβουλεύει ο κλειδαράς;", ["Να βάλει συναγερμό", "Να κρύβει ένα κλειδί κάτω από το χαλάκι", "Να αφήσει ένα κλειδί σε έναν γείτονα που εμπιστεύεται", "Να αλλάξει πόρτα"], 2, "αφήστε ένα κλειδί σε κάποιον γείτονα που εμπιστεύεστε"),
 ],
 "gloss": {"κλειδωθήκατε": "κλειδώνομαι έξω — to lock oneself out", "κλειδαρά": "κλειδαράς — locksmith", "κλειδαριά": "κλειδαριά — lock", "φθαρμένη": "φθαρμένος — worn", "κολλήσει": "κολλάω — to jam, get stuck", "ασφαλείας": "κλειδαριά ασφαλείας — security lock", "τρυπήσουμε": "τρυπάω — to drill, make a hole", "τοποθέτηση": "τοποθέτηση — fitting, installation", "χρεώσω": "χρεώνω — to charge", "βολεύει": "με βολεύει — it suits me", "εμπιστεύεστε": "εμπιστεύομαι — to trust", "μεσάνυχτα": "μεσάνυχτα — midnight"}
})
ITEMS.append({
 "id": "l91-dia-lakkouva", "title": "Μια λακκούβα στον δρόμο", "title_en": "A pothole in the road", "type": "dialogue", "level": "B2",
 "context_el": "Μια κάτοικος τηλεφωνεί στην εξυπηρέτηση πολιτών του δήμου της.",
 "script": [
  L("Υπάλληλος", "m", "Δήμος Ηλιούπολης, εξυπηρέτηση πολιτών, λέγετε.", "Ilioupoli Municipality, citizens' service, go ahead."),
  L("Κάτοικος", "f", "Καλημέρα. Θέλω να αναφέρω μια μεγάλη λακκούβα στην οδό Ανεμώνης, ακριβώς έξω από το νηπιαγωγείο. Είναι εκεί από τις βροχές του Νοεμβρίου και κάθε μέρα μεγαλώνει.", "Good morning. I'd like to report a large pothole on Anemonis Street, right outside the nursery school. It's been there since the November rains and it gets bigger every day."),
  L("Υπάλληλος", "m", "Μάλιστα. Έχει προκαλέσει κάποιο ατύχημα;", "I see. Has it caused any accident?"),
  L("Κάτοικος", "f", "Χθες ένας μοτοσικλετιστής έπεσε μέσα και παραλίγο να τραυματιστεί. Και τα παιδιά περνάνε από εκεί κάθε πρωί. Την έχω ήδη αναφέρει στην πλατφόρμα του δήμου πριν από τρεις εβδομάδες, αλλά δεν έγινε τίποτα.", "Yesterday a motorcyclist fell into it and nearly got hurt. And the children walk past there every morning. I already reported it on the municipality's platform three weeks ago, but nothing happened."),
  L("Υπάλληλος", "m", "Λυπάμαι πολύ. Βλέπω το αίτημά σας εδώ· είχε μπει σε σειρά προτεραιότητας. Επειδή είναι δίπλα σε σχολείο και υπάρχει πια κίνδυνος, το χαρακτηρίζω επείγον. Ένα συνεργείο θα περάσει μέσα στις επόμενες σαράντα οχτώ ώρες για να βάλει σήμανση, και η επισκευή θα γίνει μέσα στην εβδομάδα.", "I'm very sorry. I can see your request here; it had been put in a priority queue. Because it's next to a school and there is now a danger, I'm marking it as urgent. A crew will come within the next forty-eight hours to put up warning signs, and the repair will be done within the week."),
  L("Κάτοικος", "f", "Σας ευχαριστώ. Μπορώ να έχω έναν αριθμό πρωτοκόλλου, για να ξέρω τι να πω αν χρειαστεί να ξαναπάρω;", "Thank you. Could I have a reference number, so I know what to say if I need to call again?"),
 ],
 "questions": [
  Q("Πού βρίσκεται η λακκούβα;", ["Έξω από το δημαρχείο", "Έξω από ένα νηπιαγωγείο", "Σε μια πλατεία", "Σε έναν χώρο στάθμευσης"], 1, "ακριβώς έξω από το νηπιαγωγείο"),
  Q("Τι έγινε χθες;", ["Ένα αυτοκίνητο έσπασε λάστιχο", "Ένα παιδί χτύπησε", "Ένας μοτοσικλετιστής έπεσε μέσα", "Πλημμύρισε ο δρόμος"], 2, "Χθες ένας μοτοσικλετιστής έπεσε μέσα"),
  Q("Τι θα γίνει μέσα σε σαράντα οχτώ ώρες;", ["Θα κλείσει ο δρόμος", "Θα επισκευαστεί η λακκούβα", "Ένα συνεργείο θα βάλει σήμανση", "Θα τηλεφωνήσει ο δήμαρχος"], 2, "Ένα συνεργείο θα περάσει μέσα στις επόμενες σαράντα οχτώ ώρες για να βάλει σήμανση"),
 ],
 "gloss": {"εξυπηρέτηση πολιτών": "εξυπηρέτηση πολιτών — citizens' service desk", "λακκούβα": "λακκούβα — pothole", "νηπιαγωγείο": "νηπιαγωγείο — nursery school", "μοτοσικλετιστής": "μοτοσικλετιστής — motorcyclist", "παραλίγο": "παραλίγο να — nearly", "τραυματιστεί": "τραυματίζομαι — to be injured", "πλατφόρμα": "πλατφόρμα — (online) platform", "προτεραιότητας": "προτεραιότητα — priority", "επείγον": "επείγων — urgent", "συνεργείο": "συνεργείο — (work) crew", "σήμανση": "σήμανση — warning signs", "πρωτοκόλλου": "αριθμός πρωτοκόλλου — reference number"}
})
ITEMS.append({
 "id": "l91-int-limeniki", "title": "Μια μέρα στο Λιμενικό", "title_en": "A day in the Coast Guard", "type": "interview", "level": "B2",
 "context_el": "Σε μια ραδιοφωνική εκπομπή, μια δημοσιογράφος μιλά με μια υπαξιωματικό του Λιμενικού Σώματος σε ένα νησί.",
 "script": [
  L("Δημοσιογράφος", "f", "Οι περισσότεροι σας βλέπουμε στο λιμάνι, όταν ελέγχετε τα εισιτήρια στα πλοία. Είναι αυτή η κύρια δουλειά σας;", "Most of us see you at the port, when you check tickets on the ships. Is that your main job?"),
  L("Λιμενικός", "f", "Είναι ένα μικρό κομμάτι. Ελέγχουμε, βέβαια, αν τα πλοία φεύγουν με τον σωστό αριθμό επιβατών και αν τηρούνται οι κανόνες ασφαλείας. Αλλά κάνουμε και έρευνες και διασώσεις στη θάλασσα, ελέγχουμε την αλιεία και προστατεύουμε το θαλάσσιο περιβάλλον από τη ρύπανση.", "It's a small part. We check, of course, that ships leave with the right number of passengers and that safety rules are followed. But we also carry out search and rescue at sea, monitor fishing and protect the marine environment from pollution."),
  L("Δημοσιογράφος", "f", "Ποια ήταν η πιο δύσκολη στιγμή σας;", "What was your most difficult moment?"),
  L("Λιμενικός", "f", "Ένα βράδυ του Φεβρουαρίου, με εννιά μποφόρ, ένα μικρό ψαροκάικο έστειλε σήμα κινδύνου. Ο ψαράς είχε πέσει στη θάλασσα και ο γιος του δεν μπορούσε να τον τραβήξει πάνω. Φτάσαμε σε είκοσι λεπτά, που μου φάνηκαν ώρες. Τους βγάλαμε και τους δύο ζωντανούς.", "One February night, in force nine winds, a small fishing boat sent a distress signal. The fisherman had fallen into the sea and his son couldn't pull him up. We got there in twenty minutes, which felt like hours to me. We got them both out alive."),
  L("Δημοσιογράφος", "f", "Τι θα λέγατε στους λουόμενους και στους ιδιοκτήτες σκαφών το καλοκαίρι;", "What would you say to bathers and boat owners in the summer?"),
  L("Λιμενικός", "f", "Να σέβονται τη θάλασσα. Να ελέγχουν τον καιρό πριν ξεκινήσουν, να έχουν σωσίβια για όλους και να μην πλησιάζουν ποτέ με ταχύπλοο τις περιοχές όπου κολυμπάει κόσμος. Και να θυμούνται τον αριθμό 108: είναι η γραμμή έκτακτης ανάγκης του Λιμενικού.", "To respect the sea. To check the weather before setting off, to have life jackets for everyone and never to approach areas where people are swimming in a speedboat. And to remember the number 108: it's the Coast Guard's emergency line."),
 ],
 "questions": [
  Q("Τι λέει η λιμενικός για τον έλεγχο των εισιτηρίων;", ["Ότι είναι η κύρια δουλειά της", "Ότι είναι ένα μικρό κομμάτι της δουλειάς της", "Ότι δεν το κάνει πια", "Ότι το κάνουν οι εταιρείες"], 1, "Είναι ένα μικρό κομμάτι"),
  Q("Τι συνέβη το βράδυ του Φεβρουαρίου;", ["Βυθίστηκε ένα πλοίο", "Ένας ψαράς έπεσε στη θάλασσα", "Χάθηκε ένας κολυμβητής", "Έπιασε φωτιά ένα σκάφος"], 1, "Ο ψαράς είχε πέσει στη θάλασσα"),
  Q("Τι είναι ο αριθμός 108;", ["Το τηλέφωνο του λιμανιού", "Η γραμμή έκτακτης ανάγκης του Λιμενικού", "Ο αριθμός για πληροφορίες καιρού", "Το τηλέφωνο της Πυροσβεστικής"], 1, "είναι η γραμμή έκτακτης ανάγκης του Λιμενικού"),
 ],
 "gloss": {"υπαξιωματικό": "υπαξιωματικός — petty officer", "Λιμενικού": "Λιμενικό (Σώμα) — Coast Guard", "τηρούνται": "τηρούμαι — to be observed, followed", "διασώσεις": "διάσωση — rescue", "αλιεία": "αλιεία — fishing", "ρύπανση": "ρύπανση — pollution", "μποφόρ": "μποφόρ — Beaufort (wind force)", "ψαροκάικο": "ψαροκάικο — small fishing boat", "σήμα κινδύνου": "σήμα κινδύνου — distress signal", "σωσίβια": "σωσίβιο — life jacket", "ταχύπλοο": "ταχύπλοο — speedboat", "έκτακτης ανάγκης": "έκτακτη ανάγκη — emergency"}
})
ITEMS.append({
 "id": "l91-rep-skiathos", "title": "Η Σκιάθος πέρα από τις παραλίες", "title_en": "Skiathos beyond the beaches", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ταξιδιωτικό ρεπορτάζ στο ραδιόφωνο.",
 "script": [
  L("Ρεπόρτερ", "f", "Η Σκιάθος είναι γνωστή κυρίως για τις παραλίες της: λένε ότι έχει πάνω από εξήντα, με πιο φημισμένη τις Κουκουναριές, όπου το πευκοδάσος φτάνει μέχρι τη χρυσή άμμο. Όμως το νησί έχει και μια άλλη, πιο ήσυχη πλευρά.", "Skiathos is known mainly for its beaches: they say it has more than sixty, the most famous being Koukounaries, where the pine forest reaches all the way down to the golden sand. But the island also has another, quieter side."),
  L("Ρεπόρτερ", "f", "Στην πόλη, σε ένα στενό πίσω από το λιμάνι, βρίσκεται το σπίτι του Αλέξανδρου Παπαδιαμάντη, του μεγάλου διηγηματογράφου που γεννήθηκε και πέθανε εδώ. Σήμερα είναι μουσείο: μικρά δωμάτια, ένα γραφείο, τα γυαλιά του, και ιστορίες για τους ανθρώπους του νησιού, που ο συγγραφέας τους περιέγραψε με τόση τρυφερότητα.", "In the town, in an alley behind the harbour, stands the house of Alexandros Papadiamantis, the great short-story writer who was born and died here. Today it is a museum: small rooms, a desk, his glasses, and stories about the island's people, whom the writer described with such tenderness."),
  L("Ρεπόρτερ", "f", "Για όσους αγαπούν το περπάτημα, ένα παλιό μονοπάτι οδηγεί στο Κάστρο, στο βόρειο άκρο του νησιού. Εκεί έμεναν οι κάτοικοι για αιώνες, για να προστατεύονται από τους πειρατές. Σήμερα έχουν μείνει λίγα ερείπια και μερικές εκκλησίες, αλλά η θέα προς το Αιγαίο αξίζει κάθε βήμα.", "For those who love walking, an old path leads to Kastro, at the northern tip of the island. That is where the inhabitants lived for centuries, to protect themselves from pirates. Today only a few ruins and some churches remain, but the view over the Aegean is worth every step."),
 ],
 "questions": [
  Q("Τι είναι ξεχωριστό στις Κουκουναριές;", ["Τα μαύρα βότσαλα", "Το πευκοδάσος φτάνει μέχρι την άμμο", "Τα ζεστά νερά", "Οι σπηλιές"], 1, "το πευκοδάσος φτάνει μέχρι τη χρυσή άμμο"),
  Q("Τι βρίσκεται σε ένα στενό πίσω από το λιμάνι;", ["Ένα αρχαίο θέατρο", "Το σπίτι του Παπαδιαμάντη", "Ένα ναυτικό μουσείο", "Το παλιό δημαρχείο"], 1, "βρίσκεται το σπίτι του Αλέξανδρου Παπαδιαμάντη"),
  Q("Γιατί οι κάτοικοι ζούσαν στο Κάστρο;", ["Για να προστατεύονται από τους πειρατές", "Γιατί εκεί υπήρχε νερό", "Για τη δροσιά", "Γιατί εκεί ήταν τα χωράφια τους"], 0, "για να προστατεύονται από τους πειρατές"),
 ],
 "gloss": {"φημισμένη": "φημισμένος — famous", "πευκοδάσος": "πευκοδάσος — pine forest", "άμμο": "άμμος — sand", "στενό": "στενό — alley", "διηγηματογράφου": "διηγηματογράφος — short-story writer", "τρυφερότητα": "τρυφερότητα — tenderness", "μονοπάτι": "μονοπάτι — path", "άκρο": "άκρο — tip, end", "πειρατές": "πειρατής — pirate", "ερείπια": "ερείπιο — ruin", "θέα": "θέα — view"}
})
ITEMS.append({
 "id": "l91-rep-arachova", "title": "Αράχωβα, χειμώνα και καλοκαίρι", "title_en": "Arachova, winter and summer", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια τηλεοπτική εκπομπή για ταξίδια στην ηπειρωτική Ελλάδα.",
 "script": [
  L("Ρεπόρτερ", "m", "Χτισμένη αμφιθεατρικά στις πλαγιές του Παρνασσού, η Αράχωβα είναι από τους πιο δημοφιλείς χειμερινούς προορισμούς της χώρας. Τα Σαββατοκύριακα του χειμώνα, οι δρόμοι της γεμίζουν επισκέπτες από την Αθήνα, που έρχονται για σκι στο χιονοδρομικό κέντρο, μόλις είκοσι πέντε χιλιόμετρα μακριά.", "Built like an amphitheatre on the slopes of Parnassus, Arachova is one of the country's most popular winter destinations. On winter weekends its streets fill with visitors from Athens, who come to ski at the ski centre, only twenty-five kilometres away."),
  L("Ρεπόρτερ", "m", "Το χωριό, όμως, δεν ζει μόνο από το χιόνι. Είναι γνωστό για τα υφαντά του, χαλιά και κουβέρτες που έφτιαχναν παλιά οι γυναίκες στον αργαλειό, και για τη φορμαέλα, ένα σκληρό τυρί που τρώγεται ψημένο. Την άνοιξη γιορτάζει τον πολιούχο του, τον Άγιο Γεώργιο, με ένα πανηγύρι τριών ημερών, χορούς και αγώνες.", "But the village doesn't live only from snow. It is known for its weavings, rugs and blankets that the women used to make on the loom, and for formaela, a hard cheese that is eaten grilled. In spring it celebrates its patron saint, Saint George, with a three-day festival, dances and contests."),
  L("Ρεπόρτερ", "m", "Και επειδή οι Δελφοί απέχουν μόλις δέκα χιλιόμετρα, πολλοί συνδυάζουν μια επίσκεψη στον αρχαιολογικό χώρο με μια βόλτα στα πλακόστρωτα σοκάκια της Αράχωβας. Όπως μας είπε ένας ντόπιος, «το καλοκαίρι η θέα είναι ακόμα πιο ωραία, γιατί τη βλέπεις χωρίς ομίχλη και χωρίς κίνηση».", "And because Delphi is only ten kilometres away, many people combine a visit to the archaeological site with a stroll through the cobbled lanes of Arachova. As a local told us, 'in summer the view is even lovelier, because you see it without fog and without traffic'."),
 ],
 "questions": [
  Q("Γιατί έρχονται πολλοί επισκέπτες τον χειμώνα;", ["Για τις ιαματικές πηγές", "Για σκι στο χιονοδρομικό κέντρο", "Για το πανηγύρι", "Για τα μουσεία"], 1, "που έρχονται για σκι στο χιονοδρομικό κέντρο"),
  Q("Τι είναι η φορμαέλα;", ["Ένα υφαντό", "Ένας χορός", "Ένα σκληρό τυρί που τρώγεται ψημένο", "Ένα γλυκό του κουταλιού"], 2, "ένα σκληρό τυρί που τρώγεται ψημένο"),
  Q("Γιατί πολλοί συνδυάζουν την Αράχωβα με τους Δελφούς;", ["Γιατί υπάρχει κοινό εισιτήριο", "Γιατί απέχουν μόλις δέκα χιλιόμετρα", "Γιατί εκεί είναι τα ξενοδοχεία", "Γιατί το λέει ο ταξιδιωτικός οδηγός"], 1, "επειδή οι Δελφοί απέχουν μόλις δέκα χιλιόμετρα"),
 ],
 "gloss": {"αμφιθεατρικά": "αμφιθεατρικά — in tiers, like an amphitheatre", "πλαγιές": "πλαγιά — slope", "χειμερινούς": "χειμερινός — winter (adjective)", "χιονοδρομικό": "χιονοδρομικό κέντρο — ski centre", "υφαντά": "υφαντό — woven textile", "αργαλειό": "αργαλειός — loom", "φορμαέλα": "φορμαέλα — formaela (hard cheese of Arachova)", "πολιούχο": "πολιούχος — patron saint", "πανηγύρι": "πανηγύρι — village festival", "πλακόστρωτα": "πλακόστρωτος — cobbled, paved", "σοκάκια": "σοκάκι — lane", "ομίχλη": "ομίχλη — fog"}
})
ITEMS.append({
 "id": "l91-mono-cheimerino-banio", "title": "Κολύμπι τον χειμώνα", "title_en": "Swimming in winter", "type": "monologue", "level": "B2",
 "context_el": "Σε ένα podcast για την υγεία, μια νοσηλεύτρια μιλά για μια καινούργια συνήθειά της.",
 "script": [
  L("Νοσηλεύτρια", "f", "Όλα ξεκίνησαν πριν από δύο χρόνια, όταν μια συνάδελφος με κάλεσε να κολυμπήσουμε μαζί ένα πρωί του Νοεμβρίου. Νόμιζα ότι αστειευόταν. Το νερό είχε δεκαεπτά βαθμούς, κι εγώ ήμουν από αυτούς που μπαίνουν στη θάλασσα μόνο τον Αύγουστο.", "It all started two years ago, when a colleague invited me to go swimming together one November morning. I thought she was joking. The water was seventeen degrees, and I was one of those people who only go into the sea in August."),
  L("Νοσηλεύτρια", "f", "Την πρώτη φορά άντεξα μόνο ένα λεπτό. Βγήκα τρέμοντας, αλλά ένιωθα απίστευτα ζωντανή, σαν να είχα πιει τρεις καφέδες. Από τότε πηγαίνω τρεις φορές την εβδομάδα, μετά τη νυχτερινή βάρδια, με μια ομάδα που μαζεύεται στην ίδια παραλία. Ο μεγαλύτερος είναι ογδόντα ενός χρόνων.", "The first time I only lasted a minute. I got out shivering, but I felt incredibly alive, as if I'd drunk three coffees. Since then I've been going three times a week, after the night shift, with a group that meets at the same beach. The oldest is eighty-one."),
  L("Νοσηλεύτρια", "f", "Ως νοσηλεύτρια, όμως, πρέπει να πω και κάτι σοβαρό: το κρύο νερό δεν είναι για όλους. Όποιος έχει πρόβλημα με την καρδιά ή την πίεση πρέπει πρώτα να μιλήσει με τον γιατρό του. Και ποτέ δεν κολυμπάμε μόνοι, ούτε μένουμε μέσα πολλή ώρα. Το θέμα δεν είναι να αποδείξεις ότι αντέχεις, αλλά να το απολαύσεις.", "As a nurse, though, I must also say something serious: cold water is not for everyone. Anyone with a heart or blood-pressure problem must first talk to their doctor. And we never swim alone, nor do we stay in for long. The point is not to prove you can take it, but to enjoy it."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η νοσηλεύτρια το χειμερινό κολύμπι;", ["Της το πρότεινε ο γιατρός της", "Την κάλεσε μια συνάδελφος", "Το είδε σε ένα ντοκιμαντέρ", "Ήθελε να χάσει βάρος"], 1, "μια συνάδελφος με κάλεσε να κολυμπήσουμε μαζί"),
  Q("Πώς ένιωσε την πρώτη φορά;", ["Απογοητευμένη", "Άρρωστη", "Απίστευτα ζωντανή", "Πολύ κουρασμένη"], 2, "ένιωθα απίστευτα ζωντανή"),
  Q("Τι συμβουλεύει όσους έχουν πρόβλημα με την καρδιά;", ["Να κολυμπούν μόνο το καλοκαίρι", "Να μιλήσουν πρώτα με τον γιατρό τους", "Να κολυμπούν μόνο ένα λεπτό", "Να φορούν στολή"], 1, "πρέπει πρώτα να μιλήσει με τον γιατρό του"),
 ],
 "gloss": {"νοσηλεύτρια": "νοσηλεύτρια — nurse", "συνάδελφος": "συνάδελφος — colleague", "αστειευόταν": "αστειεύομαι — to joke", "άντεξα": "αντέχω — to bear, last", "τρέμοντας": "τρέμω — to shiver, tremble", "βάρδια": "βάρδια — shift", "πίεση": "πίεση — blood pressure", "αποδείξεις": "αποδεικνύω — to prove", "απολαύσεις": "απολαμβάνω — to enjoy", "podcast": "podcast — podcast"}
})
ITEMS.append({
 "id": "l91-mono-diploma-exinta", "title": "Δίπλωμα οδήγησης στα εξήντα", "title_en": "A driving licence at sixty", "type": "monologue", "level": "B2",
 "context_el": "Σε μια εκπομπή με ιστορίες ακροατών, μια γυναίκα διηγείται πώς έμαθε να οδηγεί.",
 "script": [
  L("Ακροάτρια", "f", "Σε όλη μου τη ζωή οδηγούσε ο άντρας μου. Εγώ καθόμουν δίπλα, κρατούσα τον χάρτη και του έλεγα πού να στρίψει. Όταν πέθανε, πριν από τρία χρόνια, κατάλαβα ότι για να πάω οπουδήποτε, έπρεπε να παρακαλάω τα παιδιά μου ή να περιμένω το λεωφορείο, που περνάει από το χωριό δύο φορές τη μέρα.", "All my life my husband did the driving. I sat beside him, held the map and told him where to turn. When he died, three years ago, I realised that to go anywhere I had to beg my children or wait for the bus, which comes through the village twice a day."),
  L("Ακροάτρια", "f", "Έτσι, στα εξήντα ένα μου, γράφτηκα σε σχολή οδηγών. Ο δάσκαλος ήταν νεότερος από τον γιο μου και στην αρχή με κοίταζε με δυσπιστία. Τα πρώτα μαθήματα ήταν καταστροφή: έσβηνα τη μηχανή σε κάθε ανηφόρα και τρόμαζα όταν με προσπερνούσε φορτηγό.", "So, at sixty-one, I enrolled in a driving school. The instructor was younger than my son and at first looked at me with disbelief. The first lessons were a disaster: I stalled the engine on every uphill slope and panicked when a lorry overtook me."),
  L("Ακροάτρια", "f", "Κόπηκα μία φορά στην εξέταση, στο παρκάρισμα. Τη δεύτερη φορά πέρασα, και ο δάσκαλος μού έφερε ένα γλυκό. Τώρα πηγαίνω μόνη μου στη λαϊκή, στις φίλες μου, ακόμα και στη θάλασσα. Η εγγονή μου λέει ότι οδηγώ σαν τη γιαγιά που είμαι, αλλά εγώ δεν έχω πάρει ούτε μία κλήση.", "I failed the test once, on parking. The second time I passed, and the instructor brought me a cake. Now I go on my own to the street market, to my friends, even to the sea. My granddaughter says I drive like the grandmother I am, but I haven't had a single ticket."),
 ],
 "questions": [
  Q("Γιατί αποφάσισε να μάθει να οδηγεί;", ["Γιατί αγόρασε αυτοκίνητο", "Γιατί μετά τον θάνατο του άντρα της δεν μπορούσε να πηγαίνει πουθενά μόνη", "Γιατί βρήκε δουλειά στην πόλη", "Γιατί της το ζήτησαν τα παιδιά της"], 1, "κατάλαβα ότι για να πάω οπουδήποτε, έπρεπε να παρακαλάω τα παιδιά μου"),
  Q("Ποιο ήταν το πρόβλημα στα πρώτα μαθήματα;", ["Δεν έβλεπε καλά", "Έσβηνε τη μηχανή στις ανηφόρες", "Δεν ήξερε τους κανόνες", "Ο δάσκαλος ήταν αυστηρός"], 1, "έσβηνα τη μηχανή σε κάθε ανηφόρα"),
  Q("Σε τι κόπηκε την πρώτη φορά;", ["Στη θεωρία", "Στο παρκάρισμα", "Σε μια ανηφόρα", "Σε ένα φανάρι"], 1, "Κόπηκα μία φορά στην εξέταση, στο παρκάρισμα"),
 ],
 "gloss": {"ακροατών": "ακροατής — listener", "στρίψει": "στρίβω — to turn", "οπουδήποτε": "οπουδήποτε — anywhere", "σχολή οδηγών": "σχολή οδηγών — driving school", "δυσπιστία": "δυσπιστία — disbelief", "έσβηνα": "σβήνω τη μηχανή — to stall the engine", "ανηφόρα": "ανηφόρα — uphill slope", "προσπερνούσε": "προσπερνάω — to overtake", "Κόπηκα": "κόβομαι — to fail (an exam)", "παρκάρισμα": "παρκάρισμα — parking", "λαϊκή": "λαϊκή (αγορά) — street market", "κλήση": "κλήση — (traffic) ticket"}
})
ITEMS.append({
 "id": "l91-c1-provoleas", "title": "Το φαινόμενο του προβολέα", "title_en": "The spotlight effect", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την ψυχολογία της καθημερινότητας, η παρουσιάστρια συζητά με έναν κοινωνικό ψυχολόγο.",
 "script": [
  L("Παρουσιάστρια", "f", "Σας έχει συμβεί να μπείτε σε μια αίθουσα με έναν λεκέ στο πουκάμισο και να είστε βέβαιοι ότι όλοι τον κοιτάζουν; Αυτό, μας λένε, έχει όνομα.", "Has it ever happened to you to walk into a room with a stain on your shirt and be sure that everyone is looking at it? That, we are told, has a name."),
  L("Ψυχολόγος", "m", "Ναι, το λέμε «φαινόμενο του προβολέα». Είναι η τάση μας να υπερεκτιμούμε πόσο προσέχουν οι άλλοι την εμφάνιση ή τη συμπεριφορά μας. Επειδή εμείς βρισκόμαστε διαρκώς στο κέντρο της δικής μας εμπειρίας, υποθέτουμε ότι βρισκόμαστε και στο κέντρο της προσοχής των άλλων.", "Yes, we call it the 'spotlight effect'. It is our tendency to overestimate how much other people notice our appearance or our behaviour. Because we are constantly at the centre of our own experience, we assume that we are also at the centre of other people's attention."),
  L("Παρουσιάστρια", "f", "Υπάρχουν πειράματα που το δείχνουν;", "Are there experiments that show it?"),
  L("Ψυχολόγος", "m", "Το πιο γνωστό έγινε σε ένα αμερικανικό πανεπιστήμιο. Οι ερευνητές έβαλαν φοιτητές να φορέσουν ένα μπλουζάκι με τη φωτογραφία ενός τραγουδιστή που θεωρούνταν ντεμοντέ και να μπουν σε μια αίθουσα γεμάτη συμφοιτητές. Οι φοιτητές πίστευαν ότι περίπου οι μισοί είχαν προσέξει το μπλουζάκι. Στην πραγματικότητα, το είχε προσέξει περίπου ένας στους τέσσερις.", "The best known took place at an American university. The researchers had students put on a T-shirt with a picture of a singer considered unfashionable and walk into a room full of fellow students. The students believed that about half had noticed the T-shirt. In reality, about one in four had noticed it."),
  L("Παρουσιάστρια", "f", "Και πώς μας βοηθά να το ξέρουμε αυτό;", "And how does it help us to know this?"),
  L("Ψυχολόγος", "m", "Μας απελευθερώνει. Το ίδιο φαινόμενο ισχύει και για τα λάθη μας: ένα κόμπιασμα σε μια ομιλία ή μια άστοχη φράση σε μια σύσκεψη μάς βασανίζουν για μέρες, ενώ οι άλλοι τα έχουν ξεχάσει σχεδόν αμέσως, απασχολημένοι καθώς είναι με τους δικούς τους προβολείς. Αν το θυμόμαστε, τολμάμε περισσότερα.", "It frees us. The same effect applies to our mistakes: a stumble in a speech or an ill-judged phrase in a meeting torments us for days, while others have forgotten them almost immediately, busy as they are with their own spotlights. If we remember this, we dare more."),
 ],
 "questions": [
  Q("Πώς ορίζει ο ψυχολόγος το φαινόμενο του προβολέα;", ["Ως την τάση να μην προσέχουμε τους άλλους", "Ως την τάση να υπερεκτιμούμε πόσο μας προσέχουν οι άλλοι", "Ως τον φόβο της σκηνής", "Ως την ανάγκη να είμαστε στο κέντρο της προσοχής"], 1, "Είναι η τάση μας να υπερεκτιμούμε πόσο προσέχουν οι άλλοι την εμφάνιση ή τη συμπεριφορά μας"),
  Q("Πού οφείλεται, κατά τον ψυχολόγο, αυτή η τάση;", ["Στην κακή μας αυτοεκτίμηση", "Στο ότι βρισκόμαστε διαρκώς στο κέντρο της δικής μας εμπειρίας", "Στα μέσα κοινωνικής δικτύωσης", "Στην ανατροφή μας"], 1, "Επειδή εμείς βρισκόμαστε διαρκώς στο κέντρο της δικής μας εμπειρίας"),
  Q("Τι έδειξε το πείραμα με το μπλουζάκι;", ["Ότι το πρόσεξαν σχεδόν όλοι", "Ότι το πρόσεξαν οι μισοί, όπως πίστευαν οι φοιτητές", "Ότι το πρόσεξε περίπου ένας στους τέσσερις", "Ότι δεν το πρόσεξε κανείς"], 2, "το είχε προσέξει περίπου ένας στους τέσσερις"),
  Q("Γιατί, κατά τον ψυχολόγο, οι άλλοι ξεχνούν γρήγορα τα λάθη μας;", ["Γιατί είναι ευγενικοί", "Γιατί δεν τα καταλαβαίνουν", "Γιατί είναι απασχολημένοι με τους δικούς τους προβολείς", "Γιατί τα λάθη μας είναι μικρά"], 2, "απασχολημένοι καθώς είναι με τους δικούς τους προβολείς"),
 ],
 "gloss": {"λεκέ": "λεκές — stain", "προβολέα": "προβολέας — spotlight", "υπερεκτιμούμε": "υπερεκτιμώ — to overestimate", "εμφάνιση": "εμφάνιση — appearance", "υποθέτουμε": "υποθέτω — to assume", "ντεμοντέ": "ντεμοντέ — out of fashion", "συμφοιτητές": "συμφοιτητής — fellow student", "απελευθερώνει": "απελευθερώνω — to free", "κόμπιασμα": "κόμπιασμα — stumble, hesitation (in speech)", "άστοχη": "άστοχος — ill-judged, unfortunate", "βασανίζουν": "βασανίζω — to torment", "τολμάμε": "τολμάω — to dare"}
})
ITEMS.append({
 "id": "l91-c1-katochi", "title": "Γιατί υπερτιμάμε ό,τι μας ανήκει", "title_en": "Why we overvalue what we own", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας διάλεξης για τη συμπεριφορική οικονομία σε ένα πανεπιστήμιο.",
 "script": [
  L("Καθηγήτρια", "f", "Ας ξεκινήσουμε με ένα πείραμα που έχει επαναληφθεί πολλές φορές. Σε μια ομάδα φοιτητών δίνουμε από μια κούπα με το σήμα του πανεπιστημίου και τους ρωτάμε με πόσα χρήματα θα την πουλούσαν. Σε μια άλλη ομάδα, που δεν έχει κούπα, ρωτάμε πόσα θα έδιναν για να αγοράσουν την ίδια ακριβώς κούπα. Το αποτέλεσμα είναι σταθερό: όσοι την κατέχουν ζητούν περίπου τα διπλάσια από όσα είναι διατεθειμένοι να πληρώσουν οι άλλοι.", "Let's start with an experiment that has been repeated many times. We give each student in one group a mug with the university logo and ask them for how much money they would sell it. We ask another group, who have no mug, how much they would pay to buy exactly the same mug. The result is consistent: those who own it ask for roughly twice as much as the others are willing to pay."),
  L("Καθηγήτρια", "f", "Το φαινόμενο αυτό ονομάστηκε από τον οικονομολόγο Ρίτσαρντ Θέιλερ «φαινόμενο της κατοχής». Μόλις κάτι γίνει δικό μας, του αποδίδουμε μεγαλύτερη αξία, απλώς και μόνο επειδή μας ανήκει. Μια εξήγηση είναι η λεγόμενη αποστροφή στην απώλεια: η λύπη που νιώθουμε όταν χάνουμε κάτι είναι πιο έντονη από τη χαρά που νιώθουμε όταν αποκτούμε κάτι ισοδύναμο.", "This phenomenon was named the 'endowment effect' by the economist Richard Thaler. As soon as something becomes ours, we attribute greater value to it, simply because it belongs to us. One explanation is so-called loss aversion: the sorrow we feel when we lose something is more intense than the joy we feel when we acquire something equivalent."),
  L("Καθηγήτρια", "f", "Οι επιχειρήσεις το γνωρίζουν πολύ καλά. Γι’ αυτό σας προσφέρουν δωρεάν δοκιμή για έναν μήνα ή σας επιτρέπουν να επιστρέψετε το προϊόν χωρίς ερωτήσεις. Ξέρουν ότι, αφού το έχετε στα χέρια σας, η ιδέα να το αποχωριστείτε θα σας φαίνεται πολύ πιο δυσάρεστη απ’ ό,τι φανταζόσασταν. Και το ίδιο ισχύει, όπως θα δούμε, για τις ιδέες και τις πεποιθήσεις μας.", "Businesses know this very well. That is why they offer you a free one-month trial or let you return the product with no questions asked. They know that once you have it in your hands, the idea of parting with it will seem much more unpleasant to you than you imagined. And the same applies, as we shall see, to our ideas and beliefs."),
 ],
 "questions": [
  Q("Τι έδειξε το πείραμα με τις κούπες;", ["Ότι οι φοιτητές δεν ήθελαν τις κούπες", "Ότι όσοι είχαν κούπα ζητούσαν περίπου τα διπλάσια", "Ότι οι δύο ομάδες έδωσαν την ίδια τιμή", "Ότι όσοι δεν είχαν κούπα ήταν διατεθειμένοι να πληρώσουν περισσότερα"], 1, "όσοι την κατέχουν ζητούν περίπου τα διπλάσια από όσα είναι διατεθειμένοι να πληρώσουν οι άλλοι"),
  Q("Τι είναι η «αποστροφή στην απώλεια»;", ["Ο φόβος να ξοδέψουμε χρήματα", "Το ότι η λύπη για μια απώλεια είναι πιο έντονη από τη χαρά για ένα ισοδύναμο κέρδος", "Η τάση να χάνουμε πράγματα", "Η απροθυμία να δανείζουμε"], 1, "η λύπη που νιώθουμε όταν χάνουμε κάτι είναι πιο έντονη από τη χαρά που νιώθουμε όταν αποκτούμε κάτι ισοδύναμο"),
  Q("Γιατί οι επιχειρήσεις προσφέρουν δωρεάν δοκιμή;", ["Για να μάθουν τη γνώμη των πελατών", "Γιατί το απαιτεί ο νόμος", "Γιατί ξέρουν ότι θα είναι δυσάρεστο να αποχωριστούμε το προϊόν", "Για να ξεφορτωθούν παλιά προϊόντα"], 2, "η ιδέα να το αποχωριστείτε θα σας φαίνεται πολύ πιο δυσάρεστη απ’ ό,τι φανταζόσασταν"),
  Q("Σε τι άλλο, κατά την καθηγήτρια, ισχύει το ίδιο φαινόμενο;", ["Στις φιλίες μας", "Στις ιδέες και τις πεποιθήσεις μας", "Στα χρήματα που κερδίζουμε", "Στον χρόνο μας"], 1, "για τις ιδέες και τις πεποιθήσεις μας"),
 ],
 "gloss": {"συμπεριφορική": "συμπεριφορικός — behavioural", "επαναληφθεί": "επαναλαμβάνομαι — to be repeated", "κατέχουν": "κατέχω — to own, possess", "διατεθειμένοι": "διατεθειμένος — willing", "κατοχής": "κατοχή — possession, ownership", "αποδίδουμε": "αποδίδω — to attribute", "αποστροφή": "αποστροφή — aversion", "απώλεια": "απώλεια — loss", "ισοδύναμο": "ισοδύναμος — equivalent", "δοκιμή": "δοκιμή — trial", "αποχωριστείτε": "αποχωρίζομαι — to part with", "πεποιθήσεις": "πεποίθηση — belief"}
})

rnd = random.Random(91)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-91.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
