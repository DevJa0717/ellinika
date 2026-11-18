# Source for library/listening/listening-209.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l209.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l209-news-lagokefalos", "title": "Ο λαγοκέφαλος στα δίχτυα των ψαράδων", "title_en": "The silver-cheeked toadfish in fishermen's nets", "type": "news", "level": "B2",
 "context_el": "Ακούτε ένα δελτίο ειδήσεων σε έναν ραδιοφωνικό σταθμό της Κρήτης.",
 "script": [
  L("Εκφωνητής", "m", "Ανησυχία στους ψαράδες της νότιας Κρήτης, καθώς ο λαγοκέφαλος εμφανίζεται όλο και πιο συχνά στα δίχτυα τους. Το ψάρι αυτό ήρθε στη Μεσόγειο από την Ερυθρά Θάλασσα, μέσω της διώρυγας του Σουέζ, και εξαπλώνεται γρήγορα, ευνοημένο από τη θέρμανση των θαλασσών.", "Concern among fishermen in southern Crete, as the silver-cheeked toadfish appears more and more often in their nets. This fish came to the Mediterranean from the Red Sea, through the Suez Canal, and is spreading fast, helped by the warming of the seas."),
  L("Εκφωνητής", "m", "Το κύριο πρόβλημα είναι ότι είναι εξαιρετικά τοξικό. Περιέχει μια ισχυρή τοξίνη, που δεν καταστρέφεται ούτε με το μαγείρεμα, γι' αυτό η πώλησή του απαγορεύεται. Οι αρχές προειδοποιούν τους ερασιτέχνες ψαράδες να μην το τρώνε σε καμία περίπτωση και να το αναγνωρίζουν από το ασημί χρώμα και τα δυνατά δόντια του.", "The main problem is that it is extremely toxic. It contains a powerful toxin, which is not destroyed even by cooking, which is why its sale is banned. The authorities warn amateur fishermen not to eat it under any circumstances and to recognise it by its silver colour and its strong teeth."),
  L("Εκφωνητής", "m", "Οι επαγγελματίες ψαράδες λένε ότι με τα δόντια του ο λαγοκέφαλος κόβει τα δίχτυα και τρώει τα ψάρια που έχουν πιαστεί, προκαλώντας τους μεγάλη οικονομική ζημιά. Ζητούν από το κράτος αποζημιώσεις και ένα πρόγραμμα για τη μείωση του πληθυσμού του.", "Professional fishermen say that with its teeth the toadfish cuts the nets and eats the fish that have been caught, causing them great financial loss. They are asking the state for compensation and a programme to reduce its population."),
 ],
 "questions": [
  Q("Από πού ήρθε ο λαγοκέφαλος στη Μεσόγειο;", ["Από τον Ατλαντικό", "Από την Ερυθρά Θάλασσα, μέσω της διώρυγας του Σουέζ", "Από τη Μαύρη Θάλασσα", "Τον έφεραν ιχθυοτροφεία"], 1, "ήρθε στη Μεσόγειο από την Ερυθρά Θάλασσα, μέσω της διώρυγας του Σουέζ"),
  Q("Γιατί απαγορεύεται η πώλησή του;", ["Γιατί είναι σπάνιος", "Γιατί περιέχει τοξίνη που δεν καταστρέφεται ούτε με το μαγείρεμα", "Γιατί είναι πολύ ακριβός", "Γιατί είναι προστατευόμενο είδος"], 1, "Περιέχει μια ισχυρή τοξίνη, που δεν καταστρέφεται ούτε με το μαγείρεμα"),
  Q("Πώς μπορεί κανείς να τον αναγνωρίσει;", ["Από το κόκκινο χρώμα του", "Από το ασημί χρώμα και τα δυνατά δόντια του", "Από τα μεγάλα πτερύγια", "Από τη μυρωδιά του"], 1, "να το αναγνωρίζουν από το ασημί χρώμα και τα δυνατά δόντια του"),
  Q("Τι ζητούν οι επαγγελματίες ψαράδες;", ["Να απαγορευτεί το ψάρεμα", "Αποζημιώσεις και ένα πρόγραμμα για τη μείωση του πληθυσμού του", "Καινούργια σκάφη", "Να πουλάνε το ψάρι σε άλλες χώρες"], 1, "Ζητούν από το κράτος αποζημιώσεις και ένα πρόγραμμα για τη μείωση του πληθυσμού του"),
 ],
 "gloss": {"λαγοκέφαλος": "λαγοκέφαλος — silver-cheeked toadfish (a toxic pufferfish)", "διώρυγας": "διώρυγα — canal", "ευνοημένο": "ευνοημένος — favoured, helped", "τοξικό": "τοξικός — toxic", "τοξίνη": "τοξίνη — toxin", "ερασιτέχνες": "ερασιτέχνης — amateur", "αποζημιώσεις": "αποζημίωση — compensation"},
})
ITEMS.append({
 "id": "l209-dia-nychterida", "title": "Μια νυχτερίδα στο σαλόνι", "title_en": "A bat in the living room", "type": "dialogue", "level": "B2",
 "context_el": "Δύο συγκάτοικοι ανακαλύπτουν ένα καλοκαιρινό βράδυ ότι κάτι πετάει μέσα στο διαμέρισμά τους.",
 "script": [
  L("Μαρίνα", "f", "Θεέ μου, τι ήταν αυτό; Κάτι πέρασε πάνω από το κεφάλι μου! Πουλί είναι;", "My God, what was that? Something went over my head! Is it a bird?"),
  L("Άγγελος", "m", "Όχι, νυχτερίδα είναι. Θα μπήκε από την μπαλκονόπορτα, που την αφήσαμε ανοιχτή με το φως αναμμένο. Μην τρομάζεις, δεν θα σου επιτεθεί. Πιο φοβισμένη είναι εκείνη από εμάς.", "No, it's a bat. It must have come in through the balcony door, which we left open with the light on. Don't panic, it won't attack you. It's more frightened than we are."),
  L("Μαρίνα", "f", "Και τι κάνουμε; Να την πιάσουμε με μια πετσέτα;", "And what do we do? Shall we catch it with a towel?"),
  L("Άγγελος", "m", "Καλύτερα όχι. Δεν πρέπει να τις αγγίζουμε με γυμνά χέρια, και εξάλλου είναι προστατευόμενα ζώα. Σβήνουμε όλα τα φώτα μέσα, ανοίγουμε διάπλατα την μπαλκονόπορτα και κλείνουμε τις πόρτες των δωματίων. Συνήθως βγαίνουν μόνες τους μέσα σε λίγα λεπτά.", "Better not. We mustn't touch them with bare hands, and besides, they're protected animals. We turn off all the lights inside, open the balcony door wide and close the bedroom doors. They usually go out by themselves within a few minutes."),
  L("Μαρίνα", "f", "Εντάξει... Κοίτα, βγήκε! Μάλλον να βάλουμε σήτα στην μπαλκονόπορτα. Αν και, απ' ό,τι έχω ακούσει, οι νυχτερίδες τρώνε πολλά κουνούπια, οπότε δεν θέλω να τις διώξω από τη γειτονιά, απλώς από το σαλόνι μου.", "OK... Look, it's gone! Maybe we should put a screen on the balcony door. Although, from what I've heard, bats eat lots of mosquitoes, so I don't want to drive them out of the neighbourhood, just out of my living room."),
 ],
 "questions": [
  Q("Πώς μπήκε η νυχτερίδα στο διαμέρισμα;", ["Από την καμινάδα", "Από την μπαλκονόπορτα που ήταν ανοιχτή με το φως αναμμένο", "Από την πόρτα της εισόδου", "Ήταν μέσα από το πρωί"], 1, "Θα μπήκε από την μπαλκονόπορτα, που την αφήσαμε ανοιχτή με το φως αναμμένο"),
  Q("Γιατί ο Άγγελος δεν θέλει να την πιάσουν με πετσέτα;", ["Γιατί θα λερωθεί η πετσέτα", "Γιατί δεν πρέπει να τις αγγίζουμε με γυμνά χέρια και είναι προστατευόμενα ζώα", "Γιατί θα πετάξει πιο γρήγορα", "Γιατί είναι πολύ μεγάλη"], 1, "Δεν πρέπει να τις αγγίζουμε με γυμνά χέρια, και εξάλλου είναι προστατευόμενα ζώα"),
  Q("Τι κάνουν για να φύγει η νυχτερίδα;", ["Καλούν την πυροσβεστική", "Βάζουν δυνατή μουσική", "Σβήνουν τα φώτα, ανοίγουν διάπλατα την μπαλκονόπορτα και κλείνουν τις πόρτες των δωματίων", "Την κυνηγούν με μια σκούπα"], 2, "Σβήνουμε όλα τα φώτα μέσα, ανοίγουμε διάπλατα την μπαλκονόπορτα"),
  Q("Γιατί η Μαρίνα δεν θέλει να διώξει τις νυχτερίδες από τη γειτονιά;", ["Γιατί της αρέσει να τις βλέπει", "Γιατί τρώνε πολλά κουνούπια", "Γιατί φέρνουν τύχη", "Γιατί τις ταΐζει"], 1, "οι νυχτερίδες τρώνε πολλά κουνούπια"),
 ],
 "gloss": {"νυχτερίδα": "νυχτερίδα — bat", "μπαλκονόπορτα": "μπαλκονόπορτα — balcony door", "επιτεθεί": "επιτίθεμαι — to attack", "γυμνά": "γυμνός — bare, naked", "προστατευόμενα": "προστατευόμενος — protected", "διάπλατα": "διάπλατα — wide open", "σήτα": "σήτα — insect screen", "διώξω": "διώχνω — to drive away, chase off"},
})
ITEMS.append({
 "id": "l209-c1-mono-pirouni", "title": "Ένα σκάνδαλο στο τραπέζι: η ιστορία του πιρουνιού", "title_en": "A scandal at the table: the history of the fork", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ιστορικός της καθημερινής ζωής σε μια εκπομπή για τη γαστρονομία.",
 "script": [
  L("Ιστορικός", "f", "Μας φαίνεται αυτονόητο να τρώμε με πιρούνι, κι όμως στη Δυτική Ευρώπη το μικρό αυτό εργαλείο χρειάστηκε σχεδόν επτακόσια χρόνια για να γίνει αποδεκτό. Στο Βυζάντιο, αντίθετα, τα μικρά πιρούνια φαγητού χρησιμοποιούνταν στα τραπέζια των ευγενών ήδη από πολύ νωρίς.", "It seems self-evident to us to eat with a fork, and yet in Western Europe this small tool took almost seven hundred years to be accepted. In Byzantium, by contrast, small table forks were used at the tables of the nobility from very early on."),
  L("Ιστορικός", "f", "Μια περίφημη ιστορία, που καλό είναι να τη διαβάζουμε με κάποια επιφύλαξη, αφορά μια βυζαντινή πριγκίπισσα που παντρεύτηκε στις αρχές του 11ου αιώνα τον γιο του δόγη της Βενετίας. Λέγεται ότι έτρωγε με ένα χρυσό πιρουνάκι αντί για τα δάχτυλα, και ότι ένας κληρικός της εποχής είδε σε αυτό μια προκλητική πολυτέλεια. Όταν εκείνη πέθανε νέα, ο ίδιος παρουσίασε τον θάνατό της σχεδόν ως τιμωρία για τη ματαιοδοξία της.", "A famous story, which we would do well to read with some caution, concerns a Byzantine princess who at the beginning of the 11th century married the son of the doge of Venice. She is said to have eaten with a little golden fork instead of her fingers, and a churchman of the time saw in this a provocative luxury. When she died young, he presented her death almost as a punishment for her vanity."),
  L("Ιστορικός", "f", "Το πιρούνι διαδόθηκε πρώτα στην Ιταλία, όπου τα ζυμαρικά το έκαναν ιδιαίτερα χρήσιμο. Στην Αγγλία, ένας ταξιδιώτης που το έφερε από την Ιταλία στις αρχές του 17ου αιώνα έγινε αντικείμενο χλευασμού, και στις αυλές της Βόρειας Ευρώπης πολλοί το θεωρούσαν για αρκετές δεκαετίες ακόμη επιτήδευση.", "The fork spread first in Italy, where pasta made it particularly useful. In England, a traveller who brought it back from Italy at the beginning of the 17th century became an object of mockery, and at the courts of Northern Europe many considered it an affectation for several more decades."),
  L("Ιστορικός", "f", "Η ιστορία του πιρουνιού μάς θυμίζει ότι οι «καλοί τρόποι» δεν είναι φυσικοί νόμοι. Αυτό που μια εποχή θεωρεί ένδειξη πολιτισμού, μια άλλη μπορεί να το βλέπει ως ύποπτη υπερβολή, και το αντίστροφο.", "The history of the fork reminds us that 'good manners' are not laws of nature. What one age considers a sign of civilisation, another may see as suspicious excess, and vice versa."),
 ],
 "questions": [
  Q("Πόσο χρόνο χρειάστηκε το πιρούνι για να γίνει αποδεκτό στη Δυτική Ευρώπη;", ["Λίγες δεκαετίες", "Σχεδόν επτακόσια χρόνια", "Δύο χιλιάδες χρόνια", "Έναν αιώνα"], 1, "χρειάστηκε σχεδόν επτακόσια χρόνια για να γίνει αποδεκτό"),
  Q("Πώς παρουσιάζει η ομιλήτρια την ιστορία της βυζαντινής πριγκίπισσας;", ["Ως απόλυτα τεκμηριωμένο γεγονός", "Ως ιστορία που πρέπει να διαβάζεται με κάποια επιφύλαξη", "Ως αστείο της εποχής της", "Ως μύθο χωρίς καμία βάση"], 1, "που καλό είναι να τη διαβάζουμε με κάποια επιφύλαξη"),
  Q("Γιατί διαδόθηκε πρώτα στην Ιταλία;", ["Γιατί εκεί κατασκευάζονταν τα καλύτερα μέταλλα", "Γιατί τα ζυμαρικά το έκαναν ιδιαίτερα χρήσιμο", "Γιατί το επέβαλε ο πάπας", "Γιατί ήταν φθηνό"], 1, "όπου τα ζυμαρικά το έκαναν ιδιαίτερα χρήσιμο"),
  Q("Ποιο είναι το γενικό συμπέρασμα της ομιλήτριας;", ["Ότι οι καλοί τρόποι αλλάζουν από εποχή σε εποχή", "Ότι το πιρούνι είναι βυζαντινή εφεύρεση", "Ότι οι Άγγλοι άργησαν σε όλα", "Ότι πρέπει να τρώμε με τα χέρια"], 0, "οι «καλοί τρόποι» δεν είναι φυσικοί νόμοι"),
 ],
 "gloss": {"αυτονόητο": "αυτονόητος — self-evident", "ευγενών": "ευγενής — noble(man)", "επιφύλαξη": "επιφύλαξη — reservation, caution", "δόγη": "δόγης — doge", "κληρικός": "κληρικός — cleric, churchman", "ματαιοδοξία": "ματαιοδοξία — vanity", "χλευασμού": "χλευασμός — mockery", "επιτήδευση": "επιτήδευση — affectation"},
})
ITEMS.append({
 "id": "l209-c1-int-metafrasi-komik", "title": "Πώς μεταφράζεις ένα λογοπαίγνιο;", "title_en": "How do you translate a pun? A comics translator", "type": "interview", "level": "C1",
 "context_el": "Μια δημοσιογράφος συζητά με μια μεταφράστρια κόμικς σε μια εκπομπή για το βιβλίο.",
 "script": [
  L("Δημοσιογράφος", "f", "Πολλοί πιστεύουν ότι το κόμικ είναι το πιο εύκολο κείμενο για να το μεταφράσεις: λίγες λέξεις, πολλές εικόνες. Ισχύει;", "Many people believe that a comic is the easiest text to translate: few words, many pictures. Is that true?"),
  L("Μεταφράστρια", "f", "Ακριβώς το αντίθετο. Το συννεφάκι έχει συγκεκριμένο μέγεθος, οπότε δεν μπορώ να γράψω μια πρόταση διπλάσια από το πρωτότυπο. Και η εικόνα δεν αλλάζει: αν ο ήρωας δείχνει ένα ψάρι και κάνει λογοπαίγνιο με τη λέξη «ψάρι», πρέπει να βρω ένα αστείο στα ελληνικά που να ταιριάζει με το ίδιο ψάρι.", "Exactly the opposite. The speech bubble has a fixed size, so I can't write a sentence twice as long as the original. And the picture doesn't change: if the hero points at a fish and makes a pun on the word 'fish', I have to find a joke in Greek that fits the same fish."),
  L("Δημοσιογράφος", "f", "Και τι γίνεται με τα ονόματα; Σε πολλές σειρές τα ονόματα είναι κι αυτά αστεία.", "And what about the names? In many series the names are jokes too."),
  L("Μεταφράστρια", "f", "Εκεί είναι η μεγαλύτερη πρόκληση. Αν μεταφέρω το όνομα όπως είναι, ο Έλληνας αναγνώστης χάνει το αστείο. Αν το αλλάξω εντελώς, ίσως χάσω κάτι από τον χαρακτήρα ή από την κουλτούρα του πρωτοτύπου. Συνήθως ψάχνω μια λύση στη μέση: ένα όνομα που ακούγεται ξένο, αλλά κρύβει μια ελληνική λέξη που ταιριάζει στον ήρωα. Όταν ένα παιδί γελάει χωρίς να καταλάβει ότι διαβάζει μετάφραση, ξέρω ότι τα κατάφερα.", "That's the biggest challenge. If I carry the name over as it is, the Greek reader loses the joke. If I change it completely, I may lose something of the character or of the culture of the original. Usually I look for a solution in the middle: a name that sounds foreign but hides a Greek word that suits the hero. When a child laughs without realising they're reading a translation, I know I've succeeded."),
  L("Δημοσιογράφος", "f", "Υπάρχει κάτι που δεν μεταφράζεται;", "Is there anything that can't be translated?"),
  L("Μεταφράστρια", "f", "Σχεδόν πάντα κάτι χάνεται, αλλά συχνά κάτι κερδίζεται σε άλλο σημείο. Αν σε μια σελίδα δεν μπορώ να κρατήσω ένα λογοπαίγνιο, προσπαθώ να βάλω ένα δικό μου λίγο πιο κάτω, εκεί που η εικόνα το επιτρέπει. Η πιστότητα, για μένα, δεν είναι λέξη προς λέξη· είναι να γελάσει ο αναγνώστης όσες φορές γέλασε και ο αναγνώστης του πρωτοτύπου.", "Almost always something is lost, but often something is gained elsewhere. If on one page I can't keep a pun, I try to put one of my own a little further on, where the picture allows it. Faithfulness, for me, is not word for word; it's for the reader to laugh as many times as the reader of the original laughed."),
 ],
 "questions": [
  Q("Γιατί, κατά τη μεταφράστρια, το κόμικ δεν είναι εύκολο στη μετάφραση;", ["Γιατί έχει πάρα πολλές λέξεις", "Γιατί το συννεφάκι έχει συγκεκριμένο μέγεθος και η εικόνα δεν αλλάζει", "Γιατί οι εκδότες πληρώνουν λίγο", "Γιατί τα κόμικς γράφονται σε διαλέκτους"], 1, "Το συννεφάκι έχει συγκεκριμένο μέγεθος ... Και η εικόνα δεν αλλάζει"),
  Q("Ποιος είναι ο κίνδυνος αν μεταφέρει ένα αστείο όνομα όπως είναι;", ["Ότι θα είναι πολύ μακρύ", "Ότι ο Έλληνας αναγνώστης θα χάσει το αστείο", "Ότι θα προσβάλει κάποιον", "Ότι δεν θα χωράει στη σελίδα"], 1, "ο Έλληνας αναγνώστης χάνει το αστείο"),
  Q("Τι λύση προτιμά συνήθως για τα ονόματα;", ["Τα αφήνει πάντα αμετάφραστα", "Τα αλλάζει εντελώς σε ελληνικά ονόματα", "Ένα όνομα που ακούγεται ξένο αλλά κρύβει μια ελληνική λέξη", "Τα αντικαθιστά με αριθμούς"], 2, "ένα όνομα που ακούγεται ξένο, αλλά κρύβει μια ελληνική λέξη"),
  Q("Τι σημαίνει πιστότητα για τη μεταφράστρια;", ["Να μεταφράζει λέξη προς λέξη", "Να γελάει ο αναγνώστης όσες φορές γέλασε και ο αναγνώστης του πρωτοτύπου", "Να κρατάει όλα τα ονόματα", "Να μην προσθέτει ποτέ τίποτα δικό της"], 1, "είναι να γελάσει ο αναγνώστης όσες φορές γέλασε και ο αναγνώστης του πρωτοτύπου"),
 ],
 "gloss": {"συννεφάκι": "συννεφάκι — speech bubble (lit. little cloud)", "πρωτότυπο": "πρωτότυπο — the original (text)", "λογοπαίγνιο": "λογοπαίγνιο — pun", "πρόκληση": "πρόκληση — challenge", "κουλτούρα": "κουλτούρα — culture", "κερδίζεται": "κερδίζομαι — to be gained", "πιστότητα": "πιστότητα — faithfulness, fidelity"},
})
rnd = random.Random(209)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-209.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
