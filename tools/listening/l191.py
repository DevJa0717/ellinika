# Source for library/listening/listening-191.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l191.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l191-ann-christougenniatiko-treno-me-atmomichani", "title": "Χριστουγεννιάτικο τρένο με ατμομηχανή", "title_en": "A Christmas steam train", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση ενός συλλόγου φίλων του σιδηροδρόμου στο ραδιόφωνο.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο Σύλλογος Φίλων του Σιδηροδρόμου ανακοινώνει ότι και φέτος, τις Κυριακές 15 και 22 Δεκεμβρίου, η παλιά ατμομηχανή του συλλόγου θα κάνει το χριστουγεννιάτικο δρομολόγιο από την πόλη ως το χωριό στους πρόποδες του βουνού. Η διαδρομή κρατάει μιάμιση ώρα και περνάει από δύο πέτρινες γέφυρες και ένα τούνελ.", "The Railway Friends' Society announces that again this year, on Sundays 15 and 22 December, the society's old steam locomotive will run the Christmas service from the town to the village at the foot of the mountain. The journey takes an hour and a half and passes over two stone bridges and through a tunnel."),
  L("Εκφωνήτρια", "f", "Στο τρένο θα υπάρχουν μουσικοί με κάλαντα, και τα παιδιά θα πάρουν από ένα σακουλάκι με κουραμπιέδες. Στο χωριό οι επιβάτες θα έχουν δύο ώρες για να επισκεφθούν τη χριστουγεννιάτικη αγορά, πριν από την επιστροφή.", "On the train there will be musicians playing carols, and the children will each get a little bag of kourabiedes. In the village passengers will have two hours to visit the Christmas market before the return journey."),
  L("Εκφωνήτρια", "f", "Τα εισιτήρια πωλούνται μόνο στο εκδοτήριο του σταθμού, γιατί ο σύλλογος θέλει να αποφύγει τη μεταπώληση στο διαδίκτυο. Παρακαλούνται οι επιβάτες να μην ανοίγουν τα παράθυρα στο τούνελ, γιατί ο καπνός της μηχανής μπαίνει στα βαγόνια, και να φορούν ρούχα που δεν πειράζει αν μαυρίσουν λίγο.", "Tickets are sold only at the station ticket office, because the society wants to avoid resale online. Passengers are asked not to open the windows in the tunnel, because smoke from the engine gets into the carriages, and to wear clothes that won't matter if they get a little black."),
 ],
 "questions": [
  Q("Πόσο κρατάει η διαδρομή ως το χωριό;", ["Μισή ώρα", "Μιάμιση ώρα", "Δύο ώρες", "Τρεις ώρες"], 1, "Η διαδρομή κρατάει μιάμιση ώρα"),
  Q("Γιατί τα εισιτήρια πωλούνται μόνο στο εκδοτήριο;", ["Γιατί ο σύλλογος δεν έχει ιστοσελίδα", "Γιατί είναι δωρεάν για τα παιδιά", "Για να αποφευχθεί η μεταπώληση στο διαδίκτυο", "Γιατί οι θέσεις είναι λίγες"], 2, "γιατί ο σύλλογος θέλει να αποφύγει τη μεταπώληση στο διαδίκτυο"),
  Q("Τι ζητείται από τους επιβάτες στο τούνελ;", ["Να μην ανοίγουν τα παράθυρα", "Να μένουν στις θέσεις τους", "Να κλείνουν τα φώτα", "Να μη φωτογραφίζουν"], 0, "να μην ανοίγουν τα παράθυρα στο τούνελ"),
 ],
 "gloss": {"ατμομηχανή": "ατμομηχανή — steam locomotive", "πρόποδες": "πρόποδες — foot (of a mountain)", "κάλαντα": "κάλαντα — carols", "εκδοτήριο": "εκδοτήριο — ticket office", "μεταπώληση": "μεταπώληση — resale", "μαυρίσουν": "μαυρίζω — to turn black"},
})

ITEMS.append({
 "id": "l191-int-odigos-ekchionistikou", "title": "Η οδηγός του εκχιονιστικού", "title_en": "The snowplough driver", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γυναίκα που οδηγεί εκχιονιστικό σε ένα ορεινό δήμο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς είναι μια βάρδια σας όταν χιονίζει;", "What is one of your shifts like when it snows?"),
  L("Οδηγός", "f", "Αν η πρόγνωση λέει χιόνι, είμαι στο αμαξοστάσιο από τις τρεις τα ξημερώματα. Ρίχνουμε πρώτα αλάτι στους κεντρικούς δρόμους και μετά, όταν το χιόνι ξεπεράσει τους πέντε πόντους, βγαίνουμε με τη λεπίδα. Προτεραιότητα έχουν ο δρόμος για το κέντρο υγείας και οι στάσεις των σχολικών.", "If the forecast says snow, I'm at the depot from three in the morning. First we spread salt on the main roads, and then, when the snow goes over five centimetres, we go out with the blade. Priority goes to the road to the health centre and the school-bus stops."),
  L("Δημοσιογράφος", "m", "Είστε η μόνη γυναίκα στην υπηρεσία;", "Are you the only woman in the service?"),
  L("Οδηγός", "f", "Ναι, και στην αρχή κάποιοι στα χωριά έβγαιναν στα παράθυρα να δουν ποιος οδηγεί. Ένας παππούς με σταμάτησε μια φορά και μου είπε ότι σε εβδομήντα χρόνια δεν είχε δει γυναίκα να καθαρίζει τον δρόμο. Μετά μου έφερε ένα ποτήρι τσίπουρο, που φυσικά δεν το ήπια, γιατί οδηγούσα.", "Yes, and at first some people in the villages came to their windows to see who was driving. An old man stopped me once and told me that in seventy years he had never seen a woman clearing the road. Then he brought me a glass of tsipouro, which of course I didn't drink, because I was driving."),
  L("Δημοσιογράφος", "m", "Τι σας θυμώνει περισσότερο;", "What makes you angriest?"),
  L("Οδηγός", "f", "Τα αυτοκίνητα που παρκάρουν στη μέση του δρόμου ή χωρίς αλυσίδες κολλάνε στις στροφές. Τότε το εκχιονιστικό δεν μπορεί να περάσει, και ένα ολόκληρο χωριό μένει αποκλεισμένο. Λίγη υπομονή στο σπίτι σώζει πολλές ώρες δουλειάς.", "Cars that park in the middle of the road or get stuck on the bends without chains. Then the snowplough can't get through, and a whole village is cut off. A little patience at home saves many hours of work."),
 ],
 "questions": [
  Q("Ποιος δρόμος καθαρίζεται πρώτος;", ["Ο δρόμος για το κέντρο υγείας", "Ο δρόμος για το χιονοδρομικό", "Ο δρόμος προς την πόλη", "Ο δρόμος του δημαρχείου"], 0, "Προτεραιότητα έχουν ο δρόμος για το κέντρο υγείας"),
  Q("Γιατί δεν ήπιε το τσίπουρο που της πρόσφερε ο παππούς;", ["Γιατί δεν της αρέσει", "Γιατί ήταν πολύ νωρίς", "Γιατί οδηγούσε", "Γιατί το απαγορεύει ο δήμος"], 2, "που φυσικά δεν το ήπια, γιατί οδηγούσα"),
  Q("Τι θυμώνει περισσότερο την οδηγό;", ["Οι οδηγοί που κορνάρουν", "Τα αυτοκίνητα που μπλοκάρουν τον δρόμο", "Οι γείτονες που παραπονιούνται", "Το κρύο"], 1, "Τα αυτοκίνητα που παρκάρουν στη μέση του δρόμου ή χωρίς αλυσίδες κολλάνε στις στροφές"),
 ],
 "gloss": {"εκχιονιστικό": "εκχιονιστικό — snowplough", "αμαξοστάσιο": "αμαξοστάσιο — depot", "λεπίδα": "λεπίδα — blade", "Προτεραιότητα": "προτεραιότητα — priority", "αλυσίδες": "αλυσίδα — (snow) chain", "αποκλεισμένο": "αποκλεισμένος — cut off"},
})

ITEMS.append({
 "id": "l191-vm-paraggelia-apo-to-ichthyopoleio", "title": "Η παραγγελία σας από το ιχθυοπωλείο", "title_en": "Your order from the fishmonger's", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε παραγγείλει ψάρια για το γιορτινό τραπέζι. Ακούτε ένα μήνυμα από τον ιχθυοπώλη.",
 "script": [
  L("Ιχθυοπώλης", "m", "Καλημέρα σας, ο Θοδωρής από το ιχθυοπωλείο της αγοράς. Σας παίρνω για την παραγγελία σας για την Παραμονή. Τον μπακαλιάρο τον έχω, φρέσκο, και θα σας τον κόψω φιλέτα, όπως ζητήσατε. Με τις γαρίδες όμως έχουμε πρόβλημα: λόγω του αέρα τα καΐκια δεν βγήκαν τρεις μέρες.", "Good morning, it's Thodoris from the fishmonger's at the market. I'm calling about your order for Christmas Eve. I've got the cod, fresh, and I'll cut it into fillets for you, as you asked. But we have a problem with the prawns: because of the wind the boats haven't been out for three days."),
  L("Ιχθυοπώλης", "m", "Μπορώ να σας δώσω κατεψυγμένες, αλλά καλής ποιότητας, σε χαμηλότερη τιμή. Ή, αν θέλετε κάτι φρέσκο, έχω σήμερα πολύ ωραία καλαμάρια, που ταιριάζουν κι αυτά με το τραπέζι σας.", "I can give you frozen ones, but good quality, at a lower price. Or, if you want something fresh, today I have some lovely squid, which also go well with your meal."),
  L("Ιχθυοπώλης", "m", "Επειδή την Παραμονή έχουμε πολύ κόσμο, σας προτείνω να περάσετε να τα πάρετε την προηγούμενη μέρα, μετά τις πέντε. Θα τα έχω έτοιμα σε πάγο. Και φέρτε, αν μπορείτε, μια δική σας τσάντα-ψυγείο, γιατί μας τελείωσαν οι φελιζόλ.", "Because we're very busy on Christmas Eve, I suggest you come and collect them the day before, after five. I'll have them ready on ice. And bring a cool bag of your own if you can, because we've run out of polystyrene boxes."),
 ],
 "questions": [
  Q("Γιατί δεν υπάρχουν φρέσκες γαρίδες;", ["Γιατί τις αγόρασε άλλος πελάτης", "Γιατί λόγω του αέρα τα καΐκια δεν βγήκαν", "Γιατί δεν είναι εποχή τους", "Γιατί είναι πολύ ακριβές"], 1, "λόγω του αέρα τα καΐκια δεν βγήκαν τρεις μέρες"),
  Q("Πότε προτείνει ο ιχθυοπώλης να παραλάβετε την παραγγελία;", ["Την Παραμονή το πρωί", "Μετά τις γιορτές", "Την προηγούμενη μέρα, μετά τις πέντε", "Σήμερα το απόγευμα"], 2, "να περάσετε να τα πάρετε την προηγούμενη μέρα, μετά τις πέντε"),
  Q("Τι σας ζητά να φέρετε;", ["Μια τσάντα-ψυγείο", "Μετρητά", "Το χαρτί της παραγγελίας", "Πάγο"], 0, "φέρτε, αν μπορείτε, μια δική σας τσάντα-ψυγείο"),
 ],
 "gloss": {"ιχθυοπωλείο": "ιχθυοπωλείο — fishmonger's", "ιχθυοπώλη": "ιχθυοπώλης — fishmonger", "μπακαλιάρο": "μπακαλιάρος — cod", "φιλέτα": "φιλέτο — fillet", "κατεψυγμένες": "κατεψυγμένος — frozen", "φελιζόλ": "φελιζόλ — polystyrene (box)"},
})

ITEMS.append({
 "id": "l191-mono-ematha-ntaouli", "title": "Έμαθα να παίζω νταούλι", "title_en": "I learned to play the daouli", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλάει σε ένα ραδιοφωνικό πρόγραμμα για ένα παραδοσιακό όργανο που έμαθε.",
 "script": [
  L("Δέσποινα", "f", "Στο χωριό της μητέρας μου, στη Μακεδονία, σε κάθε πανηγύρι υπήρχαν δύο ζουρνάδες και ένα νταούλι. Όταν ήμουν μικρή, στεκόμουν δίπλα στον νταουλιέρη και ένιωθα τον ήχο στο στήθος μου, σαν δεύτερη καρδιά. Αλλά τότε κανείς δεν φανταζόταν ότι ένα κορίτσι θα μπορούσε να παίξει νταούλι.", "In my mother's village, in Macedonia, at every festival there were two zournas and a daouli. When I was little, I would stand next to the drummer and feel the sound in my chest, like a second heart. But back then nobody imagined that a girl could play the daouli."),
  L("Δέσποινα", "f", "Στα τριάντα πέντε μου βρήκα έναν δάσκαλο σε ένα πολιτιστικό σύλλογο στη Θεσσαλονίκη. Το νταούλι παίζεται με δύο ξύλα: ένα χοντρό για τα βαριά χτυπήματα και μια λεπτή βέργα για τα ελαφριά. Ο δυσκολότερος ρυθμός για μένα ήταν ο εννιάσημος, που μετράει εννιά και όχι οχτώ. Για μήνες μετρούσα φωναχτά ακόμα και όταν έπλενα τα πιάτα.", "At thirty-five I found a teacher at a cultural association in Thessaloniki. The daouli is played with two sticks: a thick one for the heavy beats and a thin switch for the light ones. The hardest rhythm for me was the nine-beat one, which counts nine and not eight. For months I counted aloud even while I was washing the dishes."),
  L("Δέσποινα", "f", "Πέρσι το καλοκαίρι έπαιξα για πρώτη φορά στο πανηγύρι του χωριού της μητέρας μου. Κάποιοι ηλικιωμένοι στην αρχή κοίταζαν με απορία. Μετά από δέκα λεπτά όμως είχαν πιαστεί όλοι στον χορό, και μια γιαγιά ήρθε στο τέλος και μου φίλησε τα χέρια.", "Last summer I played for the first time at the festival in my mother's village. Some of the older people looked puzzled at first. But after ten minutes they had all joined hands in the dance, and at the end a grandmother came and kissed my hands."),
 ],
 "questions": [
  Q("Πώς ένιωθε η Δέσποινα τον ήχο του νταουλιού όταν ήταν μικρή;", ["Την τρόμαζε", "Τον ένιωθε στο στήθος της σαν δεύτερη καρδιά", "Της προκαλούσε πονοκέφαλο", "Δεν της άρεσε καθόλου"], 1, "ένιωθα τον ήχο στο στήθος μου, σαν δεύτερη καρδιά"),
  Q("Ποιος ρυθμός τη δυσκόλεψε περισσότερο;", ["Ο εννιάσημος", "Ο οχτάσημος", "Ο αργός συρτός", "Ο τσάμικος"], 0, "Ο δυσκολότερος ρυθμός για μένα ήταν ο εννιάσημος"),
  Q("Τι έγινε όταν έπαιξε στο πανηγύρι;", ["Οι ηλικιωμένοι έφυγαν", "Τη σταμάτησε ο πρόεδρος του χωριού", "Μετά από δέκα λεπτά όλοι χόρευαν", "Έπαιξε μόνο ένα κομμάτι"], 2, "Μετά από δέκα λεπτά όμως είχαν πιαστεί όλοι στον χορό"),
 ],
 "gloss": {"νταούλι": "νταούλι — large double-headed drum", "ζουρνάδες": "ζουρνάς — zourna (folk shawm)", "νταουλιέρη": "νταουλιέρης — daouli player", "βέργα": "βέργα — switch, thin stick", "εννιάσημος": "εννιάσημος — (rhythm) in nine beats", "απορία": "απορία — puzzlement"},
})

ITEMS.append({
 "id": "l191-dia-poios-mageirevei-ti-ta-christougenna", "title": "Ποιος μαγειρεύει τι τα Χριστούγεννα;", "title_en": "Who's cooking what at Christmas?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέρφια μοιράζουν τις δουλειές για το χριστουγεννιάτικο τραπέζι της οικογένειας.",
 "script": [
  L("Νίκος", "m", "Φέτος η μαμά είπε ότι δεν θέλει να μαγειρέψει τίποτα. Θέλει να κάτσει στο τραπέζι σαν καλεσμένη, για πρώτη φορά εδώ και τριάντα χρόνια.", "This year Mum said she doesn't want to cook anything. She wants to sit at the table like a guest, for the first time in thirty years."),
  L("Άννα", "f", "Το αξίζει. Ας μοιράσουμε τότε τις δουλειές. Εγώ μπορώ να κάνω τη γαλοπούλα. Την έχω δει τόσες φορές, ξέρω απ' έξω τη γέμιση με το κάστανο και το κουκουνάρι.", "She's earned it. Let's divide up the jobs, then. I can do the turkey. I've watched her so many times; I know the stuffing with the chestnuts and pine nuts by heart."),
  L("Νίκος", "m", "Εντάξει, αλλά η γαλοπούλα θέλει τέσσερις ώρες στον φούρνο, και ο δικός σου φούρνος είναι μικρός. Γιατί δεν τη φτιάχνεις στο σπίτι της μαμάς από το πρωί; Εγώ αναλαμβάνω τις σαλάτες και τα ορεκτικά, που μπορώ να τα φέρω έτοιμα.", "OK, but the turkey needs four hours in the oven, and your oven is small. Why don't you make it at Mum's house from the morning? I'll take care of the salads and starters, which I can bring ready-made."),
  L("Άννα", "f", "Καλή ιδέα. Και τα γλυκά; Τα μελομακάρονα της μαμάς δεν συγκρίνονται με τίποτα.", "Good idea. And the sweets? Mum's melomakarona are beyond compare."),
  L("Νίκος", "m", "Τα παίρνουμε από τον φούρνο της γειτονιάς. Αν προσπαθήσω να τα φτιάξω εγώ, η μαμά θα σηκωθεί από την καρέκλα να με διορθώσει, και τότε χάλασε όλο το σχέδιο.", "We'll get them from the neighbourhood bakery. If I try to make them myself, Mum will get up from her chair to correct me, and then the whole plan is ruined."),
  L("Άννα", "f", "Έχεις δίκιο. Και να θυμηθούμε να της κρύψουμε την ποδιά, αλλιώς θα τη βρούμε στην κουζίνα πριν καν βγάλουμε τα παλτά μας.", "You're right. And we must remember to hide her apron, otherwise we'll find her in the kitchen before we've even taken our coats off."),
 ],
 "questions": [
  Q("Γιατί δεν θέλει η μητέρα να μαγειρέψει φέτος;", ["Γιατί είναι άρρωστη", "Γιατί θέλει να κάτσει στο τραπέζι σαν καλεσμένη", "Γιατί θα λείπει ταξίδι", "Γιατί χάλασε ο φούρνος της"], 1, "Θέλει να κάτσει στο τραπέζι σαν καλεσμένη"),
  Q("Γιατί προτείνει ο Νίκος να ψηθεί η γαλοπούλα στο σπίτι της μητέρας;", ["Γιατί ο φούρνος της Άννας είναι μικρός", "Γιατί η μητέρα θέλει να βοηθήσει", "Γιατί εκεί θα φάνε", "Γιατί η Άννα δεν έχει φούρνο"], 0, "ο δικός σου φούρνος είναι μικρός"),
  Q("Γιατί θα αγοράσουν τα μελομακάρονα;", ["Γιατί είναι φθηνότερα", "Γιατί δεν τους τρώει κανείς", "Γιατί η μητέρα θα σηκωνόταν να διορθώσει τον Νίκο", "Γιατί ο φούρνος της γειτονιάς κάνει έκπτωση"], 2, "η μαμά θα σηκωθεί από την καρέκλα να με διορθώσει"),
 ],
 "gloss": {"καλεσμένη": "καλεσμένος — guest", "γαλοπούλα": "γαλοπούλα — turkey", "γέμιση": "γέμιση — stuffing", "κουκουνάρι": "κουκουνάρι — pine nut", "μελομακάρονα": "μελομακάρονο — honey-soaked Christmas biscuit", "ποδιά": "ποδιά — apron"},
})

ITEMS.append({
 "id": "l191-news-chelidonia-stamatoun-ergasies", "title": "Χελιδόνια σταματούν τις εργασίες σε έναν σταθμό", "title_en": "Swallows halt works at a station", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο τοπικό δελτίο ειδήσεων.",
 "script": [
  L("Εκφωνητής", "m", "Μια αποικία από χελιδόνια ανάγκασε τον δήμο να καθυστερήσει κατά δύο μήνες την ανακαίνιση του παλιού σιδηροδρομικού σταθμού της πόλης. Οι εργάτες βρήκαν κάτω από το στέγαστρο της αποβάθρας πάνω από σαράντα φωλιές, πολλές με αυγά και νεοσσούς.", "A colony of swallows has forced the municipality to delay by two months the renovation of the town's old railway station. The workers found more than forty nests under the platform canopy, many with eggs and chicks."),
  L("Εκφωνητής", "m", "Σύμφωνα με τη νομοθεσία, οι φωλιές των άγριων πουλιών προστατεύονται όσο χρησιμοποιούνται, και η καταστροφή τους τιμωρείται με πρόστιμο. Ο δήμος αποφάσισε να ξεκινήσουν οι εργασίες από την άλλη πλευρά του κτιρίου και να φτάσουν στο στέγαστρο τον Σεπτέμβριο, όταν τα πουλιά θα έχουν φύγει για την Αφρική.", "Under the law, the nests of wild birds are protected while they are in use, and destroying them is punished with a fine. The municipality decided that the works will start on the other side of the building and reach the canopy in September, when the birds will have left for Africa."),
  L("Εκφωνητής", "m", "Ο αρχιτέκτονας του έργου δήλωσε ότι στο νέο στέγαστρο θα τοποθετηθούν ειδικές τεχνητές φωλιές από πηλό, ώστε τα χελιδόνια να βρουν σπίτι όταν επιστρέψουν την άνοιξη. Κάτω από τις φωλιές θα μπουν μικρά ράφια, για να μη λερώνονται οι επιβάτες.", "The project's architect stated that special artificial clay nests will be fitted on the new canopy, so that the swallows will find a home when they return in spring. Small shelves will go under the nests so that passengers don't get dirtied."),
 ],
 "questions": [
  Q("Τι βρήκαν οι εργάτες κάτω από το στέγαστρο;", ["Ένα παλιό ρολόι του σταθμού", "Πάνω από σαράντα φωλιές χελιδονιών", "Μια οικογένεια από κουκουβάγιες", "Παλιά εισιτήρια"], 1, "πάνω από σαράντα φωλιές"),
  Q("Πότε θα φτάσουν οι εργασίες στο στέγαστρο;", ["Τον Σεπτέμβριο, όταν θα έχουν φύγει τα πουλιά", "Αμέσως", "Την επόμενη άνοιξη", "Σε έναν χρόνο"], 0, "να φτάσουν στο στέγαστρο τον Σεπτέμβριο, όταν τα πουλιά θα έχουν φύγει"),
  Q("Γιατί θα μπουν μικρά ράφια κάτω από τις νέες φωλιές;", ["Για να μην πέφτουν τα αυγά", "Για να στηρίζονται οι φωλιές", "Για να μη λερώνονται οι επιβάτες", "Για να μην πλησιάζουν οι γάτες"], 2, "για να μη λερώνονται οι επιβάτες"),
 ],
 "gloss": {"αποικία": "αποικία — colony", "στέγαστρο": "στέγαστρο — canopy, shelter", "νεοσσούς": "νεοσσός — chick, nestling", "νομοθεσία": "νομοθεσία — legislation", "τεχνητές": "τεχνητός — artificial", "πηλό": "πηλός — clay"},
})

ITEMS.append({
 "id": "l191-rep-nychterini-laiki", "title": "Μια λαϊκή αγορά που ανοίγει το βράδυ", "title_en": "A street market that opens in the evening", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ραδιοφωνικό ρεπορτάζ από μια λαϊκή αγορά που λειτουργεί απογευματινές και βραδινές ώρες.",
 "script": [
  L("Ρεπόρτερ", "f", "Είναι εφτά το απόγευμα, και ενώ τα περισσότερα μαγαζιά της γειτονιάς κλείνουν, στον δρόμο πίσω από την εκκλησία ανάβουν τα φώτα των πάγκων. Εδώ και έναν χρόνο ο δήμος δοκιμάζει μια λαϊκή που λειτουργεί από τις τέσσερις ως τις δέκα το βράδυ.", "It's seven in the evening, and while most of the neighbourhood's shops are closing, in the street behind the church the lights of the stalls are coming on. For a year now the municipality has been trying out a street market that runs from four until ten at night."),
  L("Παραγωγός", "m", "Για εμάς είναι πιο βολικό απ' ό,τι φαίνεται. Το πρωί μαζεύω τα λαχανικά από το χωράφι, και το απόγευμα τα έχω εδώ φρέσκα, όχι από την προηγούμενη μέρα. Κι έρχονται άνθρωποι που δεν είχαν πατήσει ποτέ σε λαϊκή, γιατί δούλευαν τις πρωινές ώρες.", "For us it's more convenient than it looks. In the morning I pick the vegetables from the field, and in the afternoon I have them here fresh, not from the day before. And people come who had never set foot in a street market, because they worked in the mornings."),
  L("Ρεπόρτερ", "f", "Ανάμεσα στους πάγκους κυκλοφορούν νεαρά ζευγάρια, φοιτητές και μητέρες με καρότσια. Μια νοσηλεύτρια μάς λέει ότι μετά από βάρδιες δώδεκα ωρών, αυτή είναι η μόνη ευκαιρία της να αγοράσει φρούτα που δεν είναι από το σούπερ μάρκετ.", "Among the stalls wander young couples, students and mothers with prams. A nurse tells us that after twelve-hour shifts, this is her only chance to buy fruit that isn't from the supermarket."),
  L("Ρεπόρτερ", "f", "Δεν είναι όλοι ευχαριστημένοι. Οι κάτοικοι του δρόμου παραπονιούνται για τον θόρυβο από τα φορτηγάκια που μαζεύουν τους πάγκους μετά τις δέκα. Ο δήμος σκέφτεται να μεταφέρει την αγορά σε μια πλατεία με λιγότερα σπίτια.", "Not everyone is happy. Residents of the street complain about the noise from the vans that pack up the stalls after ten. The municipality is considering moving the market to a square with fewer houses."),
 ],
 "questions": [
  Q("Τι πλεονέκτημα έχει η βραδινή λαϊκή για τον παραγωγό;", ["Πουλάει πιο ακριβά", "Τα λαχανικά του είναι φρέσκα από το ίδιο πρωί", "Δεν πληρώνει ενοίκιο για τον πάγκο", "Ξεκουράζεται το πρωί"], 1, "Το πρωί μαζεύω τα λαχανικά από το χωράφι, και το απόγευμα τα έχω εδώ φρέσκα"),
  Q("Γιατί η νοσηλεύτρια ψωνίζει εκεί;", ["Γιατί μένει δίπλα", "Γιατί είναι φθηνότερα", "Γιατί είναι η μόνη ευκαιρία της μετά τις μεγάλες βάρδιες", "Γιατί γνωρίζει τους παραγωγούς"], 2, "αυτή είναι η μόνη ευκαιρία της να αγοράσει φρούτα"),
  Q("Για τι παραπονιούνται οι κάτοικοι;", ["Για τον θόρυβο από τα φορτηγάκια μετά τις δέκα", "Για τα σκουπίδια", "Για τις υψηλές τιμές", "Για το πάρκινγκ"], 0, "για τον θόρυβο από τα φορτηγάκια που μαζεύουν τους πάγκους μετά τις δέκα"),
 ],
 "gloss": {"πάγκων": "πάγκος — stall", "λαϊκή": "λαϊκή (αγορά) — street market", "βολικό": "βολικός — convenient", "καρότσια": "καρότσι — pram, pushchair", "βάρδιες": "βάρδια — shift", "φορτηγάκια": "φορτηγάκι — van, small truck"},
})

ITEMS.append({
 "id": "l191-c1-onomata-ton-dromon", "title": "Τι μας λένε τα ονόματα των δρόμων", "title_en": "What street names tell us", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν ιστορικό που μελετά τα ονόματα των δρόμων στις ελληνικές πόλεις.",
 "script": [
  L("Δημοσιογράφος", "f", "Γιατί ένας ιστορικός ασχολείται με τις πινακίδες των δρόμων;", "Why does a historian concern himself with street signs?"),
  L("Ιστορικός", "m", "Γιατί είναι ίσως το πιο δημόσιο αρχείο που έχουμε. Κάθε φορά που ένας δήμος δίνει όνομα σε έναν δρόμο, δηλώνει ποιον θέλει να θυμάται η κοινότητα. Αν περπατήσετε σε μια ελληνική πόλη, θα δείτε στρώματα: αρχαίους φιλοσόφους και θεούς, αγωνιστές του 1821, ευεργέτες, πολιτικούς, και, πιο πρόσφατα, λογοτέχνες και επιστήμονες. Οι γυναίκες, πάντως, παραμένουν εντυπωσιακά λίγες, πέρα από ηρωίδες της Επανάστασης.", "Because it is perhaps the most public archive we have. Every time a municipality gives a street a name, it declares whom it wants the community to remember. If you walk through a Greek town, you'll see layers: ancient philosophers and gods, fighters of 1821, benefactors, politicians, and, more recently, writers and scientists. Women, though, remain strikingly few, apart from heroines of the Revolution."),
  L("Δημοσιογράφος", "f", "Και τα ονόματα αλλάζουν;", "And do the names change?"),
  L("Ιστορικός", "m", "Συνεχώς, και κάθε αλλαγή καθρεφτίζει μια πολιτική στιγμή. Μετά από κάθε μεγάλη πολιτική μεταβολή στη χώρα, ορισμένοι δρόμοι μετονομάστηκαν. Το ενδιαφέρον όμως είναι ότι ο κόσμος συχνά αγνοεί την επίσημη ονομασία. Στην Αθήνα, για παράδειγμα, η οδός Πανεπιστημίου ονομάζεται επίσημα Ελευθερίου Βενιζέλου, όμως σχεδόν κανείς δεν τη λέει έτσι. Η καθημερινή χρήση έχει τη δική της μνήμη, που δεν υπακούει σε αποφάσεις δημοτικών συμβουλίων.", "Constantly, and each change mirrors a political moment. After every major political upheaval in the country, certain streets were renamed. What's interesting, though, is that people often ignore the official name. In Athens, for example, Panepistimiou Street is officially called Eleftheriou Venizelou, yet almost nobody calls it that. Everyday usage has a memory of its own, which doesn't obey the decisions of municipal councils."),
  L("Δημοσιογράφος", "f", "Τι θα προτείνατε σε έναν δήμο που θέλει να ονομάσει έναν νέο δρόμο;", "What would you suggest to a municipality that wants to name a new street?"),
  L("Ιστορικός", "m", "Να ρωτήσει τους κατοίκους και να βάλει κάτω από την πινακίδα μια μικρή επεξήγηση: ποιος ήταν αυτός ή αυτή και γιατί τον θυμόμαστε. Ένα όνομα χωρίς ιστορία γίνεται γρήγορα απλώς μια διεύθυνση. Και, αν μου επιτρέπετε, να κοιτάξει πόσοι δρόμοι της πόλης έχουν ονόματα γυναικών, πριν αποφασίσει.", "To ask the residents, and to put a short explanation under the sign: who he or she was and why we remember them. A name without a story quickly becomes merely an address. And, if you'll allow me, to look at how many of the town's streets bear women's names, before deciding."),
 ],
 "questions": [
  Q("Γιατί θεωρεί ο ιστορικός τα ονόματα των δρόμων σημαντικό αρχείο;", ["Γιατί είναι πολύ παλιά", "Γιατί δείχνουν ποιον θέλει να θυμάται η κοινότητα", "Γιατί βοηθούν τους τουρίστες", "Γιατί δεν αλλάζουν ποτέ"], 1, "δηλώνει ποιον θέλει να θυμάται η κοινότητα"),
  Q("Τι δείχνει, κατά τον ιστορικό, το παράδειγμα της οδού Πανεπιστημίου;", ["Ότι οι Αθηναίοι δεν ξέρουν ιστορία", "Ότι οι πινακίδες είναι λάθος", "Ότι η καθημερινή χρήση δεν υπακούει στις επίσημες αποφάσεις", "Ότι ο δρόμος πρέπει να μετονομαστεί"], 2, "Η καθημερινή χρήση έχει τη δική της μνήμη, που δεν υπακούει σε αποφάσεις δημοτικών συμβουλίων"),
  Q("Τι προτείνει να μπαίνει κάτω από τις νέες πινακίδες;", ["Μια μικρή επεξήγηση για το πρόσωπο", "Ο ταχυδρομικός κώδικας", "Ένας χάρτης της περιοχής", "Το όνομα του δημάρχου"], 0, "να βάλει κάτω από την πινακίδα μια μικρή επεξήγηση"),
 ],
 "gloss": {"πινακίδες": "πινακίδα — (street) sign", "στρώματα": "στρώμα — layer", "ευεργέτες": "ευεργέτης — benefactor", "μετονομάστηκαν": "μετονομάζομαι — to be renamed", "αγνοεί": "αγνοώ — to ignore", "υπακούει": "υπακούω — to obey", "επεξήγηση": "επεξήγηση — explanation"},
})

ITEMS.append({
 "id": "l191-c1-giati-kleinoume-ta-matia-otan-ftarnizomaste", "title": "Γιατί κλείνουμε τα μάτια όταν φτερνιζόμαστε", "title_en": "Why we close our eyes when we sneeze", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν γιατρό σε μια ραδιοφωνική εκπομπή επιστήμης.",
 "script": [
  L("Γιατρός", "m", "Υπάρχει ένας επίμονος μύθος ότι, αν φτερνιστεί κανείς με ανοιχτά μάτια, θα του πεταχτούν τα μάτια από τις κόγχες. Δεν ισχύει. Η πίεση που δημιουργείται κατά το φτέρνισμα αφορά κυρίως τους πνεύμονες και τη μύτη, και δεν υπάρχει κανένας μηχανισμός που να σπρώχνει τα μάτια προς τα έξω. Το ότι τα κλείνουμε είναι ένα αντανακλαστικό: τα νεύρα που ενεργοποιούνται στο φτέρνισμα συνδέονται στενά με εκείνα που ελέγχουν τα βλέφαρα.", "There is a persistent myth that, if you sneeze with your eyes open, your eyes will pop out of their sockets. It isn't true. The pressure created during a sneeze mainly concerns the lungs and the nose, and there is no mechanism that pushes the eyes outwards. The fact that we close them is a reflex: the nerves activated in a sneeze are closely connected with those that control the eyelids."),
  L("Γιατρός", "m", "Γιατί όμως να έχει εξελιχθεί ένα τέτοιο αντανακλαστικό; Η πιο διαδεδομένη υπόθεση είναι ότι προστατεύει τα μάτια από τα μικρόβια και τα σωματίδια που εκτοξεύονται με μεγάλη ταχύτητα. Είναι μια λογική εξήγηση, αλλά να το πούμε τίμια: δεν έχει αποδειχθεί. Και υπάρχουν άνθρωποι που καταφέρνουν να κρατήσουν τα μάτια τους ανοιχτά, χωρίς καμία συνέπεια.", "But why would such a reflex have evolved? The most widespread hypothesis is that it protects the eyes from germs and particles that are expelled at great speed. It's a reasonable explanation, but let's be honest: it hasn't been proven. And there are people who manage to keep their eyes open, with no consequences at all."),
  L("Γιατρός", "m", "Ένα ακόμα πιο παράξενο φαινόμενο είναι το λεγόμενο φωτικό αντανακλαστικό του φτερνίσματος: ορισμένοι άνθρωποι φτερνίζονται όταν βγαίνουν ξαφνικά από το σκοτάδι στον ήλιο. Οι εκτιμήσεις διαφέρουν πολύ, αλλά αφορά ένα σημαντικό ποσοστό του πληθυσμού, και φαίνεται να κληρονομείται. Η επικρατέστερη εξήγηση είναι ότι τα σήματα από το οπτικό νεύρο «διαρρέουν» σε γειτονικά νεύρα του προσώπου. Με άλλα λόγια, ο εγκέφαλος, για μια στιγμή, μπερδεύει το φως με τον κόκκο της σκόνης.", "An even stranger phenomenon is the so-called photic sneeze reflex: some people sneeze when they suddenly step out of the dark into the sun. Estimates vary a lot, but it affects a significant proportion of the population, and it appears to be inherited. The prevailing explanation is that signals from the optic nerve 'leak' into neighbouring facial nerves. In other words, the brain, for a moment, confuses light with a speck of dust."),
 ],
 "questions": [
  Q("Τι λέει ο γιατρός για τον μύθο ότι πετάγονται τα μάτια;", ["Ότι ισχύει μόνο για τα παιδιά", "Ότι δεν ισχύει, γιατί δεν υπάρχει μηχανισμός που να σπρώχνει τα μάτια προς τα έξω", "Ότι συμβαίνει σπάνια", "Ότι δεν έχει μελετηθεί"], 1, "δεν υπάρχει κανένας μηχανισμός που να σπρώχνει τα μάτια προς τα έξω"),
  Q("Πώς κρίνει ο γιατρός την υπόθεση ότι το αντανακλαστικό προστατεύει τα μάτια;", ["Ως αποδεδειγμένη", "Ως παράλογη", "Ως λογική αλλά μη αποδεδειγμένη", "Ως ξεπερασμένη"], 2, "Είναι μια λογική εξήγηση, αλλά να το πούμε τίμια: δεν έχει αποδειχθεί"),
  Q("Ποια είναι η επικρατέστερη εξήγηση για το φωτικό αντανακλαστικό;", ["Τα σήματα του οπτικού νεύρου διαρρέουν σε γειτονικά νεύρα του προσώπου", "Ο ήλιος ερεθίζει τη μύτη", "Είναι μια μορφή αλλεργίας", "Η ζέστη προκαλεί φτέρνισμα"], 0, "τα σήματα από το οπτικό νεύρο «διαρρέουν» σε γειτονικά νεύρα του προσώπου"),
 ],
 "gloss": {"φτερνιστεί": "φτερνίζομαι — to sneeze", "κόγχες": "κόγχη — (eye) socket", "αντανακλαστικό": "αντανακλαστικό — reflex", "βλέφαρα": "βλέφαρο — eyelid", "εκτοξεύονται": "εκτοξεύομαι — to be shot out, expelled", "κληρονομείται": "κληρονομούμαι — to be inherited", "διαρρέουν": "διαρρέω — to leak"},
})

ITEMS.append({
 "id": "l191-rep-koureas-sto-syssitio", "title": "Ο κουρέας του συσσιτίου", "title_en": "The barber at the soup kitchen", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για έναν κουρέα που κουρεύει δωρεάν άστεγους σε ένα συσσίτιο.",
 "script": [
  L("Ρεπόρτερ", "m", "Κάθε Κυριακή, μετά το μεσημεριανό φαγητό στο συσσίτιο της ενορίας, ο κύριος Παναγιώτης στήνει μια καρέκλα, έναν καθρέφτη και ένα τραπεζάκι με τα εργαλεία του. Είναι κουρέας εδώ και σαράντα χρόνια, και εδώ και πέντε κουρεύει δωρεάν όποιον το χρειάζεται.", "Every Sunday, after lunch at the parish soup kitchen, Mr Panagiotis sets up a chair, a mirror and a small table with his tools. He has been a barber for forty years, and for five years now he has been cutting the hair of anyone who needs it, free of charge."),
  L("Κουρέας", "m", "Ένα κούρεμα δεν είναι πολυτέλεια. Όταν ψάχνεις δουλειά ή πας σε μια υπηρεσία, ο τρόπος που φαίνεσαι μετράει, είτε μας αρέσει είτε όχι. Έχω δει ανθρώπους να κοιτάζονται στον καθρέφτη μετά από μήνες και να χαμογελούν σαν να ξαναβρήκαν έναν παλιό φίλο.", "A haircut isn't a luxury. When you're looking for work or going to a public office, the way you look matters, whether we like it or not. I've seen people look at themselves in the mirror after months and smile as if they'd found an old friend again."),
  L("Ρεπόρτερ", "m", "Ο πρώτος πελάτης σήμερα είναι ο Στάθης, πρώην ναυτικός, που έχει συνέντευξη για δουλειά σε μια αποθήκη την Τρίτη. Όσο ο κύριος Παναγιώτης του κόβει τα γένια, οι δυο τους συζητούν για ποδόσφαιρο και για λιμάνια που έχουν δει.", "The first customer today is Stathis, a former sailor, who has a job interview at a warehouse on Tuesday. While Mr Panagiotis trims his beard, the two of them talk about football and about ports they have seen."),
  L("Κουρέας", "m", "Δεν ρωτάω ποτέ πώς βρέθηκε κάποιος στον δρόμο. Αν θέλει να μου πει, ακούω. Στο κουρείο πάντα αυτό έκανα: έκοβα μαλλιά και άκουγα. Εδώ απλώς δεν παίρνω χρήματα.", "I never ask how someone ended up on the street. If they want to tell me, I listen. At the barber's shop that's what I always did: I cut hair and I listened. Here I just don't take money."),
 ],
 "questions": [
  Q("Πότε κουρεύει ο κύριος Παναγιώτης στο συσσίτιο;", ["Κάθε Κυριακή μετά το μεσημεριανό", "Κάθε πρωί πριν ανοίξει το κουρείο", "Μία φορά τον μήνα", "Μόνο τις γιορτές"], 0, "Κάθε Κυριακή, μετά το μεσημεριανό φαγητό"),
  Q("Γιατί λέει ότι το κούρεμα δεν είναι πολυτέλεια;", ["Γιατί κοστίζει φθηνά", "Γιατί η εμφάνιση μετράει όταν ψάχνεις δουλειά", "Γιατί προλαμβάνει ασθένειες", "Γιατί το ζητούν οι υπηρεσίες"], 1, "ο τρόπος που φαίνεσαι μετράει"),
  Q("Τι κάνει ο κουρέας όσον αφορά τις ιστορίες των πελατών του;", ["Τις γράφει σε ένα τετράδιο", "Ρωτά πάντα τι τους συνέβη", "Δεν ρωτά, αλλά ακούει αν θέλουν να μιλήσουν", "Τις διηγείται σε άλλους"], 2, "Δεν ρωτάω ποτέ πώς βρέθηκε κάποιος στον δρόμο. Αν θέλει να μου πει, ακούω"),
 ],
 "gloss": {"κουρέας": "κουρέας — barber", "συσσίτιο": "συσσίτιο — soup kitchen", "ενορίας": "ενορία — parish", "πολυτέλεια": "πολυτέλεια — luxury", "πρώην": "πρώην — former", "γένια": "γένια — beard"},
})

rnd = random.Random(191)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-191.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
