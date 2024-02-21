from typing import overload
from edu.mines.jtk.mapping import *


class KaiserWindow:
    """
    The Kaiser window is often used in FIR filter design. It is easy to
    use and exhibits near-optimal properties for many filter design
    problems. The window is defined by any two of three parameters:
    window length, transition width, and maximum absolute error.
    
    For definiteness, assume that the Kaiser window is a function w(x)
    of argument x. Then, the window length is that range of x, centered
    about x = 0, for which the Kaiser window is non-zero. In other words,
    w(x) = 0 for |x| &gt; length/2. When windowing functions of time, both
    the window length and the argument x of w(x) have dimensions of time.
    
    The transition width is the width of the central lobe in the Fourier
    transform of the window. For band-pass filters, this is the width of
    the transition between pass and stop bands. When windowing functions
    of time, the dimensions of transition width are cycles per unit time
    (frequency). In any case, the product of window length and transition
    width is dimensionless.
    
    The maximum absolute error corresponds to the magnitude of ripples in
    the passbands and stopbands of windowed filters. For an ideal band-pass
    filter that has magnitude one in the pass band, the maximum (or minimum)
    amplitude in the passband of a windowed filter is one plus (or minus)
    the maximum amplitude error. Likewise, the maximum amplitude in the
    stopband of such a windowed filter equals the maximum amplitude error.
    
    Kaiser windows are based on approximate relationships among the three
    design parameters. These approximations break down for passbands and
    stopbands that are narrow relative to the transition width. In such
    cases, the actual maximum error may exceed a specified maximum error
    for which a Kaiser window is designed by up to a factor of two.
    
    When constructing a Kaiser window for a specified window length and
    transition width, the product of these two parameters cannot be less
    than one. When lengthwidth is less than one, a useful upper bound for
    the maximum absolute error cannot be obtained from the Kaiser window
    design equations. However, in this case, the lower bound for maximum
    absolute error is nearly 10%, which is too large for most applications
    anyway. Therefore, in practice, this restriction seldom matters.
    """

    @staticmethod
    def fromErrorAndWidth(self, error: double, width: double) -> KaiserWindow:
        """
        Returns a Kaiser window with specified error and transition width.
        
        Parameters
        -----------
        error : double
            the maximum absolute error.
        width : double
            the transition width.
        
        Returns
        --------
        output : KaiserWindow
            the window.
        """

    @staticmethod
    def fromErrorAndLength(self, error: double,
                           length: double) -> KaiserWindow:
        """
        Returns a Kaiser window with specified error and window length.
        
        Parameters
        -----------
        error : double
            the maximum absolute error.
        length : double
            the two-sided window length.
        
        Returns
        --------
        output : KaiserWindow
            the window.
        """

    @staticmethod
    def fromWidthAndLength(self, width: double,
                           length: double) -> KaiserWindow:
        """
        Returns a Kaiser window with specified transition width and window length.
        The product widthlength cannot be less than one.
        
        Parameters
        -----------
        width : double
            the transition width
        length : double
            the two-sided window length.
        
        Returns
        --------
        output : KaiserWindow
            the window.
        """

    def evaluate(self, x: double) -> double:
        """
        Returns the value of this Kaiser window function w(x) for specified x.
        
        Parameters
        -----------
        x : double
            the argument for which to evaluate w(x).
        
        Returns
        --------
        output : double
            the value w(x).
        """

    def getError(self) -> double:
        """
        Gets the maximum absolute error.
        Returns
        --------
        output : double
            the maximum absolute error.
        """

    def getLength(self) -> double:
        """
        Gets the two-sided window length.
        Returns
        --------
        output : double
            the window length.
        """

    def getWidth(self) -> double:
        """
        Gets the transition width.
        Returns
        --------
        output : double
            the transition width.
        """
