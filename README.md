# Sokratis-OS Core

[![CI](https://github.com/chilla909/sokratis-os-core/actions/workflows/ci.yml/badge.svg)](https://github.com/chilla909/sokratis-os-core/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A provider-neutral governance kernel for human-led AI systems.

Sokratis-OS treats reliable AI-assisted work as a governance problem, not only a
model problem. Work should cross explicit gates where intent, risk, authority,
action, evidence, and verification remain inspectable.

> A model may propose. An adapter may execute. Evidence determines what can be accepted.

## The core idea

The public core extracts the reusable control-plane layer from the broader
Sokratis-OS project. It defines a small, deterministic contract for moving work
from intake to planning, approval, execution, and verification.

The wider Sokratis-OS architecture was designed around separate Life-OS,
Learning-OS, and business/trading domains. The public package does not publish
those private domains. It publishes the domain-neutral governance kernel that
can support them without making provider, model, or personal data part of the
core.

## What makes this different

The individual mechanisms are deliberately familiar. The design contribution is
their combination as a small reusable boundary:

- human authority is explicit at approval gates;
- evidence is required before consequential state changes;
- domain separation is a system-level boundary, not an implicit shared memory;
- execution is delegated through provider-neutral adapters;
- the core is deterministic, immutable, portable, and dependency-light;
- integrations remain responsible for authentication, authorization, isolation,
  persistence, and retention.

This is not an agent framework, scheduler, credentials manager, or production
security boundary. It is the governance kernel around which such systems can be
built and evaluated.

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

## Included

- immutable work items with explicit state;
- deterministic transition rules;
- evidence requirements at approval, execution, and verification gates;
- a provider-neutral execution adapter contract;
- a dependency-free in-memory adapter;
- runnable examples and tests;
- CI across supported Python versions;
- maintainer, security, contribution, and publication-boundary documentation.

## Possible uses

- domain-aware personal assistants;
- AI-assisted pull-request review and release preparation;
- documentation and refactoring workflows;
- data and automation pipelines;
- approval-aware internal tools;
- experiments comparing different AI providers against one contract.

See docs/DESIGN_THESIS.md, docs/USE_CASES.md, and
docs/ADAPTER_CONTRACT.md for the design rationale and examples.

## Project lineage

Sokratis-OS was developed first as a private project with real iterative
history. At the time of the public-edition preparation, the private source
contained 71 commits dated 2026-08-16 through 2026-08-20.

The public repository starts with a clean publication snapshot dated
2026-09-16. This boundary is intentional: the private source contains personal,
financial, trading, operational, and runtime material that must not be
published. The public edition preserves the reusable control-plane idea without
claiming that private work was public activity.

See docs/PROJECT_HISTORY.md for the verified provenance summary and
docs/PUBLICATION_BOUNDARY.md for the publication rules.

## Status

Early-stage reference implementation. It makes no claim of broad adoption or
production readiness. Progress is measured through reproducible code, tests,
documentation, and real contributor feedback.

## Roadmap

See docs/ROADMAP.md. The adapter contract and in-memory reference adapter are
implemented. The next milestones are structured decision records, explicit
domain-context boundaries, and evaluation fixtures.

## Contributing

Please read CONTRIBUTING.md before opening an issue or pull request. Focused,
test-backed changes are preferred.

## License

MIT. See LICENSE.
