from langchain_prolog import PrologTool, PrologConfig

pl_tool = PrologTool(
    name="prolog_tool",
    description="Queries a Prolog knowledge base for logical inference.",
    prolog=PrologConfig(path="kb.pl")
)

def query_prolog(state):
    q = state["query"]
    output = pl_tool.run(q)
    return {"messages": state["messages"] + [{"role": "assistant", "content": output}], **state}