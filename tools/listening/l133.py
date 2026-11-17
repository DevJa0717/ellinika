# Source for library/listening/listening-133.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l133.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l133-ann-proti-kyriaki", "title": "Ελεύθερη είσοδος στα μουσεία την Κυριακή", "title_en": "Free entry to museums on Sunday", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε στο ραδιόφωνο μια ανακοίνωση της Εφορείας Αρχαιοτήτων της πόλης σας.",
 "script": [
  L("Εκφωνητής", "m", "Η Εφορεία Αρχαιοτήτων υπενθυμίζει ότι αυτή την Κυριακή, πρώτη του μήνα, η είσοδος στον αρχαιολογικό χώρο και στο Αρχαιολογικό Μουσείο της πόλης θα είναι ελεύθερη για όλους τους επισκέπτες.", "The Ephorate of Antiquities reminds the public that this Sunday, the first of the month, entry to the archaeological site and the city's Archaeological Museum will be free for all visitors."),
  L("Εκφωνητής", "m", "Λόγω της αυξημένης προσέλευσης που αναμένεται, οι ομάδες άνω των δεκαπέντε ατόμων θα πρέπει να έχουν κλείσει ραντεβού τηλεφωνικώς έως την Παρασκευή. Οι επισκέπτες παρακαλούνται να μην αφήνουν σακίδια και ομπρέλες στην γκαρνταρόμπα, η οποία θα παραμείνει κλειστή.", "Because of the increased attendance expected, groups of more than fifteen people must have booked a time slot by phone by Friday. Visitors are asked not to bring backpacks and umbrellas for the cloakroom, which will remain closed."),
  L("Εκφωνητής", "m", "Στις έντεκα και στις δώδεκα το μεσημέρι θα πραγματοποιηθούν δωρεάν ξεναγήσεις για οικογένειες με παιδιά. Ο αρχαιολογικός χώρος κλείνει στις πέντε, και η τελευταία είσοδος επιτρέπεται μισή ώρα νωρίτερα.", "At eleven and twelve noon there will be free guided tours for families with children. The archaeological site closes at five, and last entry is allowed half an hour earlier."),
 ],
 "questions": [
  Q("Τι ισχύει αυτή την Κυριακή;", ["Ο αρχαιολογικός χώρος θα είναι κλειστός", "Η είσοδος θα είναι ελεύθερη για όλους", "Θα πληρώνουν μόνο οι ξένοι", "Το μουσείο θα ανοίξει νωρίτερα"], 1, "η είσοδος στον αρχαιολογικό χώρο και στο Αρχαιολογικό Μουσείο της πόλης θα είναι ελεύθερη για όλους τους επισκέπτες"),
  Q("Τι πρέπει να κάνουν οι μεγάλες ομάδες;", ["Να πληρώσουν ειδικό εισιτήριο", "Να έρθουν πριν από τις έντεκα", "Να κλείσουν ραντεβού τηλεφωνικώς έως την Παρασκευή", "Να έχουν μαζί τους ξεναγό"], 2, "οι ομάδες άνω των δεκαπέντε ατόμων θα πρέπει να έχουν κλείσει ραντεβού τηλεφωνικώς έως την Παρασκευή"),
  Q("Μέχρι τι ώρα μπορεί κανείς να μπει στον αρχαιολογικό χώρο;", ["Μέχρι τις τεσσερισήμισι", "Μέχρι τις πέντε", "Μέχρι τις δώδεκα", "Μέχρι τις πεντέμισι"], 0, "η τελευταία είσοδος επιτρέπεται μισή ώρα νωρίτερα"),
 ],
 "gloss": {"Εφορεία Αρχαιοτήτων": "Εφορεία Αρχαιοτήτων — Ephorate (regional service) of Antiquities", "υπενθυμίζει": "υπενθυμίζω — to remind", "αρχαιολογικό χώρο": "αρχαιολογικός χώρος — archaeological site", "ελεύθερη": "ελεύθερη είσοδος — free entry", "προσέλευσης": "προσέλευση — attendance, turnout", "αναμένεται": "αναμένεται — is expected", "τηλεφωνικώς": "τηλεφωνικώς — by phone", "σακίδια": "σακίδιο — backpack", "γκαρνταρόμπα": "γκαρνταρόμπα — cloakroom", "πραγματοποιηθούν": "πραγματοποιούμαι — to take place", "ξεναγήσεις": "ξενάγηση — guided tour"}
})

ITEMS.append({
 "id": "l133-vm-dermatologos", "title": "Μήνυμα από τη δερματολόγο", "title_en": "A message from the dermatologist", "type": "voicemail", "level": "B2",
 "context_el": "Πριν από λίγες μέρες κάνατε έλεγχο σπίλων σε μια δερματολόγο. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Γιατρός", "f", "Καλησπέρα, η Ρένα Λιάπη είμαι, η δερματολόγος. Σας τηλεφωνώ για τα αποτελέσματα του ελέγχου που κάναμε την Τρίτη. Καταρχάς, μην ανησυχείτε: όλοι οι σπίλοι είναι καλοήθεις.", "Good evening, this is Rena Liapi, the dermatologist. I'm calling about the results of the check-up we did on Tuesday. First of all, don't worry: all the moles are benign."),
  L("Γιατρός", "f", "Υπάρχει μόνο ένας, αυτός στην πλάτη, που έχει ακανόνιστο σχήμα και τον τρίβει το λουρί της τσάντας σας. Προτείνω να τον αφαιρέσουμε προληπτικά. Είναι μια απλή επέμβαση με τοπική αναισθησία, κρατάει περίπου είκοσι λεπτά.", "There's just one, the one on your back, which has an irregular shape and is rubbed by your bag strap. I suggest we remove it as a precaution. It's a simple procedure under local anaesthetic; it takes about twenty minutes."),
  L("Γιατρός", "f", "Θα ήταν καλύτερα να γίνει πριν από το καλοκαίρι, γιατί μετά την επέμβαση πρέπει να αποφύγετε τον ήλιο για έναν μήνα. Πάρτε τη γραμματεία μου να κλείσετε ραντεβού. Γεια σας.", "It would be better to do it before the summer, because after the procedure you must avoid the sun for a month. Call my receptionist to book an appointment. Goodbye."),
 ],
 "questions": [
  Q("Τι έδειξε ο έλεγχος;", ["Ότι χρειάζεται νέα εξέταση", "Ότι όλοι οι σπίλοι είναι καλοήθεις", "Ότι υπάρχει ένα σοβαρό πρόβλημα", "Ότι τα αποτελέσματα δεν βγήκαν ακόμη"], 1, "όλοι οι σπίλοι είναι καλοήθεις"),
  Q("Γιατί προτείνει η γιατρός να αφαιρεθεί ο σπίλος της πλάτης;", ["Γιατί είναι επικίνδυνος", "Γιατί μεγαλώνει γρήγορα", "Γιατί έχει ακανόνιστο σχήμα και τον τρίβει το λουρί της τσάντας", "Γιατί το ζήτησε ο ασθενής"], 2, "έχει ακανόνιστο σχήμα και τον τρίβει το λουρί της τσάντας σας"),
  Q("Γιατί είναι καλύτερα να γίνει η επέμβαση πριν από το καλοκαίρι;", ["Γιατί μετά πρέπει να αποφεύγεται ο ήλιος για έναν μήνα", "Γιατί η γιατρός φεύγει διακοπές", "Γιατί το καλοκαίρι κοστίζει περισσότερο", "Γιατί η αναισθησία δεν γίνεται με ζέστη"], 0, "μετά την επέμβαση πρέπει να αποφύγετε τον ήλιο για έναν μήνα"),
 ],
 "gloss": {"δερματολόγο": "δερματολόγος — dermatologist", "σπίλων": "σπίλος — mole", "καλοήθεις": "καλοήθης — benign", "ακανόνιστο": "ακανόνιστος — irregular", "τρίβει": "τρίβω — to rub", "λουρί": "λουρί — strap", "αφαιρέσουμε": "αφαιρώ — to remove", "προληπτικά": "προληπτικά — as a precaution", "επέμβαση": "επέμβαση — (surgical) procedure", "τοπική αναισθησία": "τοπική αναισθησία — local anaesthetic", "γραμματεία": "γραμματεία — reception, secretary's office"}
})

ITEMS.append({
 "id": "l133-dial-ektos-sezon", "title": "Διακοπές τον Νοέμβριο;", "title_en": "A holiday in November?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φίλες συζητούν πότε να κάνουν διακοπές σε ένα νησί.",
 "script": [
  L("Δέσποινα", "f", "Λέω φέτος να μην πάμε στο νησί τον Αύγουστο. Πέρσι πληρώσαμε το δωμάτιο όσο ένα μηνιάτικο, και στην παραλία δεν έβρισκες μέρος να απλώσεις πετσέτα.", "I'm thinking this year we shouldn't go to the island in August. Last year we paid as much as a month's wages for the room, and on the beach you couldn't find a spot to lay down a towel."),
  L("Στέλλα", "f", "Και πότε να πάμε; Τον Νοέμβριο; Θα είναι όλα κλειστά, και η θάλασσα παγωμένη.", "So when should we go? In November? Everything will be closed, and the sea freezing."),
  L("Δέσποινα", "f", "Όχι όλα. Ρώτησα: τα περισσότερα καφενεία και μερικές ταβέρνες μένουν ανοιχτά, γιατί εκεί ζουν άνθρωποι όλο τον χρόνο. Και η θάλασσα τον Οκτώβριο είναι ακόμα ζεστή, πιο ζεστή απ' ό,τι τον Ιούνιο.", "Not everything. I asked: most cafés and some tavernas stay open, because people live there all year round. And in October the sea is still warm, warmer than in June."),
  L("Στέλλα", "f", "Τον Οκτώβριο, λοιπόν, όχι τον Νοέμβριο. Εντάξει, με έπεισες. Μόνο να ελέγξουμε τα πλοία, γιατί τον χειμώνα τα δρομολόγια είναι λιγότερα.", "October, then, not November. OK, you've convinced me. We just need to check the ferries, because in winter there are fewer sailings."),
 ],
 "questions": [
  Q("Γιατί δεν θέλει η Δέσποινα να πάνε τον Αύγουστο;", ["Γιατί κάνει πολλή ζέστη", "Γιατί είναι ακριβά και έχει πολύ κόσμο", "Γιατί δουλεύει τον Αύγουστο", "Γιατί δεν της αρέσει η θάλασσα"], 1, "πληρώσαμε το δωμάτιο όσο ένα μηνιάτικο, και στην παραλία δεν έβρισκες μέρος"),
  Q("Τι λέει η Δέσποινα για τη θάλασσα τον Οκτώβριο;", ["Ότι είναι πολύ κρύα", "Ότι έχει μεγάλα κύματα", "Ότι είναι πιο ζεστή απ' ό,τι τον Ιούνιο", "Ότι είναι πιο καθαρή"], 2, "πιο ζεστή απ' ό,τι τον Ιούνιο"),
  Q("Τι πρέπει να ελέγξουν, σύμφωνα με τη Στέλλα;", ["Τα δρομολόγια των πλοίων", "Τις τιμές των ξενοδοχείων", "Τον καιρό", "Αν είναι ανοιχτές οι παραλίες"], 0, "να ελέγξουμε τα πλοία, γιατί τον χειμώνα τα δρομολόγια είναι λιγότερα"),
 ],
 "gloss": {"μηνιάτικο": "μηνιάτικο — a month's wages", "απλώσεις": "απλώνω — to spread out", "πετσέτα": "πετσέτα — towel", "παγωμένη": "παγωμένος — freezing", "καφενεία": "καφενείο — traditional café", "όλο τον χρόνο": "όλο τον χρόνο — all year round", "με έπεισες": "πείθω — to convince", "δρομολόγια": "δρομολόγιο — (scheduled) sailing, route"}
})

ITEMS.append({
 "id": "l133-int-ergotherapeftria", "title": "Μια εργοθεραπεύτρια", "title_en": "An occupational therapist", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια ραδιοφωνική συνέντευξη με μια εργοθεραπεύτρια που δουλεύει σε ένα κέντρο αποκατάστασης.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί δεν ξέρουν τι κάνει ένας εργοθεραπευτής. Πώς θα το εξηγούσατε;", "Many people don't know what an occupational therapist does. How would you explain it?"),
  L("Εργοθεραπεύτρια", "f", "Βοηθάμε ανθρώπους να ξανακάνουν τις καθημερινές τους δραστηριότητες μετά από ένα ατύχημα ή μια ασθένεια. Να ντυθούν, να μαγειρέψουν, να γράψουν, να γυρίσουν στη δουλειά τους. Ο φυσικοθεραπευτής δουλεύει την κίνηση· εμείς δουλεύουμε τη ζωή που θα κάνει ο άνθρωπος με αυτή την κίνηση.", "We help people get back to their everyday activities after an accident or an illness. Getting dressed, cooking, writing, going back to work. The physiotherapist works on movement; we work on the life the person will live with that movement."),
  L("Δημοσιογράφος", "m", "Θυμάστε κάποιον ασθενή που σας συγκίνησε;", "Do you remember a patient who moved you?"),
  L("Εργοθεραπεύτρια", "f", "Έναν ζαχαροπλάστη που είχε πάθει εγκεφαλικό και δεν μπορούσε να κουνήσει το δεξί του χέρι. Δουλέψαμε μήνες με απλές ασκήσεις, πλάθοντας ζύμη. Την ημέρα που μου έφερε ένα ταψί κουλουράκια που είχε φτιάξει μόνος του, κλάψαμε και οι δύο.", "A pastry chef who had had a stroke and couldn't move his right hand. We worked for months with simple exercises, kneading dough. The day he brought me a tray of biscuits he had made by himself, we both cried."),
 ],
 "questions": [
  Q("Με τι ασχολείται ένας εργοθεραπευτής;", ["Με τη θεραπεία του πόνου με φάρμακα", "Βοηθά ανθρώπους να ξανακάνουν τις καθημερινές τους δραστηριότητες", "Βρίσκει δουλειά σε ανέργους", "Κάνει χειρουργικές επεμβάσεις"], 1, "Βοηθάμε ανθρώπους να ξανακάνουν τις καθημερινές τους δραστηριότητες"),
  Q("Πώς διαφέρει, κατά την ίδια, από τον φυσικοθεραπευτή;", ["Δουλεύει μόνο με παιδιά", "Δουλεύει μόνο σε νοσοκομεία", "Ο φυσικοθεραπευτής δουλεύει την κίνηση, εκείνη τη ζωή με αυτή την κίνηση", "Δεν υπάρχει καμία διαφορά"], 2, "Ο φυσικοθεραπευτής δουλεύει την κίνηση· εμείς δουλεύουμε τη ζωή που θα κάνει ο άνθρωπος με αυτή την κίνηση"),
  Q("Τι έφερε ο ζαχαροπλάστης στην εργοθεραπεύτρια;", ["Ένα ταψί κουλουράκια που είχε φτιάξει μόνος του", "Μια τούρτα γενεθλίων", "Ένα ευχαριστήριο γράμμα", "Λουλούδια"], 0, "μου έφερε ένα ταψί κουλουράκια που είχε φτιάξει μόνος του"),
 ],
 "gloss": {"εργοθεραπεύτρια": "εργοθεραπεύτρια — occupational therapist (f.)", "αποκατάστασης": "αποκατάσταση — rehabilitation", "δραστηριότητες": "δραστηριότητα — activity", "φυσικοθεραπευτής": "φυσικοθεραπευτής — physiotherapist", "συγκίνησε": "συγκινώ — to move, touch", "ζαχαροπλάστη": "ζαχαροπλάστης — pastry chef", "εγκεφαλικό": "εγκεφαλικό — stroke", "πλάθοντας": "πλάθω — to knead, shape", "ζύμη": "ζύμη — dough", "ταψί": "ταψί — baking tray", "κουλουράκια": "κουλουράκι — (Greek) biscuit"}
})

ITEMS.append({
 "id": "l133-rep-kouklotheatro", "title": "Ένα κουκλοθέατρο που ταξιδεύει", "title_en": "A travelling puppet theatre", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα κουκλοθέατρο που επισκέπτεται τα χωριά της Ηπείρου.",
 "script": [
  L("Ρεπόρτερ", "f", "Ένα παλιό φορτηγάκι, βαμμένο κόκκινο, σταματά στην πλατεία ενός χωριού στα Τζουμέρκα. Σε λίγα λεπτά η καρότσα του έχει γίνει σκηνή. Είναι το κουκλοθέατρο της Ευτυχίας και του Παύλου, δύο ηθοποιών που εδώ και πέντε χρόνια γυρίζουν τα ορεινά χωριά της Ηπείρου.", "An old pickup truck, painted red, stops in the square of a village in the Tzoumerka mountains. In a few minutes its back has become a stage. It's the puppet theatre of Eftychia and Pavlos, two actors who for five years have been touring the mountain villages of Epirus."),
  L("Ρεπόρτερ", "f", "Τις κούκλες τις φτιάχνουν μόνοι τους, από ξύλο και παλιά υφάσματα που τους χαρίζουν οι κάτοικοι. Οι ιστορίες τους βασίζονται σε παραμύθια της περιοχής, που τα έχουν καταγράψει από τους ηλικιωμένους.", "They make the puppets themselves, from wood and old fabrics given to them by the locals. Their stories are based on folk tales of the area, which they have recorded from the elderly."),
  L("Ρεπόρτερ", "f", "Στις παραστάσεις έρχονται όχι μόνο τα λίγα παιδιά των χωριών, αλλά και οι παππούδες τους, που συχνά αναγνωρίζουν τις ιστορίες και τις διορθώνουν φωναχτά. «Αυτό είναι το καλύτερο κομμάτι», λέει η Ευτυχία γελώντας.", "Not only the few village children come to the shows, but also their grandparents, who often recognise the stories and correct them out loud. 'That's the best part,' says Eftychia, laughing."),
 ],
 "questions": [
  Q("Πού γίνονται οι παραστάσεις;", ["Σε ένα θέατρο στα Γιάννενα", "Στην καρότσα ενός φορτηγού, στις πλατείες των χωριών", "Στα σχολεία της πόλης", "Σε ένα πανηγύρι μία φορά τον χρόνο"], 1, "η καρότσα του έχει γίνει σκηνή"),
  Q("Από τι φτιάχνονται οι κούκλες;", ["Από πλαστικό", "Από χαρτί", "Από ξύλο και παλιά υφάσματα", "Από πηλό"], 2, "από ξύλο και παλιά υφάσματα που τους χαρίζουν οι κάτοικοι"),
  Q("Τι κάνουν συχνά οι παππούδες στις παραστάσεις;", ["Διορθώνουν φωναχτά τις ιστορίες", "Φεύγουν στη μέση", "Βοηθούν στο στήσιμο της σκηνής", "Πληρώνουν τα εισιτήρια των παιδιών"], 0, "συχνά αναγνωρίζουν τις ιστορίες και τις διορθώνουν φωναχτά"),
 ],
 "gloss": {"κουκλοθέατρο": "κουκλοθέατρο — puppet theatre", "φορτηγάκι": "φορτηγάκι — pickup, small truck", "καρότσα": "καρότσα — truck bed", "σκηνή": "σκηνή — stage", "κούκλες": "κούκλα — puppet, doll", "υφάσματα": "ύφασμα — fabric", "χαρίζουν": "χαρίζω — to give (as a gift)", "παραμύθια": "παραμύθι — fairy tale, folk tale", "καταγράψει": "καταγράφω — to record, write down", "φωναχτά": "φωναχτά — out loud"}
})

ITEMS.append({
 "id": "l133-rep-scholikos-doryforos", "title": "Ένας δορυφόρος από ένα σχολείο", "title_en": "A satellite from a school", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για μια ομάδα μαθητών που κατασκευάζει έναν μικρό δορυφόρο.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο εργαστήριο φυσικής ενός λυκείου, δώδεκα μαθητές σκύβουν πάνω από έναν κύβο που χωράει στην παλάμη. Είναι ένας μικροδορυφόρος, και, αν όλα πάνε καλά, του χρόνου θα βρίσκεται σε τροχιά γύρω από τη Γη.", "In the physics lab of a high school, twelve pupils lean over a cube that fits in the palm of a hand. It is a small satellite, and, if all goes well, next year it will be in orbit around the Earth."),
  L("Ρεπόρτερ", "m", "Η ομάδα δουλεύει δύο χρόνια στο πλαίσιο ενός ευρωπαϊκού εκπαιδευτικού προγράμματος. Ο δορυφόρος θα μετράει τη θερμοκρασία και την υγρασία της ατμόσφαιρας, και τα δεδομένα θα τα λαμβάνει μια κεραία στην ταράτσα του σχολείου.", "The team has been working for two years as part of a European education programme. The satellite will measure the temperature and humidity of the atmosphere, and the data will be received by an antenna on the school roof."),
  L("Ρεπόρτερ", "m", "«Το πιο δύσκολο δεν ήταν τα ηλεκτρονικά», λέει μια μαθήτρια. «Ήταν να μάθουμε να δουλεύουμε σαν ομάδα, να μοιράζουμε τις ευθύνες και να δεχόμαστε τα λάθη μας.» Τρεις από τα μέλη της ομάδας σκοπεύουν πλέον να σπουδάσουν μηχανικοί.", "'The hardest thing wasn't the electronics,' says a pupil. 'It was learning to work as a team, share responsibilities and accept our mistakes.' Three of the team members now plan to study engineering."),
 ],
 "questions": [
  Q("Πόσο μεγάλος είναι ο δορυφόρος;", ["Όσο ένα αυτοκίνητο", "Χωράει στην παλάμη", "Όσο ένα ψυγείο", "Όσο μια τάξη"], 1, "έναν κύβο που χωράει στην παλάμη"),
  Q("Τι θα μετράει ο δορυφόρος;", ["Τους σεισμούς", "Την ποιότητα του νερού", "Τη θερμοκρασία και την υγρασία της ατμόσφαιρας", "Την κίνηση των πλοίων"], 2, "θα μετράει τη θερμοκρασία και την υγρασία της ατμόσφαιρας"),
  Q("Τι ήταν το πιο δύσκολο, σύμφωνα με τη μαθήτρια;", ["Να μάθουν να δουλεύουν σαν ομάδα", "Τα ηλεκτρονικά", "Να βρουν χρήματα", "Να γράψουν το πρόγραμμα"], 0, "Ήταν να μάθουμε να δουλεύουμε σαν ομάδα"),
 ],
 "gloss": {"δορυφόρο": "δορυφόρος — satellite", "εργαστήριο": "εργαστήριο — laboratory", "σκύβουν": "σκύβω — to lean over, bend", "κύβο": "κύβος — cube", "παλάμη": "παλάμη — palm (of the hand)", "μικροδορυφόρος": "μικροδορυφόρος — small satellite", "τροχιά": "τροχιά — orbit", "υγρασία": "υγρασία — humidity", "δεδομένα": "δεδομένα — data", "κεραία": "κεραία — antenna", "ευθύνες": "ευθύνη — responsibility"}
})

ITEMS.append({
 "id": "l133-mono-logariasmoi", "title": "Γιατί έκλεισα τους λογαριασμούς μου στα κοινωνικά δίκτυα", "title_en": "Why I closed my social media accounts", "type": "monologue", "level": "B2",
 "context_el": "Ένας νέος άντρας μιλά σε ένα πόντκαστ για την απόφασή του να φύγει από τα κοινωνικά δίκτυα.",
 "script": [
  L("Άρης", "m", "Ένα βράδυ κοίταξα στο κινητό πόσες ώρες την ημέρα περνούσα στις εφαρμογές. Ήταν πάνω από τέσσερις. Τέσσερις ώρες την ημέρα, σκέφτηκα, είναι σχεδόν δύο μήνες τον χρόνο. Την επόμενη μέρα έκλεισα όλους τους λογαριασμούς μου.", "One evening I checked on my phone how many hours a day I spent in the apps. It was more than four. Four hours a day, I thought, is almost two months a year. The next day I closed all my accounts."),
  L("Άρης", "m", "Οι πρώτες εβδομάδες ήταν δύσκολες. Έπιανα το κινητό χωρίς λόγο, από συνήθεια. Ένιωθα και ότι έχανα τι γινόταν στις ζωές των φίλων μου. Μετά όμως άρχισα να τους τηλεφωνώ, και τελικά βρισκόμαστε πιο συχνά από πριν.", "The first weeks were hard. I'd pick up my phone for no reason, out of habit. I also felt I was missing what was happening in my friends' lives. But then I started phoning them, and in the end we meet more often than before."),
  L("Άρης", "m", "Δεν λέω ότι τα κοινωνικά δίκτυα είναι κακά. Για τη δουλειά μου, για παράδειγμα, θα μου ήταν χρήσιμα. Απλώς εγώ δεν μπορούσα να τα χρησιμοποιώ με μέτρο. Τώρα διαβάζω περισσότερο και κοιμάμαι καλύτερα.", "I'm not saying social media are bad. For my job, for example, they would be useful to me. It's just that I couldn't use them in moderation. Now I read more and sleep better."),
 ],
 "questions": [
  Q("Τι τον έκανε να κλείσει τους λογαριασμούς του;", ["Ένα πρόβλημα στη δουλειά", "Είδε ότι περνούσε πάνω από τέσσερις ώρες την ημέρα στις εφαρμογές", "Του το ζήτησε η κοπέλα του", "Του χάλασε το κινητό"], 1, "Ήταν πάνω από τέσσερις"),
  Q("Τι άλλαξε στη σχέση του με τους φίλους του;", ["Έχασε επαφή μαζί τους", "Τους στέλνει πια μόνο μηνύματα", "Βρίσκονται πιο συχνά από πριν", "Τσακώθηκε με πολλούς"], 2, "τελικά βρισκόμαστε πιο συχνά από πριν"),
  Q("Ποια είναι η άποψή του για τα κοινωνικά δίκτυα;", ["Δεν είναι κακά, αλλά ο ίδιος δεν μπορούσε να τα χρησιμοποιεί με μέτρο", "Πρέπει να απαγορευτούν", "Είναι χρήσιμα μόνο για τους νέους", "Είναι η καλύτερη εφεύρεση της εποχής μας"], 0, "Δεν λέω ότι τα κοινωνικά δίκτυα είναι κακά"),
 ],
 "gloss": {"λογαριασμούς": "λογαριασμός — account", "κοινωνικά δίκτυα": "κοινωνικά δίκτυα — social media", "πόντκαστ": "πόντκαστ — podcast", "εφαρμογές": "εφαρμογή — app", "συνήθεια": "συνήθεια — habit", "έχανα": "χάνω — to miss, lose", "με μέτρο": "με μέτρο — in moderation"}
})

ITEMS.append({
 "id": "l133-mono-fovos-ptisis", "title": "Πώς ξεπέρασα τον φόβο της πτήσης", "title_en": "How I got over my fear of flying", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα διηγείται σε μια ραδιοφωνική εκπομπή πώς ξεπέρασε τον φόβο της για το αεροπλάνο.",
 "script": [
  L("Ναταλία", "f", "Για χρόνια δεν έμπαινα σε αεροπλάνο. Όταν ο αδερφός μου παντρεύτηκε στη Βαρκελώνη, πήγα με τρένα και πλοία, ένα ταξίδι τριών ημερών. Όλοι γελούσαν, αλλά εμένα μου κοβόταν η ανάσα μόνο στη σκέψη της απογείωσης.", "For years I wouldn't get on a plane. When my brother got married in Barcelona, I went by train and ferry, a three-day journey. Everyone laughed, but I'd lose my breath just at the thought of take-off."),
  L("Ναταλία", "f", "Κάποια στιγμή γράφτηκα σε ένα σεμινάριο που οργάνωνε μια αεροπορική εταιρεία μαζί με ψυχολόγους. Ένας πιλότος μάς εξήγησε τι είναι οι αναταράξεις και γιατί δεν είναι επικίνδυνες, και μάθαμε ασκήσεις αναπνοής.", "At some point I signed up for a seminar organised by an airline together with psychologists. A pilot explained to us what turbulence is and why it isn't dangerous, and we learned breathing exercises."),
  L("Ναταλία", "f", "Στο τέλος του σεμιναρίου κάναμε όλοι μαζί μια σύντομη πτήση, Αθήνα–Θεσσαλονίκη. Κρατούσα το χέρι της διπλανής μου σε όλη τη διαδρομή, αλλά τα κατάφερα. Πέρσι πήγα για πρώτη φορά μόνη μου στη Λισαβόνα.", "At the end of the seminar we all took a short flight together, Athens–Thessaloniki. I held the hand of the woman next to me the whole way, but I made it. Last year I went to Lisbon on my own for the first time."),
 ],
 "questions": [
  Q("Πώς πήγε στον γάμο του αδερφού της;", ["Δεν πήγε καθόλου", "Με τρένα και πλοία", "Με αυτοκίνητο", "Με αεροπλάνο, παίρνοντας χάπια"], 1, "πήγα με τρένα και πλοία"),
  Q("Τι τους εξήγησε ο πιλότος στο σεμινάριο;", ["Πώς οδηγείται ένα αεροπλάνο", "Πώς να κλείνουν φτηνά εισιτήρια", "Τι είναι οι αναταράξεις και γιατί δεν είναι επικίνδυνες", "Τι να κάνουν σε περίπτωση ατυχήματος"], 2, "τι είναι οι αναταράξεις και γιατί δεν είναι επικίνδυνες"),
  Q("Τι έγινε στο τέλος του σεμιναρίου;", ["Έκαναν όλοι μαζί μια σύντομη πτήση", "Πήρε πιστοποιητικό", "Πήγε μόνη της στη Λισαβόνα", "Έγινε η ίδια εκπαιδεύτρια"], 0, "κάναμε όλοι μαζί μια σύντομη πτήση"),
 ],
 "gloss": {"ξεπέρασε": "ξεπερνώ — to get over, overcome", "μου κοβόταν η ανάσα": "κόβεται η ανάσα μου — I lose my breath", "απογείωσης": "απογείωση — take-off", "σεμινάριο": "σεμινάριο — seminar, course", "αεροπορική εταιρεία": "αεροπορική εταιρεία — airline", "αναταράξεις": "αναταράξεις — turbulence", "ασκήσεις αναπνοής": "ασκήσεις αναπνοής — breathing exercises", "διπλανής": "διπλανός — the person next to one", "τα κατάφερα": "τα καταφέρνω — to manage, make it"}
})

ITEMS.append({
 "id": "l133-c1-petrov", "title": "Ο άνθρωπος που δεν σήμανε συναγερμό", "title_en": "The man who did not raise the alarm", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη για τα αυτοματοποιημένα συστήματα και την ανθρώπινη κρίση.",
 "script": [
  L("Ομιλητής", "m", "Τα ξημερώματα της 26ης Σεπτεμβρίου 1983, ο αντισυνταγματάρχης Στανισλάβ Πετρόφ είχε υπηρεσία σε ένα κέντρο έγκαιρης προειδοποίησης κοντά στη Μόσχα. Ξαφνικά, οι οθόνες έδειξαν ότι από τις Ηνωμένες Πολιτείες είχε εκτοξευθεί ένας πύραυλος και, λίγο αργότερα, ακόμη τέσσερις.", "In the early hours of 26 September 1983, Lieutenant Colonel Stanislav Petrov was on duty at an early-warning centre near Moscow. Suddenly, the screens showed that a missile had been launched from the United States and, a little later, four more."),
  L("Ομιλητής", "m", "Το πρωτόκολλο ήταν σαφές: έπρεπε να ενημερώσει αμέσως τους ανωτέρους του, κάτι που, σε μια περίοδο έντονης έντασης ανάμεσα στις δύο υπερδυνάμεις, θα μπορούσε να οδηγήσει σε αντίποινα. Ο Πετρόφ, όμως, δίστασε. Μια αμερικανική επίθεση, σκέφτηκε, δεν θα ξεκινούσε με πέντε μόνο πυραύλους, και τα επίγεια ραντάρ δεν είχαν εντοπίσει τίποτα.", "The protocol was clear: he had to inform his superiors immediately, something that, at a time of intense tension between the two superpowers, could have led to retaliation. Petrov, however, hesitated. An American attack, he thought, would not begin with only five missiles, and the ground radars had detected nothing."),
  L("Ομιλητής", "m", "Ανέφερε λοιπόν το περιστατικό ως βλάβη του συστήματος, και είχε δίκιο. Όπως αποδείχθηκε αργότερα, οι δορυφόροι είχαν ερμηνεύσει λανθασμένα την αντανάκλαση του ήλιου πάνω σε σύννεφα. Το επεισόδιο έμεινε μυστικό για χρόνια και έγινε γνωστό μόλις στη δεκαετία του 1990.", "So he reported the incident as a system malfunction, and he was right. As was later shown, the satellites had misinterpreted the reflection of the sun on clouds. The episode remained secret for years and only became known in the 1990s."),
  L("Ομιλητής", "m", "Γιατί μας ενδιαφέρει σήμερα; Γιατί όσο πιο αξιόπιστα φαίνονται τα αυτοματοποιημένα συστήματα, τόσο πιο εύκολα τους εμπιστευόμαστε τυφλά. Η περίπτωση Πετρόφ μάς θυμίζει ότι η κρίση ενός ανθρώπου που αμφιβάλλει μπορεί, σε κρίσιμες στιγμές, να αξίζει περισσότερο από τη βεβαιότητα μιας μηχανής.", "Why does it interest us today? Because the more reliable automated systems appear, the more easily we trust them blindly. The Petrov case reminds us that the judgement of a person who doubts may, at critical moments, be worth more than the certainty of a machine."),
 ],
 "questions": [
  Q("Τι έδειξαν οι οθόνες εκείνο το ξημέρωμα;", ["Ότι ένα αεροπλάνο είχε μπει στον εναέριο χώρο", "Ότι είχαν εκτοξευθεί πύραυλοι από τις Ηνωμένες Πολιτείες", "Ότι είχε γίνει σεισμός", "Ότι ένας δορυφόρος είχε πέσει"], 1, "είχε εκτοξευθεί ένας πύραυλος και, λίγο αργότερα, ακόμη τέσσερις"),
  Q("Γιατί δίστασε ο Πετρόφ;", ["Γιατί δεν ήξερε το πρωτόκολλο", "Γιατί δεν μπορούσε να επικοινωνήσει με τους ανωτέρους του", "Γιατί μια επίθεση δεν θα ξεκινούσε με πέντε πυραύλους και τα ραντάρ δεν είχαν εντοπίσει τίποτα", "Γιατί φοβόταν να τιμωρηθεί"], 2, "δεν θα ξεκινούσε με πέντε μόνο πυραύλους, και τα επίγεια ραντάρ δεν είχαν εντοπίσει τίποτα"),
  Q("Τι είχε προκαλέσει τον ψευδή συναγερμό;", ["Η αντανάκλαση του ήλιου πάνω σε σύννεφα", "Μια δοκιμή του αμερικανικού στρατού", "Μια διακοπή ρεύματος", "Ένα λάθος του Πετρόφ"], 0, "είχαν ερμηνεύσει λανθασμένα την αντανάκλαση του ήλιου πάνω σε σύννεφα"),
  Q("Ποιο είναι το συμπέρασμα του ομιλητή;", ["Ότι οι μηχανές δεν κάνουν ποτέ λάθη", "Ότι τα αυτοματοποιημένα συστήματα πρέπει να καταργηθούν", "Ότι τα μυστικά πρέπει να μένουν μυστικά", "Ότι η ανθρώπινη κρίση μπορεί να αξίζει περισσότερο από τη βεβαιότητα μιας μηχανής"], 3, "η κρίση ενός ανθρώπου που αμφιβάλλει μπορεί, σε κρίσιμες στιγμές, να αξίζει περισσότερο από τη βεβαιότητα μιας μηχανής"),
 ],
 "gloss": {"αυτοματοποιημένα": "αυτοματοποιημένος — automated", "κρίση": "κρίση — judgement", "αντισυνταγματάρχης": "αντισυνταγματάρχης — lieutenant colonel", "έγκαιρης προειδοποίησης": "έγκαιρη προειδοποίηση — early warning", "εκτοξευθεί": "εκτοξεύομαι — to be launched", "πύραυλος": "πύραυλος — missile", "πρωτόκολλο": "πρωτόκολλο — protocol", "ανωτέρους": "ανώτερος — superior (officer)", "υπερδυνάμεις": "υπερδύναμη — superpower", "αντίποινα": "αντίποινα — retaliation", "επίγεια": "επίγειος — ground-based", "εντοπίσει": "εντοπίζω — to detect", "βλάβη": "βλάβη — malfunction", "αντανάκλαση": "αντανάκλαση — reflection", "τυφλά": "τυφλά — blindly", "αμφιβάλλει": "αμφιβάλλω — to doubt"}
})

ITEMS.append({
 "id": "l133-c1-voulgaris", "title": "Ευγένιος Βούλγαρις, ένας λόγιος ανάμεσα σε δύο κόσμους", "title_en": "Evgenios Voulgaris, a scholar between two worlds", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια ιστορικό για τον λόγιο Ευγένιο Βούλγαρι.",
 "script": [
  L("Δημοσιογράφος", "m", "Ποιος ήταν ο Ευγένιος Βούλγαρις;", "Who was Evgenios Voulgaris?"),
  L("Ιστορικός", "f", "Ήταν ένας από τους πρώτους μεγάλους δασκάλους του Νεοελληνικού Διαφωτισμού. Γεννήθηκε στην Κέρκυρα το 1716 και σπούδασε στην Ιταλία, όπου γνώρισε τη σύγχρονη ευρωπαϊκή φιλοσοφία. Όταν γύρισε, δίδαξε σε σχολές των Ιωαννίνων και της Κοζάνης, και, σύμφωνα με τις πηγές, προκάλεσε αντιδράσεις, επειδή δίδασκε τους νεότερους φιλοσόφους δίπλα στον Αριστοτέλη.", "He was one of the first great teachers of the Modern Greek Enlightenment. He was born on Corfu in 1716 and studied in Italy, where he came to know modern European philosophy. When he returned, he taught at schools in Ioannina and Kozani and, according to the sources, provoked reactions because he taught the modern philosophers alongside Aristotle."),
  L("Δημοσιογράφος", "m", "Τι ήταν η Αθωνιάδα Ακαδημία;", "What was the Athonite Academy?"),
  L("Ιστορικός", "f", "Μια φιλόδοξη σχολή στο Άγιον Όρος, της οποίας ανέλαβε τη διεύθυνση τη δεκαετία του 1750. Η σχολή γνώρισε για λίγα χρόνια μεγάλη ακμή, όμως οι συγκρούσεις με όσους θεωρούσαν επικίνδυνες τις νέες ιδέες τον ανάγκασαν τελικά να αποχωρήσει.", "An ambitious school on Mount Athos, whose direction he took over in the 1750s. The school flourished greatly for a few years, but the clashes with those who considered the new ideas dangerous eventually forced him to leave."),
  L("Δημοσιογράφος", "m", "Και πώς βρέθηκε στη Ρωσία;", "And how did he end up in Russia?"),
  L("Ιστορικός", "f", "Η Αικατερίνη η Μεγάλη τον κάλεσε στην αυλή της, όπου έγινε αρχιεπίσκοπος σε μια περιοχή της νότιας Ρωσίας. Εκεί συνέχισε να γράφει και να μεταφράζει· μετέφρασε μάλιστα έργα του Βιργιλίου σε ομηρικό στίχο. Πέθανε στην Αγία Πετρούπολη το 1806. Είναι μια μορφή αντιφατική: άνοιξε τον δρόμο στις νέες ιδέες, αλλά στα γεράματά του έγινε πιο συντηρητικός.", "Catherine the Great invited him to her court, where he became archbishop of a region in southern Russia. There he went on writing and translating; he even translated works of Virgil into Homeric verse. He died in Saint Petersburg in 1806. He is a contradictory figure: he opened the way to new ideas, but in his old age he became more conservative."),
 ],
 "questions": [
  Q("Γιατί προκάλεσε αντιδράσεις η διδασκαλία του;", ["Γιατί δίδασκε στα ιταλικά", "Γιατί δίδασκε τους νεότερους φιλοσόφους δίπλα στον Αριστοτέλη", "Γιατί αρνιόταν να διδάξει τον Αριστοτέλη", "Γιατί δεν δεχόταν μαθητές από φτωχές οικογένειες"], 1, "δίδασκε τους νεότερους φιλοσόφους δίπλα στον Αριστοτέλη"),
  Q("Γιατί έφυγε τελικά από την Αθωνιάδα Ακαδημία;", ["Γιατί έκλεισε η σχολή από έλλειψη χρημάτων", "Γιατί τον κάλεσε η Αικατερίνη", "Λόγω των συγκρούσεων με όσους θεωρούσαν επικίνδυνες τις νέες ιδέες", "Γιατί αρρώστησε"], 2, "οι συγκρούσεις με όσους θεωρούσαν επικίνδυνες τις νέες ιδέες τον ανάγκασαν τελικά να αποχωρήσει"),
  Q("Τι έκανε στη Ρωσία;", ["Έγινε αρχιεπίσκοπος και συνέχισε να γράφει και να μεταφράζει", "Ίδρυσε ένα πανεπιστήμιο", "Έγινε σύμβουλος του στρατού", "Σταμάτησε να γράφει"], 0, "έγινε αρχιεπίσκοπος σε μια περιοχή της νότιας Ρωσίας. Εκεί συνέχισε να γράφει και να μεταφράζει"),
  Q("Γιατί τον χαρακτηρίζει η ιστορικός «αντιφατική μορφή»;", ["Γιατί άλλαζε συχνά χώρα", "Γιατί έγραφε σε πολλές γλώσσες", "Γιατί ήταν ταυτόχρονα κληρικός και φιλόσοφος", "Γιατί άνοιξε τον δρόμο στις νέες ιδέες, αλλά στα γεράματα έγινε πιο συντηρητικός"], 3, "άνοιξε τον δρόμο στις νέες ιδέες, αλλά στα γεράματά του έγινε πιο συντηρητικός"),
 ],
 "gloss": {"λόγιο": "λόγιος — scholar", "Διαφωτισμού": "Διαφωτισμός — the Enlightenment", "αντιδράσεις": "αντίδραση — reaction, opposition", "φιλόδοξη": "φιλόδοξος — ambitious", "Άγιον Όρος": "Άγιον Όρος — Mount Athos", "ακμή": "ακμή — peak, heyday", "αποχωρήσει": "αποχωρώ — to withdraw, leave", "αυλή": "αυλή — (royal) court", "αρχιεπίσκοπος": "αρχιεπίσκοπος — archbishop", "ομηρικό στίχο": "ομηρικός στίχος — Homeric verse", "αντιφατική": "αντιφατικός — contradictory", "γεράματά": "γεράματα — old age", "συντηρητικός": "συντηρητικός — conservative"}
})

rnd = random.Random(133)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-133.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
