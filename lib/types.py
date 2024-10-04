from dataclasses import dataclass
from typing import Any, Callable

import numpy.typing as npt

NDARRAY = npt.NDArray[Any]
Formula = Callable[[NDARRAY, NDARRAY, NDARRAY], NDARRAY]


@dataclass
class PlotParams:
    name: str

    # math surface space
    subdivisions: int
    span: float
    formula: Formula

    # conversion to solid space
    size: float = 40.0
    thickness: float = 0.3
    granularity: float = 0.1
