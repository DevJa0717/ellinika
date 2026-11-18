# Source for library/listening/listening-183.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l183.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l183-ann-kanones-katafygiou", "title": "Οι κανόνες του ορειβατικού καταφυγίου", "title_en": "The rules of the mountain refuge", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε τον υπεύθυνο ενός ορειβατικού καταφυγίου να μιλά στους επισκέπτες την ώρα του δείπνου.",
 "script": [
  L("Υπεύθυνος", "m", "Καλησπέρα σε όλους και καλώς ήρθατε. Πριν σερβιρίσουμε τη σούπα, λίγοι κανόνες. Τις μπότες τις αφήνετε στην είσοδο· μέσα κυκλοφορούμε μόνο με παντόφλες, που θα βρείτε στο ράφι δίπλα στην πόρτα. Τα φώτα στους κοιτώνες σβήνουν στις δέκα, γιατί πολλοί ξεκινούν για την κορυφή πριν ξημερώσει.", "Good evening, everyone, and welcome. Before we serve the soup, a few rules. You leave your boots at the entrance; inside we only walk around in slippers, which you'll find on the shelf next to the door. The lights in the dormitories go out at ten, because many people set off for the summit before dawn."),
  L("Υπεύθυνος", "m", "Το νερό εδώ το μαζεύουμε από τη βροχή και το χιόνι, οπότε σας παρακαλώ να μην κάνετε ντους πάνω από τρία λεπτά. Τα σκουπίδια σας τα παίρνετε μαζί σας όταν κατεβαίνετε· εδώ πάνω δεν περνάει απορριμματοφόρο.", "We collect the water here from rain and snow, so please don't take showers longer than three minutes. You take your rubbish with you when you go down; no rubbish truck comes up here."),
  L("Υπεύθυνος", "m", "Τέλος, όσοι ανεβαίνετε αύριο στην κορυφή, γράψτε το όνομά σας και την ώρα που φεύγετε στο βιβλίο της εισόδου. Αν δεν έχετε γυρίσει ως τις τρεις το απόγευμα, θα ειδοποιήσουμε την ομάδα διάσωσης.", "Finally, those of you going up to the summit tomorrow, write your name and the time you leave in the book at the entrance. If you haven't come back by three in the afternoon, we'll notify the rescue team."),
 ],
 "questions": [
  Q("Γιατί σβήνουν τα φώτα στις δέκα;", ["Για να κάνουν οικονομία στο ρεύμα", "Γιατί πολλοί ξεκινούν για την κορυφή πριν ξημερώσει", "Γιατί το ζητούν οι γείτονες", "Γιατί κλείνει η κουζίνα"], 1, "πολλοί ξεκινούν για την κορυφή πριν ξημερώσει"),
  Q("Γιατί πρέπει τα ντους να είναι σύντομα;", ["Γιατί το νερό μαζεύεται από τη βροχή και το χιόνι", "Γιατί δεν υπάρχει ζεστό νερό", "Γιατί υπάρχει μόνο ένα μπάνιο", "Γιατί κάνει κρύο"], 0, "Το νερό εδώ το μαζεύουμε από τη βροχή και το χιόνι"),
  Q("Τι πρέπει να κάνουν όσοι ανεβαίνουν στην κορυφή;", ["Να πάρουν μαζί τους έναν οδηγό", "Να φύγουν μετά τις οχτώ", "Να γράψουν το όνομά τους και την ώρα αναχώρησης στο βιβλίο της εισόδου", "Να αφήσουν τις μπότες τους στο καταφύγιο"], 2, "γράψτε το όνομά σας και την ώρα που φεύγετε στο βιβλίο της εισόδου"),
 ],
 "gloss": {"ορειβατικού καταφυγίου": "ορειβατικό καταφύγιο — mountain refuge", "μπότες": "μπότα — boot", "παντόφλες": "παντόφλα — slipper", "κοιτώνες": "κοιτώνας — dormitory", "ξημερώσει": "ξημερώνει — dawn breaks", "απορριμματοφόρο": "απορριμματοφόρο — rubbish truck", "κορυφή": "κορυφή — summit", "ομάδα διάσωσης": "ομάδα διάσωσης — rescue team"},
})

ITEMS.append({
 "id": "l183-int-mouseiopaidagogos", "title": "Η μουσειοπαιδαγωγός", "title_en": "The museum educator", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια μουσειοπαιδαγωγό σε μια εκπομπή για τον πολιτισμό.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι κάνει ακριβώς μια μουσειοπαιδαγωγός;", "What exactly does a museum educator do?"),
  L("Μουσειοπαιδαγωγός", "f", "Σχεδιάζω προγράμματα που βοηθούν τους επισκέπτες, κυρίως παιδιά, να καταλάβουν τα εκθέματα. Δεν κάνω ξενάγηση με ημερομηνίες και ονόματα. Προτιμώ να τα βάζω να παρατηρούν. Για παράδειγμα, μπροστά σε ένα αρχαίο αγγείο τους ρωτάω: «Τι νομίζετε ότι έβαζαν μέσα; Πώς το κρατούσαν;»", "I design programmes that help visitors, mainly children, understand the exhibits. I don't give tours with dates and names. I prefer to get them to observe. For example, in front of an ancient vase I ask them: 'What do you think they put in it? How did they hold it?'"),
  L("Δημοσιογράφος", "m", "Και τα παιδιά απαντούν;", "And do the children answer?"),
  L("Μουσειοπαιδαγωγός", "f", "Πάντα, και συχνά πιο έξυπνα απ' ό,τι περιμένουμε. Ένα κοριτσάκι κάποτε πρόσεξε ότι ένας αμφορέας δεν μπορεί να σταθεί όρθιος, γιατί έχει μυτερό πάτο. Από εκεί ξεκινήσαμε μια ολόκληρη συζήτηση για το πώς τους μετέφεραν στα πλοία.", "Always, and often more cleverly than we expect. A little girl once noticed that an amphora can't stand upright, because it has a pointed bottom. From there we started a whole discussion about how they transported them on ships."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το μεγαλύτερο εμπόδιο στη δουλειά σας;", "What's the biggest obstacle in your work?"),
  L("Μουσειοπαιδαγωγός", "f", "Η ιδέα ότι το μουσείο είναι ένα μέρος όπου πρέπει να είσαι ήσυχος και να μην αγγίζεις τίποτα. Γι' αυτό σε κάθε πρόγραμμα έχουμε και αντίγραφα που τα παιδιά μπορούν να πιάσουν στα χέρια τους.", "The idea that a museum is a place where you have to be quiet and not touch anything. That's why in every programme we also have replicas that the children can hold in their hands."),
 ],
 "questions": [
  Q("Πώς δουλεύει με τα παιδιά;", ["Τους λέει ημερομηνίες και ονόματα", "Τα βάζει να παρατηρούν και να κάνουν υποθέσεις", "Τους δίνει τεστ στο τέλος", "Τους δείχνει ταινίες"], 1, "Προτιμώ να τα βάζω να παρατηρούν"),
  Q("Τι πρόσεξε κάποτε ένα κοριτσάκι;", ["Ότι ένα αγγείο ήταν σπασμένο", "Ότι ένας αμφορέας δεν μπορεί να σταθεί όρθιος, γιατί έχει μυτερό πάτο", "Ότι ένα άγαλμα δεν είχε χέρια", "Ότι τα χρώματα είχαν ξεθωριάσει"], 1, "ένας αμφορέας δεν μπορεί να σταθεί όρθιος, γιατί έχει μυτερό πάτο"),
  Q("Γιατί υπάρχουν αντίγραφα σε κάθε πρόγραμμα;", ["Για να μην κλέβονται τα πρωτότυπα", "Γιατί τα πρωτότυπα είναι σε αποθήκη", "Για να μπορούν τα παιδιά να τα πιάσουν στα χέρια τους", "Για να τα πουλάει το πωλητήριο"], 2, "αντίγραφα που τα παιδιά μπορούν να πιάσουν στα χέρια τους"),
 ],
 "gloss": {"μουσειοπαιδαγωγό": "μουσειοπαιδαγωγός — museum educator", "εκθέματα": "έκθεμα — exhibit", "ξενάγηση": "ξενάγηση — guided tour", "παρατηρούν": "παρατηρώ — to observe", "αγγείο": "αγγείο — vase, vessel", "αμφορέας": "αμφορέας — amphora", "μυτερό": "μυτερός — pointed", "πάτο": "πάτος — bottom", "εμπόδιο": "εμπόδιο — obstacle", "αντίγραφα": "αντίγραφο — replica, copy"},
})

ITEMS.append({
 "id": "l183-int-anthokomos", "title": "Η ανθοκόμος", "title_en": "The flower grower", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που καλλιεργεί λουλούδια σε θερμοκήπια, σε μια εκπομπή για την ύπαιθρο.",
 "script": [
  L("Δημοσιογράφος", "f", "Ποια είναι η πιο δύσκολη εποχή της χρονιάς για έναν ανθοκόμο;", "What's the hardest time of the year for a flower grower?"),
  L("Ανθοκόμος", "f", "Η Μεγάλη Εβδομάδα, χωρίς δεύτερη σκέψη. Κάθε ενορία στολίζει τον Επιτάφιο τη Μεγάλη Παρασκευή, και χρειάζονται χιλιάδες λουλούδια μέσα σε δύο τρεις μέρες. Τότε δουλεύουμε από τα χαράματα ως τα μεσάνυχτα. Ακολουθούν ο Άγιος Βαλεντίνος και η γιορτή της μητέρας.", "Holy Week, without a second thought. Every parish decorates the Epitaphios on Good Friday, and thousands of flowers are needed within two or three days. Then we work from dawn until midnight. Next come Valentine's Day and Mother's Day."),
  L("Δημοσιογράφος", "f", "Και πώς καταφέρνετε να είναι έτοιμα τα λουλούδια ακριβώς εκείνες τις μέρες;", "And how do you manage to have the flowers ready exactly on those days?"),
  L("Ανθοκόμος", "f", "Με πολύ προσεκτικό προγραμματισμό. Το Πάσχα αλλάζει ημερομηνία κάθε χρόνο, οπότε υπολογίζω πότε θα φυτέψω, και ρυθμίζω τη θερμοκρασία και το φως στο θερμοκήπιο. Μια εβδομάδα νωρίτερα ή αργότερα, και η σοδειά πάει χαμένη.", "With very careful planning. Easter changes date every year, so I calculate when I'll plant, and I adjust the temperature and light in the greenhouse. A week early or late, and the crop is wasted."),
  L("Δημοσιογράφος", "f", "Σας ανταγωνίζονται τα εισαγόμενα λουλούδια;", "Do imported flowers compete with you?"),
  L("Ανθοκόμος", "f", "Πολύ. Πολλά έρχονται από το εξωτερικό, ταξιδεύουν μέρες σε ψυγεία. Τα δικά μας κόβονται το πρωί και είναι στο ανθοπωλείο το απόγευμα, γι' αυτό κρατάνε περισσότερο στο βάζο.", "A lot. Many come from abroad and travel for days in refrigerated trucks. Ours are cut in the morning and are in the flower shop by the afternoon, which is why they last longer in the vase."),
 ],
 "questions": [
  Q("Ποια είναι η πιο δύσκολη εποχή για την ανθοκόμο;", ["Τα Χριστούγεννα", "Η Μεγάλη Εβδομάδα", "Το καλοκαίρι", "Ο Σεπτέμβριος"], 1, "Η Μεγάλη Εβδομάδα, χωρίς δεύτερη σκέψη"),
  Q("Γιατί πρέπει να προγραμματίζει προσεκτικά κάθε χρόνο;", ["Γιατί το Πάσχα αλλάζει ημερομηνία", "Γιατί αλλάζουν οι τιμές", "Γιατί αλλάζει ο καιρός", "Γιατί έχει λίγους εργάτες"], 0, "Το Πάσχα αλλάζει ημερομηνία κάθε χρόνο"),
  Q("Γιατί, κατά την ίδια, τα δικά της λουλούδια κρατάνε περισσότερο;", ["Γιατί είναι πιο ακριβά", "Γιατί ψεκάζονται λιγότερο", "Γιατί φτάνουν στο ανθοπωλείο την ίδια μέρα που κόβονται", "Γιατί είναι άλλες ποικιλίες"], 2, "Τα δικά μας κόβονται το πρωί και είναι στο ανθοπωλείο το απόγευμα"),
 ],
 "gloss": {"θερμοκήπια": "θερμοκήπιο — greenhouse", "ανθοκόμο": "ανθοκόμος — flower grower", "ενορία": "ενορία — parish", "στολίζει": "στολίζω — to decorate", "Επιτάφιο": "Επιτάφιος — the Epitaphios (bier of Christ, decorated with flowers on Good Friday)", "χαράματα": "χαράματα — daybreak", "προγραμματισμό": "προγραμματισμός — planning", "σοδειά": "σοδειά — crop, harvest", "εισαγόμενα": "εισαγόμενος — imported", "ανθοπωλείο": "ανθοπωλείο — flower shop"},
})

ITEMS.append({
 "id": "l183-vm-aimodosia-epeigon", "title": "Μήνυμα από την υπηρεσία αιμοδοσίας", "title_en": "A message from the blood donation service", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από την υπηρεσία αιμοδοσίας ενός νοσοκομείου.",
 "script": [
  L("Νοσηλεύτρια", "f", "Καλημέρα, κύριε Ραφαηλίδη. Σας τηλεφωνώ από την υπηρεσία αιμοδοσίας του Γενικού Νοσοκομείου. Είστε στη λίστα των τακτικών μας αιμοδοτών, και ξέρουμε ότι η ομάδα αίματός σας είναι μηδέν αρνητικό. Αυτή τη στιγμή τα αποθέματα αυτής της ομάδας είναι πολύ χαμηλά, γιατί μετά από ένα σοβαρό τροχαίο χρειάστηκαν πολλές μονάδες μέσα σε λίγες ώρες.", "Good morning, Mr Rafailidis. I'm calling from the blood donation service at the General Hospital. You're on our list of regular donors, and we know your blood group is O negative. At the moment the stocks of that group are very low, because after a serious road accident many units were needed within a few hours."),
  L("Νοσηλεύτρια", "f", "Από την τελευταία σας αιμοδοσία έχουν περάσει πάνω από τρεις μήνες, οπότε μπορείτε να ξαναδώσετε. Αν σας είναι εύκολο, ελάτε αύριο ή μεθαύριο, από τις οχτώ ως τις δύο. Μην έρθετε νηστικός· φάτε ένα ελαφρύ πρωινό και πιείτε άφθονο νερό. Αν δεν μπορείτε αυτή την εβδομάδα, πάρτε μας στο 2310 451 200 να κλείσουμε ένα ραντεβού για αργότερα. Σας ευχαριστούμε πολύ.", "More than three months have passed since your last donation, so you can give again. If it's convenient for you, come tomorrow or the day after, from eight to two. Don't come on an empty stomach; have a light breakfast and drink plenty of water. If you can't this week, call us on 2310 451 200 so we can book an appointment for later. Thank you very much."),
 ],
 "questions": [
  Q("Γιατί είναι χαμηλά τα αποθέματα της ομάδας μηδέν αρνητικό;", ["Γιατί είναι καλοκαίρι", "Γιατί χρειάστηκαν πολλές μονάδες μετά από ένα σοβαρό τροχαίο", "Γιατί χάλασε ένα ψυγείο", "Γιατί μειώθηκαν οι αιμοδότες"], 1, "μετά από ένα σοβαρό τροχαίο χρειάστηκαν πολλές μονάδες"),
  Q("Γιατί μπορεί ο κύριος Ραφαηλίδης να ξαναδώσει αίμα;", ["Γιατί έχουν περάσει πάνω από τρεις μήνες από την τελευταία φορά", "Γιατί είναι πάνω από πενήντα", "Γιατί το ζήτησε ο γιατρός του", "Γιατί έκανε εξετάσεις"], 0, "έχουν περάσει πάνω από τρεις μήνες, οπότε μπορείτε να ξαναδώσετε"),
  Q("Τι πρέπει να κάνει πριν έρθει;", ["Να μη φάει τίποτα", "Να πιει έναν καφέ", "Να φάει ένα ελαφρύ πρωινό και να πιει άφθονο νερό", "Να κλείσει ραντεβού οπωσδήποτε"], 2, "φάτε ένα ελαφρύ πρωινό και πιείτε άφθονο νερό"),
 ],
 "gloss": {"αιμοδοσίας": "αιμοδοσία — blood donation", "αιμοδοτών": "αιμοδότης — blood donor", "ομάδα αίματός": "ομάδα αίματος — blood group", "μηδέν αρνητικό": "μηδέν αρνητικό — O negative", "αποθέματα": "απόθεμα — stock, reserve", "τροχαίο": "τροχαίο — road accident", "μονάδες": "μονάδα — unit", "νηστικός": "νηστικός — on an empty stomach", "άφθονο": "άφθονος — plentiful"},
})

ITEMS.append({
 "id": "l183-mon-kryfa-ti-zygaria", "title": "Γιατί έκρυψα τη ζυγαριά", "title_en": "Why I hid the scales", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλά σε ένα πόντκαστ για μια μικρή αλλαγή στη ζωή της.",
 "script": [
  L("Μυρτώ", "f", "Για χρόνια ζυγιζόμουν κάθε πρωί, πριν καν πλύνω τα δόντια μου. Αν η ζυγαριά έδειχνε ένα κιλό παραπάνω, η μέρα μου είχε ήδη χαλάσει· αν έδειχνε ένα λιγότερο, έτρωγα ένα κομμάτι γλυκό για επιβράβευση, που φυσικά το πλήρωνα την επόμενη μέρα.", "For years I weighed myself every morning, before I even brushed my teeth. If the scales showed a kilo more, my day was already ruined; if they showed one less, I'd eat a piece of cake as a reward, which of course I paid for the next day."),
  L("Μυρτώ", "f", "Μια μέρα η διαιτολόγος μου μού εξήγησε ότι το βάρος μας αλλάζει μέσα στη μέρα, ακόμη και κατά ένα δυο κιλά, ανάλογα με το νερό, το αλάτι, τον ύπνο. Δηλαδή εγώ στενοχωριόμουν για αριθμούς που δεν σήμαιναν σχεδόν τίποτα.", "One day my dietitian explained to me that our weight changes during the day, even by a kilo or two, depending on water, salt, sleep. In other words, I was getting upset about numbers that meant almost nothing."),
  L("Μυρτώ", "f", "Έτσι έβαλα τη ζυγαριά στο πατάρι και ζυγίζομαι μία φορά τον μήνα. Τώρα καταλαβαίνω πώς είμαι από το πώς μου κάθεται το αγαπημένο μου τζιν και από το αν ανεβαίνω τις σκάλες χωρίς να λαχανιάζω. Και το πρωινό μου ξεκινά με καφέ, όχι με άγχος.", "So I put the scales up in the loft and I weigh myself once a month. Now I can tell how I'm doing from how my favourite jeans fit and from whether I climb the stairs without getting out of breath. And my morning starts with coffee, not with anxiety."),
 ],
 "questions": [
  Q("Τι έκανε η Μυρτώ όταν η ζυγαριά έδειχνε ένα κιλό λιγότερο;", ["Έκανε περισσότερη γυμναστική", "Έτρωγε ένα κομμάτι γλυκό για επιβράβευση", "Τηλεφωνούσε στη διαιτολόγο", "Ζυγιζόταν ξανά το βράδυ"], 1, "έτρωγα ένα κομμάτι γλυκό για επιβράβευση"),
  Q("Τι της εξήγησε η διαιτολόγος;", ["Ότι το βάρος αλλάζει μέσα στη μέρα, ακόμη και κατά ένα δυο κιλά", "Ότι η ζυγαριά της ήταν χαλασμένη", "Ότι πρέπει να ζυγίζεται κάθε βράδυ", "Ότι πρέπει να κόψει το αλάτι"], 0, "το βάρος μας αλλάζει μέσα στη μέρα, ακόμη και κατά ένα δυο κιλά"),
  Q("Πώς καταλαβαίνει τώρα πώς είναι;", ["Από μια εφαρμογή στο κινητό", "Από τις εξετάσεις αίματος", "Από το πώς της κάθεται το τζιν και από το αν λαχανιάζει στις σκάλες", "Από τα σχόλια των φίλων της"], 2, "από το πώς μου κάθεται το αγαπημένο μου τζιν"),
 ],
 "gloss": {"ζυγαριά": "ζυγαριά — scales", "ζυγιζόμουν": "ζυγίζομαι — to weigh oneself", "επιβράβευση": "επιβράβευση — reward", "διαιτολόγος": "διαιτολόγος — dietitian", "στενοχωριόμουν": "στενοχωριέμαι — to be upset", "πατάρι": "πατάρι — loft, storage space", "μου κάθεται": "μου κάθεται — it fits me", "λαχανιάζω": "λαχανιάζω — to get out of breath", "άγχος": "άγχος — anxiety"},
})

ITEMS.append({
 "id": "l183-dia-palia-paichnidia", "title": "Τι θα κάνουμε με τα παλιά παιχνίδια;", "title_en": "What shall we do with the old toys?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο γονείς να συζητούν τι θα κάνουν με τα παιχνίδια που τα παιδιά τους δεν παίζουν πια.",
 "script": [
  L("Λευτέρης", "m", "Άνοιξα σήμερα την ντουλάπα του διαδρόμου και μου έπεσαν στο κεφάλι τρία κουτιά με τουβλάκια. Τα παιδιά είναι δώδεκα και δεκατεσσάρων. Δεν νομίζω ότι θα τα ξαναπαίξουν.", "I opened the hall cupboard today and three boxes of building bricks fell on my head. The kids are twelve and fourteen. I don't think they'll play with them again."),
  L("Ρένα", "f", "Μην τα πετάξεις, σε παρακαλώ. Ο παιδικός σταθμός της γειτονιάς ζητούσε παιχνίδια τον περασμένο μήνα. Τα τουβλάκια και τα επιτραπέζια που είναι ολόκληρα μπορούμε να τους τα δώσουμε.", "Please don't throw them away. The neighbourhood nursery was asking for toys last month. We can give them the bricks and the board games that are complete."),
  L("Λευτέρης", "m", "Και τα λούτρινα; Είναι γύρω στα τριάντα.", "And the cuddly toys? There are about thirty of them."),
  L("Ρένα", "f", "Αυτά οι σταθμοί συνήθως δεν τα δέχονται, για λόγους υγιεινής. Θα τα πλύνουμε και θα τα δώσουμε στο κτηνιατρείο, που τα θέλει για τα κλουβιά των ζώων που νοσηλεύονται. Αλλά ρώτα πρώτα τη μικρή. Το κουνέλι με το ένα αυτί δεν θα το αφήσει να φύγει, να το ξέρεις.", "Nurseries don't usually accept those, for hygiene reasons. We'll wash them and give them to the vet's, which wants them for the cages of the animals being treated there. But ask our youngest first. She won't let the one-eared rabbit go, I can tell you."),
 ],
 "questions": [
  Q("Πού προτείνει η Ρένα να δώσουν τα τουβλάκια και τα επιτραπέζια;", ["Σε ένα σχολείο", "Στον παιδικό σταθμό της γειτονιάς", "Στα ανίψια τους", "Σε ένα παζάρι"], 1, "Ο παιδικός σταθμός της γειτονιάς ζητούσε παιχνίδια"),
  Q("Γιατί δεν θα δώσουν τα λούτρινα στον σταθμό;", ["Γιατί οι σταθμοί συνήθως δεν τα δέχονται για λόγους υγιεινής", "Γιατί είναι χαλασμένα", "Γιατί θέλουν να τα κρατήσουν", "Γιατί είναι πάρα πολλά"], 0, "Αυτά οι σταθμοί συνήθως δεν τα δέχονται, για λόγους υγιεινής"),
  Q("Τι θα κάνουν με τα λούτρινα;", ["Θα τα πουλήσουν στο διαδίκτυο", "Θα τα πετάξουν", "Θα τα πλύνουν και θα τα δώσουν στο κτηνιατρείο", "Θα τα βάλουν στο πατάρι"], 2, "Θα τα πλύνουμε και θα τα δώσουμε στο κτηνιατρείο"),
 ],
 "gloss": {"τουβλάκια": "τουβλάκι — toy brick", "επιτραπέζια": "επιτραπέζιο (παιχνίδι) — board game", "ολόκληρα": "ολόκληρος — whole, complete", "λούτρινα": "λούτρινο — cuddly toy", "υγιεινής": "υγιεινή — hygiene", "κτηνιατρείο": "κτηνιατρείο — vet's clinic", "κλουβιά": "κλουβί — cage", "νοσηλεύονται": "νοσηλεύομαι — to be treated in hospital"},
})

ITEMS.append({
 "id": "l183-news-dorean-metakinisi-mathiton", "title": "Δωρεάν μετακίνηση για τους μαθητές", "title_en": "Free travel for school pupils", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση από ένα τοπικό δελτίο ειδήσεων.",
 "script": [
  L("Παρουσιάστρια", "f", "Από τη Δευτέρα, όλοι οι μαθητές δημοτικού, γυμνασίου και λυκείου της πόλης θα μετακινούνται δωρεάν με τα αστικά λεωφορεία, τις εργάσιμες μέρες, από τις έξι το πρωί ως τις οχτώ το βράδυ. Θα αρκεί να δείχνουν στον οδηγό μια ειδική κάρτα, που θα μοιραστεί μέσω των σχολείων.", "From Monday, all primary, lower and upper secondary pupils in the town will travel free on city buses on working days, from six in the morning to eight in the evening. They will only need to show the driver a special card, which will be handed out through the schools."),
  L("Παρουσιάστρια", "f", "Ο δήμος εξηγεί ότι στόχος είναι να μειωθεί η κίνηση έξω από τα σχολεία τις ώρες αιχμής, όταν εκατοντάδες γονείς πηγαίνουν τα παιδιά τους με το αυτοκίνητο. Μια πρόσφατη έρευνα του δήμου έδειξε ότι σχεδόν τα μισά από αυτά τα δρομολόγια είναι μικρότερα από δύο χιλιόμετρα.", "The municipality explains that the aim is to reduce traffic outside schools at rush hour, when hundreds of parents take their children by car. A recent survey by the municipality showed that almost half of these trips are shorter than two kilometres."),
  L("Παρουσιάστρια", "f", "Οι σύλλογοι γονέων χαιρετίζουν το μέτρο, ζητούν όμως να αυξηθούν τα δρομολόγια στις γραμμές που περνούν από σχολεία, γιατί ήδη τα λεωφορεία γεμίζουν τις πρωινές ώρες.", "Parents' associations welcome the measure, but are asking for more services on the lines that pass schools, because the buses are already full in the morning hours."),
 ],
 "questions": [
  Q("Τι θα χρειάζονται οι μαθητές για να ταξιδεύουν δωρεάν;", ["Ένα εισιτήριο από το περίπτερο", "Μια ειδική κάρτα που θα μοιραστεί μέσω των σχολείων", "Την ταυτότητά τους", "Μια εφαρμογή στο κινητό"], 1, "να δείχνουν στον οδηγό μια ειδική κάρτα, που θα μοιραστεί μέσω των σχολείων"),
  Q("Τι έδειξε η έρευνα του δήμου;", ["Ότι σχεδόν τα μισά δρομολόγια των γονέων είναι μικρότερα από δύο χιλιόμετρα", "Ότι οι μαθητές δεν παίρνουν ποτέ λεωφορείο", "Ότι τα λεωφορεία είναι άδεια το πρωί", "Ότι οι γονείς προτιμούν το ποδήλατο"], 0, "σχεδόν τα μισά από αυτά τα δρομολόγια είναι μικρότερα από δύο χιλιόμετρα"),
  Q("Τι ζητούν οι σύλλογοι γονέων;", ["Να ισχύει το μέτρο και τα Σαββατοκύριακα", "Να καταργηθεί η κάρτα", "Να αυξηθούν τα δρομολόγια στις γραμμές που περνούν από σχολεία", "Να είναι δωρεάν και για τους γονείς"], 2, "να αυξηθούν τα δρομολόγια στις γραμμές που περνούν από σχολεία"),
 ],
 "gloss": {"μετακινούνται": "μετακινούμαι — to travel, get around", "αστικά λεωφορεία": "αστικό λεωφορείο — city bus", "εργάσιμες": "εργάσιμος — working (day)", "ώρες αιχμής": "ώρα αιχμής — rush hour", "δρομολόγια": "δρομολόγιο — trip, service", "σύλλογοι γονέων": "σύλλογος γονέων — parents' association", "χαιρετίζουν": "χαιρετίζω — to welcome", "μέτρο": "μέτρο — measure"},
})

ITEMS.append({
 "id": "l183-rep-giorti-sardelas", "title": "Η γιορτή της σαρδέλας", "title_en": "The sardine festival", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από το λιμάνι ενός παραθαλάσσιου χωριού ένα καλοκαιρινό βράδυ.",
 "script": [
  L("Ρεπόρτερ", "m", "Από το απόγευμα, η μυρωδιά από τις σχάρες απλώνεται σε όλο το λιμάνι. Οι ψαράδες του χωριού έχουν φέρει από το πρωί εκατοντάδες κιλά φρέσκες σαρδέλες, και εθελοντές τις ψήνουν σε μακριές σχάρες με κάρβουνα. Το πιάτο, με ψωμί και ντομάτα, κοστίζει τρία ευρώ, και τα χρήματα πηγαίνουν στον σύλλογο ψαράδων.", "Since the afternoon, the smell from the grills has been spreading across the whole harbour. The village fishermen have brought hundreds of kilos of fresh sardines since the morning, and volunteers grill them on long charcoal grills. A plate, with bread and tomato, costs three euros, and the money goes to the fishermen's association."),
  L("Ψαράς", "m", "Η σαρδέλα είναι το ψάρι του φτωχού, έτσι λέγαμε παλιά. Όμως είναι από τα πιο υγιεινά ψάρια, γεμάτη καλά λιπαρά, και ψαρεύεται εδώ, δίπλα μας. Τη γιορτή την ξεκινήσαμε για να θυμίσουμε στον κόσμο ότι δεν χρειάζεται να φάει ακριβό εισαγόμενο ψάρι για να φάει καλά.", "Sardines are the poor man's fish, that's what we used to say. But it's one of the healthiest fish, full of good fats, and it's caught here, right next to us. We started the festival to remind people that they don't need to eat expensive imported fish to eat well."),
  L("Ρεπόρτερ", "m", "Μετά το φαγητό, τα τραπέζια παραμερίζονται και η ορχήστρα ανεβαίνει σε μια βάρκα δεμένη στον μόλο. Ο χορός θα κρατήσει, όπως μας λένε, μέχρι να ξεκινήσουν τα καΐκια για το επόμενο ψάρεμα, λίγο πριν από το ξημέρωμα.", "After the meal, the tables are moved aside and the band climbs onto a boat moored at the jetty. The dancing will last, so we're told, until the boats set off for the next fishing trip, shortly before dawn."),
 ],
 "questions": [
  Q("Πού πηγαίνουν τα χρήματα από τα πιάτα;", ["Στον δήμο", "Στον σύλλογο ψαράδων", "Στο σχολείο του χωριού", "Στην ορχήστρα"], 1, "τα χρήματα πηγαίνουν στον σύλλογο ψαράδων"),
  Q("Γιατί ξεκίνησε η γιορτή, σύμφωνα με τον ψαρά;", ["Για να θυμίσει ότι δεν χρειάζεται ακριβό εισαγόμενο ψάρι για να φάει κανείς καλά", "Για να έρθουν περισσότεροι τουρίστες", "Για να πουληθούν οι σαρδέλες που περίσσευαν", "Για να γιορτάσει την ίδρυση του συλλόγου"], 0, "να θυμίσουμε στον κόσμο ότι δεν χρειάζεται να φάει ακριβό εισαγόμενο ψάρι"),
  Q("Πού παίζει η ορχήστρα;", ["Στην πλατεία", "Σε μια ταβέρνα", "Σε μια βάρκα δεμένη στον μόλο", "Στην εκκλησία"], 2, "η ορχήστρα ανεβαίνει σε μια βάρκα δεμένη στον μόλο"),
 ],
 "gloss": {"παραθαλάσσιου": "παραθαλάσσιος — seaside", "σχάρες": "σχάρα — grill", "σαρδέλες": "σαρδέλα — sardine", "κάρβουνα": "κάρβουνο — charcoal", "σύλλογο ψαράδων": "σύλλογος ψαράδων — fishermen's association", "λιπαρά": "λιπαρά — fats", "παραμερίζονται": "παραμερίζω — to move aside", "μόλο": "μόλος — jetty, pier", "ξημέρωμα": "ξημέρωμα — dawn"},
})

ITEMS.append({
 "id": "l183-c1-nifades-chioniou", "title": "Γιατί δεν υπάρχουν δύο ίδιες νιφάδες χιονιού", "title_en": "Why no two snowflakes are alike", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια φυσικό σε μια εκπομπή εκλαΐκευσης της επιστήμης.",
 "script": [
  L("Παρουσιαστής", "m", "Λένε ότι δεν υπάρχουν δύο νιφάδες χιονιού ακριβώς ίδιες. Είναι μύθος ή αλήθεια;", "They say no two snowflakes are exactly alike. Is it a myth or the truth?"),
  L("Φυσικός", "f", "Για τις μεγάλες, περίτεχνες νιφάδες, πρακτικά ισχύει. Μια νιφάδα ξεκινά από ένα μικροσκοπικό εξάγωνο κρυσταλλάκι πάγου, γιατί έτσι οργανώνονται τα μόρια του νερού όταν παγώνουν. Καθώς πέφτει, συναντά συνεχώς διαφορετική θερμοκρασία και υγρασία, και από αυτές εξαρτάται αν θα αναπτυχθούν πλάκες, βελόνες ή εκείνα τα γνωστά κλαδιά.", "For large, elaborate snowflakes, it's practically true. A snowflake starts as a tiny hexagonal ice crystal, because that's how water molecules organise themselves when they freeze. As it falls, it keeps meeting different temperatures and humidity, and these determine whether plates, needles or those familiar branches will grow."),
  L("Παρουσιαστής", "m", "Και γιατί τότε τα έξι κλαδιά μιας νιφάδας μοιάζουν τόσο μεταξύ τους;", "And why, then, do the six branches of a snowflake look so alike?"),
  L("Φυσικός", "f", "Ακριβώς επειδή μεγαλώνουν ταυτόχρονα και περνούν από τις ίδιες ακριβώς συνθήκες. Κάθε κλαδί «καταγράφει» το ταξίδι της νιφάδας μέσα στο σύννεφο. Δύο νιφάδες όμως ακολουθούν διαφορετικές διαδρομές, και ο αριθμός των πιθανών συνδυασμών είναι αστρονομικός, οπότε η πιθανότητα να προκύψουν δύο πανομοιότυπες είναι ουσιαστικά μηδενική.", "Precisely because they grow at the same time and go through exactly the same conditions. Each branch 'records' the snowflake's journey through the cloud. Two snowflakes, however, follow different paths, and the number of possible combinations is astronomical, so the probability of two identical ones arising is effectively zero."),
  L("Παρουσιαστής", "m", "Ισχύει και για τις πολύ μικρές νιφάδες;", "Does it also apply to very small snowflakes?"),
  L("Φυσικός", "f", "Όχι απαραίτητα. Τα πολύ απλά, μικρά κρυσταλλάκια, που δεν πρόλαβαν να αναπτυχθούν, μπορεί να μοιάζουν σχεδόν απόλυτα μεταξύ τους. Ο κανόνας αφορά κυρίως τις μεγάλες νιφάδες που βλέπουμε στις φωτογραφίες.", "Not necessarily. Very simple, small crystals that didn't have time to grow may look almost exactly alike. The rule mainly concerns the large snowflakes we see in photographs."),
 ],
 "questions": [
  Q("Γιατί μια νιφάδα ξεκινά από ένα εξάγωνο κρυσταλλάκι;", ["Γιατί έτσι οργανώνονται τα μόρια του νερού όταν παγώνουν", "Γιατί το σχήμα το δίνει ο αέρας", "Γιατί κολλάει πάνω σε σκόνη", "Γιατί έτσι πέφτει πιο γρήγορα"], 0, "έτσι οργανώνονται τα μόρια του νερού όταν παγώνουν"),
  Q("Γιατί τα έξι κλαδιά μιας νιφάδας μοιάζουν μεταξύ τους;", ["Γιατί έχουν την ίδια μάζα", "Γιατί μεγαλώνουν ταυτόχρονα κάτω από τις ίδιες ακριβώς συνθήκες", "Γιατί σπάνε με τον ίδιο τρόπο", "Γιατί είναι αντίγραφα του πρώτου κλαδιού"], 1, "επειδή μεγαλώνουν ταυτόχρονα και περνούν από τις ίδιες ακριβώς συνθήκες"),
  Q("Τι λέει η φυσικός για τις πολύ μικρές νιφάδες;", ["Ότι δεν σχηματίζονται ποτέ", "Ότι είναι πάντα διαφορετικές", "Ότι μπορεί να μοιάζουν σχεδόν απόλυτα μεταξύ τους", "Ότι λιώνουν πριν φτάσουν στη γη"], 2, "μπορεί να μοιάζουν σχεδόν απόλυτα μεταξύ τους"),
 ],
 "gloss": {"νιφάδες": "νιφάδα — snowflake", "εκλαΐκευσης": "εκλαΐκευση — popularisation", "περίτεχνες": "περίτεχνος — elaborate, intricate", "εξάγωνο": "εξάγωνος — hexagonal", "μόρια": "μόριο — molecule", "υγρασία": "υγρασία — humidity", "βελόνες": "βελόνα — needle", "ταυτόχρονα": "ταυτόχρονα — at the same time", "συνδυασμών": "συνδυασμός — combination", "πανομοιότυπες": "πανομοιότυπος — identical", "μηδενική": "μηδενικός — zero"},
})

ITEMS.append({
 "id": "l183-c1-idia-tragoudia-xana", "title": "Γιατί ακούμε τα ίδια τραγούδια ξανά και ξανά", "title_en": "Why we listen to the same songs again and again", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ψυχολόγο της μουσικής να μιλά σε μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Ψυχολόγος", "m", "Οι περισσότεροι από εμάς έχουμε ένα τραγούδι που το βάζουμε δέκα φορές στη σειρά, ενώ ξέρουμε κάθε νότα του απέξω. Θα περίμενε κανείς να μας κουράσει. Κι όμως, η γνώριμη μουσική μας δίνει μια ιδιαίτερη ευχαρίστηση: ο εγκέφαλος προβλέπει τι θα ακολουθήσει, και όταν η πρόβλεψη επιβεβαιώνεται, νιώθουμε κάτι σαν ανταμοιβή.", "Most of us have a song we play ten times in a row, even though we know every note of it by heart. You'd expect it to tire us. And yet familiar music gives us a special pleasure: the brain predicts what will come next, and when the prediction is confirmed, we feel something like a reward."),
  L("Ψυχολόγος", "m", "Οι ερευνητές μιλούν επίσης για το «φαινόμενο της απλής έκθεσης»: όσο συχνότερα συναντάμε κάτι, τόσο περισσότερο τείνουμε να μας αρέσει. Γι' αυτό ένα τραγούδι που στην αρχή μάς φάνηκε αδιάφορο μπορεί, μετά από μερικές ακροάσεις στο ραδιόφωνο, να γίνει το αγαπημένο μας.", "Researchers also talk about the 'mere exposure effect': the more often we encounter something, the more we tend to like it. That's why a song that seemed dull to us at first may, after a few listens on the radio, become our favourite."),
  L("Ψυχολόγος", "m", "Υπάρχει όμως κι ένα όριο. Αν το ακούσουμε υπερβολικά πολλές φορές, η ευχαρίστηση πέφτει απότομα, και το κάποτε αγαπημένο τραγούδι γίνεται ενοχλητικό. Επιπλέον, πολλοί επιστρέφουμε σε τραγούδια για τα συναισθήματα και τις αναμνήσεις που ξυπνούν: δεν ακούμε μόνο τη μελωδία, αλλά και το καλοκαίρι ή τον άνθρωπο με τον οποίο τη συνδέουμε.", "There is, however, a limit. If we hear it too many times, the pleasure drops sharply, and the once-favourite song becomes irritating. Moreover, many of us return to songs for the feelings and memories they awaken: we don't only hear the melody, but also the summer or the person we associate it with."),
 ],
 "questions": [
  Q("Γιατί, σύμφωνα με τον ψυχολόγο, μας ευχαριστεί η γνώριμη μουσική;", ["Γιατί είναι πιο απλή", "Γιατί ο εγκέφαλος προβλέπει τι θα ακολουθήσει και η επιβεβαίωση λειτουργεί σαν ανταμοιβή", "Γιατί μας χαλαρώνει ο ρυθμός", "Γιατί τη διαλέγουμε εμείς"], 1, "όταν η πρόβλεψη επιβεβαιώνεται, νιώθουμε κάτι σαν ανταμοιβή"),
  Q("Τι λέει το «φαινόμενο της απλής έκθεσης»;", ["Ότι όσο συχνότερα συναντάμε κάτι, τόσο περισσότερο τείνουμε να μας αρέσει", "Ότι βαριόμαστε γρήγορα ό,τι ακούμε συχνά", "Ότι προτιμάμε τη μουσική που ακούσαμε στην εφηβεία", "Ότι η μουσική επηρεάζει τη διάθεση"], 0, "όσο συχνότερα συναντάμε κάτι, τόσο περισσότερο τείνουμε να μας αρέσει"),
  Q("Τι συμβαίνει αν ακούσουμε ένα τραγούδι υπερβολικά πολλές φορές;", ["Το ξεχνάμε", "Μας αρέσει ακόμα περισσότερο", "Η ευχαρίστηση πέφτει απότομα και μπορεί να γίνει ενοχλητικό", "Αρχίζουμε να το τραγουδάμε"], 2, "η ευχαρίστηση πέφτει απότομα"),
 ],
 "gloss": {"απέξω": "απέξω — by heart", "γνώριμη": "γνώριμος — familiar", "προβλέπει": "προβλέπω — to predict", "επιβεβαιώνεται": "επιβεβαιώνομαι — to be confirmed", "ανταμοιβή": "ανταμοιβή — reward", "φαινόμενο της απλής έκθεσης": "φαινόμενο της απλής έκθεσης — mere exposure effect", "τείνουμε": "τείνω — to tend", "αδιάφορο": "αδιάφορος — dull, uninteresting", "ακροάσεις": "ακρόαση — listen, listening", "ενοχλητικό": "ενοχλητικός — irritating", "αναμνήσεις": "ανάμνηση — memory"},
})

rnd = random.Random(183)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-183.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
