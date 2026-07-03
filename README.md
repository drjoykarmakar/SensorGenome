# SensorGenome

**SensorGenome** is an open-source research platform and benchmark for AI-guided molecular sensing.

It starts with **FluoroGenome-ProbeResponse**: a condition-standardized benchmark for small-molecule fluorescent sensor response under analyte, interferent, pH, solvent, and matrix variation.

The long-term goal is to become a shared infrastructure layer for molecular sensor discovery across fluorescence, colorimetric, Raman, electrochemical, chemiluminescent, and other sensing modalities.

## Why this exists

Most AI chemistry platforms optimize molecules. Sensor discovery requires optimizing experiments:

```text
analyte -> recognition mechanism -> sensor molecule -> assay protocol -> signal -> selectivity -> uncertainty -> next experiment
```

SensorGenome treats the **experiment** as the atomic unit, not just the molecule.

## Initial scientific wedge

The first benchmark focuses on fluorescent small-molecule probe response, beginning with:

- bimane-derived probes
- xylazine/adulterant sensing workflows
- analyte/interferent selectivity
- raw spectra and response curves
- standardized assay metadata
- uncertainty-aware ML baselines
- active-learning experiment selection

## What is included in this starter repo

- Python package scaffold
- data schemas for sensors, analytes, assays, spectra, and responses
- sample dataset
- CLI for validation and baseline training
- FastAPI skeleton
- active-learning selection utilities
- baseline ML pipeline
- benchmark metrics
- Dockerfile and docker-compose
- GitHub Actions CI
- tests
- documentation and roadmap
- paper outline

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Validate sample data

```bash
sensorgenome validate data/sample/probe_response_sample.csv
```

## Train baseline model

```bash
sensorgenome train-baseline data/sample/probe_response_sample.csv --target response_ratio --out reports/baseline_metrics.json
```

## Run API

```bash
uvicorn sensorgenome.api.main:app --reload
```

## Repository philosophy

SensorGenome is not a fluorescence property-prediction clone. Existing fluorophore datasets and tools already cover photophysical prediction. This project focuses on **probe response**, especially the experimental conditions that determine whether a sensor actually works.

## Proposed novelty claim

> SensorGenome-ProbeResponse is an open benchmark for condition-standardized molecular sensor response, with analyte/interferent metadata, raw spectra, uncertainty-aware baselines, and active-learning selection of the next experiment.

Avoid claiming it is the first fluorescence ML platform.

## License

MIT for code. Dataset licensing should be decided separately before public release.
