from app import DocumentService
from app.config import settings
from app.models import Document, SearchRequest



def main() -> None:

    print(f"Starting {settings.app_name}")

    documents = [
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
        ),
    ]

    request = SearchRequest(
        keyword="kafka lag",
        threshold=0.80,
        top_k=2
    )

    service = DocumentService()

    results = service.search(
        documents=documents,
        request=request
    )

    print("\nSearch results:")

    for document in results:
        print(
            f"{document.text} - {document.score}"
        )


if __name__ == "__main__":
    main()