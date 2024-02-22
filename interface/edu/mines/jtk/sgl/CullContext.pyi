from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class CullContext:
    """
    A context for view frustum culling.
    
    A cull context has a draw list, in which it accumulates copies of
    its node stack. Typically, a leaf node copies the node stack to the
    draw list when its bounding sphere intersects the view frustum of
    the cull context.
    """

    def __init__(self, canvas: ViewCanvas) -> None:
        """
        Constructs a transform context for the specified view canvas.
        
        Parameters
        -----------
        canvas : ViewCanvas
            the view canvas.
        """

    def frustumIntersectsSphereOf(self, node: Node) -> bool:
        """
        Determines whether the view frustrum intersects the bounding sphere
        of the specified node.
        false, otherwise.
        
        Parameters
        -----------
        node : Node
            the node with a bounding sphere.
        
        Returns
        --------
        output : bool
            true, if the view frustum intersects the bounding sphere;
        """

    def appendNodes(self) -> None:
        """
        Appends the node stack to the draw list in this context.
        """

    def getDrawList(self) -> DrawList:
        """
        Gets the draw list accumulated in this context.
        Returns
        --------
        output : DrawList
            the draw list.
        """

    def pushNode(self, node: Node) -> None:
        """
        Saves the current node, and then makes the specified node current.
        
        Parameters
        -----------
        node : Node
            the new current node.
        """

    def popNode(self) -> None:
        """
        Restores the most recently saved (pushed) node.
        Discards the current node.
        """

    def pushLocalToWorld(self, transform: Matrix44) -> None:
        """
        Saves the local-to-world transform before appending a transform.
        The specified transform matrix is post-multiplied with the current
        local-to-world transform, such that the specified transform is applied
        first when transforming local coordinates to world coordinates.
        
        Parameters
        -----------
        transform : Matrix44
            the transform to append.
        """

    def popLocalToWorld(self) -> None:
        """
        Restores the most recently saved (pushed) local-to-world transform.
        Discards the current local-to-world transform.
        """
