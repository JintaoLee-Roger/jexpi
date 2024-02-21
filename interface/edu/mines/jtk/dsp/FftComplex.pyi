from typing import overload
from edu.mines.jtk.mapping import *


class FftComplex:
    """
    Fast Fourier transform of complex-valued arrays. The FFT length
    nfft equals the number of <em>complex</em> numbers transformed.
    The transform of nfft complex numbers yields nfft complex numbers.
    Those complex numbers are packed into arrays of floats as [real_0,
    imag_0, real_1, imag_1, ...]. Here, real_k and imag_k correspond to
    the real and imaginary parts, respectively, of the complex number
    with array index k.
    
    When input and output arrays are the same array, transforms are
    performed in-place. For example, an input array cx[2nfft] of nfft
    complex numbers may be the same as an output array cy[2nfft] of
    nfft complex numbers. By "the same array", we mean that cx==cy.
    
    Transforms may be performed for any dimension of a multi-dimensional
    array. For example, we may transform the 1st dimension of an input
    array cx[n2][2nfft] of n2nfft complex numbers to an output array
    cy[n2][2nfft] of n2nfft complex numbers. Or, we may transform the
    2nd dimension of an input array cx[nfft][2n1] of nfftn1 complex
    numbers to an output array cy[nfft][2n1] of nfftn1 complex numbers.
    In either case, the input array cx and the output array cy may be the
    same array, such that the transform may be performed in-place.
    """

    def __init__(self, nfft: int) -> None:
        """
        Constructs a new FFT, with specified length. Valid FFT lengths
        can be obtained by calling the methods {@link #nfftSmall(int)}
        and {@link #nfftFast(int)}.
        
        Parameters
        -----------
        nfft : int
            the FFT length, which must be valid.
        """

    @staticmethod
    def nfftSmall(self, n: int) -> int:
        """
        Returns an FFT length optimized for memory. The FFT length will be the
        smallest valid length that is not less than the specified length n.
        the maximum length supported by this implementation. Currently, the
        maximum length is 720,720.
        
        Parameters
        -----------
        n : int
            the lower bound on FFT length.
        
        Returns
        --------
        output : int
            the FFT length.
        """

    @staticmethod
    def nfftFast(self, n: int) -> int:
        """
        Returns an FFT length optimized for speed. The FFT length will be the
        fastest valid length that is not less than the specified length n.
        the maximum length supported by this implementation. Currently, the
        maximum length is 720,720.
        
        Parameters
        -----------
        n : int
            the lower bound on FFT length.
        
        Returns
        --------
        output : int
            the FFT length.
        """

    def getNfft(self) -> int:
        """
        Gets the FFT length for this FFT.
        Returns
        --------
        output : int
            the FFT length.
        """

    def complexToComplex(self, sign: int, cx: Float1D, cy: Float1D) -> None:
        """
        Computes a complex-to-complex fast Fourier transform.
        Transforms a 1-D input array cx[2nfft] of nfft complex numbers
        to a 1-D output array cy[2nfft] of nfft complex numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        cx : Float1D
            the input array.
        cy : Float1D
            the output array.
        """

    @overload
    def complexToComplex1(self, sign: int, n2: int, cx: Float2D,
                          cy: Float2D) -> None:
        """
        Computes a complex-to-complex dimension-1 fast Fourier transform.
        Transforms a 2-D input array cx[n2][2nfft] of n2nfft complex numbers
        to a 2-D output array cy[n2][2nfft] of n2nfft complex numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        n2 : int
            the 2nd dimension of arrays.
        cx : Float2D
            the input array.
        cy : Float2D
            the output array.
        """

    @overload
    def complexToComplex2(self, sign: int, n1: int, cx: Float2D,
                          cy: Float2D) -> None:
        """
        Computes a complex-to-complex dimension-2 fast Fourier transform.
        Transforms a 2-D input array cx[nfft][2n1] of nfftn1 complex numbers
        to a 2-D output array cy[nfft][2n1] of nfftn1 complex numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        n1 : int
            the 1st dimension of arrays.
        cx : Float2D
            the input array.
        cy : Float2D
            the output array.
        """

    @overload
    def complexToComplex1(self, sign: int, n2: int, n3: int, cx: Float3D,
                          cy: Float3D) -> None:
        """
        Computes a complex-to-complex dimension-1 fast Fourier transform.
        Transforms a 3-D input array cx[n3][n2][2nfft] of n3n2nfft complex
        numbers to a 3-D output array cy[n3][n2][2nfft] of n3n2nfft complex
        numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        n2 : int
            the 2nd dimension of arrays.
        n3 : int
            the 3rd dimension of arrays.
        cx : Float3D
            the input array.
        cy : Float3D
            the output array.
        """

    @overload
    def complexToComplex2(self, sign: int, n1: int, n3: int, cx: Float3D,
                          cy: Float3D) -> None:
        """
        Computes a complex-to-complex dimension-2 fast Fourier transform.
        Transforms a 3-D input array cx[n3][nfft][2n1] of n3nfftn1 complex
        numbers to a 3-D output array cy[n3][nfft][2n1] of n3nfftn1 complex
        numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        n1 : int
            the 1st dimension of arrays.
        n3 : int
            the 3rd dimension of arrays.
        cx : Float3D
            the input array.
        cy : Float3D
            the output array.
        """

    def complexToComplex3(self, sign: int, n1: int, n2: int, cx: Float3D,
                          cy: Float3D) -> None:
        """
        Computes a complex-to-complex dimension-3 fast Fourier transform.
        Transforms a 3-D input array cx[nfft][n2][2n1] of nfftn2n1 complex
        numbers to a 3-D output array cy[nfft][n2][2n1] of nfftn2n1 complex
        numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        n1 : int
            the 1st dimension of arrays.
        n2 : int
            the 2nd dimension of arrays.
        cx : Float3D
            the input array.
        cy : Float3D
            the output array.
        """

    @overload
    def scale(self, n1: int, cx: Float1D) -> None:
        """
        Scales n1 complex numbers in the specified array by 1/nfft.
        The inverse of a complex-to-complex FFT is a complex-to-complex
        FFT (with opposite sign) followed by this scaling.
        
        Parameters
        -----------
        n1 : int
            1st (only) dimension of the array cx.
        cx : Float1D
            the input/output array[2n1].
        """

    @overload
    def scale(self, n1: int, n2: int, cx: Float2D) -> None:
        """
        Scales n1n2 complex numbers in the specified array by 1/nfft.
        The inverse of a complex-to-complex FFT is a complex-to-complex
        FFT (with opposite sign) followed by this scaling.
        
        Parameters
        -----------
        n1 : int
            the 1st dimension of the array cx.
        n2 : int
            the 2nd dimension of the array cx.
        cx : Float2D
            the input/output array[n2][2n1].
        """

    @overload
    def scale(self, n1: int, n2: int, n3: int, cx: Float3D) -> None:
        """
        Scales n1n2n3 complex numbers in the specified array by 1/nfft.
        The inverse of a complex-to-complex FFT is a complex-to-complex
        FFT (with opposite sign) followed by this scaling.
        
        Parameters
        -----------
        n1 : int
            the 1st dimension of the array cx.
        n2 : int
            the 2nd dimension of the array cx.
        n3 : int
            the 3rd dimension of the array cx.
        cx : Float3D
            the input/output array[n3][n2][2n1].
        """
