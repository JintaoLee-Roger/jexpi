from typing import overload
from java.awt import *
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *
from edu.mines.jtk.dsp import *


class BarsView:
    """
    A view of bars.
    Bars may be specified as arrays of x2 values. Each array of x2 corresponds
    to one plot segment. Multiple plot segments may be specified by arrays of
    arrays of x1 and x2 coordinates.
    
    For example, to view sampled functions x2 = f(x1) and x2 = g(x1),
    one might construct two plot segments by specifying an array of two
    arrays of x1 coordinates and a corresponding array of two arrays of
    x2 coordinates.
    
    Note that some attributes remain constant across all plot segments,
    including: bar width, bar stacking, line style, bar alignment, and
    axis orientation.
    """

    @overload
    def __init__(self, x2: Float1D) -> None:
        """
        Constructs a view of bars with specified x2 quantities.
        The corresponding coordinates x1 are assumed to be 0, 1, 2, ....
        
        Parameters
        -----------
        x2 : Float1D
            array of x2 coordinates.
        """

    @overload
    def __init__(self, s1: Sampling, x2: Float1D) -> None:
        """
        Constructs a view of bars for a sampled function x2(x1).
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of x1 coordinates.
        x2 : Float1D
            array of x2 values.
        """

    @overload
    def __init__(self, x2: Float2D) -> None:
        """
        Constructs a view of bars for x2.length data sets.
        
        Parameters
        -----------
        x2 : Float2D
            array of values containing x2.length separate sets.
        """

    @overload
    def __init__(self, s1: Sampling, x2: Float2D) -> None:
        """
        Constructs a view of bars with multiple plot segments.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of x1 coordinates.
        x2 : Float2D
            array of x2 values, containing x2.length plot segments.
        """

    @overload
    def __init__(self, x1: Float2D, x2: Float2D) -> None:
        """
        Constructs a view of bars with multiple plot segments.
        
        Parameters
        -----------
        x1 : Float2D
            array of x1 coordinates.
        x2 : Float2D
            array of x2 coordinates.
        """

    @overload
    def __init__(self, x1: Float1D, x2: Float1D) -> None:
        """
        Constructs a view of bars with a single plot segment.
        The lengths of the specified arrays x1 and x2 must be equal.
        
        Parameters
        -----------
        x1 : Float1D
            array of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        """

    @overload
    def set(self, s1: Sampling, x2: Float1D) -> None:
        """
        Sets (x1,x2) coordinates for a sampled function x2(x1).
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        """

    @overload
    def set(self, x1: Float1D, x2: Float1D) -> None:
        """
        Sets array of (x1,x2) coordinates for a plot segment.
        The lengths of x1 and x2 must be equal.
        
        Parameters
        -----------
        x1 : Float1D
            array of x1 values.
        x2 : Float1D
            array of x2 coordinates.
        """

    @overload
    def set(self, x1: Float2D, x2: Float2D) -> None:
        """
        Sets array of arrays of (x1,x2) coordinates for multiple plot segments.
        The lengths of the specified arrays x1 and x2 must be equal.
        
        Parameters
        -----------
        x1 : Float2D
            array of arrays of x1 values.
        x2 : Float2D
            array of arrays of x2 coordinates.
        """

    def setOrientation(self, orientation: Orientation) -> None:
        """
        Sets the orientation of (x1,x2) axes.
        
        Parameters
        -----------
        orientation : Orientation
            the orientation.
        """

    def getOrientation(self) -> Orientation:
        """
        Gets the orientation of (x1,x2) axes.
        Returns
        --------
        output : Orientation
            the orientation.
        """

    def setStyle(self, style: String) -> None:
        """
        Sets the color, line style, and mark style from a style string.
        This method provides a convenient way to set the most commonly
        specified attributes of lines and marks painted by this view.
        
        To specify a color, the style string may contain one of "r" for red,
        "g" for green, "b" for blue, "c" for cyan, "m" for magenta, "y" for
        yellow, "k" for black, or "w" for white. If the style string contains
        none of these colors, then the default color is used.
        
        To specify a line style, the style string may contain one of "-" for
        solid lines, "--" for dashed lines, "-." for dotted lines, or "--."
        for dash-dotted lines. If the style string contains none of these
        line styles, then no lines are painted.
        
        To specify a mark style, the style string may contain one of "." for
        point, "+" for plus, "x" for cross, "o" for hollow circle", "O" for
        filled circle, "s" for hollow square, or "S" for filled square. If
        the style string contains none of these mark styles, then no marks
        are painted.
        
        Parameters
        -----------
        style : String
            the style string.
        """

    def setBarWidth(self, width: float) -> None:
        """
        Sets the bar width.
        The default width will be 1, or fully expanded bars.
        
        Parameters
        -----------
        width : float
            the bar width in range [0.0 - 1.0]
        """

    @overload
    def setFillColor(self, color: Color) -> None:
        """
        Sets the fill color for all bar sets.
        The default fill color is the tile background color.
        
        Parameters
        -----------
        color : Color
            the bar color.
        """

    @overload
    def setColorModel(self, colorModel: IndexColorModel) -> None:
        """
        Sets a color model for all bar sets.
        
        Parameters
        -----------
        colorModel : IndexColorModel
            a color model.
        """

    @overload
    def setColorModel(self, i: int, colorModel: IndexColorModel) -> None:
        """
        Sets a color model for a specific bar set.
        
        Parameters
        -----------
        i : int
            index of a bar set.
        colorModel : IndexColorModel
            a color model.
        """

    @overload
    def setColorMap(self, colorMap: ColorMap) -> None:
        """
        Sets a color map for all bar sets.
        
        Parameters
        -----------
        colorMap : ColorMap
            a color map.
        """

    @overload
    def setColorMap(self, i: int, colorMap: ColorMap) -> None:
        """
        Sets a color map for a specific bar set.
        
        Parameters
        -----------
        i : int
            index of a bar set.
        colorMap : ColorMap
            a color map.
        """

    @overload
    def setFillColor(self, i: int, color: Color) -> None:
        """
        Sets the fill color for a set of bars.
        The default fill color is the tile background color.
        
        Parameters
        -----------
        i : int
            the index of a bar set.
        color : Color
            the bar color.
        """

    def setAlignment(self, alignment: Alignment) -> None:
        """
        Sets the alignment of the bars.
        The default alignment is centered about the value's tick mark.
        
        Parameters
        -----------
        alignment : Alignment
            the bar alignment.
        """

    def setStackBars(self, stack: bool) -> None:
        """
        Sets the stacking behavior of the bars.
        The default stacking behavior is to plot multiple bars adjacent.
        
        Parameters
        -----------
        stack : bool
            true, if stacking bars; false, otherwise.
        """

    def setLineStyle(self, style: Line) -> None:
        """
        Sets the line style.
        The default style is solid.
        
        Parameters
        -----------
        style : Line
            the line style.
        """

    def setLineWidth(self, width: float) -> None:
        """
        Sets the line width.
        The default width is zero, for the thinnest lines.
        
        Parameters
        -----------
        width : float
            the line width.
        """

    @overload
    def setLineColor(self, color: Color) -> None:
        """
        Sets the line color for all sets of bars.
        The default line color is the tile foreground color.
        That default is used if the specified line color is null.
        
        Parameters
        -----------
        color : Color
            the line color; null, for tile foreground color.
        """

    @overload
    def setLineColor(self, ibar: int, color: Color) -> None:
        """
        Sets the line color for a set of bars.
        The default line color is the tile foreground color.
        That default is used if the specified line color is null.
        
        Parameters
        -----------
        ibar : int
            the index of the set of bars.
        color : Color
            the line color; null, for tile foreground color.
        """

    def setTextFormat(self, format: String) -> None:
        """
        Sets the format used for text labels.
        The default format is "%1.4G".
        
        Parameters
        -----------
        format : String
            the text format.
        """

    def paint(self, g2d: Graphics2D) -> None:
        """
    
        """
