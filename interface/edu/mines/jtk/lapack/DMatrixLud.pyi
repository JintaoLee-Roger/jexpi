from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.lapack import *


class DMatrixLud:
    """
    LU decomposition of a matrix A.
    For an m-by-n matrix A, the LU decomposition is A = PLU or A(p,:) =
    LU, where P is an m-by-m row permutation matrix, p is a corresponding
    array of m row permutation indices, L is an m-by-min(m,n) lower
    triangular or trapezoidal matrix with unit diagonal elements, and
    U is a min(m,n)-by-n upper triangular or trapezoidal matrix.
    
    The LU decomposition with pivoting never fails, even if the matrix
    A is singular. However, the primary use of LU decomposition is in the
    solution of square systems of linear equations, which will fail if A
    is singular (or not square).
    """

    def __init__(self, a: DMatrix) -> None:
        """
        Constructs an LU decomposition of the specified matrix A.
        
        Parameters
        -----------
        a : DMatrix
            the matrix.
        """

    def isSingular(self) -> bool:
        """
        Determines whether the matrix A is singular. If singular, then this
        decomposition cannot be used to solve systems of linear equations.
        Returns
        --------
        output : bool
            true, if singular; false, otherwise.
        """

    def getL(self) -> DMatrix:
        """
        Gets the lower triangular (or lower trapezoidal) factor L.
        The matrix L has dimensions m-by-min(m,n) and unit diagonal elements.
        Returns
        --------
        output : DMatrix
            the factor L.
        """

    def getU(self) -> DMatrix:
        """
        Gets the upper triangular (or upper trapezoidal) factor U.
        The matrix U has dimensions min(m,n)-by-n.
        Returns
        --------
        output : DMatrix
            the factor L.
        """

    def getP(self) -> DMatrix:
        """
        Gets the row permutation matrix P.
        The matrix P has dimensions m-by-m.
        Returns
        --------
        output : DMatrix
            the permutation matrix P.
        """

    def getPivotIndices(self) -> Int1D:
        """
        Gets the array of row permutation (pivot) indices p. In this
        decomposition of the m-by-n matrix A, row i was interchanged
        with row p[i], for i = 0, 1, 2, ..., m-1.
        Returns
        --------
        output : Int1D
            the pivot indices p.
        """

    def det(self) -> double:
        """
        Returns the determinant of the square matrix A.
        The determinant exists only for square matrices A.
        Returns
        --------
        output : double
            the determinant.
        """

    def solve(self, b: DMatrix) -> DMatrix:
        """
        Returns the solution X of the linear system AX = B.
        The matrix A must be square and non singular.
        Also, the matrices A and B must have the same number of rows.
        
        Parameters
        -----------
        b : DMatrix
            the right-hand-side matrix B.
        
        Returns
        --------
        output : DMatrix
            the solution matrix X.
        """
