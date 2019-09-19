#!/usr/bin/python3

import numpy
from skimage import measure
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import stl

################################################################################

def compute_volume(span, resolution, lattice_param, f):
    x, y, z = span * numpy.mgrid[-1:1:resolution,
                                 -1:1:resolution,
                                 -1:1:resolution] * lattice_param
    volume = f(x, y, z)
    vertices, faces, normals, vals = measure.marching_cubes_lewiner(
        volume, 0,
        spacing=(0.1, 0.1, 0.1),
        allow_degenerate=True)
    return vertices, faces

def save_stl(vertices, faces, filename):
    data = numpy.zeros(faces.shape[0], dtype=stl.mesh.Mesh.dtype)
    mesh = stl.mesh.Mesh(data, remove_empty_areas=False)
    for i, f in enumerate(faces):
        for j in range(3):
            mesh.vectors[i][j] = vertices[f[j], :]
    mesh.save(filename, mode=stl.Mode.ASCII)

def make_plot(vertices, faces):
    fig = pyplot.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_trisurf(
        vertices[:, 0], vertices[:, 1], faces, vertices[:, 2],
        cmap='ocean',
        lw=1)
    return pyplot
