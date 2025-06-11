# LangGraph Logic Agent

This project implements a generalized reasoning system using [LangGraph](https://python.langchain.com/docs/langgraph/) and [Prolog](https://www.swi-prolog.org/), capable of answering symbolic logic queries with the help of:

- Retrieval-Augmented Generation (RAG)
- Prolog inference
- Chain-of-Thought LLM reasoning

Inspired by modular graph-based architectures, this system is **domain-independent** and supports any `.pl` knowledge base.

---

## 🗂️ File Structure

```
langgraph_logic_agent/
├── app.py                   # Main LangGraph execution
├── kb.pl                    # Prolog knowledge base
├── test_app.py              # Tests for core functionality
├── data/
│   └── examples.json        # Example queries
└── pipeline/
    ├── classifier.py
    ├── retriever.py
    ├── prolog_agent.py
    └── reasoner.py
```

---

## Pipeline Flow

```mermaid
graph TD
  A[START] --> B[Classify Question]
  B --> C[Retrieve Context]
  C --> D[Query Prolog]
  D --> E[LLM Reasoning (Chain-of-Thought)]
  E --> F[END]
```

---

## How to Run

### 1. Install dependencies

```bash
pip install langgraph langchain langchain-prolog langchain-openai faiss-cpu
```

> You must also export your OpenAI API key:

```bash
export OPENAI_API_KEY=your-key-here
```

### 2. Start the app

```bash
python app.py
```

You'll be prompted for a question, e.g.:

```
User: rule_example(item1, item2).
AI: true
```

---

## Run Tests

```bash
pytest test_app.py
```

This runs:
- Prolog query validation
- Retrieval pipeline checks

---

## How It Works

- `app.py`: defines the LangGraph pipeline and execution loop
- `classifier.py`: placeholder for logic/ranking classification (extendable)
- `retriever.py`: uses FAISS + embeddings to fetch relevant context
- `prolog_agent.py`: runs queries against a `.pl` knowledge base
- `reasoner.py`: uses OpenAI’s LLM for natural language reasoning based on Prolog results

---

## Sample Queries

See `data/examples.json`:

```
[
  { "query": "rule_example(item1, item2).", "expected": "true" },
  { "query": "related(item1, item2).", "expected": "true" },
  { "query": "fact(item1).", "expected": "true" }
]
```

These queries are domain-agnostic and test symbolic reasoning.