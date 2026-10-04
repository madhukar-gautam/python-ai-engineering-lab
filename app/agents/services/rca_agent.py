import time

from app.agents.graphs.multi_agent_rca_graph import (
    multi_agent_rca_graph
)

from app.observability.trace import TraceContext


class RCAAgent:

    async def investigate(
        self,
        question: str
    ) -> str:

        trace = TraceContext()

        trace.start(
            "RCA investigation"
        )

        start = time.perf_counter()

        result = await multi_agent_rca_graph.ainvoke(
            {
                "order_id": "ORDER-938271"
            }
        )

        latency_ms = (
            time.perf_counter() - start
        ) * 1000

        trace.log_step(
            "RCA graph",
            latency_ms=latency_ms
        )

        trace.end()

        return result["answer"]