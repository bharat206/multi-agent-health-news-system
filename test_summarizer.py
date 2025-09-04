import asyncio
from agents.summarizer import summarize_articles

def test_summarize_dummy():
    items = [{"title": "Test", "content": "A study shows X may help Y."}]
    out = asyncio.run(summarize_articles(items))
    assert isinstance(out, list)
    assert "summary" in out[0]
