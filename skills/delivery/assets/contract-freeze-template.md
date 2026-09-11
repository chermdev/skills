---
record_type: contract_freeze
plan: ../PLAN.md
features: []
status: draft
captured: YYYY-MM-DD
contract_revision: pending
approved_by: []
---

# Shared contract freeze

## Frozen contracts

- Exact schemas and discriminated types:
- RPC or command signatures:
- Query keys and read models:
- Exact DDL or migrations:

## Physical ownership

| Feature | File or module | Function/object | Write permission |
| ------- | -------------- | --------------- | ---------------- |

## Merge order

1. Shared contract/base:
2. Independent branch A:
3. Independent branch B:
4. Integration and QA:

## Parallel-safety gate

- [ ] Every dependency is `completed`.
- [ ] Physical ownership does not overlap.
- [ ] Merge order is explicit and safe.
- [ ] Each feature has independently verifiable QA.
- [ ] The window stays within configured WIP.
- [ ] Every write owner and required reviewer approved this record.

`shared_contracts_frozen` is true only while this record is `approved`, references every feature in
the window, and its contract revision remains current. A material contract change moves the record
to `superseded`, closes the parallel window, and schedules affected candidates serially in
dependency/priority order until a new freeze is approved.
