---
name: distributed-systems
description: Design or review operations crossing processes, services, queues or replicas where partial failure, retries, ordering, consistency or overload matter. Use for distributed guarantees; do not introduce distributed infrastructure for ordinary local operations.
---

# Distributed Systems

Make guarantees explicit at each boundary. A successful local transaction or an exactly-once transport claim does not establish an exactly-once business effect across systems.

## Reason from an operation

1. Identify the operation's invariant, participants, authoritative state, external effects and observable completion state.
2. Write the event order for success, delay, duplicate, out-of-order delivery, process crash, partition and recovery.
3. Choose the required consistency per operation. State which stale reads are tolerable and what must remain safe during failover.
4. Define stable operation identities, atomic claims, durable progress and replay semantics. Use transactional coordination within one store where supported; identify gaps across stores.
5. Bound latency and work using deadlines, backpressure, retry budgets and resource isolation. Choose these from workload and failure impact rather than copied constants.
6. Specify reconciliation and operator recovery for outcomes the caller cannot determine.

## Protocol criteria

- A durable outbox can coordinate a local state change and event publication, but consumers still need duplicate handling.
- An inbox or idempotency record must be coordinated with its local effect. Marking an event done before a non-atomic external call can lose work; marking afterward can duplicate it.
- External side effects require provider idempotency, operation lookup, reconciliation, or explicit compensating actions. Do not claim a local deduplication table solves every crash window.
- Order only as broadly as the invariant requires. Use sequence/version checks when stale events could overwrite newer state.
- Expiring a distributed lock does not stop an old worker. Evaluate fencing tokens or conditional writes where stale ownership can corrupt state.
- Compensation is a business action with its own failure/retry semantics, not a universal rollback.
- Read replicas and caches may lag. Define read-your-writes behavior when the user must observe a completed change.
- A partition-related consistency/availability decision does not mean choosing two properties permanently from a slogan.

## Avoid unnecessary infrastructure

Keep a local atomic operation local when it meets the requirements. Use services, queues, replication and partitioning for measured workload, ownership or reliability needs. Identify operational cost and the threshold that would justify a deferred mechanism.

## Output and verification

Deliver the invariant, protocol/event sequence, guarantees and non-guarantees, recovery path and failure-injection checks. Exercise crash windows and duplicate execution in an authorized test environment, not against live customers by default.

Read [sources](references/sources.md) for data-systems and resilience provenance. Use datastore and runtime specialists for verified implementation semantics when available.

