from typing import overload
from edu.mines.jtk.mapping import *


class ArrayVect3f:
    """
    Implement a Vect as a three-dimensional array of floats.
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
    def __init__(self, data: Float3D, variance: double) -> None:
        """
        Wrap an array as a Vect.
        multiplyInverseCovariance.
        
        Parameters
        -----------
        data : Float3D
            This will be assigned to the public data.
        variance : double
            This variance will be used to divide data in
        """

    @overload
    def __init__(self) -> None:
        """
        To be used with init()
        """

    def getVariance(self) -> double:
        """
        Get the value of the variance passed to the constructor.
        multiplyInverseCovariance.
        Returns
        --------
        output : double
            This variance will be used to divide data in
        """

    def getData(self) -> Float3D:
        """
        Get the embedded data.
        Returns
        --------
        output : Float3D
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

    def clone(self) -> ArrayVect3f:
        """
    
        """

    def dot(self, other: VectConst) -> double:
        """
    
        """
