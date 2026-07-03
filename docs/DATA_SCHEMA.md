# Data Schema

## Required CSV columns

- `sensor_id`: stable identifier.
- `sensor_name`: human-readable name.
- `smiles`: sensor structure.
- `scaffold`: molecular family or scaffold.
- `analyte_name`: target, interferent, or control.
- `role`: target, interferent, or control.
- `modality`: fluorescence, colorimetric, Raman, electrochemical, chemiluminescence, or other.
- `mechanism`: PET, ICT, FRET, ESIPT, CHEF, CHEQ, reaction-based, host-guest, aggregation, unknown.
- `solvent`: solvent or solvent mixture.
- `ph`: assay pH.
- `matrix`: buffer, serum, urine, water, cell lysate, etc.
- `excitation_nm`: excitation wavelength for fluorescence assays.
- `emission_nm`: emission wavelength monitored.
- `sensor_concentration_um`: sensor concentration.
- `analyte_concentration_um`: analyte concentration.
- `response_ratio`: signal with analyte divided by control signal.
- `lod_um`: limit of detection where available.
- `response_time_s`: response time.
- `selectivity_index`: target response relative to interferent response.
- `evidence_grade`: A, B, C, or D.

## Evidence grades

- A: prospective raw data with full metadata.
- B: curated literature data with sufficient metadata.
- C: partial literature data.
- D: low-confidence or ambiguous data.
