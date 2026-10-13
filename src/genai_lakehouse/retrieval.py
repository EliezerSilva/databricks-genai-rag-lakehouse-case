from __future__ import annotations

import pickle
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

from .config import VECTOR_DIR

VECTORIZER_FILE = VECTOR_DIR / "tfidf_vectorizer.pkl"
MATRIX_FILE = VECTOR_DIR / "tfidf_matrix.pkl"
METADATA_FILE = VECTOR_DIR / "vector_metadata.csv"


def load_index():
    with VECTORIZER_FILE.open("rb") as f:
        vectorizer = pickle.load(f)
    with MATRIX_FILE.open("rb") as f:
        matrix = pickle.load(f)
    metadata = pd.read_csv(METADATA_FILE)
    return vectorizer, matrix, metadata


def search(query: str, top_k: int = 3) -> pd.DataFrame:
    vectorizer, matrix, metadata = load_index()
    query_vector = vectorizer.transform([query])
    scores = cosine_similarity(query_vector, matrix).flatten()
    result = metadata.copy()
    result["score"] = scores
    result = result.sort_values("score", ascending=False).head(top_k)
    return result.reset_index(drop=True)
