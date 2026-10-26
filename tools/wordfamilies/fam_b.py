from common import G

ASSIM = "Prefixes ending in a vowel usually drop it before a vowel (**απο- + ουσία** → **απουσία**, **κατα- + οικώ** → **κατοικώ**). Before a vowel that once had a rough breathing they also turn π and τ into φ and θ (**απο- + αιρώ** → **αφαιρώ**, **μετα- + αύριο** → **μεθαύριο**, **κατα- + ιερός** → **καθιερώνω**). The breathing is no longer written, so learn these as they come. **περι-** and **προ-** never drop their vowel."

CHAPTERS = [
dict(id="prefix-1", part="Β", el="Προθήματα από προθέσεις (Α)", title="Prepositional prefixes I: ανα-, απο-, δια-, εκ-/εξ-, εν-", level="A2–C1",
 intro=[{"p": "Most Greek prefixes are old prepositions. Each has a basic spatial sense (up, away, through, out, in) and a few figurative ones that grew from it. Learn the spatial sense first and the figurative ones follow."},
        {"tip": ASSIM}],
 groups=[
  G("ανα- / αν-", "up; back; again (re-)", m="""
ανεβαίνω|go up, climb
αναβάλλω|postpone
αναγνωρίζω|recognise
ανακαλύπτω|discover
ανακοινώνω|announce
αναπνέω|breathe
αναλύω|analyse
αναγέννηση|renaissance, rebirth
ανασκαφή|excavation
ανάμνηση|memory, recollection
ανακαίνιση|renovation
αναδρομή|retrospective, look back
""", note="Three senses: **up** (ανεβαίνω, ανασκαφή *digging up*), **back** (αναβάλλω *throw back, postpone*, αναδρομή *running back*), **again** (αναγέννηση *birth again*, ανακαίνιση *making new again*). Do not confuse it with **αν-** *not* (ανεργία, ανίκανος), which only appears before a vowel.",
    ex=[("Αναβάλαμε τη συνάντηση για την Πέμπτη.", "We postponed the meeting until Thursday."), ("Τον αναγνώρισα αμέσως από τη φωνή.", "I recognised him at once by his voice.")]),
  G("απο- / απ- / αφ-", "away, off, from; finishing", m="""
αποφεύγω|avoid
απομακρύνω|move away, remove
αποχωρώ|withdraw, leave
αποτυγχάνω|fail
απολύω|dismiss, fire
αποκλείω|exclude; cut off
αποθηκεύω|store; save (a file)
απογοητεύω|disappoint
αποδεικνύω|prove
αποτέλεσμα|result
αποφασίζω|decide
αποστολή|mission; dispatch
απόφοιτος|graduate
απουσία|absence
αφαιρώ|remove, subtract
""", note="The sense is movement **away** (αποχωρώ, απομακρύνω) and, from there, **completion**: something done to the end (αποφασίζω *decide*, αποτέλεσμα *the outcome*, απόφοιτος *one who has finished going to school*).",
    ex=[("Απολύθηκαν σαράντα υπάλληλοι.", "Forty employees were laid off."), ("Μην ξεχάσεις να αποθηκεύσεις το αρχείο.", "Don't forget to save the file.")]),
  G("δια- / δι-", "through, across; apart; between", m="""
διαβάζω|read; study
διασχίζω|cross
διαδρομή|route
διάδρομος|corridor
διαφωνώ|disagree
διαφορά|difference
διαλέγω|choose
διάλογος|dialogue
διαμέρισμα|flat, apartment
διακοπές|holidays
διαρκώ|last
διαφήμιση|advertisement
διεθνής|international
διευθυντής|director, manager
""", note="**Through** (διασχίζω, διαδρομή, διαρκώ *last through*), **apart** (διαφωνώ *voice apart*, διαφορά, διαλέγω *pick out from*, διαμέρισμα *a part divided off*) and **between** (διάλογος *speech between*, διεθνής *between nations*). διακοπή is an *interruption*; the plural διακοπές is *holidays*, a break in work."),
  G("εκ- / εξ-", "out, out of; fully", m="""
εκφράζω|express
εκδίδω|publish; issue
εκλογές|elections
εκπαίδευση|education
εκτελώ|carry out; execute
έκθεση|exhibition; report; essay
εκπλήσσω|surprise
εξαφανίζομαι|disappear
εξάγω|export
εξαγωγή|export (noun)
εξήγηση|explanation
εξωτερικό|abroad
εξαιρετικός|exceptional
εξαντλημένος|exhausted
""", note="**εκ-** before a consonant, **εξ-** before a vowel. The image is something brought **out**: εκφράζω *press out (a thought)*, εκλογές *picking out*, εξάγω *lead out, export*, εξαιρετικός *taken out of the ordinary*. It can also mean *completely*: εξαντλημένος *drained to the last drop*."),
  G("εν- / εμ- / εγ- / ελ-", "in, into", m="""
ενδιαφέρον|interest
ενθουσιασμός|enthusiasm
ενέργεια|energy; action
ενημερώνω|inform
εντύπωση|impression
ενσωματώνω|incorporate
ενοίκιο|rent
εμπιστεύομαι|trust
εμπόριο|trade
εμφανίζομαι|appear
εμπειρία|experience
εγκαταλείπω|abandon
εγχείρηση|operation (surgery)
έλλειψη|lack, shortage
""", note="The ν changes to suit the next sound: **εμ-** before β, π, φ, ψ, μ (εμπόριο, εμφανίζομαι); **εγ-** before γ, κ, ξ, χ (εγκαταλείπω, εγχείρηση); **ελ-** before λ (έλλειψη). εμπειρία is *being in the trial* (πείρα *experience, trial*), εντύπωση a *stamp pressed in*.",
    ex=[("Σε εμπιστεύομαι απόλυτα.", "I trust you completely."), ("Μου έκανε καλή εντύπωση.", "He made a good impression on me.")]),
 ]),

dict(id="prefix-2", part="Β", el="Προθήματα από προθέσεις (Β)", title="Prepositional prefixes II: επι-, κατα-, μετα-, παρα-, περι-, προ-, προσ-", level="A2–C1",
 intro=[{"p": "The second set of prepositional prefixes. **παρα-** is the one to watch: it means *beside*, *wrongly* or *too much*, and the colloquial *too much* sense is fully productive, so you can make new verbs with it yourself (παρατρώω, παρακοιμάμαι, παραλέω)."}],
 groups=[
  G("επι- / επ- / εφ-", "on, upon; in addition; towards", m="""
επιβάτης|passenger
επιβεβαιώνω|confirm
επιτυχία|success
επιχείρηση|business, company; operation
επισκέπτομαι|visit
επιστρέφω|return
επιθυμία|desire
επίθεση|attack
επιπλέον|additionally; extra
επιφάνεια|surface
επιτρέπω|allow
επηρεάζω|influence
επείγων|urgent
εφαρμόζω|apply
""", note="**On, upon** (επιβάτης *one who steps on*, επιφάνεια *what appears on top*), **towards, against** (επίθεση *a setting upon, attack*, επιστρέφω *turn back towards*) and **in addition** (επιπλέον *on top of that*). επ- before a vowel, εφ- where the next vowel once had a rough breathing (εφαρμόζω)."),
  G("κατα- / κατ- / καθ-", "down; against; thoroughly", m="""
κατεβαίνω|go down
καταλαβαίνω|understand
καταστρέφω|destroy
καταφέρνω|manage, succeed
καταγγέλλω|report (a crime), denounce
κατάστημα|shop
κατάσταση|situation; state
καταλήγω|end up
καταναλωτής|consumer
κατηγορώ|accuse; blame
καταπίνω|swallow
κατασκευάζω|build, manufacture
κατοικώ|reside
καθιερώνω|establish
""", note="**Down** (κατεβαίνω, καταπίνω *drink down*), **against** (κατηγορώ *speak against*, καταγγέλλω) and **fully, to the end** (καταστρέφω *turn over completely*, καταναλώνω *spend completely, consume*, καταλήγω *come to the end*). In speech it also intensifies colours and feelings: **κατακόκκινος** *bright red*, **κατενθουσιασμένος** *thrilled*."),
  G("μετα- / μετ- / μεθ-", "change; after; across", m="""
μεταφράζω|translate
μεταφέρω|transport, carry over
μετακομίζω|move house
μεταβολή|change
μεταμόρφωση|transformation
μετανάστης|immigrant, emigrant
μετανιώνω|regret
μεταπτυχιακό|master's degree
μεταγενέστερος|later, subsequent
μεταδίδω|broadcast; transmit
μετέχω|take part
μεθαύριο|the day after tomorrow
""", note="The most productive sense is **change of place or state**: μεταφράζω *carry speech across*, μετακομίζω, μεταμόρφωση *change of form*, μετανιώνω *change one's mind (and regret)*. The time sense **after** shows in μεταπτυχιακό *after the first degree*, μεταγενέστερος, μεθαύριο."),
  G("παρα- / παρ-", "beside; wrongly; too much", m="""
παραλία|beach
παράθυρο|window
παράδειγμα|example
παρακολουθώ|follow; attend
παραδίδω|hand over; deliver
παραγγέλνω|order (food, goods)
παρατηρώ|observe
παρεξήγηση|misunderstanding
παράνομος|illegal
παραλείπω|omit, leave out
παρατρώω|overeat
παρακοιμάμαι|oversleep
παραλίγο|almost, nearly
παραμένω|remain, stay on
""", note="**Beside, along** (παραλία *by the sea*, παράθυρο *by the door*, παρακολουθώ *follow alongside*), **wrongly, against** (παρεξήγηση *mis-explanation*, παράνομος *beside the law*, παραλείπω *leave out*), and in everyday speech **too much** (παρατρώω, παρακοιμάμαι). As a separate word **πάρα** means *very*: πάρα πολύ.",
    ex=[("Παρακοιμήθηκα και έχασα το τρένο.", "I overslept and missed the train."), ("Έγινε μια παρεξήγηση, συγγνώμη.", "There was a misunderstanding, sorry.")]),
  G("περι-", "around, about", m="""
περιγράφω|describe
περιβάλλον|environment
περιοχή|area, region
περίπτωση|case
περιμένω|wait
περιορίζω|limit, restrict
περίπατος|walk, stroll
περιφέρεια|region; periphery
περιεχόμενο|content
περιποιούμαι|take care of, look after
περιέργεια|curiosity
περικυκλώνω|surround
""", note="Unlike the others, **περι-** keeps its ι before a vowel (περιοχή, περιεχόμενο). περιβάλλον is *what is thrown around us*, περίπτωση *what falls around, a case*, περιμένω *stay around (until)*."),
  G("προ-", "before, forward, in front", m="""
πρόβλημα|problem
πρόγραμμα|programme
προβλέπω|foresee, forecast
πρόοδος|progress
προτείνω|propose
προχωρώ|proceed, go on
προτιμώ|prefer
προϋπόθεση|precondition
προηγούμενος|previous
προκαταβολή|down payment, deposit
προχθές|the day before yesterday
πρόεδρος|president
""", note="**προ-** never drops its ο: πρόοδος *a way forward*, προϋπόθεση (the diaeresis shows ο and υ are pronounced separately). πρόβλημα is *something thrown in front of you*, πρόεδρος *the one who sits in front*."),
  G("προσ-", "towards; in addition", m="""
προσέχω|pay attention; be careful
προσθέτω|add
προσπαθώ|try
προσφέρω|offer
προσκαλώ|invite
πρόσκληση|invitation
προσαρμόζω|adapt
πρόσβαση|access
προσωρινός|temporary
προσεγγίζω|approach
προσφορά|offer; contribution
πρόσωπο|face
""", note="Keep **προσ-** (towards) apart from **προ-** (before): προσκαλώ *call towards, invite* but προκαλώ *call forth, provoke, challenge*; προσφέρω *bring towards, offer* but προφέρω *bring forth, pronounce*. πρόσωπο is *what faces the eyes*.",
    ex=[("Πρόσεχε, το πάτωμα γλιστράει.", "Careful, the floor is slippery."), ("Η είσοδος έχει πρόσβαση για αναπηρικά αμαξίδια.", "The entrance has wheelchair access.")]),
 ]),

dict(id="prefix-3", part="Β", el="Προθήματα από προθέσεις (Γ)", title="Prepositional prefixes III: συν-, υπερ-, υπο-, αντι-, αμφι-", level="B1–C1",
 intro=[{"p": "**συν-** changes its last letter more than any other prefix, so its family is the hardest to spot: συμφωνώ, συγκρίνω, συλλέγω, σύστημα and συζητώ all start with the same συν- *with*."}],
 groups=[
  G("συν- / συμ- / συγ- / συλ- / συ-", "with, together", m="""
συνεργάζομαι|cooperate
συνάδελφος|colleague
συναυλία|concert
συνέντευξη|interview
συμφωνώ|agree
συμμετέχω|take part
συμπεριφορά|behaviour
συγκρίνω|compare
συγχωρώ|forgive
συλλέγω|collect
σύλλογος|club, association
σύστημα|system
συζητώ|discuss
σύζυγος|spouse
""", note="**συμ-** before β, π, φ, ψ, μ; **συγ-** before γ, κ, ξ, χ; **συλ-** before λ; **συρ-** before ρ (συρρίκνωση *shrinkage*); **συ-** before σ + consonant and ζ (σύστημα, σύζυγος *yoked together*). συναυλία is *playing the pipe together*, συνάδελφος *brother together*.",
    ex=[("Συμφωνώ μαζί σου σε όλα.", "I agree with you on everything."), ("Θα συγκρίνουμε τις δύο προσφορές.", "We'll compare the two offers.")]),
  G("υπερ-", "over, above; too much; super-", m="""
υπερβολή|exaggeration
υπερβαίνω|exceed
υπεραγορά|supermarket
υπερωρία|overtime
υπερπαραγωγή|blockbuster; overproduction
υπέρβαρος|overweight
υπερασπίζομαι|defend
υπερθέρμανση|overheating; global warming
υπερπόντιος|overseas
υπεράνω|above, over
υπερήφανος|proud
""", note="**Over** in space (υπερπόντιος *over the sea*), in amount (υπερβολή *throwing beyond*, υπερωρία *hours beyond*, υπέρβαρος) and in protection (υπερασπίζομαι *hold the shield over*). The everyday form of υπερήφανος is **περήφανος**."),
  G("υπο- / υπ- / υφ-", "under; slightly; subordinate", m="""
υπογράφω|sign
υπόγειος|underground
υποτροφία|scholarship
υποψήφιος|candidate
υπουργός|minister
υπόσχομαι|promise
υποστηρίζω|support
υποθέτω|suppose
υπόθεση|case; hypothesis; affair
υποχρεωτικός|compulsory
υπότιτλος|subtitle
υποβάλλω|submit
υποδέχομαι|welcome, receive
υπάλληλος|employee
""", note="**Under** (υπογράφω *write underneath*, υπόγειος, υπότιτλος) and **subordinate, serving** (υπουργός *one who works under*: once a servant, now a minister; υπάλληλος). υποψήφιος is *under the vote*, υποστηρίζω *prop up from below*."),
  G("αντι- / αντ- / ανθ-", "against; opposite; in exchange; vice-", m="""
αντίθετος|opposite, contrary
αντιμετωπίζω|face, deal with
αντιδρώ|react
αντίδραση|reaction
αντικαθιστώ|replace
αντίγραφο|copy
αντιπρόεδρος|vice-president
αντιβιοτικό|antibiotic
αντιπαθώ|dislike
ανταλλαγή|exchange
ανθυγιεινός|unhealthy
αντισταθμίζω|offset, compensate
""", note="**Against** (αντιβιοτικό *against life (of bacteria)*, αντιπαθώ, ανθυγιεινός), **facing** (αντιμετωπίζω *put one's forehead against*), **in exchange, in place of** (αντικαθιστώ, ανταλλαγή, αντίγραφο *a writing in place of the original*) and **vice-** (αντιπρόεδρος). **αντίο** *goodbye* is not one of them: it comes from Italian *addio*."),
  G("αμφι-", "on both sides; around; doubt", m="""
αμφιθέατρο|amphitheatre; lecture hall
αμφίβιος|amphibious
αμφιβάλλω|doubt
αμφιβολία|doubt
αμφισβητώ|question, dispute
αμφίδρομος|two-way
αμφιλεγόμενος|controversial
αμφιταλαντεύομαι|waver, hesitate
""", note="Literally *on both sides* (αμφίδρομος, αμφίβιος *living both ways*); from there **doubt**: to be thrown both ways (αμφιβάλλω), to argue both sides (αμφισβητώ, αμφιλεγόμενος).",
    ex=[("Δεν αμφιβάλλω ότι θα τα καταφέρεις.", "I don't doubt you'll manage."), ("Ήταν μια αμφιλεγόμενη απόφαση.", "It was a controversial decision.")]),
 ]),

dict(id="prefix-4", part="Β", el="Άρνηση, αξιολόγηση, επανάληψη", title="Negative, evaluative and repetitive prefixes: α-/αν-, δυσ-, ευ-, κακο-, καλο-, ξε-, ξανα-", level="A2–B2",
 intro=[{"p": "These prefixes judge or reverse: *not*, *badly*, *well*, *undo*, *again*. **ξε-** and **ξανα-** are fully alive in speech, so you can attach them to verbs you already know."}],
 groups=[
  G("α- / αν-", "not, without (un-, in-, -less)", m="""
άγνωστος|unknown
άδικος|unjust
άχρηστος|useless
αδύνατος|impossible; thin, weak
ακατάλληλος|unsuitable
αθάνατος|immortal
άπειρος|infinite; inexperienced
άνεργος|unemployed
ανίκανος|incapable
ανεξάρτητος|independent
ανήσυχος|worried, restless
ανώνυμος|anonymous
άυπνος|sleepless
άοπλος|unarmed
""", note="**α-** before a consonant, **αν-** before a vowel; a few old words keep α- before a vowel (άοπλος, άυπνος). The stress usually moves back as far as it can: γνωστός → **ά**γνωστος, χρήσιμος → **ά**χρηστος.",
    ex=[("Είναι άνεργος εδώ και έναν χρόνο.", "He has been unemployed for a year."), ("Αυτή η ταινία είναι ακατάλληλη για παιδιά.", "This film is unsuitable for children.")]),
  G("δυσ-", "bad, hard, ill-", m="""
δύσκολος|difficult
δυσκολία|difficulty
δυστυχία|misery, unhappiness
δυστυχώς|unfortunately
δυσάρεστος|unpleasant
δυσαρέσκεια|displeasure
δυσπιστία|distrust
δυσλεξία|dyslexia
δύσπεπτος|indigestible
δυσανάλογος|disproportionate
δυσφήμιση|defamation
""", note="The opposite of **ευ-**: δυστυχία / ευτυχία, δυσάρεστος / ευχάριστος, δύσκολος / εύκολος. Spelled with **υ**: δυσ- is never δισ- (which means *twice*, as in δισεκατομμύριο *billion*)."),
  G("ευ-", "well, good, easily", m="""
εύκολος|easy
ευκαιρία|opportunity
ευτυχία|happiness
ευτυχώς|fortunately
ευχαριστώ|thank
ευγενικός|polite, kind
ευχάριστος|pleasant
ευαίσθητος|sensitive
ευημερία|prosperity
εύφορος|fertile
ευφυΐα|intelligence
ευέλικτος|flexible
ευδιάθετος|in a good mood
""", note="ευκαιρία is *the good moment* (καιρός *the right time*), ευγενικός *well-born, hence polite*, ευαίσθητος *quick to feel*: **sensitive**, not *sensible* (that is **λογικός**)."),
  G("κακο- / καλο-", "badly / well", m="""
κακοκαιρία|bad weather
κακομαθημένος|spoilt
κακοποίηση|abuse
κακοτυχία|bad luck
κακόγουστος|tasteless
καλοκαίρι|summer
καλοσύνη|kindness
καλοπέραση|comfort, easy living
καλοψημένος|well-done (cooked)
καλοντυμένος|well-dressed
καλοπροαίρετος|well-meaning
""", note="Both attach to participles and adjectives freely: **κακοψημένος** *badly cooked*, **καλοδεχούμενος** *welcome*. καλοκαίρι is *the good weather* (καλός + καιρός)."),
  G("ξε-", "un-, out; the reverse of the base verb", m="""
ξεκλειδώνω|unlock
ξεβιδώνω|unscrew
ξεντύνομαι|undress
ξεπαγώνω|defrost, thaw
ξεχνώ|forget
ξεκουράζομαι|rest
ξεκινώ|start out, set off
ξεφεύγω|escape, get away
ξενυχτώ|stay up all night
ξεπουλώ|sell off
ξεχωρίζω|stand out; tell apart
ξεπερνώ|overcome; surpass
ξεθωριάζω|fade
ξεκαθαρίζω|clear up, clarify
""", note="From ancient **εξ-** *out*. Three uses: **undo** (κλειδώνω *lock* → ξεκλειδώνω; ντύνομαι → ξεντύνομαι), **out, away** (ξεφεύγω, ξεκινώ *move out*), **thoroughly, all the way** (ξενυχτώ *go through the night*, ξεπουλώ *sell everything*). Make your own: **ξεβάφω** *take off make-up, fade*, **ξεκολλάω** *come unstuck*.",
    ex=[("Ξεπάγωσε το κρέας από το πρωί.", "Defrost the meat in the morning."), ("Ξενύχτησα για να τελειώσω την εργασία.", "I stayed up all night to finish the assignment.")]),
  G("ξανα-", "again, re-", m="""
ξαναρχίζω|start again
ξαναβλέπω|see again
ξαναγράφω|rewrite
ξαναζώ|relive
ξαναπαντρεύομαι|remarry
ξαναλέω|say again
ξανασκέφτομαι|reconsider, think again
""", note="Works with almost any verb, in speech and writing: **ξαναδοκιμάζω** *try again*, **ξαναπάω** *go again*. The adverb **ξανά** *again* is the same word. In formal Greek **επανα-** does the job: **επαναλαμβάνω** *repeat*, **επανεκλογή** *re-election*.",
    ex=[("Θα το ξανασκεφτώ και θα σου πω.", "I'll think it over again and let you know.")]),
 ]),

dict(id="prefix-5", part="Β", el="Ποσότητα, ένταση, εαυτός", title="Quantity, intensity and self: πολυ-, μονο-, ημι-/μισο-, αυτο-, αρχι-, θεο-, ολο-, ψιλο-", level="B1–C1",
 intro=[{"p": "The first part of these compounds is an adjective or adverb: πολύς, μόνος, μισός, αυτός, ολος. Colloquial Greek adds a set of intensifiers (θεο-, κατα-, ολο-, πεντα-, τρισ-) and one softener, **ψιλο-** *a bit*."}],
 groups=[
  G("πολυ- / ολιγο- / μονο-", "many / few / one", m="""
πολυκατοικία|apartment block
πολυτέλεια|luxury
πολυάσχολος|very busy
πολύγλωσσος|multilingual
πολυπολιτισμικός|multicultural
ολιγόλεπτος|lasting a few minutes
ολιγαρχία|oligarchy
μονόδρομος|one-way street
μονοπάτι|path
μονότονος|monotonous
μονοκατοικία|detached house
μονογονεϊκός|single-parent
""", note="**πολυκατοικία** (many households) and **μονοκατοικία** (one household) are the two kinds of home in Greek ads. μονοπάτι is *a path for one walker* (μόνος + πατώ)."),
  G("ημι- / μισο-", "half, semi-", m="""
ημιτελής|unfinished
ημίχρονο|half-time
ημιυπόγειο|semi-basement
ημιαπασχόληση|part-time work
ημισέληνος|crescent
μισάνοιχτος|half-open
μισοτιμής|at half price
μισόλογα|half-words, hints
μισοκοιμισμένος|half asleep
μισοτελειωμένος|half-finished
""", note="**ημι-** is learned (official, technical), **μισο-** is everyday: *a half-finished job* is **μισοτελειωμένη δουλειά** in speech, **ημιτελές έργο** in a report."),
  G("αυτο-", "self, auto-", m="""
αυτοκίνητο|car
αυτοπεποίθηση|self-confidence
αυτοαπασχολούμενος|self-employed
αυτοκτονία|suicide
αυτόματος|automatic
αυτοδιοίκηση|self-government
αυτοσυγκράτηση|self-restraint
αυτογνωσία|self-knowledge
αυτοβιογραφία|autobiography
αυτοσχεδιάζω|improvise
αυτοεξυπηρέτηση|self-service
""", note="αυτοκίνητο is *self-moving*. **Τοπική αυτοδιοίκηση** is local government, a term you need for the B2 reading paper."),
  G("αρχι-", "chief, arch-", m="""
αρχιτέκτονας|architect
αρχισυντάκτης|editor-in-chief
αρχιεπίσκοπος|archbishop
αρχιμάγειρας|head chef
αρχιστράτηγος|commander-in-chief
αρχιφύλακας|chief warden
""", note="From **άρχω** *lead*: αρχιτέκτονας is the *master builder*. The same root gives **αρχηγός** *leader*, **αρχή** *beginning, authority* (see the chapter on society)."),
  G("θεο- / κατα- / ολο- / πεντα- / τρισ-", "intensifiers: completely, utterly", m="""
θεόκουφος|stone-deaf
θεοσκότεινος|pitch dark
κατακόκκινος|bright red
καταμεσήμερο|high noon
ολόιδιος|exactly the same
ολομόναχος|all alone
ολοκαίνουργιος|brand new
πεντακάθαρος|spotlessly clean
πεντάρφανος|completely orphaned
τρισευτυχισμένος|blissfully happy
""", note="Spoken Greek loves these: **θεο-** (*god-*), **ολο-** (*all*), **πεντα-** (*five times*), **τρισ-** (*thrice*). They attach mostly to adjectives of colour, light, sound and feeling."),
  G("ψιλο-", "a little, slightly (colloquial)", m="""
ψιλοβρέχει|it's drizzling
ψιλοκουρασμένος|a bit tired
ψιλοκαταλαβαίνω|sort of understand
ψιλοαδιάφορο|more or less irrelevant
ψιλοκόβω|chop finely
""", note="From **ψιλός** *fine, thin*. With verbs and adjectives it softens (ψιλοκουρασμένος *a bit tired*); in cooking it keeps its literal sense: **ψιλοκομμένο κρεμμύδι** *finely chopped onion*. Not to be confused with **ψηλός** *tall*.",
    ex=[("Ψιλοβρέχει, πάρε μια ομπρέλα.", "It's drizzling, take an umbrella."), ("Είμαι ψιλοκουρασμένη σήμερα.", "I'm a bit tired today.")]),
 ]),
]
