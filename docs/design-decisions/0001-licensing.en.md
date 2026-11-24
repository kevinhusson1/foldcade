# ADR 0001 — Licensing

- **Status:** Accepted
- **Date:** 2026-11-24

## Context
We want a free, open project that others can build, sell and adapt, as long as
they say where the plans come from.

## Decision
Three permissive licences that all require attribution, plus an `ATTRIBUTION.md`
that spells out the expected credit in practice:

- Hardware: **CERN-OHL-P-2.0**
- Software: **MIT**
- Documentation and media: **CC BY 4.0**

## Consequences
- Commercial use is allowed. Attribution is required for redistribution and
  commercial use; private builds need no label.
- No copyleft: derivatives may be closed. If sharing improvements back becomes a
  priority, switch hardware to CERN-OHL-S for **future** releases (past releases
  keep their licence).
- "Non-commercial" licences were rejected: they are not open source and block
  workshops, makerspaces and small makers.
