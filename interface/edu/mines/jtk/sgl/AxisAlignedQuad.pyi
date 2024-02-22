from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class AxisAlignedQuad:
    """
    An axis-aligned quad has one frame that contains one or more panels.
    The quad is constrained to lie within a box specified by two corner
    points.
    """

    def __init__(self, axis: Axis, qa: Point3, qb: Point3) -> None:
        """
        Constructs an axis-aligned quad with specified axis and corner points.
        
        Parameters
        -----------
        axis : Axis
            the axis orthogonal to the plane of this quad.
        qa : Point3
            a corner point.
        qb : Point3
            a corner point.
        """

    def getFrame(self) -> AxisAlignedFrame:
        """
        Gets the frame for this quad.
        Returns
        --------
        output : AxisAlignedFrame
            the frame.
        """

    @overload
    def dragBegin(self, dc: DragContext) -> None:
        """
    
        """

    @overload
    def drag(self, dc: DragContext) -> None:
        """
    
        """

    @overload
    def dragEnd(self, dc: DragContext) -> None:
        """
    
        """
