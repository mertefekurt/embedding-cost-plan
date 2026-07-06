# Embedding Cost Plan

> A small command-line review pass for embedding systems.

![Embedding Cost Plan cover](assets/readme-cover.svg)

Estimate embedding job notes for batch size, retry, and cost cap gaps. In practice it is a narrow guardrail for model evaluation, traces, retrieval, and prompt review: one command, a concrete report, and very little ceremony.

## Signals in plain English

- `huge-documents` (high): large embedding job detected. Fix: estimate cost before run.
- `missing-cost-cap` (medium): cost cap missing. Fix: set budget limit.
- `retry-forever` (low): retry is unbounded. Fix: use bounded retries.

## Input and report

The reader accepts text, JSON, JSONL, or CSV. The default report is readable in a terminal or pull request; `--json` keeps the same findings available to automation.

## Demo

```bash
git clone https://github.com/mertefekurt/embedding-cost-plan.git
cd embedding-cost-plan
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
embedding-cost-plan examples/sample.txt
embedding-cost-plan examples/sample.txt --json
```

## Sanity checks

```bash
ruff check .
pytest
python -m embedding_cost_plan --help
```
