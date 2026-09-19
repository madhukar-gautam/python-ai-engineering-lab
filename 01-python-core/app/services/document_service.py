from app.models import Document, SearchRequest


class DocumentService:

    def search(
        self,
        documents: list[Document],
        request: SearchRequest
    ) -> list[Document]:

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