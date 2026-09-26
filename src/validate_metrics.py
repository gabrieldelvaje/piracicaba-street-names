"""Validate documented carousel metrics and required repository files."""

from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED = {
    ("theme", "Nova Piracicaba", "flowers_and_plants"): 32,
    ("theme", "Nova Piracicaba", "birds"): 23,
    ("theme", "Mario Dedini", "trees_and_plants"): 16,
    ("theme", "Mario Dedini", "stones_and_gems"): 8,
    ("theme", "Cidade Jardim", "countries"): 9,
    ("theme", "Jupia", "fish"): 8,
    ("title", "municipality", "Doutor"): 102,
    ("title", "municipality", "Doutora"): 1,
    ("title", "municipality", "Professor"): 74,
    ("title", "municipality", "Professora"): 29,
    ("surname", "municipality", "Furlan"): 22,
    ("surname", "municipality", "Trevisan"): 19,
    ("surname", "municipality", "Ometto"): 9,
    ("surname", "municipality", "Dedini"): 8,
    ("surname", "municipality", "Pecorari"): 8,
}

BASE_EXPECTED = {
    "address_records": 224750,
    "unique_street_denominations": 4086,
    "locality_street_combinations": 5603,
}

CAROUSEL = [
    "01-cover.jpg",
    "02-bairros-tematicos.jpg",
    "03-nova-piracicaba.jpg",
    "04-cidade-jardim.jpg",
    "05-sobrenomes.jpg",
    "06-titulos.jpg",
    "07-resumo.jpg",
]


def main() -> None:
    path = ROOT / "data" / "insights_summary.csv"

    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))

    values = {
        (r["category"], r["scope"], r["metric"]): int(r["value"])
        for r in rows
    }

    failures = []

    for key, expected in EXPECTED.items():
        actual = values.get(key)
        if actual != expected:
            failures.append(f"{key}: expected {expected}, got {actual}")

    for metric, expected in BASE_EXPECTED.items():
        key = ("base", "municipality", metric)
        actual = values.get(key)
        if actual != expected:
            failures.append(f"{key}: expected {expected}, got {actual}")

    for filename in CAROUSEL:
        p = ROOT / "carousel" / filename
        if not p.exists():
            failures.append(f"Missing carousel image: {p}")

    if failures:
        print("Validation failed:")
        for item in failures:
            print(f"- {item}")
        raise SystemExit(1)

    print("Validation OK")
    print(f"- {len(CAROUSEL)} carousel images found")
    print(f"- {len(EXPECTED)} carousel metrics checked")
    print(f"- {len(BASE_EXPECTED)} base metrics checked")


if __name__ == "__main__":
    main()
