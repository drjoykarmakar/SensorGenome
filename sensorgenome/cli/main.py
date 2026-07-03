from __future__ import annotations

import json
from pathlib import Path
import pandas as pd
import typer

from sensorgenome.active_learning.selection import select_diverse_uncertain_candidates
from sensorgenome.data.validation import validate_probe_response_csv
from sensorgenome.models.baseline import train_baseline

app = typer.Typer(help="SensorGenome command-line tools.")


@app.command()
def validate(path: Path):
    """Validate a probe-response CSV against the starter schema."""
    result = validate_probe_response_csv(path)
    typer.echo(json.dumps(result.__dict__, indent=2))
    if not result.ok:
        raise typer.Exit(code=1)


@app.command("train-baseline")
def train_baseline_cmd(
    path: Path,
    target: str = typer.Option("response_ratio", help="Target column."),
    out: Path = typer.Option(Path("reports/baseline_metrics.json"), help="Metrics output JSON."),
):
    """Train a transparent baseline model."""
    metrics = train_baseline(path, target=target, out=out)
    typer.echo(json.dumps(metrics, indent=2))


@app.command("select-next")
def select_next_cmd(
    path: Path,
    k: int = typer.Option(5, help="Number of next experiments to select."),
):
    """Select next candidate sensor experiments with a transparent active-learning heuristic."""
    df = pd.read_csv(path)
    if "predicted_response" not in df.columns:
        df["predicted_response"] = df.get("response_ratio", 0.0)
    if "uncertainty" not in df.columns:
        # Simple demo uncertainty: prioritize lower evidence-grade records for follow-up.
        grade_to_uncertainty = {"A": 0.25, "B": 0.5, "C": 0.75, "D": 1.0}
        df["uncertainty"] = df.get("evidence_grade", "D").map(grade_to_uncertainty).fillna(1.0)
    selected = select_diverse_uncertain_candidates(df, k=k)
    cols = [c for c in ["sensor_id", "sensor_name", "scaffold", "analyte_name", "role", "response_ratio", "uncertainty", "acquisition_score"] if c in selected.columns]
    typer.echo(selected[cols].to_csv(index=False))


if __name__ == "__main__":
    app()
