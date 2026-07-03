from __future__ import annotations

import hashlib
import numpy as np
import pandas as pd


def hashed_smiles_features(smiles: str, n_bits: int = 256) -> np.ndarray:
    """Dependency-light stand-in for molecular fingerprints.

    Replace with RDKit Morgan fingerprints in production. This keeps the starter
    repository installable even where RDKit is unavailable.
    """
    arr = np.zeros(n_bits, dtype=float)
    if not isinstance(smiles, str) or not smiles:
        return arr
    for token_size in (1, 2, 3):
        for i in range(max(1, len(smiles) - token_size + 1)):
            token = smiles[i : i + token_size]
            digest = hashlib.sha256(token.encode()).hexdigest()
            idx = int(digest, 16) % n_bits
            arr[idx] += 1.0
    norm = np.linalg.norm(arr)
    return arr / norm if norm else arr


def featurize_dataframe(df: pd.DataFrame, n_bits: int = 256) -> pd.DataFrame:
    fps = np.vstack([hashed_smiles_features(s, n_bits=n_bits) for s in df["smiles"].fillna("")])
    fp_df = pd.DataFrame(fps, columns=[f"fp_{i}" for i in range(n_bits)])

    numeric_cols = [c for c in ["ph", "excitation_nm", "emission_nm", "sensor_concentration_um", "analyte_concentration_um"] if c in df.columns]
    numeric = df[numeric_cols].copy() if numeric_cols else pd.DataFrame(index=df.index)
    for col in numeric_cols:
        numeric[col] = pd.to_numeric(numeric[col], errors="coerce").fillna(numeric[col].median())

    categorical_cols = [c for c in ["modality", "mechanism", "solvent", "matrix", "role"] if c in df.columns]
    categorical = pd.get_dummies(df[categorical_cols].fillna("unknown"), dummy_na=False) if categorical_cols else pd.DataFrame(index=df.index)

    return pd.concat([fp_df.reset_index(drop=True), numeric.reset_index(drop=True), categorical.reset_index(drop=True)], axis=1)
