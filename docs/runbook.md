# Deployment Runbook

## Pre-release Checks

- CI tests pass.
- Evaluation gate passes on representative prompts.
- Tool permissions are reviewed.
- Rollback image is available.

## Local Container

```bash
docker build -t agentic-mlops-foundry .
docker run -p 8000:8000 agentic-mlops-foundry
```

## Incident Response

- Disable expanded tool permissions first.
- Roll back to the previous image if evaluation failures increase.
- Preserve traces for review.
- Add a regression test before re-enabling the failed path.

