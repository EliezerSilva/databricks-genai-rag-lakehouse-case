# Regras de Qualidade

| Regra | Severidade | Descrição |
|---|---|---|
| DOC_NOT_EMPTY | crítica | documento não pode estar vazio |
| CONTENT_HASH_PRESENT | crítica | todo documento e chunk precisa ter hash |
| CHUNK_MIN_SIZE | média | chunk deve ter tamanho mínimo configurado |
| NO_DUPLICATE_CHUNK | crítica | chunks duplicados não devem ser publicados na Gold |
| VALID_SENSITIVITY_LEVEL | crítica | nível de sensibilidade deve estar no domínio permitido |
| SOURCE_METADATA_PRESENT | média | origem, versão e domínio devem estar preenchidos |
