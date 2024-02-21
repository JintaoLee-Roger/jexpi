from typing import overload
from edu.mines.jtk.mapping import *


class FftFilter:
    """
    A linear shift-invariant filter implemented by fast Fourier transform.
    This filtering is equivalent to computing the convolution y = hx,
    where h, x and y are filter, input and output arrays, respectively.
    
    The filter is specified as a 1D, 2D or 3D array of coefficients.
    Filter dimension must match that of arrays to be filtered. For
    example, a filter constructed with a 2D array of coefficients
    cannot be applied to a 1D array.
    
    The linear shift-invariant filtering performed by this class is a
    convolution sum. Each output sample in y is a sum of scaled input
    samples in x. For 1D filters this sum is
    <pre><code>
    nh-1-kh
    y[i] =  sum  h[kh+j]x[i-j] ; i = 0, 1, 2, ..., ny-1 = nx-1
    j=-kh
    </code></pre>
    For each output sample y[i], kh is the array index of the filter
    coefficient h[kh] that scales the corresponding input sample x[i].
    For example, in a symmetric filter with odd length nh, the index
    kh = (nh-1)/2 is that of the middle coefficient in the array h.
    In other words, kh is the array index of the filter's origin.
    
    The lengths nx and ny of the input and output arrays x and y are
    assumed to be equal. By default, values beyond the ends of an input
    array x in the convolution sum above are assumed to be zero. That
    is, zero values are used for x[i-j] when i-j &lt; 0 or when
    i-j &gt;= nx. Other methods for defining values beyond the ends of
    the array x may be specified. With any of these methods, the input
    array x is padded with extra values so that x[i-j] is defined for
    any i-j in the range [kh-nh+1:kh+nx-1] required by the convolution sum.
    
    For efficiency, this filter can cache the fast Fourier transform of
    its coefficients h when the filter is first applied to any input
    array x. The filter may then be applied again, without recomputing
    its FFT, to other input arrays x that have the same lengths. The FFT
    of a cached filter is recomputed only when the lengths of the input
    and output arrays have changed. Because this caching consumes memory,
    it is disabled by default.
    """

    @overload
    def __init__(self, h: Float1D) -> None:
        """
        Constructs an FFT filter for specified filter coefficients.
        The filter's origin is the center of the array.
        
        Parameters
        -----------
        h : Float1D
            array of filter coefficients; copied, not referenced.
        """

    @overload
    def __init__(self, kh: int, h: Float1D) -> None:
        """
        Constructs an FFT filter for specified filter coefficients.
        The coefficient h[kh] corresponds to the filter's origin.
        
        Parameters
        -----------
        kh : int
            array index of the filter's origin.
        h : Float1D
            array of filter coefficients; copied, not referenced.
        """

    @overload
    def __init__(self, h: Float2D) -> None:
        """
        Constructs an FFT filter for specified filter coefficients.
        The filter's origin is the center of the array.
        
        Parameters
        -----------
        h : Float2D
            array of filter coefficients; copied, not referenced.
        """

    @overload
    def __init__(self, kh1: int, kh2: int, h: Float2D) -> None:
        """
        Constructs an FFT filter for specified filter coefficients.
        The coefficient h[kh2][kh1] corresponds to the filter's origin.
        
        Parameters
        -----------
        kh1 : int
            array index in 1st dimension of the filter's origin.
        kh2 : int
            array index in 2nd dimension of the filter's origin.
        h : Float2D
            array of filter coefficients; copied, not referenced.
        """

    @overload
    def __init__(self, h: Float3D) -> None:
        """
        Constructs an FFT filter for specified filter coefficients.
        The filter's origin is the center of the array.
        
        Parameters
        -----------
        h : Float3D
            array of filter coefficients; copied, not referenced.
        """

    @overload
    def __init__(self, kh1: int, kh2: int, kh3: int, h: Float3D) -> None:
        """
        Constructs an FFT filter for specified filter coefficients.
        The coefficient h[kh3][kh2][kh1] corresponds to the filter's origin.
        
        Parameters
        -----------
        kh1 : int
            array index in 1st dimension of the filter's origin.
        kh2 : int
            array index in 2nd dimension of the filter's origin.
        kh3 : int
            array index in 3rd dimension of the filter's origin.
        h : Float3D
            array of filter coefficients; copied, not referenced.
        """

    def setExtrapolation(self, extrapolation: Extrapolation) -> None:
        """
        Sets the method used to extrapolate values beyond the ends of input arrays.
        
        Parameters
        -----------
        extrapolation : Extrapolation
            the extrapolation method.
        """

    def setFilterCaching(self, filterCaching: bool) -> None:
        """
        Enables or disables caching of the Fourier transform of the filter.
        Caching consumes memory but improves performance by about 50% when
        the same filter is applied repeatedly to arrays that have the same
        dimensions.
        
        Parameters
        -----------
        filterCaching : bool
            true, to enable caching; false, to disable.
        """

    @overload
    def apply(self, x: Float1D) -> Float1D:
        """
        Applies this filter.
        
        Parameters
        -----------
        x : Float1D
            input array.
        
        Returns
        --------
        output : Float1D
            filtered array.
        """

    @overload
    def apply(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter.
        Input and output arrays may be the same array.
        
        Parameters
        -----------
        x : Float1D
            input array.
        y : Float1D
            output array.
        """

    @overload
    def apply(self, x: Float2D) -> Float2D:
        """
        Applies this filter.
        
        Parameters
        -----------
        x : Float2D
            input array.
        
        Returns
        --------
        output : Float2D
            filtered array.
        """

    @overload
    def apply(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter.
        Input and output arrays may be the same array.
        
        Parameters
        -----------
        x : Float2D
            input array.
        y : Float2D
            output filtered array.
        """

    @overload
    def apply(self, x: Float3D) -> Float3D:
        """
        Applies this filter.
        
        Parameters
        -----------
        x : Float3D
            input array.
        
        Returns
        --------
        output : Float3D
            filtered array.
        """

    @overload
    def apply(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter.
        Input and output arrays may be the same array.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output filtered array.
        """
