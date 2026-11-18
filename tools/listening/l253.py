# Source for library/listening/listening-253.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l253.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l253-news-vivlio-epistrofi-60-chronia", "title": "Βιβλίο επιστράφηκε στη δημοτική βιβλιοθήκη εξήντα χρόνια μετά", "title_en": "A book is returned to the municipal library sixty years late", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο απογευματινό δελτίο ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνήτρια", "f", "Με καθυστέρηση εξήντα ολόκληρων χρόνων επέστρεψε την περασμένη εβδομάδα ένα βιβλίο στη δημοτική βιβλιοθήκη της πόλης μας. Πρόκειται για μια παλιά έκδοση του «Μικρού Πρίγκιπα», που είχε δανειστεί το 1965 ένας μαθητής του γυμνασίου.", "A book came back to our town's municipal library last week a full sixty years late. It is an old edition of 'The Little Prince', which a secondary-school pupil had borrowed in 1965."),
  L("Εκφωνήτρια", "f", "Το βιβλίο έφτασε με το ταχυδρομείο, μέσα σε ένα προσεκτικά τυλιγμένο δέμα, μαζί με ένα χειρόγραφο γράμμα. Ο αποστολέας, σήμερα συνταξιούχος γιατρός που ζει στο εξωτερικό, εξηγεί ότι η οικογένειά του μετακόμισε ξαφνικά εκείνο το καλοκαίρι και το βιβλίο χάθηκε μέσα στα κιβώτια.", "The book arrived by post in a carefully wrapped parcel, together with a handwritten letter. The sender, today a retired doctor living abroad, explains that his family moved suddenly that summer and the book got lost among the boxes."),
  L("Εκφωνήτρια", "f", "«Το βρήκα όταν άδειαζα το σπίτι της μητέρας μου», γράφει. «Ντρέπομαι που άργησα τόσο. Ελπίζω να το διαβάσει ένα παιδί, όπως το διάβασα κι εγώ.» Στο δέμα είχε βάλει και ένα χαρτονόμισμα για το πρόστιμο, όπως έγραφε, «με τόκους».", "'I found it when I was clearing out my mother's house,' he writes. 'I'm ashamed to be so late. I hope a child reads it, as I did.' He had also put a banknote in the parcel for the fine, 'with interest', as he put it."),
  L("Εκφωνήτρια", "f", "Η διευθύντρια της βιβλιοθήκης δήλωσε ότι δεν θα κρατήσει τα χρήματα, αλλά θα αγοράσει με αυτά καινούργια παιδικά βιβλία. Το παλιό αντίτυπο θα εκτεθεί σε μια βιτρίνα της εισόδου μαζί με το γράμμα, για να θυμίζει, όπως είπε, ότι «ένα βιβλίο πάντα βρίσκει τον δρόμο του για το σπίτι».", "The library's director said she will not keep the money but will use it to buy new children's books. The old copy will be displayed in a cabinet at the entrance together with the letter, to remind people, as she put it, that 'a book always finds its way home'."),
 ],
 "questions": [
  Q("Πότε είχε δανειστεί το βιβλίο;", ["Το 1956", "Το 1965", "Πριν από έξι χρόνια", "Την περασμένη εβδομάδα"], 1, "που είχε δανειστεί το 1965 ένας μαθητής του γυμνασίου"),
  Q("Γιατί δεν επιστράφηκε το βιβλίο τότε;", ["Γιατί ο μαθητής το ξέχασε στο σχολείο", "Γιατί η οικογένειά του μετακόμισε ξαφνικά και το βιβλίο χάθηκε στα κιβώτια", "Γιατί η βιβλιοθήκη έκλεισε", "Γιατί το έδωσε σε έναν φίλο"], 1, "η οικογένειά του μετακόμισε ξαφνικά εκείνο το καλοκαίρι και το βιβλίο χάθηκε μέσα στα κιβώτια"),
  Q("Τι έβαλε ο αποστολέας στο δέμα εκτός από το βιβλίο;", ["Μια φωτογραφία του", "Ένα καινούργιο αντίτυπο", "Ένα γράμμα και ένα χαρτονόμισμα για το πρόστιμο", "Μια κάρτα της βιβλιοθήκης"], 2, "μαζί με ένα χειρόγραφο γράμμα"),
  Q("Τι θα κάνει η βιβλιοθήκη με τα χρήματα;", ["Θα τα επιστρέψει", "Θα αγοράσει καινούργια παιδικά βιβλία", "Θα επισκευάσει την είσοδο", "Θα τα δώσει σε ένα σχολείο"], 1, "θα αγοράσει με αυτά καινούργια παιδικά βιβλία"),
 ],
 "gloss": {"καθυστέρηση": "καθυστέρηση — delay", "έκδοση": "έκδοση — edition", "δανειστεί": "δανείζομαι — to borrow", "τυλιγμένο": "τυλιγμένος — wrapped", "χειρόγραφο": "χειρόγραφος — handwritten", "αποστολέας": "αποστολέας — sender", "κιβώτια": "κιβώτιο — box, crate", "χαρτονόμισμα": "χαρτονόμισμα — banknote", "πρόστιμο": "πρόστιμο — fine", "τόκους": "τόκος — interest (on money)", "αντίτυπο": "αντίτυπο — copy (of a book)", "βιτρίνα": "βιτρίνα — display case"}
})

ITEMS.append({
 "id": "l253-vm-ksylourgos-vivliothiki", "title": "Μήνυμα από τον ξυλουργό για τη βιβλιοθήκη του σαλονιού", "title_en": "A message from the carpenter about the living-room bookcase", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε παραγγείλει σε έναν ξυλουργό μια βιβλιοθήκη για τον τοίχο του σαλονιού σας. Ακούτε ένα μήνυμα που σας άφησε στον τηλεφωνητή.",
 "script": [
  L("Γρηγόρης", "m", "Καλησπέρα σας, ο Γρηγόρης είμαι, ο ξυλουργός. Σας παίρνω για τη βιβλιοθήκη. Πήρα τις μετρήσεις που μου στείλατε, αλλά υπάρχει ένα πρόβλημα: ο τοίχος σας δεν είναι ίσιος, έχει μια κλίση σχεδόν δύο εκατοστά από πάνω ως κάτω.", "Good evening, it's Grigoris, the carpenter. I'm calling about the bookcase. I got the measurements you sent me, but there's a problem: your wall isn't straight; it leans almost two centimetres from top to bottom."),
  L("Γρηγόρης", "m", "Δεν είναι κάτι σπάνιο στις παλιές πολυκατοικίες, μην ανησυχείτε. Μπορώ να το διορθώσω με ένα πλαίσιο στο πίσω μέρος, αλλά θα ήθελα πρώτα να έρθω να το δω με τα μάτια μου. Θα μπορούσα την Τετάρτη το πρωί ή την Πέμπτη μετά τις πέντε.", "It's not unusual in old blocks of flats, don't worry. I can correct it with a frame at the back, but I'd like to come and see it with my own eyes first. I could come on Wednesday morning or Thursday after five."),
  L("Γρηγόρης", "m", "Για το ξύλο: η δρυς που διαλέξατε έχει ακριβύνει αρκετά από τον Σεπτέμβριο. Αν θέλετε να μείνουμε στην τιμή που συζητήσαμε, μπορώ να κάνω τον σκελετό από καρυδιά, που μοιάζει πολύ, και να κρατήσουμε τη δρυ μόνο για τα ράφια. Σκεφτείτε το και μου λέτε.", "About the wood: the oak you chose has gone up quite a bit in price since September. If you want to stay within the price we discussed, I can make the frame in walnut, which looks very similar, and keep the oak just for the shelves. Think about it and let me know."),
  L("Γρηγόρης", "m", "Και κάτι τελευταίο: αν σκοπεύετε να βάλετε πολλά βιβλία, όπως μου είπατε, προτείνω τα ράφια να μην είναι πάνω από ογδόντα εκατοστά μακριά, αλλιώς με τον καιρό θα λυγίσουν. Το κινητό μου το έχετε. Καλό βράδυ.", "And one last thing: if you're planning to put a lot of books on it, as you told me, I suggest the shelves are no more than eighty centimetres long, otherwise they'll sag over time. You have my mobile. Good evening."),
 ],
 "questions": [
  Q("Ποιο πρόβλημα βρήκε ο ξυλουργός;", ["Οι μετρήσεις ήταν λάθος", "Ο τοίχος δεν είναι ίσιος", "Ο τοίχος έχει υγρασία", "Η πόρτα του σαλονιού είναι στενή"], 1, "ο τοίχος σας δεν είναι ίσιος"),
  Q("Τι θέλει να κάνει πριν αρχίσει;", ["Να μιλήσει με τον διαχειριστή", "Να έρθει να δει τον τοίχο", "Να πάρει προκαταβολή", "Να αγοράσει το ξύλο"], 1, "θα ήθελα πρώτα να έρθω να το δω με τα μάτια μου"),
  Q("Τι προτείνει για να μείνει η τιμή ίδια;", ["Να γίνουν λιγότερα ράφια", "Να γίνει όλη η βιβλιοθήκη από καρυδιά", "Να γίνει ο σκελετός από καρυδιά και τα ράφια από δρυ", "Να περιμένουν μέχρι να πέσει η τιμή"], 2, "μπορώ να κάνω τον σκελετό από καρυδιά, που μοιάζει πολύ, και να κρατήσουμε τη δρυ μόνο για τα ράφια"),
  Q("Γιατί προτείνει τα ράφια να μην είναι πάνω από ογδόντα εκατοστά;", ["Για να χωρούν στο αυτοκίνητό του", "Γιατί αλλιώς θα λυγίσουν με τον καιρό", "Γιατί έτσι είναι φθηνότερα", "Γιατί ο τοίχος είναι μικρός"], 1, "αλλιώς με τον καιρό θα λυγίσουν"),
 ],
 "gloss": {"ξυλουργός": "ξυλουργός — carpenter", "μετρήσεις": "μέτρηση — measurement", "ίσιος": "ίσιος — straight", "κλίση": "κλίση — slope, lean", "πλαίσιο": "πλαίσιο — frame", "δρυς": "δρυς — oak", "ακριβύνει": "ακριβαίνω — to become more expensive", "σκελετό": "σκελετός — frame, carcass", "καρυδιά": "καρυδιά — walnut (tree, wood)", "ράφια": "ράφι — shelf", "λυγίσουν": "λυγίζω — to bend, sag"}
})

ITEMS.append({
 "id": "l253-c1-mono-lamptiras", "title": "Πολλοί πατέρες για ένα φως: η ιστορία του λαμπτήρα", "title_en": "Many fathers for one light: the history of the light bulb", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για την ιστορία των καθημερινών αντικειμένων.",
 "script": [
  L("Παρουσιάστρια", "f", "Αν ρωτήσετε ποιος εφηύρε τον ηλεκτρικό λαμπτήρα, οι περισσότεροι θα σας πουν «ο Έντισον». Η απάντηση δεν είναι λάθος, αλλά είναι ελλιπής. Για δεκαετίες πριν από αυτόν, δεκάδες εφευρέτες σε Ευρώπη και Αμερική προσπαθούσαν να κάνουν ένα σύρμα να λάμπει με το ρεύμα χωρίς να καεί σε λίγα λεπτά.", "If you ask who invented the electric light bulb, most people will tell you 'Edison'. The answer isn't wrong, but it is incomplete. For decades before him, dozens of inventors in Europe and America were trying to make a wire glow with electricity without burning out in a few minutes."),
  L("Παρουσιάστρια", "f", "Το πρόβλημα ήταν διπλό: έπρεπε να βρεθεί ένα νήμα που να αντέχει τη θερμότητα και να αφαιρεθεί ο αέρας από τη γυάλινη φούσκα, γιατί το οξυγόνο έκαιγε το νήμα. Στην Αγγλία ο Τζόζεφ Σουάν είχε παρουσιάσει λαμπτήρες με νήμα άνθρακα σχεδόν ταυτόχρονα με τον Έντισον, και οι δύο τελικά, αντί να συνεχίσουν τη δικαστική διαμάχη, ένωσαν τις εταιρείες τους.", "The problem was twofold: a filament had to be found that could withstand the heat, and the air had to be removed from the glass bulb, because the oxygen burned the filament. In England Joseph Swan had presented carbon-filament lamps almost at the same time as Edison, and the two eventually, rather than continue the legal dispute, merged their companies."),
  L("Παρουσιάστρια", "f", "Η πραγματική συμβολή του Έντισον ήταν ίσως άλλη: δεν έφτιαξε μόνο έναν λαμπτήρα που κρατούσε εκατοντάδες ώρες, αλλά σχεδίασε ολόκληρο το σύστημα γύρω του, από τις γεννήτριες και τα καλώδια μέχρι τους μετρητές. Ένας λαμπτήρας χωρίς δίκτυο ήταν απλώς ένα περίεργο αντικείμενο.", "Edison's real contribution was perhaps something else: he didn't only make a lamp that lasted hundreds of hours, but designed the whole system around it, from the generators and the cables to the meters. A lamp without a network was just a curious object."),
  L("Παρουσιάστρια", "f", "Τον εικοστό αιώνα το νήμα από βολφράμιο έκανε τους λαμπτήρες πιο φωτεινούς και ανθεκτικούς. Τη δεκαετία του 1920, όμως, οι μεγάλοι κατασκευαστές συμφώνησαν κρυφά να περιορίσουν τη διάρκεια ζωής τους στις χίλιες ώρες, ένα από τα πρώτα γνωστά παραδείγματα προγραμματισμένης απαξίωσης. Σήμερα ο κλασικός λαμπτήρας πυράκτωσης έχει σχεδόν εξαφανιστεί από την Ευρώπη, γιατί μετέτρεπε σε φως μόνο ένα μικρό μέρος της ενέργειας· το υπόλοιπο γινόταν θερμότητα.", "In the twentieth century the tungsten filament made bulbs brighter and more durable. In the 1920s, however, the big manufacturers secretly agreed to limit their life to a thousand hours, one of the first known examples of planned obsolescence. Today the classic incandescent bulb has almost disappeared from Europe, because it turned only a small part of its energy into light; the rest became heat."),
 ],
 "questions": [
  Q("Πώς κρίνει η παρουσιάστρια την απάντηση «ο Έντισον»;", ["Τη θεωρεί εντελώς λάθος", "Τη θεωρεί σωστή αλλά ελλιπή", "Τη θεωρεί μύθο", "Λέει ότι ο λαμπτήρας ήταν ιδέα του Σουάν"], 1, "Η απάντηση δεν είναι λάθος, αλλά είναι ελλιπής"),
  Q("Γιατί έπρεπε να αφαιρεθεί ο αέρας από τη φούσκα;", ["Γιατί το οξυγόνο έκαιγε το νήμα", "Γιατί έσπαγε το γυαλί", "Για να είναι ελαφρύτερος ο λαμπτήρας", "Για να αλλάζει το χρώμα του φωτός"], 0, "γιατί το οξυγόνο έκαιγε το νήμα"),
  Q("Ποια ήταν, κατά την παρουσιάστρια, η πραγματική συμβολή του Έντισον;", ["Η ανακάλυψη του άνθρακα", "Το ότι σχεδίασε ολόκληρο το σύστημα γύρω από τον λαμπτήρα", "Το ότι κέρδισε τη δίκη με τον Σουάν", "Το νήμα από βολφράμιο"], 1, "σχεδίασε ολόκληρο το σύστημα γύρω του"),
  Q("Τι συμφώνησαν κρυφά οι κατασκευαστές τη δεκαετία του 1920;", ["Να ανεβάσουν τις τιμές", "Να σταματήσουν να χρησιμοποιούν βολφράμιο", "Να περιορίσουν τη διάρκεια ζωής των λαμπτήρων στις χίλιες ώρες", "Να μοιραστούν τις αγορές της Ευρώπης"], 2, "συμφώνησαν κρυφά να περιορίσουν τη διάρκεια ζωής τους στις χίλιες ώρες"),
 ],
 "gloss": {"λαμπτήρα": "λαμπτήρας — light bulb", "ελλιπής": "ελλιπής — incomplete", "νήμα": "νήμα — filament; thread", "φούσκα": "φούσκα — bulb; bubble", "άνθρακα": "άνθρακας — carbon", "διαμάχη": "διαμάχη — dispute", "γεννήτριες": "γεννήτρια — generator", "μετρητές": "μετρητής — meter", "βολφράμιο": "βολφράμιο — tungsten", "απαξίωσης": "απαξίωση — obsolescence; devaluation", "πυράκτωσης": "πυράκτωση — incandescence"}
})

ITEMS.append({
 "id": "l253-c1-int-romaiko-skyrodema", "title": "Γιατί αντέχει δύο χιλιάδες χρόνια; Μια επιστήμονας υλικών για το ρωμαϊκό σκυρόδεμα", "title_en": "Why has it lasted two thousand years? A materials scientist on Roman concrete", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια επιστημονική εκπομπή του ραδιοφώνου.",
 "script": [
  L("Δημοσιογράφος", "m", "Ο θόλος του Πάνθεου στη Ρώμη στέκεται σχεδόν δύο χιλιάδες χρόνια, ενώ γέφυρες από σύγχρονο μπετόν χρειάζονται επισκευές μετά από λίγες δεκαετίες. Τι ήξεραν οι Ρωμαίοι που εμείς δεν ξέρουμε;", "The dome of the Pantheon in Rome has stood for almost two thousand years, while bridges made of modern concrete need repairs after a few decades. What did the Romans know that we don't?"),
  L("Επιστήμονας", "f", "Δεν ήξεραν περισσότερα, ήξεραν διαφορετικά. Ανακάτευαν ασβέστη με ηφαιστειακή στάχτη, κυρίως από την περιοχή γύρω από τον Βεζούβιο, και με κομμάτια πέτρας. Η στάχτη αντιδρά χημικά με τον ασβέστη και δημιουργεί ένα υλικό εξαιρετικά σταθερό. Το Πάνθεο, μάλιστα, παραμένει ο μεγαλύτερος θόλος από άοπλο σκυρόδεμα στον κόσμο.", "They didn't know more; they knew differently. They mixed lime with volcanic ash, mainly from the area around Vesuvius, and with pieces of stone. The ash reacts chemically with the lime and creates an extremely stable material. The Pantheon, in fact, remains the largest dome of unreinforced concrete in the world."),
  L("Δημοσιογράφος", "m", "Έχω διαβάσει ότι τα ρωμαϊκά λιμάνια γίνονται πιο ανθεκτικά μέσα στο θαλασσινό νερό. Πώς γίνεται αυτό;", "I've read that Roman harbours become more durable in seawater. How does that happen?"),
  L("Επιστήμονας", "f", "Αυτό είναι το πιο εντυπωσιακό. Το θαλασσινό νερό διεισδύει στο υλικό και, αντί να το διαβρώσει, προκαλεί την ανάπτυξη νέων κρυστάλλων μέσα στους πόρους, που το δένουν ακόμη περισσότερο. Πρόσφατες έρευνες έδειξαν επίσης ότι μικρά κομματάκια ασβέστη μέσα στη μάζα λειτουργούν σαν απόθεμα: όταν ανοίγει μια ρωγμή και μπαίνει νερό, ο ασβέστης διαλύεται και την ξανακλείνει. Είναι, ας πούμε, ένα υλικό που επουλώνει τον εαυτό του.", "That is the most impressive part. Seawater penetrates the material and, instead of eroding it, makes new crystals grow inside the pores, binding it even more. Recent research has also shown that small lumps of lime in the mass act as a reserve: when a crack opens and water gets in, the lime dissolves and seals it again. It is, so to speak, a material that heals itself."),
  L("Δημοσιογράφος", "m", "Γιατί, τότε, δεν χτίζουμε όπως οι Ρωμαίοι;", "Why, then, don't we build like the Romans?"),
  L("Επιστήμονας", "f", "Γιατί το ρωμαϊκό σκυρόδεμα αντέχει λιγότερο σε θλίψη και σκληραίνει πολύ πιο αργά, ενώ εμείς θέλουμε ουρανοξύστες και γέφυρες γρήγορα. Επιπλέον, το σύγχρονο μπετόν έχει μέσα σίδερα, που σκουριάζουν και το σπάνε από μέσα. Αυτό που κάνουμε σήμερα είναι να δανειζόμαστε ιδέες από τους Ρωμαίους, για παράδειγμα για κατασκευές που πρέπει να αντέχουν στη θάλασσα, όχι να τους αντιγράφουμε.", "Because Roman concrete is weaker in compression and hardens much more slowly, whereas we want skyscrapers and bridges fast. Moreover, modern concrete has steel inside it, which rusts and breaks it from within. What we do today is borrow ideas from the Romans, for example for structures that have to withstand the sea, not copy them."),
 ],
 "questions": [
  Q("Τι ανακάτευαν οι Ρωμαίοι για να φτιάξουν το σκυρόδεμά τους;", ["Τσιμέντο και σίδερα", "Ασβέστη, ηφαιστειακή στάχτη και κομμάτια πέτρας", "Πηλό και άχυρο", "Άμμο της θάλασσας και αλάτι"], 1, "Ανακάτευαν ασβέστη με ηφαιστειακή στάχτη"),
  Q("Τι συμβαίνει στο ρωμαϊκό σκυρόδεμα μέσα στο θαλασσινό νερό;", ["Διαβρώνεται γρήγορα", "Αναπτύσσονται νέοι κρύσταλλοι που το δένουν περισσότερο", "Αλλάζει χρώμα", "Γίνεται πιο ελαφρύ"], 1, "προκαλεί την ανάπτυξη νέων κρυστάλλων μέσα στους πόρους, που το δένουν ακόμη περισσότερο"),
  Q("Τι κάνουν τα μικρά κομματάκια ασβέστη όταν ανοίγει μια ρωγμή;", ["Διαλύονται και την ξανακλείνουν", "Τη μεγαλώνουν", "Απορροφούν όλο το νερό", "Σκληραίνουν και σπάνε"], 0, "ο ασβέστης διαλύεται και την ξανακλείνει"),
  Q("Γιατί δεν χτίζουμε σήμερα όπως οι Ρωμαίοι;", ["Γιατί η ηφαιστειακή στάχτη έχει τελειώσει", "Γιατί είναι πολύ ακριβό", "Γιατί αντέχει λιγότερο σε θλίψη και σκληραίνει πολύ πιο αργά", "Γιατί απαγορεύεται από τον νόμο"], 2, "αντέχει λιγότερο σε θλίψη και σκληραίνει πολύ πιο αργά"),
 ],
 "gloss": {"θόλος": "θόλος — dome", "μπετόν": "μπετόν — concrete (everyday word)", "ασβέστη": "ασβέστης — lime", "ηφαιστειακή": "ηφαιστειακός — volcanic", "άοπλο": "άοπλος — unreinforced (concrete); unarmed", "σκυρόδεμα": "σκυρόδεμα — concrete", "διεισδύει": "διεισδύω — to penetrate", "διαβρώσει": "διαβρώνω — to erode, corrode", "πόρους": "πόρος — pore", "ρωγμή": "ρωγμή — crack", "επουλώνει": "επουλώνω — to heal", "θλίψη": "θλίψη — compression (engineering); grief"}
})
rnd = random.Random(253)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-253.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
