from typing import overload
from edu.mines.jtk.mapping import *


class CausalFilter:
    """
    A multi-dimensional causal filter that is linear and shift-invariant.
    The output samples of a causal filter depend only on present and past
    input samples. In two dimensions, causal filters are also called
    non-symmetric half-plane (NSHP) filters, and this notion of causal
    can be extended to higher dimensions.
    
    A causal filter is a linear operator with a corresponding anti-causal
    transpose (adjoint) operator. A causal filter may have a causal inverse,
    and its transpose may have an anti-causal inverse.
    
    A causal filter is a stable all-zero filter that may or may not
    be minimum-phase; that is, it may or may not have a causal stable
    inverse. That inverse is a recursive all-pole filter, as described by
    Claerbout, J., 1998, Multidimensional recursive filters via a helix:
    Geophysics, v. 63, n. 5, p. 1532-1541.
    
    The filter and its transpose, inverse, and inverse-transpose may all
    be applied in-place; that is, the input and output arrays may be the
    same array.
    """

    @overload
    def __init__(self, lag1: Int1D) -> None:
        """
        Constructs a unit-impulse filter for specified lag1.
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
        Constructs a unit-impulse filter for specified lag1 and lag2.
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
        Constructs a unit-impulse filter for specified lag1, lag2, and lag3.
        
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

    @overload
    def __init__(self, lag1: Int1D, a: Float1D) -> None:
        """
        Constructs a causal filter for specified lag1.
        By default, all lag2 and lag3 are assumed to be zero.
        
        For j=0 only, lag1[j] is zero.
        All lag1[j] must be non-negative.
        
        Parameters
        -----------
        lag1 : Int1D
            array of lags.
        a : Float1D
            array of filter coefficients for each lag.
        """

    @overload
    def __init__(self, lag1: Int1D, lag2: Int1D, a: Float1D) -> None:
        """
        Constructs a causal filter for specified lag1 and lag2.
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
        a : Float1D
            array of filter coefficients for each lag.
        """

    @overload
    def __init__(self, lag1: Int1D, lag2: Int1D, lag3: Int1D,
                 a: Float1D) -> None:
        """
        Constructs a causal filter for specified lag1, lag2, and lag3.
        
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
        a : Float1D
            array of filter coefficients for each lag.
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

    def getA(self) -> Float1D:
        """
        Gets a copy of the filter coefficients.
        Returns
        --------
        output : Float1D
            array of filter coefficients; by copy, not by reference.
        """

    @overload
    def factorWilsonBurg(self, maxiter: int, epsilon: float,
                         r: Float1D) -> None:
        """
        Wilson-Burg factorization for the specified 1-D auto-correlation.
        Modifies this filter using the iterative Wilson-Burg algorithm. If this
        algorithm converges, the impulse response of this filter cascaded with
        its transpose approximates the specified auto-correlation.
        when the change in all filter coefficients is less than this factor
        times the square root of the zero-lag of the auto correlation.
        The middle array element is the zero-lag of the auto-correlation,
        and other elements are symmetric about the middle element.
        converge within the specified maximum number of iterations.
        
        Parameters
        -----------
        maxiter : int
            maximum number of Wilson-Burg iterations.
        epsilon : float
            tolerance for convergence. Iterations have converged
        r : Float1D
            the auto-correlation. This 1-D array must have odd length.
        """

    @overload
    def factorWilsonBurg(self, maxiter: int, epsilon: float,
                         r: Float2D) -> None:
        """
        Wilson-Burg factorization for the specified 2-D auto-correlation.
        Modifies this filter using the iterative Wilson-Burg algorithm. If this
        algorithm converges, the impulse response of this filter cascaded with
        its transpose approximates the specified auto-correlation.
        when the change in all filter coefficients is less than this factor
        times the square root of the zero-lag of the auto correlation.
        The middle array element is the zero-lag of the auto-correlation,
        and other elements are symmetric about the middle element.
        converge within the specified maximum number of iterations.
        
        Parameters
        -----------
        maxiter : int
            maximum number of Wilson-Burg iterations.
        epsilon : float
            tolerance for convergence. Iterations have converged
        r : Float2D
            the auto-correlation. This 2-D array must have odd lengths.
        """

    @overload
    def factorWilsonBurg(self, maxiter: int, epsilon: float,
                         r: Float3D) -> None:
        """
        Wilson-Burg factorization for the specified 3-D auto-correlation.
        Modifies this filter using the iterative Wilson-Burg algorithm. If this
        algorithm converges, the impulse response of this filter cascaded with
        its transpose approximates the specified auto-correlation.
        when the change in all filter coefficients is less than this factor
        times the square root of the zero-lag of the auto correlation.
        The middle array element is the zero-lag of the auto-correlation,
        and other elements are symmetric about the middle element.
        converge within the specified maximum number of iterations.
        
        Parameters
        -----------
        maxiter : int
            maximum number of Wilson-Burg iterations.
        epsilon : float
            tolerance for convergence. Iterations have converged
        r : Float3D
            the auto-correlation. This 3-D array must have odd lengths.
        """

    @overload
    def apply(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter.
        Uses lag1; ignores lag2 or lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        x : Float1D
            input array.
        y : Float1D
            output array.
        """

    @overload
    def applyTranspose(self, x: Float1D, y: Float1D) -> None:
        """
        Applies the transpose of this filter.
        Uses lag1; ignores lag2 or lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        x : Float1D
            input array.
        y : Float1D
            output array.
        """

    @overload
    def applyInverse(self, y: Float1D, x: Float1D) -> None:
        """
        Applies the inverse of this filter.
        Uses lag1; ignores lag2 or lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        y : Float1D
            input array.
        x : Float1D
            output array.
        """

    @overload
    def applyInverseTranspose(self, y: Float1D, x: Float1D) -> None:
        """
        Applies the inverse transpose of this filter.
        Uses lag1; ignores lag2 or lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        y : Float1D
            input array.
        x : Float1D
            output array.
        """

    @overload
    def apply(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter.
        Uses lag1 and lag2; ignores lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def applyTranspose(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the transpose of this filter.
        Uses lag1 and lag2; ignores lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def applyInverse(self, y: Float2D, x: Float2D) -> None:
        """
        Applies the inverse of this filter.
        Uses lag1 and lag2; ignores lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        y : Float2D
            input array.
        x : Float2D
            output array.
        """

    @overload
    def applyInverseTranspose(self, y: Float2D, x: Float2D) -> None:
        """
        Applies the inverse transpose of this filter.
        Uses lag1 and lag2; ignores lag3, if specified.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        y : Float2D
            input array.
        x : Float2D
            output array.
        """

    @overload
    def apply(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter.
        Uses lag1, lag2, and lag3.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def applyTranspose(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the transpose of this filter.
        Uses lag1, lag2, and lag3.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def applyInverse(self, y: Float3D, x: Float3D) -> None:
        """
        Applies the inverse of this filter.
        Uses lag1, lag2, and lag3.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        y : Float3D
            output array.
        x : Float3D
            input array.
        """

    @overload
    def applyInverseTranspose(self, y: Float3D, x: Float3D) -> None:
        """
        Applies the inverse transpose of this filter.
        Uses lag1, lag2, and lag3.
        
        May be applied in-place; input and output arrays may be the same.
        
        Parameters
        -----------
        y : Float3D
            output array.
        x : Float3D
            input array.
        """
