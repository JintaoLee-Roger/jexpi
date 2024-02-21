from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class RecursiveCascadeFilter:
    """
    A recursive filter implemented as a cascade of 2nd-order filters.
    The output of each 2nd-order recursive filter becomes the input to
    the next 2nd-order recursive filter in the cascade.
    
    An advantage of recursive cascade filters is that they can be
    applied in-place; input and output arrays may be the same arrays.
    
    A disadvantage of recursive cascade filters is that a forward-reverse
    application yields only an approximation to a symmetric zero-phase
    impulse response. This approximation is worst at array ends where the
    output of each 2nd-order filter truncated.
    """

    @overload
    def __init__(self, poles: Cdouble1D, zeros: Cdouble1D,
                 gain: double) -> None:
        """
        Constructs a recursive filter with specified poles, zeros, and gain.
        The coefficients of this recursive filter are real. Therefore, poles
        and zeros with non-zero imaginary parts must have conjugate mates.
        
        Parameters
        -----------
        poles : Cdouble1D
            array of complex poles.
        zeros : Cdouble1D
            array of complex poles.
        gain : double
            the filter gain.
        """

    @overload
    def __init__(self) -> None:
        """
    
        """

    def applyForward(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter in the forward direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
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
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
        Parameters
        -----------
        x : Float1D
            the input array.
        y : Float1D
            the output array.
        """

    def applyForwardReverse(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter in the forward and reverse directions.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
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
        Applies this filter along the 1st dimension in the forward direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
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
        Applies this filter along the 1st dimension in the reverse direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
        Parameters
        -----------
        x : Float2D
            the input array.
        y : Float2D
            the output array.
        """

    @overload
    def apply1ForwardReverse(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter along the 1st dimension in the forward and
        reverse directions.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
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
        Applies this filter along the 2nd dimension in the forward direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
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
        Applies this filter along the 2nd dimension in the reverse direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
        Parameters
        -----------
        x : Float2D
            the input array.
        y : Float2D
            the output array.
        """

    @overload
    def apply2ForwardReverse(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter along the 2nd dimension in the forward and
        reverse directions.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
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
        Applies this filter along the 1st dimension in the forward direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
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
        Applies this filter along the 1st dimension in the reverse direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    @overload
    def apply1ForwardReverse(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 1st dimension in the forward and
        reverse directions.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
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
        Applies this filter along the 2nd dimension in the forward direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
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
        Applies this filter along the 2nd dimension in the reverse direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    @overload
    def apply2ForwardReverse(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 2nd dimension in the forward and
        reverse directions.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    def apply3Forward(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 3rd dimension in the forward direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    def apply3Reverse(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 3rd dimension in the reverse direction.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    def apply3ForwardReverse(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 3rd dimension in the forward and
        reverse directions.
        Input and output arrays may be the same array.
        Lengths of the input and output arrays must be equal.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """
