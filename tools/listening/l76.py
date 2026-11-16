# Source for library/listening/listening-76.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l76.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l76-ann-marina", "title": "Προειδοποίηση για θυελλώδεις ανέμους στη μαρίνα", "title_en": "Gale warning at the marina", "type": "announcement", "level": "B2",
 "context_el": "Έχετε δέσει το σκάφος σας σε μια μαρίνα των Κυκλάδων. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα του γραφείου της μαρίνας για θυελλώδεις ανέμους.",
 "script": [
  L("Υπάλληλος", "f", "Προσοχή σε όλους τους ιδιοκτήτες και τα πληρώματα σκαφών. Η Εθνική Μετεωρολογική Υπηρεσία εξέδωσε έκτακτο δελτίο: από απόψε τα μεσάνυχτα αναμένονται βόρειοι άνεμοι οκτώ με εννιά μποφόρ, που θα διαρκέσουν τουλάχιστον μέχρι την Πέμπτη.", "Attention all boat owners and crews. The National Meteorological Service has issued an emergency bulletin: from midnight tonight north winds of force eight to nine are expected, lasting at least until Thursday."),
  L("Υπάλληλος", "f", "Παρακαλούμε να ελέγξετε τους κάβους και να προσθέσετε δεύτερο κάβο όπου χρειάζεται. Τοποθετήστε επιπλέον μπαλόνια ανάμεσα στο σκάφος σας και στα διπλανά, και κατεβάστε τα πανιά, τις τέντες και ό,τι άλλο μπορεί να παρασύρει ο αέρας. Κανένα σκάφος δεν επιτρέπεται να βγει από τη μαρίνα μέχρι νεωτέρας.", "Please check your mooring lines and add a second line where needed. Put extra fenders between your boat and the ones next to it, and take down sails, awnings and anything else the wind could carry off. No vessel is allowed to leave the marina until further notice."),
  L("Υπάλληλος", "f", "Ο σταθμός καυσίμων θα κλείσει σήμερα στις έξι το απόγευμα. Το προσωπικό της μαρίνας θα κάνει περιπολίες όλη τη νύχτα. Για οποιοδήποτε πρόβλημα, καλέστε στο κανάλι εννιά του ασυρμάτου.", "The fuel station will close today at six in the afternoon. Marina staff will patrol all night. For any problem, call on channel nine on the radio."),
 ],
 "questions": [
  Q("Τι αναμένεται από απόψε τα μεσάνυχτα;", ["Καταιγίδα με χαλάζι", "Βόρειοι άνεμοι οκτώ με εννιά μποφόρ", "Πυκνή ομίχλη", "Απεργία στα λιμάνια"], 1, "αναμένονται βόρειοι άνεμοι οκτώ με εννιά μποφόρ"),
  Q("Τι ζητείται από τους ιδιοκτήτες;", ["Να βγάλουν τα σκάφη από το νερό", "Να ελέγξουν τους κάβους και να προσθέσουν δεύτερο κάβο", "Να φύγουν αμέσως από τη μαρίνα", "Να γεμίσουν καύσιμα"], 1, "να ελέγξετε τους κάβους και να προσθέσετε δεύτερο κάβο"),
  Q("Πώς μπορούν να ζητήσουν βοήθεια τη νύχτα;", ["Στο τηλέφωνο της αστυνομίας", "Στο κανάλι εννιά του ασυρμάτου", "Στο γραφείο της μαρίνας", "Με ένα μήνυμα στο κινητό"], 1, "καλέστε στο κανάλι εννιά του ασυρμάτου"),
 ],
 "gloss": {"θυελλώδεις": "θυελλώδης — gale-force, stormy", "πληρώματα": "πλήρωμα — crew", "έκτακτο δελτίο": "έκτακτο δελτίο — emergency bulletin", "μποφόρ": "μποφόρ — Beaufort (wind force)", "κάβους": "κάβος — mooring line", "μπαλόνια": "μπαλόνι — fender (on a boat)", "πανιά": "πανί — sail", "τέντες": "τέντα — awning", "περιπολίες": "περιπολία — patrol", "ασυρμάτου": "ασύρματος — radio"},
})

ITEMS.append({
 "id": "l76-vm-steirosi", "title": "Η στείρωση της γάτας", "title_en": "Having the cat spayed", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει ραντεβού σε μια κτηνιατρική κλινική για τη στείρωση της γάτας σας. Θα ακούσετε ένα μήνυμα που σας άφησαν στον τηλεφωνητή.",
 "script": [
  L("Γραμματέας", "f", "Καλησπέρα σας, από την κτηνιατρική κλινική «Αρωγή» σας παίρνω, για το ραντεβού της Μπίλιας την Τρίτη. Θυμίζω ότι η γάτα πρέπει να είναι νηστική από τις δέκα το βράδυ της Δευτέρας. Νερό μπορεί να πίνει κανονικά μέχρι το πρωί.", "Good evening, I'm calling from the Arogi veterinary clinic, about Billia's appointment on Tuesday. A reminder that the cat must not eat from ten o'clock on Monday evening. She can drink water normally until the morning."),
  L("Γραμματέας", "f", "Φέρτε τη στις οχτώ και μισή, μέσα σε κλουβί μεταφοράς, όχι στην αγκαλιά σας. Η επέμβαση γίνεται με γενική αναισθησία και θα μπορείτε να την πάρετε το ίδιο απόγευμα, μετά τις πέντε, όταν θα έχει ξυπνήσει εντελώς.", "Bring her at half past eight, in a pet carrier, not in your arms. The operation is done under general anaesthetic and you'll be able to collect her the same afternoon, after five, when she's fully awake."),
  L("Γραμματέας", "f", "Για δέκα μέρες μετά θα φοράει ένα κολάρο σαν χωνί, για να μη γλείφει τα ράμματα. Ο γιατρός θα σας δώσει και ένα παυσίπονο. Αν θέλετε να αλλάξετε την ώρα, καλέστε μας ως αύριο το μεσημέρι.", "For ten days afterwards she'll wear a funnel-shaped collar so she doesn't lick the stitches. The vet will also give you a painkiller. If you want to change the time, call us by tomorrow noon."),
 ],
 "questions": [
  Q("Από πότε πρέπει η γάτα να μην τρώει;", ["Από το μεσημέρι της Δευτέρας", "Από τις δέκα το βράδυ της Δευτέρας", "Από το πρωί της Τρίτης", "Από την Κυριακή"], 1, "πρέπει να είναι νηστική από τις δέκα το βράδυ της Δευτέρας"),
  Q("Πότε μπορούν να πάρουν τη γάτα πίσω;", ["Την επόμενη μέρα", "Το ίδιο απόγευμα, μετά τις πέντε", "Μετά από δέκα μέρες", "Το ίδιο πρωί"], 1, "το ίδιο απόγευμα, μετά τις πέντε"),
  Q("Γιατί θα φοράει κολάρο η γάτα;", ["Για να μην κρυώνει", "Για να μη γλείφει τα ράμματα", "Για να μη χαθεί", "Για να μην τρώει"], 1, "για να μη γλείφει τα ράμματα"),
 ],
 "gloss": {"στείρωση": "στείρωση — spaying, neutering", "κτηνιατρική": "κτηνιατρικός — veterinary", "νηστική": "νηστικός — not having eaten, fasting", "επέμβαση": "επέμβαση — operation", "αναισθησία": "αναισθησία — anaesthesia", "κολάρο": "κολάρο — collar", "χωνί": "χωνί — funnel", "γλείφει": "γλείφω — to lick", "ράμματα": "ράμμα — stitch", "παυσίπονο": "παυσίπονο — painkiller"},
})

ITEMS.append({
 "id": "l76-dia-triimero-katharas", "title": "Πού θα πάμε το τριήμερο της Καθαράς Δευτέρας;", "title_en": "Where shall we go for the Clean Monday long weekend?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φίλοι κάνουν σχέδια για το τριήμερο της Καθαράς Δευτέρας.",
 "script": [
  L("Άρης", "m", "Λέω φέτος να πάμε στο Γαλαξίδι, για το αλευρομουτζούρωμα. Το έχω δει μόνο σε βίντεο: όλο το λιμάνι γεμάτο κόσμο που πετάει ο ένας στον άλλον χρωματιστό αλεύρι. Λένε ότι είναι απίστευτη εμπειρία.", "I say this year we go to Galaxidi, for the flour war. I've only seen it on video: the whole harbour full of people throwing coloured flour at each other. They say it's an incredible experience."),
  L("Νεφέλη", "f", "Απίστευτη, αλλά και χαοτική. Η ξαδέρφη μου πήγε πέρσι και έλεγε ότι έβγαζε αλεύρι από τα αυτιά της για τρεις μέρες. Και τα δωμάτια κλείνονται από τον Ιανουάριο, θα πληρώσουμε μια περιουσία.", "Incredible, but also chaotic. My cousin went last year and said she was getting flour out of her ears for three days. And rooms are booked up from January, we'll pay a fortune."),
  L("Άρης", "m", "Εντάξει, δίκιο έχεις για τα δωμάτια. Εσύ τι προτείνεις;", "OK, you're right about the rooms. What do you suggest?"),
  L("Νεφέλη", "f", "Να πάμε στο χωριό του πατέρα μου, στην Ευρυτανία. Το σπίτι είναι άδειο, πετάμε χαρταετό στο λόφο, τρώμε λαγάνα και ταραμά στην πλατεία με τους χωριανούς. Ήσυχα και δωρεάν. Και αν θέλεις τόσο πολύ το αλεύρι, μπορούμε να πάμε στο Γαλαξίδι για μια μέρα, φεύγοντας το πρωί της Δευτέρας.", "We go to my father's village, in Evrytania. The house is empty, we fly kites on the hill, we eat lagana and taramas in the square with the villagers. Quiet and free. And if you want the flour so badly, we can go to Galaxidi for one day, leaving on Monday morning."),
 ],
 "questions": [
  Q("Γιατί θέλει ο Άρης να πάνε στο Γαλαξίδι;", ["Για τα ψάρια", "Για το αλευρομουτζούρωμα", "Για να δουν φίλους", "Για το καρναβάλι της Πάτρας"], 1, "για το αλευρομουτζούρωμα"),
  Q("Τι πρόβλημα αναφέρει η Νεφέλη για το Γαλαξίδι;", ["Ότι είναι πολύ μακριά", "Ότι τα δωμάτια κλείνονται από τον Ιανουάριο και είναι ακριβά", "Ότι δεν της αρέσει η θάλασσα", "Ότι η γιορτή ακυρώθηκε"], 1, "τα δωμάτια κλείνονται από τον Ιανουάριο, θα πληρώσουμε μια περιουσία"),
  Q("Ποια λύση προτείνει τελικά η Νεφέλη;", ["Να μείνουν στην Αθήνα", "Να πάνε στο χωριό και στο Γαλαξίδι για μια μέρα", "Να πάνε μόνο στο Γαλαξίδι", "Να πάνε σε ένα νησί"], 1, "μπορούμε να πάμε στο Γαλαξίδι για μια μέρα"),
 ],
 "gloss": {"τριήμερο": "τριήμερο — long (three-day) weekend", "Καθαράς Δευτέρας": "Καθαρά Δευτέρα — Clean Monday (first day of Lent)", "αλευρομουτζούρωμα": "αλευρομουτζούρωμα — flour war (Galaxidi custom)", "αλεύρι": "αλεύρι — flour", "χαοτική": "χαοτικός — chaotic", "περιουσία": "περιουσία — fortune", "χαρταετό": "χαρταετός — kite", "λαγάνα": "λαγάνα — flat bread for Clean Monday", "ταραμά": "ταραμάς — fish-roe spread", "χωριανούς": "χωριανός — fellow villager"},
})

ITEMS.append({
 "id": "l76-dia-vasilopita", "title": "Ποιος θα φτιάξει τη βασιλόπιτα;", "title_en": "Who will make the New Year's cake?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδερφές συζητούν στο τηλέφωνο για την Πρωτοχρονιά, την πρώτη χρονιά χωρίς τη μητέρα τους.",
 "script": [
  L("Μαρία", "f", "Σκεφτόμουν την Πρωτοχρονιά. Τόσα χρόνια τη βασιλόπιτα την έφτιαχνε η μαμά. Φέτος ποια από τις δύο μας θα την κάνει;", "I was thinking about New Year's Day. All these years Mum made the vasilopita. This year which of us will make it?"),
  L("Λένα", "f", "Εγώ φοβάμαι ότι δεν θα βγει σαν τη δική της. Τη συνταγή την ήξερε απέξω, δεν την είχε γράψει πουθενά. Θυμάμαι μόνο ότι έβαζε πολύ πορτοκάλι και λίγο μαχλέπι.", "I'm afraid it won't turn out like hers. She knew the recipe by heart, she hadn't written it down anywhere. All I remember is that she put in a lot of orange and a little mahlab."),
  L("Μαρία", "f", "Βρήκα ένα τετράδιο στο ντουλάπι της κουζίνας, με συνταγές από τη γιαγιά. Η βασιλόπιτα είναι εκεί, με σημειώσεις της μαμάς στο περιθώριο: «λιγότερη ζάχαρη», «ψήνεται μια ώρα». Λέω να τη φτιάξουμε μαζί, την παραμονή, στο δικό μου σπίτι.", "I found a notebook in the kitchen cupboard, with recipes from Grandma. The vasilopita is in there, with Mum's notes in the margin: 'less sugar', 'bake for an hour'. I say we make it together, on New Year's Eve, at my place."),
  L("Λένα", "f", "Μου αρέσει αυτό. Και το φλουρί να το βάλουμε εμείς οι δύο, χωρίς να βλέπουν τα παιδιά. Όποιος κι αν το βρει, θα είναι σαν να μας το έδωσε εκείνη.", "I like that. And let's put the coin in, just the two of us, without the children seeing. Whoever finds it, it will be as if she gave it to us."),
 ],
 "questions": [
  Q("Γιατί φοβάται η Λένα να φτιάξει τη βασιλόπιτα;", ["Γιατί δεν της αρέσουν τα γλυκά", "Γιατί η μητέρα τους δεν είχε γράψει τη συνταγή", "Γιατί δεν έχει φούρνο", "Γιατί δεν έχει χρόνο"], 1, "δεν την είχε γράψει πουθενά"),
  Q("Τι βρήκε η Μαρία στο ντουλάπι της κουζίνας;", ["Το φλουρί της γιαγιάς", "Ένα τετράδιο με συνταγές και σημειώσεις της μαμάς", "Ένα ταψί", "Μια παλιά φωτογραφία"], 1, "Βρήκα ένα τετράδιο στο ντουλάπι της κουζίνας"),
  Q("Τι αποφασίζουν για το φλουρί;", ["Να μην το βάλουν φέτος", "Να το βάλουν οι δύο τους χωρίς να βλέπουν τα παιδιά", "Να το βάλουν τα παιδιά", "Να βάλουν δύο φλουριά"], 1, "το φλουρί να το βάλουμε εμείς οι δύο, χωρίς να βλέπουν τα παιδιά"),
 ],
 "gloss": {"βασιλόπιτα": "βασιλόπιτα — New Year's cake (vasilopita)", "απέξω": "απέξω — by heart", "μαχλέπι": "μαχλέπι — mahlab (spice)", "τετράδιο": "τετράδιο — notebook", "περιθώριο": "περιθώριο — margin", "ψήνεται": "ψήνομαι — to bake, be baked", "παραμονή": "παραμονή — eve", "φλουρί": "φλουρί — coin hidden in the vasilopita"},
})

ITEMS.append({
 "id": "l76-int-epimelitria", "title": "Μια επιμελήτρια μουσείου", "title_en": "A museum curator", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια επιμελήτρια αρχαιολογικού μουσείου σε μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "m", "Κυρία Σταυροπούλου, τι κάνει ακριβώς μια επιμελήτρια μουσείου;", "Ms Stavropoulou, what exactly does a museum curator do?"),
  L("Επιμελήτρια", "f", "Αποφασίζω ποια αντικείμενα θα εκτεθούν, πώς θα τοποθετηθούν και τι θα γράφουν οι λεζάντες. Πολλοί δεν το ξέρουν, αλλά στις προθήκες βλέπετε μόνο ένα μικρό μέρος από όσα έχει ένα μουσείο. Τα υπόλοιπα, συχνά χιλιάδες αντικείμενα, βρίσκονται στις αποθήκες.", "I decide which objects will be exhibited, how they'll be arranged and what the labels will say. Many people don't know it, but in the display cases you see only a small part of what a museum holds. The rest, often thousands of objects, are in the storerooms."),
  L("Δημοσιογράφος", "m", "Με ποιο κριτήριο διαλέγετε;", "By what criterion do you choose?"),
  L("Επιμελήτρια", "f", "Δεν διαλέγω πάντα το πιο εντυπωσιακό. Προσπαθώ να πω μια ιστορία. Ένα σπασμένο πήλινο παιχνίδι μπορεί να συγκινήσει περισσότερο από ένα χρυσό κόσμημα, αν ο επισκέπτης καταλάβει ότι κάποτε το κρατούσε ένα παιδί σαν το δικό του.", "I don't always choose the most impressive. I try to tell a story. A broken clay toy can move people more than a gold jewel, if the visitor understands that a child like their own once held it."),
  L("Δημοσιογράφος", "m", "Πώς έχει αλλάξει η δουλειά σας τα τελευταία χρόνια;", "How has your work changed in recent years?"),
  L("Επιμελήτρια", "f", "Πολύ. Παλιά οι λεζάντες ήταν γραμμένες για ειδικούς. Τώρα γράφουμε κείμενα που να τα καταλαβαίνει ένας δωδεκάχρονος, και προσθέτουμε αντίγραφα που μπορεί κανείς να αγγίξει, για τους τυφλούς επισκέπτες αλλά και για όλους. Το μουσείο δεν είναι πια ναός. Είναι τόπος συνάντησης.", "A lot. In the past labels were written for specialists. Now we write texts a twelve-year-old can understand, and we add copies that people can touch, for blind visitors but also for everyone. The museum is no longer a temple. It's a meeting place."),
 ],
 "questions": [
  Q("Τι δεν ξέρουν πολλοί για τα μουσεία, κατά την επιμελήτρια;", ["Ότι τα αντικείμενα είναι αντίγραφα", "Ότι στις προθήκες βλέπουμε μόνο ένα μικρό μέρος από όσα έχουν", "Ότι η είσοδος είναι δωρεάν", "Ότι κλείνουν τον χειμώνα"], 1, "στις προθήκες βλέπετε μόνο ένα μικρό μέρος από όσα έχει ένα μουσείο"),
  Q("Με ποιο κριτήριο διαλέγει τα αντικείμενα;", ["Διαλέγει πάντα το πιο εντυπωσιακό", "Προσπαθεί να πει μια ιστορία", "Διαλέγει τα πιο ακριβά", "Διαλέγει τα πιο παλιά"], 1, "Προσπαθώ να πω μια ιστορία"),
  Q("Για ποιον γράφονται σήμερα οι λεζάντες;", ["Για τους ειδικούς", "Ώστε να τις καταλαβαίνει ένας δωδεκάχρονος", "Μόνο για τους ξένους", "Για τους φοιτητές αρχαιολογίας"], 1, "γράφουμε κείμενα που να τα καταλαβαίνει ένας δωδεκάχρονος"),
 ],
 "gloss": {"επιμελήτρια": "επιμελήτρια — curator", "εκτεθούν": "εκτίθεμαι — to be exhibited", "λεζάντες": "λεζάντα — label, caption", "προθήκες": "προθήκη — display case", "αποθήκες": "αποθήκη — storeroom", "κριτήριο": "κριτήριο — criterion", "πήλινο": "πήλινος — clay", "κόσμημα": "κόσμημα — jewel", "αγγίξει": "αγγίζω — to touch"},
})

ITEMS.append({
 "id": "l76-rep-agriogida", "title": "Τα αγριόγιδα του Ολύμπου", "title_en": "The chamois of Mount Olympus", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για την άγρια ζωή, γυρισμένο στον Όλυμπο.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρισκόμαστε στα δύο χιλιάδες μέτρα, λίγο πάνω από το καταφύγιο. Ο φύλακας του Εθνικού Πάρκου μάς δείχνει με το κιάλι μια πλαγιά γεμάτη βράχια. Χρειάζονται μερικά λεπτά για να τα δούμε: πέντε αγριόγιδα, που πηδούν από βράχο σε βράχο με απίστευτη ευκολία.", "We are at two thousand metres, a little above the refuge. The National Park ranger points out a rocky slope to us with his binoculars. It takes a few minutes to see them: five chamois, jumping from rock to rock with incredible ease."),
  L("Ρεπόρτερ", "f", "Το μυστικό τους είναι οι οπλές: είναι σκληρές στις άκρες και μαλακές από κάτω, σαν σόλα παπουτσιού ορειβασίας. Το καλοκαίρι ανεβαίνουν ψηλά, κοντά στις κορυφές· τον χειμώνα κατεβαίνουν στα δάση, όπου βρίσκουν πιο εύκολα τροφή κάτω από το χιόνι.", "Their secret is their hooves: hard at the edges and soft underneath, like the sole of a climbing boot. In summer they go up high, near the peaks; in winter they come down into the forests, where they find food more easily under the snow."),
  L("Ρεπόρτερ", "f", "Το αγριόγιδο είναι αυστηρά προστατευόμενο είδος, όμως οι πληθυσμοί του στην Ελλάδα παραμένουν μικροί και διάσπαρτοι. Η λαθροθηρία εξακολουθεί να αποτελεί απειλή, όπως και η όχληση από ανθρώπους. «Ένας πεζοπόρος που φωνάζει ή ένα σκυλί χωρίς λουρί αρκούν για να τρέψουν ένα κοπάδι σε φυγή», λέει ο φύλακας. «Και κάθε φυγή, τον χειμώνα, κοστίζει ενέργεια που δεν έχουν.»", "The chamois is a strictly protected species, but its populations in Greece remain small and scattered. Poaching is still a threat, as is disturbance by people. 'A hiker who shouts or a dog off the lead is enough to put a herd to flight,' says the ranger. 'And every flight, in winter, costs energy they don't have.'"),
 ],
 "questions": [
  Q("Ποιο είναι το μυστικό των αγριόγιδων;", ["Τα μακριά τους πόδια", "Οι οπλές τους, σκληρές στις άκρες και μαλακές από κάτω", "Το χοντρό τους τρίχωμα", "Τα κέρατά τους"], 1, "Το μυστικό τους είναι οι οπλές"),
  Q("Πού πηγαίνουν τα αγριόγιδα τον χειμώνα;", ["Ανεβαίνουν στις κορυφές", "Κατεβαίνουν στα δάση", "Πηγαίνουν στη θάλασσα", "Μένουν σε σπηλιές"], 1, "τον χειμώνα κατεβαίνουν στα δάση"),
  Q("Γιατί είναι επικίνδυνο να τρομάζουν τα αγριόγιδα τον χειμώνα;", ["Γιατί πέφτουν στους γκρεμούς", "Γιατί κάθε φυγή κοστίζει ενέργεια που δεν έχουν", "Γιατί χάνουν τα μικρά τους", "Γιατί επιτίθενται στους ανθρώπους"], 1, "κάθε φυγή, τον χειμώνα, κοστίζει ενέργεια που δεν έχουν"),
 ],
 "gloss": {"αγριόγιδα": "αγριόγιδο — chamois", "καταφύγιο": "καταφύγιο — mountain refuge", "κιάλι": "κιάλι — binoculars", "οπλές": "οπλή — hoof", "ορειβασίας": "ορειβασία — mountaineering", "διάσπαρτοι": "διάσπαρτος — scattered", "λαθροθηρία": "λαθροθηρία — poaching", "όχληση": "όχληση — disturbance", "τρέψουν": "τρέπω (σε φυγή) — to put to flight", "κοπάδι": "κοπάδι — herd"},
})

ITEMS.append({
 "id": "l76-mono-fovos-ptisis", "title": "Ο φόβος της πτήσης", "title_en": "Fear of flying", "type": "monologue", "level": "B2",
 "context_el": "Ένας άντρας μιλάει σε ένα podcast για το πώς ξεπέρασε τον φόβο της πτήσης.",
 "script": [
  L("Τάσος", "m", "Για είκοσι χρόνια δεν μπήκα σε αεροπλάνο. Πήγαινα παντού με το πλοίο ή με το αυτοκίνητο, ακόμα και στη Γερμανία, όπου μένει ο αδερφός μου. Έλεγα ότι μου αρέσει να ταξιδεύω αργά, αλλά η αλήθεια ήταν ότι έτρεμα και μόνο στη σκέψη.", "For twenty years I didn't get on a plane. I went everywhere by boat or by car, even to Germany, where my brother lives. I said I liked to travel slowly, but the truth was that I trembled at the very thought."),
  L("Τάσος", "m", "Όταν γεννήθηκε η ανιψιά μου, αποφάσισα ότι έφτασε η ώρα. Έκανα ένα πρόγραμμα με μια ψυχολόγο που συνεργάζεται με μια αεροπορική εταιρεία. Μας εξήγησαν πώς πετάει ένα αεροπλάνο, τι είναι οι αναταράξεις και γιατί δεν είναι επικίνδυνες. Ένας πιλότος απάντησε σε όλες μας τις ερωτήσεις, ακόμα και στις πιο αφελείς.", "When my niece was born, I decided it was time. I did a programme with a psychologist who works with an airline. They explained how a plane flies, what turbulence is and why it isn't dangerous. A pilot answered all our questions, even the most naive ones."),
  L("Τάσος", "m", "Στο τέλος κάναμε μια σύντομη πτήση όλοι μαζί, από την Αθήνα στη Θεσσαλονίκη. Τα χέρια μου ίδρωναν και μετρούσα την ανάσα μου, όπως μας είχαν μάθει. Δεν θα πω ότι το απόλαυσα. Αλλά όταν προσγειωθήκαμε, όλη η ομάδα χειροκρότησε, και εγώ έκλαιγα σαν παιδί. Τον Μάρτιο πετάω στη Στουτγάρδη.", "At the end we all took a short flight together, from Athens to Thessaloniki. My hands were sweating and I counted my breaths, as they'd taught us. I won't say I enjoyed it. But when we landed, the whole group clapped, and I was crying like a child. In March I'm flying to Stuttgart."),
 ],
 "questions": [
  Q("Πώς ταξίδευε ο Τάσος όλα αυτά τα χρόνια;", ["Μόνο με το τρένο", "Με το πλοίο ή με το αυτοκίνητο", "Δεν ταξίδευε καθόλου", "Με το λεωφορείο"], 1, "Πήγαινα παντού με το πλοίο ή με το αυτοκίνητο"),
  Q("Τι τον έκανε να αποφασίσει να αντιμετωπίσει τον φόβο του;", ["Μια δουλειά στο εξωτερικό", "Η γέννηση της ανιψιάς του", "Μια συμβουλή του γιατρού", "Ένα ταξίδι με φίλους"], 1, "Όταν γεννήθηκε η ανιψιά μου, αποφάσισα ότι έφτασε η ώρα"),
  Q("Τι έγινε όταν προσγειώθηκαν;", ["Ο Τάσος λιποθύμησε", "Όλη η ομάδα χειροκρότησε και ο Τάσος έκλαιγε", "Ο πιλότος τους μίλησε", "Ο Τάσος γύρισε με το τρένο"], 1, "όλη η ομάδα χειροκρότησε, και εγώ έκλαιγα σαν παιδί"),
 ],
 "gloss": {"πτήσης": "πτήση — flight", "έτρεμα": "τρέμω — to tremble", "ανιψιά": "ανιψιά — niece", "αεροπορική εταιρεία": "αεροπορική εταιρεία — airline", "αναταράξεις": "αναταράξεις — turbulence", "πιλότος": "πιλότος — pilot", "αφελείς": "αφελής — naive", "ίδρωναν": "ιδρώνω — to sweat", "προσγειωθήκαμε": "προσγειώνομαι — to land", "χειροκρότησε": "χειροκροτώ — to clap, applaud"},
})

ITEMS.append({
 "id": "l76-mono-didymi", "title": "Μεγαλώνοντας με μια δίδυμη αδερφή", "title_en": "Growing up with a twin sister", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα μιλάει σε μια ραδιοφωνική εκπομπή για τη σχέση της με τη δίδυμη αδερφή της.",
 "script": [
  L("Αλίκη", "f", "Η Ναταλία και εγώ είμαστε μονοζυγωτικές δίδυμες. Μέχρι τα δώδεκα, η μητέρα μας μάς έντυνε ίδια, και οι δάσκαλοι στο σχολείο μάς φώναζαν «οι δίδυμες», σαν να ήμασταν ένα πρόσωπο. Κάποιες φορές αλλάζαμε θέσεις στην τάξη για πλάκα, και κανείς δεν το καταλάβαινε.", "Natalia and I are identical twins. Until we were twelve, our mother dressed us the same, and the teachers at school called us 'the twins', as if we were one person. Sometimes we swapped seats in class for fun, and nobody noticed."),
  L("Αλίκη", "f", "Στην εφηβεία, όμως, ένιωσα την ανάγκη να ξεχωρίσω. Έκοψα τα μαλλιά μου κοντά, άρχισα να παίζω μπάσκετ, ενώ εκείνη έκανε μπαλέτο. Για ένα διάστημα σχεδόν δεν μιλούσαμε. Η μητέρα μας στενοχωριόταν, αλλά ένας ψυχολόγος της είπε ότι ήταν απολύτως φυσιολογικό: έπρεπε η καθεμιά να βρει ποια είναι χωρίς την άλλη.", "In adolescence, though, I felt the need to stand out. I cut my hair short, started playing basketball, while she did ballet. For a while we hardly spoke. Our mother was upset, but a psychologist told her it was completely normal: each of us had to find out who she was without the other."),
  L("Αλίκη", "f", "Σήμερα ζούμε σε διαφορετικές πόλεις και έχουμε πολύ διαφορετικές ζωές. Αλλά υπάρχει κάτι που δεν εξηγείται: συχνά παίρνουμε τηλέφωνο η μία την άλλη την ίδια στιγμή, ή αγοράζουμε το ίδιο φόρεμα χωρίς να το ξέρουμε. Δεν πιστεύω σε τηλεπάθεια. Πιστεύω ότι σε ξέρει κάποιος τόσο καλά, που σκέφτεται σαν εσένα.", "Today we live in different cities and have very different lives. But there's something that can't be explained: we often call each other at the same moment, or buy the same dress without knowing it. I don't believe in telepathy. I believe someone knows you so well that they think like you."),
 ],
 "questions": [
  Q("Τι έκαναν κάποιες φορές οι δίδυμες στο σχολείο;", ["Έγραφαν η μία τις εξετάσεις της άλλης", "Άλλαζαν θέσεις στην τάξη για πλάκα", "Έλειπαν μαζί από το μάθημα", "Μάλωναν με τους δασκάλους"], 1, "Κάποιες φορές αλλάζαμε θέσεις στην τάξη για πλάκα"),
  Q("Τι είπε ο ψυχολόγος στη μητέρα τους;", ["Ότι έπρεπε να τις ντύνει ίδια", "Ότι ήταν φυσιολογικό να βρει η καθεμιά ποια είναι χωρίς την άλλη", "Ότι έπρεπε να πάνε σε διαφορετικά σχολεία", "Ότι είχαν πρόβλημα συμπεριφοράς"], 1, "έπρεπε η καθεμιά να βρει ποια είναι χωρίς την άλλη"),
  Q("Πώς εξηγεί η Αλίκη τις «συμπτώσεις» με την αδερφή της;", ["Με την τηλεπάθεια", "Ότι την ξέρει τόσο καλά, που σκέφτεται σαν εκείνη", "Με την τύχη", "Ότι μιλούν συνέχεια στο τηλέφωνο"], 1, "Πιστεύω ότι σε ξέρει κάποιος τόσο καλά, που σκέφτεται σαν εσένα"),
 ],
 "gloss": {"δίδυμη": "δίδυμος — twin", "μονοζυγωτικές": "μονοζυγωτικός — identical (twins)", "έντυνε": "ντύνω — to dress", "για πλάκα": "για πλάκα — for fun", "εφηβεία": "εφηβεία — adolescence", "ξεχωρίσω": "ξεχωρίζω — to stand out", "στενοχωριόταν": "στενοχωριέμαι — to be upset", "φυσιολογικό": "φυσιολογικός — normal", "τηλεπάθεια": "τηλεπάθεια — telepathy"},
})

ITEMS.append({
 "id": "l76-c1-katharsi", "title": "Η κάθαρση στην αρχαία τραγωδία", "title_en": "Catharsis in ancient tragedy", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε μια φιλόλογο να μιλάει σε μια σειρά διαλέξεων για το αρχαίο θέατρο.",
 "script": [
  L("Φιλόλογος", "f", "Στην «Ποιητική» του, ο Αριστοτέλης ορίζει την τραγωδία ως μίμηση μιας σοβαρής πράξης, η οποία, προκαλώντας έλεος και φόβο, επιτυγχάνει την κάθαρση τέτοιων παθημάτων. Η φράση είναι μία από τις πιο πολυσυζητημένες της παγκόσμιας γραμματείας, κυρίως επειδή ο Αριστοτέλης δεν εξηγεί πουθενά τι ακριβώς εννοεί με τη λέξη «κάθαρση».", "In his Poetics, Aristotle defines tragedy as the imitation of a serious action which, by arousing pity and fear, achieves the catharsis of such emotions. The phrase is one of the most debated in world literature, mainly because Aristotle nowhere explains what exactly he means by the word 'catharsis'."),
  L("Φιλόλογος", "f", "Οι ερμηνείες χωρίζονται, σε γενικές γραμμές, σε τρεις κατηγορίες. Η πρώτη τη συνδέει με τη θρησκεία: η κάθαρση ως εξαγνισμός της ψυχής. Η δεύτερη, που επικράτησε από τον δέκατο ένατο αιώνα, τη διαβάζει ως ιατρικό όρο: ο θεατής απαλλάσσεται από τα συσσωρευμένα συναισθήματα, όπως ο οργανισμός αποβάλλει ό,τι τον βλάπτει. Ας μην ξεχνάμε ότι ο πατέρας του Αριστοτέλη ήταν γιατρός.", "The interpretations fall, broadly speaking, into three categories. The first links it to religion: catharsis as purification of the soul. The second, which prevailed from the nineteenth century, reads it as a medical term: the spectator is relieved of accumulated emotions, as the body expels what harms it. Let us not forget that Aristotle's father was a doctor."),
  L("Φιλόλογος", "f", "Η τρίτη ερμηνεία είναι διανοητική: κάθαρση σημαίνει διαύγεια. Βλέποντας τον Οιδίποδα να καταρρέει, ο θεατής δεν «ξαλαφρώνει» απλώς· κατανοεί κάτι για την ανθρώπινη μοίρα, για τα όρια της γνώσης και της δύναμης. Το έλεος και ο φόβος δεν εξαφανίζονται, αλλά μετασχηματίζονται σε γνώση.", "The third interpretation is intellectual: catharsis means clarity. Watching Oedipus collapse, the spectator does not simply 'feel relieved'; they understand something about human fate, about the limits of knowledge and power. Pity and fear do not vanish, but are transformed into knowledge."),
  L("Φιλόλογος", "f", "Το ενδιαφέρον είναι ότι η έννοια επιβιώνει σήμερα σε πεδία που ο Αριστοτέλης δεν θα φανταζόταν: στην ψυχοθεραπεία, στη δραματοθεραπεία, ακόμα και στην καθημερινή γλώσσα, όταν λέμε ότι μια ταινία ή ένα κλάμα «μας λύτρωσε». Ίσως η ασάφεια του ορισμού να είναι ακριβώς ο λόγος που η λέξη έζησε τόσους αιώνες.", "What is interesting is that the concept survives today in fields Aristotle could not have imagined: in psychotherapy, in drama therapy, even in everyday language, when we say that a film or a good cry 'released' us. Perhaps the vagueness of the definition is precisely the reason the word has lived for so many centuries."),
 ],
 "questions": [
  Q("Γιατί η φράση του Αριστοτέλη είναι τόσο πολυσυζητημένη;", ["Γιατί σώζεται σε κακή κατάσταση", "Γιατί δεν εξηγεί πουθενά τι εννοεί με τη λέξη «κάθαρση»", "Γιατί είναι γραμμένη σε ποίηση", "Γιατί έρχεται σε αντίθεση με τον Πλάτωνα"], 1, "ο Αριστοτέλης δεν εξηγεί πουθενά τι ακριβώς εννοεί με τη λέξη «κάθαρση»"),
  Q("Ποιο στοιχείο υποστηρίζει την ιατρική ερμηνεία;", ["Ότι ο Αριστοτέλης έγραψε για την ιατρική", "Ότι ο πατέρας του Αριστοτέλη ήταν γιατρός", "Ότι οι θεατές ήταν άρρωστοι", "Ότι οι τραγωδίες παίζονταν σε ιερά"], 1, "ο πατέρας του Αριστοτέλη ήταν γιατρός"),
  Q("Τι σημαίνει κάθαρση κατά τη διανοητική ερμηνεία;", ["Εξαγνισμός της ψυχής", "Διαύγεια, κατανόηση της ανθρώπινης μοίρας", "Απαλλαγή από τα συναισθήματα", "Διασκέδαση"], 1, "κάθαρση σημαίνει διαύγεια"),
  Q("Ποια υπόθεση κάνει η φιλόλογος στο τέλος;", ["Ότι η λέξη θα ξεχαστεί", "Ότι η ασάφεια του ορισμού ίσως εξηγεί γιατί η λέξη έζησε τόσους αιώνες", "Ότι ο Αριστοτέλης δεν έγραψε την «Ποιητική»", "Ότι η ψυχοθεραπεία παρεξήγησε τον όρο"], 1, "Ίσως η ασάφεια του ορισμού να είναι ακριβώς ο λόγος που η λέξη έζησε τόσους αιώνες"),
 ],
 "gloss": {"κάθαρση": "κάθαρση — catharsis, purgation", "μίμηση": "μίμηση — imitation", "έλεος": "έλεος — pity", "παθημάτων": "πάθημα — emotion, suffering", "πολυσυζητημένες": "πολυσυζητημένος — much-debated", "εξαγνισμός": "εξαγνισμός — purification", "απαλλάσσεται": "απαλλάσσομαι — to be relieved of", "συσσωρευμένα": "συσσωρευμένος — accumulated", "διαύγεια": "διαύγεια — clarity", "μετασχηματίζονται": "μετασχηματίζομαι — to be transformed", "λύτρωσε": "λυτρώνω — to release, redeem", "ασάφεια": "ασάφεια — vagueness"},
})

ITEMS.append({
 "id": "l76-c1-iatriki-orologia", "title": "Τα ελληνικά της ιατρικής", "title_en": "The Greek of medicine", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν γιατρό και ιστορικό της ιατρικής σε μια εκπομπή για τη γλώσσα.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Αναστασίου, γιατί η ιατρική ορολογία είναι γεμάτη ελληνικές λέξεις;", "Mr Anastasiou, why is medical terminology full of Greek words?"),
  L("Γιατρός", "m", "Εν μέρει λόγω παράδοσης: τα κείμενα του Ιπποκράτη και του Γαληνού διδάσκονταν στα ευρωπαϊκά πανεπιστήμια για αιώνες. Όμως οι περισσότεροι όροι που χρησιμοποιούμε σήμερα δεν είναι αρχαίοι. Πλάστηκαν τον δέκατο όγδοο και τον δέκατο ένατο αιώνα από γιατρούς που συνδύαζαν ελληνικές ρίζες, όπως σήμερα συνδυάζουμε τουβλάκια.", "Partly because of tradition: the texts of Hippocrates and Galen were taught in European universities for centuries. But most of the terms we use today aren't ancient. They were coined in the eighteenth and nineteenth centuries by doctors who combined Greek roots, the way we combine building blocks today."),
  L("Δημοσιογράφος", "f", "Μπορείτε να μας δώσετε ένα παράδειγμα;", "Can you give us an example?"),
  L("Γιατρός", "m", "Η κατάληξη «-ίτιδα» σημαίνει φλεγμονή: αμυγδαλίτιδα, ωτίτιδα, γαστρίτιδα. Η «-εκτομή» σημαίνει αφαίρεση: σκωληκοειδεκτομή. Αν ξέρεις δέκα-δεκαπέντε τέτοια κομμάτια, μπορείς να μαντέψεις τι σημαίνουν εκατοντάδες όροι. Γι’ αυτό οι Έλληνες φοιτητές ιατρικής έχουν ένα πλεονέκτημα στην αρχή των σπουδών τους.", "The ending '-itis' means inflammation: tonsillitis, otitis, gastritis. '-ectomy' means removal: appendectomy. If you know ten or fifteen such pieces, you can guess what hundreds of terms mean. That's why Greek medical students have an advantage at the start of their studies."),
  L("Δημοσιογράφος", "f", "Υπάρχουν και παγίδες;", "Are there pitfalls too?"),
  L("Γιατρός", "m", "Βεβαίως. Μερικές λέξεις κουβαλούν προκαταλήψεις άλλων εποχών. Η «υστερία», για παράδειγμα, προέρχεται από την «υστέρα», τη μήτρα, γιατί κάποτε πίστευαν ότι μόνο οι γυναίκες έπασχαν από αυτήν. Ο όρος έχει πια εγκαταλειφθεί από την ψυχιατρική. Η γλώσσα της επιστήμης, όπως βλέπετε, δεν είναι ποτέ εντελώς ουδέτερη.", "Of course. Some words carry the prejudices of other eras. 'Hysteria', for example, comes from 'hystera', the womb, because it was once believed that only women suffered from it. The term has now been abandoned by psychiatry. The language of science, as you see, is never entirely neutral."),
 ],
 "questions": [
  Q("Πότε πλάστηκαν οι περισσότεροι ιατρικοί όροι που χρησιμοποιούμε σήμερα;", ["Στην αρχαιότητα", "Τον δέκατο όγδοο και τον δέκατο ένατο αιώνα", "Στον Μεσαίωνα", "Τον εικοστό πρώτο αιώνα"], 1, "Πλάστηκαν τον δέκατο όγδοο και τον δέκατο ένατο αιώνα"),
  Q("Τι σημαίνει η κατάληξη «-ίτιδα»;", ["Αφαίρεση", "Φλεγμονή", "Πόνος", "Όγκος"], 1, "Η κατάληξη «-ίτιδα» σημαίνει φλεγμονή"),
  Q("Γιατί οι Έλληνες φοιτητές ιατρικής έχουν πλεονέκτημα;", ["Γιατί διαβάζουν τον Ιπποκράτη στο πρωτότυπο", "Γιατί μπορούν να μαντέψουν τι σημαίνουν εκατοντάδες όροι", "Γιατί οι εξετάσεις γίνονται στα ελληνικά", "Γιατί έχουν καλύτερους καθηγητές"], 1, "μπορείς να μαντέψεις τι σημαίνουν εκατοντάδες όροι"),
  Q("Τι δείχνει, κατά τον γιατρό, το παράδειγμα της «υστερίας»;", ["Ότι οι αρχαίοι γιατροί είχαν δίκιο", "Ότι η γλώσσα της επιστήμης δεν είναι ποτέ εντελώς ουδέτερη", "Ότι ο όρος χρησιμοποιείται ακόμα", "Ότι η λέξη είναι λατινική"], 1, "Η γλώσσα της επιστήμης, όπως βλέπετε, δεν είναι ποτέ εντελώς ουδέτερη"),
 ],
 "gloss": {"ορολογία": "ορολογία — terminology", "Πλάστηκαν": "πλάθομαι — to be coined, formed", "ρίζες": "ρίζα — root", "τουβλάκια": "τουβλάκι — building block", "κατάληξη": "κατάληξη — ending, suffix", "φλεγμονή": "φλεγμονή — inflammation", "αφαίρεση": "αφαίρεση — removal", "σκωληκοειδεκτομή": "σκωληκοειδεκτομή — appendectomy", "προκαταλήψεις": "προκατάληψη — prejudice", "μήτρα": "μήτρα — womb", "έπασχαν": "πάσχω — to suffer (from an illness)", "ουδέτερη": "ουδέτερος — neutral"},
})

rnd = random.Random(76)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-76.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
