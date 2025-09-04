# Slide 1: Problem & Goals
- Multi-agent pipeline: Data Miner → Medical Summarizer → Decision Maker
- Requirements: async orchestration, error handling, production-grade code, slides + trade-offs

---
# Slide 2: Architecture
- Async orchestrator
- Data Miner: RSS + NewsAPI fallback
- Summarizer: LangChain/OpenAI LLM
- Decision Maker: LLM classifier
- Logging, retries

---
# Slide 3: Tech Choices
- LangChain for LLM orchestration
- httpx/aiohttp for async HTTP
- tenacity for retry/backoff
- CrewAI/AutoGen possible, but LangChain chosen for ecosystem

---
# Slide 4: Error Handling & Scaling
- Retries with backoff
- Graceful degradation: UNKNOWN labels
- Scale horizontally: multiple orchestrator workers

---
# Slide 5: Performance & Cost
- Latency dominated by LLM calls
- Cost controlled by model choice
- Scale with queue + worker pool

---
# Slide 6: Trade-offs
- LLM classification: accurate but costly
- Rule-based classification: cheap but brittle
- RSS vs API: cost vs coverage

---
# Slide 7: Next Steps
- Add monitoring, metrics
- Add storage & dashboard
- Enhance prompts and safety filters
