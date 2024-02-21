from typing import overload
from edu.mines.jtk.mapping import *


class CubicInterpolator:
    """
    Piecewise cubic interpolation of a function y(x).
    
    Piecewise cubic interpolators differ in the method they use to compute
    slopes y'(x) at specified x (knots). The classic cubic spline computes the
    slopes to obtain a continuous second derivative at the knots. These splines
    often yield unacceptable wiggliness (overshoot) between the knots. A linear
    spline yields no overshoot, but has discontinuous first (and higher)
    derivatives. A monotonic spline has continuous first derivatives and yields
    monotonic interpolation (with no overshoot) where function values at the
    knots are monotonically increasing or decreasing.
    
    For x outside the range of values specified when an interpolator was
    constructed, the interpolator <em>extrapolates</em> using the cubic
    polynomial corresponding to the knot nearest to x.
    """

    @overload
    def __init__(self, x: Float1D, y: Float1D, y1: Float1D) -> None:
        """
        Constructs an interpolator with specified 1st derivatives y'(x).
        These values must be monotonically increasing or decreasing,
        with no equal values. (In other words, the array must be
        monotonic-definite.)
        
        Parameters
        -----------
        x : Float1D
            array of values at which y(x) are specified.
        y : Float1D
            array of function values y(x).
        y1 : Float1D
            array of 1st derivatives y'(x).
        """

    @overload
    def __init__(self, x: Float1D, y: Float1D) -> None:
        """
        Constructs an interpolator with default method monotonic.
        These values must be monotonically increasing or decreasing,
        with no equal values. (In other words, the array must be
        monotonic-definite.)
        
        Parameters
        -----------
        x : Float1D
            array of values at which y(x) are specified.
        y : Float1D
            array of function values y(x).
        """

    @overload
    def __init__(self, method: Method, x: Float1D, y: Float1D) -> None:
        """
        Constructs an interpolator.
        These values must be monotonically increasing or decreasing,
        with no equal values. (In other words, the array must be
        monotonic-definite.)
        
        Parameters
        -----------
        method : Method
            interpolation method: LINEAR, MONOTONIC, or SPLINE.
        x : Float1D
            array of values at which y(x) are specified.
        y : Float1D
            array of function values y(x).
        """

    @overload
    def __init__(self, method: Method, n: int, x: Float1D, y: Float1D) -> None:
        """
        Constructs an interpolator.
        These values must be monotonically increasing or decreasing,
        with no equal values. (In other words, the array must be
        monotonic-definite.)
        
        Parameters
        -----------
        method : Method
            interpolation method: LINEAR, MONOTONIC, or SPLINE.
        n : int
            number of x and y(x) values specified.
        x : Float1D
            array[n] of values at which y(x) are specified.
        y : Float1D
            array[n] of function values y(x).
        """

    @overload
    def interpolate(self, x: float) -> float:
        """
        Interpolates a function value y(x).
        Same as {@link #interpolate0(float)}.
        
        Parameters
        -----------
        x : float
            value at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated function value y(x).
        """

    @overload
    def interpolate0(self, x: float) -> float:
        """
        Interpolates a function value y(x).
        
        Parameters
        -----------
        x : float
            value at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated function value y(x).
        """

    @overload
    def interpolate1(self, x: float) -> float:
        """
        Interpolates the first derivative y'(x).
        
        Parameters
        -----------
        x : float
            value at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated first derivative y'(x).
        """

    @overload
    def interpolate2(self, x: float) -> float:
        """
        Interpolates the second derivative y''(x).
        
        Parameters
        -----------
        x : float
            value at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated second derivative y''(x).
        """

    @overload
    def interpolate3(self, x: float) -> float:
        """
        Interpolates the third derivative y'''(x).
        
        Parameters
        -----------
        x : float
            value at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated third derivative y'''(x).
        """

    @overload
    def interpolate(self, x: Float1D) -> Float1D:
        """
        Returns an array of interpolated function values y(x).
        Same as {@link #interpolate0(float[])}.
        
        Parameters
        -----------
        x : Float1D
            array of values at which to interpolate.
        
        Returns
        --------
        output : Float1D
            array of interpolated function values.
        """

    @overload
    def interpolate0(self, x: Float1D) -> Float1D:
        """
        Returns an array of interpolated function values y(x).
        
        Parameters
        -----------
        x : Float1D
            array of values at which to interpolate.
        
        Returns
        --------
        output : Float1D
            array of interpolated function values.
        """

    @overload
    def interpolate(self, x: Float1D, y: Float1D) -> None:
        """
        Interpolates an array of function values y(x).
        Same as {@link #interpolate0(float[],float[])}.
        
        Parameters
        -----------
        x : Float1D
            array of values at which to interpolate.
        y : Float1D
            array of interpolated function values.
        """

    @overload
    def interpolate0(self, x: Float1D, y: Float1D) -> None:
        """
        Interpolates an array of function values y(x).
        
        Parameters
        -----------
        x : Float1D
            array of values at which to interpolate.
        y : Float1D
            array of interpolated function values.
        """

    @overload
    def interpolate1(self, x: Float1D) -> Float1D:
        """
        Returns an array of interpolated first derivatives y'(x).
        
        Parameters
        -----------
        x : Float1D
            array of values at which to interpolate.
        
        Returns
        --------
        output : Float1D
            array of interpolated first derivatives y'(x).
        """

    @overload
    def interpolate1(self, x: Float1D, y: Float1D) -> None:
        """
        Interpolates an array of first derivatives y'(x).
        
        Parameters
        -----------
        x : Float1D
            array of values at which to interpolate.
        y : Float1D
            array of interpolated first derivatives y'(x).
        """

    @overload
    def interpolate2(self, x: Float1D) -> Float1D:
        """
        Returns an array of interpolated second derivatives y''(x).
        
        Parameters
        -----------
        x : Float1D
            array of values at which to interpolate.
        
        Returns
        --------
        output : Float1D
            array of interpolated second derivatives y''(x).
        """

    @overload
    def interpolate2(self, x: Float1D, y: Float1D) -> None:
        """
        Interpolates an array of second derivatives y''(x).
        
        Parameters
        -----------
        x : Float1D
            array of values at which to interpolate.
        y : Float1D
            array of interpolated second derivatives y''(x).
        """

    @overload
    def interpolate3(self, x: Float1D) -> Float1D:
        """
        Returns an array of interpolated third derivatives y'''(x).
        
        Parameters
        -----------
        x : Float1D
            array of values at which to interpolate.
        
        Returns
        --------
        output : Float1D
            array of interpolated third derivatives y'''(x).
        """

    @overload
    def interpolate3(self, x: Float1D, y: Float1D) -> None:
        """
        Interpolates an array of third derivatives y'''(x).
        
        Parameters
        -----------
        x : Float1D
            array of values at which to interpolate.
        y : Float1D
            array of interpolated third derivatives y'''(x).
        """

    @overload
    def interpolate(self, n: int, x: Float1D, y: Float1D) -> None:
        """
        Interpolates an array of function values y(x).
        Same as {@link #interpolate0(int,float[],float[])}.
        
        Parameters
        -----------
        n : int
            number of values to interpolate.
        x : Float1D
            array of values at which to interpolate.
        y : Float1D
            array of interpolated function values.
        """

    @overload
    def interpolate0(self, n: int, x: Float1D, y: Float1D) -> None:
        """
        Interpolates an array of function values y(x).
        
        Parameters
        -----------
        n : int
            number of values to interpolate.
        x : Float1D
            array of values at which to interpolate.
        y : Float1D
            array of interpolated function values.
        """

    @overload
    def interpolate1(self, n: int, x: Float1D, y: Float1D) -> None:
        """
        Interpolates an array of first derivatives y'(x).
        
        Parameters
        -----------
        n : int
            number of derivatives to interpolate.
        x : Float1D
            array of values at which to interpolate.
        y : Float1D
            array of interpolated first derivatives y'(x).
        """

    @overload
    def interpolate2(self, n: int, x: Float1D, y: Float1D) -> None:
        """
        Interpolates an array of second derivatives y''(x).
        
        Parameters
        -----------
        n : int
            number of derivatives to interpolate.
        x : Float1D
            array of values at which to interpolate.
        y : Float1D
            array of interpolated second derivatives y''(x).
        """

    @overload
    def interpolate3(self, n: int, x: Float1D, y: Float1D) -> None:
        """
        Interpolates an array of third derivatives y'''(x).
        
        Parameters
        -----------
        n : int
            number of derivatives to interpolate.
        x : Float1D
            array of values at which to interpolate.
        y : Float1D
            array of interpolated third derivatives y'''(x).
        """
