# Modelo de Governança para IA

O projeto simula um modelo onde documentos e chunks possuem metadados de origem, domínio, versão, classificação de sensibilidade e status ativo.

Em Databricks, a implementação alvo seria:

- Unity Catalog para catálogo central.
- Schemas separados por camada: bronze, silver, gold e audit.
- Grupos de acesso por domínio.
- Tags para classificação de dados.
- Auditoria de consultas RAG.
- Revisão periódica de permissões.
- Políticas de mascaramento para dados sensíveis.
