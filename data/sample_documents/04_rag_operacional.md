# Operação de RAG Corporativo

Um fluxo RAG recebe uma pergunta, gera representação vetorial, recupera documentos relevantes, monta contexto e envia para o modelo de linguagem.
O objetivo é reduzir alucinação usando contexto recuperado de fontes governadas.
O sistema deve retornar fontes, trechos utilizados e score de recuperação.
Quando a recuperação não encontrar evidência suficiente, a resposta deve indicar que não há base documental adequada.
A observabilidade deve acompanhar latência, custo, taxa de resposta sem evidência e documentos mais utilizados.
