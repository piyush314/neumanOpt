# Installation

This page covers the shortest path to using the library and the extra steps
needed to build the GitHub Pages site locally.

## Library Install

```bash
python -m venv .venv
. .venv/bin/activate
pip install -e .
```

For plotting and tutorial execution:

```bash
pip install -e '.[plots,tutorials]'
```

## Smoke Checks

```bash
pytest -q tests
python scripts/reproduce_all.py
```

## Build The Documentation Site

The Pages site uses Jupyter Book 2 and executes the tutorial notebooks during
the build.

```bash
pip install -r docs/requirements.txt
cd docs
BASE_URL=/neumanOpt MPLBACKEND=Agg jupyter-book build --html --execute --force --ci
```

After a successful build, the generated site will be in `docs/_build/html`.
