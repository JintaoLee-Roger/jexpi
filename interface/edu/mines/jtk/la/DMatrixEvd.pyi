from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.la import *


class DMatrixEvd:
    """
    Eigenvalue and eigenvector decomposition of a square matrix A.
    
    If A is symmetric, then A = VDV' where the matrix of eigenvalues D
    is diagonal and the matrix of eigenvectors V is orthogonal (VV' = I).
    
    If A is not symmetric, then the eigenvalue matrix D is block diagonal
    with real eigenvalues in 1-by-1 blocks and any complex eigenvalues
    lambda + imu in 2-by-2 block [lambda, mu; -mu, lambda]. The columns
    of V represent the eigenvectors in the sense that AV = VD. The matrix
    V may be badly conditioned or even singular, so the validity of the
    equation A = VDinverse(V) depends on the condition number of V.
    
    This class was adapted from the package Jama, which was developed by
    Joe Hicklin, Cleve Moler, and Peter Webb of The MathWorks, Inc., and by
    Ronald Boisvert, Bruce Miller, Roldan Pozo, and Karin Remington of the
    National Institue of Standards and Technology.
    """

    def __init__(self, a: DMatrix) -> None:
        """
        Constructs an eigenvalue decomposition for the specified square matrix.
        
        Parameters
        -----------
        a : DMatrix
            the square matrix
        """

    def getV(self) -> DMatrix:
        """
        Gets the matrix of eigenvectors V.
        Returns
        --------
        output : DMatrix
            the matrix V.
        """

    def getD(self) -> DMatrix:
        """
        Gets the block diagonal matrix of eigenvalues D.
        Returns
        --------
        output : DMatrix
            the matrix D.
        """

    def getRealEigenvalues(self) -> Double1D:
        """
        Gets the real parts of the eigenvalues.
        Returns
        --------
        output : Double1D
            array of real parts = real(diag(D)).
        """

    def getImagEigenvalues(self) -> Double1D:
        """
        Gets the imaginary parts of the eigenvalues
        Returns
        --------
        output : Double1D
            array of imaginary parts = imag(diag(D))
        """
