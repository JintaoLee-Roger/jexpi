"""
Utilities for arrays plus math methods for floats and doubles.

The math methods mirror those in the standard {@link java.lang.Math}, 
but include overloaded methods that return floats when passed float
arguments. This eliminates tedious and ugly casts when using floats.

This class also provides utility functions for working with arrays of 
primitive types, including arrays of real numbers (floats and doubles)
and complex numbers (pairs of floats and doubles). Many of the array
methods (e.g., sqrt) overload scalar math methods.

Here is an example of using this class:
<pre><code>
import static edu.mines.jtk.util.ArrayMath.*;
...
float[] x = randfloat(10); // an array of 10 random floats
System.out.println("x="); dump(x); // print x
float[] y = sqrt(x); // an array of square roots of those floats
System.out.println("y="); dump(y); // print y
float z = sqrt(x[0]); // no (float) cast required
System.out.println("z="); // print z
...
</code></pre>

A real array rx is an array of numeric values, in which each value 
represents one real number. A complex array is an array of float or
double values, in which each consecutive pair of values represents the 
real and imaginary parts of one complex number. This means that a 
complex array cx contains cx.length/2 complex numbers, and cx.length is 
an even number. For example, the length of a 1-D complex array cx with 
dimension n1 is cx.length = 2*n1; i.e., n1 is the number of complex 
elements in the array.

Methods are overloaded for 1-D arrays, 2-D arrays (arrays of arrays), 
and 3-D arrays (arrays of arrays of arrays). Multi-dimensional arrays 
can be regular or ragged. For example, the dimensions of a regular 3-D 
array float[n3][n2][n1] are n1, n2, and n3, where n1 is the fastest
dimension, and n3 is the slowest dimension. In contrast, the lengths 
of arrays within a ragged array of arrays (of arrays) may vary.

Some methods that create new arrays (e.g., zero, fill, ramp, and 
rand) have no array arguments; these methods have arguments that 
specify regular array dimensions n1, n2, and/or n3. All other methods, 
those with at least one array argument, use the dimensions of the first 
array argument to determine the number of array elements to process.

Some methods may have arguments that are arrays of real and/or complex 
numbers. In such cases, arguments with names like rx, ry, and rz denote 
arrays of real (non-complex) elements. Arguments with names like ra and 
rb denote real values. Arguments with names like cx, cy, and cz denote 
arrays of complex elements, and arguments with names like ca and cb 
denote complex values. 

Because complex numbers are packed into arrays of the same types (float
or double) as real arrays, method overloading cannot distinguish methods 
with real array arguments from those with complex array arguments.
Therefore, all methods with at least one complex array argument are
prefixed with the letter 'c'. For example, methods mul that multiply 
two arrays of real numbers have corresponding methods cmul that multiply 
two arrays of complex numbers.
<pre>
Creation and copy operations:
zero - fills an array with a constant value zero
fill - fills an array with a specified constant value
ramp - fills an array with a linear values ra + rb1*i1 (+ rb2*i2 + rb3*i3)
rand - fills an array with pseudo-random numbers
copy - copies an array, or a specified subset of an array
</pre><pre>
Binary operations:
add - adds one array (or value) to another array (or value)
sub - subtracts one array (or value) from another array (or value)
mul - multiplies one array (or value) by another array (or value)
div - divides one array (or value) by another array (or value)
</pre><pre>
Unary operations:
abs - absolute value
neg - negation
cos - cosine
sin - sine
sqrt - square-root
exp - exponential
log - natural logarithm
log10 - logarithm base 10
clip - clip values to be within specified min/max bounds
pow - raise to a specified power
sgn - sign (1 if positive, -1 if negative, 0 if zero)
</pre><pre>
Other operations:
equal - compares arrays for equality (to within an optional tolerance)
sum - returns the sum of array values
max - returns the maximum value in an array and (optionally) its indices
min - returns the minimum value in an array and (optionally) its indices
dump - prints an array to standard output
</pre>
Many more utility methods are included as well, for sorting, searching, 
etc.
@see java.lang.Math
@author Dave Hale and Chris Engelsma, Colorado School of Mines
@version 2017.05.31
"""


from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.util import *

@overload
def sin(x: float) -> float:
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
def sin(x: double) -> double:
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
def cos(x: float) -> float:
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
def cos(x: double) -> double:
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
def tan(x: float) -> float:
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
def tan(x: double) -> double:
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
def asin(x: float) -> float:
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
def asin(x: double) -> double:
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
def acos(x: float) -> float:
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
def acos(x: double) -> double:
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
def atan(x: float) -> float:
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
def atan(x: double) -> double:
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
def atan2(y: float, x: float) -> float:
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
def atan2(y: double, x: double) -> double:
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
def toRadians(angdeg: float) -> float:
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
def toRadians(angdeg: double) -> double:
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
def toDegrees(angrad: float) -> float:
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
def toDegrees(angrad: double) -> double:
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
def exp(x: float) -> float:
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
def exp(x: double) -> double:
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
def log(x: float) -> float:
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
def log(x: double) -> double:
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
def log10(x: float) -> float:
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
def log10(x: double) -> double:
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
def sqrt(x: float) -> float:
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
def sqrt(x: double) -> double:
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
def pow(x: float, y: float) -> float:
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
def pow(x: double, y: double) -> double:
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
def sinh(x: float) -> float:
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
def sinh(x: double) -> double:
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
def cosh(x: float) -> float:
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
def cosh(x: double) -> double:
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
def tanh(x: float) -> float:
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
def tanh(x: double) -> double:
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
def ceil(x: float) -> float:
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
def ceil(x: double) -> double:
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
def floor(x: float) -> float:
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
def floor(x: double) -> double:
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
def rint(x: float) -> float:
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
def rint(x: double) -> double:
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
def round(x: float) -> int:
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
def round(x: double) -> long:
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
def signum(x: float) -> float:
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
def signum(x: double) -> double:
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
def abs(x: int) -> int:
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
def abs(x: long) -> long:
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
def abs(x: float) -> float:
    """
    Returns the absolute value of the specified value.
    Note that {@code abs(-0.0f)} returns {@code -0.0f};
    the sign bit is not cleared.
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
def abs(x: double) -> double:
    """
    Returns the absolute value of the specified value.
    Note that {@code abs(-0.0d)} returns {@code -0.0d};
    the sign bit is not cleared.
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
def max(a: int, b: int) -> int:
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
def max(a: int, b: int, c: int) -> int:
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
def max(a: int, b: int, c: int, d: int) -> int:
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
def max(a: long, b: long) -> long:
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
def max(a: long, b: long, c: long) -> long:
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
def max(a: long, b: long, c: long, d: long) -> long:
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
def max(a: float, b: float) -> float:
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
def max(a: float, b: float, c: float) -> float:
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
def max(a: float, b: float, c: float, d: float) -> float:
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
def max(a: double, b: double) -> double:
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
def max(a: double, b: double, c: double) -> double:
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
def max(a: double, b: double, c: double, d: double) -> double:
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
def min(a: int, b: int) -> int:
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
def min(a: int, b: int, c: int) -> int:
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
def min(a: int, b: int, c: int, d: int) -> int:
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
def min(a: long, b: long) -> long:
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
def min(a: long, b: long, c: long) -> long:
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
def min(a: long, b: long, c: long, d: long) -> long:
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
def min(a: float, b: float) -> float:
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
def min(a: float, b: float, c: float) -> float:
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
def min(a: float, b: float, c: float, d: float) -> float:
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
def min(a: double, b: double) -> double:
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
def min(a: double, b: double, c: double) -> double:
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
def min(a: double, b: double, c: double, d: double) -> double:
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


@overload
def cbrt(a: double) -> double:
    """
    Returns the cube root of the specified value.
    
    Parameters
    -----------
    a : double
        a value.
    
    Returns
    --------
    output : double
        the cube root
    """


@overload
def cbrt(a: float) -> float:
    """
    Returns the cube root of the specified value.
    
    Parameters
    -----------
    a : float
        a value.
    
    Returns
    --------
    output : float
        the cube root
    """


@overload
def IEEEremainder(f1: double, f2: double) -> double:
    """
    Computes the remainder operation on two arguments as prescribed by the
    IEEE 754 standard.
    
    Parameters
    -----------
    f1 : double
        the dividend.
    f2 : double
        the divisor.
    
    Returns
    --------
    output : double
        the remainder when f1 is divided by f2
    """


@overload
def IEEEremainder(f1: float, f2: float) -> float:
    """
    Computes the remainder operation on two arguments as prescribed by the
    IEEE 754 standard.
    
    Parameters
    -----------
    f1 : float
        the dividend.
    f2 : float
        the divisor.
    
    Returns
    --------
    output : float
        the remainder when f1 is divided by f2
    """


def random() -> double:
    """
    Returns a positive number that is greater than or equal to 0.0, and
    less than 1.0.
    Returns
    --------
    output : double
        a pseudorandom number.
    """


def randomDouble() -> double:
    """
    Returns a positive number that is greater than or equal to 0.0, and
    less than 1.0.
    Returns
    --------
    output : double
        a pseudorandom number.
    """


def randomFloat() -> float:
    """
    Returns a positive number that is greater than or equal to 0.0, and
    less than 1.0.
    Returns
    --------
    output : float
        a pseudorandom number.
    """


@overload
def ulp(d: double) -> double:
    """
    Returns the size of an ulp of the argument.
    
    Parameters
    -----------
    d : double
        the value whose ulp is to be returned.
    
    Returns
    --------
    output : double
        the size of an ulp of the argument.
    """


@overload
def ulp(d: float) -> float:
    """
    Returns the size of an ulp of the argument.
    
    Parameters
    -----------
    d : float
        the value whose ulp is to be returned.
    
    Returns
    --------
    output : float
        the size of an ulp of the argument.
    """


@overload
def hypot(x: double, y: double) -> double:
    """
    Returns the hypotenuse for two given values.
    The hypotenuse is calculated using the Pythagorean theorem.
    
    Parameters
    -----------
    x : double
        a value.
    y : double
        a value.
    
    Returns
    --------
    output : double
        the hypotenuse.
    """


@overload
def hypot(x: float, y: float) -> float:
    """
    Returns the hypotenuse for two given values.
    The hypotenuse is calculated using the Pythagorean theorem.
    
    Parameters
    -----------
    x : float
        a value.
    y : float
        a value.
    
    Returns
    --------
    output : float
        the hypotenuse.
    """


@overload
def expm1(x: double) -> double:
    """
    Returns <i>e</i><sup>x</sup>-1.
    
    Parameters
    -----------
    x : double
        the exponent.
    
    Returns
    --------
    output : double
        the value <i>e</i><sup>x</sup>-1.
    """


@overload
def expm1(x: float) -> float:
    """
    Returns <i>e</i><sup>x</sup>-1.
    
    Parameters
    -----------
    x : float
        the exponent.
    
    Returns
    --------
    output : float
        the value <i>e</i><sup>x</sup>-1.
    """


@overload
def log1p(x: double) -> double:
    """
    Returns the natural logarithm of the sum of the argument and 1.
    
    Parameters
    -----------
    x : double
        a value.
    
    Returns
    --------
    output : double
        the value ln(x+1).
    """


@overload
def log1p(x: float) -> float:
    """
    Returns the natural logarithm of the sum of the argument and 1.
    
    Parameters
    -----------
    x : float
        a value.
    
    Returns
    --------
    output : float
        the value ln(x+1).
    """


@overload
def zerobyte(n1: int) -> Byte1D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Byte1D
        an array[n1] of zero bytes.
    """


@overload
def zerobyte(n1: int, n2: int) -> Byte2D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Byte2D
        an array[n2][n1] of zero bytes.
    """


@overload
def zerobyte(n1: int, n2: int, n3: int) -> Byte3D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Byte3D
        an array[n3][n2][n1] of zero bytes.
    """


@overload
def zero(rx: Byte1D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Byte1D
        the array.
    """


@overload
def zero(rx: Byte2D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Byte2D
        the array.
    """


@overload
def zero(rx: Byte3D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Byte3D
        the array.
    """


@overload
def zeroshort(n1: int) -> Short1D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Short1D
        an array[n1] of zero shorts.
    """


@overload
def zeroshort(n1: int, n2: int) -> Short2D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Short2D
        an array[n2][n1] of zero shorts.
    """


@overload
def zeroshort(n1: int, n2: int, n3: int) -> Short3D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Short3D
        an array[n3][n2][n1] of zero shorts.
    """


@overload
def zero(rx: Short1D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Short1D
        the array.
    """


@overload
def zero(rx: Short2D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Short2D
        the array.
    """


@overload
def zero(rx: Short3D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Short3D
        the array.
    """


@overload
def zeroint(n1: int) -> Int1D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Int1D
        an array[n1] of zero integers.
    """


@overload
def zeroint(n1: int, n2: int) -> Int2D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Int2D
        an array[n2][n1] of zero integers.
    """


@overload
def zeroint(n1: int, n2: int, n3: int) -> Int3D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Int3D
        an array[n3][n2][n1] of zero integers.
    """


@overload
def zero(rx: Int1D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Int1D
        the array.
    """


@overload
def zero(rx: Int2D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Int2D
        the array.
    """


@overload
def zero(rx: Int3D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Int3D
        the array.
    """


@overload
def zerolong(n1: int) -> Long1D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Long1D
        an array[n1] of zero longs.
    """


@overload
def zerolong(n1: int, n2: int) -> Long2D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Long2D
        an array[n2][n1] of zero longs.
    """


@overload
def zerolong(n1: int, n2: int, n3: int) -> Long3D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Long3D
        an array[n3][n2][n1] of zero longs.
    """


@overload
def zero(rx: Long1D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Long1D
        the array.
    """


@overload
def zero(rx: Long2D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Long2D
        the array.
    """


@overload
def zero(rx: Long3D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Long3D
        the array.
    """


@overload
def zerofloat(n1: int) -> Float1D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Float1D
        an array[n1] of zero floats.
    """


@overload
def zerofloat(n1: int, n2: int) -> Float2D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Float2D
        an array[n2][n1] of zero floats.
    """


@overload
def zerofloat(n1: int, n2: int, n3: int) -> Float3D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Float3D
        an array[n3][n2][n1] of zero floats.
    """


@overload
def zero(rx: Float1D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Float1D
        the array.
    """


@overload
def zero(rx: Float2D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Float2D
        the array.
    """


@overload
def zero(rx: Float3D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Float3D
        the array.
    """


@overload
def czerofloat(n1: int) -> Float1D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Float1D
        an array[2n1] of zero complex floats.
    """


@overload
def czerofloat(n1: int, n2: int) -> Float2D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Float2D
        an array[n2][2n1] of zero complex floats.
    """


@overload
def czerofloat(n1: int, n2: int, n3: int) -> Float3D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Float3D
        an array[n3][n2][2n1] of zero complex floats.
    """


@overload
def czero(cx: Float1D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    cx : Float1D
        the array.
    """


@overload
def czero(cx: Float2D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    cx : Float2D
        the array.
    """


@overload
def czero(cx: Float3D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    cx : Float3D
        the array.
    """


@overload
def zerodouble(n1: int) -> Double1D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Double1D
        an array[n1] of zero doubles.
    """


@overload
def zerodouble(n1: int, n2: int) -> Double2D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Double2D
        an array[n2][n1] of zero doubles.
    """


@overload
def zerodouble(n1: int, n2: int, n3: int) -> Double3D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Double3D
        an array[n3][n2][n1] of zero doubles.
    """


@overload
def zero(rx: Double1D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Double1D
        the array.
    """


@overload
def zero(rx: Double2D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Double2D
        the array.
    """


@overload
def zero(rx: Double3D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    rx : Double3D
        the array.
    """


@overload
def czerodouble(n1: int) -> Double1D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Double1D
        an array[2n1] of zero complex doubles.
    """


@overload
def czerodouble(n1: int, n2: int) -> Double2D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Double2D
        an array[n2][2n1] of zero complex doubles.
    """


@overload
def czerodouble(n1: int, n2: int, n3: int) -> Double3D:
    """
    Returns a new array of zeros.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Double3D
        an array[n3][n2][2n1] of zero complex doubles.
    """


@overload
def czero(cx: Double1D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    cx : Double1D
        the array.
    """


@overload
def czero(cx: Double2D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    cx : Double2D
        the array.
    """


@overload
def czero(cx: Double3D) -> None:
    """
    Zeros the the specified array.
    
    Parameters
    -----------
    cx : Double3D
        the array.
    """


@overload
def randint(n1: int) -> Int1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Int1D
        an array[n1] of random integers.
    """


@overload
def randint(n1: int, n2: int) -> Int2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Int2D
        an array[n2][n1] of random integers.
    """


@overload
def randint(n1: int, n2: int, n3: int) -> Int3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Int3D
        an array[n3][n2][n1] of random integers.
    """


@overload
def randint(random: Random, n1: int) -> Int1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Int1D
        an array[n1] of random integers.
    """


@overload
def randint(random: Random, n1: int, n2: int) -> Int2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Int2D
        an array[n2][n1] of random integers.
    """


@overload
def randint(random: Random, n1: int, n2: int, n3: int) -> Int3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Int3D
        an array[n3][n2][n1] of random integers.
    """


@overload
def rand(rx: Int1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Int1D
        the array.
    """


@overload
def rand(rx: Int2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Int2D
        the array.
    """


@overload
def rand(rx: Int3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Int3D
        the array.
    """


@overload
def rand(random: Random, rx: Int1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Int1D
        the array.
    """


@overload
def rand(random: Random, rx: Int2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Int2D
        the array.
    """


@overload
def rand(random: Random, rx: Int3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Int3D
        the array.
    """


@overload
def randlong(n1: int) -> Long1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Long1D
        an array[n1] of random longs.
    """


@overload
def randlong(n1: int, n2: int) -> Long2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Long2D
        an array[n2][n1] of random longs.
    """


@overload
def randlong(n1: int, n2: int, n3: int) -> Long3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Long3D
        an array[n3][n2][n1] of random longs.
    """


@overload
def randlong(random: Random, n1: int) -> Long1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Long1D
        an array[n1] of random longs.
    """


@overload
def randlong(random: Random, n1: int, n2: int) -> Long2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Long2D
        an array[n2][n1] of random longs.
    """


@overload
def randlong(random: Random, n1: int, n2: int, n3: int) -> Long3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Long3D
        an array[n3][n2][n1] of random longs.
    """


@overload
def rand(rx: Long1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Long1D
        the array.
    """


@overload
def rand(rx: Long2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Long2D
        the array.
    """


@overload
def rand(rx: Long3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Long3D
        the array.
    """


@overload
def rand(random: Random, rx: Long1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Long1D
        the array.
    """


@overload
def rand(random: Random, rx: Long2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Long2D
        the array.
    """


@overload
def rand(random: Random, rx: Long3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Long3D
        the array.
    """


@overload
def randfloat(n1: int) -> Float1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Float1D
        an array[n1] of random floats.
    """


@overload
def randfloat(n1: int, n2: int) -> Float2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Float2D
        an array[n2][n1] of random floats.
    """


@overload
def randfloat(n1: int, n2: int, n3: int) -> Float3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Float3D
        an array[n3][n2][n1] of random floats.
    """


@overload
def randfloat(random: Random, n1: int) -> Float1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Float1D
        an array[n1] of random floats.
    """


@overload
def randfloat(random: Random, n1: int, n2: int) -> Float2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Float2D
        an array[n2][n1] of random floats.
    """


@overload
def randfloat(random: Random, n1: int, n2: int, n3: int) -> Float3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Float3D
        an array[n3][n2][n1] of random floats.
    """


@overload
def rand(rx: Float1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Float1D
        the array.
    """


@overload
def rand(rx: Float2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Float2D
        the array.
    """


@overload
def rand(rx: Float3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Float3D
        the array.
    """


@overload
def rand(random: Random, rx: Float1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Float1D
        the array.
    """


@overload
def rand(random: Random, rx: Float2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Float2D
        the array.
    """


@overload
def rand(random: Random, rx: Float3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Float3D
        the array.
    """


@overload
def crandfloat(n1: int) -> Float1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Float1D
        an array[2n1] of random complex floats.
    """


@overload
def crandfloat(n1: int, n2: int) -> Float2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Float2D
        an array[n2][2n1] of random complex floats.
    """


@overload
def crandfloat(n1: int, n2: int, n3: int) -> Float3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Float3D
        an array[n3][n2][2n1] of random complex floats.
    """


@overload
def crandfloat(random: Random, n1: int) -> Float1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Float1D
        an array[2n1] of random complex floats.
    """


@overload
def crandfloat(random: Random, n1: int, n2: int) -> Float2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Float2D
        an array[n2][2n1] of random complex floats.
    """


@overload
def crandfloat(random: Random, n1: int, n2: int, n3: int) -> Float3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Float3D
        an array[n3][n2][2n1] of random complex floats.
    """


@overload
def crand(cx: Float1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    cx : Float1D
        the array.
    """


@overload
def crand(cx: Float2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    cx : Float2D
        the array.
    """


@overload
def crand(cx: Float3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    cx : Float3D
        the array.
    """


@overload
def crand(random: Random, cx: Float1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    cx : Float1D
        the array.
    """


@overload
def crand(random: Random, cx: Float2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    cx : Float2D
        the array.
    """


@overload
def crand(random: Random, cx: Float3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    cx : Float3D
        the array.
    """


@overload
def randdouble(n1: int) -> Double1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Double1D
        an array[n1] of random doubles.
    """


@overload
def randdouble(n1: int, n2: int) -> Double2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Double2D
        an array[n2][n1] of random doubles.
    """


@overload
def randdouble(n1: int, n2: int, n3: int) -> Double3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Double3D
        an array[n3][n2][n1] of random doubles.
    """


@overload
def randdouble(random: Random, n1: int) -> Double1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Double1D
        an array[n1] of random doubles.
    """


@overload
def randdouble(random: Random, n1: int, n2: int) -> Double2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Double2D
        an array[n2][n1] of random doubles.
    """


@overload
def randdouble(random: Random, n1: int, n2: int, n3: int) -> Double3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Double3D
        an array[n3][n2][n1] of random doubles.
    """


@overload
def rand(rx: Double1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Double1D
        the array.
    """


@overload
def rand(rx: Double2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Double2D
        the array.
    """


@overload
def rand(rx: Double3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    rx : Double3D
        the array.
    """


@overload
def rand(random: Random, rx: Double1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Double1D
        the array.
    """


@overload
def rand(random: Random, rx: Double2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Double2D
        the array.
    """


@overload
def rand(random: Random, rx: Double3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    rx : Double3D
        the array.
    """


@overload
def cranddouble(n1: int) -> Double1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Double1D
        an array[2n1] of random doubles.
    """


@overload
def cranddouble(n1: int, n2: int) -> Double2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Double2D
        an array[n2][2n1] of random doubles.
    """


@overload
def cranddouble(n1: int, n2: int, n3: int) -> Double3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Double3D
        an array[n3][n2][2n1] of random doubles.
    """


@overload
def cranddouble(random: Random, n1: int) -> Double1D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Double1D
        an array[2n1] of random doubles.
    """


@overload
def cranddouble(random: Random, n1: int, n2: int) -> Double2D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Double2D
        an array[n2][2n1] of random doubles.
    """


@overload
def cranddouble(random: Random, n1: int, n2: int, n3: int) -> Double3D:
    """
    Returns a new array of random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Double3D
        an array[n3][n2][2n1] of random doubles.
    """


@overload
def crand(cx: Double1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    cx : Double1D
        the array.
    """


@overload
def crand(cx: Double2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    cx : Double2D
        the array.
    """


@overload
def crand(cx: Double3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    cx : Double3D
        the array.
    """


@overload
def crand(random: Random, cx: Double1D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    cx : Double1D
        the array.
    """


@overload
def crand(random: Random, cx: Double2D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    cx : Double2D
        the array.
    """


@overload
def crand(random: Random, cx: Double3D) -> None:
    """
    Fills the specified array with random values.
    
    Parameters
    -----------
    random : Random
        random number generator.
    cx : Double3D
        the array.
    """


@overload
def fillbyte(ra: byte, n1: int) -> Byte1D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : byte
        the value.
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Byte1D
        an array[n1] of bytes.
    """


@overload
def fillbyte(ra: byte, n1: int, n2: int) -> Byte2D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : byte
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Byte2D
        an array[n2][n1] of bytes.
    """


@overload
def fillbyte(ra: byte, n1: int, n2: int, n3: int) -> Byte3D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : byte
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Byte3D
        an array[n3][n2][n1] of bytes.
    """


@overload
def fill(ra: byte, rx: Byte1D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : byte
        the value.
    rx : Byte1D
        the array.
    """


@overload
def fill(ra: byte, rx: Byte2D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : byte
        the value.
    rx : Byte2D
        the array.
    """


@overload
def fill(ra: byte, rx: Byte3D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : byte
        the value.
    rx : Byte3D
        the array.
    """


@overload
def fillshort(ra: short, n1: int) -> Short1D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : short
        the value.
    n1 : int
        1st array dimension.
    
    Returns
    --------
    output : Short1D
        an array[n1] of shorts.
    """


@overload
def fillshort(ra: short, n1: int, n2: int) -> Short2D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : short
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    
    Returns
    --------
    output : Short2D
        an array[n2][n1] of shorts.
    """


@overload
def fillshort(ra: short, n1: int, n2: int, n3: int) -> Short3D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : short
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    
    Returns
    --------
    output : Short3D
        an array[n3][n2][n1] of shorts.
    """


@overload
def fill(ra: short, rx: Short1D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : short
        the value.
    rx : Short1D
        the array.
    """


@overload
def fill(ra: short, rx: Short2D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : short
        the value.
    rx : Short2D
        the array.
    """


@overload
def fill(ra: short, rx: Short3D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : short
        the value.
    rx : Short3D
        the array.
    """


@overload
def fillint(ra: int, n1: int) -> Int1D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : int
        the value.
    n1 : int
        1st array dimension.
    """


@overload
def fillint(ra: int, n1: int, n2: int) -> Int2D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : int
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def fillint(ra: int, n1: int, n2: int, n3: int) -> Int3D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : int
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def fill(ra: int, rx: Int1D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : int
        the value.
    rx : Int1D
        the array.
    """


@overload
def fill(ra: int, rx: Int2D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : int
        the value.
    rx : Int2D
        the array.
    """


@overload
def fill(ra: int, rx: Int3D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : int
        the value.
    rx : Int3D
        the array.
    """


@overload
def filllong(ra: long, n1: int) -> Long1D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : long
        the value.
    n1 : int
        1st array dimension.
    """


@overload
def filllong(ra: long, n1: int, n2: int) -> Long2D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : long
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def filllong(ra: long, n1: int, n2: int, n3: int) -> Long3D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : long
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def fill(ra: long, rx: Long1D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : long
        the value.
    rx : Long1D
        the array.
    """


@overload
def fill(ra: long, rx: Long2D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : long
        the value.
    rx : Long2D
        the array.
    """


@overload
def fill(ra: long, rx: Long3D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : long
        the value.
    rx : Long3D
        the array.
    """


@overload
def fillfloat(ra: float, n1: int) -> Float1D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : float
        the value.
    n1 : int
        1st array dimension.
    """


@overload
def fillfloat(ra: float, n1: int, n2: int) -> Float2D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : float
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def fillfloat(ra: float, n1: int, n2: int, n3: int) -> Float3D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : float
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def fill(ra: float, rx: Float1D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : float
        the value.
    rx : Float1D
        the array.
    """


@overload
def fill(ra: float, rx: Float2D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : float
        the value.
    rx : Float2D
        the array.
    """


@overload
def fill(ra: float, rx: Float3D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : float
        the value.
    rx : Float3D
        the array.
    """


@overload
def cfillfloat(ca: Cfloat, n1: int) -> Float1D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ca : Cfloat
        the value.
    n1 : int
        1st array dimension.
    """


@overload
def cfillfloat(ca: Cfloat, n1: int, n2: int) -> Float2D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ca : Cfloat
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def cfillfloat(ca: Cfloat, n1: int, n2: int, n3: int) -> Float3D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ca : Cfloat
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def cfill(ca: Cfloat, cx: Float1D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ca : Cfloat
        the value.
    cx : Float1D
        the array.
    """


@overload
def cfill(ca: Cfloat, cx: Float2D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ca : Cfloat
        the value.
    cx : Float2D
        the array.
    """


@overload
def cfill(ca: Cfloat, cx: Float3D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ca : Cfloat
        the value.
    cx : Float3D
        the array.
    """


@overload
def filldouble(ra: double, n1: int) -> Double1D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : double
        the value.
    n1 : int
        1st array dimension.
    """


@overload
def filldouble(ra: double, n1: int, n2: int) -> Double2D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : double
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def filldouble(ra: double, n1: int, n2: int, n3: int) -> Double3D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ra : double
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def fill(ra: double, rx: Double1D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : double
        the value.
    rx : Double1D
        the array.
    """


@overload
def fill(ra: double, rx: Double2D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : double
        the value.
    rx : Double2D
        the array.
    """


@overload
def fill(ra: double, rx: Double3D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ra : double
        the value.
    rx : Double3D
        the array.
    """


@overload
def cfilldouble(ca: Cdouble, n1: int) -> Double1D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ca : Cdouble
        the value.
    n1 : int
        1st array dimension.
    """


@overload
def cfilldouble(ca: Cdouble, n1: int, n2: int) -> Double2D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ca : Cdouble
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def cfilldouble(ca: Cdouble, n1: int, n2: int, n3: int) -> Double3D:
    """
    Returns an array initialized to a specified value.
    
    Parameters
    -----------
    ca : Cdouble
        the value.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def cfill(ca: Cdouble, cx: Double1D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ca : Cdouble
        the value.
    cx : Double1D
        the array.
    """


@overload
def cfill(ca: Cdouble, cx: Double2D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ca : Cdouble
        the value.
    cx : Double2D
        the array.
    """


@overload
def cfill(ca: Cdouble, cx: Double3D) -> None:
    """
    Fills the specified array with a specified value.
    
    Parameters
    -----------
    ca : Cdouble
        the value.
    cx : Double3D
        the array.
    """


@overload
def rampbyte(ra: byte, rb1: byte, n1: int) -> Byte1D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : byte
        value of the first element.
    rb1 : byte
        gradient in 1st dimension.
    n1 : int
        1st array dimension.
    """


@overload
def rampbyte(ra: byte, rb1: byte, rb2: byte, n1: int, n2: int) -> Byte2D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : byte
        value of the first element.
    rb1 : byte
        gradient in 1st dimension.
    rb2 : byte
        gradient in 2nd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def rampbyte(ra: byte, rb1: byte, rb2: byte, rb3: byte, n1: int, n2: int,
             n3: int) -> Byte3D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : byte
        value of the first element.
    rb1 : byte
        gradient in 1st dimension.
    rb2 : byte
        gradient in 2nd dimension.
    rb3 : byte
        gradient in 3rd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def ramp(ra: byte, rb1: byte, rx: Byte1D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : byte
        value of the first element.
    rb1 : byte
        gradient in 1st dimension.
    rx : Byte1D
        the array.
    """


@overload
def ramp(ra: byte, rb1: byte, rb2: byte, rx: Byte2D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : byte
        value of the first element.
    rb1 : byte
        gradient in 1st dimension.
    rb2 : byte
        gradient in 2nd dimension.
    rx : Byte2D
        the array.
    """


@overload
def ramp(ra: byte, rb1: byte, rb2: byte, rb3: byte, rx: Byte3D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : byte
        value of the first element.
    rb1 : byte
        gradient in 1st dimension.
    rb2 : byte
        gradient in 2nd dimension.
    rb3 : byte
        gradient in 3rd dimension.
    rx : Byte3D
        the array.
    """


@overload
def rampshort(ra: short, rb1: short, n1: int) -> Short1D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : short
        value of the first element.
    rb1 : short
        gradient in 1st dimension.
    n1 : int
        1st array dimension.
    """


@overload
def rampshort(ra: short, rb1: short, rb2: short, n1: int, n2: int) -> Short2D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : short
        value of the first element.
    rb1 : short
        gradient in 1st dimension.
    rb2 : short
        gradient in 2nd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def rampshort(ra: short, rb1: short, rb2: short, rb3: short, n1: int, n2: int,
              n3: int) -> Short3D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : short
        value of the first element.
    rb1 : short
        gradient in 1st dimension.
    rb2 : short
        gradient in 2nd dimension.
    rb3 : short
        gradient in 3rd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def ramp(ra: short, rb1: short, rx: Short1D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : short
        value of the first element.
    rb1 : short
        gradient in 1st dimension.
    rx : Short1D
        the array.
    """


@overload
def ramp(ra: short, rb1: short, rb2: short, rx: Short2D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : short
        value of the first element.
    rb1 : short
        gradient in 1st dimension.
    rb2 : short
        gradient in 2nd dimension.
    rx : Short2D
        the array.
    """


@overload
def ramp(ra: short, rb1: short, rb2: short, rb3: short, rx: Short3D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : short
        value of the first element.
    rb1 : short
        gradient in 1st dimension.
    rb2 : short
        gradient in 2nd dimension.
    rb3 : short
        gradient in 3rd dimension.
    rx : Short3D
        the array.
    """


@overload
def rampint(ra: int, rb1: int, n1: int) -> Int1D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : int
        value of the first element.
    rb1 : int
        gradient in 1st dimension.
    n1 : int
        1st array dimension.
    """


@overload
def rampint(ra: int, rb1: int, rb2: int, n1: int, n2: int) -> Int2D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : int
        value of the first element.
    rb1 : int
        gradient in 1st dimension.
    rb2 : int
        gradient in 2nd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def rampint(ra: int, rb1: int, rb2: int, rb3: int, n1: int, n2: int,
            n3: int) -> Int3D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : int
        value of the first element.
    rb1 : int
        gradient in 1st dimension.
    rb2 : int
        gradient in 2nd dimension.
    rb3 : int
        gradient in 3rd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def ramp(ra: int, rb1: int, rx: Int1D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : int
        value of the first element.
    rb1 : int
        gradient in 1st dimension.
    rx : Int1D
        the array.
    """


@overload
def ramp(ra: int, rb1: int, rb2: int, rx: Int2D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : int
        value of the first element.
    rb1 : int
        gradient in 1st dimension.
    rb2 : int
        gradient in 2nd dimension.
    rx : Int2D
        the array.
    """


@overload
def ramp(ra: int, rb1: int, rb2: int, rb3: int, rx: Int3D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : int
        value of the first element.
    rb1 : int
        gradient in 1st dimension.
    rb2 : int
        gradient in 2nd dimension.
    rb3 : int
        gradient in 3rd dimension.
    rx : Int3D
        the array.
    """


@overload
def ramplong(ra: long, rb1: long, n1: int) -> Long1D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : long
        value of the first element.
    rb1 : long
        gradient in 1st dimension.
    n1 : int
        1st array dimension.
    """


@overload
def ramplong(ra: long, rb1: long, rb2: long, n1: int, n2: int) -> Long2D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : long
        value of the first element.
    rb1 : long
        gradient in 1st dimension.
    rb2 : long
        gradient in 2nd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def ramplong(ra: long, rb1: long, rb2: long, rb3: long, n1: int, n2: int,
             n3: int) -> Long3D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : long
        value of the first element.
    rb1 : long
        gradient in 1st dimension.
    rb2 : long
        gradient in 2nd dimension.
    rb3 : long
        gradient in 3rd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def ramp(ra: long, rb1: long, rx: Long1D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : long
        value of the first element.
    rb1 : long
        gradient in 1st dimension.
    rx : Long1D
        the array.
    """


@overload
def ramp(ra: long, rb1: long, rb2: long, rx: Long2D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : long
        value of the first element.
    rb1 : long
        gradient in 1st dimension.
    rb2 : long
        gradient in 2nd dimension.
    rx : Long2D
        the array.
    """


@overload
def ramp(ra: long, rb1: long, rb2: long, rb3: long, rx: Long3D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : long
        value of the first element.
    rb1 : long
        gradient in 1st dimension.
    rb2 : long
        gradient in 2nd dimension.
    rb3 : long
        gradient in 3rd dimension.
    rx : Long3D
        the array.
    """


@overload
def rampfloat(ra: float, rb1: float, n1: int) -> Float1D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : float
        value of the first element.
    rb1 : float
        gradient in 1st dimension.
    n1 : int
        1st array dimension.
    """


@overload
def rampfloat(ra: float, rb1: float, rb2: float, n1: int, n2: int) -> Float2D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : float
        value of the first element.
    rb1 : float
        gradient in 1st dimension.
    rb2 : float
        gradient in 2nd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def rampfloat(ra: float, rb1: float, rb2: float, rb3: float, n1: int, n2: int,
              n3: int) -> Float3D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : float
        value of the first element.
    rb1 : float
        gradient in 1st dimension.
    rb2 : float
        gradient in 2nd dimension.
    rb3 : float
        gradient in 3rd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def ramp(ra: float, rb1: float, rx: Float1D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : float
        value of the first element.
    rb1 : float
        gradient in 1st dimension.
    rx : Float1D
        the array.
    """


@overload
def ramp(ra: float, rb1: float, rb2: float, rx: Float2D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : float
        value of the first element.
    rb1 : float
        gradient in 1st dimension.
    rb2 : float
        gradient in 2nd dimension.
    rx : Float2D
        the array.
    """


@overload
def ramp(ra: float, rb1: float, rb2: float, rb3: float, rx: Float3D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : float
        value of the first element.
    rb1 : float
        gradient in 1st dimension.
    rb2 : float
        gradient in 2nd dimension.
    rb3 : float
        gradient in 3rd dimension.
    rx : Float3D
        the array.
    """


@overload
def crampfloat(ca: Cfloat, cb1: Cfloat, n1: int) -> Float1D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ca+i1cb1.
    
    Parameters
    -----------
    ca : Cfloat
        value of the first element.
    cb1 : Cfloat
        gradient in 1st dimension.
    n1 : int
        1st array dimension.
    """


@overload
def crampfloat(ca: Cfloat, cb1: Cfloat, cb2: Cfloat, n1: int,
               n2: int) -> Float2D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ca+i1cb1+i2cb2.
    
    Parameters
    -----------
    ca : Cfloat
        value of the first element.
    cb1 : Cfloat
        gradient in 1st dimension.
    cb2 : Cfloat
        gradient in 2nd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def crampfloat(ca: Cfloat, cb1: Cfloat, cb2: Cfloat, cb3: Cfloat, n1: int,
               n2: int, n3: int) -> Float3D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ca+i1cb1+i2cb2+i3cb3.
    
    Parameters
    -----------
    ca : Cfloat
        value of the first element.
    cb1 : Cfloat
        gradient in 1st dimension.
    cb2 : Cfloat
        gradient in 2nd dimension.
    cb3 : Cfloat
        gradient in 3rd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def cramp(ca: Cfloat, cb1: Cfloat, cx: Float1D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ca+i1cb1.
    
    Parameters
    -----------
    ca : Cfloat
        value of the first element.
    cb1 : Cfloat
        gradient in 1st dimension.
    cx : Float1D
        the array.
    """


@overload
def cramp(ca: Cfloat, cb1: Cfloat, cb2: Cfloat, cx: Float2D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ca+i1cb1+i2cb2.
    
    Parameters
    -----------
    ca : Cfloat
        value of the first element.
    cb1 : Cfloat
        gradient in 1st dimension.
    cb2 : Cfloat
        gradient in 2nd dimension.
    cx : Float2D
        the array.
    """


@overload
def cramp(ca: Cfloat, cb1: Cfloat, cb2: Cfloat, cb3: Cfloat,
          cx: Float3D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ca+i1cb1+i2cb2+i3cb3.
    
    Parameters
    -----------
    ca : Cfloat
        value of the first element.
    cb1 : Cfloat
        gradient in 1st dimension.
    cb2 : Cfloat
        gradient in 2nd dimension.
    cb3 : Cfloat
        gradient in 3rd dimension.
    cx : Float3D
        the array.
    """


@overload
def rampdouble(ra: double, rb1: double, n1: int) -> Double1D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : double
        value of the first element.
    rb1 : double
        gradient in 1st dimension.
    n1 : int
        1st array dimension.
    """


@overload
def rampdouble(ra: double, rb1: double, rb2: double, n1: int,
               n2: int) -> Double2D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : double
        value of the first element.
    rb1 : double
        gradient in 1st dimension.
    rb2 : double
        gradient in 2nd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def rampdouble(ra: double, rb1: double, rb2: double, rb3: double, n1: int,
               n2: int, n3: int) -> Double3D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : double
        value of the first element.
    rb1 : double
        gradient in 1st dimension.
    rb2 : double
        gradient in 2nd dimension.
    rb3 : double
        gradient in 3rd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def ramp(ra: double, rb1: double, rx: Double1D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1.
    
    Parameters
    -----------
    ra : double
        value of the first element.
    rb1 : double
        gradient in 1st dimension.
    rx : Double1D
        the array.
    """


@overload
def ramp(ra: double, rb1: double, rb2: double, rx: Double2D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2.
    
    Parameters
    -----------
    ra : double
        value of the first element.
    rb1 : double
        gradient in 1st dimension.
    rb2 : double
        gradient in 2nd dimension.
    rx : Double2D
        the array.
    """


@overload
def ramp(ra: double, rb1: double, rb2: double, rb3: double,
         rx: Double3D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ra+i1rb1+i2rb2+i3rb3.
    
    Parameters
    -----------
    ra : double
        value of the first element.
    rb1 : double
        gradient in 1st dimension.
    rb2 : double
        gradient in 2nd dimension.
    rb3 : double
        gradient in 3rd dimension.
    rx : Double3D
        the array.
    """


@overload
def crampdouble(ca: Cdouble, cb1: Cdouble, n1: int) -> Double1D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ca+i1cb1.
    
    Parameters
    -----------
    ca : Cdouble
        value of the first element.
    cb1 : Cdouble
        gradient in 1st dimension.
    n1 : int
        1st array dimension.
    """


@overload
def crampdouble(ca: Cdouble, cb1: Cdouble, cb2: Cdouble, n1: int,
                n2: int) -> Double2D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ca+i1cb1+i2cb2.
    
    Parameters
    -----------
    ca : Cdouble
        value of the first element.
    cb1 : Cdouble
        gradient in 1st dimension.
    cb2 : Cdouble
        gradient in 2nd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    """


@overload
def crampdouble(ca: Cdouble, cb1: Cdouble, cb2: Cdouble, cb3: Cdouble, n1: int,
                n2: int, n3: int) -> Double3D:
    """
    Returns an array initialized to a specified linear ramp.
    Array values are ca+i1cb1+i2cb2+i3cb3.
    
    Parameters
    -----------
    ca : Cdouble
        value of the first element.
    cb1 : Cdouble
        gradient in 1st dimension.
    cb2 : Cdouble
        gradient in 2nd dimension.
    cb3 : Cdouble
        gradient in 3rd dimension.
    n1 : int
        1st array dimension.
    n2 : int
        2nd array dimension.
    n3 : int
        3rd array dimension.
    """


@overload
def cramp(ca: Cdouble, cb1: Cdouble, cx: Double1D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ca+i1cb1.
    
    Parameters
    -----------
    ca : Cdouble
        value of the first element.
    cb1 : Cdouble
        gradient in 1st dimension.
    cx : Double1D
        the array.
    """


@overload
def cramp(ca: Cdouble, cb1: Cdouble, cb2: Cdouble, cx: Double2D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ca+i1cb1+i2cb2.
    
    Parameters
    -----------
    ca : Cdouble
        value of the first element.
    cb1 : Cdouble
        gradient in 1st dimension.
    cb2 : Cdouble
        gradient in 2nd dimension.
    cx : Double2D
        the array.
    """


@overload
def cramp(ca: Cdouble, cb1: Cdouble, cb2: Cdouble, cb3: Cdouble,
          cx: Double3D) -> None:
    """
    Sets the specified array with a specified linear ramp.
    Array values are ca+i1cb1+i2cb2+i3cb3.
    
    Parameters
    -----------
    ca : Cdouble
        value of the first element.
    cb1 : Cdouble
        gradient in 1st dimension.
    cb2 : Cdouble
        gradient in 2nd dimension.
    cb3 : Cdouble
        gradient in 3rd dimension.
    cx : Double3D
        the array.
    """


@overload
def copy(rx: Byte1D) -> Byte1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Byte1D
        source array.
    
    Returns
    --------
    output : Byte1D
        array copy
    """


@overload
def copy(rx: Byte2D) -> Byte2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Byte2D
        source array.
    
    Returns
    --------
    output : Byte2D
        array copy
    """


@overload
def copy(rx: Byte3D) -> Byte3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Byte3D
        source array.
    
    Returns
    --------
    output : Byte3D
        array copy
    """


@overload
def copy(rx: Byte1D, ry: Byte1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Byte1D
        source array.
    ry : Byte1D
        destination array.
    """


@overload
def copy(rx: Byte2D, ry: Byte2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Byte2D
        source array.
    ry : Byte2D
        destination array.
    """


@overload
def copy(rx: Byte3D, ry: Byte3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Byte3D
        source array.
    ry : Byte3D
        destination array.
    """


@overload
def copy(n1: int, rx: Byte1D) -> Byte1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Byte1D
        source array.
    
    Returns
    --------
    output : Byte1D
        array copy
    """


@overload
def copy(n1: int, n2: int, rx: Byte2D) -> Byte2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Byte2D
        source array.
    
    Returns
    --------
    output : Byte2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Byte3D) -> Byte3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Byte3D
        source array.
    
    Returns
    --------
    output : Byte3D
        array copy
    """


@overload
def copy(n1: int, rx: Byte1D, ry: Byte1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Byte1D
        source array.
    ry : Byte1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, rx: Byte2D, ry: Byte2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Byte2D
        source array.
    ry : Byte2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Byte3D, ry: Byte3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Byte3D
        source array.
    ry : Byte3D
        destination array.
    """


@overload
def copy(n1: int, j1: int, rx: Byte1D) -> Byte1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    rx : Byte1D
        source array.
    
    Returns
    --------
    output : Byte1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, rx: Byte2D) -> Byte2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    rx : Byte2D
        source array.
    
    Returns
    --------
    output : Byte2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int,
         rx: Byte3D) -> Byte3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    rx : Byte3D
        source array.
    
    Returns
    --------
    output : Byte3D
        array copy
    """


@overload
def copy(n1: int, j1: int, k1: int, rx: Byte1D) -> Byte1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    rx : Byte1D
        source array.
    
    Returns
    --------
    output : Byte1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, k1: int, k2: int,
         rx: Byte2D) -> Byte2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    rx : Byte2D
        source array.
    
    Returns
    --------
    output : Byte2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int, k1: int,
         k2: int, k3: int, rx: Byte3D) -> Byte3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    k3 : int
        stride in 3rd dimension of rx.
    rx : Byte3D
        source array.
    
    Returns
    --------
    output : Byte3D
        array copy
    """


@overload
def copy(n1: int, j1x: int, rx: Byte1D, j1y: int, ry: Byte1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    rx : Byte1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    ry : Byte1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, rx: Byte2D, j1y: int, j2y: int,
         ry: Byte2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    rx : Byte2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    ry : Byte2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, rx: Byte3D,
         j1y: int, j2y: int, j3y: int, ry: Byte3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    rx : Byte3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    ry : Byte3D
        destination array.
    """


@overload
def copy(n1: int, j1x: int, k1x: int, rx: Byte1D, j1y: int, k1y: int,
         ry: Byte1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    rx : Byte1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    ry : Byte1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, k1x: int, k2x: int, rx: Byte2D,
         j1y: int, j2y: int, k1y: int, k2y: int, ry: Byte2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    rx : Byte2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    ry : Byte2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, k1x: int,
         k2x: int, k3x: int, rx: Byte3D, j1y: int, j2y: int, j3y: int,
         k1y: int, k2y: int, k3y: int, ry: Byte3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    k3x : int
        stride in 3rd dimension of rx.
    rx : Byte3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    k3y : int
        stride in 3rd dimension of ry.
    ry : Byte3D
        destination array.
    """


@overload
def copy(rx: Short1D) -> Short1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Short1D
        source array.
    
    Returns
    --------
    output : Short1D
        array copy
    """


@overload
def copy(rx: Short2D) -> Short2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Short2D
        source array.
    
    Returns
    --------
    output : Short2D
        array copy
    """


@overload
def copy(rx: Short3D) -> Short3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Short3D
        source array.
    
    Returns
    --------
    output : Short3D
        array copy
    """


@overload
def copy(rx: Short1D, ry: Short1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Short1D
        source array.
    ry : Short1D
        destination array.
    """


@overload
def copy(rx: Short2D, ry: Short2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Short2D
        source array.
    ry : Short2D
        destination array.
    """


@overload
def copy(rx: Short3D, ry: Short3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Short3D
        source array.
    ry : Short3D
        destination array.
    """


@overload
def copy(n1: int, rx: Short1D) -> Short1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Short1D
        source array.
    
    Returns
    --------
    output : Short1D
        array copy
    """


@overload
def copy(n1: int, n2: int, rx: Short2D) -> Short2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Short2D
        source array.
    
    Returns
    --------
    output : Short2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Short3D) -> Short3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Short3D
        source array.
    
    Returns
    --------
    output : Short3D
        array copy
    """


@overload
def copy(n1: int, rx: Short1D, ry: Short1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Short1D
        source array.
    ry : Short1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, rx: Short2D, ry: Short2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Short2D
        source array.
    ry : Short2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Short3D, ry: Short3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Short3D
        source array.
    ry : Short3D
        destination array.
    """


@overload
def copy(n1: int, j1: int, rx: Short1D) -> Short1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    rx : Short1D
        source array.
    
    Returns
    --------
    output : Short1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, rx: Short2D) -> Short2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    rx : Short2D
        source array.
    
    Returns
    --------
    output : Short2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int,
         rx: Short3D) -> Short3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    rx : Short3D
        source array.
    
    Returns
    --------
    output : Short3D
        array copy
    """


@overload
def copy(n1: int, j1: int, k1: int, rx: Short1D) -> Short1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    rx : Short1D
        source array.
    
    Returns
    --------
    output : Short1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, k1: int, k2: int,
         rx: Short2D) -> Short2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    rx : Short2D
        source array.
    
    Returns
    --------
    output : Short2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int, k1: int,
         k2: int, k3: int, rx: Short3D) -> Short3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    k3 : int
        stride in 3rd dimension of rx.
    rx : Short3D
        source array.
    
    Returns
    --------
    output : Short3D
        array copy
    """


@overload
def copy(n1: int, j1x: int, rx: Short1D, j1y: int, ry: Short1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    rx : Short1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    ry : Short1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, rx: Short2D, j1y: int, j2y: int,
         ry: Short2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    rx : Short2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    ry : Short2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, rx: Short3D,
         j1y: int, j2y: int, j3y: int, ry: Short3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    rx : Short3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    ry : Short3D
        destination array.
    """


@overload
def copy(n1: int, j1x: int, k1x: int, rx: Short1D, j1y: int, k1y: int,
         ry: Short1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    rx : Short1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    ry : Short1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, k1x: int, k2x: int, rx: Short2D,
         j1y: int, j2y: int, k1y: int, k2y: int, ry: Short2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    rx : Short2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    ry : Short2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, k1x: int,
         k2x: int, k3x: int, rx: Short3D, j1y: int, j2y: int, j3y: int,
         k1y: int, k2y: int, k3y: int, ry: Short3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    k3x : int
        stride in 3rd dimension of rx.
    rx : Short3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    k3y : int
        stride in 3rd dimension of ry.
    ry : Short3D
        destination array.
    """


@overload
def copy(rx: Int1D) -> Int1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Int1D
        source array.
    
    Returns
    --------
    output : Int1D
        array copy
    """


@overload
def copy(rx: Int2D) -> Int2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Int2D
        source array.
    
    Returns
    --------
    output : Int2D
        array copy
    """


@overload
def copy(rx: Int3D) -> Int3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Int3D
        source array.
    
    Returns
    --------
    output : Int3D
        array copy
    """


@overload
def copy(rx: Int1D, ry: Int1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Int1D
        source array.
    ry : Int1D
        destination array.
    """


@overload
def copy(rx: Int2D, ry: Int2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Int2D
        source array.
    ry : Int2D
        destination array.
    """


@overload
def copy(rx: Int3D, ry: Int3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Int3D
        source array.
    ry : Int3D
        destination array.
    """


@overload
def copy(n1: int, rx: Int1D) -> Int1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Int1D
        source array.
    
    Returns
    --------
    output : Int1D
        array copy
    """


@overload
def copy(n1: int, n2: int, rx: Int2D) -> Int2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Int2D
        source array.
    
    Returns
    --------
    output : Int2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Int3D) -> Int3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Int3D
        source array.
    
    Returns
    --------
    output : Int3D
        array copy
    """


@overload
def copy(n1: int, rx: Int1D, ry: Int1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Int1D
        source array.
    ry : Int1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, rx: Int2D, ry: Int2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Int2D
        source array.
    ry : Int2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Int3D, ry: Int3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Int3D
        source array.
    ry : Int3D
        destination array.
    """


@overload
def copy(n1: int, j1: int, rx: Int1D) -> Int1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    rx : Int1D
        source array.
    
    Returns
    --------
    output : Int1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, rx: Int2D) -> Int2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    rx : Int2D
        source array.
    
    Returns
    --------
    output : Int2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int,
         rx: Int3D) -> Int3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    rx : Int3D
        source array.
    
    Returns
    --------
    output : Int3D
        array copy
    """


@overload
def copy(n1: int, j1: int, k1: int, rx: Int1D) -> Int1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    rx : Int1D
        source array.
    
    Returns
    --------
    output : Int1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, k1: int, k2: int,
         rx: Int2D) -> Int2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    rx : Int2D
        source array.
    
    Returns
    --------
    output : Int2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int, k1: int,
         k2: int, k3: int, rx: Int3D) -> Int3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    k3 : int
        stride in 3rd dimension of rx.
    rx : Int3D
        source array.
    
    Returns
    --------
    output : Int3D
        array copy
    """


@overload
def copy(n1: int, j1x: int, rx: Int1D, j1y: int, ry: Int1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    rx : Int1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    ry : Int1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, rx: Int2D, j1y: int, j2y: int,
         ry: Int2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    rx : Int2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    ry : Int2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, rx: Int3D,
         j1y: int, j2y: int, j3y: int, ry: Int3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    rx : Int3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    ry : Int3D
        destination array.
    """


@overload
def copy(n1: int, j1x: int, k1x: int, rx: Int1D, j1y: int, k1y: int,
         ry: Int1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    rx : Int1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    ry : Int1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, k1x: int, k2x: int, rx: Int2D,
         j1y: int, j2y: int, k1y: int, k2y: int, ry: Int2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    rx : Int2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    ry : Int2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, k1x: int,
         k2x: int, k3x: int, rx: Int3D, j1y: int, j2y: int, j3y: int, k1y: int,
         k2y: int, k3y: int, ry: Int3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    k3x : int
        stride in 3rd dimension of rx.
    rx : Int3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    k3y : int
        stride in 3rd dimension of ry.
    ry : Int3D
        destination array.
    """


@overload
def copy(rx: Long1D) -> Long1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Long1D
        source array.
    
    Returns
    --------
    output : Long1D
        array copy
    """


@overload
def copy(rx: Long2D) -> Long2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Long2D
        source array.
    
    Returns
    --------
    output : Long2D
        array copy
    """


@overload
def copy(rx: Long3D) -> Long3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Long3D
        source array.
    
    Returns
    --------
    output : Long3D
        array copy
    """


@overload
def copy(rx: Long1D, ry: Long1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Long1D
        source array.
    ry : Long1D
        destination array.
    """


@overload
def copy(rx: Long2D, ry: Long2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Long2D
        source array.
    ry : Long2D
        destination array.
    """


@overload
def copy(rx: Long3D, ry: Long3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Long3D
        source array.
    ry : Long3D
        destination array.
    """


@overload
def copy(n1: int, rx: Long1D) -> Long1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Long1D
        source array.
    
    Returns
    --------
    output : Long1D
        array copy
    """


@overload
def copy(n1: int, n2: int, rx: Long2D) -> Long2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Long2D
        source array.
    
    Returns
    --------
    output : Long2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Long3D) -> Long3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Long3D
        source array.
    
    Returns
    --------
    output : Long3D
        array copy
    """


@overload
def copy(n1: int, rx: Long1D, ry: Long1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Long1D
        source array.
    ry : Long1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, rx: Long2D, ry: Long2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Long2D
        source array.
    ry : Long2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Long3D, ry: Long3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Long3D
        source array.
    ry : Long3D
        destination array.
    """


@overload
def copy(n1: int, j1: int, rx: Long1D) -> Long1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    rx : Long1D
        source array.
    
    Returns
    --------
    output : Long1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, rx: Long2D) -> Long2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    rx : Long2D
        source array.
    
    Returns
    --------
    output : Long2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int,
         rx: Long3D) -> Long3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    rx : Long3D
        source array.
    
    Returns
    --------
    output : Long3D
        array copy
    """


@overload
def copy(n1: int, j1: int, k1: int, rx: Long1D) -> Long1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    rx : Long1D
        source array.
    
    Returns
    --------
    output : Long1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, k1: int, k2: int,
         rx: Long2D) -> Long2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    rx : Long2D
        source array.
    
    Returns
    --------
    output : Long2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int, k1: int,
         k2: int, k3: int, rx: Long3D) -> Long3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    k3 : int
        stride in 3rd dimension of rx.
    rx : Long3D
        source array.
    
    Returns
    --------
    output : Long3D
        array copy
    """


@overload
def copy(n1: int, j1x: int, rx: Long1D, j1y: int, ry: Long1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    rx : Long1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    ry : Long1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, rx: Long2D, j1y: int, j2y: int,
         ry: Long2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    rx : Long2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    ry : Long2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, rx: Long3D,
         j1y: int, j2y: int, j3y: int, ry: Long3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    rx : Long3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    ry : Long3D
        destination array.
    """


@overload
def copy(n1: int, j1x: int, k1x: int, rx: Long1D, j1y: int, k1y: int,
         ry: Long1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    rx : Long1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    ry : Long1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, k1x: int, k2x: int, rx: Long2D,
         j1y: int, j2y: int, k1y: int, k2y: int, ry: Long2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    rx : Long2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    ry : Long2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, k1x: int,
         k2x: int, k3x: int, rx: Long3D, j1y: int, j2y: int, j3y: int,
         k1y: int, k2y: int, k3y: int, ry: Long3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    k3x : int
        stride in 3rd dimension of rx.
    rx : Long3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    k3y : int
        stride in 3rd dimension of ry.
    ry : Long3D
        destination array.
    """


@overload
def copy(rx: Float1D) -> Float1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Float1D
        source array.
    
    Returns
    --------
    output : Float1D
        array copy
    """


@overload
def copy(rx: Float2D) -> Float2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Float2D
        source array.
    
    Returns
    --------
    output : Float2D
        array copy
    """


@overload
def copy(rx: Float3D) -> Float3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Float3D
        source array.
    
    Returns
    --------
    output : Float3D
        array copy
    """


@overload
def copy(rx: Float1D, ry: Float1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Float1D
        source array.
    ry : Float1D
        destination array.
    """


@overload
def copy(rx: Float2D, ry: Float2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Float2D
        source array.
    ry : Float2D
        destination array.
    """


@overload
def copy(rx: Float3D, ry: Float3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Float3D
        source array.
    ry : Float3D
        destination array.
    """


@overload
def copy(n1: int, rx: Float1D) -> Float1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Float1D
        source array.
    
    Returns
    --------
    output : Float1D
        array copy
    """


@overload
def copy(n1: int, n2: int, rx: Float2D) -> Float2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Float2D
        source array.
    
    Returns
    --------
    output : Float2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Float3D) -> Float3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Float3D
        source array.
    
    Returns
    --------
    output : Float3D
        array copy
    """


@overload
def copy(n1: int, rx: Float1D, ry: Float1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Float1D
        source array.
    ry : Float1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, rx: Float2D, ry: Float2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Float2D
        source array.
    ry : Float2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Float3D, ry: Float3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Float3D
        source array.
    ry : Float3D
        destination array.
    """


@overload
def copy(n1: int, j1: int, rx: Float1D) -> Float1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    rx : Float1D
        source array.
    
    Returns
    --------
    output : Float1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, rx: Float2D) -> Float2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    rx : Float2D
        source array.
    
    Returns
    --------
    output : Float2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int,
         rx: Float3D) -> Float3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    rx : Float3D
        source array.
    
    Returns
    --------
    output : Float3D
        array copy
    """


@overload
def copy(n1: int, j1: int, k1: int, rx: Float1D) -> Float1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    rx : Float1D
        source array.
    
    Returns
    --------
    output : Float1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, k1: int, k2: int,
         rx: Float2D) -> Float2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    rx : Float2D
        source array.
    
    Returns
    --------
    output : Float2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int, k1: int,
         k2: int, k3: int, rx: Float3D) -> Float3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    k3 : int
        stride in 3rd dimension of rx.
    rx : Float3D
        source array.
    
    Returns
    --------
    output : Float3D
        array copy
    """


@overload
def copy(n1: int, j1x: int, rx: Float1D, j1y: int, ry: Float1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    rx : Float1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    ry : Float1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, rx: Float2D, j1y: int, j2y: int,
         ry: Float2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    rx : Float2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    ry : Float2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, rx: Float3D,
         j1y: int, j2y: int, j3y: int, ry: Float3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    rx : Float3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    ry : Float3D
        destination array.
    """


@overload
def copy(n1: int, j1x: int, k1x: int, rx: Float1D, j1y: int, k1y: int,
         ry: Float1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    rx : Float1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    ry : Float1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, k1x: int, k2x: int, rx: Float2D,
         j1y: int, j2y: int, k1y: int, k2y: int, ry: Float2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    rx : Float2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    ry : Float2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, k1x: int,
         k2x: int, k3x: int, rx: Float3D, j1y: int, j2y: int, j3y: int,
         k1y: int, k2y: int, k3y: int, ry: Float3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    k3x : int
        stride in 3rd dimension of rx.
    rx : Float3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    k3y : int
        stride in 3rd dimension of ry.
    ry : Float3D
        destination array.
    """


@overload
def ccopy(cx: Float1D) -> Float1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    cx : Float1D
        source array.
    
    Returns
    --------
    output : Float1D
        array copy
    """


@overload
def ccopy(cx: Float2D) -> Float2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    cx : Float2D
        source array.
    
    Returns
    --------
    output : Float2D
        array copy
    """


@overload
def ccopy(cx: Float3D) -> Float3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    cx : Float3D
        source array.
    
    Returns
    --------
    output : Float3D
        array copy
    """


@overload
def ccopy(cx: Float1D, cy: Float1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    cx : Float1D
        source array.
    cy : Float1D
        destination array.
    """


@overload
def ccopy(cx: Float2D, cy: Float2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    cx : Float2D
        source array.
    cy : Float2D
        destination array.
    """


@overload
def ccopy(cx: Float3D, cy: Float3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    cx : Float3D
        source array.
    cy : Float3D
        destination array.
    """


@overload
def ccopy(n1: int, cx: Float1D) -> Float1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    cx : Float1D
        source array.
    
    Returns
    --------
    output : Float1D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, cx: Float2D) -> Float2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    cx : Float2D
        source array.
    
    Returns
    --------
    output : Float2D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, n3: int, cx: Float3D) -> Float3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    cx : Float3D
        source array.
    
    Returns
    --------
    output : Float3D
        array copy
    """


@overload
def ccopy(n1: int, cx: Float1D, cy: Float1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    cx : Float1D
        source array.
    cy : Float1D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, cx: Float2D, cy: Float2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    cx : Float2D
        source array.
    cy : Float2D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, n3: int, cx: Float3D, cy: Float3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    cx : Float3D
        source array.
    cy : Float3D
        destination array.
    """


@overload
def ccopy(n1: int, j1: int, cx: Float1D) -> Float1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of cx.
    cx : Float1D
        source array.
    
    Returns
    --------
    output : Float1D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, j1: int, j2: int, cx: Float2D) -> Float2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of cx.
    j2 : int
        offset in 2nd dimension of cx.
    cx : Float2D
        source array.
    
    Returns
    --------
    output : Float2D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int,
          cx: Float3D) -> Float3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of cx.
    j2 : int
        offset in 2nd dimension of cx.
    j3 : int
        offset in 3rd dimension of cx.
    cx : Float3D
        source array.
    
    Returns
    --------
    output : Float3D
        array copy
    """


@overload
def ccopy(n1: int, j1: int, k1: int, cx: Float1D) -> Float1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of cx.
    k1 : int
        stride in 1st dimension of cx.
    cx : Float1D
        source array.
    
    Returns
    --------
    output : Float1D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, j1: int, j2: int, k1: int, k2: int,
          cx: Float2D) -> Float2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of cx.
    j2 : int
        offset in 2nd dimension of cx.
    k1 : int
        stride in 1st dimension of cx.
    k2 : int
        stride in 2nd dimension of cx.
    cx : Float2D
        source array.
    
    Returns
    --------
    output : Float2D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int, k1: int,
          k2: int, k3: int, cx: Float3D) -> Float3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of cx.
    j2 : int
        offset in 2nd dimension of cx.
    j3 : int
        offset in 3rd dimension of cx.
    k1 : int
        stride in 1st dimension of cx.
    k2 : int
        stride in 2nd dimension of cx.
    k3 : int
        stride in 3rd dimension of cx.
    cx : Float3D
        source array.
    
    Returns
    --------
    output : Float3D
        array copy
    """


@overload
def ccopy(n1: int, j1x: int, cx: Float1D, j1y: int, cy: Float1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of cx.
    cx : Float1D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    cy : Float1D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, j1x: int, j2x: int, cx: Float2D, j1y: int,
          j2y: int, cy: Float2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of cx.
    j2x : int
        offset in 2nd dimension of cx.
    cx : Float2D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    j2y : int
        offset in 2nd dimension of cy.
    cy : Float2D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, cx: Float3D,
          j1y: int, j2y: int, j3y: int, cy: Float3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of cx.
    j2x : int
        offset in 2nd dimension of cx.
    j3x : int
        offset in 3rd dimension of cx.
    cx : Float3D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    j2y : int
        offset in 2nd dimension of cy.
    j3y : int
        offset in 3rd dimension of cy.
    cy : Float3D
        destination array.
    """


@overload
def ccopy(n1: int, j1x: int, k1x: int, cx: Float1D, j1y: int, k1y: int,
          cy: Float1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of cx.
    k1x : int
        stride in 1st dimension of cx.
    cx : Float1D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    k1y : int
        stride in 1st dimension of cy.
    cy : Float1D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, j1x: int, j2x: int, k1x: int, k2x: int,
          cx: Float2D, j1y: int, j2y: int, k1y: int, k2y: int,
          cy: Float2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of cx.
    j2x : int
        offset in 2nd dimension of cx.
    k1x : int
        stride in 1st dimension of cx.
    k2x : int
        stride in 2nd dimension of cx.
    cx : Float2D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    j2y : int
        offset in 2nd dimension of cy.
    k1y : int
        stride in 1st dimension of cy.
    k2y : int
        stride in 2nd dimension of cy.
    cy : Float2D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, k1x: int,
          k2x: int, k3x: int, cx: Float3D, j1y: int, j2y: int, j3y: int,
          k1y: int, k2y: int, k3y: int, cy: Float3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of cx.
    j2x : int
        offset in 2nd dimension of cx.
    j3x : int
        offset in 3rd dimension of cx.
    k1x : int
        stride in 1st dimension of cx.
    k2x : int
        stride in 2nd dimension of cx.
    k3x : int
        stride in 3rd dimension of cx.
    cx : Float3D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    j2y : int
        offset in 2nd dimension of cy.
    j3y : int
        offset in 3rd dimension of cy.
    k1y : int
        stride in 1st dimension of cy.
    k2y : int
        stride in 2nd dimension of cy.
    k3y : int
        stride in 3rd dimension of cy.
    cy : Float3D
        destination array.
    """


@overload
def copy(rx: Double1D) -> Double1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Double1D
        source array.
    
    Returns
    --------
    output : Double1D
        array copy
    """


@overload
def copy(rx: Double2D) -> Double2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Double2D
        source array.
    
    Returns
    --------
    output : Double2D
        array copy
    """


@overload
def copy(rx: Double3D) -> Double3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    rx : Double3D
        source array.
    
    Returns
    --------
    output : Double3D
        array copy
    """


@overload
def copy(rx: Double1D, ry: Double1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Double1D
        source array.
    ry : Double1D
        destination array.
    """


@overload
def copy(rx: Double2D, ry: Double2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Double2D
        source array.
    ry : Double2D
        destination array.
    """


@overload
def copy(rx: Double3D, ry: Double3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    rx : Double3D
        source array.
    ry : Double3D
        destination array.
    """


@overload
def copy(n1: int, rx: Double1D) -> Double1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Double1D
        source array.
    
    Returns
    --------
    output : Double1D
        array copy
    """


@overload
def copy(n1: int, n2: int, rx: Double2D) -> Double2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Double2D
        source array.
    
    Returns
    --------
    output : Double2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Double3D) -> Double3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Double3D
        source array.
    
    Returns
    --------
    output : Double3D
        array copy
    """


@overload
def copy(n1: int, rx: Double1D, ry: Double1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    rx : Double1D
        source array.
    ry : Double1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, rx: Double2D, ry: Double2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    rx : Double2D
        source array.
    ry : Double2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, rx: Double3D, ry: Double3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    rx : Double3D
        source array.
    ry : Double3D
        destination array.
    """


@overload
def copy(n1: int, j1: int, rx: Double1D) -> Double1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    rx : Double1D
        source array.
    
    Returns
    --------
    output : Double1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, rx: Double2D) -> Double2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    rx : Double2D
        source array.
    
    Returns
    --------
    output : Double2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int,
         rx: Double3D) -> Double3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    rx : Double3D
        source array.
    
    Returns
    --------
    output : Double3D
        array copy
    """


@overload
def copy(n1: int, j1: int, k1: int, rx: Double1D) -> Double1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    rx : Double1D
        source array.
    
    Returns
    --------
    output : Double1D
        array copy
    """


@overload
def copy(n1: int, n2: int, j1: int, j2: int, k1: int, k2: int,
         rx: Double2D) -> Double2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    rx : Double2D
        source array.
    
    Returns
    --------
    output : Double2D
        array copy
    """


@overload
def copy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int, k1: int,
         k2: int, k3: int, rx: Double3D) -> Double3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of rx.
    j2 : int
        offset in 2nd dimension of rx.
    j3 : int
        offset in 3rd dimension of rx.
    k1 : int
        stride in 1st dimension of rx.
    k2 : int
        stride in 2nd dimension of rx.
    k3 : int
        stride in 3rd dimension of rx.
    rx : Double3D
        source array.
    
    Returns
    --------
    output : Double3D
        array copy
    """


@overload
def copy(n1: int, j1x: int, rx: Double1D, j1y: int, ry: Double1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    rx : Double1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    ry : Double1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, rx: Double2D, j1y: int,
         j2y: int, ry: Double2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    rx : Double2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    ry : Double2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, rx: Double3D,
         j1y: int, j2y: int, j3y: int, ry: Double3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    rx : Double3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    ry : Double3D
        destination array.
    """


@overload
def copy(n1: int, j1x: int, k1x: int, rx: Double1D, j1y: int, k1y: int,
         ry: Double1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    rx : Double1D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    ry : Double1D
        destination array.
    """


@overload
def copy(n1: int, n2: int, j1x: int, j2x: int, k1x: int, k2x: int,
         rx: Double2D, j1y: int, j2y: int, k1y: int, k2y: int,
         ry: Double2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    rx : Double2D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    ry : Double2D
        destination array.
    """


@overload
def copy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, k1x: int,
         k2x: int, k3x: int, rx: Double3D, j1y: int, j2y: int, j3y: int,
         k1y: int, k2y: int, k3y: int, ry: Double3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of rx.
    j2x : int
        offset in 2nd dimension of rx.
    j3x : int
        offset in 3rd dimension of rx.
    k1x : int
        stride in 1st dimension of rx.
    k2x : int
        stride in 2nd dimension of rx.
    k3x : int
        stride in 3rd dimension of rx.
    rx : Double3D
        source array.
    j1y : int
        offset in 1st dimension of ry.
    j2y : int
        offset in 2nd dimension of ry.
    j3y : int
        offset in 3rd dimension of ry.
    k1y : int
        stride in 1st dimension of ry.
    k2y : int
        stride in 2nd dimension of ry.
    k3y : int
        stride in 3rd dimension of ry.
    ry : Double3D
        destination array.
    """


@overload
def ccopy(cx: Double1D) -> Double1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    cx : Double1D
        source array.
    
    Returns
    --------
    output : Double1D
        array copy
    """


@overload
def ccopy(cx: Double2D) -> Double2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    cx : Double2D
        source array.
    
    Returns
    --------
    output : Double2D
        array copy
    """


@overload
def ccopy(cx: Double3D) -> Double3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    cx : Double3D
        source array.
    
    Returns
    --------
    output : Double3D
        array copy
    """


@overload
def ccopy(cx: Double1D, cy: Double1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    cx : Double1D
        source array.
    cy : Double1D
        destination array.
    """


@overload
def ccopy(cx: Double2D, cy: Double2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    cx : Double2D
        source array.
    cy : Double2D
        destination array.
    """


@overload
def ccopy(cx: Double3D, cy: Double3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    cx : Double3D
        source array.
    cy : Double3D
        destination array.
    """


@overload
def ccopy(n1: int, cx: Double1D) -> Double1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    cx : Double1D
        source array.
    
    Returns
    --------
    output : Double1D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, cx: Double2D) -> Double2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    cx : Double2D
        source array.
    
    Returns
    --------
    output : Double2D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, n3: int, cx: Double3D) -> Double3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    cx : Double3D
        source array.
    
    Returns
    --------
    output : Double3D
        array copy
    """


@overload
def ccopy(n1: int, cx: Double1D, cy: Double1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    cx : Double1D
        source array.
    cy : Double1D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, cx: Double2D, cy: Double2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    cx : Double2D
        source array.
    cy : Double2D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, n3: int, cx: Double3D, cy: Double3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    cx : Double3D
        source array.
    cy : Double3D
        destination array.
    """


@overload
def ccopy(n1: int, j1: int, cx: Double1D) -> Double1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of cx.
    cx : Double1D
        source array.
    
    Returns
    --------
    output : Double1D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, j1: int, j2: int, cx: Double2D) -> Double2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of cx.
    j2 : int
        offset in 2nd dimension of cx.
    cx : Double2D
        source array.
    
    Returns
    --------
    output : Double2D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int,
          cx: Double3D) -> Double3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of cx.
    j2 : int
        offset in 2nd dimension of cx.
    j3 : int
        offset in 3rd dimension of cx.
    cx : Double3D
        source array.
    
    Returns
    --------
    output : Double3D
        array copy
    """


@overload
def ccopy(n1: int, j1: int, k1: int, cx: Double1D) -> Double1D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1 : int
        offset in 1st dimension of cx.
    k1 : int
        stride in 1st dimension of cx.
    cx : Double1D
        source array.
    
    Returns
    --------
    output : Double1D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, j1: int, j2: int, k1: int, k2: int,
          cx: Double2D) -> Double2D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1 : int
        offset in 1st dimension of cx.
    j2 : int
        offset in 2nd dimension of cx.
    k1 : int
        stride in 1st dimension of cx.
    k2 : int
        stride in 2nd dimension of cx.
    cx : Double2D
        source array.
    
    Returns
    --------
    output : Double2D
        array copy
    """


@overload
def ccopy(n1: int, n2: int, n3: int, j1: int, j2: int, j3: int, k1: int,
          k2: int, k3: int, cx: Double3D) -> Double3D:
    """
    Returns array copy of elements from the specified array.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1 : int
        offset in 1st dimension of cx.
    j2 : int
        offset in 2nd dimension of cx.
    j3 : int
        offset in 3rd dimension of cx.
    k1 : int
        stride in 1st dimension of cx.
    k2 : int
        stride in 2nd dimension of cx.
    k3 : int
        stride in 3rd dimension of cx.
    cx : Double3D
        source array.
    
    Returns
    --------
    output : Double3D
        array copy
    """


@overload
def ccopy(n1: int, j1x: int, cx: Double1D, j1y: int, cy: Double1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of cx.
    cx : Double1D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    cy : Double1D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, j1x: int, j2x: int, cx: Double2D, j1y: int,
          j2y: int, cy: Double2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of cx.
    j2x : int
        offset in 2nd dimension of cx.
    cx : Double2D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    j2y : int
        offset in 2nd dimension of cy.
    cy : Double2D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int,
          cx: Double3D, j1y: int, j2y: int, j3y: int, cy: Double3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of cx.
    j2x : int
        offset in 2nd dimension of cx.
    j3x : int
        offset in 3rd dimension of cx.
    cx : Double3D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    j2y : int
        offset in 2nd dimension of cy.
    j3y : int
        offset in 3rd dimension of cy.
    cy : Double3D
        destination array.
    """


@overload
def ccopy(n1: int, j1x: int, k1x: int, cx: Double1D, j1y: int, k1y: int,
          cy: Double1D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    j1x : int
        offset in 1st dimension of cx.
    k1x : int
        stride in 1st dimension of cx.
    cx : Double1D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    k1y : int
        stride in 1st dimension of cy.
    cy : Double1D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, j1x: int, j2x: int, k1x: int, k2x: int,
          cx: Double2D, j1y: int, j2y: int, k1y: int, k2y: int,
          cy: Double2D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    j1x : int
        offset in 1st dimension of cx.
    j2x : int
        offset in 2nd dimension of cx.
    k1x : int
        stride in 1st dimension of cx.
    k2x : int
        stride in 2nd dimension of cx.
    cx : Double2D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    j2y : int
        offset in 2nd dimension of cy.
    k1y : int
        stride in 1st dimension of cy.
    k2y : int
        stride in 2nd dimension of cy.
    cy : Double2D
        destination array.
    """


@overload
def ccopy(n1: int, n2: int, n3: int, j1x: int, j2x: int, j3x: int, k1x: int,
          k2x: int, k3x: int, cx: Double3D, j1y: int, j2y: int, j3y: int,
          k1y: int, k2y: int, k3y: int, cy: Double3D) -> None:
    """
    Copies elements from one specified array to another.
    
    Parameters
    -----------
    n1 : int
        number of elements to copy in 1st dimension.
    n2 : int
        number of elements to copy in 2nd dimension.
    n3 : int
        number of elements to copy in 3rd dimension.
    j1x : int
        offset in 1st dimension of cx.
    j2x : int
        offset in 2nd dimension of cx.
    j3x : int
        offset in 3rd dimension of cx.
    k1x : int
        stride in 1st dimension of cx.
    k2x : int
        stride in 2nd dimension of cx.
    k3x : int
        stride in 3rd dimension of cx.
    cx : Double3D
        source array.
    j1y : int
        offset in 1st dimension of cy.
    j2y : int
        offset in 2nd dimension of cy.
    j3y : int
        offset in 3rd dimension of cy.
    k1y : int
        stride in 1st dimension of cy.
    k2y : int
        stride in 2nd dimension of cy.
    k3y : int
        stride in 3rd dimension of cy.
    cy : Double3D
        destination array.
    """


@overload
def reverse(rx: Byte1D) -> Byte1D:
    """

    """


@overload
def reverse(rx: Byte1D, ry: Byte1D) -> None:
    """

    """


@overload
def reverse(rx: Short1D) -> Short1D:
    """

    """


@overload
def reverse(rx: Short1D, ry: Short1D) -> None:
    """

    """


@overload
def reverse(rx: Int1D) -> Int1D:
    """

    """


@overload
def reverse(rx: Int1D, ry: Int1D) -> None:
    """

    """


@overload
def reverse(rx: Long1D) -> Long1D:
    """

    """


@overload
def reverse(rx: Long1D, ry: Long1D) -> None:
    """

    """


@overload
def reverse(rx: Float1D) -> Float1D:
    """

    """


@overload
def reverse(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def creverse(rx: Float1D) -> Float1D:
    """

    """


@overload
def creverse(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def reverse(rx: Double1D) -> Double1D:
    """

    """


@overload
def reverse(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def creverse(rx: Double1D) -> Double1D:
    """

    """


@overload
def creverse(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def flatten(rx: Byte2D) -> Byte1D:
    """
    Flattens a specified 2-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Byte2D
        the array.
    
    Returns
    --------
    output : Byte1D
        the flattened array.
    """


@overload
def flatten(rx: Byte3D) -> Byte1D:
    """
    Flattens a specified 3-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Byte3D
        the array.
    
    Returns
    --------
    output : Byte1D
        the flattened array.
    """


@overload
def flatten(rx: Short2D) -> Short1D:
    """
    Flattens a specified 2-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Short2D
        the array.
    
    Returns
    --------
    output : Short1D
        the flattened array.
    """


@overload
def flatten(rx: Short3D) -> Short1D:
    """
    Flattens a specified 3-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Short3D
        the array.
    
    Returns
    --------
    output : Short1D
        the flattened array.
    """


@overload
def flatten(rx: Int2D) -> Int1D:
    """
    Flattens a specified 2-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Int2D
        the array.
    
    Returns
    --------
    output : Int1D
        the flattened array.
    """


@overload
def flatten(rx: Int3D) -> Int1D:
    """
    Flattens a specified 3-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Int3D
        the array.
    
    Returns
    --------
    output : Int1D
        the flattened array.
    """


@overload
def flatten(rx: Long2D) -> Long1D:
    """
    Flattens a specified 2-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Long2D
        the array.
    
    Returns
    --------
    output : Long1D
        the flattened array.
    """


@overload
def flatten(rx: Long3D) -> Long1D:
    """
    Flattens a specified 3-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Long3D
        the array.
    
    Returns
    --------
    output : Long1D
        the flattened array.
    """


@overload
def flatten(rx: Float2D) -> Float1D:
    """
    Flattens a specified 2-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Float2D
        the array.
    
    Returns
    --------
    output : Float1D
        the flattened array.
    """


@overload
def flatten(rx: Float3D) -> Float1D:
    """
    Flattens a specified 3-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Float3D
        the array.
    
    Returns
    --------
    output : Float1D
        the flattened array.
    """


@overload
def cflatten(cx: Float2D) -> Float1D:
    """
    Flattens a specified 2-D array into a 1-D array.
    
    Parameters
    -----------
    cx : Float2D
        the array.
    
    Returns
    --------
    output : Float1D
        the flattened array.
    """


@overload
def cflatten(cx: Float3D) -> Float1D:
    """
    Flattens a specified 3-D array into a 1-D array.
    
    Parameters
    -----------
    cx : Float3D
        the array.
    
    Returns
    --------
    output : Float1D
        the flattened array.
    """


@overload
def flatten(rx: Double2D) -> Double1D:
    """
    Flattens a specified 2-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Double2D
        the array.
    
    Returns
    --------
    output : Double1D
        the flattened array.
    """


@overload
def flatten(rx: Double3D) -> Double1D:
    """
    Flattens a specified 3-D array into a 1-D array.
    
    Parameters
    -----------
    rx : Double3D
        the array.
    
    Returns
    --------
    output : Double1D
        the flattened array.
    """


@overload
def cflatten(cx: Double2D) -> Double1D:
    """
    Flattens a specified 2-D array into a 1-D array.
    
    Parameters
    -----------
    cx : Double2D
        the array.
    
    Returns
    --------
    output : Double1D
        the flattened array.
    """


@overload
def cflatten(cx: Double3D) -> Double1D:
    """
    Flattens a specified 3-D array into a 1-D array.
    
    Parameters
    -----------
    cx : Double3D
        the array.
    
    Returns
    --------
    output : Double1D
        the flattened array.
    """


@overload
def reshape(n1: int, n2: int, rx: Byte1D) -> Byte2D:
    """
    Reshapes a 1-D array into a 2-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    rx : Byte1D
        the array.
    
    Returns
    --------
    output : Byte2D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, n3: int, rx: Byte1D) -> Byte3D:
    """
    Reshapes a 1-D array into a 3-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    n3 : int
        the 3rd dimension of the reshaped array.
    rx : Byte1D
        the array.
    
    Returns
    --------
    output : Byte3D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, rx: Short1D) -> Short2D:
    """
    Reshapes a 1-D array into a 2-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    rx : Short1D
        the array.
    
    Returns
    --------
    output : Short2D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, n3: int, rx: Short1D) -> Short3D:
    """
    Reshapes a 1-D array into a 3-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    n3 : int
        the 3rd dimension of the reshaped array.
    rx : Short1D
        the array.
    
    Returns
    --------
    output : Short3D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, rx: Int1D) -> Int2D:
    """
    Reshapes a 1-D array into a 2-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    rx : Int1D
        the array.
    
    Returns
    --------
    output : Int2D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, n3: int, rx: Int1D) -> Int3D:
    """
    Reshapes a 1-D array into a 3-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    n3 : int
        the 3rd dimension of the reshaped array.
    rx : Int1D
        the array.
    
    Returns
    --------
    output : Int3D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, rx: Long1D) -> Long2D:
    """
    Reshapes a 1-D array into a 2-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    rx : Long1D
        the array.
    
    Returns
    --------
    output : Long2D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, n3: int, rx: Long1D) -> Long3D:
    """
    Reshapes a 1-D array into a 3-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    n3 : int
        the 3rd dimension of the reshaped array.
    rx : Long1D
        the array.
    
    Returns
    --------
    output : Long3D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, rx: Float1D) -> Float2D:
    """
    Reshapes a 1-D array into a 2-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    rx : Float1D
        the array.
    
    Returns
    --------
    output : Float2D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, n3: int, rx: Float1D) -> Float3D:
    """
    Reshapes a 1-D array into a 3-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    n3 : int
        the 3rd dimension of the reshaped array.
    rx : Float1D
        the array.
    
    Returns
    --------
    output : Float3D
        the reshaped array.
    """


@overload
def creshape(n1: int, n2: int, cx: Float1D) -> Float2D:
    """
    Reshapes a 1-D array into a 2-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    cx : Float1D
        the array.
    
    Returns
    --------
    output : Float2D
        the reshaped array.
    """


@overload
def creshape(n1: int, n2: int, n3: int, cx: Float1D) -> Float3D:
    """
    Reshapes a 1-D array into a 3-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    n3 : int
        the 3rd dimension of the reshaped array.
    cx : Float1D
        the array.
    
    Returns
    --------
    output : Float3D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, rx: Double1D) -> Double2D:
    """
    Reshapes a 1-D array into a 2-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    rx : Double1D
        the array.
    
    Returns
    --------
    output : Double2D
        the reshaped array.
    """


@overload
def reshape(n1: int, n2: int, n3: int, rx: Double1D) -> Double3D:
    """
    Reshapes a 1-D array into a 3-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    n3 : int
        the 3rd dimension of the reshaped array.
    rx : Double1D
        the array.
    
    Returns
    --------
    output : Double3D
        the reshaped array.
    """


@overload
def creshape(n1: int, n2: int, cx: Double1D) -> Double2D:
    """
    Reshapes a 1-D array into a 2-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    cx : Double1D
        the array.
    
    Returns
    --------
    output : Double2D
        the reshaped array.
    """


@overload
def creshape(n1: int, n2: int, n3: int, cx: Double1D) -> Double3D:
    """
    Reshapes a 1-D array into a 3-D array with specified dimensions.
    
    Parameters
    -----------
    n1 : int
        the 1st dimension of the reshaped array.
    n2 : int
        the 2nd dimension of the reshaped array.
    n3 : int
        the 3rd dimension of the reshaped array.
    cx : Double1D
        the array.
    
    Returns
    --------
    output : Double3D
        the reshaped array.
    """


@overload
def transpose(rx: Byte2D) -> Byte2D:
    """
    Transpose the specified 2-D array.
    
    Parameters
    -----------
    rx : Byte2D
        the array; must be regular.
    
    Returns
    --------
    output : Byte2D
        the transposed array.
    """


@overload
def transpose(rx: Short2D) -> Short2D:
    """
    Transpose the specified 2-D array.
    
    Parameters
    -----------
    rx : Short2D
        the array; must be regular.
    
    Returns
    --------
    output : Short2D
        the transposed array.
    """


@overload
def transpose(rx: Int2D) -> Int2D:
    """
    Transpose the specified 2-D array.
    
    Parameters
    -----------
    rx : Int2D
        the array; must be regular.
    
    Returns
    --------
    output : Int2D
        the transposed array.
    """


@overload
def transpose(rx: Long2D) -> Long2D:
    """
    Transpose the specified 2-D array.
    
    Parameters
    -----------
    rx : Long2D
        the array; must be regular.
    
    Returns
    --------
    output : Long2D
        the transposed array.
    """


@overload
def transpose(rx: Float2D) -> Float2D:
    """
    Transpose the specified 2-D array.
    
    Parameters
    -----------
    rx : Float2D
        the array; must be regular.
    
    Returns
    --------
    output : Float2D
        the transposed array.
    """


@overload
def ctranspose(cx: Float2D) -> Float2D:
    """
    Transpose the specified 2-D array.
    
    Parameters
    -----------
    cx : Float2D
        the array; must be regular.
    
    Returns
    --------
    output : Float2D
        the transposed array.
    """


@overload
def transpose(rx: Double2D) -> Double2D:
    """
    Transpose the specified 2-D array.
    
    Parameters
    -----------
    rx : Double2D
        the array; must be regular.
    
    Returns
    --------
    output : Double2D
        the transposed array.
    """


@overload
def ctranspose(cx: Double2D) -> Double2D:
    """
    Transpose the specified 2-D array.
    
    Parameters
    -----------
    cx : Double2D
        the array; must be regular.
    
    Returns
    --------
    output : Double2D
        the transposed array.
    """


@overload
def distinct(x: Byte1D, y: Byte1D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Byte1D
        an array.
    y : Byte1D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Byte2D, y: Byte2D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Byte2D
        an array.
    y : Byte2D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Byte3D, y: Byte3D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Byte3D
        an array.
    y : Byte3D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Short1D, y: Short1D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Short1D
        an array.
    y : Short1D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Short2D, y: Short2D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Short2D
        an array.
    y : Short2D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Short3D, y: Short3D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Short3D
        an array.
    y : Short3D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Int1D, y: Int1D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Int1D
        an array.
    y : Int1D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Int2D, y: Int2D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Int2D
        an array.
    y : Int2D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Int3D, y: Int3D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Int3D
        an array.
    y : Int3D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Long1D, y: Long1D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Long1D
        an array.
    y : Long1D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Long2D, y: Long2D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Long2D
        an array.
    y : Long2D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Long3D, y: Long3D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Long3D
        an array.
    y : Long3D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Float1D, y: Float1D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Float1D
        an array.
    y : Float1D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Float2D, y: Float2D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Float2D
        an array.
    y : Float2D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Float3D, y: Float3D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Float3D
        an array.
    y : Float3D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Double1D, y: Double1D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Double1D
        an array.
    y : Double1D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Double2D, y: Double2D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Double2D
        an array.
    y : Double2D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def distinct(x: Double3D, y: Double3D) -> bool:
    """
    Determines whether the two specified arrays are distinct.
    
    Parameters
    -----------
    x : Double3D
        an array.
    y : Double3D
        an array.
    
    Returns
    --------
    output : bool
        true, if distinct; false, otherwise.
    """


@overload
def equal(rx: Byte1D, ry: Byte1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Byte1D
        an array.
    ry : Byte1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Byte2D, ry: Byte2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Byte2D
        an array.
    ry : Byte2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Byte3D, ry: Byte3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Byte3D
        an array.
    ry : Byte3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Short1D, ry: Short1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Short1D
        an array.
    ry : Short1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Short2D, ry: Short2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Short2D
        an array.
    ry : Short2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Short3D, ry: Short3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Short3D
        an array.
    ry : Short3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Int1D, ry: Int1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Int1D
        an array.
    ry : Int1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Int2D, ry: Int2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Int2D
        an array.
    ry : Int2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Int3D, ry: Int3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Int3D
        an array.
    ry : Int3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Long1D, ry: Long1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Long1D
        an array.
    ry : Long1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Long2D, ry: Long2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Long2D
        an array.
    ry : Long2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Long3D, ry: Long3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Long3D
        an array.
    ry : Long3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Float1D, ry: Float1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Float1D
        an array.
    ry : Float1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Float2D, ry: Float2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Float2D
        an array.
    ry : Float2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Float3D, ry: Float3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Float3D
        an array.
    ry : Float3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(tolerance: float, rx: Float1D, ry: Float1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : float
        the tolerance.
    rx : Float1D
        an array.
    ry : Float1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(tolerance: float, rx: Float2D, ry: Float2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : float
        the tolerance.
    rx : Float2D
        an array.
    ry : Float2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(tolerance: float, rx: Float3D, ry: Float3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : float
        the tolerance.
    rx : Float3D
        an array.
    ry : Float3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(cx: Float1D, cy: Float1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    cx : Float1D
        an array.
    cy : Float1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(cx: Float2D, cy: Float2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    cx : Float2D
        an array.
    cy : Float2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(cx: Float3D, cy: Float3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    cx : Float3D
        an array.
    cy : Float3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(tolerance: float, cx: Float1D, cy: Float1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : float
        the tolerance.
    cx : Float1D
        an array.
    cy : Float1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(tolerance: float, cx: Float2D, cy: Float2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : float
        the tolerance.
    cx : Float2D
        an array.
    cy : Float2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(tolerance: float, cx: Float3D, cy: Float3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : float
        the tolerance.
    cx : Float3D
        an array.
    cy : Float3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Double1D, ry: Double1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Double1D
        an array.
    ry : Double1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Double2D, ry: Double2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Double2D
        an array.
    ry : Double2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(rx: Double3D, ry: Double3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    rx : Double3D
        an array.
    ry : Double3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(tolerance: double, rx: Double1D, ry: Double1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : double
        the tolerance.
    rx : Double1D
        an array.
    ry : Double1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(tolerance: double, rx: Double2D, ry: Double2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : double
        the tolerance.
    rx : Double2D
        an array.
    ry : Double2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def equal(tolerance: double, rx: Double3D, ry: Double3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : double
        the tolerance.
    rx : Double3D
        an array.
    ry : Double3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(cx: Double1D, cy: Double1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    cx : Double1D
        an array.
    cy : Double1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(cx: Double2D, cy: Double2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    cx : Double2D
        an array.
    cy : Double2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(cx: Double3D, cy: Double3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal.
    
    Parameters
    -----------
    cx : Double3D
        an array.
    cy : Double3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(tolerance: double, cx: Double1D, cy: Double1D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : double
        the tolerance.
    cx : Double1D
        an array.
    cy : Double1D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(tolerance: double, cx: Double2D, cy: Double2D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : double
        the tolerance.
    cx : Double2D
        an array.
    cy : Double2D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def cequal(tolerance: double, cx: Double3D, cy: Double3D) -> bool:
    """
    Determines whether all elements in two specified arrays are equal,
    to within a specified tolerance.
    
    Parameters
    -----------
    tolerance : double
        the tolerance.
    cx : Double3D
        an array.
    cy : Double3D
        an array.
    
    Returns
    --------
    output : bool
        true, if equal; false, otherwise.
    """


@overload
def isRegular(a: Byte2D) -> bool:
    """
    Determines whether the specified array of arrays is regular. The array
    is regular if each of its elements, which are arrays, have the same
    length.
    
    Parameters
    -----------
    a : Byte2D
        the array.
    
    Returns
    --------
    output : bool
        true, if regular; false, otherwise.
    """


@overload
def isRegular(a: Byte3D) -> bool:
    """
    Determines whether the specified array of arrays of arrays is regular.
    The array is regular if each of its elements, which are arrays of arrays,
    has the same length and is regular.
    
    Parameters
    -----------
    a : Byte3D
        the array.
    
    Returns
    --------
    output : bool
        true, if regular; false, otherwise.
    """


@overload
def isRegular(a: Short2D) -> bool:
    """
    Determines whether the specified array of arrays is regular. The array
    is regular if each of its elements, which are arrays, have the same
    length.
    
    Parameters
    -----------
    a : Short2D
        the array.
    
    Returns
    --------
    output : bool
        true, if regular; false, otherwise.
    """


@overload
def isRegular(a: Short3D) -> bool:
    """
    Determines whether the specified array of arrays of arrays is regular.
    The array is regular if each of its elements, which are arrays of arrays,
    has the same length and is regular.
    
    Parameters
    -----------
    a : Short3D
        the array.
    
    Returns
    --------
    output : bool
        true, if regular; false, otherwise.
    """


@overload
def isRegular(a: Int2D) -> bool:
    """
    Determines whether the specified array of arrays is regular. The array
    is regular if each of its elements, which are arrays, have the same
    length.
    
    Parameters
    -----------
    a : Int2D
        the array.
    
    Returns
    --------
    output : bool
        true, if regular; false, otherwise.
    """


@overload
def isRegular(a: Int3D) -> bool:
    """
    Determines whether the specified array of arrays of arrays is regular.
    The array is regular if each of its elements, which are arrays of arrays,
    has the same length and is regular.
    
    Parameters
    -----------
    a : Int3D
        the array.
    
    Returns
    --------
    output : bool
        true, if regular; false, otherwise.
    """


@overload
def isRegular(a: Float2D) -> bool:
    """
    Determines whether the specified array of arrays is regular. The array
    is regular if each of its elements, which are arrays, have the same
    length.
    
    Parameters
    -----------
    a : Float2D
        the array.
    
    Returns
    --------
    output : bool
        true, if regular; false, otherwise.
    """


@overload
def isRegular(a: Float3D) -> bool:
    """
    Determines whether the specified array of arrays of arrays is regular.
    The array is regular if each of its elements, which are arrays of arrays,
    has the same length and is regular.
    
    Parameters
    -----------
    a : Float3D
        the array.
    
    Returns
    --------
    output : bool
        true, if regular; false, otherwise.
    """


@overload
def isRegular(a: Double2D) -> bool:
    """
    Determines whether the specified array of arrays is regular. The array
    is regular if each of its elements, which are arrays, have the same
    length.
    
    Parameters
    -----------
    a : Double2D
        the array.
    
    Returns
    --------
    output : bool
        true, if regular; false, otherwise.
    """


@overload
def isRegular(a: Double3D) -> bool:
    """
    Determines whether the specified array of arrays of arrays is regular.
    The array is regular if each of its elements, which are arrays of arrays,
    has the same length and is regular.
    
    Parameters
    -----------
    a : Double3D
        the array.
    
    Returns
    --------
    output : bool
        true, if regular; false, otherwise.
    """


@overload
def isIncreasing(a: Byte1D) -> bool:
    """
    Determines whether the specified array is increasing. The array is
    increasing if its elements a[i] increase with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Byte1D
        the array.
    
    Returns
    --------
    output : bool
        true, if increasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isDecreasing(a: Byte1D) -> bool:
    """
    Determines whether the specified array is decreasing. The array is
    decreasing if its elements a[i] decrease with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Byte1D
        the array.
    
    Returns
    --------
    output : bool
        true, if decreasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isMonotonic(a: Byte1D) -> bool:
    """
    Determines whether the specified array is monotonic. The array is
    monotonic if its elements a[i] either increase or decrease (but
    not both) with array index i, with no equal values.
    
    Parameters
    -----------
    a : Byte1D
        the array.
    
    Returns
    --------
    output : bool
        true, if monotonic (or a.length&lt;2); false, otherwise.
    """


@overload
def isIncreasing(a: Short1D) -> bool:
    """
    Determines whether the specified array is increasing. The array is
    increasing if its elements a[i] increase with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Short1D
        the array.
    
    Returns
    --------
    output : bool
        true, if increasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isDecreasing(a: Short1D) -> bool:
    """
    Determines whether the specified array is decreasing. The array is
    decreasing if its elements a[i] decrease with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Short1D
        the array.
    
    Returns
    --------
    output : bool
        true, if decreasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isMonotonic(a: Short1D) -> bool:
    """
    Determines whether the specified array is monotonic. The array is
    monotonic if its elements a[i] either increase or decrease (but
    not both) with array index i, with no equal values.
    
    Parameters
    -----------
    a : Short1D
        the array.
    
    Returns
    --------
    output : bool
        true, if monotonic (or a.length&lt;2); false, otherwise.
    """


@overload
def isIncreasing(a: Int1D) -> bool:
    """
    Determines whether the specified array is increasing. The array is
    increasing if its elements a[i] increase with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Int1D
        the array.
    
    Returns
    --------
    output : bool
        true, if increasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isDecreasing(a: Int1D) -> bool:
    """
    Determines whether the specified array is decreasing. The array is
    decreasing if its elements a[i] decrease with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Int1D
        the array.
    
    Returns
    --------
    output : bool
        true, if decreasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isMonotonic(a: Int1D) -> bool:
    """
    Determines whether the specified array is monotonic. The array is
    monotonic if its elements a[i] either increase or decrease (but
    not both) with array index i, with no equal values.
    
    Parameters
    -----------
    a : Int1D
        the array.
    
    Returns
    --------
    output : bool
        true, if monotonic (or a.length&lt;2); false, otherwise.
    """


@overload
def isIncreasing(a: Long1D) -> bool:
    """
    Determines whether the specified array is increasing. The array is
    increasing if its elements a[i] increase with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Long1D
        the array.
    
    Returns
    --------
    output : bool
        true, if increasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isDecreasing(a: Long1D) -> bool:
    """
    Determines whether the specified array is decreasing. The array is
    decreasing if its elements a[i] decrease with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Long1D
        the array.
    
    Returns
    --------
    output : bool
        true, if decreasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isMonotonic(a: Long1D) -> bool:
    """
    Determines whether the specified array is monotonic. The array is
    monotonic if its elements a[i] either increase or decrease (but
    not both) with array index i, with no equal values.
    
    Parameters
    -----------
    a : Long1D
        the array.
    
    Returns
    --------
    output : bool
        true, if monotonic (or a.length&lt;2); false, otherwise.
    """


@overload
def isIncreasing(a: Float1D) -> bool:
    """
    Determines whether the specified array is increasing. The array is
    increasing if its elements a[i] increase with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Float1D
        the array.
    
    Returns
    --------
    output : bool
        true, if increasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isDecreasing(a: Float1D) -> bool:
    """
    Determines whether the specified array is decreasing. The array is
    decreasing if its elements a[i] decrease with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Float1D
        the array.
    
    Returns
    --------
    output : bool
        true, if decreasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isMonotonic(a: Float1D) -> bool:
    """
    Determines whether the specified array is monotonic. The array is
    monotonic if its elements a[i] either increase or decrease (but
    not both) with array index i, with no equal values.
    
    Parameters
    -----------
    a : Float1D
        the array.
    
    Returns
    --------
    output : bool
        true, if monotonic (or a.length&lt;2); false, otherwise.
    """


@overload
def isIncreasing(a: Double1D) -> bool:
    """
    Determines whether the specified array is increasing. The array is
    increasing if its elements a[i] increase with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Double1D
        the array.
    
    Returns
    --------
    output : bool
        true, if increasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isDecreasing(a: Double1D) -> bool:
    """
    Determines whether the specified array is decreasing. The array is
    decreasing if its elements a[i] decrease with array index i, with
    no equal values.
    
    Parameters
    -----------
    a : Double1D
        the array.
    
    Returns
    --------
    output : bool
        true, if decreasing (or a.length&lt;2); false, otherwise.
    """


@overload
def isMonotonic(a: Double1D) -> bool:
    """
    Determines whether the specified array is monotonic. The array is
    monotonic if its elements a[i] either increase or decrease (but
    not both) with array index i, with no equal values.
    
    Parameters
    -----------
    a : Double1D
        the array.
    
    Returns
    --------
    output : bool
        true, if monotonic (or a.length&lt;2); false, otherwise.
    """


@overload
def quickSort(a: Byte1D) -> None:
    """
    Sorts the elements of the specified array in ascending order.
    After sorting, a[0] &lt;= a[1] &lt;= a[2] &lt;= ....
    
    Parameters
    -----------
    a : Byte1D
        the array to be sorted.
    """


@overload
def quickIndexSort(a: Byte1D, i: Int1D) -> None:
    """
    Sorts indices of the elements of the specified array in ascending order.
    After sorting, a[i[0]] &lt;= a[i[1]] &lt;= a[i[2]] &lt;= ....
    
    Parameters
    -----------
    a : Byte1D
        the array.
    i : Int1D
        the indices to be sorted.
    """


@overload
def quickPartialSort(k: int, a: Byte1D) -> None:
    """
    Partially sorts the elements of the specified array in ascending order.
    After partial sorting, the element a[k] with specified index k has the
    value it would have if the array were completely sorted. That is,
    a[0:k-1] &lt;= a[k] &lt;= a[k:n-1], where n is the length of a.
    
    Parameters
    -----------
    k : int
        the index.
    a : Byte1D
        the array to be partially sorted.
    """


@overload
def quickPartialIndexSort(k: int, a: Byte1D, i: Int1D) -> None:
    """
    Partially sorts indices of the elements of the specified array.
    After partial sorting, the element i[k] with specified index k has the
    value it would have if the indices were completely sorted. That is,
    a[i[0:k-1]] &lt;= a[i[k]] &lt;= a[i[k:n-1]], where n is the length of i.
    
    Parameters
    -----------
    k : int
        the index.
    a : Byte1D
        the array.
    i : Int1D
        the indices to be partially sorted.
    """


@overload
def quickSort(a: Short1D) -> None:
    """
    Sorts the elements of the specified array in ascending order.
    After sorting, a[0] &lt;= a[1] &lt;= a[2] &lt;= ....
    
    Parameters
    -----------
    a : Short1D
        the array to be sorted.
    """


@overload
def quickIndexSort(a: Short1D, i: Int1D) -> None:
    """
    Sorts indices of the elements of the specified array in ascending order.
    After sorting, a[i[0]] &lt;= a[i[1]] &lt;= a[i[2]] &lt;= ....
    
    Parameters
    -----------
    a : Short1D
        the array.
    i : Int1D
        the indices to be sorted.
    """


@overload
def quickPartialSort(k: int, a: Short1D) -> None:
    """
    Partially sorts the elements of the specified array in ascending order.
    After partial sorting, the element a[k] with specified index k has the
    value it would have if the array were completely sorted. That is,
    a[0:k-1] &lt;= a[k] &lt;= a[k:n-1], where n is the length of a.
    
    Parameters
    -----------
    k : int
        the index.
    a : Short1D
        the array to be partially sorted.
    """


@overload
def quickPartialIndexSort(k: int, a: Short1D, i: Int1D) -> None:
    """
    Partially sorts indices of the elements of the specified array.
    After partial sorting, the element i[k] with specified index k has the
    value it would have if the indices were completely sorted. That is,
    a[i[0:k-1]] &lt;= a[i[k]] &lt;= a[i[k:n-1]], where n is the length of i.
    
    Parameters
    -----------
    k : int
        the index.
    a : Short1D
        the array.
    i : Int1D
        the indices to be partially sorted.
    """


@overload
def quickSort(a: Int1D) -> None:
    """
    Sorts the elements of the specified array in ascending order.
    After sorting, a[0] &lt;= a[1] &lt;= a[2] &lt;= ....
    
    Parameters
    -----------
    a : Int1D
        the array to be sorted.
    """


@overload
def quickIndexSort(a: Int1D, i: Int1D) -> None:
    """
    Sorts indices of the elements of the specified array in ascending order.
    After sorting, a[i[0]] &lt;= a[i[1]] &lt;= a[i[2]] &lt;= ....
    
    Parameters
    -----------
    a : Int1D
        the array.
    i : Int1D
        the indices to be sorted.
    """


@overload
def quickPartialSort(k: int, a: Int1D) -> None:
    """
    Partially sorts the elements of the specified array in ascending order.
    After partial sorting, the element a[k] with specified index k has the
    value it would have if the array were completely sorted. That is,
    a[0:k-1] &lt;= a[k] &lt;= a[k:n-1], where n is the length of a.
    
    Parameters
    -----------
    k : int
        the index.
    a : Int1D
        the array to be partially sorted.
    """


@overload
def quickPartialIndexSort(k: int, a: Int1D, i: Int1D) -> None:
    """
    Partially sorts indices of the elements of the specified array.
    After partial sorting, the element i[k] with specified index k has the
    value it would have if the indices were completely sorted. That is,
    a[i[0:k-1]] &lt;= a[i[k]] &lt;= a[i[k:n-1]], where n is the length of i.
    
    Parameters
    -----------
    k : int
        the index.
    a : Int1D
        the array.
    i : Int1D
        the indices to be partially sorted.
    """


@overload
def quickSort(a: Long1D) -> None:
    """
    Sorts the elements of the specified array in ascending order.
    After sorting, a[0] &lt;= a[1] &lt;= a[2] &lt;= ....
    
    Parameters
    -----------
    a : Long1D
        the array to be sorted.
    """


@overload
def quickIndexSort(a: Long1D, i: Int1D) -> None:
    """
    Sorts indices of the elements of the specified array in ascending order.
    After sorting, a[i[0]] &lt;= a[i[1]] &lt;= a[i[2]] &lt;= ....
    
    Parameters
    -----------
    a : Long1D
        the array.
    i : Int1D
        the indices to be sorted.
    """


@overload
def quickPartialSort(k: int, a: Long1D) -> None:
    """
    Partially sorts the elements of the specified array in ascending order.
    After partial sorting, the element a[k] with specified index k has the
    value it would have if the array were completely sorted. That is,
    a[0:k-1] &lt;= a[k] &lt;= a[k:n-1], where n is the length of a.
    
    Parameters
    -----------
    k : int
        the index.
    a : Long1D
        the array to be partially sorted.
    """


@overload
def quickPartialIndexSort(k: int, a: Long1D, i: Int1D) -> None:
    """
    Partially sorts indices of the elements of the specified array.
    After partial sorting, the element i[k] with specified index k has the
    value it would have if the indices were completely sorted. That is,
    a[i[0:k-1]] &lt;= a[i[k]] &lt;= a[i[k:n-1]], where n is the length of i.
    
    Parameters
    -----------
    k : int
        the index.
    a : Long1D
        the array.
    i : Int1D
        the indices to be partially sorted.
    """


@overload
def quickSort(a: Float1D) -> None:
    """
    Sorts the elements of the specified array in ascending order.
    After sorting, a[0] &lt;= a[1] &lt;= a[2] &lt;= ....
    
    Parameters
    -----------
    a : Float1D
        the array to be sorted.
    """


@overload
def quickIndexSort(a: Float1D, i: Int1D) -> None:
    """
    Sorts indices of the elements of the specified array in ascending order.
    After sorting, a[i[0]] &lt;= a[i[1]] &lt;= a[i[2]] &lt;= ....
    
    Parameters
    -----------
    a : Float1D
        the array.
    i : Int1D
        the indices to be sorted.
    """


@overload
def quickPartialSort(k: int, a: Float1D) -> None:
    """
    Partially sorts the elements of the specified array in ascending order.
    After partial sorting, the element a[k] with specified index k has the
    value it would have if the array were completely sorted. That is,
    a[0:k-1] &lt;= a[k] &lt;= a[k:n-1], where n is the length of a.
    
    Parameters
    -----------
    k : int
        the index.
    a : Float1D
        the array to be partially sorted.
    """


@overload
def quickPartialIndexSort(k: int, a: Float1D, i: Int1D) -> None:
    """
    Partially sorts indices of the elements of the specified array.
    After partial sorting, the element i[k] with specified index k has the
    value it would have if the indices were completely sorted. That is,
    a[i[0:k-1]] &lt;= a[i[k]] &lt;= a[i[k:n-1]], where n is the length of i.
    
    Parameters
    -----------
    k : int
        the index.
    a : Float1D
        the array.
    i : Int1D
        the indices to be partially sorted.
    """


@overload
def quickSort(a: Double1D) -> None:
    """
    Sorts the elements of the specified array in ascending order.
    After sorting, a[0] &lt;= a[1] &lt;= a[2] &lt;= ....
    
    Parameters
    -----------
    a : Double1D
        the array to be sorted.
    """


@overload
def quickIndexSort(a: Double1D, i: Int1D) -> None:
    """
    Sorts indices of the elements of the specified array in ascending order.
    After sorting, a[i[0]] &lt;= a[i[1]] &lt;= a[i[2]] &lt;= ....
    
    Parameters
    -----------
    a : Double1D
        the array.
    i : Int1D
        the indices to be sorted.
    """


@overload
def quickPartialSort(k: int, a: Double1D) -> None:
    """
    Partially sorts the elements of the specified array in ascending order.
    After partial sorting, the element a[k] with specified index k has the
    value it would have if the array were completely sorted. That is,
    a[0:k-1] &lt;= a[k] &lt;= a[k:n-1], where n is the length of a.
    
    Parameters
    -----------
    k : int
        the index.
    a : Double1D
        the array to be partially sorted.
    """


@overload
def quickPartialIndexSort(k: int, a: Double1D, i: Int1D) -> None:
    """
    Partially sorts indices of the elements of the specified array.
    After partial sorting, the element i[k] with specified index k has the
    value it would have if the indices were completely sorted. That is,
    a[i[0:k-1]] &lt;= a[i[k]] &lt;= a[i[k:n-1]], where n is the length of i.
    
    Parameters
    -----------
    k : int
        the index.
    a : Double1D
        the array.
    i : Int1D
        the indices to be partially sorted.
    """


@overload
def binarySearch(a: Byte1D, x: byte) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Byte1D
        the array of values, assumed to be monotonic.
    x : byte
        the value for which to search.
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Byte1D, x: byte, i: int) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    This method is most efficient when called repeatedly for slightly
    changing search values; in such cases, the index returned from one
    call should be passed in the next.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    method interprets this index as if returned from a previous call.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Byte1D
        the array of values, assumed to be monotonic.
    x : byte
        the value for which to search.
    i : int
        the index at which to begin the search. If negative, this
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Short1D, x: short) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Short1D
        the array of values, assumed to be monotonic.
    x : short
        the value for which to search.
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Short1D, x: short, i: int) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    This method is most efficient when called repeatedly for slightly
    changing search values; in such cases, the index returned from one
    call should be passed in the next.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    method interprets this index as if returned from a previous call.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Short1D
        the array of values, assumed to be monotonic.
    x : short
        the value for which to search.
    i : int
        the index at which to begin the search. If negative, this
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Int1D, x: int) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Int1D
        the array of values, assumed to be monotonic.
    x : int
        the value for which to search.
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Int1D, x: int, i: int) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    This method is most efficient when called repeatedly for slightly
    changing search values; in such cases, the index returned from one
    call should be passed in the next.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    method interprets this index as if returned from a previous call.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Int1D
        the array of values, assumed to be monotonic.
    x : int
        the value for which to search.
    i : int
        the index at which to begin the search. If negative, this
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Long1D, x: long) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Long1D
        the array of values, assumed to be monotonic.
    x : long
        the value for which to search.
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Long1D, x: long, i: int) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    This method is most efficient when called repeatedly for slightly
    changing search values; in such cases, the index returned from one
    call should be passed in the next.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    method interprets this index as if returned from a previous call.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Long1D
        the array of values, assumed to be monotonic.
    x : long
        the value for which to search.
    i : int
        the index at which to begin the search. If negative, this
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Float1D, x: float) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Float1D
        the array of values, assumed to be monotonic.
    x : float
        the value for which to search.
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Float1D, x: float, i: int) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    This method is most efficient when called repeatedly for slightly
    changing search values; in such cases, the index returned from one
    call should be passed in the next.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    method interprets this index as if returned from a previous call.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Float1D
        the array of values, assumed to be monotonic.
    x : float
        the value for which to search.
    i : int
        the index at which to begin the search. If negative, this
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Double1D, x: double) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Double1D
        the array of values, assumed to be monotonic.
    x : double
        the value for which to search.
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def binarySearch(a: Double1D, x: double, i: int) -> int:
    """
    Performs a binary search in a monotonic array of values. Values are
    assumed to increase or decrease monotonically, with no equal values.
    This method is most efficient when called repeatedly for slightly
    changing search values; in such cases, the index returned from one
    call should be passed in the next.
    
    Warning: this method does not ensure that the specified array is
    monotonic; that check would be more costly than this search.
    method interprets this index as if returned from a previous call.
    found, -(i+1), where i equals the index at which the specified value
    would be located if it was inserted into the monotonic array.
    
    Parameters
    -----------
    a : Double1D
        the array of values, assumed to be monotonic.
    x : double
        the value for which to search.
    i : int
        the index at which to begin the search. If negative, this
    
    Returns
    --------
    output : int
        the index at which the specified value is found, or, if not
    """


@overload
def add(rx: Float1D, ry: Float1D) -> Float1D:
    """

    """


@overload
def add(ra: float, ry: Float1D) -> Float1D:
    """

    """


@overload
def add(rx: Float1D, rb: float) -> Float1D:
    """

    """


@overload
def add(rx: Float2D, ry: Float2D) -> Float2D:
    """

    """


@overload
def add(ra: float, ry: Float2D) -> Float2D:
    """

    """


@overload
def add(rx: Float2D, rb: float) -> Float2D:
    """

    """


@overload
def add(rx: Float3D, ry: Float3D) -> Float3D:
    """

    """


@overload
def add(ra: float, ry: Float3D) -> Float3D:
    """

    """


@overload
def add(rx: Float3D, rb: float) -> Float3D:
    """

    """


@overload
def add(rx: Float1D, ry: Float1D, rz: Float1D) -> None:
    """

    """


@overload
def add(ra: float, ry: Float1D, rz: Float1D) -> None:
    """

    """


@overload
def add(rx: Float1D, rb: float, rz: Float1D) -> None:
    """

    """


@overload
def add(rx: Float2D, ry: Float2D, rz: Float2D) -> None:
    """

    """


@overload
def add(ra: float, ry: Float2D, rz: Float2D) -> None:
    """

    """


@overload
def add(rx: Float2D, rb: float, rz: Float2D) -> None:
    """

    """


@overload
def add(rx: Float3D, ry: Float3D, rz: Float3D) -> None:
    """

    """


@overload
def add(ra: float, ry: Float3D, rz: Float3D) -> None:
    """

    """


@overload
def add(rx: Float3D, rb: float, rz: Float3D) -> None:
    """

    """


@overload
def sub(rx: Float1D, ry: Float1D) -> Float1D:
    """

    """


@overload
def sub(ra: float, ry: Float1D) -> Float1D:
    """

    """


@overload
def sub(rx: Float1D, rb: float) -> Float1D:
    """

    """


@overload
def sub(rx: Float2D, ry: Float2D) -> Float2D:
    """

    """


@overload
def sub(ra: float, ry: Float2D) -> Float2D:
    """

    """


@overload
def sub(rx: Float2D, rb: float) -> Float2D:
    """

    """


@overload
def sub(rx: Float3D, ry: Float3D) -> Float3D:
    """

    """


@overload
def sub(ra: float, ry: Float3D) -> Float3D:
    """

    """


@overload
def sub(rx: Float3D, rb: float) -> Float3D:
    """

    """


@overload
def sub(rx: Float1D, ry: Float1D, rz: Float1D) -> None:
    """

    """


@overload
def sub(ra: float, ry: Float1D, rz: Float1D) -> None:
    """

    """


@overload
def sub(rx: Float1D, rb: float, rz: Float1D) -> None:
    """

    """


@overload
def sub(rx: Float2D, ry: Float2D, rz: Float2D) -> None:
    """

    """


@overload
def sub(ra: float, ry: Float2D, rz: Float2D) -> None:
    """

    """


@overload
def sub(rx: Float2D, rb: float, rz: Float2D) -> None:
    """

    """


@overload
def sub(rx: Float3D, ry: Float3D, rz: Float3D) -> None:
    """

    """


@overload
def sub(ra: float, ry: Float3D, rz: Float3D) -> None:
    """

    """


@overload
def sub(rx: Float3D, rb: float, rz: Float3D) -> None:
    """

    """


@overload
def mul(rx: Float1D, ry: Float1D) -> Float1D:
    """

    """


@overload
def mul(ra: float, ry: Float1D) -> Float1D:
    """

    """


@overload
def mul(rx: Float1D, rb: float) -> Float1D:
    """

    """


@overload
def mul(rx: Float2D, ry: Float2D) -> Float2D:
    """

    """


@overload
def mul(ra: float, ry: Float2D) -> Float2D:
    """

    """


@overload
def mul(rx: Float2D, rb: float) -> Float2D:
    """

    """


@overload
def mul(rx: Float3D, ry: Float3D) -> Float3D:
    """

    """


@overload
def mul(ra: float, ry: Float3D) -> Float3D:
    """

    """


@overload
def mul(rx: Float3D, rb: float) -> Float3D:
    """

    """


@overload
def mul(rx: Float1D, ry: Float1D, rz: Float1D) -> None:
    """

    """


@overload
def mul(ra: float, ry: Float1D, rz: Float1D) -> None:
    """

    """


@overload
def mul(rx: Float1D, rb: float, rz: Float1D) -> None:
    """

    """


@overload
def mul(rx: Float2D, ry: Float2D, rz: Float2D) -> None:
    """

    """


@overload
def mul(ra: float, ry: Float2D, rz: Float2D) -> None:
    """

    """


@overload
def mul(rx: Float2D, rb: float, rz: Float2D) -> None:
    """

    """


@overload
def mul(rx: Float3D, ry: Float3D, rz: Float3D) -> None:
    """

    """


@overload
def mul(ra: float, ry: Float3D, rz: Float3D) -> None:
    """

    """


@overload
def mul(rx: Float3D, rb: float, rz: Float3D) -> None:
    """

    """


@overload
def div(rx: Float1D, ry: Float1D) -> Float1D:
    """

    """


@overload
def div(ra: float, ry: Float1D) -> Float1D:
    """

    """


@overload
def div(rx: Float1D, rb: float) -> Float1D:
    """

    """


@overload
def div(rx: Float2D, ry: Float2D) -> Float2D:
    """

    """


@overload
def div(ra: float, ry: Float2D) -> Float2D:
    """

    """


@overload
def div(rx: Float2D, rb: float) -> Float2D:
    """

    """


@overload
def div(rx: Float3D, ry: Float3D) -> Float3D:
    """

    """


@overload
def div(ra: float, ry: Float3D) -> Float3D:
    """

    """


@overload
def div(rx: Float3D, rb: float) -> Float3D:
    """

    """


@overload
def div(rx: Float1D, ry: Float1D, rz: Float1D) -> None:
    """

    """


@overload
def div(ra: float, ry: Float1D, rz: Float1D) -> None:
    """

    """


@overload
def div(rx: Float1D, rb: float, rz: Float1D) -> None:
    """

    """


@overload
def div(rx: Float2D, ry: Float2D, rz: Float2D) -> None:
    """

    """


@overload
def div(ra: float, ry: Float2D, rz: Float2D) -> None:
    """

    """


@overload
def div(rx: Float2D, rb: float, rz: Float2D) -> None:
    """

    """


@overload
def div(rx: Float3D, ry: Float3D, rz: Float3D) -> None:
    """

    """


@overload
def div(ra: float, ry: Float3D, rz: Float3D) -> None:
    """

    """


@overload
def div(rx: Float3D, rb: float, rz: Float3D) -> None:
    """

    """


@overload
def add(rx: Double1D, ry: Double1D) -> Double1D:
    """

    """


@overload
def add(ra: double, ry: Double1D) -> Double1D:
    """

    """


@overload
def add(rx: Double1D, rb: double) -> Double1D:
    """

    """


@overload
def add(rx: Double2D, ry: Double2D) -> Double2D:
    """

    """


@overload
def add(ra: double, ry: Double2D) -> Double2D:
    """

    """


@overload
def add(rx: Double2D, rb: double) -> Double2D:
    """

    """


@overload
def add(rx: Double3D, ry: Double3D) -> Double3D:
    """

    """


@overload
def add(ra: double, ry: Double3D) -> Double3D:
    """

    """


@overload
def add(rx: Double3D, rb: double) -> Double3D:
    """

    """


@overload
def add(rx: Double1D, ry: Double1D, rz: Double1D) -> None:
    """

    """


@overload
def add(ra: double, ry: Double1D, rz: Double1D) -> None:
    """

    """


@overload
def add(rx: Double1D, rb: double, rz: Double1D) -> None:
    """

    """


@overload
def add(rx: Double2D, ry: Double2D, rz: Double2D) -> None:
    """

    """


@overload
def add(ra: double, ry: Double2D, rz: Double2D) -> None:
    """

    """


@overload
def add(rx: Double2D, rb: double, rz: Double2D) -> None:
    """

    """


@overload
def add(rx: Double3D, ry: Double3D, rz: Double3D) -> None:
    """

    """


@overload
def add(ra: double, ry: Double3D, rz: Double3D) -> None:
    """

    """


@overload
def add(rx: Double3D, rb: double, rz: Double3D) -> None:
    """

    """


@overload
def sub(rx: Double1D, ry: Double1D) -> Double1D:
    """

    """


@overload
def sub(ra: double, ry: Double1D) -> Double1D:
    """

    """


@overload
def sub(rx: Double1D, rb: double) -> Double1D:
    """

    """


@overload
def sub(rx: Double2D, ry: Double2D) -> Double2D:
    """

    """


@overload
def sub(ra: double, ry: Double2D) -> Double2D:
    """

    """


@overload
def sub(rx: Double2D, rb: double) -> Double2D:
    """

    """


@overload
def sub(rx: Double3D, ry: Double3D) -> Double3D:
    """

    """


@overload
def sub(ra: double, ry: Double3D) -> Double3D:
    """

    """


@overload
def sub(rx: Double3D, rb: double) -> Double3D:
    """

    """


@overload
def sub(rx: Double1D, ry: Double1D, rz: Double1D) -> None:
    """

    """


@overload
def sub(ra: double, ry: Double1D, rz: Double1D) -> None:
    """

    """


@overload
def sub(rx: Double1D, rb: double, rz: Double1D) -> None:
    """

    """


@overload
def sub(rx: Double2D, ry: Double2D, rz: Double2D) -> None:
    """

    """


@overload
def sub(ra: double, ry: Double2D, rz: Double2D) -> None:
    """

    """


@overload
def sub(rx: Double2D, rb: double, rz: Double2D) -> None:
    """

    """


@overload
def sub(rx: Double3D, ry: Double3D, rz: Double3D) -> None:
    """

    """


@overload
def sub(ra: double, ry: Double3D, rz: Double3D) -> None:
    """

    """


@overload
def sub(rx: Double3D, rb: double, rz: Double3D) -> None:
    """

    """


@overload
def mul(rx: Double1D, ry: Double1D) -> Double1D:
    """

    """


@overload
def mul(ra: double, ry: Double1D) -> Double1D:
    """

    """


@overload
def mul(rx: Double1D, rb: double) -> Double1D:
    """

    """


@overload
def mul(rx: Double2D, ry: Double2D) -> Double2D:
    """

    """


@overload
def mul(ra: double, ry: Double2D) -> Double2D:
    """

    """


@overload
def mul(rx: Double2D, rb: double) -> Double2D:
    """

    """


@overload
def mul(rx: Double3D, ry: Double3D) -> Double3D:
    """

    """


@overload
def mul(ra: double, ry: Double3D) -> Double3D:
    """

    """


@overload
def mul(rx: Double3D, rb: double) -> Double3D:
    """

    """


@overload
def mul(rx: Double1D, ry: Double1D, rz: Double1D) -> None:
    """

    """


@overload
def mul(ra: double, ry: Double1D, rz: Double1D) -> None:
    """

    """


@overload
def mul(rx: Double1D, rb: double, rz: Double1D) -> None:
    """

    """


@overload
def mul(rx: Double2D, ry: Double2D, rz: Double2D) -> None:
    """

    """


@overload
def mul(ra: double, ry: Double2D, rz: Double2D) -> None:
    """

    """


@overload
def mul(rx: Double2D, rb: double, rz: Double2D) -> None:
    """

    """


@overload
def mul(rx: Double3D, ry: Double3D, rz: Double3D) -> None:
    """

    """


@overload
def mul(ra: double, ry: Double3D, rz: Double3D) -> None:
    """

    """


@overload
def mul(rx: Double3D, rb: double, rz: Double3D) -> None:
    """

    """


@overload
def div(rx: Double1D, ry: Double1D) -> Double1D:
    """

    """


@overload
def div(ra: double, ry: Double1D) -> Double1D:
    """

    """


@overload
def div(rx: Double1D, rb: double) -> Double1D:
    """

    """


@overload
def div(rx: Double2D, ry: Double2D) -> Double2D:
    """

    """


@overload
def div(ra: double, ry: Double2D) -> Double2D:
    """

    """


@overload
def div(rx: Double2D, rb: double) -> Double2D:
    """

    """


@overload
def div(rx: Double3D, ry: Double3D) -> Double3D:
    """

    """


@overload
def div(ra: double, ry: Double3D) -> Double3D:
    """

    """


@overload
def div(rx: Double3D, rb: double) -> Double3D:
    """

    """


@overload
def div(rx: Double1D, ry: Double1D, rz: Double1D) -> None:
    """

    """


@overload
def div(ra: double, ry: Double1D, rz: Double1D) -> None:
    """

    """


@overload
def div(rx: Double1D, rb: double, rz: Double1D) -> None:
    """

    """


@overload
def div(rx: Double2D, ry: Double2D, rz: Double2D) -> None:
    """

    """


@overload
def div(ra: double, ry: Double2D, rz: Double2D) -> None:
    """

    """


@overload
def div(rx: Double2D, rb: double, rz: Double2D) -> None:
    """

    """


@overload
def div(rx: Double3D, ry: Double3D, rz: Double3D) -> None:
    """

    """


@overload
def div(ra: double, ry: Double3D, rz: Double3D) -> None:
    """

    """


@overload
def div(rx: Double3D, rb: double, rz: Double3D) -> None:
    """

    """


@overload
def abs(rx: Float1D) -> Float1D:
    """

    """


@overload
def abs(rx: Float2D) -> Float2D:
    """

    """


@overload
def abs(rx: Float3D) -> Float3D:
    """

    """


@overload
def abs(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def abs(rx: Float2D, ry: Float2D) -> None:
    """

    """


@overload
def abs(rx: Float3D, ry: Float3D) -> None:
    """

    """


@overload
def neg(rx: Float1D) -> Float1D:
    """

    """


@overload
def neg(rx: Float2D) -> Float2D:
    """

    """


@overload
def neg(rx: Float3D) -> Float3D:
    """

    """


@overload
def neg(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def neg(rx: Float2D, ry: Float2D) -> None:
    """

    """


@overload
def neg(rx: Float3D, ry: Float3D) -> None:
    """

    """


@overload
def cos(rx: Float1D) -> Float1D:
    """

    """


@overload
def cos(rx: Float2D) -> Float2D:
    """

    """


@overload
def cos(rx: Float3D) -> Float3D:
    """

    """


@overload
def cos(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def cos(rx: Float2D, ry: Float2D) -> None:
    """

    """


@overload
def cos(rx: Float3D, ry: Float3D) -> None:
    """

    """


@overload
def sin(rx: Float1D) -> Float1D:
    """

    """


@overload
def sin(rx: Float2D) -> Float2D:
    """

    """


@overload
def sin(rx: Float3D) -> Float3D:
    """

    """


@overload
def sin(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def sin(rx: Float2D, ry: Float2D) -> None:
    """

    """


@overload
def sin(rx: Float3D, ry: Float3D) -> None:
    """

    """


@overload
def exp(rx: Float1D) -> Float1D:
    """

    """


@overload
def exp(rx: Float2D) -> Float2D:
    """

    """


@overload
def exp(rx: Float3D) -> Float3D:
    """

    """


@overload
def exp(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def exp(rx: Float2D, ry: Float2D) -> None:
    """

    """


@overload
def exp(rx: Float3D, ry: Float3D) -> None:
    """

    """


@overload
def log(rx: Float1D) -> Float1D:
    """

    """


@overload
def log(rx: Float2D) -> Float2D:
    """

    """


@overload
def log(rx: Float3D) -> Float3D:
    """

    """


@overload
def log(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def log(rx: Float2D, ry: Float2D) -> None:
    """

    """


@overload
def log(rx: Float3D, ry: Float3D) -> None:
    """

    """


@overload
def log10(rx: Float1D) -> Float1D:
    """

    """


@overload
def log10(rx: Float2D) -> Float2D:
    """

    """


@overload
def log10(rx: Float3D) -> Float3D:
    """

    """


@overload
def log10(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def log10(rx: Float2D, ry: Float2D) -> None:
    """

    """


@overload
def log10(rx: Float3D, ry: Float3D) -> None:
    """

    """


@overload
def sqrt(rx: Float1D) -> Float1D:
    """

    """


@overload
def sqrt(rx: Float2D) -> Float2D:
    """

    """


@overload
def sqrt(rx: Float3D) -> Float3D:
    """

    """


@overload
def sqrt(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def sqrt(rx: Float2D, ry: Float2D) -> None:
    """

    """


@overload
def sqrt(rx: Float3D, ry: Float3D) -> None:
    """

    """


@overload
def sgn(rx: Float1D) -> Float1D:
    """

    """


@overload
def sgn(rx: Float2D) -> Float2D:
    """

    """


@overload
def sgn(rx: Float3D) -> Float3D:
    """

    """


@overload
def sgn(rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def sgn(rx: Float2D, ry: Float2D) -> None:
    """

    """


@overload
def sgn(rx: Float3D, ry: Float3D) -> None:
    """

    """


@overload
def abs(rx: Double1D) -> Double1D:
    """

    """


@overload
def abs(rx: Double2D) -> Double2D:
    """

    """


@overload
def abs(rx: Double3D) -> Double3D:
    """

    """


@overload
def abs(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def abs(rx: Double2D, ry: Double2D) -> None:
    """

    """


@overload
def abs(rx: Double3D, ry: Double3D) -> None:
    """

    """


@overload
def neg(rx: Double1D) -> Double1D:
    """

    """


@overload
def neg(rx: Double2D) -> Double2D:
    """

    """


@overload
def neg(rx: Double3D) -> Double3D:
    """

    """


@overload
def neg(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def neg(rx: Double2D, ry: Double2D) -> None:
    """

    """


@overload
def neg(rx: Double3D, ry: Double3D) -> None:
    """

    """


@overload
def cos(rx: Double1D) -> Double1D:
    """

    """


@overload
def cos(rx: Double2D) -> Double2D:
    """

    """


@overload
def cos(rx: Double3D) -> Double3D:
    """

    """


@overload
def cos(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def cos(rx: Double2D, ry: Double2D) -> None:
    """

    """


@overload
def cos(rx: Double3D, ry: Double3D) -> None:
    """

    """


@overload
def sin(rx: Double1D) -> Double1D:
    """

    """


@overload
def sin(rx: Double2D) -> Double2D:
    """

    """


@overload
def sin(rx: Double3D) -> Double3D:
    """

    """


@overload
def sin(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def sin(rx: Double2D, ry: Double2D) -> None:
    """

    """


@overload
def sin(rx: Double3D, ry: Double3D) -> None:
    """

    """


@overload
def exp(rx: Double1D) -> Double1D:
    """

    """


@overload
def exp(rx: Double2D) -> Double2D:
    """

    """


@overload
def exp(rx: Double3D) -> Double3D:
    """

    """


@overload
def exp(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def exp(rx: Double2D, ry: Double2D) -> None:
    """

    """


@overload
def exp(rx: Double3D, ry: Double3D) -> None:
    """

    """


@overload
def log(rx: Double1D) -> Double1D:
    """

    """


@overload
def log(rx: Double2D) -> Double2D:
    """

    """


@overload
def log(rx: Double3D) -> Double3D:
    """

    """


@overload
def log(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def log(rx: Double2D, ry: Double2D) -> None:
    """

    """


@overload
def log(rx: Double3D, ry: Double3D) -> None:
    """

    """


@overload
def log10(rx: Double1D) -> Double1D:
    """

    """


@overload
def log10(rx: Double2D) -> Double2D:
    """

    """


@overload
def log10(rx: Double3D) -> Double3D:
    """

    """


@overload
def log10(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def log10(rx: Double2D, ry: Double2D) -> None:
    """

    """


@overload
def log10(rx: Double3D, ry: Double3D) -> None:
    """

    """


@overload
def sqrt(rx: Double1D) -> Double1D:
    """

    """


@overload
def sqrt(rx: Double2D) -> Double2D:
    """

    """


@overload
def sqrt(rx: Double3D) -> Double3D:
    """

    """


@overload
def sqrt(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def sqrt(rx: Double2D, ry: Double2D) -> None:
    """

    """


@overload
def sqrt(rx: Double3D, ry: Double3D) -> None:
    """

    """


@overload
def sgn(rx: Double1D) -> Double1D:
    """

    """


@overload
def sgn(rx: Double2D) -> Double2D:
    """

    """


@overload
def sgn(rx: Double3D) -> Double3D:
    """

    """


@overload
def sgn(rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def sgn(rx: Double2D, ry: Double2D) -> None:
    """

    """


@overload
def sgn(rx: Double3D, ry: Double3D) -> None:
    """

    """


@overload
def clip(rxmin: float, rxmax: float, rx: Float1D) -> Float1D:
    """

    """


@overload
def clip(rxmin: float, rxmax: float, rx: Float2D) -> Float2D:
    """

    """


@overload
def clip(rxmin: float, rxmax: float, rx: Float3D) -> Float3D:
    """

    """


@overload
def clip(rxmin: float, rxmax: float, rx: Float1D, ry: Float1D) -> None:
    """

    """


@overload
def clip(rxmin: float, rxmax: float, rx: Float2D, ry: Float2D) -> None:
    """

    """


@overload
def clip(rxmin: float, rxmax: float, rx: Float3D, ry: Float3D) -> None:
    """

    """


@overload
def clip(rxmin: double, rxmax: double, rx: Double1D) -> Double1D:
    """

    """


@overload
def clip(rxmin: double, rxmax: double, rx: Double2D) -> Double2D:
    """

    """


@overload
def clip(rxmin: double, rxmax: double, rx: Double3D) -> Double3D:
    """

    """


@overload
def clip(rxmin: double, rxmax: double, rx: Double1D, ry: Double1D) -> None:
    """

    """


@overload
def clip(rxmin: double, rxmax: double, rx: Double2D, ry: Double2D) -> None:
    """

    """


@overload
def clip(rxmin: double, rxmax: double, rx: Double3D, ry: Double3D) -> None:
    """

    """


@overload
def pow(rx: Float1D, ra: float) -> Float1D:
    """

    """


@overload
def pow(rx: Float2D, ra: float) -> Float2D:
    """

    """


@overload
def pow(rx: Float3D, ra: float) -> Float3D:
    """

    """


@overload
def pow(rx: Float1D, ra: float, ry: Float1D) -> None:
    """

    """


@overload
def pow(rx: Float2D, ra: float, ry: Float2D) -> None:
    """

    """


@overload
def pow(rx: Float3D, ra: float, ry: Float3D) -> None:
    """

    """


@overload
def pow(rx: Double1D, ra: double) -> Double1D:
    """

    """


@overload
def pow(rx: Double2D, ra: double) -> Double2D:
    """

    """


@overload
def pow(rx: Double3D, ra: double) -> Double3D:
    """

    """


@overload
def pow(rx: Double1D, ra: double, ry: Double1D) -> None:
    """

    """


@overload
def pow(rx: Double2D, ra: double, ry: Double2D) -> None:
    """

    """


@overload
def pow(rx: Double3D, ra: double, ry: Double3D) -> None:
    """

    """


@overload
def sum(rx: Byte1D) -> byte:
    """

    """


@overload
def sum(rx: Byte2D) -> byte:
    """

    """


@overload
def sum(rx: Byte3D) -> byte:
    """

    """


@overload
def sum(rx: Short1D) -> short:
    """

    """


@overload
def sum(rx: Short2D) -> short:
    """

    """


@overload
def sum(rx: Short3D) -> short:
    """

    """


@overload
def sum(rx: Int1D) -> int:
    """

    """


@overload
def sum(rx: Int2D) -> int:
    """

    """


@overload
def sum(rx: Int3D) -> int:
    """

    """


@overload
def sum(rx: Long1D) -> long:
    """

    """


@overload
def sum(rx: Long2D) -> long:
    """

    """


@overload
def sum(rx: Long3D) -> long:
    """

    """


@overload
def sum(rx: Float1D) -> float:
    """

    """


@overload
def sum(rx: Float2D) -> float:
    """

    """


@overload
def sum(rx: Float3D) -> float:
    """

    """


@overload
def sum(rx: Double1D) -> double:
    """

    """


@overload
def sum(rx: Double2D) -> double:
    """

    """


@overload
def sum(rx: Double3D) -> double:
    """

    """


@overload
def max(rx: Byte1D) -> byte:
    """

    """


@overload
def max(rx: Byte2D) -> byte:
    """

    """


@overload
def max(rx: Byte3D) -> byte:
    """

    """


@overload
def max(rx: Byte1D, index: Int1D) -> byte:
    """

    """


@overload
def max(rx: Byte2D, index: Int1D) -> byte:
    """

    """


@overload
def max(rx: Byte3D, index: Int1D) -> byte:
    """

    """


@overload
def min(rx: Byte1D) -> byte:
    """

    """


@overload
def min(rx: Byte2D) -> byte:
    """

    """


@overload
def min(rx: Byte3D) -> byte:
    """

    """


@overload
def min(rx: Byte1D, index: Int1D) -> byte:
    """

    """


@overload
def min(rx: Byte2D, index: Int1D) -> byte:
    """

    """


@overload
def min(rx: Byte3D, index: Int1D) -> byte:
    """

    """


@overload
def max(rx: Short1D) -> short:
    """

    """


@overload
def max(rx: Short2D) -> short:
    """

    """


@overload
def max(rx: Short3D) -> short:
    """

    """


@overload
def max(rx: Short1D, index: Int1D) -> short:
    """

    """


@overload
def max(rx: Short2D, index: Int1D) -> short:
    """

    """


@overload
def max(rx: Short3D, index: Int1D) -> short:
    """

    """


@overload
def min(rx: Short1D) -> short:
    """

    """


@overload
def min(rx: Short2D) -> short:
    """

    """


@overload
def min(rx: Short3D) -> short:
    """

    """


@overload
def min(rx: Short1D, index: Int1D) -> short:
    """

    """


@overload
def min(rx: Short2D, index: Int1D) -> short:
    """

    """


@overload
def min(rx: Short3D, index: Int1D) -> short:
    """

    """


@overload
def max(rx: Int1D) -> int:
    """

    """


@overload
def max(rx: Int2D) -> int:
    """

    """


@overload
def max(rx: Int3D) -> int:
    """

    """


@overload
def max(rx: Int1D, index: Int1D) -> int:
    """

    """


@overload
def max(rx: Int2D, index: Int1D) -> int:
    """

    """


@overload
def max(rx: Int3D, index: Int1D) -> int:
    """

    """


@overload
def min(rx: Int1D) -> int:
    """

    """


@overload
def min(rx: Int2D) -> int:
    """

    """


@overload
def min(rx: Int3D) -> int:
    """

    """


@overload
def min(rx: Int1D, index: Int1D) -> int:
    """

    """


@overload
def min(rx: Int2D, index: Int1D) -> int:
    """

    """


@overload
def min(rx: Int3D, index: Int1D) -> int:
    """

    """


@overload
def max(rx: Long1D) -> long:
    """

    """


@overload
def max(rx: Long2D) -> long:
    """

    """


@overload
def max(rx: Long3D) -> long:
    """

    """


@overload
def max(rx: Long1D, index: Int1D) -> long:
    """

    """


@overload
def max(rx: Long2D, index: Int1D) -> long:
    """

    """


@overload
def max(rx: Long3D, index: Int1D) -> long:
    """

    """


@overload
def min(rx: Long1D) -> long:
    """

    """


@overload
def min(rx: Long2D) -> long:
    """

    """


@overload
def min(rx: Long3D) -> long:
    """

    """


@overload
def min(rx: Long1D, index: Int1D) -> long:
    """

    """


@overload
def min(rx: Long2D, index: Int1D) -> long:
    """

    """


@overload
def min(rx: Long3D, index: Int1D) -> long:
    """

    """


@overload
def max(rx: Float1D) -> float:
    """

    """


@overload
def max(rx: Float2D) -> float:
    """

    """


@overload
def max(rx: Float3D) -> float:
    """

    """


@overload
def max(rx: Float1D, index: Int1D) -> float:
    """

    """


@overload
def max(rx: Float2D, index: Int1D) -> float:
    """

    """


@overload
def max(rx: Float3D, index: Int1D) -> float:
    """

    """


@overload
def min(rx: Float1D) -> float:
    """

    """


@overload
def min(rx: Float2D) -> float:
    """

    """


@overload
def min(rx: Float3D) -> float:
    """

    """


@overload
def min(rx: Float1D, index: Int1D) -> float:
    """

    """


@overload
def min(rx: Float2D, index: Int1D) -> float:
    """

    """


@overload
def min(rx: Float3D, index: Int1D) -> float:
    """

    """


@overload
def max(rx: Double1D) -> double:
    """

    """


@overload
def max(rx: Double2D) -> double:
    """

    """


@overload
def max(rx: Double3D) -> double:
    """

    """


@overload
def max(rx: Double1D, index: Int1D) -> double:
    """

    """


@overload
def max(rx: Double2D, index: Int1D) -> double:
    """

    """


@overload
def max(rx: Double3D, index: Int1D) -> double:
    """

    """


@overload
def min(rx: Double1D) -> double:
    """

    """


@overload
def min(rx: Double2D) -> double:
    """

    """


@overload
def min(rx: Double3D) -> double:
    """

    """


@overload
def min(rx: Double1D, index: Int1D) -> double:
    """

    """


@overload
def min(rx: Double2D, index: Int1D) -> double:
    """

    """


@overload
def min(rx: Double3D, index: Int1D) -> double:
    """

    """


@overload
def cadd(cx: Float1D, cy: Float1D) -> Float1D:
    """

    """


@overload
def cadd(ca: Cfloat, cy: Float1D) -> Float1D:
    """

    """


@overload
def cadd(cx: Float1D, cb: Cfloat) -> Float1D:
    """

    """


@overload
def cadd(cx: Float2D, cy: Float2D) -> Float2D:
    """

    """


@overload
def cadd(ca: Cfloat, cy: Float2D) -> Float2D:
    """

    """


@overload
def cadd(cx: Float2D, cb: Cfloat) -> Float2D:
    """

    """


@overload
def cadd(cx: Float3D, cy: Float3D) -> Float3D:
    """

    """


@overload
def cadd(ca: Cfloat, cy: Float3D) -> Float3D:
    """

    """


@overload
def cadd(cx: Float3D, cb: Cfloat) -> Float3D:
    """

    """


@overload
def cadd(cx: Float1D, cy: Float1D, cz: Float1D) -> None:
    """

    """


@overload
def cadd(ca: Cfloat, cy: Float1D, cz: Float1D) -> None:
    """

    """


@overload
def cadd(cx: Float1D, cb: Cfloat, cz: Float1D) -> None:
    """

    """


@overload
def cadd(cx: Float2D, cy: Float2D, cz: Float2D) -> None:
    """

    """


@overload
def cadd(ca: Cfloat, cy: Float2D, cz: Float2D) -> None:
    """

    """


@overload
def cadd(cx: Float2D, cb: Cfloat, cz: Float2D) -> None:
    """

    """


@overload
def cadd(cx: Float3D, cy: Float3D, cz: Float3D) -> None:
    """

    """


@overload
def cadd(ca: Cfloat, cy: Float3D, cz: Float3D) -> None:
    """

    """


@overload
def cadd(cx: Float3D, cb: Cfloat, cz: Float3D) -> None:
    """

    """


@overload
def csub(cx: Float1D, cy: Float1D) -> Float1D:
    """

    """


@overload
def csub(ca: Cfloat, cy: Float1D) -> Float1D:
    """

    """


@overload
def csub(cx: Float1D, cb: Cfloat) -> Float1D:
    """

    """


@overload
def csub(cx: Float2D, cy: Float2D) -> Float2D:
    """

    """


@overload
def csub(ca: Cfloat, cy: Float2D) -> Float2D:
    """

    """


@overload
def csub(cx: Float2D, cb: Cfloat) -> Float2D:
    """

    """


@overload
def csub(cx: Float3D, cy: Float3D) -> Float3D:
    """

    """


@overload
def csub(ca: Cfloat, cy: Float3D) -> Float3D:
    """

    """


@overload
def csub(cx: Float3D, cb: Cfloat) -> Float3D:
    """

    """


@overload
def csub(cx: Float1D, cy: Float1D, cz: Float1D) -> None:
    """

    """


@overload
def csub(ca: Cfloat, cy: Float1D, cz: Float1D) -> None:
    """

    """


@overload
def csub(cx: Float1D, cb: Cfloat, cz: Float1D) -> None:
    """

    """


@overload
def csub(cx: Float2D, cy: Float2D, cz: Float2D) -> None:
    """

    """


@overload
def csub(ca: Cfloat, cy: Float2D, cz: Float2D) -> None:
    """

    """


@overload
def csub(cx: Float2D, cb: Cfloat, cz: Float2D) -> None:
    """

    """


@overload
def csub(cx: Float3D, cy: Float3D, cz: Float3D) -> None:
    """

    """


@overload
def csub(ca: Cfloat, cy: Float3D, cz: Float3D) -> None:
    """

    """


@overload
def csub(cx: Float3D, cb: Cfloat, cz: Float3D) -> None:
    """

    """


@overload
def cmul(cx: Float1D, cy: Float1D) -> Float1D:
    """

    """


@overload
def cmul(ca: Cfloat, cy: Float1D) -> Float1D:
    """

    """


@overload
def cmul(cx: Float1D, cb: Cfloat) -> Float1D:
    """

    """


@overload
def cmul(cx: Float2D, cy: Float2D) -> Float2D:
    """

    """


@overload
def cmul(ca: Cfloat, cy: Float2D) -> Float2D:
    """

    """


@overload
def cmul(cx: Float2D, cb: Cfloat) -> Float2D:
    """

    """


@overload
def cmul(cx: Float3D, cy: Float3D) -> Float3D:
    """

    """


@overload
def cmul(ca: Cfloat, cy: Float3D) -> Float3D:
    """

    """


@overload
def cmul(cx: Float3D, cb: Cfloat) -> Float3D:
    """

    """


@overload
def cmul(cx: Float1D, cy: Float1D, cz: Float1D) -> None:
    """

    """


@overload
def cmul(ca: Cfloat, cy: Float1D, cz: Float1D) -> None:
    """

    """


@overload
def cmul(cx: Float1D, cb: Cfloat, cz: Float1D) -> None:
    """

    """


@overload
def cmul(cx: Float2D, cy: Float2D, cz: Float2D) -> None:
    """

    """


@overload
def cmul(ca: Cfloat, cy: Float2D, cz: Float2D) -> None:
    """

    """


@overload
def cmul(cx: Float2D, cb: Cfloat, cz: Float2D) -> None:
    """

    """


@overload
def cmul(cx: Float3D, cy: Float3D, cz: Float3D) -> None:
    """

    """


@overload
def cmul(ca: Cfloat, cy: Float3D, cz: Float3D) -> None:
    """

    """


@overload
def cmul(cx: Float3D, cb: Cfloat, cz: Float3D) -> None:
    """

    """


@overload
def cdiv(cx: Float1D, cy: Float1D) -> Float1D:
    """

    """


@overload
def cdiv(ca: Cfloat, cy: Float1D) -> Float1D:
    """

    """


@overload
def cdiv(cx: Float1D, cb: Cfloat) -> Float1D:
    """

    """


@overload
def cdiv(cx: Float2D, cy: Float2D) -> Float2D:
    """

    """


@overload
def cdiv(ca: Cfloat, cy: Float2D) -> Float2D:
    """

    """


@overload
def cdiv(cx: Float2D, cb: Cfloat) -> Float2D:
    """

    """


@overload
def cdiv(cx: Float3D, cy: Float3D) -> Float3D:
    """

    """


@overload
def cdiv(ca: Cfloat, cy: Float3D) -> Float3D:
    """

    """


@overload
def cdiv(cx: Float3D, cb: Cfloat) -> Float3D:
    """

    """


@overload
def cdiv(cx: Float1D, cy: Float1D, cz: Float1D) -> None:
    """

    """


@overload
def cdiv(ca: Cfloat, cy: Float1D, cz: Float1D) -> None:
    """

    """


@overload
def cdiv(cx: Float1D, cb: Cfloat, cz: Float1D) -> None:
    """

    """


@overload
def cdiv(cx: Float2D, cy: Float2D, cz: Float2D) -> None:
    """

    """


@overload
def cdiv(ca: Cfloat, cy: Float2D, cz: Float2D) -> None:
    """

    """


@overload
def cdiv(cx: Float2D, cb: Cfloat, cz: Float2D) -> None:
    """

    """


@overload
def cdiv(cx: Float3D, cy: Float3D, cz: Float3D) -> None:
    """

    """


@overload
def cdiv(ca: Cfloat, cy: Float3D, cz: Float3D) -> None:
    """

    """


@overload
def cdiv(cx: Float3D, cb: Cfloat, cz: Float3D) -> None:
    """

    """


@overload
def cadd(cx: Double1D, cy: Double1D) -> Double1D:
    """

    """


@overload
def cadd(ca: Cdouble, cy: Double1D) -> Double1D:
    """

    """


@overload
def cadd(cx: Double1D, cb: Cdouble) -> Double1D:
    """

    """


@overload
def cadd(cx: Double2D, cy: Double2D) -> Double2D:
    """

    """


@overload
def cadd(ca: Cdouble, cy: Double2D) -> Double2D:
    """

    """


@overload
def cadd(cx: Double2D, cb: Cdouble) -> Double2D:
    """

    """


@overload
def cadd(cx: Double3D, cy: Double3D) -> Double3D:
    """

    """


@overload
def cadd(ca: Cdouble, cy: Double3D) -> Double3D:
    """

    """


@overload
def cadd(cx: Double3D, cb: Cdouble) -> Double3D:
    """

    """


@overload
def cadd(cx: Double1D, cy: Double1D, cz: Double1D) -> None:
    """

    """


@overload
def cadd(ca: Cdouble, cy: Double1D, cz: Double1D) -> None:
    """

    """


@overload
def cadd(cx: Double1D, cb: Cdouble, cz: Double1D) -> None:
    """

    """


@overload
def cadd(cx: Double2D, cy: Double2D, cz: Double2D) -> None:
    """

    """


@overload
def cadd(ca: Cdouble, cy: Double2D, cz: Double2D) -> None:
    """

    """


@overload
def cadd(cx: Double2D, cb: Cdouble, cz: Double2D) -> None:
    """

    """


@overload
def cadd(cx: Double3D, cy: Double3D, cz: Double3D) -> None:
    """

    """


@overload
def cadd(ca: Cdouble, cy: Double3D, cz: Double3D) -> None:
    """

    """


@overload
def cadd(cx: Double3D, cb: Cdouble, cz: Double3D) -> None:
    """

    """


@overload
def csub(cx: Double1D, cy: Double1D) -> Double1D:
    """

    """


@overload
def csub(ca: Cdouble, cy: Double1D) -> Double1D:
    """

    """


@overload
def csub(cx: Double1D, cb: Cdouble) -> Double1D:
    """

    """


@overload
def csub(cx: Double2D, cy: Double2D) -> Double2D:
    """

    """


@overload
def csub(ca: Cdouble, cy: Double2D) -> Double2D:
    """

    """


@overload
def csub(cx: Double2D, cb: Cdouble) -> Double2D:
    """

    """


@overload
def csub(cx: Double3D, cy: Double3D) -> Double3D:
    """

    """


@overload
def csub(ca: Cdouble, cy: Double3D) -> Double3D:
    """

    """


@overload
def csub(cx: Double3D, cb: Cdouble) -> Double3D:
    """

    """


@overload
def csub(cx: Double1D, cy: Double1D, cz: Double1D) -> None:
    """

    """


@overload
def csub(ca: Cdouble, cy: Double1D, cz: Double1D) -> None:
    """

    """


@overload
def csub(cx: Double1D, cb: Cdouble, cz: Double1D) -> None:
    """

    """


@overload
def csub(cx: Double2D, cy: Double2D, cz: Double2D) -> None:
    """

    """


@overload
def csub(ca: Cdouble, cy: Double2D, cz: Double2D) -> None:
    """

    """


@overload
def csub(cx: Double2D, cb: Cdouble, cz: Double2D) -> None:
    """

    """


@overload
def csub(cx: Double3D, cy: Double3D, cz: Double3D) -> None:
    """

    """


@overload
def csub(ca: Cdouble, cy: Double3D, cz: Double3D) -> None:
    """

    """


@overload
def csub(cx: Double3D, cb: Cdouble, cz: Double3D) -> None:
    """

    """


@overload
def cmul(cx: Double1D, cy: Double1D) -> Double1D:
    """

    """


@overload
def cmul(ca: Cdouble, cy: Double1D) -> Double1D:
    """

    """


@overload
def cmul(cx: Double1D, cb: Cdouble) -> Double1D:
    """

    """


@overload
def cmul(cx: Double2D, cy: Double2D) -> Double2D:
    """

    """


@overload
def cmul(ca: Cdouble, cy: Double2D) -> Double2D:
    """

    """


@overload
def cmul(cx: Double2D, cb: Cdouble) -> Double2D:
    """

    """


@overload
def cmul(cx: Double3D, cy: Double3D) -> Double3D:
    """

    """


@overload
def cmul(ca: Cdouble, cy: Double3D) -> Double3D:
    """

    """


@overload
def cmul(cx: Double3D, cb: Cdouble) -> Double3D:
    """

    """


@overload
def cmul(cx: Double1D, cy: Double1D, cz: Double1D) -> None:
    """

    """


@overload
def cmul(ca: Cdouble, cy: Double1D, cz: Double1D) -> None:
    """

    """


@overload
def cmul(cx: Double1D, cb: Cdouble, cz: Double1D) -> None:
    """

    """


@overload
def cmul(cx: Double2D, cy: Double2D, cz: Double2D) -> None:
    """

    """


@overload
def cmul(ca: Cdouble, cy: Double2D, cz: Double2D) -> None:
    """

    """


@overload
def cmul(cx: Double2D, cb: Cdouble, cz: Double2D) -> None:
    """

    """


@overload
def cmul(cx: Double3D, cy: Double3D, cz: Double3D) -> None:
    """

    """


@overload
def cmul(ca: Cdouble, cy: Double3D, cz: Double3D) -> None:
    """

    """


@overload
def cmul(cx: Double3D, cb: Cdouble, cz: Double3D) -> None:
    """

    """


@overload
def cdiv(cx: Double1D, cy: Double1D) -> Double1D:
    """

    """


@overload
def cdiv(ca: Cdouble, cy: Double1D) -> Double1D:
    """

    """


@overload
def cdiv(cx: Double1D, cb: Cdouble) -> Double1D:
    """

    """


@overload
def cdiv(cx: Double2D, cy: Double2D) -> Double2D:
    """

    """


@overload
def cdiv(ca: Cdouble, cy: Double2D) -> Double2D:
    """

    """


@overload
def cdiv(cx: Double2D, cb: Cdouble) -> Double2D:
    """

    """


@overload
def cdiv(cx: Double3D, cy: Double3D) -> Double3D:
    """

    """


@overload
def cdiv(ca: Cdouble, cy: Double3D) -> Double3D:
    """

    """


@overload
def cdiv(cx: Double3D, cb: Cdouble) -> Double3D:
    """

    """


@overload
def cdiv(cx: Double1D, cy: Double1D, cz: Double1D) -> None:
    """

    """


@overload
def cdiv(ca: Cdouble, cy: Double1D, cz: Double1D) -> None:
    """

    """


@overload
def cdiv(cx: Double1D, cb: Cdouble, cz: Double1D) -> None:
    """

    """


@overload
def cdiv(cx: Double2D, cy: Double2D, cz: Double2D) -> None:
    """

    """


@overload
def cdiv(ca: Cdouble, cy: Double2D, cz: Double2D) -> None:
    """

    """


@overload
def cdiv(cx: Double2D, cb: Cdouble, cz: Double2D) -> None:
    """

    """


@overload
def cdiv(cx: Double3D, cy: Double3D, cz: Double3D) -> None:
    """

    """


@overload
def cdiv(ca: Cdouble, cy: Double3D, cz: Double3D) -> None:
    """

    """


@overload
def cdiv(cx: Double3D, cb: Cdouble, cz: Double3D) -> None:
    """

    """


@overload
def cneg(cx: Float1D) -> Float1D:
    """

    """


@overload
def cneg(cx: Float2D) -> Float2D:
    """

    """


@overload
def cneg(cx: Float3D) -> Float3D:
    """

    """


@overload
def cneg(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def cneg(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def cneg(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def cconj(cx: Float1D) -> Float1D:
    """

    """


@overload
def cconj(cx: Float2D) -> Float2D:
    """

    """


@overload
def cconj(cx: Float3D) -> Float3D:
    """

    """


@overload
def cconj(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def cconj(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def cconj(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def ccos(cx: Float1D) -> Float1D:
    """

    """


@overload
def ccos(cx: Float2D) -> Float2D:
    """

    """


@overload
def ccos(cx: Float3D) -> Float3D:
    """

    """


@overload
def ccos(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def ccos(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def ccos(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def csin(cx: Float1D) -> Float1D:
    """

    """


@overload
def csin(cx: Float2D) -> Float2D:
    """

    """


@overload
def csin(cx: Float3D) -> Float3D:
    """

    """


@overload
def csin(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def csin(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def csin(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def csqrt(cx: Float1D) -> Float1D:
    """

    """


@overload
def csqrt(cx: Float2D) -> Float2D:
    """

    """


@overload
def csqrt(cx: Float3D) -> Float3D:
    """

    """


@overload
def csqrt(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def csqrt(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def csqrt(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def cexp(cx: Float1D) -> Float1D:
    """

    """


@overload
def cexp(cx: Float2D) -> Float2D:
    """

    """


@overload
def cexp(cx: Float3D) -> Float3D:
    """

    """


@overload
def cexp(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def cexp(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def cexp(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def clog(cx: Float1D) -> Float1D:
    """

    """


@overload
def clog(cx: Float2D) -> Float2D:
    """

    """


@overload
def clog(cx: Float3D) -> Float3D:
    """

    """


@overload
def clog(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def clog(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def clog(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def clog10(cx: Float1D) -> Float1D:
    """

    """


@overload
def clog10(cx: Float2D) -> Float2D:
    """

    """


@overload
def clog10(cx: Float3D) -> Float3D:
    """

    """


@overload
def clog10(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def clog10(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def clog10(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def cneg(cx: Double1D) -> Double1D:
    """

    """


@overload
def cneg(cx: Double2D) -> Double2D:
    """

    """


@overload
def cneg(cx: Double3D) -> Double3D:
    """

    """


@overload
def cneg(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def cneg(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def cneg(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def cconj(cx: Double1D) -> Double1D:
    """

    """


@overload
def cconj(cx: Double2D) -> Double2D:
    """

    """


@overload
def cconj(cx: Double3D) -> Double3D:
    """

    """


@overload
def cconj(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def cconj(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def cconj(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def ccos(cx: Double1D) -> Double1D:
    """

    """


@overload
def ccos(cx: Double2D) -> Double2D:
    """

    """


@overload
def ccos(cx: Double3D) -> Double3D:
    """

    """


@overload
def ccos(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def ccos(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def ccos(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def csin(cx: Double1D) -> Double1D:
    """

    """


@overload
def csin(cx: Double2D) -> Double2D:
    """

    """


@overload
def csin(cx: Double3D) -> Double3D:
    """

    """


@overload
def csin(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def csin(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def csin(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def csqrt(cx: Double1D) -> Double1D:
    """

    """


@overload
def csqrt(cx: Double2D) -> Double2D:
    """

    """


@overload
def csqrt(cx: Double3D) -> Double3D:
    """

    """


@overload
def csqrt(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def csqrt(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def csqrt(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def cexp(cx: Double1D) -> Double1D:
    """

    """


@overload
def cexp(cx: Double2D) -> Double2D:
    """

    """


@overload
def cexp(cx: Double3D) -> Double3D:
    """

    """


@overload
def cexp(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def cexp(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def cexp(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def clog(cx: Double1D) -> Double1D:
    """

    """


@overload
def clog(cx: Double2D) -> Double2D:
    """

    """


@overload
def clog(cx: Double3D) -> Double3D:
    """

    """


@overload
def clog(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def clog(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def clog(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def clog10(cx: Double1D) -> Double1D:
    """

    """


@overload
def clog10(cx: Double2D) -> Double2D:
    """

    """


@overload
def clog10(cx: Double3D) -> Double3D:
    """

    """


@overload
def clog10(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def clog10(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def clog10(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def cpow(cx: Float1D, ra: float) -> Float1D:
    """

    """


@overload
def cpow(cx: Float2D, ra: float) -> Float2D:
    """

    """


@overload
def cpow(cx: Float3D, ra: float) -> Float3D:
    """

    """


@overload
def cpow(cx: Float1D, ra: float, cy: Float1D) -> None:
    """

    """


@overload
def cpow(cx: Float2D, ra: float, cy: Float2D) -> None:
    """

    """


@overload
def cpow(cx: Float3D, ra: float, cy: Float3D) -> None:
    """

    """


@overload
def cpow(cx: Float1D, ca: Cfloat) -> Float1D:
    """

    """


@overload
def cpow(cx: Float2D, ca: Cfloat) -> Float2D:
    """

    """


@overload
def cpow(cx: Float3D, ca: Cfloat) -> Float3D:
    """

    """


@overload
def cpow(cx: Float1D, ca: Cfloat, cy: Float1D) -> None:
    """

    """


@overload
def cpow(cx: Float2D, ca: Cfloat, cy: Float2D) -> None:
    """

    """


@overload
def cpow(cx: Float3D, ca: Cfloat, cy: Float3D) -> None:
    """

    """


@overload
def cpow(cx: Double1D, ra: double) -> Double1D:
    """

    """


@overload
def cpow(cx: Double2D, ra: double) -> Double2D:
    """

    """


@overload
def cpow(cx: Double3D, ra: double) -> Double3D:
    """

    """


@overload
def cpow(cx: Double1D, ra: double, cy: Double1D) -> None:
    """

    """


@overload
def cpow(cx: Double2D, ra: double, cy: Double2D) -> None:
    """

    """


@overload
def cpow(cx: Double3D, ra: double, cy: Double3D) -> None:
    """

    """


@overload
def cpow(cx: Double1D, ca: Cdouble) -> Double1D:
    """

    """


@overload
def cpow(cx: Double2D, ca: Cdouble) -> Double2D:
    """

    """


@overload
def cpow(cx: Double3D, ca: Cdouble) -> Double3D:
    """

    """


@overload
def cpow(cx: Double1D, ca: Cdouble, cy: Double1D) -> None:
    """

    """


@overload
def cpow(cx: Double2D, ca: Cdouble, cy: Double2D) -> None:
    """

    """


@overload
def cpow(cx: Double3D, ca: Cdouble, cy: Double3D) -> None:
    """

    """


@overload
def creal(cx: Float1D) -> Float1D:
    """

    """


@overload
def creal(cx: Float2D) -> Float2D:
    """

    """


@overload
def creal(cx: Float3D) -> Float3D:
    """

    """


@overload
def creal(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def creal(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def creal(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def cimag(cx: Float1D) -> Float1D:
    """

    """


@overload
def cimag(cx: Float2D) -> Float2D:
    """

    """


@overload
def cimag(cx: Float3D) -> Float3D:
    """

    """


@overload
def cimag(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def cimag(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def cimag(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def cabs(cx: Float1D) -> Float1D:
    """

    """


@overload
def cabs(cx: Float2D) -> Float2D:
    """

    """


@overload
def cabs(cx: Float3D) -> Float3D:
    """

    """


@overload
def cabs(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def cabs(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def cabs(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def carg(cx: Float1D) -> Float1D:
    """

    """


@overload
def carg(cx: Float2D) -> Float2D:
    """

    """


@overload
def carg(cx: Float3D) -> Float3D:
    """

    """


@overload
def carg(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def carg(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def carg(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def cnorm(cx: Float1D) -> Float1D:
    """

    """


@overload
def cnorm(cx: Float2D) -> Float2D:
    """

    """


@overload
def cnorm(cx: Float3D) -> Float3D:
    """

    """


@overload
def cnorm(cx: Float1D, cy: Float1D) -> None:
    """

    """


@overload
def cnorm(cx: Float2D, cy: Float2D) -> None:
    """

    """


@overload
def cnorm(cx: Float3D, cy: Float3D) -> None:
    """

    """


@overload
def creal(cx: Double1D) -> Double1D:
    """

    """


@overload
def creal(cx: Double2D) -> Double2D:
    """

    """


@overload
def creal(cx: Double3D) -> Double3D:
    """

    """


@overload
def creal(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def creal(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def creal(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def cimag(cx: Double1D) -> Double1D:
    """

    """


@overload
def cimag(cx: Double2D) -> Double2D:
    """

    """


@overload
def cimag(cx: Double3D) -> Double3D:
    """

    """


@overload
def cimag(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def cimag(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def cimag(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def cabs(cx: Double1D) -> Double1D:
    """

    """


@overload
def cabs(cx: Double2D) -> Double2D:
    """

    """


@overload
def cabs(cx: Double3D) -> Double3D:
    """

    """


@overload
def cabs(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def cabs(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def cabs(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def carg(cx: Double1D) -> Double1D:
    """

    """


@overload
def carg(cx: Double2D) -> Double2D:
    """

    """


@overload
def carg(cx: Double3D) -> Double3D:
    """

    """


@overload
def carg(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def carg(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def carg(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def cnorm(cx: Double1D) -> Double1D:
    """

    """


@overload
def cnorm(cx: Double2D) -> Double2D:
    """

    """


@overload
def cnorm(cx: Double3D) -> Double3D:
    """

    """


@overload
def cnorm(cx: Double1D, cy: Double1D) -> None:
    """

    """


@overload
def cnorm(cx: Double2D, cy: Double2D) -> None:
    """

    """


@overload
def cnorm(cx: Double3D, cy: Double3D) -> None:
    """

    """


@overload
def cmplx(rx: Float1D, ry: Float1D) -> Float1D:
    """

    """


@overload
def cmplx(rx: Float2D, ry: Float2D) -> Float2D:
    """

    """


@overload
def cmplx(rx: Float3D, ry: Float3D) -> Float3D:
    """

    """


@overload
def cmplx(rx: Float1D, ry: Float1D, cz: Float1D) -> None:
    """

    """


@overload
def cmplx(rx: Float2D, ry: Float2D, cz: Float2D) -> None:
    """

    """


@overload
def cmplx(rx: Float3D, ry: Float3D, cz: Float3D) -> None:
    """

    """


@overload
def polar(rx: Float1D, ry: Float1D) -> Float1D:
    """

    """


@overload
def polar(rx: Float2D, ry: Float2D) -> Float2D:
    """

    """


@overload
def polar(rx: Float3D, ry: Float3D) -> Float3D:
    """

    """


@overload
def polar(rx: Float1D, ry: Float1D, cz: Float1D) -> None:
    """

    """


@overload
def polar(rx: Float2D, ry: Float2D, cz: Float2D) -> None:
    """

    """


@overload
def polar(rx: Float3D, ry: Float3D, cz: Float3D) -> None:
    """

    """


@overload
def cmplx(rx: Double1D, ry: Double1D) -> Double1D:
    """

    """


@overload
def cmplx(rx: Double2D, ry: Double2D) -> Double2D:
    """

    """


@overload
def cmplx(rx: Double3D, ry: Double3D) -> Double3D:
    """

    """


@overload
def cmplx(rx: Double1D, ry: Double1D, cz: Double1D) -> None:
    """

    """


@overload
def cmplx(rx: Double2D, ry: Double2D, cz: Double2D) -> None:
    """

    """


@overload
def cmplx(rx: Double3D, ry: Double3D, cz: Double3D) -> None:
    """

    """


@overload
def polar(rx: Double1D, ry: Double1D) -> Double1D:
    """

    """


@overload
def polar(rx: Double2D, ry: Double2D) -> Double2D:
    """

    """


@overload
def polar(rx: Double3D, ry: Double3D) -> Double3D:
    """

    """


@overload
def polar(rx: Double1D, ry: Double1D, cz: Double1D) -> None:
    """

    """


@overload
def polar(rx: Double2D, ry: Double2D, cz: Double2D) -> None:
    """

    """


@overload
def polar(rx: Double3D, ry: Double3D, cz: Double3D) -> None:
    """

    """


@overload
def csum(cx: Float1D) -> Cfloat:
    """

    """


@overload
def csum(cx: Float2D) -> Cfloat:
    """

    """


@overload
def csum(cx: Float3D) -> Cfloat:
    """

    """


@overload
def csum(cx: Double1D) -> Cdouble:
    """

    """


@overload
def csum(cx: Double2D) -> Cdouble:
    """

    """


@overload
def csum(cx: Double3D) -> Cdouble:
    """

    """


@overload
def tofloat(rx: Byte1D) -> Float1D:
    """

    """


@overload
def tofloat(rx: Byte2D) -> Float2D:
    """

    """


@overload
def tofloat(rx: Byte3D) -> Float3D:
    """

    """


@overload
def dump(rx: Byte1D) -> None:
    """

    """


@overload
def dump(rx: Byte2D) -> None:
    """

    """


@overload
def dump(rx: Byte3D) -> None:
    """

    """


@overload
def dump(rx: Short1D) -> None:
    """

    """


@overload
def dump(rx: Short2D) -> None:
    """

    """


@overload
def dump(rx: Short3D) -> None:
    """

    """


@overload
def dump(rx: Int1D) -> None:
    """

    """


@overload
def dump(rx: Int2D) -> None:
    """

    """


@overload
def dump(rx: Int3D) -> None:
    """

    """


@overload
def dump(rx: Long1D) -> None:
    """

    """


@overload
def dump(rx: Long2D) -> None:
    """

    """


@overload
def dump(rx: Long3D) -> None:
    """

    """


@overload
def dump(rx: Float1D) -> None:
    """

    """


@overload
def dump(rx: Float2D) -> None:
    """

    """


@overload
def dump(rx: Float3D) -> None:
    """

    """


@overload
def cdump(cx: Float1D) -> None:
    """

    """


@overload
def cdump(cx: Float2D) -> None:
    """

    """


@overload
def cdump(cx: Float3D) -> None:
    """

    """


@overload
def dump(rx: Double1D) -> None:
    """

    """


@overload
def dump(rx: Double2D) -> None:
    """

    """


@overload
def dump(rx: Double3D) -> None:
    """

    """


@overload
def cdump(cx: Double1D) -> None:
    """

    """


@overload
def cdump(cx: Double2D) -> None:
    """

    """


@overload
def cdump(cx: Double3D) -> None:
    """

    """
