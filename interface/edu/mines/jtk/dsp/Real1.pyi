from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.dsp import Sampling


class Real1:
    """
    A real-valued sampled function of one variable.
    A {@link Real1} combines a {@link Sampling} with a reference to an
    an array of function values. In this way, a {@link Real1} <em>wraps</em>
    an array of function values. Because array values are referenced (not
    copied), the cost of wrapping any array with a {@link Real1} is small.
    
    One consequence of referencing the array of function values is that
    changes to elements in such an array are reflected in <em>all</em>
    {@link Real1}s that reference that array. If this behavior is not
    desired, the copy constructor {@link Real1#Real1(Real1)} creates a
    new array copy of function values.
    """

    @overload
    def __init__(self, s: Sampling) -> None:
        """
        Constructs a function with specified sampling and values zero.
        
        Parameters
        -----------
        s : Sampling
            the sampling.
        """

    @overload
    def __init__(self, v: Float1D) -> None:
        """
        Constructs a function with specified values and default sampling.
        The default sampling has number (count) of samples = v.length, sampling
        interval (delta) = 1.0 and first sample value (first) = 0.0.
        
        Parameters
        -----------
        v : Float1D
            array of function values; referenced, not copied.
        """

    @overload
    def __init__(self, s: Sampling, v: Float1D) -> None:
        """
        Constructs a function with specified sampling and values.
        The array length v.length must equal the number of samples in s.
        
        Parameters
        -----------
        s : Sampling
            the sampling.
        v : Float1D
            array of function values; referenced, not copied.
        """

    @overload
    def __init__(self, n: int, d: double, f: double) -> None:
        """
        Constructs a function with specified sampling and values zero.
        
        Parameters
        -----------
        n : int
            the number (count) of samples.
        d : double
            the sampling interval (delta).
        f : double
            the value of the first sample.
        """

    @overload
    def __init__(self, n: int, d: double, f: double, v: Float1D) -> None:
        """
        Constructs a function with specified sampling and values.
        The array length v.length must equal n.
        
        Parameters
        -----------
        n : int
            the number (count) of time samples.
        d : double
            the sampling interval (delta).
        f : double
            the value of the first sample.
        v : Float1D
            array of function values; referenced, not copied.
        """

    @overload
    def __init__(self, r: Real1) -> None:
        """
        Constructs a copy of the specified sampled function. This constructor
        <em>copies</em> (does not reference) the array of function values from
        the specified sampled function.
        
        Parameters
        -----------
        r : Real1
            the function to copy.
        """

    def getSampling(self) -> Sampling:
        """
        Gets the sampling for this function.
        Returns
        --------
        output : Sampling
            the sampling.
        """

    def getValues(self) -> Float1D:
        """
        Gets the array of function values for this function.
        Returns
        --------
        output : Float1D
            the array of function values; by reference, not by copy.
        """

    def resample(self, s: Sampling) -> Real1:
        """
        Returns this function resampled to have the specified sampling.
        
        If the specified sampling is compatible with the sampling of this
        function, this method copies the function values in the overlap
        between the two samplings, and assigns zero values to the function
        values where the two samplings do not overlap.
        
        If the specified sampling is incompatible with the sampling of this
        function, then this method must interpolate or decimate this function
        Neither interpolation or decimation is supported, yet.
        incompatible with this sampling.
        
        Parameters
        -----------
        s : Sampling
            the sampling.
        
        Returns
        --------
        output : Real1
            the resampled function.
        """

    @overload
    def plus(self, ra: Real1) -> Real1:
        """
        Returns the sum this + ra of functions this and ra.
        The samplings of this and ra must be equivalent.
        
        Parameters
        -----------
        ra : Real1
            a function.
        
        Returns
        --------
        output : Real1
            the sum.
        """

    @overload
    def plus(self, ar: float) -> Real1:
        """
        Returns the sum this + ar of this function and constant ar.
        
        Parameters
        -----------
        ar : float
            a constant.
        
        Returns
        --------
        output : Real1
            the sum.
        """

    def convolve(self, ra: Real1) -> Real1:
        """
        Convolves this function with the specified function. The two functions
        must be uniformly sampled with equal sampling intervals.
        
        Parameters
        -----------
        ra : Real1
            the function with which to convolve.
        
        Returns
        --------
        output : Real1
            the convolution function.
        """

    def getFourierSampling(self, nmin: int) -> Sampling:
        """
        Gets sampling for the Fourier transform of this function. The first
        sample value will be zero, because the Fourier transform of a real
        function has conjugate-symmetry.
        
        A minimum number of Fourier transform samples must be specified, and
        the number of samlpes in the returned sampling will not be less than
        the larger of that specified minimum and the number of samples in this
        function.
        
        Parameters
        -----------
        nmin : int
            the minimum number of samples after Fourier transform.
        
        Returns
        --------
        output : Sampling
            the Fourier transform sampling.
        """

    @overload
    @staticmethod
    def zero(self, n: int) -> Real1:
        """
        Returns a sampled function with values zero.
        
        Parameters
        -----------
        n : int
            the number of samples.
        
        Returns
        --------
        output : Real1
            the function.
        """

    @overload
    @staticmethod
    def zero(self, s: Sampling) -> Real1:
        """
        Returns a sampled function with values zero.
        
        Parameters
        -----------
        s : Sampling
            the sampling.
        
        Returns
        --------
        output : Real1
            the function.
        """

    @overload
    @staticmethod
    def fill(self, ar: double, n: int) -> Real1:
        """
        Returns a function with constant values.
        
        Parameters
        -----------
        ar : double
            the constant.
        n : int
            the number of samples.
        
        Returns
        --------
        output : Real1
            the function.
        """

    @overload
    @staticmethod
    def fill(self, ar: double, s: Sampling) -> Real1:
        """
        Returns a function with constant values.
        
        Parameters
        -----------
        ar : double
            the constant.
        s : Sampling
            the sampling.
        
        Returns
        --------
        output : Real1
            the function.
        """

    @overload
    @staticmethod
    def ramp(self, fv: double, dv: double, nv: int) -> Real1:
        """
        Returns a sampled linear (ramp) function.
        The function values are fv+ivdv, for iv in [0:nv).
        
        Parameters
        -----------
        fv : double
            the first function value.
        dv : double
            the function value delta.
        nv : int
            the number of values.
        
        Returns
        --------
        output : Real1
            the function.
        """

    @overload
    @staticmethod
    def ramp(self, fv: double, dv: double, s: Sampling) -> Real1:
        """
        Returns a sampled linear (ramp) function.
        The function values are fv+dv(s-f), for s = f, f+d, ..., f+d(n-1),
        where n, d, and f are the sampling count, delta, and first value.
        
        Parameters
        -----------
        fv : double
            the first function value.
        dv : double
            the function value delta.
        s : Sampling
            the sampling.
        
        Returns
        --------
        output : Real1
            the function.
        """

    @overload
    @staticmethod
    def add(self, ra: Real1, rb: Real1) -> Real1:
        """
        Returns the sum ra + rb of two functions ra and rb.
        The samplings of ra and rb must be equivalent.
        
        Parameters
        -----------
        ra : Real1
            a function.
        rb : Real1
            a function.
        
        Returns
        --------
        output : Real1
            the sum.
        """

    @overload
    @staticmethod
    def add(self, ar: float, rb: Real1) -> Real1:
        """
        Returns the sum ar + rb of constant ar and function rb.
        
        Parameters
        -----------
        ar : float
            a constant.
        rb : Real1
            a function.
        
        Returns
        --------
        output : Real1
            the sum.
        """

    @overload
    @staticmethod
    def add(self, ra: Real1, br: float) -> Real1:
        """
        Returns the sum ra + br of function ra and constant br.
        
        Parameters
        -----------
        ra : Real1
            a function.
        br : float
            a constant.
        
        Returns
        --------
        output : Real1
            the sum.
        """

    @overload
    @staticmethod
    def sub(self, ra: Real1, rb: Real1) -> Real1:
        """
        Returns the difference ra - rb of two functions ra and rb.
        The samplings of ra and rb must be equivalent.
        
        Parameters
        -----------
        ra : Real1
            a function.
        rb : Real1
            a function.
        
        Returns
        --------
        output : Real1
            the difference.
        """

    @overload
    @staticmethod
    def sub(self, ar: float, rb: Real1) -> Real1:
        """
        Returns the difference ar - rb of constant ar and function rb.
        
        Parameters
        -----------
        ar : float
            a constant.
        rb : Real1
            a function.
        
        Returns
        --------
        output : Real1
            the sum.
        """

    @overload
    @staticmethod
    def sub(self, ra: Real1, br: float) -> Real1:
        """
        Returns the difference ra - br of function ra and constant br.
        
        Parameters
        -----------
        ra : Real1
            a function.
        br : float
            a constant.
        
        Returns
        --------
        output : Real1
            the sum.
        """

    @overload
    @staticmethod
    def mul(self, ra: Real1, rb: Real1) -> Real1:
        """
        Returns the product ra  rb of two functions ra and rb.
        The samplings of ra and rb must be equivalent.
        
        Parameters
        -----------
        ra : Real1
            a function.
        rb : Real1
            a function.
        
        Returns
        --------
        output : Real1
            the difference.
        """

    @overload
    @staticmethod
    def mul(self, ar: float, rb: Real1) -> Real1:
        """
        Returns the product ar  rb of constant ar and function rb.
        
        Parameters
        -----------
        ar : float
            a constant.
        rb : Real1
            a function.
        
        Returns
        --------
        output : Real1
            the sum.
        """

    @overload
    @staticmethod
    def mul(self, ra: Real1, br: float) -> Real1:
        """
        Returns the product ra  br of function ra and constant br.
        
        Parameters
        -----------
        ra : Real1
            a function.
        br : float
            a constant.
        
        Returns
        --------
        output : Real1
            the sum.
        """

    @overload
    @staticmethod
    def div(self, ra: Real1, rb: Real1) -> Real1:
        """
        Returns the quotient ra / rb of two functions ra and rb.
        The samplings of ra and rb must be equivalent.
        
        Parameters
        -----------
        ra : Real1
            a function.
        rb : Real1
            a function.
        
        Returns
        --------
        output : Real1
            the difference.
        """

    @overload
    @staticmethod
    def div(self, ar: float, rb: Real1) -> Real1:
        """
        Returns the quotient ar / rb of constant ar and function rb.
        
        Parameters
        -----------
        ar : float
            a constant.
        rb : Real1
            a function.
        
        Returns
        --------
        output : Real1
            the sum.
        """

    @overload
    @staticmethod
    def div(self, ra: Real1, br: float) -> Real1:
        """
        Returns the quotient ra / br of function ra and constant br.
        
        Parameters
        -----------
        ra : Real1
            a function.
        br : float
            a constant.
        
        Returns
        --------
        output : Real1
            the sum.
        """
