#!/usr/bin/env python3

import argparse
import math
from pathlib import Path

import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser(description="Process derived dataset with pandas (workshop demo)")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--summary", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    df = pd.read_csv(args.input)

    summary_kv: dict[str, str] = {}
    for line in args.summary.read_text().splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        summary_kv[key.strip()] = value.strip()

    mean_s = float(summary_kv.get("value_centered_mean", "nan"))
    sd_s = float(summary_kv.get("value_centered_sd", "nan"))

    # Add a simple pandas-derived feature for the report. It intentionally depends
    # on the R-produced summary so this step sits "between" R and Quarto.
    if pd.isna(mean_s):
        mean_s = float(df["value_centered"].mean())
    if pd.isna(sd_s) or math.isclose(sd_s, 0.0, abs_tol=1e-12):
        sd_s = float(df["value_centered"].std(ddof=0)) or 1.0

    df["value_centered_z"] = (df["value_centered"] - mean_s) / sd_s

    args.output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
