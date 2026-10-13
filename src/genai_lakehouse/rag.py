from __future__ import annotations

from time import perf_counter

from .audit import log_event
from .retrieval import search


def build_context(results) -> str:
    parts = []
    for _, row in results.iterrows():
        parts.append(f"Fonte: {row['source_file']} | Score: {row['score']:.4f}\n{row['content']}")
    return "\n\n".join(parts)


def generate_extractive_answer(question: str, context: str, min_score: float) -> str:
    if min_score < 0.05:
        return "Não encontrei evidência suficiente na base de conhecimento para responder com segurança."

    first_block = context.split("\n\n", 1)[0]
    first_content = first_block.split("\n", 1)[-1]
    return (
        "Com base no trecho mais relevante da base de conhecimento, a resposta é: "
        + first_content[:900]
    )


def ask(question: str, top_k: int = 3) -> dict:
    started = perf_counter()
    results = search(question, top_k=top_k)
    max_score = float(results["score"].max()) if not results.empty else 0.0
    context = build_context(results)
    answer = generate_extractive_answer(question, context, max_score)
    elapsed_ms = int((perf_counter() - started) * 1000)
    sources = [
        {
            "source_file": row["source_file"],
            "chunk_id": row["chunk_id"],
            "score": round(float(row["score"]), 4),
            "sensitivity_level": row["sensitivity_level"],
        }
        for _, row in results.iterrows()
    ]
    payload = {
        "question": question,
        "answer": answer,
        "sources": sources,
        "latency_ms": elapsed_ms,
        "status": "ANSWERED" if max_score >= 0.05 else "NO_EVIDENCE",
    }
    log_event("RAG_QUERY", payload)
    return payload
