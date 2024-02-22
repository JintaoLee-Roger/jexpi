from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class Tile:
    """
    A tile in a mosaic contains a list of tiled views. A tile coordinates
    changes to its tiled views and its view rectangle with other tiles
    in its mosaic.
    
    Each tile has a horizontal projector and a vertical projector. These
    map world coordinates to and from normalized coordinates. The mosaic
    aligns its tiles such that all tiles in the same column share the same
    horizontal projector, and all tiles in the same row share the same
    vertical projector.
    
    A tile's view rectangle represents a subset of a unit square; i.e., the
    view rectangle is in normalized coordinates. Setting the view rectangle
    of a tile causes the view rectangle to be set accordingly in all tiles
    in the same column and row of the mosaic. To zoom or scroll a tile,
    change its view rectangle.
    
    A tile's transcaler maps normalized coordinates to and from device
    coordinates. When unzoomed (by default), the tile's transcaler maps
    normalized coordinates (0.0,0.0) to device coordinates (0,0) and
    normalized coordinates (1.0,1.0) to device coordinates (width-1,height-1),
    where width and height represent the size of the tile. The transcaler
    changes when either its size or its view rectangle is changed.
    """

    def __init__(self, mosaic: Mosaic, irow: int, icol: int) -> None:
        """
    
        """

    def getMosaic(self) -> Mosaic:
        """
        Gets the mosaic that contains this tile.
        Returns
        --------
        output : Mosaic
            the mosaic.
        """

    def getRowIndex(self) -> int:
        """
        Gets the row index of this tile.
        Returns
        --------
        output : int
            the row index.
        """

    def getColumnIndex(self) -> int:
        """
        Gets the column index of this tile.
        Returns
        --------
        output : int
            the column index.
        """

    def setLimits(self, hmin: double, vmin: double, hmax: double,
                  vmax: double) -> None:
        """
        Sets limits for the both horizontal and vertical axes.
        By default, limits are computed automatically by tiled graphical views.
        This method can be used to override those default limits.
        
        Parameters
        -----------
        hmin : double
            the minimum value.
        vmin : double
            the minimum value.
        hmax : double
            the maximum value.
        vmax : double
            the maximum value.
        """

    def setHLimits(self, hmin: double, hmax: double) -> None:
        """
        Sets limits for the horizontal axis.
        By default, limits are computed automatically by tiled graphical views.
        This method can be used to override those default limits.
        
        Parameters
        -----------
        hmin : double
            the minimum value.
        hmax : double
            the maximum value.
        """

    def setVLimits(self, vmin: double, vmax: double) -> None:
        """
        Sets limits for the vertical axis.
        By default, limits are computed automatically by tiled graphical views.
        This method can be used to override those default limits.
        
        Parameters
        -----------
        vmin : double
            the minimum value.
        vmax : double
            the maximum value.
        """

    def setLimitsDefault(self) -> None:
        """
        Sets default limits for horizontal and vertical axes. This method may
        be used to restore default limits after they have been set explicitly.
        """

    def setHLimitsDefault(self) -> None:
        """
        Sets default limits for the horizontal axis. This method may be used
        to restore default limits after they have been set explicitly.
        """

    def setVLimitsDefault(self) -> None:
        """
        Sets default limits for the vertical axis. This method may be used
        to restore default limits after they have been set explicitly.
        """

    def setBestHorizontalProjector(self, bhp: Projector) -> None:
        """
        Sets the best horizontal projector for this tile. If null, this
        tile will compute its best horizontal projector by merging those
        of its tiled views. If not null, the specified projector is best.
        In either case, this tile's horizontal projector may be adjusted by
        it's mosaic during alignment with other tiles in the same column.
        
        Parameters
        -----------
        bhp : Projector
            the best horizontal projector.
        """

    def setBestVerticalProjector(self, bvp: Projector) -> None:
        """
        Sets the best vertical projector for this tile. If null, this
        tile will compute its best vertical projector by merging those
        of its tiled views. If not null, the specified projector is best.
        In either case, this tile's vertical projector may be adjusted by
        it's mosaic during alignment with other tiles in the same row.
        
        Parameters
        -----------
        bvp : Projector
            the best vertical projector.
        """

    def getHorizontalProjector(self) -> Projector:
        """
        Gets the horizontal projector for this tile.
        Returns
        --------
        output : Projector
            the horizontal projector.
        """

    def getVerticalProjector(self) -> Projector:
        """
        Gets the vertical projector for this tile.
        Returns
        --------
        output : Projector
            the vertical projector.
        """

    def getTranscaler(self) -> Transcaler:
        """
        Gets the transcaler for this tile.
        Returns
        --------
        output : Transcaler
            the transcaler.
        """

    def pixelToWorldHorizontal(self, x: int) -> double:
        """
        Transforms a pixel x coordinate to a horizontal world coordinate.
        
        Parameters
        -----------
        x : int
            the pixel x coordinate.
        
        Returns
        --------
        output : double
            the horizontal world coordinate.
        """

    def pixelToWorldVertical(self, y: int) -> double:
        """
        Transforms a pixel y coordinate to a vertical world coordinate.
        
        Parameters
        -----------
        y : int
            the pixel y coordinate.
        
        Returns
        --------
        output : double
            the vertical world coordinate.
        """

    def addTiledView(self, tv: TiledView) -> bool:
        """
        Adds the specified tiled view to this tile. If the tiled view is
        already in this tile, it is first removed, before adding it again.
        tiled view; false, otherwise.
        
        Parameters
        -----------
        tv : TiledView
            the tiled view.
        
        Returns
        --------
        output : bool
            true, if this tile did not already contain the specified
        """

    def removeTiledView(self, tv: TiledView) -> bool:
        """
        Removes the specified tiled view from this tile. If the tiled view
        is not in this tile, this method does nothing.
        false, otherwise.
        
        Parameters
        -----------
        tv : TiledView
            the tiled view.
        
        Returns
        --------
        output : bool
            true, if this tile contained the specified tiled view;
        """

    def countTiledViews(self) -> int:
        """
        Returns the number of tiled views in this this.
        Returns
        --------
        output : int
            the number of tiled views.
        """

    def getTiledView(self, index: int) -> TiledView:
        """
        Gets the tiled view with specified index.
        
        Parameters
        -----------
        index : int
            the index.
        
        Returns
        --------
        output : TiledView
            the tiled view.
        """

    def getTiledViews(self) -> Iterator:
        """
        Gets an iterator for the tiled views in this tile.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def getViewRectangle(self) -> DRectangle:
        """
        Gets the view rectangle for this tile. The view rectangle represents
        the subset of normalized coordinate space that is displayed in this
        tile.
        Returns
        --------
        output : DRectangle
            the view rectangle.
        """

    def setViewRectangle(self, vr: DRectangle) -> None:
        """
        Sets the view rectangle for this tile. The view rectangle represents
        the subset of normalized coordinate space that is displayed in this
        tile. Setting the view rectangle may zoom or scroll this tile.
        
        Parameters
        -----------
        vr : DRectangle
            the view rectangle.
        """

    def setBounds(self, x: int, y: int, width: int, height: int) -> None:
        """
    
        """

    def getTileAxisTop(self) -> TileAxis:
        """
        Gets the top tile axis for this tile.
        Returns
        --------
        output : TileAxis
            the axis; null, if none.
        """

    def getTileAxisLeft(self) -> TileAxis:
        """
        Gets the left tile axis for this tile.
        Returns
        --------
        output : TileAxis
            the axis; null, if none.
        """

    def getTileAxisBottom(self) -> TileAxis:
        """
        Gets the bottom tile axis for this tile.
        Returns
        --------
        output : TileAxis
            the axis; null, if none.
        """

    def getTileAxisRight(self) -> TileAxis:
        """
        Gets the right tile axis for this tile.
        Returns
        --------
        output : TileAxis
            the axis; null, if none.
        """

    def getHScale(self) -> AxisScale:
        """
        Gets the Horizontal axis scaling.
        Returns
        --------
        output : AxisScale
            the Scale; null, if none.
        """

    def getVScale(self) -> AxisScale:
        """
        Gets the Vertical axis scaling.
        Returns
        --------
        output : AxisScale
            the Scale; null, if none.
        """

    def paintToRect(self, g2d: Graphics2D, x: int, y: int, w: int,
                    h: int) -> None:
        """
    
        """
