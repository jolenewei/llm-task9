from pipeline.prolog_agent import query_prolog

def test_prolog_query():
    state = {"query": "connected(luna, milo).", "context": [], "messages": []}
    result = query_prolog(state)
    assert "true" in result["messages"][-1]["content"].lower()
