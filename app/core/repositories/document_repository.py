from app.core.models.document import Document


class DocumentRepository:

    def find_all(self) -> list[Document]:

        return [
            Document(
                id="1",
                text=(
                    "Kafka consumer lag occurs when consumers "
                    "process messages slower than producers publish them. "
                    "Monitor consumer lag and processing latency to "
                    "identify bottlenecks."
                ),
                score=0.92
            ),
            Document(
                id="2",
                text=(
                    "Kafka consumer performance can be affected by "
                    "slow downstream services, database latency, "
                    "insufficient consumer instances, or expensive "
                    "message processing."
                ),
                score=0.90
            ),
            Document(
                id="3",
                text=(
                    "RAG systems retrieve relevant documents using "
                    "vector similarity search and provide those documents "
                    "as context to a language model."
                ),
                score=0.87
            ),
            Document(
                id="4",
                text=(
                    "Spring Boot applications can expose operational "
                    "metrics using Actuator and Micrometer. Metrics can "
                    "be collected by Prometheus and visualized in Grafana."
                ),
                score=0.85
            ),
            Document(
                id="5",
                text=(
                    "Docker containers package applications and their "
                    "dependencies into portable runtime environments."
                ),
                score=0.80
            ),
            Document(
                id="6",
                text=(
                    "Incident ORDER-938271 failed while processing "
                    "a database request. The application reported "
                    "ORA-12541 because the Oracle listener was unavailable."
                ),
                score=0.90
            ),
        ]