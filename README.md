# 🔍 LangGraph Prolog Reasoning Agent

This project is a symbolic reasoning pipeline that integrates:

- **SWI-Prolog** for symbolic logic evaluation  
- **OpenAI LLMs** (via LangChain) for reasoning and explanation  
- **LangGraph** to build a reactive graph-based agent  
- **FAISS + Embeddings** for fact retrieval based on query similarity

## What It Does

You can input symbolic logic queries like:

```prolog
connected(luna, milo).
trusts(luna, nova).
```

The agent will:

1. Retrieve similar facts/rules from a vector database  
2. Query a Prolog knowledge base (`kb.pl`)  
3. Generate a natural language explanation using an LLM

## File Structure

```
llm-task9/
├── app.py                  # CLI for querying the logic agent
├── kb.pl                   # Prolog knowledge base (facts and rules)
├── test_app.py             # Quick test script
├── data/
│   └── examples.json       # Optional symbolic queries for testing
├── pipeline/
│   ├── classifier.py       # (Placeholder) question classifier
│   ├── retriever.py        # FAISS vector retriever
│   ├── prolog_agent.py     # Runs Prolog subprocess
│   └── reasoner.py         # Generates LLM reasoning explanation
├── .env                    # Set your OpenAI API key here
├── requirements.txt        # Dependencies
└── README.md               # This file
```

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Install SWI-Prolog

Make sure `swipl` works in your terminal.

You should be able to run:

```bash
swipl -q -f kb.pl -t "connected(luna, milo)."
```

### 3. Set your OpenAI API Key

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=sk-...
```

## Usage

Start the CLI agent:

```bash
python app.py
```

Then input example queries like:

```prolog
connected(luna, milo).
trusts(nova, luna).
rule_example(luna, milo).
```

Or run tests:

```bash
python test_app.py
```

## Example `kb.pl`

```prolog
fact(luna).
fact(milo).
connected(luna, milo).
trusts(nova, luna).

rule_example(X, Y) :- connected(X, Y).

respond(Query) :- call(Query), write('true'), nl.
respond(_) :- write('false'), nl.
```

## requirements.txt - Download before

```
langchain
langchain-community
langchain-openai
langgraph
faiss-cpu
openai
tiktoken
python-dotenv
typing-extensions
```