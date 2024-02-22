from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import *
from edu.mines.jtk.dsp import *


class Gridder3:
    """
    Gridded interpolation of scattered samples of 3D functions f(x1,x2,x3).
    The orthogonal Cartesian grid is defined by uniform samplings of the
    independent variables x1, x2 and x3. A gridder can interpolate on such a
    uniform sampling grid, but may or may not be capable of interpolating at
    other locations (x1,x2,x3) not on the grid, depending on its implementation.
    """

    def setScattered(f: Float1D, x1: Float1D, x2: Float1D,
                     x3: Float1D) -> None:
        """
        Sets the known (scattered) samples.
        The specified arrays may be either referenced or copied,
        depending on the implementation. Unless stated otherwise,
        assume that these arrays are referenced, not copied.
        
        Parameters
        -----------
        f : Float1D
            array of sample values f(x1,x2,x3).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        x3 : Float1D
            array of sample x3 coordinates.
        """

    def grid(s1: Sampling, s2: Sampling, s3: Sampling) -> Float3D:
        """
        Computes gridded sample values from the known sample values.
        Known (scattered) samples must be set before calling this method.
        Some implementations require that the specified samplings be uniform.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of x1.
        s2 : Sampling
            sampling of x2.
        s3 : Sampling
            sampling of x3.
        
        Returns
        --------
        output : Float3D
            array of gridded sample values.
        """
