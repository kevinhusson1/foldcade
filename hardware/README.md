# Hardware / Matériel

Licence: **CERN-OHL-P-2.0** — attribution required, see [../ATTRIBUTION.md](../ATTRIBUTION.md).

| Folder / Dossier | EN | FR |
|---|---|---|
| `cad/` | Sources (FreeCAD preferred) + STEP exports | Sources (FreeCAD de préférence) + exports STEP |
| `cutting-plans/` | DXF/SVG/PDF panel layouts | Plans de découpe DXF/SVG/PDF |
| `3d-prints/` | STL + sources | STL + sources |
| `electronics/` | Wiring diagrams, KiCad if needed | Schémas de câblage, KiCad si besoin |
| `bom/` | Bill of materials (CSV) | Nomenclature (CSV) |

Rules / Règles: always export open formats (STEP, DXF, SVG, PDF, STL) next to
native files; units in millimetres; add the title block with the attribution line.
Large binaries use Git LFS (see `.gitattributes`).
