from __future__ import annotations

import pandas as pd

from .audit import log_event
from .config import BRONZE_DIR, SILVER_DIR
from .utils import normalize_text, sha256_text, utc_now

BRONZE_FILE = BRONZE_DIR / "bronze_documents.csv"
SILVER_FILE = SILVER_DIR / "silver_chunks.csv"


def chunk_text(text: str, max_words: int = 85, overlap: int = 15) -> list[str]:
    words = normalize_text(text).split()
    if not words:
        return []
    chunks = []
    step = max(max_words - overlap, 1)
    for start in range(0, len(words), step):
        part = words[start:start + max_words]
        if part:
            chunks.append(" ".join(part))
        if start + max_words >= len(words):
            break
    return chunks


def build_silver_chunks(bronze_file=BRONZE_FILE, output_file=SILVER_FILE) -> pd.DataFrame:
    bronze = pd.read_csv(bronze_file)
    rows = []
    for _, row in bronze.iterrows():
        clean_content = normalize_text(str(row["raw_content"]))
        for idx, chunk in enumerate(chunk_text(clean_content)):
            chunk_hash = sha256_text(chunk)
            rows.append({
                "document_id": row["document_id"],
                "chunk_id": sha256_text(f"{row['document_id']}|{idx}|{chunk_hash}")[:24],
                "chunk_order": idx,
                "source_file": row["source_file"],
                "domain": row["domain"],
                "version": row["version"],
                "sensitivity_level": row["sensitivity_level"],
                "content": chunk,
                "content_hash": chunk_hash,
                "chunk_size": len(chunk.split()),
                "created_at": utc_now(),
                "is_duplicate": False,
            })
    df = pd.DataFrame(rows)
    if not df.empty:
        df["is_duplicate"] = df.duplicated(subset=["content_hash"], keep="first")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    log_event("SILVER_CHUNKING", {"records": len(df), "output": str(output_file)})
    return df
