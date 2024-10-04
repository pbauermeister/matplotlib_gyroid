#!/usr/bin/python3

from numpy import pi, sin, sinh

from lib import NDARRAY, PlotParams, run
from lib.types import *


def scherk_singly(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    # sin(z) = sinh(x) * sinh(y)
    return sinh(x / 2.0) * sinh(y / 2.0) - sin(z / 1.5 - pi / 2.0)


params = PlotParams(
    name="scherk-singly",
    subdivisions=150,
    span=pi * 6.0,
    formula=scherk_singly,
    scale_factor=4.0,
    thickness=0.8,
    granularity=0.1,
)

run(params)
