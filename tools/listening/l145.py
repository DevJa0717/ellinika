# Source for library/listening/listening-145.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l145.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l145-vm-kourdistis", "title": "Ο κουρδιστής του πιάνου", "title_en": "The piano tuner", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από τον κουρδιστή που έχετε καλέσει.",
 "script": [
  L("Κουρδιστής", "m", "Καλησπέρα, ο Παύλος είμαι, ο κουρδιστής. Σας τηλεφωνώ για το πιάνο σας. Είχαμε κανονίσει για την Τετάρτη στις πέντε, αλλά μου ακυρώθηκε ένα ραντεβού και μπορώ να έρθω νωρίτερα, την Τρίτη το πρωί, αν σας βολεύει.", "Good evening, it's Pavlos, the tuner. I'm calling about your piano. We'd arranged Wednesday at five, but an appointment of mine was cancelled and I can come earlier, on Tuesday morning, if that suits you."),
  L("Κουρδιστής", "m", "Μια παράκληση: μην έχετε το καλοριφέρ αναμμένο δίπλα στο πιάνο τη μέρα που θα έρθω, γιατί με τη ζέστη το ξύλο ξεραίνεται και το κούρδισμα δεν κρατάει.", "One request: don't have the radiator on next to the piano on the day I come, because with the heat the wood dries out and the tuning doesn't hold."),
  L("Κουρδιστής", "m", "Από ό,τι μου είπατε, έχει να κουρδιστεί πάνω από πέντε χρόνια, οπότε μάλλον θα χρειαστεί και δεύτερη επίσκεψη σε έναν μήνα. Πείτε μου με ένα μήνυμα τι προτιμάτε.", "From what you told me, it hasn't been tuned for more than five years, so it will probably need a second visit in a month. Let me know by message what you prefer."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί ο κουρδιστής;", ["Για να ακυρώσει το ραντεβού", "Για να προτείνει να έρθει νωρίτερα", "Για να ζητήσει περισσότερα χρήματα", "Για να πει ότι θα αργήσει"], 1, "μπορώ να έρθω νωρίτερα, την Τρίτη το πρωί"),
  Q("Τι σας ζητάει να κάνετε τη μέρα της επίσκεψης;", ["Να μην είναι αναμμένο το καλοριφέρ δίπλα στο πιάνο", "Να μετακινήσετε το πιάνο", "Να είστε στο σπίτι όλη μέρα", "Να ανοίξετε τα παράθυρα"], 0, "μην έχετε το καλοριφέρ αναμμένο δίπλα στο πιάνο"),
  Q("Γιατί μάλλον θα χρειαστεί δεύτερη επίσκεψη;", ["Γιατί το πιάνο είναι χαλασμένο", "Γιατί λείπει ένα εργαλείο", "Γιατί έχει να κουρδιστεί πάνω από πέντε χρόνια", "Γιατί θα μετακομίσετε"], 2, "έχει να κουρδιστεί πάνω από πέντε χρόνια"),
 ],
 "gloss": {"κουρδιστής": "κουρδιστής — (piano) tuner", "κανονίσει": "κανονίζω — to arrange", "ακυρώθηκε": "ακυρώνομαι — to be cancelled", "βολεύει": "βολεύω — to suit", "καλοριφέρ": "καλοριφέρ — radiator", "ξεραίνεται": "ξεραίνομαι — to dry out", "κούρδισμα": "κούρδισμα — tuning", "κουρδιστεί": "κουρδίζω — to tune"}
})

ITEMS.append({
 "id": "l145-ann-anavatires", "title": "Κλειστοί αναβατήρες λόγω αέρα", "title_en": "Lifts closed because of wind", "type": "announcement", "level": "B2",
 "context_el": "Βρίσκεστε σε ένα χιονοδρομικό κέντρο και ακούτε μια ανακοίνωση από τα μεγάφωνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί επισκέπτες, λόγω των ισχυρών ανέμων στα ψηλότερα σημεία του βουνού, οι δύο αναβατήρες της κορυφής θα παραμείνουν κλειστοί τουλάχιστον μέχρι τις δώδεκα. Οι πίστες των αρχαρίων και ο μικρός αναβατήρας δίπλα στο σαλέ λειτουργούν κανονικά.", "Dear visitors, because of the strong winds at the highest points of the mountain, the two summit lifts will remain closed at least until twelve. The beginners' slopes and the small lift next to the chalet are operating normally."),
  L("Εκφωνήτρια", "f", "Όσοι έχετε αγοράσει ημερήσιο εισιτήριο και θέλετε να φύγετε, μπορείτε να ζητήσετε στα ταμεία κουπόνι για μια άλλη μέρα της σεζόν, μέχρι τις έντεκα.", "Those of you who have bought a day ticket and want to leave can ask at the ticket office for a voucher for another day of the season, until eleven."),
  L("Εκφωνήτρια", "f", "Για την ασφάλειά σας, παρακαλούμε να μη βγαίνετε έξω από τις σημαδεμένες πίστες. Η επόμενη ενημέρωση θα γίνει στις έντεκα και μισή.", "For your safety, please do not go outside the marked slopes. The next update will be at half past eleven."),
 ],
 "questions": [
  Q("Τι ισχύει για τους αναβατήρες της κορυφής;", ["Λειτουργούν κανονικά", "Είναι κλειστοί τουλάχιστον μέχρι τις δώδεκα", "Κλείνουν οριστικά για τη σεζόν", "Λειτουργούν μόνο για αρχάριους"], 1, "θα παραμείνουν κλειστοί τουλάχιστον μέχρι τις δώδεκα"),
  Q("Τι μπορούν να κάνουν όσοι θέλουν να φύγουν;", ["Να πάρουν πίσω τα χρήματά τους σε μετρητά", "Να ζητήσουν κουπόνι για μια άλλη μέρα της σεζόν", "Να πάρουν δωρεάν φαγητό στο σαλέ", "Τίποτα"], 1, "μπορείτε να ζητήσετε στα ταμεία κουπόνι για μια άλλη μέρα της σεζόν"),
  Q("Πότε θα γίνει η επόμενη ενημέρωση;", ["Στις έντεκα", "Στις δώδεκα", "Στις έντεκα και μισή", "Το απόγευμα"], 2, "Η επόμενη ενημέρωση θα γίνει στις έντεκα και μισή"),
 ],
 "gloss": {"χιονοδρομικό κέντρο": "χιονοδρομικό κέντρο — ski resort", "ισχυρών": "ισχυρός — strong", "αναβατήρες": "αναβατήρας — ski lift", "πίστες": "πίστα — ski slope", "αρχαρίων": "αρχάριος — beginner", "σαλέ": "σαλέ — chalet", "ημερήσιο": "ημερήσιος — daily, day (ticket)", "κουπόνι": "κουπόνι — voucher", "σημαδεμένες": "σημαδεμένος — marked"}
})

ITEMS.append({
 "id": "l145-dia-gyalia", "title": "Καινούργια γυαλιά", "title_en": "New glasses", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο σε ένα κατάστημα οπτικών.",
 "script": [
  L("Πελάτισσα", "f", "Καλημέρα. Έχω τη συνταγή από τον οφθαλμίατρο. Μου είπε ότι χρειάζομαι πια γυαλιά και για κοντά, όχι μόνο για μακριά.", "Good morning. I have the prescription from the eye doctor. He told me I now need glasses for near vision too, not only for distance."),
  L("Οπτικός", "m", "Μάλιστα. Έχετε δύο επιλογές: είτε δύο ζευγάρια γυαλιά, είτε πολυεστιακούς φακούς, που έχουν και τις δύο διορθώσεις στον ίδιο φακό. Οι πολυεστιακοί είναι πιο πρακτικοί, αλλά θέλουν μερικές μέρες για να τους συνηθίσετε.", "Right. You have two options: either two pairs of glasses, or varifocal lenses, which have both corrections in the same lens. Varifocals are more practical, but they take a few days to get used to."),
  L("Πελάτισσα", "f", "Δουλεύω πολλές ώρες στον υπολογιστή. Αυτό παίζει ρόλο;", "I work many hours at the computer. Does that matter?"),
  L("Οπτικός", "m", "Ναι, γιατί η οθόνη είναι σε μεσαία απόσταση. Θα σας πρότεινα πολυεστιακούς με μεγαλύτερη ζώνη για τη μεσαία απόσταση. Θα είναι έτοιμοι σε δέκα μέρες, και αν μέσα σε έναν μήνα δεν τους συνηθίσετε, τους αλλάζουμε χωρίς χρέωση.", "Yes, because the screen is at middle distance. I'd suggest varifocals with a wider zone for middle distance. They'll be ready in ten days, and if you haven't got used to them within a month, we change them at no charge."),
 ],
 "questions": [
  Q("Τι της είπε ο οφθαλμίατρος;", ["Ότι δεν χρειάζεται πια γυαλιά", "Ότι χρειάζεται γυαλιά και για κοντά", "Ότι πρέπει να χειρουργηθεί", "Ότι χρειάζεται φακούς επαφής"], 1, "χρειάζομαι πια γυαλιά και για κοντά"),
  Q("Ποιο είναι το μειονέκτημα των πολυεστιακών φακών;", ["Θέλουν μερικές μέρες για να τους συνηθίσει κανείς", "Σπάνε εύκολα", "Δεν κάνουν για υπολογιστή", "Είναι πολύ βαριοί"], 0, "θέλουν μερικές μέρες για να τους συνηθίσετε"),
  Q("Τι θα γίνει αν δεν τους συνηθίσει μέσα σε έναν μήνα;", ["Θα πληρώσει τη διαφορά", "Θα πρέπει να ξαναπάει στον γιατρό", "Θα της τους αλλάξουν χωρίς χρέωση", "Θα της δώσουν δεύτερο ζευγάρι"], 2, "τους αλλάζουμε χωρίς χρέωση"),
 ],
 "gloss": {"οπτικών": "οπτικά — optician's (shop)", "συνταγή": "συνταγή — prescription", "οφθαλμίατρο": "οφθαλμίατρος — eye doctor", "πολυεστιακούς": "πολυεστιακός — varifocal, multifocal", "φακούς": "φακός — lens", "διορθώσεις": "διόρθωση — correction", "συνηθίσετε": "συνηθίζω — to get used to", "ζώνη": "ζώνη — zone", "χρέωση": "χρέωση — charge"}
})

ITEMS.append({
 "id": "l145-int-fokies", "title": "Φύλακες της μεσογειακής φώκιας", "title_en": "Guardians of the monk seal", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη σε τοπικό ραδιόφωνο με μια εθελόντρια που παρακολουθεί τις φώκιες σε ένα νησί.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνετε ως εθελόντρια;", "What exactly do you do as a volunteer?"),
  L("Εθελόντρια", "f", "Η μεσογειακή φώκια είναι από τα πιο απειλούμενα θηλαστικά της Ευρώπης, και ένα μεγάλο μέρος του πληθυσμού της ζει στις ελληνικές θάλασσες. Εμείς καταγράφουμε πού εμφανίζονται, και ενημερώνουμε τους ψαράδες και τους λουόμενους.", "The Mediterranean monk seal is one of the most endangered mammals in Europe, and a large part of its population lives in Greek seas. We record where they appear, and we inform fishermen and bathers."),
  L("Δημοσιογράφος", "m", "Τι πρέπει να κάνει κάποιος αν δει μια φώκια σε μια παραλία;", "What should someone do if they see a seal on a beach?"),
  L("Εθελόντρια", "f", "Να κρατήσει απόσταση, τουλάχιστον τριάντα μέτρα, και να μην προσπαθήσει να την ταΐσει ή να τη φωτογραφίσει από κοντά. Πολλές φορές η φώκια απλώς ξεκουράζεται. Αν όμως φαίνεται τραυματισμένη, πρέπει να ειδοποιήσει αμέσως το λιμεναρχείο ή εμάς.", "Keep a distance, at least thirty metres, and not try to feed it or photograph it close up. Often the seal is simply resting. If it looks injured, though, they should immediately notify the port authority or us."),
  L("Δημοσιογράφος", "m", "Οι ψαράδες σας βλέπουν θετικά;", "Do the fishermen view you positively?"),
  L("Εθελόντρια", "f", "Στην αρχή όχι, γιατί οι φώκιες καμιά φορά σκίζουν τα δίχτυα. Τώρα όμως πολλοί μας τηλεφωνούν οι ίδιοι όταν δουν μια φώκια, και νιώθουν ότι την προστατεύουν κι αυτοί.", "At first no, because the seals sometimes tear the nets. But now many of them call us themselves when they see a seal, and they feel that they are protecting it too."),
 ],
 "questions": [
  Q("Τι λέει η εθελόντρια για τον πληθυσμό της φώκιας;", ["Ένα μεγάλο μέρος του ζει στις ελληνικές θάλασσες", "Αυξάνεται γρήγορα", "Ζει μόνο στον Ατλαντικό", "Δεν κινδυνεύει πια"], 0, "ένα μεγάλο μέρος του πληθυσμού της ζει στις ελληνικές θάλασσες"),
  Q("Τι πρέπει να κάνει κάποιος αν δει μια φώκια τραυματισμένη;", ["Να την πάει στη θάλασσα", "Να της δώσει φαγητό", "Να ειδοποιήσει αμέσως το λιμεναρχείο ή την ομάδα", "Να τη φωτογραφίσει"], 2, "πρέπει να ειδοποιήσει αμέσως το λιμεναρχείο ή εμάς"),
  Q("Γιατί στην αρχή οι ψαράδες δεν έβλεπαν θετικά την ομάδα;", ["Γιατί η ομάδα τούς απαγόρευε το ψάρεμα", "Γιατί οι φώκιες σκίζουν καμιά φορά τα δίχτυα", "Γιατί δεν τους ενημέρωνε", "Γιατί έπαιρνε τα ψάρια τους"], 1, "οι φώκιες καμιά φορά σκίζουν τα δίχτυα"),
 ],
 "gloss": {"εθελόντρια": "εθελόντρια — volunteer", "απειλούμενα": "απειλούμενος — endangered", "θηλαστικά": "θηλαστικό — mammal", "πληθυσμού": "πληθυσμός — population", "καταγράφουμε": "καταγράφω — to record", "λουόμενους": "λουόμενος — bather", "ταΐσει": "ταΐζω — to feed", "τραυματισμένη": "τραυματισμένος — injured", "λιμεναρχείο": "λιμεναρχείο — port authority", "σκίζουν": "σκίζω — to tear", "δίχτυα": "δίχτυ — fishing net"}
})

ITEMS.append({
 "id": "l145-news-vera", "title": "Η βέρα βρέθηκε στον βυθό", "title_en": "The wedding ring found on the seabed", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός τοπικού ραδιοφώνου.",
 "script": [
  L("Εκφωνητής", "m", "Με αίσιο τέλος ολοκληρώθηκε μια μικρή περιπέτεια στη Χαλκιδική. Ένας ηλικιωμένος τουρίστας από τη Σερβία έχασε την περασμένη Κυριακή τη βέρα του, ενώ κολυμπούσε σε μια παραλία της Σιθωνίας. Ήταν η βέρα που φορούσε εδώ και πενήντα χρόνια.", "A small adventure in Halkidiki ended happily. An elderly tourist from Serbia lost his wedding ring last Sunday while swimming at a beach in Sithonia. It was the ring he had worn for fifty years."),
  L("Εκφωνητής", "m", "Ο γιος του ανέβασε μια ανάρτηση σε μια ομάδα του διαδικτύου, και την είδε ένας ντόπιος δύτης. Την επόμενη μέρα βούτηξε με ανιχνευτή μετάλλων και, μετά από δύο ώρες, βρήκε τη βέρα στην άμμο, σε βάθος τεσσάρων μέτρων.", "His son posted on an online group, and a local diver saw it. The next day he dived with a metal detector and, after two hours, found the ring in the sand, at a depth of four metres."),
  L("Εκφωνητής", "m", "Ο δύτης αρνήθηκε την αμοιβή που του πρόσφερε η οικογένεια. Δέχτηκε μόνο ένα τραπέζι στην ταβέρνα του χωριού, όπου, όπως είπε, ήπιαν ένα ποτήρι για τα επόμενα πενήντα χρόνια.", "The diver refused the reward the family offered him. He accepted only a meal at the village taverna, where, as he said, they had a glass to the next fifty years."),
 ],
 "questions": [
  Q("Πότε έχασε ο τουρίστας τη βέρα του;", ["Ενώ κολυμπούσε", "Ενώ έτρωγε στην ταβέρνα", "Στο αεροδρόμιο", "Στο ξενοδοχείο"], 0, "ενώ κολυμπούσε σε μια παραλία της Σιθωνίας"),
  Q("Πώς έμαθε ο δύτης για τη βέρα;", ["Από την αστυνομία", "Από μια ανάρτηση του γιου σε μια ομάδα του διαδικτύου", "Από το ραδιόφωνο", "Από τον ιδιοκτήτη της ταβέρνας"], 1, "Ο γιος του ανέβασε μια ανάρτηση σε μια ομάδα του διαδικτύου"),
  Q("Τι δέχτηκε ο δύτης από την οικογένεια;", ["Χρήματα", "Ένα δώρο", "Μόνο ένα τραπέζι στην ταβέρνα του χωριού", "Τίποτα απολύτως"], 2, "Δέχτηκε μόνο ένα τραπέζι στην ταβέρνα του χωριού"),
 ],
 "gloss": {"αίσιο": "αίσιος — happy, fortunate", "βέρα": "βέρα — wedding ring", "ανάρτηση": "ανάρτηση — (online) post", "δύτης": "δύτης — diver", "βούτηξε": "βουτάω — to dive", "ανιχνευτή μετάλλων": "ανιχνευτής μετάλλων — metal detector", "βάθος": "βάθος — depth", "αρνήθηκε": "αρνούμαι — to refuse", "αμοιβή": "αμοιβή — reward, fee"}
})

ITEMS.append({
 "id": "l145-mon-sideroma", "title": "Πώς σιδερώνουμε ένα πουκάμισο", "title_en": "How to iron a shirt", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε ένα απόσπασμα από μια εκπομπή με πρακτικές συμβουλές για το σπίτι.",
 "script": [
  L("Παρουσιάστρια", "f", "Πολλοί βαριούνται να σιδερώνουν πουκάμισα, γιατί δεν ξέρουν από πού να ξεκινήσουν. Το μυστικό είναι η σειρά. Πρώτα ο γιακάς, από την ανάποδη και μετά από την καλή, μετά τα μανίκια και τα μανικέτια, και στο τέλος το σώμα του πουκάμισου.", "Many people can't be bothered to iron shirts, because they don't know where to start. The secret is the order. First the collar, from the inside and then from the outside, then the sleeves and cuffs, and finally the body of the shirt."),
  L("Παρουσιάστρια", "f", "Το πουκάμισο σιδερώνεται πιο εύκολα όταν είναι ακόμα λίγο υγρό. Αν έχει στεγνώσει τελείως, ψεκάστε το με λίγο νερό. Και προσοχή στη θερμοκρασία: τα βαμβακερά αντέχουν πολλή ζέστη, τα συνθετικά όμως μπορεί να λιώσουν.", "A shirt irons more easily when it's still a little damp. If it has dried completely, spray it with a little water. And be careful with the temperature: cotton can take a lot of heat, but synthetics can melt."),
  L("Παρουσιάστρια", "f", "Τέλος, μην το διπλώσετε αμέσως. Κρεμάστε το σε μια κρεμάστρα για δέκα λεπτά, να κρυώσει, αλλιώς θα τσαλακωθεί ξανά.", "Finally, don't fold it straight away. Hang it on a hanger for ten minutes to cool down, otherwise it will crease again."),
 ],
 "questions": [
  Q("Από πού ξεκινάμε το σιδέρωμα;", ["Από το σώμα", "Από τα μανίκια", "Από τον γιακά", "Από τις τσέπες"], 2, "Πρώτα ο γιακάς"),
  Q("Τι κάνουμε αν το πουκάμισο έχει στεγνώσει τελείως;", ["Το ψεκάζουμε με λίγο νερό", "Το ξαναπλένουμε", "Ανεβάζουμε τη θερμοκρασία στο μέγιστο", "Το βάζουμε στο ψυγείο"], 0, "ψεκάστε το με λίγο νερό"),
  Q("Γιατί κρεμάμε το πουκάμισο για δέκα λεπτά;", ["Για να στεγνώσει", "Για να κρυώσει και να μην τσαλακωθεί ξανά", "Για να φύγει η μυρωδιά", "Για να μη χαλάσει το χρώμα"], 1, "αλλιώς θα τσαλακωθεί ξανά"),
 ],
 "gloss": {"σιδερώνουν": "σιδερώνω — to iron", "γιακάς": "γιακάς — collar", "ανάποδη": "ανάποδη — reverse side, inside", "μανίκια": "μανίκι — sleeve", "μανικέτια": "μανικέτι — cuff", "υγρό": "υγρός — damp, wet", "ψεκάστε": "ψεκάζω — to spray", "βαμβακερά": "βαμβακερός — cotton", "συνθετικά": "συνθετικός — synthetic", "κρεμάστρα": "κρεμάστρα — hanger", "τσαλακωθεί": "τσαλακώνομαι — to crease"}
})

ITEMS.append({
 "id": "l145-rep-kolympi-enilikes", "title": "Ποτέ δεν είναι αργά για κολύμπι", "title_en": "It's never too late to swim", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για την υγεία.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε μια χώρα με τόση θάλασσα, πολλοί θα εκπλαγούν να μάθουν ότι αρκετοί ενήλικες δεν ξέρουν κολύμπι. Τα τελευταία χρόνια όμως, όλο και περισσότεροι από αυτούς αποφασίζουν να μάθουν, ακόμα και μετά τα πενήντα.", "In a country with so much sea, many will be surprised to learn that quite a few adults can't swim. In recent years, though, more and more of them decide to learn, even after fifty."),
  L("Ρεπόρτερ", "f", "Σε ένα δημοτικό κολυμβητήριο στη Θεσσαλονίκη, τα τμήματα ενηλίκων γεμίζουν από τον Σεπτέμβριο. Ο προπονητής λέει ότι το πρώτο εμπόδιο δεν είναι η τεχνική, αλλά ο φόβος. Γι' αυτό τα πρώτα μαθήματα γίνονται στη ρηχή πισίνα, όπου όλοι πατάνε.", "At a municipal swimming pool in Thessaloniki, the adult classes fill up from September. The coach says the first obstacle isn't technique but fear. That's why the first lessons take place in the shallow pool, where everyone can stand."),
  L("Ρεπόρτερ", "f", "Η κυρία Ρούλα, εξήντα δύο χρονών, μας είπε ότι όλη της τη ζωή καθόταν στην άμμο και κοίταζε τα εγγόνια της. «Φέτος το καλοκαίρι», λέει, «θα κολυμπήσω μαζί τους μέχρι τη σημαδούρα.»", "Mrs Roula, sixty-two, told us that all her life she sat on the sand and watched her grandchildren. \"This summer,\" she says, \"I'll swim with them out to the buoy.\""),
 ],
 "questions": [
  Q("Τι λέει το ρεπορτάζ για τους ενήλικες;", ["Όλοι ξέρουν κολύμπι", "Όλο και περισσότεροι αποφασίζουν να μάθουν κολύμπι", "Δεν τους επιτρέπεται να μάθουν", "Προτιμούν το γυμναστήριο"], 1, "όλο και περισσότεροι από αυτούς αποφασίζουν να μάθουν"),
  Q("Ποιο είναι το πρώτο εμπόδιο, σύμφωνα με τον προπονητή;", ["Η τεχνική", "Το κόστος", "Ο φόβος", "Η ηλικία"], 2, "το πρώτο εμπόδιο δεν είναι η τεχνική, αλλά ο φόβος"),
  Q("Τι θέλει να κάνει η κυρία Ρούλα φέτος το καλοκαίρι;", ["Να κολυμπήσει με τα εγγόνια της μέχρι τη σημαδούρα", "Να γίνει προπονήτρια", "Να πάει σε αγώνες", "Να μάθει καταδύσεις"], 0, "θα κολυμπήσω μαζί τους μέχρι τη σημαδούρα"),
 ],
 "gloss": {"εκπλαγούν": "εκπλήσσομαι — to be surprised", "ενήλικες": "ενήλικας — adult", "κολυμβητήριο": "κολυμβητήριο — swimming pool (complex)", "τμήματα": "τμήμα — class, group", "εμπόδιο": "εμπόδιο — obstacle", "ρηχή": "ρηχός — shallow", "πατάνε": "πατάω — to stand (touch the bottom)", "σημαδούρα": "σημαδούρα — buoy"}
})

ITEMS.append({
 "id": "l145-dia-laptop-daneio", "title": "Μου δανείζεις το λάπτοπ;", "title_en": "Can you lend me your laptop?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε έναν διάλογο ανάμεσα σε δύο φοιτητές που μένουν στο ίδιο διαμέρισμα.",
 "script": [
  L("Θοδωρής", "m", "Βάσω, μπορείς να μου δανείσεις το λάπτοπ σου για απόψε; Το δικό μου δεν ανοίγει από το πρωί, και πρέπει να παραδώσω την εργασία μέχρι τα μεσάνυχτα.", "Vaso, can you lend me your laptop for tonight? Mine hasn't turned on since this morning, and I have to hand in the assignment by midnight."),
  L("Βάσω", "f", "Ναι, αλλά το χρειάζομαι μέχρι τις εννιά για ένα διαδικτυακό μάθημα. Μετά είναι δικό σου. Έχεις κρατήσει αντίγραφο της εργασίας κάπου;", "Yes, but I need it until nine for an online class. After that it's yours. Have you kept a copy of the assignment somewhere?"),
  L("Θοδωρής", "m", "Νομίζω ότι την είχα ανεβάσει στο cloud χθες το βράδυ, αλλά από τότε έγραψα άλλες τρεις σελίδες.", "I think I uploaded it to the cloud last night, but since then I've written another three pages."),
  L("Βάσω", "f", "Τότε γράψε στον καθηγητή τώρα και εξήγησέ του τι έγινε. Οι περισσότεροι δίνουν παράταση μιας μέρας, αν τους ενημερώσεις πριν από την προθεσμία. Και πήγαινε αύριο το λάπτοπ στο τμήμα πληροφορικής· ίσως σώσουν τα αρχεία.", "Then write to the professor now and explain what happened. Most give a one-day extension if you let them know before the deadline. And take the laptop to the IT department tomorrow; maybe they can save the files."),
 ],
 "questions": [
  Q("Γιατί χρειάζεται ο Θοδωρής το λάπτοπ της Βάσως;", ["Γιατί το δικό του δεν ανοίγει", "Γιατί το δικό του το έχει δανείσει", "Για να δει μια ταινία", "Για ένα διαδικτυακό μάθημα"], 0, "Το δικό μου δεν ανοίγει από το πρωί"),
  Q("Πότε μπορεί να το πάρει;", ["Αμέσως", "Μετά τις εννιά", "Αύριο το πρωί", "Μετά τα μεσάνυχτα"], 1, "το χρειάζομαι μέχρι τις εννιά"),
  Q("Τι τον συμβουλεύει η Βάσω να κάνει πρώτα;", ["Να αγοράσει καινούργιο λάπτοπ", "Να ξαναγράψει όλη την εργασία", "Να γράψει στον καθηγητή τώρα και να του εξηγήσει τι έγινε", "Να μην παραδώσει την εργασία"], 2, "γράψε στον καθηγητή τώρα και εξήγησέ του τι έγινε"),
 ],
 "gloss": {"δανείσεις": "δανείζω — to lend", "παραδώσω": "παραδίδω — to hand in", "εργασία": "εργασία — assignment", "διαδικτυακό": "διαδικτυακός — online", "αντίγραφο": "αντίγραφο — copy", "ανεβάσει": "ανεβάζω — to upload", "παράταση": "παράταση — extension", "προθεσμία": "προθεσμία — deadline", "πληροφορικής": "πληροφορική — IT, computing", "αρχεία": "αρχείο — file"}
})

ITEMS.append({
 "id": "l145-c1-hofstadter", "title": "Ο νόμος του Χόφστατερ", "title_en": "Hofstadter's law", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια ομιλία για τον προγραμματισμό των έργων.",
 "script": [
  L("Ομιλητής", "m", "Ο Αμερικανός επιστήμονας Ντάγκλας Χόφστατερ διατύπωσε στα τέλη της δεκαετίας του 1970 έναν «νόμο» που κάθε υπεύθυνος έργου τον έχει ζήσει στο πετσί του: «Όλα παίρνουν περισσότερο χρόνο απ' όσο περιμένεις, ακόμα κι όταν λαμβάνεις υπόψη τον νόμο του Χόφστατερ».", "The American scientist Douglas Hofstadter formulated at the end of the 1970s a \"law\" that every project manager has lived through first-hand: \"It always takes longer than you expect, even when you take into account Hofstadter's law.\""),
  L("Ομιλητής", "m", "Η διατύπωση είναι σκόπιμα αυτοαναφορική: ακόμα κι αν ξέρουμε ότι υποτιμούμε τον χρόνο και προσθέσουμε ένα περιθώριο, πάλι θα πέσουμε έξω. Οι ψυχολόγοι μιλούν για την «πλάνη του σχεδιασμού»: όταν εκτιμούμε μια εργασία, φανταζόμαστε το ιδανικό σενάριο και ξεχνάμε τα απρόοπτα που σχεδόν πάντα προκύπτουν.", "The wording is deliberately self-referential: even if we know that we underestimate time and add a margin, we'll still get it wrong. Psychologists speak of the \"planning fallacy\": when we estimate a task, we imagine the ideal scenario and forget the unforeseen events that almost always crop up."),
  L("Ομιλητής", "m", "Ένα πρακτικό αντίδοτο είναι να μη ρωτάμε «πόσο θα μου πάρει αυτό;», αλλά «πόσο πήραν παρόμοια έργα στο παρελθόν;». Τα στοιχεία από το παρελθόν είναι συνήθως πολύ πιο ειλικρινή από την αισιοδοξία μας.", "A practical antidote is not to ask \"how long will this take me?\" but \"how long did similar projects take in the past?\". Data from the past is usually far more honest than our optimism."),
  L("Ομιλητής", "m", "Ο νόμος, βέβαια, δεν είναι επιστημονικός νόμος, αλλά ένα πνευματώδες αξίωμα. Η δύναμή του βρίσκεται στο ότι μας θυμίζει πόσο επίμονη είναι αυτή η συστηματική αισιοδοξία, ακόμα και σε όσους τη γνωρίζουν.", "The law, of course, is not a scientific law but a witty adage. Its power lies in the fact that it reminds us how persistent this systematic optimism is, even among those who know about it."),
 ],
 "questions": [
  Q("Τι υποστηρίζει ο νόμος του Χόφστατερ;", ["Ότι τα έργα τελειώνουν πάντα νωρίτερα", "Ότι όλα παίρνουν περισσότερο χρόνο απ' όσο περιμένουμε, ακόμα κι αν το λάβουμε υπόψη", "Ότι η τεχνολογία διπλασιάζεται κάθε δύο χρόνια", "Ότι οι μεγάλες ομάδες δουλεύουν πιο αργά"], 1, "Όλα παίρνουν περισσότερο χρόνο απ' όσο περιμένεις, ακόμα κι όταν λαμβάνεις υπόψη τον νόμο του Χόφστατερ"),
  Q("Τι είναι η «πλάνη του σχεδιασμού»;", ["Η τάση να φανταζόμαστε το ιδανικό σενάριο και να ξεχνάμε τα απρόοπτα", "Ένα λάθος στους υπολογισμούς του κόστους", "Η αδυναμία να πάρουμε αποφάσεις", "Ο φόβος της αποτυχίας"], 0, "φανταζόμαστε το ιδανικό σενάριο και ξεχνάμε τα απρόοπτα"),
  Q("Ποιο αντίδοτο προτείνει ο ομιλητής;", ["Να προσθέτουμε πάντα διπλάσιο χρόνο", "Να δουλεύουμε περισσότερες ώρες", "Να κοιτάμε πόσο πήραν παρόμοια έργα στο παρελθόν", "Να μοιράζουμε τη δουλειά σε περισσότερους"], 2, "πόσο πήραν παρόμοια έργα στο παρελθόν"),
  Q("Πώς χαρακτηρίζει ο ομιλητής τον νόμο;", ["Ως αποδεδειγμένο επιστημονικό νόμο", "Ως ανοησία", "Ως οικονομική θεωρία", "Ως πνευματώδες αξίωμα"], 3, "ένα πνευματώδες αξίωμα"),
 ],
 "gloss": {"διατύπωσε": "διατυπώνω — to formulate", "στο πετσί του": "ζω κάτι στο πετσί μου — to experience first-hand", "λαμβάνεις υπόψη": "λαμβάνω υπόψη — to take into account", "αυτοαναφορική": "αυτοαναφορικός — self-referential", "υποτιμούμε": "υποτιμώ — to underestimate", "περιθώριο": "περιθώριο — margin", "πλάνη": "πλάνη — fallacy, delusion", "απρόοπτα": "απρόοπτο — unforeseen event", "αντίδοτο": "αντίδοτο — antidote", "πνευματώδες": "πνευματώδης — witty", "αξίωμα": "αξίωμα — axiom, adage", "επίμονη": "επίμονος — persistent"}
})

ITEMS.append({
 "id": "l145-c1-cantillon", "title": "Το φαινόμενο Καντιγιόν", "title_en": "The Cantillon effect", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια εκπομπή για την οικονομία, με καλεσμένη μια οικονομολόγο.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι είναι αυτό που οι οικονομολόγοι ονομάζουν «φαινόμενο Καντιγιόν»;", "What is it that economists call the \"Cantillon effect\"?"),
  L("Οικονομολόγος", "f", "Πήρε το όνομά του από τον Ρισάρ Καντιγιόν, έναν τραπεζίτη και οικονομικό στοχαστή του 18ου αιώνα. Η ιδέα είναι ότι, όταν μπαίνει νέο χρήμα στην οικονομία, δεν φτάνει σε όλους ταυτόχρονα. Το παίρνουν πρώτα ορισμένοι, οι τράπεζες, το κράτος ή όσοι δανείζονται, και αυτοί το ξοδεύουν όταν οι τιμές είναι ακόμα χαμηλές.", "It's named after Richard Cantillon, an eighteenth-century banker and economic thinker. The idea is that when new money enters the economy, it doesn't reach everyone at the same time. Certain people get it first, the banks, the state or borrowers, and they spend it while prices are still low."),
  L("Δημοσιογράφος", "m", "Και οι υπόλοιποι;", "And everyone else?"),
  L("Οικονομολόγος", "f", "Οι υπόλοιποι, για παράδειγμα οι μισθωτοί ή οι συνταξιούχοι, βλέπουν το νέο χρήμα πολύ αργότερα, αν το δουν, και στο μεταξύ οι τιμές έχουν ήδη ανέβει. Έτσι, το ίδιο ποσό νέου χρήματος μπορεί να αναδιανείμει τον πλούτο χωρίς να το έχει αποφασίσει κανείς ρητά.", "The rest, for example wage earners or pensioners, see the new money much later, if at all, and in the meantime prices have already risen. So the same amount of new money can redistribute wealth without anyone having explicitly decided it."),
  L("Δημοσιογράφος", "m", "Είναι μια ιδέα που αποδέχονται όλοι;", "Is it an idea everyone accepts?"),
  L("Οικονομολόγος", "f", "Ότι το χρήμα δεν διαχέεται ομοιόμορφα, το αποδέχονται οι περισσότεροι. Το πόσο μεγάλη είναι η επίδραση στην πράξη, όμως, παραμένει αντικείμενο έντονης συζήτησης, και εξαρτάται πολύ από το πώς ακριβώς μπαίνει το χρήμα στην οικονομία.", "That money doesn't spread evenly is accepted by most. How large the effect is in practice, though, remains the subject of intense debate, and depends a lot on exactly how the money enters the economy."),
 ],
 "questions": [
  Q("Ποια είναι η βασική ιδέα του φαινομένου;", ["Ότι το νέο χρήμα δεν φτάνει σε όλους ταυτόχρονα", "Ότι οι τιμές πέφτουν πάντα", "Ότι οι τράπεζες χάνουν χρήματα", "Ότι οι μισθοί ανεβαίνουν πρώτοι"], 0, "δεν φτάνει σε όλους ταυτόχρονα"),
  Q("Γιατί ωφελούνται όσοι παίρνουν πρώτοι το νέο χρήμα;", ["Γιατί δεν πληρώνουν φόρους", "Γιατί το ξοδεύουν όταν οι τιμές είναι ακόμα χαμηλές", "Γιατί το αποταμιεύουν", "Γιατί το στέλνουν στο εξωτερικό"], 1, "το ξοδεύουν όταν οι τιμές είναι ακόμα χαμηλές"),
  Q("Τι συμβαίνει με τους μισθωτούς και τους συνταξιούχους;", ["Παίρνουν πρώτοι το χρήμα", "Δεν επηρεάζονται", "Βλέπουν το χρήμα αργότερα, όταν οι τιμές έχουν ήδη ανέβει", "Κερδίζουν περισσότερο από όλους"], 2, "στο μεταξύ οι τιμές έχουν ήδη ανέβει"),
  Q("Τι παραμένει αντικείμενο συζήτησης;", ["Αν υπήρξε ο Καντιγιόν", "Αν το χρήμα διαχέεται ομοιόμορφα", "Αν οι τράπεζες είναι απαραίτητες", "Πόσο μεγάλη είναι η επίδραση στην πράξη"], 3, "Το πόσο μεγάλη είναι η επίδραση στην πράξη"),
 ],
 "gloss": {"οικονομολόγο": "οικονομολόγος — economist", "στοχαστή": "στοχαστής — thinker", "ταυτόχρονα": "ταυτόχρονα — simultaneously", "δανείζονται": "δανείζομαι — to borrow", "μισθωτοί": "μισθωτός — wage earner", "αναδιανείμει": "αναδιανέμω — to redistribute", "ρητά": "ρητά — explicitly", "διαχέεται": "διαχέομαι — to spread, diffuse", "ομοιόμορφα": "ομοιόμορφα — evenly", "επίδραση": "επίδραση — effect, influence"}
})

rnd = random.Random(145)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-145.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
