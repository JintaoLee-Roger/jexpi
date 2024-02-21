from typing import overload
from edu.mines.jtk.mapping import *


class ButterworthFilter:
    """
    Butterworth filter.
    """

    @overload
    def __init__(self, fl: double, al: double, fh: double, ah: double) -> None:
        """
        Construct a Butterworth filter with specified parameters.
        The filter is specified by amplitudes at two frequencies. The
        frequencies are in normalized units of cycles/sample. Either a
        low-pass or high-pass filter is constructed, depending on which
        of the corresponding two amplitudes is smaller. The filter is
        designed to match the larger (pass band) amplitude exactly, but
        may have amplitude lower than the smaller (reject band) amplitude.
        The low frequency fl must be greater than 0.0 and less than fh.
        The amplitude al must be greater than 0.0, less than 1.0, and
        not equal to the amplitude ah.
        The high frequency fh must be less than 0.5 and greater than fl.
        The amplitude ah must be greater than 0.0, less than 1.0, and
        not equal to the amplitude al.
        
        Parameters
        -----------
        fl : double
            the low frequency at which the amplitude al is specified.
        al : double
            the amplitude at the specified low frequency fl.
        fh : double
            the high frequency at which the amplitude ah is is specified.
        ah : double
            the amplitude at the specified high frequency fh.
        """

    @overload
    def __init__(self, fc: double, np: int, type: Type) -> None:
        """
        Construct Butterworth filter with specified parameters.
        At this cutuff frequency, the filter amplitude squared equals 0.5.
        The cutoff frequency must be greater than 0.0 and less than 0.5.
        
        Parameters
        -----------
        fc : double
            the cutoff (half-power) frequency, in cycles per sample.
        np : int
            the number of poles in the recursive filter.
        type : Type
            the filter type.
        """
