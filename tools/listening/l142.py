# Source for library/listening/listening-142.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l142.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l142-vm-raftis", "title": "Το κοστούμι είναι σχεδόν έτοιμο", "title_en": "The suit is almost ready", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δώσει ένα κοστούμι για μεταποίηση σε ένα ραφείο. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Ράφτρα", "f", "Καλημέρα σας, από το ραφείο «Η Βελόνα» σας τηλεφωνώ, για το κοστούμι που μας φέρατε την Τρίτη. Το παντελόνι είναι έτοιμο, το κοντύναμε όπως είπαμε, τρία εκατοστά.", "Good morning, I'm calling from 'The Needle' tailor's, about the suit you brought us on Tuesday. The trousers are ready, we shortened them as we said, three centimetres."),
  L("Ράφτρα", "f", "Με το σακάκι όμως έχουμε ένα μικρό πρόβλημα. Τα μανίκια δεν μπορούν να μακρύνουν όσο θέλατε, γιατί δεν υπάρχει αρκετό ύφασμα στο εσωτερικό. Μπορούμε να τα μακρύνουμε ενάμισι εκατοστό το πολύ. Αν σας κάνει, θα είναι έτοιμο την Παρασκευή.", "With the jacket, though, we have a small problem. The sleeves can't be lengthened as much as you wanted, because there isn't enough fabric inside. We can lengthen them one and a half centimetres at most. If that suits you, it will be ready on Friday."),
  L("Ράφτρα", "f", "Καλό θα ήταν να περάσετε να το δοκιμάσετε πριν τελειώσουμε. Είμαστε ανοιχτά καθημερινά μέχρι τις οχτώ, εκτός Σαββάτου απόγευμα.", "It would be good if you came by to try it on before we finish. We're open daily until eight, except Saturday afternoon."),
 ],
 "questions": [
  Q("Τι έχουν κάνει ήδη στο παντελόνι;", ["Το κοντύνανε τρία εκατοστά", "Το φάρδυναν", "Άλλαξαν το φερμουάρ", "Τίποτα ακόμα"], 0, "το κοντύναμε όπως είπαμε, τρία εκατοστά"),
  Q("Γιατί δεν μπορούν να μακρύνουν τα μανίκια όσο θέλατε;", ["Γιατί δεν έχουν χρόνο", "Γιατί δεν υπάρχει αρκετό ύφασμα στο εσωτερικό", "Γιατί το ύφασμα είναι πολύ λεπτό", "Γιατί χάλασε η ραπτομηχανή"], 1, "δεν υπάρχει αρκετό ύφασμα στο εσωτερικό"),
  Q("Τι σας προτείνει να κάνετε;", ["Να φέρετε άλλο σακάκι", "Να πληρώσετε προκαταβολή", "Να περάσετε να το δοκιμάσετε πριν τελειώσουν", "Να τηλεφωνήσετε το Σάββατο"], 2, "Καλό θα ήταν να περάσετε να το δοκιμάσετε πριν τελειώσουμε"),
 ],
 "gloss": {"μεταποίηση": "μεταποίηση — alteration", "ραφείο": "ραφείο — tailor's shop", "κοντύναμε": "κονταίνω — to shorten", "εκατοστά": "εκατοστό — centimetre", "σακάκι": "σακάκι — jacket", "μανίκια": "μανίκι — sleeve", "μακρύνουν": "μακραίνω — to lengthen", "ύφασμα": "ύφασμα — fabric", "δοκιμάσετε": "δοκιμάζω — to try on"}
})

ITEMS.append({
 "id": "l142-ann-podilatikos", "title": "Κλειστοί δρόμοι την Κυριακή", "title_en": "Roads closed on Sunday", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση για την κυκλοφορία σε έναν τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνήτρια", "f", "Ενημερώνουμε τους οδηγούς ότι την Κυριακή, λόγω του ποδηλατικού αγώνα «Γύρος της Πόλης», θα διακοπεί η κυκλοφορία των οχημάτων στην παραλιακή λεωφόρο από τις επτά το πρωί μέχρι τις δύο το μεσημέρι.", "Drivers are informed that on Sunday, because of the cycling race 'Tour of the City', traffic will be stopped on the seafront avenue from seven in the morning until two in the afternoon."),
  L("Εκφωνήτρια", "f", "Τα αστικά λεωφορεία των γραμμών 5 και 12 θα ακολουθούν παρακαμπτήριο δρόμο μέσω της οδού Εθνικής Αντιστάσεως. Η στάθμευση στην παραλιακή απαγορεύεται ήδη από το βράδυ του Σαββάτου, και όσα αυτοκίνητα βρίσκονται εκεί θα μεταφερθούν με γερανό.", "City buses on lines 5 and 12 will follow a diversion via Ethnikis Antistaseos Street. Parking on the seafront is prohibited from Saturday evening, and any cars there will be towed away."),
  L("Εκφωνήτρια", "f", "Οι κάτοικοι που χρειάζονται να μετακινηθούν για λόγους υγείας μπορούν να απευθύνονται στους τροχονόμους, οι οποίοι θα βρίσκονται σε κάθε διασταύρωση.", "Residents who need to travel for health reasons can turn to the traffic police, who will be at every junction."),
 ],
 "questions": [
  Q("Γιατί θα κλείσει η παραλιακή λεωφόρος;", ["Λόγω έργων", "Λόγω ενός ποδηλατικού αγώνα", "Λόγω μιας διαδήλωσης", "Λόγω μιας συναυλίας"], 1, "λόγω του ποδηλατικού αγώνα"),
  Q("Τι θα γίνει με τα αυτοκίνητα που θα είναι σταθμευμένα στην παραλιακή;", ["Θα πάρουν κλήση", "Τίποτα", "Θα μεταφερθούν με γερανό", "Θα τα φυλάνε τροχονόμοι"], 2, "θα μεταφερθούν με γερανό"),
  Q("Σε ποιον μπορούν να απευθυνθούν όσοι πρέπει να μετακινηθούν για λόγους υγείας;", ["Στους τροχονόμους στις διασταυρώσεις", "Στον δήμο", "Στο νοσοκομείο", "Στους διοργανωτές"], 0, "μπορούν να απευθύνονται στους τροχονόμους"),
 ],
 "gloss": {"ποδηλατικού": "ποδηλατικός — cycling", "διακοπεί": "διακόπτομαι — to be stopped", "οχημάτων": "όχημα — vehicle", "παραλιακή": "παραλιακός — seafront", "παρακαμπτήριο": "παρακαμπτήριος — diversion, bypass", "στάθμευση": "στάθμευση — parking", "γερανό": "γερανός — tow truck", "τροχονόμους": "τροχονόμος — traffic police officer", "διασταύρωση": "διασταύρωση — junction"}
})

ITEMS.append({
 "id": "l142-dia-doro-syntaxi", "title": "Ένα δώρο για τη σύνταξη", "title_en": "A retirement present", "type": "dialogue", "level": "B2",
 "context_el": "Δύο συνάδελφοι συζητούν στο γραφείο.",
 "script": [
  L("Μαρίνα", "f", "Ξέρεις ότι ο κύριος Αντωνίου βγαίνει στη σύνταξη στο τέλος του μήνα; Τριάντα πέντε χρόνια στην εταιρεία! Πρέπει να του πάρουμε κάτι ωραίο.", "Do you know Mr Antoniou is retiring at the end of the month? Thirty-five years at the company! We have to get him something nice."),
  L("Θοδωρής", "m", "Σκεφτόμουν ένα ρολόι, αλλά είναι λίγο τυπικό. Και είναι ακριβό, αν μαζέψουμε μόνο από το τμήμα μας.", "I was thinking of a watch, but it's a bit conventional. And it's expensive, if we only collect from our department."),
  L("Μαρίνα", "f", "Μου είπε κάποτε ότι ονειρεύεται να μάθει να ψαρεύει με καλάμι, αλλά δεν είχε ποτέ χρόνο. Τι λες για ένα σετ ψαρέματος κι ένα μάθημα με έναν έμπειρο ψαρά;", "He once told me he dreams of learning to fish with a rod, but never had time. What do you think of a fishing set and a lesson with an experienced fisherman?"),
  L("Θοδωρής", "m", "Τέλειο! Και να γράψουμε όλοι από μια ευχή σε ένα άλμπουμ με φωτογραφίες από τα χρόνια του εδώ. Αναλαμβάνω εγώ να μαζέψω τα χρήματα, εσύ βρες τις φωτογραφίες.", "Perfect! And let's all write a wish in an album with photos from his years here. I'll take care of collecting the money, you find the photos."),
 ],
 "questions": [
  Q("Γιατί ο Θοδωρής δεν είναι σίγουρος για το ρολόι;", ["Γιατί ο κύριος Αντωνίου έχει ήδη ρολόι", "Γιατί είναι τυπικό και ακριβό", "Γιατί δεν βρίσκει κατάστημα", "Γιατί δεν του αρέσουν τα ρολόγια"], 1, "είναι λίγο τυπικό. Και είναι ακριβό"),
  Q("Τι ονειρεύεται ο κύριος Αντωνίου;", ["Να ταξιδέψει στην Ιαπωνία", "Να μάθει κιθάρα", "Να γράψει ένα βιβλίο", "Να μάθει να ψαρεύει με καλάμι"], 3, "ονειρεύεται να μάθει να ψαρεύει με καλάμι"),
  Q("Τι θα κάνει η Μαρίνα;", ["Θα μαζέψει τα χρήματα", "Θα αγοράσει το ρολόι", "Θα βρει τις φωτογραφίες", "Θα κλείσει εστιατόριο"], 2, "εσύ βρες τις φωτογραφίες"),
 ],
 "gloss": {"σύνταξη": "σύνταξη — retirement, pension", "τυπικό": "τυπικός — conventional, formal", "τμήμα": "τμήμα — department", "ψαρεύει": "ψαρεύω — to fish", "καλάμι": "καλάμι — fishing rod", "έμπειρο": "έμπειρος — experienced", "ευχή": "ευχή — wish", "Αναλαμβάνω": "αναλαμβάνω — to take on"}
})

ITEMS.append({
 "id": "l142-int-rologas", "title": "Ο άνθρωπος του ρολογιού", "title_en": "The man who keeps the clock", "type": "interview", "level": "B2",
 "context_el": "Ακούτε απόσπασμα από μια τοπική ραδιοφωνική εκπομπή.",
 "script": [
  L("Δημοσιογράφος", "f", "Εδώ και είκοσι χρόνια φροντίζετε το ρολόι στον πύργο της πλατείας. Τι ακριβώς κάνετε;", "For twenty years you've been looking after the clock in the tower on the square. What exactly do you do?"),
  L("Ωρολογοποιός", "m", "Το ρολόι είναι μηχανικό, του 1910, και κουρδίζεται με το χέρι. Κάθε Δευτέρα ανεβαίνω ενενήντα δύο σκαλιά και γυρίζω τη μανιβέλα για περίπου είκοσι λεπτά. Αν το ξεχάσω, μέχρι την Πέμπτη η πόλη μένει χωρίς ώρα.", "The clock is mechanical, from 1910, and is wound by hand. Every Monday I climb ninety-two steps and turn the crank for about twenty minutes. If I forget, by Thursday the town is left without the time."),
  L("Δημοσιογράφος", "f", "Είναι ακριβές;", "Is it accurate?"),
  L("Ωρολογοποιός", "m", "Χάνει περίπου ένα λεπτό την εβδομάδα, πιο πολύ τον χειμώνα, γιατί με το κρύο τα λάδια πήζουν. Γι' αυτό το ρυθμίζω με το ραδιόφωνο, με το σήμα των ειδήσεων. Πέρσι ο δήμος πρότεινε να βάλουμε ηλεκτρονικό μηχανισμό, αλλά οι κάτοικοι μάζεψαν υπογραφές και το παλιό έμεινε. Ψάχνω όμως κάποιον νέο να του μάθω τη δουλειά, γιατί τα γόνατά μου δεν αντέχουν για πολύ ακόμα.", "It loses about a minute a week, more in winter, because the oils thicken in the cold. So I set it by the radio, by the news signal. Last year the municipality proposed fitting an electronic mechanism, but the residents collected signatures and the old one stayed. But I'm looking for a young person to teach the job to, because my knees won't hold out much longer."),
 ],
 "questions": [
  Q("Τι κάνει κάθε Δευτέρα;", ["Ανεβαίνει στον πύργο και κουρδίζει το ρολόι", "Καθαρίζει τους δείκτες", "Αλλάζει τις μπαταρίες", "Χτυπά την καμπάνα"], 0, "Κάθε Δευτέρα ανεβαίνω ενενήντα δύο σκαλιά και γυρίζω τη μανιβέλα"),
  Q("Γιατί το ρολόι χάνει περισσότερο τον χειμώνα;", ["Γιατί έχει λιγότερο φως", "Γιατί φυσάει", "Γιατί με το κρύο τα λάδια πήζουν", "Γιατί ο ίδιος ανεβαίνει λιγότερο"], 2, "με το κρύο τα λάδια πήζουν"),
  Q("Τι έγινε όταν ο δήμος πρότεινε ηλεκτρονικό μηχανισμό;", ["Ο μηχανισμός αγοράστηκε", "Οι κάτοικοι μάζεψαν υπογραφές και το παλιό έμεινε", "Ο ωρολογοποιός παραιτήθηκε", "Το ρολόι σταμάτησε"], 1, "οι κάτοικοι μάζεψαν υπογραφές και το παλιό έμεινε"),
 ],
 "gloss": {"πύργο": "πύργος — tower", "μηχανικό": "μηχανικός — mechanical", "κουρδίζεται": "κουρδίζομαι — to be wound", "σκαλιά": "σκαλί — step", "μανιβέλα": "μανιβέλα — crank", "ακριβές": "ακριβής — accurate", "πήζουν": "πήζω — to thicken, set", "ρυθμίζω": "ρυθμίζω — to set, adjust", "σήμα": "σήμα — signal", "υπογραφές": "υπογραφή — signature", "γόνατά": "γόνατο — knee"}
})

ITEMS.append({
 "id": "l142-news-eikona", "title": "Η εικόνα γύρισε στο χωριό", "title_en": "The icon came back to the village", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο τοπικό δελτίο ειδήσεων.",
 "script": [
  L("Εκφωνητής", "m", "Με καμπάνες και δάκρυα υποδέχτηκαν χθες οι κάτοικοι ενός μικρού χωριού της Αρκαδίας μια εικόνα του Αγίου Γεωργίου, η οποία είχε κλαπεί από την εκκλησία τους πριν από τριάντα ένα χρόνια.", "With bells and tears, the residents of a small village in Arcadia yesterday welcomed an icon of Saint George that had been stolen from their church thirty-one years ago."),
  L("Εκφωνητής", "m", "Η εικόνα, του δέκατου όγδοου αιώνα, εντοπίστηκε πέρσι σε έναν κατάλογο οίκου δημοπρασιών στη Γερμανία. Ένας ερευνητής που μελετά κλεμμένα έργα τέχνης την αναγνώρισε από μια παλιά φωτογραφία του ιερέα του χωριού και ειδοποίησε το υπουργείο Πολιτισμού.", "The icon, from the eighteenth century, was located last year in an auction-house catalogue in Germany. A researcher who studies stolen works of art recognised it from an old photograph by the village priest and notified the Ministry of Culture."),
  L("Εκφωνητής", "m", "Μετά από διαπραγματεύσεις, η δημοπρασία ακυρώθηκε και η εικόνα επιστράφηκε. Θα μείνει όμως πρώτα δύο μήνες σε εργαστήριο συντήρησης, πριν πάρει ξανά τη θέση της στο τέμπλο.", "After negotiations, the auction was cancelled and the icon was returned. But it will first spend two months in a conservation workshop before taking its place again on the iconostasis."),
 ],
 "questions": [
  Q("Πότε είχε κλαπεί η εικόνα;", ["Πριν από τριάντα ένα χρόνια", "Πέρσι", "Τον δέκατο όγδοο αιώνα", "Πριν από δέκα χρόνια"], 0, "είχε κλαπεί από την εκκλησία τους πριν από τριάντα ένα χρόνια"),
  Q("Πώς αναγνωρίστηκε η εικόνα;", ["Από μια επιγραφή στο πίσω μέρος", "Από μια παλιά φωτογραφία του ιερέα", "Από έναν κάτοικο που την είδε σε μουσείο", "Από τον κλέφτη"], 1, "την αναγνώρισε από μια παλιά φωτογραφία του ιερέα του χωριού"),
  Q("Τι θα γίνει πριν επιστρέψει στο τέμπλο;", ["Θα εκτεθεί σε μουσείο της Αθήνας", "Θα ταξιδέψει σε άλλα χωριά", "Θα μείνει δύο μήνες σε εργαστήριο συντήρησης", "Θα πουληθεί"], 2, "Θα μείνει όμως πρώτα δύο μήνες σε εργαστήριο συντήρησης"),
 ],
 "gloss": {"καμπάνες": "καμπάνα — bell", "υποδέχτηκαν": "υποδέχομαι — to welcome", "εικόνα": "εικόνα — icon", "κλαπεί": "κλέβομαι — to be stolen", "εντοπίστηκε": "εντοπίζομαι — to be located", "δημοπρασιών": "δημοπρασία — auction", "κλεμμένα": "κλεμμένος — stolen", "διαπραγματεύσεις": "διαπραγμάτευση — negotiation", "συντήρησης": "συντήρηση — conservation", "τέμπλο": "τέμπλο — iconostasis"}
})

ITEMS.append({
 "id": "l142-mon-syntirisi", "title": "Πώς καθαρίζεται ένας πίνακας", "title_en": "How a painting is cleaned", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια συντηρήτρια να μιλά σε μια ομάδα επισκεπτών σε ένα μουσείο.",
 "script": [
  L("Συντηρήτρια", "f", "Αυτός ο πίνακας ήρθε στο εργαστήριό μας σχεδόν καφέ. Δεν ήταν το χρώμα του ζωγράφου· ήταν το βερνίκι, που με τα χρόνια κιτρινίζει, και από πάνω του σκόνη και καπνός από κεριά.", "This painting came to our workshop almost brown. It wasn't the painter's colour; it was the varnish, which yellows over the years, and on top of it dust and smoke from candles."),
  L("Συντηρήτρια", "f", "Πρώτα τον φωτογραφίζουμε και τον εξετάζουμε με υπεριώδες φως, για να δούμε ποια σημεία έχουν βαφτεί αργότερα. Ύστερα δοκιμάζουμε διαλύτες σε μια μικρή γωνία, ένα τετραγωνάκι ενός εκατοστού, και μόνο όταν είμαστε σίγουροι προχωράμε, με μπατονέτες, σημείο προς σημείο.", "First we photograph it and examine it under ultraviolet light, to see which areas were painted later. Then we test solvents in a small corner, a one-centimetre square, and only when we are sure do we proceed, with cotton swabs, spot by spot."),
  L("Συντηρήτρια", "f", "Ο κανόνας μας είναι ότι ό,τι κάνουμε πρέπει να μπορεί να αναιρεθεί στο μέλλον. Γι' αυτό τα κενά τα συμπληρώνουμε με χρώματα που αφαιρούνται εύκολα. Αυτός ο πίνακας μάς πήρε οχτώ μήνες.", "Our rule is that whatever we do must be reversible in the future. That's why we fill the gaps with paints that can be removed easily. This painting took us eight months."),
 ],
 "questions": [
  Q("Γιατί ο πίνακας είχε γίνει σχεδόν καφέ;", ["Γιατί ο ζωγράφος χρησιμοποίησε καφέ χρώματα", "Λόγω του βερνικιού που κιτρινίζει, της σκόνης και του καπνού", "Λόγω υγρασίας", "Γιατί είχε καεί"], 1, "ήταν το βερνίκι, που με τα χρόνια κιτρινίζει"),
  Q("Πού δοκιμάζουν πρώτα τους διαλύτες;", ["Σε όλο τον πίνακα", "Σε έναν άλλο πίνακα", "Σε μια μικρή γωνία, ένα τετραγωνάκι ενός εκατοστού", "Στο κέντρο του πίνακα"], 2, "δοκιμάζουμε διαλύτες σε μια μικρή γωνία"),
  Q("Ποιος είναι ο βασικός κανόνας της συντήρησης, σύμφωνα με την ομιλήτρια;", ["Ό,τι κάνουν πρέπει να μπορεί να αναιρεθεί στο μέλλον", "Να τελειώνουν γρήγορα", "Να μη φωτογραφίζουν τους πίνακες", "Να ξαναβάφουν τα κενά με λάδι"], 0, "ό,τι κάνουμε πρέπει να μπορεί να αναιρεθεί στο μέλλον"),
 ],
 "gloss": {"συντηρήτρια": "συντηρήτρια — (female) conservator", "βερνίκι": "βερνίκι — varnish", "κιτρινίζει": "κιτρινίζω — to turn yellow", "υπεριώδες": "υπεριώδης — ultraviolet", "διαλύτες": "διαλύτης — solvent", "μπατονέτες": "μπατονέτα — cotton swab", "αναιρεθεί": "αναιρούμαι — to be undone", "κενά": "κενό — gap", "αφαιρούνται": "αφαιρούμαι — to be removed"}
})

ITEMS.append({
 "id": "l142-rep-allagi-douleias", "title": "Οι νέοι αλλάζουν δουλειά", "title_en": "Young people change jobs", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια οικονομική εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Σύμφωνα με μια νέα έρευνα ενός πανεπιστημιακού ινστιτούτου, οι εργαζόμενοι κάτω των τριάντα πέντε ετών στην Ελλάδα μένουν σε μια θέση εργασίας κατά μέσο όρο δυόμισι χρόνια, ενώ οι γονείς τους έμεναν πάνω από δέκα.", "According to a new survey by a university institute, employees under thirty-five in Greece stay in a job for two and a half years on average, while their parents stayed more than ten."),
  L("Ρεπόρτερ", "f", "Ως κυριότερο λόγο για την αλλαγή, οι νέοι αναφέρουν τον μισθό. Αμέσως μετά όμως έρχεται η έλλειψη ευελιξίας στο ωράριο, και τρίτη η αίσθηση ότι δεν μαθαίνουν τίποτα καινούργιο.", "As the main reason for changing, young people cite pay. Right after that, however, comes the lack of flexibility in working hours, and third the feeling that they are not learning anything new."),
  L("Ρεπόρτερ", "f", "Οι εργοδότες, από την πλευρά τους, παραπονιούνται ότι επενδύουν στην εκπαίδευση ενός νέου υπαλλήλου και τον χάνουν μόλις γίνει παραγωγικός. Κάποιες εταιρείες έχουν αρχίσει να προσφέρουν ετήσια μπόνους παραμονής και μία μέρα την εβδομάδα τηλεργασία.", "Employers, for their part, complain that they invest in training a new employee and lose them as soon as they become productive. Some companies have started offering annual retention bonuses and one day a week of remote work."),
 ],
 "questions": [
  Q("Πόσο μένουν κατά μέσο όρο οι νέοι σε μια θέση εργασίας;", ["Δέκα χρόνια", "Έξι μήνες", "Δυόμισι χρόνια", "Πέντε χρόνια"], 2, "κατά μέσο όρο δυόμισι χρόνια"),
  Q("Ποιος είναι ο δεύτερος λόγος που αναφέρουν οι νέοι;", ["Ο μισθός", "Η έλλειψη ευελιξίας στο ωράριο", "Οι κακοί συνάδελφοι", "Η απόσταση από το σπίτι"], 1, "Αμέσως μετά όμως έρχεται η έλλειψη ευελιξίας στο ωράριο"),
  Q("Τι προσφέρουν κάποιες εταιρείες για να κρατήσουν τους υπαλλήλους;", ["Μπόνους παραμονής και μία μέρα τηλεργασία την εβδομάδα", "Δωρεάν φαγητό", "Αυτοκίνητο", "Περισσότερες άδειες το καλοκαίρι"], 0, "ετήσια μπόνους παραμονής και μία μέρα την εβδομάδα τηλεργασία"),
 ],
 "gloss": {"ινστιτούτου": "ινστιτούτο — institute", "εργαζόμενοι": "εργαζόμενος — employee", "μέσο όρο": "μέσος όρος — average", "ευελιξίας": "ευελιξία — flexibility", "ωράριο": "ωράριο — working hours", "εργοδότες": "εργοδότης — employer", "επενδύουν": "επενδύω — to invest", "παραγωγικός": "παραγωγικός — productive", "παραμονής": "παραμονή — staying, retention", "τηλεργασία": "τηλεργασία — remote work"}
})

ITEMS.append({
 "id": "l142-dia-trapezi", "title": "Τραπέζι για γενέθλια", "title_en": "A table for a birthday", "type": "dialogue", "level": "B2",
 "context_el": "Μια πελάτισσα τηλεφωνεί σε ένα εστιατόριο.",
 "script": [
  L("Πελάτισσα", "f", "Καλησπέρα, θα ήθελα να κλείσω ένα τραπέζι για δώδεκα άτομα το Σάββατο το βράδυ, για τα γενέθλια της μητέρας μου.", "Good evening, I'd like to book a table for twelve on Saturday evening, for my mother's birthday."),
  L("Υπάλληλος", "m", "Το Σάββατο στις εννιά έχουμε χώρο μόνο στην αυλή. Μέσα είμαστε γεμάτοι. Η αυλή όμως έχει θερμάστρες, οπότε δεν θα κρυώσετε.", "On Saturday at nine we only have room in the courtyard. Inside we're full. But the courtyard has heaters, so you won't be cold."),
  L("Πελάτισσα", "f", "Εντάξει. Ένα ακόμα: η θεία μου έχει κοιλιοκάκη και δεν μπορεί να φάει τίποτα με γλουτένη. Έχετε κάτι για εκείνη;", "Fine. One more thing: my aunt has coeliac disease and can't eat anything with gluten. Do you have something for her?"),
  L("Υπάλληλος", "m", "Βεβαίως. Τα περισσότερα ψητά μας δεν έχουν γλουτένη, και έχουμε και ψωμί χωρίς γλουτένη, αλλά πρέπει να το παραγγείλουμε από πριν. Θα το σημειώσω. Αν φέρετε δική σας τούρτα, η χρέωση είναι δύο ευρώ το άτομο για το σερβίρισμα.", "Of course. Most of our grilled dishes have no gluten, and we also have gluten-free bread, but we have to order it in advance. I'll note it down. If you bring your own cake, the charge is two euros per person for serving it."),
 ],
 "questions": [
  Q("Πού θα καθίσουν;", ["Μέσα, δίπλα στο τζάκι", "Στην αυλή, που έχει θερμάστρες", "Στον πρώτο όροφο", "Σε άλλο εστιατόριο"], 1, "έχουμε χώρο μόνο στην αυλή"),
  Q("Τι πρόβλημα έχει η θεία;", ["Είναι χορτοφάγος", "Δεν τρώει ψάρι", "Έχει κοιλιοκάκη και δεν τρώει γλουτένη", "Έχει αλλεργία στους ξηρούς καρπούς"], 2, "έχει κοιλιοκάκη και δεν μπορεί να φάει τίποτα με γλουτένη"),
  Q("Τι ισχύει αν φέρουν δική τους τούρτα;", ["Δεν επιτρέπεται", "Είναι δωρεάν", "Πρέπει να την αφήσουν στην κουζίνα από το πρωί", "Υπάρχει χρέωση δύο ευρώ το άτομο"], 3, "η χρέωση είναι δύο ευρώ το άτομο"),
 ],
 "gloss": {"αυλή": "αυλή — courtyard", "θερμάστρες": "θερμάστρα — heater", "κοιλιοκάκη": "κοιλιοκάκη — coeliac disease", "γλουτένη": "γλουτένη — gluten", "ψητά": "ψητό — grilled dish", "παραγγείλουμε": "παραγγέλνω — to order", "τούρτα": "τούρτα — cake", "χρέωση": "χρέωση — charge", "σερβίρισμα": "σερβίρισμα — serving"}
})

ITEMS.append({
 "id": "l142-c1-baumol", "title": "Η «ασθένεια του κόστους»", "title_en": "Baumol's cost disease", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη οικονομικών.",
 "script": [
  L("Καθηγήτρια", "f", "Το 1966 οι οικονομολόγοι Ουίλιαμ Μπόμολ και Ουίλιαμ Μπόουεν δημοσίευσαν μια μελέτη για τα οικονομικά των παραστατικών τεχνών, που έμελλε να ξεπεράσει κατά πολύ τα όρια του θεάτρου. Το παράδειγμά τους έμεινε κλασικό: για να παιχτεί ένα κουαρτέτο εγχόρδων του Μπετόβεν χρειάζονται σήμερα τέσσερις μουσικοί και περίπου όσος χρόνος χρειαζόταν και το 1800. Η «παραγωγικότητα» της μουσικής, αν μπορούμε να το πούμε έτσι, δεν έχει αυξηθεί καθόλου.", "In 1966 the economists William Baumol and William Bowen published a study on the economics of the performing arts that was to go far beyond the confines of the theatre. Their example became a classic: to play a Beethoven string quartet you need four musicians today and about as much time as was needed in 1800. The 'productivity' of music, if we can put it that way, has not increased at all."),
  L("Καθηγήτρια", "f", "Στο μεταξύ όμως, στη βιομηχανία, ένας εργάτης παράγει σήμερα πολλαπλάσια προϊόντα απ' ό,τι πριν από έναν αιώνα, και ο μισθός του ανεβαίνει ανάλογα. Αν οι μουσικοί δεν πληρώνονταν περίπου όσο οι άλλοι εργαζόμενοι, θα άλλαζαν επάγγελμα. Έτσι οι μισθοί τους ανεβαίνουν, χωρίς να ανεβαίνει η παραγωγικότητά τους, και το κόστος μιας συναυλίας αυξάνεται σταθερά σε σχέση με το κόστος των βιομηχανικών αγαθών.", "Meanwhile, though, in industry a worker today produces many times more goods than a century ago, and his wage rises accordingly. If musicians weren't paid roughly as much as other workers, they would change profession. So their wages rise without their productivity rising, and the cost of a concert grows steadily relative to the cost of industrial goods."),
  L("Καθηγήτρια", "f", "Το ίδιο φαινόμενο εξηγεί, κατά πολλούς οικονομολόγους, γιατί η εκπαίδευση και η υγεία γίνονται διαρκώς ακριβότερες: ένας δάσκαλος δεν μπορεί να διδάξει διπλάσιους μαθητές χωρίς να χειροτερέψει η διδασκαλία, ούτε μια νοσηλεύτρια να φροντίσει διπλάσιους ασθενείς. Ο ίδιος ο Μπόμολ υποστήριζε ότι αυτό δεν είναι λόγος πανικού: μια κοινωνία που γίνεται πλουσιότερη μπορεί να αντέξει ακριβότερες υπηρεσίες. Το λάθος θα ήταν να ερμηνεύουμε το αυξανόμενο κόστος ως απόδειξη ότι οι υπηρεσίες αυτές λειτουργούν απαραίτητα χειρότερα.", "The same phenomenon explains, according to many economists, why education and health keep getting more expensive: a teacher can't teach twice as many pupils without teaching getting worse, nor can a nurse look after twice as many patients. Baumol himself argued that this is no reason to panic: a society that grows richer can afford more expensive services. The mistake would be to interpret the rising cost as proof that these services necessarily work worse."),
 ],
 "questions": [
  Q("Τι δείχνει το παράδειγμα με το κουαρτέτο του Μπετόβεν;", ["Ότι η κλασική μουσική χάνει το κοινό της", "Ότι η παραγωγικότητα της μουσικής δεν έχει αυξηθεί", "Ότι οι μουσικοί σήμερα παίζουν πιο γρήγορα", "Ότι τα κουαρτέτα χρειάζονται περισσότερους μουσικούς"], 1, "δεν έχει αυξηθεί καθόλου"),
  Q("Γιατί ανεβαίνουν οι μισθοί των μουσικών;", ["Γιατί πουλιούνται περισσότερα εισιτήρια", "Γιατί το κράτος τους επιδοτεί", "Γιατί αλλιώς θα άλλαζαν επάγγελμα", "Γιατί παίζουν περισσότερες συναυλίες"], 2, "θα άλλαζαν επάγγελμα"),
  Q("Ποιους άλλους τομείς εξηγεί, κατά πολλούς, το ίδιο φαινόμενο;", ["Την εκπαίδευση και την υγεία", "Τη γεωργία και την αλιεία", "Τη βιομηχανία αυτοκινήτων", "Το εμπόριο"], 0, "γιατί η εκπαίδευση και η υγεία γίνονται διαρκώς ακριβότερες"),
  Q("Ποια ήταν η στάση του ίδιου του Μπόμολ;", ["Ότι οι υπηρεσίες αυτές πρέπει να ιδιωτικοποιηθούν", "Ότι οι μισθοί πρέπει να παγώσουν", "Ότι η τεχνολογία θα λύσει γρήγορα το πρόβλημα", "Ότι μια κοινωνία που γίνεται πλουσιότερη μπορεί να αντέξει ακριβότερες υπηρεσίες"], 3, "μια κοινωνία που γίνεται πλουσιότερη μπορεί να αντέξει ακριβότερες υπηρεσίες"),
 ],
 "gloss": {"διάλεξη": "διάλεξη — lecture", "παραστατικών τεχνών": "παραστατικές τέχνες — performing arts", "έμελλε": "μέλλει — was destined to", "κουαρτέτο": "κουαρτέτο — quartet", "εγχόρδων": "έγχορδα — string instruments", "παραγωγικότητα": "παραγωγικότητα — productivity", "πολλαπλάσια": "πολλαπλάσιος — many times more", "αγαθών": "αγαθό — good, commodity", "διπλάσιους": "διπλάσιος — twice as many", "αντέξει": "αντέχω — to afford, bear", "ερμηνεύουμε": "ερμηνεύω — to interpret"}
})

ITEMS.append({
 "id": "l142-c1-braess", "title": "Ένας δρόμος παραπάνω, μια καθυστέρηση παραπάνω", "title_en": "One more road, one more delay", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια επιστημονική εκπομπή στο ραδιόφωνο.",
 "script": [
  L("Δημοσιογράφος", "m", "Λένε ότι μερικές φορές, αν κλείσεις έναν δρόμο, η κυκλοφορία βελτιώνεται. Ακούγεται παράλογο.", "They say that sometimes, if you close a road, traffic improves. It sounds absurd."),
  L("Μαθηματικός", "f", "Κι όμως, έχει όνομα: το παράδοξο του Μπρες. Το περιέγραψε το 1968 ο Γερμανός μαθηματικός Ντίτριχ Μπρες. Έδειξε, με ένα απλό μοντέλο, ότι αν προσθέσεις σε ένα οδικό δίκτυο έναν καινούργιο, γρήγορο δρόμο, μπορεί ο χρόνος διαδρομής να αυξηθεί για όλους τους οδηγούς. Το κλειδί είναι ότι ο καθένας διαλέγει τη διαδρομή που συμφέρει τον ίδιο, χωρίς να λογαριάζει την επίδραση που έχει η επιλογή του στους άλλους.", "And yet it has a name: Braess's paradox. It was described in 1968 by the German mathematician Dietrich Braess. He showed, with a simple model, that if you add a new, fast road to a road network, travel time can increase for all drivers. The key is that each person chooses the route that suits them, without taking into account the effect their choice has on others."),
  L("Δημοσιογράφος", "m", "Δηλαδή όλοι πέφτουν πάνω στον ίδιο «έξυπνο» δρόμο.", "So everyone piles onto the same 'clever' road."),
  L("Μαθηματικός", "f", "Ακριβώς. Ο νέος δρόμος γεμίζει, μποτιλιάρεται, και καταλήγουμε σε μια κατάσταση όπου κανείς δεν έχει λόγο να αλλάξει διαδρομή μόνος του, αλλά όλοι θα ήταν καλύτερα αν ο δρόμος δεν υπήρχε. Στην οικονομία αυτό λέγεται ισορροπία Νας. Συχνά αναφέρεται το παράδειγμα της Σεούλ, όπου στις αρχές της δεκαετίας του 2000 γκρεμίστηκε ένας υπερυψωμένος αυτοκινητόδρομος για να αποκατασταθεί ένα ρέμα, και, σύμφωνα με τις αναφορές, η κυκλοφορία δεν χειροτέρεψε. Βέβαια, οι πραγματικές πόλεις είναι πολύ πιο σύνθετες από ένα μοντέλο, και το παράδοξο δεν σημαίνει ότι κάθε νέος δρόμος είναι κακή ιδέα. Σημαίνει ότι η διαίσθηση «περισσότερη χωρητικότητα, λιγότερη κίνηση» δεν είναι νόμος της φύσης.", "Exactly. The new road fills up, gets jammed, and we end up in a situation where nobody has a reason to change route on their own, but everyone would be better off if the road didn't exist. In economics this is called a Nash equilibrium. The example of Seoul is often cited, where in the early 2000s an elevated motorway was demolished to restore a stream, and, according to reports, traffic did not get worse. Of course, real cities are far more complex than a model, and the paradox doesn't mean that every new road is a bad idea. It means that the intuition 'more capacity, less traffic' is not a law of nature."),
 ],
 "questions": [
  Q("Τι έδειξε ο Μπρες με το μοντέλο του;", ["Ότι οι οδηγοί προτιμούν πάντα τον συντομότερο δρόμο", "Ότι ένας νέος γρήγορος δρόμος μπορεί να αυξήσει τον χρόνο διαδρομής για όλους", "Ότι τα φανάρια μειώνουν την κίνηση", "Ότι τα δίκτυα λειτουργούν καλύτερα με λιγότερα αυτοκίνητα"], 1, "μπορεί ο χρόνος διαδρομής να αυξηθεί για όλους τους οδηγούς"),
  Q("Ποιο είναι, κατά τη μαθηματικό, το «κλειδί» του παραδόξου;", ["Ο καθένας διαλέγει τη διαδρομή που συμφέρει τον ίδιο, χωρίς να λογαριάζει τους άλλους", "Οι οδηγοί δεν γνωρίζουν τους δρόμους", "Οι μηχανικοί σχεδιάζουν κακά τους δρόμους", "Οι δρόμοι είναι πολύ στενοί"], 0, "ο καθένας διαλέγει τη διαδρομή που συμφέρει τον ίδιο"),
  Q("Τι αναφέρεται για τη Σεούλ;", ["Χτίστηκε ένας νέος αυτοκινητόδρομος και η κίνηση μειώθηκε", "Απαγορεύτηκαν τα αυτοκίνητα στο κέντρο", "Γκρεμίστηκε ένας υπερυψωμένος αυτοκινητόδρομος και, σύμφωνα με τις αναφορές, η κυκλοφορία δεν χειροτέρεψε", "Το ρέμα καλύφθηκε για να γίνει δρόμος"], 2, "η κυκλοφορία δεν χειροτέρεψε"),
  Q("Ποιο συμπέρασμα βγάζει η μαθηματικός;", ["Ότι κάθε νέος δρόμος είναι κακή ιδέα", "Ότι τα μοντέλα δεν έχουν καμία αξία", "Ότι πρέπει να κλείσουν όλοι οι αυτοκινητόδρομοι", "Ότι η διαίσθηση «περισσότερη χωρητικότητα, λιγότερη κίνηση» δεν είναι νόμος της φύσης"], 3, "δεν είναι νόμος της φύσης"),
 ],
 "gloss": {"παράλογο": "παράλογος — absurd", "οδικό δίκτυο": "οδικό δίκτυο — road network", "διαδρομής": "διαδρομή — route, journey", "συμφέρει": "συμφέρει — it suits, is advantageous", "λογαριάζει": "λογαριάζω — to take into account", "μποτιλιάρεται": "μποτιλιάρομαι — to get jammed", "ισορροπία": "ισορροπία — equilibrium", "υπερυψωμένος": "υπερυψωμένος — elevated", "αποκατασταθεί": "αποκαθίσταμαι — to be restored", "ρέμα": "ρέμα — stream", "διαίσθηση": "διαίσθηση — intuition", "χωρητικότητα": "χωρητικότητα — capacity"}
})

rnd = random.Random(142)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-142.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
