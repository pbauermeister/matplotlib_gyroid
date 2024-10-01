#!/usr/bin/python3

from typing import Callable, Any

import numpy.typing as npt
import stl
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D  # type: ignore[import-untyped]
from numpy import mgrid  # type: ignore[attr-defined]
from numpy import zeros
from skimage import measure
from dataclasses import dataclass

################################################################################

NDARRAY = npt.NDArray[Any]

Formula = Callable[[NDARRAY, NDARRAY, NDARRAY], NDARRAY]


@dataclass
class PlotParams:
    name: str
    lattice_param: float
    resolution: complex
    span: float
    formula: Formula


def compute_volume(
    span: float, resolution: complex, lattice_param: float, f: Formula
) -> tuple[NDARRAY, NDARRAY]:
    mg = mgrid[-1:1:resolution, -1:1:resolution, -1:1:resolution]  # type: ignore
    x, y, z = span * mg * lattice_param
    volume = f(x, y, z)
    vertices, faces, normals, vals = measure.marching_cubes(
        volume,
        0,
        spacing=(0.1, 0.1, 0.1),
        allow_degenerate=True,
    )  # type: ignore[no-untyped-call]

    return vertices, faces


def save_stl(vertices: NDARRAY, faces: NDARRAY, filename: str) -> None:
    data = zeros(faces.shape[0], dtype=stl.mesh.Mesh.dtype)
    mesh = stl.mesh.Mesh(data, remove_empty_areas=False)  # type: ignore[no-untyped-call]
    for i, f in enumerate(faces):
        for j in range(3):
            mesh.vectors[i][j] = vertices[f[j], :]
    mesh.save(filename, mode=stl.Mode.ASCII)  # type: ignore[no-untyped-call]


def make_plot(vertices: NDARRAY, faces: NDARRAY) -> None:
    fig = pyplot.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.plot_trisurf(vertices[:, 0], vertices[:, 1], faces, vertices[:, 2], cmap="ocean", lw=1)  # type: ignore[attr-defined]


def run(params: PlotParams) -> None:
    vertices, faces = compute_volume(
        params.span, params.resolution, params.lattice_param, params.formula
    )
    save_stl(vertices, faces, f"{params.name}.stl")
    make_plot(vertices, faces)
    pyplot.show()
