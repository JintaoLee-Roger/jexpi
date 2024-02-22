from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import *
from edu.mines.jtk.dsp import *


class SimpleGridder3:
    """
    Simple griding of scattered samples of 3D functions f(x1,x2,x3).
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

    def __init__(self, f: Float1D, x1: Float1D, x2: Float1D,
                 x3: Float1D) -> None:
        """
        Constructs a simple gridder with specified known samples.
        The specified arrays are referenced, not copied.
        
        Parameters
        -----------
        f : Float1D
            array of known sample values f(x1,x2,x3).
        x1 : Float1D
            array of known sample x1 coordinates.
        x2 : Float1D
            array of known sample x2 coordinates.
        x3 : Float1D
            array of known sample x3 coordinates.
        """

    def setNullValue(self, fnull: float) -> None:
        """
        Sets the null value used for grid cells that contain no known samples.
        
        Parameters
        -----------
        fnull : float
            the null value.
        """

    @staticmethod
    def getGriddedSamples(self, fnull: float, s1: Sampling, s2: Sampling,
                          s3: Sampling, g: Float3D) -> Float2D:
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
        s3 : Sampling
            sampling of x3.
        g : Float3D
            array of gridded sample values.
        
        Returns
        --------
        output : Float2D
            array {f,x1,x2,x3} of arrays of non-null samples.
        """

    def setScattered(self, f: Float1D, x1: Float1D, x2: Float1D,
                     x3: Float1D) -> None:
        """
    
        """

    def grid(self, s1: Sampling, s2: Sampling, s3: Sampling) -> Float3D:
        """
    
        """
