from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class RecursiveGaussianFilter:
    """
    Recursive implementation of a Gaussian filter and derivatives. Filters
    include the 0th, 1st, and 2nd derivatives. The impulse response of the
    0th-derivative smoothing filter is infinitely long, and is approximately
    h[n] = 1.0/(sqrt(2PI)sigma)exp(-0.5(nn)/(sigmasigma)). Here,
    sigma denotes the standard width of the Gaussian.
    
    For large filter widths sigma, this recursive implementation can be
    much more efficient than convolution with a truncated Gaussian.
    Specifically, if the Gaussian is truncated for |n| &gt; 4sigma, then
    this recursive implementation requires 2/sigma of the multiplications
    required by convolution. In other words, for sigma &gt; 2, this
    recursive implementation should be more efficient than convolution.
    
    For any application of this filter, input and output arrays may be the
    same array. When the filter cannot be applied in-place, intermediate
    arrays are constructed internally.
    
    This filter implements two different methods for approximating
    with difference equations a Gaussian filter and its derivatives.
    
    The first method is that of Deriche, R., 1993, Recursively implementing
    the Gaussian and its derivatives: INRIA Research Report, number 1893.
    Deriche's method is used for small widths sigma, for which it is most
    accurate.
    
    The second method is that of van Vliet, L.J., Young, I.T., and Verbeek,
    P.W., 1998, Recursive Gaussian derivative filters, Proceedings of the
    14th International Conference on Pattern Recognition, IEEE Computer
    Society Press. The parallel implementation used here yields zero-phase
    impulse responses without the end effects caused by the serial (cascade)
    poles-only implementation recommended by van Vliet, et al. This
    second method is used for large widths sigma.
    """

    @overload
    def __init__(self, sigma: double, method: Method) -> None:
        """
        Construct a Gaussian filter with specified width and design method.
        
        Parameters
        -----------
        sigma : double
            the width; must not be less than 1.
        method : Method
            the method used to design the filter.
        """

    @overload
    def __init__(self, sigma: double) -> None:
        """
        Construct a Gaussian filter with specified width.
        
        Parameters
        -----------
        sigma : double
            the width; must not be less than 1.
        """

    def apply0(self, x: Float1D, y: Float1D) -> None:
        """
        Applies the 0th-derivative filter.
        
        Parameters
        -----------
        x : Float1D
            the filter input.
        y : Float1D
            the filter output.
        """

    def apply1(self, x: Float1D, y: Float1D) -> None:
        """
        Applies the 1st-derivative filter.
        
        Parameters
        -----------
        x : Float1D
            the filter input.
        y : Float1D
            the filter output.
        """

    def apply2(self, x: Float1D, y: Float1D) -> None:
        """
        Applies the 2nd-derivative filter.
        
        Parameters
        -----------
        x : Float1D
            the filter input.
        y : Float1D
            the filter output.
        """

    def apply0X(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 0th-derivative filter along the 1st dimension.
        Applies no filter along the 2nd dimension.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def apply1X(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 1st-derivative filter along the 1st dimension.
        Applies no filter along the 2nd dimension.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def apply2X(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 2nd-derivative filter along the 1st dimension.
        Applies no filter along the 2nd dimension.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def applyX0(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 0th-derivative filter along the 2nd dimension.
        Applies no filter along the 1st dimension.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def applyX1(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 1st-derivative filter along the 2nd dimension.
        Applies no filter along the 1st dimension.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def applyX2(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 2nd-derivative filter along the 2nd dimension.
        Applies no filter along the 1st dimension.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def apply0XX(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 0th-derivative filter along the 1st dimension.
        Applies no filter along the 2nd or 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply1XX(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 1st-derivative filter along the 1st dimension.
        Applies no filter along the 2nd or 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply2XX(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 2nd-derivative filter along the 1st dimension.
        Applies no filter along the 2nd or 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def applyX0X(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 0th-derivative filter along the 2nd dimension.
        Applies no filter along the 1st or 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def applyX1X(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 1st-derivative filter along the 2nd dimension.
        Applies no filter along the 1st or 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def applyX2X(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 2nd-derivative filter along the 2nd dimension.
        Applies no filter along the 1st or 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def applyXX0(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 0th-derivative filter along the 3rd dimension.
        Applies no filter along the 1st or 2nd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def applyXX1(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 1st-derivative filter along the 3rd dimension.
        Applies no filter along the 1st or 2nd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def applyXX2(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 2nd-derivative filter along the 3rd dimension.
        Applies no filter along the 1st or 2nd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply00(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 0th-derivative filter along the 1st and 2nd dimensions.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def apply10(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 1st-derivative filter along the 1st dimension
        and the 0th-derivative filter along the 2nd dimension.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def apply01(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 0th-derivative filter along the 1st dimension
        and the 1st-derivative filter along the 2nd dimension.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def apply11(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 1st-derivative filter along the 1st and 2nd dimensions.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def apply20(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 2nd-derivative filter along the 1st dimension
        and the 0th-derivative filter along the 2nd dimension.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def apply02(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the 0th-derivative filter along the 1st dimension
        and the 2nd-derivative filter along the 2nd dimension.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    def apply000(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 0th-derivative filter along the 1st, 2nd and 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply100(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 1st-derivative filter along the 1st dimension
        and the 0th-derivative filter along the 2nd and 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply010(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 1st-derivative filter along the 2nd dimension
        and the 0th-derivative filter along the 1st and 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply001(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 1st-derivative filter along the 3rd dimension
        and the 0th-derivative filter along the 1st and 2nd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply110(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 1st-derivative filter along the 1st and 2nd dimensions
        and the 0th-derivative filter along the 3rd dimension.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply101(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 1st-derivative filter along the 1st and 3rd dimensions
        and the 0th-derivative filter along the 2nd dimension.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply011(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 1st-derivative filter along the 2nd and 3rd dimensions
        and the 0th-derivative filter along the 1st dimension.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply200(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 2nd-derivative filter along the 1st dimension
        and the 0th-derivative filter along the 2nd and 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply020(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 2nd-derivative filter along the 2nd dimension
        and the 0th-derivative filter along the 1st and 3rd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    def apply002(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the 2nd-derivative filter along the 3rd dimension
        and the 0th-derivative filter along the 1st and 2nd dimensions.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """
