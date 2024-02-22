from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class BoundingSphere:
    """
    A bounding sphere.
    
    A bounding sphere may be empty. An empty sphere contains no points. A
    non-empty sphere contains at least one point. Some attributes, such as
    the sphere center and radius, are defined only for spheres that are not
    empty.
    
    A bounding sphere may be infinite. An infinite sphere contains all points.
    Its radius is Double.POSITIVE_INFINITY, and its center is undefined.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty bounding sphere.
        """

    @overload
    def __init__(self, x: double, y: double, z: double, r: double) -> None:
        """
        Constructs a bounding sphere with specified center and radius.
        
        Parameters
        -----------
        x : double
            the center x coordinate.
        y : double
            the center y coordinate.
        z : double
            the center z coordinate.
        r : double
            the radius; must be non-negative.
        """

    @overload
    def __init__(self, c: Point3, r: double) -> None:
        """
        Constructs a bounding sphere with specified center and radius.
        
        Parameters
        -----------
        c : Point3
            the center.
        r : double
            the radius; must be non-negative.
        """

    @overload
    def __init__(self, bb: BoundingBox) -> None:
        """
        Constructs a bounding sphere that contains the specified bounding box.
        
        Parameters
        -----------
        bb : BoundingBox
            the bounding box.
        """

    @overload
    def __init__(self, bs: BoundingSphere) -> None:
        """
        Constructs a copy of the specified bounding sphere.
        
        Parameters
        -----------
        bs : BoundingSphere
            the bounding sphere.
        """

    def isEmpty(self) -> bool:
        """
        Determines whether this sphere is empty.
        Returns
        --------
        output : bool
            true, if empty; false, otherwise.
        """

    def isInfinite(self) -> bool:
        """
        Determines whether this sphere is infinite.
        Returns
        --------
        output : bool
            true, if infinite; false, otherwise.
        """

    def getCenter(self) -> Point3:
        """
        Gets the sphere center.
        Returns
        --------
        output : Point3
            the center.
        """

    def getRadius(self) -> double:
        """
        Gets the sphere radius.
        Returns
        --------
        output : double
            the radius.
        """

    def getRadiusSquared(self) -> double:
        """
        Gets the sphere radius-squared.
        Returns
        --------
        output : double
            the radius-squared.
        """

    @overload
    def expandBy(self, x: double, y: double, z: double) -> None:
        """
        Expands this sphere to include the point with specified coordinates.
        Adjusts the sphere center to minimize any increase in radius.
        
        Parameters
        -----------
        x : double
            the x coordinate of the point.
        y : double
            the y coordinate of the point.
        z : double
            the z coordinate of the point.
        """

    @overload
    def expandRadiusBy(self, x: double, y: double, z: double) -> None:
        """
        Expands this sphere to include the point with specified coordinates.
        Changes only the radius, if necessary, not the center of this sphere.
        
        Parameters
        -----------
        x : double
            the x coordinate of the point.
        y : double
            the y coordinate of the point.
        z : double
            the z coordinate of the point.
        """

    @overload
    def expandBy(self, p: Point3) -> None:
        """
        Expands this sphere to include the specified point.
        Adjusts the sphere center to minimize any increase in radius.
        
        Parameters
        -----------
        p : Point3
            the point.
        """

    @overload
    def expandRadiusBy(self, p: Point3) -> None:
        """
        Expands this sphere to include the specified point.
        Changes only the radius, if necessary, not the center of this sphere.
        
        Parameters
        -----------
        p : Point3
            the point.
        """

    @overload
    def expandBy(self, bs: BoundingSphere) -> None:
        """
        Expands this sphere to include the specified bounding sphere.
        Adjusts the sphere center to minimize any increase in radius.
        
        Parameters
        -----------
        bs : BoundingSphere
            the bounding sphere.
        """

    @overload
    def expandRadiusBy(self, bs: BoundingSphere) -> None:
        """
        Expands this sphere to include the specified bounding sphere.
        Changes only the radius, if necessary, not the center of this sphere.
        
        Parameters
        -----------
        bs : BoundingSphere
            the bounding sphere.
        """

    @overload
    def expandBy(self, bb: BoundingBox) -> None:
        """
        Expands this sphere to include the specified bounding box.
        Adjusts the sphere center to minimize any increase in radius.
        
        Parameters
        -----------
        bb : BoundingBox
            the bounding box.
        """

    @overload
    def expandRadiusBy(self, bb: BoundingBox) -> None:
        """
        Expands this sphere to include the specified bounding box.
        Changes only the radius, if necessary, not the center of this sphere.
        
        Parameters
        -----------
        bb : BoundingBox
            the bounding box.
        """

    @overload
    def contains(self, x: double, y: double, z: double) -> bool:
        """
        Determines whether this sphere contains a point with specified coordinates.
        
        Parameters
        -----------
        x : double
            the point x coordinate.
        y : double
            the point y coordinate.
        z : double
            the point z coordinate.
        
        Returns
        --------
        output : bool
            true, if this sphere contains the point; false, otherwise.
        """

    @overload
    def contains(self, p: Point3) -> bool:
        """
        Determines whether this sphere contains the specified point.
        
        Parameters
        -----------
        p : Point3
            the point.
        
        Returns
        --------
        output : bool
            true, if this sphere contains the point; false, otherwise.
        """

    @staticmethod
    def empty(self) -> BoundingSphere:
        """
        Returns a new empty bounding sphere.
        Returns
        --------
        output : BoundingSphere
            a new empty bounding sphere.
        """

    @staticmethod
    def infinite(self) -> BoundingSphere:
        """
        Returns a new infinite bounding sphere.
        Returns
        --------
        output : BoundingSphere
            a new infinite bounding sphere.
        """

    def toString(self) -> String:
        """
    
        """
