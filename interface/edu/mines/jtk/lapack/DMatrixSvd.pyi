from typing import overload
from edu.mines.jtk.mapping import *


class DMatrixSvd:
    """
    Singular value decomposition of a matrix A.
    For an m-by-n matrix A, let mn = min(m,n). Then the singular value
    decomposition is A = USV', where U is an m-by-mn orthogonal matrix,
    S is an mn-by-mn diagonal matrix of singular values, and V' is an
    mn-by-n orthogonal matrix. The columns of U are the left singular
    vectors and the rows of V' (V transpose) are the right singular
    vectors.
    
    The singular values s[k] = S(k,k) are in decreasing order, such
    that s[0] &gt;= s[1] &gt;= ... &gt;= s[mn-1].
    """

    def __init__(self, a: DMatrix) -> None:
        """
        Constructs a singular value decomposition for the specified matrix A.
        
        Parameters
        -----------
        a : DMatrix
            the matrix A.
        """

    def getU(self) -> DMatrix:
        """
        Gets the matrix U of left singular vectors.
        Returns
        --------
        output : DMatrix
            the matrix U.
        """

    def getS(self) -> DMatrix:
        """
        Gets the diagonal matrix S of singular values.
        Returns
        --------
        output : DMatrix
            the matrix S.
        """

    def getSingularValues(self) -> Double1D:
        """
        Gets the array s of singular values.
        Returns
        --------
        output : Double1D
            the array s.
        """

    def getV(self) -> DMatrix:
        """
        Gets the matrix V of right singular vectors.
        The right singular vectors are in the columns of V.
        Returns
        --------
        output : DMatrix
            the matrix V.
        """

    def getVTranspose(self) -> DMatrix:
        """
        Gets the matrix V' (V transposed) of right singular vectors.
        The right singular vectors are in the rows of V'.
        Returns
        --------
        output : DMatrix
            the matrix V'.
        """

    def norm2(self) -> double:
        """
        Returns the two-norm of the matrix A.
        Returns
        --------
        output : double
            the two-norm.
        """

    def cond(self) -> double:
        """
        Returns the condition number of the matrix A.
        Returns
        --------
        output : double
            the condition number.
        """

    def rank(self) -> int:
        """
        Returns the effective numerical rank of the matrix A.
        The effective numerical rank is the number of significant
        singular values.
        Returns
        --------
        output : int
            the rank.
        """
