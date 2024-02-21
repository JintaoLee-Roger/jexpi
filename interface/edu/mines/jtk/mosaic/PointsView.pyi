from typing import overload
from edu.mines.jtk.mapping import *


class PointsView:
    """
    A view of points (x1,x2) with marks at points and/or lines between them.
    Points (x1,x2) may be specified as arrays x1 and x2 of coordinates. Each
    pair of arrays x1 and x2 corresponds to one plot segment. Multiple plot
    segments may be specified by arrays of arrays of x1 and x2 coordinates.
    
    For each point (x1,x2), a mark with a specified style, size, and color
    may be painted. Between each consecutive pair of points (x1,x2) within
    a plot segment, lines with specified style, width, and color may be
    painted.
    
    For example, to view sampled functions x2 = sin(x1) and x2 = cos(x1),
    one might construct two plot segments by specifying an array of two
    arrays of x1 coordinates and a corresponding array of two arrays of
    x2 coordinates.
    
    Note that mark and line attributes are constant for each points view.
    These attributes do not vary among plot segments. To paint marks and
    lines with different attributes, construct multiple views.
    """

    @overload
    def __init__(self, x2: Float1D) -> None:
        """
        Constructs a view of points (x1,x2) with specified x2 coordinates.
        The corresponding coordinates x1 are assumed to be 0, 1, 2, ....
        
        Parameters
        -----------
        x2 : Float1D
            array of x2 coordinates.
        """

    @overload
    def __init__(self, s1: Sampling, x2: Float1D) -> None:
        """
        Constructs a view of points (x1,x2) for a sampled function x2(x1).
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        """

    @overload
    def __init__(self, x1: Float1D, x2: Float1D) -> None:
        """
        Constructs a view of points (x1,x2) with a single plot segment.
        The lengths of the specified arrays x1 and x2 must be equal.
        
        Parameters
        -----------
        x1 : Float1D
            array of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        """

    @overload
    def __init__(self, x1: Float2D, x2: Float2D) -> None:
        """
        Constructs a view of points (x1,x2) with multiple plot segments.
        The lengths of the specified arrays x1 and x2 must be equal.
        
        Parameters
        -----------
        x1 : Float2D
            array of arrays of x1 coordinates.
        x2 : Float2D
            array of arrays of x2 coordinates.
        """

    @overload
    def __init__(self, x1: Float1D, x2: Float1D, x3: Float1D) -> None:
        """
        Constructs a view of points (x1,x2,x3) with a single plot segment.
        The lengths of the specified arrays x1 and x2 must be equal.
        If x3 is not null, its length must equal that of x1 and x2.
        
        Parameters
        -----------
        x1 : Float1D
            array of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        x3 : Float1D
            array of x3 coordinates; null, if none.
        """

    @overload
    def __init__(self, x1: Float2D, x2: Float2D, x3: Float2D) -> None:
        """
        Constructs a view of points (x1,x2,x3) with multiple plot segments.
        The lengths of the specified arrays x1 and x2 must be equal.
        If x3 is not null, its length must equal that of x1 and x2.
        
        Parameters
        -----------
        x1 : Float2D
            array of arrays of x1 coordinates.
        x2 : Float2D
            array of arrays of x2 coordinates.
        x3 : Float2D
            array of arrays of x3 coordinates.
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
        Sets arrays of (x1,x2) coordinates for a single plot segment.
        The lengths of the specified arrays x1 and x2 must be equal.
        
        Parameters
        -----------
        x1 : Float1D
            array of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        """

    @overload
    def set(self, x1: Float1D, x2: Float1D, x3: Float1D) -> None:
        """
        Sets arrays of (x1,x2,x3) coordinates for a single plot segment.
        The lengths of the specified arrays x1 and x2 must be equal.
        If x3 is not null, its length must equal that of x1 and x2.
        
        Parameters
        -----------
        x1 : Float1D
            array of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        x3 : Float1D
            array of x3 coordinates; null, if none.
        """

    @overload
    def set(self, x1: Float2D, x2: Float2D) -> None:
        """
        Sets array of arrays of (x1,x2) coordinates for multiple plot segments.
        The lengths of the specified arrays x1 and x2 must be equal.
        
        Parameters
        -----------
        x1 : Float2D
            array of arrays of x1 coordinates.
        x2 : Float2D
            array of arrays of x2 coordinates.
        """

    @overload
    def set(self, x1: Float2D, x2: Float2D, x3: Float2D) -> None:
        """
        Sets array of arrays of (x1,x2,x3) coordinates for multiple plot segments.
        The lengths of the specified arrays x1 and x2 must be equal.
        If x3 is not null, its length must equal that of x1 and x2.
        
        Parameters
        -----------
        x1 : Float2D
            array of arrays of x1 coordinates.
        x2 : Float2D
            array of arrays of x2 coordinates.
        x3 : Float2D
            array of arrays of x3 coordinates; null, if none.
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

    def setLineColor(self, color: Color) -> None:
        """
        Sets the line color.
        The default line color is the tile foreground color.
        That default is used if the specified line color is null.
        
        Parameters
        -----------
        color : Color
            the line color; null, for tile foreground color.
        """

    def setMarkStyle(self, style: Mark) -> None:
        """
        Sets the mark style.
        The default mark style is none, for no marks.
        
        Parameters
        -----------
        style : Mark
            the mark style.
        """

    def setMarkSize(self, size: float) -> None:
        """
        Sets the mark size.
        The default mark size is half the tile font size.
        The default is used if the specified mark size is zero.
        
        Parameters
        -----------
        size : float
            the mark size.
        """

    def setMarkColor(self, color: Color) -> None:
        """
        Sets the mark color.
        The default mark color is the tile foreground color.
        That default is used if the specified mark color is null.
        
        Parameters
        -----------
        color : Color
            the mark color.
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

    def setScales(self, hscale: AxisScale, vscale: AxisScale) -> PointsView:
        """
        Sets the horizontal axis scaling.
        
        Parameters
        -----------
        hscale : AxisScale
            horizontal axis scaling.
        vscale : AxisScale
            vertical axis scaling.
        """

    def paint(self, g2d: Graphics2D) -> None:
        """
    
        """
