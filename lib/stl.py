from pathlib import Path
from tempfile import NamedTemporaryFile

from meshlib import mrmeshpy  # type:ignore[import-untyped]
from numpy import zeros


import stl

from .types import *

################################################################################


def save_surface_stl(vertices: NDARRAY, faces: NDARRAY, dest: Path) -> None:
    # 2D surface in 3D space
    data = zeros(faces.shape[0], dtype=stl.mesh.Mesh.dtype)
    mesh = stl.mesh.Mesh(data, remove_empty_areas=False)  # type: ignore[no-untyped-call]
    for i, f in enumerate(faces):
        for j in range(3):
            mesh.vectors[i][j] = vertices[f[j], :]
    mesh.save(dest, mode=stl.Mode.ASCII)  # type: ignore[no-untyped-call]


def thicken(source: Path, params: PlotParams, dest: Path) -> mrmeshpy.Mesh:
    # load non-closed mesh
    sheet_mesh = mrmeshpy.loadMesh(source)

    k = params.size / params.subdivisions * 10.0
    m = mrmeshpy.Matrix3f.scale(k, k, k)
    a = mrmeshpy.AffineXf3f.linear(m)
    sheet_mesh.transform(a)

    # thin? save results
    if params.thickness == 0:
        return sheet_mesh

    # setup offset parameters
    offset_params = mrmeshpy.OffsetParameters()
    offset_params.voxelSize = params.granularity
    return mrmeshpy.offsetMesh(mp=sheet_mesh, offset=params.thickness, params=offset_params)


def save_volume_stl(vertices: NDARRAY, faces: NDARRAY, params: PlotParams, dest: Path) -> None:
    with NamedTemporaryFile(suffix=".stl") as f:
        print("Making STL of surface...")
        source = Path(Path(f.name))
        save_surface_stl(vertices, faces, source)
        f.seek(0)

        if params.thickness > 0:
            print("Thickening surface...")
        mesh = thicken(source, params, dest)

        print(f"Saving STL as '{dest}'...")
        mrmeshpy.saveMesh(mesh, dest)
