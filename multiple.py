#!/usr/bin/python3

from numpy import pi

from lib import run, name_of_file
from lib.types import *
from lib.surfaces import (
    schwarz_g,
    l_surface,
    icosahedron,
    p_w_hybrid,
    schwarz_d,
    iwp,
    neovius,
    schwarz_p,
    diamond,
    holes,
)


for f in (
    schwarz_g,
    l_surface,
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
