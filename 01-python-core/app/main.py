from app.models import Document
from app.service import search_documents

documents = [
    Document("1", "Kafka architecture", 0.92),
    Document("2", "Spring Boot", 0.61),
    Document("3", "RAG architecture", 0.87),
    Document("4", "Docker basics", 0.45),
Document("5", "Kafka consumer lag", 0.95)
]

result = search_documents(documents, "kafka")

for document in result:
    print(document.text, document.score)