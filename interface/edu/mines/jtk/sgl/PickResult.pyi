
from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class PickResult:
    """
    A result from a pick traversal.
    
    A pick result has a list of nodes, ordered parent to child, that
    represents the path from the root node to the picked node. The last
    node in the list is the picked node.
    
    A pick result also has a point of intersection with a pick shape.
    This point may be obtained in either the local or world coordinate
    system, and its depth (z) may be obtained in pixel coordinates.
    """

    def __init__(self, pc: PickContext, point: Point3) -> None:
        """
        Constructs a new pick result in the specified context.
        
        Parameters
        -----------
        pc : PickContext
            the pick context.
        point : Point3
            the picked point, in local coordinates.
        """
    def getMouseEvent(self) -> MouseEvent:
        """
        Gets the mouse event for this pick result. This is the mouse event
        of the pick context for which this pick result was constructed.
        Returns
        --------
        output : MouseEvent
            the mouse event.
        """
    def getNodes(self) -> Node1D:
        """
        Gets the array of nodes in this result. The nodes are ordered parent
        to child; the last node in the array is the picked node.
        Returns
        --------
        output : Node[]
            the array of nodes; by copy, not by reference.
        """
    @overload
    def getNode(self) -> Node:
        """
        Gets the picked node in this result. The picked node is the last node
        in the list (ordered parent to child) of nodes in this pick result.
        Returns
        --------
        output : Node
            the picked node.
        """
    def getDragableNode(self) -> Dragable:
        """
        Gets a node in this result that is dragable.
        The node returned is the last node in the list (ordered parent to
        child) of nodes in this pick result that implements the interface
        {@link Dragable}. If no such node exists, this method returns null.
        Returns
        --------
        output : Dragable
            the dragable node; null, if none.
        """
    def getSelectableNode(self) -> Selectable:
        """
        Gets a node in this result that is selectable.
        The node returned is the last node in the list (ordered parent to
        child) of nodes in this pick result that implements the interface
        {@link Selectable}. If no such node exists, this method returns null.
        Returns
        --------
        output : Selectable
            the selectable node; null, if none.
        """
    @overload
    def getNode(self, nodeClass: Class) -> Node:
        """
        Gets a node in this result that is an instance of the specified class.
        The node returned is the last node in the list (ordered parent to
        child) of nodes in this pick result that is an instance of the
        specified class. If no such node exists, this method returns null.
        Returns
        --------
        output : Node
            the node; null, if none.
        """
    def getPointLocal(self) -> Point3:
        """
        Gets the picked point in local coordinates.
        Returns
        --------
        output : Point3
            the picked point in local coordinates.
        """
    def getPointWorld(self) -> Point3:
        """
        Gets the picked point in world coordinates.
        Returns
        --------
        output : Point3
            the picked point in world coordinates.
        """
    def getPointPixel(self) -> Point3:
        """
        Gets the picked point in pixel coordinates.
        Returns
        --------
        output : Point3
            the picked point in pixel coordinates.
        """
    def getPixelZ(self) -> double:
        """
        Gets the pixel z (depth) coordinate of the picked point. This depth
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
    def getViewCanvas(self) -> ViewCanvas:
        """
        Gets the canvas for which this pick result was constructed.
        Returns
        --------
        output : ViewCanvas
            the view canvas.
        """
    def getView(self) -> View:
        """
        Gets the view for which this pick result was constructed.
        Returns
        --------
        output : View
            the view.
        """
    def getWorld(self) -> World:
        """
        Gets the world for which this pick result was constructed.
        Returns
        --------
        output : World
            the world.
        """