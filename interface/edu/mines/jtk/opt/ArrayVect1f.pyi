from typing import overload
from edu.mines.jtk.mapping import *


class ArrayVect1f:
    """
    Implements a Vect by wrapping an array of floats.
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
    def __init__(self, data: Float1D, firstSample: int,
                 variance: double) -> None:
        """
        Construct from an array of data.
        Earlier samples should be constrained to zero.
        will divide all samples by this number.  Pass a value
        of 1 if you do not care.
        
        Parameters
        -----------
        data : Float1D
            This is the data that will be manipulated.
        firstSample : int
            This is the first sample to treat as non-zero.
        variance : double
            The method multiplyInverseCovariance()
        """

    @overload
    def __init__(self) -> None:
        """
        Constructor for derived classes that call init()
        """

    def getFirstSample(self) -> int:
        """
        This is the first sample to treat as non-zero.
        Returns
        --------
        output : int
            first non-zero sample
        """

    def getSize(self) -> int:
        """
        Return the size of the embedded array
        Returns
        --------
        output : int
            size of embedded array
        """

    def getData(self) -> Float1D:
        """
        Get the embedded data
        Returns
        --------
        output : Float1D
            Same array as passed to constructor.
        """

    def setData(self, data: Float1D) -> None:
        """
        Set the internal data array to new values.
        
        Parameters
        -----------
        data : Float1D
            Copy this data into the internal wrapped array.
        """

    @staticmethod
    def fillContainer(self, container: VectContainer, firstSamples: Int1D,
                      data: Float2D, variance: double) -> None:
        """
        Fill a VectContainer with instances of ArrayVect1f
        from a 2D array.
        wrapped as ArrayVect1f.
        
        Parameters
        -----------
        container : VectContainer
            Container to be filled with instances of float[]
        firstSamples : Int1D
            Array of data to be wrapped.
        data : Float2D
            Array of first non-zero samples in each array.
        variance : double
            Variance of each ArrayVect1f
        """

    @staticmethod
    def extractContainer(self, data: Float2D,
                         container: VectContainer) -> None:
        """
        Extract 2D array from a VectContainer with instances of ArrayVect1f.
        
        Parameters
        -----------
        data : Float2D
            Array of data to be extracted.
        container : VectContainer
            Container of ArrayVect1f to be extracted from.
        """

    def clone(self) -> ArrayVect1f:
        """
    
        """

    def toString(self) -> String:
        """
    
        """

    def dot(self, other: VectConst) -> double:
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

    def postCondition(self) -> None:
        """
    
        """
