# Source for library/listening/listening-103.json: ten more B2–C1 listening items (script + questions + gloss).
# Build: python3 tools/listening/l103.py
import json, os, random

def L(sp, v, el, en): return {"speaker": sp, "voice": v, "el": el, "en": en}
def Q(q, opts, ans, why): return {"q": q, "options": opts, "answer": opts[ans], "why": why}

ITEMS = []

ITEMS.append({
 "id": "l103-ann-protes-voitheies", "title": "Δωρεάν μαθήματα πρώτων βοηθειών", "title_en": "Free first-aid classes", "type": "announcement", "level": "B2",
 "context_el": "Ακούτε μια ανακοίνωση στο τοπικό ραδιόφωνο.",
 "script": [
  L("Εκφωνητής", "m", "Η εθελοντική ομάδα διάσωσης της πόλης, σε συνεργασία με τον δήμο, οργανώνει δωρεάν μαθήματα πρώτων βοηθειών για ενήλικες. Τα μαθήματα θα γίνονται κάθε Σάββατο του Μαρτίου, από τις δέκα ως τη μία, στο πνευματικό κέντρο του δήμου.", "The town's volunteer rescue team, in cooperation with the municipality, is organising free first-aid classes for adults. The classes will take place every Saturday in March, from ten to one, at the municipal cultural centre."),
  L("Εκφωνητής", "m", "Οι συμμετέχοντες θα μάθουν πώς να κάνουν καρδιοπνευμονική αναζωογόνηση, πώς να χρησιμοποιούν απινιδωτή και τι να κάνουν αν κάποιος πνίγεται με φαγητό. Στο τέλος θα πάρουν βεβαίωση παρακολούθησης.", "Participants will learn how to perform CPR, how to use a defibrillator and what to do if someone is choking on food. At the end they will receive a certificate of attendance."),
  L("Εκφωνητής", "m", "Οι θέσεις είναι περιορισμένες, είκοσι ανά τμήμα. Οι ενδιαφερόμενοι μπορούν να δηλώσουν συμμετοχή στην ιστοσελίδα του δήμου ή στο τηλέφωνο του πνευματικού κέντρου, μέχρι τις είκοσι Φεβρουαρίου. Παρακαλούνται να φορούν άνετα ρούχα, γιατί η εκπαίδευση περιλαμβάνει πρακτική άσκηση στο πάτωμα.", "Places are limited, twenty per group. Those interested can register on the municipality's website or by phoning the cultural centre, until the twentieth of February. They are asked to wear comfortable clothes, because the training includes practice on the floor."),
 ],
 "questions": [
  Q("Πότε θα γίνονται τα μαθήματα;", ["Κάθε απόγευμα του Φεβρουαρίου", "Κάθε Σάββατο του Μαρτίου, από τις δέκα ως τη μία", "Κάθε Κυριακή πρωί", "Μία φορά τον μήνα"], 1, "κάθε Σάββατο του Μαρτίου, από τις δέκα ως τη μία"),
  Q("Τι θα πάρουν οι συμμετέχοντες στο τέλος;", ["Βεβαίωση παρακολούθησης", "Ένα κουτί πρώτων βοηθειών", "Έναν απινιδωτή", "Ένα βιβλίο"], 0, "Στο τέλος θα πάρουν βεβαίωση παρακολούθησης"),
  Q("Γιατί πρέπει να φορούν άνετα ρούχα;", ["Γιατί η αίθουσα δεν έχει θέρμανση", "Γιατί θα γίνει μάθημα στο ύπαιθρο", "Γιατί η εκπαίδευση περιλαμβάνει πρακτική άσκηση στο πάτωμα", "Γιατί θα βγουν φωτογραφίες"], 2, "η εκπαίδευση περιλαμβάνει πρακτική άσκηση στο πάτωμα"),
 ],
 "gloss": {"διάσωσης": "διάσωση — rescue", "βοηθειών": "πρώτες βοήθειες — first aid", "καρδιοπνευμονική": "καρδιοπνευμονική αναζωογόνηση — CPR", "απινιδωτή": "απινιδωτής — defibrillator", "πνίγεται": "πνίγομαι — to choke", "βεβαίωση": "βεβαίωση — certificate", "παρακολούθησης": "παρακολούθηση — attendance", "περιορισμένες": "περιορισμένος — limited"}
})

ITEMS.append({
 "id": "l103-vm-ananeosi-symvolaiou", "title": "Μήνυμα από τον ιδιοκτήτη για το συμβόλαιο", "title_en": "A message from the landlord about the lease", "type": "voicemail", "level": "B2",
 "context_el": "Νοικιάζετε ένα διαμέρισμα. Ακούτε ένα μήνυμα από τον ιδιοκτήτη στον τηλεφωνητή σας.",
 "script": [
  L("Ιδιοκτήτης", "m", "Καλησπέρα, κυρία Νικολάου, ο Παπαδάκης είμαι, ο ιδιοκτήτης του διαμερίσματος. Σας τηλεφωνώ γιατί το συμβόλαιό μας λήγει στο τέλος του Απριλίου και ήθελα να συζητήσουμε την ανανέωση.", "Good evening, Mrs Nikolaou, it's Papadakis, the owner of the flat. I'm calling because our lease expires at the end of April and I wanted to discuss renewing it."),
  L("Ιδιοκτήτης", "m", "Θα ήθελα πολύ να μείνετε, γιατί είστε εξαιρετική ενοικιάστρια. Όπως ξέρετε, όμως, οι τιμές έχουν ανέβει αρκετά. Σκέφτομαι μια αύξηση πενήντα ευρώ τον μήνα, αλλά σε αντάλλαγμα θα αλλάξω τα παλιά παράθυρα του σαλονιού πριν από τον χειμώνα, όπως μου είχατε ζητήσει.", "I would very much like you to stay, because you are an excellent tenant. As you know, though, prices have gone up quite a bit. I'm thinking of an increase of fifty euros a month, but in return I'll replace the old living-room windows before the winter, as you had asked me."),
  L("Ιδιοκτήτης", "m", "Αν συμφωνείτε, μπορούμε να υπογράψουμε νέο συμβόλαιο για τρία χρόνια. Πείτε μου, σας παρακαλώ, την απόφασή σας μέχρι τα μέσα Μαρτίου, για να έχω χρόνο να βρω άλλον ενοικιαστή αν χρειαστεί. Θα είμαι στην Αθήνα την επόμενη εβδομάδα, αν θέλετε να τα πούμε από κοντά.", "If you agree, we can sign a new lease for three years. Please let me know your decision by mid-March, so that I have time to find another tenant if necessary. I'll be in Athens next week, if you'd like to talk in person."),
 ],
 "questions": [
  Q("Γιατί τηλεφωνεί ο ιδιοκτήτης;", ["Γιατί θέλει να πουλήσει το διαμέρισμα", "Γιατί η ενοικιάστρια δεν πλήρωσε το ενοίκιο", "Γιατί έχει παράπονα από τους γείτονες", "Γιατί το συμβόλαιο λήγει και θέλει να συζητήσουν την ανανέωση"], 3, "το συμβόλαιό μας λήγει στο τέλος του Απριλίου και ήθελα να συζητήσουμε την ανανέωση"),
  Q("Τι προσφέρει σε αντάλλαγμα για την αύξηση;", ["Να βάψει το διαμέρισμα", "Να αλλάξει τα παλιά παράθυρα του σαλονιού", "Να αγοράσει καινούργιο ψυγείο", "Να μειώσει τα κοινόχρηστα"], 1, "θα αλλάξω τα παλιά παράθυρα του σαλονιού"),
  Q("Μέχρι πότε θέλει να μάθει την απόφαση;", ["Μέχρι το τέλος του Απριλίου", "Μέχρι την επόμενη εβδομάδα", "Μέχρι τα μέσα Μαρτίου", "Μέχρι τον χειμώνα"], 2, "μέχρι τα μέσα Μαρτίου"),
 ],
 "gloss": {"συμβόλαιο": "συμβόλαιο — contract, lease", "λήγει": "λήγω — to expire", "ανανέωση": "ανανέωση — renewal", "ενοικιάστρια": "ενοικιάστρια — tenant (f.)", "αύξηση": "αύξηση — increase", "αντάλλαγμα": "σε αντάλλαγμα — in return", "ενοικιαστή": "ενοικιαστής — tenant"}
})

ITEMS.append({
 "id": "l103-dia-allagi-vardias", "title": "Ανταλλαγή βάρδιας με μια συνάδελφο", "title_en": "Swapping a shift with a colleague", "type": "dialogue", "level": "B2",
 "context_el": "Δύο συνάδελφοι σε ένα σούπερ μάρκετ συζητούν για το πρόγραμμα της εβδομάδας.",
 "script": [
  L("Κατερίνα", "f", "Ηλία, έχεις ένα λεπτό; Θέλω να σου ζητήσω μια χάρη.", "Ilias, have you got a minute? I want to ask you a favour."),
  L("Ηλίας", "m", "Πες μου.", "Tell me."),
  L("Κατερίνα", "f", "Την Παρασκευή έχω πρωινή βάρδια, αλλά παντρεύεται η ξαδέρφη μου στην Κόρινθο και πρέπει να φύγω νωρίς το πρωί. Μπορείς να πάρεις εσύ την πρωινή μου, κι εγώ να κάνω τη δική σου απογευματινή την Κυριακή;", "On Friday I'm on the morning shift, but my cousin is getting married in Corinth and I have to leave early in the morning. Could you take my morning shift, and I'll do your afternoon one on Sunday?"),
  L("Ηλίας", "m", "Την Παρασκευή το πρωί... Έχω ραντεβού με τον οδοντίατρο στις εννιά. Μπορώ να έρθω, αλλά όχι πριν από τις έντεκα.", "Friday morning... I have a dentist's appointment at nine. I can come, but not before eleven."),
  L("Κατερίνα", "f", "Η βάρδια ξεκινά στις επτά. Χμ. Μήπως ρωτήσω τη Δέσποινα για τις πρώτες τέσσερις ώρες κι εσύ έρχεσαι μετά;", "The shift starts at seven. Hmm. What if I ask Despoina for the first four hours and you come after that?"),
  L("Ηλίας", "m", "Γίνεται κι αυτό, αρκεί να το εγκρίνει ο προϊστάμενος. Ξέρεις ότι θέλει να του το λέμε τουλάχιστον τρεις μέρες πριν.", "That works too, as long as the supervisor approves. You know he wants us to tell him at least three days in advance."),
  L("Κατερίνα", "f", "Το ξέρω. Θα του στείλω μήνυμα σήμερα κιόλας. Σ' ευχαριστώ πολύ, σου χρωστάω!", "I know. I'll message him today. Thanks a lot, I owe you!"),
 ],
 "questions": [
  Q("Γιατί η Κατερίνα θέλει να αλλάξει βάρδια;", ["Γιατί είναι άρρωστη", "Γιατί παντρεύεται η ξαδέρφη της στην Κόρινθο", "Γιατί έχει ραντεβού με τον οδοντίατρο", "Γιατί θέλει να πάει διακοπές"], 1, "παντρεύεται η ξαδέρφη μου στην Κόρινθο"),
  Q("Από τι ώρα μπορεί να έρθει ο Ηλίας την Παρασκευή;", ["Από τις επτά", "Από τις εννιά", "Από το απόγευμα", "Από τις έντεκα"], 3, "όχι πριν από τις έντεκα"),
  Q("Τι θέλει ο προϊστάμενος;", ["Να του το λένε τουλάχιστον τρεις μέρες πριν", "Να μην αλλάζουν ποτέ βάρδιες", "Να του στέλνουν γραπτή αίτηση", "Να βρίσκουν μόνοι τους αντικαταστάτη"], 0, "θέλει να του το λέμε τουλάχιστον τρεις μέρες πριν"),
 ],
 "gloss": {"χάρη": "χάρη — favour", "βάρδια": "βάρδια — shift", "απογευματινή": "απογευματινός — afternoon (shift)", "εγκρίνει": "εγκρίνω — to approve", "προϊστάμενος": "προϊστάμενος — supervisor", "χρωστάω": "χρωστάω — to owe"}
})

ITEMS.append({
 "id": "l103-int-xenagos-spilaiou", "title": "Μια ξεναγός σε σπήλαιο", "title_en": "A cave guide", "type": "interview", "level": "B2",
 "context_el": "Ακούτε μια συνέντευξη με μια ξεναγό που δουλεύει σε ένα σπήλαιο.",
 "script": [
  L("Δημοσιογράφος", "m", "Πόσα χρόνια ξεναγείτε επισκέπτες στο σπήλαιο;", "How many years have you been guiding visitors in the cave?"),
  L("Ξεναγός", "f", "Δώδεκα χρόνια. Κάθε μέρα κατεβαίνω τα ίδια σκαλιά, κι όμως κάθε φορά κάτι μου φαίνεται καινούργιο. Το φως πέφτει αλλιώς, ή κάποιος επισκέπτης προσέχει μια λεπτομέρεια που εγώ δεν είχα δει.", "Twelve years. Every day I go down the same steps, and yet each time something seems new to me. The light falls differently, or a visitor notices a detail that I hadn't seen."),
  L("Δημοσιογράφος", "m", "Τι ρωτούν πιο συχνά οι επισκέπτες;", "What do visitors ask most often?"),
  L("Ξεναγός", "f", "Πόσο χρόνο χρειάζεται για να σχηματιστεί ένας σταλακτίτης. Η απάντηση τους εκπλήσσει πάντα: σε πολλά σπήλαια μεγαλώνει μόλις ένα εκατοστό στα εκατό χρόνια, ανάλογα με το νερό και τα άλατα. Έτσι καταλαβαίνουν γιατί απαγορεύεται αυστηρά να τους αγγίζουν.", "How long it takes for a stalactite to form. The answer always surprises them: in many caves it grows just one centimetre in a hundred years, depending on the water and the minerals. That way they understand why touching them is strictly forbidden."),
  L("Δημοσιογράφος", "m", "Και γιατί ακριβώς δεν επιτρέπεται να τους αγγίζουν;", "And why exactly are they not allowed to touch them?"),
  L("Ξεναγός", "f", "Γιατί το λίπος από το δέρμα μας εμποδίζει το νερό να αφήσει τα άλατα, και ο σταλακτίτης σταματά να μεγαλώνει. Ένα άγγιγμα αρκεί για να καταστρέψει τη δουλειά αιώνων. Γι' αυτό, στο τέλος κάθε ξενάγησης, λέω πάντα στους επισκέπτες: «Φύγετε μόνο με φωτογραφίες και αναμνήσεις.»", "Because the oil from our skin stops the water from leaving its minerals, and the stalactite stops growing. A single touch is enough to destroy the work of centuries. That's why at the end of every tour I always tell visitors: 'Leave with nothing but photos and memories.'"),
 ],
 "questions": [
  Q("Γιατί κάτι της φαίνεται καινούργιο κάθε φορά;", ["Γιατί το σπήλαιο αλλάζει κάθε μέρα σχήμα", "Γιατί αλλάζει συχνά διαδρομή", "Γιατί το φως πέφτει αλλιώς ή κάποιος επισκέπτης προσέχει μια λεπτομέρεια", "Γιατί ανοίγουν συνεχώς νέες αίθουσες"], 2, "Το φως πέφτει αλλιώς, ή κάποιος επισκέπτης προσέχει μια λεπτομέρεια που εγώ δεν είχα δει"),
  Q("Τι ρωτούν πιο συχνά οι επισκέπτες;", ["Πόσο βαθύ είναι το σπήλαιο", "Πόσο χρόνο χρειάζεται για να σχηματιστεί ένας σταλακτίτης", "Αν ζουν ζώα μέσα", "Πότε ανακαλύφθηκε το σπήλαιο"], 1, "Πόσο χρόνο χρειάζεται για να σχηματιστεί ένας σταλακτίτης"),
  Q("Γιατί απαγορεύεται να αγγίζουν τους σταλακτίτες;", ["Γιατί το λίπος από το δέρμα σταματά την ανάπτυξή τους", "Γιατί είναι αιχμηροί", "Γιατί μπορεί να πέσουν", "Γιατί είναι πολύ κρύοι"], 0, "το λίπος από το δέρμα μας εμποδίζει το νερό να αφήσει τα άλατα"),
 ],
 "gloss": {"ξεναγό": "ξεναγός — guide", "ξεναγείτε": "ξεναγώ — to guide", "σπήλαιο": "σπήλαιο — cave", "σταλακτίτης": "σταλακτίτης — stalactite", "σχηματιστεί": "σχηματίζομαι — to form", "εκπλήσσει": "εκπλήσσω — to surprise", "άλατα": "άλας — mineral salt", "αγγίζουν": "αγγίζω — to touch", "άγγιγμα": "άγγιγμα — touch", "αιώνων": "αιώνας — century"}
})

ITEMS.append({
 "id": "l103-rep-tournoua-astegon", "title": "Ένα ποδοσφαιρικό τουρνουά για αστέγους", "title_en": "A football tournament for homeless people", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ σε μια εκπομπή για την κοινωνία.",
 "script": [
  L("Ρεπόρτερ", "m", "Σε ένα γήπεδο πέντε επί πέντε στο κέντρο της Θεσσαλονίκης, δώδεκα ομάδες παίζουν με πάθος, ενώ γύρω τους εκατό περίπου θεατές χειροκροτούν. Δεν πρόκειται για ένα συνηθισμένο τουρνουά: οι παίκτες είναι άνθρωποι που ζουν ή έχουν ζήσει στον δρόμο.", "On a five-a-side pitch in the centre of Thessaloniki, twelve teams are playing with passion, while around them about a hundred spectators applaud. This is not an ordinary tournament: the players are people who live or have lived on the street."),
  L("Ρεπόρτερ", "m", "Το τουρνουά το οργανώνει για τρίτη χρονιά μια οργάνωση που βοηθά αστέγους. «Το ποδόσφαιρο είναι η αφορμή», λέει μια από τις κοινωνικές λειτουργούς. «Αυτό που μετράει είναι ότι οι παίκτες προπονούνται τακτικά, έχουν ένα πρόγραμμα, μια ομάδα που τους περιμένει. Για πολλούς είναι το πρώτο βήμα για να ξαναβρούν τον εαυτό τους.»", "The tournament is organised for the third year by an organisation that helps homeless people. 'Football is the occasion,' says one of the social workers. 'What counts is that the players train regularly, have a schedule, a team waiting for them. For many it is the first step towards finding themselves again.'"),
  L("Ρεπόρτερ", "m", "Ο Γιάννης, σαράντα πέντε χρονών, έχασε τη δουλειά και το σπίτι του πριν από τέσσερα χρόνια. Σήμερα μένει σε ένα δωμάτιο που του παρέχει η οργάνωση και δουλεύει σε μια αποθήκη. «Όταν παίζω, δεν είμαι ο άστεγος», λέει. «Είμαι ο τερματοφύλακας.»", "Giannis, forty-five, lost his job and his home four years ago. Today he lives in a room provided by the organisation and works in a warehouse. 'When I play, I'm not the homeless guy,' he says. 'I'm the goalkeeper.'"),
 ],
 "questions": [
  Q("Ποιοι είναι οι παίκτες του τουρνουά;", ["Επαγγελματίες ποδοσφαιριστές", "Μαθητές λυκείου", "Άνθρωποι που ζουν ή έχουν ζήσει στον δρόμο", "Υπάλληλοι του δήμου"], 2, "οι παίκτες είναι άνθρωποι που ζουν ή έχουν ζήσει στον δρόμο"),
  Q("Τι μετράει περισσότερο, κατά την κοινωνική λειτουργό;", ["Ότι οι παίκτες προπονούνται τακτικά και έχουν μια ομάδα που τους περιμένει", "Η νίκη", "Τα χρήματα που μαζεύονται", "Η προβολή στα μέσα ενημέρωσης"], 0, "οι παίκτες προπονούνται τακτικά, έχουν ένα πρόγραμμα, μια ομάδα που τους περιμένει"),
  Q("Τι κάνει σήμερα ο Γιάννης;", ["Ζει ακόμα στον δρόμο", "Είναι προπονητής", "Έχει γυρίσει στο χωριό του", "Μένει σε ένα δωμάτιο της οργάνωσης και δουλεύει σε μια αποθήκη"], 3, "μένει σε ένα δωμάτιο που του παρέχει η οργάνωση και δουλεύει σε μια αποθήκη"),
 ],
 "gloss": {"πάθος": "πάθος — passion", "θεατές": "θεατής — spectator", "αστέγους": "άστεγος — homeless person", "αφορμή": "αφορμή — occasion, pretext", "λειτουργούς": "κοινωνικός λειτουργός — social worker", "προπονούνται": "προπονούμαι — to train", "παρέχει": "παρέχω — to provide", "τερματοφύλακας": "τερματοφύλακας — goalkeeper"}
})

ITEMS.append({
 "id": "l103-rep-giorti-kastanou", "title": "Η γιορτή του κάστανου", "title_en": "The chestnut festival", "type": "report", "level": "B2",
 "context_el": "Ακούτε ένα ρεπορτάζ από ένα ορεινό χωριό.",
 "script": [
  L("Ρεπόρτερ", "f", "Κάθε Οκτώβριο, ένα μικρό ορεινό χωριό της Αρκαδίας γεμίζει επισκέπτες για τη γιορτή του κάστανου. Στην πλατεία ανάβουν μεγάλες φωτιές, πάνω στις οποίες ψήνονται κάστανα σε τρυπημένα τηγάνια, και η μυρωδιά απλώνεται σε όλο το χωριό.", "Every October, a small mountain village in Arcadia fills with visitors for the chestnut festival. In the square they light big fires, over which chestnuts are roasted in pans with holes, and the smell spreads all over the village."),
  L("Ρεπόρτερ", "f", "Οι νοικοκυρές του χωριού ετοιμάζουν για μέρες γλυκά με κάστανο: κάστανα σε σιρόπι, πίτες, ακόμη και ένα λικέρ που η συνταγή του περνά από μητέρα σε κόρη. Τα έσοδα από τις πωλήσεις πηγαίνουν στον πολιτιστικό σύλλογο, που συντηρεί την παλιά βρύση και το κτίριο του σχολείου, το οποίο έχει κλείσει εδώ και χρόνια.", "The women of the village spend days preparing chestnut sweets: chestnuts in syrup, pies, even a liqueur whose recipe passes from mother to daughter. The proceeds from the sales go to the cultural association, which maintains the old fountain and the school building, which closed years ago."),
  L("Ρεπόρτερ", "f", "«Τον χειμώνα μένουμε εδώ μόνο τριάντα άνθρωποι», λέει ο πρόεδρος του συλλόγου. «Αυτές τις δύο μέρες έρχονται πάνω από δύο χιλιάδες. Πολλοί είναι παιδιά και εγγόνια του χωριού, που ζουν στην Αθήνα. Η γιορτή είναι ο τρόπος μας να μη σβήσει το χωριό.»", "'In winter only thirty of us live here,' says the president of the association. 'On these two days more than two thousand come. Many are children and grandchildren of the village who live in Athens. The festival is our way of keeping the village from dying out.'"),
 ],
 "questions": [
  Q("Πώς ψήνονται τα κάστανα;", ["Στον φούρνο του χωριού", "Σε ηλεκτρικές ψησταριές", "Στα τζάκια των σπιτιών", "Σε τρυπημένα τηγάνια πάνω σε μεγάλες φωτιές"], 3, "ψήνονται κάστανα σε τρυπημένα τηγάνια"),
  Q("Πού πηγαίνουν τα έσοδα από τις πωλήσεις;", ["Στον δήμο", "Στον πολιτιστικό σύλλογο", "Στις νοικοκυρές", "Στην εκκλησία"], 1, "Τα έσοδα από τις πωλήσεις πηγαίνουν στον πολιτιστικό σύλλογο"),
  Q("Πόσοι μένουν στο χωριό τον χειμώνα;", ["Τριάντα", "Δύο χιλιάδες", "Τριακόσιοι", "Κανείς"], 0, "Τον χειμώνα μένουμε εδώ μόνο τριάντα άνθρωποι"),
 ],
 "gloss": {"κάστανα": "κάστανο — chestnut", "τρυπημένα": "τρυπημένος — with holes", "τηγάνια": "τηγάνι — frying pan", "απλώνεται": "απλώνομαι — to spread", "σιρόπι": "σιρόπι — syrup", "λικέρ": "λικέρ — liqueur", "έσοδα": "έσοδα — proceeds, income", "συντηρεί": "συντηρώ — to maintain", "σβήσει": "σβήνω — to die out"}
})

ITEMS.append({
 "id": "l103-mono-na-leo-ochi", "title": "Πώς έμαθα να λέω «όχι»", "title_en": "How I learned to say no", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια γυναίκα να μιλά σε ένα podcast για την καθημερινή ψυχολογία.",
 "script": [
  L("Ομιλήτρια", "f", "Για χρόνια δεν μπορούσα να πω όχι σε κανέναν. Αν ένας συνάδελφος μού ζητούσε να τελειώσω μια δουλειά του, έλεγα ναι. Αν μια φίλη με καλούσε σε πάρτι ενώ ήμουν πτώμα, πήγαινα. Το αποτέλεσμα ήταν ότι δεν είχα ποτέ χρόνο για τον εαυτό μου.", "For years I couldn't say no to anyone. If a colleague asked me to finish a job of his, I said yes. If a friend invited me to a party when I was dead tired, I went. The result was that I never had time for myself."),
  L("Ομιλήτρια", "f", "Η αλλαγή ήρθε όταν, μια Κυριακή, βρέθηκα να βοηθάω στη μετακόμιση ενός γνωστού που δεν είχα δει εδώ και δύο χρόνια, ενώ είχα υποσχεθεί στην κόρη μου να πάμε θάλασσα. Το βλέμμα της όταν της το είπα δεν θα το ξεχάσω ποτέ.", "The change came when, one Sunday, I found myself helping an acquaintance I hadn't seen for two years move house, although I had promised my daughter we would go to the beach. I will never forget the look on her face when I told her."),
  L("Ομιλήτρια", "f", "Ξεκίνησα με μικρά πράγματα. Όταν κάποιος μου ζητούσε κάτι, δεν απαντούσα αμέσως· έλεγα «άσε με να το σκεφτώ». Αυτά τα λίγα λεπτά μου έδιναν χρόνο να αναρωτηθώ αν το ήθελα πραγματικά. Οι περισσότεροι, προς μεγάλη μου έκπληξη, δεν θύμωσαν καθόλου όταν τελικά αρνήθηκα.", "I started with small things. When someone asked me for something, I didn't answer straight away; I said 'let me think about it'. Those few minutes gave me time to ask myself whether I really wanted to. Most people, to my great surprise, didn't get angry at all when I finally said no."),
 ],
 "questions": [
  Q("Ποιο ήταν το αποτέλεσμα του ότι έλεγε πάντα ναι;", ["Έχασε τη δουλειά της", "Δεν είχε ποτέ χρόνο για τον εαυτό της", "Τσακώθηκε με τους φίλους της", "Αρρώστησε"], 1, "δεν είχα ποτέ χρόνο για τον εαυτό μου"),
  Q("Τι είχε υποσχεθεί στην κόρη της εκείνη την Κυριακή;", ["Να πάνε σινεμά", "Να τη βοηθήσει στα μαθήματα", "Να πάνε θάλασσα", "Να μαγειρέψουν μαζί"], 2, "είχα υποσχεθεί στην κόρη μου να πάμε θάλασσα"),
  Q("Τι άρχισε να λέει όταν της ζητούσαν κάτι;", ["«Ρώτα κάποιον άλλον»", "«Όχι, ευχαριστώ»", "«Ίσως την άλλη εβδομάδα»", "«Άσε με να το σκεφτώ»"], 3, "έλεγα «άσε με να το σκεφτώ»"),
 ],
 "gloss": {"πτώμα": "είμαι πτώμα — to be dead tired", "μετακόμιση": "μετακόμιση — moving house", "υποσχεθεί": "υπόσχομαι — to promise", "βλέμμα": "βλέμμα — look", "αναρωτηθώ": "αναρωτιέμαι — to wonder, ask oneself", "έκπληξη": "έκπληξη — surprise", "αρνήθηκα": "αρνούμαι — to refuse"}
})

ITEMS.append({
 "id": "l103-mono-agrotissa", "title": "Η πρώτη μου χρονιά ως αγρότισσα", "title_en": "My first year as a farmer", "type": "monologue", "level": "B2",
 "context_el": "Ακούτε μια νέα αγρότισσα να μιλά σε μια εκπομπή για την ύπαιθρο.",
 "script": [
  L("Ομιλήτρια", "f", "Πριν από δύο χρόνια δούλευα σε μια διαφημιστική εταιρεία στην Αθήνα. Όταν πέθανε ο παππούς μου, μου άφησε δέκα στρέμματα με ελιές στη Μεσσηνία. Όλοι περίμεναν ότι θα τα πουλήσω. Εγώ αποφάσισα να δοκιμάσω να τα καλλιεργήσω.", "Two years ago I was working for an advertising company in Athens. When my grandfather died, he left me ten stremmata of olive trees in Messinia. Everyone expected me to sell them. I decided to try farming them."),
  L("Ομιλήτρια", "f", "Η πρώτη χρονιά ήταν πολύ πιο δύσκολη απ' όσο φανταζόμουν. Δεν ήξερα πότε να κλαδέψω ούτε πώς να προστατέψω τα δέντρα από τον δάκο. Ευτυχώς, ο γείτονάς μου, ένας ηλικιωμένος αγρότης, μου έδειχνε υπομονετικά τα πάντα, αν και στην αρχή γελούσε με τα καινούργια μου γάντια.", "The first year was much harder than I imagined. I didn't know when to prune or how to protect the trees from the olive fly. Fortunately, my neighbour, an elderly farmer, patiently showed me everything, although at first he laughed at my new gloves."),
  L("Ομιλήτρια", "f", "Τον Νοέμβριο μαζέψαμε τις ελιές με τη βοήθεια φίλων από την Αθήνα. Βγάλαμε περίπου πεντακόσια κιλά λάδι. Δεν είναι πολλά, αλλά όταν δοκίμασα το πρώτο ζεστό ψωμί με το δικό μου λάδι, ήξερα ότι είχα πάρει τη σωστή απόφαση.", "In November we picked the olives with the help of friends from Athens. We got about five hundred kilos of oil. It isn't much, but when I tasted the first warm bread with my own oil, I knew I had made the right decision."),
 ],
 "questions": [
  Q("Τι δουλειά έκανε πριν από δύο χρόνια;", ["Δούλευε σε μια διαφημιστική εταιρεία", "Ήταν δασκάλα", "Είχε ένα εστιατόριο", "Ήταν νοσηλεύτρια"], 0, "δούλευα σε μια διαφημιστική εταιρεία στην Αθήνα"),
  Q("Ποιος τη βοήθησε την πρώτη χρονιά;", ["Ο παππούς της", "Ένας γεωπόνος του δήμου", "Οι γονείς της", "Ο γείτονάς της, ένας ηλικιωμένος αγρότης"], 3, "ο γείτονάς μου, ένας ηλικιωμένος αγρότης, μου έδειχνε υπομονετικά τα πάντα"),
  Q("Πότε κατάλαβε ότι είχε πάρει τη σωστή απόφαση;", ["Όταν πούλησε το λάδι", "Όταν τελείωσε η συγκομιδή", "Όταν δοκίμασε ζεστό ψωμί με το δικό της λάδι", "Όταν ήρθαν οι φίλοι της"], 2, "όταν δοκίμασα το πρώτο ζεστό ψωμί με το δικό μου λάδι"),
 ],
 "gloss": {"αγρότισσα": "αγρότισσα — farmer (f.)", "διαφημιστική": "διαφημιστικός — advertising", "στρέμματα": "στρέμμα — stremma (1,000 m²)", "καλλιεργήσω": "καλλιεργώ — to cultivate", "κλαδέψω": "κλαδεύω — to prune", "δάκο": "δάκος — olive fruit fly", "υπομονετικά": "υπομονετικά — patiently"}
})

ITEMS.append({
 "id": "l103-c1-mousiki-kai-ponos", "title": "Μπορεί η μουσική να μειώσει τον πόνο;", "title_en": "Can music reduce pain?", "type": "monologue", "level": "C1",
 "context_el": "Ακούτε απόσπασμα από την ομιλία μιας αναισθησιολόγου σε μια εκδήλωση για το κοινό.",
 "script": [
  L("Ομιλήτρια", "f", "Όταν μιλάμε για τη διαχείριση του πόνου, σκεφτόμαστε συνήθως φάρμακα. Τις τελευταίες δεκαετίες, ωστόσο, πληθαίνουν οι μελέτες που εξετάζουν κάτι πολύ απλούστερο: τη μουσική.", "When we talk about pain management, we usually think of drugs. In recent decades, however, there has been a growing number of studies examining something much simpler: music."),
  L("Ομιλήτρια", "f", "Το 2015 μια ομάδα Βρετανών ερευνητών δημοσίευσε στο ιατρικό περιοδικό Λάνσετ μια ανάλυση δεκάδων κλινικών μελετών με χιλιάδες ασθενείς που είχαν υποβληθεί σε χειρουργικές επεμβάσεις. Όσοι άκουγαν μουσική πριν, κατά τη διάρκεια ή μετά την επέμβαση ανέφεραν λιγότερο πόνο και λιγότερο άγχος, και χρειάστηκαν μικρότερες δόσεις παυσίπονων.", "In 2015 a team of British researchers published in the medical journal The Lancet an analysis of dozens of clinical studies with thousands of patients who had undergone surgery. Those who listened to music before, during or after the operation reported less pain and less anxiety, and needed smaller doses of painkillers."),
  L("Ομιλήτρια", "f", "Πώς εξηγείται αυτό; Ένα μέρος της απάντησης είναι η απόσπαση της προσοχής: ο εγκέφαλος έχει περιορισμένη ικανότητα επεξεργασίας, και ό,τι τον απασχολεί ευχάριστα αφήνει λιγότερο χώρο στον πόνο. Υπάρχουν επίσης ενδείξεις ότι η μουσική που μας αρέσει ενεργοποιεί το σύστημα ανταμοιβής του εγκεφάλου, το ίδιο σύστημα που εμπλέκεται στην ευχαρίστηση.", "How can this be explained? Part of the answer is distraction: the brain has a limited processing capacity, and whatever occupies it pleasantly leaves less room for pain. There is also evidence that music we like activates the brain's reward system, the same system involved in pleasure."),
  L("Ομιλήτρια", "f", "Δεν πρόκειται, βέβαια, για υποκατάστατο των φαρμάκων, αλλά για ένα συμπλήρωμα σχεδόν χωρίς κόστος και χωρίς παρενέργειες. Ενδιαφέρον έχει ότι οι ασθενείς φαίνεται να ωφελούνται ακόμη κι όταν βρίσκονται υπό γενική αναισθησία, κάτι που δείχνει πόσα λίγα ξέρουμε ακόμη για το τι αντιλαμβάνεται ο εγκέφαλος.", "It is not, of course, a substitute for drugs, but a supplement with almost no cost and no side effects. Interestingly, patients seem to benefit even when they are under general anaesthesia, which shows how little we still know about what the brain perceives."),
 ],
 "questions": [
  Q("Τι εξέτασε η ανάλυση του 2015;", ["Μία μόνο μελέτη σε μουσικούς", "Την επίδραση των φαρμάκων στη μουσική ικανότητα", "Δεκάδες κλινικές μελέτες με χιλιάδες ασθενείς που είχαν χειρουργηθεί", "Πειράματα σε ζώα"], 2, "μια ανάλυση δεκάδων κλινικών μελετών με χιλιάδες ασθενείς που είχαν υποβληθεί σε χειρουργικές επεμβάσεις"),
  Q("Ποια εξήγηση δίνει πρώτα η ομιλήτρια;", ["Την απόσπαση της προσοχής", "Ότι η μουσική χαλαρώνει τους μυς", "Ότι οι ασθενείς κοιμούνται", "Ότι η μουσική δρα σαν φάρμακο στο αίμα"], 0, "Ένα μέρος της απάντησης είναι η απόσπαση της προσοχής"),
  Q("Πώς χαρακτηρίζει τη μουσική σε σχέση με τα φάρμακα;", ["Ως υποκατάστατό τους", "Ως συμπλήρωμα σχεδόν χωρίς κόστος και χωρίς παρενέργειες", "Ως επικίνδυνη", "Ως ακριβή θεραπεία"], 1, "ένα συμπλήρωμα σχεδόν χωρίς κόστος και χωρίς παρενέργειες"),
  Q("Τι θεωρεί ενδιαφέρον;", ["Ότι μόνο η κλασική μουσική βοηθά", "Ότι οι γιατροί δεν δέχονται τα αποτελέσματα", "Ότι τα παιδιά δεν ωφελούνται", "Ότι οι ασθενείς ωφελούνται ακόμη κι υπό γενική αναισθησία"], 3, "οι ασθενείς φαίνεται να ωφελούνται ακόμη κι όταν βρίσκονται υπό γενική αναισθησία"),
 ],
 "gloss": {"αναισθησιολόγου": "αναισθησιολόγος — anaesthetist", "διαχείριση": "διαχείριση — management", "πληθαίνουν": "πληθαίνω — to increase in number", "κλινικών": "κλινικός — clinical", "δόσεις": "δόση — dose", "παυσίπονων": "παυσίπονο — painkiller", "απόσπαση": "απόσπαση της προσοχής — distraction", "επεξεργασίας": "επεξεργασία — processing", "ανταμοιβής": "ανταμοιβή — reward", "εμπλέκεται": "εμπλέκομαι — to be involved", "υποκατάστατο": "υποκατάστατο — substitute", "παρενέργειες": "παρενέργεια — side effect", "αναισθησία": "αναισθησία — anaesthesia"}
})

ITEMS.append({
 "id": "l103-c1-paradoxo-diakopon", "title": "Το παράδοξο των διακοπών", "title_en": "The holiday paradox", "type": "interview", "level": "C1",
 "context_el": "Σε μια εκπομπή για την επιστήμη, μια δημοσιογράφος συζητά με έναν ψυχολόγο για την αίσθηση του χρόνου.",
 "script": [
  L("Δημοσιογράφος", "f", "Όλοι το έχουμε ζήσει: οι διακοπές περνούν σαν αστραπή, αλλά όταν γυρίζουμε, μας φαίνεται ότι λείπαμε πολύ καιρό. Πώς εξηγείται;", "We've all experienced it: holidays go by in a flash, but when we get back, it feels as if we'd been away a long time. How can that be explained?"),
  L("Ψυχολόγος", "m", "Η Βρετανίδα συγγραφέας Κλόντια Χάμοντ το ονόμασε «παράδοξο των διακοπών». Η εξήγηση βρίσκεται στη διαφορά ανάμεσα στον χρόνο όπως τον ζούμε και στον χρόνο όπως τον θυμόμαστε. Όταν περνάμε καλά και όλα είναι καινούργια, δεν κοιτάμε το ρολόι, και ο χρόνος φεύγει γρήγορα.", "The British writer Claudia Hammond called it the 'holiday paradox'. The explanation lies in the difference between time as we live it and time as we remember it. When we are having a good time and everything is new, we don't look at the clock, and time flies."),
  L("Δημοσιογράφος", "f", "Και γιατί μετά μας φαίνονται μεγάλες;", "And why do they seem long afterwards?"),
  L("Ψυχολόγος", "m", "Γιατί η μνήμη μετρά τον χρόνο με βάση τον αριθμό των νέων εμπειριών. Μια εβδομάδα σε ένα άγνωστο μέρος είναι γεμάτη πρωτόγνωρες εικόνες, και ο εγκέφαλος αποθηκεύει πολλές ξεχωριστές αναμνήσεις. Όταν τις ανακαλούμε, η εβδομάδα μοιάζει μακριά. Αντίθετα, μια εβδομάδα ρουτίνας στο γραφείο αφήνει ελάχιστα ίχνη και στη μνήμη συρρικνώνεται.", "Because memory measures time by the number of new experiences. A week in an unfamiliar place is full of new images, and the brain stores many separate memories. When we recall them, the week seems long. By contrast, a week of routine at the office leaves very few traces and shrinks in memory."),
  L("Δημοσιογράφος", "f", "Αυτό εξηγεί και γιατί τα χρόνια περνούν πιο γρήγορα όσο μεγαλώνουμε;", "Does that also explain why the years go by faster as we get older?"),
  L("Ψυχολόγος", "m", "Είναι μία από τις πιθανές εξηγήσεις. Στα παιδικά χρόνια σχεδόν όλα είναι πρώτη φορά. Αργότερα, η ζωή αποκτά επαναλήψεις. Η πρακτική συμβουλή που προκύπτει είναι απλή: αν θέλουμε η ζωή μας να μοιάζει πιο γεμάτη όταν την κοιτάμε πίσω, χρειαζόμαστε καινούργιες εμπειρίες, έστω και μικρές, όπως έναν διαφορετικό δρόμο για το σπίτι.", "It's one of the possible explanations. In childhood almost everything is a first time. Later, life acquires repetitions. The practical advice that follows is simple: if we want our life to look fuller when we look back on it, we need new experiences, even small ones, like a different route home."),
 ],
 "questions": [
  Q("Ποιος έδωσε το όνομα «παράδοξο των διακοπών»;", ["Ένας Έλληνας ψυχολόγος", "Ένας νευρολόγος", "Ένα ταξιδιωτικό γραφείο", "Η Βρετανίδα συγγραφέας Κλόντια Χάμοντ"], 3, "Η Βρετανίδα συγγραφέας Κλόντια Χάμοντ το ονόμασε «παράδοξο των διακοπών»"),
  Q("Με βάση τι μετρά η μνήμη τον χρόνο, σύμφωνα με τον ψυχολόγο;", ["Με βάση τον αριθμό των νέων εμπειριών", "Με βάση τις ώρες ύπνου", "Με βάση το ρολόι", "Με βάση την κούραση"], 0, "η μνήμη μετρά τον χρόνο με βάση τον αριθμό των νέων εμπειριών"),
  Q("Τι συμβαίνει στη μνήμη με μια εβδομάδα ρουτίνας;", ["Μεγαλώνει", "Συρρικνώνεται", "Μένει ίδια", "Σβήνει εντελώς"], 1, "στη μνήμη συρρικνώνεται"),
  Q("Ποια πρακτική συμβουλή δίνει;", ["Να παίρνουμε περισσότερες άδειες", "Να κοιτάμε συχνά το ρολόι", "Να αναζητάμε καινούργιες εμπειρίες, έστω και μικρές", "Να κρατάμε ημερολόγιο"], 2, "χρειαζόμαστε καινούργιες εμπειρίες, έστω και μικρές"),
 ],
 "gloss": {"αστραπή": "αστραπή — lightning; σαν αστραπή — in a flash", "παράδοξο": "παράδοξο — paradox", "πρωτόγνωρες": "πρωτόγνωρος — never experienced before", "αποθηκεύει": "αποθηκεύω — to store", "ανακαλούμε": "ανακαλώ — to recall", "ίχνη": "ίχνος — trace", "συρρικνώνεται": "συρρικνώνομαι — to shrink", "επαναλήψεις": "επανάληψη — repetition", "προκύπτει": "προκύπτω — to follow, result"}
})

rnd = random.Random(103)  # spread the right answers over the four positions (the page shows options in file order)
for it in ITEMS:
    for q in it["questions"]: rnd.shuffle(q["options"])
for it in ITEMS:
    for q in it["questions"]: assert q["answer"] in q["options"], (it["id"], q["q"])
    for k in it["gloss"]:
        if not (any(k in s["el"] for s in it["script"]) or k in it["context_el"]): raise SystemExit(f"gloss key not in text: {it['id']} {k}")
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
with open(os.path.join(root, "library", "listening", "listening-103.json"), "w", encoding="utf-8") as fh:
    json.dump({"items": ITEMS}, fh, ensure_ascii=False, indent=1); fh.write("\n")
print(len(ITEMS), "items,", sum(len(i["questions"]) for i in ITEMS), "questions")
