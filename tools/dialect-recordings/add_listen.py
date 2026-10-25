"""Write the "listen" block into the dialect pages. Run after clips.py (cues.json)."""
import json, re, sys
CUES = json.load(open(sys.argv[1]))
ROOT = "/home/user/ellinika/library/dialects/"
VL = "https://www.oeaw.ac.at/vlach"
RENDER = "Greek-script lines: the app's rendering of VLACH's phonetic transcription (shown under each line as “VLACH transcription”); English: VLACH's translation."

def g(s):
    out = {}
    for l in s.strip().split("\n"):
        k, v = l.split(" = ", 1)
        lemma, _, rest = v.partition(" — ")
        if rest and not re.search("[α-ωά-ώΑ-Ω]", lemma):  # English headword: show it as a plain gloss
            v = lemma + (" " if rest.startswith("(") else ", ") + rest
        out[k] = v
    return out

W_GLOSS = g("""παρχάρ = παρχάρ — summer mountain pasture (Pontic)
πάπον = πάππος — grandfather (Pontic)
τρανίτερος = τρανός — bigger, older (comparative)
νέικον = νέος — young (Pontic)
έτον = ήταν — he was (Pontic έτον)
σο = σε + το — in the, to the (Pontic)
σον = σε + τον — in the, to the (Pontic)
καλύβ = καλύβι — hut (Pontic drops final -ι)
βράδ = βράδυ — evening, night
κ = και — and (Pontic κ' [kʲe])
απού = από — from; απού κάποτε, after a while (Pontic)
εξέβεν = εβγαίνω — he went out (Pontic aorist)
οξωκά = έξω — outside (Pontic)
α = από — from (Pontic α σο, from the)
καπινέδες = καπινές — privy, toilet (Pontic)
ορμίεν = forest — (VLACH translation)
στέκ = στέκω — stands (Pontic drops final -ει)
φωσόπολι = φως — a little light (Pontic diminutive)
κεμεντζέν = κεμεντζές — the Pontic lyra (accusative)
πα = πα — also, too (Pontic)
τηρώ = τηρώ — I look, I see (Pontic)
ντο = ντο — what (Pontic)
εν = είναι — is (Pontic)
εκεκά = εκεί — over there (Pontic)
επήα = πήγα — I went (Pontic)
λαγγεύ = λαγγεύω — it leaps, jumps (Pontic)
ένι = είναι — there is (Pontic)
τραγωδί = τραγούδι — song (Pontic)
λαλία = λαλιά — voice
νου = νους — mind; σο νου μ', into my mind
ατον = αυτόν — him, it (Pontic)
καλομάνα = καλομάνα — grandmother (Pontic)
εθυμέθα = θυμάμαι — I remembered (Pontic)
ουχ = ουχ — oh! (exclamation)
γλήγορα = γρήγορα — quickly
τρέχ = τρέχει — he runs
αέτσ = έτσι — so, like this (Pontic); έτσ' κ' αέτσ', this and that
εσέν = εσένα — you (Pontic)
κι = κι (Pontic) — not = δεν; elsewhere κι = και 'and'
πίσ = πίσω — behind; από πίσ' α, after
αείκα = τέτοια — such things (Pontic)
ατά = αυτά — these (Pontic)
μάισσες = μάισσα — witch (Pontic, = μάγισσα)
μάισσα = μάισσα — witch (Pontic, = μάγισσα)
μαεύνε = μαγεύω — they bewitch (Pontic)
εμάευες = μαγεύω — you would be bewitched (Pontic)
εποίνε = ποιώ — did, would do (Pontic)""")

V_GLOSS = g("""μουλουγούσι = μολογώ — he used to tell (northern: ο → ου, final ε → ι)
δέδες = δέδες — grandfather (from Turkish dede)
γκουμπλάρ = Γκουμπλάρ — Gublar, Greek Μυρσίνη, a village near Grevena
τσουτσανός = τσουτσανός — boy (VLACH translation)
λε = λέει — he/she says
ιγώ = εγώ — I (northern: unstressed ε → ι)
πάνου = πάω — I go (northern)
κουμπσίσα = κουμπσίσα — neighbour, a woman next door (from Turkish komşu)
τήρα = τηράω — look after, watch
κουσάρια = κουσάρα — hen with chicks
κουσάρα = κουσάρα — hen with chicks
μι = με — with; me (northern: ε → ι)
πλια = πουλιά — chicks (northern drops unstressed ου)
παρ = παίρνω — (may) take
γιράκ = γεράκι — hawk
γιτουνιά = γειτονιά — neighbourhood
γιτνιά = γειτονιά — to the neighbour's
χάλιβι = χαλεύω — he wanted (northern)
παίξ = παίζω — to play
εμ = εμ — but, well (from Turkish)
αφήκ = αφήνω — (if) he leaves (northern)
α = θα — will (northern)
πουδάρ = ποδάρι — leg, foot
άδισι = δένω — he tied (northern έδεσε)
ήρσι = έρχομαι — came (northern ήρθε)
ήρθι = έρχομαι — came (northern ήρθε)
σαχίν = σαχίν — falcon, hawk (from Turkish şahin)
έφυι = φεύγω — left (northern έφυγε)
είνι = είναι — is, are
έδιρι = δέρνω — hit, beat (northern έδειρε)
τουν = τον — him
μύλου = μύλος — mill (northern ο → ου)
μύλους = μύλος — miller, the man at the mill
μυλουνάς = μυλωνάς — miller
ρα = ρε — hey (form of address)
έτσας = έτσι — so; έτσας κι έτσας, this and that
κάτσι = κάθομαι — stay (northern κάτσε)
ιδώ = εδώ — here
απόψι = απόψε — tonight
κμήσ = κοιμάμαι — sleep! (northern κοιμήσου)
φύγου = φεύγω — I leave (northern φύγω)
κμήθκι = κοιμάμαι — he slept (northern κοιμήθηκε)
ξύπνισι = ξυπνώ — he woke up (northern ξύπνησε)
βγήκι = βγαίνω — went out (northern βγήκε)
όξου = έξω — out
άφκι = αφήνω — he left (northern άφησε)
γουρούν = γουρούνι — pig
όφαϊ = τρώω — ate (northern έφαγε)
έφαϊ = τρώω — ate (northern έφαγε)
αλεύρ = αλεύρι — flour
χαραΐ = χαραυγή — dawn
βρήκι = βρίσκω — found (northern βρήκε)
ρουμνιός = Ρωμιός — a (Christian) Greek
ρουμνός = Ρωμιός — a (Christian) Greek
κρες = κλαίω — you cry (as transcribed)
σι = σε — you (northern)
πάρου = παίρνω — I take (northern πάρω)
γέντσ = γίνομαι — you become (northern)
θκο = δικό — own; θκο μ', my own
πιδί = παιδί — child
σπίτ = σπίτι — house, home
ν = την — the (northern ν' before a noun)
έβαναμι = βάζω — we put up (northern)
μπαϊράκ = μπαϊράκι — flag; here the wedding flag (from Turkish bayrak)
χιρνούσι = began — (VLACH translation)
χαρά = χαρά — joy; here the wedding
πέφτ = Πέμπτη — Thursday
πήαμ = πηγαίνω — we went
πάιναμι = πηγαίνω — we went, we took (northern)
πάιναν = πηγαίνω — they went (northern)
ταχνά = ταχιά — in the morning
ζγουρ = lamb — (VLACH translation)
τσ = της, τους — her, their (northern)
νύφς = νύφη — bride
νύφ = νύφη — bride
κιαφέτια = clothes — (VLACH translation)
έδουναν = δίνω — they gave
ψουμί = ψωμί — bread; a meal
ικεί = εκεί — there
εκάθουμασταν = κάθομαι — we sat (northern)
έτρουγαμι = τρώω — we ate (northern τρώγαμε)
χουσαβέρ = then — (VLACH translation)
γυρνούσαμι = γυρνώ — we returned
έρουμασταν = έρχομαι — we came back (northern)
σάβατου = Σάββατο — Saturday
βιουλιά = βιολιά — violins; the musicians
λαλούσαν = λαλώ — they played (music)
χόριβναν = χορεύω — they danced (northern)
ίπιναν = πίνω — they drank
ύστιρα = ύστερα — later, then
κουμβόι = group, procession — (VLACH translation)
πάρουμι = παίρνω — we take
ούλου = όλος — all
χουριό = χωριό — village
χουριά = χωριό — villages
όπιους = όποιος — whoever
ήνταν = ήταν — they were
νταβετλής = guest — invited (from Turkish davetli)
έπιρναν = παίρνω — they took
έπερναν = παίρνω — they took
πέρναν = παίρνω — they took
πέρουν = παίρνω — they take
γένουνταν = γίνομαι — happened, were done
φαγιά = φαγητό — dishes, food
έφκιαναν = φτιάχνω — they made (northern φκιάνω)
έφκιαναμι = φτιάχνω — we made (northern φκιάνω)
μπακλαβάν = μπακλαβάς — baklava
μουσακάν = μουσακάς — moussaka
τσουρβάν = soup — (from Turkish çorba)
ριζ = ρύζι — rice
κιμπάπ = κεμπάπ — kebab
πίτις = πίτα — pies
μπιρέκια = μπουρέκι — börek, filled pastry
πράσα = πράσο — leeks
νύφις = νύφη — brides
αρβανίτ = Αρβανίτης — Albanian
ίρχισαν = αρχίζω — they started
μουρσαλί = Μουρσαλί — Mursallı, the village in Turkey
έβετ = yes — (Turkish evet)""")

def clip(**k): return {x: y for x, y in k.items() if y is not None}

PONTIC = {
  "h": "Listen: Pontic today",
  "intro": "Recordings from the **Vanishing Languages and Cultural Heritage** (VLACH) archive of the Austrian Academy of Sciences, played from its YouTube channel and not stored in the app. Tap any Greek word in the subtitles to look it up.",
  "clips": [
    clip(id="pont-witches", yt="EXBGL8rICIg", el="Μάισσες", title="The witches",
      who="Ioannis Amarantidis, Oinoi (Kastoria). His grandparents came from Matsuka (Maçka) in the hills behind Trabzon. VLACH notes that his Pontic shows influence from written Modern Greek.",
      cite="Máises – The witches; performer: Ioannis Amarantidis; camera/interview/scientific advisor: Andreea Pascaru; transcription: Thede Kahl, Sotirios Rousiakis; translation: Sotirios Rousiakis; project coordinator: Thede Kahl; editor: Antonio Fichera; retrieved from www.oeaw.ac.at/VLACH, ID-number: pont1253GRV0009a.",
      listenFor="κ' for 'and' but κι for 'not'; σο for 'in the'; τηρώ 'I look'; ντο 'what'; εν 'is'; the dropped final vowel in καλύβ', βράδ'.",
      cues=CUES["witches"], gloss=W_GLOSS),
    clip(id="pont-language", yt="CoS7_c5pZyw", title="We, the Pontic Greeks, love our language",
      who="Anatoli Karipidou, who translated the Iliad and the Odyssey into Pontic, on why a language survives only if it is spoken and taught.",
      cite="We, the Pontic Greeks, love our language; performer: Anatoli Karipidou; Vanishing Languages and Cultural Heritage (VLACH), Austrian Academy of Sciences, ID-number: pont1253GRV0011a.",
      note="VLACH has not published a timed transcription of this clip, so it plays without app subtitles."),
  ],
}

NORTHERN = {
  "h": "Listen: the Vallahades of Grevena",
  "intro": "The **Vallahades** were Greek-speaking Muslims of the Grevena area in western Macedonia. In 1923 the exchange of populations sent them to Turkey; the village of **Mursallı** has been home since then to families from Gublar (today Μυρσίνη). Their Greek kept the northern vowel system: unstressed **ε → ι**, **ο → ου**, and unstressed **ι, ου** dropped (πουλιά → πλια, κοιμήσου → κμήσ'). Recordings from the VLACH archive of the Austrian Academy of Sciences, played from its YouTube channel and not stored in the app.",
  "clips": [
    clip(id="vall-suleiman", yt="m_dJ-spfq-8", el="Σιλιμάν, τα πουλιά κι μυλουνάς", title="Suleiman, the chickens and the miller",
      who="Konuk Serap, Mursallı, tells a story her grandfather from Gublar used to tell.",
      cite="Syʎimán, ta puʎá k'i milunás – Suleiman, the chickens and the miller; performer: Konuk Serap; camera/interview: Thede Kahl, Andreea Pascaru; transcription/translation: Thede Kahl, Sotirios Rousiakis; editor: Helmut Sandeck; retrieved from www.oeaw.ac.at/VLACH, ID number: mace1251TRV0002a.",
      listenFor="ιγώ, ιδώ, απόψι (ε → ι); στου μύλου, πάνου (ο → ου); έδιρι, βγήκι (final ε → ι); κμήσ', σπίτ' (lost vowels); Turkish loans σαχίν, εμ.",
      cues=CUES["suleiman"], gloss=V_GLOSS),
    clip(id="vall-wedding", yt="0ytf7T7j6kY", el="Η χαρά", title="The wedding",
      who="Azem Altay, Mursallı, on the wedding days and the food served.",
      cite="I xará – Marriage; performer: Azem Altay; camera/interview: Thede Kahl, Andreea Pascaru; transcription/translation: Thede Kahl, Sotirios Rousiakis; editor: Helmut Sandeck; retrieved from www.oeaw.ac.at/VLACH, ID number: mace1251TRV0003a.",
      listenFor="χαρά for 'wedding'; the weekdays Πέφτ' and Σάβατου; Turkish words for things of daily life (μπαϊράκ', νταβετλής, τσουρβάν, έβετ).",
      cues=CUES["marriage"]),  # shares the page gloss of the first clip
    clip(id="thrace-giannis", yt="5pwa_m3d0lE", title="Giannis and Marulio (Thracian song)",
      who="Tasoula Papavasiliou, Proskynites (Rodopi), sings a tragic love song brought from Mikro Bogialiki in North Thrace, today Malko Sharkovo in Bulgaria.",
      cite="Giannis and Marulio; performer: Tasoula Papavasiliou; Vanishing Languages and Cultural Heritage (VLACH), Austrian Academy of Sciences, ID-number: thra1248GRV0020a.",
      note="VLACH has not published a timed transcription of this clip, so it plays without app subtitles."),
    clip(id="thrace-pilgrims", yt="XGqZR9vc5c8", title="Five pilgrims journeying to the Holy Land (Thracian song)",
      who="Tasoula Papavasiliou sings a dance song from Mikro Bogialiki.",
      cite="Five pilgrims journeying to the Holy Land; performer: Tasoula Papavasiliou; Vanishing Languages and Cultural Heritage (VLACH), Austrian Academy of Sciences, ID-number: thra1248GRV0017a.",
      note="VLACH has not published a timed transcription of this clip, so it plays without app subtitles."),
  ],
}

CAPP = {
  "h": "Listen: Pharasa Greek",
  "intro": "A recording from the VLACH archive of the Austrian Academy of Sciences, played from its YouTube channel and not stored in the app.",
  "clips": [
    clip(id="capp-chicken", yt="33dbRBT0Yow", title="The French-style chicken",
      who="Varvara Konstantinidou tells, in the Pharasa variety, how a featherless-necked hen she loved was cured with oil and raki instead of going into the pot, and how the same cure later healed her own foot.",
      cite="A rníθi alafránka – The French-style chicken; performer: Varvara Konstantinidou; Vanishing Languages and Cultural Heritage (VLACH), Austrian Academy of Sciences, ID-number: capp1230GRV0006a.",
      note="VLACH has not published a timed transcription of this clip, so it plays without app subtitles."),
  ],
}

ITAL = {
  "h": "Listen: Griko of Sternatia",
  "intro": "A recording from the VLACH archive of the Austrian Academy of Sciences, played from its YouTube channel and not stored in the app.",
  "clips": [
    clip(id="griko-1567", yt="QV17Yr1ZrKs", title="In 1567",
      who="Luigia Linciano (1923–2016) of Sternatia tells an old tale of the hail of 1567 that destroyed the crops, and of the young women who asked the Virgin to calm her son's anger.",
      cite="In 1567; performer: Luigia Linciano; transcription/translation: Francesco Giannachi, Thede Kahl; Vanishing Languages and Cultural Heritage (VLACH), Austrian Academy of Sciences, ID-number: apul1237ITV0001a.",
      note="VLACH has not published a timed transcription of this clip, so it plays without app subtitles."),
  ],
}

SRC = {"label": "Vanishing Languages and Cultural Heritage (VLACH), Austrian Academy of Sciences: recordings, transcriptions and translations", "url": VL}
for page, block in (("pontic", PONTIC), ("northern", NORTHERN), ("cappadocian", CAPP), ("italiot", ITAL)):
    p = ROOT + page + ".json"; txt = open(p).read(); d = json.loads(txt)
    assert "listen" not in d, page
    block["render"] = RENDER
    nxt = "culture" if "culture" in d else "questions"
    body = json.dumps(block, ensure_ascii=False, indent=2).replace("\n", "\n  ")
    key = '\n  "' + nxt + '":'
    assert txt.count(key) == 1, page
    txt = txt.replace(key, '\n  "listen": ' + body + ',' + key)
    assert txt.rstrip().endswith("]\n}"), page
    if VL not in txt:
        end = txt.rstrip()[:-3].rstrip()
        txt = end + ",\n    " + json.dumps(SRC, ensure_ascii=False).replace('{"', '{ "').replace('"}', '" }').replace('", "', '", "') + "\n  ]\n}\n"
    json.loads(txt); open(p, "w").write(txt)
    print(page, len(block["clips"]))
