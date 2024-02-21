from typing import overload
from edu.mines.jtk.mapping import *


class SimpleFloat3:
    """
    A simple 3-D array of floats. Implements the generic interface
    {@link edu.mines.jtk.util.Float3} using a straightforward Java 3-D
    array of floats.
    """

    @overload
    def __init__(self, n1: int, n2: int, n3: int) -> None:
        """
        Constructs an array of elements initialized to zero.
        
        Parameters
        -----------
        n1 : int
            the 1st dimension of the array[n3][n2][n1].
        n2 : int
            the 2nd dimension of the array[n3][n2][n1].
        n3 : int
            the 3rd dimension of the array[n3][n2][n1].
        """

    @overload
    def __init__(self, a: Float3D) -> None:
        """
        Constructs an array of elements for the specified array.
        References (does not copy) elements from the specified array.
        
        Parameters
        -----------
        a : Float3D
            array[n3][n2][n1] of elements to be referenced.
        """

    def getN1(self) -> int:
        """
    
        """

    def getN2(self) -> int:
        """
    
        """

    def getN3(self) -> int:
        """
    
        """

    def get1(self, m1: int, j1: int, j2: int, j3: int, s: Float1D) -> None:
        """
    
        """

    def get2(self, m2: int, j1: int, j2: int, j3: int, s: Float1D) -> None:
        """
    
        """

    def get3(self, m3: int, j1: int, j2: int, j3: int, s: Float1D) -> None:
        """
    
        """

    def get12(self, m1: int, m2: int, j1: int, j2: int, j3: int,
              s: Float2D) -> None:
        """
    
        """

    def get13(self, m1: int, m3: int, j1: int, j2: int, j3: int,
              s: Float2D) -> None:
        """
    
        """

    def get23(self, m2: int, m3: int, j1: int, j2: int, j3: int,
              s: Float2D) -> None:
        """
    
        """

    @overload
    def get123(self, m1: int, m2: int, m3: int, j1: int, j2: int, j3: int,
               s: Float3D) -> None:
        """
    
        """

    @overload
    def get123(self, m1: int, m2: int, m3: int, j1: int, j2: int, j3: int,
               s: Float1D) -> None:
        """
    
        """

    def set1(self, m1: int, j1: int, j2: int, j3: int, s: Float1D) -> None:
        """
    
        """

    def set2(self, m2: int, j1: int, j2: int, j3: int, s: Float1D) -> None:
        """
    
        """

    def set3(self, m3: int, j1: int, j2: int, j3: int, s: Float1D) -> None:
        """
    
        """

    def set12(self, m1: int, m2: int, j1: int, j2: int, j3: int,
              s: Float2D) -> None:
        """
    
        """

    def set13(self, m1: int, m3: int, j1: int, j2: int, j3: int,
              s: Float2D) -> None:
        """
    
        """

    def set23(self, m2: int, m3: int, j1: int, j2: int, j3: int,
              s: Float2D) -> None:
        """
    
        """

    @overload
    def set123(self, m1: int, m2: int, m3: int, j1: int, j2: int, j3: int,
               s: Float3D) -> None:
        """
    
        """

    @overload
    def set123(self, m1: int, m2: int, m3: int, j1: int, j2: int, j3: int,
               s: Float1D) -> None:
        """
    
        """
