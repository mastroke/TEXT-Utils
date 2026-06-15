from fastapi import FastAPI
from pydantic import BaseModel, Field

from agentic_mlops_foundry.eval_gate import evaluate_response
from agentic_mlops_foundry.runtime import AgentRuntime

app = FastAPI(title="Agentic MLOps Foundry", version="0.1.0")
runtime = AgentRuntime()


class AgentRequest(BaseModel):
    task: str = Field(min_length=1, max_length=2000)


class AgentRunResponse(BaseModel):
    output: str
    eval_passed: bool
    eval_score: float
    eval_reason: str
    traces: list[str]


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/agent/run")
def run_agent(request: AgentRequest) -> AgentRunResponse:
    response = runtime.run(request.task)
    eval_result = evaluate_response(response)
    return AgentRunResponse(
        output=response.output,
        eval_passed=eval_result.passed,
        eval_score=eval_result.score,
        eval_reason=eval_result.reason,
        traces=response.traces,
    )

