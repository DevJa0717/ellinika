# Source for library/listening/listening-134.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l134.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l134-ann-gyrisma", "title": "Κλειστοί δρόμοι για το γύρισμα μιας ταινίας", "title_en": "Streets closed for a film shoot", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε στο ραδιόφωνο μια ανακοίνωση του δήμου για κυκλοφοριακές ρυθμίσεις στο ιστορικό κέντρο.",
 "script": [
  L("Εκφωνήτρια", "f", "Ο δήμος ενημερώνει τους κατοίκους ότι από την Τρίτη έως και την Πέμπτη θα πραγματοποιηθεί στο ιστορικό κέντρο το γύρισμα μιας διεθνούς κινηματογραφικής παραγωγής.", "The municipality informs residents that from Tuesday to Thursday a scene of an international film production will be shot in the historic centre."),
  L("Εκφωνήτρια", "f", "Κατά τη διάρκεια των γυρισμάτων, από τις επτά το πρωί έως τις τρεις το απόγευμα, θα διακόπτεται η κυκλοφορία των οχημάτων στις οδούς γύρω από την κεντρική πλατεία. Οι κάτοικοι θα μπορούν να περνούν με τα πόδια, δείχνοντας την ταυτότητά τους στους υπαλλήλους της παραγωγής.", "During the shooting, from seven in the morning to three in the afternoon, vehicle traffic will be stopped in the streets around the central square. Residents will be able to pass on foot by showing their identity card to the production staff."),
  L("Εκφωνήτρια", "f", "Η παραγωγή αναζητά επίσης κατοίκους της περιοχής που θα ήθελαν να συμμετάσχουν ως κομπάρσοι. Οι ενδιαφερόμενοι μπορούν να δηλώσουν συμμετοχή στο Κέντρο Εξυπηρέτησης Πολιτών έως τη Δευτέρα.", "The production is also looking for local residents who would like to take part as extras. Those interested can sign up at the Citizens' Service Centre by Monday."),
 ],
 "questions": [
  Q("Γιατί θα κλείσουν οι δρόμοι;", ["Για έργα στο οδόστρωμα", "Για το γύρισμα μιας ταινίας", "Για μια πορεία", "Για έναν αγώνα δρόμου"], 1, "θα πραγματοποιηθεί στο ιστορικό κέντρο το γύρισμα μιας διεθνούς κινηματογραφικής παραγωγής"),
  Q("Πώς θα μπορούν να περνούν οι κάτοικοι;", ["Με το αυτοκίνητο, μετά τις επτά", "Μόνο με ειδική άδεια του δήμου", "Με τα πόδια, δείχνοντας την ταυτότητά τους", "Δεν θα μπορούν να περνούν καθόλου"], 2, "Οι κάτοικοι θα μπορούν να περνούν με τα πόδια, δείχνοντας την ταυτότητά τους"),
  Q("Τι ζητά η παραγωγή από τους κατοίκους;", ["Να συμμετάσχουν ως κομπάρσοι", "Να νοικιάσουν τα σπίτια τους", "Να μην ανοίγουν τα παράθυρα", "Να μετακινήσουν τα αυτοκίνητά τους στο λιμάνι"], 0, "αναζητά επίσης κατοίκους της περιοχής που θα ήθελαν να συμμετάσχουν ως κομπάρσοι"),
 ],
 "gloss": {"κυκλοφοριακές ρυθμίσεις": "κυκλοφοριακές ρυθμίσεις — traffic arrangements", "γύρισμα": "γύρισμα — (film) shoot", "κινηματογραφικής παραγωγής": "κινηματογραφική παραγωγή — film production", "διακόπτεται": "διακόπτομαι — to be stopped, interrupted", "οχημάτων": "όχημα — vehicle", "ταυτότητά": "ταυτότητα — identity card", "αναζητά": "αναζητώ — to look for", "κομπάρσοι": "κομπάρσος — extra (in a film)", "ενδιαφερόμενοι": "ενδιαφερόμενος — interested party", "δηλώσουν συμμετοχή": "δηλώνω συμμετοχή — to sign up"}
})

ITEMS.append({
 "id": "l134-vm-poleodomia", "title": "Μήνυμα από την πολεοδομία", "title_en": "A message from the planning office", "type": "voicemail", "level": "B2",
 "context_el": "Έχετε κάνει αίτηση για άδεια ανακαίνισης στο σπίτι σας. Ακούτε ένα μήνυμα στον τηλεφωνητή σας.",
 "script": [
  L("Υπάλληλος", "f", "Καλημέρα σας, σας καλώ από την Υπηρεσία Δόμησης του δήμου, για την αίτησή σας να επεκτείνετε το μπαλκόνι του διαμερίσματος. Ο φάκελός σας έχει ελεγχθεί, αλλά λείπει η έγκριση της γενικής συνέλευσης της πολυκατοικίας.", "Good morning, I'm calling from the municipality's Building Department about your application to extend the balcony of your flat. Your file has been checked, but the approval of the building's general meeting is missing."),
  L("Υπάλληλος", "f", "Χρειαζόμαστε το πρακτικό της συνέλευσης, υπογεγραμμένο από τον διαχειριστή, στο οποίο να φαίνεται ότι συμφωνεί η πλειοψηφία των ιδιοκτητών. Μπορείτε να το ανεβάσετε ηλεκτρονικά στην πλατφόρμα, δεν χρειάζεται να έρθετε.", "We need the minutes of the meeting, signed by the building manager, showing that the majority of owners agree. You can upload it online to the platform; there's no need to come in."),
  L("Υπάλληλος", "f", "Μόλις το λάβουμε, ο μηχανικός μας θα κάνει αυτοψία στο κτίριο, και η άδεια θα εκδοθεί μέσα σε περίπου δύο εβδομάδες. Για οποιαδήποτε απορία, καλέστε μας πρωινές ώρες. Ευχαριστώ.", "As soon as we receive it, our engineer will inspect the building, and the permit will be issued within about two weeks. For any questions, call us in the morning. Thank you."),
 ],
 "questions": [
  Q("Τι λείπει από τον φάκελο;", ["Τα σχέδια του μηχανικού", "Η έγκριση της γενικής συνέλευσης της πολυκατοικίας", "Η πληρωμή του παραβόλου", "Μια φωτογραφία του μπαλκονιού"], 1, "λείπει η έγκριση της γενικής συνέλευσης της πολυκατοικίας"),
  Q("Πώς μπορεί να σταλεί το έγγραφο;", ["Μόνο με ταχυδρομείο", "Αυτοπροσώπως στην υπηρεσία", "Ηλεκτρονικά στην πλατφόρμα", "Με φαξ"], 2, "Μπορείτε να το ανεβάσετε ηλεκτρονικά στην πλατφόρμα"),
  Q("Τι θα γίνει μόλις σταλεί το έγγραφο;", ["Ο μηχανικός θα κάνει αυτοψία στο κτίριο", "Η αίτηση θα απορριφθεί", "Θα χρειαστεί νέα αίτηση", "Θα αρχίσουν αμέσως οι εργασίες"], 0, "ο μηχανικός μας θα κάνει αυτοψία στο κτίριο"),
 ],
 "gloss": {"άδεια": "άδεια — permit", "ανακαίνισης": "ανακαίνιση — renovation", "Υπηρεσία Δόμησης": "Υπηρεσία Δόμησης — building (planning) department", "επεκτείνετε": "επεκτείνω — to extend", "φάκελός": "φάκελος — file", "έγκριση": "έγκριση — approval", "γενικής συνέλευσης": "γενική συνέλευση — general meeting", "πρακτικό": "πρακτικό — minutes (of a meeting)", "διαχειριστή": "διαχειριστής — building manager", "πλειοψηφία": "πλειοψηφία — majority", "αυτοψία": "αυτοψία — on-site inspection", "εκδοθεί": "εκδίδομαι — to be issued"}
})

ITEMS.append({
 "id": "l134-dial-xaderfos", "title": "Να φιλοξενήσουμε τον ξάδερφό σου;", "title_en": "Shall we put up your cousin?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι συζητά αν θα φιλοξενήσει για λίγο έναν συγγενή.",
 "script": [
  L("Άννα", "f", "Πήρε τηλέφωνο ο ξάδερφός μου ο Λευτέρης. Βρήκε δουλειά εδώ στην Αθήνα και ρωτάει αν μπορεί να μείνει μαζί μας έναν μήνα, μέχρι να βρει σπίτι.", "My cousin Lefteris called. He's found a job here in Athens and is asking if he can stay with us for a month, until he finds a place."),
  L("Νίκος", "m", "Έναν μήνα; Άννα, το διαμέρισμα είναι εξήντα τετραγωνικά. Πού θα κοιμάται; Στον καναπέ του σαλονιού, που δουλεύω κάθε μέρα από το σπίτι;", "A month? Anna, the flat is sixty square metres. Where will he sleep? On the living-room sofa, where I work from home every day?"),
  L("Άννα", "f", "Το ξέρω, δεν είναι ιδανικό. Αλλά τα ενοίκια είναι τρελά, και του έχουν ζητήσει τρία νοίκια προκαταβολή. Εκείνος μας φιλοξένησε στη Θεσσαλονίκη ολόκληρο καλοκαίρι, θυμάσαι.", "I know, it's not ideal. But rents are crazy, and they've asked him for three months' rent in advance. He put us up in Thessaloniki for a whole summer, remember."),
  L("Νίκος", "m", "Καλά, εντάξει. Αλλά να συμφωνήσουμε από την αρχή μια ημερομηνία, και τις μέρες που δουλεύω από το σπίτι να πηγαίνει κάπου αλλού μέχρι το απόγευμα.", "Fine, OK. But let's agree on a date from the start, and on the days I work from home he should go somewhere else until the afternoon."),
 ],
 "questions": [
  Q("Τι ζητάει ο ξάδερφος της Άννας;", ["Να του δανείσουν χρήματα", "Να μείνει μαζί τους έναν μήνα", "Να του βρουν δουλειά", "Να τον βοηθήσουν στη μετακόμιση"], 1, "ρωτάει αν μπορεί να μείνει μαζί μας έναν μήνα"),
  Q("Γιατί διστάζει ο Νίκος;", ["Γιατί δεν συμπαθεί τον Λευτέρη", "Γιατί περιμένουν κι άλλους επισκέπτες", "Γιατί το διαμέρισμα είναι μικρό και δουλεύει από το σπίτι", "Γιατί θα λείπουν διακοπές"], 2, "το διαμέρισμα είναι εξήντα τετραγωνικά"),
  Q("Με ποιον όρο συμφωνεί τελικά ο Νίκος;", ["Να ορίσουν μια ημερομηνία από την αρχή", "Να πληρώνει ο Λευτέρης ενοίκιο", "Να μείνει μόνο μία εβδομάδα", "Να κοιμάται στο δωμάτιο του Νίκου"], 0, "να συμφωνήσουμε από την αρχή μια ημερομηνία"),
 ],
 "gloss": {"φιλοξενήσει": "φιλοξενώ — to put up, host", "συγγενή": "συγγενής — relative", "ξάδερφός": "ξάδερφος — cousin", "τετραγωνικά": "τετραγωνικά — square metres", "καναπέ": "καναπές — sofa", "ενοίκια": "ενοίκιο — rent", "νοίκια": "νοίκι — rent (colloquial)", "προκαταβολή": "προκαταβολή — advance payment", "φιλοξένησε": "φιλοξενώ — to put up, host"}
})

ITEMS.append({
 "id": "l134-int-thalassia-biologos", "title": "Μια θαλάσσια βιολόγος σε ερευνητικό σκάφος", "title_en": "A marine biologist on a research vessel", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια ραδιοφωνική συνέντευξη με μια θαλάσσια βιολόγο που δουλεύει σε ερευνητικό σκάφος.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς είναι μια μέρα πάνω σε ένα ερευνητικό σκάφος;", "What is a day like on a research vessel?"),
  L("Βιολόγος", "f", "Ξεκινάμε πριν από την ανατολή. Παίρνουμε δείγματα νερού από διάφορα βάθη και μετράμε τη θερμοκρασία, την αλατότητα και το πλαγκτόν. Οι αποστολές κρατάνε συνήθως δύο με τρεις εβδομάδες, και δουλεύουμε σε βάρδιες, γιατί τα όργανα δεν σταματούν ούτε τη νύχτα.", "We start before sunrise. We take water samples from various depths and measure temperature, salinity and plankton. Missions usually last two to three weeks, and we work in shifts, because the instruments don't stop even at night."),
  L("Δημοσιογράφος", "m", "Τι έχετε παρατηρήσει τα τελευταία χρόνια;", "What have you observed in recent years?"),
  L("Βιολόγος", "f", "Ότι η θάλασσα ζεσταίνεται, και αυτό φαίνεται καθαρά στα δεδομένα. Βρίσκουμε όλο και συχνότερα είδη ψαριών που έρχονται από την Ερυθρά Θάλασσα. Το πιο δύσκολο, πάντως, δεν είναι η δουλειά· είναι η ναυτία τις πρώτες μέρες. Ακόμα και μετά από δεκαπέντε χρόνια, δεν τη συνήθισα.", "That the sea is warming, and it shows clearly in the data. We increasingly find fish species that come from the Red Sea. The hardest thing, though, isn't the work; it's the seasickness in the first days. Even after fifteen years, I haven't got used to it."),
 ],
 "questions": [
  Q("Τι κάνουν οι ερευνητές κάθε μέρα;", ["Ψαρεύουν για τις αγορές", "Παίρνουν δείγματα νερού και κάνουν μετρήσεις", "Καθαρίζουν παραλίες", "Ξεναγούν τουρίστες"], 1, "Παίρνουμε δείγματα νερού από διάφορα βάθη"),
  Q("Γιατί δουλεύουν σε βάρδιες;", ["Γιατί είναι λίγοι", "Γιατί το σκάφος κινείται μόνο τη νύχτα", "Γιατί τα όργανα δεν σταματούν ούτε τη νύχτα", "Γιατί το ζητά ο καπετάνιος"], 2, "τα όργανα δεν σταματούν ούτε τη νύχτα"),
  Q("Τι είναι το πιο δύσκολο για εκείνη;", ["Η ναυτία τις πρώτες μέρες", "Η απόσταση από την οικογένειά της", "Το φαγητό του πλοίου", "Οι πολλές ώρες δουλειάς"], 0, "είναι η ναυτία τις πρώτες μέρες"),
 ],
 "gloss": {"θαλάσσια βιολόγο": "θαλάσσιος βιολόγος — marine biologist", "ερευνητικό σκάφος": "ερευνητικό σκάφος — research vessel", "ανατολή": "ανατολή — sunrise", "δείγματα": "δείγμα — sample", "βάθη": "βάθος — depth", "αλατότητα": "αλατότητα — salinity", "πλαγκτόν": "πλαγκτόν — plankton", "αποστολές": "αποστολή — mission, expedition", "βάρδιες": "βάρδια — shift", "Ερυθρά Θάλασσα": "Ερυθρά Θάλασσα — Red Sea", "ναυτία": "ναυτία — seasickness"}
})

ITEMS.append({
 "id": "l134-rep-orchistra-anakyklosis", "title": "Μια ορχήστρα με όργανα από σκουπίδια", "title_en": "An orchestra with instruments made from rubbish", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για μια σχολική ορχήστρα με ασυνήθιστα μουσικά όργανα.",
 "script": [
  L("Ρεπόρτερ", "m", "Στο γυμνάσιο μιας μικρής πόλης της Θεσσαλίας, είκοσι μαθητές κουρδίζουν τα όργανά τους πριν από την πρόβα. Τα βιολιά τους είναι φτιαγμένα από τενεκεδάκια, οι κιθάρες από παλιά ταψιά και τα φλάουτα από σωλήνες ύδρευσης.", "At a lower secondary school in a small town in Thessaly, twenty pupils tune their instruments before rehearsal. Their violins are made from tin cans, the guitars from old baking trays and the flutes from water pipes."),
  L("Ρεπόρτερ", "m", "Την ιδέα την έφερε ο καθηγητής μουσικής, που είχε δει ένα ντοκιμαντέρ για μια ορχήστρα παιδιών από μια φτωχή γειτονιά της Παραγουάης, χτισμένη δίπλα σε μια χωματερή. Τα όργανα τα κατασκεύασαν οι ίδιοι οι μαθητές, με τη βοήθεια ενός ντόπιου τεχνίτη.", "The idea was brought by the music teacher, who had seen a documentary about a children's orchestra from a poor neighbourhood in Paraguay, built next to a landfill. The pupils made the instruments themselves, with the help of a local craftsman."),
  L("Ρεπόρτερ", "m", "Ο ήχος, παραδέχεται ο καθηγητής, δεν είναι ακριβώς σαν των κανονικών οργάνων. Το σημαντικό όμως είναι ότι πολλά παιδιά που δεν θα μπορούσαν ποτέ να αγοράσουν ένα όργανο, παίζουν τώρα μουσική. Τον Ιούνιο η ορχήστρα θα δώσει την πρώτη της συναυλία στην πλατεία της πόλης.", "The sound, the teacher admits, isn't exactly like that of ordinary instruments. What matters, though, is that many children who could never afford an instrument are now playing music. In June the orchestra will give its first concert in the town square."),
 ],
 "questions": [
  Q("Από τι είναι φτιαγμένα τα βιολιά;", ["Από ξύλο", "Από τενεκεδάκια", "Από πλαστικά μπουκάλια", "Από χαρτόνι"], 1, "Τα βιολιά τους είναι φτιαγμένα από τενεκεδάκια"),
  Q("Πού βρήκε την ιδέα ο καθηγητής;", ["Σε ένα βιβλίο", "Σε ένα φεστιβάλ στην Αθήνα", "Σε ένα ντοκιμαντέρ για μια ορχήστρα στην Παραγουάη", "Από έναν μαθητή του"], 2, "είχε δει ένα ντοκιμαντέρ για μια ορχήστρα παιδιών από μια φτωχή γειτονιά της Παραγουάης"),
  Q("Τι είναι το σημαντικό, κατά τον καθηγητή;", ["Ότι παιδιά που δεν θα μπορούσαν να αγοράσουν όργανο παίζουν τώρα μουσική", "Ότι ο ήχος είναι ίδιος με των κανονικών οργάνων", "Ότι η ορχήστρα θα κερδίσει βραβεία", "Ότι το σχολείο θα πουλήσει τα όργανα"], 0, "πολλά παιδιά που δεν θα μπορούσαν ποτέ να αγοράσουν ένα όργανο, παίζουν τώρα μουσική"),
 ],
 "gloss": {"ορχήστρα": "ορχήστρα — orchestra", "κουρδίζουν": "κουρδίζω — to tune", "πρόβα": "πρόβα — rehearsal", "τενεκεδάκια": "τενεκεδάκι — tin can", "ταψιά": "ταψί — baking tray", "σωλήνες ύδρευσης": "σωλήνας ύδρευσης — water pipe", "ντοκιμαντέρ": "ντοκιμαντέρ — documentary", "χωματερή": "χωματερή — landfill", "τεχνίτη": "τεχνίτης — craftsman", "παραδέχεται": "παραδέχομαι — to admit"}
})

ITEMS.append({
 "id": "l134-rep-scholeio-argotera", "title": "Ένα σχολείο που ξεκινά μία ώρα αργότερα", "title_en": "A school that starts an hour later", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ για ένα λύκειο που άλλαξε την ώρα έναρξης των μαθημάτων.",
 "script": [
  L("Ρεπόρτερ", "f", "Σε ένα λύκειο της Πάτρας, τα μαθήματα ξεκινούν πια στις εννιά αντί για τις οχτώ και δέκα. Η αλλαγή έγινε πιλοτικά φέτος, ύστερα από πρόταση του συλλόγου γονέων.", "At a high school in Patras, lessons now start at nine instead of ten past eight. The change was introduced this year as a pilot, following a proposal from the parents' association."),
  L("Ρεπόρτερ", "f", "Οι ειδικοί εξηγούν ότι στην εφηβεία το βιολογικό ρολόι μετατοπίζεται: οι έφηβοι νυστάζουν αργότερα το βράδυ και δυσκολεύονται να ξυπνήσουν νωρίς. Έτσι, πολλοί φτάνουν στην πρώτη ώρα χωρίς να έχουν κοιμηθεί αρκετά.", "Experts explain that in adolescence the body clock shifts: teenagers get sleepy later at night and find it hard to wake up early. So many arrive for the first lesson without having slept enough."),
  L("Ρεπόρτερ", "f", "Οι καθηγητές λένε ότι οι μαθητές είναι πιο συγκεντρωμένοι και ότι οι καθυστερήσεις έχουν μειωθεί. Υπάρχει όμως και ένα πρόβλημα: το σχολείο τελειώνει αργότερα, και οι μαθητές έχουν λιγότερο χρόνο για φροντιστήρια και αθλητισμό το απόγευμα.", "Teachers say pupils are more focused and that late arrivals have fallen. But there's also a problem: school finishes later, and pupils have less time for private lessons and sport in the afternoon."),
 ],
 "questions": [
  Q("Ποιος πρότεινε την αλλαγή;", ["Το υπουργείο", "Ο σύλλογος γονέων", "Οι μαθητές", "Ο διευθυντής"], 1, "ύστερα από πρόταση του συλλόγου γονέων"),
  Q("Τι συμβαίνει στο βιολογικό ρολόι στην εφηβεία, κατά τους ειδικούς;", ["Σταματά να λειτουργεί", "Οι έφηβοι νυστάζουν νωρίτερα", "Μετατοπίζεται και οι έφηβοι νυστάζουν αργότερα", "Οι έφηβοι χρειάζονται λιγότερο ύπνο"], 2, "οι έφηβοι νυστάζουν αργότερα το βράδυ"),
  Q("Ποιο πρόβλημα έχει προκύψει;", ["Οι μαθητές έχουν λιγότερο χρόνο το απόγευμα", "Οι καθυστερήσεις αυξήθηκαν", "Οι καθηγητές διαμαρτύρονται", "Τα λεωφορεία δεν ταιριάζουν με το νέο ωράριο"], 0, "οι μαθητές έχουν λιγότερο χρόνο για φροντιστήρια και αθλητισμό το απόγευμα"),
 ],
 "gloss": {"έναρξης": "έναρξη — start", "πιλοτικά": "πιλοτικά — as a pilot (trial)", "συλλόγου γονέων": "σύλλογος γονέων — parents' association", "εφηβεία": "εφηβεία — adolescence", "βιολογικό ρολόι": "βιολογικό ρολόι — body clock", "μετατοπίζεται": "μετατοπίζομαι — to shift", "νυστάζουν": "νυστάζω — to feel sleepy", "συγκεντρωμένοι": "συγκεντρωμένος — focused", "καθυστερήσεις": "καθυστέρηση — late arrival, delay", "φροντιστήρια": "φροντιστήριο — private tutoring school"}
})

ITEMS.append({
 "id": "l134-mono-enoikio", "title": "Γιατί προτιμώ να νοικιάζω", "title_en": "Why I prefer to rent", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα εξηγεί σε ένα πόντκαστ γιατί δεν θέλει να αγοράσει σπίτι.",
 "script": [
  L("Ελένη", "f", "Οι γονείς μου μού λένε συνέχεια ότι πετάω τα λεφτά μου στο ενοίκιο και ότι πρέπει να αγοράσω σπίτι. Για τη δική τους γενιά, το σπίτι ήταν η μεγαλύτερη ασφάλεια. Για μένα, είναι μια δέσμευση για τριάντα χρόνια.", "My parents keep telling me I'm throwing my money away on rent and that I should buy a house. For their generation, a house was the greatest security. For me, it's a thirty-year commitment."),
  L("Ελένη", "f", "Δουλεύω σε ένα επάγγελμα όπου αλλάζεις πόλη κάθε λίγα χρόνια. Μέσα σε μια δεκαετία έχω ζήσει σε τρεις πόλεις. Αν είχα πάρει δάνειο, θα έπρεπε είτε να αρνηθώ ευκαιρίες είτε να ψάχνω ενοικιαστές από μακριά.", "I work in a profession where you change city every few years. Within a decade I've lived in three cities. If I'd taken out a loan, I'd have had to either turn down opportunities or look for tenants from far away."),
  L("Ελένη", "f", "Δεν λέω ότι δεν θα αγοράσω ποτέ. Ίσως, όταν αποφασίσω πού θέλω να μείνω, να το σκεφτώ. Μέχρι τότε, προτιμώ την ελευθερία μου, ακόμα κι αν μου κοστίζει λίγο περισσότερο.", "I'm not saying I'll never buy. Maybe, when I decide where I want to settle, I'll think about it. Until then, I prefer my freedom, even if it costs me a bit more."),
 ],
 "questions": [
  Q("Τι λένε οι γονείς της;", ["Ότι πρέπει να μετακομίσει κοντά τους", "Ότι πετάει τα λεφτά της στο ενοίκιο", "Ότι πρέπει να αλλάξει δουλειά", "Ότι το σπίτι της είναι πολύ μικρό"], 1, "πετάω τα λεφτά μου στο ενοίκιο"),
  Q("Γιατί δεν θέλει να πάρει δάνειο;", ["Γιατί έχει ήδη χρέη", "Γιατί η τράπεζα δεν της δίνει", "Γιατί αλλάζει πόλη κάθε λίγα χρόνια λόγω δουλειάς", "Γιατί τα σπίτια είναι παλιά"], 2, "Δουλεύω σε ένα επάγγελμα όπου αλλάζεις πόλη κάθε λίγα χρόνια"),
  Q("Θα αγοράσει ποτέ σπίτι;", ["Ίσως, όταν αποφασίσει πού θέλει να μείνει", "Ποτέ", "Τον επόμενο χρόνο", "Μόνο αν της το χαρίσουν οι γονείς της"], 0, "όταν αποφασίσω πού θέλω να μείνω, να το σκεφτώ"),
 ],
 "gloss": {"πόντκαστ": "πόντκαστ — podcast", "ενοίκιο": "ενοίκιο — rent", "γενιά": "γενιά — generation", "ασφάλεια": "ασφάλεια — security", "δέσμευση": "δέσμευση — commitment", "επάγγελμα": "επάγγελμα — profession", "δάνειο": "δάνειο — loan", "αρνηθώ": "αρνούμαι — to refuse, turn down", "ενοικιαστές": "ενοικιαστής — tenant"}
})

ITEMS.append({
 "id": "l134-mono-anagnostria-nosokomeiou", "title": "Διαβάζω παραμύθια σε ένα νοσοκομείο παίδων", "title_en": "I read stories in a children's hospital", "type": "monologue", "level": "B2",
 "context_el": "Ένας συνταξιούχος μιλά σε μια ραδιοφωνική εκπομπή για την εθελοντική του δουλειά.",
 "script": [
  L("Θανάσης", "m", "Όταν βγήκα στη σύνταξη, ένιωθα ότι οι μέρες δεν τελείωναν. Η κόρη μου, που είναι νοσηλεύτρια, μου είπε ότι στο νοσοκομείο παίδων ζητούσαν εθελοντές για να διαβάζουν βιβλία στα παιδιά. Έτσι ξεκίνησα, πριν από τρία χρόνια.", "When I retired, I felt the days never ended. My daughter, who is a nurse, told me that the children's hospital was looking for volunteers to read books to the children. That's how I started, three years ago."),
  L("Θανάσης", "m", "Πηγαίνω κάθε Τρίτη και Πέμπτη απόγευμα. Στην αρχή ήμουν αμήχανος, δεν ήξερα τι να πω σε ένα άρρωστο παιδί. Γρήγορα όμως κατάλαβα ότι δεν χρειάζεται να πεις πολλά· αρκεί να είσαι εκεί και να κάνεις φωνές για τους λύκους και τους δράκους.", "I go every Tuesday and Thursday afternoon. At first I felt awkward; I didn't know what to say to a sick child. But I soon understood that you don't need to say much; it's enough to be there and do voices for the wolves and the dragons."),
  L("Θανάσης", "m", "Κάποια παιδιά μένουν μήνες στο νοσοκομείο. Ένα κορίτσι με περίμενε κάθε φορά στην πόρτα του θαλάμου. Όταν πήρε εξιτήριο, μου άφησε μια ζωγραφιά με έναν δράκο που διάβαζε βιβλίο. Την έχω κρεμάσει πάνω από το γραφείο μου.", "Some children stay in hospital for months. One girl waited for me every time at the door of the ward. When she was discharged, she left me a drawing of a dragon reading a book. I've hung it above my desk."),
 ],
 "questions": [
  Q("Πώς έμαθε για την εθελοντική δουλειά;", ["Από μια διαφήμιση", "Από την κόρη του, που είναι νοσηλεύτρια", "Από τον γιατρό του", "Από έναν φίλο του"], 1, "Η κόρη μου, που είναι νοσηλεύτρια, μου είπε"),
  Q("Τι κατάλαβε μετά τις πρώτες φορές;", ["Ότι δεν του ταιριάζει αυτή η δουλειά", "Ότι πρέπει να μιλάει πολύ στα παιδιά", "Ότι αρκεί να είναι εκεί και να κάνει φωνές", "Ότι τα παιδιά προτιμούν τα παιχνίδια"], 2, "αρκεί να είσαι εκεί και να κάνεις φωνές για τους λύκους και τους δράκους"),
  Q("Τι του άφησε το κορίτσι όταν πήρε εξιτήριο;", ["Μια ζωγραφιά με έναν δράκο που διάβαζε βιβλίο", "Ένα βιβλίο", "Ένα γράμμα", "Ένα λούτρινο ζωάκι"], 0, "μου άφησε μια ζωγραφιά με έναν δράκο που διάβαζε βιβλίο"),
 ],
 "gloss": {"συνταξιούχος": "συνταξιούχος — pensioner", "σύνταξη": "βγαίνω στη σύνταξη — to retire", "νοσηλεύτρια": "νοσηλεύτρια — nurse (f.)", "νοσοκομείο παίδων": "νοσοκομείο παίδων — children's hospital", "εθελοντές": "εθελοντής — volunteer", "αμήχανος": "αμήχανος — awkward", "δράκους": "δράκος — dragon", "θαλάμου": "θάλαμος — (hospital) ward", "εξιτήριο": "παίρνω εξιτήριο — to be discharged", "ζωγραφιά": "ζωγραφιά — drawing"}
})

ITEMS.append({
 "id": "l134-c1-ntintero", "title": "Η ρόμπα του Ντιντερό", "title_en": "Diderot's dressing gown", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από μια διάλεξη για την ψυχολογία της κατανάλωσης.",
 "script": [
  L("Ομιλήτρια", "f", "Το 1769 ο Γάλλος φιλόσοφος Ντενί Ντιντερό έγραψε ένα σύντομο, αυτοσαρκαστικό δοκίμιο με τίτλο «Λύπη για την παλιά μου ρόμπα». Ένας φίλος τού είχε χαρίσει μια πολυτελή κόκκινη ρόμπα, και ο Ντιντερό πέταξε την παλιά, φθαρμένη αλλά άνετη ρόμπα του.", "In 1769 the French philosopher Denis Diderot wrote a short, self-mocking essay titled 'Regrets on my old dressing gown'. A friend had given him a luxurious scarlet dressing gown, and Diderot threw away his old, worn but comfortable one."),
  L("Ομιλήτρια", "f", "Σύντομα, όμως, παρατήρησε κάτι παράξενο. Δίπλα στη νέα ρόμπα, όλα στο γραφείο του φαίνονταν φτωχικά: η ψάθινη καρέκλα, το ξύλινο γραφείο, η ταπετσαρία. Ένα ένα, τα αντικατέστησε όλα, και στο τέλος βρέθηκε χρεωμένος, σε ένα δωμάτιο που δεν αναγνώριζε, και, όπως ομολογεί, λιγότερο ευτυχισμένος.", "Soon, however, he noticed something strange. Next to the new gown, everything in his study looked shabby: the straw chair, the wooden desk, the wallpaper. One by one, he replaced them all, and in the end found himself in debt, in a room he did not recognise, and, as he confesses, less happy."),
  L("Ομιλήτρια", "f", "Δύο αιώνες αργότερα, ο ανθρωπολόγος Γκραντ ΜακΚράκεν ονόμασε το φαινόμενο «φαινόμενο Ντιντερό». Τα αντικείμενα που έχουμε, υποστήριξε, σχηματίζουν ένα πολιτισμικά συνεπές σύνολο. Όταν προσθέτουμε ένα καινούργιο, που δεν ταιριάζει, νιώθουμε την ανάγκη να αλλάξουμε και τα υπόλοιπα, για να αποκατασταθεί η αρμονία.", "Two centuries later, the anthropologist Grant McCracken named the phenomenon the 'Diderot effect'. The objects we own, he argued, form a culturally consistent whole. When we add a new one that doesn't fit, we feel the need to change the rest too, to restore harmony."),
  L("Ομιλήτρια", "f", "Η σύγχρονη διαφήμιση γνωρίζει καλά αυτόν τον μηχανισμό: ένα καινούργιο κινητό απαιτεί καινούργια θήκη, καινούργια ακουστικά, ίσως και καινούργιο ρολόι. Το δοκίμιο του Ντιντερό μάς προτείνει μια απλή ερώτηση πριν από κάθε αγορά: τι άλλο θα με κάνει αυτό να θέλω;", "Modern advertising knows this mechanism well: a new phone calls for a new case, new earphones, perhaps a new watch too. Diderot's essay suggests a simple question before every purchase: what else will this make me want?"),
 ],
 "questions": [
  Q("Τι συνέβη στον Ντιντερό;", ["Έχασε την αγαπημένη του ρόμπα", "Ένας φίλος του χάρισε μια πολυτελή κόκκινη ρόμπα", "Αγόρασε ένα καινούργιο γραφείο", "Μετακόμισε σε ένα μεγαλύτερο σπίτι"], 1, "Ένας φίλος τού είχε χαρίσει μια πολυτελή κόκκινη ρόμπα"),
  Q("Τι έκανε μετά, σύμφωνα με το δοκίμιο;", ["Επέστρεψε τη ρόμπα στον φίλο του", "Έγραψε ένα βιβλίο για τη μόδα", "Αντικατέστησε ένα ένα όλα τα πράγματα του γραφείου του", "Πούλησε την παλιά του ρόμπα"], 2, "Ένα ένα, τα αντικατέστησε όλα"),
  Q("Πώς εξήγησε ο ΜακΚράκεν το φαινόμενο;", ["Τα αντικείμενά μας σχηματίζουν ένα συνεπές σύνολο, και ένα νέο που δεν ταιριάζει μας σπρώχνει να αλλάξουμε τα υπόλοιπα", "Οι άνθρωποι βαριούνται γρήγορα τα πράγματά τους", "Η διαφήμιση μάς αναγκάζει να αγοράζουμε", "Τα πολυτελή αντικείμενα χαλάνε ευκολότερα"], 0, "Τα αντικείμενα που έχουμε, υποστήριξε, σχηματίζουν ένα πολιτισμικά συνεπές σύνολο"),
  Q("Τι προτείνει η ομιλήτρια, με αφορμή το δοκίμιο;", ["Να μην αγοράζουμε ποτέ τίποτα καινούργιο", "Να αγοράζουμε μόνο ακριβά πράγματα", "Να αγνοούμε τη διαφήμιση", "Να αναρωτιόμαστε πριν από κάθε αγορά τι άλλο θα μας κάνει να θέλουμε"], 3, "τι άλλο θα με κάνει αυτό να θέλω"),
 ],
 "gloss": {"κατανάλωσης": "κατανάλωση — consumption", "αυτοσαρκαστικό": "αυτοσαρκαστικός — self-mocking", "δοκίμιο": "δοκίμιο — essay", "ρόμπα": "ρόμπα — dressing gown", "πολυτελή": "πολυτελής — luxurious", "φθαρμένη": "φθαρμένος — worn", "φτωχικά": "φτωχικός — shabby, humble", "ψάθινη": "ψάθινος — straw, wicker", "ταπετσαρία": "ταπετσαρία — wallpaper", "χρεωμένος": "χρεωμένος — in debt", "ομολογεί": "ομολογώ — to confess", "ανθρωπολόγος": "ανθρωπολόγος — anthropologist", "συνεπές": "συνεπής — consistent", "αποκατασταθεί": "αποκαθίσταμαι — to be restored", "θήκη": "θήκη — case, cover"}
})

ITEMS.append({
 "id": "l134-c1-vamvas", "title": "Νεόφυτος Βάμβας, ο δάσκαλος της Χίου", "title_en": "Neofytos Vamvas, the teacher of Chios", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με έναν ιστορικό για τον λόγιο κληρικό Νεόφυτο Βάμβα.",
 "script": [
  L("Δημοσιογράφος", "f", "Ποιος ήταν ο Νεόφυτος Βάμβας;", "Who was Neofytos Vamvas?"),
  L("Ιστορικός", "m", "Ήταν κληρικός και δάσκαλος, ένας από τους σημαντικούς λόγιους του Νεοελληνικού Διαφωτισμού. Γεννήθηκε στη Χίο γύρω στο 1770 και σπούδασε στο Παρίσι, όπου συνδέθηκε με τον Αδαμάντιο Κοραή. Όταν γύρισε, ανέλαβε τη διεύθυνση της περίφημης Σχολής της Χίου, η οποία, σύμφωνα με τις πηγές, είχε τότε εκατοντάδες μαθητές από όλο τον ελληνικό κόσμο.", "He was a cleric and teacher, one of the important scholars of the Modern Greek Enlightenment. He was born on Chios around 1770 and studied in Paris, where he became associated with Adamantios Korais. When he returned, he took over the direction of the famous School of Chios, which, according to the sources, then had hundreds of pupils from all over the Greek world."),
  L("Δημοσιογράφος", "f", "Και μετά την Επανάσταση;", "And after the Revolution?"),
  L("Ιστορικός", "m", "Πήρε μέρος στον Αγώνα, και αργότερα, όταν ιδρύθηκε το Πανεπιστήμιο Αθηνών, το 1837, έγινε ένας από τους πρώτους καθηγητές του και δίδαξε φιλοσοφία. Έγραψε επίσης εγχειρίδια, γιατί πίστευε ότι ένα νέο κράτος χρειάζεται πρώτα απ' όλα καλά σχολικά βιβλία.", "He took part in the struggle, and later, when the University of Athens was founded in 1837, he became one of its first professors and taught philosophy. He also wrote textbooks, because he believed a new state needs good schoolbooks above all."),
  L("Δημοσιογράφος", "f", "Γιατί όμως το όνομά του προκαλούσε αντιδράσεις;", "But why did his name provoke reactions?"),
  L("Ιστορικός", "m", "Κυρίως εξαιτίας της μετάφρασης της Αγίας Γραφής στη γλώσσα της εποχής του, που έγινε με τη στήριξη μιας βρετανικής εταιρείας. Πολλοί στην Εκκλησία θεώρησαν απαράδεκτο να μεταφραστεί το ιερό κείμενο, και η μετάφραση καταδικάστηκε. Σήμερα πολλοί ιστορικοί τη βλέπουν ως μια πρώιμη απόπειρα να γίνει το κείμενο κατανοητό σε όλους.", "Mainly because of his translation of the Bible into the language of his time, which was made with the support of a British society. Many in the Church considered it unacceptable for the sacred text to be translated, and the translation was condemned. Today many historians see it as an early attempt to make the text understandable to everyone."),
 ],
 "questions": [
  Q("Με ποιον συνδέθηκε στο Παρίσι;", ["Με τον Ρήγα Βελεστινλή", "Με τον Αδαμάντιο Κοραή", "Με τον Ιωάννη Καποδίστρια", "Με τον Ευγένιο Βούλγαρι"], 1, "όπου συνδέθηκε με τον Αδαμάντιο Κοραή"),
  Q("Τι έκανε όταν ιδρύθηκε το Πανεπιστήμιο Αθηνών;", ["Έγινε πρύτανης", "Αρνήθηκε να διδάξει", "Έγινε ένας από τους πρώτους καθηγητές και δίδαξε φιλοσοφία", "Ίδρυσε μια βιβλιοθήκη"], 2, "έγινε ένας από τους πρώτους καθηγητές του και δίδαξε φιλοσοφία"),
  Q("Γιατί έγραψε σχολικά εγχειρίδια;", ["Γιατί πίστευε ότι ένα νέο κράτος χρειάζεται πρώτα απ' όλα καλά σχολικά βιβλία", "Για να κερδίσει χρήματα", "Γιατί του το ζήτησε ο Κοραής", "Γιατί δεν υπήρχαν τυπογραφεία"], 0, "πίστευε ότι ένα νέο κράτος χρειάζεται πρώτα απ' όλα καλά σχολικά βιβλία"),
  Q("Γιατί προκάλεσε αντιδράσεις η μετάφραση της Αγίας Γραφής;", ["Γιατί είχε πολλά λάθη", "Γιατί ήταν πολύ ακριβή", "Γιατί γράφτηκε στα γαλλικά", "Γιατί πολλοί στην Εκκλησία θεώρησαν απαράδεκτο να μεταφραστεί το ιερό κείμενο"], 3, "Πολλοί στην Εκκλησία θεώρησαν απαράδεκτο να μεταφραστεί το ιερό κείμενο"),
 ],
 "gloss": {"λόγιο": "λόγιος — scholar", "κληρικό": "κληρικός — cleric", "Διαφωτισμού": "Διαφωτισμός — the Enlightenment", "συνδέθηκε": "συνδέομαι — to become associated", "διεύθυνση": "διεύθυνση — direction, headship", "περίφημης": "περίφημος — famous", "εγχειρίδια": "εγχειρίδιο — textbook, manual", "Αγίας Γραφής": "Αγία Γραφή — the Bible", "στήριξη": "στήριξη — support", "απαράδεκτο": "απαράδεκτος — unacceptable", "καταδικάστηκε": "καταδικάζομαι — to be condemned", "πρώιμη": "πρώιμος — early", "απόπειρα": "απόπειρα — attempt"}
})

rnd = random.Random(134)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-134.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
