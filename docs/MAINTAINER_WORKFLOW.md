# Maintainer workflow

The project follows a compact loop:

1. Inspect the current repository state.
2. Plan the smallest change that answers the issue.
3. Obtain approval when the change is high-risk or destructive.
4. Execute with a narrow scope.
5. Verify with tests, review, and documentation.
6. Record the result in the change history.

AI coding tools may help with issue triage, code review, test generation,
documentation, and release-note drafts. A human maintainer remains responsible
for permissions, dependency changes, releases, and any action that affects
users or external systems.

For API credits or agent time, useful low-risk experiments include:

- testing failure paths and invariants;
- comparing provider adapters against the same contract;
- reviewing pull requests for missing evidence;
- improving documentation and contributor onboarding.

Each experiment should produce a reproducible artifact such as a test, issue,
review note, or documentation change.
