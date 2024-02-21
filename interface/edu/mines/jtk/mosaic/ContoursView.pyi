from typing import overload
from edu.mines.jtk.mapping import *


class ContoursView:
    """
    A view of a sampled function f(x1,x2), displayed with contour lines.
    """

    @overload
    def __init__(self, f: Float2D) -> None:
        """
        Constructs a contours view of the specified sampled function f(x1,x2).
        Assumes zero first sample values and unit sampling intervals.
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, f: Float2D) -> None:
        """
        Constructs a contours view of the specified sampled function f(x1,x2).
        n1 and n2 denote the number of samples in s1 and s2, respectively.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
        """

    @overload
    def set(self, f: Float2D) -> None:
        """
        Sets the sampled function f(x1,x2) for this view.
        Assumes zero first sample values and unit sampling intervals.
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
        """

    @overload
    def set(self, s1: Sampling, s2: Sampling, f: Float2D) -> None:
        """
        Sets the sampled function f(x1,x2) for this view.
        n1 and n2 denote the number of samples in s1 and s2, respectively.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
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

    def setLineStyle(self, style: Line) -> None:
        """
        Sets the contour line style.
        The default style is solid.
        
        Parameters
        -----------
        style : Line
            the line style.
        """

    def setLineStyleNegative(self, style: Line) -> None:
        """
        Sets the contour line style for negative-valued contours.
        By default, all contours share the same line style.
        
        Parameters
        -----------
        style : Line
            the line style.
        """

    def setLineWidth(self, width: float) -> None:
        """
        Sets the contour line width.
        The default width is zero, for the thinnest lines.
        
        Parameters
        -----------
        width : float
            the line width.
        """

    def setLineColor(self, color: Color) -> None:
        """
        Sets the color of each contour line to the specified color.
        
        Parameters
        -----------
        color : Color
            the contour line color.
        """

    def setColorModel(self, colorModel: IndexColorModel) -> None:
        """
        Sets the color model used to map contour values to colors.
        If set, then byte 0 of the color model corresponds to the minimum
        clip value, and byte 255 corresponds to the maximum clip value.
        If not set, then all contour lines have the same color.
        
        Parameters
        -----------
        colorModel : IndexColorModel
            the color model.
        """

    def getColorMap(self) -> ColorMap:
        """
    
        """

    def setReadableContours(self, readableContours: bool) -> None:
        """
        Enables or disables automatically computed readable contour values.
        Here, readable values are multiples of 1, 2, and 5 times some
        power of ten. If enabled, then any specified number of contours
        serves as an upper bound on the number of contour values.
        Readable contour values are the default.
        
        Parameters
        -----------
        readableContours : bool
            true, for readable contours; false, otherwise.
        """

    @overload
    def setContours(self, n: int) -> None:
        """
        Sets the number of contour values.
        If readable contours are enabled, then this number is an upper bound,
        and the actual number of contours may be less than this number.
        Otherwise, if readable contours are disabled, then contour values
        will be evenly spaced between, but not including, the minimum and
        maximum clip values. The default number of contour values is 25.
        
        Parameters
        -----------
        n : int
            the number of contour values.
        """

    @overload
    def setContours(self, c: Float1D) -> None:
        """
        Sets the contour values to those in the specified array.
        If this method is called, then clips (or percentiles) are not used
        to determine contour values, and readable contours are disabled.
        
        Parameters
        -----------
        c : Float1D
            the array of contour values.
        """

    @overload
    def setContours(self, cs: Sampling) -> None:
        """
        Sets the contour values to the specified sampling.
        If this method is called, then clips (or percentiles) are not used
        to determine contour values, and readable contours are disabled.
        
        Parameters
        -----------
        cs : Sampling
            the contour sampling.
        """

    def getContours(self) -> Float1D:
        """
        Gets the contour values.
        Returns
        --------
        output : Float1D
            array of contour values.
        """

    def setClips(self, clipMin: float, clipMax: float) -> None:
        """
        Sets the clips for this view. These values limit the range used
        to determine contour values. Function values f(x1,x2) less than
        clipMin and greater than clipMax are ignored.
        
        Calling this method disables the computation of clips from percentiles.
        Previous clip values will be forgotten.
        
        Parameters
        -----------
        clipMin : float
            the lower bound on contour values.
        clipMax : float
            the upper bound on contour values.
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

    def setPercentiles(self, percMin: float, percMax: float) -> None:
        """
        Sets the percentiles used to compute clips for this view. The default
        percentiles are 0 and 100, which correspond to the minimum and maximum
        values of the sampled function f(x1,x2).
        
        Calling this method enables the computation of clips from percentiles.
        Any clip values specified or computed previously will be forgotten.
        
        Parameters
        -----------
        percMin : float
            the percentile corresponding to clipMin.
        percMax : float
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

    def paint(self, g2d: Graphics2D) -> None:
        """
    
        """
