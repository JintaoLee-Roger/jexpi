from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import Cdouble


class Recursive2ndOrderFilter:
    """
    Recursive 2nd-order filter. This filter solves a linear, 2nd-order,
    constant-coefficient difference equation in either forward or reverse
    directions along any dimension of a 1-D, 2-D, or 3-D array.
    
    Application of the filter in the forward direction computes
    <pre>
    y[i] = b0x[i]+b1x[i-1]+b2x[i-2]-a1y[i-1]-a2y[i-2],
    </pre>
    for i = 0, 1, 2, ..., n-1, where x[i] = y[i] = 0 for i&lt;0.
    Application of the filter in the reverse direction computes
    <pre>
    y[i] = b0x[i]+b1x[i+1]+b2x[i+2]-a1y[i+1]-a2y[i+2],
    </pre>
    for i = n-1, n-2, ..., 0, where x[i] = y[i] = 0 for i&gt;=n.
    """

    @overload
    def __init__(self, b0: float, b1: float, b2: float, a1: float,
                 a2: float) -> None:
        """
        Constructs a recursive 2nd-order filter with specified coefficients.
        If some of the coefficients are zero, the filter may be of only 1st
        or even 0th order.
        
        Parameters
        -----------
        b0 : float
            a filter coefficient.
        b1 : float
            a filter coefficient.
        b2 : float
            a filter coefficient.
        a1 : float
            a filter coefficient.
        a2 : float
            a filter coefficient.
        """

    @overload
    def __init__(self, pole: double, zero: double, gain: double) -> None:
        """
        Constructs a recursive 2nd-order filter from pole, zero, and gain.
        This filter is actually a 1st-order filter, because it has only
        one (real) pole and zero.
        
        Parameters
        -----------
        pole : double
            the pole.
        zero : double
            the zero.
        gain : double
            the filter gain.
        """

    @overload
    def __init__(self, pole1: Cdouble, pole2: Cdouble, zero1: Cdouble,
                 zero2: Cdouble, gain: double) -> None:
        """
        Constructs a recursive 2nd-order filter from poles, zeros, and gain.
        The poles must be real or conjugate pairs; likewise for the zeros.
        
        Parameters
        -----------
        pole1 : Cdouble
            the 1st pole.
        pole2 : Cdouble
            the 2nd pole.
        zero1 : Cdouble
            the 1st zero.
        zero2 : Cdouble
            the 2nd zero.
        gain : double
            the filter gain.
        """

    def applyForward(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter in the forward direction.
        
        Input and output arrays may be the same array, but must have equal
        lengths.
        
        Parameters
        -----------
        x : Float1D
            the input array.
        y : Float1D
            the output array.
        """

    def applyReverse(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter in the reverse direction.
        
        Input and output arrays may be the same array, but must have equal
        lengths.
        
        Parameters
        -----------
        x : Float1D
            the input array.
        y : Float1D
            the output array.
        """

    def accumulateForward(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter in the forward direction, accumulating the output.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must have equal
        lengths.
        
        Parameters
        -----------
        x : Float1D
            the input array.
        y : Float1D
            the output array.
        """

    def accumulateReverse(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter in the reverse direction, accumulating the output.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must have equal
        lengths.
        
        Parameters
        -----------
        x : Float1D
            the input array.
        y : Float1D
            the output array.
        """

    @overload
    def apply1Forward(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter in 1st dimension in the forward direction.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float2D
            the input array.
        y : Float2D
            the output array.
        """

    @overload
    def apply1Reverse(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter in 1st dimension in the reverse direction.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float2D
            the input array.
        y : Float2D
            the output array.
        """

    @overload
    def apply2Forward(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter in 2nd dimension in the forward direction.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float2D
            the input array.
        y : Float2D
            the output array.
        """

    @overload
    def apply2Reverse(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter in 2nd dimension in the reverse direction.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float2D
            the input array.
        y : Float2D
            the output array.
        """

    @overload
    def accumulate1Forward(self, x: Float2D, y: Float2D) -> None:
        """
        Accumulates output in 1st dimension in the forward direction.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float2D
            the input array.
        y : Float2D
            the output array.
        """

    @overload
    def accumulate1Reverse(self, x: Float2D, y: Float2D) -> None:
        """
        Accumulates output in 1st dimension in the reverse direction.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float2D
            the input array.
        y : Float2D
            the output array.
        """

    @overload
    def accumulate2Forward(self, x: Float2D, y: Float2D) -> None:
        """
        Accumulates output in 2nd dimension in the forward direction.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float2D
            the input array.
        y : Float2D
            the output array.
        """

    @overload
    def accumulate2Reverse(self, x: Float2D, y: Float2D) -> None:
        """
        Accumulates output in 2nd dimension in the reverse direction.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float2D
            the input array.
        y : Float2D
            the output array.
        """

    @overload
    def apply1Forward(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter in 1st dimension in the forward direction.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    @overload
    def apply1Reverse(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter in 1st dimension in the reverse direction.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    @overload
    def apply2Forward(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter in 2nd dimension in the forward direction.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    @overload
    def apply2Reverse(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter in 2nd dimension in the reverse direction.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    def apply3Forward(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter in 3rd dimension in the forward direction.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    def apply3Reverse(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter in 3rd dimension in the reverse direction.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    @overload
    def accumulate1Forward(self, x: Float3D, y: Float3D) -> None:
        """
        Accumulates output in 1st dimension in the forward direction.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    @overload
    def accumulate1Reverse(self, x: Float3D, y: Float3D) -> None:
        """
        Accumulates output in 1st dimension in the reverse direction.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    @overload
    def accumulate2Forward(self, x: Float3D, y: Float3D) -> None:
        """
        Accumulates output in 2nd dimension in the forward direction.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    @overload
    def accumulate2Reverse(self, x: Float3D, y: Float3D) -> None:
        """
        Accumulates output in 2nd dimension in the reverse direction.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    def accumulate3Forward(self, x: Float3D, y: Float3D) -> None:
        """
        Accumulates output in 3rd dimension in the forward direction.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    def accumulate3Reverse(self, x: Float3D, y: Float3D) -> None:
        """
        Accumulates output in 3rd dimension in the reverse direction.
        This method filters the input, and adds the result to the output; it
        is most useful when implementing parallel forms of recursive filters.
        
        Input and output arrays may be the same array, but must be
        regular and have equal lengths.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """
