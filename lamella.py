#!/usr/bin/python3

from numpy import cos, pi, sin

from lib import run, name_of_file
from lib.types import *


def f(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    x, y, z = y, z, x
    k = 0.50
    x *= k
    y *= k
    z *= k

    return 0.5 * (
        sin(2.0 * x) * cos(y) * sin(z)
        + sin(2.0 * y) * cos(z) * sin(x)
        + sin(2.0 * z) * cos(x) * sin(y)
    ) - 0.5 * (cos(2.0 * x) * cos(2.0 * z) + cos(2.0 * z) * cos(2.0 * x))


params = PlotParams(
    name=name_of_file(__file__),
    subdivisions=150 * 2,
    span=pi * 2.0,
    formula=f,
    size=100,
    thickness=0.6,
    granularity=0.3,
)
run(params)
