from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from fastapi import FastAPI
from pydantic import BaseModel
from genai_lakehouse.rag import ask

app = FastAPI(title="GenAI RAG Lakehouse Case")

class Question(BaseModel):
    question: str
    top_k: int = 3

@app.post("/ask")
def ask_question(payload: Question):
    return ask(payload.question, top_k=payload.top_k)
