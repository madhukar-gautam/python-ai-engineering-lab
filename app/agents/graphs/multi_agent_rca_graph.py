import time
from typing import TypedDict

from langgraph.graph import START, END, StateGraph

from app.agents.specialists.log_agent import LogAgent
from app.agents.specialists.knowledge_agent import KnowledgeAgent
from app.observability.trace import logger


class MultiAgentRCAState(TypedDict, total=False):
    order_id: str
    logs: str
    error_code: str
    knowledge: str
    answer: str

log_agent = LogAgent()
knowledge_agent = KnowledgeAgent()




async def log_agent_node(state):

    start = time.perf_counter()

    logs = await log_agent.investigate(
        state["order_id"]
    )

    latency_ms = (
        time.perf_counter() - start
    ) * 1000

    logger.info(
        "│   ├── TOOL_CALL search_logs latency=%.2fms",
        latency_ms
    )

    return {
        "logs": logs
    }
async def knowledge_agent_node(state):

    start = time.perf_counter()

    knowledge = await knowledge_agent.investigate(
        state["error_code"]
    )

    latency_ms = (
        time.perf_counter() - start
    ) * 1000

    logger.info(
        "│   ├── TOOL_CALL search_knowledge latency=%.2fms",
        latency_ms
    )

    return {
        "knowledge": knowledge
    }
async def analyze_node(
    state: MultiAgentRCAState
) -> dict:

    if "ORA-12541" in state["logs"]:
        return {
            "error_code": "ORA-12541"
        }

    return {
        "error_code": ""
    }
async def synthesize_node(
    state: MultiAgentRCAState
) -> dict:

    answer = (
        f"Logs: {state['logs']} "
        f"Knowledge: "
        f"{state.get('knowledge', 'Not available')}"
    )

    return {
        "answer": answer
    }
def build_multi_agent_rca_graph():

    builder = StateGraph(
        MultiAgentRCAState
    )

    builder.add_node(
        "log_agent",
        log_agent_node
    )

    builder.add_node(
        "analyze",
        analyze_node
    )

    builder.add_node(
        "knowledge_agent",
        knowledge_agent_node
    )

    builder.add_node(
        "synthesize",
        synthesize_node
    )

    builder.add_edge(
        START,
        "log_agent"
    )

    builder.add_edge(
        "log_agent",
        "analyze"
    )

    builder.add_edge(
        "analyze",
        "knowledge_agent"
    )

    builder.add_edge(
        "knowledge_agent",
        "synthesize"
    )

    builder.add_edge(
        "synthesize",
        END
    )

    return builder.compile()


multi_agent_rca_graph = build_multi_agent_rca_graph()