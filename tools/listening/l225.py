# Source for library/listening/listening-225.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l225.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l225-news-leoforeio-kat-apaitisi", "title": "Ένα λεωφορείο που έρχεται όταν το καλέσεις", "title_en": "A bus that comes when you call it", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση σε έναν τοπικό ραδιοφωνικό σταθμό για μια νέα συγκοινωνία στα ορεινά χωριά.",
 "script": [
  L("Εκφωνητής", "m", "Από την επόμενη εβδομάδα, οι κάτοικοι δεκαοκτώ ορεινών χωριών του δήμου θα μπορούν να καλούν ένα μικρό λεωφορείο, όπως καλούν ένα ταξί. Το λεωφορείο δεν θα έχει σταθερά δρομολόγια· θα περνά μόνο από τα χωριά όπου κάποιος έχει κάνει κράτηση.", "From next week, residents of eighteen mountain villages in the municipality will be able to call a minibus, the way they call a taxi. The bus will not have fixed routes; it will pass only through the villages where someone has made a booking."),
  L("Εκφωνητής", "m", "Οι κρατήσεις θα γίνονται μέσω μιας εφαρμογής ή, για όσους δεν έχουν έξυπνο κινητό, με ένα απλό τηλεφώνημα στο κέντρο του δήμου, τουλάχιστον μία ώρα πριν. Το εισιτήριο θα κοστίζει όσο και στο αστικό λεωφορείο, ενώ οι συνταξιούχοι θα ταξιδεύουν δωρεάν.", "Bookings will be made through an app or, for those who don't have a smartphone, with a simple phone call to the municipal centre, at least an hour beforehand. The ticket will cost the same as on the city bus, while pensioners will travel free."),
  L("Εκφωνητής", "m", "Μέχρι σήμερα, τα περισσότερα από αυτά τα χωριά είχαν ένα λεωφορείο δύο φορές την εβδομάδα, που συχνά έκανε τη διαδρομή σχεδόν άδειο. Ο δήμαρχος ελπίζει ότι η νέα υπηρεσία θα βοηθήσει κυρίως τους ηλικιωμένους να πηγαίνουν στον γιατρό και στην αγορά χωρίς να εξαρτώνται από συγγενείς.", "Until now, most of these villages had a bus twice a week, which often made the journey almost empty. The mayor hopes the new service will mainly help older people get to the doctor and the market without depending on relatives."),
 ],
 "questions": [
  Q("Σε τι διαφέρει το νέο λεωφορείο;", ["Είναι ηλεκτρικό", "Δεν έχει σταθερά δρομολόγια και περνά μόνο όπου υπάρχει κράτηση", "Πηγαίνει μόνο στην πρωτεύουσα", "Κινείται μόνο τη νύχτα"], 1, "Το λεωφορείο δεν θα έχει σταθερά δρομολόγια· θα περνά μόνο από τα χωριά όπου κάποιος έχει κάνει κράτηση"),
  Q("Πώς μπορεί να κλείσει θέση κάποιος χωρίς έξυπνο κινητό;", ["Με ένα τηλεφώνημα στο κέντρο του δήμου", "Μόνο από το καφενείο του χωριού", "Με επιστολή", "Δεν μπορεί"], 0, "με ένα απλό τηλεφώνημα στο κέντρο του δήμου"),
  Q("Πόσο θα κοστίζει το εισιτήριο για τους συνταξιούχους;", ["Όσο ένα ταξί", "Το μισό", "Τίποτα", "Όσο το αστικό λεωφορείο"], 2, "οι συνταξιούχοι θα ταξιδεύουν δωρεάν"),
  Q("Ποιο ήταν το πρόβλημα με το παλιό λεωφορείο;", ["Ήταν πολύ ακριβό", "Περνούσε δύο φορές την εβδομάδα και συχνά ήταν σχεδόν άδειο", "Χαλούσε συνέχεια", "Δεν σταματούσε στα χωριά"], 1, "είχαν ένα λεωφορείο δύο φορές την εβδομάδα, που συχνά έκανε τη διαδρομή σχεδόν άδειο"),
 ],
 "gloss": {"ορεινών": "ορεινός — mountain, mountainous", "δρομολόγια": "δρομολόγιο — route, scheduled service", "κράτηση": "κράτηση — booking, reservation", "εφαρμογής": "εφαρμογή — app; application", "τηλεφώνημα": "τηλεφώνημα — phone call", "αστικό": "αστικός — urban, city (bus)", "εξαρτώνται": "εξαρτώμαι — to depend"},
})
ITEMS.append({
 "id": "l225-vm-odigos-scholikou", "title": "Μήνυμα από τον οδηγό του σχολικού", "title_en": "Message from the school bus driver", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον οδηγό του σχολικού λεωφορείου που παίρνει την κόρη σας.",
 "script": [
  L("Οδηγός", "m", "Καλησπέρα, κυρία Παππά, ο Θανάσης είμαι, ο οδηγός του σχολικού. Σας παίρνω για τη Δανάη, για να σας ενημερώσω για κάποιες αλλαγές από τη Δευτέρα.", "Good afternoon, Ms Pappa, it's Thanasis, the school bus driver. I'm calling about Danai, to let you know about some changes from Monday."),
  L("Οδηγός", "m", "Ξεκινούν έργα στην οδό Κύπρου και ο δρόμος θα είναι κλειστός για έναν μήνα περίπου. Έτσι, δεν θα μπορώ να σταματάω έξω από την πολυκατοικία σας. Η πιο κοντινή στάση θα είναι στη γωνία με την Αγίας Σοφίας, μπροστά στο φαρμακείο, δύο τετράγωνα πιο κάτω.", "Roadworks are starting on Kyprou Street and the road will be closed for about a month. So I won't be able to stop outside your apartment block. The nearest stop will be at the corner with Agias Sofias, in front of the pharmacy, two blocks further down."),
  L("Οδηγός", "m", "Επειδή θα πρέπει να κάνω μεγαλύτερο κύκλο, θα περνάω δέκα λεπτά νωρίτερα το πρωί, δηλαδή στις επτά και είκοσι αντί για επτά και μισή. Το μεσημέρι η ώρα μένει ίδια. Αν δεν μπορεί κάποιος να τη συνοδεύει ως τη γωνία, πείτε μου, να το συζητήσουμε με το σχολείο.", "Because I'll have to make a bigger loop, I'll come by ten minutes earlier in the morning, that is at twenty past seven instead of half past seven. At midday the time stays the same. If no one can walk her to the corner, tell me, so we can discuss it with the school."),
  L("Οδηγός", "m", "Α, και κάτι ακόμη: η Δανάη ξέχασε σήμερα το μπουφάν της στο λεωφορείο. Το έχω φυλάξει και θα της το δώσω τη Δευτέρα. Καλό σαββατοκύριακο!", "Oh, and one more thing: Danai left her jacket on the bus today. I've kept it and I'll give it to her on Monday. Have a nice weekend!"),
 ],
 "questions": [
  Q("Γιατί αλλάζει η στάση;", ["Γιατί μετακόμισε το σχολείο", "Γιατί ξεκινούν έργα και ο δρόμος θα είναι κλειστός", "Γιατί άλλαξε οδηγός", "Γιατί παραπονέθηκαν οι γείτονες"], 1, "Ξεκινούν έργα στην οδό Κύπρου και ο δρόμος θα είναι κλειστός"),
  Q("Πού θα είναι η νέα στάση;", ["Έξω από την πολυκατοικία", "Μπροστά στο σχολείο", "Στη γωνία με την Αγίας Σοφίας, μπροστά στο φαρμακείο", "Δίπλα σε ένα περίπτερο"], 2, "στη γωνία με την Αγίας Σοφίας, μπροστά στο φαρμακείο"),
  Q("Τι ώρα θα περνά το πρωί;", ["Στις επτά και μισή", "Στις επτά και είκοσι", "Στις επτά και σαράντα", "Στις οκτώ"], 1, "στις επτά και είκοσι αντί για επτά και μισή"),
  Q("Τι ξέχασε η Δανάη στο λεωφορείο;", ["Την τσάντα της", "Το κινητό της", "Το μπουφάν της", "Ένα βιβλίο"], 2, "η Δανάη ξέχασε σήμερα το μπουφάν της στο λεωφορείο"),
 ],
 "gloss": {"σχολικού": "σχολικό — school bus (short for σχολικό λεωφορείο)", "έργα": "έργα — roadworks, construction", "πολυκατοικία": "πολυκατοικία — apartment block", "τετράγωνα": "τετράγωνο — (city) block", "κύκλο": "κύκλος — circle; loop, detour", "συνοδεύει": "συνοδεύω — to accompany", "φυλάξει": "φυλάω — to keep, to look after"},
})
ITEMS.append({
 "id": "l225-c1-mono-fantasmatiki-donisi", "title": "Το κινητό που «δονείται» χωρίς να δονείται", "title_en": "The phone that 'vibrates' without vibrating", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή ψυχολογίας για την τεχνολογία και τον εγκέφαλο.",
 "script": [
  L("Ομιλητής", "m", "Σας έχει συμβεί να νιώσετε το κινητό να δονείται στην τσέπη σας, να το βγάλετε βιαστικά, και να διαπιστώσετε ότι δεν υπάρχει καμία κλήση και κανένα μήνυμα; Αν ναι, δεν είστε οι μόνοι. Οι ερευνητές το ονομάζουν «φαντασματική δόνηση», και είναι εξαιρετικά διαδεδομένη.", "Has it happened to you that you felt your phone vibrate in your pocket, took it out hurriedly, and found there was no call and no message? If so, you are not alone. Researchers call it 'phantom vibration', and it is extremely widespread."),
  L("Ομιλητής", "m", "Σε μία από τις πρώτες σχετικές έρευνες, σε προσωπικό ενός νοσοκομείου, περίπου δύο στους τρεις ανέφεραν ότι το είχαν ζήσει. Σε μεταγενέστερες έρευνες με φοιτητές, τα ποσοστά ήταν ακόμη υψηλότερα. Οι περισσότεροι, πάντως, δηλώνουν ότι δεν τους ενοχλεί ιδιαίτερα.", "In one of the first studies on the subject, among hospital staff, about two in three said they had experienced it. In later studies with university students, the percentages were even higher. Most, though, say it does not particularly bother them."),
  L("Ομιλητής", "m", "Πώς εξηγείται; Ο εγκέφαλος δέχεται συνεχώς μικρά ερεθίσματα από το δέρμα: το τρίψιμο του υφάσματος, μια σύσπαση ενός μυός. Όταν περιμένουμε ένα μήνυμα, τα ερμηνεύουμε πιο εύκολα ως δόνηση. Από τη σκοπιά του εγκεφάλου, ένας ψεύτικος συναγερμός κοστίζει λίγο, ενώ μια χαμένη κλήση μπορεί να κοστίσει πολύ· γι’ αυτό προτιμά να κάνει λάθος προς τη μία πλευρά.", "How is it explained? The brain constantly receives small stimuli from the skin: the rubbing of fabric, a twitch of a muscle. When we are expecting a message, we more readily interpret them as a vibration. From the brain's point of view, a false alarm costs little, while a missed call can cost a lot; so it prefers to err on one side."),
  L("Ομιλητής", "m", "Το φαινόμενο δεν θεωρείται ασθένεια, αλλά είναι ενδεικτικό του πόσο έχει προσαρμοστεί η προσοχή μας στη συσκευή. Όσοι θέλουν να το περιορίσουν, μπορούν να αλλάξουν τσέπη, να απενεργοποιήσουν τη δόνηση ή, απλώς, να αφήνουν το κινητό σε ένα άλλο δωμάτιο για λίγες ώρες. Συνήθως, οι «φαντασματικές» δονήσεις αραιώνουν μέσα σε λίγες μέρες.", "The phenomenon is not considered an illness, but it is telling of how far our attention has adapted to the device. Those who want to reduce it can change pockets, switch off vibration or simply leave the phone in another room for a few hours. Usually the 'phantom' vibrations become less frequent within a few days."),
 ],
 "questions": [
  Q("Τι είναι η «φαντασματική δόνηση»;", ["Μια βλάβη των κινητών", "Η αίσθηση ότι το κινητό δονείται ενώ δεν δονείται", "Ένα είδος ήχου κλήσης", "Ένας φόβος για τα κινητά"], 1, "να νιώσετε το κινητό να δονείται ... και να διαπιστώσετε ότι δεν υπάρχει καμία κλήση"),
  Q("Τι έδειξε μία από τις πρώτες έρευνες σε νοσοκομείο;", ["Ότι κανείς δεν το είχε ζήσει", "Ότι περίπου δύο στους τρεις το είχαν ζήσει", "Ότι αφορά μόνο τους γιατρούς", "Ότι προκαλεί πόνο"], 1, "περίπου δύο στους τρεις ανέφεραν ότι το είχαν ζήσει"),
  Q("Γιατί, σύμφωνα με τον ομιλητή, ο εγκέφαλος «κάνει λάθος» προς αυτή την πλευρά;", ["Γιατί ένας ψεύτικος συναγερμός κοστίζει λιγότερο από μια χαμένη κλήση", "Γιατί το δέρμα δεν στέλνει ερεθίσματα", "Γιατί τα κινητά δονούνται πολύ δυνατά", "Γιατί κουράζεται το βράδυ"], 0, "ένας ψεύτικος συναγερμός κοστίζει λίγο, ενώ μια χαμένη κλήση μπορεί να κοστίσει πολύ"),
  Q("Τι προτείνει σε όσους θέλουν να το περιορίσουν;", ["Να αγοράσουν καινούργιο κινητό", "Να δουν γιατρό", "Να αλλάξουν τσέπη, να κλείσουν τη δόνηση ή να αφήνουν το κινητό σε άλλο δωμάτιο", "Να έχουν το κινητό πάντα στο χέρι"], 2, "μπορούν να αλλάξουν τσέπη, να απενεργοποιήσουν τη δόνηση ή, απλώς, να αφήνουν το κινητό σε ένα άλλο δωμάτιο"),
 ],
 "gloss": {"δονείται": "δονούμαι — to vibrate", "φαντασματική": "φαντασματικός — phantom, ghostly", "διαδεδομένη": "διαδεδομένος — widespread", "μεταγενέστερες": "μεταγενέστερος — later, subsequent", "ερεθίσματα": "ερέθισμα — stimulus", "σύσπαση": "σύσπαση — contraction, twitch", "σκοπιά": "σκοπιά — point of view; lookout", "συναγερμός": "συναγερμός — alarm", "ενδεικτικό": "ενδεικτικός — indicative, telling", "αραιώνουν": "αραιώνω — to become less frequent, thin out"},
})
ITEMS.append({
 "id": "l225-c1-int-diapragmateftis", "title": "Ο διαπραγματευτής της αστυνομίας", "title_en": "The police crisis negotiator", "type": "interview", "level": "C1",
 "context_el": "Ένας αστυνομικός διαπραγματευτής μιλά σε μια ραδιοφωνική εκπομπή για τη δουλειά του σε καταστάσεις κρίσης.",
 "script": [
  L("Δημοσιογράφος", "f", "Στις ταινίες, ο διαπραγματευτής φτάνει με ένα μεγάφωνο και σε δέκα λεπτά όλα έχουν λυθεί. Πόσο μοιάζει αυτό με την πραγματικότητα;", "In films, the negotiator arrives with a megaphone and in ten minutes everything is resolved. How much does that resemble reality?"),
  L("Διαπραγματευτής", "m", "Σχεδόν καθόλου. Πρώτον, οι περισσότερες υποθέσεις μας δεν είναι ομηρίες με ληστές, αλλά άνθρωποι σε απόγνωση, που απειλούν να κάνουν κακό στον εαυτό τους. Δεύτερον, ο χρόνος δουλεύει υπέρ μας. Όσο περισσότερο μιλάμε, τόσο πέφτει η ένταση και τόσο πιο καθαρά αρχίζει να σκέφτεται ο άλλος. Μια διαπραγμάτευση μπορεί να κρατήσει ώρες.", "Hardly at all. First, most of our cases are not hostage situations with robbers but people in despair who are threatening to harm themselves. Second, time works in our favour. The longer we talk, the more the tension drops and the more clearly the other person starts to think. A negotiation can last hours."),
  L("Δημοσιογράφος", "f", "Και τι λέτε όλες αυτές τις ώρες;", "And what do you say all those hours?"),
  L("Διαπραγματευτής", "m", "Λιγότερα απ’ όσα φαντάζεστε. Το βασικό μας εργαλείο είναι η ενεργητική ακρόαση. Επαναλαμβάνουμε με δικά μας λόγια αυτό που μας είπε, ονομάζουμε το συναίσθημα που ακούμε, «ακούγεστε πολύ θυμωμένος», κάνουμε παύσεις. Ο άνθρωπος απέναντι πρέπει να νιώσει ότι κάποιος επιτέλους τον ακούει. Μόνο τότε μπορεί να αρχίσει να μας εμπιστεύεται.", "Less than you imagine. Our main tool is active listening. We repeat in our own words what they told us, we name the emotion we hear, 'you sound very angry', we pause. The person opposite must feel that someone is finally listening. Only then can they start to trust us."),
  L("Δημοσιογράφος", "f", "Υπάρχουν πράγματα που δεν λέτε ποτέ;", "Are there things you never say?"),
  L("Διαπραγματευτής", "m", "Βεβαίως. Δεν λέμε ποτέ ψέματα, γιατί αν μας πιάσουν σε ένα ψέμα, η εμπιστοσύνη χάνεται για πάντα. Αποφεύγουμε επίσης το ξερό «όχι»· προτιμάμε να πούμε «αυτό είναι δύσκολο, ας δούμε τι μπορούμε να κάνουμε». Και ποτέ δεν λέμε «σε καταλαβαίνω απόλυτα». Κανείς δεν καταλαβαίνει απόλυτα τι περνά ένας άλλος, και ο άνθρωπος σε κρίση το νιώθει αμέσως.", "Of course. We never lie, because if they catch us in a lie, trust is lost for ever. We also avoid a flat 'no'; we prefer to say 'that's difficult, let's see what we can do'. And we never say 'I understand you completely'. No one completely understands what another person is going through, and a person in crisis senses it immediately."),
 ],
 "questions": [
  Q("Ποιες είναι οι περισσότερες υποθέσεις του διαπραγματευτή;", ["Ομηρίες με ληστές", "Άνθρωποι σε απόγνωση που απειλούν να κάνουν κακό στον εαυτό τους", "Διαδηλώσεις", "Απαγωγές παιδιών"], 1, "άνθρωποι σε απόγνωση, που απειλούν να κάνουν κακό στον εαυτό τους"),
  Q("Γιατί ο χρόνος δουλεύει υπέρ των διαπραγματευτών;", ["Γιατί κουράζεται ο άλλος και παραδίνεται", "Γιατί όσο μιλούν πέφτει η ένταση και ο άλλος σκέφτεται πιο καθαρά", "Γιατί φτάνουν ενισχύσεις", "Γιατί νυχτώνει"], 1, "Όσο περισσότερο μιλάμε, τόσο πέφτει η ένταση και τόσο πιο καθαρά αρχίζει να σκέφτεται ο άλλος"),
  Q("Τι περιλαμβάνει η ενεργητική ακρόαση, σύμφωνα με τον ίδιο;", ["Γρήγορες απαντήσεις και υποσχέσεις", "Επανάληψη με δικά τους λόγια, ονομασία του συναισθήματος και παύσεις", "Συνεχείς ερωτήσεις για τα γεγονότα", "Αυστηρές προειδοποιήσεις"], 1, "Επαναλαμβάνουμε με δικά μας λόγια ... ονομάζουμε το συναίσθημα ... κάνουμε παύσεις"),
  Q("Γιατί δεν λένε ποτέ «σε καταλαβαίνω απόλυτα»;", ["Γιατί είναι αγενές", "Γιατί απαγορεύεται από τον νόμο", "Γιατί κανείς δεν καταλαβαίνει απόλυτα τι περνά ένας άλλος, και ο άνθρωπος σε κρίση το νιώθει", "Γιατί ακούγεται πολύ επίσημο"], 2, "Κανείς δεν καταλαβαίνει απόλυτα τι περνά ένας άλλος, και ο άνθρωπος σε κρίση το νιώθει αμέσως"),
 ],
 "gloss": {"διαπραγματευτής": "διαπραγματευτής — negotiator", "μεγάφωνο": "μεγάφωνο — megaphone, loudspeaker", "ομηρίες": "ομηρία — hostage situation", "απόγνωση": "απόγνωση — despair", "ένταση": "ένταση — tension; intensity", "ενεργητική ακρόαση": "ενεργητική ακρόαση — active listening", "παύσεις": "παύση — pause", "εμπιστοσύνη": "εμπιστοσύνη — trust", "ξερό": "ξερός — dry; (of a reply) curt, flat"},
})
rnd = random.Random(225)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-225.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
