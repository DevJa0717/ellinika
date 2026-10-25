import json, sys, random
random.seed(7)
I1 = [ # idiom, literal, meaning, example
 ("κάνω τα στραβά μάτια","make the crooked eyes","turn a blind eye","Η αστυνομία έκανε τα στραβά μάτια για χρόνια."),
 ("έχω τον νου μου","have my mind (on it)","keep an eye on, be careful","Έχε τον νου σου στο παιδί."),
 ("βάζω το χέρι μου στη φωτιά","put my hand in the fire","vouch absolutely for","Για τον Νίκο βάζω το χέρι μου στη φωτιά."),
 ("μου σηκώθηκε η τρίχα","my hair stood up","it gave me goosebumps","Όταν άκουσα την ιστορία, μου σηκώθηκε η τρίχα."),
 ("δεν μου γεμίζει το μάτι","it doesn't fill my eye","I'm not convinced by it/him","Ο νέος προπονητής δεν μου γεμίζει το μάτι."),
 ("έχει γερό στομάχι","has a strong stomach","can take a lot","Για να δουλεύεις στα επείγοντα, θέλει γερό στομάχι."),
 ("μου βγήκε η ψυχή","my soul came out","I was exhausted, it was a struggle","Μου βγήκε η ψυχή να βρω πάρκινγκ."),
 ("τρώω τη χυλόπιτα","eat the noodle","get turned down (romantically)","Της ζήτησε να βγουν κι έφαγε χυλόπιτα."),
 ("έχω πολλά στο κεφάλι μου","have a lot on my head","have a lot on my mind","Συγγνώμη, έχω πολλά στο κεφάλι μου αυτές τις μέρες."),
 ("μου την έδωσε","it gave it to me","it got on my nerves","Μου την έδωσε που άργησε πάλι."),
 ("τα έκανε θάλασσα","made it all sea","made a mess of it","Προσπάθησε να βοηθήσει, αλλά τα έκανε θάλασσα."),
 ("τα βρήκαμε","we found them","we came to an agreement / made up","Μαλώσαμε, αλλά στο τέλος τα βρήκαμε."),
 ("τα παράτησα","I dropped them","I gave up","Τα παράτησα τα πιάνο μετά από δύο χρόνια."),
 ("τα 'χω χαμένα","I have them lost","I'm confused, at a loss","Με τόσες αλλαγές, τα 'χω χαμένα."),
 ("τα 'βαλε μαζί μου","he put them with me","he picked on me, blamed me","Γιατί τα βάζεις μαζί μου; Δεν φταίω εγώ!"),
 ("την πάτησα","I stepped on it","I got caught out, I fell for it","Την πάτησα με τη φθηνή πτήση: τελικά πλήρωσα διπλά."),
 ("την κοπανάω","I hammer it","I slip away, sneak off","Η συνάντηση ήταν βαρετή, οπότε την κοπάνησα."),
 ("κόβω κίνηση","cut movement","check things out, observe","Πήγα πρώτα να κόψω κίνηση."),
 ("ψάχνω ψύλλους στ' άχυρα","look for fleas in the straw","nitpick, look for trouble","Μην ψάχνεις ψύλλους στ' άχυρα, το κείμενο είναι καλό."),
 ("δεν μασάω","I don't chew","I'm not fooled, I'm not scared","Μη μου λες ιστορίες, δεν μασάω."),
 ("έφαγε τα λυσσακά του","ate his rabid fits","tried everything, nagged endlessly","Έφαγα τα λυσσακά μου να του εξηγήσω."),
 ("κάνω την πάπια","play the duck","play dumb, keep quiet","Όταν ρωτήσαμε ποιος το έσπασε, έκανε την πάπια."),
 ("πουλάω τρέλα","sell madness","act crazy (to get away with something)","Πούλησε τρέλα στον έλεγχο και τη γλίτωσε."),
 ("ρίχνω άδεια να πιάσω γεμάτα","throw empty to catch full","fish for information","Δεν ξέρει τίποτα, απλώς ρίχνει άδεια να πιάσει γεμάτα."),
 ("άλλα λόγια ν' αγαπιόμαστε","other words so we love each other","changing the subject (avoiding the point)","Τον ρώτησα για τα χρήματα κι εκείνος άλλα λόγια ν' αγαπιόμαστε."),
 ("φτάνει ο κόμπος στο χτένι","the knot reaches the comb","things come to a head","Κάποια στιγμή θα φτάσει ο κόμπος στο χτένι."),
 ("τα κάνει πλακάκια","makes them tiles","colludes, cosies up","Η διοίκηση τα έκανε πλακάκια με τον εργολάβο."),
 ("κάνω τον κινέζο","play the Chinese man","pretend not to understand","Του ζήτησα τα λεφτά και έκανε τον κινέζο."),
]
I2 = [
 ("όπου φτωχός κι η μοίρα του","wherever a poor man, his fate too","misfortune follows the unlucky","Χάλασε και το αυτοκίνητο: όπου φτωχός κι η μοίρα του."),
 ("κάθε εμπόδιο για καλό","every obstacle for good","every cloud has a silver lining","Έχασα την πτήση, αλλά γνώρισα τη γυναίκα μου. Κάθε εμπόδιο για καλό!"),
 ("τον έπιασε το παράπονο","the grievance took him","he felt sorry for himself, got upset","Την έπιασε το παράπονο που δεν την κάλεσαν."),
 ("μου έφυγε ένα βάρος","a weight left me","a weight off my mind","Πήρα τα αποτελέσματα κι έφυγε ένα βάρος."),
 ("άνθρωπος με τα όλα του","a person with all of his","a decent, proper person","Ο θείος σου είναι άνθρωπος με τα όλα του."),
 ("έχει μαύρα μεσάνυχτα","has black midnight","hasn't a clue","Για την οικονομία έχει μαύρα μεσάνυχτα."),
 ("του έψησε το ψάρι στα χείλη","grilled the fish on his lips","made his life hell","Ο προϊστάμενος του έψησε το ψάρι στα χείλη."),
 ("μου έπεσαν τα μούτρα","my face fell","I was embarrassed","Μου έπεσαν τα μούτρα όταν το ανακάλυψα."),
 ("κατά φωνή κι ο γάιδαρος","at the voice, the donkey too","speak of the devil","Μιλούσαμε για σένα, κατά φωνή κι ο γάιδαρος!"),
 ("το 'χει ο χαρακτήρας του","his character has it","it's in his nature","Δεν το κάνει επίτηδες, το 'χει ο χαρακτήρας του."),
 ("δεν χαρίζει κάστανα","doesn't give away chestnuts","is tough, gives no quarter","Ο καθηγητής δεν χαρίζει κάστανα στις εξετάσεις."),
 ("έχει γάτα","has a cat","is shrewd, sharp","Μικρή, αλλά έχει γάτα."),
 ("βάζω τα δυνατά μου","put on my strengths","do my best","Θα βάλω τα δυνατά μου να τελειώσω έγκαιρα."),
 ("παίρνω τους δρόμους","take the roads","wander aimlessly, go out of one's mind","Όταν το έμαθε, πήρε τους δρόμους."),
 ("κόβει και ράβει","cuts and sews","talks non-stop / runs the show","Η κυρία Ρούλα κόβει και ράβει στη γειτονιά."),
 ("είναι στα κάγκελα","is on the railings","is furious, up in arms","Οι κάτοικοι είναι στα κάγκελα με τη χωματερή."),
 ("μας έπρηξε","he swelled us","he bored/annoyed us to death","Μας έπρηξε με τις διακοπές του."),
 ("μου ήρθε κεραμίδα","a roof tile came to me","it hit me like a bolt from the blue","Μου ήρθε κεραμίδα ο λογαριασμός του ρεύματος."),
 ("ψήνομαι","I'm being grilled","I'm up for it, I'm tempted","Ψήνεσαι για ένα ταξίδι στη Νάξο;"),
 ("τζάμπα κόπος","free effort","wasted effort","Όλη η δουλειά ήταν τζάμπα κόπος."),
 ("στο άψε σβήσε","in light-put out","in a flash","Τα έφτιαξε στο άψε σβήσε."),
 ("τα ψιλά γράμματα","the small letters","the fine print","Διάβασε προσεκτικά τα ψιλά γράμματα πριν υπογράψεις."),
 ("χαμένος από χέρι","lost from the hand","a lost cause from the start","Ο αγώνας ήταν χαμένος από χέρι."),
 ("δεν μου καίγεται καρφί","not a nail of mine burns","I couldn't care less","Τι θα πει ο κόσμος; Δεν μου καίγεται καρφί."),
 ("έγινε της κακομοίρας","the wretched woman's [thing] happened","all hell broke loose","Όταν ανακοινώθηκε η απόφαση, έγινε της κακομοίρας."),
 ("φέρνω τα πάνω κάτω","bring the up down","turn everything upside down","Ο νέος διευθυντής έφερε τα πάνω κάτω."),
 ("τα φέρνω βόλτα","bring them round","make ends meet, cope","Με αυτόν τον μισθό δύσκολα τα φέρνω βόλτα."),
 ("από το στόμα σου και στου Θεού τ' αυτί","from your mouth to God's ear","let's hope so","Θα πάρεις τη θέση! — Από το στόμα σου και στου Θεού τ' αυτί!"),
]
def lesson(code, el, title, items, intro, culture, reading, n):
    meanings=[m for _,_,m,_ in items]
    mc=[{"prompt":f"**{a}** means…","answer":m,"options":[m]+random.sample([x for x in meanings if x!=m],3),"why":f"*{e}*"} for a,l,m,e in items]
    ty=[{"prompt":f"Idiom for **{m}** (lit. *{l}*)","answer":a,"accept":[a,a.replace("'","’")],"why":f"*{e}*"} for a,l,m,e in items]
    return {"el":el,"title":title,"section":"C1 · idiom","goal":"Understand and use the idioms educated Greeks drop into everyday conversation.",
      "blocks":[{"type":"text","text":intro},
        {"type":"table","title":"The idioms","head":["Idiom","Literally","Meaning","Example"],"rows":[[f"**{a}**",f"*{l}*",m,f"*{e}*"] for a,l,m,e in items]},
        {"type":"culture","title":culture[0],"text":culture[1]},
        reading],
      "practice":[{"gen":"mc","n":12,"items":mc},{"gen":"type","n":n,"items":ty}]}
R1={"type":"reading","title":"Στο γραφείο, Δευτέρα πρωί","text":"— Τι έγινε, ρε Μαρία; Φαίνεσαι κουρασμένη.\n\n— Άσ' τα. **Μου βγήκε η ψυχή** με την παρουσίαση. Ο Κώστας **τα έκανε θάλασσα** με τα στοιχεία και τελευταία στιγμή έπρεπε να τα ξαναφτιάξω όλα.\n\n— Πάλι; Κι ο διευθυντής δεν λέει τίποτα;\n\n— Ο διευθυντής **κάνει τα στραβά μάτια**. Ξέρεις, **τα έχουν κάνει πλακάκια** από τότε που παίζουν τένις μαζί.\n\n— Κι εσύ γιατί δεν μιλάς;\n\n— Μίλησα! Αλλά όταν τον ρώτησα ευθέως, **έκανε την πάπια**. Και μετά **άλλα λόγια ν' αγαπιόμαστε**: «Πώς πήγε το Σαββατοκύριακο;» και τέτοια.\n\n— Κάποια στιγμή **θα φτάσει ο κόμπος στο χτένι**, θα δεις.\n\n— Μακάρι. Εγώ πάντως **δεν μασάω** άλλο. Αν ξαναγίνει, πάω στη γενική διεύθυνση.\n\n— Μπράβο. Κι αν χρειαστείς μάρτυρα, εγώ **βάζω το χέρι μου στη φωτιά** για σένα.","en":"— What's up, Maria? You look tired.\n\n— Don't ask. The presentation nearly killed me. Kostas made a mess of the figures and at the last minute I had to redo everything.\n\n— Again? And the director says nothing?\n\n— The director turns a blind eye. You know, they've been thick as thieves since they started playing tennis together.\n\n— And why don't you speak up?\n\n— I did! But when I asked him directly, he played dumb. And then he changed the subject: 'How was the weekend?' and so on.\n\n— At some point things will come to a head, you'll see.\n\n— I hope so. Anyway, I'm not putting up with it any more. If it happens again, I'm going to head office.\n\n— Good for you. And if you need a witness, I'll vouch for you all the way.",
 "gloss":{"άσ' τα":"don't ask (lit. leave them)","ευθέως":"directly","μάρτυρα":"witness (acc.)","γενική διεύθυνση":"head office"},
 "questions":[{"prompt":"Γιατί ο διευθυντής δεν λέει τίποτα στον Κώστα;","answer":"Επειδή είναι φίλοι και τον καλύπτει.","options":["Επειδή είναι φίλοι και τον καλύπτει.","Επειδή δεν ξέρει τι έγινε.","Επειδή η Μαρία δεν του μίλησε.","Επειδή η παρουσίαση πήγε καλά."],"why":"κάνει τα στραβά μάτια … τα έχουν κάνει πλακάκια."},
  {"prompt":"Τι έκανε ο διευθυντής όταν τον ρώτησε η Μαρία;","answer":"Έκανε πως δεν καταλαβαίνει και άλλαξε θέμα.","options":["Έκανε πως δεν καταλαβαίνει και άλλαξε θέμα.","Της ζήτησε συγγνώμη.","Απέλυσε τον Κώστα.","Της είπε να πάει στη γενική διεύθυνση."],"why":"έκανε την πάπια … άλλα λόγια ν' αγαπιόμαστε."}]}
R2={"type":"reading","title":"Ένα τηλεφώνημα από τη Θεσσαλονίκη","text":"— Έλα, Γιώργο! **Κατά φωνή κι ο γάιδαρος**, μόλις μιλούσαμε για σένα με τη Ρένα.\n\n— Καλά λόγια ελπίζω! Λοιπόν, έχω νέα: πήρα τη θέση στο πανεπιστήμιο.\n\n— Σοβαρά; Συγχαρητήρια! Και πέρσι που σε απέρριψαν… **κάθε εμπόδιο για καλό**, τελικά.\n\n— Ναι, αλλά **μου ήρθε κεραμίδα** το ενοίκιο εδώ. Με τον μισθό του λέκτορα δύσκολα **θα τα φέρω βόλτα**.\n\n— Διάβασες τα **ψιλά γράμματα** του συμβολαίου;\n\n— Όλα. Ο πρόεδρος του τμήματος **δεν χαρίζει κάστανα**, αλλά είναι **άνθρωπος με τα όλα του**. Θα **βάλω τα δυνατά μου**.\n\n— Θα τα πας περίφημα. Κι αν **ψήνεσαι**, ερχόμαστε με τη Ρένα τον Νοέμβριο να γιορτάσουμε.\n\n— **Από το στόμα σου και στου Θεού τ' αυτί**! Σας περιμένω.","en":"— Hi, George! Speak of the devil, we were just talking about you with Rena.\n\n— Good things, I hope! So, I have news: I got the job at the university.\n\n— Really? Congratulations! And last year when they turned you down… every cloud has a silver lining, after all.\n\n— Yes, but the rent here hit me like a ton of bricks. On a lecturer's salary I'll struggle to make ends meet.\n\n— Did you read the fine print of the contract?\n\n— All of it. The head of department is tough, but he's a decent man. I'll do my best.\n\n— You'll do brilliantly. And if you're up for it, Rena and I will come in November to celebrate.\n\n— From your lips to God's ears! I'll be expecting you.",
 "gloss":{"λέκτορα":"lecturer (gen.)","τμήματος":"department (gen.)","περίφημα":"splendidly"},
 "questions":[{"prompt":"Ποιο είναι το πρόβλημα του Γιώργου;","answer":"Το ενοίκιο είναι πολύ ακριβό για τον μισθό του.","options":["Το ενοίκιο είναι πολύ ακριβό για τον μισθό του.","Δεν πήρε τη θέση.","Ο πρόεδρος του τμήματος είναι κακός άνθρωπος.","Δεν διάβασε το συμβόλαιο."],"why":"μου ήρθε κεραμίδα το ενοίκιο … δύσκολα θα τα φέρω βόλτα."},
  {"prompt":"Πώς περιγράφει τον πρόεδρο του τμήματος;","answer":"Αυστηρό αλλά έντιμο.","options":["Αυστηρό αλλά έντιμο.","Αδιάφορο.","Γενναιόδωρο με τους νέους.","Άσχετο με τα οικονομικά."],"why":"δεν χαρίζει κάστανα, αλλά είναι άνθρωπος με τα όλα του."}]}
L1=lesson("c1-idioms-1","Ιδιωματισμοί (1)","Idioms 1: κάνω τα στραβά μάτια, τα έκανε θάλασσα, την πάτησα",I1,
 "Greek conversation runs on idioms, and many are built on a vague feminine or neuter plural object: **τα** βρήκαμε, **τα** παράτησα, **την** πάτησα, **την** κοπάνησα. The *τα/την* refers to nothing in particular (a vague 'things', 'it'), so don't look for an antecedent. Learn these as whole verbs; they conjugate normally: *τα βρήκαμε, θα τα βρούμε, να τα βρείτε*.",
 ("Τα και την: τα αόριστα αντικείμενα","The empty object is so productive that Greeks invent new idioms with it all the time: *την έκανα* 'I left' (lit. 'I did it'), *την έβγαλα* 'I got by', *τα πήρα* 'I got angry' (also: 'I took a bribe'!), *τα 'παιξα* 'I lost it, I cracked'. Context and tone decide. When a Greek says *Τα 'πιαν'*, ask: did they get together romantically, or take bribes? Both readings exist."),R1,10)
L2=lesson("c1-idioms-2","Ιδιωματισμοί (2)","Idioms 2: δεν μου καίγεται καρφί, τα φέρνω βόλτα, κάθε εμπόδιο για καλό",I2,
 "A second set: reactions and set responses (*κάθε εμπόδιο για καλό, από το στόμα σου και στου Θεού τ' αυτί*), judgements of people (*έχει γάτα, άνθρωπος με τα όλα του, δεν χαρίζει κάστανα*) and everyday struggles (*τα φέρνω βόλτα, μου ήρθε κεραμίδα*). Set responses are the fastest way to sound fluent: they come at predictable moments, and Greeks expect them.",
 ("Παροιμίες στην καθημερινή κουβέντα","Proverbs are not old-fashioned in Greek: people under thirty use *κάθε εμπόδιο για καλό*, *κατά φωνή κι ο γάιδαρος* and *όπου φτωχός κι η μοίρα του* without irony. Many come in half: Greeks say just *Όπου φτωχός…* and let the listener complete it. Social media coined new ones too, such as *τα 'χουμε πει* 'we've been over this'."),R2,10)
for L,f in ((L1,"c1-idioms-1"),(L2,"c1-idioms-2")):
    json.dump(L, open(f"/mnt/project-files/app/lessons/{f}.json","w"), ensure_ascii=False, indent=1)
print("ok")
