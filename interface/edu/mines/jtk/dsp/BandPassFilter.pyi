from typing import overload
from edu.mines.jtk.mapping import *


class BandPassFilter:
    """
    A multi-dimensional band-pass filter. Filtering is performed using fast
    Fourier transforms. The result is equivalent to convolution with an
    ideal symmetric (zero-phase) band-pass filter that has been smoothly
    tapered to zero.
    
    Filter parameters include lower and upper frequencies that define the
    pass band, the width of the transition from pass band to stop bands,
    and the maximum error for amplitude in both pass and stop bands.
    
    For efficiency the Fourier transform of the filter may be cached for
    repeated application to multiple input arrays. A cached transform
    can be reused while the lengths of input and output arrays do not
    change. Because caching consumes memory, it is disabled by default.
    """

    def __init__(self, klower: double, kupper: double, kwidth: double,
                 aerror: double) -> None:
        """
        Constructs a band-pass filter with specified parameters.
        
        Parameters
        -----------
        klower : double
            the lower pass band frequency, in cycles per sample.
        kupper : double
            the upper pass band frequency, in cycles per sample.
        kwidth : double
            width of the transition between pass and stop bands.
        aerror : double
            approximate bound on amplitude error, a positive fraction.
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

    def getCoefficients1(self) -> Float1D:
        """
        Gets the 1D array of coefficients for this filter.
        The origin of the filter is at the center of the array.
        Returns
        --------
        output : Float1D
            the array of filter coefficients.
        """

    def getCoefficients2(self) -> Float2D:
        """
        Gets the 2D array of coefficients for this filter.
        The origin of the filter is at the center of the array.
        Returns
        --------
        output : Float2D
            the array of filter coefficients.
        """

    def getCoefficients3(self) -> Float3D:
        """
        Gets the 3D array of coefficients for this filter.
        The origin of the filter is at the center of the array.
        Returns
        --------
        output : Float3D
            the array of filter coefficients.
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
            output filtered array.
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
