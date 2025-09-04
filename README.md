# Multi-Agent Health News System

See project layout above. To run locally:

1. Create virtualenv & install: `pip install -r requirements.txt`
2. Create `.env` from `.env.example` and set `OPENAI_API_KEY`.
3. Run once: `python orchestrator.py --once`

Testing: `pytest -q`

Notes: Configure NEWSAPI_KEY if you want NewsAPI fallback. Replace LLM model in `.env` as desired.
