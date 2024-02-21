from typing import overload
from edu.mines.jtk.mapping import *


class DynamicWarping:
    """
    Dynamic warping of sequences and images.
    
    For sequences f and g, dynamic warping finds a sequence of
    shifts u such that f[i1] ~ g[i1+u[i1]], subject to a bound b1
    on strain, the rate at which the shifts u[i1] vary with sample
    index i1.
    
    An increasing u[i1] = u[i1-1] + 1 implies that, between indices
    i1-1 and i1, g[i1] is a stretched version of f[i1] ~ g[i1+u[i1]].
    For, in this case, values in f for indices i1 and i1-1 are one
    sample apart, but corresponding values in g are two samples
    apart, which implies stretching by 100%. Likewise, a decreasing
    u[i1] = u[i1-1] - 1 implies squeezing by 100%.
    
    In practice, 100% strain (stretching or squeezing) may be extreme.
    Therefore, the upper bound on strain may be smaller than one. For
    example, if the bound b1 = 0.5, then |u[i1]-u[i1-1]| &le; 0.5.
    
    For 2D images f and g, dynamic warping finds a 2D array of shifts
    u[i2][i1] such that f[i2][i1] ~ g[i2][i1+u[i2][i1]], subject to
    bounds b1 and b2 on strains, the rates at which shifts u[i2][i1]
    vary with samples indices i1 and i2, respectively.
    
    For 3D images f and g, dynamic warping finds a 3D array of shifts
    u[i3][i2][i1] in a similar way. However, finding shifts for 3D
    images may require an excessive amount of memory. Dynamic image
    warping requires a temporary array of nlagnsample floats, where
    the number of lags nlag = 1+shiftMax-shiftMin and nsample is the
    number of image samples. For 3D images, the product nlagnsample
    is likely to be too large for the temporary array to fit in random-
    access memory (RAM). In this case, shifts u are obtained by blending
    together shifts computed from overlapping subsets of the 3D image.
    
    Estimated shifts u can be smoothed, and the extent of smoothing
    along each dimension is inversely proportional to the strain limit
    for that dimension. These extents can be scaled by specified factors
    for more or less smoothing. The default scale factors are zero, for
    no smoothing.
    
    This class provides numerous methods, but typical applications
    require only several of these, usually only the methods that find
    and apply shifts. The many other methods are provided only for
    atypical applications and research.
    """

    def __init__(self, shiftMin: int, shiftMax: int) -> None:
        """
        Constructs a dynamic warping for specified bounds on shifts.
        
        Parameters
        -----------
        shiftMin : int
            lower bound on shift u.
        shiftMax : int
            upper bound on shift u.
        """

    @overload
    def setStrainMax(self, strainMax: double) -> None:
        """
        Sets bound on strain for all dimensions. Must be in (0,1].
        The actual bound on strain is 1.0/ceil(1.0/strainMax), which
        is less than the specified strainMax when 1.0/strainMax is not
        an integer. The default bound on strain is 1.0 (100%).
        
        Parameters
        -----------
        strainMax : double
            the bound, a value less than or equal to one.
        """

    @overload
    def setStrainMax(self, strainMax1: double, strainMax2: double) -> None:
        """
        Sets bound on strains in 1st and 2nd dimensions.
        
        Parameters
        -----------
        strainMax1 : double
            bound on strain in the 1st dimension.
        strainMax2 : double
            bound on strain in the 2nd dimension.
        """

    @overload
    def setStrainMax(self, strainMax1: double, strainMax2: double,
                     strainMax3: double) -> None:
        """
        Sets bound on strains in 1st, 2nd and 3rd dimensions.
        
        Parameters
        -----------
        strainMax1 : double
            bound on strain in the 1st dimension.
        strainMax2 : double
            bound on strain in the 2nd dimension.
        strainMax3 : double
            bound on strain in the 3rd dimension.
        """

    def setErrorExtrapolation(self, ee: ErrorExtrapolation) -> None:
        """
        Sets the method used to extrapolate alignment errors.
        Extrapolation is necessary when the sum i+l of sample index
        i and lag l is out of bounds. The default method is to use
        the error computed for the nearest index i and the same lag l.
        
        Parameters
        -----------
        ee : ErrorExtrapolation
            the error extrapolation method.
        """

    def setErrorExponent(self, e: double) -> None:
        """
        Sets the exponent used to compute alignment errors |f-g|^e.
        The default exponent is 2.
        
        Parameters
        -----------
        e : double
            the exponent.
        """

    def setErrorSmoothing(self, esmooth: int) -> None:
        """
        Sets the number of nonlinear smoothings of alignment errors.
        In dynamic warping, alignment errors are smoothed the specified
        number of times, along all dimensions (in order 1, 2, ...),
        before estimating shifts by accumulating and backtracking along
        only the 1st dimension.
        
        The default number of smoothings is zero, which is best for 1D
        sequences. For 2D and 3D images, two smoothings are recommended.
        
        Parameters
        -----------
        esmooth : int
            number of nonlinear smoothings.
        """

    @overload
    def setShiftSmoothing(self, usmooth: double) -> None:
        """
        Sets extent of smoothing filters used to smooth shifts.
        Half-widths of smoothing filters are inversely proportional to
        strain limits, and are scaled by the specified factor. Default
        factor is zero, for no smoothing.
        
        Parameters
        -----------
        usmooth : double
            extent of smoothing filter in all dimensions.
        """

    @overload
    def setShiftSmoothing(self, usmooth1: double, usmooth2: double) -> None:
        """
        Sets extents of smoothing filters used to smooth shifts.
        Half-widths of smoothing filters are inversely proportional to
        strain limits, and are scaled by the specified factors. Default
        factors are zero, for no smoothing.
        
        Parameters
        -----------
        usmooth1 : double
            extent of smoothing filter in 1st dimension.
        usmooth2 : double
            extent of smoothing filter in 2nd dimension.
        """

    @overload
    def setShiftSmoothing(self, usmooth1: double, usmooth2: double,
                          usmooth3: double) -> None:
        """
        Sets extents of smoothing filters used to smooth shifts.
        Half-widths of smoothing filters are inversely proportional to
        strain limits, and are scaled by the specified factors. Default
        factors are zero, for no smoothing.
        
        Parameters
        -----------
        usmooth1 : double
            extent of smoothing filter in 1st dimension.
        usmooth2 : double
            extent of smoothing filter in 2nd dimension.
        usmooth3 : double
            extent of smoothing filter in 3rd dimension.
        """

    def setWindowSizeAndOverlap(self, l2: int, l3: int, f2: double,
                                f3: double) -> None:
        """
        Sets the size and overlap of windows used for 3D image warping.
        Window size determines the amount of memory required to store
        a temporary array[l3][l2][n1][nl] of floats used to compute
        shifts. Here, nl is the number of lags and n1, l2 and l3 are
        the numbers of samples in the 1st, 2nd and 3rd dimensions of
        3D image subsets. Let n1, n2 and n3 denote numbers of samples
        for all three dimensions of a complete 3D image. Typically,
        l2&lt;n2 and l3&lt;n3, because insufficient memory is available
        for a temporary array of nln1n2n3 floats.
        
        Image subsets overlap in the 2nd and 3rd dimensions by specified
        fractions f2 and f3, which must be less than one. Because window
        sizes are integers, the actual overlap be greater than (but never
        less than) these fractions.
        
        Default window sizes are 50 samples; default overlap fractions
        are 0.5, which corresponds to 50% overlap in both dimensions.
        
        Parameters
        -----------
        l2 : int
            length of window in 2nd dimension.
        l3 : int
            length of window in 3rd dimension.
        f2 : double
            fraction of window overlap in 2nd dimension.
        f3 : double
            fraction of window overlap in 3rd dimension.
        """

    @overload
    def findShifts(self, f: Float1D, g: Float1D) -> Float1D:
        """
        Computes and returns shifts for specified sequences.
        
        Parameters
        -----------
        f : Float1D
            array for the sequence f.
        g : Float1D
            array for the sequence g.
        
        Returns
        --------
        output : Float1D
            array of shifts u.
        """

    @overload
    def findShifts(self, f: Float2D, g: Float2D) -> Float2D:
        """
        Computes and returns shifts for specified images.
        
        Parameters
        -----------
        f : Float2D
            array for the image f.
        g : Float2D
            array for the image g.
        
        Returns
        --------
        output : Float2D
            array of shifts u.
        """

    @overload
    def findShifts(self, f: Float3D, g: Float3D) -> Float3D:
        """
        Computes and returns shifts for specified images.
        
        Parameters
        -----------
        f : Float3D
            array for the image f.
        g : Float3D
            array for the image g.
        
        Returns
        --------
        output : Float3D
            array of shifts u.
        """

    @overload
    def findShifts1(self, f: Float2D, g: Float2D) -> Float1D:
        """
        Computes and returns 1D shifts u for specified 2D images f and g.
        This method is useful in the case that shifts vary only slightly
        (or perhaps not at all) in the 2nd image dimension.
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] for the image f.
        g : Float2D
            array[n2][n1] for the image g.
        
        Returns
        --------
        output : Float1D
            array[n1] of shifts u.
        """

    @overload
    def findShifts1(self, f: Float3D, g: Float3D) -> Float1D:
        """
        Computes and returns 1D shifts u for specified 3D images f and g.
        This method is useful in the case that shifts vary only slightly
        (or perhaps not at all) in the 2nd and 3rd image dimensions.
        
        Parameters
        -----------
        f : Float3D
            array[n3][n2][n1] for the image f.
        g : Float3D
            array[n3][n2][n1] for the image g.
        
        Returns
        --------
        output : Float1D
            array[n1] of shifts u.
        """

    @overload
    def findShifts(self, f: Float1D, g: Float1D, u: Float1D) -> None:
        """
        Computes shifts for specified sequences.
        
        Parameters
        -----------
        f : Float1D
            input array for the sequence f.
        g : Float1D
            input array for the sequence g.
        u : Float1D
            output array of shifts u.
        """

    @overload
    def findShifts(self, f: Float2D, g: Float2D, u: Float2D) -> None:
        """
        Computes shifts for specified images.
        
        Parameters
        -----------
        f : Float2D
            input array for the image f.
        g : Float2D
            input array for the image g.
        u : Float2D
            output array of shifts u.
        """

    @overload
    def findShifts(self, f: Float3D, g: Float3D, u: Float3D) -> None:
        """
        Computes shifts for specified images.
        
        Parameters
        -----------
        f : Float3D
            input array for the image f.
        g : Float3D
            input array for the image g.
        u : Float3D
            output array of shifts u.
        """

    @overload
    def findShifts1(self, f: Float2D, g: Float2D, u: Float1D) -> None:
        """
        Computes 1D shifts u for specified 2D images f and g.
        This method is useful in the case that shifts vary only slightly
        (or perhaps not at all) in the 2nd image dimension.
        
        Parameters
        -----------
        f : Float2D
            input array[n2][n1] for the image f.
        g : Float2D
            input array[n2][n1] for the image g.
        u : Float1D
            output array[n1] of shifts u.
        """

    @overload
    def findShifts1(self, f: Float3D, g: Float3D, u: Float1D) -> None:
        """
        Computes 1D shifts u for specified 3D images f and g.
        This method is useful in the case that shifts vary only slightly
        (or perhaps not at all) in the 2nd and 3rd image dimensions.
        
        Parameters
        -----------
        f : Float3D
            input array[n3][n2][n1] for the image f.
        g : Float3D
            input array[n3][n2][n1] for the image g.
        u : Float1D
            output array[n1] of shifts u.
        """

    @overload
    def applyShifts(self, u: Float1D, g: Float1D) -> Float1D:
        """
        Returns a sequence warped by applying specified shifts.
        
        Parameters
        -----------
        u : Float1D
            array of shifts.
        g : Float1D
            array for the sequence to be warped.
        
        Returns
        --------
        output : Float1D
            array for the warped sequence.
        """

    @overload
    def applyShifts(self, u: Float2D, g: Float2D) -> Float2D:
        """
        Returns an image warped by applying specified shifts.
        
        Parameters
        -----------
        u : Float2D
            array of shifts.
        g : Float2D
            array for the image to be warped.
        
        Returns
        --------
        output : Float2D
            array for the warped image.
        """

    @overload
    def applyShifts(self, u: Float3D, g: Float3D) -> Float3D:
        """
        Returns an image warped by applying specified shifts.
        
        Parameters
        -----------
        u : Float3D
            array of shifts.
        g : Float3D
            array for the image to be warped.
        
        Returns
        --------
        output : Float3D
            array for the warped image.
        """

    @overload
    def applyShifts(self, u: Float1D, g: Float1D, h: Float1D) -> None:
        """
        Computes a sequence warped by applying specified shifts.
        
        Parameters
        -----------
        u : Float1D
            input array of shifts.
        g : Float1D
            input array for the sequence to be warped.
        h : Float1D
            output array for the warped sequence.
        """

    @overload
    def applyShifts(self, u: Float2D, g: Float2D, h: Float2D) -> None:
        """
        Computes an image warped by applying specified shifts.
        
        Parameters
        -----------
        u : Float2D
            input array of shifts.
        g : Float2D
            input array for the image to be warped.
        h : Float2D
            output array for the warped image.
        """

    @overload
    def applyShifts(self, u: Float3D, g: Float3D, h: Float3D) -> None:
        """
        Computes an image warped by applying specified shifts.
        
        Parameters
        -----------
        u : Float3D
            input array of shifts.
        g : Float3D
            input array for the image to be warped.
        h : Float3D
            output array for the warped image.
        """

    @overload
    def computeErrors(self, f: Float1D, g: Float1D) -> Float2D:
        """
        Returns normalized alignment errors for all samples and lags.
        The number of lags nl = 1+shiftMax-shiftMin. Lag indices
        il = 0, 1, 2, ..., nl-1 correspond to integer shifts in
        [shiftMin,shiftMax]. Alignment errors are a monotonically
        increasing function of |f[i1]-g[i1+il+shiftMin]|.
        
        Parameters
        -----------
        f : Float1D
            array[n1] for the sequence f[i1].
        g : Float1D
            array[n1] for the sequence g[i1].
        
        Returns
        --------
        output : Float2D
            array[n1][nl] of alignment errors.
        """

    @overload
    def computeErrors(self, f: Float2D, g: Float2D) -> Float3D:
        """
        Returns normalized alignment errors for all samples and lags.
        The number of lags nl = 1+shiftMax-shiftMin. Lag indices
        il = 0, 1, 2, ..., nl-1 correspond to integer shifts in
        [shiftMin,shiftMax]. Alignment errors are a monotonically
        increasing function of |f[i2][i1]-g[i2][i1+il+shiftMin]|.
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] for the image f[i2][i1].
        g : Float2D
            array[n2][n1] for the image g[i2][i1].
        
        Returns
        --------
        output : Float3D
            array[n2][n1][nl] of alignment errors.
        """

    @overload
    def computeErrors1(self, f: Float2D, g: Float2D) -> Float2D:
        """
        Returns normalized 1D alignment errors for 2D images.
        The number of lags nl = 1+shiftMax-shiftMin. Lag indices
        il = 0, 1, 2, ..., nl-1 correspond to integer shifts in
        [shiftMin,shiftMax].
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] for the image f[i2][i1].
        g : Float2D
            array[n2][n1] for the image g[i2][i1].
        
        Returns
        --------
        output : Float2D
            array[n1][nl] of alignment errors.
        """

    @overload
    def computeErrors1(self, f: Float3D, g: Float3D) -> Float2D:
        """
        Returns normalized 1D alignment errors for 3D images.
        The number of lags nl = 1+shiftMax-shiftMin. Lag indices
        il = 0, 1, 2, ..., nl-1 correspond to integer shifts in
        [shiftMin,shiftMax].
        
        Parameters
        -----------
        f : Float3D
            array[n3][n2][n1] for the image f[i3][i2][i1].
        g : Float3D
            array[n3][n2][n1] for the image g[i3][i2][i1].
        
        Returns
        --------
        output : Float2D
            array[n1][nl] of alignment errors.
        """

    @overload
    def smoothErrors(self, e: Float2D) -> Float2D:
        """
        Returns smoothed (and normalized) alignment errors.
        
        Parameters
        -----------
        e : Float2D
            array[n1][nl] of alignment errors.
        
        Returns
        --------
        output : Float2D
            array[n1][nl] of smoothed errors.
        """

    @overload
    def smoothErrors(self, e: Float3D) -> Float3D:
        """
        Returns smoothed (and normalized) alignment errors.
        
        Parameters
        -----------
        e : Float3D
            array[n2][n1][nl] of alignment errors.
        
        Returns
        --------
        output : Float3D
            array[n2][n1][nl] of smoothed errors.
        """

    @overload
    def smoothErrors(self, e: Float2D, es: Float2D) -> None:
        """
        Smooths (and normalizes) alignment errors.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        e : Float2D
            input array[n1][nl] of alignment errors.
        es : Float2D
            output array[n1][nl] of smoothed errors.
        """

    @overload
    def smoothErrors(self, e: Float3D, es: Float3D) -> None:
        """
        Smooths (and normalizes) alignment errors.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        e : Float3D
            input array[n2][n1][nl] of alignment errors.
        es : Float3D
            output array[n2][n1][nl] of smoothed errors.
        """

    def smoothErrors1(self, e: Float3D, es: Float3D) -> None:
        """
        Smooths (and normalizes) alignment errors in only the 1st dimension.
        Input and output arrays can be the same array.
        
        Parameters
        -----------
        e : Float3D
            input array[n2][n1][nl] of alignment errors.
        es : Float3D
            output array[n2][n1][nl] of smoothed errors.
        """

    @overload
    def smoothShifts(self, u: Float1D) -> Float1D:
        """
        Returns smoothed shifts.
        
        Parameters
        -----------
        u : Float1D
            array of shifts to be smoothed.
        
        Returns
        --------
        output : Float1D
            array of smoothed shifts
        """

    @overload
    def smoothShifts(self, u: Float2D) -> Float2D:
        """
        Returns smoothed shifts.
        
        Parameters
        -----------
        u : Float2D
            array of shifts to be smoothed.
        
        Returns
        --------
        output : Float2D
            array of smoothed shifts
        """

    @overload
    def smoothShifts(self, u: Float1D, us: Float1D) -> None:
        """
        Smooths the specified shifts. Smoothing can be performed
        in place; input and output arrays can be the same array.
        
        Parameters
        -----------
        u : Float1D
            input array of shifts to be smoothed.
        us : Float1D
            output array of smoothed shifts.
        """

    @overload
    def smoothShifts(self, u: Float2D, us: Float2D) -> None:
        """
        Smooths the specified shifts. Smoothing can be performed
        in place; input and output arrays can be the same array.
        
        Parameters
        -----------
        u : Float2D
            input array of shifts to be smoothed.
        us : Float2D
            output array of smoothed shifts.
        """

    @overload
    def accumulateForward(self, e: Float2D) -> Float2D:
        """
        Returns errors accumulated in forward direction.
        
        Parameters
        -----------
        e : Float2D
            array of alignment errors.
        
        Returns
        --------
        output : Float2D
            array of accumulated errors.
        """

    @overload
    def accumulateReverse(self, e: Float2D) -> Float2D:
        """
        Returns errors accumulated in reverse direction.
        
        Parameters
        -----------
        e : Float2D
            array of alignment errors.
        
        Returns
        --------
        output : Float2D
            array of accumulated errors.
        """

    @overload
    def accumulateForward1(self, e: Float3D) -> Float3D:
        """
        Returns errors accumulated in forward direction in 1st dimension.
        
        Parameters
        -----------
        e : Float3D
            array of alignment errors.
        
        Returns
        --------
        output : Float3D
            array of accumulated errors.
        """

    @overload
    def accumulateReverse1(self, e: Float3D) -> Float3D:
        """
        Returns errors accumulated in reverse direction in 1st dimension.
        
        Parameters
        -----------
        e : Float3D
            array of alignment errors.
        
        Returns
        --------
        output : Float3D
            array of accumulated errors.
        """

    @overload
    def accumulateForward2(self, e: Float3D) -> Float3D:
        """
        Returns errors accumulated in forward direction in 2nd dimension.
        
        Parameters
        -----------
        e : Float3D
            array of alignment errors.
        
        Returns
        --------
        output : Float3D
            array of accumulated errors.
        """

    @overload
    def accumulateReverse2(self, e: Float3D) -> Float3D:
        """
        Returns errors accumulated in reverse direction in 2nd dimension.
        
        Parameters
        -----------
        e : Float3D
            array of alignment errors.
        
        Returns
        --------
        output : Float3D
            array of accumulated errors.
        """

    @overload
    def accumulateForward(self, e: Float2D, d: Float2D) -> None:
        """
        Accumulates alignment errors in forward direction.
        
        Parameters
        -----------
        e : Float2D
            input array of alignment errors.
        d : Float2D
            output array of accumulated errors.
        """

    @overload
    def accumulateReverse(self, e: Float2D, d: Float2D) -> None:
        """
        Accumulates alignment errors in reverse direction.
        
        Parameters
        -----------
        e : Float2D
            input array of alignment errors.
        d : Float2D
            output array of accumulated errors.
        """

    @overload
    def accumulateForward1(self, e: Float3D, d: Float3D) -> None:
        """
        Accumulates alignment errors in forward direction in 1st dimension.
        
        Parameters
        -----------
        e : Float3D
            input array of alignment errors.
        d : Float3D
            output array of accumulated errors.
        """

    @overload
    def accumulateReverse1(self, e: Float3D, d: Float3D) -> None:
        """
        Accumulates alignment errors in reverse direction in 1st dimension.
        
        Parameters
        -----------
        e : Float3D
            input array of alignment errors.
        d : Float3D
            output array of accumulated errors.
        """

    @overload
    def accumulateForward2(self, e: Float3D, d: Float3D) -> None:
        """
        Accumulates alignment errors in forward direction in 2nd dimension.
        
        Parameters
        -----------
        e : Float3D
            input array of alignment errors.
        d : Float3D
            output array of accumulated errors.
        """

    @overload
    def accumulateReverse2(self, e: Float3D, d: Float3D) -> None:
        """
        Accumulates alignment errors in reverse direction in 2nd dimension.
        
        Parameters
        -----------
        e : Float3D
            input array of alignment errors.
        d : Float3D
            output array of accumulated errors.
        """

    @overload
    def backtrackReverse(self, d: Float2D, e: Float2D) -> Float1D:
        """
        Returns shifts found by backtracking in reverse.
        
        Parameters
        -----------
        d : Float2D
            array of accumulated errors.
        e : Float2D
            array of alignment errors.
        
        Returns
        --------
        output : Float1D
            an array of shifts.
        """

    @overload
    def backtrackReverse1(self, d: Float3D, e: Float3D) -> Float2D:
        """
        Returns shifts found by backtracking in reverse in 1st dimension.
        
        Parameters
        -----------
        d : Float3D
            array of accumulated errors.
        e : Float3D
            array of alignment errors.
        
        Returns
        --------
        output : Float2D
            an array of shifts.
        """

    @overload
    def backtrackReverse2(self, d: Float3D, e: Float3D) -> Float2D:
        """
        Returns shifts found by backtracking in reverse in 2nd dimension.
        
        Parameters
        -----------
        d : Float3D
            array of accumulated errors.
        e : Float3D
            array of alignment errors.
        
        Returns
        --------
        output : Float2D
            an array of shifts.
        """

    @overload
    def backtrackReverse(self, d: Float2D, e: Float2D, u: Float1D) -> None:
        """
        Computes shifts by backtracking in reverse direction.
        
        Parameters
        -----------
        d : Float2D
            input array of accumulated errors.
        e : Float2D
            input array of alignment errors.
        u : Float1D
            output array of shifts.
        """

    @overload
    def backtrackReverse1(self, d: Float3D, e: Float3D, u: Float2D) -> None:
        """
        Computes shifts by backtracking in reverse direction in 1st dimension.
        
        Parameters
        -----------
        d : Float3D
            input array of accumulated errors.
        e : Float3D
            input array of alignment errors.
        u : Float2D
            output array of shifts.
        """

    @overload
    def backtrackReverse2(self, d: Float3D, e: Float3D, u: Float2D) -> None:
        """
        Computes shifts by backtracking in reverse direction in 2nd dimension.
        
        Parameters
        -----------
        d : Float3D
            input array of accumulated errors.
        e : Float3D
            input array of alignment errors.
        u : Float2D
            output array of shifts.
        """

    @overload
    @staticmethod
    def normalizeErrors(self, e: Float2D) -> None:
        """
        Normalizes alignment errors to be in range [0,1].
        
        Parameters
        -----------
        e : Float2D
            input/output array of alignment errors.
        """

    @overload
    @staticmethod
    def normalizeErrors(self, e: Float3D) -> None:
        """
        Normalizes alignment errors to be in range [0,1].
        
        Parameters
        -----------
        e : Float3D
            input/output array of alignment errors.
        """

    @overload
    def sumErrors(self, e: Float2D, u: Float1D) -> float:
        """
        Returns the sum of errors for specified shifts, rounded to integers.
        
        Parameters
        -----------
        e : Float2D
            array[n1][nl] of errors.
        u : Float1D
            array[n1] of shifts.
        
        Returns
        --------
        output : float
            the sum of errors.
        """

    @overload
    def sumErrors(self, e: Float3D, u: Float2D) -> float:
        """
        Returns the sum of errors for specified shifts, rounded to integers.
        
        Parameters
        -----------
        e : Float3D
            array[n2][n1][nl] of errors.
        u : Float2D
            array[n2][n1] of shifts.
        
        Returns
        --------
        output : float
            the sum of errors.
        """

    @overload
    @staticmethod
    def transposeLag(self, e: Float2D) -> Float2D:
        """
        Returns errors in an array with lag the slowest dimension.
        Useful only for visualization of errors. Other methods in this
        class assume that lag is the fastest dimension in arrays of errors.
        
        Parameters
        -----------
        e : Float2D
            array[n1][nl] of errors.
        
        Returns
        --------
        output : Float2D
            transposed array[nl][n1] of errors.
        """

    @overload
    @staticmethod
    def transposeLag(self, e: Float3D) -> Float3D:
        """
        Returns errors in an array with lag the slowest dimension.
        Useful only for visualization of errors. Other methods in this
        class assume that lag is the fastest dimension in arrays of errors.
        
        Parameters
        -----------
        e : Float3D
            array[n2][n1][nl] of errors.
        
        Returns
        --------
        output : Float3D
            transposed array[nl][n2][n1] of errors.
        """
