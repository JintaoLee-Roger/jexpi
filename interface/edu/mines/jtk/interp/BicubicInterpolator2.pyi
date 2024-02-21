from typing import overload
from edu.mines.jtk.mapping import *


class BicubicInterpolator2:
    """
    Piecewise bicubic polynomial interpolation of a function y(x1,x2).
    The interpolated function has continuous first derivatives dy/d1, dy/d2 and
    cross-derivatives ddy/d1d2. First derivatives are computed using methods
    that may be specified for each dimension. Cross-derivatives are computed by
    averaging derivatives of first derivatives.
    
    The function y(x1,x2) is specified by samples on a regular grid, which need
    not be uniform. The regular grid is specified by one-dimensional arrays of
    monotonically increasing coordinates x1 and x2, such that gridded x1 are
    identical for all gridded x2, and gridded x2 are identical for all gridded
    x1.
    
    Extrapolation (that is, interpolation outside the specified grid of (x1,x2)
    coordinates), is performed using cubic polynomials for the nearest grid
    samples. Extrapolated values can be well outside the [min,max] range of
    interpolated values, and should typically be avoided.
    """

    @overload
    def __init__(self, x1: Float1D, x2: Float1D, y: Float2D) -> None:
        """
        Constructs an interpolator for specified values y(x1,x2).
        
        Parameters
        -----------
        x1 : Float1D
            array[n1] of x1 coordinates; monotonically increasing.
        x2 : Float1D
            array[n2] of x2 coordinates; monotonically increasing.
        y : Float2D
            array[n2][n1] of sampled values y(x1,x2).
        """

    @overload
    def __init__(self, method1: Method, method2: Method, x1: Float1D,
                 x2: Float1D, y: Float2D) -> None:
        """
        Constructs an interpolator for specified methods and values.
        
        Parameters
        -----------
        method1 : Method
            method used to compute dy/d1.
        method2 : Method
            method used to compute dy/d2.
        x1 : Float1D
            array[n1] of x1 coordinates; monotonically increasing.
        x2 : Float1D
            array[n2] of x2 coordinates; monotonically increasing.
        y : Float2D
            array[n2][n1] of sampled values y(x1,x2).
        """

    @overload
    def __init__(self, method1: Method, method2: Method, n1: int, n2: int,
                 x1: Float1D, x2: Float1D, y: Float2D) -> None:
        """
        Constructs an interpolator for specified methods and values.
        
        Parameters
        -----------
        method1 : Method
            method used to compute dy/d1.
        method2 : Method
            method used to compute dy/d2.
        n1 : int
            number of x1 coordinates.
        n2 : int
            number of x2 coordinates.
        x1 : Float1D
            array[n1] of x1 coordinates; monotonically increasing.
        x2 : Float1D
            array[n2] of x2 coordinates; monotonically increasing.
        y : Float2D
            array[n2][n1] of sampled values y(x1,x2).
        """

    @overload
    def interpolate(self, x1: float, x2: float) -> float:
        """
        Returns interpolated value y.
        Same as {@link #interpolate00(float,float)}.
        
        Parameters
        -----------
        x1 : float
            coordinate x1.
        x2 : float
            coordinate x2.
        
        Returns
        --------
        output : float
            interpolated y(x1,x2).
        """

    @overload
    def interpolate00(self, x1: float, x2: float) -> float:
        """
        Returns interpolated value y.
        
        Parameters
        -----------
        x1 : float
            coordinate x1.
        x2 : float
            coordinate x2.
        
        Returns
        --------
        output : float
            interpolated y(x1,x2).
        """

    def interpolate10(self, x1: float, x2: float) -> float:
        """
        Returns interpolated partial derivative dy/d1.
        
        Parameters
        -----------
        x1 : float
            coordinate x1.
        x2 : float
            coordinate x2.
        
        Returns
        --------
        output : float
            interpolated dy/d1.
        """

    def interpolate01(self, x1: float, x2: float) -> float:
        """
        Returns interpolated partial derivative dy/d2.
        
        Parameters
        -----------
        x1 : float
            coordinate x1.
        x2 : float
            coordinate x2.
        
        Returns
        --------
        output : float
            interpolated dy/d2.
        """

    @overload
    def interpolate(self, s1: Sampling, s2: Sampling) -> Float2D:
        """
        Returns an array of interpolated values y.
        Same as {@link #interpolate00(Sampling,Sampling)}.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of coordinate x1.
        s2 : Sampling
            sampling of coordinate x2.
        
        Returns
        --------
        output : Float2D
            interpolated y(x1,x2).
        """

    @overload
    def interpolate00(self, s1: Sampling, s2: Sampling) -> Float2D:
        """
        Returns an array of interpolated values y.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of coordinate x1.
        s2 : Sampling
            sampling of coordinate x2.
        
        Returns
        --------
        output : Float2D
            interpolated y(x1,x2).
        """

    @overload
    def interpolate(self, s1: Sampling, s2: Sampling, y: Float2D) -> None:
        """
        Computes an array of interpolated values y.
        Same as {@link #interpolate00(Sampling,Sampling,float[][])}.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of coordinate x1.
        s2 : Sampling
            sampling of coordinate x2.
        y : Float2D
            output array of interpolated y(x1,x2).
        """

    @overload
    def interpolate00(self, s1: Sampling, s2: Sampling, y: Float2D) -> None:
        """
        Computes an array of interpolated values y.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of coordinate x1.
        s2 : Sampling
            sampling of coordinate x2.
        y : Float2D
            output array of interpolated y(x1,x2).
        """

    @overload
    def interpolate(self, x1: Float1D, x2: Float1D) -> Float2D:
        """
        Returns an array of interpolated values y.
        Same as {@link #interpolate00(float[],float[])}.
        
        Parameters
        -----------
        x1 : Float1D
            array[n1] of coordinates x1.
        x2 : Float1D
            array[n2] of coordinates x2.
        
        Returns
        --------
        output : Float2D
            array[n2][n1] of interpolated y(x1,x2).
        """

    @overload
    def interpolate00(self, x1: Float1D, x2: Float1D) -> Float2D:
        """
        Returns an array of interpolated values y.
        
        Parameters
        -----------
        x1 : Float1D
            array[n1] of coordinates x1.
        x2 : Float1D
            array[n2] of coordinates x2.
        
        Returns
        --------
        output : Float2D
            array[n2][n1] of interpolated y(x1,x2).
        """

    @overload
    def interpolate(self, x1: Float1D, x2: Float1D, y: Float2D) -> None:
        """
        Computes an array of interpolated values y.
        Same as {@link #interpolate00(float[],float[],float[][])}.
        
        Parameters
        -----------
        x1 : Float1D
            array[n1] of coordinates x1.
        x2 : Float1D
            array[n2] of coordinates x2.
        y : Float2D
            output array[n2][n1] of interpolated y(x1,x2).
        """

    @overload
    def interpolate00(self, x1: Float1D, x2: Float1D, y: Float2D) -> None:
        """
        Computes an array of interpolated values y.
        
        Parameters
        -----------
        x1 : Float1D
            array[n1] of coordinates x1.
        x2 : Float1D
            array[n2] of coordinates x2.
        y : Float2D
            output array[n2][n1] of interpolated y(x1,x2).
        """
