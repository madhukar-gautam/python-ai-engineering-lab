from app.evaluation.services.answer_evaluator import (
    AnswerEvaluator
)


def test_grounded_answer():

    evaluator = AnswerEvaluator()

    result = evaluator.evaluate(
        question="Why did ORDER-938271 fail?",
        context=(
            "ORDER-938271 failed because "
            "the Oracle listener was unavailable."
        ),
        answer=(
            "ORDER-938271 failed because "
            "the Oracle listener was unavailable."
        )
    )

    assert result["grounded"] is True