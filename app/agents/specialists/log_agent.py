from app.agents.tools.incident_tools import search_logs


class LogAgent:

    async def investigate(
        self,
        order_id: str
    ) -> str:

        return await search_logs(order_id)