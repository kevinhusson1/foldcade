# SPDX-License-Identifier: MIT
"""Validate hardware/bom/bom.csv: expected header and numeric qty/price."""
import csv
import sys
from pathlib import Path

EXPECTED = ["ref", "category", "description_en", "description_fr", "qty",
            "unit_price_eur", "supplier_url", "alternative", "notes"]
path = Path(__file__).resolve().parent.parent / "hardware" / "bom" / "bom.csv"

with path.open(newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    if reader.fieldnames != EXPECTED:
        sys.exit(f"BOM header mismatch: {reader.fieldnames}")
    for n, row in enumerate(reader, start=2):
        try:
            if int(row["qty"]) <= 0 or float(row["unit_price_eur"]) < 0:
                raise ValueError
        except ValueError:
            sys.exit(f"bom.csv line {n}: invalid qty or unit_price_eur")
print("BOM OK")
