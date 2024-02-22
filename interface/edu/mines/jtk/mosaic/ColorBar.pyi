from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class ColorBar:
    """
    A color bar is a view of a color map, a mapping from values to colors.
    A color bar listens for changes to a colormap, and updates itself
    accordingly.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a new color bar with no label.
        """

    @overload
    def __init__(self, label: String) -> None:
        """
        Constructs a new color bar with specified label.
        
        Parameters
        -----------
        label : String
            the label; null, if none.
        """

    def setLabel(self, label: String) -> None:
        """
        Sets the label for this color bar.
        
        Parameters
        -----------
        label : String
            the label; null, if none.
        """

    def setWidthMinimum(self, widthMinimum: int) -> None:
        """
    
        """

    def setFormat(self, format: String) -> None:
        """
        Sets the format for major tic annotation for this color bar.
        The default format is "%1.4G", which yields a minimum of 1 digit,
        with up to 4 digits of precision. Any trailing zeros and decimal
        point are removed from tic annotation.
        
        Parameters
        -----------
        format : String
            the format.
        """

    def setInterval(self, interval: double) -> None:
        """
        Sets the major labeled tic interval in the axis for this color bar.
        
        Parameters
        -----------
        interval : double
            the major labeled tic interval.
        """

    def getTile(self) -> Tile:
        """
        Gets the tile used to display this color bar.
        Returns
        --------
        output : Tile
            the tile.
        """

    def colorMapChanged(self, cm: ColorMap) -> None:
        """
    
        """

    def paintToRect(self, g2d: Graphics2D, x: int, y: int, w: int,
                    h: int) -> None:
        """
    
        """

    def setFont(self, font: Font) -> None:
        """
    
        """

    def setForeground(self, color: Color) -> None:
        """
    
        """

    def setBackground(self, color: Color) -> None:
        """
    
        """
