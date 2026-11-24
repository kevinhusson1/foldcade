# Concept

## Vision

A 2-player arcade cabinet that is **floor-standing, movable and hidden in plain
sight**. Closed, it looks like a sideboard; open, it is a full arcade machine. It
runs on a PC powerful enough to emulate recent consoles, supports motion controls
(Wiimotes, gyroscope) and stores its gamepads inside.

## Inspirations

FoldCade mixes two references. We take **ideas, not designs**; all drawings are
redrawn from scratch.

| Reference | What we retain |
|---|---|
| *Swap Arcade* by Les Cookson & Ken Higginson, Kickstarter 2026 ([campaign](https://www.kickstarter.com/projects/amat/swap-arcade-full-arcade-that-turns-into-a-furniture-cabinet/description)) | Full-size arcade that becomes a sideboard, clean "furniture" look, colour-blocked artwork, retro + console versatility, built-in storage, safe motion (counterbalance, redundant locking) |
| *"This Arcade Machine is hidden in plain sight! And This is how I Built It!"* by Alexandre Chappel — <https://youtu.be/OB8VauGEvqg> | Homemade construction method, door that becomes the control desk, hidden hardware, 3D-printed parts. Its [sales page](https://www.alch.shop/projects/p/arcade-cabinet) sells paid plans (metric drawings, 3D-print files, parts list with links, video resources) for a cabinet built from **a single sheet of 16 mm plywood**, on a Raspberry Pi with RetroPie. |

### What we keep, change and add vs. the plan set above

| | Keep | Change / add |
|---|---|---|
| Material | Sheet-material construction, **metric drawings**, 3D-printed small parts | Basic tools, no CNC; **3D-printed drilling jigs** for accuracy; check the sheet count (cut-list optimisation, see R8) |
| Documentation | Parts list with links, video resources, clear "what is included" note | **Free and open**, with a **full wiring diagram** and safety guide (the reference explicitly excludes electronics support), BOM with quantities, prices and alternatives, bilingual, public **logbook** |
| Scope | 2 players | **Floor-standing, movable** cabinet; **powerful PC** (emulation up to PS3, Xbox 360, Switch, maybe PS4); **motion controls**; gamepad storage and charging |
| Licence | — | Open licences with mandatory credit (see ADR 0001) |

!!! info "What we know about Swap Arcade"
    From the public campaign page (accessed 2026-11-24, details in
    [logbook 0001](journal/0001-reference-analysis.md)): about 178 × 71 × 36 cm
    in arcade mode and 91 × 74 × 34 cm in cabinet mode; 27" screen with speakers;
    Sanwa joysticks and 8 buttons per player; Raspberry Pi 4 running Batocera or an
    N100 mini PC; encoder compatible with Switch, PlayStation and PC; painted MDF
    top half on a pivoting metal frame, counterbalanced and locked by pins at the
    front and back; storage only accessible in arcade mode.

!!! warning "Patent pending"
    Swap Arcade is announced as "patent pending". We rely on generic principles
    (hinges, pivots, counterweights, slides) without reproducing its kinematics,
    and we check before publishing a similar mechanism.

The second reference's mechanism is detailed in [ADR 0003](design-decisions/0003-fold-mechanism.md).

## Decided directions

Decided on 2026-11-24 by the project owner; reasons and consequences in
[logbook 0002](journal/0002-scoping.md).

- **D1** Floor-standing, movable cabinet, no wall fixing.
- **D2** A real mini PC or powerful compact PC, no Raspberry Pi.
- **D3** Emulation: all retro consoles, PS3, Xbox 360, Switch, and PS4 if the hardware allows.
- **D4** Motion controls: real Wiimotes and a built-in sensor; motion support for Switch emulation.
- **D5** Basic tools, no CNC; 3D printing mandatory in the loop.
- **D6** No budget constraint during the concept phase.
- **D7** Fully open, collaborative plans.
- **D8** Logbook of every step; all iterations stay visible.

## Functional requirements (draft)

| ID | Requirement |
|---|---|
| R1 | 2 players: 1 joystick and 6 to 8 action buttons each (count set by the study), start/coin, function buttons (menu, hotkeys) |
| R2 | 16:9 screen, size to be decided (starting point: about 27") |
| R3 | Folded state hides screen and controls; no loose parts; credible furniture look |
| R4 | Mechanism safe: no pinch points, damped or counterbalanced motion, redundant locking, stable when open |
| R5 | Technical bay for a powerful PC: filtered active ventilation, cable routing, service access without risky disassembly |
| R6 | Buildable with basic tools, no CNC; 3D printing for specific parts and jigs, on a consumer printer |
| R7 | No budget constraint in the concept phase; costs are recorded in the BOM as soon as they are known |
| R8 | Optimised cut list (target: minimum number of standard sheets), all drawings metric |
| R9 | Complete wiring diagram, power-button/shutdown wiring and a "what is included / not included" note in the build guide |
| R10 | Floor-standing with no wall fixing; movable by one person (locking casters or equivalent); stable open and closed |
| R11 | Emulation target: retro consoles, PS3, Xbox 360, Switch; PS4 if the hardware allows |
| R12 | Motion controls: real Wiimotes with a built-in IR sensor bar; gyroscope (Joy-Cons or compatible controllers) for Switch emulation |
| R13 | Wireless gamepads, Wiimotes and Joy-Cons stored and charged inside the cabinet |
| R14 | Open, collaborative plans; every iteration recorded in the [logbook](journal/index.md) |

## Open questions

- Transformation mechanism: hinge + gas strut, counterweight, linkage, or sliding?
- Screen: final size, eye height, standing and seated use?
- PC: mini PC with integrated graphics, or compact PC with a graphics card? Linux (Batocera-like) or Windows (RetroBat or LaunchBox-type frontend)?
- Panel encoder: XInput at minimum (open option: RP2040 + GP2040-CE)?
- Motion sensor: IR bar only, or an IR frame that also serves light guns?
- Casters: visible or retractable?
- Material: birch plywood vs MDF (finish, weight, cost).
