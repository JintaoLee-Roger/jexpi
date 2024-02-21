from typing import overload
from edu.mines.jtk.mapping import *


class GridView:
    """
    Grid lines that extend tics in tile axes into tiles. Grid lines can be
    painted above or below other tiled views in a tile, simply by adding
    a grid view before or after those other tiled views.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a grid view with default types, style, and color.
        """

    @overload
    def __init__(self, horizontal: Horizontal, vertical: Vertical) -> None:
        """
        Constructs a grid view with specified types.
        
        Parameters
        -----------
        horizontal : Horizontal
            the grid horizontal type.
        vertical : Vertical
            the grid vertical type.
        """

    @overload
    def __init__(self, style: Style) -> None:
        """
        Constructs a grid view with specified style.
        
        Parameters
        -----------
        style : Style
            the grid style.
        """

    @overload
    def __init__(self, color: Color) -> None:
        """
        Constructs a grid view with specified color.
        
        Parameters
        -----------
        color : Color
            the grid color.
        """

    @overload
    def __init__(self, horizontal: Horizontal, vertical: Vertical,
                 color: Color) -> None:
        """
        Constructs a grid view with specified types and color.
        
        Parameters
        -----------
        horizontal : Horizontal
            the grid horizontal type.
        vertical : Vertical
            the grid vertical type.
        color : Color
            the grid color.
        """

    @overload
    def __init__(self, horizontal: Horizontal, vertical: Vertical,
                 color: Color, style: Style) -> None:
        """
        Constructs a grid view with specified types, style, and color.
        
        Parameters
        -----------
        horizontal : Horizontal
            the grid horizontal type.
        vertical : Vertical
            the grid vertical type.
        color : Color
            the grid color.
        style : Style
            the grid style.
        """

    @overload
    def __init__(self, parameters: String) -> None:
        """
        Constructs a grid view with specified parameters string. See the method
        {@link #setParameters(String)} for the format of the parameters string.
        
        Parameters
        -----------
        parameters : String
            the color and style of grid lines.
        """

    def setHorizontal(self, horizontal: Horizontal) -> None:
        """
        Sets the grid horizontal type.
        The default grid horizontal type is major.
        
        Parameters
        -----------
        horizontal : Horizontal
            the grid horizontal type
        """

    def setVertical(self, vertical: Vertical) -> None:
        """
        Sets the grid vertical type.
        The default grid vertical type is major.
        
        Parameters
        -----------
        vertical : Vertical
            the grid vertical type
        """

    def setColor(self, color: Color) -> None:
        """
        Sets the grid color.
        The default grid color is the tile foreground color.
        That default is used if the specified color is null.
        
        Parameters
        -----------
        color : Color
            the color; null, for default color.
        """

    def setStyle(self, style: Style) -> None:
        """
        Sets the grid style.
        The default grid style is solid.
        
        Parameters
        -----------
        style : Style
            the style.
        """

    def setParameters(self, parameters: String) -> None:
        """
        Sets the grid types, color, and style parameters from a string.
        This method provides a convenient way to set the grid horizontal
        and vertical types, color, and style of grid lines for this view.
        
        To specify grid horizontal type, the parameters string may contain
        "H0" for grid horizontal type zero, or simply "H" for grid horizontal
        type major. Otherwise, the grid horizontal type is none.
        
        To specify grid vertical type, the parameters string may contain
        "V0" for grid vertical type zero, or simply "V" for grid vertical
        type major. Otherwise, the grid vertical type is none.
        
        To specify a grid color, the parameters string may contain one of "r"
        for red, "g" for green, "b" for blue, "c" for cyan, "m" for magenta,
        "y" for yellow, "k" for black, or "w" for white. If the parameter
        string contains none of these colors, then the default color is used.
        
        To specify a grid style, the parameters string may contain one of "-"
        for solid lines, "--" for dashed lines, "-." for dotted lines, or "--."
        for dash-dotted lines. If the parameters string contains none of these
        line styles, then no grid lines are painted.
        
        Parameters
        -----------
        parameters : String
            the grid parameters string.
        """

    def paint(self, g2d: Graphics2D) -> None:
        """
    
        """
