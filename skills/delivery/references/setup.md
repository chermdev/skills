# Setup

Use this mode for `$delivery setup` or when the user explicitly asks to configure structured delivery in a repository.

## Discover before asking

Inspect read-only signals first:

- nearest `AGENTS.md` or `CLAUDE.md` and linked planning/domain documents;
- Git remotes, hosting provider, branch conventions, monorepo boundaries, and existing worktrees;
- existing plans, specs, ADRs, handoffs, backlog files, issue references, and commit conventions;
- package scripts, test frameworks, database/migration tools, browser tooling, and CI checks;
- available and authenticated tracker tools or connectors such as GitHub, GitLab, Linear, Plane, Jira, or a custom system;
- existing projects, teams, states, labels, and issue mappings when read access is available.

Do not mutate trackers or create repository files during discovery.

## Propose a routing matrix

For each artifact type, recommend one canonical source and zero or more mirrors:

- roadmap or initiatives;
- executable features;
- public bugs or support reports;
- pull requests and review;
- runtime handoff;
- detailed acceptance evidence.

Git Markdown is usually the canonical source for executable contracts and evidence because it versions with code. An external tracker is often canonical for priority, assignment, and cross-team visibility. These are defaults to evaluate, not fixed rules.

## Ask only unresolved decisions

Batch the smallest set of questions that materially changes the contract. Include a recommended answer and explain the tradeoff. Typical unresolved decisions are:

- canonical tracker and mirrors for each artifact type;
- team/project, state, and label mappings;
- planning root and documentation location;
- approval boundaries for implementation, tracker writes, deployment, and rollout;
- whether an existing backlog should be migrated now or preserved as legacy;
- repository-specific verification gates not discoverable from scripts or CI.

Support one tracker, several trackers with separate responsibilities, or Git files only. If a requested tracker is unavailable or unauthenticated, configure the intended routing and record the external setup as pending; never invent IDs.

## Materialize the contract

After the user approves the routing and local rules:

1. Create or update `.github/plans/config.yaml` from `assets/config-template.yaml`.
2. Generate a short `.github/plans/README.md` from `assets/readme-template.md`; keep generic behavior in this skill.
3. Create missing `INDEX.md`, `handoff.md`, templates, and optional legacy/evidence records from `assets/`.
4. Add one concise pointer to the nearest agent instruction file. Preserve its existing product and verification rules.
5. Migrate existing state only when approved. Link instead of copying checklists.
6. Create tracker projects, states, labels, or issues only when explicitly authorized and the configured provider is available.

Setup is idempotent: preserve existing decisions and active records, show meaningful differences, and change only approved configuration. Never replace a non-empty plan, handoff, or backlog with a template.

## Import or change tracker strategy

When Linear, Plane, GitHub, or another tracker already contains work, begin with a read-only inventory. Collect projects, initiatives, issues, relationships, statuses, labels, owners, dates, descriptions, and stable provider IDs/URLs. Then:

1. Match existing Git plans by provider reference first, then by outcome and scope. Treat title similarity alone as a candidate, not a match.
2. Classify each external item as initiative, executable feature, bug, decision, operational task, completed history, or out of scope.
3. Reconstruct dependency edges from native blockers, parent/child relationships, project ordering, and explicit description links. Mark inferred edges as proposals.
4. Propose one of three strategies per artifact type:
   - **Move canonical state to Git:** import local records and leave the external item unchanged unless the user authorizes a backlink, label, closure, or archive.
   - **Hybrid:** Git owns executable scope/evidence; the tracker owns priority, assignment, dates, or team coordination.
   - **Tracker canonical:** keep external scope authoritative and create only the local execution detail needed beside the code.
5. Present counts, duplicates, ambiguous mappings, status conversions, unsupported fields, and the proposed file tree before writing.
6. After approval, create local records with `external_refs` provenance. An external “done” status does not make a local feature `completed` unless the repository's completion evidence is available; otherwise import it as historical or `draft` with the gap recorded.

Never delete, close, archive, relabel, or comment on external work as an implicit part of import. Those are separate authorized mirror actions.

## Stage imported work for grooming

Setup imports provenance and routing, not invented implementation scope. For confidently matched external initiatives, create or update an initiative shell with `status: draft`, `planning_state: intake`, its stable `external_refs`, and an intake summary. Leave its feature sequence empty by default.

Attach external tickets as intake candidates by stable ID and URL. Do not create one local feature per ticket merely because the provider calls it an issue. Create a canonical feature during setup only when the external item already describes an independently valuable vertical delivery, repository evidence supports the mapping, and the user approves the proposed import.

Record ambiguous mappings, missing intent, and required repository analysis as grooming questions. Preserve the provider's original state separately when it does not map safely to the local vocabulary. `$delivery plan` resolves the intake with repository exploration and user decisions before creating executable features.

## Completion criteria

Setup is complete when:

- every artifact type has a declared canonical source;
- mirrors and pending external configuration are explicit;
- imported records retain stable external references and unresolved mappings;
- local paths and verification gates are recorded once;
- agent instructions point to `$delivery` and the local manifest;
- generated files resolve and no existing state was silently overwritten;
- the dashboard can distinguish imported intake from executable work;
- the user can continue with `$delivery plan`, or with `$delivery next` only when an approved feature already exists.
