# 0001 — Reference analysis

| | |
|---|---|
| **Date** | 2026-11-24 |
| **Milestone** | v0.0 Design study |
| **Authors** | Project owner · AI assistant (Claude) |
| **Status** | Done |

## Goal
Understand the need before any design work, by analysing the repository, the local
reference image and the public sources of both references.

## What was done
- Full review of the repository (concept, ADRs 0001 to 0003, study, safety, roadmap).
- Analysis of the local image `assets/references/inspiration-concept.webp` (not redistributed).
- Reading of the Swap Arcade Kickstarter page (story, FAQ, rewards) and its
  visuals, accessed 2026-11-24.
- Reading of the description and auto-generated transcript of Alexandre Chappel's
  video, and of his plans page.

## Findings

### Local reference image
It is a Swap Arcade marketing visual showing the four states: full arcade,
opening, folding, closed sideboard.

### Swap Arcade (commercial product)

| Item | Published value |
|---|---|
| Campaign | 12 May – 12 June 2026; $231,392 pledged by 177 backers; delivery announced for January 2027 |
| Price | $1,297 ($1,097 early bird); a **non-transforming** DIY kit at $447 |
| Arcade mode | approx. 70" × 28" × 14" (≈ 178 × 71 × 36 cm) |
| Cabinet mode | approx. 36" × 29" × 13.5" (≈ 91 × 74 × 34 cm) |
| Screen | 27", HDMI, built-in speakers |
| Controls | 2 players, Sanwa JLF-TP-8YT joysticks, **8 buttons per player** + function buttons; add-ons: spinner, 2" trackball, Sinden light gun |
| Electronics | Raspberry Pi 4 running Batocera; Intel N100 mini PC upgrade; Brook Zero-Pi encoder compatible with Switch/Switch 2, PS1 to PS3, PC X-Input |
| Structure | Painted MDF top half attached to a **metal frame** with a pivot joint; base in hardwood and plywood; Natural, Walnut, Dark Tobacco or bare finishes |
| Safety | **Counterbalanced** motion; quick-locking pins at the front corners, redundant second set at the back |
| Storage | In the base, accessible **only in arcade mode**; the front doors are false doors |
| IP | **Patent pending** (Cookson Innovations Inc.) |

The exact kinematics are not published. The visuals show wooden panels on visible
black hinges that open to let the top half rise.

### Chappel's hidden arcade (homemade build, 2021)
The transcript **confirms** the mechanism described in [ADR 0003](../design-decisions/0003-fold-mechanism.md):

- **wall-mounted** cabinet in 16 mm oak plywood, one sheet, edge-banded, no visible screws (biscuits and pocket holes);
- the front flips down 90° and becomes the control desk; the screen sits tilted back inside the box;
- pivot: 3D-printed cylinder with a wooden dowel through it; stop: shelf pins; latch: spring and brass rod in a printed housing;
- fake groove at the bottom, because the bottom rail belongs to the door;
- desk top clipped on (Lamello Clamex-type connectors), removed with a suction cup; it fell once and three corners broke: **service access is a weak point**;
- Raspberry Pi with RetroPie, USB encoder kit, microswitch buttons; speakers above the screen; 3D-printed I/O plate (USB, reset, main switch, power inlet);
- plans sold at $15: metric woodwork drawings and 3D files, **no wiring diagram**, no licence stated.

### Synthesis
The "best cabinet" must keep three promises at once:

1. **Authentic arcade experience** (screen, stance, controls, sound, presence);
2. **Complete disappearance** (credible furniture, no loose parts or visible hardware);
3. **Buildable and open** (accessible tooling, serviceable, safe, documented down to the wiring).

Swap Arcade keeps 1 and 2 at the expense of 3; Chappel keeps 2 and 3 at the expense of 1.

### Gaps found in the repository
- The concept said Swap Arcade's specs were not accessible.
- ADR 0003 said it was "not verified".
- R1 planned 6 buttons per player; Swap Arcade has 8.
- Console connectivity was not a requirement.
- Swap Arcade's pending patent was not mentioned.

These gaps are handled in entry [0002](0002-scoping.md).

## Decisions
None: analysis entry.

## Files produced or changed
None in the repository (analysis only).

## Next step
Scope the need with the project owner: format, platform, tooling, licence.
