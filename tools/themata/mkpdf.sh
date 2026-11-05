set -e
S=$1; OUT=$2; TITLE=$3
cd /home/user/ellinika/deploy/textbook
B=/tmp/claude-0/pdf/$S; rm -rf $B; mkdir -p $B
python3 build_bilingual.py --shelf $S --app /home/user/ellinika --out $B >/dev/null
node render_pdf.js $B $B $S >/dev/null
node render_cover.js $B/$S.html $B/c.pdf >/dev/null
python3 swap_cover.py $B/Ellinika-$S-textbook.pdf $B/c.pdf >/dev/null
python3 compress.py $B/Ellinika-$S-textbook.pdf ../../downloads/textbook/$OUT "$TITLE"
