from typing import overload
from edu.mines.jtk.mapping import *


class Cdouble:
    """
    A complex number, with double-precision real and imaginary parts.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a complex number with zero real and imaginary parts.
        """

    @overload
    def __init__(self, r: double) -> None:
        """
        Constructs a complex number with zero imaginary part.
        
        Parameters
        -----------
        r : double
            the real part.
        """

    @overload
    def __init__(self, r: double, i: double) -> None:
        """
        Constructs a complex number.
        
        Parameters
        -----------
        r : double
            the real part.
        i : double
            the imaginary part.
        """

    @overload
    def __init__(self, x: Cdouble) -> None:
        """
        Constructs a copy of the specified complex number.
        
        Parameters
        -----------
        x : Cdouble
            the complex number.
        """

    @overload
    def plus(self, x: Cdouble) -> Cdouble:
        """
        Returns the sum z + x, where z is this complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            z + x.
        """

    @overload
    def minus(self, x: Cdouble) -> Cdouble:
        """
        Returns the difference z - x, where z is this complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            z - x.
        """

    @overload
    def times(self, x: Cdouble) -> Cdouble:
        """
        Returns the product z  x, where z is this complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            z  x.
        """

    @overload
    def over(self, x: Cdouble) -> Cdouble:
        """
        Returns the quotent z / x, where z is this complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            z / x.
        """

    @overload
    def plus(self, x: double) -> Cdouble:
        """
        Returns the sum z + x, where z is this complex number.
        
        Parameters
        -----------
        x : double
            a real number.
        
        Returns
        --------
        output : Cdouble
            z + x.
        """

    @overload
    def minus(self, x: double) -> Cdouble:
        """
        Returns the difference z - x, where z is this complex number.
        
        Parameters
        -----------
        x : double
            a real number.
        
        Returns
        --------
        output : Cdouble
            z - x.
        """

    @overload
    def times(self, x: double) -> Cdouble:
        """
        Returns the product z  x, where z is this complex number.
        
        Parameters
        -----------
        x : double
            a real number.
        
        Returns
        --------
        output : Cdouble
            z  x.
        """

    @overload
    def over(self, x: double) -> Cdouble:
        """
        Returns the quotent z / x, where z is this complex number.
        
        Parameters
        -----------
        x : double
            a real number.
        
        Returns
        --------
        output : Cdouble
            z / x.
        """

    @overload
    def plusEquals(self, x: Cdouble) -> Cdouble:
        """
        Returns the sum z += x, where z is this complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            z += x.
        """

    @overload
    def minusEquals(self, x: Cdouble) -> Cdouble:
        """
        Returns the difference z -= x, where z is this complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            z -= x.
        """

    @overload
    def timesEquals(self, x: Cdouble) -> Cdouble:
        """
        Returns the product z = x, where z is this complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            z = x.
        """

    @overload
    def overEquals(self, x: Cdouble) -> Cdouble:
        """
        Returns the quotient z /= x, where z is this complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            z /= x.
        """

    @overload
    def plusEquals(self, x: double) -> Cdouble:
        """
        Returns the sum z += x, where z is this complex number.
        
        Parameters
        -----------
        x : double
            a real number.
        
        Returns
        --------
        output : Cdouble
            z += x.
        """

    @overload
    def minusEquals(self, x: double) -> Cdouble:
        """
        Returns the difference z -= x, where z is this complex number.
        
        Parameters
        -----------
        x : double
            a real number.
        
        Returns
        --------
        output : Cdouble
            z -= x.
        """

    @overload
    def timesEquals(self, x: double) -> Cdouble:
        """
        Returns the product z = x, where z is this complex number.
        
        Parameters
        -----------
        x : double
            a real number.
        
        Returns
        --------
        output : Cdouble
            z = x.
        """

    @overload
    def overEquals(self, x: double) -> Cdouble:
        """
        Returns the quotient z /= x, where z is this complex number.
        
        Parameters
        -----------
        x : double
            a real number.
        
        Returns
        --------
        output : Cdouble
            z /= x.
        """

    def conjEquals(self) -> Cdouble:
        """
        Returns the conjugate z = conj(z), where z is this complex number.
        Returns
        --------
        output : Cdouble
            z = conj(z).
        """

    def invEquals(self) -> Cdouble:
        """
        Returns the inverse z = inv(z), where z is this complex number.
        Returns
        --------
        output : Cdouble
            z = inv(z).
        """

    def negEquals(self) -> Cdouble:
        """
        Returns the negative z = neg(z), where z is this complex number.
        Returns
        --------
        output : Cdouble
            z = neg(z).
        """

    @overload
    def isReal(self) -> bool:
        """
        Determines whether this complex number is real (has zero imaginary part).
        Returns
        --------
        output : bool
            true, if real; false, otherwise.
        """

    @overload
    def isImag(self) -> bool:
        """
        Determines whether this complex number is imaginary (has zero real part).
        Returns
        --------
        output : bool
            true, if imaginary; false, otherwise.
        """

    @overload
    def conj(self) -> Cdouble:
        """
        Returns the complex conjugate of this complex number.
        Returns
        --------
        output : Cdouble
            the complex conjugate.
        """

    @overload
    def inv(self) -> Cdouble:
        """
        Returns the complex inverse of this complex number.
        Returns
        --------
        output : Cdouble
            the complex inverse.
        """

    @overload
    def neg(self) -> Cdouble:
        """
        Returns the complex negative of this complex number.
        Returns
        --------
        output : Cdouble
            the complex negative.
        """

    @overload
    def abs(self) -> double:
        """
        Returns the magnitude of this complex number.
        Returns
        --------
        output : double
            the magnitude.
        """

    @overload
    def arg(self) -> double:
        """
        Returns the argument of this complex number.
        Returns
        --------
        output : double
            the argument.
        """

    @overload
    def norm(self) -> double:
        """
        Returns the norm of this complex number.
        The norm is the sum of the squares of the real and imaginary parts.
        Returns
        --------
        output : double
            the norm.
        """

    @overload
    def sqrt(self) -> Cdouble:
        """
        Returns the square-root of this complex number.
        Returns
        --------
        output : Cdouble
            the square-root.
        """

    @overload
    def exp(self) -> Cdouble:
        """
        Returns the exponential of this complex number.
        Returns
        --------
        output : Cdouble
            the exponential.
        """

    @overload
    def log(self) -> Cdouble:
        """
        Returns the natural logarithm of this complex number.
        Returns
        --------
        output : Cdouble
            the natural logarithm.
        """

    @overload
    def log10(self) -> Cdouble:
        """
        Returns the logarithm base 10 of this complex number.
        Returns
        --------
        output : Cdouble
            the logarithm base 10.
        """

    @overload
    def pow(self, y: double) -> Cdouble:
        """
        Returns z to the y'th power, where z is this complex number.
        
        Parameters
        -----------
        y : double
            a real number.
        
        Returns
        --------
        output : Cdouble
            z to the y'th power.
        """

    @overload
    def pow(self, y: Cdouble) -> Cdouble:
        """
        Returns z to the y'th power, where z is this complex number.
        
        Parameters
        -----------
        y : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            z to the y'th power.
        """

    @overload
    def sin(self) -> Cdouble:
        """
        Returns the sine of this complex number.
        Returns
        --------
        output : Cdouble
            the sine.
        """

    @overload
    def cos(self) -> Cdouble:
        """
        Returns the cosine of this complex number.
        Returns
        --------
        output : Cdouble
            the cosine.
        """

    @overload
    def tan(self) -> Cdouble:
        """
        Returns the tangent of this complex number.
        Returns
        --------
        output : Cdouble
            the tangent.
        """

    @overload
    def sinh(self) -> Cdouble:
        """
        Returns the hyberbolic sine of this complex number.
        Returns
        --------
        output : Cdouble
            the hyberbolic sine.
        """

    @overload
    def cosh(self) -> Cdouble:
        """
        Returns the hyberbolic cosine of this complex number.
        Returns
        --------
        output : Cdouble
            the hyberbolic cosine.
        """

    @overload
    def tanh(self) -> Cdouble:
        """
        Returns the hyberbolic tangent of this complex number.
        Returns
        --------
        output : Cdouble
            the hyberbolic tangent.
        """

    @overload
    @staticmethod
    def isReal(self, x: Cdouble) -> bool:
        """
        Determines whether x is real (has zero imaginary part).
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : bool
            true, if real; false, otherwise.
        """

    @overload
    @staticmethod
    def isImag(self, x: Cdouble) -> bool:
        """
        Determines whether x is imaginary (has zero real part).
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : bool
            true, if imaginary; false, otherwise.
        """

    @overload
    @staticmethod
    def conj(self, x: Cdouble) -> Cdouble:
        """
        Returns the conjugate of x.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the conjugate.
        """

    @overload
    @staticmethod
    def inv(self, x: Cdouble) -> Cdouble:
        """
        Returns the inverse of x.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the complex inverse.
        """

    @overload
    @staticmethod
    def neg(self, x: Cdouble) -> Cdouble:
        """
        Returns the negative of x.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the negative.
        """

    @staticmethod
    def polar(self, r: double, a: double) -> Cdouble:
        """
        Returns the complex number (rcos(a),rsin(a)).
        
        Parameters
        -----------
        r : double
            the polar radius.
        a : double
            the polar angle.
        
        Returns
        --------
        output : Cdouble
            the complex number.
        """

    @staticmethod
    def add(self, x: Cdouble, y: Cdouble) -> Cdouble:
        """
        Returns the sum x + y.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        y : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the sum.
        """

    @staticmethod
    def sub(self, x: Cdouble, y: Cdouble) -> Cdouble:
        """
        Returns the difference x - y.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        y : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the difference.
        """

    @staticmethod
    def mul(self, x: Cdouble, y: Cdouble) -> Cdouble:
        """
        Returns the product x  y.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        y : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the product.
        """

    @staticmethod
    def div(self, x: Cdouble, y: Cdouble) -> Cdouble:
        """
        Returns the quotient x  y.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        y : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the quotient.
        """

    @overload
    @staticmethod
    def abs(self, x: Cdouble) -> double:
        """
        Returns the magnitude of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : double
            the magnitude.
        """

    @overload
    @staticmethod
    def arg(self, x: Cdouble) -> double:
        """
        Returns the argument of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : double
            the argument.
        """

    @overload
    @staticmethod
    def norm(self, x: Cdouble) -> double:
        """
        Returns the norm of a complex number.
        The norm is the sum of the squares of the real and imaginary parts.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : double
            the norm.
        """

    @overload
    @staticmethod
    def sqrt(self, x: Cdouble) -> Cdouble:
        """
        Returns the square root of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the square root.
        """

    @overload
    @staticmethod
    def exp(self, x: Cdouble) -> Cdouble:
        """
        Returns the exponential of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the exponential.
        """

    @overload
    @staticmethod
    def log(self, x: Cdouble) -> Cdouble:
        """
        Returns the natural logarithm of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the natural logarithm.
        """

    @overload
    @staticmethod
    def log10(self, x: Cdouble) -> Cdouble:
        """
        Returns the logarithm base 10 of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the logarithm base 10.
        """

    @overload
    @staticmethod
    def pow(self, x: Cdouble, y: double) -> Cdouble:
        """
        Returns x to the y'th power.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        y : double
            a real number.
        
        Returns
        --------
        output : Cdouble
            x to the y'th power.
        """

    @overload
    @staticmethod
    def pow(self, x: double, y: Cdouble) -> Cdouble:
        """
        Returns x to the y'th power.
        
        Parameters
        -----------
        x : double
            a real number.
        y : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            x to the y'th power.
        """

    @overload
    @staticmethod
    def pow(self, x: Cdouble, y: Cdouble) -> Cdouble:
        """
        Returns x to the y'th power.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        y : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            x to the y'th power.
        """

    @overload
    @staticmethod
    def sin(self, x: Cdouble) -> Cdouble:
        """
        Returns the sine of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the sine.
        """

    @overload
    @staticmethod
    def cos(self, x: Cdouble) -> Cdouble:
        """
        Returns the cosine of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the cosine.
        """

    @overload
    @staticmethod
    def tan(self, x: Cdouble) -> Cdouble:
        """
        Returns the tangent of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the tangent.
        """

    @overload
    @staticmethod
    def sinh(self, x: Cdouble) -> Cdouble:
        """
        Returns the hyperbolic sine of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the hyperbolic sine.
        """

    @overload
    @staticmethod
    def cosh(self, x: Cdouble) -> Cdouble:
        """
        Returns the hyperbolic cosine of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the hyperbolic cosine.
        """

    @overload
    @staticmethod
    def tanh(self, x: Cdouble) -> Cdouble:
        """
        Returns the hyperbolic tangent of a complex number.
        
        Parameters
        -----------
        x : Cdouble
            a complex number.
        
        Returns
        --------
        output : Cdouble
            the hyperbolic tangent.
        """

    def equals(self, obj: Object) -> bool:
        """
    
        """

    def hashCode(self) -> int:
        """
    
        """

    def toString(self) -> String:
        """
    
        """
