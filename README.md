# Agent Security Radar

[![Validate radar catalog](https://github.com/jearthliu/agent-security-radar/actions/workflows/validate.yml/badge.svg)](https://github.com/jearthliu/agent-security-radar/actions/workflows/validate.yml)

A practical research radar for turning agent-security papers and incidents into engineering controls.

## Latest radar

**[2026-07-26 · Authorization, malicious issues, jailbreak evaluation, and RAG salience](reports/2026-07-26.md)**

Five direct-source papers are mapped to the agent lifecycle with facts, engineering interpretation, and explicit unknowns.

## Use the repository

| Resource | Purpose |
|---|---|
| [Latest report](reports/2026-07-26.md) | A reviewed seven-day radar with exactly five items |
| [Risk taxonomy](docs/risk-taxonomy.md) | Threats and controls across the agent lifecycle |
| [Research method](docs/research-method.md) | Source, inclusion, evidence, and stop rules |
| [Paper catalog](data/papers.json) | Machine-readable metadata for reviewed papers |
| [Catalog schema](data/papers.schema.json) | JSON Schema for structure and lifecycle vocabulary |
| [Report template](templates/radar-report.md) | Reusable daily or weekly format |
| [Catalog validator](scripts/validate_catalog.py) | Lightweight structural validation |
| [Validation tests](tests/test_validate_catalog.py) | Regression coverage for date and lifecycle rules |
| [Contributing](CONTRIBUTING.md) | How to propose a paper or correction |

## Scope

The radar tracks risks created when AI agents read untrusted content, call tools, retain memory, coordinate with other agents, or act in external systems.

| Area | Core question |
|---|---|
| Prompt injection | Can untrusted content redirect the agent? |
| Tool use | Is every capability scoped, authorized, and auditable? |
| Memory and retrieval | Can poisoned, true-but-misleading, or sensitive context persist? |
| Multi-agent systems | Can authority or misinformation propagate between agents? |
| Data security | Can secrets cross an unintended boundary? |
| Execution safety | Does uncertainty stop real-world actions? |

## Lifecycle model

```text
Input → Context → Planning → Tool selection → Authorization
      → Execution → External state → Reconciliation → Memory
```

Findings are mapped to one or more stages rather than grouped under an undifferentiated “AI safety” label.

## Editorial rules

- Prefer papers, advisories, repositories, and incident reports from direct sources.
- Keep a fixed research window and avoid backfilling weak items to reach a count.
- Separate source-reported facts, engineering interpretation, and unknowns.
- Do not treat benchmark performance as production safety.
- Link each recommended control to a concrete risk and lifecycle stage.
- Keep consequential actions fail-closed when identity, authorization, data, or external state is uncertain.

## Validate the catalog

```bash
check-jsonschema --schemafile data/papers.schema.json data/papers.json
python3 -m unittest discover -s tests -v
python3 scripts/validate_catalog.py data/papers.json
```

The validator checks structure, unique identifiers, direct HTTPS sources, and the exact-five invariant used by the current public report.

> Direct sources first. Facts, inference, and unknowns stay separate.

## License

- Code, tests, workflows, and schema implementation: [Apache-2.0](LICENSE)
- Reports, catalog data, templates, and research documents: [CC BY 4.0](CONTENT_LICENSE.md)
