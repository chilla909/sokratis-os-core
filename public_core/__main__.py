"""Run a small end-to-end workflow demonstration."""

from .workflow import State, WorkItem


def main() -> None:
    item = WorkItem(
        "demo-1",
        "Review a proposed change",
        risk="high",
    )
    print(f"{item.state.value}: {item.task_id}")
    item = item.transition(State.PLANNED)
    print(f"{item.state.value}: plan recorded")
    item = item.transition(State.APPROVED, ["human-approval.md"])
    print(f"{item.state.value}: approval evidence recorded")
    item = item.transition(State.EXECUTED, ["test-output.txt"])
    print(f"{item.state.value}: execution evidence recorded")
    item = item.transition(State.VERIFIED, ["review.md"])
    print(f"{item.state.value}: verification evidence recorded")


if __name__ == "__main__":
    main()
