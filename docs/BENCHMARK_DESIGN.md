# Benchmark Design

## Task A: Response prediction
Predict response ratio for a sensor-analyte-condition tuple.

## Task B: Selectivity prediction
Rank target analyte response above interferent response.

## Task C: Condition generalization
Hold out solvents, pH ranges, matrices, or scaffolds.

## Task D: Applicability domain
Models must abstain or flag out-of-domain cases.

## Task E: Active-learning selection
Given a small experimental history, choose the next experiments.

## Metrics

- MAE and RMSE for response ratio.
- Spearman/Kendall for ranking.
- Top-k enrichment for finding high-response probes.
- Calibration error for uncertainty.
- Conformal coverage where implemented.
- OOD AUROC for applicability domain.
- Cost-normalized information gain for active learning.
