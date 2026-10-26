# Helpers for the history reader sources: each era file builds chapters in the shared bilingual format.
def P(el, en, cite=()):
    return {"el": el, "en": en, "cite": list(cite)}
def S(id, el, en, paras):
    return {"id": id, "el": el, "en": en, "paras": paras}
def G(level, title, el, en, examples):
    return {"level": level, "title": title, "el": el, "en": en, "examples": [{"el": a, "en": b} for a, b in examples]}
def T(el, en, def_el, def_en):
    return {"el": el, "en": en, "def_el": def_el, "def_en": def_en}
def Q(q, options, answer, why=""):
    return {"q": q, "options": options, "answer": options[answer], "why": why}
def SRC(text, url=None):
    d = {"text": text}
    if url: d["url"] = url
    return d
