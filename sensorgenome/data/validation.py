from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import pandas as pd

REQUIRED_PROBE_RESPONSE_COLUMNS = {
    "sensor_id",
    "sensor_name",
    "smiles",
    "analyte_name",
    "role",
    "modality",
    "mechanism",
    "solvent",
    "ph",
    "matrix",
    "excitation_nm",
    "emission_nm",
    "sensor_concentration_um",
    "analyte_concentration_um",
    "response_ratio",
    "evidence_grade",
}


@dataclass
class ValidationResult:
    ok: bool
    missing_columns: list[str]
    row_count: int
    warnings: list[str]


def validate_probe_response_csv(path: str | Path) -> ValidationResult:
    df = pd.read_csv(path)
    missing = sorted(REQUIRED_PROBE_RESPONSE_COLUMNS - set(df.columns))
    warnings: list[str] = []

    if "response_ratio" in df.columns and (df["response_ratio"] < 0).any():
        warnings.append("Negative response_ratio values found.")
    if "ph" in df.columns and ((df["ph"] < 0) | (df["ph"] > 14)).any():
        warnings.append("pH values outside 0-14 found.")
    if "evidence_grade" in df.columns:
        bad = set(df["evidence_grade"].dropna()) - {"A", "B", "C", "D"}
        if bad:
            warnings.append(f"Unexpected evidence grades: {sorted(bad)}")

    return ValidationResult(ok=not missing, missing_columns=missing, row_count=len(df), warnings=warnings)
