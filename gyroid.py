#!/usr/bin/python3

from numpy import cos, pi, sin
from equation_surface import run, NDARRAY, PlotParams

STRUT_PARAM = 0.0


def gyroid(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return cos(x) * sin(y) + cos(y) * sin(z) + cos(z) * sin(x) - STRUT_PARAM  # type: ignore


params = PlotParams(
    name="gyroid",
    lattice_param=1.0,
    resolution=31j,
    span=pi,
    formula=gyroid,
)

run(params)
