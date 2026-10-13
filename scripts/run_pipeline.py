from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from genai_lakehouse.ingestion import ingest_documents
from genai_lakehouse.chunking import build_silver_chunks
from genai_lakehouse.quality import publish_gold
from genai_lakehouse.embeddings import build_embeddings

if __name__ == "__main__":
    print("[1/4] Bronze ingestion")
    ingest_documents()
    print("[2/4] Silver chunking")
    build_silver_chunks()
    print("[3/4] Gold publish and quality")
    publish_gold()
    print("[4/4] Embeddings and vector index")
    build_embeddings()
    print("Pipeline finished.")
