from app.rag.services.text_chunker import TextChunker


def test_chunking_with_overlap():

    text = " ".join(
        f"word{i}"
        for i in range(1, 101)
    )

    chunker = TextChunker(
        chunk_size=20,
        overlap=5
    )

    chunks = chunker.chunk(text)

    assert len(chunks) > 1

    print()

    for index, chunk in enumerate(chunks):
        print(
            f"Chunk {index}: {chunk}"
        )