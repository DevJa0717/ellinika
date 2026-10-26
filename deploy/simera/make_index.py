"""Build library/simera/index.json from BATCHES.md and the chapter files present."""
import re, json, os
B = open(os.path.join(os.path.dirname(__file__), "BATCHES.md")).read()
LIB = "/mnt/project-files/app/library/simera"
parts, items = [], []
INTRO = {
 "geo": ("Η χώρα: βουνά, θάλασσες, κλίμα, άνθρωποι.", "The land: mountains, seas, climate and where people live."),
 "cul": ("Γλώσσα, μουσική, οθόνη, τραπέζι και αθλητισμός.", "Language, music, screen and page, food, sport."),
 "soc": ("Τα μεγάλα κοινωνικά ζητήματα μετά την κρίση.", "The big social questions after the debt crisis."),
 "pol": ("Πώς ζουν οι Έλληνες την πολιτική κάθε μέρα. Για τους θεσμούς, δείτε το «Πολίτευμα».", "How Greeks live politics day to day. For institutions see the polity reader."),
 "rel": ("Ορθοδοξία, μειονότητες και πίστη στην καθημερινή ζωή.", "Orthodoxy, minorities and faith in daily life."),
 "hr": ("Δικαιώματα, μετανάστευση, ισότητα και ελευθερία του Τύπου.", "Rights in practice, migration, equality, press freedom."),
 "glo": ("Η Ελλάδα μέσα στον κόσμο: Ευρώπη, τουρισμός, θάλασσα, ομογένεια, ενέργεια.", "Greece in the world: Europe, tourism, shipping, diaspora, energy."),
 "portrait": ("Ένα πορτρέτο της ελληνικής κοινωνίας σήμερα.", "A portrait of Greek society today."),
 "reg": ("Οι δεκατρείς περιφέρειες και το Άγιον Όρος, μία προς μία.", "The thirteen regions and Mount Athos, one by one."),
}
for m in re.finditer(r"^## (\w+) · (.+?) · (.+?) \(", B, re.M):
    pid, el, en = m.groups()
    parts.append({"id": pid, "el": el, "en": en, "intro_el": INTRO[pid][0], "intro_en": INTRO[pid][1]})
    sect = B[m.end():].split("\n## ")[0]
    for c in re.finditer(r"^- ([\w-]+) · (.+?) · (.+?) · (B1|B2|C1)", sect, re.M):
        cid, cel, cen, lvl = c.groups()
        f = f"{LIB}/{cid}.json"
        if not os.path.exists(f): continue
        d = json.load(open(f))
        items.append({"id": cid, "file": f"{cid}.json", "el": d.get("el", cel), "title": d.get("title", cen), "level": d.get("level", lvl), "part": pid, "dates": d.get("dates", "2026")})
idx = {"kind": "bilingual", "id": "simera", "el": "Η Ελλάδα σήμερα", "title": "Greece today",
  "intro_el": "Ένα δίγλωσσο ανάγνωσμα για τη σύγχρονη Ελλάδα: γεωγραφία, πολιτισμός, κοινωνία, πολιτική, θρησκεία, ανθρώπινα δικαιώματα, παγκοσμιοποίηση και οι περιφέρειες της χώρας. Τα ελληνικά ξεκινούν από το επίπεδο Β2 και γίνονται σταδιακά πιο απαιτητικά.",
  "intro_en": "A bilingual reader on contemporary Greece: geography, culture, society, politics, religion, human rights, globalisation, a portrait of Greek society, and every region. The Greek starts at B2 and grows gradually harder; the English carries more detail. Every fact is cited, with sources at the end of each chapter.",
  "parts": parts, "items": items}
json.dump(idx, open(f"{LIB}/index.json", "w"), ensure_ascii=False, indent=1)
print(len(parts), "parts,", len(items), "items")
