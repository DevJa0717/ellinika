# Source for library/listening/listening-256.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l256.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l256-news-drachmes-sto-patari", "title": "Κουτί με δραχμές βρέθηκε στο πατάρι ενός παλιού σπιτιού", "title_en": "A box of drachmas is found in the loft of an old house", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο πρωινό δελτίο ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Μια απρόσμενη ανακάλυψη έκανε την περασμένη εβδομάδα μια εβδομηντάχρονη κάτοικος της πόλης μας. Καθαρίζοντας το πατάρι του πατρικού της, βρήκε ένα τενεκεδένιο κουτί από μπισκότα, γεμάτο χαρτονομίσματα των παλιών δραχμών.", "A seventy-year-old resident of our town made an unexpected discovery last week. While clearing out the loft of her family home, she found a tin biscuit box full of old drachma banknotes."),
  L("Εκφωνητής", "m", "Τα χρήματα, συνολικά πάνω από ένα εκατομμύριο δραχμές, φαίνεται πως τα είχε κρύψει ο πατέρας της, που πέθανε πριν από είκοσι χρόνια. «Δεν εμπιστευόταν τις τράπεζες», είπε η ίδια. «Τα μάζευε για να μου πάρει σπίτι, αλλά δεν μας το είπε ποτέ.»", "The money, more than a million drachmas in total, seems to have been hidden by her father, who died twenty years ago. 'He didn't trust banks,' she said. 'He was saving it to buy me a house, but he never told us.'"),
  L("Εκφωνητής", "m", "Δυστυχώς για εκείνη, τα χαρτονομίσματα δεν μπορούν πια να ανταλλαχθούν με ευρώ, αφού η προθεσμία για την ανταλλαγή τους έληξε το 2012. Ένας συλλέκτης της περιοχής εξήγησε, πάντως, ότι κάποια σπάνια χαρτονομίσματα, αν είναι σε καλή κατάσταση, έχουν συλλεκτική αξία.", "Unfortunately for her, the notes can no longer be exchanged for euros, since the deadline for exchanging them expired in 2012. A local collector explained, however, that some rare notes, if they are in good condition, have value to collectors."),
  L("Εκφωνητής", "m", "Η ίδια δεν φαίνεται απογοητευμένη. Δήλωσε ότι θα κρατήσει μερικά χαρτονομίσματα για τα εγγόνια της, «για να ξέρουν πώς ήταν τα λεφτά του προπάππου τους», και ότι τα υπόλοιπα θα τα χαρίσει στο λαογραφικό μουσείο της πόλης.", "She does not seem disappointed. She said she will keep a few notes for her grandchildren, 'so they know what their great-grandfather's money looked like', and will donate the rest to the town's folklore museum."),
 ],
 "questions": [
  Q("Πού βρέθηκε το κουτί;", ["Στο υπόγειο", "Στο πατάρι του πατρικού της", "Σε μια ντουλάπα της τράπεζας", "Στον κήπο"], 1, "Καθαρίζοντας το πατάρι του πατρικού της"),
  Q("Γιατί είχε κρύψει ο πατέρας της τα χρήματα;", ["Γιατί ήθελε να ταξιδέψει", "Γιατί δεν εμπιστευόταν τις τράπεζες", "Γιατί τα είχε κερδίσει στα χαρτιά", "Γιατί φοβόταν τους κλέφτες"], 1, "«Δεν εμπιστευόταν τις τράπεζες»"),
  Q("Γιατί δεν μπορούν να ανταλλαχθούν τα χαρτονομίσματα;", ["Γιατί είναι σκισμένα", "Γιατί η προθεσμία έληξε το 2012", "Γιατί είναι πλαστά", "Γιατί η τράπεζα έκλεισε"], 1, "η προθεσμία για την ανταλλαγή τους έληξε το 2012"),
  Q("Τι θα κάνει με τα περισσότερα χαρτονομίσματα;", ["Θα τα πουλήσει σε έναν συλλέκτη", "Θα τα δώσει στα εγγόνια της", "Θα τα χαρίσει στο λαογραφικό μουσείο", "Θα τα κάψει"], 2, "τα υπόλοιπα θα τα χαρίσει στο λαογραφικό μουσείο της πόλης"),
 ],
 "gloss": {"απρόσμενη": "απρόσμενος — unexpected", "πατάρι": "πατάρι — loft, attic", "πατρικού": "πατρικό — family home", "τενεκεδένιο": "τενεκεδένιος — tin (adj.)", "χαρτονομίσματα": "χαρτονόμισμα — banknote", "δραχμών": "δραχμή — drachma", "εμπιστευόταν": "εμπιστεύομαι — to trust", "ανταλλαχθούν": "ανταλλάσσω — to exchange", "προθεσμία": "προθεσμία — deadline", "συλλέκτης": "συλλέκτης — collector", "συλλεκτική": "συλλεκτικός — collector's (adj.)", "απογοητευμένη": "απογοητευμένος — disappointed", "λαογραφικό": "λαογραφικός — folklore (adj.)"}
})

ITEMS.append({
 "id": "l256-vm-scholi-ippasias", "title": "Μήνυμα από τη σχολή ιππασίας για το πρώτο μάθημα", "title_en": "A message from the riding school about the first lesson", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει ένα πρώτο μάθημα ιππασίας. Ακούτε ένα μήνυμα που σας άφησε στον τηλεφωνητή η εκπαιδεύτρια.",
 "script": [
  L("Ελπίδα", "f", "Γεια σας, η Ελπίδα είμαι, από τη σχολή ιππασίας στο Κορωπί. Σας παίρνω για το πρώτο σας μάθημα το Σάββατο στις δέκα. Παρακαλώ ελάτε ένα τέταρτο νωρίτερα, γιατί πριν ανεβείτε στο άλογο θα κάνουμε μια μικρή γνωριμία στον στάβλο.", "Hello, it's Elpida from the riding school in Koropi. I'm calling about your first lesson on Saturday at ten. Please come a quarter of an hour early, because before you get on the horse we'll do a short introduction in the stable."),
  L("Ελπίδα", "f", "Το κράνος σάς το δίνουμε εμείς. Χρειάζεστε όμως ένα μακρύ παντελόνι, όχι τζιν αν γίνεται, γιατί τρίβεται, και παπούτσια με μικρό τακούνι. Τα αθλητικά δεν είναι καλή ιδέα, γιατί γλιστράνε από τον αναβολέα.", "We provide the helmet. But you need long trousers, not jeans if possible, because they chafe, and shoes with a small heel. Trainers aren't a good idea, because they slip out of the stirrup."),
  L("Ελπίδα", "f", "Θα κάνετε μάθημα με τη Μέλισσα, μια φοράδα δεκαπέντε χρονών, πολύ ήρεμη, ιδανική για αρχάριους. Μην της δώσετε όμως τίποτα να φάει χωρίς να με ρωτήσετε πρώτα· έχει ευαίσθητο στομάχι.", "You'll have your lesson with Melissa, a fifteen-year-old mare, very calm, ideal for beginners. But don't give her anything to eat without asking me first; she has a sensitive stomach."),
  L("Ελπίδα", "f", "Αν βρέξει πολύ, το μάθημα θα γίνει στο σκεπαστό μανέζ, οπότε δεν ακυρώνεται. Αν όμως χρειαστεί να το ακυρώσετε εσείς, ενημερώστε με τουλάχιστον μία μέρα πριν. Τα λέμε το Σάββατο!", "If it rains a lot, the lesson will take place in the covered arena, so it won't be cancelled. But if you need to cancel it yourself, let me know at least one day before. See you on Saturday!"),
 ],
 "questions": [
  Q("Γιατί πρέπει να έρθετε νωρίτερα;", ["Για να συμπληρώσετε μια αίτηση", "Για να γνωριστείτε με το άλογο στον στάβλο", "Για να αγοράσετε κράνος", "Για να δείτε ένα βίντεο"], 1, "θα κάνουμε μια μικρή γνωριμία στον στάβλο"),
  Q("Γιατί δεν είναι καλή ιδέα τα αθλητικά παπούτσια;", ["Γιατί λερώνονται", "Γιατί γλιστράνε από τον αναβολέα", "Γιατί τρομάζουν το άλογο", "Γιατί είναι βαριά"], 1, "γλιστράνε από τον αναβολέα"),
  Q("Τι πρέπει να προσέχετε με τη Μέλισσα;", ["Να μην της μιλάτε δυνατά", "Να μην την πλησιάζετε από πίσω", "Να μην της δώσετε να φάει χωρίς να ρωτήσετε", "Να μην την αγγίζετε στο κεφάλι"], 2, "Μην της δώσετε όμως τίποτα να φάει χωρίς να με ρωτήσετε πρώτα"),
  Q("Τι θα γίνει αν βρέξει πολύ;", ["Το μάθημα θα ακυρωθεί", "Το μάθημα θα γίνει στο σκεπαστό μανέζ", "Το μάθημα θα μετατεθεί για την Κυριακή", "Θα γίνει θεωρητικό μάθημα"], 1, "το μάθημα θα γίνει στο σκεπαστό μανέζ"),
 ],
 "gloss": {"ιππασίας": "ιππασία — horse riding", "στάβλο": "στάβλος — stable", "κράνος": "κράνος — helmet", "τρίβεται": "τρίβομαι — to rub, chafe", "τακούνι": "τακούνι — heel", "γλιστράνε": "γλιστράω — to slip", "αναβολέα": "αναβολέας — stirrup", "φοράδα": "φοράδα — mare", "αρχάριους": "αρχάριος — beginner", "σκεπαστό": "σκεπαστός — covered", "μανέζ": "μανέζ — riding arena"}
})

ITEMS.append({
 "id": "l256-c1-mono-anelkystiras", "title": "«Όλα ασφαλή, κύριοι!»: η ιστορία του ανελκυστήρα", "title_en": "'All safe, gentlemen!': the history of the lift", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας ομιλίας σε έναν κύκλο εκδηλώσεων για την ιστορία της τεχνολογίας.",
 "script": [
  L("Ομιλητής", "m", "Μηχανισμοί που ανέβαζαν φορτία με σχοινιά και τροχαλίες υπήρχαν ήδη στην αρχαιότητα· στο Κολοσσαίο, για παράδειγμα, ανυψωτικές πλατφόρμες έφερναν τα θηρία από τα υπόγεια στην αρένα. Κανείς όμως δεν ήθελε να ταξιδεύει ο ίδιος με κάτι τέτοιο, για έναν απλό λόγο: αν έσπαγε το σχοινί, η πτώση ήταν θανατηφόρα.", "Mechanisms that raised loads with ropes and pulleys already existed in antiquity; in the Colosseum, for example, lifting platforms brought the wild animals from the underground chambers into the arena. But nobody wanted to travel on such a thing themselves, for a simple reason: if the rope broke, the fall was fatal."),
  L("Ομιλητής", "m", "Τη λύση έδωσε ένας Αμερικανός μηχανικός, ο Ελάιζα Ότις. Το 1854, σε μια έκθεση στη Νέα Υόρκη, ανέβηκε σε μια ανοιχτή πλατφόρμα ψηλά πάνω από το κοινό και διέταξε να κόψουν το σχοινί. Η πλατφόρμα έπεσε μόνο λίγα εκατοστά και σταμάτησε, γιατί ένα σύστημα από ελατήρια και οδοντωτές ράγες ενεργοποιήθηκε αυτόματα. «Όλα ασφαλή, κύριοι, όλα ασφαλή!», φώναξε, σύμφωνα με τη γνωστή διήγηση.", "The solution came from an American mechanic, Elisha Otis. In 1854, at an exhibition in New York, he went up on an open platform high above the audience and ordered the rope to be cut. The platform fell only a few centimetres and stopped, because a system of springs and toothed rails was activated automatically. 'All safe, gentlemen, all safe!' he shouted, according to the well-known account."),
  L("Ομιλητής", "m", "Λίγα χρόνια αργότερα εγκαταστάθηκε σε ένα κατάστημα της Νέας Υόρκης ο πρώτος ανελκυστήρας για επιβάτες με τέτοιο σύστημα ασφαλείας, που κινούνταν με ατμό. Χωρίς αυτή την εφεύρεση, οι ουρανοξύστες που ακολούθησαν θα ήταν πρακτικά άχρηστοι, αφού κανείς δεν θα ανέβαινε με τα πόδια είκοσι ορόφους.", "A few years later the first passenger lift with such a safety system, powered by steam, was installed in a New York shop. Without this invention, the skyscrapers that followed would have been practically useless, since nobody would climb twenty floors on foot."),
  L("Ομιλητής", "m", "Υπάρχει και μια λιγότερο γνωστή συνέπεια. Πριν από τον ανελκυστήρα, οι ψηλότεροι όροφοι ήταν οι φθηνότεροι, και εκεί έμεναν οι υπηρέτες και οι φτωχοί. Ο ανελκυστήρας αντέστρεψε αυτή την ιεραρχία: σήμερα το ρετιρέ με τη θέα είναι το πιο ακριβό διαμέρισμα της πολυκατοικίας.", "There is also a lesser-known consequence. Before the lift, the highest floors were the cheapest, and that is where servants and the poor lived. The lift reversed this hierarchy: today the penthouse with the view is the most expensive flat in the building."),
 ],
 "questions": [
  Q("Γιατί κανείς δεν ήθελε να ταξιδεύει με τους παλιούς ανυψωτικούς μηχανισμούς;", ["Γιατί ήταν πολύ αργοί", "Γιατί αν έσπαγε το σχοινί η πτώση ήταν θανατηφόρα", "Γιατί ήταν πολύ ακριβοί", "Γιατί προορίζονταν μόνο για ζώα"], 1, "αν έσπαγε το σχοινί, η πτώση ήταν θανατηφόρα"),
  Q("Τι έκανε ο Ότις στην έκθεση του 1854;", ["Παρουσίασε έναν ηλεκτρικό ανελκυστήρα", "Διέταξε να κόψουν το σχοινί ενώ στεκόταν στην πλατφόρμα", "Ανέβηκε με τα πόδια σε έναν πύργο", "Πούλησε τον πρώτο ανελκυστήρα"], 1, "διέταξε να κόψουν το σχοινί"),
  Q("Πώς κινούνταν ο πρώτος ανελκυστήρας για επιβάτες;", ["Με ηλεκτρισμό", "Με ατμό", "Με νερό", "Με τα χέρια"], 1, "που κινούνταν με ατμό"),
  Q("Ποια λιγότερο γνωστή συνέπεια αναφέρει ο ομιλητής;", ["Ότι οι πολυκατοικίες έγιναν πιο φθηνές", "Ότι οι ψηλότεροι όροφοι έγιναν οι πιο ακριβοί", "Ότι εξαφανίστηκαν οι σκάλες", "Ότι οι υπηρέτες μετακόμισαν στα προάστια"], 1, "σήμερα το ρετιρέ με τη θέα είναι το πιο ακριβό διαμέρισμα"),
 ],
 "gloss": {"τροχαλίες": "τροχαλία — pulley", "ανυψωτικές": "ανυψωτικός — lifting (adj.)", "θηρία": "θηρίο — wild beast", "θανατηφόρα": "θανατηφόρος — fatal", "διέταξε": "διατάζω — to order", "ελατήρια": "ελατήριο — spring", "οδοντωτές": "οδοντωτός — toothed", "ενεργοποιήθηκε": "ενεργοποιούμαι — to be activated", "ανελκυστήρας": "ανελκυστήρας — lift, elevator", "ουρανοξύστες": "ουρανοξύστης — skyscraper", "αντέστρεψε": "αντιστρέφω — to reverse", "ιεραρχία": "ιεραρχία — hierarchy", "ρετιρέ": "ρετιρέ — penthouse, top-floor flat"}
})

ITEMS.append({
 "id": "l256-c1-int-koloumpo", "title": "Ένα ηφαίστειο κάτω από τη θάλασσα: μια ηφαιστειολόγος για το Κολούμπο", "title_en": "A volcano under the sea: a volcanologist on Kolumbo", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια επιστημονική εκπομπή του ραδιοφώνου.",
 "script": [
  L("Δημοσιογράφος", "m", "Όταν λέμε «ηφαίστειο της Σαντορίνης», όλοι σκεφτόμαστε την καλντέρα. Εσείς όμως μελετάτε ένα άλλο ηφαίστειο, που δεν το βλέπει κανείς.", "When we say 'the Santorini volcano', we all think of the caldera. But you study another volcano, one that nobody can see."),
  L("Ηφαιστειολόγος", "f", "Ακριβώς. Λίγα χιλιόμετρα βορειοανατολικά της Σαντορίνης, κάτω από τη θάλασσα, βρίσκεται το Κολούμπο. Είναι ένας υποθαλάσσιος κρατήρας με διάμετρο περίπου ενάμισι χιλιόμετρο, και η κορυφή του βρίσκεται μόλις μερικές δεκάδες μέτρα κάτω από την επιφάνεια.", "Exactly. A few kilometres north-east of Santorini, under the sea, lies Kolumbo. It is a submarine crater about one and a half kilometres in diameter, and its top is only a few dozen metres below the surface."),
  L("Δημοσιογράφος", "m", "Έχει εκραγεί ποτέ στην ιστορική εποχή;", "Has it ever erupted in historical times?"),
  L("Ηφαιστειολόγος", "f", "Ναι, το 1650. Οι πηγές της εποχής περιγράφουν τη θάλασσα να βράζει, ένα παλιρροϊκό κύμα που χτύπησε τις ακτές και, το χειρότερο, τοξικά αέρια που έφτασαν ως τη Σαντορίνη και σκότωσαν δεκάδες ανθρώπους και πολλά ζώα. Κάποια στιγμή η έκρηξη έχτισε για λίγο ένα νησάκι, που η θάλασσα το διέβρωσε γρήγορα.", "Yes, in 1650. Sources from the time describe the sea boiling, a tidal wave that struck the coasts and, worst of all, toxic gases that reached Santorini and killed dozens of people and many animals. At one point the eruption briefly built a small island, which the sea quickly eroded."),
  L("Δημοσιογράφος", "m", "Και σήμερα; Πρέπει να ανησυχούμε;", "And today? Should we worry?"),
  L("Ηφαιστειολόγος", "f", "Το ηφαίστειο είναι ενεργό, αλλά αυτό δεν σημαίνει ότι επίκειται έκρηξη. Στον πυθμένα του κρατήρα υπάρχουν θερμές πηγές, από τις οποίες βγαίνουν αέρια και ζεστά ρευστά, και γύρω τους ζουν μικροοργανισμοί προσαρμοσμένοι σε ακραίες συνθήκες. Γι' αυτό τοποθετούμε όργανα στον βυθό, που μετρούν συνεχώς τη θερμοκρασία, τη χημεία του νερού και τη σεισμικότητα. Η παρακολούθηση δεν σταματά την έκρηξη, μας δίνει όμως χρόνο.", "The volcano is active, but that doesn't mean an eruption is imminent. On the floor of the crater there are hot vents, from which gases and hot fluids escape, and around them live micro-organisms adapted to extreme conditions. That's why we place instruments on the seabed that continuously measure temperature, water chemistry and seismic activity. Monitoring doesn't stop an eruption, but it gives us time."),
 ],
 "questions": [
  Q("Πού βρίσκεται το Κολούμπο;", ["Μέσα στην καλντέρα", "Βορειοανατολικά της Σαντορίνης, κάτω από τη θάλασσα", "Στη Νίσυρο", "Νότια της Κρήτης"], 1, "Λίγα χιλιόμετρα βορειοανατολικά της Σαντορίνης, κάτω από τη θάλασσα"),
  Q("Ποια ήταν η χειρότερη συνέπεια της έκρηξης του 1650;", ["Ένα παλιρροϊκό κύμα", "Η στάχτη που κάλυψε τα χωράφια", "Τα τοξικά αέρια που σκότωσαν ανθρώπους και ζώα", "Ένας μεγάλος σεισμός"], 2, "το χειρότερο, τοξικά αέρια που έφτασαν ως τη Σαντορίνη"),
  Q("Τι συνέβη στο νησάκι που δημιούργησε η έκρηξη;", ["Υπάρχει ακόμη", "Το διέβρωσε γρήγορα η θάλασσα", "Ενώθηκε με τη Σαντορίνη", "Το κάλυψε η λάβα"], 1, "που η θάλασσα το διέβρωσε γρήγορα"),
  Q("Τι προσφέρει, κατά την ηφαιστειολόγο, η παρακολούθηση;", ["Σταματά την έκρηξη", "Δίνει χρόνο", "Μειώνει τους σεισμούς", "Ψύχει το νερό"], 1, "μας δίνει όμως χρόνο"),
 ],
 "gloss": {"καλντέρα": "καλντέρα — caldera", "υποθαλάσσιος": "υποθαλάσσιος — submarine, undersea", "κρατήρας": "κρατήρας — crater", "διάμετρο": "διάμετρος — diameter", "εκραγεί": "εκρήγνυμαι — to erupt, explode", "παλιρροϊκό": "παλιρροϊκό κύμα — tidal wave", "τοξικά": "τοξικός — toxic", "διέβρωσε": "διαβρώνω — to erode", "επίκειται": "επίκειμαι — to be imminent", "πυθμένα": "πυθμένας — bottom, floor (of the sea)", "ρευστά": "ρευστό — fluid", "σεισμικότητα": "σεισμικότητα — seismicity, seismic activity"}
})
rnd = random.Random(256)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-256.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
