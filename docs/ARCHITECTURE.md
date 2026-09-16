# Architecture

Sokratis-OS is intentionally small in this public edition. The reference core
separates a work item from the systems that plan, execute, and verify it.

## Layers

1. Work contract: identity, objective, risk, state, and evidence.
2. Decision gate: explicit transitions and approval requirements.
3. Execution adapter: an external tool or provider performs the approved work.
4. Verification: tests, review, or other evidence is attached to the result.

The public core implements the first two layers. Adapters are deliberately left
outside the reference package so that the contract remains provider-neutral.

## Invariants

- State transitions are explicit and deterministic.
- Work items are immutable values.
- Approval, execution, and verification require evidence.
- Terminal states cannot be reopened.
- The core has no network, filesystem, credential, or vendor dependency.

## Non-goals

This package is not an agent framework, a scheduler, a credentials manager, or
a production security boundary. Integrations must add their own authentication,
authorization, isolation, and audit controls.
