# SensorGenome

**SensorGenome** is an open foundation for AI-driven molecular sensing: datasets, benchmarks, models, and active-learning workflows for discovering and evaluating chemical sensors.

The project begins with fluorescent small-molecule probes and expands toward a general machine-readable standard for molecular sensing experiments, including analyte response, interferent selectivity, raw spectra, assay conditions, uncertainty, and prospective validation.

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

## v0.1.0-alpha public milestone

**SensorGenome-Bench v0.1**: fluorescent probe-response benchmark with 25 curated seed sensor examples, schema validation, baseline model, and active-learning demo.

This alpha release is intentionally small. Its purpose is to establish the data standard, benchmark interface, and contribution workflow before larger literature-curated and prospectively measured datasets are added.

## What is included

- Python package scaffold
- 25-row seed probe-response dataset
- data schemas for sensors, analytes, assays, spectra, and responses
- CLI for validation, baseline training, and active-learning selection
- FastAPI skeleton
- active-learning selection utilities
- baseline ML pipeline
- benchmark metrics
- Dockerfile and docker-compose
- GitHub Actions CI
- tests
- GitHub issue templates
- release notes and milestone plan
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

## Run active-learning demo

```bash
sensorgenome select-next data/sample/probe_response_sample.csv --k 5
```

## Run API

```bash
uvicorn sensorgenome.api.main:app --reload
```

## Repository topics

Suggested GitHub topics:

```text
ai-for-science molecular-sensing chemical-sensors fluorescence cheminformatics active-learning benchmark rdkit spectroscopy machine-learning chemical-biology open-science
```

## Repository philosophy

SensorGenome is not a fluorescence property-prediction clone. Existing fluorophore datasets and tools already cover photophysical prediction. This project focuses on **probe response**, especially the experimental conditions that determine whether a sensor actually works.

## Proposed novelty claim

> SensorGenome-ProbeResponse is an open benchmark for condition-standardized molecular sensor response, with analyte/interferent metadata, raw spectra, uncertainty-aware baselines, and active-learning selection of the next experiment.

Avoid claiming it is the first fluorescence ML platform.

## License

MIT for code. Dataset licensing should be decided separately before public release.
