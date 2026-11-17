# Source for library/listening/listening-110.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l110.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l110-ann-thalamos-vivliothiki", "title": "Ο παλιός τηλεφωνικός θάλαμος γίνεται βιβλιοθήκη", "title_en": "The old phone box becomes a library", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση του δήμου στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος ανακοινώνει ότι ο παλιός τηλεφωνικός θάλαμος της πλατείας Αγίου Νικολάου, που δεν λειτουργεί εδώ και χρόνια, μετατρέπεται σε μικρή ανοιχτή βιβλιοθήκη. Τα εγκαίνια θα γίνουν το Σάββατο στις έντεκα το πρωί.", "The municipality announces that the old phone box in Agios Nikolaos square, which hasn't worked for years, is being turned into a small open library. The opening will take place on Saturday at eleven in the morning."),
  L("Εκφωνήτρια", "f", "Η λειτουργία της είναι απλή: όποιος θέλει παίρνει ένα βιβλίο και, όταν το τελειώσει, το επιστρέφει ή αφήνει στη θέση του ένα άλλο. Δεν χρειάζεται κάρτα μέλους ούτε εγγραφή.", "It works simply: anyone who wants takes a book and, when they finish it, returns it or leaves another one in its place. No membership card or registration is needed."),
  L("Εκφωνήτρια", "f", "Παρακαλούνται οι δημότες να μην αφήνουν σχολικά βιβλία, περιοδικά ή βιβλία σε κακή κατάσταση. Όσοι θέλουν να δωρίσουν μεγαλύτερες ποσότητες βιβλίων μπορούν να τα φέρουν στη δημοτική βιβλιοθήκη, που θα αναλάβει να ανανεώνει τακτικά τα ράφια του θαλάμου.", "Residents are asked not to leave school textbooks, magazines or books in poor condition. Those who want to donate larger quantities of books can bring them to the municipal library, which will take care of regularly renewing the shelves of the box."),
 ],
 "questions": [
  Q("Τι θα γίνει το Σάββατο;", ["Θα επισκευαστεί το τηλέφωνο", "Θα γίνουν τα εγκαίνια της μικρής βιβλιοθήκης", "Θα γίνει παζάρι βιβλίων", "Θα κλείσει η δημοτική βιβλιοθήκη"], 1, "Τα εγκαίνια θα γίνουν το Σάββατο στις έντεκα το πρωί"),
  Q("Τι χρειάζεται για να πάρει κανείς ένα βιβλίο;", ["Κάρτα μέλους", "Μια μικρή συνδρομή", "Τίποτα, ούτε κάρτα ούτε εγγραφή", "Ταυτότητα"], 2, "Δεν χρειάζεται κάρτα μέλους ούτε εγγραφή"),
  Q("Τι πρέπει να κάνει όποιος θέλει να δωρίσει πολλά βιβλία;", ["Να τα φέρει στη δημοτική βιβλιοθήκη", "Να τα αφήσει όλα στον θάλαμο", "Να ειδοποιήσει τον δήμαρχο", "Να τα πουλήσει σε παλαιοπωλείο"], 0, "μπορούν να τα φέρουν στη δημοτική βιβλιοθήκη"),
 ],
 "gloss": {"θάλαμος": "τηλεφωνικός θάλαμος — phone box", "μετατρέπεται": "μετατρέπομαι — to be turned into", "εγκαίνια": "εγκαίνια — opening, inauguration", "εγγραφή": "εγγραφή — registration", "δημότες": "δημότης — resident (of a municipality)", "δωρίσουν": "δωρίζω — to donate", "ανανεώνει": "ανανεώνω — to renew"}
})

ITEMS.append({
 "id": "l110-vm-ergastiri-keramikis", "title": "Μήνυμα από το εργαστήρι κεραμικής", "title_en": "A message from the pottery workshop", "type": "voicemail", "level": "B2",
 "context_el": "Παρακολουθείτε μαθήματα κεραμικής. Ακούτε ένα μήνυμα από την υπεύθυνη του εργαστηρίου στον τηλεφωνητή.",
 "script": [
  L("Δάφνη", "f", "Γεια σου, Ηλία, η Δάφνη από το εργαστήρι κεραμικής είμαι. Τα κομμάτια σου βγήκαν από τον φούρνο. Τα δύο μπολ είναι τέλεια, αλλά το βάζο, δυστυχώς, ράγισε στο ψήσιμο, μάλλον γιατί ο πάτος του ήταν πολύ πιο χοντρός από τα τοιχώματα.", "Hi Ilias, it's Dafni from the pottery workshop. Your pieces have come out of the kiln. The two bowls are perfect, but the vase, unfortunately, cracked during firing, probably because its base was much thicker than its walls."),
  L("Δάφνη", "f", "Μην στενοχωριέσαι, συμβαίνει σε όλους στην αρχή. Αν θέλεις, την Τετάρτη μπορούμε να φτιάξουμε μαζί ένα καινούργιο και να σου δείξω πώς να ελέγχεις το πάχος του πηλού με ένα απλό σύρμα.", "Don't be upset, it happens to everyone at the beginning. If you like, on Wednesday we can make a new one together and I'll show you how to check the thickness of the clay with a simple wire."),
  L("Δάφνη", "f", "Τα μπολ πρέπει τώρα να τα βάψεις με σμάλτο πριν από το δεύτερο ψήσιμο. Διάλεξε χρώματα από τον κατάλογο στο ράφι, αλλά να ξέρεις ότι στον φούρνο τα χρώματα βγαίνουν πιο σκούρα απ' ό,τι φαίνονται στο βάζο του σμάλτου.", "You now need to glaze the bowls before the second firing. Choose colours from the catalogue on the shelf, but be aware that in the kiln the colours come out darker than they look in the glaze jar."),
 ],
 "questions": [
  Q("Τι έπαθε το βάζο του Ηλία;", ["Έσπασε στη μεταφορά", "Ράγισε στο ψήσιμο", "Χάθηκε", "Βγήκε στραβό"], 1, "το βάζο, δυστυχώς, ράγισε στο ψήσιμο"),
  Q("Τι προτείνει η Δάφνη για την Τετάρτη;", ["Να φτιάξουν μαζί ένα καινούργιο βάζο", "Να πάνε σε μια έκθεση", "Να βάψουν τα μπολ", "Να καθαρίσουν τον φούρνο"], 0, "την Τετάρτη μπορούμε να φτιάξουμε μαζί ένα καινούργιο"),
  Q("Τι πρέπει να ξέρει ο Ηλίας για τα χρώματα;", ["Είναι πολύ ακριβά", "Ξεθωριάζουν με τον καιρό", "Στον φούρνο βγαίνουν πιο σκούρα", "Πρέπει να τα φέρει ο ίδιος"], 2, "στον φούρνο τα χρώματα βγαίνουν πιο σκούρα"),
 ],
 "gloss": {"κεραμικής": "κεραμική — pottery, ceramics", "ράγισε": "ραγίζω — to crack", "ψήσιμο": "ψήσιμο — firing (of pottery); baking", "τοιχώματα": "τοίχωμα — wall (of a vessel)", "πηλού": "πηλός — clay", "σμάλτο": "σμάλτο — glaze, enamel", "πάχος": "πάχος — thickness"}
})

ITEMS.append({
 "id": "l110-dia-oreivatikos-syllogos", "title": "Θα γραφτούμε στον ορειβατικό σύλλογο;", "title_en": "Shall we join the mountaineering club?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο φίλους να συζητούν αν θα γραφτούν σε έναν ορειβατικό σύλλογο.",
 "script": [
  L("Μάνος", "m", "Είδα ότι ο ορειβατικός σύλλογος οργανώνει κάθε Κυριακή πεζοπορίες για αρχάριους. Λέω να γραφτώ. Έλα κι εσύ, μια ζωή λες ότι θες να ανέβεις στον Όλυμπο.", "I saw that the mountaineering club organises hikes for beginners every Sunday. I'm thinking of joining. Come too, you've been saying forever that you want to climb Olympus."),
  L("Ρένα", "f", "Θέλω, αλλά φοβάμαι ότι δεν θα μπορώ να ακολουθήσω. Δεν έχω περπατήσει ποτέ πάνω από δύο ώρες. Και δεν έχω ούτε μπότες ούτε σακίδιο.", "I do, but I'm afraid I won't be able to keep up. I've never walked more than two hours. And I have neither boots nor a backpack."),
  L("Μάνος", "m", "Γι' αυτό ακριβώς υπάρχουν οι πεζοπορίες για αρχάριους: είναι τρεις με τέσσερις ώρες, με πολλές στάσεις, και ο αρχηγός περιμένει πάντα τον τελευταίο. Τον εξοπλισμό μπορείς να τον δανειστείς από τον σύλλογο τις πρώτες φορές.", "That's exactly why there are beginners' hikes: they're three to four hours, with many stops, and the leader always waits for the last person. You can borrow the equipment from the club the first few times."),
  L("Ρένα", "f", "Αφού είναι έτσι, θα έρθω στην πρώτη. Αν αντέξω, γράφομαι. Πάντως τον Όλυμπο τον αφήνουμε για του χρόνου.", "If that's how it is, I'll come on the first one. If I can take it, I'll join. But we're leaving Olympus for next year."),
 ],
 "questions": [
  Q("Γιατί διστάζει η Ρένα;", ["Δεν της αρέσει το βουνό", "Δουλεύει τις Κυριακές", "Φοβάται ότι δεν θα μπορεί να ακολουθήσει", "Δεν συμπαθεί τον σύλλογο"], 2, "φοβάμαι ότι δεν θα μπορώ να ακολουθήσω"),
  Q("Τι ισχύει για τον εξοπλισμό;", ["Πρέπει να τον αγοράσει αμέσως", "Μπορεί να τον δανειστεί από τον σύλλογο τις πρώτες φορές", "Τον δίνει δωρεάν ο δήμος", "Δεν χρειάζεται εξοπλισμός"], 1, "Τον εξοπλισμό μπορείς να τον δανειστείς από τον σύλλογο τις πρώτες φορές"),
  Q("Τι αποφασίζει τελικά η Ρένα;", ["Θα έρθει στην πρώτη πεζοπορία και, αν αντέξει, θα γραφτεί", "Θα γραφτεί αμέσως", "Θα ανέβει στον Όλυμπο φέτος", "Δεν θα πάει καθόλου"], 0, "θα έρθω στην πρώτη. Αν αντέξω, γράφομαι"),
 ],
 "gloss": {"ορειβατικός": "ορειβατικός σύλλογος — mountaineering club", "πεζοπορίες": "πεζοπορία — hike", "αρχάριους": "αρχάριος — beginner", "σακίδιο": "σακίδιο — backpack", "εξοπλισμό": "εξοπλισμός — equipment", "δανειστείς": "δανείζομαι — to borrow", "αντέξω": "αντέχω — to bear, last, cope"}
})

ITEMS.append({
 "id": "l110-int-tsangaris", "title": "Ο τσαγκάρης της γειτονιάς", "title_en": "The neighbourhood shoe repairer", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν τσαγκάρη σε μια εκπομπή για τα παλιά επαγγέλματα.",
 "script": [
  L("Δημοσιογράφος", "f", "Κύριε Στάθη, πόσα χρόνια επισκευάζετε παπούτσια σε αυτό το μαγαζάκι;", "Mr Stathis, how many years have you been repairing shoes in this little shop?"),
  L("Στάθης", "m", "Σαράντα δύο. Το μαγαζί το άνοιξε ο πατέρας μου. Τότε στη γειτονιά υπήρχαν πέντε τσαγκάρηδες· σήμερα έχω μείνει μόνο εγώ. Πολλοί πετούν τα παπούτσια μόλις χαλάσουν, γιατί ένα καινούργιο ζευγάρι κοστίζει συχνά λιγότερο από την επισκευή.", "Forty-two. My father opened the shop. Back then there were five shoe repairers in the neighbourhood; today only I am left. Many people throw their shoes away as soon as they break, because a new pair often costs less than the repair."),
  L("Δημοσιογράφος", "f", "Και ποιοι έρχονται ακόμα σε εσάς;", "And who still comes to you?"),
  L("Στάθης", "m", "Οι ηλικιωμένοι, φυσικά, αλλά τα τελευταία χρόνια και πολλοί νέοι, που έχουν αγοράσει ακριβά δερμάτινα παπούτσια και θέλουν να κρατήσουν. Αλλάζω σόλες και τακούνια, ράβω, βάφω. Η πιο συχνή δουλειά πάντως είναι τα φερμουάρ στις μπότες.", "Older people, of course, but in recent years many young people too, who have bought expensive leather shoes and want them to last. I change soles and heels, I stitch, I dye. The most common job, though, is zips on boots."),
  L("Δημοσιογράφος", "f", "Έχετε κάποιον να συνεχίσει τη δουλειά;", "Do you have someone to carry on the business?"),
  L("Στάθης", "m", "Τα παιδιά μου έχουν άλλα επαγγέλματα. Έχω όμως έναν νεαρό μαθητευόμενο, που έρχεται τρία απογεύματα την εβδομάδα. Έχει καλά χέρια. Ίσως κάποια μέρα το μαγαζί να περάσει σε εκείνον.", "My children have other professions. But I have a young apprentice who comes three afternoons a week. He has good hands. Perhaps one day the shop will pass to him."),
 ],
 "questions": [
  Q("Γιατί, κατά τον κ. Στάθη, πολλοί πετούν τα χαλασμένα παπούτσια;", ["Γιατί δεν βρίσκουν τσαγκάρη", "Γιατί ένα καινούργιο ζευγάρι κοστίζει συχνά λιγότερο από την επισκευή", "Γιατί αλλάζει η μόδα", "Γιατί η επισκευή κρατά πολύ"], 1, "ένα καινούργιο ζευγάρι κοστίζει συχνά λιγότερο από την επισκευή"),
  Q("Ποια είναι η πιο συχνή του δουλειά;", ["Οι σόλες", "Το βάψιμο", "Τα τακούνια", "Τα φερμουάρ στις μπότες"], 3, "Η πιο συχνή δουλειά πάντως είναι τα φερμουάρ στις μπότες"),
  Q("Τι λέει για το μέλλον του μαγαζιού;", ["Θα το κλείσει του χρόνου", "Θα το αναλάβουν τα παιδιά του", "Ίσως περάσει στον νεαρό μαθητευόμενό του", "Θα το πουλήσει"], 2, "Ίσως κάποια μέρα το μαγαζί να περάσει σε εκείνον"),
 ],
 "gloss": {"τσαγκάρη": "τσαγκάρης — shoe repairer, cobbler", "τσαγκάρηδες": "τσαγκάρης — shoe repairer (plural τσαγκάρηδες)", "δερμάτινα": "δερμάτινος — leather", "σόλες": "σόλα — sole", "τακούνια": "τακούνι — heel", "φερμουάρ": "φερμουάρ — zip", "μαθητευόμενο": "μαθητευόμενος — apprentice"}
})

ITEMS.append({
 "id": "l110-rep-sxoleio-xoris-koudouni", "title": "Ένα σχολείο χωρίς κουδούνι", "title_en": "A school without a bell", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ στο ραδιόφωνο για ένα δημοτικό σχολείο.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε ένα δημοτικό σχολείο της Πάτρας δεν ακούγεται πια το γνωστό τσουχτερό κουδούνι. Στη θέση του, στην αρχή και στο τέλος κάθε διαλείμματος, παίζει από τα μεγάφωνα ένα κομμάτι μουσικής, περίπου μισό λεπτό.", "In a primary school in Patras, the familiar shrill bell is no longer heard. In its place, at the start and end of every break, a piece of music, about half a minute long, plays over the loudspeakers."),
  L("Ρεπόρτερ", "m", "Τη μουσική τη διαλέγουν οι ίδιοι οι μαθητές: κάθε εβδομάδα μια διαφορετική τάξη προτείνει τα κομμάτια, και ο δάσκαλος της μουσικής ελέγχει ότι οι στίχοι είναι κατάλληλοι. Έχουν ακουστεί από παραδοσιακά τραγούδια μέχρι μουσική κινούμενων σχεδίων.", "The music is chosen by the pupils themselves: each week a different class suggests the pieces, and the music teacher checks that the lyrics are suitable. Everything has been heard, from traditional songs to cartoon music."),
  L("Ρεπόρτερ", "m", "Η διευθύντρια λέει ότι τα παιδιά μπαίνουν πια στις τάξεις πιο ήρεμα, και ότι οι μικρότεροι μαθητές, που τρόμαζαν με το κουδούνι, δεν βάζουν πια τα χέρια στα αυτιά. Το κουδούνι πάντως δεν καταργήθηκε εντελώς: χρησιμοποιείται μόνο στις ασκήσεις σεισμού.", "The head teacher says that the children now go into class more calmly, and that the younger pupils, who were frightened by the bell, no longer put their hands over their ears. The bell, however, hasn't been abolished entirely: it is used only in earthquake drills."),
 ],
 "questions": [
  Q("Τι έχει αντικαταστήσει το κουδούνι;", ["Ένα σφύριγμα", "Ένα κομμάτι μουσικής από τα μεγάφωνα", "Ένα φωτεινό σήμα", "Η φωνή της διευθύντριας"], 1, "παίζει από τα μεγάφωνα ένα κομμάτι μουσικής"),
  Q("Ποιος διαλέγει τη μουσική;", ["Κάθε εβδομάδα μια διαφορετική τάξη", "Η διευθύντρια", "Ο σύλλογος γονέων", "Ένας ραδιοφωνικός σταθμός"], 0, "κάθε εβδομάδα μια διαφορετική τάξη προτείνει τα κομμάτια"),
  Q("Πότε χρησιμοποιείται ακόμη το κουδούνι;", ["Στην αρχή της χρονιάς", "Στις γιορτές", "Μόνο στις ασκήσεις σεισμού", "Όταν χαλάσουν τα μεγάφωνα"], 2, "χρησιμοποιείται μόνο στις ασκήσεις σεισμού"),
 ],
 "gloss": {"τσουχτερό": "τσουχτερός — shrill, piercing; biting", "διαλείμματος": "διάλειμμα — break (at school)", "μεγάφωνα": "μεγάφωνο — loudspeaker", "στίχοι": "στίχος — line of verse; lyrics (plural)", "κατάλληλοι": "κατάλληλος — suitable", "τρόμαζαν": "τρομάζω — to be frightened", "καταργήθηκε": "καταργούμαι — to be abolished"}
})

ITEMS.append({
 "id": "l110-rep-kerasia-parko", "title": "Μια κερασιά για κάθε τάξη που αποφοιτά", "title_en": "A cherry tree for every graduating class", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια περιφερειακή εκπομπή.",
 "script": [
  L("Ρεπόρτερ", "f", "Στην Έδεσσα, κάθε τάξη που τελειώνει το λύκειο φυτεύει πια μια κερασιά σε ένα χωράφι του δήμου στην άκρη της πόλης. Η ιδέα ξεκίνησε πριν από δέκα χρόνια από μια καθηγήτρια βιολογίας, και σήμερα ο κήπος έχει γίνει ένα μικρό κερασόδασος.", "In Edessa, every class finishing upper secondary school now plants a cherry tree in a municipal field at the edge of the town. The idea started ten years ago with a biology teacher, and today the garden has become a small cherry grove."),
  L("Ρεπόρτερ", "f", "Κάθε δέντρο έχει ένα ξύλινο ταμπελάκι με τη χρονιά και τα ονόματα των μαθητών. Πολλοί απόφοιτοι, όπως μας είπαν, επιστρέφουν κάθε Ιούνιο να μαζέψουν κεράσια από το δικό τους δέντρο και να συναντήσουν παλιούς συμμαθητές.", "Each tree has a small wooden sign with the year and the pupils' names. Many graduates, as they told us, come back every June to pick cherries from their own tree and to meet old classmates."),
  L("Ρεπόρτερ", "f", "Το πότισμα και το κλάδεμα τα αναλαμβάνουν οι μαθητές της πρώτης τάξης, με τη βοήθεια ενός γεωπόνου του δήμου. Τα κεράσια που περισσεύουν δίνονται στο κοινωνικό παντοπωλείο της πόλης.", "The watering and pruning are taken on by first-year pupils, with the help of a municipal agronomist. The cherries left over are given to the town's social grocery."),
 ],
 "questions": [
  Q("Ποιος είχε την ιδέα;", ["Ο δήμαρχος", "Μια καθηγήτρια βιολογίας", "Ένας γεωπόνος", "Ένας σύλλογος γονέων"], 1, "Η ιδέα ξεκίνησε πριν από δέκα χρόνια από μια καθηγήτρια βιολογίας"),
  Q("Τι κάνουν πολλοί απόφοιτοι κάθε Ιούνιο;", ["Φυτεύουν νέα δέντρα", "Επιστρέφουν να μαζέψουν κεράσια και να δουν παλιούς συμμαθητές", "Πουλάνε τα κεράσια", "Κλαδεύουν τα δέντρα"], 1, "επιστρέφουν κάθε Ιούνιο να μαζέψουν κεράσια από το δικό τους δέντρο"),
  Q("Πού πηγαίνουν τα κεράσια που περισσεύουν;", ["Στο κοινωνικό παντοπωλείο της πόλης", "Στη λαϊκή αγορά", "Στην καντίνα του σχολείου", "Σε ένα εργοστάσιο μαρμελάδας"], 0, "Τα κεράσια που περισσεύουν δίνονται στο κοινωνικό παντοπωλείο της πόλης"),
 ],
 "gloss": {"κερασιά": "κερασιά — cherry tree", "κερασόδασος": "κερασόδασος — cherry grove (literally cherry forest)", "ταμπελάκι": "ταμπελάκι — small sign, label", "απόφοιτοι": "απόφοιτος — graduate", "κλάδεμα": "κλάδεμα — pruning", "γεωπόνου": "γεωπόνος — agronomist", "παντοπωλείο": "κοινωνικό παντοπωλείο — social grocery (free food for people in need)"}
})

ITEMS.append({
 "id": "l110-mono-laiki-pwlitis", "title": "Ένα καλοκαίρι πίσω από τον πάγκο της λαϊκής", "title_en": "A summer behind a stall at the street market", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια φοιτήτρια να μιλά σε ένα podcast για μια καλοκαιρινή της δουλειά.",
 "script": [
  L("Αλίκη", "f", "Πέρσι το καλοκαίρι ο θείος μου έσπασε το πόδι του και μου ζήτησε να τον αντικαταστήσω στον πάγκο του στη λαϊκή. Πουλάει ντομάτες, αγγούρια και πιπεριές από το χωράφι του. Δέχτηκα, αν και δεν είχα ιδέα από πώληση.", "Last summer my uncle broke his leg and asked me to replace him at his stall at the street market. He sells tomatoes, cucumbers and peppers from his field. I agreed, although I had no idea about selling."),
  L("Αλίκη", "f", "Οι πρώτες μέρες ήταν δύσκολες. Ξυπνούσα στις πέντε, κουβαλούσα τελάρα και δεν μπορούσα να φωνάξω όπως οι διπλανοί πωλητές. Μια ηλικιωμένη κυρία μού είπε ότι οι ντομάτες μου ήταν οι καλύτερες της λαϊκής, αλλά κανείς δεν το ήξερε γιατί δεν φώναζα.", "The first days were hard. I woke up at five, carried crates and couldn't shout like the sellers next to me. An elderly lady told me that my tomatoes were the best at the market, but nobody knew it because I didn't shout."),
  L("Αλίκη", "f", "Έτσι, άρχισα να δίνω στους περαστικούς να δοκιμάσουν. Σε δύο εβδομάδες είχα σταθερούς πελάτες. Το πιο πολύτιμο που έμαθα δεν ήταν να πουλάω, αλλά να μιλάω με αγνώστους χωρίς να ντρέπομαι.", "So I started giving passers-by a taste. In two weeks I had regular customers. The most valuable thing I learned wasn't selling, but talking to strangers without feeling shy."),
 ],
 "questions": [
  Q("Γιατί η Αλίκη δούλεψε στη λαϊκή;", ["Ήθελε να βγάλει χρήματα για ένα ταξίδι", "Ο θείος της έσπασε το πόδι του", "Το ζήτησε η σχολή της", "Ήθελε να ανοίξει δικό της μαγαζί"], 1, "ο θείος μου έσπασε το πόδι του"),
  Q("Τι της είπε μια ηλικιωμένη κυρία;", ["Ότι οι τιμές της ήταν υψηλές", "Ότι οι ντομάτες της ήταν οι καλύτερες, αλλά κανείς δεν το ήξερε", "Ότι έπρεπε να πουλάει και φρούτα", "Ότι φώναζε πολύ δυνατά"], 1, "οι ντομάτες μου ήταν οι καλύτερες της λαϊκής, αλλά κανείς δεν το ήξερε"),
  Q("Ποιο ήταν, κατά την ίδια, το πιο πολύτιμο που έμαθε;", ["Να ξυπνάει νωρίς", "Να μετράει γρήγορα τα ρέστα", "Να μιλάει με αγνώστους χωρίς να ντρέπεται", "Να καλλιεργεί λαχανικά"], 2, "να μιλάω με αγνώστους χωρίς να ντρέπομαι"),
 ],
 "gloss": {"πάγκο": "πάγκος — stall, counter", "λαϊκή": "λαϊκή (αγορά) — weekly street market", "αντικαταστήσω": "αντικαθιστώ — to replace, stand in for", "τελάρα": "τελάρο — crate (for fruit and vegetables)", "περαστικούς": "περαστικός — passer-by", "σταθερούς": "σταθερός πελάτης — regular customer", "ντρέπομαι": "ντρέπομαι — to be shy, ashamed"}
})

ITEMS.append({
 "id": "l110-mono-xoris-asansser", "title": "Ένας χρόνος χωρίς ασανσέρ", "title_en": "A year without the lift", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε έναν άντρα να μιλά σε μια ραδιοφωνική εκπομπή για την υγεία.",
 "script": [
  L("Φώτης", "m", "Μένω στον έβδομο όροφο και δουλεύω στον πέμπτο ενός γραφείου στο κέντρο. Πριν από έναν χρόνο ο γιατρός μού είπε ότι η πίεσή μου ανεβαίνει και ότι πρέπει να κινούμαι περισσότερο. Δεν είχα χρόνο για γυμναστήριο, οπότε αποφάσισα να μην παίρνω πια το ασανσέρ.", "I live on the seventh floor and work on the fifth floor of an office in the centre. A year ago the doctor told me my blood pressure was going up and that I needed to move more. I didn't have time for a gym, so I decided not to take the lift any more."),
  L("Φώτης", "m", "Τον πρώτο μήνα έφτανα στο γραφείο λαχανιασμένος και ιδρωμένος, και οι συνάδελφοι με κοίταζαν με απορία. Άρχισα να έχω μαζί μου ένα δεύτερο πουκάμισο. Σιγά σιγά, όμως, τα σκαλιά έγιναν συνήθεια.", "The first month I arrived at the office out of breath and sweaty, and my colleagues looked at me in puzzlement. I started carrying a second shirt. Little by little, though, the stairs became a habit."),
  L("Φώτης", "m", "Σήμερα η πίεσή μου είναι φυσιολογική, χωρίς φάρμακα. Το πιο αστείο είναι ότι τρεις συνάδελφοι άρχισαν κι αυτοί να ανεβαίνουν με τα πόδια, και κάθε πρωί κάνουμε κόντρα ποιος θα φτάσει πρώτος.", "Today my blood pressure is normal, without medication. The funniest thing is that three colleagues have also started walking up, and every morning we race to see who gets there first."),
 ],
 "questions": [
  Q("Γιατί ο Φώτης σταμάτησε να παίρνει το ασανσέρ;", ["Χάλασε το ασανσέρ της πολυκατοικίας", "Ο γιατρός τού είπε ότι η πίεσή του ανεβαίνει και πρέπει να κινείται περισσότερο", "Φοβάται τους κλειστούς χώρους", "Ήθελε να χάσει βάρος για έναν γάμο"], 1, "η πίεσή μου ανεβαίνει και ότι πρέπει να κινούμαι περισσότερο"),
  Q("Τι έκανε τον πρώτο μήνα;", ["Είχε μαζί του ένα δεύτερο πουκάμισο", "Πήγαινε στο γραφείο με ταξί", "Έπαιρνε το ασανσέρ μέχρι τη μέση", "Άλλαξε γραφείο"], 0, "Άρχισα να έχω μαζί μου ένα δεύτερο πουκάμισο"),
  Q("Τι συμβαίνει σήμερα με τους συναδέλφους του;", ["Τον κοροϊδεύουν", "Ζήτησαν να φτιαχτεί γυμναστήριο", "Τρεις ανεβαίνουν κι αυτοί με τα πόδια και κάνουν κόντρα", "Κανένας δεν τον ακολούθησε"], 2, "τρεις συνάδελφοι άρχισαν κι αυτοί να ανεβαίνουν με τα πόδια"),
 ],
 "gloss": {"ασανσέρ": "ασανσέρ — lift, elevator", "πίεσή": "πίεση — blood pressure", "λαχανιασμένος": "λαχανιασμένος — out of breath", "ιδρωμένος": "ιδρωμένος — sweaty", "απορία": "με απορία — in puzzlement", "φυσιολογική": "φυσιολογικός — normal", "κόντρα": "κάνω κόντρα — to race, compete"}
})

ITEMS.append({
 "id": "l110-c1-ichotopia", "title": "Τι μας λένε οι ήχοι ενός τόπου", "title_en": "What the sounds of a place tell us", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ερευνήτρια να μιλά σε μια διάλεξη για την ακουστική οικολογία.",
 "script": [
  L("Ερευνήτρια", "f", "Όταν περιγράφουμε έναν τόπο, μιλάμε σχεδόν πάντα για το τι βλέπουμε. Κι όμως, κάθε τόπος έχει και το δικό του ηχητικό τοπίο. Τον όρο αυτό τον καθιέρωσε στη δεκαετία του 1970 ο Καναδός συνθέτης Ρέιμοντ Μάρεϊ Σέιφερ, που κατέγραφε συστηματικά τους ήχους πόλεων και χωριών, ήχους που, όπως έλεγε, χάνονται χωρίς να το καταλάβουμε.", "When we describe a place, we almost always talk about what we see. And yet every place also has its own soundscape. The term was established in the 1970s by the Canadian composer Raymond Murray Schafer, who systematically recorded the sounds of towns and villages, sounds which, as he said, are lost without our noticing."),
  L("Ερευνήτρια", "f", "Αργότερα ο Αμερικανός ερευνητής Μπέρνι Κράους πρότεινε μια απλή διάκριση: τη βιοφωνία, δηλαδή τους ήχους των ζώων, τη γεωφωνία, τους ήχους του ανέμου, του νερού και της βροχής, και την ανθρωποφωνία, όλους τους ήχους που παράγουμε εμείς.", "Later the American researcher Bernie Krause proposed a simple distinction: biophony, that is, the sounds of animals; geophony, the sounds of wind, water and rain; and anthropophony, all the sounds we produce."),
  L("Ερευνήτρια", "f", "Η διάκριση αυτή δεν είναι μόνο θεωρητική. Σε πολλές μελέτες, οι ερευνητές αφήνουν μικρόφωνα σε ένα δάσος για μήνες. Αν η βιοφωνία φτωχαίνει, αν λιγοστεύουν τα πουλιά, τα βατράχια, τα έντομα, αυτό μπορεί να είναι ένδειξη ότι το οικοσύστημα υποφέρει, ακόμη κι όταν, με το μάτι, το δάσος φαίνεται ανέπαφο.", "This distinction is not only theoretical. In many studies, researchers leave microphones in a forest for months. If the biophony grows poorer, if birds, frogs and insects become fewer, this can be a sign that the ecosystem is suffering, even when, to the eye, the forest looks untouched."),
  L("Ερευνήτρια", "f", "Η ανθρωποφωνία, από την άλλη, δεν είναι πάντα εχθρός. Οι καμπάνες ενός χωριού ή οι φωνές μιας λαϊκής αγοράς είναι κομμάτι της ταυτότητας ενός τόπου. Το πρόβλημα είναι ο συνεχής θόρυβος της κυκλοφορίας, που σκεπάζει όλους τους άλλους ήχους. Γι' αυτό ορισμένες πόλεις χαρτογραφούν πια όχι μόνο τον θόρυβο, αλλά και τις «ήσυχες περιοχές» τους, για να τις προστατεύσουν.", "Anthropophony, on the other hand, is not always the enemy. A village's church bells or the voices of a street market are part of a place's identity. The problem is the constant noise of traffic, which drowns out all other sounds. That is why some cities now map not only noise but also their 'quiet areas', in order to protect them."),
 ],
 "questions": [
  Q("Τι έκανε ο Ρέιμοντ Μάρεϊ Σέιφερ;", ["Κατασκεύασε τα πρώτα μικρόφωνα για δάση", "Καθιέρωσε τον όρο «ηχητικό τοπίο» και κατέγραφε τους ήχους πόλεων και χωριών", "Μελέτησε τον θόρυβο στα αεροδρόμια", "Συνέθεσε μουσική με ήχους ζώων"], 1, "ο Καναδός συνθέτης Ρέιμοντ Μάρεϊ Σέιφερ, που κατέγραφε συστηματικά τους ήχους πόλεων και χωριών"),
  Q("Τι είναι η «γεωφωνία», σύμφωνα με τη διάκριση του Κράους;", ["Οι ήχοι των ζώων", "Οι ήχοι που παράγουν οι άνθρωποι", "Οι ήχοι του ανέμου, του νερού και της βροχής", "Οι ήχοι μέσα στη γη"], 2, "τη γεωφωνία, τους ήχους του ανέμου, του νερού και της βροχής"),
  Q("Τι μπορεί να δείξει η φτωχότερη βιοφωνία σε ένα δάσος;", ["Ότι το οικοσύστημα υποφέρει, ακόμη κι αν το δάσος φαίνεται ανέπαφο", "Ότι πλησιάζει ο χειμώνας", "Ότι τα μικρόφωνα έχουν χαλάσει", "Ότι αυξήθηκαν οι επισκέπτες"], 0, "αυτό μπορεί να είναι ένδειξη ότι το οικοσύστημα υποφέρει"),
  Q("Ποια είναι η θέση της ομιλήτριας για την ανθρωποφωνία;", ["Πρέπει να περιοριστεί παντού στο ελάχιστο", "Δεν είναι πάντα εχθρός· το πρόβλημα είναι ο συνεχής θόρυβος της κυκλοφορίας", "Είναι πιο σημαντική από τη βιοφωνία", "Δεν έχει καμία σχέση με την ταυτότητα ενός τόπου"], 1, "Η ανθρωποφωνία, από την άλλη, δεν είναι πάντα εχθρός"),
 ],
 "gloss": {"ηχητικό": "ηχητικό τοπίο — soundscape", "καθιέρωσε": "καθιερώνω — to establish (a term, a custom)", "διάκριση": "διάκριση — distinction", "βιοφωνία": "βιοφωνία — biophony (sounds made by living creatures)", "ανέπαφο": "ανέπαφος — untouched, intact", "σκεπάζει": "σκεπάζω — to cover; drown out (a sound)", "χαρτογραφούν": "χαρτογραφώ — to map"}
})

ITEMS.append({
 "id": "l110-c1-gnostiki-asymfonia", "title": "Όταν τα πιστεύω μας συγκρούονται με τις πράξεις μας", "title_en": "When our beliefs clash with our actions", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη με έναν κοινωνικό ψυχολόγο σε μια εκπομπή για την επιστήμη.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι εννοούμε όταν μιλάμε για «γνωστική ασυμφωνία»;", "What do we mean when we talk about 'cognitive dissonance'?"),
  L("Ψυχολόγος", "m", "Πρόκειται για την ενόχληση που νιώθουμε όταν δύο πεποιθήσεις μας συγκρούονται, ή όταν κάνουμε κάτι που αντιβαίνει σε όσα πιστεύουμε. Την έννοια τη διατύπωσε ο Αμερικανός ψυχολόγος Λίον Φεστίνγκερ το 1957. Η βασική του ιδέα ήταν ότι δεν αντέχουμε για πολύ αυτή την ένταση και ψάχνουμε τρόπους να τη μειώσουμε.", "It is the discomfort we feel when two of our beliefs clash, or when we do something that goes against what we believe. The concept was formulated by the American psychologist Leon Festinger in 1957. His basic idea was that we can't bear this tension for long and we look for ways to reduce it."),
  L("Δημοσιογράφος", "f", "Και ποιοι είναι αυτοί οι τρόποι;", "And what are those ways?"),
  L("Ψυχολόγος", "m", "Θεωρητικά, θα μπορούσαμε να αλλάξουμε τη συμπεριφορά μας. Στην πράξη, συχνά αλλάζουμε τις πεποιθήσεις μας. Ο καπνιστής που ξέρει ότι το τσιγάρο βλάπτει λέει στον εαυτό του ότι ο παππούς του κάπνιζε και έζησε ενενήντα χρόνια. Σε ένα γνωστό πείραμα του Φεστίνγκερ και ενός συνεργάτη του, οι συμμετέχοντες έκαναν μια βαρετή δουλειά και μετά πληρώνονταν για να πουν σε άλλους ότι ήταν ενδιαφέρουσα.", "In theory, we could change our behaviour. In practice, we often change our beliefs. The smoker who knows that cigarettes are harmful tells himself that his grandfather smoked and lived to ninety. In a well-known experiment by Festinger and a colleague, the participants did a boring task and were then paid to tell others that it had been interesting."),
  L("Δημοσιογράφος", "f", "Και τι έδειξε το πείραμα;", "And what did the experiment show?"),
  L("Ψυχολόγος", "m", "Κάτι παράδοξο. Όσοι πήραν μόνο ένα δολάριο δήλωσαν αργότερα ότι η δουλειά τούς είχε αρέσει περισσότερο από όσους πήραν είκοσι. Η ερμηνεία ήταν ότι οι δεύτεροι είχαν μια καλή δικαιολογία για το ψέμα τους, τα χρήματα. Οι πρώτοι δεν είχαν, κι έτσι έπεισαν τον εαυτό τους ότι δεν είχαν πει και τόσο μεγάλο ψέμα. Αυτό, παρεμπιπτόντως, εξηγεί γιατί συχνά αγαπάμε περισσότερο ό,τι μας κόστισε κόπο.", "Something paradoxical. Those who received only one dollar later stated that they had liked the task more than those who received twenty. The interpretation was that the latter had a good excuse for their lie, the money. The former didn't, and so they convinced themselves that they hadn't told such a big lie after all. This, incidentally, explains why we often love more what has cost us effort."),
 ],
 "questions": [
  Q("Τι είναι, σύμφωνα με τον ψυχολόγο, η γνωστική ασυμφωνία;", ["Η αδυναμία να θυμηθούμε τις πεποιθήσεις μας", "Η ενόχληση που νιώθουμε όταν οι πεποιθήσεις ή οι πράξεις μας συγκρούονται", "Η διαφωνία δύο ανθρώπων", "Μια ψυχική ασθένεια"], 1, "Πρόκειται για την ενόχληση που νιώθουμε όταν δύο πεποιθήσεις μας συγκρούονται"),
  Q("Τι κάνουμε συχνά στην πράξη για να μειώσουμε την ένταση;", ["Αλλάζουμε τη συμπεριφορά μας", "Ζητάμε τη γνώμη των άλλων", "Αλλάζουμε τις πεποιθήσεις μας", "Αγνοούμε εντελώς το πρόβλημα"], 2, "Στην πράξη, συχνά αλλάζουμε τις πεποιθήσεις μας"),
  Q("Τι δήλωσαν όσοι πήραν μόνο ένα δολάριο;", ["Ότι η δουλειά τούς άρεσε περισσότερο από όσους πήραν είκοσι", "Ότι ζητούσαν περισσότερα χρήματα", "Ότι δεν είπαν ψέματα", "Ότι η δουλειά ήταν πολύ βαρετή"], 0, "Όσοι πήραν μόνο ένα δολάριο δήλωσαν αργότερα ότι η δουλειά τούς είχε αρέσει περισσότερο από όσους πήραν είκοσι"),
  Q("Πώς ερμηνεύτηκε το αποτέλεσμα;", ["Οι συμμετέχοντες με το ένα δολάριο ήταν πιο ειλικρινείς", "Όσοι πήραν είκοσι δολάρια είχαν δικαιολογία για το ψέμα τους, ενώ οι άλλοι έπεισαν τον εαυτό τους", "Η δουλειά ήταν πράγματι ενδιαφέρουσα", "Τα χρήματα δεν παίζουν κανέναν ρόλο"], 1, "οι δεύτεροι είχαν μια καλή δικαιολογία για το ψέμα τους"),
 ],
 "gloss": {"ασυμφωνία": "γνωστική ασυμφωνία — cognitive dissonance", "ενόχληση": "ενόχληση — discomfort, annoyance", "πεποιθήσεις": "πεποίθηση — belief, conviction", "αντιβαίνει": "αντιβαίνω — to go against, contravene", "διατύπωσε": "διατυπώνω — to formulate", "παράδοξο": "παράδοξος — paradoxical", "δικαιολογία": "δικαιολογία — excuse, justification", "παρεμπιπτόντως": "παρεμπιπτόντως — incidentally"}
})

rnd = random.Random(110)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-110.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
