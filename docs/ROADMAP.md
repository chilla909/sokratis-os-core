# Roadmap

The roadmap is organized around small, testable milestones.

## M0: public reference core

Status: complete.

- immutable WorkItem and State types;
- deterministic transition rules;
- evidence gates;
- failure-path tests;
- runnable demo;
- CI and contributor documentation.

## M1: adapter contract

Goal: allow external tools to provide execution and verification without coupling
the core to a vendor.

Acceptance criteria:

- a documented adapter protocol;
- one in-memory reference adapter;
- tests for successful, rejected, and failed execution;
- no provider-specific dependency in the core package.

## M2: structured decision records

Goal: represent why a transition occurred.

Acceptance criteria:

- typed decision records;
- actor and timestamp fields;
- serializable evidence references;
- backwards-compatible examples.

## M3: evaluation fixtures

Goal: make workflow behavior easy to compare across implementations.

Acceptance criteria:

- synthetic fixtures;
- expected transition outcomes;
- documented evaluation procedure;
- repeatable CI execution.

## M4: integration guidance

Goal: show how the contract can be embedded into real maintainer workflows.

Potential integrations include pull-request review, issue triage, and release
preparation. Each integration must document its own permissions and security
assumptions.

Changes to the public API should remain small until real users and contributors
provide evidence that a larger abstraction is needed.
