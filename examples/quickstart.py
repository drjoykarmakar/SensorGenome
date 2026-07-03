from sensorgenome.data.validation import validate_probe_response_csv
from sensorgenome.models.baseline import train_baseline

path = "data/sample/probe_response_sample.csv"
print(validate_probe_response_csv(path))
print(train_baseline(path, target="response_ratio"))
