# Source for library/listening/listening-261.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l261.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l261-news-anepafi-pliromi-leoforeia", "title": "Ανέπαφη πληρωμή μέσα στα αστικά λεωφορεία της Λάρισας", "title_en": "Contactless payment on board Larissa's city buses", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο πρωινό δελτίο ενός περιφερειακού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνήτρια", "f", "Από σήμερα οι επιβάτες των αστικών λεωφορείων της Λάρισας μπορούν να πληρώνουν το εισιτήριό τους με τραπεζική κάρτα ή με το κινητό τους, ακουμπώντας τα σε ένα μηχάνημα δίπλα στην πόρτα. Τα παλιά χάρτινα εισιτήρια θα ισχύουν ως το τέλος του χρόνου.", "From today passengers on Larissa's city buses can pay for their ticket with a bank card or their mobile phone, by touching it to a machine next to the door. The old paper tickets will remain valid until the end of the year."),
  L("Εκφωνήτρια", "f", "Το σύστημα έχει και ένα πλεονέκτημα που δεν φαίνεται με την πρώτη ματιά: υπολογίζει αυτόματα τη φθηνότερη χρέωση. Όποιος κάνει πάνω από τρεις διαδρομές την ίδια μέρα δεν θα πληρώσει περισσότερο από την τιμή του ημερήσιου εισιτηρίου.", "The system also has an advantage that is not obvious at first sight: it automatically calculates the cheapest fare. Anyone who makes more than three journeys on the same day will not pay more than the price of a day ticket."),
  L("Εκφωνήτρια", "f", "Οι φοιτητές, οι συνταξιούχοι και τα άτομα με αναπηρία, που δικαιούνται μειωμένο εισιτήριο, θα πρέπει προς το παρόν να συνεχίσουν να χρησιμοποιούν την προσωποποιημένη κάρτα τους. Η εταιρεία υπόσχεται ότι η εκπτωτική χρέωση θα ενσωματωθεί στο νέο σύστημα μέσα στους επόμενους μήνες.", "Students, pensioners and people with disabilities, who are entitled to a reduced fare, will for now have to keep using their personal card. The company promises that the discounted fare will be built into the new system within the coming months."),
  L("Εκφωνήτρια", "f", "Οι οδηγοί, πάντως, δεν θα πουλάνε πια εισιτήρια μέσα στο λεωφορείο. Σύλλογοι ηλικιωμένων εξέφρασαν την ανησυχία τους για όσους δεν έχουν τραπεζική κάρτα, και η εταιρεία απάντησε ότι τα περίπτερα και τα εκδοτήρια στις στάσεις θα συνεχίσουν να λειτουργούν κανονικά.", "Drivers, however, will no longer sell tickets on board. Pensioners' associations expressed concern about people who do not have a bank card, and the company replied that kiosks and ticket offices at the stops will continue to operate as normal."),
 ],
 "questions": [
  Q("Πώς μπορούν να πληρώνουν από σήμερα οι επιβάτες;", ["Μόνο με μετρητά στον οδηγό", "Με τραπεζική κάρτα ή με το κινητό", "Μόνο με μηνιαία κάρτα", "Με εισιτήριο από το διαδίκτυο"], 1, "μπορούν να πληρώνουν το εισιτήριό τους με τραπεζική κάρτα ή με το κινητό τους"),
  Q("Τι γίνεται με όποιον κάνει πάνω από τρεις διαδρομές την ίδια μέρα;", ["Πληρώνει πρόστιμο", "Δεν πληρώνει περισσότερο από ένα ημερήσιο εισιτήριο", "Ταξιδεύει δωρεάν την επόμενη μέρα", "Πρέπει να αγοράσει μηνιαία κάρτα"], 1, "δεν θα πληρώσει περισσότερο από την τιμή του ημερήσιου εισιτηρίου"),
  Q("Τι πρέπει να κάνουν προς το παρόν οι φοιτητές και οι συνταξιούχοι;", ["Να πληρώνουν κανονικό εισιτήριο", "Να συνεχίσουν να χρησιμοποιούν την προσωποποιημένη κάρτα τους", "Να ζητήσουν νέα κάρτα από την τράπεζα", "Να ταξιδεύουν μόνο τα πρωινά"], 1, "θα πρέπει προς το παρόν να συνεχίσουν να χρησιμοποιούν την προσωποποιημένη κάρτα τους"),
  Q("Τι απάντησε η εταιρεία στους συλλόγους ηλικιωμένων;", ["Ότι οι οδηγοί θα συνεχίσουν να πουλάνε εισιτήρια", "Ότι θα μοιράσει δωρεάν κάρτες", "Ότι τα περίπτερα και τα εκδοτήρια θα συνεχίσουν να λειτουργούν", "Ότι οι ηλικιωμένοι θα ταξιδεύουν δωρεάν"], 2, "τα περίπτερα και τα εκδοτήρια στις στάσεις θα συνεχίσουν να λειτουργούν κανονικά"),
 ],
 "gloss": {"ακουμπώντας": "ακουμπώ — to touch, rest against", "ισχύουν": "ισχύω — to be valid", "χρέωση": "χρέωση — charge, fare", "ημερήσιου": "ημερήσιος — daily, day (ticket)", "δικαιούνται": "δικαιούμαι — to be entitled to", "αναπηρία": "αναπηρία — disability", "προσωποποιημένη": "προσωποποιημένος — personalised", "εκπτωτική": "εκπτωτικός — discounted", "ενσωματωθεί": "ενσωματώνω — to incorporate, build in", "ανησυχία": "ανησυχία — concern", "εκδοτήρια": "εκδοτήριο — ticket office"}
})

ITEMS.append({
 "id": "l261-vm-ethelontes-festival", "title": "Μήνυμα από τη συντονίστρια των εθελοντών ενός μουσικού φεστιβάλ", "title_en": "A message from the volunteer coordinator of a music festival", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε δηλώσει ότι θα δουλέψετε ως εθελοντής σε ένα καλοκαιρινό μουσικό φεστιβάλ. Ακούτε ένα μήνυμα που σας άφησε η συντονίστρια των εθελοντών.",
 "script": [
  L("Ζωή", "f", "Γεια σου, η Ζωή είμαι, η συντονίστρια των εθελοντών του φεστιβάλ. Σε παίρνω για τη βάρδιά σου. Είχαμε πει ότι θα είσαι στην είσοδο την Παρασκευή το απόγευμα, αλλά μας λείπουν άτομα στο σημείο ανακύκλωσης το Σάββατο, από τις έξι ως τις δώδεκα το βράδυ.", "Hi, it's Zoi, the festival's volunteer coordinator. I'm calling about your shift. We'd said you'd be at the entrance on Friday afternoon, but we're short of people at the recycling point on Saturday, from six until midnight."),
  L("Ζωή", "f", "Ξέρω ότι το Σάββατο παίζει το συγκρότημα που ήθελες να δεις, γι’ αυτό σου προτείνω κάτι: αν κάνεις τη βάρδια του Σαββάτου, μπορείς να κάνεις διάλειμμα όσο κρατάει η συναυλία τους. Το σημείο ανακύκλωσης είναι ακριβώς δίπλα στη μεγάλη σκηνή, οπότε δεν θα χάσεις τίποτα.", "I know the band you wanted to see plays on Saturday, so I'm suggesting something: if you do the Saturday shift, you can take a break for as long as their concert lasts. The recycling point is right next to the main stage, so you won't miss a thing."),
  L("Ζωή", "f", "Για πρακτικά θέματα: φέρε κλειστά παπούτσια, γιατί θα πατάς σε χώμα, και ένα παγούρι. Μπλουζάκι, γάντια και κάρτα για δύο γεύματα θα πάρεις από τη σκηνή των εθελοντών, μισή ώρα πριν από την έναρξη της βάρδιας.", "On practical matters: bring closed shoes, because you'll be standing on earth, and a water bottle. You'll pick up a T-shirt, gloves and a card for two meals from the volunteers' tent, half an hour before your shift starts."),
  L("Ζωή", "f", "Αν δεν σε βολεύει η αλλαγή, κανένα πρόβλημα, μένεις στην είσοδο την Παρασκευή. Απλώς πες μου ως την Τετάρτη, για να κλείσω το πρόγραμμα. Ευχαριστώ πολύ!", "If the change doesn't suit you, no problem, you stay at the entrance on Friday. Just tell me by Wednesday, so I can finalise the schedule. Thanks a lot!"),
 ],
 "questions": [
  Q("Πού και πότε σας ζητά να δουλέψετε η Ζωή;", ["Στην είσοδο την Παρασκευή", "Στο σημείο ανακύκλωσης το Σάββατο βράδυ", "Στο μπαρ την Κυριακή", "Στη σκηνή των εθελοντών το Σάββατο πρωί"], 1, "μας λείπουν άτομα στο σημείο ανακύκλωσης το Σάββατο, από τις έξι ως τις δώδεκα"),
  Q("Τι σας προτείνει για τη συναυλία του συγκροτήματος;", ["Να την ακούσετε από το ραδιόφωνο", "Να κάνετε διάλειμμα όσο κρατάει", "Να έρθετε άλλη μέρα", "Να αλλάξετε βάρδια με έναν φίλο"], 1, "μπορείς να κάνεις διάλειμμα όσο κρατάει η συναυλία τους"),
  Q("Τι πρέπει να φέρετε μαζί σας;", ["Γάντια και μπλουζάκι", "Κλειστά παπούτσια και παγούρι", "Φακό και αδιάβροχο", "Κάρτα για γεύματα"], 1, "φέρε κλειστά παπούτσια … και ένα παγούρι"),
  Q("Ως πότε πρέπει να της απαντήσετε;", ["Ως την Τρίτη", "Ως την Τετάρτη", "Ως την Παρασκευή", "Ως το Σάββατο το πρωί"], 1, "πες μου ως την Τετάρτη"),
 ],
 "gloss": {"συντονίστρια": "συντονίστρια — coordinator", "εθελοντών": "εθελοντής — volunteer", "βάρδιά": "βάρδια — shift", "ανακύκλωσης": "ανακύκλωση — recycling", "συγκρότημα": "συγκρότημα — band", "σκηνή": "σκηνή — stage; tent", "παγούρι": "παγούρι — water bottle, flask", "έναρξη": "έναρξη — start", "βολεύει": "βολεύω — to suit"}
})

ITEMS.append({
 "id": "l261-c1-mono-tsichla", "title": "Από τη μαστίχα στο σούπερ μάρκετ: η ιστορία της τσίχλας", "title_en": "From mastic to the supermarket: the history of chewing gum", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε την αρχή μιας ομιλίας σε έναν κύκλο εκδηλώσεων για την ιστορία των καθημερινών αντικειμένων.",
 "script": [
  L("Ομιλητής", "m", "Οι άνθρωποι μασούν ρετσίνια δέντρων εδώ και χιλιάδες χρόνια. Στην αρχαία Ελλάδα μασούσαν τη μαστίχα, το ρετσίνι του σχίνου, για να καθαρίζουν τα δόντια και να δροσίζουν την αναπνοή τους· ο γιατρός Διοσκουρίδης την αναφέρει ήδη τον πρώτο αιώνα μ.Χ. Στην άλλη άκρη του κόσμου, οι Μάγια μασούσαν το τσικλ, τον γαλακτώδη χυμό ενός τροπικού δέντρου.", "People have chewed tree resins for thousands of years. In ancient Greece they chewed mastic, the resin of the mastic tree, to clean their teeth and freshen their breath; the physician Dioscorides already mentions it in the first century AD. At the other end of the world, the Maya chewed chicle, the milky sap of a tropical tree."),
  L("Ομιλητής", "m", "Η σύγχρονη τσίχλα γεννήθηκε από μια αποτυχία. Γύρω στο 1870, ένας Αμερικανός εφευρέτης, ο Τόμας Άνταμς, προσπάθησε να φτιάξει συνθετικό καουτσούκ από τσικλ, που του είχε φέρει ένας εξόριστος Μεξικανός στρατηγός. Το πείραμα απέτυχε. Ο Άνταμς όμως θυμήθηκε ότι οι Μεξικανοί το μασούσαν, έφτιαξε μικρά κομμάτια και τα πούλησε στα φαρμακεία. Η επιτυχία ήταν άμεση.", "Modern chewing gum was born of a failure. Around 1870 an American inventor, Thomas Adams, tried to make synthetic rubber from chicle, which an exiled Mexican general had brought him. The experiment failed. But Adams remembered that Mexicans chewed it, made small pieces and sold them to pharmacies. The success was immediate."),
  L("Ομιλητής", "m", "Λίγο αργότερα, ένας πωλητής σαπουνιού από το Σικάγο, ο Ουίλιαμ Ρίγκλεϊ, άρχισε να χαρίζει τσίχλες σε όσους αγόραζαν το προϊόν του. Σύντομα διαπίστωσε ότι οι πελάτες ενδιαφέρονταν περισσότερο για το δώρο παρά για το σαπούνι, και αφοσιώθηκε στις τσίχλες, επενδύοντας τεράστια ποσά στη διαφήμιση, κάτι πρωτοποριακό για την εποχή.", "A little later, a soap salesman from Chicago, William Wrigley, began giving away chewing gum to people who bought his product. He soon found that customers were more interested in the gift than in the soap, and devoted himself to gum, investing huge sums in advertising, something pioneering for the time."),
  L("Ομιλητής", "m", "Μετά τον Δεύτερο Παγκόσμιο Πόλεμο, το φυσικό τσικλ αντικαταστάθηκε σχεδόν παντού από συνθετικά πολυμερή, δηλαδή από πλαστικό. Γι’ αυτό η τσίχλα που πετάμε στο πεζοδρόμιο δεν διαλύεται και κοστίζει στους δήμους μια περιουσία για να καθαριστεί. Δεν είναι τυχαίο ότι η Σιγκαπούρη απαγόρευσε την πώλησή της ήδη από το 1992.", "After the Second World War natural chicle was replaced almost everywhere by synthetic polymers, that is, by plastic. That is why the gum we throw on the pavement does not dissolve and costs municipalities a fortune to clean. It is no coincidence that Singapore banned its sale as early as 1992."),
 ],
 "questions": [
  Q("Για ποιο λόγο μασούσαν μαστίχα οι αρχαίοι Έλληνες;", ["Για να μην πεινάνε", "Για να καθαρίζουν τα δόντια και να δροσίζουν την αναπνοή", "Ως φάρμακο για το στομάχι", "Σε θρησκευτικές τελετές"], 1, "για να καθαρίζουν τα δόντια και να δροσίζουν την αναπνοή τους"),
  Q("Τι προσπαθούσε αρχικά να φτιάξει ο Άνταμς;", ["Ένα φάρμακο για τον βήχα", "Συνθετικό καουτσούκ", "Μια νέα καραμέλα", "Ένα σαπούνι"], 1, "προσπάθησε να φτιάξει συνθετικό καουτσούκ από τσικλ"),
  Q("Τι διαπίστωσε ο Ρίγκλεϊ;", ["Ότι οι πελάτες προτιμούσαν το δώρο από το σαπούνι", "Ότι το σαπούνι πουλούσε περισσότερο", "Ότι η διαφήμιση δεν είχε αποτέλεσμα", "Ότι οι τσίχλες χαλούσαν γρήγορα"], 0, "οι πελάτες ενδιαφέρονταν περισσότερο για το δώρο παρά για το σαπούνι"),
  Q("Γιατί η σημερινή τσίχλα δεν διαλύεται στο πεζοδρόμιο;", ["Γιατί περιέχει ζάχαρη", "Γιατί φτιάχνεται από συνθετικά πολυμερή", "Γιατί είναι πολύ σκληρή", "Γιατί περιέχει μαστίχα"], 1, "το φυσικό τσικλ αντικαταστάθηκε … από συνθετικά πολυμερή"),
 ],
 "gloss": {"ρετσίνια": "ρετσίνι — resin", "σχίνου": "σχίνος — mastic tree, lentisk", "αναπνοή": "αναπνοή — breath", "γαλακτώδη": "γαλακτώδης — milky", "καουτσούκ": "καουτσούκ — rubber", "εξόριστος": "εξόριστος — exiled", "αφοσιώθηκε": "αφοσιώνομαι — to devote oneself", "επενδύοντας": "επενδύω — to invest", "πρωτοποριακό": "πρωτοποριακός — pioneering", "πολυμερή": "πολυμερές — polymer", "διαλύεται": "διαλύομαι — to dissolve", "περιουσία": "περιουσία — fortune"}
})

ITEMS.append({
 "id": "l261-c1-int-tselementes", "title": "Ο Τσελεμεντές και η ελληνική κουζίνα: μια ιστορικός της διατροφής", "title_en": "Tselementes and Greek cooking: a food historian", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε μια ραδιοφωνική εκπομπή για τη διατροφή και τον πολιτισμό.",
 "script": [
  L("Δημοσιογράφος", "m", "Στα ελληνικά λέμε «τσελεμεντές» για κάθε βιβλίο μαγειρικής. Ποιος ήταν ο άνθρωπος πίσω από τη λέξη;", "In Greek we say 'tselementes' for any cookbook. Who was the man behind the word?"),
  L("Ιστορικός", "f", "Ο Νικόλαος Τσελεμεντές γεννήθηκε το 1878 και καταγόταν από τη Σίφνο. Εκπαιδεύτηκε ως μάγειρας στη Βιέννη και στις αρχές του εικοστού αιώνα άρχισε να εκδίδει στην Αθήνα ένα περιοδικό μαγειρικής. Το μεγάλο του βιβλίο, ο «Οδηγός Μαγειρικής και Ζαχαροπλαστικής», κυκλοφόρησε στα μέσα της δεκαετίας του 1920 και ξανατυπώθηκε αμέτρητες φορές. Μπήκε σχεδόν σε κάθε ελληνικό σπίτι, γι’ αυτό το όνομά του έγινε κοινό ουσιαστικό.", "Nikolaos Tselementes was born in 1878 and came from Sifnos. He trained as a cook in Vienna and in the early twentieth century began publishing a cookery magazine in Athens. His great book, the 'Guide to Cookery and Pastry-making', came out in the mid-1920s and was reprinted countless times. It went into almost every Greek home, which is why his name became a common noun."),
  L("Δημοσιογράφος", "m", "Συχνά όμως ακούμε ότι «χάλασε» την ελληνική κουζίνα. Ισχύει;", "But we often hear that he 'ruined' Greek cooking. Is that true?"),
  L("Ιστορικός", "f", "Είναι μια κατηγορία που αξίζει να την εξετάσουμε με προσοχή. Είναι αλήθεια ότι ήθελε να «εξευγενίσει» την ελληνική μαγειρική με γαλλικές τεχνικές: λιγότερο λάδι, λιγότερα μπαχαρικά, περισσότερο βούτυρο. Του αποδίδεται συνήθως και η μπεσαμέλ πάνω στον μουσακά, που σήμερα τη θεωρούμε αυτονόητη. Ταυτόχρονα, όμως, κατέγραψε συστηματικά συνταγές που αλλιώς ίσως θα είχαν χαθεί, και έδωσε ακριβείς ποσότητες σε γενιές νοικοκυριών της πόλης.", "It's an accusation worth examining carefully. It is true that he wanted to 'refine' Greek cooking with French techniques: less oil, fewer spices, more butter. The béchamel on top of moussaka, which we now take for granted, is also usually attributed to him. At the same time, though, he systematically recorded recipes that might otherwise have been lost, and gave exact quantities to generations of urban households."),
  L("Δημοσιογράφος", "m", "Δηλαδή ο Τσελεμεντές δεν είναι ο κακός της ιστορίας;", "So Tselementes isn't the villain of the story?"),
  L("Ιστορικός", "f", "Θα έλεγα ότι είναι ο καθρέφτης μιας εποχής. Η αστική τάξη της Αθήνας ήθελε τότε να μοιάσει στην Ευρώπη, και εκείνος της έδωσε ακριβώς αυτό που ζητούσε. Η αγροτική κουζίνα, με τα χόρτα και τα όσπρια, δεν εξαφανίστηκε· απλώς δεν θεωρούνταν άξια για βιβλίο. Το ενδιαφέρον είναι ότι σήμερα κάνουμε το αντίστροφο: γράφουμε ολόκληρα βιβλία για τα χόρτα της γιαγιάς.", "I'd say he is the mirror of an era. The Athenian middle class wanted to resemble Europe at the time, and he gave it exactly what it was asking for. Peasant cooking, with wild greens and pulses, did not disappear; it simply wasn't considered worthy of a book. What's interesting is that today we do the opposite: we write whole books about grandma's greens."),
 ],
 "questions": [
  Q("Πού εκπαιδεύτηκε ως μάγειρας ο Τσελεμεντές;", ["Στο Παρίσι", "Στη Βιέννη", "Στη Σίφνο", "Στη Νέα Υόρκη"], 1, "Εκπαιδεύτηκε ως μάγειρας στη Βιέννη"),
  Q("Γιατί το όνομά του έγινε κοινό ουσιαστικό;", ["Γιατί άνοιξε πολλά εστιατόρια", "Γιατί το βιβλίο του μπήκε σχεδόν σε κάθε σπίτι", "Γιατί είχε τηλεοπτική εκπομπή", "Γιατί το αποφάσισε το υπουργείο"], 1, "Μπήκε σχεδόν σε κάθε ελληνικό σπίτι, γι’ αυτό το όνομά του έγινε κοινό ουσιαστικό"),
  Q("Ποια θετική συμβολή του αναγνωρίζει η ιστορικός;", ["Ότι κατέγραψε συστηματικά συνταγές με ακριβείς ποσότητες", "Ότι έφερε τα μπαχαρικά στην Ελλάδα", "Ότι μείωσε το βούτυρο", "Ότι κατάργησε τη γαλλική κουζίνα"], 0, "κατέγραψε συστηματικά συνταγές … και έδωσε ακριβείς ποσότητες"),
  Q("Πώς βλέπει τελικά η ιστορικός τον Τσελεμεντέ;", ["Ως τον κακό της ιστορίας", "Ως αγρότη μάγειρα", "Ως καθρέφτη μιας εποχής", "Ως άνθρωπο χωρίς επιρροή"], 2, "Θα έλεγα ότι είναι ο καθρέφτης μιας εποχής"),
 ],
 "gloss": {"εκδίδει": "εκδίδω — to publish", "Ζαχαροπλαστικής": "ζαχαροπλαστική — pastry-making", "αμέτρητες": "αμέτρητος — countless", "ουσιαστικό": "ουσιαστικό — noun", "κατηγορία": "κατηγορία — accusation", "εξευγενίσει": "εξευγενίζω — to refine, ennoble", "αποδίδεται": "αποδίδομαι — to be attributed", "αυτονόητη": "αυτονόητος — self-evident, taken for granted", "νοικοκυριών": "νοικοκυριό — household", "αστική": "αστικός — urban, middle-class", "όσπρια": "όσπρια — pulses, legumes", "αντίστροφο": "αντίστροφος — opposite, reverse"}
})

rnd = random.Random(261)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-261.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
