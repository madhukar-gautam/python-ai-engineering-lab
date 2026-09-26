from app.evaluation.models.evaluation_case import (
    EvaluationCase
)


def get_rag_evaluation_dataset() -> list[EvaluationCase]:

    return [
        EvaluationCase(
            id="kafka_performance",
            question=(
                "What can cause Kafka consumers "
                "to process messages slowly?"
            ),
            expected_source_ids=["2-0"],
            expected_answer_concepts=[
                "slow downstream services",
                "database latency",
                "insufficient consumer instances",
                "expensive message processing"
            ]
        ),

        EvaluationCase(
            id="kafka_lag",
            question=(
                "What happens when Kafka consumers "
                "process messages slower than producers?"
            ),
            expected_source_ids=["1-0"],
            expected_answer_concepts=[
                "consumer lag"
            ]
        ),

        EvaluationCase(
            id="order_failure",
            question=(
                "Why did ORDER-938271 fail "
                "with ORA-12541?"
            ),
            expected_source_ids=["6-0"],
            expected_answer_concepts=[
                "Oracle listener",
                "unavailable"
            ]
        ),

        EvaluationCase(
            id="rag_architecture",
            question=(
                "How does a RAG system use "
                "retrieved documents?"
            ),
            expected_source_ids=["3-0"],
            expected_answer_concepts=[
                "context",
                "language model"
            ]
        ),

        EvaluationCase(
            id="spring_metrics",
            question=(
                "How can Spring Boot metrics be "
                "collected and visualized?"
            ),
            expected_source_ids=["4-0"],
            expected_answer_concepts=[
                "Actuator",
                "Micrometer",
                "Prometheus",
                "Grafana"
            ]
        ),
        EvaluationCase(
            id="kafka_semantic_paraphrase",
            question=(
                "Why might message consumption "
                "fall behind message production?"
            ),
            expected_source_ids=["1-0"],
            expected_answer_concepts=[
                "consumer lag"
            ]
        ),

        EvaluationCase(
            id="order_identifier_only",
            question=(
                "What infrastructure problem caused "
                "incident ORDER-938271?"
            ),
            expected_source_ids=["6-0"],
            expected_answer_concepts=[
                "Oracle listener",
                "unavailable"
            ]
        ),

        EvaluationCase(
            id="observability_paraphrase",
            question=(
                "How can I monitor a Java service "
                "and display its operational measurements?"
            ),
            expected_source_ids=["4-0"],
            expected_answer_concepts=[
                "Micrometer",
                "Prometheus",
                "Grafana"
            ]
        ),

        EvaluationCase(
            id="kafka_troubleshooting_multi",
            question=(
                "How should I investigate Kafka consumers "
                "that are falling behind?"
            ),
            expected_source_ids=[
                "1-0",
                "2-0"
            ],
            expected_answer_concepts=[
                "consumer lag",
                "processing latency",
                "downstream services",
                "database latency"
            ]
        ),
    ]