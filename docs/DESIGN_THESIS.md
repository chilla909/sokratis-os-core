# Design thesis: a human-authority kernel for AI-assisted systems

## Problem

Many AI projects focus on model capability, tool access, or autonomous execution.
Those are important, but they do not by themselves answer four governance
questions:

1. What exactly is the work?
2. Which domain and risk boundary does it belong to?
3. Who may approve the next consequential action?
4. What evidence is needed before the result can be trusted?

Without explicit answers, an AI system can become difficult to inspect,
reproduce, or safely reuse across different areas of life and work.

## Thesis

A reliable AI-assisted system should separate:

- the human's intent from the model's proposal;
- the domain context from global shared memory;
- approval from execution;
- execution from verification;
- the governance contract from the provider that performs the work.

Sokratis-OS expresses that separation as a small, provider-neutral kernel. The
same contract can support distinct personal, learning, research, and business
domains while keeping authority, evidence, and context boundaries explicit.

## Four design boundaries

### 1. Human authority

Models and adapters may propose or perform work, but high-risk transitions
require explicit approval evidence. The system should not silently turn model
output into authorization.

### 2. Domain isolation

Life, learning, and business/trading work may share a governance contract without
sharing all data or policies. Domain context should be passed deliberately by an
integration, not inherited through an uncontrolled global memory.

### 3. Evidence-bearing state

A state change is not merely a label. Approval, execution, and verification
carry evidence references so that a later reviewer can reconstruct what happened.

### 4. Provider neutrality

The governance contract should survive changes in models, vendors, runtimes, and
user interfaces. Provider-specific authentication, permissions, persistence,
and observability belong at the adapter boundary.

## What is and is not claimed

Sokratis-OS does not claim that state machines, approval gates, evidence, or audit
logs are individually novel. The differentiating proposal is a deliberately
small, testable governance kernel that combines them with domain separation for
human-led AI operating systems.

The public core is an early reference implementation. Its value must be tested
through real integrations, external review, and contributor feedback.

## Relation to the public package

The current package implements:

- immutable work items;
- explicit state transitions;
- evidence requirements;
- a provider-neutral execution boundary;
- a dependency-free reference adapter.

It does not yet implement domain storage, identity, permissions, persistence,
or a full agent runtime. Those remain integration concerns and future research
areas.

## Open questions

- How should domain context be represented without forcing one storage model?
- Which evidence formats work across code, data, and human decisions?
- How should policy differences between domains be tested?
- Which integrations create enough value to justify additional abstractions?
