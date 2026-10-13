from __future__ import annotations

import pandas as pd

from .audit import log_event
from .config import ALLOWED_SENSITIVITY_LEVELS, GOLD_DIR, SILVER_DIR
from .utils import utc_now

SILVER_FILE = SILVER_DIR / "silver_chunks.csv"
GOLD_FILE = GOLD_DIR / "gold_knowledge_base.csv"
QUALITY_FILE = GOLD_DIR / "quality_report.csv"


def evaluate_quality(silver: pd.DataFrame) -> pd.DataFrame:
    results = []
    def add(rule_id, severity, passed, failed_count, description):
        results.append({
            "rule_id": rule_id,
            "severity": severity,
            "passed": bool(passed),
            "failed_count": int(failed_count),
            "description": description,
            "evaluated_at": utc_now(),
        })
    add("DOC_NOT_EMPTY", "CRITICAL", silver["content"].fillna("").str.len().gt(0).all(), silver["content"].fillna("").str.len().le(0).sum(), "Chunk content cannot be empty")
    add("CONTENT_HASH_PRESENT", "CRITICAL", silver["content_hash"].fillna("").str.len().gt(0).all(), silver["content_hash"].fillna("").str.len().le(0).sum(), "Every chunk must have content hash")
    add("CHUNK_MIN_SIZE", "MEDIUM", silver["chunk_size"].ge(8).all(), silver["chunk_size"].lt(8).sum(), "Chunks should have at least 8 words")
    add("NO_DUPLICATE_CHUNK", "CRITICAL", (~silver["is_duplicate"].astype(bool)).all(), silver["is_duplicate"].astype(bool).sum(), "Duplicate chunks cannot be published")
    add("VALID_SENSITIVITY_LEVEL", "CRITICAL", silver["sensitivity_level"].isin(ALLOWED_SENSITIVITY_LEVELS).all(), (~silver["sensitivity_level"].isin(ALLOWED_SENSITIVITY_LEVELS)).sum(), "Sensitivity level must be valid")
    add("SOURCE_METADATA_PRESENT", "MEDIUM", silver[["source_file", "domain", "version"]].notna().all().all(), silver[["source_file", "domain", "version"]].isna().any(axis=1).sum(), "Source metadata must be present")
    return pd.DataFrame(results)


def publish_gold(silver_file=SILVER_FILE, gold_file=GOLD_FILE, quality_file=QUALITY_FILE) -> tuple[pd.DataFrame, pd.DataFrame]:
    silver = pd.read_csv(silver_file)
    quality = evaluate_quality(silver)
    gold = silver[(~silver["is_duplicate"].astype(bool)) & silver["content"].fillna("").str.len().gt(0)].copy()
    gold["is_active"] = True
    gold["published_at"] = utc_now()
    gold_file.parent.mkdir(parents=True, exist_ok=True)
    gold.to_csv(gold_file, index=False)
    quality.to_csv(quality_file, index=False)
    log_event("GOLD_PUBLISH", {"records": len(gold), "quality_rules": len(quality), "output": str(gold_file)})
    return gold, quality
