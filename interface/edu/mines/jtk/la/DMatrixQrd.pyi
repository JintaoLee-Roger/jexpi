from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.la import *


class DMatrixQrd:
    """
    QR decomposition of a matrix A.
    For an m-by-n matrix A, with m&gt;=n, the QR decomposition is A = QR,
    where Q is an m-by-n orthogonal matrix, and R is an n-by-n upper-triangular
    matrix.
    
    The QR decomposition is constructed even if the matrix A is rank
    deficient. However, the primary use of the QR decomposition is for
    least-squares solutions of non-square systems of linear equations,
    and such solutions are feasible only if the matrix A is of full rank.
    
    This class was adapted from the package Jama, which was developed by
    Joe Hicklin, Cleve Moler, and Peter Webb of The MathWorks, Inc., and by
    Ronald Boisvert, Bruce Miller, Roldan Pozo, and Karin Remington of the
    National Institue of Standards and Technology.
    """

    def __init__(self, a: DMatrix) -> None:
        """
        Constructs an QR decomposition for the specified matrix A.
        The matrix A must not have more columns than rows.
        If A is m-by-n, then, m&gt;=n is required.
        
        Parameters
        -----------
        a : DMatrix
            the matrix A.
        """

    def isFullRank(self) -> bool:
        """
        Determines whether the matrix A = QR is of full rank.
        Returns
        --------
        output : bool
            true, if full rank; false, otherwise.
        """

    def getQ(self) -> DMatrix:
        """
        Gets the m-by-n matrix factor Q.
        Returns
        --------
        output : DMatrix
            the m-by-n matrix factor Q.
        """

    def getR(self) -> DMatrix:
        """
        Gets the n-by-n upper triangular matrix factor R.
        Returns
        --------
        output : DMatrix
            the n-by-n matrix factor R.
        """

    def solve(self, b: DMatrix) -> DMatrix:
        """
        Returns the least-squares solution X of the system AX = B.
        This solution exists only if the matrix A is of full rank.
        have the same number (m) of rows as the matrix A, but may have
        any number of columns.
        
        Parameters
        -----------
        b : DMatrix
            a matrix of right-hand-side vectors. This matrix must
        
        Returns
        --------
        output : DMatrix
            the matrix X that minimizes the two-norm of AX-B.
        """
