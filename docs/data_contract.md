# Contrato de Dados - Gold Knowledge Base

| Campo | Tipo | Obrigatório | Regra |
|---|---|---|---|
| document_id | string | sim | hash do documento |
| chunk_id | string | sim | hash do chunk |
| source_file | string | sim | arquivo de origem |
| domain | string | sim | domínio de negócio |
| sensitivity_level | string | sim | PUBLIC, INTERNAL ou SENSITIVE |
| version | string | sim | versão lógica do documento |
| content | string | sim | texto do chunk |
| content_hash | string | sim | hash do conteúdo |
| chunk_size | int | sim | quantidade de palavras |
| created_at | timestamp | sim | data de processamento |
| is_active | boolean | sim | chunk ativo para busca |
