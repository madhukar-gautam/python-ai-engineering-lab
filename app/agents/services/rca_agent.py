import json
import logging

from app.llm.clients.llm_client import LLMClient
from app.agents.tools.incident_tools import (
    search_logs,
    search_knowledge
)

logger = logging.getLogger(__name__)


class RCAAgent:

    def __init__(
        self,
        llm_client: LLMClient
    ) -> None:
        self.llm_client = llm_client

    async def investigate(
        self,
        question: str
    ) -> str:

        logger.warning(
            "RCA agent started question=%s",
            question
        )

        decision = await self.llm_client.generate(
            system_prompt=(
                "You are an RCA agent. "
                "Available tools:\n"
                "1. search_logs(order_id)\n"
                "2. search_knowledge(error_code)\n\n"
                "Choose the best tool for the user's request. "
                "Return ONLY valid JSON in this format: "
                '{"tool":"search_logs",'
                '"arguments":{"order_id":"ORDER-938271"}}'
            ),
            message=question
        )

        logger.warning(
            "Agent decision=%s",
            decision.answer
        )

        action = json.loads(decision.answer)

        tool = action["tool"]
        arguments = action["arguments"]

        logger.warning(
            "Agent selected tool=%s arguments=%s",
            tool,
            arguments
        )

        if tool == "search_logs":
            observation = await search_logs(
                arguments["order_id"]
            )

        elif tool == "search_knowledge":
            observation = await search_knowledge(
                arguments["error_code"]
            )

        else:
            observation = "Unknown tool."

        logger.warning(
            "Tool observation=%s",
            observation
        )

        final = await self.llm_client.generate(
            system_prompt=(
                "Answer using the supplied "
                "investigation evidence."
            ),
            message=f"""
Question:
{question}

Evidence:
{observation}
"""
        )

        return final.answer