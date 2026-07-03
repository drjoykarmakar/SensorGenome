from __future__ import annotations

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, HttpUrl


class Modality(str, Enum):
    fluorescence = "fluorescence"
    colorimetric = "colorimetric"
    raman = "raman"
    electrochemical = "electrochemical"
    chemiluminescence = "chemiluminescence"
    other = "other"


class SensorRecord(BaseModel):
    sensor_id: str
    sensor_name: str
    smiles: str
    scaffold: Optional[str] = None
    modality: Modality = Modality.fluorescence
    mechanism: Optional[str] = Field(default=None, description="PET, ICT, FRET, ESIPT, CHEF, CHEQ, reaction-based, host-guest, etc.")
    source: Optional[str] = None


class AnalyteRecord(BaseModel):
    analyte_id: str
    analyte_name: str
    analyte_class: Optional[str] = None
    smiles: Optional[str] = None
    role: str = Field(default="target", description="target, interferent, control")


class AssayRecord(BaseModel):
    assay_id: str
    sensor_id: str
    analyte_id: str
    modality: Modality
    solvent: str
    buffer: Optional[str] = None
    ph: Optional[float] = None
    matrix: Optional[str] = None
    temperature_c: Optional[float] = None
    excitation_nm: Optional[float] = None
    emission_nm: Optional[float] = None
    sensor_concentration_um: Optional[float] = None
    analyte_concentration_um: Optional[float] = None
    instrument: Optional[str] = None
    protocol_url: Optional[HttpUrl] = None


class ResponseRecord(BaseModel):
    response_id: str
    assay_id: str
    response_ratio: float = Field(description="Signal_with_analyte / signal_control")
    lod_um: Optional[float] = None
    response_time_s: Optional[float] = None
    selectivity_index: Optional[float] = None
    replicated_n: Optional[int] = None
    uncertainty: Optional[float] = None
    evidence_grade: str = Field(default="C", description="A=prospective raw data, B=curated full metadata, C=partial literature, D=low confidence")


class ExperimentRecord(BaseModel):
    experiment_id: str
    scientific_question: str
    hypothesis: str
    sensor_id: str
    analyte_id: str
    assay_id: str
    response_id: Optional[str] = None
    next_action: Optional[str] = None
