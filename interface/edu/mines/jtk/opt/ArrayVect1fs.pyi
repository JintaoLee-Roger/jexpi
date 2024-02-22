from typing import overload, List
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class ArrayVect1fs:
    """
    Implements a Vect as a collection of ArrayVect1f's of fixed size.
    """

    @overload
    def __init__(self, data: List[ArrayVect1f]) -> None:
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

    def getData(self) -> List[ArrayVect1f]:
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
