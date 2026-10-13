from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from genai_lakehouse.rag import ask

if __name__ == "__main__":
    question = " ".join(sys.argv[1:]) or "Como o Unity Catalog ajuda na governança de IA?"
    result = ask(question)
    print("Pergunta:", result["question"])
    print("Status:", result["status"])
    print("Resposta:\n", result["answer"])
    print("Fontes:")
    for source in result["sources"]:
        print("-", source)
