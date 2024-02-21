from typing import overload
from edu.mines.jtk.mapping import *


class LocalCorrelationFilter:
    """
    Local cross-correlation of two arrays with seamless overlapping windows.
    Given two input arrays f and g and a specified lag, this filter computes
    an output array c of local cross-correlation coefficients, one for each
    sample in the input arrays f and g.
    
    Two types of cross-correlation are implemented. Both types can be
    normalized to obtain cross-correlation coefficients with magnitudes
    that do not exceed one. The normalization varies, depending on the
    type of cross-correlation.
    
    <em>Simple</em> cross-correlation computes an array of products
    h[j] = f[j]g[j+lag] and then filters this array of products with a
    window. The resulting correlation cfg[k,lag] is not symmetric with
    respect to lag; cfg[k,-lag] = cgf[k-lag,lag] != cgf[k,lag]. For
    simple cross-correlation, normalization scale factors vary with lag
    and should be applied before picking correlation peaks.
    
    <em>Symmetric</em> cross-correlation computes an array of products
    h[j] = f[j-lag/2]g[j+lag/2] and therefore requires interpolation
    between samples for odd lags. (For efficiency, we interpolate the
    products h, not the inputs f and g.) The resulting correlation is
    symmetric with respect to lag; cfg[k,lag] = cgf[k,-lag]. Moreover,
    when inputs f and g are the same, each local auto-correlation has a
    Fourier transform (a power spectrum) that is positive-semidefinite.
    For symmetric cross-correlation, normalization scale factors do not
    vary with lag, and therefore need not be applied before picking
    correlation peaks.
    
    Two correlation windows are implemented: Gaussian and rectangular.
    Gaussian windows should be used for most applications. Rectangular
    windows are provided primarily for comparison, because they are so
    often used by others.
    """

    @overload
    def __init__(self, type: Type, window: Window, sigma: double) -> None:
        """
        Construct a correlation filter with specified parameters.
        When applied to multi-dimensional arrays, the filter has the
        same half-width for all dimensions.
        
        Parameters
        -----------
        type : Type
            the correlation type.
        window : Window
            the correlation window.
        sigma : double
            the correlation window half-width; must not be less than 1.
        """

    @overload
    def __init__(self, type: Type, window: Window, sigma1: double,
                 sigma2: double) -> None:
        """
        Construct a correlation filter with specified parameters.
        When applied to multi-dimensional arrays, the filter has half-width
        sigma1 for the 1st dimension and half-width sigma2 for 2nd and higher
        dimensions.
        must not be less than 1.
        dimensions; must not be less than 1.
        
        Parameters
        -----------
        type : Type
            the correlation type.
        window : Window
            the correlation window.
        sigma1 : double
            correlation window half-width for 1st dimension;
        sigma2 : double
            correlation window half-width for 2nd and higher
        """

    @overload
    def __init__(self, type: Type, window: Window, sigma1: double,
                 sigma2: double, sigma3: double) -> None:
        """
        Construct a correlation filter with specified parameters.
        When applied to multi-dimensional arrays, the filter has half-width
        sigma1 for the 1st dimension, half-width sigma2 for the 2nd dimension,
        and half-width sigma3 for 3rd and higher dimensions.
        must not be less than 1.
        must not be less than 1.
        dimensions; must not be less than 1.
        
        Parameters
        -----------
        type : Type
            the correlation type.
        window : Window
            the correlation window.
        sigma1 : double
            correlation window half-width for 1st dimension;
        sigma2 : double
            correlation window half-width for 2nd dimension;
        sigma3 : double
            correlation window half-width for 3rd and higher
        """

    @overload
    def setInputs(self, f: Float1D, g: Float1D) -> None:
        """
        Sets the input arrays to be cross-correlated.
        The input arrays f and g can be the same array.
        
        Parameters
        -----------
        f : Float1D
            the input array f; by reference, not copied.
        g : Float1D
            the input array g; by reference, not copied.
        """

    @overload
    def setInputs(self, f: Float2D, g: Float2D) -> None:
        """
        Sets the input arrays to be cross-correlated.
        The input arrays f and g can be the same array.
        
        Parameters
        -----------
        f : Float2D
            the input array f; by reference, not copied.
        g : Float2D
            the input array g; by reference, not copied.
        """

    @overload
    def setInputs(self, f: Float3D, g: Float3D) -> None:
        """
        Sets the input arrays to be cross-correlated.
        The input arrays f and g can be the same array.
        
        Parameters
        -----------
        f : Float3D
            the input array f; by reference, not copied.
        g : Float3D
            the input array g; by reference, not copied.
        """

    @overload
    def correlate(self, lag: int, c: Float1D) -> None:
        """
        Correlates the current inputs for the specified lag.
        
        Parameters
        -----------
        lag : int
            the correlation lag.
        c : Float1D
            the output array; cannot be the same as inputs f or g.
        """

    @overload
    def correlate(self, lag1: int, lag2: int, c: Float2D) -> None:
        """
        Correlates the current inputs for the specified lag.
        
        Parameters
        -----------
        lag1 : int
            the lag in the 1st dimension.
        lag2 : int
            the lag in the 2nd dimension.
        c : Float2D
            the output array; cannot be the same as inputs f or g.
        """

    @overload
    def correlate(self, lag1: int, lag2: int, lag3: int, c: Float3D) -> None:
        """
        Correlates the current inputs for the specified lag.
        
        Parameters
        -----------
        lag1 : int
            the lag in the 1st dimension.
        lag2 : int
            the lag in the 2nd dimension.
        lag3 : int
            the lag in the 3rd dimension.
        c : Float3D
            the output array; cannot be the same as inputs f or g.
        """

    @overload
    def normalize(self, lag: int, c: Float1D) -> None:
        """
        Normalizes the cross-correlation for a specified lag.
        
        Parameters
        -----------
        lag : int
            the lag.
        c : Float1D
            the cross-correlation to be modified.
        """

    @overload
    def normalize(self, lag1: int, lag2: int, c: Float2D) -> None:
        """
        Normalizes the cross-correlation for a specified lag.
        
        Parameters
        -----------
        lag1 : int
            the lag in the 1st dimension.
        lag2 : int
            the lag in the 2nd dimension.
        c : Float2D
            the cross-correlation to be modified.
        """

    @overload
    def normalize(self, lag1: int, lag2: int, lag3: int, c: Float3D) -> None:
        """
        Normalizes the cross-correlation for a specified lag.
        
        Parameters
        -----------
        lag1 : int
            the lag in the 1st dimension.
        lag2 : int
            the lag in the 2nd dimension.
        lag3 : int
            the lag in the 3rd dimension.
        c : Float3D
            the cross-correlation to be modified.
        """

    @overload
    def unbias(self, f: Float1D) -> Float1D:
        """
        Removes bias by subtracting local means from the specified array.
        
        Parameters
        -----------
        f : Float1D
            the input array.
        
        Returns
        --------
        output : Float1D
            the output array, with bias subtracted.
        """

    @overload
    def unbias(self, f: Float2D) -> Float2D:
        """
        Removes bias by subtracting local means from the specified array.
        
        Parameters
        -----------
        f : Float2D
            the input array.
        
        Returns
        --------
        output : Float2D
            the output array, with bias subtracted.
        """

    @overload
    def unbias(self, f: Float3D) -> Float3D:
        """
        Removes bias by subtracting local means from the specified array.
        
        Parameters
        -----------
        f : Float3D
            the input array.
        
        Returns
        --------
        output : Float3D
            the output array, with bias subtracted.
        """
