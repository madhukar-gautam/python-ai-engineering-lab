import logging

from app.agents.graphs.rca_graph import rca_graph

logger = logging.getLogger(__name__)


class RCAAgent:

    async def investigate(
        self,
        question: str
    ) -> str:

        logger.info(
            "Starting RCA graph question=%s",
            question
        )

        result = await rca_graph.ainvoke(
            {
                "question": question,
                "order_id": "ORDER-938271"
            }
        )

        logger.info(
            "RCA graph completed error_code=%s",
            result.get("error_code")
        )

        return result["answer"]