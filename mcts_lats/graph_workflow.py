from typing import Literal
from pydantic import BaseModel
from langgraph.graph import END, StateGraph, START
from mcts_lats.agent import TreeState, generate_initial_response, expand

def should_loop(state: TreeState) -> Literal["expand", "__end__"]:
    """Determine whether to continue the tree search."""
    root = state["root"]
    if root.is_solved:
        return END
    if root.height > 5:
        return END
    return "expand"


def setup_workflow():
    builder = StateGraph(TreeState)
    builder.add_node("start", generate_initial_response)
    builder.add_node("expand", expand)
    builder.add_edge(START, "start")

    builder.add_conditional_edges(
        "start",
        # Either expand/rollout or finish
        should_loop,
    )
    builder.add_conditional_edges(
        "expand",
        # Either continue to rollout or finish
        should_loop,
    )

    graph = builder.compile()

    return graph
