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
| *Swap Arcade* by Les Cookson & Ken Higginson, Kickstarter 2026 ([campaign](https://www.kickstarter.com/projects/amat/swap-arcade-full-arcade-that-turns-into-a-furniture-cabinet/description)) | Storage base with double doors, transformable arcade module, clean "furniture" look, colour-blocked front, 2 joysticks + 6 buttons per player |
| *"This Arcade Machine is hidden in plain sight! And This is how I Built It!"* by Alexandre Chappel — <https://youtu.be/OB8VauGEvqg> | Homemade construction method, hidden-arcade principle, workshop-level tooling. Its [sales page](https://www.alch.shop/projects/p/arcade-cabinet) sells paid plans (metric drawings, 3D-print files, parts list with links, video resources) for a cabinet built from **a single sheet of 16 mm plywood**, on a Raspberry Pi with RetroPie. |

### What we keep, change and add vs. the plan set above

| | Keep | Change / add |
|---|---|---|
| Material | Sheet-material construction, **metric drawings**, 3D-printed small parts | Evaluate whether the whole cabinet can still come from few sheets (cut-list optimisation, see R8) |
| Documentation | Parts list with links, video resources, clear "what is included" note | **Free and open**, with a **full wiring diagram** and safety guide (the reference explicitly excludes electronics support), BOM with quantities, prices and alternatives, bilingual |
| Scope | 2 players, RetroPie-style software | Closable furniture-style base with storage (first reference) |
| Licence | — | Open licences with mandatory credit (see ADR 0001) |

!!! info "What we know about Swap Arcade"
    From the public campaign page: built-in retro gaming **plus** connection to
    Switch, PlayStation, PC and more; swaps into a furniture cabinet; built from
    MDF, hardwood and plywood; serviceable, replaceable parts (joysticks, buttons,
    cables, electronics). Its detailed specs, dimensions and mechanism were not
    available to us, so they are not assumed here.

    The mechanism we study in depth comes from the second reference: see
    [ADR 0003](design-decisions/0003-fold-mechanism.md).

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
| R8 | Optimised cut list (target: minimum number of standard sheets, e.g. 16 mm plywood), all drawings metric |
| R9 | Complete wiring diagram, power-button/shutdown wiring and a "what is included / not included" note in the build guide |

## Open questions

- Fold mechanism: hinge + gas strut, linkage, or sliding?
- Screen: 24" 16:9 landscape, or 4:3 / vertical-capable?
- Computer: Raspberry Pi 5, mini-PC, or leave open?
- Material: birch plywood vs MDF (finish, weight, cost).
