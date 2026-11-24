# Concept

## Vision

A 2-player stand-up arcade cabinet that **hides in plain sight**: the arcade
module folds down onto a wooden storage base with double doors. Closed, it looks
like a sideboard; open, it is a full arcade machine with space inside for a
console, a computer and cables.

## Inspirations

FoldCade mixes two references. We take **ideas, not designs**; all drawings are
redrawn from scratch.

| Reference | What we retain |
|---|---|
| A commercial closable arcade cabinet (crowdfunded; reference to be added — see TODO) | Storage base with double doors, transformable arcade module, clean "furniture" look, colour-blocked front, 2 joysticks + 6 buttons per player |
| *"This Arcade Machine is hidden in plain sight! And This is how I Built It!"* by Alexandre Chappel — <https://youtu.be/OB8VauGEvqg> | Homemade construction method, hidden-arcade principle, workshop-level tooling |

!!! note "TODO"
    Add the exact crowdfunding campaign link and a short list of what we keep /
    change (dimensions, mechanism, materials, price target).

## Functional requirements (draft)

| ID | Requirement |
|---|---|
| R1 | 2 players, 2 joysticks, 6 action buttons each, start/coin |
| R2 | Screen size and ratio to be decided (see ADR 0002) |
| R3 | Folded state hides screen and controls; no loose parts |
| R4 | Mechanism safe: no pinch points, damped motion, stable when open |
| R5 | Base holds a console/PC with ventilation and cable routing |
| R6 | Buildable from sheet material with standard tools; CNC/laser optional |
| R7 | Total BOM cost target to be defined at v0.1 |

## Open questions

- Fold mechanism: hinge + gas strut, linkage, or sliding?
- Screen: 24" 16:9 landscape, or 4:3 / vertical-capable?
- Computer: Raspberry Pi 5, mini-PC, or leave open?
- Material: birch plywood vs MDF (finish, weight, cost).
