# Sokratis-OS

[![CI](https://github.com/chilla909/sokratis-os-core/actions/workflows/ci.yml/badge.svg)](https://github.com/chilla909/sokratis-os-core/actions/workflows/ci.yml)

A provider-neutral control plane for reliable AI-assisted work.

## What it does

Sokratis-OS makes the control loop around AI-assisted work explicit:

1. define the work;
2. plan the next step;
3. require approval where risk demands it;
4. execute through an external adapter;
5. attach evidence and verify the result.

The public edition is intentionally small. It provides a deterministic, immutable
workflow contract that other tools and providers can build around.

## 30-second demo

~~~text
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"
python -m public_core
pytest
~~~

The demo walks a high-risk work item through planning, approval, execution, and
verification. The tests cover the same contract and its failure paths.

## Why this exists

AI-assisted systems need a shared language for intent, risk, approval, and proof.
Without that contract, planning and execution can become difficult to inspect,
review, or reproduce.

Sokratis-OS separates the contract from any particular model, agent, provider,
runtime, or user interface.

## Included

- immutable work items with explicit state;
- deterministic transition rules;
- evidence requirements at approval, execution, and verification gates;
- a provider-neutral execution adapter contract;
- an in-memory adapter for examples and tests;
- runnable examples and tests;
- CI across supported Python versions;
- maintainer, security, contribution, and publication-boundary documentation.

## Possible uses

- pull-request review workflows;
- agent-assisted documentation or refactoring;
- data and automation pipelines;
- approval-aware internal tools;
- experiments comparing different AI providers against one contract.

See docs/USE_CASES.md and docs/ADAPTER_CONTRACT.md for concrete examples.

## Boundaries

This package is not an agent framework, scheduler, credentials manager, or
production security boundary. Integrations must provide their own authentication,
authorization, isolation, persistence, and audit controls.

The public edition contains no personal data, credentials, private prompts,
financial or trading logic, runtime state, session data, local paths, or private
operational history.

## Project history

Sokratis-OS began as a broader private project and accumulated real development
history before this public edition was prepared. The public repository is a
sanitized, reusable extraction of the control-plane layer. Its lineage is
documented openly without exposing the private source history.

## Status

Early-stage reference implementation. It makes no claim of broad adoption or
production readiness. Progress is measured through reproducible code, tests,
documentation, and real contributor feedback.

## Roadmap

See docs/ROADMAP.md. The adapter contract and in-memory reference adapter are
implemented; the next milestone is structured decision records.

## Contributing

Please read CONTRIBUTING.md before opening an issue or pull request. Focused,
test-backed changes are preferred.

## License

MIT. See LICENSE.
