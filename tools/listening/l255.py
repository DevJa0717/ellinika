# Source for library/listening/listening-255.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l255.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l255-news-paidiko-dimotiko-symvoulio", "title": "Πρώτη συνεδρίαση για το Δημοτικό Συμβούλιο Παιδιών", "title_en": "The Children's Town Council holds its first meeting", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο απογευματινό δελτίο ενός τοπικού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνήτρια", "f", "Με πολλή σοβαρότητα, αλλά και λίγο τρακ, πραγματοποιήθηκε χθες στην αίθουσα του δημοτικού συμβουλίου η πρώτη συνεδρίαση του Δημοτικού Συμβουλίου Παιδιών. Τα είκοσι ένα μέλη του, μαθητές από δέκα έως δεκατεσσάρων χρονών, εκλέχτηκαν τον περασμένο μήνα από τους συμμαθητές τους.", "With great seriousness, but also a little stage fright, the first meeting of the Children's Town Council took place yesterday in the council chamber. Its twenty-one members, pupils aged ten to fourteen, were elected last month by their classmates."),
  L("Εκφωνήτρια", "f", "Το πρώτο θέμα της ημερήσιας διάταξης ήταν η ασφάλεια στον δρόμο προς το σχολείο. Τα παιδιά παρουσίασαν έναν χάρτη που έφτιαξαν μόνα τους, με όλα τα σημεία όπου, όπως είπαν, «φοβούνται να περάσουν», και ζήτησαν περισσότερους τροχονόμους τις ώρες της εισόδου και της εξόδου.", "The first item on the agenda was safety on the way to school. The children presented a map they had made themselves, showing all the spots where, as they put it, 'they are afraid to cross', and asked for more traffic wardens at the times when school starts and finishes."),
  L("Εκφωνήτρια", "f", "Ακολούθησε μια ζωηρή συζήτηση για τις παιδικές χαρές. Μια μαθήτρια της έκτης δημοτικού πρότεινε να μπουν σε κάθε παιδική χαρά και κούνιες κατάλληλες για παιδιά σε αναπηρικό αμαξίδιο, και η πρότασή της εγκρίθηκε ομόφωνα.", "A lively discussion about playgrounds followed. A sixth-grade pupil proposed that every playground should also have swings suitable for children in wheelchairs, and her proposal was approved unanimously."),
  L("Εκφωνήτρια", "f", "Ο δήμαρχος, που παρακολούθησε τη συνεδρίαση, δεσμεύτηκε ότι οι αποφάσεις του Συμβουλίου θα συζητούνται υποχρεωτικά και από το κανονικό δημοτικό συμβούλιο. «Τα παιδιά βλέπουν την πόλη από ένα ύψος που εμείς έχουμε ξεχάσει», σχολίασε. Το Συμβούλιο Παιδιών θα συνεδριάζει μία φορά τον μήνα.", "The mayor, who attended the meeting, pledged that the Council's decisions will necessarily also be discussed by the regular town council. 'Children see the town from a height we have forgotten,' he commented. The Children's Council will meet once a month."),
 ],
 "questions": [
  Q("Ποιος εξέλεξε τα μέλη του Συμβουλίου Παιδιών;", ["Ο δήμαρχος", "Οι δάσκαλοι", "Οι συμμαθητές τους", "Οι γονείς τους"], 2, "εκλέχτηκαν τον περασμένο μήνα από τους συμμαθητές τους"),
  Q("Τι παρουσίασαν τα παιδιά για την ασφάλεια στον δρόμο;", ["Μια ταινία", "Έναν χάρτη με τα σημεία όπου φοβούνται να περάσουν", "Μια λίστα με υπογραφές", "Φωτογραφίες από ατυχήματα"], 1, "Τα παιδιά παρουσίασαν έναν χάρτη που έφτιαξαν μόνα τους"),
  Q("Ποια πρόταση εγκρίθηκε ομόφωνα;", ["Να κλείνουν οι δρόμοι γύρω από τα σχολεία", "Να φτιαχτεί νέα παιδική χαρά", "Να μπουν κούνιες για παιδιά σε αναπηρικό αμαξίδιο", "Να μεγαλώσει το διάλειμμα"], 2, "κούνιες κατάλληλες για παιδιά σε αναπηρικό αμαξίδιο"),
  Q("Τι υποσχέθηκε ο δήμαρχος;", ["Να γίνεται συνεδρίαση κάθε εβδομάδα", "Να συζητούνται οι αποφάσεις και από το κανονικό δημοτικό συμβούλιο", "Να δοθούν χρήματα σε κάθε σχολείο", "Να γίνουν νέες εκλογές τον Ιούνιο"], 1, "θα συζητούνται υποχρεωτικά και από το κανονικό δημοτικό συμβούλιο"),
 ],
 "gloss": {"σοβαρότητα": "σοβαρότητα — seriousness", "τρακ": "τρακ — stage fright, nerves", "συνεδρίαση": "συνεδρίαση — meeting, session", "συμβουλίου": "συμβούλιο — council", "ημερήσιας": "ημερήσια διάταξη — agenda", "τροχονόμους": "τροχονόμος — traffic warden", "ζωηρή": "ζωηρός — lively", "αμαξίδιο": "αμαξίδιο — wheelchair (αναπηρικό αμαξίδιο)", "εγκρίθηκε": "εγκρίνω — to approve", "ομόφωνα": "ομόφωνα — unanimously", "δεσμεύτηκε": "δεσμεύομαι — to commit oneself, pledge", "υποχρεωτικά": "υποχρεωτικά — compulsorily, necessarily"}
})

ITEMS.append({
 "id": "l255-vm-ergastiri-chartaetou", "title": "Μήνυμα από το εργαστήρι χαρταετού για τα παιδιά", "title_en": "A message from the children's kite workshop", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε γράψει το παιδί σας σε ένα εργαστήρι όπου τα παιδιά φτιάχνουν χαρταετούς για την Καθαρά Δευτέρα. Ακούτε ένα μήνυμα που σας άφησε στον τηλεφωνητή η υπεύθυνη.",
 "script": [
  L("Δέσποινα", "f", "Καλησπέρα σας, η Δέσποινα είμαι, από το πολιτιστικό κέντρο. Σας τηλεφωνώ για το εργαστήρι χαρταετού, όπου έχετε γράψει τον μικρό σας. Έχουμε μια μικρή αλλαγή: το εργαστήρι δεν θα γίνει το Σάββατο, αλλά την Κυριακή στις έντεκα, γιατί το Σάββατο η αίθουσα χρειάζεται για μια συναυλία.", "Good evening, it's Despoina from the cultural centre. I'm calling about the kite workshop you've signed your little one up for. We have a small change: the workshop won't take place on Saturday but on Sunday at eleven, because on Saturday the hall is needed for a concert."),
  L("Δέσποινα", "f", "Τα καλάμια, το χαρτί και τον σπάγκο τα έχουμε εμείς. Θα ήθελα όμως να φέρει ο μικρός ένα παλιό πουκάμισο ή μια ποδιά, γιατί θα δουλέψουμε με κόλλα και τα παιδιά συνήθως λερώνονται μέχρι τα αυτιά.", "We have the reeds, the paper and the string. But I'd like your little one to bring an old shirt or an apron, because we'll be working with glue and children usually get messy up to their ears."),
  L("Δέσποινα", "f", "Οι γονείς είναι ευπρόσδεκτοι να μείνουν, αλλά σας παρακαλώ να μην κάνετε τη δουλειά για τα παιδιά! Ο χαρταετός δεν χρειάζεται να είναι τέλειος· σημασία έχει να τον φτιάξουν μόνα τους. Θα τελειώσουμε γύρω στη μία.", "Parents are welcome to stay, but please don't do the work for the children! The kite doesn't need to be perfect; what matters is that they make it themselves. We'll finish around one."),
  L("Δέσποινα", "f", "Και κάτι ακόμα: αν ο καιρός το επιτρέψει, την Καθαρά Δευτέρα θα πετάξουμε όλοι μαζί τους χαρταετούς στον λόφο πίσω από το κέντρο. Αν φυσάει πολύ δυνατά, θα το μεταθέσουμε για την επόμενη Κυριακή. Θα σας ενημερώσω με μήνυμα. Καλό βράδυ.", "And one more thing: if the weather allows, on Clean Monday we'll all fly the kites together on the hill behind the centre. If the wind is too strong, we'll move it to the following Sunday. I'll let you know by text message. Good evening."),
 ],
 "questions": [
  Q("Γιατί αλλάζει η μέρα του εργαστηρίου;", ["Γιατί η Δέσποινα είναι άρρωστη", "Γιατί η αίθουσα χρειάζεται για μια συναυλία", "Γιατί έχει κακοκαιρία", "Γιατί δεν έφτασαν τα υλικά"], 1, "η αίθουσα χρειάζεται για μια συναυλία"),
  Q("Τι πρέπει να φέρει το παιδί;", ["Καλάμια και χαρτί", "Ψαλίδι και κόλλα", "Ένα παλιό πουκάμισο ή μια ποδιά", "Κολατσιό"], 2, "ένα παλιό πουκάμισο ή μια ποδιά"),
  Q("Τι ζητά από τους γονείς;", ["Να μην μείνουν στην αίθουσα", "Να μην κάνουν τη δουλειά για τα παιδιά", "Να φέρουν τον δικό τους χαρταετό", "Να έρθουν νωρίτερα"], 1, "να μην κάνετε τη δουλειά για τα παιδιά"),
  Q("Τι θα γίνει αν φυσάει πολύ δυνατά την Καθαρά Δευτέρα;", ["Θα πετάξουν τους χαρταετούς στην αίθουσα", "Θα ακυρωθεί οριστικά", "Θα μετατεθεί για την επόμενη Κυριακή", "Θα πάνε σε άλλον λόφο"], 2, "θα το μεταθέσουμε για την επόμενη Κυριακή"),
 ],
 "gloss": {"εργαστήρι": "εργαστήρι — workshop", "χαρταετού": "χαρταετός — kite", "καλάμια": "καλάμι — reed, cane", "σπάγκο": "σπάγκος — string", "ποδιά": "ποδιά — apron", "λερώνονται": "λερώνομαι — to get dirty", "ευπρόσδεκτοι": "ευπρόσδεκτος — welcome", "Καθαρά": "Καθαρά Δευτέρα — Clean Monday (first day of Lent)", "λόφο": "λόφος — hill", "μεταθέσουμε": "μεταθέτω — to postpone, move"}
})

ITEMS.append({
 "id": "l255-c1-mono-fanaria-kykloforias", "title": "Από το φανάρι με γκάζι στα τρία χρώματα: η ιστορία των φαναριών της κυκλοφορίας", "title_en": "From the gas lamp to three colours: the history of traffic lights", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ραδιοφωνική εκπομπή για την ιστορία των καθημερινών αντικειμένων.",
 "script": [
  L("Παρουσιάστρια", "f", "Το πρώτο φανάρι της κυκλοφορίας δεν τοποθετήθηκε για αυτοκίνητα, αφού αυτά δεν υπήρχαν ακόμη. Στήθηκε στο Λονδίνο το 1868, έξω από το Κοινοβούλιο, για να ρυθμίζει τις άμαξες και να προστατεύει τους πεζούς. Το σχεδίασε ένας μηχανικός των σιδηροδρόμων, που πήρε την ιδέα από τα σήματα των τρένων.", "The first traffic light was not installed for cars, since they did not exist yet. It was put up in London in 1868, outside Parliament, to regulate carriages and protect pedestrians. It was designed by a railway engineer, who took the idea from train signals."),
  L("Παρουσιάστρια", "f", "Τη μέρα λειτουργούσε με βραχίονες που σήκωνε και κατέβαζε ένας αστυφύλακας, και τη νύχτα με ένα φανάρι γκαζιού, κόκκινο και πράσινο. Η εφεύρεση όμως είχε άδοξο τέλος: λίγες εβδομάδες αργότερα μια διαρροή γκαζιού προκάλεσε έκρηξη που τραυμάτισε τον αστυφύλακα, και το φανάρι απομακρύνθηκε.", "By day it worked with arms that a policeman raised and lowered, and by night with a gas lamp, red and green. But the invention had an inglorious end: a few weeks later a gas leak caused an explosion that injured the policeman, and the light was removed."),
  L("Παρουσιάστρια", "f", "Χρειάστηκαν σχεδόν πενήντα χρόνια και η εξάπλωση του αυτοκινήτου για να επανέλθει η ιδέα. Τα πρώτα ηλεκτρικά φανάρια εμφανίστηκαν στις Ηνωμένες Πολιτείες τη δεκαετία του 1910, και γύρω στο 1920 ένας αστυνομικός στο Ντιτρόιτ πρόσθεσε το τρίτο, το κίτρινο χρώμα, για να προειδοποιεί τους οδηγούς ότι το σήμα πρόκειται να αλλάξει.", "It took almost fifty years and the spread of the car for the idea to return. The first electric traffic lights appeared in the United States in the 1910s, and around 1920 a policeman in Detroit added the third colour, amber, to warn drivers that the signal was about to change."),
  L("Παρουσιάστρια", "f", "Γιατί όμως κόκκινο για τη στάση; Το κόκκινο χρησιμοποιούνταν ήδη στους σιδηροδρόμους ως σήμα κινδύνου, και επιπλέον διακρίνεται από μακριά. Έτσι, μια σύμβαση που γεννήθηκε στις γραμμές των τρένων του δέκατου ένατου αιώνα ρυθμίζει σήμερα, σχεδόν απαράλλαχτη, την κίνηση σε όλο τον πλανήτη.", "But why red for stop? Red was already used on the railways as a danger signal, and moreover it can be seen from far away. So a convention born on the railway lines of the nineteenth century today regulates traffic all over the planet, almost unchanged."),
 ],
 "questions": [
  Q("Για ποιον λόγο στήθηκε το πρώτο φανάρι στο Λονδίνο;", ["Για να ρυθμίζει τα αυτοκίνητα", "Για να ρυθμίζει τις άμαξες και να προστατεύει τους πεζούς", "Για να φωτίζει την είσοδο του Κοινοβουλίου", "Για να δίνει σήματα στα τρένα"], 1, "για να ρυθμίζει τις άμαξες και να προστατεύει τους πεζούς"),
  Q("Από πού πήρε την ιδέα ο σχεδιαστής του;", ["Από τους φάρους", "Από τα σήματα των τρένων", "Από τα πλοία", "Από τα θέατρα"], 1, "πήρε την ιδέα από τα σήματα των τρένων"),
  Q("Γιατί απομακρύνθηκε το πρώτο φανάρι;", ["Γιατί δεν το καταλάβαιναν οι οδηγοί", "Γιατί κόστιζε πολύ", "Γιατί μια διαρροή γκαζιού προκάλεσε έκρηξη", "Γιατί το χτύπησε μια άμαξα"], 2, "μια διαρροή γκαζιού προκάλεσε έκρηξη"),
  Q("Τι σκοπό είχε το κίτρινο χρώμα που προστέθηκε;", ["Να δείχνει τη διάβαση των πεζών", "Να προειδοποιεί ότι το σήμα πρόκειται να αλλάξει", "Να φαίνεται το φανάρι στην ομίχλη", "Να ξεχωρίζουν τα λεωφορεία"], 1, "για να προειδοποιεί τους οδηγούς ότι το σήμα πρόκειται να αλλάξει"),
 ],
 "gloss": {"φανάρι": "φανάρι — traffic light; lantern", "άμαξες": "άμαξα — carriage", "σιδηροδρόμων": "σιδηρόδρομος — railway", "βραχίονες": "βραχίονας — arm (of a signal)", "αστυφύλακας": "αστυφύλακας — police constable", "γκαζιού": "γκάζι — gas", "άδοξο": "άδοξος — inglorious", "διαρροή": "διαρροή — leak", "απομακρύνθηκε": "απομακρύνω — to remove", "επανέλθει": "επανέρχομαι — to return, come back", "σύμβαση": "σύμβαση — convention; contract", "απαράλλαχτη": "απαράλλαχτος — unchanged, identical"}
})

ITEMS.append({
 "id": "l255-c1-int-bananes-klonoi", "title": "Γιατί όλες οι μπανάνες είναι σχεδόν ίδιες; Μια φυτοπαθολόγος εξηγεί", "title_en": "Why are all bananas almost identical? A plant pathologist explains", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια εκπομπή του ραδιοφώνου για τη διατροφή και τη γεωργία.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι μπανάνες που αγοράζουμε στο σούπερ μάρκετ μοιάζουν σαν να βγήκαν από το ίδιο καλούπι. Είναι σύμπτωση;", "The bananas we buy at the supermarket look as if they came out of the same mould. Is that a coincidence?"),
  L("Φυτοπαθολόγος", "f", "Καθόλου. Η συντριπτική πλειονότητα των μπανανών του διεθνούς εμπορίου ανήκει σε μία μόνο ποικιλία, την Κάβεντις, και τα φυτά της είναι στην ουσία κλώνοι. Η εμπορική μπανάνα δεν έχει γόνιμους σπόρους· τα μαύρα στιγματάκια στο εσωτερικό της είναι υπολείμματα σπόρων. Έτσι, οι παραγωγοί δεν τη σπέρνουν, αλλά τη φυτεύουν από παραφυάδες, δηλαδή βλαστούς που φυτρώνουν στη βάση του μητρικού φυτού.", "Not at all. The overwhelming majority of internationally traded bananas belong to a single variety, the Cavendish, and its plants are in essence clones. The commercial banana has no fertile seeds; the little black specks inside are the remains of seeds. So growers don't sow it but plant it from suckers, that is, shoots that grow at the base of the mother plant."),
  L("Δημοσιογράφος", "m", "Και πού είναι το πρόβλημα; Ομοιομορφία σημαίνει και σταθερή ποιότητα.", "And where's the problem? Uniformity also means consistent quality."),
  L("Φυτοπαθολόγος", "f", "Το πρόβλημα είναι ότι, όταν όλα τα φυτά είναι γενετικά ίδια, μια ασθένεια που προσβάλλει το ένα μπορεί να τα προσβάλει όλα. Αυτό έχει ήδη συμβεί μία φορά. Ως τα μέσα του εικοστού αιώνα η κυρίαρχη ποικιλία ήταν μια άλλη, η Γκρο Μισέλ, που λέγεται ότι ήταν πιο γευστική. Ένας μύκητας του εδάφους, που προκαλεί τη λεγόμενη ασθένεια του Παναμά, την κατέστρεψε σε φυτείες ολόκληρων χωρών.", "The problem is that when all the plants are genetically identical, a disease that attacks one can attack them all. This has already happened once. Until the middle of the twentieth century the dominant variety was another one, the Gros Michel, which is said to have been tastier. A soil fungus, which causes the so-called Panama disease, destroyed it on the plantations of entire countries."),
  L("Δημοσιογράφος", "m", "Και η Κάβεντις κινδυνεύει τώρα με τον ίδιο τρόπο;", "And is the Cavendish now in danger in the same way?"),
  L("Φυτοπαθολόγος", "f", "Δυστυχώς ναι. Ένα νέο στέλεχος του ίδιου μύκητα εξαπλώνεται εδώ και δεκαετίες από την Ασία σε άλλες ηπείρους, και η Κάβεντις δεν του αντιστέκεται. Ο μύκητας επιβιώνει στο χώμα για πολλά χρόνια, οπότε δεν αρκεί να ξεριζώσεις τα άρρωστα φυτά. Οι ερευνητές δοκιμάζουν ανθεκτικές ποικιλίες, αλλά το βασικό μάθημα είναι άλλο: μια καλλιέργεια χωρίς ποικιλομορφία είναι σαν ένα κτίριο με μία μόνο κολόνα.", "Unfortunately, yes. A new strain of the same fungus has been spreading for decades from Asia to other continents, and the Cavendish has no resistance to it. The fungus survives in the soil for many years, so it's not enough to uproot the sick plants. Researchers are testing resistant varieties, but the main lesson is a different one: a crop without diversity is like a building with a single pillar."),
 ],
 "questions": [
  Q("Γιατί οι εμπορικές μπανάνες μοιάζουν τόσο πολύ μεταξύ τους;", ["Γιατί καλλιεργούνται στην ίδια χώρα", "Γιατί ανήκουν σχεδόν όλες σε μία ποικιλία και είναι κλώνοι", "Γιατί ωριμάζουν με τον ίδιο τρόπο", "Γιατί επιλέγονται με μηχανήματα"], 1, "ανήκει σε μία μόνο ποικιλία, την Κάβεντις, και τα φυτά της είναι στην ουσία κλώνοι"),
  Q("Πώς πολλαπλασιάζουν οι παραγωγοί την μπανάνα;", ["Με σπόρους από τον καρπό", "Με μπόλιασμα σε άλλα δέντρα", "Από παραφυάδες στη βάση του μητρικού φυτού", "Με σπόρους από εργαστήρια"], 2, "τη φυτεύουν από παραφυάδες"),
  Q("Τι συνέβη στην ποικιλία Γκρο Μισέλ;", ["Αντικαταστάθηκε επειδή ήταν άνοστη", "Την κατέστρεψε ένας μύκητας του εδάφους", "Δεν άντεχε τη μεταφορά", "Απαγορεύτηκε η καλλιέργειά της"], 1, "Ένας μύκητας του εδάφους, που προκαλεί τη λεγόμενη ασθένεια του Παναμά, την κατέστρεψε"),
  Q("Γιατί δεν αρκεί να ξεριζώσει κανείς τα άρρωστα φυτά;", ["Γιατί ο μύκητας επιβιώνει στο χώμα για πολλά χρόνια", "Γιατί ο μύκητας μεταφέρεται με τον αέρα", "Γιατί τα φυτά ξαναφυτρώνουν", "Γιατί απαγορεύεται από τον νόμο"], 0, "Ο μύκητας επιβιώνει στο χώμα για πολλά χρόνια"),
 ],
 "gloss": {"καλούπι": "καλούπι — mould", "συντριπτική": "συντριπτικός — overwhelming", "ποικιλία": "ποικιλία — variety", "κλώνοι": "κλώνος — clone", "γόνιμους": "γόνιμος — fertile", "στιγματάκια": "στιγματάκι — little speck, dot", "παραφυάδες": "παραφυάδα — sucker, offshoot (of a plant)", "προσβάλλει": "προσβάλλω — to attack (of a disease); to offend", "μύκητας": "μύκητας — fungus", "φυτείες": "φυτεία — plantation", "στέλεχος": "στέλεχος — strain (of a microbe); executive", "ξεριζώσεις": "ξεριζώνω — to uproot", "ποικιλομορφία": "ποικιλομορφία — diversity"}
})
rnd = random.Random(255)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-255.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
