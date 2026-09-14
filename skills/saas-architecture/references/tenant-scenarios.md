# Tenant scenarios

Use these checks when the affected feature crosses the named surface. Translate them to the project's actual enforcement boundary; a hypothetical design is not an executed test.

## Identity and context

- A user belongs to tenant A only and selects tenant B in a path/header/body. Confirm the server rejects the selection before accessing B's data.
- A user belongs to A and B with different roles. Confirm changing active tenant cannot carry A's stronger role into B.
- Revoke membership during an active session. Define when sessions, authorization caches and queued jobs observe revocation; test the promised boundary.
- Execute an ordinary tenant-owned operation without context. Confirm there is no fallback to an unrestricted query or default tenant.

## Persistence and derived data

- Reference a resource owned by B while creating a record in A. Test the ownership relation as well as the query filter.
- Repeat the operation with privileged administrative credentials in a controlled test. Identify intentional bypasses and the access/audit requirements around them.
- Warm a cache as A, then request the same resource identifier as B. Repeat after a role or membership change.
- Rebuild an index, export, or AI retrieval corpus. Check tenant scoping during ingestion, query, results, citations, deletion, and cached output.

## Files and asynchronous work

- Enqueue work for A and tamper with tenant/resource fields. Confirm the worker validates trusted context and operation ownership.
- Crash after creating an export but before recording completion. Retry without leaking or duplicating another tenant's artifact.
- Reuse an expired or incorrectly scoped download link. Check object reads and listing operations independently.
- Offboard a tenant while work is queued. State whether work is canceled or allowed under a narrow retained authority; test that decision.

## Lifecycle and fairness

- Interrupt provisioning after partial success, then replay the same request. Confirm one tenant and a recoverable lifecycle state.
- Delay or duplicate a billing/usage event. Confirm deterministic entitlement reconciliation and deduplicated usage attribution.
- Saturate one tenant's expensive workload in a test environment. Measure another tenant's latency/error behavior against the chosen service objective.
- Delete authoritative data and verify configured retention/deletion propagation into caches, exports, search, backups and logs without claiming immediate deletion where retention prevents it.

Report unsupported surfaces as not applicable, missing evidence as unverified, and actual failures as findings. Do not claim complete tenant isolation from this scenario list alone.
