# Source for library/listening/listening-238.json: four more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l238.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []
ITEMS.append({
 "id": "l238-news-oreivatiko-katafygio", "title": "Ξανανοίγει το ορειβατικό καταφύγιο μετά από δύο χρόνια ανακαίνισης", "title_en": "The mountain refuge reopens after two years of renovation", "type": "news", "level": "B2",
 "context_el": "Ακούτε μια είδηση στο δελτίο ειδήσεων ενός περιφερειακού ραδιοφωνικού σταθμού.",
 "script": [
  L("Εκφωνήτρια", "f", "Μετά από δύο χρόνια εργασιών, ξανανοίγει το Σάββατο το ορειβατικό καταφύγιο του βουνού, σε υψόμετρο χιλίων οκτακοσίων μέτρων. Το καταφύγιο ανήκει στον τοπικό ορειβατικό σύλλογο, που κάλυψε μέρος του κόστους με δωρεές μελών και φίλων του βουνού.", "After two years of work, the mountain refuge reopens on Saturday, at an altitude of eighteen hundred metres. The refuge belongs to the local mountaineering club, which covered part of the cost with donations from members and friends of the mountain."),
  L("Εκφωνήτρια", "f", "Το κτίριο έχει πλέον καινούργια στέγη και μόνωση, ενώ το ρεύμα θα παράγεται από ηλιακούς συλλέκτες. Οι θέσεις ύπνου αυξήθηκαν από είκοσι σε τριάντα δύο, και προστέθηκε ένας μικρός χώρος που θα μένει πάντα ανοιχτός, ακόμη και τον χειμώνα, ως καταφύγιο έκτακτης ανάγκης.", "The building now has a new roof and insulation, while electricity will be produced by solar panels. Sleeping places have increased from twenty to thirty-two, and a small room has been added that will always stay open, even in winter, as an emergency shelter."),
  L("Εκφωνήτρια", "f", "Η διανυκτέρευση θα γίνεται μόνο με κράτηση, μέσω της ιστοσελίδας του συλλόγου. Ο σύλλογος υπενθυμίζει ότι στο καταφύγιο δεν υπάρχει δρόμος για αυτοκίνητα: η πρόσβαση γίνεται μόνο με τα πόδια, από ένα μονοπάτι περίπου τριών ωρών.", "Overnight stays will be by booking only, through the club's website. The club reminds people that there is no road for cars to the refuge: access is only on foot, by a path of about three hours."),
  L("Εκφωνήτρια", "f", "Τέλος, οι επισκέπτες καλούνται να παίρνουν μαζί τους τα σκουπίδια τους, γιατί η μεταφορά τους από το καταφύγιο γίνεται με μουλάρια και κοστίζει ακριβά.", "Finally, visitors are asked to take their rubbish away with them, because carrying it down from the refuge is done by mule and is expensive."),
 ],
 "questions": [
  Q("Πώς καλύφθηκε μέρος του κόστους της ανακαίνισης;", ["Με ένα δάνειο από την τράπεζα", "Με δωρεές μελών και φίλων του βουνού", "Με εισιτήρια από τους επισκέπτες", "Από το υπουργείο Τουρισμού"], 1, "κάλυψε μέρος του κόστους με δωρεές μελών και φίλων του βουνού"),
  Q("Τι θα είναι ο μικρός χώρος που προστέθηκε;", ["Μια κουζίνα για τους ορειβάτες", "Ένα καταφύγιο έκτακτης ανάγκης ανοιχτό όλο τον χρόνο", "Ένα μικρό μουσείο του βουνού", "Μια αποθήκη για τον εξοπλισμό"], 1, "ένας μικρός χώρος που θα μένει πάντα ανοιχτός, ακόμη και τον χειμώνα, ως καταφύγιο έκτακτης ανάγκης"),
  Q("Πώς φτάνει κανείς στο καταφύγιο;", ["Με αυτοκίνητο ως την πόρτα", "Μόνο με τα πόδια, από ένα μονοπάτι", "Με το λεωφορείο του συλλόγου", "Με τελεφερίκ"], 1, "η πρόσβαση γίνεται μόνο με τα πόδια, από ένα μονοπάτι περίπου τριών ωρών"),
  Q("Γιατί ζητείται από τους επισκέπτες να παίρνουν τα σκουπίδια τους;", ["Γιατί δεν υπάρχουν κάδοι στο βουνό", "Γιατί η μεταφορά τους γίνεται με μουλάρια και κοστίζει", "Γιατί τα τρώνε τα άγρια ζώα", "Γιατί το απαγορεύει ο νόμος"], 1, "η μεταφορά τους από το καταφύγιο γίνεται με μουλάρια και κοστίζει ακριβά"),
 ],
 "gloss": {"ορειβατικό": "ορειβατικός — mountaineering", "καταφύγιο": "καταφύγιο — (mountain) refuge, shelter", "υψόμετρο": "υψόμετρο — altitude", "δωρεές": "δωρεά — donation", "μόνωση": "μόνωση — insulation", "ηλιακούς συλλέκτες": "ηλιακός συλλέκτης — solar panel", "έκτακτης ανάγκης": "έκτακτη ανάγκη — emergency", "διανυκτέρευση": "διανυκτέρευση — overnight stay", "υπενθυμίζει": "υπενθυμίζω — to remind", "πρόσβαση": "πρόσβαση — access", "μουλάρια": "μουλάρι — mule"},
})
ITEMS.append({
 "id": "l238-vm-geitonas-enydreio", "title": "Μήνυμα από τον γείτονα που προσέχει το ενυδρείο σας", "title_en": "A message from the neighbour looking after your aquarium", "type": "voicemail", "level": "B2",
 "context_el": "Λείπετε σε ταξίδι, και ένας γείτονας ταΐζει τα ψάρια του ενυδρείου σας. Ακούτε ένα μήνυμα που σας άφησε στον τηλεφωνητή.",
 "script": [
  L("Γείτονας", "m", "Γεια σου, ο Μανώλης είμαι, από τον τρίτο. Μην ανησυχήσεις, όλα καλά γενικά, απλώς ήθελα να σε ρωτήσω κάτι για το ενυδρείο. Τα ψάρια τα ταΐζω κάθε πρωί, όπως μου είπες, μία φορά τη μέρα και λίγο, για να μη λερώνεται το νερό.", "Hi, it's Manolis, from the third floor. Don't worry, everything's fine on the whole, I just wanted to ask you something about the aquarium. I feed the fish every morning, as you told me, once a day and only a little, so the water doesn't get dirty."),
  L("Γείτονας", "m", "Από χθες, όμως, το φίλτρο κάνει έναν παράξενο θόρυβο, σαν να βουίζει, και βγάζει λιγότερο νερό από πριν. Δεν το άγγιξα, γιατί δεν ήξερα αν πρέπει να το σβήσω ή όχι, και φοβήθηκα μήπως κάνω ζημιά.", "Since yesterday, though, the filter has been making a strange noise, a sort of humming, and it's putting out less water than before. I didn't touch it, because I didn't know whether I should switch it off or not, and I was afraid of doing some damage."),
  L("Γείτονας", "m", "Και κάτι ακόμη: το μικρό πορτοκαλί ψάρι κάθεται συνέχεια κάτω, δίπλα στις πέτρες, ενώ τα άλλα κολυμπούν κανονικά. Τρώει, πάντως. Δεν ξέρω αν είναι κάτι σοβαρό ή αν έτσι κάνει πάντα.", "And one more thing: the little orange fish keeps sitting at the bottom, next to the stones, while the others swim normally. It is eating, though. I don't know if it's something serious or if it always does that."),
  L("Γείτονας", "m", "Αν θέλεις, μπορώ να πάω στο κατάστημα με τα είδη ενυδρείου στη γωνία και να ρωτήσω. Στείλε μου ένα μήνυμα όταν μπορέσεις, γιατί το απόγευμα φεύγω κι εγώ για δύο μέρες και θα ταΐζει τα ψάρια η κόρη μου.", "If you like, I can go to the aquarium shop on the corner and ask. Send me a message when you can, because I'm going away too for two days this afternoon and my daughter will be feeding the fish."),
 ],
 "questions": [
  Q("Πόσο συχνά ταΐζει ο Μανώλης τα ψάρια;", ["Δύο φορές τη μέρα", "Μία φορά τη μέρα, κάθε πρωί", "Μέρα παρά μέρα", "Κάθε βράδυ"], 1, "Τα ψάρια τα ταΐζω κάθε πρωί … μία φορά τη μέρα"),
  Q("Γιατί δεν άγγιξε το φίλτρο;", ["Γιατί ήταν πολύ ζεστό", "Γιατί φοβήθηκε μήπως κάνει ζημιά", "Γιατί δεν μπορούσε να το φτάσει", "Γιατί του το απαγόρεψαν"], 1, "δεν ήξερα αν πρέπει να το σβήσω ή όχι, και φοβήθηκα μήπως κάνω ζημιά"),
  Q("Τι παράξενο κάνει το μικρό πορτοκαλί ψάρι;", ["Δεν τρώει καθόλου", "Κάθεται συνέχεια κάτω, δίπλα στις πέτρες", "Πηδάει έξω από το νερό", "Κυνηγάει τα άλλα ψάρια"], 1, "το μικρό πορτοκαλί ψάρι κάθεται συνέχεια κάτω, δίπλα στις πέτρες"),
  Q("Γιατί θέλει να του απαντήσετε σύντομα;", ["Γιατί έχει χαλάσει το κλειδί", "Γιατί το απόγευμα φεύγει για δύο μέρες", "Γιατί κλείνει το κατάστημα", "Γιατί πρέπει να αγοράσει τροφή"], 1, "το απόγευμα φεύγω κι εγώ για δύο μέρες"),
 ],
 "gloss": {"ενυδρείο": "ενυδρείο — aquarium", "ταΐζω": "ταΐζω — to feed", "λερώνεται": "λερώνομαι — to get dirty", "φίλτρο": "φίλτρο — filter", "παράξενο": "παράξενος — strange", "βουίζει": "βουίζω — to hum, buzz", "άγγιξα": "αγγίζω — to touch", "ζημιά": "ζημιά — damage", "είδη": "είδος — item, kind (είδη ενυδρείου = aquarium supplies)"},
})
ITEMS.append({
 "id": "l238-c1-mono-omprela", "title": "Από σκιά για τον ήλιο σε προστασία από τη βροχή: η ιστορία της ομπρέλας", "title_en": "From shade against the sun to shelter from the rain: the history of the umbrella", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε μια ιστορικό σε μια ραδιοφωνική εκπομπή για την ιστορία των καθημερινών αντικειμένων.",
 "script": [
  L("Ιστορικός", "f", "Η ομπρέλα είναι από τα αντικείμενα που θεωρούμε τόσο αυτονόητα, ώστε σπάνια αναρωτιόμαστε από πού ήρθαν. Κι όμως, για χιλιάδες χρόνια δεν είχε σχεδόν καμία σχέση με τη βροχή. Στις αρχαίες αυτοκρατορίες της Ανατολής, στην Αίγυπτο, στην Ασσυρία, στην Κίνα, ήταν σύμβολο εξουσίας: ένας υπηρέτης κρατούσε τη σκιά πάνω από το κεφάλι του βασιλιά.", "The umbrella is one of those objects we take so much for granted that we rarely wonder where they came from. And yet for thousands of years it had almost nothing to do with rain. In the ancient empires of the East, in Egypt, Assyria and China, it was a symbol of power: a servant held the shade over the king's head."),
  L("Ιστορικός", "f", "Και στην αρχαία Αθήνα υπήρχε το σκιάδειο, μια μικρή ομπρέλα για τον ήλιο, που τη χρησιμοποιούσαν κυρίως οι γυναίκες. Η ίδια η λέξη μάς θυμίζει τη χρήση του: σκιάδειο από τη σκιά, όπως και η ιταλική λέξη ombrello προέρχεται από τη λατινική λέξη για τη σκιά.", "In ancient Athens too there was the skiadeion, a small parasol against the sun, used mainly by women. The word itself reminds us of its use: skiadeion from skia, shade, just as the Italian word ombrello comes from the Latin word for shade."),
  L("Ιστορικός", "f", "Το να κρατά κανείς ομπρέλα για τη βροχή άργησε να γίνει αποδεκτό, τουλάχιστον για τους άνδρες. Στο Λονδίνο του δέκατου όγδοου αιώνα λέγεται ότι ένας έμπορος, ο Τζόνας Χάνγουεϊ, κυκλοφορούσε με ομπρέλα για χρόνια, και οι αμαξάδες τον κορόιδευαν, γιατί φοβούνταν ότι θα έχαναν πελάτες. Μια ομπρέλα σήμαινε ότι δεν χρειαζόσουν άμαξα για να μη βραχείς.", "Carrying an umbrella against the rain was slow to become acceptable, at least for men. In eighteenth-century London a merchant, Jonas Hanway, is said to have walked about with an umbrella for years, and the coachmen mocked him, because they feared they would lose customers. An umbrella meant you didn't need a carriage to keep from getting wet."),
  L("Ιστορικός", "f", "Η μεγάλη αλλαγή ήρθε στα μέσα του δέκατου ένατου αιώνα, όταν οι βαριοί σκελετοί από ξύλο ή από κόκαλο φάλαινας αντικαταστάθηκαν από ατσάλινες ακτίνες. Η ομπρέλα έγινε ελαφριά και φτηνή, και από αντικείμενο πολυτέλειας έγινε αντικείμενο καθημερινής χρήσης. Ίσως γι' αυτό σήμερα είναι και ένα από τα πράγματα που ξεχνάμε πιο συχνά στα λεωφορεία.", "The big change came in the middle of the nineteenth century, when the heavy frames of wood or whalebone were replaced by steel ribs. The umbrella became light and cheap, and turned from a luxury item into an everyday object. Perhaps that's why today it's also one of the things we most often forget on buses."),
 ],
 "questions": [
  Q("Τι συμβόλιζε η ομπρέλα στις αρχαίες αυτοκρατορίες της Ανατολής;", ["Τον πλούτο των εμπόρων", "Την εξουσία του βασιλιά", "Τη θρησκεία", "Την προστασία από τη βροχή"], 1, "ήταν σύμβολο εξουσίας: ένας υπηρέτης κρατούσε τη σκιά πάνω από το κεφάλι του βασιλιά"),
  Q("Από πού προέρχεται η λέξη «σκιάδειο»;", ["Από ένα ιταλικό όνομα", "Από τη λέξη «σκιά»", "Από το όνομα του εφευρέτη", "Από μια αιγυπτιακή λέξη"], 1, "σκιάδειο από τη σκιά"),
  Q("Γιατί, σύμφωνα με την ιστορία, οι αμαξάδες κορόιδευαν τον Χάνγουεϊ;", ["Γιατί η ομπρέλα του ήταν γυναικεία", "Γιατί φοβούνταν ότι θα έχαναν πελάτες", "Γιατί δεν έβρεχε ποτέ στο Λονδίνο", "Γιατί ήταν ξένος"], 1, "οι αμαξάδες τον κορόιδευαν, γιατί φοβούνταν ότι θα έχαναν πελάτες"),
  Q("Τι έκανε την ομπρέλα ελαφριά και φτηνή;", ["Το πλαστικό ύφασμα", "Οι ατσάλινες ακτίνες", "Η μαζική παραγωγή στην Κίνα", "Ο ξύλινος σκελετός"], 1, "οι βαριοί σκελετοί από ξύλο ή από κόκαλο φάλαινας αντικαταστάθηκαν από ατσάλινες ακτίνες"),
 ],
 "gloss": {"αυτονόητα": "αυτονόητος — self-evident, taken for granted", "αναρωτιόμαστε": "αναρωτιέμαι — to wonder", "αυτοκρατορίες": "αυτοκρατορία — empire", "εξουσίας": "εξουσία — power, authority", "σκιάδειο": "σκιάδειο — parasol (ancient)", "αποδεκτό": "αποδεκτός — acceptable", "αμαξάδες": "αμαξάς — coachman", "κορόιδευαν": "κοροϊδεύω — to mock, make fun of", "βραχείς": "βρέχομαι — to get wet", "σκελετοί": "σκελετός — frame, skeleton", "φάλαινας": "φάλαινα — whale", "ατσάλινες": "ατσάλινος — (made of) steel", "ακτίνες": "ακτίνα — rib (of an umbrella), ray", "πολυτέλειας": "πολυτέλεια — luxury"},
})
ITEMS.append({
 "id": "l238-c1-int-arachnologos", "title": "Μια αραχνολόγος για τις αράχνες που τόσο φοβόμαστε", "title_en": "An arachnologist on the spiders we fear so much", "type": "interview", "level": "C1",
 "context_el": "Μια αραχνολόγος, που εργάζεται σε ένα μουσείο φυσικής ιστορίας, μιλά σε μια ραδιοφωνική εκπομπή για τη φύση.",
 "script": [
  L("Δημοσιογράφος", "m", "Οι αράχνες είναι από τα ζώα που φοβούνται περισσότερο οι άνθρωποι. Είναι δικαιολογημένος αυτός ο φόβος;", "Spiders are among the animals people fear most. Is that fear justified?"),
  L("Αραχνολόγος", "f", "Στη συντριπτική πλειονότητα των περιπτώσεων, όχι. Έχουν περιγραφεί περίπου πενήντα χιλιάδες είδη αράχνης, και σχεδόν όλα έχουν δηλητήριο, αλλά το χρησιμοποιούν για να ακινητοποιούν έντομα. Μόνο λίγες δεκάδες είδη μπορούν να προκαλέσουν σοβαρό πρόβλημα σε έναν άνθρωπο, και ακόμη κι αυτά δαγκώνουν μόνο όταν νιώσουν ότι απειλούνται.", "In the overwhelming majority of cases, no. About fifty thousand species of spider have been described, and almost all have venom, but they use it to immobilise insects. Only a few dozen species can cause a serious problem for a human, and even those bite only when they feel threatened."),
  L("Δημοσιογράφος", "m", "Και στην Ελλάδα;", "And in Greece?"),
  L("Αραχνολόγος", "f", "Το πιο γνωστό επικίνδυνο είδος είναι μια συγγενής της μαύρης χήρας, μια μικρή μαύρη αράχνη με κόκκινες κηλίδες, που ζει κυρίως σε χωράφια και ξερολιθιές. Το τσίμπημά της είναι πολύ επώδυνο και χρειάζεται ιατρική φροντίδα, αλλά είναι σπάνιο. Οι αράχνες που βρίσκουμε στο σπίτι, στις γωνίες του ταβανιού, είναι εντελώς ακίνδυνες. Αντίθετα, μας κάνουν χάρη: τρώνε κουνούπια και μύγες.", "The best-known dangerous species is a relative of the black widow, a small black spider with red spots that lives mainly in fields and dry-stone walls. Its bite is very painful and needs medical care, but it is rare. The spiders we find in the house, in the corners of the ceiling, are completely harmless. On the contrary, they do us a favour: they eat mosquitoes and flies."),
  L("Δημοσιογράφος", "m", "Τι είναι αυτό που σας γοητεύει περισσότερο σε αυτά τα ζώα;", "What fascinates you most about these animals?"),
  L("Αραχνολόγος", "f", "Το μετάξι τους, χωρίς αμφιβολία. Ορισμένα είδη μεταξιού είναι, σε σχέση με το βάρος τους, πιο ανθεκτικά από το ατσάλι, και ταυτόχρονα ελαστικά. Οι επιστήμονες προσπαθούν εδώ και δεκαετίες να το αντιγράψουν, για ράμματα στη χειρουργική ή για ελαφριά υφάσματα. Και κάτι ακόμη: μια μελέτη υπολόγισε ότι όλες οι αράχνες του πλανήτη τρώνε κάθε χρόνο εκατοντάδες εκατομμύρια τόνους έντομα. Χωρίς αυτές, θα είχαμε πολύ μεγαλύτερο πρόβλημα με τα παράσιτα στις καλλιέργειες.", "Their silk, without a doubt. Some kinds of silk are, relative to their weight, stronger than steel, and elastic at the same time. Scientists have been trying for decades to copy it, for stitches in surgery or for light fabrics. And one more thing: a study estimated that all the spiders on the planet eat hundreds of millions of tonnes of insects every year. Without them, we'd have a much bigger problem with pests in our crops."),
 ],
 "questions": [
  Q("Για ποιο σκοπό χρησιμοποιούν οι αράχνες το δηλητήριό τους;", ["Για να επιτίθενται στους ανθρώπους", "Για να ακινητοποιούν έντομα", "Για να προστατεύουν τον ιστό τους από τη βροχή", "Για να επικοινωνούν μεταξύ τους"], 1, "το χρησιμοποιούν για να ακινητοποιούν έντομα"),
  Q("Τι λέει για την επικίνδυνη αράχνη που ζει στην Ελλάδα;", ["Ότι ζει κυρίως μέσα στα σπίτια", "Ότι το τσίμπημά της είναι επώδυνο αλλά σπάνιο", "Ότι έχει εξαφανιστεί", "Ότι δεν χρειάζεται γιατρό"], 1, "Το τσίμπημά της είναι πολύ επώδυνο και χρειάζεται ιατρική φροντίδα, αλλά είναι σπάνιο"),
  Q("Γιατί, κατά την αραχνολόγο, οι αράχνες του σπιτιού «μας κάνουν χάρη»;", ["Γιατί καθαρίζουν τη σκόνη", "Γιατί τρώνε κουνούπια και μύγες", "Γιατί διώχνουν τα ποντίκια", "Γιατί προειδοποιούν για την υγρασία"], 1, "μας κάνουν χάρη: τρώνε κουνούπια και μύγες"),
  Q("Για ποιο λόγο προσπαθούν οι επιστήμονες να αντιγράψουν το μετάξι της αράχνης;", ["Για να φτιάξουν φθηνότερο ατσάλι", "Για χειρουργικά ράμματα και ελαφριά υφάσματα", "Για να καταπολεμήσουν τα κουνούπια", "Για να παράγουν φάρμακα"], 1, "για ράμματα στη χειρουργική ή για ελαφριά υφάσματα"),
 ],
 "gloss": {"αραχνολόγος": "αραχνολόγος — arachnologist", "δικαιολογημένος": "δικαιολογημένος — justified", "συντριπτική πλειονότητα": "συντριπτική πλειονότητα — overwhelming majority", "δηλητήριο": "δηλητήριο — venom, poison", "ακινητοποιούν": "ακινητοποιώ — to immobilise", "απειλούνται": "απειλούμαι — to be threatened", "κηλίδες": "κηλίδα — spot", "ξερολιθιές": "ξερολιθιά — dry-stone wall", "επώδυνο": "επώδυνος — painful", "μετάξι": "μετάξι — silk", "ανθεκτικά": "ανθεκτικός — strong, durable", "ράμματα": "ράμμα — stitch, suture", "παράσιτα": "παράσιτο — pest, parasite", "καλλιέργειες": "καλλιέργεια — crop"},
})

rnd = random.Random(238)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-238.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
