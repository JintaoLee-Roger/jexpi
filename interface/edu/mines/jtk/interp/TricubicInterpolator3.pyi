from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import *
from edu.mines.jtk.dsp import *


class TricubicInterpolator3:
    """
    Piecewise tricubic polynomial interpolation of a function y(x1,x2,x3).
    The interpolated function has continuous first derivatives dy/d1, dy/d2,
    dy/d3 and cross-derivatives ddy/d1d2, ddy/d1d3, ddy/d2d3 and dddy/d1d2d3.
    First derivatives are computed using methods that may be specified for each
    dimension. Cross-derivatives are computed by averaging derivatives of first
    derivatives.
    
    The function y(x1,x2,x3) is specified by samples on a regular grid, which
    need not be uniform. The regular grid is specified by one-dimensional
    arrays of monotonically increasing coordinates x1, x2 and x3, such that
    gridded x1 are identical for all gridded x2 and x3, gridded x2 are
    identical for all gridded x1 and x2, and gridded x3 are identical for all
    gridded x1 and x2.
    
    Extrapolation (that is, interpolation outside the specified grid of
    (x1,x2,x3) coordinates), is performed using cubic polynomials for the
    nearest grid samples. Extrapolated values can be well outside the [min,max]
    range of interpolated values, and should typically be avoided.
    """

    @overload
    def __init__(self, x1: Float1D, x2: Float1D, x3: Float1D,
                 y: Float3D) -> None:
        """
        Constructs an interpolator for specified values y(x1,x2).
        
        Parameters
        -----------
        x1 : Float1D
            array[n1] of x1 coordinates; monotonically increasing.
        x2 : Float1D
            array[n2] of x2 coordinates; monotonically increasing.
        x3 : Float1D
            array[n3] of x3 coordinates; monotonically increasing.
        y : Float3D
            array[n3][n2][n1] of sampled values y(x1,x2,x3).
        """

    @overload
    def __init__(self, method1: Method, method2: Method, method3: Method,
                 x1: Float1D, x2: Float1D, x3: Float1D, y: Float3D) -> None:
        """
        Constructs an interpolator for specified methods and values.
        
        Parameters
        -----------
        method1 : Method
            method used to compute dy/d1.
        method2 : Method
            method used to compute dy/d2.
        method3 : Method
            method used to compute dy/d3.
        x1 : Float1D
            array[n1] of x1 coordinates; monotonically increasing.
        x2 : Float1D
            array[n2] of x2 coordinates; monotonically increasing.
        x3 : Float1D
            array[n3] of x3 coordinates; monotonically increasing.
        y : Float3D
            array[n3][n2][n1] of sampled values y(x1,x2,x3).
        """

    @overload
    def __init__(self, method1: Method, method2: Method, method3: Method,
                 n1: int, n2: int, n3: int, x1: Float1D, x2: Float1D,
                 x3: Float1D, y: Float3D) -> None:
        """
        Constructs an interpolator for specified methods and values.
        
        Parameters
        -----------
        method1 : Method
            method used to compute dy/d1.
        method2 : Method
            method used to compute dy/d2.
        method3 : Method
            method used to compute dy/d3.
        n1 : int
            number of x1 coordinates.
        n2 : int
            number of x2 coordinates.
        n3 : int
            number of x3 coordinates.
        x1 : Float1D
            array[n1] of x1 coordinates; monotonically increasing.
        x2 : Float1D
            array[n2] of x2 coordinates; monotonically increasing.
        x3 : Float1D
            array[n3] of x3 coordinates; monotonically increasing.
        y : Float3D
            array[n3][n2][n1] of sampled values y(x1,x2,x3).
        """

    @overload
    def interpolate(self, x1: float, x2: float, x3: float) -> float:
        """
        Returns interpolated value y.
        Same as {@link #interpolate000(float,float,float)}.
        
        Parameters
        -----------
        x1 : float
            coordinate x1.
        x2 : float
            coordinate x2.
        x3 : float
            coordinate x3.
        
        Returns
        --------
        output : float
            interpolated y(x1,x2,x3).
        """

    @overload
    def interpolate000(self, x1: float, x2: float, x3: float) -> float:
        """
        Returns interpolated value y.
        
        Parameters
        -----------
        x1 : float
            coordinate x1.
        x2 : float
            coordinate x2.
        x3 : float
            coordinate x3.
        
        Returns
        --------
        output : float
            interpolated y(x1,x2,x3).
        """

    def interpolate100(self, x1: float, x2: float, x3: float) -> float:
        """
        Returns interpolated partial derivative dy/d1.
        
        Parameters
        -----------
        x1 : float
            coordinate x1.
        x2 : float
            coordinate x2.
        x3 : float
            coordinate x3.
        
        Returns
        --------
        output : float
            interpolated dy/d1.
        """

    def interpolate010(self, x1: float, x2: float, x3: float) -> float:
        """
        Returns interpolated partial derivative dy/d2.
        
        Parameters
        -----------
        x1 : float
            coordinate x1.
        x2 : float
            coordinate x2.
        x3 : float
            coordinate x3.
        
        Returns
        --------
        output : float
            interpolated dy/d2.
        """

    def interpolate001(self, x1: float, x2: float, x3: float) -> float:
        """
        Returns interpolated partial derivative dy/d3.
        
        Parameters
        -----------
        x1 : float
            coordinate x1.
        x2 : float
            coordinate x2.
        x3 : float
            coordinate x3.
        
        Returns
        --------
        output : float
            interpolated dy/d3.
        """

    @overload
    def interpolate(self, s1: Sampling, s2: Sampling, s3: Sampling) -> Float3D:
        """
        Returns an array of interpolated values y.
        Same as {@link #interpolate000(Sampling,Sampling,Sampling)}.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of coordinate x1.
        s2 : Sampling
            sampling of coordinate x2.
        s3 : Sampling
            sampling of coordinate x3.
        
        Returns
        --------
        output : Float3D
            interpolated y(x1,x2,x3).
        """

    @overload
    def interpolate000(self, s1: Sampling, s2: Sampling,
                       s3: Sampling) -> Float3D:
        """
        Returns an array of interpolated values y.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of coordinate x1.
        s2 : Sampling
            sampling of coordinate x2.
        s3 : Sampling
            sampling of coordinate x3.
        
        Returns
        --------
        output : Float3D
            interpolated y(x1,x2,x3).
        """

    @overload
    def interpolate(self, s1: Sampling, s2: Sampling, s3: Sampling,
                    y: Float3D) -> None:
        """
        Computes an array of interpolated values y.
        Same as {@link #interpolate000(Sampling,Sampling,Sampling,float[][][])}.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of coordinate x1.
        s2 : Sampling
            sampling of coordinate x2.
        s3 : Sampling
            sampling of coordinate x3.
        y : Float3D
            output array of interpolated y(x1,x2,x3).
        """

    @overload
    def interpolate000(self, s1: Sampling, s2: Sampling, s3: Sampling,
                       y: Float3D) -> None:
        """
        Computes an array of interpolated values y.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of coordinate x1.
        s2 : Sampling
            sampling of coordinate x2.
        s3 : Sampling
            sampling of coordinate x3.
        y : Float3D
            output array of interpolated y(x1,x2,x3).
        """

    @overload
    def interpolate(self, x1: Float1D, x2: Float1D, x3: Float1D) -> Float3D:
        """
        Returns an array of interpolated values y.
        Same as {@link #interpolate000(float[],float[],float[])}.
        
        Parameters
        -----------
        x1 : Float1D
            array[n1] of coordinates x1.
        x2 : Float1D
            array[n2] of coordinates x2.
        x3 : Float1D
            array[n3] of coordinates x3.
        
        Returns
        --------
        output : Float3D
            array[n3][n2][n1] of interpolated y(x1,x2,x3).
        """

    @overload
    def interpolate000(self, x1: Float1D, x2: Float1D, x3: Float1D) -> Float3D:
        """
        Returns an array of interpolated values y.
        
        Parameters
        -----------
        x1 : Float1D
            array[n1] of coordinates x1.
        x2 : Float1D
            array[n2] of coordinates x2.
        x3 : Float1D
            array[n3] of coordinates x3.
        
        Returns
        --------
        output : Float3D
            array[n3][n2][n1] of interpolated y(x1,x2,x3).
        """

    @overload
    def interpolate(self, x1: Float1D, x2: Float1D, x3: Float1D,
                    y: Float3D) -> None:
        """
        Computes an array of interpolated values y.
        Same as {@link #interpolate000(float[],float[],float[],float[][][])}.
        
        Parameters
        -----------
        x1 : Float1D
            array[n1] of coordinates x1.
        x2 : Float1D
            array[n2] of coordinates x2.
        x3 : Float1D
            array[n3] of coordinates x3.
        y : Float3D
            output array[n3][n2][n1] of interpolated y(x1,x2,x3).
        """

    @overload
    def interpolate000(self, x1: Float1D, x2: Float1D, x3: Float1D,
                       y: Float3D) -> None:
        """
        Computes an array of interpolated values y.
        
        Parameters
        -----------
        x1 : Float1D
            array[n1] of coordinates x1.
        x2 : Float1D
            array[n2] of coordinates x2.
        x3 : Float1D
            array[n3] of coordinates x3.
        y : Float3D
            output array[n3][n2][n1] of interpolated y(x1,x2,x3).
        """
