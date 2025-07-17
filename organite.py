#!/usr/bin/python3

from numpy import pi

from lib import run, name_of_file
from lib.types import *
from lib.surfaces import organite


params = PlotParams(
    name=name_of_file(__file__),
    subdivisions=150,
    span=pi * 2.0,
    formula=organite,
    size=70,
    thickness=0.3,
    granularity=0.2,
)
run(params)
