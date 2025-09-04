# orchestrator.py
import os
import asyncio
import logging
from agents.data_miner import fetch_health_news, DataMinerError
from agents.summarizer import summarize_articles
from agents.decision_maker import decide_all
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger("orchestrator")

MAX_ARTICLES = int(os.getenv("MAX_ARTICLES", "6"))


async def run_once():
    logger.info("Starting run_once pipeline")
    try:
        articles = await fetch_health_news(limit=MAX_ARTICLES)
    except DataMinerError as e:
        logger.exception("Data miner failed: %s", e)
        return []

    logger.info("Fetched %d articles", len(articles))

    summarized = await summarize_articles(articles)
    logger.info("Summarized articles")

    decided = await decide_all(summarized)
    logger.info("Decision maker labeled %d articles", len(decided))

    for d in decided:
        logger.info("TITLE: %s | LABEL: %s | SUMMARY: %s", d.get("title"), d.get("label"), (d.get("summary") or "<err>"))

    return decided


async def main_loop(poll_interval: int = 300):
    while True:
        await run_once()
        logger.info("Sleeping for %d seconds", poll_interval)
        await asyncio.sleep(poll_interval)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="Run pipeline once and exit")
    parser.add_argument("--interval", type=int, default=300, help="Poll interval in seconds")
    args = parser.parse_args()

    if args.once:
        asyncio.run(run_once())
    else:
        asyncio.run(main_loop(poll_interval=args.interval))
