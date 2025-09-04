import asyncio
from agents.data_miner import fetch_health_news

def test_fetch_health_news_returns_list():
    out = asyncio.run(fetch_health_news(limit=1))
    assert isinstance(out, list)
