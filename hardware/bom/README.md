# Bill of materials / Nomenclature

`bom.csv` columns: `ref, category, description_en, description_fr, qty, unit_price_eur, supplier_url, alternative, notes`.

- One line per part; give at least one alternative when possible.
- Prices are indicative and dated in `notes`. No affiliate links.
- CI checks the header (see `tools/check_bom.py`).

Status: empty template — filled during v0.1.
