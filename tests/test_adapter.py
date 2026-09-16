import pytest

from public_core import (
    InMemoryAdapter,
    State,
    WorkItem,
    WorkflowError,
)


def approved_item() -> WorkItem:
    return WorkItem("adapter-1", "Review a proposed change").transition(
        State.PLANNED
    ).transition(State.APPROVED, ["approval.md"])


def test_in_memory_adapter_executes_and_verifies() -> None:
    adapter = InMemoryAdapter()
    item = adapter.execute(approved_item())
    item = adapter.verify(item)

    assert item.state is State.VERIFIED
    assert item.evidence == (
        "approval.md",
        "adapter:in-memory-execution",
        "adapter:in-memory-verification",
    )


def test_adapter_rejects_unapproved_execution() -> None:
    adapter = InMemoryAdapter()
    item = WorkItem("adapter-2", "Review a proposed change")

    with pytest.raises(WorkflowError, match="approved"):
        adapter.execute(item)


def test_adapter_rejects_unexecuted_verification() -> None:
    adapter = InMemoryAdapter()
    item = approved_item()

    with pytest.raises(WorkflowError, match="executed"):
        adapter.verify(item)
