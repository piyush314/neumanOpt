# neumann-kernels

Companion software for the manuscript *Fast Evaluation of Truncated Neumann Series by Low-Product Radix Kernels*.

This public-lite release contains:
- exact kernel helpers for radix 5 and radix 9,
- bilinear ansatz evaluation for higher-radix kernels,
- residual-iteration and stability-bound utilities,
- certified coefficient/error-map JSON files for radix 15 and radix 24,
- one-command reproduction of the certified radius tables.

The repository intentionally omits the full internal certification engine while ORNL/DOE release review is pending. The certified data files shipped in `data/certified/` are the same artifacts cited by the paper.

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
pip install numpy
python scripts/reproduce_all.py
```

If `matplotlib` is installed, `scripts/compute_qrho.py` can also emit quick plots in addition to CSV output.
