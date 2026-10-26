"""Greek-only cover text shared by the companion-volume builders (Devon, 2026-10-26: covers entirely in Greek)."""
import datetime, os

MONTHS = ["Ιανουαρίου", "Φεβρουαρίου", "Μαρτίου", "Απριλίου", "Μαΐου", "Ιουνίου",
          "Ιουλίου", "Αυγούστου", "Σεπτεμβρίου", "Οκτωβρίου", "Νοεμβρίου", "Δεκεμβρίου"]
# CEFR levels as the Greek certificate names them (Γ1, not C1)
LEVEL_EL = {"A1": "Α1", "A2": "Α2", "B1": "Β1", "B2": "Β2", "C1": "Γ1", "C2": "Γ2"}

def el_date(d=None):
    """'25 Οκτωβρίου 2026'. COVER_DATE=YYYY-MM-DD overrides today (to keep a volume's original date)."""
    d = d or (datetime.date.fromisoformat(os.environ["COVER_DATE"]) if os.environ.get("COVER_DATE") else datetime.date.today())
    return f"{d.day} {MONTHS[d.month - 1]} {d.year}"

def el_level(s):
    for k, v in LEVEL_EL.items(): s = s.replace(k, v)
    return s
