"""Copyright (c) 2024 galax maintainers. All rights reserved.

plotting_backends: Plotting dispatch backends
"""

__all__ = [
    "AbstractPlottingBackend",
    "AltairBackend",
    "BokehBackend",
    "GGPlotBackend",
    "MatplotlibBackend",
    "PlotlyBackend",
    "SeabornBackend",
]

from typing import final

from ._version import version as __version__  # noqa: F401


class AbstractPlottingBackend:
    """Abstract base class for plotting backends."""


@final
class MatplotlibBackend(AbstractPlottingBackend):
    """Matplotlib plotting backend."""


@final
class SeabornBackend(AbstractPlottingBackend):
    """Seaborn plotting backend."""


@final
class PlotlyBackend(AbstractPlottingBackend):
    """Plotly plotting backend."""


@final
class BokehBackend(AbstractPlottingBackend):
    """Bokeh plotting backend."""


@final
class AltairBackend(AbstractPlottingBackend):
    """Altair plotting backend."""


@final
class GGPlotBackend(AbstractPlottingBackend):
    """GGPlot plotting backend."""
