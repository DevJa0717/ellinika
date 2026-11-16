# Source for library/listening/listening-22.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l22.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l22-ann-skoupidia", "title": "Αλλαγές στην αποκομιδή απορριμμάτων", "title_en": "Changes to rubbish collection", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση του δήμου στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Ο δήμος ενημερώνει τους δημότες ότι από την πρώτη του επόμενου μήνα αλλάζει το πρόγραμμα αποκομιδής απορριμμάτων. Τα σκουπίδια θα μαζεύονται πλέον κάθε βράδυ μετά τις δέκα, αντί για τις πρωινές ώρες, ώστε να μην εμποδίζεται η κυκλοφορία.", "The council informs residents that from the first of next month the rubbish collection schedule is changing. Rubbish will now be collected every evening after ten, instead of in the morning hours, so that traffic is not obstructed."),
  L("Εκφωνητής", "m", "Παρακαλούμε να βγάζετε τις σακούλες μετά τις οχτώ το βράδυ και όχι νωρίτερα, για να αποφεύγονται οι δυσάρεστες μυρωδιές, ιδιαίτερα τους καλοκαιρινούς μήνες. Ο μπλε κάδος ανακύκλωσης θα αδειάζει δύο φορές την εβδομάδα, Τρίτη και Παρασκευή.", "Please put your bags out after eight in the evening and not earlier, to avoid unpleasant smells, especially in the summer months. The blue recycling bin will be emptied twice a week, Tuesday and Friday."),
  L("Εκφωνητής", "m", "Για ογκώδη αντικείμενα, όπως παλιά έπιπλα ή στρώματα, μην τα αφήνετε στο πεζοδρόμιο. Καλέστε στο τηλεφωνικό κέντρο του δήμου και κλείστε ραντεβού· η παραλαβή γίνεται δωρεάν μέσα σε τρεις εργάσιμες ημέρες.", "For bulky items, such as old furniture or mattresses, don't leave them on the pavement. Call the council's call centre and book an appointment; collection is free within three working days."),
 ],
 "questions": [
  Q("Γιατί αλλάζει η ώρα της αποκομιδής;", ["Για να μειωθεί το κόστος", "Για να μην εμποδίζεται η κυκλοφορία", "Γιατί το ζήτησαν οι εργαζόμενοι", "Λόγω καύσωνα"], 1, "ώστε να μην εμποδίζεται η κυκλοφορία"),
  Q("Πότε πρέπει να βγάζουν οι κάτοικοι τις σακούλες;", ["Το πρωί πριν από τη δουλειά", "Μετά τις οχτώ το βράδυ", "Μόνο την Τρίτη και την Παρασκευή", "Οποιαδήποτε ώρα"], 1, "να βγάζετε τις σακούλες μετά τις οχτώ το βράδυ"),
  Q("Τι πρέπει να κάνει κανείς με ένα παλιό στρώμα;", ["Να το αφήσει στο πεζοδρόμιο", "Να το πάει ο ίδιος στη χωματερή", "Να τηλεφωνήσει στον δήμο και να κλείσει ραντεβού", "Να το βάλει στον μπλε κάδο"], 2, "Καλέστε στο τηλεφωνικό κέντρο του δήμου και κλείστε ραντεβού"),
 ],
 "gloss": {"αποκομιδής απορριμμάτων": "αποκομιδή απορριμμάτων — rubbish collection", "δημότες": "δημότης — resident of a municipality", "εμποδίζεται": "εμποδίζομαι — to be obstructed", "σακούλες": "σακούλα — bag", "δυσάρεστες": "δυσάρεστος — unpleasant", "κάδος ανακύκλωσης": "κάδος ανακύκλωσης — recycling bin", "ογκώδη": "ογκώδης — bulky", "στρώματα": "στρώμα — mattress", "πεζοδρόμιο": "πεζοδρόμιο — pavement", "παραλαβή": "παραλαβή — collection, pick-up", "εργάσιμες": "εργάσιμος — working (day)"},
})

ITEMS.append({
 "id": "l22-vm-gamos", "title": "Μια πρόσκληση σε γάμο", "title_en": "A wedding invitation", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από μια φίλη.",
 "script": [
  L("Φίλη", "f", "Ελένη μου, γεια! Η Ρένα είμαι. Σου έστειλα την πρόσκληση με το ταχυδρομείο, αλλά φοβάμαι ότι μπορεί να πήγε στην παλιά σου διεύθυνση, γι' αυτό σε παίρνω. Παντρευόμαστε με τον Άρη στις είκοσι επτά Ιουνίου, στη Νάξο!", "Eleni, hi! It's Rena. I sent you the invitation by post, but I'm afraid it may have gone to your old address, that's why I'm calling. Aris and I are getting married on the twenty-seventh of June, on Naxos!"),
  L("Φίλη", "f", "Το μυστήριο θα γίνει σε ένα εκκλησάκι πάνω από τη θάλασσα στις επτά το απόγευμα, και μετά το γλέντι σε μια ταβέρνα στην παραλία. Θα χαρούμε πολύ να έρθεις και με τον Στέφανο, φυσικά.", "The ceremony will be in a little chapel above the sea at seven in the evening, and afterwards the party at a taverna on the beach. We'd be very happy if you came, and with Stefanos, of course."),
  L("Φίλη", "f", "Μια χάρη μόνο: πες μου μέχρι το τέλος του μήνα αν θα έρθετε, γιατί πρέπει να κλείσουμε δωμάτια, που τον Ιούνιο γεμίζουν γρήγορα. Και μη φέρετε δώρο· έχουμε φτιάξει μια λίστα για ένα ταξίδι, θα σου στείλω τα στοιχεία.", "Just one favour: tell me by the end of the month whether you're coming, because we have to book rooms, which fill up quickly in June. And don't bring a present; we've set up a list for a trip, I'll send you the details."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί η Ρένα;", ["Γιατί ακύρωσε τον γάμο", "Γιατί η πρόσκληση μπορεί να πήγε σε παλιά διεύθυνση", "Γιατί άλλαξε η ημερομηνία", "Γιατί χρειάζεται κουμπάρα"], 1, "φοβάμαι ότι μπορεί να πήγε στην παλιά σου διεύθυνση"),
  Q("Πού θα γίνει το γλέντι;", ["Σε ένα εκκλησάκι", "Σε ένα ξενοδοχείο στην Αθήνα", "Σε μια ταβέρνα στην παραλία", "Στο σπίτι του Άρη"], 2, "μετά το γλέντι σε μια ταβέρνα στην παραλία"),
  Q("Γιατί πρέπει να απαντήσει η Ελένη μέχρι το τέλος του μήνα;", ["Γιατί πρέπει να κλείσουν δωμάτια", "Γιατί τυπώνουν τα μενού", "Γιατί φεύγουν ταξίδι", "Γιατί πρέπει να αγοράσει δώρο"], 0, "γιατί πρέπει να κλείσουμε δωμάτια"),
 ],
 "gloss": {"πρόσκληση": "πρόσκληση — invitation", "Παντρευόμαστε": "παντρεύομαι — to get married", "μυστήριο": "μυστήριο — (church) ceremony, sacrament", "εκκλησάκι": "εκκλησάκι — little chapel", "γλέντι": "γλέντι — party, celebration", "χάρη": "χάρη — favour", "να κλείσουμε": "κλείνω — to book", "γεμίζουν": "γεμίζω — to fill up", "στοιχεία": "στοιχεία — details"},
})

ITEMS.append({
 "id": "l22-dia-trapeza", "title": "Ανοίγοντας λογαριασμό στην τράπεζα", "title_en": "Opening a bank account", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα κατάστημα τράπεζας.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Ήρθα πρόσφατα από τη Γερμανία για δουλειά και θα ήθελα να ανοίξω έναν λογαριασμό για να μπαίνει ο μισθός μου.", "Good morning. I came recently from Germany for work and I'd like to open an account for my salary to be paid into."),
  L("Υπάλληλος", "m", "Βεβαίως. Θα χρειαστώ το διαβατήριο ή την ταυτότητά σας, τον αριθμό φορολογικού μητρώου και ένα αποδεικτικό διεύθυνσης, για παράδειγμα έναν λογαριασμό ρεύματος ή το μισθωτήριο του σπιτιού σας. Έχετε κάποια βεβαίωση από τον εργοδότη σας;", "Of course. I'll need your passport or ID card, your tax number and proof of address, for example an electricity bill or your rental contract. Do you have a letter from your employer?"),
  L("Πελάτισσα", "f", "Έχω τη σύμβαση εργασίας. Λογαριασμό ρεύματος δεν έχω ακόμη, γιατί είναι στο όνομα του ιδιοκτήτη, αλλά έχω το μισθωτήριο. Υπάρχουν χρεώσεις για τη διατήρηση του λογαριασμού;", "I have my employment contract. I don't have an electricity bill yet, because it's in the landlord's name, but I have the rental contract. Are there charges for keeping the account?"),
  L("Υπάλληλος", "m", "Όταν ο λογαριασμός είναι μισθοδοσίας, δεν υπάρχει μηνιαία χρέωση. Η κάρτα θα σας έρθει ταχυδρομικά σε πέντε με επτά ημέρες, και τον κωδικό για την ηλεκτρονική τραπεζική θα τον λάβετε με μήνυμα στο κινητό σας.", "When it's a salary account, there's no monthly charge. The card will come to you by post in five to seven days, and you'll receive the code for online banking by text message on your mobile."),
 ],
 "questions": [
  Q("Γιατί θέλει να ανοίξει λογαριασμό η πελάτισσα;", ["Για να πάρει δάνειο", "Για να μπαίνει ο μισθός της", "Για να στέλνει χρήματα στη Γερμανία", "Για να αγοράσει σπίτι"], 1, "για να μπαίνει ο μισθός μου"),
  Q("Ποιο έγγραφο χρησιμοποιεί ως αποδεικτικό διεύθυνσης;", ["Τον λογαριασμό ρεύματος", "Το διαβατήριο", "Το μισθωτήριο", "Τη σύμβαση εργασίας"], 2, "έχω το μισθωτήριο"),
  Q("Πώς θα λάβει τον κωδικό για την ηλεκτρονική τραπεζική;", ["Με μήνυμα στο κινητό", "Με την κάρτα", "Από το κατάστημα", "Με email"], 0, "θα τον λάβετε με μήνυμα στο κινητό σας"),
 ],
 "gloss": {"λογαριασμό": "λογαριασμός — account; bill", "μισθός": "μισθός — salary", "αριθμό φορολογικού μητρώου": "αριθμός φορολογικού μητρώου (ΑΦΜ) — tax number", "αποδεικτικό διεύθυνσης": "αποδεικτικό διεύθυνσης — proof of address", "μισθωτήριο": "μισθωτήριο — rental contract", "βεβαίωση": "βεβαίωση — certificate, letter", "εργοδότη": "εργοδότης — employer", "σύμβαση εργασίας": "σύμβαση εργασίας — employment contract", "χρεώσεις": "χρέωση — charge", "διατήρηση": "διατήρηση — maintenance, keeping", "μισθοδοσίας": "μισθοδοσία — payroll", "ηλεκτρονική τραπεζική": "ηλεκτρονική τραπεζική — online banking"},
})

ITEMS.append({
 "id": "l22-dia-delfoi", "title": "Μια εκδρομή στους Δελφούς", "title_en": "A trip to Delphi", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια συζήτηση σε ένα τουριστικό γραφείο.",
 "script": [
  L("Πελάτης", "m", "Γεια σας. Θα θέλαμε να πάμε στους Δελφούς το Σάββατο, αλλά δεν έχουμε αυτοκίνητο. Τι μας προτείνετε;", "Hello. We'd like to go to Delphi on Saturday, but we don't have a car. What do you suggest?"),
  L("Υπάλληλος", "f", "Έχουμε μια οργανωμένη εκδρομή με πούλμαν. Φεύγει στις επτά και μισή το πρωί από την Ομόνοια και επιστρέφει γύρω στις επτά το βράδυ. Η τιμή περιλαμβάνει ξεναγό, εισιτήριο για τον αρχαιολογικό χώρο και το μουσείο, και μια στάση στην Αράχωβα.", "We have an organised coach trip. It leaves at half past seven in the morning from Omonia and returns at around seven in the evening. The price includes a guide, a ticket for the archaeological site and the museum, and a stop in Arachova."),
  L("Πελάτης", "m", "Και το φαγητό; Η γυναίκα μου είναι χορτοφάγος.", "And food? My wife is vegetarian."),
  L("Υπάλληλος", "f", "Το μεσημεριανό δεν περιλαμβάνεται, γιατί πολλοί προτιμούν να περπατήσουν στην Αράχωβα και να διαλέξουν μόνοι τους. Υπάρχουν πολλές ταβέρνες με επιλογές χωρίς κρέας. Σας συμβουλεύω πάντως να φορέσετε άνετα παπούτσια· ο χώρος είναι στην πλαγιά του βουνού και έχει πολύ ανέβασμα μέχρι το στάδιο.", "Lunch isn't included, because many people prefer to walk around Arachova and choose for themselves. There are lots of tavernas with meat-free options. But I'd advise you to wear comfortable shoes; the site is on the mountainside and there's a lot of climbing up to the stadium."),
 ],
 "questions": [
  Q("Τι περιλαμβάνει η τιμή της εκδρομής;", ["Ξεναγό, εισιτήρια και μια στάση στην Αράχωβα", "Το μεσημεριανό", "Διανυκτέρευση στους Δελφούς", "Μόνο τη μεταφορά"], 0, "Η τιμή περιλαμβάνει ξεναγό, εισιτήριο για τον αρχαιολογικό χώρο και το μουσείο, και μια στάση στην Αράχωβα"),
  Q("Γιατί δεν περιλαμβάνεται το μεσημεριανό;", ["Γιατί είναι ακριβό", "Γιατί πολλοί προτιμούν να διαλέξουν μόνοι τους", "Γιατί δεν υπάρχουν ταβέρνες", "Γιατί η εκδρομή είναι σύντομη"], 1, "πολλοί προτιμούν να περπατήσουν στην Αράχωβα και να διαλέξουν μόνοι τους"),
  Q("Γιατί τους συμβουλεύει να φορέσουν άνετα παπούτσια;", ["Γιατί θα κάνουν πεζοπορία στον Παρνασσό", "Γιατί ο χώρος είναι στην πλαγιά και έχει πολύ ανέβασμα", "Γιατί βρέχει", "Γιατί το πούλμαν σταματά μακριά"], 1, "ο χώρος είναι στην πλαγιά του βουνού και έχει πολύ ανέβασμα"),
 ],
 "gloss": {"τουριστικό γραφείο": "τουριστικό γραφείο — travel agency", "οργανωμένη": "οργανωμένος — organised", "πούλμαν": "πούλμαν — coach", "ξεναγό": "ξεναγός — tour guide", "αρχαιολογικό χώρο": "αρχαιολογικός χώρος — archaeological site", "στάση": "στάση — stop", "χορτοφάγος": "χορτοφάγος — vegetarian", "μεσημεριανό": "μεσημεριανό — lunch", "άνετα": "άνετος — comfortable", "πλαγιά": "πλαγιά — slope, mountainside", "ανέβασμα": "ανέβασμα — climb, uphill", "στάδιο": "στάδιο — stadium"},
})

ITEMS.append({
 "id": "l22-mon-marathonios", "title": "Ο πρώτος μου μαραθώνιος", "title_en": "My first marathon", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε μια γυναίκα να μιλάει για τον πρώτο μαραθώνιο που έτρεξε.",
 "script": [
  L("Δρομέας", "f", "Ξεκίνησα να τρέχω στα σαράντα, μετά από ένα διαζύγιο, απλώς για να βγαίνω από το σπίτι. Στην αρχή δεν μπορούσα να τρέξω ούτε δέκα λεπτά χωρίς να σταματήσω. Μια φίλη με έπεισε να γραφτώ σε μια ομάδα δρομέων στο πάρκο, και εκεί άλλαξαν όλα.", "I started running at forty, after a divorce, just to get out of the house. At first I couldn't run even ten minutes without stopping. A friend persuaded me to join a running group in the park, and that's where everything changed."),
  L("Δρομέας", "f", "Δύο χρόνια μετά, βρέθηκα στην αφετηρία του Αυθεντικού Μαραθωνίου, στον Μαραθώνα, με άλλους είκοσι χιλιάδες ανθρώπους. Η διαδρομή είναι δύσκολη, γιατί από το δέκατο ως το τριακοστό χιλιόμετρο έχει συνεχώς ανηφόρες. Γύρω στο τριακοστό πέμπτο ένιωσα ότι δεν θα τα καταφέρω.", "Two years later I found myself at the start of the Authentic Marathon, in Marathon, with twenty thousand other people. The route is hard, because from the tenth to the thirtieth kilometre it's constantly uphill. Around the thirty-fifth I felt I wouldn't make it."),
  L("Δρομέας", "f", "Τότε άκουσα έναν ηλικιωμένο κύριο στο πεζοδρόμιο να φωνάζει το όνομά μου, που ήταν γραμμένο στο νούμερό μου. Δεν τον ήξερα, αλλά με έκανε να συνεχίσω. Τερμάτισα στο Παναθηναϊκό Στάδιο σε πέντε ώρες. Αργά, το ξέρω, αλλά δεν ένιωσα ποτέ τόσο περήφανη.", "Then I heard an elderly man on the pavement shouting my name, which was written on my number. I didn't know him, but he made me keep going. I finished at the Panathenaic Stadium in five hours. Slow, I know, but I've never felt so proud."),
 ],
 "questions": [
  Q("Γιατί ξεκίνησε να τρέχει;", ["Για να χάσει βάρος", "Για να βγαίνει από το σπίτι μετά από ένα διαζύγιο", "Γιατί της το είπε ο γιατρός", "Για να τρέξει στον μαραθώνιο"], 1, "μετά από ένα διαζύγιο, απλώς για να βγαίνω από το σπίτι"),
  Q("Τι κάνει δύσκολη τη διαδρομή του Αυθεντικού Μαραθωνίου;", ["Η ζέστη", "Οι συνεχείς ανηφόρες από το δέκατο ως το τριακοστό χιλιόμετρο", "Ο πολύς κόσμος", "Τα στενά πεζοδρόμια"], 1, "από το δέκατο ως το τριακοστό χιλιόμετρο έχει συνεχώς ανηφόρες"),
  Q("Τι τη βοήθησε να συνεχίσει;", ["Μια φίλη που έτρεχε δίπλα της", "Ένας άγνωστος ηλικιωμένος που φώναζε το όνομά της", "Η μουσική στα ακουστικά", "Ο προπονητής της ομάδας"], 1, "άκουσα έναν ηλικιωμένο κύριο στο πεζοδρόμιο να φωνάζει το όνομά μου"),
 ],
 "gloss": {"διαζύγιο": "διαζύγιο — divorce", "με έπεισε": "πείθω — to persuade", "να γραφτώ": "γράφομαι — to sign up, join", "δρομέων": "δρομέας — runner", "αφετηρία": "αφετηρία — start (line)", "διαδρομή": "διαδρομή — route", "ανηφόρες": "ανηφόρα — uphill stretch", "θα τα καταφέρω": "τα καταφέρνω — to manage, make it", "νούμερό": "νούμερο — (race) number", "Τερμάτισα": "τερματίζω — to finish (a race)", "περήφανη": "περήφανος — proud"},
})

ITEMS.append({
 "id": "l22-rep-meteora", "title": "Τα Μετέωρα", "title_en": "Meteora", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από τα Μετέωρα.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρισκόμαστε πάνω από την Καλαμπάκα, ανάμεσα σε γιγάντιους βράχους που υψώνονται απότομα από τον θεσσαλικό κάμπο. Πάνω στις κορυφές τους, από τον δέκατο τέταρτο αιώνα και μετά, μοναχοί έχτισαν μοναστήρια, αναζητώντας την ησυχία και την ασφάλεια μακριά από τον κόσμο.", "We are above Kalambaka, among gigantic rocks that rise steeply from the Thessalian plain. On their summits, from the fourteenth century onwards, monks built monasteries, seeking quiet and safety far from the world."),
  L("Ρεπόρτερ", "f", "Κάποτε υπήρχαν πάνω από είκοσι μονές· σήμερα λειτουργούν έξι. Για αιώνες, ο μόνος τρόπος για να ανέβει κανείς ήταν με σκοινένιες σκάλες ή μέσα σε ένα δίχτυ που το τραβούσαν με βαρούλκο. Τα σκαλοπάτια που χρησιμοποιούν σήμερα οι επισκέπτες σκαλίστηκαν στον βράχο μόλις τον εικοστό αιώνα.", "There were once more than twenty monasteries; today six are active. For centuries the only way up was by rope ladders or inside a net hauled up with a winch. The steps visitors use today were cut into the rock only in the twentieth century."),
  L("Ρεπόρτερ", "f", "Από το 1988 τα Μετέωρα είναι μνημείο παγκόσμιας κληρονομιάς της UNESCO και δέχονται περισσότερους από ένα εκατομμύριο επισκέπτες τον χρόνο. Οι μοναχοί ζητούν από τους επισκέπτες σεμνό ντύσιμο: οι γυναίκες πρέπει να φορούν φούστα, την οποία μπορούν να δανειστούν στην είσοδο.", "Since 1988 Meteora has been a UNESCO World Heritage site and receives more than a million visitors a year. The monks ask visitors for modest dress: women must wear a skirt, which they can borrow at the entrance."),
 ],
 "questions": [
  Q("Γιατί έχτισαν οι μοναχοί τα μοναστήρια στις κορυφές των βράχων;", ["Για να βλέπουν τη θάλασσα", "Αναζητώντας την ησυχία και την ασφάλεια μακριά από τον κόσμο", "Γιατί ο κάμπος πλημμύριζε", "Για να προσελκύσουν επισκέπτες"], 1, "αναζητώντας την ησυχία και την ασφάλεια μακριά από τον κόσμο"),
  Q("Πώς ανέβαινε κανείς στα μοναστήρια για αιώνες;", ["Με τελεφερίκ", "Με σκοινένιες σκάλες ή μέσα σε ένα δίχτυ", "Από σκαλοπάτια στον βράχο", "Με άλογα"], 1, "με σκοινένιες σκάλες ή μέσα σε ένα δίχτυ που το τραβούσαν με βαρούλκο"),
  Q("Τι ζητούν οι μοναχοί από τις γυναίκες επισκέπτριες;", ["Να μη φωτογραφίζουν", "Να φορούν φούστα", "Να πληρώνουν διπλό εισιτήριο", "Να μη μιλούν"], 1, "οι γυναίκες πρέπει να φορούν φούστα"),
 ],
 "gloss": {"γιγάντιους": "γιγάντιος — gigantic", "βράχους": "βράχος — rock", "υψώνονται": "υψώνομαι — to rise", "απότομα": "απότομα — steeply, abruptly", "κάμπο": "κάμπος — plain", "μοναχοί": "μοναχός — monk", "μονές": "μονή — monastery", "σκοινένιες": "σκοινένιος — (made of) rope", "δίχτυ": "δίχτυ — net", "βαρούλκο": "βαρούλκο — winch", "σκαλίστηκαν": "σκαλίζομαι — to be carved", "μνημείο παγκόσμιας κληρονομιάς": "μνημείο παγκόσμιας κληρονομιάς — World Heritage site", "σεμνό": "σεμνός — modest", "να δανειστούν": "δανείζομαι — to borrow"},
})

ITEMS.append({
 "id": "l22-rep-samothraki", "title": "Η Σαμοθράκη", "title_en": "Samothrace", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τη Σαμοθράκη σε μια ταξιδιωτική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "m", "Η Σαμοθράκη, στο βόρειο Αιγαίο, δεν μοιάζει με τα νησιά των καρτ ποστάλ. Δεν έχει μεγάλες αμμουδιές ούτε πολυτελή ξενοδοχεία. Έχει όμως το Φεγγάρι, ένα βουνό πάνω από χίλια εξακόσια μέτρα, από τα ψηλότερα στα νησιά του Αιγαίου, και δεκάδες ρυάκια που σχηματίζουν καταρράκτες και φυσικές λίμνες, τις λεγόμενες βάθρες.", "Samothrace, in the northern Aegean, doesn't look like the postcard islands. It has no big sandy beaches or luxury hotels. But it has Fengari, a mountain over one thousand six hundred metres, one of the highest in the Aegean islands, and dozens of streams that form waterfalls and natural pools, the so-called vathres."),
  L("Ρεπόρτερ", "m", "Στην αρχαιότητα το νησί ήταν φημισμένο για το Ιερό των Μεγάλων Θεών, όπου γίνονταν μυστικές τελετές. Εκεί βρέθηκε το 1863 η περίφημη Νίκη της Σαμοθράκης, το άγαλμα που σήμερα στέκεται στην κορυφή μιας σκάλας στο Λούβρο. Στο τοπικό μουσείο οι επισκέπτες βλέπουν ένα αντίγραφο.", "In antiquity the island was famous for the Sanctuary of the Great Gods, where secret rites took place. It was there that the famous Victory of Samothrace was found in 1863, the statue that today stands at the top of a staircase in the Louvre. In the local museum visitors see a copy."),
  L("Ρεπόρτερ", "m", "Πολλοί κάτοικοι θέλουν να μείνει το νησί όπως είναι. Τα τελευταία χρόνια έχουν αντισταθεί σε σχέδια για μεγάλες ξενοδοχειακές μονάδες και προτιμούν τον ήπιο τουρισμό: κάμπινγκ, πεζοπορία και μικρούς ξενώνες.", "Many residents want the island to stay as it is. In recent years they have resisted plans for large hotel complexes and prefer gentle tourism: camping, hiking and small guesthouses."),
 ],
 "questions": [
  Q("Τι είναι οι βάθρες;", ["Αρχαίοι ναοί", "Φυσικές λίμνες που σχηματίζουν τα ρυάκια", "Αμμουδιές", "Παραδοσιακά σπίτια"], 1, "δεκάδες ρυάκια που σχηματίζουν καταρράκτες και φυσικές λίμνες, τις λεγόμενες βάθρες"),
  Q("Πού βρίσκεται σήμερα η αυθεντική Νίκη της Σαμοθράκης;", ["Στο τοπικό μουσείο", "Στο Λούβρο", "Στην Αθήνα", "Στο Ιερό των Μεγάλων Θεών"], 1, "στέκεται στην κορυφή μιας σκάλας στο Λούβρο"),
  Q("Τι είδους τουρισμό προτιμούν πολλοί κάτοικοι;", ["Μεγάλα ξενοδοχεία", "Κρουαζιέρες", "Ήπιο τουρισμό, όπως κάμπινγκ και πεζοπορία", "Νυχτερινή διασκέδαση"], 2, "προτιμούν τον ήπιο τουρισμό: κάμπινγκ, πεζοπορία και μικρούς ξενώνες"),
 ],
 "gloss": {"καρτ ποστάλ": "καρτ ποστάλ — postcard", "αμμουδιές": "αμμουδιά — sandy beach", "πολυτελή": "πολυτελής — luxury", "ρυάκια": "ρυάκι — stream", "καταρράκτες": "καταρράκτης — waterfall", "βάθρες": "βάθρα — natural rock pool", "Ιερό": "ιερό — sanctuary", "τελετές": "τελετή — ceremony, rite", "άγαλμα": "άγαλμα — statue", "αντίγραφο": "αντίγραφο — copy", "έχουν αντισταθεί": "αντιστέκομαι — to resist", "ξενοδοχειακές μονάδες": "ξενοδοχειακή μονάδα — hotel complex", "ήπιο": "ήπιος — mild, gentle", "ξενώνες": "ξενώνας — guesthouse"},
})

ITEMS.append({
 "id": "l22-int-tachydromos", "title": "Ο ταχυδρόμος του νησιού", "title_en": "The island postman", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με έναν ταχυδρόμο σε ένα μικρό νησί.",
 "script": [
  L("Δημοσιογράφος", "f", "Πόσα χρόνια μοιράζετε γράμματα στο νησί;", "How many years have you been delivering letters on the island?"),
  L("Ταχυδρόμος", "m", "Είκοσι δύο. Όταν ξεκίνησα, κουβαλούσα κυρίως γράμματα και κάρτες· οι ξενιτεμένοι έγραφαν στους γονείς τους κάθε εβδομάδα. Σήμερα τα γράμματα είναι ελάχιστα. Μοιράζω κυρίως δέματα από ηλεκτρονικές αγορές και λογαριασμούς.", "Twenty-two. When I started, I carried mainly letters and cards; emigrants wrote to their parents every week. Today letters are very few. I mainly deliver parcels from online shopping and bills."),
  L("Δημοσιογράφος", "f", "Λένε ότι για τους ηλικιωμένους είστε κάτι παραπάνω από ταχυδρόμος.", "They say that for elderly people you're something more than a postman."),
  L("Ταχυδρόμος", "m", "Ε, σε ένα χωριό με σαράντα κατοίκους, κάποιος πρέπει να ρωτήσει αν είσαι καλά. Πολλές φορές τους φέρνω φάρμακα από το φαρμακείο της Χώρας ή τους διαβάζω ένα έγγραφο από την εφορία που δεν καταλαβαίνουν. Κάποτε βρήκα μια κυρία πεσμένη στην αυλή της και κάλεσα το κέντρο υγείας. Από τότε, όταν δεν με βλέπει μια μέρα, ανησυχεί εκείνη για μένα.", "Well, in a village with forty residents, someone has to ask if you're all right. Often I bring them medicine from the pharmacy in the main town or read them a document from the tax office that they don't understand. Once I found a lady fallen in her yard and called the health centre. Since then, when she doesn't see me one day, she's the one who worries about me."),
 ],
 "questions": [
  Q("Τι μοιράζει κυρίως σήμερα ο ταχυδρόμος;", ["Γράμματα από ξενιτεμένους", "Δέματα από ηλεκτρονικές αγορές και λογαριασμούς", "Εφημερίδες", "Κάρτες"], 1, "Μοιράζω κυρίως δέματα από ηλεκτρονικές αγορές και λογαριασμούς"),
  Q("Πώς βοηθά τους ηλικιωμένους;", ["Τους πηγαίνει στον γιατρό με το αυτοκίνητό του", "Τους φέρνει φάρμακα και τους διαβάζει έγγραφα", "Τους μαγειρεύει", "Τους πληρώνει τους λογαριασμούς"], 1, "τους φέρνω φάρμακα από το φαρμακείο της Χώρας ή τους διαβάζω ένα έγγραφο"),
  Q("Τι άλλαξε μετά το περιστατικό με την κυρία που έπεσε;", ["Εκείνη ανησυχεί για τον ταχυδρόμο όταν δεν τον βλέπει", "Μετακόμισε στη Χώρα", "Ο ταχυδρόμος άλλαξε δρομολόγιο", "Ο δήμος έφτιαξε κέντρο υγείας"], 0, "όταν δεν με βλέπει μια μέρα, ανησυχεί εκείνη για μένα"),
 ],
 "gloss": {"ταχυδρόμο": "ταχυδρόμος — postman", "μοιράζετε": "μοιράζω — to deliver, distribute", "κουβαλούσα": "κουβαλάω — to carry", "ξενιτεμένοι": "ξενιτεμένος — emigrant (living abroad)", "ελάχιστα": "ελάχιστος — very few, minimal", "δέματα": "δέμα — parcel", "ηλεκτρονικές αγορές": "ηλεκτρονική αγορά — online purchase", "Χώρας": "Χώρα — main town of an island", "έγγραφο": "έγγραφο — document", "εφορία": "εφορία — tax office", "πεσμένη": "πεσμένος — fallen", "αυλή": "αυλή — yard", "κέντρο υγείας": "κέντρο υγείας — health centre"},
})

ITEMS.append({
 "id": "l22-mon-kapodistrias", "title": "Ο Ιωάννης Καποδίστριας", "title_en": "Ioannis Kapodistrias", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για τον πρώτο κυβερνήτη της Ελλάδας.",
 "script": [
  L("Ιστορικός", "f", "Ο Ιωάννης Καποδίστριας γεννήθηκε στην Κέρκυρα το 1776 και σπούδασε ιατρική στην Πάντοβα. Η καριέρα του όμως εξελίχθηκε στη διπλωματία: μπήκε στην υπηρεσία του τσάρου και έφτασε να γίνει υπουργός Εξωτερικών της Ρωσίας, θέση που μοιραζόταν με τον Νέσελροντ. Συνέβαλε μάλιστα καθοριστικά στη διαμόρφωση του ελβετικού ομοσπονδιακού συστήματος.", "Ioannis Kapodistrias was born in Corfu in 1776 and studied medicine in Padua. His career, however, developed in diplomacy: he entered the Tsar's service and rose to become Russia's foreign minister, a post he shared with Nesselrode. He even made a decisive contribution to shaping the Swiss federal system."),
  L("Ιστορικός", "f", "Όταν το 1827 η Εθνοσυνέλευση της Τροιζήνας τον εξέλεξε κυβερνήτη, βρήκε μια χώρα κατεστραμμένη, χωρίς ταμείο, χωρίς στρατό, χωρίς διοίκηση. Έφτασε στο Ναύπλιο τον Ιανουάριο του 1828 και αρνήθηκε κάθε μισθό. Ίδρυσε σχολεία, οργάνωσε την πρώτη εθνική τράπεζα και κυκλοφόρησε το πρώτο νόμισμα, τον φοίνικα.", "When in 1827 the National Assembly of Troezen elected him governor, he found a country in ruins, with no treasury, no army, no administration. He arrived in Nafplio in January 1828 and refused any salary. He founded schools, organised the first national bank and issued the first currency, the phoenix."),
  L("Ιστορικός", "f", "Το συγκεντρωτικό του ύφος, ωστόσο, τον έφερε σε σύγκρουση με τους προκρίτους και τους οπλαρχηγούς, που είχαν συνηθίσει να ασκούν τοπική εξουσία. Η σύγκρουση με τους Μαυρομιχαλαίους της Μάνης κορυφώθηκε όταν ο Καποδίστριας φυλάκισε τον Πετρόμπεη. Τον Οκτώβριο του 1831, ο αδελφός και ο γιος του Πετρόμπεη τον δολοφόνησαν έξω από την εκκλησία του Αγίου Σπυρίδωνα στο Ναύπλιο.", "His centralising style, however, brought him into conflict with the notables and chieftains, who had grown used to exercising local power. The conflict with the Mavromichalis family of Mani came to a head when Kapodistrias imprisoned Petrobey. In October 1831, Petrobey's brother and son assassinated him outside the church of Saint Spyridon in Nafplio."),
  L("Ιστορικός", "f", "Μέχρι σήμερα οι ιστορικοί διαφωνούν: για άλλους ήταν ένας οραματιστής που θεμελίωσε το σύγχρονο κράτος, για άλλους ένας αυταρχικός ηγέτης που αγνόησε τις φιλελεύθερες επιδιώξεις της Επανάστασης. Πιθανότατα ήταν και τα δύο.", "To this day historians disagree: for some he was a visionary who laid the foundations of the modern state, for others an authoritarian leader who ignored the liberal aspirations of the Revolution. Most probably he was both."),
 ],
 "questions": [
  Q("Σε ποιον τομέα εξελίχθηκε η καριέρα του Καποδίστρια πριν γίνει κυβερνήτης;", ["Στην ιατρική", "Στη διπλωματία", "Στο εμπόριο", "Στον στρατό"], 1, "Η καριέρα του όμως εξελίχθηκε στη διπλωματία"),
  Q("Ποια από τα παρακάτω έκανε ως κυβερνήτης;", ["Δέχτηκε υψηλό μισθό", "Ίδρυσε σχολεία και κυκλοφόρησε το πρώτο νόμισμα", "Μετέφερε την πρωτεύουσα στην Αθήνα", "Διέλυσε τα σχολεία"], 1, "Ίδρυσε σχολεία, οργάνωσε την πρώτη εθνική τράπεζα και κυκλοφόρησε το πρώτο νόμισμα"),
  Q("Γιατί ήρθε σε σύγκρουση με τους προκρίτους και τους οπλαρχηγούς;", ["Γιατί ήταν ξένος", "Λόγω του συγκεντρωτικού του ύφους", "Γιατί αύξησε τους φόρους", "Γιατί υποστήριζε την Αγγλία"], 1, "Το συγκεντρωτικό του ύφος, ωστόσο, τον έφερε σε σύγκρουση"),
  Q("Ποια είναι η τελική εκτίμηση της ιστορικού;", ["Ότι ήταν μόνο αυταρχικός", "Ότι ήταν μόνο οραματιστής", "Ότι πιθανότατα ήταν και οραματιστής και αυταρχικός", "Ότι δεν έπαιξε σημαντικό ρόλο"], 2, "Πιθανότατα ήταν και τα δύο"),
 ],
 "gloss": {"κυβερνήτη": "κυβερνήτης — governor", "εξελίχθηκε": "εξελίσσομαι — to develop, evolve", "διπλωματία": "διπλωματία — diplomacy", "τσάρου": "τσάρος — tsar", "Συνέβαλε": "συμβάλλω — to contribute", "καθοριστικά": "καθοριστικά — decisively", "ομοσπονδιακού": "ομοσπονδιακός — federal", "Εθνοσυνέλευση": "εθνοσυνέλευση — national assembly", "κατεστραμμένη": "κατεστραμμένος — ruined, destroyed", "ταμείο": "ταμείο — treasury", "διοίκηση": "διοίκηση — administration", "νόμισμα": "νόμισμα — currency, coin", "συγκεντρωτικό": "συγκεντρωτικός — centralising", "σύγκρουση": "σύγκρουση — conflict", "ασκούν": "ασκώ — to exercise (power)", "κορυφώθηκε": "κορυφώνομαι — to come to a head, peak", "φυλάκισε": "φυλακίζω — to imprison", "δολοφόνησαν": "δολοφονώ — to assassinate", "οραματιστής": "οραματιστής — visionary", "θεμελίωσε": "θεμελιώνω — to lay the foundations of", "αυταρχικός": "αυταρχικός — authoritarian", "επιδιώξεις": "επιδίωξη — aim, aspiration"},
})

ITEMS.append({
 "id": "l22-int-nomades", "title": "Ψηφιακοί νομάδες στα νησιά", "title_en": "Digital nomads on the islands", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με έναν κοινωνιολόγο για τους ψηφιακούς νομάδες.",
 "script": [
  L("Δημοσιογράφος", "f", "Τα τελευταία χρόνια όλο και περισσότεροι ξένοι επαγγελματίες ζουν σε ελληνικά νησιά και δουλεύουν από απόσταση. Είναι ευλογία ή απειλή για τις τοπικές κοινωνίες;", "In recent years more and more foreign professionals live on Greek islands and work remotely. Is this a blessing or a threat for local communities?"),
  L("Κοινωνιολόγος", "m", "Εξαρτάται από το πώς θα το διαχειριστούμε. Από τη μία, οι ψηφιακοί νομάδες μένουν μήνες, όχι μέρες, ξοδεύουν τα χρήματά τους στην τοπική αγορά και, το σημαντικότερο, έρχονται και τον χειμώνα, όταν τα νησιά ερημώνουν. Σε ορισμένα χωριά, χάρη σε αυτούς, κράτησε ανοιχτά το καφενείο ή ακόμη και το σχολείο.", "It depends on how we manage it. On the one hand, digital nomads stay for months, not days, spend their money in the local economy and, most importantly, come in winter too, when the islands empty out. In some villages, thanks to them, the café or even the school stayed open."),
  L("Δημοσιογράφος", "f", "Και από την άλλη;", "And on the other hand?"),
  L("Κοινωνιολόγος", "m", "Από την άλλη, οι μισθοί τους είναι συχνά τριπλάσιοι από τους ντόπιους, κι αυτό ανεβάζει τα ενοίκια σε επίπεδα που ένας δάσκαλος ή μια νοσηλεύτρια δεν μπορούν να πληρώσουν. Υπάρχει και ο κίνδυνος να δημιουργηθούν παράλληλες κοινότητες, που ζουν στο νησί χωρίς να συνδέονται με αυτό, χωρίς να μαθαίνουν ούτε δυο λέξεις ελληνικά.", "On the other hand, their salaries are often three times those of locals, and that pushes rents to levels a teacher or a nurse can't pay. There's also the risk of parallel communities forming, living on the island without connecting with it, without learning even a couple of words of Greek."),
  L("Κοινωνιολόγος", "m", "Η λύση δεν είναι να τους διώξουμε, αλλά να τους εντάξουμε: κίνητρα για μακροχρόνιες μισθώσεις σε ντόπιους, μαθήματα γλώσσας, συμμετοχή στη ζωή του τόπου. Ένας νομάδας που μαθαίνει να χορεύει στο πανηγύρι του χωριού δεν είναι πια απλώς επισκέπτης.", "The solution is not to drive them away but to integrate them: incentives for long-term lets to locals, language classes, participation in local life. A nomad who learns to dance at the village festival is no longer just a visitor."),
 ],
 "questions": [
  Q("Ποιο θεωρεί ο κοινωνιολόγος το σημαντικότερο θετικό στοιχείο;", ["Ότι ξοδεύουν πολλά χρήματα", "Ότι έρχονται και τον χειμώνα, όταν τα νησιά ερημώνουν", "Ότι μιλούν πολλές γλώσσες", "Ότι αγοράζουν σπίτια"], 1, "το σημαντικότερο, έρχονται και τον χειμώνα, όταν τα νησιά ερημώνουν"),
  Q("Ποια συνέπεια έχουν οι υψηλοί μισθοί τους;", ["Ανεβάζουν τα ενοίκια σε επίπεδα απρόσιτα για τους ντόπιους", "Αυξάνουν τους μισθούς των ντόπιων", "Μειώνουν την ανεργία", "Φέρνουν περισσότερους τουρίστες"], 0, "αυτό ανεβάζει τα ενοίκια σε επίπεδα που ένας δάσκαλος ή μια νοσηλεύτρια δεν μπορούν να πληρώσουν"),
  Q("Τι εννοεί με τον όρο «παράλληλες κοινότητες»;", ["Ομάδες που ζουν στο νησί χωρίς να συνδέονται με αυτό", "Χωριά που χτίζονται για ξένους", "Συνεταιρισμούς ντόπιων", "Διαδικτυακές ομάδες"], 0, "ζουν στο νησί χωρίς να συνδέονται με αυτό"),
  Q("Ποια λύση προτείνει;", ["Να περιοριστεί η είσοδός τους", "Να πληρώνουν υψηλότερους φόρους", "Να ενταχθούν στην τοπική κοινωνία", "Να μένουν μόνο το καλοκαίρι"], 2, "Η λύση δεν είναι να τους διώξουμε, αλλά να τους εντάξουμε"),
 ],
 "gloss": {"κοινωνιολόγο": "κοινωνιολόγος — sociologist", "ψηφιακούς νομάδες": "ψηφιακός νομάδας — digital nomad", "από απόσταση": "από απόσταση — remotely", "ευλογία": "ευλογία — blessing", "απειλή": "απειλή — threat", "διαχειριστούμε": "διαχειρίζομαι — to manage", "ερημώνουν": "ερημώνω — to become deserted", "τριπλάσιοι": "τριπλάσιος — three times as much", "ντόπιους": "ντόπιος — local", "ενοίκια": "ενοίκιο — rent", "παράλληλες κοινότητες": "παράλληλη κοινότητα — parallel community", "να συνδέονται": "συνδέομαι — to connect, be linked", "να τους διώξουμε": "διώχνω — to drive away", "να τους εντάξουμε": "εντάσσω — to integrate", "κίνητρα": "κίνητρο — incentive", "μακροχρόνιες μισθώσεις": "μακροχρόνια μίσθωση — long-term let", "πανηγύρι": "πανηγύρι — village festival"},
})
rnd = random.Random(22)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-22.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
