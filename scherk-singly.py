#!/usr/bin/python3

from numpy import pi

from lib import run, name_of_file
from lib.types import *
from lib.surfaces import scherk_singly


params = PlotParams(
    name=name_of_file(__file__),
    subdivisions=150,
    span=pi * 4.0,
    formula=scherk_singly,
    size=150.0,
    thickness=0.4 * 3.0,
    granularity=0.3,
)

run(params)
