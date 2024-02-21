from typing import overload
from edu.mines.jtk.mapping import *


class LogAxisTics:
    """
    LogAxisTics is a subclass of AxisTics that computes the information
    needed to draw logarithmically scaled tic marks. A LogAxisTics object
    is constructed by providing the value range end points x1 and x2.
    
    Powers of ten in the value range are drawn as the labeled major tics,
    and all eight intermediate values between two successive decades are
    drawn as minor tics. Currently it does not intelligently decide the
    number of major tics to draw, it will only draw tics as previously
    described.
    """

    def __init__(self, x1: double, x2: double) -> None:
        """
        Constructs axis tics for a specified maximum number of major tics.
        
        Parameters
        -----------
        x1 : double
            the value at one end of the axis.
        x2 : double
            the value at the other end of the axis.
        """

    def getCountMajor(self) -> int:
        """
        Gets the number of major tics.
        Returns
        --------
        output : int
            the number of major tics.
        """

    def getDeltaMajor(self) -> double:
        """
        Gets major tic interval.
        Returns
        --------
        output : double
            the major tic interval.
        """

    def getFirstMajor(self) -> double:
        """
        Gets the value of the first major tic.
        Returns
        --------
        output : double
            the value of the first major tic.
        """

    def getCountMinor(self) -> int:
        """
        Gets the number of minor tics.
        Returns
        --------
        output : int
            the number of minor tics.
        """

    def getDeltaMinor(self) -> double:
        """
        Gets minor tic interval.
        Returns
        --------
        output : double
            the minor tic interval.
        """

    def getFirstMinor(self) -> double:
        """
        Gets the value of the first minor tic.
        Returns
        --------
        output : double
            the value of the first minor tic.
        """

    def getMultiple(self) -> int:
        """
        Gets the tic multiple. The tic multiple is the number of (major and minor)
        tics per major tic, except near the ends of the axis. Between any pair of
        major tics there are multiple-1 minor tics.
        Returns
        --------
        output : int
            the tic multiple.
        """

    def getFirstMinorSkip(self) -> int:
        """
        Gets the minor tic skip value, the first minor tic at which to skip because
        it coincides with a major tic.
        Returns
        --------
        output : int
            the first minor tic to skip
        """
