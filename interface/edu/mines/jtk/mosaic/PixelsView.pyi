from typing import overload
from edu.mines.jtk.mapping import *


class PixelsView:
    """
    A view of sampled functions f(x1,x2), displayed as a 2-D array of pixels.
    Function values are converted to pixel colors in two steps. In the first
    step, these values are converted to unsigned bytes in the range [0,255].
    In the second step, those bytes are converted to pixel colors.
    
    The first step is a mapping from function values to unsigned byte values.
    This mapping is linear, except for clipping, which ensures that no byte
    value lies outside the range [0,255]. The linear mapping is defined by
    two clip values, clipMin and clipMax. The minimum clip value clipMin
    corresponds to byte value 0, and the maximum clip value clipMax
    corresponds to byte value 255. Sample values less than clipMin are
    mapped to 0; sample values greater than clipMax are mapped to 255.
    
    Byte values are computed for every pixel displayed by this view. Because
    the view typically contains more pixels than samples, this first mapping
    often requires interpolation between sampled values of functions f(x1,x2).
    Either linear or nearest-neighbor interpolation may be specified for this
    first step.
    
    The second step depends on the number (one, three, or four) of sampled
    functions specified. For one function, the byte values are indices for
    a table of 256 colors (a color map) in a specified index color model.
    See {@link edu.mines.jtk.awt.ColorMap} for more details.
    
    For three (or four) sampled functions, the byte values are interpreted
    directly as color components red, green, and blue (and alpha). In this
    case, any indexed color model specified is not used. The number of color
    components equals the number of sampled functions specified.
    """

    @overload
    def __init__(self, f: Float2D) -> None:
        """
        Constructs a pixels view of the specified sampled function f(x1,x2).
        Assumes zero first sample values and unit sampling intervals.
        Function values are converted to colors using an index color model.
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2).
        """

    @overload
    def __init__(self, f: Float3D) -> None:
        """
        Constructs a pixels view of the specified sampled functions f(x1,x2).
        Assumes zero first sample values and unit sampling intervals.
        Function values are converted to colors using a direct color model.
        where nc is the number (three or four) of color components.
        
        Parameters
        -----------
        f : Float3D
            array[nc][n2][n1] of sampled function values f(x1,x2),
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, f: Float2D) -> None:
        """
        Constructs a pixels view of the specified sampled function f(x1,x2).
        Function values are converted to colors using an index color model.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2).
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, f: Float3D) -> None:
        """
        Constructs a pixels view of the specified sampled functions f(x1,x2).
        Assumes zero first sample values and unit sampling intervals.
        Function values are converted to colors using a direct color model.
        where nc is the number (three or four) of color components.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float3D
            array[nc][n2][n1] of sampled function values f(x1,x2),
        """

    @overload
    def set(self, f: Float2D) -> None:
        """
        Sets the sampled function f(x1,x2) for this view.
        If compatible samplings for x1 and x2 have already been specified,
        then this method uses them. Otherwise, this method assumes zero
        first sample values and unit sampling intervals.
        Function values are converted to colors using an index color model.
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2).
        """

    @overload
    def set(self, f: Float3D) -> None:
        """
        Sets the sampled functions f(x1,x2) for this view.
        If compatible samplings for x1 and x2 have already been specified,
        then this method uses them. Otherwise, this method assumes zero
        first sample values and unit sampling intervals.
        Function values are converted to colors using a direct color model.
        where nc is the number (three or four) of color components.
        
        Parameters
        -----------
        f : Float3D
            array[nc][n2][n1] of sampled function values f(x1,x2),
        """

    @overload
    def set(self, s1: Sampling, s2: Sampling, f: Float2D) -> None:
        """
        Sets the sampled function f(x1,x2) for this view.
        Function values are converted to colors using an index color model.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2).
        """

    @overload
    def set(self, s1: Sampling, s2: Sampling, f: Float3D) -> None:
        """
        Sets the sampled functions f(x1,x2) for this view.
        Function values are converted to colors using a direct color model.
        where nc is the number (three or four) of color components.
        This number must equal that when this view was constructed.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float3D
            array[nc][n2][n1] of sampled function values f(x1,x2),
        """

    def setOrientation(self, orientation: Orientation) -> None:
        """
        Sets the orientation of sample axes.
        
        Parameters
        -----------
        orientation : Orientation
            the orientation.
        """

    def getOrientation(self) -> Orientation:
        """
        Gets the orientation of sample axes.
        Returns
        --------
        output : Orientation
            the orientation.
        """

    def setInterpolation(self, interpolation: Interpolation) -> None:
        """
        Sets the method for interpolation between samples.
        
        Parameters
        -----------
        interpolation : Interpolation
            the interpolation method.
        """

    def getInterpolation(self) -> Interpolation:
        """
        Gets the method for interpolation between samples.
        Returns
        --------
        output : Interpolation
            the interpolation method.
        """

    def setColorModel(self, colorModel: IndexColorModel) -> None:
        """
        Sets the index color model for this view. For three or four color
        components, a direct color model is used instead of this index color
        model. The default color model is a black-to-white gray model.
        
        Parameters
        -----------
        colorModel : IndexColorModel
            the index color model.
        """

    def getColorModel(self) -> IndexColorModel:
        """
        Gets the index color model for this view.
        used (for multiple color components) instead of an index color model.
        Returns
        --------
        output : IndexColorModel
            the index color model; null, if a direct color model is being
        """

    @overload
    def setClips(self, clipMin: float, clipMax: float) -> None:
        """
        Sets the clips for this view. A pixels view maps values of the sampled
        function f(x1,x2) to bytes, which are then used as indices into a
        specified color model. This mapping from sample values to byte indices
        is linear, and depends on only these two clip values. The minimum clip
        value corresponds to byte index 0, and the maximum clip value corresponds
        to byte index 255. Sample values outside of the range (clipMin,clipMax)
        are clipped to lie inside this range.
        
        Calling this method disables the computation of clips from percentiles.
        Any clip values computed or specified previously will be forgotten.
        
        If multiple color components, sets clips for all components.
        
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
        Gets the minimum clip value. If multiple color components, gets the
        minimum clip value for only the first color component.
        Returns
        --------
        output : float
            the minimum clip value.
        """

    @overload
    def getClipMax(self) -> float:
        """
        Gets the maximum clip value. If multiple color components, gets the
        maximum clip value for only the first color component.
        Returns
        --------
        output : float
            the maximum clip value.
        """

    @overload
    def setPercentiles(self, percMin: float, percMax: float) -> None:
        """
        Sets the percentiles used to compute clips for this view. The default
        percentiles are 0 and 100, which correspond to the minimum and maximum
        values of the sampled function f(x1,x2).
        
        Calling this method enables the computation of clips from percentiles.
        Any clip values specified or computed previously will be forgotten.
        
        If multiple color components, sets percentiles for all components.
        
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
        Gets the minimum percentile. If multiple color components, gets the
        minimum percentile for only the first color component.
        Returns
        --------
        output : float
            the minimum percentile.
        """

    @overload
    def getPercentileMax(self) -> float:
        """
        Gets the maximum percentile. If multiple color components, gets the
        maximum percentile for only the first color component.
        Returns
        --------
        output : float
            the maximum percentile.
        """

    @overload
    def setClips(self, ic: int, clipMin: float, clipMax: float) -> None:
        """
        Sets the clips for the specified color component.
        
        Parameters
        -----------
        ic : int
            the index (0, 1, 2, or 3) of the color component.
        clipMin : float
            the sample value corresponding to byte value 0.
        clipMax : float
            the sample value corresponding to byte value 255.
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

    def paint(self, g2d: Graphics2D) -> None:
        """
    
        """

    def getColorMap(self) -> ColorMap:
        """
    
        """
