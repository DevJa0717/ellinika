# Source for library/listening/listening-215.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l215.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l215-news-revma-apo-steria", "title": "Τα κρουαζιερόπλοια θα σβήνουν τις μηχανές τους στο λιμάνι", "title_en": "Cruise ships to switch off their engines in port", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο ραδιόφωνο για ένα έργο σε ένα μεγάλο λιμάνι.",
 "script": [
  L("Εκφωνήτρια", "f", "Ξεκίνησαν οι εργασίες για την ηλεκτροδότηση των κρουαζιερόπλοιων από την ξηρά στο λιμάνι της πόλης. Μέχρι σήμερα, τα πλοία κρατούν τις μηχανές τους αναμμένες όσο είναι δεμένα, για να έχουν ρεύμα για τον κλιματισμό, τις κουζίνες και τα φώτα. Αυτό σημαίνει καυσαέριο και θόρυβο για τις γειτονιές γύρω από το λιμάνι, ακόμα και όταν τα πλοία δεν κινούνται.", "Work has begun on supplying cruise ships with electricity from the shore in the city's port. Until now, ships have kept their engines running while moored, to have power for air conditioning, kitchens and lights. That means exhaust fumes and noise for the neighbourhoods around the port, even when the ships aren't moving."),
  L("Εκφωνήτρια", "f", "Με το νέο σύστημα, τα πλοία θα συνδέονται με ειδικά καλώδια στο δίκτυο ρεύματος και θα σβήνουν τις μηχανές τους. Η πρώτη φάση αφορά τρεις θέσεις πρόσδεσης και αναμένεται να ολοκληρωθεί σε δύο χρόνια. Μια ευρωπαϊκή οδηγία προβλέπει ότι από το 2030 τα μεγάλα κρουαζιερόπλοια θα πρέπει να χρησιμοποιούν ρεύμα από την ξηρά στα μεγάλα λιμάνια της Ευρώπης.", "With the new system, ships will connect to the power grid with special cables and switch off their engines. The first phase covers three berths and is expected to be completed in two years. A European directive provides that from 2030 large cruise ships will have to use shore power in Europe's major ports."),
  L("Εκφωνήτρια", "f", "Οι κάτοικοι των γύρω περιοχών χαιρετίζουν το έργο, αλλά επισημαίνουν ότι πρέπει να καλυφθούν και τα επιβατηγά πλοία της ακτοπλοΐας, που πιάνουν λιμάνι πολύ πιο συχνά. Η διοίκηση του λιμανιού απαντά ότι αυτό θα εξεταστεί στη δεύτερη φάση.", "Residents of the surrounding areas welcome the project, but point out that the coastal passenger ferries, which call at the port much more often, must also be covered. The port authority replies that this will be examined in the second phase."),
 ],
 "questions": [
  Q("Γιατί τα πλοία κρατούν μέχρι σήμερα τις μηχανές τους αναμμένες στο λιμάνι;", ["Για να φύγουν πιο γρήγορα", "Για να έχουν ρεύμα για κλιματισμό, κουζίνες και φώτα", "Επειδή το απαιτεί ο νόμος", "Για να ζεσταίνεται το νερό της πισίνας"], 1, "για να έχουν ρεύμα για τον κλιματισμό, τις κουζίνες και τα φώτα"),
  Q("Τι θα γίνεται με το νέο σύστημα;", ["Τα πλοία θα δένουν πιο μακριά από την πόλη", "Τα πλοία θα συνδέονται στο δίκτυο ρεύματος και θα σβήνουν τις μηχανές", "Τα πλοία θα έχουν ηλιακά πάνελ", "Τα πλοία θα μένουν λιγότερες ώρες"], 1, "θα συνδέονται με ειδικά καλώδια στο δίκτυο ρεύματος και θα σβήνουν τις μηχανές τους"),
  Q("Τι αφορά η πρώτη φάση;", ["Όλο το λιμάνι", "Μόνο τα πλοία της ακτοπλοΐας", "Τρεις θέσεις πρόσδεσης", "Τα φορτηγά πλοία"], 2, "Η πρώτη φάση αφορά τρεις θέσεις πρόσδεσης"),
  Q("Τι ζητούν οι κάτοικοι;", ["Να σταματήσουν οι κρουαζιέρες", "Να καλυφθούν και τα επιβατηγά πλοία της ακτοπλοΐας", "Να γίνει πάρκο στο λιμάνι", "Να μειωθούν τα εισιτήρια"], 1, "πρέπει να καλυφθούν και τα επιβατηγά πλοία της ακτοπλοΐας"),
 ],
 "gloss": {"ηλεκτροδότηση": "ηλεκτροδότηση — supply of electricity", "κρουαζιερόπλοιων": "κρουαζιερόπλοιο — cruise ship", "δεμένα": "δεμένος — moored, tied up", "καυσαέριο": "καυσαέριο — exhaust fumes", "πρόσδεσης": "θέση πρόσδεσης — berth", "οδηγία": "οδηγία — (EU) directive; instruction", "χαιρετίζουν": "χαιρετίζω — to welcome, hail", "ακτοπλοΐας": "ακτοπλοΐα — coastal shipping"},
})
ITEMS.append({
 "id": "l215-dia-genealogiko-dentro", "title": "Το γενεαλογικό δέντρο της οικογένειας", "title_en": "Drawing up the family tree", "type": "dialogue", "level": "B2",
 "context_el": "Δύο ξαδέρφια φτιάχνουν μαζί το γενεαλογικό δέντρο της οικογένειάς τους και συζητούν τι έχουν βρει.",
 "script": [
  L("Νίκος", "m", "Λοιπόν, βρήκα στο κουτί της γιαγιάς το πιστοποιητικό γάμου του προπάππου. Γράφει ότι γεννήθηκε το 1898 στα Βουρλά, κοντά στη Σμύρνη. Εμείς πιστεύαμε πάντα ότι ήταν από τη Μυτιλήνη!", "So, I found great-grandad's marriage certificate in grandma's box. It says he was born in 1898 in Vourla, near Smyrna. We always thought he was from Mytilene!"),
  L("Ελένη", "f", "Ίσως πέρασε στη Μυτιλήνη ως πρόσφυγας το 1922 και έμεινε εκεί. Γι' αυτό η γιαγιά έλεγε ότι ο πατέρας της «ήρθε από απέναντι». Νόμιζα ότι εννοούσε απλώς από άλλο χωριό.", "Maybe he crossed to Mytilene as a refugee in 1922 and stayed there. That's why grandma said her father 'came from across the water'. I thought she just meant from another village."),
  L("Νίκος", "m", "Σκέφτομαι να κάνουμε κι ένα τεστ DNA, από αυτά που στέλνεις με το ταχυδρομείο. Μπορεί να βρούμε και μακρινούς συγγενείς.", "I'm thinking we should also do a DNA test, one of those you send off by post. We might even find distant relatives."),
  L("Ελένη", "f", "Δεν είμαι σίγουρη. Δεν ξέρω πού καταλήγουν αυτά τα δεδομένα και ποιος θα τα χρησιμοποιήσει. Προτιμώ να ψάξουμε πρώτα στα δημοτολόγια και στα αρχεία της εκκλησίας. Και να ρωτήσουμε τη θεία Σοφία, που θυμάται τα πάντα.", "I'm not sure. I don't know where that data ends up or who will use it. I'd rather we search the municipal registers and the church records first. And ask Aunt Sofia, who remembers everything."),
  L("Νίκος", "m", "Δίκιο έχεις, η θεία Σοφία είναι καλύτερη από κάθε βάση δεδομένων. Πάμε την Κυριακή; Θα πάρω και το κασετοφωνάκι του παππού να την ηχογραφήσουμε.", "You're right, Aunt Sofia is better than any database. Shall we go on Sunday? I'll bring grandad's little tape recorder too so we can record her."),
  L("Ελένη", "f", "Καλύτερα το κινητό, Νίκο. Το κασετόφωνο να το κρατήσουμε για το μουσείο της οικογένειας!", "Better the phone, Nikos. Let's keep the tape recorder for the family museum!"),
 ],
 "questions": [
  Q("Τι βρήκε ο Νίκος στο κουτί της γιαγιάς;", ["Ένα ημερολόγιο", "Το πιστοποιητικό γάμου του προπάππου", "Παλιές φωτογραφίες", "Ένα διαβατήριο"], 1, "βρήκα στο κουτί της γιαγιάς το πιστοποιητικό γάμου του προπάππου"),
  Q("Πώς εξηγεί η Ελένη ότι ο προπάππους θεωρούνταν από τη Μυτιλήνη;", ["Είχε γεννηθεί εκεί", "Ίσως πέρασε εκεί ως πρόσφυγας το 1922 και έμεινε", "Παντρεύτηκε μια γυναίκα από τη Μυτιλήνη", "Δούλευε εκεί ως ψαράς"], 1, "Ίσως πέρασε στη Μυτιλήνη ως πρόσφυγας το 1922 και έμεινε εκεί"),
  Q("Γιατί η Ελένη διστάζει να κάνουν τεστ DNA;", ["Είναι πολύ ακριβό", "Δεν ξέρει πού καταλήγουν τα δεδομένα", "Φοβάται τις βελόνες", "Αργεί πολύ να βγει το αποτέλεσμα"], 1, "Δεν ξέρω πού καταλήγουν αυτά τα δεδομένα"),
  Q("Τι θα κάνουν την Κυριακή;", ["Θα πάνε στη Σμύρνη", "Θα επισκεφτούν τη θεία Σοφία και θα την ηχογραφήσουν", "Θα πάνε στο μουσείο", "Θα στείλουν το τεστ"], 1, "Πάμε την Κυριακή; ... να την ηχογραφήσουμε"),
 ],
 "gloss": {"πιστοποιητικό": "πιστοποιητικό — certificate", "προπάππου": "προπάππους — great-grandfather", "πρόσφυγας": "πρόσφυγας — refugee", "δεδομένα": "δεδομένα — data", "δημοτολόγια": "δημοτολόγιο — municipal register", "βάση δεδομένων": "βάση δεδομένων — database", "κασετοφωνάκι": "κασετόφωνο — cassette recorder"},
})
ITEMS.append({
 "id": "l215-c1-mono-grammotos-kodikas", "title": "Από τις γραμμές στην άμμο στο ταμείο του σούπερ μάρκετ", "title_en": "From lines in the sand to the supermarket till: the barcode", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε ένα απόσπασμα από ραδιοφωνική εκπομπή για την ιστορία των καθημερινών εφευρέσεων.",
 "script": [
  L("Παρουσιαστής", "m", "Τον βλέπουμε σε κάθε συσκευασία και δεν του δίνουμε καμία σημασία: τον γραμμωτό κώδικα. Η ιστορία του ξεκινά στα τέλη της δεκαετίας του 1940, όταν ένας διευθυντής σούπερ μάρκετ στις Ηνωμένες Πολιτείες ζήτησε από ένα πανεπιστήμιο έναν τρόπο να καταγράφονται αυτόματα τα προϊόντα στο ταμείο. Δύο νέοι μηχανικοί, ο Νόρμαν Γούντλαντ και ο Μπέρναρντ Σίλβερ, πήραν την πρόκληση στα σοβαρά.", "We see it on every package and pay it no attention: the barcode. Its story begins in the late 1940s, when a supermarket manager in the United States asked a university for a way to record products automatically at the till. Two young engineers, Norman Woodland and Bernard Silver, took the challenge seriously."),
  L("Παρουσιαστής", "m", "Ο Γούντλαντ αφηγήθηκε αργότερα ότι η ιδέα τού ήρθε σε μια παραλία. Γνώριζε τον κώδικα Μορς από τους προσκόπους και, καθισμένος στην άμμο, τράβηξε με τα δάχτυλά του τελείες και παύλες. Όταν τις επέκτεινε προς τα κάτω, έγιναν λεπτές και χοντρές γραμμές. Το πρώτο τους σχέδιο ήταν κυκλικό, σαν στόχος, ώστε να διαβάζεται από οποιαδήποτε κατεύθυνση, και πήρε δίπλωμα ευρεσιτεχνίας το 1952.", "Woodland later recounted that the idea came to him on a beach. He knew Morse code from the Scouts and, sitting in the sand, drew dots and dashes with his fingers. When he extended them downwards, they became thin and thick lines. Their first design was circular, like a target, so it could be read from any direction, and it was patented in 1952."),
  L("Παρουσιαστής", "m", "Η εφεύρεση όμως ήταν πολύ μπροστά από την εποχή της. Δεν υπήρχαν ακόμα φθηνά λέιζερ ούτε υπολογιστές για να διαβάζουν τους κώδικες. Χρειάστηκαν άλλα είκοσι και πλέον χρόνια, μέχρι να συμφωνήσουν οι αμερικανικές αλυσίδες σε ένα κοινό ορθογώνιο πρότυπο. Το πρώτο προϊόν που σαρώθηκε σε ταμείο, τον Ιούνιο του 1974 στο Οχάιο, ήταν ένα πακέτο τσίχλες.", "But the invention was far ahead of its time. There were not yet cheap lasers nor computers to read the codes. It took another twenty-odd years for the American chains to agree on a common rectangular standard. The first product scanned at a checkout, in June 1974 in Ohio, was a packet of chewing gum."),
  L("Παρουσιαστής", "m", "Λίγα χρόνια αργότερα η Ευρώπη υιοθέτησε μια παραλλαγή με δεκατρία ψηφία. Τα πρώτα ψηφία δείχνουν τον οργανισμό στον οποίο έχει καταχωριστεί ο κωδικός, όχι απαραίτητα τη χώρα όπου φτιάχτηκε το προϊόν· έτσι, ένας κωδικός που αρχίζει από 520 δεν εγγυάται ότι κάτι παράχθηκε στην Ελλάδα. Και κάτι τελευταίο: ο Σίλβερ πέθανε νέος, το 1963, και δεν πρόλαβε να δει την εφεύρεσή του να αλλάζει το εμπόριο σε όλο τον κόσμο.", "A few years later Europe adopted a version with thirteen digits. The first digits show the organisation with which the code was registered, not necessarily the country where the product was made; so a code beginning with 520 doesn't guarantee that something was produced in Greece. And one last thing: Silver died young, in 1963, and didn't live to see his invention change trade around the world."),
 ],
 "questions": [
  Q("Ποιος έθεσε αρχικά το πρόβλημα που οδήγησε στον γραμμωτό κώδικα;", ["Ένας καθηγητής φυσικής", "Ένας διευθυντής σούπερ μάρκετ", "Ο στρατός", "Μια εταιρεία τσίχλας"], 1, "ένας διευθυντής σούπερ μάρκετ ... ζήτησε από ένα πανεπιστήμιο έναν τρόπο"),
  Q("Από πού εμπνεύστηκε ο Γούντλαντ;", ["Από τις νότες της μουσικής", "Από τον κώδικα Μορς, που σχεδίασε στην άμμο", "Από τα δακτυλικά αποτυπώματα", "Από τις ρίγες της ζέβρας"], 1, "Γνώριζε τον κώδικα Μορς ... τράβηξε με τα δάχτυλά του τελείες και παύλες"),
  Q("Γιατί άργησε τόσο να χρησιμοποιηθεί η εφεύρεση;", ["Γιατί το δίπλωμα ευρεσιτεχνίας απορρίφθηκε", "Γιατί δεν υπήρχαν ακόμα φθηνά λέιζερ και υπολογιστές", "Γιατί οι καταναλωτές τη φοβούνταν", "Γιατί οι εφευρέτες δεν ήθελαν να την πουλήσουν"], 1, "Δεν υπήρχαν ακόμα φθηνά λέιζερ ούτε υπολογιστές"),
  Q("Τι δείχνουν τα πρώτα ψηφία ενός ευρωπαϊκού κωδικού;", ["Τη χώρα όπου φτιάχτηκε σίγουρα το προϊόν", "Την τιμή", "Τον οργανισμό στον οποίο έχει καταχωριστεί ο κωδικός", "Την ημερομηνία λήξης"], 2, "δείχνουν τον οργανισμό στον οποίο έχει καταχωριστεί ο κωδικός, όχι απαραίτητα τη χώρα"),
 ],
 "gloss": {"γραμμωτό κώδικα": "γραμμωτός κώδικας — barcode", "συσκευασία": "συσκευασία — packaging, package", "προσκόπους": "πρόσκοπος — scout", "τελείες": "τελεία — dot, full stop", "παύλες": "παύλα — dash", "δίπλωμα ευρεσιτεχνίας": "δίπλωμα ευρεσιτεχνίας — patent", "πρότυπο": "πρότυπο — standard", "σαρώθηκε": "σαρώνω — to scan; sweep", "καταχωριστεί": "καταχωρίζω — to register, enter"},
})
ITEMS.append({
 "id": "l215-c1-int-palies-diafimiseis", "title": "Τι μας λένε οι παλιές διαφημίσεις", "title_en": "What old advertisements tell us: a historian of advertising", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε ραδιοφωνική εκπομπή με έναν ιστορικό που μελετά τις παλιές ελληνικές διαφημίσεις.",
 "script": [
  L("Δημοσιογράφος", "f", "Οι περισσότεροι από εμάς αλλάζουμε κανάλι όταν αρχίζουν οι διαφημίσεις. Εσείς τις μελετάτε ως ιστορικές πηγές. Γιατί;", "Most of us change the channel when the adverts start. You study them as historical sources. Why?"),
  L("Ιστορικός", "m", "Γιατί η διαφήμιση δεν δείχνει πώς ζούσαν οι άνθρωποι, αλλά πώς ονειρεύονταν ότι θα ζήσουν. Αυτό είναι πολύτιμο. Μια αφίσα για ψυγείο της δεκαετίας του 1960 σού δείχνει τι σήμαινε τότε «σύγχρονο σπίτι», ποιος υποτίθεται ότι στεκόταν στην κουζίνα και ποιος γύριζε από τη δουλειά.", "Because advertising doesn't show how people lived, but how they dreamed they would live. That's valuable. A poster for a refrigerator from the 1960s shows you what a 'modern home' meant then, who was supposed to stand in the kitchen and who came home from work."),
  L("Δημοσιογράφος", "f", "Από πότε μπορούμε να μιλάμε για διαφήμιση στην Ελλάδα;", "Since when can we speak of advertising in Greece?"),
  L("Ιστορικός", "m", "Στις εφημερίδες του 19ου αιώνα βρίσκουμε ήδη μικρές αγγελίες: φαρμακεία, τονωτικά «για κάθε ασθένεια», ράφτες, ατμόπλοια. Η γλώσσα είναι συχνά μια βαριά καθαρεύουσα, με υποσχέσεις που σήμερα θα ήταν παράνομες. Στον Μεσοπόλεμο έρχονται οι μεγάλες λιθογραφικές αφίσες, που κάποιες φορές τις σχεδίαζαν γνωστοί ζωγράφοι. Και αργότερα το ραδιόφωνο φέρνει τα πρώτα τραγουδάκια, τα τζινγκλ, που κάποιοι ηλικιωμένοι θυμούνται ακόμα απέξω.", "In 19th-century newspapers we already find small notices: pharmacies, tonics 'for every illness', tailors, steamships. The language is often a heavy katharevousa, with promises that would be illegal today. Between the wars come the big lithographic posters, sometimes designed by well-known painters. And later radio brings the first little songs, the jingles, which some elderly people still remember by heart."),
  L("Δημοσιογράφος", "f", "Υπάρχει κάτι που σας έχει εκπλήξει ιδιαίτερα;", "Is there something that has particularly surprised you?"),
  L("Ιστορικός", "m", "Το πόσο γρήγορα αλλάζουν οι αξίες. Σε διαφημίσεις της δεκαετίας του 1950 το τσιγάρο παρουσιάζεται σχεδόν ως προϊόν υγείας, που «χαλαρώνει τα νεύρα». Λίγες δεκαετίες αργότερα, η διαφήμιση του καπνού απαγορεύεται. Γι' αυτό λέω στους φοιτητές μου να κοιτάζουν και τις σημερινές διαφημίσεις με το ίδιο μάτι: σε πενήντα χρόνια κάποιος θα τις μελετά και θα αναρωτιέται τι πιστεύαμε εμείς.", "How quickly values change. In 1950s adverts cigarettes are presented almost as a health product that 'calms the nerves'. A few decades later, tobacco advertising is banned. That's why I tell my students to look at today's adverts with the same eye: in fifty years someone will study them and wonder what we believed."),
 ],
 "questions": [
  Q("Γιατί θεωρεί ο ιστορικός τις διαφημίσεις πολύτιμες πηγές;", ["Γιατί δείχνουν ακριβώς πώς ζούσαν οι άνθρωποι", "Γιατί δείχνουν πώς ονειρεύονταν οι άνθρωποι ότι θα ζήσουν", "Γιατί είναι πάντα αληθινές", "Γιατί είναι φτηνές στην αγορά"], 1, "δεν δείχνει πώς ζούσαν οι άνθρωποι, αλλά πώς ονειρεύονταν ότι θα ζήσουν"),
  Q("Τι διαφήμιζαν οι μικρές αγγελίες του 19ου αιώνα, σύμφωνα με τον ιστορικό;", ["Αυτοκίνητα και ραδιόφωνα", "Φαρμακεία, τονωτικά, ράφτες και ατμόπλοια", "Μόνο βιβλία", "Κινηματογραφικές ταινίες"], 1, "φαρμακεία, τονωτικά «για κάθε ασθένεια», ράφτες, ατμόπλοια"),
  Q("Τι έφερε το ραδιόφωνο στη διαφήμιση;", ["Τις πρώτες έγχρωμες αφίσες", "Τα πρώτα τραγουδάκια, τα τζινγκλ", "Την απαγόρευση των διαφημίσεων", "Τις μικρές αγγελίες"], 1, "το ραδιόφωνο φέρνει τα πρώτα τραγουδάκια, τα τζινγκλ"),
  Q("Τι συμβουλεύει τους φοιτητές του;", ["Να μη βλέπουν διαφημίσεις", "Να κοιτάζουν και τις σημερινές διαφημίσεις με το ίδιο κριτικό μάτι", "Να συλλέγουν παλιές αφίσες", "Να δουλέψουν σε διαφημιστικές εταιρείες"], 1, "να κοιτάζουν και τις σημερινές διαφημίσεις με το ίδιο μάτι"),
 ],
 "gloss": {"πηγές": "πηγή — source; spring", "αγγελίες": "αγγελία — notice, small ad", "τονωτικά": "τονωτικό — tonic", "ατμόπλοια": "ατμόπλοιο — steamship", "καθαρεύουσα": "καθαρεύουσα — formal 'purified' Greek", "Μεσοπόλεμο": "Μεσοπόλεμος — the interwar period", "λιθογραφικές": "λιθογραφικός — lithographic", "απέξω": "απέξω — by heart; from outside", "αναρωτιέται": "αναρωτιέμαι — to wonder"},
})
rnd = random.Random(215)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-215.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
