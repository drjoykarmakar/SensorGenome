from __future__ import annotations

import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def regression_metrics(y_true, y_pred) -> dict:
    y_true = np.asarray(y_true, dtype=float)
    y_pred = np.asarray(y_pred, dtype=float)
    return {
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "rmse": float(mean_squared_error(y_true, y_pred) ** 0.5),
        "r2": float(r2_score(y_true, y_pred)) if len(y_true) > 1 else None,
    }


def top_k_enrichment(y_true, scores, k: int = 10, active_quantile: float = 0.8) -> float:
    y_true = np.asarray(y_true, dtype=float)
    scores = np.asarray(scores, dtype=float)
    threshold = np.quantile(y_true, active_quantile)
    active = y_true >= threshold
    top_idx = np.argsort(scores)[::-1][: min(k, len(scores))]
    baseline_rate = active.mean() if len(active) else 0.0
    top_rate = active[top_idx].mean() if len(top_idx) else 0.0
    return float(top_rate / baseline_rate) if baseline_rate > 0 else 0.0


def conformal_coverage(y_true, lower, upper) -> float:
    y_true = np.asarray(y_true, dtype=float)
    lower = np.asarray(lower, dtype=float)
    upper = np.asarray(upper, dtype=float)
    return float(((y_true >= lower) & (y_true <= upper)).mean())
