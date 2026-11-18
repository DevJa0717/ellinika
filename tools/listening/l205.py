# Source for library/listening/listening-205.json: five more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l205.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l205-news-galazios-karcharias", "title": "Ένας γαλάζιος καρχαρίας στο λιμάνι", "title_en": "A blue shark in the harbour", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα τοπικό δελτίο ειδήσεων σε έναν παραθαλάσσιο σταθμό.",
 "script": [
  L("Εκφωνητής", "m", "Ασυνήθιστος επισκέπτης εμφανίστηκε χθες το πρωί στο λιμάνι της πόλης μας. Ψαράδες που έδεναν τις βάρκες τους είδαν έναν γαλάζιο καρχαρία, μήκους περίπου δύο μέτρων, να κολυμπά αργά ανάμεσα στα σκάφη. Το βίντεο που τράβηξε ένας από αυτούς έκανε τον γύρο των κοινωνικών δικτύων μέσα σε λίγες ώρες.", "An unusual visitor appeared yesterday morning in our town's harbour. Fishermen tying up their boats saw a blue shark, about two metres long, swimming slowly among the vessels. The video one of them took went round social media within a few hours."),
  L("Εκφωνητής", "m", "Θαλάσσιος βιολόγος με τον οποίο μιλήσαμε εξήγησε ότι ο γαλάζιος καρχαρίας ζει κανονικά στα ανοιχτά και πλησιάζει τις ακτές σπάνια, συνήθως όταν είναι άρρωστος ή αποπροσανατολισμένος. Επιθέσεις σε ανθρώπους είναι εξαιρετικά σπάνιες. Αντίθετα, ο ίδιος ο καρχαρίας κινδυνεύει: στη Μεσόγειο οι πληθυσμοί του έχουν μειωθεί δραματικά, κυρίως επειδή πιάνεται κατά λάθος στα δίχτυα και στα παραγάδια.", "A marine biologist we spoke to explained that the blue shark normally lives in open water and rarely approaches the coast, usually when it is sick or disoriented. Attacks on people are extremely rare. On the contrary, the shark itself is in danger: in the Mediterranean its populations have fallen dramatically, mainly because it is caught by accident in nets and longlines."),
  L("Εκφωνητής", "m", "Το λιμενικό ζητά από τους πολίτες να μην πλησιάζουν το ζώο με βάρκες και να μην προσπαθήσουν να το ταΐσουν. Μέχρι το απόγευμα ο καρχαρίας είχε απομακρυνθεί προς τα ανοιχτά.", "The coastguard asks citizens not to approach the animal in boats and not to try to feed it. By the afternoon the shark had moved away towards open water."),
 ],
 "questions": [
  Q("Ποιοι είδαν πρώτοι τον καρχαρία;", ["Λουόμενοι σε μια παραλία", "Ψαράδες που έδεναν τις βάρκες τους", "Το λιμενικό", "Ένας θαλάσσιος βιολόγος"], 1, "Ψαράδες που έδεναν τις βάρκες τους είδαν έναν γαλάζιο καρχαρία"),
  Q("Πότε πλησιάζει συνήθως τις ακτές ο γαλάζιος καρχαρίας, σύμφωνα με τον βιολόγο;", ["Όταν ψάχνει τροφή κοντά στους ανθρώπους", "Το καλοκαίρι", "Όταν είναι άρρωστος ή αποπροσανατολισμένος", "Όταν γεννά"], 2, "συνήθως όταν είναι άρρωστος ή αποπροσανατολισμένος"),
  Q("Γιατί έχουν μειωθεί οι πληθυσμοί του στη Μεσόγειο;", ["Λόγω της ζέστης", "Γιατί πιάνεται κατά λάθος στα δίχτυα και στα παραγάδια", "Γιατί δεν βρίσκει τροφή", "Λόγω του τουρισμού"], 1, "επειδή πιάνεται κατά λάθος στα δίχτυα και στα παραγάδια"),
  Q("Τι ζητά το λιμενικό από τους πολίτες;", ["Να καλούν αμέσως την αστυνομία", "Να μην κολυμπούν στο λιμάνι για μια εβδομάδα", "Να μην πλησιάζουν το ζώο με βάρκες και να μην το ταΐζουν", "Να τραβούν βίντεο"], 2, "να μην πλησιάζουν το ζώο με βάρκες και να μην προσπαθήσουν να το ταΐσουν"),
 ],
 "gloss": {"καρχαρία": "καρχαρίας — shark", "έκανε τον γύρο": "κάνω τον γύρο — to go round, spread widely", "στα ανοιχτά": "στα ανοιχτά — in open water, offshore", "αποπροσανατολισμένος": "αποπροσανατολισμένος — disoriented", "παραγάδια": "παραγάδι — longline (fishing)", "λιμενικό": "λιμενικό — coastguard", "απομακρυνθεί": "απομακρύνομαι — to move away"},
})
ITEMS.append({
 "id": "l205-dia-syndromes", "title": "Πόσες συνδρομές πληρώνουμε;", "title_en": "How many subscriptions are we paying for?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι κοιτάζει τον λογαριασμό της κάρτας του.",
 "script": [
  L("Ειρήνη", "f", "Κάθισα χθες και μέτρησα όλες τις συνδρομές μας. Δύο πλατφόρμες για ταινίες, μία για μουσική, αποθηκευτικός χώρος στο διαδίκτυο, η εφαρμογή για τα ισπανικά σου και το γυμναστήριο. Σύνολο: ογδόντα επτά ευρώ τον μήνα.", "I sat down yesterday and counted all our subscriptions. Two film platforms, one for music, online storage, the app for your Spanish and the gym. Total: eighty-seven euros a month."),
  L("Άρης", "m", "Ογδόντα επτά; Αποκλείεται. Όλα είναι πέντε, έξι ευρώ το καθένα.", "Eighty-seven? No way. They're all five or six euros each."),
  L("Ειρήνη", "f", "Ακριβώς έτσι σε παγιδεύουν. Το γυμναστήριο μόνο είναι τριάντα πέντε, και τελευταία φορά πήγαμε τον Μάρτιο. Και τα ισπανικά τα άνοιξες ξανά πότε;", "That's exactly how they trap you. The gym alone is thirty-five, and the last time we went was in March. And when did you last open the Spanish?"),
  L("Άρης", "m", "Εντάξει, το γυμναστήριο να το κόψουμε, να τρέχουμε στο πάρκο. Τα ισπανικά όμως θα τα ξαναρχίσω, το υπόσχομαι. Για τις ταινίες τι λες;", "OK, let's cancel the gym and run in the park. But I'll start the Spanish again, I promise. What do you say about the films?"),
  L("Ειρήνη", "f", "Λέω να κρατάμε μόνο μία πλατφόρμα κάθε φορά. Έναν μήνα τη μία, όταν βγει κάποια σειρά που θέλουμε, και τον άλλον μήνα την άλλη. Έτσι γλιτώνουμε σχεδόν πενήντα ευρώ τον μήνα, χωρίς να στερηθούμε τίποτα.", "I say we keep just one platform at a time. One month the one, when a series we want comes out, and the next month the other. That way we save almost fifty euros a month without missing out on anything."),
 ],
 "questions": [
  Q("Πόσο πληρώνει το ζευγάρι συνολικά τον μήνα;", ["Πενήντα ευρώ", "Τριάντα πέντε ευρώ", "Ογδόντα επτά ευρώ", "Πέντε με έξι ευρώ"], 2, "Σύνολο: ογδόντα επτά ευρώ τον μήνα"),
  Q("Γιατί η Ειρήνη θέλει να κόψουν το γυμναστήριο;", ["Γιατί έκλεισε", "Γιατί είναι το φθηνότερο", "Γιατί είναι ακριβό και δεν έχουν πάει από τον Μάρτιο", "Γιατί ο Άρης χτύπησε"], 2, "Το γυμναστήριο μόνο είναι τριάντα πέντε, και τελευταία φορά πήγαμε τον Μάρτιο"),
  Q("Τι θέλει να κρατήσει ο Άρης;", ["Την εφαρμογή για τα ισπανικά", "Το γυμναστήριο", "Και τις δύο πλατφόρμες", "Τον αποθηκευτικό χώρο"], 0, "Τα ισπανικά όμως θα τα ξαναρχίσω, το υπόσχομαι"),
  Q("Τι προτείνει η Ειρήνη για τις πλατφόρμες με ταινίες;", ["Να τις κόψουν και τις δύο", "Να κρατούν μία κάθε μήνα και να αλλάζουν", "Να τις μοιραστούν με φίλους", "Να πάρουν μια τρίτη, φθηνότερη"], 1, "να κρατάμε μόνο μία πλατφόρμα κάθε φορά"),
 ],
 "gloss": {"συνδρομές": "συνδρομή — subscription", "πλατφόρμες": "πλατφόρμα — (streaming) platform", "αποθηκευτικός χώρος": "αποθηκευτικός χώρος — storage space", "Αποκλείεται": "αποκλείεται — no way, it's impossible", "παγιδεύουν": "παγιδεύω — to trap", "γλιτώνουμε": "γλιτώνω — to save (money); to escape", "στερηθούμε": "στερούμαι — to go without, miss out on"},
})
ITEMS.append({
 "id": "l205-vm-elaiochromatistis", "title": "Μήνυμα από τον ελαιοχρωματιστή", "title_en": "A message from the house painter", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον ελαιοχρωματιστή που θα βάψει την πρόσοψη του σπιτιού σας.",
 "script": [
  L("Θανάσης", "m", "Καλησπέρα, κυρία Λαμπροπούλου, ο Θανάσης είμαι, για το βάψιμο της πρόσοψης. Είδα το δελτίο καιρού και για την Πέμπτη και την Παρασκευή δίνει βροχές. Η μπογιά θέλει τουλάχιστον δύο στεγνές μέρες για να πιάσει, οπότε λέω να ξεκινήσουμε τη Δευτέρα αντί για την Τετάρτη.", "Good evening, Mrs Lambropoulou, it's Thanasis, about painting the front of the house. I saw the weather forecast and it says rain on Thursday and Friday. The paint needs at least two dry days to take, so I suggest we start on Monday instead of Wednesday."),
  L("Θανάσης", "m", "Δεύτερον, πρέπει να μου πείτε ποιο λευκό θέλετε. Σας άφησα στο γραμματοκιβώτιο δύο δείγματα: το καθαρό λευκό και ένα υπόλευκο, λίγο πιο ζεστό. Στον ήλιο το καθαρό λευκό κουράζει λίγο το μάτι, αλλά η απόφαση είναι δική σας.", "Secondly, you need to tell me which white you want. I left two samples in your letterbox: pure white and an off-white, a little warmer. In the sun pure white is a bit tiring on the eye, but it's your decision."),
  L("Θανάσης", "m", "Και κάτι τελευταίο: αν μπορείτε, μέχρι την Κυριακή μαζέψτε τις γλάστρες από το μπαλκόνι. Το κλιματιστικό θα το σκεπάσω εγώ με νάιλον. Πάρτε με όταν μπορέσετε. Γεια σας.", "And one last thing: if you can, by Sunday move the flowerpots off the balcony. I'll cover the air conditioner with plastic myself. Call me when you can. Goodbye."),
 ],
 "questions": [
  Q("Γιατί θέλει ο Θανάσης να αλλάξει την ημέρα έναρξης;", ["Γιατί είναι άρρωστος", "Γιατί η πρόβλεψη δίνει βροχές και η μπογιά θέλει δύο στεγνές μέρες", "Γιατί δεν έχει έρθει η μπογιά", "Γιατί έχει άλλη δουλειά την Τετάρτη"], 1, "για την Πέμπτη και την Παρασκευή δίνει βροχές. Η μπογιά θέλει τουλάχιστον δύο στεγνές μέρες"),
  Q("Πού άφησε τα δείγματα χρώματος;", ["Στο μπαλκόνι", "Στον γείτονα", "Στο γραμματοκιβώτιο", "Στο κατάστημα με τα χρώματα"], 2, "Σας άφησα στο γραμματοκιβώτιο δύο δείγματα"),
  Q("Τι λέει για το καθαρό λευκό;", ["Ότι είναι ακριβότερο", "Ότι στον ήλιο κουράζει λίγο το μάτι", "Ότι λερώνεται εύκολα", "Ότι δεν κρατάει πολύ"], 1, "Στον ήλιο το καθαρό λευκό κουράζει λίγο το μάτι"),
  Q("Τι πρέπει να κάνει η κυρία Λαμπροπούλου μέχρι την Κυριακή;", ["Να σκεπάσει το κλιματιστικό", "Να αγοράσει τη μπογιά", "Να μαζέψει τις γλάστρες από το μπαλκόνι", "Να πληρώσει προκαταβολή"], 2, "μέχρι την Κυριακή μαζέψτε τις γλάστρες από το μπαλκόνι"),
 ],
 "gloss": {"ελαιοχρωματιστή": "ελαιοχρωματιστής — house painter", "πρόσοψης": "πρόσοψη — front, façade", "να πιάσει": "πιάνω (για μπογιά) — to take, adhere", "δείγματα": "δείγμα — sample", "γραμματοκιβώτιο": "γραμματοκιβώτιο — letterbox", "υπόλευκο": "υπόλευκος — off-white", "γλάστρες": "γλάστρα — flowerpot", "νάιλον": "νάιλον — plastic sheeting"},
})
ITEMS.append({
 "id": "l205-c1-mono-teflon", "title": "Πώς ένα «άδειο» μπουκάλι αερίου έδωσε το αντικολλητικό τηγάνι", "title_en": "How an 'empty' gas cylinder gave us the non-stick pan", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για τις τυχαίες ανακαλύψεις: την ιστορία του αντικολλητικού τηγανιού.",
 "script": [
  L("Παρουσιάστρια", "f", "Το 1938 ένας νεαρός χημικός της αμερικανικής εταιρείας DuPont, ο Ρόι Πλάνκετ, πειραματιζόταν με αέρια για ψυγεία. Ένα πρωί άνοιξε τη βαλβίδα μιας φιάλης που, σύμφωνα με το βάρος της, έπρεπε να είναι γεμάτη· όμως δεν βγήκε τίποτα. Αντί να την πετάξει, την έκοψε στα δύο. Μέσα βρήκε μια λευκή, γλιστερή σκόνη: το αέριο είχε πολυμεριστεί από μόνο του.", "In 1938 a young chemist at the American company DuPont, Roy Plunkett, was experimenting with gases for refrigerators. One morning he opened the valve of a cylinder which, judging by its weight, should have been full; but nothing came out. Instead of throwing it away, he cut it in two. Inside he found a white, slippery powder: the gas had polymerised by itself."),
  L("Παρουσιάστρια", "f", "Το νέο υλικό είχε σχεδόν απίστευτες ιδιότητες: δεν αντιδρούσε σχεδόν με καμία χημική ουσία και τίποτα δεν κολλούσε πάνω του. Οι πρώτες του χρήσεις δεν είχαν καμία σχέση με την κουζίνα· χρησιμοποιήθηκε, για παράδειγμα, σε στεγανωτικά υλικά στο αμερικανικό πρόγραμμα της ατομικής βόμβας, επειδή άντεχε σε εξαιρετικά διαβρωτικές ουσίες.", "The new material had almost incredible properties: it hardly reacted with any chemical and nothing stuck to it. Its first uses had nothing to do with the kitchen; it was used, for example, in seals in the American atomic bomb programme, because it withstood extremely corrosive substances."),
  L("Παρουσιάστρια", "f", "Στο τηγάνι το έφερε, λέγεται, μια γυναίκα. Στα μέσα της δεκαετίας του 1950 ο Γάλλος μηχανικός Μαρκ Γκρεγκουάρ έβαζε το υλικό στις πετονιές του για να μην μπερδεύονται. Η σύζυγός του, η Κολέτ, τού πρότεινε να δοκιμάσει το ίδιο στις κατσαρόλες της. Έτσι γεννήθηκε το 1956 η εταιρεία Tefal. Σήμερα οι ειδικοί συμβουλεύουν μόνο να μη ζεσταίνουμε το άδειο τηγάνι σε πολύ υψηλές θερμοκρασίες, γιατί η επίστρωση μπορεί να αρχίσει να διασπάται.", "It was brought to the frying pan, so the story goes, by a woman. In the mid-1950s the French engineer Marc Grégoire was putting the material on his fishing lines so they wouldn't tangle. His wife, Colette, suggested he try the same on her saucepans. That is how the company Tefal was born in 1956. Today experts only advise us not to heat an empty pan to very high temperatures, because the coating can begin to break down."),
 ],
 "questions": [
  Q("Τι παράξενο παρατήρησε ο Πλάνκετ στη φιάλη;", ["Ότι ήταν πολύ ζεστή", "Ότι, ενώ φαινόταν γεμάτη από το βάρος, δεν έβγαινε αέριο", "Ότι είχε σκουριάσει", "Ότι μύριζε παράξενα"], 1, "σύμφωνα με το βάρος της, έπρεπε να είναι γεμάτη· όμως δεν βγήκε τίποτα"),
  Q("Ποιες ήταν οι βασικές ιδιότητες του νέου υλικού;", ["Ήταν πολύ σκληρό και διαφανές", "Δεν αντιδρούσε σχεδόν με τίποτα και τίποτα δεν κολλούσε πάνω του", "Ήταν καλός αγωγός του ηλεκτρισμού", "Διαλυόταν στο νερό"], 1, "δεν αντιδρούσε σχεδόν με καμία χημική ουσία και τίποτα δεν κολλούσε πάνω του"),
  Q("Πώς έφτασε το υλικό στις κατσαρόλες, σύμφωνα με την παράδοση;", ["Με διαγωνισμό της DuPont", "Η σύζυγος ενός μηχανικού πρότεινε να το δοκιμάσει στις κατσαρόλες της", "Ένας σεφ το ζήτησε από την εταιρεία", "Μετά από μια ατομική δοκιμή"], 1, "Η σύζυγός του, η Κολέτ, τού πρότεινε να δοκιμάσει το ίδιο στις κατσαρόλες της"),
  Q("Ποια συμβουλή δίνουν σήμερα οι ειδικοί;", ["Να μην πλένουμε το τηγάνι με απορρυπαντικό", "Να μη ζεσταίνουμε το άδειο τηγάνι σε πολύ υψηλές θερμοκρασίες", "Να αλλάζουμε τηγάνι κάθε χρόνο", "Να μη μαγειρεύουμε αυγά"], 1, "να μη ζεσταίνουμε το άδειο τηγάνι σε πολύ υψηλές θερμοκρασίες"),
 ],
 "gloss": {"αντικολλητικού": "αντικολλητικός — non-stick", "βαλβίδα": "βαλβίδα — valve", "φιάλης": "φιάλη — cylinder, bottle", "γλιστερή": "γλιστερός — slippery", "πολυμεριστεί": "πολυμερίζομαι — to polymerise", "στεγανωτικά": "στεγανωτικός — sealing", "διαβρωτικές": "διαβρωτικός — corrosive", "πετονιές": "πετονιά — fishing line", "επίστρωση": "επίστρωση — coating", "διασπάται": "διασπώμαι — to break down, decompose"},
})
ITEMS.append({
 "id": "l205-c1-int-alexikeravno", "title": "Το αλεξικέραυνο και το κλουβί του Φαραντέι", "title_en": "The lightning rod and the Faraday cage", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με μια φυσικό σε μια εκπομπή για την επιστήμη της καθημερινής ζωής.",
 "script": [
  L("Δημοσιογράφος", "m", "Πολλοί πιστεύουν ότι το αλεξικέραυνο «τραβάει» τους κεραυνούς. Ισχύει;", "Many people believe that the lightning rod 'attracts' lightning. Is that true?"),
  L("Φυσικός", "f", "Όχι ακριβώς. Ο κεραυνός θα πέσει έτσι κι αλλιώς σε κάποιο ψηλό σημείο. Το αλεξικέραυνο απλώς του προσφέρει έναν ασφαλή δρόμο: μια μεταλλική ράβδο στην κορυφή, συνδεδεμένη με ένα χοντρό καλώδιο που καταλήγει βαθιά στο έδαφος. Έτσι το ρεύμα περνάει έξω από τους τοίχους, αντί να διασχίσει το κτίριο και να προκαλέσει φωτιά. Η ιδέα είναι του Βενιαμίν Φραγκλίνου, στα μέσα του 18ου αιώνα. Στην αρχή πολλοί αντέδρασαν, γιατί θεωρούσαν ασέβεια να εμποδίζει κανείς αυτό που έμοιαζε με θεϊκή τιμωρία.", "Not exactly. Lightning will strike some high point anyway. The lightning rod simply offers it a safe path: a metal rod at the top, connected to a thick cable that ends deep in the ground. That way the current passes outside the walls instead of crossing the building and starting a fire. The idea is Benjamin Franklin's, in the mid-18th century. At first many objected, because they considered it irreverent to block what looked like divine punishment."),
  L("Δημοσιογράφος", "m", "Και στο αυτοκίνητο είμαστε ασφαλείς χάρη στα λάστιχα, σωστά;", "And in the car we're safe thanks to the tyres, right?"),
  L("Φυσικός", "f", "Αυτός είναι ο πιο διαδεδομένος μύθος. Ένας κεραυνός έχει διανύσει χιλιόμετρα μέσα στον αέρα· λίγα εκατοστά λάστιχο δεν τον σταματούν. Μας προστατεύει το μεταλλικό αμάξωμα: το ρεύμα κυλά στην εξωτερική επιφάνεια και περνά στο έδαφος, ενώ το εσωτερικό μένει σχεδόν ανέγγιχτο. Είναι αυτό που ονομάζουμε κλουβί του Φαραντέι. Γι' αυτό ένα αυτοκίνητο με υφασμάτινη οροφή δεν προσφέρει την ίδια προστασία, και γι' αυτό καλό είναι, μέσα στην καταιγίδα, να μην ακουμπάμε τα μεταλλικά μέρη της καμπίνας.", "That is the most widespread myth. A lightning bolt has travelled kilometres through the air; a few centimetres of rubber won't stop it. What protects us is the metal body: the current flows over the outer surface and passes into the ground, while the inside remains almost untouched. That's what we call a Faraday cage. That's why a car with a fabric roof doesn't offer the same protection, and why during a storm it's best not to touch the metal parts of the cabin."),
 ],
 "questions": [
  Q("Τι κάνει στην πραγματικότητα το αλεξικέραυνο, σύμφωνα με τη φυσικό;", ["Τραβάει κεραυνούς από χιλιόμετρα μακριά", "Προσφέρει στον κεραυνό έναν ασφαλή δρόμο προς το έδαφος", "Εμποδίζει τη δημιουργία καταιγίδων", "Αποθηκεύει την ενέργεια του κεραυνού"], 1, "Το αλεξικέραυνο απλώς του προσφέρει έναν ασφαλή δρόμο"),
  Q("Γιατί αντέδρασαν αρχικά πολλοί στην ιδέα του Φραγκλίνου;", ["Γιατί ήταν πολύ ακριβή", "Γιατί θεωρούσαν ασέβεια να εμποδίζεται κάτι που έμοιαζε με θεϊκή τιμωρία", "Γιατί χαλούσε την εμφάνιση των εκκλησιών", "Γιατί δεν είχε δοκιμαστεί"], 1, "θεωρούσαν ασέβεια να εμποδίζει κανείς αυτό που έμοιαζε με θεϊκή τιμωρία"),
  Q("Γιατί είμαστε ασφαλείς μέσα σε ένα αυτοκίνητο με μεταλλική οροφή;", ["Γιατί τα λάστιχα μονώνουν", "Γιατί το ρεύμα κυλά στο εξωτερικό αμάξωμα και περνά στο έδαφος", "Γιατί οι κεραυνοί δεν πέφτουν σε κινούμενα οχήματα", "Γιατί τα τζάμια σταματούν το ρεύμα"], 1, "το ρεύμα κυλά στην εξωτερική επιφάνεια και περνά στο έδαφος"),
  Q("Τι συμβουλεύει η φυσικός για όσους βρίσκονται στο αυτοκίνητο μέσα σε καταιγίδα;", ["Να βγουν αμέσως έξω", "Να ανοίξουν τα παράθυρα", "Να μην ακουμπούν τα μεταλλικά μέρη της καμπίνας", "Να σβήσουν τη μηχανή και τα φώτα"], 2, "να μην ακουμπάμε τα μεταλλικά μέρη της καμπίνας"),
 ],
 "gloss": {"αλεξικέραυνο": "αλεξικέραυνο — lightning rod", "κεραυνός": "κεραυνός — lightning bolt", "ράβδο": "ράβδος — rod", "διασχίσει": "διασχίζω — to cross", "ασέβεια": "ασέβεια — irreverence, impiety", "διανύσει": "διανύω — to travel, cover (a distance)", "αμάξωμα": "αμάξωμα — car body", "ανέγγιχτο": "ανέγγιχτος — untouched", "υφασμάτινη": "υφασμάτινος — fabric, cloth"},
})
rnd = random.Random(205)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-205.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
