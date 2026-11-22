#!/usr/bin/env python3
"""Build Σιγανή φωτιά (Greek edition of "Fuoco Lento"): self-contained HTML + PDF.
Usage: python3 build.py   (needs weasyprint)
Output: ../../downloads/textbook/Ellinika-Sigani-fotia.html and .pdf
"""
import base64, os, sys, unicodedata, html as H
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import content as C
OUT = os.path.join(HERE, '..', '..', 'downloads', 'textbook')

def up(s):
    """Greek uppercase without tonos (keeps dialytika), as Greek typography wants."""
    out = []
    for ch in unicodedata.normalize('NFD', s.upper()):
        if ch in ('́', '̀', '͂'):
            continue
        out.append(ch)
    return unicodedata.normalize('NFC', ''.join(out))

def img(name, embed):
    if not embed:
        return 'file://' + os.path.join(HERE, 'img', name)
    return 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(HERE, 'img', name), 'rb').read()).decode()

def esc(s):
    return H.escape(s, quote=True)

def story(s, embed, lead=False):
    lvcls = 'lv-c1' if s['level'] == 'c1' else 'lv-b1'
    o = [f'<article class="scheda{" lead" if lead else ""}">',
         '<header class="scheda-head">',
         f'<span class="eyebrow">{up(s["eyebrow"])}</span>',
         f'<span class="level {lvcls}"><span class="dot"></span>{up(C.LEVELS[s["level"]])}</span>',
         '</header>', f'<h2>{s["title"]}</h2>']
    if s.get('pre'):
        o.append(f'<div class="pre"><span class="pre-label">{up("Πριν διαβάσεις")}</span><p lang="en">{esc(s["pre"])}</p></div>')
    for f, alt in s['imgs']:
        o.append(f'<figure class="panel"><img loading="lazy" src="{img(f, embed)}" alt="{esc(alt)}"></figure>')
    o.append('<div class="prose">' + ''.join(f'<p>{p}</p>' for p in s['prose']) + '</div>')
    lex = ' · '.join(f'<span class="g">{esc(g)}</span> <i lang="en">({esc(e)})</i>' for g, e in s['lex'])
    gram = ''.join(f'<li>{g}</li>' for g in s['gram'])
    o.append('<div class="apparatus">'
             f'<div class="app-col"><span class="app-label">{up("Βασικό λεξιλόγιο")}</span><p class="lexl">{lex}</p></div>'
             f'<div class="app-col"><span class="app-label">{up("Γραμματική")}</span><ul>{gram}</ul></div>'
             '</div></article>')
    return '\n'.join(o)

def fonts(local):
    if not local:
        return ('<link rel="preconnect" href="https://fonts.googleapis.com">'
                '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
                '<link href="https://fonts.googleapis.com/css2?family=Literata:ital,opsz,wght@0,7..72,400;0,7..72,500;0,7..72,600;0,7..72,700;1,7..72,400;1,7..72,600&family=Commissioner:wght@500;600;700&display=swap" rel="stylesheet">')
    faces = []
    for fn in sorted(os.listdir(os.path.join(HERE, 'fonts'))):
        fam, rest = fn[:-4].split('-')
        if fam not in ('Literata', 'Commissioner'):
            continue
        it = rest.endswith('i'); w = rest.rstrip('i')
        faces.append(f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:{"italic" if it else "normal"};'
                     f'src:url("file://{os.path.join(HERE, "fonts", fn)}");}}')
    return '<style>' + ''.join(faces) + '</style>'

def page(embed, local_fonts):
    css = open(os.path.join(HERE, 'screen.css')).read()
    pcss = open(os.path.join(HERE, 'print.css')).read()
    o = ['<!DOCTYPE html>', '<html lang="el">', '<head>', '<meta charset="utf-8">',
         '<meta name="viewport" content="width=device-width, initial-scale=1">',
         f'<title>{C.TITLE}</title>', fonts(local_fonts), f'<style>{css}</style>', f'<style>{pcss}</style>',
         '</head>', '<body>', '<div class="wrap">',
         '<header class="masthead">', f'<div class="collana">{up(C.SERIES)}</div>',
         '<h1>Σιγανή<br>φωτιά</h1>', f'<p class="tagline">{C.TAGLINE}</p>', f'<div class="meta-row">{C.META}</div>',
         f'<figure class="cover"><img src="{img(C.COVER[0], embed)}" alt="{esc(C.COVER[1])}"></figure>',
         f'<div class="edition">{C.EDITION}</div>', '</header>', '<hr class="ember">',
         '<section class="front">', f'<h2>{up("Για ποιον είναι αυτό το βιβλίο")}</h2>']
    o += [f'<p>{p}</p>' for p in C.FRONT]
    o.append(f'<div class="legend"><span class="item"><span class="dot d-c1"></span>{C.LEVELS["c1"]}</span>'
             f'<span class="item"><span class="dot d-b1"></span>{C.LEVELS["b1"]}</span></div></section>')
    o.append(story(C.LEAD, embed, lead=True))
    o.append('<hr class="ember">')
    o += [story(s, embed) for s in C.STORIES]
    f, alt, cap = C.CLOSING
    o.append(f'<figure class="closing"><img src="{img(f, embed)}" alt="{esc(alt)}"><figcaption>{cap}</figcaption></figure>')
    o.append('<hr class="ember">')
    o.append(f'<section class="riflettere"><h2>{up("Για σκέψη")}</h2><p>{C.REFLECT}</p></section>')
    o.append(f'<section class="appendix"><h2>{C.APPENDIX_TITLE}</h2><p class="sub">{C.APPENDIX_SUB}</p><div class="lex-grid">')
    for h, rows in C.APPENDIX:
        trs = ''.join(f'<tr><td class="gr">{esc(g)}</td><td class="en" lang="en">{esc(e)}</td></tr>' for g, e in rows)
        o.append(f'<div class="lex-block"><h3>{up(h)}</h3><table class="lex"><thead><tr><th>Ελληνικά</th><th>English</th></tr></thead><tbody>{trs}</tbody></table></div>')
    o.append('</div></section>')
    o.append('<div class="colophon"><div class="md-mark">Μ × Δ</div><div class="pride-rule"></div>'
             + ''.join(f'<p>{p}</p>' for p in C.COLOPHON) + '</div>')
    o += ['</div>', '</body>', '</html>']
    return '\n'.join(o)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    hp = os.path.join(OUT, 'Ellinika-Sigani-fotia.html')
    open(hp, 'w').write(page(embed=True, local_fonts=False))
    print('wrote', hp)
    from weasyprint import HTML
    pp = os.path.join(OUT, 'Ellinika-Sigani-fotia.pdf')
    HTML(string=page(embed=False, local_fonts=True), base_url=HERE).write_pdf(pp)
    print('wrote', pp)
