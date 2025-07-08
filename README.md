<h1 align='center'> plotting_backends </h1>
<h3 align="center"> plotting dispatch backends </h3>

## Installation

[![PyPI platforms][pypi-platforms]][pypi-link]
[![PyPI version][pypi-version]][pypi-link]

```bash
pip install plotting_backends
```

## Documentation

The `plotting_backends` library provides a set of classes that can be used for
dispatching plotting functions to different backends.

The common base class is `AbstractPlottingBackend` and the pre-defined backends
are:

- `MatplotlibBackend`
- `SeabornBackend`
- `PlotlyBackend`
- `BokehBackend`
- `AltairBackend`
- `GGPlotBackend`

### Using with `functools.singledispatch`

This shows how to use `plotting_backends` with `functools.singledispatch`.

```python
import plotting_backends
from functools import singledispatch


@singledispatch
def plotting_func(
    backend: type[plotting_backends.AbstractPlottingBackend], x: Any, y: Any
) -> None: ...


@plotting_func.register
def matplotlib(
    backend: type[plotting_backends.MatplotlibBackend], x: Any, y: Any
) -> None: ...
```

### Using with `plum` (multiple dispatch)

This example shows how to use `plotting_backends` in conjunction with `plum`, a
multiple dispatch library.

```python
import plotting_backends
from plum import dispatch


@dispatch.abstract
def plotting_func(
    backend: type[plotting_backends.AbstractPlottingBackend], x: Any, y: Any
) -> None: ...


@dispatch
def plotting_func(
    backend: type[plotting_backends.MatplotlibBackend], x: Any, y: Any
) -> None: ...
```

---

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
