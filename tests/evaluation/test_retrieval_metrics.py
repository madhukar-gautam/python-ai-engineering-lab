from app.evaluation.metrics.retrieval_metrics import (
    precision_at_k,
    recall_at_k,
    reciprocal_rank
)


def test_recall_at_k():

    retrieved = [
        "6-0",
        "2-0",
        "1-0"
    ]

    relevant = ["6-0"]

    result = recall_at_k(
        retrieved_ids=retrieved,
        relevant_ids=relevant,
        k=3
    )

    assert result == 1.0


def test_precision_at_k():

    retrieved = [
        "6-0",
        "2-0",
        "1-0"
    ]

    relevant = ["6-0"]

    result = precision_at_k(
        retrieved_ids=retrieved,
        relevant_ids=relevant,
        k=3
    )

    assert result == 1 / 3


def test_reciprocal_rank_first():

    retrieved = [
        "6-0",
        "2-0",
        "1-0"
    ]

    relevant = ["6-0"]

    result = reciprocal_rank(
        retrieved_ids=retrieved,
        relevant_ids=relevant
    )

    assert result == 1.0


def test_reciprocal_rank_third():

    retrieved = [
        "2-0",
        "1-0",
        "6-0"
    ]

    relevant = ["6-0"]

    result = reciprocal_rank(
        retrieved_ids=retrieved,
        relevant_ids=relevant
    )

    assert result == 1 / 3