#!/usr/bin/python3

from numpy import pi, sin, sinh

from lib import run
from lib.types import *


def scherk_singly(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    # sin(z) = sinh(x) * sinh(y)
    z = z / (5 / 3)
    return sinh(x / 2.0) * sinh(y / 2.0) - sin(z)


params = PlotParams(
    name="scherk-singly",
    subdivisions=150,
    span=pi * 4.0,
    formula=scherk_singly,
    size=10,
    thickness=0.8,
    granularity=0.1,
)

run(params)
