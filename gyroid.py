#!/usr/bin/python3

from numpy import cos, pi, sin

from lib import run, name_of_file
from lib.types import *


def f(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return cos(x) * sin(y) + cos(y) * sin(z) + cos(z) * sin(x)  # type: ignore


params = PlotParams(
    name=name_of_file(__file__),
    subdivisions=150,
    span=pi * 2.0,
    formula=f,
    size=50,
    thickness=0.5,
    granularity=0.3,
)

run(params)
