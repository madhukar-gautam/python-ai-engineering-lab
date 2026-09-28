from typing import TypedDict

from langgraph.graph import START, END, StateGraph

from app.agents.tools.incident_tools import (
    search_logs,
    search_knowledge
)
import logging

logger = logging.getLogger(__name__)


class RCAState(TypedDict, total=False):
    question: str
    order_id: str
    logs: str
    error_code: str
    knowledge: str
    answer: str


async def search_logs_node(
    state: RCAState
) -> dict:

    logger.info(
        "NODE=search_logs order_id=%s",
        state["order_id"]
    )

    logs = await search_logs(
        state["order_id"]
    )

    return {"logs": logs}


async def analyze_error_node(
    state: RCAState
) -> dict:

    logger.info("NODE=analyze_error")

    logs = state["logs"]

    if "ORA-12541" in logs:
        return {"error_code": "ORA-12541"}

    return {"error_code": ""}


async def search_knowledge_node(
    state: RCAState
) -> dict:

    logger.info(
        "NODE=search_knowledge error_code=%s",
        state["error_code"]
    )

    knowledge = await search_knowledge(
        state["error_code"]
    )

    return {"knowledge": knowledge}


async def answer_node(
    state: RCAState
) -> dict:

    logger.info("NODE=answer")

    answer = (
        f"Order investigation: {state['logs']} "
        f"Knowledge: "
        f"{state.get('knowledge', 'Not required')}"
    )

    return {"answer": answer}
def route_after_analysis(
    state: RCAState
) -> str:

    if state.get("error_code"):
        logger.info(
            "ROUTE=search_knowledge"
        )
        return "search_knowledge"

    logger.info(
        "ROUTE=answer"
    )
    return "answer"

def build_rca_graph():

    builder = StateGraph(RCAState)

    builder.add_node(
        "search_logs",
        search_logs_node
    )

    builder.add_node(
        "analyze_error",
        analyze_error_node
    )

    builder.add_node(
        "search_knowledge",
        search_knowledge_node
    )

    builder.add_node(
        "answer",
        answer_node
    )

    builder.add_edge(
        START,
        "search_logs"
    )

    builder.add_edge(
        "search_logs",
        "analyze_error"
    )

    builder.add_conditional_edges(
        "analyze_error",
        route_after_analysis,
        {
            "search_knowledge": "search_knowledge",
            "answer": "answer"
        }
    )

    builder.add_edge(
        "search_knowledge",
        "answer"
    )

    builder.add_edge(
        "answer",
        END
    )

    return builder.compile()


rca_graph = build_rca_graph()