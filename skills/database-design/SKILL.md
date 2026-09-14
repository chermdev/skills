---
name: database-design
description: Design or review data models, access patterns, constraints, transaction boundaries, indexes, and migration safety. Use when persistence semantics change or a data correctness problem needs analysis; do not prescribe a particular database or ORM.
---

# Database Design

Start with durable business invariants and observed access patterns. A schema that represents entities but cannot enforce the important concurrent operations is incomplete.

## Design procedure

1. List authoritative records, derived views, retention rules, tenant ownership, and read/write operations. Include volume, skew, latency, and freshness requirements when known.
2. Choose a model by relationship and query needs. Compare operational costs before adding another datastore; avoid polyglot persistence without a workload reason.
3. Express invariants using the datastore's supported constraints, atomic operations, and transaction boundaries. Application validation improves errors but may not protect against races.
4. Walk through two concurrent executions. State the actual isolation/consistency guarantees, conflict detection, lock scope, retry behavior, and abort conditions.
5. Design indexes from query predicates, ordering and representative distributions. Account for write cost, maintenance, storage, and tenant skew. Measure before claiming a speedup.
6. Make derived data rebuildable, with ownership, freshness expectations, reconciliation and deletion propagation.
7. Plan change and recovery before applying a migration.

## Concurrency decisions

- A read followed by a write is not automatically atomic. Show which mechanism prevents the invariant from being violated.
- A uniqueness check before insert cannot replace a race-safe uniqueness constraint or equivalent atomic claim.
- Distinguish row conflicts, lost updates, and invariants spanning multiple rows. A lock on one record does not necessarily protect a predicate.
- Retrying a transaction must not duplicate external effects. Keep external calls outside retried transactions or coordinate them using a durable protocol.
- Include tenant ownership in keys/relationships where needed to prevent cross-tenant references; a filter alone does not establish referential integrity.
- Verify the chosen engine and version's guarantees through official documentation before giving engine-specific commands.

## Migration contract

Use versioned migrations as the canonical change path when the repository requires them. Identify old/new application compatibility, lock and scan cost, backfill size, restart/checkpoint behavior, validation, and cutover order.

For a live schema rename or type change, consider expand -> compatible reads/writes -> bounded backfill -> verify -> switch readers -> retire old representation. Identify concurrent writes during backfill and how they cannot overwrite newer data.

Separate code rollback from data recovery. A backup needs a viable restore procedure and an understood recovery window; a reverse migration may be lossy. Destructive cleanup waits for the agreed compatibility and retention boundary.

## Output and verification

Return model/invariant decisions, representative operations, concurrency schedules, migration sequence, and concrete checks. State unknown load/engine details instead of inventing limits.

Validate with representative data and concurrent/failure cases where applicable. Do not execute production migrations, destructive transformations, or live load tests from a design request. Read [sources](references/sources.md) for adapted data-system criteria.

