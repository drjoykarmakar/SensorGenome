from __future__ import annotations

import json
from pathlib import Path
import typer

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


if __name__ == "__main__":
    app()
