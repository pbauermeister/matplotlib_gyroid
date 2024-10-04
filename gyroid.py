#!/usr/bin/python3

from numpy import cos, pi, sin

from lib import run
from lib.types import *

STRUT_PARAM = 0.0


def gyroid(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return cos(x) * sin(y) + cos(y) * sin(z) + cos(z) * sin(x) - STRUT_PARAM  # type: ignore


params = PlotParams(
    name="gyroid",
    subdivisions=150,
    span=pi * 2.0,
    formula=gyroid,
    size=60,
    thickness=0.8,
    granularity=0.1,
)

run(params)
