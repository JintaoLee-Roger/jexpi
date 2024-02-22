from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class PlotPanel:
    """
    A plot panel is a panel that contains a mosaic of 2-D graphical views.
    A plot panel may also contain a color bar and/or title. The plot panel's
    mosaic may contain any number or rows and columns of tiles. Each tile
    may contain any number of tiled graphical views.
    
    The primary purpose of this class is ease-of-use. A plot panel handles
    much of the work of constructing a mosaic of tiled graphical views.
    
    One consequence of ease-of-use is that some of the methods provided
    by this class are redundant. For example, some methods have (irow,icol)
    parameters that specify the row and column indices of a tile. These
    parameters are useful for mosaics with more than one tile. However, the
    most common case is a mosaic with only one tile; and, for this case, a
    corresponding method without (irow,icol) parameters is provided as well.
    The latter method simply calls the former with (irow,icol) = (0,0).
    
    An important property of a plot panel is the orientation of its axes.
    Tiles have axes x1 and x2. By default, the x1 axis increases toward
    the right and the x2 axis increases toward the top of each tile in a
    mosaic. In this default X1RIGHT_X2UP orientation, the coordinates
    (x1,x2) correspond to conventional (x,y) coordinates. An alternative
    orientation is X1DOWN_X2RIGHT, which is useful when the x1 axis
    corresponds to, say, a depth coordinate z.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a new plot panel with a mosaic of one tile.
        Uses the default orientation X1RIGHT_X2UP.
        """

    @overload
    def __init__(self, nrow: int, ncol: int) -> None:
        """
        Constructs a new plot panel with a mosaic of nrow by ncol tiles.
        Uses the default orientation X1RIGHT_X2UP.
        
        Parameters
        -----------
        nrow : int
            the number of rows.
        ncol : int
            the number of columns.
        """

    @overload
    def __init__(self, orientation: Orientation) -> None:
        """
        Constructs a new plot panel with a mosaic of one tile.
        
        Parameters
        -----------
        orientation : Orientation
            the plot orientation.
        """

    @overload
    def __init__(self, nrow: int, ncol: int, orientation: Orientation) -> None:
        """
    
        """

    @overload
    def __init__(self, nrow: int, ncol: int, orientation: Orientation,
                 axesPlacement: AxesPlacement) -> None:
        """
        Constructs a new plot panel with a mosaic of nrow by ncol tiles.
        
        Parameters
        -----------
        nrow : int
            the number of rows.
        ncol : int
            the number of columns.
        orientation : Orientation
            the plot orientation.
        axesPlacement : AxesPlacement
            the placement of axes.
        """

    def getMosaic(self) -> Mosaic:
        """
        Gets the mosaic. The mosaic contains one or more tiles.
        Returns
        --------
        output : Mosaic
            the mosaic.
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

    @overload
    def addColorBar(self) -> ColorBar:
        """
        Adds the color bar with no label. The color bar paints the color map
        of the most recently added pixels view. To avoid confusion, a color
        bar should perhaps not be added when this plot panel contains multiple
        pixels views with different color maps..
        Returns
        --------
        output : ColorBar
            the color bar.
        """

    @overload
    def addColorBar(self, label: String) -> ColorBar:
        """
        Adds the color bar with specified label.
        
        Parameters
        -----------
        label : String
            the label; null, if none.
        
        Returns
        --------
        output : ColorBar
            the color bar.
        """

    @overload
    def addColorBar(self, cm: ColorMapped) -> ColorBar:
        """
        Adds a color bar with a specified color mapped object and no label.
        
        Parameters
        -----------
        cm : ColorMapped
            the specified color mapped.
        
        Returns
        --------
        output : ColorBar
            the color bar.
        """

    @overload
    def addColorBar(self, cm: ColorMapped, label: String) -> ColorBar:
        """
        Adds a color bar with a specified color mapped object and label.
        If the specified color mapped object is null, then this plot panel
        will try to find the best color map to display in the color bar.
        
        Parameters
        -----------
        cm : ColorMapped
            the color mapped object.
        label : String
            the label.
        
        Returns
        --------
        output : ColorBar
            the color bar.
        """

    def setColorBarWidthMinimum(self, widthMinimum: int) -> None:
        """
        Sets a minimum width (in pixels) for a color bar.
        This method is useful when attempting to construct multiple plot
        panels with the same layout. In this scenario, set this minimum
        equal to the width of the widest color bar. Then all color bars
        will have the same width. Those widths might otherwise vary as tic
        and axes labels vary for the different panels.
        
        Parameters
        -----------
        widthMinimum : int
            the minimum width.
        """

    def setColorBarFormat(self, format: String) -> None:
        """
        Sets the format for major tic annotation of the color bar.
        The default format is "%1.4G", which yields a minimum of 1 digit,
        with up to 4 digits of precision. Any trailing zeros and decimal
        point are removed from tic annotation.
        
        Parameters
        -----------
        format : String
            the format.
        """

    def removeColorBar(self) -> None:
        """
        Removes the color bar.
        """

    def addTitle(self, title: String) -> None:
        """
        Adds the plot title. Equivalent to {@link #setTitle(String)}.
        The title font is 1.5 times larger than the font of this panel.
        
        Parameters
        -----------
        title : String
            the title; null, if none.
        """

    def setTitle(self, title: String) -> None:
        """
        Sets the plot title. Equivalent to {@link #addTitle(String)}.
        
        Parameters
        -----------
        title : String
            the title; null, for no title.
        """

    def removeTitle(self) -> None:
        """
        Removes the plot title. Equivalent to calling the method
        {@link #setTitle(String)} with a null title.
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

    @overload
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

    @overload
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

    @overload
    def setHLimits(self, icol: int, hmin: double, hmax: double) -> None:
        """
        Sets limits for the horizontal axis in the specified column.
        By default, limits are computed automatically by tiled graphical views.
        This method can be used to override those default limits.
        
        Parameters
        -----------
        icol : int
            the column index.
        hmin : double
            the minimum value.
        hmax : double
            the maximum value.
        """

    @overload
    def setVLimits(self, irow: int, vmin: double, vmax: double) -> None:
        """
        Sets limits for the vertical axis in the specified row.
        By default, limits are computed automatically by tiled graphical views.
        This method can be used to override those default limits.
        
        Parameters
        -----------
        irow : int
            the row index.
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

    @overload
    def setHLimitsDefault(self) -> None:
        """
        Sets default limits for the horizontal axis. This method may be used
        to restore default limits after they have been set explicitly.
        """

    @overload
    def setVLimitsDefault(self) -> None:
        """
        Sets default limits for the vertical axis. This method may be used
        to restore default limits after they have been set explicitly.
        """

    @overload
    def setHLimitsDefault(self, icol: int) -> None:
        """
        Sets default limits for the horizontal axis in the specified column.
        This method may be used to restore default limits after they have
        been set explicitly.
        
        Parameters
        -----------
        icol : int
            the column index.
        """

    @overload
    def setVLimitsDefault(self, irow: int) -> None:
        """
        Sets default limits for the vertical axis in the specified column.
        This method may be used to restore default limits after they have
        been set explicitly.
        
        Parameters
        -----------
        irow : int
            the row index.
        """

    @overload
    def setHLabel(self, label: String) -> None:
        """
        Sets the label for the horizontal axis.
        
        Parameters
        -----------
        label : String
            the label.
        """

    @overload
    def setVLabel(self, label: String) -> None:
        """
        Sets the label for the vertical axis.
        
        Parameters
        -----------
        label : String
            the label.
        """

    @overload
    def setHLabel(self, icol: int, label: String) -> None:
        """
        Sets the label for the horizontal axis in the specified column.
        
        Parameters
        -----------
        icol : int
            the column index.
        label : String
            the label.
        """

    @overload
    def setVLabel(self, irow: int, label: String) -> None:
        """
        Sets the label for the vertical axis in the specified row.
        
        Parameters
        -----------
        irow : int
            the row index.
        label : String
            the label.
        """

    @overload
    def setHFormat(self, format: String) -> None:
        """
        Sets the format for the horizontal axis.
        
        Parameters
        -----------
        format : String
            the format.
        """

    @overload
    def setVFormat(self, format: String) -> None:
        """
        Sets the format for the vertical axis.
        
        Parameters
        -----------
        format : String
            the format.
        """

    @overload
    def setHFormat(self, icol: int, format: String) -> None:
        """
        Sets the format for the horizontal axis in the specified column.
        
        Parameters
        -----------
        icol : int
            the column index.
        format : String
            the format.
        """

    @overload
    def setVFormat(self, irow: int, format: String) -> None:
        """
        Sets the format for the vertical axis in the specified row.
        
        Parameters
        -----------
        irow : int
            the row index.
        format : String
            the format.
        """

    def setVRotated(self, irow: int, rotated: bool) -> None:
        """
        Sets tic label rotation for the vertical axis in the specifie row.
        If true, tic labels in the vertical axis are rotated 90 degrees
        counter-clockwise. The default is false, not rotated.
        
        Parameters
        -----------
        irow : int
            the row index.
        rotated : bool
            true, if rotated; false, otherwise.
        """

    @overload
    def setHInterval(self, interval: double) -> None:
        """
        Sets the tic interval for the horizontal axis.
        
        Parameters
        -----------
        interval : double
            the major labeled tic interval.
        """

    @overload
    def setVInterval(self, interval: double) -> None:
        """
        Sets the tic interval for the vertical axis.
        
        Parameters
        -----------
        interval : double
            the major labeled tic interval.
        """

    @overload
    def setHInterval(self, icol: int, interval: double) -> None:
        """
        Sets the tic interval for the horizontal axis in the specified column.
        
        Parameters
        -----------
        icol : int
            the column index.
        interval : double
            the major labeled tic interval.
        """

    @overload
    def setVInterval(self, irow: int, interval: double) -> None:
        """
        Sets the tic interval for the vertical axis in the specified column.
        
        Parameters
        -----------
        irow : int
            the row index.
        interval : double
            the major labeled tic interval.
        """

    @overload
    def addGrid(self) -> GridView:
        """
        Adds a grid view.
        Returns
        --------
        output : GridView
            the grid view.
        """

    @overload
    def addGrid(self, parameters: String) -> GridView:
        """
        Adds a grid view with specified parameters string.
        For the format of the parameters string, see
        {@link edu.mines.jtk.mosaic.GridView#setParameters(String)}.
        
        Parameters
        -----------
        parameters : String
            the parameters string.
        
        Returns
        --------
        output : GridView
            the grid view.
        """

    @overload
    def addGrid(self, irow: int, icol: int) -> GridView:
        """
        Adds a grid view.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        
        Returns
        --------
        output : GridView
            the grid view.
        """

    @overload
    def addGrid(self, irow: int, icol: int, parameters: String) -> GridView:
        """
        Adds a grid view with specified parameters string.
        For the format of the parameters string, see
        {@link edu.mines.jtk.mosaic.GridView#setParameters(String)}.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        parameters : String
            the parameters string.
        
        Returns
        --------
        output : GridView
            the grid view.
        """

    @overload
    def addBars(self, x2: Float1D) -> BarsView:
        """
        Adds a bars view of the array x2.
        
        Parameters
        -----------
        x2 : Float1D
            array of x2 values.
        
        Returns
        --------
        output : BarsView
            the bars view.
        """

    @overload
    def addBars(self, s1: Sampling, x2: Float1D) -> BarsView:
        """
        Adds a view of bars (x1,x2) for a sampled function x2(x1).
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        x2 : Float1D
            array of x2 coordinates.
        
        Returns
        --------
        output : BarsView
            the bars view.
        """

    @overload
    def addBars(self, x2: Float2D) -> BarsView:
        """
        Adds a view of bars of the array x2 containing x2.length plot segments.
        
        Parameters
        -----------
        x2 : Float2D
            array of array of x2 values.
        
        Returns
        --------
        output : BarsView
            the bars view.
        """

    @overload
    def addBars(self, s1: Sampling, x2: Float2D) -> BarsView:
        """
        Adds a view of bars (x1,x2) for a sampled function x2(x1) and x2.length
        plot segments.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        x2 : Float2D
            array of array of x2 values.
        
        Returns
        --------
        output : BarsView
            a bars view.
        """

    @overload
    def addBars(self, irow: int, icol: int, s1: Sampling,
                x2: Float1D) -> BarsView:
        """
        Adds a view of bars x2 for a sampled function x2(x1).
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        x2 : Float1D
            array of x2 values.
        
        Returns
        --------
        output : BarsView
            the bars view.
        """

    @overload
    def addBars(self, irow: int, icol: int, x2: Float1D) -> BarsView:
        """
        Adds a bars view of the array x2 of bar values.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        x2 : Float1D
            array of x2 values.
        
        Returns
        --------
        output : BarsView
            the bars view.
        """

    @overload
    def addBars(self, irow: int, icol: int, x2: Float2D) -> BarsView:
        """
        Adds a bars view of the array of arrays x2 of bar values and x2.length
        plot segments.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        x2 : Float2D
            array of arrays of x2 values.
        
        Returns
        --------
        output : BarsView
            the bars view.
        """

    @overload
    def addBars(self, irow: int, icol: int, s1: Sampling,
                x2: Float2D) -> BarsView:
        """
        Adds a bars view of the array of arrays x2 of bar values and x2.length
        plot segments for a sample function x2(x1).
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        x2 : Float2D
            array of array of x2 values.
        
        Returns
        --------
        output : BarsView
            the bars view.
        """

    @overload
    def addPixels(self, f: Float2D) -> PixelsView:
        """
        Adds a pixels view of the specified sampled function f(x1,x2).
        Assumes zero first sample values and unit sampling intervals.
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    @overload
    def addPixels(self, s1: Sampling, s2: Sampling, f: Float2D) -> PixelsView:
        """
        Adds a pixels view of the specified sampled function f(x1,x2).
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    @overload
    def addPixels(self, irow: int, icol: int, f: Float2D) -> PixelsView:
        """
        Adds a pixels view of the specified sampled function f(x1,x2).
        Assumes zero first sample values and unit sampling intervals.
        where n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2),
        
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    @overload
    def addPixels(self, irow: int, icol: int, s1: Sampling, s2: Sampling,
                  f: Float2D) -> PixelsView:
        """
        Adds a pixels view of the specified sampled function f(x1,x2).
        where n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2),
        
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    @overload
    def addPixels(self, f: Float3D) -> PixelsView:
        """
        Adds a pixels view of the specified sampled function f(x1,x2).
        Assumes zero first sample values and unit sampling intervals.
        where n1 = f[0][0].length, n2 = f[0].length, and nc is the
        number of components.
        
        Parameters
        -----------
        f : Float3D
            array[nc][n2][n1] of sampled function values f(x1,x2),
        
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    @overload
    def addPixels(self, s1: Sampling, s2: Sampling, f: Float3D) -> PixelsView:
        """
        Adds a pixels view of the specified sampled function f(x1,x2).
        where n1 = f[0][0].length, n2 = f[0].length, and nc is the
        number of components.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float3D
            array[nc][n2][n1] of sampled function values f(x1,x2),
        
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    @overload
    def addPixels(self, irow: int, icol: int, f: Float3D) -> PixelsView:
        """
        Adds a pixels view of the specified sampled function f(x1,x2).
        Assumes zero first sample values and unit sampling intervals.
        where n1 = f[0][0].length, n2 = f[0].length, and nc is the
        number of components.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        f : Float3D
            array[nc][n2][n1] of sampled function values f(x1,x2),
        
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    @overload
    def addPixels(self, irow: int, icol: int, s1: Sampling, s2: Sampling,
                  f: Float3D) -> PixelsView:
        """
        Adds a pixels view of the specified sampled function f(x1,x2).
        where n1 = f[0][0].length, n2 = f[0].length, and nc is the
        number of components.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float3D
            array[nc][n2][n1] of sampled function values f(x1,x2),
        
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    @overload
    def addPoints(self, x1: Float1D, x2: Float1D) -> PointsView:
        """
        Adds a points view of the arrays x1 and x2 of point (x1,x2) coordinates.
        
        Parameters
        -----------
        x1 : Float1D
            array of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, x1: Float1D, x2: Float1D, x3: Float1D) -> PointsView:
        """
        Adds a points view of arrays x1, x2 and x3 of point (x1,x2,x3) coordinates.
        
        Parameters
        -----------
        x1 : Float1D
            array of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        x3 : Float1D
            array of x3 coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, x2: Float1D) -> PointsView:
        """
        Adds a points view of (x1,x2) with specified x2 coordinates.
        The corresponding coordinates x1 are assumed to be 0, 1, 2, ....
        
        Parameters
        -----------
        x2 : Float1D
            array of x2 coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, s1: Sampling, x2: Float1D) -> PointsView:
        """
        Adds a view of points (x1,x2) for a sampled function x2(x1).
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, x1: Float2D, x2: Float2D) -> PointsView:
        """
        Adds a view of arrays of (x1,x2) coordinates for multiple plot segments.
        The lengths of the specified arrays x1 and x2 must be equal.
        
        Parameters
        -----------
        x1 : Float2D
            array of arrays of x1 coordinates.
        x2 : Float2D
            array of arrays of x2 coordinates.
        
        Returns
        --------
        output : PointsView
            a points view.
        """

    @overload
    def addPoints(self, irow: int, icol: int, x1: Float1D,
                  x2: Float1D) -> PointsView:
        """
        Adds a points view of the arrays x1 and x2 of point (x1,x2) coordinates.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        x1 : Float1D
            array of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, irow: int, icol: int, x1: Float1D, x2: Float1D,
                  x3: Float1D) -> PointsView:
        """
        Adds a points view of arrays x1, x2 and x3 of point (x1,x2,x3) coordinates.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        x1 : Float1D
            array of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        x3 : Float1D
            array of x3 coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, irow: int, icol: int, x2: Float1D) -> PointsView:
        """
        Adds a points view of (x1,x2) with specified x2 coordinates.
        The corresponding coordinates x1 are assumed to be 0, 1, 2, ....
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        x2 : Float1D
            array of x2 coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, irow: int, icol: int, s1: Sampling,
                  x2: Float1D) -> PointsView:
        """
        Adds a view of points (x1,x2) for a sampled function x2(x1).
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        s1 : Sampling
            the sampling of x1 coordinates.
        x2 : Float1D
            array of x2 coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, irow: int, icol: int, x1: Float2D,
                  x2: Float2D) -> PointsView:
        """
        Adds a view of arrays of (x1,x2) coordinates for multiple plot segments.
        The lengths of the specified arrays x1 and x2 must be equal.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        x1 : Float2D
            array of arrays of x1 coordinates.
        x2 : Float2D
            array of arrays of x2 coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addContours(self, f: Float2D) -> ContoursView:
        """
        Adds a contours view with the function f(x1,x2).
        Function f(x1,x2) assumed to have uniform sampling.
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : ContoursView
            the contours view.
        """

    @overload
    def addContours(self, s1: Sampling, s2: Sampling,
                    f: Float2D) -> ContoursView:
        """
        Adds a contours view of the specified sampled function f(x1,x2).
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : ContoursView
            the contours view.
        """

    @overload
    def addContours(self, irow: int, icol: int, f: Float2D) -> ContoursView:
        """
        Adds a contours view with the function f(x1,x2).
        Function f(x1,x2) assumed to have uniform sampling.
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        f : Float2D
            array[n2][n1] of sampline function values f(x1,x2), where
        
        Returns
        --------
        output : ContoursView
            a contours view.
        """

    @overload
    def addContours(self, irow: int, icol: int, s1: Sampling, s2: Sampling,
                    f: Float2D) -> ContoursView:
        """
        Adds a contours view of the specified sampled function f(x1,x2).
        where n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2),
        
        Returns
        --------
        output : ContoursView
            the contours view.
        """

    @overload
    def addSequence(self, f: Float1D) -> SequenceView:
        """
        Adds a sequence view with specified values f(x).
        Uses default sampling of x = 0, 1, 2, ....
        
        Parameters
        -----------
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SequenceView
            the sequence view.
        """

    @overload
    def addSequence(self, sx: Sampling, f: Float1D) -> SequenceView:
        """
        Adds a sequence view with specified sampling and values f(x).
        
        Parameters
        -----------
        sx : Sampling
            the sampling of the variable x.
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SequenceView
            the sequence view.
        """

    @overload
    def addSequence(self, irow: int, icol: int, f: Float1D) -> SequenceView:
        """
        Adds a sequence view with specified values f(x).
        Uses default sampling of x = 0, 1, 2, ....
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SequenceView
            the sequence view.
        """

    @overload
    def addSequence(self, irow: int, icol: int, sx: Sampling,
                    f: Float1D) -> SequenceView:
        """
        Adds a sequence view with specified sampling and values f(x).
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        sx : Sampling
            the sampling of the variable x.
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SequenceView
            the sequence view.
        """

    @overload
    def addTiledView(self, tv: TiledView) -> bool:
        """
        Adds the specified tiled view to this plot panel. If the tiled view
        is already in this panel, it is first removed, before adding it again.
        tiled view; false, otherwise.
        
        Parameters
        -----------
        tv : TiledView
            the tiled view.
        
        Returns
        --------
        output : bool
            true, if this panel did not already contain the specified
        """

    @overload
    def addTiledView(self, irow: int, icol: int, tv: TiledView) -> bool:
        """
        Adds the specified tiled view to this plot panel. If the tiled view
        is already in the specified tile, it is first removed, before adding
        it again.
        tiled view; false, otherwise.
        
        Parameters
        -----------
        irow : int
            the tile row index.
        icol : int
            the tile column index.
        tv : TiledView
            the tiled view.
        
        Returns
        --------
        output : bool
            true, if the tile did not already contain the specified
        """

    def remove(self, tv: TiledView) -> bool:
        """
        Removes the specified tiled view from this plot panel.
        false, otherwise.
        
        Parameters
        -----------
        tv : TiledView
            the tiled view.
        
        Returns
        --------
        output : bool
            true, if this panel contained the specified tiled view;
        """

    def setFont(self, font: Font) -> None:
        """
        Sets the font in all components of this panel.
        Sets the title font to be 1.5 times larger than the specified font.
        
        Parameters
        -----------
        font : Font
            the font.
        """

    def setForeground(self, color: Color) -> None:
        """
        Sets the foreground color in all components of this panel.
        
        Parameters
        -----------
        color : Color
            the foreground color.
        """

    def setBackground(self, color: Color) -> None:
        """
        Sets the background color in all components of this panel.
        
        Parameters
        -----------
        color : Color
            the background color.
        """
