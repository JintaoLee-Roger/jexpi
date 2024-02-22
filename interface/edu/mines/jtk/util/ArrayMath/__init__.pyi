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

from .ArrayMath import *
