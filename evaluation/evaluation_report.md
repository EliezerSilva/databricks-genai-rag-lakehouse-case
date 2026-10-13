# Evaluation Report

Execute:

```bash
python scripts/run_pipeline.py
python -c "import sys; sys.path.insert(0, 'src'); from genai_lakehouse.evaluation import run_evaluation; run_evaluation('evaluation/eval_dataset.csv', 'evaluation/evaluation_results.csv')"
```

Métricas esperadas:

- `hit_expected_source`: se a fonte esperada apareceu entre os documentos recuperados.
- `status`: ANSWERED ou NO_EVIDENCE.
- `latency_ms`: latência local da consulta.
