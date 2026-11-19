# Source for library/listening/listening-266.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l266.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l266-news-potistres-kafsonas", "title": "Ποτίστρες για τα αδέσποτα και τα πουλιά στις γειτονιές της Λάρισας", "title_en": "Water bowls for strays and birds in Larissa's neighbourhoods", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο μεσημεριανό δελτίο ενός τοπικού ραδιοφωνικού σταθμού, εν μέσω καύσωνα.",
 "script": [
  L("Εκφωνητής", "m", "Με τη θερμοκρασία να ξεπερνά τους σαράντα βαθμούς για πέμπτη συνεχόμενη μέρα, ο δήμος Λαρισαίων τοποθέτησε εκατόν πενήντα ποτίστρες σε πάρκα, πλατείες και σχολικές αυλές, για να βρίσκουν νερό τα αδέσποτα ζώα και τα πουλιά της πόλης.", "With temperatures above forty degrees for the fifth day in a row, the municipality of Larissa has placed a hundred and fifty water bowls in parks, squares and school yards, so that the town's stray animals and birds can find water."),
  L("Εκφωνητής", "m", "Οι ποτίστρες είναι από ανοξείδωτο μέταλλο και στερεώνονται στο έδαφος, ώστε να μην αναποδογυρίζουν. Τις γεμίζουν κάθε πρωί εθελοντές από φιλοζωικές ομάδες, σε συνεργασία με τους υπαλλήλους πρασίνου του δήμου.", "The bowls are made of stainless steel and are fixed to the ground so that they don't tip over. Volunteers from animal welfare groups fill them every morning, in cooperation with the municipality's parks staff."),
  L("Εκφωνητής", "m", "Ο δήμος καλεί και τους κατοίκους να βάζουν ένα πιάτο με νερό στα μπαλκόνια και στις αυλές τους, σε σκιερό σημείο. Όπως εξηγεί μια κτηνίατρος, το νερό πρέπει να αλλάζει καθημερινά, γιατί στη ζέστη χαλάει γρήγορα και μπορεί να γίνει εστία για κουνούπια.", "The municipality is also asking residents to put a dish of water on their balconies and in their yards, in a shady spot. As a vet explains, the water must be changed every day, because in the heat it goes bad quickly and can become a breeding ground for mosquitoes."),
  L("Εκφωνητής", "m", "Η κτηνίατρος συμβουλεύει επίσης όσους έχουν σκύλους να μην τους βγάζουν βόλτα το μεσημέρι, γιατί η άσφαλτος ζεσταίνεται τόσο που μπορεί να κάψει τα πέλματά τους. Ένα απλό τεστ, λέει: αν δεν αντέχετε να κρατήσετε την παλάμη σας στην άσφαλτο για επτά δευτερόλεπτα, είναι πολύ ζεστή και για τον σκύλο.", "The vet also advises dog owners not to take them for walks at midday, because the asphalt gets so hot that it can burn their paws. A simple test, she says: if you can't bear to hold your palm on the asphalt for seven seconds, it's too hot for the dog as well."),
 ],
 "questions": [
  Q("Πού τοποθέτησε ο δήμος τις ποτίστρες;", ["Μόνο στο κέντρο της πόλης", "Σε πάρκα, πλατείες και σχολικές αυλές", "Στις στάσεις των λεωφορείων", "Έξω από τα σούπερ μάρκετ"], 1, "σε πάρκα, πλατείες και σχολικές αυλές"),
  Q("Γιατί οι ποτίστρες στερεώνονται στο έδαφος;", ["Για να μην τις κλέβουν", "Για να μένει κρύο το νερό", "Για να μην αναποδογυρίζουν", "Για να μη φτάνουν εκεί τα πουλιά"], 2, "ώστε να μην αναποδογυρίζουν"),
  Q("Γιατί πρέπει να αλλάζει καθημερινά το νερό;", ["Γιατί στη ζέστη χαλάει γρήγορα και μαζεύει κουνούπια", "Γιατί το πίνουν γρήγορα τα ζώα", "Γιατί το ζητά ο δήμος", "Γιατί ζεσταίνεται πολύ"], 0, "στη ζέστη χαλάει γρήγορα και μπορεί να γίνει εστία για κουνούπια"),
  Q("Τι δείχνει το τεστ με την παλάμη;", ["Αν ο σκύλος διψάει", "Αν πρέπει να βάλετε νερό στο μπαλκόνι", "Αν ο σκύλος έχει πυρετό", "Αν η άσφαλτος είναι πολύ ζεστή για τον σκύλο"], 3, "είναι πολύ ζεστή και για τον σκύλο"),
 ],
 "gloss": {"ποτίστρες": "ποτίστρα — water bowl, drinking trough", "αδέσποτα": "αδέσποτος — stray", "συνεχόμενη": "συνεχόμενος — consecutive", "ανοξείδωτο": "ανοξείδωτος — stainless", "στερεώνονται": "στερεώνομαι — to be fixed, secured", "αναποδογυρίζουν": "αναποδογυρίζω — to tip over, overturn", "φιλοζωικές": "φιλοζωικός — animal welfare (adj.)", "σκιερό": "σκιερός — shady", "εστία": "εστία — source, breeding ground; hearth", "άσφαλτος": "άσφαλτος — asphalt", "πέλματά": "πέλμα — sole; (animal) pad, paw", "παλάμη": "παλάμη — palm (of the hand)"}
})

ITEMS.append({
 "id": "l266-vm-diaplous-kolpou", "title": "Μήνυμα από τους διοργανωτές του διάπλου του κόλπου", "title_en": "A message from the organisers of the open-water swim across the gulf", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δηλώσει συμμετοχή σε έναν κολυμβητικό αγώνα ανοιχτής θάλασσας, έναν διάπλου τριών χιλιομέτρων. Ακούτε ένα μήνυμα από τους διοργανωτές.",
 "script": [
  L("Διοργανώτρια", "f", "Καλησπέρα, η Σοφία είμαι από τον ναυτικό όμιλο, για τον διάπλου της Κυριακής. Σας θυμίζω ότι η παραλαβή των σκουφακιών και των αριθμών γίνεται το Σάββατο, από τις πέντε ως τις οχτώ το απόγευμα, στο γραφείο του ομίλου. Την Κυριακή το πρωί δεν θα δίνουμε πια αριθμούς.", "Good evening, it's Sofia from the sailing club, about Sunday's open-water swim. I'm reminding you that you collect your caps and numbers on Saturday, from five to eight in the evening, at the club office. On Sunday morning we won't be handing out numbers any more."),
  L("Διοργανώτρια", "f", "Μην ξεχάσετε να φέρετε τη βεβαίωση από τον γιατρό σας, γιατί χωρίς αυτήν δεν μπορείτε να αγωνιστείτε. Την Κυριακή, στις επτά και μισή, ένα καΐκι θα σας μεταφέρει από το λιμάνι στην απέναντι ακτή, από όπου ξεκινά ο αγώνας. Ο αριθμός σας θα γραφτεί με μαρκαδόρο στο χέρι σας πριν επιβιβαστείτε.", "Don't forget to bring the certificate from your doctor, because without it you cannot compete. On Sunday, at half past seven, a caïque will take you from the harbour to the opposite shore, where the race starts. Your number will be written on your arm with a marker before you board."),
  L("Διοργανώτρια", "f", "Το πορτοκαλί σκουφάκι είναι υποχρεωτικό, για να σας βλέπουν οι διασώστες στα σκάφη και στα καγιάκ. Αν κουραστείτε ή νιώσετε κράμπα, σηκώστε το χέρι σας ψηλά και περιμένετε· κάποιος θα έρθει αμέσως. Η θερμοκρασία του νερού είναι γύρω στους είκοσι τρεις βαθμούς, οπότε η στολή κατάδυσης δεν είναι απαραίτητη.", "The orange cap is compulsory, so that the lifeguards in the boats and kayaks can see you. If you get tired or feel a cramp, raise your arm high and wait; someone will come straight away. The water temperature is around twenty-three degrees, so a wetsuit isn't necessary."),
  L("Διοργανώτρια", "f", "Τέλος, ο αγώνας γίνεται μόνο αν ο άνεμος δεν ξεπερνά τα πέντε μποφόρ. Την τελική απόφαση θα την ανακοινώσουμε με μήνυμα στο κινητό σας το Σάββατο στις εννιά το βράδυ. Καλή επιτυχία και τα λέμε στο νερό!", "Finally, the race takes place only if the wind doesn't exceed five on the Beaufort scale. We'll announce the final decision by text message to your mobile on Saturday at nine in the evening. Good luck, and see you in the water!"),
 ],
 "questions": [
  Q("Πότε πρέπει να παραλάβετε το σκουφάκι και τον αριθμό σας;", ["Την Κυριακή το πρωί", "Το Σάββατο το απόγευμα", "Στο καΐκι", "Την Παρασκευή"], 1, "η παραλαβή των σκουφακιών και των αριθμών γίνεται το Σάββατο, από τις πέντε ως τις οχτώ"),
  Q("Τι θα γίνει πριν ανεβείτε στο καΐκι;", ["Θα σας δώσουν το σκουφάκι", "Θα σας ζυγίσουν", "Θα γράψουν τον αριθμό σας στο χέρι σας", "Θα ελέγξουν τη στολή σας"], 2, "Ο αριθμός σας θα γραφτεί με μαρκαδόρο στο χέρι σας πριν επιβιβαστείτε"),
  Q("Γιατί είναι υποχρεωτικό το πορτοκαλί σκουφάκι;", ["Για να σας βλέπουν οι διασώστες", "Για να σας προστατεύει από τον ήλιο", "Για να ξεχωρίζουν οι κατηγορίες", "Για τις φωτογραφίες του αγώνα"], 0, "για να σας βλέπουν οι διασώστες"),
  Q("Πώς θα μάθετε αν θα γίνει τελικά ο αγώνας;", ["Από την ιστοσελίδα του ομίλου", "Από ένα τηλεφώνημα την Κυριακή", "Από τις τοπικές ειδήσεις", "Από ένα μήνυμα στο κινητό το Σάββατο το βράδυ"], 3, "θα την ανακοινώσουμε με μήνυμα στο κινητό σας το Σάββατο στις εννιά το βράδυ"),
 ],
 "gloss": {"διάπλου": "διάπλους — open-water crossing (swim)", "κολυμβητικό": "κολυμβητικός — swimming (adj.)", "σκουφακιών": "σκουφάκι — (swimming) cap", "βεβαίωση": "βεβαίωση — certificate", "αγωνιστείτε": "αγωνίζομαι — to compete", "καΐκι": "καΐκι — caïque, small wooden boat", "επιβιβαστείτε": "επιβιβάζομαι — to board", "υποχρεωτικό": "υποχρεωτικός — compulsory", "διασώστες": "διασώστης — rescuer, lifeguard", "κράμπα": "κράμπα — cramp", "στολή κατάδυσης": "στολή κατάδυσης — wetsuit", "μποφόρ": "μποφόρ — (degree on the) Beaufort scale"}
})

ITEMS.append({
 "id": "l266-c1-mono-filtro-kafe", "title": "Ένα σχολικό τετράδιο και ένα τρυπημένο μπρίκι: πώς γεννήθηκε το χάρτινο φίλτρο του καφέ", "title_en": "A school exercise book and a pot full of holes: how the paper coffee filter was born", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από μια ομιλία σε έναν κύκλο εκδηλώσεων για τις εφευρέσεις της καθημερινής ζωής.",
 "script": [
  L("Ομιλήτρια", "f", "Στις αρχές του εικοστού αιώνα, όποιος έφτιαχνε καφέ στη Γερμανία είχε δύο επιλογές, και καμία καλή. Ή έβραζε τον καφέ και έπινε μαζί και το κατακάθι, ή τον περνούσε από ένα υφασμάτινο σακουλάκι, που ήταν δύσκολο να καθαριστεί και άφηνε στο ρόφημα μια γεύση από χθεσινό καφέ.", "At the beginning of the twentieth century, anyone making coffee in Germany had two options, and neither was good. Either they boiled the coffee and drank the grounds along with it, or they passed it through a cloth bag, which was hard to clean and left a taste of yesterday's coffee in the drink."),
  L("Ομιλήτρια", "f", "Η Μελίτα Μπεντς, μια νοικοκυρά από τη Δρέσδη, αποφάσισε να βρει κάτι καλύτερο. Σύμφωνα με την ιστορία που διηγείται η εταιρεία που φέρει ακόμη το όνομά της, άνοιξε με ένα καρφί τρύπες στον πάτο ενός μπρούντζινου δοχείου και έβαλε από πάνω ένα φύλλο στυπόχαρτο από το σχολικό τετράδιο του γιου της.", "Melitta Bentz, a housewife from Dresden, decided to find something better. According to the story told by the company that still bears her name, she punched holes in the bottom of a brass pot with a nail and placed on top a sheet of blotting paper from her son's school exercise book."),
  L("Ομιλήτρια", "f", "Το αποτέλεσμα ήταν ένας καφές καθαρός, χωρίς κατακάθι και με λιγότερη πίκρα. Το 1908 κατοχύρωσε την εφεύρεσή της και ίδρυσε μια μικρή επιχείρηση με ελάχιστο κεφάλαιο· ο σύζυγός της και οι γιοι της έγιναν οι πρώτοι της υπάλληλοι, και τα φίλτρα παρουσιάστηκαν σε μια μεγάλη εμπορική έκθεση στη Λειψία.", "The result was a clean coffee, with no grounds and less bitterness. In 1908 she patented her invention and founded a small business with minimal capital; her husband and sons became her first employees, and the filters were presented at a large trade fair in Leipzig."),
  L("Ομιλήτρια", "f", "Αυτό που μου φαίνεται πιο αξιοσημείωτο δεν είναι η τεχνική λύση, που είναι σχεδόν παιδικά απλή, αλλά το ότι προήλθε από μια γυναίκα που δεν είχε καμία τεχνική εκπαίδευση, σε μια εποχή που οι γυναίκες σπάνια κατοχύρωναν εφευρέσεις. Συχνά, οι καλύτερες ιδέες δεν γεννιούνται στα εργαστήρια, αλλά από την καθημερινή ενόχληση.", "What seems to me most remarkable is not the technical solution, which is almost childishly simple, but the fact that it came from a woman with no technical training at all, at a time when women rarely patented inventions. Often the best ideas are born not in laboratories but from everyday annoyance."),
 ],
 "questions": [
  Q("Ποιο ήταν το πρόβλημα με το υφασμάτινο σακουλάκι;", ["Ήταν πολύ ακριβό", "Ήταν δύσκολο να καθαριστεί και άφηνε γεύση από χθεσινό καφέ", "Έσκιζε εύκολα", "Έκανε τον καφέ πολύ αραιό"], 1, "ήταν δύσκολο να καθαριστεί και άφηνε στο ρόφημα μια γεύση από χθεσινό καφέ"),
  Q("Τι χρησιμοποίησε, σύμφωνα με την ιστορία, η Μελίτα Μπεντς ως φίλτρο;", ["Ένα κομμάτι ύφασμα από ένα σεντόνι", "Ένα κομμάτι εφημερίδα", "Ένα φύλλο στυπόχαρτο από το τετράδιο του γιου της", "Ένα λεπτό μεταλλικό πλέγμα"], 2, "ένα φύλλο στυπόχαρτο από το σχολικό τετράδιο του γιου της"),
  Q("Ποιοι ήταν οι πρώτοι υπάλληλοι της επιχείρησης;", ["Ο σύζυγος και οι γιοι της", "Γειτόνισσες από τη Δρέσδη", "Φοιτητές από τη Λειψία", "Οι αδερφές της"], 0, "ο σύζυγός της και οι γιοι της έγιναν οι πρώτοι της υπάλληλοι"),
  Q("Τι θεωρεί η ομιλήτρια πιο αξιοσημείωτο;", ["Το ότι η εφεύρεση ήταν πολύ σύνθετη", "Το ότι η εταιρεία υπάρχει ακόμη", "Το ότι η ιδέα πουλήθηκε σε άλλους", "Το ότι η ιδέα ήρθε από μια γυναίκα χωρίς τεχνική εκπαίδευση"], 3, "προήλθε από μια γυναίκα που δεν είχε καμία τεχνική εκπαίδευση"),
 ],
 "gloss": {"κατακάθι": "κατακάθι — grounds, sediment", "υφασμάτινο": "υφασμάτινος — cloth (adj.)", "ρόφημα": "ρόφημα — (hot) drink, beverage", "νοικοκυρά": "νοικοκυρά — housewife", "φέρει": "φέρω — to bear (a name)", "καρφί": "καρφί — nail", "μπρούντζινου": "μπρούντζινος — brass, bronze (adj.)", "δοχείου": "δοχείο — pot, container", "στυπόχαρτο": "στυπόχαρτο — blotting paper", "πίκρα": "πίκρα — bitterness", "κατοχύρωσε": "κατοχυρώνω — to patent; to secure (a right)", "ενόχληση": "ενόχληση — annoyance, irritation"}
})

ITEMS.append({
 "id": "l266-c1-int-poulia-se-schima-v", "title": "Γιατί τα αποδημητικά πουλιά πετούν σε σχήμα V; Μια ορνιθολόγος εξηγεί", "title_en": "Why do migrating birds fly in a V? An ornithologist explains", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή για τη φύση.",
 "script": [
  L("Δημοσιογράφος", "m", "Το φθινόπωρο βλέπουμε συχνά πάνω από τους υγροτόπους μας σμήνη πουλιών να πετούν σε σχήμα V. Είναι απλώς σύμπτωση ή υπάρχει λόγος;", "In autumn we often see flocks of birds above our wetlands flying in a V shape. Is it just coincidence, or is there a reason?"),
  L("Ορνιθολόγος", "f", "Υπάρχει, και μάλιστα αεροδυναμικός. Όταν ένα πουλί χτυπά τα φτερά του, στις άκρες τους δημιουργούνται στροβιλισμοί του αέρα· λίγο πιο πίσω και στο πλάι, ο αέρας κινείται προς τα πάνω. Ένα πουλί που πετά ακριβώς σε εκείνο το σημείο «πατάει» σε αυτό το ρεύμα και ξοδεύει λιγότερη ενέργεια.", "There is, and an aerodynamic one at that. When a bird beats its wings, swirls of air form at the wingtips; a little behind and to the side, the air moves upwards. A bird flying exactly in that spot 'steps' on this current and spends less energy."),
  L("Δημοσιογράφος", "m", "Αυτό το ξέραμε θεωρητικά εδώ και καιρό. Έχει αποδειχτεί και στην πράξη;", "We have known that in theory for a long time. Has it been proven in practice too?"),
  L("Ορνιθολόγος", "f", "Για πολλά χρόνια ήταν δύσκολο να μετρηθεί. Μια μελέτη του 2014, όμως, εξόπλισε με μικροσκοπικές συσκευές καταγραφής ένα σμήνος από ίβιδες που είχαν μεγαλώσει με ανθρώπους και ακολουθούσαν ένα υπερελαφρύ αεροσκάφος. Φάνηκε ότι τα πουλιά έπαιρναν σχεδόν ακριβώς τις θέσεις που προβλέπει η θεωρία, και μάλιστα συγχρόνιζαν τα φτεροκοπήματά τους με εκείνο που πετούσε μπροστά.", "For many years it was hard to measure. A 2014 study, however, fitted tiny data loggers to a flock of ibises that had been raised by humans and were following a microlight aircraft. It turned out that the birds took almost exactly the positions the theory predicts, and they even synchronised their wingbeats with the bird flying in front."),
  L("Δημοσιογράφος", "m", "Και το πουλί που πετά πρώτο; Αυτό δεν κουράζεται περισσότερο;", "And the bird flying first? Doesn't it get more tired?"),
  L("Ορνιθολόγος", "f", "Ακριβώς, και γι’ αυτό, τουλάχιστον σε ορισμένα είδη, τα πουλιά αλλάζουν θέσεις: όποιος κουραστεί στην κορυφή περνάει πίσω. Στη μελέτη με τις ίβιδες, μάλιστα, τα πουλιά φαίνεται ότι περνούσαν στην μπροστινή θέση περίπου για όσο χρόνο είχαν «κερδίσει» πετώντας πίσω από άλλα. Είναι ένα είδος δίκαιης ανταλλαγής, χωρίς κανέναν να την οργανώνει.", "Exactly, and that's why, at least in some species, the birds swap positions: whoever gets tired at the front moves to the back. In the ibis study, in fact, the birds seemed to spend roughly as much time in the front position as they had 'gained' by flying behind others. It's a kind of fair exchange, with nobody organising it."),
 ],
 "questions": [
  Q("Τι συμβαίνει λίγο πιο πίσω και στο πλάι από τις άκρες των φτερών;", ["Ο αέρας γίνεται πιο κρύος", "Ο αέρας κινείται προς τα πάνω", "Ο αέρας σταματά εντελώς", "Ο αέρας κινείται προς τα κάτω"], 1, "λίγο πιο πίσω και στο πλάι, ο αέρας κινείται προς τα πάνω"),
  Q("Γιατί οι ίβιδες της μελέτης ήταν κατάλληλες για μετρήσεις;", ["Γιατί πετούσαν πολύ χαμηλά", "Γιατί ήταν πολύ μεγάλα πουλιά", "Γιατί είχαν μεγαλώσει με ανθρώπους και ακολουθούσαν ένα αεροσκάφος", "Γιατί ζούσαν σε ζωολογικό κήπο"], 2, "ίβιδες που είχαν μεγαλώσει με ανθρώπους και ακολουθούσαν ένα υπερελαφρύ αεροσκάφος"),
  Q("Τι έδειξε η μελέτη για τα φτεροκοπήματα;", ["Ότι τα πουλιά τα συγχρόνιζαν με εκείνο που πετούσε μπροστά", "Ότι γίνονταν πιο γρήγορα στην κορυφή", "Ότι ήταν εντελώς τυχαία", "Ότι σταματούσαν όταν φυσούσε"], 0, "συγχρόνιζαν τα φτεροκοπήματά τους με εκείνο που πετούσε μπροστά"),
  Q("Τι λέει η ορνιθολόγος για την αλλαγή θέσεων;", ["Ότι την οργανώνει το μεγαλύτερο πουλί", "Ότι συμβαίνει μόνο όταν βρέχει", "Ότι τα νεαρά πουλιά πετούν πάντα μπροστά", "Ότι είναι ένα είδος δίκαιης ανταλλαγής χωρίς οργανωτή"], 3, "Είναι ένα είδος δίκαιης ανταλλαγής, χωρίς κανέναν να την οργανώνει"),
 ],
 "gloss": {"υγροτόπους": "υγρότοπος — wetland", "σμήνη": "σμήνος — flock, swarm", "σύμπτωση": "σύμπτωση — coincidence", "αεροδυναμικός": "αεροδυναμικός — aerodynamic", "στροβιλισμοί": "στροβιλισμός — swirl, vortex", "εξόπλισε": "εξοπλίζω — to equip, fit", "συσκευές καταγραφής": "συσκευή καταγραφής — data logger", "ίβιδες": "ίβιδα — ibis", "υπερελαφρύ": "υπερελαφρύς — ultralight, microlight", "συγχρόνιζαν": "συγχρονίζω — to synchronise", "φτεροκοπήματά": "φτεροκόπημα — wingbeat", "ανταλλαγής": "ανταλλαγή — exchange"}
})

rnd = random.Random(266)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-266.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
