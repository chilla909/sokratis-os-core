import pytest

from public_core import State, WorkItem, WorkflowError


def test_low_risk_item_reaches_verified() -> None:
    item = WorkItem("demo-1", "Review a proposed change")
    item = item.transition(State.PLANNED)
    item = item.transition(State.APPROVED, ["plan.md"])
    item = item.transition(State.EXECUTED, ["test-output.txt"])
    item = item.transition(State.VERIFIED, ["review.md"])

    assert item.state is State.VERIFIED
    assert item.evidence == (
        "plan.md",
        "test-output.txt",
        "review.md",
    )


def test_high_risk_item_cannot_skip_approval() -> None:
    item = WorkItem("demo-2", "Perform a sensitive operation", risk="high")
    item = item.transition(State.PLANNED)

    with pytest.raises(WorkflowError, match="invalid transition"):
        item.transition(State.EXECUTED, ["plan.md"])


def test_evidence_is_required_at_gates() -> None:
    item = WorkItem("demo-3", "Review a change").transition(State.PLANNED)

    with pytest.raises(WorkflowError, match="evidence is required"):
        item.transition(State.APPROVED)


def test_terminal_states_cannot_reopen() -> None:
    item = WorkItem("demo-4", "Close a task").transition(
        State.REJECTED, ["decision.md"]
    )

    with pytest.raises(WorkflowError, match="invalid transition"):
        item.transition(State.PLANNED)
