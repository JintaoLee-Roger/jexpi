from typing import overload
from edu.mines.jtk.mapping import *


class ArrayVect2:
    """
    Implement a Vect as a two dimensional array of doubles.
    The embedded data are exposed by a getData method.  For all practical
    purposes this member is public, except that this class must always
    point to the same array.  The implementation as an array
    is the point of this class, to avoid duplicate implementations
    elsewhere.  Multiple inheritance is prohibited and
    prevents the mixin pattern, but you can share the wrapped array
    as a private member of your own class,
    and easily delegate all implemented methods.
    """

    @overload
    def __init__(self, data: Double2D, variance: double) -> None:
        """
        Wrap an array as a Vect.
        multiplyInverseCovariance.
        
        Parameters
        -----------
        data : Double2D
            This will be assigned to the public data.
        variance : double
            This variance will be used to divide data in
        """

    @overload
    def __init__(self) -> None:
        """
        To be used with init()
        """

    def getData(self) -> Double2D:
        """
        Get the embedded data.
        Returns
        --------
        output : Double2D
            Same array as passed to constructore.
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

    def clone(self) -> ArrayVect2:
        """
    
        """

    def dot(self, other: VectConst) -> double:
        """
    
        """
