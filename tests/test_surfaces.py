"""
Test suite for surface generation functionality.
"""

import numpy as np

from lib.solver import compute_surface
from lib.types import PlotParams
from lib.surfaces import gyroid, schwarz_p


class TestSurfaceFormulas:
    """Test mathematical surface formulas."""

    def test_gyroid_basic(self):
        """Test basic gyroid function."""
        x = np.array([0.0, np.pi / 2, np.pi])
        y = np.array([0.0, np.pi / 2, np.pi])
        z = np.array([0.0, np.pi / 2, np.pi])

        result = gyroid(x, y, z)

        assert isinstance(result, np.ndarray)
        assert result.shape == (3,)
        assert np.all(np.isfinite(result))

    def test_schwarz_p_basic(self):
        """Test basic Schwarz P function."""
        x = np.array([0.0, np.pi / 2, np.pi])
        y = np.array([0.0, np.pi / 2, np.pi])
        z = np.array([0.0, np.pi / 2, np.pi])

        result = schwarz_p(x, y, z)

        assert isinstance(result, np.ndarray)
        assert result.shape == (3,)
        assert np.all(np.isfinite(result))


class TestSurfaceGeneration:
    """Test surface mesh generation."""

    def test_compute_surface_basic(self):
        """Test basic surface computation."""
        span = 2 * np.pi
        subdivisions = 50  # Small for speed

        vertices, faces = compute_surface(span, subdivisions, gyroid)

        assert vertices.shape[1] == 3  # 3D vertices
        assert faces.shape[1] == 3  # Triangular faces
        assert len(vertices) > 0
        assert len(faces) > 0

    def test_compute_surface_parameters(self):
        """Test surface computation with different parameters."""
        test_cases = [
            (np.pi, 25, gyroid),
            (2 * np.pi, 50, schwarz_p),
            (4 * np.pi, 30, gyroid),
        ]

        for span, subdivisions, formula in test_cases:
            vertices, faces = compute_surface(span, subdivisions, formula)
            assert len(vertices) > 0
            assert len(faces) > 0

    def test_compute_surface_edge_cases(self):
        """Test edge cases for surface computation."""
        # Very small subdivisions
        vertices, faces = compute_surface(np.pi, 10, gyroid)
        assert len(vertices) > 0

        # Very small span
        vertices, faces = compute_surface(0.1, 20, gyroid)
        assert len(vertices) > 0


class TestPlotParams:
    """Test PlotParams configuration."""

    def test_plot_params_creation(self):
        """Test PlotParams creation and usage."""
        params = PlotParams(
            name="test_surface",
            subdivisions=100,
            span=2 * np.pi,
            formula=gyroid,
            size=50.0,
            thickness=0.5,
            granularity=0.2,
        )

        assert params.name == "test_surface"
        assert params.subdivisions == 100
        assert params.span == 2 * np.pi
        assert params.formula == gyroid
        assert params.size == 50.0
        assert params.thickness == 0.5
        assert params.granularity == 0.2

    def test_plot_params_defaults(self):
        """Test PlotParams with default values."""
        params = PlotParams(
            name="test",
            subdivisions=150,
            span=np.pi,
            formula=schwarz_p,
        )

        # Check defaults are applied
        assert params.size == 40.0
        assert params.thickness == 0.3
        assert params.granularity == 0.1


if __name__ == '__main__':
    # Simple test runner
    print("Running surface formula tests...")
    test_class = TestSurfaceFormulas()
    test_class.test_gyroid_basic()
    test_class.test_schwarz_p_basic()
    print("✓ Surface formula tests passed")

    print("Running surface generation tests...")
    test_class = TestSurfaceGeneration()
    test_class.test_compute_surface_basic()
    test_class.test_compute_surface_parameters()
    test_class.test_compute_surface_edge_cases()
    print("✓ Surface generation tests passed")

    print("Running PlotParams tests...")
    test_class = TestPlotParams()
    test_class.test_plot_params_creation()
    test_class.test_plot_params_defaults()
    print("✓ PlotParams tests passed")

    print("All tests passed!")
