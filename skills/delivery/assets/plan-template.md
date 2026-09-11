---
plan_id: PLAN-SLUG
name: plan-slug
title: Outcome-oriented plan title
description: One-line outcome
portfolio_horizon: horizon-slug
status: proposed
planning_state: needs_grooming
rollout_state: gated
owner: unassigned
created: YYYY-MM-DD
updated: YYYY-MM-DD
depends_on_plans: []
required_features: []
tracker_project: null
external_refs: []
---

# Outcome-oriented plan title

## Outcome and rollout boundary

Describe what users or operators can do when implementation is complete.

## Context and constraints

Link to durable business, architecture, security, and rollout contracts.

## Intake and grooming

- Provider facts and candidate tickets:
- Repository evidence:
- Unresolved product intent:
- Next grooming action:

## Decisions

| Decision | Status | Rationale |
| -------- | ------ | --------- |

## Feature DAG

| Feature | Visible delivery | Depends on | Parallel candidate | Delivery | Planning |
| ------- | ---------------- | ---------- | ------------------ | -------- | -------- |

## Critical path

Describe dependency order and genuinely independent branches. `parallelizable_with` does not
authorize execution or reserve WIP. Name the contract-freeze record required before any parallel
window; without an approved current record, execute serially.

## Rollout

Record gates, safe defaults, migration/deployment order, rollback, and authorization boundary.

## Activation and next eligibility

Record the exact sequence: resolve blocking decisions, reconcile portfolio priority, approve plan
planning, assign plan owner, activate the plan, then approve/assign only the first dependency-ready
feature. Do not bulk-promote downstream features.

## Open decisions

List only decisions that materially change behavior or scope.

## Completion record

- Implementation completed:
- Final commit:
- Tracker:
- Rollout state:
- Remaining debt:
