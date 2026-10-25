import json, sys
DAT = [("εν τω μεταξύ","meanwhile"),("εν πάση περιπτώσει","in any case"),("εν ολίγοις","in short"),("εν μέρει","partly"),
 ("εν λόγω","in question, aforementioned (ο εν λόγω νόμος)"),("εν τάξει / εντάξει","in order; OK"),("εν γνώσει","knowingly, aware of"),
 ("εν καιρώ","in due course"),("εν ενεργεία","in office, serving"),("εν αγνοία","unaware (+ gen.)"),("εν ονόματι","in the name of"),
 ("εν κατακλείδι","in conclusion"),("εν ψυχρώ","in cold blood"),("εν συντομία","briefly"),("εν πολλοίς","to a large extent"),
 ("εν τέλει","in the end"),("εν αναμονή","pending, awaiting"),("τοις μετρητοίς","in cash"),("τω όντι","indeed, in fact"),
 ("επί τω έργω","in the act, at work"),("σὺν Θεῷ / συν Θεώ","God willing")]
PREP = [
 ("εκ / εξ + gen.","from, out of","εκ των υστέρων 'in hindsight', εξ αρχής 'from scratch', εκ μέρους 'on behalf of', εξ ορισμού 'by definition', εξ αποστάσεως 'remote(ly)', εκ πρώτης όψεως"),
 ("προ + gen.","before","προ ημερών 'a few days ago', προ πολλού 'long ago', προ των πυλών 'at the gates, imminent', π.Χ. (προ Χριστού)"),
 ("υπέρ + gen.","for, in favour of","υπέρ της πρότασης; τα υπέρ και τα κατά 'pros and cons'; υπέρ το δέον 'excessively'"),
 ("κατά + gen.","against","κατά της βίας; ψήφισε κατά"),
 ("ανά + acc.","per, throughout","ανά άτομο 'per person', ανά πάσα στιγμή 'at any moment', ανά τον κόσμο 'around the world'"),
 ("άνευ + gen.","without","άνευ όρων 'unconditionally', άνευ προηγουμένου 'unprecedented', άνευ σημασίας"),
 ("περί + gen. / acc.","about / around","περί τίνος πρόκειται; 'what is it about?'; περί τις 100 'about 100'"),
 ("επί + gen. / acc.","on, during / for, times","επί Καραμανλή 'under Karamanlis', επί τόπου 'on the spot', επί δέκα χρόνια 'for ten years', δύο επί τρία '2×3', επί του παρόντος 'for the time being'"),
 ("διά / δια + gen.","by means of, through","διά ζώσης 'in person', δια βίου μάθηση 'lifelong learning', διά νόμου, δια της βίας 'by force'"),
 ("μετά + gen.","with","μετά χαράς 'gladly', μετά βίας 'barely', μετά τιμής 'respectfully'"),
 ("παρά + gen.","by, from (a person)","παρά τω Αρείω Πάγω 'at the Supreme Court', προϋποθέσεις που τίθενται παρά του νόμου (very formal)"),
 ("υπό + acc. / gen.","under / by","υπό την προϋπόθεση ότι 'on condition that', υπό κατασκευή 'under construction', υπό συζήτηση, υπό την αιγίδα 'under the auspices'"),
 ("εις + acc.","into, in","εις βάρος 'at the expense of', εις βάθος 'in depth', εις διπλούν 'in duplicate', εις μάτην 'in vain'"),
 ("εντός / εκτός + gen.","within / outside","εντός της προθεσμίας 'within the deadline', εκτός έδρας 'away (match)', εκτός των άλλων 'among other things'"),
 ("ενώπιον + gen.","before, in front of","ενώπιον του δικαστηρίου, ενώπιον της Βουλής"),
 ("δυνάμει / βάσει + gen.","by virtue of / on the basis of","δυνάμει του νόμου, βάσει της συμφωνίας"),
 ("ένεκα / χάριν + gen.","for the sake of","χάριν συντομίας 'for brevity', χάριν παραδείγματος 'for example', τιμής ένεκεν 'as an honour'"),
 ("πλην / συν / μείον","except; minus / plus / minus","πλην ελαχίστων εξαιρέσεων; πέντε συν δύο"),
]
L = {
 "el": "Λόγιες προθέσεις και δοτική",
 "title": "Learned prepositions and frozen datives: εν τω μεταξύ, εκ των υστέρων, άνευ όρων",
 "section": "C1 · learned morphology",
 "goal": "Own the hundred or so fixed learned phrases that every educated Greek uses, and the prepositions behind them.",
 "blocks": [
  {"type":"text","text":"The dative case died in spoken Greek a thousand years ago, and so did prepositions like εν, εκ, προ, υπέρ, άνευ. But they survive in **fixed phrases** that are not learned or bookish at all: *εν τω μεταξύ* is as normal as 'meanwhile', *τοις μετρητοίς* is what the shopkeeper asks. Treat each phrase as a single word; don't try to build new ones. The case after the old preposition is usually the genitive (where the ancient language had the genitive) and the frozen datives keep their **-ω, -η, -οις, -αις** endings."},
  {"type":"table","title":"Frozen datives","head":["Phrase","Meaning"],"rows":[[f"**{a}**",b] for a,b in DAT]},
  {"type":"table","title":"Learned prepositions in living phrases","head":["Preposition","Basic meaning","Phrases you need"],"rows":[[f"**{a}**",b,c] for a,b,c in PREP]},
  {"type":"callout","text":"**Two traps.** *Εν τάξει* vs *εντάξει*: the first means 'in order' (*Όλα εν τάξει με τα χαρτιά σας*), the second is the everyday 'OK'; both spellings are correct for 'OK'. *Κατά* + genitive means 'against' (*κατά της απόφασης*), + accusative 'during, according to, about' (*κατά τη γνώμη μου, κατά τις δέκα*).\n\n**υπό την προϋπόθεση ότι/να** 'provided that' and **εκ των υστέρων** 'in hindsight' are the two phrases from this list that will most quickly raise your spoken register."},
  {"type":"culture","title":"Ο εν λόγω κύριος","text":"Greeks use learned phrases with a wink as often as seriously. *Ο εν λόγω κύριος* 'the gentleman in question' is how you refer, slightly ironically, to someone everyone is gossiping about. *Εν ψυχρώ* 'in cold blood' is a newspaper staple for crimes. And when a waiter in a village says *Τοις μετρητοίς, παρακαλώ*, he isn't being formal; card machines just aren't working."},
  {"type":"reading","title":"Μια συνέντευξη εξ αποστάσεως","text":"— Κύριε καθηγητά, **εν ολίγοις**, ποιο είναι το συμπέρασμα της έρευνάς σας;\n\n— **Εκ πρώτης όψεως** τα αποτελέσματα είναι ενθαρρυντικά. Τα παιδιά που παρακολούθησαν μαθήματα **εξ αποστάσεως** κατά την πανδημία δεν έμειναν, **κατά μέσο όρο**, πολύ πίσω. **Εν τούτοις**, η εικόνα αλλάζει όταν εξετάσουμε τα στοιχεία **εις βάθος**: η διαφορά **εις βάρος** των φτωχότερων οικογενειών ήταν **άνευ προηγουμένου**.\n\n— Δηλαδή, **εκ των υστέρων**, το κλείσιμο των σχολείων ήταν λάθος;\n\n— Δεν το λέω αυτό. **Εν πάση περιπτώσει**, η απόφαση πάρθηκε **εν αγνοία** πολλών δεδομένων. Αυτό που προτείνω είναι να επιστρέψουμε στη διδασκαλία **διά ζώσης**, **υπό την προϋπόθεση ότι** θα διατηρηθούν τα ψηφιακά εργαλεία, και να επενδύσουμε στη **δια βίου** μάθηση των εκπαιδευτικών.\n\n— Και **επί του παρόντος**;\n\n— **Επί του παρόντος** χρειαζόμαστε χρόνο. Τα συμπεράσματα θα τα δούμε **εν καιρώ**.","en":"— Professor, in short, what is the conclusion of your research?\n\n— At first sight the results are encouraging. Children who attended lessons remotely during the pandemic did not, on average, fall far behind. However, the picture changes when we examine the data in depth: the gap to the detriment of poorer families was unprecedented.\n\n— So, in hindsight, closing the schools was a mistake?\n\n— I'm not saying that. In any case, the decision was taken without knowledge of much of the data. What I propose is that we return to in-person teaching, provided that the digital tools are kept, and invest in lifelong learning for teachers.\n\n— And for the time being?\n\n— For the time being we need time. We'll see the conclusions in due course.",
   "gloss":{"ενθαρρυντικά":"encouraging","κατά μέσο όρο":"on average","εν τούτοις":"nevertheless","δεδομένων":"data (gen. pl.)","εκπαιδευτικών":"teachers (gen. pl.)"},
   "questions":[
    {"prompt":"Ποιοι επηρεάστηκαν περισσότερο από την τηλεκπαίδευση;","answer":"Τα παιδιά φτωχότερων οικογενειών.","options":["Τα παιδιά φτωχότερων οικογενειών.","Οι εκπαιδευτικοί.","Όλα τα παιδιά εξίσου.","Κανένας, κατά μέσο όρο."],"why":"η διαφορά εις βάρος των φτωχότερων οικογενειών ήταν άνευ προηγουμένου."},
    {"prompt":"Τι προτείνει ο καθηγητής;","answer":"Μαθήματα με φυσική παρουσία, κρατώντας τα ψηφιακά εργαλεία.","options":["Μαθήματα με φυσική παρουσία, κρατώντας τα ψηφιακά εργαλεία.","Μόνιμη τηλεκπαίδευση.","Να κλείσουν ξανά τα σχολεία.","Να καταργηθούν τα ψηφιακά εργαλεία."],"why":"διά ζώσης, υπό την προϋπόθεση ότι θα διατηρηθούν τα ψηφιακά εργαλεία."}]}
 ],
 "practice": [
  {"gen":"type","n":10,"items":[{"prompt":f"Learned phrase for **{b.split(' (')[0]}**","answer":a.split(" / ")[0],"accept":a.split(" / "),"why":f"{a}: {b}"} for a,b in DAT if a not in("εν τάξει / εντάξει","σὺν Θεῷ / συν Θεώ")]},
  {"gen":"mc","items":[
    {"prompt":"Η συνάντηση θα γίνει ___, όχι διαδικτυακά. (in person)","answer":"διά ζώσης","options":["διά ζώσης","εξ αποστάσεως","εν ψυχρώ","επί τόπου"],"why":"διά ζώσης 'in person'."},
    {"prompt":"___, η απόφαση ήταν λάθος. (in hindsight)","answer":"Εκ των υστέρων","options":["Εκ των υστέρων","Εκ πρώτης όψεως","Εξ ορισμού","Προ πολλού"],"why":"εκ των υστέρων 'after the fact'."},
    {"prompt":"Θα σε βοηθήσω, ___ ότι θα με βοηθήσεις κι εσύ. (provided)","answer":"υπό την προϋπόθεση","options":["υπό την προϋπόθεση","υπέρ το δέον","επί του παρόντος","εις βάρος"],"why":"υπό την προϋπόθεση ότι/να."},
    {"prompt":"Η κρίση ήταν ___: κανείς δεν είχε ζήσει κάτι παρόμοιο. (unprecedented)","answer":"άνευ προηγουμένου","options":["άνευ προηγουμένου","άνευ όρων","εν αγνοία","προ των πυλών"],"why":"άνευ προηγουμένου 'without precedent'."},
    {"prompt":"Πληρώνουμε 20 ευρώ ___. (per person)","answer":"ανά άτομο","options":["ανά άτομο","επί άτομο","υπέρ ατόμου","διά ατόμου"],"why":"ανά + accusative 'per'."},
    {"prompt":"Ο ___ υπουργός δεν σχολίασε. (in question)","answer":"εν λόγω","options":["εν λόγω","εν ενεργεία","εν τάξει","εν μέρει"],"why":"ο εν λόγω 'the … in question'."},
    {"prompt":"Ψήφισε ___ του νομοσχεδίου. (against)","answer":"κατά","options":["κατά","υπέρ","ανά","περί"],"why":"κατά + genitive 'against'."},
    {"prompt":"Οι εκλογές είναι ___. (imminent)","answer":"προ των πυλών","options":["προ των πυλών","προ ημερών","εν καιρώ","εν τέλει"],"why":"προ των πυλών 'at the gates'."},
    {"prompt":"Το έκανε ___ των συνεπειών. (knowingly)","answer":"εν γνώσει","options":["εν γνώσει","εν αγνοία","εν ψυχρώ","εν συντομία"],"why":"εν γνώσει + gen. 'aware of'."},
    {"prompt":"___, δεν σχεδιάζουμε αλλαγές. (for the time being)","answer":"Επί του παρόντος","options":["Επί του παρόντος","Εν καιρώ","Προ πολλού","Εξ αρχής"],"why":"επί του παρόντος 'for now'."},
    {"prompt":"Ας ξεκινήσουμε ___. (from scratch)","answer":"εξ αρχής","options":["εξ αρχής","εκ μέρους","εξ ορισμού","εκ νέου"],"why":"εξ αρχής 'from the start, from scratch'. εκ νέου = again."},
    {"prompt":"Μίλησε ___ όλων των εργαζομένων. (on behalf of)","answer":"εκ μέρους","options":["εκ μέρους","εν αγνοία","υπέρ το δέον","χάριν"],"why":"εκ μέρους + gen. 'on behalf of'."}]}
 ]
}
json.dump(L, open(sys.argv[1],"w"), ensure_ascii=False, indent=1)
