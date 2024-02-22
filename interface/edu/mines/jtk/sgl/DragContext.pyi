from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class DragContext:
    """
    A context for dragging. {@link Dragable} nodes use a drag context to
    implement dragging with a mouse.
    
    A drag context is constructed from a pick result, which has a picked
    point in local coordinates, as well as transforms to world and pixel
    coordinates. Those local-to-world and and local-to-pixel transforms
    are assumed to be constant while the the mouse is being dragged. This
    assumption implies that the view must not change while dragging.
    
    A drag context has a current mouse event and a current point, with
    local, world, and pixel coordinates. A mouse motion listener (not
    part of this context) is responsible for updating this context as
    the mouse is dragged. Updates modify the current mouse event and the
    current point maintained by this context.
    """

    def __init__(self, pr: PickResult) -> None:
        """
        Constructs a drag context for the specified pick result.
        
        Parameters
        -----------
        pr : PickResult
            the pick result.
        """

    def update(self, event: MouseEvent) -> None:
        """
        Updates this drag context for the specified mouse event. Updates the
        current mouse event and the current point's local, world, and pixel
        coordinates. Mouse motion listeners call this method as the mouse is
        dragged.
        
        Parameters
        -----------
        event : MouseEvent
            the mouse event.
        """

    def getViewCanvas(self) -> ViewCanvas:
        """
        Gets the canvas for which this context was constructed.
        Returns
        --------
        output : ViewCanvas
            the view canvas.
        """

    def getView(self) -> View:
        """
        Gets the view for which this context was constructed.
        Returns
        --------
        output : View
            the view.
        """

    def getWorld(self) -> World:
        """
        Gets the world for which this context was constructed.
        Returns
        --------
        output : World
            the world.
        """

    def getMouseEvent(self) -> MouseEvent:
        """
        Gets the current mouse event.
        Returns
        --------
        output : MouseEvent
            the mouse event.
        """

    def getPointLocal(self) -> Point3:
        """
        Gets the current point in local coordinates.
        Returns
        --------
        output : Point3
            the current point in local coordinates.
        """

    def getPointWorld(self) -> Point3:
        """
        Gets the current point in world coordinates.
        Returns
        --------
        output : Point3
            the current point in world coordinates.
        """

    def getPointPixel(self) -> Point3:
        """
        Gets the current point in pixel coordinates.
        Returns
        --------
        output : Point3
            the current point in pixel coordinates.
        """

    def getPixelZ(self) -> double:
        """
        Gets the pixel z (depth) coordinate of the current point. This depth
        depth coordinate increases from 0.0 at the near clipping plane to 1.0
        at the far clipping plane.
        Returns
        --------
        output : double
            the pixel z coordinate.
        """

    def getLocalToWorld(self) -> Matrix44:
        """
        Gets the local-to-world coordinate transform matrix.
        Returns
        --------
        output : Matrix44
            the local-to-world coordinate transform matrix.
        """

    def getLocalToPixel(self) -> Matrix44:
        """
        Gets the local-to-pixel coordinate transform matrix.
        Returns
        --------
        output : Matrix44
            the local-to-pixel coordinate transform matrix.
        """

    def getWorldToPixel(self) -> Matrix44:
        """
        Gets the world-to-pixel coordinate transform matrix.
        Returns
        --------
        output : Matrix44
            the world-to-pixel coordinate transform matrix.
        """
