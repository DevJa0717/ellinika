# Source for library/listening/listening-106.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l106.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l106-ann-elegxos-diaviti", "title": "Δωρεάν έλεγχος για τον διαβήτη", "title_en": "Free diabetes screening", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του κέντρου υγείας στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνήτρια", "f", "Το κέντρο υγείας της πόλης, με αφορμή την Παγκόσμια Ημέρα Διαβήτη, πραγματοποιεί δωρεάν προληπτικό έλεγχο για τον διαβήτη την επόμενη Τετάρτη και Πέμπτη, από τις οχτώ το πρωί ως τις δώδεκα το μεσημέρι.", "The town's health centre, on the occasion of World Diabetes Day, is carrying out free preventive diabetes screening next Wednesday and Thursday, from eight in the morning until twelve noon."),
  L("Εκφωνήτρια", "f", "Ο έλεγχος περιλαμβάνει μέτρηση του σακχάρου με μια σταγόνα αίμα από το δάχτυλο, μέτρηση της αρτηριακής πίεσης και του βάρους. Οι ενδιαφερόμενοι πρέπει να έρθουν νηστικοί, δηλαδή να μην έχουν φάει τίποτα για τουλάχιστον οχτώ ώρες. Επιτρέπεται μόνο λίγο νερό.", "The screening includes measuring blood sugar with a drop of blood from the finger, and measuring blood pressure and weight. Those interested must come fasting, that is, not having eaten anything for at least eight hours. Only a little water is allowed."),
  L("Εκφωνήτρια", "f", "Ο έλεγχος απευθύνεται κυρίως σε ενήλικες άνω των σαράντα πέντε ετών και σε όσους έχουν συγγενείς με διαβήτη. Δεν χρειάζεται ραντεβού. Όσοι έχουν τιμές εκτός ορίων θα παραπέμπονται στον γιατρό του κέντρου για περαιτέρω εξετάσεις.", "The screening is aimed mainly at adults over forty-five and at those who have relatives with diabetes. No appointment is needed. Anyone with values outside the normal range will be referred to the centre's doctor for further tests."),
 ],
 "questions": [
  Q("Τι περιλαμβάνει ο έλεγχος;", ["Ακτινογραφία και καρδιογράφημα", "Μέτρηση σακχάρου, αρτηριακής πίεσης και βάρους", "Μόνο μέτρηση βάρους", "Εξέταση ματιών"], 1, "μέτρηση του σακχάρου με μια σταγόνα αίμα από το δάχτυλο, μέτρηση της αρτηριακής πίεσης και του βάρους"),
  Q("Τι πρέπει να κάνουν πριν από τον έλεγχο;", ["Να κλείσουν ραντεβού", "Να φέρουν τις παλιές τους εξετάσεις", "Να μην έχουν φάει τίποτα για τουλάχιστον οχτώ ώρες", "Να πιουν πολύ νερό"], 2, "να μην έχουν φάει τίποτα για τουλάχιστον οχτώ ώρες"),
  Q("Σε ποιους απευθύνεται κυρίως ο έλεγχος;", ["Σε ενήλικες άνω των σαράντα πέντε και σε όσους έχουν συγγενείς με διαβήτη", "Σε παιδιά και εφήβους", "Μόνο σε όσους έχουν ήδη διαβήτη", "Σε έγκυες γυναίκες"], 0, "απευθύνεται κυρίως σε ενήλικες άνω των σαράντα πέντε ετών και σε όσους έχουν συγγενείς με διαβήτη"),
 ],
 "gloss": {"διαβήτη": "διαβήτης — diabetes", "προληπτικό": "προληπτικός — preventive", "σακχάρου": "σάκχαρο — blood sugar", "αρτηριακής": "αρτηριακή πίεση — blood pressure", "νηστικοί": "νηστικός — fasting, with an empty stomach", "παραπέμπονται": "παραπέμπω — to refer", "περαιτέρω": "περαιτέρω — further"}
})

ITEMS.append({
 "id": "l106-vm-plyntirio-piaton", "title": "Μήνυμα από τον τεχνικό για το πλυντήριο πιάτων", "title_en": "A message from the technician about the dishwasher", "type": "voicemail", "level": "B2",
 "context_el": "Το πλυντήριο πιάτων σας χάλασε. Ακούτε ένα μήνυμα από τον τεχνικό στον τηλεφωνητή.",
 "script": [
  L("Τεχνικός", "m", "Καλησπέρα, κυρία Δημητρίου, ο Λευτέρης είμαι, ο τεχνικός που ήρθε χθες για το πλυντήριο πιάτων. Σας τηλεφωνώ για να σας πω τι βρήκα. Η αντλία που βγάζει το νερό έχει καεί, γι' αυτό έμενε νερό στον πάτο.", "Good evening, Mrs Dimitriou, it's Lefteris, the technician who came yesterday about the dishwasher. I'm calling to tell you what I found. The pump that drains the water has burnt out, which is why water was left in the bottom."),
  L("Τεχνικός", "m", "Το ανταλλακτικό κοστίζει ογδόντα ευρώ και η εργασία άλλα σαράντα. Επειδή όμως το πλυντήριο είναι δώδεκα χρονών, να ξέρετε ότι μπορεί σύντομα να χαλάσει κάτι άλλο. Ένα καινούργιο, μεσαίας κατηγορίας, κοστίζει γύρω στα τετρακόσια. Η απόφαση είναι δική σας.", "The spare part costs eighty euros and the labour another forty. But because the dishwasher is twelve years old, you should know that something else may soon break. A new one, mid-range, costs around four hundred. The decision is yours."),
  L("Τεχνικός", "m", "Αν θέλετε να το φτιάξουμε, πρέπει να παραγγείλω το ανταλλακτικό, που θα έρθει σε τρεις με τέσσερις εργάσιμες. Μέχρι τότε, σας παρακαλώ, μην το χρησιμοποιείτε, γιατί μπορεί να τρέξουν νερά στο πάτωμα. Πάρτε με όποτε μπορείτε, ως τις οχτώ το βράδυ.", "If you want us to repair it, I need to order the spare part, which will arrive in three to four working days. Until then, please don't use it, because water may leak onto the floor. Call me whenever you can, until eight in the evening."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα του πλυντηρίου;", ["Η πόρτα δεν κλείνει", "Η αντλία που βγάζει το νερό έχει καεί", "Δεν ζεσταίνει το νερό", "Έχει σπάσει το καλάθι"], 1, "Η αντλία που βγάζει το νερό έχει καεί"),
  Q("Γιατί ο τεχνικός αναφέρει την τιμή ενός καινούργιου;", ["Γιατί το ανταλλακτικό δεν υπάρχει", "Γιατί η επισκευή κοστίζει περισσότερο από καινούργιο", "Γιατί ο ίδιος πουλάει πλυντήρια", "Γιατί το πλυντήριο είναι δώδεκα χρονών και μπορεί σύντομα να χαλάσει κάτι άλλο"], 3, "Επειδή όμως το πλυντήριο είναι δώδεκα χρονών, να ξέρετε ότι μπορεί σύντομα να χαλάσει κάτι άλλο"),
  Q("Τι ζητά να μην κάνει μέχρι την επισκευή;", ["Να μην το χρησιμοποιεί", "Να μην το βγάλει από την πρίζα", "Να μην ανοίξει την πόρτα", "Να μην τον πάρει τηλέφωνο"], 0, "μην το χρησιμοποιείτε"),
 ],
 "gloss": {"αντλία": "αντλία — pump", "καεί": "καίγομαι — to burn out", "πάτο": "πάτος — bottom", "ανταλλακτικό": "ανταλλακτικό — spare part", "εργασία": "εργασία — labour", "εργάσιμες": "εργάσιμη (μέρα) — working day"}
})

ITEMS.append({
 "id": "l106-dia-scholiki-giorti", "title": "Ποιος θα πάει στη σχολική γιορτή;", "title_en": "Who will go to the school show?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο γονείς οργανώνουν την εβδομάδα τους.",
 "script": [
  L("Ρένα", "f", "Θυμάσαι ότι την Πέμπτη στις έντεκα είναι η χριστουγεννιάτικη γιορτή της Άννας; Λέει ένα ποίημα και είναι πολύ αγχωμένη.", "Do you remember that on Thursday at eleven it's Anna's Christmas show? She's reciting a poem and she's very nervous."),
  L("Γιώργος", "m", "Την Πέμπτη; Έχω τη σύσκεψη με τους πελάτες από τη Θεσσαλονίκη. Δεν μπορώ να τη μεταθέσω, έρχονται ειδικά γι' αυτό.", "Thursday? I've got the meeting with the clients from Thessaloniki. I can't move it, they're coming specially for it."),
  L("Ρένα", "f", "Κι εγώ έχω βάρδια στο νοσοκομείο μέχρι τις δύο. Μπορώ να ζητήσω από τη Μαίρη να με καλύψει για δύο ώρες, αλλά της χρωστάω ήδη μια χάρη.", "And I'm on shift at the hospital until two. I could ask Mary to cover for me for two hours, but I already owe her a favour."),
  L("Γιώργος", "m", "Τι ώρα ακριβώς λέει το ποίημά της;", "What time exactly is she reciting her poem?"),
  L("Ρένα", "f", "Η δασκάλα είπε ότι η τάξη της είναι τρίτη στο πρόγραμμα, άρα γύρω στις έντεκα και μισή.", "The teacher said her class is third in the programme, so around half past eleven."),
  L("Γιώργος", "m", "Η σύσκεψη ξεκινά στις δέκα. Αν ζητήσω να κάνουμε ένα διάλειμμα στις έντεκα και τέταρτο, το σχολείο είναι δέκα λεπτά με τα πόδια. Θα δω το ποίημα και θα γυρίσω.", "The meeting starts at ten. If I ask for a break at quarter past eleven, the school is ten minutes' walk away. I'll see the poem and come back."),
  L("Ρένα", "f", "Τέλεια! Και τράβηξέ τη βίντεο, σε παρακαλώ, να το δει και η γιαγιά. Εγώ θα την πάρω από το σχολείο στις δύο και μισή.", "Perfect! And film her, please, so that grandma can see it too. I'll pick her up from school at half past two."),
 ],
 "questions": [
  Q("Γιατί δεν μπορεί να πάει η Ρένα;", ["Γιατί είναι άρρωστη", "Γιατί έχει βάρδια στο νοσοκομείο μέχρι τις δύο", "Γιατί έχει σύσκεψη με πελάτες", "Γιατί πρέπει να πάει στη γιαγιά"], 1, "έχω βάρδια στο νοσοκομείο μέχρι τις δύο"),
  Q("Γύρω στις πόσες θα πει το ποίημα η Άννα;", ["Στις δέκα", "Στις έντεκα", "Γύρω στις έντεκα και μισή", "Στις δύο και μισή"], 2, "γύρω στις έντεκα και μισή"),
  Q("Τι θα κάνει τελικά ο Γιώργος;", ["Θα ακυρώσει τη σύσκεψη", "Θα ζητήσει από τη Μαίρη να πάει", "Θα στείλει τη γιαγιά", "Θα ζητήσει διάλειμμα στη σύσκεψη για να δει το ποίημα"], 3, "Αν ζητήσω να κάνουμε ένα διάλειμμα στις έντεκα και τέταρτο"),
 ],
 "gloss": {"αγχωμένη": "αγχωμένος — nervous, anxious", "σύσκεψη": "σύσκεψη — meeting", "μεταθέσω": "μεταθέτω — to move, postpone", "καλύψει": "καλύπτω — to cover (for someone)", "χρωστάω": "χρωστάω — to owe", "διάλειμμα": "διάλειμμα — break"}
})

ITEMS.append({
 "id": "l106-int-skinothetria-ntokimanter", "title": "Μια σκηνοθέτρια ντοκιμαντέρ", "title_en": "A documentary director", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε μια πολιτιστική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "m", "Το τελευταίο σας ντοκιμαντέρ ακολουθεί για έναν χρόνο τις γυναίκες ενός ορεινού χωριού. Πώς ξεκίνησε;", "Your latest documentary follows the women of a mountain village for a year. How did it start?"),
  L("Σκηνοθέτρια", "f", "Από μια φωτογραφία. Είδα σε ένα παλιό λεύκωμα δέκα γυναίκες να πλένουν μαλλιά σε μια νεροτριβή, το 1960, και αναρωτήθηκα τι έγιναν οι κόρες τους. Πήγα στο χωριό για μία μέρα και έμεινα δεκατέσσερις μήνες.", "From a photograph. I saw in an old album ten women washing wool at a fulling mill in 1960, and I wondered what had become of their daughters. I went to the village for one day and stayed fourteen months."),
  L("Δημοσιογράφος", "m", "Πώς κερδίσατε την εμπιστοσύνη τους;", "How did you win their trust?"),
  L("Σκηνοθέτρια", "f", "Με τον χρόνο. Τους πρώτους δύο μήνες δεν άνοιξα καν την κάμερα. Βοηθούσα στον τρύγο, στη ζύμη, έπινα πολλούς καφέδες. Όταν τελικά άρχισα να γυρίζω, είχαν συνηθίσει τόσο πολύ την παρουσία μου, που ξεχνούσαν ότι τις κινηματογραφώ.", "With time. For the first two months I didn't even switch the camera on. I helped with the grape harvest, with the dough, I drank a lot of coffees. When I finally started filming, they had got so used to my presence that they forgot I was filming them."),
  L("Δημοσιογράφος", "m", "Ποιο ήταν το πιο δύσκολο κομμάτι;", "What was the hardest part?"),
  L("Σκηνοθέτρια", "f", "Το μοντάζ. Είχα διακόσιες ώρες υλικό για μια ταινία ενενήντα λεπτών. Κάθε σκηνή που έκοβα ήταν σαν να έκοβα έναν άνθρωπο. Πριν από την πρεμιέρα, έκανα μια προβολή στην πλατεία του χωριού. Ήθελα να τη δουν πρώτες εκείνες.", "The editing. I had two hundred hours of footage for a ninety-minute film. Every scene I cut felt like cutting out a person. Before the premiere, I held a screening in the village square. I wanted them to see it first."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η ιδέα για το ντοκιμαντέρ;", ["Από μια φωτογραφία σε ένα παλιό λεύκωμα", "Από ένα βιβλίο", "Από μια πρόταση ενός καναλιού", "Από μια ιστορία της γιαγιάς της"], 0, "Από μια φωτογραφία"),
  Q("Τι έκανε τους πρώτους δύο μήνες;", ["Γύριζε κάθε μέρα", "Έγραφε το σενάριο", "Δεν άνοιξε καν την κάμερα και βοηθούσε στις δουλειές", "Έψαχνε χρηματοδότηση"], 2, "Τους πρώτους δύο μήνες δεν άνοιξα καν την κάμερα"),
  Q("Πού έγινε η πρώτη προβολή;", ["Σε ένα φεστιβάλ", "Στην πλατεία του χωριού", "Στην τηλεόραση", "Σε έναν κινηματογράφο της Αθήνας"], 1, "έκανα μια προβολή στην πλατεία του χωριού"),
 ],
 "gloss": {"λεύκωμα": "λεύκωμα — album", "νεροτριβή": "νεροτριβή — water-powered fulling mill", "εμπιστοσύνη": "εμπιστοσύνη — trust", "τρύγο": "τρύγος — grape harvest", "κινηματογραφώ": "κινηματογραφώ — to film", "μοντάζ": "μοντάζ — editing", "προβολή": "προβολή — screening"}
})

ITEMS.append({
 "id": "l106-rep-archeio-fotografion", "title": "Το ψηφιακό αρχείο φωτογραφιών ενός χωριού", "title_en": "A village's digital photo archive", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια περιφερειακή εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο παλιό σχολείο του χωριού, που έκλεισε πριν από είκοσι χρόνια, ένας σαρωτής δουλεύει ασταμάτητα. Δίπλα του, κουτιά γεμάτα ασπρόμαυρες φωτογραφίες: γάμοι, πανηγύρια, ξενιτεμένοι που ποζάρουν μπροστά σε καράβια.", "In the village's old school, which closed twenty years ago, a scanner works non-stop. Next to it are boxes full of black-and-white photographs: weddings, festivals, emigrants posing in front of ships."),
  L("Υπεύθυνη", "f", "Πριν από δύο χρόνια ζητήσαμε από τους κατοίκους να μας δανείσουν τις οικογενειακές τους φωτογραφίες. Τις σαρώνουμε και τις επιστρέφουμε την ίδια μέρα. Μέχρι τώρα έχουμε συγκεντρώσει πάνω από τέσσερις χιλιάδες. Το πιο δύσκολο είναι να βρούμε ποιοι είναι οι άνθρωποι στις φωτογραφίες.", "Two years ago we asked the residents to lend us their family photographs. We scan them and return them the same day. So far we have gathered more than four thousand. The hardest part is finding out who the people in the photographs are."),
  L("Ρεπόρτερ", "m", "Γι' αυτό, κάθε Σάββατο οι ηλικιωμένοι του χωριού μαζεύονται στο καφενείο και κοιτάζουν τις φωτογραφίες σε μια οθόνη, αναγνωρίζοντας συγγενείς και φίλους. Συχνά ξεκινούν συζητήσεις για το ποιος ήταν ο γαμπρός και ποιος ο κουμπάρος. Το αρχείο είναι ανοιχτό στο διαδίκτυο και πολλοί απόγονοι μεταναστών από την Αμερική και την Αυστραλία έχουν βρει εκεί προγόνους τους.", "That's why every Saturday the village's elderly gather at the café and look at the photographs on a screen, recognising relatives and friends. Discussions often start about who was the groom and who the best man. The archive is open online, and many descendants of emigrants in America and Australia have found their ancestors there."),
 ],
 "questions": [
  Q("Τι γίνεται με τις φωτογραφίες που δανείζουν οι κάτοικοι;", ["Τις κρατούν για μια έκθεση", "Τις σαρώνουν και τις επιστρέφουν την ίδια μέρα", "Τις στέλνουν σε ένα μουσείο", "Τις πουλούν στο διαδίκτυο"], 1, "Τις σαρώνουμε και τις επιστρέφουμε την ίδια μέρα"),
  Q("Ποιο είναι το πιο δύσκολο κομμάτι της δουλειάς;", ["Να βρουν χρήματα", "Να πείσουν τους κατοίκους", "Να βρουν ποιοι είναι οι άνθρωποι στις φωτογραφίες", "Να επισκευάσουν τις φωτογραφίες"], 2, "Το πιο δύσκολο είναι να βρούμε ποιοι είναι οι άνθρωποι στις φωτογραφίες"),
  Q("Ποιοι έχουν βρει προγόνους τους στο αρχείο;", ["Μαθητές του σχολείου", "Τουρίστες", "Ιστορικοί από την Αθήνα", "Απόγονοι μεταναστών από την Αμερική και την Αυστραλία"], 3, "πολλοί απόγονοι μεταναστών από την Αμερική και την Αυστραλία έχουν βρει εκεί προγόνους τους"),
 ],
 "gloss": {"σαρωτής": "σαρωτής — scanner", "ασταμάτητα": "ασταμάτητα — non-stop", "ξενιτεμένοι": "ξενιτεμένος — emigrant, living abroad", "ποζάρουν": "ποζάρω — to pose", "κουμπάρος": "κουμπάρος — best man", "απόγονοι": "απόγονος — descendant", "προγόνους": "πρόγονος — ancestor"}
})

ITEMS.append({
 "id": "l106-rep-laiki-choris-sakoules", "title": "Μια λαϊκή χωρίς πλαστικές σακούλες", "title_en": "A street market without plastic bags", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για το περιβάλλον.",
 "script": [
  L("Ρεπόρτερ", "f", "Είναι Παρασκευή πρωί και στη λαϊκή της γειτονιάς οι πάγκοι είναι γεμάτοι πορτοκάλια, λάχανα και σέλινα. Κάτι όμως λείπει: οι πλαστικές σακούλες. Εδώ και έξι μήνες οι παραγωγοί αυτής της λαϊκής έχουν συμφωνήσει να μη δίνουν καθόλου.", "It's Friday morning and at the neighbourhood street market the stalls are full of oranges, cabbages and celery. But something is missing: plastic bags. For six months now the producers at this market have agreed not to give out any at all."),
  L("Παραγωγός", "m", "Στην αρχή φοβηθήκαμε ότι θα χάσουμε πελάτες. Από το 2018 οι λεπτές σακούλες πληρώνονται, αλλά στη λαϊκή όλοι συνέχιζαν να τις παίρνουν. Ο σύλλογος των παραγωγών αγόρασε πεντακόσιες υφασμάτινες τσάντες και τις μοιράσαμε δωρεάν τον πρώτο μήνα. Όποιος ξεχνάει την τσάντα του, παίρνει τα φρούτα σε χάρτινη σακούλα ή σε κουτί.", "At first we were afraid we'd lose customers. Since 2018 thin bags have had to be paid for, but at the market everyone kept taking them. The producers' association bought five hundred cloth bags and we handed them out free in the first month. Anyone who forgets their bag gets their fruit in a paper bag or a box."),
  L("Ρεπόρτερ", "f", "Οι περισσότεροι πελάτες έχουν συνηθίσει. Μια κυρία μάς δείχνει το καρότσι της: «Το είχα στην αποθήκη από τη μάνα μου», λέει. Ο δήμος σκέφτεται να επεκτείνει το πρόγραμμα και στις άλλες λαϊκές της πόλης από την άνοιξη.", "Most customers have got used to it. A lady shows us her shopping trolley: 'I had it in the storeroom from my mother,' she says. The municipality is thinking of extending the scheme to the town's other markets from the spring."),
 ],
 "questions": [
  Q("Τι έκανε ο σύλλογος των παραγωγών;", ["Αύξησε την τιμή των σακουλών", "Απαγόρευσε τα κουτιά", "Αγόρασε υφασμάτινες τσάντες και τις μοίρασε δωρεάν", "Έβαλε πρόστιμο στους πελάτες"], 2, "αγόρασε πεντακόσιες υφασμάτινες τσάντες και τις μοιράσαμε δωρεάν τον πρώτο μήνα"),
  Q("Τι γίνεται όταν κάποιος ξεχάσει την τσάντα του;", ["Παίρνει τα φρούτα σε χάρτινη σακούλα ή σε κουτί", "Πληρώνει πρόστιμο", "Δεν μπορεί να ψωνίσει", "Παίρνει πλαστική σακούλα"], 0, "παίρνει τα φρούτα σε χάρτινη σακούλα ή σε κουτί"),
  Q("Τι σκέφτεται να κάνει ο δήμος;", ["Να κλείσει τη λαϊκή", "Να επεκτείνει το πρόγραμμα και στις άλλες λαϊκές από την άνοιξη", "Να μοιράσει καρότσια", "Να μεταφέρει τη λαϊκή σε άλλη μέρα"], 1, "Ο δήμος σκέφτεται να επεκτείνει το πρόγραμμα και στις άλλες λαϊκές της πόλης από την άνοιξη"),
 ],
 "gloss": {"πάγκοι": "πάγκος — stall", "σέλινα": "σέλινο — celery", "παραγωγοί": "παραγωγός — producer, grower", "υφασμάτινες": "υφασμάτινος — cloth", "χάρτινη": "χάρτινος — paper", "καρότσι": "καρότσι — shopping trolley", "επεκτείνει": "επεκτείνω — to extend"}
})

ITEMS.append({
 "id": "l106-mono-dotis-organon", "title": "Γιατί έγινα δωρητής οργάνων", "title_en": "Why I became an organ donor", "type": "monologue", "level": "B2",
 "context_el": "Ένας άντρας μιλά σε μια ραδιοφωνική εκπομπή για την υγεία.",
 "script": [
  L("Ηλίας", "m", "Πριν από πέντε χρόνια ο καλύτερός μου φίλος, ο Παύλος, χρειάστηκε μεταμόσχευση νεφρού. Περίμενε τρία χρόνια, κάνοντας αιμοκάθαρση τρεις φορές την εβδομάδα, τέσσερις ώρες κάθε φορά. Δεν μπορούσε να ταξιδέψει, δεν μπορούσε να δουλέψει κανονικά.", "Five years ago my best friend, Pavlos, needed a kidney transplant. He waited three years, having dialysis three times a week, four hours each time. He couldn't travel, he couldn't work normally."),
  L("Ηλίας", "m", "Ένα βράδυ του Σεπτεμβρίου χτύπησε το τηλέφωνό του: είχε βρεθεί νεφρό. Κάποια οικογένεια, την πιο δύσκολη μέρα της ζωής της, είχε πει «ναι». Σήμερα ο Παύλος παίζει μπάσκετ μαζί μου κάθε Κυριακή.", "One September evening his phone rang: a kidney had been found. Some family, on the hardest day of their lives, had said 'yes'. Today Pavlos plays basketball with me every Sunday."),
  L("Ηλίας", "m", "Την επόμενη εβδομάδα δήλωσα κι εγώ ότι θέλω να γίνω δωρητής, και το συζήτησα με τη γυναίκα μου και τους γονείς μου. Αυτό είναι, νομίζω, το πιο σημαντικό: να ξέρει η οικογένειά σου τι θέλεις, ώστε να μην πρέπει να αποφασίσει μόνη της σε μια τέτοια στιγμή. Δεν είναι ευχάριστη κουβέντα, αλλά κράτησε μόνο δέκα λεπτά.", "The following week I too registered that I want to become a donor, and I discussed it with my wife and my parents. That, I think, is the most important thing: for your family to know what you want, so that they don't have to decide on their own at such a moment. It isn't a pleasant conversation, but it lasted only ten minutes."),
 ],
 "questions": [
  Q("Πόσο περίμενε ο Παύλος για μεταμόσχευση;", ["Τρεις μήνες", "Πέντε χρόνια", "Έναν χρόνο", "Τρία χρόνια"], 3, "Περίμενε τρία χρόνια"),
  Q("Τι κάνει σήμερα ο Παύλος;", ["Παίζει μπάσκετ με τον Ηλία κάθε Κυριακή", "Κάνει ακόμα αιμοκάθαρση", "Δουλεύει σε νοσοκομείο", "Ταξιδεύει στο εξωτερικό"], 0, "Σήμερα ο Παύλος παίζει μπάσκετ μαζί μου κάθε Κυριακή"),
  Q("Τι θεωρεί ο Ηλίας το πιο σημαντικό;", ["Να γραφτεί κανείς όσο πιο νέος γίνεται", "Να ξέρει η οικογένειά σου τι θέλεις", "Να μιλήσει με γιατρό", "Να μην το πει σε κανέναν"], 1, "να ξέρει η οικογένειά σου τι θέλεις"),
 ],
 "gloss": {"μεταμόσχευση": "μεταμόσχευση — transplant", "νεφρού": "νεφρό — kidney", "αιμοκάθαρση": "αιμοκάθαρση — dialysis", "δωρητής": "δωρητής οργάνων — organ donor", "κουβέντα": "κουβέντα — conversation"}
})

ITEMS.append({
 "id": "l106-mono-skylos-odigos", "title": "Η ζωή μου με τη σκυλίτσα-οδηγό", "title_en": "My life with my guide dog", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα με πρόβλημα όρασης μιλά σε μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Κατερίνα", "f", "Έχασα την όρασή μου στα τριάντα δύο, από μια ασθένεια του αμφιβληστροειδούς. Για χρόνια κυκλοφορούσα με το λευκό μπαστούνι. Ήταν ασφαλές, αλλά αργό, και πάντα φοβόμουν τα πεζοδρόμια με τα παρκαρισμένα μηχανάκια.", "I lost my sight at thirty-two, from a disease of the retina. For years I got around with the white cane. It was safe, but slow, and I was always afraid of pavements with parked motorbikes."),
  L("Κατερίνα", "f", "Πριν από τρία χρόνια ήρθε στη ζωή μου η Λούνα, ένα λαμπραντόρ που είχε εκπαιδευτεί για σχεδόν δύο χρόνια. Περάσαμε έναν μήνα μαζί σε μια σχολή, για να μάθουμε να δουλεύουμε σαν ομάδα. Η Λούνα σταματά στα κράσπεδα, με οδηγεί γύρω από τα εμπόδια και βρίσκει την πόρτα του λεωφορείου.", "Three years ago Luna came into my life, a Labrador who had been trained for almost two years. We spent a month together at a school, to learn to work as a team. Luna stops at kerbs, guides me around obstacles and finds the bus door."),
  L("Κατερίνα", "f", "Ο νόμος μού επιτρέπει να μπαίνω μαζί της σε καταστήματα, ταξί και εστιατόρια, αλλά ακόμη συμβαίνει να μου αρνηθούν. Και μια παράκληση: όταν βλέπετε τη Λούνα με το χαλινάρι της, μην τη χαϊδεύετε και μην της μιλάτε. Δουλεύει. Όταν της το βγάζω, το βράδυ, είναι ένα σκυλί σαν όλα τα άλλα, που λατρεύει τα χάδια.", "The law allows me to go into shops, taxis and restaurants with her, but it still happens that I'm refused. And a request: when you see Luna in her harness, don't stroke her and don't talk to her. She's working. When I take it off, in the evening, she's a dog like any other, who adores being petted."),
 ],
 "questions": [
  Q("Πώς κυκλοφορούσε η Κατερίνα πριν από τη Λούνα;", ["Με τη βοήθεια μιας φίλης", "Μόνο με ταξί", "Με το λευκό μπαστούνι", "Δεν έβγαινε από το σπίτι"], 2, "κυκλοφορούσα με το λευκό μπαστούνι"),
  Q("Τι έκαναν η Κατερίνα και η Λούνα σε μια σχολή;", ["Πέρασαν έναν μήνα μαζί για να μάθουν να δουλεύουν σαν ομάδα", "Η Λούνα εκπαιδεύτηκε δύο χρόνια μαζί της", "Έμαθαν να ταξιδεύουν με αεροπλάνο", "Γνώρισαν άλλους σκύλους"], 0, "Περάσαμε έναν μήνα μαζί σε μια σχολή, για να μάθουμε να δουλεύουμε σαν ομάδα"),
  Q("Τι ζητά η Κατερίνα από τους περαστικούς;", ["Να τη βοηθούν να περάσει τον δρόμο", "Να μην παρκάρουν στα πεζοδρόμια", "Να δίνουν λιχουδιές στη Λούνα", "Να μη χαϊδεύουν και να μη μιλούν στη Λούνα όταν φορά το χαλινάρι"], 3, "όταν βλέπετε τη Λούνα με το χαλινάρι της, μην τη χαϊδεύετε και μην της μιλάτε"),
 ],
 "gloss": {"όρασή": "όραση — sight", "αμφιβληστροειδούς": "αμφιβληστροειδής — retina", "μπαστούνι": "μπαστούνι — cane, stick", "εκπαιδευτεί": "εκπαιδεύομαι — to be trained", "κράσπεδα": "κράσπεδο — kerb", "εμπόδια": "εμπόδιο — obstacle", "χαλινάρι": "χαλινάρι — harness", "χάδια": "χάδι — stroke, caress"}
})

ITEMS.append({
 "id": "l106-c1-den-xero", "title": "Γιατί μας είναι τόσο δύσκολο να πούμε «δεν ξέρω»;", "title_en": "Why is it so hard to say 'I don't know'?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια γνωστική ψυχολόγο σε μια εκπομπή εκλαΐκευσης της επιστήμης.",
 "script": [
  L("Ψυχολόγος", "f", "Κάντε το εξής πείραμα: ρωτήστε έναν φίλο σας αν ξέρει πώς λειτουργεί ένα φερμουάρ. Οι περισσότεροι απαντούν «ναι» χωρίς δισταγμό. Ζητήστε τους, όμως, να το εξηγήσουν βήμα βήμα, και θα δείτε την αυτοπεποίθησή τους να εξαφανίζεται. Οι ψυχολόγοι το ονομάζουν «ψευδαίσθηση της επεξηγηματικής βαθύτητας»: νομίζουμε ότι καταλαβαίνουμε τον κόσμο πολύ καλύτερα απ' ό,τι στην πραγματικότητα.", "Try the following experiment: ask a friend whether they know how a zip works. Most people answer 'yes' without hesitation. Ask them, though, to explain it step by step, and you'll see their confidence vanish. Psychologists call it 'the illusion of explanatory depth': we think we understand the world much better than we actually do."),
  L("Ψυχολόγος", "f", "Η δυσκολία να παραδεχτούμε την άγνοιά μας ξεκινά νωρίς. Σε ορισμένες μελέτες, όταν έκαναν σε μικρά παιδιά ερωτήσεις χωρίς νόημα, του τύπου «Είναι το κόκκινο πιο βαρύ από το Σάββατο;», πολλά απαντούσαν «ναι» ή «όχι» αντί για «δεν ξέρω». Μαθαίνουμε από νωρίς ότι οι ερωτήσεις έχουν σωστές απαντήσεις και ότι η σιωπή μοιάζει με αποτυχία.", "The difficulty of admitting our ignorance begins early. In some studies, when young children were asked meaningless questions, such as 'Is red heavier than Saturday?', many answered 'yes' or 'no' instead of 'I don't know'. We learn early on that questions have right answers and that silence looks like failure."),
  L("Ψυχολόγος", "f", "Στους ενήλικες προστίθεται και ο κοινωνικός φόβος: φοβόμαστε ότι, αν πούμε «δεν ξέρω», θα φανούμε ανίκανοι. Είναι ειρωνικό, γιατί οι έρευνες δείχνουν ότι συχνά συμβαίνει το αντίθετο. Ένας γιατρός ή ένας δάσκαλος που λέει «δεν είμαι σίγουρος, θα το ψάξω» κερδίζει συχνά περισσότερη εμπιστοσύνη, γιατί όλα τα άλλα που λέει γίνονται πιο πιστευτά. Το «δεν ξέρω» δεν είναι το τέλος της σκέψης. Είναι η αρχή της.", "Adults add social fear as well: we fear that if we say 'I don't know', we'll look incompetent. It's ironic, because research shows that the opposite often happens. A doctor or a teacher who says 'I'm not sure, I'll look it up' often gains more trust, because everything else they say becomes more believable. 'I don't know' is not the end of thinking. It is the beginning."),
 ],
 "questions": [
  Q("Τι δείχνει το πείραμα με το φερμουάρ;", ["Ότι οι περισσότεροι ξέρουν πώς λειτουργεί", "Ότι νομίζουμε ότι καταλαβαίνουμε τα πράγματα καλύτερα απ' ό,τι στην πραγματικότητα", "Ότι τα φερμουάρ είναι πολύπλοκα", "Ότι οι φίλοι μας δεν μας λένε την αλήθεια"], 1, "νομίζουμε ότι καταλαβαίνουμε τον κόσμο πολύ καλύτερα απ' ό,τι στην πραγματικότητα"),
  Q("Πώς απαντούσαν πολλά μικρά παιδιά σε ερωτήσεις χωρίς νόημα;", ["Έλεγαν «δεν ξέρω»", "Γελούσαν", "Απαντούσαν «ναι» ή «όχι»", "Δεν απαντούσαν καθόλου"], 2, "πολλά απαντούσαν «ναι» ή «όχι» αντί για «δεν ξέρω»"),
  Q("Τι φοβούνται οι ενήλικες, σύμφωνα με την ψυχολόγο;", ["Ότι θα φανούν ανίκανοι", "Ότι θα κάνουν λάθος ερώτηση", "Ότι θα κουράσουν τους άλλους", "Ότι θα χάσουν χρόνο"], 0, "φοβόμαστε ότι, αν πούμε «δεν ξέρω», θα φανούμε ανίκανοι"),
  Q("Γιατί ένας γιατρός που παραδέχεται ότι δεν είναι σίγουρος κερδίζει συχνά περισσότερη εμπιστοσύνη;", ["Γιατί φαίνεται πιο ταπεινός", "Γιατί οι ασθενείς προτιμούν τους νέους γιατρούς", "Γιατί δίνει περισσότερο χρόνο στους ασθενείς", "Γιατί όλα τα άλλα που λέει γίνονται πιο πιστευτά"], 3, "όλα τα άλλα που λέει γίνονται πιο πιστευτά"),
 ],
 "gloss": {"φερμουάρ": "φερμουάρ — zip", "δισταγμό": "δισταγμός — hesitation", "ψευδαίσθηση": "ψευδαίσθηση — illusion", "επεξηγηματικής": "επεξηγηματικός — explanatory", "βαθύτητας": "βαθύτητα — depth", "άγνοιά": "άγνοια — ignorance", "ανίκανοι": "ανίκανος — incompetent", "ειρωνικό": "ειρωνικός — ironic", "πιστευτά": "πιστευτός — believable"}
})

ITEMS.append({
 "id": "l106-c1-poses-lexeis", "title": "Πόσες λέξεις χρειαζόμαστε για να μιλάμε μια γλώσσα;", "title_en": "How many words do we need to speak a language?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν γλωσσολόγο σε μια εκπομπή για την εκμάθηση γλωσσών.",
 "script": [
  L("Δημοσιογράφος", "f", "Πόσες λέξεις ξέρει ένας μέσος ενήλικας στη μητρική του γλώσσα;", "How many words does an average adult know in their native language?"),
  L("Γλωσσολόγος", "m", "Εξαρτάται από το πώς μετράμε. Αν θεωρήσουμε μία «οικογένεια» το «γράφω», το «γραφή» και το «συγγραφέας», οι εκτιμήσεις για ενήλικες με καλή μόρφωση κυμαίνονται συνήθως γύρω στις είκοσι χιλιάδες οικογένειες λέξεων, αν και οι αριθμοί διαφέρουν πολύ από μελέτη σε μελέτη. Κανείς, όμως, δεν χρειάζεται τόσες για να επικοινωνήσει σε μια ξένη γλώσσα.", "It depends on how we count. If we treat 'write', 'writing' and 'writer' as one 'family', estimates for well-educated adults usually range around twenty thousand word families, although the figures vary a great deal from study to study. Nobody, however, needs that many to communicate in a foreign language."),
  L("Δημοσιογράφος", "f", "Πόσες αρκούν, λοιπόν;", "How many are enough, then?"),
  L("Γλωσσολόγος", "m", "Οι έρευνες για την κάλυψη κειμένων δίνουν μια ενδεικτική απάντηση. Οι δύο με τρεις χιλιάδες πιο συχνές οικογένειες καλύπτουν το μεγαλύτερο μέρος μιας καθημερινής συζήτησης. Για να διαβάζει κανείς άνετα ένα μυθιστόρημα ή μια εφημερίδα, όμως, χρειάζεται να καταλαβαίνει σχεδόν όλες τις λέξεις, γύρω στο ενενήντα οχτώ τοις εκατό, και αυτό απαιτεί, κατά ορισμένους υπολογισμούς, οχτώ με εννιά χιλιάδες οικογένειες. Αν δεν καταλαβαίνεις μία λέξη σε κάθε γραμμή, το διάβασμα γίνεται κουραστικό.", "Research on text coverage gives an indicative answer. The two to three thousand most frequent families cover most of an everyday conversation. To read a novel or a newspaper comfortably, however, you need to understand almost all the words, around ninety-eight per cent, and that requires, by some calculations, eight to nine thousand families. If you don't understand one word in every line, reading becomes tiring."),
  L("Δημοσιογράφος", "f", "Και πώς τις μαθαίνει κανείς;", "And how does one learn them?"),
  L("Γλωσσολόγος", "m", "Με δύο τρόπους που συμπληρώνουν ο ένας τον άλλον. Οι πιο συχνές λέξεις αξίζει να μελετηθούν συστηματικά, με επαναλήψεις σε αυξανόμενα διαστήματα. Οι σπανιότερες μαθαίνονται κυρίως μέσα από πολύ διάβασμα, γιατί τις συναντάμε ξανά και ξανά σε διαφορετικά συμφραζόμενα. Και κάτι ακόμα: το να αναγνωρίζεις μια λέξη δεν σημαίνει ότι μπορείς να τη χρησιμοποιήσεις. Η παραγωγή χρειάζεται τη δική της εξάσκηση.", "In two ways that complement each other. The most frequent words are worth studying systematically, with reviews at increasing intervals. The rarer ones are learnt mainly through a lot of reading, because we meet them again and again in different contexts. And one more thing: being able to recognise a word doesn't mean you can use it. Production needs its own practice."),
 ],
 "questions": [
  Q("Τι λέει ο γλωσσολόγος για τον αριθμό λέξεων που ξέρει ένας ενήλικας με καλή μόρφωση;", ["Ότι είναι ακριβώς είκοσι χιλιάδες λέξεις", "Ότι οι εκτιμήσεις είναι γύρω στις είκοσι χιλιάδες οικογένειες, αλλά διαφέρουν πολύ", "Ότι είναι λιγότερες από πέντε χιλιάδες", "Ότι κανείς δεν έχει προσπαθήσει να τις μετρήσει"], 1, "οι εκτιμήσεις για ενήλικες με καλή μόρφωση κυμαίνονται συνήθως γύρω στις είκοσι χιλιάδες οικογένειες λέξεων, αν και οι αριθμοί διαφέρουν πολύ από μελέτη σε μελέτη"),
  Q("Τι καλύπτουν οι δύο με τρεις χιλιάδες πιο συχνές οικογένειες;", ["Το μεγαλύτερο μέρος μιας καθημερινής συζήτησης", "Ένα ολόκληρο μυθιστόρημα", "Τις επιστημονικές ομιλίες", "Μόνο τις ειδήσεις"], 0, "καλύπτουν το μεγαλύτερο μέρος μιας καθημερινής συζήτησης"),
  Q("Γιατί χρειάζονται περισσότερες λέξεις για να διαβάζει κανείς άνετα;", ["Γιατί τα βιβλία έχουν πιο δύσκολη γραμματική", "Γιατί οι εφημερίδες χρησιμοποιούν ξένες λέξεις", "Γιατί χρειάζεται να καταλαβαίνει σχεδόν όλες τις λέξεις, γύρω στο ενενήντα οχτώ τοις εκατό", "Γιατί η ανάγνωση είναι πιο γρήγορη από την ομιλία"], 2, "χρειάζεται να καταλαβαίνει σχεδόν όλες τις λέξεις, γύρω στο ενενήντα οχτώ τοις εκατό"),
  Q("Τι λέει για την αναγνώριση και την παραγωγή;", ["Ότι είναι το ίδιο πράγμα", "Ότι η παραγωγή μαθαίνεται μόνο με διάβασμα", "Ότι η αναγνώριση είναι πιο δύσκολη", "Ότι το να αναγνωρίζεις μια λέξη δεν σημαίνει ότι μπορείς να τη χρησιμοποιήσεις"], 3, "το να αναγνωρίζεις μια λέξη δεν σημαίνει ότι μπορείς να τη χρησιμοποιήσεις"),
 ],
 "gloss": {"μητρική": "μητρική γλώσσα — native language", "μόρφωση": "μόρφωση — education", "κυμαίνονται": "κυμαίνομαι — to range", "κάλυψη": "κάλυψη — coverage", "ενδεικτική": "ενδεικτικός — indicative", "αυξανόμενα": "αυξανόμενος — increasing", "συμφραζόμενα": "συμφραζόμενα — context", "παραγωγή": "παραγωγή — production"}
})

rnd = random.Random(106)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-106.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
