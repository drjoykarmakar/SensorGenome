from sensorgenome.models.baseline import train_baseline


def test_train_baseline_runs(tmp_path):
    out = tmp_path / "metrics.json"
    metrics = train_baseline("data/sample/probe_response_sample.csv", "response_ratio", out=out)
    assert metrics["n"] == 5
    assert out.exists()
