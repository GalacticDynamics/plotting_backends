# /// script
# requires-python = ">=3.11"
# dependencies = ["resvg-py"]
# ///
# Copyright (c) 2024 galax maintainers. All rights reserved.
"""Draw the plotting_backends logo: one plotting call, three backends.

A dot, the plotting call, branching to three small charts. Each shows the same
plot, drawn by a different backend in its own colour. The shapes are vector, so
the logo is written as an SVG, sharp at any size; for a bitmap, name a .png and
give its size::

    uv run docs/_static/make_logo.py                     # favicon.svg
    uv run docs/_static/make_logo.py --size 2048 big.png
"""

import argparse
from pathlib import Path

NAVY = "#030a23"  # GalacticDynamics' navy
BACKENDS = ("#66a19a", "#4fb8e8", "#7738eb")  # each backend's colour, top first

# In a 64-unit square: the call's centre and radius, and each chart's left x,
# its side, and the top y of each.
CALL = (12, 32, 6)
CHART_X, CHART_SIZE, CHART_TOPS = 36, 16, (4, 24, 44)
# The plot every backend draws, as points in its chart: 0-1 across, 0-1 down.
PLOT = ((0.15, 0.78), (0.4, 0.42), (0.62, 0.6), (0.86, 0.18))

SVG = """\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="512" height="512">
  <circle cx="{cx:g}" cy="{cy:g}" r="{cr:g}" fill="{navy}"/>
  <g fill="none" stroke-linecap="round" stroke-linejoin="round">
{branches}
{charts}
  </g>
</svg>
"""


def chart(top: float, colour: str) -> str:
    """Return one backend's chart: a frame, and the plot in ``colour``."""
    x, s = CHART_X, CHART_SIZE
    line = "L".join(f"{x + u * s:.2f} {top + v * s:.2f}" for u, v in PLOT)
    return (
        f'    <rect x="{x:g}" y="{top:g}" width="{s:g}" height="{s:g}" rx="2.5"'
        f' fill="#fff" stroke="{NAVY}" stroke-width="2"/>\n'
        f'    <path d="M{line}" stroke="{colour}" stroke-width="2.4"/>'
    )


def svg() -> str:
    """Return the logo as SVG text."""
    cx, cy, cr = CALL
    middle = CHART_SIZE / 2
    branches = "\n".join(
        f'    <path d="M{cx + cr:g} {cy:g}C{cx + 16:g} {cy:g} {cx + 14:g}'
        f' {top + middle:g} {CHART_X - 2:g} {top + middle:g}"'
        f' stroke="{NAVY}" stroke-width="2.4"/>'
        for top in CHART_TOPS
    )
    charts = "\n".join(
        chart(top, colour) for top, colour in zip(CHART_TOPS, BACKENDS, strict=True)
    )
    return SVG.format(
        cx=cx,
        cy=cy,
        cr=cr,
        navy=NAVY,
        branches=branches,
        charts=charts,
    )


def main() -> None:
    """Parse the command line and save the logo."""
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument(
        "out",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("favicon.svg"),
        help="output file, SVG or PNG by its extension (default: favicon.svg)",
    )
    parser.add_argument(
        "--size",
        type=int,
        default=512,
        help="pixels per side, for a PNG",
    )
    args = parser.parse_args()

    if args.out.suffix == ".svg":
        args.out.write_text(svg())
    else:
        import resvg_py  # noqa: PLC0415  # only a PNG needs a renderer

        png = resvg_py.svg_to_bytes(svg_string=svg(), width=args.size)
        args.out.write_bytes(bytes(png))


if __name__ == "__main__":
    main()
