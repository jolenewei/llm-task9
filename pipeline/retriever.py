import os
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

# General-purpose placeholder documents
DOCS = [
    "fact(item1).",
    "fact(item2).",
    "related(item1, item2).",
    "rule_example(X,Y) :- related(X,Y)."
]
VS = FAISS.from_texts(DOCS, OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"]))

def retrieve_context(state):
    results = VS.similarity_search(state["query"], k=3)
    return {"context": [r.page_content for r in results], **state}
