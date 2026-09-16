"""Provider-neutral execution and verification adapter contracts."""

from dataclasses import dataclass
from typing import Protocol

from .workflow import State, WorkItem, WorkflowError


class ExecutionAdapter(Protocol):
    """The minimal boundary an external execution system must implement."""

    def execute(self, item: WorkItem) -> WorkItem:
        """Execute an approved work item and attach evidence."""

    def verify(self, item: WorkItem) -> WorkItem:
        """Verify an executed work item and attach evidence."""


@dataclass(frozen=True, slots=True)
class InMemoryAdapter:
    """Small dependency-free adapter used for examples and tests."""

    execution_evidence: str = "adapter:in-memory-execution"
    verification_evidence: str = "adapter:in-memory-verification"

    def execute(self, item: WorkItem) -> WorkItem:
        if item.state is not State.APPROVED:
            raise WorkflowError("execution requires an approved work item")
        return item.transition(
            State.EXECUTED,
            [self.execution_evidence],
        )

    def verify(self, item: WorkItem) -> WorkItem:
        if item.state is not State.EXECUTED:
            raise WorkflowError("verification requires an executed work item")
        return item.transition(
            State.VERIFIED,
            [self.verification_evidence],
        )
