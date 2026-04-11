#!/usr/bin/env python3
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from neumann_kernels import kernel_catalog, multiply_count


def main():
    outdir = ROOT / "docs" / "_static"
    outdir.mkdir(exist_ok=True)

    degrees = np.array([2 ** k for k in range(3, 14)], dtype=int)

    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(
        degrees,
        degrees - 1,
        marker="o",
        linewidth=2,
        color="#6B7280",
        label="Direct evaluation",
    )

    colors = {
        "Radix-5": "#C84C09",
        "Radix-9": "#E0A100",
        "Radix-15": "#2A7F62",
        "Radix-24": "#2457A5",
    }
    for entry in kernel_catalog():
        counts = [
            multiply_count(entry["radix"], entry["num_products"], int(degree))
            for degree in degrees
        ]
        label = f'{entry["display_name"]} ({entry["status"]})'
        ax.plot(
            degrees,
            counts,
            marker="o",
            linewidth=2,
            color=colors[entry["display_name"]],
            label=label,
        )

    ax.set_xscale("log", base=2)
    ax.set_xlabel("Target truncated degree d")
    ax.set_ylabel("Matrix-matrix products")
    ax.set_title("Product count to reach degree d")
    ax.grid(alpha=0.25)
    ax.legend(frameon=False, ncol=2)
    plt.tight_layout()
    fig.savefig(outdir / "multiply_count_vs_degree.png", dpi=180)


if __name__ == "__main__":
    main()
