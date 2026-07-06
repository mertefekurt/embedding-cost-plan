# Embedding Cost Plan

![Embedding Cost Plan cover](assets/readme-cover.svg)

> Estimate embedding job notes for batch size, retry, and cost cap gaps

![stack](https://img.shields.io/badge/stack-Python-b45309?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-be185d?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-4b5563?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-2563eb?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | embedding systems |
| Command | `embedding-cost-plan` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `huge-documents` | high | large embedding job detected |
| `missing-cost-cap` | medium | cost cap missing |
| `retry-forever` | low | retry is unbounded |

## Try it locally

```bash
python -m pip install -e ".[dev]"
embedding-cost-plan examples/sample.txt
embedding-cost-plan examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m embedding_cost_plan --help
```
