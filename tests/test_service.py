from fastapi.testclient import TestClient

from agentic_mlops_foundry.api import app
from agentic_mlops_foundry.eval_gate import evaluate_response
from agentic_mlops_foundry.runtime import AgentResponse


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_agent_run_endpoint_passes_eval() -> None:
    response = client.post("/agent/run", json={"task": "draft an agent deployment checklist"})

    assert response.status_code == 200
    body = response.json()
    assert body["eval_passed"] is True
    assert body["traces"]


def test_eval_gate_rejects_low_confidence() -> None:
    result = evaluate_response(AgentResponse(output="Draft answer", confidence=0.2, traces=[]))

    assert result.passed is False
    assert "Confidence" in result.reason

