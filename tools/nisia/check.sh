#!/bin/sh
# Rebuild a reader and check every chapter: sh check.sh [src_dir]   (default tools/nisia)
D=${1:-/mnt/project-files/tools/nisia}
python3 /mnt/project-files/tools/nisia/build.py "$D" || exit 1
SHELF=$(cd "$D" && python3 -c "import meta; print(meta.SHELF)")
LANG=C.UTF-8 node /mnt/project-files/tools/philosophers/check.js $(ls /mnt/project-files/app/library/$SHELF/*.json | grep -v index.json)
