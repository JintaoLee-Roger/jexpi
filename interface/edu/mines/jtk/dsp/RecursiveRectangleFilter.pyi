from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class RecursiveRectangleFilter:
    """
    Recursive implementation of a rectangle filter.
    The rectangle filter is a moving average defined by the following sum:
    <pre><code>
    m
    y[i] = s  sum x[i+j]
    j=l
    for 0&lt;=i&lt;n, l&lt;=m, and s = 1.0/(1.0+m-l).
    </code></pre>
    This recursive implementation computes
    <pre><code>
    y[i] = y[i-1]+s(x[i+m]-x[i+l-1]),
    </code></pre>
    with care taken to initialize y[0] and handle array index bounds.
    For long filters (large 1+m-l), this recursive implementation may be
    much more efficient than the more straightforward sum for each index i.
    """

    def __init__(self, l: int, m: int) -> None:
        """
        Constructs a rectangle filter with specified index bounds.
        
        Parameters
        -----------
        l : int
            the lower index bound in the sum; must not be greater than m.
        m : int
            the upper index bound in the sum; must not be less than l.
        """

    def apply(self, x: Float1D, y: Float1D) -> None:
        """
        Applies the filter.
        
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
        Applies the filter along the 1st dimension.
        Applies no filter along the 2nd dimension.
        
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
        Applies the filter along the 2nd dimension.
        Applies no filter along the 1st dimension.
        
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
        Applies the filter along the 1st dimension.
        Applies no filter along the 2nd or 3rd dimensions.
        
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
        Applies the filter along the 2nd dimension.
        Applies no filter along the 1st or 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    def apply3(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the filter along the 3rd dimension.
        Applies no filter along the 1st or 2nd dimensions.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """
