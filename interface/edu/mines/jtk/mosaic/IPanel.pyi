from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class IPanel:
    """
    A panel that can paint itself to fit an image.
    Some components in this package, such as mosaics, tiles, and tile axes,
    must be able to render themselves to images as well as on screen. For
    various reasons, those images often have resolution that is higher
    than that of a display screen. Simply scaling an on-screen rendering
    does not exploit this higher resolution, because screen coordinates
    are typically specified as integers. Rounding to the nearest integer
    screen coordinates and then scaling to a high resolution image yields
    visual artifacts, such as curves that appear jagged in the image.
    
    Classes that extend this base class work differently. They paint
    themselves to fit any specified rectangle of a specified graphics
    context. When painting to a display screen, that graphics rectangle
    is simply the panel's rectangle, in screen coordinates. However, when
    painting to an image, the dimensions of that rectangle may be much
    larger, corresponding to the higher resolution of the image. When
    painting, these panels round coordinates to the nearest pixel of that
    graphics rectangle, not the panel's on-screen rectangle. In this way,
    panels can paint themselves with any desired resolution.
    
    One complication is font size. Another is line width. Such properties
    are typically specified in points, which are roughly equivalant to
    on-screen pixels. Therefore, when drawing to a high-resolution image,
    font sizes and line widths must be increased. This base class provides
    methods that panels in this package use to properly scale font sizes,
    line widths, and other resolution-dependent properties.
    """

    def paintToRect(self, g2d: Graphics2D, x: int, y: int, w: int,
                    h: int) -> None:
        """
        Paints this panel to a specified rectangle of a graphics context.
        This implementation simply paints any IPanel children of this panel.
        It ignores and does not draw any children that are not IPanels.
        
        Classes that extend this base class typically override this method
        to draw something besides children of this panel. When appropriate,
        those extensions may also call this method.
        
        Parameters
        -----------
        g2d : Graphics2D
            the graphics context.
        x : int
            the x-coordinate of the graphics rectangle.
        y : int
            the y-coordinate of the graphics rectangle.
        w : int
            the width of the graphics rectangle.
        h : int
            the height of the graphics rectangle.
        """

    @overload
    def paintToImage(self, image: BufferedImage) -> None:
        """
        Paints this panel to fit the specified image.
        
        Parameters
        -----------
        image : BufferedImage
            the image.
        """

    @overload
    def paintToImage(self, width: int) -> BufferedImage:
        """
        Paints this panel to fit a new image with specified width in pixels.
        The image height is computed so that the image has the same aspect
        ratio as this panel.
        
        Parameters
        -----------
        width : int
            the image width, in pixels.
        
        Returns
        --------
        output : BufferedImage
            the image.
        """

    def paintToPng(self, dpi: double, win: double, fileName: String) -> None:
        """
        Paints this panel to a PNG image with specified resolution and width.
        The image height is computed so that the image has the same aspect
        ratio as this panel.
        
        Parameters
        -----------
        dpi : double
            the image resolution, in dots per inch.
        win : double
            the image width, in inches.
        fileName : String
            the name of the file to contain the PNG image.
        """
