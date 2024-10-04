"""
Solve the formula for %s, and optionally show an interactive plot,
or export as STL.
"""

from argparse import ArgumentParser, Namespace
from pathlib import Path

from matplotlib import pyplot

from . import solver, stl
from .types import *


def make_plot(vertices: NDARRAY, faces: NDARRAY) -> None:
    fig = pyplot.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], faces, vertices[:, 2], cmap='ocean', lw=1)  # type: ignore[attr-defined]


def parse_args(name: str) -> Namespace:
    assert __doc__
    parser = ArgumentParser(description=__doc__ % name)
    parser.add_argument(
        '-p',
        '--view-plot',
        action='store_true',
        help='launch interactive plot viewer',
    )
    parser.add_argument(
        '-s',
        '--generate-stl',
        action='store_true',
        help='generate STL file',
    )
    return parser.parse_args()


def run(params: PlotParams) -> None:
    args = parse_args(params.name)

    print('Computing surface...')
    vertices, faces = solver.compute_surface(params.span, params.subdivisions, params.formula)

    if args.generate_stl:
        stl.save_volume_stl(vertices, faces, params, Path(f'{params.name}.stl'))

    if args.view_plot:
        print('Viewing surface...')
        make_plot(vertices, faces)
        pyplot.show()

    print('Done.')
