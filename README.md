# neumann-kernels

`neumann-kernels` is a Python library for evaluating truncated Neumann
polynomials with low-product radix kernels. It gives you exact and certified
kernel constructions, cost-model helpers, and tutorial notebooks so you can
replace expensive direct polynomial expansion with structured low-product
updates.

$$
S_d(B) = I + B + B^2 + \cdots + B^{d-1}.
$$

## Why This Gets Expensive

In inverse refinement and related matrix-polynomial updates, the dominant cost
is usually matrix-matrix multiplication. Direct evaluation of a degree-`d`
truncated Neumann polynomial costs `d - 1` products, so the method becomes
impractical as the target degree grows.

The same object appears naturally inside residual iterations of the form

$$
Y_{k+1} = Y_k T_r(R_k),
\qquad
R_k = I - A Y_k.
$$

## What The Library Provides

`neumann-kernels` packages exact radix-5 and radix-9 kernels, certified
radix-15 and radix-24 kernel data, cost-model helpers for choosing a radix at
a target degree, and tutorial notebooks that explain how to use and interpret
the shipped methods.

## Performance Payoff

The shipped radix-24 construction reaches degree 4096 in 21 matrix-matrix
products. Direct evaluation needs 4095.

## What Problem This Solves

Use `neumann-kernels` when you need one of these:

- fast evaluation of long truncated Neumann polynomials,
- explicit low-product kernels instead of generic polynomial-evaluation
  routines,
- certified higher-radix approximate kernels with machine-readable metadata,
- or a compact reference implementation of the kernel cost model.

For a target degree `d`, a kernel with radix `r` and kernel-product count `mu`
needs

$$
C(r,\mu,d) = (\mu + 2)\,\lceil \log_r d \rceil
$$

matrix-matrix products in the standard residual-update model. The `+2` term is
the update overhead per outer step.

## Benefit At A Glance

The figure below compares direct evaluation against the kernels shipped in the
library.

![Matrix-product count versus target degree](docs/_static/multiply_count_vs_degree.png)

## What Is In The Package

- exact kernel coefficients for radix-5 and radix-9,
- certified kernel records for radix-15 and radix-24,
- cost-model helpers such as `kernel_catalog()` and `multiply_count()`,
- error-map and residual-analysis helpers for deeper inspection,
- and beginner-oriented tutorials in both GitHub Pages and Colab form.

### Kernel Catalog

| Method | Radix | Kernel products `mu` | Full-step products `mu + 2` | `(mu + 2)/log2(radix)` | Status |
|---|---:|---:|---:|---:|---|
| Direct polynomial evaluation | - | - | `d - 1` | linear in `d` | exact baseline |
| Radix-5 | 5 | 2 | 4 | 1.723 | exact |
| Radix-9 | 9 | 3 | 5 | 1.577 | exact |
| Radix-15 | 15 | 4 | 6 | 1.536 | certified approximate |
| Radix-24 | 24 | 5 | 7 | 1.527 | certified approximate |

The same information is available programmatically through
`neumann_kernels.kernel_catalog()`.

## Install

Minimal install:

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

Install plotting and tutorial dependencies:

```bash
pip install -e '.[plots,tutorials]'
```

## Quick Start

```python
from neumann_kernels import kernel_catalog, load_certified_kernel, multiply_count

for row in kernel_catalog():
    print(
        row["display_name"],
        row["status"],
        round(row["asymptotic_coefficient"], 3),
    )

rad24 = load_certified_kernel("radix24")
print(rad24["safe_radii"])

print(multiply_count(24, 5, 4096))
```

What this tells you:

- `kernel_catalog()` lists the exact and certified options,
- `load_certified_kernel("radix24")` loads the shipped certification summary,
- `multiply_count(24, 5, 4096)` returns `21`.

## Learn The Library

Documentation site:

- Homepage: <https://piyush314.github.io/neumanOpt/>
- Installation guide: <https://piyush314.github.io/neumanOpt/install>
- First steps tutorial: <https://piyush314.github.io/neumanOpt/tutorials/first-steps>
- Certified kernels tutorial: <https://piyush314.github.io/neumanOpt/tutorials/certified-kernels>
- Cost model tutorial: <https://piyush314.github.io/neumanOpt/tutorials/cost-model-and-benefit-plot>
- Paper page: <https://piyush314.github.io/neumanOpt/paper>

Run in Colab:

- First steps: <https://colab.research.google.com/github/piyush314/neumanOpt/blob/main/docs/tutorials/01_first_steps.ipynb>
- Certified kernels: <https://colab.research.google.com/github/piyush314/neumanOpt/blob/main/docs/tutorials/02_certified_kernels.ipynb>
- Cost model walkthrough: <https://colab.research.google.com/github/piyush314/neumanOpt/blob/main/docs/tutorials/03_cost_model_and_benefit_plot.ipynb>

## Theory And Paper

If you want the theory behind the implementation, read
[`paper/arxiv.pdf`](paper/arxiv.pdf). The paper discusses:

- the exact radix-9 construction,
- certified higher-radix approximate constructions,
- local-structure and stability analysis,
- and the broader cost tradeoffs behind these kernels.

## Repository Layout

- `src/neumann_kernels/`: installable Python library.
- `data/certified/`: machine-readable certified kernel JSON files.
- `data/results/`: summary CSV and manifest files.
- `scripts/`: small utilities, including the README plot generator.
- `docs/`: GitHub Pages source, including the canonical tutorial notebooks.
- `paper/arxiv.pdf`: repository copy of the paper PDF.

## Where To Start

If you are new to the package, start with the
[documentation homepage](https://piyush314.github.io/neumanOpt/) or the
[first steps tutorial](https://piyush314.github.io/neumanOpt/tutorials/first-steps).
Then use `kernel_catalog()` to compare available kernels and
`load_certified_kernel()` to inspect the higher-radix certified data.
