#!/usr/bin/python3

from numpy import pi

from lib import run, name_of_file
from lib.types import *
from lib.surfaces import lamella


params = PlotParams(
    name=name_of_file(__file__),
    subdivisions=150 * 2,
    span=pi * 2.0,
    formula=lamella,
    size=100,
    thickness=0.6,
    granularity=0.3,
)
run(params)
