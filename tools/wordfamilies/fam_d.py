from common import G

ROOTS_NOTE = {"tip": "Each family starts from a root, often in two or three shapes (the present stem, the aorist stem, the ε/ο switch). The Greek verb under the heading is the everyday word that still carries the root; where the everyday word is different (παίρνω for λαμβάνω, γυρίζω for στρέφω) both are given."}

CHAPTERS = [
dict(id="roots-motion", part="Δ", el="Ρίζες της κίνησης", title="Root families: leading, going, running, carrying, sending", level="A2–C1",
 intro=[{"p": "Six roots of movement that generate a large share of everyday and newspaper vocabulary: **άγω** *lead*, **βαίνω** *go*, **δρομ-** *run*, **πορ-** *way through*, **φέρω** *carry* and **στέλλω** *send*."}, ROOTS_NOTE],
 groups=[
  G("αγ- / αγωγ- / -ηγ-", "lead, drive", el="άγω (ancient), οδηγώ", m="""
οδηγώ|drive; lead
οδηγός|driver; guide
αγωγή|upbringing; lawsuit
αγωγός|pipeline
παράγω|produce
παραγωγή|production
εισάγω|import; introduce
εισαγωγή|import; introduction
εξαγωγή|export
αγώνας|struggle; match, race
αρχηγός|leader
στρατηγός|general
ψυχαγωγία|entertainment
""", note="**-ηγός** is *the one who leads*: οδηγός leads on the road (οδός), στρατηγός leads the army (στρατός), αρχηγός leads as the first (αρχή). **-αγωγή** is *a leading*: παραγωγή *a leading forth*, εισαγωγή *a leading in*, ψυχαγωγία *a leading of the soul*.",
    ex=[("Ποιος θα οδηγήσει απόψε;", "Who's driving tonight?"), ("Η Ελλάδα εισάγει περισσότερα απ' όσα εξάγει.", "Greece imports more than it exports.")]),
  G("βα- / βασ- / βατ- / βη-", "go, step", el="βαίνω (ancient), μπαίνω, βγαίνω", m="""
μπαίνω|go in, enter
βγαίνω|go out
ανεβαίνω|go up
κατεβαίνω|go down
βήμα|step
βάση|base, basis
διάβαση|(pedestrian) crossing
διαβατήριο|passport
επιβάτης|passenger
συμβαίνει|it happens
ακροβάτης|acrobat
αμφισβητώ|question, dispute
""", note="**μπαίνω** and **βγαίνω** are the old **εμβαίνω** *go in* and **εκβαίνω** *go out*, worn down by speech. A **διαβατήριο** lets you go across (δια-), a **επιβάτης** steps on board, and what **συμβαίνει** is what *goes together* and so comes about.",
    ex=[("Τι συμβαίνει; Γιατί δεν μπαίνεις;", "What's going on? Why aren't you coming in?")]),
  G("δρομ- / δραμ-", "run", el="τρέχω (everyday); ancient δραμεῖν", m="""
δρόμος|road, street
δρομέας|runner
δρομολόγιο|timetable; route
διαδρομή|route, journey
διάδρομος|corridor; aisle; runway
αεροδρόμιο|airport
πεζόδρομος|pedestrian street
ποδηλατόδρομος|cycle lane
συνδρομή|subscription; help
συνδρομητής|subscriber
πρόδρομος|forerunner
αναδρομικά|back pay
""", note="The everyday verb is **τρέχω**, but the nouns keep the old **δρομ-**. **αεροδρόμιο** is an *air racecourse*, a **πεζόδρομος** a street for walkers (πεζός *on foot*). **αναδρομικά** is money that *runs back*: arrears owed for past months."),
  G("πορ-", "way, passage", el="πορεύομαι (formal)", m="""
πορεία|course; march
πόρος|resource; pore
απορία|question, query
απορώ|wonder, be puzzled
άπορος|needy, poor
εύπορος|well-off
έμπορος|merchant
εμπόριο|trade
πορθμείο|ferry
πορτοφόλι|wallet
""", note="A **πόρος** is a way through; **πόροι** are *means, resources*. Without a way you are **άπορος** *poor* or you have an **απορία** *a question you cannot get past*; with a good way you are **εύπορος**. The **έμπορος** is the one *on the road*, a travelling merchant. **πορτοφόλι** is a trap: it comes from Italian *portafoglio*, not from this root.", drill=True),
  G("φερ- / φορ-", "carry, bring", el="φέρνω (φέρω)", m="""
φέρνω|bring
φορά|time (once); direction
φόρος|tax
φορτίο|load, cargo
φορτηγό|lorry, truck
φορητός|portable
διαφορά|difference
μεταφορά|transport; metaphor
αναφορά|reference; report
προσφορά|offer
συμπεριφορά|behaviour
φορέας|body, organisation
ενδιαφέρον|interest
αδιάφορος|indifferent
""", note="The ε/ο switch at work: φ**έ**ρω, φ**ο**ρά. A **φόρος** is what you bring (to the state), a **μεταφορά** carries something across (goods, or a meaning: a metaphor), **ενδιαφέρον** is what *carries you in*, and if nothing makes a difference to you, you are **αδιάφορος**. **φορά** is *a time*: μία φορά, πολλές φορές."),
  G("στελ- / στολ- / σταλ-", "send; equip", el="στέλνω (στέλλω)", m="""
στέλνω|send
αποστολή|shipment; mission
αποστολέας|sender
επιστολή|letter (formal)
απόστολος|apostle
στόλος|fleet
στολή|uniform
στολίζω|decorate
στολίδι|ornament
""", note="The root first meant *make ready, equip*: a **στόλος** is an equipped fleet, a **στολή** an outfit, **στολίζω** *dress up, decorate* (το χριστουγεννιάτικο δέντρο). With απο- it means *send away*: **αποστολή** *dispatch, mission*, **απόστολος** *one sent out*."),
 ]),

dict(id="roots-place", part="Δ", el="Ρίζες της θέσης και της κατοχής", title="Root families: putting, placing, standing, having, staying, taking, giving", level="B1–C1",
 intro=[{"p": "Seven roots for where things are and who holds them. These are the most productive in all of Greek: with the prepositional prefixes they make hundreds of abstract nouns (**υπόθεση**, **κατάσταση**, **σχέση**, **παράδοση**) that dominate formal texts."}, ROOTS_NOTE],
 groups=[
  G("βαλ- / βολ- / βλη-", "throw, put", el="βάζω (aorist έβαλα), ancient βάλλω", m="""
βάζω|put
αναβάλλω|postpone
αναβολή|postponement
επιβάλλω|impose
προβάλλω|project; screen; promote
προβολή|screening; projection
πρόβλημα|problem
σύμβολο|symbol
συμβόλαιο|contract
συμβολή|contribution
μεταβολή|change
υπερβολή|exaggeration
περιβάλλον|environment
διάβολος|devil
""", note="Three shapes: **βαλ-** (βάλλω, έβαλα), **βολ-** (the ε/ο switch's cousin: βολή *a throw*), **βλη-** (πρόβλημα *what is thrown before you*). A **σύμβολο** was a token *thrown together* with its other half; the **διάβολος** is *the one who throws (words) across*, the slanderer.",
    ex=[("Ο αγώνας αναβλήθηκε λόγω βροχής.", "The match was postponed because of rain."), ("Μην το παίρνεις τόσο βαριά, είναι υπερβολή.", "Don't take it so hard, it's an exaggeration.")]),
  G("θε- / θεσ- / θη- / θετ-", "place, put", el="θέτω, ancient τίθημι", m="""
θέση|position; seat
θέμα|subject, topic
υπόθεση|case; hypothesis; matter
σύνθεση|composition
σύνθετος|complex, compound
προσθέτω|add
επίθεση|attack
έκθεση|exhibition; essay; report
διάθεση|mood; disposal
αντίθετος|opposite
ανάθεση|assignment
παρένθεση|brackets
αποθήκη|storeroom
νομοθεσία|legislation
""", note="**θέση** *a placing* is the base. Add a prefix and you get the vocabulary of argument: **υπόθεση** *what is put under* (a hypothesis), **σύνθεση** *put together*, **αντίθεση** *put against*, **έκθεση** *put out* (an exhibition, or the essay of the writing paper). **διάθεση** is *how you are disposed*: mood. The **-θήκη** containers belong here too."),
  G("στα- / στη- / στασ-", "stand, set up", el="στέκομαι, ancient ίστημι", m="""
στέκομαι|stand
στάση|(bus) stop; stance
σταθμός|station
σταθερός|stable, steady
κατάσταση|situation, state
κατάστημα|shop
σύστημα|system
απόσταση|distance
επανάσταση|revolution
ανάσταση|resurrection
αντίσταση|resistance
ένσταση|objection
προστάτης|protector
""", note="Everything that *stands*: a **στάση** is where the bus stands, a **σταθμός** a standing place, a **κατάσταση** *how things stand*. **Ανάσταση** is *standing up again* (Easter), **επανάσταση** *standing up against (once more)*, and the 1821 Revolution is simply **η Επανάσταση**."),
  G("εχ- / οχ- / σχ-", "have, hold", el="έχω", m="""
σχέση|relationship; relation
σχήμα|shape
σχεδόν|almost
σχολή|school, faculty
συνέχεια|continuation
περιέχω|contain
περιεχόμενο|content
απέχω|be distant; abstain
αποχή|abstention
ανοχή|tolerance
μέτοχος|shareholder
προσοχή|attention
εξοχή|countryside
""", note="**σχ-** is the aorist of έχω (ἔσχον): a **σχέση** is how you *hold* to someone, a **σχήμα** how a thing *holds itself*. **σχολή** first meant *leisure* (time you hold for yourself), then what the leisured did: study. The ο-form gives **προσοχή** *holding towards* and **εξοχή** *what stands out*: the open country."),
  G("μεν- / μον-", "stay, remain", el="μένω", m="""
μένω|stay; live
περιμένω|wait
παραμένω|remain
επιμένω|insist
επιμονή|persistence
υπομονή|patience
υπομένω|endure
αναμένω|await
απομένω|be left over
μόνιμος|permanent
μονή|monastery
""", note="**υπομονή** is *staying under* a weight, **επιμονή** *staying on* a point. **μονή** is a place where monks stay; **μόνιμος** *staying for good* (μόνιμη θέση *a permanent post*)."),
  G("λαβ- / ληπ- / ληψ- / λαμβ-", "take", el="λαμβάνω (formal), παίρνω (everyday)", m="""
λαμβάνω|receive (formal)
λήψη|receipt; reception
λαβή|handle; grip
καταλαβαίνω|understand
αναλαμβάνω|take on, undertake
απολαμβάνω|enjoy
περιλαμβάνω|include
συλλαμβάνω|arrest; conceive
σύλληψη|arrest; conception
συλλαβή|syllable
προκατάληψη|prejudice
παραλήπτης|recipient (of a letter)
""", note="Everyday Greek says **παίρνω** *take*, but every compound keeps **λαμβάνω**: **καταλαβαίνω** *take down (into the mind)*, **απολαμβάνω** *take from, enjoy*, **συλλαμβάνω** *take together*: arrest, or conceive (a child, an idea). A **συλλαβή** is letters *taken together*. On a parcel: **αποστολέας** *sender*, **παραλήπτης** *recipient*."),
  G("δο- / δοσ- / δω-", "give", el="δίνω (δίδω)", m="""
δίνω|give
δόση|dose; instalment
δώρο|gift
δωρεάν|free of charge
δωρεά|donation
παράδοση|tradition; delivery
προδοσία|betrayal
προδότης|traitor
έκδοση|edition; publication
εκδότης|publisher
απόδοση|performance; yield
μεταδίδω|transmit; broadcast
ανέκδοτο|joke
""", note="**παράδοση** is *handing over*: of goods (delivery) or of customs from one generation to the next (tradition). **προδοσία** is handing over the wrong way. An **ανέκδοτο** was once an *unpublished* story (α(ν)- + έκδοση) and became the word for a joke. **δωρεάν** *as a gift*: free."),
 ]),

dict(id="roots-word", part="Δ", el="Ρίζες του λόγου και της γνώσης", title="Root families: saying, voice, knowing, learning", level="A2–C1",
 intro=[{"p": "Words for speech and knowledge. **λέγω** alone generates more abstract nouns than any other Greek verb; **γνω-** and **μαθ-** give the vocabulary of school and study."}, ROOTS_NOTE],
 groups=[
  G("λεγ- / λογ- / λεξ-", "say; choose; reason", el="λέω (λέγω)", m="""
λέξη|word
λεξικό|dictionary
λόγος|speech; reason
λογικός|reasonable, logical
διάλογος|dialogue
πρόλογος|preface
επίλογος|epilogue
διαλέγω|choose
συλλογή|collection
εκλογές|elections
αναλογία|proportion; analogy
απολογία|defence (in court)
λογαριασμός|bill; account
λογοτεχνία|literature
""", note="The root once meant both *gather, pick* and *say* (to pick words). From *pick*: **διαλέγω** *choose*, **συλλογή** *collection*, **εκλογές** *elections*. From *say*: **λόγος**, **λέξη**, **διάλογος**. From *reckon*: **λογαριασμός**, **λογικός**. **-λογία** names a science (βιολογία), **-λόγος** its practitioner (βιολόγος)."),
  G("φων-", "voice, sound", el="φωνή", m="""
φωνή|voice
φωνάζω|shout; call
φωνήεν|vowel
σύμφωνο|consonant; pact
συμφωνώ|agree
συμφωνία|agreement; symphony
διαφωνώ|disagree
διαφωνία|disagreement
ομόφωνος|unanimous
άφωνος|speechless
τηλέφωνο|telephone
μικρόφωνο|microphone
""", note="To agree is to *sound together* (**συμφωνώ**), to disagree to *sound apart* (**διαφωνώ**). A **σύμφωνο** is a letter that sounds *with* a vowel, and also a pact (σύμφωνο συμβίωσης *civil partnership*). **ομόφωνα** *with one voice*: unanimously."),
  G("γνω-", "know", el="γνωρίζω (ξέρω)", m="""
γνωρίζω|know; get to know
γνώση|knowledge
γνωστός|known; acquaintance
άγνωστος|unknown
γνώμη|opinion
γνωριμία|acquaintance
αναγνωρίζω|recognise
ανάγνωση|reading
αναγνώστης|reader
διάγνωση|diagnosis
πρόγνωση|forecast, prognosis
επίγνωση|awareness
συγγνώμη|sorry; forgiveness
""", note="**ανάγνωση** is *knowing again* (the letters): reading. **διάγνωση** is *knowing through*, **πρόγνωση** *knowing before* (πρόγνωση καιρού *weather forecast*). **συγγνώμη** is *knowing with*: understanding someone's fault, hence forgiveness. **ξέρω** is the everyday *know (a fact)*; **γνωρίζω** is *know a person* or formal *know*."),
  G("μαθ-", "learn", el="μαθαίνω", m="""
μαθαίνω|learn; find out
μάθημα|lesson
μαθητής|pupil
μάθηση|learning
μαθηματικά|mathematics
μαθητεία|apprenticeship
αμάθεια|ignorance
πολυμαθής|very learned
κακομαθημένος|spoilt
μαθημένος|used to
ξεμαθαίνω|unlearn, lose the habit
""", note="**μαθηματικά** were simply *the things learnt*. **μαθημένος** *used to it* and **κακομαθημένος** *badly brought up, spoilt* come from μαθαίνω in its sense *get used to*: *Είμαι μαθημένος να ξυπνάω νωρίς* I'm used to getting up early."),
 ]),

dict(id="roots-mind", part="Δ", el="Ρίζες της σκέψης και της αντίληψης", title="Root families: thinking, seeing, hearing, judging, remembering, understanding", level="B1–C1",
 intro=[{"p": "The roots behind the vocabulary of opinion, perception and memory, the words you need to discuss ideas in the B2 and C1 speaking papers."}, ROOTS_NOTE],
 groups=[
  G("σκοπ- / σκεπ- / σκεψ-", "look at, consider", el="σκέφτομαι", m="""
σκέφτομαι|think
σκέψη|thought
σκοπός|aim, purpose
σκόπιμος|deliberate; advisable
αποσκοπώ|aim at
επισκέπτομαι|visit
επίσκεψη|visit
επισκέπτης|visitor
ανασκόπηση|review
σκεπτικισμός|scepticism
τηλεσκόπιο|telescope
μικροσκόπιο|microscope
""", note="The root is *look carefully*: **σκέφτομαι** *look into (in the mind)*, **σκοπός** *what you look at*: the target, the aim. **επισκέπτομαι** first meant *look in on*, as a doctor or an inspector does. A **τηλεσκόπιο** looks far, a **μικροσκόπιο** looks at the small."),
  G("ορ- / οπ- / οψ-", "see", el="βλέπω (everyday), ancient ορώ", m="""
όραση|sight
ορατός|visible
αόρατος|invisible
όραμα|vision
οπτικός|optical, visual
όψη|appearance, aspect
άποψη|view, opinion
σύνοψη|summary
πρόσοψη|façade
επόπτης|supervisor
""", note="**βλέπω** is the everyday verb, but learned words take **ορ-** and **οπ- / οψ-**. **άποψη** is *a view from (somewhere)*: an opinion; **σύνοψη** *seeing together*: a summary; **πρόσοψη** *the side that looks out front*. Useful at B2: *Από την άποψή μου…* From my point of view…"),
  G("ακου- / ακο-", "hear", el="ακούω", m="""
ακούω|hear; listen
ακοή|hearing
ακουστικό|receiver; headphone
ακουστικός|acoustic
ακουστός|audible
ανήκουστος|unheard of, outrageous
υπακούω|obey
υπάκουος|obedient
παρακούω|mishear; disobey
""", note="To **obey** is to *listen under* (**υπακούω**, like Latin *ob-oedire*). **παρακούω** is listening wrongly: either mishearing or not doing as told. **ανήκουστο!** *unheard of!* is a common exclamation of outrage."),
  G("κριν- / κρισ- / κριτ-", "judge, separate", el="κρίνω", m="""
κρίνω|judge
κρίση|crisis; judgement
κριτής|judge (of a contest)
κριτική|criticism; review
κριτικός|critical; critic
κριτήριο|criterion
διακρίνω|distinguish
διάκριση|distinction; discrimination
σύγκριση|comparison
ανάκριση|interrogation
υποκριτής|hypocrite
""", note="**κρίση** is the *decisive moment*, when things are judged: a crisis. **διάκριση** is *separating apart*: either honour (a distinction) or unfairness (discrimination). The ancient **υποκριτής** was an *actor*, one who answers on stage; the modern word means a hypocrite, someone who plays a part. A court judge is **δικαστής**, not κριτής."),
  G("μνη- / μνημ-", "remember", el="θυμάμαι (everyday), ancient μιμνήσκομαι", m="""
μνήμη|memory
μνημείο|monument
μνημόσυνο|memorial service
μνημόνιο|memorandum
ανάμνηση|recollection, memory
αμνησία|amnesia
αμνηστία|amnesty
υπόμνηση|reminder
αξιομνημόνευτος|memorable
""", note="**μνήμη** is the faculty (memory), **ανάμνηση** a single memory. **αμνηστία** is a *not remembering* by law: amnesty. **Το Μνημόνιο** (plural τα Μνημόνια) is what Greeks call the bailout memoranda of 2010–2018. The everyday verb **θυμάμαι** belongs to a different root (see θυμ- in the chapter on feelings)."),
  G("νο- / νου-", "mind, understand", el="νους, κατανοώ", m="""
νους|mind
νόημα|meaning, sense
νοημοσύνη|intelligence
κατανοώ|understand
κατανόηση|understanding
παρανόηση|misunderstanding
έννοια|concept; worry
διάνοια|intellect; genius
ευνόητος|self-evident
υπονοώ|imply
μετάνοια|repentance
""", note="**νόημα** is *what is in mind*: the meaning (*Δεν έχει νόημα* There's no point). **έννοια** is a concept, and in everyday speech also *worry, care*: *Έννοια σου!* Don't worry! **τεχνητή νοημοσύνη** is *artificial intelligence*."),
 ]),

dict(id="roots-doing", part="Δ", el="Ρίζες της πράξης και της δημιουργίας", title="Root families: work, making, doing, craft, turning, loosening", level="B1–C1",
 intro=[{"p": "Six roots of doing and making. Learn the shapes **εργ- / ουργ-** and **ποι-**: they end hundreds of compounds (χειρουργός, δημιουργός, ηθοποιός, απλοποιώ)."}, ROOTS_NOTE],
 groups=[
  G("εργ- / ουργ-", "work", el="εργάζομαι, έργο", m="""
έργο|work; project; play, film
εργασία|work; assignment
εργάζομαι|work
εργάτης|worker
εργαλείο|tool
εργοστάσιο|factory
εργαστήριο|workshop; laboratory
συνεργάτης|collaborator
άνεργος|unemployed
ανεργία|unemployment
ενέργεια|energy; action
αργία|public holiday
υπουργός|minister
χειρουργός|surgeon
δημιουργός|creator
""", note="At the end of a compound **εργ-** becomes **-ουργός**: the **χειρουργός** works with his hands, the **δημιουργός** works for the people (δήμος), the **υπουργός** works under (someone). **αργία** is *not working* (α- + εργ-): a public holiday; **αργός** *slow, idle* is the same word."),
  G("ποι-", "make, do", el="ποιώ (in compounds), κάνω", m="""
ποίημα|poem
ποιητής|poet
ποίηση|poetry
ηθοποιός|actor
απλοποιώ|simplify
αξιοποιώ|make use of
τροποποιώ|modify
πραγματοποιώ|carry out
ενοποίηση|unification
κακοποίηση|abuse
οινοποιείο|winery
""", note="A **ποιητής** is a *maker*, a **ηθοποιός** a *maker of characters* (ήθος). **-ποιώ** makes verbs from adjectives and nouns: απλός → **απλοποιώ**, αξία → **αξιοποιώ**, τρόπος → **τροποποιώ**. Do not mix it up with **ποιος** *who* and **ποιότητα** *quality*, which belong to a different word."),
  G("πραγ- / πραξ- / πρακτ-", "do, act", el="πράττω (formal), κάνω", m="""
πράξη|act, deed; operation (maths)
πράγμα|thing
πραγματικός|real, actual
πραγματικότητα|reality
πρακτικός|practical
πρακτική|practice; work placement
πράκτορας|agent
πρακτορείο|agency
πρακτικά|minutes (of a meeting)
διαπράττω|commit (a crime)
""", note="A **πράγμα** is *something done*, then any thing at all; **πραγματικός** *real* is what has been done, not only talked of. **πρακτική άσκηση** is a student's *work placement*. **Πράξεις των Αποστόλων** is the book of *Acts*."),
  G("τεχν-", "art, craft, skill", el="τέχνη", m="""
τέχνη|art; craft
τεχνική|technique
τεχνικός|technical; technician
τεχνίτης|craftsman
τεχνολογία|technology
τεχνητός|artificial
καλλιτέχνης|artist
χειροτεχνία|handicraft
λογοτεχνία|literature
πολυτεχνείο|polytechnic, technical university
""", note="**τέχνη** covers both *art* and *craft*: **οι καλές τέχνες** *the fine arts*, **τέχνη** *skill* in *Έχει τέχνη στο μαγείρεμα*. **Το Πολυτεχνείο** also names the student uprising of November 1973 at the Athens Polytechnic, remembered every 17 November."),
  G("τρεπ- / τροπ-", "turn", el="τρέπω (in compounds)", m="""
τρόπος|way, manner
τροπή|turn (of events)
επιτρέπω|allow
μετατρέπω|convert
μετατροπή|conversion
ανατροπή|overthrow; twist
αποτρέπω|deter, prevent
προτρέπω|urge
επιτροπή|committee
τρόπαιο|trophy
""", note="To **allow** is to *turn (the matter) over to* someone (**επιτρέπω**); an **επιτροπή** is a body things are turned over to. A **τρόπαιο** marked the spot where the enemy *turned* and fled. **τρόπος** *way* gives the everyday **με κάθε τρόπο** *by all means* and **τρόποι** *manners*."),
  G("στρεφ- / στροφ-", "turn round", el="στρέφω, γυρίζω (everyday)", m="""
στρέφω|turn
στροφή|turn; bend
επιστρέφω|return
επιστροφή|return; refund
καταστρέφω|destroy
καταστροφή|destruction; disaster
αναστροφή|reversal
διαστρέφω|distort, twist
αποστροφή|aversion; apostrophe
περιστροφή|rotation
""", note="Different from **τρεπ-**: στρέφω is *turn round, rotate*. **καταστρέφω** is *turn completely upside down*: destroy. The **απόστροφος** (η) is the written apostrophe; **αποστροφή** is a *turning away* in disgust."),
  G("λυ- / λυσ-", "loosen, untie, solve", el="λύνω", m="""
λύνω|solve; untie
λύση|solution
αναλύω|analyse
ανάλυση|analysis
διαλύω|dissolve; break up
διάλυση|dissolution; break-up
απολύω|dismiss, lay off
απόλυτος|absolute
απολυτήριο|school-leaving certificate
παράλυση|paralysis
""", note="**ανάλυση** is *loosening up* into parts. **απολύω** is *let loose*: release a prisoner, discharge a soldier, dismiss an employee. **απόλυτος** is *loosed from everything*: absolute. The **απολυτήριο** releases you from school."),
 ]),

dict(id="roots-society", part="Δ", el="Ρίζες της ζωής και της κοινωνίας", title="Root families: life, birth, people, city, home, law, rule, power", level="B1–C1",
 intro=[{"p": "The roots of public life. Read a Greek newspaper and you meet these on every line: **δημ-** (δήμος, δημόσιος), **πολιτ-** (πολίτης, πολιτική), **νομ-** (νόμος), **αρχ-** (αρχή, αρχηγός) and **κρατ-** (κράτος, δημοκρατία)."}, ROOTS_NOTE],
 groups=[
  G("βι- / βιο-", "life (as lived)", el="βίος", m="""
βίος|life (formal)
βιολογία|biology
βιογραφία|biography
βιώνω|experience, live through
βίωμα|lived experience
βιώσιμος|sustainable, viable
βιοποικιλότητα|biodiversity
αντιβιοτικό|antibiotic
αμφίβιος|amphibious
μακροβιότητα|longevity
""", note="**βίος** is a life as lived (its course, its story), **ζωή** life as being alive. Hence **βιογραφία** but **ζωολογία**. **βιώσιμη ανάπτυξη** is *sustainable development*."),
  G("ζω-", "live, life", el="ζω", m="""
ζωή|life
ζώο|animal
ζωντανός|alive; lively
ζωηρός|lively
ζωτικός|vital
ζωγράφος|painter
ζωγραφική|painting
επιζώ|survive
αναζωογονώ|revive, refresh
""", note="A **ζωγράφος** is one who *paints living things* (ζω + γράφω). **επιζώ** *live on after*: survive; the survivors of a disaster are **οι επιζώντες**."),
  G("γεν- / γον-", "birth, origin, kind", el="γεννώ, γίνομαι", m="""
γέννηση|birth
γεννιέμαι|be born
γενέθλια|birthday
γενιά|generation
γονιός|parent
πρόγονος|ancestor
απόγονος|descendant
γένος|gender; kind, race
γενικός|general
γενναίος|brave
συγγενής|relative
οικογένεια|family
""", note="**γεν-** is the birth, **γον-** (the ο-form) the one who gives it: **γονιός**, **πρόγονος**. **γενικός** is *of the whole kind*: general. **γενναίος** *well-born*, hence noble, brave. **συγγενής** *of the same birth*: a relative."),
  G("δημ-", "the people; the municipality", el="δήμος", m="""
δήμος|municipality
δήμαρχος|mayor
δημόσιος|public
δημοσιογράφος|journalist
δημοσίευση|publication
δημοτικός|municipal; folk
δημοτικό|primary school
δημοκρατία|democracy; republic
δημοφιλής|popular
δημοψήφισμα|referendum
δημογραφικός|demographic
""", note="The **δήμος** was the people; today it is also the *municipality* with its **δήμαρχος**. **δημοτικό** is the primary school, **δημοτικό τραγούδι** a folk song, and **δημοτική** the spoken language (as against **καθαρεύουσα**). **Ελληνική Δημοκρατία** is the official name of the state: *the Hellenic Republic*."),
  G("πολ- / πολιτ-", "city, citizen", el="πόλη", m="""
πόλη|city
πολίτης|citizen
πολιτικός|political; politician; civil
πολιτική|politics; policy
πολιτεία|state; polity
πολιτισμός|civilisation; culture
πολιτιστικός|cultural
συμπολίτης|fellow citizen
μητρόπολη|metropolis; cathedral
ακρόπολη|acropolis
πολεοδομία|town planning
""", note="**πολιτικός** has three senses: *political*, *a politician*, and *civil* (πολιτικός μηχανικός *civil engineer*, πολιτικός γάμος *civil wedding*). **πολιτισμός** is civilisation or culture, its adjective **πολιτιστικός** (πολιτιστικό κέντρο *cultural centre*)."),
  G("οικ-", "house, household", el="οίκος (σπίτι)", m="""
οίκος|house (firm, dynasty)
οικογένεια|family
οικονομία|economy; savings
οικονομικός|economic; cheap
οικιακός|domestic, household
κατοικία|residence
κάτοικος|inhabitant
πολυκατοικία|apartment block
οικόπεδο|building plot
οικοδομή|building site
οικολογία|ecology
παροικία|community (abroad)
""", note="**οικονομία** is *managing the household* (οίκος + νέμω), so **κάνω οικονομία** means *save money* and **οικονομικός** can mean *cheap*. **οίκος** survives for firms and dynasties: **εκδοτικός οίκος** *publishing house*, **οίκος μόδας** *fashion house*."),
  G("νομ-", "law; share out", el="νόμος", m="""
νόμος|law
νόμιμος|legal, lawful
παράνομος|illegal
νομικός|legal; lawyer
νομοσχέδιο|bill (draft law)
νομοθεσία|legislation
αυτονομία|autonomy
αστυνομία|police
νομός|prefecture
νόμισμα|currency; coin
αστρονομία|astronomy
διανομή|distribution
""", note="Watch the stress: **ο νόμος** *law*, **ο νομός** *prefecture* (an old administrative district). The root first meant *share out* (νέμω): **διανομή** *distribution*, **νομός** a share of land. A **νόμισμα** is what custom (νόμος) accepts as money."),
  G("αρχ-", "beginning; rule", el="αρχή", m="""
αρχή|beginning; principle; authority
αρχίζω|begin
αρχικός|initial
αρχαίος|ancient
αρχείο|archive; file
αρχηγός|leader
μοναρχία|monarchy
αναρχία|anarchy
δήμαρχος|mayor
υπάρχω|exist
""", note="The root means both *be first in time* (αρχή *beginning*, αρχαίος *ancient*) and *be first in rank* (αρχηγός, μοναρχία *rule of one*, δήμαρχος). **οι αρχές** in the news are *the authorities*. **υπάρχω** is *be there from the beginning*: exist."),
  G("κρατ-", "power, hold", el="κράτος, κρατώ", m="""
κράτος|state
κρατικός|state, public
κρατώ|hold; keep
κράτηση|booking; detention
κρατούμενος|prisoner, detainee
συγκρατώ|restrain
επικρατώ|prevail
δημοκρατία|democracy
αριστοκρατία|aristocracy
γραφειοκρατία|bureaucracy
αυτοκράτορας|emperor
""", note="**κράτος** first meant *strength*, then the power that rules: the state. **-κρατία** names who holds power: δημοκρατία (the people), αριστοκρατία (the best), γραφειοκρατία (the desk, γραφείο). **κρατώ** is everyday: *hold, keep*: *Κράτα τα ρέστα* Keep the change."),
 ]),

dict(id="roots-world", part="Δ", el="Ρίζες του χρόνου, του χώρου και της φύσης", title="Root families: time, place, earth, light, water, heat, measure, world, nature", level="A2–C1",
 intro=[{"p": "The physical world. Several of these roots are hidden behind an everyday word that looks different: **νερό** but **υδρ-**, **γη** but **γεω-**, **φως** but **φωτ-**."}, ROOTS_NOTE],
 groups=[
  G("χρον-", "time", el="χρόνος", m="""
χρόνος|time; year; tense
χρονιά|year (as a period)
χρονολογία|date; chronology
χρονόμετρο|stopwatch
σύγχρονος|contemporary, modern
συγχρονίζω|synchronise
χρόνιος|chronic
διαχρονικός|timeless; diachronic
αναχρονισμός|anachronism
πρωτοχρονιά|New Year's Day
""", note="Note the plurals: **οι χρόνοι** *times, tenses*, **τα χρόνια** *years* (*Χρόνια πολλά!* Many happy returns). **σύγχρονος** is *of the same time*: contemporary, modern (σύγχρονη τέχνη *contemporary art*)."),
  G("τοπ-", "place", el="τόπος", m="""
τόπος|place
τοπικός|local
τοποθεσία|location, site
τοποθετώ|place, put
τοπίο|landscape
εντοπίζω|locate, detect
μετατοπίζω|shift
τοπωνύμιο|place name
ουτοπία|utopia
""", note="**ουτοπία** is *no place* (ου- *not*). **εντοπίζω** *put in a place*: find, detect (εντόπισαν το πρόβλημα *they found the problem*). **τοπικός** is *local*, as in **τοπική αυτοδιοίκηση** *local government*."),
  G("γη / γε- / γεω-", "earth, land", el="γη", m="""
γη|earth; land
γήπεδο|pitch, sports ground
γήινος|earthly
υπόγειο|basement
ισόγειο|ground floor
μεσόγειος|inland
γεωγραφία|geography
γεωργία|agriculture
γεωργός|farmer
γεωλογία|geology
γεωμετρία|geometry
απόγειο|peak, apogee
""", note="**ισόγειο** is the floor *level with the ground*; **υπόγειο** *under the ground*. **Μεσόγειος** is the *sea in the middle of the lands*. **γεωργός** works the earth (γη + έργο); **γεωμετρία** began as land surveying."),
  G("φως / φωτ-", "light", el="φως (του φωτός)", m="""
φως|light
φωτιά|fire
φωτίζω|light up
φωτεινός|bright
φωτισμός|lighting
Διαφωτισμός|the Enlightenment
φωτογραφία|photograph
φωτοτυπία|photocopy
φωτοβολταϊκό|solar panel
Φώτα|Epiphany
""", note="The genitive **του φωτός** shows the stem **φωτ-** that every derivative uses. **Τα Φώτα** (6 January) is the feast of lights, when the waters are blessed. **φωτιά** *fire* is light made visible."),
  G("υδρ- / νερ-", "water", el="νερό (ancient ύδωρ)", m="""
νερό|water
νεροχύτης|sink
νερόβραστος|boiled in water; bland
υδραυλικός|plumber
ύδρευση|water supply
υδρογόνο|hydrogen
αφυδάτωση|dehydration
ενυδρείο|aquarium
υδροπλάνο|seaplane
""", note="Everyday words build on **νερό**, learned ones on **υδρ- / υδατ-** (genitive of ύδωρ: ύδατος). The **υδραυλικός** is your *plumber*; a bill from **ΕΥΔΑΠ** (Εταιρεία Ύδρευσης και Αποχέτευσης Πρωτευούσης) is your Athens water bill."),
  G("θερμ-", "heat", el="θερμός (ζεστός)", m="""
θερμός|warm, hot (formal)
θερμοκρασία|temperature
θερμόμετρο|thermometer
θέρμανση|heating
θερμίδα|calorie
θερμοσίφωνας|water heater
θερμοκήπιο|greenhouse
υπερθέρμανση|overheating; global warming
θερμότητα|heat; warmth
""", note="Everyday Greek says **ζεστός**, but technical words use **θερμ-**: **κεντρική θέρμανση** *central heating*, **θερμοσίφωνας** (turn it on before a shower, Greek-style). **το φαινόμενο του θερμοκηπίου** is *the greenhouse effect*."),
  G("μετρ-", "measure", el="μετρώ", m="""
μέτρο|metre; measure
μετρώ|count; measure
μέτρηση|measurement
μέτριος|average, mediocre
μετρητά|cash
αμέτρητος|countless
μετριοπαθής|moderate
συμμετρία|symmetry
διάμετρος|diameter
περίμετρος|perimeter
""", note="**τα μέτρα** in the news are *measures* (λήψη μέτρων *taking measures*). **μέτριος** is *of measure*: average, middling, and of coffee *medium sweet* (ένας μέτριος *one medium-sweet Greek coffee*). **μετρητά** is cash you can count."),
  G("κοσμ-", "order, world, ornament", el="κόσμος", m="""
κόσμος|world; people
παγκόσμιος|global, world-wide
κοσμικός|worldly; social, high-society
κόσμημα|jewel
κοσμοπολίτης|cosmopolitan
διάκοσμος|decoration
κοσμολογία|cosmology
""", note="**κόσμος** first meant *order*, then *ornament* (κόσμημα *jewel*), then the ordered universe. In speech it also means *people*: *Είχε πολύ κόσμο* There were a lot of people. **κοσμικά νέα** are society pages."),
  G("φυσ-", "nature", el="φύση", m="""
φύση|nature
φυσικός|natural; physical; physicist
φυσική|physics
φυσικά|of course, naturally
φυσιολογικός|normal
υπερφυσικός|supernatural
φυσικοθεραπεία|physiotherapy
φυσιογνωμία|personality, figure
""", note="**φυσιολογικός** is the everyday *normal* (*Είναι φυσιολογικό να αγχώνεσαι* It's normal to feel stressed). **φυσικά!** *of course!* **φυσάω** *blow* looks similar but is a different word."),
 ]),

dict(id="roots-feeling", part="Δ", el="Ρίζες της ψυχής και του συναισθήματος", title="Root families: soul, suffering, love, fear, joy, hope, trust, spirit, feeling", level="B1–C1",
 intro=[{"p": "Feelings are where Greek and English look most alike and differ most. The roots are familiar (psyche, pathos, philo-, phobia, aesthetic), but the Greek words often mean something else: **συμπαθητικός** is *likeable*, **εμπάθεια** is *rancour*, **αισθηματικός** is *romantic*. Each family flags the traps."}, ROOTS_NOTE],
 groups=[
  G("ψυχ-", "soul, mind", el="ψυχή", m="""
ψυχή|soul
ψυχικός|mental, psychological
ψυχολογία|psychology
ψυχολόγος|psychologist
ψυχίατρος|psychiatrist
ψυχοθεραπεία|psychotherapy
ψυχαγωγία|entertainment
μεγαλοψυχία|magnanimity
ψυχοφθόρος|soul-destroying
ψυχούλα|darling
""", note="**ψυχική υγεία** is *mental health*. **ψυχαγωγία** (leading the soul) is the formal word for entertainment. In speech **ψυχή μου** and **ψυχούλα μου** are endearments."),
  G("παθ- / πασχ-", "suffer, undergo", el="παθαίνω, πάσχω", m="""
πάθος|passion
πάθηση|(medical) condition
παθαίνω|suffer, undergo
πάσχω|suffer (from an illness)
παθητικός|passive
συμπάθεια|liking, fondness
συμπαθητικός|likeable, nice
αντιπάθεια|dislike
απάθεια|apathy
εμπάθεια|rancour, malice
τηλεπάθεια|telepathy
παθολόγος|GP, internist
""", note="Traps: **συμπαθητικός** is *likeable* (sympathetic is **συμπονετικός**); **εμπάθεια** is *ill will, rancour* (empathy is **ενσυναίσθηση**). **Τι έπαθες;** *What happened to you?* is the everyday use of παθαίνω. The **παθολόγος** is the doctor you see first."),
  G("φιλ-", "love, friend", el="φίλος, φιλώ", m="""
φίλος|friend
φιλία|friendship
φιλώ|kiss
φιλί|kiss
φιλικός|friendly
φιλόξενος|hospitable
φιλοξενία|hospitality
φιλότιμο|sense of honour
φιλόδοξος|ambitious
φιλανθρωπία|charity
φίλαθλος|sports fan
φιλάρεσκος|vain, eager to please
""", note="**φιλώ** is *kiss* (and only formally *love*). **φιλο-** + noun makes *fond of*: φιλόξενος *fond of strangers*, φίλαθλος *fond of sport*, φιλόδοξος *fond of glory*: ambitious. **φιλότιμο** (love of honour) is one of the words Greeks say cannot be translated."),
  G("φοβ-", "fear", el="φοβάμαι", m="""
φόβος|fear
φοβάμαι|be afraid
φοβίζω|frighten
φοβισμένος|frightened
φοβερός|terrible; amazing
φοβία|phobia
άφοβος|fearless
φοβιτσιάρης|scaredy-cat
ξενοφοβία|xenophobia
κλειστοφοβία|claustrophobia
""", note="**φοβάμαι** takes **μη(ν)** for *fear that*: *Φοβάμαι μην αργήσουμε* I'm afraid we'll be late. **φοβερός** in speech is mostly praise: *φοβερό φαγητό!* amazing food."),
  G("χαρ-", "joy, grace", el="χαρά, χαίρομαι", m="""
χαρά|joy
χαίρομαι|be glad
χαρούμενος|cheerful, happy
χάρη|grace; favour
χαρίζω|give as a gift
χάρισμα|gift, talent
χαριτωμένος|cute, charming
ευχαριστώ|thank
ευχάριστος|pleasant
αχάριστος|ungrateful
χαιρετώ|greet
""", note="**Χαίρω πολύ** *pleased to meet you* and **χαιρετώ** *greet* both come from *rejoice*. **χάρη** is grace and also a favour: **κάνε μου μια χάρη** *do me a favour*; **χάρη σε** *thanks to*. **ευχαριστώ** is *show good grace*."),
  G("ελπ-", "hope", el="ελπίζω", m="""
ελπίδα|hope
ελπίζω|hope
απελπισία|despair
απελπίζομαι|despair
απελπισμένος|desperate
ελπιδοφόρος|hopeful, promising
""", note="**απελπισία** is hope *gone away* (απο-). **ελπιδοφόρος** *hope-bearing* is a favourite word of headlines: ελπιδοφόρα μηνύματα *encouraging signs*."),
  G("πιστ-", "trust, faith", el="πιστεύω", m="""
πίστη|faith
πιστεύω|believe
πιστός|faithful, loyal
απιστία|infidelity
απίστευτος|unbelievable
εμπιστεύομαι|trust
εμπιστοσύνη|trust, confidence
δυσπιστία|distrust
πιστοποιητικό|certificate
πιστωτικός|credit
""", note="Banking and paperwork use the same root: a **πιστωτική κάρτα** is a credit card (credit is trust), a **πιστοποιητικό** certifies something as trustworthy. **ψήφος εμπιστοσύνης** is a *vote of confidence* in parliament."),
  G("θυμ-", "spirit, temper, mind", el="θυμός, θυμάμαι", m="""
θυμός|anger
θυμώνω|get angry
θυμάμαι|remember
θυμίζω|remind
επιθυμία|desire
επιθυμώ|wish, desire
ενθύμιο|souvenir, keepsake
προθυμία|willingness
πρόθυμος|willing
ευθυμία|cheerfulness
""", note="**θυμός** was the spirit or heart; it heated into *anger* (θυμώνω), and *having in mind* gave **θυμάμαι** *remember* (from ενθυμούμαι) and **θυμίζω** *remind*. **επιθυμία** is *setting one's heart on*, **πρόθυμος** *with the heart forward*: willing."),
  G("αισθ-", "sense, feel", el="αισθάνομαι", m="""
αισθάνομαι|feel
αίσθηση|sense; sensation
αίσθημα|feeling
συναίσθημα|emotion
ενσυναίσθηση|empathy
αισθηματικός|sentimental, romantic
αισθητικός|aesthetic; beautician
αισθησιακός|sensual
ευαίσθητος|sensitive
αναίσθητος|unconscious; insensitive
αναισθητικό|anaesthetic
""", note="Four adjectives that learners mix up: **αισθηματικός** *romantic, sentimental* (αισθηματική ταινία *a romance*), **αισθητικός** *aesthetic* (and as a noun, *beautician*), **αισθησιακός** *sensual*, **ευαίσθητος** *sensitive*. **αναίσθητος** is literally *without sensation*: unconscious, or unfeeling."),
 ]),
]
