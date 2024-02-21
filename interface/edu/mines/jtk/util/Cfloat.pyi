from typing import overload
from edu.mines.jtk.mapping import *


class Cfloat:
    """
    A complex number, with single-precision real and imaginary parts.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a complex number with zero real and imaginary parts.
        """

    @overload
    def __init__(self, r: float) -> None:
        """
        Constructs a complex number with zero imaginary part.
        
        Parameters
        -----------
        r : float
            the real part.
        """

    @overload
    def __init__(self, r: float, i: float) -> None:
        """
        Constructs a complex number.
        
        Parameters
        -----------
        r : float
            the real part.
        i : float
            the imaginary part.
        """

    @overload
    def __init__(self, x: Cfloat) -> None:
        """
        Constructs a copy of the specified complex number.
        
        Parameters
        -----------
        x : Cfloat
            the complex number.
        """

    @overload
    def plus(self, x: Cfloat) -> Cfloat:
        """
        Returns the sum z + x, where z is this complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            z + x.
        """

    @overload
    def minus(self, x: Cfloat) -> Cfloat:
        """
        Returns the difference z - x, where z is this complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            z - x.
        """

    @overload
    def times(self, x: Cfloat) -> Cfloat:
        """
        Returns the product z  x, where z is this complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            z  x.
        """

    @overload
    def over(self, x: Cfloat) -> Cfloat:
        """
        Returns the quotent z / x, where z is this complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            z / x.
        """

    @overload
    def plus(self, x: float) -> Cfloat:
        """
        Returns the sum z + x, where z is this complex number.
        
        Parameters
        -----------
        x : float
            a real number.
        
        Returns
        --------
        output : Cfloat
            z + x.
        """

    @overload
    def minus(self, x: float) -> Cfloat:
        """
        Returns the difference z - x, where z is this complex number.
        
        Parameters
        -----------
        x : float
            a real number.
        
        Returns
        --------
        output : Cfloat
            z - x.
        """

    @overload
    def times(self, x: float) -> Cfloat:
        """
        Returns the product z  x, where z is this complex number.
        
        Parameters
        -----------
        x : float
            a real number.
        
        Returns
        --------
        output : Cfloat
            z  x.
        """

    @overload
    def over(self, x: float) -> Cfloat:
        """
        Returns the quotent z / x, where z is this complex number.
        
        Parameters
        -----------
        x : float
            a real number.
        
        Returns
        --------
        output : Cfloat
            z / x.
        """

    @overload
    def plusEquals(self, x: Cfloat) -> Cfloat:
        """
        Returns the sum z += x, where z is this complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            z += x.
        """

    @overload
    def minusEquals(self, x: Cfloat) -> Cfloat:
        """
        Returns the difference z -= x, where z is this complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            z -= x.
        """

    @overload
    def timesEquals(self, x: Cfloat) -> Cfloat:
        """
        Returns the product z = x, where z is this complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            z = x.
        """

    @overload
    def overEquals(self, x: Cfloat) -> Cfloat:
        """
        Returns the quotient z /= x, where z is this complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            z /= x.
        """

    @overload
    def plusEquals(self, x: float) -> Cfloat:
        """
        Returns the sum z += x, where z is this complex number.
        
        Parameters
        -----------
        x : float
            a real number.
        
        Returns
        --------
        output : Cfloat
            z += x.
        """

    @overload
    def minusEquals(self, x: float) -> Cfloat:
        """
        Returns the difference z -= x, where z is this complex number.
        
        Parameters
        -----------
        x : float
            a real number.
        
        Returns
        --------
        output : Cfloat
            z -= x.
        """

    @overload
    def timesEquals(self, x: float) -> Cfloat:
        """
        Returns the product z = x, where z is this complex number.
        
        Parameters
        -----------
        x : float
            a real number.
        
        Returns
        --------
        output : Cfloat
            z = x.
        """

    @overload
    def overEquals(self, x: float) -> Cfloat:
        """
        Returns the quotient z /= x, where z is this complex number.
        
        Parameters
        -----------
        x : float
            a real number.
        
        Returns
        --------
        output : Cfloat
            z /= x.
        """

    def conjEquals(self) -> Cfloat:
        """
        Returns the conjugate z = conj(z), where z is this complex number.
        Returns
        --------
        output : Cfloat
            z = conj(z).
        """

    def invEquals(self) -> Cfloat:
        """
        Returns the inverse z = inv(z), where z is this complex number.
        Returns
        --------
        output : Cfloat
            z = inv(z).
        """

    def negEquals(self) -> Cfloat:
        """
        Returns the negative z = neg(z), where z is this complex number.
        Returns
        --------
        output : Cfloat
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
    def conj(self) -> Cfloat:
        """
        Returns the complex conjugate of this complex number.
        Returns
        --------
        output : Cfloat
            the complex conjugate.
        """

    @overload
    def inv(self) -> Cfloat:
        """
        Returns the complex inverse of this complex number.
        Returns
        --------
        output : Cfloat
            the complex inverse.
        """

    @overload
    def neg(self) -> Cfloat:
        """
        Returns the complex negative of this complex number.
        Returns
        --------
        output : Cfloat
            the complex negative.
        """

    @overload
    def abs(self) -> float:
        """
        Returns the magnitude of this complex number.
        Returns
        --------
        output : float
            the magnitude.
        """

    @overload
    def arg(self) -> float:
        """
        Returns the argument of this complex number.
        Returns
        --------
        output : float
            the argument.
        """

    @overload
    def norm(self) -> float:
        """
        Returns the norm of this complex number.
        The norm is the sum of the squares of the real and imaginary parts.
        Returns
        --------
        output : float
            the norm.
        """

    @overload
    def sqrt(self) -> Cfloat:
        """
        Returns the square-root of this complex number.
        Returns
        --------
        output : Cfloat
            the square-root.
        """

    @overload
    def exp(self) -> Cfloat:
        """
        Returns the exponential of this complex number.
        Returns
        --------
        output : Cfloat
            the exponential.
        """

    @overload
    def log(self) -> Cfloat:
        """
        Returns the natural logarithm of this complex number.
        Returns
        --------
        output : Cfloat
            the natural logarithm.
        """

    @overload
    def log10(self) -> Cfloat:
        """
        Returns the logarithm base 10 of this complex number.
        Returns
        --------
        output : Cfloat
            the logarithm base 10.
        """

    @overload
    def pow(self, y: float) -> Cfloat:
        """
        Returns z to the y'th power, where z is this complex number.
        
        Parameters
        -----------
        y : float
            a real number.
        
        Returns
        --------
        output : Cfloat
            z to the y'th power.
        """

    @overload
    def pow(self, y: Cfloat) -> Cfloat:
        """
        Returns z to the y'th power, where z is this complex number.
        
        Parameters
        -----------
        y : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            z to the y'th power.
        """

    @overload
    def sin(self) -> Cfloat:
        """
        Returns the sine of this complex number.
        Returns
        --------
        output : Cfloat
            the sine.
        """

    @overload
    def cos(self) -> Cfloat:
        """
        Returns the cosine of this complex number.
        Returns
        --------
        output : Cfloat
            the cosine.
        """

    @overload
    def tan(self) -> Cfloat:
        """
        Returns the tangent of this complex number.
        Returns
        --------
        output : Cfloat
            the tangent.
        """

    @overload
    def sinh(self) -> Cfloat:
        """
        Returns the hyberbolic sine of this complex number.
        Returns
        --------
        output : Cfloat
            the hyberbolic sine.
        """

    @overload
    def cosh(self) -> Cfloat:
        """
        Returns the hyberbolic cosine of this complex number.
        Returns
        --------
        output : Cfloat
            the hyberbolic cosine.
        """

    @overload
    def tanh(self) -> Cfloat:
        """
        Returns the hyberbolic tangent of this complex number.
        Returns
        --------
        output : Cfloat
            the hyberbolic tangent.
        """

    @overload
    @staticmethod
    def isReal(self, x: Cfloat) -> bool:
        """
        Determines whether x is real (has zero imaginary part).
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : bool
            true, if real; false, otherwise.
        """

    @overload
    @staticmethod
    def isImag(self, x: Cfloat) -> bool:
        """
        Determines whether x is imaginary (has zero real part).
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : bool
            true, if imaginary; false, otherwise.
        """

    @overload
    @staticmethod
    def conj(self, x: Cfloat) -> Cfloat:
        """
        Returns the conjugate of x.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the conjugate.
        """

    @overload
    @staticmethod
    def inv(self, x: Cfloat) -> Cfloat:
        """
        Returns the inverse of x.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the complex inverse.
        """

    @overload
    @staticmethod
    def neg(self, x: Cfloat) -> Cfloat:
        """
        Returns the negative of x.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the negative.
        """

    @staticmethod
    def polar(self, r: float, a: float) -> Cfloat:
        """
        Returns the complex number (rcos(a),rsin(a)).
        
        Parameters
        -----------
        r : float
            the polar radius.
        a : float
            the polar angle.
        
        Returns
        --------
        output : Cfloat
            the complex number.
        """

    @staticmethod
    def add(self, x: Cfloat, y: Cfloat) -> Cfloat:
        """
        Returns the sum x + y.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        y : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the sum.
        """

    @staticmethod
    def sub(self, x: Cfloat, y: Cfloat) -> Cfloat:
        """
        Returns the difference x - y.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        y : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the difference.
        """

    @staticmethod
    def mul(self, x: Cfloat, y: Cfloat) -> Cfloat:
        """
        Returns the product x  y.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        y : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the product.
        """

    @staticmethod
    def div(self, x: Cfloat, y: Cfloat) -> Cfloat:
        """
        Returns the quotient x  y.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        y : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the quotient.
        """

    @overload
    @staticmethod
    def abs(self, x: Cfloat) -> float:
        """
        Returns the magnitude of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : float
            the magnitude.
        """

    @overload
    @staticmethod
    def arg(self, x: Cfloat) -> float:
        """
        Returns the argument of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : float
            the argument.
        """

    @overload
    @staticmethod
    def norm(self, x: Cfloat) -> float:
        """
        Returns the norm of a complex number.
        The norm is the sum of the squares of the real and imaginary parts.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : float
            the norm.
        """

    @overload
    @staticmethod
    def sqrt(self, x: Cfloat) -> Cfloat:
        """
        Returns the square root of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the square root.
        """

    @overload
    @staticmethod
    def exp(self, x: Cfloat) -> Cfloat:
        """
        Returns the exponential of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the exponential.
        """

    @overload
    @staticmethod
    def log(self, x: Cfloat) -> Cfloat:
        """
        Returns the natural logarithm of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the natural logarithm.
        """

    @overload
    @staticmethod
    def log10(self, x: Cfloat) -> Cfloat:
        """
        Returns the logarithm base 10 of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the logarithm base 10.
        """

    @overload
    @staticmethod
    def pow(self, x: Cfloat, y: float) -> Cfloat:
        """
        Returns x to the y'th power.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        y : float
            a real number.
        
        Returns
        --------
        output : Cfloat
            x to the y'th power.
        """

    @overload
    @staticmethod
    def pow(self, x: float, y: Cfloat) -> Cfloat:
        """
        Returns x to the y'th power.
        
        Parameters
        -----------
        x : float
            a real number.
        y : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            x to the y'th power.
        """

    @overload
    @staticmethod
    def pow(self, x: Cfloat, y: Cfloat) -> Cfloat:
        """
        Returns x to the y'th power.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        y : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            x to the y'th power.
        """

    @overload
    @staticmethod
    def sin(self, x: Cfloat) -> Cfloat:
        """
        Returns the sine of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the sine.
        """

    @overload
    @staticmethod
    def cos(self, x: Cfloat) -> Cfloat:
        """
        Returns the cosine of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the cosine.
        """

    @overload
    @staticmethod
    def tan(self, x: Cfloat) -> Cfloat:
        """
        Returns the tangent of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the tangent.
        """

    @overload
    @staticmethod
    def sinh(self, x: Cfloat) -> Cfloat:
        """
        Returns the hyperbolic sine of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the hyperbolic sine.
        """

    @overload
    @staticmethod
    def cosh(self, x: Cfloat) -> Cfloat:
        """
        Returns the hyperbolic cosine of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
            the hyperbolic cosine.
        """

    @overload
    @staticmethod
    def tanh(self, x: Cfloat) -> Cfloat:
        """
        Returns the hyperbolic tangent of a complex number.
        
        Parameters
        -----------
        x : Cfloat
            a complex number.
        
        Returns
        --------
        output : Cfloat
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
