from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
SAMPLE_DOCS_DIR = DATA_DIR / "sample_documents"
LAKEHOUSE_DIR = DATA_DIR / "lakehouse"
BRONZE_DIR = LAKEHOUSE_DIR / "bronze"
SILVER_DIR = LAKEHOUSE_DIR / "silver"
GOLD_DIR = LAKEHOUSE_DIR / "gold"
AUDIT_DIR = LAKEHOUSE_DIR / "audit"
VECTOR_DIR = LAKEHOUSE_DIR / "vector_index"

ALLOWED_SENSITIVITY_LEVELS = {"PUBLIC", "INTERNAL", "SENSITIVE"}
DEFAULT_DOMAIN = "data_and_ai_governance"
DEFAULT_VERSION = "v1"
