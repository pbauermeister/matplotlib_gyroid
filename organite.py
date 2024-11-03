#!/usr/bin/python3

from numpy import cos, pi, sin, sqrt, arctan2, power, where, abs

from lib import run, name_of_file
from lib.types import *


def f(x0: NDARRAY, y0: NDARRAY, z0: NDARRAY) -> NDARRAY:
    # to cylindric coordinates
    a = arctan2(x0, y0)
    r0 = sqrt(pow(x0, 2) + pow(y0, 2))

    # nasty cylindrical distortion
    r = power(1.0 - cos(r0 * pi), 4.0)

    # back to cartesian
    x = cos(a) * r
    y = sin(a) * r
    z = z0

    # sort of rotation
    x, y, z = y, z, x

    # x+y expansion, z compression
    k = 2.0
    x *= k
    y *= k
    z /= 8.0

    # it's a gyroid!
    def f() -> NDARRAY:
        return cos(x) * sin(y) + cos(y) * sin(z) + cos(z) * sin(x)

    # bounding box
    rmax = 2.0 * pi + 0.5
    return where(y0 > 0, where(abs(z0) < 6.05, where(r0 < rmax, f(), 1.0), 1.0), 1.0)  # type: ignore


params = PlotParams(
    name=name_of_file(__file__),
    subdivisions=150,
    span=pi * 2.0,
    formula=f,
    size=70,
    thickness=0.3,
    granularity=0.2,
)
run(params)
