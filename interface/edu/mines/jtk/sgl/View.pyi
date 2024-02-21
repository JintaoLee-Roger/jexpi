from typing import overload
from edu.mines.jtk.mapping import *


class View:
    """
    An abstract view of a world.
    
    A view draws its world on one or more view canvases. The simplest
    and typical scenario is that a view draws on only one canvas.
    
    A view manages a world-to-view transform, which is that part of the
    OpenGL modelview transform that depends on the view. A view also
    manages the view-to-cube and cube-to-pixel transforms of each of its
    view canvases, as necessary.
    
    All three transforms - world-to-view, view-to-cube, and cube-to-pixel -
    are view-dependent. Because the latter two transforms may vary among
    the multiple view canvases on which a view draws, those transforms
    are stored with each view canvas. Nevertheless, the view updates the
    view-to-cube and cube-to-pixel transforms for each view canvas on which
    it draws.
    
    Some aspects of the world-to-view transform are common to all classes of
    views. These include an initial translation, scaling, and rotation of the
    world coordinate system. Typically, these initial transforms are followed
    by other view-specific transforms, but all classes of views provide at
    least these aspects.
    
    Classes that extend this abstract base class must implement two methods:
    {@link #updateTransforms(ViewCanvas)} and {@link #draw(ViewCanvas)}. The
    method {@link #updateTransforms(ViewCanvas)} is called to update the
    three view-dependent transforms for a specified view canvas. The method
    {@link #draw(ViewCanvas)} is called to draw the view on a specified view
    canvas.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a view of no world.
        """

    @overload
    def __init__(self, world: World) -> None:
        """
        Constructs a view of the specified world.
        
        Parameters
        -----------
        world : World
            the world.
        """

    def getAxesOrientation(self) -> AxesOrientation:
        """
    
        """

    def setAxesOrientation(self, axesOrientation: AxesOrientation) -> None:
        """
    
        """

    def getAxesScale(self) -> Tuple3:
        """
    
        """

    @overload
    def setAxesScale(self, s: Tuple3) -> None:
        """
    
        """

    @overload
    def setAxesScale(self, sx: double, sy: double, sz: double) -> None:
        """
    
        """

    def setWorld(self, world: World) -> None:
        """
        Sets the world drawn by this view.
        Then repaints this view.
        
        Parameters
        -----------
        world : World
            the world.
        """

    def getWorld(self) -> World:
        """
        Gets the world drawn by in this view.
        """

    def setWorldToView(self, worldToView: Matrix44) -> None:
        """
        Sets the world-to-view transform managed by this view.
        Then repaints this view.
        
        Parameters
        -----------
        worldToView : Matrix44
            the world-to-view transform; copied, not referenced.
        """

    def getWorldToView(self) -> Matrix44:
        """
        Gets the world-to-view transform managed by this view.
        Returns
        --------
        output : Matrix44
            the world-to-view transform; by copy, not by reference.
        """

    def countCanvases(self) -> int:
        """
        Returns the number of canvases on which this view draws.
        Returns
        --------
        output : int
            the number of canvases.
        """

    def getCanvases(self) -> Iterator:
        """
        Gets an iterator for the canvases on which this view draws.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def updateTransforms(self) -> None:
        """
        Updates transforms for this view and all canvases on which it draws.
        This method should be called when the world drawn by this view changes,
        when the view parameters change, and when any canvas on which this view
        draws changes.
        """

    def repaint(self) -> None:
        """
        Repaints all canvases on which this view draws. This method should be
        called when this view must redraw its world, for example, when that
        world changes, or when a canvas on which this view draws changes.
        """
