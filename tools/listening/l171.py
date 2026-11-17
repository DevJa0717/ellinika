# Source for library/listening/listening-171.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l171.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l171-ann-ypogeio-parking", "title": "Ανακοίνωση στο υπόγειο πάρκινγκ", "title_en": "An announcement in the underground car park", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός υπόγειου πάρκινγκ στο κέντρο της πόλης.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί πελάτες, σας ενημερώνουμε ότι την Κυριακή ο δεύτερος υπόγειος όροφος θα παραμείνει κλειστός όλη την ημέρα για καθαρισμό και βάψιμο των διαγραμμίσεων.", "Dear customers, we inform you that on Sunday the second underground level will remain closed all day for cleaning and repainting of the lines."),
  L("Εκφωνήτρια", "f", "Όσοι έχετε σταθμεύσει εκεί, παρακαλούμε να μετακινήσετε τα αυτοκίνητά σας μέχρι το Σάββατο στις δέκα το βράδυ. Τα οχήματα που θα βρεθούν στον όροφο μετά από αυτή την ώρα θα μεταφερθούν με γερανό στον πρώτο όροφο, χωρίς χρέωση.", "Those of you who have parked there, please move your cars by Saturday at ten in the evening. Vehicles found on the level after that time will be moved by tow truck to the first level, free of charge."),
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε επίσης ότι τα αυτόματα μηχανήματα πληρωμής βρίσκονται στο ισόγειο, δίπλα στους ανελκυστήρες, και δέχονται μόνο κάρτες. Για πληρωμή με μετρητά, απευθυνθείτε στο ταμείο της εξόδου. Ευχαριστούμε για την κατανόηση.", "We also remind you that the automatic pay machines are on the ground floor, next to the lifts, and accept cards only. To pay in cash, go to the cash desk at the exit. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί θα κλείσει ο δεύτερος υπόγειος όροφος;", ["Για καθαρισμό και βάψιμο των διαγραμμίσεων", "Για επισκευή των ανελκυστήρων", "Λόγω πλημμύρας", "Για μια εκδήλωση"], 0, "για καθαρισμό και βάψιμο των διαγραμμίσεων"),
  Q("Τι θα γίνει με τα αυτοκίνητα που θα μείνουν στον όροφο μετά τις δέκα το Σάββατο;", ["Οι ιδιοκτήτες θα πληρώσουν πρόστιμο", "Θα μεταφερθούν στον πρώτο όροφο χωρίς χρέωση", "Θα μείνουν κλειδωμένα ως τη Δευτέρα", "Θα μεταφερθούν σε άλλο πάρκινγκ"], 1, "θα μεταφερθούν με γερανό στον πρώτο όροφο, χωρίς χρέωση"),
  Q("Πού μπορεί κανείς να πληρώσει με μετρητά;", ["Στα μηχανήματα του ισογείου", "Στον φύλακα κάθε ορόφου", "Στο ταμείο της εξόδου", "Μόνο ηλεκτρονικά"], 2, "Για πληρωμή με μετρητά, απευθυνθείτε στο ταμείο της εξόδου"),
 ],
 "gloss": {"πάρκινγκ": "πάρκινγκ — car park", "υπόγειος": "υπόγειος — underground", "διαγραμμίσεων": "διαγράμμιση — road markings, lines", "σταθμεύσει": "σταθμεύω — to park", "οχήματα": "όχημα — vehicle", "γερανό": "γερανός — tow truck; crane", "χρέωση": "χρέωση — charge", "ισόγειο": "ισόγειο — ground floor", "ανελκυστήρες": "ανελκυστήρας — lift, elevator", "μετρητά": "μετρητά — cash", "απευθυνθείτε": "απευθύνομαι — to go to, to contact"},
})

ITEMS.append({
 "id": "l171-int-foni-ton-stathmon", "title": "Η φωνή των σταθμών", "title_en": "The voice of the stations", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια ηθοποιό που έχει ηχογραφήσει τις ανακοινώσεις σε σταθμούς τρένων.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί ακούνε τη φωνή σας κάθε μέρα χωρίς να ξέρουν ποια είστε. Πώς ξεκίνησε αυτό;", "Many people hear your voice every day without knowing who you are. How did this start?"),
  L("Ηθοποιός", "f", "Από μια ακρόαση. Έψαχναν μια φωνή ήρεμη αλλά καθαρή, που να ακούγεται μέσα στον θόρυβο ενός σταθμού. Πήγαμε σαράντα ηθοποιοί και, για κάποιο λόγο, διάλεξαν εμένα.", "From an audition. They were looking for a voice that was calm but clear, that could be heard in the noise of a station. Forty actors went and, for some reason, they chose me."),
  L("Δημοσιογράφος", "m", "Πώς γίνεται η ηχογράφηση; Λέτε ολόκληρες ανακοινώσεις;", "How is the recording done? Do you say whole announcements?"),
  L("Ηθοποιός", "f", "Όχι, λέω κομμάτια: ονόματα σταθμών, αριθμούς, ώρες, φράσεις όπως «καθυστερεί περίπου». Ο υπολογιστής μετά τα ενώνει. Το δύσκολο είναι να λέω κάθε λέξη με τον ίδιο τόνο, ώστε όταν ενωθούν να μην ακούγονται σαν μωσαϊκό. Μείναμε στο στούντιο δύο εβδομάδες.", "No, I say pieces: station names, numbers, times, phrases like 'is delayed by about'. The computer then joins them. The hard part is saying every word in the same tone, so that when they are joined they don't sound like a mosaic. We stayed in the studio for two weeks."),
  L("Δημοσιογράφος", "m", "Πώς νιώθετε όταν ακούτε τον εαυτό σας στον σταθμό;", "How do you feel when you hear yourself at the station?"),
  L("Ηθοποιός", "f", "Στην αρχή ντρεπόμουν. Τώρα με διασκεδάζει. Μια φορά ανακοίνωσα, με τη φωνή των μεγαφώνων, ότι το δικό μου τρένο θα καθυστερήσει, και ένας κύριος δίπλα μου είπε: «Αυτή η κυρία πάντα φέρνει κακά νέα».", "At first I was embarrassed. Now it amuses me. Once, in the voice of the loudspeakers, I announced that my own train would be delayed, and a man next to me said: 'That lady always brings bad news.'"),
 ],
 "questions": [
  Q("Τι είδους φωνή έψαχναν;", ["Μια φωνή νεανική και χαρούμενη", "Μια φωνή ήρεμη αλλά καθαρή", "Μια φωνή βαθιά και αντρική", "Μια φωνή με ξένη προφορά"], 1, "Έψαχναν μια φωνή ήρεμη αλλά καθαρή"),
  Q("Ποιο ήταν το δύσκολο στην ηχογράφηση;", ["Να λέει κάθε λέξη με τον ίδιο τόνο", "Να μάθει απέξω μεγάλα κείμενα", "Να μιλάει πολύ γρήγορα", "Να ηχογραφεί μέσα στον σταθμό"], 0, "Το δύσκολο είναι να λέω κάθε λέξη με τον ίδιο τόνο"),
  Q("Τι είπε ο κύριος στον σταθμό;", ["Ότι η φωνή της είναι πολύ δυνατή", "Ότι την αναγνώρισε", "Ότι αυτή η κυρία πάντα φέρνει κακά νέα", "Ότι το τρένο του θα έρθει νωρίτερα"], 2, "«Αυτή η κυρία πάντα φέρνει κακά νέα»"),
 ],
 "gloss": {"ηχογραφήσει": "ηχογραφώ — to record", "ακρόαση": "ακρόαση — audition", "θόρυβο": "θόρυβος — noise", "ηχογράφηση": "ηχογράφηση — recording", "καθυστερεί": "καθυστερώ — to be delayed", "τόνο": "τόνος — tone", "μωσαϊκό": "μωσαϊκό — mosaic", "ντρεπόμουν": "ντρέπομαι — to be embarrassed", "διασκεδάζει": "διασκεδάζω — to amuse", "μεγαφώνων": "μεγάφωνο — loudspeaker"},
})

ITEMS.append({
 "id": "l171-int-katharistis-tzamion", "title": "Ο καθαριστής τζαμιών στα ψηλά κτίρια", "title_en": "The window cleaner on tall buildings", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν άντρα που καθαρίζει τα τζάμια ψηλών κτιρίων κρεμασμένος με σχοινιά.",
 "script": [
  L("Δημοσιογράφος", "f", "Δεν φοβάστε το ύψος;", "Aren't you afraid of heights?"),
  L("Καθαριστής", "m", "Τον πρώτο μήνα φοβόμουν, και καλά έκανα. Ο φόβος σε κάνει προσεκτικό. Τώρα δεν φοβάμαι, αλλά σέβομαι το ύψος. Πριν κατέβω, ελέγχω δύο φορές κάθε σχοινί και κάθε κόμπο, ακόμα κι αν τα έλεγξε ήδη ο συνάδελφός μου.", "The first month I was afraid, and rightly so. Fear makes you careful. Now I'm not afraid, but I respect the height. Before I go down, I check every rope and every knot twice, even if my colleague has already checked them."),
  L("Δημοσιογράφος", "f", "Ποιος είναι ο μεγαλύτερος εχθρός σας;", "What is your biggest enemy?"),
  L("Καθαριστής", "m", "Ο αέρας. Με τη βροχή μπορείς να δουλέψεις, αλλά όταν φυσάει πάνω από πέντε μποφόρ σταματάμε. Το σχοινί αρχίζει να κουνιέται και χτυπάς στο τζάμι. Το καλοκαίρι πάλι ξεκινάμε στις έξι το πρωί, γιατί το μεσημέρι το γυαλί καίει.", "The wind. You can work in the rain, but when it blows over five Beaufort we stop. The rope starts swinging and you hit the glass. In summer, on the other hand, we start at six in the morning, because at midday the glass burns."),
  L("Δημοσιογράφος", "f", "Βλέπετε ενδιαφέροντα πράγματα μέσα από τα παράθυρα;", "Do you see interesting things through the windows?"),
  L("Καθαριστής", "m", "Κυρίως γραφεία και ανθρώπους που κοιτάνε οθόνες. Μερικοί δεν μας προσέχουν καν. Άλλοι μας χαιρετάνε. Ένα παιδί σε ένα νοσοκομείο μού κολλούσε ζωγραφιές στο τζάμι κάθε φορά που περνούσα. Τις έχω ακόμα φωτογραφίες στο κινητό.", "Mostly offices and people looking at screens. Some don't even notice us. Others wave at us. A child in a hospital used to stick drawings on the glass for me every time I passed. I still have photos of them on my phone."),
 ],
 "questions": [
  Q("Τι λέει για τον φόβο;", ["Ότι δεν φοβήθηκε ποτέ", "Ότι ο φόβος σε κάνει προσεκτικό", "Ότι φοβάται ακόμα κάθε μέρα", "Ότι ο φόβος είναι ο μεγαλύτερος εχθρός του"], 1, "Ο φόβος σε κάνει προσεκτικό"),
  Q("Πότε σταματούν τη δουλειά;", ["Όταν βρέχει", "Όταν φυσάει πάνω από πέντε μποφόρ", "Το μεσημέρι του χειμώνα", "Όταν έχει ομίχλη"], 1, "όταν φυσάει πάνω από πέντε μποφόρ σταματάμε"),
  Q("Τι έκανε το παιδί στο νοσοκομείο;", ["Του κολλούσε ζωγραφιές στο τζάμι", "Του έγραφε γράμματα", "Του έκανε φωτογραφίες", "Του χτυπούσε το τζάμι"], 0, "Ένα παιδί σε ένα νοσοκομείο μού κολλούσε ζωγραφιές στο τζάμι"),
 ],
 "gloss": {"τζάμια": "τζάμι — window pane", "κρεμασμένος": "κρεμασμένος — hanging", "σχοινιά": "σχοινί — rope", "ύψος": "ύψος — height", "σέβομαι": "σέβομαι — to respect", "κόμπο": "κόμπος — knot", "εχθρός": "εχθρός — enemy", "μποφόρ": "μποφόρ — Beaufort (wind force)", "κουνιέται": "κουνιέμαι — to swing, sway", "γυαλί": "γυαλί — glass", "ζωγραφιές": "ζωγραφιά — drawing"},
})

ITEMS.append({
 "id": "l171-dia-pou-tha-kremasoume", "title": "Πού θα κρεμάσουμε τον πίνακα;", "title_en": "Where shall we hang the painting?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητάει πού θα κρεμάσει έναν πίνακα που του χάρισαν.",
 "script": [
  L("Ελένη", "f", "Λοιπόν, πού θα τον βάλουμε; Εγώ λέω πάνω από τον καναπέ. Εκεί ο τοίχος είναι άδειος εδώ και δύο χρόνια.", "So, where shall we put it? I say above the sofa. The wall there has been empty for two years."),
  L("Μάριος", "m", "Πάνω από τον καναπέ τον βλέπει ο ήλιος όλο το απόγευμα. Η θεία σου είπε ότι είναι λάδι και ότι ο ήλιος θα ξεθωριάσει τα χρώματα.", "Above the sofa the sun shines on it all afternoon. Your aunt said it's oil and that the sun will fade the colours."),
  L("Ελένη", "f", "Σωστά. Τότε στον διάδρομο; Εκεί δεν μπαίνει ήλιος.", "Right. The hallway then? No sun gets in there."),
  L("Μάριος", "m", "Ο διάδρομος είναι πολύ στενός. Για να δεις έναν τόσο μεγάλο πίνακα, πρέπει να σταθείς τουλάχιστον δύο μέτρα μακριά. Στον διάδρομο θα τον βλέπουμε από τόσο κοντά, που θα φαίνονται μόνο πινελιές.", "The hallway is too narrow. To see such a big painting you have to stand at least two metres away. In the hallway we'll see it from so close that only brushstrokes will show."),
  L("Ελένη", "f", "Και ο τοίχος στην τραπεζαρία; Απέναντι από το παράθυρο, οπότε ο ήλιος δεν τον χτυπάει κατευθείαν.", "And the wall in the dining room? It's opposite the window, so the sun doesn't hit it directly."),
  L("Μάριος", "m", "Ναι, αυτό μου αρέσει. Μόνο που εκεί ο τοίχος είναι από γυψοσανίδα. Θα χρειαστούμε ειδικά βύσματα, γιατί ένα απλό καρφί δεν θα αντέξει το βάρος.", "Yes, I like that. Only the wall there is plasterboard. We'll need special wall plugs, because a simple nail won't hold the weight."),
  L("Ελένη", "f", "Ωραία. Αύριο περνάω από το σιδεράδικο. Και πες στη θεία μου ότι θα έρθει να τον εγκαινιάσει.", "Great. Tomorrow I'll stop by the hardware shop. And tell my aunt she's coming to inaugurate it."),
 ],
 "questions": [
  Q("Γιατί δεν τον κρεμάνε πάνω από τον καναπέ;", ["Γιατί ο τοίχος είναι στενός", "Γιατί ο ήλιος θα ξεθωριάσει τα χρώματα", "Γιατί εκεί υπάρχει ήδη άλλος πίνακας", "Γιατί δεν αρέσει στη θεία"], 1, "ο ήλιος θα ξεθωριάσει τα χρώματα"),
  Q("Τι πρόβλημα έχει ο διάδρομος;", ["Είναι πολύ σκοτεινός", "Έχει υγρασία", "Είναι πολύ στενός για να δεις τον πίνακα από μακριά", "Έχει πολλές πόρτες"], 2, "Ο διάδρομος είναι πολύ στενός"),
  Q("Τι θα χρειαστούν για τον τοίχο της τραπεζαρίας;", ["Ειδικά βύσματα", "Ένα απλό καρφί", "Μια σκάλα", "Καινούργια μπογιά"], 0, "Θα χρειαστούμε ειδικά βύσματα"),
 ],
 "gloss": {"κρεμάσει": "κρεμάω — to hang", "καναπέ": "καναπές — sofa", "ξεθωριάσει": "ξεθωριάζω — to fade", "διάδρομο": "διάδρομος — hallway", "πινελιές": "πινελιά — brushstroke", "τραπεζαρία": "τραπεζαρία — dining room", "γυψοσανίδα": "γυψοσανίδα — plasterboard", "βύσματα": "βύσμα — wall plug", "καρφί": "καρφί — nail", "σιδεράδικο": "σιδεράδικο — hardware shop", "εγκαινιάσει": "εγκαινιάζω — to inaugurate"},
})

ITEMS.append({
 "id": "l171-dia-tzamaria-sto-mpalkoni", "title": "Να κλείσουμε το μπαλκόνι με τζαμαρία;", "title_en": "Shall we enclose the balcony with glass?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο αδέρφια να συζητούν αν θα κλείσουν το μπαλκόνι του πατρικού τους σπιτιού με τζαμαρία.",
 "script": [
  L("Στέλιος", "m", "Σκέφτομαι να κλείσουμε το μπαλκόνι του μπαμπά με τζαμαρία. Τον χειμώνα θα είναι σαν ένα επιπλέον δωμάτιο, και θα κάθεται εκεί με τον ήλιο.", "I'm thinking of enclosing Dad's balcony with glass. In winter it'll be like an extra room, and he'll sit there in the sun."),
  L("Δήμητρα", "f", "Ακούγεται ωραίο, αλλά ρώτησες αν επιτρέπεται; Σε πολλές πολυκατοικίες χρειάζεται η συμφωνία όλων των ιδιοκτητών, γιατί αλλάζει η όψη του κτιρίου.", "It sounds nice, but have you asked whether it's allowed? In many apartment blocks you need the agreement of all the owners, because it changes the look of the building."),
  L("Στέλιος", "m", "Ο διαχειριστής μού είπε ότι υπάρχουν συρόμενα τζάμια χωρίς πλαίσιο, που μαζεύονται στη μία άκρη το καλοκαίρι. Από έξω σχεδόν δεν φαίνονται.", "The building manager told me there are frameless sliding panes that fold to one side in summer. From outside they're almost invisible."),
  L("Δήμητρα", "f", "Πάλι θα πρέπει να ρωτήσουμε στη γενική συνέλευση. Και κάτι άλλο: ο μπαμπάς αγαπάει τις γλάστρες του. Αν κλείσει το μπαλκόνι, τα φυτά θα ζεσταθούν υπερβολικά το καλοκαίρι.", "We'd still have to ask at the general meeting. And something else: Dad loves his flowerpots. If the balcony is closed, the plants will overheat in summer."),
  L("Στέλιος", "m", "Γι' αυτό λέω για τα συρόμενα. Το καλοκαίρι θα είναι ανοιχτό, όπως τώρα.", "That's why I'm talking about the sliding ones. In summer it'll be open, as it is now."),
  L("Δήμητρα", "f", "Εντάξει. Αλλά πρώτα ρωτάμε τον ίδιο. Μην του κάνουμε έκπληξη ένα πράγμα που μπορεί να μην το θέλει.", "OK. But first we ask him. Let's not surprise him with something he might not want."),
 ],
 "questions": [
  Q("Τι ανησυχεί τη Δήμητρα στην αρχή;", ["Το κόστος", "Αν επιτρέπεται στην πολυκατοικία", "Ο θόρυβος από τον δρόμο", "Η ασφάλεια του πατέρα"], 1, "ρώτησες αν επιτρέπεται"),
  Q("Τι λέει η Δήμητρα για τα φυτά του πατέρα;", ["Ότι θα ζεσταθούν υπερβολικά το καλοκαίρι", "Ότι θα παγώσουν τον χειμώνα", "Ότι πρέπει να τα μεταφέρουν", "Ότι πρέπει να ποτίζονται συχνότερα"], 0, "τα φυτά θα ζεσταθούν υπερβολικά το καλοκαίρι"),
  Q("Σε τι καταλήγουν;", ["Να κάνουν έκπληξη στον πατέρα", "Να μην κάνουν τίποτα", "Να ρωτήσουν πρώτα τον πατέρα", "Να βάλουν τζαμαρία με πλαίσιο"], 2, "πρώτα ρωτάμε τον ίδιο"),
 ],
 "gloss": {"μπαλκόνι": "μπαλκόνι — balcony", "πατρικού": "πατρικό — family home", "τζαμαρία": "τζαμαρία — glass enclosure", "επιπλέον": "επιπλέον — extra", "πολυκατοικίες": "πολυκατοικία — apartment block", "όψη": "όψη — appearance, façade", "διαχειριστής": "διαχειριστής — building manager", "συρόμενα": "συρόμενος — sliding", "πλαίσιο": "πλαίσιο — frame", "γενική συνέλευση": "γενική συνέλευση — general meeting", "γλάστρες": "γλάστρα — flowerpot", "έκπληξη": "έκπληξη — surprise"},
})

ITEMS.append({
 "id": "l171-mon-diaititis-gia-mia-mera", "title": "Διαιτητής για μια μέρα", "title_en": "Referee for a day", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν πατέρα να διηγείται πώς βρέθηκε να σφυρίζει σε έναν αγώνα ποδοσφαίρου παιδιών.",
 "script": [
  L("Πατέρας", "m", "Πήγα να δω τον γιο μου να παίζει μπάλα, σε ένα τουρνουά για παιδιά δέκα χρονών. Δέκα λεπτά πριν από τον αγώνα, ο προπονητής ήρθε τρέχοντας: ο διαιτητής είχε αρρωστήσει. Με κοίταξε και είπε: «Εσύ έπαιζες μπάλα, δεν έπαιζες;» Πριν από είκοσι πέντε χρόνια, του είπα.", "I went to watch my son play football, in a tournament for ten-year-olds. Ten minutes before the match, the coach came running: the referee had fallen ill. He looked at me and said: 'You used to play football, didn't you?' Twenty-five years ago, I told him."),
  L("Πατέρας", "m", "Μου έδωσαν μια σφυρίχτρα και ένα κίτρινο μπλουζάκι, που μου ήταν μικρό. Τα παιδιά ήταν υπέροχα. Όταν κάποιος έπεφτε, ο αντίπαλος σταματούσε και τον βοηθούσε να σηκωθεί. Το πρόβλημα ήταν οι γονείς στην κερκίδα.", "They gave me a whistle and a yellow T-shirt, which was too small for me. The children were wonderful. When someone fell, the opponent would stop and help him up. The problem was the parents in the stands."),
  L("Πατέρας", "m", "Σε κάθε απόφαση, κάποιος φώναζε. Ένας πατέρας μού είπε ότι δεν ξέρω τους κανόνες. Είχε δίκιο, εν μέρει, γιατί οι κανόνες για τα παιδιά είναι διαφορετικοί: δεν υπάρχει οφσάιντ, για παράδειγμα. Στο ημίχρονο τους διάβασα στο κινητό.", "At every decision, someone shouted. One father told me I didn't know the rules. He was partly right, because the rules for children are different: there's no offside, for example. At half-time I read them on my phone."),
  L("Πατέρας", "m", "Από τότε, όταν βλέπω έναν διαιτητή, ακόμα και στην τηλεόραση, δεν φωνάζω ποτέ. Και ο γιος μου; Έχασαν δύο ένα, και μου είπε ότι έφταιγα εγώ.", "Since then, when I see a referee, even on TV, I never shout. And my son? They lost two-one, and he told me it was my fault."),
 ],
 "questions": [
  Q("Γιατί έγινε διαιτητής;", ["Γιατί ήταν προπονητής της ομάδας", "Γιατί ο διαιτητής είχε αρρωστήσει", "Γιατί του το ζήτησε ο γιος του", "Γιατί είχε κάνει σχετικά μαθήματα"], 1, "ο διαιτητής είχε αρρωστήσει"),
  Q("Ποιο ήταν, κατά τον ίδιο, το πρόβλημα στον αγώνα;", ["Τα παιδιά που τσακώνονταν", "Το μικρό μπλουζάκι", "Οι γονείς στην κερκίδα", "Η βροχή"], 2, "Το πρόβλημα ήταν οι γονείς στην κερκίδα"),
  Q("Τι έκανε στο ημίχρονο;", ["Διάβασε τους κανόνες στο κινητό", "Μίλησε με τους γονείς", "Άλλαξε μπλουζάκι", "Τηλεφώνησε στον κανονικό διαιτητή"], 0, "Στο ημίχρονο τους διάβασα στο κινητό"),
 ],
 "gloss": {"σφυρίζει": "σφυρίζω — to blow the whistle", "διαιτητής": "διαιτητής — referee", "τουρνουά": "τουρνουά — tournament", "προπονητής": "προπονητής — coach", "σφυρίχτρα": "σφυρίχτρα — whistle", "αντίπαλος": "αντίπαλος — opponent", "κερκίδα": "κερκίδα — stands", "εν μέρει": "εν μέρει — partly", "οφσάιντ": "οφσάιντ — offside", "ημίχρονο": "ημίχρονο — half-time", "έφταιγα": "φταίω — to be to blame"},
})

ITEMS.append({
 "id": "l171-vm-ekpaideftis-odigisis", "title": "Μήνυμα από τον εκπαιδευτή οδήγησης", "title_en": "A message from the driving instructor", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον εκπαιδευτή σας στη σχολή οδηγών.",
 "script": [
  L("Εκπαιδευτής", "m", "Καλησπέρα, Άννα, ο Νίκος από τη σχολή οδηγών. Έχω ένα καλό και ένα λιγότερο καλό νέο. Το καλό είναι ότι βγήκε η ημερομηνία της εξέτασης: Τρίτη είκοσι έξι, στις οχτώ το πρωί.", "Good evening, Anna, it's Nikos from the driving school. I have one piece of good news and one less good. The good news is that the test date is out: Tuesday the twenty-sixth, at eight in the morning."),
  L("Εκπαιδευτής", "m", "Το λιγότερο καλό είναι ότι το αυτοκίνητο με το οποίο κάνουμε μάθημα θα είναι στο συνεργείο την επόμενη εβδομάδα. Τα δύο τελευταία μαθήματα θα τα κάνουμε με το μεγαλύτερο, το λευκό. Δεν είναι κακό, γιατί με αυτό θα δώσεις και την εξέταση.", "The less good news is that the car we have lessons in will be at the garage next week. We'll do the last two lessons in the bigger one, the white one. That's not bad, because you'll also take the test in it."),
  L("Εκπαιδευτής", "m", "Θα σου πρότεινα να κάνουμε κι ένα επιπλέον μάθημα μόνο για παρκάρισμα, γιατί στο λευκό οι διαστάσεις είναι διαφορετικές. Πες μου αν σε βολεύει το Σάββατο το πρωί. Και μην ξεχάσεις να φέρεις την ταυτότητά σου την ημέρα της εξέτασης, αλλιώς δεν θα σε αφήσουν να δώσεις.", "I'd suggest we also do an extra lesson just for parking, because in the white one the dimensions are different. Tell me if Saturday morning suits you. And don't forget to bring your ID card on the day of the test, otherwise they won't let you take it."),
 ],
 "questions": [
  Q("Πότε είναι η εξέταση;", ["Τη Δευτέρα στις οχτώ", "Την Τρίτη στις οχτώ το πρωί", "Το Σάββατο το πρωί", "Την Τρίτη το απόγευμα"], 1, "Τρίτη είκοσι έξι, στις οχτώ το πρωί"),
  Q("Γιατί προτείνει ένα επιπλέον μάθημα;", ["Γιατί η Άννα κάνει λάθη στις στροφές", "Για παρκάρισμα, γιατί το λευκό αυτοκίνητο έχει άλλες διαστάσεις", "Γιατί η εξέταση έγινε πιο δύσκολη", "Για να μάθει να οδηγεί στον αυτοκινητόδρομο"], 1, "στο λευκό οι διαστάσεις είναι διαφορετικές"),
  Q("Τι πρέπει να φέρει η Άννα την ημέρα της εξέτασης;", ["Την ταυτότητά της", "Τα γυαλιά της", "Τα χρήματα για την εξέταση", "Μια ιατρική βεβαίωση"], 0, "μην ξεχάσεις να φέρεις την ταυτότητά σου"),
 ],
 "gloss": {"εκπαιδευτή": "εκπαιδευτής — instructor", "σχολή οδηγών": "σχολή οδηγών — driving school", "εξέτασης": "εξέταση — test, exam", "συνεργείο": "συνεργείο — garage, repair shop", "επιπλέον": "επιπλέον — extra", "παρκάρισμα": "παρκάρισμα — parking", "διαστάσεις": "διάσταση — dimension", "βολεύει": "βολεύω — to suit", "ταυτότητά": "ταυτότητα — ID card"},
})

ITEMS.append({
 "id": "l171-vm-etaireia-kourier", "title": "Μήνυμα από την εταιρεία κούριερ", "title_en": "A message from the courier company", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από μια εταιρεία ταχυμεταφορών (κούριερ).",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, σας καλούμε από την εταιρεία ταχυμεταφορών για την αποστολή σας από τη Γερμανία. Ο συνεργάτης μας πέρασε σήμερα στις έντεκα από τη διεύθυνσή σας, αλλά δεν βρήκε κανέναν και το κουδούνι με το όνομά σας δεν λειτουργούσε.", "Good morning, we're calling from the courier company about your shipment from Germany. Our driver came by your address today at eleven, but found no one, and the bell with your name wasn't working."),
  L("Υπάλληλος", "f", "Επειδή το δέμα προέρχεται από χώρα εκτός Ελλάδας και η αξία του ξεπερνά τα εκατόν πενήντα ευρώ, χρειάζεται και η υπογραφή σας. Γι' αυτό δεν μπορούμε να το αφήσουμε σε γείτονα.", "Because the parcel comes from a country outside Greece and its value exceeds one hundred and fifty euros, your signature is also required. That's why we can't leave it with a neighbour."),
  L("Υπάλληλος", "f", "Έχετε δύο επιλογές: να ορίσετε νέα ημέρα παράδοσης από την ιστοσελίδα μας, ή να το παραλάβετε από το κατάστημά μας στην οδό Πατησίων μέσα σε επτά εργάσιμες ημέρες. Μετά από αυτό το διάστημα, το δέμα επιστρέφεται στον αποστολέα. Ευχαριστούμε.", "You have two options: set a new delivery day on our website, or collect it from our shop on Patision Street within seven working days. After that period, the parcel is returned to the sender. Thank you."),
 ],
 "questions": [
  Q("Γιατί δεν παραδόθηκε το δέμα;", ["Γιατί η διεύθυνση ήταν λάθος", "Γιατί δεν βρήκε κανέναν και το κουδούνι δεν λειτουργούσε", "Γιατί το δέμα είχε καταστραφεί", "Γιατί ο συνεργάτης δεν βρήκε το σπίτι"], 1, "δεν βρήκε κανέναν και το κουδούνι με το όνομά σας δεν λειτουργούσε"),
  Q("Γιατί δεν μπορούν να το αφήσουν σε γείτονα;", ["Γιατί χρειάζεται η υπογραφή του παραλήπτη", "Γιατί είναι πολύ βαρύ", "Γιατί οι γείτονες δεν ήταν σπίτι", "Γιατί πρέπει να πληρωθεί με μετρητά"], 0, "χρειάζεται και η υπογραφή σας"),
  Q("Τι θα γίνει αν δεν το παραλάβει μέσα σε επτά εργάσιμες;", ["Θα πληρώσει πρόστιμο", "Θα το πάρει ο γείτονας", "Θα επιστραφεί στον αποστολέα", "Θα σταλεί σε άλλο κατάστημα"], 2, "το δέμα επιστρέφεται στον αποστολέα"),
 ],
 "gloss": {"ταχυμεταφορών": "ταχυμεταφορές — courier services", "κούριερ": "κούριερ — courier", "αποστολή": "αποστολή — shipment", "κουδούνι": "κουδούνι — doorbell", "δέμα": "δέμα — parcel", "ξεπερνά": "ξεπερνώ — to exceed", "υπογραφή": "υπογραφή — signature", "παράδοσης": "παράδοση — delivery", "παραλάβετε": "παραλαμβάνω — to collect, receive", "εργάσιμες": "εργάσιμος — working (day)", "αποστολέα": "αποστολέας — sender"},
})

ITEMS.append({
 "id": "l171-c1-giati-almyri-thalassa", "title": "Γιατί η θάλασσα είναι αλμυρή", "title_en": "Why the sea is salty", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε επιστημονική εκπομπή με μια ωκεανογράφο για την αλμυρότητα της θάλασσας.",
 "script": [
  L("Παρουσιαστής", "m", "Τα ποτάμια έχουν γλυκό νερό και χύνονται στη θάλασσα. Γιατί τότε η θάλασσα είναι αλμυρή;", "Rivers have fresh water and flow into the sea. Why then is the sea salty?"),
  L("Ωκεανογράφος", "f", "Είναι ένα από τα ωραιότερα παράδοξα. Το νερό των ποταμών δεν είναι εντελώς γλυκό· περιέχει μικρές ποσότητες διαλυμένων αλάτων, που η βροχή αποσπά από τα πετρώματα καθώς τα διαβρώνει. Οι ποσότητες είναι τόσο μικρές, που δεν τις καταλαβαίνουμε στη γεύση. Όταν όμως το νερό φτάσει στη θάλασσα, εξατμίζεται, ενώ τα άλατα μένουν πίσω. Αυτό συμβαίνει εδώ και εκατοντάδες εκατομμύρια χρόνια, και έτσι τα άλατα συσσωρεύτηκαν.", "It's one of the loveliest paradoxes. River water is not completely fresh; it contains small amounts of dissolved salts, which rain detaches from rocks as it erodes them. The amounts are so small that we can't taste them. But when the water reaches the sea, it evaporates, while the salts stay behind. This has been happening for hundreds of millions of years, and so the salts have accumulated."),
  L("Παρουσιαστής", "m", "Δηλαδή όλο το αλάτι έρχεται από τη στεριά;", "So all the salt comes from the land?"),
  L("Ωκεανογράφος", "f", "Όχι όλο. Το νάτριο προέρχεται κυρίως από τα πετρώματα, αλλά μεγάλο μέρος του χλωρίου έχει άλλη πηγή: τα ηφαίστεια και τις υδροθερμικές πηγές στον βυθό, που απελευθερώνουν αέρια από το εσωτερικό της Γης. Νάτριο και χλώριο μαζί δίνουν το γνωστό μας μαγειρικό αλάτι.", "Not all of it. Sodium comes mainly from rocks, but a large part of the chlorine has another source: volcanoes and the hydrothermal vents on the seabed, which release gases from the Earth's interior. Sodium and chlorine together make our familiar table salt."),
  L("Παρουσιαστής", "m", "Είναι όλες οι θάλασσες το ίδιο αλμυρές;", "Are all seas equally salty?"),
  L("Ωκεανογράφος", "f", "Καθόλου. Κατά μέσο όρο οι ωκεανοί έχουν περίπου τρεισήμισι τοις εκατό αλάτι. Η Μεσόγειος είναι πιο αλμυρή, γιατί η εξάτμιση είναι μεγαλύτερη από το νερό που φέρνουν τα ποτάμια και η βροχή. Αντίθετα, η Βαλτική, με πολλά ποτάμια και λίγη εξάτμιση, είναι σχεδόν υφάλμυρη. Και η Νεκρά Θάλασσα, που δεν έχει έξοδο, είναι σχεδόν δέκα φορές πιο αλμυρή από τον ωκεανό· γι' αυτό επιπλέεις χωρίς καμία προσπάθεια.", "Not at all. On average the oceans contain about three and a half per cent salt. The Mediterranean is saltier, because evaporation is greater than the water brought by rivers and rain. By contrast, the Baltic, with many rivers and little evaporation, is almost brackish. And the Dead Sea, which has no outlet, is almost ten times saltier than the ocean; that's why you float without any effort."),
 ],
 "questions": [
  Q("Πώς φτάνουν τα άλατα στη θάλασσα σύμφωνα με την ωκεανογράφο;", ["Τα φέρνει ο άνεμος από την έρημο", "Τα ποτάμια μεταφέρουν μικρές ποσότητες που η βροχή αποσπά από τα πετρώματα", "Δημιουργούνται από τα ψάρια", "Τα φέρνουν οι πάγοι που λιώνουν"], 1, "μικρές ποσότητες διαλυμένων αλάτων, που η βροχή αποσπά από τα πετρώματα"),
  Q("Από πού προέρχεται μεγάλο μέρος του χλωρίου;", ["Από τα ηφαίστεια και τις υδροθερμικές πηγές", "Από τα πετρώματα της στεριάς", "Από τη βροχή", "Από τα φύκια"], 0, "τα ηφαίστεια και τις υδροθερμικές πηγές στον βυθό"),
  Q("Γιατί η Μεσόγειος είναι πιο αλμυρή από τον μέσο ωκεανό;", ["Γιατί είναι πιο βαθιά", "Γιατί δεν έχει καθόλου ποτάμια", "Γιατί η εξάτμιση είναι μεγαλύτερη από το νερό που φέρνουν τα ποτάμια και η βροχή", "Γιατί έχει πολλά ηφαίστεια"], 2, "η εξάτμιση είναι μεγαλύτερη από το νερό που φέρνουν τα ποτάμια και η βροχή"),
 ],
 "gloss": {"ωκεανογράφο": "ωκεανογράφος — oceanographer", "αλμυρότητα": "αλμυρότητα — salinity", "χύνονται": "χύνομαι — to flow into", "παράδοξα": "παράδοξο — paradox", "διαλυμένων": "διαλυμένος — dissolved", "αποσπά": "αποσπώ — to detach", "πετρώματα": "πέτρωμα — rock", "διαβρώνει": "διαβρώνω — to erode", "εξατμίζεται": "εξατμίζομαι — to evaporate", "συσσωρεύτηκαν": "συσσωρεύομαι — to accumulate", "νάτριο": "νάτριο — sodium", "χλωρίου": "χλώριο — chlorine", "υδροθερμικές πηγές": "υδροθερμική πηγή — hydrothermal vent", "βυθό": "βυθός — seabed", "εξάτμιση": "εξάτμιση — evaporation", "υφάλμυρη": "υφάλμυρος — brackish", "επιπλέεις": "επιπλέω — to float"},
})

ITEMS.append({
 "id": "l171-c1-giati-trempopaizoun-ta-asteria", "title": "Γιατί τα αστέρια τρεμοπαίζουν και οι πλανήτες όχι", "title_en": "Why stars twinkle and planets don't", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν ερασιτέχνη αστρονόμο να εξηγεί σε μια βραδιά παρατήρησης του ουρανού γιατί τα αστέρια τρεμοπαίζουν.",
 "script": [
  L("Αστρονόμος", "m", "Αν κοιτάξετε απόψε προς τα ανατολικά, θα δείτε δύο φωτεινά σημάδια. Το ένα τρεμοπαίζει και αλλάζει ελαφρά χρώμα· είναι ένα αστέρι. Το άλλο λάμπει σταθερά· είναι ο Δίας. Αυτός είναι ο πιο απλός τρόπος να ξεχωρίσετε έναν πλανήτη χωρίς τηλεσκόπιο.", "If you look east tonight, you'll see two bright points. One twinkles and changes colour slightly; it's a star. The other shines steadily; it's Jupiter. That's the simplest way to tell a planet apart without a telescope."),
  L("Αστρονόμος", "m", "Το τρεμόπαιγμα δεν οφείλεται στο ίδιο το αστέρι, αλλά στην ατμόσφαιρά μας. Ο αέρας πάνω από τα κεφάλια μας δεν είναι ομοιογενής· αποτελείται από στρώματα με διαφορετική θερμοκρασία και πυκνότητα, που κινούνται συνεχώς. Κάθε φορά που το φως περνά από ένα τέτοιο στρώμα, διαθλάται λίγο διαφορετικά, και η εικόνα του αστεριού πηδάει ανεπαίσθητα από σημείο σε σημείο.", "The twinkling is not due to the star itself but to our atmosphere. The air above our heads is not uniform; it consists of layers with different temperature and density, which move constantly. Each time the light passes through such a layer it is refracted slightly differently, and the star's image jumps imperceptibly from point to point."),
  L("Αστρονόμος", "m", "Γιατί όμως δεν συμβαίνει το ίδιο με τους πλανήτες; Επειδή τα αστέρια είναι τόσο μακριά, που φτάνουν σε εμάς σαν σημεία χωρίς διάσταση. Ένας πλανήτης, αντίθετα, είναι αρκετά κοντά ώστε να φαίνεται σαν ένας μικροσκοπικός δίσκος. Ο δίσκος αυτός αποτελείται από αμέτρητα σημεία, και οι αναταράξεις τους αλληλοαναιρούνται· το σύνολο μένει σταθερό.", "But why doesn't the same happen with planets? Because stars are so far away that they reach us as points with no size. A planet, by contrast, is close enough to look like a tiny disc. That disc is made of countless points, and their disturbances cancel each other out; the whole stays steady."),
  L("Αστρονόμος", "m", "Γι' αυτό και τα αστέρια κοντά στον ορίζοντα τρεμοπαίζουν περισσότερο: το φως τους διασχίζει πολύ περισσότερο αέρα. Και γι' αυτό τα μεγάλα τηλεσκόπια χτίζονται σε ψηλά βουνά ή στέλνονται στο διάστημα, μακριά από τις αναταράξεις της ατμόσφαιρας.", "That's also why stars near the horizon twinkle more: their light crosses much more air. And that's why large telescopes are built on high mountains or sent into space, far from the disturbances of the atmosphere."),
 ],
 "questions": [
  Q("Σε τι οφείλεται το τρεμόπαιγμα των αστεριών;", ["Στις εκρήξεις στην επιφάνεια των αστεριών", "Στα στρώματα της ατμόσφαιρας που κινούνται συνεχώς", "Στην απόσταση από τη Σελήνη", "Στη μόλυνση των πόλεων"], 1, "στρώματα με διαφορετική θερμοκρασία και πυκνότητα, που κινούνται συνεχώς"),
  Q("Γιατί οι πλανήτες δεν τρεμοπαίζουν;", ["Γιατί έχουν δικό τους φως", "Γιατί κινούνται πιο αργά", "Γιατί φαίνονται σαν μικροσκοπικός δίσκος και οι αναταράξεις αλληλοαναιρούνται", "Γιατί βρίσκονται πάνω από την ατμόσφαιρα"], 2, "οι αναταράξεις τους αλληλοαναιρούνται"),
  Q("Γιατί τα αστέρια κοντά στον ορίζοντα τρεμοπαίζουν περισσότερο;", ["Γιατί το φως τους διασχίζει πολύ περισσότερο αέρα", "Γιατί είναι πιο μακριά", "Γιατί είναι μεγαλύτερα", "Γιατί είναι πιο κοντά στον Ήλιο"], 0, "το φως τους διασχίζει πολύ περισσότερο αέρα"),
 ],
 "gloss": {"ερασιτέχνη": "ερασιτέχνης — amateur", "τρεμοπαίζουν": "τρεμοπαίζω — to twinkle, flicker", "τρεμοπαίζει": "τρεμοπαίζω — to twinkle, flicker", "τηλεσκόπιο": "τηλεσκόπιο — telescope", "τρεμόπαιγμα": "τρεμόπαιγμα — twinkling", "ομοιογενής": "ομοιογενής — uniform", "στρώματα": "στρώμα — layer", "πυκνότητα": "πυκνότητα — density", "διαθλάται": "διαθλώμαι — to be refracted", "ανεπαίσθητα": "ανεπαίσθητα — imperceptibly", "δίσκος": "δίσκος — disc", "αναταράξεις": "αναταραχή — turbulence, disturbance", "αλληλοαναιρούνται": "αλληλοαναιρούνται — to cancel each other out", "ορίζοντα": "ορίζοντας — horizon", "διασχίζει": "διασχίζω — to cross"},
})

rnd = random.Random(171)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-171.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
