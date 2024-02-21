from typing import overload
from edu.mines.jtk.mapping import *


class HilbertTransformFilter:
    """
    Hilbert transform of band-limited uniformly-sampled functions.
    This filter is also known as a 90-degree phase shifter.
    
    The sign of the transform (the sign of the 90-degree phase shift)
    is the same as that for a derivative filter, such that the Hilbert
    transform of sin(t) is cos(t).
    
    The ideal Hilbert transform filter is infinitely long. The
    length of the filter used here is chosen to yield less than a
    specified maximum error for frequencies between specified lower
    and upper bounds.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a Hilbert transform filter that yields less than 1% error
        for frequencies between 5% and 95% of the Nyquist frequency.
        """

    @overload
    def __init__(self, nmax: int, emax: float, fmin: float,
                 fmax: float) -> None:
        """
        Constructs a Hilbert transform filter that yields less than a specified
        maximum error for frequencies between specified lower and upper bounds.
        Must be greater than 0.
        Must be greater than 0.0.
        If the computed filter has fewer than nmax coefficients, then for
        frequencies between fmin and fmax, the amplitude spectrum of each
        filter will be bounded by 1-emax and 1+emax.
        The length of the filter grows approximately as the logarithm of 1/emax.
        Must be greater than 0.0.
        The length of the filter grows approximately as 1/fmin.
        Must be less than the 0.5 (the Nyquist frequency).
        The length of the filter grows approximately as 1/(0.5-fmax).
        
        Parameters
        -----------
        nmax : int
            maximum number of coefficients in filter.
        emax : float
            maximum error.
        fmin : float
            minimum frequency (in cycles/sample)
        fmax : float
            maximum frequency (in cycles/sample).
        """

    def apply(self, n: int, x: Float1D, y: Float1D) -> None:
        """
        Applies this Hilbert transform filter.
        
        Parameters
        -----------
        n : int
            number of samples in input/output arrays.
        x : Float1D
            array[n] of input samples.
        y : Float1D
            array[n] of output samples.
        """

    def length(self) -> int:
        """
        Gets the length of this Hilbert transform filter.
        Returns
        --------
        output : int
            filter length.
        """
