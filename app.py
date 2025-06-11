from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from pipeline.classifier import classify_question
from pipeline.retriever import retrieve_context
from pipeline.prolog_agent import query_prolog
from pipeline.reasoner import reason_with_cot

class State(TypedDict):
    messages: Annotated[list, add_messages]
    query: str
    context: list[str]

builder = StateGraph(State)

builder.add_node("classify", classify_question)
builder.add_node("retrieve", retrieve_context)
builder.add_node("query_prolog", query_prolog)
builder.add_node("reason", reason_with_cot)

builder.set_entry_point("classify")
builder.add_edge("classify", "retrieve")
builder.add_edge("retrieve", "query_prolog")
builder.add_edge("query_prolog", "reason")
builder.add_edge("reason", END)

app = builder.compile()

def main():
    while True:
        user_input = input("User: ")
        state = {"messages": [{"role": "user", "content": user_input}], "query": user_input, "context": []}
        for step in app.stream(state, {}, stream_mode="values"):
            print("AI:", step["messages"][-1]["content"])

if __name__ == "__main__":
    main()