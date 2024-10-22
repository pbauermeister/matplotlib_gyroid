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

    args = parser.parse_args()
    if not (args.generate_stl or args.view_plot):
        parser.error('No action requested.')
    return args


def run(params: PlotParams) -> None:
    args = parse_args(params.name)

    print(f'{params.name}: Computing surface...')
    vertices, faces = solver.compute_surface(params.span, params.subdivisions, params.formula)

    if args.generate_stl:
        stl.save_volume_stl(vertices, faces, params, Path(f'{params.name}.stl'))

    if args.view_plot:
        print(f'{params.name}: Viewing surface...')
        make_plot(vertices, faces)
        pyplot.show()

    print(f'{params.name}: Done.')


def name_of_file(f: str) -> str:
    s = Path(f).name
    return s.split('.')[0]
