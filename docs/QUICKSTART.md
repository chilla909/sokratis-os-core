# Quickstart

Requirements: Python 3.11 or newer.

~~~text
python -m venv .venv
. .venv/bin/activate
python -m pip install -e ".[dev]"
pytest
~~~

A minimal example can be found at examples/minimal_task.json. The JSON file
describes the information an adapter may collect before creating a WorkItem;
the Python core intentionally stays smaller than any one adapter schema.

Example:

~~~python
from public_core import State, WorkItem

item = WorkItem("demo-1", "Review a proposed change", risk="high")
item = item.transition(State.PLANNED)
item = item.transition(State.APPROVED, ["human-approval.md"])
item = item.transition(State.EXECUTED, ["test-output.txt"])
item = item.transition(State.VERIFIED, ["review.md"])
~~~
