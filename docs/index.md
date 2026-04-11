# neumann-kernels

`neumann-kernels` is a standalone Python library for low-product radix kernels
for truncated Neumann series, matrix inverse refinement, and certified
higher-radix contraction analysis.

The core target is the truncated Neumann polynomial

$$
S_d(B) = I + B + B^2 + \cdots + B^{d-1},
$$

and the library packages exact and certified approximate kernels that reduce the
matrix-product count needed to reach large truncation degrees.

## Why This Library Exists

- It gives you exact radix-5 and radix-9 kernel helpers.
- It ships certified radix-15 and radix-24 kernel data as machine-readable JSON.
- It exposes a simple cost model for choosing a radix at a target degree.
- It includes beginner tutorials that explain the object, the certificates, and
  the benefit plot in an order that a first-time reader can follow.

## Benefit At A Glance

The figure below compares direct evaluation against the kernels shipped here.

![Matrix-product count versus target degree](_static/multiply_count_vs_degree.png)

## Quick Start

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e '.[plots,tutorials]'
pytest -q tests
```

## Start Here

- [Installation and local build guide](install.md)
- [First steps tutorial](tutorials/01_first_steps.ipynb)
- [Certified kernels tutorial](tutorials/02_certified_kernels.ipynb)
- [Cost model walkthrough](tutorials/03_cost_model_and_benefit_plot.ipynb)
- [Companion paper](paper.md)

## Run In Colab

If you want zero local setup, open the canonical notebooks directly in Google
Colab:

- [First steps in Colab](https://colab.research.google.com/github/piyush314/neumanOpt/blob/main/docs/tutorials/01_first_steps.ipynb)
- [Certified kernels in Colab](https://colab.research.google.com/github/piyush314/neumanOpt/blob/main/docs/tutorials/02_certified_kernels.ipynb)
- [Cost model walkthrough in Colab](https://colab.research.google.com/github/piyush314/neumanOpt/blob/main/docs/tutorials/03_cost_model_and_benefit_plot.ipynb)
