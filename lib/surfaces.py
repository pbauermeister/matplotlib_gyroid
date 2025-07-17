"""
Collection of mathematical surface formulas.
This module contains implementations of various minimal surfaces and periodic structures.
"""

from numpy import cos, pi, sin, sqrt, arctan2, power, where, abs, sinh
from .types import NDARRAY


def gyroid(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """
    The Gyroid surface: cos(x)sin(y) + cos(y)sin(z) + cos(z)sin(x) = 0

    Popular in 3D printing as infill pattern due to its structural properties.
    """
    return cos(x) * sin(y) + cos(y) * sin(z) + cos(z) * sin(x)


def schwarz_g(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """Schwarz G (Gyroid variant) surface."""
    return sin(x) * cos(y) + sin(z) * cos(x) + sin(y) * cos(z)


def l_surface(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """L surface (Lidinoid)."""
    return 0.5 * (
        sin(2.0 * x) * cos(y) * sin(z)
        + sin(2.0 * y) * cos(z) * sin(x)
        + sin(2.0 * z) * cos(x) * sin(y)
    ) - 0.5 * (
        cos(2.0 * x) * cos(2.0 * y) + cos(2.0 * y) * cos(2.0 * z) + cos(2.0 * z) * cos(2.0 * x)
    )


def icosahedron(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """Icosahedron surface."""
    S = 5
    return 2 - (
        cos(x + (1 + sqrt(S)) / 2 * y)
        + cos(x - (1 + sqrt(S)) / 2 * y) * cos(y + (1 + sqrt(S)) / 2 * z)
        + cos(y - (1 + sqrt(S)) / 2 * z)
        + cos(z - (1 + sqrt(S)) / 2 * x)
        + cos(z + (1 + sqrt(S)) / 2 * x)
    )


def p_w_hybrid(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """P-W hybrid surface."""
    return 10.0 * (
        cos(x) * cos(y) + (cos(y) * cos(z)) + (cos(z) * cos(x)) - 0.01 * (cos(x) * cos(y) * cos(z))
    )


def schwarz_d(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """Schwarz D (Diamond) surface."""
    return cos(x) * cos(y) * cos(z) - sin(x) * sin(y) * sin(z)


def iwp(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """IWP (I-graph and primitive) surface."""
    return cos(x) * cos(y) + cos(y) * cos(z) + cos(z) * cos(x) - cos(x) * cos(y) * cos(z)


def neovius(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """Neovius surface."""
    return 3 * (cos(x) + cos(y) + cos(z)) + 4 * (cos(x) + cos(y) + cos(z))


def schwarz_p(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """Schwarz P (Primitive) surface: -(cos(x) + cos(y) + cos(z)) = 0"""
    return -(cos(x) + cos(y) + cos(z))


def diamond(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """Diamond structure surface."""
    return (
        sin(x) * sin(y) * sin(z)
        + sin(x) * cos(y) * cos(z)
        + cos(x) * sin(y) * cos(z)
        + cos(x) * cos(y) * sin(z)
    )


def holes(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """Holes surface."""
    return (cos(x) + cos(y) + cos(z)) + 4 * cos(x) * cos(y) * cos(z)


def scherk_singly(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """Scherk's singly periodic surface: sin(z) = sinh(x) * sinh(y)"""
    zz = z / (5 / 3)
    xx = x
    yy = y
    return sinh(xx / 2.0) * sinh(yy / 2.0) - sin(zz)


def lamella(x: NDARRAY, y: NDARRAY, z: NDARRAY) -> NDARRAY:
    """Lamella-like surface (experimental)."""
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


def organite(x0: NDARRAY, y0: NDARRAY, z0: NDARRAY) -> NDARRAY:
    """Organic-looking surface with cylindrical distortions."""
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
    return where(y0 > 0, where(abs(z0) < 6.05, where(r0 < rmax, f(), 1.0), 1.0), 1.0)
