from app.agents.graphs.multi_agent_rca_graph import (
    multi_agent_rca_graph
)


class RCAAgent:

    async def investigate(
        self,
        question: str
    ) -> str:

        result = await multi_agent_rca_graph.ainvoke(
            {
                "order_id": "ORDER-938271"
            }
        )

        return result["answer"]