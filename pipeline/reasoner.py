from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI()

def reason_with_cot(state):
    context_text = "\n".join(state["context"])
    prompt = f"""Context:\n{context_text}\n\nQuestion: {state["query"]}\n\nPlease explain your answer using reasoning based on the context above."""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {
        "messages": state["messages"] + [{
            "role": "assistant",
            "content": f"Reasoning: {response.content}"
        }],
        "query": state["query"],
        "context": state["context"]
    }
