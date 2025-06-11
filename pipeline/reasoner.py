from langchain_openai import ChatOpenAI
llm = ChatOpenAI()

def reason_with_cot(state):
    messages = state["messages"] + [{"role": "user", "content": "Think step by step and answer the question."}]
    response = llm.invoke({"messages": messages})
    return {"messages": state["messages"] + [{"role": "assistant", "content": response}], **state}

