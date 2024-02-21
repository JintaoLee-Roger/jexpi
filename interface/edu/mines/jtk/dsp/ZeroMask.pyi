from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class ZeroMask:
    """
    A mask for samples that are zero or near zero.
    Values in the mask image are either true or false. Samples for which
    the mask is false may be unreliable in some applications, and this
    class can be used to identify these samples.
    For example, at samples in 3D images where the zero mask is false,
    we may set structure tensors to represent default horizontal layering.
    A sample in the mask is set to false if the mean absolute value
    of samples in a local Gaussian window is less than some specified
    fraction of the global mean absolute value of all image samples.
    Note that the global mean can be altered significantly by just a
    few samples with unusually large negative or positive values. Such
    outliers should be replaced before constructing a zero mask.
    """

    @overload
    def __init__(self, small: double, sigma1: double, sigma2: double,
                 x: Float2D) -> None:
        """
        Constructs a zero mask for a 2D image.
        The mask will be zero for samples where the local mean absolute
        amplitude is less than the specified small fraction of the global
        mean absolute amplitude.
        
        Parameters
        -----------
        small : double
            a small fraction; e.g., 0.1.
        sigma1 : double
            Gaussian window half-width for 1st dimension.
        sigma2 : double
            Gaussian window half-width for 2nd dimension.
        x : Float2D
            array of image values from which mask is derived.
        """

    @overload
    def __init__(self, small: double, sigma1: double, sigma2: double,
                 sigma3: double, x: Float3D) -> None:
        """
        Constructs a zero mask for a 3D image.
        
        Parameters
        -----------
        small : double
            small value; zeros in mask where labs &lt; smallgabs.
        sigma1 : double
            Gaussian window half-width for 1st dimension.
        sigma2 : double
            Gaussian window half-width for 2nd dimension.
        sigma3 : double
            Gaussian window half-width for 3rd dimension.
        x : Float3D
            array of image values from which mask is derived.
        """

    @overload
    def __init__(self, x: Float2D) -> None:
        """
        Constructs a zero mask from a specified array of floats.
        Mask is true for all non-zero samples in the array; false, otherwise.
        
        Parameters
        -----------
        x : Float2D
            array of values from which mask is derived.
        """

    @overload
    def __init__(self, x: Float3D) -> None:
        """
        Constructs a zero mask from a specified array of floats.
        Mask is true for all non-zero samples in the array; false, otherwise.
        
        Parameters
        -----------
        x : Float3D
            array of values from which mask is derived.
        """

    def getAsFloats2(self) -> Float2D:
        """
        Returns a 2D array of floats representing this mask.
        The returned array has values 0.0f (false) and 1.0f (true).
        Returns
        --------
        output : Float2D
            mask array of floats.
        """

    @overload
    def getAsFloats(self, mask: Float2D) -> None:
        """
        Fills a 2D array of floats representing this mask.
        The returned array has values 0.0f (false) and 1.0f (true).
        
        Parameters
        -----------
        mask : Float2D
            array of floats representing this mask.
        """

    def getAsFloats3(self) -> Float3D:
        """
        Returns a 3D array of floats representing this mask.
        The returned array has values 0.0f (false) and 1.0f (true).
        Returns
        --------
        output : Float3D
            mask array of floats.
        """

    @overload
    def getAsFloats(self, mask: Float3D) -> None:
        """
        Fills a 3D array of floats representing this mask.
        The returned array has values 0.0f (false) and 1.0f (true).
        
        Parameters
        -----------
        mask : Float3D
            array of floats representing this mask.
        """

    @overload
    def apply(self, vfalse: float, v: Float2D) -> None:
        """
        Applies this mask to a specified array of values.
        
        Parameters
        -----------
        vfalse : float
            value to use where mask is false.
        v : Float2D
            array of values to be masked.
        """

    @overload
    def apply(self, vfalse: float, v: Float3D) -> None:
        """
        Applies this mask to a specified array of values.
        
        Parameters
        -----------
        vfalse : float
            value to use where mask is false.
        v : Float3D
            array of values to be masked.
        """

    @overload
    def apply(self, efalse: Float1D, e: EigenTensors2) -> None:
        """
        Applies this mask to a specified eigentensor field.
        where the mask is false.
        
        Parameters
        -----------
        efalse : Float1D
            eigentensor {e11,e12,e22} to use for samples
        e : EigenTensors2
            eigentensors to be masked.
        """

    @overload
    def apply(self, efalse: Float1D, e: EigenTensors3) -> None:
        """
        Applies this mask to a specified eigentensor field.
        for samples where the mask is false.
        
        Parameters
        -----------
        efalse : Float1D
            eigentensor {e11,e12,e13,e22,e23,e33} to use
        e : EigenTensors3
            eigentensors to be masked.
        """
