# Lineage

Lineage lógico do case:

```text
sample_documents/*.md
  -> bronze_documents.csv
    -> silver_chunks.csv
      -> gold_knowledge_base.csv
        -> tfidf_matrix.pkl
          -> rag_response
            -> audit_events.jsonl
```

Cada resposta RAG registra os chunks recuperados, documento de origem, score e latência.
