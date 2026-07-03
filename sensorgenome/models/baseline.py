from __future__ import annotations

from pathlib import Path
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import KFold, cross_val_predict

from sensorgenome.chemistry.features import featurize_dataframe


def train_baseline(csv_path: str | Path, target: str, out: str | Path | None = None) -> dict:
    df = pd.read_csv(csv_path)
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found. Available: {list(df.columns)}")
    df = df.dropna(subset=[target, "smiles"])
    y = pd.to_numeric(df[target], errors="coerce")
    keep = y.notna()
    df = df.loc[keep].reset_index(drop=True)
    y = y.loc[keep].to_numpy(dtype=float)
    X = featurize_dataframe(df)

    model = RandomForestRegressor(n_estimators=200, random_state=42, min_samples_leaf=1)
    n_splits = min(5, len(df))
    if n_splits >= 2:
        cv = KFold(n_splits=n_splits, shuffle=True, random_state=42)
        pred = cross_val_predict(model, X, y, cv=cv)
    else:
        pred = np.full_like(y, y.mean())

    metrics = {
        "n": int(len(y)),
        "target": target,
        "mae": float(mean_absolute_error(y, pred)),
        "rmse": float(mean_squared_error(y, pred) ** 0.5),
        "r2": float(r2_score(y, pred)) if len(y) > 1 else None,
        "warning": "Small sample baseline. Do not overinterpret." if len(y) < 30 else None,
    }

    model.fit(X, y)
    if out:
        out = Path(out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(metrics, indent=2))
        joblib.dump(model, out.with_suffix(".joblib"))
    return metrics
