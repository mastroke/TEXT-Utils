# ADR 0001: Require An Evaluation Gate

## Status

Accepted

## Context

Agent services can produce plausible but unsafe output. A release path needs a repeatable quality gate.

## Decision

All agent responses pass through an evaluation gate before they are treated as successful.

## Consequences

- Low-confidence responses are visible to callers.
- CI can exercise the evaluation contract.
- Future model providers can be swapped without removing the gate.

