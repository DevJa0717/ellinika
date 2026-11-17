# Source for library/listening/listening-159.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l159.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l159-ann-votanikos", "title": "Ανακοίνωση στον βοτανικό κήπο", "title_en": "An announcement at the botanical garden", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση από τα μεγάφωνα ενός βοτανικού κήπου.",
 "script": [
  L("Εκφωνήτρια", "f", "Αγαπητοί επισκέπτες, σας ενημερώνουμε ότι το θερμοκήπιο με τους κάκτους και τα παχύφυτα παραμένει κλειστό για εργασίες ανακαίνισης. Θα ξανανοίξει την άνοιξη, με νέο σύστημα θέρμανσης και περισσότερα είδη.", "Dear visitors, please note that the greenhouse with the cacti and succulents remains closed for renovation work. It will reopen in spring, with a new heating system and more species."),
  L("Εκφωνήτρια", "f", "Στις δώδεκα ξεκινά δωρεάν ξενάγηση στον κήπο με τα αρωματικά φυτά της ελληνικής φύσης, όπως το θυμάρι, η ρίγανη και το φασκόμηλο. Σημείο συνάντησης είναι η μεγάλη πλάτανος δίπλα στη λιμνούλα.", "At twelve a free guided tour begins of the garden of aromatic plants of Greek nature, such as thyme, oregano and sage. The meeting point is the big plane tree next to the pond."),
  L("Εκφωνήτρια", "f", "Υπενθυμίζουμε ότι απαγορεύεται να κόβετε φύλλα ή λουλούδια, ακόμη και για να τα μυρίσετε. Όσοι θέλετε σπόρους ή μικρά φυτά, θα τα βρείτε στο πωλητήριο δίπλα στην έξοδο, και τα έσοδα πηγαίνουν στη συντήρηση του κήπου.", "We remind you that it is forbidden to pick leaves or flowers, even to smell them. Those of you who would like seeds or small plants will find them at the shop next to the exit, and the proceeds go to the upkeep of the garden."),
 ],
 "questions": [
  Q("Γιατί είναι κλειστό το θερμοκήπιο με τους κάκτους;", ["Λόγω κρύου", "Για εργασίες ανακαίνισης", "Γιατί μεταφέρονται τα φυτά", "Λόγω έλλειψης προσωπικού"], 1, "παραμένει κλειστό για εργασίες ανακαίνισης"),
  Q("Πού είναι το σημείο συνάντησης για την ξενάγηση;", ["Στην είσοδο", "Στο πωλητήριο", "Στη μεγάλη πλάτανο δίπλα στη λιμνούλα", "Στο θερμοκήπιο"], 2, "η μεγάλη πλάτανος δίπλα στη λιμνούλα"),
  Q("Πού πηγαίνουν τα έσοδα από το πωλητήριο;", ["Σε ένα σχολείο", "Στη συντήρηση του κήπου", "Σε νέα θερμοκήπια", "Στον δήμο"], 1, "τα έσοδα πηγαίνουν στη συντήρηση του κήπου"),
 ],
 "gloss": {"βοτανικού κήπου": "βοτανικός κήπος — botanical garden", "κάκτους": "κάκτος — cactus", "παχύφυτα": "παχύφυτο — succulent", "ανακαίνισης": "ανακαίνιση — renovation", "θέρμανσης": "θέρμανση — heating", "αρωματικά": "αρωματικός — aromatic", "θυμάρι": "θυμάρι — thyme", "φασκόμηλο": "φασκόμηλο — sage", "λιμνούλα": "λιμνούλα — pond", "πωλητήριο": "πωλητήριο — (museum/garden) shop", "έσοδα": "έσοδα — proceeds, revenue"},
})

ITEMS.append({
 "id": "l159-int-bonsai", "title": "Ένα δέντρο σε μια γλάστρα", "title_en": "A tree in a pot", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν συνταξιούχο που καλλιεργεί δέντρα μπονσάι.",
 "script": [
  L("Δημοσιογράφος", "f", "Τι ακριβώς είναι ένα μπονσάι;", "What exactly is a bonsai?"),
  L("Καλλιεργητής", "m", "Πολλοί νομίζουν ότι είναι ειδικό είδος φυτού. Δεν είναι. Είναι ένα κανονικό δέντρο, μια ελιά, ένα πεύκο, μια φτελιά, που το κρατάμε μικρό σε μια ρηχή γλάστρα, κόβοντας με προσοχή τα κλαδιά και τις ρίζες του.", "Many people think it's a special kind of plant. It isn't. It's an ordinary tree, an olive, a pine, an elm, that we keep small in a shallow pot by carefully cutting its branches and roots."),
  L("Δημοσιογράφος", "f", "Πόσο χρόνο θέλει;", "How much time does it take?"),
  L("Καλλιεργητής", "m", "Χρόνια. Η ελιά που βλέπετε εδώ τη βρήκα πριν από είκοσι χρόνια σε ένα χωράφι που θα το έκαναν οικόπεδο. Ήταν ξεραμένη από τη μία πλευρά. Χρειάστηκαν πέντε χρόνια μόνο για να ξαναβγάλει δυνατά κλαδιά.", "Years. The olive tree you see here I found twenty years ago in a field that was going to become a building plot. It was dried up on one side. It took five years just for it to put out strong branches again."),
  L("Δημοσιογράφος", "f", "Ποιο είναι το μεγαλύτερο λάθος των αρχαρίων;", "What's the biggest mistake beginners make?"),
  L("Καλλιεργητής", "m", "Τα βάζουν μέσα στο σπίτι, σαν διακοσμητικά. Τα περισσότερα μπονσάι είναι δέντρα του έξω κόσμου· χρειάζονται ήλιο, αέρα και το κρύο του χειμώνα. Μέσα στο σαλόνι μαραίνονται σε λίγους μήνες.", "They put them inside the house, as decorations. Most bonsai are outdoor trees; they need sun, air and the cold of winter. In the living room they wither within a few months."),
 ],
 "questions": [
  Q("Τι είναι, σύμφωνα με τον καλλιεργητή, ένα μπονσάι;", ["Ένα ειδικό είδος φυτού από την Ιαπωνία", "Ένα κανονικό δέντρο που το κρατάμε μικρό σε ρηχή γλάστρα", "Ένα τεχνητό φυτό", "Ένα δέντρο που δεν μεγαλώνει ποτέ"], 1, "Είναι ένα κανονικό δέντρο"),
  Q("Πού βρήκε την ελιά του;", ["Σε ένα φυτώριο", "Σε ένα χωράφι που θα το έκαναν οικόπεδο", "Στον κήπο του πατέρα του", "Σε μια έκθεση"], 1, "σε ένα χωράφι που θα το έκαναν οικόπεδο"),
  Q("Ποιο είναι το μεγαλύτερο λάθος των αρχαρίων;", ["Ότι τα ποτίζουν λίγο", "Ότι τα κλαδεύουν πολύ", "Ότι τα βάζουν μέσα στο σπίτι, σαν διακοσμητικά", "Ότι αγοράζουν ακριβά δέντρα"], 2, "Τα βάζουν μέσα στο σπίτι, σαν διακοσμητικά"),
 ],
 "gloss": {"καλλιεργεί": "καλλιεργώ — to grow, to cultivate", "μπονσάι": "μπονσάι — bonsai", "φτελιά": "φτελιά — elm", "ρηχή": "ρηχός — shallow", "γλάστρα": "γλάστρα — (flower) pot", "κλαδιά": "κλαδί — branch", "ρίζες": "ρίζα — root", "οικόπεδο": "οικόπεδο — building plot", "ξεραμένη": "ξεραμένος — dried up", "αρχαρίων": "αρχάριος — beginner", "μαραίνονται": "μαραίνομαι — to wither"},
})

ITEMS.append({
 "id": "l159-dia-pitsa", "title": "Πίτσα στο σπίτι;", "title_en": "Pizza at home?", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε ένα ζευγάρι να συζητάει αν θα φτιάξει πίτσα στο σπίτι για τους φίλους του.",
 "script": [
  L("Φαίη", "f", "Το Σάββατο που έρχονται τα παιδιά, λέω να φτιάξουμε πίτσα μόνοι μας αντί να παραγγείλουμε.", "On Saturday, when our friends come, I'm thinking we make pizza ourselves instead of ordering."),
  L("Μάρκος", "m", "Το έχουμε ξαναπροσπαθήσει, θυμάσαι; Η ζύμη βγήκε σαν παξιμάδι.", "We've tried it before, remember? The dough came out like a rusk."),
  L("Φαίη", "f", "Γιατί τη ζυμώσαμε το ίδιο απόγευμα. Διάβασα ότι η καλή ζύμη θέλει πολύ λίγη μαγιά και να μείνει στο ψυγείο τουλάχιστον μια μέρα. Έτσι γίνεται αφράτη και πιο εύπεπτη.", "Because we kneaded it the same afternoon. I read that good dough needs very little yeast and has to stay in the fridge for at least a day. That way it becomes fluffy and easier to digest."),
  L("Μάρκος", "m", "Και ο φούρνος μας δεν ζεσταίνεται αρκετά. Οι πιτσαρίες ψήνουν στους τετρακόσιους βαθμούς.", "And our oven doesn't get hot enough. Pizzerias bake at four hundred degrees."),
  L("Φαίη", "f", "Θα βάλουμε τον φούρνο στο τέρμα για μισή ώρα πριν, με το ταψί μέσα. Και θα κάνουμε έναν πάγκο με υλικά, να διαλέξει ο καθένας τα δικά του.", "We'll put the oven on full for half an hour beforehand, with the tray inside. And we'll set up a counter with toppings, so everyone can choose their own."),
  L("Μάρκος", "m", "Εντάξει, αλλά αν βγει πάλι παξιμάδι, παραγγέλνουμε και δεν το συζητάμε!", "OK, but if it comes out like a rusk again, we're ordering, no discussion!"),
 ],
 "questions": [
  Q("Γιατί, κατά τη Φαίη, απέτυχε η ζύμη την προηγούμενη φορά;", ["Γιατί έβαλαν πολύ αλεύρι", "Γιατί τη ζύμωσαν το ίδιο απόγευμα", "Γιατί ο φούρνος χάλασε", "Γιατί ξέχασαν τη μαγιά"], 1, "Γιατί τη ζυμώσαμε το ίδιο απόγευμα"),
  Q("Τι θέλει η καλή ζύμη, σύμφωνα με όσα διάβασε η Φαίη;", ["Πολλή μαγιά και ζεστό νερό", "Πολύ λίγη μαγιά και μία τουλάχιστον μέρα στο ψυγείο", "Να ψηθεί αμέσως", "Αλεύρι από την Ιταλία"], 1, "θέλει πολύ λίγη μαγιά και να μείνει στο ψυγείο τουλάχιστον μια μέρα"),
  Q("Πώς σκοπεύει η Φαίη να λύσει το πρόβλημα του φούρνου;", ["Θα αγοράσουν καινούργιο φούρνο", "Θα ψήσουν στην πιτσαρία", "Θα βάλουν τον φούρνο στο τέρμα για μισή ώρα πριν, με το ταψί μέσα", "Θα ψήσουν στα κάρβουνα"], 2, "Θα βάλουμε τον φούρνο στο τέρμα για μισή ώρα πριν, με το ταψί μέσα"),
 ],
 "gloss": {"παραγγείλουμε": "παραγγέλνω — to order", "ζύμη": "ζύμη — dough", "παξιμάδι": "παξιμάδι — rusk", "ζυμώσαμε": "ζυμώνω — to knead", "μαγιά": "μαγιά — yeast", "αφράτη": "αφράτος — fluffy", "εύπεπτη": "εύπεπτος — easy to digest", "πιτσαρίες": "πιτσαρία — pizzeria", "στο τέρμα": "στο τέρμα — (turned up) to the maximum", "ταψί": "ταψί — baking tray", "υλικά": "υλικό — ingredient, topping"},
})

ITEMS.append({
 "id": "l159-mon-tyropites", "title": "Τυρόπιτες από τις πέντε το πρωί", "title_en": "Cheese pies from five in the morning", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα που έχει ένα μικρό πιτάδικο να μιλάει σε μια εκπομπή για τη δουλειά της.",
 "script": [
  L("Πιτοποιός", "f", "Το ξυπνητήρι μου χτυπάει στις τέσσερις. Στις πέντε ανοίγω το πιτάδικο, γιατί οι πρώτοι πελάτες είναι οι οδηγοί των λεωφορείων και οι εργάτες που πάνε για δουλειά. Ως τις οκτώ έχω πουλήσει τις μισές πίτες της μέρας.", "My alarm goes off at four. At five I open the pie shop, because the first customers are the bus drivers and the workers going to work. By eight I've sold half the day's pies."),
  L("Πιτοποιός", "f", "Το φύλλο το ανοίγω μόνη μου, με τον πλάστη, όπως μου έμαθε η πεθερά μου. Είναι πιο κουραστικό από το έτοιμο φύλλο, αλλά οι πελάτες καταλαβαίνουν αμέσως τη διαφορά: είναι πιο τραγανό και δεν μουσκεύει από το βούτυρο.", "I roll out the pastry myself, with the rolling pin, as my mother-in-law taught me. It's more tiring than ready-made pastry, but customers immediately notice the difference: it's crisper and doesn't get soggy from the butter."),
  L("Πιτοποιός", "f", "Το δύσκολο είναι ότι δεν έχω κοινωνική ζωή· στις εννιά το βράδυ κοιμάμαι. Όμως δεν θα το άλλαζα. Ξέρω τους μισούς ανθρώπους της γειτονιάς με το όνομά τους, και ξέρω τι πίτα θα πάρει ο καθένας πριν μου το πει.", "The hard thing is that I have no social life; at nine in the evening I'm asleep. But I wouldn't change it. I know half the people in the neighbourhood by name, and I know which pie each one will have before they tell me."),
 ],
 "questions": [
  Q("Ποιοι είναι οι πρώτοι πελάτες της;", ["Μαθητές", "Οδηγοί λεωφορείων και εργάτες", "Τουρίστες", "Συνταξιούχοι"], 1, "οι οδηγοί των λεωφορείων και οι εργάτες"),
  Q("Γιατί ανοίγει μόνη της το φύλλο;", ["Γιατί είναι φθηνότερο", "Γιατί το έτοιμο φύλλο δεν βρίσκεται", "Γιατί βγαίνει πιο τραγανό και δεν μουσκεύει", "Γιατί είναι πιο γρήγορο"], 2, "είναι πιο τραγανό και δεν μουσκεύει από το βούτυρο"),
  Q("Ποιο είναι το δύσκολο της δουλειάς της;", ["Τα χαμηλά κέρδη", "Ότι δεν έχει κοινωνική ζωή", "Οι δύσκολοι πελάτες", "Η ζέστη του φούρνου"], 1, "δεν έχω κοινωνική ζωή"),
 ],
 "gloss": {"πιτάδικο": "πιτάδικο — pie shop", "ξυπνητήρι": "ξυπνητήρι — alarm clock", "φύλλο": "φύλλο — (filo) pastry sheet", "πλάστη": "πλάστης — rolling pin", "πεθερά": "πεθερά — mother-in-law", "τραγανό": "τραγανός — crisp, crunchy", "μουσκεύει": "μουσκεύω — to get soggy", "βούτυρο": "βούτυρο — butter"},
})

ITEMS.append({
 "id": "l159-int-drone", "title": "Ο χειριστής του μη επανδρωμένου", "title_en": "The drone operator", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με έναν εθελοντή που χειρίζεται μη επανδρωμένα αεροσκάφη σε ομάδα έρευνας και διάσωσης.",
 "script": [
  L("Δημοσιογράφος", "f", "Πώς βοηθάει ένα μη επανδρωμένο αεροσκάφος σε μια διάσωση;", "How does a drone help in a rescue?"),
  L("Εθελοντής", "m", "Όταν χάνεται κάποιος στο βουνό, οι ομάδες στο έδαφος μπορεί να χρειαστούν ώρες για να ψάξουν μια χαράδρα. Εμείς σηκώνουμε το αεροσκάφος και σε δέκα λεπτά έχουμε δει όλη την περιοχή από ψηλά.", "When someone gets lost on the mountain, ground teams may need hours to search a ravine. We put the drone up and in ten minutes we've seen the whole area from above."),
  L("Δημοσιογράφος", "f", "Και τη νύχτα;", "And at night?"),
  L("Εθελοντής", "m", "Τη νύχτα είναι ακόμα πιο χρήσιμο, γιατί έχει θερμική κάμερα. Το ανθρώπινο σώμα είναι πιο ζεστό από το περιβάλλον, οπότε φαίνεται σαν μια φωτεινή κηλίδα. Πέρσι έτσι βρήκαμε έναν ηλικιωμένο που είχε χαθεί σε έναν ελαιώνα.", "At night it's even more useful, because it has a thermal camera. The human body is warmer than its surroundings, so it shows up as a bright spot. Last year that's how we found an elderly man who had got lost in an olive grove."),
  L("Δημοσιογράφος", "f", "Υπάρχουν περιορισμοί;", "Are there limitations?"),
  L("Εθελοντής", "m", "Πολλοί. Με δυνατό αέρα ή βροχή δεν πετάμε. Η μπαταρία κρατάει περίπου μισή ώρα, γι' αυτό κουβαλάμε πάντα πολλές. Και φυσικά χρειάζεται άδεια και εκπαίδευση· δεν είναι παιχνίδι.", "Many. In strong wind or rain we don't fly. The battery lasts about half an hour, which is why we always carry several. And of course you need a licence and training; it's not a toy."),
 ],
 "questions": [
  Q("Πόσο χρόνο χρειάζεται το αεροσκάφος για να δει όλη την περιοχή;", ["Μία ώρα", "Περίπου δέκα λεπτά", "Μισή μέρα", "Δύο λεπτά"], 1, "σε δέκα λεπτά έχουμε δει όλη την περιοχή από ψηλά"),
  Q("Γιατί είναι χρήσιμο τη νύχτα;", ["Γιατί έχει δυνατούς προβολείς", "Γιατί έχει θερμική κάμερα", "Γιατί πετάει πιο ψηλά", "Γιατί δεν φυσάει αέρας"], 1, "γιατί έχει θερμική κάμερα"),
  Q("Γιατί κουβαλάνε πολλές μπαταρίες;", ["Γιατί χαλάνε συχνά", "Γιατί η μπαταρία κρατάει περίπου μισή ώρα", "Γιατί είναι φθηνές", "Γιατί το απαιτεί ο νόμος"], 1, "Η μπαταρία κρατάει περίπου μισή ώρα"),
 ],
 "gloss": {"μη επανδρωμένα αεροσκάφη": "μη επανδρωμένο αεροσκάφος — drone, unmanned aircraft", "έρευνας και διάσωσης": "έρευνα και διάσωση — search and rescue", "χαράδρα": "χαράδρα — ravine, gorge", "θερμική": "θερμικός — thermal", "κηλίδα": "κηλίδα — spot", "ελαιώνα": "ελαιώνας — olive grove", "περιορισμοί": "περιορισμός — limitation", "μπαταρία": "μπαταρία — battery", "άδεια": "άδεια — licence, permit"},
})

ITEMS.append({
 "id": "l159-vm-fytorio", "title": "Μήνυμα από το φυτώριο", "title_en": "A message from the plant nursery", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από ένα φυτώριο, όπου παραγγείλατε δέντρα για τον κήπο σας.",
 "script": [
  L("Υπάλληλος", "m", "Καλημέρα σας, από το φυτώριο σας παίρνω, για την παραγγελία σας. Οι τρεις λεμονιές και η ροδιά είναι έτοιμες. Η συκιά που ζητήσατε, όμως, δεν έχει έρθει ακόμα από τον παραγωγό· περιμένουμε να έρθει στα μέσα του μήνα.", "Good morning, I'm calling from the nursery about your order. The three lemon trees and the pomegranate are ready. The fig tree you asked for, however, hasn't arrived from the grower yet; we expect it in the middle of the month."),
  L("Υπάλληλος", "m", "Σας προτείνω να φυτέψετε τώρα τις λεμονιές, πριν πιάσουν οι παγωνιές. Αν θέλετε, ο συνεργάτης μας μπορεί να έρθει να τις φυτέψει ο ίδιος· η υπηρεσία κοστίζει είκοσι ευρώ για κάθε δέντρο και περιλαμβάνει και το λίπασμα.", "I suggest you plant the lemon trees now, before the frosts set in. If you like, our colleague can come and plant them himself; the service costs twenty euros per tree and includes the fertiliser."),
  L("Υπάλληλος", "m", "Τη μεταφορά την κάνουμε δωρεάν για παραγγελίες πάνω από εκατό ευρώ, οπότε η δική σας μπαίνει σε αυτή την κατηγορία. Πείτε μου μόνο ποια μέρα σας βολεύει.", "We deliver free of charge for orders over a hundred euros, so yours falls into that category. Just tell me which day suits you."),
 ],
 "questions": [
  Q("Ποιο δέντρο δεν έχει έρθει ακόμα;", ["Οι λεμονιές", "Η ροδιά", "Η συκιά", "Η ελιά"], 2, "Η συκιά που ζητήσατε, όμως, δεν έχει έρθει ακόμα"),
  Q("Γιατί προτείνει να φυτέψετε τώρα τις λεμονιές;", ["Πριν πιάσουν οι παγωνιές", "Γιατί αλλιώς θα ξεραθούν στις γλάστρες", "Γιατί μετά θα ακριβύνει η υπηρεσία", "Γιατί έρχονται βροχές"], 0, "πριν πιάσουν οι παγωνιές"),
  Q("Τι ισχύει για τη μεταφορά των δέντρων σας;", ["Κοστίζει είκοσι ευρώ", "Είναι δωρεάν", "Πρέπει να τα πάρετε μόνοι σας", "Γίνεται μόνο τα Σάββατα"], 1, "Τη μεταφορά την κάνουμε δωρεάν για παραγγελίες πάνω από εκατό ευρώ"),
 ],
 "gloss": {"φυτώριο": "φυτώριο — (plant) nursery", "λεμονιές": "λεμονιά — lemon tree", "ροδιά": "ροδιά — pomegranate tree", "συκιά": "συκιά — fig tree", "παραγωγό": "παραγωγός — grower, producer", "φυτέψετε": "φυτεύω — to plant", "παγωνιές": "παγωνιά — frost", "λίπασμα": "λίπασμα — fertiliser", "μεταφορά": "μεταφορά — delivery, transport", "κατηγορία": "κατηγορία — category"},
})

ITEMS.append({
 "id": "l159-vm-sokolata", "title": "Εργαστήρι σοκολάτας για τα γενέθλια", "title_en": "A chocolate workshop for the birthday", "type": "voicemail", "level": "B2",
 "context_el": "Ακούτε ένα μήνυμα στον τηλεφωνητή σας από ένα εργαστήρι σοκολάτας, όπου κλείσατε ένα παιδικό πάρτι.",
 "script": [
  L("Υπεύθυνη", "f", "Γεια σας, η Ιωάννα από το εργαστήρι σοκολάτας. Σας επιβεβαιώνω το πάρτι για τα γενέθλια της κόρης σας την Κυριακή, στις έντεκα το πρωί. Το εργαστήρι διαρκεί μιάμιση ώρα και τα παιδιά θα φτιάξουν σοκολατένια γλειφιτζούρια και τρουφάκια.", "Hello, it's Ioanna from the chocolate workshop. I'm confirming the party for your daughter's birthday on Sunday at eleven in the morning. The workshop lasts an hour and a half and the children will make chocolate lollipops and truffles."),
  L("Υπεύθυνη", "f", "Μου είπατε ότι ένα από τα παιδιά έχει αλλεργία στους ξηρούς καρπούς. Για να είμαστε σίγουροι, εκείνη τη μέρα δεν θα χρησιμοποιήσουμε καθόλου φουντούκια ή αμύγδαλα, ούτε για διακόσμηση.", "You told me that one of the children has a nut allergy. To be safe, on that day we won't use any hazelnuts or almonds at all, not even for decoration."),
  L("Υπεύθυνη", "f", "Τα παιδιά καλό είναι να φορούν ρούχα που δεν πειράζει να λερωθούν· ποδιές δίνουμε εμείς. Στο τέλος κάθε παιδί παίρνει σπίτι ένα κουτάκι με ό,τι έφτιαξε. Την πληρωμή την κάνετε την ίδια μέρα.", "It's a good idea for the children to wear clothes that can get dirty; we provide aprons. At the end each child takes home a little box with what they made. You pay on the day."),
 ],
 "questions": [
  Q("Τι θα φτιάξουν τα παιδιά;", ["Τούρτα γενεθλίων", "Σοκολατένια γλειφιτζούρια και τρουφάκια", "Μπισκότα", "Ζεστή σοκολάτα"], 1, "σοκολατένια γλειφιτζούρια και τρουφάκια"),
  Q("Γιατί δεν θα χρησιμοποιήσουν φουντούκια ή αμύγδαλα;", ["Γιατί ακρίβυναν", "Γιατί ένα παιδί έχει αλλεργία στους ξηρούς καρπούς", "Γιατί δεν αρέσουν στα παιδιά", "Γιατί λερώνουν"], 1, "ένα από τα παιδιά έχει αλλεργία στους ξηρούς καρπούς"),
  Q("Τι πρέπει να φορούν τα παιδιά;", ["Ποδιές από το σπίτι", "Γιορτινά ρούχα", "Ρούχα που δεν πειράζει να λερωθούν", "Γάντια"], 2, "ρούχα που δεν πειράζει να λερωθούν"),
 ],
 "gloss": {"εργαστήρι": "εργαστήρι — workshop", "επιβεβαιώνω": "επιβεβαιώνω — to confirm", "γλειφιτζούρια": "γλειφιτζούρι — lollipop", "τρουφάκια": "τρουφάκι — (chocolate) truffle", "αλλεργία": "αλλεργία — allergy", "ξηρούς καρπούς": "ξηροί καρποί — nuts", "φουντούκια": "φουντούκι — hazelnut", "αμύγδαλα": "αμύγδαλο — almond", "λερωθούν": "λερώνομαι — to get dirty", "ποδιές": "ποδιά — apron"},
})

ITEMS.append({
 "id": "l159-dia-kryfos-ai-vasilis", "title": "Κρυφός Άγιος Βασίλης στο γραφείο", "title_en": "Secret Santa at the office", "type": "dialogue", "level": "B2",
 "context_el": "Ακούτε δύο συναδέλφους να οργανώνουν την ανταλλαγή δώρων των Χριστουγέννων στο γραφείο τους.",
 "script": [
  L("Ρούλα", "f", "Φέτος λέω να κάνουμε κρυφό Άγιο Βασίλη. Ο καθένας τραβάει ένα όνομα και κάνει δώρο μόνο σε αυτόν τον συνάδελφο, χωρίς να ξέρει ο άλλος από ποιον είναι.", "This year I'm thinking we do Secret Santa. Everyone draws a name and gives a present only to that colleague, without the other knowing who it's from."),
  L("Θοδωρής", "m", "Καλή ιδέα, αλλά πρέπει να βάλουμε όριο στην τιμή. Πέρσι κάποιοι πήραν ακριβά δώρα και άλλοι ένα φλιτζάνι, και ένιωσαν άσχημα.", "Good idea, but we need to set a price limit. Last year some people bought expensive presents and others a mug, and they felt bad."),
  L("Ρούλα", "f", "Λέω δεκαπέντε ευρώ το πολύ. Και για όσους δεν ξέρουν τι να πάρουν, ο καθένας γράφει σε ένα χαρτάκι τρία πράγματα που του αρέσουν.", "I say fifteen euros at most. And for those who don't know what to buy, everyone writes on a slip of paper three things they like."),
  L("Θοδωρής", "m", "Τα ονόματα πώς θα τα τραβήξουμε; Ο μισός όροφος δουλεύει από το σπίτι τις Παρασκευές.", "How will we draw the names? Half the floor works from home on Fridays."),
  L("Ρούλα", "f", "Υπάρχουν εφαρμογές που το κάνουν μόνες τους και στέλνουν στον καθένα ένα μήνυμα με το όνομα. Και ανοίγουμε τα δώρα όλοι μαζί στο γιορτινό τραπέζι, στις είκοσι Δεκεμβρίου.", "There are apps that do it automatically and send each person a message with the name. And we open the presents all together at the festive meal on the twentieth of December."),
 ],
 "questions": [
  Q("Γιατί θέλει ο Θοδωρής όριο στην τιμή;", ["Γιατί δεν έχει χρήματα", "Γιατί πέρσι κάποιοι πήραν ακριβά δώρα και άλλοι φτηνά και ένιωσαν άσχημα", "Γιατί το ζήτησε ο διευθυντής", "Γιατί τα δώρα είναι περιττά"], 1, "Πέρσι κάποιοι πήραν ακριβά δώρα και άλλοι ένα φλιτζάνι"),
  Q("Τι θα γράψει ο καθένας στο χαρτάκι;", ["Το όνομά του", "Τρία πράγματα που του αρέσουν", "Το μέγεθος των ρούχων του", "Μια ευχή"], 1, "τρία πράγματα που του αρέσουν"),
  Q("Πώς θα τραβήξουν τα ονόματα;", ["Από ένα καπέλο την Παρασκευή", "Θα τα διαλέξει η Ρούλα", "Με μια εφαρμογή που στέλνει μήνυμα στον καθένα", "Στο γιορτινό τραπέζι"], 2, "Υπάρχουν εφαρμογές που το κάνουν μόνες τους"),
 ],
 "gloss": {"ανταλλαγή": "ανταλλαγή — exchange", "κρυφό Άγιο Βασίλη": "κρυφός Άγιος Βασίλης — Secret Santa", "τραβάει": "τραβάω — to draw (a name)", "όριο": "όριο — limit", "φλιτζάνι": "φλιτζάνι — cup, mug", "χαρτάκι": "χαρτάκι — slip of paper", "όροφος": "όροφος — floor, storey", "εφαρμογές": "εφαρμογή — app", "γιορτινό": "γιορτινός — festive"},
})

ITEMS.append({
 "id": "l159-c1-milgram", "title": "Μέχρι πού φτάνει η υπακοή;", "title_en": "How far does obedience go?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από διάλεξη κοινωνικής ψυχολογίας για ένα από τα πιο γνωστά και αμφιλεγόμενα πειράματα του εικοστού αιώνα.",
 "script": [
  L("Καθηγήτρια", "f", "Το 1961, την ίδια χρονιά που δικαζόταν στην Ιερουσαλήμ ο ναζί αξιωματούχος Άντολφ Άιχμαν, ο νεαρός ψυχολόγος Στάνλεϊ Μίλγκραμ ξεκίνησε στο Πανεπιστήμιο Γέιλ μια σειρά πειραμάτων. Ήθελε να μάθει πόσο μακριά θα πήγαιναν απλοί άνθρωποι, αν τους το ζητούσε μια αρχή που θεωρούσαν νόμιμη.", "In 1961, the same year that the Nazi official Adolf Eichmann was being tried in Jerusalem, the young psychologist Stanley Milgram began a series of experiments at Yale University. He wanted to find out how far ordinary people would go if asked to by an authority they regarded as legitimate."),
  L("Καθηγήτρια", "f", "Οι συμμετέχοντες πίστευαν ότι λαμβάνουν μέρος σε έρευνα για τη μάθηση. Στον ρόλο του «δασκάλου», έπρεπε να δίνουν ηλεκτροσόκ σε έναν «μαθητή» κάθε φορά που έκανε λάθος, αυξάνοντας την ένταση ως τα τετρακόσια πενήντα βολτ. Στην πραγματικότητα ο μαθητής ήταν ηθοποιός και δεν δεχόταν κανένα σοκ, αλλά φώναζε και παρακαλούσε να σταματήσουν.", "The participants believed they were taking part in research on learning. In the role of 'teacher', they had to give electric shocks to a 'learner' every time he made a mistake, increasing the intensity up to four hundred and fifty volts. In reality the learner was an actor and received no shocks at all, but he shouted and begged them to stop."),
  L("Καθηγήτρια", "f", "Στη βασική εκδοχή του πειράματος, περίπου τα δύο τρίτα των συμμετεχόντων έφτασαν ως το τέλος, συχνά ιδρώνοντας και διαμαρτυρόμενοι, αλλά υπακούοντας στον ερευνητή με τη λευκή ποδιά. Σε άλλες εκδοχές, όμως, η υπακοή μειωνόταν αισθητά: όταν ο ερευνητής έδινε τις εντολές από το τηλέφωνο ή όταν ο δάσκαλος έπρεπε να αγγίξει ο ίδιος τον μαθητή.", "In the basic version of the experiment, about two thirds of the participants went all the way to the end, often sweating and protesting, but obeying the researcher in the white coat. In other versions, however, obedience dropped noticeably: when the researcher gave orders over the phone, or when the teacher had to touch the learner himself."),
  L("Καθηγήτρια", "f", "Σήμερα ένα τέτοιο πείραμα δεν θα εγκρινόταν ποτέ, λόγω της ψυχικής πίεσης που προκάλεσε. Επιπλέον, νεότερες έρευνες στο αρχείο του Μίλγκραμ έδειξαν ότι αρκετοί συμμετέχοντες υποψιάζονταν ότι τα σοκ δεν ήταν αληθινά. Το βασικό του δίδαγμα, πάντως, ότι η κατάσταση μπορεί να μετρήσει περισσότερο από τον χαρακτήρα, εξακολουθεί να μας προβληματίζει.", "Today such an experiment would never be approved, because of the psychological strain it caused. Moreover, more recent research in Milgram's archive showed that quite a few participants suspected that the shocks were not real. Its basic lesson, however, that the situation can count for more than character, continues to trouble us."),
 ],
 "questions": [
  Q("Τι ήθελε να μάθει ο Μίλγκραμ;", ["Πώς μαθαίνουν οι άνθρωποι από τα λάθη τους", "Πόσο μακριά θα πήγαιναν απλοί άνθρωποι, αν τους το ζητούσε μια αρχή που θεωρούσαν νόμιμη", "Αν ο πόνος βοηθάει τη μνήμη", "Πώς λειτουργούν τα δικαστήρια"], 1, "πόσο μακριά θα πήγαιναν απλοί άνθρωποι"),
  Q("Τι ίσχυε στην πραγματικότητα για τον «μαθητή»;", ["Ήταν εθελοντής φοιτητής", "Ήταν ηθοποιός και δεν δεχόταν κανένα σοκ", "Δεχόταν ελαφριά σοκ", "Ήταν ο ίδιος ο Μίλγκραμ"], 1, "ο μαθητής ήταν ηθοποιός και δεν δεχόταν κανένα σοκ"),
  Q("Πότε μειωνόταν αισθητά η υπακοή;", ["Όταν ο ερευνητής φορούσε λευκή ποδιά", "Όταν ο ερευνητής έδινε τις εντολές από το τηλέφωνο", "Όταν ο μαθητής δεν φώναζε", "Όταν οι συμμετέχοντες πληρώνονταν περισσότερο"], 1, "όταν ο ερευνητής έδινε τις εντολές από το τηλέφωνο"),
  Q("Τι έδειξαν οι νεότερες έρευνες στο αρχείο του Μίλγκραμ;", ["Ότι τα αποτελέσματα είχαν παραποιηθεί πλήρως", "Ότι αρκετοί συμμετέχοντες υποψιάζονταν ότι τα σοκ δεν ήταν αληθινά", "Ότι κανείς δεν είχε φτάσει ως το τέλος", "Ότι το πείραμα είχε γίνει με παιδιά"], 1, "αρκετοί συμμετέχοντες υποψιάζονταν ότι τα σοκ δεν ήταν αληθινά"),
 ],
 "gloss": {"αμφιλεγόμενα": "αμφιλεγόμενος — controversial", "δικαζόταν": "δικάζομαι — to be tried (in court)", "αξιωματούχος": "αξιωματούχος — official", "αρχή": "αρχή — authority", "νόμιμη": "νόμιμος — legitimate, lawful", "ηλεκτροσόκ": "ηλεκτροσόκ — electric shock", "ένταση": "ένταση — intensity", "βολτ": "βολτ — volt", "ιδρώνοντας": "ιδρώνω — to sweat", "διαμαρτυρόμενοι": "διαμαρτύρομαι — to protest", "υπακοή": "υπακοή — obedience", "αισθητά": "αισθητά — noticeably", "εγκρινόταν": "εγκρίνομαι — to be approved", "δίδαγμα": "δίδαγμα — lesson, moral", "προβληματίζει": "προβληματίζω — to trouble, to make (someone) think"},
})

ITEMS.append({
 "id": "l159-c1-marshmallow", "title": "Ένα ζαχαρωτό τώρα ή δύο αργότερα;", "title_en": "One marshmallow now or two later?", "type": "interview", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από ραδιοφωνική συνέντευξη με μια αναπτυξιακή ψυχολόγο για το λεγόμενο «τεστ του ζαχαρωτού».",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς ήταν το τεστ του ζαχαρωτού;", "What exactly was the marshmallow test?"),
  L("Ψυχολόγος", "f", "Στα τέλη της δεκαετίας του 1960, ο ψυχολόγος Γουόλτερ Μίσελ έφερνε παιδιά προσχολικής ηλικίας σε ένα δωμάτιο στο Στάνφορντ και τους πρότεινε μια συμφωνία: μπορούσαν να φάνε ένα γλυκό αμέσως, ή να περιμένουν μόνα τους μέχρι να γυρίσει ο ερευνητής και να πάρουν δύο. Η αναμονή μπορούσε να κρατήσει ως και είκοσι λεπτά.", "In the late 1960s, the psychologist Walter Mischel brought preschool children into a room at Stanford and offered them a deal: they could eat one sweet immediately, or wait alone until the researcher came back and get two. The wait could last up to twenty minutes."),
  L("Δημοσιογράφος", "m", "Και τι έκαναν τα παιδιά;", "And what did the children do?"),
  L("Ψυχολόγος", "f", "Άλλα το έτρωγαν μόλις έκλεινε η πόρτα. Άλλα έκλειναν τα μάτια, τραγουδούσαν ή γύριζαν την πλάτη στο γλυκό. Αυτές οι στρατηγικές ήταν που ενδιέφεραν πρώτα τον Μίσελ: όχι η θέληση, αλλά το πώς αποσπάμε την προσοχή μας από τον πειρασμό. Χρόνια αργότερα, οι ερευνητές βρήκαν ότι όσα παιδιά είχαν περιμένει περισσότερο είχαν κατά μέσο όρο καλύτερες σχολικές επιδόσεις, και από τότε το τεστ έγινε διάσημο ως πρόβλεψη της επιτυχίας στη ζωή.", "Some ate it as soon as the door closed. Others closed their eyes, sang, or turned their backs on the sweet. These strategies were what first interested Mischel: not willpower, but how we distract our attention from temptation. Years later, the researchers found that the children who had waited longer had, on average, better school results, and from then on the test became famous as a predictor of success in life."),
  L("Δημοσιογράφος", "m", "Ισχύει αυτό;", "Is that true?"),
  L("Ψυχολόγος", "f", "Πολύ λιγότερο απ' όσο νομίζαμε. Μια μεγαλύτερη μελέτη του 2018, με πιο ποικίλο δείγμα, βρήκε ότι η σχέση ήταν πολύ ασθενέστερη και εξηγούνταν σε μεγάλο βαθμό από το οικογενειακό και οικονομικό περιβάλλον των παιδιών. Και μια άλλη μελέτη έδειξε ότι τα παιδιά περίμεναν λιγότερο όταν ο ερευνητής είχε αθετήσει νωρίτερα μια υπόσχεσή του. Δηλαδή, το να μην περιμένεις δεν είναι πάντα έλλειψη αυτοελέγχου· μπορεί να είναι λογική αντίδραση σε έναν κόσμο που δεν σου δίνει λόγους να εμπιστεύεσαι.", "Much less than we thought. A larger study in 2018, with a more varied sample, found that the link was much weaker and was largely explained by the children's family and economic background. And another study showed that children waited less when the researcher had earlier broken a promise. In other words, not waiting is not always a lack of self-control; it can be a rational response to a world that gives you no reason to trust."),
 ],
 "questions": [
  Q("Ποια συμφωνία πρότεινε ο Μίσελ στα παιδιά;", ["Να λύσουν έναν γρίφο για να πάρουν γλυκό", "Να φάνε ένα γλυκό αμέσως ή να περιμένουν και να πάρουν δύο", "Να μοιραστούν το γλυκό με ένα άλλο παιδί", "Να διαλέξουν ανάμεσα σε γλυκό και παιχνίδι"], 1, "μπορούσαν να φάνε ένα γλυκό αμέσως, ή να περιμένουν μόνα τους μέχρι να γυρίσει ο ερευνητής και να πάρουν δύο"),
  Q("Τι ενδιέφερε πρώτα τον Μίσελ;", ["Η θέληση των παιδιών", "Οι στρατηγικές με τις οποίες αποσπάμε την προσοχή μας από τον πειρασμό", "Οι σχολικοί βαθμοί", "Η σχέση των παιδιών με τους γονείς"], 1, "το πώς αποσπάμε την προσοχή μας από τον πειρασμό"),
  Q("Τι βρήκε η μελέτη του 2018;", ["Ότι η σχέση με την επιτυχία ήταν ακόμη ισχυρότερη", "Ότι η σχέση ήταν πολύ ασθενέστερη και εξηγούνταν σε μεγάλο βαθμό από το οικογενειακό και οικονομικό περιβάλλον", "Ότι τα κορίτσια περίμεναν περισσότερο", "Ότι το τεστ δεν μπορεί να επαναληφθεί"], 1, "η σχέση ήταν πολύ ασθενέστερη"),
  Q("Πώς ερμηνεύει η ψυχολόγος το ότι κάποια παιδιά δεν περιμένουν;", ["Ως σημάδι τεμπελιάς", "Ως έλλειψη ευφυΐας", "Ως πιθανή λογική αντίδραση σε έναν κόσμο που δεν τους δίνει λόγους να εμπιστεύονται", "Ως αποτέλεσμα κακής διατροφής"], 2, "μπορεί να είναι λογική αντίδραση σε έναν κόσμο που δεν σου δίνει λόγους να εμπιστεύεσαι"),
 ],
 "gloss": {"αναπτυξιακή": "αναπτυξιακός — developmental", "ζαχαρωτού": "ζαχαρωτό — marshmallow, sweet", "προσχολικής ηλικίας": "προσχολική ηλικία — preschool age", "αναμονή": "αναμονή — wait", "στρατηγικές": "στρατηγική — strategy", "θέληση": "θέληση — willpower", "αποσπάμε": "αποσπώ (την προσοχή) — to distract", "πειρασμό": "πειρασμός — temptation", "επιδόσεις": "επίδοση — performance, results", "ποικίλο": "ποικίλος — varied", "δείγμα": "δείγμα — sample", "ασθενέστερη": "ασθενής — weak; ασθενέστερος = weaker", "αθετήσει": "αθετώ (μια υπόσχεση) — to break (a promise)", "αυτοελέγχου": "αυτοέλεγχος — self-control"},
})

rnd = random.Random(159)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-159.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
