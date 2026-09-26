class TextChunker:

    def __init__(
        self,
        chunk_size: int = 50,
        overlap: int = 10
    ) -> None:

        if chunk_size <= 0:
            raise ValueError(
                "chunk_size must be greater than 0"
            )

        if overlap < 0:
            raise ValueError(
                "overlap cannot be negative"
            )

        if overlap >= chunk_size:
            raise ValueError(
                "overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(
        self,
        text: str
    ) -> list[str]:

        words = text.split()

        if not words:
            return []

        chunks = []

        step = self.chunk_size - self.overlap

        for start in range(
            0,
            len(words),
            step
        ):

            end = start + self.chunk_size

            chunk_words = words[start:end]

            if not chunk_words:
                break

            chunks.append(
                " ".join(chunk_words)
            )

            if end >= len(words):
                break

        return chunks