import asyncio
from agents.decision_maker import decide_all

def test_decide_all_dummy():
    items = [{"title": "T", "summary": "If you feel fever, rest and consult a physician."}]
    out = asyncio.run(decide_all(items))
    assert isinstance(out, list)
    assert "label" in out[0]
