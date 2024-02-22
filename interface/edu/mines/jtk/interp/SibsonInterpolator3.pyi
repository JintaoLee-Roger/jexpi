from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import *


class SibsonInterpolator3:
    """
    Sibson interpolation of scattered samples of 3D functions f(x1,x2,x3).
    Sibson's (1981) interpolant at any point (x1,x2,x3) is a weighted sum of
    values for a nearby subset of samples, the so-called natural neighbors
    of that point. Sibson interpolation is often called "natural neighbor
    interpolation."
    
    The interpolation weights, also called "Sibson coordinates", are volumes
    of overlapping Voronoi polyhedra, normalized so that they sum to one for
    any interpolation point (x1,x2,x3). Various implementations of Sibson
    interpolation differ primarily in how those volumes are computed.
    
    The basic Sibson interpolant is C1 (that is, it's gradient is continuous)
    at all points (x1,x2,x3) except at the sample points, where it is C0.
    Sibson (1981) also described an extension of his interpolant that is
    everywhere C1 and therefore smoother. This smoother interpolant requires
    gradients at the sample points, and those gradients can be estimated or
    specified explicitly.
    
    The use of gradients is controlled by a gradient power. If this power
    is zero (the default), then gradients are not used. Sibson's (1981)
    smoother C1 interpolant corresponds to a power of 1.0. Larger powers
    cause the interpolant to more rapidly approach the linear functions
    defined by the values and gradients at the sample points.
    
    Sibson's interpolant is undefined at points on or outside the convex
    hull of sample points. In this sense, Sibson interpolation does not
    extrapolate; the interpolant is implicitly bounded by the convex hull,
    and null values are returned when attempting to interpolate outside
    those bounds.
    
    To extend the interpolant outside the convex hull, this class enables
    bounds to be set explicitly. When bounds are set, extra ghost samples
    are added outside the convex hull. These ghost samples have no values,
    but they create a larger convex hull so that Sibson coordinates can be
    computed anywhere within the specified bounds. While often useful, this
    extrapolation feature should be used with care, because the added ghost
    samples may alter the Sibson interpolant at points inside but near the
    original convex hull.
    
    References:
    <ul><li>
    Braun, J. and M. Sambridge, 1995, A numerical method for solving partial
    differential equations on highly irregular evolving grids: Nature, 376,
    655--660.
    </li><li>
    Lasserre J.B., 1983, An analytical expression and an algorithm for the
    volume of a convex polyhedron in R^n: Journal of Optimization Theory
    and Applications, 39, 363--377.
    </li><li>
    Sambridge, M., J. Braun, and H. McQueen, 1995, Geophysical
    parameterization and interpolation of irregular data using
    natural neighbors.
    </li><li>
    Sibson, R., 1981, A brief description of natural neighbor interpolation,
    in V. Barnett, ed., Interpreting Multivariate Data, John Wiley and Sons,
    21--36.
    </li><li>
    Watson, D.F., 1992, Contouring: a guide to the analysis and display
    of spatial data: Pergamon, Oxford.
    </li></ul>
    """

    @overload
    def __init__(self, x1: Float1D, x2: Float1D, x3: Float1D) -> None:
        """
        Constructs an interpolator with specified sample coordinates.
        Function values f(x1,x2,x3) are not set and are assumed to be zero.
        Uses the most accurate and efficient implementation.
        
        Parameters
        -----------
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        x3 : Float1D
            array of sample x3 coordinates.
        """

    @overload
    def __init__(self, f: Float1D, x1: Float1D, x2: Float1D,
                 x3: Float1D) -> None:
        """
        Constructs an interpolator with specified samples.
        Uses the most accurate and efficient implementation.
        
        Parameters
        -----------
        f : Float1D
            array of sample values f(x1,x2,x3).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        x3 : Float1D
            array of sample x3 coordinates.
        """

    @overload
    def __init__(self, method: Method, x1: Float1D, x2: Float1D,
                 x3: Float1D) -> None:
        """
        Constructs an interpolator with specified method and sample coordinates.
        Function values f(x1,x2,x3) are not set and are assumed to be zero.
        This constructor is provided primarily for testing.
        The default Hale-Liang method is accurate and fast.
        
        Parameters
        -----------
        method : Method
            the implementation method.
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        x3 : Float1D
            array of sample x3 coordinates.
        """

    @overload
    def __init__(self, method: Method, f: Float1D, x1: Float1D, x2: Float1D,
                 x3: Float1D) -> None:
        """
        Constructs an interpolator with specified method and samples.
        This constructor is provided primarily for testing.
        The default Hale-Liang method is accurate and fast.
        
        Parameters
        -----------
        method : Method
            the implementation method.
        f : Float1D
            array of sample values f(x1,x2,x3).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        x3 : Float1D
            array of sample x3 coordinates.
        """

    def setSamples(self, f: Float1D, x1: Float1D, x2: Float1D,
                   x3: Float1D) -> None:
        """
        Sets the samples to be interpolated.
        Any sample coordinates, values or gradients set previously are forgotten.
        
        Parameters
        -----------
        f : Float1D
            array of sample values f(x1,x2,x3).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        x3 : Float1D
            array of sample x3 coordinates.
        """

    def setGradients(self, g1: Float1D, g2: Float1D, g3: Float1D) -> None:
        """
        Sets gradients for all samples. If the gradient power is currently
        zero, then this method also sets the gradient power to one. To later
        ignore gradients that have been set, the gradient power can be reset
        to zero.
        
        Parameters
        -----------
        g1 : Float1D
            array of 1st components of gradients.
        g2 : Float1D
            array of 2nd components of gradients.
        g3 : Float1D
            array of 3rd components of gradients.
        """

    def setGradientPower(self, gradientPower: double) -> None:
        """
        Sets the power of gradients for this interpolator. The default
        gradient power is zero, which implies no use of gradients and
        a basic Sibson interpolant that is smooth (C1) everywhere except
        at the specified sample points (where it is C0).
        
        If the gradient power is set to a non-zero value, and if gradients
        have not been set explicitly, then this method will also estimate
        gradients for all samples, as described by Sibson (1981).
        
        If bounds are set explicitly, gradient estimates can be improved
        by setting the bounds before calling this method.
        
        Parameters
        -----------
        gradientPower : double
            the gradient power.
        """

    def setNullValue(self, fnull: float) -> None:
        """
        Sets the null value for this interpolator.
        This null value is returned when interpolation is attempted at a
        point that lies outside the bounds of this interpolator. Those
        bounds are by default the convex hull of the sample points, but
        may also be set explicitly. The default null value is zero.
        
        Parameters
        -----------
        fnull : float
            the null value.
        """

    @overload
    def setBounds(self, x1min: float, x1max: float, x2min: float, x2max: float,
                  x3min: float, x3max: float) -> None:
        """
        Sets a bounding box for this interpolator.
        Sibson interpolation is undefined for points (x1,x2,x3) outside the
        convex hull of sample points, so the default bounds are that convex
        hull. This method enables extrapolation for points outside the convex
        hull, while restricting interpolation to points inside the box.
        
        If gradients are to be computed (not specified explicitly), it is best
        to set bounds by calling this method before computing gradients.
        
        Parameters
        -----------
        x1min : float
            lower bound on x1.
        x1max : float
            upper bound on x1.
        x2min : float
            lower bound on x2.
        x2max : float
            upper bound on x2.
        x3min : float
            lower bound on x3.
        x3max : float
            upper bound on x3.
        """

    @overload
    def setBounds(self, s1: Sampling, s2: Sampling, s3: Sampling) -> None:
        """
        Sets bounds for this interpolator using specified samplings.
        Values interpolated within the bounding box of these samplings
        are never null, even when the interpolation point (x1,x2,x3)
        lies outside that box.
        
        If gradients are to be computed (not specified explicitly), it is best
        to set bounds by calling this method before computing gradients.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of x1.
        s2 : Sampling
            sampling of x2.
        s3 : Sampling
            sampling of x3.
        """

    def useConvexHullBounds(self) -> None:
        """
        If bounds have been set explicitly, this method unsets them,
        so that the convex hull of sample points will be used instead.
        """

    @overload
    def interpolate(self, x1: float, x2: float, x3: float) -> float:
        """
        Returns a value interpolated at the specified point.
        
        Parameters
        -----------
        x1 : float
            the x1 coordinate of the point.
        x2 : float
            the x2 coordinate of the point.
        x3 : float
            the x3 coordinate of the point.
        
        Returns
        --------
        output : float
            the interpolated value.
        """

    @overload
    def interpolate(self, s1: Sampling, s2: Sampling, s3: Sampling) -> Float3D:
        """
        Returns an array of interpolated values sampled on a grid.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of n1 x1 coordinates.
        s2 : Sampling
            the sampling of n2 x2 coordinates.
        s3 : Sampling
            the sampling of n3 x3 coordinates.
        
        Returns
        --------
        output : Float3D
            array[n3][n2][n1] of interpolated values.
        """

    def getIndexWeights(self, x1: float, x2: float,
                        x3: float) -> IndexWeight1D:
        """
        Gets sample indices and interpolation weights for the specified point.
        Given a point (x1,x2,x3), the sample indices represent the natural
        neighbors of that point, and the interpolation weights are its Sibson
        coordinates. Indices correspond to the arrays that are specified when
        constructing this interpolator.
        
        Indices and weights are especially useful in applications where they
        can be reused, say, to interpolate multiple function values at a
        single point.
        
        Parameters
        -----------
        x1 : float
            the x1 coordinate of the point.
        x2 : float
            the x2 coordinate of the point.
        x3 : float
            the x3 coordinate of the point.
        
        Returns
        --------
        output : IndexWeight[]
            array of sample indices and weights; null if none.
        """

    @overload
    def validate(self, i: int) -> float:
        """
        Interpolates at the i'th sample point without using the i'th sample.
        This method implements leave-one-out cross-validation. The difference
        between the i'th sample value and the returned interpolated value is
        a measure of error at the i'th sample.
        
        If bounds have not been set explicitly, then this method will return
        a null value if the validated sample is on the convex hull of samples.
        
        This method does not recompute gradients that may have been estimated
        using the sample to be validated. Therefore, validation should be
        performed without using gradients.
        
        Parameters
        -----------
        i : int
            the index of the sample to validate.
        
        Returns
        --------
        output : float
            the value interpolated at the validated sample point.
        """

    @overload
    def validate(self, i: Int1D) -> Float1D:
        """
        Interpolates at specified sample points without using those samples.
        This method implements a form of cross-validation. Differences
        between the values of the specified samples and the returned
        interpolated values are measures of errors for those samples.
        
        If bounds have not been set explicitly, then this method will return
        null values if the validated sample is on the convex hull of samples.
        
        This method does not recompute gradients that may have been estimated
        using the samples to be validated. Therefore, validation should be
        performed without using gradients.
        
        Parameters
        -----------
        i : Int1D
            array of indices of samples to validate.
        
        Returns
        --------
        output : Float1D
            array of values interpolated at validated sample points.
        """
