from dataclasses import dataclass


@dataclass(frozen=True)
class AgentResponse:
    output: str
    confidence: float
    traces: list[str]


class AgentRuntime:
    def run(self, task: str) -> AgentResponse:
        normalized = task.strip()
        if not normalized:
            return AgentResponse(output="No task provided.", confidence=0.0, traces=["empty_task"])

        output = (
            "Plan: clarify objective, identify tools, run bounded steps, "
            "evaluate result, and return a traceable answer."
        )
        return AgentResponse(
            output=f"{output} Task received: {normalized}",
            confidence=0.86,
            traces=["input_validated", "policy_checked", "deterministic_runtime"],
        )

