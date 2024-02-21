from typing import overload
from edu.mines.jtk.mapping import *


class SimplePlot:
    """
    A simple plot is easy to construct and especially useful for quick
    diagnostic plots of arrays of floats or doubles. Specifically, a
    simple plot is a plot frame with only one plot panel.
    
    For example, a simple plot of an array float[] f can be displayed with
    <pre><code>
    SimplePlot.asSequence(f);
    </code></pre>
    Likewise, a simple plot of an array float[][] f can be displayed with
    <pre><code>
    SimplePlot.asPixels(f);
    </code></pre>
    The plots in these examples use default parameters and cannot be
    customized easily. More complex plots can be constructed as in this
    example:
    <pre><code>
    SimplePlot plot = new SimplePlot();
    plot.addGrid("H-.V-.");
    PointsView pv = plot.addPoints(f);
    pv.setStyle("r-o");
    plot.setTitle("A plot of an array");
    plot.setVLabel("array value");
    plot.setHLabel("array index");
    </code></pre>
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a simple plot with default lower-left origin.
        """

    @overload
    def __init__(self, origin: Origin) -> None:
        """
        Constructs a simple plot with specified origin.
        
        Parameters
        -----------
        origin : Origin
            the plot origin.
        """

    @overload
    @staticmethod
    def asPoints(self, f: Float1D) -> SimplePlot:
        """
        Returns a new plot with a points view of specified values f(x).
        Uses default sampling of x = 0, 1, 2, ....
        
        Parameters
        -----------
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asPoints(self, s: Sampling, f: Float1D) -> SimplePlot:
        """
        Returns a new plot with a points view of a sampled function f(x).
        
        Parameters
        -----------
        s : Sampling
            the sampling of the x coordinate.
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asPoints(self, x: Float1D, y: Float1D) -> SimplePlot:
        """
        Returns a new plot with a points view of specified values (x,y).
        
        Parameters
        -----------
        x : Float1D
            array of x coordinates.
        y : Float1D
            array of y coordinates.
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asSequence(self, f: Float1D) -> SimplePlot:
        """
        Returns a new plot with a sequence view of specified values f(x).
        Uses default sampling of x = 0, 1, 2, ....
        
        Parameters
        -----------
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asSequence(self, s: Sampling, f: Float1D) -> SimplePlot:
        """
        Returns a new plot with a sequence view of a sampled function f(x).
        
        Parameters
        -----------
        s : Sampling
            the sampling of the x coordinate.
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asPixels(self, f: Float2D) -> SimplePlot:
        """
        Returns a new plot with a pixels view of a sampled function f(x1,x2).
        Assumes zero first-sample values and unit sampling intervals.
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asPixels(self, s1: Sampling, s2: Sampling, f: Float2D) -> SimplePlot:
        """
        Returns a new plot with a pixels view of a sampled function f(x1,x2).
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the x1 coordinate.
        s2 : Sampling
            the sampling of the x2 coordinate.
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asPoints(self, f: Double1D) -> SimplePlot:
        """
        Returns a new plot with a points view of specified values f(x).
        Uses default sampling of x = 0, 1, 2, ....
        
        Parameters
        -----------
        f : Double1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asPoints(self, s: Sampling, f: Double1D) -> SimplePlot:
        """
        Returns a new plot with a points view of a sampled function f(x).
        
        Parameters
        -----------
        s : Sampling
            the sampling of the x coordinate.
        f : Double1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asPoints(self, x: Double1D, y: Double1D) -> SimplePlot:
        """
        Returns a new plot with a points view of specified values (x,y).
        
        Parameters
        -----------
        x : Double1D
            array of x coordinates.
        y : Double1D
            array of y coordinates.
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asSequence(self, f: Double1D) -> SimplePlot:
        """
        Returns a new plot with a sequence view of specified values f(x).
        Uses default sampling of x = 0, 1, 2, ....
        
        Parameters
        -----------
        f : Double1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asSequence(self, s: Sampling, f: Double1D) -> SimplePlot:
        """
        Returns a new plot with a sequence view of a sampled function f(x).
        
        Parameters
        -----------
        s : Sampling
            the sampling of the x coordinate.
        f : Double1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asPixels(self, f: Double2D) -> SimplePlot:
        """
        Returns a new plot with a pixels view of a sampled function f(x1,x2).
        Assumes zero first-sample values and unit sampling intervals.
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        f : Double2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @overload
    @staticmethod
    def asPixels(self, s1: Sampling, s2: Sampling, f: Double2D) -> SimplePlot:
        """
        Returns a new plot with a pixels view of a sampled function f(x1,x2).
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the x1 coordinate.
        s2 : Sampling
            the sampling of the x2 coordinate.
        f : Double2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : SimplePlot
            the plot.
        """

    @staticmethod
    def asContours(self, f: Float2D) -> SimplePlot:
        """
        Returns a new plot with a contours view of a sampled function f(x1,x2).
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        f : Float2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : SimplePlot
            the plot.
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
    def addPoints(self, f: Float1D) -> PointsView:
        """
        Adds a points view of specified values f(x).
        Uses default sampling of x = 0, 1, 2, ....
        
        Parameters
        -----------
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, s: Sampling, f: Float1D) -> PointsView:
        """
        Adds a points view of a sampled function f(x).
        
        Parameters
        -----------
        s : Sampling
            the sampling of the x coordinate.
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, x: Float1D, y: Float1D) -> PointsView:
        """
        Adds a points view of specified values (x,y).
        
        Parameters
        -----------
        x : Float1D
            array of x coordinates.
        y : Float1D
            array of y coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, f: Double1D) -> PointsView:
        """
        Adds a points view of specified values f(x).
        Uses default sampling of x = 0, 1, 2, ....
        
        Parameters
        -----------
        f : Double1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, s: Sampling, f: Double1D) -> PointsView:
        """
        Adds a points view of a sampled function f(x).
        
        Parameters
        -----------
        s : Sampling
            the sampling of the x coordinate.
        f : Double1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : PointsView
            the points view.
        """

    @overload
    def addPoints(self, x: Double1D, y: Double1D) -> PointsView:
        """
        Adds a points view of specified values (x,y).
        
        Parameters
        -----------
        x : Double1D
            array of x coordinates.
        y : Double1D
            array of y coordinates.
        
        Returns
        --------
        output : PointsView
            the points view.
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
    def addSequence(self, s: Sampling, f: Float1D) -> SequenceView:
        """
        Adds a sequence view with specified sampling and values f(x).
        
        Parameters
        -----------
        s : Sampling
            the sampling of the variable x.
        f : Float1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SequenceView
            the sequence view.
        """

    @overload
    def addSequence(self, f: Double1D) -> SequenceView:
        """
        Adds a sequence view with specified values f(x).
        Uses default sampling of x = 0, 1, 2, ....
        
        Parameters
        -----------
        f : Double1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SequenceView
            the sequence view.
        """

    @overload
    def addSequence(self, s: Sampling, f: Double1D) -> SequenceView:
        """
        Adds a sequence view with specified sampling and values f(x).
        
        Parameters
        -----------
        s : Sampling
            the sampling of the variable x.
        f : Double1D
            array of sampled function values f(x).
        
        Returns
        --------
        output : SequenceView
            the sequence view.
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
    def addPixels(self, f: Double2D) -> PixelsView:
        """
        Adds a pixels view of the specified sampled function f(x1,x2).
        Assumes zero first sample values and unit sampling intervals.
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        f : Double2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    @overload
    def addPixels(self, s1: Sampling, s2: Sampling, f: Double2D) -> PixelsView:
        """
        Adds a pixels view of the specified sampled function f(x1,x2).
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Double2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : PixelsView
            the pixels view.
        """

    @overload
    def addContours(self, f: Float2D) -> ContoursView:
        """
        Adds a contours view of the specified sample function f(x1,x2).
        n2 = f[0].length and n2 = f.length.
        
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
    def addContours(self, f: Double2D) -> ContoursView:
        """
        Adds a contours view of the specified sampled function f(x1,x2).
        Assumes zero first sample values and unit sampling intervals.
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        f : Double2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : ContoursView
            the contours view.
        """

    @overload
    def addContours(self, s1: Sampling, s2: Sampling,
                    f: Double2D) -> ContoursView:
        """
        Adds a contours view of the specified sampled function f(x1,x2).
        n1 = f[0].length and n2 = f.length.
        
        Parameters
        -----------
        s1 : Sampling
            the sampling of the variable x1; must be uniform.
        s2 : Sampling
            the sampling of the variable x2; must be uniform.
        f : Double2D
            array[n2][n1] of sampled function values f(x1,x2), where
        
        Returns
        --------
        output : ContoursView
            the contours view.
        """

    @overload
    def addColorBar(self) -> ColorBar:
        """
        Adds the color bar with no label. The color bar paints the color map
        of the most recently added pixels view. To avoid confusion, a color
        bar should perhaps not be added when this plot contains more  than
        one pixels view.
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
        Adds the color bar for the specified color mapped object.
        
        Parameters
        -----------
        cm : ColorMapped
            the color mapped object.
        
        Returns
        --------
        output : ColorBar
            the color bar.
        """

    @overload
    def addColorBar(self, cm: ColorMapped, label: String) -> ColorBar:
        """
        Adds the color bar for the specified color mapped object and label.
        
        Parameters
        -----------
        cm : ColorMapped
            the color mapped object.
        label : String
            the label; null, if none.
        
        Returns
        --------
        output : ColorBar
            the color bar.
        """

    def add(self, tv: TiledView) -> bool:
        """
        Adds the specified tiled view to this plot's panel. If the tiled view
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

    def remove(self, tv: TiledView) -> bool:
        """
        Removes the specified tiled view from this plot's panel.
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

    def addTitle(self, title: String) -> None:
        """
        Adds the plot title. Equivalent to {@link #setTitle(String)}.
        The title font is 1.5 times larger than the font of this plot.
        
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
        By default, limits are computed automatically by graphical views.
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
        By default, limits are computed automatically by graphical views.
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
        By default, limits are computed automatically by graphical views.
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

    def setHInterval(self, interval: double) -> None:
        """
        Sets the tic interval for the horizontal axis.
        
        Parameters
        -----------
        interval : double
            the major labeled tic interval.
        """

    def setVInterval(self, interval: double) -> None:
        """
        Sets the tic interval for the vertical axis.
        
        Parameters
        -----------
        interval : double
            the major labeled tic interval.
        """

    def setHLabel(self, label: String) -> None:
        """
        Sets the label for the horizontal axis.
        
        Parameters
        -----------
        label : String
            the label.
        """

    def setVLabel(self, label: String) -> None:
        """
        Sets the label for the vertical axis.
        
        Parameters
        -----------
        label : String
            the label.
        """

    def setHFormat(self, format: String) -> None:
        """
        Sets the format for tic labels in the horizontal axis.
        
        Parameters
        -----------
        format : String
            the format.
        """

    def setVFormat(self, format: String) -> None:
        """
        Sets the format for tic labels in the vertical axis.
        
        Parameters
        -----------
        format : String
            the format.
        """

    def setVRotated(self, rotated: bool) -> None:
        """
        Sets the rotation of tic labels in the vertical axis.
        If true, tic labels in the vertical axis are rotated 90 degrees
        counter-clockwise. The default is false, not rotated.
        
        Parameters
        -----------
        rotated : bool
            true if rotated; false, otherwise.
        """

    def getPlotPanel(self) -> PlotPanel:
        """
        Gets the plot panel for this plot.
        Returns
        --------
        output : PlotPanel
            the plot panel.
        """
