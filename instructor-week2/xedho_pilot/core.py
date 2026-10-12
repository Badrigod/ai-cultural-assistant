"""Private, source-limited pilot logic. No cloud calls or visitor identifiers."""
import json
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "xedho.json"
EVENTS = ROOT / "data" / "events.sqlite3"
ALLOWED_EVENTS = {"page_view", "language_selected", "audio_play", "question_asked"}


def load_artifact(path=DATA):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def approved_passages(record, language="en"):
    """Only reviewed passages with an explicit source reference enter retrieval."""
    if record.get("status") != "approved" or not record.get("approval", {}).get("reviewer"):
        return []
    approved_ids = {s["id"] for s in record.get("sources", []) if s.get("approved") is True and s.get("id")}
    return [p for p in record.get("passages", [])
            if p.get("approved") is True and p.get("source_id") in approved_ids
            and p.get("language") == language and p.get("text", "").strip()]


def release_ready(record):
    return (record.get("status") == "approved"
            and bool(record.get("approval", {}).get("reviewer"))
            and bool(record.get("approval", {}).get("date"))
            and record.get("image", {}).get("permission") == "confirmed"
            and record.get("inventory_row") is not None
            and all(record.get(field, "").strip() for field in
                    ("name_so", "traditional_use", "story_en", "story_so"))
            and bool(approved_passages(record, "en"))
            and bool(approved_passages(record, "so")))


def answer(question, record, language="en"):
    fallback = "Macluumaad la ansixiyey oo ku filan lama hayo." if language == "so" else "Approved information is not available for that question."
    words = lambda text: set(re.findall(r"\w+", text.lower(), flags=re.UNICODE))
    q = words(question)
    stop = {"what", "where", "when", "who", "how", "the", "is", "it", "a", "an", "of", "and", "for", "does", "was", "this", "its", "waa", "maxay", "maxaa", "xagee", "iyo", "ka", "ku", "oo", "ee"}
    q -= stop
    if not q:
        return fallback, None
    scored = [(len(q & words(p["text"])), p) for p in approved_passages(record, language)] if release_ready(record) else []
    if not scored:
        return fallback, None
    score, passage = max(scored, key=lambda item: item[0])
    if score < 1:
        return fallback, None
    # Return the approved passage verbatim: no model can add unsupported claims.
    return passage["text"], passage["source_id"]


def draft_example_answer(question, record, language="en"):
    """Local demonstration using explicitly draft inventory passages."""
    if record.get("status") != "draft":
        return answer(question, record, language)
    question_lower = question.lower()
    fallback = "Tusaalaha hordhaca ah kama jawaabi karo su'aashaas." if language == "so" else "The draft inventory does not answer that question."
    # The inventory covers only appearance, materials, and a vague use statement.
    # Restrict preview retrieval to those intents so unrelated words cannot select a passage.
    if language == "en":
        if re.search(r"\b(who|when|where|which community|origin|year|century)\b", question_lower):
            return fallback, None
        if re.search(r"\b(use|used|purpose|collect|carry|store|storing)\b", question_lower):
            intent = "use"
        elif re.search(r"\b(material|made of|made from|wood|gourd|leather|hide|shell)\b", question_lower):
            intent = "material"
        elif re.search(r"\b(look|appearance|describe|decoration|decorated)\b", question_lower):
            intent = "description"
        else:
            return fallback, None
    else:
        if re.search(r"\b(yaa|goorma|xaggee|xagee|halkee|sanadkee)\b", question_lower):
            return fallback, None
        if re.search(r"\b(isticmaal|isticmaalaa|adeegsan|ururin|qaadid|kaydin)\b", question_lower):
            intent = "use"
        elif re.search(r"\b(agab|samaysan|alwaax|maqaar|cowrie)\b", question_lower):
            intent = "material"
        elif re.search(r"\b(tilmaam|muuqaal|qurxiyey)\b", question_lower):
            intent = "description"
        else:
            return fallback, None
    terms = set(re.findall(r"\w+", question.lower(), flags=re.UNICODE))
    terms -= {"what", "where", "how", "is", "are", "it", "the", "a", "of", "for", "and", "does", "xedho", "maxaa", "waa", "loo", "iyo", "ka", "ku"}
    passages = [p for p in record.get("passages", []) if p.get("language") == language and p.get("preview_only") is True and p.get("intent") == intent]
    matches = [(len(terms & set(re.findall(r"\w+", (p["text"] + " " + p.get("keywords", "")).lower(), flags=re.UNICODE))), p) for p in passages]
    if not matches or max(matches, key=lambda pair: pair[0])[0] == 0:
        return fallback, None
    passage = max(matches, key=lambda pair: pair[0])[1]
    return passage["text"], passage["source_id"]


def log_event(event, artifact_id="KHH-005", path=EVENTS):
    if event not in ALLOWED_EVENTS:
        raise ValueError("Unknown event type")
    with sqlite3.connect(path) as db:
        db.execute("CREATE TABLE IF NOT EXISTS events (at TEXT DEFAULT CURRENT_TIMESTAMP, artifact_id TEXT, event TEXT)")
        db.execute("INSERT INTO events (artifact_id, event) VALUES (?, ?)", (artifact_id, event))


def event_counts(path=EVENTS):
    if not Path(path).exists():
        return []
    with sqlite3.connect(path) as db:
        return db.execute("SELECT artifact_id, event, COUNT(*) FROM events GROUP BY artifact_id, event ORDER BY artifact_id, event").fetchall()
