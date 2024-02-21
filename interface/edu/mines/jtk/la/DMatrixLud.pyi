from typing import overload
from edu.mines.jtk.mapping import *


class DMatrixLud:
    """
    LU decomposition (with pivoting) of a matrix A.
    For an m-by-n matrix A, with m&gt;=n, the LU decomposition is
    A(piv,:) = LU, where L is an m-by-n unit lower triangular matrix,
    U is an n-by-n upper-triangular matrix, and piv is a permutation
    vector of length m.
    
    The LU decomposition with pivoting always exists, even for singular
    matrices A. The primary use of LU decomposition is in the solution of
    square systems of simultaneous linear equations. These solutions will
    fila if the matrix A is singular.
    
    This class was adapted from the package Jama, which was developed by
    Joe Hicklin, Cleve Moler, and Peter Webb of The MathWorks, Inc., and by
    Ronald Boisvert, Bruce Miller, Roldan Pozo, and Karin Remington of the
    National Institue of Standards and Technology.
    """

    def __init__(self, a: DMatrix) -> None:
        """
        Constructs an LU decomposition for the specified matrix A.
        
        Parameters
        -----------
        a : DMatrix
            the matrix A.
        """

    def isNonSingular(self) -> bool:
        """
        Determines whether the matrix A is non-singular.
        Returns
        --------
        output : bool
            true, if non-singular; false, otherwise.
        """

    def isSingular(self) -> bool:
        """
        Determines whether the matrix A is singular.
        Returns
        --------
        output : bool
            true, if singular; false, otherwise.
        """

    def getL(self) -> DMatrix:
        """
        Gets the m-by-n unit lower triangular matrix factor L.
        Returns
        --------
        output : DMatrix
            the m-by-n factor L.
        """

    def getU(self) -> DMatrix:
        """
        Gets the n-by-n upper triangular matrix factor U.
        Returns
        --------
        output : DMatrix
            the n-by-n matrix factor U.
        """

    def getPivot(self) -> Int1D:
        """
        Gets the pivot vector, an array of length m.
        Returns
        --------
        output : Int1D
            the pivot vector.
        """

    def solve(self, b: DMatrix) -> DMatrix:
        """
        Returns the solution X of the system AX = B.
        This solution exists only if the matrix A is non-singular.
        have the same number (m) of rows as the matrix A, but may have
        any number of columns.
        
        Parameters
        -----------
        b : DMatrix
            a matrix of right-hand-side vectors. This matrix must
        
        Returns
        --------
        output : DMatrix
            the matrix solution X.
        """

    def det(self) -> double:
        """
        Returns the determinant of the  matrix A.
        Returns
        --------
        output : double
            the the determinant.
        """
