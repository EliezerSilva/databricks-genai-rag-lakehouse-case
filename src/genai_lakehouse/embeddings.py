from __future__ import annotations

import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from .audit import log_event
from .config import GOLD_DIR, VECTOR_DIR

GOLD_FILE = GOLD_DIR / "gold_knowledge_base.csv"
VECTORIZER_FILE = VECTOR_DIR / "tfidf_vectorizer.pkl"
MATRIX_FILE = VECTOR_DIR / "tfidf_matrix.pkl"
METADATA_FILE = VECTOR_DIR / "vector_metadata.csv"


def build_embeddings(gold_file=GOLD_FILE):
    gold = pd.read_csv(gold_file)
    texts = gold["content"].fillna("").tolist()
    vectorizer = TfidfVectorizer(lowercase=True, ngram_range=(1, 2), min_df=1)
    matrix = vectorizer.fit_transform(texts)
    VECTOR_DIR.mkdir(parents=True, exist_ok=True)
    with VECTORIZER_FILE.open("wb") as f:
        pickle.dump(vectorizer, f)
    with MATRIX_FILE.open("wb") as f:
        pickle.dump(matrix, f)
    metadata = gold[["chunk_id", "document_id", "source_file", "domain", "sensitivity_level", "version", "content"]].copy()
    metadata.to_csv(METADATA_FILE, index=False)
    log_event("EMBEDDINGS_BUILD", {"records": len(metadata), "features": len(vectorizer.get_feature_names_out()), "output": str(VECTOR_DIR)})
    return vectorizer, matrix, metadata
