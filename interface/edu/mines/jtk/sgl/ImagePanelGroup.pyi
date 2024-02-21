from typing import overload
from edu.mines.jtk.mapping import *


class ImagePanelGroup:
    """
    A group of image panels that display a single 3D array.
    Specifically, an image panel group contains one or more axis-aligned
    frames, each containing one axis-aligned image panel child.
    
    After constructing an image panel group, but before its image panels are
    drawn, one should set clips or percentiles. Otherwise, as each image panel
    is drawn for the first time, it will compute clip min and max values using
    default percentiles. Because all image panels in this group display the
    same array, much of this computation is redundant.
    """

    @overload
    def __init__(self, f: Float3D) -> None:
        """
        Constructs an image panel group for all three axes.
        Assumes default unit sampling.
        
        Parameters
        -----------
        f : Float3D
            3D array of floats.
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, s3: Sampling,
                 f: Float3D) -> None:
        """
        Constructs an image panel group for all three axes.
        
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
        Constructs an image panel group for all three axes.
        
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

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, s3: Sampling, f: Float3D,
                 axes: Axis1D) -> None:
        """
        Constructs image panel group for specified axes.
        
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
        axes : Axis[]
            array of axes, one for each image panel.
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, s3: Sampling, f: Float3,
                 axes: Axis1D) -> None:
        """
        Constructs image panel group for specified axes.
        
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
        axes : Axis[]
            array of axes, one for each image panel.
        """

    def getImagePanel(self, axis: Axis) -> ImagePanel:
        """
        Gets an image panel in this group with the specified axis.
        
        Parameters
        -----------
        axis : Axis
            the axis.
        
        Returns
        --------
        output : ImagePanel
            the image panel; null, if none has the axis specified.
        """

    def getImagePanels(self) -> Iterator:
        """
        Gets an iterator for the image panels in this group.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def setColorModel(self, colorModel: IndexColorModel) -> None:
        """
        Sets the index color model for this group.
        The default color model is a black-to-white gray model.
        
        Parameters
        -----------
        colorModel : IndexColorModel
            the index color model.
        """

    def getColorModel(self) -> IndexColorModel:
        """
        Gets the index color model for this group.
        Returns
        --------
        output : IndexColorModel
            the index color model.
        """

    def setClips(self, clipMin: double, clipMax: double) -> None:
        """
        Sets the clips for this group. Image panels in this group map array
        values to bytes, which are then used as indices into a specified color
        model. This mapping from array values to byte indices is linear, and
        so depends on only these two clip values. The clip minimum value
        corresponds to byte index 0, and the clip maximum value corresponds to
        byte index 255. Sample values outside of the range [clipMin,clipMax]
        are clipped to lie inside this range.
        
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
        Sets the percentiles used to compute clips for this group. The default
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

    def setSlices(self, k1: int, k2: int, k3: int) -> None:
        """
        Sets indices of image slices displayed in this group.
        
        Parameters
        -----------
        k1 : int
            index in 1st dimension (Z axis).
        k2 : int
            index in 2nd dimension (Y axis).
        k3 : int
            index in 3rd dimension (X axis).
        """
