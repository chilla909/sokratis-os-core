"""Small, provider-neutral workflow primitives for Sokratis-OS."""

from .adapter import ExecutionAdapter, InMemoryAdapter
from .workflow import State, WorkItem, WorkflowError

__all__ = [
    "ExecutionAdapter",
    "InMemoryAdapter",
    "State",
    "WorkItem",
    "WorkflowError",
]
