# Design study: the best of both references

!!! info "Status: planned"
    This study has not started. This page fixes its scope so it can be run
    separately and its result plugged back into the project.

## Objective
Design the best solution **between** two references:

- **Ref 1 — Swap Arcade**: a full arcade that turns into a furniture cabinet, also
  usable with consoles/PC.
- **Ref 2 — Chappel's hidden arcade**: tilting box-door, homemade, workshop-level.

Not a copy of either: an original concept that combines the furniture-grade
result of the first with the simplicity and buildability of the second.

## Candidates
| | Idea |
|---|---|
| A | Tilting box-door ([ADR 0003](design-decisions/0003-fold-mechanism.md)) |
| B | Arcade module folding onto a storage base (reference photo) |
| C… | Hybrids to invent during the study |

## Criteria (weights to set at kick-off)
Buildability with standard tools · cost · "furniture" look when closed · ergonomics
(height, screen angle, player stance) · mechanism safety · stability/wall fixing ·
cooling and cable routing · console/PC connectivity · serviceability · number of
sheets / cut-list efficiency · weight and moving · bilingual documentability.

## Method
1. Freeze requirements R1–R9 ([concept](concept.md)) and add user scenarios (flat, family, small room).
2. Functional breakdown → morphological chart of solutions per function.
3. Generate 3–5 concepts, sketch each (side views open/closed).
4. Weighted scoring matrix; eliminate, then refine the top 2.
5. Quick mock-ups (cardboard / 1:5) and load calculations for the winner(s).
6. Safety pre-review ([safety](safety.md)).

## Deliverables
Study report (EN/FR), sketches and renders in `assets/renders/`, scoring sheet,
decision recorded as **ADR 0004**, updated requirements and roadmap.

## Open inputs
- Detailed specs of Swap Arcade (only partly accessible so far).
- Target budget, room constraints (wall vs floor-standing), target audience.
