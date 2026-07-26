# Research Method

## 1. Define the window first

Every report records a start time, end time, timezone, and search completion time. Publication date and event date are kept separate when they differ.

## 2. Build a candidate set

Preferred sources:

1. paper or advisory primary page;
2. official project repository or benchmark;
3. vendor security advisory or regulator publication;
4. incident report from the affected organization.

Secondary reporting may help discovery but does not replace the direct source.

## 3. Apply inclusion gates

An item is included only when it:

- falls inside the declared window;
- has a stable direct source;
- adds a distinct risk, method, benchmark, incident, or control;
- can be mapped to an agent lifecycle stage;
- supports at least one practical engineering implication.

A weak or duplicate item is not added merely to satisfy a target count.

## 4. Separate evidence layers

Each entry uses four labels:

- **Fact:** what the source directly states or reports.
- **Why it matters:** relevance to agent systems.
- **Engineering interpretation:** a reasoned control or design implication.
- **Unknown:** limits, missing replication, or deployment uncertainty.

Reported benchmark numbers remain source claims unless independently reproduced.

## 5. Map to lifecycle

```text
Input
  → Context / Retrieval
  → Planning
  → Tool selection
  → Authorization
  → Execution
  → External state
  → Reconciliation
  → Memory
```

This mapping prevents a model-level jailbreak result from being misreported as proof of end-to-end agent compromise, and prevents an API response from being treated as external completion.

## 6. Derive controls

Controls should identify:

- enforcement point;
- trusted decision maker;
- data or capability boundary;
- failure state;
- evidence needed to resume.

“Improve the prompt” is not a complete control when the risk involves external side effects.

## 7. Stop rules

The report remains incomplete when direct sources are missing, dates cannot be verified, selected items are duplicates, or required persistence fails. Research progress is not reported as publication success.