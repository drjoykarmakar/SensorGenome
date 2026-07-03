# Paper Outline

## Working title

SensorGenome-ProbeResponse: A Condition-Standardized Benchmark for AI-Guided Molecular Sensor Discovery

## Abstract skeleton

Molecular sensor discovery remains limited by fragmented assay metadata, inconsistent response reporting, and poor machine-readability of sensor performance. We introduce SensorGenome-ProbeResponse, an open benchmark for condition-standardized sensor response prediction and active-learning experiment selection.

## Figures

1. Concept: molecule-centric AI vs experiment-centric sensor discovery.
2. Data schema and evidence grades.
3. Baseline performance under random, scaffold-held-out, and condition-held-out splits.
4. Uncertainty and applicability-domain analysis.
5. Active-learning simulation.
6. Prospective validation workflow.

## Claims to test

- Condition-aware metadata improves response prediction.
- Scaffold-held-out performance is much lower than random split performance.
- Calibrated uncertainty reduces false confidence.
- Active learning selects more informative experiments than greedy predicted response.
