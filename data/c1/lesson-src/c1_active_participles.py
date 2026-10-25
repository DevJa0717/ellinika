import json, sys
NEUT = [("το περιβάλλον","του περιβάλλοντος","τα περιβάλλοντα","environment"),
 ("το ενδιαφέρον","του ενδιαφέροντος","τα ενδιαφέροντα","interest"),
 ("το συμφέρον","του συμφέροντος","τα συμφέροντα","(self-)interest"),
 ("το προϊόν","του προϊόντος","τα προϊόντα","product"),
 ("το παρελθόν","του παρελθόντος","—","the past"),
 ("το μέλλον","του μέλλοντος","—","the future"),
 ("το παρόν","του παρόντος","—","the present"),
 ("το καθήκον","του καθήκοντος","τα καθήκοντα","duty; pl. duties of a post"),
 ("το προσόν","του προσόντος","τα προσόντα","qualification, asset"),
 ("το σύμπαν","του σύμπαντος","—","universe"),
 ("το φωνήεν","του φωνήεντος","τα φωνήεντα","vowel"),
 ("το ον","του όντος","τα όντα","being"),
 ("το επείγον","του επείγοντος","τα επείγοντα","urgent matter; τα επείγοντα = A&E")]
AGREE = [
 ("Η ___ νομοθεσία δεν το επιτρέπει. (ισχύω)","ισχύουσα",["ισχύουσα","ισχύων","ισχύον","ισχύοντα"],"Feminine nom.: ισχύουσα. ο ισχύων νόμος, το ισχύον καθεστώς."),
 ("Ο ___ σύμβουλος παραιτήθηκε. (διευθύνω)","διευθύνων",["διευθύνων","διευθύνοντας","διευθύνον","διευθυνόμενος"],"ο διευθύνων σύμβουλος = CEO. διευθύνοντας is the gerund."),
 ("Οι βουλευτές του ___ κόμματος ψήφισαν υπέρ. (κυβερνώ)","κυβερνώντος",["κυβερνώντος","κυβερνών","κυβερνώντα","κυβερνούντος"],"Genitive of το κυβερνών (κόμμα): του κυβερνώντος."),
 ("Ευχαριστούμε όλους τους ___ στο συνέδριο. (συμμετέχω)","συμμετέχοντες",["συμμετέχοντες","συμμετέχοντας","συμμετέχουσες","συμμετέχων"],"Accusative plural masculine: τους συμμετέχοντες (same as nom.). συμμετέχοντας is the gerund."),
 ("Η ___ της Κύπρου είναι η Λευκωσία.","πρωτεύουσα",["πρωτεύουσα","πρωτεύων","πρωτεύον","πρώτη πόλη"],"πρωτεύουσα 'capital' is a fossilised participle of πρωτεύω 'come first'."),
 ("Τον έστειλαν στα ___ με πυρετό 40.","επείγοντα",["επείγοντα","επείγον","επείγουσα","επειγόντων"],"τα επείγοντα (περιστατικά) = A&E."),
 ("Τα ___ του ηλικιωμένου μοιράστηκαν στα παιδιά του. (υπάρχω)","υπάρχοντα",["υπάρχοντα","υπάρχον","υπάρχουσα","υπάρχοντες"],"τα υπάρχοντα 'belongings'."),
 ("Οι ___ από τον σεισμό μίλησαν στους δημοσιογράφους. (επιζώ)","επιζώντες",["επιζώντες","επιζώντας","επιζούντες","επιζών"],"ο επιζών, οι επιζώντες 'survivors'."),
 ("Η ___ έκθεση εξετάζει τρία ζητήματα. (this report)","παρούσα",["παρούσα","παρούσης","παρόν","παρών"],"η παρούσα έκθεση 'the present report'."),
 ("Ο Γιάννης ήταν ___ στη συνεδρίαση. (absent)","απών",["απών","απόντας","απούσα","απόν"],"ο απών / η απούσα / οι απόντες."),
 ("Σε ζητήματα ___ σημασίας, αποφασίζει η Ολομέλεια. (urgent, fem. gen. sg.)","επείγουσας",["επείγουσας","επειγούσης","επείγοντος","επείγουσα"],"της επείγουσας (formal also επειγούσης)."),
 ("Οι ___ γλώσσες της Ευρώπης (ζω)","ζώσες",["ζώσες","ζώντας","ζώντες","ζούσες"],"ζων, ζώσα, ζων: οι ζώσες γλώσσες 'living languages'. ζώντας is the gerund.")]
L = {
 "el": "Ενεργητικές μετοχές σε -ων",
 "title": "Active participles: ο ενδιαφέρων, η ισχύουσα, το περιβάλλον",
 "section": "C1 · learned morphology",
 "goal": "Decline the learned active participles and the everyday nouns built from them (περιβάλλον, προϊόν, συμφέρον) without slipping on the genitive.",
 "blocks": [
  {"type":"text","text":"Ancient Greek had a full active participle (*λύων, λύουσα, λῦον* 'loosing'). Spoken Modern Greek kept only the frozen gerund in -οντας, but the learned language preserved the declined participle, and a few dozen of them are everywhere in formal Greek: **ο ισχύων νόμος** 'the law in force', **ο διευθύνων σύμβουλος** 'the CEO', **η τρέχουσα κατάσταση** 'the current situation', **οι συμμετέχοντες** 'the participants'. More important still, many common neuter nouns are old participles and decline like them: **το περιβάλλον, του περιβάλλοντος**."},
  {"type":"table","title":"ενδιαφέρων 'interesting' (from ενδιαφέρω)","head":["","Masculine","Feminine","Neuter"],"rows":[
    ["Nom. sg.","ο ενδιαφέρ**ων**","η ενδιαφέρ**ουσα**","το ενδιαφέρ**ον**"],
    ["Gen. sg.","του ενδιαφέρ**οντος**","της ενδιαφέρ**ουσας**","του ενδιαφέρ**οντος**"],
    ["Acc. sg.","τον ενδιαφέρ**οντα**","την ενδιαφέρ**ουσα**","το ενδιαφέρ**ον**"],
    ["Nom. pl.","οι ενδιαφέρ**οντες**","οι ενδιαφέρ**ουσες**","τα ενδιαφέρ**οντα**"],
    ["Gen. pl.","των ενδιαφερ**όντων**","των ενδιαφερ**ουσών**","των ενδιαφερ**όντων**"],
    ["Acc. pl.","τους ενδιαφέρ**οντες**","τις ενδιαφέρ**ουσες**","τα ενδιαφέρ**οντα**"]]},
  {"type":"table","title":"Contracted type, from -ώ verbs: κυβερνών 'governing'","head":["","Masculine","Feminine","Neuter"],"rows":[
    ["Nom. sg.","ο κυβερν**ών**","η κυβερν**ώσα**","το κυβερν**ών**"],
    ["Gen. sg.","του κυβερν**ώντος**","της κυβερν**ώσας**","του κυβερν**ώντος**"],
    ["Acc. sg.","τον κυβερν**ώντα**","την κυβερν**ώσα**","το κυβερν**ών**"],
    ["Nom./Acc. pl.","οι/τους κυβερν**ώντες**","οι/τις κυβερν**ώσες**","τα κυβερν**ώντα**"],
    ["Gen. pl.","των κυβερν**ώντων**","των κυβερν**ωσών**","των κυβερν**ώντων**"]]},
  {"type":"callout","text":"**Vowel of the contracted type:** verbs in -άω/-ώ (αγαπώ type) give -ών, -ώσα, -ώντος (κυβερνών, επιζών, ζων/ζώσα); verbs in -ώ/-είς (θεωρώ type) give -ών, -ούσα, -ούντος (ο αιτών, η αιτούσα, οι αιτούντες 'the applicants'). Forms printed on every application form: **ο αιτών / η αιτούσα**.\n\n**Don't confuse it with the gerund.** *Οι συμμετέχοντες ήρθαν* 'the participants came' (declined participle) vs *Συμμετέχοντας στο συνέδριο, γνώρισα πολλούς* 'by taking part…' (invariable gerund, stress pattern identical!). The article tells you which one it is."},
  {"type":"table","title":"Everyday nouns that are old participles","head":["Nominative","Genitive","Plural","Meaning"],"rows":[[f"**{a}**",b,c,d] for a,b,c,d in NEUT]},
  {"type":"table","title":"Participles to recognise and use","head":["Participle","Typical phrase","Meaning"],"rows":[
    ["ισχύων, -ουσα, -ον","ο ισχύων νόμος, η ισχύουσα νομοθεσία, τα ισχύοντα","in force"],
    ["τρέχων","η τρέχουσα χρονιά, τα τρέχοντα","current; current affairs"],
    ["διευθύνων","ο διευθύνων σύμβουλος","managing (director)"],
    ["προεδρεύων","ο προεδρεύων της συνεδρίασης","chairing"],
    ["συμμετέχων","οι συμμετέχοντες","participant"],
    ["υπάρχων","η υπάρχουσα υποδομή, τα υπάρχοντα","existing; belongings"],
    ["παρών / απών","η παρούσα έκθεση, οι απόντες","present / absent"],
    ["μέλλων","η μέλλουσα σύζυγος, ο μέλλων πρόεδρος","future, -to-be"],
    ["επείγων","επείγουσα ανάγκη, τα επείγοντα","urgent; A&E"],
    ["κυβερνών","το κυβερνών κόμμα","ruling"],
    ["αιτών","ο αιτών, η αιτούσα, οι αιτούντες","applicant"],
    ["επιζών","οι επιζώντες","survivor"],
    ["ζων","οι ζώσες γλώσσες","living"],
    ["δέων","η δέουσα προσοχή, τα δέοντα, δεόντως","due; what is proper"],
    ["πρωτεύων","η πρωτεύουσα","capital city"]]},
  {"type":"culture","title":"Τα επείγοντα και η πρωτεύουσα","text":"Some of these participles are so common that nobody feels them as learned: you go to **τα επείγοντα** 'A&E' at the hospital, you live in **την πρωτεύουσα**, you worry about **το μέλλον** and **το περιβάλλον**. Others are a register marker: **δεόντως** 'duly, properly' is the bureaucrat's word, and a friend saying *σε ευχαριστώ δεόντως* is being playfully pompous. A classic schoolroom error, mocked in the press, is *του περιβάλλον* instead of **του περιβάλλοντος**."},
  {"type":"reading","title":"Το μέλλον της πόλης","text":"Η δημοτική αρχή παρουσίασε χθες το νέο σχέδιο για την προστασία **του περιβάλλοντος** στο κέντρο της πόλης. Σύμφωνα με τον δήμαρχο, η **υπάρχουσα** υποδομή δεν επαρκεί πλέον, και η **ισχύουσα** νομοθεσία επιτρέπει στον δήμο να απαγορεύσει την κυκλοφορία των αυτοκινήτων σε όλο το ιστορικό τρίγωνο.\n\nΤο σχέδιο προκάλεσε έντονο **ενδιαφέρον**. Οι **συμμετέχοντες** στη δημόσια διαβούλευση, κάτοικοι και επαγγελματίες, εξέφρασαν διαφορετικές απόψεις: οι πρώτοι μίλησαν για την ποιότητα ζωής, οι δεύτεροι για τα **συμφέροντα** της αγοράς, που ήδη πλήττεται από την **τρέχουσα** οικονομική συγκυρία.\n\n«Δεν μπορούμε να ζούμε στο **παρελθόν**», δήλωσε ο αντιδήμαρχος. «Το **μέλλον** της πόλης εξαρτάται από τις αποφάσεις του **παρόντος**.» Οι **αιτούντες** άδεια εισόδου, όπως οι προμηθευτές τοπικών **προϊόντων**, θα πρέπει να υποβάλουν τα σχετικά δικαιολογητικά έως το τέλος της **τρέχουσας** χρονιάς.","en":"Yesterday the municipal authority presented its new plan to protect the environment in the city centre. According to the mayor, the existing infrastructure is no longer adequate, and the legislation in force allows the municipality to ban car traffic in the whole historic triangle.\n\nThe plan aroused keen interest. Participants in the public consultation, residents and business owners, expressed different views: the former spoke of quality of life, the latter of the interests of the market, already hit by the current economic conjuncture.\n\n'We cannot live in the past,' the deputy mayor said. 'The future of the city depends on the decisions of the present.' Applicants for an entry permit, such as suppliers of local products, will have to submit the relevant documents by the end of the current year.",
   "gloss":{"δημοτική αρχή":"municipal authority","επαρκεί":"suffices","διαβούλευση":"consultation","πλήττεται":"is hit, suffers","συγκυρία":"conjuncture, circumstances","αντιδήμαρχος":"deputy mayor","δικαιολογητικά":"supporting documents","προμηθευτές":"suppliers"},
   "questions":[
    {"prompt":"Τι επιτρέπει η ισχύουσα νομοθεσία στον δήμο;","answer":"Να κλείσει το ιστορικό κέντρο στα αυτοκίνητα.","options":["Να κλείσει το ιστορικό κέντρο στα αυτοκίνητα.","Να χτίσει νέα υποδομή.","Να αυξήσει τους φόρους των καταστημάτων.","Να ακυρώσει τη διαβούλευση."],"why":"να απαγορεύσει την κυκλοφορία των αυτοκινήτων σε όλο το ιστορικό τρίγωνο."},
    {"prompt":"Για τι ανησυχούν κυρίως οι επαγγελματίες;","answer":"Για την αγορά, που ήδη δυσκολεύεται.","options":["Για την αγορά, που ήδη δυσκολεύεται.","Για την ποιότητα ζωής.","Για το παρελθόν της πόλης.","Για την έλλειψη προϊόντων."],"why":"οι δεύτεροι για τα συμφέροντα της αγοράς, που ήδη πλήττεται."}]}
 ],
 "practice": [
  {"gen":"mc","items":[{"prompt":p,"answer":a,"options":o,"why":w} for p,a,o,w in AGREE]},
  {"gen":"type","n":8,"items":[{"prompt":f"Genitive singular: **{a}** ({d})","answer":b,"accept":[b,b.split(' ',1)[1]],"why":f"{a}, {b}"} for a,b,c,d in NEUT]+
    [{"prompt":f"Plural: **{a}** ({d})","answer":c,"accept":[c,c.split(' ',1)[1]],"why":f"{a}, {c}"} for a,b,c,d in NEUT if c!="—"]},
  {"gen":"type","n":6,"items":[
    {"prompt":"ενδιαφέρων: genitive plural (των ___)","answer":"ενδιαφερόντων","why":"Stress moves to -όντων in the genitive plural."},
    {"prompt":"ενδιαφέρων: feminine accusative singular (την ___ πρόταση)","answer":"ενδιαφέρουσα"},
    {"prompt":"ενδιαφέρων: masculine accusative singular (τον ___ ομιλητή)","answer":"ενδιαφέροντα"},
    {"prompt":"ισχύων: neuter nom. plural (τα ___)","answer":"ισχύοντα"},
    {"prompt":"τρέχων: feminine genitive singular (της ___ χρονιάς)","answer":"τρέχουσας","accept":["τρέχουσας","τρεχούσης"]},
    {"prompt":"αιτών: masculine nom. plural (οι ___)","answer":"αιτούντες"},
    {"prompt":"κυβερνών: neuter genitive singular (του ___ κόμματος)","answer":"κυβερνώντος"},
    {"prompt":"συμμετέχων: masculine genitive plural (των ___)","answer":"συμμετεχόντων"},
    {"prompt":"παρών: feminine nominative singular (η ___ έκθεση)","answer":"παρούσα"}]}
 ]
}
json.dump(L, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
