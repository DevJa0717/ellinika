# Source for library/listening/listening-257.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l257.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l257-news-papagalos", "title": "Ένας χαμένος παπαγάλος γύρισε σπίτι του χάρη σε ένα τραγούδι", "title_en": "A lost parrot comes home thanks to a song", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο πρωινό δελτίο ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνήτρια", "f", "Αίσιο τέλος είχε η περιπέτεια του Ρίκο, ενός γκρίζου παπαγάλου από την Πάτρα, που είχε εξαφανιστεί την περασμένη Κυριακή. Ο παπαγάλος πέταξε από το ανοιχτό παράθυρο της κουζίνας, ενώ η ιδιοκτήτριά του καθάριζε το κλουβί του.", "The adventure of Rico, a grey parrot from Patras who disappeared last Sunday, has had a happy ending. The parrot flew out of the open kitchen window while his owner was cleaning his cage."),
  L("Εκφωνήτρια", "f", "Η κυρία Λίτσα ανέβασε αμέσως φωτογραφίες του στα μέσα κοινωνικής δικτύωσης και κόλλησε αφίσες σε όλη τη γειτονιά. «Δεν κοιμήθηκα τρεις νύχτες», λέει. «Είναι είκοσι δύο χρονών, σχεδόν μέλος της οικογένειας.»", "Mrs Litsa immediately posted photos of him on social media and put up posters all over the neighbourhood. 'I didn't sleep for three nights,' she says. 'He's twenty-two years old, almost a member of the family.'"),
  L("Εκφωνήτρια", "f", "Την Τετάρτη το πρωί μια δεκάχρονη μαθήτρια άκουσε από το μπαλκόνι της κάποιον να σφυρίζει το τραγούδι μιας γνωστής παιδικής σειράς. Είδε έναν γκρίζο παπαγάλο στη διπλανή κληματαριά, θυμήθηκε την αφίσα και ειδοποίησε τους γονείς της.", "On Wednesday morning a ten-year-old schoolgirl heard someone whistling the theme song of a well-known children's series from her balcony. She saw a grey parrot in the vine next door, remembered the poster and told her parents."),
  L("Εκφωνήτρια", "f", "Ο Ρίκο επέστρεψε στο σπίτι του λίγο πεινασμένος, αλλά υγιής. Η κυρία Λίτσα έδωσε στη μικρή την αμοιβή που είχε τάξει, και εκείνη δήλωσε ότι θα αγοράσει με αυτήν βιβλία για τη βιβλιοθήκη του σχολείου της.", "Rico came home a little hungry but healthy. Mrs Litsa gave the girl the reward she had promised, and the girl said she will use it to buy books for her school library."),
 ],
 "questions": [
  Q("Πώς χάθηκε ο παπαγάλος;", ["Τον έκλεψαν", "Πέταξε από το ανοιχτό παράθυρο της κουζίνας", "Έσπασε το κλουβί του", "Τον άφησε ελεύθερο ένα παιδί"], 1, "πέταξε από το ανοιχτό παράθυρο της κουζίνας"),
  Q("Τι έκανε η κυρία Λίτσα για να τον βρει;", ["Πήγε στην αστυνομία", "Ανέβασε φωτογραφίες και κόλλησε αφίσες", "Ζήτησε βοήθεια από έναν κτηνίατρο", "Τηλεφώνησε σε μια εκπομπή"], 1, "ανέβασε αμέσως φωτογραφίες του … και κόλλησε αφίσες"),
  Q("Τι έκανε τη μαθήτρια να προσέξει τον παπαγάλο;", ["Το χρώμα του", "Ένα τραγούδι που σφύριζε", "Το όνομα που φώναζε", "Ένα δαχτυλίδι στο πόδι του"], 1, "άκουσε … κάποιον να σφυρίζει το τραγούδι μιας γνωστής παιδικής σειράς"),
  Q("Τι θα κάνει η μαθήτρια με την αμοιβή;", ["Θα αγοράσει έναν δικό της παπαγάλο", "Θα την κρατήσει για τις διακοπές", "Θα αγοράσει βιβλία για τη βιβλιοθήκη του σχολείου", "Θα τη δώσει σε ένα καταφύγιο ζώων"], 2, "θα αγοράσει με αυτήν βιβλία για τη βιβλιοθήκη του σχολείου της"),
 ],
 "gloss": {"Αίσιο": "αίσιος — happy, auspicious (αίσιο τέλος = happy ending)", "περιπέτεια": "περιπέτεια — adventure", "εξαφανιστεί": "εξαφανίζομαι — to disappear", "κλουβί": "κλουβί — cage", "αφίσες": "αφίσα — poster", "κληματαριά": "κληματαριά — vine trellis, pergola", "ειδοποίησε": "ειδοποιώ — to notify, tell", "πεινασμένος": "πεινασμένος — hungry", "αμοιβή": "αμοιβή — reward", "τάξει": "τάζω — to promise"}
})

ITEMS.append({
 "id": "l257-vm-rafting", "title": "Μήνυμα από την ομάδα ράφτινγκ για την κατάβαση του Σαββάτου", "title_en": "A message from the rafting team about Saturday's descent", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κλείσει μια κατάβαση με ράφτινγκ σε ένα ποτάμι της Ηπείρου. Ακούτε ένα μήνυμα που σας άφησε στον τηλεφωνητή ο οργανωτής.",
 "script": [
  L("Στράτος", "m", "Καλησπέρα, ο Στράτος είμαι, από την ομάδα ράφτινγκ στον Άραχθο. Σας παίρνω για την κατάβαση του Σαββάτου. Το ραντεβού είναι στις εννιάμισι το πρωί στη βάση μας, δίπλα στο ποτάμι. Μην αργήσετε, γιατί πριν μπούμε στο νερό κάνουμε μισή ώρα εκπαίδευση στην όχθη.", "Good evening, it's Stratos from the rafting team on the Arachthos. I'm calling about Saturday's descent. We meet at half past nine in the morning at our base, next to the river. Don't be late, because before we get into the water we do half an hour of training on the bank."),
  L("Στράτος", "m", "Εμείς σας δίνουμε στολή, κράνος και σωσίβιο. Εσείς φέρτε μαγιό, πετσέτα και ρούχα για να αλλάξετε. Στα πόδια χρειάζεστε παλιά αθλητικά που μπορούν να βραχούν· σαγιονάρες όχι, γιατί φεύγουν με το πρώτο κύμα.", "We give you a wetsuit, a helmet and a life jacket. You bring a swimsuit, a towel and clothes to change into. On your feet you need old trainers that can get wet; no flip-flops, because they come off with the first wave."),
  L("Στράτος", "m", "Λόγω των βροχών της εβδομάδας, η στάθμη του νερού είναι ψηλή, οπότε θα κάνουμε τη μικρότερη διαδρομή, περίπου μιάμιση ώρα, και όχι τις τρεις ώρες που λέγαμε. Γι’ αυτό η τιμή θα είναι τριάντα ευρώ το άτομο αντί για σαράντα πέντε.", "Because of this week's rain the water level is high, so we'll do the shorter route, about an hour and a half, not the three hours we said. So the price will be thirty euros per person instead of forty-five."),
  L("Στράτος", "m", "Μου είπατε ότι θα έρθει και ο γιος σας. Σας θυμίζω ότι δεχόμαστε παιδιά από δώδεκα χρονών και πάνω, και πρέπει να ξέρουν κολύμπι. Αν έχετε απορίες, πάρτε με σε αυτό το νούμερο. Τα λέμε το Σάββατο!", "You told me your son is coming too. Just a reminder that we take children from twelve years old up, and they must be able to swim. If you have any questions, call me on this number. See you on Saturday!"),
 ],
 "questions": [
  Q("Γιατί δεν πρέπει να αργήσετε;", ["Γιατί το λεωφορείο φεύγει νωρίς", "Γιατί γίνεται εκπαίδευση στην όχθη πριν από την κατάβαση", "Γιατί το ποτάμι φουσκώνει το μεσημέρι", "Γιατί τα σωσίβια είναι λίγα"], 1, "πριν μπούμε στο νερό κάνουμε μισή ώρα εκπαίδευση στην όχθη"),
  Q("Γιατί δεν πρέπει να φορέσετε σαγιονάρες;", ["Γιατί γλιστράνε στις πέτρες", "Γιατί φεύγουν με το πρώτο κύμα", "Γιατί απαγορεύονται από τον νόμο", "Γιατί κόβουν τα πόδια"], 1, "σαγιονάρες όχι, γιατί φεύγουν με το πρώτο κύμα"),
  Q("Γιατί αλλάζει η διαδρομή;", ["Γιατί η στάθμη του νερού είναι ψηλή", "Γιατί δεν υπάρχει αρκετό νερό", "Γιατί ο οδηγός είναι άρρωστος", "Γιατί κλείνει ο δρόμος"], 0, "η στάθμη του νερού είναι ψηλή, οπότε θα κάνουμε τη μικρότερη διαδρομή"),
  Q("Ποια προϋπόθεση ισχύει για τον γιο σας;", ["Να φέρει δικό του κράνος", "Να είναι πάνω από δεκαέξι χρονών", "Να είναι τουλάχιστον δώδεκα χρονών και να ξέρει κολύμπι", "Να έχει κάνει ξανά ράφτινγκ"], 2, "δεχόμαστε παιδιά από δώδεκα χρονών και πάνω, και πρέπει να ξέρουν κολύμπι"),
 ],
 "gloss": {"κατάβαση": "κατάβαση — descent", "όχθη": "όχθη — river bank", "στολή": "στολή — suit (here: wetsuit)", "σωσίβιο": "σωσίβιο — life jacket", "μαγιό": "μαγιό — swimsuit", "βραχούν": "βρέχομαι — to get wet", "σαγιονάρες": "σαγιονάρα — flip-flop", "στάθμη": "στάθμη — level", "απορίες": "απορία — question, query"}
})

ITEMS.append({
 "id": "l257-c1-mono-xypnitiri", "title": "Ποιος ξυπνούσε τους ξυπνητές; Η ιστορία του ξυπνητηριού", "title_en": "Who woke the knocker-uppers? The history of the alarm clock", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας ομιλίας σε έναν κύκλο εκδηλώσεων για την ιστορία της τεχνολογίας.",
 "script": [
  L("Ομιλήτρια", "f", "Για χιλιάδες χρόνια οι άνθρωποι ξυπνούσαν με το φως, με τον πετεινό ή με την καμπάνα της εκκλησίας. Υπάρχει μια παράδοση ότι ο Πλάτωνας είχε ένα υδραυλικό ρολόι που σφύριζε την αυγή για να ξυπνά τους μαθητές του· η πληροφορία όμως προέρχεται από πολύ μεταγενέστερες πηγές, και δεν μπορούμε να είμαστε βέβαιοι.", "For thousands of years people woke with the light, with the cockerel or with the church bell. There is a tradition that Plato had a water clock that whistled at dawn to wake his students; but the information comes from much later sources, and we cannot be sure."),
  L("Ομιλήτρια", "f", "Το 1787 ένας Αμερικανός ωρολογοποιός, ο Λίβαϊ Χάτσινς, κατασκεύασε ένα ρολόι που χτυπούσε για να τον ξυπνήσει. Είχε όμως ένα μειονέκτημα: χτυπούσε μόνο στις τέσσερις το πρωί, την ώρα που σηκωνόταν ο ίδιος, και δεν ρυθμιζόταν. Ο Χάτσινς, άλλωστε, δεν σκέφτηκε ποτέ να το κατοχυρώσει ή να το πουλήσει.", "In 1787 an American clockmaker, Levi Hutchins, built a clock that rang to wake him. But it had a drawback: it rang only at four in the morning, the time he himself got up, and it could not be adjusted. Hutchins, after all, never thought of patenting it or selling it."),
  L("Ομιλήτρια", "f", "Ρυθμιζόμενο μηχανικό ξυπνητήρι κατοχύρωσε ο Γάλλος Αντουάν Ρεντιέ το 1847, και προς τα τέλη του 19ου αιώνα τα μικρά κουρδιστά ξυπνητήρια άρχισαν να μπαίνουν στα σπίτια. Ως τότε, σε πολλές βιομηχανικές πόλεις της Βρετανίας υπήρχε ένα παράξενο επάγγελμα: οι «ξυπνητές» περνούσαν τα ξημερώματα από τα σπίτια των εργατών και χτυπούσαν τα παράθυρα με ένα μακρύ ραβδί, έναντι μικρής αμοιβής.", "An adjustable mechanical alarm clock was patented by the Frenchman Antoine Redier in 1847, and towards the end of the nineteenth century small wind-up alarm clocks began to enter homes. Until then, in many industrial towns in Britain, there was a strange profession: 'knocker-uppers' went round the workers' houses before dawn and tapped on the windows with a long stick, for a small fee."),
  L("Ομιλήτρια", "f", "Και ποιος ξυπνούσε τους ξυπνητές; Σύμφωνα με ένα αστείο της εποχής, κανείς· γι’ αυτό, έλεγαν, κοιμούνταν τη μέρα. Το επάγγελμα πάντως επιβίωσε σε ορισμένες περιοχές μέχρι και τον 20ό αιώνα, ώσπου το φθηνό ξυπνητήρι το έκανε τελικά περιττό.", "And who woke the knocker-uppers? According to a joke of the time, nobody; that's why, people said, they slept during the day. The profession did survive in some areas into the twentieth century, until the cheap alarm clock finally made it unnecessary."),
 ],
 "questions": [
  Q("Τι λέει η ομιλήτρια για το ρολόι του Πλάτωνα;", ["Ότι σώζεται σε ένα μουσείο", "Ότι η πληροφορία είναι αβέβαιη", "Ότι λειτουργούσε με άμμο", "Ότι το εφηύρε ο Αριστοτέλης"], 1, "η πληροφορία όμως προέρχεται από πολύ μεταγενέστερες πηγές, και δεν μπορούμε να είμαστε βέβαιοι"),
  Q("Ποιο ήταν το μειονέκτημα του ρολογιού του Χάτσινς;", ["Ήταν πολύ ακριβό", "Χτυπούσε μόνο στις τέσσερις το πρωί", "Ήταν πολύ μεγάλο για ένα δωμάτιο", "Χαλούσε συχνά"], 1, "χτυπούσε μόνο στις τέσσερις το πρωί … και δεν ρυθμιζόταν"),
  Q("Τι έκαναν οι «ξυπνητές»;", ["Χτυπούσαν τις καμπάνες των εκκλησιών", "Χτυπούσαν τα παράθυρα των εργατών με ένα μακρύ ραβδί", "Πουλούσαν ξυπνητήρια στους δρόμους", "Μοίραζαν εφημερίδες τα ξημερώματα"], 1, "χτυπούσαν τα παράθυρα με ένα μακρύ ραβδί"),
  Q("Τι έκανε τελικά περιττό το επάγγελμα των ξυπνητών;", ["Ένας νόμος", "Το φθηνό ξυπνητήρι", "Το ραδιόφωνο", "Οι νέες βάρδιες στα εργοστάσια"], 1, "ώσπου το φθηνό ξυπνητήρι το έκανε τελικά περιττό"),
 ],
 "gloss": {"πετεινό": "πετεινός — cockerel", "υδραυλικό": "υδραυλικός — water-driven, hydraulic", "μεταγενέστερες": "μεταγενέστερος — later", "ωρολογοποιός": "ωρολογοποιός — clockmaker", "μειονέκτημα": "μειονέκτημα — drawback", "ρυθμιζόταν": "ρυθμίζομαι — to be adjusted", "κατοχυρώσει": "κατοχυρώνω — to patent, secure legally", "κουρδιστά": "κουρδιστός — wind-up", "ραβδί": "ραβδί — stick", "περιττό": "περιττός — unnecessary"}
})

ITEMS.append({
 "id": "l257-c1-int-enigma", "title": "Ο κώδικας που θεωρούσαν απαραβίαστο: μια ιστορικός για την Ενίγμα", "title_en": "The code thought to be unbreakable: a historian on Enigma", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια ιστορική εκπομπή του ραδιοφώνου.",
 "script": [
  L("Δημοσιογράφος", "m", "Η Ενίγμα θεωρείται το πιο διάσημο κρυπτογραφικό μηχάνημα της ιστορίας. Τι ακριβώς ήταν;", "Enigma is considered the most famous cipher machine in history. What exactly was it?"),
  L("Ιστορικός", "f", "Μια ηλεκτρομηχανική συσκευή που έμοιαζε με γραφομηχανή. Πατούσες ένα γράμμα και άναβε ένα άλλο, γιατί το ρεύμα περνούσε από περιστρεφόμενους δίσκους, τους ρότορες. Σε κάθε πάτημα πλήκτρου οι ρότορες γύριζαν, οπότε το ίδιο γράμμα κρυπτογραφούνταν κάθε φορά διαφορετικά. Οι Γερμανοί άλλαζαν τις ρυθμίσεις κάθε μέρα και ήταν βέβαιοι ότι ο κώδικας ήταν απαραβίαστος.", "An electromechanical device that looked like a typewriter. You pressed one letter and another lit up, because the current passed through rotating discs, the rotors. With every key press the rotors turned, so the same letter was encrypted differently each time. The Germans changed the settings every day and were certain the code was unbreakable."),
  L("Δημοσιογράφος", "m", "Συνήθως ακούμε για τον Άλαν Τούρινγκ. Εκείνος την έσπασε;", "We usually hear about Alan Turing. Was he the one who broke it?"),
  L("Ιστορικός", "f", "Ο Τούρινγκ έπαιξε καθοριστικό ρόλο, αλλά η ιστορία ξεκινά στην Πολωνία. Τρεις νεαροί Πολωνοί μαθηματικοί, με πιο γνωστό τον Μαριάν Ρεγιέφσκι, κατάφεραν ήδη από το 1932 να διαβάζουν μηνύματα μιας πρώτης εκδοχής της. Λίγες εβδομάδες πριν από την έναρξη του πολέμου, το καλοκαίρι του 1939, μοιράστηκαν όσα ήξεραν με τους Βρετανούς και τους Γάλλους.", "Turing played a decisive role, but the story begins in Poland. Three young Polish mathematicians, the best known being Marian Rejewski, managed as early as 1932 to read messages from an early version of it. A few weeks before the war began, in the summer of 1939, they shared what they knew with the British and the French."),
  L("Δημοσιογράφος", "m", "Και τι έγινε στη συνέχεια στη Βρετανία;", "And what happened next in Britain?"),
  L("Ιστορικός", "f", "Στο Μπλέτσλεϊ Παρκ, μια έπαυλη βορειοδυτικά του Λονδίνου, συγκεντρώθηκαν μαθηματικοί, γλωσσολόγοι, ακόμα και πρωταθλητές σκακιού. Ο Τούρινγκ σχεδίασε μηχανές, τις λεγόμενες «βόμβες», που δοκίμαζαν γρήγορα πιθανές ρυθμίσεις. Βοήθησαν όμως και τα ανθρώπινα λάθη: οι Γερμανοί χειριστές επαναλάμβαναν τις ίδιες φράσεις, όπως στα πρωινά δελτία καιρού, και αυτό έδινε στους αναλυτές ένα σημείο εκκίνησης. Ορισμένοι ιστορικοί εκτιμούν ότι η δουλειά αυτή συντόμευσε τον πόλεμο κατά δύο περίπου χρόνια, αν και τέτοιοι υπολογισμοί είναι πάντα αβέβαιοι.", "At Bletchley Park, a country house north-west of London, mathematicians, linguists and even chess champions were brought together. Turing designed machines, the so-called 'bombes', which quickly tested possible settings. But human errors helped too: the German operators repeated the same phrases, as in the morning weather reports, and this gave the analysts a starting point. Some historians estimate that this work shortened the war by about two years, although such calculations are always uncertain."),
 ],
 "questions": [
  Q("Γιατί το ίδιο γράμμα κρυπτογραφούνταν κάθε φορά διαφορετικά;", ["Γιατί οι ρότορες γύριζαν σε κάθε πάτημα πλήκτρου", "Γιατί ο χειριστής άλλαζε γλώσσα", "Γιατί το πληκτρολόγιο είχε δύο σειρές", "Γιατί το μηχάνημα χαλούσε συχνά"], 0, "Σε κάθε πάτημα πλήκτρου οι ρότορες γύριζαν"),
  Q("Πού ξεκινά, κατά την ιστορικό, η ιστορία της αποκρυπτογράφησης;", ["Στη Βρετανία", "Στη Γαλλία", "Στην Πολωνία", "Στις Ηνωμένες Πολιτείες"], 2, "η ιστορία ξεκινά στην Πολωνία"),
  Q("Ποιοι εργάστηκαν στο Μπλέτσλεϊ Παρκ εκτός από μαθηματικούς;", ["Γιατροί και νοσοκόμες", "Γλωσσολόγοι και πρωταθλητές σκακιού", "Μόνο αξιωματικοί του στρατού", "Δημοσιογράφοι"], 1, "μαθηματικοί, γλωσσολόγοι, ακόμα και πρωταθλητές σκακιού"),
  Q("Πώς βοήθησαν τα λάθη των Γερμανών χειριστών;", ["Έστελναν μηνύματα χωρίς κρυπτογράφηση", "Επαναλάμβαναν τις ίδιες φράσεις", "Ξεχνούσαν να αλλάξουν τις ρυθμίσεις για μήνες", "Άφηναν τα μηχανήματα αφύλαχτα"], 1, "επαναλάμβαναν τις ίδιες φράσεις … και αυτό έδινε στους αναλυτές ένα σημείο εκκίνησης"),
 ],
 "gloss": {"κρυπτογραφικό": "κρυπτογραφικός — cryptographic, cipher (adj.)", "ηλεκτρομηχανική": "ηλεκτρομηχανικός — electromechanical", "περιστρεφόμενους": "περιστρεφόμενος — rotating", "ρότορες": "ρότορας — rotor", "κρυπτογραφούνταν": "κρυπτογραφούμαι — to be encrypted", "απαραβίαστος": "απαραβίαστος — unbreakable, inviolable", "καθοριστικό": "καθοριστικός — decisive", "εκδοχής": "εκδοχή — version", "έπαυλη": "έπαυλη — country house, villa", "χειριστές": "χειριστής — operator", "συντόμευσε": "συντομεύω — to shorten"}
})
rnd = random.Random(257)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-257.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
