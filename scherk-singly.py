#!/usr/bin/python3

from numpy import pi, sin, sinh

from lib import run, name_of_file
from lib.types import *


def f(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    # sin(z) = sinh(x) * sinh(y)
    zz = z / (5 / 3)
    xx = x  # * 2.0 + y / 2.0
    yy = y
    return sinh(xx / 2.0) * sinh(yy / 2.0) - sin(zz)


params = PlotParams(
    name=name_of_file(__file__),
    subdivisions=150,
    span=pi * 4.0,
    formula=f,
    size=150.0,
    thickness=0.4 * 3.0,
    granularity=0.3,
)

run(params)
