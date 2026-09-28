async def search_logs(
    order_id: str
) -> str:

    if order_id == "ORDER-938271":
        return (
            "Order failed with ORA-12541. "
            "Database connection failed."
        )

    return "No logs found."


async def search_knowledge(
    error_code: str
) -> str:

    if error_code == "ORA-12541":
        return (
            "ORA-12541 means the Oracle "
            "listener is unavailable."
        )

    return "No knowledge found."