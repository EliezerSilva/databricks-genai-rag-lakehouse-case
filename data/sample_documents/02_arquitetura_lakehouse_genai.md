# Arquitetura Lakehouse para GenAI

A arquitetura proposta usa camadas Bronze, Silver e Gold para preparar dados e documentos para GenAI.
A camada Bronze mantém o documento bruto, hash, origem, caminho e data de ingestão.
A camada Silver extrai texto, remove duplicidades, aplica validações, gera chunks e padroniza metadados.
A camada Gold organiza a base de conhecimento pronta para busca semântica e RAG.
A solução pode ser implementada em Databricks usando Delta Lake, Unity Catalog, Workflows, MLflow e AI Search.
