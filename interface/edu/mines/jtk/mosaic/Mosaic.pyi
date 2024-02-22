from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class Mosaic:
    """
    A mosaic of tiles and tile axes. A mosaic lays out its tiles in a matrix,
    with a specified number of rows and columns. It manages the world and
    normalized coordinate systems of those tiles, so that tiles zoom and
    scroll consistently.
    
    For example, when the the view rectangle (in normalized coordinates)
    of a tile is set, perhaps while zooming or scrolling, then that tile's
    mosaic changes the view rectangles of any other tiles in the same row
    or column accordingly, so that they all zoom and scroll together.
    
    A mosaic can also manage axes at the top, left, bottom, and/or right
    sides of its matrix of tiles. These axes annotate the adjacent tiles,
    and mosaic ensures that they too zoom and scroll consistent with any
    changes to the view rectangles of those tiles.
    
    A mosaic also manages a horizontal scrollbar for each column and a
    vertical scrollbar for each row. The mosaic shows scrollbars for only
    those dimensions of view rectangles that are zoomed. In other words,
    scrollbars are visible and consume space only when they are needed.
    """

    def __init__(self, nrow: int, ncol: int, axesPlacement: Set) -> None:
        """
        Constructs a mosaic with the specified number of rows and columns.
        
        Parameters
        -----------
        nrow : int
            the number of rows.
        ncol : int
            the number of columns.
        axesPlacement : Set
            the placement of axes.
        """

    def setModeManager(self, modeManager: ModeManager) -> None:
        """
        Sets the mode manager for this mosaic. By default, a mosaic
        constructs a unique mode manager when it is constructed. This
        default may be overridden, for example, when two or more mosaics
        must share modes.
        
        Parameters
        -----------
        modeManager : ModeManager
            the mode manager.
        """

    def countRows(self) -> int:
        """
        Returns the number of rows of tiles in this mosaic.
        Returns
        --------
        output : int
            the number of rows.
        """

    def countColumns(self) -> int:
        """
        Returns the number of columns of tiles in this mosaic.
        Returns
        --------
        output : int
            the number of columns.
        """

    def getTile(self, irow: int, icol: int) -> Tile:
        """
        Gets the tile with specified row and column indices.
        
        Parameters
        -----------
        irow : int
            the row index.
        icol : int
            the column index.
        
        Returns
        --------
        output : Tile
            the tile.
        """

    def getTileAxisTop(self, icol: int) -> TileAxis:
        """
        Gets the top tile axis with specified column index.
        
        Parameters
        -----------
        icol : int
            the column index.
        
        Returns
        --------
        output : TileAxis
            the axis; null, if none.
        """

    def getTileAxisLeft(self, irow: int) -> TileAxis:
        """
        Gets the left tile axis with specified row index.
        
        Parameters
        -----------
        irow : int
            the row index.
        
        Returns
        --------
        output : TileAxis
            the axis; null, if none.
        """

    def getTileAxisBottom(self, icol: int) -> TileAxis:
        """
        Gets the bottom tile axis with specified column index.
        
        Parameters
        -----------
        icol : int
            the column index.
        
        Returns
        --------
        output : TileAxis
            the axis; null, if none.
        """

    def getTileAxisRight(self, irow: int) -> TileAxis:
        """
        Gets the right tile axis with specified row index.
        
        Parameters
        -----------
        irow : int
            the row index.
        
        Returns
        --------
        output : TileAxis
            the axis; null, if none.
        """

    def setWidthMinimum(self, icol: int, widthMinimum: int) -> None:
        """
        Sets the width minimum for the specified column. All tiles in the
        specified column will have width not less than the specified minimum.
        Width minimums are used to compute the preferred width of this mosaic.
        The default width minimum is 100.
        
        Parameters
        -----------
        icol : int
            the column index.
        widthMinimum : int
            the width minimum.
        """

    def setWidthElastic(self, icol: int, widthElastic: int) -> None:
        """
        Sets the width elastic for the specified column. If extra width is
        available in this mosaic, it is allocated to the specified column
        of tiles in proportion to the specified width elastic.
        For fixed-width columns, the width elastic should be zero.
        The default width elastic is 100.
        
        Parameters
        -----------
        icol : int
            the column index.
        widthElastic : int
            the width elastic.
        """

    def setHeightMinimum(self, irow: int, heightMinimum: int) -> None:
        """
        Sets the height minimum for the specified row. All tiles in the
        specified row will have height not less than the specified minimum.
        Height minimums are used to compute the preferred height of this mosaic.
        The default height minimum is 100.
        
        Parameters
        -----------
        irow : int
            the row index.
        heightMinimum : int
            the height minimum.
        """

    def setHeightElastic(self, irow: int, heightElastic: int) -> None:
        """
        Sets the height elastic for the specified row. If extra height is
        available in this mosaic, it is allocated to the specified row
        of tiles in proportion to the specified height elastic.
        For fixed-height rows, the height elastic should be zero.
        The default height elastic is 100.
        
        Parameters
        -----------
        irow : int
            the row index.
        heightElastic : int
            the height elastic.
        """

    def setWidthTileSpacing(self, wts: int) -> None:
        """
        Sets the width in pixels of spacing between adjacent tiles.
        
        Parameters
        -----------
        wts : int
            the width of the inter-tile spacing.
        """

    def getModeManager(self) -> ModeManager:
        """
        Gets the mode manager for this mosaic.
        Returns
        --------
        output : ModeManager
            the mode manager.
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

    def getMinimumSize(self) -> Dimension:
        """
    
        """

    def getPreferredSize(self) -> Dimension:
        """
    
        """

    def doLayout(self) -> None:
        """
    
        """

    def paintToRect(self, g2d: Graphics2D, x: int, y: int, w: int,
                    h: int) -> None:
        """
    
        """
