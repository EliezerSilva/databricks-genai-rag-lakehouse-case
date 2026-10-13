# Contrato de Dados - Base de Conhecimento RAG

A tabela gold_knowledge_base deve conter: document_id, chunk_id, source_file, domain, sensitivity_level, version, content, content_hash, chunk_size, created_at e is_active.
O campo content não pode estar vazio.
O campo sensitivity_level deve aceitar PUBLIC, INTERNAL ou SENSITIVE.
O campo version deve permitir rastrear alterações do documento ao longo do tempo.
O campo content_hash deve permitir identificar duplicidades e reprocessamentos.
