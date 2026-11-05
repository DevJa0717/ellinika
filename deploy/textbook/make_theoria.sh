#!/bin/sh
# Rebuild the grammar outline PDF (downloads/textbook/Ellinika-Grammar-outline.pdf) from library/theoria/*.json.
# Usage: sh deploy/textbook/make_theoria.sh   (needs Playwright/Chromium and pikepdf)
set -e
HERE=$(cd "$(dirname "$0")" && pwd); ROOT="$HERE/../.."; B=$(mktemp -d)
cp -r "$HERE/fonts" "$B/"
python3 "$HERE/build_theoria.py" --out "$B"
node "$HERE/render_theoria.js" "$B" "$ROOT/downloads/textbook"
node "$HERE/render_cover.js" "$B/Grammar outline.html" "$B/cover.pdf"
PDF="$ROOT/downloads/textbook/Ellinika-Grammar-outline.pdf"
python3 "$HERE/swap_cover.py" "$PDF" "$B/cover.pdf"
python3 "$HERE/compress.py" "$PDF" "$B/c.pdf" "Ελληνικά · Γραμματική σε θεωρία και ασκήσεις" && mv "$B/c.pdf" "$PDF"
rm -rf "$B"; ls -la "$PDF"
