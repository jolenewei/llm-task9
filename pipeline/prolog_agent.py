import subprocess

def query_prolog(state):
    query = f"verify({state['query'].rstrip('.')})"
    try:
        result = subprocess.run(
            ["swipl", "-q", "-f", "kb.pl", "-t", query],
            capture_output=True,
            text=True
        )
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if stdout:
            output = stdout
        elif stderr:
            output = f"[Prolog error] {stderr}"
        else:
            output = "No result from Prolog."

    except Exception as e:
        output = f"Exception running Prolog: {e}"

    return {
        "messages": state["messages"] + [{
            "role": "assistant",
            "content": f"🤖 Prolog result: `{output}`"
        }],
        "query": state["query"],
        "context": state["context"]
    }