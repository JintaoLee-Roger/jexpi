from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class ImagePanelGroup2:
    """
    A group of image panels that displays two 3D arrays of floats.
    Specifically, an image panel group contains one or more axis-aligned
    frames, each containing two axis-aligned image panel children.
    
    The two sets of image panels are called "1st and 2nd image panels." The
    1st image panels are rendered (with polygon offset) slightly behind the
    2nd image panels.
    
    After constructing an image panel group, but before its image panels are
    drawn, one should set clips or percentiles. Otherwise, as each image panel
    is drawn for the first time, it will compute clip min and max values using
    default percentiles. Because all image panels in this group display the
    same array, much of this computation is redundant.
    """

    @overload
    def __init__(self, f1: Float3D, f2: Float3D) -> None:
        """
        Constructs an image panel group for all three axes.
        Assumes default unit sampling.
        Both 3D arrays of floats must have consistent dimensions.
        
        Parameters
        -----------
        f1 : Float3D
            1st 3D array of floats.
        f2 : Float3D
            2nd 3D array of floats.
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, s3: Sampling, f1: Float3D,
                 f2: Float3D) -> None:
        """
        Constructs an image panel group for all three axes.
        Both 3D arrays of floats much be consistent with the specified sampling.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of 1st dimension (Z axis).
        s2 : Sampling
            sampling of 2nd dimension (Y axis).
        s3 : Sampling
            sampling of 3rd dimension (X axis).
        f1 : Float3D
            1st 3D array of floats.
        f2 : Float3D
            2nd 3D array of floats.
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, s3: Sampling, f1: Float3,
                 f2: Float3) -> None:
        """
        Constructs an image panel group for all three axes.
        Both 3D arrays of floats much be consistent with the specified sampling.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of 1st dimension (Z axis).
        s2 : Sampling
            sampling of 2nd dimension (Y axis).
        s3 : Sampling
            sampling of 3rd dimension (X axis).
        f1 : Float3
            1st abstract 3D array of floats.
        f2 : Float3
            2nd abstract 3D array of floats.
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, s3: Sampling, f1: Float3D,
                 f2: Float3D, axes: Axis1D) -> None:
        """
        Constructs an image panel group for specified axes.
        Both 3D arrays of floats much be consistent with the specified sampling.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of 1st dimension (Z axis).
        s2 : Sampling
            sampling of 2nd dimension (Y axis).
        s3 : Sampling
            sampling of 3rd dimension (X axis).
        f1 : Float3D
            1st 3D array of floats.
        f2 : Float3D
            2nd 3D array of floats.
        axes : Axis[]
            array of axes, one for each image panel.
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, s3: Sampling, f1: Float3,
                 f2: Float3, axes: Axis1D) -> None:
        """
        Constructs an image panel group for specified axes.
        Both 3D arrays of floats much be consistent with the specified sampling.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of 1st dimension (Z axis).
        s2 : Sampling
            sampling of 2nd dimension (Y axis).
        s3 : Sampling
            sampling of 3rd dimension (X axis).
        f1 : Float3
            1st abstract 3D array of floats.
        f2 : Float3
            2nd abstract 3D array of floats.
        axes : Axis[]
            array of axes, one for each image panel.
        """

    def update1(self) -> None:
        """
        Notifies this panel that values in the 1st 3D array have changed.
        """

    def update2(self) -> None:
        """
        Notifies this panel that values in the 2nd 3D array have changed.
        """

    def getImagePanel1(self, axis: Axis) -> ImagePanel:
        """
        Gets a 1st image panel in this group with the specified axis.
        
        Parameters
        -----------
        axis : Axis
            the axis.
        
        Returns
        --------
        output : ImagePanel
            the image panel; null, if none has the axis specified.
        """

    def getImagePanel2(self, axis: Axis) -> ImagePanel:
        """
        Gets a 2nd image panel in this group with the specified axis.
        
        Parameters
        -----------
        axis : Axis
            the axis.
        
        Returns
        --------
        output : ImagePanel
            the image panel; null, if none has the axis specified.
        """

    def getImagePanels1(self) -> Iterator:
        """
        Gets an iterator for 1st image panels in this group.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def getImagePanels2(self) -> Iterator:
        """
        Gets an iterator for 2nd image panels in this group.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def setColorModel1(self, colorModel: IndexColorModel) -> None:
        """
        Sets the index color model for 1st image panels in this group.
        The default color model is a black-to-white gray model.
        
        Parameters
        -----------
        colorModel : IndexColorModel
            the index color model.
        """

    def setColorModel2(self, colorModel: IndexColorModel) -> None:
        """
        Sets the index color model for 2nd image panels in this group.
        The default color model is a jet model with alpha = 0.5.
        
        Parameters
        -----------
        colorModel : IndexColorModel
            the index color model.
        """

    def getColorModel1(self) -> IndexColorModel:
        """
        Gets the index color model for 1st image panels in this group.
        Returns
        --------
        output : IndexColorModel
            the index color model.
        """

    def getColorModel2(self) -> IndexColorModel:
        """
        Gets the index color model for 2nd image panels in this group.
        Returns
        --------
        output : IndexColorModel
            the index color model.
        """

    def setClips1(self, clipMin: double, clipMax: double) -> None:
        """
        Sets the clips for 1st image panels in this group. Image panels in
        this group map array values to bytes, which are then used as indices
        into a specified color model. This mapping from array values to byte
        indices is linear, and so depends on only these two clip values. The
        clip minimum value corresponds to byte index 0, and the clip maximum
        value corresponds to byte index 255. Sample values outside of the
        range [clipMin,clipMax] are clipped to lie inside this range.
        
        Calling this method disables the computation of clips from percentiles.
        Any clip values computed or specified previously will be forgotten.
        
        Parameters
        -----------
        clipMin : double
            the sample value corresponding to color model index 0.
        clipMax : double
            the sample value corresponding to color model index 255.
        """

    def setClips2(self, clipMin: double, clipMax: double) -> None:
        """
        Sets the clips for 2nd image panels in this group. Image panels in
        this group map array values to bytes, which are then used as indices
        into a specified color model. This mapping from array values to byte
        indices is linear, and so depends on only these two clip values. The
        clip minimum value corresponds to byte index 0, and the clip maximum
        value corresponds to byte index 255. Sample values outside of the
        range [clipMin,clipMax] are clipped to lie inside this range.
        
        Calling this method disables the computation of clips from percentiles.
        Any clip values computed or specified previously will be forgotten.
        
        Parameters
        -----------
        clipMin : double
            the sample value corresponding to color model index 0.
        clipMax : double
            the sample value corresponding to color model index 255.
        """

    def getClip1Min(self) -> float:
        """
        Gets the minimum clip value for 1st image panels.
        Returns
        --------
        output : float
            the minimum clip value.
        """

    def getClip2Min(self) -> float:
        """
        Gets the minimum clip value for 2nd image panels.
        Returns
        --------
        output : float
            the minimum clip value.
        """

    def getClip1Max(self) -> float:
        """
        Gets the maximum clip value for 1st image panels.
        Returns
        --------
        output : float
            the maximum clip value.
        """

    def getClip2Max(self) -> float:
        """
        Gets the maximum clip value for 2nd image panels.
        Returns
        --------
        output : float
            the maximum clip value.
        """

    def setPercentiles1(self, percMin: double, percMax: double) -> None:
        """
        Sets the percentiles used to compute clips for 1st image panels in
        this group. The default percentiles are 0 and 100, which correspond
        to the minimum and maximum array values.
        
        Calling this method enables the computation of clips from percentiles.
        Any clip values specified or computed previously will be forgotten.
        
        Parameters
        -----------
        percMin : double
            the percentile corresponding to clipMin.
        percMax : double
            the percentile corresponding to clipMax.
        """

    def setPercentiles2(self, percMin: double, percMax: double) -> None:
        """
        Sets the percentiles used to compute clips for 2nd image panels in
        this group. The default percentiles are 0 and 100, which correspond
        to the minimum and maximum array values.
        
        Calling this method enables the computation of clips from percentiles.
        Any clip values specified or computed previously will be forgotten.
        
        Parameters
        -----------
        percMin : double
            the percentile corresponding to clipMin.
        percMax : double
            the percentile corresponding to clipMax.
        """

    def getPercentile1Min(self) -> float:
        """
        Gets the minimum percentile for 1st image panels.
        Returns
        --------
        output : float
            the minimum percentile.
        """

    def getPercentile2Min(self) -> float:
        """
        Gets the minimum percentile for 2nd image panels.
        Returns
        --------
        output : float
            the minimum percentile.
        """

    def getPercentile1Max(self) -> float:
        """
        Gets the maximum percentile for 1st image panels.
        Returns
        --------
        output : float
            the maximum percentile.
        """

    def getPercentile2Max(self) -> float:
        """
        Gets the maximum percentile for 2nd image panels.
        Returns
        --------
        output : float
            the maximum percentile.
        """

    def addColorMap1Listener(self, cml: ColorMapListener) -> None:
        """
        Adds the specified color map listener for 1st image panels.
        
        Parameters
        -----------
        cml : ColorMapListener
            the listener.
        """

    def addColorMap2Listener(self, cml: ColorMapListener) -> None:
        """
        Adds the specified color map listener for 2nd image panels.
        
        Parameters
        -----------
        cml : ColorMapListener
            the listener.
        """

    def removeColorMap1Listener(self, cml: ColorMapListener) -> None:
        """
        Removes the specified color map listener.
        
        Parameters
        -----------
        cml : ColorMapListener
            the listener.
        """

    def removeColorMap2Listener(self, cml: ColorMapListener) -> None:
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
