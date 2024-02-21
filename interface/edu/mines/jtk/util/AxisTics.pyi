from typing import overload
from edu.mines.jtk.mapping import *


class AxisTics:
    """
    Tics for annotating an axis. Given values at the endpoints of the axis,
    axes tics are constructed by computing parameters for both major and
    minor tics. Major tics are a subset of minor tics. Typically, major
    tics are labeled with character strings that represent their values.
    
    Axes tics can be constructed in two ways, by specifying either (1) the
    interval between major tics or (2) the maximum number of major tics.
    
    In the first case, when the major tic interval (a positive number) is
    specified, other tic parameters are easily computed. For example, the
    value of the first major tic equals the smallest multiple of the major
    tic interval that is not less than the minimum of the axis endpoint
    values. Likewise, the number of major tics is computed so that the
    value of the last major tic is not greater than the maximum of the
    axis endpoint values.
    
    In the second case, when the maximum number of major tics is specified,
    the major tic interval is computed to be 2, 5, or 10 times some power
    of 10. Then, other tic parameters are computed as in the first case.
    The tricky part in this second case is choosing the best number from
    the set {2,5,10}. That best number is called the tic <em>multiple</em>,
    and is computed so that the number of major tics is close to, but not
    greater than, the specified maximum number of major tics.
    
    After construction, the counts, increments, and first values of both
    major and minor tics are available.
    """

    @overload
    def __init__(self, x1: double, x2: double, dtic: double) -> None:
        """
        Constructs axis tics for a specified major tic interval.
        
        Parameters
        -----------
        x1 : double
            the value at one end of the axis.
        x2 : double
            the value at the other end of the axis.
        dtic : double
            the major tic interval; a positive number.
        """

    @overload
    def __init__(self, x1: double, x2: double, ntic: int) -> None:
        """
        Constructs axis tics for a specified maximum number of major tics.
        
        Parameters
        -----------
        x1 : double
            the value at one end of the axis.
        x2 : double
            the value at the other end of the axis.
        ntic : int
            the maximum number of major tics.
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
        Gets the tic multiple. The tic multiple is the number of (major
        and minor) tics per major tic, except near the ends of the axis.
        Between any pair of major tics there are multiple-1 minor tics.
        Returns
        --------
        output : int
            the tic multiple.
        """
