"""Test the package itself."""

import importlib.metadata

import plotting_backends as pkg


def test_version() -> None:
    """Test the package version."""
    assert importlib.metadata.version("plotting_backends") == pkg.__version__  # type: ignore[attr-defined]
