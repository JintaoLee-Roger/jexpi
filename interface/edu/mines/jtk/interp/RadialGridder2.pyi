from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import RadialInterpolator2
from edu.mines.jtk.dsp import Sampling


class RadialGridder2:
    """
    Gridding by interpolation with radial basis functions.
    This class exists only to implement the interface {@link Gridder2}.
    It otherwise adds no significant functionality to its base class
    {@link RadialInterpolator2}.
    """

    def __init__(self, basis: RadialInterpolator2, f: Float1D, x1: Float1D,
                 x2: Float1D) -> None:
        """
        Constructs a gridder with specified known (scattered) samples.
        
        Parameters
        -----------
        basis : RadialInterpolator2
            the radial basis function.
        f : Float1D
            array of known sample values f(x1,x2).
        x1 : Float1D
            array of known sample x1 coordinates.
        x2 : Float1D
            array of known sample x2 coordinates.
        """

    def setScattered(self, f: Float1D, x1: Float1D, x2: Float1D) -> None:
        """
        Sets the known (scattered) samples to be interpolated.
        
        Parameters
        -----------
        f : Float1D
            array of sample values f(x1,x2).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        """

    def grid(self, s1: Sampling, s2: Sampling) -> Float2D:
        """
        Computes gridded sample values from the known sample values.
        Before interpolating, this method sets the bounds to be consistent
        with the first and last values of the specified samplings, so that
        interpolated values will never be null.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of x1.
        s2 : Sampling
            sampling of x2.
        
        Returns
        --------
        output : Float2D
            array of gridded sample values.
        """
