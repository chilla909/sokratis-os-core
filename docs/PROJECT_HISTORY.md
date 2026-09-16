# Project history and public provenance

## Summary

Sokratis-OS was developed first as a private project. The public repository is a
sanitized OSS edition of its reusable governance/control-plane layer.

At the time this public edition was prepared, the private source history
contained 71 commits spanning 2026-08-16 through 2026-08-20. This is a verified
repository fact available to the maintainer. Because the source repository is
private, public readers cannot independently inspect that commit graph. This
document therefore presents the history as provenance, not as public GitHub
activity.

The public repository was intentionally started from a clean snapshot on
2026-09-16. The initial public snapshot contained 22 sanitized files. Future
public development is recorded normally through public commits, issues, pull
requests, tests, and releases.

## Verified private-development milestones

| Date | Development milestone | Why it matters to the public core |
| --- | --- | --- |
| 2026-08-16 | M0 initial governance baseline | Established the inspect-plan-execute-verify working discipline. |
| 2026-08-16 | Core v1.1 artifact boundary | Made learning and work artifacts explicit rather than implicit. |
| 2026-08-16 | Core v1.2 mastery and learning analytics | Extended the model from task execution toward accountable progress. |
| 2026-08-16 | Core v1.3 retry, state-tracking, and maintenance rules | Strengthened lifecycle control and controlled change. |
| 2026-08-16 | Mandatory pre-implementation checks and audit backlog | Turned governance into an operational practice. |
| 2026-08-17 | ADR and governance review proposals | Added explicit decision-making and falsification work. |
| 2026-08-20 | Separation into life, trade, Sokratis, and business domains | Made domain boundaries a first-class architectural concern. |

These milestones are a concise summary of the private source history. They are
not retroactively imported commits and do not expose private files, prompts,
data, runtime state, or operational details.

## What was retained

The public edition retains the generalizable ideas:

- explicit work state and legal transitions;
- human approval for consequential work;
- evidence as a first-class part of the workflow;
- separation between governance and execution providers;
- domain boundaries and controlled context;
- reproducible verification and maintainer responsibility.

## What was excluded

The public boundary excludes:

- personal records and correspondence;
- private prompts and recovery material;
- credentials, tokens, sessions, and runtime state;
- financial, trading, tax, and broker data;
- local paths and private infrastructure;
- raw exports and operational databases.

See docs/PUBLICATION_BOUNDARY.md and
docs/DECISIONS/0001-public-edition-boundary.md.

## Provenance commitments

The project makes four explicit commitments:

1. private development history is described, not misrepresented as public activity;
2. no historical dates or commits are fabricated;
3. the public edition remains independently buildable and testable;
4. future public work is visible through ordinary open-source collaboration.

The clean public start is a safety boundary, not an attempt to hide the
project's origin.
