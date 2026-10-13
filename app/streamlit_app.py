from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

import streamlit as st
from genai_lakehouse.rag import ask

st.set_page_config(page_title="GenAI RAG Lakehouse Case")
st.title("GenAI RAG Lakehouse Case")
st.write("Consulta RAG com base governada em arquitetura Lakehouse.")
question = st.text_input("Pergunta", "Como o Unity Catalog ajuda na governança de IA?")
if st.button("Perguntar"):
    result = ask(question)
    st.subheader("Resposta")
    st.write(result["answer"])
    st.subheader("Fontes")
    st.json(result["sources"])
