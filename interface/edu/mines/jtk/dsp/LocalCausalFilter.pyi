from typing import overload
from edu.mines.jtk.mapping import *


class LocalCausalFilter:
    """
    A multi-dimensional causal filter with locally variable coefficients.
    The output samples of a causal filter depend only on present and past
    input samples. In two dimensions, causal filters are also called
    non-symmetric half-plane (NSHP) filters, and this notion of causal
    can be extended to higher dimensions.
    
    Local causal filters have coefficients that may vary from one output
    sample to the next. Such a filter is <em>not</em> shift invariant. Its
    application is not equivalent to convolution with its impulse response.
    
    Though not shift-invariant, a local causal filter is a linear operator
    with a corresponding anti-causal transpose (adjoint) operator. A local
    causal filter may have a causal inverse, and its transpose may have an
    anti-causal inverse.
    
    A local causal filter is a stable all-zero filter that may or may not
    be minimum-phase; that is, it may or may not have a causal stable
    inverse. That inverse is a recursive all-pole filter, as described by
    Claerbout, J., 1998, Multidimensional recursive filters via a helix:
    Geophysics, v. 63, n. 5, p. 1532-1541.
    
    The filter and its transpose and inverse may all be applied in-place;
    that is, the input and output arrays may be the same array. However,
    <em>the inverse-transpose filter cannot be applied in-place.</em>
    """

    @overload
    def __init__(self, lag1: Int1D) -> None:
        """
        Constructs a local causal filter for specified lag1.
        By default, all lag2 and lag3 are assumed to be zero.
        
        For j=0 only, lag1[j] is zero.
        All lag1[j] must be non-negative.
        
        Parameters
        -----------
        lag1 : Int1D
            array of lags.
        """

    @overload
    def __init__(self, lag1: Int1D, lag2: Int1D) -> None:
        """
        Constructs a local causal filter for specified lag1 and lag2.
        By default, all lag3 are assumed to be zero.
        
        For j=0 only, lag1[j] and lag2[j] are zero.
        All lag2[j] must be non-negative.
        If lag2[j] is zero, then lag1[j] must be non-negative.
        
        Parameters
        -----------
        lag1 : Int1D
            array of lags in 1st dimension.
        lag2 : Int1D
            array of lags in 2nd dimension.
        """

    @overload
    def __init__(self, lag1: Int1D, lag2: Int1D, lag3: Int1D) -> None:
        """
        Constructs a local causal filter for specified lag1, lag2, and lag3.
        
        For j=0 only, lag1[j] and lag2[j] and lag3[j] are zero.
        All lag3[j] must be non-negative.
        If lag3[j] is zero, then lag2[j] must be non-negative.
        If lag3[j] and lag2[j] are zero, then lag1[j] must be non-negative.
        
        Parameters
        -----------
        lag1 : Int1D
            array of lags in 1st dimension.
        lag2 : Int1D
            array of lags in 2nd dimension.
        lag3 : Int1D
            array of lags in 3rd dimension.
        """

    def getLag1(self) -> Int1D:
        """
        Gets a copy of the lags in the 1st dimension.
        Returns
        --------
        output : Int1D
            array of lags; by copy, not by reference.
        """

    def getLag2(self) -> Int1D:
        """
        Gets a copy of the lags in the 2nd dimension.
        Returns
        --------
        output : Int1D
            array of lags; by copy, not by reference.
        """

    def getLag3(self) -> Int1D:
        """
        Gets a copy of the lags in the 3rd dimension.
        Returns
        --------
        output : Int1D
            array of lags; by copy, not by reference.
        """

    @overload
    def apply(self, a1: A1, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter.
        Uses lag1; ignores lag2 or lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        a1 : A1
            filter coefficients.
        x : Float1D
            input array.
        y : Float1D
            output array.
        """

    @overload
    def applyTranspose(self, a1: A1, x: Float1D, y: Float1D) -> None:
        """
        Applies the transpose of this filter.
        Uses lag1; ignores lag2 or lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        a1 : A1
            filter coefficients.
        x : Float1D
            input array.
        y : Float1D
            output array.
        """

    @overload
    def applyInverse(self, a1: A1, y: Float1D, x: Float1D) -> None:
        """
        Applies the inverse of this filter.
        Uses lag1; ignores lag2 or lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        a1 : A1
            filter coefficients.
        y : Float1D
            input array.
        x : Float1D
            output array.
        """

    @overload
    def applyInverseTranspose(self, a1: A1, y: Float1D, x: Float1D) -> None:
        """
        Applies the inverse transpose of this filter.
        Uses lag1; ignores lag2 or lag3, if specified.
        
        <em>The inverse transpose cannot be applied in-place;
        input and output arrays cannot be the same array.</em>
        
        Parameters
        -----------
        a1 : A1
            filter coefficients.
        y : Float1D
            input array.
        x : Float1D
            output array.
        """

    @overload
    def apply(self, a2: A2, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter.
        Uses lag1 and lag2; ignores lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        a2 : A2
            filter coefficients.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def applyTranspose(self, a2: A2, x: Float2D, y: Float2D) -> None:
        """
        Applies the transpose of this filter.
        Uses lag1 and lag2; ignores lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        a2 : A2
            filter coefficients.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def applyInverse(self, a2: A2, y: Float2D, x: Float2D) -> None:
        """
        Applies the inverse of this filter.
        Uses lag1 and lag2; ignores lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        a2 : A2
            filter coefficients.
        y : Float2D
            input array.
        x : Float2D
            output array.
        """

    @overload
    def applyInverseTranspose(self, a2: A2, y: Float2D, x: Float2D) -> None:
        """
        Applies the inverse transpose of this filter.
        Uses lag1 and lag2; ignores lag3, if specified.
        
        <em>The inverse transpose cannot be applied in-place;
        input and output arrays cannot be the same array.</em>
        
        Parameters
        -----------
        a2 : A2
            filter coefficients.
        y : Float2D
            input array.
        x : Float2D
            output array.
        """

    @overload
    def apply(self, a3: A3, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter.
        Uses lag1, lag2, and lag3.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        a3 : A3
            filter coefficients.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def applyTranspose(self, a3: A3, x: Float3D, y: Float3D) -> None:
        """
        Applies the transpose of this filter.
        Uses lag1, lag2, and lag3.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        a3 : A3
            filter coefficients.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def applyInverse(self, a3: A3, y: Float3D, x: Float3D) -> None:
        """
        Applies the inverse of this filter.
        Uses lag1, lag2, and lag3.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        a3 : A3
            filter coefficients.
        y : Float3D
            output array.
        x : Float3D
            input array.
        """

    @overload
    def applyInverseTranspose(self, a3: A3, y: Float3D, x: Float3D) -> None:
        """
        Applies the inverse transpose of this filter.
        Uses lag1, lag2, and lag3.
        
        <em>The inverse transpose cannot be applied in-place;
        input and output arrays cannot be the same array.</em>
        
        Parameters
        -----------
        a3 : A3
            filter coefficients.
        y : Float3D
            output array.
        x : Float3D
            input array.
        """
