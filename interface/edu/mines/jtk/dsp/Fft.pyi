from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.dsp import *


class Fft:
    """
    An easy to use fast Fourier transform.
    This class is less flexible than {@link FftComplex} and {@link FftReal}.
    For example, the user has less control over the sampling of frequency.
    However, for many applications this class may be simpler to use.
    
    For example, the following program shows how to use this class to
    filter a real-valued sequence in the frequency domain.
    <pre><code>
    Fft fft = new Fft(nx); // nx = number of samples of f(x)
    Sampling sk = fft.getFrequencySampling1();
    int nk = sk.getCount(); // number of frequencies sampled
    float[] f = ... // nx real samples of input f(x)
    float[] g = fft.applyForward(f); // nk complex samples of g(k)
    for (int kk=0,kr=0,ki=kr+1; kk&lt;nk; ++kk,kr+=2,ki+=2) {
    double k = sk.getValue(kk); // frequency k in cycles/sample
    // modify g[kr], the real part of g(k)
    // modify g[ki], the imag part of g(k)
    }
    float[] h = fft.applyInverse(g); // nx real samples of output h(x)
    </code></pre>
    This example is almost as simple for multi-dimensional transforms.
    
    A forward transform computes an output array of complex values g(k)
    from an input array of real or complex values f(x). An inverse
    transform computes the corresponding real or complex values f(x)
    from g(k). For definiteness, in this documentation, the variable x
    represents spatial coordinates and the variable k represents spatial
    frequencies (or wavenumbers). For functions of time, simply replace
    the word "space" with "time" in this documentation.
    
    This class enables transforms of 1D, 2D, and 3D arrays. For example,
    a 2D array f[nx2][nx1] represents nx2nx1 samples of a function
    f(x1,x2) of two spatial coordinates x1 and x2. In addition to
    numbers of samples nx1 and nx2, sampling intervals dx1 and dx2
    and first sampled coordinates fx1 and fx2 may also be specified.
    (The default sampling interval is 1.0 and the default first sample
    coordinate is 0.0.) These sampling parameters may be specified with
    samplings sx1 and sx2.
    
    For each specified spatial sampling sx, this class defines a
    corresponding frequency sampling sk, in which units of frequency
    are cycles per unit distance. The number of frequencies sampled
    is computed so that the Fourier transform is fast, but the number
    of frequency samples is never less than the number of space samples.
    Arrays to be transformed may be padded with zeros to obtain the
    required frequency sampling. Optional additional padding may be
    specified to sample frequency more finely.
    
    A frequency sampling sk may be centered. Such a centered frequency
    sampling always has an odd number of samples, and zero frequency
    corresponds to the middle sample in the array of complex transformed
    values. The default is not centered, so that zero frequency corresponds
    to the first sample, the one with index 0.
    
    Arrays input to forward transforms may contain either real or
    complex values. If complex, values are packed sequentially as
    (real,imaginary) pairs of consecutive floats. The default input
    type is real.
    
    Signs of the exponents in the complex exponentials used in forward
    transforms may be specified. The opposite signs are used for inverse
    transforms. The default signs are -1 for forward transforms and 1 for
    inverse transforms.
    """

    @overload
    def __init__(self, f: Float1D) -> None:
        """
        Constructs an FFT for the specified 1D array of real values.
        Spatial dimensions are determined from the dimensions of the
        specified array. Spatial sampling intervals are 1.0, and first
        sample coordinates are 0.0.
        
        Parameters
        -----------
        f : Float1D
            an array with dimensions like those to be transformed.
        """

    @overload
    def __init__(self, f: Float2D) -> None:
        """
        Constructs an FFT for the specified 2D array of real values.
        Spatial dimensions are determined from the dimensions of the
        specified array. Spatial sampling intervals are 1.0, and first
        sample coordinates are 0.0.
        
        Parameters
        -----------
        f : Float2D
            an array with dimensions like those to be transformed.
        """

    @overload
    def __init__(self, f: Float3D) -> None:
        """
        Constructs an FFT for the specified 3D array of real values.
        Spatial dimensions are determined from the dimensions of the
        specified array. Spatial sampling intervals are 1.0, and first
        sample coordinates are 0.0.
        
        Parameters
        -----------
        f : Float3D
            an array with dimensions like those to be transformed.
        """

    @overload
    def __init__(self, complex: bool, f: Float1D) -> None:
        """
        Constructs an FFT for the specified 1D array of values.
        Spatial dimensions are determined from the dimensions of the
        specified array. Spatial sampling intervals are 1.0, and first
        sample coordinates are 0.0.
        
        Parameters
        -----------
        complex : bool
            true, for complex values; false, for real values.
        f : Float1D
            an array with dimensions like those to be transformed.
        """

    @overload
    def __init__(self, complex: bool, f: Float2D) -> None:
        """
        Constructs an FFT for the specified 2D array of values.
        Spatial dimensions are determined from the dimensions of the
        specified array. Spatial sampling intervals are 1.0, and first
        sample coordinates are 0.0.
        
        Parameters
        -----------
        complex : bool
            true, for complex values; false, for real values.
        f : Float2D
            an array with dimensions like those to be transformed.
        """

    @overload
    def __init__(self, complex: bool, f: Float3D) -> None:
        """
        Constructs an FFT for the specified 3D array of values.
        Spatial dimensions are determined from the dimensions of the
        specified array. Spatial sampling intervals are 1.0, and first
        sample coordinates are 0.0.
        
        Parameters
        -----------
        complex : bool
            true, for complex values; false, for real values.
        f : Float3D
            an array with dimensions like those to be transformed.
        """

    @overload
    def __init__(self, nx1: int) -> None:
        """
        Constructs an FFT with specified number of space samples.
        The sampling interval is 1.0 and the first sample coordinate is 0.0.
        
        Parameters
        -----------
        nx1 : int
            number of samples in the 1st dimension.
        """

    @overload
    def __init__(self, nx1: int, nx2: int) -> None:
        """
        Constructs an FFT with specified numbers of space samples.
        Sampling intervals are 1.0 and first sample coordinates are 0.0.
        
        Parameters
        -----------
        nx1 : int
            number of samples in the 1st dimension.
        nx2 : int
            number of samples in the 2nd dimension.
        """

    @overload
    def __init__(self, nx1: int, nx2: int, nx3: int) -> None:
        """
        Constructs an FFT with specified numbers of space samples.
        Sampling intervals are 1.0 and first sample coordinates are 0.0.
        
        Parameters
        -----------
        nx1 : int
            number of samples in the 1st dimension.
        nx2 : int
            number of samples in the 2nd dimension.
        nx3 : int
            number of samples in the 3rd dimension.
        """

    @overload
    def __init__(self, sx1: Sampling) -> None:
        """
        Constructs an FFT with specified space sampling.
        
        Parameters
        -----------
        sx1 : Sampling
            space sampling for the 1st dimension.
        """

    @overload
    def __init__(self, sx1: Sampling, sx2: Sampling) -> None:
        """
        Constructs an FFT with specified space sampling.
        
        Parameters
        -----------
        sx1 : Sampling
            space sampling for the 1st dimension.
        sx2 : Sampling
            space sampling for the 2nd dimension.
        """

    @overload
    def __init__(self, sx1: Sampling, sx2: Sampling, sx3: Sampling) -> None:
        """
        Constructs an FFT with specified space sampling.
        
        Parameters
        -----------
        sx1 : Sampling
            space sampling for the 1st dimension.
        sx2 : Sampling
            space sampling for the 2nd dimension.
        sx3 : Sampling
            space sampling for the 3rd dimension.
        """

    def setComplex(self, complex: bool) -> None:
        """
        Sets the type of input (output) values for forward (inverse) transforms.
        The default type is real.
        
        Parameters
        -----------
        complex : bool
            true, for complex values; false, for real values.
        """

    def setOverwrite(self, overwrite: bool) -> None:
        """
        Sets the ability of this transform to overwrite specified arrays.
        The array specified in an inverse transform is either copied or
        overwritten internally by the inverse transform. Copying preserves
        the values in the specified array, but wastes memory in the case
        when those values are no longer needed. If overwrite is true, then
        the inverse transform will be performed in place, so that no copy
        is necessary. The default is false.
        
        Parameters
        -----------
        overwrite : bool
            true, to overwrite; false, to copy.
        """

    def getFrequencySampling1(self) -> Sampling:
        """
        Gets the frequency sampling for the 1st dimension.
        Returns
        --------
        output : Sampling
            the frequency sampling.
        """

    def getFrequencySampling2(self) -> Sampling:
        """
        Gets the frequency sampling for the 2nd dimension.
        Returns
        --------
        output : Sampling
            the frequency sampling.
        """

    def getFrequencySampling3(self) -> Sampling:
        """
        Gets the frequency sampling for the 3rd dimension.
        Returns
        --------
        output : Sampling
            the frequency sampling.
        """

    def setSign(self, sign: int) -> None:
        """
        Sets the sign used for forward transforms in all dimensions.
        The opposite sign is used for inverse transforms.
        The default sign is -1.
        
        Parameters
        -----------
        sign : int
            the sign, -1 or 1.
        """

    def setSign1(self, sign: int) -> None:
        """
        Sets the sign used for forward transforms in the 1st dimension.
        The opposite sign is used for inverse transforms.
        The default sign is -1.
        
        Parameters
        -----------
        sign : int
            the sign, -1 or 1.
        """

    def setSign2(self, sign: int) -> None:
        """
        Sets the sign used for forward transforms in the 2nd dimension.
        The opposite sign is used for inverse transforms.
        The default sign is -1.
        
        Parameters
        -----------
        sign : int
            the sign, -1 or 1.
        """

    def setSign3(self, sign: int) -> None:
        """
        Sets the sign used for forward transforms in the 3rd dimension.
        The opposite sign is used for inverse transforms.
        The default sign is -1.
        
        Parameters
        -----------
        sign : int
            the sign, -1 or 1.
        """

    def setCenter(self, center: bool) -> None:
        """
        Sets the centering of frequency samplings for all dimensions.
        If centered, the number of frequency samples is always odd,
        and zero frequency corresponds to the middle sample. The
        default center is false, so that zero frequency corresponds to
        the sample with index zero in the output transformed array.
        
        Parameters
        -----------
        center : bool
            true, for centering; false, otherwise.
        """

    def setCenter1(self, center: bool) -> None:
        """
        Sets the centering of frequency sampling for the 1st dimension.
        If centered, the number of frequency samples is always odd,
        and zero frequency corresponds to the middle sample. The
        default center is false, so that zero frequency corresponds to
        the sample with index zero in the output transformed array.
        
        Parameters
        -----------
        center : bool
            true, for centering; false, otherwise.
        """

    def setCenter2(self, center: bool) -> None:
        """
        Sets the centering of frequency sampling for the 2nd dimension.
        If centered, the number of frequency samples is always odd,
        and zero frequency corresponds to the middle sample. The
        default center is false, so that zero frequency corresponds to
        the sample with index zero in the output transformed array.
        
        Parameters
        -----------
        center : bool
            true, for centering; false, otherwise.
        """

    def setCenter3(self, center: bool) -> None:
        """
        Sets the centering of frequency sampling for the 3rd dimension.
        If centered, the number of frequency samples is always odd,
        and zero frequency corresponds to the middle sample. The
        default center is false, so that zero frequency corresponds to
        the sample with index zero in the output transformed array.
        
        Parameters
        -----------
        center : bool
            true, for centering; false, otherwise.
        """

    def setPadding(self, padding: int) -> None:
        """
        Sets the minimum padding with zeros for all array dimensions.
        The default minimum is zero. However, some amount of padding
        may be required by the FFT.
        
        Parameters
        -----------
        padding : int
            the minimum padding.
        """

    def setPadding1(self, padding: int) -> None:
        """
        Sets the minimum padding with zeros for the 1st array dimension.
        The default minimum is zero. However, some amount of padding may
        be required by the FFT.
        
        Parameters
        -----------
        padding : int
            the minimum padding.
        """

    def setPadding2(self, padding: int) -> None:
        """
        Sets the minimum padding with zeros for the 2nd array dimension.
        The default minimum is zero. However, some amount of padding may
        be required by the FFT.
        
        Parameters
        -----------
        padding : int
            the minimum padding.
        """

    def setPadding3(self, padding: int) -> None:
        """
        Sets the minimum padding with zeros for the 3rd array dimension.
        The default minimum is zero. However, some amount of padding may
        be required by the FFT.
        
        Parameters
        -----------
        padding : int
            the minimum padding.
        """

    @overload
    def applyForward(self, f: Float1D) -> Float1D:
        """
        Applies a forward space-to-frequency transform of a 1D array.
        
        Parameters
        -----------
        f : Float1D
            the array to be transformed, a sampled function of space.
        
        Returns
        --------
        output : Float1D
            the transformed array, a sampled function of frequency.
        """

    @overload
    def applyForward(self, f: Float2D) -> Float2D:
        """
        Applies a forward space-to-frequency transform of a 2D array.
        
        Parameters
        -----------
        f : Float2D
            the array to be transformed, a sampled function of space.
        
        Returns
        --------
        output : Float2D
            the transformed array, a sampled function of frequency.
        """

    @overload
    def applyForward(self, f: Float3D) -> Float3D:
        """
        Applies a forward space-to-frequency transform of a 3D array.
        
        Parameters
        -----------
        f : Float3D
            the array to be transformed, a sampled function of space.
        
        Returns
        --------
        output : Float3D
            the transformed array, a sampled function of frequency.
        """

    @overload
    def applyInverse(self, g: Float1D) -> Float1D:
        """
        Applies an inverse frequency-to-space transform of a 1D array.
        
        Parameters
        -----------
        g : Float1D
            the array to be transformed, a sampled function of frequency.
        
        Returns
        --------
        output : Float1D
            the transformed array, a sampled function of space.
        """

    @overload
    def applyInverse(self, g: Float2D) -> Float2D:
        """
        Applies an inverse frequency-to-space transform of a 2D array.
        
        Parameters
        -----------
        g : Float2D
            the array to be transformed, a sampled function of frequency.
        
        Returns
        --------
        output : Float2D
            the transformed array, a sampled function of space.
        """

    @overload
    def applyInverse(self, g: Float3D) -> Float3D:
        """
        Applies an inverse frequency-to-space transform of a 3D array.
        
        Parameters
        -----------
        g : Float3D
            the array to be transformed, a sampled function of frequency.
        
        Returns
        --------
        output : Float3D
            the transformed array, a sampled function of space.
        """
