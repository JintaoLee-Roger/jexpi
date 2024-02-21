from typing import overload
from edu.mines.jtk.mapping import *


class ArrayVect1fs:
    """
    Implements a Vect as a collection of ArrayVect1f's of fixed size.
    """

    @overload
    def __init__(self, data: ArrayVect1f1D) -> None:
        """
        Wrap an array of ArrayVect1f's
        """

    @overload
    def __init__(self) -> None:
        """
        To be used with init()
        """

    def getSize(self) -> int:
        """
        Return the size of the embedded array
        """

    def getData(self) -> ArrayVect1f1D:
        """
        Get the embedded data
        """

    def clone(self) -> ArrayVect1fs:
        """
    
        """

    def dot(self, other: VectConst) -> double:
        """
    
        """

    def toString(self) -> String:
        """
    
        """

    def dispose(self) -> None:
        """
    
        """

    def multiplyInverseCovariance(self) -> None:
        """
    
        """

    def constrain(self) -> None:
        """
    
        """

    def postCondition(self) -> None:
        """
    
        """

    def add(self, scaleThis: double, scaleOther: double,
            other: VectConst) -> None:
        """
    
        """

    def project(self, scaleThis: double, scaleOther: double,
                other: VectConst) -> None:
        """
    
        """

    def magnitude(self) -> double:
        """
    
        """
