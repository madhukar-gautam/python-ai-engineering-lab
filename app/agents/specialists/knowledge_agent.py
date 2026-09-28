from app.agents.tools.incident_tools import search_knowledge


class KnowledgeAgent:

    async def investigate(
        self,
        error_code: str
    ) -> str:

        return await search_knowledge(error_code)