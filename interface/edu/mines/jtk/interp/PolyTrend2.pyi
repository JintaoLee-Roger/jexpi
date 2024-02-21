from typing import overload
from edu.mines.jtk.mapping import *


class PolyTrend2:
    """
    A low-order polynomial trend in scattered data f(x1,x2).
    The trend is computed by least-squares fitting of the scattered
    data values. This class enables the computed trend to be easily
    removed from scattered data and restored to interpolated data.
    """

    def __init__(self, order: int, f: Float1D, x1: Float1D,
                 x2: Float1D) -> None:
        """
        Constructs a trend with specified scattered samples.
        The specified arrays are referenced; not copied.
        
        If insufficient samples are available for the specified order,
        then a fit is performed with a polynomial of lower order than
        that specified. Note that an order zero (constant) polynomial
        fit is always possible when at least one sample is specified.
        
        Parameters
        -----------
        order : int
            order of polynomial; must be 0, 1, or 2.
        f : Float1D
            array of sample values f(x1,x2).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        """

    def setSamples(self, f: Float1D, x1: Float1D, x2: Float1D) -> None:
        """
        Sets the known (scattered) samples to be fit.
        The specified arrays are referenced, not copied.
        
        Parameters
        -----------
        f : Float1D
            array of sample values f(x1,x2).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        """

    @overload
    def detrend(self) -> None:
        """
        Removes this trend from its referenced scattered sample values.
        Modifies values in the array f referenced by this trend.
        """

    @overload
    def restore(self) -> None:
        """
        Restores this trend to its referenced scattered sample valuess.
        Modifies values in the array f referenced by this trend.
        """

    @overload
    def detrend(self, f: float, x1: float, x2: float) -> float:
        """
        Removes this trend from the specified sample.
        
        Parameters
        -----------
        f : float
            the sample value.
        x1 : float
            the sample x1 coordinate.
        x2 : float
            the sample x2 coordinate.
        
        Returns
        --------
        output : float
            the sample value with trend removed.
        """

    @overload
    def restore(self, f: float, x1: float, x2: float) -> float:
        """
        Restores this trend to the specified sample.
        
        Parameters
        -----------
        f : float
            the sample value.
        x1 : float
            the sample x1 coordinate.
        x2 : float
            the sample x2 coordinate.
        
        Returns
        --------
        output : float
            the sample value with trend restored.
        """

    @overload
    def detrend(self, f: Float1D, x1: Float1D, x2: Float1D) -> None:
        """
        Removes this trend from the specified samples.
        
        Parameters
        -----------
        f : Float1D
            array of sample values to be detrended.
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        """

    @overload
    def restore(self, f: Float1D, x1: Float1D, x2: Float1D) -> None:
        """
        Restores this trend to the specified samples.
        
        Parameters
        -----------
        f : Float1D
            array of sample values to be restored.
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        """

    @overload
    def detrend(self, f: Float2D, s1: Sampling, s2: Sampling) -> None:
        """
        Removes this trend from the specified samples.
        
        Parameters
        -----------
        f : Float2D
            array of sample values to be detrended.
        s1 : Sampling
            sampling of x1 coordinates.
        s2 : Sampling
            sampling of x2 coordinates.
        """

    @overload
    def restore(self, f: Float2D, s1: Sampling, s2: Sampling) -> None:
        """
        Restores this trend to the specified samples.
        
        Parameters
        -----------
        f : Float2D
            array of sample values to be restored.
        s1 : Sampling
            sampling of x1 coordinates.
        s2 : Sampling
            sampling of x2 coordinates.
        """
