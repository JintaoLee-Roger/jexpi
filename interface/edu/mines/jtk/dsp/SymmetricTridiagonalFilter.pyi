from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class SymmetricTridiagonalFilter:
    """
    A symmetric filter with three constant (shift-invariant) coefficients.
    Application of this filter is equivalent to multiplication by a tridiagonal
    matrix. Application of the inverse of this filter (if the inverse exists)
    is equivalent to solving a tridiagonal system of equations.
    
    When applied to an input array x of length n, the filter computes elements
    of an output y as follows:
    <pre><code>
    y[i] =            afx[i] + bx[i+1] ; for i = 0
    y[i] = bx[i-1] + aix[i] + bx[i+1] ; for i = 1, 2, ..., n-2
    y[i] = bx[i-1] + alx[i]            ; for i = n-1
    </code></pre>
    To facilitate different assumptions about values off the ends of arrays
    (boundary conditions), the coefficients <code>af</code> and <code>al</code>
    for the first and last equations may differ from the coefficient
    <code>ai</code> used in the interior equations. In a tridiagonal matrix
    representation of this filter, the coefficient <code>af</code> is in the
    upper left corner, and the coefficient <code>al</code> is in the lower
    right corner.
    
    For example, the choice <code>af = al = ai</code> is equivalent to assuming
    zero values off the ends of input arrays. Likewise, the choice <code>af =
    al = ai+b</code> is equivalent to assuming zero-slope.
    
    This filter and its inverse (if that exists) may be applied in place. For
    all methods, the input array <code>x</code> and output array <code>y</code>
    can be the same array.
    
    When applying an inverse filter, only a few simple checks are performed to
    ensure that the inverse exists, that the tridiagonal matrix is not
    singular. For example <code>|a|&ge;2|b|</code> is required, so that the
    matrix is diagonally dominant.
    
    This software is an adaptation of Algorithm 4.1 in Boisvert, R.F., 1991,
    Algorithms for special tridiagonal systems: SIAM J. Sci. Stat. Comput., v.
    12, no. 2, pp. 423-442.
    """

    def __init__(self, af: double, ai: double, al: double, b: double) -> None:
        """
        Constructs a symmetric tridiagonal filter.
        
        Parameters
        -----------
        af : double
            the diagonal coefficient a for the first sample.
        ai : double
            the diagonal coefficient a for interior samples.
        al : double
            the diagonal coefficient a for the last sample.
        b : double
            the off-diagonal coefficient b.
        """

    def apply(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter.
        
        Parameters
        -----------
        x : Float1D
            input array x; may be the same as the output array y.
        y : Float1D
            output array y; may be the same as the input array x.
        """

    @overload
    def apply1(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter along the 1st dimension of a 2D array.
        
        Parameters
        -----------
        x : Float2D
            input array x; may be the same as the output array y.
        y : Float2D
            output array y; may be the same as the input array x.
        """

    @overload
    def apply2(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter along the 2nd dimension of a 2D array.
        
        Parameters
        -----------
        x : Float2D
            input array x; may be the same as the output array y.
        y : Float2D
            output array y; may be the same as the input array x.
        """

    @overload
    def apply1(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 1st dimension of a 3D array.
        
        Parameters
        -----------
        x : Float3D
            input array x; may be the same as the output array y.
        y : Float3D
            output array y; may be the same as the input array x.
        """

    @overload
    def apply2(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 2nd dimension of a 3D array.
        
        Parameters
        -----------
        x : Float3D
            input array x; may be the same as the output array y.
        y : Float3D
            output array y; may be the same as the input array x.
        """

    def apply3(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter along the 3rd dimension of a 3D array.
        
        Parameters
        -----------
        x : Float3D
            input array x; may be the same as the output array y.
        y : Float3D
            output array y; may be the same as the input array x.
        """

    def applyInverse(self, x: Float1D, y: Float1D) -> None:
        """
        Applies the inverse of this filter.
        
        Parameters
        -----------
        x : Float1D
            input array x; may be the same as the output array y.
        y : Float1D
            output array y; may be the same as the input array x.
        """

    @overload
    def applyInverse1(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the inverse of this filter along the 1st dimension of a 2D array.
        
        Parameters
        -----------
        x : Float2D
            input array x; may be the same as the output array y.
        y : Float2D
            output array y; may be the same as the input array x.
        """

    @overload
    def applyInverse2(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the inverse of this filter along the 2nd dimension of a 2D array.
        
        Parameters
        -----------
        x : Float2D
            input array x; may be the same as the output array y.
        y : Float2D
            output array y; may be the same as the input array x.
        """

    @overload
    def applyInverse1(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the inverse of this filter along the 1st dimension of a 3D array.
        
        Parameters
        -----------
        x : Float3D
            input array x; may be the same as the output array y.
        y : Float3D
            output array y; may be the same as the input array x.
        """

    @overload
    def applyInverse2(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the inverse of this filter along the 2nd dimension of a 3D array.
        
        Parameters
        -----------
        x : Float3D
            input array x; may be the same as the output array y.
        y : Float3D
            output array y; may be the same as the input array x.
        """

    def applyInverse3(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the inverse of this filter along the 3rd dimension of a 3D array.
        
        Parameters
        -----------
        x : Float3D
            input array x; may be the same as the output array y.
        y : Float3D
            output array y; may be the same as the input array x.
        """

    @staticmethod
    def test1Simple(self) -> None:
        """
    
        """

    @staticmethod
    def test2Simple(self) -> None:
        """
    
        """

    @staticmethod
    def test3Simple(self) -> None:
        """
    
        """

    @staticmethod
    def test1Random(self) -> None:
        """
    
        """

    @staticmethod
    def test2Random(self) -> None:
        """
    
        """

    @staticmethod
    def test3Random(self) -> None:
        """
    
        """

    @staticmethod
    def main(self, args: String1D) -> None:
        """
    
        """
