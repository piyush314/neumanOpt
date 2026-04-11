import json
from pathlib import Path

def load_certified_kernel(kernel_id, root=None):
    root = Path(root or Path(__file__).resolve().parents[2])
    path = root / "data" / "certified" / f"certified_coeffs_{kernel_id}.json"
    return json.loads(path.read_text())
