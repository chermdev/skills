---
name: saas-architecture
description: Design or review multi-tenant SaaS identity, isolation, onboarding, lifecycle, quotas, metering, and operations. Use when tenant boundaries or SaaS operating models change, not for every feature in a SaaS repository.
---

# SaaS Architecture

Treat the tenant as an explicit security and operational boundary. Start with the customer's required isolation, workload, lifecycle, and service tier rather than choosing a hosting vendor.

## Establish the tenant contract

1. Distinguish user identity, organization membership, active tenant, roles, entitlements, and resource ownership. Users may belong to multiple tenants.
2. Resolve tenant context from authenticated, authorized state. A request header, URL, domain, or body may select a tenant but cannot prove permission to act in it.
3. Define how context reaches data access, background jobs, cache, files, search, and external calls. Missing or mismatched context must fail closed on tenant-owned operations.
4. Separate control-plane capabilities (provisioning, subscriptions, entitlements, lifecycle) from application operations conceptually. Separate deployments only where justified.
5. Compare pooled, siloed, and hybrid isolation against confidentiality, capacity, cost, and operational requirements. A tier label is not an isolation guarantee.

## Isolation assessment

| Surface | Required decision and evidence |
| --- | --- |
| Data | Tenant ownership and access enforced at a shared boundary; constraints and privileged paths included |
| Cache | Keys and invalidation include every authorization-relevant dimension; identity changes do not reuse another tenant's result |
| Storage/downloads | Object ownership, list access, signed-link scope and expiry, export lifecycle |
| Jobs/events | Context derived from trusted producer state, validated on execution, retained through retries and dead letters |
| Search/AI retrieval | Tenant filtering before disclosure, indexes and derived data isolated, citations and cached responses checked |
| Telemetry | Tenant-aware diagnostics with access controls and bounded cardinality; no secrets or unneeded personal data |

Do not rely solely on developers remembering a query filter. Prefer centrally enforced, testable scoping with defense in depth supported by the datastore and runtime. Inventory admin/bypass paths separately.

## Lifecycle and fairness

- Make provisioning restartable: stable tenant ID, explicit states, idempotent steps, partial-failure recovery, and compensation where possible.
- Define membership revocation, suspension, reactivation, offboarding, retention, exports, and deletion of derived copies.
- Distinguish billing records from authorization decisions. State how entitlement updates propagate and what happens when the billing provider is unavailable.
- Bound per-tenant concurrency, storage, request rate, and expensive operations where noisy-neighbor risk exists. Test a busy tenant alongside an ordinary one.
- Attribute usage with stable event IDs and reconciliation; define duplicate, delayed, and corrected usage semantics before charging.

## Verification and output

Produce an isolation matrix, lifecycle decisions, exceptions, and acceptance evidence for two tenants plus multi-membership and revoked membership. Include manipulated tenant/resource identifiers, background execution, privileged access, and cache reuse. A successful login or happy-path query does not establish isolation.

Keep requirements vendor-neutral. Ask the project's technology capability to implement the selected enforcement and report its limitations. Use existing planning and architecture records; do not provision services or change subscriptions from a design request.

Read [tenant scenarios](references/tenant-scenarios.md) for detailed adversarial checks and [sources](references/sources.md) for provenance and the book-analysis boundary.

