from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class WarpFunction3:
    """
    Synthetic warping functions for 3-D images.
    The function u(x) describes the warping, in which a point x
    is displaced to a point y(x) = x+u(x).
    
    Warping is the computation of the image g(y) = f(x(y)).
    Unwarping is the computation of the image f(x) = g(y(x)).
    
    For warping, we need the function x(y) = y-u(x(y)) = y-uy(y). We
    compute the displacement uy(y) by iteration so that uy(y) = u(x(y)).
    
    We also define a midpoint m(x) = (x+y(x))/2, and compute the
    displacement um(m) = u(x(m)) from u(x) by iteration so that
    um(m) = u(x(m)).
    """

    def __init__(self, n1: int, n2: int, n3: int) -> None:
        """
    
        """

    @staticmethod
    def constant(self, u1: double, u2: double, u3: double, n1: int, n2: int,
                 n3: int) -> WarpFunction3:
        """
        Returns a warping for a constant shift.
        
        Parameters
        -----------
        u1 : double
            shift in 1st dimension.
        u2 : double
            shift in 2nd dimension.
        u3 : double
            shift in 3rd dimension.
        n1 : int
            number of samples in 1st dimension.
        n2 : int
            number of samples in 2nd dimension.
        n3 : int
            number of samples in 3rd dimension.
        
        Returns
        --------
        output : WarpFunction3
            a constant-shift 3d warp function.
        """

    @staticmethod
    def gaussian(self, u1: double, u2: double, u3: double, n1: int, n2: int,
                 n3: int) -> WarpFunction3:
        """
        Returns a derivative-of-Gaussian warping.
        
        Parameters
        -----------
        u1 : double
            maximum shift in 1st dimension.
        u2 : double
            maximum shift in 2nd dimension.
        u3 : double
            maximum shift in 3rd dimension.
        n1 : int
            number of samples in 1st dimension.
        n2 : int
            number of samples in 2nd dimension.
        n3 : int
            number of samples in 3rd dimension.
        
        Returns
        --------
        output : WarpFunction3
            a derivative-of-Gaussian 3d warping function.
        """

    @staticmethod
    def sinusoid(self, u1: double, u2: double, u3: double, n1: int, n2: int,
                 n3: int) -> WarpFunction3:
        """
        Returns a sinusoidal warping.
        
        Parameters
        -----------
        u1 : double
            maximum shift in 1st dimension.
        u2 : double
            maximum shift in 2nd dimension.
        u3 : double
            maximum shift in 3rd dimension.
        n1 : int
            number of samples in 1st dimension.
        n2 : int
            number of samples in 2nd dimension.
        n3 : int
            number of samples in 3rd dimension.
        
        Returns
        --------
        output : WarpFunction3
            a sinusoidal 3d warping function.
        """

    @staticmethod
    def constantPlusSinusoid(self, c1: double, c2: double, c3: double,
                             u1: double, u2: double, u3: double, n1: int,
                             n2: int, n3: int) -> WarpFunction3:
        """
        Returns a constant-plus-sinusoidal warping.
        
        Parameters
        -----------
        c1 : double
            constant shift in 1st dimension.
        c2 : double
            constant shift in 2nd dimension.
        c3 : double
            constant shift in 3rd dimension.
        u1 : double
            maximum sinusoidal shift in 1st dimension.
        u2 : double
            maximum sinusoidal shift in 2nd dimension.
        u3 : double
            maximum sinusoidal shift in 3rd dimension.
        n1 : int
            number of samples in 1st dimension.
        n2 : int
            number of samples in 2nd dimension.
        n3 : int
            number of samples in 3rd dimension.
        
        Returns
        --------
        output : WarpFunction3
            a constant-plus-sinusoidal 3d warping function.
        """

    @overload
    def u1(self, x1: double, x2: double, x3: double) -> double:
        """
        Returns the 1st component of the shift u(x).
        
        Parameters
        -----------
        x1 : double
            1st coordinate of the point x.
        x2 : double
            2nd coordinate of the point x.
        x3 : double
            3rd coordinate of the point x.
        
        Returns
        --------
        output : double
            1st component of shift.
        """

    @overload
    def u2(self, x1: double, x2: double, x3: double) -> double:
        """
        Returns the 2nd component of the shift u(x).
        
        Parameters
        -----------
        x1 : double
            1st coordinate of the point x.
        x2 : double
            2nd coordinate of the point x.
        x3 : double
            3rd coordinate of the point x.
        
        Returns
        --------
        output : double
            2nd component of shift.
        """

    @overload
    def u3(self, x1: double, x2: double, x3: double) -> double:
        """
        Returns the 3rd component of the shift u(x).
        
        Parameters
        -----------
        x1 : double
            1st coordinate of the point x.
        x2 : double
            2nd coordinate of the point x.
        x3 : double
            3rd coordinate of the point x.
        
        Returns
        --------
        output : double
            3rd component of shift.
        """

    @overload
    def u1x(self, x1: double, x2: double, x3: double) -> double:
        """
        Returns the 1st component of the shift u(x).
        
        Parameters
        -----------
        x1 : double
            1st coordinate of the point x.
        x2 : double
            2nd coordinate of the point x.
        x3 : double
            3rd coordinate of the point x.
        
        Returns
        --------
        output : double
            1st component of shift.
        """

    @overload
    def u2x(self, x1: double, x2: double, x3: double) -> double:
        """
        Returns the 2nd component of the shift u(x).
        
        Parameters
        -----------
        x1 : double
            1st coordinate of the point x.
        x2 : double
            2nd coordinate of the point x.
        x3 : double
            3rd coordinate of the point x.
        
        Returns
        --------
        output : double
            2nd component of shift.
        """

    @overload
    def u3x(self, x1: double, x2: double, x3: double) -> double:
        """
        Returns the 3rd component of the shift u(x).
        
        Parameters
        -----------
        x1 : double
            1st coordinate of the point x.
        x2 : double
            2nd coordinate of the point x.
        x3 : double
            3rd coordinate of the point x.
        
        Returns
        --------
        output : double
            3rd component of shift.
        """

    @overload
    def u1m(self, m1: double, m2: double, m3: double) -> double:
        """
        Returns the 1st component of the shift um(m) = u(x(m)).
        
        Parameters
        -----------
        m1 : double
            1st coordinate of the point m.
        m2 : double
            2nd coordinate of the point m.
        m3 : double
            3rd coordinate of the point m.
        
        Returns
        --------
        output : double
            1st component of shift.
        """

    @overload
    def u2m(self, m1: double, m2: double, m3: double) -> double:
        """
        Returns the 2nd component of the shift um(m) = u(x(m)).
        
        Parameters
        -----------
        m1 : double
            1st coordinate of the point m.
        m2 : double
            2nd coordinate of the point m.
        m3 : double
            3rd coordinate of the point m.
        
        Returns
        --------
        output : double
            2nd component of shift.
        """

    @overload
    def u3m(self, m1: double, m2: double, m3: double) -> double:
        """
        Returns the 3rd component of the shift um(m) = u(x(m)).
        
        Parameters
        -----------
        m1 : double
            1st coordinate of the point m.
        m2 : double
            2nd coordinate of the point m.
        m3 : double
            3rd coordinate of the point m.
        
        Returns
        --------
        output : double
            3rd component of shift.
        """

    @overload
    def u1y(self, y1: double, y2: double, y3: double) -> double:
        """
        Returns the 1st component of the shift uy(y) = u(x(y)).
        
        Parameters
        -----------
        y1 : double
            1st coordinate of the point y.
        y2 : double
            2nd coordinate of the point y.
        y3 : double
            3rd coordinate of the point y.
        
        Returns
        --------
        output : double
            1st component of shift.
        """

    @overload
    def u2y(self, y1: double, y2: double, y3: double) -> double:
        """
        Returns the 2nd component of the shift uy(y) = u(x(y)).
        
        Parameters
        -----------
        y1 : double
            1st coordinate of the point y.
        y2 : double
            2nd coordinate of the point y.
        y3 : double
            3rd coordinate of the point y.
        
        Returns
        --------
        output : double
            2nd component of shift.
        """

    @overload
    def u3y(self, y1: double, y2: double, y3: double) -> double:
        """
        Returns the 3rd component of the shift uy(y) = u(x(y)).
        
        Parameters
        -----------
        y1 : double
            1st coordinate of the point y.
        y2 : double
            2nd coordinate of the point y.
        y3 : double
            3rd coordinate of the point y.
        
        Returns
        --------
        output : double
            3rd component of shift.
        """

    @overload
    def u1x(self) -> Float3D:
        """
        Returns an array[n3][n2][n1] of 1st components of shifts u(x).
        Returns
        --------
        output : Float3D
            array of 1st components of shifts.
        """

    @overload
    def u2x(self) -> Float3D:
        """
        Returns an array[n3][n2][n1] of 2nd components of shifts u(x).
        Returns
        --------
        output : Float3D
            array of 2nd components of shifts.
        """

    @overload
    def u3x(self) -> Float3D:
        """
        Returns an array[n3][n2][n1] of 3rd components of shifts u(x).
        Returns
        --------
        output : Float3D
            array of 3rd components of shifts.
        """

    @overload
    def u1m(self) -> Float3D:
        """
        Returns an array[n3][n2][n1] of 1st components of shifts um(m) = u(x(m)).
        Returns
        --------
        output : Float3D
            array of 1st components of shifts.
        """

    @overload
    def u2m(self) -> Float3D:
        """
        Returns an array[n3][n2][n1] of 2nd components of shifts um(m) = u(x(m)).
        Returns
        --------
        output : Float3D
            array of 2nd components of shifts.
        """

    @overload
    def u3m(self) -> Float3D:
        """
        Returns an array[n3][n2][n1] of 3rd components of shifts um(m) = u(x(m)).
        Returns
        --------
        output : Float3D
            array of 3rd components of shifts.
        """

    @overload
    def u1y(self) -> Float3D:
        """
        Returns an array[n3][n2][n1] of 1st components of shifts uy(y) = u(x(y)).
        Returns
        --------
        output : Float3D
            array of 1st components of shifts.
        """

    @overload
    def u2y(self) -> Float3D:
        """
        Returns an array[n3][n2][n1] of 2nd components of shifts uy(y) = u(x(y)).
        Returns
        --------
        output : Float3D
            array of 2nd components of shifts.
        """

    @overload
    def u3y(self) -> Float3D:
        """
        Returns an array[n3][n2][n1] of 3rd components of shifts uy(y) = u(x(y)).
        Returns
        --------
        output : Float3D
            array of 3rd components of shifts.
        """

    def warp1(self, f: Float3D) -> Float3D:
        """
        Warps a sampled function using only 1st components of shifts.
        
        Parameters
        -----------
        f : Float3D
            array of values f(x).
        
        Returns
        --------
        output : Float3D
            array of values g(y) = f(y-u1(x(y)).
        """

    def warp(self, f: Float3D) -> Float3D:
        """
        Warps a sampled function using only all components of shifts.
        
        Parameters
        -----------
        f : Float3D
            array of values f(x).
        
        Returns
        --------
        output : Float3D
            array of values g(y) = f(y-u(x(y)).
        """

    def unwarp1(self, g: Float3D) -> Float3D:
        """
        Unwarps a sampled function using only 1st components of shifts.
        
        Parameters
        -----------
        g : Float3D
            array of values g(x).
        
        Returns
        --------
        output : Float3D
            array of values f(x) = g(x+u1(x)).
        """

    def unwarp(self, g: Float3D) -> Float3D:
        """
        Unwarps a sampled function using only all components of shifts.
        
        Parameters
        -----------
        g : Float3D
            array of values g(x).
        
        Returns
        --------
        output : Float3D
            array of values f(x) = g(x+u(x)).
        """
