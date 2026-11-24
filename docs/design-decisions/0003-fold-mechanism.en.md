# ADR 0003 — Fold mechanism: tilting box-door (option A)

- **Status:** Proposed (to be validated by a prototype)
- **Date:** 2026-11-24

## Context
The hidden-arcade build by Alexandre Chappel (see [concept](../concept.md)) uses
a **tilting box-door that rotates 90°**: the cabinet front is a hollow volume
that becomes the control desk once lowered. The summary below is a technical
analysis supplied by the project owner; it describes that reference build. It
was **cross-checked on 2026-11-24 against the video transcript**
([logbook 0001](../journal/0001-reference-analysis.md)): every point in the table
is confirmed. The video also shows that the front panel already fell once when
removed with a suction cup (three corners broken).

## Reference mechanism (summary)

| Subsystem | Principle |
|---|---|
| **Pivot** | Two hollow 3D-printed cylinders in the side walls of the moving box; wooden dowels pass through them into blind holes in the fixed frame uprights. Pivot is invisible from outside. |
| **90° stop** | Two metal shelf pins in the frame's inner walls; the back of the box rests on them when lowered, so the desk stops horizontal and carries both players' hands. |
| **Hidden gap** | The bottom rail is part of the moving door. A routed decorative groove on the front imitates a normal door gap and hides the clearance needed to rotate inward. |
| **Latch** | Spring-loaded brass rod in a 3D-printed housing set into the door's top edge; the spring pushes it up into a keeper under the fixed top. Pull the pin down to release. |
| **Service access** | Box closed on all sides; the front panel is removable with Lamello Clamex/Tenso connectors (aligned at the bottom with two wooden lamellos, clipped on top), pulled off with a glass suction cup. No visible screws. |
| **Wall fixing** | French cleat: two rear rails cut at 45°, mating with a reverse-bevel batten on the wall, so gravity pulls the cabinet against the wall and spreads the load. |

## Options for FoldCade

- **A — Tilting box-door (this ADR).** Simple, few parts, fully hidden hardware,
  suits a wall-mounted or low cabinet. Needs strong wall fixing.
- **B — Arcade module folding onto a base cabinet** (Swap Arcade style, per the
  reference photo). More complex linkage; floor-standing; to be studied.

## Points to verify / adapt (our notes, not from the reference)

- **Load case:** lean/press forces of two players on a cantilevered desk; define a
  test load and safety factor before v0.1 (see [safety](../safety.md)).
- **Stop & pivot:** shelf pins and wooden dowels must be sized for shear;
  consider metal sleeves or rated hinges as a safer variant.
- **Latch:** a failed latch must not drop a heavy panel; add a second retention
  or damping and check pinch points (R4).
- **Lamello Clamex/Tenso** needs a specialised cutter; document alternatives
  (cam locks, magnets, concealed screws behind a cover) so the build stays
  affordable.
- **French cleat:** the wall must carry the load: specify wall types, fixings and
  a stud/anchor check; floor-standing variant or anti-tip strap as alternative.
- **Heat:** a closed box with a Raspberry Pi needs ventilation (R5).

## Decision
**No choice yet.** The goal is to design the best solution *between* the two
references, not to pick one. A dedicated [design study](../study-hybrid-concept.md)
will compare options A, B and hybrids, and its outcome will be recorded in ADR 0004.
Option A is listed as the best-documented starting point, nothing more.

## Update (2026-11-24)
Decision D1 in [logbook 0002](../journal/0002-scoping.md) requires a **floor-standing,
movable** cabinet with no wall fixing. Option A is therefore ruled out **as is**
(wall cabinet on a cleat). Its principle, a box-door that tilts down and becomes the
control desk, remains a **candidate building block** for a floor-standing cabinet.
The "French cleat" point above no longer applies; the "Heat" point now concerns a
powerful PC, not a Raspberry Pi (R5).
