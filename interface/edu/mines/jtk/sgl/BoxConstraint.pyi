from typing import overload
from edu.mines.jtk.mapping import *


class BoxConstraint:
    """
    A constraint for objects that must lie inside an axis-aligned box.
    """

    @overload
    def __init__(self, box: BoundingBox) -> None:
        """
        Constructs a box constraint with specified bounding box.
        Constrains objects to lie inside the bounding box.
        
        Parameters
        -----------
        box : BoundingBox
            bounding box.
        """

    @overload
    def __init__(self, box: BoundingBox, dxmin: double, dymin: double,
                 dzmin: double) -> None:
        """
        Constructs a box constraint with specified bounding box and min sizes.
        Constrains objects to lie inside the bounding box.
        
        Parameters
        -----------
        box : BoundingBox
            bounding box.
        dxmin : double
            minimum size in x dimension.
        dymin : double
            minimum size in y dimension.
        dzmin : double
            minimum size in z dimension.
        """

    @overload
    def __init__(self, p: Point3, q: Point3) -> None:
        """
        Constructs a box constraint with specified corner points.
        Constrains objects to lie inside a box defined by the corner points.
        
        Parameters
        -----------
        p : Point3
            a corner point.
        q : Point3
            a corner point.
        """

    @overload
    def __init__(self, p: Point3, q: Point3, dxmin: double, dymin: double,
                 dzmin: double) -> None:
        """
        Constructs a box constraint with specified corner points and min sizes.
        Constrains objects to lie inside a box defined by the corner points.
        
        Parameters
        -----------
        p : Point3
            a corner point.
        q : Point3
            a corner point.
        dxmin : double
            minimum size in x dimension.
        dymin : double
            minimum size in y dimension.
        dzmin : double
            minimum size in z dimension.
        """

    @overload
    def __init__(self, sx: Sampling, sy: Sampling, sz: Sampling) -> None:
        """
        Constructs a box constraint with specified samplings.
        Constrains objects vertices to lie on the sampling grid.
        
        Parameters
        -----------
        sx : Sampling
            sampling of x coordinate
        sy : Sampling
            sampling of y coordinate
        sz : Sampling
            sampling of z coordinate
        """

    @overload
    def __init__(self, sx: Sampling, sy: Sampling, sz: Sampling, dxmin: double,
                 dymin: double, dzmin: double) -> None:
        """
        Constructs a box constraint with specified samplings and min sizes.
        Constrains object vertices to lie on the sampling grid.
        
        Parameters
        -----------
        sx : Sampling
            sampling of x coordinate
        sy : Sampling
            sampling of y coordinate
        sz : Sampling
            sampling of z coordinate
        dxmin : double
            minimum size in x dimension.
        dymin : double
            minimum size in y dimension.
        dzmin : double
            minimum size in z dimension.
        """

    def getBoundingBox(self) -> BoundingBox:
        """
        Gets the bounding box for this constraint.
        Returns
        --------
        output : BoundingBox
            the bounding box.
        """

    def getBoundingSphere(self) -> BoundingSphere:
        """
        Gets the bounding sphere for this constraint.
        Returns
        --------
        output : BoundingSphere
            the bounding sphere.
        """

    def containsPoint(self, p: Point3) -> bool:
        """
        Determines whether this box constraint contains the specified point.
        
        Parameters
        -----------
        p : Point3
            the point
        
        Returns
        --------
        output : bool
            true, if this box contains the point; false, otherwise.
        """

    def constrainPoint(self, p: Point3) -> None:
        """
        Constrains a specified point.
        
        Parameters
        -----------
        p : Point3
            the point.
        """

    def constrainBox(self, p: Point3, q: Point3) -> None:
        """
        Constrains a box defined by two specified corner points. If necessary,
        modifies either or both of the points to satisfy this constraint.
        
        Parameters
        -----------
        p : Point3
            a corner point
        q : Point3
            a corner point
        """
