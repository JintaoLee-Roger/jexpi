from typing import overload
from edu.mines.jtk.mapping import *


class PlotFrame:
    """
    A plot frame is a window containing one or two plot panels.
    A plot frame (like any JFrame) has a content pane with a border layout,
    and it adds a panel (JPanel) containing its plot panel(s) to the center
    of that content pane. Menu and tool bars can be added as for any other
    JFrame.
    
    Plot frames that contain two plot panels also contain a split pane
    with either a horizontal (side by side) or vertical (above and below)
    orientation. The split pane enables interactive resizing of the plot
    panels.
    
    A plot frame has a single mode manager
    ({@link edu.mines.jtk.awt.ModeManager}).
    When constructed, a plot frame adds and sets active (1) a tile zoom mode
    ({@link edu.mines.jtk.mosaic.TileZoomMode}) and (2) a mouse track mode
    ({@link edu.mines.jtk.mosaic.MouseTrackMode}) to that mode manager. Of
    course, other modes of interaction can be added as well.
    
    The default font and background and foreground colors for a plot frame
    are Arial (plain, 24 point), white, and black, respectively. Any of
    these attributes can be changed. For both simplicity and consistency,
    when any of these attributes are set for this frame, they are set for
    all components in this frame as well. For example, calling the method
    {@link #setFont(java.awt.Font)} will set the font for all panels and,
    in turn, all mosaics, tiles, tile axes, color bars, and titles in this
    frame.
    
    Note that a plot frame has methods that enable font sizes to be
    automatically computed for figures in printed manuscripts and in
    presentation slides.
    """

    @overload
    def __init__(self, panel: PlotPanel) -> None:
        """
        Constructs a plot frame for the specified plot panel.
        
        Parameters
        -----------
        panel : PlotPanel
            the plot panel.
        """

    @overload
    def __init__(self, panelTL: PlotPanel, panelBR: PlotPanel,
                 split: Split) -> None:
        """
        Constructs a plot frame with two plot panels in a split pane.
        
        Parameters
        -----------
        panelTL : PlotPanel
            the top-left panel.
        panelBR : PlotPanel
            the bottom-right panel.
        split : Split
            the split pane orientation.
        """

    def getPlotPanel(self) -> PlotPanel:
        """
        Gets the plot panel in this frame. If this frame contains more
        than one plot panel, this method returns the top-left panel.
        Returns
        --------
        output : PlotPanel
            the plot panel.
        """

    def getPlotPanelTopLeft(self) -> PlotPanel:
        """
        Gets the top-left plot panel in this frame. If this panel contains only
        one panel, then the top-left and bottom-right panels are the same.
        Returns
        --------
        output : PlotPanel
            the top-left plot panel.
        """

    def getPlotPanelBottomRight(self) -> PlotPanel:
        """
        Gets the bottom-right plot panel in this frame. If this panel contains
        only one panel, then the top-left and bottom-right panels are the same.
        Returns
        --------
        output : PlotPanel
            the bottom-right plot panel.
        """

    def getSplitPane(self) -> JSplitPane:
        """
        Gets the split pane for this frame if it contains two panels.
        Returns
        --------
        output : JSplitPane
            the split pane; null, if this frame contains only one panel.
        """

    def getModeManager(self) -> ModeManager:
        """
        Gets the mode manager for this plot frame.
        Returns
        --------
        output : ModeManager
            the mode manager.
        """

    def getTileZoomMode(self) -> TileZoomMode:
        """
        Gets the tile zoom mode for this plot frame.
        By default, this mode is active.
        Returns
        --------
        output : TileZoomMode
            the tile zoom mode.
        """

    def getMouseTrackMode(self) -> MouseTrackMode:
        """
        Gets the mouse track mode for this plot frame.
        By default, this mode is active.
        Returns
        --------
        output : MouseTrackMode
            the mouse track mode.
        """

    def paintToPng(self, dpi: double, win: double, fileName: String) -> None:
        """
        Paints this frame's panel(s) to a PNG image with specified parameters.
        The image height is computed so that the image has the same aspect
        ratio as the panel(s) in this frame.
        
        Parameters
        -----------
        dpi : double
            the image resolution, in dots per inch.
        win : double
            the image width, in inches.
        fileName : String
            the name of the file to contain the PNG image.
        """

    def setFont(self, font: Font) -> None:
        """
        Sets the font in all components in this frame.
        
        Parameters
        -----------
        font : Font
            the font.
        """

    def setFontSize(self, size: float) -> None:
        """
        Sets the font size (in points) for all panels in this frame.
        The font size will not change as this frame is resized.
        
        Parameters
        -----------
        size : float
            the size.
        """

    @overload
    def setFontSizeForSlide(self, fracWidth: double,
                            fracHeight: double) -> None:
        """
        Sets font size automatically for a slide in presentations.
        This method causes the font size to change as this frame is resized,
        so that text height will be about 1/25 of slide height if this frame
        is saved to an image.
        Specified fractions indicate indicate how much of the slide is
        available for this plot. These fractions may be less than one,
        to leave room for titles, other plots, etc.
        
        This method uses a default width/height aspect ratio = 4.0/3.0.
        To explicitly specify the aspect ratio, use the method
        {@link #setFontSizeForSlide(double,double,double)}.
        
        Parameters
        -----------
        fracWidth : double
            the fraction of slide width available.
        fracHeight : double
            the fraction of slide height available.
        """

    @overload
    def setFontSizeForSlide(self, fracWidth: double, fracHeight: double,
                            aspectRatio: double) -> None:
        """
        Sets font size automatically for a slide in presentations.
        This method causes the font size to change as this frame is resized,
        so that text height will be about 1/25 of slide height if this frame
        is saved to an image.
        
        Parameters
        -----------
        fracWidth : double
            the fraction of slide width available.
        fracHeight : double
            the fraction of slide height available.
        aspectRatio : double
            the width/height ratio for slides; e.g., 16.0/9.0.
        """

    def setFontSizeForPrint(self, fontSize: double, plotWidth: double) -> None:
        """
        Sets font size to automatically adjust for a printed manuscript.
        This method causes the font size to change as this frame is resized,
        so that font size will equal the specified size if this frame is saved
        to an image and that image is then scaled to fit the specified width.
        
        Parameters
        -----------
        fontSize : double
            the printed font size (in points) for this plot.
        plotWidth : double
            the printed width (in points) of this plot.
        """

    def setForeground(self, color: Color) -> None:
        """
        Sets the foreground color in all components in this frame.
        
        Parameters
        -----------
        color : Color
            the foreground color.
        """

    def setBackground(self, color: Color) -> None:
        """
        Sets the background color in all components in this frame.
        
        Parameters
        -----------
        color : Color
            the background color.
        """
