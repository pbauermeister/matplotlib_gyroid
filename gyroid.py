#!/usr/bin/python3

from numpy import pi

from lib import run, name_of_file
from lib.types import *
from lib.surfaces import gyroid


params = PlotParams(
    name=name_of_file(__file__),
    subdivisions=150,
    span=pi * 2.0,
    formula=gyroid,
    size=40,
    thickness=0.4,
    granularity=0.4,
)

run(params)
