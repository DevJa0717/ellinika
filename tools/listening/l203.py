# Source for library/listening/listening-203.json: seven more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l203.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l203-ann-titan-arum", "title": "Ανθίζει το «λουλούδι-πτώμα»", "title_en": "The giant 'corpse flower' is in bloom", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός βοτανικού κήπου.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί επισκέπτες, έχουμε μια σπάνια είδηση: το γιγάντιο άρον του τροπικού θερμοκηπίου, το φυτό που είναι γνωστό και ως «λουλούδι-πτώμα», άρχισε σήμερα το πρωί να ανθίζει. Το φυτό ανθίζει μόνο κάθε λίγα χρόνια, και το άνθος του μένει ανοιχτό μόνο μία με δύο μέρες. Το δικό μας ξεπερνά ήδη τα δύο μέτρα.", "Dear visitors, we have rare news: the giant arum in the tropical greenhouse, the plant also known as the 'corpse flower', began to bloom this morning. The plant flowers only every few years, and its bloom stays open for only one or two days. Ours already exceeds two metres."),
  L("Εκφωνήτρια", "f", "Σας προειδοποιούμε ότι το άνθος βγάζει μια πολύ έντονη και δυσάρεστη μυρωδιά, σαν χαλασμένο κρέας. Με αυτήν προσελκύει τα έντομα που το επικονιάζουν. Για τον λόγο αυτόν, η είσοδος στο θερμοκήπιο θα γίνεται σε ομάδες των δεκαπέντε ατόμων, για πέντε λεπτά η καθεμιά.", "We warn you that the flower gives off a very strong and unpleasant smell, like rotten meat. With it, it attracts the insects that pollinate it. For this reason, entry to the greenhouse will be in groups of fifteen people, for five minutes each."),
  L("Εκφωνήτρια", "f", "Απόψε ο κήπος θα μείνει ανοιχτός ως τα μεσάνυχτα, γιατί η μυρωδιά γίνεται πιο έντονη τη νύχτα. Παρακαλούμε να μη χρησιμοποιείτε φλας στις φωτογραφίες σας.", "Tonight the garden will stay open until midnight, because the smell becomes stronger at night. Please do not use flash in your photographs."),
 ],
 "questions": [
  Q("Πόσο συχνά ανθίζει αυτό το φυτό;", ["Κάθε άνοιξη", "Κάθε λίγα χρόνια", "Κάθε μήνα", "Μία φορά στη ζωή του"], 1, "ανθίζει μόνο κάθε λίγα χρόνια"),
  Q("Γιατί το άνθος μυρίζει άσχημα;", ["Γιατί είναι άρρωστο", "Για να προσελκύει τα έντομα που το επικονιάζουν", "Για να διώχνει τα ζώα", "Λόγω του θερμοκηπίου"], 1, "Με αυτήν προσελκύει τα έντομα που το επικονιάζουν"),
  Q("Γιατί ο κήπος θα μείνει ανοιχτός ως τα μεσάνυχτα;", ["Λόγω της ζέστης", "Γιατί η μυρωδιά γίνεται πιο έντονη τη νύχτα", "Για μια συναυλία", "Γιατί έρχεται τηλεόραση"], 1, "η μυρωδιά γίνεται πιο έντονη τη νύχτα"),
 ],
 "gloss": {"γιγάντιο": "γιγάντιος — giant", "άρον": "άρον — arum (plant)", "ανθίζει": "ανθίζω — to bloom", "άνθος": "άνθος — flower, bloom", "δυσάρεστη": "δυσάρεστος — unpleasant", "προσελκύει": "προσελκύω — to attract", "επικονιάζουν": "επικονιάζω — to pollinate"},
})
ITEMS.append({
 "id": "l203-vm-chelona-geitonas", "title": "Η χελώνα σας είναι στον κήπο μου", "title_en": "Your tortoise is in my garden", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από μια γειτόνισσα.",
 "script": [
  L("Γειτόνισσα", "f", "Καλησπέρα, κύριε Παύλο, η Ευτυχία είμαι, από το σπίτι με τις λεμονιές. Μάλλον ψάχνετε τη χελώνα σας. Τη βρήκα σήμερα το πρωί στο μποστάνι μου, να τρώει με μεγάλη όρεξη τα μαρούλια μου. Δεν πειράζει, μου έφυγε το θυμάρι από τα γέλια.", "Good evening, Mr Pavlos, it's Eftychia, from the house with the lemon trees. You're probably looking for your tortoise. I found it this morning in my vegetable patch, eating my lettuces with a great appetite. Never mind, I couldn't stop laughing."),
  L("Γειτόνισσα", "f", "Νομίζω ότι πέρασε από ένα λάκκο κάτω από τον φράχτη, δίπλα στην αποθήκη. Οι χελώνες σκάβουν πολύ καλά, ξέρετε. Ο άντρας μου λέει ότι αν θάψετε ένα συρματόπλεγμα είκοσι-τριάντα πόντους μέσα στο χώμα, δεν θα ξαναβγεί.", "I think it got through a hole under the fence, next to the shed. Tortoises dig very well, you know. My husband says that if you bury some wire mesh twenty or thirty centimetres into the soil, it won't get out again."),
  L("Γειτόνισσα", "f", "Την έχω βάλει σε ένα κουτί στη σκιά, με λίγο νερό. Περάστε να την πάρετε όποτε μπορείτε, είμαι σπίτι ως τις οχτώ.", "I've put it in a box in the shade, with a little water. Come by and pick it up whenever you can; I'm home until eight."),
 ],
 "questions": [
  Q("Πού βρήκε η Ευτυχία τη χελώνα;", ["Στον δρόμο", "Στο μποστάνι της, να τρώει μαρούλια", "Στην αποθήκη", "Στο σαλόνι της"], 1, "Τη βρήκα σήμερα το πρωί στο μποστάνι μου"),
  Q("Πώς πιστεύει ότι βγήκε η χελώνα;", ["Από την πόρτα του κήπου", "Από ένα λάκκο κάτω από τον φράχτη", "Την πήρε ένα παιδί", "Πήδηξε τον φράχτη"], 1, "πέρασε από ένα λάκκο κάτω από τον φράχτη"),
  Q("Τι προτείνει ο άντρας της;", ["Να μπει η χελώνα σε κλουβί", "Να θαφτεί συρματόπλεγμα μέσα στο χώμα", "Να ψηλώσει ο φράχτης", "Να δοθεί η χελώνα σε ένα πάρκο"], 1, "αν θάψετε ένα συρματόπλεγμα είκοσι-τριάντα πόντους μέσα στο χώμα"),
 ],
 "gloss": {"μποστάνι": "μποστάνι — vegetable patch", "μαρούλια": "μαρούλι — lettuce", "λάκκο": "λάκκος — hole, pit", "φράχτη": "φράχτης — fence", "σκάβουν": "σκάβω — to dig", "θάψετε": "θάβω — to bury", "συρματόπλεγμα": "συρματόπλεγμα — wire mesh"},
})
ITEMS.append({
 "id": "l203-int-neon-epigrafes", "title": "Ο τεχνίτης των επιγραφών νέον", "title_en": "The last neon sign maker in town", "type": "interview", "level": "B2",
 "context_el": "Συνέντευξη με έναν τεχνίτη που φτιάχνει φωτεινές επιγραφές νέον.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς φτιάχνεται μια επιγραφή νέον;", "How is a neon sign made?"),
  L("Τεχνίτης", "m", "Με το χέρι, ένα ένα τα γράμματα. Ζεσταίνω έναν γυάλινο σωλήνα πάνω σε μια φλόγα, μέχρι να μαλακώσει, και τον λυγίζω πάνω σε ένα σχέδιο σε φυσικό μέγεθος. Αν βιαστώ, ο σωλήνας σπάει ή στραβώνει. Μετά βάζω ηλεκτρόδια στις άκρες, βγάζω τον αέρα και γεμίζω τον σωλήνα με αέριο.", "By hand, letter by letter. I heat a glass tube over a flame until it softens, and I bend it over a life-size drawing. If I rush, the tube breaks or bends crooked. Then I put electrodes at the ends, pump out the air and fill the tube with gas."),
  L("Δημοσιογράφος", "f", "Και τα χρώματα από πού έρχονται;", "And where do the colours come from?"),
  L("Τεχνίτης", "m", "Το ίδιο το νέον δίνει μόνο ένα κοκκινοπορτοκαλί φως. Για τα άλλα χρώματα χρησιμοποιούμε κυρίως αργό και ειδικές επιστρώσεις στο εσωτερικό του σωλήνα, ή χρωματιστό γυαλί. Ο κόσμος λέει «νέον» για όλες, αλλά στην πραγματικότητα οι περισσότερες δεν έχουν καθόλου νέον.", "Neon itself gives only a red-orange light. For the other colours we mainly use argon and special coatings on the inside of the tube, or coloured glass. People call them all 'neon', but in reality most of them don't contain any neon at all."),
  L("Δημοσιογράφος", "f", "Οι φτηνές επιγραφές LED δεν σας έχουν κλείσει τη δουλειά;", "Haven't cheap LED signs put you out of business?"),
  L("Τεχνίτης", "m", "Σχεδόν. Τώρα όμως έρχονται νέοι άνθρωποι που θέλουν μια επιγραφή για το μπαρ τους ή για το σαλόνι τους, ακριβώς επειδή είναι χειροποίητη και ζεστή. Το φως του νέον έχει κάτι ζωντανό, κάτι που το LED δεν το έχει.", "Almost. But now young people come who want a sign for their bar or their living room, precisely because it's handmade and warm. Neon light has something alive about it, something LED doesn't have."),
 ],
 "questions": [
  Q("Τι συμβαίνει αν ο τεχνίτης βιαστεί;", ["Το αέριο φεύγει", "Ο σωλήνας σπάει ή στραβώνει", "Το χρώμα αλλάζει", "Η φλόγα σβήνει"], 1, "ο σωλήνας σπάει ή στραβώνει"),
  Q("Τι χρώμα δίνει το ίδιο το νέον;", ["Μπλε", "Πράσινο", "Κοκκινοπορτοκαλί", "Λευκό"], 2, "Το ίδιο το νέον δίνει μόνο ένα κοκκινοπορτοκαλί φως"),
  Q("Γιατί έρχονται τώρα νέοι πελάτες;", ["Γιατί οι επιγραφές νέον είναι φτηνότερες", "Γιατί θέλουν κάτι χειροποίητο και ζεστό", "Γιατί το LED απαγορεύτηκε", "Γιατί τις χρειάζονται για ταινίες"], 1, "ακριβώς επειδή είναι χειροποίητη και ζεστή"),
 ],
 "gloss": {"επιγραφές": "επιγραφή — sign", "σωλήνα": "σωλήνας — tube", "μαλακώσει": "μαλακώνω — to soften", "λυγίζω": "λυγίζω — to bend", "στραβώνει": "στραβώνω — to bend crooked", "ηλεκτρόδια": "ηλεκτρόδιο — electrode", "αργό": "αργό — argon", "επιστρώσεις": "επίστρωση — coating", "χειροποίητη": "χειροποίητος — handmade"},
})
ITEMS.append({
 "id": "l203-mono-kotsyfas-mpalkoni", "title": "Ο κότσυφας στη γλάστρα μου", "title_en": "A blackbird nested in my balcony flowerpot", "type": "monologue", "level": "B2",
 "context_el": "Μια γυναίκα μιλάει σε μια ραδιοφωνική εκπομπή για τη φύση στην πόλη.",
 "script": [
  L("Ακροάτρια", "f", "Τον Απρίλιο ήθελα να φυτέψω ντομάτες στη μεγάλη γλάστρα του μπαλκονιού μου. Όταν βγήκα με το φτυαράκι, ένα μαύρο πουλί με κίτρινη μύτη πετάχτηκε μπροστά μου. Ήταν ένας κότσυφας, και μέσα στα ξερά φύλλα της γλάστρας υπήρχε μια φωλιά με τέσσερα γαλαζοπράσινα αυγά.", "In April I wanted to plant tomatoes in the big pot on my balcony. When I went out with the trowel, a black bird with a yellow beak shot out in front of me. It was a blackbird, and among the dry leaves in the pot there was a nest with four blue-green eggs."),
  L("Ακροάτρια", "f", "Οι ντομάτες περίμεναν. Για δύο εβδομάδες άνοιγα την μπαλκονόπορτα όσο πιο αθόρυβα μπορούσα και έπινα τον καφέ μου μέσα, πίσω από την κουρτίνα. Όταν βγήκαν τα μικρά, οι γονείς τους πηγαινοέρχονταν όλη μέρα με σκουλήκια στο στόμα.", "The tomatoes waited. For two weeks I opened the balcony door as quietly as I could and drank my coffee inside, behind the curtain. When the chicks hatched, their parents came and went all day with worms in their beaks."),
  L("Ακροάτρια", "f", "Περίπου δύο εβδομάδες αργότερα, ένα πρωί η φωλιά ήταν άδεια. Λυπήθηκα λίγο, σαν να είχαν φύγει παιδιά από το σπίτι. Φέτος δεν φύτεψα τίποτα σε εκείνη τη γλάστρα. Την άφησα με τα ξερά φύλλα, για την περίπτωση που θα ξανάρθουν.", "About two weeks later, one morning the nest was empty. I felt a little sad, as if children had left home. This year I didn't plant anything in that pot. I left it with the dry leaves, in case they come back."),
 ],
 "questions": [
  Q("Τι βρήκε στη γλάστρα της;", ["Ένα ποντίκι", "Μια φωλιά με τέσσερα αυγά", "Ένα τραυματισμένο πουλί", "Σπόρους ντομάτας"], 1, "υπήρχε μια φωλιά με τέσσερα γαλαζοπράσινα αυγά"),
  Q("Πώς άλλαξε τη ζωή της για δύο εβδομάδες;", ["Έφυγε για διακοπές", "Άνοιγε αθόρυβα την μπαλκονόπορτα και έπινε τον καφέ της μέσα", "Τάιζε τα πουλιά", "Έβγαζε φωτογραφίες κάθε μέρα"], 1, "έπινα τον καφέ μου μέσα, πίσω από την κουρτίνα"),
  Q("Τι έκανε φέτος με τη γλάστρα;", ["Φύτεψε ντομάτες", "Την πέταξε", "Την άφησε με τα ξερά φύλλα, μήπως ξανάρθουν τα πουλιά", "Την έδωσε σε μια γειτόνισσα"], 2, "Την άφησα με τα ξερά φύλλα, για την περίπτωση που θα ξανάρθουν"),
 ],
 "gloss": {"κότσυφας": "κότσυφας — blackbird", "γλάστρα": "γλάστρα — flowerpot", "φτυαράκι": "φτυαράκι — trowel, small spade", "φωλιά": "φωλιά — nest", "μπαλκονόπορτα": "μπαλκονόπορτα — balcony door", "αθόρυβα": "αθόρυβα — quietly", "σκουλήκια": "σκουλήκι — worm"},
})
ITEMS.append({
 "id": "l203-news-smhnos-paidiki-chara", "title": "Σμήνος μελισσών σε παιδική χαρά", "title_en": "A swarm of bees settles in a playground", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση από τοπικό ραδιοφωνικό σταθμό.",
 "script": [
  L("Εκφωνητής", "m", "Ασυνήθιστη εικόνα χθες το μεσημέρι σε παιδική χαρά της πόλης: ένα σμήνος από χιλιάδες μέλισσες κάθισε πάνω στην τσουλήθρα, σχηματίζοντας μια μεγάλη καφετιά μπάλα. Οι γονείς απομάκρυναν αμέσως τα παιδιά και ο δήμος έκλεισε προσωρινά τον χώρο. Κανείς δεν τσιμπήθηκε.", "An unusual sight yesterday at noon in one of the town's playgrounds: a swarm of thousands of bees settled on the slide, forming a large brown ball. Parents immediately moved the children away and the municipality temporarily closed the area. No one was stung."),
  L("Εκφωνητής", "m", "Ένας μελισσοκόμος του συλλόγου της περιοχής μάζεψε το σμήνος μέσα σε ένα ξύλινο κιβώτιο. Όπως εξήγησε, την άνοιξη τα μελίσσια συχνά χωρίζονται: η παλιά βασίλισσα φεύγει με ένα μέρος των εργατριών, για να βρει νέο σπίτι. Ενώ ψάχνουν, οι μέλισσες ξεκουράζονται για λίγες ώρες σε ένα κλαδί ή, όπως εδώ, σε μια τσουλήθρα.", "A beekeeper from the local association gathered the swarm into a wooden box. As he explained, in spring colonies often split: the old queen leaves with part of the workers to find a new home. While searching, the bees rest for a few hours on a branch or, as here, on a slide."),
  L("Εκφωνητής", "m", "Ο μελισσοκόμος τόνισε ότι οι μέλισσες ενός σμήνους είναι συνήθως ήρεμες, γιατί δεν έχουν κυψέλη να υπερασπιστούν. Συνέστησε όμως, σε ανάλογες περιπτώσεις, να μην τις πλησιάζει κανείς και να ειδοποιείται η πυροσβεστική ή ένας μελισσοκόμος.", "The beekeeper stressed that the bees of a swarm are usually calm, because they have no hive to defend. He advised, however, that in similar cases no one should approach them and the fire service or a beekeeper should be notified."),
 ],
 "questions": [
  Q("Πού κάθισε το σμήνος;", ["Σε ένα δέντρο", "Πάνω στην τσουλήθρα μιας παιδικής χαράς", "Σε ένα αυτοκίνητο", "Στο δημαρχείο"], 1, "κάθισε πάνω στην τσουλήθρα"),
  Q("Γιατί σχηματίζονται σμήνη την άνοιξη;", ["Γιατί οι μέλισσες πεινάνε", "Γιατί τα μελίσσια χωρίζονται και η παλιά βασίλισσα ψάχνει νέο σπίτι", "Γιατί κάνει ζέστη", "Γιατί τις ενοχλούν τα παιδιά"], 1, "η παλιά βασίλισσα φεύγει με ένα μέρος των εργατριών"),
  Q("Γιατί οι μέλισσες ενός σμήνους είναι συνήθως ήρεμες;", ["Γιατί είναι κουρασμένες", "Γιατί δεν έχουν κυψέλη να υπερασπιστούν", "Γιατί είναι νέες", "Γιατί δεν έχουν κεντρί"], 1, "δεν έχουν κυψέλη να υπερασπιστούν"),
 ],
 "gloss": {"σμήνος": "σμήνος — swarm", "τσουλήθρα": "τσουλήθρα — slide", "τσιμπήθηκε": "τσιμπιέμαι — to be stung", "κιβώτιο": "κιβώτιο — box, crate", "μελίσσια": "μελίσσι — bee colony, hive", "εργατριών": "εργάτρια — worker (bee)", "κυψέλη": "κυψέλη — beehive", "υπερασπιστούν": "υπερασπίζομαι — to defend"},
})
ITEMS.append({
 "id": "l203-c1-mono-velcro", "title": "Από τις κολλιτσίδες στο βέλκρο", "title_en": "From burrs on a dog's coat to Velcro", "type": "monologue", "level": "C1",
 "context_el": "Μια μηχανικός μιλάει σε ένα φεστιβάλ επιστήμης για τις εφευρέσεις που εμπνεύστηκαν από τη φύση.",
 "script": [
  L("Μηχανικός", "f", "Το 1941 ένας Ελβετός μηχανικός, ο Ζορζ ντε Μεστράλ, γύρισε από μια βόλτα στα βουνά με τον σκύλο του και διαπίστωσε ότι τα ρούχα του και το τρίχωμα του σκύλου ήταν γεμάτα κολλιτσίδες, τα μικρά αγκαθωτά σποροκέφαλα ενός άγριου φυτού. Αντί να τις πετάξει εκνευρισμένος, όπως θα κάναμε οι περισσότεροι, τις κοίταξε στο μικροσκόπιο.", "In 1941 a Swiss engineer, George de Mestral, came back from a walk in the mountains with his dog and found that his clothes and the dog's coat were full of burrs, the small prickly seed heads of a wild plant. Instead of throwing them away in irritation, as most of us would, he looked at them under a microscope."),
  L("Μηχανικός", "f", "Είδε ότι κάθε αγκάθι κατέληγε σε ένα μικροσκοπικό άγκιστρο, που πιανόταν στις θηλιές του υφάσματος και στις τρίχες. Η φύση είχε λύσει με κομψότητα ένα πρόβλημα μεταφοράς: το φυτό χρησιμοποιεί τα ζώα για να σκορπίσει τους σπόρους του μακριά. Ο ντε Μεστράλ σκέφτηκε ότι η ίδια αρχή θα μπορούσε να ενώνει δύο κομμάτια υφάσματος.", "He saw that each spine ended in a tiny hook, which caught in the loops of the fabric and in the hairs. Nature had elegantly solved a transport problem: the plant uses animals to scatter its seeds far away. De Mestral thought the same principle could join two pieces of fabric."),
  L("Μηχανικός", "f", "Η ιδέα ήταν απλή, η υλοποίηση όχι. Χρειάστηκαν χρόνια δοκιμών, ώσπου να βρεθεί ένα υλικό, το νάιλον, που να κρατά το σχήμα των αγκίστρων χωρίς να σπάει. Το δίπλωμα ευρεσιτεχνίας κατοχυρώθηκε στις αρχές της δεκαετίας του πενήντα, και στην αρχή η εφεύρεση αντιμετωπίστηκε με δυσπιστία, ως άσχημη και φτηνή.", "The idea was simple, its execution was not. It took years of trials until a material was found, nylon, that kept the shape of the hooks without breaking. The patent was secured in the early fifties, and at first the invention was met with scepticism, as ugly and cheap."),
  L("Μηχανικός", "f", "Η ιστορία αυτή αποτελεί κλασικό παράδειγμα αυτού που σήμερα ονομάζουμε βιομιμητική: τη μελέτη λύσεων που έχει ήδη δοκιμάσει η εξέλιξη επί εκατομμύρια χρόνια. Το μάθημά της όμως είναι λιγότερο τεχνικό απ' ό,τι φαίνεται. Η ανακάλυψη δεν ξεκίνησε από ένα εργαστήριο, αλλά από μια ενόχληση που κάποιος αποφάσισε να την πάρει στα σοβαρά.", "This story is a classic example of what we now call biomimetics: the study of solutions that evolution has already tested over millions of years. Its lesson, though, is less technical than it seems. The discovery didn't start in a laboratory but with an annoyance that someone decided to take seriously."),
 ],
 "questions": [
  Q("Τι έκανε ο ντε Μεστράλ με τις κολλιτσίδες;", ["Τις πέταξε", "Τις κοίταξε στο μικροσκόπιο", "Τις φύτεψε", "Τις έδωσε σε έναν βοτανολόγο"], 1, "τις κοίταξε στο μικροσκόπιο"),
  Q("Τι πρόβλημα λύνουν τα άγκιστρα για το φυτό;", ["Το προστατεύουν από τα ζώα", "Του επιτρέπουν να σκορπίσει τους σπόρους του μέσω των ζώων", "Το βοηθούν να κρατά νερό", "Το στηρίζουν στον αέρα"], 1, "το φυτό χρησιμοποιεί τα ζώα για να σκορπίσει τους σπόρους του μακριά"),
  Q("Γιατί χρειάστηκαν χρόνια δοκιμών;", ["Γιατί δεν υπήρχαν χρήματα", "Γιατί έπρεπε να βρεθεί υλικό που να κρατά το σχήμα των αγκίστρων χωρίς να σπάει", "Γιατί κανείς δεν πίστευε στην ιδέα", "Λόγω του πολέμου"], 1, "που να κρατά το σχήμα των αγκίστρων χωρίς να σπάει"),
  Q("Ποιο είναι, κατά την ομιλήτρια, το βασικό μάθημα της ιστορίας;", ["Ότι τα εργαστήρια είναι περιττά", "Ότι μια ανακάλυψη μπορεί να ξεκινήσει από μια ενόχληση που παίρνεις στα σοβαρά", "Ότι η φύση είναι πάντα καλύτερη από την τεχνολογία", "Ότι οι εφευρέσεις πρέπει να είναι όμορφες"], 1, "από μια ενόχληση που κάποιος αποφάσισε να την πάρει στα σοβαρά"),
 ],
 "gloss": {"κολλιτσίδες": "κολλιτσίδα — burr", "τρίχωμα": "τρίχωμα — coat (of an animal)", "σποροκέφαλα": "σποροκέφαλο — seed head", "άγκιστρο": "άγκιστρο — hook", "θηλιές": "θηλιά — loop", "σκορπίσει": "σκορπίζω — to scatter", "δίπλωμα ευρεσιτεχνίας": "δίπλωμα ευρεσιτεχνίας — patent", "δυσπιστία": "δυσπιστία — scepticism, distrust", "βιομιμητική": "βιομιμητική — biomimetics"},
})
ITEMS.append({
 "id": "l203-c1-int-fakos-frenel", "title": "Ο φακός που έκανε τους φάρους να φαίνονται από μακριά", "title_en": "The Fresnel lens: how lighthouses reach the horizon", "type": "interview", "level": "C1",
 "context_el": "Συνέντευξη με έναν φυσικό σε μια εκπομπή για την ιστορία της τεχνολογίας.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς ήταν οι φάροι πριν από τον φακό Φρενέλ;", "What were lighthouses like before the Fresnel lens?"),
  L("Φυσικός", "m", "Αρκετά απογοητευτικοί. Έκαιγαν λάδι ή κεριά, και πίσω από τη φλόγα έβαζαν μεταλλικούς καθρέφτες, που όμως απορροφούσαν μεγάλο μέρος του φωτός. Ένας μεγάλος γυάλινος φακός θα συγκέντρωνε καλύτερα το φως, αλλά θα ήταν τόσο χοντρός και βαρύς που θα έσπαγε ή θα ράγιζε από τη ζέστη, και επιπλέον το ίδιο το γυαλί θα απορροφούσε φως.", "Rather disappointing. They burned oil or candles, and behind the flame they placed metal mirrors, which, however, absorbed a large part of the light. A large glass lens would concentrate the light better, but it would be so thick and heavy that it would break or crack from the heat, and on top of that the glass itself would absorb light."),
  L("Δημοσιογράφος", "f", "Και τι σκέφτηκε ο Φρενέλ;", "And what did Fresnel come up with?"),
  L("Φυσικός", "m", "Ο Γάλλος φυσικός Ογκυστέν Φρενέλ παρατήρησε, τη δεκαετία του 1820, ότι το φως διαθλάται μόνο στις επιφάνειες του φακού. Το εσωτερικό γυαλί απλώς προσθέτει βάρος. Έτσι, «έκοψε» νοερά τον φακό σε ομόκεντρους δακτυλίους και κράτησε μόνο τις καμπύλες επιφάνειές τους, τοποθετώντας τους τον έναν δίπλα στον άλλον. Το αποτέλεσμα ήταν ένας φακός πολύ πιο λεπτός και ελαφρύς, που όμως έστελνε το φως σε μια σχεδόν παράλληλη δέσμη.", "The French physicist Augustin Fresnel observed, in the 1820s, that light is refracted only at the surfaces of the lens. The glass inside merely adds weight. So he mentally 'cut' the lens into concentric rings and kept only their curved surfaces, placing them side by side. The result was a lens much thinner and lighter, which nevertheless sent the light out in an almost parallel beam."),
  L("Δημοσιογράφος", "f", "Πόσο μεγάλη ήταν η διαφορά;", "How big was the difference?"),
  L("Φυσικός", "m", "Τεράστια. Ένας φάρος με τέτοιο φακό μπορούσε να φανεί από πολύ μεγαλύτερη απόσταση με την ίδια πηγή φωτός, και έτσι σώθηκαν αμέτρητα πλοία. Το εντυπωσιακό είναι ότι την ίδια αρχή τη βρίσκουμε σήμερα σε πολύ πιο ταπεινά αντικείμενα: στους φακούς των προβολέων, στα φανάρια των αυτοκινήτων, ακόμα και σε εκείνους τους λεπτούς πλαστικούς μεγεθυντικούς φακούς σε μέγεθος πιστωτικής κάρτας.", "Enormous. A lighthouse with such a lens could be seen from a much greater distance with the same light source, and so countless ships were saved. What is striking is that we find the same principle today in much humbler objects: in projector lenses, in car lights, even in those thin plastic magnifiers the size of a credit card."),
 ],
 "questions": [
  Q("Ποιο ήταν το πρόβλημα με τους μεταλλικούς καθρέφτες;", ["Σκούριαζαν", "Απορροφούσαν μεγάλο μέρος του φωτός", "Ήταν πολύ ακριβοί", "Θάμπωναν τους ναυτικούς"], 1, "απορροφούσαν μεγάλο μέρος του φωτός"),
  Q("Γιατί ένας μεγάλος συμπαγής φακός δεν ήταν λύση;", ["Γιατί δεν υπήρχε γυαλί", "Γιατί θα ήταν πολύ χοντρός και βαρύς και θα ράγιζε από τη ζέστη", "Γιατί σκόρπιζε το φως", "Γιατί απαγορευόταν"], 1, "θα ήταν τόσο χοντρός και βαρύς που θα έσπαγε ή θα ράγιζε από τη ζέστη"),
  Q("Ποια ήταν η βασική ιδέα του Φρενέλ;", ["Να χρησιμοποιήσει περισσότερα κεριά", "Να κρατήσει μόνο τις καμπύλες επιφάνειες, σε ομόκεντρους δακτυλίους", "Να βάψει το γυαλί", "Να βάλει τον φακό πιο ψηλά"], 1, "κράτησε μόνο τις καμπύλες επιφάνειές τους"),
  Q("Πού βρίσκουμε σήμερα την ίδια αρχή, σύμφωνα με τον φυσικό;", ["Μόνο σε φάρους", "Σε προβολείς, φανάρια αυτοκινήτων και λεπτούς μεγεθυντικούς φακούς", "Στα κινητά τηλέφωνα", "Στα γυαλιά ηλίου"], 1, "στους φακούς των προβολέων, στα φανάρια των αυτοκινήτων"),
 ],
 "gloss": {"απογοητευτικοί": "απογοητευτικός — disappointing", "απορροφούσαν": "απορροφώ — to absorb", "διαθλάται": "διαθλώμαι — to be refracted", "ομόκεντρους": "ομόκεντρος — concentric", "καμπύλες": "καμπύλος — curved", "δέσμη": "δέσμη — beam", "ταπεινά": "ταπεινός — humble", "μεγεθυντικούς": "μεγεθυντικός — magnifying"},
})

rnd = random.Random(203)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-203.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
