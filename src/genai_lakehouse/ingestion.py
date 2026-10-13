from __future__ import annotations

from pathlib import Path
import pandas as pd

from .audit import log_event
from .config import BRONZE_DIR, DEFAULT_DOMAIN, DEFAULT_VERSION, SAMPLE_DOCS_DIR
from .utils import normalize_text, sha256_text, utc_now

BRONZE_FILE = BRONZE_DIR / "bronze_documents.csv"


def infer_sensitivity(text: str) -> str:
    lower = text.lower()
    sensitive_terms = ["cpf", "cnpj", "paciente", "médica", "medica", "imagem médica", "imagem medica"]
    if any(term in lower for term in sensitive_terms):
        return "SENSITIVE"
    internal_terms = ["política", "governança", "unity catalog", "contrato de dados"]
    if any(term in lower for term in internal_terms):
        return "INTERNAL"
    return "PUBLIC"


def ingest_documents(source_dir: Path = SAMPLE_DOCS_DIR, output_file: Path = BRONZE_FILE) -> pd.DataFrame:
    rows = []
    for path in sorted(source_dir.glob("*")):
        if path.is_dir():
            continue
        if path.suffix.lower() not in {".md", ".txt"}:
            continue
        raw_text = path.read_text(encoding="utf-8")
        normalized = normalize_text(raw_text)
        document_id = sha256_text(f"{path.name}|{normalized}")[:24]
        rows.append({
            "document_id": document_id,
            "source_file": path.name,
            "source_path": str(path),
            "file_type": path.suffix.lower().replace(".", ""),
            "domain": DEFAULT_DOMAIN,
            "version": DEFAULT_VERSION,
            "sensitivity_level": infer_sensitivity(normalized),
            "raw_content": raw_text,
            "content_hash": sha256_text(normalized),
            "ingested_at": utc_now(),
            "record_status": "LOADED" if normalized else "EMPTY",
        })
    df = pd.DataFrame(rows)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_file, index=False)
    log_event("BRONZE_INGESTION", {"records": len(df), "output": str(output_file)})
    return df
