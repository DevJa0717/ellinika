# Source for library/listening/listening-207.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l207.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l207-news-skoni-sacharas", "title": "Σκόνη από τη Σαχάρα πάνω από την Αθήνα", "title_en": "Saharan dust over Athens", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων στο ραδιόφωνο ένα ανοιξιάτικο πρωί.",
 "script": [
  L("Εκφωνητής", "m", "Πορτοκαλί ουρανός και χαμηλή ορατότητα σήμερα σε μεγάλο μέρος της χώρας. Οι νότιοι άνεμοι μεταφέρουν μεγάλες ποσότητες σκόνης από τη Σαχάρα, και οι συγκεντρώσεις σωματιδίων στον αέρα της Αθήνας είναι πολλαπλάσιες από τα επιτρεπτά όρια.", "An orange sky and low visibility today over much of the country. The southerly winds are carrying large amounts of dust from the Sahara, and the concentrations of particles in Athens's air are many times higher than the permitted limits."),
  L("Εκφωνητής", "m", "Οι γιατροί συνιστούν στους ηλικιωμένους, στις εγκύους και σε όσους έχουν άσθμα ή καρδιοπάθειες να μένουν όσο γίνεται μέσα στο σπίτι και να κρατούν τα παράθυρα κλειστά. Δεν είναι καλή μέρα για τρέξιμο ή ποδήλατο στους δρόμους· όσοι πρέπει να κυκλοφορήσουν καλό είναι να φορούν μάσκα.", "Doctors advise the elderly, pregnant women and those with asthma or heart conditions to stay indoors as much as possible and keep the windows closed. It isn't a good day for running or cycling in the streets; those who have to go out would do well to wear a mask."),
  L("Εκφωνητής", "m", "Σύμφωνα με τους μετεωρολόγους, το φαινόμενο θα κορυφωθεί απόψε, ενώ αύριο οι βροχές που αναμένονται θα φέρουν τη γνωστή λασποβροχή. Όσοι σκέφτονταν να πλύνουν το αυτοκίνητό τους, ας περιμένουν μέχρι την Πέμπτη.", "According to meteorologists, the phenomenon will peak tonight, while tomorrow the expected rain will bring the familiar mud rain. Anyone thinking of washing their car had better wait until Thursday."),
 ],
 "questions": [
  Q("Τι προκαλεί το φαινόμενο;", ["Οι πυρκαγιές", "Οι νότιοι άνεμοι που φέρνουν σκόνη από τη Σαχάρα", "Η κίνηση των αυτοκινήτων", "Ένα ηφαίστειο"], 1, "Οι νότιοι άνεμοι μεταφέρουν μεγάλες ποσότητες σκόνης από τη Σαχάρα"),
  Q("Σε ποιους απευθύνονται κυρίως οι συστάσεις των γιατρών;", ["Στους οδηγούς", "Σε ηλικιωμένους, εγκύους και όσους έχουν άσθμα ή καρδιοπάθειες", "Στους μαθητές", "Στους τουρίστες"], 1, "στους ηλικιωμένους, στις εγκύους και σε όσους έχουν άσθμα ή καρδιοπάθειες"),
  Q("Τι θα φέρουν οι αυριανές βροχές;", ["Καθαρό αέρα αμέσως", "Χαλάζι", "Λασποβροχή", "Πλημμύρες"], 2, "θα φέρουν τη γνωστή λασποβροχή"),
  Q("Τι συμβουλεύει ο εκφωνητής όσους θέλουν να πλύνουν το αυτοκίνητο;", ["Να το πλύνουν σήμερα", "Να περιμένουν μέχρι την Πέμπτη", "Να το βάλουν σε γκαράζ", "Να το σκεπάσουν"], 1, "ας περιμένουν μέχρι την Πέμπτη"),
 ],
 "gloss": {"ορατότητα": "ορατότητα — visibility", "σωματιδίων": "σωματίδιο — particle", "πολλαπλάσιες": "πολλαπλάσιος — many times greater", "επιτρεπτά": "επιτρεπτός — permitted", "εγκύους": "έγκυος — pregnant woman", "καρδιοπάθειες": "καρδιοπάθεια — heart condition", "κορυφωθεί": "κορυφώνομαι — to peak", "λασποβροχή": "λασποβροχή — mud rain"},
})
ITEMS.append({
 "id": "l207-dia-stegnotirio", "title": "Στεγνωτήριο ή απλώστρα;", "title_en": "A tumble dryer or a clothes rack?", "type": "dialogue", "level": "B2",
 "context_el": "Δύο συγκάτοικοι συζητούν αν θα αγοράσουν στεγνωτήριο ρούχων.",
 "script": [
  L("Φαίη", "f", "Τρεις μέρες τώρα τα ρούχα κρέμονται στο σαλόνι και δεν λένε να στεγνώσουν. Το διαμέρισμα μυρίζει υγρασία. Λέω να πάρουμε στεγνωτήριο.", "For three days now the clothes have been hanging in the living room and they just won't dry. The flat smells of damp. I say we get a tumble dryer."),
  L("Στέλιος", "m", "Στεγνωτήριο; Ξέρεις πόσο ρεύμα καίει; Θα το δούμε στον λογαριασμό. Και ζούμε σε μια χώρα με ήλιο τριακόσιες μέρες τον χρόνο.", "A dryer? Do you know how much electricity it uses? We'll see it on the bill. And we live in a country with sun three hundred days a year."),
  L("Φαίη", "f", "Οι άλλες εξήντα πέφτουν όλες τον Νοέμβριο. Υπάρχουν και καινούργια μοντέλα με αντλία θερμότητας, που καταναλώνουν πολύ λιγότερο. Τα έχω κοιτάξει.", "The other sixty all fall in November. There are also new models with a heat pump that use much less. I've looked into them."),
  L("Στέλιος", "m", "Και πού θα το βάλουμε; Το μπάνιο χωράει μόλις το πλυντήριο. Τι θα έλεγες για μια απλώστρα στο μπαλκόνι με ένα πλαστικό κάλυμμα, και έναν αφυγραντήρα για τις πολύ υγρές μέρες;", "And where would we put it? The bathroom barely fits the washing machine. What would you say to a rack on the balcony with a plastic cover, and a dehumidifier for the really damp days?"),
  L("Φαίη", "f", "Ο αφυγραντήρας δεν είναι κακή ιδέα. Θα βοηθήσει και με τη μούχλα στη γωνία του υπνοδωματίου. Εντάξει, ας ξεκινήσουμε από αυτό, και αν δεν τα καταφέρει, ξανασυζητάμε το στεγνωτήριο.", "The dehumidifier isn't a bad idea. It'll also help with the mould in the corner of the bedroom. OK, let's start with that, and if it doesn't manage, we'll discuss the dryer again."),
 ],
 "questions": [
  Q("Ποιο πρόβλημα αναφέρει η Φαίη;", ["Ότι το πλυντήριο χάλασε", "Ότι τα ρούχα δεν στεγνώνουν και το διαμέρισμα μυρίζει υγρασία", "Ότι δεν υπάρχει μπαλκόνι", "Ότι ο λογαριασμός ρεύματος είναι υψηλός"], 1, "τα ρούχα κρέμονται στο σαλόνι και δεν λένε να στεγνώσουν. Το διαμέρισμα μυρίζει υγρασία"),
  Q("Ποια είναι η πρώτη αντίρρηση του Στέλιου;", ["Ότι είναι άσχημο", "Ότι καταναλώνει πολύ ρεύμα", "Ότι χαλάει τα ρούχα", "Ότι κάνει θόρυβο"], 1, "Ξέρεις πόσο ρεύμα καίει;"),
  Q("Τι απαντά η Φαίη για την κατανάλωση;", ["Ότι το ρεύμα είναι φθηνό", "Ότι θα το χρησιμοποιούν σπάνια", "Ότι υπάρχουν μοντέλα με αντλία θερμότητας που καταναλώνουν πολύ λιγότερο", "Ότι θα πληρώσει εκείνη"], 2, "μοντέλα με αντλία θερμότητας, που καταναλώνουν πολύ λιγότερο"),
  Q("Τι αποφασίζουν τελικά;", ["Να αγοράσουν στεγνωτήριο", "Να ξεκινήσουν με αφυγραντήρα και απλώστρα στο μπαλκόνι", "Να πηγαίνουν στο πλυντήριο της γειτονιάς", "Να μετακομίσουν"], 1, "ας ξεκινήσουμε από αυτό"),
 ],
 "gloss": {"στεγνωτήριο": "στεγνωτήριο — tumble dryer", "απλώστρα": "απλώστρα — clothes rack, airer", "συγκάτοικοι": "συγκάτοικος — flatmate", "δεν λένε να στεγνώσουν": "δεν λέει να — just won't", "αντλία θερμότητας": "αντλία θερμότητας — heat pump", "κάλυμμα": "κάλυμμα — cover", "αφυγραντήρα": "αφυγραντήρας — dehumidifier", "μούχλα": "μούχλα — mould"},
})
ITEMS.append({
 "id": "l207-c1-mono-molyvi", "title": "Ένα μολύβι χωρίς μόλυβδο", "title_en": "A pencil without lead", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για την ιστορία των καθημερινών αντικειμένων.",
 "script": [
  L("Παρουσιαστής", "m", "Λέμε «μολύβι», και στα αγγλικά λένε ακόμη «lead», δηλαδή μόλυβδος. Κι όμως, κανένα μολύβι δεν περιείχε ποτέ μόλυβδο. Η παρεξήγηση ξεκινά τον 16ο αιώνα στο Μπόροουντεϊλ της βόρειας Αγγλίας, όπου βρέθηκε ένα κοίτασμα από ένα μαύρο, γυαλιστερό υλικό που άφηνε σημάδι στο χαρτί. Οι άνθρωποι νόμισαν ότι ήταν ένα είδος μολύβδου. Ήταν γραφίτης.", "We say «μολύβι», and in English they still say 'lead'. And yet no pencil ever contained lead. The misunderstanding begins in the 16th century in Borrowdale in northern England, where a deposit of a black, shiny material that left a mark on paper was found. People thought it was a kind of lead. It was graphite."),
  L("Παρουσιαστής", "m", "Ο γραφίτης του Μπόροουντεϊλ ήταν τόσο καθαρός, ώστε τον έκοβαν σε λεπτά ραβδάκια. Ήταν και τόσο πολύτιμος, που το ορυχείο φυλασσόταν. Στα τέλη του 18ου αιώνα η Γαλλία, σε πόλεμο με τη Βρετανία, δεν είχε πρόσβαση σε αυτόν. Τότε ο Νικολά-Ζακ Κοντέ βρήκε τη λύση: ανακάτεψε σκόνη γραφίτη με πηλό και το έψησε. Αλλάζοντας την αναλογία, μπορούσε να φτιάξει μολύβια πιο σκληρά ή πιο μαλακά. Αυτή η μέθοδος χρησιμοποιείται, με λίγες αλλαγές, μέχρι σήμερα.", "Borrowdale graphite was so pure that it was cut into thin sticks. It was also so valuable that the mine was guarded. At the end of the 18th century France, at war with Britain, had no access to it. Then Nicolas-Jacques Conté found the solution: he mixed graphite powder with clay and fired it. By changing the proportion, he could make harder or softer pencils. This method is still used today with few changes."),
  L("Παρουσιαστής", "m", "Και γιατί τόσα μολύβια είναι κίτρινα; Λέγεται ότι στα τέλη του 19ου αιώνα μια εταιρεία έβαψε τα δικά της κίτρινα, για να δείξει ότι ο γραφίτης της ήταν εξαιρετικής ποιότητας. Η ιστορία δεν είναι απολύτως επιβεβαιωμένη, όμως το κίτρινο μολύβι έγινε, σε πολλές χώρες, το μολύβι «κατά τεκμήριο».", "And why are so many pencils yellow? It's said that at the end of the 19th century a company painted its pencils yellow to show that its graphite was of exceptional quality. The story isn't fully confirmed, but the yellow pencil became, in many countries, the 'default' pencil."),
 ],
 "questions": [
  Q("Γιατί το μολύβι ονομάστηκε έτσι;", ["Γιατί αρχικά περιείχε μόλυβδο", "Γιατί οι άνθρωποι νόμισαν ότι ο γραφίτης ήταν είδος μολύβδου", "Γιατί ήταν βαρύ", "Από το όνομα του εφευρέτη του"], 1, "Οι άνθρωποι νόμισαν ότι ήταν ένα είδος μολύβδου. Ήταν γραφίτης"),
  Q("Γιατί φυλασσόταν το ορυχείο του Μπόροουντεϊλ;", ["Γιατί ήταν επικίνδυνο", "Γιατί ο γραφίτης ήταν πολύ πολύτιμος", "Γιατί ήταν σε στρατιωτική περιοχή", "Γιατί ανήκε στον βασιλιά"], 1, "Ήταν και τόσο πολύτιμος, που το ορυχείο φυλασσόταν"),
  Q("Ποια ήταν η λύση του Κοντέ;", ["Βρήκε καινούργιο ορυχείο στη Γαλλία", "Ανακάτεψε σκόνη γραφίτη με πηλό και το έψησε", "Χρησιμοποίησε κάρβουνο", "Αγόρασε γραφίτη κρυφά από την Αγγλία"], 1, "ανακάτεψε σκόνη γραφίτη με πηλό και το έψησε"),
  Q("Πόσο βέβαιη είναι η ιστορία για τα κίτρινα μολύβια, σύμφωνα με τον παρουσιαστή;", ["Απολύτως βέβαιη", "Δεν είναι απολύτως επιβεβαιωμένη", "Είναι σίγουρα ψέμα", "Δεν αναφέρει τίποτα σχετικό"], 1, "Η ιστορία δεν είναι απολύτως επιβεβαιωμένη"),
 ],
 "gloss": {"μόλυβδος": "μόλυβδος — lead (metal)", "παρεξήγηση": "παρεξήγηση — misunderstanding", "κοίτασμα": "κοίτασμα — deposit", "γραφίτης": "γραφίτης — graphite", "ραβδάκια": "ραβδάκι — little stick", "ορυχείο": "ορυχείο — mine", "πηλό": "πηλός — clay", "αναλογία": "αναλογία — proportion, ratio", "κατά τεκμήριο": "κατά τεκμήριο — by default, presumptively"},
})
ITEMS.append({
 "id": "l207-c1-int-medicanes", "title": "Μεσογειακοί κυκλώνες: οι «τυφώνες» της Μεσογείου", "title_en": "Medicanes: the Mediterranean's 'hurricanes'", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με μια μετεωρολόγο σε μια εκπομπή για το κλίμα.",
 "script": [
  L("Δημοσιογράφος", "m", "Τα τελευταία χρόνια ακούμε όλο και συχνότερα για «μεσογειακούς κυκλώνες». Τι ακριβώς είναι;", "In recent years we've been hearing more and more about 'Mediterranean cyclones'. What exactly are they?"),
  L("Μετεωρολόγος", "f", "Είναι συστήματα χαμηλών πιέσεων που, σε ορισμένα στάδια, αποκτούν χαρακτηριστικά τροπικού κυκλώνα: ένα «μάτι» στο κέντρο, ισχυρούς ανέμους γύρω του και καταρρακτώδεις βροχές. Είναι όμως πολύ μικρότεροι και συνήθως λιγότερο ισχυροί από τους τυφώνες του Ατλαντικού. Σχηματίζονται κυρίως το φθινόπωρο, όταν η θάλασσα είναι ακόμα ζεστή από το καλοκαίρι και φτάνει ψυχρός αέρας από τον βορρά.", "They are low-pressure systems which at certain stages acquire features of a tropical cyclone: an 'eye' in the centre, strong winds around it and torrential rain. But they are much smaller and usually less powerful than Atlantic hurricanes. They form mainly in autumn, when the sea is still warm from the summer and cold air arrives from the north."),
  L("Δημοσιογράφος", "m", "Στην Ελλάδα θυμόμαστε τον «Ιανό» και τον «Daniel».", "In Greece we remember 'Ianos' and 'Daniel'."),
  L("Μετεωρολόγος", "f", "Ακριβώς. Ο Daniel, τον Σεπτέμβριο του 2023, έριξε μέσα σε λίγες μέρες στη Θεσσαλία ποσότητες βροχής που αντιστοιχούν σε ολόκληρη χρονιά, και πλημμύρισε τεράστιες εκτάσεις. Λίγες μέρες αργότερα έπληξε τη Λιβύη με τραγικές συνέπειες. Το σημαντικό είναι ότι η καταστροφή δεν οφειλόταν μόνο στον άνεμο, αλλά κυρίως στο νερό.", "Exactly. Daniel, in September 2023, dropped in a few days on Thessaly amounts of rain equal to a whole year and flooded vast areas. A few days later it struck Libya with tragic consequences. What's important is that the destruction was due not only to the wind but mainly to the water."),
  L("Δημοσιογράφος", "m", "Θα γίνονται συχνότεροι λόγω της κλιματικής αλλαγής;", "Will they become more frequent because of climate change?"),
  L("Μετεωρολόγος", "f", "Εδώ πρέπει να είμαστε προσεκτικοί. Οι περισσότερες μελέτες δεν δείχνουν απαραίτητα περισσότερους κυκλώνες, δείχνουν όμως ότι μια θερμότερη θάλασσα δίνει περισσότερη ενέργεια και υγρασία, άρα πιθανώς πιο έντονα φαινόμενα. Για εμάς αυτό σημαίνει ότι η πρόληψη, οι αντιπλημμυρικές υποδομές και τα έγκαιρα μηνύματα προς τους πολίτες γίνονται πιο σημαντικά από ποτέ.", "Here we must be careful. Most studies don't necessarily show more cyclones, but they do show that a warmer sea gives more energy and moisture, and therefore probably more intense events. For us this means that prevention, flood defences and timely warnings to citizens become more important than ever."),
 ],
 "questions": [
  Q("Πώς διαφέρουν οι μεσογειακοί κυκλώνες από τους τυφώνες του Ατλαντικού;", ["Είναι μεγαλύτεροι", "Δεν έχουν ποτέ μάτι", "Είναι πολύ μικρότεροι και συνήθως λιγότερο ισχυροί", "Σχηματίζονται μόνο τον χειμώνα"], 2, "Είναι όμως πολύ μικρότεροι και συνήθως λιγότερο ισχυροί"),
  Q("Πότε σχηματίζονται κυρίως;", ["Την άνοιξη, όταν λιώνουν τα χιόνια", "Το φθινόπωρο, όταν η θάλασσα είναι ζεστή και φτάνει ψυχρός αέρας", "Στο κατακαλόκαιρο", "Μόνο τον Ιανουάριο"], 1, "κυρίως το φθινόπωρο, όταν η θάλασσα είναι ακόμα ζεστή"),
  Q("Σε τι οφειλόταν κυρίως η καταστροφή από τον Daniel;", ["Στον άνεμο", "Στο νερό", "Στο χαλάζι", "Στις πυρκαγιές"], 1, "η καταστροφή δεν οφειλόταν μόνο στον άνεμο, αλλά κυρίως στο νερό"),
  Q("Τι δείχνουν οι περισσότερες μελέτες για το μέλλον, σύμφωνα με τη μετεωρολόγο;", ["Σίγουρα πολύ περισσότερους κυκλώνες", "Ότι θα σταματήσουν", "Όχι απαραίτητα περισσότερους, αλλά πιθανώς πιο έντονους", "Ότι θα μετακινηθούν στον Ατλαντικό"], 2, "δεν δείχνουν απαραίτητα περισσότερους κυκλώνες ... πιθανώς πιο έντονα φαινόμενα"),
 ],
 "gloss": {"χαμηλών πιέσεων": "χαμηλή πίεση — low pressure", "καταρρακτώδεις": "καταρρακτώδης — torrential", "τυφώνες": "τυφώνας — hurricane, typhoon", "ψυχρός": "ψυχρός — cold", "εκτάσεις": "έκταση — area, expanse", "έπληξε": "πλήττω — to strike, hit", "αντιπλημμυρικές": "αντιπλημμυρικός — flood-prevention", "υποδομές": "υποδομή — infrastructure", "έγκαιρα": "έγκαιρος — timely"},
})
rnd = random.Random(207)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-207.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
