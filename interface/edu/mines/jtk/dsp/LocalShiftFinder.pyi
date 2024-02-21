from typing import overload
from edu.mines.jtk.mapping import *


class LocalShiftFinder:
    """
    Estimates displacement vector fields for two images. For example, given
    two 2-D images f(x1,x2) and g(x1,x2), a shift finder estimates two vector
    components of displacement u1(x1,x2) and u2(x1,x2) such that
    f(x1,x2) ~ g(x1+u1(x1,x2),x2+u2(x1,x2)).
    
    Like the images f and g, the components of displacement are sampled
    functions of coordinates x1 and x2. That is, displacements may vary
    from sample to sample. The components u1 and u2 represent displacements
    in the x1 and x2 coordinate directions, respectively.
    
    This shift finder estimates each component of displacement using local
    cross-correlations. For each image sample, the estimated shift is that
    which yields the maximum correlation coefficient. This coefficient is
    found by quadratic interpolation of correlation functions sampled at
    integer lags.
    
    The peak (maximum) correlation coefficient may be used to measure
    quality of an estimated shift. However, because a correlation function
    may have more than one peak (local maxima), a better measure of quality
    may be the difference between the coefficients for the correlation peak
    and next highest peak. Both the peak coefficient and this difference may
    be computed with the shifts.
    
    Methods are provided to find and compensate for each component of shift
    sequentially. As each component is found, that component can be removed
    from the image g before estimating another component. For example, again
    for 2-D images f(x1,x2) and g(x1,x2), we might first estimate u1(x1,x2).
    If we then compute an image h(x1,x2) = g(x1+u1(x1,x2),x2), we can use
    f(x1,x2) and h(x1,x2) to estimate u2(x1,x2). By repeating this process
    sequentially, we obtain estimates for both u1(x1,x2) and u2(x1,x2) such
    that f(x1,x2) ~ g(x1+u1(x1,x2),x2+u2(x1,x2)).
    
    Methods are also provided to whiten 2-D and 3-D images before estimating
    displacement vectors. This (spectral) whitening improves estimates of
    displacements parallel to image features that may be otherwise poorly
    resolved. Whitening is performed with local prediction error filters
    computed from local auto-correlations.
    """

    @overload
    def __init__(self, sigma: double) -> None:
        """
        Construct a shift estimator with specified parameters.
        When applied to multi-dimensional arrays, the estimator has the
        same correlation window half-width for all dimensions.
        
        Parameters
        -----------
        sigma : double
            the correlation window half-width; must not be less than 1.
        """

    @overload
    def __init__(self, sigma1: double, sigma2: double) -> None:
        """
        Construct a shift estimator with specified parameters.
        When applied to multi-dimensional arrays, the estimator has half-width
        sigma1 for the 1st dimension and half-width sigma2 for 2nd and higher
        dimensions.
        must not be less than 1.
        dimensions; must not be less than 1.
        
        Parameters
        -----------
        sigma1 : double
            correlaton window half-width for 0st dimension;
        sigma2 : double
            correlation window half-width for 2nd and higher
        """

    @overload
    def __init__(self, sigma1: double, sigma2: double, sigma3: double) -> None:
        """
        Construct a shift estimator with specified parameters.
        When applied to multi-dimensional arrays, the estimator has half-width
        sigma1 for the 1st dimension, half-width sigma2 for the 2nd dimension,
        and half-width sigma3 for 3rd and higher dimensions.
        must not be less than 1.
        must not be less than 1.
        dimensions; must not be less than 1.
        
        Parameters
        -----------
        sigma1 : double
            correlation window half-width for 1st dimension;
        sigma2 : double
            correlation window half-width for 2nd dimension;
        sigma3 : double
            correlation window half-width for 3rd and higher
        """

    def setInterpolateDisplacements(self, enable: bool) -> None:
        """
        Enables or disables interpolation of displacements when shifting.
        The default is to interpolate displacements. This is the most
        accurate method when sequentially applying non-constant shifts.
        
        Parameters
        -----------
        enable : bool
            true, to enable interpolation; false, to disable.
        """

    @overload
    def find1(self, min1: int, max1: int, f: Float1D, g: Float1D,
              u: Float1D) -> None:
        """
        Finds shifts in the 1st (and only) dimension.
        
        Parameters
        -----------
        min1 : int
            the minimum shift.
        max1 : int
            the maximum shift.
        f : Float1D
            the input array f.
        g : Float1D
            the input array g.
        u : Float1D
            output array of shifts.
        """

    @overload
    def find1(self, min1: int, max1: int, f: Float1D, g: Float1D, u: Float1D,
              c: Float1D, d: Float1D) -> None:
        """
        Finds shifts in the 1st (and only) dimension.
        Also computes peak correlation coefficients and differences between
        the peak and next-highest-peak coeffcients.
        
        Parameters
        -----------
        min1 : int
            the minimum shift.
        max1 : int
            the maximum shift.
        f : Float1D
            the input array f.
        g : Float1D
            the input array g.
        u : Float1D
            output array of shifts.
        c : Float1D
            output array of peak correlation coefficients.
        d : Float1D
            output array of differences, peak minus next-highest-peak.
        """

    @overload
    def find1(self, min1: int, max1: int, f: Float2D, g: Float2D,
              u: Float2D) -> None:
        """
        Finds shifts in the 1st dimension.
        
        Parameters
        -----------
        min1 : int
            the minimum shift.
        max1 : int
            the maximum shift.
        f : Float2D
            the input array f.
        g : Float2D
            the input array g.
        u : Float2D
            output array of shifts.
        """

    @overload
    def find2(self, min2: int, max2: int, f: Float2D, g: Float2D,
              u: Float2D) -> None:
        """
        Finds shifts in the 2nd dimension.
        
        Parameters
        -----------
        min2 : int
            the minimum shift.
        max2 : int
            the maximum shift.
        f : Float2D
            the input array f.
        g : Float2D
            the input array g.
        u : Float2D
            output array of shifts.
        """

    @overload
    def find1(self, min1: int, max1: int, f: Float3D, g: Float3D,
              u: Float3D) -> None:
        """
        Finds shifts in the 1st dimension.
        
        Parameters
        -----------
        min1 : int
            the minimum shift.
        max1 : int
            the maximum shift.
        f : Float3D
            the input array f.
        g : Float3D
            the input array g.
        u : Float3D
            output array of shifts.
        """

    @overload
    def find2(self, min2: int, max2: int, f: Float3D, g: Float3D,
              u: Float3D) -> None:
        """
        Finds shifts in the 2nd dimension.
        
        Parameters
        -----------
        min2 : int
            the minimum shift.
        max2 : int
            the maximum shift.
        f : Float3D
            the input array f.
        g : Float3D
            the input array g.
        u : Float3D
            output array of shifts.
        """

    def find3(self, min3: int, max3: int, f: Float3D, g: Float3D,
              u: Float3D) -> None:
        """
        Finds shifts in the 3rd dimension.
        
        Parameters
        -----------
        min3 : int
            the minimum shift.
        max3 : int
            the maximum shift.
        f : Float3D
            the input array f.
        g : Float3D
            the input array g.
        u : Float3D
            output array of shifts.
        """

    @overload
    def shift1(self, du: Float1D, u1: Float1D, h: Float1D) -> None:
        """
        Applies specified shift in the 1st (and only) dimension.
        
        Parameters
        -----------
        du : Float1D
            input array of changes to displacements in 1st dimension.
        u1 : Float1D
            input/output array of displacements in 1st dimension.
        h : Float1D
            input/output array of image samples.
        """

    @overload
    def shift1(self, du: Float2D, u1: Float2D, u2: Float2D,
               h: Float2D) -> None:
        """
        Applies specified shift in the 1st dimension.
        
        Parameters
        -----------
        du : Float2D
            input array of changes to displacements in 1st dimension.
        u1 : Float2D
            input/output array of displacements in 1st dimension.
        u2 : Float2D
            input/output array of displacements in 2nd dimension.
        h : Float2D
            input/output array of image samples.
        """

    @overload
    def shift2(self, du: Float2D, u1: Float2D, u2: Float2D,
               h: Float2D) -> None:
        """
        Applies specified shift in the 2nd dimension.
        
        Parameters
        -----------
        du : Float2D
            input array of changes to displacements in 2nd dimension.
        u1 : Float2D
            input/output array of displacements in 1st dimension.
        u2 : Float2D
            input/output array of displacements in 2nd dimension.
        h : Float2D
            input/output array of image samples.
        """

    @overload
    def shift1(self, du: Float3D, u1: Float3D, u2: Float3D, u3: Float3D,
               h: Float3D) -> None:
        """
        Applies specified shift in the 1st dimension.
        
        Parameters
        -----------
        du : Float3D
            input array of changes to displacements in 1st dimension.
        u1 : Float3D
            input/output array of displacements in 1st dimension.
        u2 : Float3D
            input/output array of displacements in 2nd dimension.
        u3 : Float3D
            input/output array of displacements in 3rd dimension.
        h : Float3D
            input/output array of image samples.
        """

    @overload
    def shift2(self, du: Float3D, u1: Float3D, u2: Float3D, u3: Float3D,
               h: Float3D) -> None:
        """
        Applies specified shift in the 2nd dimension.
        
        Parameters
        -----------
        du : Float3D
            input array of changes to displacements in 2nd dimension.
        u1 : Float3D
            input/output array of displacements in 1st dimension.
        u2 : Float3D
            input/output array of displacements in 2nd dimension.
        u3 : Float3D
            input/output array of displacements in 3rd dimension.
        h : Float3D
            input/output array of image samples.
        """

    def shift3(self, du: Float3D, u1: Float3D, u2: Float3D, u3: Float3D,
               h: Float3D) -> None:
        """
        Applies specified shift in the 3rd dimension.
        
        Parameters
        -----------
        du : Float3D
            input array of changes to displacements in 3rd dimension.
        u1 : Float3D
            input/output array of displacements in 1st dimension.
        u2 : Float3D
            input/output array of displacements in 2nd dimension.
        u3 : Float3D
            input/output array of displacements in 3rd dimension.
        h : Float3D
            input/output array of image samples.
        """

    @overload
    def whiten(self, f: Float2D, g: Float2D) -> None:
        """
        Applies local prediction-error (spectal whitening) filters.
        The input and output arrays f and g can be the same array.
        
        Parameters
        -----------
        f : Float2D
            the input array.
        g : Float2D
            the output array.
        """

    @overload
    def whiten(self, sigma: double, f: Float2D, g: Float2D) -> None:
        """
        Applies local prediction-error (spectal whitening) filters.
        The input and output arrays f and g can be the same array.
        less than one for no smoothing.
        
        Parameters
        -----------
        sigma : double
            half-width of Gaussian smoothing applied after whitening;
        f : Float2D
            the input array.
        g : Float2D
            the output array.
        """

    @overload
    def whiten(self, f: Float3D, g: Float3D) -> None:
        """
        Applies local prediction-error (spectal whitening) filters.
        The input and output arrays f and g can be the same array.
        Smooths the output with a Gaussian filter with half-width sigma = 1.0.
        
        Parameters
        -----------
        f : Float3D
            the input array.
        g : Float3D
            the output array.
        """

    @overload
    def whiten(self, sigma: double, f: Float3D, g: Float3D) -> None:
        """
        Applies local prediction-error (spectal whitening) filters.
        The input and output arrays f and g can be the same array.
        less than one for no smoothing.
        
        Parameters
        -----------
        sigma : double
            half-width of Gaussian smoothing applied after whitening;
        f : Float3D
            the input array.
        g : Float3D
            the output array.
        """
