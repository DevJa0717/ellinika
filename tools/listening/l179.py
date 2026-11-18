# Source for library/listening/listening-179.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l179.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l179-ann-allagi-solista", "title": "Αλλαγή σολίστ πριν από τη συναυλία", "title_en": "A change of soloist before the concert", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στο φουαγιέ μιας αίθουσας συναυλιών, λίγο πριν αρχίσει μια συναυλία κλασικής μουσικής.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητό κοινό, καλησπέρα σας. Λυπούμαστε που σας ανακοινώνουμε ότι η βιολονίστρια που θα ερμήνευε απόψε το κονσέρτο του Μέντελσον δεν θα μπορέσει να εμφανιστεί, λόγω ενός τραυματισμού στο χέρι της. Της ευχόμαστε ολόψυχα γρήγορη ανάρρωση.", "Dear audience, good evening. We regret to announce that the violinist who was to perform Mendelssohn's concerto tonight will not be able to appear, due to an injury to her hand. We wholeheartedly wish her a speedy recovery."),
  L("Εκφωνήτρια", "f", "Τη θέση της θα πάρει ο κορυφαίος της ορχήστρας μας, ο οποίος δέχτηκε να παίξει το ίδιο έργο με ειδοποίηση μόλις μίας ημέρας. Το υπόλοιπο πρόγραμμα παραμένει όπως είναι τυπωμένο. Η συναυλία θα αρχίσει με δέκα λεπτά καθυστέρηση.", "Her place will be taken by our orchestra's concertmaster, who agreed to play the same work at just one day's notice. The rest of the programme remains as printed. The concert will begin ten minutes late."),
  L("Εκφωνήτρια", "f", "Όσοι επιθυμούν, μπορούν να ζητήσουν επιστροφή του αντιτίμου του εισιτηρίου τους από το ταμείο, μόνο απόψε και μόνο πριν από την έναρξη. Σας παρακαλούμε, επίσης, να απενεργοποιήσετε τα κινητά σας τηλέφωνα. Σας ευχαριστούμε.", "Those who wish can request a refund of their ticket price from the box office, only tonight and only before the start. We also ask you to switch off your mobile phones. Thank you."),
 ],
 "questions": [
  Q("Γιατί δεν θα εμφανιστεί η βιολονίστρια;", ["Γιατί έχασε την πτήση της", "Λόγω τραυματισμού στο χέρι της", "Γιατί είναι κρυωμένη", "Γιατί άλλαξε το πρόγραμμα"], 1, "λόγω ενός τραυματισμού στο χέρι της"),
  Q("Ποιος θα παίξει στη θέση της;", ["Μια φοιτήτρια του ωδείου", "Ο μαέστρος", "Ο κορυφαίος της ορχήστρας", "Ένας πιανίστας"], 2, "Τη θέση της θα πάρει ο κορυφαίος της ορχήστρας μας"),
  Q("Πότε μπορεί κάποιος να ζητήσει επιστροφή χρημάτων;", ["Μόνο απόψε, πριν από την έναρξη", "Την επόμενη εβδομάδα", "Μετά το διάλειμμα", "Μέσω του διαδικτύου ως αύριο"], 0, "μόνο απόψε και μόνο πριν από την έναρξη"),
 ],
 "gloss": {"φουαγιέ": "φουαγιέ — foyer", "βιολονίστρια": "βιολονίστρια — violinist (f.)", "ερμήνευε": "ερμηνεύω — to perform, interpret", "κονσέρτο": "κονσέρτο — concerto", "τραυματισμού": "τραυματισμός — injury", "ολόψυχα": "ολόψυχα — wholeheartedly", "ανάρρωση": "ανάρρωση — recovery", "κορυφαίος της ορχήστρας": "κορυφαίος (της ορχήστρας) — concertmaster", "ειδοποίηση": "ειδοποίηση — notice", "αντιτίμου": "αντίτιμο — price, cost", "απενεργοποιήσετε": "απενεργοποιώ — to switch off"},
})

ITEMS.append({
 "id": "l179-int-astrofotografos", "title": "Ο αστροφωτογράφος", "title_en": "The astrophotographer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν ερασιτέχνη αστροφωτογράφο, του οποίου οι φωτογραφίες του νυχτερινού ουρανού έχουν βραβευτεί.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς ξεκινήσατε να φωτογραφίζετε τα αστέρια;", "How did you start photographing the stars?"),
  L("Αστροφωτογράφος", "m", "Εντελώς τυχαία. Ένα καλοκαίρι, σε ένα χωριό των Αγράφων, κόπηκε το ρεύμα και βγήκαμε όλοι στην αυλή. Πάνω από τα κεφάλια μας φαινόταν ο Γαλαξίας σαν ένα φωτεινό σύννεφο. Ήμουν σαράντα χρονών και δεν τον είχα δει ποτέ. Την επόμενη μέρα αγόρασα ένα τρίποδο.", "Completely by chance. One summer, in a village in the Agrafa mountains, the power went out and we all went out into the yard. Above our heads the Milky Way appeared like a bright cloud. I was forty and had never seen it. The next day I bought a tripod."),
  L("Δημοσιογράφος", "f", "Τι χρειάζεται για μια καλή φωτογραφία;", "What do you need for a good photograph?"),
  L("Αστροφωτογράφος", "m", "Πρώτα απ' όλα σκοτάδι, που είναι πια το πιο σπάνιο αγαθό. Από την Αθήνα, λόγω της φωτορύπανσης, βλέπεις ελάχιστα αστέρια. Οδηγώ συχνά τρεις ώρες για να βρω έναν ουρανό αρκετά σκοτεινό. Μετά χρειάζεται υπομονή: η μηχανή μένει ανοιχτή για πολλά δευτερόλεπτα, και πολλές φορές συνδυάζω δεκάδες λήψεις στον υπολογιστή για να βγει μία εικόνα. Και πρέπει να έχεις κοιτάξει το φεγγάρι· μια πανσέληνος μπορεί να καταστρέψει μια ολόκληρη νύχτα.", "First of all darkness, which is now the rarest commodity. From Athens, because of light pollution, you see very few stars. I often drive three hours to find a sky that's dark enough. Then you need patience: the camera stays open for many seconds, and I often combine dozens of shots on the computer to get one image. And you have to have checked the moon; a full moon can ruin a whole night."),
  L("Δημοσιογράφος", "f", "Ποια φωτογραφία αγαπάτε περισσότερο;", "Which photograph do you love most?"),
  L("Αστροφωτογράφος", "m", "Μια που τράβηξα πάνω από ένα ξωκλήσι στη Νάξο, με τον Γαλαξία να «βγαίνει» από το καμπαναριό. Την έστειλα σε μια ηλικιωμένη κυρία του χωριού, που ανάβει το καντήλι εκεί κάθε βράδυ. Μου είπε ότι τόσα χρόνια δεν είχε σηκώσει ποτέ τα μάτια της ψηλά. Από τότε, λέει, κάθε φορά που κλειδώνει το ξωκλήσι, κοιτάζει τον ουρανό.", "One I took above a chapel on Naxos, with the Milky Way 'coming out' of the bell tower. I sent it to an elderly lady in the village, who lights the oil lamp there every evening. She told me that in all those years she'd never raised her eyes upwards. Since then, she says, every time she locks the chapel, she looks at the sky."),
 ],
 "questions": [
  Q("Πώς ξεκίνησε να φωτογραφίζει τα αστέρια;", ["Από ένα μάθημα φωτογραφίας", "Όταν είδε τον Γαλαξία σε ένα χωριό, μια νύχτα που κόπηκε το ρεύμα", "Από ένα βιβλίο αστρονομίας", "Όταν του χάρισαν ένα τηλεσκόπιο"], 1, "κόπηκε το ρεύμα και βγήκαμε όλοι στην αυλή"),
  Q("Γιατί οδηγεί συχνά τρεις ώρες;", ["Για να συναντήσει άλλους αστροφωτογράφους", "Γιατί εκεί ο καιρός είναι πάντα καλός", "Για να βρει έναν ουρανό αρκετά σκοτεινό", "Γιατί εκεί βλέπει το φεγγάρι καλύτερα"], 2, "για να βρω έναν ουρανό αρκετά σκοτεινό"),
  Q("Τι άλλαξε για την ηλικιωμένη κυρία μετά τη φωτογραφία;", ["Κοιτάζει τον ουρανό κάθε φορά που κλειδώνει το ξωκλήσι", "Αγόρασε κι εκείνη μια φωτογραφική μηχανή", "Σταμάτησε να ανάβει το καντήλι", "Κρέμασε τη φωτογραφία στην εκκλησία"], 0, "κάθε φορά που κλειδώνει το ξωκλήσι, κοιτάζει τον ουρανό"),
 ],
 "gloss": {"αστροφωτογράφο": "αστροφωτογράφος — astrophotographer", "βραβευτεί": "βραβεύομαι — to be awarded", "Αγράφων": "Άγραφα — Agrafa (mountain region)", "Γαλαξίας": "Γαλαξίας — the Milky Way", "τρίποδο": "τρίποδο — tripod", "αγαθό": "αγαθό — good, commodity", "φωτορύπανσης": "φωτορύπανση — light pollution", "λήψεις": "λήψη — shot, exposure", "πανσέληνος": "πανσέληνος — full moon", "ξωκλήσι": "ξωκλήσι — country chapel", "καμπαναριό": "καμπαναριό — bell tower", "καντήλι": "καντήλι — oil lamp (before an icon)"},
})

ITEMS.append({
 "id": "l179-vm-gatakia-geitonissas", "title": "Μήνυμα από τη γειτόνισσα με τα γατάκια", "title_en": "A message from the neighbour with the kittens", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από μια γειτόνισσα, σχετικά με ένα γατάκι που της είχατε πει ότι ίσως θέλετε να υιοθετήσετε.",
 "script": [
  L("Γειτόνισσα", "f", "Γεια σου, η Αθηνά είμαι, από τον τρίτο. Θυμάσαι που μου είχες πει ότι, αν η Μπιλιό κάνει μικρά, θα ήθελες ένα; Ε, λοιπόν, πριν από επτά εβδομάδες γέννησε πέντε! Τρία τα έχουν ήδη κλείσει φίλοι μου, οπότε έμειναν δύο: ένα γκρίζο αρσενικό κι ένα τρίχρωμο θηλυκό.", "Hi, it's Athina, from the third floor. Remember you told me that, if Bilio had kittens, you'd like one? Well, seven weeks ago she had five! Three have already been claimed by friends of mine, so there are two left: a grey male and a tortoiseshell female."),
  L("Γειτόνισσα", "f", "Ο κτηνίατρος λέει ότι μπορούν να αποχωριστούν τη μητέρα τους όταν κλείσουν δέκα με δώδεκα εβδομάδες, δηλαδή σε έναν μήνα περίπου. Μέχρι τότε θα έχουν κάνει και το πρώτο εμβόλιο και αποπαρασίτωση. Το τσιπάκι και τη στείρωση, όμως, θα πρέπει να τα αναλάβεις εσύ αργότερα.", "The vet says they can leave their mother when they're ten to twelve weeks old, so in about a month. By then they'll have had their first vaccination and deworming too. The microchip and the neutering, though, you'll have to take care of yourself later."),
  L("Γειτόνισσα", "f", "Πέρνα όποτε θέλεις να τα δεις, συνήθως είμαι σπίτι μετά τις έξι. Και σκέψου αν θες να τα πάρεις και τα δύο· μαζί παίζουν και δεν βαριούνται όταν λείπεις. Τα λέμε!", "Come by whenever you want to see them, I'm usually home after six. And think about whether you want to take both; together they play and don't get bored when you're out. See you!"),
 ],
 "questions": [
  Q("Πόσα γατάκια είναι ακόμα διαθέσιμα;", ["Πέντε", "Δύο", "Τρία", "Ένα"], 1, "οπότε έμειναν δύο"),
  Q("Τι θα πρέπει να αναλάβει αργότερα ο νέος ιδιοκτήτης;", ["Το πρώτο εμβόλιο", "Την αποπαρασίτωση", "Το τσιπάκι και τη στείρωση", "Την εκπαίδευση στην άμμο"], 2, "Το τσιπάκι και τη στείρωση, όμως, θα πρέπει να τα αναλάβεις εσύ αργότερα"),
  Q("Γιατί προτείνει η Αθηνά να πάρει και τα δύο;", ["Γιατί μαζί παίζουν και δεν βαριούνται", "Γιατί είναι φθηνότερο", "Γιατί δεν θέλει να τα χωρίσει από τη μητέρα τους", "Γιατί κανείς άλλος δεν τα θέλει"], 0, "μαζί παίζουν και δεν βαριούνται όταν λείπεις"),
 ],
 "gloss": {"γατάκι": "γατάκι — kitten", "υιοθετήσετε": "υιοθετώ — to adopt", "κάνει μικρά": "κάνω μικρά — to have young", "τρίχρωμο": "τρίχρωμος — three-coloured, tortoiseshell", "αποχωριστούν": "αποχωρίζομαι — to part from", "εμβόλιο": "εμβόλιο — vaccine", "αποπαρασίτωση": "αποπαρασίτωση — deworming", "τσιπάκι": "τσιπάκι — microchip", "στείρωση": "στείρωση — neutering, sterilisation", "βαριούνται": "βαριέμαι — to get bored"},
})

ITEMS.append({
 "id": "l179-mon-ellispontos", "title": "Κολυμπώντας από την Ευρώπη στην Ασία", "title_en": "Swimming from Europe to Asia", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια ερασιτέχνιδα κολυμβήτρια να διηγείται πώς διέσχισε τα Δαρδανέλια, το στενό που χωρίζει την Ευρώπη από την Ασία.",
 "script": [
  L("Κολυμβήτρια", "f", "Τον μύθο τον ήξερα από το σχολείο: ο Λέανδρος κολυμπούσε κάθε νύχτα τον Ελλήσποντο για να δει την αγαπημένη του, την Ηρώ, ώσπου μια καταιγίδα έσβησε τη λάμπα που του έδειχνε τον δρόμο. Αιώνες αργότερα, ο λόρδος Βύρων τον διέσχισε κι αυτός, για να αποδείξει ότι γίνεται. Όταν έμαθα ότι κάθε καλοκαίρι οργανώνεται εκεί ένας αγώνας για ερασιτέχνες, είπα: «Γιατί όχι κι εγώ;»", "I knew the myth from school: Leander swam the Hellespont every night to see his beloved, Hero, until a storm put out the lamp that showed him the way. Centuries later, Lord Byron crossed it too, to prove it could be done. When I found out that every summer a race for amateurs is organised there, I said: 'Why not me too?'"),
  L("Κολυμβήτρια", "f", "Η απόσταση δεν είναι τεράστια, γύρω στα τεσσερισήμισι χιλιόμετρα. Το δύσκολο είναι τα ρεύματα. Το νερό κινείται συνεχώς από τη Μαύρη Θάλασσα προς το Αιγαίο, και αν κολυμπήσεις ευθεία προς την απέναντι ακτή, το ρεύμα σε παρασύρει και χάνεις τον τερματισμό. Γι' αυτό προπονήθηκα έναν χρόνο σε ανοιχτή θάλασσα, όχι σε πισίνα.", "The distance isn't huge, around four kilometres. The hard part is the currents. The water moves constantly from the Black Sea towards the Aegean, and if you swim straight towards the opposite shore, the current carries you away and you miss the finish. That's why I trained for a year in open sea, not in a pool."),
  L("Κολυμβήτρια", "f", "Τη μέρα του αγώνα, γύρω στη μέση του στενού, κοίταξα δεξιά και είδα ένα τεράστιο φορτηγό πλοίο να περνάει, σταματημένη η κυκλοφορία για χάρη μας. Τερμάτισα σε μία ώρα και είκοσι λεπτά. Δεν ήρθα πρώτη, ούτε καν στις πρώτες εκατό. Όταν όμως πάτησα στην ακτή της Ασίας, έκλαιγα σαν μικρό παιδί.", "On race day, around the middle of the strait, I looked right and saw a huge cargo ship passing, with traffic stopped for our sake. I finished in an hour and twenty minutes. I didn't come first, not even in the first hundred. But when I set foot on the Asian shore, I was crying like a little child."),
 ],
 "questions": [
  Q("Γιατί διέσχισε ο λόρδος Βύρων τον Ελλήσποντο κατά την κολυμβήτρια;", ["Για να δει την αγαπημένη του", "Για να αποδείξει ότι γίνεται", "Για έναν αγώνα", "Για να σώσει κάποιον"], 1, "για να αποδείξει ότι γίνεται"),
  Q("Ποιο είναι, κατά την ίδια, το πιο δύσκολο;", ["Η απόσταση", "Η θερμοκρασία του νερού", "Τα ρεύματα", "Τα πλοία"], 2, "Το δύσκολο είναι τα ρεύματα"),
  Q("Πώς προετοιμάστηκε;", ["Προπονήθηκε έναν χρόνο σε ανοιχτή θάλασσα", "Κολυμπούσε κάθε μέρα σε πισίνα", "Έκανε μαθήματα με προπονητή στην Τουρκία", "Έτρεχε στο βουνό"], 0, "προπονήθηκα έναν χρόνο σε ανοιχτή θάλασσα, όχι σε πισίνα"),
 ],
 "gloss": {"ερασιτέχνιδα": "ερασιτέχνιδα — amateur (f.)", "διέσχισε": "διασχίζω — to cross", "Δαρδανέλια": "Δαρδανέλια — the Dardanelles", "στενό": "στενό — strait", "Ελλήσποντο": "Ελλήσποντος — Hellespont", "λόρδος Βύρων": "λόρδος Βύρων — Lord Byron", "ρεύματα": "ρεύμα — current", "παρασύρει": "παρασύρω — to sweep away", "τερματισμό": "τερματισμός — finish (line)", "προπονήθηκα": "προπονούμαι — to train", "για χάρη μας": "για χάρη μου — for my sake"},
})

ITEMS.append({
 "id": "l179-dia-kafetiera-grafeiou", "title": "Μια καφετιέρα για το γραφείο", "title_en": "A coffee machine for the office", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο συναδέλφους να συζητούν αν θα αγοράσουν μια κοινή καφετιέρα για το γραφείο τους.",
 "script": [
  L("Πέτρος", "m", "Έκανα έναν λογαριασμό χθες: δίνω πάνω από εξήντα ευρώ τον μήνα σε καφέδες από την καφετέρια απέναντι. Αν είμαστε οκτώ στο γραφείο, φαντάσου πόσα πάνε όλοι μαζί.", "I did a calculation yesterday: I spend over sixty euros a month on coffees from the café opposite. If there are eight of us in the office, imagine how much goes on it all together."),
  L("Μαρίνα", "f", "Προτείνεις να πάρουμε μια μηχανή; Το έχουμε ξανασυζητήσει. Το πρόβλημα δεν είναι η αγορά, είναι ποιος θα την καθαρίζει. Στην προηγούμενη δουλειά μου, σε δύο μήνες είχε γίνει πειραματικό εργαστήριο για μούχλα.", "You're suggesting we get a machine? We've discussed it before. The problem isn't buying it, it's who'll clean it. In my previous job, within two months it had become an experimental lab for mould."),
  L("Πέτρος", "m", "Το σκέφτηκα. Βάζουμε ένα πρόγραμμα στο ψυγείο: κάθε εβδομάδα ένας άλλος υπεύθυνος. Και ένα κουτί για τον καφέ: δέκα ευρώ ο καθένας τον μήνα. Ακόμα κι έτσι, βγαίνουμε πολύ πιο φτηνά.", "I've thought about it. We put a rota on the fridge: a different person in charge every week. And a box for the coffee: ten euros each a month. Even so, it works out much cheaper."),
  L("Μαρίνα", "f", "Και ο Στάθης, που πίνει μόνο τσάι; Και η Κατερίνα, που θέλει πάντα φρέντο με αφρόγαλα;", "And Stathis, who only drinks tea? And Katerina, who always wants a freddo with milk froth?"),
  L("Πέτρος", "m", "Ο Στάθης δεν θα πληρώνει, προφανώς. Για την Κατερίνα, παίρνουμε μια μηχανή που φτιάχνει και αφρόγαλα. Υπάρχουν καλές μεταχειρισμένες στο διαδίκτυο.", "Stathis won't pay, obviously. For Katerina, we get a machine that also makes milk froth. There are good second-hand ones online."),
  L("Μαρίνα", "f", "Εντάξει, με έπεισες. Αλλά με μία προϋπόθεση: την πρώτη εβδομάδα καθαρισμού την αναλαμβάνεις εσύ. Για να δούμε αν το εννοείς.", "All right, you've convinced me. But on one condition: you take on the first week of cleaning. So we can see if you mean it."),
 ],
 "questions": [
  Q("Πόσα ξοδεύει ο Πέτρος τον μήνα σε καφέδες;", ["Δέκα ευρώ", "Πάνω από εξήντα ευρώ", "Οκτώ ευρώ", "Εκατό ευρώ"], 1, "δίνω πάνω από εξήντα ευρώ τον μήνα"),
  Q("Ποιο είναι, κατά τη Μαρίνα, το πρόβλημα;", ["Η τιμή της μηχανής", "Ότι δεν υπάρχει χώρος", "Ποιος θα καθαρίζει τη μηχανή", "Ότι ο καφές της μηχανής δεν είναι καλός"], 2, "Το πρόβλημα δεν είναι η αγορά, είναι ποιος θα την καθαρίζει"),
  Q("Με ποια προϋπόθεση συμφωνεί η Μαρίνα;", ["Ο Πέτρος να αναλάβει την πρώτη εβδομάδα καθαρισμού", "Να πληρώσει ο Πέτρος τη μηχανή", "Να πίνει και ο Στάθης καφέ", "Να πάρουν καινούργια μηχανή"], 0, "την πρώτη εβδομάδα καθαρισμού την αναλαμβάνεις εσύ"),
 ],
 "gloss": {"καφετιέρα": "καφετιέρα — coffee maker", "συναδέλφους": "συνάδελφος — colleague", "έναν λογαριασμό": "κάνω έναν λογαριασμό — to do a calculation", "πειραματικό εργαστήριο": "πειραματικό εργαστήριο — experimental lab", "μούχλα": "μούχλα — mould", "υπεύθυνος": "υπεύθυνος — person in charge", "βγαίνουμε πολύ πιο φτηνά": "βγαίνω φτηνά — to come out cheap", "αφρόγαλα": "αφρόγαλα — milk froth", "μεταχειρισμένες": "μεταχειρισμένος — second-hand", "με έπεισες": "πείθω — to convince", "προϋπόθεση": "προϋπόθεση — condition, prerequisite"},
})

ITEMS.append({
 "id": "l179-rep-giorti-skiachtron", "title": "Η γιορτή των σκιάχτρων", "title_en": "The scarecrow festival", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ραδιοφωνικό ρεπορτάζ για ένα ορεινό χωριό που κάθε φθινόπωρο γεμίζει σκιάχτρα.",
 "script": [
  L("Ρεπόρτερ", "m", "Στην είσοδο του χωριού σε υποδέχεται ένας παπάς από άχυρο, με μαύρο ράσο και γυαλιά ηλίου. Λίγο πιο κάτω, ένας ποδοσφαιριστής κλωτσάει μια κολοκύθα, και στο μπαλκόνι του καφενείου δύο σκιάχτρα παίζουν τάβλι. Σήμερα στο χωριό ζουν περίπου ογδόντα άνθρωποι, αλλά αυτή την εβδομάδα τα σκιάχτρα είναι διπλάσια.", "At the entrance to the village you're greeted by a priest made of straw, with a black cassock and sunglasses. A little further down, a footballer is kicking a pumpkin, and on the café balcony two scarecrows are playing backgammon. Today about eighty people live in the village, but this week there are twice as many scarecrows."),
  L("Πρόεδρος συλλόγου", "f", "Η ιδέα ήρθε πριν από έξι χρόνια, όταν κλείσαμε το σχολείο γιατί δεν είχε πια παιδιά. Θέλαμε κάτι να φέρει ξανά κόσμο εδώ. Κάθε οικογένεια φτιάχνει ένα σκιάχτρο με παλιά ρούχα και άχυρο από τα χωράφια, και οι επισκέπτες ψηφίζουν το καλύτερο. Πέρσι κέρδισε η γιαγιά Λενιώ με ένα σκιάχτρο που έμοιαζε απίστευτα με τον δήμαρχο.", "The idea came six years ago, when we closed the school because it no longer had any children. We wanted something to bring people here again. Every family makes a scarecrow with old clothes and straw from the fields, and the visitors vote for the best. Last year grandma Lenio won with a scarecrow that looked incredibly like the mayor."),
  L("Ρεπόρτερ", "m", "Το Σαββατοκύριακο της γιορτής οι κάτοικοι πουλάνε μέλι, τραχανά και πλεκτά, και τα έσοδα πηγαίνουν στην επισκευή της εκκλησίας. Κάποιοι επισκέπτες έρχονται κάθε χρόνο, και δύο οικογένειες από την Αθήνα αγόρασαν μάλιστα σπίτια στο χωριό. «Τα σκιάχτρα», λέει γελώντας η πρόεδρος, «αντί να διώχνουν, μας φέρνουν κόσμο».", "On the festival weekend the residents sell honey, trahanas and knitwear, and the proceeds go to repairing the church. Some visitors come every year, and two families from Athens have even bought houses in the village. 'The scarecrows,' the president says laughing, 'instead of chasing people away, bring them to us.'"),
 ],
 "questions": [
  Q("Πόσοι άνθρωποι ζουν σήμερα στο χωριό;", ["Περίπου σαράντα", "Περίπου ογδόντα", "Περίπου διακόσιοι", "Κανένας τον χειμώνα"], 1, "Σήμερα στο χωριό ζουν περίπου ογδόντα άνθρωποι"),
  Q("Πότε γεννήθηκε η ιδέα της γιορτής;", ["Όταν ήρθε ένας νέος δήμαρχος", "Μετά από μια καλή σοδειά", "Όταν έκλεισε το σχολείο γιατί δεν είχε παιδιά", "Όταν επισκευάστηκε η εκκλησία"], 2, "όταν κλείσαμε το σχολείο γιατί δεν είχε πια παιδιά"),
  Q("Πού πηγαίνουν τα έσοδα της γιορτής;", ["Στην επισκευή της εκκλησίας", "Στο σχολείο", "Στον δήμο", "Στους νικητές"], 0, "τα έσοδα πηγαίνουν στην επισκευή της εκκλησίας"),
 ],
 "gloss": {"σκιάχτρα": "σκιάχτρο — scarecrow", "άχυρο": "άχυρο — straw", "ράσο": "ράσο — cassock", "κλωτσάει": "κλωτσάω — to kick", "κολοκύθα": "κολοκύθα — pumpkin", "διπλάσια": "διπλάσιος — double, twice as many", "ψηφίζουν": "ψηφίζω — to vote", "τραχανά": "τραχανάς — trahanas (dried grain and milk pasta)", "πλεκτά": "πλεκτά — knitwear", "έσοδα": "έσοδα — proceeds, income"},
})

ITEMS.append({
 "id": "l179-news-isychi-ora-souper-market", "title": "Η «ήσυχη ώρα» στα σούπερ μάρκετ", "title_en": "The 'quiet hour' in supermarkets", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση σε έναν ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνητής", "m", "Μια αλυσίδα σούπερ μάρκετ ανακοίνωσε ότι από τον επόμενο μήνα θα καθιερώσει σε όλα της τα καταστήματα μια «ήσυχη ώρα», κάθε Τρίτη και Πέμπτη από τις δύο ως τις τρεις το μεσημέρι. Η πρωτοβουλία απευθύνεται κυρίως σε άτομα στο φάσμα του αυτισμού, που συχνά νιώθουν έντονη δυσφορία από τον θόρυβο και τα δυνατά φώτα.", "A supermarket chain has announced that from next month it will introduce a 'quiet hour' in all its stores, every Tuesday and Thursday from two to three in the afternoon. The initiative is aimed mainly at people on the autism spectrum, who often feel intense discomfort from noise and bright lights."),
  L("Εκφωνητής", "m", "Κατά τη διάρκεια της ήσυχης ώρας, η μουσική θα σβήνει, τα φώτα θα χαμηλώνουν όσο το επιτρέπουν οι κανόνες ασφαλείας, και οι ανακοινώσεις από τα μεγάφωνα θα σταματούν. Οι υπάλληλοι δεν θα γεμίζουν τα ράφια με καρότσια, και στα ταμεία θα έχει κλειστεί ο ήχος των σαρωτών.", "During the quiet hour, the music will be switched off, the lights will be dimmed as far as safety rules allow, and the loudspeaker announcements will stop. Staff won't restock the shelves with trolleys, and at the checkouts the sound of the scanners will be turned off."),
  L("Εκφωνητής", "m", "Σύλλογοι γονέων χαιρέτισαν την απόφαση, αλλά ζήτησαν να υπάρξει και εκπαίδευση των υπαλλήλων, ώστε να ξέρουν πώς να βοηθήσουν έναν πελάτη που έχει αγχωθεί. Η εταιρεία δήλωσε ότι το πρόγραμμα εκπαίδευσης θα ξεκινήσει μέσα στο φθινόπωρο.", "Parents' associations welcomed the decision, but asked that there also be staff training, so they know how to help a customer who has become anxious. The company stated that the training programme will start during the autumn."),
 ],
 "questions": [
  Q("Πότε θα ισχύει η «ήσυχη ώρα»;", ["Κάθε μέρα το πρωί", "Κάθε Τρίτη και Πέμπτη, από τις δύο ως τις τρεις", "Μόνο τα Σάββατα", "Κάθε Δευτέρα βράδυ"], 1, "κάθε Τρίτη και Πέμπτη από τις δύο ως τις τρεις το μεσημέρι"),
  Q("Ποιο από τα παρακάτω ΔΕΝ θα γίνεται κατά την ήσυχη ώρα;", ["Θα σβήνει η μουσική", "Θα χαμηλώνουν τα φώτα", "Θα κλείνουν τα ταμεία", "Θα σταματούν οι ανακοινώσεις"], 2, "η μουσική θα σβήνει, τα φώτα θα χαμηλώνουν"),
  Q("Τι ζήτησαν οι σύλλογοι γονέων;", ["Εκπαίδευση των υπαλλήλων", "Περισσότερες ήσυχες ώρες", "Εκπτώσεις για τις οικογένειες", "Ειδικά καρότσια"], 0, "ζήτησαν να υπάρξει και εκπαίδευση των υπαλλήλων"),
 ],
 "gloss": {"αλυσίδα": "αλυσίδα — chain", "καθιερώσει": "καθιερώνω — to establish, introduce", "πρωτοβουλία": "πρωτοβουλία — initiative", "απευθύνεται": "απευθύνομαι — to be aimed at", "φάσμα του αυτισμού": "φάσμα του αυτισμού — autism spectrum", "δυσφορία": "δυσφορία — discomfort", "ράφια": "ράφι — shelf", "ταμεία": "ταμείο — checkout, till", "σαρωτών": "σαρωτής — scanner", "χαιρέτισαν": "χαιρετίζω — to welcome (a decision)", "αγχωθεί": "αγχώνομαι — to get anxious"},
})

ITEMS.append({
 "id": "l179-int-touristiki-astynomia", "title": "Μια μέρα με την τουριστική αστυνομία", "title_en": "A day with the tourist police", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια αστυνομικό της τουριστικής αστυνομίας σε ένα μεγάλο νησί των Κυκλάδων.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι διαφέρει η τουριστική αστυνομία από την υπόλοιπη αστυνομία;", "How does the tourist police differ from the rest of the police?"),
  L("Αστυνομικός", "f", "Ασχολούμαστε κυρίως με προβλήματα που αφορούν επισκέπτες: χαμένα διαβατήρια, κλοπές, διαφωνίες με καταστήματα ή με ενοικιαστήρια αυτοκινήτων. Όλοι μας μιλάμε τουλάχιστον δύο ξένες γλώσσες. Εγώ μιλάω αγγλικά και ιταλικά, και τα τελευταία χρόνια μαθαίνω και λίγα πολωνικά, γιατί έρχονται πολλοί Πολωνοί.", "We deal mainly with problems that concern visitors: lost passports, thefts, disputes with shops or car-hire agencies. All of us speak at least two foreign languages. I speak English and Italian, and in recent years I've been learning a little Polish too, because a lot of Poles come."),
  L("Δημοσιογράφος", "m", "Ποιο είναι το πιο συνηθισμένο πρόβλημα;", "What's the most common problem?"),
  L("Αστυνομικός", "f", "Οι υπερβολικές χρεώσεις. Ένας πελάτης παραγγέλνει ψάρι χωρίς να ρωτήσει την τιμή και μετά βλέπει λογαριασμό εκατόν πενήντα ευρώ. Ελέγχουμε αν η τιμή ανά κιλό ήταν γραμμένη στον κατάλογο και αν ζυγίστηκε το ψάρι μπροστά του. Αν όχι, ο καταστηματάρχης έχει πρόβλημα. Συμβουλεύω πάντα τους επισκέπτες: ζητάτε να δείτε το ψάρι στη ζυγαριά.", "Excessive charges. A customer orders fish without asking the price and then sees a bill for a hundred and fifty euros. We check whether the price per kilo was written on the menu and whether the fish was weighed in front of him. If not, the owner has a problem. I always advise visitors: ask to see the fish on the scales."),
  L("Δημοσιογράφος", "m", "Θυμάστε κάποια περίπτωση με χαρούμενο τέλος;", "Do you remember a case with a happy ending?"),
  L("Αστυνομικός", "f", "Μια Ιαπωνέζα έχασε ένα σημειωματάριο με σκίτσα που είχε κάνει σε όλο το ταξίδι. Ήταν απαρηγόρητη. Το βρήκε ένας ψαράς δύο μέρες αργότερα στο λιμάνι και μας το έφερε. Της το στείλαμε στο Τόκιο. Μας απάντησε με ένα σκίτσο του αστυνομικού τμήματος, που το έχουμε κρεμάσει στον τοίχο.", "A Japanese woman lost a notebook with sketches she had made throughout her trip. She was inconsolable. A fisherman found it two days later at the harbour and brought it to us. We sent it to her in Tokyo. She replied with a sketch of the police station, which we've hung on the wall."),
 ],
 "questions": [
  Q("Γιατί μαθαίνει η αστυνομικός πολωνικά;", ["Γιατί το απαιτεί η υπηρεσία", "Γιατί έρχονται πολλοί Πολωνοί", "Γιατί έχει συγγενείς στην Πολωνία", "Για να διαβάζει βιβλία"], 1, "γιατί έρχονται πολλοί Πολωνοί"),
  Q("Τι συμβουλεύει τους επισκέπτες για το ψάρι;", ["Να μην παραγγέλνουν ψάρι", "Να τρώνε μόνο σε μεγάλα εστιατόρια", "Να ζητούν να δουν το ψάρι στη ζυγαριά", "Να πληρώνουν πάντα με κάρτα"], 2, "ζητάτε να δείτε το ψάρι στη ζυγαριά"),
  Q("Τι έστειλε η Ιαπωνέζα στην αστυνομία;", ["Ένα σκίτσο του αστυνομικού τμήματος", "Ένα γράμμα ευχαριστίας", "Ένα δώρο για τον ψαρά", "Το σημειωματάριό της"], 0, "Μας απάντησε με ένα σκίτσο του αστυνομικού τμήματος"),
 ],
 "gloss": {"τουριστικής αστυνομίας": "τουριστική αστυνομία — tourist police", "διαβατήρια": "διαβατήριο — passport", "κλοπές": "κλοπή — theft", "ενοικιαστήρια αυτοκινήτων": "ενοικιαστήριο αυτοκινήτων — car-hire agency", "υπερβολικές χρεώσεις": "υπερβολική χρέωση — overcharging", "ζυγίστηκε": "ζυγίζομαι — to be weighed", "καταστηματάρχης": "καταστηματάρχης — shop owner", "ζυγαριά": "ζυγαριά — scales", "σημειωματάριο": "σημειωματάριο — notebook", "σκίτσα": "σκίτσο — sketch", "απαρηγόρητη": "απαρηγόρητος — inconsolable"},
})

ITEMS.append({
 "id": "l179-c1-ntezavou", "title": "Τι είναι το «ντεζαβού»;", "title_en": "What is déjà vu?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια νευροψυχολόγο να εξηγεί σε μια εκπομπή τι γνωρίζουμε σήμερα για το φαινόμενο του «ήδη ειδωμένου».",
 "script": [
  L("Παρουσιάστρια", "f", "Όλοι το έχουμε ζήσει: μπαίνουμε σε ένα δωμάτιο για πρώτη φορά και νιώθουμε, με απόλυτη βεβαιότητα, ότι έχουμε ξαναβρεθεί εκεί. Τι συμβαίνει;", "We've all experienced it: we walk into a room for the first time and feel, with absolute certainty, that we've been there before. What's happening?"),
  L("Νευροψυχολόγος", "f", "Το πρώτο που πρέπει να πούμε είναι ότι το ντεζαβού δεν είναι ανάμνηση, αλλά αίσθηση οικειότητας χωρίς ανάμνηση. Ο εγκέφαλος μάς λέει «αυτό το ξέρεις», αλλά όταν ψάχνουμε πότε και πού το ζήσαμε, δεν βρίσκουμε τίποτα. Και, κάτι σημαντικό, συνήθως γνωρίζουμε ταυτόχρονα ότι η αίσθηση είναι λανθασμένη. Αυτή η σύγκρουση είναι που το κάνει τόσο παράξενο.", "The first thing we must say is that déjà vu is not a memory, but a feeling of familiarity without a memory. The brain tells us 'you know this', but when we search for when and where we lived it, we find nothing. And, importantly, we usually know at the same time that the feeling is wrong. This conflict is what makes it so strange."),
  L("Παρουσιάστρια", "f", "Υπάρχει κάποια εξήγηση;", "Is there an explanation?"),
  L("Νευροψυχολόγος", "f", "Υπάρχουν αρκετές υποθέσεις, καμία οριστική. Μία είναι ότι ο νέος χώρος μοιάζει στη διάταξή του με κάποιον που έχουμε δει αλλά έχουμε ξεχάσει· σε πειράματα με εικονικά περιβάλλοντα, οι συμμετέχοντες ανέφεραν συχνότερα ντεζαβού όταν ένα νέο σκηνικό είχε την ίδια διάταξη με ένα παλιό. Μια άλλη άποψη βλέπει το φαινόμενο σαν ένα είδος «ελέγχου» της μνήμης: ένα τμήμα του εγκεφάλου εντοπίζει ένα λάθος σήμα οικειότητας και μας το επισημαίνει.", "There are several hypotheses, none definitive. One is that the new space resembles in its layout one we've seen but forgotten; in experiments with virtual environments, participants reported déjà vu more often when a new scene had the same layout as an old one. Another view sees the phenomenon as a kind of memory 'check': a part of the brain detects a false signal of familiarity and points it out to us."),
  L("Νευροψυχολόγος", "f", "Είναι πιο συχνό στους νέους και μειώνεται με την ηλικία, κάτι που ίσως ταιριάζει με τη δεύτερη ερμηνεία. Σε σπάνιες περιπτώσεις, πολύ συχνά και έντονα επεισόδια μπορεί να συνδέονται με μια μορφή επιληψίας. Για τους περισσότερους ανθρώπους όμως είναι απλώς μια παράξενη, ακίνδυνη στιγμή.", "It's more common in young people and decreases with age, something that may fit the second interpretation. In rare cases, very frequent and intense episodes may be linked to a form of epilepsy. For most people, though, it's simply a strange, harmless moment."),
 ],
 "questions": [
  Q("Πώς ορίζει η νευροψυχολόγος το ντεζαβού;", ["Ως μια πραγματική ανάμνηση", "Ως αίσθηση οικειότητας χωρίς ανάμνηση", "Ως ένα όνειρο που θυμόμαστε", "Ως πρόβλεψη του μέλλοντος"], 1, "το ντεζαβού δεν είναι ανάμνηση, αλλά αίσθηση οικειότητας χωρίς ανάμνηση"),
  Q("Τι έδειξαν τα πειράματα με εικονικά περιβάλλοντα;", ["Ότι το ντεζαβού δεν υπάρχει", "Ότι συμβαίνει μόνο σε κουρασμένους ανθρώπους", "Ότι ήταν συχνότερο όταν ένα νέο σκηνικό είχε την ίδια διάταξη με ένα παλιό", "Ότι το προκαλούν τα χρώματα"], 2, "οι συμμετέχοντες ανέφεραν συχνότερα ντεζαβού όταν ένα νέο σκηνικό είχε την ίδια διάταξη με ένα παλιό"),
  Q("Πώς αλλάζει η συχνότητα του φαινομένου με την ηλικία;", ["Μειώνεται", "Αυξάνεται", "Μένει ίδια", "Εξαφανίζεται μετά τα τριάντα"], 0, "Είναι πιο συχνό στους νέους και μειώνεται με την ηλικία"),
 ],
 "gloss": {"ντεζαβού": "ντεζαβού — déjà vu", "νευροψυχολόγο": "νευροψυχολόγος — neuropsychologist", "ήδη ειδωμένου": "το ήδη ειδωμένο — déjà vu (lit. the already seen)", "βεβαιότητα": "βεβαιότητα — certainty", "οικειότητας": "οικειότητα — familiarity", "σύγκρουση": "σύγκρουση — conflict, clash", "οριστική": "οριστικός — definitive", "διάταξη": "διάταξη — layout, arrangement", "εικονικά περιβάλλοντα": "εικονικό περιβάλλον — virtual environment", "επισημαίνει": "επισημαίνω — to point out", "επιληψίας": "επιληψία — epilepsy", "ακίνδυνη": "ακίνδυνος — harmless"},
})

ITEMS.append({
 "id": "l179-c1-giati-oi-gates-pefoun-sta-podia", "title": "Γιατί οι γάτες πέφτουν στα πόδια τους", "title_en": "Why cats land on their feet", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε έναν φυσικό να εξηγεί σε μια εκπομπή εκλαΐκευσης της επιστήμης πώς καταφέρνουν οι γάτες να προσγειώνονται στα πόδια τους.",
 "script": [
  L("Φυσικός", "m", "Στα τέλη του δέκατου ένατου αιώνα, ένας Γάλλος επιστήμονας φωτογράφισε μια γάτα που έπεφτε ανάποδα, με μια σειρά από γρήγορα στιγμιότυπα. Οι φωτογραφίες προκάλεσαν αναστάτωση, γιατί έμοιαζαν να παραβιάζουν έναν βασικό νόμο της φυσικής: ένα σώμα που πέφτει χωρίς να στηρίζεται πουθενά δεν μπορεί, έτσι πιστευόταν, να αρχίσει να περιστρέφεται από μόνο του. Κι όμως, η γάτα γύριζε.", "At the end of the nineteenth century, a French scientist photographed a cat falling upside down, in a series of rapid snapshots. The photographs caused a stir, because they seemed to violate a basic law of physics: a falling body that isn't supported by anything cannot, so it was believed, start rotating by itself. And yet, the cat turned."),
  L("Φυσικός", "m", "Η λύση είναι ότι η γάτα δεν γυρίζει σαν ένα στερεό κομμάτι. Λυγίζει στη μέση και περιστρέφει το μπροστινό και το πίσω μέρος του σώματος σε αντίθετες κατευθύνσεις. Πρώτα μαζεύει τα μπροστινά πόδια και γυρίζει το κεφάλι και τον κορμό, ενώ τα πίσω πόδια, απλωμένα, γυρίζουν ελάχιστα. Μετά κάνει το αντίστροφο. Με αυτές τις διαδοχικές κινήσεις, η συνολική στροφορμή μένει μηδέν, όπως απαιτεί ο νόμος, αλλά ο προσανατολισμός της αλλάζει.", "The solution is that the cat doesn't turn like one rigid piece. It bends in the middle and rotates the front and back of its body in opposite directions. First it tucks in its front legs and turns its head and torso, while the back legs, stretched out, turn very little. Then it does the reverse. With these successive movements, the total angular momentum stays zero, as the law requires, but its orientation changes."),
  L("Φυσικός", "m", "Όλο αυτό διαρκεί κλάσματα του δευτερολέπτου, και το αντανακλαστικό εμφανίζεται ήδη στα γατάκια λίγων εβδομάδων. Μην βγάλετε όμως το λάθος συμπέρασμα: οι πτώσεις από μπαλκόνια τραυματίζουν σοβαρά πολλές γάτες κάθε χρόνο. Το ότι προσγειώνονται στα πόδια τους δεν σημαίνει ότι προσγειώνονται ακέραιες.", "All this lasts fractions of a second, and the reflex already appears in kittens a few weeks old. But don't draw the wrong conclusion: falls from balconies seriously injure many cats every year. The fact that they land on their feet doesn't mean they land unharmed."),
 ],
 "questions": [
  Q("Γιατί οι φωτογραφίες προκάλεσαν αναστάτωση;", ["Γιατί η γάτα τραυματίστηκε", "Γιατί έμοιαζαν να παραβιάζουν έναν βασικό νόμο της φυσικής", "Γιατί ήταν οι πρώτες φωτογραφίες ζώου", "Γιατί η γάτα δεν γύρισε"], 1, "έμοιαζαν να παραβιάζουν έναν βασικό νόμο της φυσικής"),
  Q("Πώς καταφέρνει η γάτα να γυρίσει;", ["Κουνώντας την ουρά της σαν προπέλα", "Σπρώχνοντας τον αέρα με τα πόδια", "Περιστρέφοντας το μπροστινό και το πίσω μέρος του σώματος σε αντίθετες κατευθύνσεις", "Γυρίζοντας σαν ένα στερεό κομμάτι"], 2, "περιστρέφει το μπροστινό και το πίσω μέρος του σώματος σε αντίθετες κατευθύνσεις"),
  Q("Ποιο λάθος συμπέρασμα θέλει να αποφύγουμε ο φυσικός;", ["Ότι οι γάτες δεν παθαίνουν τίποτα όταν πέφτουν από μπαλκόνια", "Ότι τα γατάκια δεν έχουν το αντανακλαστικό", "Ότι ο νόμος της φυσικής είναι λάθος", "Ότι μόνο οι γάτες το κάνουν"], 0, "οι πτώσεις από μπαλκόνια τραυματίζουν σοβαρά πολλές γάτες κάθε χρόνο"),
 ],
 "gloss": {"εκλαΐκευσης": "εκλαΐκευση — popularisation", "προσγειώνονται": "προσγειώνομαι — to land", "ανάποδα": "ανάποδα — upside down", "στιγμιότυπα": "στιγμιότυπο — snapshot", "αναστάτωση": "αναστάτωση — stir, commotion", "παραβιάζουν": "παραβιάζω — to violate", "περιστρέφεται": "περιστρέφομαι — to rotate", "στερεό": "στερεός — rigid, solid", "διαδοχικές": "διαδοχικός — successive", "στροφορμή": "στροφορμή — angular momentum", "προσανατολισμός": "προσανατολισμός — orientation", "κλάσματα": "κλάσμα — fraction", "ακέραιες": "ακέραιος — intact, unharmed"},
})

rnd = random.Random(179)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-179.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
