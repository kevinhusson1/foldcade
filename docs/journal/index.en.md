# Logbook

The logbook records **every step** of the work on FoldCade, in order, so that all
iterations stay visible: what was tried, decided, dropped, and why. It is the
project's memory and the entry point for anyone who wants to join.

## Entries

| No. | Date | Title | Milestone | Outcome |
|---|---|---|---|---|
| [0001](0001-reference-analysis.md) | 2026-11-24 | Reference analysis | v0.0 | Swap Arcade specs and Chappel's mechanism established |
| [0002](0002-scoping.md) | 2026-11-24 | Scoping the need | v0.0 | Floor-standing movable cabinet, powerful mini PC, motion controls, basic tools + 3D printing |

## Rules

1. **One entry per completed step** (or significant work session), numbered `NNNN`.
   A number is never reused.
2. **A published entry is not rewritten.** A substantive correction goes into a new
   entry, or into a dated "Update" note appended at the bottom. Typos may be fixed.
3. **Each entry** gives the goal, what was done, findings, decisions, files produced
   or changed, and the next step.
4. **Design iterations are never overwritten**: sketches, renders, mock-ups and CAD
   files are stored per iteration (e.g. `assets/renders/iter-0003/`). Rejected
   variants are kept with the reason they were rejected.
5. **Structural decisions become ADRs** (`docs/design-decisions/`). A superseded ADR
   gets the status "Superseded by ADR XXXX"; it is never deleted.
6. **Bilingual** EN/FR, like the rest of the documentation.
7. **Git**: one commit (or pull request) per entry, e.g.
   `docs(journal): 0003 functional breakdown`. Git history remains the complete
   record; the logbook is its readable summary.

## Entry template

```markdown
# NNNN — Title

| | |
|---|---|
| **Date** | YYYY-MM-DD |
| **Milestone** | v0.x |
| **Authors** | … |
| **Status** | In progress / Done |

## Goal
## What was done
## Findings
## Decisions
## Files produced or changed
## Open questions
## Next step
```
