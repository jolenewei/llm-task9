from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI()

def reason_with_cot(state):
    context_text = "\n".join(state["context"])
    prompt = f"""Here are some facts and logic rules:\n{context_text}\n\nBased on the above, answer the query:\n{state["query"]}\nExplain your reasoning."""

    response = llm.invoke(prompt)

    return {
        "messages": state["messages"] + [{"role": "assistant", "content": response.content}],
        **state
    }
