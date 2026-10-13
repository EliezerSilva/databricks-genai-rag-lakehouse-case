from pathlib import Path
import sys
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from genai_lakehouse.ingestion import ingest_documents
from genai_lakehouse.chunking import build_silver_chunks
from genai_lakehouse.quality import publish_gold
from genai_lakehouse.embeddings import build_embeddings
from genai_lakehouse.rag import ask


def test_pipeline_end_to_end():
    bronze = ingest_documents()
    assert len(bronze) > 0
    silver = build_silver_chunks()
    assert len(silver) > 0
    gold, quality = publish_gold()
    assert len(gold) > 0
    assert len(quality) >= 1
    build_embeddings()
    result = ask("Como o Unity Catalog ajuda na governança de IA?")
    assert result["status"] in {"ANSWERED", "NO_EVIDENCE"}
    assert "sources" in result
