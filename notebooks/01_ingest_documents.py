# Databricks notebook source
from pathlib import Path
import sys
PROJECT_ROOT = Path.cwd()
if (PROJECT_ROOT / "src").exists():
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

from genai_lakehouse.ingestion import ingest_documents
ingest_documents()
