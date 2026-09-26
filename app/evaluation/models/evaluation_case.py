from pydantic import BaseModel, Field


class EvaluationCase(BaseModel):
    id: str

    question: str

    expected_source_ids: list[str] = Field(
        default_factory=list
    )

    expected_answer_concepts: list[str] = Field(
        default_factory=list
    )