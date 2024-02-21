from typing import overload
from edu.mines.jtk.mapping import *


class TiledView:
    """
    A tiled view in a tile. To paint something in a tile, classes extend
    and use the methods of this abstract base class.
    """

    def paint(self, g2d: Graphics2D) -> None:
        """
        Paints this tiled view. This method is implemented by classes that
        extend this abstract base class. Implementations may modify the
        specified graphics context freely. Such modifications will not affect
        the paintings of other tiled views in the same tile or mosaic.
        
        Tiled views should <em>not</em> replace (set) entirely the transform
        in the specified graphics context. This transform may already have
        been set by the tile or its mosaic. Therefore, tiled views should
        modify this transform only by specifying <em>additional</em> scaling,
        translation, etc.
        
        Parameters
        -----------
        g2d : Graphics2D
            the graphics context in which to paint.
        """

    def getTile(self) -> Tile:
        """
        Gets the tile that contains this tiled view.
        Returns
        --------
        output : Tile
            the tile; null, if none.
        """

    def getHorizontalProjector(self) -> Projector:
        """
        Gets the horizontal projector of this tiled view.
        The returned horizontal projector is a reference to that for the tile
        that contains this tiled view or null, if this tiled view is not in a
        tile.
        Returns
        --------
        output : Projector
            the horizontal projector; null, if none.
        """

    def getVerticalProjector(self) -> Projector:
        """
        Gets the vertical projector of this tiled view.
        The returned vertical projector is a reference to that for the tile
        that contains this tiled view or null, if this tiled view is not in
        a tile.
        Returns
        --------
        output : Projector
            the vertical projector; null, if none.
        """

    def getTranscaler(self) -> Transcaler:
        """
        Gets the transcaler of this tiled view.
        The returned transcaler is a reference to that for the tile that
        contains this tiled view or null, if this tiled view is not in a
        tile.
        Returns
        --------
        output : Transcaler
            the transcaler; null, if none.
        """

    def getHScale(self) -> AxisScale:
        """
        Gets the scale of the best horizontal projector.
        Returns
        --------
        output : AxisScale
            the scale of the best horizontal projector.
        """

    def getVScale(self) -> AxisScale:
        """
        Gets the scale of the best vertical projector.
        Returns
        --------
        output : AxisScale
            the scale of the best horizontal projector.
        """

    @overload
    def setScales(self, hscale: AxisScale, vscale: AxisScale) -> TiledView:
        """
        Sets the scale both best projectors.
        The method must be overridden by a subclass
        to implement non-linear scaling.
        
        Parameters
        -----------
        hscale : AxisScale
            the new horizontal scale
        vscale : AxisScale
            the new vertical scale
        
        Returns
        --------
        output : TiledView
            null, unless overriden by subclass to return this TiledView
        """

    @overload
    def setScales(self, scale: AxisScale) -> TiledView:
        """
        Convenience method to set both scales the same
        
        Parameters
        -----------
        scale : AxisScale
            the new scale
        
        Returns
        --------
        output : TiledView
            this TiledView
        """

    def setHScale(self, scale: AxisScale) -> TiledView:
        """
        Convenience method to set the scale of the
        best horizontal projector.
        
        Parameters
        -----------
        scale : AxisScale
            the new scale
        
        Returns
        --------
        output : TiledView
            this TiledView
        """

    def setVScale(self, scale: AxisScale) -> TiledView:
        """
        Convenience method to set the scale of the
        best vertical projector.
        
        Parameters
        -----------
        scale : AxisScale
            the new scale
        
        Returns
        --------
        output : TiledView
            this TiledView
        """
