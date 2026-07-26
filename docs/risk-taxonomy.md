# Agent Risk Taxonomy

## 1. Input and context

Risks: prompt injection, indirect instructions, malicious documents, hidden content, context confusion.

Controls: source labeling, content isolation, instruction hierarchy enforcement, suspicious-content detection.

## 2. Planning and tool selection

Risks: capability escalation, unsafe decomposition, excessive autonomy, tool confusion.

Controls: least-capability routing, explicit plans for consequential actions, policy checks before tool selection.

## 3. Authorization

Risks: stale consent, ambiguous authority, permission inheritance, cross-user action.

Controls: action-specific authorization, identity binding, expiry, human confirmation for consequential writes.

## 4. Execution

Risks: parameter manipulation, race conditions, partial execution, irreversible side effects.

Controls: schema validation, idempotency, precondition checks, dry-run support, bounded retries.

## 5. External state and reconciliation

Risks: treating request acceptance as completion, unknown terminal states, inconsistent local and external records.

Controls: terminal-state polling, authoritative readback, mismatch halt, explicit unknown state.

## 6. Memory and retrieval

Risks: memory poisoning, secret retention, tenant leakage, stale instructions.

Controls: provenance, retention limits, scoped namespaces, reviewable writes, deletion guarantees.

## 7. Multi-agent coordination

Risks: authority laundering, unverified delegation, cascading hallucinations, compromised peer agents.

Controls: signed task boundaries, independent verification, role separation, bounded delegation depth.

## Control principle

When identity, authorization, data freshness, or external state is uncertain, stop the consequential action and preserve the uncertainty for review.