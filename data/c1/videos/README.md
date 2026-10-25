# C1 Greek videos

Retrieved 2026-10-18. This is for personal, non-commercial study only.

## Files
- **videos-c1.json**: 22 C1 videos in the app schema. All are TEDx talks given in Greek by native speakers. Each one is embedded from YouTube (`embed.kind = "youtube"`). The file only stores the subtitle cues and never the video. Each video has a 4–6.5 minute excerpt set by `start`/`end`, with 27–45 cues per video and 831 cues in total. Every cue has `el` and `en`. Each video also has 18–25 glossed C1 words. Every video has one `lessons` value, and no lesson has more than 2 videos.
- **candidates.json**: 11 promising items that were not built, each with the reason. They are mostly non-TED sources with no usable timed Greek subtitles. The four Amara-ready candidates listed earlier (Papadatou, Georgakopoulos, Papachelas, Spinellis) have now been built.
- **amara-greek-tedx-index.json**: an index of 277 Greek-audio TEDx talks that have published human Greek subtitles on Amara. It is a pool for future videos.
- **sources.json**: the source, licence and retrieval date for every item.

## Videos
| id | speaker | topic | excerpt | lesson |
|---|---|---|---|---|
| c1-ramfos | Stelios Ramfos | philosophy, Greek political culture | 329–654 s | c1-read-philosophy |
| c1-zei | Alki Zei | memoir, occupation and resistance | 348–623 s | c1-read-history |
| c1-kottaridi | Angeliki Kottaridi | archaeology, memory, Aigai | 19–288 s | c1-ancient-sayings |
| c1-triantafyllou | Soti Triantafyllou | ιθαγένεια vs υπηκοότητα, etymology | 15–374 s | c1-learned-nouns |
| c1-tsalikoglou | Fotini Tsalikoglou | psychology, loss and creativity | 344–613 s | c1-hedging |
| c1-nanopoulos | Dimitri Nanopoulos | cosmology | 227–481 s | c1-read-science-tech |
| c1-tsoukalis | Loukas Tsoukalis | European integration, the euro | 58–362 s | c1-read-society |
| c1-agathos | Michalis Agathos | gravitational waves | 76–387 s | c1-read-science-tech |
| c1-kouvelas | Elias Kouvelas | neuroscience, free will | 217–569 s | c1-nominal-style |
| c1-ioannidis | John Ioannidis | meritocracy, brain drain | 363–626 s | c1-emphasis |
| c1-politicswords | Giannis Vlastaris | political doublespeak | 12–275 s | c1-register |
| c1-efthymiou | Maria Efthymiou | history of the Greek language | 542–817 s | c1-language-question |
| c1-papadatou | Danai Papadatou | talking to children about death | 220–539 s | c1-connectors |
| c1-georgakopoulos | Thodoris Georgakopoulos | journalism, death of print media | 92–381 s | c1-idioms-1 |
| c1-papachelas | Alexis Papachelas | public life, conspiracy theories | 86–392 s | c1-read-press |
| c1-spinellis | Diomidis Spinellis | public administration, meritocracy, IT | 6–326 s | c1-idioms-2 |
| c1-sotiropoulos | Vasilis Sotiropoulos | law vs statutes, self-help, Cretan mediation | 14–400 s | c1-read-law |
| c1-doxiadis | Aristos Doxiadis | economics, tradable sectors, small business | 0–348 s | c1-collocations |
| c1-dragona | Thalia Dragona | education reform, Finland, critical thinking | 280–662 s | c1-read-society |
| c1-pittara | Melpo Pittara | medicine, rare genetic disease, chronic pain | 435–709 s | c1-idioms-1 |
| c1-stergiopoulos | Georgios Stergiopoulos | aesthetics, beauty in art and science | 203–513 s | c1-read-philosophy |
| c1-vitos | Michalis Vitos | environment, forest law, indigenous mapping tech | 14–396 s | c1-read-law |

## Method and notes
- **Greek cues.** These are human subtitles from TED's Open Translation Project, published on Amara (`amara.org/api/videos/<id>/languages/el/subtitles/?format=json`) and tied to the same YouTube video. Times are seconds on the video's own timeline. `captions` is `"human"` for every video.
- **Cleaning.** Subtitle fragments were merged into sentence-sized cues, so a few cues are 10–17 s long. Text was normalised to NFC and Latin look-alike letters inside Greek words were fixed. A few subtitle typos were corrected, for example `αρνεμήνευτο`→`ανερμήνευτο`, `παραξηγηθούμε`→`παρεξηγηθούμε`, `συνομίληκούς`→`συνομηλίκους`, `ένοιωθα`→`ένιωθα`, and Latin `To`/`to`→`Το`/`το`. Brand and technical names (Sapelli, PISA, LZTR1, DNA) stay in Latin script. Stage directions such as (Γέλια) and (Χειροκρότημα) were kept. Polytonic Homeric quotations in c1-kottaridi (e.g. «ἵνα πάγχυ λαθοίατο πατρίδος αἴης») are genuinely polytonic and were kept as they are.
- **Speakers.** c1-pittara is a Greek Cypriot speaking standard Greek (TEDxNicosiaSalon). The c1-dragona excerpt begins after a dubbed clip about Finland, so every line is the speaker's own.
- **English lines.** These were written by the agent from the Greek and are not TED's translations.
- **Availability.** Every video returned HTTP 200 from YouTube oEmbed, so each one exists and can be embedded.
- **Licence.** TED/TEDx talks are CC BY-NC-ND 4.0 under TED's usage policy. The videos are embedded from YouTube and the subtitles are credited to TED OTP volunteers on Amara.
- **Limitation.** YouTube watch pages and caption tracks returned a bot-check ("sign in to confirm you're not a bot") from this environment, so YouTube's own caption tracks were not used. Non-TED sources were not captioned: ERT documentaries, Babiniotis interviews and Alexiadou's talk are listed in candidates.json. No access control was bypassed.
- **No ERT or university lectures.** opencourses/uniflix lectures have no timed subtitles, and TED.com hosts no talks with Greek audio.
