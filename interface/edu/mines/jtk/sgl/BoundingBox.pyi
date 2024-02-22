from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class BoundingBox:
    """
    An axis-aligned bounding box.
    
    A bounding box may be empty. An empty box contains no points. A non-empty
    box contains at least one point. Some attributes, such as the box minimum
    and maximum points, center, and radius, are defined only for boxes that
    are not empty.
    
    A bounding box may be infinite. An infinite box contains all points.
    Its minimum and maximum points are at Double.NEGATIVE_INFINITY and
    Double.POSITIVE_INFINITY, respectively, and its center is undefined.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an empty bounding box.
        """

    @overload
    def __init__(self, p: Point3) -> None:
        """
        Constructs the smallest bounding box that contains one point.
        
        Parameters
        -----------
        p : Point3
            a point.
        """

    @overload
    def __init__(self, p: Point3, q: Point3) -> None:
        """
        Constructs the smallest bounding box that contains two points.
        The two points represent two of the eight corners of the box.
        
        Parameters
        -----------
        p : Point3
            a point.
        q : Point3
            a point.
        """

    @overload
    def __init__(self, xmin: double, ymin: double, zmin: double, xmax: double,
                 ymax: double, zmax: double) -> None:
        """
        Constructs a bounding box with specified bounds.
        
        Parameters
        -----------
        xmin : double
            the minimum x coordinate.
        ymin : double
            the minimum y coordinate.
        zmin : double
            the minimum z coordinate.
        xmax : double
            the maximum x coordinate.
        ymax : double
            the maximum y coordinate.
        zmax : double
            the maximum z coordinate.
        """

    @overload
    def __init__(self, xyz: Float1D) -> None:
        """
        Constructs a bounding box for points with specified coordinates.
        The (x,y,z) coordinates are packed into the specified array such
        that (xyz[0],xyz[1],xyz[2]) are the (x,y,z) coordinates of the
        1st point, (xyz[3],xyz[4],xyz[5]) are the (x,y,z) coordinates of
        the 2nd point, and so on.
        
        Parameters
        -----------
        xyz : Float1D
            array of packed (x,y,z) coordinates.
        """

    @overload
    def __init__(self, x: Float1D, y: Float1D, z: Float1D) -> None:
        """
        Constructs a bounding box for points with specified coordinates.
        
        Parameters
        -----------
        x : Float1D
            array of x coordinates.
        y : Float1D
            array of y coordinates.
        z : Float1D
            array of z coordinates.
        """

    @overload
    def __init__(self, bb: BoundingBox) -> None:
        """
        Constructs a copy of the specified bounding box.
        
        Parameters
        -----------
        bb : BoundingBox
            the bounding box.
        """

    def isEmpty(self) -> bool:
        """
        Determines whether this box is empty.
        Returns
        --------
        output : bool
            true, if empty; false, otherwise.
        """

    def isInfinite(self) -> bool:
        """
        Determines whether this box is infinite.
        Returns
        --------
        output : bool
            true, if infinite; false, otherwise.
        """

    def getMin(self) -> Point3:
        """
        Gets the point in this box with minimum coordinates.
        Returns
        --------
        output : Point3
            the minimim point.
        """

    def getMax(self) -> Point3:
        """
        Gets the point in this box with maximum coordinates.
        Returns
        --------
        output : Point3
            the maximim point.
        """

    def getCenter(self) -> Point3:
        """
        Gets the point at the center of this box.
        Returns
        --------
        output : Point3
            the box center.
        """

    def getRadius(self) -> double:
        """
        Gets the box radius, the distance from the center to any corner.
        Returns
        --------
        output : double
            the box radius.
        """

    def getRadiusSquared(self) -> double:
        """
        Gets the box radius-squared.
        Returns
        --------
        output : double
            the box radius-squared.
        """

    def getCorner(self, index: int) -> Point3:
        """
        Gets the point at a specified corner of this box.
        The corner is specified by index, an integer between 0 and 7. From
        least to most significant, the three bits of this index correspond
        to x, y, and z coordinates of a corner point. A zero bit selects a
        minimum coordinate; a one bit selects a maximum coordinate.
        
        Parameters
        -----------
        index : int
            the corner index.
        
        Returns
        --------
        output : Point3
            the corner point.
        """

    @overload
    def expandBy(self, p: Point3) -> None:
        """
        Expands this box to include the specified point.
        
        Parameters
        -----------
        p : Point3
            the point.
        """

    @overload
    def expandBy(self, x: double, y: double, z: double) -> None:
        """
        Expands this box to include the point with specified coordinates.
        
        Parameters
        -----------
        x : double
            the point x coordinate.
        y : double
            the point y coordinate.
        z : double
            the point z coordinate.
        """

    @overload
    def expandBy(self, xyz: Float1D) -> None:
        """
        Expands this box to include the points with specified coordinates.
        The (x,y,z) coordinates are packed into the specified array, such
        that (xyz[0],xyz[1],xyz[2]) are the (x,y,z) coordinates of the 1st
        point, (xyz[3],xyz[4],xyz[5]) are the (x,y,z) coordinates of the 2nd
        point, and so on.
        
        Parameters
        -----------
        xyz : Float1D
            array of packed (x,y,z) coordinates.
        """

    @overload
    def expandBy(self, x: Float1D, y: Float1D, z: Float1D) -> None:
        """
        Expands this box to include the points with specified coordinates.
        
        Parameters
        -----------
        x : Float1D
            array of x coordinates.
        y : Float1D
            array of y coordinates.
        z : Float1D
            array of z coordinates.
        """

    @overload
    def expandBy(self, bb: BoundingBox) -> None:
        """
        Expands this box to include the specified bounding box.
        
        Parameters
        -----------
        bb : BoundingBox
            the bounding box.
        """

    @overload
    def expandBy(self, bs: BoundingSphere) -> None:
        """
        Expands this box to include the specified bounding sphere.
        
        Parameters
        -----------
        bs : BoundingSphere
            the bounding sphere.
        """

    @overload
    def contains(self, x: double, y: double, z: double) -> bool:
        """
        Determines whether this box contains the point with specified coordinates.
        
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
            true, if this box contains the point; false, otherwise.
        """

    @overload
    def contains(self, p: Point3) -> bool:
        """
        Determines whether this box contains the specified point.
        
        Parameters
        -----------
        p : Point3
            the point.
        
        Returns
        --------
        output : bool
            true, if this box contains the point; false, otherwise.
        """

    @overload
    def contains(self, bb: BoundingBox) -> bool:
        """
        Determines whether this box contains the specified bounding box.
        
        Parameters
        -----------
        bb : BoundingBox
            the bounding box.
        
        Returns
        --------
        output : bool
            true, if this box contains the specified box; false, otherwise.
        """

    def intersects(self, bb: BoundingBox) -> bool:
        """
        Determines whether this box intersects the specified bounding box.
        
        Parameters
        -----------
        bb : BoundingBox
            the bounding box.
        
        Returns
        --------
        output : bool
            true, if intersects; false, otherwise.
        """

    @staticmethod
    def empty(self) -> BoundingBox:
        """
        Returns a new empty bounding box.
        Returns
        --------
        output : BoundingBox
            a new empty bounding box.
        """

    @staticmethod
    def infinite(self) -> BoundingBox:
        """
        Returns a new infinite bounding box.
        Returns
        --------
        output : BoundingBox
            a new infinite bounding box.
        """

    def toString(self) -> String:
        """
    
        """
