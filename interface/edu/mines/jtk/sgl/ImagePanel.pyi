from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class ImagePanel:
    """
    An axis-aligned panel that draws a 2D image of a slice of a 3D array.
    The corner points of the image panel's axis-aligned frame determines
    which slice of the 3D array is drawn.
    """

    @overload
    def __init__(self, f: Float3D) -> None:
        """
        Constructs an image panel with default unit sampling for 3D array.
        
        Parameters
        -----------
        f : Float3D
            3D array of floats.
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, s3: Sampling,
                 f: Float3D) -> None:
        """
        Constructs an image panel for specified sampling and 3D array.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of 1st dimension (Z axis).
        s2 : Sampling
            sampling of 2nd dimension (Y axis).
        s3 : Sampling
            sampling of 3rd dimension (X axis).
        f : Float3D
            3D array of floats.
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, s3: Sampling,
                 f: Float3) -> None:
        """
        Constructs an image panel for specified sampling and abstract 3D array.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of 1st dimension (Z axis).
        s2 : Sampling
            sampling of 2nd dimension (Y axis).
        s3 : Sampling
            sampling of 3rd dimension (X axis).
        f : Float3
            abstract 3D array of floats.
        """

    def update(self) -> None:
        """
        Notifies this panel that values in the referenced 3D array have changed.
        """

    def getBoxConstraint(self) -> BoxConstraint:
        """
        Gets a box constraint for this panel. The constraint is consistent
        with the sampling of this image.
        Returns
        --------
        output : BoxConstraint
            the box constraint.
        """

    def setColorModel(self, colorModel: IndexColorModel) -> None:
        """
        Sets the index color model for this panel.
        The default color model is a black-to-white gray model.
        
        Parameters
        -----------
        colorModel : IndexColorModel
            the index color model.
        """

    def getColorModel(self) -> IndexColorModel:
        """
        Gets the index color model for this panel.
        Returns
        --------
        output : IndexColorModel
            the index color model.
        """

    def setClips(self, clipMin: double, clipMax: double) -> None:
        """
        Sets the clips for this panel. An image panel maps array values
        to bytes, which are then used as indices into a specified color
        model. This mapping from array values to byte indices is linear,
        and so depends on only these two clip values. The minimum clip
        value corresponds to byte index 0, and the maximum clip value
        corresponds to byte index 255. Array values outside of the range
        [clipMin,clipMax] are clipped to lie inside this range.
        
        Calling this method disables the computation of clips from percentiles.
        Any clip values computed or specified previously will be forgotten.
        
        Parameters
        -----------
        clipMin : double
            the sample value corresponding to color model index 0.
        clipMax : double
            the sample value corresponding to color model index 255.
        """

    def getClipMin(self) -> float:
        """
        Gets the minimum clip value.
        Returns
        --------
        output : float
            the minimum clip value.
        """

    def getClipMax(self) -> float:
        """
        Gets the maximum clip value.
        Returns
        --------
        output : float
            the maximum clip value.
        """

    def setPercentiles(self, percMin: double, percMax: double) -> None:
        """
        Sets the percentiles used to compute clips for this panel. The default
        percentiles are 0 and 100, which correspond to the minimum and maximum
        array values.
        
        Calling this method enables the computation of clips from percentiles.
        Any clip values specified or computed previously will be forgotten.
        
        Parameters
        -----------
        percMin : double
            the percentile corresponding to clipMin.
        percMax : double
            the percentile corresponding to clipMax.
        """

    def getPercentileMin(self) -> float:
        """
        Gets the minimum percentile.
        Returns
        --------
        output : float
            the minimum percentile.
        """

    def getPercentileMax(self) -> float:
        """
        Gets the maximum percentile.
        Returns
        --------
        output : float
            the maximum percentile.
        """

    def addColorMapListener(self, cml: ColorMapListener) -> None:
        """
        Adds the specified color map listener.
        
        Parameters
        -----------
        cml : ColorMapListener
            the listener.
        """

    def removeColorMapListener(self, cml: ColorMapListener) -> None:
        """
        Removes the specified color map listener.
        
        Parameters
        -----------
        cml : ColorMapListener
            the listener.
        """
