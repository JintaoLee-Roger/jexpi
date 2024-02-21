from typing import overload
from edu.mines.jtk.mapping import *


class FftReal:
    """
    Fast Fourier transform of real-valued arrays. The FFT length nfft
    equals the number of <em>real</em> numbers transformed. The transform
    of nfft real numbers yields nfft/2+1 complex numbers. (The imaginary
    parts of the first and last complex numbers are always zero.) For
    real-to-complex and complex-to-real transforms, nfft is always an even
    number.
    
    Complex numbers are packed into arrays of floats as [real_0, imag_0,
    real_1, imag_1, ...]. Here, real_k and imag_k correspond to the real
    and imaginary parts of the complex number with index k.
    
    When input and output arrays are the same array, transforms are performed
    in-place. For example, an input array rx[nfft] of nfft real numbers may be
    the same as an output array cy[nfft+2] of nfft/2+1 complex numbers. By
    "the same array", we mean that rx==cy. In this case, both rx.length and
    cy.length equal nfft+2. When we write rx[nfft] (here and below), we imply
    that only the first nfft floats in the input array rx are accessed.
    
    Transforms may be performed for any dimension of a multi-dimensional
    array. For example, we may transform the 1st dimension of an input array
    rx[n2][nfft] of n2nfft real numbers to an output array cy[n2][nfft+2] of
    n2(nfft/2+1) complex numbers. Or, we may transform the 2nd dimension of
    an input array rx[nfft][n1] of nfftn1 real numbers to an output array
    cy[nfft/2+1][2n1] of (nfft/2+1)n1 complex numbers. In either case, the
    input array rx and the output array cy may be the same array, such that
    the transform may be performed in-place.
    
    In-place transforms are typically used to reduce memory consumption.
    Note, however, that memory consumption is reduced for only dimension-1
    in-place transforms. Dimension-2 (and higher) in-place transforms save
    no memory, because of the contiguous packing of real and imaginary parts
    of complex numbers in multi-dimensional arrays of floats. (See above.)
    Therefore, dimension-1 transforms are best when performing real-to-complex
    or complex-to-real transforms of multi-dimensional arrays.
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
        maximum length is 1,441,440.
        
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
        maximum length is 1,441,440.
        
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
        Gets the FFT length nfft for this FFT.
        Returns
        --------
        output : int
            the FFT length.
        """

    def realToComplex(self, sign: int, rx: Float1D, cy: Float1D) -> None:
        """
        Computes a real-to-complex fast Fourier transform.
        Transforms a 1-D input array rx[nfft] of nfft real numbers to
        a 1-D output array cy[nfft+2] of nfft/2+1 complex numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        rx : Float1D
            the input array.
        cy : Float1D
            the output array.
        """

    def complexToReal(self, sign: int, cx: Float1D, ry: Float1D) -> None:
        """
        Computes a complex-to-real fast Fourier transform.
        Transforms a 1-D input array cx[nfft+2] of nfft/2+1 complex numbers
        to a 1-D output array ry[nfft] of nfft real numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        cx : Float1D
            the input array.
        ry : Float1D
            the output array.
        """

    @overload
    def realToComplex1(self, sign: int, n2: int, rx: Float2D,
                       cy: Float2D) -> None:
        """
        Computes a real-to-complex dimension-1 fast Fourier transform.
        Transforms a 2-D input array rx[n2][nfft] of n2nfft real numbers to
        a 2-D output array cy[n2][nfft+2] of n2(nfft/2+1) complex numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        n2 : int
            the 2nd dimension of arrays.
        rx : Float2D
            the input array.
        cy : Float2D
            the output array.
        """

    @overload
    def complexToReal1(self, sign: int, n2: int, cx: Float2D,
                       ry: Float2D) -> None:
        """
        Computes a complex-to-real dimension-1 fast Fourier transform.
        Transforms a 2-D input array cx[n2][nfft+2] of n2(nfft/2+1) complex
        numbers to a 2-D output array ry[n2][nfft] of n2nfft real numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        n2 : int
            the 2nd dimension of arrays.
        cx : Float2D
            the input array.
        ry : Float2D
            the output array.
        """

    def realToComplex2(self, sign: int, n1: int, rx: Float2D,
                       cy: Float2D) -> None:
        """
        Computes a real-to-complex dimension-2 fast Fourier transform.
        Transforms a 2-D input array rx[nfft][n1] of nfftn1 real numbers to a
        2-D output array cy[nfft/2+1][2n1] of (nfft/2+1)n1 complex numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        n1 : int
            the 1st dimension of arrays.
        rx : Float2D
            the input array.
        cy : Float2D
            the output array.
        """

    def complexToReal2(self, sign: int, n1: int, cx: Float2D,
                       ry: Float2D) -> None:
        """
        Computes a complex-to-real dimension-2 fast Fourier transform.
        Transforms a 2-D input array cx[nfft/2+1][2n1] of (nfft/2+1)n1 complex
        numbers to a 2-D output array ry[nfft][n1] of nfftn1 real numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        n1 : int
            the 1st dimension of arrays.
        cx : Float2D
            the input array.
        ry : Float2D
            the output array.
        """

    @overload
    def realToComplex1(self, sign: int, n2: int, n3: int, rx: Float3D,
                       cy: Float3D) -> None:
        """
        Computes a real-to-complex dimension-1 fast Fourier transform.
        Transforms a 3-D input array rx[n3][n2][nfft] of n3n2nfft real
        numbers to a 3-D output array cy[n3][n2][nfft+2] of n3n2(nfft/2+1)
        complex numbers.
        
        Parameters
        -----------
        sign : int
            the sign (1 or -1) of the exponent used in the FFT.
        n2 : int
            the 2nd dimension of arrays.
        n3 : int
            the 3rd dimension of arrays.
        rx : Float3D
            the input array.
        cy : Float3D
            the output array.
        """

    @overload
    def complexToReal1(self, sign: int, n2: int, n3: int, cx: Float3D,
                       ry: Float3D) -> None:
        """
        Computes a complex-to-real dimension-1 fast Fourier transform.
        Transforms a 3-D input array cx[n3][n2][nfft+2] of n3n2(nfft/2+1)
        complex numbers to a 3-D output array ry[n3][n2][nfft] of n3n2nfft
        real numbers.
        
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
        ry : Float3D
            the output array.
        """

    @overload
    def scale(self, n1: int, rx: Float1D) -> None:
        """
        Scales n1 real numbers in the specified array by 1/nfft.
        The inverse of a real-to-complex FFT is a complex-to-real FFT
        (with opposite sign) followed by this scaling.
        
        Parameters
        -----------
        n1 : int
            1st (only) dimension of the array rx.
        rx : Float1D
            the input/output array[n1].
        """

    @overload
    def scale(self, n1: int, n2: int, rx: Float2D) -> None:
        """
        Scales n1n2 real numbers in the specified array by 1/nfft.
        The inverse of a real-to-complex FFT is a complex-to-real FFT
        (with opposite sign) followed by this scaling.
        
        Parameters
        -----------
        n1 : int
            the 1st dimension of the array rx.
        n2 : int
            the 2nd dimension of the array rx.
        rx : Float2D
            the input/output array[n2][n1].
        """

    @overload
    def scale(self, n1: int, n2: int, n3: int, rx: Float3D) -> None:
        """
        Scales n1n2n3 real numbers in the specified array by 1/nfft.
        The inverse of a real-to-complex FFT is a complex-to-real FFT
        (with opposite sign) followed by this scaling.
        
        Parameters
        -----------
        n1 : int
            the 1st dimension of the array rx.
        n2 : int
            the 2nd dimension of the array rx.
        n3 : int
            the 3rd dimension of the array rx.
        rx : Float3D
            the input/output array[n3][n2][n1].
        """
