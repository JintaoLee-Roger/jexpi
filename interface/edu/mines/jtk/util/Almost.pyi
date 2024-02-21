from typing import overload
from edu.mines.jtk.mapping import *


class Almost:
    """
    This class allows safe comparisons of floating point numbers
    with limited precision.
    The Comparator interface should be used for instances of
    java.lang.Number.
    """

    @overload
    def __init__(self) -> None:
        """
        Accept default precision, appropriate for arithmetic on floats.
        """

    @overload
    def __init__(self, epsilon: double, minValue: double) -> None:
        """
        Specify precision to be used for operations.
        before the number is considered different from 1.
        For double precision, use a multiple of MathPlus.DBL_EPSILON.
        For float precision use a multiple of MathPlus.FLT_EPSILON.
        I recommend multiplying these values by at least 10
        to allow for errors introduced by arithmetic.
        distinguished from zero. Use a multiple (say 100) of
        Double.MIN_VALUE or Float.MIN_VALUE.
        
        Parameters
        -----------
        epsilon : double
            The smallest positive number that can be added to 1
        minValue : double
            The smallest positive value that should be
        """

    @overload
    def __init__(self, epsilon: double) -> None:
        """
        Specify precision to be used for operations.
        MinValue defaults to 100.Float.MIN_VALUE;
        before the number is considered different from 1.
        For float precision use a multiple of 1.192092896e-07.
        For double precision, use a multiple of 2.2204460492503131e-016;
        I recommend multiplying these values by at least 10
        to allow for errors introduced by arithmetic.
        Should be much less than 1.
        
        Parameters
        -----------
        epsilon : double
            The smallest positive number that can be added to 1
        """

    @overload
    def __init__(self, significantDigits: int) -> None:
        """
        Specify precision to be used for operations.
        Epsilon will be 0.1 to this power.
        MinValue defaults to 100.Float.MIN_VALUE;
        positive.
        
        Parameters
        -----------
        significantDigits : int
            the number of significant digits, should be
        """

    @overload
    def __init__(self, isDouble: bool) -> None:
        """
        Constructor that allows either double or float precision.
        for a double; if false, a float.
        
        Parameters
        -----------
        isDouble : bool
            If true, the precision will be appropriate
        """

    def getEpsilon(self) -> double:
        """
        Get the smallest positive number that can be added to 1
        before the number is considered different from 1.
        Returns
        --------
        output : double
            epsilon
        """

    def getMinValue(self) -> double:
        """
        Get the smallest positive value that should be distinguished from
        zero.
        Returns
        --------
        output : double
            minValue
        """

    def between(self, x: double, x1: double, x2: double) -> bool:
        """
        See if value is between two other values, including almost equality
        
        Parameters
        -----------
        x : double
            Value to check
        x1 : double
            Value at one end of interval.
        x2 : double
            Value at other end of interval.
        
        Returns
        --------
        output : bool
            true if x is between x1 and x2.
        """

    def outside(self, x: double, x1: double, x2: double) -> int:
        """
        See if value is outside two other values.
        -1 if outside and closer to x1, 1 if outside and closer to x2.
        
        Parameters
        -----------
        x : double
            Value to check
        x1 : double
            Value at one end of interval.
        x2 : double
            Value at other end of interval.
        
        Returns
        --------
        output : int
            Return 0 if x is between x1 and x2,
        """

    def zero(self, r: double) -> bool:
        """
        See if the number is almost zero
        
        Parameters
        -----------
        r : double
            A number to check
        
        Returns
        --------
        output : bool
            true if the r is almost zero.
        """

    def equal(self, r1: double, r2: double) -> bool:
        """
        See if two numbers are almost equal.
        
        Parameters
        -----------
        r1 : double
            First number to check
        r2 : double
            Second number to check
        
        Returns
        --------
        output : bool
            True if r1 and r2 are almost equal
        """

    def lt(self, r1: double, r2: double) -> bool:
        """
        Check whether first number is strictly less than second.
        
        Parameters
        -----------
        r1 : double
            First number to check
        r2 : double
            Second number to check
        
        Returns
        --------
        output : bool
            true if r1&lt;r2
        """

    def le(self, r1: double, r2: double) -> bool:
        """
        Check whether first number is less than or equal to second.
        
        Parameters
        -----------
        r1 : double
            First number to check
        r2 : double
            Second number to check
        
        Returns
        --------
        output : bool
            true if r1&lt;=r2
        """

    def gt(self, r1: double, r2: double) -> bool:
        """
        Check whether first number is strictly greater than second.
        
        Parameters
        -----------
        r1 : double
            First number to check
        r2 : double
            Second number to check
        
        Returns
        --------
        output : bool
            true if r1&gt;r2
        """

    def ge(self, r1: double, r2: double) -> bool:
        """
        Check whether first number is greater than or equal to second.
        
        Parameters
        -----------
        r1 : double
            First number to check
        r2 : double
            Second number to check
        
        Returns
        --------
        output : bool
            true if r1&gt;=r2
        """

    def cmp(self, r1: double, r2: double) -> int:
        """
        Check order of two numbers, within precision.
        
        Parameters
        -----------
        r1 : double
            First number to check
        r2 : double
            Second number to check
        
        Returns
        --------
        output : int
            1 if r1 &gt; r2; -1 if r1 &lt; r2; 0 if r1==r2, within precision.
        """

    @overload
    def hashCodeOf(self, number: Number, significantDigits: int) -> int:
        """
        Return a hashcode consistent with imprecise floating-point equality.
        Integers and Longs require exact equality.
        
        Parameters
        -----------
        number : Number
            Number to get hashcode of
        significantDigits : int
            Number of significant digits to honor in hashCode
        
        Returns
        --------
        output : int
            new hash code.
        """

    @overload
    def hashCodeOf(self, number: Number) -> int:
        """
        Return a hashcode consistent with imprecise floating-point equality.
        Integers and Longs require exact equality.
        The precision is consistent with the value of epsilon.
        
        Parameters
        -----------
        number : Number
            number to get hashcode from
        
        Returns
        --------
        output : int
            hashcode
        """

    @overload
    def divide(self, top: double, bottom: double, limitIsOne: bool) -> double:
        """
        Safely divide one number by another.  Handle zeros and infinity.
        Never throws floating point exceptions.
        Return +/- 0.01Float.MAX_VALUE, rather than infinity.
        
        Parameters
        -----------
        top : double
            Numerator
        bottom : double
            Denominator
        limitIsOne : bool
            If true, 0/0 returns 1.  If false, 0/0 returns 0.
        
        Returns
        --------
        output : double
            Regular value if arguments are okay.
        """

    def reciprocal(self, value: double) -> double:
        """
        Safely take the reciprocal of a number.
        
        Parameters
        -----------
        value : double
            Value to take reciprocal of.
        
        Returns
        --------
        output : double
            reciprocal of value
        """

    @overload
    def divide(self, top: double, bottom: double, limit: double) -> double:
        """
        Safely divide one number by another.  Handle zeros and infinity.
        Never throws floating point exceptions.
        Return +/- 0.01Float.MAX_VALUE, rather than infinity.
        
        Parameters
        -----------
        top : double
            Numerator
        bottom : double
            Denominator
        limit : double
            This is the returned value for 0/0.
        
        Returns
        --------
        output : double
            Regular value if arguments are okay.
        """

    def compare(self, n1: Number, n2: Number) -> int:
        """
    
        """

    def equals(self, object: Object) -> bool:
        """
    
        """

    def hashCode(self) -> int:
        """
    
        """

    def toString(self) -> String:
        """
    
        """
