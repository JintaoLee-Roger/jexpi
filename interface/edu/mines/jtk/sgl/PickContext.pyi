from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class PickContext:
    """
    A transform context for picking.
    
    A pick context has a pick segment, which is a line segment in a local
    coordinate system. During a pick traversal of the scene graph, nodes
    compute points of intersection, if any, between their geometry and
    the pick segment. For efficiency, only nodes with bounding spheres that
    intersect the pick segment will perform intersection computations.
    
    The pick segment in a pick context has two endpoints. One endpoint lies
    on the near clipping plane, with specified pixel (x,y) coordinates and
    pixel z coordinate 0.0. This endpoint is called the <em>near</em>
    endpoint of the pick segment. The <em>far</em> endpoint lies on the far
    clipping plane. It has the same specified pixel (x,y) coordinates as
    the near endpoint, but has pixel z coordinate 1.0. With these pick
    segment endpoints, only geometry between the near and far clipping
    planes can be picked.
    """

    def __init__(self, event: MouseEvent) -> None:
        """
        Constructs a pick context for the specified mouse event.
        
        Parameters
        -----------
        event : MouseEvent
            the mouse event.
        """

    def getMouseEvent(self) -> MouseEvent:
        """
        Gets the mouse event for which this context was constructed.
        Returns
        --------
        output : MouseEvent
            the mouse event.
        """

    def getPickSegment(self) -> Segment:
        """
        Gets the pick segment for this context. Endpoint A of the segment lies
        on the near clipping plane; endpoint B lies on the far clipping plane.
        Returns
        --------
        output : Segment
            the pick segment.
        """

    def segmentIntersectsSphereOf(self, node: Node) -> bool:
        """
        Determines whether the pick segment intersects the bounding sphere
        of the specified node.
        false, otherwise.
        
        Parameters
        -----------
        node : Node
            the node with a bounding sphere.
        
        Returns
        --------
        output : bool
            true, if the pick segment intersects the bounding sphere;
        """

    def addResult(self, point: Point3) -> None:
        """
        Adds a pick result with specified pick point to this context.
        
        Parameters
        -----------
        point : Point3
            the pick point, in local coordinates.
        """

    def getClosest(self) -> PickResult:
        """
        Gets the pick result closest to the origin of the pick segment.
        Returns
        --------
        output : PickResult
            the pick result; null, if none.
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
