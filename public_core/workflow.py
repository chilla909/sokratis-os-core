"""Deterministic workflow primitives.

The module intentionally has no provider, network, filesystem, or runtime
dependencies. It is a small reference contract that can be adapted by other
systems.
"""

from dataclasses import dataclass, replace
from enum import StrEnum
from typing import Iterable


class State(StrEnum):
    INTAKE = "intake"
    PLANNED = "planned"
    APPROVED = "approved"
    EXECUTED = "executed"
    VERIFIED = "verified"
    REJECTED = "rejected"


class WorkflowError(ValueError):
    """Raised when a work item violates the workflow contract."""


_ALLOWED_TRANSITIONS = {
    State.INTAKE: frozenset({State.PLANNED, State.REJECTED}),
    State.PLANNED: frozenset({State.APPROVED, State.REJECTED}),
    State.APPROVED: frozenset({State.EXECUTED, State.REJECTED}),
    State.EXECUTED: frozenset({State.VERIFIED, State.REJECTED}),
    State.VERIFIED: frozenset(),
    State.REJECTED: frozenset(),
}
_EVIDENCE_STATES = frozenset(
    {State.APPROVED, State.EXECUTED, State.VERIFIED}
)
_RISKS = frozenset({"low", "medium", "high"})


@dataclass(frozen=True, slots=True)
class WorkItem:
    """An immutable task record with explicit state and evidence."""

    task_id: str
    objective: str
    risk: str = "low"
    state: State = State.INTAKE
    evidence: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if not self.task_id.strip():
            raise WorkflowError("task_id must not be empty")
        if not self.objective.strip():
            raise WorkflowError("objective must not be empty")
        if self.risk not in _RISKS:
            raise WorkflowError("risk must be one of: low, medium, high")
        if not isinstance(self.state, State):
            object.__setattr__(self, "state", State(self.state))
        object.__setattr__(self, "evidence", tuple(self.evidence))

    @property
    def requires_approval(self) -> bool:
        """Whether the item should receive explicit human approval."""

        return self.risk == "high"

    def transition(
        self,
        target: State,
        evidence: Iterable[str] = (),
    ) -> "WorkItem":
        """Return a new item after a valid, evidenced transition."""

        target = State(target)
        if target not in _ALLOWED_TRANSITIONS[self.state]:
            raise WorkflowError(
                f"invalid transition: {self.state.value} -> {target.value}"
            )

        new_evidence = tuple(item for item in evidence if item)
        if target in _EVIDENCE_STATES and not new_evidence:
            raise WorkflowError(
                f"evidence is required before entering {target.value}"
            )

        return replace(
            self,
            state=target,
            evidence=self.evidence + new_evidence,
        )
