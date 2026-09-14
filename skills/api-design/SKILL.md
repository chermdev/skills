---
name: api-design
description: Design or review service APIs, commands, events, pagination, errors, idempotency, and compatibility for consumers. Use when an externally consumed contract changes; ordinary internal function edits do not require an API design review.
---

# API Design

Design from the consumer's operation and observable outcomes. Keep transport and framework decisions separate from semantic guarantees.

## Contract procedure

1. Identify callers, trust boundaries, operation ownership, latency needs, and compatibility obligations. Inspect existing conventions before adding a protocol.
2. Specify inputs, outputs, validation, authentication, resource-level authorization, and side effects. Define missing, null, empty, unknown and invalid values when they differ.
3. Define error categories and consumer recovery. Separate retryable failures, conflicts, invalid requests, and forbidden actions without exposing sensitive internals.
4. For mutations, define atomicity and what the caller can know after a timeout. Choose a stable operation identity when retries can duplicate effects.
5. Bound collections and expensive requests. Specify stable pagination/order, filtering, visibility, and behavior when records change between pages.
6. Assess changes against actual consumers: serialized shapes, meaning, defaults, error handling, generated clients, and supported old versions.
7. Show a successful interaction and a failure/retry interaction. Translate decisions into a schema or contract fixture using the repository's existing format.

## Idempotency contract

Define key scope (including caller/tenant and operation), request fingerprint, atomic claim, in-progress behavior, saved result, retention and expiry. Same key plus a different payload is a conflict; concurrent identical requests cannot both execute the side effect.

An idempotent endpoint does not make an external provider exactly-once. After a timeout, reconcile the stable operation with the provider or expose pending/unknown state. Define compensation separately.

For asynchronous work, distinguish accepted, processing, succeeded, failed, and canceled states only as needed. State how the caller observes progress. Events need a stable identity, producer ownership, schema evolution, and duplicate/out-of-order semantics.

## Compatibility criteria

- A new required field, changed meaning, stricter validation, or different default can break a consumer even if a schema validator passes.
- New enum values and additional fields are not automatically safe for every generated or strict client.
- Prefer an additive transition with old/new consumer checks, a usage-informed deprecation period, and an explicit retirement condition.
- Document authorization on the server boundary; hiding a control in a client is not access control.

## Output and verification

Deliver the contract, compatibility decisions, failure examples, and consumer/provider checks. Include concurrent duplicate submission, timeout after commit, invalid resource ownership, and pagination changes where relevant.

A design request does not authorize publishing an endpoint or changing consumers. Specialized security/data review may help, but this skill works without another installed skill. Read [sources](references/sources.md) for provenance.

