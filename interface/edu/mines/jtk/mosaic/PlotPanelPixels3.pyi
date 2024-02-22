from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class PlotPanelPixels3:
    """
    A plot panel with three pixels views of slices from a 3-D array.
    
    Pixels views are arranged in one of four ways, depending on the
    orientation of this panel. All arrangements are L-shaped with an
    empty tile in the upper-right corner of a 2x2 mosaic contained in
    this panel.
    
    This class has numerous methods that enable changing various attributes
    of the three pixels views while keeping them consistent. Although such
    attributes can be set independently for each pixels view, one should
    use the methods in this class when possible.
    """

    @overload
    def __init__(self, orientation: Orientation, axesPlacement: AxesPlacement,
                 s1: Sampling, s2: Sampling, s3: Sampling, f: Float3D) -> None:
        """
        Constructs a plot panel with three pixels views.
        
        Parameters
        -----------
        orientation : Orientation
            the orientation of views.
        axesPlacement : AxesPlacement
            the placement of axes.
        s1 : Sampling
            sampling of the 1st dimension.
        s2 : Sampling
            sampling of the 2nd dimension.
        s3 : Sampling
            sampling of the 3rd dimension.
        f : Float3D
            3-D array of floats.
        """

    @overload
    def __init__(self, orientation: Orientation, axesPlacement: AxesPlacement,
                 s1: Sampling, s2: Sampling, s3: Sampling, f: Float4D) -> None:
        """
        Constructs a plot panel with three pixels views.
        
        Parameters
        -----------
        orientation : Orientation
            the orientation of views.
        axesPlacement : AxesPlacement
            the placement of axes.
        s1 : Sampling
            sampling of the 1st dimension.
        s2 : Sampling
            sampling of the 2nd dimension.
        s3 : Sampling
            sampling of the 3rd dimension.
        f : Float4D
            array of 3-D arrays of floats.
        """

    @overload
    def __init__(self, orientation: Orientation, axesPlacement: AxesPlacement,
                 s1: Sampling, s2: Sampling, s3: Sampling, f3: Float3) -> None:
        """
        Constructs a plot panel with three pixels views.
        
        Parameters
        -----------
        orientation : Orientation
            the orientation of views.
        axesPlacement : AxesPlacement
            the placement of axes.
        s1 : Sampling
            sampling of the 1st dimension.
        s2 : Sampling
            sampling of the 2nd dimension.
        s3 : Sampling
            sampling of the 3rd dimension.
        f3 : Float3
            abstract 3-D array of floats.
        """

    @overload
    def __init__(self, orientation: Orientation, axesPlacement: AxesPlacement,
                 s1: Sampling, s2: Sampling, s3: Sampling,
                 f3: Float31D) -> None:
        """
        Constructs a plot panel with three pixels views.
        
        Parameters
        -----------
        orientation : Orientation
            the orientation of views.
        axesPlacement : AxesPlacement
            the placement of axes.
        s1 : Sampling
            sampling of the 1st dimension.
        s2 : Sampling
            sampling of the 2nd dimension.
        s3 : Sampling
            sampling of the 3rd dimension.
        f3 : Float3[]
            array of abstract 3-D array of floats, one for each component.
        """

    def getPixelsView12(self) -> PixelsView:
        """
        Gets the pixels view for the 1-2 slice.
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    def getPixelsView13(self) -> PixelsView:
        """
        Gets the pixels view for the 1-3 slice.
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    def getPixelsView23(self) -> PixelsView:
        """
        Gets the pixels view for the 2-3 slice.
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    def setSlice23(self, k1: int) -> None:
        """
        Sets sample index for 2-3 slice of 1st dimension.
        
        Parameters
        -----------
        k1 : int
            sample index for 1st dimension.
        """

    def setSlice13(self, k2: int) -> None:
        """
        Sets sample index for slice of 2nd dimension.
        
        Parameters
        -----------
        k2 : int
            sample index for 2nd dimension.
        """

    def setSlice12(self, k3: int) -> None:
        """
        Sets sample index for slice of 3rd dimension.
        
        Parameters
        -----------
        k3 : int
            sample index for 3rd dimension.
        """

    def setSlices(self, k1: int, k2: int, k3: int) -> None:
        """
        Sets sample indices for all slices.
        
        Parameters
        -----------
        k1 : int
            sample index for 1st dimension.
        k2 : int
            sample index for 2nd dimension.
        k3 : int
            sample index for 3rd dimension.
        """

    def setInterpolation(self, interpolation: PixelsView) -> None:
        """
        Sets the method for interpolation between samples.
        
        Parameters
        -----------
        interpolation : PixelsView
            the interpolation method.
        """

    def setLineColor(self, color: Color) -> None:
        """
        Sets the color of lines drawn to indicate slice locations.
        
        Parameters
        -----------
        color : Color
            the line color; if null, no lines are drawn.
        """

    def setLabel1(self, label: String) -> None:
        """
        Sets the label for axis 1.
        
        Parameters
        -----------
        label : String
            the label.
        """

    def setLabel2(self, label: String) -> None:
        """
        Sets the label for axis 2.
        
        Parameters
        -----------
        label : String
            the label.
        """

    def setLabel3(self, label: String) -> None:
        """
        Sets the label for axis 3.
        
        Parameters
        -----------
        label : String
            the label.
        """

    def setFormat1(self, format: String) -> None:
        """
        Sets the format for axis 1.
        
        Parameters
        -----------
        format : String
            the format.
        """

    def setFormat2(self, format: String) -> None:
        """
        Sets the format for axis 2.
        
        Parameters
        -----------
        format : String
            the format.
        """

    def setFormat3(self, format: String) -> None:
        """
        Sets the format for axis 3.
        
        Parameters
        -----------
        format : String
            the format.
        """

    def setInterval1(self, interval: double) -> None:
        """
        Sets the interval for axis 1.
        
        Parameters
        -----------
        interval : double
            the interval.
        """

    def setInterval2(self, interval: double) -> None:
        """
        Sets the interval for axis 2.
        
        Parameters
        -----------
        interval : double
            the interval.
        """

    def setInterval3(self, interval: double) -> None:
        """
        Sets the interval for axis 3.
        
        Parameters
        -----------
        interval : double
            the interval.
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
        used (for multiple color components) instead of an index color model.
        Returns
        --------
        output : IndexColorModel
            the index color model; null, if a direct color model is being
        """

    @overload
    def setClips(self, clipMin: float, clipMax: float) -> None:
        """
        Sets the clips for this panel.
        Calling this method disables the computation of clips from percentiles.
        Any clip values computed or specified previously will be forgotten.
        
        Parameters
        -----------
        clipMin : float
            the sample value corresponding to color model index 0.
        clipMax : float
            the sample value corresponding to color model index 255.
        """

    @overload
    def getClipMin(self) -> float:
        """
        Gets the minimum clip value.
        Returns
        --------
        output : float
            the minimum clip value.
        """

    @overload
    def getClipMax(self) -> float:
        """
        Gets the maximum clip value.
        Returns
        --------
        output : float
            the maximum clip value.
        """

    @overload
    def setPercentiles(self, percMin: float, percMax: float) -> None:
        """
        Sets the percentiles used to compute clips for this panel.
        Calling this method enables the computation of clips from percentiles.
        Any clip values specified or computed previously will be forgotten.
        
        Parameters
        -----------
        percMin : float
            the percentile corresponding to clipMin.
        percMax : float
            the percentile corresponding to clipMax.
        """

    @overload
    def getPercentileMin(self) -> float:
        """
        Gets the minimum percentile.
        Returns
        --------
        output : float
            the minimum percentile.
        """

    @overload
    def getPercentileMax(self) -> float:
        """
        Gets the maximum percentile.
        Returns
        --------
        output : float
            the maximum percentile.
        """

    @overload
    def setClips(self, ic: int, clipMin: float, clipMax: float) -> None:
        """
        Sets the clips for the specified color component.
        Calling this method disables the computation of clips from percentiles.
        Any clip values computed or specified previously will be forgotten.
        
        Parameters
        -----------
        ic : int
            the index (0, 1, 2, or 3) of the color component.
        clipMin : float
            the sample value corresponding to color byte value 0.
        clipMax : float
            the sample value corresponding to color byte value 255.
        """

    @overload
    def getClipMin(self, ic: int) -> float:
        """
        Gets the minimum clip value for the specified color component.
        
        Parameters
        -----------
        ic : int
            the index (0, 1, 2, or 3) of the color component.
        
        Returns
        --------
        output : float
            the minimum clip value.
        """

    @overload
    def getClipMax(self, ic: int) -> float:
        """
        Gets the maximum clip value for the specified color component.
        
        Parameters
        -----------
        ic : int
            the index (0, 1, 2, or 3) of the color component.
        
        Returns
        --------
        output : float
            the maximum clip value.
        """

    @overload
    def setPercentiles(self, ic: int, percMin: float, percMax: float) -> None:
        """
        Sets the percentiles for the specified color component.
        Calling this method enables the computation of clips from percentiles.
        Any clip values specified or computed previously will be forgotten.
        
        Parameters
        -----------
        ic : int
            the index (0, 1, 2, or 3) of the color component.
        percMin : float
            the percentile corresponding to clipMin.
        percMax : float
            the percentile corresponding to clipMax.
        """

    @overload
    def getPercentileMin(self, ic: int) -> float:
        """
        Gets the minimum percentile for the specified color component.
        
        Parameters
        -----------
        ic : int
            the index (0, 1, 2, or 3) of the color component.
        
        Returns
        --------
        output : float
            the minimum percentile.
        """

    @overload
    def getPercentileMax(self, ic: int) -> float:
        """
        Gets the maximum percentile for the specified color component.
        
        Parameters
        -----------
        ic : int
            the index (0, 1, 2, or 3) of the color component.
        
        Returns
        --------
        output : float
            the maximum percentile.
        """
