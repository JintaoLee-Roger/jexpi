from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.la import *


class TridiagonalFMatrix:
    """
    A tridiagonal matrix is a square matrix specified by three diagonals.
    All elements except for those on the diagonal, lower sub-diagonal, and
    upper super-diagonal of the matrix are equal to zero. The diagonals are
    represented by three arrays a, b, and c of matrix elements. Here is an
    example of a tridiagonal system of n = 4 equations:
    <pre><code>
    |b[0]    c[0]     0       0  | |u[0]|     |r[0]|
    |a[1]    b[1]    c[1]     0  | |u[1]|  =  |r[1]|
    | 0      a[2]    b[2]    c[2]| |u[2]|     |r[2]|
    | 0       0      a[3]    b[3]| |u[3]|     |r[3]|
    </code></pre>
    The values a[0] and c[n-1] are ignored.
    """

    @overload
    def __init__(self, n: int) -> None:
        """
        Constructs a tridiagonal matrix with the specified number of rows.
        All matrix elements are initially zero.
        
        Parameters
        -----------
        n : int
            the number of rows (and columns) in the matrix.
        """

    @overload
    def __init__(self, n: int, a: Float1D, b: Float1D, c: Float1D) -> None:
        """
        Constructs a new tridiagonal matrix with specified elements.
        The arrays a, b, and c are passed by reference, not by copy.
        
        Parameters
        -----------
        n : int
            the number of rows (and columns) in the matrix.
        a : Float1D
            array of lower sub-diagonal elements; a[0] is ignored.
        b : Float1D
            array of diagonal elements.
        c : Float1D
            array of upper super-diagonal elements; c[n-1] is ignored.
        """

    def n(self) -> int:
        """
        Returns the number of rows and columns in this matrix.
        Returns
        --------
        output : int
            the number of rows and columns.
        """

    def a(self) -> Float1D:
        """
        Returns the array a of lower sub-diagonal elements.
        Returns
        --------
        output : Float1D
            the array a; by reference, not by copy.
        """

    def b(self) -> Float1D:
        """
        Returns the array b of diagonal elements.
        Returns
        --------
        output : Float1D
            the array b; by reference, not by copy.
        """

    def c(self) -> Float1D:
        """
        Returns the array c of upper sub-diagonal elements.
        Returns
        --------
        output : Float1D
            the array c; by reference, not by copy.
        """

    def solve(self, r: Float1D, u: Float1D) -> None:
        """
        Solves this tridiagonal system for specified right-hand-side.
        Uses Gaussian elimination without pivoting, and assumes that this
        matrix is non-singular.
        
        Parameters
        -----------
        r : Float1D
            input array containing the right-hand-side column vector.
        u : Float1D
            output array containing the left-hand-side vector of unknowns.
        """

    @overload
    def times(self, x: Float1D) -> Float1D:
        """
        Multiplies this matrix by the specified column vector.
        
        Parameters
        -----------
        x : Float1D
            input array containing the column vector.
        
        Returns
        --------
        output : Float1D
            array containing the matrix-vector product.
        """

    @overload
    def times(self, x: Float1D, y: Float1D) -> None:
        """
        Multiplies this matrix by the specified column vector.
        
        Parameters
        -----------
        x : Float1D
            input array containing the column vector.
        y : Float1D
            output array containing the matrix-vector product.
        """
