# Design study: the best of both references

!!! info "Status: planned"
    This study has not started. This page fixes its scope so it can be run
    separately and its result plugged back into the project. Every step will be
    recorded in the [logbook](journal/index.md).

## Objective
Design the best solution **between** two references:

- **Ref 1 — Swap Arcade**: a full arcade that turns into a furniture cabinet, also
  usable with consoles/PC.
- **Ref 2 — Chappel's hidden arcade**: tilting box-door, homemade, workshop-level.

Not a copy of either: an original concept that combines the furniture-grade
result of the first with the simplicity and buildability of the second.

## Fixed constraints
From the scoping step ([logbook 0002](journal/0002-scoping.md)):

- **floor-standing, movable** cabinet, no wall fixing (R10);
- **powerful PC** in a ventilated bay (R5, R11);
- **motion controls** and gamepad storage/charging (R12, R13);
- **basic tools, no CNC**, 3D printing in the loop (R6);
- no budget constraint during the concept (R7);
- no reuse of Swap Arcade's patent-pending kinematics.

## Candidates
| | Idea |
|---|---|
| A′ | Tilting box-door ([ADR 0003](design-decisions/0003-fold-mechanism.md)) built into a floor-standing cabinet |
| B | Arcade module folding onto a storage base (reference photo) |
| C… | Hybrids to invent during the study |

## Criteria (weights to set at kick-off)
Buildability with basic tools and 3D printing · "furniture" look when closed ·
ergonomics (screen height, angle and size, standing and seated use) · mechanism
safety · stability open and closed · mobility (weight, casters, thresholds) ·
cooling of a powerful PC, noise and cable routing · motion-sensor integration and
Bluetooth link · gamepad storage and charging · serviceability and access · number
of sheets / cut-list efficiency · cost (tracked, not binding) · bilingual
documentability.

## Method
1. Freeze requirements R1–R14 ([concept](concept.md)) and add user scenarios (flat, family, small room, moving between rooms).
2. Functional breakdown → morphological chart of solutions per function.
3. Generate 3–5 concepts, sketch each (side views open/closed).
4. Weighted scoring matrix; eliminate, then refine the top 2.
5. Quick mock-ups (cardboard / 1:5) and load and stability calculations for the winner(s).
6. Safety pre-review ([safety](safety.md)).

## Deliverables
Study report (EN/FR), sketches and renders stored per iteration in
`assets/renders/iter-NNNN/`, scoring sheet, decision recorded as **ADR 0004**,
updated requirements and roadmap, one logbook entry per step.

## Open inputs
- Assumptions H1 to H4 to confirm (tooling, printer, one person, 27" screen): see [logbook 0002](journal/0002-scoping.md).
- Buttons per player, main stance, caster type.
- PC platform and OS: dedicated ADR, run in parallel (it drives volume and ventilation).
