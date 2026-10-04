import re


class AnswerEvaluator:

    def evaluate(
        self,
        question: str,
        context: str,
        answer: str
    ) -> dict:

        context_words = set(
            re.findall(
                r"\b\w+\b",
                context.lower()
            )
        )

        answer_words = set(
            re.findall(
                r"\b\w+\b",
                answer.lower()
            )
        )

        supported_words = (
            answer_words & context_words
        )

        grounded_ratio = (
            len(supported_words)
            / len(answer_words)
            if answer_words
            else 0
        )

        return {
            "grounded": grounded_ratio >= 0.5,
            "grounded_ratio": round(
                grounded_ratio,
                2
            )
        }