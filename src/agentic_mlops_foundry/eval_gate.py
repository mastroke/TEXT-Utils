from dataclasses import dataclass

from agentic_mlops_foundry.runtime import AgentResponse


@dataclass(frozen=True)
class EvalResult:
    passed: bool
    score: float
    reason: str


def evaluate_response(response: AgentResponse, min_confidence: float = 0.7) -> EvalResult:
    if response.confidence < min_confidence:
        return EvalResult(
            passed=False,
            score=response.confidence,
            reason="Confidence below release threshold.",
        )

    if "evaluate" not in response.output.lower():
        return EvalResult(
            passed=False,
            score=response.confidence,
            reason="Response did not mention evaluation.",
        )

    return EvalResult(
        passed=True,
        score=response.confidence,
        reason="Response passed confidence and evaluation checks.",
    )

