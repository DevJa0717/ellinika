# Source for library/listening/listening-213.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l213.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l213-news-tsimpouria", "title": "Οδηγίες για τα τσιμπούρια μετά από έναν ήπιο χειμώνα", "title_en": "Advice on ticks after a mild winter", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο ραδιόφωνο με οδηγίες των υγειονομικών αρχών προς τους πολίτες.",
 "script": [
  L("Εκφωνήτρια", "f", "Οι υγειονομικές αρχές καλούν όσους κάνουν πεζοπορία ή δουλεύουν στην ύπαιθρο να προσέχουν τα τσιμπούρια, που φέτος εμφανίστηκαν νωρίτερα από ό,τι συνήθως εξαιτίας του ήπιου χειμώνα. Τα τσιμπούρια είναι μικρά παράσιτα που κρύβονται στα ψηλά χόρτα και στους θάμνους και κολλάνε σε ανθρώπους και ζώα.", "The health authorities are calling on those who go hiking or work outdoors to watch out for ticks, which this year appeared earlier than usual because of the mild winter. Ticks are small parasites that hide in tall grass and bushes and attach themselves to people and animals."),
  L("Εκφωνήτρια", "f", "Συνιστάται να φοράμε ανοιχτόχρωμα ρούχα με μακριά μανίκια και μακριά παντελόνια, ώστε να φαίνονται εύκολα, και να χρησιμοποιούμε εντομοαπωθητικό. Μετά από κάθε βόλτα στη φύση πρέπει να ελέγχουμε προσεκτικά το σώμα μας, ιδιαίτερα πίσω από τα αυτιά, στις μασχάλες και πίσω από τα γόνατα, καθώς και τα κατοικίδιά μας.", "It is recommended that we wear light-coloured clothes with long sleeves and long trousers, so that they can be seen easily, and use insect repellent. After every walk in nature we should check our bodies carefully, especially behind the ears, in the armpits and behind the knees, as well as our pets."),
  L("Εκφωνήτρια", "f", "Αν βρούμε τσιμπούρι, δεν πρέπει να το πιέζουμε ούτε να του βάζουμε λάδι ή οινόπνευμα. Το σωστό είναι να το πιάσουμε όσο πιο κοντά στο δέρμα γίνεται με μια λεπτή τσιμπίδα και να το τραβήξουμε σταθερά προς τα έξω. Αν τις επόμενες εβδομάδες εμφανιστεί πυρετός ή κοκκίνισμα, πρέπει να επισκεφτούμε γιατρό.", "If we find a tick, we must not squeeze it or put oil or alcohol on it. The right thing is to grip it as close to the skin as possible with fine tweezers and pull it steadily outwards. If fever or redness appears in the following weeks, we should see a doctor."),
 ],
 "questions": [
  Q("Γιατί εμφανίστηκαν φέτος νωρίτερα τα τσιμπούρια;", ["Εξαιτίας των πυρκαγιών", "Εξαιτίας του ήπιου χειμώνα", "Εξαιτίας των βροχών", "Επειδή αυξήθηκαν τα αδέσποτα"], 1, "εμφανίστηκαν νωρίτερα από ό,τι συνήθως εξαιτίας του ήπιου χειμώνα"),
  Q("Γιατί συνιστώνται ανοιχτόχρωμα ρούχα;", ["Για να μη ζεσταινόμαστε", "Για να φαίνονται εύκολα τα τσιμπούρια", "Για να μας βλέπουν οι οδηγοί", "Γιατί απωθούν τα έντομα"], 1, "ώστε να φαίνονται εύκολα"),
  Q("Τι ΔΕΝ πρέπει να κάνουμε αν βρούμε τσιμπούρι;", ["Να το πιάσουμε με τσιμπίδα", "Να το πιέσουμε ή να του βάλουμε λάδι", "Να το τραβήξουμε σταθερά", "Να επισκεφτούμε γιατρό αν έχουμε πυρετό"], 1, "δεν πρέπει να το πιέζουμε ούτε να του βάζουμε λάδι ή οινόπνευμα"),
  Q("Πότε πρέπει να επισκεφτούμε γιατρό;", ["Αμέσως μόλις βρούμε τσιμπούρι", "Αν εμφανιστεί πυρετός ή κοκκίνισμα τις επόμενες εβδομάδες", "Μόνο αν μας τσιμπήσουν πολλά", "Μετά από κάθε πεζοπορία"], 1, "Αν τις επόμενες εβδομάδες εμφανιστεί πυρετός ή κοκκίνισμα"),
 ],
 "gloss": {"τσιμπούρια": "τσιμπούρι — tick", "ύπαιθρο": "ύπαιθρος — countryside, outdoors", "ήπιου": "ήπιος — mild", "θάμνους": "θάμνος — bush, shrub", "εντομοαπωθητικό": "εντομοαπωθητικό — insect repellent", "μασχάλες": "μασχάλη — armpit", "οινόπνευμα": "οινόπνευμα — (surgical) alcohol", "τσιμπίδα": "τσιμπίδα — tweezers"},
})
ITEMS.append({
 "id": "l213-dia-sygchroni-techni", "title": "Είναι τέχνη ένας σωρός από παπούτσια;", "title_en": "Is a pile of shoes art? Two friends at an exhibition", "type": "dialogue", "level": "B2",
 "context_el": "Δύο φίλοι επισκέπτονται μια έκθεση σύγχρονης τέχνης στην Αθήνα και συζητούν μπροστά σε ένα έργο.",
 "script": [
  L("Φώτης", "m", "Δηλαδή αυτό είναι το έργο; Ένας σωρός από παλιά παπούτσια στη μέση της αίθουσας; Νόμιζα ότι κάποιος τα ξέχασε εδώ.", "So that's the artwork? A pile of old shoes in the middle of the room? I thought someone had left them here."),
  L("Ζωή", "f", "Διάβασε την ταμπέλα. Η καλλιτέχνιδα μάζεψε χίλια ζευγάρια παπούτσια από ανθρώπους που μετανάστευσαν, και ο καθένας έγραψε μέσα στο παπούτσι πού πήγε και γιατί.", "Read the label. The artist collected a thousand pairs of shoes from people who emigrated, and each of them wrote inside the shoe where they went and why."),
  L("Φώτης", "m", "Εντάξει, η ιδέα είναι συγκινητική. Αλλά τέχνη για μένα σημαίνει να ξέρεις να ζωγραφίζεις ή να σκαλίζεις. Αυτό θα μπορούσε να το κάνει ο καθένας.", "OK, the idea is moving. But art for me means knowing how to paint or carve. Anyone could do this."),
  L("Ζωή", "f", "Ναι, αλλά δεν το έκανε ο καθένας. Της πήρε τρία χρόνια να βρει τους ανθρώπους και να ακούσει τις ιστορίες τους. Η τέχνη δεν είναι μόνο τεχνική· είναι και το ότι σε κάνει να σκεφτείς κάτι που δεν είχες σκεφτεί.", "Yes, but not just anyone did it. It took her three years to find the people and listen to their stories. Art isn't only technique; it's also that it makes you think of something you hadn't thought of."),
  L("Φώτης", "m", "Χμ. Η αλήθεια είναι ότι μου θύμισε τον παππού μου, που έφυγε για τη Γερμανία το '62 με ένα ζευγάρι παπούτσια κι ένα βαλιτσάκι.", "Hmm. The truth is it reminded me of my grandfather, who left for Germany in '62 with one pair of shoes and a little suitcase."),
  L("Ζωή", "f", "Βλέπεις; Αυτό ακριβώς ήθελε η καλλιτέχνιδα. Έλα, πάμε στην επόμενη αίθουσα. Εκεί έχει και πίνακες, να ησυχάσεις.", "You see? That's exactly what the artist wanted. Come on, let's go to the next room. There are paintings there too, so you can relax."),
 ],
 "questions": [
  Q("Τι νόμιζε στην αρχή ο Φώτης;", ["Ότι το έργο ήταν ακριβό", "Ότι κάποιος ξέχασε τα παπούτσια", "Ότι η έκθεση ήταν κλειστή", "Ότι τα παπούτσια ήταν για πούλημα"], 1, "Νόμιζα ότι κάποιος τα ξέχασε εδώ"),
  Q("Από ποιους μάζεψε η καλλιτέχνιδα τα παπούτσια;", ["Από καταστήματα", "Από ανθρώπους που μετανάστευσαν", "Από ένα εργοστάσιο", "Από φίλους της"], 1, "από ανθρώπους που μετανάστευσαν"),
  Q("Τι σημαίνει τέχνη για τον Φώτη;", ["Να σε κάνει να σκεφτείς", "Να ξέρεις να ζωγραφίζεις ή να σκαλίζεις", "Να είναι ακριβή", "Να είναι σε μουσείο"], 1, "τέχνη για μένα σημαίνει να ξέρεις να ζωγραφίζεις ή να σκαλίζεις"),
  Q("Γιατί τελικά το έργο άγγιξε τον Φώτη;", ["Του θύμισε τον παππού του που μετανάστευσε", "Του άρεσαν τα χρώματα", "Γνώριζε την καλλιτέχνιδα", "Είχε κι αυτός παλιά παπούτσια"], 0, "μου θύμισε τον παππού μου, που έφυγε για τη Γερμανία"),
 ],
 "gloss": {"σωρός": "σωρός — pile, heap", "ταμπέλα": "ταμπέλα — label, sign", "καλλιτέχνιδα": "καλλιτέχνιδα — (female) artist", "μετανάστευσαν": "μεταναστεύω — to emigrate", "συγκινητική": "συγκινητικός — moving, touching", "σκαλίζεις": "σκαλίζω — to carve", "βαλιτσάκι": "βαλιτσάκι — little suitcase", "ησυχάσεις": "ησυχάζω — to calm down, relax"},
})
ITEMS.append({
 "id": "l213-c1-mono-giati-epta-meres", "title": "Γιατί η εβδομάδα έχει εφτά μέρες;", "title_en": "Why does the week have seven days?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ομιλία για την ιστορία του ημερολογίου σε έναν κύκλο εκλαϊκευμένων διαλέξεων.",
 "script": [
  L("Ομιλητής", "m", "Η μέρα, ο μήνας και το έτος έχουν μια αστρονομική βάση: την περιστροφή της Γης, τον κύκλο της Σελήνης, την περιφορά γύρω από τον Ήλιο. Η εβδομάδα, όμως, δεν αντιστοιχεί σε κανένα φυσικό φαινόμενο. Γιατί τότε μετράμε τον χρόνο σε ομάδες των εφτά ημερών;", "The day, the month and the year have an astronomical basis: the rotation of the Earth, the cycle of the Moon, the orbit around the Sun. The week, however, corresponds to no natural phenomenon. Why then do we count time in groups of seven days?"),
  L("Ομιλητής", "m", "Μια εξήγηση συνδέεται με τους αρχαίους αστρονόμους της Μεσοποταμίας, που παρατηρούσαν εφτά ουράνια σώματα να κινούνται ανάμεσα στα άστρα: τον Ήλιο, τη Σελήνη και πέντε πλανήτες ορατούς με γυμνό μάτι. Ο αριθμός εφτά απέκτησε έτσι ιερό χαρακτήρα. Παράλληλα, η εβραϊκή παράδοση καθιέρωσε έναν κύκλο έξι ημερών εργασίας και μιας ημέρας ανάπαυσης, το Σάββατο.", "One explanation is linked to the ancient astronomers of Mesopotamia, who observed seven celestial bodies moving among the stars: the Sun, the Moon and five planets visible to the naked eye. The number seven thus acquired a sacred character. In parallel, the Jewish tradition established a cycle of six working days and one day of rest, the Sabbath."),
  L("Ομιλητής", "m", "Στη Ρωμαϊκή Αυτοκρατορία οι δύο παραδόσεις συναντήθηκαν, και οι μέρες πήραν τα ονόματα των εφτά «πλανητών», όπως φαίνεται ακόμα στις ρομανικές γλώσσες: η Δευτέρα είναι η μέρα της Σελήνης, η Τρίτη του Άρη. Τα ελληνικά ακολούθησαν άλλον δρόμο: Δευτέρα, Τρίτη, Τετάρτη και Πέμπτη είναι απλώς αριθμοί, η Παρασκευή είναι η μέρα της «προετοιμασίας» για το Σάββατο, και η Κυριακή η «ημέρα του Κυρίου». Το 321 ο Μέγας Κωνσταντίνος όρισε την Κυριακή ως ημέρα ανάπαυσης.", "In the Roman Empire the two traditions met, and the days took the names of the seven 'planets', as can still be seen in the Romance languages: Monday is the day of the Moon, Tuesday of Mars. Greek took another path: Δευτέρα, Τρίτη, Τετάρτη and Πέμπτη are simply numbers, Παρασκευή is the day of 'preparation' for the Sabbath, and Κυριακή the 'Lord's day'. In 321 Constantine the Great established Sunday as a day of rest."),
  L("Ομιλητής", "m", "Η εβδομάδα αποδείχθηκε εντυπωσιακά ανθεκτική. Η Γαλλική Επανάσταση προσπάθησε να την αντικαταστήσει με μια «δεκάδα» δέκα ημερών, και η Σοβιετική Ένωση πειραματίστηκε για λίγα χρόνια με εβδομάδες πέντε και έξι ημερών. Και τα δύο εγχειρήματα εγκαταλείφθηκαν· ίσως γιατί, εκτός από τη θρησκεία και τη συνήθεια, εννιά συνεχόμενες μέρες δουλειάς πριν από ένα ρεπό δεν ενθουσίασαν κανέναν.", "The week proved remarkably resilient. The French Revolution tried to replace it with a ten-day 'décade', and the Soviet Union experimented for a few years with five- and six-day weeks. Both ventures were abandoned; perhaps because, apart from religion and habit, nine consecutive working days before a day off thrilled nobody."),
 ],
 "questions": [
  Q("Σε τι διαφέρει η εβδομάδα από τη μέρα, τον μήνα και το έτος;", ["Είναι πιο σύντομη", "Δεν αντιστοιχεί σε κανένα φυσικό φαινόμενο", "Ορίστηκε από τους Έλληνες", "Αλλάζει κάθε χρόνο"], 1, "Η εβδομάδα, όμως, δεν αντιστοιχεί σε κανένα φυσικό φαινόμενο"),
  Q("Ποια εφτά ουράνια σώματα παρατηρούσαν οι αστρονόμοι της Μεσοποταμίας;", ["Εφτά φωτεινά άστρα", "Τον Ήλιο, τη Σελήνη και πέντε ορατούς πλανήτες", "Εφτά αστερισμούς", "Τη Γη και έξι πλανήτες"], 1, "τον Ήλιο, τη Σελήνη και πέντε πλανήτες ορατούς με γυμνό μάτι"),
  Q("Τι σημαίνει η λέξη «Παρασκευή», σύμφωνα με τον ομιλητή;", ["Η μέρα της Αφροδίτης", "Η μέρα της προετοιμασίας για το Σάββατο", "Η έκτη μέρα", "Η μέρα της αγοράς"], 1, "η Παρασκευή είναι η μέρα της «προετοιμασίας» για το Σάββατο"),
  Q("Τι απέγιναν οι προσπάθειες να αλλάξει η εβδομάδα;", ["Επικράτησαν στην Ευρώπη", "Εγκαταλείφθηκαν", "Ισχύουν ακόμα στη Γαλλία", "Δεν εφαρμόστηκαν ποτέ"], 1, "Και τα δύο εγχειρήματα εγκαταλείφθηκαν"),
 ],
 "gloss": {"περιστροφή": "περιστροφή — rotation", "περιφορά": "περιφορά — orbit, revolution", "ουράνια": "ουράνιος — celestial", "ανάπαυσης": "ανάπαυση — rest", "ρομανικές": "ρομανικός — Romance (languages)", "ανθεκτική": "ανθεκτικός — resilient, durable", "εγχειρήματα": "εγχείρημα — venture, undertaking", "συνεχόμενες": "συνεχόμενος — consecutive", "ρεπό": "ρεπό — day off"},
})
ITEMS.append({
 "id": "l213-c1-int-istoria-chartografias", "title": "Χάρτες που λένε ψέματα: μια ιστορικός της χαρτογραφίας", "title_en": "Maps that lie: a historian of cartography", "type": "interview", "level": "C1",
 "context_el": "Ακούτε μια συνέντευξη σε πολιτιστική εκπομπή με μια ιστορικό που μελετά τους παλιούς χάρτες.",
 "script": [
  L("Δημοσιογράφος", "m", "Λέτε ότι κάθε χάρτης λέει και λίγα ψέματα. Γιατί;", "You say every map tells a few lies. Why?"),
  L("Ιστορικός", "f", "Γιατί είναι αδύνατον να απλώσεις μια σφαίρα πάνω σε ένα επίπεδο χαρτί χωρίς να την παραμορφώσεις. Κάθε χαρτογράφος διαλέγει τι θα θυσιάσει: τις αποστάσεις, τα σχήματα ή τις επιφάνειες. Η πιο γνωστή περίπτωση είναι η προβολή του Μερκάτορα, του 1569. Ήταν σχεδιασμένη για ναυτικούς, γιατί μια σταθερή πορεία πυξίδας γίνεται ευθεία γραμμή στον χάρτη. Το τίμημα είναι ότι οι περιοχές κοντά στους πόλους φαίνονται τεράστιες: η Γροιλανδία μοιάζει σχεδόν όσο η Αφρική, ενώ στην πραγματικότητα η Αφρική είναι περίπου δεκατέσσερις φορές μεγαλύτερη.", "Because it's impossible to spread a sphere over a flat sheet of paper without distorting it. Every cartographer chooses what to sacrifice: distances, shapes or areas. The best-known case is the Mercator projection of 1569. It was designed for sailors, because a constant compass course becomes a straight line on the map. The price is that areas near the poles look huge: Greenland looks almost as big as Africa, whereas in reality Africa is about fourteen times larger."),
  L("Δημοσιογράφος", "m", "Και πριν από τον Μερκάτορα;", "And before Mercator?"),
  L("Ιστορικός", "f", "Τον Μεσαίωνα οι ναυτικοί της Μεσογείου χρησιμοποιούσαν τους λεγόμενους πορτολανούς, χάρτες με εκπληκτικά ακριβείς ακτογραμμές, γεμάτους με γραμμές που ξεκινούν από ανεμολόγια. Ο παλαιότερος που σώζεται χρονολογείται γύρω στο 1275. Το εσωτερικό των ηπείρων, αντίθετα, συχνά έμενε σχεδόν κενό· τους ναυτικούς τους ενδιέφεραν τα λιμάνια, όχι τα βουνά.", "In the Middle Ages Mediterranean sailors used so-called portolan charts, maps with astonishingly accurate coastlines, full of lines radiating from compass roses. The oldest surviving one dates to around 1275. The interior of the continents, by contrast, was often left almost empty; sailors cared about harbours, not mountains."),
  L("Δημοσιογράφος", "m", "Υπάρχει κάποιος ελληνικός χάρτης που σας συγκινεί ιδιαίτερα;", "Is there a Greek map that moves you in particular?"),
  L("Ιστορικός", "f", "Η «Χάρτα» του Ρήγα Βελεστινλή, που τυπώθηκε στη Βιέννη το 1797 σε δώδεκα φύλλα. Δεν είναι μόνο γεωγραφικός χάρτης· είναι πολιτικό μανιφέστο. Γεμίζει τον χώρο με αρχαίες πόλεις, νομίσματα και μάχες, για να θυμίσει στους υπόδουλους λαούς της Βαλκανικής ένα κοινό παρελθόν και να τους εμπνεύσει. Αυτό είναι το πιο ενδιαφέρον με τους χάρτες: δεν δείχνουν απλώς πού βρίσκεται κάτι, αλλά και πώς θέλει κάποιος να δούμε τον κόσμο.", "Rigas Velestinlis's 'Charta', printed in Vienna in 1797 in twelve sheets. It isn't just a geographical map; it's a political manifesto. It fills the space with ancient cities, coins and battles, to remind the subject peoples of the Balkans of a common past and to inspire them. That's the most interesting thing about maps: they don't simply show where something is, but also how someone wants us to see the world."),
 ],
 "questions": [
  Q("Γιατί κάθε χάρτης «λέει ψέματα», σύμφωνα με την ιστορικό;", ["Γιατί οι χαρτογράφοι κάνουν λάθη", "Γιατί είναι αδύνατον να απλώσεις μια σφαίρα σε επίπεδο χωρίς παραμόρφωση", "Γιατί τα σύνορα αλλάζουν", "Γιατί οι χάρτες είναι πάντα παλιοί"], 1, "είναι αδύνατον να απλώσεις μια σφαίρα πάνω σε ένα επίπεδο χαρτί χωρίς να την παραμορφώσεις"),
  Q("Γιατί η προβολή του Μερκάτορα ήταν χρήσιμη στους ναυτικούς;", ["Γιατί έδειχνε σωστά τις επιφάνειες", "Γιατί μια σταθερή πορεία πυξίδας γίνεται ευθεία γραμμή", "Γιατί ήταν μικρή και φορητή", "Γιατί έδειχνε τα βάθη της θάλασσας"], 1, "μια σταθερή πορεία πυξίδας γίνεται ευθεία γραμμή στον χάρτη"),
  Q("Τι χαρακτήριζε τους πορτολανούς;", ["Έδειχναν με ακρίβεια τα βουνά", "Είχαν ακριβείς ακτογραμμές αλλά συχνά κενό εσωτερικό", "Ήταν τυπωμένοι στη Βιέννη", "Χρησιμοποιούσαν την προβολή του Μερκάτορα"], 1, "χάρτες με εκπληκτικά ακριβείς ακτογραμμές ... Το εσωτερικό των ηπείρων, αντίθετα, συχνά έμενε σχεδόν κενό"),
  Q("Ποιος ήταν ο σκοπός της «Χάρτας» του Ρήγα;", ["Να βοηθήσει τους εμπόρους", "Να θυμίσει στους υπόδουλους λαούς ένα κοινό παρελθόν και να τους εμπνεύσει", "Να δείξει τους δρόμους της Βιέννης", "Να διορθώσει τον χάρτη του Μερκάτορα"], 1, "για να θυμίσει στους υπόδουλους λαούς της Βαλκανικής ένα κοινό παρελθόν και να τους εμπνεύσει"),
 ],
 "gloss": {"σφαίρα": "σφαίρα — sphere", "επίπεδο": "επίπεδος — flat", "παραμορφώσεις": "παραμορφώνω — to distort", "προβολή": "προβολή — projection", "τίμημα": "τίμημα — price, cost", "πορτολανούς": "πορτολανός — portolan chart", "ακτογραμμές": "ακτογραμμή — coastline", "ανεμολόγια": "ανεμολόγιο — compass rose, wind rose", "υπόδουλους": "υπόδουλος — subjugated, enslaved", "μανιφέστο": "μανιφέστο — manifesto"},
})
rnd = random.Random(213)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-213.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
