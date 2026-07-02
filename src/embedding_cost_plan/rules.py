from __future__ import annotations

from embedding_cost_plan.models import Rule

PROJECT_NAME = 'embedding-cost-plan'
SUMMARY = 'Estimate embedding job notes for batch size, retry, and cost cap gaps.'
SAMPLE_RISK = 'documents 5000000 batch_size unknown cost_cap none retry forever'
SAMPLE_CLEAN = 'documents 50000 batch_size 100 cost_cap 200 retry 3'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='huge-documents',
        severity='high',
        pattern='documents\\s+[5-9][0-9]{6,}',
        message='large embedding job detected',
        recommendation='estimate cost before run',
    ),
    Rule(
        code='missing-cost-cap',
        severity='medium',
        pattern='cost_cap\\s+(none|missing|unknown)',
        message='cost cap missing',
        recommendation='set budget limit',
    ),
    Rule(
        code='retry-forever',
        severity='low',
        pattern='retry\\s+forever',
        message='retry is unbounded',
        recommendation='use bounded retries',
    ),
)
