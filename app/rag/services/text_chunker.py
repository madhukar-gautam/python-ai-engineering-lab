class TextChunker:

    def __init__(
        self,
        chunk_size: int = 50
    ) -> None:
        self.chunk_size = chunk_size

    def chunk(
        self,
        text: str
    ) -> list[str]:

        words = text.split()

        return [
            " ".join(
                words[i:i + self.chunk_size]
            )
            for i in range(
                0,
                len(words),
                self.chunk_size
            )
        ]