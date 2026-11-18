# Source for library/listening/listening-204.json: five more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l204.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l204-ann-pyrosvestiki-anoixti-mera", "title": "Ανοιχτή μέρα στον πυροσβεστικό σταθμό", "title_en": "Open day at the fire station", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στο ραδιόφωνο ενός δήμου.",
 "script": [
  L("Εκφωνήτρια", "f", "Την Κυριακή, από τις δέκα το πρωί ως τις δύο το μεσημέρι, ο πυροσβεστικός σταθμός της πόλης ανοίγει τις πόρτες του στο κοινό. Μικροί και μεγάλοι θα μπορούν να ανέβουν στα οχήματα, να δοκιμάσουν τον εξοπλισμό των πυροσβεστών και, για τους πιο τολμηρούς, να κρατήσουν για λίγο τη μάνικα.", "On Sunday, from ten in the morning until two in the afternoon, the town's fire station opens its doors to the public. Young and old will be able to climb into the vehicles, try out the firefighters' equipment and, for the bravest, hold the hose for a while."),
  L("Εκφωνήτρια", "f", "Στις έντεκα και στις δώδεκα και μισή θα γίνει επίδειξη χρήσης πυροσβεστήρα. Οι πυροσβέστες θα εξηγήσουν επίσης πού πρέπει να τοποθετούνται οι ανιχνευτές καπνού στο σπίτι και τι κάνουμε αν πιάσει φωτιά το τηγάνι. Το πιο σημαντικό: ποτέ νερό στο καυτό λάδι.", "At eleven and at half past twelve there will be a demonstration of how to use a fire extinguisher. The firefighters will also explain where smoke detectors should be placed in the home and what to do if a frying pan catches fire. The most important thing: never water on hot oil."),
  L("Εκφωνήτρια", "f", "Η είσοδος είναι ελεύθερη. Επειδή ο χώρος στάθμευσης του σταθμού πρέπει να μείνει πάντα ελεύθερος για τα οχήματα, παρακαλούμε να έρθετε με τα πόδια ή με το λεωφορείο.", "Admission is free. Because the station's parking area must always remain clear for the vehicles, please come on foot or by bus."),
 ],
 "questions": [
  Q("Τι θα μπορούν να κάνουν οι πιο τολμηροί επισκέπτες;", ["Να οδηγήσουν ένα όχημα", "Να κρατήσουν για λίγο τη μάνικα", "Να σβήσουν μια αληθινή φωτιά", "Να ανέβουν στη σκάλα"], 1, "να κρατήσουν για λίγο τη μάνικα"),
  Q("Ποια συμβουλή χαρακτηρίζεται ως η πιο σημαντική;", ["Να έχουμε πυροσβεστήρα στο αυτοκίνητο", "Ποτέ νερό στο καυτό λάδι", "Να ανοίγουμε τα παράθυρα", "Να καλούμε τους γείτονες"], 1, "ποτέ νερό στο καυτό λάδι"),
  Q("Γιατί ζητούν από τους επισκέπτες να μην έρθουν με αυτοκίνητο;", ["Γιατί δεν υπάρχει δρόμος", "Γιατί ο χώρος στάθμευσης πρέπει να μείνει ελεύθερος για τα οχήματα", "Για περιβαλλοντικούς λόγους", "Γιατί θα γίνουν έργα"], 1, "ο χώρος στάθμευσης του σταθμού πρέπει να μείνει πάντα ελεύθερος"),
 ],
 "gloss": {"πυροσβεστικός σταθμός": "πυροσβεστικός σταθμός — fire station", "εξοπλισμό": "εξοπλισμός — equipment", "τολμηρούς": "τολμηρός — bold, brave", "μάνικα": "μάνικα — fire hose", "επίδειξη": "επίδειξη — demonstration", "πυροσβεστήρα": "πυροσβεστήρας — fire extinguisher", "ανιχνευτές καπνού": "ανιχνευτής καπνού — smoke detector"},
})
ITEMS.append({
 "id": "l204-dia-organosi-gamou", "title": "Διοργανώτρια γάμων ή όλα μόνοι μας;", "title_en": "Shall we hire a wedding planner or do it all ourselves?", "type": "dialogue", "level": "B2",
 "context_el": "Ένα ζευγάρι που θα παντρευτεί το καλοκαίρι συζητά την οργάνωση του γάμου.",
 "script": [
  L("Δανάη", "f", "Η ξαδέρφη μου μού έδωσε το τηλέφωνο μιας διοργανώτριας γάμων. Αναλαμβάνει τα πάντα: κτήμα, λουλούδια, μουσική, ακόμα και το πρόγραμμα της βραδιάς. Εμείς απλώς εμφανιζόμαστε.", "My cousin gave me the number of a wedding planner. She takes care of everything: the venue, flowers, music, even the evening's schedule. We just show up."),
  L("Νίκος", "m", "Και πόσο κοστίζει αυτή η ευτυχία; Με αυτά τα λεφτά θα μπορούσαμε να πάμε ένα ταξίδι του μέλιτος στην Ιαπωνία.", "And how much does this happiness cost? With that money we could go on a honeymoon to Japan."),
  L("Δανάη", "f", "Ζητάει ένα ποσοστό επί του συνολικού κόστους. Σκέψου όμως τι γλιτώνουμε: δεν θα περάσουμε έξι μήνες κάνοντας τηλέφωνα σε μαγαζιά. Και συχνά τέτοιοι επαγγελματίες παίρνουν καλύτερες τιμές από τους προμηθευτές.", "She asks for a percentage of the total cost. But think what we save: we won't spend six months phoning shops. And professionals like that often get better prices from suppliers."),
  L("Νίκος", "m", "Δεν θέλω όμως να γίνει ο γάμος μας ένα πακέτο από κατάλογο. Μου αρέσει η ιδέα να φτιάξουμε κάποια πράγματα μόνοι μας, με τους φίλους μας.", "But I don't want our wedding to become a package from a catalogue. I like the idea of making some things ourselves, with our friends."),
  L("Δανάη", "f", "Τότε ας τη συναντήσουμε μια φορά και ας τη ρωτήσουμε αν δέχεται να αναλάβει μόνο την οργάνωση της ημέρας. Τα υπόλοιπα, τις προσκλήσεις και τη διακόσμηση, τα κάνουμε εμείς με την παρέα.", "Then let's meet her once and ask whether she'd agree to handle only the organisation of the day itself. The rest, the invitations and decorations, we'll do ourselves with our friends."),
 ],
 "questions": [
  Q("Γιατί διστάζει ο Νίκος;", ["Γιατί δεν του αρέσουν τα λουλούδια", "Λόγω του κόστους, που θα αρκούσε για ένα ταξίδι", "Γιατί δεν θέλει γάμο", "Γιατί η διοργανώτρια μένει μακριά"], 1, "Με αυτά τα λεφτά θα μπορούσαμε να πάμε ένα ταξίδι του μέλιτος"),
  Q("Ποιο πλεονέκτημα αναφέρει η Δανάη;", ["Ότι η διοργανώτρια είναι φίλη τους", "Ότι γλιτώνουν χρόνο και ίσως παίρνουν καλύτερες τιμές", "Ότι η διοργανώτρια δεν πληρώνεται", "Ότι ο γάμος θα γίνει πιο γρήγορα"], 1, "συχνά τέτοιοι επαγγελματίες παίρνουν καλύτερες τιμές από τους προμηθευτές"),
  Q("Ποια λύση προτείνει τελικά η Δανάη;", ["Να μην κάνουν γάμο", "Η διοργανώτρια να αναλάβει μόνο την οργάνωση της ημέρας", "Να τα κάνει όλα η ξαδέρφη της", "Να πάνε μόνο ταξίδι"], 1, "αν δέχεται να αναλάβει μόνο την οργάνωση της ημέρας"),
 ],
 "gloss": {"διοργανώτριας": "διοργανώτρια — organiser, planner", "κτήμα": "κτήμα — estate, (wedding) venue", "ταξίδι του μέλιτος": "ταξίδι του μέλιτος — honeymoon", "ποσοστό": "ποσοστό — percentage", "γλιτώνουμε": "γλιτώνω — to save, spare", "προμηθευτές": "προμηθευτής — supplier", "διακόσμηση": "διακόσμηση — decoration"},
})
ITEMS.append({
 "id": "l204-news-yperpanselinos", "title": "Υπερπανσέληνος απόψε", "title_en": "A supermoon tonight", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ενός ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνητής", "m", "Όσοι σηκώσουν απόψε το βλέμμα στον ουρανό θα δουν μια υπερπανσέληνο. Ο όρος χρησιμοποιείται όταν η πανσέληνος συμπίπτει με τη στιγμή που η Σελήνη βρίσκεται κοντά στο πλησιέστερο σημείο της τροχιάς της γύρω από τη Γη.", "Those who look up at the sky tonight will see a supermoon. The term is used when the full moon coincides with the moment the Moon is near the closest point of its orbit around the Earth."),
  L("Εκφωνητής", "m", "Σύμφωνα με τους αστρονόμους, η Σελήνη θα φαίνεται έως και δεκατέσσερα τοις εκατό μεγαλύτερη και περίπου τριάντα τοις εκατό φωτεινότερη σε σύγκριση με μια πανσέληνο στο πιο απομακρυσμένο σημείο της τροχιάς. Στην πράξη, όμως, η διαφορά δεν είναι εύκολο να γίνει αντιληπτή με γυμνό μάτι.", "According to astronomers, the Moon will appear up to fourteen per cent larger and about thirty per cent brighter compared with a full moon at the most distant point of its orbit. In practice, however, the difference is not easy to notice with the naked eye."),
  L("Εκφωνητής", "m", "Το πιο εντυπωσιακό θέαμα θα είναι την ώρα που η Σελήνη ανατέλλει, λίγο μετά τη δύση του ήλιου, όταν, κοντά στον ορίζοντα, μοιάζει πάντα πιο μεγάλη. Οι επιστήμονες υπενθυμίζουν ότι η υπερπανσέληνος προκαλεί μόνο ελαφρώς ψηλότερες παλίρροιες και δεν έχει καμία αποδεδειγμένη σχέση με σεισμούς.", "The most impressive sight will be when the Moon rises, shortly after sunset, when, near the horizon, it always looks larger. Scientists remind us that the supermoon causes only slightly higher tides and has no proven link with earthquakes."),
 ],
 "questions": [
  Q("Πότε μιλάμε για υπερπανσέληνο;", ["Όταν υπάρχει έκλειψη", "Όταν η πανσέληνος συμπίπτει με το πλησιέστερο σημείο της τροχιάς της Σελήνης", "Όταν η Σελήνη είναι κόκκινη", "Όταν έχει δύο πανσελήνους σε έναν μήνα"], 1, "όταν η πανσέληνος συμπίπτει με τη στιγμή που η Σελήνη βρίσκεται κοντά στο πλησιέστερο σημείο"),
  Q("Τι λέει η είδηση για τη διαφορά στο μέγεθος;", ["Ότι είναι τεράστια", "Ότι δεν είναι εύκολο να γίνει αντιληπτή με γυμνό μάτι", "Ότι φαίνεται μόνο με τηλεσκόπιο", "Ότι δεν υπάρχει καμία διαφορά"], 1, "η διαφορά δεν είναι εύκολο να γίνει αντιληπτή με γυμνό μάτι"),
  Q("Τι υπενθυμίζουν οι επιστήμονες;", ["Ότι προκαλεί σεισμούς", "Ότι προκαλεί μόνο ελαφρώς ψηλότερες παλίρροιες", "Ότι είναι επικίνδυνη για τα μάτια", "Ότι επηρεάζει τον ύπνο"], 1, "προκαλεί μόνο ελαφρώς ψηλότερες παλίρροιες"),
 ],
 "gloss": {"υπερπανσέληνο": "υπερπανσέληνος — supermoon", "συμπίπτει": "συμπίπτω — to coincide", "πλησιέστερο": "πλησιέστερος — nearest", "τροχιάς": "τροχιά — orbit", "απομακρυσμένο": "απομακρυσμένος — distant", "αντιληπτή": "αντιληπτός — perceptible", "ανατέλλει": "ανατέλλω — to rise (of sun/moon)", "παλίρροιες": "παλίρροια — tide"},
})
ITEMS.append({
 "id": "l204-c1-mono-megethos-seismou", "title": "Τι σημαίνουν τα «Ρίχτερ»;", "title_en": "What the magnitude of an earthquake really measures", "type": "monologue", "level": "C1",
 "context_el": "Μια σεισμολόγος μιλάει σε μια εκδήλωση για το κοινό σχετικά με το πώς μετριούνται οι σεισμοί.",
 "script": [
  L("Σεισμολόγος", "f", "Μετά από κάθε σεισμό ακούμε ότι «ήταν πέντε Ρίχτερ» ή «έξι Ρίχτερ». Η κλίμακα που πρότεινε ο Τσαρλς Ρίχτερ το 1935 ήταν μια επανάσταση, γιατί για πρώτη φορά έδινε στον σεισμό έναν αριθμό, ανεξάρτητο από το πόσο τον ένιωσε ο καθένας. Έχει όμως ένα χαρακτηριστικό που ξεγελάει σχεδόν όλους: είναι λογαριθμική.", "After every earthquake we hear that 'it was five on the Richter scale' or 'six'. The scale proposed by Charles Richter in 1935 was a revolution, because for the first time it gave an earthquake a number, independent of how strongly each person felt it. But it has one feature that fools almost everyone: it is logarithmic."),
  L("Σεισμολόγος", "f", "Αυτό σημαίνει ότι κάθε μονάδα παραπάνω δεν είναι «λίγο πιο δυνατή». Ένας σεισμός έξι βαθμών προκαλεί δονήσεις με δεκαπλάσιο εύρος από έναν σεισμό πέντε βαθμών και απελευθερώνει περίπου τριάντα φορές περισσότερη ενέργεια. Από το πέντε στο επτά, η ενέργεια πολλαπλασιάζεται περίπου επί χίλια. Γι' αυτό ένας σεισμός επτά βαθμών δεν είναι απλώς χειρότερος· είναι άλλης τάξης γεγονός.", "This means that each extra unit is not 'a little stronger'. A magnitude six earthquake causes vibrations with ten times the amplitude of a magnitude five and releases about thirty times more energy. From five to seven, the energy is multiplied by about a thousand. That's why a magnitude seven earthquake isn't simply worse; it is an event of a different order."),
  L("Σεισμολόγος", "f", "Υπάρχει και μια μικρή παρεξήγηση. Οι σεισμολόγοι σήμερα, για τους μεγάλους σεισμούς, δεν χρησιμοποιούν πια την αρχική κλίμακα του Ρίχτερ, αλλά το λεγόμενο «μέγεθος σεισμικής ροπής», που υπολογίζεται από το μέγεθος του ρήγματος και τη μετατόπισή του. Τα νούμερα είναι παρόμοια, οπότε τα μέσα ενημέρωσης συνεχίζουν να λένε «Ρίχτερ».", "There's also a small misunderstanding. Seismologists today no longer use Richter's original scale for large earthquakes, but the so-called 'moment magnitude', which is calculated from the size of the fault and how far it slipped. The numbers are similar, so the media keep saying 'Richter'."),
  L("Σεισμολόγος", "f", "Και κάτι τελευταίο: το μέγεθος δεν λέει πόση ζημιά θα γίνει. Αυτό εξαρτάται από το βάθος, την απόσταση, το έδαφος και, πάνω απ' όλα, από το πώς είναι χτισμένα τα σπίτια μας.", "And one last thing: magnitude doesn't tell you how much damage there will be. That depends on depth, distance, the ground and, above all, on how our houses are built."),
 ],
 "questions": [
  Q("Γιατί η κλίμακα του Ρίχτερ ήταν επανάσταση;", ["Γιατί προέβλεπε τους σεισμούς", "Γιατί έδινε στον σεισμό έναν αριθμό ανεξάρτητο από το πώς τον ένιωσε ο καθένας", "Γιατί μετρούσε τις ζημιές", "Γιατί ήταν η πρώτη κλίμακα με δώδεκα βαθμούς"], 1, "για πρώτη φορά έδινε στον σεισμό έναν αριθμό, ανεξάρτητο από το πόσο τον ένιωσε ο καθένας"),
  Q("Πόση περισσότερη ενέργεια απελευθερώνει ένας σεισμός έξι βαθμών σε σχέση με έναν πέντε βαθμών;", ["Διπλάσια", "Περίπου τριάντα φορές περισσότερη", "Δέκα φορές λιγότερη", "Περίπου χίλιες φορές περισσότερη"], 1, "απελευθερώνει περίπου τριάντα φορές περισσότερη ενέργεια"),
  Q("Τι χρησιμοποιούν σήμερα οι σεισμολόγοι για τους μεγάλους σεισμούς;", ["Την κλίμακα Μερκάλι", "Το μέγεθος σεισμικής ροπής", "Την αρχική κλίμακα του Ρίχτερ", "Τις μαρτυρίες των κατοίκων"], 1, "το λεγόμενο «μέγεθος σεισμικής ροπής»"),
  Q("Από τι εξαρτάται, πάνω απ' όλα, η ζημιά;", ["Από την ώρα του σεισμού", "Από το πώς είναι χτισμένα τα σπίτια", "Από το μέγεθος μόνο", "Από τον καιρό"], 1, "πάνω απ' όλα, από το πώς είναι χτισμένα τα σπίτια μας"),
 ],
 "gloss": {"λογαριθμική": "λογαριθμικός — logarithmic", "δονήσεις": "δόνηση — vibration, tremor", "δεκαπλάσιο": "δεκαπλάσιος — tenfold", "εύρος": "εύρος — amplitude, range", "απελευθερώνει": "απελευθερώνω — to release", "ροπής": "ροπή — moment (physics), tendency", "ρήγματος": "ρήγμα — fault, rift", "μετατόπισή": "μετατόπιση — displacement, slip"},
})
ITEMS.append({
 "id": "l204-c1-int-zones-oras", "title": "Πώς απέκτησε ο κόσμος ζώνες ώρας", "title_en": "How railways gave the world time zones", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με έναν ιστορικό της τεχνολογίας σε μια εκπομπή για την ιστορία των καθημερινών πραγμάτων.",
 "script": [
  L("Δημοσιογράφος", "f", "Είναι αλήθεια ότι κάποτε κάθε πόλη είχε τη δική της ώρα;", "Is it true that once every town had its own time?"),
  L("Ιστορικός", "m", "Απολύτως. Για αιώνες η ώρα οριζόταν από τον ήλιο: μεσημέρι ήταν η στιγμή που ο ήλιος βρισκόταν στο ψηλότερο σημείο του. Επειδή η Γη γυρίζει, αυτή η στιγμή διαφέρει από τόπο σε τόπο. Δύο πόλεις με απόσταση μερικών εκατοντάδων χιλιομέτρων από την ανατολή προς τη δύση μπορούσαν να απέχουν αρκετά λεπτά. Κανείς δεν ενοχλούνταν, αφού κανείς δεν ταξίδευε τόσο γρήγορα ώστε να το καταλάβει.", "Absolutely. For centuries time was set by the sun: noon was the moment the sun was at its highest point. Because the Earth rotates, that moment differs from place to place. Two towns a few hundred kilometres apart from east to west could be several minutes apart. Nobody was bothered, since nobody travelled fast enough to notice."),
  L("Δημοσιογράφος", "f", "Και τότε ήρθαν οι σιδηρόδρομοι.", "And then the railways came."),
  L("Ιστορικός", "m", "Ακριβώς. Με τα τρένα, οι τοπικές ώρες έγιναν πονοκέφαλος: πώς να τυπώσεις ένα δρομολόγιο όταν κάθε σταθμός έχει άλλη ώρα; Οι βρετανικοί σιδηρόδρομοι υιοθέτησαν ενιαία ώρα ήδη από τη δεκαετία του 1840, και στις Ηνωμένες Πολιτείες οι σιδηροδρομικές εταιρείες χώρισαν τη χώρα σε ζώνες το 1883. Έναν χρόνο αργότερα, μια διεθνής διάσκεψη στην Ουάσιγκτον επέλεξε τον μεσημβρινό του Γκρίνουιτς ως αφετηρία για όλο τον κόσμο.", "Exactly. With trains, local times became a headache: how do you print a timetable when every station has a different time? British railways adopted a single time as early as the 1840s, and in the United States the railway companies divided the country into zones in 1883. A year later, an international conference in Washington chose the Greenwich meridian as the starting point for the whole world."),
  L("Δημοσιογράφος", "f", "Και η Ελλάδα;", "And Greece?"),
  L("Ιστορικός", "m", "Η Ελλάδα κράτησε για αρκετό καιρό τη μέση ώρα της Αθήνας και πέρασε στην ώρα Ανατολικής Ευρώπης, δύο ώρες μπροστά από το Γκρίνουιτς, το 1916, αν δεν κάνω λάθος. Το ενδιαφέρον είναι ότι σήμερα η ώρα δεν ορίζεται πια από τον ήλιο ούτε καν από τη Γη, αλλά από ατομικά ρολόγια. Η ώρα έπαψε να είναι φυσικό φαινόμενο και έγινε κοινωνική συμφωνία.", "Greece kept Athens mean time for quite a while and switched to Eastern European Time, two hours ahead of Greenwich, in 1916, if I'm not mistaken. What's interesting is that today time is no longer set by the sun or even by the Earth, but by atomic clocks. Time stopped being a natural phenomenon and became a social agreement."),
 ],
 "questions": [
  Q("Πώς οριζόταν η ώρα για αιώνες;", ["Με εκκλησιαστικές καμπάνες", "Από τον ήλιο, με το μεσημέρι στο ψηλότερο σημείο του", "Με ρολόγια από την πρωτεύουσα", "Από τα άστρα"], 1, "μεσημέρι ήταν η στιγμή που ο ήλιος βρισκόταν στο ψηλότερο σημείο του"),
  Q("Γιατί οι τοπικές ώρες δεν ενοχλούσαν κανέναν;", ["Γιατί δεν υπήρχαν ρολόγια", "Γιατί κανείς δεν ταξίδευε τόσο γρήγορα ώστε να το καταλάβει", "Γιατί όλες οι πόλεις είχαν την ίδια ώρα", "Γιατί το απαγόρευε ο νόμος"], 1, "κανείς δεν ταξίδευε τόσο γρήγορα ώστε να το καταλάβει"),
  Q("Τι αποφάσισε η διεθνής διάσκεψη στην Ουάσιγκτον;", ["Να καταργηθούν οι ζώνες ώρας", "Να γίνει ο μεσημβρινός του Γκρίνουιτς αφετηρία για όλο τον κόσμο", "Να αλλάζει η ώρα δύο φορές τον χρόνο", "Να μπουν ατομικά ρολόγια στους σταθμούς"], 1, "επέλεξε τον μεσημβρινό του Γκρίνουιτς ως αφετηρία"),
  Q("Τι εννοεί ο ιστορικός όταν λέει ότι η ώρα έγινε «κοινωνική συμφωνία»;", ["Ότι την ψηφίζουν οι πολίτες", "Ότι δεν ορίζεται πια από τη φύση αλλά από ανθρώπινες αποφάσεις και ατομικά ρολόγια", "Ότι κάθε χώρα έχει την ίδια ώρα", "Ότι κανείς δεν τη σέβεται"], 1, "Η ώρα έπαψε να είναι φυσικό φαινόμενο και έγινε κοινωνική συμφωνία"),
 ],
 "gloss": {"σιδηρόδρομοι": "σιδηρόδρομος — railway", "δρομολόγιο": "δρομολόγιο — timetable, route", "υιοθέτησαν": "υιοθετώ — to adopt", "ενιαία": "ενιαίος — single, uniform", "διάσκεψη": "διάσκεψη — conference", "μεσημβρινό": "μεσημβρινός — meridian", "αφετηρία": "αφετηρία — starting point", "ατομικά ρολόγια": "ατομικό ρολόι — atomic clock"},
})

rnd = random.Random(204)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-204.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
