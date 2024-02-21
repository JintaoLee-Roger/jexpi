from typing import overload
from edu.mines.jtk.mapping import *


class MathPlus:
    """
    Basic math functions. Like the standard class {@link java.lang.Math}, but
    with overloaded methods that return floats when passed float arguments.
    (This eliminates ugly casts when using floats.) This class also defines
    useful additional constants, such as {@link #FLT_PI}.
    """

    @overload
    @staticmethod
    def sin(self, x: float) -> float:
        """
        Returns the trigonometric sine of an angle.
        
        Parameters
        -----------
        x : float
            the angle, in radians.
        
        Returns
        --------
        output : float
            the sine of the argument.
        """

    @overload
    @staticmethod
    def sin(self, x: double) -> double:
        """
        Returns the trigonometric sine of an angle.
        
        Parameters
        -----------
        x : double
            the angle, in radians.
        
        Returns
        --------
        output : double
            the sine of the argument.
        """

    @overload
    @staticmethod
    def cos(self, x: float) -> float:
        """
        Returns the trigonometric cosine of an angle.
        
        Parameters
        -----------
        x : float
            the angle, in radians.
        
        Returns
        --------
        output : float
            the cosine of the argument.
        """

    @overload
    @staticmethod
    def cos(self, x: double) -> double:
        """
        Returns the trigonometric cosine of an angle.
        
        Parameters
        -----------
        x : double
            the angle, in radians.
        
        Returns
        --------
        output : double
            the cosine of the argument.
        """

    @overload
    @staticmethod
    def tan(self, x: float) -> float:
        """
        Returns the trigonometric tangent of an angle.
        
        Parameters
        -----------
        x : float
            the angle, in radians.
        
        Returns
        --------
        output : float
            the tangent of the argument.
        """

    @overload
    @staticmethod
    def tan(self, x: double) -> double:
        """
        Returns the trigonometric tangent of an angle.
        
        Parameters
        -----------
        x : double
            the angle, in radians.
        
        Returns
        --------
        output : double
            the tangent of the argument.
        """

    @overload
    @staticmethod
    def asin(self, x: float) -> float:
        """
        Returns the arc sine of the specified value, in the range
        -<i>pi</i>/2 through <i>pi</i>/2.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the arc sine.
        """

    @overload
    @staticmethod
    def asin(self, x: double) -> double:
        """
        Returns the arc sine of the specified value, in the range
        -<i>pi</i>/2 through <i>pi</i>/2.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the arc sine.
        """

    @overload
    @staticmethod
    def acos(self, x: float) -> float:
        """
        Returns the arc cosine of the specified value, in the range
        0.0 through <i>pi</i>.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the arc cosine.
        """

    @overload
    @staticmethod
    def acos(self, x: double) -> double:
        """
        Returns the arc cosine of the specified value, in the range
        0.0 through <i>pi</i>.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the arc cosine.
        """

    @overload
    @staticmethod
    def atan(self, x: float) -> float:
        """
        Returns the arc tangent of the specified value, in the range
        -<i>pi</i>/2 through <i>pi</i>/2.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the arc tangent.
        """

    @overload
    @staticmethod
    def atan(self, x: double) -> double:
        """
        Returns the arc tangent of the specified value, in the range
        -<i>pi</i>/2 through <i>pi</i>/2.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the arc tangent.
        """

    @overload
    @staticmethod
    def atan2(self, y: float, x: float) -> float:
        """
        Computes the arc tangent of the specified y/x, in the range
        -<i>pi</i> to <i>pi</i>.
        
        Parameters
        -----------
        y : float
            the ordinate coordinate y.
        x : float
            the abscissa coordinate x.
        
        Returns
        --------
        output : float
            the arc tangent.
        """

    @overload
    @staticmethod
    def atan2(self, y: double, x: double) -> double:
        """
        Computes the arc tangent of the specified y/x, in the range
        -<i>pi</i> to <i>pi</i>.
        
        Parameters
        -----------
        y : double
            the ordinate coordinate y.
        x : double
            the abscissa coordinate x.
        
        Returns
        --------
        output : double
            the arc tangent.
        """

    @overload
    @staticmethod
    def toRadians(self, angdeg: float) -> float:
        """
        Converts an angle measured in degrees to radians.
        
        Parameters
        -----------
        angdeg : float
            an angle, in degrees.
        
        Returns
        --------
        output : float
            the angle in radians.
        """

    @overload
    @staticmethod
    def toRadians(self, angdeg: double) -> double:
        """
        Converts an angle measured in degrees to radians.
        
        Parameters
        -----------
        angdeg : double
            an angle, in degrees.
        
        Returns
        --------
        output : double
            the angle in radians.
        """

    @overload
    @staticmethod
    def toDegrees(self, angrad: float) -> float:
        """
        Converts an angle measured in radians to degrees.
        
        Parameters
        -----------
        angrad : float
            an angle, in radians.
        
        Returns
        --------
        output : float
            the angle in degrees.
        """

    @overload
    @staticmethod
    def toDegrees(self, angrad: double) -> double:
        """
        Converts an angle measured in radians to degrees.
        
        Parameters
        -----------
        angrad : double
            an angle, in radians.
        
        Returns
        --------
        output : double
            the angle in degrees.
        """

    @overload
    @staticmethod
    def exp(self, x: float) -> float:
        """
        Returns the value of <i>e</i> raised to the specified power.
        
        Parameters
        -----------
        x : float
            the exponent.
        
        Returns
        --------
        output : float
            the value.
        """

    @overload
    @staticmethod
    def exp(self, x: double) -> double:
        """
        Returns the value of <i>e</i> raised to the specified power.
        
        Parameters
        -----------
        x : double
            the exponent.
        
        Returns
        --------
        output : double
            the value.
        """

    @overload
    @staticmethod
    def log(self, x: float) -> float:
        """
        Returns the natural logarithm (base <i>e</i>) of the specified value.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the natural logarithm.
        """

    @overload
    @staticmethod
    def log(self, x: double) -> double:
        """
        Returns the natural logarithm (base <i>e</i>) of the specified value.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the natural logarithm.
        """

    @overload
    @staticmethod
    def log10(self, x: float) -> float:
        """
        Returns the logarithm base 10 of the specified value.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the logarithm base 10.
        """

    @overload
    @staticmethod
    def log10(self, x: double) -> double:
        """
        Returns the logarithm base 10 of the specified value.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the logarithm base 10.
        """

    @overload
    @staticmethod
    def sqrt(self, x: float) -> float:
        """
        Returns the positive square root of a the specified value.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the positive square root.
        """

    @overload
    @staticmethod
    def sqrt(self, x: double) -> double:
        """
        Returns the positive square root of a the specified value.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the positive square root.
        """

    @overload
    @staticmethod
    def pow(self, x: float, y: float) -> float:
        """
        Returns the value of x raised to the y'th power.
        
        Parameters
        -----------
        x : float
            the base.
        y : float
            the exponent.
        
        Returns
        --------
        output : float
            the value.
        """

    @overload
    @staticmethod
    def pow(self, x: double, y: double) -> double:
        """
        Returns the value of x raised to the y'th power.
        
        Parameters
        -----------
        x : double
            the base.
        y : double
            the exponent.
        
        Returns
        --------
        output : double
            the value.
        """

    @overload
    @staticmethod
    def sinh(self, x: float) -> float:
        """
        Returns the hyperbolic sine of the specified value.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the hyperbolic sine.
        """

    @overload
    @staticmethod
    def sinh(self, x: double) -> double:
        """
        Returns the hyperbolic sine of the specified value.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the hyperbolic sine.
        """

    @overload
    @staticmethod
    def cosh(self, x: float) -> float:
        """
        Returns the hyperbolic cosine of the specified value.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the hyperbolic cosine.
        """

    @overload
    @staticmethod
    def cosh(self, x: double) -> double:
        """
        Returns the hyperbolic cosine of the specified value.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the hyperbolic cosine.
        """

    @overload
    @staticmethod
    def tanh(self, x: float) -> float:
        """
        Returns the hyperbolic tangent of the specified value.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the hyperbolic tangent.
        """

    @overload
    @staticmethod
    def tanh(self, x: double) -> double:
        """
        Returns the hyperbolic tangent of the specified value.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the hyperbolic tangent.
        """

    @overload
    @staticmethod
    def ceil(self, x: float) -> float:
        """
        Returns the smallest (closest to negative infinity) value that is greater
        than or equal to the argument and is equal to a mathematical integer.
        
        Parameters
        -----------
        x : float
            a value.
        
        Returns
        --------
        output : float
            the smallest value.
        """

    @overload
    @staticmethod
    def ceil(self, x: double) -> double:
        """
        Returns the smallest (closest to negative infinity) value that is greater
        than or equal to the argument and is equal to a mathematical integer.
        
        Parameters
        -----------
        x : double
            a value.
        
        Returns
        --------
        output : double
            the smallest value.
        """

    @overload
    @staticmethod
    def floor(self, x: float) -> float:
        """
        Returns the largest (closest to positive infinity) value that is less
        than or equal to the argument and is equal to a mathematical integer.
        
        Parameters
        -----------
        x : float
            a value.
        
        Returns
        --------
        output : float
            the largest value.
        """

    @overload
    @staticmethod
    def floor(self, x: double) -> double:
        """
        Returns the largest (closest to positive infinity) value that is less
        than or equal to the argument and is equal to a mathematical integer.
        
        Parameters
        -----------
        x : double
            a value.
        
        Returns
        --------
        output : double
            the largest value.
        """

    @overload
    @staticmethod
    def rint(self, x: float) -> float:
        """
        Returns the value that is closest to the specified value and is equal
        to a mathematical integer.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the closest value.
        """

    @overload
    @staticmethod
    def rint(self, x: double) -> double:
        """
        Returns the value that is closest to the specified value and is equal
        to a mathematical integer.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the closest value.
        """

    @overload
    @staticmethod
    def round(self, x: float) -> int:
        """
        Returns the closest int to the specified value. The result is the
        value of the expression <code>(int)Math.floor(a+0.5f)</code>.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : int
            the value rounded to the nearest int.
        """

    @overload
    @staticmethod
    def round(self, x: double) -> long:
        """
        Returns the closest long to the specified value. The result is the
        value of the expression <code>(long)Math.floor(a+0.5)</code>.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : long
            the value rounded to the nearest long.
        """

    @overload
    @staticmethod
    def signum(self, x: float) -> float:
        """
        Returns the signum of the specified value. The signum is zero if the
        argument is zero, 1.0 if the argument is greater than zero, -1.0 if
        the argument is less than zero.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the signum.
        """

    @overload
    @staticmethod
    def signum(self, x: double) -> double:
        """
        Returns the signum of the specified value. The signum is zero if the
        argument is zero, 1.0 if the argument is greater than zero, -1.0 if
        the argument is less than zero.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the signum.
        """

    @overload
    @staticmethod
    def abs(self, x: int) -> int:
        """
        Returns the absolute value of the specified value.
        
        Parameters
        -----------
        x : int
            the value.
        
        Returns
        --------
        output : int
            the absolute value.
        """

    @overload
    @staticmethod
    def abs(self, x: long) -> long:
        """
        Returns the absolute value of the specified value.
        
        Parameters
        -----------
        x : long
            the value.
        
        Returns
        --------
        output : long
            the absolute value.
        """

    @overload
    @staticmethod
    def abs(self, x: float) -> float:
        """
        Returns the absolute value of the specified value.
        If this is a problem, use {@code Math.abs}.
        
        Parameters
        -----------
        x : float
            the value.
        
        Returns
        --------
        output : float
            the absolute value.
        """

    @overload
    @staticmethod
    def abs(self, x: double) -> double:
        """
        Returns the absolute value of the specified value.
        If this is a problem, use {@code Math.abs}.
        
        Parameters
        -----------
        x : double
            the value.
        
        Returns
        --------
        output : double
            the absolute value.
        """

    @overload
    @staticmethod
    def max(self, a: int, b: int) -> int:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : int
            a value.
        b : int
            a value.
        
        Returns
        --------
        output : int
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: int, b: int, c: int) -> int:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : int
            a value.
        b : int
            a value.
        c : int
            a value.
        
        Returns
        --------
        output : int
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: int, b: int, c: int, d: int) -> int:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : int
            a value.
        b : int
            a value.
        c : int
            a value.
        d : int
            a value.
        
        Returns
        --------
        output : int
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: long, b: long) -> long:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : long
            a value.
        b : long
            a value.
        
        Returns
        --------
        output : long
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: long, b: long, c: long) -> long:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : long
            a value.
        b : long
            a value.
        c : long
            a value.
        
        Returns
        --------
        output : long
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: long, b: long, c: long, d: long) -> long:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : long
            a value.
        b : long
            a value.
        c : long
            a value.
        d : long
            a value.
        
        Returns
        --------
        output : long
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: float, b: float) -> float:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : float
            a value.
        b : float
            a value.
        
        Returns
        --------
        output : float
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: float, b: float, c: float) -> float:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : float
            a value.
        b : float
            a value.
        c : float
            a value.
        
        Returns
        --------
        output : float
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: float, b: float, c: float, d: float) -> float:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : float
            a value.
        b : float
            a value.
        c : float
            a value.
        d : float
            a value.
        
        Returns
        --------
        output : float
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: double, b: double) -> double:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : double
            a value.
        b : double
            a value.
        
        Returns
        --------
        output : double
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: double, b: double, c: double) -> double:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : double
            a value.
        b : double
            a value.
        c : double
            a value.
        
        Returns
        --------
        output : double
            the maximum value.
        """

    @overload
    @staticmethod
    def max(self, a: double, b: double, c: double, d: double) -> double:
        """
        Returns the maximum of the specified values.
        
        Parameters
        -----------
        a : double
            a value.
        b : double
            a value.
        c : double
            a value.
        d : double
            a value.
        
        Returns
        --------
        output : double
            the maximum value.
        """

    @overload
    @staticmethod
    def min(self, a: int, b: int) -> int:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : int
            a value.
        b : int
            a value.
        
        Returns
        --------
        output : int
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: int, b: int, c: int) -> int:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : int
            a value.
        b : int
            a value.
        c : int
            a value.
        
        Returns
        --------
        output : int
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: int, b: int, c: int, d: int) -> int:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : int
            a value.
        b : int
            a value.
        c : int
            a value.
        d : int
            a value.
        
        Returns
        --------
        output : int
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: long, b: long) -> long:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : long
            a value.
        b : long
            a value.
        
        Returns
        --------
        output : long
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: long, b: long, c: long) -> long:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : long
            a value.
        b : long
            a value.
        c : long
            a value.
        
        Returns
        --------
        output : long
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: long, b: long, c: long, d: long) -> long:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : long
            a value.
        b : long
            a value.
        c : long
            a value.
        d : long
            a value.
        
        Returns
        --------
        output : long
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: float, b: float) -> float:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : float
            a value.
        b : float
            a value.
        
        Returns
        --------
        output : float
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: float, b: float, c: float) -> float:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : float
            a value.
        b : float
            a value.
        c : float
            a value.
        
        Returns
        --------
        output : float
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: float, b: float, c: float, d: float) -> float:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : float
            a value.
        b : float
            a value.
        c : float
            a value.
        d : float
            a value.
        
        Returns
        --------
        output : float
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: double, b: double) -> double:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : double
            a value.
        b : double
            a value.
        
        Returns
        --------
        output : double
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: double, b: double, c: double) -> double:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : double
            a value.
        b : double
            a value.
        c : double
            a value.
        
        Returns
        --------
        output : double
            the minimum value.
        """

    @overload
    @staticmethod
    def min(self, a: double, b: double, c: double, d: double) -> double:
        """
        Returns the minimum of the specified values.
        
        Parameters
        -----------
        a : double
            a value.
        b : double
            a value.
        c : double
            a value.
        d : double
            a value.
        
        Returns
        --------
        output : double
            the minimum value.
        """
