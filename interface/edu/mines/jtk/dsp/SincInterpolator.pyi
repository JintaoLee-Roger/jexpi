from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.dsp import Sampling


class SincInterpolator:
    """
    A sinc interpolator for bandlimited uniformly-sampled functions y(x).
    Interpolators can be designed for any two of three parameters: maximum
    error (emax), maximum frequency (fmax) and maximum length (lmax). The
    parameter not specified is computed when an interpolator is designed.
    
    Below the specified (or computed) maximum frequency fmax, the maximum
    interpolation error should be less than the specified (or computed)
    maximum error emax. For frequencies above fmax, interpolation error
    may be much greater. Therefore, sequences to be interpolated should
    be bandlimited to frequencies less than fmax.
    
    The maximum length lmax of an interpolator is an even positive integer.
    It is the number of uniform samples required to interpolate a single
    value y(x). Ideally, the weights applied to each uniform sample are
    values of a sinc function. Although the ideal sinc function yields zero
    interpolation error for all frequencies up to the Nyquist frequency
    (0.5 cycles/sample), it has infinite length.
    
    With recursive filtering, infinite-length approximations to the sinc
    function are feasible and, in some applications, most efficient. When
    the number of interpolated values is large relative to the number of
    uniform samples, the cost of recursive filtering is amortized over those
    many interpolated values, and can be negligible. However, this cost
    becomes significant when only a few values are interpolated for each
    sequence of uniform samples.
    
    This interpolator is based on a <em>finite-length</em> approximation
    to the sinc function. The efficiency of finite-length interpolators
    like this one does not depend on the number of samples interpolated.
    Also, this interpolator is robust in the presence of noise spikes,
    which affect only nearby samples.
    
    Finite-length interpolators present a tradeoff between cost and accuracy.
    Interpolators with small maximum lengths are most efficient, and those
    with high maximum frequencies and small maximum errors are most accurate.
    
    When interpolating multiple values of y(x) from a single sequence of
    uniformly sampled values, efficiency may be improved by using one of the
    methods that enables specification of multiple x values at which to
    interpolate.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a default sinc interpolator. The default design parameters
        are fmax = 0.3 cycles/sample (60% of Nyquist) and lmax = 8 samples.
        For these parameters, the computed maximum error is less than 0.007
        (0.7%). In testing, observed maximum error is less than 0.005 (0.5%).
        """

    @overload
    def __init__(self, emax: double, fmax: double, lmax: int) -> None:
        """
        Constructs a sinc interpolator with specified parameters.
        Exactly one of the parameters must be zero, and is computed here.
        """

    @staticmethod
    def fromErrorAndLength(self, emax: double, lmax: int) -> SincInterpolator:
        """
        Returns a sinc interpolator with specified maximum error and length.
        Computes the maximum frequency fmax. Note that for some parameters
        emax and lmax, the maximum frequency fmax may be zero. In this case,
        the returned interpolator is useless.
        0.01 for 1% percent error. 0.0 &lt; emax &lt;= 0.1 is required.
        Must be an even integer not less than 8.
        
        Parameters
        -----------
        emax : double
            the maximum error for frequencies less than fmax; e.g.,
        lmax : int
            the maximum interpolator length, in samples.
        
        Returns
        --------
        output : SincInterpolator
            the sinc interpolator.
        """

    @staticmethod
    def fromErrorAndFrequency(self, emax: double,
                              fmax: double) -> SincInterpolator:
        """
        Returns a sinc interpolator with specified maximum error and frequency.
        Computes the maximum length lmax.
        0.01 for 1% percent error. Must be greater than 0.0 and less than 1.0.
        Must be greater than 0.0 and less than 0.5.
        
        Parameters
        -----------
        emax : double
            the maximum error for frequencies less than fmax; e.g.,
        fmax : double
            the maximum frequency, in cycles per sample.
        
        Returns
        --------
        output : SincInterpolator
            the sinc interpolator.
        """

    @staticmethod
    def fromFrequencyAndLength(self, fmax: double,
                               lmax: int) -> SincInterpolator:
        """
        Returns a sinc interpolator with specified maximum frequency and length.
        Computes the maximum error emax.
        
        The product (1-2fmax)lmax must be greater than one. For when this
        product is less than one, a useful upper bound on interpolation error
        cannot be computed.
        Must be greater than 0.0 and less than 0.5(1.0-1.0/lmax).
        Must be an even integer not less than 8 and greater than
        1.0/(1.0-2.0fmax).
        
        Parameters
        -----------
        fmax : double
            the maximum frequency, in cycles per sample.
        lmax : int
            the maximum interpolator length, in samples.
        
        Returns
        --------
        output : SincInterpolator
            the sinc interpolator.
        """

    def getMaximumError(self) -> double:
        """
        Gets the maximum error for this interpolator.
        Returns
        --------
        output : double
            the maximum error.
        """

    def getMaximumFrequency(self) -> double:
        """
        Gets the maximum frequency for this interpolator.
        Returns
        --------
        output : double
            the maximum frequency.
        """

    def getMaximumLength(self) -> int:
        """
        Gets the maximum length for this interpolator.
        Returns
        --------
        output : int
            the maximum length.
        """

    def getTableBytes(self) -> long:
        """
        Gets the number of bytes consumed by the table of interpolators.
        The use of interpolators with small emax and large lmax may require
        the computation of large tables. This method can be used to determine
        how much memory is consumed by the table for an interpolator.
        Returns
        --------
        output : long
            the number of bytes.
        """

    def getExtrapolation(self) -> Extrapolation:
        """
        Gets the extrapolation method for this interpolator.
        Returns
        --------
        output : Extrapolation
            the extrapolation method.
        """

    def setExtrapolation(self, extrap: Extrapolation) -> None:
        """
        Sets the extrapolation method for this interpolator.
        The default extrapolation method is extrapolation with zeros.
        
        Parameters
        -----------
        extrap : Extrapolation
            the extrapolation method.
        """

    @overload
    def interpolate(self, nxu: int, dxu: double, fxu: double, yu: Float1D,
                    xi: double) -> float:
        """
        Interpolates one real value y(x).
        
        Parameters
        -----------
        nxu : int
            number of input samples.
        dxu : double
            input sampling interval.
        fxu : double
            first input sampled x value.
        yu : Float1D
            input array of sampled values y(x).
        xi : double
            value x at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated value y(x).
        """

    @overload
    def interpolate(self, nxu: int, dxu: double, fxu: double, yu: Float1D,
                    nxi: int, xi: Float1D, yi: Float1D) -> None:
        """
        Interpolates multiple real values y(x).
        
        Parameters
        -----------
        nxu : int
            number of input samples.
        dxu : double
            input sampling interval.
        fxu : double
            first input sampled x value.
        yu : Float1D
            input array of sampled values y(x).
        nxi : int
            number of output samples.
        xi : Float1D
            input array of x values at which to interpolate.
        yi : Float1D
            output array of interpolated values y(x).
        """

    @overload
    def interpolate(self, nxu: int, dxu: double, fxu: double, yu: Float1D,
                    nxi: int, dxi: double, fxi: double, yi: Float1D) -> None:
        """
        Interpolates multiple real values y(x).
        
        Parameters
        -----------
        nxu : int
            number of input samples.
        dxu : double
            input sampling interval.
        fxu : double
            first input sampled x value.
        yu : Float1D
            input array of sampled values y(x).
        nxi : int
            number of output samples.
        dxi : double
            output sampling interval.
        fxi : double
            first output sampled x value.
        yi : Float1D
            output array of interpolated values y(x).
        """

    @overload
    def interpolate(self, nx1u: int, dx1u: double, fx1u: double, nx2u: int,
                    dx2u: double, fx2u: double, yu: Float2D, x1i: double,
                    x2i: double) -> float:
        """
        Interpolates one real value y(x1,x2).
        
        Parameters
        -----------
        nx1u : int
            number of input samples in 1st dimension.
        dx1u : double
            input sampling interval in 1st dimension.
        fx1u : double
            first input sampled x value in 1st dimension.
        nx2u : int
            number of input samples in 2nd dimension.
        dx2u : double
            input sampling interval in 2nd dimension.
        fx2u : double
            first input sampled x value in 2nd dimension.
        yu : Float2D
            input array of sampled values y(x).
        x1i : double
            1st coordinate of x at which to interpolate.
        x2i : double
            2nd coordinate of x at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated value y(x).
        """

    @overload
    def interpolate(self, nx1u: int, dx1u: double, fx1u: double, nx2u: int,
                    dx2u: double, fx2u: double, nx3u: int, dx3u: double,
                    fx3u: double, yu: Float3D, x1i: double, x2i: double,
                    x3i: double) -> float:
        """
        Interpolates one real value y(x1,x2,x3).
        
        Parameters
        -----------
        nx1u : int
            number of input samples in 1st dimension.
        dx1u : double
            input sampling interval in 1st dimension.
        fx1u : double
            first input sampled x value in 1st dimension.
        nx2u : int
            number of input samples in 2nd dimension.
        dx2u : double
            input sampling interval in 2nd dimension.
        fx2u : double
            first input sampled x value in 2nd dimension.
        nx3u : int
            number of input samples in 3rd dimension.
        dx3u : double
            input sampling interval in 3rd dimension.
        fx3u : double
            first input sampled x value in 3rd dimension.
        yu : Float3D
            input array of sampled values y(x).
        x1i : double
            1st coordinate of x at which to interpolate.
        x2i : double
            2nd coordinate of x at which to interpolate.
        x3i : double
            3rd coordinate of x at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated value y(x).
        """

    @overload
    def interpolate(self, sxu: Sampling, yu: Float1D, xi: double) -> float:
        """
        Interpolates one real value y(x).
        
        Parameters
        -----------
        sxu : Sampling
            sampling of input samples.
        yu : Float1D
            input array of uniformly sampled values y(x).
        xi : double
            value x at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated value y(x).
        """

    @overload
    def interpolate(self, sxu: Sampling, yu: Float1D, sxi: Sampling,
                    yi: Float1D) -> None:
        """
        Interpolates multiple real values y(x).
        
        Parameters
        -----------
        sxu : Sampling
            sampling of input samples.
        yu : Float1D
            input array of uniformly sampled values y(x).
        sxi : Sampling
            sampling of output samples.
        yi : Float1D
            output array of interpolated values y(x).
        """

    @overload
    def interpolate(self, sx1u: Sampling, sx2u: Sampling, yu: Float2D,
                    x1i: double, x2i: double) -> float:
        """
        Interpolates one real value y(x1,x2).
        
        Parameters
        -----------
        sx1u : Sampling
            sampling of input x in 1st dimension.
        sx2u : Sampling
            sampling of input x in 2nd dimension.
        yu : Float2D
            input array of sampled values y(x).
        x1i : double
            1st coordinate of x at which to interpolate.
        x2i : double
            2nd coordinate of x at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated value y(x).
        """

    @overload
    def interpolate(self, sx1u: Sampling, sx2u: Sampling, sx3u: Sampling,
                    yu: Float3D, x1i: double, x2i: double,
                    x3i: double) -> float:
        """
        Interpolates one real value y(x1,x2,x3).
        
        Parameters
        -----------
        sx1u : Sampling
            sampling of input x in 1st dimension.
        sx2u : Sampling
            sampling of input x in 2nd dimension.
        sx3u : Sampling
            sampling of input x in 3rd dimension.
        yu : Float3D
            input array of sampled values y(x).
        x1i : double
            1st coordinate of x at which to interpolate.
        x2i : double
            2nd coordinate of x at which to interpolate.
        x3i : double
            3rd coordinate of x at which to interpolate.
        
        Returns
        --------
        output : float
            interpolated value y(x).
        """

    @overload
    def interpolateComplex(self, nxu: int, dxu: double, fxu: double,
                           yu: Float1D, nxi: int, dxi: double, fxi: double,
                           yi: Float1D) -> None:
        """
        Interpolates multiple complex values y(x).
        Complex output samples are packed in the specified output array as
        real, imag, real, imag, ....
        
        Parameters
        -----------
        nxu : int
            number of input samples.
        dxu : double
            input sampling interval.
        fxu : double
            first input sampled x value.
        yu : Float1D
            input array[2nxu] of sampled complex values y(x).
        nxi : int
            number of output samples.
        dxi : double
            output sampling interval.
        fxi : double
            first output sampled x value.
        yi : Float1D
            output array[2nxi] of interpolated complex values y(x).
        """

    @overload
    def interpolateComplex(self, nxu: int, dxu: double, fxu: double,
                           yu: Float1D, nxi: int, xi: Float1D,
                           yi: Float1D) -> None:
        """
        Interpolates multiple complex values y(x).
        Complex output samples are packed in the specified output array as
        real, imag, real, imag, ....
        
        Parameters
        -----------
        nxu : int
            number of input samples.
        dxu : double
            input sampling interval.
        fxu : double
            first input sampled x value.
        yu : Float1D
            input array[2nxu] of sampled complex values y(x).
        nxi : int
            number of output samples.
        xi : Float1D
            input array[nxi] of x values at which to interpolate.
        yi : Float1D
            output array[2nxi] of interpolated complex values y(x).
        """

    @overload
    def interpolateComplex(self, sxu: Sampling, yu: Float1D, sxi: Sampling,
                           yi: Float1D) -> None:
        """
        Interpolates multiple complex values y(x).
        Complex output samples are packed in the specified output array as
        real, imag, real, imag, ....
        
        Parameters
        -----------
        sxu : Sampling
            sampling of input samples.
        yu : Float1D
            input array[2nxu] of sampled complex values y(x).
        sxi : Sampling
            sampling of output samples.
        yi : Float1D
            output array[2nxi] of interpolated complex values y(x).
        """

    @overload
    def accumulate(self, xa: double, ya: float, nxu: int, dxu: double,
                   fxu: double, yu: Float1D) -> None:
        """
        Accumulates a specified real value y(x) into uniformly-sampled yu.
        Accumulation is the transpose (not the inverse) of interpolation.
        Whereas interpolation gathers from uniformly sampled values.
        accumulation scatters into uniformly sampled values.
        
        Parameters
        -----------
        xa : double
            value x at which to accumulate.
        ya : float
            value y(x) to accumulate.
        nxu : int
            number of input/output samples.
        dxu : double
            input/output sampling interval.
        fxu : double
            first input/output sampled x value.
        yu : Float1D
            input/output array of sampled values y(x).
        """

    @overload
    def accumulate(self, nxa: int, xa: Float1D, ya: Float1D, nxu: int,
                   dxu: double, fxu: double, yu: Float1D) -> None:
        """
        Accumulates a specified real value y(x) into uniformly-sampled yu.
        Accumulation is the transpose (not the inverse) of interpolation.
        Whereas interpolation gathers from uniformly sampled values.
        accumulation scatters into uniformly sampled values.
        
        Parameters
        -----------
        nxa : int
            number of values to accumulate.
        xa : Float1D
            input array of values x at which to accumulate.
        ya : Float1D
            input array of values y(x) to accumulate.
        nxu : int
            number of input/output samples.
        dxu : double
            input/output sampling interval.
        fxu : double
            first input/output sampled x value.
        yu : Float1D
            input/output array of sampled values y(x).
        """

    def getTable(self) -> Float2D:
        """
        Get a copy of the interpolation table.  Returns a copy of this
        interpolator's table of sinc interpolation coefficients.
        Returns
        --------
        output : Float2D
            A copy of the table.
        """

    def getNumberInTable(self) -> int:
        """
        Gets the number of sampled sinc approximations in the table.
        Returns
        --------
        output : int
            the number of tabulated sampled sinc approximations.
        """

    def getLengthInTable(self) -> int:
        """
        Gets the length of sampled sinc approximations in the table.
        Returns
        --------
        output : int
            the length of tabulated sampled sinc approximations.
        """
