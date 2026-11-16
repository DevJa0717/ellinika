# Source for library/listening/listening-36.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l36.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []


ITEMS.append({
 "id": "l36-ann-dioryga", "title": "Διασχίζοντας τη Διώρυγα της Κορίνθου", "title_en": "Crossing the Corinth Canal", "type": "announcement", "level": "B2",
 "context_el": "Θα ακούσετε μια ανακοίνωση σε ένα τουριστικό σκάφος λίγο πριν μπει στη Διώρυγα της Κορίνθου.",
 "script": [
  L("Ξεναγός", "f", "Αγαπητοί επιβάτες, σε λίγα λεπτά θα μπούμε στη Διώρυγα της Κορίνθου. Το κανάλι έχει μήκος έξι χιλιόμετρα και τετρακόσια μέτρα, ενώ τα κάθετα τοιχώματά του φτάνουν σε ύψος περίπου ογδόντα μέτρων. Η διέλευση θα διαρκέσει περίπου σαράντα λεπτά.", "Dear passengers, in a few minutes we will enter the Corinth Canal. The canal is six kilometres and four hundred metres long, while its vertical walls reach a height of about eighty metres. The crossing will last about forty minutes."),
  L("Ξεναγός", "f", "Την ιδέα να ενωθούν οι δύο θάλασσες την είχαν ήδη οι αρχαίοι. Ο αυτοκράτορας Νέρων ξεκίνησε μάλιστα τις εργασίες, αλλά αυτές εγκαταλείφθηκαν. Για αιώνες τα πλοία σέρνονταν πάνω από τον ισθμό, σε έναν πέτρινο δρόμο, τον Δίολκο. Η διώρυγα που βλέπετε εγκαινιάστηκε τελικά το 1893.", "The ancients already had the idea of joining the two seas. The emperor Nero even started the works, but they were abandoned. For centuries ships were dragged over the isthmus on a stone road, the Diolkos. The canal you see was finally inaugurated in 1893."),
  L("Ξεναγός", "f", "Για την ασφάλειά σας, παρακαλούμε να μη σκύβετε έξω από την κουπαστή και να κρατάτε τα παιδιά κοντά σας. Μπορείτε να βγάζετε φωτογραφίες από το πάνω κατάστρωμα, αλλά χωρίς φλας, γιατί ενοχλεί τον καπετάνιο κάτω από τη γέφυρα. Καλή διέλευση!", "For your safety, please do not lean out over the rail and keep children close to you. You may take photographs from the upper deck, but without flash, because it disturbs the captain under the bridge. Enjoy the crossing!"),
 ],
 "questions": [
  Q("Πόσο θα διαρκέσει η διέλευση;", ["Δέκα λεπτά", "Περίπου σαράντα λεπτά", "Δύο ώρες", "Έξι ώρες"], 1, "Η διέλευση θα διαρκέσει περίπου σαράντα λεπτά"),
  Q("Τι ήταν ο Δίολκος;", ["Ένα αρχαίο λιμάνι", "Ένας πέτρινος δρόμος όπου σέρνονταν τα πλοία", "Ένας ναός στον ισθμό", "Ένα αρχαίο κανάλι"], 1, "τα πλοία σέρνονταν πάνω από τον ισθμό, σε έναν πέτρινο δρόμο"),
  Q("Τι ζητείται από τους επιβάτες;", ["Να μείνουν στις καμπίνες", "Να μη σκύβουν έξω από την κουπαστή", "Να μη βγάζουν καθόλου φωτογραφίες", "Να φορέσουν σωσίβια"], 1, "να μη σκύβετε έξω από την κουπαστή"),
 ],
 "gloss": {"Διώρυγα": "διώρυγα — canal", "μήκος": "μήκος — length", "κάθετα": "κάθετος — vertical", "τοιχώματά": "τοίχωμα — wall, side", "διέλευση": "διέλευση — passage, crossing", "εγκαταλείφθηκαν": "εγκαταλείπομαι — to be abandoned", "σέρνονταν": "σέρνομαι — to be dragged", "ισθμό": "ισθμός — isthmus", "εγκαινιάστηκε": "εγκαινιάζομαι — to be inaugurated", "σκύβετε": "σκύβω — to lean, bend", "κουπαστή": "κουπαστή — ship's rail", "κατάστρωμα": "κατάστρωμα — deck"},
})

ITEMS.append({
 "id": "l36-vm-kalorifer", "title": "Μήνυμα από τον διαχειριστή της πολυκατοικίας", "title_en": "A message from the building manager", "type": "voicemail", "level": "B2",
 "context_el": "Θα ακούσετε ένα μήνυμα στον τηλεφωνητή σας από τον διαχειριστή της πολυκατοικίας όπου μένετε.",
 "script": [
  L("Διαχειριστής", "m", "Καλησπέρα, ο Παύλος είμαι, ο διαχειριστής. Σας τηλεφωνώ για τη θέρμανση. Στη γενική συνέλευση αποφασίσαμε να ανάψουμε τα καλοριφέρ από την πρώτη Νοεμβρίου, αλλά πρώτα πρέπει να γεμίσουμε τη δεξαμενή με πετρέλαιο.", "Good evening, it's Pavlos, the building manager. I'm calling about the heating. At the general meeting we decided to turn the radiators on from the first of November, but first we need to fill the tank with heating oil."),
  L("Διαχειριστής", "m", "Η προκαταβολή για το πετρέλαιο βγαίνει για το διαμέρισμά σας εκατόν ογδόντα ευρώ. Θα σας παρακαλούσα να την καταθέσετε στον λογαριασμό της πολυκατοικίας μέχρι την Παρασκευή, γιατί αλλιώς ο προμηθευτής δεν θα μας κρατήσει την τιμή.", "The advance for the heating oil for your flat comes to one hundred and eighty euros. I'd ask you to deposit it into the building's account by Friday, because otherwise the supplier won't hold the price for us."),
  L("Διαχειριστής", "m", "Επίσης, την Πέμπτη το πρωί θα έρθει ο τεχνικός να καθαρίσει τον καυστήρα. Θα κλείσει το νερό για δύο περίπου ώρες, από τις εννιά μέχρι τις έντεκα. Ευχαριστώ, και ό,τι χρειαστείτε, με βρίσκετε στο δεύτερο.", "Also, on Thursday morning the technician will come to clean the boiler. He'll turn off the water for about two hours, from nine to eleven. Thanks, and if you need anything, you'll find me on the second floor."),
 ],
 "questions": [
  Q("Τι πρέπει να γίνει πριν ανάψουν τα καλοριφέρ;", ["Να γίνει νέα συνέλευση", "Να γεμίσει η δεξαμενή με πετρέλαιο", "Να αλλάξει ο καυστήρας", "Να πληρωθεί ο τεχνικός"], 1, "πρώτα πρέπει να γεμίσουμε τη δεξαμενή με πετρέλαιο"),
  Q("Γιατί πρέπει να πληρωθεί η προκαταβολή μέχρι την Παρασκευή;", ["Γιατί φεύγει ο διαχειριστής", "Γιατί αλλιώς ο προμηθευτής δεν θα κρατήσει την τιμή", "Γιατί κλείνει η τράπεζα", "Γιατί θα ανέβει ο φόρος"], 1, "αλλιώς ο προμηθευτής δεν θα μας κρατήσει την τιμή"),
  Q("Τι θα γίνει την Πέμπτη το πρωί;", ["Θα κοπεί το ρεύμα", "Θα καθαριστεί ο καυστήρας και θα κλείσει το νερό", "Θα γίνει η συνέλευση", "Θα έρθει το πετρέλαιο"], 1, "θα έρθει ο τεχνικός να καθαρίσει τον καυστήρα. Θα κλείσει το νερό"),
 ],
 "gloss": {"διαχειριστή": "διαχειριστής — building manager", "πολυκατοικίας": "πολυκατοικία — apartment block", "θέρμανση": "θέρμανση — heating", "γενική συνέλευση": "γενική συνέλευση — general meeting", "καλοριφέρ": "καλοριφέρ — radiator, central heating", "δεξαμενή": "δεξαμενή — tank", "πετρέλαιο": "πετρέλαιο — heating oil", "προκαταβολή": "προκαταβολή — advance payment", "προμηθευτής": "προμηθευτής — supplier", "καυστήρα": "καυστήρας — boiler, burner"},
})

ITEMS.append({
 "id": "l36-dia-koureio", "title": "Στο κουρείο", "title_en": "At the barber's", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε έναν διάλογο σε ένα κουρείο της γειτονιάς.",
 "script": [
  L("Κουρέας", "m", "Καλώς τον! Πάλι το ίδιο, κοντά στα πλάγια και λίγο πιο μακριά από πάνω;", "Welcome! The same again, short on the sides and a bit longer on top?"),
  L("Πελάτης", "m", "Όχι, αυτή τη φορά θέλω κάτι διαφορετικό. Την άλλη εβδομάδα παντρεύεται ο αδελφός μου και είμαι κουμπάρος. Η νύφη μού είπε ότι στις φωτογραφίες δεν θέλει να φαίνομαι σαν να μόλις βγήκα από τον στρατό.", "No, this time I want something different. My brother is getting married next week and I'm the best man. The bride told me that in the photos she doesn't want me to look as if I've just left the army."),
  L("Κουρέας", "m", "Χα! Τότε ας μην κόψουμε πολύ σήμερα. Θα το καθαρίσω λίγο στον σβέρκο και γύρω από τα αυτιά, και τα υπόλοιπα θα τα αφήσουμε να μεγαλώσουν. Έλα την παραμονή του γάμου να το φρεσκάρουμε. Και τα γένια;", "Ha! Then let's not cut much today. I'll tidy it a little at the nape and around the ears, and we'll let the rest grow. Come the day before the wedding and we'll freshen it up. And the beard?"),
  L("Πελάτης", "m", "Τα γένια τα κρατάω, αλλά θέλω να τα κάνεις πιο κοντά και πιο καθαρά στο περίγραμμα. Πόσο θα μου κοστίσει το πακέτο, μαλλιά και γένια, δύο φορές;", "I'm keeping the beard, but I want you to make it shorter and neater at the edges. How much will the package cost me, hair and beard, twice?"),
  L("Κουρέας", "m", "Για τον κουμπάρο, ειδική τιμή: τριάντα ευρώ και τα δύο. Και να μου φέρεις κουφέτα!", "For the best man, a special price: thirty euros for both. And bring me some sugared almonds!"),
 ],
 "questions": [
  Q("Γιατί θέλει ο πελάτης κάτι διαφορετικό αυτή τη φορά;", ["Γιατί πάει σε συνέντευξη για δουλειά", "Γιατί είναι κουμπάρος στον γάμο του αδελφού του", "Γιατί δεν του άρεσε το προηγούμενο κούρεμα", "Γιατί πάει στον στρατό"], 1, "παντρεύεται ο αδελφός μου και είμαι κουμπάρος"),
  Q("Τι προτείνει ο κουρέας;", ["Να κόψουν πολύ κοντά σήμερα", "Να κόψουν λίγο τώρα και να ξανάρθει την παραμονή του γάμου", "Να ξυρίσει τα γένια", "Να βάψει τα μαλλιά"], 1, "Έλα την παραμονή του γάμου να το φρεσκάρουμε"),
  Q("Τι ζητάει ο κουρέας στο τέλος, αστειευόμενος;", ["Φιλοδώρημα", "Να του φέρει κουφέτα", "Πρόσκληση στον γάμο", "Να πληρώσει από πριν"], 1, "Και να μου φέρεις κουφέτα"),
 ],
 "gloss": {"κουρείο": "κουρείο — barber's shop", "πλάγια": "πλάγια — sides", "κουμπάρος": "κουμπάρος — best man, wedding sponsor", "νύφη": "νύφη — bride", "σβέρκο": "σβέρκος — nape of the neck", "παραμονή": "παραμονή — eve, day before", "να το φρεσκάρουμε": "φρεσκάρω — to freshen up", "γένια": "γένια — beard", "περίγραμμα": "περίγραμμα — outline, edges", "κουφέτα": "κουφέτο — sugared almond"},
})

ITEMS.append({
 "id": "l36-dia-katafygio", "title": "Κράτηση σε καταφύγιο του Ολύμπου", "title_en": "Booking a refuge on Mount Olympus", "type": "dialogue", "level": "B2",
 "context_el": "Θα ακούσετε μια τηλεφωνική συνομιλία ανάμεσα σε έναν ορειβάτη και τη φύλακα ενός καταφυγίου στον Όλυμπο.",
 "script": [
  L("Ορειβάτης", "m", "Καλημέρα σας. Θα θέλαμε να κλείσουμε δύο κρεβάτια για το Σάββατο, δεκαπέντε Ιουλίου. Σκοπεύουμε να ανεβούμε την Κυριακή στον Μύτικα.", "Good morning. We'd like to book two beds for Saturday, the fifteenth of July. We plan to climb Mytikas on Sunday."),
  L("Φύλακας", "f", "Για το Σάββατο έχω μόνο δύο θέσεις στον κοιτώνα, όχι σε δωμάτιο. Σας κάνουν; Πρέπει όμως να ξέρετε ότι η τελευταία ανάβαση στον Μύτικα είναι αναρρίχηση, όχι απλή πεζοπορία. Έχετε εμπειρία σε βράχο;", "For Saturday I only have two places in the dormitory, not in a room. Do they suit you? But you should know that the last climb to Mytikas is scrambling, not a simple hike. Do you have experience on rock?"),
  L("Ορειβάτης", "m", "Ναι, έχουμε ανέβει στον Σμόλικα και στην Γκιώνα, και έχουμε κράνη. Τι ώρα πρέπει να ξεκινήσουμε από τα Πριόνια για να φτάσουμε σε σας;", "Yes, we've climbed Smolikas and Giona, and we have helmets. What time should we start from Prionia to reach you?"),
  L("Φύλακας", "f", "Θέλει περίπου τρεις ώρες. Ξεκινήστε το αργότερο στις δύο, γιατί το απόγευμα συχνά πιάνουν καταιγίδες. Την Κυριακή να είστε έτοιμοι να φύγετε από το καταφύγιο στις έξι το πρωί. Και φέρτε υπνόσακο ή σεντόνι· κουβέρτες έχουμε, αλλά όχι σεντόνια.", "It takes about three hours. Start by two at the latest, because in the afternoon storms often break. On Sunday be ready to leave the refuge at six in the morning. And bring a sleeping bag or a sheet; we have blankets, but not sheets."),
 ],
 "questions": [
  Q("Τι διαθεσιμότητα έχει το καταφύγιο για το Σάββατο;", ["Ένα δίκλινο δωμάτιο", "Δύο θέσεις στον κοιτώνα", "Καμία θέση", "Μόνο θέσεις για σκηνή"], 1, "έχω μόνο δύο θέσεις στον κοιτώνα"),
  Q("Γιατί ρωτάει η φύλακας για εμπειρία σε βράχο;", ["Γιατί το μονοπάτι προς το καταφύγιο είναι επικίνδυνο", "Γιατί η τελευταία ανάβαση στον Μύτικα είναι αναρρίχηση", "Γιατί απαιτείται δίπλωμα", "Γιατί το καταφύγιο οργανώνει μαθήματα"], 1, "η τελευταία ανάβαση στον Μύτικα είναι αναρρίχηση"),
  Q("Γιατί πρέπει να ξεκινήσουν το αργότερο στις δύο;", ["Γιατί κλείνει το καταφύγιο", "Γιατί το απόγευμα συχνά πιάνουν καταιγίδες", "Γιατί σκοτεινιάζει στις τέσσερις", "Γιατί το φαγητό σερβίρεται νωρίς"], 1, "το απόγευμα συχνά πιάνουν καταιγίδες"),
 ],
 "gloss": {"ορειβάτη": "ορειβάτης — mountaineer", "φύλακα": "φύλακας — warden, keeper", "καταφυγίου": "καταφύγιο — mountain refuge", "κοιτώνα": "κοιτώνας — dormitory", "ανάβαση": "ανάβαση — ascent, climb", "αναρρίχηση": "αναρρίχηση — climbing, scrambling", "πεζοπορία": "πεζοπορία — hiking", "κράνη": "κράνος — helmet", "καταιγίδες": "καταιγίδα — thunderstorm", "υπνόσακο": "υπνόσακος — sleeping bag"},
})

ITEMS.append({
 "id": "l36-mono-arkadia", "title": "Πίσω στο χωριό της Αρκαδίας", "title_en": "Back to the village in Arcadia", "type": "monologue", "level": "B2",
 "context_el": "Θα ακούσετε έναν άντρα να μιλάει για την απόφασή του να επιστρέψει στο χωριό του.",
 "script": [
  L("Γιάννης", "m", "Δούλευα δεκαπέντε χρόνια σε μια εταιρεία πληροφορικής στην Αθήνα. Καλός μισθός, αλλά έφευγα από το σπίτι στις επτά και γύριζα στις εννιά το βράδυ. Τα παιδιά τα έβλεπα μόνο κοιμισμένα. Στην πανδημία, όταν δουλεύαμε όλοι από το σπίτι, ήρθαμε για λίγες εβδομάδες στο πατρικό μου, σε ένα χωριό της Αρκαδίας, και δεν ξαναφύγαμε.", "I worked for fifteen years at an IT company in Athens. A good salary, but I left home at seven and came back at nine in the evening. I only saw the children asleep. During the pandemic, when we were all working from home, we came for a few weeks to my family home, in a village in Arcadia, and we never left again."),
  L("Γιάννης", "m", "Συνεχίζω να δουλεύω εξ αποστάσεως τρεις μέρες την εβδομάδα. Τις υπόλοιπες ασχολούμαι με τις καστανιές του παππού μου, που ήταν παρατημένες είκοσι χρόνια. Τις κλαδέψαμε, καθαρίσαμε τα χωράφια, και πέρσι πουλήσαμε τα πρώτα μας κάστανα σε έναν συνεταιρισμό.", "I still work remotely three days a week. The rest of the time I look after my grandfather's chestnut trees, which had been abandoned for twenty years. We pruned them, cleared the fields, and last year we sold our first chestnuts to a cooperative."),
  L("Γιάννης", "m", "Δεν είναι όλα ρόδινα. Το σχολείο έχει μόνο έντεκα μαθητές, ο γιατρός έρχεται δύο φορές την εβδομάδα, και τον χειμώνα το χιόνι μάς κλείνει μερικές φορές στο σπίτι. Αλλά τώρα τρώμε όλοι μαζί κάθε μεσημέρι. Αυτό δεν το αλλάζω με κανέναν μισθό.", "Not everything is rosy. The school has only eleven pupils, the doctor comes twice a week, and in winter the snow sometimes shuts us in the house. But now we all eat together every midday. I wouldn't swap that for any salary."),
 ],
 "questions": [
  Q("Ποιο ήταν το πρόβλημα με τη δουλειά του στην Αθήνα;", ["Ο χαμηλός μισθός", "Οι πολλές ώρες, που δεν του άφηναν χρόνο για τα παιδιά", "Η απόσταση από τη θάλασσα", "Οι κακές σχέσεις με τους συναδέλφους"], 1, "Τα παιδιά τα έβλεπα μόνο κοιμισμένα"),
  Q("Με τι ασχολείται τις μέρες που δεν δουλεύει εξ αποστάσεως;", ["Με τουρισμό", "Με τις καστανιές του παππού του", "Με μελισσοκομία", "Με το σχολείο του χωριού"], 1, "ασχολούμαι με τις καστανιές του παππού μου"),
  Q("Ποιο από τα παρακάτω ΔΕΝ αναφέρει ως δυσκολία;", ["Το μικρό σχολείο", "Την έλλειψη ίντερνετ", "Τον γιατρό που έρχεται δύο φορές την εβδομάδα", "Το χιόνι τον χειμώνα"], 1, "Το σχολείο έχει μόνο έντεκα μαθητές, ο γιατρός έρχεται δύο φορές την εβδομάδα"),
 ],
 "gloss": {"πληροφορικής": "πληροφορική — IT, computing", "πατρικό": "πατρικό — family home", "εξ αποστάσεως": "εξ αποστάσεως — remotely", "καστανιές": "καστανιά — chestnut tree", "παρατημένες": "παρατημένος — abandoned, neglected", "Τις κλαδέψαμε": "κλαδεύω — to prune", "χωράφια": "χωράφι — field", "συνεταιρισμό": "συνεταιρισμός — cooperative", "ρόδινα": "ρόδινος — rosy"},
})

ITEMS.append({
 "id": "l36-rep-ompreles", "title": "Οι «Ομπρέλες» της Θεσσαλονίκης", "title_en": "Thessaloniki's 'Umbrellas'", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ από τη Νέα Παραλία της Θεσσαλονίκης.",
 "script": [
  L("Δημοσιογράφος", "f", "Είναι Κυριακή απόγευμα, και η Νέα Παραλία της Θεσσαλονίκης είναι γεμάτη ποδηλάτες, οικογένειες με καρότσια και ανθρώπους που κάνουν τζόκινγκ. Όλοι, κάποια στιγμή, σταματούν μπροστά στις «Ομπρέλες», το γλυπτό του Γιώργου Ζογγολόπουλου, που έγινε ένα από τα σύμβολα της πόλης.", "It's Sunday afternoon, and Thessaloniki's New Waterfront is full of cyclists, families with pushchairs and people jogging. Everyone, at some point, stops in front of the 'Umbrellas', the sculpture by Giorgos Zongolopoulos, which has become one of the city's symbols."),
  L("Δημοσιογράφος", "f", "Το έργο τοποθετήθηκε εδώ το 1997, όταν η Θεσσαλονίκη ήταν Πολιτιστική Πρωτεύουσα της Ευρώπης. Οι ψηλές μεταλλικές ομπρέλες, που μοιάζουν να αιωρούνται στον αέρα, αντανακλούν τον ουρανό και τη θάλασσα και αλλάζουν όψη ανάλογα με το φως της ημέρας.", "The work was placed here in 1997, when Thessaloniki was European Capital of Culture. The tall metal umbrellas, which seem to float in the air, reflect the sky and the sea and change their appearance depending on the daylight."),
  L("Περαστικός", "m", "Εδώ έκανα πρόταση γάμου στη γυναίκα μου, πριν από δεκαπέντε χρόνια, στο ηλιοβασίλεμα. Τώρα φέρνω τα παιδιά μου. Για εμάς τους Θεσσαλονικείς, δεν είναι απλώς ένα γλυπτό· είναι σημείο συνάντησης. «Τα λέμε στις Ομπρέλες» λέμε, και όλοι ξέρουν πού.", "This is where I proposed to my wife, fifteen years ago, at sunset. Now I bring my children. For us people of Thessaloniki, it isn't just a sculpture; it's a meeting point. 'See you at the Umbrellas', we say, and everyone knows where."),
 ],
 "questions": [
  Q("Πότε τοποθετήθηκε το γλυπτό;", ["Το 2004, για τους Ολυμπιακούς Αγώνες", "Το 1997, όταν η πόλη ήταν Πολιτιστική Πρωτεύουσα", "Πριν από δεκαπέντε χρόνια", "Μετά τον πόλεμο"], 1, "Το έργο τοποθετήθηκε εδώ το 1997"),
  Q("Τι λέει το ρεπορτάζ για την όψη των ομπρελών;", ["Είναι βαμμένες σε έντονα χρώματα", "Αλλάζει ανάλογα με το φως της ημέρας", "Φωτίζονται μόνο τη νύχτα", "Είναι καλυμμένες με ύφασμα"], 1, "αλλάζουν όψη ανάλογα με το φως της ημέρας"),
  Q("Τι σημαίνουν οι «Ομπρέλες» για τον περαστικό;", ["Ένα έργο που δεν καταλαβαίνει", "Ένα σημείο συνάντησης και προσωπικών αναμνήσεων", "Ένα τουριστικό αξιοθέατο μόνο για ξένους", "Μια σπατάλη δημόσιου χρήματος"], 1, "δεν είναι απλώς ένα γλυπτό· είναι σημείο συνάντησης"),
 ],
 "gloss": {"καρότσια": "καρότσι — pushchair", "γλυπτό": "γλυπτό — sculpture", "σύμβολα": "σύμβολο — symbol", "τοποθετήθηκε": "τοποθετούμαι — to be placed", "μεταλλικές": "μεταλλικός — metal", "να αιωρούνται": "αιωρούμαι — to float, hover", "αντανακλούν": "αντανακλώ — to reflect", "όψη": "όψη — appearance", "πρόταση γάμου": "πρόταση γάμου — marriage proposal", "ηλιοβασίλεμα": "ηλιοβασίλεμα — sunset"},
})

ITEMS.append({
 "id": "l36-rep-gefyra-riou", "title": "Η γέφυρα Ρίου–Αντιρρίου", "title_en": "The Rio–Antirrio bridge", "type": "report", "level": "B2",
 "context_el": "Θα ακούσετε ένα ρεπορτάζ για τη γέφυρα που ενώνει την Πελοπόννησο με τη Δυτική Στερεά Ελλάδα.",
 "script": [
  L("Δημοσιογράφος", "m", "Για δεκαετίες, όποιος ήθελε να πάει από την Πάτρα στη Ναύπακτο έπρεπε να περιμένει το φέρι μποτ, και τις μέρες με θυελλώδεις ανέμους τα δρομολόγια ακυρώνονταν. Από το καλοκαίρι του 2004, λίγο πριν από τους Ολυμπιακούς Αγώνες, η διαδρομή γίνεται σε λίγα λεπτά πάνω από τη γέφυρα «Χαρίλαος Τρικούπης», με συνολικό μήκος σχεδόν τρία χιλιόμετρα.", "For decades, anyone who wanted to go from Patras to Nafpaktos had to wait for the ferry, and on days with gale-force winds the crossings were cancelled. Since the summer of 2004, just before the Olympic Games, the journey takes a few minutes over the 'Charilaos Trikoupis' bridge, with a total length of almost three kilometres."),
  L("Μηχανικός", "f", "Η κατασκευή ήταν τεράστια πρόκληση. Ο βυθός εκεί είναι βαθύς, το έδαφος μαλακό, και η περιοχή έχει έντονη σεισμική δραστηριότητα. Επιπλέον, οι δύο ακτές απομακρύνονται η μία από την άλλη κατά μερικά χιλιοστά τον χρόνο. Γι' αυτό τα βάθρα δεν είναι πακτωμένα στο έδαφος· απλώς ακουμπούν στον βυθό, ώστε σε έναν σεισμό να μπορούν να μετακινηθούν χωρίς να σπάσουν.", "The construction was an enormous challenge. The seabed there is deep, the ground soft, and the area has intense seismic activity. In addition, the two coasts are moving away from each other by a few millimetres a year. That's why the piers aren't fixed into the ground; they simply rest on the seabed, so that in an earthquake they can shift without breaking."),
  L("Δημοσιογράφος", "m", "Σήμερα η γέφυρα θεωρείται από τα σημαντικότερα τεχνικά έργα της χώρας, και τη νύχτα, φωτισμένη, φαίνεται από χιλιόμετρα μακριά. Τα φέρι μποτ πάντως δεν σταμάτησαν· πολλοί οδηγοί τα προτιμούν ακόμη, γιατί είναι φθηνότερα από τα διόδια της γέφυρας.", "Today the bridge is considered one of the country's most important engineering works, and at night, lit up, it can be seen from kilometres away. The ferries, however, didn't stop; many drivers still prefer them, because they are cheaper than the bridge tolls."),
 ],
 "questions": [
  Q("Ποιο ήταν το πρόβλημα πριν από τη γέφυρα;", ["Δεν υπήρχε καμία σύνδεση", "Με θυελλώδεις ανέμους τα δρομολόγια του φέρι μποτ ακυρώνονταν", "Τα φέρι μποτ ήταν πολύ ακριβά", "Ο δρόμος ήταν κλειστός τον χειμώνα"], 1, "τις μέρες με θυελλώδεις ανέμους τα δρομολόγια ακυρώνονταν"),
  Q("Γιατί τα βάθρα δεν είναι πακτωμένα στο έδαφος;", ["Για να κοστίσουν λιγότερο", "Για να μπορούν να μετακινηθούν σε σεισμό χωρίς να σπάσουν", "Γιατί ο βυθός είναι πολύ ρηχός", "Για να περνούν τα πλοία"], 1, "ώστε σε έναν σεισμό να μπορούν να μετακινηθούν χωρίς να σπάσουν"),
  Q("Γιατί πολλοί οδηγοί προτιμούν ακόμη το φέρι μποτ;", ["Γιατί φοβούνται τη γέφυρα", "Γιατί είναι φθηνότερο από τα διόδια", "Γιατί είναι πιο γρήγορο", "Γιατί η γέφυρα κλείνει τη νύχτα"], 1, "είναι φθηνότερα από τα διόδια της γέφυρας"),
 ],
 "gloss": {"φέρι μποτ": "φέρι μποτ — ferry", "θυελλώδεις": "θυελλώδης — gale-force, stormy", "δρομολόγια": "δρομολόγιο — scheduled crossing, route", "πρόκληση": "πρόκληση — challenge", "βυθός": "βυθός — seabed", "σεισμική δραστηριότητα": "σεισμική δραστηριότητα — seismic activity", "απομακρύνονται": "απομακρύνομαι — to move away", "χιλιοστά": "χιλιοστό — millimetre", "βάθρα": "βάθρο — pier, pylon base", "πακτωμένα": "πακτωμένος — fixed, anchored", "διόδια": "διόδια — tolls"},
})

ITEMS.append({
 "id": "l36-int-pilotos", "title": "Πιλότος πυροσβεστικού αεροσκάφους", "title_en": "A firefighting-plane pilot", "type": "interview", "level": "B2",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια πιλότο της Πολεμικής Αεροπορίας που πετά με πυροσβεστικό αεροσκάφος.",
 "script": [
  L("Δημοσιογράφος", "m", "Πώς είναι μια μέρα σας το καλοκαίρι, στην αντιπυρική περίοδο;", "What is one of your days like in summer, during the fire season?"),
  L("Πιλότος", "f", "Είμαστε σε ετοιμότητα από την ανατολή μέχρι τη δύση του ηλίου. Μπορεί να περάσει όλη η μέρα χωρίς τίποτα, και ξαφνικά να χτυπήσει το τηλέφωνο και σε δεκαπέντε λεπτά να είμαστε στον αέρα. Τις μέρες με πολύ αέρα και ζέστη, ξέρουμε από το πρωί ότι θα πετάξουμε.", "We're on standby from sunrise to sunset. A whole day can pass with nothing, and suddenly the phone rings and in fifteen minutes we're in the air. On days with strong wind and heat, we know from the morning that we'll fly."),
  L("Δημοσιογράφος", "m", "Πώς γεμίζει το αεροσκάφος με νερό;", "How does the plane fill up with water?"),
  L("Πιλότος", "f", "Κατεβαίνουμε πολύ χαμηλά πάνω από τη θάλασσα ή από μια λίμνη και, χωρίς να σταματήσουμε, αγγίζουμε την επιφάνεια. Σε λίγα δευτερόλεπτα παίρνουμε αρκετούς τόνους νερό και ξαναπαίρνουμε ύψος. Το πιο δύσκολο είναι η ρίψη: ο καπνός κρύβει την ορατότητα, ο αέρας είναι γεμάτος αναταράξεις, και πρέπει να ρίξεις το νερό ακριβώς στο μέτωπο της φωτιάς. Μετά από μια τέτοια μέρα δεν νιώθεις ήρωας· νιώθεις κουρασμένος και σκέφτεσαι μόνο αν σώθηκαν τα σπίτια.", "We descend very low over the sea or a lake and, without stopping, touch the surface. In a few seconds we take on several tonnes of water and climb again. The hardest part is the drop: the smoke hides visibility, the air is full of turbulence, and you have to drop the water exactly on the fire front. After a day like that you don't feel like a hero; you feel tired and think only about whether the houses were saved."),
 ],
 "questions": [
  Q("Τι σημαίνει ότι είναι «σε ετοιμότητα»;", ["Ότι πετούν συνεχώς όλη τη μέρα", "Ότι πρέπει να μπορούν να απογειωθούν μέσα σε λίγα λεπτά", "Ότι κάνουν εκπαίδευση", "Ότι δουλεύουν μόνο τη νύχτα"], 1, "σε δεκαπέντε λεπτά να είμαστε στον αέρα"),
  Q("Πώς γεμίζει το αεροσκάφος με νερό;", ["Σε ειδικές δεξαμενές στο αεροδρόμιο", "Αγγίζοντας την επιφάνεια της θάλασσας χωρίς να σταματήσει", "Από πυροσβεστικά οχήματα", "Με ελικόπτερα"], 1, "χωρίς να σταματήσουμε, αγγίζουμε την επιφάνεια"),
  Q("Πώς νιώθει η πιλότος μετά από μια δύσκολη μέρα;", ["Σαν ήρωας", "Κουρασμένη και αγχωμένη για τα σπίτια", "Θυμωμένη με τους εμπρηστές", "Ενθουσιασμένη"], 1, "νιώθεις κουρασμένος και σκέφτεσαι μόνο αν σώθηκαν τα σπίτια"),
 ],
 "gloss": {"πιλότο": "πιλότος — pilot", "πυροσβεστικό αεροσκάφος": "πυροσβεστικό αεροσκάφος — firefighting plane", "αντιπυρική περίοδο": "αντιπυρική περίοδος — fire season", "ετοιμότητα": "ετοιμότητα — readiness, standby", "επιφάνεια": "επιφάνεια — surface", "ρίψη": "ρίψη — drop", "ορατότητα": "ορατότητα — visibility", "αναταράξεις": "αναταράξεις — turbulence", "μέτωπο": "μέτωπο — front (of a fire)", "ήρωας": "ήρωας — hero"},
})

ITEMS.append({
 "id": "l36-mono-kleisthenis", "title": "Ο Κλεισθένης και η γέννηση της δημοκρατίας", "title_en": "Cleisthenes and the birth of democracy", "type": "monologue", "level": "C1",
 "context_el": "Θα ακούσετε έναν ιστορικό να μιλάει σε μια διάλεξη για τις μεταρρυθμίσεις του Κλεισθένη στην αρχαία Αθήνα.",
 "script": [
  L("Ιστορικός", "m", "Όταν μιλάμε για την αθηναϊκή δημοκρατία, το πρώτο όνομα που έρχεται στο μυαλό είναι συνήθως ο Περικλής. Ωστόσο, τα θεμέλιά της τα έθεσε μισό αιώνα νωρίτερα, το 508 ή 507 π.Χ., ένας αριστοκράτης λιγότερο γνωστός στο ευρύ κοινό: ο Κλεισθένης.", "When we talk about Athenian democracy, the first name that comes to mind is usually Pericles. However, its foundations were laid half a century earlier, in 508 or 507 BC, by an aristocrat less known to the general public: Cleisthenes."),
  L("Ιστορικός", "m", "Μέχρι τότε, η πολιτική ζωή της Αθήνας κυριαρχούνταν από ισχυρές οικογένειες, που στηρίζονταν σε τοπικά δίκτυα πελατείας. Η ιδιοφυής κίνηση του Κλεισθένη ήταν να αναδιοργανώσει ολόκληρο τον πληθυσμό σε δέκα νέες φυλές. Κάθε φυλή περιλάμβανε περιοχές από τρεις διαφορετικές ζώνες της Αττικής, την πόλη, τα παράλια και την ενδοχώρα, ώστε κανένας τοπικός άρχοντας να μην μπορεί να ελέγξει μια ολόκληρη φυλή.", "Until then, Athens's political life was dominated by powerful families, who relied on local networks of patronage. Cleisthenes's ingenious move was to reorganise the entire population into ten new tribes. Each tribe included areas from three different zones of Attica, the city, the coast and the inland, so that no local lord could control a whole tribe."),
  L("Ιστορικός", "m", "Η βασική μονάδα έγινε ο δήμος, η τοπική κοινότητα, στην οποία ο πολίτης καταγραφόταν και από την οποία έπαιρνε, από τότε, και το όνομά του. Κάθε φυλή έστελνε πενήντα μέλη, που κληρώνονταν, στη νέα Βουλή των Πεντακοσίων. Στον Κλεισθένη αποδίδεται, αν και όχι με απόλυτη βεβαιότητα, και ο θεσμός του οστρακισμού.", "The basic unit became the deme, the local community, in which the citizen was registered and from which, from then on, he also took his name. Each tribe sent fifty members, chosen by lot, to the new Council of Five Hundred. The institution of ostracism is also attributed to Cleisthenes, though not with absolute certainty."),
  L("Ιστορικός", "m", "Δεν πρέπει, βέβαια, να εξιδανικεύουμε. Από αυτή τη δημοκρατία αποκλείονταν οι γυναίκες, οι δούλοι και οι μέτοικοι, δηλαδή η πλειονότητα των κατοίκων. Το ριζοσπαστικό όμως στοιχείο της παραμένει εντυπωσιακό: η ιδέα ότι η εξουσία δεν πηγάζει από την καταγωγή ή τον πλούτο, αλλά από το σύνολο των πολιτών.", "We shouldn't, of course, idealise it. Women, slaves and resident foreigners, that is the majority of the inhabitants, were excluded from this democracy. But its radical element remains impressive: the idea that power does not stem from birth or wealth, but from the citizen body as a whole."),
 ],
 "questions": [
  Q("Τι υποστηρίζει ο ομιλητής για τον Κλεισθένη;", ["Ότι ήταν μαθητής του Περικλή", "Ότι έθεσε τα θεμέλια της δημοκρατίας πριν από τον Περικλή", "Ότι ήταν ο πιο γνωστός Αθηναίος πολιτικός", "Ότι κατήργησε τη δημοκρατία"], 1, "τα θεμέλιά της τα έθεσε μισό αιώνα νωρίτερα"),
  Q("Ποιος ήταν ο σκοπός της αναδιοργάνωσης σε δέκα φυλές;", ["Να αυξηθεί ο στρατός", "Να μην μπορεί κανένας τοπικός άρχοντας να ελέγξει μια ολόκληρη φυλή", "Να μειωθούν οι φόροι", "Να χωριστεί η πόλη από την ύπαιθρο"], 1, "ώστε κανένας τοπικός άρχοντας να μην μπορεί να ελέγξει μια ολόκληρη φυλή"),
  Q("Πώς επιλέγονταν τα μέλη της Βουλής των Πεντακοσίων;", ["Με εκλογές", "Με κλήρωση", "Από τους αριστοκράτες", "Κληρονομικά"], 1, "πενήντα μέλη, που κληρώνονταν"),
  Q("Τι λέει ο ομιλητής για τον οστρακισμό;", ["Ότι τον εφηύρε σίγουρα ο Περικλής", "Ότι αποδίδεται στον Κλεισθένη, χωρίς απόλυτη βεβαιότητα", "Ότι δεν εφαρμόστηκε ποτέ", "Ότι καταργήθηκε από τον Κλεισθένη"], 1, "αποδίδεται, αν και όχι με απόλυτη βεβαιότητα"),
 ],
 "gloss": {"μεταρρυθμίσεις": "μεταρρύθμιση — reform", "θεμέλιά": "θεμέλιο — foundation", "έθεσε": "θέτω — to lay, set", "αριστοκράτης": "αριστοκράτης — aristocrat", "δίκτυα πελατείας": "δίκτυο πελατείας — patronage network", "ιδιοφυής": "ιδιοφυής — ingenious", "να αναδιοργανώσει": "αναδιοργανώνω — to reorganise", "φυλές": "φυλή — tribe", "ενδοχώρα": "ενδοχώρα — inland, hinterland", "κληρώνονταν": "κληρώνομαι — to be chosen by lot", "οστρακισμού": "οστρακισμός — ostracism", "να εξιδανικεύουμε": "εξιδανικεύω — to idealise", "μέτοικοι": "μέτοικος — resident foreigner, metic", "πηγάζει": "πηγάζω — to stem, spring"},
})

ITEMS.append({
 "id": "l36-int-lithi", "title": "Το δικαίωμα στη λήθη", "title_en": "The right to be forgotten", "type": "interview", "level": "C1",
 "context_el": "Θα ακούσετε μια συνέντευξη με μια δικηγόρο ειδική στο δίκαιο προστασίας προσωπικών δεδομένων.",
 "script": [
  L("Δημοσιογράφος", "m", "Τι ακριβώς είναι το λεγόμενο «δικαίωμα στη λήθη»;", "What exactly is the so-called 'right to be forgotten'?"),
  L("Δικηγόρος", "f", "Είναι το δικαίωμα ενός ανθρώπου να ζητήσει να διαγραφούν ή να μην εμφανίζονται στις μηχανές αναζήτησης πληροφορίες για τον ίδιο που είναι πια ανακριβείς, ξεπερασμένες ή άσχετες. Στην Ευρώπη καθιερώθηκε το 2014, με μια απόφαση του Δικαστηρίου της Ευρωπαϊκής Ένωσης, μετά από προσφυγή ενός Ισπανού πολίτη, και αργότερα κατοχυρώθηκε στον Γενικό Κανονισμό για την Προστασία Δεδομένων.", "It is a person's right to ask that information about them which is now inaccurate, outdated or irrelevant be deleted or not appear in search engines. In Europe it was established in 2014, by a ruling of the Court of Justice of the European Union, following an appeal by a Spanish citizen, and was later enshrined in the General Data Protection Regulation."),
  L("Δημοσιογράφος", "m", "Δεν υπάρχει κίνδυνος να χρησιμοποιηθεί για να «σβήσει» κανείς το παρελθόν του, για παράδειγμα ένας πολιτικός;", "Isn't there a risk that it will be used by someone to 'erase' their past, for example a politician?"),
  L("Δικηγόρος", "f", "Αυτή είναι ακριβώς η δυσκολία. Το δικαίωμα δεν είναι απόλυτο. Πρέπει κάθε φορά να σταθμίζεται απέναντι στην ελευθερία της έκφρασης και στο δικαίωμα του κοινού να ενημερώνεται. Ένας ιδιώτης που πριν από είκοσι χρόνια χρεοκόπησε έχει, κατά κανόνα, ισχυρό επιχείρημα. Ένας υπουργός που κατηγορήθηκε για διαφθορά, πολύ πιο αδύναμο, γιατί η πληροφορία αφορά τη δημόσια δράση του.", "That is exactly the difficulty. The right is not absolute. It must be weighed each time against freedom of expression and the public's right to be informed. A private individual who went bankrupt twenty years ago has, as a rule, a strong argument. A minister accused of corruption, a much weaker one, because the information concerns his public conduct."),
  L("Δημοσιογράφος", "m", "Και πώς το ασκεί στην πράξη ένας πολίτης;", "And how does a citizen exercise it in practice?"),
  L("Δικηγόρος", "f", "Υποβάλλει αίτημα απευθείας στη μηχανή αναζήτησης, συνήθως μέσω μιας ηλεκτρονικής φόρμας. Αν απορριφθεί, μπορεί να προσφύγει στην Αρχή Προστασίας Δεδομένων. Να σημειώσω όμως κάτι που πολλοί αγνοούν: η αφαίρεση ενός συνδέσμου από τα αποτελέσματα δεν σημαίνει ότι το ίδιο το άρθρο εξαφανίζεται. Απλώς γίνεται πολύ πιο δύσκολο να το βρει κανείς.", "They submit a request directly to the search engine, usually through an online form. If it is rejected, they can appeal to the Data Protection Authority. But let me point out something many people don't know: removing a link from the results doesn't mean the article itself disappears. It just becomes much harder for anyone to find."),
 ],
 "questions": [
  Q("Πώς καθιερώθηκε το δικαίωμα στη λήθη στην Ευρώπη;", ["Με νόμο της ελληνικής Βουλής", "Με απόφαση του Δικαστηρίου της ΕΕ το 2014", "Με απόφαση των μηχανών αναζήτησης", "Με δημοψήφισμα"], 1, "με μια απόφαση του Δικαστηρίου της Ευρωπαϊκής Ένωσης"),
  Q("Γιατί λέει η δικηγόρος ότι το δικαίωμα «δεν είναι απόλυτο»;", ["Γιατί ισχύει μόνο στην Ισπανία", "Γιατί πρέπει να σταθμίζεται απέναντι στην ελευθερία της έκφρασης και την ενημέρωση", "Γιατί κοστίζει πολύ", "Γιατί αφορά μόνο πολιτικούς"], 1, "Πρέπει κάθε φορά να σταθμίζεται απέναντι στην ελευθερία της έκφρασης"),
  Q("Γιατί ο υπουργός έχει πιο αδύναμο επιχείρημα από τον ιδιώτη;", ["Γιατί έχει περισσότερα χρήματα", "Γιατί η πληροφορία αφορά τη δημόσια δράση του", "Γιατί η υπόθεση είναι πιο πρόσφατη", "Γιατί δεν είναι Ευρωπαίος πολίτης"], 1, "η πληροφορία αφορά τη δημόσια δράση του"),
  Q("Τι πολλοί αγνοούν, σύμφωνα με τη δικηγόρο;", ["Ότι το αίτημα κοστίζει", "Ότι το άρθρο δεν εξαφανίζεται, απλώς βρίσκεται πιο δύσκολα", "Ότι η Αρχή δεν δέχεται προσφυγές", "Ότι οι μηχανές αναζήτησης απορρίπτουν όλα τα αιτήματα"], 1, "η αφαίρεση ενός συνδέσμου από τα αποτελέσματα δεν σημαίνει ότι το ίδιο το άρθρο εξαφανίζεται"),
 ],
 "gloss": {"λήθη": "λήθη — oblivion, forgetting", "προσωπικών δεδομένων": "προσωπικά δεδομένα — personal data", "να διαγραφούν": "διαγράφομαι — to be deleted", "μηχανές αναζήτησης": "μηχανή αναζήτησης — search engine", "ανακριβείς": "ανακριβής — inaccurate", "ξεπερασμένες": "ξεπερασμένος — outdated", "καθιερώθηκε": "καθιερώνομαι — to be established", "προσφυγή": "προσφυγή — appeal", "κατοχυρώθηκε": "κατοχυρώνομαι — to be enshrined", "να σταθμίζεται": "σταθμίζομαι — to be weighed", "χρεοκόπησε": "χρεοκοπώ — to go bankrupt", "διαφθορά": "διαφθορά — corruption", "να προσφύγει": "προσφεύγω — to appeal", "συνδέσμου": "σύνδεσμος — link"},
})

rnd = random.Random(36)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-36.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
