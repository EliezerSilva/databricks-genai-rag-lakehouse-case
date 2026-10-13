from __future__ import annotations

import pandas as pd

from .rag import ask


def run_evaluation(eval_file: str, output_file: str) -> pd.DataFrame:
    dataset = pd.read_csv(eval_file)
    rows = []
    for _, row in dataset.iterrows():
        result = ask(row["question"], top_k=3)
        retrieved_sources = ",".join([s["source_file"] for s in result["sources"]])
        expected_source = row.get("expected_source", "")
        rows.append({
            "question": row["question"],
            "expected_source": expected_source,
            "retrieved_sources": retrieved_sources,
            "hit_expected_source": expected_source in retrieved_sources if expected_source else None,
            "status": result["status"],
            "latency_ms": result["latency_ms"],
        })
    df = pd.DataFrame(rows)
    df.to_csv(output_file, index=False)
    return df
