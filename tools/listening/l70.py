# Source for library/listening/listening-70.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l70.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l70-ann-delfinia", "title": "Δελφίνια στα δεξιά του πλοίου", "title_en": "Dolphins to starboard", "type": "announcement", "level": "B2",
 "context_el": "Ταξιδεύετε με πλοίο στις Κυκλάδες. Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Καπετάνιος", "m", "Κυρίες και κύριοι, σας μιλάει ο καπετάνιος. Αν κοιτάξετε από τη δεξιά πλευρά του πλοίου, θα δείτε μια ομάδα δελφινιών που κολυμπά δίπλα μας. Θα μειώσουμε για λίγα λεπτά ταχύτητα, για να τα απολαύσετε.", "Ladies and gentlemen, this is the captain speaking. If you look out from the right-hand side of the ship, you will see a group of dolphins swimming alongside us. We will reduce speed for a few minutes so that you can enjoy them."),
  L("Καπετάνιος", "m", "Παρακαλούμε, μη σκύβετε πάνω από τα κάγκελα και κρατάτε τα παιδιά από το χέρι. Για τη δική σας ασφάλεια, η πρόσβαση στο κατάστρωμα της πλώρης παραμένει κλειστή λόγω του αέρα.", "Please do not lean over the railings and hold children by the hand. For your own safety, access to the bow deck remains closed because of the wind."),
  L("Καπετάνιος", "m", "Θα φτάσουμε στη Νάξο με μισή ώρα καθυστέρηση, περίπου στις τέσσερις και μισή. Το κυλικείο θα κλείσει δέκα λεπτά πριν από την άφιξη. Σας ευχόμαστε καλή συνέχεια.", "We will arrive in Naxos half an hour late, at about half past four. The snack bar will close ten minutes before arrival. We wish you a pleasant onward journey."),
 ],
 "questions": [
  Q("Γιατί θα μειώσει ταχύτητα το πλοίο;", ["Λόγω του αέρα", "Για να απολαύσουν οι επιβάτες τα δελφίνια", "Γιατί έχει βλάβη", "Για να μπει στο λιμάνι"], 1, "για να τα απολαύσετε"),
  Q("Γιατί είναι κλειστό το κατάστρωμα της πλώρης;", ["Λόγω καθαρισμού", "Λόγω του αέρα", "Λόγω της καθυστέρησης", "Γιατί είναι μόνο για το πλήρωμα"], 1, "παραμένει κλειστή λόγω του αέρα"),
  Q("Πότε θα κλείσει το κυλικείο;", ["Αμέσως", "Δέκα λεπτά πριν από την άφιξη", "Στις τέσσερις και μισή", "Μισή ώρα πριν από την άφιξη"], 1, "Το κυλικείο θα κλείσει δέκα λεπτά πριν από την άφιξη"),
 ],
 "gloss": {"δελφινιών": "δελφίνι — dolphin", "μειώσουμε": "μειώνω — to reduce", "ταχύτητα": "ταχύτητα — speed", "σκύβετε": "σκύβω — to lean, bend", "κάγκελα": "κάγκελο — railing", "κατάστρωμα": "κατάστρωμα — deck", "πλώρης": "πλώρη — bow (of a ship)", "άφιξη": "άφιξη — arrival"},
})

ITEMS.append({
 "id": "l70-vm-magnitiki", "title": "Τα αποτελέσματα της μαγνητικής", "title_en": "The MRI results", "type": "voicemail", "level": "B2",
 "context_el": "Κάνατε μαγνητική τομογραφία στο γόνατο. Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από το ιατρείο του ορθοπεδικού σας.",
 "script": [
  L("Γραμματέας", "f", "Καλημέρα σας, από το ιατρείο του κυρίου Μαυρίδη σας τηλεφωνώ. Ο γιατρός είδε τα αποτελέσματα της μαγνητικής σας και ζήτησε να σας πω ότι δεν υπάρχει ρήξη χιαστού, όπως φοβόταν. Πρόκειται για μια ελαφριά θλάση του μηνίσκου.", "Good morning, I'm calling from Dr Mavridis's practice. The doctor has seen the results of your MRI and asked me to tell you that there is no cruciate ligament tear, as he feared. It's a mild strain of the meniscus."),
  L("Γραμματέας", "f", "Δεν χρειάζεται χειρουργείο. Ο γιατρός προτείνει δέκα συνεδρίες φυσικοθεραπείας και αποχή από το τρέξιμο για έναν μήνα. Μπορείτε, όμως, να κολυμπάτε και να κάνετε ποδήλατο, αν δεν πονάτε.", "No surgery is needed. The doctor recommends ten physiotherapy sessions and no running for a month. You can, however, swim and cycle, if it doesn't hurt."),
  L("Γραμματέας", "f", "Το παραπεμπτικό για τη φυσικοθεραπεία θα το βρείτε στη γραμματεία από αύριο. Το επόμενο ραντεβού σας με τον γιατρό είναι σε έξι εβδομάδες· θα σας στείλουμε υπενθύμιση με μήνυμα. Περαστικά!", "You can pick up the referral for physiotherapy at reception from tomorrow. Your next appointment with the doctor is in six weeks; we'll send you a text reminder. Get well soon!"),
 ],
 "questions": [
  Q("Τι έδειξε η μαγνητική;", ["Ρήξη χιαστού", "Μια ελαφριά θλάση του μηνίσκου", "Κάταγμα", "Τίποτα απολύτως"], 1, "Πρόκειται για μια ελαφριά θλάση του μηνίσκου"),
  Q("Τι πρέπει να αποφύγει ο ασθενής για έναν μήνα;", ["Το κολύμπι", "Το ποδήλατο", "Το τρέξιμο", "Το περπάτημα"], 2, "αποχή από το τρέξιμο για έναν μήνα"),
  Q("Πού θα βρει το παραπεμπτικό;", ["Στο ηλεκτρονικό ταχυδρομείο", "Στη γραμματεία από αύριο", "Στο φαρμακείο", "Στο νοσοκομείο"], 1, "θα το βρείτε στη γραμματεία από αύριο"),
 ],
 "gloss": {"μαγνητικής": "μαγνητική (τομογραφία) — MRI scan", "ορθοπεδικού": "ορθοπεδικός — orthopaedic surgeon", "ρήξη": "ρήξη — tear, rupture", "χιαστού": "χιαστός (σύνδεσμος) — cruciate ligament", "θλάση": "θλάση — strain", "μηνίσκου": "μηνίσκος — meniscus", "συνεδρίες": "συνεδρία — session", "φυσικοθεραπείας": "φυσικοθεραπεία — physiotherapy", "αποχή": "αποχή — abstaining", "παραπεμπτικό": "παραπεμπτικό — referral", "Περαστικά": "περαστικά — get well soon"},
})

ITEMS.append({
 "id": "l70-dia-deuteri-gnomi", "title": "Δεύτερη γνώμη πριν από την επέμβαση", "title_en": "A second opinion before the operation", "type": "dialogue", "level": "B2",
 "context_el": "Δύο αδέρφια συζητούν για την επέμβαση στο γόνατο που πρότεινε ο γιατρός στον πατέρα τους.",
 "script": [
  L("Μαρίνα", "f", "Ο γιατρός λέει ότι ο μπαμπάς χρειάζεται ολική αρθροπλαστική στο γόνατο. Θέλει να κλείσουμε ημερομηνία για τον επόμενο μήνα. Εμένα μου φαίνεται πολύ βιαστικό.", "The doctor says Dad needs a total knee replacement. He wants us to book a date for next month. It seems very rushed to me."),
  L("Κώστας", "m", "Συμφωνώ. Είναι μεγάλη επέμβαση, και ο μπαμπάς είναι εβδομήντα οκτώ χρονών. Πριν αποφασίσουμε, ας πάρουμε μια δεύτερη γνώμη. Ένας συνάδελφός μου ξέρει έναν πολύ καλό ορθοπεδικό στη Θεσσαλονίκη.", "I agree. It's a big operation, and Dad is seventy-eight. Before we decide, let's get a second opinion. A colleague of mine knows a very good orthopaedic surgeon in Thessaloniki."),
  L("Μαρίνα", "f", "Καλή ιδέα. Αλλά δεν θέλω να το πάρει ο μπαμπάς σαν να μην εμπιστευόμαστε τον γιατρό του. Τον ξέρει εδώ και είκοσι χρόνια.", "Good idea. But I don't want Dad to take it as if we don't trust his doctor. He's known him for twenty years."),
  L("Κώστας", "m", "Θα του το πούμε απλά: για μια τόσο σοβαρή απόφαση, δύο γνώμες είναι καλύτερες από μία. Θα στείλω στον γιατρό της Θεσσαλονίκης τις ακτινογραφίες με ηλεκτρονικό ταχυδρομείο, για να μη χρειαστεί να ταξιδέψει ο μπαμπάς χωρίς λόγο.", "We'll put it to him simply: for such a serious decision, two opinions are better than one. I'll email the X-rays to the doctor in Thessaloniki, so that Dad doesn't have to travel for no reason."),
 ],
 "questions": [
  Q("Τι πρότεινε ο γιατρός;", ["Φυσικοθεραπεία", "Ολική αρθροπλαστική στο γόνατο", "Φάρμακα για τον πόνο", "Να περιμένουν έναν χρόνο"], 1, "ο μπαμπάς χρειάζεται ολική αρθροπλαστική στο γόνατο"),
  Q("Τι ανησυχεί τη Μαρίνα;", ["Το κόστος της επέμβασης", "Να μη νομίσει ο πατέρας ότι δεν εμπιστεύονται τον γιατρό του", "Το ταξίδι στη Θεσσαλονίκη", "Η ηλικία του γιατρού"], 1, "δεν θέλω να το πάρει ο μπαμπάς σαν να μην εμπιστευόμαστε τον γιατρό του"),
  Q("Γιατί ο Κώστας θα στείλει τις ακτινογραφίες με ηλεκτρονικό ταχυδρομείο;", ["Για να μη χρειαστεί να ταξιδέψει ο πατέρας χωρίς λόγο", "Γιατί είναι φθηνότερο", "Γιατί το ζήτησε ο γιατρός του πατέρα", "Γιατί χάθηκαν οι πρωτότυπες"], 0, "για να μη χρειαστεί να ταξιδέψει ο μπαμπάς χωρίς λόγο"),
 ],
 "gloss": {"επέμβαση": "επέμβαση — operation", "αρθροπλαστική": "αρθροπλαστική — joint replacement", "βιαστικό": "βιαστικός — hasty, rushed", "δεύτερη γνώμη": "δεύτερη γνώμη — second opinion", "εμπιστευόμαστε": "εμπιστεύομαι — to trust", "ακτινογραφίες": "ακτινογραφία — X-ray"},
})

ITEMS.append({
 "id": "l70-dia-kinito-sta-deka", "title": "Κινητό στα δέκα;", "title_en": "A phone at ten?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο γονείς συζητούν αν πρέπει να πάρουν κινητό στην κόρη τους.",
 "script": [
  L("Άννα", "f", "Η Δανάη μού είπε πάλι σήμερα ότι είναι η μόνη στην τάξη της χωρίς κινητό. Λέει ότι οι φίλες της κανονίζουν τα πάντα σε μια ομάδα συνομιλίας και εκείνη τα μαθαίνει τελευταία.", "Danai told me again today that she's the only one in her class without a phone. She says her friends arrange everything in a group chat and she's the last to find out."),
  L("Πέτρος", "m", "Είναι δέκα χρονών, Άννα. Έχω διαβάσει ότι όσο αργότερα αποκτούν τα παιδιά κινητό, τόσο καλύτερα. Φοβάμαι ότι θα κολλήσει στην οθόνη και θα σταματήσει να διαβάζει βιβλία.", "She's ten, Anna. I've read that the later children get a phone, the better. I'm afraid she'll get glued to the screen and stop reading books."),
  L("Άννα", "f", "Κι εγώ το φοβάμαι. Τι λες για έναν συμβιβασμό; Ένα απλό κινητό, μόνο για κλήσεις και μηνύματα, χωρίς ίντερνετ. Έτσι θα μπορεί να μας παίρνει τηλέφωνο, όταν γυρίζει από το μπαλέτο.", "I'm afraid of that too. How about a compromise? A simple phone, only for calls and texts, without internet. That way she can phone us when she's coming back from ballet."),
  L("Πέτρος", "m", "Αυτό μου αρέσει. Και το βράδυ το κινητό θα μένει στην κουζίνα, όχι στο δωμάτιό της. Θα το συζητήσουμε μαζί της, για να καταλάβει γιατί.", "I like that. And at night the phone will stay in the kitchen, not in her room. We'll discuss it with her, so she understands why."),
 ],
 "questions": [
  Q("Τι παραπονιέται η Δανάη;", ["Ότι οι φίλες της δεν της μιλάνε", "Ότι μαθαίνει τελευταία ό,τι κανονίζουν οι φίλες της", "Ότι δεν την αφήνουν να βγαίνει", "Ότι έχει πολλά μαθήματα"], 1, "εκείνη τα μαθαίνει τελευταία"),
  Q("Τι φοβάται ο Πέτρος;", ["Ότι θα χάσει το κινητό", "Ότι θα κοστίσει πολύ", "Ότι θα κολλήσει στην οθόνη και θα σταματήσει να διαβάζει", "Ότι θα του τηλεφωνούν άγνωστοι"], 2, "θα κολλήσει στην οθόνη και θα σταματήσει να διαβάζει βιβλία"),
  Q("Ποιος είναι ο συμβιβασμός;", ["Ένα κινητό στα δώδεκα", "Ένα απλό κινητό μόνο για κλήσεις και μηνύματα", "Ένα τάμπλετ για το σπίτι", "Το κινητό της μητέρας της"], 1, "Ένα απλό κινητό, μόνο για κλήσεις και μηνύματα"),
 ],
 "gloss": {"κανονίζουν": "κανονίζω — to arrange", "ομάδα συνομιλίας": "ομάδα συνομιλίας — group chat", "αποκτούν": "αποκτώ — to acquire, get", "κολλήσει": "κολλάω — to get hooked, stuck", "συμβιβασμό": "συμβιβασμός — compromise", "κλήσεις": "κλήση — call"},
})

ITEMS.append({
 "id": "l70-int-synodigos-rali", "title": "Συνοδηγός σε ράλι", "title_en": "A rally co-driver", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια συνοδηγό αγώνων ράλι.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί πιστεύουν ότι ο συνοδηγός απλώς κάθεται δίπλα στον οδηγό. Τι κάνετε στην πραγματικότητα;", "Many people think the co-driver just sits next to the driver. What do you really do?"),
  L("Συνοδηγός", "f", "Διαβάζω τις «σημειώσεις», δηλαδή την περιγραφή της διαδρομής που έχουμε γράψει μαζί πριν από τον αγώνα: πόσο κλειστή είναι κάθε στροφή, πού υπάρχει λακκούβα, πού πρέπει να φρενάρει. Ο οδηγός δεν βλέπει τι υπάρχει πίσω από τη στροφή· οδηγεί με βάση τη δική μου φωνή. Αν κάνω λάθος έστω και ένα δευτερόλεπτο, μπορεί να βγούμε από τον δρόμο.", "I read the 'notes', that is the description of the route that we wrote together before the race: how tight each bend is, where there's a pothole, where he must brake. The driver can't see what's behind the bend; he drives by my voice. If I'm wrong by even one second, we can go off the road."),
  L("Δημοσιογράφος", "m", "Δεν φοβάστε;", "Aren't you afraid?"),
  L("Συνοδηγός", "f", "Στον αγώνα δεν έχω χρόνο να φοβηθώ. Ο φόβος έρχεται μετά, όταν βλέπω τα βίντεο. Το πιο δύσκολο για μένα δεν είναι η ταχύτητα, αλλά η ναυτία: διαβάζεις συνέχεια ένα χαρτί μέσα σε ένα αυτοκίνητο που χοροπηδάει. Τα πρώτα χρόνια έκανα εμετό σχεδόν σε κάθε αγώνα.", "During the race I have no time to be afraid. The fear comes afterwards, when I watch the videos. The hardest thing for me isn't the speed but the motion sickness: you're constantly reading a sheet of paper in a car that's bouncing around. In the first years I was sick at almost every race."),
 ],
 "questions": [
  Q("Τι είναι οι «σημειώσεις»;", ["Οι κανόνες του αγώνα", "Η περιγραφή της διαδρομής που γράφουν μαζί πριν από τον αγώνα", "Οι χρόνοι των άλλων οδηγών", "Οι οδηγίες των μηχανικών"], 1, "την περιγραφή της διαδρομής που έχουμε γράψει μαζί πριν από τον αγώνα"),
  Q("Πότε έρχεται ο φόβος;", ["Πριν από τον αγώνα", "Στις στροφές", "Μετά, όταν βλέπει τα βίντεο", "Ποτέ"], 2, "Ο φόβος έρχεται μετά, όταν βλέπω τα βίντεο"),
  Q("Τι είναι το πιο δύσκολο για τη συνοδηγό;", ["Η ταχύτητα", "Η ναυτία", "Ο θόρυβος", "Η ζέστη"], 1, "αλλά η ναυτία"),
 ],
 "gloss": {"συνοδηγό": "συνοδηγός — co-driver", "ράλι": "ράλι — rally", "διαδρομής": "διαδρομή — route", "στροφή": "στροφή — bend, turn", "λακκούβα": "λακκούβα — pothole", "φρενάρει": "φρενάρω — to brake", "ναυτία": "ναυτία — motion sickness, nausea", "χοροπηδάει": "χοροπηδάω — to bounce, jump about", "εμετό": "εμετός — vomiting"},
})

ITEMS.append({
 "id": "l70-rep-chrysi", "title": "Το νησί Χρυσή", "title_en": "The island of Chrysi", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ραδιοφωνικό ρεπορτάζ από ένα μικρό ακατοίκητο νησί νότια της Κρήτης.",
 "script": [
  L("Ρεπόρτερ", "f", "Βρίσκομαι στη Χρυσή, ένα μικρό ακατοίκητο νησί νότια της Ιεράπετρας. Το καλοκαίρι, καραβάκια φέρνουν εδώ καθημερινά χιλιάδες επισκέπτες, που έρχονται για τα τιρκουάζ νερά και τις παραλίες με τα χρυσαφένια βότσαλα και τα κοχύλια.", "I'm on Chrysi, a small uninhabited island south of Ierapetra. In summer, small boats bring thousands of visitors here every day, who come for the turquoise waters and the beaches with golden pebbles and shells."),
  L("Ρεπόρτερ", "f", "Ο μεγαλύτερος θησαυρός του νησιού, όμως, είναι το δάσος του, με κέδρους που φτάνουν τα εκατοντάδες χρόνια. Οι κέδροι φυτρώνουν πάνω στους αμμόλοφους και είναι πολύ ευαίσθητοι. Γι’ αυτό το νησί προστατεύεται, και οι επισκέπτες πρέπει να περπατούν μόνο στα σημαδεμένα μονοπάτια.", "The island's greatest treasure, though, is its forest, with cedars hundreds of years old. The cedars grow on the sand dunes and are very fragile. That's why the island is protected, and visitors must walk only on the marked paths."),
  L("Ρεπόρτερ", "f", "Απαγορεύεται η διανυκτέρευση και το κάμπινγκ, όπως και να παίρνει κανείς κοχύλια ή άμμο. Οι φύλακες ελέγχουν τις τσάντες στην επιστροφή. Τα τελευταία καραβάκια φεύγουν στις έξι το απόγευμα, και όποιος τα χάσει, μπορεί να έχει μεγάλο πρόβλημα.", "Staying overnight and camping are forbidden, as is taking shells or sand. The wardens check bags on the way back. The last boats leave at six in the evening, and anyone who misses them could be in big trouble."),
 ],
 "questions": [
  Q("Τι είναι, σύμφωνα με τη ρεπόρτερ, ο μεγαλύτερος θησαυρός του νησιού;", ["Οι παραλίες", "Το δάσος με τους κέδρους", "Τα κοχύλια", "Τα αρχαία"], 1, "Ο μεγαλύτερος θησαυρός του νησιού, όμως, είναι το δάσος του"),
  Q("Γιατί πρέπει οι επισκέπτες να περπατούν μόνο στα σημαδεμένα μονοπάτια;", ["Γιατί υπάρχουν φίδια", "Γιατί οι κέδροι είναι πολύ ευαίσθητοι", "Για να μη χαθούν", "Γιατί η άμμος καίει"], 1, "είναι πολύ ευαίσθητοι"),
  Q("Τι απαγορεύεται;", ["Το κολύμπι", "Οι φωτογραφίες", "Η διανυκτέρευση και να παίρνει κανείς κοχύλια ή άμμο", "Τα σκυλιά"], 2, "Απαγορεύεται η διανυκτέρευση και το κάμπινγκ, όπως και να παίρνει κανείς κοχύλια ή άμμο"),
 ],
 "gloss": {"ακατοίκητο": "ακατοίκητος — uninhabited", "τιρκουάζ": "τιρκουάζ — turquoise", "χρυσαφένια": "χρυσαφένιος — golden", "κοχύλια": "κοχύλι — shell", "κέδρους": "κέδρος — cedar", "αμμόλοφους": "αμμόλοφος — sand dune", "σημαδεμένα": "σημαδεμένος — marked", "διανυκτέρευση": "διανυκτέρευση — overnight stay", "φύλακες": "φύλακας — warden, guard"},
})

ITEMS.append({
 "id": "l70-mono-chortofagos", "title": "Γιατί έγινα χορτοφάγος", "title_en": "Why I became vegetarian", "type": "monologue", "level": "B2",
 "context_el": "Ένας νέος άντρας εξηγεί πώς και γιατί σταμάτησε να τρώει κρέας.",
 "script": [
  L("Παναγιώτης", "m", "Μεγάλωσα σε ένα χωριό της Θεσσαλίας, όπου το Πάσχα σημαίνει αρνί στη σούβλα και η Κυριακή κοκκινιστό. Αν μου έλεγε κάποιος πριν από πέντε χρόνια ότι θα γινόμουν χορτοφάγος, θα γελούσα.", "I grew up in a village in Thessaly, where Easter means lamb on the spit and Sunday means meat in tomato sauce. If someone had told me five years ago that I'd become vegetarian, I would have laughed."),
  L("Παναγιώτης", "m", "Δεν ήταν μια ξαφνική απόφαση. Όλα ξεκίνησαν, όταν ο γιατρός μού είπε ότι η χοληστερίνη μου ήταν ψηλή. Άρχισα να τρώω λιγότερο κρέας και ανακάλυψα ότι η παραδοσιακή ελληνική κουζίνα είναι γεμάτη πιάτα χωρίς κρέας: φασολάδα, γεμιστά, μπριάμ, φακές. Οι γιαγιάδες μας, άλλωστε, έτρωγαν κρέας μόνο στις γιορτές.", "It wasn't a sudden decision. It all started when the doctor told me my cholesterol was high. I started eating less meat and discovered that traditional Greek cuisine is full of meatless dishes: bean soup, stuffed vegetables, briam, lentils. Our grandmothers, after all, ate meat only on feast days."),
  L("Παναγιώτης", "m", "Το δυσκολότερο δεν ήταν το φαγητό, αλλά η οικογένεια. Η μητέρα μου ανησυχούσε ότι δεν θα έπαιρνα αρκετές πρωτεΐνες. Τώρα, όταν πηγαίνω στο χωριό, μου μαγειρεύει χωριστά γίγαντες στον φούρνο, και στο τέλος τούς τρώνε όλοι.", "The hardest thing wasn't the food but the family. My mother worried that I wouldn't get enough protein. Now, when I go to the village, she cooks me baked giant beans separately, and in the end everyone eats them."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε η αλλαγή στη διατροφή του;", ["Είδε ένα ντοκιμαντέρ", "Ο γιατρός του είπε ότι η χοληστερίνη του ήταν ψηλή", "Του το πρότεινε η μητέρα του", "Μετακόμισε στην πόλη"], 1, "ο γιατρός μού είπε ότι η χοληστερίνη μου ήταν ψηλή"),
  Q("Τι ανακάλυψε για την ελληνική κουζίνα;", ["Ότι είναι γεμάτη πιάτα χωρίς κρέας", "Ότι είναι πολύ λιπαρή", "Ότι δεν έχει λαχανικά", "Ότι είναι δύσκολη"], 0, "η παραδοσιακή ελληνική κουζίνα είναι γεμάτη πιάτα χωρίς κρέας"),
  Q("Τι συμβαίνει τώρα, όταν πηγαίνει στο χωριό;", ["Τρώει μόνος του", "Η μητέρα του τού μαγειρεύει χωριστά, και στο τέλος τρώνε όλοι το φαγητό του", "Τρώει κρέας για να μη στενοχωρήσει τη μητέρα του", "Μαγειρεύει ο ίδιος για όλους"], 1, "μου μαγειρεύει χωριστά γίγαντες στον φούρνο, και στο τέλος τούς τρώνε όλοι"),
 ],
 "gloss": {"χορτοφάγος": "χορτοφάγος — vegetarian", "σούβλα": "σούβλα — spit", "κοκκινιστό": "κοκκινιστό — meat in tomato sauce", "ξαφνική": "ξαφνικός — sudden", "χοληστερίνη": "χοληστερίνη — cholesterol", "φασολάδα": "φασολάδα — bean soup", "γεμιστά": "γεμιστά — stuffed vegetables", "πρωτεΐνες": "πρωτεΐνη — protein", "χωριστά": "χωριστά — separately", "γίγαντες": "γίγαντες — giant beans"},
})

ITEMS.append({
 "id": "l70-mono-poulao-vivlia", "title": "Γιατί πουλάω τα βιβλία μου", "title_en": "Why I'm selling my books", "type": "monologue", "level": "B2",
 "context_el": "Μια συνταξιούχος καθηγήτρια μιλά για τη βιβλιοθήκη της.",
 "script": [
  L("Ευδοκία", "f", "Σε σαράντα χρόνια μάζεψα σχεδόν τρεις χιλιάδες βιβλία. Γέμιζαν όλους τους τοίχους του σπιτιού, ακόμη και τον διάδρομο. Τώρα που μετακομίζω σε ένα μικρότερο διαμέρισμα, πρέπει να αποχωριστώ τα περισσότερα.", "In forty years I collected almost three thousand books. They filled every wall of the house, even the corridor. Now that I'm moving to a smaller flat, I have to part with most of them."),
  L("Ευδοκία", "f", "Στην αρχή ένιωθα ότι πουλούσα κομμάτια από τον εαυτό μου. Σε πολλά βιβλία έχω γράψει σημειώσεις στο περιθώριο, σε άλλα υπάρχουν αφιερώσεις από φίλους που δεν ζουν πια. Αυτά τα κρατάω. Τα υπόλοιπα, όμως, γιατί να μαζεύουν σκόνη;", "At first I felt I was selling pieces of myself. In many books I've written notes in the margin; in others there are dedications from friends who are no longer alive. Those I'm keeping. But the rest, why should they gather dust?"),
  L("Ευδοκία", "f", "Τα πουλάω σε ένα παλαιοβιβλιοπωλείο, και ένα μέρος τα χαρίζω στη βιβλιοθήκη του σχολείου όπου δίδασκα. Πριν από λίγες μέρες, ο βιβλιοπώλης μού είπε ότι ένας φοιτητής αγόρασε τον Καβάφη μου και ενθουσιάστηκε με τις σημειώσεις μου. Αυτό με παρηγόρησε περισσότερο από κάθε χρήμα.", "I'm selling them to a second-hand bookshop, and I'm giving some to the library of the school where I taught. A few days ago the bookseller told me a student had bought my Cavafy and was thrilled with my notes. That comforted me more than any money."),
 ],
 "questions": [
  Q("Γιατί πουλάει τα βιβλία της;", ["Γιατί χρειάζεται χρήματα", "Γιατί μετακομίζει σε μικρότερο διαμέρισμα", "Γιατί δεν διαβάζει πια", "Γιατί χάλασαν από την υγρασία"], 1, "Τώρα που μετακομίζω σε ένα μικρότερο διαμέρισμα"),
  Q("Ποια βιβλία κρατάει;", ["Τα πιο ακριβά", "Αυτά με σημειώσεις και αφιερώσεις", "Μόνο την ποίηση", "Τα σχολικά βιβλία"], 1, "Αυτά τα κρατάω"),
  Q("Τι την παρηγόρησε περισσότερο από κάθε χρήμα;", ["Ότι ένας φοιτητής ενθουσιάστηκε με τις σημειώσεις της", "Ότι το σχολείο την ευχαρίστησε", "Ότι πούλησε όλα τα βιβλία", "Ότι βρήκε ένα σπάνιο βιβλίο"], 0, "ένας φοιτητής αγόρασε τον Καβάφη μου και ενθουσιάστηκε με τις σημειώσεις μου"),
 ],
 "gloss": {"αποχωριστώ": "αποχωρίζομαι — to part with", "περιθώριο": "περιθώριο — margin", "αφιερώσεις": "αφιέρωση — dedication", "σκόνη": "σκόνη — dust", "παλαιοβιβλιοπωλείο": "παλαιοβιβλιοπωλείο — second-hand bookshop", "χαρίζω": "χαρίζω — to give away", "βιβλιοπώλης": "βιβλιοπώλης — bookseller", "παρηγόρησε": "παρηγορώ — to comfort"},
})

ITEMS.append({
 "id": "l70-c1-zoologika-parka", "title": "Χρειαζόμαστε ακόμη ζωολογικούς κήπους;", "title_en": "Do we still need zoos?", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια βιολόγο για τον ρόλο των ζωολογικών κήπων σήμερα.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι ζωολογικοί κήποι δέχονται όλο και περισσότερη κριτική. Έχουν, κατά τη γνώμη σας, θέση στον 21ο αιώνα;", "Zoos face more and more criticism. Do they, in your opinion, have a place in the 21st century?"),
  L("Βιολόγος", "f", "Εξαρτάται από το τι εννοούμε με τον όρο «ζωολογικός κήπος». Οι σύγχρονοι, σοβαροί ζωολογικοί κήποι υποστηρίζουν ότι ο ρόλος τους δεν είναι πια η διασκέδαση, αλλά η διατήρηση των ειδών. Ορισμένα ζώα, όπως ο όρυγας της Αραβίας, σώθηκαν από την εξαφάνιση χάρη σε προγράμματα αναπαραγωγής σε αιχμαλωσία και επανεισήχθησαν αργότερα στη φύση.", "It depends on what we mean by the term 'zoo'. Modern, serious zoos argue that their role is no longer entertainment but the conservation of species. Some animals, such as the Arabian oryx, were saved from extinction thanks to captive breeding programmes and were later reintroduced into the wild."),
  L("Δημοσιογράφος", "m", "Και η άλλη πλευρά;", "And the other side?"),
  L("Βιολόγος", "f", "Η κριτική είναι σε μεγάλο βαθμό δικαιολογημένη για ορισμένα είδη. Οι ελέφαντες, οι όρκες, τα μεγάλα αρπακτικά χρειάζονται τεράστιες εκτάσεις· σε έναν περιορισμένο χώρο εμφανίζουν συχνά στερεοτυπικές συμπεριφορές, όπως το συνεχές πήγαινε-έλα, που είναι ένδειξη άγχους. Πιστεύω ότι το μέλλον ανήκει σε κάτι ενδιάμεσο: σε καταφύγια που φιλοξενούν ζώα τα οποία δεν μπορούν να επιβιώσουν στη φύση, και όπου ο επισκέπτης δεν είναι το κέντρο του κόσμου.", "The criticism is largely justified for certain species. Elephants, orcas and big predators need huge areas; in a confined space they often show stereotypic behaviours, such as constant pacing, which is a sign of stress. I believe the future belongs to something in between: sanctuaries that house animals which cannot survive in the wild, and where the visitor is not the centre of the world."),
 ],
 "questions": [
  Q("Ποιον ρόλο υποστηρίζουν ότι έχουν οι σύγχρονοι ζωολογικοί κήποι;", ["Τη διασκέδαση", "Τη διατήρηση των ειδών", "Την έρευνα για φάρμακα", "Την εκπαίδευση των κτηνιάτρων"], 1, "ο ρόλος τους δεν είναι πια η διασκέδαση, αλλά η διατήρηση των ειδών"),
  Q("Τι συνέβη με τον όρυγα της Αραβίας;", ["Εξαφανίστηκε", "Σώθηκε χάρη σε προγράμματα αναπαραγωγής και επανεισήχθη στη φύση", "Ζει μόνο σε ζωολογικούς κήπους", "Μεταφέρθηκε στην Ελλάδα"], 1, "σώθηκαν από την εξαφάνιση χάρη σε προγράμματα αναπαραγωγής σε αιχμαλωσία"),
  Q("Τι δείχνουν οι στερεοτυπικές συμπεριφορές;", ["Ότι τα ζώα παίζουν", "Ότι τα ζώα είναι άρρωστα από ιούς", "Άγχος", "Ότι τα ζώα πεινάνε"], 2, "που είναι ένδειξη άγχους"),
  Q("Σε τι πιστεύει η βιολόγος ότι ανήκει το μέλλον;", ["Στο κλείσιμο όλων των ζωολογικών κήπων", "Σε μεγαλύτερους ζωολογικούς κήπους", "Σε καταφύγια για ζώα που δεν μπορούν να επιβιώσουν στη φύση", "Σε ψηφιακούς ζωολογικούς κήπους"], 2, "σε καταφύγια που φιλοξενούν ζώα τα οποία δεν μπορούν να επιβιώσουν στη φύση"),
 ],
 "gloss": {"ζωολογικοί κήποι": "ζωολογικός κήπος — zoo", "κριτική": "κριτική — criticism", "διατήρηση": "διατήρηση — conservation", "όρυγας": "όρυγας — oryx", "εξαφάνιση": "εξαφάνιση — extinction", "αναπαραγωγής": "αναπαραγωγή — breeding", "αιχμαλωσία": "αιχμαλωσία — captivity", "επανεισήχθησαν": "επανεισάγομαι — to be reintroduced", "αρπακτικά": "αρπακτικό — predator", "εκτάσεις": "έκταση — area, expanse", "στερεοτυπικές": "στερεοτυπικός — stereotypic", "καταφύγια": "καταφύγιο — sanctuary, refuge"},
})

ITEMS.append({
 "id": "l70-c1-agia-sofia", "title": "Η Αγία Σοφία", "title_en": "Hagia Sophia", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από διάλεξη ιστορικού της τέχνης για έναν από τους πιο σημαντικούς ναούς του κόσμου.",
 "script": [
  L("Ιστορικός τέχνης", "f", "Η Αγία Σοφία, όπως τη βλέπουμε σήμερα στην Κωνσταντινούπολη, χτίστηκε μέσα σε μόλις πέντε χρόνια, από το 532 έως το 537, με εντολή του αυτοκράτορα Ιουστινιανού. Τον σχεδιασμό ανέλαβαν δύο επιστήμονες περισσότερο παρά αρχιτέκτονες με τη σημερινή έννοια: ο Ανθέμιος από τις Τράλλεις και ο Ισίδωρος από τη Μίλητο, και οι δύο βαθιοί γνώστες της γεωμετρίας και της μηχανικής.", "Hagia Sophia, as we see it today in Constantinople, was built in just five years, from 532 to 537, on the orders of the emperor Justinian. The design was undertaken by two men who were scientists rather than architects in today's sense: Anthemius of Tralles and Isidore of Miletus, both deeply versed in geometry and mechanics."),
  L("Ιστορικός τέχνης", "f", "Το πιο εντυπωσιακό στοιχείο είναι ο τεράστιος τρούλος, που μοιάζει να αιωρείται πάνω από τον ναό, χάρη στη σειρά παραθύρων στη βάση του, από τα οποία μπαίνει το φως. Η τόλμη του σχεδίου, όμως, είχε το τίμημά της: το 558, ύστερα από σεισμούς, ο πρώτος τρούλος κατέρρευσε, και ο νέος χτίστηκε ψηλότερος και πιο σταθερός. Σύμφωνα με μια παράδοση, ο Ιουστινιανός, όταν μπήκε για πρώτη φορά στον ναό, αναφώνησε: «Σε νίκησα, Σολομώντα!»", "The most impressive feature is the enormous dome, which seems to float above the church thanks to the row of windows at its base through which the light enters. The boldness of the design, however, came at a price: in 558, after earthquakes, the first dome collapsed, and the new one was built higher and more stable. According to one tradition, when Justinian first entered the church, he exclaimed: 'Solomon, I have surpassed you!'"),
  L("Ιστορικός τέχνης", "f", "Μετά την Άλωση του 1453, ο ναός μετατράπηκε σε τζαμί, και προστέθηκαν μιναρέδες. Το 1934 έγινε μουσείο, και το 2020 μετατράπηκε ξανά σε τζαμί, απόφαση που προκάλεσε έντονες αντιδράσεις, ιδίως στην Ελλάδα. Η ιστορία της Αγίας Σοφίας είναι, κατά κάποιον τρόπο, η ιστορία της ίδιας της πόλης: ένα μνημείο στο οποίο συνυπάρχουν, όχι πάντα αρμονικά, πολλά διαφορετικά στρώματα μνήμης.", "After the Fall in 1453, the church was converted into a mosque, and minarets were added. In 1934 it became a museum, and in 2020 it was turned into a mosque again, a decision that provoked strong reactions, especially in Greece. The history of Hagia Sophia is, in a way, the history of the city itself: a monument in which many different layers of memory coexist, not always harmoniously."),
 ],
 "questions": [
  Q("Τι ισχύει για τον Ανθέμιο και τον Ισίδωρο;", ["Ήταν αυτοκράτορες", "Ήταν βαθιοί γνώστες της γεωμετρίας και της μηχανικής", "Ήταν ζωγράφοι", "Ήταν μοναχοί"], 1, "και οι δύο βαθιοί γνώστες της γεωμετρίας και της μηχανικής"),
  Q("Γιατί ο τρούλος μοιάζει να αιωρείται;", ["Γιατί είναι από ξύλο", "Χάρη στη σειρά παραθύρων στη βάση του", "Γιατί είναι χρυσός", "Γιατί είναι πολύ μικρός"], 1, "χάρη στη σειρά παραθύρων στη βάση του"),
  Q("Τι συνέβη το 558;", ["Ο ναός εγκαινιάστηκε", "Ο πρώτος τρούλος κατέρρευσε ύστερα από σεισμούς", "Ο ναός έγινε τζαμί", "Ο Ιουστινιανός πέθανε"], 1, "ο πρώτος τρούλος κατέρρευσε"),
  Q("Πώς χαρακτηρίζει η ομιλήτρια την Αγία Σοφία στο τέλος;", ["Ως ένα μνημείο όπου συνυπάρχουν πολλά στρώματα μνήμης", "Ως ένα απλό μουσείο", "Ως ένα κτίριο χωρίς ιστορία", "Ως τον μεγαλύτερο ναό του κόσμου"], 0, "ένα μνημείο στο οποίο συνυπάρχουν, όχι πάντα αρμονικά, πολλά διαφορετικά στρώματα μνήμης"),
 ],
 "gloss": {"εντολή": "εντολή — order, command", "γνώστες": "γνώστης — expert, connoisseur", "τρούλος": "τρούλος — dome", "αιωρείται": "αιωρούμαι — to float, hover", "τόλμη": "τόλμη — boldness", "τίμημά": "τίμημα — price, cost", "κατέρρευσε": "καταρρέω — to collapse", "αναφώνησε": "αναφωνώ — to exclaim", "Άλωση": "Άλωση — the Fall (of Constantinople)", "μετατράπηκε": "μετατρέπομαι — to be converted", "μιναρέδες": "μιναρές — minaret", "συνυπάρχουν": "συνυπάρχω — to coexist", "στρώματα": "στρώμα — layer"},
})

rnd = random.Random(70)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-70.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
