from __future__ import annotations

from .config import AUDIT_DIR
from .utils import utc_now, write_jsonl

AUDIT_FILE = AUDIT_DIR / "audit_events.jsonl"


def log_event(event_type: str, payload: dict) -> None:
    row = {"event_ts": utc_now(), "event_type": event_type, **payload}
    write_jsonl(AUDIT_FILE, [row], append=True)
