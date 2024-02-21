from typing import overload
from edu.mines.jtk.mapping import *


class AxisAlignedFrame:
    """
    An axis-aligned frame is a group of axis-aligned panels. A frame's
    geometry is an axis-aligned quadrilateral defined by an axis and two
    corner points. The axis is perpendicular to the plane containing the
    quadrilateral. The corner points are a pair of opposite vertices of
    the quadrilateral. Each corner point has three (X,Y,Z) coordinate
    values. For the axis that is orthogonal to the plane of this frame,
    the corresponding coordinate values of the two corner points are equal.
    
    By convention, axis-aligned panel children of axis-aligned frames
    honor their parent frame's geometry when drawing, picking, etc. This
    convention keeps multiple panel children consistent as their frame is
    moved and resized.
    
    Panels do not typically control the geometry of their frame, but
    they may set a box constraint on the corner points of that frame.
    For example, a panel may constrain those corner points to lie on a
    sampling grid. Only one constraint, the last one set, is applied. A
    frame does not attempt to reconcile inconsistent constraints.
    """

    def __init__(self, axis: Axis, pa: Point3, pb: Point3) -> None:
        """
        Constructs a frame with specified axis and corner points.
        
        Parameters
        -----------
        axis : Axis
            the axis.
        pa : Point3
            a corner point.
        pb : Point3
            a corner point.
        """

    def getAxis(self) -> Axis:
        """
        Gets the axis for this frame.
        Returns
        --------
        output : Axis
            the axis.
        """

    def getCornerMin(self) -> Point3:
        """
        Gets the minimum corner point for this frame.
        Returns
        --------
        output : Point3
            the minimum corner point.
        """

    def getCornerMax(self) -> Point3:
        """
        Gets the maximum corner point for this frame.
        Returns
        --------
        output : Point3
            the maximum corner point.
        """

    def getCorner(self, index: int) -> Point3:
        """
        Gets the corner point with specified index for this frame.
        
        Parameters
        -----------
        index : int
            the index in [0,3].
        
        Returns
        --------
        output : Point3
            the corner point.
        """

    def setCorners(self, pa: Point3, pb: Point3) -> None:
        """
        Sets the corner points of (moves and/or resizes) this frame.
        If this frame has a non-null box constraint, then this method
        first applies the constraint before settig the corner points.
        
        The specified corner points must be opposite vertices of the
        quadrilateral that defines this frame. For the axis that is
        orthogonal to the plane of this frame, the corresponding (X,
        Y, or Z) coordinate values of the two points should be equal;
        this method moves this frame to the average of those two
        coordinate values.
        
        Parameters
        -----------
        pa : Point3
            a corner point
        pb : Point3
            a corner point
        """

    def getBoxConstraint(self) -> BoxConstraint:
        """
        Gets the box constraint for this frame.
        Returns
        --------
        output : BoxConstraint
            the box constraint; null, if none.
        """

    def setBoxConstraint(self, constraint: BoxConstraint) -> None:
        """
        Sets the box constraint for this frame. Typically, only panels in a
        frame call this method, because the constraint often depends on what
        is drawn by those panels. This frame uses only the last constraint set.
        
        Parameters
        -----------
        constraint : BoxConstraint
            the box constraint.
        """

    def addChild(self, node: Node) -> None:
        """
    
        """

    def removeChild(self, node: Node) -> None:
        """
    
        """
