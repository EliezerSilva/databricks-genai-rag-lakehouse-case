# Playbook de Qualidade de Dados

As regras mínimas de qualidade para dados usados por IA incluem obrigatoriedade de metadados, detecção de documento vazio, controle de duplicidade por hash, tamanho mínimo do chunk e bloqueio de conteúdo sensível quando aplicável.
Falhas críticas devem impedir a publicação na camada Gold.
Falhas não críticas podem seguir para quarentena com registro em tabela de auditoria.
Os indicadores operacionais incluem volume ingerido, chunks válidos, documentos duplicados, taxa de erro, tempo de processamento e cobertura de metadados.
