from typing import overload
from edu.mines.jtk.mapping import *


class DiscreteSibsonGridder3:
    """
    A discrete approximation of Sibson's natural neighbor interpolation.
    Given a set of known samples of a function f(x1,x2,x3) for scattered
    points (x1,x2,x3), this approximation computes an interpolating
    function g(x1,x2,x3) with specified uniform samplings of x1, x2 and
    x3. The function g(x1,x2,x3) approximates the natural neighbor
    interpolant proposed by Sibson (1981).
    
    In this approximation, all scattered points (x1,x2,x3) are rounded to the
    nearest uniformly sampled points. If two or more known samples fall into
    a single uniform sample bin, their values f(x1,x2,x3) are averaged to
    obtain the value g(x1,x2,x3) for that bin. Values of g(x1,x2,x3) for all
    other bins are computed to approximate natural neighbor interpolation.
    
    The primary goal of this implementation is simplicity. Like the method
    of Park et al. (2006), it requires no Delaunay triangulation or Voronoi
    tesselation, and its cost decreases as the number of known samples
    increases. Moreover, unlike the method of Park et al., this method uses
    no auxilary data structure such as a k-D tree to find nearest known
    samples. Computational complexity of this method is within a constant
    factor of that of Park et al.
    
    Discrete implementations of Sibson's interpolation can produce artifacts
    (small axis-aligned ridges or valleys) caused by sampling circles on a
    rectangular grid. To attenuate these artifacts, this method applies some
    number of Gauss-Seidel iterations of bi-Laplacian smoothing to the
    interpolated samples, without modifying the known samples.
    <pre>
    References:
    Park, S.W., L. Linsen, O. Kreylos, J.D. Owens, B. Hamann, 2006,
    Discrete Sibson interpolation: IEEE Transactions on Visualization
    and Computer Graphics,
    v. 12, 243-253.
    Sibson, R., 1981, A brief description of natural neighbor interpolation,
    in V. Barnett, ed., Interpreting Multivariate Data: John Wiley and Sons,
    21-36.
    </pre>
    """

    def __init__(self, f: Float1D, x1: Float1D, x2: Float1D,
                 x3: Float1D) -> None:
        """
        Constructs a nearest neighbor gridder with specified known samples.
        The specified arrays are copied; not referenced.
        
        Parameters
        -----------
        f : Float1D
            array of known sample values f(x1,x2).
        x1 : Float1D
            array of known sample x1 coordinates.
        x2 : Float1D
            array of known sample x2 coordinates.
        x3 : Float1D
            array of known sample x3 coordinates.
        """

    def setScattered(self, f: Float1D, x1: Float1D, x2: Float1D,
                     x3: Float1D) -> None:
        """
    
        """

    def grid(self, s1: Sampling, s2: Sampling, s3: Sampling) -> Float3D:
        """
    
        """
