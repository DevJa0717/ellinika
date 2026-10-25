import json, sys
FREE = [
 ("όποιος, -α, -ο","whoever","Όποιος θέλει, μπορεί να έρθει."),
 ("ό,τι","whatever","Ό,τι κι αν πεις, δεν αλλάζω γνώμη."),
 ("όσος, -η, -ο","as much/many as; all who","Όσοι διαφωνούν, ας μιλήσουν τώρα."),
 ("όπου","wherever","Όπου κι αν πας, θα σε βρω."),
 ("όποτε","whenever","Όποτε θέλεις, πάρε με τηλέφωνο."),
 ("όπως","however, the way that","Κάν' το όπως νομίζεις."),
 ("οποιοσδήποτε / οτιδήποτε","anyone / anything at all","Οτιδήποτε χρειαστείς, πες μου."),
]
CONC = [
 ("όσο κι αν + ind./subj.","however much","Όσο κι αν προσπάθησε, δεν τα κατάφερε."),
 ("ό,τι κι αν / ό,τι και να","whatever","Ό,τι και να γίνει, θα είμαι εδώ."),
 ("όποιος κι αν","whoever","Όποιος κι αν κερδίσει, τα προβλήματα μένουν."),
 ("όπου κι αν / όπου και να","wherever","Όπου και να ψάξεις, δεν θα το βρεις φθηνότερα."),
 ("όπως και να 'χει","be that as it may, anyway","Όπως και να 'χει, πρέπει να αποφασίσουμε."),
 ("ακόμη κι αν / ακόμα και να","even if","Ακόμη κι αν βρέξει, θα πάμε."),
 ("είτε… είτε…","whether… or…","Είτε σου αρέσει είτε όχι, έτσι είναι."),
]
L = {
 "el": "Έμφαση και ελεύθερες αναφορικές",
 "title": "Emphasis: όποιος κι αν, όσο κι αν, αυτό που, ούτε καν, ίσα ίσα",
 "section": "C1 · argument and register",
 "goal": "Put weight where you want it in a sentence: generalising relatives, concessive 'however much', clefts and emphatic particles.",
 "blocks": [
  {"type":"text","text":"B2 gave you word order and clitic doubling for topic and focus. C1 adds the tools speakers use to **generalise** (*όποιος*, *όσοι*), to **concede everything and still insist** (*όσο κι αν*, *ό,τι κι αν*), to **frame** a claim (*αυτό που με ενοχλεί είναι…*), and to **intensify** (*ούτε καν*, *ίσα ίσα*, *και βέβαια*)."},
  {"type":"table","title":"Free relatives (no antecedent)","head":["Word","Meaning","Example"],"rows":[[f"**{a}**",b,f"*{c}*"] for a,b,c in FREE]},
  {"type":"callout","text":"**ό,τι vs ότι:** the comma is the whole difference. **ό,τι** 'whatever' (relative), **ότι** 'that' (conjunction): *Ό,τι είπε ήταν ψέμα* 'Whatever he said was a lie' vs *Είπε ότι ήταν ψέμα* 'He said that it was a lie'.\n\n**Case of όποιος** follows its own clause, while the main clause may need doubling: *Όποιον δεις, πες του να με πάρει* 'Whoever you see, tell him to call me' (όποιον: object of δεις; *του*: resumes it in the main clause)."},
  {"type":"table","title":"Concessive generalisers","head":["Pattern","Meaning","Example"],"rows":[[f"**{a}**",b,f"*{c}*"] for a,b,c in CONC]},
  {"type":"table","title":"Framing and intensifying","head":["Device","Example","Effect"],"rows":[
    ["**Αυτό που… είναι…** (cleft)","*Αυτό που με ανησυχεί είναι η σιωπή της κυβέρνησης.*","frames the key point"],
    ["**Εκείνο που…**","*Εκείνο που μετράει είναι το αποτέλεσμα.*","same, slightly more formal"],
    ["**Το θέμα είναι ότι / Το ζήτημα είναι…**","*Το θέμα είναι ότι κανείς δεν ρώτησε.*","introduces the real issue"],
    ["**ούτε καν**","*Δεν μου είπε ούτε καν καλημέρα.*","not even"],
    ["**ίσα ίσα / απεναντίας**","*Δεν με πείραξε· ίσα ίσα, χάρηκα.*","on the contrary"],
    ["**και βέβαια / και πολύ μάλιστα**","*Θα έρθεις; — Και βέβαια!*","of course; very much so"],
    ["**ακριβώς επειδή**","*Ακριβώς επειδή τον εκτιμώ, του μίλησα ειλικρινά.*","precisely because"],
    ["**τόσο… ώστε / που**","*Ήταν τόσο κουρασμένος που αποκοιμήθηκε στο τραπέζι.*","so … that"],
    ["**μόνο που**","*Ωραίο σπίτι, μόνο που είναι μακριά.*","the only thing is"],
    ["**καθόλου / διόλου**","*Δεν είναι καθόλου αυτονόητο.*","not at all"]]},
  {"type":"culture","title":"Όποιος έχει τα γένια, έχει και τα χτένια","text":"Free relatives power half of Greek proverbs: **Όποιος βιάζεται, σκοντάφτει** 'Whoever hurries, stumbles'; **Όποιος ανακατεύεται με τα πίτουρα, τον τρώνε οι κότες** 'Whoever mixes with the bran gets eaten by the hens' (bad company); **Όποιος έχει τα γένια, έχει και τα χτένια** 'Whoever has the beard has the combs' (you're responsible for what's yours); **Ό,τι λάμπει δεν είναι χρυσός**. Dropping one into a discussion is perfectly natural at C1."},
  {"type":"reading","title":"Γράμμα σε έναν νέο","text":"Αγαπητέ μου Στέφανε,\n\n**Αυτό που** θέλω να σου πω δεν είναι συμβουλή· είναι μια παρατήρηση. **Όσο κι αν** σε πιέζουν οι γονείς σου να σπουδάσεις κάτι «σίγουρο», **ό,τι κι αν** επιλέξεις θα το κάνεις καλά μόνο αν σε ενδιαφέρει. **Όσοι** έχω γνωρίσει να δουλεύουν χωρίς όρεξη, **ούτε καν** θυμούνται γιατί διάλεξαν τον δρόμο τους.\n\nΔεν σου λέω να αγνοήσεις την πραγματικότητα· **ίσα ίσα**. **Ακριβώς επειδή** η αγορά εργασίας αλλάζει τόσο γρήγορα, δεν υπάρχει πια κανένα «σίγουρο» επάγγελμα. **Όπου κι αν** βρεθείς, θα χρειαστεί να μαθαίνεις ξανά και ξανά. **Είτε** γίνεις μηχανικός **είτε** μουσικός, **εκείνο που** θα μετρήσει είναι η επιμονή σου.\n\n**Όπως και να 'χει**, **όποτε** θέλεις να το συζητήσουμε, ξέρεις πού θα με βρεις.\n\nΜε αγάπη,\nο θείος σου Μανόλης","en":"My dear Stefanos,\n\nWhat I want to tell you isn't advice; it's an observation. However much your parents push you to study something 'safe', whatever you choose you'll only do well if it interests you. All the people I've known who work without any appetite for it don't even remember why they chose their path.\n\nI'm not telling you to ignore reality; quite the opposite. Precisely because the job market changes so fast, there is no longer any 'safe' profession. Wherever you end up, you'll need to learn again and again. Whether you become an engineer or a musician, what will count is your persistence.\n\nBe that as it may, whenever you want to talk it over, you know where to find me.\n\nWith love,\nyour uncle Manolis",
   "gloss":{"όρεξη":"appetite, keenness","επιμονή":"persistence","επάγγελμα":"profession"},
   "questions":[
    {"prompt":"Τι πιστεύει ο θείος για τα «σίγουρα» επαγγέλματα;","answer":"Ότι δεν υπάρχουν πια.","options":["Ότι δεν υπάρχουν πια.","Ότι είναι η καλύτερη επιλογή.","Ότι είναι μόνο για μηχανικούς.","Ότι οι γονείς έχουν δίκιο."],"why":"δεν υπάρχει πια κανένα «σίγουρο» επάγγελμα."},
    {"prompt":"Τι σημαίνει εδώ το «ίσα ίσα»;","answer":"Το αντίθετο: πρέπει να λάβεις υπόψη την πραγματικότητα.","options":["Το αντίθετο: πρέπει να λάβεις υπόψη την πραγματικότητα.","Ακριβώς: αγνόησε την πραγματικότητα.","Περίπου.","Μόλις που."],"why":"ίσα ίσα = on the contrary."}]}
 ],
 "practice": [
  {"gen":"mc","items":[
    {"prompt":"___ θέλει να βοηθήσει, είναι ευπρόσδεκτος.","answer":"Όποιος","options":["Όποιος","Ο οποίος","Ποιος","Που"],"why":"Free relative 'whoever': όποιος."},
    {"prompt":"___ κι αν προσπαθήσεις, δεν θα τον πείσεις.","answer":"Όσο","options":["Όσο","Όπως","Όπου","Ό,τι"],"why":"όσο κι αν 'however much'."},
    {"prompt":"Δεν άκουσε ___ τι του είπα. (not even)","answer":"ούτε καν","options":["ούτε καν","ούτε","καθόλου","ίσα ίσα"],"why":"ούτε καν 'not even'."},
    {"prompt":"___ μου είπες θα μείνει μεταξύ μας. (whatever)","answer":"Ό,τι","options":["Ό,τι","Ότι","Όποιο","Τι"],"why":"ό,τι with the comma = 'whatever'."},
    {"prompt":"___ με ενοχλεί είναι η αδιαφορία. (What)","answer":"Αυτό που","options":["Αυτό που","Ό,τι που","Αυτό το οποίο ότι","Τι"],"why":"Cleft: αυτό που… είναι…"},
    {"prompt":"Δεν θύμωσα· ___, χάρηκα που μου το είπες. (on the contrary)","answer":"ίσα ίσα","options":["ίσα ίσα","ούτε καν","μόνο που","όπως και να 'χει"],"why":"ίσα ίσα 'on the contrary'."},
    {"prompt":"___ του τηλεφωνήσω, δεν απαντάει. (whenever)","answer":"Όποτε","options":["Όποτε","Όταν που","Οπότε","Όπου"],"why":"όποτε 'whenever'; οπότε means 'so, therefore'."},
    {"prompt":"___ σου αρέσει ___ όχι, θα το κάνουμε.","answer":"Είτε … είτε","options":["Είτε … είτε","Ούτε … ούτε","Ή … ή","Όσο … τόσο"],"why":"είτε… είτε 'whether… or'."},
    {"prompt":"___ ήρθαν, έφυγαν ικανοποιημένοι. (All who)","answer":"Όσοι","options":["Όσοι","Όποιοι","Οι οποίοι","Όλοι που"],"why":"όσοι 'all those who'."},
    {"prompt":"Ωραία ταινία, ___ κράτησε τρεις ώρες. (the only thing is)","answer":"μόνο που","options":["μόνο που","ίσα ίσα","ούτε καν","ακριβώς επειδή"],"why":"μόνο που 'except that'."}]},
  {"gen":"type","n":5,"items":[
    {"prompt":"Say in Greek: **Be that as it may** (όπως…)","answer":"όπως και να 'χει","accept":["όπως και να 'χει","όπως και να έχει","όπως κι αν έχει"]},
    {"prompt":"Say in Greek: **precisely because**","answer":"ακριβώς επειδή"},
    {"prompt":"Say in Greek: **Whatever happens, …** (ό,τι…)","answer":"Ό,τι και να γίνει","accept":["ό,τι και να γίνει","ό,τι κι αν γίνει","ό,τι και αν γίνει"]},
    {"prompt":"Say in Greek: **wherever you go** (όπου… εσύ)","answer":"όπου κι αν πας","accept":["όπου κι αν πας","όπου και να πας","όπου και αν πας"]},
    {"prompt":"Say in Greek: **even if it rains** (ακόμη…)","answer":"ακόμη κι αν βρέξει","accept":["ακόμη κι αν βρέξει","ακόμα κι αν βρέξει","ακόμη και αν βρέξει","ακόμα και να βρέξει","ακόμη και να βρέξει"]},
    {"prompt":"Say in Greek: **Of course!** (emphatic, και…)","answer":"Και βέβαια","accept":["και βέβαια","και βέβαια!","Και βέβαια!"]}]}
 ]
}
json.dump(L, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
