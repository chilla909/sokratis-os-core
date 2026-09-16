# Adapter contract

The core workflow does not execute external work itself. An adapter connects the
contract to a provider, tool, or runtime.

## Required boundary

An adapter implements two operations:

- execute an approved WorkItem and return it in EXECUTED state;
- verify an executed WorkItem and return it in VERIFIED state.

Both operations must attach evidence. The core remains responsible for checking
that the state transition is legal.

## Minimal example

~~~python
from public_core import InMemoryAdapter, State, WorkItem

item = WorkItem("demo-1", "Review a proposed change", risk="high")
item = item.transition(State.PLANNED)
item = item.transition(State.APPROVED, ["human-approval.md"])

adapter = InMemoryAdapter()
item = adapter.execute(item)
item = adapter.verify(item)
~~~

The in-memory adapter is intentionally simple. It demonstrates the contract
without network access, credentials, persistence, or vendor dependencies.

## Integration responsibilities

A real adapter must define its own:

- authentication and authorization;
- isolation and resource limits;
- retries and failure handling;
- persistence and retention;
- logging and observability;
- mapping from external results to evidence references.

Those concerns are deliberately outside this small public core.
