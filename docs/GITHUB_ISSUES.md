# Suggested GitHub Issues for v0.1.0-alpha

Create these issues immediately after uploading the repository.

## 1. Finalize SensorGenome schema v0.1
**Labels:** schema, data, v0.1  
**Goal:** Lock the minimum viable probe-response schema.

Tasks:
- Review required columns in `probe_response.schema.json`.
- Add raw spectrum pointer fields.
- Add publication/provenance fields.
- Add assay uncertainty fields.
- Document allowed modalities and mechanisms.

Acceptance criteria:
- Schema validates the 25-row sample dataset.
- `docs/DATA_SCHEMA.md` matches the JSON schema.

## 2. Add 25 seed sensor examples
**Labels:** data, curation, good first issue  
**Goal:** Establish the first toy-but-realistic benchmark table.

Acceptance criteria:
- `data/sample/probe_response_sample.csv` has at least 25 rows.
- Rows include target and interferent examples.
- Rows include multiple modalities beyond fluorescence.

## 3. Add raw spectra example format
**Labels:** spectra, schema  
**Goal:** Define how raw spectra will be stored and referenced.

Acceptance criteria:
- Add `data/sample/raw_spectra/` example CSV.
- Add docs explaining wavelength/intensity format.
- Add schema fields for raw spectrum URI.

## 4. Add fluorescence probe-response benchmark task
**Labels:** benchmark, fluorescence  
**Goal:** Create the first benchmark task definition.

Acceptance criteria:
- Task card exists in `docs/BENCHMARK_DESIGN.md`.
- Metrics include response-ratio prediction and selectivity ranking.

## 5. Add active-learning simulator demo
**Labels:** active-learning, demo  
**Goal:** Demonstrate next-experiment selection.

Acceptance criteria:
- CLI command returns top-k candidate records.
- Example output is documented in README.

## 6. Add model card template
**Labels:** documentation, model-card  
**Goal:** Make baseline models reproducible and honest.

Acceptance criteria:
- Add `docs/templates/MODEL_CARD.md`.

## 7. Add dataset card template
**Labels:** documentation, dataset-card  
**Goal:** Make dataset releases citable and auditable.

Acceptance criteria:
- Add `docs/templates/DATASET_CARD.md`.

## 8. Add first tutorial notebook
**Labels:** tutorial, docs  
**Goal:** Help new users validate data and train a baseline.

Acceptance criteria:
- Add notebook or Python script showing validation, training, metrics.

## 9. Add prior-art table
**Labels:** prior-art, research  
**Goal:** Avoid false novelty claims.

Acceptance criteria:
- Add table comparing SensorGenome with fluorescence databases, chemical sensor datasets, and spectroscopy ML tools.

## 10. Prepare v0.1 release notes
**Labels:** release, v0.1  
**Goal:** Ship an alpha release that looks professional.

Acceptance criteria:
- `releases/v0.1.0-alpha.md` exists.
- README links to release notes.
