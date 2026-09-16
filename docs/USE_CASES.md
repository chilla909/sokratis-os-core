# Use cases

The core is useful when an AI-assisted workflow needs an explicit handoff
between intent, permission, action, and proof.

## Pull-request review

A review adapter can create a WorkItem from a pull request:

- objective: review the proposed change;
- risk: high when permissions, dependencies, or production behavior change;
- approval evidence: maintainer approval or review checklist;
- execution evidence: test results and the proposed patch;
- verification evidence: final review decision.

The adapter owns GitHub authentication and review permissions. The core only
defines the workflow contract.

## Documentation and refactoring

A coding assistant can use the same contract for a documentation or refactoring
task. Low-risk work may use a lightweight approval process; higher-risk changes
must leave explicit evidence before execution and verification.

## Data and automation pipelines

A pipeline can represent a transformation as a WorkItem and attach:

- the input schema;
- the planned transformation;
- the execution result;
- validation or comparison output.

The core does not store the data or run the pipeline. It makes the control
points inspectable.

## Provider comparison

Different model or agent providers can be evaluated against the same workflow
contract. This makes it possible to compare:

- plan quality;
- approval compliance;
- evidence quality;
- verification coverage;
- failure handling.

## Integration boundary

An integration should add authentication, authorization, isolation, persistence,
observability, and retention rules appropriate to its environment. The public
core deliberately does not pretend to solve those deployment concerns.
