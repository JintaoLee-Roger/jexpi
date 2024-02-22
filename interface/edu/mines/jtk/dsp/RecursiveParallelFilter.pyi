from typing import overload, List
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import Cdouble


class RecursiveParallelFilter:
    """
    A recursive parallel filter is implemented as a sum of 2nd-order filters.
    In other words, the output of a recursive parallel filter is the sum of
    the outputs of 2nd-order recursive filters applied to the same input.
    
    An advantage of recursive parallel filters is that they can be applied
    in both forward and reverse directions to obtain symmetric zero-phase
    filters, without end effects. The 2nd-order filters applied in this
    two-way forward-and-reverse application are not the same as those
    applied in one-way forward or reverse applications.
    
    A disadvantage of recursive parallel filters is that they cannot be
    applied in-place; input and output arrays must be distinct arrays.
    Also, in the current implementation, the number of non-zero zeros
    cannot exceed the number of non-zero poles, and all poles must be
    unique.
    """

    @overload
    def __init__(self, poles: List[Cdouble], zeros: List[Cdouble],
                 gain: double) -> None:
        """
        Constructs a recursive filter with specified poles, zeros, and gain.
        Any poles or zeros at zero (the origin of the complex z-plane) are
        ignored. The number of non-zero zeros cannot exceed the number of
        non-zero poles, and all poles must be unique.
        
        Parameters
        -----------
        poles : List[Cdouble]
            array of complex poles.
        zeros : List[Cdouble]
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
        Input and output arrays must be distinct arrays.
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
        Input and output arrays must be distinct arrays.
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
        Note that this method does not simply call the methods
        {@link #applyForward(float[],float[])} and
        {@link #applyReverse(float[],float[])} in sequence.
        Input and output arrays must be distinct arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
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
        Input and output arrays must be distinct regular arrays.
        Lengths of the input and output arrays must be equal.
        
        Parameters
        -----------
        x : Float3D
            the input array.
        y : Float3D
            the output array.
        """

    def applyFrf(self, x: Float1D, y: Float1D) -> None:
        """
        For experimental use only.
        
        Parameters
        -----------
        x : Float1D
            array of x-coordinates.
        y : Float1D
            array of y-coordinates.
        """

    def applyFrr(self, x: Float1D, y: Float1D) -> None:
        """
        For experimental use only.
        
        Parameters
        -----------
        x : Float1D
            array of x-coordinates.
        y : Float1D
            array of y-coordinates.
        """
