# Source for library/listening/listening-98.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l98.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l98-ann-rypansi-paralia", "title": "Απαγόρευση κολύμβησης στην παραλία", "title_en": "No swimming at the beach", "type": "announcement", "level": "B2",
 "context_el": "Είστε σε μια οργανωμένη παραλία το πρωί. Ακούτε μια ανακοίνωση του δήμου από τα μεγάφωνα.",
 "script": [
  L("Εκφωνήτρια", "f", "Προσοχή, παρακαλώ. Ο δήμος ενημερώνει τους λουόμενους ότι από σήμερα το πρωί απαγορεύεται προσωρινά η κολύμβηση στο τμήμα της παραλίας ανάμεσα στο λιμανάκι και στο ναυτικό καφέ. Κατά τη διάρκεια της νύχτας, λόγω βλάβης σε έναν αγωγό, διέρρευσαν λύματα στη θάλασσα.", "Attention, please. The municipality informs bathers that from this morning swimming is temporarily forbidden on the part of the beach between the small harbour and the nautical café. During the night, because of damage to a pipe, waste water leaked into the sea."),
  L("Εκφωνήτρια", "f", "Τα συνεργεία του δήμου εργάζονται ήδη για την επισκευή της βλάβης, και κλιμάκιο της υγειονομικής υπηρεσίας πήρε δείγματα νερού, τα αποτελέσματα των οποίων αναμένονται μέσα σε σαράντα οκτώ ώρες. Μέχρι τότε, παρακαλούμε να μην μπαίνετε στη θάλασσα και να μην αφήνετε τα παιδιά να παίζουν στην άκρη του νερού.", "Municipal crews are already working to repair the damage, and a team from the health service has taken water samples, the results of which are expected within forty-eight hours. Until then, please do not go into the sea and do not let children play at the water's edge."),
  L("Εκφωνήτρια", "f", "Το υπόλοιπο τμήμα της παραλίας, ανατολικά του λιμανιού, είναι ασφαλές και ανοιχτό κανονικά. Η ξαπλώστρα και η ομπρέλα εκεί θα κοστίζουν σήμερα στο μισό, για όσους μετακινηθούν από την κλειστή ζώνη. Ευχαριστούμε για την κατανόηση.", "The rest of the beach, east of the harbour, is safe and open as usual. Sunbeds and umbrellas there will cost half price today for those moving from the closed area. Thank you for your understanding."),
 ],
 "questions": [
  Q("Γιατί απαγορεύεται η κολύμβηση;", ["Λόγω μεδουσών", "Λόγω δυνατού ανέμου", "Γιατί διέρρευσαν λύματα από έναν χαλασμένο αγωγό", "Γιατί γίνονται έργα στο λιμάνι"], 2, "λόγω βλάβης σε έναν αγωγό, διέρρευσαν λύματα στη θάλασσα"),
  Q("Πότε αναμένονται τα αποτελέσματα των δειγμάτων;", ["Μέσα σε σαράντα οκτώ ώρες", "Σήμερα το απόγευμα", "Σε μία εβδομάδα", "Αύριο το πρωί"], 0, "αναμένονται μέσα σε σαράντα οκτώ ώρες"),
  Q("Τι προσφέρεται σε όσους μετακινηθούν ανατολικά του λιμανιού;", ["Δωρεάν καφές", "Ξαπλώστρα και ομπρέλα στη μισή τιμή", "Δωρεάν στάθμευση", "Μεταφορά με λεωφορείο"], 1, "θα κοστίζουν σήμερα στο μισό"),
 ],
 "gloss": {"λουόμενους": "λουόμενος — bather", "κολύμβηση": "κολύμβηση — swimming", "βλάβης": "βλάβη — damage, fault", "αγωγό": "αγωγός — pipe", "διέρρευσαν": "διαρρέω — to leak", "λύματα": "λύματα — sewage, waste water", "συνεργεία": "συνεργείο — (work) crew", "κλιμάκιο": "κλιμάκιο — team, unit", "δείγματα": "δείγμα — sample", "ξαπλώστρα": "ξαπλώστρα — sunbed", "κατανόηση": "κατανόηση — understanding"}
})
ITEMS.append({
 "id": "l98-vm-maestros-chorodias", "title": "Μήνυμα από τη μαέστρο της χορωδίας", "title_en": "A message from the choir conductor", "type": "voicemail", "level": "B2",
 "context_el": "Τραγουδάτε σε μια ερασιτεχνική χορωδία. Ακούτε ένα μήνυμα από τη μαέστρο στον τηλεφωνητή σας.",
 "script": [
  L("Μαέστρος", "f", "Γεια σου, Κατερίνα, η Ελπίδα είμαι, από τη χορωδία. Σου τηλεφωνώ γιατί αλλάζει κάτι για τη συναυλία των Χριστουγέννων. Η εκκλησία όπου θα τραγουδούσαμε έχει εργασίες, οπότε η συναυλία θα γίνει τελικά στην αίθουσα του Πνευματικού Κέντρου, την ίδια μέρα και ώρα.", "Hi, Katerina, it's Elpida, from the choir. I'm calling because something is changing for the Christmas concert. The church where we were going to sing is having work done, so the concert will finally take place in the hall of the Cultural Centre, same day and time."),
  L("Μαέστρος", "f", "Η αίθουσα έχει άλλη ακουστική, πιο «στεγνή», και γι' αυτό θα χρειαστούμε μία έξτρα πρόβα, την Πέμπτη στις οχτώ, επιτόπου, για να συνηθίσουμε τον χώρο. Ξέρω ότι είναι λίγο τελευταία στιγμή, αλλά είναι σημαντικό να έρθουν όλοι, ιδίως οι άλτο, γιατί είστε λίγες φέτος.", "The hall has different acoustics, 'drier', so we'll need one extra rehearsal, on Thursday at eight, on site, to get used to the space. I know it's a bit last-minute, but it's important that everyone comes, especially the altos, because there are only a few of you this year."),
  L("Μαέστρος", "f", "Και κάτι ακόμα: για τη συναυλία φοράμε μαύρο από πάνω ως κάτω, αλλά φέτος θα βάλουμε κι ένα κόκκινο φουλάρι, που θα το μοιράσω εγώ την Πέμπτη. Αν δεν μπορείς να έρθεις στην πρόβα, στείλε μου ένα μήνυμα, να σου το κρατήσω. Τα λέμε!", "And one more thing: for the concert we wear black from head to toe, but this year we'll also put on a red scarf, which I'll hand out on Thursday. If you can't come to the rehearsal, send me a message so I can keep one for you. See you!"),
 ],
 "questions": [
  Q("Γιατί αλλάζει ο χώρος της συναυλίας;", ["Γιατί η εκκλησία έχει εργασίες", "Γιατί η αίθουσα είναι μεγαλύτερη", "Γιατί άλλαξε η ημερομηνία", "Γιατί το ζήτησε ο δήμος"], 0, "Η εκκλησία όπου θα τραγουδούσαμε έχει εργασίες"),
  Q("Γιατί χρειάζεται έξτρα πρόβα;", ["Γιατί υπάρχουν καινούργια τραγούδια", "Για να συνηθίσουν την ακουστική του νέου χώρου", "Γιατί λείπει η μαέστρος", "Για να γίνει φωτογράφιση"], 1, "για να συνηθίσουμε τον χώρο"),
  Q("Τι θα φορέσουν φέτος στη συναυλία;", ["Μόνο λευκά", "Κόκκινα φορέματα", "Μαύρα ρούχα και ένα κόκκινο φουλάρι", "Παραδοσιακές στολές"], 2, "φοράμε μαύρο από πάνω ως κάτω, αλλά φέτος θα βάλουμε κι ένα κόκκινο φουλάρι"),
 ],
 "gloss": {"ερασιτεχνική": "ερασιτεχνικός — amateur", "χορωδία": "χορωδία — choir", "μαέστρο": "μαέστρος — conductor", "συναυλία": "συναυλία — concert", "αίθουσα": "αίθουσα — hall", "ακουστική": "ακουστική — acoustics", "πρόβα": "πρόβα — rehearsal", "επιτόπου": "επιτόπου — on site", "άλτο": "άλτο — alto", "φουλάρι": "φουλάρι — scarf"}
})
ITEMS.append({
 "id": "l98-dia-krasi", "title": "Ένα κρασί για το τραπέζι", "title_en": "A wine for dinner", "type": "dialogue", "level": "B2",
 "context_el": "Μια γυναίκα μπαίνει σε ένα κατάστημα με κρασιά, για να αγοράσει ένα μπουκάλι για ένα δείπνο.",
 "script": [
  L("Πελάτισσα", "f", "Καλησπέρα. Είμαι καλεσμένη απόψε σε φίλους για φαγητό και θέλω να πάρω ένα κρασί, αλλά δεν ξέρω πολλά. Μπορείτε να με βοηθήσετε;", "Good evening. I'm invited to friends' tonight for dinner and I want to take a wine, but I don't know much. Can you help me?"),
  L("Πωλητής", "m", "Ναι, ευχαρίστως. Ξέρετε τι θα φάτε; Αυτό είναι το πιο σημαντικό.", "Gladly. Do you know what you'll be eating? That's the most important thing."),
  L("Πελάτισσα", "f", "Μου είπαν ότι θα φτιάξουν ψάρι στον φούρνο με λαχανικά. Σκεφτόμουν ένα κόκκινο, γιατί μου αρέσει περισσότερο.", "They told me they'll make baked fish with vegetables. I was thinking of a red, because I like it more."),
  L("Πωλητής", "m", "Με ψάρι στον φούρνο θα σας πρότεινα ένα λευκό, ένα ασύρτικο από τη Σαντορίνη, για παράδειγμα, που έχει ωραία οξύτητα και ταιριάζει πολύ με το λεμόνι και το λάδι. Αν, όμως, προτιμάτε οπωσδήποτε κόκκινο, να πάρετε κάτι ελαφρύ, όπως ένα ξινόμαυρο ή ένα αγιωργίτικο, και να το σερβίρετε λίγο δροσερό.", "With baked fish I'd suggest a white, an Assyrtiko from Santorini, for example, which has nice acidity and goes very well with lemon and oil. But if you really prefer red, take something light, like a Xinomavro or an Agiorgitiko, and serve it slightly cool."),
  L("Πελάτισσα", "f", "Πόσο κάνει το ασύρτικο;", "How much is the Assyrtiko?"),
  L("Πωλητής", "m", "Αυτό εδώ είναι δεκαοκτώ ευρώ. Έχω κι ένα άλλο, από μικρότερο οινοποιείο, στα δώδεκα, που είναι πολύ καλό για την τιμή του. Και να σας πω κάτι; Βάλτε το στο ψυγείο μόλις φτάσετε, γιατί στο αυτοκίνητο θα ζεσταθεί.", "This one here is eighteen euros. I also have another one, from a smaller winery, at twelve, which is very good for the price. And let me tell you something: put it in the fridge as soon as you arrive, because it will warm up in the car."),
 ],
 "questions": [
  Q("Τι κρασί προτείνει ο πωλητής με το ψάρι;", ["Ένα βαρύ κόκκινο", "Ένα λευκό ασύρτικο", "Ένα γλυκό κρασί", "Ένα ροζέ"], 1, "θα σας πρότεινα ένα λευκό, ένα ασύρτικο"),
  Q("Αν η πελάτισσα θέλει οπωσδήποτε κόκκινο, τι της συμβουλεύει;", ["Να πάρει κάτι ελαφρύ και να το σερβίρει λίγο δροσερό", "Να πάρει το πιο ακριβό", "Να το σερβίρει ζεστό", "Να πάρει δύο μπουκάλια"], 0, "να πάρετε κάτι ελαφρύ"),
  Q("Γιατί πρέπει να βάλει το κρασί στο ψυγείο;", ["Γιατί είναι λευκό και πρέπει να παγώσει πολύ", "Γιατί θα ζεσταθεί στο αυτοκίνητο", "Γιατί το ζήτησαν οι φίλοι της", "Γιατί είναι από μικρό οινοποιείο"], 1, "στο αυτοκίνητο θα ζεσταθεί"),
 ],
 "gloss": {"καλεσμένη": "καλεσμένος — invited", "ευχαρίστως": "ευχαρίστως — gladly", "ασύρτικο": "ασύρτικο — Assyrtiko (white grape of Santorini)", "οξύτητα": "οξύτητα — acidity", "ταιριάζει": "ταιριάζω — to go well with", "οπωσδήποτε": "οπωσδήποτε — definitely, at all costs", "ξινόμαυρο": "ξινόμαυρο — Xinomavro (red grape)", "αγιωργίτικο": "αγιωργίτικο — Agiorgitiko (red grape)", "δροσερό": "δροσερός — cool", "οινοποιείο": "οινοποιείο — winery"}
})
ITEMS.append({
 "id": "l98-int-oinologos", "title": "Μια νεαρή οινολόγος", "title_en": "A young oenologist", "type": "interview", "level": "B2",
 "context_el": "Σε μια εκπομπή για τη γεωργία, ένας δημοσιογράφος μιλά με μια οινολόγο που δουλεύει σε ένα οινοποιείο της Νεμέας.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς κάνει ένας οινολόγος;", "What exactly does an oenologist do?"),
  L("Οινολόγος", "f", "Πολλοί νομίζουν ότι απλώς δοκιμάζουμε κρασιά όλη μέρα! Στην πραγματικότητα, παρακολουθούμε όλη τη διαδικασία, από το αμπέλι μέχρι το μπουκάλι. Αποφασίζουμε πότε θα γίνει ο τρύγος, ελέγχουμε τη ζύμωση, κάνουμε αναλύσεις στο εργαστήριο. Το μεγαλύτερο μέρος της δουλειάς μου είναι, στην ουσία, χημεία.", "Many people think we just taste wines all day! In reality, we oversee the whole process, from the vineyard to the bottle. We decide when the harvest will take place, monitor the fermentation, do analyses in the laboratory. Most of my work is, essentially, chemistry."),
  L("Δημοσιογράφος", "m", "Πώς αποφασίζετε πότε θα γίνει ο τρύγος;", "How do you decide when the harvest will take place?"),
  L("Οινολόγος", "f", "Τις τελευταίες εβδομάδες του καλοκαιριού γυρίζω στα αμπέλια σχεδόν κάθε μέρα. Μετράω τα σάκχαρα και την οξύτητα του σταφυλιού, αλλά δοκιμάζω και τις ρώγες, κοιτάζω τα κουκούτσια: όταν γίνουν καφετιά, είναι καλό σημάδι. Τα τελευταία χρόνια, με τη ζέστη, ο τρύγος γίνεται όλο και νωρίτερα, και αυτό μας ανησυχεί πολύ.", "In the last weeks of summer I go round the vineyards almost every day. I measure the sugars and acidity of the grapes, but I also taste the berries and look at the pips: when they turn brown, that's a good sign. In recent years, with the heat, the harvest has been getting earlier and earlier, and that worries us a lot."),
  L("Δημοσιογράφος", "m", "Δεν είναι συνηθισμένο να βλέπουμε τόσο νέους ανθρώπους σε αυτόν τον χώρο.", "It's not common to see such young people in this field."),
  L("Οινολόγος", "f", "Αυτό αλλάζει. Στη σχολή μου, οι μισοί φοιτητές ήταν γυναίκες. Και πολλοί νέοι επιστρέφουν στα χωριά τους για να συνεχίσουν τα αμπέλια των παππούδων τους, αλλά με νέες γνώσεις. Εγώ, για παράδειγμα, δουλεύω με τις ίδιες ποικιλίες που καλλιεργούσε ο παππούς μου, αλλά με εντελώς διαφορετικό τρόπο.", "That's changing. In my school, half the students were women. And many young people are going back to their villages to continue their grandparents' vineyards, but with new knowledge. I, for example, work with the same varieties my grandfather grew, but in a completely different way."),
 ],
 "questions": [
  Q("Τι λέει για το μεγαλύτερο μέρος της δουλειάς της;", ["Ότι είναι η δοκιμή κρασιών", "Ότι είναι, στην ουσία, χημεία", "Ότι είναι οι πωλήσεις", "Ότι είναι η φροντίδα των αμπελιών"], 1, "Το μεγαλύτερο μέρος της δουλειάς μου είναι, στην ουσία, χημεία"),
  Q("Ποιο είναι καλό σημάδι για τον τρύγο;", ["Όταν τα κουκούτσια γίνουν καφετιά", "Όταν πέσουν τα φύλλα", "Όταν βρέξει", "Όταν οι ρώγες γίνουν πράσινες"], 0, "όταν γίνουν καφετιά, είναι καλό σημάδι"),
  Q("Τι ανησυχεί τους οινολόγους τα τελευταία χρόνια;", ["Η έλλειψη εργατών", "Οι χαμηλές τιμές", "Ότι ο τρύγος γίνεται όλο και νωρίτερα λόγω της ζέστης", "Οι ασθένειες των αμπελιών"], 2, "ο τρύγος γίνεται όλο και νωρίτερα, και αυτό μας ανησυχεί πολύ"),
 ],
 "gloss": {"οινολόγο": "οινολόγος — oenologist", "αμπέλι": "αμπέλι — vineyard, vine", "τρύγος": "τρύγος — grape harvest", "ζύμωση": "ζύμωση — fermentation", "αναλύσεις": "ανάλυση — analysis", "σάκχαρα": "σάκχαρα — sugars", "ρώγες": "ρώγα — grape (single berry)", "κουκούτσια": "κουκούτσι — pip, seed", "καφετιά": "καφετής — brown", "ποικιλίες": "ποικιλία — variety"}
})
ITEMS.append({
 "id": "l98-rep-kavala-kapnos", "title": "Η Καβάλα του καπνού", "title_en": "Tobacco-era Kavala", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για τις ελληνικές πόλεις και την ιστορία τους.",
 "script": [
  L("Ρεπόρτερ", "m", "Όποιος περπατά στο κέντρο της Καβάλας θα προσέξει μεγάλα, επιβλητικά κτίρια με πολλά παράθυρα, που μοιάζουν περισσότερο με αρχοντικά παρά με εργοστάσια. Είναι οι παλιές καπναποθήκες, ζωντανά μνημεία μιας εποχής όταν η Καβάλα ήταν ένα από τα σημαντικότερα κέντρα του εμπορίου καπνού στην ανατολική Μεσόγειο.", "Anyone walking in the centre of Kavala will notice large, imposing buildings with many windows, which look more like mansions than factories. They are the old tobacco warehouses, living monuments of an era when Kavala was one of the most important centres of the tobacco trade in the eastern Mediterranean."),
  L("Ρεπόρτερ", "m", "Στα τέλη του δέκατου ένατου και στις αρχές του εικοστού αιώνα, χιλιάδες εργάτες, πολλοί από αυτούς γυναίκες, δούλευαν εκεί για να επεξεργαστούν τα φύλλα του καπνού. Οι συνθήκες ήταν σκληρές: η σκόνη του καπνού γέμιζε τους χώρους, και πολλοί αρρώσταιναν. Οι καπνεργάτες της Καβάλας οργάνωσαν μερικές από τις μεγαλύτερες εργατικές κινητοποιήσεις της εποχής.", "In the late nineteenth and early twentieth centuries, thousands of workers, many of them women, worked there processing the tobacco leaves. Conditions were harsh: tobacco dust filled the rooms, and many fell ill. Kavala's tobacco workers organised some of the largest labour movements of the period."),
  L("Ρεπόρτερ", "m", "Σήμερα, πολλές από τις καπναποθήκες έχουν αποκτήσει νέα ζωή. Σε μία από αυτές στεγάζεται το Μουσείο Καπνού, όπου ο επισκέπτης μπορεί να δει εργαλεία, φωτογραφίες και δείγματα φύλλων. Άλλες έχουν γίνει αίθουσες συναυλιών, γραφεία ή χώροι του πανεπιστημίου, και έτσι η μνήμη της πόλης δεν χάνεται.", "Today many of the tobacco warehouses have acquired new life. One of them houses the Tobacco Museum, where visitors can see tools, photographs and samples of leaves. Others have become concert halls, offices or university premises, and so the city's memory is not lost."),
 ],
 "questions": [
  Q("Με τι μοιάζουν οι παλιές καπναποθήκες;", ["Με εκκλησίες", "Με αρχοντικά", "Με σχολεία", "Με αποθήκες λιμανιού"], 1, "μοιάζουν περισσότερο με αρχοντικά παρά με εργοστάσια"),
  Q("Πώς ήταν οι συνθήκες εργασίας;", ["Σκληρές, με πολλή σκόνη", "Καλές, με υψηλούς μισθούς", "Εύκολες, γιατί δούλευαν λίγες ώρες", "Δεν αναφέρεται"], 0, "Οι συνθήκες ήταν σκληρές"),
  Q("Τι στεγάζεται σήμερα σε μία από τις καπναποθήκες;", ["Ένα ξενοδοχείο", "Ένα εργοστάσιο τσιγάρων", "Το Μουσείο Καπνού", "Το δημαρχείο"], 2, "στεγάζεται το Μουσείο Καπνού"),
 ],
 "gloss": {"επιβλητικά": "επιβλητικός — imposing", "αρχοντικά": "αρχοντικό — mansion", "καπναποθήκες": "καπναποθήκη — tobacco warehouse", "μνημεία": "μνημείο — monument, reminder", "εμπορίου": "εμπόριο — trade", "επεξεργαστούν": "επεξεργάζομαι — to process", "σκόνη": "σκόνη — dust", "καπνεργάτες": "καπνεργάτης — tobacco worker", "κινητοποιήσεις": "κινητοποίηση — mobilisation, protest", "στεγάζεται": "στεγάζομαι — to be housed"}
})
ITEMS.append({
 "id": "l98-rep-elaionas-amfissas", "title": "Μια θάλασσα από ελιές", "title_en": "A sea of olive trees", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για το ελληνικό τοπίο.",
 "script": [
  L("Ρεπόρτερ", "f", "Όποιος κοιτάξει από τους Δελφούς προς τη θάλασσα θα δει μια ασημοπράσινη πεδιάδα που φτάνει ως τον κόλπο της Ιτέας. Είναι ο ελαιώνας της Άμφισσας, ένας από τους μεγαλύτερους της Ελλάδας, με περισσότερα από ένα εκατομμύριο δέντρα. Κάποια από αυτά, λένε οι ντόπιοι, είναι αιώνων.", "Anyone who looks from Delphi towards the sea will see a silvery-green plain stretching to the Gulf of Itea. It's the olive grove of Amfissa, one of the largest in Greece, with more than a million trees. Some of them, the locals say, are centuries old."),
  L("Ρεπόρτερ", "f", "Η περιοχή είναι γνωστή κυρίως για τις βρώσιμες ελιές της, την κονσερβολιά Αμφίσσης, που είναι προϊόν προστατευόμενης ονομασίας προέλευσης. Ο κύριος Γιάννης, παραγωγός τρίτης γενιάς, μας εξηγεί ότι η συγκομιδή γίνεται ακόμα με το χέρι, γιατί οι ελιές που προορίζονται για το τραπέζι πρέπει να μείνουν άθικτες, χωρίς χτυπήματα.", "The area is known mainly for its table olives, the Amfissa konservolia, a product with protected designation of origin. Mr Giannis, a third-generation grower, explains that the harvest is still done by hand, because olives intended for the table must stay intact, without bruises."),
  L("Ρεπόρτερ", "f", "Ο ελαιώνας δεν είναι μόνο πηγή εισοδήματος. Το καλοκαίρι, η σκιά του προσφέρει δροσιά, και τα μονοπάτια του είναι αγαπημένα από πεζοπόρους και ποδηλάτες. Οι κάτοικοι, όμως, ανησυχούν: πολλοί νέοι δεν θέλουν να συνεχίσουν τη δουλειά, και κάποια χωράφια έχουν αρχίσει να μένουν απεριποίητα.", "The olive grove is not only a source of income. In summer its shade offers coolness, and its paths are popular with hikers and cyclists. The residents, however, are worried: many young people don't want to carry on the work, and some fields have started to be left untended."),
 ],
 "questions": [
  Q("Πόσα δέντρα έχει ο ελαιώνας;", ["Περίπου εκατό χιλιάδες", "Περισσότερα από ένα εκατομμύριο", "Δέκα χιλιάδες", "Πεντακόσια"], 1, "με περισσότερα από ένα εκατομμύριο δέντρα"),
  Q("Γιατί η συγκομιδή γίνεται ακόμα με το χέρι;", ["Γιατί οι ελιές του τραπεζιού πρέπει να μείνουν άθικτες", "Γιατί τα μηχανήματα είναι ακριβά", "Γιατί το απαιτεί ο νόμος", "Γιατί τα δέντρα είναι πολύ ψηλά"], 0, "οι ελιές που προορίζονται για το τραπέζι πρέπει να μείνουν άθικτες"),
  Q("Τι ανησυχεί τους κατοίκους;", ["Οι πυρκαγιές", "Οι χαμηλές τιμές", "Ότι πολλοί νέοι δεν θέλουν να συνεχίσουν τη δουλειά", "Ο τουρισμός"], 2, "πολλοί νέοι δεν θέλουν να συνεχίσουν τη δουλειά"),
 ],
 "gloss": {"ασημοπράσινη": "ασημοπράσινος — silvery green", "πεδιάδα": "πεδιάδα — plain", "ελαιώνας": "ελαιώνας — olive grove", "ντόπιοι": "ντόπιος — local", "βρώσιμες": "βρώσιμος — edible (βρώσιμες ελιές: table olives)", "ονομασίας προέλευσης": "προστατευόμενη ονομασία προέλευσης — protected designation of origin (PDO)", "συγκομιδή": "συγκομιδή — harvest", "άθικτες": "άθικτος — intact", "εισοδήματος": "εισόδημα — income", "απεριποίητα": "απεριποίητος — untended, neglected"}
})
ITEMS.append({
 "id": "l98-mono-syntaxi", "title": "Η πρώτη μου εβδομάδα στη σύνταξη", "title_en": "My first week of retirement", "type": "monologue", "level": "B2",
 "context_el": "Σε μια εκπομπή για τη ζωή μετά τα εξήντα, μια ακροάτρια μιλά για τις πρώτες μέρες της σύνταξής της.",
 "script": [
  L("Ακροάτρια", "f", "Δούλεψα τριάντα πέντε χρόνια ως λογίστρια στην ίδια εταιρεία. Για χρόνια ονειρευόμουν τη μέρα που θα έβγαινα στη σύνταξη: θα κοιμόμουν όσο ήθελα, θα διάβαζα, θα ταξίδευα. Την πρώτη Δευτέρα, όμως, ξύπνησα στις επτά παρά τέταρτο, όπως πάντα, και δεν ήξερα τι να κάνω με τον εαυτό μου.", "I worked thirty-five years as an accountant at the same company. For years I dreamed of the day I'd retire: I'd sleep as long as I wanted, read, travel. On the first Monday, though, I woke up at a quarter to seven, as always, and didn't know what to do with myself."),
  L("Ακροάτρια", "f", "Την Τρίτη καθάρισα όλο το σπίτι. Την Τετάρτη ξανακαθάρισα τα ντουλάπια της κουζίνας. Την Πέμπτη ο άντρας μου, που είχε βγει στη σύνταξη δύο χρόνια νωρίτερα, μου είπε γελώντας: «Χρειάζεσαι πρόγραμμα, αλλιώς θα τρελαθείς εσύ και θα τρελάνεις κι εμένα.» Είχε δίκιο.", "On Tuesday I cleaned the whole house. On Wednesday I cleaned the kitchen cupboards again. On Thursday my husband, who had retired two years earlier, said to me laughing: 'You need a schedule, otherwise you'll go mad and drive me mad too.' He was right."),
  L("Ακροάτρια", "f", "Έτσι, την Παρασκευή γράφτηκα σε ένα μάθημα ιταλικών στο ΚΑΠΗ της γειτονιάς και σε μια ομάδα πεζοπορίας που βγαίνει κάθε Κυριακή. Ακόμα συνηθίζω. Αλλά έμαθα ότι η ελευθερία δεν είναι να μην έχεις τίποτα να κάνεις· είναι να διαλέγεις μόνος σου τι θα κάνεις.", "So on Friday I signed up for an Italian class at the neighbourhood senior citizens' centre and for a hiking group that goes out every Sunday. I'm still getting used to it. But I've learned that freedom isn't having nothing to do; it's choosing for yourself what you'll do."),
 ],
 "questions": [
  Q("Τι έγινε την πρώτη Δευτέρα της σύνταξης;", ["Κοιμήθηκε ως το μεσημέρι", "Ξύπνησε νωρίς, όπως πάντα, και δεν ήξερε τι να κάνει", "Έφυγε για ταξίδι", "Πήγε στην παλιά της δουλειά"], 1, "ξύπνησα στις επτά παρά τέταρτο, όπως πάντα, και δεν ήξερα τι να κάνω"),
  Q("Τι της είπε ο άντρας της;", ["Ότι χρειάζεται πρόγραμμα", "Ότι πρέπει να ξαναβρεί δουλειά", "Ότι το σπίτι δεν είναι καθαρό", "Ότι πρέπει να ξεκουραστεί"], 0, "Χρειάζεσαι πρόγραμμα"),
  Q("Πώς ορίζει τώρα την ελευθερία;", ["Να μην έχεις τίποτα να κάνεις", "Να ταξιδεύεις συνέχεια", "Να διαλέγεις μόνος σου τι θα κάνεις", "Να κοιμάσαι όσο θέλεις"], 2, "είναι να διαλέγεις μόνος σου τι θα κάνεις"),
 ],
 "gloss": {"σύνταξη": "σύνταξη — pension, retirement", "λογίστρια": "λογίστρια — accountant (f.)", "ονειρευόμουν": "ονειρεύομαι — to dream", "ντουλάπια": "ντουλάπι — cupboard", "τρελαθείς": "τρελαίνομαι — to go mad", "γράφτηκα": "γράφομαι — to sign up, enrol", "ΚΑΠΗ": "ΚΑΠΗ — community centre for older people", "πεζοπορίας": "πεζοπορία — hiking", "συνηθίζω": "συνηθίζω — to get used to"}
})
ITEMS.append({
 "id": "l98-mono-emfialomeno", "title": "Δεν αγοράζω πια νερό σε μπουκάλια", "title_en": "I no longer buy bottled water", "type": "monologue", "level": "B2",
 "context_el": "Σε μια εκπομπή για το περιβάλλον, ένας ακροατής μιλά για μια αλλαγή στις συνήθειές του.",
 "script": [
  L("Ακροατής", "m", "Μέχρι πέρσι αγόραζα κάθε εβδομάδα δύο εξάδες με μπουκάλια νερό. Δεν το σκεφτόμουν καν. Μια μέρα, όμως, καθάρισα την αποθήκη και βρήκα δύο μεγάλες σακούλες γεμάτες άδεια πλαστικά μπουκάλια, που περίμεναν να πάνε στην ανακύκλωση. Εκείνη τη στιγμή κατάλαβα πόσο πλαστικό πετούσα χωρίς λόγο.", "Until last year I bought two six-packs of bottled water every week. I didn't even think about it. One day, though, I cleaned out the storeroom and found two big bags full of empty plastic bottles waiting to go for recycling. At that moment I realised how much plastic I was throwing away for no reason."),
  L("Ακροατής", "m", "Το νερό της βρύσης στην πόλη μου είναι πόσιμο και ελέγχεται τακτικά, αλλά εγώ δεν το εμπιστευόμουν, κυρίως λόγω της γεύσης του χλωρίου. Ρώτησα έναν φίλο χημικό, και μου είπε κάτι απλό: αν αφήσεις το νερό σε μια κανάτα στο ψυγείο για λίγες ώρες, η μυρωδιά φεύγει σχεδόν εντελώς.", "The tap water in my city is drinkable and regularly tested, but I didn't trust it, mainly because of the taste of chlorine. I asked a chemist friend, and he told me something simple: if you leave the water in a jug in the fridge for a few hours, the smell almost completely goes away."),
  L("Ακροατής", "m", "Έτσι αγόρασα δύο γυάλινες κανάτες και ένα μεταλλικό παγούρι για τη δουλειά. Υπολόγισα ότι εξοικονομώ πάνω από διακόσια ευρώ τον χρόνο. Δεν λέω ότι έτσι σώζω τον πλανήτη, αλλά τουλάχιστον δεν κουβαλάω πια εξάδες από το σούπερ μάρκετ ως τον τρίτο όροφο.", "So I bought two glass jugs and a metal water bottle for work. I calculated that I save more than two hundred euros a year. I'm not saying I'm saving the planet this way, but at least I no longer carry six-packs from the supermarket up to the third floor."),
 ],
 "questions": [
  Q("Τι τον έκανε να αλλάξει συνήθεια;", ["Ένα άρθρο που διάβασε", "Οι σακούλες με άδεια μπουκάλια που βρήκε στην αποθήκη", "Η αύξηση της τιμής του νερού", "Μια συμβουλή του γιατρού"], 1, "βρήκα δύο μεγάλες σακούλες γεμάτες άδεια πλαστικά μπουκάλια"),
  Q("Γιατί δεν εμπιστευόταν το νερό της βρύσης;", ["Λόγω της γεύσης του χλωρίου", "Γιατί δεν ελέγχεται", "Γιατί είναι θολό", "Γιατί οι σωλήνες είναι παλιοί"], 0, "κυρίως λόγω της γεύσης του χλωρίου"),
  Q("Τι συμβουλή του έδωσε ο φίλος του;", ["Να βράζει το νερό", "Να αγοράσει φίλτρο", "Να αφήνει το νερό σε κανάτα στο ψυγείο για λίγες ώρες", "Να πίνει μόνο μεταλλικό νερό"], 2, "αν αφήσεις το νερό σε μια κανάτα στο ψυγείο για λίγες ώρες"),
 ],
 "gloss": {"εξάδες": "εξάδα — six-pack", "αποθήκη": "αποθήκη — storeroom", "ανακύκλωση": "ανακύκλωση — recycling", "πόσιμο": "πόσιμος — drinkable", "χλωρίου": "χλώριο — chlorine", "κανάτα": "κανάτα — jug", "παγούρι": "παγούρι — water bottle, flask", "εξοικονομώ": "εξοικονομώ — to save"}
})
ITEMS.append({
 "id": "l98-c1-goiteia-ereipion", "title": "Γιατί μας γοητεύουν τα ερείπια;", "title_en": "Why are we fascinated by ruins?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη για την ιστορία της αισθητικής σε ένα πολιτιστικό κέντρο.",
 "script": [
  L("Ομιλητής", "m", "Ένας αρχαίος ναός χωρίς στέγη, ένα μεσαιωνικό κάστρο μισογκρεμισμένο, ένα εγκαταλειμμένο εργοστάσιο με σπασμένα τζάμια: γιατί αυτές οι εικόνες μάς συγκινούν περισσότερο από τα ίδια κτίρια στην ακμή τους; Η γοητεία των ερειπίων δεν είναι καινούργια. Ήδη τον δέκατο όγδοο αιώνα, Ευρωπαίοι ζωγράφοι και ποιητές είχαν αναγάγει τα ερείπια σε αυτοτελές θέμα, και ορισμένοι γαιοκτήμονες έχτιζαν μάλιστα τεχνητά ερείπια στους κήπους τους.", "An ancient temple without a roof, a half-ruined medieval castle, an abandoned factory with broken windows: why do these images move us more than the same buildings in their prime? The fascination with ruins isn't new. Already in the eighteenth century, European painters and poets had raised ruins into a subject in their own right, and some landowners even built artificial ruins in their gardens."),
  L("Ομιλητής", "m", "Μια πρώτη εξήγηση είναι ότι το ερείπιο κάνει ορατό τον χρόνο. Ένα ολόκληρο κτίριο ανήκει στο παρόν· ένα ερείπιο είναι ταυτόχρονα παρόν και παρελθόν, και μας θυμίζει, με τρόπο σχεδόν σωματικό, ότι τίποτα ανθρώπινο δεν είναι μόνιμο. Υπάρχει, θα λέγαμε, μια μελαγχολική ηδονή στη σκέψη ότι και ο δικός μας πολιτισμός κάποτε θα γίνει θέαμα για άλλους.", "A first explanation is that ruins make time visible. A whole building belongs to the present; a ruin is at once present and past, and reminds us, in an almost physical way, that nothing human is permanent. There is, we might say, a melancholy pleasure in the thought that our own civilisation will one day become a spectacle for others."),
  L("Ομιλητής", "m", "Μια δεύτερη εξήγηση έχει να κάνει με τη φαντασία. Το ερείπιο είναι ημιτελές· μας καλεί να συμπληρώσουμε νοερά ό,τι λείπει. Γι' αυτό και οι πλήρεις ανακατασκευές αρχαίων μνημείων προκαλούν συχνά απογοήτευση: όσο πιστές κι αν είναι, μας στερούν τον ρόλο του συνδημιουργού. Δεν είναι τυχαίο ότι η σύγχρονη επιστήμη της αναστήλωσης προτιμά, κατά κανόνα, τις ελάχιστες και αναστρέψιμες επεμβάσεις.", "A second explanation has to do with imagination. A ruin is unfinished; it invites us to fill in mentally whatever is missing. That's also why complete reconstructions of ancient monuments often cause disappointment: however faithful they are, they deprive us of the role of co-creator. It's no coincidence that the modern science of restoration generally prefers minimal and reversible interventions."),
  L("Ομιλητής", "m", "Θα ήθελα, ωστόσο, να κλείσω με μια επιφύλαξη. Η αισθητική των ερειπίων μπορεί να γίνει και επικίνδυνη, όταν ωραιοποιεί την καταστροφή. Τα ερείπια μιας πόλης που βομβαρδίστηκε χθες δεν είναι «γραφικά»· είναι τραύμα. Η γοητεία που ασκεί ένα ερείπιο προϋποθέτει, ίσως, μια απόσταση, χρονική και συναισθηματική, που δεν έχουμε δικαίωμα να επιβάλλουμε σε όσους ζουν ακόμα ανάμεσα στα συντρίμμια.", "I'd like, however, to end with a reservation. The aesthetics of ruins can also become dangerous when it beautifies destruction. The ruins of a city bombed yesterday are not 'picturesque'; they are trauma. The fascination a ruin exerts perhaps presupposes a distance, in time and in feeling, which we have no right to impose on those who still live among the rubble."),
 ],
 "questions": [
  Q("Τι έκαναν ορισμένοι γαιοκτήμονες τον δέκατο όγδοο αιώνα;", ["Κατέστρεφαν παλιά κτίρια", "Έχτιζαν τεχνητά ερείπια στους κήπους τους", "Αγόραζαν αρχαία αγάλματα", "Χρηματοδοτούσαν ανασκαφές"], 1, "ορισμένοι γαιοκτήμονες έχτιζαν μάλιστα τεχνητά ερείπια στους κήπους τους"),
  Q("Ποια είναι η πρώτη εξήγηση που δίνει ο ομιλητής;", ["Ότι τα ερείπια είναι φθηνότερα στη συντήρηση", "Ότι το ερείπιο κάνει ορατό τον χρόνο", "Ότι τα ερείπια είναι πιο φωτογενή", "Ότι προσελκύουν τουρίστες"], 1, "το ερείπιο κάνει ορατό τον χρόνο"),
  Q("Γιατί οι πλήρεις ανακατασκευές προκαλούν συχνά απογοήτευση;", ["Γιατί δεν είναι πιστές", "Γιατί κοστίζουν πολύ", "Γιατί μας στερούν τον ρόλο του συνδημιουργού", "Γιατί χρησιμοποιούν σύγχρονα υλικά"], 2, "μας στερούν τον ρόλο του συνδημιουργού"),
  Q("Ποια επιφύλαξη διατυπώνει στο τέλος;", ["Ότι η αισθητική των ερειπίων μπορεί να ωραιοποιήσει την καταστροφή", "Ότι τα ερείπια πρέπει να ανακατασκευάζονται πάντα", "Ότι οι τουρίστες καταστρέφουν τα ερείπια", "Ότι τα σύγχρονα ερείπια δεν έχουν αξία"], 0, "όταν ωραιοποιεί την καταστροφή"),
 ],
 "gloss": {"ερείπια": "ερείπιο — ruin", "μισογκρεμισμένο": "μισογκρεμισμένος — half-ruined", "εγκαταλειμμένο": "εγκαταλειμμένος — abandoned", "ακμή": "ακμή — prime, peak", "αναγάγει": "ανάγω σε — to raise into", "αυτοτελές": "αυτοτελής — self-contained, in its own right", "γαιοκτήμονες": "γαιοκτήμονας — landowner", "μελαγχολική": "μελαγχολικός — melancholy", "ηδονή": "ηδονή — pleasure", "ημιτελές": "ημιτελής — unfinished", "νοερά": "νοερά — mentally, in the mind", "συνδημιουργού": "συνδημιουργός — co-creator", "αναστήλωσης": "αναστήλωση — restoration (of monuments)", "αναστρέψιμες": "αναστρέψιμος — reversible", "ωραιοποιεί": "ωραιοποιώ — to beautify, prettify", "συντρίμμια": "συντρίμμια — rubble, debris"}
})
ITEMS.append({
 "id": "l98-c1-dialeimma-apo-ti-douleia", "title": "Ένα χρόνο άδεια χωρίς αποδοχές", "title_en": "A year of unpaid leave", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την εργασία, μια δημοσιογράφος συζητά με έναν μηχανικό που πήρε έναν χρόνο άδεια από τη δουλειά του.",
 "script": [
  L("Δημοσιογράφος", "f", "Πριν από δύο χρόνια, στα σαράντα σας, αποφασίσατε να πάρετε έναν χρόνο άδεια χωρίς αποδοχές. Τι σας οδήγησε σε αυτή την απόφαση;", "Two years ago, at forty, you decided to take a year of unpaid leave. What led you to that decision?"),
  L("Μηχανικός", "m", "Δεν ήταν, όπως ίσως φαντάζεστε, μια κρίση επαγγελματικής εξουθένωσης, αν και δεν απείχα πολύ. Ήταν περισσότερο μια αίσθηση ότι η ζωή μου είχε μπει σε αυτόματο πιλότο. Ήξερα με ακρίβεια τι θα έκανα κάθε μέρα για τα επόμενα είκοσι πέντε χρόνια, και αυτό, αντί να με καθησυχάζει, με τρόμαζε.", "It wasn't, as you might imagine, a burnout crisis, though I wasn't far from it. It was more a feeling that my life had gone onto autopilot. I knew exactly what I would do every day for the next twenty-five years, and that, instead of reassuring me, frightened me."),
  L("Δημοσιογράφος", "f", "Πώς αντιμετώπισε ο εργοδότης σας το αίτημά σας;", "How did your employer react to your request?"),
  L("Μηχανικός", "m", "Με μεγαλύτερη κατανόηση από ό,τι περίμενα. Είχα προετοιμάσει ένα σχέδιο για το πώς θα μοιράζονταν οι αρμοδιότητές μου και είχα εκπαιδεύσει έναν νεότερο συνάδελφο. Νομίζω ότι αυτό έκανε τη διαφορά: δεν πήγα να ζητήσω μια χάρη, αλλά να προτείνω μια λύση. Φυσικά, είχα και αποταμιεύσεις για να ζήσω εκείνο τον χρόνο, κάτι που, το αναγνωρίζω, είναι προνόμιο που δεν έχουν όλοι.", "With more understanding than I expected. I had prepared a plan for how my responsibilities would be shared out and had trained a younger colleague. I think that made the difference: I didn't go to ask for a favour but to propose a solution. Of course, I also had savings to live on that year, which, I acknowledge, is a privilege not everyone has."),
  L("Δημοσιογράφος", "f", "Και τι κρατήσατε από εκείνη τη χρονιά;", "And what did you take away from that year?"),
  L("Μηχανικός", "m", "Τους πρώτους δύο μήνες ένιωθα ενοχές, σαν να έκανα κοπάνα από το σχολείο. Μετά έμαθα να ξεκουράζομαι χωρίς να το δικαιολογώ. Έμαθα ξυλουργική, περπάτησα ένα μεγάλο μέρος του Ευρωπαϊκού Μονοπατιού Ε4 στην Κρήτη, πέρασα χρόνο με τον πατέρα μου, που αρρώστησε εκείνη τη χρονιά. Όταν γύρισα στη δουλειά, η δουλειά ήταν η ίδια, εγώ όμως όχι. Σήμερα δουλεύω τέσσερις μέρες την εβδομάδα, με αντίστοιχα μειωμένο μισθό, και δεν το μετάνιωσα ούτε μία μέρα.", "For the first two months I felt guilty, as if I was skipping school. Then I learned to rest without justifying it. I learned carpentry, walked a large part of the European E4 path in Crete, spent time with my father, who fell ill that year. When I went back to work, the job was the same, but I wasn't. Today I work four days a week, with a correspondingly reduced salary, and I haven't regretted it for a single day."),
 ],
 "questions": [
  Q("Τι τον οδήγησε στην απόφαση να πάρει άδεια;", ["Μια σοβαρή επαγγελματική εξουθένωση", "Η αίσθηση ότι η ζωή του είχε μπει σε αυτόματο πιλότο", "Μια πρόταση για καινούργια δουλειά", "Η αρρώστια του πατέρα του"], 1, "μια αίσθηση ότι η ζωή μου είχε μπει σε αυτόματο πιλότο"),
  Q("Τι πιστεύει ότι έκανε τη διαφορά στη συζήτηση με τον εργοδότη;", ["Ότι απείλησε να παραιτηθεί", "Ότι ζήτησε μια χάρη", "Ότι πρότεινε μια λύση, με σχέδιο και εκπαιδευμένο αντικαταστάτη", "Ότι δέχτηκε μικρότερο μισθό"], 2, "δεν πήγα να ζητήσω μια χάρη, αλλά να προτείνω μια λύση"),
  Q("Τι αναγνωρίζει ως προνόμιο;", ["Ότι είχε αποταμιεύσεις για να ζήσει εκείνο τον χρόνο", "Ότι μιλάει ξένες γλώσσες", "Ότι ζει στην Κρήτη", "Ότι η εταιρεία του είναι μεγάλη"], 0, "είχα και αποταμιεύσεις για να ζήσω εκείνο τον χρόνο"),
  Q("Πώς δουλεύει σήμερα;", ["Από το σπίτι", "Τέσσερις μέρες την εβδομάδα, με μειωμένο μισθό", "Ως ξυλουργός", "Σε άλλη εταιρεία"], 1, "Σήμερα δουλεύω τέσσερις μέρες την εβδομάδα"),
 ],
 "gloss": {"άδεια χωρίς αποδοχές": "άδεια χωρίς αποδοχές — unpaid leave", "εξουθένωσης": "εξουθένωση — exhaustion (επαγγελματική εξουθένωση: burnout)", "απείχα": "απέχω — to be far from", "καθησυχάζει": "καθησυχάζω — to reassure", "εργοδότης": "εργοδότης — employer", "αρμοδιότητές": "αρμοδιότητα — responsibility, remit", "αποταμιεύσεις": "αποταμίευση — savings", "προνόμιο": "προνόμιο — privilege", "ενοχές": "ενοχή — guilt", "κοπάνα": "κάνω κοπάνα — to skip school, play truant", "ξυλουργική": "ξυλουργική — carpentry", "μετάνιωσα": "μετανιώνω — to regret"}
})

rnd = random.Random(98)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-98.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
