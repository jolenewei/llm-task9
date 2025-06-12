import subprocess

def query_prolog(state):
    # Get and sanitize input
    raw_query = state["query"].strip().rstrip(".")
    wrapped_query = f"respond({raw_query})"
    
    print("🧠 Query to Prolog:", wrapped_query)

    try:
        result = subprocess.run(
            ["swipl", "-q", "-f", "kb.pl", "-t", wrapped_query],
            capture_output=True,
            text=True
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        print("STDOUT:", repr(stdout))
        print("STDERR:", repr(stderr))

        if stdout:
            output = stdout
        elif stderr:
            output = f"[Prolog error] {stderr}"
        else:
            output = "No output from Prolog."

    except Exception as e:
        output = f"[Exception] {e}"

    # Return updated state
    return {
        "messages": state["messages"] + [{
            "role": "assistant",
            "content": output
        }],
        "query": state["query"],
        "context": state["context"]
    }

