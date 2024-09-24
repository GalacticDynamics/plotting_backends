"""Copyright (c) 2024 galax maintainers. All rights reserved.

plotting_backends: Plotting dispatch backends
"""

__all__ = [
    "AbstractPlottingBackend",
    "MatplotlibBackend",
]

from typing import final

from ._version import version as __version__  # noqa: F401


class AbstractPlottingBackend:
    """Abstract base class for plotting backends."""


@final
class MatplotlibBackend(AbstractPlottingBackend):
    """Matplotlib plotting backend."""
