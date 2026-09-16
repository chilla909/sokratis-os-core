# Architecture

Sokratis-OS is intentionally small in this public edition. The reference core
separates a work item from the systems that plan, execute, and verify it.

## Design position

The public package is the governance kernel of a broader operating-system idea.
It is not the complete Life-OS, Learning-OS, business/trading system, or agent
runtime.

The broader architecture treats domains as separate contexts that may share a
governance contract without sharing all data, permissions, or memory. The public
core documents that boundary but does not pretend to implement domain routing or
persistence yet.

## Layers

1. Work contract: identity, objective, risk, state, and evidence.
2. Decision gate: explicit transitions and approval requirements.
3. Execution adapter: an external tool or provider performs the approved work.
4. Verification: tests, review, or other evidence is attached to the result.
5. Domain integration: an external system supplies the intended domain context,
   permissions, persistence, and retention policy.

The public core implements the first four layers. The fifth remains an explicit
integration boundary.

## Invariants

- State transitions are explicit and deterministic.
- Work items are immutable values.
- Approval, execution, and verification require evidence.
- Terminal states cannot be reopened.
- The core has no network, filesystem, credential, or vendor dependency.
- The core does not silently claim authority for a model, provider, or domain.

## Non-goals

This package is not an agent framework, a scheduler, a credentials manager, a
domain database, or a production security boundary. Integrations must add their
own authentication, authorization, isolation, persistence, observability, and
retention controls.
