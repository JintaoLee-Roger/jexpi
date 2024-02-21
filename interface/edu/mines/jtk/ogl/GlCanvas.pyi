from typing import overload
from edu.mines.jtk.mapping import *


class GlCanvas:
    """
    A canvas that paints via OpenGL. To paint a canvas using OpenGL,
    extend this class and implement the method {@link #glPaint()}.
    Classes that extend this class may also implement the methods
    {@link #glInit()} and {@link #glResize(int,int,int,int)}.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a canvas with default capabilities.
        """

    @overload
    def __init__(self, capabilities: GLCapabilities) -> None:
        """
        Constructs a canvas with specified capabilities.
        
        Parameters
        -----------
        capabilities : GLCapabilities
            the OpenGL capabilities.
        """

    def setAutoRepaint(self, autoRepaint: bool) -> None:
        """
        Enables or disables automatic repainting. If enabled, then,
        immediately after this canvas paints itself, it automatically
        requests that it be painted again. By default, automatic
        repainting is disabled.
        
        Parameters
        -----------
        autoRepaint : bool
            true, for automatic repainting; false, otherwise.
        """

    def runWithContext(self, runnable: Runnable) -> None:
        """
        Runs the specified runnable with a current OpenGL context.
        The specified runnable may safely call OpenGL functions within
        its method run.
        
        Parameters
        -----------
        runnable : Runnable
            the object to run.
        """

    def paintToFile(self, fileName: String) -> None:
        """
        Paints this canvas to an image in a file with specified name.
        Uses the file suffix to determine the format of the image.
        
        Parameters
        -----------
        fileName : String
            name of the file to contain the image.
        """

    def glInit(self) -> None:
        """
        Initializes OpenGL state when this canvas is first painted.
        This method is called before the methods
        {@link #glResize(int,int,int,int)} and {@link #glPaint()} when (1)
        this canvas must be painted and (2) it has never been painted before.
        
        In classes that extend this class, implementations of this method
        use the OpenGL context that has been locked for the current thread.
        This implementation does nothing.
        """

    def glResize(self, x: int, y: int, width: int, height: int) -> None:
        """
        Modifies OpenGL state when this canvas has been resized.
        This method is called before the method {@link #glPaint()} when
        (1) this canvas must be painted and (2) its width or height have
        changed since it was last painted or it has never been painted.
        
        In classes that extend this class, implementations of this method
        use the OpenGL context that has been locked for the current thread.
        This implementation does nothing.
        
        Parameters
        -----------
        x : int
            the x pixel coordinate of top-left corner.
        y : int
            the y pixel coordinate of top-left corner.
        width : int
            the width in pixels.
        height : int
            the height in pixels.
        """

    def glPaint(self) -> None:
        """
        Paints this canvas via OpenGL.
        
        In classes that extend this class, implementations of this method
        use the OpenGL context that has been locked for the current thread.
        This implementation does nothing.
        """

    def init(self, drawable: GLAutoDrawable) -> None:
        """
    
        """

    def reshape(self, drawable: GLAutoDrawable, x: int, y: int, w: int,
                h: int) -> None:
        """
    
        """

    def display(self, drawable: GLAutoDrawable) -> None:
        """
    
        """

    def dispose(self, drawable: GLAutoDrawable) -> None:
        """
    
        """

    def displayChanged(self, drawable: GLAutoDrawable, modeChanged: bool,
                       deviceChanged: bool) -> None:
        """
    
        """
