from pipeline.retriever import retrieve_context
from pipeline.prolog_agent import query_prolog

def test_retrieve():
    state = {"query": "What is related to item1?", "context": [], "messages": []}
    result = retrieve_context(state)
    assert len(result["context"]) > 0

def test_prolog_query():
    state = {"query": "rule_example(item1, item2).", "context": [], "messages": []}
    result = query_prolog(state)
    assert "true" in result["messages"][-1]["content"].lower()