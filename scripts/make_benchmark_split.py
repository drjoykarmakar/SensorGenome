from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv")
    parser.add_argument("--outdir", default="data/benchmark_splits")
    parser.add_argument("--test-size", type=float, default=0.2)
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    train, test = train_test_split(df, test_size=args.test_size, random_state=42)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    train.to_csv(outdir / "train.csv", index=False)
    test.to_csv(outdir / "test.csv", index=False)
    print(f"Wrote {len(train)} train and {len(test)} test rows to {outdir}")


if __name__ == "__main__":
    main()
