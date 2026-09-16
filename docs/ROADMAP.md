# Roadmap

The roadmap follows the original Sokratis-OS direction: establish a small
governance kernel first, then add domain and provider integrations only when
real usage demonstrates that an abstraction is needed.

## M0: public reference core

Status: complete.

- immutable WorkItem and State types;
- deterministic transition rules;
- evidence gates;
- failure-path tests;
- runnable demo;
- CI and contributor documentation.

## M1: adapter contract

Status: complete.

- documented provider-neutral adapter protocol;
- dependency-free in-memory reference adapter;
- tests for successful, rejected, and invalid-state execution;
- no provider-specific dependency in the core package.

## M2: structured decision records

Goal: represent why a transition occurred.

Acceptance criteria:

- typed decision records;
- actor and timestamp fields;
- serializable evidence references;
- backwards-compatible examples.

## M3: explicit domain-context contract

Goal: make domain separation usable without coupling the core to a storage
engine or private data model.

Acceptance criteria:

- a minimal domain/context vocabulary;
- explicit handling of missing or conflicting context;
- tests proving that context is not silently inherited;
- documentation of integration-owned permissions and retention.

## M4: evaluation fixtures

Goal: make workflow behavior easy to compare across implementations.

Acceptance criteria:

- synthetic fixtures;
- expected transition outcomes;
- documented evaluation procedure;
- repeatable CI execution;
- checks for evidence completeness and illegal transitions.

## M5: integration guidance

Goal: show how the contract can be embedded into real maintainer, personal,
learning, and business workflows.

Potential integrations include pull-request review, issue triage, release
preparation, and domain-separated personal assistants. Each integration must
document its own permissions and security assumptions.

Changes to the public API should remain small until real users and contributors
provide evidence that a larger abstraction is needed.
