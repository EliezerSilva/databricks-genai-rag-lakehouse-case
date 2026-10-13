# Databricks notebook source
from pathlib import Path
import sys
PROJECT_ROOT = Path.cwd()
if (PROJECT_ROOT / "src").exists():
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

print("Vector index artifacts are created by 04_generate_embeddings.py")
