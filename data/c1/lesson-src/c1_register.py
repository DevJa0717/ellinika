import json, sys
R = [ # everyday, formal, meaning, example formal
 ("φτιάχνω","κατασκευάζω / συντάσσω / διαμορφώνω","make (build / draw up / shape)","συντάσσω έκθεση"),
 ("βάζω","θέτω / τοποθετώ","put, set","θέτω όρους"),
 ("δίνω","παρέχω / χορηγώ","give, provide / grant","παρέχω υπηρεσίες, χορηγώ άδεια"),
 ("παίρνω","λαμβάνω","receive, take","λαμβάνω μέτρα"),
 ("βγάζω","εκδίδω / εξάγω","issue / extract, export","εκδίδω ανακοίνωση"),
 ("λέω","δηλώνω / αναφέρω / επισημαίνω","state / mention / point out","επισημαίνω ότι…"),
 ("δείχνω","καταδεικνύω / φανερώνω","show, demonstrate","τα στοιχεία καταδεικνύουν"),
 ("ψάχνω","αναζητώ / διερευνώ","look for / investigate","διερευνώ το ενδεχόμενο"),
 ("κοιτάζω","εξετάζω","look at, examine","εξετάζουμε τις επιλογές"),
 ("αλλάζω","τροποποιώ / μεταβάλλω","modify / alter","τροποποιώ το κείμενο"),
 ("τελειώνω","ολοκληρώνω / περατώνω","complete","ολοκληρώθηκε η διαδικασία"),
 ("αρχίζω","ξεκινώ / εκκινώ / εγκαινιάζω","start / launch","εγκαινιάζεται η έκθεση"),
 ("σταματάω","διακόπτω / παύω","stop, cease","παύει να ισχύει"),
 ("βοηθάω","συνδράμω / συμβάλλω","assist / contribute","συμβάλλω στην επίλυση"),
 ("χρειάζομαι","απαιτείται / χρήζει + gen.","need, require","το θέμα χρήζει διερεύνησης"),
 ("μπορώ","δύναμαι / είμαι σε θέση","be able","δεν είμαι σε θέση να απαντήσω"),
 ("έχω","διαθέτω / κατέχω","have, possess","διαθέτει εμπειρία"),
 ("είναι","αποτελεί / συνιστά","is, constitutes","αποτελεί πρόκληση"),
 ("γίνεται","πραγματοποιείται / διεξάγεται","takes place","η συνάντηση πραγματοποιήθηκε"),
 ("φαίνεται","διαφαίνεται / καθίσταται εμφανές","it appears","διαφαίνεται βελτίωση"),
 ("πάλι","εκ νέου","again","εξετάζεται εκ νέου"),
 ("μετά","ακολούθως / εν συνεχεία","then, next","εν συνεχεία, θα αναφερθώ…"),
 ("πολύ","ιδιαίτερα / εξαιρετικά","very","ιδιαίτερα σημαντικό"),
 ("τώρα","επί του παρόντος / πλέον","now; nowadays","πλέον είναι σαφές"),
 ("γιατί","διότι / καθώς / δεδομένου ότι","because","διότι δεν υπήρξε συναίνεση"),
 ("αλλά","ωστόσο / εντούτοις","but; however","Εντούτοις, το ζήτημα παραμένει."),
 ("σχεδόν","σχεδόν / κατά προσέγγιση","approximately","κατά προσέγγιση 300 άτομα"),
 ("λεφτά","χρήματα / κονδύλια / πόροι","money / funds / resources","διατίθενται πόροι"),
 ("δουλειά","εργασία / απασχόληση","work / employment","θέσεις απασχόλησης"),
 ("σπίτι","κατοικία / οικία","dwelling / residence","κύρια κατοικία"),
]
L = {
 "el": "Αλλαγή ύφους",
 "title": "Register shifting: φτιάχνω → συντάσσω, βγάζω → εκδίδω, είναι → αποτελεί",
 "section": "C1 · argument and register",
 "goal": "Move one message up or down the register scale on demand: chat, neutral, formal.",
 "blocks": [
  {"type":"text","text":"The C1 exam asks you to **rewrite** a text for another reader (*μετασχηματισμός* 'transformation'): a friendly email becomes a formal letter, a news item becomes a chat. Educated Greeks do this constantly, and the switch is mostly lexical: a few dozen everyday verbs each have a learned partner. Learn them as **pairs**, so either one calls up the other."},
  {"type":"table","title":"Thirty register pairs","head":["Everyday","Formal","Meaning","Formal in use"],"rows":[[a,f"**{b}**",c,f"*{d}*"] for a,b,c,d in R]},
  {"type":"callout","text":"**Don't overshoot.** Mixing a learned verb into a casual sentence sounds comic: *Θα λάβω ένα σουβλάκι* 'I shall receive a souvlaki'. The other mistake is the reverse: *φτιάξαμε μια έκθεση* in a report. Neutral Greek, the register of a good newspaper, sits in between: *ετοιμάσαμε μια έκθεση, ξεκίνησε η διαδικασία, δόθηκε παράταση*.\n\n**χρήζει + genitive** ('requires') is a pure-written marker: *Το θέμα χρήζει περαιτέρω διερεύνησης.*"},
  {"type":"table","title":"One message, three registers","head":["Register","Text"],"rows":[
    ["Chat","*Ρε συ, ο Νίκος δεν μπορεί να έρθει αύριο, θα το κάνουμε την άλλη βδομάδα.*"],
    ["Neutral","*Ο Νίκος δεν μπορεί να έρθει αύριο, οπότε η συνάντηση μεταφέρεται για την επόμενη εβδομάδα.*"],
    ["Formal","*Λόγω κωλύματος του κ. Παπαδόπουλου, η συνεδρίαση αναβάλλεται και θα πραγματοποιηθεί την ερχόμενη εβδομάδα.*"],
    ["Chat","*Τα νούμερα δείχνουν ότι η ανεργία έπεσε, αλλά οι νέοι ακόμα δεν βρίσκουν δουλειά.*"],
    ["Formal","*Τα στοιχεία καταδεικνύουν μείωση της ανεργίας· εντούτοις, η απασχόληση των νέων παραμένει χαμηλή.*"]]},
  {"type":"culture","title":"Πληθυντικός ευγενείας και κ.κ.","text":"Register in Greek is also grammar: the polite plural (*Τι κάνετε;*), titles (*κύριε καθηγητά*, *κυρία πρόεδρε*, the learned vocative -ά of καθηγητής), and abbreviations in letters: **κ.** (κύριος/κυρία), **κ.κ.** (κύριοι), **Αξιότιμε κύριε** 'Dear Sir', **Με εκτίμηση** 'Yours sincerely'. In an email to a professor or an official, *Αξιότιμε κύριε Παπαδόπουλε* is still normal; in a company, colleagues of all ages use first names and the singular *εσύ* within days."},
  {"type":"reading","title":"Από το μήνυμα στην επιστολή","text":"**Μήνυμα σε φίλο:**\n\nΓεια σου Άρη! Άκου, έψαξα λίγο το θέμα με το διαμέρισμα. Ο ιδιοκτήτης λέει ότι θα φτιάξει τη θέρμανση, αλλά τώρα δεν έχει λεφτά. Μου έδωσε ένα χαρτί να το υπογράψω, αλλά δεν θα το κάνω αν δεν το κοιτάξει πρώτα ένας δικηγόρος. Θα σου πω μετά τι έγινε.\n\n**Επιστολή στον ιδιοκτήτη:**\n\nΑξιότιμε κύριε Δημητρίου,\n\nσε συνέχεια της συνομιλίας μας, θα ήθελα να **επισημάνω** ότι η επισκευή της θέρμανσης **αποτελεί** υποχρέωσή σας βάσει του μισθωτηρίου. Κατανοώ ότι **επί του παρόντος** δεν **διαθέτετε** τους απαιτούμενους **πόρους**· ωστόσο, το ζήτημα **χρήζει** άμεσης αντιμετώπισης ενόψει του χειμώνα.\n\nΌσον αφορά το έγγραφο που μου **παραδώσατε**, δεν **είμαι σε θέση** να το υπογράψω πριν το **εξετάσει** νομικός σύμβουλος. **Εν συνεχεία**, θα επικοινωνήσω μαζί σας για τη **διευθέτηση** του θέματος.\n\nΜε εκτίμηση,\nΆννα Κωστοπούλου","en":"Message to a friend: Hi Aris! Listen, I looked into the flat thing a bit. The landlord says he'll fix the heating, but he has no money right now. He gave me a paper to sign, but I won't do it unless a lawyer looks at it first. I'll tell you later what happened.\n\nLetter to the landlord: Dear Mr Dimitriou, further to our conversation, I would like to point out that repairing the heating is your obligation under the lease. I understand that you do not at present have the necessary resources; however, the matter requires immediate attention in view of the winter. As regards the document you handed me, I am not in a position to sign it before a legal adviser has examined it. I shall then contact you to settle the matter. Yours sincerely, Anna Kostopoulou",
   "gloss":{"μισθωτηρίου":"lease (gen.)","ενόψει":"in view of","διευθέτηση":"settlement, arrangement","νομικός σύμβουλος":"legal adviser","σε συνέχεια":"further to"},
   "questions":[
    {"prompt":"Ποια φράση της επιστολής αντιστοιχεί στο «τώρα δεν έχει λεφτά»;","answer":"επί του παρόντος δεν διαθέτετε τους απαιτούμενους πόρους","options":["επί του παρόντος δεν διαθέτετε τους απαιτούμενους πόρους","χρήζει άμεσης αντιμετώπισης","αποτελεί υποχρέωσή σας","δεν είμαι σε θέση"],"why":"τώρα → επί του παρόντος, έχει → διαθέτετε, λεφτά → πόροι."},
    {"prompt":"Ποια λέξη της επιστολής αντιστοιχεί στο «κοιτάξει»;","answer":"εξετάσει","options":["εξετάσει","επισημάνω","παραδώσατε","διευθέτηση"],"why":"κοιτάζω → εξετάζω."}]}
 ],
 "practice": [
  {"gen":"type","n":12,"items":[{"prompt":f"Formal equivalent of **{a}** ({c})","answer":b.split(" / ")[0],"accept":[x.split(" + ")[0] for x in b.split(" / ")],"why":f"{a} → {b}: *{d}*"} for a,b,c,d in R if a!="σχεδόν"]},
  {"gen":"mc","items":[
    {"prompt":"Η εταιρεία ___ ανακοίνωση για το περιστατικό. (formal 'put out')","answer":"εξέδωσε","options":["εξέδωσε","έβγαλε","έκανε","έδωσε"],"why":"βγάζω ανακοίνωση → εκδίδω ανακοίνωση."},
    {"prompt":"Η ανεργία ___ το μεγαλύτερο πρόβλημα της περιοχής. (formal 'is')","answer":"αποτελεί","options":["αποτελεί","είναι σαν","υφίσταται","γίνεται"],"why":"είναι → αποτελεί."},
    {"prompt":"Το ζήτημα ___ περαιτέρω διερεύνησης.","answer":"χρήζει","options":["χρήζει","χρειάζεται","απαιτεί","ζητάει"],"why":"Only χρήζει takes the genitive; the others take the accusative."},
    {"prompt":"Which is the comic register clash?","answer":"Θα λάβω έναν φρέντο, παρακαλώ.","options":["Θα λάβω έναν φρέντο, παρακαλώ.","Θα πάρω έναν φρέντο, παρακαλώ.","Λάβαμε την επιστολή σας.","Πήραμε το μήνυμά σου."],"why":"λαμβάνω belongs to letters, not to a café counter."},
    {"prompt":"Η συνάντηση ___ στο Υπουργείο. (formal 'took place')","answer":"πραγματοποιήθηκε","options":["πραγματοποιήθηκε","έγινε σαν","κατέστη","επήλθε"],"why":"γίνεται → πραγματοποιείται."},
    {"prompt":"Ο υποψήφιος ___ μεγάλη εμπειρία. (formal 'has')","answer":"διαθέτει","options":["διαθέτει","κατέχεται","έχεται","χρήζει"],"why":"έχω → διαθέτω."}]}
 ]
}
json.dump(L, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
