#!/usr/bin/python3

from numpy import cos, pi, sin, sqrt

from lib import run, name_of_file
from lib.types import *


def schwarz_g(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return sin(x) * cos(y) + sin(z) * cos(x) + sin(y) * cos(z)


def l(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return 0.5 * (
        sin(2.0 * x) * cos(y) * sin(z)
        + sin(2.0 * y) * cos(z) * sin(x)
        + sin(2.0 * z) * cos(x) * sin(y)
    ) - 0.5 * (
        cos(2.0 * x) * cos(2.0 * y) + cos(2.0 * y) * cos(2.0 * z) + cos(2.0 * z) * cos(2.0 * x)
    )


def icosahedron(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    # bugged?
    S = 5
    return 2 - (
        cos(x + (1 + sqrt(S)) / 2 * y)
        + cos(x - (1 + sqrt(S)) / 2 * y) * cos(y + (1 + sqrt(S)) / 2 * z)
        + cos(y - (1 + sqrt(S)) / 2 * z)
        + cos(z - (1 + sqrt(S)) / 2 * x)
        + cos(z + (1 + sqrt(S)) / 2 * x)
    )


def p_w_hybrid(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return 10.0 * (
        cos(x) * cos(y) + (cos(y) * cos(z)) + (cos(z) * cos(x)) - 0.01 * (cos(x) * cos(y) * cos(z))
    )


def schwarz_d(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return cos(x) * cos(y) * cos(z) - sin(x) * sin(y) * sin(z)


def iwp(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return cos(x) * cos(y) + cos(y) * cos(z) + cos(z) * cos(x) - cos(x) * cos(y) * cos(z)


def neovius(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return 3 * (cos(x) + cos(y) + cos(z)) + 4 * (cos(x) + cos(y) + cos(z))


def schwarz_p(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return -(cos(x) + cos(y) + cos(z))


def diamond(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return (
        sin(x) * sin(y) * sin(z)
        + sin(x) * cos(y) * cos(z)
        + cos(x) * sin(y) * cos(z)
        + cos(x) * cos(y) * sin(z)
    )


def holes(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    return (cos(x) + cos(y) + cos(z)) + 4 * cos(x) * cos(y) * cos(z)


for f in (
    schwarz_g,
    l,
    icosahedron,
    p_w_hybrid,
    schwarz_d,
    iwp,
    neovius,
    schwarz_p,
    diamond,
    holes,
):
    params = PlotParams(
        name=f.__name__,
        subdivisions=150,
        span=pi * 2.0,
        formula=f,
        size=50,  # 30,
        thickness=0.5,
        granularity=0.2,
    )
    run(params)
