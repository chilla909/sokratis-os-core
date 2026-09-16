# Sokratis-OS

A provider-neutral control plane for reliable AI-assisted work.

## Status

This is an experimental public-edition candidate. It is a small, runnable reference core extracted from the longer-running Sokratis-OS project. The public edition focuses on the reusable control-plane layer: explicit state, approval gates, evidence, and verification.

It does not claim public adoption, production readiness, or community scale.

## Why this exists

AI-assisted work becomes easier to trust when the system can answer four questions:

1. What is the current task?
2. What may happen next?
3. Which actions require approval?
4. What evidence proves that the result was checked?

Sokratis-OS makes those questions explicit in a provider-neutral workflow contract.

## What is included

- A deterministic work-item state machine.
- Explicit evidence requirements for approval, execution, and verification.
- A minimal Python reference implementation.
- Maintainer documentation and CI.
- A clear boundary between reusable public concepts and private project material.

## What is intentionally excluded

The public edition contains no personal data, credentials, private prompts, financial or trading logic, runtime state, session data, local paths, or private operational history.

## Quick start

~~~text
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
~~~

Then inspect examples/minimal_task.json and docs/ARCHITECTURE.md.

## Project history

Sokratis-OS began as a broader private project and accumulated real development history before this public-edition candidate was prepared. The public edition is a sanitized, reusable extraction of the control-plane ideas, not an unrelated replacement and not a manufactured activity history. See docs/PROJECT_HISTORY.md.

## Roadmap

- Add a provider-neutral adapter interface.
- Add structured decision records.
- Add more property-based and failure-path tests.
- Document interoperability with external coding agents.
- Gather feedback before committing to a larger API.

## Contributing

Please read CONTRIBUTING.md before opening an issue or pull request. Small, test-backed changes are preferred.

## License

MIT. See LICENSE.
