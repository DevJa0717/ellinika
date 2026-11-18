# Source for library/listening/listening-190.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l190.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l190-ann-xenagisi-sto-katafygio", "title": "Ξενάγηση στο καταφύγιο κάτω από την πλατεία", "title_en": "A tour of the shelter under the square", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στον τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνητής", "m", "Για πρώτη φορά μετά από ογδόντα χρόνια, ο δήμος ανοίγει στο κοινό το αντιαεροπορικό καταφύγιο που βρίσκεται κάτω από την κεντρική πλατεία. Το καταφύγιο χτίστηκε το 1939 και κατά τη διάρκεια του πολέμου έκρυβε εκατοντάδες κατοίκους κάθε φορά που ακούγονταν οι σειρήνες.", "For the first time in eighty years, the municipality is opening to the public the air-raid shelter beneath the central square. The shelter was built in 1939 and during the war it hid hundreds of residents every time the sirens sounded."),
  L("Εκφωνητής", "m", "Οι ξεναγήσεις θα γίνονται κάθε Σάββατο και Κυριακή στις έντεκα και στις μία, σε ομάδες των δεκαπέντε ατόμων, και θα διαρκούν σαράντα πέντε λεπτά. Στους διαδρόμους θα δείτε τα πρωτότυπα παγκάκια, τις οδηγίες γραμμένες με μπογιά στους τοίχους και φωτογραφίες από το αρχείο του δήμου.", "Tours will take place every Saturday and Sunday at eleven and at one, in groups of fifteen, and will last forty-five minutes. In the corridors you will see the original benches, the instructions painted on the walls and photographs from the municipal archive."),
  L("Εκφωνητής", "m", "Η είσοδος είναι δωρεάν, αλλά χρειάζεται κράτηση στο κέντρο εξυπηρέτησης πολιτών. Επειδή η σκάλα είναι στενή και απότομη, το καταφύγιο δεν είναι δυστυχώς προσβάσιμο σε αμαξίδια, και δεν συνιστάται σε όσους υποφέρουν από κλειστοφοβία. Η θερμοκρασία μέσα είναι δεκατέσσερις βαθμοί όλο τον χρόνο.", "Entry is free, but booking is needed at the citizens' service centre. Because the staircase is narrow and steep, the shelter is unfortunately not accessible to wheelchairs, and it is not recommended for people who suffer from claustrophobia. The temperature inside is fourteen degrees all year round."),
 ],
 "questions": [
  Q("Πότε χρησιμοποιούσαν οι κάτοικοι το καταφύγιο;", ["Όταν ακούγονταν οι σειρήνες στον πόλεμο", "Κατά τη διάρκεια σεισμών", "Όταν πλημμύριζε η πλατεία", "Τις πολύ ζεστές μέρες του καλοκαιριού"], 0, "κάθε φορά που ακούγονταν οι σειρήνες"),
  Q("Τι θα δουν οι επισκέπτες στους διαδρόμους;", ["Ένα ντοκιμαντέρ για τον πόλεμο", "Όπλα και στολές στρατιωτών", "Τα πρωτότυπα παγκάκια και οδηγίες στους τοίχους", "Μια έκθεση ζωγραφικής"], 2, "θα δείτε τα πρωτότυπα παγκάκια, τις οδηγίες γραμμένες με μπογιά στους τοίχους"),
  Q("Γιατί το καταφύγιο δεν είναι προσβάσιμο σε αμαξίδια;", ["Γιατί δεν υπάρχει ρεύμα", "Γιατί η σκάλα είναι στενή και απότομη", "Γιατί οι διάδρομοι έχουν νερό", "Γιατί δεν έχει έξοδο κινδύνου"], 1, "Επειδή η σκάλα είναι στενή και απότομη"),
 ],
 "gloss": {"αντιαεροπορικό": "αντιαεροπορικός — anti-aircraft; αντιαεροπορικό καταφύγιο = air-raid shelter", "σειρήνες": "σειρήνα — siren", "μπογιά": "μπογιά — paint", "αμαξίδια": "αμαξίδιο — wheelchair", "κλειστοφοβία": "κλειστοφοβία — claustrophobia", "απότομη": "απότομος — steep"},
})

ITEMS.append({
 "id": "l190-int-organistria-sti-syro", "title": "Η οργανίστρια του καθολικού ναού", "title_en": "The organist of the Catholic church", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με την οργανίστρια ενός καθολικού ναού στη Σύρο.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι περισσότεροι Έλληνες δεν έχουν ακούσει ποτέ από κοντά εκκλησιαστικό όργανο. Πώς βρεθήκατε εσείς να παίζετε;", "Most Greeks have never heard a church organ up close. How did you come to play one?"),
  L("Οργανίστρια", "f", "Στη Σύρο υπάρχει μεγάλη καθολική κοινότητα εδώ και αιώνες, και στους ναούς της το όργανο συνοδεύει τη λειτουργία, όπως στους ορθόδοξους ναούς οι ψάλτες. Η γιαγιά μου έπαιζε στον ίδιο ναό. Εγώ ξεκίνησα από το πιάνο και στα δεκαπέντε μου ανέβηκα για πρώτη φορά στο πατάρι όπου βρίσκεται το όργανο.", "On Syros there has been a large Catholic community for centuries, and in its churches the organ accompanies the mass, just as cantors do in Orthodox churches. My grandmother played in the same church. I started on the piano, and at fifteen I climbed up to the gallery where the organ is for the first time."),
  L("Δημοσιογράφος", "m", "Είναι πολύ διαφορετικό από το πιάνο;", "Is it very different from the piano?"),
  L("Οργανίστρια", "f", "Εντελώς. Έχει δύο πληκτρολόγια για τα χέρια και ένα με πεντάλ για τα πόδια, οπότε παίζεις κυριολεκτικά με όλο σου το σώμα. Και ο ήχος δεν σβήνει όπως στο πιάνο: όσο κρατάς το πλήκτρο, ο αέρας περνάει από τους αυλούς και η νότα συνεχίζει. Επίσης ο ήχος φτάνει στον κόσμο λίγο αργότερα, γιατί ο ναός είναι μεγάλος, και πρέπει να μάθεις να μην περιμένεις να τον ακούσεις.", "Completely. It has two keyboards for the hands and one with pedals for the feet, so you literally play with your whole body. And the sound doesn't die away as on the piano: as long as you hold the key, the air passes through the pipes and the note continues. The sound also reaches the congregation a little later, because the church is big, and you have to learn not to wait to hear it."),
  L("Δημοσιογράφος", "m", "Χρειάζεται συντήρηση;", "Does it need maintenance?"),
  L("Οργανίστρια", "f", "Πολλή. Η υγρασία του νησιού είναι εχθρός για το δέρμα και το ξύλο. Δυστυχώς στην Ελλάδα δεν υπάρχουν σχεδόν καθόλου ειδικοί, οπότε κάθε λίγα χρόνια έρχεται ένας τεχνίτης από την Ιταλία. Τον περιμένουμε σαν γιατρό.", "A lot. The island's humidity is an enemy of the leather and the wood. Unfortunately in Greece there are hardly any specialists, so every few years a craftsman comes from Italy. We wait for him like a doctor."),
 ],
 "questions": [
  Q("Τι ρόλο έχει το όργανο στους καθολικούς ναούς της Σύρου;", ["Παίζει μόνο σε συναυλίες", "Συνοδεύει τη λειτουργία, όπως οι ψάλτες στους ορθόδοξους ναούς", "Χρησιμοποιείται μόνο στους γάμους", "Παίζει μόνο τα Χριστούγεννα"], 1, "το όργανο συνοδεύει τη λειτουργία, όπως στους ορθόδοξους ναούς οι ψάλτες"),
  Q("Γιατί πρέπει η οργανίστρια να μάθει να μην περιμένει να ακούσει τον ήχο;", ["Γιατί το όργανο είναι χαλασμένο", "Γιατί φοράει ωτοασπίδες", "Γιατί ο ήχος φτάνει λίγο αργότερα στον μεγάλο ναό", "Γιατί παίζει πολύ σιγά"], 2, "ο ήχος φτάνει στον κόσμο λίγο αργότερα, γιατί ο ναός είναι μεγάλος"),
  Q("Ποιος συντηρεί το όργανο;", ["Η ίδια η οργανίστρια", "Ένας τεχνίτης που έρχεται από την Ιταλία", "Ένας ξυλουργός του νησιού", "Οι ιερείς του ναού"], 1, "κάθε λίγα χρόνια έρχεται ένας τεχνίτης από την Ιταλία"),
 ],
 "gloss": {"οργανίστρια": "οργανίστρια — (female) organist", "ψάλτες": "ψάλτης — cantor (Orthodox church singer)", "πατάρι": "πατάρι — gallery, loft", "πληκτρολόγια": "πληκτρολόγιο — keyboard, manual", "αυλούς": "αυλός — pipe (of an organ)", "υγρασία": "υγρασία — humidity, damp"},
})

ITEMS.append({
 "id": "l190-vm-ntamitzanes-apo-to-oinopoieio", "title": "Οι νταμιτζάνες σας είναι έτοιμες", "title_en": "Your demijohns are ready", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε παραγγείλει κρασί από ένα μικρό οινοποιείο για μια γιορτή. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Οινοποιός", "m", "Γεια σας, ο Μανώλης από το οινοποιείο είμαι, για την παραγγελία σας για τη γιορτή του Σαββάτου. Οι δύο νταμιτζάνες με το λευκό είναι έτοιμες. Για το κόκκινο όμως έχουμε ένα θεματάκι: η φετινή σοδειά δεν έχει ωριμάσει ακόμα, και δεν θέλω να σας δώσω κρασί που δεν είναι έτοιμο.", "Hello, it's Manolis from the winery, about your order for Saturday's party. The two demijohns of white are ready. For the red, though, we have a little problem: this year's vintage hasn't matured yet, and I don't want to give you wine that isn't ready."),
  L("Οινοποιός", "m", "Μπορώ να σας δώσω από το περσινό κόκκινο, που είναι πιο σκούρο και πιο βαρύ, στην ίδια τιμή. Ταιριάζει πολύ με κρέας στα κάρβουνα, αν έχετε ψητά. Αν πάλι προτιμάτε κάτι πιο ελαφρύ, έχω ένα ροζέ που αρέσει πολύ το καλοκαίρι.", "I can give you some of last year's red, which is darker and heavier, at the same price. It goes very well with chargrilled meat, if you're having grills. Or if you prefer something lighter, I have a rosé that people love in summer."),
  L("Οινοποιός", "m", "Να ξέρετε ότι τις νταμιτζάνες τις θέλουμε πίσω, άδειες, μέσα σε έναν μήνα, αλλιώς χρεώνουμε δέκα ευρώ για την καθεμία. Και φέρτε μαζί σας ένα παλιό σεντόνι για το πορτμπαγκάζ, γιατί στις στροφές του δρόμου καμιά φορά χτυπάνε μεταξύ τους.", "Just so you know, we want the demijohns back, empty, within a month, otherwise we charge ten euros for each one. And bring an old sheet with you for the boot, because on the bends in the road they sometimes knock against each other."),
 ],
 "questions": [
  Q("Γιατί δεν είναι διαθέσιμο το φετινό κόκκινο κρασί;", ["Γιατί πουλήθηκε όλο", "Γιατί η σοδειά δεν έχει ωριμάσει ακόμα", "Γιατί χάλασε από τη ζέστη", "Γιατί η τιμή του ανέβηκε"], 1, "η φετινή σοδειά δεν έχει ωριμάσει ακόμα"),
  Q("Με τι ταιριάζει, σύμφωνα με τον οινοποιό, το περσινό κόκκινο;", ["Με ψάρι", "Με γλυκά", "Με κρέας στα κάρβουνα", "Με τυριά"], 2, "Ταιριάζει πολύ με κρέας στα κάρβουνα"),
  Q("Γιατί πρέπει να φέρετε ένα παλιό σεντόνι;", ["Για να μην χτυπάνε μεταξύ τους οι νταμιτζάνες στο πορτμπαγκάζ", "Για να σκεπάσετε το τραπέζι της γιορτής", "Για να μη ζεσταθεί το κρασί", "Για να τυλίξετε τα ποτήρια"], 0, "στις στροφές του δρόμου καμιά φορά χτυπάνε μεταξύ τους"),
 ],
 "gloss": {"νταμιτζάνες": "νταμιτζάνα — demijohn", "οινοποιείο": "οινοποιείο — winery", "σοδειά": "σοδειά — harvest, vintage", "ωριμάσει": "ωριμάζω — to mature, ripen", "κάρβουνα": "κάρβουνο — charcoal; στα κάρβουνα = chargrilled", "πορτμπαγκάζ": "πορτμπαγκάζ — car boot, trunk"},
})

ITEMS.append({
 "id": "l190-mono-sfyrizo-sta-peninta", "title": "Έμαθα να σφυρίζω στα πενήντα", "title_en": "I learned to whistle at fifty", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλάει σε ένα ραδιοφωνικό πρόγραμμα για κάτι που έμαθε πρόσφατα.",
 "script": [
  L("Αντώνης", "m", "Όλη μου τη ζωή ντρεπόμουν που δεν ήξερα να σφυρίζω. Ο πατέρας μου σφύριζε τραγούδια ενώ ξύριζε τα γένια του, η αδερφή μου καλούσε τον σκύλο με ένα σφύριγμα από την άλλη άκρη του χωραφιού, κι εγώ έβγαζα μόνο αέρα. Στο σχολείο με κορόιδευαν, και κάποια στιγμή σταμάτησα να προσπαθώ.", "All my life I was embarrassed that I couldn't whistle. My father whistled songs while he shaved, my sister called the dog with a whistle from the other end of the field, and all I produced was air. At school they teased me, and at some point I stopped trying."),
  L("Αντώνης", "m", "Πέρσι, στα πενήντα μου, η εγγονή μου μού ζήτησε να της μάθω να σφυρίζει. Δεν είχα την καρδιά να της πω ότι δεν ξέρω, οπότε αρχίσαμε να μαθαίνουμε μαζί από βίντεο στο διαδίκτυο. Το μυστικό, απ' ό,τι φαίνεται, είναι η θέση της γλώσσας: την ακουμπάς πίσω από τα κάτω δόντια και φυσάς απαλά, όχι δυνατά.", "Last year, at fifty, my granddaughter asked me to teach her to whistle. I didn't have the heart to tell her I didn't know how, so we started learning together from videos online. The secret, it seems, is the position of the tongue: you rest it behind the lower teeth and blow gently, not hard."),
  L("Αντώνης", "m", "Εκείνη τα κατάφερε σε τρεις μέρες. Εγώ σε τρεις μήνες. Αλλά θυμάμαι ακόμα το πρωί που, ενώ έπλενα τα πιάτα, βγήκε από το στόμα μου μια καθαρή νότα. Φώναξα σαν να είχα κερδίσει το λαχείο. Τώρα σφυρίζω συνέχεια, και η γυναίκα μου λέει ότι προτιμούσε τον παλιό, σιωπηλό Αντώνη.", "She managed it in three days. Me in three months. But I still remember the morning when, as I was washing the dishes, a clear note came out of my mouth. I shouted as if I'd won the lottery. Now I whistle all the time, and my wife says she preferred the old, silent Antonis."),
 ],
 "questions": [
  Q("Γιατί αποφάσισε ο Αντώνης να μάθει να σφυρίζει;", ["Γιατί τον κορόιδευαν στη δουλειά", "Γιατί του το ζήτησε η εγγονή του", "Γιατί ήθελε να καλεί τον σκύλο του", "Γιατί του το πρότεινε ο γιατρός"], 1, "η εγγονή μου μού ζήτησε να της μάθω να σφυρίζει"),
  Q("Ποιο είναι το μυστικό, σύμφωνα με τον Αντώνη;", ["Να φυσάς πολύ δυνατά", "Να κρατάς τα χείλη κλειστά", "Η θέση της γλώσσας πίσω από τα κάτω δόντια", "Να εξασκείσαι πριν από το φαγητό"], 2, "είναι η θέση της γλώσσας: την ακουμπάς πίσω από τα κάτω δόντια"),
  Q("Τι λέει η γυναίκα του σήμερα;", ["Ότι σφυρίζει πολύ ωραία", "Ότι θέλει κι εκείνη να μάθει", "Ότι προτιμούσε τον παλιό, σιωπηλό Αντώνη", "Ότι πρέπει να γραφτεί σε χορωδία"], 2, "η γυναίκα μου λέει ότι προτιμούσε τον παλιό, σιωπηλό Αντώνη"),
 ],
 "gloss": {"σφυρίζω": "σφυρίζω — to whistle", "ξύριζε": "ξυρίζω — to shave", "σφύριγμα": "σφύριγμα — whistle (the sound)", "κορόιδευαν": "κοροϊδεύω — to tease, make fun of", "νότα": "νότα — (musical) note", "σιωπηλό": "σιωπηλός — silent"},
})

ITEMS.append({
 "id": "l190-dia-onoma-gia-ti-varka", "title": "Τι όνομα θα δώσουμε στη βάρκα;", "title_en": "What shall we call the boat?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι μόλις αγόρασε μια μεταχειρισμένη ψαρόβαρκα και συζητά τι όνομα θα της δώσει.",
 "script": [
  L("Στέλιος", "m", "Ο προηγούμενος ιδιοκτήτης την έλεγε «Κική», από το όνομα της πεθεράς του. Δεν θέλω να βγαίνω για ψάρεμα με την πεθερά κάποιου άλλου.", "The previous owner called her 'Kiki', after his mother-in-law. I don't want to go fishing with someone else's mother-in-law."),
  L("Μαρίνα", "f", "Ο θείος μου όμως λέει ότι δεν κάνει να αλλάζεις το όνομα μιας βάρκας. Οι ψαράδες το θεωρούν γρουσουζιά. Λένε ότι η θάλασσα ξέρει τη βάρκα με το πρώτο της όνομα.", "But my uncle says you shouldn't change a boat's name. Fishermen consider it bad luck. They say the sea knows the boat by her first name."),
  L("Στέλιος", "m", "Δεν το πιστεύω αυτό. Και πάντως, απ' ό,τι διάβασα, υπάρχει λύση: κάνεις μια μικρή τελετή, ρίχνεις λίγο κρασί στη θάλασσα και ζητάς συγγνώμη από το παλιό όνομα.", "I don't believe that. And anyway, from what I've read, there's a solution: you hold a little ceremony, pour some wine into the sea and apologise to the old name."),
  L("Μαρίνα", "f", "Εντάξει, αν θα κάνουμε και τελετή, ας είναι ένα όνομα που αξίζει. Τι λες για «Γαλήνη»; Είναι όμορφο και μας εύχεται ήσυχη θάλασσα.", "OK, if we're going to have a ceremony, let it be a name that's worth it. What about 'Galini'? It's beautiful and it wishes us calm seas."),
  L("Στέλιος", "m", "Είναι ωραίο, αλλά στο λιμάνι υπάρχουν ήδη τρεις «Γαλήνες». Όταν θα φωνάζει κάποιος από την προβλήτα, θα γυρίζουν όλοι. Εγώ σκεφτόμουν κάτι πιο δικό μας, όπως «Λιόπετρα», η παραλία όπου γνωριστήκαμε.", "It's nice, but there are already three 'Galinis' in the harbour. When someone shouts from the jetty, they'll all turn round. I was thinking of something more our own, like 'Liopetra', the beach where we met."),
  L("Μαρίνα", "f", "Αυτό μ' αρέσει πολύ. Και ο θείος μου θα το δεχτεί, γιατί είναι όνομα τόπου, όχι ανθρώπου. Θα του ζητήσω να έρθει να γράψει τα γράμματα με το πινέλο, έχει πολύ ωραίο χέρι.", "I really like that. And my uncle will accept it, because it's a place name, not a person's. I'll ask him to come and paint the letters with the brush; he has a lovely hand."),
 ],
 "questions": [
  Q("Γιατί ο θείος της Μαρίνας δεν θέλει να αλλάξει το όνομα;", ["Γιατί του αρέσει το όνομα «Κική»", "Γιατί οι ψαράδες το θεωρούν γρουσουζιά", "Γιατί κοστίζει πολύ", "Γιατί απαγορεύεται από το λιμεναρχείο"], 1, "Οι ψαράδες το θεωρούν γρουσουζιά"),
  Q("Γιατί ο Στέλιος δεν θέλει το όνομα «Γαλήνη»;", ["Γιατί υπάρχουν ήδη τρεις «Γαλήνες» στο λιμάνι", "Γιατί είναι το όνομα μιας πρώην του", "Γιατί είναι πολύ μεγάλο για τη βάρκα", "Γιατί φέρνει κακοτυχία"], 0, "στο λιμάνι υπάρχουν ήδη τρεις «Γαλήνες»"),
  Q("Τι είναι η «Λιόπετρα»;", ["Το χωριό του θείου", "Το όνομα της πεθεράς του ιδιοκτήτη", "Η παραλία όπου γνωρίστηκαν", "Ένα παλιό καΐκι του λιμανιού"], 2, "η παραλία όπου γνωριστήκαμε"),
 ],
 "gloss": {"ψαρόβαρκα": "ψαρόβαρκα — fishing boat", "πεθεράς": "πεθερά — mother-in-law", "γρουσουζιά": "γρουσουζιά — bad luck, jinx", "τελετή": "τελετή — ceremony", "προβλήτα": "προβλήτα — jetty, pier", "πινέλο": "πινέλο — paintbrush"},
})

ITEMS.append({
 "id": "l190-news-alogo-se-pigadi", "title": "Πυροσβέστες βγάζουν ένα άλογο από πηγάδι", "title_en": "Firefighters pull a horse out of a well", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο τοπικό δελτίο ειδήσεων.",
 "script": [
  L("Εκφωνήτρια", "f", "Με αίσιο τέλος ολοκληρώθηκε χθες το απόγευμα μια ασυνήθιστη επιχείρηση διάσωσης σε ένα χωριό της Ηλείας. Μια δεκαοχτάχρονη φοράδα έπεσε σε ένα παλιό, ξεχασμένο πηγάδι βάθους τεσσάρων μέτρων, όταν υποχώρησαν οι σάπιες σανίδες που το σκέπαζαν.", "An unusual rescue operation in a village in Ilia ended happily yesterday afternoon. An eighteen-year-old mare fell into an old, forgotten well four metres deep when the rotten boards covering it gave way."),
  L("Εκφωνήτρια", "f", "Οι πυροσβέστες, με τη βοήθεια ενός κτηνίατρου που της έδωσε ηρεμιστικό, πέρασαν φαρδιούς ιμάντες κάτω από την κοιλιά του ζώου και το σήκωσαν με γερανό. Η επιχείρηση κράτησε σχεδόν πέντε ώρες, και τη συγκινημένη ιδιοκτήτρια τη χειροκρότησαν οι γείτονες όταν η φοράδα πάτησε ξανά στο χώμα.", "The firefighters, with the help of a vet who gave her a sedative, passed wide straps under the animal's belly and lifted it with a crane. The operation lasted almost five hours, and the neighbours applauded the moved owner when the mare set foot on the ground again."),
  L("Εκφωνήτρια", "f", "Ο κτηνίατρος δήλωσε ότι το ζώο έχει μόνο μερικές γρατζουνιές. Η πυροσβεστική υπενθυμίζει στους ιδιοκτήτες αγροτεμαχίων ότι τα εγκαταλελειμμένα πηγάδια πρέπει να σκεπάζονται με γερό μεταλλικό κάλυμμα, γιατί κάθε χρόνο σε αυτά πέφτουν ζώα, αλλά και άνθρωποι.", "The vet stated that the animal has only a few scratches. The fire service reminds owners of plots of land that abandoned wells must be covered with a strong metal cover, because every year animals, and people too, fall into them."),
 ],
 "questions": [
  Q("Πώς έπεσε η φοράδα στο πηγάδι;", ["Την κυνήγησε ένα σκυλί", "Υποχώρησαν οι σάπιες σανίδες που το σκέπαζαν", "Γλίστρησε στη λάσπη μετά τη βροχή", "Πήδηξε για να πιει νερό"], 1, "όταν υποχώρησαν οι σάπιες σανίδες που το σκέπαζαν"),
  Q("Τι έκανε ο κτηνίατρος κατά τη διάσωση;", ["Έδωσε στο ζώο ηρεμιστικό", "Οδήγησε τον γερανό", "Κατέβηκε μέσα στο πηγάδι", "Τηλεφώνησε στην πυροσβεστική"], 0, "ενός κτηνίατρου που της έδωσε ηρεμιστικό"),
  Q("Τι υπενθυμίζει η πυροσβεστική;", ["Να μην αφήνουν τα ζώα ελεύθερα", "Να γεμίζουν τα πηγάδια με χώμα", "Να σκεπάζονται τα πηγάδια με γερό μεταλλικό κάλυμμα", "Να καλούν αμέσως τον κτηνίατρο"], 2, "πρέπει να σκεπάζονται με γερό μεταλλικό κάλυμμα"),
 ],
 "gloss": {"αίσιο": "αίσιος — happy (ending), auspicious", "φοράδα": "φοράδα — mare", "υποχώρησαν": "υποχωρώ — to give way, collapse", "ηρεμιστικό": "ηρεμιστικό — sedative", "ιμάντες": "ιμάντας — strap, belt", "γερανό": "γερανός — crane", "αγροτεμαχίων": "αγροτεμάχιο — plot of farmland"},
})

ITEMS.append({
 "id": "l190-rep-nychta-sto-fourno-to-pascha", "title": "Μια νύχτα στον φούρνο πριν από το Πάσχα", "title_en": "A night at the bakery before Easter", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ραδιοφωνικό ρεπορτάζ από έναν φούρνο γειτονιάς τη Μεγάλη Εβδομάδα.",
 "script": [
  L("Ρεπόρτερ", "f", "Είναι τρεις τα ξημερώματα της Μεγάλης Πέμπτης, και στον φούρνο της κυρίας Ευτυχίας τα φώτα δεν έσβησαν ποτέ. Η μυρωδιά από το μαχλέπι και τη μαστίχα φτάνει ως τη γωνία του δρόμου. Μέσα, πέντε άνθρωποι πλάθουν τσουρέκια από τις δέκα το βράδυ.", "It's three in the morning on Holy Thursday, and at Mrs Eftychia's bakery the lights never went off. The smell of mahlab and mastic reaches the corner of the street. Inside, five people have been shaping tsourekia since ten in the evening."),
  L("Φούρναρισσα", "f", "Αυτή την εβδομάδα ψήνουμε πάνω από χίλια τσουρέκια, ενώ τις άλλες εβδομάδες μόλις πενήντα. Το μυστικό είναι η υπομονή: η ζύμη πρέπει να φουσκώσει τρεις φορές, και αν βιαστείς, το τσουρέκι δεν βγάζει εκείνες τις ίνες που τραβιούνται σαν βαμβάκι.", "This week we bake over a thousand tsourekia, while other weeks just fifty. The secret is patience: the dough has to rise three times, and if you rush it, the tsoureki doesn't get those strands that pull apart like cotton wool."),
  L("Ρεπόρτερ", "f", "Ανάμεσα στους φούρναρηδες είναι και ο εγγονός της, φοιτητής, που έρχεται κάθε χρόνο από τη Θεσσαλονίκη για να βοηθήσει. Λέει ότι εδώ έμαθε να πλέκει την πλεξούδα με τρία κορδόνια ζύμης πριν μάθει να δένει τα κορδόνια των παπουτσιών του.", "Among the bakers is her grandson, a student, who comes from Thessaloniki every year to help. He says that here he learned to plait the braid with three strands of dough before he learned to tie his shoelaces."),
  L("Φούρναρισσα", "f", "Τη Μεγάλη Παρασκευή κλείνουμε τον φούρνο το απόγευμα για να πάμε στον Επιτάφιο. Και το Μεγάλο Σάββατο βάφουμε κι εμείς τα δικά μας κόκκινα αυγά, γιατί όλη την εβδομάδα δεν προλαβαίνουμε.", "On Good Friday we close the bakery in the afternoon to go to the Epitaphios procession. And on Holy Saturday we dye our own red eggs, because all week we don't have time."),
 ],
 "questions": [
  Q("Πόσα τσουρέκια ψήνει ο φούρνος τις υπόλοιπες εβδομάδες;", ["Πάνω από χίλια", "Περίπου πεντακόσια", "Μόλις πενήντα", "Κανένα"], 2, "τις άλλες εβδομάδες μόλις πενήντα"),
  Q("Τι γίνεται αν βιαστείς με τη ζύμη;", ["Το τσουρέκι καίγεται", "Το τσουρέκι δεν βγάζει τις ίνες που τραβιούνται", "Η ζύμη γίνεται πολύ γλυκιά", "Χάνεται η μυρωδιά της μαστίχας"], 1, "αν βιαστείς, το τσουρέκι δεν βγάζει εκείνες τις ίνες"),
  Q("Γιατί κλείνει ο φούρνος τη Μεγάλη Παρασκευή το απόγευμα;", ["Για να βάψουν τα αυγά", "Για να ξεκουραστούν οι φούρναρηδες", "Για να πάνε στον Επιτάφιο", "Γιατί τελειώνει το αλεύρι"], 2, "κλείνουμε τον φούρνο το απόγευμα για να πάμε στον Επιτάφιο"),
 ],
 "gloss": {"ξημερώματα": "ξημερώματα — small hours, dawn", "μαχλέπι": "μαχλέπι — mahlab (cherry-stone spice)", "πλάθουν": "πλάθω — to shape, knead", "φουσκώσει": "φουσκώνω — to rise (of dough)", "ίνες": "ίνα — fibre, strand", "πλεξούδα": "πλεξούδα — braid, plait", "Επιτάφιο": "Επιτάφιος — Good Friday procession of Christ's bier"},
})

ITEMS.append({
 "id": "l190-c1-erotimatiko-kai-ano-teleia", "title": "Το ερωτηματικό που μοιάζει με άνω τελεία", "title_en": "The question mark that looks like a semicolon", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με μια γλωσσολόγο για την ιστορία της στίξης στα ελληνικά.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι ξένοι που μαθαίνουν ελληνικά σοκάρονται όταν βλέπουν ότι το ερωτηματικό μας είναι το δικό τους σύμβολο για τη «semicolon». Από πού προέρχεται αυτή η σύμπτωση;", "Foreigners learning Greek are shocked to see that our question mark is their symbol for the semicolon. Where does this coincidence come from?"),
  L("Γλωσσολόγος", "f", "Δεν είναι ακριβώς σύμπτωση, είναι δύο ξεχωριστές ιστορίες που κατέληξαν στο ίδιο σχήμα. Στην αρχαιότητα τα κείμενα γράφονταν σχεδόν χωρίς στίξη, συχνά και χωρίς κενά ανάμεσα στις λέξεις. Η παράδοση αποδίδει στον Αριστοφάνη τον Βυζάντιο, γύρω στον τρίτο αιώνα π.Χ., ένα σύστημα με τελείες σε διαφορετικό ύψος, που έδειχναν στον αναγνώστη πόση ανάσα να πάρει. Το σημάδι που λειτουργεί ως ερωτηματικό εμφανίζεται πολύ αργότερα, στα βυζαντινά χειρόγραφα, και η Δύση έδωσε στο ίδιο σχήμα άλλη αποστολή.", "It isn't exactly a coincidence; it's two separate stories that ended up with the same shape. In antiquity texts were written with almost no punctuation, often without spaces between words either. Tradition credits Aristophanes of Byzantium, around the third century BC, with a system of dots at different heights, which showed the reader how much breath to take. The sign that works as a question mark appears much later, in Byzantine manuscripts, and the West gave the same shape a different job."),
  L("Δημοσιογράφος", "m", "Και στους υπολογιστές; Είναι το ίδιο πλήκτρο;", "And on computers? Is it the same key?"),
  L("Γλωσσολόγος", "f", "Εδώ η ιστορία γίνεται διασκεδαστική. Το πρότυπο Unicode έχει ξεχωριστό χαρακτήρα για το ελληνικό ερωτηματικό, αλλά τον ορίζει ως ισοδύναμο με το λατινικό σημείο, οπότε στην πράξη τα περισσότερα προγράμματα τα μετατρέπουν σιωπηλά στον ίδιο χαρακτήρα. Δηλαδή ο υπολογιστής αναγνωρίζει ότι πρόκειται για κάτι άλλο, και αμέσως μετά το ξεχνά.", "This is where the story gets amusing. The Unicode standard has a separate character for the Greek question mark, but defines it as equivalent to the Latin sign, so in practice most programs silently convert them to the same character. In other words, the computer recognises that it's something different, and immediately forgets it."),
  L("Δημοσιογράφος", "m", "Η άνω τελεία, πάντως, μοιάζει να εξαφανίζεται.", "The raised dot, anyway, seems to be disappearing."),
  L("Γλωσσολόγος", "f", "Υποχωρεί, αυτό είναι αλήθεια, κυρίως στα μηνύματα και στα μέσα κοινωνικής δικτύωσης, όπου την αντικαθιστούν η τελεία, η παύλα ή απλώς μια νέα γραμμή. Δεν θα μιλούσα για παρακμή όμως. Η στίξη πάντα ακολουθούσε τον τρόπο που διαβάζουμε. Όταν διαβάζαμε φωναχτά, χρειαζόμασταν σημάδια για την αναπνοή· τώρα που διαβάζουμε βιαστικά σε μια οθόνη, χρειαζόμαστε σημάδια για το μάτι. Όποιος όμως θέλει να γράψει μια περίοδο με δύο σκέλη που ανήκουν μαζί, θα ανακαλύψει ότι η άνω τελεία κάνει μια δουλειά που κανένα άλλο σημείο δεν κάνει τόσο κομψά.", "It's receding, that's true, mainly in messages and on social media, where it's replaced by the full stop, the dash or simply a new line. I wouldn't speak of decline, though. Punctuation has always followed the way we read. When we read aloud, we needed signs for breathing; now that we read hurriedly on a screen, we need signs for the eye. But anyone who wants to write a sentence with two halves that belong together will discover that the raised dot does a job that no other mark does so elegantly."),
 ],
 "questions": [
  Q("Τι έδειχναν οι τελείες σε διαφορετικό ύψος που αποδίδονται στον Αριστοφάνη τον Βυζάντιο;", ["Πού τελειώνει κάθε λέξη", "Πόση ανάσα να πάρει ο αναγνώστης", "Ποια συλλαβή τονίζεται", "Πότε μιλά άλλο πρόσωπο"], 1, "έδειχναν στον αναγνώστη πόση ανάσα να πάρει"),
  Q("Τι κάνουν στην πράξη τα περισσότερα προγράμματα με το ελληνικό ερωτηματικό;", ["Το εμφανίζουν με άλλη γραμματοσειρά", "Το αρνούνται ως λάθος χαρακτήρα", "Το μετατρέπουν σιωπηλά στον ίδιο χαρακτήρα με το λατινικό σημείο", "Το αντικαθιστούν με το λατινικό ερωτηματικό"], 2, "τα περισσότερα προγράμματα τα μετατρέπουν σιωπηλά στον ίδιο χαρακτήρα"),
  Q("Πώς ερμηνεύει η γλωσσολόγος την υποχώρηση της άνω τελείας;", ["Ως σημάδι παρακμής της γλώσσας", "Ως αποτέλεσμα κακής διδασκαλίας στο σχολείο", "Ως προσαρμογή της στίξης στον τρόπο που διαβάζουμε σήμερα", "Ως επιρροή της αγγλικής γραμματικής"], 2, "Η στίξη πάντα ακολουθούσε τον τρόπο που διαβάζουμε"),
 ],
 "gloss": {"στίξης": "στίξη — punctuation", "σύμπτωση": "σύμπτωση — coincidence", "χειρόγραφα": "χειρόγραφο — manuscript", "ισοδύναμο": "ισοδύναμος — equivalent", "Υποχωρεί": "υποχωρώ — to recede", "παρακμή": "παρακμή — decline", "σκέλη": "σκέλος — part, half (of a sentence)"},
})

ITEMS.append({
 "id": "l190-c1-arithmos-ntanmpar", "title": "Πόσους φίλους μπορεί να έχει ένας άνθρωπος;", "title_en": "How many friends can one person have?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ψυχολόγο σε μια ραδιοφωνική εκπομπή επιστήμης.",
 "script": [
  L("Ψυχολόγος", "f", "Στη δεκαετία του '90, ο Βρετανός ανθρωπολόγος Ρόμπιν Ντάνμπαρ παρατήρησε ότι στα πρωτεύοντα θηλαστικά το μέγεθος της ομάδας στην οποία ζει ένα είδος συσχετίζεται με το μέγεθος του νεοφλοιού, του εξωτερικού στρώματος του εγκεφάλου. Αν προεκτείνει κανείς τη σχέση αυτή στον άνθρωπο, καταλήγει σε έναν αριθμό γύρω στο εκατόν πενήντα: τόσες περίπου σταθερές σχέσεις, κατά τον Ντάνμπαρ, μπορεί να διατηρεί ένας άνθρωπος, δηλαδή ανθρώπους που ξέρεις ποιοι είναι και πώς σχετίζονται μεταξύ τους.", "In the nineties, the British anthropologist Robin Dunbar observed that in primates the size of the group a species lives in correlates with the size of the neocortex, the outer layer of the brain. If you extend this relationship to humans, you arrive at a number around one hundred and fifty: roughly that many stable relationships, according to Dunbar, a person can maintain, meaning people you know who they are and how they relate to each other."),
  L("Ψυχολόγος", "f", "Ο Ντάνμπαρ πρότεινε μάλιστα ότι οι σχέσεις μας οργανώνονται σε ομόκεντρους κύκλους: περίπου πέντε πολύ στενοί άνθρωποι, δεκαπέντε καλοί φίλοι, πενήντα φίλοι και εκατόν πενήντα γνωστοί με νόημα. Το ενδιαφέρον είναι ότι παρόμοια νούμερα εμφανίζονται, κατά τους υποστηρικτές της θεωρίας, στο μέγεθος των παραδοσιακών χωριών, των στρατιωτικών μονάδων ή των λιστών με ευχετήριες κάρτες.", "Dunbar even proposed that our relationships are organised in concentric circles: about five very close people, fifteen good friends, fifty friends and a hundred and fifty meaningful acquaintances. What's interesting is that similar numbers appear, according to supporters of the theory, in the size of traditional villages, military units or Christmas-card lists."),
  L("Ψυχολόγος", "f", "Η θεωρία όμως δεν έμεινε αναπάντητη. Μια μελέτη του 2021 επανέλαβε τους υπολογισμούς με νεότερα δεδομένα και βρήκε ότι, ανάλογα με τη μέθοδο, το όριο μπορεί να είναι από λίγες μονάδες μέχρι πολλές εκατοντάδες, πράγμα που κάνει τον συγκεκριμένο αριθμό λιγότερο πειστικό. Νομίζω ότι η πιο χρήσιμη ιδέα του Ντάνμπαρ δεν είναι ο αριθμός, αλλά η διαπίστωση ότι ο χρόνος και η προσοχή μας είναι πεπερασμένα. Όσο κι αν μεγαλώνει η λίστα των επαφών στο κινητό, η μέρα έχει ακόμα εικοσιτέσσερις ώρες.", "But the theory did not go unanswered. A 2021 study repeated the calculations with newer data and found that, depending on the method, the limit could be anything from a handful to many hundreds, which makes the specific number less convincing. I think Dunbar's most useful idea is not the number, but the observation that our time and attention are finite. However long the contact list on your phone grows, the day still has twenty-four hours."),
 ],
 "questions": [
  Q("Σε ποια παρατήρηση στηρίχτηκε αρχικά ο Ντάνμπαρ;", ["Στον αριθμό των φίλων των φοιτητών του", "Στη σχέση ανάμεσα στο μέγεθος της ομάδας και στο μέγεθος του νεοφλοιού στα πρωτεύοντα", "Στο μέγεθος των σύγχρονων πόλεων", "Στις λίστες επαφών των κινητών τηλεφώνων"], 1, "το μέγεθος της ομάδας στην οποία ζει ένα είδος συσχετίζεται με το μέγεθος του νεοφλοιού"),
  Q("Τι έδειξε η μελέτη του 2021;", ["Ότι ο αριθμός είναι ακριβώς εκατόν πενήντα", "Ότι οι γυναίκες έχουν περισσότερους φίλους", "Ότι το όριο ποικίλλει πολύ ανάλογα με τη μέθοδο", "Ότι τα μέσα κοινωνικής δικτύωσης αυξάνουν το όριο"], 2, "ανάλογα με τη μέθοδο, το όριο μπορεί να είναι από λίγες μονάδες μέχρι πολλές εκατοντάδες"),
  Q("Ποια θεωρεί η ψυχολόγος την πιο χρήσιμη ιδέα του Ντάνμπαρ;", ["Ότι ο χρόνος και η προσοχή μας είναι πεπερασμένα", "Ότι οι στενοί φίλοι είναι πάντα πέντε", "Ότι τα χωριά είναι καλύτερα από τις πόλεις", "Ότι χρειαζόμαστε περισσότερες επαφές"], 0, "ο χρόνος και η προσοχή μας είναι πεπερασμένα"),
 ],
 "gloss": {"ανθρωπολόγος": "ανθρωπολόγος — anthropologist", "πρωτεύοντα": "πρωτεύοντα (θηλαστικά) — primates", "νεοφλοιού": "νεοφλοιός — neocortex", "προεκτείνει": "προεκτείνω — to extend, extrapolate", "ομόκεντρους": "ομόκεντρος — concentric", "αναπάντητη": "αναπάντητος — unanswered", "πεπερασμένα": "πεπερασμένος — finite"},
})

ITEMS.append({
 "id": "l190-rep-theatro-gia-mora", "title": "Θέατρο για θεατές κάτω των δύο", "title_en": "Theatre for audiences under two", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για μια θεατρική παράσταση που απευθύνεται σε βρέφη.",
 "script": [
  L("Ρεπόρτερ", "m", "Στην αίθουσα δεν υπάρχουν καθίσματα, μόνο μαλακά μαξιλάρια σε κύκλο. Οι θεατές είναι από έξι μηνών μέχρι δύο χρονών, και κάθονται στην αγκαλιά των γονιών τους. Η παράσταση κρατάει μόνο τριάντα λεπτά, γιατί, όπως λέει η σκηνοθέτιδα, μετά από μισή ώρα ακόμα και το πιο ήσυχο μωρό θέλει να φύγει.", "In the hall there are no seats, only soft cushions in a circle. The audience is aged from six months to two years, and they sit in their parents' laps. The show lasts only thirty minutes, because, as the director says, after half an hour even the quietest baby wants to leave."),
  L("Σκηνοθέτιδα", "f", "Δεν υπάρχει υπόθεση με την κλασική έννοια. Υπάρχουν χρώματα, απαλοί ήχοι, ένα τσέλο και δύο ηθοποιοί που παίζουν με υφάσματα και σαπουνόφουσκες. Τα μωρά δεν χρειάζονται ιστορία, χρειάζονται έκπληξη. Και ό,τι κάνουν, αν κλάψουν ή αν μπουσουλήσουν μέχρι τη σκηνή, γίνεται μέρος της παράστασης.", "There isn't a plot in the classic sense. There are colours, soft sounds, a cello and two actors who play with fabrics and soap bubbles. Babies don't need a story, they need surprise. And whatever they do, whether they cry or crawl up to the stage, becomes part of the show."),
  L("Ρεπόρτερ", "m", "Η μητέρα του δεκάμηνου Άρη μάς λέει ότι ήρθε κυρίως για τον εαυτό της. Για μήνες δεν είχε βγει πουθενά, και εδώ κανείς δεν την κοιτάζει άσχημα αν ο γιος της αρχίσει να φωνάζει. Οι παραστάσεις είναι κάθε Κυριακή πρωί, και τα εισιτήρια εξαντλούνται συνήθως μέσα σε μία μέρα.", "Ten-month-old Aris's mother tells us she came mainly for herself. For months she hadn't been out anywhere, and here nobody looks at her disapprovingly if her son starts shouting. Performances are every Sunday morning, and tickets usually sell out within a day."),
 ],
 "questions": [
  Q("Γιατί η παράσταση κρατάει μόνο τριάντα λεπτά;", ["Γιατί η αίθουσα χρειάζεται για άλλη παράσταση", "Γιατί μετά από μισή ώρα και το πιο ήσυχο μωρό θέλει να φύγει", "Γιατί οι ηθοποιοί κουράζονται", "Γιατί τα εισιτήρια είναι φθηνά"], 1, "μετά από μισή ώρα ακόμα και το πιο ήσυχο μωρό θέλει να φύγει"),
  Q("Τι χρειάζονται τα μωρά, σύμφωνα με τη σκηνοθέτιδα;", ["Μια ξεκάθαρη ιστορία", "Ησυχία και σκοτάδι", "Έκπληξη", "Γνωστά τραγούδια"], 2, "χρειάζονται έκπληξη"),
  Q("Γιατί ήρθε κυρίως η μητέρα του Άρη;", ["Γιατί της το πρότεινε ο παιδίατρος", "Για τον εαυτό της, γιατί για μήνες δεν είχε βγει πουθενά", "Γιατί ο Άρης λατρεύει το τσέλο", "Γιατί η είσοδος ήταν δωρεάν"], 1, "Για μήνες δεν είχε βγει πουθενά"),
 ],
 "gloss": {"βρέφη": "βρέφος — baby, infant", "σκηνοθέτιδα": "σκηνοθέτιδα — (female) director", "υπόθεση": "υπόθεση — plot", "σαπουνόφουσκες": "σαπουνόφουσκα — soap bubble", "μπουσουλήσουν": "μπουσουλάω — to crawl", "εξαντλούνται": "εξαντλούμαι — to sell out, run out"},
})

rnd = random.Random(190)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-190.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
