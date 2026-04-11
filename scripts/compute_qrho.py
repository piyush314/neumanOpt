#!/usr/bin/env python3
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from neumann_kernels.io import load_certified_kernel

with (ROOT / "data" / "results" / "qrho_summary.csv").open("w", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["kernel_id", "eta_certified", "q_certified", "q_estimated"])
    for kernel_id in ["radix15", "radix24"]:
        data = load_certified_kernel(kernel_id, root=ROOT)
        radii = data["safe_radii"]
        writer.writerow([kernel_id, radii["eta_certified"], radii["q_certified"], radii["q_estimated"]])
