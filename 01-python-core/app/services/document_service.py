from app.models import Document, SearchRequest
from app.repositories import DocumentRepository


class DocumentService:

    def __init__(
        self,
        repository: DocumentRepository
    ) -> None:
        self.repository = repository

    def search(
        self,
        request: SearchRequest
    ) -> list[Document]:

        documents = self.repository.find_all()

        words = request.keyword.lower().split()

        filtered_documents = [
            document
            for document in documents
            if document.score >= request.threshold
            and self._matches(document, words)
        ]

        return sorted(
            filtered_documents,
            key=lambda document: document.score,
            reverse=True
        )[:request.top_k]

    def get_documents(
        self
    ) -> list[Document]:

        return self.repository.find_all()

    @staticmethod
    def _matches(
        document: Document,
        words: list[str]
    ) -> bool:

        text = document.text.lower()

        return all(
            word in text
            for word in words
        )