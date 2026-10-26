"""Shared helpers for the word-family (#families) and confusables (#confusables) sources.

Family chapters are written as Python dicts in fam_*.py; G() builds one family group from a block of
"greek|english" lines. Confusable chapters (conf_*.py) use P() for one pair or set of words that learners
mix up. build.py turns both into library/families/*.json and library/confusables/*.json.
"""


def members(block):
    out = []
    for line in block.strip().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        el, en = [x.strip() for x in line.split("|", 1)]
        out.append({"el": el, "en": en})
    return out


def G(key, meaning, m, note=None, ex=None, el=None, drill=True):
    """One family: the affix or root (key), what it means, its members, an optional note and examples.
    el: an optional Greek label (e.g. the verb the root comes from). drill=False keeps members out of drills."""
    g = {"key": key, "meaning": meaning, "members": members(m)}
    if el:
        g["el"] = el
    if note:
        g["note"] = note
    if ex:
        g["ex"] = [{"el": a, "en": b} for a, b in ex]
    if not drill:
        g["nodrill"] = True
    return g


def W(el, en):
    return {"el": el, "en": en}


def P(words, note, ex=(), gaps=(), trap=None, level=None):
    """One confusable set.
    words: list of (greek, english) the learner must tell apart; note: markdown explanation;
    ex: contrastive examples as (greek, english); gaps: (sentence with ___, answer, [distractors], english);
    trap: one-line warning shown as the headline (e.g. 'sympathetic ≠ συμπαθητικός')."""
    p = {"words": [W(a, b) for a, b in words], "note": note,
         "ex": [{"el": a, "en": b} for a, b in ex],
         "gaps": [{"s": s, "a": a, "o": list(o), "en": en} for s, a, o, en in gaps]}
    if trap:
        p["trap"] = trap
    if level:
        p["level"] = level
    return p
