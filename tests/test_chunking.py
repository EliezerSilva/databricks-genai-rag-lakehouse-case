from pathlib import Path
import sys
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from genai_lakehouse.chunking import chunk_text


def test_chunk_text_returns_chunks():
    text = " ".join(["palavra"] * 120)
    chunks = chunk_text(text, max_words=50, overlap=10)
    assert len(chunks) >= 2
    assert all(len(c.split()) <= 50 for c in chunks)
