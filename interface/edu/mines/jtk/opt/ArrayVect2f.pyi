from typing import overload
from edu.mines.jtk.mapping import *


class ArrayVect2f:
    """
    Implement a Vect as a two dimensional array of floats.
    """

    @overload
    def __init__(self, data: Float2D, variance: double) -> None:
        """
        Wrap an array as a Vect.
        """

    @overload
    def __init__(self, data: Float2D, firstSample: Int1D,
                 variance: double) -> None:
        """
        Wrap an array as a Vect.
        """

    @overload
    def __init__(self) -> None:
        """
        To be used with init()
        """

    def getData(self) -> Float2D:
        """
        Get the embedded data.
        """

    def dataChanged(self) -> None:
        """
        Call this method when there has been any external change
        """

    def getSize(self) -> int:
        """
        Return the size of the embedded array
        Returns
        --------
        output : int
            size of embedded array
        """

    def add(self, scaleThis: double, scaleOther: double,
            other: VectConst) -> None:
        """
    
        """

    def project(self, scaleThis: double, scaleOther: double,
                other: VectConst) -> None:
        """
    
        """

    def dispose(self) -> None:
        """
    
        """

    def multiplyInverseCovariance(self) -> None:
        """
    
        """

    def magnitude(self) -> double:
        """
    
        """

    def constrain(self) -> None:
        """
    
        """

    def postCondition(self) -> None:
        """
    
        """

    def clone(self) -> ArrayVect2f:
        """
    
        """

    def dot(self, other: VectConst) -> double:
        """
    
        """
