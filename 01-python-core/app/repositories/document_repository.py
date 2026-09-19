from app.models import Document


class DocumentRepository:

    def find_all(self) -> list[Document]:

        return [
            Document(
                id="1",
                text="Kafka architecture",
                score=0.92
            ),
            Document(
                id="2",
                text="Spring Boot",
                score=0.61
            ),
            Document(
                id="3",
                text="RAG architecture",
                score=0.87
            ),
            Document(
                id="4",
                text="Docker basics",
                score=0.45
            ),
            Document(
                id="5",
                text="Kafka consumer lag",
                score=0.95
            )
        ]