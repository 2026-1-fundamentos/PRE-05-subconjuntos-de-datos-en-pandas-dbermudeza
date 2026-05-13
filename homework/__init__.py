"""Homework package entry point."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
INPUT_CSV = ROOT_DIR / "files" / "input" / "truck_event_text_partition.csv"
OUTPUT_DIR = ROOT_DIR / "files" / "output"
OUTPUT_CSV = OUTPUT_DIR / "specific-columns.csv"

SELECT_COLUMNS = [
    "driverId",
    "truckId",
    "eventTime",
    "eventType",
    "longitude",
    "latitude",
    "routeName",
    "eventDate",
]


def generate_specific_columns_csv() -> Path:
    """Read the input data and write a subset of specific columns to CSV."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT_CSV)
    available_columns = [col for col in SELECT_COLUMNS if col in df.columns]
    df.loc[:, available_columns].to_csv(OUTPUT_CSV, index=False)
    return OUTPUT_CSV


if __name__ == "__main__":
    generate_specific_columns_csv()
