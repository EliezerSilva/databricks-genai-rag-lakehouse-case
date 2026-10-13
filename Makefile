install:
	pip install -r requirements.txt

run:
	python scripts/run_pipeline.py

query:
	python scripts/run_demo_query.py "Como preparar dados para GenAI com governança?"

test:
	pytest -q
