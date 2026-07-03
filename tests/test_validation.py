from sensorgenome.data.validation import validate_probe_response_csv


def test_sample_validates():
    result = validate_probe_response_csv("data/sample/probe_response_sample.csv")
    assert result.ok
    assert result.row_count == 25
