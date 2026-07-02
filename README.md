# embedding-cost-plan

> Estimate embedding job notes for batch size, retry, and cost cap gaps.

## Quick start Overview

Estimate embedding job notes for batch size, retry, and cost cap gaps. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 41

Accepts embedding job plan. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 41

```bash
python -m pip install -e ".[dev]"
embedding-cost-plan examples/sample.txt
embedding-cost-plan examples/sample.txt --json --fail-on medium
python -m embedding_cost_plan --help
```

## Rule Surface 41

| Rule | Severity | Meaning |
|---|---:|---|
| `huge-documents` | high | large embedding job detected |
| `missing-cost-cap` | medium | cost cap missing |
| `retry-forever` | low | retry is unbounded |

## Validation Notes 41

```bash
ruff check .
pytest
python -m embedding_cost_plan --help
```

Example risky input:

```text
documents 5000000 batch_size unknown cost_cap none retry forever
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
