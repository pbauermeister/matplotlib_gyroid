#!/usr/bin/python3

from equation_surface import compute_volume, save_stl, make_plot
from numpy import sin, cos, pi, sqrt

lattice_param = 1.0
resolution = 31j
span = pi
strut_param = 0.0

def gyroid(x, y, z):
    return cos(x)*sin(y) + cos(y)*sin(z) + cos(z)*sin(x) - strut_param

vertices, faces = compute_volume(span, resolution, lattice_param, gyroid)
save_stl(vertices, faces, 'Gyroid.stl')
plot = make_plot(vertices, faces)

plot.show()
