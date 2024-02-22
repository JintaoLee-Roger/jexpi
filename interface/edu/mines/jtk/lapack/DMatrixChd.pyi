from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.lapack import *


class DMatrixChd:
    """
    Cholesky decomposition of a symmetric positive-definite matrix A.
    For a symmetric positive-definite matrix a, the Cholesky decomposition
    is A = LL', where L is a lower triangular matrix.
    """

    def __init__(self, a: DMatrix) -> None:
        """
        Constructs a Cholesky decomposition of the specified matrix A.
        The matrix A must be symmetric. For efficiency, this condition
        is assumed and not checked. That is, only the lower triangular
        part of A is used to perform the decomposition.
        
        Parameters
        -----------
        a : DMatrix
            the matrix.
        """

    def isPositiveDefinite(self) -> bool:
        """
        Determines whether the matrix A is positive definite. (The matrix
        A was assumed to be symmetric when this decomposition was constructed.)
        If not symmetric and positive-definite, then this decomposition cannot
        be used to solve systems of linear equations.
        Returns
        --------
        output : bool
            true, if positive-definite; false, otherwise.
        """

    def getL(self) -> DMatrix:
        """
        Gets the lower triangular factor L.
        Returns
        --------
        output : DMatrix
            the factor L.
        """

    def det(self) -> double:
        """
        Returns the determinant of the matrix A.
        Returns
        --------
        output : double
            the determinant.
        """

    def solve(self, b: DMatrix) -> DMatrix:
        """
        Returns the solution X of the linear system AX = B.
        The matrix A must be symmetric and positive-definite.
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
