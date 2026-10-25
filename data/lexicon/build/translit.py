# Rule-based transliteration in the lexicon's scheme (see brief_new.md).
import unicodedata
VOICELESS = set('θκξπστφχψ')
SINGLE = dict(zip('αβγδεζηθικλμνξοπρσςτυφχψω', ['a','v','g','d','e','z','i','th','i','k','l','m','n','ks','o','p','r','s','s','t','i','f','ch','ps','o']))
def base(c): return unicodedata.normalize('NFD', c)[0]
def translit(word):
    out = []
    for token in word.split(' '):
        w = token.lower(); n = len(w); i = 0; res = ''
        b = [base(c) for c in w]
        dia = [('̈' in unicodedata.normalize('NFD', c)) for c in w]
        acc = [('\u0301' in unicodedata.normalize('NFD', c)) for c in w]
        while i < n:
            c, nx = b[i], (b[i+1] if i + 1 < n else '')
            two = c + nx; init = (i == 0)
            if nx and not dia[i+1] and not acc[i]:
                if two == 'ου': res += 'ou'; i += 2; continue
                if two == 'αι': res += 'e'; i += 2; continue
                if two in ('ει', 'οι', 'υι'): res += 'i'; i += 2; continue
                if two in ('αυ', 'ευ', 'ηυ'):
                    nn = b[i+2] if i + 2 < n else ''
                    res += {'α':'a','ε':'e','η':'i'}[c] + ('f' if (not nn or nn in VOICELESS) else 'v'); i += 2; continue
            if two == 'μπ': res += 'b' if init else ('mp' if (i + 2 < n and b[i+2] not in 'αεηιουω') else 'mb'); i += 2; continue
            if two == 'ντ': res += 'd' if init else 'nd'; i += 2; continue
            if two == 'γκ': res += 'g' if init else 'ng'; i += 2; continue
            if two == 'γγ': res += 'ng'; i += 2; continue
            if two == 'γχ': res += 'nch'; i += 2; continue
            if two == 'γξ': res += 'nks'; i += 2; continue
            res += SINGLE.get(c, c); i += 1
        out.append(res[:1].upper() + res[1:] if token[:1].isupper() else res)
    return ' '.join(out)
