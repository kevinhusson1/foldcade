# 0002 — Scoping the need

| | |
|---|---|
| **Date** | 2026-11-24 |
| **Milestone** | v0.0 Design study |
| **Authors** | Project owner · AI assistant (Claude) |
| **Status** | Done |

## Goal
Set the project's main directions from analysis [0001](0001-reference-analysis.md),
before starting the design study.

## Project owner's decisions

| ID | Decision | Reason |
|---|---|---|
| D1 | **Floor-standing, movable cabinet.** No wall fixing. | No holes in the wall; the cabinet can change rooms; more volume for electronics. |
| D2 | **A real mini PC or powerful compact PC**, no Raspberry Pi. | Emulate recent consoles. |
| D3 | **Emulation target**: all retro consoles, PS3, Xbox 360, Switch, and PS4 if the hardware allows. | A versatile machine, not just a multicade. |
| D4 | **Motion controls**: real Wiimotes and a built-in motion sensor; motion support for Switch emulation. | A real plus over the references. |
| D5 | **Basic tools only**, no CNC. **3D printing is mandatory in the loop** for parts that justify it. | Stay buildable by as many people as possible. |
| D6 | **No budget constraint** during the concept phase. | Find the best solution first; costs are recorded as we go. |
| D7 | **Fully open plans.** | Let others join the project and work together. |
| D8 | **Logbook** of every step; all iterations stay visible. | Traceability and onboarding (see [rules](index.md)). |

Direct consequence of D1: option A of [ADR 0003](../design-decisions/0003-fold-mechanism.md)
(wall-mounted cabinet) is ruled out **as is**. Its principle of a box-door that
becomes the control desk remains a candidate building block for a floor-standing cabinet.

## Technical consequences to study
These are not decisions: they are the points the design study must address.

1. **Power and heat.** PS3, Xbox 360 and PS4 need a recent multi-core CPU and a
   capable GPU. Depending on the machine, heat output ranges from about 65 W (mini PC)
   to over 300 W (compact PC with a graphics card). This needs filtered active
   ventilation (low intake, high exhaust), an accessible technical bay and attention
   to noise. Hardware and OS choice (Linux such as Batocera, or Windows with a
   frontend such as RetroBat or LaunchBox, since some emulators are mainly developed
   for Windows) will get its own ADR.
2. **Gamepads.** 3D games on these consoles are played with two sticks and
   triggers: the arcade panel is not enough. The cabinet needs wireless gamepads,
   storage and charging for them. The panel encoder must support at least XInput;
   open option to evaluate: an RP2040 board with the open-source GP2040-CE firmware.
3. **Motion.**
    - Wiimotes are for Wii (Dolphin) and Wii U (Cemu) games. They need an **infrared
      sensor bar** (plain IR LEDs) and a Bluetooth link. Option: a USB sensor bar with
      built-in Bluetooth (Mayflash DolphinBar type), housed in the marquee or below
      the screen.
    - Switch motion relies on the **gyroscope** of Joy-Cons or compatible controllers
      (Pro Controller, DualShock 4, DualSense), not on the Wiimote's IR camera. These
      controllers and their charging must be planned too.
    - An IR LED frame around the screen could also serve IR light guns (GUN4IR
      type): synergy to study.
    - The Bluetooth receiver must sit away from any metal mass.
4. **Mobility and stability.** Locking casters, hidden in the plinth if possible;
   low centre of gravity (PC and power supply at the bottom); stability checked open
   and closed; grips to push; moving parts locked during transport; threshold crossing.
5. **Tooling and 3D printing.** Without CNC, 3D printing also provides accuracy:
   **drilling and assembly jigs**, mechanism parts, grilles, panels, brackets. No
   special cutter such as Lamello; router optional. Large parts are split to fit a
   standard bed; heat-resistant material (PETG or ASA rather than PLA) near the PC.
6. **Legal.** Emulating recent consoles, the Switch in particular, is sensitive: the
   project neither ships nor points to any keys, firmware, BIOS or games. Everyone
   uses dumps from their own hardware, according to the law of their country.
7. **Dual-use ergonomics.** Arcade games are played standing at the panel; console
   games with a gamepad may be played seated, further away. Screen height and size
   must serve both.
8. **Intellectual property.** Swap Arcade has a pending patent: we rely on generic
   principles (hinges, pivots, counterweights, slides) without reproducing its
   kinematics, and check before publishing a similar mechanism.

## Assumptions to confirm

| ID | Assumption |
|---|---|
| H1 | "Basic tools" = drill-driver, jigsaw, circular saw with guide rail, sander, clamps; panels can be cut to size at the store. |
| H2 | Consumer 3D printer: about 220 × 220 × 250 mm build volume, PLA and PETG. |
| H3 | One adult must be able to move and transform the cabinet. |
| H4 | Starting point: 16:9 screen of about 27". |

## Files produced or changed
- Logbook created: `docs/journal/` (index, entries 0001 and 0002).
- `docs/concept`: Swap Arcade public specs, decisions D1 to D8, requirements R1 to R14.
- `docs/design-decisions/0003-fold-mechanism`: verified against the transcript, impact of D1.
- `docs/study-hybrid-concept`: new constraints and criteria.
- `docs/safety`: mobility and heat.
- `docs/legal`: keys and firmware.
- `docs/index`, `docs/roadmap`, `README`, `software/README.md`, `CHANGELOG.md`, `mkdocs.yml`.

## Open questions
- Buttons per player: 6 or 8?
- Main stance: standing, seated, or both?
- Final screen size and eye height.
- Visible or retractable casters?

## Next step
Start the design study (v0.0): user scenarios, functional breakdown, morphological
chart, then 3 to 5 sketched concepts.
