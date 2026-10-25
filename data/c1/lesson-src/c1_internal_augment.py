import json, sys
V = [  # present, 3sg past, 1pl past, meaning
 ("υποβάλλω","υπέβαλε","υποβάλαμε","submit"),
 ("επιβάλλω","επέβαλε","επιβάλαμε","impose"),
 ("αναβάλλω","ανέβαλε","αναβάλαμε","postpone"),
 ("συμβάλλω","συνέβαλε","συμβάλαμε","contribute"),
 ("εκλέγω","εξέλεξε","εκλέξαμε","elect"),
 ("αποδεικνύω","απέδειξε","αποδείξαμε","prove"),
 ("καταλήγω","κατέληξε","καταλήξαμε","conclude, end up"),
 ("καταθέτω","κατέθεσε","καταθέσαμε","deposit, testify, table"),
 ("διαθέτω","διέθεσε","διαθέσαμε","allocate, make available"),
 ("εκδίδω","εξέδωσε","εκδώσαμε","publish, issue"),
 ("παραδίδω","παρέδωσε","παραδώσαμε","hand over"),
 ("μεταφέρω","μετέφερε","μεταφέραμε","transfer, carry"),
 ("αναλαμβάνω","ανέλαβε","αναλάβαμε","take on"),
 ("συλλαμβάνω","συνέλαβε","συλλάβαμε","arrest; conceive"),
 ("παραλαμβάνω","παρέλαβε","παραλάβαμε","receive, collect"),
 ("διακόπτω","διέκοψε","διακόψαμε","interrupt"),
 ("εγκρίνω","ενέκρινε","εγκρίναμε","approve"),
 ("εκφράζω","εξέφρασε","εκφράσαμε","express"),
 ("επιστρέφω","επέστρεψε","επιστρέψαμε","return"),
 ("καταστρέφω","κατέστρεψε","καταστρέψαμε","destroy"),
 ("αναπτύσσω","ανέπτυξε","αναπτύξαμε","develop"),
 ("αποφεύγω","απέφυγε","αποφύγαμε","avoid"),
 ("αποτυγχάνω","απέτυχε","αποτύχαμε","fail"),
 ("υπογράφω","υπέγραψε","υπογράψαμε","sign"),
 ("περιγράφω","περιέγραψε","περιγράψαμε","describe"),
 ("προβλέπω","προέβλεψε","προβλέψαμε","foresee, provide for"),
 ("εμπνέω","ενέπνευσε","εμπνεύσαμε","inspire"),
 ("αποκτώ","απέκτησε","αποκτήσαμε","acquire"),
 ("συμπεριλαμβάνω","συμπεριέλαβε","συμπεριλάβαμε","include"),
 ("υπάρχω","υπήρξε","υπήρξαμε","exist, be (once)"),
]
PASS = [("υπογράφτηκε","υπεγράφη","was signed"),("εγκρίθηκε","ενεκρίθη","was approved"),("εκλέχτηκε","εξελέγη","was elected"),
 ("συλλήφθηκε","συνελήφθη","was arrested"),("απορρίφθηκε","απερρίφθη","was rejected"),("εκδόθηκε","εξεδόθη","was issued"),
 ("κατατέθηκε","κατετέθη","was tabled, submitted"),("παραδόθηκε","παρεδόθη","was handed over"),("ανακηρύχτηκε","ανεκηρύχθη","was proclaimed"),
 ("διεξάχθηκε","διεξήχθη","was conducted"),("ανεστάλη","ανεστάλη","was suspended (no colloquial form)"),("πέθανε","απεβίωσε","died (formal: passed away)")]
L = {
 "el": "Εσωτερική αύξηση",
 "title": "Internal augment: υπέβαλε, εξέλεξε, συνέβη",
 "section": "C1 · Holton §6.23",
 "goal": "Produce the past tense of learned compound verbs the way the news, the law and educated speakers do.",
 "blocks": [
  {"type":"rules","src":"grammar/verbs-holton.json#sections[section=6.23].rule","cite":"Holton §6.23"},
  {"type":"table","title":"Prefix + ε + stem","head":["Prefix","Before the augment","Example"],"rows":[
    ["απο-, υπο-, κατα-, ανα-, δια-, μετα-, παρα-, επι-, αντι-","drops its vowel","απο-δείχνω → **απ-έ-δειξε**; κατα-λήγω → **κατ-έ-ληξε**; δια-κόπτω → **δι-έ-κοψε**"],
    ["εκ-","becomes **εξ-**","εκλέγω → **εξέλεξε**; εκδίδω → **εξέδωσε**; εκφράζω → **εξέφρασε**"],
    ["εν- (εμ-, εγ-)","returns to **εν-**","εγκρίνω → **ενέκρινε**; εμπνέω → **ενέπνευσε**"],
    ["συν- (συμ-, συγ-, συλ-)","returns to **συν-**","συμβάλλω → **συνέβαλε**; συλλαμβάνω → **συνέλαβε**; συμβαίνει → **συνέβη**"],
    ["περι-, προ-","keep their vowel","περιγράφω → **περιέγραψε**; προβλέπω → **προέβλεψε**"],
    ["prefix + vowel stem","vowel lengthens to **η**","υπάρχω → **υπήρξε**; εξηγώ → **εξήγησε**; εισάγω → **εισήγαγε**"]]},
  {"type":"callout","text":"**The augment only appears when it is stressed.** Greek stress can go back at most three syllables, so the augment shows up in the 1sg, 2sg, 3sg and 3pl of the past (υπέβαλα, υπέβαλες, υπέβαλε, υπέβαλαν) and vanishes when the ending adds a syllable: **υποβάλαμε, υποβάλατε**. The same holds for the long 3pl: υπέβαλαν but **υποβάλανε**.\n\n**Never augmented:** προτείνω → πρότεινε, απαγορεύω → απαγόρευσε, συνεχίζω → συνέχισε, and all second-conjugation compounds in -ώ/-ησα with a stressed ending (παρακολουθώ → παρακολούθησε, αντιδρώ → αντέδρασε)."},
  {"type":"table","title":"Thirty verbs to own","head":["Present","He/she …ed","We …ed","Meaning"],"rows":[[f"**{a}**",f"**{b}**",c,d] for a,b,c,d in V]},
  {"type":"text","title":"Register: who says what","text":"In speech many people drop the internal augment and say *υπόγραψε, παράδωσε, ανάλαβε*, or put it at the front (*εκλέξανε*, *έκανε κατάθεση*). These forms are fine in a kafeneio but sound uneducated in an interview, a meeting or an essay. At C1 you are expected to use the internal augment in writing and in formal speech, and to recognise the learned passive pasts below in every news bulletin."},
  {"type":"table","title":"Learned passive pasts in the news","head":["Everyday","News and official","Meaning"],"rows":[[a,f"**{b}**",c] for a,b,c in PASS]},
  {"type":"culture","title":"Ο υπουργός προέβη σε δηλώσεις","text":"Greek news Greek (*η γλώσσα των δελτίων ειδήσεων*) is the last refuge of many καθαρεύουσα forms. A minister doesn't *say* things, he **προέβη σε δηλώσεις** 'proceeded to statements'; a suspect isn't *caught*, he **συνελήφθη**; a law isn't *voted*, it **ψηφίστηκε** or, more solemnly, **υπερψηφίστηκε**. The verb **προβαίνω σε** + noun is pure officialese and survives almost only in this past form: *προέβη σε συλλήψεις, σε ανακοινώσεις, σε αλλαγές*. Recognising it is C1; using it in conversation sounds like a newsreader, which Greeks find funny."},
  {"type":"reading","title":"Δελτίο ειδήσεων","text":"Η κυβέρνηση **κατέθεσε** χθες στη Βουλή το νέο νομοσχέδιο για την ανώτατη εκπαίδευση. Ο αρμόδιος υπουργός **εξέφρασε** την ικανοποίησή του και **ανέλαβε** τη δέσμευση να ανοίξει ευρύ διάλογο με τα πανεπιστήμια.\n\nΗ αντιπολίτευση **απέρριψε** το κείμενο ως «βιαστικό» και **υπέβαλε** σειρά τροπολογιών. Ο εισηγητής της **υποστήριξε** ότι η κυβέρνηση **απέφυγε** να συμβουλευτεί τους φοιτητές και **κατέληξε** σε ρυθμίσεις που, όπως είπε, **επέβαλε** η ίδια χωρίς διαβούλευση.\n\nΣτο μεταξύ, η Αστυνομία **συνέλαβε** τρία άτομα μετά τα επεισόδια έξω από το Πολυτεχνείο. Σύμφωνα με την ανακοίνωση που **εξεδόθη** το απόγευμα, η συγκέντρωση **διεξήχθη** ειρηνικά μέχρι τις οκτώ, όταν μια ομάδα **διέκοψε** την κυκλοφορία στην Πατησίον.\n\nΤέλος, σε ηλικία 91 ετών **απεβίωσε** ο σκηνοθέτης που **ανέπτυξε** όσο λίγοι το ελληνικό ντοκιμαντέρ. Το έργο του **ενέπνευσε** δύο γενιές κινηματογραφιστών.","en":"Yesterday the government tabled the new bill on higher education in Parliament. The minister responsible expressed his satisfaction and committed himself to opening a broad dialogue with the universities.\n\nThe opposition rejected the text as 'hasty' and submitted a series of amendments. Its rapporteur argued that the government had avoided consulting students and had arrived at provisions which, he said, it had imposed on its own without consultation.\n\nMeanwhile, the police arrested three people after the clashes outside the Polytechnic. According to the statement issued in the afternoon, the gathering was conducted peacefully until eight, when a group blocked traffic on Patission Street.\n\nFinally, the director who did more than almost anyone to develop Greek documentary film has died, aged 91. His work inspired two generations of filmmakers.",
   "gloss":{"νομοσχέδιο":"bill (draft law)","αρμόδιος":"competent, responsible","δέσμευση":"commitment","αντιπολίτευση":"the opposition","τροπολογιών":"amendments (gen. pl.)","εισηγητής":"rapporteur","διαβούλευση":"public consultation","επεισόδια":"clashes, incidents","απεβίωσε":"died (formal)","απέρριψε":"rejected (απορρίπτω)","εξεδόθη":"was issued","διεξήχθη":"was conducted"},
   "questions":[
    {"prompt":"Τι έκανε η αντιπολίτευση με το νομοσχέδιο;","answer":"Το απέρριψε και πρότεινε αλλαγές.","options":["Το απέρριψε και πρότεινε αλλαγές.","Το ψήφισε με επιφυλάξεις.","Ζήτησε να αναβληθεί η συζήτηση.","Το κατέθεσε η ίδια στη Βουλή."],"why":"απέρριψε … και υπέβαλε σειρά τροπολογιών."},
    {"prompt":"Τι κατηγορεί ο εισηγητής την κυβέρνηση ότι δεν έκανε;","answer":"Δεν ρώτησε τους φοιτητές.","options":["Δεν ρώτησε τους φοιτητές.","Δεν κατέθεσε το νομοσχέδιο.","Δεν συνέλαβε κανέναν.","Δεν εξέδωσε ανακοίνωση."],"why":"απέφυγε να συμβουλευτεί τους φοιτητές."},
    {"prompt":"Πώς ήταν η συγκέντρωση μέχρι τις οκτώ;","answer":"Ειρηνική.","options":["Ειρηνική.","Βίαιη.","Αναβλήθηκε.","Απαγορεύτηκε."],"why":"διεξήχθη ειρηνικά μέχρι τις οκτώ."}]}
 ],
 "practice": [
  {"gen":"type","n":10,"items":[{"prompt":f"Simple past, 3sg: **{a}** ({d})","answer":b,"why":f"{a} → {b} (we: {c})."} for a,b,c,d in V]},
  {"gen":"mc","items":[
    {"prompt":"Χθες ___ την αίτηση στο υπουργείο. (we submitted)","answer":"υποβάλαμε","options":["υποβάλαμε","υπεβάλαμε","υπέβαλαμε","υποβάλλαμε"],"why":"Unstressed augment drops: υποβάλαμε. υποβάλλαμε (λλ) is the imperfect."},
    {"prompt":"Ο λαός ___ νέο πρόεδρο. (elected)","answer":"εξέλεξε","options":["εξέλεξε","εκλέξε","έκλεξε","εξέλεγε"],"why":"εκ- becomes εξ- before the augment: εξέλεξε."},
    {"prompt":"Η επιτροπή ___ την πρόταση ομόφωνα. (approved)","answer":"ενέκρινε","options":["ενέκρινε","εγέκρινε","έγκρινε","ενέκρινα"],"why":"εγ- returns to εν-: εν-έ-κρινε."},
    {"prompt":"Ο συγγραφέας ___ με ακρίβεια την Αθήνα του '60. (described)","answer":"περιέγραψε","options":["περιέγραψε","περέγραψε","περίγραψε","περιγράφει"],"why":"περι- keeps its vowel: περι-έ-γραψε."},
    {"prompt":"Ο νόμος ___ αυστηρές ποινές. (provided for)","answer":"προέβλεπε","options":["προέβλεπε","προύβλεπε","πρόβλεπε","προβλέψε"],"why":"Imperfect also takes the internal augment: προ-έ-βλεπε."},
    {"prompt":"Τι ___ χθες στη σύσκεψη; (happened)","answer":"συνέβη","options":["συνέβη","συμβαίνει","σύμβηκε","συνέβαινε"],"why":"συμβαίνει → συνέβη (learned, but the everyday form)."},
    {"prompt":"Η Ελλάδα ___ στην ΕΟΚ το 1981. (was admitted: εντάχθηκε)","answer":"εντάχθηκε","options":["εντάχθηκε","ενέταξε","εντάχτηκε","ενετάχθη"],"why":"Standard modern passive: εντάχθηκε (εντάσσομαι). ενετάγη exists but is archaic."},
    {"prompt":"Ποιο είναι λάθος σε επίσημο κείμενο;","answer":"Ο υπουργός πρότεινε υπόγραψε τη σύμβαση.","options":["Ο υπουργός πρότεινε υπόγραψε τη σύμβαση.","Ο υπουργός υπέγραψε τη σύμβαση.","Η σύμβαση υπεγράφη χθες.","Η σύμβαση υπογράφτηκε χθες."],"why":"υπόγραψε is colloquial; the others are all correct (υπεγράφη formal, υπογράφτηκε neutral)."},
    {"prompt":"Ο υποψήφιος ___ να απαντήσει. (avoided)","answer":"απέφυγε","options":["απέφυγε","απόφυγε","αποφεύγε","αποφύγε"],"why":"απο- drops its vowel: απ-έ-φυγε."},
    {"prompt":"Η εταιρεία ___ πέρσι τρία νέα προϊόντα. (developed)","answer":"ανέπτυξε","options":["ανέπτυξε","ανάπτυξε","αναπτύξε","ανέπτυσσε"],"why":"ανα- drops its vowel: αν-έ-πτυξε."}]},
  {"gen":"type","n":6,"items":[{"prompt":f"Newsreader form of **{a}** ({c})","answer":b,"why":f"{a} = {b}."} for a,b,c in PASS if a!=b]}
 ]
}
L["practice"][1]["items"][7]={"prompt":"Which one is colloquial, not for an essay?","answer":"Ο υπουργός υπόγραψε τη σύμβαση.","options":["Ο υπουργός υπόγραψε τη σύμβαση.","Ο υπουργός υπέγραψε τη σύμβαση.","Η σύμβαση υπεγράφη χθες.","Η σύμβαση υπογράφτηκε χθες."],"why":"υπόγραψε drops the internal augment; the others are correct (υπεγράφη formal, υπογράφτηκε neutral)."}
json.dump(L, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
