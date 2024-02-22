from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class TileAxis:
    """
    A tile axis in a mosaic. Tile axes may be placed along the top, left,
    bottom, and right sides of the mosaic of tiles. Each horizontal (top or
    bottom) axis annotates the tiles in its column, and each vertical (left
    or right) axis annotates the tiles in its row.
    
    Axis tics, tic annotations, and the (optional) axis label are painted
    using the tile axis font and foreground colors.
    """

    def __init__(self, mosaic: Mosaic, placement: Placement,
                 index: int) -> None:
        """
    
        """

    def getMosaic(self) -> Mosaic:
        """
        Gets the mosaic that contains this axis.
        Returns
        --------
        output : Mosaic
            the mosaic.
        """

    def getIndex(self) -> int:
        """
        Gets the row or column index for this axis.
        Returns
        --------
        output : int
            the row or column index.
        """

    def getPlacement(self) -> Placement:
        """
        Gets the placement of this axis.
        Returns
        --------
        output : Placement
            the placement.
        """

    def getTile(self) -> Tile:
        """
        Gets the tile adjacent to this axis.
        Returns
        --------
        output : Tile
            the tile.
        """

    def isTop(self) -> bool:
        """
        Determines whether this axis is placed at top of mosaic.
        Returns
        --------
        output : bool
            true, if at top; false, otherwise.
        """

    def isLeft(self) -> bool:
        """
        Determines whether this axis is placed at left of mosaic.
        Returns
        --------
        output : bool
            true, if at left; false, otherwise.
        """

    def isBottom(self) -> bool:
        """
        Determines whether this axis is placed at bottom of mosaic.
        Returns
        --------
        output : bool
            true, if at bottom; false, otherwise.
        """

    def isRight(self) -> bool:
        """
        Determines whether this axis is placed at right of mosaic.
        Returns
        --------
        output : bool
            true, if at right; false, otherwise.
        """

    def isHorizontal(self) -> bool:
        """
        Determines whether this axis is placed at top or bottom of mosaic.
        An axis placed at the top or bottom is a horizontal axis.
        Returns
        --------
        output : bool
            true, if horizontal (at top or bottom); false, otherwise.
        """

    def isVertical(self) -> bool:
        """
        Determines whether this axis is placed at left or right of mosaic.
        An axis placed at the left or right is a vertical axis.
        Returns
        --------
        output : bool
            true, if vertical (at left or right); false, otherwise.
        """

    def isVerticalRotated(self) -> bool:
        """
        Determines whether this axis is placed at left or right of mosaic, and
        is rotated to read normal to the vertical axis.
        Returns
        --------
        output : bool
            true, if vertical and rotated; false, otherwise.
        """

    def setInterval(self, interval: double) -> None:
        """
        Sets the interval between major labeled tics for this axis.
        The default tic interval is zero, in which case a readable tic
        interval is computed automatically. This default is especially
        useful when interactively zooming and scrolling.
        
        Parameters
        -----------
        interval : double
            the major labeled tic interval.
        """

    def setLabel(self, label: String) -> None:
        """
        Sets the label for this axis.
        
        Parameters
        -----------
        label : String
            the label.
        """

    def setFormat(self, format: String) -> None:
        """
        Sets the format for major tic annotation for this axis.
        The default format is "%1.4G", which yields a minimum of 1 digit,
        with up to 4 digits of precision. Any trailing zeros and decimal
        point are removed from tic annotation.
        
        Parameters
        -----------
        format : String
            the format.
        """

    def setFont(self, font: Font) -> None:
        """
    
        """

    def setBounds(self, x: int, y: int, width: int, height: int) -> None:
        """
    
        """

    def setVerticalAxisRotated(self, rotated: bool) -> None:
        """
        Sets the rotation of tic labels in the vertical axis.
        Tic labels for a rotated vertical axis are rotated 90 degrees
        counter-clockwise.
        
        Parameters
        -----------
        rotated : bool
            true if rotated; false, otherwise.
        """

    def getAxisTics(self) -> AxisTics:
        """
        Gets the axis tics painted by this tile axis.
        Returns
        --------
        output : AxisTics
            the axis tics.
        """

    def paintToRect(self, g2d: Graphics2D, x: int, y: int, w: int,
                    h: int) -> None:
        """
    
        """
