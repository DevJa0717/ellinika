# Source for library/listening/listening-31.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l31.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l31-ann-krouaziera", "title": "Ανακοίνωση σε κρουαζιερόπλοιο", "title_en": "An announcement on a cruise ship", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση από τα μεγάφωνα ενός κρουαζιερόπλοιου.",
 "script": [
  L("Εκφωνήτρια", "f", "Καλημέρα σας, κυρίες και κύριοι. Σε περίπου μισή ώρα το πλοίο μας θα αγκυροβολήσει στη Σαντορίνη. Επειδή το λιμάνι των Φηρών είναι πολύ μικρό για μεγάλα πλοία, η αποβίβαση θα γίνει με μικρές βάρκες, τις λάντζες, οι οποίες θα ξεκινήσουν στις εννιά και θα αναχωρούν κάθε δεκαπέντε λεπτά από το κατάστρωμα τρία.", "Good morning, ladies and gentlemen. In about half an hour our ship will anchor at Santorini. Because the port of Fira is too small for large ships, disembarkation will be by small boats, the tenders, which will start at nine and leave every fifteen minutes from deck three."),
  L("Εκφωνήτρια", "f", "Από το παλιό λιμάνι μπορείτε να ανεβείτε στα Φηρά με το τελεφερίκ ή με τα πόδια, από ένα μονοπάτι με εξακόσια περίπου σκαλιά. Παρακαλούμε τους επιβάτες να μη χρησιμοποιούν γαϊδουράκια· οι κτηνίατροι προειδοποιούν ότι τα ζώα υποφέρουν από το βάρος και τη ζέστη.", "From the old port you can go up to Fira by cable car or on foot, by a path with about six hundred steps. We ask passengers not to use the donkeys; vets warn that the animals suffer from the weight and the heat."),
  L("Εκφωνήτρια", "f", "Η τελευταία λάντζα για την επιστροφή στο πλοίο θα αναχωρήσει στις πέντε και μισή ακριβώς. Μην ξεχάσετε την κάρτα επιβάτη σας, γιατί χωρίς αυτήν δεν θα μπορείτε να επιβιβαστείτε ξανά. Σας ευχόμαστε μια υπέροχη μέρα.", "The last tender back to the ship will leave at exactly half past five. Don't forget your passenger card, because without it you won't be able to board again. We wish you a wonderful day."),
 ],
 "questions": [
  Q("Γιατί η αποβίβαση θα γίνει με μικρές βάρκες;", ["Γιατί έχει κύμα", "Γιατί το λιμάνι των Φηρών είναι πολύ μικρό για μεγάλα πλοία", "Γιατί υπάρχει απεργία", "Γιατί είναι πιο φθηνό"], 1, "το λιμάνι των Φηρών είναι πολύ μικρό για μεγάλα πλοία"),
  Q("Τι ζητούν από τους επιβάτες για τα γαϊδουράκια;", ["Να τα ταΐζουν", "Να μην τα χρησιμοποιούν", "Να πληρώνουν μετρητά", "Να κλείνουν θέση νωρίς"], 1, "Παρακαλούμε τους επιβάτες να μη χρησιμοποιούν γαϊδουράκια"),
  Q("Τι χρειάζονται οι επιβάτες για να επιβιβαστούν ξανά;", ["Το διαβατήριο", "Την κάρτα επιβάτη", "Ένα εισιτήριο για τη λάντζα", "Την απόδειξη του τελεφερίκ"], 1, "Μην ξεχάσετε την κάρτα επιβάτη σας, γιατί χωρίς αυτήν δεν θα μπορείτε να επιβιβαστείτε ξανά"),
 ],
 "gloss": {"κρουαζιερόπλοιου": "κρουαζιερόπλοιο — cruise ship", "θα αγκυροβολήσει": "αγκυροβολώ — to anchor", "αποβίβαση": "αποβίβαση — disembarkation", "λάντζες": "λάντζα — tender (boat)", "κατάστρωμα": "κατάστρωμα — deck", "τελεφερίκ": "τελεφερίκ — cable car", "σκαλιά": "σκαλί — step", "γαϊδουράκια": "γαϊδουράκι — little donkey", "υποφέρουν": "υποφέρω — to suffer", "να επιβιβαστείτε": "επιβιβάζομαι — to board"},
})

ITEMS.append({
 "id": "l31-vm-pezoporia", "title": "Αλλαγή σχεδίων για την πεζοπορία", "title_en": "A change of plans for the hike", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από έναν φίλο σας.",
 "script": [
  L("Νίκος", "m", "Γεια σου, Κατερίνα, ο Νίκος είμαι. Σε παίρνω για την πεζοπορία της Κυριακής στην Πάρνηθα. Η πρόγνωση δίνει καταιγίδες από το μεσημέρι, και ο οδηγός της ομάδας λέει ότι δεν είναι ασφαλές να ανεβούμε στην κορυφή με κεραυνούς.", "Hi Katerina, it's Nikos. I'm calling about Sunday's hike on Parnitha. The forecast shows thunderstorms from midday, and the group leader says it's not safe to go up to the summit with lightning."),
  L("Νίκος", "m", "Έτσι, έχουμε δύο επιλογές: ή ξεκινάμε πολύ νωρίτερα, στις έξι αντί για τις εννιά, και κάνουμε μια πιο σύντομη διαδρομή μέχρι το καταφύγιο, ή αναβάλλουμε για την επόμενη Κυριακή. Οι περισσότεροι προτιμούν να ξεκινήσουμε νωρίς, αλλά θέλουμε να ρωτήσουμε όλους.", "So we have two options: either we start much earlier, at six instead of nine, and do a shorter route to the refuge, or we postpone until next Sunday. Most people would rather start early, but we want to ask everyone."),
  L("Νίκος", "m", "Αν έρθεις, φέρε οπωσδήποτε αδιάβροχο και ένα ζεστό ρούχο, γιατί στο βουνό η θερμοκρασία πέφτει απότομα. Στείλε μου μήνυμα μέχρι αύριο το βράδυ, για να ξέρουμε πόσα αυτοκίνητα θα χρειαστούμε.", "If you come, be sure to bring a raincoat and something warm, because on the mountain the temperature drops sharply. Text me by tomorrow evening, so we know how many cars we'll need."),
 ],
 "questions": [
  Q("Γιατί πρέπει να αλλάξει το σχέδιο;", ["Γιατί ο οδηγός είναι άρρωστος", "Γιατί η πρόγνωση δίνει καταιγίδες από το μεσημέρι", "Γιατί έκλεισε το καταφύγιο", "Γιατί δεν υπάρχουν αυτοκίνητα"], 1, "Η πρόγνωση δίνει καταιγίδες από το μεσημέρι"),
  Q("Τι προτιμούν οι περισσότεροι;", ["Να αναβάλουν την πεζοπορία", "Να ξεκινήσουν νωρίς με πιο σύντομη διαδρομή", "Να πάνε σε άλλο βουνό", "Να ανέβουν στην κορυφή όπως είχαν πει"], 1, "Οι περισσότεροι προτιμούν να ξεκινήσουμε νωρίς"),
  Q("Γιατί θέλει ο Νίκος απάντηση μέχρι αύριο το βράδυ;", ["Για να κλείσει τραπέζι", "Για να ξέρουν πόσα αυτοκίνητα θα χρειαστούν", "Για να αγοράσει εισιτήρια", "Για να ενημερώσει το καταφύγιο"], 1, "για να ξέρουμε πόσα αυτοκίνητα θα χρειαστούμε"),
 ],
 "gloss": {"πεζοπορία": "πεζοπορία — hike, hiking", "πρόγνωση": "πρόγνωση (καιρού) — (weather) forecast", "καταιγίδες": "καταιγίδα — thunderstorm", "οδηγός": "οδηγός — guide, leader", "κορυφή": "κορυφή — summit", "κεραυνούς": "κεραυνός — lightning bolt", "καταφύγιο": "καταφύγιο — (mountain) refuge", "αναβάλλουμε": "αναβάλλω — to postpone", "αδιάβροχο": "αδιάβροχο — raincoat", "απότομα": "απότομα — sharply, suddenly"},
})

ITEMS.append({
 "id": "l31-dia-raftis", "title": "Μεταποίηση σε ένα κουστούμι", "title_en": "Altering a suit", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα ραφείο.",
 "script": [
  L("Πελάτης", "m", "Καλημέρα. Αγόρασα αυτό το κουστούμι για τον γάμο του αδελφού μου, αλλά το παντελόνι είναι πολύ μακρύ και το σακάκι λίγο φαρδύ στους ώμους.", "Good morning. I bought this suit for my brother's wedding, but the trousers are too long and the jacket is a bit wide in the shoulders."),
  L("Ράφτρα", "f", "Ας το δοκιμάσετε, να δούμε. Το παντελόνι είναι εύκολο: θα το κοντύνω τρία εκατοστά. Οι ώμοι όμως είναι πιο δύσκολη υπόθεση, γιατί πρέπει να ξηλώσω το μανίκι. Σας προτείνω να το στενέψω λίγο στη μέση· έτσι θα δείχνει καλύτερα και δεν θα χρειαστεί να πειράξουμε τους ώμους.", "Try it on, let's see. The trousers are easy: I'll shorten them by three centimetres. The shoulders, though, are trickier, because I have to unpick the sleeve. I suggest taking it in a little at the waist; that way it'll look better and we won't need to touch the shoulders."),
  L("Πελάτης", "m", "Εντάξει, εσείς ξέρετε καλύτερα. Πόσο θα κοστίσει και πότε θα είναι έτοιμο; Ο γάμος είναι σε δέκα μέρες.", "All right, you know best. How much will it cost and when will it be ready? The wedding is in ten days."),
  L("Ράφτρα", "f", "Το κόντεμα κοστίζει δώδεκα ευρώ και το στένεμα είκοσι. Θα είναι έτοιμο την Πέμπτη. Καλό είναι να έρθετε με τα παπούτσια που θα φορέσετε στον γάμο, για να ελέγξουμε το μήκος του παντελονιού με αυτά.", "The shortening costs twelve euros and the taking-in twenty. It'll be ready on Thursday. It's a good idea to come with the shoes you'll wear at the wedding, so we can check the length of the trousers with them."),
 ],
 "questions": [
  Q("Ποιο είναι το πρόβλημα με το παντελόνι;", ["Είναι στενό", "Είναι πολύ μακρύ", "Έχει σκιστεί", "Είναι κοντό"], 1, "το παντελόνι είναι πολύ μακρύ"),
  Q("Τι προτείνει η ράφτρα για το σακάκι;", ["Να αλλάξει τους ώμους", "Να το στενέψει λίγο στη μέση", "Να αγοράσει καινούργιο", "Να κοντύνει τα μανίκια"], 1, "Σας προτείνω να το στενέψω λίγο στη μέση"),
  Q("Γιατί πρέπει ο πελάτης να φέρει τα παπούτσια του;", ["Για να τα γυαλίσει η ράφτρα", "Για να ελεγχθεί το μήκος του παντελονιού", "Για να ταιριάξει το χρώμα", "Για να δει αν του χωράνε"], 1, "για να ελέγξουμε το μήκος του παντελονιού με αυτά"),
 ],
 "gloss": {"ραφείο": "ραφείο — tailor's shop", "κουστούμι": "κουστούμι — suit", "σακάκι": "σακάκι — jacket", "φαρδύ": "φαρδύς — wide, loose", "ώμους": "ώμος — shoulder", "θα το κοντύνω": "κονταίνω — to shorten", "να ξηλώσω": "ξηλώνω — to unpick, take apart", "μανίκι": "μανίκι — sleeve", "να το στενέψω": "στενεύω — to take in, narrow", "κόντεμα": "κόντεμα — shortening", "στένεμα": "στένεμα — taking in", "μήκος": "μήκος — length"},
})

ITEMS.append({
 "id": "l31-dia-emvolio", "title": "Εμβόλια για ένα ταξίδι", "title_en": "Vaccines for a trip", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα ιατρείο, όπου μια ασθενής ρωτά για εμβόλια πριν από ένα ταξίδι.",
 "script": [
  L("Ασθενής", "f", "Καλημέρα, γιατρέ. Τον Φεβρουάριο θα πάω τρεις εβδομάδες στην Κένυα, για εθελοντική δουλειά σε ένα σχολείο. Τι εμβόλια χρειάζομαι;", "Good morning, doctor. In February I'm going to Kenya for three weeks, for volunteer work in a school. What vaccines do I need?"),
  L("Γιατρός", "m", "Καλά κάνατε και ήρθατε νωρίς, γιατί κάποια εμβόλια θέλουν χρόνο για να δράσουν. Για την Κένυα σας συνιστώ οπωσδήποτε το εμβόλιο του κίτρινου πυρετού, που πρέπει να γίνει τουλάχιστον δέκα μέρες πριν από την αναχώρηση. Θα σας δώσουμε και ένα διεθνές πιστοποιητικό, που μπορεί να σας το ζητήσουν στα σύνορα.", "You did well to come early, because some vaccines need time to work. For Kenya I definitely recommend the yellow fever vaccine, which must be given at least ten days before departure. We'll also give you an international certificate, which you may be asked for at the border."),
  L("Ασθενής", "f", "Και για την ελονοσία;", "And for malaria?"),
  L("Γιατρός", "m", "Για την ελονοσία δεν υπάρχει εμβόλιο που να κυκλοφορεί ευρέως για ταξιδιώτες, οπότε θα σας γράψω χάπια. Θα αρχίσετε να τα παίρνετε λίγες μέρες πριν από το ταξίδι και θα συνεχίσετε για ένα διάστημα μετά την επιστροφή. Το πιο σημαντικό όμως είναι να προστατεύεστε από τα κουνούπια: εντομοαπωθητικό, μακριά μανίκια το βράδυ και κουνουπιέρα στο κρεβάτι.", "For malaria there's no vaccine widely available for travellers, so I'll prescribe you pills. You'll start taking them a few days before the trip and continue for a while after you return. The most important thing, though, is to protect yourself from mosquitoes: insect repellent, long sleeves in the evening and a mosquito net over the bed."),
 ],
 "questions": [
  Q("Γιατί ο γιατρός λέει ότι καλά έκανε η ασθενής και ήρθε νωρίς;", ["Γιατί τα εμβόλια ακριβαίνουν", "Γιατί κάποια εμβόλια θέλουν χρόνο για να δράσουν", "Γιατί το ιατρείο κλείνει τον Φεβρουάριο", "Γιατί χρειάζεται βίζα"], 1, "κάποια εμβόλια θέλουν χρόνο για να δράσουν"),
  Q("Τι ισχύει για το εμβόλιο του κίτρινου πυρετού;", ["Γίνεται μετά την επιστροφή", "Πρέπει να γίνει τουλάχιστον δέκα μέρες πριν από την αναχώρηση", "Δεν χρειάζεται για την Κένυα", "Γίνεται στο αεροδρόμιο"], 1, "πρέπει να γίνει τουλάχιστον δέκα μέρες πριν από την αναχώρηση"),
  Q("Τι θεωρεί ο γιατρός το πιο σημαντικό για την ελονοσία;", ["Το εμβόλιο", "Την προστασία από τα κουνούπια", "Να μην πίνει νερό της βρύσης", "Να μένει σε ξενοδοχείο"], 1, "Το πιο σημαντικό όμως είναι να προστατεύεστε από τα κουνούπια"),
 ],
 "gloss": {"εμβόλια": "εμβόλιο — vaccine", "εθελοντική": "εθελοντικός — voluntary, volunteer", "να δράσουν": "δρω — to act, take effect", "κίτρινου πυρετού": "κίτρινος πυρετός — yellow fever", "πιστοποιητικό": "πιστοποιητικό — certificate", "σύνορα": "σύνορα — border", "ελονοσία": "ελονοσία — malaria", "κουνούπια": "κουνούπι — mosquito", "εντομοαπωθητικό": "εντομοαπωθητικό — insect repellent", "κουνουπιέρα": "κουνουπιέρα — mosquito net"},
})

ITEMS.append({
 "id": "l31-mon-xoris-aftokinito", "title": "Ένας χρόνος χωρίς αυτοκίνητο", "title_en": "A year without a car", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλά σε μια ραδιοφωνική εκπομπή για τη ζωή του χωρίς αυτοκίνητο.",
 "script": [
  L("Γιάννης", "m", "Πέρσι τον Οκτώβριο, το αυτοκίνητό μου χάλασε και ο μηχανικός μού είπε ότι η επισκευή θα κόστιζε περισσότερο από όσο άξιζε. Αποφάσισα να μην αγοράσω καινούργιο, τουλάχιστον για έναν χρόνο, για να δω αν μπορώ να ζήσω χωρίς αυτό στη Θεσσαλονίκη.", "Last October my car broke down and the mechanic told me the repair would cost more than it was worth. I decided not to buy a new one, at least for a year, to see whether I could live without it in Thessaloniki."),
  L("Γιάννης", "m", "Οι πρώτες εβδομάδες ήταν δύσκολες. Έπρεπε να σχεδιάζω κάθε διαδρομή, και τα ψώνια της εβδομάδας γίνονταν μια μικρή περιπέτεια. Σιγά σιγά όμως βρήκα τον ρυθμό μου. Πηγαίνω στη δουλειά με το μετρό και με ποδήλατο, ψωνίζω από τα μαγαζιά της γειτονιάς, και για τις εκδρομές νοικιάζω αυτοκίνητο κάνα δυο φορές τον μήνα.", "The first weeks were difficult. I had to plan every journey, and the weekly shopping became a little adventure. Gradually, though, I found my rhythm. I go to work by metro and by bike, I shop in the neighbourhood shops, and for trips I rent a car once or twice a month."),
  L("Γιάννης", "m", "Υπολόγισα ότι εξοικονόμησα πάνω από δύο χιλιάδες ευρώ: βενζίνη, ασφάλεια, τέλη κυκλοφορίας, πάρκινγκ. Έχασα και τέσσερα κιλά χωρίς να πατήσω σε γυμναστήριο. Το πιο απρόσμενο όμως είναι ότι γνώρισα τη γειτονιά μου. Τώρα ο μανάβης με φωνάζει με το όνομά μου.", "I calculated that I saved over two thousand euros: petrol, insurance, road tax, parking. I also lost four kilos without setting foot in a gym. But the most unexpected thing is that I got to know my neighbourhood. Now the greengrocer calls me by my name."),
 ],
 "questions": [
  Q("Γιατί ο Γιάννης έμεινε χωρίς αυτοκίνητο;", ["Του το έκλεψαν", "Η επισκευή θα κόστιζε περισσότερο από όσο άξιζε", "Έχασε το δίπλωμά του", "Το πούλησε για να ταξιδέψει"], 1, "η επισκευή θα κόστιζε περισσότερο από όσο άξιζε"),
  Q("Πώς κάνει τις εκδρομές του;", ["Με λεωφορείο", "Νοικιάζει αυτοκίνητο κάνα δυο φορές τον μήνα", "Δανείζεται το αυτοκίνητο ενός φίλου", "Δεν κάνει πια εκδρομές"], 1, "για τις εκδρομές νοικιάζω αυτοκίνητο κάνα δυο φορές τον μήνα"),
  Q("Ποιο ήταν, κατά τον Γιάννη, το πιο απρόσμενο αποτέλεσμα;", ["Ότι εξοικονόμησε χρήματα", "Ότι γνώρισε τη γειτονιά του", "Ότι έχασε κιλά", "Ότι άργησε στη δουλειά"], 1, "Το πιο απρόσμενο όμως είναι ότι γνώρισα τη γειτονιά μου"),
 ],
 "gloss": {"χάλασε": "χαλάω — to break down", "μηχανικός": "μηχανικός — mechanic", "επισκευή": "επισκευή — repair", "άξιζε": "αξίζω — to be worth", "περιπέτεια": "περιπέτεια — adventure", "ρυθμό": "ρυθμός — rhythm, pace", "κάνα δυο": "κάνα δυο — one or two", "εξοικονόμησα": "εξοικονομώ — to save", "τέλη κυκλοφορίας": "τέλη κυκλοφορίας — road tax", "απρόσμενο": "απρόσμενος — unexpected", "μανάβης": "μανάβης — greengrocer"},
})

ITEMS.append({
 "id": "l31-rep-kournas", "title": "Η λίμνη Κουρνά", "title_en": "Lake Kournas", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από τη λίμνη Κουρνά, στον νομό Χανίων.",
 "script": [
  L("Ρεπόρτερ", "f", "Ανάμεσα σε βουνά, λίγα χιλιόμετρα από τη θάλασσα, απλώνεται η λίμνη Κουρνά, η μοναδική φυσική λίμνη γλυκού νερού της Κρήτης. Το νερό της αλλάζει χρώμα ανάλογα με την εποχή και την ώρα: το πρωί είναι γαλάζιο, το μεσημέρι πρασινωπό και το σούρουπο σχεδόν ασημένιο.", "Among the mountains, a few kilometres from the sea, lies Lake Kournas, the only natural freshwater lake in Crete. Its water changes colour depending on the season and the time of day: in the morning it's light blue, at midday greenish and at dusk almost silver."),
  L("Ρεπόρτερ", "f", "Η λίμνη τροφοδοτείται από πηγές και από τα νερά των γύρω βουνών, γι' αυτό η στάθμη της ανεβαίνει τον χειμώνα και κατεβαίνει πολύ το καλοκαίρι. Στα νερά της ζουν χελώνες, χέλια και πολλά είδη πουλιών, και η περιοχή είναι προστατευόμενη.", "The lake is fed by springs and by water from the surrounding mountains, which is why its level rises in winter and drops a lot in summer. Turtles, eels and many species of bird live in and around its waters, and the area is protected."),
  L("Ρεπόρτερ", "f", "Το καλοκαίρι, οι επισκέπτες νοικιάζουν θαλάσσια ποδήλατα ή κάνουν τον γύρο της λίμνης με τα πόδια. Οι ντόπιοι, όμως, ζητούν σεβασμό: απαγορεύεται να ταΐζετε τις χελώνες με ψωμί, γιατί τις βλάπτει, και τα σκουπίδια πρέπει να τα παίρνετε μαζί σας. Αν θέλετε ησυχία, ελάτε νωρίς το πρωί ή τον Σεπτέμβριο, όταν φεύγουν τα πλήθη.", "In summer, visitors rent pedal boats or walk round the lake. Locals, however, ask for respect: it's forbidden to feed the turtles bread, because it harms them, and you must take your rubbish with you. If you want peace and quiet, come early in the morning or in September, when the crowds leave."),
 ],
 "questions": [
  Q("Τι είναι ιδιαίτερο στη λίμνη Κουρνά;", ["Είναι η μεγαλύτερη λίμνη της Ελλάδας", "Είναι η μοναδική φυσική λίμνη γλυκού νερού της Κρήτης", "Είναι τεχνητή", "Έχει αλμυρό νερό"], 1, "η μοναδική φυσική λίμνη γλυκού νερού της Κρήτης"),
  Q("Γιατί η στάθμη της λίμνης κατεβαίνει το καλοκαίρι;", ["Γιατί την αδειάζουν για τα χωράφια", "Γιατί τροφοδοτείται από πηγές και νερά των βουνών, που λιγοστεύουν το καλοκαίρι", "Γιατί πίνουν νερό τα ζώα", "Λόγω των τουριστών"], 1, "η στάθμη της ανεβαίνει τον χειμώνα και κατεβαίνει πολύ το καλοκαίρι"),
  Q("Γιατί απαγορεύεται να ταΐζουν τις χελώνες με ψωμί;", ["Γιατί τις παχαίνει", "Γιατί τις βλάπτει", "Γιατί λερώνει το νερό", "Γιατί τις φέρνει κοντά στους ανθρώπους"], 1, "απαγορεύεται να ταΐζετε τις χελώνες με ψωμί, γιατί τις βλάπτει"),
 ],
 "gloss": {"απλώνεται": "απλώνομαι — to spread out, lie", "γλυκού νερού": "γλυκό νερό — fresh water", "πρασινωπό": "πρασινωπός — greenish", "σούρουπο": "σούρουπο — dusk", "ασημένιο": "ασημένιος — silver", "τροφοδοτείται": "τροφοδοτούμαι — to be fed, supplied", "στάθμη": "στάθμη — level", "χελώνες": "χελώνα — turtle", "χέλια": "χέλι — eel", "προστατευόμενη": "προστατευόμενος — protected", "θαλάσσια ποδήλατα": "θαλάσσιο ποδήλατο — pedal boat", "πλήθη": "πλήθος — crowd"},
})

ITEMS.append({
 "id": "l31-rep-averof", "title": "Το θωρηκτό Αβέρωφ", "title_en": "The battleship Averof", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από το πλωτό μουσείο «Αβέρωφ», στο Παλαιό Φάληρο.",
 "script": [
  L("Ρεπόρτερ", "m", "Αγκυροβολημένο στο Παλαιό Φάληρο, το «Αβέρωφ» φαίνεται από μακριά με τις ψηλές του τσιμινιέρες. Ναυπηγήθηκε στην Ιταλία το 1910 και πήρε το όνομά του από τον εθνικό ευεργέτη Γεώργιο Αβέρωφ, που άφησε στη διαθήκη του μεγάλο ποσό για την αγορά ενός πολεμικού πλοίου.", "Moored at Palaio Faliro, the Averof can be seen from afar with its tall funnels. It was built in Italy in 1910 and took its name from the national benefactor Georgios Averof, who left a large sum in his will for the purchase of a warship."),
  L("Ρεπόρτερ", "m", "Στους Βαλκανικούς Πολέμους, με κυβερνήτη τον ναύαρχο Παύλο Κουντουριώτη, το «Αβέρωφ» ήταν η ναυαρχίδα του ελληνικού στόλου και έπαιξε καθοριστικό ρόλο στις ναυμαχίες της Έλλης και της Λήμνου, που έδωσαν στην Ελλάδα τον έλεγχο του Αιγαίου.", "In the Balkan Wars, under the command of Admiral Pavlos Kountouriotis, the Averof was the flagship of the Greek fleet and played a decisive role in the naval battles of Elli and Lemnos, which gave Greece control of the Aegean."),
  L("Ρεπόρτερ", "m", "Σήμερα είναι πλωτό μουσείο. Οι επισκέπτες περπατούν στο κατάστρωμα, βλέπουν τα κανόνια, την καμπίνα του ναυάρχου και τους θαλάμους όπου κοιμούνταν οι ναύτες σε κρεμαστές κουκέτες. Είναι το μόνο θωρακισμένο καταδρομικό της εποχής του που σώζεται σε όλο τον κόσμο.", "Today it's a floating museum. Visitors walk on the deck and see the guns, the admiral's cabin and the quarters where the sailors slept in hanging bunks. It's the only armoured cruiser of its era that survives anywhere in the world."),
 ],
 "questions": [
  Q("Από πού πήρε το όνομά του το πλοίο;", ["Από έναν ναύαρχο", "Από τον ευεργέτη Γεώργιο Αβέρωφ", "Από ένα νησί", "Από τον Ιταλό ναυπηγό"], 1, "πήρε το όνομά του από τον εθνικό ευεργέτη Γεώργιο Αβέρωφ"),
  Q("Ποιος ήταν ο ρόλος του «Αβέρωφ» στους Βαλκανικούς Πολέμους;", ["Μετέφερε στρατιώτες", "Ήταν η ναυαρχίδα του στόλου και έπαιξε καθοριστικό ρόλο σε ναυμαχίες", "Ήταν νοσοκομειακό πλοίο", "Έμεινε στο λιμάνι"], 1, "ήταν η ναυαρχίδα του ελληνικού στόλου και έπαιξε καθοριστικό ρόλο στις ναυμαχίες"),
  Q("Τι είναι μοναδικό στο «Αβέρωφ» σήμερα;", ["Είναι το μεγαλύτερο πλοίο της Ελλάδας", "Είναι το μόνο θωρακισμένο καταδρομικό της εποχής του που σώζεται", "Ταξιδεύει ακόμα", "Είναι ξύλινο"], 1, "Είναι το μόνο θωρακισμένο καταδρομικό της εποχής του που σώζεται σε όλο τον κόσμο"),
 ],
 "gloss": {"πλωτό": "πλωτός — floating", "τσιμινιέρες": "τσιμινιέρα — funnel, smokestack", "Ναυπηγήθηκε": "ναυπηγούμαι — to be built (of ships)", "ευεργέτη": "ευεργέτης — benefactor", "διαθήκη": "διαθήκη — will", "ναύαρχο": "ναύαρχος — admiral", "ναυαρχίδα": "ναυαρχίδα — flagship", "στόλου": "στόλος — fleet", "ναυμαχίες": "ναυμαχία — naval battle", "θαλάμους": "θάλαμος — quarters, cabin", "κουκέτες": "κουκέτα — bunk", "θωρακισμένο καταδρομικό": "θωρακισμένο καταδρομικό — armoured cruiser"},
})

ITEMS.append({
 "id": "l31-int-aromatopoios", "title": "Μια αρωματοποιός", "title_en": "A perfumer", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια αρωματοποιό που έχει εργαστήριο στην Αθήνα.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς γίνεται κανείς αρωματοποιός; Υπάρχει σχολή;", "How does someone become a perfumer? Is there a school?"),
  L("Αρωματοποιός", "f", "Υπάρχουν λίγες σχολές στον κόσμο, κυρίως στη Γαλλία. Εγώ σπούδασα χημεία και μετά έκανα ένα μεταπτυχιακό στην Γκρας, την πόλη των αρωμάτων. Το πιο δύσκολο ήταν η εκπαίδευση της μύτης. Για δύο χρόνια μύριζα κάθε μέρα εκατοντάδες ουσίες και μάθαινα να τις αναγνωρίζω με κλειστά μάτια, όπως ένας μουσικός μαθαίνει τις νότες.", "There are a few schools in the world, mainly in France. I studied chemistry and then did a master's in Grasse, the city of perfumes. The hardest part was training the nose. For two years I smelled hundreds of substances every day and learned to recognise them with my eyes closed, the way a musician learns notes."),
  L("Δημοσιογράφος", "m", "Τα αρώματά σας εμπνέονται από την Ελλάδα;", "Are your perfumes inspired by Greece?"),
  L("Αρωματοποιός", "f", "Πάντα. Το πιο αγαπημένο μου λέγεται «Αύγουστος» και θέλει να θυμίζει ένα απόγευμα σε ένα νησί: αλάτι, σύκο, θυμάρι, και λίγη ζεστή πέτρα. Χρησιμοποιώ πολλά ελληνικά υλικά, όπως τη μαστίχα Χίου και το λάδανο από την Κρήτη, μια ρητίνη που οι βοσκοί μάζευαν παλιά από τα γένια των κατσικιών!", "Always. My favourite is called 'August' and is meant to recall an afternoon on an island: salt, fig, thyme and a little warm stone. I use many Greek ingredients, such as Chios mastic and labdanum from Crete, a resin that shepherds used to collect from the beards of goats!"),
  L("Αρωματοποιός", "f", "Ένα άρωμα είναι σαν μια ιστορία χωρίς λέξεις. Η μυρωδιά συνδέεται με τη μνήμη πιο άμεσα από οποιαδήποτε άλλη αίσθηση. Γι' αυτό, όταν ένας πελάτης μυρίζει κάτι και λέει «αυτό είναι το σπίτι της γιαγιάς μου», ξέρω ότι πέτυχα.", "A perfume is like a story without words. Smell is linked to memory more directly than any other sense. That's why, when a customer smells something and says 'that's my grandmother's house', I know I've succeeded."),
 ],
 "questions": [
  Q("Ποιο ήταν, κατά την αρωματοποιό, το πιο δύσκολο στην εκπαίδευσή της;", ["Η χημεία", "Η εκπαίδευση της μύτης", "Τα γαλλικά", "Το κόστος των σπουδών"], 1, "Το πιο δύσκολο ήταν η εκπαίδευση της μύτης"),
  Q("Τι θέλει να θυμίζει το άρωμα «Αύγουστος»;", ["Ένα χριστουγεννιάτικο βράδυ", "Ένα απόγευμα σε ένα νησί", "Έναν ανθισμένο κήπο", "Ένα δάσος με πεύκα"], 1, "θέλει να θυμίζει ένα απόγευμα σε ένα νησί"),
  Q("Πότε νιώθει η αρωματοποιός ότι πέτυχε;", ["Όταν πουλάει πολλά μπουκάλια", "Όταν ένας πελάτης συνδέει τη μυρωδιά με μια ανάμνηση", "Όταν παίρνει βραβείο", "Όταν ένα άρωμα κρατάει πολλές ώρες"], 1, "όταν ένας πελάτης μυρίζει κάτι και λέει «αυτό είναι το σπίτι της γιαγιάς μου», ξέρω ότι πέτυχα"),
 ],
 "gloss": {"αρωματοποιό": "αρωματοποιός — perfumer", "μεταπτυχιακό": "μεταπτυχιακό — master's degree", "μύτης": "μύτη — nose", "μύριζα": "μυρίζω — to smell", "ουσίες": "ουσία — substance", "νότες": "νότα — (musical) note", "εμπνέονται": "εμπνέομαι — to be inspired", "θυμάρι": "θυμάρι — thyme", "μαστίχα": "μαστίχα — mastic", "ρητίνη": "ρητίνη — resin", "γένια": "γένια — beard", "αίσθηση": "αίσθηση — sense"},
})

ITEMS.append({
 "id": "l31-mon-mixanismos", "title": "Ο Μηχανισμός των Αντικυθήρων", "title_en": "The Antikythera Mechanism", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε ένα απόσπασμα από μια διάλεξη για τον Μηχανισμό των Αντικυθήρων.",
 "script": [
  L("Αρχαιολόγος", "f", "Το 1901, σφουγγαράδες από τη Σύμη, που είχαν καταφύγει στα Αντικύθηρα εξαιτίας μιας καταιγίδας, ανακάλυψαν στον βυθό ένα αρχαίο ναυάγιο. Ανάμεσα σε χάλκινα αγάλματα, αγγεία και κοσμήματα, ανέσυραν και μερικά διαβρωμένα κομμάτια μπρούντζου, στα οποία αρχικά κανείς δεν έδωσε ιδιαίτερη σημασία.", "In 1901, sponge divers from Symi, who had taken shelter at Antikythera because of a storm, discovered an ancient shipwreck on the seabed. Among bronze statues, pots and jewellery, they brought up a few corroded pieces of bronze, to which at first nobody paid particular attention."),
  L("Αρχαιολόγος", "f", "Χρειάστηκαν δεκαετίες για να καταλάβουμε τι ήταν. Τα κομμάτια περιείχαν οδοντωτούς τροχούς, γρανάζια δηλαδή, με μια ακρίβεια που δεν ξανασυναντάμε σε κανένα γνωστό αντικείμενο για περισσότερο από χίλια χρόνια. Ο Μηχανισμός, που χρονολογείται γύρω στο δεύτερο ή τον πρώτο αιώνα π.Χ., ήταν ένα είδος αστρονομικού υπολογιστή: γυρίζοντας μια λαβή, μπορούσε κανείς να δει τη θέση του Ήλιου και της Σελήνης, τις φάσεις της Σελήνης και να προβλέψει εκλείψεις.", "It took decades to understand what it was. The pieces contained toothed wheels, that is, gears, with a precision we don't meet again in any known object for more than a thousand years. The Mechanism, which dates to around the second or first century BC, was a kind of astronomical computer: by turning a handle, one could see the position of the Sun and Moon, the phases of the Moon, and predict eclipses."),
  L("Αρχαιολόγος", "f", "Η μεγάλη πρόοδος ήρθε στις αρχές του εικοστού πρώτου αιώνα, όταν οι ερευνητές χρησιμοποίησαν προηγμένη αξονική τομογραφία με ακτίνες Χ. Έτσι διαβάστηκαν χιλιάδες γράμματα από τις επιγραφές που ήταν κρυμμένες μέσα στα κομμάτια, ένα είδος εγχειριδίου χρήσης, και αποκαλύφθηκε ότι ο Μηχανισμός έδειχνε ακόμη και τον τετραετή κύκλο των αθλητικών αγώνων, ανάμεσά τους και των Ολυμπιακών.", "The great breakthrough came at the beginning of the twenty-first century, when researchers used advanced X-ray computed tomography. In this way thousands of letters were read from the inscriptions hidden inside the fragments, a kind of user's manual, and it was revealed that the Mechanism even showed the four-year cycle of athletic games, among them the Olympics."),
  L("Αρχαιολόγος", "f", "Πολλά ερωτήματα παραμένουν ανοιχτά: ποιος τον κατασκεύασε, πού, και για ποιον. Ένα πράγμα όμως είναι βέβαιο: ο Μηχανισμός μάς υποχρεώνει να αναθεωρήσουμε την εικόνα που είχαμε για την τεχνολογία του αρχαίου κόσμου.", "Many questions remain open: who built it, where, and for whom. But one thing is certain: the Mechanism forces us to revise the picture we had of the technology of the ancient world."),
 ],
 "questions": [
  Q("Πώς ανακαλύφθηκε το ναυάγιο;", ["Από αρχαιολόγους σε οργανωμένη ανασκαφή", "Από σφουγγαράδες που είχαν καταφύγει στο νησί λόγω καταιγίδας", "Από ψαράδες που έπιασαν ένα άγαλμα στα δίχτυα τους", "Από ένα υποβρύχιο του ναυτικού"], 1, "σφουγγαράδες από τη Σύμη, που είχαν καταφύγει στα Αντικύθηρα εξαιτίας μιας καταιγίδας, ανακάλυψαν στον βυθό ένα αρχαίο ναυάγιο"),
  Q("Τι μπορούσε να δείξει ο Μηχανισμός;", ["Την ώρα της ημέρας μόνο", "Τη θέση του Ήλιου και της Σελήνης, τις φάσεις της Σελήνης και τις εκλείψεις", "Τη διαδρομή των πλοίων", "Τις καιρικές συνθήκες"], 1, "μπορούσε κανείς να δει τη θέση του Ήλιου και της Σελήνης, τις φάσεις της Σελήνης και να προβλέψει εκλείψεις"),
  Q("Τι αποκάλυψε η αξονική τομογραφία;", ["Το όνομα του κατασκευαστή", "Κρυμμένες επιγραφές και τον τετραετή κύκλο των αθλητικών αγώνων", "Ότι ο Μηχανισμός ήταν ρολόι", "Ότι κατασκευάστηκε στη Ρώμη"], 1, "διαβάστηκαν χιλιάδες γράμματα από τις επιγραφές … και αποκαλύφθηκε ότι ο Μηχανισμός έδειχνε ακόμη και τον τετραετή κύκλο των αθλητικών αγώνων"),
  Q("Γιατί, κατά την ομιλήτρια, ο Μηχανισμός είναι τόσο σημαντικός;", ["Γιατί είναι φτιαγμένος από χρυσό", "Γιατί μας υποχρεώνει να αναθεωρήσουμε την εικόνα μας για την αρχαία τεχνολογία", "Γιατί λύνει όλα τα ερωτήματα για την αρχαία αστρονομία", "Γιατί είναι το παλαιότερο ναυάγιο"], 1, "ο Μηχανισμός μάς υποχρεώνει να αναθεωρήσουμε την εικόνα που είχαμε για την τεχνολογία του αρχαίου κόσμου"),
 ],
 "gloss": {"σφουγγαράδες": "σφουγγαράς — sponge diver", "βυθό": "βυθός — seabed", "ναυάγιο": "ναυάγιο — shipwreck", "ανέσυραν": "ανασύρω — to bring up, retrieve", "διαβρωμένα": "διαβρωμένος — corroded", "οδοντωτούς τροχούς": "οδοντωτός τροχός — toothed wheel, gear", "ακρίβεια": "ακρίβεια — precision", "χρονολογείται": "χρονολογούμαι — to date (from)", "λαβή": "λαβή — handle", "εκλείψεις": "έκλειψη — eclipse", "αξονική τομογραφία": "αξονική τομογραφία — CT scan", "εγχειριδίου": "εγχειρίδιο — manual, handbook", "να αναθεωρήσουμε": "αναθεωρώ — to revise"},
})

ITEMS.append({
 "id": "l31-int-sygxorisi", "title": "Η δύναμη της συγχώρεσης", "title_en": "The power of forgiveness", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια ραδιοφωνική συνέντευξη με μια ψυχολόγο για τη συγχώρεση.",
 "script": [
  L("Δημοσιογράφος", "m", "Συχνά λέμε «συγχωρώ, αλλά δεν ξεχνώ». Τι σημαίνει, τελικά, να συγχωρείς;", "We often say 'I forgive but I don't forget'. What does it actually mean to forgive?"),
  L("Ψυχολόγος", "f", "Η φράση αυτή είναι πιο σοφή απ' ό,τι νομίζουμε. Η συγχώρεση δεν σημαίνει λήθη, ούτε δικαιολόγηση της πράξης που μας πλήγωσε. Δεν σημαίνει καν απαραίτητα συμφιλίωση. Είναι μια εσωτερική διαδικασία, κατά την οποία αποφασίζουμε να απελευθερωθούμε από τον θυμό και την επιθυμία για εκδίκηση. Με άλλα λόγια, συγχωρούμε πρώτα για τον εαυτό μας.", "That phrase is wiser than we think. Forgiveness doesn't mean forgetting, nor excusing the act that hurt us. It doesn't even necessarily mean reconciliation. It's an internal process in which we decide to free ourselves from anger and the desire for revenge. In other words, we forgive first of all for ourselves."),
  L("Δημοσιογράφος", "m", "Υπάρχουν μετρήσιμα οφέλη;", "Are there measurable benefits?"),
  L("Ψυχολόγος", "f", "Αρκετές μελέτες συνδέουν την ικανότητα συγχώρεσης με λιγότερο άγχος, καλύτερο ύπνο και χαμηλότερη αρτηριακή πίεση. Αντίθετα, η χρόνια μνησικακία λειτουργεί σαν ένα διαρκές στρες: ξαναζούμε συνεχώς την προσβολή, και το σώμα αντιδρά κάθε φορά σαν να συμβαίνει τώρα. Πρέπει όμως να είμαστε προσεκτικοί: οι περισσότερες έρευνες δείχνουν συσχέτιση και όχι απαραίτητα αιτιότητα.", "Several studies link the capacity to forgive with less anxiety, better sleep and lower blood pressure. Conversely, chronic resentment works like constant stress: we relive the offence again and again, and the body reacts each time as if it were happening now. But we have to be careful: most studies show correlation and not necessarily causation."),
  L("Ψυχολόγος", "f", "Και κάτι ακόμη: η συγχώρεση δεν μπορεί να επιβληθεί. Όταν πιέζουμε κάποιον να συγχωρήσει πριν είναι έτοιμος, ιδίως μετά από σοβαρή κακοποίηση, μπορεί να του κάνουμε περισσότερο κακό. Η συγχώρεση έρχεται, αν έρθει, στον δικό της χρόνο.", "And one more thing: forgiveness cannot be imposed. When we pressure someone to forgive before they're ready, especially after serious abuse, we may do them more harm. Forgiveness comes, if it comes, in its own time."),
 ],
 "questions": [
  Q("Τι σημαίνει, κατά την ψυχολόγο, η συγχώρεση;", ["Να ξεχάσουμε ό,τι έγινε", "Μια εσωτερική απελευθέρωση από τον θυμό και την επιθυμία για εκδίκηση", "Να δικαιολογήσουμε την πράξη", "Να συμφιλιωθούμε οπωσδήποτε"], 1, "αποφασίζουμε να απελευθερωθούμε από τον θυμό και την επιθυμία για εκδίκηση"),
  Q("Πώς λειτουργεί η χρόνια μνησικακία;", ["Σαν προστασία από νέες προσβολές", "Σαν ένα διαρκές στρες", "Σαν κίνητρο για επιτυχία", "Δεν έχει επιπτώσεις"], 1, "η χρόνια μνησικακία λειτουργεί σαν ένα διαρκές στρες"),
  Q("Γιατί η ψυχολόγος ζητά προσοχή με τις έρευνες;", ["Γιατί είναι λίγες", "Γιατί δείχνουν συσχέτιση και όχι απαραίτητα αιτιότητα", "Γιατί έγιναν μόνο σε ζώα", "Γιατί είναι παλιές"], 1, "οι περισσότερες έρευνες δείχνουν συσχέτιση και όχι απαραίτητα αιτιότητα"),
  Q("Τι μπορεί να συμβεί αν πιέσουμε κάποιον να συγχωρήσει;", ["Θα συγχωρήσει πιο γρήγορα", "Μπορεί να του κάνουμε περισσότερο κακό", "Θα ξεχάσει την προσβολή", "Θα βελτιωθεί η υγεία του"], 1, "μπορεί να του κάνουμε περισσότερο κακό"),
 ],
 "gloss": {"συγχώρεση": "συγχώρεση — forgiveness", "λήθη": "λήθη — oblivion, forgetting", "δικαιολόγηση": "δικαιολόγηση — justification, excusing", "πλήγωσε": "πληγώνω — to hurt", "συμφιλίωση": "συμφιλίωση — reconciliation", "εκδίκηση": "εκδίκηση — revenge", "αρτηριακή πίεση": "αρτηριακή πίεση — blood pressure", "μνησικακία": "μνησικακία — resentment, grudge", "προσβολή": "προσβολή — offence, insult", "συσχέτιση": "συσχέτιση — correlation", "αιτιότητα": "αιτιότητα — causation", "να επιβληθεί": "επιβάλλομαι — to be imposed", "κακοποίηση": "κακοποίηση — abuse"},
})
rnd = random.Random(31)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-31.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
