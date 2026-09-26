def recall_at_k(
    retrieved_ids: list[str],
    relevant_ids: list[str],
    k: int
) -> float:

    if not relevant_ids:
        return 0.0

    retrieved_at_k = set(
        retrieved_ids[:k]
    )

    relevant = set(relevant_ids)

    relevant_retrieved = (
        retrieved_at_k & relevant
    )

    return (
        len(relevant_retrieved)
        / len(relevant)
    )
def precision_at_k(
    retrieved_ids: list[str],
    relevant_ids: list[str],
    k: int
) -> float:

    retrieved_at_k = retrieved_ids[:k]

    if not retrieved_at_k:
        return 0.0

    relevant = set(relevant_ids)

    relevant_retrieved = [
        document_id
        for document_id in retrieved_at_k
        if document_id in relevant
    ]

    return (
        len(relevant_retrieved)
        / len(retrieved_at_k)
    )
def reciprocal_rank(
    retrieved_ids: list[str],
    relevant_ids: list[str]
) -> float:

    relevant = set(relevant_ids)

    for rank, document_id in enumerate(
        retrieved_ids,
        start=1
    ):
        if document_id in relevant:
            return 1.0 / rank

    return 0.0