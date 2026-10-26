"""Shorthand for writing a digest issue in Python (the scheduled task may also write the JSON by hand).
P(el, en) paragraph, G(el, en) glossary entry, Q(question, options, index of the right option, why in English).
story(...) returns one story dict in the format of deploy/news/README.md."""
def P(el, en): return {"el": el, "en": en}
def G(el, en): return {"el": el, "en": en}
def Q(q, options, right, why): return {"q": q, "options": options, "answer": options[right], "why": why}
def L(el, title, paras, glossary, questions): return {"el": el, "title": title, "paras": paras, "glossary": glossary, "questions": questions}
def story(id, section, sources, B1, B2, C1, grammar=None, vocab=None):
    s = {"id": id, "section": section, "el": B2["el"], "title": B2["title"], "levels": {"B1": B1, "B2": B2, "C1": C1}, "sources": sources}
    if grammar: s["grammar"] = grammar
    if vocab: s["vocab"] = vocab
    return s
def S(name, url, date): return {"name": name, "url": url, "date": date}
def GR(level, title, en, examples): return {"level": level, "title": title, "en": en, "examples": [{"el": a, "en": b} for a, b in examples]}
