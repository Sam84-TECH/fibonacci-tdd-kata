# Fibonacci TDD Kata

[![Tests](https://github.com/Sam84-TECH/fibonacci-tdd-kata/actions/workflows/tests.yml/badge.svg)](https://github.com/Sam84-TECH/fibonacci-tdd-kata/actions/workflows/tests.yml)

A TDD kata on the Fibonacci sequence: from exploration in a Marimo notebook to a tested Python package, with a command-line interface and a web demo.

**Live demo:** https://sam84-tech.github.io/fibonacci-tdd-kata/

## Definition

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)   for n >= 2
``

## Installation

Requirement: [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/Sam84-TECH/fibonacci-tdd-kata.git
cd fibonacci-tdd-kata
uv sync --all-groups
```

## Usage

### In Python

```python
from fibonacci_kata import fibonacci

fibonacci(10)  # 55
```

### From the command line

```bash
uv run fibonacci-kata 10                  # 55
uv run fibonacci-kata --start 0 --end 10  # 0 1 1 2 3 5 8 ... 55 (one per line)
```

### Marimo notebooks

```bash
uv run marimo edit notebooks/notebook.py             # the TDD kata, step by step
uv run marimo edit notebooks/fibonacci_explorer.py   # interactive explorer
```

## Development

```bash
uv run pytest --cov=src --cov-report=term-missing   # tests + coverage (>= 90%)
uv run ruff format .                                # formatting
uv run ruff check .                                 # linting
uv run mypy src                                     # type checking
```

## Project structure

```
fibonacci-tdd-kata/
├── .github/workflows/
│   ├── tests.yml          # lint, format, type check, tests + coverage
│   ├── publish.yml        # PyPI publishing (on release)
│   └── deploy-pages.yml   # notebook deployment to GitHub Pages
├── notebooks/
│   ├── notebook.py            # TDD kata notebook
│   └── fibonacci_explorer.py  # interactive notebook
├── src/fibonacci_kata/
│   ├── __init__.py
│   ├── core.py            # business logic
│   └── cli.py             # command-line interface
├── tests/
│   ├── test_core.py
│   └── test_cli.py
├── pyproject.toml
└── README.md
```

## Git workflow

- One commit per Red-Green-Refactor cycle
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `ci:`, `docs:`)
- One branch per feature, merged through a Pull Request
- CI must be green before merging into `main`

## CI/CD

- **Tests**: on every push and Pull Request to `main` (Python 3.11, 3.12, 3.13)
- **Deployment**: on every push to `main`, the explorer notebook is exported to WebAssembly and published on GitHub Pages, only if the tests pass
- **Publishing**: when a GitHub release is created, the package is built and published to PyPI

## Author

KOUYELE Samaa Ashley, Refresher in Computer Science 2026-2027