from __future__ import annotations

import pandas as pd


def select_diverse_uncertain_candidates(
    candidates: pd.DataFrame,
    prediction_col: str = "predicted_response",
    uncertainty_col: str = "uncertainty",
    cost_col: str | None = None,
    scaffold_col: str = "scaffold",
    k: int = 10,
) -> pd.DataFrame:
    """Select next experiments using a simple uncertainty/diversity/cost heuristic.

    This is a transparent baseline, not a state-of-the-art policy. It is meant
    to be replaced by Bayesian optimization, Thompson sampling, or expected
    information gain policies.
    """
    df = candidates.copy()
    if uncertainty_col not in df.columns:
        df[uncertainty_col] = 1.0
    if prediction_col not in df.columns:
        df[prediction_col] = 0.0
    if cost_col and cost_col in df.columns:
        cost = df[cost_col].clip(lower=1e-6)
    else:
        cost = 1.0

    df["acquisition_score"] = (df[prediction_col].rank(pct=True) + df[uncertainty_col].rank(pct=True)) / cost
    df = df.sort_values("acquisition_score", ascending=False)

    selected = []
    seen_scaffolds = set()
    for _, row in df.iterrows():
        scaffold = row.get(scaffold_col, None)
        if scaffold and scaffold in seen_scaffolds and len(seen_scaffolds) < k:
            continue
        selected.append(row)
        if scaffold:
            seen_scaffolds.add(scaffold)
        if len(selected) >= k:
            break

    if len(selected) < k:
        remaining = df.drop(index=[r.name for r in selected], errors="ignore")
        selected.extend([r for _, r in remaining.head(k - len(selected)).iterrows()])

    return pd.DataFrame(selected).reset_index(drop=True)
