from mcp.server import MCPServer


mcp = MCPServer(
    "Incident Investigation Server"
)


@mcp.tool()
async def search_logs(
    order_id: str
) -> str:
    """
    Search application logs for an order.
    """

    if order_id == "ORDER-938271":
        return (
            "Order failed with ORA-12541. "
            "Database connection failed."
        )

    return "No relevant logs found."


@mcp.tool()
async def search_knowledge(
    error_code: str
) -> str:
    """
    Search operational knowledge for an error.
    """

    if error_code == "ORA-12541":
        return (
            "ORA-12541 means the Oracle "
            "listener is unavailable."
        )

    return "No knowledge found."


if __name__ == "__main__":
    mcp.run()