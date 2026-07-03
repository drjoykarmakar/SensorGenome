from __future__ import annotations

from pathlib import Path
import json
from typing import Any


def read_json(path: str | Path) -> Any:
    return json.loads(Path(path).read_text())


def write_json(obj: Any, path: str | Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2))
