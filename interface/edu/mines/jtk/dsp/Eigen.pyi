from typing import overload
from edu.mines.jtk.mapping import *


class Eigen:
    """
    Special-purpose eigensolvers for digital signal processing.
    Methods of this class solve small eigen-problems efficiently.
    """

    @overload
    @staticmethod
    def solveSymmetric22(self, a: Float2D, v: Float2D, d: Float1D) -> None:
        """
        Computes eigenvalues and eigenvectors for a symmetric 2x2 matrix A.
        If the eigenvectors are placed in columns in a matrix V, and the
        eigenvalues are placed in corresponding columns of a diagonal
        matrix D, then AV = VD.
        
        Parameters
        -----------
        a : Float2D
            the symmetric matrix A.
        v : Float2D
            the array of eigenvectors v[0] and v[1].
        d : Float1D
            the array of eigenvalues d[0] and d[1].
        """

    @overload
    @staticmethod
    def solveSymmetric22(self, a: Double2D, v: Double2D, d: Double1D) -> None:
        """
        Computes eigenvalues and eigenvectors for a symmetric 2x2 matrix A.
        If the eigenvectors are placed in columns in a matrix V, and the
        eigenvalues are placed in corresponding columns of a diagonal
        matrix D, then AV = VD.
        
        Parameters
        -----------
        a : Double2D
            the symmetric matrix A.
        v : Double2D
            the array of eigenvectors v[0] and v[1].
        d : Double1D
            the array of eigenvalues d[0] and d[1].
        """

    @staticmethod
    def solveSymmetric33(self, a: Double2D, v: Double2D, d: Double1D) -> None:
        """
        Computes eigenvalues and eigenvectors for a symmetric 3x3 matrix A.
        If the eigenvectors are placed in columns in a matrix V, and the
        eigenvalues are placed in corresponding columns of a diagonal
        matrix D, then AV = VD.
        
        Parameters
        -----------
        a : Double2D
            the symmetric matrix A.
        v : Double2D
            the array of eigenvectors v[0], v[1], and v[2].
        d : Double1D
            the array of eigenvalues d[0], d[1], and d[2].
        """

    @staticmethod
    def solveSymmetric33Fast(self, a: Double2D, v: Double2D,
                             d: Double1D) -> None:
        """
        Computes eigenvalues and eigenvectors for a symmetric 3x3 matrix A.
        If the eigenvectors are placed in columns in a matrix V, and the
        eigenvalues are placed in corresponding columns of a diagonal
        matrix D, then AV = VD.
        
        This method is typically faster but not as accurate when eigenvalues
        differ by more than a few orders of magnitude.
        
        Parameters
        -----------
        a : Double2D
            the symmetric matrix A.
        v : Double2D
            the array of eigenvectors v[0], v[1], and v[2].
        d : Double1D
            the array of eigenvalues d[0], d[1], and d[2].
        """
