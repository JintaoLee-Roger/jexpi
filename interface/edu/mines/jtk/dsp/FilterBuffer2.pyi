from typing import overload
from edu.mines.jtk.mapping import *


class FilterBuffer2:
    """
    A buffer that facilitates the implementation of 2D filters. In effect,
    this class pads a 2D array with extra values on the sides, but without
    making a padded copy of the entire 2D array. Instead, this buffer
    maintains copies of only a subset of the 1D arrays stored in the 2D
    array. For typical 2D filters, that subset includes all input values
    required to update a subset (often a single 1D array) of output values.
    
    Output (filtered) values y[i2][i1] are assumed to depend on a limited
    subset of input values x[i2-l2:i2+m2][i1-l1:i1+m1], where l1, m1, l2,
    and m2 are non-negative integers that define the extent of the filter.
    Finite-difference stencils are examples of such filters.
    
    One purpose of this buffer is to pad the input array so that indices
    such as i1-l1, i1+m1, i2-l2, and i2+m2 are never out of bounds, say,
    when i1-l1&lt;0. Instead, values are extrapolated, when necessary.
    Padding with extrapolated values simplifies filters by eliminating
    special processing near the ends of arrays. Here, for example, is a
    program for a simple five-sample finite-difference approximation to
    a Laplacian:
    <pre><code>
    float[][] x = ... // an array[n2][n1] of input values
    float[][] y = ... // an array[n2][n1] of output values
    FilterBuffer2 fbx = new FilterBuffer2(1,1,1,1,x); // l1 = m1 = l2 = m2 = 1
    fbx.setExtrapolation(FilterBuffer2.Extrapolation.ZERO_SLOPE);
    for (int i2=0; i2&lt;n2; ++i2) { // the outer loop
    float[] xm = fbx.get(i2-1); // x[i2-1], extrapolation when i2 = 0
    float[] x0 = fbx.get(i2  ); // x[i2  ], extrapolation unnecessary
    float[] xp = fbx.get(i2+1); // x[i2+1], extrapolation when i2 = n2-1
    float[] y0 = y[i2]; // cache output array reference, for efficiency
    for (int i1=0,j1=1; i1&lt;n1; ++i1,++j1) // the inner loop
    y0[i1] = xm[j1]+xp[j1]+x0[j1-1]+x0[j1+1]-4.0fx0[j1];
    }
    </code></pre>
    In the inner loop, the input index j1 is one greater than the output
    index i1. This difference accounts for the padding with an extra
    l1 = 1 value at the beginning of the arrays xm, x0 and xp. An extra
    m1 = 1 value of padding is also provided at the end of each of these
    three arrays. In other words, the arrays xm, x0 and xp each contain
    l1+n1+m1 values. This padding enables the inner loop to be written
    simply, with no special cases near the ends of the arrays.
    
    While simple, the program above is also efficient. First, the buffer
    contains only three 1D arrays, independent of the 2D array length n2.
    Second, although input array values must be copied to the buffer,
    those values are used multiple times before being replaced by other
    values.
    
    Another purpose of this class is to facilitate filtering in place. In
    the example above, the input array x and output array y can be the same
    array, so that output values replace input values. This works because
    input values x are copied into the buffer <em>before</em> they are
    overwritten by output values y.
    """

    @overload
    def __init__(self, l1: int, m1: int, l2: int, m2: int, a: Float2D) -> None:
        """
        Constructs a buffer for the specified array. The buffer will
        store l2+1+m2 1D arrays, each with l1+n1+m1 values. Array
        lengths n1 and n2 are set to n1=a[0].length and n2=a.length.
        
        Parameters
        -----------
        l1 : int
            number of extra values at beginning in 1st dimension.
        m1 : int
            number of extra values at end in 1st dimension.
        l2 : int
            number of extra values at beginning in 2nd dimension.
        m2 : int
            number of extra values at end in 2nd dimension.
        a : Float2D
            the array[n2][n1] of values to be buffered.
        """

    @overload
    def __init__(self, l1: int, m1: int, n1: int, l2: int, m2: int,
                 n2: int) -> None:
        """
        Constructs a buffer for specified array lengths. The buffer
        will store l2+1+m2 1D arrays, each with l1+n1+m1 values. Array
        lengths n1 and n2 are specified explicitly here. An array with
        those lengths must be specified later, but before accessing
        buffered values.
        
        Parameters
        -----------
        l1 : int
            number of extra values at beginning in 1st dimension.
        m1 : int
            number of extra values at end in 1st dimension.
        n1 : int
            number of values (not counting extras) in 1st dimension.
        l2 : int
            number of extra values at beginning in 2nd dimension.
        m2 : int
            number of extra values at end in 2nd dimension.
        n2 : int
            number of values (not counting extras) in 2nd dimension.
        """

    def setArray(self, a: Float2D) -> None:
        """
        Sets the array of values to be buffered. Array lengths must match
        those with which this buffer was constructed. Any values currently
        in this buffer are forgotten. Therefore, this method should not be
        called while looping over array values.
        
        Parameters
        -----------
        a : Float2D
            the array; referenced, not copied.
        """

    def setExtrapolation(self, extrapolation: Extrapolation) -> None:
        """
        Sets the method used to extrapolate values beyond the ends of arrays.
        
        Parameters
        -----------
        extrapolation : Extrapolation
            the extrapolation method.
        """

    def setMode(self, mode: Mode) -> None:
        """
        Sets the mode (input, output, or input-output) for this buffer.
        
        Parameters
        -----------
        mode : Mode
            the mode.
        """

    def get(self, i2: int) -> Float1D:
        """
        Copies values from the buffered array into this buffer.
        If the values are already in this buffer, they are assumed to be
        unchanged, and no copy is performed. In either case, this method
        returns a referenced to the buffered values.
        
        The returned buffered array has l1+m1 extra values at the ends;
        the first l1 values and the last m1 values are extrapolated.
        
        Parameters
        -----------
        i2 : int
            index in 2nd dimension of the buffered array to get.
        
        Returns
        --------
        output : Float1D
            reference to an array of buffered values.
        """

    def flush(self) -> None:
        """
        Flushes this buffer, if it is an output or input-output buffer.
        Flushing copies all values (except extrapolated values) from this
        buffer to its buffered array. This method should be called after
        any loops in which output values have been buffered. For input-only
        buffers, this method does nothing.
        """
