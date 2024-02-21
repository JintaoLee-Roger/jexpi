from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class WarpFunction1:
    """
    Synthetic warping functions for 1-D sequences.
    The function u(x) describes the warping, in which a point x
    is displaced to a point y(x) = x+u(x).
    
    Warping is the computation of the sequence g(y) = f(x(y)).
    Unwarping is the computation of the sequence f(x) = g(y(x)).
    
    For warping, we need the function x(y) = y-u(x(y)) = y-uy(y). We
    compute the displacement uy(y) by iteration so that uy(y) = u(x(y)).
    
    We also define a midpoint m(x) = (x+y(x))/2, and compute the
    displacement um(m) = u(x(m)) from u(x) by iteration so that
    um(m) = u(x(m)).
    """

    def __init__(self, n: int) -> None:
        """
    
        """

    @staticmethod
    def constant(self, u: double, n: int) -> WarpFunction1:
        """
        Returns a warping for a constant shift.
        
        Parameters
        -----------
        u : double
            shift.
        n : int
            number of samples.
        
        Returns
        --------
        output : WarpFunction1
            a constant-shift 1d warping function.
        """

    @staticmethod
    def gaussian(self, u: double, n: int) -> WarpFunction1:
        """
        Returns a derivative-of-Gaussian warping.
        
        Parameters
        -----------
        u : double
            maximum shift.
        n : int
            number of samples.
        
        Returns
        --------
        output : WarpFunction1
            a derivative-of-Gaussian 1d warping function.
        """

    @staticmethod
    def sinusoid(self, u: double, n: int) -> WarpFunction1:
        """
        Returns a sinusoidal warping.
        
        Parameters
        -----------
        u : double
            maximum shift.
        n : int
            number of samples.
        
        Returns
        --------
        output : WarpFunction1
            a sinusoidal 1d warping function.
        """

    @staticmethod
    def constantPlusSinusoid(self, c: double, u: double,
                             n: int) -> WarpFunction1:
        """
        Returns a constant-plus-sinusoidal warping.
        
        Parameters
        -----------
        c : double
            constant shift.
        u : double
            maximum sinusoidal shift.
        n : int
            number of samples.
        
        Returns
        --------
        output : WarpFunction1
            a constant-plus-sinusoidal 1d warping function.
        """

    @overload
    def u(self, x: double) -> double:
        """
        Returns the shift u(x).
        
        Parameters
        -----------
        x : double
            the coordinate x.
        
        Returns
        --------
        output : double
            the shift.
        """

    @overload
    def ux(self, x: double) -> double:
        """
        Returns the shift u(x).
        
        Parameters
        -----------
        x : double
            the coordinate x.
        
        Returns
        --------
        output : double
            the shift.
        """

    @overload
    def um(self, m: double) -> double:
        """
        Returns the shift um(m) = u(x(m)).
        
        Parameters
        -----------
        m : double
            the coordinate m.
        
        Returns
        --------
        output : double
            the shift.
        """

    @overload
    def uy(self, y: double) -> double:
        """
        Returns the shift uy(y) = u(x(y)).
        
        Parameters
        -----------
        y : double
            the coordinate y.
        
        Returns
        --------
        output : double
            the shift.
        """

    @overload
    def ux(self) -> Float1D:
        """
        Returns an array[n] of shifts u(x).
        Returns
        --------
        output : Float1D
            array of shifts.
        """

    @overload
    def um(self) -> Float1D:
        """
        Returns an array[n] of shifts um(m) = u(x(m)).
        Returns
        --------
        output : Float1D
            array of shifts.
        """

    @overload
    def uy(self) -> Float1D:
        """
        Returns an array[n] of shifts uy(y) = u(x(y)).
        Returns
        --------
        output : Float1D
            array of shifts.
        """

    def warp(self, f: Float1D) -> Float1D:
        """
        Warps a sampled function.
        
        Parameters
        -----------
        f : Float1D
            array of values f(x).
        
        Returns
        --------
        output : Float1D
            array of values g(y) = f(y-u(x(y)).
        """

    def unwarp(self, g: Float1D) -> Float1D:
        """
        Unwarps a sampled function.
        
        Parameters
        -----------
        g : Float1D
            array of values g(x).
        
        Returns
        --------
        output : Float1D
            array of values f(x) = g(x+u(x)).
        """
