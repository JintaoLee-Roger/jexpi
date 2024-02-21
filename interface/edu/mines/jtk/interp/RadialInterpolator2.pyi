from typing import overload
from edu.mines.jtk.mapping import *


class RadialInterpolator2:
    """
    Interpolation of scattered data f(x1,x2) with radial basis functions.
    """

    def __init__(self, basis: Basis, f: Float1D, x1: Float1D,
                 x2: Float1D) -> None:
        """
        Constructs a gridder with specified known (scattered) samples.
        
        Parameters
        -----------
        basis : Basis
            the radial basis function.
        f : Float1D
            array of known sample values f(x1,x2).
        x1 : Float1D
            array of known sample x1 coordinates.
        x2 : Float1D
            array of known sample x2 coordinates.
        """

    def setBasis(self, basis: Basis) -> None:
        """
        Sets the radial basis function used by this interpolator.
        
        Parameters
        -----------
        basis : Basis
            the radial basis function.
        """

    def setSamples(self, f: Float1D, x1: Float1D, x2: Float1D) -> None:
        """
        Sets the known (scattered) samples to be interpolated.
        The specified arrays are copied; not referenced.
        
        Parameters
        -----------
        f : Float1D
            array of sample values f(x1,x2).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        """

    def setMetricTensor(self, m11: double, m12: double, m22: double) -> None:
        """
        Sets the metric tensor used to compute distances.
        A metric tensor can make the radial basis function anisotropic,
        with elliptical contours of constant value. The default metric
        tensor is the identity matrix, which corresponds to an isotropic
        basis function.
        
        Distance squared from the origin to a point (x1,x2) is
        x1m11x1 + 2x1m12x2 + x2m22x2. The determinant
        m11m22-m12m12 of the metric tensor must be non-negative.
        
        Parameters
        -----------
        m11 : double
            the metric tensor element (1,1).
        m12 : double
            the metric tensor element (1,2).
        m22 : double
            the metric tensor element (2,2).
        """

    def setPolyTrend(self, order: int) -> None:
        """
        Sets the order of the polynomial trend to be fit to sample values.
        This trend is subtracted before computing weights for the radial
        basis functions, and it is restored when values are interpolated.
        The default order is -1, so that no trend is removed.
        
        Parameters
        -----------
        order : int
            the order of the polynomial fit; must be -1, 0, 1, or 2.
        """

    @overload
    def interpolate(self, x1: float, x2: float) -> float:
        """
        Returns a value interpolated at the specified point.
        
        Parameters
        -----------
        x1 : float
            the x1 coordinate of the point.
        x2 : float
            the x2 coordinate of the point.
        
        Returns
        --------
        output : float
            the interpolated value.
        """

    @overload
    def interpolate(self, s1: Sampling, s2: Sampling) -> Float2D:
        """
        Returns an array of interpolated values sampled on a grid.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of n1 x1 coordinates.
        s2 : Sampling
            the sampling of n2 x2 coordinates.
        
        Returns
        --------
        output : Float2D
            array[n2][n1] of interpolated values.
        """

    def getWeights(self) -> Float1D:
        """
        Gets the weights that scale the basis for each known sample.
        Returns
        --------
        output : Float1D
            array of weights; by copy, not by reference.
        """
