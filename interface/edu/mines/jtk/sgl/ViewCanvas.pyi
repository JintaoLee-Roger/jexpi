from typing import overload
from edu.mines.jtk.mapping import *


class ViewCanvas:
    """
    An OpenGL canvas on which a view draws its world.
    
    The relationship between views and view canvases is one-to-many. A view
    canvas is managed by only one view, but that view may draw its world on
    on one or more view canvases.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a canvas with no view.
        """

    @overload
    def __init__(self, view: View) -> None:
        """
        Constructs a canvas for the specified view.
        
        Parameters
        -----------
        view : View
            the view.
        """

    def setView(self, view: View) -> None:
        """
        Sets the view that draws on this canvas.
        
        Parameters
        -----------
        view : View
            the view; null, if none.
        """

    def getView(self) -> View:
        """
        Gets the view that draws on this canvas.
        Returns
        --------
        output : View
            the view; null, if none.
        """

    def setViewToCube(self, viewToCube: Matrix44) -> None:
        """
        Sets the view-to-cube transform for this canvas.
        Typically, the view sets the view-to-cube transform.
        
        Parameters
        -----------
        viewToCube : Matrix44
            the view-to-cube transform; copied, not referenced.
        """

    def getViewToCube(self) -> Matrix44:
        """
        Gets the view-to-cube transform for this canvas.
        Returns
        --------
        output : Matrix44
            the view-to-cube transform; by copy, not by reference.
        """

    def setCubeToPixel(self, cubeToPixel: Matrix44) -> None:
        """
        Sets the cube-to-pixel transform for this canvas.
        Typically, the view sets the cube-to-pixel transform.
        
        Parameters
        -----------
        cubeToPixel : Matrix44
            the cube-to-pixel transform; copied, not referenced.
        """

    def getCubeToPixel(self) -> Matrix44:
        """
        Gets the cube-to-pixel transform for this canvas.
        Returns
        --------
        output : Matrix44
            the cube-to-pixel transform; by copy, not by reference.
        """

    def getPixelZ(self, xp: int, yp: int) -> double:
        """
        Gets the pixel z coordinate at the specified pixel x and y coordinates.
        Reads the front depth buffer of this canvas at the specified pixel
        coordinates (xp,yp) to compute (approximately) the pixel z coordinate zp.
        
        The pixel z coordinate is a floating point number between 0.0 and 1.0.
        The value zp = 0.0 corresponds to the near clipping plane, and the value
        zp = 1.0 corresponds to the far clipping plane.
        
        Parameters
        -----------
        xp : int
            the pixel x coordinate.
        yp : int
            the pixel y coordinate.
        
        Returns
        --------
        output : double
            the pixel z coordinate.
        """

    def glInit(self) -> None:
        """
    
        """

    def glPaint(self) -> None:
        """
    
        """

    def glResize(self, x: int, y: int, width: int, height: int) -> None:
        """
    
        """
