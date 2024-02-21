from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class RecursiveExponentialFilter:
    """
    Recursive symmetric exponential smoothing filter. Except perhaps near
    the edges of input and output arrays, the impulse response of this
    two-sided filter is symmetric and decays exponentially from its peak
    value at zero lag. Specifically, the impulse response has the form
    h[n] = a^abs(n)(1-a)/(1+a), where a is a parameter in the range
    [0:1) derived from a specified half-width sigma.
    
    Like the Gaussian filter, the impulse response of the exponential
    filter is nowhere zero. The half-width sigma for the exponential
    filter is here defined so that, for low frequencies, the frequency
    response of the exponential filter approximates that for a Gaussian
    filter with the same specified half-width sigma. Specifically, the
    value, slope and curvature of the frequency responses will be the
    same for exponential and Gaussian filters if the same half-widths
    are specified.
    
    This smoothing filter is faster than a recursive Gaussian filter.
    This filter also provides a variety of boundary conditions that
    can be used to control the filtering of samples near the edges
    of arrays. For most (but not all) of these boundary conditions,
    this filter is symmetric and positive-definite (SPD). This means,
    for example, that it can be used as a preconditioner in
    conjugate-gradient solutions of SPD systems of equations.
    
    Multidimensional filters are applied as a cascade of one-dimensional
    filters applied for each dimension of multidimensional arrays. In
    contrast to the Gaussian filter, this cascade for the exponential
    filter does not have isotropic impulse or frequency responses.
    
    All smoothing can be performed in place, so that input and output
    arrays can be the same array.
    """

    @overload
    def __init__(self, sigma: double) -> None:
        """
        Constructs a filter with specified half-width.
        The same half-width is used when applying the filter for all
        dimensions of multidimensional arrays.
        
        Parameters
        -----------
        sigma : double
            filter half-width.
        """

    @overload
    def __init__(self, sigma1: double, sigma23: double) -> None:
        """
        Constructs a filter with specified half-widths.
        
        Parameters
        -----------
        sigma1 : double
            filter half-width for the 1st dimension.
        sigma23 : double
            filter half-width for 2nd and 3rd dimensions.
        """

    @overload
    def __init__(self, sigma1: double, sigma2: double, sigma3: double) -> None:
        """
        Constructs a filter with specified half-widths.
        
        Parameters
        -----------
        sigma1 : double
            filter half-width for the 1st dimension.
        sigma2 : double
            filter half-width for the 2nd dimension.
        sigma3 : double
            filter half-width for the 3rd dimension.
        """

    def setEdges(self, edges: Edges) -> None:
        """
        Sets the boundary condition used for samples beyond edges.
        
        Parameters
        -----------
        edges : Edges
            the boundary condition.
        """

    @overload
    def apply(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter.
        
        Parameters
        -----------
        x : Float1D
            input array.
        y : Float1D
            output array.
        """

    @overload
    def apply(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter along all array dimensions.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along all array dimensions.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply1(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter along the 1st (only) array dimension.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        x : Float1D
            input array.
        y : Float1D
            output array.
        """

    @overload
    def apply1(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter along the 1st array dimension.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply2(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter along the 2nd array dimension.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply1(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 1st array dimension.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply2(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 2nd array dimension.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    def apply3(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 3rd array dimension.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """
