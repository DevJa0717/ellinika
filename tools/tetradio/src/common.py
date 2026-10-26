"""Helpers for the writing-workbook sources (one module per part, each defines ITEMS)."""
import textwrap

def P(s):
    """Split a triple-quoted block into paragraphs on blank lines; single newlines stay (letter headers, sign-offs)."""
    s = textwrap.dedent(s).strip("\n")
    return [p.strip() for p in s.split("\n\n") if p.strip()]

def ph(*rows):
    """Phrase rows: ("Greek", "English") or ("Greek", "English", "register")."""
    return [dict(el=r[0], en=r[1], **({"reg": r[2]} if len(r) > 2 else {})) for r in rows]

def q(text, options, answer, why=""):
    assert answer in options, (text, answer)
    return dict(q=text, options=options, answer=answer, **({"why": why} if why else {}))

def ex(*pairs):
    return [dict(el=a, en=b) for a, b in pairs]
