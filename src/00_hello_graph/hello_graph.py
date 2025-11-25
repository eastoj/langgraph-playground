from langgraph.graph import StateGraph, END

def node_fn(state: dict) -> dict:
    print("Hello from LangGraph! State:", state)
    return {"message": "done"}

graph = StateGraph(dict)
graph.add_node("start", node_fn)
graph.set_entry_point("start")
graph.add_edge("start", END)

app = graph.compile()

if __name__ == "__main__":
    result = app.invoke({"message": "start"})
    print("Result:", result)