# Databricks GenAI RAG Lakehouse Case

Case técnico de **Engenharia de Dados para IA Generativa**, criado como evolução do projeto `databricks-lakehouse-case`.

O objetivo não é demonstrar um chatbot genérico. O foco é mostrar como um Engenheiro de Dados Sênior prepara uma base confiável, governada e rastreável para aplicações de **RAG, embeddings, busca semântica, Analytics, Machine Learning, IA e GenAI**.

---

## Objetivo do case

Demonstrar uma arquitetura Lakehouse para documentos corporativos usados por IA Generativa:

```text
SAMPLE DOCUMENTS
      ↓
BRONZE  - documento bruto, hash, origem, metadados técnicos
      ↓
SILVER  - texto limpo, chunking, deduplicação, qualidade e quarentena
      ↓
GOLD    - knowledge base governada para RAG
      ↓
VECTOR INDEX - embeddings e busca semântica
      ↓
RAG APP - resposta com fontes, score, auditoria e avaliação
```

---

## Competências demonstradas

- Databricks Lakehouse Architecture
- Bronze, Silver e Gold
- PySpark / Spark SQL como desenho alvo
- Python para implementação local e reprodutível
- Delta Lake como arquitetura conceitual
- Data Quality
- Data Governance
- Data Lineage
- Unity Catalog como camada de governança conceitual
- RAG
- Embeddings
- Semantic Search
- Vector Index
- Auditoria e observabilidade
- Avaliação de respostas GenAI
- FastAPI / Streamlit como camada de consumo
- CI/CD e testes automatizados

---

## Por que este projeto é útil em entrevista

Este projeto permite explicar GenAI do ponto de vista correto para Engenharia de Dados:

> Minha atuação em GenAI está na fundação de dados: ingestão, qualidade, governança, rastreabilidade, segurança, preparação de documentos, geração de chunks, embeddings, busca semântica, auditoria e avaliação. O objetivo é permitir que aplicações de IA consumam dados confiáveis e governados.

---

## Estrutura

```text
databricks-genai-rag-lakehouse-case/
├── architecture/
├── data/
│   ├── sample_documents/
│   └── lakehouse/
├── docs/
├── notebooks/
├── src/genai_lakehouse/
├── app/
├── tests/
├── evaluation/
└── orchestration/
```

---

## Execução local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/run_pipeline.py
python scripts/run_demo_query.py "Como o Unity Catalog ajuda na governança de IA?"
pytest -q
```

A implementação local usa **TF-IDF** como embedding simples para permitir execução sem chave de API e sem custo. Em produção, a troca natural seria usar **Databricks Model Serving, Mosaic AI, OpenAI, Claude, Gemini ou outro provedor aprovado pela empresa**.

---

## Execução no Databricks

Os scripts em `notebooks/` foram organizados para simular uma sequência de notebooks Databricks:

```text
01_ingest_documents
  → 02_extract_clean_chunk
    → 03_quality_and_gold
      → 04_generate_embeddings
        → 05_build_vector_index
          → 06_rag_query_demo
```

O arquivo `orchestration/databricks_workflow.yml` mostra uma proposta de workflow.

---

## Principais tabelas simuladas

| Camada | Artefato | Descrição |
|---|---|---|
| Bronze | `bronze_documents.csv` | documento bruto, hash, origem e metadados técnicos |
| Silver | `silver_chunks.csv` | chunks limpos, deduplicados e validados |
| Gold | `gold_knowledge_base.csv` | base governada para RAG |
| Audit | `audit_events.jsonl` | eventos do pipeline e perguntas do RAG |
| Vector | `tfidf_matrix.pkl` | matriz vetorial local para busca semântica |

---

## Decisões técnicas

- **Medallion Architecture:** separa ingestão, limpeza e consumo.
- **Hash determinístico:** permite deduplicação e rastreabilidade.
- **Chunking com overlap:** preserva contexto entre trechos.
- **Resposta com fontes:** evita resposta sem evidência.
- **Auditoria:** registra execução do pipeline, pergunta, documentos recuperados, score e latência.
- **Avaliação:** mede cobertura, recuperação e comportamento das respostas.
- **Sem dependência de API paga:** facilita demonstração em entrevista e GitHub.

---

## Limitações

- TF-IDF foi usado como embedding local para simplificar execução.
- Não há uso real de endpoint LLM por padrão.
- Delta Lake e Unity Catalog aparecem como arquitetura-alvo e documentação, não como dependência obrigatória local.
- Os documentos são sintéticos e criados para demonstrar o padrão.

---

## Evoluções recomendadas

- Implementar Delta Lake real em Databricks.
- Publicar tabelas no Unity Catalog.
- Trocar TF-IDF por Databricks AI Search / Vector Search.
- Adicionar MLflow Tracing para RAG.
- Implementar avaliação automática de respostas.
- Integrar Model Serving com LLM corporativo.
- Adicionar DAB - Databricks Asset Bundles.

---

## Pitch curto

> Desenvolvi um case de Engenharia de Dados para GenAI usando arquitetura Lakehouse. O fluxo ingere documentos, organiza em Bronze/Silver/Gold, aplica qualidade e governança, gera chunks e embeddings, cria busca semântica e expõe uma aplicação RAG com auditoria, lineage e avaliação. O foco é mostrar como dados corporativos precisam ser preparados e governados antes de serem usados por IA Generativa.
