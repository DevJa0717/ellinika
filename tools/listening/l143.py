# Source for library/listening/listening-143.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l143.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l143-vm-synergeio", "title": "Το αυτοκίνητο στο συνεργείο", "title_en": "The car at the garage", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε αφήσει το αυτοκίνητό σας για σέρβις. Ακούτε ένα μήνυμα από το συνεργείο στον τηλεφωνητή σας.",
 "script": [
  L("Μηχανικός", "m", "Καλησπέρα, ο Σταύρος από το συνεργείο είμαι. Τελειώσαμε το σέρβις: αλλάξαμε λάδια και φίλτρα, όπως είχαμε πει.", "Good afternoon, it's Stavros from the garage. We've finished the service: we changed the oil and filters, as we'd said."),
  L("Μηχανικός", "m", "Βρήκαμε όμως ότι τα τακάκια στα μπροστινά φρένα έχουν σχεδόν τελειώσει. Δεν είναι επικίνδυνο για τις επόμενες μέρες, αλλά καλό θα ήταν να τα αλλάξουμε τώρα, που το αυτοκίνητο είναι εδώ. Το κόστος είναι εκατόν είκοσι ευρώ μαζί με την εργασία.", "But we found that the pads on the front brakes are almost worn out. It's not dangerous for the next few days, but it would be good to change them now, while the car is here. The cost is a hundred and twenty euros including labour."),
  L("Μηχανικός", "m", "Αν συμφωνείτε, πάρτε με τηλέφωνο μέχρι τις έξι, για να παραγγείλω τα ανταλλακτικά. Θα έρθουν αύριο το πρωί και το αυτοκίνητο θα είναι έτοιμο το μεσημέρι. Αν όχι, μπορείτε να το πάρετε από σήμερα.", "If you agree, call me by six so I can order the parts. They'll arrive tomorrow morning and the car will be ready at noon. If not, you can pick it up today."),
 ],
 "questions": [
  Q("Τι πρόβλημα βρήκε ο μηχανικός;", ["Τα τακάκια στα μπροστινά φρένα έχουν σχεδόν τελειώσει", "Η μπαταρία είναι άδεια", "Ένα λάστιχο είναι τρυπημένο", "Τα λάδια ήταν λάθος"], 0, "τα τακάκια στα μπροστινά φρένα έχουν σχεδόν τελειώσει"),
  Q("Πόσο κοστίζει η αλλαγή;", ["Είκοσι ευρώ", "Εκατόν είκοσι ευρώ μαζί με την εργασία", "Διακόσια ευρώ", "Εκατό ευρώ χωρίς την εργασία"], 1, "Το κόστος είναι εκατόν είκοσι ευρώ μαζί με την εργασία"),
  Q("Μέχρι πότε πρέπει να του τηλεφωνήσετε, αν συμφωνείτε;", ["Μέχρι αύριο το πρωί", "Μέχρι το μεσημέρι", "Μέχρι τις έξι", "Μέχρι το Σάββατο"], 2, "πάρτε με τηλέφωνο μέχρι τις έξι"),
 ],
 "gloss": {"σέρβις": "σέρβις — service", "συνεργείο": "συνεργείο — garage, repair shop", "φίλτρα": "φίλτρο — filter", "τακάκια": "τακάκι — brake pad", "φρένα": "φρένο — brake", "εργασία": "εργασία — labour", "παραγγείλω": "παραγγέλνω — to order", "ανταλλακτικά": "ανταλλακτικό — spare part"}
})

ITEMS.append({
 "id": "l143-ann-anaklisi", "title": "Ανάκληση γιαουρτιού", "title_en": "Yoghurt recall", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα σούπερ μάρκετ και ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Υπάλληλος", "f", "Αγαπητοί πελάτες, σας ενημερώνουμε ότι η εταιρεία γαλακτοκομικών «Λευκό Βουνό» ανακαλεί μία παρτίδα στραγγιστού γιαουρτιού των πεντακοσίων γραμμαρίων, με ημερομηνία λήξης δεκαπέντε Δεκεμβρίου.", "Dear customers, we inform you that the dairy company 'White Mountain' is recalling one batch of strained yoghurt in five-hundred-gram pots, with a best-before date of the fifteenth of December."),
  L("Υπάλληλος", "f", "Σε κάποια κεσεδάκια της παρτίδας μπορεί να υπάρχουν μικρά κομμάτια πλαστικού από τη συσκευασία. Τα υπόλοιπα προϊόντα της εταιρείας δεν επηρεάζονται και μπορούν να καταναλωθούν κανονικά.", "Some pots in the batch may contain small pieces of plastic from the packaging. The company's other products are not affected and can be consumed as normal."),
  L("Υπάλληλος", "f", "Αν έχετε αγοράσει το συγκεκριμένο προϊόν, μην το καταναλώσετε. Μπορείτε να το επιστρέψετε σε οποιοδήποτε κατάστημά μας και να πάρετε πίσω τα χρήματά σας, ακόμα και χωρίς απόδειξη.", "If you have bought this product, do not eat it. You can return it to any of our shops and get your money back, even without a receipt."),
 ],
 "questions": [
  Q("Ποιο προϊόν ανακαλείται;", ["Όλα τα γιαούρτια της εταιρείας", "Μία παρτίδα στραγγιστού γιαουρτιού των πεντακοσίων γραμμαρίων", "Ένα είδος γάλακτος", "Ένα τυρί"], 1, "ανακαλεί μία παρτίδα στραγγιστού γιαουρτιού των πεντακοσίων γραμμαρίων"),
  Q("Ποιο είναι το πρόβλημα;", ["Το γιαούρτι έχει λήξει", "Η τιμή ήταν λάθος", "Μπορεί να υπάρχουν μικρά κομμάτια πλαστικού", "Λείπει η ετικέτα"], 2, "μπορεί να υπάρχουν μικρά κομμάτια πλαστικού"),
  Q("Τι μπορούν να κάνουν όσοι το αγόρασαν;", ["Να το επιστρέψουν σε οποιοδήποτε κατάστημα και να πάρουν πίσω τα χρήματά τους, και χωρίς απόδειξη", "Να το φάνε αν είναι κρύο", "Να το αλλάξουν μόνο με απόδειξη", "Να τηλεφωνήσουν στην εταιρεία"], 0, "Μπορείτε να το επιστρέψετε σε οποιοδήποτε κατάστημά μας"),
 ],
 "gloss": {"γαλακτοκομικών": "γαλακτοκομικός — dairy", "ανακαλεί": "ανακαλώ — to recall", "παρτίδα": "παρτίδα — batch", "στραγγιστού": "στραγγιστός — strained", "λήξης": "λήξη — expiry", "κεσεδάκια": "κεσεδάκι — (yoghurt) pot", "συσκευασία": "συσκευασία — packaging", "επηρεάζονται": "επηρεάζομαι — to be affected", "καταναλωθούν": "καταναλώνομαι — to be consumed", "απόδειξη": "απόδειξη — receipt"}
})

ITEMS.append({
 "id": "l143-dia-gamos-xorio", "title": "Ποιος θα οδηγήσει στον γάμο;", "title_en": "Who will drive to the wedding?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φίλοι συζητούν για έναν γάμο σε ένα χωριό.",
 "script": [
  L("Άρης", "m", "Ο γάμος του Μάνου είναι σε ένα χωριό δύο ώρες από την Αθήνα, και το γλέντι μετά θα κρατήσει σίγουρα μέχρι το πρωί. Πώς θα γυρίσουμε;", "Manos's wedding is in a village two hours from Athens, and the party afterwards will surely last until morning. How will we get back?"),
  L("Ελένη", "f", "Σκέφτηκα να κλείσουμε δωμάτιο σε έναν ξενώνα στο χωριό και να γυρίσουμε την Κυριακή. Έχει μόνο τέσσερα δωμάτια όμως, και ο Μάνος λέει ότι τα μισά τα έχουν ήδη κλείσει συγγενείς.", "I thought we could book a room at a guesthouse in the village and come back on Sunday. But it only has four rooms, and Manos says relatives have already booked half of them."),
  L("Άρης", "m", "Τότε ας το κλείσουμε σήμερα κιόλας. Αλλιώς, κάποιος από εμάς θα πρέπει να μην πιει τίποτα όλο το βράδυ και να οδηγήσει στις πέντε το πρωί.", "Then let's book it today. Otherwise, one of us will have to drink nothing all evening and drive at five in the morning."),
  L("Ελένη", "f", "Εγώ πάντως δεν οδηγώ τέτοια ώρα σε επαρχιακό δρόμο. Πάρε τώρα τον ξενώνα, κι εγώ θα βρω πού θα αφήσουμε τον σκύλο για το σαββατοκύριακο.", "Well, I'm not driving on a country road at that hour. Call the guesthouse now, and I'll find where we can leave the dog for the weekend."),
 ],
 "questions": [
  Q("Τι προτείνει η Ελένη;", ["Να γυρίσουν με λεωφορείο", "Να κλείσουν δωμάτιο σε έναν ξενώνα στο χωριό", "Να φύγουν πριν από το γλέντι", "Να μην πάνε στον γάμο"], 1, "να κλείσουμε δωμάτιο σε έναν ξενώνα στο χωριό"),
  Q("Γιατί πρέπει να βιαστούν;", ["Γιατί ο ξενώνας έχει μόνο τέσσερα δωμάτια και τα μισά είναι κλεισμένα", "Γιατί οι τιμές θα ανέβουν", "Γιατί ο γάμος είναι αύριο", "Γιατί ο ξενώνας κλείνει τον χειμώνα"], 0, "Έχει μόνο τέσσερα δωμάτια όμως"),
  Q("Τι θα κάνει η Ελένη;", ["Θα οδηγήσει στην επιστροφή", "Θα τηλεφωνήσει στον ξενώνα", "Θα αγοράσει το δώρο", "Θα βρει πού θα αφήσουν τον σκύλο"], 3, "θα βρω πού θα αφήσουμε τον σκύλο"),
 ],
 "gloss": {"γλέντι": "γλέντι — party, celebration", "ξενώνα": "ξενώνας — guesthouse", "συγγενείς": "συγγενής — relative", "κιόλας": "κιόλας — already, right away", "επαρχιακό": "επαρχιακός — provincial, country (road)"}
})

ITEMS.append({
 "id": "l143-int-kapetanios", "title": "Το τελευταίο ταξίδι του καπετάνιου", "title_en": "The captain's last voyage", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια ραδιοφωνική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "f", "Καπετάν Μιχάλη, αύριο κάνετε το τελευταίο σας δρομολόγιο πριν από τη σύνταξη. Πόσα χρόνια ταξιδεύετε στη γραμμή των Κυκλάδων;", "Captain Michalis, tomorrow you make your last crossing before retirement. How many years have you sailed the Cyclades line?"),
  L("Καπετάνιος", "m", "Τριάντα δύο χρόνια σε αυτή τη γραμμή, και άλλα δέκα πριν σε φορτηγά πλοία. Έχω περάσει από τη Σύρο, υπολογίζω, πάνω από έξι χιλιάδες φορές. Ξέρω κάθε βράχο και κάθε φάρο.", "Thirty-two years on this line, and another ten before that on cargo ships. I reckon I've passed through Syros more than six thousand times. I know every rock and every lighthouse."),
  L("Δημοσιογράφος", "f", "Ποια είναι η πιο δύσκολη στιγμή που θυμάστε;", "What is the hardest moment you remember?"),
  L("Καπετάνιος", "m", "Ένα βράδυ του Φεβρουαρίου, με εννιά μποφόρ, μια γυναίκα στο πλοίο άρχισε να γεννάει. Δεν μπορούσαμε να μπούμε σε κανένα λιμάνι. Ευτυχώς υπήρχε μια νοσηλεύτρια ανάμεσα στους επιβάτες, και το μωρό γεννήθηκε στο σαλόνι της πρώτης θέσης. Τον λένε Νικόλα, σαν τον άγιο των ναυτικών, και κάθε χρόνο μού στέλνει κάρτα στη γιορτή του. Αύριο θα είναι στη γέφυρα μαζί μου.", "One February night, in force nine, a woman on board went into labour. We couldn't enter any port. Fortunately there was a nurse among the passengers, and the baby was born in the first-class lounge. He's called Nikolas, like the saint of sailors, and every year he sends me a card on his name day. Tomorrow he'll be on the bridge with me."),
 ],
 "questions": [
  Q("Πόσα χρόνια ταξιδεύει στη γραμμή των Κυκλάδων;", ["Δέκα", "Έξι", "Σαράντα δύο", "Τριάντα δύο"], 3, "Τριάντα δύο χρόνια σε αυτή τη γραμμή"),
  Q("Τι συνέβη ένα βράδυ του Φεβρουαρίου;", ["Το πλοίο χάλασε", "Μια γυναίκα γέννησε στο πλοίο", "Ένας επιβάτης έπεσε στη θάλασσα", "Το πλοίο έπεσε σε βράχο"], 1, "μια γυναίκα στο πλοίο άρχισε να γεννάει"),
  Q("Ποιος θα είναι μαζί του αύριο στη γέφυρα;", ["Η γυναίκα του", "Η νοσηλεύτρια", "Ο Νικόλας, το παιδί που γεννήθηκε στο πλοίο", "Ο νέος καπετάνιος"], 2, "Αύριο θα είναι στη γέφυρα μαζί μου"),
 ],
 "gloss": {"δρομολόγιο": "δρομολόγιο — (scheduled) crossing", "φορτηγά πλοία": "φορτηγό πλοίο — cargo ship", "υπολογίζω": "υπολογίζω — to reckon", "φάρο": "φάρος — lighthouse", "μποφόρ": "μποφόρ — Beaufort (wind force)", "γεννάει": "γεννάω — to give birth", "επιβάτες": "επιβάτης — passenger", "σαλόνι": "σαλόνι — lounge", "ναυτικών": "ναυτικός — sailor", "γέφυρα": "γέφυρα — (ship's) bridge"}
})

ITEMS.append({
 "id": "l143-news-nomisma", "title": "Ένα αρχαίο νόμισμα στον βυθό", "title_en": "An ancient coin on the seabed", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων.",
 "script": [
  L("Εκφωνήτρια", "f", "Ένας δεκατετράχρονος μαθητής από τη Θεσσαλονίκη βρήκε ένα αρχαίο ασημένιο νόμισμα, ενώ έκανε κατάδυση με μάσκα σε μια παραλία της Χαλκιδικής, και το παρέδωσε αμέσως στην αστυνομία.", "A fourteen-year-old pupil from Thessaloniki found an ancient silver coin while snorkelling at a beach in Halkidiki, and immediately handed it over to the police."),
  L("Εκφωνήτρια", "f", "Σύμφωνα με τους αρχαιολόγους της Εφορείας Εναλίων Αρχαιοτήτων, το νόμισμα χρονολογείται στον τέταρτο αιώνα προ Χριστού και φέρει στη μία πλευρά το κεφάλι του θεού Απόλλωνα. Είναι σε εξαιρετική κατάσταση, παρόλο που έμεινε στη θάλασσα πάνω από δύο χιλιάδες χρόνια.", "According to archaeologists from the Ephorate of Underwater Antiquities, the coin dates from the fourth century BC and bears the head of the god Apollo on one side. It is in excellent condition, even though it spent more than two thousand years in the sea."),
  L("Εκφωνήτρια", "f", "Οι αρχαιολόγοι θα ερευνήσουν την περιοχή τις επόμενες εβδομάδες, μήπως υπάρχει εκεί κάποιο αρχαίο ναυάγιο. Ο μαθητής θα λάβει έπαινο από το υπουργείο Πολιτισμού, και το νόμισμα θα εκτεθεί σε μουσείο της περιοχής.", "The archaeologists will search the area in the coming weeks, in case there is an ancient shipwreck there. The pupil will receive a commendation from the Ministry of Culture, and the coin will be displayed in a museum in the area."),
 ],
 "questions": [
  Q("Τι έκανε ο μαθητής με το νόμισμα;", ["Το κράτησε", "Το παρέδωσε αμέσως στην αστυνομία", "Το πούλησε", "Το έδειξε στους φίλους του"], 1, "το παρέδωσε αμέσως στην αστυνομία"),
  Q("Από πότε είναι το νόμισμα;", ["Από τον τέταρτο αιώνα προ Χριστού", "Από τη βυζαντινή εποχή", "Από τον 19ο αιώνα", "Από τον πρώτο αιώνα μετά Χριστόν"], 0, "χρονολογείται στον τέταρτο αιώνα προ Χριστού"),
  Q("Γιατί θα ερευνήσουν την περιοχή οι αρχαιολόγοι;", ["Για να βρουν κι άλλα νομίσματα για το μουσείο", "Γιατί εκεί θα χτιστεί ξενοδοχείο", "Μήπως υπάρχει εκεί κάποιο αρχαίο ναυάγιο", "Για να καθαρίσουν τον βυθό"], 2, "μήπως υπάρχει εκεί κάποιο αρχαίο ναυάγιο"),
 ],
 "gloss": {"ασημένιο": "ασημένιος — silver", "κατάδυση": "κατάδυση — dive", "παρέδωσε": "παραδίδω — to hand over", "Εναλίων Αρχαιοτήτων": "ενάλιες αρχαιότητες — underwater antiquities", "χρονολογείται": "χρονολογούμαι — to date from", "φέρει": "φέρω — to bear", "ναυάγιο": "ναυάγιο — shipwreck", "έπαινο": "έπαινος — commendation", "εκτεθεί": "εκτίθεμαι — to be displayed"}
})

ITEMS.append({
 "id": "l143-mon-kano", "title": "Πριν από τη βόλτα με κανό", "title_en": "Before the canoe trip", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν οδηγό να μιλά σε μια ομάδα πριν από μια βόλτα με κανό στο ποτάμι.",
 "script": [
  L("Οδηγός", "m", "Καλημέρα σε όλους! Πριν μπούμε στο νερό, λίγα σημαντικά πράγματα. Η διαδρομή είναι οχτώ χιλιόμετρα και θα κρατήσει περίπου δυόμισι ώρες, με μια στάση για μπάνιο και φαγητό στη μέση.", "Good morning, everyone! Before we get in the water, a few important things. The route is eight kilometres and will take about two and a half hours, with a stop for a swim and food halfway."),
  L("Οδηγός", "m", "Το σωσίβιο το φοράτε όλη την ώρα, ακόμα κι αν είστε καλοί κολυμβητές, και το κλείνετε καλά. Τα κινητά και τα κλειδιά μπαίνουν σε αυτές τις αδιάβροχες σακούλες. Το ποτάμι σε δύο σημεία έχει μικρά ρεύματα· εκεί θα πηγαίνω πρώτος και θα σας δείχνω με το κουπί από πού να περάσετε.", "You wear the life jacket the whole time, even if you're good swimmers, and you fasten it properly. Phones and keys go into these waterproof bags. In two places the river has small rapids; there I'll go first and show you with my paddle where to pass."),
  L("Οδηγός", "m", "Αν αναποδογυρίσει το κανό, μην πανικοβληθείτε. Κρατηθείτε από το κανό, βάλτε τα πόδια μπροστά και περιμένετε. Θα έρθω αμέσως. Και κάτι τελευταίο: μην αφήνετε τίποτα στο ποτάμι, ούτε ένα χαρτάκι.", "If the canoe capsizes, don't panic. Hold on to the canoe, put your feet in front and wait. I'll come straight away. And one last thing: don't leave anything in the river, not even a scrap of paper."),
 ],
 "questions": [
  Q("Πόσο θα κρατήσει η διαδρομή;", ["Οχτώ ώρες", "Περίπου δυόμισι ώρες", "Μία ώρα", "Όλη τη μέρα"], 1, "θα κρατήσει περίπου δυόμισι ώρες"),
  Q("Τι πρέπει να κάνουν με το σωσίβιο;", ["Να το φορούν μόνο στα ρεύματα", "Να το φορούν όσοι δεν ξέρουν κολύμπι", "Να το φορούν όλη την ώρα και να το κλείνουν καλά", "Να το έχουν μέσα στο κανό"], 2, "Το σωσίβιο το φοράτε όλη την ώρα"),
  Q("Τι πρέπει να κάνουν αν αναποδογυρίσει το κανό;", ["Να κρατηθούν από το κανό, να βάλουν τα πόδια μπροστά και να περιμένουν", "Να κολυμπήσουν γρήγορα στην όχθη", "Να φωνάξουν βοήθεια", "Να αφήσουν το κανό"], 0, "Κρατηθείτε από το κανό, βάλτε τα πόδια μπροστά και περιμένετε"),
 ],
 "gloss": {"κανό": "κανό — canoe", "σωσίβιο": "σωσίβιο — life jacket", "κολυμβητές": "κολυμβητής — swimmer", "αδιάβροχες": "αδιάβροχος — waterproof", "ρεύματα": "ρεύμα — current, rapid", "κουπί": "κουπί — paddle", "αναποδογυρίσει": "αναποδογυρίζω — to capsize", "πανικοβληθείτε": "πανικοβάλλομαι — to panic"}
})

ITEMS.append({
 "id": "l143-rep-metaxeirismena", "title": "Ρούχα με δεύτερη ζωή", "title_en": "Clothes with a second life", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για την κατανάλωση.",
 "script": [
  L("Ρεπόρτερ", "m", "Μέχρι πριν από λίγα χρόνια, πολλοί στην Ελλάδα ντρέπονταν να φορέσουν ρούχα που είχε φορέσει κάποιος άλλος. Σήμερα τα καταστήματα με μεταχειρισμένα ρούχα πληθαίνουν, και οι εφαρμογές για αγοραπωλησία ρούχων έχουν εκατοντάδες χιλιάδες χρήστες.", "Until a few years ago, many people in Greece were ashamed to wear clothes someone else had worn. Today second-hand clothing shops are multiplying, and apps for buying and selling clothes have hundreds of thousands of users."),
  L("Ρεπόρτερ", "m", "Σύμφωνα με μια έρευνα αγοράς, οι μισοί σχεδόν αγοραστές είναι κάτω των τριάντα. Ως βασικούς λόγους αναφέρουν τις χαμηλές τιμές και την προστασία του περιβάλλοντος, αφού η παραγωγή ενός καινούργιου ρούχου απαιτεί μεγάλες ποσότητες νερού και ενέργειας.", "According to a market survey, almost half of buyers are under thirty. As their main reasons they cite low prices and protecting the environment, since producing a new garment requires large quantities of water and energy."),
  L("Ρεπόρτερ", "m", "Οι ειδικοί πάντως προειδοποιούν ότι η τάση έχει και μια σκοτεινή πλευρά: κάποιοι αγοράζουν περισσότερα από όσα χρειάζονται, επειδή είναι φτηνά, και τελικά τα ρούχα καταλήγουν πάλι στα σκουπίδια.", "Experts warn, though, that the trend also has a dark side: some people buy more than they need because it's cheap, and in the end the clothes end up in the rubbish again."),
 ],
 "questions": [
  Q("Τι ίσχυε μέχρι πριν από λίγα χρόνια;", ["Πολλοί ντρέπονταν να φορέσουν μεταχειρισμένα ρούχα", "Δεν υπήρχαν καταστήματα ρούχων", "Τα ρούχα ήταν πολύ φτηνά", "Όλοι αγόραζαν από εφαρμογές"], 0, "πολλοί στην Ελλάδα ντρέπονταν να φορέσουν ρούχα που είχε φορέσει κάποιος άλλος"),
  Q("Ποιους βασικούς λόγους αναφέρουν οι αγοραστές;", ["Τη μόδα και τις μάρκες", "Τις χαμηλές τιμές και την προστασία του περιβάλλοντος", "Την ποιότητα και την ποικιλία", "Τη συμβουλή των φίλων τους"], 1, "Ως βασικούς λόγους αναφέρουν τις χαμηλές τιμές και την προστασία του περιβάλλοντος"),
  Q("Ποια είναι, κατά τους ειδικούς, η σκοτεινή πλευρά της τάσης;", ["Τα ρούχα είναι βρόμικα", "Τα καταστήματα κλείνουν", "Κάποιοι αγοράζουν περισσότερα από όσα χρειάζονται", "Οι τιμές ανεβαίνουν"], 2, "κάποιοι αγοράζουν περισσότερα από όσα χρειάζονται"),
 ],
 "gloss": {"ντρέπονταν": "ντρέπομαι — to be ashamed", "μεταχειρισμένα": "μεταχειρισμένος — second-hand", "πληθαίνουν": "πληθαίνω — to multiply, increase", "αγοραπωλησία": "αγοραπωλησία — buying and selling", "χρήστες": "χρήστης — user", "ποσότητες": "ποσότητα — quantity", "τάση": "τάση — trend", "καταλήγουν": "καταλήγω — to end up"}
})

ITEMS.append({
 "id": "l143-dia-dema", "title": "Ένα δέμα για τον Καναδά", "title_en": "A parcel for Canada", "type": "dialogue", "level": "B2",
 "context_el": "Ένας πελάτης βρίσκεται στο ταχυδρομείο.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Θέλω να στείλω αυτό το δέμα στην αδερφή μου στο Τορόντο. Έχει μέσα μέλι, ένα βιβλίο και δυο πουλόβερ.", "Good morning. I want to send this parcel to my sister in Toronto. It has honey, a book and two jumpers inside."),
  L("Υπάλληλος", "f", "Για χώρες εκτός Ευρωπαϊκής Ένωσης πρέπει να συμπληρώσετε αυτό το τελωνειακό έντυπο: τι περιέχει το δέμα και πόση είναι περίπου η αξία κάθε πράγματος. Το μέλι επιτρέπεται, αλλά πρέπει να είναι σε κλειστό βάζο και καλά τυλιγμένο.", "For countries outside the European Union you must fill in this customs form: what the parcel contains and roughly how much each item is worth. Honey is allowed, but it must be in a sealed jar and well wrapped."),
  L("Πελάτης", "m", "Πόσο κάνει και πότε θα φτάσει;", "How much is it and when will it arrive?"),
  L("Υπάλληλος", "f", "Ζυγίζει τρία κιλά. Με την απλή αποστολή κάνει τριάντα οχτώ ευρώ και φτάνει σε δύο με τρεις εβδομάδες. Με την ταχεία είναι εβδομήντα ευρώ, σε πέντε εργάσιμες. Και στις δύο περιπτώσεις μπορείτε να το παρακολουθείτε στο διαδίκτυο με αυτόν τον αριθμό.", "It weighs three kilos. By standard post it's thirty-eight euros and arrives in two to three weeks. By express it's seventy euros, in five working days. In both cases you can track it online with this number."),
 ],
 "questions": [
  Q("Τι πρέπει να συμπληρώσει ο πελάτης;", ["Ένα τελωνειακό έντυπο με το περιεχόμενο και την αξία", "Μια αίτηση για διαβατήριο", "Μια δήλωση για τον φόρο", "Τίποτα"], 0, "πρέπει να συμπληρώσετε αυτό το τελωνειακό έντυπο"),
  Q("Τι ισχύει για το μέλι;", ["Απαγορεύεται", "Επιτρέπεται, αν είναι σε κλειστό βάζο και καλά τυλιγμένο", "Πρέπει να σταλεί χωριστά", "Επιτρέπεται μόνο με την ταχεία"], 1, "Το μέλι επιτρέπεται, αλλά πρέπει να είναι σε κλειστό βάζο και καλά τυλιγμένο"),
  Q("Πόσο κοστίζει η απλή αποστολή;", ["Εβδομήντα ευρώ", "Τρία ευρώ", "Τριάντα οχτώ ευρώ", "Πενήντα ευρώ"], 2, "Με την απλή αποστολή κάνει τριάντα οχτώ ευρώ"),
 ],
 "gloss": {"δέμα": "δέμα — parcel", "ταχυδρομείο": "ταχυδρομείο — post office", "τελωνειακό": "τελωνειακός — customs", "έντυπο": "έντυπο — form", "αξία": "αξία — value", "βάζο": "βάζο — jar", "τυλιγμένο": "τυλιγμένος — wrapped", "Ζυγίζει": "ζυγίζω — to weigh", "ταχεία": "ταχεία — express (post)", "εργάσιμες": "εργάσιμη — working day"}
})

ITEMS.append({
 "id": "l143-c1-olbers", "title": "Γιατί η νύχτα είναι σκοτεινή;", "title_en": "Why is the night dark?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ομιλία σε ένα πλανητάριο.",
 "script": [
  L("Αστρονόμος", "f", "Η ερώτηση μοιάζει παιδική: γιατί ο νυχτερινός ουρανός είναι σκοτεινός; Κι όμως, απασχόλησε σοβαρά τους αστρονόμους για αιώνες και έμεινε γνωστή ως «παράδοξο του Όλμπερς», από τον Γερμανό αστρονόμο Χάινριχ Όλμπερς, που τη διατύπωσε το 1823, αν και δεν ήταν ο πρώτος. Το επιχείρημα είναι το εξής: αν το σύμπαν ήταν άπειρο, αιώνιο και γεμάτο ομοιόμορφα με αστέρια, τότε, όπου κι αν κοιτάζαμε, το βλέμμα μας θα κατέληγε τελικά στην επιφάνεια κάποιου άστρου. Ολόκληρος ο ουρανός θα έπρεπε να λάμπει σαν τον Ήλιο.", "The question seems childish: why is the night sky dark? And yet it seriously occupied astronomers for centuries and became known as 'Olbers' paradox', after the German astronomer Heinrich Olbers, who formulated it in 1823, although he was not the first. The argument is this: if the universe were infinite, eternal and uniformly filled with stars, then wherever we looked, our line of sight would eventually end on the surface of some star. The whole sky ought to shine like the Sun."),
  L("Αστρονόμος", "f", "Η πρώτη εξήγηση που προτάθηκε ήταν ότι η σκόνη ανάμεσα στα άστρα απορροφά το φως. Δεν στέκει όμως: η σκόνη, απορροφώντας τόση ενέργεια, θα ζεσταινόταν και θα άρχιζε να λάμπει κι εκείνη. Παραδόξως, ο πρώτος που διατύπωσε κάτι κοντά στη σωστή απάντηση δεν ήταν επιστήμονας αλλά ποιητής: ο Έντγκαρ Άλαν Πόε, σε ένα δοκίμιο του 1848, υπέθεσε ότι το φως από τα πιο μακρινά άστρα δεν έχει προλάβει ακόμα να φτάσει σε εμάς.", "The first explanation proposed was that dust between the stars absorbs the light. But it doesn't hold: the dust, absorbing so much energy, would heat up and start to glow itself. Paradoxically, the first to formulate something close to the right answer was not a scientist but a poet: Edgar Allan Poe, in an essay of 1848, suggested that the light from the most distant stars has not yet had time to reach us."),
  L("Αστρονόμος", "f", "Σήμερα ξέρουμε ότι το σύμπαν έχει ηλικία περίπου δεκατεσσάρων δισεκατομμυρίων ετών, άρα βλέπουμε μόνο όσο φως πρόλαβε να ταξιδέψει μέχρι εδώ. Επιπλέον, το σύμπαν διαστέλλεται, και το φως των πολύ μακρινών γαλαξιών «τεντώνεται» προς μεγαλύτερα μήκη κύματος, πέρα από όσα βλέπει το μάτι μας. Με άλλα λόγια, το σκοτάδι της νύχτας είναι, με τον δικό του τρόπο, μια απόδειξη ότι το σύμπαν είχε αρχή.", "Today we know that the universe is about fourteen billion years old, so we see only as much light as has had time to travel here. Moreover, the universe is expanding, and the light of very distant galaxies is 'stretched' to longer wavelengths, beyond what our eye can see. In other words, the darkness of night is, in its own way, evidence that the universe had a beginning."),
 ],
 "questions": [
  Q("Τι θα συνέβαινε, σύμφωνα με το επιχείρημα, σε ένα άπειρο και αιώνιο σύμπαν γεμάτο αστέρια;", ["Ο ουρανός θα ήταν εντελώς μαύρος", "Ολόκληρος ο ουρανός θα έλαμπε σαν τον Ήλιο", "Τα άστρα θα έσβηναν", "Δεν θα υπήρχαν γαλαξίες"], 1, "Ολόκληρος ο ουρανός θα έπρεπε να λάμπει σαν τον Ήλιο"),
  Q("Γιατί δεν στέκει η εξήγηση με τη σκόνη;", ["Γιατί δεν υπάρχει σκόνη στο διάστημα", "Γιατί η σκόνη είναι πολύ λίγη", "Γιατί η σκόνη θα ζεσταινόταν και θα άρχιζε να λάμπει κι εκείνη", "Γιατί η σκόνη αντανακλά το φως"], 2, "θα ζεσταινόταν και θα άρχιζε να λάμπει κι εκείνη"),
  Q("Ποιος πλησίασε πρώτος στη σωστή απάντηση, κατά την ομιλήτρια;", ["Ο ποιητής Έντγκαρ Άλαν Πόε", "Ο ίδιος ο Όλμπερς", "Ο Νεύτωνας", "Ένας σύγχρονος αστρονόμος"], 0, "ο Έντγκαρ Άλαν Πόε"),
  Q("Τι δείχνει τελικά το σκοτάδι της νύχτας;", ["Ότι τα άστρα είναι λίγα", "Ότι το σύμπαν είναι άπειρο", "Ότι η σκόνη κρύβει το φως", "Ότι το σύμπαν είχε αρχή"], 3, "το σύμπαν είχε αρχή"),
 ],
 "gloss": {"πλανητάριο": "πλανητάριο — planetarium", "διατύπωσε": "διατυπώνω — to formulate", "άπειρο": "άπειρος — infinite", "αιώνιο": "αιώνιος — eternal", "ομοιόμορφα": "ομοιόμορφα — uniformly", "απορροφά": "απορροφώ — to absorb", "στέκει": "στέκει — it holds up (of an argument)", "δοκίμιο": "δοκίμιο — essay", "διαστέλλεται": "διαστέλλομαι — to expand", "μήκη κύματος": "μήκος κύματος — wavelength", "απόδειξη": "απόδειξη — proof, evidence"}
})

ITEMS.append({
 "id": "l143-c1-zipf", "title": "Ο νόμος του Ζιπφ", "title_en": "Zipf's law", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή για τη γλώσσα.",
 "script": [
  L("Δημοσιογράφος", "m", "Λένε ότι υπάρχει ένας μαθηματικός νόμος που ισχύει σχεδόν σε όλες τις γλώσσες. Τι ακριβώς περιγράφει;", "They say there is a mathematical law that holds in almost all languages. What exactly does it describe?"),
  L("Γλωσσολόγος", "f", "Πρόκειται για τον λεγόμενο νόμο του Ζιπφ, από τον Αμερικανό γλωσσολόγο Τζορτζ Ζιπφ, που τον έκανε γνωστό τη δεκαετία του 1930 και του 1940. Αν πάρετε ένα μεγάλο σύνολο κειμένων και κατατάξετε τις λέξεις από τη συχνότερη στη σπανιότερη, θα δείτε ότι η δεύτερη λέξη εμφανίζεται περίπου τις μισές φορές από την πρώτη, η τρίτη περίπου το ένα τρίτο, και ούτω καθεξής. Η συχνότητα μιας λέξης είναι, κατά προσέγγιση, αντιστρόφως ανάλογη της θέσης της στον κατάλογο.", "It's the so-called Zipf's law, after the American linguist George Zipf, who made it known in the 1930s and 1940s. If you take a large collection of texts and rank the words from the most frequent to the rarest, you'll see that the second word appears about half as often as the first, the third about a third as often, and so on. A word's frequency is, approximately, inversely proportional to its position on the list."),
  L("Δημοσιογράφος", "m", "Και τι σημαίνει αυτό για όποιον μαθαίνει μια ξένη γλώσσα;", "And what does that mean for someone learning a foreign language?"),
  L("Γλωσσολόγος", "f", "Σημαίνει ότι λίγες εκατοντάδες λέξεις, κυρίως άρθρα, προθέσεις και αντωνυμίες, καλύπτουν ένα πολύ μεγάλο μέρος κάθε κειμένου. Γι' αυτό η μάθηση με βάση τη συχνότητα έχει νόημα στην αρχή. Έχει όμως και έναν δυσάρεστο αντίκτυπο: όσο προχωράς, κάθε καινούργια λέξη που μαθαίνεις εμφανίζεται όλο και πιο σπάνια. Οι λέξεις που πραγματικά δίνουν νόημα σε ένα κείμενο συχνά βρίσκονται στη «μακριά ουρά» της κατανομής. Ο ίδιος ο Ζιπφ πρότεινε μια εξήγηση με βάση την «αρχή της ελάχιστης προσπάθειας», αλλά για το γιατί ακριβώς ισχύει ο νόμος οι επιστήμονες συζητούν ακόμη. Το εντυπωσιακό είναι ότι παρόμοιες κατανομές εμφανίζονται και αλλού, για παράδειγμα στους πληθυσμούς των πόλεων.", "It means that a few hundred words, mainly articles, prepositions and pronouns, cover a very large part of any text. That's why learning by frequency makes sense at the beginning. But it also has an unpleasant consequence: the further you go, each new word you learn appears more and more rarely. The words that really give meaning to a text are often in the 'long tail' of the distribution. Zipf himself proposed an explanation based on the 'principle of least effort', but scientists are still debating exactly why the law holds. What's striking is that similar distributions appear elsewhere too, for example in city populations."),
 ],
 "questions": [
  Q("Τι λέει ο νόμος του Ζιπφ;", ["Ότι όλες οι λέξεις εμφανίζονται εξίσου συχνά", "Ότι η συχνότητα μιας λέξης είναι περίπου αντιστρόφως ανάλογη της θέσης της στον κατάλογο", "Ότι οι μακριές λέξεις είναι πιο συχνές", "Ότι κάθε γλώσσα έχει τον ίδιο αριθμό λέξεων"], 1, "Η συχνότητα μιας λέξης είναι, κατά προσέγγιση, αντιστρόφως ανάλογη της θέσης της στον κατάλογο"),
  Q("Ποιες λέξεις καλύπτουν μεγάλο μέρος κάθε κειμένου;", ["Λίγες εκατοντάδες λέξεις, κυρίως άρθρα, προθέσεις και αντωνυμίες", "Τα ρήματα", "Οι επιστημονικοί όροι", "Τα επίθετα"], 0, "λίγες εκατοντάδες λέξεις, κυρίως άρθρα, προθέσεις και αντωνυμίες"),
  Q("Ποιος είναι ο «δυσάρεστος αντίκτυπος» για όποιον μαθαίνει μια γλώσσα;", ["Οι συχνές λέξεις ξεχνιούνται γρήγορα", "Η γραμματική γίνεται πιο δύσκολη", "Κάθε νέα λέξη εμφανίζεται όλο και πιο σπάνια", "Τα λεξικά είναι πολύ μεγάλα"], 2, "κάθε καινούργια λέξη που μαθαίνεις εμφανίζεται όλο και πιο σπάνια"),
  Q("Τι ισχύει για την εξήγηση του νόμου;", ["Ο Ζιπφ την απέδειξε οριστικά", "Ισχύει μόνο για τα αγγλικά", "Δεν ενδιαφέρει κανέναν", "Οι επιστήμονες συζητούν ακόμη γιατί ακριβώς ισχύει"], 3, "οι επιστήμονες συζητούν ακόμη"),
 ],
 "gloss": {"γλωσσολόγο": "γλωσσολόγος — linguist", "κατατάξετε": "κατατάσσω — to rank", "συχνότητα": "συχνότητα — frequency", "κατά προσέγγιση": "κατά προσέγγιση — approximately", "αντιστρόφως ανάλογη": "αντιστρόφως ανάλογος — inversely proportional", "αντωνυμίες": "αντωνυμία — pronoun", "αντίκτυπο": "αντίκτυπος — consequence, impact", "κατανομής": "κατανομή — distribution", "ελάχιστης": "ελάχιστος — least", "πληθυσμούς": "πληθυσμός — population"}
})

rnd = random.Random(143)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-143.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
