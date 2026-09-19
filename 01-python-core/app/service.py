from app.models import Document

def search_documents(
    documents: list[Document],
    keyword: str,
    threshold: float = 0.80,
    top_k: int = 2
) -> list[Document]:

    filtered = [
        document
        for document in documents
        if document.score >= threshold
        and keyword.lower() in document.text.lower()
    ]

    return sorted(
        filtered,
        key=lambda document: document.score,
        reverse=True
    )[:top_k]
