#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
subprocess.check_call([sys.executable, "scripts/compute_qrho.py"], cwd=ROOT)
