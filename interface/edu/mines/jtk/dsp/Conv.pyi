from typing import overload
from edu.mines.jtk.mapping import *


class Conv:
    """
    Computes the convolution (or cross-correlation) of two sequences.
    
    Convolution of one-dimensional sequences x and y is defined generically
    by the following sum:
    <pre><code>
    z[i] =  sum x[j]y[i-j]
    j
    </code></pre>
    In practice, the sequences x, y, and z are non-zero for only finite
    ranges of sample indices i and j, and these ranges determine limits
    on the summation index j.
    
    Specifically, the sequences x, y, and z are stored in arrays with
    zero-based indexing; e.g., x[0], x[1], x[2], ..., x[lx-1], where lx
    denotes the length of the array x. Sequences are assumed to be zero
    for indices outside the bounds of these arrays.
    
    Note that an array index need not equal its corresponding sample index.
    For each sequence, we must specify the sample index of the first sample
    in the array of sample values; e.g., kx denotes the sample index of x[0].
    With this distinction between sample and array indices in mind, in terms
    of arrays x, y, and z, the convolution sum may be rewritten as
    <pre><code>
    jhi
    z[i-k] =  sum  x[j]y[i-j] ; i = k, k+1, ..., k+lz-1
    j=jlo
    </code></pre>
    where k = kz-kx-ky, jlo = max(0,i-ly+1), and jhi = min(lx-1,i). The
    summation limits jlo and jhi ensure that array indices are always in
    bounds. The effect of the three first-sample indices is encoded in the
    single shift k.
    
    For example, if sequence z is to be a weighted average of the nearest
    five samples of sequence y, one might use
    <pre><code>
    ...
    x[0] = x[1] = x[2] = x[3] = x[4] = 1.0/5.0;
    conv(5,-2,x,ly,0,y,ly,0,z);
    ...
    </code></pre>
    In this example, the sequence x is symmetric about the origin, with
    first-sample index kx = -2.
    
    Cross-correlation is similar to convolution. (Indeed, cross-correlation
    of x and y equals the convolution of x-reversed and y. The generic
    definition of cross-correlation is
    <pre><code>
    z[i] =  sum x[j]y[i+j]
    j
    </code></pre>
    Unlike convolution, cross-correlation is not commutative. In other words,
    the cross-correlation of x and y does not equal the cross-correlation of
    y and x.
    """

    @overload
    @staticmethod
    def conv(self, lx: int, kx: int, x: Float1D, ly: int, ky: int, y: Float1D,
             lz: int, kz: int, z: Float1D) -> None:
        """
        Computes the 1-D convolution of specified sequences x and y.
        
        Parameters
        -----------
        lx : int
            the length of x.
        kx : int
            the sample index of x[0].
        x : Float1D
            array[lx] of x values.
        ly : int
            the length of y.
        ky : int
            the sample index of y[0].
        y : Float1D
            array[ly] of y values.
        lz : int
            the length of z.
        kz : int
            the sample index of z[0].
        z : Float1D
            array[lz] of z values.
        """

    @overload
    @staticmethod
    def conv(self, lx1: int, lx2: int, kx1: int, kx2: int, x: Float2D,
             ly1: int, ly2: int, ky1: int, ky2: int, y: Float2D, lz1: int,
             lz2: int, kz1: int, kz2: int, z: Float2D) -> None:
        """
        Computes the 2-D convolution of specified sequences x and y.
        
        Parameters
        -----------
        lx1 : int
            the length of x in 1st dimension.
        lx2 : int
            the length of x in 2nd dimension.
        kx1 : int
            the sample index in 1st dimension of x[0][0].
        kx2 : int
            the sample index in 2nd dimension of x[0][0].
        x : Float2D
            array[lx2][lx1] of x values.
        ly1 : int
            the length of y in 1st dimension.
        ly2 : int
            the length of y in 2nd dimension.
        ky1 : int
            the sample index in 1st dimension of y[0][0].
        ky2 : int
            the sample index in 2nd dimension of y[0][0].
        y : Float2D
            array[ly2][ly1] of y values.
        lz1 : int
            the length of z in 1st dimension.
        lz2 : int
            the length of z in 2nd dimension.
        kz1 : int
            the sample index in 1st dimension of z[0][0].
        kz2 : int
            the sample index in 2nd dimension of z[0][0].
        z : Float2D
            array[lz2][lz1] of z values.
        """

    @overload
    @staticmethod
    def conv(self, lx1: int, lx2: int, lx3: int, kx1: int, kx2: int, kx3: int,
             x: Float3D, ly1: int, ly2: int, ly3: int, ky1: int, ky2: int,
             ky3: int, y: Float3D, lz1: int, lz2: int, lz3: int, kz1: int,
             kz2: int, kz3: int, z: Float3D) -> None:
        """
        Computes the 3-D convolution of specified sequences x and y.
        
        Parameters
        -----------
        lx1 : int
            the length of x in 1st dimension.
        lx2 : int
            the length of x in 2nd dimension.
        lx3 : int
            the length of x in 3rd dimension.
        kx1 : int
            the sample index in 1st dimension of x[0][0][0].
        kx2 : int
            the sample index in 2nd dimension of x[0][0][0].
        kx3 : int
            the sample index in 3rd dimension of x[0][0][0].
        x : Float3D
            array[lx3][lx2][lx1] of x values.
        ly1 : int
            the length of y in 1st dimension.
        ly2 : int
            the length of y in 2nd dimension.
        ly3 : int
            the length of y in 3rd dimension.
        ky1 : int
            the sample index in 1st dimension of y[0][0][0].
        ky2 : int
            the sample index in 2nd dimension of y[0][0][0].
        ky3 : int
            the sample index in 3rd dimension of y[0][0][0].
        y : Float3D
            array[ly3][ly2][ly1] of y values.
        lz1 : int
            the length of z in 1st dimension.
        lz2 : int
            the length of z in 2nd dimension.
        lz3 : int
            the length of z in 3rd dimension.
        kz1 : int
            the sample index in 1st dimension of z[0][0][0].
        kz2 : int
            the sample index in 2nd dimension of z[0][0][0].
        kz3 : int
            the sample index in 3rd dimension of z[0][0][0].
        z : Float3D
            array[lz3][lz2][lz1] of z values.
        """

    @overload
    @staticmethod
    def xcor(self, lx: int, kx: int, x: Float1D, ly: int, ky: int, y: Float1D,
             lz: int, kz: int, z: Float1D) -> None:
        """
        Computes the 1-D cross-correlation of specified sequences x and y.
        
        Parameters
        -----------
        lx : int
            the length of x.
        kx : int
            the sample index of x[0].
        x : Float1D
            array[lx] of x values.
        ly : int
            the length of y.
        ky : int
            the sample index of y[0].
        y : Float1D
            array[ly] of y values.
        lz : int
            the length of z.
        kz : int
            the sample index of z[0].
        z : Float1D
            array[lz] of z values.
        """

    @overload
    @staticmethod
    def xcor(self, lx1: int, lx2: int, kx1: int, kx2: int, x: Float2D,
             ly1: int, ly2: int, ky1: int, ky2: int, y: Float2D, lz1: int,
             lz2: int, kz1: int, kz2: int, z: Float2D) -> None:
        """
        Computes the 2-D cross-correlation of specified sequences x and y.
        
        Parameters
        -----------
        lx1 : int
            the length of x in 1st dimension.
        lx2 : int
            the length of x in 2nd dimension.
        kx1 : int
            the sample index in 1st dimension of x[0][0].
        kx2 : int
            the sample index in 2nd dimension of x[0][0].
        x : Float2D
            array[lx2][lx1] of x values.
        ly1 : int
            the length of y in 1st dimension.
        ly2 : int
            the length of y in 2nd dimension.
        ky1 : int
            the sample index in 1st dimension of y[0][0].
        ky2 : int
            the sample index in 2nd dimension of y[0][0].
        y : Float2D
            array[ly2][ly1] of y values.
        lz1 : int
            the length of z in 1st dimension.
        lz2 : int
            the length of z in 2nd dimension.
        kz1 : int
            the sample index in 1st dimension of z[0][0].
        kz2 : int
            the sample index in 2nd dimension of z[0][0].
        z : Float2D
            array[lz2][lz1] of z values.
        """

    @overload
    @staticmethod
    def xcor(self, lx1: int, lx2: int, lx3: int, kx1: int, kx2: int, kx3: int,
             x: Float3D, ly1: int, ly2: int, ly3: int, ky1: int, ky2: int,
             ky3: int, y: Float3D, lz1: int, lz2: int, lz3: int, kz1: int,
             kz2: int, kz3: int, z: Float3D) -> None:
        """
        Computes the 3-D cross-correlation of specified sequences x and y.
        
        Parameters
        -----------
        lx1 : int
            the length of x in 1st dimension.
        lx2 : int
            the length of x in 2nd dimension.
        lx3 : int
            the length of x in 3rd dimension.
        kx1 : int
            the sample index in 1st dimension of x[0][0][0].
        kx2 : int
            the sample index in 2nd dimension of x[0][0][0].
        kx3 : int
            the sample index in 3rd dimension of x[0][0][0].
        x : Float3D
            array[lx3][lx2][lx1] of x values.
        ly1 : int
            the length of y in 1st dimension.
        ly2 : int
            the length of y in 2nd dimension.
        ly3 : int
            the length of y in 3rd dimension.
        ky1 : int
            the sample index in 1st dimension of y[0][0][0].
        ky2 : int
            the sample index in 2nd dimension of y[0][0][0].
        ky3 : int
            the sample index in 3rd dimension of y[0][0][0].
        y : Float3D
            array[ly3][ly2][ly1] of y values.
        lz1 : int
            the length of z in 1st dimension.
        lz2 : int
            the length of z in 2nd dimension.
        lz3 : int
            the length of z in 3rd dimension.
        kz1 : int
            the sample index in 1st dimension of z[0][0][0].
        kz2 : int
            the sample index in 2nd dimension of z[0][0][0].
        kz3 : int
            the sample index in 3rd dimension of z[0][0][0].
        z : Float3D
            array[lz3][lz2][lz1] of z values.
        """
