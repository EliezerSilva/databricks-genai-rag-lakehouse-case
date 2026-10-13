# Arquitetura do Case

Este case adapta a arquitetura Lakehouse do projeto original para um fluxo de IA Generativa.

## Fluxo lógico

1. Ingestão dos documentos na camada Bronze.
2. Extração e limpeza do conteúdo textual.
3. Geração de chunks com metadados e hash.
4. Validação de qualidade e classificação de sensibilidade.
5. Publicação da base Gold para consumo por RAG.
6. Geração de embeddings e índice vetorial.
7. Consulta RAG com resposta baseada em evidências.
8. Registro de auditoria e avaliação.

## Arquitetura alvo em Databricks

- ADLS Gen2 ou S3 como landing zone.
- Delta Lake nas camadas Bronze, Silver e Gold.
- Unity Catalog para governança, ownership e controle de acesso.
- Databricks Workflows para orquestração.
- MLflow para rastreabilidade e avaliação.
- Databricks AI Search para busca semântica.
- Model Serving para endpoint de LLM.
