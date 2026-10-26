"""Merge photo credits and diagrams.json into images.json (run diagrams.py first)."""
import json
LOC = "Library of Congress, Prints and Photographs Division"
MET = "The Metropolitan Museum of Art, Open Access"
P = {
 "syntagma-1975": ("syntagma-1901.jpg", "Η πλατεία Συντάγματος και τα παλιά ανάκτορα, σήμερα η Βουλή, το 1901.", "Syntagma (Constitution) Square and the old royal palace, now Parliament, in 1901.", f"H. C. White Co., 1901 · {LOC}", "Public domain (no known restrictions)", "https://www.loc.gov/item/2003681446/"),
 "vouli": ("vouli-palace.jpg", "Εύζωνες μπροστά στα παλιά ανάκτορα, όπου συνεδριάζει η Βουλή από το 1935 (αρχές 20ού αι.).", "Evzone guards before the old royal palace, home of Parliament since 1935 (early 20th century).", f"Keystone View Company · {LOC}", "Public domain (no known restrictions)", "https://www.loc.gov/item/2020680584/"),
 "dikastiria": ("dikaiosyni-ammannati.jpg", "Η Δικαιοσύνη, χάλκινο αγαλματίδιο του Μπαρτολομέο Αμανάτι (16ος αι.).", "Justice, bronze statuette after Bartolomeo Ammannati (16th century).", f"Bartolomeo Ammannati · {MET}", "CC0", "https://www.metmuseum.org/art/collection/search/197057"),
 "koinonia-politon": ("ethniki-vivliothiki.jpg", "Η Εθνική Βιβλιοθήκη στην οδό Πανεπιστημίου, χτισμένη με δωρεά των αδελφών Βαλλιάνου (αρχές 20ού αι.).", "The National Library on Panepistimiou Street, built with a gift from the Vallianos brothers (early 20th century; catalogued as “The University of Athens”).", f"Keystone View Company · {LOC}", "Public domain (no known restrictions)", "https://www.loc.gov/item/2020680596/"),
 "pelateiakes": ("diafthora-alligoria.jpg", "Αλληγορία για τη Δικαιοσύνη και τις παγίδες της διαφθοράς (περ. 1590–1630).", "Allegory on Justice and the Pitfalls of Corruption (c. 1590–1630).", f"Lambert Cornelisz · {MET}", "CC0", "https://www.metmuseum.org/art/collection/search/837725"),
 "ekklisia-kratos": ("tzafouris.jpg", "Ο Χριστός ελκόμενος, εικόνα του Κρητικού ζωγράφου Νικόλαου Τζαφούρη (τέλη 15ου αι.).", "Christ Bearing the Cross, icon by the Cretan painter Nikolaos Tzafouris (late 15th century).", f"Nikolaos Tzafouris · {MET}", "CC0", "https://www.metmuseum.org/art/collection/search/437855"),
 "europi": ("tetradrachmo.jpg", "Αθηναϊκό τετράδραχμο με την κουκουβάγια (περ. 440–404 π.Χ.)· το ίδιο σχέδιο έχει το ελληνικό κέρμα του ενός ευρώ.", "Athenian silver tetradrachm with the owl (c. 440–404 BC); the Greek one-euro coin carries the same design.", MET, "CC0", "https://www.metmuseum.org/art/collection/search/330160"),
 "exoteriki": ("chartis-ellados.jpg", "Χάρτης της Ελλάδας από τη Ρώμη του 16ου αιώνα.", "Map of Greece, from the Speculum Romanae Magnificentiae (mid-16th century).", f"Sebastiano di Re · {MET}", "CC0", "https://www.metmuseum.org/art/collection/search/403169"),
 "empistosyni": ("diogenis.jpg", "Ο Διογένης με το φανάρι του, «ψάχνοντας άνθρωπο» (χαρακτικό του 18ου αι. από έργο του Ριμπέρα).", "Diogenes with his lantern, “looking for an honest man” (18th-century print after Ribera).", f"after Jusepe de Ribera · {MET}", "CC0", "https://www.metmuseum.org/art/collection/search/650907"),
 "mnimi": ("diadilosi-1897.jpg", "Διαδήλωση μπροστά στα ανάκτορα μετά την ήττα στον πόλεμο του 1897.", "Demonstration before the royal palace after the Greek army's defeat in the war of 1897.", f"Underwood & Underwood, 1898 · {LOC}", "Public domain (no known restrictions)", "https://www.loc.gov/item/2003681462/"),
}
out = {k: {"file": "img/politeia/" + f, "caption": c, "caption_en": ce, "credit": cr, "license": li, "source": so} for k, (f, c, ce, cr, li, so) in P.items()}
out.update(json.load(open("/mnt/project-files/tools/politeia/diagrams.json", encoding="utf-8")))
json.dump(out, open("/mnt/project-files/tools/politeia/images.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "images")
