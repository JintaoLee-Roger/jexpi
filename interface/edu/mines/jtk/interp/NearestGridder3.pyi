from typing import overload
from edu.mines.jtk.mapping import *


class NearestGridder3:
    """
    Nearest neighbor gridding of scattered samples of 3D functions f(x1,x2,x3).
    Each gridded value is the value of the nearest known (scattered) sample.
    This gridder can also compute distances to those nearest known samples.
    """

    def __init__(self, f: Float1D, x1: Float1D, x2: Float1D,
                 x3: Float1D) -> None:
        """
        Constructs a nearest neighbor gridder with specified known samples.
        The specified arrays are copied; not referenced.
        
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

    def computeDistancesAndValues(self, s1: Sampling, s2: Sampling,
                                  s3: Sampling, d: Float3D,
                                  g: Float3D) -> None:
        """
        Computes nearest neighbor distances and values.
        
        Parameters
        -----------
        s1 : Sampling
            sampling for coordinate x1.
        s2 : Sampling
            sampling for coordinate x2.
        s3 : Sampling
            sampling for coordinate x3.
        d : Float3D
            array of distances to nearest known samples.
        g : Float3D
            array of nearest known sample values.
        """

    def setScattered(self, f: Float1D, x1: Float1D, x2: Float1D,
                     x3: Float1D) -> None:
        """
    
        """

    def grid(self, s1: Sampling, s2: Sampling, s3: Sampling) -> Float3D:
        """
    
        """
