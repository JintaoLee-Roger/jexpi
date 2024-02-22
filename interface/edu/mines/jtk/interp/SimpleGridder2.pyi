from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import *
from edu.mines.jtk.dsp import *


class SimpleGridder2:
    """
    Simple griding of scattered samples of 2D functions f(x1,x2).
    Each gridded value is simply the average of the values of all known
    samples that lie within the corresponding grid cell. For a grid cell
    that contains no such known samples, the gridded value is null.
    
    Note that this simple method performs no interpolation for grid cells
    that do not contain at least one scattered sample. It may however be
    used as a first step in other more sophisticated gridding methods. In
    particular, the averaging performed by this simple gridder provides a
    crude form of anti-alias filtering when grid cells contain multiple
    scattered samples.
    """

    def __init__(self, f: Float1D, x1: Float1D, x2: Float1D) -> None:
        """
        Constructs a simple gridder with specified known samples.
        The specified arrays are referenced, not copied.
        
        Parameters
        -----------
        f : Float1D
            array of known sample values f(x1,x2).
        x1 : Float1D
            array of known sample x1 coordinates.
        x2 : Float1D
            array of known sample x2 coordinates.
        """

    def setNullValue(self, fnull: float) -> None:
        """
        Sets the null value used for grid cells that contain no known samples.
        The default null value is zero.
        
        Parameters
        -----------
        fnull : float
            the null value.
        """

    @overload
    @staticmethod
    def samplesOnGrid(self, s1: Sampling, s2: Sampling, f: Float1D,
                      x1: Float1D, x2: Float1D) -> Float2D:
        """
        Returns samples adjusted to lie on a specified grid.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of x1.
        s2 : Sampling
            sampling of x2.
        f : Float1D
            array of sample values f(x1,x2).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        
        Returns
        --------
        output : Float2D
            array {f,x1,x2} of arrays of samples after gridding.
        """

    @overload
    @staticmethod
    def samplesOnGrid(self, s1: Sampling, s2: Sampling, f: Float1D,
                      x1: Float1D, x2: Float1D, sd: Float1D) -> Float2D:
        """
        Returns samples adjusted to lie on a specified grid.
        Sample values may have uncertainties, specified as standard
        deviations of errors assumed to be uncorrelated and to have
        zero mean.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of x1.
        s2 : Sampling
            sampling of x2.
        f : Float1D
            array of sample values f(x1,x2).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        sd : Float1D
            array of std dev for sample values; null, if none.
        
        Returns
        --------
        output : Float2D
            array {f,x1,x2,sd} of arrays of samples after gridding.
        """

    @staticmethod
    def getGriddedSamples(self, fnull: float, s1: Sampling, s2: Sampling,
                          g: Float2D) -> Float2D:
        """
        Gets the non-null samples from the specified gridded sample values.
        
        Parameters
        -----------
        fnull : float
            the null value.
        s1 : Sampling
            sampling of x1.
        s2 : Sampling
            sampling of x2.
        g : Float2D
            array of gridded sample values.
        
        Returns
        --------
        output : Float2D
            array {f,x1,x2} of arrays of non-null samples.
        """

    def setScattered(self, f: Float1D, x1: Float1D, x2: Float1D) -> None:
        """
    
        """

    def grid(self, s1: Sampling, s2: Sampling) -> Float2D:
        """
    
        """
