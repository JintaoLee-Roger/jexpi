from typing import overload
from edu.mines.jtk.mapping import *


class ArrayVect1:
    """
    Implements a Vect by wrapping an array of doubles.
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
    def __init__(self, data: Double1D, variance: double) -> None:
        """
        Construct from an array of data.
        will divide all samples by this number.  Pass a value
        of 1 if you do not care.
        
        Parameters
        -----------
        data : Double1D
            This is the data that will be manipulated.
        variance : double
            The method multiplyInverseCovariance()
        """

    @overload
    def __init__(self) -> None:
        """
        To be used with init()
        """

    def getSize(self) -> int:
        """
        Return the size of the embedded array
        Returns
        --------
        output : int
            size of the embedded array
        """

    def getData(self) -> Double1D:
        """
        Get the embedded data
        Returns
        --------
        output : Double1D
            Same array as passed to constructore.
        """

    def clone(self) -> ArrayVect1:
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
