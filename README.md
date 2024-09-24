<h1 align='center'> plotting_backends </h1>
<h3 align="center">Plotting dispatch backends</h3>

## Installation

[![PyPI platforms][pypi-platforms]][pypi-link]
[![PyPI version][pypi-version]][pypi-link]

```bash
pip install plotting_backends
```

## Documentation

### Getting Started

```python
import plotting_backends
import plum


@dispatch.abstract
def plotting_func(
    backend: plotting_backends.AbstractPlottingBackend, x: Any, y: Any
) -> None: ...


@dispatch
def plotting_func(
    backend: plotting_backends.MatplotlibBackend, x: Any, y: Any
) -> None: ...
```

## Development

[![Actions Status][actions-badge]][actions-link]
[![ruff status][ruff-badge]][ruff-link]

We welcome contributions!

<!-- prettier-ignore-start -->

[actions-badge]:            https://github.com/GalacticDynamics/plotting_backends/workflows/CI/badge.svg
[actions-link]:             https://github.com/GalacticDynamics/plotting_backends/actions
[pypi-link]:                https://pypi.org/project/plotting_backends/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/plotting_backends
[pypi-version]:             https://img.shields.io/pypi/v/plotting_backends
[ruff-badge]:               https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
[ruff-link]:                https://github.com/astral-sh/ruff

<!-- prettier-ignore-end -->
