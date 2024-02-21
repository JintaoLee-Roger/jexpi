from typing import overload
from edu.mines.jtk.mapping import *


class SibsonGridder3:
    """
    Gridding by Sibson interpolation of scattered samples of f(x1,x2,x3).
    This class exists only to implement the interface {@link Gridder3}.
    It otherwise adds no significant functionality to its base class
    {@link SibsonInterpolator3}.
    """

    def __init__(self, f: Float1D, x1: Float1D, x2: Float1D,
                 x3: Float1D) -> None:
        """
        Constructs a gridder with specified known (scattered) samples.
        
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

    def setSmooth(self, smooth: bool) -> None:
        """
        Sets the smoothness of the Sibson interpolant.
        Two values for smoothness are possible.
        
        If false (the default), the interpolant is C1 everywhere except
        at the known sample points, where it is C0, with a discontinuous
        derivative. For this default, interpolated values are guaranteed
        to be within the range of known sample values.
        
        If true, the interpolant is smoother, C1 everywhere, but interpolated
        values may be outside the range of known sample values.
        
        Parameters
        -----------
        smooth : bool
            true, for C1 everywhere; false, for C0 at known samples.
        """

    def setScattered(self, f: Float1D, x1: Float1D, x2: Float1D,
                     x3: Float1D) -> None:
        """
        Sets the known (scattered) samples to be interpolated.
        
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

    def grid(self, s1: Sampling, s2: Sampling, s3: Sampling) -> Float3D:
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
        s3 : Sampling
            sampling of x3.
        
        Returns
        --------
        output : Float3D
            array of gridded sample values.
        """
