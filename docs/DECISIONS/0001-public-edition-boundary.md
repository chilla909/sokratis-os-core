# ADR-0001: Publish a sanitized public core

- Status: accepted
- Date: 2026-09-16
- Scope: public repository

## Context

The broader Sokratis-OS project contains a real private development history and
multiple domains. Some of that material includes personal, financial, trading,
operational, and runtime information that is not suitable for public release.

The reusable governance/control-plane idea is useful beyond those private
domains. A public edition should therefore expose the safe technical boundary
without publishing the private source repository or its full history.

## Decision

Publish Sokratis-OS Core as a clean, sanitized public snapshot.

The public edition must:

- contain only provider-neutral code, tests, examples, and safe documentation;
- describe its private-project lineage explicitly;
- avoid claiming that private work was public activity;
- record all future public changes through the normal open-source workflow;
- preserve the private source repository as the source of private project history.

## Consequences

Positive:

- private data and operational history remain protected;
- the public core is focused, portable, and independently testable;
- the public design thesis can be evaluated on its own merits.

Trade-off:

- the public Git history begins with the publication snapshot;
- the private history is documented as provenance but cannot be independently
  inspected by public readers;
- public adoption and contributor evidence must be built from this point onward.

## Rejected alternatives

- publishing the private repository unchanged;
- copying sensitive history into the public repository;
- fabricating historical commits or dates;
- presenting the public snapshot as an already established public project.
