# tools/themata — thematic bilingual readers

Shelves: kathimerini (everyday life), ygeia (health); planned douleia, scheseis, nomos, eleftheros.

    python3 tools/themata/build.py <shelf> library/<shelf>     # build JSON
    python3 tools/themata/glossfill.py <shelf>                 # lookup/lint check, fills gloss.txt from other tools/*/gloss.txt
    python3 tools/themata/check_sources.py <shelf>             # every source URL resolves
    python3 tools/themata/patch_shared.py /home/user/ellinika  # wire shelves into bilingual.js, library, offline list, sw
    bash tools/themata/mkpdf.sh <shelf> Ellinika-<Name>.pdf "Ελληνικά · <Greek title>"
    python3 tools/themata/coverage.py [--exclude ...]          # which top-10k lemmas appear nowhere
