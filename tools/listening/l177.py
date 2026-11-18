# Source for library/listening/listening-177.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l177.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l177-ann-ydatino-parko", "title": "Ανακοίνωση σε ένα υδάτινο πάρκο", "title_en": "An announcement at a water park", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός υδάτινου πάρκου, ένα ζεστό απόγευμα του Ιουλίου.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί επισκέπτες, σας ενημερώνουμε ότι η μεγάλη νεροτσουλήθρα «Κύκλωπας» θα μείνει κλειστή για μισή ώρα λόγω τεχνικού ελέγχου. Στο μεταξύ, μπορείτε να χρησιμοποιήσετε την πισίνα με τα κύματα, που λειτουργεί κανονικά.", "Dear visitors, please note that the big water slide 'Cyclops' will remain closed for half an hour for a technical check. In the meantime, you can use the wave pool, which is operating normally."),
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε ότι στις μεγάλες νεροτσουλήθρες επιτρέπεται η είσοδος μόνο σε παιδιά με ύψος πάνω από ένα μέτρο και είκοσι. Για τους μικρότερους υπάρχει η παιδική πισίνα, δίπλα στο κυλικείο, όπου επιβλέπουν συνεχώς δύο ναυαγοσώστες.", "We remind you that on the big water slides entry is allowed only for children taller than one metre twenty. For the little ones there is the children's pool, next to the snack bar, where two lifeguards are on watch at all times."),
  L("Εκφωνήτρια", "f", "Ο ήλιος σήμερα είναι πολύ δυνατός. Βάζετε αντηλιακό κάθε δύο ώρες και πίνετε άφθονο νερό· στις βρύσες δίπλα στις τουαλέτες το νερό είναι πόσιμο και δωρεάν. Σας ευχόμαστε καλή διασκέδαση!", "The sun is very strong today. Put on sunscreen every two hours and drink plenty of water; at the taps next to the toilets the water is drinkable and free. We wish you a good time!"),
 ],
 "questions": [
  Q("Γιατί είναι κλειστή η νεροτσουλήθρα «Κύκλωπας»;", ["Γιατί έχει πολύ κόσμο", "Λόγω τεχνικού ελέγχου", "Γιατί χάλασε οριστικά", "Λόγω του αέρα"], 1, "θα μείνει κλειστή για μισή ώρα λόγω τεχνικού ελέγχου"),
  Q("Ποιοι μπορούν να μπουν στις μεγάλες νεροτσουλήθρες;", ["Όλοι οι επισκέπτες", "Μόνο οι ενήλικες", "Παιδιά με ύψος πάνω από ένα μέτρο και είκοσι", "Παιδιά κάτω των δώδεκα"], 2, "μόνο σε παιδιά με ύψος πάνω από ένα μέτρο και είκοσι"),
  Q("Πού μπορούν οι επισκέπτες να βρουν δωρεάν πόσιμο νερό;", ["Στις βρύσες δίπλα στις τουαλέτες", "Στο κυλικείο", "Στην είσοδο του πάρκου", "Στην παιδική πισίνα"], 0, "στις βρύσες δίπλα στις τουαλέτες το νερό είναι πόσιμο και δωρεάν"),
 ],
 "gloss": {"μεγάφωνα": "μεγάφωνο — loudspeaker", "υδάτινου πάρκου": "υδάτινο πάρκο — water park", "νεροτσουλήθρα": "νεροτσουλήθρα — water slide", "τεχνικού ελέγχου": "τεχνικός έλεγχος — technical check", "πισίνα με τα κύματα": "πισίνα με κύματα — wave pool", "κυλικείο": "κυλικείο — snack bar", "επιβλέπουν": "επιβλέπω — to supervise", "ναυαγοσώστες": "ναυαγοσώστης — lifeguard", "αντηλιακό": "αντηλιακό — sunscreen", "πόσιμο": "πόσιμος — drinkable"},
})

ITEMS.append({
 "id": "l177-int-xylina-paichnidia", "title": "Ο κατασκευαστής ξύλινων παιχνιδιών", "title_en": "The wooden toy maker", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν άντρα που φτιάχνει ξύλινα παιχνίδια σε ένα εργαστήριο στα Τρίκαλα.",
 "script": [
  L("Δημοσιογράφος", "f", "Σε μια εποχή με τάμπλετ και βιντεοπαιχνίδια, ποιος αγοράζει ξύλινα παιχνίδια;", "In an age of tablets and video games, who buys wooden toys?"),
  L("Τεχνίτης", "m", "Περισσότεροι απ' όσους φαντάζεστε. Συνήθως γονείς που θέλουν τα παιδιά τους να παίζουν με κάτι που δεν έχει οθόνη ούτε μπαταρίες. Και παππούδες, που θυμούνται τα δικά τους παιχνίδια. Το πιο δημοφιλές μου είναι ένα τρενάκι με βαγόνια που ενώνονται με μαγνήτες.", "More than you'd imagine. Usually parents who want their children to play with something that has no screen or batteries. And grandparents, who remember their own toys. My most popular one is a little train with carriages that join together with magnets."),
  L("Δημοσιογράφος", "f", "Τι ξύλο χρησιμοποιείτε;", "What wood do you use?"),
  L("Τεχνίτης", "m", "Κυρίως οξιά από τα δάση της Πίνδου, γιατί είναι σκληρή και δεν βγάζει σκλήθρες. Δεν βάφω ποτέ με χρώματα που περιέχουν τοξικές ουσίες, γιατί ξέρω ότι κάθε παιχνίδι κάποια στιγμή θα μπει σε ένα στόμα. Τα περισσότερα τα αφήνω στο φυσικό τους χρώμα, απλώς με λίγο λάδι.", "Mainly beech from the forests of the Pindus, because it's hard and doesn't splinter. I never paint with colours that contain toxic substances, because I know every toy will at some point end up in a mouth. Most of them I leave in their natural colour, just with a little oil."),
  L("Δημοσιογράφος", "f", "Ποιο παιχνίδι σάς έχει μείνει αξέχαστο;", "Which toy has stayed with you unforgettably?"),
  L("Τεχνίτης", "m", "Ένας κύριος μού έφερε ένα σπασμένο ξύλινο άλογο που του είχε φτιάξει ο πατέρας του το 1960. Ήθελε να το χαρίσει στον εγγονό του. Το επισκεύασα χωρίς να αλλάξω τίποτα από το παλιό, ούτε καν τα σημάδια από τα δόντια του.", "A gentleman brought me a broken wooden horse that his father had made for him in 1960. He wanted to give it to his grandson. I repaired it without changing anything of the old one, not even the tooth marks."),
 ],
 "questions": [
  Q("Ποιο είναι το πιο δημοφιλές του παιχνίδι;", ["Ένα ξύλινο άλογο", "Ένα τρενάκι με βαγόνια που ενώνονται με μαγνήτες", "Ένα παζλ", "Ένα κουκλόσπιτο"], 1, "ένα τρενάκι με βαγόνια που ενώνονται με μαγνήτες"),
  Q("Γιατί δεν βάφει με τοξικά χρώματα;", ["Γιατί είναι ακριβά", "Γιατί δεν αρέσουν στους πελάτες", "Γιατί κάθε παιχνίδι κάποια στιγμή θα μπει σε ένα στόμα", "Γιατί το απαγορεύει ο νόμος"], 2, "κάθε παιχνίδι κάποια στιγμή θα μπει σε ένα στόμα"),
  Q("Τι έκανε με το παλιό ξύλινο άλογο;", ["Το επισκεύασε χωρίς να αλλάξει τίποτα από το παλιό", "Το έβαψε από την αρχή", "Έφτιαξε ένα καινούργιο ίδιο", "Το κράτησε για τη συλλογή του"], 0, "Το επισκεύασα χωρίς να αλλάξω τίποτα από το παλιό"),
 ],
 "gloss": {"εργαστήριο": "εργαστήριο — workshop", "βιντεοπαιχνίδια": "βιντεοπαιχνίδι — video game", "δημοφιλές": "δημοφιλής — popular", "βαγόνια": "βαγόνι — carriage, wagon", "μαγνήτες": "μαγνήτης — magnet", "οξιά": "οξιά — beech", "σκλήθρες": "σκλήθρα — splinter", "τοξικές ουσίες": "τοξική ουσία — toxic substance", "αξέχαστο": "αξέχαστος — unforgettable", "επισκεύασα": "επισκευάζω — to repair"},
})

ITEMS.append({
 "id": "l177-int-glossologos-arvanitika", "title": "Η γλωσσολόγος που ηχογραφεί τα αρβανίτικα", "title_en": "The linguist recording Arvanitika", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια γλωσσολόγο που ηχογραφεί ηλικιωμένους ομιλητές των αρβανίτικων στην Αττική και στη Βοιωτία.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς είναι τα αρβανίτικα;", "What exactly is Arvanitika?"),
  L("Γλωσσολόγος", "f", "Είναι μια γλώσσα συγγενική με τα αλβανικά, που την έφεραν πληθυσμοί οι οποίοι εγκαταστάθηκαν στη νότια Ελλάδα κυρίως από τον δέκατο τέταρτο αιώνα και μετά. Για αιώνες μιλιόταν σε εκατοντάδες χωριά της Αττικής, της Βοιωτίας και της Πελοποννήσου, αλλά σχεδόν ποτέ δεν γράφτηκε. Ζούσε μόνο στο στόμα των ανθρώπων.", "It's a language related to Albanian, brought by populations who settled in southern Greece mainly from the fourteenth century onwards. For centuries it was spoken in hundreds of villages in Attica, Boeotia and the Peloponnese, but it was almost never written down. It lived only in people's mouths."),
  L("Δημοσιογράφος", "m", "Πόσοι τη μιλούν σήμερα;", "How many speak it today?"),
  L("Γλωσσολόγος", "f", "Δεν υπάρχουν ακριβείς αριθμοί. Αυτό που ξέρουμε είναι ότι οι περισσότεροι ομιλητές είναι πάνω από εβδομήντα. Πολλοί γονείς τη δεκαετία του πενήντα και του εξήντα σταμάτησαν να τη μιλούν στα παιδιά τους, γιατί πίστευαν ότι θα τα εμπόδιζε στο σχολείο. Έτσι, οι εγγονοί καταλαβαίνουν λίγες λέξεις, αλλά δεν μπορούν να κάνουν μια συζήτηση.", "There are no exact numbers. What we know is that most speakers are over seventy. Many parents in the fifties and sixties stopped speaking it to their children, because they believed it would hold them back at school. So the grandchildren understand a few words, but can't hold a conversation."),
  L("Δημοσιογράφος", "m", "Πώς γίνονται οι ηχογραφήσεις;", "How are the recordings made?"),
  L("Γλωσσολόγος", "f", "Δεν ζητάω ποτέ από κάποιον να μου «μιλήσει αρβανίτικα». Του ζητάω να μου πει πώς έφτιαχναν το ψωμί ή πώς γινόταν ένας γάμος. Όταν θυμάται, η γλώσσα έρχεται μόνη της. Μια γιαγιά στη Βοιωτία μου τραγούδησε ένα νανούρισμα που δεν είχε πει εδώ και εξήντα χρόνια· στο τέλος έκλαιγε κι εκείνη κι εγώ.", "I never ask someone to 'speak Arvanitika to me'. I ask them to tell me how they used to make bread or how a wedding took place. When they remember, the language comes by itself. A grandmother in Boeotia sang me a lullaby she hadn't sung for sixty years; at the end both she and I were crying."),
 ],
 "questions": [
  Q("Γιατί τα αρβανίτικα δεν άφησαν σχεδόν καθόλου γραπτά κείμενα;", ["Γιατί απαγορεύονταν", "Γιατί σχεδόν ποτέ δεν γράφτηκαν· ζούσαν μόνο στον προφορικό λόγο", "Γιατί χάθηκαν σε μια φωτιά", "Γιατί τα έγραφαν σε ξύλο"], 1, "σχεδόν ποτέ δεν γράφτηκε"),
  Q("Γιατί πολλοί γονείς σταμάτησαν να τα μιλούν στα παιδιά τους;", ["Γιατί τα είχαν ξεχάσει", "Γιατί μετακόμισαν στο εξωτερικό", "Γιατί πίστευαν ότι θα τα εμπόδιζαν στο σχολείο", "Γιατί τα παιδιά δεν ήθελαν"], 2, "πίστευαν ότι θα τα εμπόδιζε στο σχολείο"),
  Q("Πώς πετυχαίνει η γλωσσολόγος να μιλήσουν οι ηλικιωμένοι;", ["Τους ζητάει να διηγηθούν πώς γίνονταν τα πράγματα παλιά", "Τους πληρώνει", "Τους δίνει να διαβάσουν ένα κείμενο", "Τους ζητάει να μεταφράσουν λέξεις"], 0, "Του ζητάω να μου πει πώς έφτιαχναν το ψωμί ή πώς γινόταν ένας γάμος"),
 ],
 "gloss": {"γλωσσολόγο": "γλωσσολόγος — linguist", "ηχογραφεί": "ηχογραφώ — to record (sound)", "αρβανίτικων": "αρβανίτικα — Arvanitika", "συγγενική": "συγγενικός — related", "εγκαταστάθηκαν": "εγκαθίσταμαι — to settle", "ακριβείς": "ακριβής — exact", "εμπόδιζε": "εμποδίζω — to hinder, hold back", "ηχογραφήσεις": "ηχογράφηση — recording", "νανούρισμα": "νανούρισμα — lullaby"},
})

ITEMS.append({
 "id": "l177-dia-pame-sto-irodeio", "title": "Πάμε στο Ηρώδειο;", "title_en": "Shall we go to the Odeon of Herodes Atticus?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλες να συζητούν αν θα αγοράσουν εισιτήρια για μια παράσταση στο Ηρώδειο.",
 "script": [
  L("Αλίκη", "f", "Βγήκαν τα εισιτήρια για την «Ιφιγένεια» στο Ηρώδειο, τον Ιούλιο. Λέω να πάρουμε δύο, πριν εξαντληθούν.", "Tickets are out for 'Iphigenia' at the Odeon of Herodes Atticus, in July. I'm thinking we should get two, before they sell out."),
  L("Νεφέλη", "f", "Τα είδα. Οι καλές θέσεις είναι εβδομήντα ευρώ! Τόσα λεφτά για να κάθομαι τρεις ώρες σε μάρμαρο;", "I saw them. The good seats are seventy euros! That much money to sit for three hours on marble?"),
  L("Αλίκη", "f", "Υπάρχουν και φθηνότερες, στα πάνω διαζώματα, γύρω στα είκοσι. Από εκεί δεν βλέπεις τόσο καλά τα πρόσωπα, αλλά βλέπεις όλη την Ακρόπολη φωτισμένη από πάνω σου. Για μένα, αυτό είναι η μισή παράσταση.", "There are cheaper ones too, in the upper tiers, around twenty. From there you can't see the faces so well, but you can see the whole Acropolis lit up above you. For me, that's half the performance."),
  L("Νεφέλη", "f", "Καλά, αλλά τι γίνεται με το μάρμαρο; Την τελευταία φορά πόνεσε η πλάτη μου για δύο μέρες.", "Fine, but what about the marble? Last time my back hurt for two days."),
  L("Αλίκη", "f", "Θα πάρουμε μαξιλαράκια από το σπίτι. Και ζακέτα, γιατί αργά το βράδυ φυσάει, ακόμα και τον Ιούλιο.", "We'll take little cushions from home. And a cardigan, because late at night it gets windy, even in July."),
  L("Νεφέλη", "f", "Εντάξει, με έπεισες. Πάρε δύο στα πάνω διαζώματα, και το φαγητό μετά το κερνάω εγώ.", "OK, you've convinced me. Get two in the upper tiers, and dinner afterwards is on me."),
 ],
 "questions": [
  Q("Γιατί διστάζει στην αρχή η Νεφέλη;", ["Γιατί δεν της αρέσει το έργο", "Γιατί οι καλές θέσεις είναι ακριβές", "Γιατί δουλεύει τον Ιούλιο", "Γιατί έχει δει ήδη την παράσταση"], 1, "Οι καλές θέσεις είναι εβδομήντα ευρώ!"),
  Q("Ποιο είναι, κατά την Αλίκη, το πλεονέκτημα των πάνω διαζωμάτων;", ["Ακούς καλύτερα", "Έχουν μαξιλάρια", "Βλέπεις όλη την Ακρόπολη φωτισμένη", "Είναι πιο κοντά στην έξοδο"], 2, "βλέπεις όλη την Ακρόπολη φωτισμένη από πάνω σου"),
  Q("Τι θα πάρουν μαζί τους;", ["Μαξιλαράκια και ζακέτα", "Φαγητό και νερό", "Κιάλια", "Ομπρέλα"], 0, "Θα πάρουμε μαξιλαράκια από το σπίτι. Και ζακέτα"),
 ],
 "gloss": {"Ηρώδειο": "Ηρώδειο — the Odeon of Herodes Atticus (ancient theatre in Athens)", "εξαντληθούν": "εξαντλούμαι — to sell out, run out", "μάρμαρο": "μάρμαρο — marble", "διαζώματα": "διάζωμα — tier (of an ancient theatre)", "φωτισμένη": "φωτισμένος — lit up", "μαξιλαράκια": "μαξιλαράκι — small cushion", "ζακέτα": "ζακέτα — cardigan", "με έπεισες": "πείθω — to convince", "κερνάω": "κερνάω — to treat (someone)"},
})

ITEMS.append({
 "id": "l177-dia-katering-i-mageirevoume", "title": "Κέτερινγκ ή μαγειρεύουμε μόνοι μας;", "title_en": "Catering or do we cook ourselves?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέλφια να οργανώνουν το γλέντι για τα ογδοηκοστά γενέθλια του πατέρα τους.",
 "script": [
  L("Πέτρος", "m", "Θα είμαστε σαράντα άτομα. Βρήκα μια εταιρεία κέτερινγκ που φέρνει τα πάντα: φαγητό, πιάτα, ποτήρια, και δύο σερβιτόρους. Δεκαπέντε ευρώ το άτομο.", "There'll be forty of us. I've found a catering company that brings everything: food, plates, glasses and two waiters. Fifteen euros a head."),
  L("Δέσποινα", "f", "Εξακόσια ευρώ για φαγητό που ο μπαμπάς δεν θα το φάει. Ξέρεις ότι τρώει μόνο το παστίτσιο της θείας Ρένας.", "Six hundred euros for food that Dad won't eat. You know he only eats Aunt Rena's pastitsio."),
  L("Πέτρος", "m", "Δεν μπορούμε να ζητήσουμε από τη θεία Ρένα να μαγειρέψει για σαράντα άτομα. Είναι ογδόντα πέντε χρονών!", "We can't ask Aunt Rena to cook for forty people. She's eighty-five!"),
  L("Δέσποινα", "f", "Όχι για σαράντα. Σκέψου το αλλιώς: το κέτερινγκ φέρνει τα ορεκτικά και τα ποτά, και η θεία φτιάχνει ένα ταψί παστίτσιο, με τη βοήθειά μου. Θα της αρέσει να νιώθει χρήσιμη.", "Not for forty. Think of it differently: the caterer brings the starters and the drinks, and our aunt makes one tray of pastitsio, with my help. She'll like feeling useful."),
  L("Πέτρος", "m", "Και το γλυκό; Η εταιρεία έχει και τούρτες.", "And dessert? The company has cakes too."),
  L("Δέσποινα", "f", "Τούρτα θα φέρει ο ζαχαροπλάστης της γειτονιάς, που τον ξέρει ο μπαμπάς πενήντα χρόνια. Ρώτα το κέτερινγκ πόσο κοστίζουν μόνο τα ορεκτικά και τα ποτά.", "The neighbourhood pastry cook will bring the cake; Dad has known him for fifty years. Ask the caterer how much just the starters and drinks cost."),
 ],
 "questions": [
  Q("Τι προσφέρει η εταιρεία κέτερινγκ που βρήκε ο Πέτρος;", ["Μόνο τα ποτά", "Φαγητό, πιάτα, ποτήρια και δύο σερβιτόρους", "Μόνο την τούρτα", "Μουσική και φαγητό"], 1, "φαγητό, πιάτα, ποτήρια, και δύο σερβιτόρους"),
  Q("Τι προτείνει η Δέσποινα για το παστίτσιο;", ["Να το παραγγείλουν από την εταιρεία", "Να μην υπάρχει παστίτσιο", "Να φτιάξει η θεία Ρένα ένα ταψί, με τη βοήθειά της", "Να το φτιάξει ο Πέτρος"], 2, "η θεία φτιάχνει ένα ταψί παστίτσιο, με τη βοήθειά μου"),
  Q("Ποιος θα φέρει την τούρτα;", ["Ο ζαχαροπλάστης της γειτονιάς", "Η εταιρεία κέτερινγκ", "Η θεία Ρένα", "Η Δέσποινα"], 0, "Τούρτα θα φέρει ο ζαχαροπλάστης της γειτονιάς"),
 ],
 "gloss": {"γλέντι": "γλέντι — party, celebration", "ογδοηκοστά": "ογδοηκοστός — eightieth", "κέτερινγκ": "κέτερινγκ — catering", "παστίτσιο": "παστίτσιο — pastitsio (baked pasta with mince and béchamel)", "ορεκτικά": "ορεκτικό — starter", "ταψί": "ταψί — baking tray", "χρήσιμη": "χρήσιμος — useful", "τούρτες": "τούρτα — cake, gateau", "ζαχαροπλάστης": "ζαχαροπλάστης — pastry cook"},
})

ITEMS.append({
 "id": "l177-mon-deka-chronia-sto-tokio", "title": "Δέκα χρόνια στο Τόκιο", "title_en": "Ten years in Tokyo", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα που γύρισε στην Αθήνα μετά από δέκα χρόνια δουλειάς στο Τόκιο.",
 "script": [
  L("Φίλιππος", "m", "Πήγα στο Τόκιο για δύο χρόνια, με μια θέση σε ένα πανεπιστήμιο, και έμεινα δέκα. Τους πρώτους μήνες ένιωθα σαν να είχα προσγειωθεί σε άλλον πλανήτη. Δεν καταλάβαινα ούτε τις ταμπέλες ούτε τις σιωπές των ανθρώπων.", "I went to Tokyo for two years, with a post at a university, and stayed ten. In the first months I felt as if I had landed on another planet. I understood neither the signs nor people's silences."),
  L("Φίλιππος", "m", "Με τον καιρό έμαθα να εκτιμώ πράγματα που στην αρχή μου φαίνονταν υπερβολικά. Στα τρένα δεν μιλάει κανείς στο τηλέφωνο. Αν το τρένο αργήσει ένα λεπτό, ο οδηγός ζητάει συγγνώμη από τα μεγάφωνα. Αν ξεχάσεις το πορτοφόλι σου σε ένα καφέ, το βρίσκεις την επόμενη μέρα στο ίδιο τραπέζι.", "Over time I learned to appreciate things that at first seemed excessive to me. On the trains nobody talks on the phone. If the train is a minute late, the driver apologises over the loudspeakers. If you forget your wallet in a café, you find it the next day on the same table."),
  L("Φίλιππος", "m", "Το δύσκολο ήταν η επιστροφή. Τις πρώτες εβδομάδες στην Αθήνα όλα μου φαίνονταν θορυβώδη: οι κόρνες, οι φωνές στα καφενεία, οι γείτονες που συζητούν από μπαλκόνι σε μπαλκόνι. Έπιανα τον εαυτό μου να βγάζει τα παπούτσια στην πόρτα των φίλων μου και να υποκλίνεται στον περιπτερά.", "The hard part was coming back. In the first weeks in Athens everything seemed noisy to me: the horns, the voices in the cafés, the neighbours chatting from balcony to balcony. I caught myself taking off my shoes at my friends' doors and bowing to the kiosk owner."),
  L("Φίλιππος", "m", "Τώρα έχω βρει μια ισορροπία. Κρατάω από την Ιαπωνία την ησυχία του πρωινού και τη συνέπεια στα ραντεβού. Και από την Ελλάδα, την αγκαλιά που σου δίνει ένας άγνωστος όταν μαθαίνει ότι γύρισες σπίτι.", "Now I've found a balance. From Japan I keep the quiet of the morning and punctuality at appointments. And from Greece, the hug a stranger gives you when they learn you've come home."),
 ],
 "questions": [
  Q("Για πόσο καιρό είχε σκοπό αρχικά να μείνει στο Τόκιο;", ["Για δέκα χρόνια", "Για δύο χρόνια", "Για έξι μήνες", "Για πάντα"], 1, "Πήγα στο Τόκιο για δύο χρόνια"),
  Q("Τι συμβαίνει, σύμφωνα με τον Φίλιππο, αν το τρένο αργήσει ένα λεπτό;", ["Οι επιβάτες διαμαρτύρονται", "Το εισιτήριο επιστρέφεται", "Ο οδηγός ζητάει συγγνώμη από τα μεγάφωνα", "Κανείς δεν το προσέχει"], 2, "ο οδηγός ζητάει συγγνώμη από τα μεγάφωνα"),
  Q("Τι κρατάει από την Ιαπωνία;", ["Την ησυχία του πρωινού και τη συνέπεια στα ραντεβού", "Την ιαπωνική κουζίνα", "Τη συνήθεια να δουλεύει πολλές ώρες", "Τα ιαπωνικά βιβλία του"], 0, "Κρατάω από την Ιαπωνία την ησυχία του πρωινού και τη συνέπεια στα ραντεβού"),
 ],
 "gloss": {"προσγειωθεί": "προσγειώνομαι — to land", "ταμπέλες": "ταμπέλα — sign", "σιωπές": "σιωπή — silence", "εκτιμώ": "εκτιμώ — to appreciate", "υπερβολικά": "υπερβολικός — excessive", "θορυβώδη": "θορυβώδης — noisy", "κόρνες": "κόρνα — (car) horn", "υποκλίνεται": "υποκλίνομαι — to bow", "περιπτερά": "περιπτεράς — kiosk owner", "συνέπεια": "συνέπεια — punctuality, consistency"},
})

ITEMS.append({
 "id": "l177-vm-aftokinoumeno", "title": "Μήνυμα από τον πωλητή ενός αυτοκινούμενου", "title_en": "A message from the seller of a camper van", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον ιδιοκτήτη ενός μεταχειρισμένου αυτοκινούμενου, για το οποίο ενδιαφερθήκατε μέσω μιας αγγελίας.",
 "script": [
  L("Πωλητής", "m", "Καλησπέρα, κυρία Μαυρίδου, ο Διονύσης είμαι, για το αυτοκινούμενο της αγγελίας. Σας ευχαριστώ για το ενδιαφέρον. Ναι, είναι ακόμα διαθέσιμο. Είναι του 2012, έχει διακόσιες χιλιάδες χιλιόμετρα και κοιμίζει τέσσερα άτομα.", "Good evening, Mrs Mavridou, it's Dionysis, about the camper van in the ad. Thank you for your interest. Yes, it is still available. It's a 2012 model, has two hundred thousand kilometres and sleeps four people."),
  L("Πωλητής", "m", "Να σας πω από τώρα τι θέλει: το ψυγείο δουλεύει μόνο με ρεύμα, όχι με γκάζι, και η τέντα έχει ένα μικρό σκίσιμο. Κατά τα άλλα, η μηχανή είναι σε άριστη κατάσταση, με όλα τα σέρβις στην αντιπροσωπεία· έχω όλα τα χαρτιά.", "Let me tell you right away what it needs: the fridge only works on mains power, not on gas, and the awning has a small tear. Otherwise, the engine is in excellent condition, with all services at the dealership; I have all the paperwork."),
  L("Πωλητής", "m", "Μπορείτε να έρθετε να το δείτε το Σάββατο το πρωί στο Μαρκόπουλο. Αν θέλετε, φέρτε και έναν μηχανικό της εμπιστοσύνης σας. Για την τιμή, συζητάμε, αλλά όχι στο τηλέφωνο. Το κινητό μου είναι 6944 318 207.", "You can come and see it on Saturday morning in Markopoulo. If you want, bring a mechanic you trust as well. As for the price, we can discuss it, but not on the phone. My mobile is 6944 318 207."),
 ],
 "questions": [
  Q("Πόσα άτομα κοιμίζει το αυτοκινούμενο;", ["Δύο", "Τέσσερα", "Έξι", "Οκτώ"], 1, "κοιμίζει τέσσερα άτομα"),
  Q("Ποιο πρόβλημα αναφέρει ο πωλητής;", ["Η μηχανή χρειάζεται επισκευή", "Δεν έχει χαρτιά", "Το ψυγείο δουλεύει μόνο με ρεύμα και η τέντα έχει ένα μικρό σκίσιμο", "Τα λάστιχα είναι φθαρμένα"], 2, "το ψυγείο δουλεύει μόνο με ρεύμα, όχι με γκάζι, και η τέντα έχει ένα μικρό σκίσιμο"),
  Q("Τι προτείνει για την τιμή;", ["Να τη συζητήσουν από κοντά, όχι στο τηλέφωνο", "Είναι σταθερή και δεν αλλάζει", "Να του στείλει προσφορά με email", "Να την ορίσει ο μηχανικός"], 0, "Για την τιμή, συζητάμε, αλλά όχι στο τηλέφωνο"),
 ],
 "gloss": {"αυτοκινούμενου": "αυτοκινούμενο — camper van, motorhome", "αγγελίας": "αγγελία — advert, listing", "διαθέσιμο": "διαθέσιμος — available", "κοιμίζει": "κοιμίζω — to sleep (people), to put to sleep", "γκάζι": "γκάζι — gas (bottled)", "τέντα": "τέντα — awning", "σκίσιμο": "σκίσιμο — tear, rip", "αντιπροσωπεία": "αντιπροσωπεία — dealership", "της εμπιστοσύνης σας": "της εμπιστοσύνης μου — whom I trust"},
})

ITEMS.append({
 "id": "l177-vm-odigos-kanyon", "title": "Μήνυμα από τον οδηγό για την κατάβαση στο φαράγγι", "title_en": "A message from the guide about the canyoning trip", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον οδηγό μιας ομάδας στην οποία κλείσατε θέσεις για μια κατάβαση φαραγγιού, με σκοινιά και κολύμπι, στην Ήπειρο.",
 "script": [
  L("Οδηγός", "m", "Γεια σας, ο Λευτέρης από την ομάδα καταβάσεων. Λάβαμε την κράτησή σας για τρία άτομα για τις δεκαπέντε του μήνα, ευχαριστούμε! Πριν σας στείλω την επιβεβαίωση, χρειάζομαι μερικές πληροφορίες, γιατί είναι θέμα ασφάλειας.", "Hi, it's Lefteris from the canyoning group. We've received your booking for three people for the fifteenth of the month, thank you! Before I send you the confirmation, I need some information, because it's a safety matter."),
  L("Οδηγός", "m", "Πρώτον, όλοι οι συμμετέχοντες πρέπει να ξέρουν να κολυμπούν, τουλάχιστον πενήντα μέτρα χωρίς στάση, γιατί σε δύο σημεία το νερό είναι βαθύ και δεν πατάς. Δεύτερον, γράψατε ότι ο γιος σας είναι δεκατεσσάρων χρονών. Για ανήλικους χρειαζόμαστε υπογεγραμμένη άδεια από έναν γονιό, και πρέπει να έρθει μαζί του ένας ενήλικας της οικογένειας.", "First, all participants must know how to swim, at least fifty metres without stopping, because in two places the water is deep and you can't touch the bottom. Second, you wrote that your son is fourteen. For minors we need signed permission from a parent, and an adult from the family must come with him."),
  L("Οδηγός", "m", "Τέλος, στείλτε μου με μήνυμα το ύψος και το βάρος του καθενός, για να σας ετοιμάσουμε στολές στο σωστό μέγεθος. Κράνος και σκοινιά τα δίνουμε εμείς· εσείς φέρτε μόνο παπούτσια που μπορούν να βραχούν, όχι σαγιονάρες. Ευχαριστώ!", "Finally, send me by text each person's height and weight, so that we can get wetsuits ready for you in the right size. We provide helmets and ropes; you only bring shoes that can get wet, not flip-flops. Thank you!"),
 ],
 "questions": [
  Q("Γιατί πρέπει όλοι να ξέρουν κολύμπι;", ["Γιατί η διαδρομή τελειώνει στη θάλασσα", "Γιατί σε δύο σημεία το νερό είναι βαθύ και δεν πατάς", "Γιατί το ζητάει η ασφαλιστική", "Γιατί θα κάνουν αγώνα κολύμβησης"], 1, "σε δύο σημεία το νερό είναι βαθύ και δεν πατάς"),
  Q("Τι χρειάζεται για τον γιο, επειδή είναι ανήλικος;", ["Πιστοποιητικό υγείας", "Ειδικό εισιτήριο", "Υπογεγραμμένη άδεια από γονιό και συνοδεία ενήλικα της οικογένειας", "Τίποτα ιδιαίτερο"], 2, "χρειαζόμαστε υπογεγραμμένη άδεια από έναν γονιό"),
  Q("Γιατί ζητάει το ύψος και το βάρος των συμμετεχόντων;", ["Για να ετοιμάσει στολές στο σωστό μέγεθος", "Για την ασφάλιση", "Για να υπολογίσει την τιμή", "Για να διαλέξει τη διαδρομή"], 0, "για να σας ετοιμάσουμε στολές στο σωστό μέγεθος"),
 ],
 "gloss": {"κατάβαση φαραγγιού": "κατάβαση φαραγγιού — canyoning", "κράτησή": "κράτηση — booking", "επιβεβαίωση": "επιβεβαίωση — confirmation", "συμμετέχοντες": "συμμετέχων — participant", "δεν πατάς": "δεν πατάω — I can't touch the bottom", "ανήλικους": "ανήλικος — minor", "υπογεγραμμένη": "υπογεγραμμένος — signed", "ενήλικας": "ενήλικας — adult", "στολές": "στολή — wetsuit; uniform", "Κράνος": "κράνος — helmet", "σαγιονάρες": "σαγιονάρα — flip-flop"},
})

ITEMS.append({
 "id": "l177-c1-pos-vlepoun-oi-melisses", "title": "Πώς βλέπουν και πώς «μιλούν» οι μέλισσες", "title_en": "How bees see and how they 'talk'", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια εντομολόγο για την όραση και την επικοινωνία των μελισσών.",
 "script": [
  L("Δημοσιογράφος", "m", "Βλέπουν οι μέλισσες τα λουλούδια όπως εμείς;", "Do bees see flowers the way we do?"),
  L("Εντομολόγος", "f", "Όχι ακριβώς. Οι μέλισσες δεν διακρίνουν το κόκκινο, βλέπουν όμως το υπεριώδες φως, που για εμάς είναι αόρατο. Πολλά λουλούδια που στα μάτια μας φαίνονται μονόχρωμα έχουν στα πέταλά τους υπεριώδη σχέδια, κάτι σαν διαδρόμους προσγείωσης, που οδηγούν το έντομο κατευθείαν στο νέκταρ. Το λουλούδι και η μέλισσα, με άλλα λόγια, έχουν εξελιχθεί μαζί, σαν δύο συνομιλητές που έμαθαν την ίδια γλώσσα.", "Not exactly. Bees can't distinguish red, but they can see ultraviolet light, which is invisible to us. Many flowers that look single-coloured to our eyes have ultraviolet patterns on their petals, something like landing strips, that guide the insect straight to the nectar. The flower and the bee, in other words, have evolved together, like two interlocutors who learned the same language."),
  L("Δημοσιογράφος", "m", "Και μεταξύ τους πώς επικοινωνούν;", "And how do they communicate among themselves?"),
  L("Εντομολόγος", "f", "Με έναν χορό. Όταν μια εργάτρια βρει πλούσια πηγή τροφής, γυρίζει στην κυψέλη και κάνει πάνω στις κερήθρες έναν χορό σε σχήμα οκτώ, κουνώντας την κοιλιά της στο ευθύ τμήμα. Η γωνία αυτού του τμήματος σε σχέση με την κατακόρυφο δείχνει την κατεύθυνση της τροφής σε σχέση με τον ήλιο, και η διάρκεια του κουνήματος δείχνει την απόσταση. Τον κώδικα αυτόν τον αποκρυπτογράφησε ο Αυστριακός Καρλ φον Φρις, που τιμήθηκε γι' αυτό με το Νόμπελ το 1973.", "With a dance. When a worker finds a rich food source, she returns to the hive and performs on the combs a dance in the shape of a figure eight, waggling her abdomen on the straight section. The angle of that section relative to the vertical shows the direction of the food relative to the sun, and the duration of the waggling shows the distance. This code was deciphered by the Austrian Karl von Frisch, who was awarded the Nobel Prize for it in 1973."),
  L("Εντομολόγος", "f", "Το πιο εντυπωσιακό είναι ότι ο ήλιος μετακινείται όσο περνά η μέρα, και οι μέλισσες το λαμβάνουν υπόψη: διορθώνουν τη γωνία του χορού τους ανάλογα με την ώρα. Πρόκειται για έναν συμβολικό κώδικα, σε έναν εγκέφαλο μικρότερο από ένα κεφάλι καρφίτσας.", "The most impressive thing is that the sun moves as the day goes on, and the bees take it into account: they correct the angle of their dance according to the time. It is a symbolic code, in a brain smaller than a pinhead."),
 ],
 "questions": [
  Q("Τι βλέπουν οι μέλισσες που εμείς δεν βλέπουμε;", ["Το κόκκινο χρώμα", "Το υπεριώδες φως", "Το υπέρυθρο φως", "Τα χρώματα τη νύχτα"], 1, "βλέπουν όμως το υπεριώδες φως, που για εμάς είναι αόρατο"),
  Q("Τι δείχνει η γωνία του ευθύ τμήματος του χορού;", ["Την απόσταση της τροφής", "Την ποσότητα της τροφής", "Την κατεύθυνση της τροφής σε σχέση με τον ήλιο", "Το είδος του λουλουδιού"], 2, "δείχνει την κατεύθυνση της τροφής σε σχέση με τον ήλιο"),
  Q("Πώς λαμβάνουν υπόψη οι μέλισσες την κίνηση του ήλιου;", ["Διορθώνουν τη γωνία του χορού ανάλογα με την ώρα", "Χορεύουν μόνο το μεσημέρι", "Σταματούν να χορεύουν το απόγευμα", "Δεν τη λαμβάνουν υπόψη"], 0, "διορθώνουν τη γωνία του χορού τους ανάλογα με την ώρα"),
 ],
 "gloss": {"εντομολόγο": "εντομολόγος — entomologist", "όραση": "όραση — vision, eyesight", "διακρίνουν": "διακρίνω — to distinguish", "υπεριώδες": "υπεριώδης — ultraviolet", "αόρατο": "αόρατος — invisible", "πέταλά": "πέταλο — petal", "εξελιχθεί": "εξελίσσομαι — to evolve", "κερήθρες": "κερήθρα — honeycomb", "κατακόρυφο": "κατακόρυφος — vertical", "αποκρυπτογράφησε": "αποκρυπτογραφώ — to decipher", "λαμβάνουν υπόψη": "λαμβάνω υπόψη — to take into account", "καρφίτσας": "καρφίτσα — pin"},
})

ITEMS.append({
 "id": "l177-c1-giati-kokkinizoume", "title": "Γιατί κοκκινίζουμε όταν ντρεπόμαστε", "title_en": "Why we blush when we're embarrassed", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ψυχολόγο να εξηγεί σε μια ραδιοφωνική εκπομπή γιατί κοκκινίζουμε.",
 "script": [
  L("Ψυχολόγος", "f", "Ο Δαρβίνος έγραψε ότι το κοκκίνισμα είναι η πιο παράξενη και η πιο ανθρώπινη από όλες τις εκφράσεις. Κανένα άλλο ζώο, απ' όσο ξέρουμε, δεν κοκκινίζει από ντροπή. Και, σε αντίθεση με το χαμόγελο, δεν μπορούμε ούτε να το προκαλέσουμε με τη θέλησή μας ούτε να το σταματήσουμε.", "Darwin wrote that blushing is the most peculiar and the most human of all expressions. No other animal, as far as we know, blushes from embarrassment. And, unlike a smile, we can neither cause it at will nor stop it."),
  L("Ψυχολόγος", "f", "Ο μηχανισμός είναι απλός: όταν νιώθουμε ότι τα βλέμματα των άλλων πέφτουν πάνω μας, το νευρικό σύστημα διαστέλλει τα μικρά αιμοφόρα αγγεία του προσώπου, του λαιμού και των αυτιών, και το δέρμα κοκκινίζει. Το ενδιαφέρον είναι το «γιατί». Το να δείχνεις στους άλλους ότι ντρέπεσαι μοιάζει, με την πρώτη ματιά, μειονέκτημα.", "The mechanism is simple: when we feel that other people's eyes are on us, the nervous system dilates the small blood vessels of the face, neck and ears, and the skin goes red. The interesting part is the 'why'. Showing others that you're embarrassed seems, at first sight, a disadvantage."),
  L("Ψυχολόγος", "f", "Μια ερμηνεία είναι ότι το κοκκίνισμα λειτουργεί σαν μια ειλικρινής συγγνώμη χωρίς λόγια. Λέει: «Ξέρω ότι έκανα λάθος και με νοιάζει τι σκέφτεστε». Ακριβώς επειδή δεν μπορούμε να το προσποιηθούμε, οι άλλοι το εμπιστεύονται. Έρευνες έχουν δείξει ότι όταν κάποιος κοκκινίζει μετά από ένα λάθος, οι γύρω του τον κρίνουν πιο επιεικώς και τον θεωρούν πιο αξιόπιστο. Αυτό που μας φαίνεται αδυναμία είναι ίσως ένας από τους πιο έξυπνους τρόπους που βρήκε η φύση για να μας κρατά ενωμένους.", "One interpretation is that blushing works like a sincere apology without words. It says: 'I know I made a mistake and I care what you think.' Precisely because we can't fake it, others trust it. Studies have shown that when someone blushes after a mistake, the people around them judge them more leniently and consider them more trustworthy. What seems to us a weakness is perhaps one of the cleverest ways nature has found to keep us together."),
 ],
 "questions": [
  Q("Σε τι διαφέρει το κοκκίνισμα από το χαμόγελο;", ["Είναι πιο σύντομο", "Δεν μπορούμε ούτε να το προκαλέσουμε ούτε να το σταματήσουμε με τη θέλησή μας", "Το έχουν και τα ζώα", "Εμφανίζεται μόνο στα παιδιά"], 1, "δεν μπορούμε ούτε να το προκαλέσουμε με τη θέλησή μας ούτε να το σταματήσουμε"),
  Q("Τι συμβαίνει στο σώμα όταν κοκκινίζουμε;", ["Η καρδιά σταματά για λίγο", "Ανεβαίνει η θερμοκρασία όλου του σώματος", "Διαστέλλονται τα μικρά αιμοφόρα αγγεία του προσώπου", "Σφίγγονται οι μύες του προσώπου"], 2, "το νευρικό σύστημα διαστέλλει τα μικρά αιμοφόρα αγγεία του προσώπου"),
  Q("Ποια ερμηνεία δίνει η ψυχολόγος για το κοκκίνισμα;", ["Λειτουργεί σαν ειλικρινής συγγνώμη χωρίς λόγια", "Είναι ένα κατάλοιπο χωρίς χρησιμότητα", "Δείχνει θυμό", "Μας προστατεύει από το κρύο"], 0, "το κοκκίνισμα λειτουργεί σαν μια ειλικρινής συγγνώμη χωρίς λόγια"),
 ],
 "gloss": {"κοκκίνισμα": "κοκκίνισμα — blushing", "Δαρβίνος": "Δαρβίνος — Darwin", "παράξενη": "παράξενος — peculiar, strange", "με τη θέλησή μας": "με τη θέλησή μου — at will", "βλέμματα": "βλέμμα — gaze, look", "διαστέλλει": "διαστέλλω — to dilate", "αιμοφόρα αγγεία": "αιμοφόρο αγγείο — blood vessel", "μειονέκτημα": "μειονέκτημα — disadvantage", "προσποιηθούμε": "προσποιούμαι — to fake, pretend", "επιεικώς": "επιεικώς — leniently", "αξιόπιστο": "αξιόπιστος — trustworthy"},
})

rnd = random.Random(177)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-177.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
